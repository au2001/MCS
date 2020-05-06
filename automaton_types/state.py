#!/usr/bin/env python3

class State(object):

	def __init__(self, automaton, state_id, initial=False, terminal=False):
		super(State, self).__init__()

		self.automaton = automaton
		self.state_id = state_id
		self.transitions_from = set()
		self.transitions_to = set()
		self.initial = initial
		self.terminal = terminal

		self.automaton.states.add(self)
		if initial:
			self.automaton.initial_states.add(self)
		if terminal:
			self.automaton.terminal_states.add(self)

	def copy(self, automaton=None):
		if automaton is None:
			automaton = self.automaton

		return State(automaton, self.state_id, self.initial, self.terminal)

	def remove(self):
		for transition in self.transitions_from:
			transition.remove()

		for transition in self.transitions_to:
			transition.remove()

		self.automaton.states.remove(self)
		if self.initial:
			self.automaton.initial_states.remove(self)
		if self.terminal:
			self.automaton.terminal_states.remove(self)

	def get_next_states(self, letter):
		next_states = set()

		for transition in self.transitions_from:
			if transition.letter == letter:
				next_states.add(transition.state_to)

		return next_states

	def get_previous_states(self, letter):
		next_states = set()

		for transition in self.transitions_to:
			if transition.letter == letter:
				next_states.add(transition.state_from)

		return next_states
