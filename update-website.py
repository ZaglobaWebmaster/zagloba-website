from subprocess import call
from docx import Document

call(["git", "add", "."])
call(["git", "commit", "-m", "\"Update\""])
call(["git", "push"])

doc = Document("frontpage.docx")
p = doc.paragraphs
r = range(len(p))
for i in r:
	text = p[i].text
	r.remove(i)
	if text == "BANNER":
		i += 1
		r.remove(i)
		print("Banner Text:")
		print(p[i].text)
	elif text == "EVENT":
		i += 1
		r.remove(i)
		print("Event Details:")
		event_name = str(p[i].text).replace("Name: ", "")
		i += 1
		r.remove(i)
		event_name += "\n"
		event_details = str(p[i].text).replace("Location: ", "")
		i += 1
		r.remove(i)
		event_details += " - "
		event_details += str(p[i].text).replace("Date: ", "")
		i += 1
		r.remove(i)
		event_details += " - "
		event_details += str(p[i].text).replace("Time: ", "")
		print(event_name + event_details)
	print(i)

input()