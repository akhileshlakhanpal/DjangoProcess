# import pdb
# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import *
# from Auth.models import *
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login
# from django.shortcuts import render,redirect
# from django.contrib import messages
# import format
#
# def home(request):
#     return redirect('secondaryres')
# def signout(request):
#     return redirect('index')
# def dashboard(request):
#     return render(request,'pages/dashboard.html')
# def secondaryres(request,id):
#     project_data=project_info.objects.filter(id=id).values()
#     filename=project_data[0]['file']
#     data_list= []
#     data_pass={}
#     details=format.format_file(filename)
#     projectname = details['pname']
#     projectcode = details['pcode'].split('.')[0]
#     loop_length=len(details['ques_label'])
#     for i in range(loop_length):
#         data={'ques_label':details['ques_label'][i],'ques_text':details['que_text'][i],'ques_type':details['que_type'][i],'option_list':details['option_list'][i]}
#         data_list.append(data)
#     data_pass['length']=data_list
#     data_pass['pname']=projectname
#     data_pass['pcode']=projectcode
#     if request.method == 'POST':
#         for i in range(loop_length):
#             quantative_ans = []
#             qualitative_ans=[]
#             for j in range(len(details['option_list'][i])):
#                 Insight1=request.POST.get(f"{details['ques_label'][i]}_{details['option_list'][i][j]}_1")
#                 Insight2=request.POST.get(f"{details['ques_label'][i]}_{details['option_list'][i][j]}_2")
#                 quantative_ans.append(Insight1)
#                 qualitative_ans.append(Insight2)
#             en = secondaryT_details(projectcode=projectcode,question_label=details['ques_label'][i], quantative_ans=quantative_ans, qualitative_ans=qualitative_ans)
#             en.save()
#         return redirect('/dashboard')
#
#     else:
#         return render(request, 'pages/SecondaryT_Entry.html',data_pass)
#
#
#
#
