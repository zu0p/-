-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: j5d103.p.ssafy.io    Database: ssafy_django_web
-- ------------------------------------------------------
-- Server version	8.0.26

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
-- Table structure for table `like_image`
--

DROP TABLE IF EXISTS `like_image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `like_image` (
  `id` int NOT NULL AUTO_INCREMENT,
  `keword` varchar(45) NOT NULL,
  `like_count` int NOT NULL DEFAULT '0',
  `url` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `like_image`
--

LOCK TABLES `like_image` WRITE;
/*!40000 ALTER TABLE `like_image` DISABLE KEYS */;
INSERT INTO `like_image` VALUES (1,'mom',0,'mom1'),(2,'mom',0,'mom10'),(3,'mom',10,'mom11'),(4,'mom',0,'mom12'),(5,'mom',0,'mom13'),(6,'mom',77,'mom14'),(7,'mom',0,'mom15'),(8,'mom',0,'mom16'),(9,'mom',0,'mom17'),(10,'mom',0,'mom18'),(11,'mom',80,'mom19'),(12,'mom',0,'mom2'),(13,'mom',0,'mom20'),(14,'mom',0,'mom3'),(15,'mom',0,'mom4'),(16,'mom',0,'mom5'),(17,'mom',100,'mom6'),(18,'mom',0,'mom7'),(19,'mom',0,'mom8'),(20,'mom',55,'mom9');
/*!40000 ALTER TABLE `like_image` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-14 16:52:45
