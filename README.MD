# CSV Merger for MDR and Project Control Files

این پروژه به منظور هماهنگ‌سازی و ترکیب داده‌ها از دو فایل CSV طراحی شده است. 
فایل اول شامل اطلاعات MDR (Master Document Register) تجهیزات و فایل دوم 
شامل اطلاعات کنترل پروژه برای تجهیزات است. با استفاده از این کد، می‌توانید 
ردیف‌های مشترک را شناسایی کرده و اطلاعات را به صورت خودکار ترکیب کنید.

## ویژگی‌ها

- خواندن دو فایل CSV
- تطابق داده‌ها بر اساس کلید (ستون اول)
- اضافه کردن اطلاعات فایل دوم به فایل اول
- مدیریت نام فایل خروجی با اضافه کردن شماره در صورت وجود نام مشابه
- اضافه کردن ستون کلید فایل دوم در خروجی

## نیازمندی‌ها

- Python 3.x
- ماژول‌های `csv` و `re` (به صورت پیش‌فرض در Python موجود هستند)

## نصب

1. این مخزن را کلون کنید یا فایل‌های پروژه را دانلود کنید.
2. اطمینان حاصل کنید که Python 3.x بر روی سیستم شما نصب شده باشد.
3. فایل‌های CSV مربوط به MDR و کنترل پروژه را در مسیر مناسب قرار دهید.

## نحوه استفاده

1. **مسیرهای فایل‌های CSV را در کد تنظیم کنید**:  
   در فایل `merge_csv.py`، خطوط زیر را با مسیرهای فایل‌های خود به‌روز کنید:
   ```python
   file1 = r'path_to_your_mdr_file.csv'
   file2 = r'path_to_your_project_control_file.csv'
   output_file = r'path_to_your_output_file.csv'