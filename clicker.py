from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.uix.switch import Switch
from kivy.uix.slider import Slider
from kivy.uix.image import Image
from kivy.uix.spinner import Spinner
#from kivy.lang import Builder

Window.size = (360, 640)

#НИЖНЯ ПАНЕЛЬ ДЛЯ ВСІХ ЕКРАНІВ
class BarScreen(Screen):
    def build_bottom_bar(self):
        self.layout = FloatLayout()
        self.panel_for_exit = FloatLayout(size_hint=(0.6, 0.23),
                                          pos_hint={'center_x': 0.5, 'center_y': 0.51})
        self.btns = BoxLayout(size_hint=(0.94, 0.08),
                              pos_hint={'center_x': 0.5, 'center_y': 0.05},
                              spacing=2)
        self.blocker = Button(size_hint=(1, 1),
                              background_color=(0.5, 0.5, 0.5),
                              disabled=True)
        #КНОПКИ
        panel = Button(size_hint=(0.94, 0.08),
                       background_color=(0.5, 0.5, 0.5),
                       pos_hint={'center_x': 0.5, 'center_y': 0.05})
        question = Label(text='Вийти з гри?',
                         font_size=30,
                         color=(0 , 0 , 0),
                         pos_hint={'x': 0, 'y': 0.2})
        question2 = Label(text='Ви дійсно хочете вийти?',
                         font_size=20,
                         bold=True,
                         color=(0 , 0 , 0),
                         pos_hint={'x': 0, 'y': -0.04})
        bg = Button(background_normal='',
                    size_hint=(1, 1),
                    pos_hint={'x': 0, 'y': 0},
                    background_color=(0.5, 0.5, 0.5))
        accept = Button(text='Так!',
                        size_hint=(0.4, 0.22),
                        pos_hint={'x': 0.05, 'y': 0.05})
        cancel = Button(text='Ні!',
                        size_hint=(0.4, 0.22),
                        pos_hint={'right': 0.95, 'y': 0.05})
        self.btn_game = Button(background_normal='',
                               background_color=(1, 0, 0))
        self.btn_shop = Button(background_normal='',
                               background_color=(0, 1, 0))
        self.btn_settings = Button(background_normal='',
                                   background_color=(0, 0, 1))
        self.btn_exit_game = Button(background_normal='',
                                    background_color=(0, 0, 0))
        #БІНДИ
        self.btn_game.bind(on_press=self.go_to_game)
        self.btn_shop.bind(on_press=self.go_to_shop)
        self.btn_settings.bind(on_press=self.go_to_settings)
        self.btn_exit_game.bind(on_press=self.show_exit_panel)
        accept.bind(on_press=self.exit_app)
        cancel.bind(on_press=self.hide_exit_panel)
        #ВІДОБРАЖЕННЯ
        self.layout.add_widget(panel)
        self.panel_for_exit.add_widget(bg)
        self.panel_for_exit.add_widget(question)
        self.panel_for_exit.add_widget(question2)
        self.panel_for_exit.add_widget(accept)
        self.panel_for_exit.add_widget(cancel)
        self.btns.add_widget(self.btn_game)
        self.btns.add_widget(self.btn_shop)
        self.btns.add_widget(self.btn_settings)
        self.btns.add_widget(self.btn_exit_game)
        self.layout.add_widget(self.btns)
        return self.layout
    #КОМАНДИ
    def show_exit_panel(self, instance):
        self.layout.add_widget(self.blocker)
        self.layout.add_widget(self.panel_for_exit)
    def hide_exit_panel(self, instance):
        self.layout.remove_widget(self.blocker)
        self.layout.remove_widget(self.panel_for_exit)
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
        widget = BoxLayout(size_hint=(0.94, 0.8),
                           orientation='vertical',
                           spacing=15,
                           pos_hint={'center_x': 0.5, 'center_y': 0.515})
        
        wb1 = BoxLayout(padding=15)
        wb2 = BoxLayout(padding=15)
        wb3 = BoxLayout(padding=15)
   
        inside1 = BoxLayout(size_hint=(1, 0.8),
                            orientation='vertical',
                            pos_hint={'center_x': 0.5})
        inside2 = BoxLayout(size_hint=(1, 0.8),
                            orientation='vertical',
                            pos_hint={'center_x': 0.5})
        inside3 = BoxLayout(size_hint=(1, 0.8),
                            orientation='vertical',
                            pos_hint={'center_x': 0.5})
        
        btn_sound1 = BoxLayout(orientation='horizontal', size_hint=(1, None), height=40, padding=(0, 0, 30, 0), spacing=15)
        img_s1 = Image(source='image/music-player.png',
                       size_hint=(None, 1),
                       width=35)
        txt_s1 = Label(text='Музика',
                       font_size=25,
                       bold=True,
                       color=(0, 0, 0),
                       halign='left',
                       valign='middle',
                       size_hint=(1, 1),
                       text_size=(None, None))
        txt_s1.bind(size=lambda inst, val: setattr(inst, 'text_size', val))
        sw_s1 = Switch(size_hint=(None, 1), width=45)

        btn_sound1.add_widget(img_s1)
        btn_sound1.add_widget(txt_s1)
        btn_sound1.add_widget(sw_s1)
        
        btn_sound2 = BoxLayout(orientation='horizontal', size_hint=(1, None), height=40, padding=(0, 0, 30, 0), spacing=15)
        img_s2 = Image(source='image/speaker-filled-audio-tool.png',
                       size_hint=(None, 1),
                       width=35)
        txt_s2 = Label(text='Звукові ефекти',
                       font_size=23,
                       bold=True,
                       color=(0, 0, 0),
                       halign='left',
                       valign='middle',
                       size_hint=(1, 1),
                       text_size=(None, None))
        txt_s2.bind(size=lambda inst, val: setattr(inst, 'text_size', val))
        sw_s2 = Switch(size_hint=(None, 1), width=45)
        btn_sound2.add_widget(img_s2)
        btn_sound2.add_widget(txt_s2)
        btn_sound2.add_widget(sw_s2)
        
        btn_sound3 = BoxLayout(orientation='horizontal', size_hint=(1, None), height=40, spacing=15)
        img_s3 = Image(source='image/wave-sound.png',
                       size_hint=(None, 1),
                       width=35)
        txt_s3 = Label(text='Гучність',
                       font_size=23,
                       bold=True,
                       color=(0, 0, 0),
                       halign='left',
                       valign='middle',
                       size_hint=(None, 1),
                       width=95,
                       text_size=(None, None))
        txt_s3.bind(size=lambda inst, val: setattr(inst, 'text_size', val))
        sl_s3 = Slider(min=0, max=100, value=50, size_hint=(1, 1))
        btn_sound3.add_widget(img_s3)
        btn_sound3.add_widget(txt_s3)
        btn_sound3.add_widget(sl_s3)
        
        btn_general1 = BoxLayout(orientation='horizontal', size_hint=(1, None), height=40, spacing=15)
        img_g1 = Image(source='image/globe.png',
                       size_hint=(None, 1),
                       width=35)
        txt_g1 = Label(text='Мова',
                       font_size=23,
                       bold=True,
                       color=(0, 0, 0),
                       halign='left',
                       valign='middle',
                       size_hint=(None, 1),
                       width=200,
                       text_size=(None, None))
        txt_g1.bind(size=lambda inst, val: setattr(inst, 'text_size', val))
        sp_g1 = Spinner(text='Українська',
                        values=('Українська', 'English'),
                        size_hint=(1, 1))
        btn_general1.add_widget(img_g1)
        btn_general1.add_widget(txt_g1)
        btn_general1.add_widget(sp_g1)
        
        btn_general2 = BoxLayout(orientation='horizontal', size_hint=(1, None), height=40, spacing=15)
        img_g2 = Image(source='image/art.png',
                       size_hint=(None, 1),
                       width=35)
        txt_g2 = Label(text='Тема',
                       font_size=23,
                       bold=True,
                       color=(0, 0, 0),
                       halign='left',
                       valign='middle',
                       size_hint=(None, 1),
                       width=200,
                       text_size=(None, None))
        txt_g2.bind(size=lambda inst, val: setattr(inst, 'text_size', val))
        sp_g2 = Spinner(text='Світла',
                        values=('Світла', 'Темна'),
                        size_hint=(1, 1))
        btn_general2.add_widget(img_g2)
        btn_general2.add_widget(txt_g2)
        btn_general2.add_widget(sp_g2)
        btn_general3=Button()
        
        btn_other1=Button()
        btn_other2=Button()
        btn_other3=Button()
        
        label = Label(text='Налаштування',
                      bold=True,
                      font_size=35,
                      color=(0, 0, 0),
                      pos_hint={'center_x': 0.5, 'center_y': 0.955})
        
        layout.add_widget(widget)
        
        widget.add_widget(wb1)
        widget.add_widget(wb2)
        widget.add_widget(wb3)
        
        wb1.add_widget(inside1)
        wb2.add_widget(inside2)
        wb3.add_widget(inside3)
        
        inside1.add_widget(btn_sound1)
        inside1.add_widget(btn_sound2)
        inside1.add_widget(btn_sound3)
        
        inside2.add_widget(btn_general1)
        inside2.add_widget(btn_general2)
        inside2.add_widget(btn_general3)
        
        inside3.add_widget(btn_other1)
        inside3.add_widget(btn_other2)
        inside3.add_widget(btn_other3)
        
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