# pandasを使ったデータ操作

DataFrameは多次元の配列で、行と列のラベルが付与され、異なる型や欠損値を許容する。

## Series

Seriesオブジェクトは1次元のインデックス付きのデータ。
Seriesは、リストまたは配列から作成できる。

```bash
# リストからSeriesを作成
import pandas as pd
In [9]: data = pd.Series([0.25, 0.5, 0.75, 1.0])
In [10]: data
Out[10]: 
0    0.25
1    0.50
2    0.75
3    1.00
dtype: float64

# 配列からSeriesを作成
In [1]: import pandas as pd
   ...: import numpy as np
In [2]: arr = np.arange(0, 20, 2)
In [4]: series = pd.Series(arr)

# values属性はNumPy配列
In [5]: series.values
Out[5]: array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])
# index属性はpd.Indexの配列に似たオブジェクト
In [6]: series.index
Out[6]: RangeIndex(start=0, stop=10, step=1)
```

SeriesとNumPy配列の違いはインデックスの存在にある。
インデックスは整数である必要はなく、任意の型で構成できる。

```bash
In [4]: arr = np.linspace(0, 20, 5)
   ...: arr
Out[4]: array([ 0.,  5., 10., 15., 20.])
# インデックスに文字列を使用する
In [8]: data = pd.Series(arr, index=['a', 'b', 'c', 'd', 'e'])
In [9]: data
Out[9]: 
a     0.0
b     5.0
c    10.0
d    15.0
e    20.0
dtype: float64
```

## DataFrame

DataFrameは行と列をもつ2次元配列に例えられる。

```py
# 人口
population_dict = {
  'California': 38332521,
  'Texas': 26448193,
  'New York': 19651127
}
population = pd.Series(population_dict)

# 面積
area_dict = {
  'California': 423967,
  'Texas': 695662,
  'New York': 141297
}
area = pd.Series(area_dict)

# 人口と面積のSeriesからDataFrameを作成
states = pd.DataFrame({
  'population': population,
  'area': area
})
states

Out[16]: 
            population    area
California    38332521  423967
Texas         26448193  695662
New York      19651127  141297
```

DataFrameはindex属性と列にアクセスするためのcolumns属性をもつ。

```bash
In [18]: states.index
Out[18]: Index(['California', 'Texas', 'New York'], dtype='object')

In [19]: states.columns
Out[19]: Index(['population', 'area'], dtype='object')

In [21]: states['area']
Out[21]: 
California    423967
Texas         695662
New York      141297
Name: area, dtype: int64
```

辞書のリストからもDataFrameを作成でき、辞書内に見つからない値はNaNで埋める。

```py
In [24]: pd.DataFrame([
    ...:   {'a': 1, 'b': 2},
    ...:   {'b': 3, 'c': 4}
    ...: ])
Out[24]: 
     a  b    c
0  1.0  2  NaN
1  NaN  3  4.0
```

2次元NumPy配列からDataFrameを作成する。

```py
# 3行2列の二次元配列
In [25]: np.random.rand(3, 2)
Out[25]: 
array([[0.98625273, 0.11776922],
       [0.70299981, 0.74584383],
       [0.54616266, 0.54801788]])

# 二次元配列からDataFrameを作成
In [28]: pd.DataFrame(
    ...:   np.random.rand(3, 2),
    ...:   columns=['foo', 'bar'],
    ...:   index=['a', 'b', 'c']
    ...: )
Out[28]: 
        foo       bar
a  0.150188  0.205562
b  0.744482  0.028064
c  0.990841  0.529022
```

SeriesとDataFrameは、データの参照と変更のためのIndexオブジェクトを持つ。
Indexは、変更できない配列または順序付き集合を考えることができる。

```py
In [32]: df = pd.DataFrame(
    ...:   np.random.rand(3, 2),
    ...:   columns=['foo', 'bar'],
    ...:   index=['a', 'b', 'c']
    ...: )

In [33]: df
Out[33]: 
        foo       bar
a  0.160525  0.892786
b  0.720032  0.055069
c  0.475056  0.847682

# DataFrameはindex属性をもつ
In [34]: ind = df.index

In [35]: ind
Out[35]: Index(['a', 'b', 'c'], dtype='object')
```

IndexオブジェクトはNumPy配列と同じような振る舞いをするが、不変である点が異なる。

