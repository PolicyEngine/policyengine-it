from policyengine_it.model_api import *


class ab_benefits(Variable):
    value_type = float
    entity = Household
    label = "Alberta benefits"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.AB
    adds = "gov.provinces.ab.benefits.benefits"
