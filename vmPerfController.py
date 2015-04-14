#!/usr/bin/python

import sched, time
import datetime
import vmPerfNode

class vmPerfController:
	def __init__(self):
		self.nodes = []
		self.runFreq = 60 # once in a minute
		self.setThreshold(10, 20, 10)
	
	def setThreshold(self, cpuThreshold, memThreshold, dskThreshold):
		self.cpuThreshold = cpuThreshold
		self.memThreshold = memThreshold
		self.dskThreshold = dskThreshold
		

	def addNode(self, pid):
		node = vmPerfNode.vmPerfNode(pid)
		self.nodes.append(node)

	def deleteNode(self, pid):
		for node in self.nodes:
			if (node.getpid() == pid):
				self.nodes.remove(node)
				return

	def run(self, vmpTimer, starttime, minutes):

		for node in self.nodes:
			node.collectStats()

		currtime = datetime.datetime.now()
		elapsed = currtime - starttime
		if (elapsed < datetime.timedelta(seconds=minutes)):
			vmpTimer.enter(self.runFreq, 1, self.run,
					(vmpTimer, starttime, minutes,))

	def monitor(self, minutes):

		for node in self.nodes:
			node.clearStats()

		vmpTimer = sched.scheduler(time.time, time.sleep)
		starttime = datetime.datetime.now()

		vmpTimer.enter(self.runFreq, 1, self.run,
					(vmpTimer, starttime, minutes,))
		vmpTimer.run()

	def getStats(self):
		
		records = []
		for node in self.nodes:
			cpu = node.getAvgCPU()
			mem = node.getAvgMem()
			dsk = node.getAvgDsk()
			if (cpu < self.cpuThreshold or mem < self.memThreshold or dsk < self.dskThreshold):
				flag = 1
			else:
				flag = 0
			records.append([cpu, mem, dsk, flag])

		return (records)
