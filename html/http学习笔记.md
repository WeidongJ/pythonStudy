---
title: HTTP学习笔记
date: 2019-05-22 10:43:04
tags:
    - http
    - 网络协议
---

# Http权威指南学习笔记
## 第一章

一个http请求流程：
1. 浏览器从 URL 中解析出服务器的主机名；
2. 浏览器将服务器的主机名转换成服务器的 IP 地址；
3. 浏览器将端口号（如果有的话）从 URL 中解析出来；
4. 浏览器建立一条与 Web 服务器的 TCP 连接；
5. 浏览器向服务器发送一条 HTTP 请求报文；
6. 服务器向浏览器回送一条 HTTP 响应报文；
7. 关闭连接，浏览器显示文档。

URL 组成：

    schema://host[:port#]/path/.../[?query-string][#anchor]
* scheme 指定低层使用的协议(例如：http, https, ftp)
* host HTTP服务器的IP地址或者域名
* port HTTP服务器的默认端口是80，这种情况下端口号可以省略。如果使用了别的端口，必须指明，例如 `http://www.cnblogs.com:8080/`
* path 访问资源的路径
* query-string       发送给http服务器的数据
* anchor：锚

web应用程序结构组件：
* 代理：位于客户端和服务器之间的 HTTP 中间实体。
* 缓存：HTTP 的仓库，使常用页面的副本可以保存在离客户端更近的地方。
* 网关：连接其他应用程序的特殊 Web 服务器。
* 隧道：对 HTTP 通信报文进行盲转发的特殊代理。
* Agent 代理：发起自动 HTTP 请求的半智能 Web 客户端

get和post的区别：get提交的数据大小有限制，因为url长度有限制，get会有安全问题；post提交数据没有限制

http状态码：
* 200 OK
* 302 Found 重定向
* 304 Not Modified 没有更改，表示上次被缓存的文档可以继续使用
* 400 Bad Request  客户端请求与语法错误，不能被服务器所理解
* 403 Forbidden 服务器收到请求，但是拒绝提供服务
* 404 Not Found 请求资源不存在（输错了URL）
* 500 Internal Server Error 服务器发生了不可预期的错误
* 503 Server Unavailable 服务器当前不能处理客户端的请求，一段时间后可能恢复正常

### http request header字段解释:
* **cache 缓存策略**
    * Cache-Control: max-age=0 单位是秒
    * If-Modified-Since 作用： 把浏览器端缓存页面的最后修改时间发送到服务器去，服务器会把这个时间与服务器上实际文件的最后修改时间进行对比。如果时间一致，那么返回304，客户端就直接使用本地缓存文件。如果时间不一致，就会返回200和新的文件内容。客户端接到之后，会丢弃旧文件，把新文件缓存起来，并显示在浏览器中.
    * If-None-Match 作用: If-None-Match和ETag一起工作，工作原理是在HTTP Response中添加ETag信息。 当用户再次请求该资源时，将在HTTP Request 中加入If-None-Match信息(ETag的值)。如果服务器验证资源的ETag没有改变（该资源没有更新），将返回一个304状态告诉客户端使用本地缓存文件。否则将返回200状态和新的资源和Etag.  使用这样的机制将提高网站的性能.
    * Pragma 作用： 防止页面被缓存， 在HTTP/1.1版本中，它和Cache-Control:no-cache作用一模一样,Pargma只有一个用法， 例如： Pragma: no-cache,注意: *在HTTP/1.0版本中，只实现了Pragema:no-cache, 没有实现Cache-Control*
    * Cache-Control 作用: 这个是非常重要的规则。 这个用来指定Response-Request遵循的缓存机制。各个指令含义如下
        * Cache-Control:Public   可以被任何缓存所缓存（）
        * Cache-Control:Private     内容只缓存到私有缓存中
        * Cache-Control:no-cache  所有内容都不会被缓存

问题：如果同时存在cache-control和Expires怎么办呢？浏览器总是优先使用cache-control，如果没有cache-control才考虑Expires 

* **Cookie 作用： 最重要的header, 将cookie的值发送给HTTP 服务器**
* **Entity头域：**
    * Content-Type 作用：指定内容 MIME类型 例如：Content-Type: application/x-www-form-urlencoded
* **Miscellaneous 头域**
    * Referer 作用： 提供了Request的上下文信息的服务器，告诉服务器我是从哪个链接过来的，比如从我主页上链接到一个朋友那里，他的服务器就能够从HTTP Referer中统计出每天有多少用户点击我主页上的链接访问他的网站。例如: Referer:http://translate.google.cn/?hl=zh-cn&tab=wT
* **Transport 头域**
    * Connection
        * Connection: keep-alive   当一个网页打开完成后，客户端和服务器之间用于传输HTTP数据的TCP连接不会关闭，如果客户端再次访问这个服务器上的网页，会继续使用这一条已经建立的连接
        * Connection: close  代表一个Request完成后，客户端和服务器之间用于传输HTTP数据的TCP连接会关闭， 当客户端再次发送Request，需要重新建立TCP连接。
