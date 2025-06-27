import pymysql
import re
import hashlib

# تابع اعتبارسنجی رمز عبور
def pass_validator(password):
    passPattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$'  # حداقل ۶ کاراکتر، شامل حرف و عدد
    return re.match(passPattern, password)

# تابع اعتبارسنجی ایمیل
def user_validator(username):
    userPattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.match(userPattern, username)

# دریافت ایمیل
def get_username():
    while True:
        username = input("Username (email): ")
        if user_validator(username):
            return username
        else:
            print("Invalid email format. Example: example@domain.com\n")

# دریافت رمز عبور
def get_password():
    while True:
        password = input("Password: ")
        if pass_validator(password):
            return password
        else: 
            print("Invalid password. Must be at least 6 characters with letters and numbers.\n")

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# اتصال به MySQL (بدون دیتابیس برای ساخت اولیه)
connection = pymysql.connect(
    host='localhost',
    user='username',
    password='yourpassword'
)

username = get_username()
password = get_password()
hashed_password = hash_password(password)

try:
    cursor = connection.cursor()

    # ایجاد دیتابیس در صورت نبود آن
    cursor.execute("CREATE DATABASE IF NOT EXISTS userpass")
    print("Database successfully created or already exists.")

    # استفاده از دیتابیس userpass
    cursor.execute("USE userpass")

    # ایجاد جدول در صورت عدم وجود
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) UNIQUE,
            password VARCHAR(255)
        )
    """)

    # درج داده‌های کاربر
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
    connection.commit()
    print("User registered successfully.")

    # نمایش کاربران
    cursor.execute("SELECT * FROM users ORDER BY id DESC")
    results = cursor.fetchall()

finally:
    cursor.close()
    connection.close()

# نمایش نتایج
for row in results:
    print(row)
