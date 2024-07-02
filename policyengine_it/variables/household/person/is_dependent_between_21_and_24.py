from policyengine_it.model_api import *


class is_dependent_between_21_and_24(Variable):
    value_type = bool
    entity = Person
    label = "Is between 21 and 24 years old"
    definition_period = YEAR

    def formula(person, period, parameters):
        return (
            person("age", period) >= 21
            and person("age", period) < 24
            and person("is_dependent", period) == True
        )
