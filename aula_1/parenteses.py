def zero_division_to_inf(fn):
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except ZeroDivisionError:
            return float('inf')
    return wrapper

@zero_division_to_inf
def f(x):
    return 1 / x

@zero_division_to_inf
def g(x, y, z):
    return x ** y * (z / x)

@zero_division_to_inf
def h(x):
    return 99 / (x - 3)

v = [ 'Lucas', 'Ricciardi', 'de', 'Salles' ]

inf = float('inf') 

X = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

for x in X:
    print('f({}) = {}'.format(x, g(x, 2, 2)))

def cache(fn):
    fn._cache = {}
    def wrapper(*args, **kwargs):
        if args not in fn._cache:
            fn._cache[args] = fn(*args)
        return fn._cache[args]
    return wrapper

@cache
def fib(n):
    if n < 1:
        return 1
    return fib(n-1) + fib(n-2)

fib = cache(fib)

for i in range(100):
    print(i, fib(i))

def login_required(fn):
    def wrapper(*args, **kwargs):
        user = User.get_by_email(flask.request.cookies.get('email'))
        if not user.authenticated():
            return 'permission denied', 403
        return fn(*args, **kwargs)
    return wrapper

class Xpto:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def reducer(self):
        return self.a + self.b + self.c

registro = {
    'a': 1,
    'b': 2,
    'c': 3
}
registros = [ registro ] * 100

print(type(registros[0]))

registros = [ 
    Xpto(**r) for r in registros 
]

print(type(registros[0]))

r = registros[0]
print(r.reducer())

class ContaBancaria:

    @staticmethod
    def ver_descricao():
        return {
            'saque_maximo': 5000
        }

    def __init__(self, capital_inicial):
        self.saldo = capital_inicial

    def depositar(self, dinheiro):
        self.saldo += dinheiro

    def sacar(self, dinheiro):
        self.saldo -= dinheiro

class ContaPoupanca(ContaBancaria):

    @staticmethod
    def ver_descricao():
        return {
            'saque_maximo': 1000
        }

    def __init__(self, capital_inicial):
        self.saldo = capital_inicial

    def depositar(self, dinheiro):
        self.saldo += dinheiro

    def sacar(self, dinheiro):
        self.saldo -= dinheiro

ContaBancaria.ver_descricao()

lucas = ContaBancaria(1000)
fabiola = ContaBancaria(2000)

lucas.depositar(500)        # depositar(lucas, 500)
fabiola.depositar(1000)     # depositar(fabiola, 1000)

print(lucas.saldo)
print(fabiola.saldo)

class Vetor:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return '[{}, {}, {}]'.format(self.x, self.y, self.z)

    def __add__(self, other):
        return Vetor(self.x + other.x, self.y + other.y, self.z + other.z)

u = Vetor(1, 2, 3)
v = Vetor(3, 4, 5)

print(u)
print(v)

w = u + v

print(w)