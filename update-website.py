from subprocess import call
from docx import Document

call(["git", "add", "."])
call(["git", "commit", "-m", "\"Update\""])
call(["git", "push"])

doc = Document("frontpage.docx")
for p in doc.paragraphs:
	print(p.text)

input()