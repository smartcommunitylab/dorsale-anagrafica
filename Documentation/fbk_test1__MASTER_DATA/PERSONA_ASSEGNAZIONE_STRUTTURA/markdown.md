# PERSONA_ASSEGNAZIONE_STRUTTURA

## Info tabella

| Info                     | Descrizione                                                                                                                                                                       |
|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nome tabella Dremio      | PERSONA_ASSEGNAZIONE_STRUTTURA                                                                                                                                                    |
| Space Dremio             | fbk_test1__MASTER_DATA                                                                                                                                                            |
| Nome completo            | fbk_test1__MASTER_DATA.PERSONA_ASSEGNAZIONE_STRUTTURA                                                                                                                             |
| Descrizione tabella      |                                                                                                                                                                                   |
| Versione                 | 1.0                                                                                                                                                                               |
| Core dataset             | False                                                                                                                                                                             |
| Dataset di origine       |                                                                                                                                                                                   |
| Richiede validazione     | True                                                                                                                                                                              |
| Esposta in DSS           | False                                                                                                                                                                             |
| Endpoint DSS             |                                                                                                                                                                                   |
| Query name DSS           |                                                                                                                                                                                   |
| Formato esposizione      |                                                                                                                                                                                   |
| Tipologia autenticazione |                                                                                                                                                                                   |
| Tabelle genitrici        | [fbk_test1__MASTER_DATA.PERSONA_ASSEGNAZIONE_STRUTTURA_RCE](/Documentation/fbk_test1__MASTER_DATA/PERSONA_ASSEGNAZIONE_STRUTTURA_RCE/markdown.md)                                 |
|                          | [fbk_test1__MASTER_DATA.PERSONA_ASSEGNAZIONE_STRUTTURA_S1P](/Documentation/fbk_test1__MASTER_DATA/PERSONA_ASSEGNAZIONE_STRUTTURA_S1P/markdown.md)                                 |
|                          | [fbk_test1__MASTER_DATA.STRUTTURA_BASE](/Documentation/fbk_test1__MASTER_DATA/STRUTTURA_BASE/markdown.md)                                                                         |
|                          | [fbk_test1__MASTER_DATA.STRUTTURA_ULTIMA_STRUTTURA](/Documentation/fbk_test1__MASTER_DATA/STRUTTURA_ULTIMA_STRUTTURA/markdown.md)                                                 |
| Tabelle figlie           | [fbk_test1__MASTER_DATA.ASSET_PERSONE_ASSEGNAZIONE_LINEA](/Documentation/fbk_test1__MASTER_DATA/ASSET_PERSONE_ASSEGNAZIONE_LINEA/markdown.md)                                     |
|                          | [fbk_test1__MASTER_DATA.ASSET_PERSONE_ASSEGNAZIONE_TERMINALE](/Documentation/fbk_test1__MASTER_DATA/ASSET_PERSONE_ASSEGNAZIONE_TERMINALE/markdown.md)                             |
|                          | [fbk_test1__MASTER_DATA.PERSONA_ASSEGNAZIONE_STRUTTURA_ULTIMA_ASSEGNAZIONE](/Documentation/fbk_test1__MASTER_DATA/PERSONA_ASSEGNAZIONE_STRUTTURA_ULTIMA_ASSEGNAZIONE/markdown.md) |
|                          | [fbk_test1__VISUALIZATION_TABLES.PERSONA_ASSEGNAZIONE_STRUTTURA](/Documentation/fbk_test1__VISUALIZATION_TABLES/PERSONA_ASSEGNAZIONE_STRUTTURA/markdown.md)                       |

## Struttura relazionale

![PERSONA_ASSEGNAZIONE_STRUTTURA](./graph_png.png)

## Descrizione struttura tabella

| Campo                                    | Descrizione                              | Tipo    | Constraints   | Linked data   | errors   |
|:-----------------------------------------|:-----------------------------------------|:--------|:--------------|:--------------|:---------|
| codice_ente                              | Codice ente                              | integer | {}            |               | {}       |
| matricola                                | Matricola                                | integer | {}            |               | {}       |
| data_inizio_assegnazione_struttura       | Data inizio assegnazione struttura       | date    | {}            |               | {}       |
| data_fine_assegnazione_struttura         | Data fine assegnazione struttura         | date    | {}            |               | {}       |
| tipo_assegnazione_struttura              | Tipo assegnazione struttura              | string  | {}            |               | {}       |
| codice_struttura                         | Codice struttura                         | string  | {}            |               | {}       |
| data_inserimento_assegnazione_struttura  | Data inserimento assegnazione struttura  | date    | {}            |               | {}       |
| data_applicazione_assegnazione_struttura | Data applicazione assegnazione struttura | date    | {}            |               | {}       |
| matricola_estesa                         | Matricola estesa                         | string  | {}            |               | {}       |
| id_struttura                             | Id struttura                             | integer | {}            |               | {}       |
