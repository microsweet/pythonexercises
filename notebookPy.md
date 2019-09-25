### 变量
|   | 变量规则                                                                                                                                             |
|---|------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | 变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，</br>但不能以数字打头，例如，可将变量命名为message_1，</br>但不能将其命名为1_message。 |
| 2 | 变量名不能包含空格，但可使用下划线来分隔其中的单词。</br>例如，变量名greeting_message可行，但变量名greetingmessage会引发错误。                       |
| 3 | 不要将Python关键字和函数名用作变量名，</br>即不要使用Python保留用于特殊用途的单词，如print。                                                         |
| 4 | 变量名应既简短又具有描述性。</br>例如，name比n好，student_name比s_n好，</br>name_length比length_of_persons_name好。                                  |
| 5 | 慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0                                                                                             |

### 字符串
| 方法     | 作用                 |
| ----     | ----                 |
| title()  | 以首字母大写显示单词 |
| upper()  | 全部大写             |
| lower()  | 全部小写             |
| rstrip() | 去除尾部空白         |
| lstrip() | 去除首部空白         |
| strip()  | 去掉首尾空白         |

### 数字

| 方法    | 作用                                                                      |
|---------|---------------------------------------------------------------------------|
| str()   | 方法转换字符串                                                            |
| range() | 函数生成一系列数字（range(1,5)，可以指定步长range(2,11,2)生成10以内偶数） |
| int()   | 将字符串转换为整数                                                        |
| float() | 将字符串转换为浮点数                                                      |


### 列表
|   | 内容                                               |
|---|----------------------------------------------------|
| 1 | 列表用[]表示，如：['car', 'bicycle']               |
| 2 | 列表是有序集合                                     |
| 3 | 索引从0开始                                        |
| 4 | 从列表反向取值用负数                               |
| 5 | for循环遍历list（for value in range(1,5)）         |
| 6 | 切片是list的子集（list[0:3]，通过list[:]复制list） |
| 7 | 元组使用()标识，元组类似列表但元素不可修改         |

| 方法      | 作用                                                                                       |
|-----------|--------------------------------------------------------------------------------------------|
| append()  | 列表末尾添加                                                                               |
| insert()  | 列表中插入值（需要指定新元素索引，insert(0,'sss')                                          |
| del       | 删除列表中的元素（须知要删除元素的索引，del list[index])                                   |
| pop()     | 弹出列表中的元素(默认弹出最后一个元素，</br>添加索引后可弹出任意位置元素，弹出后列表中消失 |
| remove()  | 只知道元素的值不知道索引时用该方法删除元素</br>（remove(值),remove只能删除第一个）         |
| sort()    | 对list永久排序                                                                             |
| sorted()  | 对list临时排序                                                                             |
| reverse() | 反转list排序                                                                               |
| len()     | 确定列表长度                                                                               |

list(range(1,5))生成一个数字列表

### 字典
python中字典是键—值对，如：apple={'color': 'red', 'shap': 'circle'}

### 循环
| 名称     | 简介                       |
|----------|----------------------------|
| for      | for value in list:         |
| while    | while flag:                |
| break    | 终止循环                   |
| continue | 跳出本次循环继续执行下一次 |

### 函数
|   | 描述                                             |
|---|--------------------------------------------------|
| 1 | def funcname():                                  |
| 2 | def funcname(value1,value2)                      |
| 3 | def funcname(value1='str', value2)待默认值的形参 |

```
2. 传递参数时有两种方式：位置实参、关键字实参：</br>
def funcname(value1, value2):
    print(value1 + value2)

funcname('1', '2') 结果为：12
funcname(value2='2', value='1') 结果为：12
```

### 类
* 创建一个类
```
class classname():
    def __init__(self, var1, var2):
        self.var1 = var1
	self.var2 = var2
	self.var3 = defaultVal
```
* 继承
```
class classname(superclassname):
    def __init__(self, var1, var2):
        super().__init__(var1, var2)
```

* 一个类的属性也可以是一个类
```
class classname1():
    --snip--
class classname2():
    def __init__(self):
        self.var1 = classname1()
```
* 导入类
```
from module_name from class_name

import 模块(使用时需要module_name.class_name)

from module_name import *(不推荐使用，1、没有明确指出使用了模块中的哪些类；2、容易引起类名重复)
```

### 文件
1. 读取整个文件
```
with open(file_path) as file_object:
    var = file_object.read()
```
2. 逐行读取
```
with open(file_path) as file_object:
    for line in file_object:
        print(line)
```
3. 创建包含文件各行的列表
```
with open(file_path) as file_object:
    lines = file_object.readlines()
```
4. 写入文件
open(file_path, type)
>省略type时默认为读取模式

| type | 模式                             |
|------|----------------------------------|
| 'r'  | 读取模式                         |
| 'w'  | 写入模式 (写入时会清空原文件）   |
| 'a'  | 附加模式（写入时不会清空原文件） |
| 'r+' | 读取写入                         |
```
with open(file_path, 'w') as file_object:
    file_object.write('sssss')
```
>写入json：
>>import json</br>
>>json.dump(var, file_object)</br>

>读取json：
>>json.load(file_object)

### 异常
```
try:
    part_1 
except error_type:
    part_2
else:
    part_3

可能会出现异常的代码块放到part_1
出现异常后执行的代码块放到part_2(可以pass跳过)
part_1成功后执行的代码块放到part_3
```

| error_type        | 释义       |
|-------------------|------------|
| ZeroDivisionError | 除数为0    |
| FileNotFoundError | 文件未找到 |


