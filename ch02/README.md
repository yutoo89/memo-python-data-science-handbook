# NumPyの基礎

ドキュメント、画像、サウンドクリップ、数値測定結果など、すべてのデータを数値の配列として扱う。
NumPyは、Numerical Pythonの略。

## データ型

Pythonは動的型付け言語で、変数のデータ型を明示的に宣言しなくても、自動的に推測される。

```python
result = 0
for i range(100)
  result += i
```

type関数で変数の型を確認することができる。

```bash
In [12]: type(result)
Out[12]: int
```

### 整数

Cの整数は、整数値を格納するメモリ内の位置のラベル。
しかしPythonの整数は、整数値を格納するデータを含むPythonオブジェクト情報を格納するメモリ内の位置のポインタ。
これによりPythonではより柔軟にコーディングできるようになるが、同時にオーバーヘッドでもある。

### リスト

リストはPythonの標準的なコンテナで、可変個の要素を格納する。

```bash
In [13]: l = list(range(10))

In [14]: l
Out[14]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

動的型付けにより、異なる型の要素をひとつのリストに格納できる。

```bash
In [16]: l = [True, "2", 3.0, 4]

In [17]: [type(item) for item in l]
Out[17]: [bool, str, float, int]
```

しかし、これを実現するためには、各要素が独自に型や参照数を持つ必要があるため、コストがかかる。
すべての変数が同じ型であるケースでは、これらの情報は冗長なので、固定型配列に格納した方が効率的。

配列は連続したデータブロックへのポイントだが、リストはポインタ列へのポインタで、ポインタ列のポインタは、完全なPythonオブジェクトを指している。

## 固定型配列

配列モジュールarrayはPython3.3から利用可能になった。
次のように型が同一の配列を作成する。

```bash
In [18]: import array

In [19]: l = list(range(10))

In [20]: a = array.array('i', l)

In [21]: a
Out[21]: array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

NumPyパッケージのndarrayを使って、Pythonリストから配列を作成する例。
numpyをインポートする際、監修的にnpという別名をつけるらしい。

```bash
In [26]: import numpy as np
    ...: np.array([1, 4, 2, 5, 3])
Out[26]: array([1, 4, 2, 5, 3])
```

NumPy配列の要素は、すべて同じ型である必要があるため、たとえば整数の配列に浮動小数点があると、整数は浮動小数点にアップキャストされる。

```bash
In [27]: import numpy as np
    ...: np.array([1, 4, 2, 5, 3.14])
Out[27]: array([1.  , 4.  , 2.  , 5.  , 3.14])
```

NumPy配列は、リストのリストを使用して多次元配列を作ることもできる。

```bash
In [28]: np.array([range(i, i + 3) for i in [2, 4, 6]])
Out[28]: 
array([[2, 3, 4],
       [4, 5, 6],
       [6, 7, 8]])
```

NumPyに組み込まれた関数を使って、次のような配列を作ることができる。
多次元配列も第一引数で行数と列数を指定して作ることができる。

```bash
# 要素が0である長さ10の配列
In [30]: np.zeros(10, dtype=int)
Out[30]: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# 要素が1である3行5列の配列
In [31]: np.ones((3, 5), dtype=float)
Out[31]: 
array([[1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.]])

# 要素が3.14である3行5列の配列
In [32]: np.full((3, 5), 3.14)
Out[32]: 
array([[3.14, 3.14, 3.14, 3.14, 3.14],
       [3.14, 3.14, 3.14, 3.14, 3.14],
       [3.14, 3.14, 3.14, 3.14, 3.14]])

# 開始値0、終了値20で2ずつ増加する配列
In [34]: np.arange(0, 20, 2)
Out[34]: array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])

# 最小値0、最大値10で差が均等な5つの要素の配列
In [35]: np.linspace(0, 10, 5)
Out[35]: array([ 0. ,  2.5,  5. ,  7.5, 10. ])

# 最小値0、最大値1の間に分布したランダムな値の配列
In [36]: np.random.random((3, 3))
Out[36]: 
array([[0.51945132, 0.52146822, 0.52597043],
       [0.75445209, 0.91722423, 0.76609237],
       [0.96959243, 0.75895462, 0.97508106]])

# 平均0、標準偏差1の正規分布乱数の配列
In [38]: np.random.normal(0, 1, (3, 3))
Out[38]: 
array([[ 0.95584542,  0.50367991, -0.71427953],
       [ 1.48224292, -0.07371263, -0.46092532],
       [-0.40134372,  0.97331877, -1.18272122]])

# 0~10のランダムな数字の配列
In [40]: np.random.randint(0, 10, (3, 3))
Out[40]: 
array([[3, 6, 0],
       [1, 7, 5],
       [9, 3, 9]])

# 3行3列の単位行列
# 単位行列は、行列の対角の成分がすべて1、それ以外の成分が0の行列
# 単位行列と任意の行列の積は、任意の行列のままになる
# 単位行列を作る関数がなぜeyeなのか => Identity matrix（単位行列）の音が由来？
In [41]: np.eye(3)
Out[41]: 
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])

# 3つの整数の初期化されていない配列
# 各要素の値は、そのメモリ位置にすでに存在していたものになる
In [42]: np.empty(3)
Out[42]: array([1., 1., 1.])
```

