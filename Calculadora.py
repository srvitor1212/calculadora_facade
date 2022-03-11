

class Calculadora:

    def __init__(self) -> None:        
        self.__val1:float = 0
        self.__val2:float = 0
        self.__oper:str = '+'
        self.__resultado:float = 0

        print('>>> Iniciando calculadora')
        self._coletar_dados()
        self._calcular(self.__val1, self.__val2, self.__oper)


    @property
    def resultado(self):
        return self.__resultado


    def _coletar_dados(self):
        print('>>> Informe os valores para calculo')
        print('>>> Operações [ + - / * ]')
        print('>>>')

        v1 = input('Valor 1 ...: ')
        op = input('Operação ..: ')
        v2 = input('Valor 2 ...: ')

        self.__val1 = v1
        self.__val2 = v2
        self.__oper = op

    def _calcular(self, valor_1:float=0, valor_2:float=0, operacao:str='+'):
        
        if operacao == '+':
            self.calculo = Somar(valor_1, valor_2)
        elif operacao == '-':
            self.calculo = Subtrair(valor_1, valor_2)
        elif operacao == '/':
            self.calculo = Dividir(valor_1, valor_2)
        elif operacao == '*':
            self.calculo = Multiplicar(valor_1, valor_2)
        else:
            raise NotImplementedError('Validar operação, essa operação é inválida')

        self.__resultado = self.calculo.resultado
        return self.__resultado


# ---------------------------------------------------------------------------------------------------------

class Somar:
    def __init__(self, vl_1:float=0, vl_2:float=0) -> None:
        self.__vl_1 = vl_1
        self.__vl_2 = vl_2
        
    @property
    def resultado(self):
        return (float(self.__vl_1) + float(self.__vl_2))


class Subtrair:
    def __init__(self, vl_1:float=0, vl_2:float=0) -> None:
        self.__vl_1 = vl_1
        self.__vl_2 = vl_2
        
    @property
    def resultado(self):
        return (float(self.__vl_1) - float(self.__vl_2))


class Dividir:
    def __init__(self, vl_1:float=0, vl_2:float=0) -> None:
        self.__vl_1 = vl_1
        self.__vl_2 = vl_2
        
    @property
    def resultado(self):
        return (float(self.__vl_1) / float(self.__vl_2))


class Multiplicar:
    def __init__(self, vl_1:float=0, vl_2:float=0) -> None:
        self.__vl_1 = vl_1
        self.__vl_2 = vl_2
        
    @property
    def resultado(self):
        return (float(self.__vl_1) * float(self.__vl_2))




# ---------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    print('\n\n\n')
    print('----------------------------------------------')

    print('>>> Para sair CTRL + C')
    while True:
        calc = Calculadora()
        print('________________________')
        print(calc.resultado)
