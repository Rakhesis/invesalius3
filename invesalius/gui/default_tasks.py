#--------------------------------------------------------------------------
# Software:     InVesalius - Software de Reconstrucao 3D de Imagens Medicas
# Copyright:    (C) 2001  Centro de Pesquisas Renato Archer
# Homepage:     http://www.softwarepublico.gov.br
# Contact:      invesalius@cti.gov.br
# License:      GNU - GPL 2 (LICENSE.txt/LICENCA.txt)
#--------------------------------------------------------------------------
#    Este programa e software livre; voce pode redistribui-lo e/ou
#    modifica-lo sob os termos da Licenca Publica Geral GNU, conforme
#    publicada pela Free Software Foundation; de acordo com a versao 2
#    da Licenca.
#
#    Este programa eh distribuido na expectativa de ser util, mas SEM
#    QUALQUER GARANTIA; sem mesmo a garantia implicita de
#    COMERCIALIZACAO ou de ADEQUACAO A QUALQUER PROPOSITO EM
#    PARTICULAR. Consulte a Licenca Publica Geral GNU para obter mais
#    detalhes.
#--------------------------------------------------------------------------

import wx
import wx.lib.foldpanelbar as fpb
import wx.lib.pubsub as ps

import task_exporter as exporter
import task_slice as slice_
import task_importer as importer
import task_surface as surface
import task_tools as tools

import data_notebook as nb

