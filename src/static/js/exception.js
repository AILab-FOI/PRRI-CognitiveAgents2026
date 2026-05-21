var DONT = false;
var FIRST = true;
var STOP = false;

var CURRENT_PASSAGE = "initial";

// Defines valid passages
var PASSAGE_STATES = {
  "initial": ["A", "B", "C", "Voice", "Passing-Through", "Overlook-Home", "Overlook-Family", "Overlook-Distant", "Overlook-Missed", "Overlook-Nothing", "Overlook-No-Memory", "Overlook-Burned", "Discarded-Why", "Discarded-Know", "Discarded-What", "Exit-Want", "Exit-Following", "Exit-Fine", "Exit-Stopped"],
  "3.1. Choice Voice": ["Voice-Human", "Voice-Also-Hear", "Where-Go"],
  "3.1. Human Voice": ["Voice-Saying", "Voice-Actually-Human", "Where-Go"],
  "3.1. Also Hear": ["Voice-Saying", "Voice-Actually-Human", "Where-Go"],
  "3.1. Where Go": ["Hallway"],
  "3.1. Voice Saying": ["Where-Go"],
  "3.1. Actually Human": ["Where-Go"],
  "3.1. Choice A": ["A-Obsessed", "B", "C"],
  "3.1. A Obsessed": ["A-Philosophical", "A-Enviroment"],
  "3.1. Philosophical": ["Hallway"],
  "3.1. Environment": ["Hallway"],
  "3.1. Choice B": ["B-Who-Brought"],
  "3.1. B Who Brought": ["B-Sold", "B-Earth"],
  "3.1. Back To Earth": ["What-Want", "Fight-Back"],
  "3.1. Sold Against Will": ["No-Consent", "Uncompliant"],
  //What do you want
  //Fight Back
  "3.1. No Consent": ["Hallway"],
  "3.1. Uncompliant": ["A-Philosophical", "A-Enviroment"],
  "3.1. Choice C": ["B-Who-Brought", "C-Trade"],
  "3.1. C Trade": ["B-Sold", "B-Earth"],
  "Discarded Exception Why": ["Discarded-Know", "Discarded-What", "Archive"],
  "Discarded Exception Know": ["Discarded-What", "Archive"],
  "Discarded Exception What": ["Discarded-Lying", "Discarded-Why-Telling", "Discarded-What-Suggest"],
  "Discarded What Suggest": ["Archive"],
  "Discarded Lying": [ "Discarded-Why-Telling", "Discarded-What-Suggest", "Archive"],
  "Discarded Why Telling": ["Discarded-What-Suggest", "Archive"],
  "Exit Exception Want": ["Exit-Yes", "Exit-No", "Pre-Control-Room"],
  "Exit Exception Bother Yes": ["Pre-Control-Room"],
  "Exit Exception Bother No": ["Pre-Control-Room"],
  //Exit Exception Stopped
  // Exit Exception Fine
  "Exit Exception Following": ["Pre-Control-Room"],
};

// Checks if valid transition
function canAdvance(responseCode) {
  var allowed = PASSAGE_STATES[CURRENT_PASSAGE] || [];
  return allowed.indexOf(responseCode) !== -1;
}

function tryAdvancePassage(targetPassage, responseCode) {
  if (!canAdvance(responseCode)) {
    console.warn(
      "[StateMachine] Blocked advance to '" +
        targetPassage +
        "'. " +
        "Response '" +
        responseCode +
        "' is not valid from passage '" +
        CURRENT_PASSAGE +
        "'.",
    );
    return;
  }

  console.log(
    "[StateMachine] Advancing from '" +
      CURRENT_PASSAGE +
      "' → '" +
      targetPassage +
      "'",
  );

  CURRENT_PASSAGE = targetPassage;

  window.parent.postMessage(
    {
      action: "advance_passage",
      targetPassage: targetPassage,
    },
    "*",
  );
}

// Updates Current passage if player moved using on screen choices
window.addEventListener("message", function (event) {
  if (event.data && event.data.action === "passage_changed") {
    console.log(
      "[StateMachine] Twine reported passage change → '" +
        event.data.passage +
        "'",
    );
    if (
      Object.prototype.hasOwnProperty.call(PASSAGE_STATES, event.data.passage)
    ) {
      CURRENT_PASSAGE = event.data.passage;
    }
  }

  if (event.data && event.data.action === "video_part_ended") {
    play_part("tisina");
    //if (!FIRST) DONT = true;
  }

  if (event.data && event.data.action === "stop_mic") {
      recognition.stop();
  }
});

