CREATE DATABASE `banksystem`;
use banksystem;

CREATE TABLE `accounts` (
  `id` int NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `moneys` int NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

INSERT INTO `accounts` VALUES (75,'admin','8b37ab9ad07977a7d23db3b85d053afb','admin@bankmail.com','{FLAG3-Etz351Sdc}',100);

CREATE TABLE `messages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `from` varchar(255) NOT NULL,
  `text` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=152 DEFAULT CHARSET=utf8mb3;


CREATE DATABASE `sql_injection`;
use sql_injection;

CREATE TABLE `level1` (
  `id` int NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

INSERT INTO `level1` VALUES (1,'level1','epCcYKslEZHH23aRQ5WaRffjvDtpeI6U'),(2,'maggie','1234567890'),(3,'cristina','loveyou'),(4,'manuel','basketball'),(5,'ricardo','tinkerbell'),(6,'madison','lovers');


CREATE TABLE `level2` (
  `id` int NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

INSERT INTO `level2` VALUES (1,'amanda','forever'),(2,'level2','GWtcI7bXeUlxYlo092BHoiz1Y1XQXTbv'),(3,'hannah','666666'),(4,'barbie','shadow'),(5,'melissa','elizabeth'),(6,'eminem','teamo');


CREATE TABLE `level3` (
  `id` int NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

INSERT INTO `level3` VALUES (1,'brandon','jesus'),(2,'thomas','poohbear'),(3,'level3','HpuL6s7qYcRbtFAzWwGSNqYJ5tYW7757'),(4,'angela','sakura'),(5,'adrian','iloveme'),(6,'alexander','america');


CREATE TABLE `level4_TFadFGaD` (
  `id_RjsAeRsR` int NOT NULL,
  `username_FrSdAqER` varchar(20) NOT NULL,
  `password_OiUtFSaa` varchar(100) NOT NULL,
  PRIMARY KEY (`id_RjsAeRsR`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

INSERT INTO `level4_TFadFGaD` VALUES (1,'alejandra','killer'),(2,'rachel','11111'),(3,'patricia','999999'),(4,'level4','ApiBKyh5Xrk1WWTuPkkwNkMmP1RQW4co'),(5,'brittany','hunter'),(6,'sandra','dolphin');


CREATE TABLE `level5` (
  `id` int NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

INSERT INTO `level5` VALUES (1,'fernando','pokemon'),(2,'antonio','222222'),(3,'david','blink182'),(4,'stephanie','peanut'),(5,'level5','kO1eouNe1zQfCoTKJgEuFQbyzj5mPFzY'),(6,'victoria','pepper');


CREATE TABLE `level6` (
  `id` int NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

INSERT INTO `level6` VALUES (1,'pamela','jesus1'),(2,'maria','888888'),(3,'bailey','banana'),(4,'jeremy','prince'),(5,'kimberly','friend'),(6,'level6','luq5aOkUQFMLzcsWYqdIO3cxbBUyoA29');


CREATE TABLE `level7` (
  `id` int NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

INSERT INTO `level7` VALUES (1,'jackie','789456123'),(2,'rebecca','123654'),(3,'sebastian','portugal'),(4,'johnny','volleyball'),(5,'karina','rockstar'),(7,'level7','x8b7xabx9axd0ywxa7xd2=xb3xb8]x05:xfb');


CREATE USER 'user1'@'%' IDENTIFIED BY 'Password1';
CREATE USER 'user2'@'%' IDENTIFIED BY 'Password2';
CREATE USER 'user3'@'%' IDENTIFIED BY 'Password3';
CREATE USER 'user4'@'%' IDENTIFIED BY 'Password4';
CREATE USER 'user5'@'%' IDENTIFIED BY 'Password5';
CREATE USER 'user6'@'%' IDENTIFIED BY 'Password6';
CREATE USER 'user7'@'%' IDENTIFIED BY 'Password7';
CREATE USER 'bankadmin'@'%' IDENTIFIED BY 'SuperAdminPassword!';

GRANT SELECT on sql_injection.level1 TO 'user1'@'%';
GRANT SELECT on sql_injection.level2 TO 'user2'@'%';
GRANT SELECT on sql_injection.level3 TO 'user3'@'%';
GRANT SELECT on sql_injection.level4_TFadFGaD  TO 'user4'@'%';
GRANT SELECT on sql_injection.level5 TO 'user5'@'%';
GRANT SELECT on sql_injection.level6 TO 'user6'@'%';
GRANT SELECT on sql_injection.level7 TO 'user7'@'%';
GRANT ALL PRIVILEGES on banksystem.* TO 'bankadmin'@'%';
