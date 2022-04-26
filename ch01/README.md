# IPython: Pythonより優れたPython

Pythonを用いた開発環境にはいくつもの選択肢があり、この著者はIPythonとテキストエディタ（Emacs か Atom）を好んで使う。
IPythonは、Interactive Pythonの略で、Pythonの拡張された対話型シェル。

## シェルかnotebookか

本書では、IPythonの使い方として2種類の方法を紹介する。

- IPythonシェル
- IPython notebook

## IPythonシェルの起動

コマンドラインでipythonコマンドを実行する。

```bash
root@91eabcea26ce:~/src# ipython
Python 3.9.12 (main, Apr 20 2022, 18:47:18) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.2.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: 
```

## Jupyter notebookの起動

Jupyter notebookは、コードを実行するだけでなく下記も表示できる。

- 整形されたテキスト
- 動的または静的な画像やグラフ
- 数式
- JavaScriptウィジェット

```bash
jupyter notebook
```

## IPythonのヘルプとドキュメント

ウェブ検索を使わなくても、IPythonだけで多くの情報を検索することができる。

- この関数をどうやって呼び出すか
  - 引数やオプション
- このPythonオブジェクトのソースコードはどのように構造になっているか
- このパッケージからインポートできるのは何か

## ?文字で関数の使い方を表示する

すべてのPythonオブジェクトはdocstringと呼ばれる文字列を持つ。
docstringには、たいていオブジェクトの要約と使い方が書かれている。
helpという組み込みの関数で、docstringの情報を表示できる。
柿はlenという組み込み関数のdocstringを表示する例。

```bash
In [5]: help(len)
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.
```

IPythonでは、ドキュメントにアクセスするための簡易表現として?を使える。

```bash
In [6]: len?
Signature: len(obj, /)
Docstring: Return the number of items in a container.
Type:      builtin_function_or_method
```

以下のように、オブジェクトのメソッドに対しても使用できる。

```bash
In [7]: l = [1,2,3]

In [8]: l.insert?
Signature: l.insert(index, object, /)
Docstring: Insert object before index.
Type:      builtin_function_or_method
```

また、オブジェクト自身に対して使用すれば、型の情報が得られる。

```bash
In [10]: l = [1,2,3]

In [11]: l?
Type:        list
String form: [1, 2, 3]
Length:      3
Docstring:  
Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.
```

自分で定義した関数に対しても使用できる。

```bash
In [12]: def square(a):
    ...:     """Return the square of a."""
    ...:     return a ** 2
    ...: 

In [13]: square?
Signature: square(a)
Docstring: Return the square of a.
File:      ~/src/<ipython-input-12-c96e82bfafc5>
Type:      function
```

## ??文字でソースコードを表示する

関数名の後ろに??をつけてコマンドラインで実行するとソースコードが表示される。

```bash
In [14]: square??
Signature: square(a)
Source:   
def square(a):
    """Return the square of a."""
    return a ** 2
File:      ~/src/<ipython-input-12-c96e82bfafc5>
Type:      function
```

??をつけてもソースコードが表示されないこともあるが、それは対象オブジェクトがC言語などPython以外で実装されていることが原因。
その場合、??の結果は?と同じになる。

## Tab保管を使った属性名やモジュールの検索

オブジェクトに対して適用可能な属性のリストを表示するには、オブジェクト名にピリオドをつけてからTabキーを入力する。

```bash
In [16]: l.<TAB>
            append()  count()   insert()  reverse()
            clear()   extend()  pop()     sort()   
            copy()    index()   remove()
```

属性名を途中まで入力してリストを絞り込むこともできる。

```bash
In [17]: l.c<TAB>
             clear() count()
             copy()
```

このTab保管は、パッケージからオブジェクトをインポートする際にも使える。
以下は、itertoolsからインポート可能なcoで始まるオブジェクトを表示する。

```bash
In [17]: from itertools import co<TAB>
                                  combinations()                compress                     
                                  combinations_with_replacement count
```

使用可能なインポートの確認。

```bash
In [17]: import
                  abc                                    argon2                                 asttokens                              atexit                                 babel                                  binascii                               bs4                                    certifi                                charset_normalizer                     code                                   colorsys                               contextlib                             cProfile                               curses                                  
~~ 略 ~~
```

## ワイルドカードマッチング

*文字でワイルドカードマッチングすることもできる。
以下は、名前空間にあるWarningで終わるすべてのオブジェクトを表示する。

```bash
In [17]: *Warning?
BytesWarning
DeprecationWarning
FutureWarning
ImportWarning
PendingDeprecationWarning
ResourceWarning
RuntimeWarning
SyntaxWarning
UnicodeWarning
UserWarning
Warning
```

また、名前のどこかにfindを含む文字列メソッドを検索することもできる。

