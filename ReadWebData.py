
import requests
import bs4


res = requests.get('https://cs.qau.edu.pk/faculty.php')

soup = bs4.BeautifulSoup(res.text, 'html.parser')

facultyNames = []
facultyMail = []
facultyPhone = []

def remove_prefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]

#Extracting names
names = soup.select('td > strong')


for name in names:
    n = name.text
    n = n.replace('\n',' ')
    n = n.replace('     ',' ')
    n = n.replace('  ', ' ')
    if("Res" not in n and n != ''):
        facultyNames.append(n)

nam = soup.select("td > a >strong")
n = nam[0].text
n = n.replace('\n',' ')
n = n.replace('     ',' ')
n = n.replace('  ', ' ')
facultyNames.insert(1,n)

#extracting contact information
contact = soup.select('td > p > a')


for c in contact:
    if("tel" in c['href']):
        facultyPhone.append(remove_prefix(c['href'],"tel:"))
    else:
        facultyMail.append(remove_prefix(c['href'],"mailto:"))

#One phone number not found
facultyPhone.insert(5,' ')


file = open("Facultydetails.txt","w")
file.write("Name".ljust(60) + "Phone".ljust(60) + "Email" + "\n")
for (n,p,e) in zip(facultyNames,facultyPhone,facultyMail):
    line = '{:<30}  {:>30}  {:>40}'.format(n, p, e)
    file.write(line + '\n')


print(facultyNames)


