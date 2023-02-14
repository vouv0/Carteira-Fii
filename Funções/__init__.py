carteira = []
dados = {}


class Ativo:
    def __init__(self, fii):
        import requests
        from bs4 import BeautifulSoup

        ativo = str(fii).lower().lstrip()
        url = 'https://www.fundsexplorer.com.br/funds/' + ativo

        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html.parser')

        self.nome = soup.find(class_="section-title").text
        self.preco = soup.find(class_="price").text.replace('\n', '').replace(' ', '')
        self.ultimo_rendimento = soup.find(class_='indicator-value').find_next(class_='indicator-value').text.replace(
            '\n',
            '').replace(
            ' ', '')
        self.dy = soup.find(class_='indicator-value').find_next(class_='indicator-value') \
            .findNext(class_='indicator-value').text.replace('\n', '').replace(' ', '').replace('%', '').replace(',', '.')
        self.vp = soup.find(class_='indicator-value').find_next(class_='indicator-value') \
            .findNext(class_='indicator-value').findNext(class_='indicator-value') \
            .findNext(class_='indicator-value').text.replace('\n', '').replace(' ', '')
        self.p_vp = float(self.preco.replace("R$", "").replace(",", ".")) / float(self.vp.replace("R$", "").replace(",", "."))

    def info_fii(self):
        print(f'Nome do FII: {self.nome}')
        print(f'Preço do FII: {self.preco}')
        print(f'Último rendimento: {self.ultimo_rendimento}')
        print(f'Dividend Yield: {self.dy}%')
        print(f'Valor patrimonial: {self.vp}')
        print(f'P/VP: {self.p_vp:.2f}\n')

    @staticmethod
    def mostra_carteira(lista):
        for item in range(len(lista)):
            print('=' * 20)
            for k, v in lista[item].items():
                print(f'{k} = {v}')
            print('=' * 20)


def add_carteira(fundo, lista, dicionario={}):
    dicionario.clear()
    dicionario['Nome'] = fundo.nome
    dicionario['Preço'] = fundo.preco
    dicionario['Último Rendimento'] = fundo.ultimo_rendimento
    dicionario['DY'] = fundo.dy
    dicionario['VP'] = fundo.vp
    dicionario['P/VP'] = fundo.p_vp.__round__(2)
    lista.append(dicionario.copy())
