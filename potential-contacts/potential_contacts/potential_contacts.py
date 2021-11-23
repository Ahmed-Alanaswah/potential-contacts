import re

path = "potential-contact.txt"
with open( path, 'r') as file:
    content = file.read()


def get_emails( content ):

    find_email = re.findall( r"[\w.+-]+@[\w-]+.[\w.-]+", content )

    all_email = []

    for email in find_email:
        if not email in all_email:
            all_email.append( email ) 

    all_email = sorted( all_email )

    with open( 'emails.txt', 'w' ) as result:
        for email in all_email:
            result.write( f"{email}\n" )





def get_phones( content ):

    find_phonenumber = re.findall( r'(\d{3}[-.\s]??\d{3}[-.\s]??\d{4}|(\d{3})\s*\d{3}[-.\s]??\d{4}|\d{3}[-.\s]??\d{4})', content )

    all_phone_number = []
    for phone in find_phonenumber:
        # print("".join(list(phone)))
        phone_number="".join(list(phone))

        if "(" in phone_number:
            phone_number = phone_number.replace( "(", "" )

        if ")" in phone_number or "." in phone_number:
            phone_number = phone_number.replace( ")", "-" )
            phone_number = phone_number.replace( ".", "-" )

        if len( phone_number ) == 10:
            phone_number = f"{phone_number[:3]}-{phone_number[3:6]}-{phone_number[6:]}"
        if len( phone_number ) < 10:
            phone_number = f"206-{phone_number[:3]}{phone_number[3:]}"

        if not phone_number in all_phone_number:
            all_phone_number.append( phone_number ) 
    all_phone_number = sorted( all_phone_number )
    with open( 'phone.txt', 'w' ) as result:
        for phone_number in all_phone_number:
       
            result.write( f"{phone_number}\n" )




if __name__ == "__main__":
    email = get_emails(content)
 
    phone_number = get_phones(content)
  
