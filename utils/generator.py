import random
import string

class EmailPasswordGenerator:
    def generate(self):
        # Генерируем уникальную почту в формате: имя_фамилия_номер_когорты_3цифры@домен
        base_email = "galina_iermonakhova_23" 
        random_digits = ''.join(random.choices(string.digits, k=3))
        email = f"{base_email}_{random_digits}@yandex.ru"
        
        # Генерируем пароль
        password_length = random.randint(8, 12)
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))
        
        return email, password