$(window).on("load", function () {
  counter = 0;

  if (navigator.userAgent.indexOf("Firefox") > -1) {
    document.getElementById("notSupported").style.display = "block";
    document.getElementById("startupute").style.display = "none";
    document.getElementById("output").style.display = "none";
    document.querySelector(".video-container").style.display = "none";
  } else {
    const output = document.getElementById("output");
    const button = document.getElementById("start");
    const record = document.getElementById("record");
    window.output = output;

    const SpeechRecognition =
      window.SpeechRecognition || window.webkitSpeechRecognition;

    var init = function () {
      recognition = new SpeechRecognition();

      window.recognition = recognition;

      recognition.lang = "en-US";
      recognition.continuous = true;
      recognition.interimResults = false;

      recognition.onresult = (event) => {
        const current = event.resultIndex;
        const transcript = event.results[current][0].transcript;

        window.recognition.stop();
        STOP = true;
        output.innerHTML = transcript + " ";
        window.ws.send(transcript);
      };

      recognition.onspeechend = () => {
        window.recognition.stop();
        if (!DONT) {
            setTimeout(function () {
                try { window.recognition.start(); } catch (e) {}
            }, 400);
        }
      };

      recognition.onerror = (event) => {
        window.recognition.stop();
        if (!DONT) {
            setTimeout(function () {
                try { window.recognition.start(); } catch (e) {}
            }, 400);
        }
      };
    };
    init();

    button.onclick = () => {
      window.parent.postMessage({ action: 'hide_iframe' }, '*');
      play_part("tisina");
    };
  }

  record.onclick = () => {
    window.recognition.start();
  };
});

function connect() {
  ws = new WebSocket("ws://localhost:8012");
  window.ws = ws;
  ws.onopen = function () {
    ws.send("connect");
    DONT = false;
  };

  ws.onmessage = function (msg) {
    var response = msg.data.toString();
    console.log("[WS] Received:", response);

    if (response === "ponovi") {
        play_part("ponovi");
        return;   
    }

    switch (response) {
      case "A":
        tryAdvancePassage("3.1. Choice A", response);
        break;

      case "B":
        tryAdvancePassage("3.1. Choice B", response);
        break;

      case "C":
        tryAdvancePassage("3.1. Choice C", response);
        break;

      case "Voice":
        tryAdvancePassage("3.1. Choice Voice", response);
        break;

      case "Voice-Human":
        tryAdvancePassage("3.1. Human Voice", response);
        break;

      case "Voice-Also-Hear":
        tryAdvancePassage("3.1. Also Hear", response);
        break;

      case "Where-Go":
        tryAdvancePassage("3.1. Where Go", response);
        break;

      case "Voice-Saying":
        tryAdvancePassage("3.1. Voice Saying", response);
        break;

      case "Voice-Actually-Human":
        tryAdvancePassage("3.1. Actually Human", response);
        break;

      case "Hallway":
        tryAdvancePassage("Hallway Convergence", response);
        break;

      case "Passing-Through":
        tryAdvancePassage("3.1. Passing Through", response);
        break;

      case "A-Obsessed":
        tryAdvancePassage("3.1. A Obsessed", response);
        break;

      case "A-Philosophical":
        tryAdvancePassage("3.1. A Philosophical", response);
        break;

      case "A-Environment":
        tryAdvancePassage("3.1. A Environment", response);
        break;

      case "B-Who-Brought":
        tryAdvancePassage("3.1. B Who Brought", response);
        break;

      case "B-Sold":
        tryAdvancePassage("3.1. Sold Against Will", response);
        break;

      case "B-Earth":
        tryAdvancePassage("3.1. Back To Earth", response);
        break;

      case "What-Want":
        tryAdvancePassage("3.1. What Do You Want", response);
        break;

      case "Fight-Back":
        tryAdvancePassage("3.1. Fight Back", response);
        break;

      case "No-Consent":
        tryAdvancePassage("3.1. No Consent", response);
        break;

      case "Uncompliant":
        tryAdvancePassage("3.1. Uncompliant", response);
        break;

      case "C-Trade":
        tryAdvancePassage("3.1. C Trade", response);
        break;

      case "Overlook-Home":
        tryAdvancePassage("Overlook Home", response);
        break;

      case "Overlook-Family":
        tryAdvancePassage("Overlook Family", response);
        break;

      case "Overlook-Distant":
        tryAdvancePassage("Overlook Distant", response);
        break;

      case "Overlook-Missed":
        tryAdvancePassage("Overlook Missed", response);
        break;

      case "Overlook-Nothing":
        tryAdvancePassage("Overlook Nothing", response);
        break;

      case "Overlook-No-Memory":
        tryAdvancePassage("Overlook No Memory", response);
        break;

      case "Overlook-Burned":
        tryAdvancePassage("Overlook Burned", response);
        break;

      case "Discarded-Why":
        tryAdvancePassage("Discarded Exception Why", response);
        break;

      case "Discarded-Know":
        tryAdvancePassage("Discarded Exception Know", response);
        break;

      case "Discarded-What":
        tryAdvancePassage("Discarded Exception What", response);
        break;

      case "Archive":
        tryAdvancePassage("Archive Bay Entry", response);
        break;

      case "Discarded-Lying":
        tryAdvancePassage("Discarded Lying", response);
        break;

      case "Discarded-Why-Telling":
        tryAdvancePassage("Discarded Why Telling", response);
        break;

      case "Discarded-What-Suggest":
        tryAdvancePassage("Discarded What Suggest", response);
        break;

      case "Exit-Want":
        tryAdvancePassage("Exit Exception Want", response);
        break;

      case "Exit-Following":
        tryAdvancePassage("Exit Exception Following", response);
        break;

      case "Exit-Fine":
        tryAdvancePassage("Exit Exception Fine", response);
        break;

      case "Exit-Stopped":
        tryAdvancePassage("Exit Exception Stopped", response);
        break;

      case "Exit-Yes":
        tryAdvancePassage("Exit Exception Bother Yes", response);
        break;

      case "Exit-No":
        tryAdvancePassage("Exit Exception Bother No", response);
        break;

      case "Pre-Control-Room":
        tryAdvancePassage("Pre Control Room", response);
        break;

      default:
        break;
    }
  };

  ws.onclose = function (e) {
    console.log(
      "Socket is closed. Reconnect will be attempted in 1 second.",
      e.reason,
    );
    setTimeout(function () {
      connect();
    }, 1000);
  };

  ws.onerror = function (err) {
    console.error("Socket encountered error: ", err.message, "Closing socket");
    ws.close();
  };
}

