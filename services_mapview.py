from kivy_garden.mapview import MapView
from kivy .clock import Clock as c
from kivy.app import App
from services_markers import ServicesMarker
from kivy_garden.mapview import MapMarkerPopup
from AZ_MDBoxLayout import AZMDBoxLayout


class ServicesMapView(MapView):

    markers_name=[]

    def start_move(self):
        c.schedule_once(self.move,1)
        
    def move(self,*args):
        min_lat,min_lon,max_lat,max_lon=self.get_bbox()
        app=App.get_running_app()
        sql_data='SELECT * FROM main WHERE latitude > %s AND latitude < %s AND longitude > %s AND longitude < %s'%(min_lat,max_lat,min_lon,max_lon)
        
        app.cursor.execute(sql_data)
        markers=app.cursor.fetchall()


        for marker in markers:
            if marker[1] in self.markers_name:
                continue
            else:
                self.plus_marker(marker)

    def plus_marker(self, marker=None):
        lon,lat=marker[13],marker[14]
        temp_marker=ServicesMarker(lat=lat,lon=lon)
        temp_marker.color=1,1,0,0.6
        temp_marker.marker_data=marker
        self.add_widget(temp_marker)
        self.markers_name.append(marker[1])

    def plus_public_marker(self,lat,lon):
        w=MapMarkerPopup(lat=lat,lon=lon)
        w.color=0,1,1,0.6
        self.add_widget(w)
        self.center_on(lat,lon)


