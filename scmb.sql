/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50731
 Source Host           : localhost:3306
 Source Schema         : scmb

 Target Server Type    : MySQL
 Target Server Version : 50731
 File Encoding         : 65001

 Date: 11/08/2023 00:27:40
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 25 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2022-05-07 03:06:28.517664');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2022-05-07 03:06:29.082738');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2022-05-07 03:06:29.200986');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2022-05-07 03:06:29.208963');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2022-05-07 03:06:29.217974');
INSERT INTO `django_migrations` VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2022-05-07 03:06:29.290745');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2022-05-07 03:06:29.340612');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0003_alter_user_email_max_length', '2022-05-07 03:06:29.389481');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0004_alter_user_username_opts', '2022-05-07 03:06:29.398457');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0005_alter_user_last_login_null', '2022-05-07 03:06:29.436355');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0006_require_contenttypes_0002', '2022-05-07 03:06:29.440345');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2022-05-07 03:06:29.448323');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0008_alter_user_username_max_length', '2022-05-07 03:06:29.491209');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2022-05-07 03:06:29.537086');
INSERT INTO `django_migrations` VALUES (15, 'auth', '0010_alter_group_name_max_length', '2022-05-07 03:06:29.582330');
INSERT INTO `django_migrations` VALUES (16, 'auth', '0011_update_proxy_permissions', '2022-05-07 03:06:29.591306');
INSERT INTO `django_migrations` VALUES (17, 'auth', '0012_alter_user_first_name_max_length', '2022-05-07 03:06:29.640175');
INSERT INTO `django_migrations` VALUES (18, 'entity', '0001_initial', '2022-05-07 03:06:29.786280');
INSERT INTO `django_migrations` VALUES (19, 'sessions', '0001_initial', '2022-05-07 03:06:29.820225');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for entity_image
-- ----------------------------
DROP TABLE IF EXISTS `entity_image`;
CREATE TABLE `entity_image`  (
  `uuid` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `filename` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `webpath` varchar(250) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `type` smallint(5) UNSIGNED NOT NULL,
  `classify` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `create_date` datetime(6) NULL DEFAULT NULL,
  `modify_date` datetime(6) NULL DEFAULT NULL,
  `is_show` smallint(5) UNSIGNED NOT NULL,
  `upload_user_id` varchar(9) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`webpath`) USING BTREE,
  INDEX `entity_image_upload_user_id_7c9c6c25_fk_entity_user_username`(`upload_user_id`) USING BTREE,
  CONSTRAINT `entity_image_upload_user_id_7c9c6c25_fk_entity_user_username` FOREIGN KEY (`upload_user_id`) REFERENCES `entity_user` (`username`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of entity_image
-- ----------------------------
INSERT INTO `entity_image` VALUES ('022fa2e120be454b8b600b58adcaa6e4', 'cat_2022_05_07_085521.jpg', 'https://img.cster.xyz/litao/cat_2022_05_07_085521.jpg', 0, 'cat', '2022-05-07 08:55:22.000000', '2022-05-07 09:24:15.000000', 0, 'admin');
INSERT INTO `entity_image` VALUES ('bb818daeaad84cfcb6794cb12833fecb', 'cat_2022_05_07_094628.jpg', 'https://img.cster.xyz/litao/cat_2022_05_07_094628.jpg', 0, 'cat', '2022-05-07 09:46:28.000000', '2022-05-07 09:49:06.000000', 0, 'admin');
INSERT INTO `entity_image` VALUES ('2f0c3e3b7f004ff48f584f1572c1e561', 'cat_2022_05_07_100644.jpg', 'https://img.cster.xyz/litao/cat_2022_05_07_100644.jpg', 0, 'cat', '2022-05-07 10:06:44.000000', NULL, 1, 'admin');
INSERT INTO `entity_image` VALUES ('4655d267eb4a4ece9ddd330a3de5dd79', 'chicken_2022_05_07_094830.jpg', 'https://img.cster.xyz/litao/chicken_2022_05_07_094830.jpg', 0, 'chicken', '2022-05-07 09:48:30.000000', NULL, 0, 'aaaaaa');
INSERT INTO `entity_image` VALUES ('50c30d950984448b9788d544ed1c68e8', 'dog_2022_05_07_092118.jpg', 'https://img.cster.xyz/litao/dog_2022_05_07_092118.jpg', 0, 'dog', '2022-05-07 09:21:19.000000', '2022-05-07 09:24:16.000000', 0, 'admin');
INSERT INTO `entity_image` VALUES ('d44c7230df6e4b57b28e009af36c8e32', 'dog_2022_05_07_100831.jpg', 'https://img.cster.xyz/litao/dog_2022_05_07_100831.jpg', 0, 'dog', '2022-05-07 10:08:31.000000', NULL, 0, 'litao1');
INSERT INTO `entity_image` VALUES ('7e1d72560af647e0bc173292d8757c19', 'dog_2022_05_07_103039.jpg', 'https://img.cster.xyz/litao/dog_2022_05_07_103039.jpg', 0, 'dog', '2022-05-07 10:30:40.000000', NULL, 1, 'admin');
INSERT INTO `entity_image` VALUES ('4b275fb633964da391da1f66dcf87157', 'elephant_2022_05_07_031404.jpg', 'https://img.cster.xyz/litao/elephant_2022_05_07_031404.jpg', 0, 'elephant', '2022-05-07 03:14:05.000000', '2022-05-07 08:51:59.000000', 0, 'admin');
INSERT INTO `entity_image` VALUES ('40007d5a55a04ab2a335fd87bcb416e5', 'elephant_2022_05_07_091623.jpg', 'https://img.cster.xyz/litao/elephant_2022_05_07_091623.jpg', 0, 'elephant', '2022-05-07 09:16:23.000000', '2022-05-07 09:24:12.000000', 0, 'admin');
INSERT INTO `entity_image` VALUES ('a92f75ea14e04065acfaf5147fde8720', 'elephant_2022_05_07_094806.jpg', 'https://img.cster.xyz/litao/elephant_2022_05_07_094806.jpg', 0, 'elephant', '2022-05-07 09:48:06.000000', NULL, 0, 'aaaaaa');
INSERT INTO `entity_image` VALUES ('0403f2eb59c14f579caa11beafe538c4', 'elephant_2022_05_07_103111.jpg', 'https://img.cster.xyz/litao/elephant_2022_05_07_103111.jpg', 0, 'elephant', '2022-05-07 10:31:12.000000', NULL, 1, 'admin');
INSERT INTO `entity_image` VALUES ('381e0bb051d94c06bf75c57a4b319859', 'horse_2022_05_07_031418.jpg', 'https://img.cster.xyz/litao/horse_2022_05_07_031418.jpg', 0, 'horse', '2022-05-07 03:14:18.000000', '2022-05-07 08:51:58.000000', 0, 'admin');
INSERT INTO `entity_image` VALUES ('de12b6d11b874cef8df61db81bcfc171', 'user_2022_05_07_031440.jpg', 'https://img.cster.xyz/litao/user_2022_05_07_031440.jpg', 1, '', '2022-05-07 03:14:41.000000', NULL, 1, 'admin');

-- ----------------------------
-- Table structure for entity_role
-- ----------------------------
DROP TABLE IF EXISTS `entity_role`;
CREATE TABLE `entity_role`  (
  `role_id` smallint(5) UNSIGNED NOT NULL,
  `role_name` varchar(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`role_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of entity_role
-- ----------------------------
INSERT INTO `entity_role` VALUES (0, 'user');
INSERT INTO `entity_role` VALUES (1, 'admin');

-- ----------------------------
-- Table structure for entity_user
-- ----------------------------
DROP TABLE IF EXISTS `entity_user`;
CREATE TABLE `entity_user`  (
  `uuid` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `username` varchar(9) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `webpath` varchar(250) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_login` datetime(6) NOT NULL,
  `create_date` datetime(6) NULL DEFAULT NULL,
  `modify_date` datetime(6) NULL DEFAULT NULL,
  `is_online` smallint(5) UNSIGNED NOT NULL,
  `is_activate` smallint(5) UNSIGNED NOT NULL,
  `is_show` smallint(5) UNSIGNED NOT NULL,
  `user_type_id` smallint(5) UNSIGNED NOT NULL,
  PRIMARY KEY (`username`) USING BTREE,
  INDEX `entity_user_user_type_id_39f52e12_fk_entity_role_role_id`(`user_type_id`) USING BTREE,
  CONSTRAINT `entity_user_user_type_id_39f52e12_fk_entity_role_role_id` FOREIGN KEY (`user_type_id`) REFERENCES `entity_role` (`role_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of entity_user
-- ----------------------------
INSERT INTO `entity_user` VALUES ('b7a005c4eb9447549e8db409864631f1', 'aaaaaa', '123456', 'https://img.cster.xyz/litao/default.jpg', '2022-05-07 09:47:52.000000', '2022-05-07 09:47:48.000000', '2022-05-07 09:49:14.000000', 0, 0, 0, 0);
INSERT INTO `entity_user` VALUES ('8032003dd4b04478b3bfbede05255482', 'admin', '123456', 'https://img.cster.xyz/litao/user_2022_05_07_031440.jpg', '2022-05-07 10:30:11.000000', '2022-05-07 03:09:06.000000', NULL, 1, 1, 1, 1);
INSERT INTO `entity_user` VALUES ('8cc7f3c3ddf34e5bbc1bff414af38e1e', 'litao1', '123456', 'https://img.cster.xyz/litao/default.jpg', '2022-05-07 10:08:11.000000', '2022-05-07 10:04:23.000000', '2022-05-07 10:09:07.000000', 0, 0, 0, 0);

SET FOREIGN_KEY_CHECKS = 1;
