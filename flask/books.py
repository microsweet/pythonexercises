from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/flask_books'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = '123'
db = SQLAlchemy(app)
'''
1. 配置数据库
2. 添加书和作者模型
3. 添加数据
4. 使用模板显示数据库查询的数据
5. 使用WTF显示表单
6. 实现相关的增删改查
'''


# 作者模型
class Author(db.Model):
    # 表名
    __tablename__ = 'authors'

    # 字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)

    # 关系引用
    books = db.relationship('Book', backref='Author')

    def __repr__(self):
        return 'Author: %s' % self.name


# 书籍模型
class Book(db.Model):
    # 表名
    __tablename__ = 'books'

    # 字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)

    # 外键
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    def __repr__(self):
        return 'Book: %s %s' % (self.name, self.author_id)


# 自定义表单类
class AuthorForm(FlaskForm):
    author = StringField('作者', validators=[DataRequired()])
    book = StringField('书籍', validators=[DataRequired()])
    submit = SubmitField('提交')


@app.route('/', methods=['GET', 'POST'])
def index():
    # 创建自定义表单类
    author_form = AuthorForm()
    '''
    验证逻辑：
    1. 调用WTF的函数实现验证
    2. 验证通过获取数据
    3. 判断作者是否存在
    4. 如果作者存在，判断书籍是否存在，没有重复数据就添加数据，
    如果重复，就提示错误
    5. 如果作者不存在，添加作者和书籍
    6. 验证不通过提示错误
    '''

    # 1. 调用WTF的函数实现验证
    if author_form.validate_on_submit():
        # 2. 验证通过获取数据
        author_name = author_form.author.data
        book_name = author_form.book.data

        # 3. 判断作者是否存在
        author = Author.query.filter_by(name=author_name).first()
        print(author)

        # 4. 如果作者存在
        if author:
            # 判断书籍是否存在，没有重复书籍就添加数据，重复就提示错误
            book = Book.query.filter_by(name=book_name).first()

            # 重复提示错误
            if book:
                flash('已存在同名书籍')
            else:
                # 不重复，添加书籍
                try:
                    new_book = Book(name=book_name, author_id=author.id)
                    db.session.add(new_book)
                    db.session.commit()
                except Exception as e:
                    print(e)
                    flash('添加书籍失败')
                    db.session.rollback()
        else:
            # 5. 如果作者不存在，添加作者和书籍
            try:
                new_author = Author(name=author_name)
                db.session.add(new_author)
                db.session.commit()
                new_book = Book(name=book_name, author_id=new_author.id)
                db.session.add(new_book)
                db.session.commit()
            except Exception as e:
                print(e)
                flash('添加作者和书籍失败')

    else:
        if request.method == 'POST':
            flash('参数不全')

    # 查询所有作者信息，传递给模板
    authors = Author.query.all()

    return render_template('books.html', authors=authors, form=author_form)


# 删除书籍 --> 网页中删除 --> 传参给路由 --> 路由接受参数
@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    # 1. 查询数据库，是否有该ID的书，有就删除，没有提示错误
    book = Book.query.get(book_id)
    # 2. 如果有就删除
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('删除书籍出错')
            db.session.rollback()
    else:
        # 3. 没有提示错误
        flash('书籍找不到')

    # 如何返回当前网址 --> 重定向
    # return redirect('www.baidu.com')
    # redirect：重定向，需要传入网络/路由地址
    # url_for('index')：需要传入视图函数名称，返回该视图函数对应的路由地址
    return redirect(url_for('index'))


# 删除作者
@app.route('/delete_author/<author_id>')
def delete_author(author_id):
    # 查询数据库，是否有该ID的作者，如果有就删除（先删除书，再删除作者）
    # 1. 查询数据库
    author = Author.query.get(author_id)

    # 2. 有就删除
    if author:
        try:
            # 查询之后直接删除
            Book.query.filter_by(author_id=author.id).delete()

            # 删除作者
            db.session.delete(author)
            db.session.commit()

        except Exception as e:
            print(e)
            flash('删除作者出错')
            db.session.rollback()
    else:
        flash('作者找不到')

    return redirect(url_for('index'))


if __name__ == '__main__':

    db.drop_all()
    db.create_all()

    au1 = Author(name='张三')
    au2 = Author(name='李四')
    db.session.add_all([au1, au2])
    db.session.commit()

    book1 = Book(name='长生界', author_id=au1.id)
    book2 = Book(name='遮天', author_id=au1.id)
    book3 = Book(name='星辰变', author_id=au2.id)
    db.session.add_all([book1, book2, book3])
    db.session.commit()

    app.run(debug=True)
