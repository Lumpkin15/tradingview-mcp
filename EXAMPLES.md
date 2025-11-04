# 📚 Usage Examples - TradingView MCP Server

This guide shows real-world examples of how to use the TradingView MCP Server with Claude Desktop.

## 🚀 Quick Start Examples

### Basic Market Screening

#### Find Top Gainers
```
💬 You: "Show me the top 5 crypto gainers on KuCoin in the last 15 minutes"

🤖 Claude: I'll find the top-performing cryptocurrencies for you.

[Uses: top_gainers(exchange="KUCOIN", timeframe="15m", limit=5)]

📈 Top 5 Crypto Gainers (KuCoin, 15m):

1. **ACEUSDT** - $2.34 (+8.75%)
   - Volume: 2.4M USDT
   - RSI: 72.3 (Overbought)

2. **SOLUSDT** - $145.67 (+6.23%)
   - Volume: 15.2M USDT  
   - RSI: 68.1 (Strong)

[... and so on]
```

#### Find Biggest Losers
```
💬 You: "Which cryptos are falling the most on Binance today?"

🤖 Claude: [Uses: top_losers(exchange="BINANCE", timeframe="1D", limit=10)]

📉 Biggest Crypto Losers (Binance, 24h):

1. **XRPUSDT** - $0.52 (-12.4%)
2. **ADAUSDT** - $0.38 (-9.8%)
3. **DOTUSDT** - $6.12 (-8.9%)
```

#### NYSE Stock Screening
```
💬 You: "Show me the top 5 gainers on NYSE today"

🤖 Claude: [Uses: top_gainers(exchange="NYSE", timeframe="1D", limit=5)]

📈 Top 5 NYSE Gainers (Daily):

1. **NYSE:IBM** - $293.87 (+5.2%)
   - Volume: 4.2M shares
   - RSI: 65.4 (Bullish)

2. **NYSE:GE** - $168.45 (+4.8%)
   - Volume: 8.7M shares
   - RSI: 62.1 (Strong)

[... and so on]
```

### Technical Analysis

#### Individual Coin Analysis
```
💬 You: "Give me a complete technical analysis of Bitcoin"

🤖 Claude: [Uses: coin_analysis(symbol="BTCUSDT", exchange="KUCOIN", timeframe="1D")]

📊 Bitcoin (BTCUSDT) Technical Analysis:

**Price Action:**
- Current Price: $42,750
- 24h Change: +3.2% (+$1,320)
- High: $43,100 | Low: $41,200

**Bollinger Bands:**
- Rating: +2 (BUY Signal)
- BBW: 0.0342 (Medium volatility)
- Position: Upper 50% of bands

**Technical Indicators:**
- RSI: 64.2 (Bullish momentum)
- MACD: Bullish crossover
- EMA50: $41,800 (Price above)
- EMA200: $39,500 (Strong uptrend)

**Trading Signal: BUY** 🟢
```

#### Bollinger Band Squeeze Detection
```
💬 You: "Find crypto coins ready for a breakout (tight Bollinger Bands)"

🤖 Claude: [Uses: bollinger_scan(exchange="KUCOIN", bbw_threshold=0.03, limit=10)]

🎯 Bollinger Band Squeeze Alert (BBW < 0.03):

**Ready for Breakout:**
1. **ETHUSDT** - BBW: 0.0287 ⚡
   - Price: $2,534 (Middle band)
   - Volume spike: +45%

2. **BNBUSDT** - BBW: 0.0295 ⚡
   - Price: $312 (Near upper band)
   - RSI: 58 (Neutral)

*Note: Low BBW indicates potential big price movement coming!*
```

## 🎯 Advanced Trading Strategies

### Multi-Timeframe Analysis
```
💬 You: "Compare Bitcoin's performance across different timeframes"

🤖 Claude: Let me analyze Bitcoin across multiple timeframes.

[Uses multiple calls with different timeframes]

📊 Bitcoin Multi-Timeframe Analysis:

**Short-term (15m):** +0.8% - Mild bullish
**Medium-term (1h):** +2.1% - Strong bullish  
**Daily (1D):** +3.2% - Very bullish
**Weekly (1W):** +12.5% - Extremely bullish

**Trend Alignment:** ✅ All timeframes bullish
**Signal Strength:** Strong BUY across all periods
```

### Pattern Recognition
```
💬 You: "Find coins showing consecutive bullish candle patterns"

🤖 Claude: [Uses: consecutive_candles_scan(pattern_type="bullish", timeframe="1h")]

🕯️ Consecutive Bullish Patterns Found:

**Strong Momentum Coins:**
1. **SOLUSDT** - 4 consecutive green candles (1h)
   - Total gain: +8.4%
   - Volume increasing

2. **AVAXUSDT** - 3 consecutive green candles (1h)  
   - Total gain: +5.2%
   - Breaking resistance

**Pattern Strength:** High - These show sustained buying pressure
```

