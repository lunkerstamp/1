<!DCTYPE>
<html>
<head>
    <meta charset="UTF-8">
    <title>课程外脑</title>
    <style>
        body {
            line-height: 1.6;
            padding: 20px;
        }

        h1 {
            text-align: center;
            color: black;
        }

        h2 {
            color: blue;
        }

        pre {
            background-color: skyblue;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }

        img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 20px auto;
        }
    </style>
</head>

<body>
    <h1>Python知识点与图片展示</h1>
    <h2>基础概念</h2>
    <p>·代码（块）、输入、输出、变量、常量、转义字符</p >
    <p>·整型、浮点型、逻辑运算、位运算、布尔数、布尔表达式、关键字、判断、缩进、（非）空值、嵌套</p >
    <p>·数据结构、索引、切片、追加、字典</p >
    <p>·循环、遍历、条件循环、边界条件、死循环、break与continue</p >
    <p>·匿名、形参、实参、内置函数、必选参数、匿名函数、递归</p >
    <p>·类与对象、属性与方法、模块、路径、文件后缀、网络爬虫、数据分析、数据可视化</p >
    <img src="C:\Users\21714\Desktop\知识梳理\python基础.png" alt="知识梳理图" width="1000px" height="800px">
    <h2>数据类型</h2>
    <p>包含数值、序列、文本序列、映射、集合类型</p >
    <p><b>*列表、元组、集合、字典</b></p >
    <img src="C:\Users\21714\Desktop\知识梳理\列表、元组、集合、字典.png" alt="知识梳理图" width="1000px" height="800px">
    <img src="C:\Users\21714\Desktop\知识梳理\列表、元组、集合、字典（2）.png" alt="知识梳理图" width="1000px" height="800px">
    <h2>流程控制</h2>
    <p>for循环、while循环、if-elif-else分支语句 </p>
    <p>例：</p >
    <pre><code>for item in my_list:
    print(item)
</code></pre>
    <pre><code>while True:
    print(True)
</code></pre>
    <pre><code>i = int(input())
if i < 0:
    print("负数")
elif i = 0:
    print("零")
else:
    print("正数")
</code></pre>
    <img src="C:\Users\21714\Desktop\知识梳理\流程控制.png" alt="知识梳理图" width="1000px" height="800px">
    <h2>函数</h2>
    <p>以 <code>def</code> 定义，支持多种参数传递，如：</p >
    <pre><code>def add(a, b):
    return a + b
</code></pre>
    <img src="C:\Users\21714\Desktop\知识梳理\函数.png" alt="知识梳理图" width="1000px" height="800px">
    <h2>面向对象编程</h2>
    <p>类、属性、方法与对象，以及构造、继承、多态和封装，如“古怪蛋糕”：</p >
    <pre><code>class Xcake:
    name=""
    color=['r','y','b']
    shape='triangle'
    def eat(self):
        return'drink'
from Xcake import Xcake
cake = Xcake()
print("蛋糕颜色有",cake.color)
print("吃蛋糕的方法是",cake.eat())
</code></pre>
    <h2>文件操作</h2>
    <p>用 <code>open()</code> 函数进行文件的读（<code>read()</code> 等）写（<code>write()</code> 等）操作。</p >
    <img src="C:\Users\21714\Desktop\知识梳理\文件操作与异常处理.png" alt="知识梳理图" width="1000px" height="800px">
    <h2>作品展示</h2>
    <p><i>作业一：校生游戏</i></p>
    <a href="C:\Users\21714\Desktop\3240103494 郑雨静 作业1\校生游戏.py">点我跳转到校生游戏代码</a>
    <a href="C:\Users\21714\Desktop\3240103494 郑雨静 作业1\3240103494 郑雨静 作业1.docx">点我跳转到校生游戏作业报告</a>
    <p><i>作业二：数列求和库</i></p>
    <a href="C:\Users\21714\Desktop\3240103494 郑雨静 作业2\库：等差数列求和.py">点我跳转到库：等差数列求和代码</a>
    <a href="C:\Users\21714\Desktop\3240103494 郑雨静 作业2\库：等比数列求和.py">点我跳转到库：等比数列求和代码</a>
    <a href="C:\Users\21714\Desktop\3240103494 郑雨静 作业2\库：斐波那契数列求和.py">点我跳转到库：斐波那契数列求和代码</a>
    <a href="C:\Users\21714\Desktop\3240103494 郑雨静 作业2\3240103494 郑雨静 作业2.docx">点我跳转到数列求和库作业报告</a>
    <p><i>作业三：数据分析</i></p>
    <a href="C:\Users\21714\Desktop\3240103494 郑雨静 作业3\数据.xls">点我跳转到数据</a>
    <a href="C:\Users\21714\Desktop\3240103494 郑雨静 作业3\数据分析.py">点我跳转到数据分析代码</a>
    <a href="C:\Users\21714\Desktop\3240103494 郑雨静 作业3\3240103494 郑雨静 作业3.docx">点我跳转到数据分析作业报告</a>
    <p><i>网页制作</i></p>
    <a href="C:\Users\21714\Desktop\网页\1.html">点我跳转到简单的加法运算</a>
    <a href="C:\Users\21714\Desktop\网页\webT.html">点我跳转到海棠诗</a>
</body>

</html>
