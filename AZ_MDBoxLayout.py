"""
Components/BoxLayout
====================

:class:`~kivy.uix.boxlayout.BoxLayout` class equivalent. Simplifies working
with some widget properties. For example:

BoxLayout
---------

.. code-block:: kv

    BoxLayout:
        size_hint_y: None
        height: self.minimum_height

        canvas:
            Color:
                rgba: app.theme_cls.primary_color
            Rectangle:
                pos: self.pos
                size: self.size

MDBoxLayout
-----------

.. code-block:: kv

    MDBoxLayout:
        adaptive_height: True
        md_bg_color: app.theme_cls.primary_color

Available options are:
----------------------

- adaptive_height_
- adaptive_width_
- adaptive_size_

.. adaptive_height:
adaptive_height
---------------

.. code-block:: kv

    adaptive_height: True

Equivalent

.. code-block:: kv

    size_hint_y: None
    height: self.minimum_height

.. adaptive_width:
adaptive_width
--------------

.. code-block:: kv

    adaptive_width: True

Equivalent

.. code-block:: kv

    size_hint_x: None
    height: self.minimum_width

.. adaptive_size:
adaptive_size
-------------

.. code-block:: kv

    adaptive_size: True

Equivalent

.. code-block:: kv

    size_hint: None, None
    size: self.minimum_size
"""

__all__ = ("AZMDBoxLayout",)

from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import DeclarativeBehavior
from kivy.properties import ObjectProperty
import geonamescache
from kivymd.uix.dialog import MDDialog
from kivy.app import App

class AZMDBoxLayout(
    DeclarativeBehavior, ThemableBehavior, BoxLayout, MDAdaptiveWidget
):

    ric_tx=ObjectProperty()
    lt=ObjectProperty()
    ln=ObjectProperty()

    country=None
    continent=None
    dialog4=None
    dialog5=None
    mark=None

    temp_text=''


    def receive_text(self):
        self.temp_text=self.ric_tx.text
        self.ric_tx.text=''
        return self.temp_text

    def find_place(self):
        gnc=geonamescache.GeonamesCache()
        countrise=gnc.get_countries()
        citise=gnc.get_cities()

        for q in countrise.keys():
            qq=countrise[q]['name']

            if self.temp_text == '':
                break
            elif self.temp_text==qq:
                self.country=self.temp_text

                if countrise[q]['continentcode'] == 'AS':
                    self.continent='Asia'
                elif countrise[q]['continentcode'] == 'EU':
                    self.continent = 'Europe'
                elif countrise[q]['continentcode'] == 'AF':
                    self.continent='Africa'
                elif countrise[q]['continentcode'] == 'NA':
                    self.continent='North America'
                elif countrise[q]['continentcode'] == 'SA':
                    self.continent='South America'
                elif countrise[q]['continentcode'] == 'AN':
                    self.continent='Antarctica'
                elif countrise[q]['continentcode'] == 'AU' or countrise[q]['continentcode'] == 'OC':
                    self.continent='Australia, Oceania'
                else:
                    self.continent=countrise[q]['continentcode']

                self.dialog4=MDDialog(
                    title='Info Country ',
                    text='Country : '+self.country+'\nContinent : '+self.continent
                )
                self.dialog4.open()


        for w in citise.keys():
            ww=citise[w]['name']

            if self.temp_text == '':
                break
            elif self.temp_text==ww:
                # print(citise[w])
                t_app=App.get_running_app()
                t_map = t_app.root.ids.srvice_map
                t_map.plus_public_marker(citise[w]['latitude'],citise[w]['longitude'])


                self.dialog5=MDDialog(
                    title='Info City',
                    text='City : '+self.temp_text+
                        '\nTimeZone : '+citise[w]['timezone']+
                         '\nlat(y) : '+str(citise[w]['latitude'])+
                         '\nlon(x) : '+str(citise[w]['longitude'])
                )
                self.dialog5.open()
            else:
                pass

    def move_place(self):
        t_lt=self.lt.text
        t_ln=self.ln.text

        # print(t_lt)
        # print(type(t_ln))
        try:
            t_app=App.get_running_app()
            t_map=t_app.root.ids.srvice_map
            t_map.plus_public_marker(lat=float(t_lt),lon=float(t_ln))
        except:
            self.lt.text=''
            self.ln.text=''
            d=MDDialog(
                title='Error :',
                text='Lat or Lon Not < Float >\n\nLat or Lon Not < Filled >'+
                '\n\nLat or Lon Not < Range >'
            )
            d.open()
            d.size_hint=0.3,None
    """
    Box layout class.

    For more information, see in the
    :class:`~kivy.uix.boxlayout.BoxLayout` class documentation.
    """
