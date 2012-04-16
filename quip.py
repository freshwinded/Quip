# Copyright Robin Wallar 2011
# robin@wallar.ca 
# @freshwinded
# You may use quip under either the MIT License or the GNU General Public License (GPL) Version 2

import sys, os
mode =  sys.argv[1] if len(sys.argv)>1 else 'build'
quip = '__QUIPCSS__'
defs = open('quip.css').readlines()
def procFile(file):
	f = open (file, 'r')
	data = f.readlines()
	f.close()
	i = 0
	replace = None
	for line in data:
		for definition in defs:
			replaceVals = definition.replace('\n','').split(' = ')
			if len(replaceVals) > 1:
				search = '/*' + replaceVals[0] + '*/'
				index = line.find(search)
				if index != -1:
					line = line.replace(replaceVals[1]+search,quip).replace(search, quip)
					replaceCommentStart = line.find(quip)
					replaceStart = origReplace = line.rfind(' ', 0, index+1)
					
					if replaceStart == -1:
						replaceStart = line.rfind(':')
					
					if replaceStart == -1:
						replaceStart = line.rfind(';')
					if replaceStart == -1:
						replaceStart = line.rfind('{')
					if replaceStart == -1:
						replaceStart = line.rfind('\t')
					if replaceStart == -1:
						replaceStart = 0	
					
					replaceEnd = replaceCommentStart + len(quip)
					
					if replaceCommentStart != -1:
						begin = line[0:replaceStart+1]
						end  = line[replaceEnd:len(line)]
			
						if mode == "compile":
							replace = begin+replaceVals[1]+end
						elif mode == "build":
							replace = begin+replaceVals[1]+search+end
						line = replace
		data[i] = line
		i = i + 1
	print 'Processed: '+ file
	f = open (file, 'w')
	f.write(''.join(data))
	f.close()

def walk(arg, dir, flst):
	for file in flst:
		exts = file.split('.')
		filename = file.split(os.sep)
		if exts[len(exts)-1] == "css" and len(exts) > 1 and filename[len(filename)-1]!='quip.css':
			procFile(dir+os.sep+file)
		
if len(defs)>0: 
	os.path.walk(os.path.abspath(os.path.curdir), walk, None )
else:
	print 'No defintions found.' 