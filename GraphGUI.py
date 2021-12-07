import wx
import os 
from subprocess import Popen, PIPE

#This Python based GUI utlizes the wxPython library to create an interactive display
#The os, Popen, and PIPE libraries are used to communicate with the graph.out file 
#which was produced from the files found in the Graph folder

class MyApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)
        
        #Initializes fram
        self.InitFrame()
    
    def InitFrame(self):
        frame = MyFrame()
        frame.Show()


class MyFrame(wx.Frame):
    def __init__(self, title="Project 3", pos=(100,100)):
        super().__init__(None, title=title, pos=pos)
        self.OnInit()

    # Initializes frames contents
    def OnInit(self):
        #Creates a panel for MyForm type
        self.panel = MyForm(self)
        self.Fit()

class MyForm(wx.Panel):

    def __init__(self, parent ):
        super().__init__(parent=parent)

        #Creates multiple bitmaps of Gator.png
        png = wx.Image('Images/Gator.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        gatorIco = wx.StaticBitmap(self, -1, png)
        gatorIco2 = wx.StaticBitmap(self, -1, png)
        gatorIco3= wx.StaticBitmap(self, -1, png)
        gatorIco4 = wx.StaticBitmap(self, -1, png)
        
        #Creates title and increases font size
        title = wx.StaticText(self, wx.ID_ANY, 'How Much Later Till Alligator?')
        font = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        title.SetFont(font)

        #Creates description and sets it to wrap at a width of 350 pixels
        description = wx.StaticText(self, wx.ID_ANY, "Enter a source and target animal to" +
            " find the fewest number of links you have to click to get from the source animal's" + 
            " Wikipedia page to the target animal's Wikipedia " + "and find the path between " +
            "their pages on Wikipedia.")
        description.Wrap(350);

        #Creates label and textbox for inputting source Wikipedia page
        labelOne = wx.StaticText(self, wx.ID_ANY, 'Source')
        self.inputTxtOne = wx.TextCtrl(self, wx.ID_ANY)

        #Creates label and textbox for inputting target Wikipedia page
        labelTwo = wx.StaticText(self, wx.ID_ANY, 'Target')
        self.inputTxtTwo = wx.TextCtrl(self, wx.ID_ANY)

        #Creates button and establishes link with onOk function, which runs when button is pressed
        okBtn = wx.Button(self, wx.ID_ANY, 'OK')
        self.Bind(wx.EVT_BUTTON, self.onOK, okBtn)

        #Creates labels which reflect the distance, runtime, and path returned from graph.out
        self.distanceLabel = wx.StaticText(self, wx.ID_ANY, 'Distance: ?')
        self.IDDFSRuntime = wx.StaticText(self, wx.ID_ANY, 'IDDFS Runtime: ?')
        self.BFSLabel = wx.StaticText(self, wx.ID_ANY, 'BFS Runtime: ?')
        self.path = wx.StaticText(self, wx.ID_ANY, 'Path Between Source and Target Wikipedia Pages')

        #Creates sizers for each section to deal with layout management
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

        #Each component is added to their repsective sizer
        titleSizer.Add(gatorIco, 0, wx.ALL, 5)
        titleSizer.Add(title, 0, wx.ALL, 5)
        titleSizer.Add(gatorIco2, 0, wx.ALL, 5)

        descriptionSizer.Add(description, 0, wx.ALL, 5)

        inputOneSizer.Add(gatorIco3, 0, wx.ALL, 5)
        inputOneSizer.Add(labelOne, 0, wx.ALL, 5)
        inputOneSizer.Add(self.inputTxtOne, 1, wx.ALL|wx.EXPAND, 5)
        

        inputTwoSizer.Add(gatorIco4, 0, wx.ALL, 5)
        inputTwoSizer.Add(labelTwo, 0, wx.ALL, 5)
        inputTwoSizer.Add(self.inputTxtTwo, 1, wx.ALL|wx.EXPAND, 5)
        

        submitBtnSizer.Add(okBtn, 0, wx.ALL, 5)

        distSizer.Add(self.distanceLabel, 0, wx.ALL, 5)
        IDDFSSizer.Add(self.IDDFSRuntime, 0, wx.ALL, 5)
        BFSSizer.Add(self.BFSLabel, 0, wx.ALL, 5)
        pathSizer.Add(self.path, wx.CENTER, 5)

        #All subcomponent sizers are added to mainSizer, which deals with overall layout
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

        #Sizer is set and an initial fit is established
        self.SetSizerAndFit(self.mainSizer)
        self.SetSize((375,455))
        self.Layout()


    #Function runs when button is clicked
    def onOK(self, event):
        #Establishes connection with graph.out file
        p = Popen('./graph.out', stdin=PIPE, stdout=PIPE, stderr=PIPE)
        #Gets data from textboxes using getData function
        data = self.getData()
        datastring = data[0] + " " + data[1]
        #Sends inputted source and target pages into graph.out
        output, err = p.communicate(datastring.encode("utf-8"))
        #Dispays output from graph.out to user
        result = output.decode("utf-8").split("|")
        self.distanceLabel.SetLabel(result[3])
        self.IDDFSRuntime.SetLabel(result[0])
        self.BFSLabel.SetLabel(result[1])
        self.path.SetLabel(result[4])
        self.path.Wrap(350)
        self.Layout()

    #Calls the Frame method of Close() to end the program
    def closeProgram(self):
        self.GetParent().Close()

    #Retrives data from inputTxtOne and inputTxtTwo
    def getData(self):
        data = []
        data.append(self.inputTxtOne.GetValue())
        data.append(self.inputTxtTwo.GetValue())
        return data

# Runs the program
if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
