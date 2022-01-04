# Krypto trader

Program, jenž na základě RSI nakupuje/prodává pozice v rámci libovolně zvolené kryptoměny

Před spuštěním:

1. vygenerovat si vlastní API_KEYS
2. naistahovat knihovny, co nemáte
3. stáhnout wheel od TA-Lib, odkaz a command v my_functions.py
4. nainstalovat python-dotenv-> schová api klíče proti pushnutí do githubu ->enviroment variable

Obsluha:

- v config #INPUT si zadáte parametry dle své potřeby
- vytvoříte si vlastní .env kam dáte API_KEY a SECRET_KEY

Nápady do budoucna:

- více strategií
- více burz+převody mezi nimi
- více měn zaráz
- UI

## TODO

- Lépe definovat kroky potřebné kzprovoznění traderu především část spojenou s technical analysis library (TA-Lib).
