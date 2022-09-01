#To be able to run this program: 1.Go to Python Packages 2.Search for 'kivy' 3.Install


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
    bor_cloud = ObjectProperty()

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
    sky_texture = ObjectProperty()
    red_texture = ObjectProperty(None)
    clouds_texture = ObjectProperty(None)
    water_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.grass_texture = Image(source="grass.png").texture
        #self.grass_texture = Image(source="pines.png").texture
        self.grass_texture.wrap = "repeat"
        self.grass_texture.uvsize = (Window.width/self.grass_texture.width*2,-1)

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

    def scroll_red(self, time):
        #pines
        self.red_texture.uvpos = (((self.red_texture.uvpos[0]+ time/10)%Window.height),(self.red_texture.uvpos[1]+1))
        texture = self.property("red_texture")
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
    score = NumericProperty(0)
    life = NumericProperty(3)

    def move_volcano(self, time):
        volcano = self.root.ids.volcano
        volcano.x = volcano.x - randint(1,2)

        if volcano.x <= -100:
            volcano.x = Window.width + randint(1,10)



    def move_pines(self, time):
        pines = self.root.ids.pines
        pines.x = pines.x - randint(1,2)
        if pines.x <= -100:
            pines.x = Window.width+20


         #   pines.x = pines.x - randint(0, 40)
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
        purple_cloud = self.root.ids.purple_cloud
        yell_cloud = self.root.ids.yell_cloud
        bor_cloud = self.root.ids.bor_cloud

        if balloon.y > grass.height:
            if balloon.y >= Window.height-70:
                balloon.y = balloon.y - self.GRAVITY * time * 15

            elif volcano.collide_widget(balloon) or pines.collide_widget(balloon):


                if self.life == 1:
                    self.frames.cancel()
                    self.life = 0
                    balloon.size = (350, 350)
                    balloon.pos = (200, 200)
                    balloon.size_hint= (None, None)
                    balloon.source = "heart.png"

                    label = self.root.ids.label
                    label.text = "Oh no! \nGame Over!"
                    label.pos = (50, 290)
                    label.size = (160, 150)
                    label.color = (179, 250, 22, 1)

                elif self.life >1:
                    self.life -= 1
                    balloon.y = 600 + balloon.velocity * time
                    balloon.x = balloon.x + self.WIND * time
                    balloon.velocity = balloon.velocity - self.GRAVITY * time*20


            elif purple_cloud.collide_widget(balloon):
                balloon.y = balloon.y -20 + balloon.velocity * time
                balloon.x = balloon.x+5 + self.WIND * time
                balloon.velocity = balloon.velocity - self.GRAVITY * time*2
                self.score += 10
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
            balloon.size = (350,350)
            balloon.pos=(200,200)
            self.frames.cancel()
            label = self.root.ids.label
            label.text = "Safe Landing! \nScore " + str(self.score)
            label.pos=(50,250)
            label.size = (160,150)
            label.color = (179,250,22,1)
    pass


    def next_frame(self,time_passed):
        self.move_balloon(time_passed)
        self.move_volcano(time_passed)
        self.move_pines(time_passed)
        self.move_purple_cloud(time_passed)
        self.move_yell_cloud(time_passed)
        self.move_bor_cloud(time_passed)
        self.root.ids.background.scroll_clouds(time_passed)
        self.root.ids.background.scroll_grass(time_passed)
        self.root.ids.background.scroll_red(time_passed)
    pass

    def start(self):
        self.frames = Clock.schedule_interval(self.next_frame, 1/60.)

    pass

MainApp().run()