## NumPyのデータ型

NumPyはC言語で実装されている。
配列を作るときにdtypeでデータ型を指定することができる。

> NumPyは、Pythonよりもはるかに多様な数値型をサポートしています。このセクションでは、使用可能なものと、配列のデータ型を変更する方法を示します。
> サポートされているプリミティブ型は、C言語のものと密接に結びついています。
> https://runebook.dev/ja/docs/numpy/user/basics.types

```bash
In [44]: np.zeros(10, dtype="int16")
Out[44]: array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=int16)
```

- int8	
  - i1
  - 符号あり8ビット整数型
- int16	
  - i2
  - 符号あり16ビット整数型
- int32	
  - i4
  - 符号あり32ビット整数型
- int64	
  - i8
  - 符号あり64ビット整数型
- uint8	
  - u1
  - 符号なし8ビット整数型
- uint16	
  - u2
  - 符号なし16ビット整数型
- uint32	
  - u4
  - 符号なし32ビット整数型
- uint64	
  - u8
  - 符号なし64ビット整数型
- float16	
  - f2
  - 半精度浮動小数点型（符号部1ビット、指数部5ビット、仮数部10ビット）
- float32	
  - f4
  - 単精度浮動小数点型（符号部1ビット、指数部8ビット、仮数部23ビット）
- float64	
  - f8
  - 倍精度浮動小数点型（符号部1ビット、指数部11ビット、仮数部52ビット）
- float128	
  - f16
  - 四倍精度浮動小数点型（符号部1ビット、指数部15ビット、仮数部112ビット）
- complex64	
  - c8
  - 複素数（実部・虚部がそれぞれfloat32）
- complex128	
  - c16
  - 複素数（実部・虚部がそれぞれfloat64）
- complex256	
  - c32
  - 複素数（実部・虚部がそれぞれfloat128）
- bool	
  - ?
  - ブール型（True or False）
- unicode	
  - U
  - Unicode文字列
- object	
  - O
  - Pythonオブジェクト型

## NumPy配列の属性

```bash
In [2]: import numpy as np
In [3]: np.random.seed(0)

# 1次元配列
In [6]: x1 = np.random.randint(10, size=6)

# 2次元配列
In [7]: x2 = np.random.randint(10, size=(3,4))

# 3次元配列
In [8]: x3 = np.random.randint(10, size=(3,4,5))

# ndim: 次元数
In [10]: print("x3 ndim: ", x3.ndim)
x3 ndim:  3

# shape: 各次元のサイズ
In [11]: print("x3 shape: ", x3.shape)
x3 shape:  (3, 4, 5)

# size: 配列の合計サイズ
In [12]: print("x3 size: ", x3.size)
x3 size:  60
```

配列のサイズをバイト数で取得することもできる。

```bash
# 各要素のバイト数
In [13]: print("itemsize: ", x3.itemsize)
itemsize:  8

# 配列の合計サイズ
In [14]: print("nbytes: ", x3.nbytes)
nbytes:  480
```

## 配列要素にアクセスする

```bash
In [8]: x1
Out[8]: array([5, 0, 3, 3, 7, 9])

# 角カッコにインデックスを指定してアクセスする
In [9]: x1[0]
Out[9]: 5

# 負の数を指定すると配列の最後から数える
In [10]: x1[-1]
Out[10]: 9

In [12]: x2
Out[12]: 
array([[3, 5, 2, 4],
       [7, 6, 8, 8],
       [1, 6, 7, 7]])

# 2次元配列はカンマ区切りでインデックスを指定する
In [13]: x2[0, 0]
Out[13]: 3

# 行・列ともに0から始まるので注意
In [16]: x2[1, 2]
Out[16]: 8
```

このインデックス表記で配列要素の変更もできる。

