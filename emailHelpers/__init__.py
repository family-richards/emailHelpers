"""Two classes to help with emails in python,
credit to: http://web.archive.org/web/20190131064852/http://naelshiab.com/tutorial-send-email-python/
https://stackoverflow.com/questions/5770951/python-how-can-i-change-the-to-field-in-smtp-mime-script-rather-than-adding-a
https://stackoverflow.com/questions/4152963/get-the-name-of-current-script-with-python"""
class Mailer():
    """A class to help with the mailing of emails, default server is gmail."""
    def __init__(self, emailFrom, emailPassword, emailServer='smtp.gmail.com', emailServerPort=465):
        import smtplib
        self.server = smtplib.SMTP_SSL(emailServer, emailServerPort)
        self.server.ehlo()
        self.smtplib = smtplib
        self.emailFrom = emailFrom
        self.emailPassword = emailPassword
        self.emailServer = emailServer
        self.emailServerPort = emailServerPort
        self.server.login(emailFrom, emailPassword)
        self.server.quit()
    def sendMail(self, emailString, people):
        """Sends a mail. The emailString is from an Email's to_string() function. People is a list of items."""
        self.server = self.smtplib.SMTP_SSL(self.emailServer, self.emailServerPort)
        self.server.ehlo()
        self.server.login(self.emailFrom, self.emailPassword)
        self.server.sendmail(self.emailFrom, people, emailString)
        self.server.quit()
class Email():
    """A class to help with the making of emails."""
    def __init__(self, emailFrom):
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email import encoders
        self.encoders = encoders
        self.baseMime = MIMEBase
        self.MimeEmail = MIMEMultipart()
        self.textMime = MIMEText
        self.MimeEmail['From'] = emailFrom
        #self.MimeEmail['To'] = "\n\n"
        #self.MimeEmail['Body'] = ""
    def addAttachment(self, attachment, filename):
        """Add any attachment. The filename for the email can be different than the local filename."""
        part = self.baseMime('application', 'octet-stream')
        part.set_payload((attatchment).read())
        self.encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        self.MimeEmail.attach(part)
    def setSubject(self, subject):
        """Set subject of email."""
        self.setAttr("Subject", subject)
    def setTo(self, to):
        """Set who the email is to."""
        self.setAttr("To", to)
    def _loadAttachment(self, filepath):
        """Load attatchment for adding."""
        return open(filepath, "rb")
    def addAttachmentFromFile(self, filepath):
        """straight add from filename and path to load file"""
        from os.path import basename
        self.addAttachment(self._loadAttachment(filepath), basename(filepath))
    def MimeBehind(self):
        """returns the hidden MIMEMultipart"""
        return self.MimeEmail
    def as_string(self):
        """takes the hidden MIMEMultipart and returns it as string"""
        return self.MimeEmail.as_string()
    def setBody(self, body):
        """Adds body to email."""
        self.MimeEmail.attach(self.textMime(body, 'plain'))
    def getAttr(self,attribute):
        """gets any attribute from the MIMEMultipart"""
        return self.MimeEmail[attribute]
    def setAttr(self,attribute,value):
        """sets any attribute from the MIMEMultipart"""
        if attribute in self.MimeEmail:
            self.MimeEmail.replace_header(attribute, value)
        else:
            self.MimeEmail[attribute] = value
    def addMyselfToEmail(self):
        """Finds this code on your computer and attatches this code to your email!"""
        myDirectoryPath = __file__
        from os.path import basename
        myOwnName = basename(myDirectoryPath)
        self.addAttachmentFromFile(myOwnName,myDirectoryPath)
