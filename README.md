# python-keylogger
> Keylogger simples feito em python.

python-keylogger é um projeto simples e rápido montado com propósitos educacionais e científicos. De forma simplificada um keylogger registra todas as teclas pressionadas na máquina na qual está rodando, normalmente usado com propósitos maliciosos, __mas não é o caso deste aqui__, como dito anteriormente.

## Instalação

### OS X & Linux:

- Crie seu ambiente virtual.

```sh 
python3.9 virtualenv python-keylogger
```
*Substitua a versão do python pela qual estiver usando*

- Dentro do seu ambiente virtual instale as bibliotecas necessárias.
```sh
pip3 install pynput
```

- Clone o repositório.

```sh
git clone https://github.com/P-py/python-keylogger
```

- Agora é só usar, basta executar o arquivo python.

### Windows:

- Crie seu ambiente virtual.

```sh 
mkirtualenv python-keylogger
```

- Dentro do seu ambiente virtual instale as bibliotecas necessárias.
```sh
pip3 install pynput
```

- Clone o repositório.

```sh
git clone https://github.com/P-py/python-keylogger
```

- Agora é só usar, basta executar o arquivo python.


## Exemplo de uso

Alguns exemplos interessantes e úteis sobre como seu projeto pode ser utilizado. Adicione blocos de códigos e, se necessário, screenshots.

_Para mais exemplos, consulte a [Wiki][wiki]._ 

## Configuração para Desenvolvimento

Descreva como instalar todas as dependências para desenvolvimento e como rodar um test-suite automatizado de algum tipo. Se necessário, faça isso para múltiplas plataformas.

```sh
make install
npm test
```

## Histórico de lançamentos

* 0.2.1
    * MUDANÇA: Atualização de docs (código do módulo permanece inalterado)
* 0.2.0
    * MUDANÇA: Remove `setDefaultXYZ()`
    * ADD: Adiciona `init()`
* 0.1.1
    * CONSERTADO: Crash quando chama `baz()` (Obrigado @NomeDoContribuidorGeneroso!)
* 0.1.0
    * O primeiro lançamento adequado
    * MUDANÇA: Renomeia `foo()` para `bar()`
* 0.0.1
    * Trabalho em andamento

## Meta

Seu Nome – [@SeuNome](https://twitter.com/...) – SeuEmail@exemplo.com

Distribuído sob a licença XYZ. Veja `LICENSE` para mais informações.

[https://github.com/yourname/github-link](https://github.com/othonalberto/)

## Contributing

1. Faça o _fork_ do projeto (<https://github.com/yourname/yourproject/fork>)
2. Crie uma _branch_ para sua modificação (`git checkout -b feature/fooBar`)
3. Faça o _commit_ (`git commit -am 'Add some fooBar'`)
4. _Push_ (`git push origin feature/fooBar`)
5. Crie um novo _Pull Request_

[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/seunome/seuprojeto/wiki