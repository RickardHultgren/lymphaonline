#!/usr/bin/python3
# -*- coding: ascii -*-
import sys

#for the graph function:
import os

#regex
import re

prefilecom = ""
filecom = ""
argvlen = len(sys.argv)
filename = ""

starts = list()
steps = 0
modegraph = False
modestate = False
filecheck = False
modeexe = False
modeshow = False
modemap = False
exe_list = list()
show_list = list()
map_list = list()
series = list()
substates = list()
nextstates = list()
specs = list()
tipoint1 = None
tipoint2 = None
operator1 = None
operator2 = None
valju = str()

object_list = list()
exe_objects = list()

'''
class Factor:
	def __init__(self, name, tipoint1, operator1, next_list, spec_list, cont_list):
        		
		#list of next nodes:
		#next_list = next_list
		self.next_list = []
		
		#list of specifications:
		#spec_list = spec_list
		self.spec_list = []

		#list of contents:
		#cont_list = cont_list
		self.cont_list = []

		#name
		self.name = name
		
		#tipping point
		self.tipoint1 = tippoint
		
		#relational operator1
		self.operator1 = operator1

class Event:
	def __init__(self, name, next_list, spec_list, cont_list):
        		
		#list of next nodes:
		#next_list = next_list
		self.next_list = []
		
		#list of specifications:
		#spec_list = spec_list
		self.spec_list = []

		#list of contents:
		#cont_list = cont_list
		self.cont_list = []

		#name
		self.name = name
'''

class Statement:
	def __init__(self, flow, name, tipoint1, tipoint2, valju, operator1, operator2, next_list, cont_list, spec_list):
        
		self.flow = int(flow)
        		
		#list of next nodes:
		#next_list = next_list
		self.next_list = list(next_list)
		
		#list of specifications:
		#spec_list = spec_list
		self.spec_list = list()

		#list of contents:
		#cont_list = cont_list
		self.cont_list = list(cont_list)

		#name
		self.name = name
		
		#tipping point
		self.tipoint1 = tipoint1

		#tipping point
		self.tipoint2 = tipoint2
		
		#relational operator
		self.operator1 = operator1

		#relational operator
		self.operator2 = operator2


		#valju
		#if valju != 0 :print (valju)
		if valju == "0" :self.valju = "0"
		else: self.valju = "1"
		#if self.int(valju) != 0 :print ("%s:%s" % (self.name, self.int(valju)))

#object_list.append(Event(i))
#object_list.append(Factor(i))

def exefunc() :
# Add objects.name to show_list.
	global object_list
	global starts
	global show_list
	global steps
	
	
	
	if modegraph == True:
		graphstr = 'digraph lympha {\nnode [shape=record];'	
	for step in range(0,steps):
		nextstates = list()
		for start in starts:
			#for index,obj in enumerate(object_list):
			for obj in object_list:
				if ("%s" % obj.name) == ("%s" % start) :
					subfactors = list()
					for cont_object in obj.cont_list :
						for item in object_list:							
							if cont_object == item.name :
								subfactors.append(item.int(valju))
					sum1 = subfactors.count(1)
					sum0 = subfactors.count(0)
					if obj.operator1	!= None and int(obj.valju) is None :
						if obj.operator1 == "equiv" and obj.tipoint1 == sum1:
							obj.valju = str("1")
						elif obj.operator1 == "geq" and obj.tipoint1 >= sum1:
							obj.valju = str("1")
						elif obj.operator1 == "leq" and obj.tipoint1 <= sum1:
							obj.valju = str("1")
						elif obj.operator1 == "no" and obj.tipoint1 != sum1:
							obj.valju = str("1")
						elif obj.operator1 == "g" and obj.tipoint1 > sum1:
							obj.valju = str("1")
						elif obj.operator1 == "l" and obj.tipoint1 < sum1:
							obj.valju = str("1")
						else:
							obj.valju = str("0")	
					#else:
						#obj.valju = str("1")	
