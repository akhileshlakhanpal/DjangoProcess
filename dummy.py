# import requests
# import json
#
# url = "https://resdex.naukri.com/cloudgateway-resdex/recruiter-js-profile-listing-services/v0/search/results/advSearch"
#
# payload = json.dumps({
#   "advSearchParams": {
#     "ezKeywordsAny": [
#       {
#         "key": None,
#         "value": "\"Data Scientist\"",
#         "type": None
#       }
#     ],
#     "srchType": "adv",
#     "ezKeywordsAll": [],
#     "ezKeywordsExclude": [],
#     "srchKeywordsIn": "ER",
#     "boolKeywords": "",
#     "booleanSearch": False,
#     "currentLocations": [],
#     "stateLocations": [],
#     "otherLocations": "",
#     "prefLocations": [],
#     "statePrefLocations": [],
#     "prefLocationExactMatch": False,
#     "prefLocationCriteria": True,
#     "prefLocationChecked": True,
#     "prefLocationDd": 1,
#     "currency": "rs",
#     "searchOnZeroCtc": False,
#     "noticePeriod": [
#       0
#     ],
#     "gender": "n",
#     "srchOnlyPhysicallyDisabled": False,
#     "category": [],
#     "allOrNewCV": "ALL",
#     "srchOnlyMobileVerified": False,
#     "srchOnlyEmailVerified": False,
#     "srchOnlyCvUploaded": False,
#     "industryIds": [],
#     "excludeIndustryIds": [],
#     "employeesInclude": [],
#     "employeesIncludeState": "C",
#     "employeesIncludeStrType": "ezkw",
#     "employeesExclude": [],
#     "employeesExcludeState": "C",
#     "employeesExcludeStrType": "ezkw",
#     "designation": [],
#     "designationState": "C",
#     "designationStrType": "ezkw",
#     "fareaRoleIdsEntity": [],
#     "selectedUgTab": -1,
#     "ugEducationType": [],
#     "selectedPgTab": -1,
#     "pgEducationType": [],
#     "selectedPpgTab": -1,
#     "ppgEducationType": [],
#     "ugPgCombinationCriteria": True,
#     "pgPpgCombinationCriteria": True,
#     "ugPpgCombinationCriteria": True,
#     "ugCourseSpecIds": [],
#     "pgCourseSpecIds": [],
#     "ppgCourseSpecIds": [],
#     "activeIn": 63,
#     "resPerPage": 40,
#     "sortType": "RELEVANCE",
#     "swrKeywords": ""
#   },
#   "miscellaneousInfo": {
#     "companyId": 5443710,
#     "rdxUserId": "5577796",
#     "rdxUserName": "Surendra.singh@jaspercolin.com",
#     "flowName": "search",
#     "fetchClusters": False,
#     "fetchResumeTuples": True
#   }
# })
# headers = {
#   'authority': 'resdex.naukri.com',
#   'accept': 'application/json',
#   'accept-language': 'en-US,en;q=0.9',
#   'appid': '112',
#   'content-type': 'application/json',
#   'cookie': '_did=a7c0214864; _odur=981cf70813; _t_ds=9b0648b1663608103-59b0648b-09b0648b; bm_sz=05E2F7EFC38A45E158DCAE7079E67321~YAAQFG0/F1voZz2DAQAA2yLFVhHpuVHYWOFSSQeG3zpqdclM1hZlikDoJyXCpjqepv2dQHZi+1iqSokYQPyrvrA/cuR+K68zqBPjEocgnr1XLdDfdWeIE3FbIyxSOZBg/lGNgDVau9dk+UswmHjIOM2ckKcW9YJCPhS9LYvKpjrhcDBewrZGolv3uFuAcao+hmaxn2EDTSoJjGAGPII0IzFSPGGWppfJQF93+PQl1J9Ubi6M+9EnrVdZzjB53lA3IehOdgu4QssL4fKOWWST9My/ssCYpFwvflzgO66X2iuYKfg=~4474163~3687478; page_visit=1; dfp=f5ff12eb630497ce2b0c927c15eedc80; _gcl_au=1.1.1101042809.1663608105; _ga=GA1.2.177059541.1663608105; _gid=GA1.2.62033853.1663608105; ak_bmsc=D126280FC24BD0D70C261BC7E9D94E97~000000000000000000000000000000~YAAQFG0/FyDpZz2DAQAAkifFVhGwhplgOi1ex/Vpb+L8aq0JEY5auanwd+RCbCsyDRO2+YiL6vr26LiLbxyfLsEQOc6MF1DYjlBraVOIdOndR9BHUzvnnFelceaTnpAtG2dUyAgCTho5KxbPh5PYw6kSQ3I/ztOlDmqtePsBrAdfRHkAieiWYOZe6HLvLgByAz0hgwbyiFgVkRZdTRnKFPRhubSS1j9SOy4tXBkECukm55c89MCOqNoKQyHstli4y2rI7dL7/AyiSAAze+URunJSl+WHfC4VB/ZHz7wX3eqlbfmR8sFND3TcNHp3cwavCjex6W8UxTZzeMOAzai6FBsuRyMPhd2UtUfKtsApMFbMhapbdkcjYLj1zwfTeY9ZjY2sUEpOpRoOpM7j2gpkFBLbJobdQGAz75GQ5dBPEdmltFiVT4hIK3P40wBY8y/ib39+m0aj3pTeY00VMi1QOHbOvWZ96fQjkymSqH6I0nRwFwGsUSAP1yR6glw=; _abck=D9805871E38C32F41F597AF94F452D48~0~YAAQFG0/FyXpZz2DAQAACCjFVgjXlT90hzwxgn/EvH+wE3aP/K8s6plkv3KIgo7q4XZeo1jfLMJFbAAM6QXDo+DXZkt2IwehTaEdMISPcnNnXoScIW2USbhosmuMmadbBr4y/FXy9Xzsd1walL1o9RbuSxcpf5eV7irT+rkwB+c6pbYOekqFZoyXlbNkrXzSo1Xor3bWe0V0cD4Gpa/ZFGAvELpKRQJjpC+pVmBpysrJOGTgVgD3ZPQmtYe7/gUq1nWWE68UKugy8rq4a8kw5DDDFSiekx83HBlnxHL/JbUyKE1RJidnz7b0C9Z1ZQ4fX/4R5oeTEl5X6rlzOWlMboNe5q8OC9AvPFwnJ2bqrRBwMtmmAWJR/x1Hz7M+2EUbo7twsz9kbvdX545PXTN/74cUoba2~-1~-1~-1; LPVID=c2NmNiYTJiZWRhZDQzYWJj; LPSID-77159344=eTc_711lSIKCBclH-ZULKg; kycEligibleCookie5443710=0; UNPC=5443710; UNCC=5577796; _uv5577796=isSet; test=naukri.com; showPhotoUploadPage5577796=isSet; __utma=266160400.177059541.1663608105.1663608215.1663608215.1; __utmc=266160400; __utmz=266160400.1663608215.1.1.utmcsr=naukri.com|utmccn=(referral)|utmcmd=referral|utmcct=/; bs_rnd=Ldbf1dcL; logout_check=1; 3ea1b293423b8be95df0e9447e5b2a43=v0%7CX5XhJckBo1MQ7N%2FBhIOeeIW646CxV0bIWZ47MLz9fSBieWryE7185zqamHtg3TZ8B8eoLAKU8vIoWn5BOaZ1y0FuIPCNEVPvhntYnrjnX%2FgBHdzIkWEoxCeI6u3251Q4%2BDG42JhhIgUz4WFT9VGreLERqpkuTausJDMbfgkNX0o%3D; ACCESS=1663608354; UNID=XNFkrwswx6qbWRH0F0lUg2TlUHuw5zxoZCebsRdq; showDomainLB5577796=1; __utmt=1; __utmb=266160400.13.10.1663608215; bm_sv=381B0B9CEA67E35DEABDF6999101B08C~YAAQFG0/F2H6aT2DAQAA23XaVhFQt6qUyeA39oueJw7neJTXr86vZuaQ5YcTb9M2rCaiO2v9wxPFlg7WaL9XiJ6UJfufJKjWrdNHtl1VSWv4ZFgk2vq+Rz6IVSqkaqcX6mGhepbcxzF/fFZ+Mq5SrWLs61j9+gpKFZWs+qcFVW+jN7fYNeevkohkKfxt2L/fwQcnMVWBLAH5ksxKtS7RLvjqyesoqP4+dZIKJ5kx8k75bNG3956iPLV0XzYixamOuQ==~1; HitsFromTieup=29041; TieupFromTMS=655; UNID=XNFkrwswx6qbWRH0F0lUg2TlUHuw5zxoZCebsRdq; _abck=D9805871E38C32F41F597AF94F452D48~-1~YAAQFG0/Fykvaj2DAQAAYVTcVghC18OBTciifwbgw0CyhKEYgPIqb9UJo9iRUmEhwCHeumF/AQZFhXaRQbMhJCdWI37WtdrCjkcVozSWtVc2xxVXvyHqFl1R7uYXlBZtvtfpzqqXFhs5bLEPwy+yfFQD0cs+1gWZj+ckZp8EjUbL+8XcfGjDBEKH7wJf4A2LNNcWuW/10yFmu9HbdajLgBh1ZbqN7QCoXl5ZH4kqkZMoE36IdK/i5DSIQWUQ7kb+hpN4BZKBGpW64lfP9nxfjqmghp9vnoliMI16ZnzPlas5DfTkqD4sWkvMwSk655BIe2Il0a0dBgCVBOC7oonLX00AAu2I1pzYKAVxdbNKgAaV058WkmYKOuZu5LqSc2r/OZr+lr/2iq2HsHLhko9f0D9M1CI6~0~-1~-1; _t_ds=332b63871663609435-9332b6387-0332b6387; ak_bmsc=F29944F83C3D1DDE519818ED44B42F78~000000000000000000000000000000~YAAQnJxMF82E0AODAQAARHXZVhGHRrYh2zzoziYUS5j2vAA9YMBDiy2u4nroFpEWI7duJYZ5CACuBiAEFE1juf/uU2Frwf7pbhB8FrI7buDD51libZx+gHJwFDm5/tAf3+IpUD/OfOhJK2fmejobtRnRM6XlwOYPc7tffVe4B5bm91Ex719g7AtdWF6IFBTjDHqPbILIMH1RM4fD0wwQqslvhok+1BsLaipwYaO8ylExQZiO5V7LaEfMpWphvy5W3BC7VTvPSXW2VQ+9k3oOgAU/tM5+NK7Mlh2kWpubfQvDNFGd0mM9KSFwvRQo9y1rMwM0PgBzfA==; bm_sv=381B0B9CEA67E35DEABDF6999101B08C~YAAQFG0/Fyovaj2DAQAAYVTcVhEi4g5XI2/vR3JX6sU9G1tdGKwnz9aWWxujF5+iJOsixxvsI8OAddFgb12g+s3gjxLwHg9M1Zx6jtozv/FbNV7G/z4w3IEifP9RozqLR62X5AxfU6MLGSyG89/GzrbMvQLy1bIv322Y9dvhO5ldrX0Bc97+k9xI13+1NYz/7oKWX9pcACRh3u6J0+glYc6uEt99vvGJEmJtR74dBBkm6rbGyV7FzcAvJnrNUqNn5w==~1; bm_sz=C7EAAA9B3B0C903A60E5F06573DCE557~YAAQnJxMF86E0AODAQAARHXZVhHnENj11g/1wZ6bSQpfKj2PZ8E94h7ag3DYLJrhN88mS3LSV9cGVTYt2f42XsogAC5FlL09fNsVxg1nALkm83qdEd6ClZpxXpFCen4f+MtDDh/nOwdAvmFpk0ZHden1X2gVeKvIJlz4ejj/Wnl9m3Ky0lGGusD0OKiqKy6OUjzUmUjW8/JoThjfdF5+ep8RAMtk3aoUihsiW5fTMYkmGjqcp6tIvh8AaMCAolFyTavBZW0nvmSRH+l9GNgj7vwGN9zucXbpo2xeGq/zbgAcNBw=~3487032~3425350; test=naukri.com; wExp=N',
#   'origin': 'https://resdex.naukri.com',
#   'referer': 'https://resdex.naukri.com/v3',
#   'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
#   'sec-ch-ua-mobile': '?0',
#   'sec-ch-ua-platform': '"Windows"',
#   'sec-fetch-dest': 'empty',
#   'sec-fetch-mode': 'cors',
#   'sec-fetch-site': 'same-origin',
#   'systemid': 'naukriIndia',
#   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
#   'x-transaction-id': 'fedebcce03fbae34f9b2e546a5a36555a50003b'
# }
# response = requests.request("POST", url, headers=headers, data=payload)
#
# print(response.text)
