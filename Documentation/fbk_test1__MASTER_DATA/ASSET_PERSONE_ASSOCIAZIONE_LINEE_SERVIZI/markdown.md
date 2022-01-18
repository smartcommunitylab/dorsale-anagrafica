# ASSET_PERSONE_ASSOCIAZIONE_LINEE_SERVIZI

## Info tabella

| Info                     | Descrizione                                                                                                                                                                     |
|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nome tabella Dremio      | ASSET_PERSONE_ASSOCIAZIONE_LINEE_SERVIZI                                                                                                                                        |
| Space Dremio             | fbk_test1__MASTER_DATA                                                                                                                                                          |
| Nome completo            | fbk_test1__MASTER_DATA.ASSET_PERSONE_ASSOCIAZIONE_LINEE_SERVIZI                                                                                                                 |
| Descrizione tabella      |                                                                                                                                                                                 |
| Versione                 | 1.0                                                                                                                                                                             |
| Core dataset             | False                                                                                                                                                                           |
| Dataset di origine       |                                                                                                                                                                                 |
| Richiede validazione     | True                                                                                                                                                                            |
| Esposta in DSS           | False                                                                                                                                                                           |
| Endpoint DSS             |                                                                                                                                                                                 |
| Query name DSS           |                                                                                                                                                                                 |
| Formato esposizione      |                                                                                                                                                                                 |
| Tipologia autenticazione |                                                                                                                                                                                 |
| Tabelle genitrici        | [fbk_test1__CORE_DATASET.FONIA_CONTRATTO](/Documentation/fbk_test1__CORE_DATASET/FONIA_CONTRATTO/markdown.md)                                                                   |
|                          | [fbk_test1__CORE_DATASET.FONIA_LINEA](/Documentation/fbk_test1__CORE_DATASET/FONIA_LINEA/markdown.md)                                                                           |
|                          | [fbk_test1__CORE_DATASET.FONIA_LINEA_ASSEGNATA](/Documentation/fbk_test1__CORE_DATASET/FONIA_LINEA_ASSEGNATA/markdown.md)                                                       |
|                          | [fbk_test1__CORE_DATASET.FONIA_SERVIZIO](/Documentation/fbk_test1__CORE_DATASET/FONIA_SERVIZIO/markdown.md)                                                                     |
|                          | [fbk_test1__CORE_DATASET.FONIA_SERVIZIO_ASSEGNATO](/Documentation/fbk_test1__CORE_DATASET/FONIA_SERVIZIO_ASSEGNATO/markdown.md)                                                 |
| Tabelle figlie           | [fbk_test1__MASTER_DATA.ASSET_TOTALI_ASSOCIAZIONE_LINEE_SERVIZI](/Documentation/fbk_test1__MASTER_DATA/ASSET_TOTALI_ASSOCIAZIONE_LINEE_SERVIZI/markdown.md)                     |
|                          | [fbk_test1__VISUALIZATION_TABLES.ASSET_PERSONE_ASSOCIAZIONE_LINEE_SERVIZI](/Documentation/fbk_test1__VISUALIZATION_TABLES/ASSET_PERSONE_ASSOCIAZIONE_LINEE_SERVIZI/markdown.md) |
|                          | [fbk_test1__VISUALIZATION_TABLES.ASSET_TOTALI_ASSOCIAZIONE_LINEE_SERVIZI](/Documentation/fbk_test1__VISUALIZATION_TABLES/ASSET_TOTALI_ASSOCIAZIONE_LINEE_SERVIZI/markdown.md)   |

## Struttura relazionale

![ASSET_PERSONE_ASSOCIAZIONE_LINEE_SERVIZI](./graph_png.png)

## Descrizione struttura tabella

| Campo                             | Descrizione                       | Tipo    | Constraints   | Linked data   | errors   |
|:----------------------------------|:----------------------------------|:--------|:--------------|:--------------|:---------|
| id_assegnazione_servizio          | Id assegnazione servizio          | integer | {}            |               | {}       |
| data_fine_assegnazione_servizio   | Data fine assegnazione servizio   | date    | {}            |               | {}       |
| data_inizio_assegnazione_servizio | Data inizio assegnazione servizio | date    | {}            |               | {}       |
| linea_id                          | Linea id                          | integer | {}            |               | {}       |
| numero_telefono                   | Numero telefono                   | string  | {}            |               | {}       |
| stato_linea                       | Stato linea                       | string  | {}            |               | {}       |
| descrizione_servizio              | Descrizione servizio              | string  | {}            |               | {}       |
| canone_servizio                   | Canone servizio                   | number  | {}            |               | {}       |
| codice_servizio                   | Codice servizio                   | string  | {}            |               | {}       |
| servizio_is_gratuito              | Servizio is gratuito              | integer | {}            |               | {}       |
| tipo_canone_servizio              | Tipo canone servizio              | string  | {}            |               | {}       |
| codice_riferimento_contratto      | Codice riferimento contratto      | string  | {}            |               | {}       |
| descrizione_contratto             | Descrizione contratto             | string  | {}            |               | {}       |
