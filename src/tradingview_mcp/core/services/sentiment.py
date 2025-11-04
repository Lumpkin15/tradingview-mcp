from __future__ import annotations
from typing import Dict, Optional, Tuple


def compute_technical_signals_score(indicators: Dict) -> Tuple[float, Dict]:
    """
    Compute technical signals score (0-100) from RSI, MACD, and Stochastic.
    Weight: 40% of total sentiment score.

    Returns:
        Tuple of (score, breakdown_dict)
    """
    score = 0.0
    max_score = 100.0
    breakdown = {}

    # RSI Analysis (33.3% of technical score)
    rsi = indicators.get("RSI", 50)
    if rsi:
        if rsi < 30:
            rsi_score = 0  # Oversold - bearish
            rsi_signal = "Oversold (Bearish)"
        elif rsi < 40:
            rsi_score = 25
            rsi_signal = "Weak (Bearish)"
        elif rsi < 60:
            rsi_score = 50
            rsi_signal = "Neutral"
        elif rsi < 70:
            rsi_score = 75
            rsi_signal = "Strong (Bullish)"
        else:
            rsi_score = 100  # Overbought - very bullish but risky
            rsi_signal = "Overbought (Bullish)"

        score += rsi_score * 0.333
        breakdown["rsi"] = {"value": round(rsi, 2), "score": rsi_score, "signal": rsi_signal}

    # MACD Analysis (33.3% of technical score)
    macd = indicators.get("MACD.macd", 0)
    macd_signal = indicators.get("MACD.signal", 0)

    if macd is not None and macd_signal is not None:
        macd_diff = macd - macd_signal

        if macd_diff > 0:
            # Bullish crossover
            if macd > 0:
                macd_score = 100  # Strong bullish
                signal = "Strong Bullish (Positive & Above Signal)"
            else:
                macd_score = 75  # Moderate bullish
                signal = "Bullish (Above Signal)"
        else:
            # Bearish crossover
            if macd < 0:
                macd_score = 0  # Strong bearish
                signal = "Strong Bearish (Negative & Below Signal)"
            else:
                macd_score = 25  # Moderate bearish
                signal = "Bearish (Below Signal)"

        score += macd_score * 0.333
        breakdown["macd"] = {
            "macd": round(macd, 6),
            "signal": round(macd_signal, 6),
            "divergence": round(macd_diff, 6),
            "score": macd_score,
            "interpretation": signal
        }

    # Stochastic Analysis (33.3% of technical score)
    stoch_k = indicators.get("Stoch.K", 50)
    stoch_d = indicators.get("Stoch.D", 50)

    if stoch_k is not None and stoch_d is not None:
        stoch_avg = (stoch_k + stoch_d) / 2

        if stoch_avg < 20:
            stoch_score = 0  # Oversold
            stoch_signal = "Oversold (Bearish)"
        elif stoch_avg < 40:
            stoch_score = 35
            stoch_signal = "Weak (Bearish)"
        elif stoch_avg < 60:
            stoch_score = 50
            stoch_signal = "Neutral"
        elif stoch_avg < 80:
            stoch_score = 75
            stoch_signal = "Strong (Bullish)"
        else:
            stoch_score = 100  # Overbought
            stoch_signal = "Overbought (Bullish)"

        score += stoch_score * 0.333
        breakdown["stochastic"] = {
            "k": round(stoch_k, 2),
            "d": round(stoch_d, 2),
            "avg": round(stoch_avg, 2),
            "score": stoch_score,
            "signal": stoch_signal
        }

    return round(score, 2), breakdown


def compute_trend_strength_score(indicators: Dict) -> Tuple[float, Dict]:
    """
    Compute trend strength score (0-100) from EMA alignment and ADX.
    Weight: 30% of total sentiment score.

    Returns:
        Tuple of (score, breakdown_dict)
    """
    score = 0.0
    breakdown = {}

    close = indicators.get("close", 0)
    ema50 = indicators.get("EMA50", 0)
    ema200 = indicators.get("EMA200", 0)
    adx = indicators.get("ADX", 0)

    # EMA Alignment (60% of trend score)
    if close and ema50 and ema200:
        if close > ema50 > ema200:
            ema_score = 100  # Strong uptrend
            ema_trend = "Strong Uptrend (Price > EMA50 > EMA200)"
        elif close > ema50:
            ema_score = 75  # Moderate uptrend
            ema_trend = "Uptrend (Price > EMA50)"
        elif close < ema50 < ema200:
            ema_score = 0  # Strong downtrend
            ema_trend = "Strong Downtrend (Price < EMA50 < EMA200)"
        elif close < ema50:
            ema_score = 25  # Moderate downtrend
            ema_trend = "Downtrend (Price < EMA50)"
        else:
            ema_score = 50  # Mixed signals
            ema_trend = "Mixed Signals"

        score += ema_score * 0.6
        breakdown["ema_alignment"] = {
            "close": round(close, 6),
            "ema50": round(ema50, 6),
            "ema200": round(ema200, 6),
            "score": ema_score,
            "trend": ema_trend
        }

    # ADX Trend Strength (40% of trend score)
    if adx:
        # ADX measures trend strength, not direction
        if adx < 25:
            adx_score = 25  # Weak trend
            adx_strength = "Weak/Ranging"
        elif adx < 50:
            adx_score = 60  # Moderate trend
            adx_strength = "Moderate Trend"
        elif adx < 75:
            adx_score = 85  # Strong trend
            adx_strength = "Strong Trend"
        else:
            adx_score = 100  # Very strong trend
            adx_strength = "Very Strong Trend"

        # Adjust based on trend direction (use EMA alignment)
        if "ema_alignment" in breakdown:
            ema_score_pct = breakdown["ema_alignment"]["score"]
            if ema_score_pct < 50:  # Downtrend
                adx_score = 100 - adx_score  # Invert for bearish trends

        score += adx_score * 0.4
        breakdown["adx"] = {
            "value": round(adx, 2),
            "score": adx_score,
            "strength": adx_strength
        }

    return round(score, 2), breakdown


