#To be able to run this program: 1.Go to Python Packages 2.Search for 'kivy' 3.Install
#flappy bird https://www.youtube.com/watch?v=cGYMZB_peBM&list=PLy5hjmUzdc0mSEN7WxUQ_HlP6X_OdvMlq

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.core.window import Window
from random import randint
from kivy.properties import NumericProperty

class Check(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

#class Red_pines(Image):
    #velocity = NumericProperty(0)
#    def on_touch_down(self, touch):
  #      self.source = "red_pines.png"
        #self.velocity= 150

class Balloon(Image):
    #velocity = NumericProperty(0)
    balloon= ObjectProperty()

    def on_touch_down(self, touch):
        self.source = "ballon_high.png"
        self.velocity = 150
        super().on_touch_down(touch)

    def on_touch_up(self, touch):
        self.source = "ballon_low.png"
        #self.velocity = -80
        super().on_touch_up(touch)

class Volcano(Image):
    #velocity = NumericProperty(0)
    volcano= ObjectProperty()

    def on_touch_down(self, touch):
        self.source = "volcane_high.png"
        self.velocity = 150
        super().on_touch_down(touch)

    def on_touch_up(self, touch):
        self.source = "volcane_low.png"
        #self.velocity = -80
        super().on_touch_up(touch)

class Background(Widget):
    grass_texture = ObjectProperty()
    pines_texture = ObjectProperty()
    red_texture = ObjectProperty(None)
    clouds_texture = ObjectProperty(None)
    water_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.grass_texture = Image(source="grass.png").texture
        #self.grass_texture = Image(source="pines.png").texture
        self.grass_texture.wrap = "repeat"
        self.grass_texture.uvsize = (Window.width/self.grass_texture.width*2,-2)

        self.pines_texture = Image(source="pines.png").texture
       # self.pines_texture.uvsize = (80, 80)
        self.pines_texture.wrap = "repeat"
       # self.pines_texture.wrap = ""
        self.pines_texture.uvsize = (Window.width/180,-1)

        self.red_texture = Image(source="red.png").texture
        self.red_texture.wrap ="repeat"
        self.red_texture.uvsize = (Window.width/300,-1)

        self.water_texture = Image(source="water.png").texture
        self.water_texture.wrap = "repeat"
        self.water_texture.uvsize = (Window.width/180,-1)

        self.clouds_texture = Image(source="clouds.png").texture
        self.clouds_texture.wrap = "repeat"
        self.clouds_texture.uvsize = (Window.width / self.clouds_texture.width*4, -4)

    def scroll_grass(self, time):

        self.grass_texture.uvpos = (((self.grass_texture.uvpos[0]+ time)%Window.height),(self.grass_texture.uvpos[1]+1))
        texture = self.property("grass_texture")
        #texture = self.property("pines_texture")
        texture.dispatch(self)
    pass

    def scroll_pines(self, time):
        #pines
        self.pines_texture.uvpos = (((self.pines_texture.uvpos[0]+ time/4)%Window.height),(self.pines_texture.uvpos[1]+1))
        texture = self.property("pines_texture")
        texture.dispatch(self)
    pass

    def scroll_red(self, time):
        #pines
        self.red_texture.uvpos = (((self.red_texture.uvpos[0]+ time/10)%Window.height),(self.red_texture.uvpos[1]+1))
        texture = self.property("red_texture")
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
        self.clouds_texture.uvpos = (((self.clouds_texture.uvpos[0]+ time/10)%Window.height),(self.clouds_texture.uvpos[1]))
        texture = self.property("clouds_texture")
        texture.dispatch(self)
    pass


from kivy.clock import Clock

class MainApp(App):
    GRAVITY = 100
    WIND = 10
    score = NumericProperty(3)

    def on_start(self):
        Clock.schedule_interval(self.root.ids.background.scroll_grass, 1/60)
        Clock.schedule_interval(self.root.ids.background.scroll_pines, 1 / 60)
        Clock.schedule_interval(self.root.ids.background.scroll_red, 1 / 60)
        Clock.schedule_interval(self.root.ids.background.scroll_water, 1 / 60)
        Clock.schedule_interval(self.root.ids.background.scroll_clouds, 1 / 60)

    
    def move_balloon(self, time):
    # idea to use the physics approach to the ballon movement taken from: flappy bird https://www.youtube.com/watch?v=cGYMZB_peBM&list=PLy5hjmUzdc0mSEN7WxUQ_HlP6X_OdvMlq

        balloon = self.root.ids.balloon

        grass = self.root.ids.background.grass_texture

        if balloon.y > grass.height:
            if balloon.y >= Window.height-70:
                balloon.y = balloon.y - self.GRAVITY * time * 15
            else:
                balloon.y = balloon.y + balloon.velocity * time
                balloon.x = balloon.x + self.WIND * time
                balloon.velocity = balloon.velocity - self.GRAVITY * time

        volcano = self.root.ids.volcano
        volcano.x = volcano.x - 0.7
        self.check_collision()

   # def score(self, balloon):
#

    def check_collision(self):
        balloon = self.root.ids.balloon
        volcano = self.root.ids.volcano

        if volcano.collide_widget(balloon):
            self.game_over()

    def game_over(self):

        balloon = self.root.ids.balloon
        balloon.y = balloon.y + 100
        balloon.x = balloon.x + 0
        #self.root.ids.balloon.source = ""
        self.score -= 1



#
#            elif  volcane.y <= balloon.y <= 325/2 and volcane.x <=balloon.x<=612/2:

#                balloon.y = balloon.y
#                balloon.x = balloon.x

#            else:
#                balloon.y = balloon.y + balloon.velocity * time
#                balloon.x = balloon.x + self.WIND * time
 #               balloon.velocity = balloon.velocity - self.GRAVITY * time


    def start(self):
        Clock.schedule_interval(self.move_balloon, 1/60.)
    pass

MainApp().run()



