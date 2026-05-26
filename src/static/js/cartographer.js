var DONT = false;

var CURRENT_PASSAGE = "initial"; //Starting passage

// Defines from which passages which responses are valid
var PASSAGE_STATES = {
  "initial": ["Threatening", "Effort", "Deathworld", "Join"],
  "Cart Threatening": ["Effort", "Deathworld", "Join"],
  "Cart Effort": ["Join", "Deathworld"],
  "Cart Deathworld": ["Rage", "Skeptic", "Accept"],
  "Cart Brain Rage": ["Accept", "Permanent", "Threat", "Join"],
  "Cart Brain Skeptic": ["Accept", "Permanent", "Join"],
  "Cart Brain Accept": ["Join"],
  "Cart Brain Permanent": ["Join"],
  "Cart Hit Threat": ["Join"], //Hit??
  "Cart Punch": ["Join"],
  "Cart Join Research": ["Puzzle-War", "Puzzle-Sacrifice", "Puzzle-Science"],
  "Cart Puzzle War": ["War-No", "War-Lifeform", "War-Normal", "War-Parallels"],
  "War No Conflict": ["War-Lifeform", "War-Parallels", "War-Normal", "Signal"],
  "War Between Lifeforms": ["War-Difference", "War-Parallels", "Signal"],
  "War Normal": ["War-Shame", "Signal"],
  "War Parallels": ["Signal"],
  "War No Difference": ["Signal"],
  "War Shame": ["Signal"],
  "Cart Puzzle Science": ["Science-Weapons", "Science-Kind"],
  "Science Weapons": ["Signal"],
  "Science Your Kind": ["Signal"],
  "Cart Puzzle Sacrifice": ["Sacrifice-Death", "Sacrifice-Design", "Sacrifice-Divine", "Sacrifice-Consciousness"],
  "Sacrifice Consciousness": ["Signal"],
  "Sacrifice Divine": ["Signal"],
  "Sacrifice Death": ["Signal", "Sacrifice-Design", "Sacrifice-Divine", "Sacrifice-Consciousness"],
  "Sacrifice No Design": ["Signal"]
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
    const buttonYes = document.getElementById("btn-yes");
    const buttonNo = document.getElementById("btn-no");
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

    buttonYes.onclick = () => {
      window.parent.postMessage({ action: 'hide_iframe' }, '*');
      play_part("tisina");
    };

    buttonNo.onclick = () => {
      window.parent.postMessage({ action: 'hide_iframe' }, '*');

      window.parent.postMessage({ 
        action: 'play_video_part', 
        part: 'tisina', 
        start: 5, 
        end: 5.9 
    }, '*');
    };
  }

  record.onclick = () => {
    window.recognition.start();
  };
});

function connect() {
  ws = new WebSocket("ws://localhost:8011");
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
      case "Threatening":
        tryAdvancePassage("Cart Threatening", response);
        break;

      case "Effort":
        tryAdvancePassage("Cart Effort", response);
        break;

      case "Deathworld":
        tryAdvancePassage("Cart Deathworld", response);
        break;

      case "Join":
        tryAdvancePassage("Cart Join Research", response);
        break;

      case "Rage":
        tryAdvancePassage("Cart Brain Rage", response);
        break;

      case "Skeptic":
        tryAdvancePassage("Cart Brain Skeptic", response);
        break;

      case "Accept":
        tryAdvancePassage("Cart Brain Accept", response);
        break;

      case "Permanent":
        tryAdvancePassage("Cart Brain Permanent", response);
        break;

      case "Threat":
        tryAdvancePassage("Cart Hit Threat", response);
        break;

      case "Puzzle-War":
        tryAdvancePassage("Cart Puzzle War", response);
        break;

      case "Puzzle-Sacrifice":
        tryAdvancePassage("Cart Puzzle Sacrifice", response);
        break;

      case "Puzzle-Science":
        tryAdvancePassage("Cart Puzzle Science", response);
        break;

      case "War-No":
        tryAdvancePassage("War No Conflict", response);
        break;
      
      case "War-Lifeform":
        tryAdvancePassage("War Between Lifeforms", response);
        break;

      case "War-Parallels":
        tryAdvancePassage("War Parallels", response);
        break;

      case "War-Normal":
        tryAdvancePassage("War Normal", response);
        break;

      case "Signal":
        tryAdvancePassage("Cart Signal Check", response);
        break;

      case "War-Difference":
        tryAdvancePassage("War No Difference", response);
        break;

      case "War-Shame":
        tryAdvancePassage("War Shame", response);
        break;

      case "Science-Weapons":
        tryAdvancePassage("Science Weapons", response);
        break;

      case "Science-Kind":
        tryAdvancePassage("Science Your Kind", response);
        break;

      case "Sacrifice-Death":
        tryAdvancePassage("Sacrifice Death", response);
        break;

      case "Sacrifice-Design":
        tryAdvancePassage("Sacrifice No Design", response);
        break;

      case "Sacrifice-Divine":
        tryAdvancePassage("Sacrifice Divine", response);
        break;

      case "Sacrifice-Consciousness":
        tryAdvancePassage("Sacrifice Consciousness", response);
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
    case "ponovi":
      start = 6;
      end = 12;
      break;
    default: // tisina
      start = 0;
      end = 6;
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

function isMobileBrowser() {
  return /Mobi|Android|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
    navigator.userAgent,
  );
}
