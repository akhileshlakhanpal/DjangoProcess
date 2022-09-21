from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from Web_app1 import settings
from .models import *
from Sec_Res.models import *
from Data_Team.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import fileform
import filedetails
import format
import os
import data_gen
def home(request):
    return render(request,'pages/index.html')
def projectdata(request):
    if request.method=='POST':
        projectname=request.POST.get('ProjectName')
        projectid=request.POST.get('Projectid')
        domain=request.POST.get('Domain')
        file=request.POST.get('myfile')
        en=project_info(projectname=projectname,project_id=projectid,domain=domain,file=file)
        en.save()
    return redirect('/file_app')
def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            try:
                remember = request.POST['remember-me']
                if remember:
                    settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
            except:
                is_private = False
            return redirect('/dashboard')
        else:
            messages.error(request,"Username or Password Wrong")
            return render(request,'pages/signin.html')
            pass
    else:
        return render(request,'pages/signin.html')
def signout(request):
    return render(request,'pages/index.html')
def dashboard(request):
    data_details=[]
    data_list = project_info.objects.all().values()
    data_list1=project_details.objects.all().values()
    data_pass={}
    for i in range(len(data_list)):
        data={'id':data_list[i]['id'],'project_id':data_list[i]['project_id'],'project_name':data_list[i]['projectname'],'file':data_list[i]['file']}
        data_details.append(data)
    data_pass['length']=data_details
    data_pass['ongoing']=len(data_list)
    data_pass['total']=len(data_list)
    return render(request,'pages/dashboard.html',data_pass)

