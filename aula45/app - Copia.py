from abc import ABC, abstractmethod
import random 
import	itertools
from time import sleep

class CassaNiquel:
    def __init__(self, level = 1):
        self.SIMBOLOS = {
            'money_mouth_face': '1F911',
            'money_bag': '1F4B0',
            'credit_card': '1F4B3',
            'slot_machine': '1F3B0',
            'gem_stone': '1F48E',
            'money_with_wings': '1F4B8'
        }
        self.level = level # Nível da máquina
        self.permutations = self._gen_permutations()

    def _gen_permutations(self):
        permutations = list(itertools.product(self.SIMBOLOS.keys(), repeat=3))
        for j in range(self.level):
            for i in self.SIMBOLOS.keys():
                permutations.append((i, i, i))
        return permutations
    
    def _get_final_result(self):
        if not hasattr(self, 'permutations'):
            self.permutations = self._gen_permutations()

        result = list(random.choice(self.permutations))

        if len(set(result)) == 3 and random.randint(0,5) >= 2:
            result[1] = result[0]
     
        return result

    def _display(self, amount_bet, result, time=.01):
        seconds = 1
        for i in range(0, int(seconds/time)):
            print(self._emojize(random.choice(self.permutations)))
            sleep(time)  
        print(self._emojize(result))

        if self._check_result_user(result):
            print(f'Você venceu e recebeu: {amount_bet * 3}')
        else:
            print(f'Foi quase, tente novamente.')

    def _emojize(self, emojis):
        return ''.join(tuple(chr(int(self.SIMBOLOS[code], 16)) for code in emojis))

    def _check_result_user(self, result):
        x = [result[0] == x for x in result]
        return True if all(x) else False 

maquina1 = CassaNiquel()
maquina1._display(0, maquina1._get_final_result())