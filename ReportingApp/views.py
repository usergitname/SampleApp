from django.shortcuts import render
from .models import QALabSupport
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
def dashboard(request):
    #return HttpResponse('hi')
    val=request.POST
    print(val.getlist('your_name'))
    print(val.values())
    report = QALabSupport.objects.all()    # )
    #return HttpResponseRedirect ("http://127.0.0.1:8000/admin/ReportingApp")
    return render(request,'index.html',{"report":report})
    #return HttpResponseRedirect("index.html")for i in report:
    #     #print(i.Name)
    #     print(i.Priority
    #return JsonResponse({"success": True,"value1":120,"value2":130}, status=200)
# def calc(request):
#  return JsonResponse({"success": True,"value1":120,"value2":130}, status=200)

def home(request):
    report = QALabSupport.objects.all()
    count=report.count()
    val=request.GET
    print(val.values())
    return render(request,"home.html",{"report":report})

def addnew(request):
    val=request.POST
    Name = val.get("Name", "0")
    Priority = val.get("Priority", "0")
    State = val.get("State", "0")
    Attachements = val.get("Attachements", "0")
    b = QALabSupport(Name=Name, Priority=Priority, State=State, Attachements=Attachements)
    b.save()
    url="http://127.0.0.1:8000/admin/home/"
    return render(request,"add.html",{"url":url})

# def upload(request):
#     myfile = request.FILES['myfile']
#     fs = FileSystemStorage()
#     filename = fs.save(myfile.name, myfile)
#     uploaded_file_url = fs.url(filename)
#     print(uploaded_file_url)
#     return HttpResponseRedirect("http://127.0.0.1:8000/admin/addnew")

def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload.html')