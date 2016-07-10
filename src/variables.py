# Copyright (c) 2016, Joseph R. Peterson
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# * Neither the name of PerfectBru nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import numbers

class Variable(object):
	""" A variable that includes a mean and uncertainty region.
	
	Attributes:
		value (:obj:`float`): the mean of the variable
		bounds (:obj:`float` or :obj:`tuple`): Bounds as either a single number or a 2 tuple

	"""

	def __init__(self, value, bounds):
		""" Create a variable.

		Args:
			value (:obj:`float`): The value of the `Variable`
			bounds (:obj:`float` or :obj:`tuple`): Bounds as either a single number or a 2 tuple for lower and higher 

		"""
		self.value = value
		self.bounds = bounds
		if not isinstance(value, float):
			raise ValueError("'value' must be a float")
		if not isinstance(bounds,float) and not isinstance(bounds,tuple):
			raise ValueError("'bounds' must be a float or a 2 tuple")
		if isinstance(bounds,tuple):
			if len(bounds) != 2:
				raise ValueError("bounds tuple must be of length 2")

	def __repr__(self):
		thestr = "%f"%(self.value)
		if isinstance(bounds,tuple):
			thestr += "±[%f,%f]"%(self.bounds[0],self.bounds[1])
		else:
			thestr += "±%f"%self.bounds
		return thestr


