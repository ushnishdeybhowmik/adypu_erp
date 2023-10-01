-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: erp_database
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `student_data`
--

DROP TABLE IF EXISTS `student_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_data` (
  `URN` varchar(17) NOT NULL,
  `First_Name` varchar(45) NOT NULL,
  `Middle_Name` varchar(45) DEFAULT NULL,
  `Last_Name` varchar(45) NOT NULL,
  `Mother_name` varchar(45) DEFAULT NULL,
  `Gender` varchar(45) NOT NULL,
  `DOB` date NOT NULL,
  `Local_Address` varchar(225) NOT NULL,
  `Permanent_Address` varchar(225) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Student_Phone_No` int NOT NULL,
  `Emergency_Phone` int NOT NULL,
  `Aadhar_Card_No` int NOT NULL,
  `Physical_Handicap` enum('NO','YES') NOT NULL,
  `Category` enum('General','OBC','BC','ST','SC','VJ','NT') NOT NULL,
  `Blood_Group` enum('O-positive','A-positive','B-positive','AB-positive','O-negative','A-negative','B-negative','AB-negative', 'Bombay Blood Grp') NOT NULL,
  `Religion` enum('Hindu','Muslim','Sikh','Christian','Parsi','Buddhist','Other') DEFAULT NULL,
  `Nationality` varchar(45) NOT NULL,
  `State_And_City` varchar(45) NOT NULL,
  `Student_Status` enum('ACTIVE','NOT-ACTIVE') NOT NULL,
  `Academic_Year` int NOT NULL,
  `Program` varchar(100) NOT NULL,
  `Course` varchar(45) NOT NULL,
  `Semester` varchar(12) DEFAULT NULL,
  `Father_Occupation` varchar(45) NOT NULL,
  `Father_Phone_No` int NOT NULL,
  `Father_Email_ID` varchar(45) NOT NULL,
  `Mother_Phone_No` int DEFAULT NULL,
  `Family_Income` int NOT NULL,
  `Education_Loan_Availed` enum('NO','YES') NOT NULL,
  `Photo` mediumblob NOT NULL,
  PRIMARY KEY (`URN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci KEY_BLOCK_SIZE=2;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_data`
--

LOCK TABLES `student_data` WRITE;
/*!40000 ALTER TABLE `student_data` DISABLE KEYS */;
/*!40000 ALTER TABLE `student_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-01 21:12:00