## 🏢 Different Markets & Exchanges

### Traditional Stock Markets
```
💬 You: "How are Turkish stocks performing today? Show me BIST gainers"

🤖 Claude: [Uses: top_gainers(exchange="BIST", timeframe="1D")]

🇹🇷 BIST (Turkish Stock Market) Top Gainers:

1. **AKBNK** - ₺58.40 (+4.2%)
2. **THYAO** - ₺245.50 (+3.8%)  
3. **ISCTR** - ₺12.35 (+3.1%)

*Turkish market showing strong performance today!*
```

```
💬 You: "What about NASDAQ tech stocks?"

🤖 Claude: [Uses: top_gainers(exchange="NASDAQ", timeframe="1D")]

🇺🇸 NASDAQ Top Gainers Today:

1. **AAPL** - $175.30 (+2.1%)
2. **MSFT** - $378.45 (+1.8%)
3. **NVDA** - $721.50 (+3.4%)
```

### Cross-Exchange Comparison
```
💬 You: "Compare Bitcoin prices across different exchanges"

🤖 Claude: Let me check Bitcoin across multiple exchanges.

[Uses coin_analysis for different exchanges]

₿ Bitcoin Price Comparison:

**KuCoin:** $42,750 (Main reference)
**Binance:** $42,735 (-$15 spread)
**Bybit:** $42,760 (+$10 spread)

**Best Exchange:** Bybit (highest price)
**Arbitrage Opportunity:** Minimal ($25 spread)
```

## 🎨 Creative Analysis Requests

### Sentiment Analysis
```
💬 You: "What's the overall crypto market sentiment right now?"

🤖 Claude: [Uses: top_gainers + top_losers + bollinger_scan]

📊 Crypto Market Sentiment Analysis:

**Overall Mood:** 🟢 Bullish (65% coins positive)

**Market Indicators:**
- Gainers vs Losers: 347 vs 198 (Bullish ratio)
- Average RSI: 58.3 (Healthy momentum)
- Bollinger Breakouts: 23 coins (High activity)
- Volume: +15% above average

**Interpretation:** Market showing strong bullish sentiment with healthy participation.
```

### Sector Rotation Analysis  
```
💬 You: "Which crypto sectors are hot right now?"

🤖 Claude: [Analyzes different crypto categories]

🔥 Hot Crypto Sectors:

**DeFi Tokens:** 🚀🚀🚀
- UNIUSDT: +12.4%
- AAVEUSDT: +8.9%
- COMPUSDT: +7.2%

**Layer 1s:** 🚀🚀
- SOLUSDT: +6.3%
- AVAXUSDT: +5.1%
- DOTUSDT: +3.8%

**Meme Coins:** 🚀
- DOGEUSDT: +4.2%
- SHIBUSDT: +2.9%

**Strongest Sector:** DeFi leading the rally!
```

## 🛠️ Troubleshooting Examples

### When Data Isn't Available
```
💬 You: "Show me Ethereum analysis"

🤖 Claude: [Tries coin_analysis but gets error]

I encountered an issue accessing Ethereum data. Let me try a different approach.

[Switches to different exchange or timeframe]

Found the data! Here's your Ethereum analysis...
```

### Handling Rate Limits
```
💬 You: "Give me analysis for 20 different coins"

🤖 Claude: I'll analyze these coins for you, but I'll pace the requests to avoid rate limits.

[Processes in batches]

📊 Analysis Results (Processing 5 at a time):

**Batch 1 Complete:** BTC, ETH, BNB, ADA, SOL
**Batch 2 Complete:** AVAX, DOT, MATIC, LINK, UNI
...
```

## 📈 Real Trading Scenarios

### Day Trading Setup
```
💬 You: "I'm day trading. Find me volatile coins with good volume on 15-minute charts"

🤖 Claude: Perfect for day trading! Let me find high-volume, volatile opportunities.

[Uses: bollinger_scan + volume filtering]

⚡ Day Trading Opportunities (15m):

**High Volatility + Volume:**
1. **BTCUSDT** - BBW: 0.045, Volume: 890M
2. **ETHUSDT** - BBW: 0.052, Volume: 456M  
3. **SOLUSDT** - BBW: 0.038, Volume: 123M

**Best Setup:** SOLUSDT - Tight bands + volume spike = breakout imminent
```

