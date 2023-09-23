import sqlite3
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField

from services_mapview import ServicesMapView
from kivymd.uix.dialog import MDDialog
from AZ_MDBoxLayout import AZMDBoxLayout


Builder.load_file('style.kv')

kv_search='''
AZMDBoxLayout:
    ric_tx:my_text
    MDIconButton:
        id:my_icon
        icon:'magnify'
        on_press:
            root.receive_text()
            root.find_place()
    MDTextField:
        id:my_text
        max_text_length:21
        focus:True
        mode:'round'
'''

kv_place='''
AZMDBoxLayout:
    orientation:'vertical'
    lt:lat
    ln:lon

    AZMDBoxLayout:
        MDTextField:
            id:lat
            mode:"rectangle"
            hint_text:'lat(y):'
            max_text_length:8
            input_filter:'int'
            focus:True
        Label:
            text:''
            size_hint:0.1,0.1
        MDTextField:
            id:lon
            mode:"rectangle"
            hint_text:'lon(x):'
            max_text_length:8
            input_filter:'int'
            # focus:True
    MDFlatButton:
        text:'Find'
        pos_hint:{'x':0.4,'y':0.5}
        on_press:root.move_place()
'''


class Style(MDBoxLayout):
    dialog2=None
    dialog3=None
    dialog6=None

    def show2(self):
        self.dialog2 = MDDialog(

            title='About',
            text='This program was created by Aliasghar Zahdyan\n\n'+
            '                                                   <<< A.Z >>>'

        )
        self.dialog2.open()

    def searching(self):
        self.dialog3=MDDialog(
            title='Search\n',
            type='custom',
            content_cls=Builder.load_string(kv_search)
        )

        self.dialog3.size_hint=0.5,None
        self.dialog3.open()

    def show_place(self):
        self.dialog6=MDDialog(
            title='Find Place \n\n\n',
            type='custom',
            content_cls=Builder.load_string(kv_place)
        )

        self.dialog6.open()
        self.dialog6.size_hint=0.4,None


class MainApp(MDApp):

    database=None
    cursor=None

    def build(self):
        self.theme_cls.primary_palette='Blue'
        self.theme_cls.primary_hue='800'

        return Style()

    def on_start(self):
       self.database=sqlite3.connect('city_data.db')
       self.cursor=self.database.cursor()

       
MainApp().run()


