from policyengine_it.data import EnhancedFRS, SynthFRS
from policyengine_it.initial_setup import set_default

EnhancedFRS.download(2022)
SynthFRS.download(2022)
set_default(EnhancedFRS)
