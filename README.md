# Alonzo Church lambda calculus
https://en.wikipedia.org/wiki/Lambda_calculus
Курсовая работа по дисциплине "Теория алгоритмов".  Реализация лямбда-исчислений Алонзо Чёрча

## Лямбда-функции

- **TRUE**: 
  ```python
  TRUE = lambda a: lambda b: a
  ```
  Функция TRUE принимает два аргумента a и b и возвращает a. Это означает, что если функции TRUE передать два значения, она всегда вернет первое значение.

- **FALSE**: 
  ```python
  FALSE = lambda a: lambda b: b
  ```
  Функция FALSE принимает два аргумента a и b и возвращает b. Это означает, что если функции FALSE передать два значения, она всегда вернет второе значение.

- **NOT**: 
  ```python
  NOT = lambda a: a(FALSE)(TRUE)
  ```
  Функция NOT принимает один аргумент a и возвращает FALSE, если a истинно, и TRUE, если a ложно. Это позволяет инвертировать значение a.

- **OR**: 
  ```python
  OR = lambda a: lambda b: a(TRUE)(b)
  ```
  Функция OR принимает два аргумента a и b и возвращает TRUE, если хотя бы один из них истинен, и FALSE в противном случае.

- **AND**: 
  ```python
  AND = lambda a: lambda b: a(b)(FALSE)
  ```
  Функция AND принимает два аргумента a и b и возвращает TRUE, если оба аргумента истинны, и FALSE в противном случае.

- **XOR**: 
  ```python
  XOR = lambda a: lambda b: a(b(FALSE)(TRUE))(b(TRUE)(FALSE))
  ```
  Функция XOR (исключающее ИЛИ) принимает два аргумента a и b и возвращает TRUE, если только один из них истинен, и FALSE, если оба или ни один из них не истинны.

- **XNOR**: 
  ```python
  XNOR = lambda a: lambda b: NOT(XOR(a)(b))
  ```
  Функция XNOR (исключающее НЕ-ИЛИ) принимает два аргумента a и b и возвращает TRUE, если оба аргумента одновременно истинны или одновременно ложны, и FALSE, если один из них истинен, а другой ложен.

- **ID**: 
  ```python
  ID = lambda a: a
  ```
  Функция ID принимает один аргумент a и возвращает его же.

- **COMBINE_Y**: 
  ```python
  COMBINE_Y = lambda f: (
      (lambda x: f(lambda y: x(x)(y)))
      (lambda x: f(lambda y: x(x)(y)))
  )
  ```
  Функция COMBINE_Y использует комбинатор Y для создания рекурсивной функции, которая вызывает f с самой собой в качестве аргумента. Это позволяет создавать рекурсивные вычисления в лямбда-исчислении.

- **INCREMENT**: 
  ```python
  INCREMENT = lambda n: lambda a: lambda b: a(n(a)(b))
  ```
  Функция INCREMENT принимает число n и возвращает функцию, которая принимает два аргумента a и b. Возвращает результат a + n(b).

- **ADD**: 
  ```python
  ADD = lambda a: lambda b: a(INCREMENT)(b)
  ```
  Функция ADD принимает два аргумента a и b и возвращает результат их суммы.

- **MULTIPLY**: 
  ```python
  MULTIPLY = lambda a: lambda b: lambda c: a(b(c))
  ```
  Функция MULTIPLY принимает два аргумента a и b, и возвращает результат их произведения.

- **DECREMENT**: 
  ```python
  DECREMENT = lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda _: x)(ID)
  ```
  Функция DECREMENT принимает число n и возвращает функцию, которая принимает два аргумента f и x. Возвращает результат n - 1.

- **SUBTRACT**: 
  ```python
  SUBTRACT = lambda a: lambda b: b(DECREMENT)(a)
  ```
  Функция SUBTRACT принимает два аргумента a и b и возвращает результат их разности.

