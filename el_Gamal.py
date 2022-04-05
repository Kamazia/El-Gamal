import os
from random import randint

alfa = {
    '1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
    'А':10,'Б':11,'В':12,'Г':13,'Д':14,'Е':15,
    'Ж':16,'З':17,'И':18,'Й':19,'К':20,'Л':21,
    'М':22,'Н':23,'О':24,'П':25,'Р':26,'С':27,
    'Т':28,'У':29,'Ф':30,'Х':31,'Ц':32,'Ч':33,
    'Ш':34,'Щ':35,'Ъ':36,'Ы':37,'Ь':38,'Э':39,
    'Ю':40,'Я':41,
    'A':42,'B':43,'C':44,'D':45,'E':46,'F':47,
    'G':48,'H':49,'I':50,'J':51,'K':52,'L':53,
    'M':54,'N':55,'O':56,'P':57,'Q':58,'R':59,
    'S':60,'T':61,'U':62,'V':63,'W':64,'X':65,
    'Y':66,'Z':67,
    ' ':68,',':69,'.':70
}


class Gamal:
    def __init__(self, p:int, g:int, message:str) -> None:
        self.p = p 
        self.g = g
        self.message = message
        self.x = randint(1,self.p)
    
    def key_generation(self) -> tuple:
        y = self.poww(self.g,self.x,self.p)

        with open (f'{os.path.dirname(os.path.abspath(__file__))}\\encryption.txt','w') as f:
            f.write(f'Open Key : {y} {self.p} {self.g}\n')
            
        return (y,self.p,self.g)

    def poww(self,base:int,degree:int|str,module:int) -> int:
        '''
        Быстрое возведение в степень слева направо
        '''
        degree = bin(degree)[2:]
        answer = 1

        for i in range(len(degree) - 1, -1, -1):
            answer = (answer * base ** int(degree[i])) % module
            base = (base ** 2) % module
        
        return answer
        
    def convert(self) -> tuple:
        convert_message = []
        for litter in self.message:
            convert_message.append(alfa[litter.upper()])

        return tuple(convert_message)

    def encryption(self,y:int,m:tuple)-> str:
        encrypt_message = ''

        for digit in m:

            k = randint(1,self.p-1)
            while self.nod(self.p,k) != 1:
                k = randint(1,self.p-1)

            a = self.poww(self.g,k,self.p)
                
            encrypt_message += ' ' +str(a)

            f1 = self.poww(y,k,self.p)
            b = self.poww(digit*f1,1,self.p)
            encrypt_message +=' ' + str(b)
        
        with open (f'{os.path.dirname(os.path.abspath(__file__))}\\encryption.txt','a') as f:
            f.write(f'Encryption message : {encrypt_message}')

        return encrypt_message.lstrip()

    def nod(self,a:int, b:int) -> int:
        '''
        Нахождение наибольшего общего делителя
        '''

        while a!= 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        else:
            return a + b

    def decryption(self,m:str,secret_key) -> str:
        if type(m) != tuple:
            m = m.split()
        descryption_message = []

        for digit in range(0,len(m)-1,2):
            b = int(m[digit+1])
            a = self.poww(int(m[digit]),self.p-1-int(secret_key),self.p)
            i = self.poww(b * a,1,self.p)

            letter = [key for key in alfa if alfa[key] == i]
            try:
                descryption_message.append(letter[0])
            except IndexError:
                return 'Calculation error. P or g is set incorrectly.'

        if not descryption_message:
             return 'The message is specified incorrectly.'

        return ''.join(descryption_message)

    def main(self):
        print(f'Y = {self.g} в степени {self.x} по модулю {self.p}')
        y = self.key_generation()[0]
        print(f'Y = {y}, X = {self.x}')
        open_key = self.key_generation()
        print(f'Open K: {open_key}, Secret key: {self.x}')
        convert_message = self.convert()
        print(f'Message converted by table: {convert_message}')
        print('\n*-------------------------------------------*\n')
        encrypt_message = self.encryption(y,convert_message)
        print(f'Encrypted message: {encrypt_message}')
        print('\n*-------------------------------------------*\n')
        descryption_message = self.decryption(encrypt_message,self.x)
        print(f'Descrypted message: {descryption_message}')
        print('\n*-------------------------------------------*\n')


if __name__ == '__main__':
    
    a = Gamal(259517,92,'Hello.its me you old best friend')
    a.main()