###connect to funcs


					if obj.valju == "1" :
						print ("step %s: %s; exe" % (step+1, start))
					else:
						print ("step %s: %s"% (step+1, start))
					
					
					if modegraph == True:
						if obj.valju == str("1"):
							graphstr += ('"%s" [label="step %s: %s", fillcolor=yellow, style=filled] \n' % (start,step+1,start))										
						else:
							graphstr += ('"%s" [label="step %s: %s"] \n' % (start,step+1,start))										
					for next_object in obj.next_list :
						if obj.name != next_object and start != next_object and step != steps-1:
							graphstr += ('"%s" -> "%s" \n' % (start,next_object))
							nextstates.append(next_object)
		seen2 = {}
		nextstates = [seen2.setdefault(x, x) for x in nextstates if x not in seen2]
		del starts[:]
		starts = list(nextstates)
		del nextstates[:]
	graphstr += '}'
	open('lympha.dot', 'w').close()
	outputfile = open("lympha.dot", "w")
	outputfile.write(graphstr)
	outputfile.close()
	cmd = 'dot lympha.dot -Tps -o lympha.pdf'
	os.system(cmd)


def showfunc():
# Add objects.name to show_list.
	global object_list
	global starts
	global show_list
	global steps
	if modegraph == True:
		graphstr = 'digraph lympha {\nnode [shape=record];'
	for step in range(0,steps):
		nextstates = list()
		for start in starts:
			for obj in object_list:
				if ("%s" % obj.name) == ("%s" % start) :
					print ("step %s: %s" % (step+1, start))
					if modegraph == True:
						graphstr += ('"%s" [label="step %s: %s"] \n' % (start,step+1,start))					
					for next_object in obj.next_list :
						if obj.name != next_object and start != next_object and step != steps-1:
							graphstr += ('"%s" -> "%s" \n' % (start,next_object))
							nextstates.append(next_object)
		seen2 = {}
		nextstates = [seen2.setdefault(x, x) for x in nextstates if x not in seen2]
		del starts[:]
		starts = list(nextstates)
		del nextstates[:]
	graphstr += '}'
	open('lympha.dot', 'w').close()
	outputfile = open("lympha.dot", "w")
	outputfile.write(graphstr)
	outputfile.close()
	cmd = 'dot lympha.dot -Tps -o lympha.pdf'
	os.system(cmd)

