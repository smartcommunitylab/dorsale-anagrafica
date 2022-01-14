# FONIA_DESTINATARIO_SPEDIZIONE

## Info tabella

| Info                     | Descrizione                                           |
|:-------------------------|:------------------------------------------------------|
| Nome tabella Dremio      | FONIA_DESTINATARIO_SPEDIZIONE                         |
| Space Dremio             | fbk_test1__CORE_DATASET                               |
| Nome completo            | fbk_test1__CORE_DATASET.FONIA_DESTINATARIO_SPEDIZIONE |
| Descrizione tabella      |                                                       |
| Versione                 | 1.0                                                   |
| Core dataset             | True                                                  |
| Dataset di origine       | FONIA                                                 |
| Richiede validazione     | True                                                  |
| Esposta in DSS           | False                                                 |
| Endpoint DSS             |                                                       |
| Query name DSS           |                                                       |
| Formato esposizione      |                                                       |
| Tipologia autenticazione |                                                       |
| Tabelle genitrici        |                                                       |
| Tabelle figlie           |                                                       |

## Struttura relazionale

![FONIA_DESTINATARIO_SPEDIZIONE](./graph_png.png)

## Descrizione struttura tabella

| Campo       | Descrizione   | Tipo    | Constraints   | Linked data   | errors   |
|:------------|:--------------|:--------|:--------------|:--------------|:---------|
| id          | Id            | integer | {}            |               | {}       |
| descrizione | Descrizione   | string  | {}            |               | {}       |
| cap         | Cap           | string  | {}            |               | {}       |
| citta       | Citta         | string  | {}            |               | {}       |
| provincia   | Provincia     | string  | {}            |               | {}       |
| via         | Via           | string  | {}            |               | {}       |
