[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/adity-star-mcp-yfinance-server-badge.png)](https://mseep.ai/app/adity-star-mcp-yfinance-server)

# 💹 MCP YFinance Stock Server
![Python](https://img.shields.io/badge/python-3.10-blue)
![MCP](https://img.shields.io/badge/MCP-Compatible-green)
![License](https://img.shields.io/github/license/Adity-star/mcp-yfinance-server)


This project sets up a **stock Price server** powered by the **Yahoo Finance (YFinance)** API and built for seamless integration with **MCP (Model Control Protocol)**.

It allows AI agents or clients to:
- Retrieve real-time stock data
- Manage a watchlist
- Perform full stock analysis
- Run full technical indicators
- And much more


![image](https://github.com/user-attachments/assets/b7f27442-823e-45a1-8f57-e0f6282ee36f)

---
## 🪙 Start Simple: Build a Crypto Price Tracker First
Before diving into the full-blown stock server, I recommend starting with this simple crypto tracker built with Python + MCP 👇

🔗 GitHub Repo:
https://github.com/Adity-star/mcp-crypto-server

> You'll learn how to:
> - Use MCP to expose crypto tools like get_price("BTC")
> - Build an API with FastAPI
> - Fetch real-time prices using the Alpaca API

## 🔗 Related Projects
Explore more of my work:
-  [GenAI-Learnings](https://github.com/Adity-star/GenAI-Learnings): A deep dive into Generative AI concepts, tools, and projects.
-  [LangChain-Mastery](https://github.com/Adity-star/LangChainMastery): Everything you need to master LangChain for building powerful LLM applications.
-  [Complete Data Science](https://github.com/Adity-star/Complete-DataScience-Guide):  A deep dive into Data Science AI concepts, tools, and projects and all the material for learning and interview preparation.
-  [Reinforcement-Learning](https://github.com/Adity-star/Reinforcement-Learning): Hands-on experiments and theory in Reinforcement Learning.
-  [CompleteRAG](https://github.com/Adity-star/CompleteRAG): End-to-end implementation of Retrieval-Augmented Generation (RAG) systems.
---
## 📈 Then Level Up: Build the yFinance Stock Server
Once you're familiar with the flow, move on to this more advanced stock tracker 💹

🔗 GitHub Repo:
[https://github.com/Adity-star/mcp-yfinance-server](https://github.com/Adity-star/mcp-yfinance-server)

📝 Detailed Blog:
👉 [How I Built My Own Stock Server with Python, yFinance, and a Touch of Nerdy Ambition](https://medium.com/@aakuskar.980/how-i-built-my-own-stock-server-with-python-yfinance-and-a-touch-of-nerdy-ambition-b562dc1d7b93)

> Includes:
> - Watchlists
> - Real-time(ish) price updates
> - Technical summaries
> - A full-featured dashboard
> - Trend + momentum indicators
> - Watchlist management

---

## 📦 Step 1: Set Up the Environment (with uv)

We use **[uv](https://github.com/astral-sh/uv)** — a modern, ultra-fast Python package manager — to manage our project environment.

### 🛠️ Installation & Setup

Run the following commands in your terminal:

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh 

# Create and navigate to your project directory
mkdir mcp-yfinance-server
cd mcp-yfinance-server

# Initialize a new project
uv init

# Create and activate the virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

```
## 📥 Install the project
Once your [pyproject.toml](https://github.com/Adity-star/mcp-yfinance-server/blob/main/pyproject.toml) is set up with dependencies, run: 
```bash
#  Run 
uv pip install -e .

```

---
## 🚀 Step 2: Running the MCP Server
Once your environment is ready, start the stock server:
```bash
uv run main.py
```
🧪 Want a quick test first?
Try checking the tools first:
```bash
python run test_server_fun.py
```

📄 Curious how the full server works?

Explore the source code here: 

🔗 [yf_server.py › GitHub](https://github.com/Adity-star/mcp-yfinance-server/blob/main/source/yf_server.py)


---

# 🛠️ MCP Tool Reference

The server exposes many tools for AI agents and CLI users.  
Here are some important tools, check out the complete tools list [here](https://github.com/Adity-star/mcp-yfinance-server/blob/main/results/tools.md):


## 📦 Tool List

| Tool Name                      | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| `add_to_watchlist`            | Add a stock ticker to your personal watchlist.                             |
| `analyze_stock`       |Perform a 1-month technical trend analysis (RSI, MACD, MAs)..                                        |
| `get_technical_summary`               |Generate a comprehensive technical summary including indicators & signals..                             |
| `get_watchlist_prices`        | Fetch the most recent prices for all watchlisted tickers.                  |
| `get_trend_analysiss` | Analyze recent trend shifts, patterns, and divergences..                              |
| `get_stock_price`             | Retrieve the current price for a given ticker symbol.                      |
| `get_volatility_analysis`           |  Calculate historical volatility and ATR metrics..                 |
| `compare_stocks`              | Compare two stock prices (useful for relative performance analysis).       |


> ✅ [Total: 18 powerful tools to analyze and monitor stocks with precision.](https://github.com/Adity-star/mcp-yfinance-server/blob/main/results/tools.md)

## 🧠 Use Cases

These tools are ideal for:
- 📊 Dynamic watchlist management
- 🔁 Trend and momentum detection
- 📈 Deep-dive technical analysis for investment decisions
- ⚠️ Volatility-based risk assessment
- 🤖 Powering stock-focused autonomous agents or dashboards


> ⚙️ Keep this reference handy for building intelligent financial applications with the MCP server.

---

## 🔍 Step 3: Inspecting the MCP Server

Easily explore and test your MCP tools using the **MCP Server Inspector**.
Run the following command in your terminal:

```bash
$ mcp dev source/yf_server.py
```
This launches an interactive UI to:
- 🧰 View all available tools and resources
- 📥 Test input/output for each tool
- 📡 Monitor real-time responses from your server
- 
![image](https://github.com/user-attachments/assets/886182a3-e996-4713-aec6-d9ab3fac3bd9)

---

## ⚙️ Step 4: Configure Your MCP Server

To integrate your YFinance MCP server, add the following entry to your mcp.config.json file:

```json
{
  "mcpServers": {
    "yfinance-price-tracker": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/YOUR/mcp-yfinance-server",
        "run",
        "main.py"
      ]
    }
  }
}
```
> ⚠️ Replace /ABSOLUTE/PATH/TO/... with actual file paths.
> 💡 Tip: Rename your server from crypto-price-tracker to yfinance-price-tracker for clarity.

---
## 🔁 Step 5: Restart Claude Desktop

Restart **Claude Desktop** (or any interface that uses MCP) to reload and activate your new YFinance tools.
> This ensures the updated MCP configuration is recognized and all stock tracking tools are 
 ready to use.

---
## ✅ Step 6: Testing the MCP Server with Claude Desktop

- With everything installed and configured, you're ready to test your MCP server in **Claude Desktop**.

Use these example queries to test your MCP YFinance Server in action:

> "Compare the stock prices of Tesla and Apple."
> → 🔧 Uses `compare_stocks`

> "Get the historical data for Tesla over the past month."
> → 📊 Uses `get_stock_history`

> "Add Apple, Tesla, and Reliance to my watchlist."
> → 📋 Uses `add_to_watchlist`

> "Show me a chart of Apple’s stock over the last 30 days."
> → 🖼️ Claude can fetch + visualize data using your server

📷 Sample Chart:
🖼 [view Screenshot](https://github.com/Adity-star/mcp-yfinance-server/blob/main/assets/Screenshot%20(16).png)

🌐 Live Claude Site:
[Open Demo on Claude.site](https://claude.site/artifacts/bba1b878-de53-4988-a0b5-377f2d202b3a)

🧪 These tests ensure your MCP integration is working end-to-end—from data retrieval to real-time analysis and visualization.

---

# 📊 Results

## ⚙️ Outcomes You Can Expect

| Feature                                                                 | Outcome                                                                 |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| ✅ [**Stock Analysis**](https://claude.site/artifacts/a118060f-25ac-410b-ae37-0869dc773a98)              | Analyse stock giving price, OHLC, returns, volume, insights and data.  |
| 📈 [**Technical Analysis**](https://claude.site/artifacts/4642c157-8022-43b7-a2cd-472437c62e4b)          | Access indicators like RSI, MACD, MA, and a complete technical summary.|
| 📉 [**Volatility Reports**](https://claude.site/artifacts/08214360-f08f-48d7-9cb1-1bc7334910e9)          | Analyze stock risk with ATR and volatility metrics.                    |
| 🔍 [**Trend Analysis**](https://claude.site/artifacts/878fc17e-a845-4944-b2ee-14857da2bbfc)              | Detect trend shifts and divergence using price movement analysis.      |
| 🧠 [**Visualisations**](https://claude.site/artifacts/4642c157-8022-43b7-a2cd-472437c62e4b)              | 18+ tools ready to power AI agents or dashboards to visualise stock.                      |
| 📋 [**Technical Charts**](https://claude.site/artifacts/559bf977-91dc-45e1-a6b7-e95a19eaaeab)            | Analyse and monitor technical indicators for stocks in real-time.      |
| 🖼️ [**Visual Insights**](https://claude.site/artifacts/bba1b878-de53-4988-a0b5-377f2d202b3a)            | Generate charts and visual summaries with Claude Desktop.              |


> 🎉 Ready to build your stock-tracking bot or intelligent financial dashboard? This project has all the core pieces.

---

## 📫 Feedback & Contributions
Contributions are welcome! Whether you're fixing bugs, adding features, or improving documentation, your help makes this project better.

### 🐛 Reporting Issues

If you encounter bugs or have suggestions, please open an issue in the [Issues section](https://github.com/Adity-star/mcp-yfinance-server/issues). Be sure to include:

- ✅ Steps to reproduce (if applicable)  
- 🔍 Expected vs. actual behavior  
- 📷 Screenshots or error logs (if relevant)  

### 📬 Submit a Pull Request

Have a fix or improvement? Head over to the [Pull Requests section](https://github.com/Adity-star/mcp-yfinance-server/pulls) and submit your PR. We’ll review and merge it ASAP!

---
## 💬 Spread the Word
If this project saved you from API rate limits or overpriced SaaS tools...


- 🌟 **Star** the repo  
- 🍴 **Fork** it and build your own crypto/stock tool  
- 📲 **Tag me on X** [@AdityaAkuskar](https://x.com/AdityaAkuskar) — I’d love to see what you build!  
- 🔗 **Connect with me on [LinkedIn](https://www.linkedin.com/in/aditya-a-27b43533a/)**  
---

## 📜 License

[MIT © 2025 Ak Aditya](https://github.com/Adity-star/mcp-yfinance-server/blob/main/LICENSE).

---
🚀 Let’s build better tools together.

If you’d like a tweet thread, carousel, or launch post for this — I’ve got your back 😎



