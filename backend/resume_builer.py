# from docx import Document
# import os 

# Template_path = "template/basic template.docx"

# #this function builds a docx resume
# def generate_resume(name, email, skills, experience, matched_keywords):
#     #load a template if exists, else start fresh 
#     if os.path.exists(Template_path):
#         doc = Document(Template_path)
#     else:
#         doc = Document()

#     #fill the word document with user content
#     doc.add_heading(name,0)
#     doc.add_paragraph(email)

#     doc.add_heading("Skills",level = 1)
#     doc.add_paragraph(skills)

#     doc.add_heading("Experience",level = 1)
#     doc.add_paragraph(experience)

#     doc.add_heading("Matched Job Keywords",level = 1)
#     doc.add_paragraph(",".join(matched_keywords))

#     #save the file 
#     output_path = "ATS_Resume.docx"
#     doc.save(output_path)
#     return output_path


from jinja2 import Environment, FileSystemLoader
import pdfkit
import os

def render_resume(data, output_html="resume.html", output_pdf="resume.pdf"):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("resume_template.html")

    html_content = template.render(data)

    # Save HTML
    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html_content)

    # Try to generate PDF
    try:
        pdfkit.from_file(output_html, output_pdf)
    except:
        print("⚠ PDF generation failed — make sure wkhtmltopdf is installed")

    return output_html, output_pdf