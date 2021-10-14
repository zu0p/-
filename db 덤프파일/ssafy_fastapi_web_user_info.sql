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
-- Table structure for table `user_info`
--

DROP TABLE IF EXISTS `user_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_info` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `userId` varchar(256) DEFAULT NULL,
  `userPwd` varchar(256) DEFAULT NULL,
  `userName` varchar(256) DEFAULT NULL,
  `userEmail` varchar(256) DEFAULT NULL,
  `userNick` varchar(256) DEFAULT NULL,
  `userPhone` varchar(256) DEFAULT NULL,
  `userImage` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_info`
--

LOCK TABLES `user_info` WRITE;
/*!40000 ALTER TABLE `user_info` DISABLE KEYS */;
INSERT INTO `user_info` VALUES (1,'zu0p','$2b$12$AZFyFgAin.H14DfUETvoPeXnYagvKZg3Tp9YIwg8FZb64ooee8JnK','박주영','zu0p@kakao.com','zuzu','00000000000',''),(2,'yeup','$2b$12$sjU2pwl1iXUPhDpSwXpNTOjzunlj7oIDHgDQ77sCrhIh07w2KNeAS','yeup','yeup@yeup.com','yeup','yeup','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/profile/yeup.jpg'),(3,'ssafy','$2b$12$Ydbk0l9x9YucuCv2JdFfRevPTAVaXeSBkgp2Ak2WbL.9gV6qKLSte','aaa','wndud@a.com','싸피','000-1111-2222','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/profile/ssafy.jpg'),(4,'123','$2b$12$u3Mvxi3aTnVSDja6mlhSLeI.42m2BXere2fOJHqAHRDb/UC2PCeFi','지훈','wlgns@ssafy.ssafy','지훈훈2','010-1234-4567','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/profile/123.jpg'),(5,'yeup','$2b$12$12LKpJtQfuvAM5kpCY9lAutamWaYaCLGNi8iJqRdV4KDDwQ.3o4DC','yeup','yeup@yeup.com','yeup','yeup','yeup'),(6,'audwns101','$2b$12$o1HclTcVE/Fh.WAswSxPleUIIDDeKJO18KognPnjOgHSYiBR9hJZ2','선명준','audwns101@naver.com','뽀슝슝','010-6860-8640',''),(7,'sun950903','$2b$12$tJdueF0VEahaTnZQVR11xu8JlQNUza/h7XGD9Yr0BxIYDc/eDwova','선명주운','sun950903@gmail.com','뾰슝슝','010-6860-8640',''),(8,'test','$2b$12$rnNqAP/tmsN25QMqZMMsYuIH.bSoGg6QJgbFKv2aVPasxhMKSRyOC','test','test@asd.co','test','010-0000-0000',''),(9,'daebalprime','$2b$12$G0yIybZU3TBL.ztaV2CEO.l/DA0h9pAUP6JUsgUWDnJ35x3LGpY2i','김철수','dae@dae.dae','daedaedae','010-1234-5678',''),(10,'test','$2b$12$aepaOPYLfj86vEnOM7ISw.Dvp2pqS1OCmKK0NLGLq81yBmMjjqVoK','test','test@test.test','test','010-9876-5432',''),(11,'test','$2b$12$BrttFicGWB2vbDZ7c4YVQuVGjX3hTkGZYGl.ha8yhslFKwnDZJl8G','test','test@test.test','test','010-9876-5432',''),(12,'테스트','$2b$12$./ZTUox3oCp1rDHQ7HXv/eZlh72zfqv8qQsDUboOG3rOW3fHPYLta','이름','email@email.com','닉네임','010-1234-4567',''),(13,'test','$2b$12$J8LkkSAnDxx/i4dXTWaE7.tIO6B2B5Y8A9mXuQPApb1QTSsJz6RBq','하이','email@email.com','닉네임','010-1234-4567',''),(14,'whxorb44','$2b$12$7luaUxhjm5QTulgn3DdpG.MGeDX1nkw8QQyWVzfq5JslIwbVtAjZy','민진','test@test.com','민진','010-1234-1234',''),(15,'audwns111','$2b$12$gFlP9JrnPKtN999OW58E8eiiOldSD.pWcHUnK8WOgsdMDdb5PAufW','선명준','audwns101@naver.com','아아아','010-6860-8640',''),(16,'asd','$2b$12$jemSVZxmgl.5oCaomaNRpO0JyG8kVO.hqlGIiCA9/2wJ3EZx6Q5h6','asd','asd@asd.com','asd','111-1111-1111',''),(17,'test2','$2b$12$wNQYulvOgbASPyCeIlp2YeKlscqDXg1axBE9l0G1/r2UJWy0RoXLq','test','test@email.com','test','010-1234-4567',''),(18,'test','$2b$12$FnGi4N373EdFGCjztTZl9elvvl4pn79NHt2GBnBBqkr0/4m8MkCky','test','test@test.test','test','010-9876-5432',''),(19,'1','$2b$12$PlX0.fKeZIl0sZV.MyiVnOV2WVYik0H4dG5saf/zA6Le2iTo9HtEW','1','1@naver.com','1','000-0000-0000',''),(20,'1','$2b$12$0KzMOhSRRPUL1oAF1AIjruva2mQ9mAGIllEAlp4Fp4hofKamPoFBC','1','1@naver.com','1','000-0000-0000',''),(21,'1','$2b$12$9ap8sa/7fDNjRalUNLgGo.rHA0GHRByFW8FjAfm4LYEG5JNuhxrhu','1','1@naver.com','1','000-0000-0000',''),(22,'qjawlsqjacks','$2b$12$/40katJ2S9NpS.0UaWoKEu1Fl.OpOFrn2vZed8.rsvSUQ8qPNWxHK','박범진','qjawlsqjacks@naver.com','BJP','010-2323-2322',''),(23,'test','$2b$12$mz2gEC5XcwbI90kbjtvzX.6qE1mj/sKiMHpyhz/JGYQtb4BLy.xjG','test','test@test.test','test','010-9876-5432',''),(24,'asd','$2b$12$qXcB/JTVRipbSnhszcyC2eE5b89F/fcwI0hHlKMCcpx/CFPKujYIi','aa','asd@naver.com','aa','010-1234-5678',''),(25,'1','$2b$12$3JdIK4w61Km7oaaAeespFeqg8s9pVqpDFwBX5i22Pdj9DiwfRXHpC','1','1@naver.com','1','000-0000-0000',''),(26,'asd','$2b$12$IaOLj2uZPALdpRsuGsvdLOPum8/.00.Jzc7cf/nsELNWa9ZkyXqK6','aa','asd@naver.com','aa','010-1234-5678',''),(27,'dddd','$2b$12$5ofvWQjThS.rkuLJaTf2xOPcoL4OoN2FpSOEcut1laIUhe/NA7FKe','a','asd@naver.com','aa','010-1234-5678',''),(28,'qjatn109','$2b$12$3umhQRCTAR8Kx82jb0.ADOzEzbT3tQUC2HylzSsthq7OpvKZCmSHm','범수','qhrud0527@naver.com','범수','010-2339-7702',''),(29,'tdj03063','$2b$12$7/t/CUoD2eCqdLdeSvgc2u.GZn11h0OZJiAt1LnWbP3jEvi2wf7tG','배태호','asd@naver.com','asasdqwe','010-1234-5678',''),(30,'tdj03063','$2b$12$Bt1vLClLNZR20k/kqdtv0.Kdaw2eCqGmLKnNSkpLclTAhDak1BPYi','배태호','asd@naver.com','asasdqwe','010-1234-5678',''),(31,'dan','$2b$12$F6GgeTyldFwqI03JS0AjyeRQvPY8MrCTExve4OdtwlplcKSI.HkjW','dan','dansh87@gmail.com','dan','010-6644-1160',''),(32,'dddd','$2b$12$2/OS8rG/XRK/hnfrJrvHlOnq.pbPB3EOzP8kzFek9b2o7FBQFhBku','dd','dd@gmail.com','dd','010-0401-0101',''),(33,'dddddd','$2b$12$7tk6oyCH247.AMgYZSp75up7vG4xlRoATsB.2Wsak/wM2ulWsPyyO','Qwe','test@naver.com','test','010-1111-1111',''),(34,'bong','$2b$12$KHtl3QxOnXTK4VWaw.O6PO1fTsI1nCYISw3APkklseoqmQfKskiE6','bong','bong@gmail.com','bong','010-2123-5555',''),(35,'ddddddd','$2b$12$2LxkrJY0TpSfLwDy3IFgguUP3AzxH0rZClfihQwz4Pd501ML5Rbfu','Qwe','test@naver.com','test','010-1111-1111',''),(36,'whduddn','$2b$12$tP2U3722SYqM9r03/KSW3u.2Vufsud6M0GMWoqEyoym0LCGwtfeQu','조영우','asdf@asdf.com','조영우','010-000-0000',''),(37,'ooo1','$2b$12$2WIdBSZBBi2GWas82WuQ9u8QHXTtLFf1No8het6jLMzgkP6p6z94e','pjh','ooo@naver.com','oo','010-8311-7425',''),(38,'dd','$2b$12$GLtSKAxIS7G.pNB4C22fY.Awh3HbU9I90lS3k162SvlET.xL8oRGi','asdf','dfdffdf@dsds.com','fff','010-4163-7006',''),(39,'1','$2b$12$spsUnIrBsH6aqeD05QKLJOL4G3Bnc.dgRWf03jjQeUwUXhkPiVT0O','123','dfsdfs@naver.com','12','010-1234-1234',''),(40,'1','$2b$12$aLZCrfDHFLR6w/17W0ugreSAI.6Xr2/qJ8auXoErB1oRVN4ctJQQe','fds','dfsdfs@naver.com','12','010-1234-1234',''),(41,'1','$2b$12$j6ogkUvJ2y.UkiSKQAGccuAavAwxUePbsvNfeM71L0t5KSl3p4LqW','fds','dfsdfs@naver.com','12','010-1234-1234',''),(43,'1','$2b$12$iMAjKHclJwAv7..rL1yhhehDdgaNmTYRV1MzGNv5NlPBPe6sMu2oi','213','dfsdfs@naver.com','123','010-1234-1234',''),(44,'TestUser','$2b$12$7sX1tc5Qcj3kGu/FysNcdO61GAFZf7gPqOdldpn9StepLk4nZ64Hq','김싸피','TestUser@ssafy.com','싸피생생','010-0000-0000',''),(45,'TestUser2','$2b$12$ske4D4DEUjY7y4cZYiBuJOKCEmkvxFAgRdAREARSDZQLRhBnahpga','테스트유저','TestUser2@test.com','테스져','010-0000-0000',''),(46,'TestUser3','$2b$12$NCZFvTFYCjJqt9tXS6g7uuniOfamBCGaroO2Ynp19j0Eh5OJgz8Zi','테스트3','test3@test.com','테테테','010-0000-0000',''),(47,'tt','$2b$12$.tHGgyWoU.amnAtu1e2ESeD40aMdnxwjXdfw1ICzEhvyAAyXOOkdW','박주영','wndud@a.com','싸피','000-0000-0000',''),(48,'bun95','$2b$12$OKfENYM2TPm1vPqvvh/tSO1G1Xh1/Qezxa6VZ2bBkorMZZW85nR9.','변지훈s','bfds@naver.com','변지훈','010-0000-0000','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/profile/bun95.jpg'),(49,'wndud97','$2b$12$xeGcBciPrRcC/avFwIqsveXW.zAQNp2ntxwVvvFt1kDWPFCYVRm42','박주영','wndud@grider.com','주영','010-1234-1234',''),(50,'test12345678','$2b$12$C.gFqlVZVM6QL9FwF998Ve2MoRFRh/sKc6iKgSmkILlTaBHteIg6K','Dkdk','Gndk@naver.com','Fjri','010-3845-0384',''),(51,'cherrykang97','$2b$12$Q8gVFEaRVX8CdG6tKtJ.wuU5E8Q5bGXEVy8.1AP7PbdDCSw1nHZAi','강민주','cherrykang97@naver.com','밍뚜','010-5137-8979','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/profile/cherrykang97.jpg'),(52,'zu0p','$2b$12$VPiafy56Pt57APaEG4Ktc.x6KE2OJK2FqSqXyMybTxuOCN9MefOqS','박선영','zu0p@kakao.com','서녕','010-0000-0000',''),(53,'myId97','$2b$12$9.UEt6sZ2kryceGXvL0DkOqDYRSmcWJURMpbT6Y8cBULvjhBxu8bq','김길은','mymy@my.com','길동','010-0001-0000','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/profile/myId97.jpg'),(54,'idid97','$2b$12$58xRHgqTV/NIADk8gLfk0.YtgmXJOhVPIzoQIqKBrpKJhiUexgleC','박아이디','idid@id.com','아이디','010-1111-1112','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/profile/idid97.jpg'),(55,'newId97','$2b$12$VwbMKur8ASfhJygIElnMXOcuoUlInV5opW3aFId3Ie4Ed1D.nK0/2','박주연','newId@aaa.com','주영','000-0000-0001','https://greeda-recommend.s3.ap-northeast-2.amazonaws.com/profile/newId97.jpg'),(56,'ralo','$2b$12$R/sSaEmuQaa9t3PnSyKsTu05kgAonCwdBHJtFIZ6f9aY.qlO040BG','Ralo','a@a.net','RALO','010-1234-4567',''),(57,'yeup2','yeup2','yeup2','yeup2@yeup.com','yeup2','yeup2','yeup2');
/*!40000 ALTER TABLE `user_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-14 16:52:43
