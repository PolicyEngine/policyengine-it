from policyengine_it.model_api import *


class nu_benefits(Variable):
    value_type = float
    entity = Household
    label = "Nunavut benefits"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NU
    adds = "gov.provinces.nu.benefits.benefits"
