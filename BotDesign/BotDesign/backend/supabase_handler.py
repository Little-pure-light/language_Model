import os
from supabase import create_client, Client
import logging

logger = logging.getLogger("supabase_handler")

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_ANON_KEY = os.environ.get("SUPABASE_ANON_KEY")

_supabase: Client = None

def get_supabase() -> Client:
    """獲取 Supabase 客戶端實例（單例模式）。"""
    global _supabase
    if _supabase is None:
        if not SUPABASE_URL or not SUPABASE_ANON_KEY:
            logger.warning("⚠️ SUPABASE_URL 或 SUPABASE_ANON_KEY 環境變數未設置。某些功能將不可用。")
            logger.warning("請在 Replit Secrets 中設置這些環境變數以啟用完整功能。")
            return None
        _supabase = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)
    return _supabase
