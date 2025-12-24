from django.shortcuts import render
from django.views.generic import UpdateView

from app_cybernatics_protetor.models import adminlogin, success_stories, Job_Postings, CreateAgent, Tips, Applicants, \
    Assign_Agent, CaseDetails, CaseCreation

def AdminLogin(request):
    username = request.POST.get('name')
    password = request.POST.get('password')
    #
    # adminlogin(username=username,password=password).save()
    # return render(request,"admin.html")
    qs = adminlogin.objects.filter(username=username,password=password)
    if qs:
        return render(request,"welcomeadmin.html")
    else:
        return render(request,"admin.html",{'message':'Invalid User'})

def Success_Stories(request):
    story_title = request.POST.get("t1")
    Description = request.POST.get("t2")
    success_stories(story_title=story_title,Description=Description).save()
    return render(request,"storyadded.html")

def PostSaved(request):
    job = request.POST.get('job')
    title = request.POST.get('name')
    qualification = request.POST.get('qualification')
    percentage = request.POST.get('percentage')
    Experience = request.POST.get('exp')
    LastDate = request.POST.get('lastdate')
    Location = request.POST.get('location')
    Salary = request.POST.get('salary')
    Job_Postings(Job=job,Title=title,
                 Qualification=qualification,Percentage=percentage,
                 Experience=Experience,Last_date=LastDate,Location=Location,
                 Salary=Salary).save()
    return render(request,"jobposting.html",{'message':'Posted Successfully'})

def AgentRegister(request):
    Agent_Name = request.POST.get("name")
    Password = request.POST.get("password")
    Dob = request.POST.get("dateofbirth")
    Contact_Number = request.POST.get("cno")
    Qualification = request.POST.get("quali")
    Address = request.POST.get("adress")
    CreateAgent(Agent_Name=Agent_Name,Password=Password,Dob=Dob,Contact_Number=Contact_Number,Qualification=Qualification,
                Address=Address).save()

    return render(request,"createagent.html",{'message':'Created Successfully'})

def ViewAgents(request):
    qs = CreateAgent.objects.all()
    return render(request,"viewallagents.html",{'data':qs})

def Updateagent(request):
    qs = CreateAgent.objects.all()
    return render(request, "updateagent.html", {'data': qs})

class editagent(UpdateView):
    model = CreateAgent
    template_name = "editedagent.html"
    fields = ('Agent_Name','Dob','Contact_Number','Qualification','Address')
    success_url = '/editagent/'

def ViewJobs(request):
    qs = Job_Postings.objects.filter( Job ="Agent")
    if qs:
        return render(request,"viewjobs.html",{'data':qs})

def ViewClerkjobs(request):
    # job = Job_Postings.objects.get()
    qs = Job_Postings.objects.filter(Job="clerk")
    if qs:
        return render(request,"clerkjobs.html",{'data':qs})

def Suggest(request):
    name = request.POST.get("name")
    location = request.POST.get("location")
    suggession = request.POST.get('suggession')
    Tips(Name=name,Location=location,Suggession=suggession).save()
    return render(request,"tips.html",{'message':'sent successfully'})

def ViewApplicants(request):
    JOB_TITLE = request.POST.get("name")
    FN = request.POST.get("fn")
    LN = request.POST.get("ln")
    Dob = request.POST.get("dob")
    Qualification = request.POST.get("quali")
    percentage = request.POST.get("percentage")
    Institute = request.POST.get("institute")
    Experience = request.POST.get("exp")
    Contact_Number = request.POST.get("cno")
    Applicants(JOB_TITLE=JOB_TITLE,First_Name=FN,Last_Name=LN,Dob=Dob,Qualification=Qualification,
               percentage=percentage,Institute=Institute,Experience=Experience,Contact_Number=Contact_Number).save()
    return render(request,"apply_jobs.html",{'message':'saved'})

def ShowApplicants(request):
    qs = Applicants.objects.all()
    return render(request,"showapplicants.html",{'data':qs})

def Agent_Login(request):
    Agent_Name = request.POST.get("name")
    Password = request.POST.get("password")
    qs = CreateAgent.objects.filter(Agent_Name=Agent_Name,Password=Password)
    if not qs:
        return render(request,"agent_login.html",{'message':'Invalid Agent'})
    else:
        return render(request,"welcomeagent.html")

def Assign_Agent(request):
    agent_id = request.POST.get("agent id")
    case_id = request.POST.get("case id")
    case_name = request.POST.get("name")
    evidence = request.POST.get("evidence")
    status = request.POST.get("status")
    CaseDetails(agent_id=agent_id,case_id=case_id,case_name=case_name,evidence=evidence,status=status).save()
    return render(request,"appointcaseid.html",{'message':'saved'})

def showAgent(request):
    Agent_Name = request.POST.get('name')
    qs = CreateAgent.objects.filter(Agent_Name=Agent_Name)
    if qs:
        return render(request,"appointcaseid.html")
    else:
        return render(request, "appoint_agent.html", {'message': 'Invalid'})

def GetDetails(request):
    agent_id = request.POST.get("agent id")
    qs = CaseDetails.objects.filter(agent_id=agent_id)
    if qs:
        return render(request, "agent_case.html",{'data':qs})
    else:
        return render(request, "casedetails.html", {'message': 'Invalid'})

def upDetails(request):
    qs = CaseDetails.objects.all()
    return render(request,"updateevidence.html",{"data":qs})

class UpEvidence(UpdateView):
    model = CaseDetails
    template_name = "editevidence.html"
    fields = ('agent_id','case_id','case_name','evidence','status')
    success_url = '/update_evidence/'

def Defence(request):
    username = request.POST.get('name')
    password = request.POST.get('password')

    # adminlogin(username=username,password=password).save()
    # return render(request,"defence_login.html")
    qs = adminlogin.objects.filter(username=username, password=password)
    if qs:
        return render(request, "welcomedefence.html")
    else:
        return render(request, "defence_login.html", {'message': 'Invalid User'})

def Create_Case(request):

    case_details= request.POST.get("case details")
    case_name = request.POST.get("case name")
    doc = request.POST.get("date")
    evidence  = request.POST.get("evidence")
    CaseCreation(case_name=case_name,case_details=case_details,doc=doc,evidence=evidence).save()
    return render(request,"casecreation.html",{'message':'case created'})

def casereport(request):
    qs = CaseDetails.objects.all()
    return render(request,"report.html",{'data':qs})

def adminreport(request):
    qs = CaseDetails.objects.all()
    return render(request, "report_admin.html", {'data': qs})

def defencereport(request):
    qs = CaseDetails.objects.all()
    return render(request, "report_defence.html", {'data': qs})

def AllStories(request):
    qs = success_stories.objects.all()
    return render(request,"allstories.html",{'data':qs})