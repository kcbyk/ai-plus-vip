from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Line
from kivy.clock import Clock

class ESPOverlay(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.btn = Button(text="AI PLUS VIP", size_hint=(0.2, 0.08), pos_hint={'x': 0.4, 'y': 0.9}, background_color=(0, 1, 0.8, 1))
        self.add_widget(self.btn)
        Clock.schedule_interval(self.guncelle_esp, 1/20)

    def guncelle_esp(self, dt):
        self.canvas.after.clear()
        with self.canvas.after:
            Color(1, 0, 0, 1) # Düşman ESP Kutusu
            Line(rectangle=(400, 300, 150, 150), width=2)
            Color(0, 1, 1, 0.3) # Menzil Çemberi
            Line(circle=(1200, 540, 400), width=1)

class AIPlusApp(App):
    def build(self): return ESPOverlay()

if __name__ == '__main__': AIPlusApp().run()
      
