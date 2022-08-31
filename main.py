#To be able to run this program: 1.Go to Python Packages 2.Search for 'kivy' 3.Install
#flappy bird https://www.youtube.com/watch?v=cGYMZB_peBM&list=PLy5hjmUzdc0mSEN7WxUQ_HlP6X_OdvMlq

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from random import randint
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen



class Check(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

#Player

class Balloon(Image):
    velocity = NumericProperty(0)
    balloon= ObjectProperty()

    def on_touch_down(self, touch):
        self.source = "ballon_high.png"
        self.velocity = 150
        super().on_touch_down(touch)

    def on_touch_up(self, touch):
        self.source = "ballon_low.png"
        #self.velocity = -80
        super().on_touch_up(touch)

#Loose Lives

class Volcano(Image):
    velocity = NumericProperty(0)
    volcano = ObjectProperty()

    def on_touch_down(self, touch):
        self.source = "volcane_high.png"
        self.velocity = 150
        super().on_touch_down(touch)

    def on_touch_up(self, touch):
        self.source = "volcane_low.png"
        #self.velocity = -80
        super().on_touch_up(touch)

class Pines(Image):
    velocity = NumericProperty(0)
    pines= ObjectProperty()

   # def on_touch_down(self, touch):
   #     self.source = "pines.png"
   #     self.velocity = 150
   #     super().on_touch_down(touch)

   # def on_touch_up(self, touch):
   #     self.source = "volcane_low.png"
    #    #self.velocity = -80
    #    super().on_touch_up(touch)

#Win Points
class Purple_cloud(Image):
    #velocity = NumericProperty(0)
    purple_cloud= ObjectProperty()

    def on_touch_down(self, touch):
        self.source = "purple_cloud2.png"
        self.velocity = 150
        super().on_touch_down(touch)

    def on_touch_up(self, touch):
        self.source = "purple_cloud.png"
        #self.velocity = -80
        super().on_touch_up(touch)

class Bor_cloud(Image):
    #velocity = NumericProperty(0)
    bor_cloud= ObjectProperty()

    def on_touch_down(self, touch):
        self.source = "red_cloud2.png"
        self.velocity = 150
        super().on_touch_down(touch)

    def on_touch_up(self, touch):
        self.source = "red_cloud.png"
        #self.velocity = -80
        super().on_touch_up(touch)

class Yell_cloud(Image):
    #velocity = NumericProperty(0)
    yell_cloud= ObjectProperty()

    def on_touch_down(self, touch):
        self.source = "yell_cloud2.png"
        self.velocity = 150
        super().on_touch_down(touch)

    def on_touch_up(self, touch):
        self.source = "yell_cloud.png"
        #self.velocity = -80
        super().on_touch_up(touch)

class Background(Widget):
    grass_texture = ObjectProperty()
  #  pines_texture = ObjectProperty()
    red_texture = ObjectProperty(None)
    clouds_texture = ObjectProperty(None)
    water_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.grass_texture = Image(source="grass.png").texture
        #self.grass_texture = Image(source="pines.png").texture
        self.grass_texture.wrap = "repeat"
        self.grass_texture.uvsize = (Window.width/self.grass_texture.width*2,-1)

   #     self.pines_texture = Image(source="pines.png").texture
       # self.pines_texture.uvsize = (80, 80)
     #   self.pines_texture.wrap = "repeat"
       # self.pines_texture.wrap = ""
   #     self.pines_texture.uvsize = (Window.width/180,-1)

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

  #  def scroll_pines(self, time):
        #pines
  #      self.pines_texture.uvpos = (((self.pines_texture.uvpos[0]+ time/4)%Window.height),(self.pines_texture.uvpos[1]+1))
   #     texture = self.property("pines_texture")
  #      texture.dispatch(self)
  #  pass

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
    #volcano = []
    GRAVITY = 100
    WIND = 10
    score = NumericProperty(0)
    life = NumericProperty(3)

    #def next_frame(self):
     #   Clock.schedule_interval(self.root.ids.background.scroll_grass, 1/60)
      #  Clock.schedule_interval(self.root.ids.background.scroll_pines, 1 / 60)
       # Clock.schedule_interval(self.root.ids.background.scroll_red, 1 / 60)
        #Clock.schedule_interval(self.root.ids.background.scroll_water, 1 / 60)
        #Clock.schedule_interval(self.root.ids.background.scroll_clouds, 1 / 60)

    def move_volcano(self, time):
        volcano = self.root.ids.volcano
        volcano.x = volcano.x - 0.7
        if volcano.x <= -100:
            volcano.x = Window.width+20

    def move_pines(self, time):
        pines = self.root.ids.pines
        pines.x = pines.x - 0.7
        if pines.x <= -100:
            pines.x = Window.width+20

    def move_purple_cloud(self, time):
        purple_cloud = self.root.ids.purple_cloud
        purple_cloud.x = purple_cloud.x - 0.7
        if purple_cloud.x <= -100:
            purple_cloud.x = Window.width+20
            purple_cloud.y = 100 * randint(1,5)

    def move_yell_cloud(self, time):
        yell_cloud = self.root.ids.yell_cloud
        yell_cloud.x = yell_cloud.x - 0.7
        if yell_cloud.x <= -100:
            yell_cloud.x = Window.width+20
            yell_cloud.y = 50* randint(1,10)

    def move_bor_cloud(self, time):
        bor_cloud = self.root.ids.bor_cloud
        bor_cloud.x = bor_cloud.x - 0.7
        if bor_cloud.x <= -100:
            bor_cloud.x = Window.width+20
            bor_cloud.y = 50* randint(1,10)

    def move_balloon(self, time):
    # idea to use the physics approach to the ballon movement taken from: flappy bird https://www.youtube.com/watch?v=cGYMZB_peBM&list=PLy5hjmUzdc0mSEN7WxUQ_HlP6X_OdvMlq

        balloon = self.root.ids.balloon
        grass = self.root.ids.background.grass_texture
        pines = self.root.ids.pines
        volcano = self.root.ids.volcano
        #volcano.x = volcano.x - 0.7

        purple_cloud = self.root.ids.purple_cloud

        yell_cloud = self.root.ids.yell_cloud
        bor_cloud = self.root.ids.bor_cloud
    # purple_cloud.x = purple_cloud.x - 0.7


        if balloon.y > grass.height:
            if balloon.y >= Window.height-70:
                balloon.y = balloon.y - self.GRAVITY * time * 15
            #else:
                #for volcano in self.volcano:
            elif volcano.collide_widget(balloon) or pines.collide_widget(balloon):
                balloon.y = 600 + balloon.velocity * time
                balloon.x = balloon.x +60 + self.WIND * time
                balloon.velocity = balloon.velocity - self.GRAVITY * time

                self.life -= 1
                self.game_over(time)

            elif purple_cloud.collide_widget(balloon):
                balloon.y = balloon.y -20 + balloon.velocity * time
                balloon.x = balloon.x+5 + self.WIND * time
                balloon.velocity = balloon.velocity - self.GRAVITY * time*2
                self.score += 10
                purple_cloud.source ="ten.png"
                purple_cloud.y = 800
                self.move_purple_cloud(time)
            elif yell_cloud.collide_widget(balloon):
                balloon.y = balloon.y -20 + balloon.velocity * time
                balloon.x = balloon.x+5 + self.WIND * time
                balloon.velocity = balloon.velocity - self.GRAVITY * time*2
                self.score += 20
                yell_cloud.y = 800
                self.move_yell_cloud(time)
            elif bor_cloud.collide_widget(balloon):
                balloon.y = balloon.y -20 + balloon.velocity * time
                balloon.x = balloon.x+5 + self.WIND * time
                balloon.velocity = balloon.velocity - self.GRAVITY * time*2
                self.score += 10
                bor_cloud.y = 800
                self.move_bor_cloud(time)
            else:
                balloon.y = balloon.y + balloon.velocity * time
                balloon.x = balloon.x + self.WIND * time
                balloon.velocity = balloon.velocity - self.GRAVITY * time

        elif balloon.y <= grass.height:

            self.score += 20
            balloon.y = 200
            balloon.x = 200
            balloon.velocity = 0
            balloon.source = ""
            self.frames.cancel()
            pass


    def game_over(self, time):
        balloon = self.root.ids.balloon
        if self.life == 0:
            balloon.source = "heart.png"
            balloon.y = balloon.y + balloon.velocity * time/2
            balloon.x = balloon.x
            balloon.velocity = 0
            if balloon.y <= 200:
                self.frames.cancel()
           # self.end()
        #self.check_collision(time)
  #  def end(self):
   #     self.frames.cancel()

   # def score(self, balloon):
#

    #def won(self, time):
      #  balloon = self.root.ids.balloon
       # volcano = self.root.ids.volcano
    #ask user for a name and save the score
     #   self.score -= 10
      #  save_score = input("Do you want to save your score? Y/N")
       # if save_score =="Y" or save_score == "y":
        #    name = input("Player name:")


    def on_start(self):
        Clock.schedule_interval(self.root.ids.background.scroll_grass, 1/60)
        #Clock.schedule_interval(self.root.ids.background.scroll_pines, 1 / 60)
        Clock.schedule_interval(self.root.ids.background.scroll_red, 1 / 60)
        Clock.schedule_interval(self.root.ids.background.scroll_water, 1 / 60)
        Clock.schedule_interval(self.root.ids.background.scroll_clouds, 1 / 60)

    def next_frame(self,time_passed):
        self.move_balloon(time_passed)
        self.move_volcano(time_passed)
        self.move_pines(time_passed)
        self.move_purple_cloud(time_passed)
        self.move_yell_cloud(time_passed)
        self.move_bor_cloud(time_passed)


    def start(self):
        self.frames = Clock.schedule_interval(self.next_frame, 1/60.)

        #num_volcanos = 3
        #space_btw_volcanos = Window.width/ (num_volcanos -1)
        #for i in range(num_volcanos):
         #   volcano = Volcano()
          #  volcano.size_hint=(None,None)
           # volcano.pos =(Window.width + i * space_btw_volcanos,70)
            #volcano.size = (616/2,325/2)
            #volcano.source = "volcane_low.png"

            #self.volcano.append(volcano)
            #self.root.add_widget(volcano)

        #def move_volcano(self, time_passed):
         #   for volcano in self.volcanos:
          #      volcano.x -= time_passed * 100

           # volcano_xs = list(map(lambda volcano: volcano.x, self.volcanos))
            #right_most_x = max(volcano.xs)
            #if right_most_x <= Window.width - space_btw_volcanos:
             #   most_left_volcano = self.volcanos[volcano_xs.index(min(volcano_xs))]
              #  most_left_volcano = Window.width

    pass

MainApp().run()



