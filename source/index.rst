MusicScience37
====================

Contents
-----------------

- :ref:`index_programming`

  - :ref:`index_programming_repositories`

- `English version of this page <https://www.musicscience37.com/en/>`_.

.. _index_programming:

プログラミング
-------------------

- 主な言語：C++, Python
- 興味のあること：数値計算など

.. _index_programming_repositories:

主なリポジトリ
....................

- 数値解析

  - `Numerical Analysis Note <https://gitlab.com/MusicScience37/numerical-analysis-note>`_
    : 数値解析で調査したことを書きまとめていくリポジトリ（LaTeX）
  - `numerical-collection-cpp <https://gitlab.com/MusicScience37/numerical-collection-cpp>`_
    : 数値解析のアルゴリズムを実装してためているリポジトリ（C++）

- C++ の開発をサポートするライブラリ

  - `cpp-stat-bench <https://gitlab.com/MusicScience37/cpp-stat-bench>`_
    : 統計情報に加えてグラフの作成まで行うベンチマークライブラリ（C++）
  - `cpp-hash-tables <https://gitlab.com/MusicScience37/cpp-hash-tables>`_
    : ハッシュテーブルの実装（C++）
  - `conan-extra-packages <https://gitlab.com/MusicScience37/conan-extra-packages>`_
    : Conan Center にない追加の Conan パッケージ（C++）
  - `clang-tidy-checker <https://gitlab.com/MusicScience37/clang-tidy-checker>`_
    : C++ のソースコードに対して
    `Clang-Tidy <https://clang.llvm.org/extra/clang-tidy/>`_
    によるチェックを行うツール（Python）

- Docker イメージ

  - `pipenv-docker <https://gitlab.com/MusicScience37/pipenv-docker>`_
    : Pipenv を使用するための Docker イメージ
  - `cloc-docker <https://gitlab.com/MusicScience37/cloc-docker>`_
    : cloc を使用するための Docker イメージ
  - `texlive-pipenv-docker <https://gitlab.com/MusicScience37/texlive-pipenv-docker>`_
    : TeXLive と Pipenv を使用するための Docker イメージ
  - `cpp-base-image-docker <https://gitlab.com/MusicScience37/cpp-base-image-docker>`_
    : C++ の Docker イメージのベースとして共通のものをインストールした Docker イメージ
  - `gcc-ci-docker <https://gitlab.com/MusicScience37/gcc-ci-docker>`_
    : GCC による C++ の CI のための Docker イメージ
  - `clang-ci-docker <https://gitlab.com/MusicScience37/clang-ci-docker>`_
    : Clang による C++ の CI のための Docker イメージ
  - `sphinx-doxygen-docker <https://gitlab.com/MusicScience37/sphinx-doxygen-docker>`_
    : Sphinx と Doxygen を使用するための Docker イメージ

- その他

  - `MusicScience37 <https://gitlab.com/MusicScience37/MusicScience37>`_
    : 本ページのリポジトリ（Sphinx）
  - `TIL <https://gitlab.com/MusicScience37/til>`_
    : 日々の学んだことを書き込んでいくページ（Sphinx）

.. toctree::
    :caption: Internal
    :maxdepth: 2
    :hidden:

    internal/ci-status
