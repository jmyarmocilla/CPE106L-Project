from tkinter import*
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import read_database as readDB

root = Tk()
root.title("Twiter Database Analysis")
root.config(bg='skyblue')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 1250
height = 400
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.grid_columnconfigure(0, weight=1)

Body = Frame(root, width=700, height=300, bd=8, relief="raise", bg='skyblue')
Body.pack(anchor=CENTER, expand=TRUE)

#LIST WIDGET
scrollbary = Scrollbar(Body, orient=VERTICAL)
scrollbarx = Scrollbar(Body, orient=HORIZONTAL)
tree = ttk.Treeview(Body, columns=("id", "user", "screen_name", "created_at", 
            "full_text", "source", "text", "is_quote_status", "quote_count", "reply_count", 
            "retweet_count", "favorite_count"))
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y, expand=TRUE)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X, expand=TRUE)
tree.heading('id', text="id", anchor=W)
tree.heading('user', text="user", anchor=W)
tree.heading('screen_name', text="screen_name", anchor=W)
tree.heading('created_at', text="created_at", anchor=W)
tree.heading('full_text', text="full_text", anchor=W)
tree.heading('source', text="source", anchor=W)
tree.heading('text', text="text", anchor=W)
tree.heading('is_quote_status', text="is_quote_status", anchor=W)
tree.heading('reply_count', text="reply_count", anchor=W)
tree.heading('retweet_count', text="retweet_count", anchor=W)
tree.heading('favorite_count', text="favorite_count", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=125)
tree.column('#2', stretch=NO, minwidth=0, width=125)
tree.column('#3', stretch=NO, minwidth=0, width=110)
tree.column('#4', stretch=NO, minwidth=0, width=125)
tree.column('#5', stretch=NO, minwidth=0, width=125)
tree.column('#6', stretch=NO, minwidth=0, width=125)
tree.column('#7', stretch=NO, minwidth=0, width=75)
tree.column('#8', stretch=NO, minwidth=0, width=75)
tree.column('#9', stretch=NO, minwidth=0, width=75)
tree.column('#10', stretch=NO, minwidth=0, width=75)
tree.column('#11', stretch=NO, minwidth=0, width=75)
tree.column('#12', stretch=NO, minwidth=0, width=75)
tree.pack()

#METHODS
def treeViewAll():
    for i in tree.get_children():
        tree.delete(i)
    readDB.twitterData()
    readDB.con
    readDB.cur.execute("SELECT * FROM tweets_users_normalized")
    fetch = readDB.cur.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], 
                                        data[3], data[4], data[5],
                                        data[6], data[7], data[8], data[9], data[10], data[11]))


def treeSortRetweets():
    for i in tree.get_children():
        tree.delete(i)
    readDB.twitterData()
    readDB.con
    readDB.cur.execute("SELECT * FROM tweets_users_normalized ORDER BY retweet_count DESC;")
    fetch = readDB.cur.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], 
                                        data[3], data[4], data[5],
                                        data[6], data[7], data[8], data[9], data[10], data[11]))


def treeSortFavorites():
    for i in tree.get_children():
        tree.delete(i)
    readDB.twitterData()
    readDB.con
    readDB.cur.execute("SELECT * FROM tweets_users_normalized ORDER BY favorite_count DESC;")
    fetch = readDB.cur.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], 
                                        data[3], data[4], data[5],
                                        data[6], data[7], data[8], data[9], data[10], data[11]))

def iExit():
    iExit = tkMessageBox.askyesno("Twitter Database Analysis", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return  
    readDB.cur.close()
    readDB.con.close()  

