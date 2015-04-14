#!/usr/bin/python

from subprocess import Popen
import vmPerfController

class vmPerfTest:
	def __init__(self, controller):
		self.controller = controller
		self.numVMs = input("Enter number of VMs: ")
		self.minutes = input("Enter number of minutes to monitor: ")

		for i in range(self.numVMs):
			proc = Popen(["./dummy.py", str(self.minutes)])
			self.controller.addNode(proc.pid)


	def monitor(self):
		self.controller.monitor(self.minutes)

	def report(self):
		records = self.controller.getStats()

		print "  VM   Avg_CPU_Util   Avg_Mem_Usage    Avg_Disk_Usage   Under_Utilized"
		print "----------------------------------------------------------------------"

		for i in range(len(records)):
			print "{:>5}{:>10.2f}{:16.2f}{:18.2f}{:10}".format(i,
					records[i][0], records[i][1], records[i][2], records[i][3])




if __name__ == "__main__":
	controller = vmPerfController.vmPerfController()

	test = vmPerfTest(controller)
	test.monitor()
	test.report()