### response header
* **cache**
    * date：生成消息的时间
    * expries：在指定过期时间内使用本地缓存
* **Cookie/Login 头域**
    * P3P 作用: 用于跨域设置Cookie, 这样可以解决iframe跨域访问cookie的问题，例如: P3P: CP=CURa ADMa DEVa PSAo PSDo OUR BUS UNI PUR INT DEM STA PRE COM NAV OTC NOI DSP COR
    * Set-Cookie 作用 非常重要的header, 用于把cookie 发送到客户端浏览器， 每一个写入cookie都会生成一个Set-Cookie.
* **Entity头域**
    * ETag 作用 和If-None-Match 配合使用。 （实例请看上节中If-None-Match的实例）
    
问题：ETag是实体标签（Entity Tag）的缩写， 根据实体内容生成的一段hash字符串（类似于MD5或者SHA1之后的结果），可以标识资源的状态。 当资源发送改变时，ETag也随之发生变化。
ETag是Web服务端产生的，然后发给浏览器客户端。浏览器客户端是不用关心Etag是如何产生的。
为什么使用ETag呢？ 主要是为了解决Last-Modified 无法解决的一些问题。
1. 某些服务器不能精确得到文件的最后修改时间， 这样就无法通过最后修改时间来判断文件是否更新了。

2. 某些文件的修改非常频繁，在秒以下的时间内进行修改. Last-Modified只能精确到秒。

3. 一些文件的最后修改时间改变了，但是内容并未改变。 我们不希望客户端认为这个文件修改了。
* **Miscellaneous 头域**
    * Server 作用：指明HTTP服务器的软件信息 例如:Server: Microsoft-IIS/7.5
* **Transport 头域**
    * Connection
        * Connection: keep-alive   当一个网页打开完成后，客户端和服务器之间用于传输HTTP数据的TCP连接不会关闭，如果客户端再次访问这个服务器上的网页，会继续使用这一条已经建立的连接
        * Connection: close  代表一个Request完成后，客户端和服务器之间用于传输HTTP数据的TCP连接会关闭， 当客户端再次发送Request，需要重新建立TCP连接。
* **Location头域**
    * Location作用： 用于重定向一个新的位置, 包含新的URL地址 实例请看302状态实例

## cookie 一种功能强大且高效的持久身份识别技术。（用于维护http会话的状态，达到持久会话的目的）

* 会话cookie： 会话cookie 是一种临时 cookie，它记录了用户访问站点时的设置和偏好。用户退出浏览器时，会话 cookie 就被删除了
* 持久cookie： 它们存储在硬盘上，浏览器退出，计算机重启时它们仍然存在。通常会用持久 cookie 维护某个用户会周期性访问的站点的配置文件或登录名

**与sessionId的区别**
1. cookie 是一种发送到客户浏览器的文本串句柄，并保存在客户机硬盘上，可以用来在某个WEB站点会话间持久的保持数据。
2. session其实指的就是访问者从到达某个特定主页到离开为止的那段时间。 Session其实是利用Cookie进行信息处理的，当用户首先进行了请求后，服务端就在用户浏览器上创建了一个Cookie，当这个Session结束时，其实就是意味着这个Cookie就过期了。注：为这个用户创建的Cookie的名称是aspsessionid。这个Cookie的唯一目的就是为每一个用户提供不同的身份认证。
3. cookie和session的共同之处在于：cookie和session都是用来跟踪浏览器用户身份的会话方式。
4. cookie 和session的区别是：cookie数据保存在客户端，session数据保存在服务器端。
5. 5.两个都可以用来存私密的东西，同样也都有有效期的说法,区别在于session是放在服务器上的，过期与否取决于服务期的设定，cookie是存在客户端的，过去与否可以在cookie生成的时候设置进去。
* (1)cookie数据存放在客户的浏览器上，session数据放在服务器上
* (2)cookie不是很安全，别人可以分析存放在本地的COOKIE并进行COOKIE欺骗,如果主要考虑到安全应当使用session
* (3)session会在一定时间内保存在服务器上。当访问增多，会比较占用你服务器的性能，如果主要考虑到减轻服务器性能方面，应当使用COOKIE
* (4)单个cookie在客户端的限制是3K，就是说一个站点在客户端存放的COOKIE不能3K。
* (5)所以：将登陆信息等重要信息存放为SESSION;其他信息如果需要保留，可以放在COOKIE中




每次HTTP请求，Cookie都会被发送。当然了，浏览器也不是发送它所接收到的所有Cookie，它会检查当前要请求的域名以及目录， 只要这二项目与Cookie对应的Domain和Path匹配，才会发送。对于Domain则是按照尾部匹配的原则进行的。