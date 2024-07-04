from policyengine_it.model_api import *


class national_non_refundable_credits(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    unit = EUR
    label = "Total value of national non-refundable tax credits"
    adds = [
        "low_income_credit",
    ]
