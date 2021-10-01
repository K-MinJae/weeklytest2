from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.dbtest2


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post', methods=['POST'])
def save_post():
    # idx_receive = request.form['idx_give']
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']
    # regdate_receive = request.form['regdate_give']

    doc = {
        # 'idx': idx_receive,
        'title': title_receive,
        'content': content_receive,
        # 'regdate': regdate_receive
    }
    db.posts.insert_one(doc)

    return {"result": "success"}


@app.route('/post', methods=['GET'])
def get_post():
    posts = list(db.posts.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'posts': posts})

    return {"result": "success"}


@app.route('/post', methods=['DELETE'])
def delete_post():
    idx_receive = request.form['idx_give']
    db.posts.delete_one({'name': idx_receive})

    return {"result": "success"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)