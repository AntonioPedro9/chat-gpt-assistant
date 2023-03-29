## Chat GPT Assistant

Aplicação Python que utiliza a API do Chat GPT para receber perguntas por meio de voz e respondê-las de forma falada.

**OBS:** Para sintetizar a voz das respostas esse projeto usa o português padrão do Windows 11, para usa-lo em outro SO serão necessárias adaptações.

## Como usar

Crie uma conta na Open AI adicione sua chave de API no arquivo `.env` com o nome `OPENAI_API_KEY`, depois abra o terminal dentro da pasta do projeto e execute os seguintes comandos:

```
$ pip install .
$ python src/main.py
```

A aplicação vai ouvir seu microfone e caso a palavra-chave "chuchu" esteja contida na frase você terá uma resposta falada, a palavra-chave pode ser alterada dentro do arquivo `main.py`.
