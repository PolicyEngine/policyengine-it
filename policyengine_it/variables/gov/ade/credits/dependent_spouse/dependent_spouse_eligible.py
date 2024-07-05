from policyengine_it.model_api import *


class dependent_spouse_eligible(Variable):
    value_type = bool
    entity = Household
    label = "Eligible for dependent spouse income tax credit"
    definition_period = YEAR

    def formula(household, period, parameters):
        p = parameters(period).gov.ade.credits.dependent_spouse.eligibility

        # Determine if household is married
        household_is_married: bool = household("household_married", period)
        print(household_is_married)

        # Pull overall household income pre-credits
        household_income: float = household("household_market_income", period)
        print(household_income)

        # Find spouse's income specifically
        spouse_income: float = household("spouse_market_income", period)
        print(spouse_income)

        # Find values for each eligibility criterium
        elig_income_dist: bool = household_income > spouse_income
        elig_spouse_income: bool = spouse_income <= p.spouse_income
        elig_household_income: bool = household_income <= p.household_income
        elig_marital_status: bool = household_is_married

        print(elig_income_dist)
        print(elig_spouse_income)
        print(elig_household_income)
        print(elig_marital_status)

        eligible = (
            elig_income_dist
            & elig_spouse_income
            & elig_household_income
            & elig_marital_status
        )

        print(eligible)

        return eligible
