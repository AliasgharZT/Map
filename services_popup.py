from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog

class ServicesMarkerPopup():


    def show(self,info):


        dialog=MDDialog(
            title='Information :',
            text='''Name : %s
            \nState : %s
            \nCity : %s
            \nVillage : %s
            \nPhone : %s
            \nWebSite : %s
            \nInstagram : %s
            \nAccess Road : %s
            \nTraditional residence : %s
            \nOrganic Food : %s
            \nIndigenous Music : %s
            \nUpdate Time : %s
            \nLongitude : %s
            \nLatitude : %s
            '''%(info[1],info[2],info[3],info[4],info[5],info[6],info[7],info[8],
                 info[9],info[10],info[11],info[12],info[13],info[14])

        )
        dialog.size_hint=0.4,None

        return dialog.open()



