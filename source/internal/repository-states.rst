リポジトリの状況
====================

放置しているものも含めてリポジトリごとの状況を確認する。

.. jinja:: internal_repositories

    .. list-table::
        :header-rows: 1

        - - リポジトリ
          - 主な言語
          - 最終更新
          - 自動 CI
          - ブランチ
          - CI 結果
          - Coverage

        {% for repository in repositories|sort(attribute="name") %}

        - - `{{repository.name}} <https://gitlab.com/{{repository.gitlab_path}}>`_
          - {{repository.main_languages}}
          - .. image:: https://img.shields.io/gitlab/last-commit/{{repository.gitlab_path}}?label=
          - {{repository.ci_schedule}}
          - {{repository.default_branch}}
          - .. image:: https://img.shields.io/gitlab/pipeline-status/{{repository.gitlab_path}}?branch={{repository.default_branch}}&label=
          - .. image:: https://img.shields.io/gitlab/pipeline-coverage/{{repository.gitlab_path}}?branch={{repository.default_branch}}&label=

        {% endfor %}
