
# 📄 Resume Ranker & Parser — AI-Driven Resume Shortlisting System

A smart resume filtering application that automatically **extracts resume text, matches it against a job description, and ranks candidates based on relevance** using NLP and cosine similarity.

This tool is designed to streamline the hiring process by helping recruiters shortlist candidates quickly and objectively.
## 🖥️ Demo Screenshot

<p align="center">
  <img src="twitter_streaming_dashboard.png" width="900">
</p>

## 🧠 Overview
This project demonstrates how **AI + NLP can automate resume screening**.  
It allows HR personnel and hiring teams to upload multiple PDF resumes and compare them against a job description.

The system extracts text from each resume, preprocesses it, converts it into TF-IDF vectors, and computes **cosine similarity scores** to calculate a match percentage.

### 🔍 What the tool delivers
✔ Extracts text from resumes (PDF)  
✔ Cleans and preprocesses text  
✔ Matches resumes with job description  
✔ Ranks candidates based on similarity score  
✔ Allows downloads of ranked results in CSV format  

---

## 🏗️ Architecture

```

📂 Upload Resumes (PDF)
↓
🧾 PDF Text Extraction (pdfplumber)
↓
🧹 Text Cleaning & Preprocessing
↓
🧠 TF-IDF + Cosine Similarity Matching
↓
📊 Ranking & CSV Export via Streamlit UI

```

---

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| UI Framework | Streamlit |
| Text Extraction | pdfplumber |
| NLP / Vectorization | TF-IDF |
| Similarity Scoring | Cosine Similarity |
| Language | Python |

---

## 📂 Project Structure

```

├── app.py                     # Main Streamlit UI
├── parser.py                  # Resume text extraction & cleaning
├── matcher.py                 # TF-IDF similarity calculator
├── requirements.txt
└── resume_ranker_dashboard.png (optional screenshot)

````

---

## ⚙️ Setup & Execution

### 🔹 Requirements
- Python 3.8+
- Virtual environment recommended
- PDF resumes

### 🔹 Installation
```bash
pip install -r requirements.txt
````

### 🔹 Run the application

```bash
streamlit run app.py
```

---

## 🧪 Example Workflow

1. Paste a **Job Description** in the textarea
2. Upload **one or more resumes (PDF format)**
3. Click **Rank Resumes**
4. View:

   * Candidate names
   * Match % Scores
5. Download results as CSV

---

## 📌 Key Features & Learning Outcomes

| Capability               | Demonstrated Skill           |
| ------------------------ | ---------------------------- |
| PDF Resume Parsing       | Document Processing          |
| Job Description Matching | NLP Similarity Scoring       |
| Resume Ranking           | Data Sorting & Scoring       |
| UI for Recruiters        | Streamlit Application Design |
| CSV Export               | Data Reporting               |
| Modular Code             | Scalable Project Structure   |

---

## 🔮 Potential Enhancements

| Future Upgrade                 | Benefit                       |
| ------------------------------ | ----------------------------- |
| Experience-aware scoring       | Score based on skill keywords |
| Keyword cloud                  | Highlight missing skill gaps  |
| Support for DOCX files         | More flexibility              |
| LLM-based scoring (BERT / GPT) | Smart semantic understanding  |
| Applicant dashboard & database | ATS-level automation          |

---

## 🧑‍💻 Author

| Developer        | Profile                                                                 |
| ---------------- | ----------------------------------------------------------------------- |
| **Sakshi Asati** | [LinkedIn Profile](https://www.linkedin.com/in/sakshi-asati-27984b277/) |

---

