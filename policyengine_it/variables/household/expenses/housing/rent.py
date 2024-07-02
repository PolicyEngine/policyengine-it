from policyengine_it.model_api import *


class rent(Variable):
    value_type = float
    entity = Person
    label = "Rent"
    unit = CAD
    definition_period = YEAR
