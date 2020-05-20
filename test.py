from os import getenv
def test_make_email():
  # Declare email
  from emailHelpers import Email
  # Set sender
  email = Email("send@gmail.com")
  # Set to
  email.set_to("testy@example.com")
  # Set subject
  email.set_subject("Does this thing work?")
  # Set body
  email.set_body("""Hello world!
This is just a test. Bye!""")
  # Test as string
  emailstr = email.as_string()

def advanced_email():
  # Declare email
  from emailHelpers import Email
  # Set sender
  email = Email("send@gmail.com")
  # Set to
  email.set_to("testy@example.com")
  # Test override
  email.set_to("boopy@example.com")
  # Test mime_behind
  mimeBehind = email.mime_behind()
  # Test get_attr
  fromPerson = email.get_attr("From")

def test_add_attatchment():
  # Declare email
  from emailHelpers import Email
  email = Email("kidscodingplace@gmail.com")
  # Make dummy file
  with open("test.txt", "w") as t:
    t.write("testing...")
  # Test adding file
  email.add_attachment_from_file("test.txt")
  # Test adding self
  email.add_myself_to_email()
