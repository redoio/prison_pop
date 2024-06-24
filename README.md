# Introduction
Data on the population currently incarcerated in the California Department of Corrections and Rehabilitation (CDCR) as of December 2023. This data was acquired via the California Public Records Act (CPRA). As a result, several privacy (health information, age, etc.) related exclusionary criteria have been applied. 

Using a sample population, and a set of eligibility criteria, we indicate who may be eligible for resentencing under Prosecutor Initiated Resentencing (PIR) programs. 

Some CDCR identification numbers are hashed for de-identification throughout the dataset(s). 

# Sample
We demonstrate a full execution of the resentencing eligibility model (https://github.com/redoio/resentencing_data_initiative/) on the CDCR population data. We establish a set of eligibility rules, classify offenses based on their nature and severity, and then create a scenario in which we identify the best candidates for resentencing.

## Output
As of 4/29/2024, a sample run on 50,000 randomly selected individuals out of 95,476 total individuals in CDCR custody (as reported by the department), returned 360 eligible candidates.<br>
<br>
Note: This cohort simply meets the sample eligibility crtiera. There is no implication that these individuals are falsely incarcerated. The selection process does not account for age-related criteria since the department denied sharing individual birthdays. Age is a pertinent factor, however, in PIR eligibility in some counties. The Los Angeles County District Attorney's Office, for example, reviews adult cases if the individual is over the age of 50 differently from juvenile cases if the offense was committed at age 14 or 15 (https://github.com/redoio/resentencing_data_initiative/eligibility_model/code/offense_classification/county/los_angeles)

# Contact 
Contact aparna.komarla@gmail.com for any questions
