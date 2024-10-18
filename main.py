from views.main_view import MainApp
import sys
import os

# اضافه کردن پوشه پروژه به مسیر پایتون
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    MainApp().run()

