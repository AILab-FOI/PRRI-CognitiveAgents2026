from __future__ import annotations

import asyncio
import logging
import threading
from pathlib import Path
from typing import Dict, List, Tuple

from flask import Flask, jsonify, render_template, request, send_from_directory

try:
    from websockets.asyncio.server import serve
except ImportError:
    from websockets.server import serve


BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
MEDIA_DIR = STATIC_DIR / "media"
TEMPLATE_DIR = BASE_DIR / "templates"

app = Flask(
    __name__,
    static_folder=str(STATIC_DIR),
    template_folder=str(TEMPLATE_DIR),
)

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
)


@app.route("/")
def home():
    return send_from_directory(STATIC_DIR, "index.html")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(STATIC_DIR, "favicon.ico")


@app.route("/media/<path:filename>")
def serve_media(filename):
    return send_from_directory(MEDIA_DIR, filename)


@app.route("/agent-exception")
def agent_exception():
    return render_template("exception.html")


@app.route("/agent-engineer")
def agent_engineer():
    return render_template("engineer.html")


@app.route("/agent-analyst")
def agent_analyst():
    return render_template("analyst.html")


@app.route("/agent-cartographer")
def agent_cartographer():
    return render_template("cartographer.html")


@app.route("/agent-narrator")
def agent_narrator():
    return render_template("narrator.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(error):
    return render_template("500.html"), 500


Rule = Tuple[Tuple[str, ...], str]


COMMON_RULES: List[Rule] = [
    (("hvala", "thank"), "hvala"),
    (("bravo", "dobro", "dobar", "super"), "dobro"),
    (("ponovi", "opet", "ponovno"), "ponovi"),
    (("bok", "pozdrav", "hello", "hi"), "izvoli"),
    (("kako si", "kako ste"), "dobro"),
    (("je li ti lijepo", "lijepo"), "lijepo"),
    (("tko te napravio", "napravio", "stvorio"), "predstavljanje-dugo"),
    (("tko si", "što si", "ko si"), "predstavljanje-kratko"),
]


AGENT_RULES: Dict[str, List[Rule]] = {
    "engineer": [
        (("jezgra", "core", "reaktor", "energija"), "18"),
        (("brod", "sustav", "motor", "inženjer", "engineer"), "predstavljanje-kratko"),
        (("put", "prolaz", "vrata", "servisni"), "16"),
        (("opasno", "rizik", "pazi", "nestabilno"), "20"),
    ],
    "analyst": [
        (("uzorak", "sample", "biologija", "organizam"), "18"),
        (("čovjek", "human", "ljudi", "vrsta"), "predstavljanje-kratko"),
        (("strah", "bol", "eksperiment"), "20"),
        (("zašto", "proučavate", "promatrate"), "16"),
    ],
    "cartographer": [
        (("zemlja", "earth", "planet", "dom"), "18"),
        (("death world", "smrt", "rat", "sukob"), "20"),
        (("karta", "arhiva", "mapa", "orbita"), "predstavljanje-kratko"),
        (("teleskop", "zvijezde", "svemir"), "16"),
    ],
    "exception": [
        (("narator", "glas", "signal", "sekundarni"), "18"),
        (("tijelo", "mrtav", "prethodni", "čovjek"), "20"),
        (("iznimka", "exception", "anomalija"), "predstavljanje-kratko"),
        (("čuješ", "vidiš", "znaš"), "16"),
    ],
    "narrator": [
        (("tko si", "who are you", "identitet", "pravo ime"), "Who"),
        (("što trebaš", "what need", "trebaš od mene", "misija", "zašto sam"), "What-Need"),
        (("iskoristio", "used me", "upotrijebio", "koristio me"), "Used-Me"),
        (("biočip", "biochip", "čip", "chip", "gledao si me"), "Biochip"),
        (("tijelo", "body", "trup", "prethodni", "mrtav"), "Body"),
        (("organizacija", "organization", "organisation", "naručili", "naručio"), "Organization"),
        (("tuguješ", "grieve", "žalovao", "žalost", "prva osoba"), "Grieve"),
        (("vjeruješ", "believe", "vjera", "vrijedi li", "čovječanstvo"), "Believe"),
    ],
}


AGENT_TEXT: Dict[str, str] = {
    "engineer": (
        "I maintain the vessel systems. The core is sensitive, but access is possible "
        "through lower service routing."
    ),
    "analyst": (
        "You are a conflict-adapted organism. Your species produces contradictory "
        "survival patterns."
    ),
    "cartographer": (
        "Earth is classified as a death world. Not dead — shaped by conflict, scarcity "
        "and adaptation."
    ),
    "exception": (
        "I detect a secondary signal inside the organism. Its origin does not match "
        "the current biological pattern."
    ),
    "narrator": (
        "I have been on this vessel for a very long time. You are the second person "
        "I have brought here. I am sorry about the first one."
    ),
}


AGENT_PORTS: Dict[str, int] = {
    "engineer": 8009,
    "analyst": 8010,
    "cartographer": 8011,
    "exception": 8012,
    "narrator": 8013,
}


def normalize_message(message: str) -> str:
    return message.lower().strip()


def choose_clip(agent_name: str, message: str) -> str:
    normalized = normalize_message(message)

    if not normalized or normalized == "connect":
        return "tisina"

    rules = AGENT_RULES.get(agent_name, []) + COMMON_RULES

    for keywords, clip in rules:
        if any(keyword in normalized for keyword in keywords):
            return clip

    return "tisina"


def choose_text(agent_name: str, message: str) -> str:
    normalized = normalize_message(message)

    if not normalized:
        return "Signal nije primljen."

    if "hvala" in normalized:
        return "Response acknowledged."

    if "ponovi" in normalized:
        return AGENT_TEXT.get(agent_name, "Pattern not classified.")

    return AGENT_TEXT.get(agent_name, "Pattern not classified.")


@app.route("/api/agent/<agent_name>", methods=["POST"])
def api_agent(agent_name: str):
    if agent_name not in AGENT_PORTS:
        return jsonify({"error": "Unknown agent"}), 404

    data = request.get_json(silent=True) or {}
    message = data.get("message", "")

    return jsonify(
        {
            "agent": agent_name,
            "message": message,
            "response": choose_text(agent_name, message),
            "clip": choose_clip(agent_name, message),
        }
    )


async def run_agent_websocket(agent_name: str, port: int):
    async def handler(websocket):
        logging.info("%s connected on port %s", agent_name, port)

        try:
            await websocket.send("tisina")

            async for message in websocket:
                logging.info("[%s] received: %s", agent_name, message)

                clip = choose_clip(agent_name, str(message))
                logging.info("[%s] sending clip: %s", agent_name, clip)

                await websocket.send(clip)

        except Exception as error:
            logging.warning("%s websocket closed: %s", agent_name, error)

    async with serve(handler, "127.0.0.1", port):
        logging.info("%s websocket running on ws://localhost:%s", agent_name, port)
        await asyncio.Future()


def start_websocket_thread(agent_name: str, port: int):
    def runner():
        asyncio.run(run_agent_websocket(agent_name, port))

    thread = threading.Thread(target=runner, daemon=True)
    thread.start()


def start_all_websockets():
    for agent_name, port in AGENT_PORTS.items():
        start_websocket_thread(agent_name, port)


if __name__ == "__main__":
    start_all_websockets()

    logging.info("Flask server running on http://127.0.0.1:5000")
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True,
        use_reloader=False,
    )