#!/bin/bash

echo "🚀 啟動小宸光 AI 靈魂系統..."
echo ""

# 創建日誌目錄
mkdir -p logs

# 啟動後端 API
echo "📡 啟動後端 API (Port 8000)..."
cd backend && uvicorn main:app --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!
echo "✅ 後端 PID: $BACKEND_PID"
cd ..

# 等待後端啟動
sleep 3

# 檢查後端是否運行
if curl -s http://localhost:8000/docs > /dev/null 2>&1; then
    echo "✅ 後端 API 運行成功!"
    echo "   API 文檔: http://localhost:8000/docs"
else
    echo "❌ 後端啟動失敗,請檢查日誌"
    exit 1
fi

echo ""
echo "🎨 啟動前端介面 (Port 5000)..."
cd frontend && npm run dev -- --host 0.0.0.0 --port 5000 &
FRONTEND_PID=$!
echo "✅ 前端 PID: $FRONTEND_PID"
cd ..

echo ""
echo "=== 系統已啟動 ==="
echo ""
echo "📍 前端介面: http://localhost:5000"
echo "📍 API 文檔: http://localhost:8000/docs"
echo ""
echo "💡 提示:"
echo "   - 查看測試指南: cat TEST_GUIDE.md"
echo "   - 停止服務: pkill -f 'uvicorn\|vite'"
echo ""
