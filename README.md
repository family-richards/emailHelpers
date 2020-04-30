emailHelpers is a wrapper for the `smtplib` and `email` packages I coded in my spare time. Here's an example diff to the traditional way:

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
email['To'] = toaddr
+ email.setTo(toaddr)
- email['Subject'] = "SUBJECT OF THE MAIL"
+ email.setSubject("SUBJECT OF THE MAIL")
 					
body = "YOUR MESSAGE HERE"
- email.attach(MIMEText(body, 'plain'))
 				
- mailer = smtplib.SMTP('smtp.gmail.com', 587)
+ mailer = Mailer(fromaddr, "YOUR PASSWORD")
- mailer.starttls()
- mailer.login(fromaddr, "YOUR PASSWORD")
text = email.as_string()
- mailer.sendmail(fromaddr, toaddr, text)
+ mailer.sendMail(text, toaddr)
- mailer.quit()
+ mailer.quitSelf()
```
As you can see, it reduces code size and complexity. It also has simple names, so you can easily code something new. Why emailHelpers? It's pretty well [documented](docs.md) too.  
To install emailHelpers, use pip. On a platform that only has Python 3:
```bash
python -m pip install emailHelpers
```
On a platform with Python 2 and Python 3:
```bash
python3 -m pip install emailHelpers
```
[Get started coding with emailHelpers now!](docs.md)
