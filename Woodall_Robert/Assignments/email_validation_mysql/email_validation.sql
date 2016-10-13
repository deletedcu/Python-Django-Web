-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema flask_email_validation_mysql
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema flask_email_validation_mysql
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `flask_email_validation_mysql` DEFAULT CHARACTER SET utf8 ;
USE `flask_email_validation_mysql` ;

-- -----------------------------------------------------
-- Table `flask_email_validation_mysql`.`user_email`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `flask_email_validation_mysql`.`user_email` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
