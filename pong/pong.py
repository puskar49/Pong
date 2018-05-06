from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint


class PongGame(Widget):
    ball = ObjectProperty(None)

    def on_touch_down(self, touch):
        print("touchdown: {}".format(touch))

    def on_touch_move(self, touch):
        print("touchmove: {}".format(touch))

    def on_touch_up(self, touch):
        print("touchup: {}".format(touch))

    def serve_ball(self):
        self.ball.center = self.center
        #vs = [22.5, 112.5, 202.5, 292.5]
        vs = [45, 135, 225, 315]
        self.ball.velocity = Vector(10, 0).rotate(vs[randint(0, 4)])

    def update(self, dt):
        self.ball.move()

        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.vy *= -1

        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.vx *= -1


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == "__main__":
    PongApp().run()
