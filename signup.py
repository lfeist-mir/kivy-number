from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from mydatabase import Database
from styles import Styles

Builder.load_string("""
#: import CButton custom_widgets
#: import CTextInput custom_widgets

<Signup>:
    name: "signup"
    BoxLayout:
        orientation: "vertical"
        BoxLayout:
            size_hint: 1,0.4
            Image:
                source: "background.png"
        AnchorLayout:
            size_hint: 1, 0.6
            anchor_y: "top"
            BoxLayout:
                orientation:"vertical"
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(10)
                padding: (dp(30),0,dp(30),0)
                Label:
                    font_size: "16sp"
                    halign: 'left'
                    font_name: "robotoblack.ttf"
                    text_size:self.size
                    text: "Create yout account"
                    size_hint_y: None
                    size: self.texture_size
                    color: root.secondary_color
                CTextInput:
                    id: email
                    hint_text: "Email"
                    size_hint_y: None
                    height: dp(50)
                CTextInput:
                    id: password
                    hint_text: "Password"
                    size_hint_y: None
                    height: dp(50)
                CTextInput:
                    id: confirm_password
                    hint_text: "Confirm password"
                    size_hint_y: None
                    height: dp(50)
                CButton:
                    text: "Sign Up"
                    on_press: root.create_entry()
                    size_hint_y: None
                    height: dp(50)    
""")

class Signup(Screen):
    secondary_color = Styles.secondary_color

    def create_entry(self):
        email = self.ids.email.text
        password = self.ids.password.text
        cpassword = self.ids.confirm_password.text

        if password==cpassword and Database.email_valid(email):
            Database.insert_data(email, password)
            self.manager.current = "login"
        else: 
            print('Email already exists')