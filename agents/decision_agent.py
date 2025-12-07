# agents/decision_agent.py

from agents.types import MarketUpdate, TradeDecision
from ml.ml_agent import predict_decision


class DecisionAgent:
    """
    Decision-Making Agent:
    получает MarketUpdate, вызывает ML-модель
    и возвращает TradeDecision (BUY/SELL/HOLD + confidence).
    """

    def decide(self, market_update: MarketUpdate) -> TradeDecision:
        ml_result = predict_decision(market_update.features)

        return TradeDecision(
            symbol=market_update.symbol,
            timestamp=market_update.timestamp,
            action=ml_result["action"],
            confidence_up=ml_result["confidence_up"],
            confidence_down=ml_result["confidence_down"],
            reason=ml_result["reason"],
        )
