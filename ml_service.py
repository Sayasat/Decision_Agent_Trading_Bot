# ml_service.py — HTTP API wrapper for DecisionAgent

from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

from agents.decision_agent import DecisionAgent
from agents.types import MarketUpdate


# ---------- Input / Output Schemas ----------

class FeaturesIn(BaseModel):
    return_1d: float
    SMA_5: float
    SMA_10: float
    price_over_sma5: float


class PredictRequest(BaseModel):
    symbol: str
    price: float
    features: FeaturesIn


class PredictResponse(BaseModel):
    symbol: str
    action: str
    confidence_up: float
    confidence_down: float
    reason: str
    timestamp: str


# ---------- FastAPI App ----------

app = FastAPI()
agent = DecisionAgent()


# ---------- Endpoint: /predict ----------

@app.post("/predict", response_model=PredictResponse)
def predict(body: PredictRequest):
    update = MarketUpdate(
        symbol=body.symbol,
        timestamp=datetime.utcnow(),
        price=body.price,
        features=body.features.dict(),
    )

    decision = agent.decide(update)

    return PredictResponse(
        symbol=decision.symbol,
        action=decision.action,
        confidence_up=decision.confidence_up,
        confidence_down=decision.confidence_down,
        reason=decision.reason,
        timestamp=decision.timestamp.isoformat(),
    )
