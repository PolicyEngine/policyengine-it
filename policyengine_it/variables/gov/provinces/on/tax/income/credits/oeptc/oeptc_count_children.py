from policyengine_it.model_api import *


class oeptc_count_children(Variable):
    value_type = int
    entity = Household
    label = "Ontario Energy and Property Tax Credit children"
    definition_period = YEAR

    adds = ["oeptc_child"]
