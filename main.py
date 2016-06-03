import random

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty)
from kivy.clock import Clock
from kivy.vector import Vector


class ScrollerGame(Widget):
    player = ObjectProperty(None)
    tree1 = ObjectProperty(None)
    tree2 = ObjectProperty(None)
    tree3 = ObjectProperty(None)

    def update(self, dt):
        self.player.move(dt)
        self.tree1.scroll(self.player.velocity_x)
        self.tree2.scroll(self.player.velocity_x)
        self.tree3.scroll(self.player.velocity_x)

    def on_touch_down(self, touch):
        if touch.x > self.player.center_x:
            self.player.velocity_x = 2

    def on_touch_up(self, touch):
        self.player.velocity_x = 0


class RectangleMan(Widget):
    MAX_VELOCITY_X = 10
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self, dt):
        if self.velocity_x > 0:
            self.velocity_x += 2 * dt
        if self.velocity_x > self.MAX_VELOCITY_X:
            self.velocity_x = self.MAX_VELOCITY_X
        # Track our velocity but don't actually move the player sprite
        #self.pos = Vector(*self.velocity) + self.pos


class RectangleTree(Widget):
    def scroll(self, scroll_dist):
        if self.pos[0] > 0:
            self.pos = Vector(-1 * scroll_dist, 0) + self.pos
        else:
            self.pos = Vector(
                self.parent.width + random.randint(0, self.parent.width), 0)


class ScrollerApp(App):
    def build(self):
        game = ScrollerGame()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    ScrollerApp().run()