def compute_volume_confirmation_score(indicators: Dict) -> Tuple[float, Dict]:
    """
    Compute volume confirmation score (0-100).
    Weight: 20% of total sentiment score.

    Returns:
        Tuple of (score, breakdown_dict)
    """
    score = 50.0  # Default neutral
    breakdown = {}

    volume = indicators.get("volume", 0)
    volume_sma = indicators.get("Volume.sma20", 0) or indicators.get("volume", 0)

    if volume and volume_sma and volume_sma > 0:
        volume_ratio = volume / volume_sma

        # Higher volume = stronger confirmation
        if volume_ratio > 2.0:
            vol_score = 100  # Very high volume
            vol_signal = "Very High Volume (Strong Confirmation)"
        elif volume_ratio > 1.5:
            vol_score = 85
            vol_signal = "High Volume (Good Confirmation)"
        elif volume_ratio > 1.0:
            vol_score = 65
            vol_signal = "Above Average Volume"
        elif volume_ratio > 0.7:
            vol_score = 50
            vol_signal = "Average Volume"
        elif volume_ratio > 0.4:
            vol_score = 35
            vol_signal = "Below Average Volume"
        else:
            vol_score = 15
            vol_signal = "Low Volume (Weak Confirmation)"

        score = vol_score
        breakdown["volume"] = {
            "current": volume,
            "sma20": volume_sma,
            "ratio": round(volume_ratio, 2),
            "score": vol_score,
            "signal": vol_signal
        }

    return round(score, 2), breakdown


def compute_volatility_score(indicators: Dict) -> Tuple[float, Dict]:
    """
    Compute volatility assessment score (0-100).
    Weight: 10% of total sentiment score.
    Lower volatility in uptrend = higher score (more stable)

    Returns:
        Tuple of (score, breakdown_dict)
    """
    score = 50.0  # Default neutral
    breakdown = {}

    # ATR Analysis
    atr = indicators.get("ATR", 0)
    close = indicators.get("close", 0)

    if atr and close:
        atr_pct = (atr / close) * 100

        # Lower ATR% = more stable (higher score in uptrend)
        if atr_pct < 1.0:
            atr_score = 85
            atr_signal = "Low Volatility (Stable)"
        elif atr_pct < 2.0:
            atr_score = 70
            atr_signal = "Moderate Volatility"
        elif atr_pct < 3.5:
            atr_score = 50
            atr_signal = "Average Volatility"
        elif atr_pct < 5.0:
            atr_score = 35
            atr_signal = "High Volatility"
        else:
            atr_score = 20
            atr_signal = "Very High Volatility (Risky)"

        breakdown["atr"] = {
            "value": round(atr, 6),
            "percentage": round(atr_pct, 2),
            "score": atr_score,
            "signal": atr_signal
        }
        score = atr_score * 0.6  # 60% weight

    # BBW Analysis
    sma = indicators.get("SMA20", 0)
    bb_upper = indicators.get("BB.upper", 0)
    bb_lower = indicators.get("BB.lower", 0)

    if sma and bb_upper and bb_lower:
        bbw = (bb_upper - bb_lower) / sma if sma else 0

        if bbw < 0.02:
            bbw_score = 50  # Tight bands - potential breakout
            bbw_signal = "Very Tight (Breakout Imminent)"
        elif bbw < 0.04:
            bbw_score = 65
            bbw_signal = "Tight (Low Volatility)"
        elif bbw < 0.06:
            bbw_score = 75
            bbw_signal = "Normal (Moderate Volatility)"
        elif bbw < 0.10:
            bbw_score = 50
            bbw_signal = "Wide (High Volatility)"
        else:
            bbw_score = 30
            bbw_signal = "Very Wide (Extreme Volatility)"

        breakdown["bbw"] = {
            "value": round(bbw, 4),
            "score": bbw_score,
            "signal": bbw_signal
        }

        if "atr" in breakdown:
            score = score + (bbw_score * 0.4)  # 40% weight
        else:
            score = bbw_score

    return round(score, 2), breakdown


