from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

QUIZ = [
    "pythonは何に使うもの？1.算数 2.プログラミング 3.トイレ",
    "pythonの変数はなにができる? 1.データの保存 2.文字の入力 3.ゲームの破壊",
    "pythonでprintを使うと何ができる? 1.ウィンドウの表示 2.文字の表示 3.今度こそゲーム破壊",
    "pythonでif文を使うと何ができる? 1.条件に応じた処理の実行 2.写真の表示 3.文字をバグらせる",
    "pythonで配列を使うと何ができる? 1.文字の色を変える 2.複数のデータの管理 3.文字を虹色にする",
    "pythonは結局何ができる? 1.アカウントの制作 2.ウェブやゲームの開発 3.未来を見る",
]

ANS = ["2", "1", "2", "1", "2", "2"]

@app.route('/', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        ans = request.form['answer']
        quiz_no = int(request.form['quiz_no'])
        score = int(request.form['score'])
        if ans == ANS[quiz_no]:
            score += 1
        quiz_no += 1
        if quiz_no < len(QUIZ):
            return render_template('index.html', quiz=QUIZ[quiz_no], quiz_no=quiz_no, score=score)
        else:
            return render_template('index.html', quiz="お疲れ様でした。", quiz_no=quiz_no, score=score, end=True)
    else:
        return render_template('index.html', quiz=QUIZ[0], quiz_no=0, score=0)

if __name__ == "__main__":
    app.run(debug=True)
