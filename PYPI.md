![Upload and Check Python Package](https://github.com/family-richards/Python-Email-Helpers/workflows/Upload%20Python%20Package/badge.svg)  
emailHelpers is a wrapper for the smtplib and email packages. Here's an example for how to send a Gmail message:
```python3
from emailHelpers import Mailer, Email
fromaddr = "example@example.com"
toaddr = "person@example.com"

email = Email(fromaddr)
email.setTo(toaddr)
email.setSubject("Example.")
email.setBody("It's an example!")
mailer = Mailer(fromaddr, "YOUR PASSWORD")
text = email.as_string()
mailer.sendMail(text, toaddr)
mailer.quitSelf()
```
It's simple to integrate in projects. Just note that for Gmail you might need to [let less secure apps access your account](https://devanswers.co/allow-less-secure-apps-access-gmail-account/).
