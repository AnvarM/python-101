import smtplib

def send_email(host, subject, to_addr, from_addr, body_text):
    """
    Send an email
    """
    BODY = "\r\n".join((
    "From: %s" % from_addr,
    "To: %s" % to_addr,
    "Subject: %s" % subject ,
    "",
    body_text
    ))
    server = smtplib.SMTP(host)
    server.sendmail(from_addr, [to_addr], BODY)
    server.quit()
    
if __name__ == "__main__":
    host = "mySMTP.server.com"
    subject = "Test email from Python"
    to_addr = "to@address.org"
    from_addr = "from@addres.com"
    body_text = "Test message"
    send_email(host, subject, to_addr, from_addr, body_text)    