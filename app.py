from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///songs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

Post = db.Table('post',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('image_file', db.String(120), nullable=False),
    db.Column('caption', db.String(500), nullable=False),
    db.Column('created_at', db.DateTime, default=datetime.utcnow),
    db.Column('like_count', db.Integer, default=0)
)

@app.route('/')
def index():
    # TO DO  — ADD route and function for index


@app.route('/add', methods=['GET', 'POST'])
def add_post():
    # TO DO  - ADD route and function for adding a new post

if __name__ == '__main__':
    app.run(debug=True)
