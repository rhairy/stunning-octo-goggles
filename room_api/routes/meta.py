"""Meta and catalog endpoints for The Room Dialogue API."""

from flask import Blueprint, jsonify, request
from room_api.data.quotes import (
    get_all_quotes,
    get_characters,
    get_quotes_by_character,
    get_random_quote,
    search_quotes,
    QUOTES,
)

meta_bp = Blueprint("meta", __name__)


@meta_bp.route("/", methods=["GET"])
def api_index():
    """Root endpoint providing API documentation and discovery."""
    endpoints_summary = [
        {"endpoint": q["endpoint"], "quote": q["quote"], "character": q["character"]}
        for q in QUOTES
    ]
    return jsonify(
        {
            "name": "The Room Dialogue REST API",
            "film": "The Room (2003)",
            "director": "Tommy Wiseau",
            "description": "Scaffolded RESTful API serving iconic dialogue exchanges as JSON objects.",
            "example_request": "/whos-the-client",
            "example_response": {
                "character": "Johnny",
                "dialogue": "I cannot tell you, it's confidential.",
                "endpoint": "/whos-the-client",
                "quote": "I cannot tell you, it's confidential.",
                "scene": "Bank office discussion",
            },
            "discovery_routes": {
                "dialogue_endpoints": "/endpoints",
                "all_quotes": "/quotes",
                "random_quote": "/quotes/random",
                "characters": "/characters",
                "health_check": "/health",
            },
            "available_endpoints_count": len(QUOTES),
            "endpoints": endpoints_summary,
        }
    )


@meta_bp.route("/endpoints", methods=["GET"])
def list_endpoints():
    """List all available dialogue endpoints."""
    routes = [
        {
            "endpoint": q["endpoint"],
            "prompt": q["prompt"],
            "character": q["character"],
            "quote": q["quote"],
        }
        for q in QUOTES
    ]
    return jsonify({
        "count": len(routes),
        "endpoints": routes,
    })


@meta_bp.route("/quotes", methods=["GET"])
def list_quotes():
    """List or search quotes with query parameters.
    
    Supported query parameters:
        character: Filter by character name (e.g. ?character=Johnny)
        search: Free text search in quote, character, or scene
        limit: Max number of quotes to return
    """
    character = request.args.get("character")
    search = request.args.get("search")
    limit = request.args.get("limit", type=int)

    if character:
        results = get_quotes_by_character(character)
    elif search:
        results = search_quotes(search)
    else:
        results = get_all_quotes()

    if limit and limit > 0:
        results = results[:limit]

    return jsonify({
        "count": len(results),
        "results": results,
    })


@meta_bp.route("/quotes/random", methods=["GET"])
def random_quote():
    """Return a random quote from the film."""
    quote_data = get_random_quote()
    return jsonify(quote_data)


@meta_bp.route("/characters", methods=["GET"])
def list_characters():
    """List characters with quote counts."""
    characters = get_characters()
    return jsonify({
        "count": len(characters),
        "characters": characters,
    })


@meta_bp.route("/health", methods=["GET"])
def health_check():
    """API health status endpoint."""
    return jsonify({
        "status": "healthy",
        "message": "Don't worry about it. Everything will be fine.",
    })
