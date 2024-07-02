from policyengine_it.model_api import *


class resides_on_settlement_land(Variable):
    value_type = bool
    entity = Household
    label = "Resides on Settlement land"
    definition_period = YEAR
