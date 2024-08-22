import tkinter
import tkinter.messagebox

def message(x,y,t):#影付き文字を表示する関数
    f = ("Times New Roman",17,"bold")
    cvs.delete("msg")
    cvs.create_text(x+1,y+1, text=t,font=f,fill="black",tag="msg")
    cvs.create_text(x, y, text=t, font=f,fill="yellow",tag="msg")

def button():#ボタンを押したときの処理
    global quiz_no,score
    if quiz_no==6: return
    if quiz_no==-1:
        quiz_no =0
        message(512,520,"第"+str(quiz_no+1)+"問\n"+QUIZ[quiz_no])
        return
    ans = ent.get()
    if ans=="":
        tkinter.messagebox.showinfo("","答えを入力してください。")
        return
    if ans==ANS[quiz_no]:
        tkinter.messagebox.showinfo("","正解です。")
        score = score + 1
    else:
        tkinter.messagebox.showinfo("","違います。答えは"+ANS[quiz_no])
    quiz_no = quiz_no + 1
    if quiz_no==6:
        message(512,520,"お疲れ様でした。")
        tkinter.messagebox.showinfo("ゲーム終了",str(score)+"問、正解しました。")
        return
    ent.delete(0,tkinter.END)
                
    message(512,520,"第"+str(quiz_no+1)+"問\n"+QUIZ[quiz_no])     
root = tkinter.Tk()
root.title("クイズゲーム")
root.resizable(False, False)
cvs = tkinter.Canvas(root, width=1024, height=680)
bg = tkinter.PhotoImage(file="image/bg.png")
cvs.create_image(512, 340, image=bg)
cvs.pack()
ent = tkinter.Entry(root)
ent.place(x=300, y=620, width=200, height=30)
but = tkinter.Button(root, text="OK",command=button)
but.place(x=600, y=620, width=80, height=30)
message(512, 520,"クイズを始めます。")
quiz_no = -1
score = 0
QUIZ = [
"pythonは何に使うもの？\n１算数２プログラミング３トイレ",
"pythonの変数はなにができる?\n1データの保存２文字の入力３ゲームの破壊",
"pythonでprintを使うと何ができる?\n１ウィンドウの表示２文字の表示３今度こそゲーム破壊",
"pythonでif文を使うと何ができる？\n１条件に応じた処理の実行２写真の表示３文字をバグらせる",
"pythonで配列を使うと何ができる？\n１文字の色を変える２複数のデータの管理３文字を虹色にする",
"pythonは結局何ができる？\n１アカウントの制作２ウェブやゲームの開発３未来を見る",
]
ANS = [
"2",
"1",
"2",
"1",
"2",
"2"
]

root.mainloop()
