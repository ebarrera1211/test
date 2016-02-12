import remote_cl

def create_output_file(list, name):
	f = open(name, 'w')
	f.write('\n'.join(list))
	f.close()

def split_copyright(file):
	cpu_failures = []
	df_failures = []
	fch_failures = []
	gnb_failures = []
	ids_failures = []
	mem_failures = []
	other_failures = []
	psp_failures = []
	for line in file.split('\n'):
		if 'Copyright header problem' in line:
			if '/Ccx/' in line:
				cpu_failures.append(line)
			elif '/Fabric/' in line:
				df_failures.append(line)
			elif '/Fch/' in line:
				fch_failures.append(line)
			elif '/Nbio/' in line:
				gnb_failures.append(line)
			elif '/Debug/' in line:
				ids_failures.append(line)
			elif '/Mem/' in line:
				mem_failures.append(line)
			elif '/Psp/' in line:
				psp_failures.append(line)
			else:
				other_failures.append(line)
	create_output_file(cpu_failures, 'cpu_copyright_failures.txt')
	create_output_file(df_failures, 'df_copyright_failures.txt')
	create_output_file(fch_failures, 'fch_copyright_failures.txt')
	create_output_file(gnb_failures, 'gnb_copyright_failures.txt')
	create_output_file(ids_failures, 'ids_copyright_failures.txt')
	create_output_file(mem_failures, 'mem_copyright_failures.txt')
	create_output_file(psp_failures, 'psp_copyright_failures.txt')
	create_output_file(other_failures, 'other_copyright_failures.txt')



ARGUMENTS = [['-t', '--test_type', 'Test Type that the log file belongs'], \
            ['-f', '--file', 'File that needs to be parsed']]

CONFIG_FILE = __file__.replace('.py', '.cfg')

ARGS = remote_cl.arguments_parser(ARGUMENTS, CONFIG_FILE)

TEST_TYPE = ARGS['test_type']
if TEST_TYPE <> 'copyright' and TEST_TYPE <> 'c_style':
	print "test_type(-t) supports 'copyright' and 'c_style' only"
	exit(1)
FILE_NAME = ARGS['file']
if FILE_NAME == '':
	print "file (-f) is required, this is the file needed to be parsed"
	exit(1)

FILE = open(FILE_NAME, 'r')
R_FILE = FILE.read()
FILE.close()

split_copyright(R_FILE)