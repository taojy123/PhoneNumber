#coding=utf8
#Boa:Frame:Frame1

import wx
import win32clipboard as w
import win32con

CITY_MAP = open("CITY_MAP.txt").read()
CITY_MAP = eval(CITY_MAP)
seg = {}

def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, aString)
    w.CloseClipboard()

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1LISTBOX1, wxID_FRAME1LISTBOX2, 
 wxID_FRAME1LISTBOX3, wxID_FRAME1LISTBOX4, wxID_FRAME1PANEL1, 
 wxID_FRAME1TEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(8)]


class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(376, 173), size=wx.Size(793, 576),
              style=wx.DEFAULT_FRAME_STYLE, title=u'\u6211\u8981\u67e5\u53f7')
        self.SetClientSize(wx.Size(777, 538))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(777, 538),
              style=wx.TAB_TRAVERSAL)

        self.listBox1 = wx.ListBox(choices=[], id=wxID_FRAME1LISTBOX1,
              name='listBox1', parent=self.panel1, pos=wx.Point(16, 16),
              size=wx.Size(128, 504), style=0)
        self.listBox1.Bind(wx.EVT_LISTBOX, self.OnListBox1Listbox,
              id=wxID_FRAME1LISTBOX1)

        self.listBox2 = wx.ListBox(choices=[], id=wxID_FRAME1LISTBOX2,
              name='listBox2', parent=self.panel1, pos=wx.Point(160, 16),
              size=wx.Size(160, 504), style=0)
        self.listBox2.Bind(wx.EVT_LISTBOX, self.OnListBox2Listbox,
              id=wxID_FRAME1LISTBOX2)

        self.listBox3 = wx.ListBox(choices=[], id=wxID_FRAME1LISTBOX3,
              name='listBox3', parent=self.panel1, pos=wx.Point(336, 16),
              size=wx.Size(112, 504), style=0)
        self.listBox3.Bind(wx.EVT_LISTBOX, self.OnListBox3Listbox,
              id=wxID_FRAME1LISTBOX3)

        self.listBox4 = wx.ListBox(choices=[], id=wxID_FRAME1LISTBOX4,
              name='listBox4', parent=self.panel1, pos=wx.Point(464, 16),
              size=wx.Size(120, 504), style=0)
        self.listBox4.Bind(wx.EVT_LISTBOX, self.OnListBox4Listbox,
              id=wxID_FRAME1LISTBOX4)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.panel1, pos=wx.Point(600, 16), size=wx.Size(152, 472),
              style=wx.TE_MULTILINE, value='')

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1,
              label=u'\u4e00\u952e\u590d\u5236', name='button1',
              parent=self.panel1, pos=wx.Point(600, 496), size=wx.Size(152, 23),
              style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.listBox1.Clear()
        for p in CITY_MAP.keys():
            self.listBox1.Append(p)

        dlgtext = wx.TextEntryDialog(self,u'请输入启动密码') 
        if dlgtext.ShowModal() != wx.ID_OK:
            raise
        if str(dlgtext.GetValue()) != "qq123456":
            raise



    def OnListBox1Listbox(self, event):
        self.listBox2.Clear()
        self.listBox3.Clear()
        self.listBox4.Clear()
        self.textCtrl1.SetValue("")
        p = self.listBox1.GetStringSelection()
        p = p.encode("gbk")
        citys = CITY_MAP.get(p, [])
        for city in citys:
            self.listBox2.Append(city)
        event.Skip()

    def OnListBox2Listbox(self, event):
        global seg
        self.listBox3.Clear()
        self.listBox4.Clear()
        self.textCtrl1.SetValue("")
        city = self.listBox2.GetStringSelection()
        city = city.encode("gbk")
        lines = open("./data/"+city+".txt").readlines()
        h = lines[0][:3]
        r = []
        for line in lines:
            line = line.strip()
            h2 = line[:3]
            if h == h2:
                r.append(line)
            else:
                self.listBox3.Append(h)
                seg[h] = r[:]
                h = h2
                r = [line]
        self.listBox3.Append(h)
        seg[h] = r[:]
        event.Skip()

    def OnListBox3Listbox(self, event):
        global seg
        self.listBox4.Clear()
        self.textCtrl1.SetValue("")
        h = self.listBox3.GetStringSelection()
        for s in seg.get(h, []):
            self.listBox4.Append(s)
        event.Skip()

    def OnListBox4Listbox(self, event):
        self.textCtrl1.SetValue("")
        s = self.listBox4.GetStringSelection()
        numbers = []
        for i in range(9999, -1, -1):
            number = s + str(i).zfill(4)
            numbers.append(number)
        t = "\n".join(numbers)
        self.textCtrl1.SetValue(t)
        event.Skip()

    def OnButton1Button(self, event):
        a = str(self.textCtrl1.GetValue())[:12*5000]
        setText(a)
        event.Skip()
