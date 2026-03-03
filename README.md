# PRRI-CognitiveAgents2026

A visual novel game based on the B.A.R.I.C.A. kognitive agents platform developed by students and the [Artificial Intelligence Laboratory](https://ai.foi.hr/) at the [University of Zagreb Faculty of Organization and Informatics](https://www.foi.unizg.hr/). The game is developed using the [Twine](https://twinery.org/) interactive fiction engine. More details available at [itch.io](https://ailab-foi.itch.io/prri-cognitiveagents2026). 

## Installation

In the `src` folder install `requirements.txt`:

```
pip3 install-r requirements.txt
```

## Instructions

Before first use you have to train the cognitive agent. To train the agent use:

```
python3 server.py --train
```

To start and test the game position your console to `src/` and start the server:

```
python3 server.py 
```

Then navigate in your browser to `http://localhost:5000`



To just test the current agent use:

```
python3 chat-test.py
```

To edit the game download [Twine](https://twinery.org/) and load the `The Deathworlders.twee` file. When happy with edits use `Publish to file` and publish it as `src/templates/index.html`.  

## Credits

A previous version of this game has been developed [here](https://github.com/AILab-FOI/PRRI-CognitiveAgents2025).

