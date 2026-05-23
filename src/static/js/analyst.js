var DONT = false;

var CURRENT_PASSAGE = "initial"; //Starting passage

// Defines from which passages which responses are valid
var PASSAGE_STATES = {
  "initial": ["Brain", "Place", "Alive", "Studying", "Wrong"],
  "Analyst Brain": ["Memory", "Who-I", "Build"],
  "Analyst No Memory": ["Place", "Studying", "Puzzle-Intro"],
  "Analyst Who I Am": ["Place", "Studying", "Puzzle-Intro"],
  "Analyst Why Build": ["Worse", "Puzzle-Intro", "Recording"],
  "Analyst Worse": ["Puzzle-Intro"],
  "Analyst Recording": ["Puzzle-Intro"],
  "Analyst What Place": ["Compare", "Sample", "Puzzle-Intro"],
  "Analyst Compare": ["Puzzle-Intro"],
  "Analyst Sample": ["Puzzle-Intro"],
  "Analyst Alive": ["Moving", "Feel-Alive", "Blurry"],
  "Analyst Moving": ["Puzzle-Intro"],
  "Analyst Feel Alive": ["Puzzle-Intro"],
  "Analyst Not Blurry": ["Puzzle-Intro"],
  "Analyst Wrong": ["Consent", "Objects", "Understand"],
  "Analyst No Consent": ["Puzzle-Intro"],
  "Analyst Objects": ["Puzzle-Intro"],
  "Analyst Dont Understand": ["Puzzle-Intro"],
  "Analyst Studying": ["Course", "Why-Doing", "Learned"],
  "Analyst Of Course": ["Puzzle-Intro"],
  "Analyst Why Doing": ["Puzzle-Intro"],
  "Analyst Learned": ["Puzzle-Intro"],
  "Analyst Puzzle Intro": ["Left", "Right", "Probability"],
  "Analyst Left": ["No-Signal", "Greater-Design"],
  "Analyst Greater Design": ["Carry-Yes", "Carry-Know", "Carry-Used", "Carry-No"],
  "Analyst Carry Yes": ["Exit"],
  "Analyst Carry Know": ["Exit"],
  "Analyst Carry Used Zo": ["Exit"],
  "Analyst Carry No": ["Exit"]
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
      case "Brain":
        tryAdvancePassage("Analyst Brain", response);
        break;

      case "Place":
        tryAdvancePassage("Analyst What Place", response);
        break;

      case "Alive":
        tryAdvancePassage("Analyst Alive", response);
        break;

      case "Wrong":
        tryAdvancePassage("Analyst Wrong", response);
        break;

      case "Memory":
        tryAdvancePassage("Analyst No Memory", response);
        break;

      case "Who-I":
        tryAdvancePassage("Analyst Who I Am", response);
        break;

      case "Build":
        tryAdvancePassage("Analyst Why Build", response);
        break;

      case "Puzzle-Intro":
        tryAdvancePassage("Analyst Puzzle Intro", response);
        break;

      case "Worse":
        tryAdvancePassage("Analyst Worse", response);
        break;

      case "Recording":
        tryAdvancePassage("Analyst Recording", response);
        break;

      case "Compare":
        tryAdvancePassage("Analyst Compare", response);
        break;

      case "Sample":
        tryAdvancePassage("Analyst Sample", response);
        break;

      case "Moving":
        tryAdvancePassage("Analyst Movign", response);
        break;

      case "Feel-Alive":
        tryAdvancePassage("Analyst Feel Alive", response);
        break;

      case "Blurry":
        tryAdvancePassage("Analyst Not Blurry", response);
        break;

      case "Consent":
        tryAdvancePassage("Analyst No Consent", response);
        break;

      case "Objects":
        tryAdvancePassage("Analyst Objects", response);
        break;

      case "Understand":
        tryAdvancePassage("Analyst Dont Understand", response);
        break;

      case "Course":
        tryAdvancePassage("Analyst Of Course", response);
        break;

      case "Why-Doing":
        tryAdvancePassage("Analyst Why Doing", response);
        break;

      case "Learned":
        tryAdvancePassage("Analyst Learned", response);
        break;

      case "Left":
        tryAdvancePassage("Analyst Left", response);
        break;

      case "Right":
        tryAdvancePassage("Analyst Right", response);
        break;

      case "Probability":
        tryAdvancePassage("Analyst Probability", response);
        break;

      case "No-Signal":
        tryAdvancePassage("Analyst No Signal", response);
        break;

      case "Greater-Design":
        tryAdvancePassage("Analyst Greater Design", response);
        break;

      case "Carry-Yes":
        tryAdvancePassage("Analyst Carry Yes", response);
        break;

      case "Carry-Know":
        tryAdvancePassage("Analyst Carry Know", response);
        break;

      case "Carry-Used":
        tryAdvancePassage("Analyst Carry Used To", response);
        break;

      case "Carry-No":
        tryAdvancePassage("Analyst Carry No", response);
        break;

      case "Exit":
        tryAdvancePassage("Specimen Bay Exit", response);
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

function isMobileBrowser() {
  return /Mobi|Android|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
    navigator.userAgent,
  );
}
