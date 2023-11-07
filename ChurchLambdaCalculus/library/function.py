# Логика
TRUE    = lambda a: lambda b: a
FALSE   = lambda a: lambda b: b
NOT     = lambda a: a(FALSE)(TRUE)
OR      = lambda a: lambda b: a(TRUE)(b)
AND     = lambda a: lambda b: a(b)(FALSE)
XOR     = lambda a: lambda b: a(b(FALSE)(TRUE))(b(TRUE)(FALSE))
XNOR    = lambda a: lambda b: NOT(XOR(a)(b))

ID          = lambda a: a
COMBINE_Y   = lambda f: (
    (lambda x: f(lambda y: x(x)(y)))
    (lambda x: f(lambda y: x(x)(y)))
)

# Натуральные числа
INCREMENT   = lambda n: lambda a: lambda b: a(n(a)(b))
ADD         = lambda a: lambda b: a(INCREMENT)(b)
MULTIPLY    = lambda a: lambda b: lambda c: a(b(c))
DECREMENT   = lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda _: x)(ID)
SUBTRACT    = lambda a: lambda b: b(DECREMENT)(a)
POWER       = lambda a: lambda b: b(a)
DIFF        = lambda a: lambda b: ADD(SUBTRACT(a)(b))(SUBTRACT(b)(a))
DIVIDE      = COMBINE_Y(
    lambda f: lambda a: lambda b: IS_LOWER(a)(b)
    (lambda _: FALSE)
    (lambda _: INCREMENT(f(SUBTRACT(a)(b))(b)))
    (FALSE)
)

# Проверки
IS_ZERO             = lambda a: a(lambda _: FALSE)(TRUE)
IS_GREATER_OR_EQUAL = lambda a: lambda b: IS_ZERO(SUBTRACT(b)(a))
IS_GREATER          = lambda a: lambda b: IS_ZERO(SUBTRACT(INCREMENT(b))(a))
IS_LOWER_OR_EQUAL   = lambda a: lambda b: IS_ZERO(SUBTRACT(a)(b))
IS_LOWER            = lambda a: lambda b: IS_ZERO(SUBTRACT(INCREMENT(a))(b))
IS_EQUAL            = lambda a: lambda b: AND(IS_GREATER_OR_EQUAL(a)(b))(IS_LOWER_OR_EQUAL(a)(b))

# Максимум и минимум
MIN = lambda a: lambda b: IS_LOWER_OR_EQUAL(a)(b)(a)(b)
MAX = lambda a: lambda b: IS_GREATER_OR_EQUAL(a)(b)(a)(b)

# Пары
PAIR        = lambda a: lambda b: lambda c: c(a)(b)
PAIR_SIGN   = lambda p: p(TRUE)
PAIR_VALUE  = lambda p: p(FALSE)

# Числа и знаки
SIGN        = lambda n: PAIR(TRUE)(n)
UNSIGN      = lambda p: PAIR_VALUE(p)
NEGATE      = lambda p: PAIR(NOT(PAIR_SIGN(p)))(PAIR_VALUE(p))
IS_POSITIVE = lambda p: PAIR_SIGN(p)
IS_NEGATIVE = lambda p: NOT(PAIR_SIGN(p))
SIGNED_ADD  = lambda a: lambda b: (
    XNOR(PAIR_SIGN(a))(PAIR_SIGN(b))
    (PAIR(PAIR_SIGN(a))(ADD(PAIR_VALUE(a))(PAIR_VALUE(b))))
    (
        PAIR
        (XOR(PAIR_SIGN(a))(IS_LOWER_OR_EQUAL(PAIR_VALUE(a))(PAIR_VALUE(b))))
        (DIFF(PAIR_VALUE(a))(PAIR_VALUE(b)))
    )
)
SIGNED_SUBTRACT = lambda a: lambda b: SIGNED_ADD(a)(PAIR(NOT(PAIR_SIGN(b)))(PAIR_VALUE(b)))
SIGNED_MULTIPLY = lambda a: lambda b: PAIR(XNOR(PAIR_SIGN(a))(PAIR_SIGN(b)))(MULTIPLY(PAIR_VALUE(a))(PAIR_VALUE(b)))
SIGNED_DIVIDE   = lambda a: lambda b: PAIR(XNOR(PAIR_SIGN(a))(PAIR_SIGN(b)))(DIVIDE(PAIR_VALUE(a))(PAIR_VALUE(b)))

# Конвертация числа Черча в конкретное число.
ENCODE_INCREMENT    = lambda x: x + 1
ENCODE_NATURAL      = lambda n: n(ENCODE_INCREMENT)(0)

def decodeBoolean(value: bool):
    return TRUE if value else FALSE

def decodeNatural(value: int):
    return INCREMENT(decodeNatural(value - 1)) if value > 0 else FALSE

def decodeSigned(value: int):
    return PAIR(TRUE if value >= 0 else FALSE)(decodeNatural(abs(value)))

def encodeBoolean(function):
    return function is TRUE

def encodeNatural(function):
    return ENCODE_NATURAL(function)

def encodeSigned(function):
    value = encodeNatural(UNSIGN(function))
    return value if IS_POSITIVE(function) is TRUE else 0 - value
