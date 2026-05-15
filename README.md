# Unstructured Data Pipeline & Remote MCP Server

本專案實作了一套完整的數據工程工作流，旨在將企業內部雜亂的非結構化技術文件（如 PDF、PPTX）轉化為結構化的知識庫，並透過傳統 **REST API** 與現代化 **MCP (Model Context Protocol)** 協議提供給 AI Agent 使用。

---

## 🚀 核心功能
* **自動化數據管道 (Data Pipeline)**：自動提取 PDF 與 PPTX 中的技術細節，並進行文本清洗與元數據 (Metadata) 標註。
* **雙重存取介面**：
    * **FastAPI**：提供高效能的傳統 RESTful 介面，方便現有軟體系統整合。
    * **MCP 伺服器**：採用 Anthropic 最新推廣的協議，讓 LLM Agent（如 Claude）能像使用內建工具一樣直接檢索私有數據。
* **專業工程標準**：建立完整的虛擬環境管理、`.gitignore` 排除機制與 `requirements.txt` 依賴管理，確保環境可重現性。

## 🏗️ 系統架構
本專案分為四個主要模組：
1.  **數據模擬 (`make_data.py`)**：自動產生模擬的企業技術規格書，用於模擬真實世界中的數據雜訊與複雜格式。
2.  **數據提取 (`ingest.py`)**：核心處理引擎，負責解析文件、清洗異常文字，並將數據結構化為 JSON 格式。
3.  **後端服務 (`main.py`)**：基於 FastAPI 的 API 伺服器，提供結構化查詢與數據檢索端點。
4.  **AI 工具化 (`mcp_server.py`)**：將知識庫封裝為 MCP 工具，讓 AI 代理具備主動獲取私有上下文的能力。

## 🛠️ 技術棧
* **開發語言**：Python 3.10+
* **網頁框架**：FastAPI & Uvicorn
* **AI 協議**：FastMCP (Anthropic MCP SDK)
* **文件處理**：PyPDF, python-pptx
* **版本控制**：Git

## 📦 快速開始

### 1. 環境架設
```powershell
# 建立虛擬環境
python -m venv .venv

# 啟動虛擬環境 (Windows)
.\.venv\Scripts\activate

# 安裝依賴套件
pip install -r requirements.txt
```
### 2. 執行流程
```powershell
# 步驟 1：產生模擬數據
python make_data.py

# 步驟 2：執行數據處理管道
python ingest.py

# 步驟 3：啟動伺服器
python -m uvicorn main:app --reload
```

### 3. 驗證與測試
* **API 文檔**：啟動後可訪問 http://127.0.0.1:8000/docs 使用 Swagger UI 進行互動式測試。
* **MCP 整合**：可使用 MCP Inspector 驗證伺服器是否能被 AI 工具正確調用。

## 📸 成果展示
### 1. 伺服器啟動
使用 FastAPI 與 Uvicorn 成功運行服務。
<img width="1702" height="312" alt="image" src="https://github.com/user-attachments/assets/632a6dab-3e80-4e91-a839-f4e893c8d63f" />

### 2. API 功能驗證
透過 Swagger UI 驗證非結構化數據提取至結構化知識庫的查詢結果。
<img width="2690" height="1242" alt="image" src="https://github.com/user-attachments/assets/cdbbd7ab-3b3c-422e-8fa6-0ed57a184c98" />

