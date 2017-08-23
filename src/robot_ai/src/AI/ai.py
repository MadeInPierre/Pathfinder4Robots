#!/bin/usr/python
import os, json
from treelib import Tree, Node
from ia_classes import AI_ITEM, Strategy, Objective, Action

'''
CAUTION : This module requires the 'anytree' module. Install it with :
	pip install anytree
'''

class AI():
	def __init__(self, StrategyNameToApply):
		self.AITree = self.load_json(os.path.dirname(__file__) + "/../Definitions/", StrategyNameToApply)

	def load_json(self, definitions_dir, StrategyNameToApply):
		treenode_strategy = Node(StrategyNameToApply)

		with open(definitions_dir + "1_Strategies.json")                  as file_strategies :
			with open(definitions_dir + "2_Objectives.json")              as file_objectives :
				with open(definitions_dir + "3_Actions.json")             as file_actions    :
					with open(definitions_dir + "4_HardwareActions.json") as file_hwactions  :
						data_strategies = json.load(file_strategies)
						data_objectives = json.load(file_objectives)
						data_actions    = json.load(file_actions   )
						data_hwactions  = json.load(file_hwactions )

						strategy = Strategy(StrategyNameToApply, data_strategies[StrategyNameToApply])
						# print json.dumps(strategy, indent = 2)
						
						'''
						for objective in strategy["objectives"]:
							Node(Objective(objective["name"], objective), parent = treenode_strategy)
						'''
						return None


a = AI("Strategy 1")


class TreeManager():
	def __init__(self):
		self.Tree = Tree()
		self.Tree.create_node(object)
		self.Tree.show()

	
	def addNode(self, obj):
		apss

t = TreeManager()

