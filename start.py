import requests
import json
import sys

def start_menu():
    ans=True
    # for example arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--pass", help="that optional takes your github account", required=True);
    parser.add_argument("--user", help="that optional takes your github login", required=True);
    parser.add_argument("--repo",nargs="?", help="that optional argument has:\n \"rep_name\" and \"id_rep\"")
    args = parser.parse_args()
    # use args
    # !- token = args.pass -!
    # !- user = args.user -!
    # !- repo = args.repo -!
    # path to json setting about repo
    data = json.load(open('setting.json'))
    print ("""\nGet INFO by rest_api from GIT [link: """ + str(data['repo_link']) + "]" + "\n If change repo, please look setting.json in root directory")
    while ans:
        print ("""
        1.Get ID Author [commits]
        2.Get Username Owner [commits]
        3.Get SHA [commits]
        4.Get Email Owner [commits]
        5.Get Comment count [commits]
        6.Get Weeks [commits_activity]
        7.Exit/Quit
        """)
        ans=input("What would you like to do? ") 
        if ans=="1": 
          get_info('commits', 1)
        elif ans=="2":
          get_info('commits', 2)
        elif ans=="3":
          get_info('commits', 3)
        elif ans=="4":
          get_info('commits', 4)
        elif ans=="5":
          get_info('commits', 5)
        elif ans=="6":
          get_info('commits_activity', 6)
        elif ans=="7":
          print("\033c")
          sys.exit()
        elif ans !="":
          print("\n Not Valid Choice Try again")

def get_id_author(json_dict):
    print('\nid author: ' + str(json_dict[0].get('author').get('id')))

def get_username_owner(json_dict):
    print('username login: ' + json_dict[0].get('author').get('login'))

def get_repo_sha(json_dict):
    print('repo sha: ' + str(json_dict[0].get('commit').get('tree').get('sha')))

def get_owner_email(json_dict):
    print('owner email: ' + str(json_dict[1].get('commit').get('author').get('email')))

def get_comment_count(json_dict):
    print('comment count: ' + str(json_dict[1].get('commit').get('comment_count')))

def get_repo_weeks(json_dict):
    print('repo weeks: ' + str(json_dict[0].get('week')))

# use args in function / 
# data['user_name'] equal user, 
# data['token'] = equal token
# data['repo_link_n] = equal repo
#
def get_info(link_string, wget):
    data = json.load(open('setting.json'))
    if (link_string == 'commits'):
        rc = requests.get(data['repo_link_commits'], auth=(data['user_name'], data['token']))
        json_dict = rc.json()
        choose_wget(json_dict, wget)
    else:
        rca = requests.get(data['repo_link_commit_activity'], auth=(data['user_name'], data['token']))
        json_dict = rca.json()
        choose_wget(json_dict, wget)

def choose_wget(json_dict, wget):
    if (wget == 1):
        get_id_author(json_dict)
    elif (wget == 2):
        get_username_owner(json_dict)
    elif (wget == 3):
        get_repo_sha(json_dict)
    elif (wget == 4):
        get_owner_email(json_dict)
    elif (wget == 5):
        get_comment_count(json_dict)
    elif (wget == 6):
        get_repo_weeks(json_dict)
    print("\nPress enter for choose...")
    input()
    print("\033c")
    start_menu()

start_menu()
