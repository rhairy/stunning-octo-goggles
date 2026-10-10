"""Tests for meta and catalog endpoints."""


def test_index_endpoint(client):
    """Test GET / returns API metadata and endpoints."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert "The Room Dialogue REST API" in data["name"]
    assert data["example_request"] == "/whos-the-client"
    assert "endpoints" in data
    assert data["available_endpoints_count"] > 0


def test_endpoints_list(client):
    """Test GET /endpoints returns all dialogue routes."""
    response = client.get("/endpoints")
    assert response.status_code == 200
    data = response.get_json()
    assert "endpoints" in data
    assert data["count"] > 0
    endpoints = [item["endpoint"] for item in data["endpoints"]]
    assert "/whos-the-client" in endpoints


def test_quotes_list_and_filters(client):
    """Test GET /quotes with search and character filtering."""
    # List all
    res = client.get("/quotes")
    assert res.status_code == 200
    all_quotes = res.get_json()["results"]
    assert len(all_quotes) > 0

    # Filter by character
    res_char = client.get("/quotes?character=Claudette")
    assert res_char.status_code == 200
    results_char = res_char.get_json()["results"]
    assert len(results_char) >= 1
    assert all("Claudette" in q["character"] for q in results_char)

    # Search by text
    res_search = client.get("/quotes?search=breast")
    assert res_search.status_code == 200
    results_search = res_search.get_json()["results"]
    assert len(results_search) >= 1
    assert "cancer" in results_search[0]["quote"].lower()

    # Limit
    res_limit = client.get("/quotes?limit=2")
    assert res_limit.status_code == 200
    assert len(res_limit.get_json()["results"]) == 2


def test_random_quote(client):
    """Test GET /quotes/random."""
    response = client.get("/quotes/random")
    assert response.status_code == 200
    data = response.get_json()
    assert "quote" in data
    assert "character" in data


def test_characters_list(client):
    """Test GET /characters."""
    response = client.get("/characters")
    assert response.status_code == 200
    data = response.get_json()
    assert "characters" in data
    names = [c["character"] for c in data["characters"]]
    assert "Johnny" in names
    assert "Lisa" in names or "Mark" in names


def test_health_check(client):
    """Test GET /health."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"


def test_custom_404_error(client):
    """Test that nonexistent routes return The Room themed 404."""
    response = client.get("/non-existent-endpoint-xyz")
    assert response.status_code == 404
    data = response.get_json()
    assert "You're tearing me apart!" in data["error"]
