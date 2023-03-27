import wx

class Ventana(wx.Frame):
    preguntarSalir = 0
    mensajeSal = ""
    tituloSal = ""
    def __init__(self,titulo,tam = (400,300),preguntarSalir = 0,estilo = wx.DEFAULT_FRAME_STYLE,pos = (0,0)):
        styles = estilo
        tx,ty = tam
        x,y = pos
        wx.Frame.__init__(self,None,title=titulo,size=tam,style = styles,pos = pos)
        self.preguntarSalir = preguntarSalir
        self.panel = wx.Panel(self)

        self.Show()
        # self.Hide()
        self.InitUI()
    
    def InitUI(self):
        self.Bind(wx.EVT_CLOSE,self.onClose)


    def onClose(self,event):
        if(self.preguntarSalir == 1):
            desicion = wx.MessageDialog(None,self.tituloSal,self.mensajeSal,wx.YES_NO).ShowModal()
            if (desicion == wx.ID_YES):
                self.Destroy()
            else:
                return
        else:
            self.Destroy()