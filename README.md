# emailHelpers
![Test lint and build](https://github.com/family-richards/Python-Email-Helpers/workflows/Test%20lint%20and%20build/badge.svg) ![Upload To PyPi](https://github.com/family-richards/Python-Email-Helpers/workflows/Upload%20To%20PyPi/badge.svg)  
emailHelpers is a wrapper for the `smtplib` and `email` packages. Here's an example diff to the traditional way:

```diff
-  import smtplib
-  from email.MIMEMultipart import MIMEMultipart
-  from email.MIMEText import MIMEText
+  from emailHelpers import Mailer, Email
fromaddr = "YOUR ADDRESS"
toaddr = "ADDRESS YOU WANT TO SEND TO"

- email = MIMEMultipart()
+ email = Email(fromaddr)
- email['From'] = fromaddr
- email['To'] = toaddr
+ email.set_to(toaddr)
- email['Subject'] = "SUBJECT OF THE MAIL"
+ email.set_subject("SUBJECT OF THE MAIL")
 					
body = "YOUR MESSAGE HERE"
- email.attach(MIMEText(body, 'plain'))
 				
- mailer = smtplib.SMTP('smtp.gmail.com', 587)
+ mailer = Mailer(fromaddr, "YOUR PASSWORD")
- mailer.starttls()
- mailer.login(fromaddr, "YOUR PASSWORD")
text = email.as_string()
- mailer.sendmail(fromaddr, toaddr, text)
+ mailer.send_mail(text, toaddr)
- mailer.quit()
```
As you can see, it reduces code size and complexity. It also has simple names, so you can easily code something new. Why emailHelpers? It's pretty well [documented](#emailhelpers-docs) too.  
To install emailHelpers, use pip. On a platform that only has Python 3:
```bash
python -m pip install emailHelpers
```
On a platform with Python 2 and Python 3:
```bash
python3 -m pip install emailHelpers
```
Get started coding with emailHelpers now with these docs:
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
Finally, just for the fun of it, you can call `addMyselfToEmail` to add the library as an attachment to your `Email` object. It's used like this:  
```python3
email.add_myself_to_mail()
```
## Internals... probably not needed by you
If you want to attatch a file from a variable, use `addAttachment`. It takes the attachment and the filename to call it.  
Use it like this:  
```python3
email.add_attachment(loadedattachment, "filename")
```
To load a file, use `loadAttachment`. It will return a file that can be passed to `addAttachment`.
Use it like this:  
```python3
file = email.load_attachment(["complex.stuff"])
```
The simpler function, if you don't want to disguise your filename, is addAttachmentFromFile. It was covered [earlier](#attaching-files-for-email).
To get the `MIMEMultipart` behind the object, use `MimeBehind`.
Use it like this:  
```python3
multipart = email.mime_behind()
```
To access properties of the `MIMEMultipart`, use `getAttr` and `setAttr`.
They are used like this:  
```python3
attribute = email.get_attr("attribute to get")
email.set_attr("attribute to set","new value of attribute")
```
You're dedicated to read all of this, you know. Good job! I hope that this library makes managing emails easier.
See you later! If you have any questions or bugs, feel free to make an issue. Enjoy!
