from __future__ import annotations

import asyncio
import logging
import re
import threading
import unicodedata
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
    (("ponovi", "repeat", "again", "opet", "ponovno"), "ponovi"),
    (("hvala", "thank", "thanks", "ok", "okay"), "tisina"),
]


AGENT_RULES: Dict[str, List[Rule]] = {
    "engineer": [
        (("hello", "hi", "bok", "pozdrav"), "Hello"),
        (("who are you", "who", "engineer", "tko si", "ko si"), "Who"),
        (("what are you", "what do you", "what", "sto si", "sta si"), "What"),
        (("core", "reactor", "energy", "jezgra"), "What"),
        (("route c", "option c", "third option"), "C"),
        (("research intro", "research", "experiment"), "Research-Intro"),
        (("no", "not really", "i do not"), "No"),
        (("rifle force", "force"), "Rifle-Force"),
        (("rifle power", "power"), "Rifle-Power"),
        (("rifle war", "war"), "Rifle-War"),
        (("rifle", "weapon", "gun", "puska"), "Rifle"),
        (("camera memory", "memory"), "Camera-Memory"),
        (("camera share", "share"), "Camera-Share"),
        (("camera obsession", "obsession", "obsessed"), "Camera-Obsession"),
        (("imprecision", "imprecise"), "Camera-Imprecision"),
        (("accuracy", "accurate", "precise"), "Camera-Accuracy"),
        (("alone", "lonely"), "Camera-Alone"),
        (("residue", "left behind"), "Camera-Residue"),
        (("point", "what is the point"), "Camera-Point"),
        (("problem", "issue"), "Camera-Problem"),
        (("camera", "recording", "watch"), "Camera"),
        (("leave", "exit", "go back", "done"), "Leave"),
    ],
    "analyst": [
        (("brain", "biochip", "chip", "memory implant"), "Brain"),
        (("place", "where am i", "what place", "room"), "Place"),
        (("alive", "living", "moving"), "Alive"),
        (("studying", "study", "researching", "observe"), "Studying"),
        (("wrong", "immoral", "unethical", "this is wrong"), "Wrong"),
        (("no memory", "memory", "remember"), "Memory"),
        (("who i am", "identity", "meant to be"), "Who-I"),
        (("why build", "build", "built"), "Build"),
        (("worse", "worst"), "Worse"),
        (("recording", "record"), "Recording"),
        (("compare", "comparison"), "Compare"),
        (("sample", "specimen", "organism"), "Sample"),
        (("feel alive", "feels alive"), "Feel-Alive"),
        (("blurry", "definition"), "Blurry"),
        (("consent", "permission"), "Consent"),
        (("objects", "object"), "Objects"),
        (("understand", "do not understand", "dont understand"), "Understand"),
        (("of course", "course"), "Course"),
        (("why doing", "why are you doing"), "Why-Doing"),
        (("learned", "learn"), "Learned"),
        (("puzzle", "signal", "test"), "Puzzle-Intro"),
        (("left", "left option"), "Left"),
        (("right", "right option"), "Right"),
        (("probability", "chance"), "Probability"),
        (("no signal", "without signal"), "No-Signal"),
        (("greater design", "design"), "Greater-Design"),
        (("carry yes", "yes carry"), "Carry-Yes"),
        (("carry know", "i know"), "Carry-Know"),
        (("carry used", "used to"), "Carry-Used"),
        (("carry no", "no carry"), "Carry-No"),
        (("exit", "leave"), "Exit"),
        (("moving", "move"), "Moving"),
    ],
    "cartographer": [
        (("threatening", "threats", "dangerous"), "Threatening"),
        (("effort", "work", "try"), "Effort"),
        (("death world", "deathworld", "earth", "planet"), "Deathworld"),
        (("join", "research", "study with you"), "Join"),
        (("rage", "angry", "brain rage"), "Rage"),
        (("skeptic", "doubt", "skeptical"), "Skeptic"),
        (("accept", "accepted"), "Accept"),
        (("permanent", "forever"), "Permanent"),
        (("hit it in the leg", "leg"), "Punch"),
        (("hit", "punch", "strike"), "Threat"),
        (("puzzle war", "image of war"), "Puzzle-War"),
        (("puzzle sacrifice", "sacrifice"), "Puzzle-Sacrifice"),
        (("puzzle science", "science"), "Puzzle-Science"),
        (("no conflict", "war no"), "War-No"),
        (("lifeform", "lifeforms"), "War-Lifeform"),
        (("war normal", "normal part"), "War-Normal"),
        (("parallel", "parallels"), "War-Parallels"),
        (("difference", "no difference"), "War-Difference"),
        (("shame", "ashamed"), "War-Shame"),
        (("weapons", "weapon"), "Science-Weapons"),
        (("your kind", "fundamentals"), "Science-Kind"),
        (("sacrifice death", "death"), "Sacrifice-Death"),
        (("no design", "design"), "Sacrifice-Design"),
        (("divine", "god"), "Sacrifice-Divine"),
        (("consciousness", "continuation"), "Sacrifice-Consciousness"),
        (("signal", "continue", "done"), "Signal"),
    ],
    "exception": [
        (("can you understand", "understand me", "hello", "hey"), "A"),
        (("what am i doing", "what am i even doing", "where am i"), "B"),
        (("escaped", "easily", "how did i escape"), "C"),
        (("human voice", "voice human"), "Voice-Human"),
        (("also hear", "you hear"), "Voice-Also-Hear"),
        (("where go", "where do i go"), "Where-Go"),
        (("voice saying", "what has the voice"), "Voice-Saying"),
        (("actual human", "really human"), "Voice-Actually-Human"),
        (("voice", "signal", "secondary"), "Voice"),
        (("passing through", "just passing"), "Passing-Through"),
        (("obsessed", "intent"), "A-Obsessed"),
        (("philosophical", "philosophy"), "A-Philosophical"),
        (("environment", "world come from"), "A-Environment"),
        (("who brought", "brought me"), "B-Who-Brought"),
        (("sold", "against my will"), "B-Sold"),
        (("back to earth", "bring me back"), "B-Earth"),
        (("want from me", "actually want"), "What-Want"),
        (("fight back", "fight"), "Fight-Back"),
        (("consent", "no consent"), "No-Consent"),
        (("uncompliant", "cooperate"), "Uncompliant"),
        (("trade", "cargo"), "C-Trade"),
        (("overlook home", "home"), "Overlook-Home"),
        (("overlook family", "family"), "Overlook-Family"),
        (("overlook distant", "distant"), "Overlook-Distant"),
        (("missed opportunities", "missed"), "Overlook-Missed"),
        (("nothing more", "nothing"), "Overlook-Nothing"),
        (("no memory", "memory"), "Overlook-No-Memory"),
        (("burned", "burnt"), "Overlook-Burned"),
        (("discarded why", "why are you here"), "Discarded-Why"),
        (("discarded know", "what do you know"), "Discarded-Know"),
        (("body", "dead", "corpse", "previous person"), "Discarded-What"),
        (("discarded what", "what are you"), "Discarded-What"),
        (("lying", "lie"), "Discarded-Lying"),
        (("why telling", "why tell"), "Discarded-Why-Telling"),
        (("what suggest", "suggest"), "Discarded-What-Suggest"),
        (("exit want", "what do you want"), "Exit-Want"),
        (("following", "follow"), "Exit-Following"),
        (("fine", "i do not mind", "i dont mind"), "Exit-Fine"),
        (("stopped", "stopped responding"), "Exit-Stopped"),
        (("yes", "bother yes"), "Exit-Yes"),
        (("no", "bother no"), "Exit-No"),
        (("archive", "go back"), "Archive"),
        (("pre control", "control room"), "Pre-Control-Room"),
    ],
    "narrator": [
        (("tell me", "would you tell"), "Tell-Me"),
        (("not answer", "answer is not"), "Not-Answer"),
        (("think you do", "i think you do"), "Think"),
        (("heard everything", "heard it all", "secret heard"), "Heard"),
        (("what need", "what do you need", "need from me", "mission"), "What-Need"),
        (("used me", "using me", "iskoristio"), "Used-Me"),
        (("biochip", "chip", "watch", "watching"), "Biochip"),
        (("body", "dead", "corpse", "previous person"), "Body"),
        (("organization", "organisation", "people behind"), "Organization"),
        (("now", "what now"), "Now"),
        (("grieve", "grief", "mourn"), "Grieve"),
        (("believe", "faith", "humanity"), "Believe"),
        (("intervene", "interfered", "nudged"), "Intervene"),
        (("continue", "panel", "decision"), "Continue"),
        (("who are you", "who", "identity", "name"), "Who"),
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
    normalized = unicodedata.normalize("NFKD", str(message).casefold())
    without_accents = "".join(
        char for char in normalized if not unicodedata.combining(char)
    )
    return re.sub(r"[^a-z0-9 -]+", " ", without_accents).strip()


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
