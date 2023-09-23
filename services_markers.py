from kivy_garden.mapview import MapMarkerPopup
from services_popup import ServicesMarkerPopup

class ServicesMarker(MapMarkerPopup):

    marker_data=[]

    def on_press(self):
        pop=ServicesMarkerPopup()
        pop.show(self.marker_data)


