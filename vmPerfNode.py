#!/usr/bin/python

import psutil

class vmPerfNode:
	def __init__(self, pid):
		self.pid = pid
		self.state = 1
		self.proc = psutil.Process(self.pid)

		self.clearStats()

	def getpid(self):
		return self.pid

	def collectStats(self):

		self.cpu.append(self.proc.get_cpu_percent(interval=None))
		self.mem.append(self.proc.get_memory_percent())
		self.dsk.append(len(self.proc.get_open_files()))

	def clearStats(self):
		self.cpu = []
		self.mem = []
		self.dsk = []

	def getAvgCPU(self):
		return (sum(self.cpu) / float(len(self.cpu)))

	def getAvgMem(self):
		return (sum(self.mem) / float(len(self.mem)))

	def getAvgDsk(self):
		return (sum(self.dsk) / float(len(self.dsk)))
