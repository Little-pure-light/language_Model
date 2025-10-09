# 小宸光 AI 靈魂系統 Web 版

## 專案概述
從 Telegram Bot 完整移植至 Vue 3 + FastAPI + Supabase 架構的 AI 對話系統,保留所有記憶、情感與人格功能。

## 技術架構

### 後端 (Python + FastAPI)
- **框架**: FastAPI
- **端口**: 8000
- **核心模組**:
  - `XiaoChenGuangSoul`: 小宸光靈魂設定與個性系統
  - `PersonalityEngine`: 人格引擎,從互動中學習
  - `EnhancedEmotionDetector`: 情感偵測系統
  - `MemorySystem`: 記憶檢索與儲存系統

### 前端 (Vue 3)
- **框架**: Vue 3 + Vite
- **端口**: 5000
- **功能**:
  - 即時對話介面
  - 記憶列表顯示
  - 情緒狀態視覺化
  - 檔案上傳功能

### 資料庫 (Supabase)
- **xiaochenguang_memories** 表格:儲存對話記憶
- **emotional_states** 表格:追蹤情緒狀態

## 專案結構

```
/
├── backend/                 # FastAPI 後端
│   ├── main.py             # 主應用入口
│   ├── chat_router.py      # 聊天 API
│   ├── memory_router.py    # 記憶管理 API
│   ├── file_upload.py      # 檔案上傳 API
│   ├── openai_handler.py   # OpenAI 整合
│   ├── supabase_handler.py # Supabase 整合
│   ├── prompt_engine.py    # 提示語引擎
│   └── requirements.txt    # Python 依賴
│
├── frontend/               # Vue 3 前端
│   ├── src/
│   │   ├── App.vue        # 主應用
│   │   ├── components/
│   │   │   └── ChatInterface.vue  # 聊天介面
│   │   └── main.js
│   ├── vite.config.js
│   └── package.json
│
├── modules/               # 核心靈魂模組
│   ├── emotion_detector.py    # 情感偵測
│   ├── soul.py               # 靈魂設定
│   ├── personality_engine.py # 人格引擎
│   ├── memory_system.py      # 記憶系統
│   └── file_handler.py       # 檔案處理
│
├── config/                # 配置檔案
│   └── .env.example
│
└── profile/              # 個性設定
    └── user_profile.json
```

## 環境變數

- `OPENAI_API_KEY`: OpenAI API 金鑰
- `SUPABASE_URL`: Supabase 專案 URL
- `SUPABASE_KEY`: Supabase 服務金鑰
- `SUPABASE_MEMORIES_TABLE`: 記憶表格名稱 (xiaochenguang_memories)
- `AI_ID`: AI 個體識別碼 (xiaochenguang_v1)

## 核心功能

### 1. 情感偵測系統
- 支援 9 種情緒:joy, sadness, anger, fear, love, tired, confused, grateful, neutral
- 強度分析與信心度計算
- 自動調整回應風格

### 2. 記憶系統
- 向量化記憶檢索 (OpenAI embeddings)
- 記憶重要性評分
- 存取次數追蹤
- 對話歷史管理

### 3. 人格引擎
- 從互動中學習個性特質
- 情感檔案記錄
- 知識領域追蹤
- 動態人格調整

### 4. 檔案上傳
- Supabase Storage 整合
- 檔案記錄關聯

## 啟動指令

### 後端
```bash
cd backend && python main.py
```

### 前端
```bash
cd frontend && npm run dev
```

## API 端點

- `POST /api/chat`: 對話接口
- `GET /api/memories/{conversation_id}`: 獲取記憶
- `GET /api/emotional-states/{user_id}`: 獲取情緒狀態
- `POST /api/upload`: 檔案上傳

## 最近更新

- 2025-10-08: 完成從 Telegram Bot 到 Web 版本的完整移植
- 保留所有核心功能:記憶、情感、人格系統
- 實現 Vue 3 即時對話介面
- 整合 Supabase 資料庫與 Storage
- 升級依賴版本: supabase 2.21.1, realtime 2.21.1, websockets 15.0.1, pydantic 2.12.0

## 開發備註

- 前端使用 proxy 轉發 API 請求到後端
- 情感分析結果會即時顯示在介面
- 記憶系統支援向量搜尋(需要 Supabase RPC function)
- 所有功能邏輯與原 bot.py 完全一致

## 資料庫設置

**重要**: 首次使用前,必須設置 Supabase 資料表結構。詳見 `DATABASE_SETUP.md`

必要資料表:
1. **xiaochenguang_memories** - 儲存對話記憶 (欄位: assistant_mes, embedding, importance_score, access_count 等)
2. **emotional_states** - 追蹤情緒狀態 (欄位: emotion, intensity, confidence, timestamp 等)
3. **match_memories** RPC 函數 - 向量相似度搜尋

常見問題:
- 如遇到 "column assistant_mes does not exist" 錯誤,請參考 DATABASE_SETUP.md 中的資料表建立 SQL
- 需要啟用 pgvector 擴充來支援向量嵌入功能

## 依賴版本

### Python (backend/requirements.txt)
- fastapi==0.115.6
- uvicorn[standard]==0.34.0
- supabase==2.21.1
- openai==1.58.1
- pydantic==2.12.0
- realtime==2.21.1
- websockets==15.0.1

### Node.js (frontend/package.json)
- vue@^3.5.13
- axios@^1.7.9
- vite@^6.0.3