```py
In [36]: ind[1]
Out[36]: 'b'

In [37]: ind[::2]
Out[37]: Index(['a', 'c'], dtype='object')

# size, shape, ndim, dtypeなどの属性をもつ
In [38]: print(ind.size, ind.shape, ind.ndim, ind.dtype)
3 (3,) 1 object

In [39]: ind[1] = 0
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Input In [39], in <cell line: 1>()
----> 1 ind[1] = 0

File /usr/local/lib/python3.9/site-packages/pandas/core/indexes/base.py:5021, in Index.__setitem__(self, key, value)
   5019 @final
   5020 def __setitem__(self, key, value):
-> 5021     raise TypeError("Index does not support mutable operations")

TypeError: Index does not support mutable operations
```

Indexオブジェクトは、和集合、積集合、差集合などを計算することができる。

```py
indA = pd.Index([1, 3, 5, 7, 9])
indB = pd.Index([2, 3, 5, 7, 11])

# 積集合
In [45]: indA & indB
<ipython-input-45-99513bddffa9>:1: FutureWarning: Index.__and__ operating as a set operation is deprecated, in the future this will be a logical operation matching Series.__and__.  Use index.intersection(other) instead.
  indA & indB
Out[45]: Int64Index([3, 5, 7], dtype='int64')

# 和集合
In [46]: indA | indB
<ipython-input-46-2c4bfb638f37>:1: FutureWarning: Index.__or__ operating as a set operation is deprecated, in the future this will be a logical operation matching Series.__or__.  Use index.union(other) instead.
  indA | indB
Out[46]: Int64Index([1, 2, 3, 5, 7, 9, 11], dtype='int64')

# 対称差
In [47]: indA ^ indB
<ipython-input-47-3946b5999e74>:1: FutureWarning: Index.__xor__ operating as a set operation is deprecated, in the future this will be a logical operation matching Series.__xor__.  Use index.symmetric_difference(other) instead.
  indA ^ indB
Out[47]: Int64Index([1, 2, 9, 11], dtype='int64')
```

```py

In [48]: states
Out[48]: 
            population    area
California    38332521  423967
Texas         26448193  695662
New York      19651127  141297

# 行と列の反転
In [49]: states.T
Out[49]: 
            California     Texas  New York
population    38332521  26448193  19651127
area            423967    695662    141297

# 行の取得
In [50]: states.values[0]
Out[50]: array([38332521,   423967])

# 列の取得
In [52]: states['area']
Out[52]: 
California    423967
Texas         695662
New York      141297
Name: area, dtype: int64

# ilocは単純なNumPy配列のようにインデックスする
In [55]: states.iloc[:2, :1]
Out[55]: 
            population
California    38332521
Texas         26448193

# locは列ラベルを使用する
In [57]: states.loc[:'Texas', :'population']
Out[57]: 
            population
California    38332521
Texas         26448193

# 行ラベルでスライスする
In [61]: states['California': 'Texas']
Out[61]: 
            population    area
California    38332521  423967
Texas         26448193  695662
```

## 欠損値を埋める

和集合を計算する際、どちらかの値が欠けている場合は通常NaN（Not a Number：非数）になる。

```py
A = pd.Series([2, 4, 6], index=[0, 1, 2])
B = pd.Series([1, 3, 5], index=[1, 2, 3])
# 欠けている値はNaNになる
A + B
Out[62]: 
0    NaN
1    5.0
2    9.0
3    NaN
dtype: float64

# add関数のfill_valueオプションで欠損値を補完できる
In [63]: A.add(B, fill_value=0)
Out[63]: 
0    2.0
1    5.0
2    9.0
3    5.0
dtype: float64
```

2次元配列とそのなかの一行の差を計算する。

```
In [67]: arr = np.random.rand(3, 2)
    ...: arr
Out[67]: 
array([[0.34473969, 0.29138741],
       [0.66456743, 0.94137339],
       [0.85588268, 0.76000334]])

In [68]: arr - arr[0]
Out[68]: 
array([[0.        , 0.        ],
       [0.31982774, 0.64998598],
       [0.51114299, 0.46861594]])
```

## 欠損値の扱い

欠損しているデータを一般的にnull値、NaN値、NA値と呼ぶ。
pandasは非浮動小数点データ型に対するNA値の組み込み概念を持たないNumPyパッケージに依存するため、欠損値の処理には制約が存在する。

Noneはデータが欠損していることを示すPythonオブジェクト。
Pythonオブジェクトであるため、任意のNumPy配列やpandas配列では使用できず、データ型が'object'である配列でのみ使用できる。

```py
In [71]: np.array([1, 2, 3, 4]).dtype
Out[71]: dtype('int64')

# Noneが混在するとobject型になってしまう
In [69]: np.array([1, None, 3, 4])
Out[69]: array([1, None, 3, 4], dtype=object)
```

None値を持つ配列にsum()やmin()などの集約演算を行うとエラーになる。

