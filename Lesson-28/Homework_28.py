import os
import json
import hashlib
import smtplib
from email.mime.text import MIMEText
import string
import random

BANK_EMAIL = 'SENDER_EMAIL'
EMAIL_PASSWORD = 'SENDER_APP_PASSWORD'


class BankUser:
    @staticmethod
    def check_person(name, surname):
        if name.isalpha() and surname.isalpha():
            return True
        return False
    
    @staticmethod
    def check_age(age):
        if not str(age).isdigit():
            return False
        age = int(age)
        if age < 16:
            return False
        return True
    
    @staticmethod
    def check_card_number(card_number):
        if card_number.isdigit() and len(card_number) == 16:
            return True
        
        parts = card_number.split()
        if len(parts) == 4 and all(p.isdigit() and len(p) == 4 for p in parts):
            return True
        
        return False
    
    @staticmethod
    def check_money(money):
        if not str(money).isdigit():
            return False
        if int(money) < 0:
            return False
        return True
    
    @staticmethod
    def check_pin(pin):
        if len(pin) < 8:
            return False
        if not any(c in string.ascii_uppercase for c in pin):
            return False
        if not any(c in string.ascii_lowercase for c in pin):
            return False
        if not any(c in string.digits for c in pin):
            return False
        if not any(c in string.punctuation for c in pin):
            return False
        return True
    
    @staticmethod
    def check_email(email):
        allowed_chars = string.ascii_letters + string.digits + "@._-"
        allowed_domains = ["gmail.com", "mail.ru", "yahoo.com", "outlook.com", "hotmail.com", "icloud.com"]
        
        if "@" not in email or "." not in email:
            return False
        
        for c in email:
            if c not in allowed_chars:
                return False
        
        if len(email) < 6:
            return False
        
        if email.startswith("@") or email.endswith("@"):
            return False
        if email.startswith(".") or email.endswith("."):
            return False
        
        domain = email.split("@")[-1]
        if domain not in allowed_domains:
            return False
        
        return True
    
    def __init__(self, name, surname, email, age, card_number, money_on_card, pin=None, hash_pin=None):
        if self.check_person(name, surname):
            self._name = name
            self._surname = surname
        else:
            raise ValueError("Invalid name")
        
        if self.check_email(email):
            self._email = email
        else:
            raise ValueError("Invalid email")
        
        if self.check_age(age):
            self._age = int(age)
        else:
            raise ValueError("Invalid age")
        
        if self.check_card_number(card_number):
            self.__card_number = card_number
        else:
            raise ValueError("Invalid card number")
        
        if self.check_money(money_on_card):
            self.__money_on_card = int(money_on_card)
        else:
            raise ValueError("Invalid money on card")
        
        if hash_pin is not None:
            self.__pin = hash_pin
        elif pin is not None and self.check_pin(pin):
            self.__pin = hashlib.sha256(pin.encode()).hexdigest()
        else:
            raise ValueError("Invalid pin")
        
        self.is_blocked = False
        self._filename = f"{self._name}_{self._surname}.json"
        self._save()
        self.load()
    
    def _save(self):
        data = {
            "name": self._name,
            "surname": self._surname,
            "email": self._email,
            "age": self._age,
            "card_number": self.__card_number,
            "money_on_card": self.__money_on_card,
            "pin": self.__pin,
            "is_blocked": self.is_blocked
        }
        try:
            with open(self._filename, "w") as f:
                json.dump(data, f)
        except Exception as e:
            print("Error saving:", e)
    
    def load(self):
        try:
            with open(self._filename, "r") as f:
                data = json.load(f)
            if data:
                self._name = data.get("name", self._name)
                self._surname = data.get("surname", self._surname)
                self._email = data.get("email", self._email)
                self._age = data.get("age", self._age)
                self.__card_number = data.get("card_number", self.__card_number)
                self.__money_on_card = data.get("money_on_card", self.__money_on_card)
                self.__pin = data.get("pin", self.__pin)
                self.is_blocked = data.get("is_blocked", self.is_blocked)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass
    
    def verify_pin(self):
        attempts = 3
        while attempts > 0:
            entered = input("your PIN: ")
            if entered == self.__pin:
                return True
            attempts -= 1
            print(f"Wrong PIN, try again. Your attempts: {attempts}")
        print("Your card is blocked, you can unblock it! Use an Unblock_card().")
        self.is_blocked = True
        return False
    
    def __str__(self):
        return """
            Available actions:
                1. add_money()           - Add money to your account
                2. remove_money()        - Take money from your account
                3. get_card_info()       - View your current balance
                4. get_personal_info()   - View your personal info
                5. unblock_card()        - Unblock the card
        """
    
    def get_personal_info(self):
        if self.is_blocked:
            return 'Your card is blocked, you can unblock it use "unblock_card" method'
        
        return f"Name: {self._name} {self._surname}\nAge: {self._age}\nEmail: {self._email}"
    
    def get_card_info(self):
        if self.is_blocked:
            return 'Your card is blocked, you can unblock it use "unblock_card" method'
        
        if self.verify_pin():
            masked_card = '*' * 12 + self.__card_number[-4:]
            return f"{masked_card}, {self.__money_on_card}"
        else:
            return "ou cannot access the information because your card is blocked."
    
    def add_money(self, money):
        if self.is_blocked:
            return 'Your card is blocked, you can unblock it use "unblock_card" method'
        
        if int(money) > 0:
            self.__money_on_card += int(money)
            self._save()
            return f"Your card has been added {money}."
        else:
            return "You can't add negative money"
    
    def remove_money(self, money):
        if self.is_blocked:
            return 'Your card is blocked, you can unblock it use "unblock_card" method'
        
        if self.verify_pin():
            if int(money) > 0 and self.__money_on_card - int(money) > 0:
                self.__money_on_card -= int(money)
                self._save()
                return f"Your card has been removed {money}."
            else:
                return "You don't have enough money."
        else:
            return "ou cannot remove money because your card is blocked."
    
    def unblock_card(self):
        code = random.randint(1000000, 9999999)
        to_email = self._email
        subject = "Bank"
        body = f'The verification code is {code}.'
        
        msg = MIMEText(body)
        msg['From'] = BANK_EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject
        
        if self.is_blocked:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(BANK_EMAIL, EMAIL_PASSWORD)
                server.send_message(msg)
            
            inp = input('Enter the code we sent you by email: ')
            
            if inp == str(code):
                self.is_blocked = False
                self._save()
                return 'Your card is successfully unblocked'
            else:
                return 'wrong code, try again'


name = input("Enter your name: ").strip()
surname = input("Enter your surname: ").strip()

filename = f"{name}_{surname}.json"

if os.path.exists(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    client = BankUser(
        name=data["name"],
        surname=data["surname"],
        email=data["email"],
        age=data["age"],
        card_number=data["card_number"],
        money_on_card=data["money_on_card"],
        pin=None,
        hash_pin=data["pin"]
    )
    print("Welcome back!")
else:
    email = input("Enter your email: ")
    age = int(input("Enter your age: "))
    card_number = input("Enter your card number: ")
    money_on_card = input("Enter your money on card: ")
    pin = input("Enter your pin: ")
    
    client = BankUser(
        name=name,
        surname=surname,
        email=email,
        age=age,
        card_number=card_number,
        money_on_card=money_on_card,
        pin=pin
    )
    print("Your account has been created!")
