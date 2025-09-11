from transformers import pipeline

CANDIDATE_INTENTS = ["order_status", "refund_request", "product_info", "troubleshooting", "smalltalk"]

class ZeroShotRouter:
    def __init__(self, model: str = "typeform/distilbert-base-uncased-mnli", threshold: float = 0.45):
        self.clf = pipeline("zero-shot-classification", model=model)
        self.threshold = threshold

    def classify(self, text: str):
        res = self.clf(text, candidate_labels=CANDIDATE_INTENTS)
        labels = res["labels"]
        scores = res["scores"]
        best_idx = int(max(range(len(scores)), key=lambda i: scores[i]))
        intent, conf = labels[best_idx], float(scores[best_idx])
        if conf < self.threshold:
            intent = "smalltalk"
        return {"intent": intent, "confidence": conf, "candidates": dict(zip(labels, map(float, scores)))}