def compute_sentiment_score(indicators: Dict) -> Dict:
    """
    Compute comprehensive sentiment score (0-100) by aggregating multiple factors.

    Weighting:
    - Technical signals (RSI, MACD, Stochastic): 40%
    - Trend strength (EMA, ADX): 30%
    - Volume confirmation: 20%
    - Volatility assessment: 10%

    Returns:
        Dict with overall score, category, and detailed breakdown
    """

    # Compute individual components
    tech_score, tech_breakdown = compute_technical_signals_score(indicators)
    trend_score, trend_breakdown = compute_trend_strength_score(indicators)
    volume_score, volume_breakdown = compute_volume_confirmation_score(indicators)
    volatility_score, volatility_breakdown = compute_volatility_score(indicators)

    # Calculate weighted overall score
    overall_score = (
        (tech_score * 0.40) +
        (trend_score * 0.30) +
        (volume_score * 0.20) +
        (volatility_score * 0.10)
    )

    # Determine sentiment category
    if overall_score >= 80:
        category = "Very Bullish"
        emoji = "🔥"
        recommendation = "Strong Buy Signal"
    elif overall_score >= 65:
        category = "Bullish"
        emoji = "✅"
        recommendation = "Buy Signal"
    elif overall_score >= 55:
        category = "Slightly Bullish"
        emoji = "⬆️"
        recommendation = "Weak Buy"
    elif overall_score >= 45:
        category = "Neutral"
        emoji = "➡️"
        recommendation = "Hold/Wait"
    elif overall_score >= 35:
        category = "Slightly Bearish"
        emoji = "⬇️"
        recommendation = "Weak Sell"
    elif overall_score >= 20:
        category = "Bearish"
        emoji = "❌"
        recommendation = "Sell Signal"
    else:
        category = "Very Bearish"
        emoji = "🔥"
        recommendation = "Strong Sell Signal"

    return {
        "overall_score": round(overall_score, 2),
        "sentiment_category": category,
        "emoji": emoji,
        "recommendation": recommendation,
        "component_scores": {
            "technical_signals": {
                "score": tech_score,
                "weight": "40%",
                "breakdown": tech_breakdown
            },
            "trend_strength": {
                "score": trend_score,
                "weight": "30%",
                "breakdown": trend_breakdown
            },
            "volume_confirmation": {
                "score": volume_score,
                "weight": "20%",
                "breakdown": volume_breakdown
            },
            "volatility_assessment": {
                "score": volatility_score,
                "weight": "10%",
                "breakdown": volatility_breakdown
            }
        },
        "score_interpretation": {
            "80-100": "Very Bullish - Strong upward momentum with good confirmation",
            "65-79": "Bullish - Positive signals with decent strength",
            "55-64": "Slightly Bullish - Mild positive bias",
            "45-54": "Neutral - Mixed signals, no clear direction",
            "35-44": "Slightly Bearish - Mild negative bias",
            "20-34": "Bearish - Negative signals with weakness",
            "0-19": "Very Bearish - Strong downward momentum"
        }
    }


def compute_multi_asset_sentiment(analysis_results: list) -> Dict:
    """
    Aggregate sentiment across multiple assets to determine overall market sentiment.

    Args:
        analysis_results: List of sentiment analysis results for multiple assets

    Returns:
        Dict with market-wide sentiment analysis
    """
    if not analysis_results:
        return {"error": "No analysis results provided"}

    scores = []
    categories = {"Very Bullish": 0, "Bullish": 0, "Slightly Bullish": 0,
                  "Neutral": 0, "Slightly Bearish": 0, "Bearish": 0, "Very Bearish": 0}

    for result in analysis_results:
        if "sentiment" in result and "overall_score" in result["sentiment"]:
            scores.append(result["sentiment"]["overall_score"])
            category = result["sentiment"]["sentiment_category"]
            if category in categories:
                categories[category] += 1

    if not scores:
        return {"error": "No valid sentiment scores found"}

    avg_score = sum(scores) / len(scores)

    # Determine overall market sentiment
    if avg_score >= 70:
        market_sentiment = "Very Bullish Market"
        market_emoji = "🚀"
    elif avg_score >= 60:
        market_sentiment = "Bullish Market"
        market_emoji = "📈"
    elif avg_score >= 50:
        market_sentiment = "Slightly Bullish Market"
        market_emoji = "⬆️"
    elif avg_score >= 40:
        market_sentiment = "Neutral Market"
        market_emoji = "➡️"
    elif avg_score >= 30:
        market_sentiment = "Slightly Bearish Market"
        market_emoji = "⬇️"
    elif avg_score >= 20:
        market_sentiment = "Bearish Market"
        market_emoji = "📉"
    else:
        market_sentiment = "Very Bearish Market"
        market_emoji = "💥"

    return {
        "market_sentiment": market_sentiment,
        "emoji": market_emoji,
        "average_score": round(avg_score, 2),
        "total_assets_analyzed": len(analysis_results),
        "sentiment_distribution": categories,
        "strongest_sentiment": max(categories.items(), key=lambda x: x[1])[0],
        "score_range": {
            "highest": round(max(scores), 2),
            "lowest": round(min(scores), 2)
        }
    }
