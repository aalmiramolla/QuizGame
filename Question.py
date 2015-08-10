#!/usr/bin/python
# -*- coding: utf-8 -*-

class Question:
        def __init__(self, question, answers, correctAnswer, topic, image=None):
                self.question = question
                self.correctanswer = correctAnswer
                self.answers = answers
                self.topic = topic
                self.image = image
		
        def checkAnswer(self, answer):
                if (answer == self.correctAnswer):
                        self.correct=True			
