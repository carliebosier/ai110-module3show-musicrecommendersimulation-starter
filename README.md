# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Real-world platforms like Spotify and YouTube combine two approaches. Collaborative filtering uses the behavior of millions of users (likes, skips, replays) to recommend what similar people enjoyed. Content-based filtering compares the qualities of songs to what a user says they like. My version is a simple content-based recommender. It matches a user's taste profile against each song's qualities. Genre matters most. After that, songs score higher when their energy and mood are *close* to what the user wants, not just higher or lower.

**What each song has:** genre, mood, energy level, how acoustic it sounds, how happy or sad it feels, tempo, and artist.

**What the user profile has:** favorite genre, favorite mood, preferred energy level, preferred happiness level (set to the middle if the user doesn't give one), and whether they like acoustic music.

**How songs are scored:**
- Matching the favorite genre is worth the most points (2).
- Energy is worth up to 1 point. The closer a song is to the user's preferred energy, the more points it gets.
- Happiness works the same way and is also worth up to 1 point.
- Acoustic songs get a small bonus (half a point) if the user likes acoustic music.

Mood, tempo, and artist are stored but don't count toward the score. Energy and happiness already capture most of what mood and tempo describe, and artist could become a bonus later.

**How songs are chosen:** The recommender scores every song, ranks them from best to worst, and shows the top 5, each with a short reason like "matches your genre; energy close to what you wanted."


---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



