# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import *
# import mimetypes
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login
# from django.shortcuts import render,redirect
# from django.contrib import messages
# import format
# import os
# import data_gen
#
# def home(request):
#     return redirect('datateam')
# def signout(request):
#     return redirect('index')
#
# def datateam(request):
#     details = format.format_file()
#
#
#     projectname = details['pname']
#     projectcode = details['pcode'].split('.')[0]
#     data_list = []
#     data_pass = {}
#     loop_length = len(details['ques_label'])
#     for i in range(loop_length):
#         option_list_no = []
#         for k, l in enumerate(details['option_list'][i]):
#             option_list_no.append(f"[ {details['option_no'][i][k]} ] {l}")
#         data={'ques_label':details['ques_label'][i],'ques_text':details['que_text'][i],'ques_type':details['que_type'][i],'option_list':option_list_no}
#         data_list.append(data)
#     data_pass['length']=data_list
#     data_pass['pname']=projectname
#     data_pass['pcode']=projectcode
#     if request.method == 'POST':
#         for i in range(loop_length):
#             option_ans = []
#             for j in range(len(details['option_list'][i])):
#                 percentage = request.POST.get(f"{details['ques_label'][i]}_{j+1}")
#
#                 option_ans.append(f"{details['option_no'][i][j]} = {percentage}")
#             en = dataT_details(projectcode=projectcode, question_label=details['ques_label'][i],
#                                     option_ans=option_ans)
#             en.save()
#         return redirect('datagen')
#
#     else:
#         return render(request, 'pages/DataT_Entry.html', data_pass)
#
# def datagen(request):
#     projectcode=os.listdir(fr"{os.getcwd()}\media\final")[-1].split('_')[-1].split('.')[0]
#     data_list = dataT_details.objects.filter(projectcode=projectcode).values()
#     label_={}
#     for data in data_list:
#         label_[data['question_label']]=data['option_ans']
#     if request.method == 'POST':
#         number=request.POST.get('number')
#         file_name=data_gen.generator(label_,int(number),projectcode)
#         en = data_result(projectcode=projectcode, file=fr'data\{file_name}')
#         en.save()
#         return redirect('export')
#
#     return render(request,'pages/Data_Gen.html')
# def generatedata(request):
#     return messages.success(request,"Generate Successfully")
#
#
#
# def export(request):
#     projectcode = os.listdir(fr"{os.getcwd()}\media\final")[-1].split('_')[-1].split('.')[0]
#     data_list = data_result.objects.filter(projectcode=projectcode).values()
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     print(BASE_DIR)
#     filename = data_list[0]['file']
#     filepath = BASE_DIR + '/media/' + filename
#     print(filepath)
#     with open(filepath, 'rb') as f:
#         response = HttpResponse(f.read(), content_type='application/vnd.ms-excel')
#         response['Content-Disposition'] = 'attachment; filename=' + filename
#         response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-16'
#         return response