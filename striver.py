from bs4 import BeautifulSoup
import requests 
response=requests.get("https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/")
soup=BeautifulSoup(response.content,'html.parser')
td_tags = soup.find_all('td')
for title in td_tags:
    anchors=title.find_all('a')
print(anchors)
# for leetcode in td_tags:
#     leetcodetags.append(leetcode.findall("a"))
# # Iterate over the found <td> tags and extract href attributes from <a> tags
# for td_tag in td_tags:
#     a_tag = td_tag.find('a')
#     if a_tag:
#         href_value = a_tag.get('href')
#         print(f'Found href value: {href_value}')