```bash
In [17]: x2[1, 2] = 99

In [18]: x2
Out[18]: 
array([[ 3,  5,  2,  4],
       [ 7,  6, 99,  8],
       [ 1,  6,  7,  7]])
```

2次元配列の行を取り出す場合は下記。

```bash
In [19]: x2[1]
Out[19]: array([ 7,  6, 99,  8])
```

NumPy配列は固定型なので、整数配列に浮動小数点を入れると勝手に小数点以下が切り捨てられる。

```bash
In [22]: x1
Out[22]: array([8, 1, 5, 9, 8, 9])

In [23]: x1[0] = 3.14

In [24]: x1
Out[24]: array([3, 1, 5, 9, 8, 9])
```

## 配列のスライス

NumPyのスライス構文は、標準のPythonリストの構文に従う。

```py
x[start:stop:step]
```

```bash
In [1]: import numpy as np
In [2]: x = np.arange(10)
In [3]: x
Out[3]: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# インデックス5以降
In [4]: x[5:]
Out[4]: array([5, 6, 7, 8, 9])

# 最初の5要素
In [5]: x[:5]
Out[5]: array([0, 1, 2, 3, 4])

# ステップ3を指定
In [7]: x[0:9:3]
Out[7]: array([0, 3, 6])

# ステップを負の値にすると降順になる
In [8]: x[::-1]
Out[8]: array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
```

## ユニバーサル関数

Pythonのデフォルト実装では、動的に型を解釈するという言語の性質のため、ループ処理が低速。

```py
import numpy as np
np.random.seed(0)
​
def compute_reciprocals(valus):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output
​
values = np.random.randint(1, 10, size=5)
compute_reciprocals(values)
# array([0.16666667, 1.        , 0.25      , 0.25      , 0.125     ])

big_array = np.random.randint(1, 100, size=1000000)
%timeit compute_reciprocals(big_array)
# 10.9 µs ± 192 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)
```

上記は、操作そのものではなく、ループの各サイクルでPythonが行う型チェックと関数の呼び出しに時間がかかる。
コンパイルされたコードであれば、コードの実行前に型が判明しているため、効率的に計算することができる。

NumPyのufunc(ユニバーサル関数)は、Pythonのネイティブ算術演算子を使用する。

```bash
In [3]: import numpy as np
   ...: x = np.arange(5)

In [4]: print(x)
[0 1 2 3 4]
In [5]: print(x + 5)
[5 6 7 8 9]
In [6]: print(x - 5)
[-5 -4 -3 -2 -1]
In [7]: print(x * 2)
[0 2 4 6 8]
In [8]: print(x / 2)
[0.  0.5 1.  1.5 2. ]

# 整数除算
In [9]: print(x // 2)
[0 0 1 1 2]

# べき乗
In [10]: print(x ** 2)
[ 0  1  4  9 16]
```

上記は、NumPyに組み込まれた特定の関数へのラッパー。
たとえば+演算子はadd関数のラッパー。

```bash
In [11]: np.add(x, 2)
Out[11]: array([2, 3, 4, 5, 6])
```

絶対値を取得する。

```bash
In [2]: abs(x)
Out[2]: array([2, 1, 0, 1, 2])

In [3]: np.abs(x)
Out[3]: array([2, 1, 0, 1, 2])
```

三角関数を計算する。

```
In [1]: import numpy as np
   ...: theta = np.linspace(0, np.pi, 3)
   ...: print("theta: ", theta)
theta:  [0.         1.57079633 3.14159265]

In [2]: print("sin(theta): ", np.sin(theta))
sin(theta):  [0.0000000e+00 1.0000000e+00 1.2246468e-16]

In [3]: print("cos(theta): ", np.cos(theta))
cos(theta):  [ 1.000000e+00  6.123234e-17 -1.000000e+00]

In [4]: print("tan(theta): ", np.tan(theta))
tan(theta):  [ 0.00000000e+00  1.63312394e+16 -1.22464680e-16]
```

指数関数と対数関数。

指数とは、数学におけるexponentの訳。その数がaのn乗で表されるときのnのこと。


```bash
In [1]: import numpy as np
In [2]: x = [1, 2, 3, 4]

# e^x
In [3]: print(np.exp(x))
[ 2.71828183  7.3890561  20.08553692 54.59815003]

# 2^x
In [4]: print(np.exp2(x))
[ 2.  4.  8. 16.]

# 3^x
In [5]: print(np.power(3, x))
[ 3  9 27 81]
```


