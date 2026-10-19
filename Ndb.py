import random
import os

# مسیر دقیق فایل DB.txt کنار همین برنامه
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, "DB.txt")

choices = ["سنگ", "کاغذ", "قیچی"]


def save_result(result):
    try:
        with open(DB_FILE, "a", encoding="utf-8") as database:
            database.write(result + "\n")
            database.flush()

        print("نتیجه با موفقیت ذخیره شد.")
        print("مسیر فایل:", DB_FILE)

    except OSError as error:
        print("خطا در ذخیره نتیجه:", error)


def show_history():
    if not os.path.exists(DB_FILE):
        print("فایل DB.txt هنوز وجود ندارد.")
        return

    try:
        with open(DB_FILE, "r", encoding="utf-8") as database:
            history = database.readlines()

        if not history:
            print("هنوز سابقه‌ای ثبت نشده است.")
            return

        print("\n--- سابقه بازی‌ها ---")
        for item in history:
            print(item.strip())

    except OSError as error:
        print("خطا در خواندن سابقه:", error)


def play_game():
    user_choice = input(
        "\nانتخاب کن (سنگ / کاغذ / قیچی): "
    ).strip()

    if user_choice not in choices:
        print("انتخاب نامعتبر است! سنگ، کاغذ یا قیچی وارد کن.")
        return

    computer_choice = random.choice(choices)

    print("انتخاب تو:", user_choice)
    print("انتخاب کامپیوتر:", computer_choice)

    if user_choice == computer_choice:
        result = "مساوی"
    elif (
        (user_choice == "سنگ" and computer_choice == "قیچی")
        or (user_choice == "کاغذ" and computer_choice == "سنگ")
        or (user_choice == "قیچی" and computer_choice == "کاغذ")
    ):
        result = "برد کاربر"
    else:
        result = "برد کامپیوتر"

    print("نتیجه:", result)

    record = (
        f"کاربر: {user_choice} | "
        f"کامپیوتر: {computer_choice} | "
        f"نتیجه: {result}"
    )

    save_result(record)


def main():
    while True:
        print("\n===== بازی سنگ، کاغذ، قیچی =====")
        print("1. شروع بازی")
        print("2. مشاهده سابقه بازی‌ها")
        print("3. خروج")

        menu = input("شماره گزینه را وارد کن: ").strip()

        if menu == "1":
            play_game()
        elif menu == "2":
            show_history()
        elif menu == "3":
            print("خدانگهدار!")
            break
        else:
            print("گزینه نامعتبر است!")
if __name__ == "__main__":
    main()

