import sys
import os
import streamlit as st
from parser import extract_text_from_pdf, clean_text
from matcher import compute_similarity
import pandas as pd

st.set_page_config(page_title="Resume Shortlisting Tool", layout="centered")
st.title("📄 Resume Shortlisting & Ranking Tool")

# 1. Job Description Input
st.header("1. Job Description")
jd_text = st.text_area("Paste Job Description Here", height=200)

# 2. Resume Upload
st.header("2. Upload Resumes")
uploaded_files = st.file_uploader("Upload one or more resumes (PDF format)", type=["pdf"], accept_multiple_files=True)

# 3. Run Matching
if st.button("Rank Resumes") and jd_text and uploaded_files:
    resume_texts = []
    resume_names = []

    for file in uploaded_files:
        raw_text = extract_text_from_pdf(file)
        cleaned = clean_text(raw_text)
        resume_texts.append(cleaned)
        resume_names.append(file.name)

    # 4. Compute Similarity Scores
    scores = compute_similarity(resume_texts, jd_text)
    results = pd.DataFrame({
        "Candidate": resume_names,
        "Match Score (%)": [round(score * 100, 2) for score in scores]
    }).sort_values(by="Match Score (%)", ascending=False)

    # 5. Display Results
    st.header("3. Ranked Candidates")
    st.dataframe(results)

    # 6. Download Option
    csv = results.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download Results as CSV", data=csv, file_name="ranked_candidates.csv", mime="text/csv")

# Optional: Show text of uploaded single resume (for testing/debugging)
if uploaded_files and len(uploaded_files) == 1:
    st.header("Preview Extracted Text from Resume")
    single_resume_text = clean_text(extract_text_from_pdf(uploaded_files[0]))
    st.text_area("Extracted Resume Text", single_resume_text, height=400)
