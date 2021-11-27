# apitrii

### Elección de linters
Analizando la situación que no todos los programadores no usamos el mismo ide, como que algunos tal vez no usan un ide vamos a dar las distintas alternativas que existen para los distintos ide y a continuación vamos a mostrar la solución propuesta para unificar dicho suceso.

#### visualstudio Code:
Puede implementar esa solución, comparto una, guia en el siguiente enlace: https://code.visualstudio.com/docs/python/linting

#### pycharm:

Puede implementar esa solución, comparto una, guia en el siguiente enlace https://pavelkarateev.com/posts/2017/08/13/linters/

#### otros:
 Bueno cuando llegamos a este punto,se vio dos posiblidades:
 1) Ejecutar cada uno de los linters por shell
 2) Hacer un Hook, para los que quieren conocer más les comparto este enlace https://www.hostinger.com.ar/tutoriales/como-usar-git-hooks
 
### Solución Elegida:
1) Armar un hook que se ejecute en el pre-commit, en el cual ejecutamos todos los linters
repos:
```
  - repo: https://gitlab.com/pycqa/flake8
    rev: 3.8.3
    hooks:
      - id: flake8
  - repo: https://github.com/pycqa/isort
    rev: 5.10.1
    hooks:
      - id: isort
        name: isort (python)
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: ''
    hooks:
      - id: mypy
  - repo: https://github.com/ambv/black
    rev: 20.8b1
    hooks:
      - id: black
        language_version: python3.9
        
   ```
    
2) Definimos otro lints en él una acción de github, en el caso que de alguna manera haya llegado sin el formato 
y si las reglas que definimos este se encarga de aplicar los lintrs
```
    - uses: actions/checkout@v2
    - uses: ricardochaves/python-lint@v1.4.0
      with:
        python-root-list: 'app'
        use-pylint: false
        use-pycodestyle: true
        use-flake8: true
        use-black: true
        use-mypy: false
        use-isort: true
        extra-mypy-options: "--ignore-missing-imports"
 ```
 
 #### HAPPY CODE!!!
