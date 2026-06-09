from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
#from kivy.lang import Builder

Window.size = (360, 640)

#НИЖНЯ ПАНЕЛЬ ДЛЯ ВСІХ ЕКРАНІВ
class BarScreen(Screen):
    def build_bottom_bar(self):
        layout = FloatLayout()
        btns = BoxLayout(size_hint=(0.94, 0.08),
                         pos_hint={'center_x': 0.5, 'center_y': 0.05},
                         spacing=2)
        #КНОПКИ
        panel = Button(size_hint=(0.94, 0.08),
                       background_color=(0.5, 0.5, 0.5),
                       pos_hint={'center_x': 0.5, 'center_y': 0.05})
        btn_game = Button(background_normal='',
                               background_color=(1, 0, 0))
        btn_shop = Button(background_normal='',
                               background_color=(0, 1, 0))
        btn_settings = Button(background_normal='',
                               background_color=(0, 0, 1))
        btn_exit_game = Button(background_normal='',
                               background_color=(0, 0, 0))
        #БІНДИ
        btn_game.bind(on_press=self.go_to_game)
        btn_shop.bind(on_press=self.go_to_shop)
        btn_settings.bind(on_press=self.go_to_settings)
        btn_exit_game.bind(on_press=self.exit_app)
        #ВІДОБРАЖЕННЯ
        layout.add_widget(panel)
        btns.add_widget(btn_game)
        btns.add_widget(btn_shop)
        btns.add_widget(btn_settings)
        btns.add_widget(btn_exit_game)
        layout.add_widget(btns)
        return layout
    #КОМАНДИ
    def go_to_game(self, instance):
        self.manager.current = 'game'
    def go_to_shop(self, instance):
        self.manager.current = 'shop'
    def go_to_settings(self, instance):
        self.manager.current = 'settings'
    def exit_app(self, instance):
        App.get_running_app().stop()

#ГРА
class Game(BarScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        bar = self.build_bottom_bar()
        
        self.count = 0
        btn_click = Button(text='Click',
                           bold=True,
                           font_size=60,
                           background_color=(0, 132/255, 255/255),
                           size_hint=(0.875, 0.3),
                           pos_hint={'center_x': 0.5, 'center_y': 0.55})
        
        btn_click.bind(on_press=self.add_score)
        
        score_text = Label(text='Score',
                            bold=True,
                            font_size=35,
                            color=(0, 0, 0),
                            pos_hint={'center_x': 0.5, 'center_y': 0.9})
        self.score = Label(text='0',
                           bold=True,
                           font_size=65,
                           color=(0 , 0 , 0),
                           pos_hint={'center_x': 0.5, 'center_y': 0.8})

        layout.add_widget(btn_click)
        layout.add_widget(self.score)
        layout.add_widget(score_text)
        self.add_widget(layout)
        self.add_widget(bar)

    def add_score(self, instance):
        sound = SoundLoader.load('sound/sound_click.mp3')
        sound.volume = 0.2
        sound.play()
        self.count += 1
        self.score.text = f'{self.count}'
   
#МАГАЗИН
class ShopScreen(BarScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        bar = self.build_bottom_bar()
        
        label = Label(text='Shop Screen',
                      bold=True,
                      font_size=35,
                      color=(1, 0, 0),
                      pos=(0, 0))
        
        layout.add_widget(label)
        self.add_widget(layout)
        self.add_widget(bar)

#НАЛАШТУВАННЯ
class SettingsScreen(BarScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        bar = self.build_bottom_bar()
        
        label = Label(text='Settings Screen',
                      bold=True,
                      font_size=35,
                      color=(1, 0, 0),
                      pos=(0, 0))
        
        layout.add_widget(label)
        self.add_widget(layout)
        self.add_widget(bar)

#СТРУКТУРА
class MediumApp(App):
    icon = 'image/click_icon.png'
    Window.clearcolor = (1, 1, 1)
    def build(self):
        sm = ScreenManager()
        self.title = 'Clicker'
        sm.add_widget(Game(name='game'))
        sm.add_widget(ShopScreen(name='shop'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm

MediumApp().run()