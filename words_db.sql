-- MySQL Workbench Synchronization
-- Generated: 2016-09-24 19:18
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: areliga

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE TABLE IF NOT EXISTS `words`.`words` (
  `id` BIGINT(20) NOT NULL,
  `word` VARCHAR(500) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  UNIQUE INDEX `word_UNIQUE` (`word` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'single word';

CREATE TABLE IF NOT EXISTS `words`.`sources` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `source` VARCHAR(1000) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'Source documented inspected (parsed) for words in it.';

CREATE TABLE IF NOT EXISTS `words`.`words_instances` (
  `word_id` BIGINT(20) NOT NULL,
  `source_id` INT(11) NOT NULL,
  `quantity` INT(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`word_id`, `source_id`),
  INDEX `fk_source_idx` (`source_id` ASC),
  CONSTRAINT `fk_word`
    FOREIGN KEY (`word_id`)
    REFERENCES `words`.`words` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_source`
    FOREIGN KEY (`source_id`)
    REFERENCES `words`.`sources` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'how many given word was found in a given source instance';


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
