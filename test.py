from os import getenv
def test_make_email():
  from emailHelpers import Email
  email = Email("kidscodingplace@gmail.com")
  email.set_to("kidscodingplace@gmail.com")
  email.set_subject("Does this thing work?")
  emailstr = email.as_string()

def test_add_attatchment():
  from emailHelpers import Email
  email = Email("kidscodingplace@gmail.com")
  with open("test.txt", "w") as t:
    t.write("testing...")
  email.add_attachment_from_file("test.txt")
  email.add_myself_to_email()
