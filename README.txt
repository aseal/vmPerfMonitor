A. Introduction

	This document explains how to use this tool.

B. Prerequisite

	- This tool requires Python 2.7 or later (not Python 3)
	- It also requires psuti, you can get it by (or equivalend command) -
		apt-get install python-psutil
	
C. Screenshot

	$ ./vmPerfTest.py 
	Enter number of VMs: 5
	Enter number of minutes to monitor: 5

	  VM   Avg_CPU_Util   Avg_Mem_Usage    Avg_Disk_Usage   Under_Utilized
	----------------------------------------------------------------------
    	0      0.00           69.15             75.00         1
	    1      0.00           48.62             46.00         1
    	2   2073.33          130.91             84.00         0
	    3   2073.33          181.44             41.00         0
    	4   2090.00          178.05             11.00         0
