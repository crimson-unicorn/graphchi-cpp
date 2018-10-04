import sys

def post_process(infile, outfile, size):
	"""
	Post process statistics file @infile generated by GraphChi and output @outfile.
	Converting to number of edges processed per second.
	@size is the batch size in GraphChi
	"""
	timer = 0.0
	edges = 0

	out = open(outfile, 'w')

	with open(infile, 'r') as f:
		for line in f:
			ts = float(line.strip())
			if ts == timer:
				edges += size
			elif ts > timer:
				while ts > timer:
					out.write(str(edges) + "\n")
					timer += 1
				edges += size
	f.close()
	out.close()

if __name__ == "__main__":
	if (len(sys.argv) < 4):
		print("""
			Usage: python stats.py <input_file> <output_file> <size>
		"""
		)
		sys.exit(1)

	post_process(sys.argv[1], sys.argv[2], int(sys.argv[3]))