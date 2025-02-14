import re
import dns.resolver
import smtplib
# include directore in python
# input email by user 

email_input = input("enter your email :")

# this func measurement it email is true or false

def search_email_format(email):
    # search your format email
    raenge_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(raenge_email,email):
        return False , "format not real"
    global domean
    domean = email.split('@')[-1]
    try :
        dns.resolver.resolve(domean,"MX")
        return True ,"format is true"
    except dns.resolver.NoAnswer:
        return False ,"dns not answer"
    except dns.resolver.NXDOMAIN:
        return False ,"dns not domain is true"
    except Exception as e:
        return False , f"erorr when search domain"
    
async def search_email_server(email, domean):
    mx_record = dns.resolver.resolve(domean,"MX")
    mx_record = str(mx_records[0].exchange)
    server = smtplib.SMTP(mx_record)
    server.set_debuglevel(0)
    server.helo()
    server.mail("mmahdis@gmail.com")
    code = server.rcpt(email)
    await server.quit()
    if code ==250 :
        return True , "tihs email is truo"
    else :
        return False ,"thris email is false"
    
if search_email_format(email_input) == True :
    printer = search_email_server(email_input)
    print(printre)