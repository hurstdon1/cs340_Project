-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 04, 2021 at 03:39 AM
-- Server version: 10.4.17-MariaDB-log
-- PHP Version: 7.4.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cs340_ehlertl`
--
-- --------------------------------------------------------

--
-- Table structure for table `benchmarkValues`
--

CREATE TABLE `benchmarkValues` (
  `id` int(11) NOT NULL,
  `unigineBenchmarkScore` int(11),
  `passmarkBenchmarkScore` int(11),
  `shadowOfTheTombRaiderFPS` int(11),
  `grandTheftAuto5FPS` int(11)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `benchmarkValues`
--

INSERT INTO `benchmarkValues` (`id`, `unigineBenchmarkScore`, `passmarkBenchmarkScore`, `shadowOfTheTombRaiderFPS`, `grandTheftAuto5FPS`) VALUES
(1, 3537, 12661, 101, 86),
(2, 8082, 19459, 117, 125),
(3, 9930, 21640, 188, 132),
(4, 13749, 24129, 198, 144),
(5, 18714, 25486, 203, 175);

-- --------------------------------------------------------

--
-- Table structure for table `brands`
--

CREATE TABLE `brands` (
  `id` int(11) NOT NULL,
  `brandName` varchar(255) NOT NULL,
  `productSeries` varchar(255) NOT NULL,
  `model` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



--
-- Dumping data for table `brands`
--

INSERT INTO `brands` (`id`, `brandName`, `productSeries`, `model`) VALUES
(1, 'ASUS', 'GTX 1600', 'ROG Strix'),
(2, 'ASUS', 'RTX 3000', 'ROG Strix'),
(3, 'ASUS', 'RTX 3000', 'ROG Strix'),
(4, 'ASUS', 'RTX 3000', 'ROG Strix'),
(5, 'ASUS', 'RTX 3000', 'ROG Strix');

-- --------------------------------------------------------

--
-- Table structure for table `chipsets`
--

CREATE TABLE `chipsets` (
  `id` int(11) NOT NULL,
  `chipsetManufacturer` varchar(255) NOT NULL,
  `graphicsCoprocessor` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `chipsets`
--

INSERT INTO `chipsets` (`id`, `chipsetManufacturer`, `graphicsCoprocessor`) VALUES
(1, 'Nvidia', 'GTX 1660 SUPER'),
(2, 'Nvidia', 'RTX 3060 SUPER'),
(3, 'Nvidia', 'RTX 3070'),
(4, 'Nvidia', 'RTX 3080'),
(5, 'Nvidia', 'RTX 3090');

-- --------------------------------------------------------

--
-- Table structure for table `outputs`
--

CREATE TABLE `outputs` (
  `id` int(11) NOT NULL,
  `displayPort` int(11),
  `hdmi` int(11), 
  `vga` int(11),
  `dvi` int(11)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `outputs` (`id`, `displayPort`, `hdmi`, `vga`, `dvi`) VALUES
(1, 3, 1, 0, 0),
(2, 2, 2, 0, 0),
(3, 1, 3, 0, 0),
(4, 0, 0, 2, 0),
(5, 0, 0, 1, 1);

--
-- Table structure for table `graphicsCards`
--

-- --------------------------------------------------------

CREATE TABLE `graphicsCards` (
  `id` int(11) NOT NULL,
  `averagePrice` int(11) NOT NULL,
  `memoryType` varchar(255) NOT NULL,
  `numberOfCudaCores` int(11) NOT NULL,
  `chipset` int(11) NOT NULL,
  `outputs` int(11)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `graphicsCards`
--

INSERT INTO `graphicsCards` (`id`, `averagePrice`, `memoryType`, `numberOfCudaCores`, `chipset`) VALUES
(1, 1, 'DDR6', 1408, 1),
(2, 2, 'DDR6', 4864, 2),
(3, 3, 'DDR6', 5888, 3),
(4, 4, 'DDR6X', 8704, 4),
(5, 5, 'DDR6X', 10496, 5);

-- --------------------------------------------------------

--
-- Table structure for table `graphicsCard_benchmarkValues`
--

CREATE TABLE `graphicsCard_benchmarkValues` (
  `gpuID` int(11) NOT NULL,
  `benchmarkId` int(11) NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `graphicsCard_benchmarkValues`
--

INSERT INTO `graphicsCard_benchmarkValues` (`gpuID`, `benchmarkId`) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

-- --------------------------------------------------------

--
-- Table structure for table `graphicsCard_brands`
--

CREATE TABLE `graphicsCard_brands` (
  `gpuId` int(11) NOT NULL,
  `brandId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `graphicsCard_brands`
--

INSERT INTO `graphicsCard_brands` (`gpuId`, `brandId`) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

--

--
-- Indexes for table `benchmarkValues`
--
ALTER TABLE `benchmarkValues`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `brands`
--
ALTER TABLE `brands`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `outputs`
--
ALTER TABLE `outputs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `chipsets`
--
ALTER TABLE `chipsets`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `graphicsCards`
--
ALTER TABLE `graphicsCards`
  ADD PRIMARY KEY (`id`),
  ADD KEY `averagePrice` (`averagePrice`),
  ADD KEY `chipset` (`chipset`),
  ADD KEY `outputs` (`outputs`);

--
-- Indexes for table `graphicsCard_benchmarkValues`
--
ALTER TABLE `graphicsCard_benchmarkValues`
  ADD PRIMARY KEY (`gpuID`,`benchmarkId`),
  ADD KEY `benchmarkId` (`benchmarkId`);

--
-- Indexes for table `graphicsCard_brands`
--
ALTER TABLE `graphicsCard_brands`
  ADD PRIMARY KEY (`gpuId`,`brandId`),
  ADD KEY `brandId` (`brandId`);

--
-- AUTO_INCREMENT for dumped tables
--

--


--
-- AUTO_INCREMENT for table `benchmarkValues`
--
ALTER TABLE `benchmarkValues`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `brands`
--
ALTER TABLE `brands`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `outputs`
--
ALTER TABLE `outputs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `chipsets`
--
ALTER TABLE `chipsets`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `graphicsCards`
--
ALTER TABLE `graphicsCards`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `graphicsCards`
--
ALTER TABLE `graphicsCards`
  ADD CONSTRAINT `graphicsCards_ibfk_1` FOREIGN KEY (`outputs`) REFERENCES `outputs` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `graphicsCards_ibfk_2` FOREIGN KEY (`chipset`) REFERENCES `chipsets` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `graphicsCard_benchmarkValues`
--
ALTER TABLE `graphicsCard_benchmarkValues`
  ADD CONSTRAINT `graphicsCard_benchmarkValues_ibfk_1` FOREIGN KEY (`gpuID`) REFERENCES `graphicsCards` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `graphicsCard_benchmarkValues_ibfk_2` FOREIGN KEY (`benchmarkId`) REFERENCES `benchmarkValues` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `graphicsCard_brands`
--
ALTER TABLE `graphicsCard_brands`
  ADD CONSTRAINT `graphicsCard_brands_ibfk_1` FOREIGN KEY (`gpuId`) REFERENCES `graphicsCards` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `graphicsCard_brands_ibfk_2` FOREIGN KEY (`brandId`) REFERENCES `brands` (`id`) ON DELETE CASCADE;
COMMIT;


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
