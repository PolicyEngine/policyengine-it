from policyengine_it.model_api import *

label = "Earnings"


class employment_income(Variable):
    value_type = float
    entity = Person
    label = "Employment income"
    unit = EUR
    documentation = "Income from gainful employment"
    definition_period = YEAR