```py
In [73]: np.array([1, None, 3, 4]).sum()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Input In [73], in <cell line: 1>()
----> 1 np.array([1, None, 3, 4]).sum()

File /usr/local/lib/python3.9/site-packages/numpy/core/_methods.py:48, in _sum(a, axis, dtype, out, keepdims, initial, where)
     46 def _sum(a, axis=None, dtype=None, out=None, keepdims=False,
     47          initial=_NoValue, where=True):
---> 48     return umr_sum(a, axis, dtype, out, keepdims, initial, where)

TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
```

NaNは、Noneとは異なり標準のIEEE浮動小数点表現を使用するすべてのシステムで認識される特殊な浮動小数点数。

```py
# NaNは浮動小数点値であることに注意
In [74]: arr = np.array([1, np.nan, 3, 4])
    ...: arr.dtype
Out[74]: dtype('float64')
In [75]: arr
Out[75]: array([ 1., nan,  3.,  4.])

# NumPyはNaNを無視する特別な集約関数をもっている
In [76]: np.nanmax(arr)
Out[76]: 4.0
```

NaNとNoneは別物だが、pandasでは両者を同じように扱う。
整数配列の要素にNaNやNoneが混在する場合、自動的に浮動小数点型にアップキャストする。
このときNoneはNaNに変換される。

```bash
In [5]: x = pd.Series([1, np.nan, 2, None])
In [6]: x
Out[6]: 
0    1.0
1    NaN
2    2.0
3    NaN
dtype: float64
```

Seriesオブジェクトには、null値を検出するためのメソッドが用意されている。

```bash
In [12]: x = pd.Series([1, np.nan, 2, None])
    ...: x
Out[12]: 
0    1.0
1    NaN
2    2.0
3    NaN
dtype: float64

# null値のマスク配列
In [13]: x.isnull()
Out[13]: 
0    False
1     True
2    False
3     True
dtype: bool

# not null値のマスク配列
In [14]: x.notnull()
Out[14]: 
0     True
1    False
2     True
3    False
dtype: bool

# null値以外を取得する方法
In [15]: x[x.notnull()]
Out[15]: 
0    1.0
2    2.0
dtype: float64
```

DataFrameのdropna()は、null値を含む行または列を削除する。

```py
df = pd.DataFrame([
  [1, np.nan, 2],
  [2, 3, 5],
  [np.nan, 4, 6],
])

In [17]: df
Out[17]: 
     0    1  2
0  1.0  NaN  2
1  2.0  3.0  5
2  NaN  4.0  6

# null値を含まない行を取得
In [18]: df.dropna()
Out[18]: 
     0    1  2
1  2.0  3.0  5

# null値を含まない列を取得
In [19]: df.dropna(axis='columns')
Out[19]: 
   2
0  2
1  5
2  6
```

dropna()はhowパラメータやthreshパラメータで削除する行や列を制御できる。
how='any'はデフォルトでnullを一つでも含む行や列を削除するが、how='all'はすべての要素がnullの場合のみ削除する。

```py
In [21]: df[3] = np.nan
In [22]: df
Out[22]: 
     0    1  2   3
0  1.0  NaN  2 NaN
1  2.0  3.0  5 NaN
2  NaN  4.0  6 NaN

# すべての要素がnullの行を削除する
In [23]: df.dropna(how='all')
Out[23]: 
     0    1  2   3
0  1.0  NaN  2 NaN
1  2.0  3.0  5 NaN
2  NaN  4.0  6 NaN

# すべての要素がnullの列を削除する
In [24]: df.dropna(how='all', axis='columns')
Out[24]: 
     0    1  2
0  1.0  NaN  2
1  2.0  3.0  5
2  NaN  4.0  6

# 下記は値（非null値）が2つ以上含まれる列を残す
In [26]: df.dropna(thresh=2, axis='columns')
Out[26]: 
     0    1  2
0  1.0  NaN  2
1  2.0  3.0  5
2  NaN  4.0  6
```

## 階層型インデックス

多重インデックスは次のように作る。

```py
import pandas as pd
import numpy as np
index = [
  ('California', 2000),
  ('California', 2010),
  (  'New York', 2000),
  (  'New York', 2010),
  (     'Texax', 2000),
  (     'Texax', 2010)
]
index = pd.MultiIndex.from_tuples(index)
index
Out[1]: 
MultiIndex([('California', 2000),
            ('California', 2010),
            (  'New York', 2000),
            (  'New York', 2010),
            (     'Texax', 2000),
            (     'Texax', 2010)],
           )

populations = [
  33871648,
  37253956,
  18976457,
  19372352,
  20851820,
  25145561
]
pop = pd.Series(populations, index = index)
In [3]: pop
Out[3]: 
California  2000    33871648
            2010    37253956
New York    2000    18976457
            2010    19372352
Texax       2000    20851820
            2010    25145561
dtype: int64
```

