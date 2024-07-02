from policyengine_it.model_api import *

label = "Earnings"


class family_employment_income(Variable):
    value_type = float
    entity = Household
    label = "Family Employment income"
    unit = EUR
    documentation = "Income of families from gainful employment"
    definition_period = YEAR

    adds = ["employment_income"]
