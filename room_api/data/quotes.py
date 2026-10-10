"""Dialogue data and lookup helpers from Tommy Wiseau's 'The Room' (2003)."""

from __future__ import annotations
import random
from typing import Dict, List, Optional, Any

# Primary dialogue repository
QUOTES: List[Dict[str, Any]] = [
    {
        "slug": "whos-the-client",
        "endpoint": "/whos-the-client",
        "quote": "I cannot tell you, it's confidential.",
        "character": "Johnny",
        "spoken_to": "Mark",
        "scene": "Bank office discussion",
        "prompt": "Who's the client?",
        "context": "Mark asks Johnny about a big client at the bank.",
        "follow_up": "Aw, come on, why not? / No, I can't. Anyway, how's your sex life?",
    },
    {
        "slug": "did-you-hit-her",
        "endpoint": "/did-you-hit-her",
        "quote": "I did not hit her, it's not true, it's bullshit, I did not hit her. I did not... Oh, hi Mark.",
        "character": "Johnny",
        "spoken_to": "Mark",
        "scene": "Rooftop water bottle toss",
        "prompt": "Did you hit her?",
        "context": "Johnny vents about domestic accusations before casually greeting Mark.",
        "follow_up": "Oh, hey Johnny, what's up?",
    },
    {
        "slug": "hows-your-sex-life",
        "endpoint": "/hows-your-sex-life",
        "quote": "Anyway, how's your sex life?",
        "character": "Johnny",
        "spoken_to": "Mark",
        "scene": "Bank stairs / Rooftop",
        "prompt": "How are things going with you?",
        "context": "Abrupt subject change following confidential banking inquiries.",
        "follow_up": "Can't talk about it.",
    },
    {
        "slug": "youre-tearing-me-apart",
        "endpoint": "/youre-tearing-me-apart",
        "quote": "You're tearing me apart, Lisa!",
        "character": "Johnny",
        "spoken_to": "Lisa",
        "scene": "Living room argument",
        "prompt": "What are you doing to me?",
        "context": "Johnny reacts in anguish to Lisa's manipulation.",
        "follow_up": "Why are you so hysterical?",
    },
    {
        "slug": "hi-doggie",
        "endpoint": "/hi-doggie",
        "quote": "Hi doggie.",
        "character": "Johnny",
        "spoken_to": "Pug on counter",
        "scene": "San Francisco flower shop",
        "prompt": "Do you acknowledge the canine?",
        "context": "Johnny greets the flower shop dog while purchasing red roses.",
        "follow_up": "You're my favorite customer.",
    },
    {
        "slug": "youre-my-favorite-customer",
        "endpoint": "/youre-my-favorite-customer",
        "quote": "You're my favorite customer.",
        "character": "Flower Shop Clerk",
        "spoken_to": "Johnny",
        "scene": "San Francisco flower shop",
        "prompt": "What does the florist think of Johnny?",
        "context": "The florist fails to recognize Johnny until he takes off his sunglasses.",
        "follow_up": "Thanks a lot, bye!",
    },
    {
        "slug": "what-a-story-mark",
        "endpoint": "/what-a-story-mark",
        "quote": "Haha, what a story, Mark!",
        "character": "Johnny",
        "spoken_to": "Mark",
        "scene": "Coffee shop patio",
        "prompt": "Did you hear about the woman who got beaten up?",
        "context": "Johnny laughs dismissively after Mark shares a grim anecdote about domestic violence.",
        "follow_up": "Yeah, you can say that again.",
    },
    {
        "slug": "breast-cancer",
        "endpoint": "/breast-cancer",
        "quote": "I definitely have breast cancer.",
        "character": "Claudette",
        "spoken_to": "Lisa",
        "scene": "Living room sofa",
        "prompt": "Mom, what did the doctor say?",
        "context": "Claudette casually reveals a severe medical diagnosis that is never mentioned again.",
        "follow_up": "Don't worry about it. They're curing lots of people every day.",
    },
    {
        "slug": "where-is-my-money",
        "endpoint": "/where-is-my-money",
        "quote": "Where's my fucking money, Denny?!",
        "character": "Chris-R",
        "spoken_to": "Denny",
        "scene": "Rooftop confrontation",
        "prompt": "What does Chris-R want?",
        "context": "Chris-R brandishes a gun demanding payment from Denny.",
        "follow_up": "It's coming! It's just a couple more minutes!",
    },
    {
        "slug": "leave-your-stupid-comments-in-your-pocket",
        "endpoint": "/leave-your-stupid-comments-in-your-pocket",
        "quote": "Leave your stupid comments in your pocket!",
        "character": "Mark",
        "spoken_to": "Peter",
        "scene": "Living room tuxedo chat",
        "prompt": "Can I share some psychological insight?",
        "context": "Mark shuts down Peter the psychologist during tuxedo fitting banter.",
        "follow_up": "What's the matter with you?",
    },
    {
        "slug": "chicken",
        "endpoint": "/chicken",
        "quote": "Cheep cheep cheep cheep cheep!",
        "character": "Johnny",
        "spoken_to": "Mark & Peter",
        "scene": "Alleyway / Apartment",
        "prompt": "Are you afraid?",
        "context": "Johnny taunts his friends by flapping his arms like a chicken.",
        "follow_up": "Who are you calling a chicken?",
    },
    {
        "slug": "two-is-company",
        "endpoint": "/two-is-company",
        "quote": "Two's company, three's a crowd. I just like to watch you guys.",
        "character": "Denny",
        "spoken_to": "Johnny & Lisa",
        "scene": "Johnny and Lisa's bedroom",
        "prompt": "Denny, why are you in our bed eating pillows?",
        "context": "Denny joins Johnny and Lisa in their bedroom unexpectedly.",
        "follow_up": "Denny, you have to go now.",
    },
    {
        "slug": "me-underwears",
        "endpoint": "/me-underwears",
        "quote": "Me underwears?",
        "character": "Mark",
        "spoken_to": "Johnny",
        "scene": "Living room tuxedo fitting",
        "prompt": "What are you doing with those?",
        "context": "Johnny tosses underwear at Mark.",
        "follow_up": "What are you doing, man?",
    },
    {
        "slug": "everybody-betray-me",
        "endpoint": "/everybody-betray-me",
        "quote": "Everybody betray me! I'm fed up with this world!",
        "character": "Johnny",
        "spoken_to": "Everyone",
        "scene": "Birthday party climax",
        "prompt": "Johnny, how are you feeling right now?",
        "context": "Johnny has a breakdown after discovering Lisa and Mark's affair.",
        "follow_up": "Johnny, calm down!",
    },
    {
        "slug": "oh-hi-mark",
        "endpoint": "/oh-hi-mark",
        "quote": "Oh, hi Mark.",
        "character": "Johnny",
        "spoken_to": "Mark",
        "scene": "Rooftop entrance",
        "prompt": "Oh hi Johnny.",
        "context": "Johnny transitions instantly from fury to a calm, friendly greeting.",
        "follow_up": "Hey Johnny, what's going on?",
    },
    {
        "slug": "dont-worry-about-it",
        "endpoint": "/dont-worry-about-it",
        "quote": "Don't worry about it. Everything will be fine.",
        "character": "Johnny",
        "spoken_to": "Lisa",
        "scene": "Kitchen",
        "prompt": "What should we do?",
        "context": "Johnny's universal coping mechanism.",
        "follow_up": "I'm sure it will be.",
    },
    {
        "slug": "do-you-understand-life",
        "endpoint": "/do-you-understand-life",
        "quote": "Do you understand life? Do you?!",
        "character": "Johnny",
        "spoken_to": "Mark",
        "scene": "Coffee shop patio",
        "prompt": "Do you understand life?",
        "context": "Johnny questions the nature of human existence while drinking coffee.",
        "follow_up": "People are strange these days.",
    },
    {
        "slug": "you-are-lying",
        "endpoint": "/you-are-lying",
        "quote": "You are lying, I never hit you! You are tearing me apart, Lisa!",
        "character": "Johnny",
        "spoken_to": "Lisa",
        "scene": "Living room confrontation",
        "prompt": "Lisa says you hit her!",
        "context": "Johnny confronts Lisa about false accusations.",
        "follow_up": "You don't understand anything!",
    },
    {
        "slug": "im-tired-im-wasted-i-love-you-darling",
        "endpoint": "/im-tired-im-wasted-i-love-you-darling",
        "quote": "I'm tired, I'm wasted, I love you darling!",
        "character": "Johnny",
        "spoken_to": "Lisa",
        "scene": "Apartment doorway",
        "prompt": "How are you feeling after drinking with the guys?",
        "context": "Johnny returns home from a night out.",
        "follow_up": "Come to bed, Johnny.",
    },
    {
        "slug": "keep-your-stupid-comments-in-your-pocket",
        "endpoint": "/keep-your-stupid-comments-in-your-pocket",
        "quote": "Leave your stupid comments in your pocket!",
        "character": "Mark",
        "spoken_to": "Peter",
        "scene": "Living room tuxedo chat",
        "prompt": "Can I give my opinion?",
        "context": "Alternative phrasing for the classic pocket comment.",
        "follow_up": "What's the matter with you?",
    },
    {
        "slug": "im-going-to-take-a-nap",
        "endpoint": "/im-going-to-take-a-nap",
        "quote": "It's nice to see you Denny, I'm going to take a nap.",
        "character": "Tommy",
        "spoken_to": "Denny",
        "scene": "Intro",
        "prompt": "It's nice to see you Denny.",
        "context": "Johnny wants some alone time with Lisa",
        "follow_up": "None",
    }
]

