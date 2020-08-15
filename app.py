from flask import Flask, render_template, redirect, request, url_for
from sqlalchemy import or_, func
from dbs import db
import config
from models import student, socre

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/',methods=['post','get'])
def index():
    # db.drop_all()
    db.create_all()
    content = db.session.query(socre).all()
    if request.method=='POST':
        keys=request.form.get('keys')
        return redirect(url_for('search',keys=keys))
    return render_template('index.html', content=content)


@app.route('/add/', methods=['post', 'get'])
def add():
    if request.method == 'POST':
        name = request.form.get('name')
        python = request.form.get('python')
        java = request.form.get('java')
        english = request.form.get('english')
        if name and python and java and english:
            total = int(python) + int(java) + int(english)
            db.session.add(student(name=name))
            a = db.session.query(student).filter(student.name == name).first()
            db.session.add(socre(python=python, java=java, english=english, total=total, s_student=a.id))
            db.session.commit()
            print('添加成功')
            return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/dels/')
def dels():
    id = request.args.get('id')
    db.session.query(socre).filter(socre.s_student == id).delete()
    db.session.query(student).filter(student.id == id).delete()
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/edit/', methods=['post', 'get'])
def edit():
    id = request.args.get('id')
    if request.method == 'POST':
        name = request.form.get('name')
        python = request.form.get('python')
        java = request.form.get('java')
        english = request.form.get('english')
        if name and python and java and english:
            total = int(python) + int(java) + int(english)
            student.query.filter(student.id == id).update({'name': name})
            socre.query.filter(socre.s_student == id).update(
                {'python': python, 'java': java, 'english': english, 'total': total, 's_student':id})
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('eidt.html')

@app.route('/search/',methods=['post','get'])
def search():
    if request.method=='POST':
        keys = request.form.get('keys')
        a = student.query.filter(or_(student.name.like('%{}%'.format(keys)),student.id==keys)).all()
        if a is not None:
            return render_template('search.html',a=a)
        return render_template('search.html')
    return render_template('search.html')

@app.route('/sortt/',methods=['post','get'])
def sortt():
    if request.method=='POST':
        if request.form.get('python'):
            a=socre.query.order_by(db.desc(socre.python))
            print(a)
            return render_template('sortt.html',a=a)
        if request.form.get('java'):
            a=socre.query.order_by(db.desc(socre.java))
            print(a)
            return render_template('sortt.html',a=a)
        if request.form.get('english'):
            a=socre.query.order_by(db.desc(socre.english))
            print(a)
            return render_template('sortt.html',a=a)
        if request.form.get('total'):
            a=socre.query.order_by(db.desc(socre.total))
            print(a)
            return render_template('sortt.html',a=a)
    return render_template('sortt.html')

if __name__ == '__main__':
    app.run()
