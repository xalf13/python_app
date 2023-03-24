from kivy.lang import Builder
from kivy.uix.image import AsyncImage
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.button import MDIconButton

KV = '''
<ClickableTextFieldRound>:
    size_hint_y: None
    height: text_field.height + login_field.height + dp(10)

    MDTextField:
        id: login_field
        hint_text: root.hint_text_login
        text: root.text_login
        icon_left: "account"
        max_text_length: 5
        input_filter: 'int'
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {"center_x": .5, "top": 1}

    MDTextField:
        id: text_field
        hint_text: root.hint_text
        text: root.text
        password: True
        icon_left: "key-variant"
        size_hint_y: None
        height: self.minimum_height
        pos_hint: {"center_x": .5, "top": 0.6}

    MDIconButton:
        icon: "eye-off"
        pos_hint: {"center_y": .4}
        pos: text_field.width - self.width + dp(8), 0
        theme_text_color: "Hint"
        on_release:
            self.icon = "eye" if self.icon == "eye-off" else "eye-off"
            text_field.password = False if text_field.password is True else True

    MDRoundFlatButton:
        id: auth_button
        text: "Авторизоваться"
        size_hint: None, None
        size: "150dp", "50dp"
        theme_text_color: "Custom"
        text_color: "black"
        line_color: "black"
        pos_hint: {"center_x": .5, "top": 0.1}
        on_press: root.do_login()

    AsyncImage:
        source: "C:/Users/12018/Desktop/kivy/res/log_patp.png"  
        size_hint: None, None
        size: dp(200), dp(200)
        pos_hint: {"center_x": .5, "center_y": 2.0}


MDScreen:

    ClickableTextFieldRound:
        size_hint_x: None
        width: "200dp"
        hint_text_login: "Логин"
        hint_text: "Пароль"
        pos_hint: {"center_x": .5, "center_y": .5}
'''

#lol
class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    text_login = StringProperty()
    hint_text = StringProperty()
    hint_text_login = StringProperty()
    # Here specify the required parameters for MDTextFieldRound:
    # [...]
    def do_login(self):
        print('Hello')
        pass


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()