# Slug to quote dictionary for fast lookup
_SLUG_MAP: Dict[str, Dict[str, Any]] = {q["slug"]: q for q in QUOTES}


def get_all_quotes() -> List[Dict[str, Any]]:
    """Return all quotes in the catalog."""
    return list(QUOTES)


def get_quote_by_slug(slug: str) -> Optional[Dict[str, Any]]:
    """Lookup a quote by its URL slug (e.g. 'whos-the-client')."""
    cleaned = slug.strip("/").lower()
    return _SLUG_MAP.get(cleaned)


def get_quotes_by_character(character_name: str) -> List[Dict[str, Any]]:
    """Filter quotes by character (case-insensitive substring match)."""
    search_term = character_name.strip().lower()
    return [q for q in QUOTES if search_term in q["character"].lower()]


def search_quotes(query: str) -> List[Dict[str, Any]]:
    """Search quotes by quote text, character, scene, or prompt."""
    term = query.strip().lower()
    return [
        q
        for q in QUOTES
        if term in q["quote"].lower()
        or term in q["character"].lower()
        or term in q["scene"].lower()
        or term in q["prompt"].lower()
    ]


def get_random_quote() -> Dict[str, Any]:
    """Return a random quote from the collection."""
    return random.choice(QUOTES)


def get_characters() -> List[Dict[str, Any]]:
    """Return list of distinct characters and count of their quotes."""
    counts: Dict[str, int] = {}
    for q in QUOTES:
        char = q["character"]
        counts[char] = counts.get(char, 0) + 1
    return [{"character": char, "quote_count": count} for char, count in sorted(counts.items())]
