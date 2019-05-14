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
    * mysql添加UNIQUE约束：

            CREATE TABLE `test_table` (
            `id` int(20) NOT NULL AUTO_INCREMENT COMMENT '自增长id',
            `name` varchar(30) NOT NULL COMMENT '名称',
            PRIMARY KEY (`id`),
            UNIQUE KEY `idx_name` (`name`) USING BTREE
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

            ALTER TABLE `test_table` ADD UNIQUE KEY `idx_name1` (`name`);
    * 去除UNIQUE约束：

            ALTER TABLE `test_table` DROP INDEX `idx_name`;
* PRIMARY KEY 约束唯一标识数据库表中的每条记录
    * mysql添加PRIMARY KEY 约束

            ALTER TABLE `test_table` ADD PRIMARY KEY (`id`);
    * mysql去除PRIMARY KEY 约束，tips：有自增长的需要先去除自增长：

            ALTER TABLE `test_table` CHANGE `id` `id` int(20);
            ALTER TABLE `test_table` DROP PRIMARY KEY;
* FOREIGN KEY：一个表中的 FOREIGN KEY 指向另一个表中的 PRIMARY KEY，约束用于预防破坏表之间连接的动作。
    * 添加外键：

            CREATE TABLE `price`(
            `id` int(20) NOT NULL COMMENT "id",
            `order_id` int(20) NOT NULL AUTO_INCREMENT,
            `name` VARCHAR(50) DEFAULT NULL,
            PRIMARY KEY (`id`),
            CONSTRAINT `f_key` FOREIGN KEY  (`order_id`) REFERENCES `test_table` (`id`)
            )ENGINE=INNODB DEFAULT CHARSET=utf8mb4;

            ALTER TABLE `price` ADD CONSTRAINT `f_key` FOREIGN KEY  (`order_id`) REFERENCES `test_table` (`id`)
    * 删除外键：

            ALTER TABLE `price` DROP FOREIGN KEY `f_key`;
* DEFAULT 约束默认值。
* CHECK 约束用于限制列中的值的范围,mysql不支持CHECK；可以使用emun或者触发器实现（使用if判断插入值，不满足的执行delete）。