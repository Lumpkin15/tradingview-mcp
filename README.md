# 📈 TradingView MCP Server

A powerful Model Context Protocol (MCP) server that provides advanced cryptocurrency and stock market analysis using TradingView data. Perfect for traders, analysts, and AI assistants who need real-time market intelligence.

## 🎥 Demo Video

> **Quick 19-second demo showing the MCP server in action**
> 

https://github-production-user-asset-6210df.s3.amazonaws.com/67838093/478689497-4a605d98-43e8-49a6-8d3a-559315f6c01d.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20250816%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250816T155717Z&X-Amz-Expires=300&X-Amz-Signature=1362a9ea0e886268315cfa5b63951c82929ea01c9d826c87060e3ac116cf9531&X-Amz-SignedHeaders=host

## ✨ Key Features

- 🚀 **Real-time Market Screening**: Find top gainers, losers, and trending stocks/crypto
- 📊 **Advanced Technical Analysis**: Bollinger Bands, RSI, MACD, ATR, and more indicators
- 🎯 **Bollinger Band Intelligence**: Proprietary rating system (-3 to +3) for squeeze detection
- 🕯️ **Pattern Recognition**: Detect consecutive bullish/bearish candle formations
- 🧠 **AI-Powered Sentiment Analysis**: Comprehensive 0-100 sentiment scoring with multi-factor analysis
- 📈 **Market Sentiment Overview**: Aggregate sentiment across multiple assets for market-wide insights
- 💎 **Multi-Market Support**: Crypto exchanges (KuCoin, Binance, Bybit) + Traditional markets (NASDAQ, NYSE, BIST)
- ⏰ **Multi-Timeframe Analysis**: From 5-minute to monthly charts
- 🔍 **Individual Asset Deep-Dive**: Comprehensive technical analysis for any symbol

## 🚀 Quick Start

### Option 1: Claude Desktop (Recommended)

1. **Install UV Package Manager:**
   ```bash
   # macOS (Homebrew)
   brew install uv
   
   # Windows
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # macOS/Linux (Direct)
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Add to Claude Desktop Configuration:**
   
   **Config Path:**
   - **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
   - **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
   
   ```json
   {
     "mcpServers": {
       "tradingview-mcp": {
         "command": "uv",
         "args": [
           "tool", "run", "--from",
           "git+https://github.com/Lumpkin15/tradingview-mcp.git",
           "tradingview-mcp"
         ]
       }
     }
   }
   ```

3. **Restart Claude Desktop** - The server will be automatically available!

📋 **For detailed Windows instructions, see [INSTALLATION.md](INSTALLATION.md)**

### Option 2: Manual Installation

```bash
# Clone the repository
git clone https://github.com/Lumpkin15/tradingview-mcp.git
cd tradingview-mcp

# Install dependencies
uv sync

# For local development, add to Claude Desktop:
```

**Windows Configuration Path:**
`%APPDATA%\Claude\claude_desktop_config.json`

**macOS Configuration Path:**
`~/Library/Application Support/Claude/claude_desktop_config.json`

**Configuration for Local Setup:**
```json
{
  "mcpServers": {
    "tradingview-mcp-local": {
      "command": "C:\\path\\to\\your\\tradingview-mcp\\.venv\\Scripts\\python.exe",
      "args": ["C:\\path\\to\\your\\tradingview-mcp\\src\\tradingview_mcp\\server.py"],
      "cwd": "C:\\path\\to\\your\\tradingview-mcp"
    }
  }
}
```

**macOS/Linux Configuration:**
```json
{
  "mcpServers": {
    "tradingview-mcp-local": {
      "command": "uv",
      "args": ["run", "python", "src/tradingview_mcp/server.py"],
      "cwd": "/path/to/your/tradingview-mcp"
    }
  }
}
```

## 🛠️ Available Tools

### 📈 Market Screening
| Tool | Description | Example Usage |
|------|-------------|---------------|
| `top_gainers` | Find highest performing assets | Top crypto gainers in 15m |
| `top_losers` | Find biggest declining assets | Worst performing stocks today |
| `bollinger_scan` | Find assets with tight Bollinger Bands | Coins ready for breakout |
| `rating_filter` | Filter by Bollinger Band rating | Strong buy signals (rating +2) |

### 🔍 Technical Analysis
| Tool | Description | Example Usage |
|------|-------------|---------------|
| `coin_analysis` | Complete technical analysis with sentiment | Analyze BTC with all indicators |
| `consecutive_candles_scan` | Find candlestick patterns | 3+ consecutive green candles |
| `advanced_candle_pattern` | Multi-timeframe pattern analysis | Complex pattern detection |

### 🧠 Sentiment Analysis (NEW!)
| Tool | Description | Example Usage |
|------|-------------|---------------|
| `sentiment_analysis` | AI-powered sentiment scoring (0-100) | Get sentiment score for ETHUSDT |
| `market_sentiment_overview` | Market-wide sentiment aggregation | Overall crypto market sentiment |

### 📋 Information
| Tool | Description |
|------|-------------|
| `exchanges://list` | List all supported exchanges and markets |

