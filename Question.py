#!/usr/bin/python

class Question:
	def __init__(self,anC,question,an1,an2,an3,an4):
		self.question=question
		self.answer1=an1
		self.answer2=an2
		self.answer3=an3
		self.answer4=an4
		self.correctanswer=anC
		self.correct=False
		self.playeranswer="E"
		
	def checkAnswer(self):
		if (self.playeranswer == self.correctanswer):
			self.correct=True
		
	def setPlayerAnswer(self):
		self.playeranswer=str(raw_input("Youre answer-->"))
		self.checkAnswer()

	def printQuestion(self):
		print self.question
		print "\tA) "+self.answer1
		print "\tB) "+self.answer2
		print "\tC) "+self.answer3
		print "\tD) "+self.answer4
		while (self.playeranswer<"A" or self.playeranswer>"D"):
			self.setPlayerAnswer()
			
