from os import listdir
from xmlrpc.client import DateTime
import pandas
from datetime import *
import random
import smtplib
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
#name,email,year,month,day

dict = {
    'name': ['Jit', 'trev', 'mik', 'yuv'],
    'email': ['jit@gmail.com', 'avumig@gmail.com', 'mikunjrathwa@gmail.com', 'ycgohil@gmail.com'],
    'year' : [1993, 1994, 1993, 1994],
    'month': [8, 9, 9, 9],
    'day': [22, 6, 7, 8]
}

df = pandas.DataFrame(dict)
df.to_csv('birthdays.csv', index=False)

all_letters = listdir('letter_templates')

# 2. Check if today matches a birthday in the birthdays.csv
today_date = date.today()
birthdate_data = pandas.read_csv('birthdays.csv')
birthdate_data_dict = {i:v for (i,v) in birthdate_data.iterrows() if (v.day, v.month) == (today_date.day, today_date.month)}

for rec in birthdate_data_dict.values():
    print(rec)
    print(rec['name'])
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    letter_to_send = random.Random().choice(all_letters)
    with open(f'letter_templates/{letter_to_send}') as letter_file:
        mail_text = letter_file.read().replace('[NAME]', rec['name'])
    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        connection.starttls()
        connection.login('mikunjrathwa@gmail.com', 'meomimbakhswbjls')
        connection.sendmail('mikunjrathwa@gmail.com', rec.email, f'Subject:Happy birthday!! \n\n{mail_text}')
        

