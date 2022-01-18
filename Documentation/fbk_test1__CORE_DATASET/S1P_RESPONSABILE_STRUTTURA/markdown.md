# S1P_RESPONSABILE_STRUTTURA

## Info tabella

| Info                     | Descrizione                                                                                                                                                             |
|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nome tabella Dremio      | S1P_RESPONSABILE_STRUTTURA                                                                                                                                              |
| Space Dremio             | fbk_test1__CORE_DATASET                                                                                                                                                 |
| Nome completo            | fbk_test1__CORE_DATASET.S1P_RESPONSABILE_STRUTTURA                                                                                                                      |
| Descrizione tabella      |                                                                                                                                                                         |
| Versione                 | 1.0                                                                                                                                                                     |
| Core dataset             | True                                                                                                                                                                    |
| Dataset di origine       | S1P                                                                                                                                                                     |
| Richiede validazione     | True                                                                                                                                                                    |
| Esposta in DSS           | False                                                                                                                                                                   |
| Endpoint DSS             |                                                                                                                                                                         |
| Query name DSS           |                                                                                                                                                                         |
| Formato esposizione      |                                                                                                                                                                         |
| Tipologia autenticazione |                                                                                                                                                                         |
| Tabelle genitrici        |                                                                                                                                                                         |
| Tabelle figlie           | [fbk_test1__MASTER_DATA.STRUTTURA_RESPONSABILE_ASSEGNAZIONE_STRUTTURA](/Documentation/fbk_test1__MASTER_DATA/STRUTTURA_RESPONSABILE_ASSEGNAZIONE_STRUTTURA/markdown.md) |

## Struttura relazionale

![S1P_RESPONSABILE_STRUTTURA](./graph_png.png)

## Descrizione struttura tabella

| Campo                    | Descrizione              | Tipo    | Constraints   | Linked data   | errors   |
|:-------------------------|:-------------------------|:--------|:--------------|:--------------|:---------|
| codice_struttura         | Codice struttura         | string  | {}            |               | {}       |
| codice_ente              | Codice ente              | integer | {}            |               | {}       |
| matricola                | Matricola                | integer | {}            |               | {}       |
| incarico_funzionale      | Incarico funzionale      | string  | {}            |               | {}       |
| data_inizio_responsabile | Data inizio responsabile | date    | {}            |               | {}       |
| data_fine_responsabile   | Data fine responsabile   | date    | {}            |               | {}       |
