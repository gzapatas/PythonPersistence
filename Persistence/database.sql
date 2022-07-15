CREATE DATABASE POOTarea2;

CREATE TABLE POOTarea2.Sessions (
  SessionId BIGINT AUTO_INCREMENT,
  Username CHAR(150),
  Password CHAR(150),
  Firstname VARCHAR(150),
  Lastname VARCHAR(150),
  Currency CHAR(10),
  GamesPlayed INTEGER ,
  GamesLost INTEGER ,
  GamesWon INTEGER ,
  AvailableBalance DOUBLE ,
  EventTimestamp BIGINT ,
  RegDate DATE ,
  RegDatetime DATETIME ,
  RegTimestamp BIGINT ,
  PRIMARY KEY (SessionId)
)
ENGINE = INNODB,
CHARACTER SET utf8mb4,
COLLATE utf8mb4_general_ci,
COMMENT='Tabla de sesiones';