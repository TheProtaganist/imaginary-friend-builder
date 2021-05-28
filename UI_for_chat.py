from Scooter import Bot_Response
from kivy.core.audio import SoundLoader
from kivymd.app import MDApp
from kivy.utils import get_color_from_hex as hex8
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout

Window.size = (700, 800)
sound = SoundLoader.load("sound.wav")

num_list = range(144**3)
listings = []
constant = 1
for i in num_list:
    listings.append(i)


class Screen4u(MDScreen, Image):

    def __init__(self, **kwargs):
        super(MDRaisedButton).__init__(**kwargs)
        super().__init__(**kwargs)
        self.i = Image()
        self.incoming = MDFillRoundFlatButton()
        self.msg = MDFillRoundFlatButton()
        self.incoming_text = MDLabel()
        self.text_msg = MDLabel()
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

    def send_it(self, message):
        self.count += 1
        br = Bot_Response()
        text = f"{self.text.text}"
        abc = br.respond(text)
        self.text_msg.color = hex8("#000000")
        self.text_msg.text = message
        self.text_msg.pos_hint = [0.5, 0.5]
        self.text_msg.halign = "center"
        self.text_msg.valign = "middle"
        self.text_msg.font_size = "17dp" if len(self.text.text) < 14 else '10dp'
        self.text_msg.texture_update()
        self.text_msg.text_size = self.width, None
        self.texture = self.text_msg.texture
        self.msg.md_bg_color = hex8("#ffff00")
        self.msg.size_hint_x = 1
        self.msg.height = 243
        self.msg.padding = "3dp"
        self.msg.add_widget(self.text_msg)
        emp = Widget()
        emp.size_hint_x = 1
        emp.height = 0.5
        sound.play()
        if self.count >= 1:
            print(self.count)
            self.Container.add_widget(self.msg)
            self.Container.add_widget(emp)
            self.response(abc)
        return self.count

    def response(self, query):
        self.incoming_text.color = hex8("#000000")
        self.incoming_text.text = query
        self. incoming_text.halign = "center"
        self.incoming_text.valign = "middle"
        self.incoming_text.pos_hint = [0.5, 0.5]
        self.incoming_text.font_size = "17dp" if len(self.text.text) < 14 else '10dp'
        self.incoming_text.texture_update()
        self.incoming_text.text_size = self.width, None
        self.texture = self.incoming_text.texture
        self.incoming.md_bg_color = hex8("#ffff00")
        self.incoming.size_hint_x = 1
        self.incoming.height = 243
        self.incoming.padding = "3dp"
        self.incoming.add_widget(self.incoming_text)
        emp2 = Widget()
        emp2.size_hint_x = 1
        emp2.height = 0.5
        self.Top.size_hint_y = len(range(self.count))
        self.Bot.add_widget(emp2)
        self.Bot.add_widget(self.incoming)
        self.Container.height = self.text_msg.size_hint_y
        self.Bot.width = self.incoming_text.size_hint_y
        self.Scroll.scroll_to(self.incoming)
        sound.play()


class Text_for_UI(MDApp):

    def build(self):
        self.icon = "Scooter.png"
        self.title = "Scooter The Loyal Friend"
        return Screen4u()


if __name__ == "__main__":
    Text_for_UI().run()
