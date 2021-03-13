-- ------------------ Search GPUs -----------------------------------------------

SELECT chipsetManufacturer, brandName, graphicsCoprocessor, averagePrice, unigineBenchmarkScore, passmarkBenchmarkScore, shadowOfTheTombRaiderFPS, grandTheftAuto5FPS
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

-- ------------------ Add new outputs -----------------------------------------------

INSERT INTO outputs (displayPort, hdmi, vga, dvi)
VALUES (:displayPort, :hdmi, :vga, :dvi)

-- ------------------ Add new benchmark -----------------------------------------------

INSERT INTO benchmarkValues (unigineBenchmarkScore, passmarkBenchmarkScore, shadowOfTheTombRaiderFPS, grandTheftAuto5FPS)
VALUES (:unigineBenchmarkScoreInput, :passmarkBenchmarkScoreInput, shadowOfTheTombRaiderFPSInput, grandTheftAuto5FPSInput)

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

