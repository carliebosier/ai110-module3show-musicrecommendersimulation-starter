# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeMatch 1.0**

---

## 2. Intended Use  

**Goal:** Suggest 5 songs from a small catalog that match one listener's stated taste.

**Input:** A profile with a favorite genre, a favorite mood, a target energy, a target happiness (valence), and whether the listener likes acoustic music.

**Output:** A ranked top 5. Each song has a score and a short reason.

**Assumptions:** The listener can describe their taste with a few labels and numbers. Their taste stays the same during a session. The system does not use listening history.

**Intended use:** Classroom practice. It shows how a scoring-based recommender works.

**Not intended for:** Real music apps or real users. Judging anyone's taste. Deciding which real artists get heard. Any catalog much bigger or more varied than these 18 songs.


---

## 3. How the Model Works  

Each song gets points for how well it fits the listener. Then the songs are sorted from highest to lowest.

- A genre match is worth 1.5 points.
- A mood match is worth 1.0 point.
- Energy is worth up to 2.0 points. The closer the song's energy is to the listener's target, the more points it gets. A song far from the target gets zero.
- Happiness (valence) works the same way and is worth up to 0.5 points.
- Acoustic songs get up to 0.5 bonus points if the listener likes acoustic music.

The top score is 5.5. If two songs tie, the one closer in energy wins. Each result shows the points it earned.

**Changes from the starter:** The starter had no scoring. I added the point rules above, made the closeness rule steeper so far-off songs get zero, and added a happiness preference.


---

## 4. Data  

The catalog has 18 songs. I started with 10 and added 8 made-up songs using an AI assistant, to cover more genres.

There are 15 genres and 14 moods. Lofi has 3 songs and pop has 2. The other 13 genres have one song each. 11 of the 14 moods appear only once.

Each song has genre, mood, energy, valence, acousticness, tempo, danceability, title and artist. Only genre, mood, energy, valence and acousticness are scored. Tempo and danceability are stored but not used.

**Missing:** lyrics, language, popularity, listening history, and any real user data. The songs are fictional. The catalog has no really sad quiet songs, and no loud acoustic ones.

---

## 5. Strengths  

The system works well when a listener's genre, mood and energy agree.

- The Chill Lofi listener gets Midnight Coding, Library Rain and Focus Flow on top. That matches what I would expect.
- The Pop listener gets Sunrise City first, and the Rock listener gets Storm Runner first.
- Scoring energy by closeness means a calm listener is never handed the loudest song.
- Every result explains its score, so it is easy to see why a song ranked where it did.


---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

The system lets a song's energy override the genre a listener says they like. A close energy match can earn up to 2.0 points, while a genre match earns only 1.5, and songs far from the target energy earn nothing for energy. When I tried a pop/happy listener who wanted mellow music (energy 0.4), only Sunrise City made the top five, and only because it matched both genre and mood. Gym Hero, the other pop song, dropped out because its energy was too far from the target. The other four were calm lofi and jazz songs. Across 2,016 test profiles (from a one-off script my AI assistant ran, it isn't saved in the repo), the four calmest songs showed up in the top five for 35 to 47 percent of them, while the four loudest showed up for only 17 to 22 percent. As a result, the system quietly favors calm, acoustic music and can ignore a listener's stated genre.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

**Profiles tested.** I ran seven profiles. Three were realistic: High-Energy Pop, Chill Lofi and Deep Intense Rock. Four were edge cases: Energetic but Sad (a mood that isn't in the catalog), Case-Sensitive Genre ("Pop" and "Happy" capitalized), Acoustic Headbanger (loves acoustic music but wants metal-level energy), and Out-of-Range Values (energy 1.5, valence -0.5). I checked whether each top five matched what that listener would expect.

**Why Gym Hero keeps showing up for Happy Pop listeners.** The catalog has only two pop songs, so a pop fan who wants loud music always gets Gym Hero. It is also loud and upbeat. Its mood is "intense", not "happy", so it loses one point, but it still beats every non-pop song. It appeared in five of the seven lists.

**What surprised me.**
- A rock listener got Gym Hero, a pop song, in second place. Its mood label ("intense") matched and its energy was almost exact. Iron Furnace, a metal song that sounds closer to rock, came fourth. Its label is "aggressive", and it was slightly farther from the targets than Neon Tears.
- The "likes acoustic" setting barely mattered for the Acoustic Headbanger. The bonus added at most 0.1 points.
- The Out-of-Range profile still returned five songs. Four of them scored 0.00.

**Comparing profiles.**
- **Pop vs. Chill Lofi:** no songs are shared. Pop gets loud, bright songs. Lofi gets calm, acoustic ones. That fits their energy targets of 0.85 and 0.40.
- **Pop vs. Deep Intense Rock:** both want loud music, so they share Gym Hero and Storm Runner. Pop puts Sunrise City first and Rock puts Storm Runner first, which fits their genre and mood.
- **Chill Lofi vs. Deep Intense Rock:** no overlap, as expected for opposite ends of the energy range.
- **Deep Intense Rock vs. Energetic but Sad:** four of five songs match, since both want very loud music. Neon Tears is first for the Sad listener only because it is the one EDM song.
- **High-Energy Pop vs. Case-Sensitive Genre:** capitalizing "Pop" and "Happy" drops Sunrise City from 4.84 to 2.38. Gym Hero disappears, because its place depended on the genre match.
- **Deep Intense Rock vs. Acoustic Headbanger:** four of five songs match, since both want very loud music. The acoustic bonus was too small to pull in quiet songs. Energy won.
- **Chill Lofi vs. Out-of-Range Values:** Coffee Shop Stories is fifth for Lofi but first for the jazz listener with impossible numbers. Only genre and mood scored. The system does not check whether inputs make sense.

**Experiment: turning off the mood check.** For Deep Intense Rock, Gym Hero fell from second to fourth, which looks more accurate. For Chill Lofi, the order just changed, because the system could no longer tell "chill" from "focused". The Sad and Case-Sensitive profiles did not change, since mood never matched there. I restored the mood check afterward.

---

## 8. Future Work  

1. **Give partial credit for similar labels.** "Pop" and "indie pop" would count as close, and so would "intense" and "aggressive". This would fix cases like Gym Hero outranking Iron Furnace for a rock listener.
2. **Add more songs.** Each genre needs several songs, plus more dark and quiet songs and more loud acoustic ones.
3. **Fix input and acoustic rules.** Reject values outside 0 to 1. Let a listener who dislikes acoustic music lose points for acoustic songs. Limit the top 5 to one song per artist.

---

## 9. Personal Reflection  

I learned that a recommender turns data into suggestions using a few chosen rules and weights. Deciding which features mattered most helped me see what my recommender should focus on. The biggest surprise was Gym Hero showing up for a rock listener. A pop song ranked second because its mood label matched, which showed me how much one label can change the results. If I kept building, I would add songs that sound alike but have different labels, like "pop" and "indie pop", to test for wrong or missed matches. This also changed how I think about apps like Spotify. My version only uses what a listener says they like. Real apps also learn from what people play, skip and save, and they still have to turn all of that into rules and weights.