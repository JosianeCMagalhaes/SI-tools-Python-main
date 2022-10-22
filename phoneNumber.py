import phonenumbers

from phonenumbers import geocoder

phone = input("Digite o telefone no formate: +5511400028922: ")

phoneNumbers = phonenumbers.parse(phone)

print(geocoder.description_for_number(phoneNumbers, 'pt'))