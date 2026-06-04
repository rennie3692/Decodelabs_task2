# Simple Python Chatbot and Content Recommender

This repository contains a beginner-friendly rule-based chatbot and a simple movie recommendation system.

## Files

- `chatbot.py` - A simple command-line chatbot that runs in a loop and responds to user input.
- `chatbot_gui.py` - A Tkinter-based GUI version of the chatbot with a chat history window.
- `My first chatbot.py` - A separate chatbot file created during development.
- `content_recommender.py` - A command-line movie recommender using tag matching.
- `content_recommender_gui.py` - A Tkinter GUI for the movie recommender.

## Features

- Normalizes user input by converting to lowercase and trimming whitespace.
- Responds to greetings like `hello`, `hi`, and `hey`.
- Handles `how are you`, `help`, and `what's your name` queries.
- Supports exit commands: `quit`, `exit`, and `bye`.
- Provides a fallback response for unrecognized input.
- Matches user interests to movies with tag intersection scoring.
- Displays the top 3-5 matched movie recommendations.

## Run

From the `python` folder, use:

```powershell
py chatbot.py
```

or for the GUI chatbot version:

```powershell
py chatbot_gui.py
```

For the recommender:

```powershell
py content_recommender.py
```

and for the recommender GUI:

```powershell
py content_recommender_gui.py
```
