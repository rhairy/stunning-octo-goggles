"""Dialogue endpoints from The Room (2003)."""

from flask import Blueprint, jsonify, request, Response
from room_api.data.quotes import QUOTES, get_quote_by_slug

dialogue_bp = Blueprint("dialogue", __name__)


def _format_quote_response(quote_data: dict) -> Response:
    """Format quote dictionary based on optional query parameter formatting."""
    fmt = request.args.get("format", "").lower()
    if fmt in ("simple", "minimal"):
        return jsonify({"quote": quote_data["quote"]})
    if fmt == "dialogue":
        return jsonify({
            "character": quote_data["character"],
            "dialogue": quote_data["quote"],
        })
    # Default rich response
    return jsonify({
        "endpoint": quote_data["endpoint"],
        "quote": quote_data["quote"],
        "dialogue": quote_data["quote"],
        "character": quote_data["character"],
        "spoken_to": quote_data.get("spoken_to"),
        "scene": quote_data.get("scene"),
        "prompt": quote_data.get("prompt"),
        "context": quote_data.get("context"),
        "follow_up": quote_data.get("follow_up"),
    })


@dialogue_bp.route("/whos-the-client", methods=["GET"], strict_slashes=False)
@dialogue_bp.route("/api/whos-the-client", methods=["GET"], strict_slashes=False)
@dialogue_bp.route("/api/v1/whos-the-client", methods=["GET"], strict_slashes=False)
def whos_the_client():
    """Specific endpoint for Johnny's confidential banking client inquiry.
    
    Returns:
        JSON object containing "I cannot tell you, it's confidential."
    """
    quote_data = get_quote_by_slug("whos-the-client")
    if not quote_data:
        return jsonify({"error": "Quote not found"}), 404
    return _format_quote_response(quote_data)


# Dynamically register endpoints for each dialogue quote in catalog
def _create_slug_handler(slug: str):
    def handler():
        data = get_quote_by_slug(slug)
        if not data:
            return jsonify({"error": "Quote not found"}), 404
        return _format_quote_response(data)

    handler.__name__ = f"quote_endpoint_{slug.replace('-', '_')}"
    return handler


for q in QUOTES:
    slug = q["slug"]
    if slug != "whos-the-client":  # already defined explicitly above
        handler = _create_slug_handler(slug)
        dialogue_bp.add_url_rule(f"/{slug}", endpoint=f"quote_{slug}", view_func=handler, strict_slashes=False)
        dialogue_bp.add_url_rule(f"/api/{slug}", endpoint=f"quote_api_{slug}", view_func=handler, strict_slashes=False)
        dialogue_bp.add_url_rule(f"/api/v1/{slug}", endpoint=f"quote_api_v1_{slug}", view_func=handler, strict_slashes=False)


@dialogue_bp.route("/dialogue/<slug>", methods=["GET"], strict_slashes=False)
def get_dialogue_by_param(slug: str):
    """Retrieve dialogue for any slug via path parameter."""
    quote_data = get_quote_by_slug(slug)
    if not quote_data:
        return (
            jsonify(
                {
                    "error": f"Dialogue slug '{slug}' not found.",
                    "status": 404,
                    "suggestion": "Check /endpoints to see all available slugs.",
                }
            ),
            404,
        )
    return _format_quote_response(quote_data)
