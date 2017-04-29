--CREATE DATABASE IF NOT EXISTS Chromosome_8;

-- -----------------------------------------------------
-- Table `sc001`.`Gene`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS sc001.Gene (
  Protein_product CHAR(50) NOT NULL,
  Genbank_Accession VARCHAR(10) NOT NULL,
  Chromosome_location VARCHAR(20) NOT NULL,
  Gene_name VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Genbank_Accession`)
  );

-- -----------------------------------------------------
-- Table `sc001`.`Sequence`
-- -----------------------------------------------------
  
  CREATE TABLE IF NOT EXISTS sc001.Sequence (
  `DNA_sequence` LONGTEXT NOT NULL,
  `Amino_Acid_Seq` MEDIUMTEXT NOT NULL,
  `Gene_Identifier` VARCHAR(45) NOT NULL,
  INDEX `fk_Sequence_Gene_idx` (`Gene_Identifier` ASC),
  PRIMARY KEY (`Gene_Identifier`),
  CONSTRAINT `fk_Sequence_Gene`
    FOREIGN KEY (`Gene_Identifier`)
    REFERENCES `sc001`.`Gene` (`Identifier`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `sc001`.`Exon`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS sc001.Exon (
  `Exon_Start` VARCHAR(45) NOT NULL,
  `Exon_End` VARCHAR(45) NOT NULL,
  `Sequence_Gene_Identifier` VARCHAR(45) NOT NULL,
  INDEX `fk_Exon_Sequence1_idx` (`Sequence_Gene_Identifier` ASC),
  PRIMARY KEY (`Sequence_Gene_Identifier`),
  CONSTRAINT `fk_Exon_Sequence1`
    FOREIGN KEY (`Sequence_Gene_Identifier`)
    REFERENCES `Chromosome_8`.`Sequence` (`Gene_Identifier`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sc001`.`Restriction_Enzyme`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS sc001.Restriction_Enzyme (
  `idRestriction_Enzyme` VARCHAR(7) NOT NULL,
  `Recognition_seq` MEDIUMTEXT NOT NULL,
  PRIMARY KEY (`idRestriction_Enzyme`)
  );

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
