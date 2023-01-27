from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang.builder import Builder

class MainScreen(Screen):
    pass
class WindowManager(ScreenManager):
    pass
Builder.load_file("./main.kv")
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style='Dark'
        self.wm=WindowManager()
        screens=[(MainScreen(name="mainScreen"))]
        for screen in screens:
            self.wm.add_widget(screen)
        return self.wm
    def AuthFunc(self):
        pass
   
if __name__=="__main__": 
    MainApp().run()