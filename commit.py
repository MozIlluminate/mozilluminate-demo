# -*- coding: utf-8 -*-
import json
from oauth2client.client import SignedJwtAssertionCredentials
import gspread

def get_key_from_url(url):
    m1 = gspread.client._url_key_re_v1.search(url)
    if m1:
        return m1.group(1)
    else:
        m2 = gspread.client._url_key_re_v2.search(url)
        if m2:
            return m2.group(1)
        else:
            raise Exception("Can't find key from url")

with open('./testcases_locations.txt', 'r') as f:
    testcases_locations = f.readlines()
#json_key = json.load(open('./client_secret_858094982432-q0c0lgpdcapff1vakt4eblevgvp4aq53.apps.googleusercontent.com.json'))
json_key = json.load(open('./MozIlluminate-d50d3f14975a.json')) #FIXME: hardcode
scope = ['https://spreadsheets.google.com/feeds']
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
gc = gspread.authorize(credentials)

# Open a worksheet from spreadsheet with one shot
#wks = gc.open_by_url("https://docs.google.com/spreadsheets/d/1HuKEdxLjXmHpqcVbdmRCc6uZ9LBGpAsYPJ4mJml4cyU/edit#gid=491677371")
for testcases_location in testcases_locations:
    wks = gc.open_by_url(testcases_location).sheet1
#wks = gc.open_by_key("1HuKEdxLjXmHpqcVbdmRCc6uZ9LBGpAsYPJ4mJml4cyU").sheet1

#wks.update_acell('B2', "it's down there somewhere, let me take another look.")

# Fetch a cell range
    test_case_title = wks.find('Test Case')
    test_cases_col = wks.col_values(test_case_title.col)
    test_steps_title = wks.find('Test Steps')
    test_steps_col = wks.col_values(test_steps_title.col)
#cell_list = wks.range('A1:B7')
    test_cases = zip(test_cases_col, test_steps_col)
    test_cases_json = []
    for test_case in test_cases:
        if test_case[0] != "":
            test_cases_json.append({
                'id': test_case[0],
                'instructions':test_case[1], # need to parse it
                'suite':[] # need to decide suite
            })
            #print u"Title: {}".format(test_case[0])
            #print u"-----\n{}\n=====\n".format(test_case[1])
    filename = './testcases/' + get_key_from_url(testcases_location) + ".json"
    with open(filename, 'w') as f:
        json.dump(test_cases_json, f, indent=2)

    #print json.dumps(test_cases_json, indent=3)
#[
#    {id:
#     suites:[]
#     instructions:[
#         {
#             instruction:
#             expected
#             number
#         }
#     ]
#     }
#
#]

