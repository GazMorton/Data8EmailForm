"""this section is checking the syntax of email addresses entered by users, checks performed:
- email contains one @ symbol
- email contains a full stop
- email contains one of the 5 most common domain extensions, I've used list comprehension to check
loop through the common ext's and if len of this list is greater than 0 it means at least one of these
extensions has been used
"""

common_domain_extensions = ['.com', '.net', '.org', '.co', '.co.uk']
email = input('Please enter your email address: ')
if '@' not in email or email.count('@') != 1 or '.' not in email or len([x for x in common_domain_extensions if x in email]) == 0:
    print('Please enter a valid email address')
else:
    print('Thank you, your email address is valid')


"""This code is from a tutorial I found on youtube, it sends an email to the user directly upon running the Python code.
In this case the email sent would prompt the user to verify that their email address has been entered correctly by clicking on a 'here' hyperlink.
If users have confirmed by clicking the hyperlink this proves that they've entered the correct email address, as a further step I would need to write code that flags
an error if the email didn't go through, of course the email can still go to an incorrect email address, but this user would be unlikely to confirm 
"""
from email.message import EmailMessage
import ssl
import smtplib
email_sender = 'gazmorto9@gmail.com'
email_password = 'luiqpehnkixijdha'
email_receiver = 'gazmorton8@hotmail.com'

subject = 'Email Verification Data8'
body = """
Please click here to confirm your email address
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())




