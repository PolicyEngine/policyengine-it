from policyengine_it.model_api import *


class income_tax(Variable):
    value_type = float
    entity = Household
    label = "Income tax after credits"
    unit = EUR
    definition_period = YEAR

    adds = ["income_tax_before_credits"]
