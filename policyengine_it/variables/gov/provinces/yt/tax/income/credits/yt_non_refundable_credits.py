from policyengine_it.model_api import *


class yt_non_refundable_credits(Variable):
    value_type = float
    entity = Person
    label = "YT non refundable credits"
    documentation = "Yukon non refundable tax credits"
    unit = CAD
    definition_period = YEAR

    adds = "gov.provinces.yt.tax.income.credits.non_refundable"
