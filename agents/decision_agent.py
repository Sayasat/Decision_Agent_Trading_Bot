# # agents/decision_agent.py

# from agents.types import MarketUpdate, TradeDecision
# from ml.ml_agent import predict_decision


# class DecisionAgent:
#     """
#     Decision-Making Agent:
#     получает MarketUpdate, вызывает ML-модель
#     и возвращает TradeDecision (BUY/SELL/HOLD + confidence).
#     """

#     def decide(self, market_update: MarketUpdate) -> TradeDecision:
#         ml_result = predict_decision(market_update.features)

#         return TradeDecision(
#             symbol=market_update.symbol,
#             timestamp=market_update.timestamp,
#             action=ml_result["action"],
#             confidence_up=ml_result["confidence_up"],
#             confidence_down=ml_result["confidence_down"],
#             reason=ml_result["reason"],
#         )

# agents/decision_agent.py

from datetime import datetime
from agents.types import MarketUpdate, TradeDecision
from ml.ml_agent import predict_decision


class DecisionAgent:
    """
    Decision-Making Agent:
    - Принимает обновления рынка (MarketUpdate)
    - Вызывает ML-модель для определения BUY / SELL / HOLD
    - Логирует решения
    - Может быть использован Backend/Execution Agent
    """

    def __init__(self):
        self.history = []  # хранение прошлых решений

    def decide(self, market_update: MarketUpdate) -> TradeDecision:
        """
        Принимает объект MarketUpdate, вызывает ML-модель и
        возвращает TradeDecision.
        """

        ml_result = predict_decision(market_update.features)

        decision = TradeDecision(
            symbol=market_update.symbol,
            timestamp=market_update.timestamp,
            action=ml_result["action"],
            confidence_up=ml_result["confidence_up"],
            confidence_down=ml_result["confidence_down"],
            reason=ml_result["reason"],
        )

        # Логируем решение
        self.history.append({
            "symbol": market_update.symbol,
            "price": market_update.price,
            "features": market_update.features,
            "decision": decision.action,
            "confidence_up": decision.confidence_up,
            "confidence_down": decision.confidence_down,
            "timestamp": decision.timestamp.isoformat()
        })

        return decision

    def get_last_decision(self):
        """Возвращает последнее решение (или None)."""
        if not self.history:
            return None
        return self.history[-1]

    def get_history(self):
        """Возвращает ВСЮ историю решений."""
        return self.history
