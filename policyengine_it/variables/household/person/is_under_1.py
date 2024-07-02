from policyengine_it.model_api import *


class is_dependent_under_1(Variable):
    value_type = bool
    entity = Person
    label = "Is under 1 year old"
    definition_period = YEAR

    def formula(person, period, parameters):
        return (
            person("age", period) < 1
            and person("is_dependent", period) == True
        )
