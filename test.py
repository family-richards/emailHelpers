from os import getenv
def test_make_email():
  from emailHelpers import Email
  email = Email("kidscodingplace@gmail.com")
  email.setTo("kidscodingplace@gmail.com")
  email.setSubject("Does this thing work?")
  emailstr = email.as_string()

def test_add_attatchment():
  from emailHelpers import Email
  email = Email("kidscodingplace@gmail.com")
  with open("test.txt", "w") as t:
    t.write("testing...")
  email.addAttachmentFromFile("test.txt")
  email.addMyselfToEmail()
