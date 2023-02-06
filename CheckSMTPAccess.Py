import smtplib

def CheckSmtpServer(Host, Port):
    try:
        Smtp = smtplib.SMTP(Host, Port)
        Smtp.ehlo()
        Smtp.quit()
        return True
    except:
        return False

# Example usage
Hosts = ["smtp-mail.outlook.com", "smtp.office365.com"]
Ports = [587, 25, 465]

for Host in Hosts:
    for Port in Ports:
        if CheckSmtpServer(Host, Port):
            print("SMTP server is accessible With "+Host+':'+Port)
        else:
            print("SMTP server is not accessible")

#python CheckSMTPAccess.Py
