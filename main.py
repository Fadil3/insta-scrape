from instascrape import *

# Instantiate the scraper objects 
post = Post('https://www.instagram.com/p/xxxx/')
result = []
# Scrape their respective data 
post.scrape()

# convert unix timestamp to readable date

#  remove enter character
# python function to remove enter character
def remove_enter(text):
    return text.replace('\n', '')

def remove_quotation_mark(text):
    for i in range(len(text)):
        if text[i] == '"':
            text = text[:i] + text[i+1:]
    return text

# append the result to the list
result.append(post.likes)
result.append(post.comments)
result.append(post.video_view_count)
result.append(post.username)

result.append(datetime.datetime.fromtimestamp(
        int(post.timestamp)
    ).strftime('%Y-%m-%d %H:%M:%S'))

result.append(remove_enter(post.caption))
result.append(post.location)
result.append(remove_quotation_mark(post['hashtags']))
result.append(post.tagged_users)

for i in result:
    print(i)