- **POWER**: 
  ```python
  POWER = lambda a: lambda b: b(a)
  ```
  Функция POWER принимает два аргумента a и b и возвращает результат a в степени b.

- **DIFF**: 
  ```python
  DIFF = lambda a: lambda b: ADD(SUBTRACT(a)(b))(SUBTRACT(b)(a))
  ```
  Функция DIFF принимает два аргумента a и b и возвращает разницу между ними.

- **DIVIDE**: 
  ```python
  DIVIDE = COMBINE_Y(
      lambda f: lambda a: lambda b: IS_LOWER(a)(b)
      (lambda _: FALSE)
      (lambda _: INCREMENT(f(SUBTRACT(a)(b))(b)))
      (FALSE)
  )
  ```
  Функция DIVIDE принимает два аргумента a и b и возвращает результат их деления.

- **IS_ZERO**: 
  ```python
  IS_ZERO = lambda a: a(lambda _: FALSE)(TRUE)
  ```
  Функция IS_ZERO принимает аргумент a и возвращает TRUE, если a равно нулю, и FALSE в противном случае.

- **IS_GREATER_OR_EQUAL**: 
  ```python
  IS_GREATER_OR_EQUAL = lambda a: lambda b: IS_ZERO(SUBTRACT(b)(a))
  ```
  Функция IS_GREATER_OR_EQUAL принимает два аргумента a и b и возвращает TRUE, если a больше или равно b, и FALSE в противном случае.

- **IS_GREATER**: 
  ```python
  IS_GREATER = lambda a: lambda b: IS_ZERO(SUBTRACT(INCREMENT(b))(a))
  ```
  Функция IS_GREATER принимает два аргумента a и b и возвращает TRUE, если a больше b, и FALSE в противном случае.

- **IS_LOWER_OR_EQUAL**: 
  ```python
  IS_LOWER_OR_EQUAL = lambda a: lambda b: IS_ZERO(SUBTRACT(a)(b))
  ```
  Функция IS_LOWER_OR_EQUAL принимает два аргумента a и b и возвращает TRUE, если a меньше или равно b, и FALSE в противном случае.

- **IS_LOWER**: 
  ```python
  IS_LOWER = lambda a: lambda b: IS_ZERO(SUBTRACT(INCREMENT(a))(b))
  ```
  Функция IS_LOWER принимает два аргумента a и b и возвращает TRUE, если a меньше b, и FALSE в противном случае.

- **IS_EQUAL**: 
  ```python
  IS_EQUAL = lambda a: lambda b: AND(IS_GREATER_OR_EQUAL(a)(b))(IS_LOWER_OR_EQUAL(a)(b))
  ```
  Функция IS_EQUAL принимает два аргумента a и b и возвращает TRUE, если a равно b, и FALSE в противном случае.

- **MIN**: 
  ```python
  MIN = lambda a: lambda b: IS_LOWER_OR_EQUAL(a)(b)(a)(b)
  ```
  Функция MIN принимает два аргумента a и b и возвращает меньшее из них.

- **MAX**: 
  ```python
  MAX = lambda a: lambda b: IS_GREATER_OR_EQUAL(a)(b)(a)(b)
  ```
  Функция MAX принимает два аргумента a и b и возвращает большее из них.

- **PAIR**: 
  ```python
  PAIR = lambda a: lambda b: lambda c: c(a)(b)
  ```
  Функция PAIR принимает два аргумента a и b и возвращает функцию, которая принимает другую функцию c и применяет её к a и b. Таким образом представляется связанная пара функций.

- **PAIR_SIGN**: 
  ```python
  PAIR_SIGN = lambda p: p(TRUE)
  ```
  Функция PAIR_SIGN принимает пару p и возвращает первый элемент пары.

- **PAIR_VALUE**: 
  ```python
  PAIR_VALUE = lambda p: p(FALSE)
  ```
  Функция PAIR_VALUE принимает пару p и возвращает второй элемент пары.

