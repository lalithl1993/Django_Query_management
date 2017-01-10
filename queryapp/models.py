from django.db import models

class loginInfo(models.Model):    
	id1= models.IntegerField()                                
	uname= models.CharField(max_length=30)        
	pwd = models.CharField(max_length=15)                                

	def __str__(self):
		return self.uname


class student(models.Model):
	usn=models.CharField(max_length=10,blank=False)                                
	name= models.CharField(max_length=30,blank=False)        
	password = models.CharField(max_length=15,blank=False)                                

	def __str__(self):
		return self.usn


class teacher(models.Model):                             
	name= models.CharField(max_length=30,blank=False)        
	password = models.CharField(max_length=15,blank=False)                                

	def __str__(self):
		return self.name

class question(models.Model):                             
	question= models.CharField(max_length=500,blank=False) 
	status= models.IntegerField(default=0)                                      

	def __str__(self):
		return str(self.question)

class answer(models.Model):                             
	qid= models.IntegerField(blank=False) 
	answer= models.CharField(max_length=500,blank=False)                                     

	def __str__(self):
		return self.answer