def GetCollapsedIconData():
    return \
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\
\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\
\x00\x01\x8eIDAT8\x8d\xa5\x93-n\xe4@\x10\x85?g\x03\n6lh)\xc4\xd2\x12\xc3\x81\
\xd6\xa2I\x90\x154\xb9\x81\x8f1G\xc8\x11\x16\x86\xcd\xa0\x99F\xb3A\x91\xa1\
\xc9J&\x96L"5lX\xcc\x0bl\xf7v\xb2\x7fZ\xa5\x98\xebU\xbdz\xf5\\\x9deW\x9f\xf8\
H\\\xbfO|{y\x9dT\x15P\x04\x01\x01UPUD\x84\xdb/7YZ\x9f\xa5\n\xce\x97aRU\x8a\
\xdc`\xacA\x00\x04P\xf0!0\xf6\x81\xa0\xf0p\xff9\xfb\x85\xe0|\x19&T)K\x8b\x18\
\xf9\xa3\xe4\xbe\xf3\x8c^#\xc9\xd5\n\xa8*\xc5?\x9a\x01\x8a\xd2b\r\x1cN\xc3\
\x14\t\xce\x97a\xb2F0Ks\xd58\xaa\xc6\xc5\xa6\xf7\xdfya\xe7\xbdR\x13M2\xf9\
\xf9qKQ\x1fi\xf6-\x00~T\xfac\x1dq#\x82,\xe5q\x05\x91D\xba@\xefj\xba1\xf0\xdc\
zzW\xcff&\xb8,\x89\xa8@Q\xd6\xaaf\xdfRm,\xee\xb1BDxr#\xae\xf5|\xddo\xd6\xe2H\
\x18\x15\x84\xa0q@]\xe54\x8d\xa3\xedf\x05M\xe3\xd8Uy\xc4\x15\x8d\xf5\xd7\x8b\
~\x82\x0fh\x0e"\xb0\xad,\xee\xb8c\xbb\x18\xe7\x8e;6\xa5\x89\x04\xde\xff\x1c\
\x16\xef\xe0p\xfa>\x19\x11\xca\x8d\x8d\xe0\x93\x1b\x01\xd8m\xf3(;x\xa5\xef=\
\xb7w\xf3\x1d$\x7f\xc1\xe0\xbd\xa7\xeb\xa0(,"Kc\x12\xc1+\xfd\xe8\tI\xee\xed)\
\xbf\xbcN\xc1{D\x04k\x05#\x12\xfd\xf2a\xde[\x81\x87\xbb\xdf\x9cr\x1a\x87\xd3\
0)\xba>\x83\xd5\xb97o\xe0\xaf\x04\xff\x13?\x00\xd2\xfb\xa9`z\xac\x80w\x00\
\x00\x00\x00IEND\xaeB`\x82' 

def GetCollapsedIconBitmap():
    return wx.BitmapFromImage(GetCollapsedIconImage())

def GetCollapsedIconImage():
    import cStringIO
    stream = cStringIO.StringIO(GetCollapsedIconData())
    return wx.ImageFromStream(stream)

def GetExpandedIconData():
    return \
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\
\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\
\x00\x01\x9fIDAT8\x8d\x95\x93\xa1\x8e\xdc0\x14EO\xb2\xc4\xd0\xd2\x12\xb7(mI\
\xa4%V\xd1lQT4[4-\x9a\xfe\xc1\xc2|\xc6\xc2~BY\x83:A3E\xd3\xa0*\xa4\xd2\x90H!\
\x95\x0c\r\r\x1fK\x81g\xb2\x99\x84\xb4\x0fY\xd6\xbb\xc7\xf7>=\'Iz\xc3\xbcv\
\xfbn\xb8\x9c\x15 \xe7\xf3\xc7\x0fw\xc9\xbc7\x99\x03\x0e\xfbn0\x99F+\x85R\
\x80RH\x10\x82\x08\xde\x05\x1ef\x90+\xc0\xe1\xd8\ryn\xd0Z-\\A\xb4\xd2\xf7\
\x9e\xfbwoF\xc8\x088\x1c\xbbae\xb3\xe8y&\x9a\xdf\xf5\xbd\xe7\xfem\x84\xa4\
\x97\xccYf\x16\x8d\xdb\xb2a]\xfeX\x18\xc9s\xc3\xe1\x18\xe7\x94\x12cb\xcc\xb5\
\xfa\xb1l8\xf5\x01\xe7\x84\xc7\xb2Y@\xb2\xcc0\x02\xb4\x9a\x88%\xbe\xdc\xb4\
\x9e\xb6Zs\xaa74\xadg[6\x88<\xb7]\xc6\x14\x1dL\x86\xe6\x83\xa0\x81\xba\xda\
\x10\x02x/\xd4\xd5\x06\r\x840!\x9c\x1fM\x92\xf4\x86\x9f\xbf\xfe\x0c\xd6\x9ae\
\xd6u\x8d \xf4\xf5\x165\x9b\x8f\x04\xe1\xc5\xcb\xdb$\x05\x90\xa97@\x04lQas\
\xcd*7\x14\xdb\x9aY\xcb\xb8\\\xe9E\x10|\xbc\xf2^\xb0E\x85\xc95_\x9f\n\xaa/\
\x05\x10\x81\xce\xc9\xa8\xf6><G\xd8\xed\xbbA)X\xd9\x0c\x01\x9a\xc6Q\x14\xd9h\
[\x04\xda\xd6c\xadFkE\xf0\xc2\xab\xd7\xb7\xc9\x08\x00\xf8\xf6\xbd\x1b\x8cQ\
\xd8|\xb9\x0f\xd3\x9a\x8a\xc7\x08\x00\x9f?\xdd%\xde\x07\xda\x93\xc3{\x19C\
\x8a\x9c\x03\x0b8\x17\xe8\x9d\xbf\x02.>\x13\xc0n\xff{PJ\xc5\xfdP\x11""<\xbc\
\xff\x87\xdf\xf8\xbf\xf5\x17FF\xaf\x8f\x8b\xd3\xe6K\x00\x00\x00\x00IEND\xaeB\
`\x82' 

def GetExpandedIconBitmap():
    return wx.BitmapFromImage(GetExpandedIconImage())

def GetExpandedIconImage():
    import cStringIO
    stream = cStringIO.StringIO(GetExpandedIconData())
    return wx.ImageFromStream(stream)


# Main panel
class Panel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, pos=wx.Point(5, 5),
                          size=wx.Size(280, 656))
        
        sizer = wx.BoxSizer(wx.VERTICAL)        
        #sizer.Add(UpperTaskPanel(self), 5, wx.EXPAND|wx.GROW)
        sizer.Add(UpperTaskPanel(self), 6, wx.EXPAND|wx.GROW)

        #sizer.Add(LowerTaskPanel(self), 3, wx.EXPAND|wx.GROW)
        sizer.Add(LowerTaskPanel(self), 2, wx.EXPAND|wx.GROW)

        
        self.SetSizer(sizer)

# Lower fold panel
class LowerTaskPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, pos=wx.Point(5, 5),
        #                  size=wx.Size(280, 700))
                           size=wx.Size(280, 400))
        
        fold_panel = fpb.FoldPanelBar(self, -1, wx.DefaultPosition,
                                      self.GetSize(),fpb.FPB_DEFAULT_STYLE,
                                      fpb.FPB_COLLAPSE_TO_BOTTOM) 

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(fold_panel, 1, wx.GROW|wx.EXPAND)        
        self.SetSizer(sizer)

        image_list = wx.ImageList(16,16)
        image_list.Add(GetExpandedIconBitmap())
        image_list.Add(GetCollapsedIconBitmap())

        # Fold 1 - Data
        item = fold_panel.AddFoldPanel("Data", collapsed=False,
                                       foldIcons=image_list)
        style = fold_panel.GetCaptionStyle(item)
        col = style.GetFirstColour()

        fold_panel.AddFoldPanelWindow(item, nb.NotebookPanel(item), Spacing= 0,
                                      leftSpacing=0, rightSpacing=0)
        fold_panel.Expand(fold_panel.GetFoldPanel(0))

        # Fold 2 - Tools
        # Measures
        # Text Annotations
        #item = fold_panel.AddFoldPanel("Tools", collapsed=False,
        #                               foldIcons=image_list)
        #style = fold_panel.GetCaptionStyle(item)
        #col = style.GetFirstColour()
        # 
        #fold_panel.AddFoldPanelWindow(item, tools.TaskPanel(item), Spacing= 0,
        #                              leftSpacing=0, rightSpacing=0)
        #fold_panel.Expand(fold_panel.GetFoldPanel(1))

# Upper fold panel
class UpperTaskPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, pos=wx.Point(5, 5),
                          size=wx.Size(280, 656))

        fold_panel = fpb.FoldPanelBar(self, -1, wx.DefaultPosition,
                                      self.GetSize(),fpb.FPB_DEFAULT_STYLE,
                                      fpb.FPB_SINGLE_FOLD) 
        
        print self.GetBackgroundColour()                              
        #self.SetBackgroundColour((0,255,0))


        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(fold_panel, 1, wx.GROW|wx.EXPAND)
        self.SetSizer(sizer)

        image_list = wx.ImageList(16,16)
        image_list.Add(GetExpandedIconBitmap())
        image_list.Add(GetCollapsedIconBitmap())

        # Fold 1 - Import

        item = fold_panel.AddFoldPanel(_("1. InVesalius start"), collapsed=True,
                                      foldIcons=image_list)
        style = fold_panel.GetCaptionStyle(item)
        col = style.GetFirstColour()
        
        

        fold_panel.AddFoldPanelWindow(item, importer.TaskPanel(item), Spacing= 0,
                                      leftSpacing=0, rightSpacing=0)
        fold_panel.Expand(fold_panel.GetFoldPanel(0))
        
        # Fold 2 - Mask for segmentation and edition
        
        item = fold_panel.AddFoldPanel(_("2. Select region of interest"),
                                       collapsed=True, foldIcons=image_list)
        style = fold_panel.GetCaptionStyle(item)
        col = style.GetFirstColour()
        slice_panel = slice_.TaskPanel(item) 
        fold_panel.AddFoldPanelWindow(item, slice_panel, Spacing= 0,
                                      leftSpacing=0, rightSpacing=0)
        self.__id_slice = item.GetId()
        self.slice_panel = slice_panel
        #fold_panel.Expand(fold_panel.GetFoldPanel(1))

        # Fold 3
        # select mask - combo
        # mesh quality - combo?
        # apply button
        # Contour - slider
        # enable / disable Fill holes
        item = fold_panel.AddFoldPanel(_("3. Configure 3D surface"), collapsed=True,
                                       foldIcons=image_list)
        style = fold_panel.GetCaptionStyle(item)
        col = style.GetFirstColour()
        
        fold_panel.AddFoldPanelWindow(item, surface.TaskPanel(item),
                                      Spacing= 0, leftSpacing=0, rightSpacing=0)
        #fold_panel.Expand(fold_panel.GetFoldPanel(2))

        # Fold 4
        # Export volume
        item = fold_panel.AddFoldPanel(_("4. Export data"), collapsed=True,
                                       foldIcons=image_list)
        style = fold_panel.GetCaptionStyle(item)
        col = style.GetFirstColour()
        
        fold_panel.AddFoldPanelWindow(item, exporter.TaskPanel(item), 
                                      Spacing= 0, leftSpacing=0, rightSpacing=0)

        self.fold_panel = fold_panel
        self.__bind_evt()

    def __bind_evt(self):
        self.fold_panel.Bind(fpb.EVT_CAPTIONBAR, self.OnFoldPressCaption)

    def OnFoldPressCaption(self, evt):
        id = evt.GetTag().GetId()
        closed = evt.GetFoldStatus()
         
        if self.__id_slice == id:
            ps.Publisher().sendMessage('Retrieve task slice style')
        else:
            ps.Publisher().sendMessage('Disable task slice style')

        
        evt.Skip()
