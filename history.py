from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from styles import Styles
from mydatabase import Database
from login import Login

Builder.load_string("""
<History>:    
    name: "history"
    BoxLayout:
        orientation: 'vertical'
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
                text:"History"
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
                            source: 'back.png'
                    size_hint: None, None
                    size: dp(35), dp(35)
                    background_normal: ''
                    background_color: 0,0,0,0
                    on_press: root.switch_to_home()
        BoxLayout:
            ScrollView:
                do_scroll_y : True
                Label:
                    id: history_label
                    color: root.secondary_color
                    size_hint_y:None
                    height: self.texture_size[1]
                    text_size: self.width, None
                    padding: [dp(20),dp(20)]
""")

class History(Screen):
    bg_color = Styles.primary_color
    secondary_color = Styles.secondary_color

    def on_pre_enter(self, *args):
        facts = Database.retrieve_facts(Login.get_email())
        if facts:
            label_text= '\n\n'.join(['* '+fact[0] for fact in facts])
            self.ids.history_label.text = label_text
        else:
            self.ids.history_label.text = 'No history'

        return super().on_pre_enter(*args)

    def switch_to_home(self):
        self.manager.current = 'home'