def mapfunc():
# Add objects.name to show_list.
	global object_list
	global starts
	global show_list
	global steps
	
	
	
	if modegraph == True:
		graphstr = 'digraph lympha {\nnode [shape=record];'	
	for step in range(0,steps):
		nextstates = list()
		for start in starts:
			#for index,obj in enumerate(object_list):
			for obj in object_list:

			
				if ("%s" % obj.name) == ("%s" % start) :

					###
					prevalju = "0"		
					if len(obj.cont_list) != 0 :
						subfactors = list()
						for cont_object in obj.cont_list :
							for item in object_list:							
								if cont_object == item.name :
									#if item.name != "":
									#	print("name: %s ; value: %s"%(item.name, item.int(valju)))
									subfactors.append(item.valju)
						
						
						
						sum1 = subfactors.count("1")
						sum0 = subfactors.count("0")
						print (obj.tipoint1, sum1)
						if obj.operator1 != None and obj.valju is None :
							if obj.operator1 == "equiv" and int(obj.tipoint1) == int(sum1):
								prevalju = str("1")
							elif obj.operator1 == "geq" and int(obj.tipoint1) >= int(sum1):
								prevalju = str("1")
							elif obj.operator1 == "leq" and int(obj.tipoint1) <= int(sum1):
								prevalju = str("1")
							elif obj.operator1 == "no" and int(obj.tipoint1) != int(sum1):
								prevalju = str("1")
							elif obj.operator1 == "g" and int(obj.tipoint1) > int(sum1):
								prevalju = str("1")
							elif obj.operator1 == "l" and int(obj.tipoint1) < int(sum1):
								
								prevalju = str("1")
							else:
								prevalju = str("0")
						#else:
							#obj.valju = str("1")	
							obj.valju = prevalju
												
					###
					###many tipoint1s?
					#algorithm algebra:
					elif len(obj.cont_list) < 1 :
						
						for algobj in object_list:
							###
							if  algobj.name == ("%s" % obj.valju):
								sum1 = ("%s" % algobj.valju)
								if obj.operator1 != None and obj.valju != "" :
									if obj.operator1 == "equiv" and int(obj.tipoint1) == int(sum1):
										
										prevalju = "1"
									elif obj.operator1 == "geq" and int(obj.tipoint1) >= int(sum1):
										
										prevalju = "1"
									elif obj.operator1 == "leq" and int(obj.tipoint1) <= int(sum1):
										
										print ("PREVALJU: %s"%prevalju)
										prevalju = "1"
									elif obj.operator1 == "no" and int(obj.tipoint1) != int(sum1):
										
										prevalju = "1"
									elif obj.operator1 == "g" and int(obj.tipoint1) > int(sum1):
										
										prevalju = "1"
									elif obj.operator1 == "l" and int(obj.tipoint1) < int(sum1):
										
										prevalju = "1"
									else:
										prevalju = str("0")	
								if  algobj.name == ("%s" % obj.valju):
									sum1 = ("%s" % algobj.valju)										
									if obj.operator2 != None :
										if obj.operator2 == "equiv" and int(obj.tipoint2) == int(sum1) and prevalju == "1" :
											prevalju = "1"
										elif obj.operator2 == "geq" and int(obj.tipoint2) >= int(sum1) and prevalju == "1" :
											prevalju = "1"
										elif obj.operator2 == "leq" and int(obj.tipoint2) <= int(sum1) and prevalju == "1" :
											prevalju = "1"
										elif obj.operator2 == "no" and int(obj.tipoint2) != int(sum1) and prevalju == "1" :
											prevalju = "1"
										elif obj.operator2 == "g" and int(obj.tipoint2) > int(sum1) and prevalju == "1" :
											prevalju = "1"
										elif obj.operator2 == "l" and int(obj.tipoint2) < int(sum1) and prevalju == "1" :
											prevalju = "1"
										else:
											prevalju = str("0")									
								obj.valju = prevalju
								
					if len(obj.operator1) < 1 :
							if obj.flow == 0 :
								obj.valju = "0"				
												
					if obj.valju == str("1"):
						print ("step %s: %s; exe" % (step+1, start))
					#elif obj.valju == str("0"):
					else:
						for k in obj.next_list:
							for l in object_list:
								if k==l.name:
									l.flow = 0

						print ("step %s: %s"% (step+1, start))
					
					if modegraph == True:
						if obj.valju == str("1"):
							graphstr += ('"%s" [label="step %s: %s", fillcolor=yellow, style=filled] \n' % (start,step+1,start))										
						else:
							graphstr += ('"%s" [label="step %s: %s"] \n' % (start,step+1,start))										
					for next_object in obj.next_list :
					
						if obj.name != next_object and start != next_object and step != steps-1:
							graphstr += ('"%s" -> "%s" \n' % (start,next_object))
							nextstates.append(next_object)
		seen2 = {}
		nextstates = [seen2.setdefault(x, x) for x in nextstates if x not in seen2]
		del starts[:]
		starts = list(nextstates)
		del nextstates[:]
	graphstr += '}'
	open('lympha.dot', 'w').close()
	outputfile = open("lympha.dot", "w")
	outputfile.write(graphstr)
	outputfile.close()
	cmd = 'dot lympha.dot -Tps -o lympha.pdf'
	os.system(cmd)

def statefunc():
	global object_list
	for obj in object_list:
		print("%s" % obj.name)	



