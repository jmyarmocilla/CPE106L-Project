from tkinter import*
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import read_database as readDB
from TreeLogic import*


#METHODS
treeViewAll
treeSortRetweets
treeSortFavorites
iExit

#FRAME
Top = Frame(root, width=400, height=50, bd=8, relief="raise")
Top.pack(anchor=CENTER)
Button_Group=Frame(root, width=200, height=50, padx=15, pady=15, bg='black')
Button_Group.pack(anchor=CENTER)
Buttons = Frame(Button_Group, width=200, height=76, bg='skyblue')
Buttons.pack(anchor=CENTER)
Bottom=Frame(root, width=400, relief="raise")
Bottom.pack()

#LABEL WIDGET
txt_title = Label(Top, width=40, font=('arial', 24, 'bold'), text = "Twitter Database Analysis", fg='blue')
txt_title.pack()
botLabel = Label(Bottom, width=50, font=('arial', 14, 'bold'), text = "Database used: Tweets collected containing keyword 'deepfake'", bg='skyblue')
botLabel.pack()

#BUTTONS WIDGET
buttonShowAll = Button(Buttons, width=15, text="Display All", command=treeViewAll)
buttonShowAll.grid(row=0,column=0)
buttonSortRetweet = Button(Buttons, width=15, text="Sort by Retweets", command=treeSortRetweets)
buttonSortRetweet.grid(row=0,column=2)
buttonSortFavorites = Button(Buttons, width=15, text="Sort by Favorites", command=treeSortFavorites)
buttonSortFavorites.grid(row=0,column=4)
buttonExit = Button(Buttons, width=15, text="Exit", command=iExit)
buttonExit.grid(row=0,column=6)


#INITIALIZATION

if __name__ == '__main__':
    root.mainloop()
   
