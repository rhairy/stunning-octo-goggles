"""WSGI entrypoint for The Room Dialogue API."""

from room_api import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
