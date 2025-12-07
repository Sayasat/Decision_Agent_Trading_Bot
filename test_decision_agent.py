# # test_decision_agent.py

# from datetime import datetime

# from agents.decision_agent import DecisionAgent
# from agents.types import MarketUpdate


# def main():
#     dummy_update = MarketUpdate(
#         symbol="AAPL",
#         timestamp=datetime.now(),
#         price=195.32,
#         features={
#             "return_1d": 0.0025,
#             "SMA_5": 190.0,
#             "SMA_10": 188.0,
#             "price_over_sma5": 1.028,
#         },
#     )

#     agent = DecisionAgent()
#     decision = agent.decide(dummy_update)
#     print(decision)


# if __name__ == "__main__":
#     main()

# test_decision_agent.py

from datetime import datetime
from agents.decision_agent import DecisionAgent
from agents.types import MarketUpdate

TICKERS = ["AAPL", "MSFT", "GOOGL", "TSLA", "NVDA"]

# Простые фиктивные фичи (НЕ реальные)
TEST_FEATURES = {
    "return_1d": 0.01,
    "SMA_5": 150.0,
    "SMA_10": 148.0,
    "price_over_sma5": 1.02,
}


def main():
    agent = DecisionAgent()

    for symbol in TICKERS:
        test_update = MarketUpdate(
            symbol=symbol,
            timestamp=datetime.now(),
            price=200.0,
            features=TEST_FEATURES,
        )

        decision = agent.decide(test_update)

        print(f"\n=== Testing {symbol} ===")
        print("Decision:", decision.action)
        print("Confidence up:", decision.confidence_up)
        print("Confidence down:", decision.confidence_down)
        print("Reason:", decision.reason)

    print("\n--- HISTORY (all decisions) ---")
    for record in agent.get_history():
        print(record)


if __name__ == "__main__":
    main()
