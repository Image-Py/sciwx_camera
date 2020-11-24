if __name__ == '__main__':
	import sys, wx
	sys.path.append('../')
	from sciwx_camera.campanel import CameraPanel
	app = wx.App()
	frame = wx.Frame(None, title='Camera Frame')
	CameraPanel(frame)
	frame.Fit()
	frame.Show()
	app.MainLoop()
else:
	from .campanel import CameraPanel
	from .camera import *
