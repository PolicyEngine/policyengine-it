from policyengine_it.model_api import *


class refundable_tax_credits(Variable):
    value_type = float
    entity = Household
    label = "refundable tax credits"
    unit = CAD
    definition_period = YEAR

    adds = "gov.cra.tax.income.credits.refundable"
