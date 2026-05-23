var DONT = false;

var CURRENT_PASSAGE = "initial"; //Starting passage

// Defines from which passages which responses are valid
var PASSAGE_STATES = {
  "initial": ["Who", "What-Need", "Used-Me", "Biochip", "Body", "Organization", "Grieve", "Believe"],
  "CR Who Are You": ["What-Need", "Used-Me", "Biochip", "Body", "Organization", "Grieve", "Believe", "Continue"],
  "CR What Need": ["Who", "Used-Me", "Biochip", "Body", "Organization", "Grieve", "Believe", "Continue"],
  "CR Used Me": ["Who", "What-Need", "Biochip", "Body", "Organization", "Grieve", "Believe", "Continue"],
  "CR Body Question": ["Who", "What-Need", "Used-Me", "Biochip", "Body", "Grieve", "Believe", "Continue"],
  "CR Believe": ["Who", "What-Need", "Used-Me", "Biochip", "Body", "Organization", "Grieve", "Continue"],
  "CR Biochip Watch": ["Who", "What-Need", "Used-Me", "Body", "Organization", "Grieve", "Believe", "Intervene", "Heard", "Continue"],
  "CR Grieve": ["Who", "What-Need", "Used-Me", "Biochip", "Body", "Organization", "Believe", "Continue", "Think", "Not-Answer"],
  "CR Organization": ["Who", "What-Need", "Used-Me", "Biochip", "Body", "Grieve", "Believe", "Continue", "Now", "Tell-Me"],
  "CR Intervene": ["Who", "What-Need", "Used-Me", "Body", "Organization", "Grieve", "Believe", "Continue"],
  "CR Heard Everything": ["Who", "What-Need", "Used-Me", "Body", "Organization", "Grieve", "Believe", "Continue"],
  "CR Grieve Not Answer": ["Who", "What-Need", "Used-Me", "Biochip", "Body", "Organization", "Believe", "Continue"],
  "CR Grieve Think You Do": ["Who", "What-Need", "Used-Me", "Biochip", "Body", "Organization", "Believe", "Continue"],
  "CR Organization Now": ["Who", "What-Need", "Used-Me", "Biochip", "Body", "Grieve", "Believe", "Continue"],
  "CR Tell Me": ["Who", "What-Need", "Used-Me", "Biochip", "Body", "Grieve", "Believe", "Continue"]
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
      case "What-Need":
        tryAdvancePassage("CR What Need", response);
        break;

      case "Used-Me":
        tryAdvancePassage("CR Used Me", response);
        break;

      case "Biochip":
        tryAdvancePassage("CR Biochip Watch", response);
        break;

      case "Body":
        tryAdvancePassage("CR Body Question", response);
        break;

      case "Organization":
        tryAdvancePassage("CR Organization", response);
        break;

      case "Grieve":
        tryAdvancePassage("CR Grieve", response);
        break;

      case "Believe":
        tryAdvancePassage("CR Believe", response);
        break;

      case "Continue":
        tryAdvancePassage("CR Panel Speech", response);
        break;

      case "Who":
        tryAdvancePassage("CR Who Are You", response);
        break;

      case "Heard":
        tryAdvancePassage("", response);
        break;

      case "Intervene":
        tryAdvancePassage("CR Intervene", response);
        break;

      case "Heard":
        tryAdvancePassage("CR Heard Everything", response);
        break;

      case "Not-Answer":
        tryAdvancePassage("CR Grieve Not Answer", response);
        break;

      case "Think":
        tryAdvancePassage("CR Grieve Think You Do", response);
        break;

      case "Now":
        tryAdvancePassage("CR Organization Now", response);
        break;

      case "Tell-Me":
        tryAdvancePassage("CR Tell Me", response);
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
