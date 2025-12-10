# ml/ml_agent.py
import os
import numpy as np

# Lazy-load the model so importing this module doesn't require joblib present
_HERE = os.path.dirname(__file__)
_MODEL_PATH = os.path.join(_HERE, "model5.joblib")
_model = None

def _get_model():
    global _model
    if _model is None:
        try:
            import joblib
        except Exception as e:
            raise ImportError(
                "`joblib` is required to load the ML model. Install it or use a virtualenv."
            ) from e
        _model = joblib.load(_MODEL_PATH)
    return _model

FEATURE_ORDER = ["return_1d", "SMA_5", "SMA_10", "price_over_sma5"]

def predict_decision(features: dict) -> dict:
    """
    features: dict вида
    {
      "return_1d": float,
      "SMA_5": float,
      "SMA_10": float,
      "price_over_sma5": float
    }

    Возвращает:
    {
      "action": "BUY" | "SELL" | "HOLD",
      "confidence_up": float,
      "confidence_down": float,
      "reason": str
    }
    """
    x = np.array([[features[name] for name in FEATURE_ORDER]])

    model = _get_model()
    proba = model.predict_proba(x)[0]
    proba_down = float(proba[0])
    proba_up = float(proba[1])

    if proba_up > 0.6:
        action = "BUY"
    elif proba_up < 0.4:
        action = "SELL"
    else:
        action = "HOLD"

    reason = (
        f"Model predicts {proba_up:.2f} probability of price going UP "
        f"(down={proba_down:.2f}). Decision: {action}. "
        f"Features: return_1d={features['return_1d']:.4f}, "
        f"SMA_5={features['SMA_5']:.2f}, SMA_10={features['SMA_10']:.2f}, "
        f"price_over_sma5={features['price_over_sma5']:.3f}."
    )

    return {
        "action": action,
        "confidence_up": proba_up,
        "confidence_down": proba_down,
        "reason": reason,
    }
