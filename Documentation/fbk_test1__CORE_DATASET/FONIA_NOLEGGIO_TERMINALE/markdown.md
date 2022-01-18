# FONIA_NOLEGGIO_TERMINALE

## Info tabella

| Info                     | Descrizione                                                                                                                                                               |
|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nome tabella Dremio      | FONIA_NOLEGGIO_TERMINALE                                                                                                                                                  |
| Space Dremio             | fbk_test1__CORE_DATASET                                                                                                                                                   |
| Nome completo            | fbk_test1__CORE_DATASET.FONIA_NOLEGGIO_TERMINALE                                                                                                                          |
| Descrizione tabella      |                                                                                                                                                                           |
| Versione                 | 1.0                                                                                                                                                                       |
| Core dataset             | True                                                                                                                                                                      |
| Dataset di origine       | FONIA                                                                                                                                                                     |
| Richiede validazione     | True                                                                                                                                                                      |
| Esposta in DSS           | False                                                                                                                                                                     |
| Endpoint DSS             |                                                                                                                                                                           |
| Query name DSS           |                                                                                                                                                                           |
| Formato esposizione      |                                                                                                                                                                           |
| Tipologia autenticazione |                                                                                                                                                                           |
| Tabelle genitrici        |                                                                                                                                                                           |
| Tabelle figlie           | [fbk_test1__MASTER_DATA.ASSET_PERSONE_ASSOCIAZIONE_TERMINALI_NOLEGGI](/Documentation/fbk_test1__MASTER_DATA/ASSET_PERSONE_ASSOCIAZIONE_TERMINALI_NOLEGGI/markdown.md)     |
|                          | [fbk_test1__MASTER_DATA.ASSET_STRUTTURE_ASSOCIAZIONE_TERMINALI_NOLEGGI](/Documentation/fbk_test1__MASTER_DATA/ASSET_STRUTTURE_ASSOCIAZIONE_TERMINALI_NOLEGGI/markdown.md) |

## Struttura relazionale

![FONIA_NOLEGGIO_TERMINALE](./graph_png.png)

## Descrizione struttura tabella

| Campo                     | Descrizione               | Tipo    | Constraints   | Linked data   | errors   |
|:--------------------------|:--------------------------|:--------|:--------------|:--------------|:---------|
| contratto_id              | Contratto id              | integer | {}            |               | {}       |
| modello_id                | Modello id                | integer | {}            |               | {}       |
| canone_noleggio_terminale | Canone noleggio terminale | number  | {}            |               | {}       |
| durata_noleggio_terminale | Durata noleggio terminale | integer | {}            |               | {}       |
