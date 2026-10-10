# 🎬 The Room Dialogue REST API

A Flask RESTful API serving iconic dialogue exchanges from Tommy Wiseau's cult masterpiece ***The Room* (2003)** as JSON objects.

---

## 🚀 Quickstart

### 1. Activate the Virtual Environment

```bash
source .venv/bin/activate
```

*(If creating a fresh virtual environment from scratch)*:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Start the API Server

Using the included runner:
```bash
python run.py
```

Or using Flask CLI:
```bash
export FLASK_APP=wsgi.py
flask run --port 5000
```

Or using Gunicorn:
```bash
gunicorn --bind 127.0.0.1:5000 wsgi:app
```

The server will start at `http://127.0.0.1:5000`.

---

## 💬 Example Request: `/whos-the-client`

```bash
curl http://127.0.0.1:5000/whos-the-client
```

### Response:
```json
{
  "character": "Johnny",
  "context": "Mark asks Johnny about a big client at the bank.",
  "dialogue": "I cannot tell you, it's confidential.",
  "endpoint": "/whos-the-client",
  "follow_up": "Aw, come on, why not? / No, I can't. Anyway, how's your sex life?",
  "prompt": "Who's the client?",
  "quote": "I cannot tell you, it's confidential.",
  "scene": "Bank office discussion",
  "spoken_to": "Mark"
}
```

### Optional Formats
Pass `?format=simple` to receive only the quote:
```bash
curl "http://127.0.0.1:5000/whos-the-client?format=simple"
```
```json
{
  "quote": "I cannot tell you, it's confidential."
}
```

Pass `?format=dialogue` to receive character + dialogue:
```bash
curl "http://127.0.0.1:5000/whos-the-client?format=dialogue"
```
```json
{
  "character": "Johnny",
  "dialogue": "I cannot tell you, it's confidential."
}
```

---

## 🎭 Iconic Dialogue Endpoints

Every endpoint can be reached directly (e.g. `/whos-the-client`), or prefixed with `/api` or `/api/v1`:

| Endpoint | Character | Quote |
| :--- | :--- | :--- |
| `/whos-the-client` | Johnny | *"I cannot tell you, it's confidential."* |
| `/did-you-hit-her` | Johnny | *"I did not hit her, it's not true, it's bullshit, I did not hit her. I did not... Oh, hi Mark."* |
| `/hows-your-sex-life` | Johnny | *"Anyway, how's your sex life?"* |
| `/youre-tearing-me-apart` | Johnny | *"You're tearing me apart, Lisa!"* |
| `/hi-doggie` | Johnny | *"Hi doggie."* |
| `/youre-my-favorite-customer` | Flower Clerk | *"You're my favorite customer."* |
| `/what-a-story-mark` | Johnny | *"Haha, what a story, Mark!"* |
| `/breast-cancer` | Claudette | *"I definitely have breast cancer."* |
| `/where-is-my-money` | Chris-R | *"Where's my fucking money, Denny?!"* |
| `/leave-your-stupid-comments-in-your-pocket` | Mark | *"Leave your stupid comments in your pocket!"* |
| `/chicken` | Johnny | *"Cheep cheep cheep cheep cheep!"* |
| `/two-is-company` | Denny | *"Two's company, three's a crowd. I just like to watch you guys."* |
| `/me-underwears` | Mark | *"Me underwears?"* |
| `/everybody-betray-me` | Johnny | *"Everybody betray me! I'm fed up with this world!"* |
| `/oh-hi-mark` | Johnny | *"Oh, hi Mark."* |
| `/dont-worry-about-it` | Johnny | *"Don't worry about it. Everything will be fine."* |
| `/do-you-understand-life` | Johnny | *"Do you understand life? Do you?!"* |
| `/you-are-lying` | Johnny | *"You are lying, I never hit you! You are tearing me apart, Lisa!"* |
| `/im-tired-im-wasted-i-love-you-darling` | Johnny | *"I'm tired, I'm wasted, I love you darling!"* |

---

## 🔍 Discovery & Meta Endpoints

- `GET /` - Root overview with API metadata and list of all available endpoints.
- `GET /endpoints` - Directory of all dialogue endpoints and prompts.
- `GET /quotes` - Full quotes repository with query filtering:
  - `?character=Johnny` – Filter by character name.
  - `?search=breast` – Search quotes, characters, and scenes.
  - `?limit=5` – Limit result count.
- `GET /quotes/random` - Returns a random quote.
- `GET /characters` - Returns all characters and their quote counts.
- `GET /health` - Health check status.
- `GET /dialogue/<slug>` - Parameterized slug lookup (e.g. `/dialogue/chicken`).

---

## 🧪 Running Tests

Run the full pytest suite:

```bash
pytest -v
```

All unit and integration tests verify status codes, JSON response formatting, query parameters, character filtering, and error handling.

---

## 🐳 Docker

Build and run with Docker:

```bash
docker build -t the-room-api .
docker run -p 5000:5000 the-room-api
```
