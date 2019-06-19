# markdown 前言

## markdown 学习 2019/0429

learn from [markdown.cn](http://www.markdown.cn/ "markdown中文doc")

## 标题

使用 #标记标题，数量标志标题级别

### 这是一个四级标题

## 引用

> 这是一个引用-weidong

## 列表

### 创建列表

使用*、+、-来标记无序列表，tips：红黑项目之间如果有空行，对应的html转换会加上&lt;p&gt;标签
>
    <ul>
    <li><p>Bird</p></li>
    <li><p>Magic</p></li>
    </ul>

* 红
* 黑
* 黄

使用1.（序号和英文点，与列表内容之间要有空格！）来标记无序列表

1. 计划
2. 读书
3. 学习

### 列表缩进

* 这是一个markdown学习笔记在
    2019/04/29这一天记录的
* 而这是一个列表缩进的演示
* 这是一个列表内的引用
    > 你看到的是一个列表内引用--weidong
* 列表中放置区块代码，double缩进(列表行后需要一个换行):

        print('life is short, I use pytohn.')

## 区块代码

直接使用一个制表符可以实现建立区块代码：

    Here is an example of AppleScript:

    tell application "Foo"
        beep
    end tell

这是一个代码部分：

    <div class="footer">
        &copy; 2004 Foo Corporation
    </div>

## icon

&copy;copy图标

    &copy;

## 分割线

可以使用 *  - _ 建立一个水平分割线
***

## 链接

使用[]()来创建一个链接，[]内是链接文字，()是链接,可以使用相对链接指定站内资源，可以用空格+字符串指定title：
我是从[markdown.cn](http://www.markdown.cn/ "markdown中文doc")学习markdown的

    [markdown.cn](http://www.markdown.cn/ "markdown中文doc")

### 参考式链接：

我是从[markdown.cn][id] 学习markdown的,及把url信息写在id内部再去访问，[id]内部不区分大小写

隐式参考链接：

即id值为空，默认指定链接内容作id
这是最近搭建的个人[blog][] ,一个使用github Pages + hexo搭建的个人blog

## 强调

markdown使用* 和(_)来强调,被其包围的文字会_打上 *`<em>`*标签，使用** 和__其内部文字会打上`<strong>`标签;不能2边都有空格，即\*1\*可以2边都没有空格，或者只有一个空格

## 转义符号

\\ 使用\\转义

## 标记代码

使用\` \`标记代码文本，如果code文本含有反引号可以使用多个\`：

    `` select `id` from db ``

## 图片

以!起始，其他同链接：

![background][bg]

## 自动链接

    <https://weidongj.github.io/>
以上链接会转化成`<a href="https://weidongj.github.io">weidongj.github.io</a>`

[id]: http://www.markdown.cn/ "markdown中文doc"
[blog]: https://weidongj.github.io/ "Weidong's blog"
[bg]: ../html/resources/elva-fairy-320w.jpg "block title"
