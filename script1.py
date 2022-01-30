# Python Import:
from jinja2 import Environment, BaseLoader, PackageLoader, meta
import jinja2schema
# https://towardsdatascience.com/find-the-difference-in-python-68bbd000e513

template = """
{% for interface in interfaces %}
interface {{ interface }}
   description {{ device.hostname }} {{ device_interface[interface]['ip_address'] }}
   vrf {{ device.vrf }}
   no shutdown
{% endfor %}
"""

device = {
   'hostname': 'RKKR-LAB-1',
   'vrf': 'test-vrf'
}

interfaces = {
   'gigabitethernet 1': {
      'ip_address': '192.168.1.1'
   },
   'gigabitethernet 2': {
      'ip_address': '192.168.2.1'
   }
}

class RunTemplate:

   def __init__(self, template, device) -> None:

      self.template = template 


environment = Environment(loader=BaseLoader).from_string(template)

# variables = jinja2schema.infer(template)
# print('-----(variables)>', variables)
# print('-----(variables keys)>', variables.keys())
# for row in variables.keys():
#    print('-----(1)>', variables[row])
#    print('-----(2)>', type(variables[row]))
#    print('-----(3)>', row)
#    if isinstance(variables[row], jinja2schema.model.Dictionary):
#       if row == 'device':
#          for key in variables[row].keys():
#             print(key)

rendered = environment.render(interfaces=['gigabitethernet 1', 'gigabitethernet 2'], device=device, device_interface=interfaces)
print('-----(rendered)>', rendered)
