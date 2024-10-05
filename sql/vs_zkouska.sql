-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema vs_zkouska
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema vs_zkouska
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `vs_zkouska` DEFAULT CHARACTER SET utf8 ;
USE `vs_zkouska` ;

-- -----------------------------------------------------
-- Table `vs_zkouska`.`student`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vs_zkouska`.`student` (
  `idstudent` INT NOT NULL AUTO_INCREMENT,
  `jmeno` VARCHAR(45) NOT NULL,
  `prijmeni` VARCHAR(45) NOT NULL,
  `vek` INT NOT NULL,
  PRIMARY KEY (`idstudent`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `vs_zkouska`.`ucitel`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vs_zkouska`.`ucitel` (
  `iducitel` INT NOT NULL AUTO_INCREMENT,
  `jmeno` VARCHAR(45) NOT NULL,
  `prijmeni` VARCHAR(45) NOT NULL,
  `vek` INT NOT NULL,
  PRIMARY KEY (`iducitel`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `vs_zkouska`.`misto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vs_zkouska`.`misto` (
  `idmisto` INT NOT NULL AUTO_INCREMENT,
  `zeme` VARCHAR(45) NOT NULL,
  `mesto` VARCHAR(45) NOT NULL,
  `adresa` VARCHAR(45) NOT NULL,
  `ucebna` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idmisto`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `vs_zkouska`.`predmet`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vs_zkouska`.`predmet` (
  `idpredmet` INT NOT NULL AUTO_INCREMENT,
  `nazev` VARCHAR(45) NULL,
  `obor` VARCHAR(45) NULL,
  `ucitel_iducitel` INT NOT NULL,
  PRIMARY KEY (`idpredmet`, `ucitel_iducitel`),
  INDEX `fk_predmet_ucitel1_idx` (`ucitel_iducitel` ASC) VISIBLE,
  CONSTRAINT `fk_predmet_ucitel1`
    FOREIGN KEY (`ucitel_iducitel`)
    REFERENCES `vs_zkouska`.`ucitel` (`iducitel`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `vs_zkouska`.`zkouska`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vs_zkouska`.`zkouska` (
  `idzkouska` INT NOT NULL AUTO_INCREMENT,
  `termin` DATETIME NOT NULL,
  `online` TINYINT NOT NULL,
  `misto_idmisto` INT NOT NULL,
  `student_idstudent` INT NOT NULL,
  `ucitel_iducitel` INT NOT NULL,
  `predmet_idpredmet` INT NOT NULL,
  PRIMARY KEY (`idzkouska`, `misto_idmisto`, `student_idstudent`, `ucitel_iducitel`, `predmet_idpredmet`),
  INDEX `fk_zkouska_misto1_idx` (`misto_idmisto` ASC) VISIBLE,
  INDEX `fk_zkouska_student1_idx` (`student_idstudent` ASC) VISIBLE,
  INDEX `fk_zkouska_ucitel1_idx` (`ucitel_iducitel` ASC) VISIBLE,
  INDEX `fk_zkouska_predmet1_idx` (`predmet_idpredmet` ASC) VISIBLE,
  CONSTRAINT `fk_zkouska_misto1`
    FOREIGN KEY (`misto_idmisto`)
    REFERENCES `vs_zkouska`.`misto` (`idmisto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_zkouska_student1`
    FOREIGN KEY (`student_idstudent`)
    REFERENCES `vs_zkouska`.`student` (`idstudent`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_zkouska_ucitel1`
    FOREIGN KEY (`ucitel_iducitel`)
    REFERENCES `vs_zkouska`.`ucitel` (`iducitel`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_zkouska_predmet1`
    FOREIGN KEY (`predmet_idpredmet`)
    REFERENCES `vs_zkouska`.`predmet` (`idpredmet`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `vs_zkouska`.`vysledek`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vs_zkouska`.`vysledek` (
  `idvysledek` INT NOT NULL AUTO_INCREMENT,
  `prospel` TINYINT NOT NULL,
  `body` INT NOT NULL,
  `komentar` VARCHAR(200) NOT NULL,
  `zkouska_idzkouska` INT NOT NULL,
  `zkouska_misto_idmisto` INT NOT NULL,
  `zkouska_student_idstudent` INT NOT NULL,
  `zkouska_ucitel_iducitel` INT NOT NULL,
  `zkouska_predmet_idpredmet` INT NOT NULL,
  PRIMARY KEY (`idvysledek`, `zkouska_idzkouska`, `zkouska_misto_idmisto`, `zkouska_student_idstudent`, `zkouska_ucitel_iducitel`, `zkouska_predmet_idpredmet`),
  INDEX `fk_vysledek_zkouska1_idx` (`zkouska_idzkouska` ASC, `zkouska_misto_idmisto` ASC, `zkouska_student_idstudent` ASC, `zkouska_ucitel_iducitel` ASC, `zkouska_predmet_idpredmet` ASC) VISIBLE,
  CONSTRAINT `fk_vysledek_zkouska1`
    FOREIGN KEY (`zkouska_idzkouska` , `zkouska_misto_idmisto` , `zkouska_student_idstudent` , `zkouska_ucitel_iducitel` , `zkouska_predmet_idpredmet`)
    REFERENCES `vs_zkouska`.`zkouska` (`idzkouska` , `misto_idmisto` , `student_idstudent` , `ucitel_iducitel` , `predmet_idpredmet`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