def new(name, flow, tipoint1, tipoint2, valju, operator1,  operator2, next_list, cont_list, spec_list):
	#if int(valju) != 0:
	#			print(int(valju))
	#print(int(valju))
	global object_list
	nameused = False
	for index, obj in enumerate(object_list):
		
		if (" %s " % obj.name) == name:
			#print("| %s |;|%s|" % (obj.name,name))
			nameused = True
			if tipoint1 is None:
				object_list[index].tipoint1 == tipoint1
			if valju is None:
				
				object_list[index].int(valju) == int(valju)
				if int(valju) != 0: print("%s:%s\n" % (object_list[index].int(valju), int(valju)))
			if operator1 != None:
				object_list[index].operator1 == operator1				
			if next_list != None:
				object_list[index].next_list == next_list				
			if cont_list != None:
				object_list[index].cont_list == cont_list
			if spec_list != None:
				object_list[index].spec_list == spec_list								
	if nameused == False:
		#if int(valju) != 0: print("%s:%s\n" % (object_list[index].int(valju), int(valju)))
		name = name.replace(' ', '')
		#if int(valju) !=0 :print(int(valju))
		statement = Statement(flow, name, tipoint1, tipoint2, valju, operator1, operator2, next_list, cont_list, spec_list)
		#statement = Statement(name, tipoint1, operator1, list(next_list), cont_list, spec_list)
		#if next_list != [] :
		#	statement.next_list = list(next_list)
		#if cont_list != [] :
		#	pass
		object_list.append(statement)

def assasement(eqobjs):
	#0 = operator1
	#1 = tipping point
	#2 = content
	try:
		scale = eqobjs.split('==')
		scale.insert(0, "equiv")
		return eqobjs
		#break
	except:
		pass
	try:
		scale = eqobjs.split('>=')
		scale.insert(0, "geq")
		return eqobjs
		#break
	except:
		pass
	try:
		scale = eqobjs.split('<=')
		scale.insert(0, "leq")
		return eqobjs
		#break
	except:
		pass
	try:
		scale = eqobjs.split('!=')
		scale.insert(0, "no")
		return eqobjs
		#break
	except:
		pass
	try:
		scale = eqobjs.split('>')
		scale.insert(0, "g")
		return eqobjs
		#break
	except:
		pass
	try:
		scale = eqobjs.split('<')
		scale.insert(0, "l")
		return eqobjs
		#break
	except:
		pass


def lexer():
#loop problem in the same serie
	global object_list

	nexts = list()
	conts = list()
	#make new nodes in database
	for serie in series:
		arrowobjs = serie.split('->')
		count = 0
		nexts = list()
		conts = list()
		specs = list()
		flow = int()
		tipoint1 = int()
		operator1 = str()
		valju = str()
		scale = list()
		for anobj in arrowobjs:
