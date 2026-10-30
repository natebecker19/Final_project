# Final_project
**By:** Nate Becker and Allen Solano-Rodriguez\
**Team Name:** EV

**Dataset:** The [Electric Vehicle Population Data](https://catalog.data.gov/dataset/electric-vehicle-population-data?from_hint=eyJzb3J0IjoicG9wdWxhcml0eSJ9) dataset contains a CSV file of every Battery Electric Vehicles (BEVs) and Plug-in Hybrid Electric Vehicles (PHEVs) that are currently registered in the state of Washington.

**Motivation:**
  Electric Vehicles are on the cutting edge of modern transportation, using clean energy. Through this project, we will explore how electric vehicles are being brought into daily life. The data we are using is Electric Vehicle Population Data [1] collected by the Washington State Department of Licensing. We are using Washington State as a small sample that might extend to the entire United States. The data was collected to determine which EV owners are eligible for Clean Alternative Fuel Vehicle rebates and to count and register electric vehicles. This data set can include the type of EV, model and make, and county; summing the data will give us the number of EVs, the range of EVs, and eligibility of EVs for Clean Alternative Fuel Vehicle (CAFV).
Selected Questions
[1] State of Washington - Electric Vehicle Population Data 

**Question 1:** Which model and make of EV is the most popular?\
**Answer for Question 1:** EVs manufactured by Tesla.\
**Justification/Proof of Concept for Question 1:** The dataset contains the make and model of each EV, such as a Tesla Model Y for example. By counting how many times a make and model of an EV appears and comparing it to other EVs, we can see which one is the most popular.

sum makes and models and compare them to eachother in a loop\
**Output/visualization:** list of top three most popular models and most popular makers of EVs

**Question 2:** Do counties with higher income have more EVs?\
**Answer for Question 2:** Yes, higher income areas will have more electric vehicles as they tend to cost more money upfront.\
**Justification/Proof of Concept for Question 2:** The dataset assigns each EV with the country it’s located in, we can find out which counties have the highest numbers of EVs and then use another source of data to find out which counties have the highest income levels. Then by comparing the two sets of data, we can see if there is any correlation between the number of EVs in a county and the level of income the county has.

sum number of county entries to get a number of EVs per county then compare to income in counties\
**Output/visualization:** bar chart with two bars per county, EVs per capita and income percapita

**Question 3:** What percent of the EVs are eligible for Clean Alternative Fuel Vehicle rebates from the state of Washington?\
**Answer for Question 3:** We’ve speculated that 75% of EVs are eligible for CAFV rebates.\
**Justification/Proof of Concept for Question 3:** The dataset contains a datapoint called “Clean Alternative Fuel Vehicle (CAFV) Eligibility” which tells us if an EV is eligible for CAFV rebates or not. Because every EV in the dataset includes the “Clean Alternative Fuel Vehicle (CAFV) Eligibility” datapoint, we can calculate and find the percentage of EVs that are CAFV eligible.

Sum eligibility and divide by total\
**Output/visualization:** a percentage or a pie chart


**Results:**
tbd


**Conclusions:**
tbd


**Actions to be completed:**
