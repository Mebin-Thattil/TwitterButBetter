'''
Python File so that bots can create posts
'''
import ollama
import time
import userdetails
post_list,hashtag_list = [],[]
def generate_llm_response():
        response = ollama.chat(model='content_bot_llm', messages=[
        {
            'role': 'user',
            'content': "generate",
        },
        ])
        return(response['message']['content'])
def cleanup_before_sql_query(content): #this function makes sure sql does not throw syntax for using ' as it also represents a comment
    return content.replace("'",'"')


#number_of_users = int(input("Enter How many users you want to generate for: "))
for i in range(1):
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
        print("Inserting post [", (i+1), '/', len(post_list),']...')
        username = cleanup_before_sql_query(username.strip(":"))
        postcontent = cleanup_before_sql_query(post_list[i].strip(":"))
        topics = cleanup_before_sql_query(hashtag_list[i].strip(":"))

        userdetails.insertpost(username, postcontent ,topics)
        time.sleep(0.01)