###
			#eqobjs = anobj.split(' = ',1)
			#anobj.replace(" ","")
			eqobjs = re.compile("[^=|<|>|!]=[^=|<|>|!]").split(anobj)

			anobj.replace(" ","")
			new(eqobjs[0], flow, tipoint1, tipoint2, valju, operator1, operator2, nexts,conts, specs)			
	seen = {}
	object_list = [seen.setdefault(x.name, x) for x in object_list if x.name not in seen]
	#Connect the database nodes
	
	for flowobj in object_list:
		flowobj.flow = 1
	
	for serie in series:
		arrowobj = serie.split('->')
		count = 0
		nexts = list()
		conts = list()
		# many nexts vs one
		for i in range(len(arrowobj)):
		#for anobj in arrowobj:
			#print (arrowobj[i]):
			for bnobj in object_list :
				if i!=0 and (" %s " % bnobj.name) == ("%s" % arrowobj[(i-1)]):
					nexting = ""
					nexting = arrowobj[i].replace(" ","")
					if not nexting == "":
						bnobj.next_list.append(nexting)
			seen3 = {}
			bnobj.next_list = [seen3.setdefault(x, x) for x in bnobj.next_list if x not in seen3]
			
			
	for serie in series:
		count = 0
		# many nexts vs one
		anobj = serie
		
		if anobj != "" and " = " in anobj:
			for bnobj in object_list :
				#int(valju) or tipoint1
				#sides =	anobj.split(' = ')
				sides = re.compile("[^=|<|>|!]=[^=|<|>|!]").split(anobj)
				side1 = sides[0]
				side1 = side1.replace(" ","")
				
				if side1 == bnobj.name :
					parts = sides[1]
					parts = parts.replace(" ","")
					if parts.isdigit() == True:	
						bnobj.valju = parts
					else:
						subfactorings = []
						if bnobj.operator1 != None :
							if "==" in parts :
								subfactorings = parts.split("==")
								bnobj.operator1="equiv"
							elif ">=" in parts :
								subfactorings = parts.split(">=")
								bnobj.operator1="geq"						
							elif "<=" in parts :
								subfactorings = parts.split("<=")
								bnobj.operator1="gleq"
							elif "!=" in parts :
								subfactorings = parts.split("!=")
								bnobj.operator1="no"
							elif ">" in parts :
								subfactorings = parts.split(">")
								bnobj.operator1="g"
							elif "<" in parts :
								subfactorings = parts.split("<")
								bnobj.operator1="l"
						else:
							if "==" in parts :
								subfactorings = parts.split("==")
								bnobj.operator2="equiv"
							elif ">=" in parts :
								subfactorings = parts.split(">=")
								bnobj.operator2="geq"						
							elif "<=" in parts :
								subfactorings = parts.split("<=")
								bnobj.operator2="gleq"
							elif "!=" in parts :
								subfactorings = parts.split("!=")
								bnobj.operator2="no"
							elif ">" in parts :
								subfactorings = parts.split(">")
								bnobj.operator2="g"
							elif "<" in parts :
								subfactorings = parts.split("<")
								bnobj.operator2="l"
						parts = parts.replace(" ","")
						#if re.match(r"\|\{[A-Za-z0-9.,:-_ ?]*\}\|", parts):
						if "|{" in parts and "}|" in parts :
							parts = parts.replace("|{","")
							parts = parts.replace("}|","")
							partlist = parts.split(",")
							
							for party in partlist:
								bnobj.cont_list.append(party)
								bnobj.valju = None
						else:
						###
						#elif len(partlist) == 2 :
							bnobj.valju = subfactorings[1]
							
							#valju(bnobj.valju) = [int(s) for s in sides[1].split()][1]
							
					sidelist = re.compile("\=\=|<\=|>\=|\!\=|<|>]").split(sides[1])
					#sidelist = [int(s) for s in sides[1].split() if s.isdigit()]
					#bnobj.tipoint1 = sidelist[0]
					try:
						bnobj.tipoint1 = (sidelist[0]).replace(" ","")
						#bnobj.tipoint1 = sidelist[0]	
					except:
						pass
					try:
						if bnobj.tipoint1 != None :
							bnobj.tipoint2 = (sidelist[0]).replace(" ","")
							#bnobj.tipoint1 = sidelist[0]								
					except:
							pass							
				
	#seen = {}
	#object_list = [seen.setdefault(x.name, x) for x in object_list if x.name not in seen]			

	if modeexe == True:
		exefunc()	
	if modeshow == True:
		showfunc()
	if modemap == True:
		mapfunc()
	if modestate == True:
		statefunc()	
if __name__=='__main__':
	for x in range(0, argvlen):
		if sys.argv[x] == "-f":
			prefilecom = sys.argv[x]
			filecom = sys.argv[x+1]
			filename = filecom
			textfile = open(filename, 'r')
			filetext = textfile.read()
			filetext = filetext.replace('\n', ' ')
			filetext = filetext.replace('  ', ' ')
			series = filetext.split(';')
			filecheck = True
		if sys.argv[x] == "-h":
			print ('-h for help\n-f file\n-map OR -show\n-graph\n-start "start node"\n-steps amount of steps')
		if sys.argv[x] == "-exe":
			modeexe = True
		if sys.argv[x] == "-show":
			modeshow = True
		if sys.argv[x] == "-map":
			modemap = True		
		if sys.argv[x] == "-graph":
			modegraph = True					
		if sys.argv[x] == "-statements":
			modestate = True	
		if sys.argv[x] == "-steps":
			steps = int(sys.argv[x+1])
		if sys.argv[x] == "-start":
			starts.append(sys.argv[x+1])
# Execute functions that are connected to the arguments:
	if filecheck == True:
		lexer()

#271