2番目のインデックスが2010であるすべてのデータにアクセスする場合は、スライス表現を使う。
この方式は、タプルをインデックスに使った多重インデックス方式よりも効率的。

```py
In [4]: pop[:, 2010]
Out[4]: 
California    37253956
New York      19372352
Texax         25145561
dtype: int64
```

unstack()メソッドは、多重インデックスを使ったSeriesをDataFrameに変換する。

```py
pop_df = pop.unstack()
pop_df
Out[5]: 
                2000      2010
California  33871648  37253956
New York    18976457  19372352
Texax       20851820  25145561
```

2次元のデータはDataFrameで表現できるので、多重インデックスのSeriesで表現する必要がないように見える。
しかし、多重インデックスを使えばSeriesやDataFrameで3次元以上のデータを表現することもできる。

MultiIndexを使って、各州の人口データに別の列を追加することもできる。
ここでは18歳未満の人口を追加している。

```py
pop_df = pd.DataFrame({
  'total': pop,
  'under18': [
    9267089,
    9284094,
    4687374,
    4318033,
    5906301,
    6879014
  ]
})
pop_df
Out[6]: 
                    total  under18
California 2000  33871648  9267089
           2010  37253956  9284094
New York   2000  18976457  4687374
           2010  19372352  4318033
Texax      2000  20851820  5906301
           2010  25145561  6879014
```

## MultiIndexの作成方法

MultiIndexの最も簡単な作成方法は、インデックス配列のリストをコンストラクタに渡すこと。

```py
df = pd.DataFrame(
  np.random.rand(4,2),
  index=[
    ['a', 'a', 'b', 'b'],
    [1, 2, 1, 2]
  ],
  columns=['data1', 'data2']
)
df
```

あるいは、適切なタプルをもつ辞書を渡すと、pandasはデフォルトでMultiIndexを使用する。

```py
data = {
  ('California', 2000): 33871648,
  ('California', 2010): 37253956,
  ('New York', 2000): 18976457,
  ('New York', 2010): 19372352,
  ('Texax', 2000): 20851820,
  ('Texax', 2010): 25145561
}
series = pd.Series(data)
series
Out[8]: 
California  2000    33871648
            2010    37253956
New York    2000    18976457
            2010    19372352
Texax       2000    20851820
            2010    25145561
dtype: int64
```

それぞれのインデックスのデカルト積からMultiIndexを作ることもできる。

```py
pd.MultiIndex.from_product([
  ['a', 'b'],
  [1, 2]
])
Out[9]: 
MultiIndex([('a', 1),
            ('a', 2),
            ('b', 1),
            ('b', 2)],
           )
```

## MuntiIndexのレベル名

MultiIndexのレベルに名前をつける方法には、MultiIndexのコンストラクタにnames引数を渡す方法と、作成後にnames属性を設定する方法がある。

```py
In [13]: pop.index.names
Out[13]: FrozenList(['state', 'year'])
In [14]: pop
Out[14]: 
state       year
California  2000    33871648
            2010    37253956
New York    2000    18976457
            2010    19372352
Texax       2000    20851820
            2010    25145561
dtype: int6
```

DataFrameにおいて行と列は完全に対称であり、行がMuntiIndexを持てるなら、列もMultiIndexをもつことができる。

```py
index = pd.MultiIndex.from_product(
  [
    [2013, 2014],
    [1, 2]
  ],
  names=['year', 'visit']
)
columns = pd.MultiIndex.from_product(
  [
    ['bob', 'guido', 'sue'],
    ['HR', 'Temp']
  ],
  names=['subject', 'type']
)

# 適当にデータを埋める
data = np.round(np.random.randn(4, 6), 1)
data[:, ::2] *= 10
data += 37
Out[18]: 
array([[43. , 36.4, 43. , 38.7, 30. , 36.3],
       [39. , 34.8, 40. , 34.8, 48. , 38.1],
       [31. , 38.1, 35. , 36.4, 13. , 38.5],
       [28. , 38.2, 59. , 37.8, 53. , 38.3]])

# DataFrameの作成
health_data = pd.DataFrame(data, index=index, columns=columns)
health_data
Out[24]: 
subject      bob       guido         sue      
type          HR  Temp    HR  Temp    HR  Temp
year visit                                    
2013 1      43.0  36.4  43.0  38.7  30.0  36.3
     2      39.0  34.8  40.0  34.8  48.0  38.1
2014 1      31.0  38.1  35.0  36.4  13.0  38.5
     2      28.0  38.2  59.0  37.8  53.0  38.3
```