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


from .variables import Variable



class Hops(object):
	"""A representation of a Hops ingredient.

	Attributes:
		name (:obj:`str`): Hop variety
		type (:obj:`str`): Type of hops, one of: [Aroma,Bittering,Dual]
		aromas (:obj:`list` of :obj:`str`): The aroma profile keywords.
		description (:obj:`str`): The complete aroma profile.
		alpha (:obj:`Variable`): The alpha acids %
		beta (:obj:`Variable`): The beta acids %
		cohumulone (:obj:`Variable`): The co-humulin %
		totalOil (:obj:`Variable`): The mL/100g
		bpinene (:obj:`Variable`): The b-pinene %
		myrcene (:obj:`Variable`): The  myrcene %
		linalool (:obj:`Variable`): The linalool %
		caryophyllene (:obj:`Variable`): The caryophyllene %
		farnesene (:obj:`Variable`): The farnesene %
		humulene (:obj:`Variable`): The humulene %
		greaniol (:obj:`Variable`): The geraniol %

	"""

	def __init__(self, name, type, aromas, description, alpha, beta, cohumulone, totalOil, bpinene, myrcene, linalool, caryophyllene, farnesene, humulene, geraniol):
		""" Construct a hops object.
		
		Args:
			name (:obj:`str`): Hop variety
			type (:obj:`str`): Type of hops, one of: [Aroma,Bittering,Dual]
			aromas (:obj:`list` of :obj:`str`): The aroma profile keywords.
			description (:obj:`str`): The complete aroma profile.
			alpha (:obj:`Variable`): The alpha acids %
			beta (:obj:`Variable`): The beta acids %
			cohumulone (:obj:`Variable`): The co-humulin %
			totalOil (:obj:`Variable`): The mL/100g
			bpinene (:obj:`Variable`): The b-pinene %
			myrcene (:obj:`Variable`): The  myrcene %
			linalool (:obj:`Variable`): The linalool %
			caryophyllene (:obj:`Variable`): The caryophyllene %
			farnesene (:obj:`Variable`): The farnesene %
			humulene (:obj:`Variable`): The humulene %
			greaniol (:obj:`Variable`): The geraniol %
		"""
		self.name          = name
		self.type          = type
		self.aromas        = aromas
		self.description   = description
		self.alpha         = alpha
		self.beta          = beta
		self.cohumulone    = cohumulone
		self.totalOil      = totalOil
		self.bpinene       = bpinene
		self.myrcene       = myrcene
		self.linalool      = linalool
		self.caryophyllene = caryophyllene
		self.farnesene     = farnesene
		self.humulene      = humulene
		self.geraniol      = geraniol

		strObjs = [self.name, self.type, self.description]
		if not all([isinstance(s,str) for s in strObjs]):
			raise TypeError("Variables: [%s] must be of type 'str'."%(strObjs))
		varObjs = [self.alpha,self.beta,self.cohumulone,self.totalOil,self.bpinene,self.myrcene,self.linalool,self.caryophyllene,self.farnesene,self.humulene,self.geraniol]
		if not all([isinstance(s,Variable) for s in varObjs]):
			raise TypeError("Variables: [%s] must be of type 'Variable'."%(varObjs))
		if not isinstance(self.aromas,list):
			raise TypeError("Variable 'aromas' must be of type 'list'.")
		if not all([isinstance(s,str) for s in self.aromas]):
			raise TypeError("Variables: [%s] must be of type 'str'."%(self.aromas)):



