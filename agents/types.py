# agents/types.py

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Literal

ActionType = Literal["BUY", "SELL", "HOLD"]


@dataclass
class MarketUpdate:
    symbol: str
    timestamp: datetime
    price: float
    features: Dict[str, float]


@dataclass
class TradeDecision:
    symbol: str
    timestamp: datetime
    action: ActionType
    confidence_up: float
    confidence_down: float
    reason: str
