from mcp.server.fastmcp import FastMCP
import json

# 建立一個 FastMCP 實例
mcp = FastMCP("Raydium Knowledge Base")

@mcp.tool()
def search_ic_specs(query: str) -> str:
    """搜尋瑞鼎 IC 規格書與技術文件的內容"""
    with open("data/processed/knowledge_base.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # 執行搜尋邏輯
    results = [item["content"] for item in data if query.lower() in item["content"].lower()]
    
    if not results:
        return "未找到相關規格資料。"
    
    return "\n---\n".join(results)

if __name__ == "__main__":
    print("--- 瑞鼎 AI 知識庫 MCP Server 啟動中 ---")
    print("模式：STDIO (等待 AI Agent 連接...)")
    mcp.run()