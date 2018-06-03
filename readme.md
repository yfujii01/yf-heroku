pip freeze > requirements.txt


## db仕様

```sql
create table T_Param (
	id   varchar(30),
	val  varchar(255),
	rem  varchar(255),
	PRIMARY KEY(id)
);
```

```sql
insert into T_Param (id,val,rem) values('password','aaabbbccc','接続認証用のパスワード');
insert into T_Param (id,val,rem) values('piurl','http://xxx.yyy.zzz','ラズパイのIF用APIのURL');
```

## db確認方法
heroku pg:credentials:url -a yf-heroku

Connection URL:が取得できるので

psql 取得できた文字列

で接続できる
