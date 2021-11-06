"""# PDF to Text
    -https://python.plainenglish.io/how-to-automate-the-cool-and-awesome-stuff-with-python-7f5c470f1ed
TODO:
"""

import pdfplumber

# with pdfplumber.open('sample.pdf') as pdf:
pdf = pdfplumber.open('sample.pdf')
print("No of Pages: ", print(len(pdf.pages)))

page = pdf.pages[0] # Scraping page
Text = page.extract_text()
print(Text)

pdf.close()
