# Python Import:
from jinja2 import Environment, BaseLoader, PackageLoader, meta
import jinja2schema
# https://towardsdatascience.com/find-the-difference-in-python-68bbd000e513

template = """
{% for interface in interfaces %}
interface {{ interface }}
   description {{ hostname }}
   no shutdown
{% endfor %}
"""


environment = Environment(loader=BaseLoader).from_string(template)
rendered = environment.render(interfaces=['gigabitethernet 1', 'gigabitethernet 2'])
variables = jinja2schema.infer(template)
print('-----(rendered)>', rendered)
print('-----(variables keys)>', variables.keys())
for row in variables.keys():
    print('-----()>', variables[row])
    print('-----()>', type(variables[row]))
    print('-----()>', row)
