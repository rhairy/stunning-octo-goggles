"""Routes module for The Room Dialogue API."""
from room_api.routes.dialogue import dialogue_bp
from room_api.routes.meta import meta_bp

__all__ = ["dialogue_bp", "meta_bp"]
