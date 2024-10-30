import csv
import re
import os


# تابع پاکسازی که فاصله‌ها، خط تیره و دیگر کاراکترهای غیرضروری را حذف می‌کند
def clean_key(key):
    return re.sub(r'[\s\-]', '', key).strip()


# تابعی برای ایجاد نام فایل خروجی جدید با شمارنده در صورت نیاز
def get_unique_filename(base_filename):
    if not os.path.exists(base_filename):
        return base_filename

    counter = 1
    while True:
        new_filename = f"{os.path.splitext(base_filename)[0]}_{counter}.csv"
        if not os.path.exists(new_filename):
            return new_filename
        counter += 1


# مسیر فایل‌ها
file1 = r'C:\Users\arkit\Desktop\cp\KHG3.csv'
file2 = r'C:\Users\arkit\Desktop\cp\p05.csv'
output_file = r'C:\Users\arkit\Desktop\cp\output.csv'
output_file = get_unique_filename(output_file)  # تعیین نام فایل خروجی با بررسی وجود فایل قبلی

# خواندن فایل دوم و ساخت دیکشنری
data2 = {}
with open(file2, 'r') as f2:
    reader2 = csv.reader(f2)
    header2 = next(reader2)  # هدر فایل دوم
    for row in reader2:
        key = clean_key(row[0])  # پاکسازی ستون کلید فایل دوم
        data2[key] = row  # ذخیره کامل ردیف در دیکشنری فایل دوم

# پردازش فایل اول و اضافه کردن مقادیر فایل دوم
with open(file1, 'r') as f1, open(output_file, 'w', newline='') as out:
    reader1 = csv.reader(f1)
    writer = csv.writer(out)

    header1 = next(reader1)  # هدر فایل اول
    writer.writerow(header1 + header2)  # نوشتن هدر ترکیبی

    # دنبال کردن ردیف‌هایی که در فایل اول آمده‌اند
    matched_keys = set()

    for row in reader1:
        key = clean_key(row[0])  # پاکسازی ستون کلید فایل اول
        if key in data2:
            writer.writerow(row + data2[key][1:])  # ترکیب ردیف‌های دو فایل
            matched_keys.add(key)
        else:
            writer.writerow(row)  # بدون تغییر اگر کلید در فایل دوم نباشد

    # افزودن ردیف‌های اضافی فایل دوم که در فایل اول نبودند
    for key, row in data2.items():
        if key not in matched_keys:
            writer.writerow([''] * len(header1) + row)  # ردیف فایل دوم با ستون‌های خالی برای فایل اول