```bash
In [18]: str.*find*?
str.find
str.rfind
```

## IPython Magicコマンド

IPython Magicコマンドとは、IPythonが追加した拡張のこと。
プロファイリングに使えるコマンドは後述。

## InオブジェクトとOutオブジェクト

IPythonでは、入出力の度にIn、Out変数を作成し、参照できるようになっている。

```bash
In [1]: import math

In [2]: math.sin(2)
Out[2]: 0.9092974268256817

In [3]: math.cos(2)
Out[3]: -0.4161468365471424
```

上記のような実行履歴があるとき、たとえば最初の入力は次のように参照できる。

```bash
In [4]: print(In[1])
import math
```

そのほか、_で過去の出力をサン法するショートカットもある。

## エラーとデバッグ

Pythonでもエラーが起こると例外が発生する。
エラー原因に関する情報は、Python内からアクセスできるトレースバックに残る。
Magicコマンドの%xmodeを使って、例外発生時に表示される情報の量を制御することができる。

デフォルトの情報量は下記。

```bash
In [6]: def func1(a, b):
   ...:     return a / b
   ...: 
   ...: 
   ...: def func2(x):
   ...:     a = x
   ...:     b = x - 1
   ...:     return func1(a, b)
   ...: 

In [7]: func2(1)
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
Input In [7], in <cell line: 1>()
----> 1 func2(1)

Input In [6], in func2(x)
      6 a = x
      7 b = x - 1
----> 8 return func1(a, b)

Input In [6], in func1(a, b)
      1 def func1(a, b):
----> 2     return a / b

ZeroDivisionError: division by zero
```

Verboseモードに変更すると、関数に渡された引数の情報も表示される。

```bash
In [12]: %xmode Verbose
Exception reporting mode: Verbose

In [13]: func2(1)
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
Input In [13], in <cell line: 1>()
----> 1 func2(1)

Input In [6], in func2(x=1)
      6 a = x
      7 b = x - 1
----> 8 return func1(a, b)
        a = 1
        b = 0

Input In [6], in func1(a=1, b=0)
      1 def func1(a, b):
----> 2     return a / b
        a = 1
        b = 0

ZeroDivisionError: division by zero
```

pdbは、Pythonの対話的なデバッグのための標準ツール。
pdbをIPython向けに拡張したものをipdbという。

本書では%debugコマンドの使い方を紹介している。

```bash
In [14]: %debug
> <ipython-input-6-962b301c8a52>(2)func1()
      1 def func1(a, b):
----> 2     return a / b
      3 
      4 
      5 def func2(x):

ipdb> print(a)
1
ipdb> print(b)
0
```

スタック内を上下に移動するときはup/downを使う。

```bash
ipdb> up
> <ipython-input-6-962b301c8a52>(8)func2()
      4 
      5 def func2(x):
      6     a = x
      7     b = x - 1
----> 8     return func1(a, b)

ipdb> print(a)
1
ipdb> print(x)
1
```

%pdbコマンドで、例外発生時に自動的にデバッガを起動するように設定もできる。

```bash
In [15]: %xmode Plain
Exception reporting mode: Plain

In [16]: %pdb on
Automatic pdb calling has been turned ON

In [17]: func2(1)
Traceback (most recent call last):
  Input In [17] in <cell line: 1>
    func2(1)
  Input In [6] in func2
    return func1(a, b)
  Input In [6] in func1
    return a / b
ZeroDivisionError: division by zero

> <ipython-input-6-962b301c8a52>(2)func1()
      1 def func1(a, b):
----> 2     return a / b
      3 
      4 
      5 def func2(x):
```

デバッグコマンド

- q(uit)
  - デバッガとプログラムの実行を終了する
- c(ontinue)
  - デバッガを修了し、プログラムの実行を継続する
- n(ext)
  - プログラムの次のステップへ移動する
- <enter>
  - 直前のコマンドを繰り返して実行する
- p(rint)
  - 変数の値を表示する

## コードのプロファイリングと実行時間計測

IPythonには、コードの実行時間の確認とプロファイリングのための機能が備わっている。

- %time
  - 実行時間を測定する
- %timeit
  - 複数回実行して、より正確な実行時間を測定する
- %prun
  - プロファイラと共に実行する
- %lprun
  - 行プロファイラと共に実行する
- %memit
  - 使用したメモリを測定する
- %mprun
  - 行メモリプロファイラを使って使用したメモリを測定する

実行時間の測定の例。

```bash
In [6]: %time print('test')
test
CPU times: user 0 ns, sys: 134 µs, total: 134 µs
Wall time: 141 µs
```

プロファイラと共に実行する例。

```bash
In [5]: %prun print('test')
test
         4 function calls in 0.000 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```
