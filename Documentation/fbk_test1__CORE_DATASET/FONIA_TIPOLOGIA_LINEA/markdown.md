# FONIA_TIPOLOGIA_LINEA

## Info tabella

| Info                     | Descrizione                                                                                                                                       |
|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|
| Nome tabella Dremio      | FONIA_TIPOLOGIA_LINEA                                                                                                                             |
| Space Dremio             | fbk_test1__CORE_DATASET                                                                                                                           |
| Nome completo            | fbk_test1__CORE_DATASET.FONIA_TIPOLOGIA_LINEA                                                                                                     |
| Descrizione tabella      |                                                                                                                                                   |
| Versione                 | 1.0                                                                                                                                               |
| Core dataset             | True                                                                                                                                              |
| Dataset di origine       | FONIA                                                                                                                                             |
| Richiede validazione     | True                                                                                                                                              |
| Esposta in DSS           | False                                                                                                                                             |
| Endpoint DSS             |                                                                                                                                                   |
| Query name DSS           |                                                                                                                                                   |
| Formato esposizione      |                                                                                                                                                   |
| Tipologia autenticazione |                                                                                                                                                   |
| Tabelle genitrici        |                                                                                                                                                   |
| Tabelle figlie           | [fbk_test1__MASTER_DATA.ASSET_PERSONE_ASSEGNAZIONE_LINEA](/Documentation/fbk_test1__MASTER_DATA/ASSET_PERSONE_ASSEGNAZIONE_LINEA/markdown.md)     |
|                          | [fbk_test1__MASTER_DATA.ASSET_STRUTTURE_ASSEGNAZIONE_LINEA](/Documentation/fbk_test1__MASTER_DATA/ASSET_STRUTTURE_ASSEGNAZIONE_LINEA/markdown.md) |

## Struttura relazionale

![FONIA_TIPOLOGIA_LINEA](./graph_png.png)

## Descrizione struttura tabella

| Campo                       | Descrizione                 | Tipo    | Constraints   | Linked data   | errors   |
|:----------------------------|:----------------------------|:--------|:--------------|:--------------|:---------|
| id                          | Id                          | integer | {}            |               | {}       |
| descrizione_tipologia_linea | Descrizione tipologia linea | string  | {}            |               | {}       |
