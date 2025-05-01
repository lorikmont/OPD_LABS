from collections import Counter
from flask import Flask, request, render_template, redirect, url_for


app = Flask(__name__)

def most_frequent(text):
    lst = text.split()
    w_counts = Counter(lst)
    return w_counts.most_common(1)[0][0]


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)


        if file:
            text = file.read().decode('utf-8')
            result = most_frequent(text)
            return render_template('index.html', result=result)

    return render_template('index.html', result=None)


if __name__ == '__main__':
    app.run(debug=True)





