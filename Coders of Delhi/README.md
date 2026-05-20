# 🔗 Social Network Recommendation System

A Python-based mini social network engine that simulates Facebook-style recommendations — **"People You May Know"** and **"Pages You Might Like"** — using graph traversal and collaborative filtering logic on custom JSON datasets.

---

## 📁 Project Structure

```
📦 social-network-recommendation/
├── 📓 main.ipynb                  # Data loader & network explorer
├── 📓 DataCleaning.ipynb          # Data preprocessing pipeline
├── 📓 PeopleYouMayknow.ipynb      # Friend recommendation algorithm
├── 📓 Pages_YouMight_LIke.ipynb   # Page recommendation algorithm
├── 🗂️ data.json                   # Small dataset (5 users, 4 pages)
├── 🗂️ codebook_data.json          # Raw/dirty dataset (with duplicates & nulls)
├── 🗂️ cleaned_codebook_data.json  # Cleaned output of DataCleaning.ipynb
├── 🗂️ MassiveData.json            # Full dataset (30 users, 27 pages)
└── 🗂️ massive_data.json           # Duplicate of MassiveData.json (lowercase)
```

---

## 🧠 How It Works

### 1. `main.ipynb` — Network Explorer
Loads `data.json` and prints a human-readable summary of all users, their friend connections, and liked pages. Entry point to understand the data structure.

### 2. `DataCleaning.ipynb` — Data Preprocessing
Reads `codebook_data.json` (intentionally dirty data) and applies the following cleaning steps:

| Step | Action |
|------|--------|
| ✅ Remove blank names | Users with empty `name` fields are dropped |
| ✅ Deduplicate friends | Duplicate friend IDs in lists are removed using `set()` |
| ✅ Remove inactive users | Users with no friends AND no liked pages are filtered out |
| ✅ Deduplicate pages | Pages with the same `id` are collapsed to one entry |

**Input:** `codebook_data.json` → **Output:** `cleaned_codebook_data.json`

---

### 3. `PeopleYouMayknow.ipynb` — Friend Recommendations
Implements a **mutual friends algorithm** to suggest new connections.

**Logic:**
- For a given user, traverse all their direct friends
- Collect friends-of-friends who are not already connected
- Rank suggestions by the number of mutual friends (higher = more relevant)

```
User 1 (Amit) → Friends: [2, 3, 4, 5, 6]
Suggested: [7, 8, 9, 10, 11, 12]  ← ranked by mutual friend count
```

**Time Complexity:** O(U × F²) where U = users, F = avg friends per user

---

### 4. `Pages_YouMight_LIke.ipynb` — Page Recommendations
Implements a **collaborative filtering algorithm** to suggest pages.

**Logic:**
- Find pages already liked by the target user
- For every other user, compute the overlap (shared liked pages)
- Score un-liked pages based on how many users with shared tastes also liked them
- Return pages sorted by relevance score

```
User 1 (Amit) → Liked: [101, 102]
Suggested: [103, 105, 107, 104, 106, ...]  ← ranked by shared interest score
```

---

## 🗂️ Dataset Overview

### `data.json` — Small Dataset
A minimal 5-user network used for initial development and testing.

### `codebook_data.json` — Raw / Dirty Data
Intentionally contains data quality issues: empty names, duplicate friend entries, duplicate page IDs, and inactive users — used as input for the cleaning pipeline.

### `cleaned_codebook_data.json` — Cleaned Data
The sanitized output produced by `DataCleaning.ipynb`. Contains only valid, deduplicated users and pages.

### `MassiveData.json` / `massive_data.json` — Full Dataset
A 30-user, 27-page network with rich connections and diverse tech-themed pages (e.g., *Cybersecurity Experts*, *AI & ML Community*, *Full-Stack Developers*). Used for testing recommendations at scale.

---

## ▶️ Getting Started

### Prerequisites
- Python 3.x
- Jupyter Notebook or JupyterLab

### Installation

```bash
git clone https://github.com/alhajgaming/epic-dataScience.git
cd epic-dataScience
pip install notebook
jupyter notebook
```

### Run Order

```
1. main.ipynb               → Explore the raw data
2. DataCleaning.ipynb       → Clean codebook_data.json
3. PeopleYouMayknow.ipynb   → Generate friend suggestions
4. Pages_YouMight_LIke.ipynb → Generate page suggestions
```

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![JSON](https://img.shields.io/badge/Data-JSON-lightgrey?logo=json)

| Tool | Purpose |
|------|---------|
| Python | Core logic & data processing |
| Jupyter Notebook | Interactive development & visualization |
| JSON | Lightweight data storage format |
| `json` module | Built-in JSON parsing |

---

## 💡 Key Concepts Demonstrated

- **Graph traversal** — BFS-style mutual friend discovery
- **Collaborative filtering** — Interest-based page scoring
- **Data cleaning pipeline** — Handling nulls, duplicates, and inactive records
- **Dictionary-based scoring** — Efficient ranking without external ML libraries

---

## 🚀 Possible Extensions

- [ ] Add weighted scoring using friendship strength or recency
- [ ] Integrate a graph visualization library (e.g., NetworkX + Matplotlib)
- [ ] Expose recommendations via a REST API (Flask/FastAPI)
- [ ] Scale to larger datasets using Pandas or graph databases (Neo4j)
- [ ] Add a simple frontend dashboard for interactive exploration

---

## 👤 Author

**Alhaj** — BCA Final Year | Data Analytics & Cybersecurity  
[GitHub](https://github.com/alhajgaming) • [LinkedIn](https://www.linkedin.com/in/alhaj-khan-611211292/)

---

> *Built as part of a Data Structures & Algorithms project exploring real-world applications of graph theory in social networks.*
> codeWithHarry codersOfDelhiProject
