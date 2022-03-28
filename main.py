from bs4 import BeautifulSoup
import requests
import time

#aca va la url de la pagina.
"""
html_text = requests.get('https://www.computrabajo.com.ar/trabajo-de-python').text
print(html_text)
"""

#Ahora buscamos los 'a' con clase js-o-link fc_base
"""
html_text = requests.get('https://www.computrabajo.com.ar/trabajo-de-python').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('a', class_ = 'js-o-link fc_base')
print(jobs)
"""

#Ahora buscamos solo un 'a' con clase js-o-link fc_base para el puest y a con class fc_base hover it-blank para la compañia // job.find es que busca adentro de job.
"""
html_text = requests.get('https://www.computrabajo.com.ar/trabajo-de-python').text
soup = BeautifulSoup(html_text, 'lxml')
job = soup.find('a', class_ = 'js-o-link fc_base')
company_name = soup.find('a', class_ = 'fc_base hover it-blank')
print(company_name)
"""

#Ahora copio el proyecto tal cual en times jobs. Con esto obtengo el puesto y la compañia que lo ofrece.
# Con replace evitamos los grandes espacios vacios. 
"""
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace (' ','')
print(company_name)
"""

#Ahora lo segmentamos con habilidades:
"""
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace (' ','')
skills = job.find('span', class_ = 'srp-skills').text.replace (' ','')
#print(skills)
#Ahora mostramos todo con cadena.
print(f'''
Company Name: {company_name}
Required Skills: {skills}
''')
"""

#Ahora filtramos los anuncios posteados recientemente. con span.text le decimos que busco un span adentro y solo imprima el texto. ponemos publiushed date primero para que pasados los few day ago no siga buscando otros trabajos. 
"""
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs:
    published_date = job.find('span', class_ = 'sim-posted').span.text
    if 'few' in published_date:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace (' ','')
        skills = job.find('span', class_ = 'srp-skills').text.replace (' ','')

        #Ahora mostramos todo con cadena.
        print(f'''
        Company Name: {company_name}    
        Required Skills: {skills}
        ''')               

        print('')            
"""

#------------PARTE 2-------------
# AHORA EMBELLECEMOS EL RESULTADO                                                         
#Con strip sacamos los espacios en blanco.
"""
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs:
    published_date = job.find('span', class_ = 'sim-posted').span.text
    if 'few' in published_date:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace (' ','')
        skills = job.find('span', class_ = 'srp-skills').text.replace (' ','')     
        print(f"Company Name: {company_name.strip()}")
        print(f"Required Skills: {skills.strip()}")

        print('')     
"""
#Ahora vamos a acceder al link con la descripcion de cada trabajo. 
#para ir dentro de archivos en more_info por ejemplo usamos los puntos. primero vamos a job (el li), despues entramos al header, adentro de header entramos al h2 y al final al "a".
"""
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs:
    published_date = job.find('span', class_ = 'sim-posted').span.text
    if 'few' in published_date:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace (' ','')
        skills = job.find('span', class_ = 'srp-skills').text.replace (' ','')     
        more_info = job.header.h2.a['href']
        print(f"Company Name: {company_name.strip()}")
        print(f"Required Skills: {skills.strip()}")
        print(f"More Info: {more_info}")

        print('')     
"""

#Ahora agregamos un input para que el usuario de la app pueda filtrar lo que quiera. 
"""
print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs:
    published_date = job.find('span', class_ = 'sim-posted').span.text
    if 'few' in published_date:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace (' ','')
        skills = job.find('span', class_ = 'srp-skills').text.replace (' ','')     
        more_info = job.header.h2.a['href']
        if unfamiliar_skill not in skills:
            print(f"Company Name: {company_name.strip()}")
            print(f"Required Skills: {skills.strip()}")
            print(f"More Info: {more_info}")

            print('')     
"""

#Ahora vamos a guardar un archivo con cada informacion extraida en posts. el programa se va a ejecutar automaticamente cada 10 minutos. \n es como un br

print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace (' ','')
            skills = job.find('span', class_ = 'srp-skills').text.replace (' ','')     
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'Posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info: {more_info}")
                print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)


