# Is Anagram

**Problema:** dadas duas strings `s` e `t`, retornar `True` se `t` for um anagrama de `s` (mesmas letras, qualquer ordem).

**Exemplo:**
```
s = "amj"
t = "jam"  →  True

s = "rat"
t = "car"  →  False
```

---

## Estratégia: Mapa de frequência

Contar quantas vezes cada letra aparece em cada string e comparar os dois mapas. Iguais → anagramas.

```python
if len(s) != len(t):
    return False                              # tamanhos diferentes: nem conta

countS, countT = {}, {}

for i in range(len(s)):                       # mesmo i serve pras duas, já têm o mesmo tamanho
    countS[s[i]] = 1 + countS.get(s[i], 0)
    countT[t[i]] = 1 + countT.get(t[i], 0)

return countS == countT
```

**Resultado dos dicts para `"amj"` / `"jam"`:**
```
countS = {"a": 1, "m": 1, "j": 1}
countT = {"j": 1, "a": 1, "m": 1}
countS == countT  →  True     ← ordem não importa
```

---

## Conceito: HashMap

Um **hashmap** guarda pares **chave → valor** e acha qualquer chave em **O(1)**: ele passa a chave por uma função de hash que aponta direto pra posição na memória — não varre a coleção. Em Python são duas caras da mesma estrutura:

| | Guarda | Serve pra |
|---|---|---|
| `dict` | chave → valor | associar uma informação à chave |
| `set`  | só a chave    | saber se a chave existe |

**É o padrão que mais aparece em problema de array/string** — quase sempre a pergunta se encaixa em um destes moldes:

| A pergunta | Estrutura | Problema |
|---|---|---|
| "já vi esse valor antes?" | `set` de visitados | Contains Duplicate |
| "quantas vezes aparece?" | `dict` contador | **Is Anagram** |
| "em que índice está?" | `dict` valor → índice | Two Sum |
| "quem tem a mesma assinatura?" | `dict` chave → lista | Group Anagrams |

Aqui o molde é o **contador**: a chave é a letra, o valor é quantas vezes ela apareceu. Como cada busca é O(1), o algoritmo todo fica O(n) — um passo por letra.

**`dict == dict`** compara **chaves e valores**, ignorando ordem — que é exatamente a definição de anagrama:

```python
{"a": 1, "b": 2} == {"b": 2, "a": 1}   # True   ← ordem ignorada
{"a": 1} == {"a": 2}                   # False  ← valor diferente
```

---

## A linha-chave

```python
countS[s[i]] = 1 + countS.get(s[i], 0)
```

Lê **da direita pra esquerda**:

| Parte | O que faz |
|---|---|
| `s[i]` | pega a letra na posição `i` da string |
| `countS.get(s[i], 0)` | valor atual dessa letra — **ou `0`** se nunca foi vista |
| `1 + ...` | soma 1 na contagem |
| `countS[s[i]] = ...` | grava o resultado de volta no dict |

O `.get(chave, default)` é o que evita o erro, porque na primeira vez a chave **não existe**:

```python
d = {"a": 1}
d["z"]          # KeyError!  ← quebra
d.get("z", 0)   # 0          ← o default salva
```

**Executando para `s = "amj"`:**
```
i=0  s[0]="a"  → get("a", 0) = 0  → 1 + 0 = 1  → countS = {"a": 1}
i=1  s[1]="m"  → get("m", 0) = 0  → 1 + 0 = 1  → countS = {"a": 1, "m": 1}
i=2  s[2]="j"  → get("j", 0) = 0  → 1 + 0 = 1  → countS = {"a": 1, "m": 1, "j": 1}
```

Todas as letras são novas, então sempre cai no default. Com letra repetida o `1 +` começa a valer:
```
s = "aab"
i=0  s[0]="a"  → get("a", 0) = 0  → 1 + 0 = 1  → {"a": 1}
i=1  s[1]="a"  → get("a", 0) = 1  → 1 + 1 = 2  → {"a": 2}   ← agora existe, soma em cima
i=2  s[2]="b"  → get("b", 0) = 0  → 1 + 0 = 1  → {"a": 2, "b": 1}
```

---

## Intuição rápida

> Anagrama = mesmas letras, mesma quantidade.
> Conta a frequência das letras nas duas strings e compara os mapas.
