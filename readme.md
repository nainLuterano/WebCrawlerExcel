# WebCrawler and excel

O pacote possui duas classes a webCrawler e o excel.

> O arquivo app.py possui um exemplo de uso das classes.

> Execute pip install -r requirements.txt para instalar as dependência das classes



## Classe webCrawler

    Métodos da classe  webCrawler:
        - setUrl
            parametro: 1° string        
            define a url do site que você quer.
        
        - setHeaders:
            parametro: 1° dicionário
            define o user agent que você quer usar, o formato é um dicionário. Por padrão e formato dos dado é esse.

> {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
            
        - getTags:
            parametros: 1° string
            retorna um array de objetos Tag ou array vazio se não houver tag na página buscada.

        - getTagsByClass:
            parametros: 1° string, 2° dicionário
            return um array de objetos Tag buscados, se não houver retorna um array vazio.

            > exemplo: getTagsByClass('span', {"class": "class1 class2"})
        
        - getFindById:
            parametros: 1° string
            return um Objeto Tag buscado por id, se não houver retorna objeto NoneType.
            
> getFindById('Id'). Id que você quer buscar.

        - download
            parametros: nenhum
            a função necessária para buscar o html da página e deve ser usada depois de definir url e setHeaders e  antes das outras funções de busca


## classe Excel

    Métodos da classe Excel:
        
        - setTitle
            parametros: 1° string
            define título da panilha

        - setHeader
            parametros: 1° array
            define o cabeçalho da tabela panilha
            
> setHeader(['Preço', 'Posição'])

        - setBody
            parametros: 1° array
            define os dados na linha panilha

> setBody(['R$ 12', 25])

        - setValueInPosition
            parametros: 1° int , 2° int, 3° string ou int
            define um valor em uma determinada posição na panilha
            
> setValueInPosition(row=1, column=2, 21)

        - setFunctionInPosition
            parametros: 1° string, 2° string
            define a função que a posição irá receber
            
> setValueInPosition('A21', '=SUM(A1:A12)')

        - save
            parametros: 1° string
            define o nome do arquivo excel e o formato e irá salvar dentro da pasta save

> save('dados.xlsx')

