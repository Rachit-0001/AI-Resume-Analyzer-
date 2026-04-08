# 🚀 AI Resume Analyzer  
### ATS Score + Skill Gap Detection using NLP & Flask

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)  
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)  
![spaCy](https://img.shields.io/badge/NLP-spaCy-orange)  
![scikit-learn](https://img.shields.io/badge/ML-scikit--learn-yellow)  
![Frontend](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-red)  
![PDF](https://img.shields.io/badge/PDF-pdfplumber-lightgrey)  
![DOCX](https://img.shields.io/badge/DOCX-python--docx-blueviolet)  

---

## 📌 Overview

**AI Resume Analyzer** is a smart web application that analyzes resumes (PDF/DOCX), evaluates them based on job roles, and provides:

- 📊 ATS Score  
- ✅ Matched Skills  
- ❌ Missing Skills  
- 💡 Suggestions for improvement  

This tool helps students and job seekers improve their resumes and increase their chances of getting shortlisted.

---

## ✨ Features

- 📄 Upload resumes in **PDF & DOCX format**  
- 🎯 Role-based skill matching  
- 🧠 NLP-based processing using spaCy  
- 📊 ATS score calculation  
- 🔍 Missing skills detection  
- ⚡ Fast and lightweight Flask backend  
- 🌐 Simple UI (HTML, CSS, JS)  

---

## 🧠 How It Works

1. Upload resume (PDF/DOCX)  
2. Extract text using:
   - `pdfplumber` (PDF)
   - `python-docx` (DOCX)  
3. Clean text using regex  
4. Process text using spaCy  
5. Match skills based on selected role  
6. Calculate ATS Score:



7. Generate suggestions  


---

## ⚙️ Tech Stack

### 🧠 Backend
- Python  
- Flask  
- spaCy  
- scikit-learn  

### 📄 File Processing
- pdfplumber (PDF parsing)  
- python-docx (DOCX parsing)  

### 🎨 Frontend
- HTML  
- CSS  
- JavaScript  

---

## 🧩 Dependencies

| Library        | Purpose                      |
|---------------|-----------------------------|
| Flask         | Web framework               |
| spaCy         | NLP processing              |
| scikit-learn  | Similarity & scoring        |
| pdfplumber    | Extract text from PDFs      |
| python-docx   | Read DOCX files             |
| re            | Text cleaning               |


---
Use Cases
-Resume optimization for students
-Placement preparation
-AI-based hiring tools
-College mini/major projects

----

Author-
Rachit Gangwar
If you like this project, give it a ⭐ on GitHub!
---

## 📊 Sample Output

```json
{
  "score": 80.0,
  "skills": ["python", "html", "css"],
  "missing": ["react", "node"],
  "suggestions": ["Add these skills: react, node"]
} 
 
