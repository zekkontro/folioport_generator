import errno
import shutil
import json
from scraper import WebScraper
import os
from colorama import init
from termcolor import colored

init()

scraper = WebScraper()

# Functions
def copyfolder(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno in (errno.ENOTDIR, errno.EINVAL):
            shutil.copy(src, dst)
        else: raise

def print_logo():
   os.system('cls' if os.name == 'nt' else 'clear')
   ascii_file = open("assets/folioport-ascii.txt", "r")
   ascii_image =  ascii_file.read()
   print(ascii_image)
   print("\n\n")
   print("                        The script developed by zekkontro")
   print("                     https://github.com/zekkontro/folioport")
   print("\n\n")




print_logo()

projectName = input("Project Name (output_site): ")

projectName = "output_site" if projectName == "" or projectName == None else projectName

firstName = input("Your First Name: ")
secondName = input("Your Second Name: ")
image_path = input("Profile image file: ")
email = input("Email: ")
role = input("Role: ")
introductionText = input("Introduction Text: ")
aboutMeText = input("About Me Text: ")
instagram = input("Instagram: ")
dribble = input("Dribble: ")
linkedin = input("LinkedIn: ")
github = input("GitHub Profile: ")
youtube = input("YouTube: ")
skills = input("Please enter the skills (Max 9) (Flutter, Python, SQL): ")
skills = skills.split(", ")

repo_input_count = int(input("Please enter github repo count (Max: 6): "))
repo_link_list = []

for x in range(repo_input_count):
   index_str = str(x + 1) 
   link = input("Repo " + index_str + " link: ")
   repo_link_list.append(link)

blog_input_count = int(input("Please enter medium blog count (Max: 3): "))
blogInputData = []

for x in range(blog_input_count):
   index_str = str(x + 1) 
   link = input("Blog " + index_str + " link: ")
   description = input("Blog " + index_str + " description: ")
   cover_image_link = input("Blog " + index_str + " cover image link: ")

   blogInputData.append({"cover_image_link": cover_image_link, "description": description, "link":link})

print_logo()
print("\n\n")

print(colored("Generating your web site...", color="yellow"))
print("\n\n")
# Scraping
githubRepos = scraper.getGithubRepos(repo_link_list)
mediumBlogs = scraper.getMediumBlogs(blogInputData)

data = {
 "firstName": firstName,
 "secondName": secondName,
 "email": email,
 "role": role,
 "introductionText": introductionText,
 "socialProfile": {
    "instagram": instagram,
    "dribble": dribble,
    "linkedin": linkedin,
    "github": github,
    "youtube": youtube
 },
 "githubRepos": githubRepos,
 "mediumBlogs": mediumBlogs,
 "skills": skills,
 "aboutMeText": aboutMeText
}
json_object = json.dumps(data, indent=4)


# create new project folder
copyfolder(src="default", dst=projectName)


# Save the json file
with open(projectName +'/assets/assets/data.json', 'w') as f:
    f.write(json_object)

# Copy developer image to website folder
shutil.copy(image_path, projectName +'/assets/assets/images/developer.jpeg')
    
print_logo()
print("\n\n")

print(colored("✔ Portfolio site generated with successfully", color="green"))