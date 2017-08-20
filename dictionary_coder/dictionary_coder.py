# -*- coding: utf-8 -*-
#!/usr/bin/python

#   Copyright 2017 Robert Focke
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import itertools
from string import ascii_lowercase

class DCoder:
	coding = {}

	def __init__(self, initstr):
		if len(initstr) == 26:
			for code, letter in zip(initstr, ascii_lowercase):
				self.coding[letter] = code
		else:
			raise ValueError('The input string should be 26 letters in order, showing what the coding to be used is.')

	def get_mapping(self):
		return self.coding

	def encode(self, to_encode):
		outputstr = ''
		for char in to_encode:
			if char.lower() in ascii_lowercase:
				outputstr += self.coding[char]
		return outputstr

	def quick_decode(self, to_decode):
		outputstr = ''
		for char in to_decode:
			for key, val in self.coding.iteritems():
				if char == val:
					outputstr += key
					break
		return outputstr

	def full_decode(self, to_decode):
		# find conflicting dictionary keys:
		dictionary_conflicts = {}
		for key, val in self.coding.iteritems():
			for key2, val2 in self.coding.iteritems():
				if val == val2:
					if val in dictionary_conflicts.keys():
						if not key in dictionary_conflicts[val]:
							dictionary_conflicts[val].append(key)
					else:
						dictionary_conflicts[val] = []
						dictionary_conflicts[val].append(key)

		# check how many collisions we have and size of collision space
		outputstrfmt = ''
		collisions = []
		for char in to_decode:
			if char in dictionary_conflicts.keys():
				outputstrfmt += '*'
				collisions.append(char)
			else:
				for key, val in self.coding.iteritems():
					if char == val:
						outputstrfmt += key

		# serialise outputstrfmt
		collision_space = []
		counter = 0
		for char in outputstrfmt:
			if char == '*':
				collision_space.append(dictionary_conflicts[collisions[counter]])
				counter += 1
			else:
				collision_space.append([char])

		# solve
		outputstrs = list(itertools.product(*collision_space))

		# format output
		returnstrs = []
		for output in outputstrs:
			returnstrs.append(''.join(output))

		return returnstrs
			
