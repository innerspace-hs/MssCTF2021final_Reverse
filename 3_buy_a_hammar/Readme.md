# 题目名称

py_store

# Category

reverse

# Difficulty(1-4)

 3

# key words

- python的基本使用

# Description

赌狗最后一无所有（I have hidden something, find it!!!）

`python chall.py` 

题目环境 `python3.9.6`

以防参赛者没有python的运行环境，题目附件中会给出python3.9.6的安装包

# hint

- `import magic`  and `dir(magic)`
- def check_box(*a*: int) -> str

# Environment

python3.9.6

# wp

pyd文件是由python文件编译成的库文件，可以用ida逆向，但是难度非常大。

print(dir(magic))可以看到magic.pyd中的所有函数

```python
['__builtins__','__doc__','__file__','__loader__','__name__','__package__','__spec__','__test__','check_box','hidden_func','hidden_number_guess','menu','my_python_shop','random','show','start','sys','time']
```

结合题目描述"I have hidden something"，重点查看hidden_func，与hidden_number_guess

```python
import magic
magic.hidden_func()
```

可以看到如下输出

```
QwQ, you find me.
Do you want the flag?
wwwww, I won't give it to you so easily!
How about playing another game?
yeah, a number guess game!
I have a favorite number, and it will never change.
Now, guess it!
give me a number between 1 and 999999
And I will throw it to my check box
Input the character 'q' to exit the game
```

随便输入一个数字，发现如下输出

```
WRONG!!!!
TRY AGAIN!!!
```

暂时还不知道怎么爆破，于是看一看check_box函数

```python
magic.check_box()
```

可以看到python爆error了

```
TypeError: check_box() takes exactly one argument (0 given)
```

于是给check_box一个argument

```python
magic.check_box(123)
```

可以发现输出

```
'WRONG!!!!\nTRY AGAIN!!!'
```

可以发现check_box函数的返回值是一个字符串，并且可以猜测hidden_func中调用了check_box来进行验证，于是可以写脚本爆破

```python
import magic
for i in range(1,999999):
    if "WRONG!!!!" not in magic.check_box(i) :
        print(i)
        print(magic.check_box(i))
```

运行脚本可以得到flag

```
210515
Cong
mssctf{mAy_a11_th3_b3auTy_Be_b1essed}
```

