# Introduction
Data on the population currently incarcerated in the California Department of Corrections and Rehabilitation (CDCR) as of December 2023. This data was acquired through the California Public Records Act (CPRA). As a result, several exclusionary criteria have been applied and limit visibility of the entire population. Some CDCR identification numbers are also hashed for de-identification throughout the dataset(s). 

# Sample
We demonstrate a full execution of the resentencing eligibility model (https://github.com/redoio/resentencing_data_initiative/) on the CDCR population data. We establish a set of eligibility rules, classify offenses based on their nature and severity, and then create a scenario for which we identify candidates for resentencing.

## Output
As of 4/29/2024, a sample run on 50,000 randomly selected individuals out of 95,476 total individuals in CDCR custody (reported by the department), we found 360 eligible candidates.<br>
Note: This cohort does not take into account age related criteria since the department denied providing information on birthdays under the CPRA request. Age is a pertinent factor, however, in Prosecutor Initiated Resentencing (PIR) eligibility. The Los Angeles County District Attorney's Office reviews adult cases if the individual is over the age of 50 and juvenile cases if the offense was committed at age 14 or 15 (https://github.com/redoio/resentencing_data_initiative/eligibility_model/code/offense_classification/county/los_angeles)

# Contact 
Contact aparna.komarla@gmail.com for any questions about this data.
