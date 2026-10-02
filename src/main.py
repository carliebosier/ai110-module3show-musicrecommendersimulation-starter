"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""
from src.recommender import load_songs, recommend_songs


# Base profiles: realistic listeners with consistent tastes
BASE_PROFILES = {
    "High-Energy Pop": {
        "genre": "pop", "mood": "happy", "energy": 0.85, "valence": 0.8, "likes_acoustic": False,
    },
    "Chill Lofi": {
        "genre": "lofi", "mood": "chill", "energy": 0.40, "valence": 0.55, "likes_acoustic": True,
    },
    "Deep Intense Rock": {
        "genre": "rock", "mood": "intense", "energy": 0.92, "valence": 0.4, "likes_acoustic": False,
    },
}

# Adversarial profiles: edge cases meant to expose weaknesses in the scoring
ADVERSARIAL_PROFILES = {
    # Conflicting prefs + a mood missing from the catalog: mood can never match
    "Adversarial: Energetic but Sad": {
        "genre": "edm", "mood": "sad", "energy": 0.9, "valence": 0.1, "likes_acoustic": False,
    },
    # Exact string matching is case-sensitive, so "Pop" should earn no genre points
    "Adversarial: Case-Sensitive Genre": {
        "genre": "Pop", "mood": "Happy", "energy": 0.8, "valence": 0.8, "likes_acoustic": False,
    },
    # Acoustic lover who wants metal-level energy: tests whether the acoustic bonus
    # can pull results toward quiet songs (it can't; energy dominates)
    "Adversarial: Acoustic Headbanger": {
        "genre": "metal", "mood": "aggressive", "energy": 0.95, "valence": 0.2, "likes_acoustic": True,
    },
    # Out-of-range numbers are not validated, so energy points should be zero for every song
    "Adversarial: Out-of-Range Values": {
        "genre": "jazz", "mood": "relaxed", "energy": 1.5, "valence": -0.5, "likes_acoustic": False,
    },
}


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = {**BASE_PROFILES, **ADVERSARIAL_PROFILES}

    for name, user_prefs in profiles.items():
        print("\n" + "=" * 60)
        print(f"Profile: {name}")
        print(f"Prefs:   {user_prefs}")
        print("=" * 60)

        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\nTop recommendations:\n")
        for rec in recommendations:
            # Each item is (song, score, explanation)
            song, score, explanation = rec
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
