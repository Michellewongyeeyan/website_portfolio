from flask import Flask, render_template, request, redirect, url_for, session,flash
from flask_sqlalchemy import SQLAlchemy
import web_functions
import os
import time

app = Flask(__name__, template_folder='template')
app.secret_key = 'hello123'

# Dummy user data (replace with a database in a real-world scenario)
users = {'example_user': 'password123'}



@app.route('/')
def home():
    return render_template('index.html', message='Welcome to the Home Page')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if web_functions.create_account(username, password):
            # Log in the user (customize this part based on your needs)
            session['username'] = username
            success = 'Your registration is successful.'
            return render_template('signup.html', success=success)
        else:
            error = 'The username is already used. Please choose a different username.'
            return render_template('signup.html', error=error)

    return render_template('signup.html')

 


@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if web_functions.login(username, password):
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid username or password. Please try again.'
            return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        return f'Welcome to the Dashboard, {username}!'
    else:
        return redirect(url_for('login'))

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        user = request.form['user']
        email = request.form['email']
        message = request.form['message']

        web_functions.comment(user, email, message)
        flash('Message sent successfully!', 'success')
        return redirect(url_for('home'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

# 獲取相對路徑和絕對路徑
__file__ = "."
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = "sqlite:///" + os.path.join(basedir, "db.db")

# 配置數據庫相關參數
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # 禁止 Flask- SQLAlchemy 的修改跟蹤
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE  # 設置數據庫 URI

# 創建 SQLAlchemy 實例
db = SQLAlchemy()

# 初始化 Flask 應用程序與 SQLAlchemy 實例
db.init_app(app)

# 定義 table
class Forum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    forumName =  db.Column(db.String(255), nullable=False)

class ForumContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    forumName = db.Column(db.Integer, nullable=False)
    author =  db.Column(db.String(255), nullable=False)
    content =  db.Column(db.String(255), nullable=False)
    conTime = db.Column(db.String(255), nullable=False)

# db function
## forum
def add_forum(forumName):
    with app.app_context():
        # 檢查論壇名是否已經存在
        if db.session.query(Forum).filter_by(forumName=forumName).first():
            pass
        else:
            # 如果論壇名不存在，則添加新用戶
            forum = Forum(forumName=forumName)
            db.session.add(forum)
            db.session.commit()

def del_forum(forumName):
    with app.app_context():
        # 查找要刪除的論壇
        forum =  db.session.query(Forum).filter_by(forumName=forumName).first()
        if forum:
            # 如果論壇存在，則刪除論壇
            db.session.delete(forum)
            db.session.commit()

def edit_forum(oldForumName, newForumName):
    with app.app_context():
        # 查找要修改的論壇
        forum =  db.session.query(Forum).filter_by(forumName=oldForumName).first()
        if forum:
            # 如果論壇存在，則修改論壇名 同 新名無人用
            if db.session.query(Forum).filter_by(forumName=newForumName).first():
                pass
            else:
                forum.forumName = newForumName
                db.session.commit()

## content
def add_forumContent( forumName, author, content):
    with app.app_context():
        forumContent = ForumContent(
            forumName=forumName,
            author=author,
            content=content,
            conTime=time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime())
        )
        db.session.add(forumContent)
        db.session.commit()


# 創建數據庫表
with app.app_context():
    db.create_all()


@app.route('/forum')
def forum():
    return render_template('forum.html', forums=Forum.query.all())

@app.route('/forum/<forumName>')
def forumContent(forumName):
    return render_template('forumContent.html', forumName=forumName, forumContents=ForumContent.query.filter_by(forumName=forumName).all())

@app.route('/add_forumContent', methods=['POST'])
def addForumContent():
    forumName = request.form.get('forumName')
    author = request.form.get('author')
    content = request.form.get('content')

    if forumName and author and content:
        with app.app_context():
            forumContent = ForumContent(
                forumName=forumName,
                author=author,
                content=content,
                conTime=time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime())
            )
            db.session.add(forumContent)
            db.session.commit()
        return redirect(f'/forum/{forumName}')
    










if __name__ == '__main__':
    app.run(debug=True)


