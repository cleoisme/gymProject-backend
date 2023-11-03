# Assignment 3 - 2023-10-30

## Tasks

- [ ] Database migration
  - and how to use MongoDB instead, try both for learning purposes
  - 分析一下 admin 这部分的复杂性，考虑一部分用 SQL，另一部分用 non-SQL
- [ ] Understand the Django built-in Admin system
- [ ] Fix the integration errors once all current PRs merged in
- [ ] Pytest initialization to test each i/o
  - "verify" in javascript: 应对较为复杂的逻辑链条
  - “exception”: retryable, non-retryable, and validation.
  - “assertion”
- [ ] Add steps to django.yml to fully mimic the local dependencies
  - 原因分析：Github Action 给出的默认 django.yml 是在 Ubantu 上运行的，Ubantu 系统默认存在运行的 python 版本可能不支持最新的 Django 版本
    - 比如 ios 上默认是 python2，如果不另外安装其他版本的 python，则 python3 的 features 都无法使用
  - 注意配置路径这一步，确定当程序开始跑的时候调用的是预期的 interpertor
  - 在本地和 remote 版本出现冲突时候，一般改本地使之和 remote 相同,通过在 django.ymal 上加更多的 steps 来匹配本地的 dependencies 版本
- [ ] 改 ticket on the project overview

## Notes

- 当开始一个新 feature 或者项目，一般以 object 为导向慢慢加功能
- python interpetor

  - python 是别的语言写的，所以需要一个 interpretor 把这个高级语言翻译成低 level 的机器语言
  - pip 是 python 写的所以需要先装 python 再装 pip

- built-in Object Relational Mapping only compatible to sql database, and you will need to write a ORM-alike system to connect to MongoDB
- SQL and non-SQL
  - see the 2023-10-29-SqlVsNosql.md
