       
import streamlit as st
from resume_builer import render_resume

#importing the css
def local_css(styles):
    with open(styles) as f :
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
        # call the function
        local_css("styles.css")
# setting the page title and layout
st.set_page_config(layout="centered", page_title="📄 ATS Resume Generator")

st.title("📄 ATS-Friendly Resume Builder with Hyperlinks")

# User Input for resume
name = st.text_input("Full Name")
email = st.text_input("Email")
linkedin = st.text_input("LinkedIn URL")
github = st.text_input("GitHub URL")
summary = st.text_area("Professional Summary")

skills = st.text_area("Skills (comma-separated)").split(',')

experience = []
st.subheader("Experience")
for i in range(2):
    title = st.text_input(f"Job Title {i+1}")
    company = st.text_input(f"Company {i+1}")
    years = st.text_input(f"Years (e.g. 2020-2022) {i+1}")
    details = st.text_area(f"Details {i+1}")
    if title and company:
        experience.append({"title": title, "company": company, "years": years, "details": details})

education = []
st.subheader("Education")
for i in range(2):
    degree = st.text_input(f"Degree {i+1}")
    institution = st.text_input(f"Institution {i+1}")
    year = st.text_input(f"Year {i+1}")
    if degree and institution:
        education.append({"degree": degree, "institution": institution, "year": year})

certifications = st.text_area("Certifications (comma-separated)").split(',')

projects = []
st.subheader("Projects")
for i in range(2):
    pname = st.text_input(f"Project Name {i+1}")
    pdesc = st.text_area(f"Description {i+1}")
    if pname:
        projects.append({"name": pname, "description": pdesc})

# Resume Button
if st.button("🚀 Generate Resume"):
    resume_data = {
        "name": name,
        "email": email,
        "linkedin": linkedin,
        "github": github,
        "summary": summary,
        "skills": [s.strip() for s in skills if s.strip()],
        "experience": experience,
        "education": education,
        "certifications": [c.strip() for c in certifications if c.strip()],
        "projects": projects,
    }

    html_file, pdf_file = render_resume(resume_data)
    st.success("✅ Resume Generated!")

    with open(html_file, "r", encoding="utf-8") as f:
        st.download_button("⬇ Download HTML Resume", f.read(), file_name="resume.html", mime="text/html")

    try:
        with open(pdf_file, "rb") as f:
            st.download_button("⬇ Download PDF Resume", f, file_name="resume.pdf", mime="application/pdf")
    except:
        st.warning("⚠ PDF download failed — Install wkhtmltopdf for PDF support")