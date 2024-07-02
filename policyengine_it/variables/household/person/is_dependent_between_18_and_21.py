from policyengine_it.model_api import *


class is_dependent_between_18_and_21(Variable):
    value_type = bool
    entity = Person
    label = "Is dependent between 18 and 21 years old"
    definition_period = YEAR

    def formula(person, period, parameters):
        return (
            person("age", period) >= 21
            and person("age", period) < 24
            and person("is_dependent", period) == True
        )
