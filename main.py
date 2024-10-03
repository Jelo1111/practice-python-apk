from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivymd.uix.fitimage import FitImage
from kivymd.uix.button import MDButton, MDButtonText
from kivy.uix.button import Button
from kivy.metrics import dp

#window size
Window.size = (1280, 800)
# Set the window background color to white
Window.clearcolor = (1, 1, 1, 1)  # RGBA values for white

class Mainscreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        LabelBase.register(name="Semi-Bold", fn_regular="fonts/Poppins-SemiBold.ttf")
        self.layout = FloatLayout()
        
        # Add the logo image
        self.logo_img = FitImage(source="images/logo.jpg",
                            size_hint=(None, None),
                            size=(dp(105), dp(120)),
                            pos_hint={'center_x': .1, 'top': 1})
        self.layout.add_widget(self.logo_img)

        self.promo_img = FitImage(source="images/promo.jpg",
                            size_hint=(.55, None),
                            size=(0, 400),
                            pos_hint={'center_x': 0.5, 'center_y': 0.5}
                            )
        self.layout.add_widget(self.promo_img)

        self.star_btn = MDButton(
                            MDButtonText(text = "Tap to Start",
                                        theme_text_color= "Custom",
                                        text_color= "black",
                                        theme_font_name = "Custom",
                                        font_name = "Semi-Bold",
                                        theme_font_size = "Custom",
                                        font_size = dp(20),
                                        pos_hint = {"center_x": .5, "center_y": .5}),
                                    
                                    style = "filled",
                                    theme_bg_color = "Custom",
                                    md_bg_color=(1, 0.6, 0, 1),
                                    theme_width = "Custom",
                                    size_hint_x = .5,
                                    pos_hint = {"center_x": .5, "center_y": .15})
        self.layout.add_widget(self.star_btn)
        self.add_widget(self.layout)

class KioskApp(MDApp):
     def build(self):
        sm = MyScreenManager()
        sm.add_widget(Mainscreen(name="Main"))
        return sm

if __name__ == '__main__':
    KioskApp().run()
