from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from mydatabase import Database
from styles import Styles

Builder.load_string("""
#: import CButton custom_widgets
#: import CTextInput custom_widgets
#: import SignupText custom_widgets
            
<Login>:
    name: "login"
    BoxLayout:
        orientation: "vertical"
        BoxLayout:
            size_hint: 1, 0.35
            Image:
                source: "background.png"
        AnchorLayout:
            size_hint: 1, 0.55
            anchor_y: "top"
            BoxLayout:
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(10)
                padding: (dp(30),0,dp(30),0)
                Label:
                    text: "Login to your account"
                    font_size: "16sp"
                    halign: 'left'
                    font_name: "robotoblack.ttf"
                    text_size:self.size
                    size_hint_y: None
                    size: self.texture_size
                    color: root.secondary_color
                CTextInput:
                    id: email
                    size_hint_y: None
                    height: dp(50)
                    multiline: False
                    hint_text: "Email"
                CTextInput:
                    id: password
                    size_hint_y: None
                    height: dp(50)
                    multiline: False
                    hint_text: "Password"
                CButton:
                    text: "Login"
                    size_hint_y: None
                    height: dp(50)
                    on_press: root.login()
        AnchorLayout:
            size_hint: 1, 0.1
            anchor_x: "center"
            BoxLayout:
                size_hint_x: None
                width: self.minimum_width
                Label:
                    color: root.secondary_color
                    text: "Don't have an account? "
                    size_hint_x: None
                    size: self.texture_size
                SignupText:
                    text: "Signup"
                    size_hint_x: None
                    size: self.texture_size
                    on_press: root.switch_to_signup()
""")


class Login(Screen):
    email = None
    secondary_color = Styles.secondary_color

    @staticmethod
    def get_email():
        return Login.email

    def switch_to_signup(self):
        self.manager.current = "signup"

    def login(self):
        Login.email = self.ids.email.text
        password = self.ids.password.text

        if Database.user_exists(Login.email,password):
            print("Login successful")
            self.manager.current = 'home'
        else:
            print("Login failed")