connect();

right = {
  "text-align": "right",
  width: "1000px",
  "margin-right": "-400px auto",
};

LAST_PART = "";
CUR_PART = "tisina";
END = 278;

function play_part(part) {
  LAST_PART = CUR_PART;
  CUR_PART = part;
  var start = 0;
  var end = 0;

  DONT = part !== "tisina" ? true : false;

  recognition.stop();
  switch (part) {
    case "A":
      start = 1;
      end = 5;
      break;
    case "B":
      start = 1;
      end = 5;
      break;
    case "C":
      start = 1;
      end = 5;
      break;
    case "Voice":
      start = 1;
      end = 5;
      break;
    case "Voice-Human":
      start = 1;
      end = 5;
      break;
    case "Voice-Also-Hear":
      start = 1;
      end = 5;
      break;
    case "Where-Go":
      start = 1;
      end = 5;
      break;
    case "Voice-Saying":
      start = 1;
      end = 5;
      break;
    case "Voice-Actually-Human":
      start = 1;
      end = 5;
      break;
    case "Hallway":
      start = 1;
      end = 5;
      break;
    case "Passing-Through":
      start = 1;
      end = 5;
      break;
    case "A-Obsessed":
      start = 1;
      end = 5;
      break;
    case "A-Philosophical":
      start = 1;
      end = 5;
      break;
    case "A-Environment":
      start = 1;
      end = 5;
      break;
    case "B-Who-Brought":
      start = 1;
      end = 5;
      break;
    case "B-Sold":
      start = 1;
      end = 5;
      break;
    case "B-Earth":
      start = 1;
      end = 5;
      break;
    case "What-Want":
      start = 1;
      end = 5;
      break;
    case "Fight-Back":
      start = 1;
      end = 5;
      break;
    case "No-Consent":
      start = 1;
      end = 5;
      break;
    case "Uncompliant":
      start = 1;
      end = 5;
      break;
    case "C-Trade":
      start = 1;
      end = 5;
      break;
    case "Overlook-Home":
      start = 1;
      end = 5;
      break;
    case "Overlook-Family":
      start = 1;
      end = 5;
      break;
    case "Overlook-Distant":
      start = 1;
      end = 5;
      break;
    case "Overlook-Missed":
      start = 1;
      end = 5;
      break;
    case "Overlook-Nothing":
      start = 1;
      end = 5;
      break;
    case "Overlook-No-Memory":
      start = 1;
      end = 5;
      break;
    case "Overlook-Burned":
      start = 1;
      end = 5;
      break;
    case "Discarded-Why":
      start = 1;
      end = 5;
      break;
    case "Discarded-Know":
      start = 1;
      end = 5;
      break;
    case "Discarded-What":
      start = 1;
      end = 5;
      break;
    case "Archive":
      start = 1;
      end = 5;
      break;
    case "Discarded-Lying":
      start = 1;
      end = 5;
      break;
    case "Discarded-Why-Telling":
      start = 1;
      end = 5;
      break;
    case "Discarded-What-Suggest":
      start = 1;
      end = 5;
      break;
    case "Exit-Want":
      start = 1;
      end = 5;
      break;
    case "Exit-Following":
      start = 1;
      end = 5;
      break;
    case "Exit-Fin":
      start = 1;
      end = 5;
      break;
    case "Exit-Stopped":
      start = 1;
      end = 5;
      break;
    case "Exit-Yes":
      start = 1;
      end = 5;
      break;
    case "Exit-No":
      start = 1;
      end = 5;
      break;
    case "Pre-Control-Room":
      start = 1;
      end = 5;
      break;
    case "ponovi":
      start = 1;
      end = 5;
      break;
    default: // tisina
      start = 5;
      end = 5.9;
      setTimeout(function() {
        try {
          if (!isMobileBrowser()) window.recognition.start();
        } catch (e) {}
      }, 400);
      break;
  }

  END = end;

  // Twine connection
  window.parent.postMessage({
    action: "play_video_part",
    part: part,
    start: start,
    end: end
  }, "*");
}

function question(q) {
  window.recognition.stop();
  window.output.innerHTML = q + " ";
  window.ws.send(q);
}

function isMobileBrowser() {
  return /Mobi|Android|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
    navigator.userAgent,
  );
}