## 📝 Usage Examples

### Talk to Claude Like This:

**Basic Market Screening:**
```
"Show me the top 10 crypto gainers on KuCoin in the last 15 minutes"
"Find the biggest losers on Binance today"  
"Which Turkish stocks (BIST) are down more than 5% today?"
```

**Technical Analysis:**
```
"Analyze Bitcoin with all technical indicators"
"Find crypto coins with Bollinger Band squeeze (BBW < 0.05)"
"Show me coins with strong buy signals (rating +2)"
"Analyze IBM stock on NYSE with technical indicators"
```

**Pattern Recognition:**
```
"Find coins with 3 consecutive bullish candles on Bybit"
"Scan for stocks showing growing candle patterns"
"Which assets have tight Bollinger Bands ready for breakout?"
```

**Sentiment Analysis (NEW!):**
```
"What's the sentiment score for Bitcoin right now?"
"Analyze ETHUSDT sentiment on the 4h timeframe"
"Show me the overall market sentiment on KuCoin"
"Which assets have the most bullish sentiment?"
"What's the market mood across top 30 crypto assets?"
```

**Advanced Queries:**
```
"Compare AAPL vs TSLA technical indicators with sentiment"
"Find high-volume crypto with RSI below 30"
"Show me NASDAQ stocks with strong momentum"
"Find NYSE stocks with Bollinger Band squeeze"
"Analyze market sentiment on Binance for 1h timeframe"
```

## 🎯 Understanding the Bollinger Band Rating System

Our proprietary rating system helps identify trading opportunities:

| Rating | Signal | Description |
|--------|---------|-------------|
| **+3** | 🔥 Strong Buy | Price above upper Bollinger Band |
| **+2** | ✅ Buy | Price in upper 50% of bands |
| **+1** | ⬆️ Weak Buy | Price above middle line |
| **0** | ➡️ Neutral | Price at middle line |
| **-1** | ⬇️ Weak Sell | Price below middle line |
| **-2** | ❌ Sell | Price in lower 50% of bands |
| **-3** | 🔥 Strong Sell | Price below lower Bollinger Band |

**Bollinger Band Width (BBW)**: Lower values indicate tighter bands → potential breakout coming!

## 🏢 Supported Markets & Exchanges

### 💰 Cryptocurrency Exchanges
- **KuCoin** (KUCOIN) - Primary recommendation
- **Binance** (BINANCE) - Largest crypto exchange  
- **Bybit** (BYBIT) - Derivatives focused
- **OKX** (OKX) - Global crypto exchange
- **Coinbase** (COINBASE) - US-regulated exchange
- **Gate.io** (GATEIO) - Altcoin specialist
- **Huobi** (HUOBI) - Asian market leader
- **Bitfinex** (BITFINEX) - Professional trading

### 📊 Traditional Markets
- **NASDAQ** (NASDAQ) - US tech stocks (AAPL, MSFT, TSLA)
- **NYSE** (NYSE) - New York Stock Exchange (IBM, GE, JPM)
- **BIST** (BIST) - Turkish stock market (Borsa İstanbul)
- More markets coming soon!

### ⏰ Supported Timeframes
`5m`, `15m`, `1h`, `4h`, `1D`, `1W`, `1M`

## 📊 Technical Indicators Included

