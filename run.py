# -*- coding: utf-8 -*-
import config
from scenarios import rules
from scenarios import general
import sys

# Eligibility model
sys.path.insert(0, "C:/Users/apkom/resentencing_data_initiative/eligibility_model/code")
import importlib
import helpers
import utils
import extract 
import eligibility
import summary
import pandas as pd
import numpy as np
import datetime
from tqdm import tqdm
import copy
import os

# Extract relevant datasets
demographics = pd.read_excel("C:/Users/apkom/prison_pop/data/input/Demographics_CDCR.xlsx")
current_commits = pd.read_excel("C:/Users/apkom/prison_pop/data/input/CurrentCommitments_CDCR.xlsx")
prior_commits = pd.read_excel("C:/Users/apkom/prison_pop/data/input/PriorCommitments_CDCR.xlsx")

# Randomly select individuals to evaluate (as opposed to evaluating the entire population)
sample_ids = list(demographics[config.id_label].sample(n=50000, random_state=1))
# Extract the sampled CDCR IDs
sample_demographics = demographics[demographics[config.id_label].isin(sample_ids)]
sample_current_commits = current_commits[current_commits[config.id_label].isin(sample_ids)]
sample_prior_commits = prior_commits[prior_commits[config.id_label].isin(sample_ids)]

# Extract offense classifications
sorting_criteria = pd.read_excel("C:/Users/apkom/prison_pop/offense_classification/selection_criteria.xlsx")


errors, adult_el_cdcr_nums = eligibility.gen_eligibility(demographics = sample_demographics, 
                                                         sorting_criteria = sorting_criteria,
                                                         current_commits = sample_current_commits, 
                                                         prior_commits = sample_prior_commits, 
                                                         write_path = "C:/Users/apkom/prison_pop/data/output",
                                                         eligibility_conditions = general.el_cond,
                                                         pop_label = general.el_cond['population'],
                                                         id_label = config.id_label, 
                                                         comp_int = rules.comp_int,
                                                         to_excel = True)