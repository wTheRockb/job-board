-- phpMyAdmin SQL Dump
-- version 4.9.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 12, 2021 at 08:08 AM
-- Server version: 5.6.41-84.1
-- PHP Version: 7.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `landscx3_WP3NA`
--

-- --------------------------------------------------------

--
-- Table structure for table `Q53_postmeta`
--

CREATE TABLE `Q53_postmeta` (
  `meta_id` bigint(20) UNSIGNED NOT NULL,
  `post_id` bigint(20) UNSIGNED NOT NULL DEFAULT '0',
  `meta_key` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `meta_value` longtext COLLATE utf8mb4_unicode_520_ci
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

--
-- Dumping data for table `Q53_postmeta`
--

INSERT INTO `Q53_postmeta` (`meta_id`, `post_id`, `meta_key`, `meta_value`) VALUES
(862, 116, '_tracked_submitted', '1617590665'),
(863, 116, '_filled', '0'),
(864, 116, '_featured', '0'),
(865, 116, '_edit_last', '8'),
(866, 116, '_job_expires', '2023-04-15'),
(867, 116, '_hours', ''),
(868, 116, '_job_location', 'Warsaw, Poland'),
(869, 116, '_application', 'info@vasterader.com'),
(870, 116, '_salary', ''),
(871, 116, '_company_name', 'Hexagon'),
(872, 116, '_company_website', 'http://example.com'),
(873, 116, '_company_tagline', ''),
(874, 116, '_rate', ''),
(875, 116, '_company_twitter', ''),
(876, 116, '_company_logo', 'http://workscout.purethe.me/files/2015/10/dfg.png'),
(877, 116, '_company_video', ''),
(878, 116, 'slide_template', 'default'),
(879, 116, '_salary_max', ''),
(880, 116, '_salary_min', ''),
(881, 116, '_rate_max', ''),
(882, 116, '_rate_min', ''),
(883, 116, '_edit_lock', '1578478096:8'),
(884, 116, '_apply_link', ''),
(885, 116, '_hide_expiration', '0'),
(886, 116, '_thumbnail_id', '51');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Q53_postmeta`
--
ALTER TABLE `Q53_postmeta`
  ADD PRIMARY KEY (`meta_id`),
  ADD KEY `post_id` (`post_id`),
  ADD KEY `meta_key` (`meta_key`(191));

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Q53_postmeta`
--
ALTER TABLE `Q53_postmeta`
  MODIFY `meta_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2045;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
