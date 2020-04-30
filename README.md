emailHelpers is a wrapper for the `smtplib` and `email` packages I coded in my spare time. Here's an example diff:

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
As you can see, it reduces code size and complexity. It also has simple names, so you can easily code something new.
  
That's a couple of reasons to use emailHelpers. Complete with docstrings and (mostly) self-explanatory function names, get started now.
To install emailHelpers:  
First, download this repo. Then, navigate in your terminal/shell into the repo. Now, follow the following instructions.  
If you are a Linux/Ubuntu/Raspberry Pi user:  
	Type in your terminal/shell "python3".  
	IMPORTANT: You have to say "install" in the next step, or else there will be an error.  
	If that works, type "sudo python3 setup.py install".  
	If typing in "python3" didn't work, try typing "python".  
	If that doesn't work, install python 3. Look at this page for the files: https://www.python.org/downloads/source  
	After installing python 3, type "sudo python3 setup.py install".  
	But if typing in "python" did work, check and see if it says after "Python " a 3 or a 2.  
	If it's a 3, type "sudo python setup.py install"  
	If it's a 2, install python 3. Look at this page for the files: https://www.python.org/downloads/source/  
	After installing python 3, type "sudo python3 setup.py install".  
If you are a Windows user:  
	Type in your terminal/shell "python3".  
	IMPORTANT: When you run setup.py, you have to say "install" and "--user", or else there will be an error usually.  
	If that works, type "python3 setup.py install --user".  
	If typing in "python3" didn't work, try typing "python".  
	If that doesn't work, install python 3. Look at this page for the files: https://www.python.org/downloads/windows/  
	After installing python 3, type "python3 setup.py install --user".  
	But if typing in "python" did work, check and see if it says after "Python " a 3 or a 2.  
	If it's a 3, type "python setup.py install --user"  
	If it's a 2, install python 3. Look at this page for the files: https://www.python.org/downloads/windows/  
	After installing python 3, type "python3 setup.py install --user".  
Apple and other platforms are coming. If you have a platform that isn't listed, please let the authors know.  
See INTERFACE for more info about how to use this package.  
