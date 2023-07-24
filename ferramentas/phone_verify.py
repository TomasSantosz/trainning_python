import phonenumbers 

from phonenumbers import geocoder

phone = '+553133616246'
##input('Número: formato(+553133616246)')

phone_number = phonenumbers.parse(phone)
print(geocoder.description_for_valid_number(phone_number, 'pt'))
