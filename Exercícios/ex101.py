# 65+ opcional
from datetime import datetime
from my_codes import titulo, end_program


def voto(ano):
    y = datetime.today().year
    idade = y - ano
    if idade > 65:
        return f'Tendo {idade} anos, seu voto é opcional'
    elif idade >= 18:
        return f'Tendo {idade} anos, seu voto é obrigatório!'
    else:
        return f'Tendo {idade} anos, você ainda não vota'


titulo('FUNÇÃO COM RETORNO - VOTO', 40)
print(voto(int(input('Ano de nascimento: '))))
end_program()
