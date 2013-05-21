#!/usr/bin/python

import sys
from Exam import Exam

##########################################################################################################################################

##########################################################################################################################################
### The menu
##########################################################################################################################################
def run(exam):
	exam.printExam()
	exam.reset()
##########################################################################################################################################

##########################################################################################################################################
### The menu
##########################################################################################################################################
def menu():
	print "############## QUIZ GAME ##############"
	print "A game for answer some random questions"
	print "\t1) Play"
	print "\tq) Exit"
	print "#######################################"
##########################################################################################################################################

##########################################################################################################################################
### The main
##########################################################################################################################################
def main():
	choose="0"
	if len(sys.argv) == 2:
		exam = Exam(sys.argv[1])
	else:
		exam = Exam()
	while choose!="q":
		menu()
		choose=str(raw_input("Option-->"))
		if choose == "q":
			print "The game will exit\nBye!!"
			exit
		elif choose == "1":
			run(exam)

##########################################################################################################################################

if __name__=="__main__":
	main()
