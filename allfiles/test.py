import userdetails
for i in range(2):
    # username = 
    # userdetails.insertpost("some_user","this is the body of the post", "tag1,tag2,tag3")
        #print("Inserting post [", i, '/', len(post_list),']...')
        username = "EchoFlux85"
        postcontent = "I''m obsessed with the new album by Tame Impala! The psychedelic vibes are giving me life. Kevin Parker is a genius!"
        topics = "TameImpala ,PsychedelicRock ,NewMusic"
        print("username=" ,username, "\nPostcontent = " ,postcontent,"\nTopics=",topics)
        userdetails.insertpost(username, postcontent ,topics)
print("Done")