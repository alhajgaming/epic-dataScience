# 📸 Coders of Bangalore — Instagram Data Parser

> A Python project inspired by **[Code with Harry](https://www.youtube.com/@CodeWithHarry)** that scrapes, parses, and analyzes Instagram profile data from Bangalore's tech & startup community.

---

## 📌 What is this project?

This project takes raw Instagram profile data (copy-pasted from Instagram) of Bangalore-based tech creators, developers, and startup communities, and parses it into clean, structured JSON — ready for analysis.

It answers questions like:
- Who has the **most posts**?
- Who has the **most followers**?
- Who follows the **most people**?
- How many **unique page categories** exist in the dataset?

---

## 📁 Project Structure

```
📦 coders-of-bangalore/
├── 📓 DataParsing.ipynb       # Main notebook — parsing + analysis
├── 📄 initialdata.txt         # Raw data — 13 Instagram profiles (starter dataset)
├── 📄 finaldata.txt           # Raw data — 100+ Bangalore tech profiles (full dataset)
└── 🗂️ parsed_data.json        # Structured JSON output from parsing
```

---

## 🧠 How It Works

### Raw Input Format (`initialdata.txt` / `finaldata.txt`)

Each Instagram profile is stored as a plain-text block separated by a blank line:

```
username
X posts
Y followers
Z following
Display Name
Category/Type
Bio line 1
Bio line 2
profile_link
```

### Parsing Pipeline (`DataParsing.ipynb`)

| Step | Description |
|------|-------------|
| **1. Read** | Load the `.txt` file |
| **2. Split** | Split into individual profile chunks on `\n\n` |
| **3. Filter** | Remove empty/junk chunks (`len > 3`) |
| **4. Parse** | Extract structured fields from each chunk |
| **5. Convert** | Normalize follower/following counts (`K` → ×1000, `M` → ×1,000,000) |
| **6. Export** | Dump all profiles to `parsed_data.json` |

### Output Format (`parsed_data.json`)

```json
{
    "username": "bangalore_tech_bro",
    "no_of_posts": 402,
    "no_of_followers": 12500,
    "no_of_following": 890,
    "name": "Rahul | HSR Hustler",
    "type_of_page": "Entrepreneur",
    "bio": "🚀 Building the next Unicorn in Fintech\n☕ 3rd Wave Coffee addict\n💻 Python | React | AI"
}
```

---

## 📊 Analysis Results (from `finaldata.txt`)

| Question | Answer |
|----------|--------|
| 🏆 Most Posts | `startuphub_blr` — 2,300 posts |
| 👥 Most Followers | `_anujsinghal` — 681,000 followers |
| 📲 Most Following | `bangalore_tech_bro` — 890 following |
| 🗂️ Unique Categories | 34 categories |

---

## 🗂️ Dataset Snapshot

The `finaldata.txt` contains **100+ real Bangalore tech Instagram profiles** including:

- Software engineers & full-stack developers
- AI/ML researchers and data scientists
- Startup founders & angel investors
- Tech communities & developer meetup pages
- Food & lifestyle bloggers from the tech belt

Covers Bangalore neighborhoods like Koramangala, HSR Layout, Indiranagar, Whitefield, Sarjapur, BTM Layout, and Electronic City.

---

## ▶️ Getting Started

### Prerequisites
- Python 3.x
- Jupyter Notebook

### Installation

```bash
git clone https://github.com/alhajgaming/epic-dataScience.git
cd epic-dataScience
pip install notebook
jupyter notebook
```

### Run

Open `DataParsing.ipynb` and run all cells top to bottom. Make sure `finaldata.txt` is in the same directory.

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![JSON](https://img.shields.io/badge/Output-JSON-lightgrey)

| Tool | Purpose |
|------|---------|
| Python | Core parsing logic |
| Jupyter Notebook | Interactive development |
| `json` module | Serializing output |
| String methods | `.split()`, `.strip()`, `.replace()` for parsing |

---

## 💡 Key Concepts Demonstrated

- **Text parsing** — Extracting structured data from unstructured plain text
- **String normalization** — Converting `12.5K` → `12500`, `681K` → `681000`
- **File I/O** — Reading `.txt`, writing `.json` with UTF-8 encoding (supports emojis 🎉)
- **Data analysis** — Finding max values, unique categories using Python builtins

---

## 🚀 Possible Extensions

- [ ] Visualize follower distribution with Matplotlib / Seaborn
- [ ] Categorize profiles using keyword-based classification
- [ ] Build a searchable web UI with Flask or Streamlit
- [ ] Auto-scrape live data using Selenium or Instaloader
- [ ] Export to Excel/CSV for further analysis

---

## 🙏 Credits

Project concept inspired by **[Code with Harry](https://www.youtube.com/@CodeWithHarry)** — one of India's most popular coding educators.

---

## 👤 Author

**Alhaj** — BCA Final Year | Data Analytics & Cybersecurity  
[GitHub](https://github.com/alhajgaming) • [LinkedIn](https://www.linkedin.com/in/alhaj-khan-611211292/)

---

> *"Data is everywhere — even in Instagram bias."*
