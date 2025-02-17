import re
import dns.resolver
import smtplib
# include directore in python
# input email by user

email_input = input("enter your email :").strip()

# this func measurement it email is true or false

def search_email_format(email_input):
    # search your format email
    raenge_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(raenge_email,email_input):
        return False , "format not real"
    else :
        return True , "format is real"
    
    domean = email_input.split('@')[-1]
    try :
        dns.resolver.resolve(domean,"MX")
        return True ,"format is true"
    except dns.resolver.NoAnswer:
        return False ,"dns not answer"
    except dns.resolver.NXDOMAIN:
        return False ,"dns not domain is true"
    except Exception as e:
        return False , f"erorr when search domain"

def search_email_server(email_input, domean):
    try:
        mx_records = dns.resolver.resolve(domean,"MX")
        mx_record = str(mx_records[0].exchange)
        server = smtplib.SMTP(mx_record)
        server.set_debuglevel(0)
        server.helo()
        server.mail("mmahdis2006@gmail.com")
        code,responce = server.rcpt(email_input)
        server.quit()
        if code == 250 :
            return True ,"is email is true"
        else :
            return False ,"is email is False"
    except Exception as e :
        return False ,f"erorr chaking server {e}"

is_valid ,message = search_email_format(email_input)
if is_valid:
    domean = email_input.split('@')[-1]
    is_realemail, message = search_email_server(email_input,domean)
    if is_realemail:
        print(f"{email_input} is a valid email.")
    else:
        print(f"Email exists check failed: {message}")
else :
    print("this email is not true")
