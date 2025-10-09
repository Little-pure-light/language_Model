from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.supabase_handler import get_supabase_client
from backend.openai_handler import get_openai_client, generate_response
from backend.prompt_engine import PromptEngine
from modules.memory_system import MemorySystem

router = APIRouter()

class ChatRequest(BaseModel):
    user_message: str
    conversation_id: str
    user_id: str = "default_user"

class ChatResponse(BaseModel):
    assistant_message: str
    emotion_analysis: dict
    conversation_id: str

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """處理聊天請求"""
    try:
        supabase = get_supabase_client()
        openai_client = get_openai_client()
        memories_table = os.getenv("SUPABASE_MEMORIES_TABLE", "xiaochenguang_memories")
        
        memory_system = MemorySystem(supabase, openai_client, memories_table)
        prompt_engine = PromptEngine(request.conversation_id, supabase, memories_table)
        
        recalled_memories = await memory_system.recall_memories(
            request.user_message, 
            request.conversation_id
        )
        
        conversation_history = memory_system.get_conversation_history(
            request.conversation_id, 
            limit=5
        )
        
        messages, emotion_analysis = prompt_engine.build_prompt(
            request.user_message,
            recalled_memories,
            conversation_history
        )
        
        assistant_message = await generate_response(
            openai_client,
            messages,
            model="gpt-4o-mini",
            max_tokens=1000,
            temperature=0.8
        )
        
        await memory_system.save_memory(
            request.conversation_id,
            request.user_message,
            assistant_message,
            emotion_analysis,
            ai_id=os.getenv("AI_ID", "xiaochenguang_v1")
        )
        
        await memory_system.save_emotional_state(
            request.user_id,
            emotion_analysis,
            context=request.user_message
        )
        
        prompt_engine.personality_engine.learn_from_interaction(
            request.user_message,
            assistant_message,
            emotion_analysis
        )
        prompt_engine.personality_engine.save_personality()
        
        return ChatResponse(
            assistant_message=assistant_message,
            emotion_analysis=emotion_analysis,
            conversation_id=request.conversation_id
        )
        
    except Exception as e:
        print(f"❌ Chat error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
