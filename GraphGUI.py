import wx
import os 
from subprocess import Popen, PIPE

class MyApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)
        
        # init frame
        self.InitFrame()
    
    def InitFrame(self):
        frame = MyFrame()
        frame.Show()


class MyFrame(wx.Frame):
    def __init__(self, title="Project 3", pos=(100,100)):
        super().__init__(None, title=title, pos=pos)
        # initialize the frame's contents
        self.OnInit()

    def OnInit(self):
        self.panel = MyForm(self)
        self.Fit()

class MyForm(wx.Panel):

    def __init__(self, parent ):
        super().__init__(parent=parent)

        png = wx.Image('Images/Gator.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        gatorIco = wx.StaticBitmap(self, -1, png)
        gatorIco2 = wx.StaticBitmap(self, -1, png)
        gatorIco3= wx.StaticBitmap(self, -1, png)
        # gatorIco4 = wx.StaticBitmap(self, -1, png)
        gatorIco5 = wx.StaticBitmap(self, -1, png)
        # gatorIco6 = wx.StaticBitmap(self, -1, png)
        title = wx.StaticText(self, wx.ID_ANY, 'How Much Later Till Alligator?')

        font = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        title.SetFont(font)

        description = wx.StaticText(self, wx.ID_ANY, "Enter a source and target animal to find the " + 
            "fewest number of links you have to click to get from the source animal's Wikipedia page to the target animal's Wikipedia " +
            "and find the path between their pages on Wikipedia.")
        description.Wrap(350);

        labelOne = wx.StaticText(self, wx.ID_ANY, 'Source')
        self.inputTxtOne = wx.TextCtrl(self, wx.ID_ANY)

        labelTwo = wx.StaticText(self, wx.ID_ANY, 'Target')
        self.inputTxtTwo = wx.TextCtrl(self, wx.ID_ANY)

        okBtn = wx.Button(self, wx.ID_ANY, 'OK')
        self.Bind(wx.EVT_BUTTON, self.onOK, okBtn)

        self.distanceLabel = wx.StaticText(self, wx.ID_ANY, 'Distance: ?')
        self.IDDFSRuntime = wx.StaticText(self, wx.ID_ANY, 'IDDFS Runtime: ?')
        self.BFSLabel = wx.StaticText(self, wx.ID_ANY, 'BFS Runtime: ?')
        self.path = wx.StaticText(self, wx.ID_ANY, 'Path Between Source and Target Wikipedia Pages')

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        titleSizer = wx.BoxSizer(wx.HORIZONTAL)
        descriptionSizer= wx.BoxSizer(wx.HORIZONTAL)
        inputOneSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputTwoSizer = wx.BoxSizer(wx.HORIZONTAL)
        submitBtnSizer = wx.BoxSizer(wx.HORIZONTAL)
        distSizer = wx.BoxSizer(wx.HORIZONTAL)
        IDDFSSizer = wx.BoxSizer(wx.HORIZONTAL)
        BFSSizer = wx.BoxSizer(wx.HORIZONTAL)
        pathSizer = wx.BoxSizer(wx.HORIZONTAL)

        titleSizer.Add(gatorIco, 0, wx.ALL, 5)
        titleSizer.Add(title, 0, wx.ALL, 5)
        titleSizer.Add(gatorIco2, 0, wx.ALL, 5)

        descriptionSizer.Add(description, 0, wx.ALL, 5)

        inputOneSizer.Add(gatorIco3, 0, wx.ALL, 5)
        inputOneSizer.Add(labelOne, 0, wx.ALL, 5)
        inputOneSizer.Add(self.inputTxtOne, 1, wx.ALL|wx.EXPAND, 5)
        

        inputTwoSizer.Add(gatorIco5, 0, wx.ALL, 5)
        inputTwoSizer.Add(labelTwo, 0, wx.ALL, 5)
        inputTwoSizer.Add(self.inputTxtTwo, 1, wx.ALL|wx.EXPAND, 5)
        

        submitBtnSizer.Add(okBtn, 0, wx.ALL, 5)

        distSizer.Add(self.distanceLabel, 0, wx.ALL, 5)
        IDDFSSizer.Add(self.IDDFSRuntime, 0, wx.ALL, 5)
        BFSSizer.Add(self.BFSLabel, 0, wx.ALL, 5)
        pathSizer.Add(self.path, wx.CENTER, 5)

        self.mainSizer.Add(titleSizer, 0, wx.CENTER)
        self.mainSizer.Add(wx.StaticLine(self,), 0, wx.ALL|wx.EXPAND, 5)
        self.mainSizer.Add(descriptionSizer,0, wx.ALL|wx.CENTER, 5)
        self.mainSizer.Add(wx.StaticLine(self,), 0, wx.ALL|wx.EXPAND, 5)
        self.mainSizer.Add(inputOneSizer, 0, wx.ALL|wx.EXPAND, 5)
        self.mainSizer.Add(inputTwoSizer, 0, wx.ALL|wx.EXPAND, 5)
        self.mainSizer.Add(wx.StaticLine(self), 0, wx.ALL|wx.EXPAND, 5)
        self.mainSizer.Add(submitBtnSizer, 0, wx.ALL|wx.CENTER, 5)
        self.mainSizer.Add(wx.StaticLine(self), 0, wx.ALL|wx.EXPAND, 5)
        self.mainSizer.Add(distSizer, 0, wx.ALL|wx.CENTER, 5)
        self.mainSizer.Add(BFSSizer, 0, wx.ALL|wx.CENTER, 5)
        self.mainSizer.Add(IDDFSSizer, 0, wx.ALL|wx.CENTER, 5)
        self.mainSizer.Add(wx.StaticLine(self), 0, wx.ALL|wx.EXPAND, 5)
        self.mainSizer.Add(pathSizer, 0, wx.ALL|wx.CENTER, 5)

        self.SetSizerAndFit(self.mainSizer)
        self.SetSize((375,455))
        self.Layout()


    def onOK(self, event):
        # Do something
        p = Popen('./graph.out', stdin=PIPE, stdout=PIPE, stderr=PIPE)
        data = self.getData()
        datastring = data[0] + " " + data[1]
        output, err = p.communicate(datastring.encode("utf-8"))
        result = output.decode("utf-8").split("|")
        self.distanceLabel.SetLabel(result[3])
        self.IDDFSRuntime.SetLabel(result[0])
        self.BFSLabel.SetLabel(result[1])
        self.path.SetLabel(result[4])
        self.path.Wrap(350)
        self.Layout()

    def closeProgram(self):
        # self.GetParent() will get the frame which
        # has the .Close() method to close the program
        self.GetParent().Close()

    def getData(self):
        '''
        this here will procure data from all buttons
        '''
        data = []
        data.append(self.inputTxtOne.GetValue())
        data.append(self.inputTxtTwo.GetValue())
        return data

# Run the program
if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
