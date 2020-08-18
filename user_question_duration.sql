/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.1.38-MariaDB : Database - online_exam
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
/*Data for the table `duration` */

insert  into `duration`(`id`,`time_in_minutes`) values (1,2);

/*Data for the table `question` */

insert  into `question`(`id`,`question`,`op1`,`op2`,`op3`,`op4`,`corr_ans`) values (1,'Capital of Bangladesh:','Dhaka','Rajshahi','Chottogram','Khulna','Dhaka');
insert  into `question`(`id`,`question`,`op1`,`op2`,`op3`,`op4`,`corr_ans`) values (2,'Square of 5 equals:','25','50','125','10','25');
insert  into `question`(`id`,`question`,`op1`,`op2`,`op3`,`op4`,`corr_ans`) values (3,'What is 1004 divided by 2?','52','502','520','5002','502');
insert  into `question`(`id`,`question`,`op1`,`op2`,`op3`,`op4`,`corr_ans`) values (4,'Square root of 9:','2','3','9','4','3');
insert  into `question`(`id`,`question`,`op1`,`op2`,`op3`,`op4`,`corr_ans`) values (5,'What is 8%3 equals in python?','0','3','5','2','2');

/*Data for the table `user` */

insert  into `user`(`id`,`name`,`password`) values (1,'mizan','1234');
insert  into `user`(`id`,`name`,`password`) values (2,'ridwan','1234');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
