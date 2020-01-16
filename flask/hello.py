from flask import Flask, flash, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)
app.secret_key = '111'
# 数据库地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1/flask'
# 跟踪数据库修改 --> 建议关闭
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello, World'


# 可以给变量指定规则
'''
string  （缺省值） 接受任何不包含斜杠的文本
int     接受正整数
float   接受正浮点数
path    类似 string ，但可以包含斜杠
uuid    接受 UUID 字符串
'''


@app.route('/variable/<int:variable>')
def variable(variable):
    return 'var: %s' % variable


@app.route('/index')
def index():
    url_str = 'www.baidu.com'

    my_list = [1, 2, 3]

    my_dict = {'name': '百度', 'url': 'www.baidu.com'}
    return render_template('index.html',
                           url_str=url_str,
                           my_list=my_list,
                           my_dict=my_dict)


'''
目的：实现一个简单的登录逻辑处理
1.路由需要有get和post两种请求方式 --> 需要判断请求方式
2.获取请求的参数
3.判断参数是否填写 & 密码是否相同
4.如果判断都没有问题，就返回一个success
'''
'''
给模板传递消息
flash --> 需要对内容加密，需要设置secret_key, 做加密消息的混淆
模板中需要遍历消息
'''


@app.route('/login', methods=['GET', 'POST'])
def login():
    # request: 请求对象 --> 获取请求方式、数据

    # 1.判断请求方式
    if request.method == 'POST':
        # 2.获取请求的参数
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        print(username)

        # 3.判断参数是否填写 & 密码是否相同
        if not all([username, password, password2]):
            # print('参数不完整')
            flash('参数不完整')
        elif password != password2:
            flash('密码不一致')
        else:
            return 'success'

    return render_template('login.html')


'''
WTF验证表单
'''


# 自定义表单类
class LoginForm(FlaskForm):
    username = StringField('用户名：', validators=[DataRequired()])
    password = PasswordField('密码：', validators=[DataRequired()])
    password2 = PasswordField(
        '确认密码：', validators=[DataRequired(),
                             EqualTo('password', '密码填入的不一致')])
    submit = SubmitField('提交')


@app.route('/form', methods=['POST', 'GET'])
def form():
    login_form = LoginForm()

    # 1.判断请求方式
    if request.method == 'POST':
        # 2.获取请求的参数
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        # 3.WTF验证参数
        if login_form.validate_on_submit():
            return 'success'
        else:
            flash('参数有误')

    return render_template('form.html', form=login_form)


'''
两张表
角色（管理员/普通用户）
用户（角色ID）
'''


# 数据库模型，需要继承db.Model
class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'

    # 定义字段
    # db.Column表示是一个字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)

    # 在一的一方写关联
    # users = db.relationship('User')：表示和User模型发生了关联，增加一个users属性
    # backref='role'：表示role是User要用的属性
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role: %s %s>' % (self.id, self.name)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    email = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))
    # db.ForeignKey 表示外键，表名.id
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    # User希望有role属性，但是这个属性的定义，需要在另一个模型中定义

    def __repr__(self):
        return '<User: %s %s %s %s> \n' % (self.id, self.name, self.email,
                                           self.password)


if __name__ == '__main__':
    # 删除表
    db.drop_all()

    # 创建表
    db.create_all()

    # 插入数据
    ro1 = Role(name='admin')
    db.session.add(ro1)
    db.session.commit()
    ro2 = Role(name='user')
    db.session.add(ro2)
    db.session.commit()

    us1 = User(name='wang',
               email='wang@163.com',
               password='123',
               role_id=ro1.id)
    us2 = User(name='li', email='li@163.com', password='234', role_id=ro2.id)
    us3 = User(name='zhang',
               email='zhang@163.com',
               password='345',
               role_id=ro2.id)
    us4 = User(name='sun', email='sun@163.com', password='456', role_id=ro1.id)
    us5 = User(name='qian',
               email='qian@163.com',
               password='789',
               role_id=ro2.id)
    us6 = User(name='zhao',
               email='zhao@163.com',
               password='sss',
               role_id=ro2.id)
    db.session.add_all([us1, us2, us3, us4, us5, us6])
    db.session.commit()

    app.run(debug=True)
