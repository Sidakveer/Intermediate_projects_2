import random
import smtplib
import datetime as dt
import pandas

TEMPLATES = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
my_email = ""
password = ""

data = pandas.read_csv("birthdays.csv")
dict_data = data.to_dict(orient="records")
print(dict_data)

today = dt.datetime.now()
for dictionary in dict_data:
    if today.day == dictionary["day"] and today.month == dictionary["month"]:
        letter_temp = random.choice(TEMPLATES)
        with open(f"letter_templates/{letter_temp}") as file1:
            data1 = file1.read()
            data1 = data1.replace("[NAME]", dictionary["name"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=dictionary["email"], msg=data1)
