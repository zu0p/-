-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: j5d103.p.ssafy.io    Database: ssafy_fastapi_web
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
-- Table structure for table `diary_info`
--

DROP TABLE IF EXISTS `diary_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `diary_info` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `diaryName` varchar(256) DEFAULT NULL,
  `diaryImage` varchar(256) DEFAULT NULL,
  `diaryDesc` varchar(256) DEFAULT NULL,
  `diaryShare` tinyint(1) DEFAULT NULL,
  `diaryOwnerId` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `diary_info_chk_1` CHECK ((`diaryShare` in (0,1)))
) ENGINE=InnoDB AUTO_INCREMENT=172 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diary_info`
--

LOCK TABLES `diary_info` WRITE;
/*!40000 ALTER TABLE `diary_info` DISABLE KEYS */;
INSERT INTO `diary_info` VALUES (20,'changedName','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/yeup_test.jpg','test2',1,'yeup'),(21,'test2','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/yeup_test2.jpg','test2',1,'yeup'),(22,'test3','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/yeup_test3.jpg','test2',1,'yeup'),(26,'123','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/zu0p_123.jpg','123',0,'zu0p'),(28,'dark night','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/zu0p_bbb.jpg','bbbbb',1,'zu0p'),(31,'update','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/zu0p_new.jpg','s',0,'zu0p'),(32,'sky','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/zu0p_ss.jpg','s',0,'zu0p'),(33,'aa','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/zu0p_aa.jpg','ss',0,'zu0p'),(36,'바꿈!','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/ssafy_ㅁㄴㅇㄹ.jpg','121',0,'ssafy'),(45,'ㅁㅁㅁ','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/ssafy_aaa.jpg','aaa',0,'ssafy'),(49,'6th','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/ssafy_6.jpg','666',0,'ssafy'),(50,'일기','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/123_일기.jpg','설명',0,'123'),(51,'9월일기','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/audwns101_9월일기.jpg','9월에 쓴 모음!!',0,'audwns101'),(52,'10월일기','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/audwns101_10월일기.jpg','ㄴ',0,'audwns101'),(54,'','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/audwns101_ㅁㄴㅇㄹ.jpg','ㅁㄴㅇㄹ',0,'audwns101'),(55,'ㅁㄴㅇㄹ','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/audwns101_ㅁㄴㅇㄹ.jpg','ㅁㄴㅇㄹ',0,'audwns101'),(56,'제목수정','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/audwns101_sdfasdf.jpg','1234',1,'audwns101'),(59,'으으으','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/daebalprime_으으으.jpg','어어어',0,'daebalprime'),(60,'첫번째','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/audwns111_첫번째.jpg','첫내용',0,'audwns111'),(61,'','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/asd_asd.jpg','asd',0,'asd'),(64,'두번째','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/audwns111_두번째.jpg','두번째 내용',0,'audwns111'),(65,'3','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/audwns111_3.jpg','33',0,'audwns111'),(66,'44','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/audwns111_44.jpg','44',0,'audwns111'),(67,'55','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/audwns111_55.jpg','55',0,'audwns111'),(68,'test1','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/whxorb44_test1.jpg','test1',0,'whxorb44'),(69,'sdf','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/qjawlsqjacks_sdf.jpg','dfdf',1,'qjawlsqjacks'),(71,'ㅎ2','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/dddd_ㅎ2.jpg','ㅎ2',1,'dddd'),(72,'54553534','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/qjatn109_123123.jpg','123123',0,'qjatn109'),(73,'asdf','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/1_asdf.jpg','asdf',1,'1'),(76,'a','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/tdj03063_a.jpg','dasd',1,'tdj03063'),(77,'123','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/dan_123.jpg','123',1,'dan'),(79,'123','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/dan_123.jpg','123',1,'dan'),(81,'test','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/ddddddd_test.jpg','dd',0,'ddddddd'),(83,'a','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/test_a.jpg','a',0,'test'),(85,'','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/bong_d.jpg','dddd',0,'bong'),(86,'글','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/1234_글.jpg','설명',0,'1234'),(87,'일기일기','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/123_일기일기.jpg','123',0,'123'),(89,'바다일기장','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/123_바다일기장.jpg','바다 일기장입니다',0,'123'),(93,'ㅁㅁㅇ','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/ssafy_ㅁㅁㅇ.jpg','ㅁㅁ',1,'ssafy'),(108,'되나?','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/123_되나?.jpg','ㅇㅇ',0,'123'),(109,'ㄴㄴ','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/123_ㄴㄴ.jpg','ㄴㄴ',0,'123'),(111,'제목','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/tt_제목.jpg','설명설명',1,'tt'),(112,'제목2','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/tt_제목2.jpg','설명설명2',0,'tt'),(115,'제목3','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/tt_제목3.jpg','설명설명3',0,'tt'),(122,'제목4','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/tt_제목4.jpg','글자수때문에 이미지때문인건가??정말로?',0,'tt'),(124,'제목을 길게하면 안되는건가??그럴수도 있지 않을까','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/tt_제목을 길게하면 안되는건가??그럴수도 있지 않을까.jpg','설명은 간단히',0,'tt'),(126,'띄어쓰기를하면설마안되는건아니겠지','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/tt_띄어쓰기를하면설마안되는건아니겠지.jpg','설명',0,'tt'),(129,'6월','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/TestUser3_6월.jpg','6월의 일기 모음입니다',1,'TestUser3'),(132,'6월','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/TestUser_6월.jpg','6월 일기 모음',1,'TestUser'),(133,'7월','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/TestUser_7월.jpg','7월 일기 모음',0,'TestUser'),(134,'8월','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/TestUser_8월.jpg','8월 일기 모음',0,'TestUser'),(135,'9월','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/TestUser_9월.jpg','9월 일기 모음',0,'TestUser'),(137,'10월','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/TestUser_10월.jpg','10월 일기 모음',0,'TestUser'),(138,'6월','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/bun95_6월.jpg','6월 일기 모음',0,'bun95'),(139,'7월','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/bun95_7월.jpg','7월 일기 모음',0,'bun95'),(140,'8월','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/bun95_8월.jpg','8월 일기 모음',0,'bun95'),(144,'8월 아침','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/ssafy_8월 아침.jpg','ㅁㅁ',0,'ssafy'),(145,'4월이 좋아','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/ssafy_4월이 좋아.jpg','ㅁ',0,'ssafy'),(146,'ㅁㅁ','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/ssafy_ㅁㅁ.jpg','ㄴㄴ',0,'ssafy'),(147,'9월','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/bun95_9월.jpg','9월 일기 모음',0,'bun95'),(154,'7월의기록','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/wndud97_7월의기록.jpg','7월의 일기 조각 모음',0,'wndud97'),(155,'8월의더위','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/wndud97_8월의더위.jpg','너무너무 더운 여름',0,'wndud97'),(156,'9월','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/wndud97_9월.jpg','선선해지는 날씨',0,'wndud97'),(158,'취직','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/test12345678_취직.jpg','취직설명',0,'test12345678'),(159,'주영이는봐라','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/cherrykang97_주영이는봐라.jpg','맛있는 야식 먹중',1,'cherrykang97'),(163,'10월일기','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/wndud97_10월일기.jpg','10월 일기들 모음',1,'wndud97'),(167,'11월일기','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/wndud97_11월일기.jpg','11월 일기들',0,'wndud97'),(169,'g','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/ralo_g.jpg','gsdfsd',1,'ralo'),(171,'10월','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/diary/bun95_10월.jpg','10월 일기',0,'bun95');
/*!40000 ALTER TABLE `diary_info` ENABLE KEYS */;
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
