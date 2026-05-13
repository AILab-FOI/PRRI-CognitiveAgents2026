var DONT = false;
var FIRST = true;
var STOP = false;

var CURRENT_PASSAGE = "initial";

// Defines from which passages which responses are valid
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
    // Only update if we know about this passage; ignore unknown ones.
    if (
      Object.prototype.hasOwnProperty.call(PASSAGE_STATES, event.data.passage)
    ) {
      CURRENT_PASSAGE = event.data.passage;
    }
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
        //setTimeout(function(){ recognition.start(); }, 400);
      };

      recognition.onerror = (event) => {
        window.recognition.stop();
        //setTimeout(function(){ recognition.start(); }, 400);
      };
    };
    init();

    button.onclick = () => {
      document.querySelector(".video-container").style.display = "block";
      if (!isMobileBrowser()) recognition.start();
      document.getElementById("startupute").style.display = "none";
      play_part("tisina");
      question("bok");
    };
  }

  record.onclick = () => {
    window.recognition.start();
  };

  $("#agent")[0].ontimeupdate = function () {
    var agent = $("#agent")[0];
    var the_time = agent.currentTime;
    if (the_time >= END) {
      agent.pause();
      play_part("tisina");
      if (!FIRST) DONT = true;
    } else {
      DONT = false;
    }
  };
  $("#agent")[0].loadedmetadata = function () {
    DONT = false;
    play_part("tisina");
  };
});

function connect() {
  ws = new WebSocket("ws://localhost:8012");
  window.ws = ws;
  ws.onopen = function () {
    ws.send("connect");
    DONT = false;
    play_part("tisina");
  };

  ws.onmessage = function (msg) {
    var response = msg.data.toString();
    console.log("[WS] Received:", response);

    //play_part(response);

    if (response === "ponovi") {
        play_part("ponovi"); // plays the "please repeat" audio, which ends → tisina → mic restarts
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
  var agent = $("#agent")[0];
  var end = 0;

  agent.play();

  DONT = part !== "tisina" ? true : false;
  if (part === "tisina") FIRST = !FIRST;

  recognition.stop();
  switch (part) {
    case "01":
      agent.currentTime = 0;
      end = 3.6;
      break;
    case "02":
      agent.currentTime = 3.6;
      end = 11.6;
      break;
    case "03":
      agent.currentTime = 11.6;
      end = 16.7;
      break;
    case "04":
      agent.currentTime = 16.7;
      end = 22.6;
      break;
    case "05":
      agent.currentTime = 22.6;
      end = 27.2;
      break;
    case "06":
      agent.currentTime = 27.2;
      end = 34.2;
      break;
    case "07":
      agent.currentTime = 34.2;
      end = 40.9;
      break;
    case "08":
      agent.currentTime = 40.9;
      end = 44.6;
      break;
    case "09":
      agent.currentTime = 44.6;
      end = 48.7;
      break;
    case "10":
      agent.currentTime = 48.7;
      end = 53;
      break;
    case "11":
      agent.currentTime = 53;
      end = 58.8;
      break;
    case "12":
      agent.currentTime = 58.8;
      end = 67.3;
      break;
    case "13":
      agent.currentTime = 67.3;
      end = 72;
      break;
    case "14":
      agent.currentTime = 72;
      end = 77.9;
      break;
    case "15":
      agent.currentTime = 77.9;
      end = 82.7;
      break;
    case "16":
      agent.currentTime = 82.7;
      end = 87.5;
      break;
    case "17":
      agent.currentTime = 87.5;
      end = 92.4;
      break;
    case "18":
      agent.currentTime = 92.4;
      end = 100.2;
      break;
    case "19":
      agent.currentTime = 100.2;
      end = 103.3;
      break;
    case "20":
      agent.currentTime = 103.3;
      end = 111.2;
      break;
    case "21":
      agent.currentTime = 111.2;
      end = 116;
      break;
    case "dobro":
      agent.currentTime = 116;
      end = 118.7;
      break;
    case "hvala":
      agent.currentTime = 118.7;
      end = 120.6;
      break;
    case "izvoli":
      agent.currentTime = 120.6;
      end = 122;
      break;
    case "lijepo":
      agent.currentTime = 122;
      end = 124.4;
      break;
    case "ponovi":
      agent.currentTime = 124.4;
      end = 129;
      break;
    case "predstavljanje-dugo":
      agent.currentTime = 129;
      end = 142.8;
      break;
    case "predstavljanje-kratko":
      agent.currentTime = 142.8;
      end = 145.2;
      break;
    default: // 'tisina'
      agent.currentTime = 145.2;
      end = 165;
      try {
        if (!isMobileBrowser()) window.recognition.start();
      } catch (e) {}
      break;
  }

  END = end;
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
