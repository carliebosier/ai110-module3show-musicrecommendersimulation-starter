# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

The system lets a song's energy override the genre a listener says they like. A close energy match can earn up to 2.0 points, while a genre match earns only 1.5, and songs far from the target energy earn nothing for energy. When I tried a pop/happy listener who wanted mellow music (energy 0.4), only Sunrise City made the top five, and only because its mood matched; the other four were calm lofi and jazz songs. Across 2,016 test profiles, the four calmest songs showed up in the top five for 35 to 47 percent of them, while the four loudest showed up for only 17 to 22 percent. As a result, the system quietly favors calm, acoustic music and can ignore a listener's stated genre.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

**Profiles tested.** I ran seven profiles. Three were realistic listeners: High-Energy Pop, Chill Lofi and Deep Intense Rock. Four were tricky edge cases meant to confuse the system: Energetic but Sad (asks for a mood that doesn't exist in the catalog), Case-Sensitive Genre (types "Pop" instead of "pop"), Acoustic Headbanger (wants metal-level energy but loves acoustic music), and Out-of-Range Values (energy 1.5 and valence -0.5). For each one I looked at whether the top five matched what that listener would expect.

**Why Gym Hero keeps showing up for Happy Pop listeners.** The catalog has only two pop songs, so a pop fan automatically gets the other one, Gym Hero, in the second slot. Gym Hero is also loud and upbeat, which is exactly what a High-Energy Pop listener asks for. Its mood is "intense" instead of "happy", so it loses one point, but it still beats every non-pop song. It appeared in five of the seven lists.

**What surprised me.**
- A rock listener got Gym Hero, a pop song, in second place. It earned no genre points, but its mood label ("intense") matched and its energy was almost exact. Iron Furnace, a metal song that sounds closer to rock, came fourth because its label is "aggressive".
- The "likes acoustic" setting barely mattered for the Acoustic Headbanger. The loudest songs in the catalog are almost never acoustic, so the bonus added at most 0.1 points.
- The Out-of-Range profile still returned five songs, but four of them scored 0.00 and were just the loudest songs in the catalog.

**Comparing profiles.**
- **Pop vs. Chill Lofi:** no songs overlap. Pop gets loud, bright songs like Sunrise City, while Lofi gets calm, acoustic ones like Midnight Coding. That makes sense because the energy targets are 0.85 and 0.40.
- **Pop vs. Deep Intense Rock:** both want loud music, so they share Gym Hero and Storm Runner. Pop puts Sunrise City first, and Rock puts Storm Runner first, which fits their genre and mood choices.
- **Chill Lofi vs. Deep Intense Rock:** completely different lists, as expected for opposite ends of the energy range.
- **Deep Intense Rock vs. Energetic but Sad:** four of five songs are the same. The word "sad" matches nothing, but the low valence target still pulls up the darkest loud songs, Neon Tears and Iron Furnace, into the top two.
- **High-Energy Pop vs. Case-Sensitive Genre:** capitalizing "Pop" drops Sunrise City from 4.84 to 2.38, and Gym Hero vanishes from the list entirely. Gym Hero's place depended on the genre match, so without it a pop fan sees songs from other genres.
- **Deep Intense Rock vs. Acoustic Headbanger:** four of five songs are the same. Adding "likes acoustic" changed almost nothing, so energy won the conflict.
- **Chill Lofi vs. Out-of-Range Values:** Coffee Shop Stories ranks fifth for Lofi but first for the jazz listener with impossible numbers. That's because the genre and mood match are all that scored, and the rest of the list has no meaning. The system doesn't check whether inputs make sense.

**Experiment: turning off the mood check.** For Deep Intense Rock, Gym Hero fell from second to fourth and Neon Tears and Iron Furnace moved up, which looks more accurate. For Chill Lofi, the order just changed, with Focus Flow taking first place, because the system could no longer tell "chill" from "focused". The Sad and Case-Sensitive profiles didn't change at all, since mood never matched in those lists. I restored the mood check afterward.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
