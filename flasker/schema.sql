DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id int(10) AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  primary key(id)
)engine=innodb charset=utf8mb4;

CREATE TABLE post (
  id bigint(20) AUTOINCREMENT,
  author_id int(10) NOT NULL,
  title varchar(100) NOT NULL,
  body TEXT NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  primary key(id)
)engine=innodb charset=utf8mb4;