from flask import Flask, render_template

app = Flask(__name__)

# 假设您有一个水果列表
fruits = ['苹果', '香蕉', '橙子', '葡萄']


@app.route('/')
def index():
    return render_template('index.html', fruits=fruits)


if __name__ == '__main__':
    app.run(debug=True)
