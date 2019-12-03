

create database if not exists tweetapprover default charset utf8 collate utf8_general_ci;

create user 'tweet_manager'@'%' identified by '20191203'; /*创建用户*/

grant all privileges on tweetapprover.* to 'tweet_manager'@'%' identified by '20191203';  
flush privileges;  /*分配权限并刷新*/

/* SET SQL_SAFE_UPDATES = 0; 设置数据库模式  0 为非安全模式  1为安全模式，安全模式必须主键操作*/
set global time_zone='+8:00'; /*django关联数据异常 关联mysql失败_Server returns invalid timezone. Go to 'Advanced' tab and set 'serverTimezon' 需要进行此修改*/