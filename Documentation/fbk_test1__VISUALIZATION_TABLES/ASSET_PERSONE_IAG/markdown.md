# ASSET_PERSONE_IAG

## Info tabella

| Info                     | Descrizione                                                                                                     |
|:-------------------------|:----------------------------------------------------------------------------------------------------------------|
| Nome tabella Dremio      | ASSET_PERSONE_IAG                                                                                               |
| Space Dremio             | fbk_test1__VISUALIZATION_TABLES                                                                                 |
| Nome completo            | fbk_test1__VISUALIZATION_TABLES.ASSET_PERSONE_IAG                                                               |
| Descrizione tabella      |                                                                                                                 |
| Versione                 | 1.0                                                                                                             |
| Core dataset             | False                                                                                                           |
| Dataset di origine       |                                                                                                                 |
| Richiede validazione     | False                                                                                                           |
| Esposta in DSS           | True                                                                                                            |
| Endpoint DSS             | /iag                                                                                                            |
| Query name DSS           | iag                                                                                                             |
| Formato esposizione      | JSON                                                                                                            |
| Tipologia autenticazione | Bearer token                                                                                                    |
| Tabelle genitrici        | [fbk_test1__MASTER_DATA.ASSET_PERSONE_IAG](/Documentation/fbk_test1__MASTER_DATA/ASSET_PERSONE_IAG/markdown.md) |
| Tabelle figlie           |                                                                                                                 |

## Struttura relazionale

![ASSET_PERSONE_IAG](./graph_png.png)

## Descrizione struttura tabella

| Campo                         | Descrizione                   | Tipo     | Constraints   | Linked data   | errors   |
|:------------------------------|:------------------------------|:---------|:--------------|:--------------|:---------|
| codice_identificativo_igi     | Codice identificativo igi     | string   | {}            |               | {}       |
| nome                          | Nome                          | string   | {}            |               | {}       |
| cognome                       | Cognome                       | string   | {}            |               | {}       |
| codice_fiscale                | Codice fiscale                | string   | {}            |               | {}       |
| data_nascita                  | Data nascita                  | datetime | {}            |               | {}       |
| codice_area_contrattuale      | Codice area contrattuale      | integer  | {}            |               | {}       |
| descrizione_area_contrattuale | Descrizione area contrattuale | string   | {}            |               | {}       |
| matricola                     | Matricola                     | integer  | {}            |               | {}       |
| codice_cittadino              | Codice cittadino              | integer  | {}            |               | {}       |
| applicazione                  | Applicazione                  | string   | {}            |               | {}       |
| account                       | Account                       | string   | {}            |               | {}       |
| disabilitato                  | Disabilitato                  | integer  | {}            |               | {}       |
| data_disabilitazione          | Data disabilitazione          | datetime | {}            |               | {}       |
| permesso                      | Permesso                      | string   | {}            |               | {}       |
| diritto                       | Diritto                       | string   | {}            |               | {}       |
| matricola_estesa              | Matricola estesa              | string   | {}            |               | {}       |
| codice_applicazione           | Codice applicazione           | string   | {}            |               | {}       |
| descrizione_applicazione      | Descrizione applicazione      | string   | {}            |               | {}       |
| tipologia_account             | Tipologia account             | string   | {}            |               | {}       |
| profilo                       | Profilo                       | string   | {}            |               | {}       |
| gestione                      | Gestione                      | string   | {}            |               | {}       |
