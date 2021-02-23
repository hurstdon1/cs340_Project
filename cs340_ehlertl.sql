-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 13, 2021 at 05:27 AM
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
-- Table structure for table `averagePrice`
--

CREATE TABLE `averagePrice` (
  `id` int(11) NOT NULL,
  `averagePriceValue` decimal(65,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `averagePrice`
--

INSERT INTO `averagePrice` (`id`, `averagePriceValue`) VALUES
(1, '500'),
(2, '600'),
(3, '750'),
(4, '900'),
(5, '1750');

-- --------------------------------------------------------

--
-- Table structure for table `benchmarkValues`
--

CREATE TABLE `benchmarkValues` (
  `id` int(11) NOT NULL,
  `unigineBenchmarkScore` int(11) NOT NULL,
  `passmarkBenchmarkScore` int(11) NOT NULL,
  `shadowOfTheTombRaiderFPS` int(11) NOT NULL,
  `grandTheftAuto5FPS` int(11) NOT NULL
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
-- Table structure for table `graphicsCards`
--

CREATE TABLE `graphicsCards` (
  `id` int(11) NOT NULL,
  `averagePrice` int(11) NOT NULL,
  `memoryType` varchar(255) NOT NULL,
  `numberOfCudaCores` int(11) NOT NULL,
  `chipset` int(11) NOT NULL
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
  `benchmarkId` int(11) NOT NULL
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
-- Indexes for dumped tables
--

--
-- Indexes for table `averagePrice`
--
ALTER TABLE `averagePrice`
  ADD PRIMARY KEY (`id`);

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
  ADD KEY `chipset` (`chipset`);

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
-- AUTO_INCREMENT for table `averagePrice`
--
ALTER TABLE `averagePrice`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

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
  ADD CONSTRAINT `graphicsCards_ibfk_1` FOREIGN KEY (`averagePrice`) REFERENCES `averagePrice` (`id`),
  ADD CONSTRAINT `graphicsCards_ibfk_2` FOREIGN KEY (`chipset`) REFERENCES `chipsets` (`id`);

--
-- Constraints for table `graphicsCard_benchmarkValues`
--
ALTER TABLE `graphicsCard_benchmarkValues`
  ADD CONSTRAINT `graphicsCard_benchmarkValues_ibfk_1` FOREIGN KEY (`gpuID`) REFERENCES `graphicsCards` (`id`),
  ADD CONSTRAINT `graphicsCard_benchmarkValues_ibfk_2` FOREIGN KEY (`benchmarkId`) REFERENCES `benchmarkValues` (`id`);

--
-- Constraints for table `graphicsCard_brands`
--
ALTER TABLE `graphicsCard_brands`
  ADD CONSTRAINT `graphicsCard_brands_ibfk_1` FOREIGN KEY (`gpuId`) REFERENCES `graphicsCards` (`id`),
  ADD CONSTRAINT `graphicsCard_brands_ibfk_2` FOREIGN KEY (`brandId`) REFERENCES `brands` (`id`);
COMMIT;



-- -----------QUERIES BELOW-----------------------------------------------------

-- ------------------ Search GPUs -----------------------------------------------

SELECT averagePrice, chipsetManufacturer, brandName, graphicsCoprocessor, unigineBenchmarkScore, passmarkBenchmarkScore, shadowOfTheTombRaiderFPS, grandTheftAuto5FPS
FROM graphicsCards
INNER JOIN graphicsCard_brands ON graphicsCards.id = graphicsCard_brands.gpuId
INNER JOIN brands ON graphicsCard_brands.gpuId = brands.id
INNER JOIN graphicsCard_benchmarkValues ON graphicsCards.id = graphicsCard_benchmarkValues.gpuID
INNER JOIN benchmarkValues ON benchmarkValues.id = graphicsCard_benchmarkValues.benchmarkId
INNER JOIN chipsets ON chipsets.id = graphicsCards.chipset
WHERE chipsetManufacturer=:chipsetManufacturer, brandName=:brandName, graphicsCoprocessor=:graphicsCoprocessor, unigineBenchmarkScore=:unigineBenchmarkScore,
passmarkBenchmarkScore=:passmarkBenchmarkScore, shadowOfTheTombRaiderFPS=:shadowOfTheTombRaiderFPS, grandTheftAuto5FPS

-- ------------------ Add new Graphics card -----------------------------------------------

INSERT INTO graphicsCards (averagePrice, memoryType, numberOfCudaCores, chipset)
VALUES (:averagePriceInput, :memoryTypeInput, :numberOfCudaCoresInput, :chipsetIdInput)

-- ------------------ Add new brand -----------------------------------------------

INSERT INTO brands (brandName, productSeries, model)
VALUES (:brandNameInput, :productSeriesInput, :modelInput)

-- ------------------ Add new chipset -----------------------------------------------

INSERT INTO chipsets (chipsetManufacturer, graphicsCoprocessor)
VALUES (:chipsetManufacturerInput, :graphicsCoprocessorInput)

-- ------------------ Add new benchmark -----------------------------------------------

INSERT INTO benchmarkValues (unigineBenchmarkScore, passmarkBenchmarkScore, shadowOfTheTombRaiderFPS, grandTheftAuto5FPS)
VALUES (:unigineBenchmarkScoreInput, :passmarkBenchmarkScoreInput, shadowOfTheTombRaiderFPSInput, grandTheftAuto5FPSInput)

-- ------------------ Add new average price -----------------------------------------------

INSERT INTO averagePrice (averagePriceValue)
VALUES (:averagePriceValueInput)

-- ------------------ Add a new GPU/Benchmark Relationship -----------------------------------------------

INSERT INTO graphicsCard_benchmarkValues (gpuID, benchmarkID)
VALUES (:gpuIDInput, :benchmarkIDInput)

-- ------------------ Add new GPU/Brand Relationship -----------------------------------------------

INSERT INTO graphicsCard_brands (gpuID, brandID)
VALUES (:gpuIDInput, :brandIDInput)

-- ------------------ Update Benchmark Scores -----------------------------------------------

UPDATE benchmarkValues SET 
unigineBenchmarkScore = :unigineBenchmarkScoreInput,
passmarkBenchmarkScore = :passmarkBenchmarkScoreInput,
shadowOfTheTombRaiderFPS = :shadowOfTheTombRaiderFPSInput,
grandTheftAuto5FPS = :grandTheftAuto5FPSInput
WHERE benchmarkID = :benchmarkID

-- ------------------ Delete a Graphics Card -----------------------------------------------

DELETE FROM graphicsCards
WHERE graphicsCards.id = :id

DELETE FROM graphicsCard_brands
WHERE :id = graphicsCard_brands.gpuId

DELETE FROM graphicsCard_benchmarkValues
WHERE :id = graphicsCard_benchmarkValues.gpuID

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
