#To be able to run this program: 1.Go to Python Packages 2.Search for 'kivy' 3.Install
#flappy bird https://www.youtube.com/watch?v=cGYMZB_peBM&list=PLy5hjmUzdc0mSEN7WxUQ_HlP6X_OdvMlq

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.core.window import Window
from random import randint
from kivy.properties import NumericProperty


class Pines(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Ballon(Image):
    velocity = NumericProperty(0)
    def on_touch_down(self, touch):
        self.source = "ballon_high.png"
        self.velocity = 150
        super().on_touch_down(touch)

    def on_touch_up(self, touch):
        self.source = "ballon_low.png"
        #self.velocity = -80
        super().on_touch_up(touch)

class Background(Widget):
    grass_texture= ObjectProperty(None)
    pines_texture = ObjectProperty(None)
    clouds_texture = ObjectProperty(None)
    water_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.grass_texture = Image(source="grass.png").texture
        self.grass_texture.wrap = "repeat"
        self.grass_texture.uvsize = (Window.width/self.grass_texture.width,-2)

        self.pines_texture = Image(source="pines.png").texture
        self.pines_texture.wrap = "repeat"
        self.pines_texture.uvsize = (Window.width/180,-1)

        self.water_texture = Image(source="water.png").texture
        self.water_texture.wrap = "repeat"
        self.water_texture.uvsize = (Window.width/180,-1)

        self.clouds_texture = Image(source="clouds.png").texture
        self.clouds_texture.wrap = "repeat"
        self.clouds_texture.uvsize = (Window.width / (self.clouds_texture.width), -1)

    def scroll_grass(self, time):
        #grass
        self.grass_texture.uvpos = (((self.grass_texture.uvpos[0]+ time)%Window.height),(self.grass_texture.uvpos[1]+1))
        texture = self.property("grass_texture")
        texture.dispatch(self)
    pass

    def scroll_pines(self, time):
        #pines
        self.pines_texture.uvpos = (((self.pines_texture.uvpos[0]+ time/6)%Window.height),(self.pines_texture.uvpos[1]+1))
        texture = self.property("pines_texture")
        texture.dispatch(self)
    pass

    def scroll_water(self, time):
        #water
        self.water_texture.uvpos = (((self.water_texture.uvpos[0]+ time/6)%Window.height),(self.water_texture.uvpos[1]+1))
        texture = self.property("water_texture")
        texture.dispatch(self)
    pass

    def scroll_clouds(self, time):
        #clouds
        self.clouds_texture.uvpos = (((self.clouds_texture.uvpos[0]+ time/6)%Window.height),(self.clouds_texture.uvpos[1]))
        texture = self.property("clouds_texture")
        texture.dispatch(self)
    pass

from kivy.clock import Clock

class MainApp(App):
    GRAVITY = 100

    def collides(rect1, rect2):
        r1x = rect1[0][0]
        r1y = rect1[0][1]
        r2x = rect2[0][0]
        r2y = rect2[0][1]
        r1w = rect1[1][0]
        r1h = rect1[1][1]
        r2w = rect2[1][0]
        r2h = rect2[1][1]

        if (r1x < r2x + r2w and r1x +r1w >r2x and r1y < r2y + r2h and r1y + r1h > r2y):
            return True
        else:
            return False

    def on_start(self):
        Clock.schedule_interval(self.root.ids.background.scroll_grass, 1/60)
        Clock.schedule_interval(self.root.ids.background.scroll_pines, 1 / 60)
        Clock.schedule_interval(self.root.ids.background.scroll_water, 1 / 60)
        Clock.schedule_interval(self.root.ids.background.scroll_clouds, 1 / 60)

    
    def move_ballon(self, time):
        ballon= self.root.ids.ballon
        ballon.y = ballon.y + ballon.velocity * time
        ballon.velocity = ballon.velocity - self.GRAVITY * time

    def start(self):
        Clock.schedule_interval(self.move_ballon, 1/60.)
    pass

MainApp().run()

       #step = self.root.ids.step
        ### formula from https://www.youtube.com/watch?v=2dn_ohAqkus min 15:29
      #  if self.collides((tb), (Background.step_texture)):
       #     print("collide")
        #else:
         #   print("not")
       # if tb.collide_widget(step):
       #    tb.velocity = 0
       # else:
        #    tb.y = tb.y + tb.velocity * time
        #    tb.velocity = tb.velocity - self.GRAVITY * time

    #    self.if_collision()

   # def if_collision(self):
       # tb = self.root.ids.tb
       # step = self.root.ids.step
        #print('kkkk')
        #if tb.collide_widget(step):
         #   tb.velocity = 0
        #else:
         #   self.move_tb()

    #def stop(self):
     #   tb= self.root.ids.tb
        ### formula from https://www.youtube.com/watch?v=2dn_ohAqkus min 15:29
        #tb.y = tb.y

#from https://www.youtube.com/watch?v=21tpqcO86Ko 5.21

