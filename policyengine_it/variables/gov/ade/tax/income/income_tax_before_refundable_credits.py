from policyengine_it.model_api import *


class income_tax_before_refundable_credits(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    unit = EUR
    label = "Italian national income tax before refundable credits"
    documentation = "Income tax liability (including other taxes) after non-refundable credits are used, but before refundable credits are applied"
    adds = [
        "income_tax_before_credits",
    ]
    subtracts = [
        "non_refundable_credits",
    ]
