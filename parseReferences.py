import re

def parseReferences(input_list):
	output_list = []
	for item in input_list:
		titles = re.findall('"([^"]*)"', item)
		if titles:
			for title in titles:
				print title
	
#Data-Driven Documents

if __name__ == '__main__':
	list = [u'D. Sridhara, T. Fuja, and R. M. Tanner, "Low density parity check codes from permutation matrices," Conf. on Info. Sciences and Systems, The John Hopkins University, March 2001.', u'D. Hocevar, "LDPC code construction with flexible hardware implementation," in Proc. ICC, 2003.', u'D. J. C. Mackay, "Good error correcting codes based on very sparse matrices," IEEE Trans. Inform. Theory, vol. 45, pp. 399-431, March 1999.', u'T. Zhang and K. K. Parhi, "A 54 MBPS (3, 6)-regular FPGA LDPC decoder," in Proc. IEEE SIPS, pp. 127-132, 2002.', u'A. J. Blanksby and C. J. Rowland, "A 690-mW 1-Gb/s 1024-b, rate-1/2 low-density parity-check code decoder," IEEE J. Solid-State Circuits, vol. 37, pp. 404-412, 2002.', u'Y. Chen and K. K. Parhi, "High throughput over-lapped message passing for low density parity check codes," in Proc. IEEE/ACM GLSVLSI, pp. 245-248, 2003.']
	parseReferences(list)
		