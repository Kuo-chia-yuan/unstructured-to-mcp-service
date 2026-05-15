import json
from fastapi import FastAPI, HTTPException
from typing import List, Optional

app = FastAPI(title="Raydium AI Knowledge Base API")

# 讀取剛剛處理好的數據
def load_data():
    try:
        with open("data/processed/knowledge_base.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.get("/")
def read_root():
    return {"message": "Welcome to Raydium AI Knowledge Base API"}

@app.get("/query")
def query_knowledge(q: str):
    """根據關鍵字查詢規格數據"""
    data = load_data()
    # 簡單的關鍵字比對
    results = [item for item in data if q.lower() in item["content"].lower()]
    
    if not results:
        raise HTTPException(status_code=404, detail="No matching technical data found.")
    
    return {"query": q, "results": results}

@app.get("/files")
def list_files():
    """列出目前已處理的所有文件清單"""
    data = load_data()
    return {"files": [item["source"] for item in data]}