# 📄 ATS-Friendly Resume Generator with Hyperlinks

This project is a **Streamlit-based resume builder** that creates **ATS-compliant, modern resumes** in both **HTML and PDF formats**. It includes **clickable hyperlinks** to LinkedIn, GitHub, and email. The resume content is fully customizable and supports structured input for sections like skills, experience, education, certifications, projects, and summary.

---

## 🚀 Features

- ✅ Generate resumes that are ATS-friendly and professional
- 🔗 Clickable hyperlinks for contact info (LinkedIn, GitHub, Email)
- 🛠 Supports structured resume sections:
  - Skills
  - Work Experience
  - Education
  - Certifications
  - Projects
  - Summary
- 📄 Export resumes as **HTML and PDF**
- 🎨 Jinja2-based resume templating for easy customization
- ⚙️ Built using **Streamlit** for quick UI rendering

---

## 📁 Project Structure

```bash
ATS_Resume_Generator/
├── app.py                    # Main Streamlit frontend
├── resume_builder.py         # Logic to generate resume (HTML/PDF)
├── keyword_matcher.py        # (Optional) Keyword analysis from job descriptions
├── templates/
│   └── resume_template.html  # Jinja2 HTML resume template
├── style.css                 # Optional styling for Streamlit
├── requirements.txt          # Python dependencies
