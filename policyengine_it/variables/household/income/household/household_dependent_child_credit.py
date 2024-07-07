from policyengine_it.model_api import *


class household_dependent_child_credit(Variable):
    value_type = float
    entity = Household
    label = "tax"
    documentation = "Household-level calculation of dependent child income tax credit."
    unit = EUR
    definition_period = YEAR

    def formula(household, period, parameters):
        p = parameters(period).gov.ade.credits.dependent_child




        # Find all eligible dependents in household
        dependents = household.members("dependent_child_eligible", period)

        # Calculate total credit amount
        credit = dependents * p.amount["standard"]

        return credit
