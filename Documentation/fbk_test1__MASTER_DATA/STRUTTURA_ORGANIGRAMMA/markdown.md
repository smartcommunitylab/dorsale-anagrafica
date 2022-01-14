# STRUTTURA_ORGANIGRAMMA

## Info tabella

| Info                     | Descrizione                                                                                                                   |
|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------|
| Nome tabella Dremio      | STRUTTURA_ORGANIGRAMMA                                                                                                        |
| Space Dremio             | fbk_test1__MASTER_DATA                                                                                                        |
| Nome completo            | fbk_test1__MASTER_DATA.STRUTTURA_ORGANIGRAMMA                                                                                 |
| Descrizione tabella      |                                                                                                                               |
| Versione                 | 1.0                                                                                                                           |
| Core dataset             | False                                                                                                                         |
| Dataset di origine       |                                                                                                                               |
| Richiede validazione     | False                                                                                                                         |
| Esposta in DSS           | False                                                                                                                         |
| Endpoint DSS             |                                                                                                                               |
| Query name DSS           |                                                                                                                               |
| Formato esposizione      |                                                                                                                               |
| Tipologia autenticazione |                                                                                                                               |
| Tabelle genitrici        | [fbk_test1__CORE_DATASET.S1P_GERARCHIA](/fbk_test1__CORE_DATASET/S1P_GERARCHIA/markdown.md)                                   |
|                          | [fbk_test1__MASTER_DATA.STRUTTURA_BASE](/fbk_test1__MASTER_DATA/STRUTTURA_BASE/markdown.md)                                   |
| Tabelle figlie           | [fbk_test1__VISUALIZATION_TABLES.STRUTTURA_ORGANIGRAMMA](/fbk_test1__VISUALIZATION_TABLES/STRUTTURA_ORGANIGRAMMA/markdown.md) |

## Struttura relazionale

![STRUTTURA_ORGANIGRAMMA](./graph_png.png)

## Descrizione struttura tabella

| Campo                           | Descrizione                     | Tipo    | Constraints   | Linked data   | errors   |
|:--------------------------------|:--------------------------------|:--------|:--------------|:--------------|:---------|
| codice_struttura                | Codice struttura                | string  | {}            |               | {}       |
| codice_struttura_superiore      | Codice struttura superiore      | string  | {}            |               | {}       |
| tipo_struttura_superiore        | Tipo struttura superiore        | string  | {}            |               | {}       |
| descrizione_struttura_superiore | Descrizione struttura superiore | string  | {}            |               | {}       |
| livello_struttura_superiore     | Livello struttura superiore     | integer | {}            |               | {}       |
| data_inizio_struttura_calcolata | Data inizio struttura calcolata | date    | {}            |               | {}       |
| data_fine_struttura_calcolata   | Data fine struttura calcolata   | date    | {}            |               | {}       |
| id_struttura                    | Id struttura                    | integer | {}            |               | {}       |
