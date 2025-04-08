import markdown
import pdfkit

file = '.\chapters\md_study1\README.md'
# Read the content of the markdown file
with open(file, 'r') as f:
    md_content = f.read()

# Convert markdown content to HTML
html_content = markdown.markdown(md_content)

# Convert HTML content to PDF
pdfkit.from_string(html_content, 'output.pdf')

print("The markdown file has been successfully converted to output.pdf.")