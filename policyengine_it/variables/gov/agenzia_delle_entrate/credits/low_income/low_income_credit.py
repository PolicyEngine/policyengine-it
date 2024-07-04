from policyengine_it.model_api import *

from policyengine_it.variables.household.person.employment_category import (
    EmploymentCategory,
)


class low_income_credit(Variable):
    value_type = float
    entity = Person
    label = "Value returned by the low income tax credit"
    definition_period = YEAR

    def formula(person, period, parameters):
        is_eligible = person("low_income_eligible", period)
        print(is_eligible)
        exemption_rate = parameters(
            period
        ).gov.agenzia_delle_entrate.credits.low_income.exemption_rate
        print(exemption_rate)
        income = person("total_individual_pre_tax_income", period)
        print(income)
        exempted_income = exemption_rate * income
        print(exempted_income)
        print(is_eligible * exempted_income)

        return is_eligible * exempted_income
