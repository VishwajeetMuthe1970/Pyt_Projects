import phonenumbers  # Install phonenumbers module using cmd.
from phonenumbers import timezone,  geocoder, carrier

# To take phone number from the user.
number = input("Enter your number using +__ : ")

# Passing the details related to the number provided by the user.

phone = phonenumbers.parse(number)  # To fetch the details of the phone number.
time = timezone.time_zones_for_number(phone)  # To get the timezone of the number.
car = carrier.name_for_number(phone, "en")  # `en` : To get the name of the service provider name in english.
reg = geocoder.description_for_number(phone, "en")  # Region

print(phone)
print(time)
print(car)
print(reg)


