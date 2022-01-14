# PERSONA_ANAGRAFICA

## Info tabella

| Info                     | Descrizione                                                                                                           |
|:-------------------------|:----------------------------------------------------------------------------------------------------------------------|
| Nome tabella Dremio      | PERSONA_ANAGRAFICA                                                                                                    |
| Space Dremio             | fbk_test1__MASTER_DATA                                                                                                |
| Nome completo            | fbk_test1__MASTER_DATA.PERSONA_ANAGRAFICA                                                                             |
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
| Tabelle genitrici        | [fbk_test1__MASTER_DATA.PERSONA_ANAGRAFICA_FONIA](/fbk_test1__MASTER_DATA/PERSONA_ANAGRAFICA_FONIA/markdown.md)       |
|                          | [fbk_test1__MASTER_DATA.PERSONA_ANAGRAFICA_RCE](/fbk_test1__MASTER_DATA/PERSONA_ANAGRAFICA_RCE/markdown.md)           |
|                          | [fbk_test1__MASTER_DATA.PERSONA_ANAGRAFICA_S1P](/fbk_test1__MASTER_DATA/PERSONA_ANAGRAFICA_S1P/markdown.md)           |
| Tabelle figlie           | [fbk_test1__VISUALIZATION_TABLES.PERSONA_ANAGRAFICA](/fbk_test1__VISUALIZATION_TABLES/PERSONA_ANAGRAFICA/markdown.md) |

## Struttura relazionale

![PERSONA_ANAGRAFICA](./graph_png.png)

## Descrizione struttura tabella

| Campo            | Descrizione      | Tipo    | Constraints   | Linked data   | errors   |
|:-----------------|:-----------------|:--------|:--------------|:--------------|:---------|
| matricola_estesa | Matricola estesa | string  | {}            |               | {}       |
| matricola        | Matricola        | integer | {}            |               | {}       |
| cognome          | Cognome          | string  | {}            |               | {}       |
| nome             | Nome             | string  | {}            |               | {}       |
| data_nascita     | Data nascita     | date    | {}            |               | {}       |
| codice_fiscale   | Codice fiscale   | string  | {}            |               | {}       |
| sesso            | Sesso            | string  | {}            |               | {}       |
| codice_cittadino | Codice cittadino | integer | {}            |               | {}       |
| provenienza      | Provenienza      | string  | {}            |               | {}       |
| eta              | Eta              | integer | {}            |               | {}       |
| range_eta        | Range eta        | string  | {}            |               | {}       |
