from flask import Flask
import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)


def run_flask_app():
    app.run(debug=True, port=5000)


def test_form_input(live_server_url):
    driver = webdriver.Chrome()
    driver.get(live_server_url)
    email = driver.find_element(By.CLASS_NAME, 'email-input')
    email.send_keys("elizabethbooth05@gmail.com")
    password = driver.find_element(By.CLASS_NAME, 'password-input')
    password.send_keys("123")
    display_name = driver.find_element(By.CLASS_NAME, 'display-name-input')
    display_name.send_keys("BoothGG")
    submit = driver.find_element(By.CLASS_NAME, 'submit-button')
    submit.click()
    print("Form submitted")


if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.daemon = True
    flask_thread.start()

    time.sleep(2)  # Give Flask some time to start

    with app.test_request_context():
        live_server_url = 'http://127.0.0.1:5000/'
        print(f"Flask Live Server URL: {live_server_url}")

        """
        Testing the about me button and the blog button.
        """
        try:
            driver = webdriver.Chrome()
            driver.get(live_server_url)
            about_me_button = driver.find_element(
                By.CLASS_NAME, 'about-me-link')
            blog_buttom = driver.find_element(By.CLASS_NAME, 'empathy')
            print("Testing blog button")
            about_me_button.click()
            print("Testing about button")
        except:
            print("Could not start webdriver.")

        live_server_url = 'http://127.0.0.1:5000/empathy'
        test_form_input(live_server_url)
        live_server_url = 'http://127.0.0.1:5000/'
        test_form_input(live_server_url)
