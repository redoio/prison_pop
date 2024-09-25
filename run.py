# -*- coding: utf-8 -*-
from scenarios import rules
from scenarios import general
import sys
import yaml
import pandas as pd
import numpy as np
import datetime
from tqdm import tqdm
import copy
import os
import importlib

# Eligibility model
sys.path.insert(0, "C:/Users/apkom/resentencing_data_initiative/eligibility_model/code")
import helpers
import utils
import extract 
import eligibility
import summary
import cohort


with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Extract relevant datasets
print(f"Extracting demographics, current commits and prior commits datasets from {config['base_path']}")
demographics = pd.read_excel(config['base_path']+config['dem_file_name'], engine='openpyxl')
current_commits = pd.read_excel(config['base_path']+config['curr_commits_file_name'], engine='openpyxl')
prior_commits = pd.read_excel(config['base_path']+config['prior_commits_file_name'], engine='openpyxl')

if config['eval_count']:
    print(f"Extracting a sample population of size {config['eval_count']} for eligibility evaluation")
    # Randomly select individuals to evaluate (as opposed to evaluating the entire population)
    sample_ids = list(demographics[config['id_label']].sample(n=config['eval_count'], random_state=1))
    # Extract the sampled CDCR IDs
    demographics = demographics[demographics[config['id_label']].isin(sample_ids)]
    current_commits = current_commits[current_commits[config['id_label']].isin(sample_ids)]
    prior_commits = prior_commits[prior_commits[config['id_label']].isin(sample_ids)]

# Evaluate the entire population or a sample
errors, adult_el_cdcr_nums = cohort.gen_eligible_cohort(demographics = demographics,
                                                         sorting_criteria = pd.read_excel(config['criteria_path'], engine='openpyxl'),
                                                         current_commits = current_commits,
                                                         prior_commits = prior_commits,
                                                         write_path = os.path.join(os.getcwd(), "data", "output"),
                                                         eligibility_conditions = general.el_cond,
                                                         read_path = config['base_path'],
                                                         month = config['input_timestamp'],
                                                         county_name = 'all; entire CDCR population',
                                                         pop_label = general.el_cond['population'],
                                                         id_label = config['id_label'],
                                                         comp_int = rules.comp_int,
                                                         to_excel = config['to_excel'],
                                                         parallel = False)