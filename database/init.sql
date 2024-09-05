CREATE DATABASE IF NOT EXISTS dataset_db;

USE dataset_db;

CREATE TABLE IF NOT EXISTS `dataset` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `anchor` varchar(10000) NOT NULL,
  `positive` varchar(10000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
