---
title: sql学习笔记
date： 2019-5-13
tag： 
    - W3school
    - SQL
----
# sql学习笔记
### UNION 并集操作
union 查询需要结果列数量相等，结构相同（即查的表要类似）：

    SELECT * FROM `users` union select * FROM `users_copy1`;
union 和 union all的区别：**union会去重**
### SELECT INTO
作用：从一个表中选取数据，然后把数据插入另一个表中；常用于创建表的备份复件或者用于对记录进行存档。
注意点：
* mysql不支持 SELECT INTO操作，可以相应的替换成：
    
        CREATE TABLE forum.users (SELECT * FROM webapp.users);
* SELECT INTO语句要求被插入的表不存在。
* 可以指定插入的列：

        CREATE TABLE forum.users1 (SELECT u.id,u.email,u.name FROM webapp.users as u);
* 生成的表结构同select结果，部分会根据db类型作动态改变？
### SQL 约束 (Constraints)
主要的约束如下：
* NOT NULL 强制列不接受 NULL 值。
* UNIQUE 约束唯一标识数据库表中的每条记录,每个表可以有多个 UNIQUE 约束，但是每个表只能有一个 PRIMARY KEY 约束
* PRIMARY KEY
* FOREIGN KEY
* DEFAULT
* CHECK