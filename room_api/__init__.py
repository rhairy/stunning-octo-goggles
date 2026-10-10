"""The Room (2003) Dialogue API package."""

from flask import Flask, jsonify
from room_api.routes.dialogue import dialogue_bp
from room_api.routes.meta import meta_bp


def create_app(test_config=None) -> Flask:
    """Application factory for The Room Dialogue API."""
    app = Flask(__name__)

    # Default configuration
    app.config.from_mapping(
        SECRET_KEY="oh-hi-mark",
        JSON_SORT_KEYS=False,
    )

    if test_config:
        app.config.update(test_config)

    # Register blueprints
    app.register_blueprint(dialogue_bp)
    app.register_blueprint(meta_bp)

    # Friendly Room-themed 404 handler
    @app.errorhandler(404)
    def page_not_found(e):
        return (
            jsonify(
                {
                    "error": "You're tearing me apart! Route not found.",
                    "status": 404,
                    "quote": "What a story, Mark! But this endpoint doesn't exist.",
                    "help": "Visit / or /endpoints to see all available quotes and dialogue endpoints.",
                }
            ),
            404,
        )

    # Generic 500 handler
    @app.errorhandler(500)
    def internal_error(e):
        return (
            jsonify(
                {
                    "error": "Everybody betray me! Internal server error.",
                    "status": 500,
                }
            ),
            500,
        )

    return app
