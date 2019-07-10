#
# This file is part of Dragonfly.
# (c) Copyright 2007, 2008 by Christo Butcher
# Licensed under the LGPL.
#
#   Dragonfly is free software: you can redistribute it and/or modify it
#   under the terms of the GNU Lesser General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Dragonfly is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   Lesser General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public
#   License along with Dragonfly.  If not, see
#   <http://www.gnu.org/licenses/>.
#

"""
ExecuteActionRule class
============================================================================

The ExecuteActionRule class is designed to execute a single action
associated with the value of its element. It is intended to be used
as a top-level exported rule.


Example usage
............................................................................

The ExecuteActionRule class can be used to define a voice-command as follows::

	class ExampleRule(ExecuteActionRule):

	rule = ExampleRule()
	grammar.add_rule(rule)


Class reference
............................................................................

"""

from .rule_base         import Rule
from .elements          import ElementBase, Compound, Alternative
from ..actions.actions  import ActionBase


#---------------------------------------------------------------------------

class ExecuteActionRule(Rule):
	"""
		Rule class that executes the action value of its element
	"""


	#-----------------------------------------------------------------------

	def __init__(self, name=None, element=None, context=None):
		Rule.__init__(self, name = name, element = element, context = context, imported=False, exported=True)


	#-----------------------------------------------------------------------

	def process_recognition(self, node):
		"""
			Convert value of root node to an action and execute it
		"""
		value = node.value()

		if isinstance(value, ActionBase):
			value.execute()
		elif self._log_proc:
			self._log_proc.warning("%s: mapping value is not an action,"
								   " cannot execute." % self)
