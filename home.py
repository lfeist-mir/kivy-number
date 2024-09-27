from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
import http.client
import certifi
from mydatabase import Database
from login import Login

from styles import Styles

Builder.load_string("""
#: import CButton custom_widgets
#: import CTextInput custom_widgets

<Home>:
    name: "home"
    FloatLayout:
        Image:
            id: bg_image
            source: "background.png"
            fit_mode: 'contain'
            pos_hint: {"center_x":0.5, "top":1.1}
        BoxLayout:
            orientation: "vertical"
            BoxLayout:
                canvas.before:
                    Color: 
                        rgba: root.bg_color
                    Rectangle:
                        pos: self.pos
                        size: self.size
                size_hint_y: None
                height: dp(60)
                Label:
                    text:"Interesting Fact"
                    font_name: "robotoblack.ttf"
                    font_size: '20sp'
                AnchorLayout:
                    anchor_x: "right"
                    padding: [0,0,dp(30),0]
                    Button:
                        canvas.before:
                            Rectangle:
                                pos:self.pos
                                size: self.size
                                source: 'history.png'
                        size_hint: None, None
                        size: dp(35), dp(35)
                        background_normal: ''
                        background_color: 0,0,0,0
                        on_press: root.switch_to_history()
            BoxLayout:
                Label:
                    id: fact
                    color: 0,0,0,1
                    text_size: self.width, None
                    padding: [dp(20),dp(20)]
            AnchorLayout:
                anchor_x: "center"
                anchor_y: "center"
                size_hint: 1,0.3
                
                BoxLayout:
                    orientation:'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(30)
                    spacing: dp(10)
                    BoxLayout:
                        size_hint: 1,0.65
                        spacing: dp(10)
                        BoxLayout:
                            orientation: "vertical"
                            spacing: dp(10)
                            Label:
                                font_size: "18sp"
                                halign: 'left'
                                font_name: "robotomedium.ttf"
                                text_size:self.size
                                text: "Day"
                                color: root.secondary_color
                                size_hint_y: None
                                size: self.texture_size
                            CTextInput:
                                id: day_input
                                size_hint_y: None
                                height: dp(50)
                        BoxLayout:
                            orientation: "vertical"
                            spacing: dp(10)
                            Label:
                                font_size: "18sp"
                                halign: 'left'
                                font_name: "robotomedium.ttf"
                                text_size:self.size
                                text: "Month"
                                color: root.secondary_color
                                size_hint_y: None
                                size: self.texture_size
                            CTextInput:
                                id: month_input
                                size_hint_y: None
                                height: dp(50)
                    CButton:
                        text:"Display Fact"
                        size_hint_y: None
                        height: dp(60)
                        font_name: 'robotomedium.ttf'
                        font_size: '18sp'
                        on_press: root.get_fact()
""")

class Home(Screen):
    bg_color = Styles.primary_color
    secondary_color = Styles.secondary_color

    def switch_to_history(self):
        self.manager.current = "history"

    def get_fact(self):

        day = int(self.ids.day_input.text)
        month = int(self.ids.month_input.text)

        conn = http.client.HTTPSConnection("numbersapi.p.rapidapi.com")

        headers = {
            'x-rapidapi-key': "4366b9d043mshf36cde2591eb1f0p1d3b69jsn95cc737b2136",
            'x-rapidapi-host': "numbersapi.p.rapidapi.com"
        }

        conn.request(
            "GET", 
            f"/{month}/{day}/date", 
            headers=headers
        )

        res = conn.getresponse()
        data = res.read()

        fact = data.decode("utf-8")

        Database.insert_fact(Login.get_email(), fact)

        self.ids.bg_image.color=(1,1,1,0.3)
        self.ids.fact.text = fact
