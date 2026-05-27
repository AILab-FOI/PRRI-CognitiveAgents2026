var DONT = false;

var CURRENT_PASSAGE = "initial"; //Starting passage

// Defines from which passages which responses are valid
var PASSAGE_STATES = {
  "initial": ["Hello", "Who", "What", "Rifle", "Camera"],
  "Eng A Hello": ["Who", "What", "C"],
  "Eng A Who": ["Research-Intro", "No"],
  "Eng A What": ["Research-Intro", "No"],
  "Eng Research Intro": ["Rifle", "Camera"],
  "Eng Rifle": ["Rifle-Force", "Rifle-Power", "Rifle-War"],
  "Eng Rifle Force": ["Camera", "Leave"],
  "Eng Rifle Power": ["Camera", "Leave"],
  "Eng Rifle War": ["Camera", "Leave"],
  "Eng Camera": ["Camera-Memory", "Camera-Share", "Camera-Obsession"],
  "Eng Camera Memory": ["Camera-Imprecision", "Camera-Accuracy"],
  "Eng Camera Imprecision": ["Leave"],
  "Eng Camera Accuracy": ["Camera-Alone", "Camera-Residue", "Camera-Obsession"],
  "Eng Camera Share": ["Camera-Alone", "Camera-Residue"],
  "Eng Camera Alone": ["Leave"],
  "Eng Camera Residue": ["Leave"],
  "Eng Camera Obsession": ["Camera-Point", "Camera-Problem"],
  "Eng Camera Obsession Point": ["Leave"],
  "Eng Camera Obsession Problem": ["Leave"],
  "Eng A No": ["Who", "What", "C", "Leave"]
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
    ws = new WebSocket("ws://localhost:8009");
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
      	case "Hello":
        	tryAdvancePassage("Eng A Hello", response);
        	break;

		case "Who":
        	tryAdvancePassage("Eng A Who", response);
        	break;

		case "What":
        	tryAdvancePassage("Eng A What", response);
        	break;

		case "C":
        	tryAdvancePassage("Eng Route C", response);
        	break;

		case "Research-Intro":
        	tryAdvancePassage("Eng Research Intro", response);
        	break;

		case "No":
        	tryAdvancePassage("Eng A No", response);
        	break;

		case "Rifle":
        	tryAdvancePassage("Eng Rifle", response);
        	break;

		case "Camera":
        	tryAdvancePassage("Eng Camera", response);
        	break;

		case "Rifle-Force":
        	tryAdvancePassage("Eng Rifle Force", response);
        	break;

		case "Rifle-Power":
        	tryAdvancePassage("Eng Rifle Power", response);
        	break;

		case "Rifle-War":
        	tryAdvancePassage("Eng Rifle War", response);
        	break;

		case "Leave":
        	tryAdvancePassage("Eng Bay Closing", response);
        	break;

		case "Camera-Memory":
        	tryAdvancePassage("Eng Camera Memory", response);
        	break;

		case "Camera-Share":
        	tryAdvancePassage("Eng Camera Share", response);
        	break;

		case "Camera-Obsession":
        	tryAdvancePassage("Eng Camera Obsession", response);
        	break;

		case "Camera-Imprecision":
        	tryAdvancePassage("Eng Camera Imprecision", response);
        	break;

		case "Camera-Accuracy":
        	tryAdvancePassage("Eng Camera Accuracy", response);
        	break;

		case "Camera-Alone":
        	tryAdvancePassage("Eng Camera Alone", response);
        	break;

		case "Camera-Residue":
        	tryAdvancePassage("Eng Camera Residue", response);
        	break;

		case "Camera-Point":
        	tryAdvancePassage("Eng Camera Obsession Point", response);
        	break;

		case "Camera-Problem":
        	tryAdvancePassage("Eng Camera Obsession Problem", response);
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
