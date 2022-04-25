# Pythonデータサイエンスハンドブックのメモ

## 目的

[Pythonではじめる機械学習――scikit-learnで学ぶ特徴量エンジニアリングと機械学習の基礎]（https://www.oreilly.co.jp/books/9784873117980/）を読んだ。
機械学習の代表的なアルゴリズムの原理は理解したが、PythonやNumPyの基本的な操作を知らないので、自分でモデルを構築する前に知っておきたい。
RDBMSやCSVのデータを散布図に表示したり、アルゴリズムの入力データとして渡せるようにしたい。

## 実行環境

DockerでPython3の実行環境を構築。
[Pythonではじめる機械学習――scikit-learnで学ぶ特徴量エンジニアリングと機械学習の基礎]（https://www.oreilly.co.jp/books/9784873117980/）で必須だったライブラリはインストール済み。
データの可視化もすると思うので、WebブラウザでPythonを記述・実行するためのJupyter Notebookもインストールした。

Jupyter Notebookの起動コマンドは以下。

```bash
docker-compose exec app jupyter notebook --allow-root --ip=0.0.0.0
```

コマンドを実行するとURLが表示されるので、それにアクセスする。

```bash
[C 06:18:53.952 NotebookApp] 
    
    To access the notebook, open this file in a browser:
        file:///root/.local/share/jupyter/runtime/nbserver-8-open.html
    Or copy and paste one of these URLs:
        http://91eabcea26ce:8888/?token=fac9ad381cee6d6c2b71686d46d78713e84ac224a1069249
     or http://127.0.0.1:8888/?token=fac9ad381cee6d6c2b71686d46d78713e84ac224a1069249
[I 06:19:02.535 NotebookApp] 302 GET /?token=fac9ad381cee6d6c2b71686d46d78713e84ac224a1069249 (172.19.0.1) 1.380000ms
```

