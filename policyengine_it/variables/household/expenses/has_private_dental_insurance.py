from policyengine_it.model_api import *


class has_private_dental_insurance(Variable):
    value_type = bool
    entity = Person
    label = "Has a private dental insurance plan"
    definition_period = YEAR
