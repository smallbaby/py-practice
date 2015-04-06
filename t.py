# -*- coding:utf-8 -*-
import wx
import images
import data

class myFrame(wx.Frame):
    def __init__(self,parent,title,size):
        wx.Frame.__init__(self,parent,-1,title,size = size)
        self.SetBackgroundColour('white')
        
        #布局 size
        self.width = self.Size.width
        self.height = self.Size.height
        self.up = self.Size.height/25*24
        #self.down = self.Size.height/3
        self.left = self.Size.width/4
        self.right = self.Size.width/4*3
        
        #上下结构
        self.spltUD = wx.SplitterWindow(self,size = size,style=
	wx.SP_3DBORDER)
        
        self.winUp = wx.Window(self.spltUD,-1,(0,0),(self.width,self.up))
        self.winUp.SetBackgroundColour('red')

        #self.winDown = wx.Window(self.spltUD,-1,(0,self.up),(self.width,self.down))
        #self.winDown.SetBackgroundColour('black')
        
#        self.spltUD.SplitHorizontally(self.winUp,self.winDown,-5)

        #左右结构
        self.spltLF = wx.SplitterWindow(self.winUp,size = (self.width,self.up))

        self.winLeft = wx.Window(self.spltLF,-1,(0,0),(self.left,self.up))
        self.winLeft.SetBackgroundColour('White')
        
        self.winRight = wx.Window(self.spltLF,-1,(0,self.left),(self.right,self.up))
        self.winRight.SetBackgroundColour('green')
        
        self.spltLF.SplitVertically(self.winLeft,self.winRight,-10)

	panel = wx.Panel(self,-1)
	panel.SetBackgroundColour("White")
	statusBar = self.CreateStatusBar()
	toolbar  = self.CreateToolBar()
	toolbar.AddSimpleTool(wx.NewId(),images.getNewBitmap(),"New","xxxx")
	toolbar.Realize()


        # Create an image list
        il = wx.ImageList(16,16)

        # Get some standard images from the art provider and add them
        # to the image list
        self.fldridx = il.Add(
            wx.ArtProvider.GetBitmap(wx.ART_FOLDER,
                    wx.ART_OTHER, (16,16)))
        self.fldropenidx = il.Add(
            wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN,
                    wx.ART_OTHER, (16,16)))
        self.fileidx = il.Add(
            wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE,
                    wx.ART_OTHER, (16,16)))


	self.tree = wx.TreeCtrl(self.winLeft,id = -1,pos=(0,0),size=self.winLeft.Size) 
	self.tree.AssignImageList(il)
	root = self.tree.AddRoot("数据仓库研发部")
	self.tree.SetItemImage(root, self.fldridx,
                               wx.TreeItemIcon_Normal)
        self.tree.SetItemImage(root, self.fldropenidx,
                               wx.TreeItemIcon_Expanded)

        self.AddTreeNodes(root, data.tree)
        self.tree.Expand(root)


        #事件绑定
        self.Bind(wx.EVT_SIZE,self.OnSize)
    
    def AddTreeNodes(self, parentItem, items):
        for item in items:
            if type(item) == str:
                newItem = self.tree.AppendItem(parentItem, item)
                self.tree.SetItemImage(newItem, self.fileidx,
                                       wx.TreeItemIcon_Normal)
            else:
                newItem = self.tree.AppendItem(parentItem, item[0])
                self.tree.SetItemImage(newItem, self.fldridx,
                                       wx.TreeItemIcon_Normal)
                self.tree.SetItemImage(newItem, self.fldropenidx,
                                       wx.TreeItemIcon_Expanded)

                self.AddTreeNodes(newItem, item[1])



    def OnSize(self,event):
        size = event.Size
        #self.spltUD.Size=event.Size
        self.spltLF.Size=(size.width-size.width+150,size.height)
        self.spltUD.Size=(size.width-self.spltLF.Size,size.height)

if __name__ == '__main__':
    app = wx.App(False)
    frame = myFrame(None,'bdw center',(800,600))
    frame.Show(True)
    app.MainLoop() 
