from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.switch import Switch
from kivy.uix.slider import Slider
from kivy.uix.image import Image
from kivy.uix.spinner import Spinner
from kivy.utils import platform
from kivy.lang import Builder

Builder.load_file('bar.kv')
Builder.load_file('shop.kv')
Builder.load_file('settings.kv')
Builder.load_file('game.kv')

#НИЖНЯ ПАНЕЛЬ ДЛЯ ВСІХ ЕКРАНІВ
class BarScreen(Screen):
    def show_exit_panel(self, *args):
        self._blocker = self.ids.blocker
        self._panel = self.ids.panel_for_exit
        
        self._blocker.parent.remove_widget(self._blocker)
        self._panel.parent.remove_widget(self._panel)
        self._blocker.size_hint = (1, 1)
        self._panel.size_hint = (0.7, 0.23)
        self._blocker.opacity = 1
        self._panel.opacity = 1
        self._panel.disabled = False
        self.add_widget(self._blocker)
        self.add_widget(self._panel)

    def hide_exit_panel(self, *args):
        self.ids.blocker.size_hint = (0, 0)
        self.ids.blocker.opacity = 0
        self.ids.panel_for_exit.opacity = 0
        self.ids.panel_for_exit.disabled = True
        self.ids.panel_for_exit.size_hint = (0, 0)

    def go_to_game(self, *args):
        self.manager.current = 'game'

    def go_to_shop(self, *args):
        self.manager.current = 'shop'

    def go_to_settings(self, *args):
        self.manager.current = 'settings'

    def exit_app(self, *args):
        App.get_running_app().stop()

#ГРА
class GameScreen(BarScreen): 
    count = NumericProperty(0)
    def add_score(self):
        app = App.get_running_app()
        if app.sound_enabled and app.click_sound:
            app.click_sound.seek(0)
            app.click_sound.play()
        self.count += 1
   
#МАГАЗИН
class ShopScreen(BarScreen):
    pass

#НАЛАШТУВАННЯ
class SettingsScreen(BarScreen):
    def background_music(self, value):
        app = App.get_running_app()
        if value:
            app.music.play()
        else:
            app.music.stop()
    def soundeffects(self,  value):
        App.get_running_app().sound_enabled = value
    def volume(self, value):
        App.get_running_app().music.volume = value / 100
        App.get_running_app().click_sound.volume = value / 100
    def change_language(self, value):
        app = App.get_running_app()
        app.lang = app.LANGUAGES[value]
        app.update_language()

#СТРУКТУРА
class MediumApp(App):
    icon = 'image/click_icon.png'
    theme = StringProperty('light')
    LANGUAGES = {'Українська': {'score': 'Рахунок',
                                'settings': 'Налаштування',
                                'sound': 'Звук',
                                'music': 'Музика',
                                'soundeffect': 'Звукові ефекти',
                                'loudness': 'Гучність',
                                'general': 'Загальне',
                                'language': 'Мова',
                                'topic': 'Тема',
                                'vibration': 'Вібрація',
                                'other': 'Інше',
                                'light': 'Світла',
                                'dark': 'Темна',
                                'exit_question': 'Вийти з гри?',
                                'exit_confirm': 'Ви дійсно хочете вийти?',
                                'yes': 'Так!',
                                'no': 'Ні!'},
                'English': {'score': 'Score',
                            'settings': 'Settings',
                            'sound': 'Sound',
                            'music': 'Music',
                            'soundeffect': 'Sound effects',
                            'loudness': 'Loudness',
                            'general': 'General',
                            'language': 'Language',
                            'topic': 'Topic',
                            'vibration': 'Vibration',
                            'other': 'Other',
                            'light': 'Light',
                            'dark': 'Dark',
                            'exit_question': 'Exit the game?',
                            'exit_confirm': 'Do you really want to leave?',
                            'yes': 'Yes!',
                            'no': 'No!'}}
    def build(self):
        if platform == 'android' or platform == 'ios':
            Window.fullscreen = 'auto'
        else:
            Window.size = (360, 640)
        Window.clearcolor = (0.9, 0.9, 0.9)
        self.lang = self.LANGUAGES['Українська']
        self.sound_enabled = True
        self.click_sound = SoundLoader.load('sound/sound_click.mp3')
        self.click_sound.volume = 0.2
        self.music = SoundLoader.load('sound/Lobby_Time.mp3')
        self.music.loop = True
        self.music.volume = 0.2
        self.music.play()
        sm = ScreenManager()
        self.title = 'Clicker'
        sm.add_widget(GameScreen(name='game'))
        sm.add_widget(ShopScreen(name='shop'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm
    def update_language(self):
        for screen_name in ('game', 'shop', 'settings'):
            screen = self.root.get_screen(screen_name)
            screen.ids.exit_text.text = self.lang['exit_question']
            screen.ids.exit_text_2.text = self.lang['exit_confirm']
            screen.ids.yes_button.text = self.lang['yes']
            screen.ids.no_button.text = self.lang['no']
        game = self.root.get_screen('game')
        game.ids.score_text.text = self.lang['score']
        settings = self.root.get_screen('settings')
        settings.ids.settings_label.text = self.lang['settings']
        settings.ids.sound_text.text = self.lang['sound']
        settings.ids.music_text.text = self.lang['music']
        settings.ids.soundeffects_text.text = self.lang['soundeffect']
        settings.ids.loudness_text.text = self.lang['loudness']
        settings.ids.general_text.text = self.lang['general']
        settings.ids.language_text.text = self.lang['language']
        settings.ids.topic_text.text = self.lang['topic']
        settings.ids.vibration_text.text = self.lang['vibration']
        settings.ids.other_text.text = self.lang['other']
        settings.ids.topic_spinner.values = (self.lang['light'], self.lang['dark'])
        settings.ids.topic_spinner.text = self.lang['light'] if Window.clearcolor == [0.9, 0.9, 0.9, 1.0] else self.lang['dark']
    def change_theme(self, value):
        if value in ('Світла', 'Light'):
            self.theme = 'light'
            Window.clearcolor = (0.9, 0.9, 0.9)
        else:
            self.theme = 'dark'
            Window.clearcolor = (0.118, 0.133, 0.165)
MediumApp().run()