### Swing Trading
```
💬 You: "Find me coins in oversold territory for swing trades"

🤖 Claude: [Uses: rating_filter(rating=-2) + RSI analysis]

📉➡️📈 Swing Trading Opportunities:

**Oversold But Quality:**
1. **ADAUSDT** - Rating: -2, RSI: 28 (Oversold)
   - Near strong support at $0.35
   - Good risk/reward setup

2. **DOTUSDT** - Rating: -2, RSI: 31 (Oversold)
   - Bouncing off $5.80 support
   - Potential 15-20% upside

**Strategy:** Buy oversold quality projects near support
```

### Risk Management
```
💬 You: "Help me assess the risk of my current crypto positions"

🤖 Claude: [Analyzes portfolio coins individually]

⚠️ Portfolio Risk Assessment:

**High Risk:**
- ACEUSDT: RSI 78 (Extremely overbought)
- Recommendation: Take profits

**Medium Risk:**  
- BTCUSDT: RSI 64 (Strong but manageable)
- Recommendation: Hold with stop loss

**Low Risk:**
- ETHUSDT: RSI 52 (Neutral territory)  
- Recommendation: Safe to hold

**Overall Portfolio Risk:** Medium-High
**Suggestion:** Reduce exposure in overbought positions
```

## 🧠 Sentiment Analysis (NEW!)

### Individual Asset Sentiment

#### Comprehensive Sentiment Score
```
💬 You: "What's the sentiment score for Bitcoin?"

🤖 Claude: [Uses: sentiment_analysis(symbol="BTCUSDT", exchange="KUCOIN", timeframe="4h")]

🧠 Bitcoin Sentiment Analysis:

**Overall Score: 87/100** 🔥
**Category: Very Bullish**
**Recommendation: Strong Buy Signal**

📊 Component Breakdown:

**Technical Signals (40% weight): 92/100**
├─ RSI: 68.2 - Strong Bullish
├─ MACD: Positive & Above Signal (Strong Bullish)
└─ Stochastic: K=75, D=72 (Bullish)

**Trend Strength (30% weight): 95/100**
├─ EMA Alignment: Strong Uptrend (Price > EMA50 > EMA200)
└─ ADX: 35.4 (Strong Trend)

**Volume Confirmation (20% weight): 85/100**
└─ Volume Ratio: 2.1x (High Volume - Strong Confirmation)

**Volatility Assessment (10% weight): 65/100**
├─ ATR: 2.3% (Moderate Volatility)
└─ BBW: 0.035 (Normal Volatility)

💡 Summary: Strong upward momentum with excellent confirmation across all metrics. High volume and strong trend strength support continued bullish movement.
```

#### Multi-Timeframe Sentiment Comparison
```
💬 You: "Compare Bitcoin sentiment on 1h vs 4h timeframes"

🤖 Claude: [Uses sentiment_analysis multiple times]

📈 Bitcoin Multi-Timeframe Sentiment:

**1-Hour Timeframe:**
- Score: 72/100 (Bullish) ✅
- Trend: Moderate uptrend
- Volume: Above average

**4-Hour Timeframe:**
- Score: 87/100 (Very Bullish) 🔥
- Trend: Strong uptrend
- Volume: High confirmation

**Analysis:** Higher timeframe shows stronger bullish conviction. Short-term momentum aligns with longer-term trend. Consider 4h sentiment as more reliable for position sizing.
```

### Market-Wide Sentiment

#### Overall Market Mood
```
💬 You: "What's the overall crypto market sentiment on KuCoin?"

🤖 Claude: [Uses: market_sentiment_overview(exchange="KUCOIN", timeframe="15m", limit=30)]

🌍 Crypto Market Sentiment Overview:

**Market Sentiment: Bullish Market** 📈
**Average Score: 64.5/100**
**Assets Analyzed: 30**

📊 Sentiment Distribution:
- Very Bullish: 4 assets (13%)
- Bullish: 12 assets (40%)
- Slightly Bullish: 6 assets (20%)
- Neutral: 5 assets (17%)
- Slightly Bearish: 2 assets (7%)
- Bearish: 1 asset (3%)
- Very Bearish: 0 assets (0%)

**Strongest Sentiment: Bullish** (40% of assets)

📈 Top 5 Most Bullish Assets:
1. KUCOIN:ACEUSDT - Score: 89/100 (Very Bullish) 🔥 | +8.2%
2. KUCOIN:SOLUSDT - Score: 85/100 (Very Bullish) 🔥 | +5.7%
3. KUCOIN:AVAXUSDT - Score: 78/100 (Bullish) ✅ | +4.3%
4. KUCOIN:LINKUSDT - Score: 76/100 (Bullish) ✅ | +3.9%
5. KUCOIN:MATICUSDT - Score: 72/100 (Bullish) ✅ | +3.1%

📉 Top 5 Most Bearish Assets:
1. KUCOIN:ADAUSDT - Score: 28/100 (Bearish) ❌ | -4.8%
2. KUCOIN:DOTUSDT - Score: 32/100 (Slightly Bearish) ⬇️ | -3.2%
3. KUCOIN:ATOMUSDT - Score: 38/100 (Slightly Bearish) ⬇️ | -2.1%
4. KUCOIN:ALGOUSDT - Score: 41/100 (Neutral) ➡️ | -1.5%
5. KUCOIN:FTMUSDT - Score: 43/100 (Neutral) ➡️ | -0.8%

💡 Market Summary: Predominantly bullish market with strong momentum in 53% of assets. Limited bearish pressure suggests healthy market conditions favorable for long positions.
```

