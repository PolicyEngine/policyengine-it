from policyengine_it.model_api import *


class is_disabled(Variable):
    value_type = bool
    entity = Person
    label = "Is disabled"
    definition_period = YEAR