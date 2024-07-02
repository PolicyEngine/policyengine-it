from policyengine_it.model_api import *


class count_dependants(Variable):
    value_type = int
    entity = Household
    label = "Dependannts"
    unit = EUR
    documentation = "Number of dependants"
    definition_period = YEAR
    adds = ["is_dependant"]
