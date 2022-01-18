# ASSET_STRUTTURE_ASSEGNAZIONE_LINEA

## Info tabella

| Info                     | Descrizione                                                                                                                                       |
|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|
| Nome tabella Dremio      | ASSET_STRUTTURE_ASSEGNAZIONE_LINEA                                                                                                                |
| Space Dremio             | fbk_test1__VISUALIZATION_TABLES                                                                                                                   |
| Nome completo            | fbk_test1__VISUALIZATION_TABLES.ASSET_STRUTTURE_ASSEGNAZIONE_LINEA                                                                                |
| Descrizione tabella      |                                                                                                                                                   |
| Versione                 | 1.0                                                                                                                                               |
| Core dataset             | False                                                                                                                                             |
| Dataset di origine       |                                                                                                                                                   |
| Richiede validazione     | False                                                                                                                                             |
| Esposta in DSS           | True                                                                                                                                              |
| Endpoint DSS             | /asset-strutture-assegnazione-linea                                                                                                               |
| Query name DSS           | asset_strutture_assegnazione_linea                                                                                                                |
| Formato esposizione      | JSON                                                                                                                                              |
| Tipologia autenticazione | Bearer token                                                                                                                                      |
| Tabelle genitrici        | [fbk_test1__MASTER_DATA.ASSET_STRUTTURE_ASSEGNAZIONE_LINEA](/Documentation/fbk_test1__MASTER_DATA/ASSET_STRUTTURE_ASSEGNAZIONE_LINEA/markdown.md) |
| Tabelle figlie           |                                                                                                                                                   |

## Struttura relazionale

![ASSET_STRUTTURE_ASSEGNAZIONE_LINEA](./graph_png.png)

## Descrizione struttura tabella

| Campo                          | Descrizione                    | Tipo     | Constraints   | Linked data   | errors   |
|:-------------------------------|:-------------------------------|:---------|:--------------|:--------------|:---------|
| id_assegnazione_linea          | Id assegnazione linea          | integer  | {}            |               | {}       |
| data_inizio_assegnazione_linea | Data inizio assegnazione linea | datetime | {}            |               | {}       |
| data_fine_assegnazione_linea   | Data fine assegnazione linea   | datetime | {}            |               | {}       |
| linea_is_personale             | Linea is personale             | integer  | {}            |               | {}       |
| causale_ritiro                 | Causale ritiro                 | string   | {}            |               | {}       |
| codice_struttura_fonia         | Codice struttura fonia         | string   | {}            |               | {}       |
| matricola                      | Matricola                      | integer  | {}            |               | {}       |
| matricola_estesa               | Matricola estesa               | string   | {}            |               | {}       |
| codice_fiscale                 | Codice fiscale                 | string   | {}            |               | {}       |
| descrizione_gruppo             | Descrizione gruppo             | string   | {}            |               | {}       |
| descrizione_tipologia_linea    | Descrizione tipologia linea    | string   | {}            |               | {}       |
| id_struttura                   | Id struttura                   | integer  | {}            |               | {}       |
| linea_id                       | Linea id                       | integer  | {}            |               | {}       |
