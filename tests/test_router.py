from src.router_service import RouterService

def test_routing():
    service = RouterService()
    res = service.classify("Where is my order?")
    assert "intent" in res
