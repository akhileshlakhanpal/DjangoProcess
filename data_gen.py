import pdb
import shutil
import pandas as pd
import random
import string
import os

def generator(x,n,pcode,dependency):
    print(x)
    print(dependency)
    # Length of uuid
    S = 16

    Gen_Data = {}
    label_1={}
    for i in range(0,n):
        Gen_Data[i] = {}

        ##############################record and uuid#########################
        Gen_Data[i]['record'] = i + 1
        ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k=S))
        Gen_Data[i]['uuid'] = ran

        #############################First Question################################

        for key1,value in x.items():
            key=key1.split('||')[0]
            que_typ=key1.split('||')[-1]
            if que_typ.lower()=='single select':
                value = value.strip('[').strip(']').replace("'", "").split(',')
                list_dump = []
                for j in value:
                    r=int(j.split('=')[-1].strip())
                    k=int(j.split('=')[0].strip())
                    for l in range(r):
                        list_dump.append(k)
                label_1[key]=list_dump

                # print(label_[label])
                if dependency[key]=='':
                    Gen_Data[i][key] = random.choice(label_1[key])
                else:
                    dependent = dependency[key].split('{')[-1].strip().strip('}').split(',')
                    que_dep = ''
                    dep_option = ''
                    for dep in dependent:
                        que_dep += dep.split(':')[0] + ', '
                        dep_option += dep.split(':')[-1] + ', '
                    que_dep=que_dep.strip().strip(',').strip()
                    dep_option=dep_option.strip().strip(',').strip()
                    for opt,que_d in enumerate(que_dep.split(',')):
                        try:
                            if int(Gen_Data[i][que_d.strip()])==int(dep_option.split(',')[opt].strip()):
                                Gen_Data[i][key] = random.choice(label_1[key])
                                break
                        except:
                            pass
                    try:
                        if Gen_Data[i][key]:
                            pass
                    except:
                        Gen_Data[i][key] = ''
            elif que_typ.lower()=='multi select':
                value = value.strip('[').strip(']').replace("'", "").split(',')
                list_dump = []
                for j in value:
                    dum_key=''
                    r=int(j.split('=')[-1].strip())
                    k=int(j.split('=')[0].strip())
                    r1=100-r
                    for l in range(r):
                        list_dump.append(1)
                    for l in range(r1):
                        list_dump.append(0)
                    dum_key=key+'r'+str(k)
                    label_1[dum_key]=list_dump

                    # print(label_[label])
                    # Gen_Data[i][dum_key] = random.choice(label_1[dum_key])
                    if dependency[key] == '':
                        Gen_Data[i][dum_key] = random.choice(label_1[dum_key])
                    else:
                        dependent = dependency[key].split('{')[-1].strip().strip('}').split(',')
                        que_dep = ''
                        dep_option = ''
                        for dep in dependent:
                            que_dep += dep.split(':')[0] + ', '
                            dep_option += dep.split(':')[-1] + ', '
                        que_dep = que_dep.strip().strip(',').strip()
                        dep_option = dep_option.strip().strip(',').strip()
                        for opt, que_d in enumerate(que_dep.split(',')):
                            try:
                                if int(Gen_Data[i][que_d.strip()]) == int(dep_option.split(',')[opt].strip()):
                                    Gen_Data[i][dum_key] = random.choice(label_1[dum_key])
                                    break
                            except:
                                pass
                        try:
                            if Gen_Data[i][dum_key]:
                                pass
                        except:
                            Gen_Data[i][dum_key] = ''
            elif que_typ.lower()=='multi select grid':
                value = value.strip('[').strip(']').split('",')
                list_dump = []
                for j in value:
                    dum_key = ''
                    k = int(j.split('=')[0].replace('"', '').strip())
                    value1 = j.split('[')[-1].strip(']').split(',')
                    for j1 in value1:
                        r = int(j1.split('=')[-1].replace("'", "").replace('"', "").replace(']', '').strip())
                        k1 = int(j1.split('=')[0].replace("'", "").replace('"', "").strip())
                        r1=100-r
                        for l in range(r):
                            list_dump.append(1)
                        for l in range(r1):
                            list_dump.append(0)
                        dum_key = key + 'r' + str(k)+'c'+str(k1)
                        label_1[dum_key] = list_dump
                        # Gen_Data[i][dum_key] = random.choice(label_1[dum_key])
                        if dependency[key] == '':
                            Gen_Data[i][dum_key] = random.choice(label_1[dum_key])
                        else:
                            dependent = dependency[key].split('{')[-1].strip().strip('}').split(',')
                            que_dep = ''
                            dep_option = ''
                            for dep in dependent:
                                que_dep += dep.split(':')[0] + ', '
                                dep_option += dep.split(':')[-1] + ', '
                            que_dep = que_dep.strip().strip(',').strip()
                            dep_option = dep_option.strip().strip(',').strip()
                            for opt, que_d in enumerate(que_dep.split(',')):
                                try:
                                    if int(Gen_Data[i][que_d.strip()]) == int(dep_option.split(',')[opt].strip()):
                                        Gen_Data[i][dum_key] = random.choice(label_1[dum_key])
                                        break
                                except:
                                    pass
                            try:
                                if Gen_Data[i][dum_key]:
                                    pass
                            except:
                                Gen_Data[i][dum_key] = ''


            elif que_typ.lower()=='single select grid':
                value = value.strip('[').strip(']').split('",')
                list_dump=[]
                for j in value:
                    dum_key=''
                    k=int(j.split('=')[0].replace('"','').strip())
                    value1=j.split('[')[-1].strip(']').split(',')
                    dum_key = key + 'r' + str(k)
                    for j1 in value1:
                        r=int(j1.split('=')[-1].replace("'","").replace('"',"").replace(']','').strip())
                        k1=int(j1.split('=')[0].replace("'","").replace('"',"").strip())
                        for l in range(r):
                            list_dump.append(k1)
                    label_1[dum_key]=list_dump
                    # Gen_Data[i][dum_key] = random.choice(label_1[dum_key])
                    if dependency[key] == '':
                        Gen_Data[i][dum_key] = random.choice(label_1[dum_key])
                    else:
                        dependent = dependency[key].split('{')[-1].strip().strip('}').split(',')
                        que_dep = ''
                        dep_option = ''
                        for dep in dependent:
                            que_dep += dep.split(':')[0] + ', '
                            dep_option += dep.split(':')[-1] + ', '
                        que_dep = que_dep.strip().strip(',').strip()
                        dep_option = dep_option.strip().strip(',').strip()
                        for opt, que_d in enumerate(que_dep.split(',')):
                            try:
                                if int(Gen_Data[i][que_d.strip()]) == int(dep_option.split(',')[opt].strip()):
                                    Gen_Data[i][dum_key] = random.choice(label_1[dum_key])
                                    break
                            except:
                                pass
                        try:
                            if Gen_Data[i][dum_key]:
                                pass
                        except:
                            Gen_Data[i][dum_key] = ''
            elif que_typ.lower()=='number grid':
                value = value.strip('[').strip(']').split('",')
                list_dump=[]
                for j in value:
                    dum_key=''
                    k=int(j.split('=')[0].replace('"','').strip())
                    value1=j.split('[')[-1].strip(']').split(',')
                    dum_key = key + 'r' + str(k)
                    for j1 in value1:
                        r=int(j1.split('=')[-1].replace("'","").replace('"',"").replace(']','').strip())
                        range1=int(j1.split('=')[0].replace("'","").replace('"',"").strip().split('-')[0].strip())
                        range2=int(j1.split('=')[0].replace("'","").replace('"',"").strip().split('-')[-1].strip())
                        for l in range(r):
                            list_dump.append(random.randint(range1, range2))
                    label_1[dum_key]=list_dump
                    # Gen_Data[i][dum_key] = random.choice(label_1[dum_key])
                    if dependency[key] == '':
                        Gen_Data[i][dum_key] = random.choice(label_1[dum_key])
                    else:
                        dependent = dependency[key].split('{')[-1].strip().strip('}').split(',')
                        que_dep = ''
                        dep_option = ''
                        for dep in dependent:
                            que_dep += dep.split(':')[0] + ', '
                            dep_option += dep.split(':')[-1] + ', '
                        que_dep = que_dep.strip().strip(',').strip()
                        dep_option = dep_option.strip().strip(',').strip()
                        for opt, que_d in enumerate(que_dep.split(',')):
                            try:
                                if int(Gen_Data[i][que_d.strip()])==int(dep_option.split(',')[opt].strip()):
                                    Gen_Data[i][dum_key] = random.choice(label_1[dum_key])
                                    break
                            except:
                                pass
                        try:
                            if Gen_Data[i][dum_key]:
                                pass
                        except:
                            Gen_Data[i][dum_key] = ''
            elif que_typ.lower()=='number':
                value = value.strip('[').strip(']').replace("'", "").split(',')
                list_dump=[]
                for j in value:
                    r=int(j.split('=')[-1].replace("'","").replace('"',"").replace(']','').strip())
                    range1=int(j.split('=')[0].replace("'","").replace('"',"").strip().split('-')[0].strip())
                    range2=int(j.split('=')[0].replace("'","").replace('"',"").strip().split('-')[-1].strip())
                    for l in range(r):
                        list_dump.append(random.randint(range1, range2))
                label_1[key]=list_dump
                # Gen_Data[i][key] = random.choice(label_1[key])
                if dependency[key] == '':
                    Gen_Data[i][key] = random.choice(label_1[key])
                else:
                    dependent = dependency[key].split('{')[-1].strip().strip('}').split(',')
                    que_dep = ''
                    dep_option = ''
                    for dep in dependent:
                        que_dep += dep.split(':')[0] + ', '
                        dep_option += dep.split(':')[-1] + ', '
                    que_dep = que_dep.strip().strip(',').strip()
                    dep_option = dep_option.strip().strip(',').strip()
                    for opt, que_d in enumerate(que_dep.split(',')):
                        try:
                            if int(Gen_Data[i][que_d.strip()]) == int(dep_option.split(',')[opt].strip()):
                                Gen_Data[i][key] = random.choice(label_1[key])
                                break
                        except:
                            pass
                    try:
                        if Gen_Data[i][key]:
                            pass
                    except:
                        Gen_Data[i][key] = ''
    # print(Gen_Data)
    df = pd.DataFrame(Gen_Data).T
    df.to_excel(f'{os.getcwd()}\\media\\data\\Data_{pcode}.xlsx', index=False)
    return f'Data_{pcode}.xlsx'