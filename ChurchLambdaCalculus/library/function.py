IDENTITY    = lambda a: a
NULL        = lambda _: TRUE
IS_NULL     = lambda _: lambda _: FALSE

# Логика
TRUE        = lambda a: lambda b: a
FALSE       = lambda a: lambda b: b
NOT         = lambda a: a(FALSE)(TRUE)
OR          = lambda a: lambda b: a(TRUE)(b)
AND         = lambda a: lambda b: a(b)(FALSE)
XOR         = lambda a: lambda b: a(b(FALSE)(TRUE))(b(TRUE)(FALSE))
XNOR        = lambda a: lambda b: NOT(XOR(a)(b))

# Натуральные числа
INC     = lambda n: lambda a: lambda b: a(n(a)(b))
ADD     = lambda a: lambda b: a(INC)(b)
MUL     = lambda a: lambda b: lambda c: a(b(c))
DEC     = lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda _: x)(IDENTITY)
SUB     = lambda a: lambda b: b(DEC)(a)
POW     = lambda a: lambda b: b(a)
DIFF    = lambda a: lambda b: ADD(SUB(a)(b))(SUB(b)(a))

# Базовые числа Черча
ZERO    = FALSE
ONE     = IDENTITY

# Проверки
IS_ZERO = lambda a: a(lambda _: FALSE)(TRUE)
GTE     = lambda a: lambda b: IS_ZERO(SUB(b)(a))
LTE     = lambda a: lambda b: IS_ZERO(SUB(a)(b))
GT      = lambda a: lambda b: IS_ZERO(SUB(INC(b))(a))
LT      = lambda a: lambda b: IS_ZERO(SUB(INC(a))(b))
EQ      = lambda a: lambda b: AND(GTE(a)(b))(LTE(a)(b))

# Максимум и минимум
MIN = lambda a: lambda b: LTE(a)(b)(a)(b)
MAX = lambda a: lambda b: GTE(a)(b)(a)(b)

# Пары
CONS    = lambda a: lambda b: lambda c: c(a)(b)
CAR     = lambda p: p(TRUE)
CDR     = lambda p: p(FALSE)

# Числа и знаки
SIGN    = lambda n: CONS(TRUE)(n)
NEG     = lambda p: CONS(NOT(CAR(p)))(CDR(p))
ISPOS   = lambda p: CAR(p)
ISNEG   = lambda p: NOT(CAR(p))
UNSIGN  = lambda p: CDR(p)
SADD    = lambda a: lambda b: (
    XNOR(CAR(a))(CAR(b))
    (CONS(CAR(a))(ADD(CDR(a))(CDR(b))))  # одинаковые знаки
    (
        CONS # разные знаки
        (XOR(CAR(a))(LTE(CDR(a))(CDR(b))))  # вычисление знака
        (DIFF(CDR(a))(CDR(b)))   # вычисление значения
    )
)
SSUB    = lambda a: lambda b: SADD(a)(CONS(NOT(CAR(b)))(CDR(b)))
SMUL    = lambda a: lambda b: CONS(XNOR(CAR(a))(CAR(b)))(MUL(CDR(a))(CDR(b)))

# Конвертация числа Черча в конкретное число.
INC_INT = lambda x: x + 1
TO_INT  = lambda n: n(INC_INT)(0)

# Сконвертировать конкретное число в число Черча. 
def int2church(i):
    if i <= 0:
        return ZERO
    else:
        return INC(int2church(i - 1))

# Исполнить код в строке и напечатать результат.
def peval(s):
    print(s + ' = ' + str(eval(s)))
