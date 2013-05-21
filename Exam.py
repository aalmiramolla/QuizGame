#!/usr/bin/python
from Question import *
import random
import os.path

class Exam:
	def __init__(self, file="questions/QUIZ.DAT"):
		self.questions=[]
		self.correct=[]
		self.exam=[]
		self.dFile=file
		if(self.checkFile()==True):
			self.openFile()
			print len(self.questions)
		else:
			print 'No existe fichero'
			exit()
	
	def reset(self):
		self.exam=[]
		self.correct=[]
	
	def checkFile(self):
		if os.path.exists(self.dFile) and os.path.isfile(self.dFile):
			return True
		else:
			return False
	
	def openFile(self):
		lineas = []
		fd = open(self.dFile)
		lineas=fd.readlines()
		fd.close()
		for i in range(0, len(lineas), 6):
			self.addQuestion(Question(lineas[i][0],lineas[i+1][:-1],lineas[i+2][:-1],lineas[i+3][:-1],lineas[i+4][:-1],lineas[i+5][:-1]))

	
	def addQuestion(self,question):
		self.questions.append(question)

	def printExam(self):
		if len(self.questions) < 5:
			print 'Dont exists questions'
		else:
			for i in range(5):
				number = random.randrange(0,len(self.questions))
				print "Question", i+1
				self.exam.append(self.questions[number])
				self.questions[number].printQuestion()
				self.correct.append(self.questions[number].correct)
			self.checkQuestions()
							
	def checkQuestions(self):
		print "\n\nCorrections:"
		for i in range(len(self.correct)):
			print "Youre answer for question",i+1,"is " + self.exam[i].playeranswer + " and the correct answer is " + self.exam[i].correctanswer
		print "You answer correctly",self.correct.count(True),"of",len(self.correct),"questions"
