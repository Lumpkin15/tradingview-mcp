from __future__ import annotations
from typing import Dict, Optional, Tuple


def compute_change(open_price: float, close: float) -> float:
    return ((close - open_price) / open_price) * 100 if open_price else 0.0


def compute_bbw(sma: float, bb_upper: float, bb_lower: float) -> Optional[float]:
    if not sma:
        return None
    try:
        return (bb_upper - bb_lower) / sma
    except ZeroDivisionError:
        return None


def compute_bb_rating_signal(close: float, bb_upper: float, bb_middle: float, bb_lower: float) -> Tuple[int, str]:
    rating = 0
    if close > bb_upper:
        rating = 3
    elif close > bb_middle + ((bb_upper - bb_middle) / 2):
        rating = 2
    elif close > bb_middle:
        rating = 1
    elif close < bb_lower:
        rating = -3
    elif close < bb_middle - ((bb_middle - bb_lower) / 2):
        rating = -2
    elif close < bb_middle:
        rating = -1

    signal = "NEUTRAL"
    if rating == 2:
        signal = "BUY"
    elif rating == -2:
        signal = "SELL"
    return rating, signal


def compute_atr_normalized(atr: float, close: float) -> Optional[float]:
    """Compute ATR as percentage of price for better comparison across assets."""
    if not close or close == 0:
        return None
    try:
        return (atr / close) * 100
    except (ZeroDivisionError, TypeError):
        return None


def compute_volume_trend(volume: float, volume_sma: float) -> Optional[Dict]:
    """Analyze volume trend relative to average."""
    if not volume_sma or volume_sma == 0:
        return None
    try:
        volume_ratio = volume / volume_sma
        trend = "High" if volume_ratio > 1.5 else "Above Average" if volume_ratio > 1.0 else "Below Average" if volume_ratio > 0.5 else "Low"
        return {
            "volume_ratio": round(volume_ratio, 2),
            "volume_trend": trend
        }
    except (ZeroDivisionError, TypeError):
        return None


def compute_metrics(indicators: Dict) -> Optional[Dict]:
    try:
        open_price = indicators["open"]
        close = indicators["close"]
        sma = indicators["SMA20"]
        bb_upper = indicators["BB.upper"]
        bb_lower = indicators["BB.lower"]
        bb_middle = sma

        change = compute_change(open_price, close)
        bbw = compute_bbw(sma, bb_upper, bb_lower)
        rating, signal = compute_bb_rating_signal(close, bb_upper, bb_middle, bb_lower)

        return {
            "price": round(close, 4),
            "change": round(change, 3),
            "bbw": round(bbw, 4) if bbw is not None else None,
            "rating": rating,
            "signal": signal,
        }
    except (KeyError, TypeError):
        return None
