# S1P_ASSEGNAZIONE_ORARIO

## Info tabella

| Info                     | Descrizione                                                                                                           |
|:-------------------------|:----------------------------------------------------------------------------------------------------------------------|
| Nome tabella Dremio      | S1P_ASSEGNAZIONE_ORARIO                                                                                               |
| Space Dremio             | fbk_test1__CORE_DATASET                                                                                               |
| Nome completo            | fbk_test1__CORE_DATASET.S1P_ASSEGNAZIONE_ORARIO                                                                       |
| Descrizione tabella      |                                                                                                                       |
| Versione                 | 1.0                                                                                                                   |
| Core dataset             | True                                                                                                                  |
| Dataset di origine       | S1P                                                                                                                   |
| Richiede validazione     | True                                                                                                                  |
| Esposta in DSS           | False                                                                                                                 |
| Endpoint DSS             |                                                                                                                       |
| Query name DSS           |                                                                                                                       |
| Formato esposizione      |                                                                                                                       |
| Tipologia autenticazione |                                                                                                                       |
| Tabelle genitrici        |                                                                                                                       |
| Tabelle figlie           | [fbk_test1__MASTER_DATA.PERSONA_ASSEGNAZIONE_ORARIO](/fbk_test1__MASTER_DATA/PERSONA_ASSEGNAZIONE_ORARIO/markdown.md) |

## Struttura relazionale

![S1P_ASSEGNAZIONE_ORARIO](./graph_png.png)

## Descrizione struttura tabella

| Campo                                 | Descrizione                           | Tipo    | Constraints   | Linked data   | errors   |
|:--------------------------------------|:--------------------------------------|:--------|:--------------|:--------------|:---------|
| codice_ente                           | Codice ente                           | integer | {}            |               | {}       |
| matricola                             | Matricola                             | integer | {}            |               | {}       |
| data_inizio_assegnazione_orario       | Data inizio assegnazione orario       | date    | {}            |               | {}       |
| data_fine_assegnazione_orario         | Data fine assegnazione orario         | date    | {}            |               | {}       |
| tipo_assegnazione_orario              | Tipo assegnazione orario              | string  | {}            |               | {}       |
| codice_orario                         | Codice orario                         | integer | {}            |               | {}       |
| data_inserimento_assegnazione_orario  | Data inserimento assegnazione orario  | date    | {}            |               | {}       |
| data_applicazione_assegnazione_orario | Data applicazione assegnazione orario | date    | {}            |               | {}       |
