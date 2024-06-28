'''
Python File so that bots can create posts
'''
import ollama
import time
post_list,hashtag_list = [],[]
from userdetails import insertpost
def generate_llm_response():
        response = ollama.chat(model='content_bot_llm', messages=[
        {
            'role': 'user',
            'content': "generate",
        },
        ])
        return(response['message']['content'])

number_of_users = int(input("Enter How many users you want to generate for: "))
for i in range(number_of_users):
    print("Started please wait...")
    response = generate_llm_response()
    response_list = response.split('\n')
    while '' in response_list:
          response_list.remove('')
    start_index_username = 0
    for i in range(len(response_list[0])):
          if response_list[0][i] == ":":
                start_index_username = i
                break
    username = response_list[0][start_index_username:]
    print(response_list,'\n\n\n')
    print('username is',username)

    start_index_post,end_index_post = 0,0
    for i in response_list[1:]:
        for j in range(len(i)):
            if i[j] == ':':
                start_index_post = j
                break

        for j in range(len(i)):
            if i[j] == '#':
                end_index_post = j
                break
        
        post = i[start_index_post:end_index_post]  
        hashtags = i[end_index_post:].split("#")
        while '' in hashtags:
          hashtags.remove('')
        hashtags = ",".join(hashtags)
        print('POST IS: ', post) 
        post_list.append(post)

        print("HASHTAGS is:", hashtags) 
        hashtag_list.append(hashtags)

push_to_db = input("Should I push to DB[y/n]: ")
if push_to_db == 'y':
     for i in range(len(post_list)):
        insertpost(username, post_list[i], hashtag_list[i])
        time.sleep(0.5)