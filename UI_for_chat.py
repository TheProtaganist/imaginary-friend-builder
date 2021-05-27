from kivy.core.audio import SoundLoader
from kivymd.app import MDApp
from kivy.utils import get_color_from_hex as hex8
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder as Render

Window.size = (700, 800)
sound = SoundLoader.load("sound.wav")


class Screen4u(MDScreen):

    def __init__(self, **kwargs):
        super(MDRaisedButton).__init__(**kwargs)
        super().__init__(**kwargs)
        self.Box = MDBoxLayout()
        self.count = 0
        self.count_the_length = 0
        self.screen = MDGridLayout(
            cols=1,
            rows=2,
            md_bg_color=hex8("#00ffff"),
            size_hint=[1, 1])

        self.size = [1, 1]

        self.Scroll = ScrollView()
        self.Scroll.scroll_type = ["content", "bars"]
        self.Scroll.bar_color = hex8("#000000")
        self.Scroll.bar_width = "5dp"
        self.text = TextInput(
            font_name="Default.ttf",
            size_hint=[1, 1],
            font_size=23,
            multiline=False)

        self.button = MDRaisedButton(
            size_hint=[0.124, 0.124],
            font_name="Arial",
            on_press=lambda message:self.send_it(self.text.text))
        self.button.md_bg_color = hex8("#ff00ff")
        self.button.text = "send"
        self.button.text_color = hex8("#000000")

        self.Top = MDGridLayout(
            cols=2,
            rows=1,
            md_bg_color=hex8("#00ffff"),
            size_hint_x=1,
            size_hint_y=1,
            minimum_height=20)

        self.Container = MDBoxLayout(
            md_bg_color=hex8("#00ffff"),
            orientation="vertical",
            width=self.screen.width,
            height=self.screen.height)

        self.Bot = MDBoxLayout(
            md_bg_color=hex8("##00ffff"),
            orientation="vertical",
            width=self.screen.width,
            height=self.screen.height)

        self.bottom = MDGridLayout(
            cols=2,
            rows=1,
            md_bg_color=hex8("#00ffff"),
            width=200,
            height=200,
            size_hint=[.07, .07])

        self.bottom.add_widget(self.text)
        self.bottom.add_widget(self.button)
        self.Top.add_widget(self.Container)
        self.Top.add_widget(self.Bot)
        self.Scroll.size = [self.screen.width, self.screen.height]
        self.Scroll.add_widget(self.Top)
        self.screen.add_widget(self.Scroll)
        self.screen.add_widget(self.bottom)
        self.add_widget(self.screen)

        position = self.Top.get_top()
        x = self.Top.get_right()
        print(x, position)

    def send_it(self, message):
        test = str(input("Enter anything: "))
        self.count += 1
        text_msg = MDLabel()
        text_msg.color = hex8("#000000")
        text_msg.text = message
        text_msg.pos_hint = [0.5, 0.5]
        text_msg.halign = "center"
        msg = MDFillRoundFlatButton()
        msg.md_bg_color = hex8("#ffff00")
        msg.size_hint_x = 1
        msg.height = 243
        msg.padding = "3dp"
        msg.add_widget(text_msg)
        emp = Widget()
        emp.size_hint_x = 1
        emp.height = 0.5
        sound.play()
        if self.count >= 1:
            print(self.count)
            self.Container.add_widget(msg)
            self.Container.add_widget(emp)
        if test == "password":
            self.response()
        return self.count

    def response(self):
        incoming_text = MDLabel()
        incoming_text.color = hex8("#000000")
        incoming_text.text = "Hello World!"
        incoming_text.halign = "center"
        incoming_text.pos_hint = [0.5, 0.5]
        incoming = MDFillRoundFlatButton()
        incoming.md_bg_color = hex8("#ffff00")
        incoming.size_hint_x = 1
        incoming.height = 243
        incoming.padding = "3dp"
        incoming.add_widget(incoming_text)
        emp2 = Widget()
        emp2.size_hint_x = 1
        emp2.height = 0.5
        self.Top.size_hint_y = len(range(self.count))
        self.Bot.add_widget(emp2)
        self.Bot.add_widget(incoming)
        self.Scroll.scroll_to(incoming)
        sound.play()


class Text_for_UI(MDApp):

    def build(self):
        self.icon = "Scooter.png"
        self.title = "Scooter The Loyal Friend"
        root = Render.load_file("text_for_ui.kv")
        return Screen4u()


if __name__ == "__main__":
    Text_for_UI().run()
