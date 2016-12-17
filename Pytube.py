# -*- coding: utf-8 -*-
import wx
import subprocess
import thread
# wx.TextCtrl()
# wx.StaticText()

class MiAplicacion(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent=parent,title=title,size=(800,600))
        sz = wx.BoxSizer(wx.HORIZONTAL)
        panel = wx.Panel(self, wx.ID_ANY)
       
		
        #Barra de menu
        barra_menu = wx.MenuBar()
        #Menu archivo
        menu_archivo = wx.Menu()
        m_guardar = menu_archivo.Append(-1, "Guardar como")
        m_salir = menu_archivo.Append(-1, "Salir")
       
        #Menu ayuda
        menu_ayuda = wx.Menu()
        m_ayuda=menu_ayuda.Append(-1, 'Acerca de')
        m_actualizar=menu_ayuda.Append(-1, 'Actualizar')
        
		
        
        # Agregar al menu principal
        barra_menu.Append(menu_ayuda, 'Ayuda')
        barra_menu.Append(menu_archivo, "Archivo")
        #barra_menu.Append(menu_formatos, "Formato")
        
        self.SetMenuBar(barra_menu)
        
        
        
        
        # Controles
        
       
        
        self.Bind(wx.EVT_MENU, self.actualizar, m_actualizar)
        btn1 = wx.Button(self, -1, "mp4-720x1280", pos=(80,50), size=(150,30))
        btn2 = wx.Button(self, -1, "webm-720x1280", pos=(240,50), size=(150,30))
        btn3 = wx.Button(self, -1, "mp4-360x640", pos=(400,50), size=(150,30))
        self.input_text = wx.TextCtrl(self, -1, "",pos=(80,20), size=(700,200))
        boton2 = wx.Button(self, -1, "Cancelar",pos=(650,200), size=(100,30))
        etiqueta = wx.StaticText(self, -1, "URL: ", pos=(30,110))
       
        self.Bind(wx.EVT_BUTTON, self.cancelar, boton2)
        self.Bind(wx.EVT_BUTTON, self.onClick1, btn1)
        self.Bind(wx.EVT_BUTTON, self.onClick2, btn2)
        self.Bind(wx.EVT_BUTTON, self.onClick3, btn3)
        self.Bind(wx.EVT_MENU, self.OnAboutBox, m_ayuda)
        self.Bind(wx.EVT_MENU, self.salir, m_salir)
        
        self.SetSizer(sz)
        self.Centre(True)
        self.Show()
        
		
        # Eventos
    def cancelar(self,event):
		subprocess.call(["killall", "youtube-dl"])
    def actualizar(self, event):
		subprocess.call(["pip", "install", "--upgrade", "youtube-dl"])
    def onClick1(self, event):
		txt = self.input_text.GetValue()
		print txt
		subprocess.call(["youtube-dl", "--format", "22", txt])
		start_new_thread(onClick1)
    def onClick2(self, event):
		txt = self.input_text.GetValue()
		print txt
		subprocess.call(["youtube-dl", "--format", "44", txt])
    def onClick3(self, event):
		txt = self.input_text.GetValue()
		print txt
		subprocess.call(["youtube-dl", "--format", "18", txt])
			
		
		
        
        
    def salir(self,event):
		self.Close(True)
	
		         
   
        
    def OnAboutBox(self,event):
		description="""Programador de Python repositorio en gitgub: github.com/adride00""" 
		licence = """GNU""" 
		info = wx.AboutDialogInfo()
		
		info.SetName('PyTube')
		info.SetVersion('beta 1.0')
		info.SetDescription(description)
		info.SetCopyright('(C) 2016 Adrian Campos')
		info.SetWebSite('http://www.github.com/adride00')
		info.SetLicence(licence)
		info.AddDeveloper('Adrian Campos')
		info.AddDocWriter('Adrian Campos')
		info.AddArtist('Code Python')
		
		wx.AboutBox(info) 
		start_new_thread(__init__)		
if __name__=='__main__':
    app = wx.App()
    frame = MiAplicacion(None,u"Pytube")
    app.MainLoop()
