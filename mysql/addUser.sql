--新建用户：
insert into user (host, user, password, select_priv, insert_priv, update_priv) VALUES ('localhost', 'guest', PASSWORD('123456'), 'Y', 'Y', 'Y'); --mysql5.0 insert用户,PASSWORD函数用于加密
insert into user (host, user, authentication_string, select_priv, insert_priv, update_priv) VALUES ('localhost', 'guest', PASSWORD('123456'), 'Y', 'Y', 'Y'); --mysql5.0 insert用户,PASSWORD函数用于加密

create user guest identified by '123456'; grant usage on *.* to 'guest'@'%'; --mysql 8.0
grant usage on *.* to 'guest'@'%' identified by '123456'; --mysql 5.6 usage权限只能登陆

--基础命令
use database;
--show databases, show tables, show columns from table, show index from table :查看索引, SHOW TABLE STATUS LIKE [FROM db_name] [LIKE 'pattern'] \G: 查看表性能数据

-- 数据类型：DECIMAL：小数值 column_name DECIMAL(p,d)：表示列可以存储D位小数的P位数。十进制列的实际范围取决于精度和刻度。如：column_name DECIMAL(4,2) 数值范围(-99.99~99.99)
-- 时间格式：DATE 字节大小：3 范围：1000-1-1/9999-12-31, 
-- DATETIME: 8字节 范围：1000-01-01 00:00:00/9999-12-31 23:59:59 格式：YYYY-MM-DD HH:MM:SS
-- TIMESTAMP 4字节， 范围：1970-01-01 00:00:00/2038
-- 取值范围如果加了 unsigned，则最大值翻倍，如 tinyint unsigned 的取值范围为(0~255)。

-- create table
create table if not exists 'test_table'(
    'id' varchar(50) not null,
    'times' tinyint unsigned,
    'name' varchar(50) not null,
    `create_time` DATETIME ,
    `update_time` DATETIME not null DEFAULT current_timestamp on update current_timestamp COMMENT '更新时间',
    PRIMARY KEY ('id')
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--delete table
drop table user_blog; --删除表，
truncate table user_blog;  -- 清空数据，保留表结构，立刻释放磁盘空间 ，不管是 Innodb 和 MyISAM;
delete from user_blog; --清空数据，保留表结构，对于 MyISAM 会立刻释放磁盘空间，InnoDB 不会释放磁盘空间;
delete from user_blog where id = "1"; optimize table user_blog;  --删除数据，不会释放磁盘空间，使用optimize 释放空间;虽然未释放空间，但是可以插入数据

-- select 
select * from cia_resource limit 5 offset 3; --offset 偏移量 即从偏移量的位置开始展示数据;常用于分页查询
select * from cia_resource limit 5, 3; -- 同select * from cia_resource limit 3 offset 5; offset=5

-- 联合查询需要注意性能问题
select * from cia_resource where id="123" order By create_time desc limit 50，10; --需要添加，联合查询字段需要添加索引

select distinct resource_name from cia_resource;--查询去重

-- join
select resource_id,`name`,property_name,property_value,count(*) from cia_resource_detail right join  
cia_resource on cia_resource.id = cia_resource_detail.resource_id group by cia_resource_detail.resource_id limit 500,20 ;--join 查询左表一条数据对应的多条数据 count后需要group by

select resource_id,`name`,property_name,property_value from cia_resource_detail right join  
cia_resource on cia_resource.id = cia_resource_detail.resource_id  limit 500,20 ;--join 查询左表一条数据对应的多条数据 count后需要group by

--left join & right join
select blogs.id,`name`,comments.content from blogs left join comments on blogs.id=comments.blog_id;--列出左表的所有数据，右表中没有关联的数据，自动补全null
select blogs.id,`name`,comments.content from blogs right join comments on blogs.id=comments.blog_id;--列出右表的所有数据，左表中没有关联的数据，自动补全null

--between
SELECT * FROM `banner` where proCode BETWEEN 100001 and 200001; -- mysql 左右都是闭合的， 即查询结果包含100001和200001 

--like
SELECT * from notify_like where userId LIKE '%2019%'; -- % 匹配所有字符，[abc]匹配括号内任一单一字符
SELECT * from notify_like where userId LIKE '%2019test_';-- _通配任一字符
SELECT * from notify_like where userId LIKE '%2019test_'

-- in
select * from notify_like where userId in ("12k123213121","abcd");

-- alias： table
SELECT n.notifyId,nn.content FROM notify_like as n, notify_notify as nn where n.userId = "2000000020000269187" and nn.type = "personalMessage"; -- 这条语句查的结果实际是吧2条语句结果放在一起展示

--alias ： column
SELECT userId as id FROM notify_like;
-- JOIN: 如果表中有至少一个匹配，则返回行
-- LEFT JOIN: 即使右表中没有匹配，也从左表返回所有的行
-- RIGHT JOIN: 即使左表中没有匹配，也从右表返回所有的行
-- FULL JOIN: 只要其中一个表中存在匹配，就返回行