def createproject(request):
    if request.method == 'POST':
        form = fileform(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/projectdetails')
    else:
        form = fileform()
    return render(request, 'pages/createproject.html', {'form': form})

def projectdetails(request):
    data_list=project_info.objects.all().values()
    pid_list=[]
    for data in data_list:
        pid_list.append(data['project_id']+' / '+data['projectname'])
    data={'pid':pid_list}
    try:
        if request.method == 'POST':
            projectcode=request.POST.get('ProjectCode').split('/')[-1].strip()
            methodplogy = request.POST.get('methodplogy')
            geoscope = request.POST.get('geoscope')
            industry = request.POST.get('industry')
            subjectsep = request.POST.get('subjectsep')
            pobjective = request.POST.get('pobjective')
            raudience = request.POST.get('raudience')
            sme = request.POST.get('sme')
            analyst = request.POST.get('analyst')
            dataanalyst = request.POST.get('dataanalyst')
            en = project_details(projectcode=projectcode,methodplogy=methodplogy, geoscope=geoscope, industry=industry, subjectsep=subjectsep, pobjective=pobjective,
                              raudience=raudience, sme=sme, analyst=analyst, dataanalyst=dataanalyst)
            en.save()
            return redirect('/dashboard')
    except:
        pass
    return render(request, 'pages/projectdetails.html',data)

def success(request):
    return HttpResponse("Succees")
def secondaryres(request,id):
    project_data=project_info.objects.filter(id=id).values()
    filename=project_data[0]['file']
    projectcode = project_data[0]['project_id']
    projectname = project_data[0]['projectname']
    filedetails.details(filename, projectcode, projectname)
    data_list= []
    data_pass={}
    details=format.format_file()
    projectname = details['pname']
    projectcode = details['pcode'].split('.')[0]
    loop_length=len(details['ques_label'])
    for i in range(loop_length):
        data={'id':[i],'ques_label':details['ques_label'][i],'ques_text':details['que_text'][i],'ques_type':details['que_type'][i],'option_list':details['option_list'][i],'option_dep':details['option_dep'][i]}
        data_list.append(data)
    data_pass['length']=data_list
    data_pass['pname']=projectname
    data_pass['pcode']=projectcode
    if request.method == 'POST':
        for i in range(loop_length):
            quantative_ans = []
            qualitative_ans=[]
            text_input = request.POST.get("addcomment")
            for j in range(len(details['option_list'][i])):
                if details['que_type'][i].lower()=='single select grid' or details['que_type'][i].lower()=='multi select grid':
                    Insight1_list=[]
                    Insight2_list=[]
                    for k in range(len(details['option_dep'][i])):
                        Insight1 = request.POST.get(f"{details['ques_label'][i]}_{details['option_list'][i][j]}_{k+1}_1")
                        Insight2 = request.POST.get(f"{details['ques_label'][i]}_{details['option_list'][i][j]}_{k+1}_2")
                        Insight1_list.append(Insight1)
                        Insight2_list.append(Insight2)
                    quantative_ans.append(Insight1_list)
                    qualitative_ans.append(Insight2_list)
                elif details['que_type'][i].lower() == 'number grid':
                    numberrange=request.POST.get(
                        f"{details['ques_label'][i]}_{details['option_list'][i][j]}_1")
                    Insight1 = request.POST.get(
                        f"{details['ques_label'][i]}_{details['option_list'][i][j]}_1_1")
                    Insight2 = request.POST.get(
                        f"{details['ques_label'][i]}_{details['option_list'][i][j]}_1_2")

                    quantative_ans.append(f"{numberrange}={Insight1}")
                    qualitative_ans.append(f"{numberrange}={Insight2}")
                else:
                    Insight1=request.POST.get(f"{details['ques_label'][i]}_{details['option_list'][i][j]}_1")
                    Insight2=request.POST.get(f"{details['ques_label'][i]}_{details['option_list'][i][j]}_2")
                    quantative_ans.append(Insight1)
                    qualitative_ans.append(Insight2)
            en = secondaryT_details(projectcode=projectcode,question_label=details['ques_label'][i], quantative_ans=quantative_ans, qualitative_ans=qualitative_ans,text_input=text_input)
            en.save()
        return redirect('/dashboard')

    else:
        return render(request, 'pages/SecondaryT_Entry.html',data_pass)
def datateam(request,id):
    project_data = project_info.objects.filter(id=id).values()
    filename = project_data[0]['file']
    projectcode = project_data[0]['project_id']
    projectname = project_data[0]['projectname']
    filedetails.details(filename,projectcode,projectname)
    details = format.format_file()
    projectname = details['pname']
    projectcode = details['pcode'].split('.')[0]
    data_list = []
    data_pass = {}
    loop_length = len(details['ques_label'])
    ques_ask=[]
    dependency=[]
    for i in range(loop_length):
        if len(details['dependency'][i])>1:
            dependent=details['dependency'][i].split('{')[-1].strip().strip('}').split(',')
            que_dep=''
            dep_option=''
            for dep in dependent:
                if dep.split(':')[0].strip()!=que_dep.strip().strip(',').strip():
                    que_dep += dep.split(':')[0]+', '
                dep_option += dep.split(':')[-1]+', '
            dependency.append(f"{que_dep.strip().strip(',')} : Option - {dep_option.strip().strip(',')}")
        else:
            dependency.append('')
    for i in range(loop_length):
        ques_dump=[]
        for j in range(i):
            ques_dump.append(details['ques_label'][j])
        ques_ask.append(ques_dump)
    for i in range(loop_length):
        option_list_no = []
        option_dep_list_no=[]
        for k, l in enumerate(details['option_list'][i]):
            option_list_no.append(f"[ {details['option_no'][i][k]} ] {l}")
        for k, l in enumerate(details['option_dep'][i]):
            option_dep_list_no.append(f"[ {details['option_dep_no'][i][k]} ] {l}")
        data={'id':[i],'ques_label':details['ques_label'][i],'ques_text':details['que_text'][i],'ques_type':details['que_type'][i],'option_list':option_list_no,'length':loop_length,'option_dep':option_dep_list_no,'ques_ask':ques_ask[i],'dependency':dependency[i]}
        data_list.append(data)


    data_pass['length']=data_list
    data_pass['pname']=projectname
    data_pass['pcode']=projectcode
    if request.method == 'POST':
        for i in range(loop_length):
            option_ans = []
            text_input = request.POST.get("addcomment")
            for j in range(len(details['option_list'][i])):
                if details['que_type'][i].lower()=='single select grid' or details['que_type'][i].lower()=='multi select grid':
                    percentage_list=[]
                    for k in range(len(details['option_dep'][i])):
                        percentage=request.POST.get(f"{details['ques_label'][i]}_[ {details['option_no'][i][j]} ] {details['option_list'][i][j]}_{k + 1}")
                        percentage_list.append(f"{details['option_dep_no'][i][k]} = {percentage}")
                    option_ans.append(f"{details['option_no'][i][j]} = {percentage_list}")
                elif details['que_type'][i].lower()=='number grid':
                    range_list=[]
                    numberrange=request.POST.get(f"{details['ques_label'][i]}_[ {details['option_no'][i][j]} ] {details['option_list'][i][j]}_1")
                    percentage=request.POST.get(f"{details['ques_label'][i]}_[ {details['option_no'][i][j]} ] {details['option_list'][i][j]}_2")
                    range_list.append(f"{numberrange} = {percentage}")
                    option_ans.append(f"{details['option_no'][i][j]} = {range_list}")
                elif details['que_type'][i].lower()=='number':
                    percentage = request.POST.get(f"{details['ques_label'][i]}_{j + 1}")
                    option_ans.append(f"{details['option_list'][i][j]} = {percentage}")
                else:
                    percentage = request.POST.get(f"{details['ques_label'][i]}_{j + 1}")
                    option_ans.append(f"{details['option_no'][i][j]} = {percentage}")
            en = dataT_details(projectcode=projectcode, question_label=str(details['ques_label'][i]+'||'+details['que_type'][i]),
                                    option_ans=option_ans,text_input=text_input)
            en.save()
        return redirect('datagen')


    else:
        return render(request, 'pages/DataT_Entry.html', data_pass)
# def get_options(request):
#     details = format.format_file()
#     question=request.GET.get('dependency')
#     print(question,'---------------------------')
#     loop_length = len(details['ques_label'])
#     option_list=[]
#     for i,j in enumerate(details['ques_label']):
#         opt={}
#         opt[j]=details['option_list'][i]
#         option_list.append(opt)
#     data={'ques_options':option_list}
#     return render(request,'pages/dropdown_opt.html',data)


def datagen(request):
    projectcode=os.listdir(fr"{os.getcwd()}\media\final")[-1].split('_')[-1].split('.')[0]
    data_list = dataT_details.objects.filter(projectcode=projectcode).values()
    label_={}
    details=format.format_file()
    dependency_details=details['dependency_dict']
    for data in data_list:
        label_[data['question_label']]=data['option_ans']
    if request.method == 'POST':
        number=request.POST.get('number')
        file_name=data_gen.generator(label_,int(number),projectcode,dependency_details)
        en = data_result(projectcode=projectcode, file=fr'data\{file_name}')
        en.save()
        return redirect('export')

    return render(request,'pages/Data_Gen.html')
def export(request):
    projectcode = os.listdir(fr"{os.getcwd()}\media\final")[-1].split('_')[-1].split('.')[0]
    data_list = data_result.objects.filter(projectcode=projectcode).values()
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = data_list[0]['file']
    filepath = BASE_DIR + '/media/' + filename
    with open(filepath, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=' + filename
        response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-16'
        return response