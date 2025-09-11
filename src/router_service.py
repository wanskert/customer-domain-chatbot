from .nlp_router import ZeroShotRouter
from .skills import order_status, refunds, product_info, smalltalk

HANDLERS = {
    "order_status": order_status.handle,
    "refund_request": refunds.handle,
    "product_info": product_info.handle,
    "troubleshooting": product_info.handle,
    "smalltalk": smalltalk.handle,
}

class RouterService:
    def __init__(self):
        self.router = ZeroShotRouter()

    def classify(self, text: str):
        return self.router.classify(text)

    def chat(self, text: str):
        res = self.classify(text)
        handler = HANDLERS.get(res["intent"], smalltalk.handle)
        reply = handler(text)
        return {"intent": res["intent"], "confidence": res["confidence"], "reply": reply}
