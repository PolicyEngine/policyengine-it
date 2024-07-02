# -*- coding: utf-8 -*-

import os
from policyengine_it import entities
from policyengine_it.system import (
    CountryTaxBenefitSystem,
    Microsimulation,
    Simulation,
    IndividualSim,
    COUNTRY_DIR,
    BASELINE_VARIABLES,
    parameters,
    variables,
)
from pathlib import Path
import os
from policyengine_core.taxbenefitsystems import TaxBenefitSystem
from policyengine_it.data import *
from policyengine_it.data import DATASETS

REPO = Path(__file__).parent
