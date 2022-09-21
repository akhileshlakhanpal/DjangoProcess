import os
import re
import docx2txt
from pymongo import MongoClient
import datetime
def format_file():
    details={}
    que_no=[]
    que_text=[]
    option_no=[]
    que_type=[]
    option_list=[]
    option_dep=[]
    option_dep_no=[]
    dependency_list = []
    dependency_dict={}
    # Passing docx file to process function
    file=os.listdir(fr"{os.getcwd()}\media\final")[-1]
    text = docx2txt.process(fr"{os.getcwd()}\media\final\\{file}")
    question_list=text.split('\n\n\n')
    for que in question_list:
        dep = ''
        que_no.append(que.split(']')[0].replace('[','').replace('\n',''))
        que_text.append(que.split(']')[1].split('[')[0].replace('\n',''))
        que_type.append(que.split(']')[1].split('[')[1].replace('\n','').upper())
        opt_list = []
        opt_no_list = []
        opt_dep = []
        opt_dep_no = []
        if que.split(']')[1].split('[')[1].replace('\n','').lower()=='single select grid' or que.split(']')[1].split('[')[1].replace('\n','').lower()=='multi select grid':
            if que.split('\n\n')[1].startswith('/['):
                for dep in que.split('\n\n')[1].replace('/[','').replace(']/','').split(','):
                    opt_dep.append(dep.split(')')[1])
                    opt_dep_no.append(dep.split(')')[0])
            for option in que.split('\n\n')[2:]:
                dep=''
                try:
                    opt_list.append(option.split(')')[1].split('/[')[0])
                    opt_no_list.append(option.split(')')[0])
                except:
                    if option.split('–')[0].strip() == 'DEPENDENCY':
                        dep = option.split('–')[-1].strip()

        else:
            for option in que.split('\n\n')[1:]:

                try:
                    opt_list.append(option.split(')')[1])
                    opt_no_list.append(option.split(')')[0])
                except:
                    if option.split('–')[0].strip()=='DEPENDENCY':
                        dep=option.split('–')[-1].strip()
        dependency_list.append(dep)
        dependency_dict[que.split(']')[0].replace('[','').replace('\n','')]=dep
        option_list.append(opt_list)
        option_no.append(opt_no_list)
        option_dep.append(opt_dep)
        option_dep_no.append(opt_dep_no)
    details['ques_label']=que_no
    details['que_text']=que_text
    details['que_type']=que_type
    details['option_list']=option_list
    details['option_no']=option_no
    details['pname']=file.split('_')[0]
    details['pcode']=file.split('_')[-1]
    details['option_dep']=option_dep
    details['option_dep_no']=option_dep_no
    details['dependency']=dependency_list
    details['dependency_dict']=dependency_dict
    return details