#### Sentiment-Based Trading Strategy
```
💬 You: "Help me find the best trading opportunities based on sentiment"

🤖 Claude: [Combines sentiment_analysis with other tools]

🎯 Sentiment-Based Trading Opportunities:

**High-Confidence Bullish Plays:**

1. **SOLUSDT** - Sentiment: 85/100 🔥
   - All 4 components positive
   - Volume confirmation: 2.3x average
   - Strong trend strength (ADX: 32)
   - Entry: Current price safe
   - Risk: Low-Medium

2. **AVAXUSDT** - Sentiment: 78/100 ✅
   - Technical signals: 88/100
   - Moderate volatility (safe)
   - EMA alignment bullish
   - Entry: Dip to SMA20
   - Risk: Low

**Recovery Opportunities (Oversold):**

1. **ADAUSDT** - Sentiment: 28/100 ❌
   - Currently bearish BUT:
   - RSI: 25 (Oversold - potential bounce)
   - Volume declining (selling exhaustion?)
   - Near support levels
   - Entry: Wait for sentiment > 45
   - Risk: High (counter-trend)

**Avoid:**
- Assets with sentiment 30-45 (weak signals)
- High sentiment (>85) with low volume (false breakout risk)

💡 Strategy: Focus on 65-85 sentiment range with strong volume confirmation for best risk/reward.
```

### Sentiment + Technical Analysis

#### Complete Market Intelligence
```
💬 You: "Give me a complete analysis of Ethereum with sentiment"

🤖 Claude: [Uses: coin_analysis(symbol="ETHUSDT") - now includes sentiment]

📊 Ethereum (ETHUSDT) Complete Analysis:

**Price Data:**
- Current: $2,845.67
- 24h Change: +4.3% (+$117.23)
- Volume: 145.2M USDT

**Sentiment Analysis:** 🔥
- Overall Score: 82/100 (Very Bullish)
- Recommendation: Strong Buy Signal
- Confidence: High (all components positive)

**Bollinger Bands:**
- Rating: +2 (BUY)
- Position: Upper 50% of bands
- BBW: 0.0298 (Moderate volatility)

**Technical Indicators:**
- RSI: 67.8 (Strong, not overbought)
- MACD: Bullish crossover confirmed
- EMA50 > EMA200: Uptrend intact
- ADX: 28.5 (Moderate-strong trend)
- ATR: 2.1% (Stable volatility)

**Volume Analysis:**
- Trend: High (1.8x average)
- Confirmation: Strong

**Market Sentiment:**
- Overall: Bullish
- Volume Trend: Above Average
- Momentum: Positive

💡 Verdict: Very bullish setup with strong sentiment backing. All timeframes align. Good entry opportunity with manageable risk.
```

## 🎯 Pro Tips for Best Results

### Effective Prompting
```
✅ Good: "Find oversold crypto with RSI below 30 on KuCoin"
❌ Avoid: "Find good crypto"

✅ Good: "Compare Bitcoin 15m vs 1h trends"  
❌ Avoid: "How is Bitcoin?"

✅ Good: "Show BIST stocks with Bollinger squeeze"
❌ Avoid: "Turkish stocks analysis"
```

### Combining Multiple Tools
```
💬 You: "Give me a complete market overview"

🤖 Claude: [Combines multiple tool calls]

🌍 Complete Crypto Market Overview:

**Market Leaders (Gainers):** [top_gainers results]
**Market Laggards (Losers):** [top_losers results]  
**Breakout Candidates:** [bollinger_scan results]
**Individual Spotlight:** [coin_analysis for BTC]

**Market Summary:** Bullish sentiment with healthy rotation
```

---

## 🎓 Learning Resources

Want to understand the technical indicators better?

- **Bollinger Bands:** Measure volatility and potential breakouts
- **RSI:** Shows overbought (>70) vs oversold (<30) conditions  
- **MACD:** Reveals trend changes and momentum shifts
- **Volume:** Confirms the strength of price movements

**Remember:** This tool provides data and analysis, but always do your own research and risk management!

---

**Happy Trading! May your analysis be sharp and your profits be green! 📈✨**
