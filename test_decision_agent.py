# test_decision_agent.py

from datetime import datetime

from agents.decision_agent import DecisionAgent
from agents.types import MarketUpdate


def main():
    dummy_update = MarketUpdate(
        symbol="AAPL",
        timestamp=datetime.now(),
        price=195.32,
        features={
            "return_1d": 0.0025,
            "SMA_5": 190.0,
            "SMA_10": 188.0,
            "price_over_sma5": 1.028,
        },
    )

    agent = DecisionAgent()
    decision = agent.decide(dummy_update)
    print(decision)


if __name__ == "__main__":
    main()
