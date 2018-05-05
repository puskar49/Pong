from kivy.app import App
from kivy.uix.widget import Widget


class PongWidget(Widget):
    pass


class PongApp(App):
    def build(self):
        return PongWidget()


if __name__ == "__main__":
    PongApp().run()
