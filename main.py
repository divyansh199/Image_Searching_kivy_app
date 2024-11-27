#APP->ScreenManager->Screen->Widget
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests

import os

Builder.load_file('frontend.kv')

class FirstScreen(Screen):
    def get_image_link(self):
        # get user query from text input

        query = self.manager.current_screen.ids.user_query.text

        #get wikipedia page url for images

        page = wikipedia.page(query)
        link_images = page.images[0]
        print(link_images)
        return link_images

    def download_image(self):

        #Download the images

        req = requests.get(self.get_image_link())

        os.makedirs('files', exist_ok=True)
        imagepath = 'files/image.jpg'

        with open(imagepath , 'wb') as file:
            file.write(req.content)

        return imagepath

    def set_image(self):
        # sets the image path in image widget
        self.manager.current_screen.ids.img.source = self.download_image()

class RootWidget(ScreenManager ):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()