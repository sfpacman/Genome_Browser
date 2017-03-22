CREATE DATABASE Chromosome_8;

CREATE TABLE Chromosome_8.Gene (
  Protein_product CHAR(50) NOT NULL,
  Genbank_Accession VARCHAR(6) NOT NULL,
  Chromosome_location VARCHAR(8) NOT NULL,
  Identifier VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Identifier`)
  );
  
  CREATE TABLE Chromosome_8.Sequence (
  DNA_sequence LONGTEXT NOT NULL,
  Amino_Acid_Seq MEDIUMTEXT NOT NULL,
  Gene_Identifier VARCHAR(45) NOT NULL,
  INDEX `fk_Sequence_Gene_idx` (`Gene_Identifier` ASC),
  PRIMARY KEY (`Gene_Identifier`),
    FOREIGN KEY (`Gene_Identifier`),
    );
    
CREATE TABLE Chromosome_8.Exon (
  Exon_Start VARCHAR(45) NOT NULL,
  Exon_end VARCHAR(45) NOT NULL,
  Sequence_Gene_Identifier VARCHAR(45) NOT NULL,
  INDEX `fk_Exon_Sequence1_idx` (`Sequence_Gene_Identifier` ASC),
  PRIMARY KEY (`Sequence_Gene_Identifier`),
  CONSTRAINT `fk_Exon_Sequence1`
    FOREIGN KEY (`Sequence_Gene_Identifier`)
    REFERENCES `Chromosome_8`.`Sequence` (`Gene_Identifier`)
    );

CREATE TABLE Chromosome_8.Restriction_Enzyme (
  `idRestriction_Enzyme` TEXT(7) NOT NULL,
  `Recognition_seq` MEDIUMTEXT NOT NULL,
  `Sequence_Gene_Identifier` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idRestriction_Enzyme`),
  INDEX `fk_Restriction_Enzyme_Sequence1_idx` (`Sequence_Gene_Identifier` ASC),
  CONSTRAINT `fk_Restriction_Enzyme_Sequence1`
    FOREIGN KEY (`Sequence_Gene_Identifier`)
   );
