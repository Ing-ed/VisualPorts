import wx
import serial.tools.list_ports as ports
import threading
import time
from Ventana import Ventana
flag = 1

def onEnter(event):
    frame.SetTransparent(100)

def onExit(event):
    frame.SetTransparent(30)

def Scan():
    global flag
    while(1):
        if(not flag):
            return
        lista.Clear()
        list = ports.comports() 
        for port in list:
            lista.Append(str(port))    
        time.sleep(1)
    return

def exit(event):
    global flag
    desicion = wx.MessageDialog(None,"sal","sal?",wx.YES_NO).ShowModal()
    if (desicion == wx.ID_YES):
        flag = 0
        frame.Destroy()
    else:
        return



app = wx.App()
# estilo = wx.FRAME_NO_TASKBAR & wx.CLOSE_BOX
estilo = (wx.CLOSE_BOX | wx.CAPTION | wx.FRAME_NO_TASKBAR | wx.STAY_ON_TOP)
x, y = wx.DisplaySize()
frame = Ventana("",preguntarSalir=0,tam=(300,240),estilo=estilo,pos = (x-300,30))
frame.Bind(wx.EVT_CLOSE,exit)
frame.SetTransparent(100)
lista = wx.ListBox(frame,size=(300,200))
# frame.Bind(wx.EVT_ENTER_WINDOW,onEnter)
# frame.Bind(wx.EVT_LEAVE_WINDOW,onExit)
hilo = threading.Thread(target=Scan)
hilo.start()
app.MainLoop()

