"""Tests for The Room dialogue routes."""

from room_api.data.quotes import QUOTES


def test_whos_the_client_returns_confidential(client):
    """Test the primary user request endpoint: /whos-the-client."""
    response = client.get("/whos-the-client")
    assert response.status_code == 200
    assert response.is_json

    data = response.get_json()
    assert data["quote"] == "I cannot tell you, it's confidential."
    assert data["dialogue"] == "I cannot tell you, it's confidential."
    assert data["character"] == "Johnny"
    assert data["spoken_to"] == "Mark"
    assert data["endpoint"] == "/whos-the-client"


def test_whos_the_client_api_prefixes(client):
    """Test /api and /api/v1 aliases for /whos-the-client."""
    res_api = client.get("/api/whos-the-client")
    assert res_api.status_code == 200
    assert res_api.get_json()["quote"] == "I cannot tell you, it's confidential."

    res_v1 = client.get("/api/v1/whos-the-client")
    assert res_v1.status_code == 200
    assert res_v1.get_json()["quote"] == "I cannot tell you, it's confidential."


def test_whos_the_client_format_simple(client):
    """Test format=simple query parameter on /whos-the-client."""
    response = client.get("/whos-the-client?format=simple")
    assert response.status_code == 200
    data = response.get_json()
    assert data == {"quote": "I cannot tell you, it's confidential."}


def test_whos_the_client_format_dialogue(client):
    """Test format=dialogue query parameter on /whos-the-client."""
    response = client.get("/whos-the-client?format=dialogue")
    assert response.status_code == 200
    data = response.get_json()
    assert data == {
        "character": "Johnny",
        "dialogue": "I cannot tell you, it's confidential.",
    }


def test_did_you_hit_her_endpoint(client):
    """Test rooftop domestic dispute quote."""
    response = client.get("/did-you-hit-her")
    assert response.status_code == 200
    data = response.get_json()
    assert "I did not hit her" in data["quote"]
    assert "Oh, hi Mark." in data["quote"]
    assert data["character"] == "Johnny"


def test_hows_your_sex_life_endpoint(client):
    """Test sudden subject diversion quote."""
    response = client.get("/hows-your-sex-life")
    assert response.status_code == 200
    data = response.get_json()
    assert data["quote"] == "Anyway, how's your sex life?"
    assert data["character"] == "Johnny"


def test_youre_tearing_me_apart_endpoint(client):
    """Test anguish quote."""
    response = client.get("/youre-tearing-me-apart")
    assert response.status_code == 200
    data = response.get_json()
    assert data["quote"] == "You're tearing me apart, Lisa!"


def test_hi_doggie_endpoint(client):
    """Test flower shop doggie quote."""
    response = client.get("/hi-doggie")
    assert response.status_code == 200
    data = response.get_json()
    assert data["quote"] == "Hi doggie."


def test_all_catalog_endpoints_respond_200(client):
    """Verify every quote defined in the catalog is reachable and returns valid JSON."""
    for q in QUOTES:
        endpoint = q["endpoint"]
        response = client.get(endpoint)
        assert response.status_code == 200, f"Endpoint {endpoint} failed"
        data = response.get_json()
        assert data["quote"] == q["quote"]
        assert data["character"] == q["character"]


def test_dialogue_slug_route(client):
    """Test /dialogue/<slug> path parameter route."""
    response = client.get("/dialogue/chicken")
    assert response.status_code == 200
    data = response.get_json()
    assert data["quote"] == "Cheep cheep cheep cheep cheep!"

    # Test unknown slug
    err_resp = client.get("/dialogue/non-existent-slug")
    assert err_resp.status_code == 404
    assert "not found" in err_resp.get_json()["error"]
