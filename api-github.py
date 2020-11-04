import requests
import json

class ListInformations():

    def __init__(self, user):
        self._user = user

    def request_api(self):
        response = requests.get(
            f'https://api.github.com/users/{self._user}')    

        if response.status_code == 200:
            return response.json()
        else:
            print("User not found")
            return response.status_code   
            
    def list_informations(self):
        datas_api = self.request_api()
        print("\n")
        print("User: ",datas_api['login'])
        print("ID: ",datas_api['id'])
        print("Avatar Url: ",datas_api['avatar_url'])
        print("Name: ",datas_api['name'])
        print("Company: ",datas_api['company'])
        print("Location: ",datas_api['location'])
        print("Bio: ",datas_api['bio'])
        print("Number of public repositories: ",datas_api['public_repos'])
        print("Number Followers: ",datas_api['followers'])
        print("Number Following: ",datas_api['following'])
        print("User created at: ",datas_api['created_at'])
        print("User updated at: ",datas_api['updated_at'])

class ListRepositories():
    def __init__(self, user):
        self._user = user

    def request_api(self):
        response = requests.get(
            f'https://api.github.com/users/{self._user}/repos') 

        if response.status_code == 200:
            return response.json()
        else:
            print("User not found")
            return response.status_code   
            
    def list_repositories(self):
        print("\nList of Repositories:\n ")
        datas_api = self.request_api()
        for i in range(len(datas_api)):
            print(datas_api[i]['name'])
        print("\n")

        
user = input("Enter the name of the github user: ")
informations = ListInformations(user)
repositories = ListRepositories(user)
informations.list_informations()
repositories.list_repositories()
