# GSUITE_SPAZIO_UTILIZZATO

## Info tabella

| Info                     | Descrizione                                                                                                                                                                 |
|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nome tabella Dremio      | GSUITE_SPAZIO_UTILIZZATO                                                                                                                                                    |
| Space Dremio             | fbk_test1__CORE_DATASET                                                                                                                                                     |
| Nome completo            | fbk_test1__CORE_DATASET.GSUITE_SPAZIO_UTILIZZATO                                                                                                                            |
| Descrizione tabella      |                                                                                                                                                                             |
| Versione                 | 1.0                                                                                                                                                                         |
| Core dataset             | True                                                                                                                                                                        |
| Dataset di origine       | GSUITE                                                                                                                                                                      |
| Richiede validazione     | True                                                                                                                                                                        |
| Esposta in DSS           | False                                                                                                                                                                       |
| Endpoint DSS             |                                                                                                                                                                             |
| Query name DSS           |                                                                                                                                                                             |
| Formato esposizione      |                                                                                                                                                                             |
| Tipologia autenticazione |                                                                                                                                                                             |
| Tabelle genitrici        |                                                                                                                                                                             |
| Tabelle figlie           | [fbk_test1__VISUALIZATION_TABLES.ASSET_PERSONE_GSUITE_SPAZIO_UTILIZZATO](/Documentation/fbk_test1__VISUALIZATION_TABLES/ASSET_PERSONE_GSUITE_SPAZIO_UTILIZZATO/markdown.md) |

## Struttura relazionale

![GSUITE_SPAZIO_UTILIZZATO](./graph_png.png)

## Descrizione struttura tabella

| Campo                             | Descrizione                       | Tipo   | Constraints   | Linked data   | errors   |
|:----------------------------------|:----------------------------------|:-------|:--------------|:--------------|:---------|
| mail_istituzionale                | Mail istituzionale                | string | {}            |               | {}       |
| gsuite_spazio_mail_utilizzato_gb  | Gsuite spazio mail utilizzato gb  | number | {}            |               | {}       |
| gsuite_spazio_drive_utilizzato_gb | Gsuite spazio drive utilizzato gb | number | {}            |               | {}       |
| gsuite_spazio_totale_gb           | Gsuite spazio totale gb           | number | {}            |               | {}       |
