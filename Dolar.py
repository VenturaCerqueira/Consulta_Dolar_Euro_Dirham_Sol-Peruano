import requests
from bs4 import BeautifulSoup
# Cconfiguração headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
# Get pagina
page_dolar = requests.get(
    "https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar&oq=cota%C3%A7%C3%A3o+dolar&aqs=chrome..69i57.2231j0j1&sourceid=chrome&ie=UTF-8", headers=headers)
page_euro = requests.get("https://www.google.com/search?q=cota%C3%A7%C3%A3o+euro&sxsrf=APwXEdeWGq-ySLYJ18paC-wSlzlPUhaNqw%3A1682523483653&ei=W0VJZNSwJ8PS1sQP_MKVmA4&ved=0ahUKEwiUysa08Mf-AhVDqZUCHXxhBeMQ4dUDCA8&uact=5&oq=cota%C3%A7%C3%A3o+euro&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJzIICAAQgAQQsQMyBQgAEIAEMgsIABCABBCxAxCDATIICAAQgAQQsQMyBQgAEIAEMgUIABCABDIFCAAQgAQyCwgAEIAEELEDEIMBMgUIABCABDoKCAAQRxDWBBCwAzoKCAAQigUQsAMQQ0oECEEYAFDsBlirCWDaCmgBcAF4AIABnwGIAeMEkgEDMC40mAEAoAEByAEKwAEB&sclient=gws-wiz-serp", headers=headers)
page_dirham = requests.get("https://www.google.com/search?q=cota%C3%A7%C3%A3o+dirham&sxsrf=APwXEdeB_AnqqkOToNzbvx0XTn9s7ZyfrQ%3A1682524377198&ei=2UhJZMPgC5Wx5OUPibSmwAo&oq=cota%C3%A7%C3%A3o+dihan&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgAMgwIABCABBAKEEYQggIyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyBwgAEIAEEAoyCAgAEBYQHhAKMggIABAWEB4QCjoKCAAQRxDWBBCwAzoKCAAQigUQsAMQQzoVCC4QigUQxwEQ0QMQyAMQsAMQQxgBOgQIIxAnOgsIABCABBCxAxCDAToICAAQgAQQsQM6BQgAEIAEOgsIABCKBRCxAxCDAUoECEEYAFCKA1i6CWDWHWgBcAF4AIABpwGIAb0GkgEDMC41mAEAoAEByAELwAEB2gEECAEYCA&sclient=gws-wiz-serp", headers=headers)
page_sol_peruano = requests.get("https://www.google.com/search?q=cota%C3%A7%C3%A3o+sol+peruano&sxsrf=APwXEdfeS6WiK6k8TvDMRm7IIa-dgDR_5g%3A1682530712295&ei=mGFJZPe3EavI1sQPt-a7uAs&oq=cota%C3%A7%C3%A3o+sol&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgAMgkIIxAnEEYQggIyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CggAEEcQ1gQQsAM6CggAEIoFELADEEM6FQguEIoFEMcBENEDEMgDELADEEMYAToECCMQJzoICAAQgAQQsQM6CwgAEIAEELEDEIMBSgQIQRgAULkCWNgFYLILaAFwAXgAgAGiAYgB3gOSAQMwLjOYAQCgAQHIAQvAAQHaAQQIARgI&sclient=gws-wiz-serp", headers=headers)


# Coletor HTML
valor_dolar = BeautifulSoup(page_dolar.content, "html.parser")
valor_euro = BeautifulSoup(page_euro.content, "html.parser")
valor_dirham = BeautifulSoup(page_dirham.content, "html.parser")
valor_sol_peruano = BeautifulSoup(page_sol_peruano.content, "html.parser")

# Busca do valor
dolar = valor_dolar.find_all("span", class_="DFlfde SwHCTb")[0]
euro = valor_euro.find_all("span", class_="DFlfde SwHCTb")[0]
dirham = valor_dirham.find_all("span", class_="DFlfde SwHCTb")[0]
sol_peruano = valor_sol_peruano.find_all("span", class_="DFlfde SwHCTb")[0]

print(f'1 Dólar Americano igual a R$:', dolar.text)
print(f'1 Euro igual a R$:', euro.text)
print(f'1 Dirham igual a R$:', dirham.text)
print(f'1 Novo sol peruano igual a R$:', sol_peruano.text)
