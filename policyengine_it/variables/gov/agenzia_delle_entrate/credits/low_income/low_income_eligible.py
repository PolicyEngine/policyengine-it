from policyengine_it.model_api import *

from policyengine_it.variables.household.person.employment_category import (
    EmploymentCategory,
)


class low_income_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for low income tax credit"
    definition_period = YEAR

    def formula(person, period, parameters):
        lic_eligibility = parameters(
            period
        ).gov.agenzia_delle_entrate.credits.low_income.eligibility
        employment_category = person("employment_category", period)

        lic_threshold = lic_eligibility[employment_category]
        eligible = (
            person("total_individual_pre_tax_income", period) <= lic_threshold
        )

        return eligible