- **SIGN**: 
  ```python
  SIGN = lambda n: PAIR(TRUE)(n)
  ```
  Функция SIGN принимает число n и возвращает пару, где первый элемент - TRUE, а второй элемент - n.

- **UNSIGN**: 
  ```python
  UNSIGN = lambda p: PAIR_VALUE(p)
  ```
  Функция UNSIGN принимает пару p и возвращает второй элемент пары.

- **NEGATE**: 
  ```python
  NEGATE = lambda p: PAIR(NOT(PAIR_SIGN(p)))(PAIR_VALUE(p))
  ```
  Функция NEGATE принимает пару p и возвращает пару, где первый элемент - противоположный знаку первоначальной пары, а второй элемент остается неизменным.

- **IS_POSITIVE**: 
  ```python
  IS_POSITIVE = lambda p: PAIR_SIGN(p)
  ```
  Функция IS_POSITIVE принимает пару p и возвращает TRUE, если число положительное, иначе FALSE.

- **IS_NEGATIVE**: 
  ```python
  IS_NEGATIVE = lambda p: NOT(PAIR_SIGN(p))
  ```
  Функция IS_NEGATIVE принимает пару p и возвращает TRUE, если число отрицательное, иначе FALSE.

- **SIGNED_ADD**: 
  ```python
  SIGNED_ADD = lambda a: lambda b: (
      XNOR(PAIR_SIGN(a))(PAIR_SIGN(b))
      (PAIR(PAIR_SIGN(a))(ADD(PAIR_VALUE(a))(PAIR_VALUE(b))))
      (
          PAIR
          (XOR(PAIR_SIGN(a))(IS_LOWER_OR_EQUAL(PAIR_VALUE(a))(PAIR_VALUE(b))))
          (DIFF(PAIR_VALUE(a))(PAIR_VALUE(b)))
      )
  )
  ```
  Функция SIGNED_ADD принимает два аргумента a и b и возвращает их сумму с учетом знаков.

- **SIGNED_SUBTRACT**: 
  ```python
  SIGNED_SUBTRACT = lambda a: lambda b: SIGNED_ADD(a)(PAIR(NOT(PAIR_SIGN(b)))(PAIR_VALUE(b)))
  ```
  Функция SIGNED_SUBTRACT принимает два аргумента a и b и возвращает их разность с учетом знаков.

- **SIGNED_MULTIPLY**: 
  ```python
  SIGNED_MULTIPLY = lambda a: lambda b: PAIR(XNOR(PAIR_SIGN(a))(PAIR_SIGN(b)))(MULTIPLY(PAIR_VALUE(a))(PAIR_VALUE(b)))
  ```
  Функция SIGNED_MULTIPLY принимает два аргумента a и b и возвращает их произведение с учетом знаков.

- **SIGNED_DIVIDE**: 
  ```python
  SIGNED_DIVIDE = lambda a: lambda b: PAIR(XNOR(PAIR_SIGN(a))(PAIR_SIGN(b)))(DIVIDE(PAIR_VALUE(a))(PAIR_VALUE(b)))
  ```
  Функция SIGNED_DIVIDE принимает два аргумента a и b и возвращает их частное с учетом знаков.

- **SIGNED_POWER**: 
  ```python
  SIGNED_POWER = lambda a: lambda b: PAIR(OR(PAIR_SIGN(a))(NOT(PAIR_VALUE(b)(NOT)(PAIR_SIGN(a)))))(POWER(PAIR_VALUE(a))(PAIR_VALUE(b)))
  ```
  Функция SIGNED_POWER принимает два аргумента a и b и возвращает a в степени b с учетом знаков.



## Developers

- [T.Latypov](https://github.com/N0tilT) | Team lead
- [A.Simonov](https://github.com/dubstepTractor) | Classes lead
- [M.Cherepan](https://github.com/PolShestogo) | GUI lead
- [V.Ponomarev](https://github.com/vadimyt) | Tests lead
- [P.Gromova](https://github.com/jowlly)  | Docs lead