- **Bollinger Bands** (20, 2) - Volatility and squeeze detection
- **RSI** (14) - Momentum oscillator
- **Moving Averages** - SMA20, EMA50, EMA200
- **MACD** - Trend and momentum
- **ADX** - Trend strength measurement
- **Stochastic** - Overbought/oversold conditions
- **ATR (Average True Range)** - Volatility measurement (NEW!)
- **Volume Analysis** - Market participation with trend detection
- **Price Action** - OHLC data with percentage changes

## 🧠 Understanding Sentiment Analysis

Our proprietary sentiment scoring system analyzes multiple factors to provide a comprehensive 0-100 score:

### Sentiment Score Components

| Component | Weight | Factors Analyzed |
|-----------|--------|------------------|
| **Technical Signals** | 40% | RSI, MACD, Stochastic oscillators |
| **Trend Strength** | 30% | EMA alignment, ADX strength |
| **Volume Confirmation** | 20% | Volume ratio vs average |
| **Volatility Assessment** | 10% | ATR percentage, BBW |

### Sentiment Categories

| Score Range | Category | Emoji | Recommendation |
|-------------|----------|-------|----------------|
| **80-100** | Very Bullish | 🔥 | Strong Buy Signal |
| **65-79** | Bullish | ✅ | Buy Signal |
| **55-64** | Slightly Bullish | ⬆️ | Weak Buy |
| **45-54** | Neutral | ➡️ | Hold/Wait |
| **35-44** | Slightly Bearish | ⬇️ | Weak Sell |
| **20-34** | Bearish | ❌ | Sell Signal |
| **0-19** | Very Bearish | 🔥 | Strong Sell Signal |

**Example Output:**
```
🔥 Very Bullish - Score: 87/100
Recommendation: Strong Buy Signal

Component Breakdown:
├─ Technical Signals: 92/100 (40% weight)
│  ├─ RSI: 68 (Strong Bullish)
│  ├─ MACD: Positive & Above Signal
│  └─ Stochastic: 75 (Bullish)
├─ Trend Strength: 95/100 (30% weight)
│  ├─ EMA Alignment: Strong Uptrend
│  └─ ADX: 35 (Strong Trend)
├─ Volume Confirmation: 85/100 (20% weight)
│  └─ Volume Ratio: 2.1x (High Volume)
└─ Volatility: 65/100 (10% weight)
   └─ ATR: 2.3% (Moderate Volatility)
```

## 🚨 Troubleshooting

### Common Issues:

**1. "No data found" errors:**
- Try different exchanges (KuCoin usually works best)
- Use standard timeframes (15m, 1h, 1D)
- Check symbol format (e.g., "BTCUSDT" not "BTC")

**2. Empty arrays or rate limiting:**
- If you get empty results, you may have hit TradingView's rate limits
- Wait 5-10 minutes between query sessions
- The server automatically handles retries
- KuCoin and BIST have the most reliable data

**3. Claude Desktop not detecting the server:**
- Restart Claude Desktop after adding configuration
- Check that UV is installed: `uv --version`
- Verify the configuration JSON syntax

**4. Slow responses:**
- First request may be slower (warming up)
- Subsequent requests are much faster
- Consider using smaller limits (5-10 items)

## 🔧 Development & Customization

### Running in Development Mode:
```bash
# Clone and setup
git clone https://github.com/Lumpkin15/tradingview-mcp.git
cd tradingview-mcp
uv sync

# Run with MCP Inspector for debugging
uv run mcp dev src/tradingview_mcp/server.py

# Test individual functions
uv run python test_api.py
```

### Adding New Exchanges:
The server is designed to be easily extensible. Check `src/tradingview_mcp/core/` for the modular architecture.

## 🤝 Contributing

We welcome contributions! Here's how:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Ideas for Contributions:
- Add new exchanges or markets
- Implement additional technical indicators  
- Improve error handling and rate limiting
- Add more candlestick pattern recognition
- Create comprehensive test suite

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Support & Issues

- **Report bugs**: [GitHub Issues](https://github.com/Lumpkin15/tradingview-mcp/issues)
- **Feature requests**: Open an issue with the "enhancement" label
- **Questions**: Check existing issues or open a new discussion

## 🌟 Star This Project

If you find this MCP server useful, please ⭐ star the repository to help others discover it!

---

**Built with ❤️ for traders and AI enthusiasts**

*Empowering intelligent trading decisions through advanced market analysis*
