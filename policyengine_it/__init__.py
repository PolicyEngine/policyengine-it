# -*- coding: utf-8 -*-

import os
from policyengine_it import entities
from policyengine_it.system import (
    CountryTaxBenefitSystem,
    Microsimulation,
    Simulation,
    COUNTRY_DIR,
    BASELINE_VARIABLES,
    parameters,
    variables,
)
from pathlib import Path
import os
from policyengine_core.taxbenefitsystems import TaxBenefitSystem
from policyengine_it.data import *
from policyengine_it.data.datasets import CountryTemplateDataset

DATASETS = [CountryTemplateDataset]  # Important: must be instantiated
REPO = Path(__file__).parent
