# ASSET_TOTALI_ASSEGNAZIONE_LINEA

## Info tabella

| Info                     | Descrizione                                                                                                                                       |
|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|
| Nome tabella Dremio      | ASSET_TOTALI_ASSEGNAZIONE_LINEA                                                                                                                   |
| Space Dremio             | fbk_test1__MASTER_DATA                                                                                                                            |
| Nome completo            | fbk_test1__MASTER_DATA.ASSET_TOTALI_ASSEGNAZIONE_LINEA                                                                                            |
| Descrizione tabella      |                                                                                                                                                   |
| Versione                 | 1.0                                                                                                                                               |
| Core dataset             | False                                                                                                                                             |
| Dataset di origine       |                                                                                                                                                   |
| Richiede validazione     | True                                                                                                                                              |
| Esposta in DSS           | False                                                                                                                                             |
| Endpoint DSS             |                                                                                                                                                   |
| Query name DSS           |                                                                                                                                                   |
| Formato esposizione      |                                                                                                                                                   |
| Tipologia autenticazione |                                                                                                                                                   |
| Tabelle genitrici        | [fbk_test1__MASTER_DATA.ASSET_PERSONE_ASSEGNAZIONE_LINEA](/Documentation/fbk_test1__MASTER_DATA/ASSET_PERSONE_ASSEGNAZIONE_LINEA/markdown.md)     |
|                          | [fbk_test1__MASTER_DATA.ASSET_STRUTTURE_ASSEGNAZIONE_LINEA](/Documentation/fbk_test1__MASTER_DATA/ASSET_STRUTTURE_ASSEGNAZIONE_LINEA/markdown.md) |
| Tabelle figlie           |                                                                                                                                                   |

## Struttura relazionale

![ASSET_TOTALI_ASSEGNAZIONE_LINEA](./graph_png.png)

## Descrizione struttura tabella

| Campo                          | Descrizione                    | Tipo    | Constraints   | Linked data   | errors   |
|:-------------------------------|:-------------------------------|:--------|:--------------|:--------------|:---------|
| id_assegnazione_linea          | Id assegnazione linea          | integer | {}            |               | {}       |
| data_inizio_assegnazione_linea | Data inizio assegnazione linea | date    | {}            |               | {}       |
| data_fine_assegnazione_linea   | Data fine assegnazione linea   | date    | {}            |               | {}       |
| linea_is_personale             | Linea is personale             | integer | {}            |               | {}       |
| causale_ritiro                 | Causale ritiro                 | string  | {}            |               | {}       |
| codice_struttura_fonia         | Codice struttura fonia         | string  | {}            |               | {}       |
| matricola                      | Matricola                      | integer | {}            |               | {}       |
| matricola_estesa               | Matricola estesa               | string  | {}            |               | {}       |
| codice_fiscale                 | Codice fiscale                 | string  | {}            |               | {}       |
| descrizione_gruppo             | Descrizione gruppo             | string  | {}            |               | {}       |
| descrizione_tipologia_linea    | Descrizione tipologia linea    | string  | {}            |               | {}       |
| id_struttura                   | Id struttura                   | integer | {}            |               | {}       |
| linea_id                       | Linea id                       | integer | {}            |               | {}       |
