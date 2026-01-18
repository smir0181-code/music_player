import os
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.animation import Animation
from playsound import playsound
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
Window.size = (340,550)
class SongCover(MDBoxLayout):
    angle = NumericProperty()
    anim = Animation(angle=-360, d=2,t='linear')
    #anim += Animation(angle=0, d=0, t='linear')
    #pess=MDBoxLayout()
    anim.repeat = True
    we=.001
    def rotate(self):
        if self.anim.have_properties_to_animate(self):
            self.anim.stop(self)
            #self.progress.stop(self.widget)
        else:
            self.anim.start(self)
            #self.progress.start(self.widget)
        self.anim.start(self)

    def play(self,widget):
        #progress = Animation(value=1, d=34, t='linear')
        self.widget = widget
        #self.progress.start(widget)
        self.rotate()
        self.sound=SoundLoader.load('Eva.mp3')
        self.sound.play()
        self.progressEvent = Clock.schedule_interval(self.updateprogessbar, 1)
        #self.timeEvent = Clock.schedule_interval(self.settime, 1)
    def stop(self,widget):
        self.widget = widget
        #self.progress.start(widget)
        self.sound.stop()

    def updateprogessbar(self,wer):
        self.progress=self.sound.get_pos()/self.sound.length
        SongCover.we=self.progress
        if SongCover.we>0.05:
            self.rotate()
        print(self.we)
class MusicScreen(Screen):
    pass
class MainApp(MDApp):
    def build(self):
        self.load_kv('main.kv')
        self.song = 'C:/Users/virvi/OneDrive/Документы/Python_progect/Git/music_player'
        #self.sdf = .0101
        playsc= os.listdir(self.song)
        Clock.schedule_interval(self.progg,1)
        return MusicScreen()
    def progg(self,*args):
       self.root.ids.progress.value=SongCover.we

if __name__=="__main__":
    MainApp().run()
