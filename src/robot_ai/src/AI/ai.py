#!/bin/usr/python
import os
from treelib import Tree, Node
from ia_classes import Task, Strategy, Action, Order
import xml.etree.ElementTree as ET

'''
CAUTION : This module requires the 'anytree' module. Install it with :
	pip install anytree
'''

class AI():
	def __init__(self, strategyname):
		self.xml_dirpath = os.path.dirname(__file__) + "/../Definitions/"
		self.AvailableStrategies = None
		orders = self.loadOrders()
		actions = self.loadActions(orders)
		self.Strategy = self.loadStrategy(strategyname, actions, orders)


	def loadOrders(self):
		self.XML_ORDERS = ET.parse(self.xml_dirpath + "3_Orders.xml").getroot()

		orders = []
		for order_xml in self.XML_ORDERS:
			orders.append(Order(order_xml))
		return orders


	def loadActions(self, orders):
		self.XML_ACTIONS = ET.parse(self.xml_dirpath + "2_Actions.xml").getroot()

		actionnames = [action.attrib["ref"] for action in self.XML_ACTIONS]
		actions = []
		for action_xml in self.XML_ACTIONS:
			actions.append(Action(action_xml, actions, orders))
		return actions

		
	def loadStrategy(self, strategyname, actions, orders):
		self.XML_STRATEGIES = ET.parse(self.xml_dirpath + "1_Strategies.xml").getroot()
		self.AvailableStrategies = [child.attrib["name"] for child in self.XML_STRATEGIES]

		strategy_xml = self.XML_STRATEGIES.findall("strategy[@name='" + strategyname + "']")
		if len(strategy_xml) == 1:
			return Strategy(strategy_xml[0], actions, orders)
		else:
			print "FAIL Too many or no strategy to load with the given name. Aborting."


a = AI("Test1")









'''
	def load_json(self, definitions_dir, strategyname):
		treenode_strategy = Node(strategyname)

		with open(definitions_dir + "1_Strategies.json")                  as file_strategies :
			with open(definitions_dir + "2_Objectives.json")              as file_objectives :
				with open(definitions_dir + "3_Actions.json")             as file_actions    :
					with open(definitions_dir + "4_HardwareActions.json") as file_hwactions  :
						data_strategies = json.load(file_strategies)
						data_objectives = json.load(file_objectives)
						data_actions    = json.load(file_actions   )
						data_hwactions  = json.load(file_hwactions )

						strategy = Strategy(strategyname, data_strategies[strategyname])
						# print json.dumps(strategy, indent = 2)
						return None
'''
