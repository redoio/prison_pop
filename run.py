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


with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Extract relevant datasets
print(f"Extracting demographics, current commits and prior commits datasets from {config['base_path']}")
demographics = pd.read_excel(config['base_path']+"Demographics_CDCR.xlsx", engine='openpyxl')
current_commits = pd.read_excel(config['base_path']+"CurrentCommitments_CDCR.xlsx", engine='openpyxl')
prior_commits = pd.read_excel(config['base_path']+"PriorCommitments_CDCR.xlsx", engine='openpyxl')

print(f"Extracting a sample population of size {config['eval_count']} for eligibility evaluation")
# Randomly select individuals to evaluate (as opposed to evaluating the entire population)
sample_ids = list(demographics[config['id_label']].sample(n=config['eval_count'], random_state=1))
# Extract the sampled CDCR IDs
sample_demographics = demographics[demographics[config['id_label']].isin(sample_ids)]
sample_current_commits = current_commits[current_commits[config['id_label']].isin(sample_ids)]
sample_prior_commits = prior_commits[prior_commits[config['id_label']].isin(sample_ids)]

# Extract offense classifications
sorting_criteria = pd.read_excel(config['base_path']+"/offense_classification/selection_criteria.xlsx")


errors, adult_el_cdcr_nums = eligibility.gen_eligibility(demographics = sample_demographics,
                                                         sorting_criteria = sorting_criteria,
                                                         current_commits = sample_current_commits,
                                                         prior_commits = sample_prior_commits,
                                                         write_path = "/data/output",
                                                         eligibility_conditions = general.el_cond,
                                                         pop_label = general.el_cond['population'],
                                                         id_label = config['id_label'],
                                                         comp_int = rules.comp_int,
                                                         to_excel = config['to_excel'],
                                                         parallel = config['parallel'])