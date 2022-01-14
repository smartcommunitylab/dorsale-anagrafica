# PERSONA_FORMAZIONE

## Info tabella

| Info                     | Descrizione                                                                                                           |
|:-------------------------|:----------------------------------------------------------------------------------------------------------------------|
| Nome tabella Dremio      | PERSONA_FORMAZIONE                                                                                                    |
| Space Dremio             | fbk_test1__MASTER_DATA                                                                                                |
| Nome completo            | fbk_test1__MASTER_DATA.PERSONA_FORMAZIONE                                                                             |
| Descrizione tabella      |                                                                                                                       |
| Versione                 | 1.0                                                                                                                   |
| Core dataset             | False                                                                                                                 |
| Dataset di origine       |                                                                                                                       |
| Richiede validazione     | False                                                                                                                 |
| Esposta in DSS           | False                                                                                                                 |
| Endpoint DSS             |                                                                                                                       |
| Query name DSS           |                                                                                                                       |
| Formato esposizione      |                                                                                                                       |
| Tipologia autenticazione |                                                                                                                       |
| Tabelle genitrici        | [fbk_test1__CORE_DATASET.S1P_FORMAZIONE](/fbk_test1__CORE_DATASET/S1P_FORMAZIONE/markdown.md)                         |
|                          | [fbk_test1__MASTER_DATA.MAPPING_ENTE](/fbk_test1__MASTER_DATA/MAPPING_ENTE/markdown.md)                               |
| Tabelle figlie           | [fbk_test1__VISUALIZATION_TABLES.PERSONA_FORMAZIONE](/fbk_test1__VISUALIZATION_TABLES/PERSONA_FORMAZIONE/markdown.md) |

## Struttura relazionale

![PERSONA_FORMAZIONE](./graph_png.png)

## Descrizione struttura tabella

| Campo                    | Descrizione              | Tipo    | Constraints   | Linked data   | errors   |
|:-------------------------|:-------------------------|:--------|:--------------|:--------------|:---------|
| codice_ente              | Codice ente              | integer | {}            |               | {}       |
| matricola                | Matricola                | integer | {}            |               | {}       |
| codice_corso             | Codice corso             | string  | {}            |               | {}       |
| descrizione_corso        | Descrizione corso        | string  | {}            |               | {}       |
| ambito_formativo         | Ambito formativo         | string  | {}            |               | {}       |
| quantita_ore_corso       | Quantita ore corso       | number  | {}            |               | {}       |
| data_inizio_formazione   | Data inizio formazione   | date    | {}            |               | {}       |
| data_fine_formazione     | Data fine formazione     | date    | {}            |               | {}       |
| numero_crediti_corso     | Numero crediti corso     | number  | {}            |               | {}       |
| tipologia_corso          | Tipologia corso          | string  | {}            |               | {}       |
| tipologia_partecipazione | Tipologia partecipazione | string  | {}            |               | {}       |
| matricola_estesa         | Matricola estesa         | string  | {}            |               | {}       |
