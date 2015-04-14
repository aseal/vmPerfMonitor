# VM Performance Monitor

VM Performance Monitor monitors the VMs for CPU Utilization, memory and disk
usage. It computes the average usage, which can be used to decommision under
utilized VMs at the conclusion of this program.

## Usage

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
