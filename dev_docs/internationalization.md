# 国際化の手順

## 本リポジトリの場合

1. 翻訳を記載するファイルの作成

   ```bash
   poetry shell
   ./tool.py update
   ```

2. 翻訳

   1 で生成されたファイルで

   ```po
   #: ../../source/index.rst:5
   msgid "興味のあること：数値計算など"
   msgstr ""
   ```

   のように記入欄が生成されるため、
   `msgid` の内容を `msgstr` に翻訳して記載する。

3. ビルド

   ```bash
   ./tool.py build -l en
   ```

## 上記の手順により行っていること

1. sphinx-intl Python パッケージのインストール

2. `conf.py` の設定追加

   ```python
   locale_dirs = ['locale/']
   gettext_compact = False
   ```

3. 翻訳するメッセージの取り出し

   ```bash
   make gettext
   ```

4. 翻訳を記載するファイルの作成

   ```bash
   cd <本リポジトリのルートディレクトリ>
   poetry shell
   cd source
   sphinx-intl update -p ../build/gettext/ -l en
   ```

5. 翻訳

   4 で生成されたファイルで

   ```po
   #: ../../source/index.rst:5
   msgid "興味のあること：数値計算など"
   msgstr ""
   ```

   のように記入欄が生成されるため、
   `msgid` の内容を `msgstr` に翻訳して記載する。

6. 出力

   出力時に `sphinx-build` コマンドに `-D language='en'` オプションを追加するなどして、
   出力したい言語を選択する。
   ただし、`sphinx-build` コマンドに `-M` オプションでビルド対象の種別を指定しなければ正常に動作しない。
