\babelflask>pybabel extract -F babel.cfg -o messages.pot .
\babelflask>pybabel init -i messages.pot -d translations -l zh_CN
\babelflask>pybabel compile -d translations
