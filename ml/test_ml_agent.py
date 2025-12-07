# ml/test_ml_agent.py
from ml_agent import predict_decision

dummy_features = {
    "return_1d": 0.003,
    "SMA_5": 190.0,
    "SMA_10": 188.0,
    "price_over_sma5": 1.01,
}

decision = predict_decision(dummy_features)
print(decision)
