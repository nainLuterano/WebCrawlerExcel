# -*- coding: utf-8 -*-
from webCrawler import webCrawler as Web
from excel import Excel

datas = []
prices = []

def getWeb(url):
    web = Web()
    web.setUrl(url)
    web.download()
    return web


web = getWeb('https://nerdstore.com.br/categoria/vestuario/camisetas/')

#pega os nomes dos produtos dessa página web
for nameProduct in web.getTagsByClass('h2', {"class": "woocommerce-loop-product__title"}):
    datas.append([nameProduct.text])


#pega os preços dos produtos dessa página web
for htmlSpan in web.getTagsByClass('span', {"class": "price"}):
    if len(htmlSpan.findAll('del')) == 0:
        for price in htmlSpan.findAll('bdi'):
            prices.append(price.text)
    else:
        for ins in htmlSpan.findAll('ins'):
            for price in ins.findAll('bdi'):
                prices.append(price.text)

#adiciona os preços do produto com nome
for index in range(0, len(prices)):
    datas[index].append(prices[index])



excel = Excel()

#define o título da panilha
excel.setTitle('datas camisas nerdstore')

#define célulars A1 e B1, mas poderia adicionar C1,D1...
excel.setHeader(["camisetas", "preços"])

#adiciona os dados
for dado in datas:
    excel.setBody(dado)

#salva o arquivo na pasta save
excel.save('datas.xlsx')

print('Finalizado')
