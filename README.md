<h1 align="center">emailHelpers</h1>
<p align="center">
<a href="https://github.com/family-richards/emailhelpers/actions?query=workflow%3A%22Test+lint+and+build%22">
  <img alt="Test lint and build status" src="https://img.shields.io/github/workflow/status/family-richards/emailHelpers/Test lint and build?logo=github&label=Lint%20%2B%20Build&labelColor=080808"/>
</a>
<br>
<a href="https://github.com/family-richards/emailhelpers/actions?query=workflow%3A%22Upload+To+PyPi%22">
  <img alt="Upload to PyPi status" src="https://img.shields.io/github/workflow/status/family-richards/emailHelpers/Upload To PyPi?logo=github&label=Upload%20to%20PyPi&labelColor=080808"/>
</a>
<br>
<a href="https://github.com/family-richards/emailhelpers/actions?query=workflow%3A%22Upload+To+PyPi%22">
  <img alt="VirusTotal check status" src="https://img.shields.io/github/workflow/status/family-richards/emailHelpers/VirusTotal Check?logo=virustotal&label=VirusTotal%20Scan&labelColor=080808&logoColor=394EFF"/>
</a>
</p>
  
[![emailHelpers logoimage](https://raw.githubusercontent.com/family-richards/emailHelpers/master/pyart-helpers.png)]()  
#### emailHelpers is a wrapper for the `smtplib` and `email` packages so it's easy to send emails in your projects.
Here's an example of how to send a `Gmail` message:
```python3
from emailHelpers import Mailer, Email
fromaddr = "example@example.com"
toaddr = "person@example.com"

email = Email(fromaddr)
email.set_to(toaddr)
email.set_subject("Example.")
email.set_body("It's an example!")

mailer = Mailer(fromaddr, "YOUR PASSWORD")
text = email.as_string()
mailer.send_mail(text, toaddr)
```
It's a lot less complicated compared to the normal way:
```python3
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
fromaddr = "YOUR ADDRESS"
toaddr = "ADDRESS YOU WANT TO SEND TO"

email = MIMEMultipart()
email["From"] = fromaddr
email["To"] = toaddr
email["Subject"] = "SUBJECT OF THE MAIL"
 					
body = "YOUR MESSAGE HERE"
email.attach(MIMEText(body, "plain"))
 				
mailer = smtplib.SMTP("smtp.gmail.com", 587)
mailer.starttls()
mailer.login(fromaddr, "YOUR PASSWORD")
text = email.as_string()
mailer.sendmail(fromaddr, toaddr, text)
mailer.quit()
```
  
`emailHelpers` makes it easier to code your project, reduces the complexity of it, and also makes it easier to read (in my opinion).  
## Installing `emailHelpers`
To install emailHelpers, use pip. On a platform that only has Python 3:  
```bash
python -m pip install emailHelpers
```
On a platform with Python 2 and Python 3:
```bash
python3 -m pip install emailHelpers
```
*You may want to add a `--user` to the end.*
#### Warning: The "proper" way to send Gmail is with their official [API](https://developers.google.com/gmail/api/quickstart/python). This is more secure, so if you use Gmail, consider that instead.  
#### Otherwise, as long as you have an STMP server, emailHelpers is just fine with that.  
## Quick start
1. Find out what your Google email address and password are.
2. Let [less secure apps access your account](https://devanswers.co/allow-less-secure-apps-access-gmail-account/).
3. [Install `emailHelpers`](#installing-emailhelpers).
4. You're ready! Use this code for a quickstart:
```python3
from emailHelpers import Mailer, Email
fromaddr = "me@gmail.com"
toaddr = "me@gmail.com"

email = Email(fromaddr)
email.set_to(toaddr)
email.set_subject("emailHelpers is working!")
email.set_body("Yahoo! Move on to the next step: https://family-richards.github.io/emailHelpers/#emailhelpers-docs")

mailer = Mailer(fromaddr, "IhAv3aVeRy3eCuRePa33W0Rd")
text = email.as_string()
mailer.send_mail(text, toaddr)
```


Get started making with emailHelpers now with these docs:
  
  
  
## emailHelpers Docs
emailHelpers is a combination of 2 classes to make the sending and managing of emails in python easier.
It's made of two classes: Mailer and Email.
Once you have added the library as shown in the README, import them as  
```python3
from emailHelpers import Mailer, Email
```
## The `Mailer` Class
#### Declaration for `Mailer`
To use the `Mailer` class, you need to pass it your email adress and your password. It defaults to Gmail, so if it's not gmail the server name and port number need to be passed in.  
So if:
- your email adress was `fred_loves_pickles@vinegar.helps`
- and your password was "vinegar+cucumbers=pickles"
- and your server name was `smtp.vinegar.helps.everyone`
- and the port was 567
  
You would declare your `Mailer` like:  
```python3
mailer = Mailer("fred_loves_pickles@vinegar.helps", "vinegar+cucumbers=pickles", emailServer="smtp.vinegar.helps.everyone", emailServerPort=567)
```
If you use Gmail, in order to make this work, make sure to allow less secure apps. For Gmail, you only need to do this to declare a `Mailer`:  
```python3
mailer = Mailer("freds-work@gmail.com", "fred-work=nothing")
```
#### Sending Email from `Mailer`
To send a mail from a `Mailer`, do this:  
```python3
mailer.send_mail(emailstr, ["freds-friend@anything.com"])
```
That's the Mailer object. Now on to the slightly more complex `Email`.
## The `Email` Class
To use the `Email` class, if your email adress was `fred_loves_pickles@vinegar.helps` you would declare a Email like this:
#### Declaration for `Email`
```python3
email = Email("fred_loves_pickles@vinegar.helps")
```
#### Subject for `Email`
To add a subject, run this:  
```python3
email.set_subject([subject])
```
#### Metadata To field for `Email`
Now, before I say this, I need to explain some things. Do you know how BCC works? It sends it to that person, but the email doesn't say that. To change the part of the email that says who was supposed to recieve it, use this:  
```python3
email.set_to(["soiwassupposed@torecieve.it"])
```
#### Body for `Email`
To add your body, run:  
```python3
email.set_body([body])
```
I recommend using `"""` to have newlines. Example:  
```python3
body = """This is the email body.
This is the second line.
Sincerely, your python script"""
email.set_body([body])
```
#### `as_string()` for `Email`
When you want to send your email object, you should run:  
```python3
email.as_string()
```
So you would run:  
```python3
mailer.send_mail(email.as_string(), ["person@example.com", "anybody@anywhere.com"])
```
to send your email.
#### Attaching Files for `Email`
To attach a file:  
```python3
email.add_attachment_from_file("intruder.png")
```
#### Adding `emailHelpers` to your `Email`
Finally, just for the fun of it, you can call `add_myself_to_email` to add the library as an attachment to your `Email` object. It's used like this:  
```python3
email.add_myself_to_email()
```
## Internals... probably not needed by you
### Attachments
If you want to attatch a file from a variable, use `add_attachment`. It takes the attachment and the filename to call it.  
Use it like this:  
```python3
email.add_attachment(loaded_attachment, "filename")
```
To load a file, use `load_attachment`. It will return a file that can be passed to `add_attachment`.
Use it like this:  
```python3
file = email.load_attachment(["complex.stuff"])
```
The simpler function, if you don't want to disguise your filename, is add_attachment_from_file. It was covered [earlier](#attaching-files-for-email).
To get the `MIMEMultipart` behind the object, use `mime_behind`.
Use it like this:  
```python3
multipart = email.mime_behind()
```
### Custom headers
To access properties of the `MIMEMultipart`, use `get_attr` and `set_attr`.
They are used like this:  
```python3
attribute = email.get_attr("attribute to get")
email.set_attr("attribute to set"," new value of attribute")
```
You're dedicated to read all of this, you know. Good job! I hope that this library makes managing emails easier.
See you later! If you have any questions or bugs, feel free to make an issue. Enjoy!  
<p align="center"><a href="https://saythanks.io/to/kidscodingplace@gmail.com">Consider a thanks</a></p>
