from policyengine_it.model_api import *

label = "Earnings"

class total_individual_pre_tax_income(Variable):
    # For the time being, this is equivalent to the "gross_income" variable from the
    # example code for head of household or to "spouse_income" for spouse
    value_type = float
    entity = Person
    label = "Total individual pre-tax income"
    unit = EUR
    documentation = "Income from gainful employment"
    definition_period = YEAR