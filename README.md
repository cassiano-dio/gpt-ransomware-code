# ChatGPT Ransomware Code

## Descrição

Este código contém um exemplo teório de um código de ransomware, que serve para encriptar arquivos em um computador (use com cuidado).

Obs: um ransomware vai muito além do código em si, mas o funcionamento básico é de encriptar arquivos.

* **`encrypt.py`**: encripta um arquivo (neste caso é o arquivo `example.txt` e está definido no código)
* **`decrypt.py`**: desencripta um arquivo (o mesmo arquivo encriptado `example.txt`. Também está definido no código)
* **`example.txt`**: arquivo a ser encriptado

## Como usar este exemplo

* Instalar o **pyton3** na sua máquina
* Instalar as bibliotecas **cryptography** e **fernet** através do comando `pip install fernet` e `pip install cryptography`
* Executar o comando python ` .\encrypt.py` para encriptar o arquivo, informe a senha de encriptação (que será usada na decriptação). Note que irá criar dois arquivos, o `encryption_key.key` e `salt.bin` que serão necessários para desencriptar o arquivo encriptado, além de gerar um arquivo chamado `example.txt.enc` que é o arquivo `example.txt` encriptado.
* Para desencriptar, utilize o comando `python .\decrypt.py` e informe a senha criada para encriptar. Repare que o arquivo encriptado será substituído pelo arquivo legível.
