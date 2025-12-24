from django.db import models

class adminlogin(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)

class success_stories(models.Model):
    story_title = models.CharField(max_length=30)
    Description = models.CharField(max_length=100)

class Job_Postings(models.Model):
    Job = models.CharField(max_length=30,default=False)
    Title = models.CharField(max_length=30)
    Qualification = models.CharField(max_length=50)
    Percentage = models.IntegerField()
    Experience = models.IntegerField(help_text="In Years")
    Last_date = models.DateField()
    Location = models.CharField(max_length=100)
    Salary = models.DecimalField(max_digits=10,decimal_places=2)

class CreateAgent(models.Model):
    Agent_Name = models.CharField(max_length=30)
    Password =models.CharField(max_length=50)
    Dob = models.DateField()
    Contact_Number = models.IntegerField()
    Qualification = models.CharField(max_length=30)
    Address	= models.CharField(max_length=100)

class Tips(models.Model):
    Name = models.CharField(max_length=30)
    Location = models.CharField(max_length=50)
    Suggession = models.CharField(max_length=100)

class Applicants(models.Model):
    JOB_TITLE = models.CharField(max_length=30)
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Dob = models.DateField()
    Qualification = models.CharField(max_length=30)
    percentage = models.IntegerField()
    Institute = models.CharField(max_length=30)
    Experience = models.IntegerField()
    Contact_Number = models.IntegerField()

class Assign_Agent(models.Model):
    case_id = models.IntegerField()
    agent_id = models.IntegerField()
    Agent_Name = models.CharField(max_length=30)

class CaseDetails(models.Model):
    agent_id = models.IntegerField()
    case_id = models.IntegerField()
    case_name= models.CharField(max_length=30)
    evidence= models.CharField(max_length=30)
    status= models.CharField(max_length=30)

class Defence_Login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)

class CaseCreation(models.Model):

    case_name = models.CharField(max_length=30)
    case_details = models.CharField(max_length=30)
    doc = models.DateField()
    evidence = models.CharField(max_length=30)