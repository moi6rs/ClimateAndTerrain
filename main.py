from direct.showbase.ShowBase import ShowBase
import dia
class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

    estado_dia = dia.Dia(6,23,20).manania()
    print estado_dia
app = MyApp()
app.run()