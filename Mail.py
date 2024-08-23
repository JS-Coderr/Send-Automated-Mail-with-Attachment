import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#RUN THE ABOVE PART FIRST

fromaddr = "######@gmail.com" #SENDER MAIL-ID

toaddr = "******@gmail.com" #RECIVER MAIL-ID

msg = MIMEMultipart()

# Set sender, receiver, and subject
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Test Mail-Sample" #ENTER THE SUBJECT

# Body of the email
body = "Body of the mail"
msg.attach(MIMEText(body, 'HI ')) #ENTER YOUR MESSSAGE

# Attach the file (replace 'file_path' with the actual file path)
file_path = "Sample_File.csv"
attachment = open(file_path, 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', f'attachment; filename="{file_path}"')
msg.attach(part)

# Connect to Gmail SMTP server
mailServer = smtplib.SMTP("smtp.gmail.com", 587)
mailServer.starttls()

# Login to your Gmail account
mailServer.login(fromaddr, "#################") #ENTER THE PASSWORD HERE (16 digits -Enable Two Step Authentication)

# Send the email
mailServer.sendmail(fromaddr, toaddr, msg.as_string())

# Close the connection
mailServer.quit()