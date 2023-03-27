agenda = {
    "urquidi": {
        "phone": "123-456-789",
        "city": "aguascalientes",
        "E-mail": "urquidi@gmail.com",
    },
    "cristiano": {
        "phone": "237-38-191-46",
        "city": "lisboa",
        "E-mail": "el_bicho@gmail.com",
    },
    "dua lipa": {
        "phone": "789-456-123",
        "city": "london",
        "E-mail": "dua_79@gmail.com",
    }
    
}
#accediendo a la informacion de contactos en la agenda.
print ('The information contacts is:')
for contact, info in agenda.items():
    print (f'\nContact: {contact.title()}')
    phone = info["phone"]
    print (f'Phone: {phone}')
    city = info["city"]
    print (f'City: {city.title()}')
    mail = info["E-mail"]
    print (f'E-mail: {mail.title()}')