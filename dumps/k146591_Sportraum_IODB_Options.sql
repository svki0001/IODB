-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: 91.204.46.200    Database: k146591_Sportraum_IODB
-- ------------------------------------------------------
-- Server version	5.7.33

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
-- Table structure for table `Options`
--

DROP TABLE IF EXISTS `Options`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Options` (
  `name` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `value` text COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Options`
--

LOCK TABLES `Options` WRITE;
/*!40000 ALTER TABLE `Options` DISABLE KEYS */;
INSERT INTO `Options` VALUES ('contract_active','on'),('contract_active_sose','off'),('contract_active_wise','off'),('contract_adress','AStA der HS KL StO. ZW\r\nAmerikastraße 1\r\n66482 Zweibrücken\r\n0631 – 37245188\r\nsport.asta-zw@hs-kl.de'),('contract_end_sose','03-01'),('contract_end_wise','09-01'),('contract_link_conditions','https://gremien-zw.de/wp-content/uploads/2019/11/Nutzungsbedingungen_Fitnessraum_Stand10-11-2019.pdf'),('contract_link_logo','https://gremien-zw.de/wp-content/uploads/2019/07/AStA_ZW_Logoklein.png'),('contract_note','Dieser Vertrag wird online angelegt, zu einem rechtsgültigen Abschluss kommt er jedoch erst nach Registrierung und Zahlung vor Ort im Gremienbüro der AStA.'),('contract_price_employee','35'),('contract_price_stud','20'),('contract_text_conclusion','Dieser Vertrag wird online angelegt, zu einem rechtsgültigen Abschluss kommt er jedoch erst nach Registrierung und\r\nZahlung vor Ort im Gremienbüro der AStA.\r\nDer Vertrag erneuert sich nicht automatisch. Kündigungsbedingungen siehe Nutzungsbedingungen\r\nBeginn des Vertrages ist ab Tag der Zahlung.'),('contract_text_obligations','Der Nutzer bestätigt, dass er sich an die Nutzungsbedingungen des Fitnessraumes hält. Insbesondere hält er sich\r\nan die Anweisung der Sportreferenten (auch durch Aushänge im Sportraum möglich) sowie der\r\nSorgfaltspflichtgegenüber der Einrichtung des Fitnessraumes. Er ist sich über den Haftungsausschluss bewusst (der\r\nAStA haftet nicht für Schäden an Personen und Gegenständen).Bei Zuwiderhandlungen behalten wir uns vor den\r\nZugang zu sperren und gegebenenfalls Anzeige zu erstatten.'),('contract_text_services','Wir bieten den Sportraum und die darin stehenden Geräte zur Verfügung und stellen einen ganztägigen Zugang\r\nsicher, sollte Hinderungen geben, die die Nutzung des Sportraumes / Equipments behindern, werden diese in\r\nangemessenem Zeitraum behoben. Alle weiteren Leistungen bitte den Nutzungsbedingungen entnehmen.'),('contract_title','Nutzungsvertrag \r\nfür den Fitnessraum des AStA'),('email_again_text','Anbei erhälst du deinen Vertrag erneut zugeschickt'),('email_block_text','Du wirst nun gesperrt'),('email_contract_subject','Das ist dein Vertrag'),('email_contract_text','Dein Vertrag wurde erfolgreich angelegt :)\r\nNut noch bezahlen und es kann losgehen, bei Fragen oder Problemen melde dich und so\r\n\r\n'),('email_contract_text_final','Mit sportlichen Grüßen dein\r\nAStA Sport\r\n\r\n'),('email_from','mail@karolisdailidonis.de'),('email_paid_subject','Deine Zahlung'),('email_paid_text','Deine Zahlung war erfolgreich\r\n\r\nMit sportlichen Grüßen dein\r\nAStA Sport'),('email_test','mail@karolisdailidonis.de'),('room_max_person','15'),('room_max_time','120'),('room_min_person','2'),('room_min_person_max_time','15'),('system_camera_1','0'),('system_door_active','on'),('system_door_display','1'),('system_plugin_user_0','mail@karolisdailidonis.de'),('system_plugin_user_1','langpeno@gmail.com'),('user_max_strike','3');
/*!40000 ALTER TABLE `Options` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-29 17:05:23
