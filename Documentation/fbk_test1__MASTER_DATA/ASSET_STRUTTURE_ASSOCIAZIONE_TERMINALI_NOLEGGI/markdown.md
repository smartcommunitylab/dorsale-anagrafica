# ASSET_STRUTTURE_ASSOCIAZIONE_TERMINALI_NOLEGGI

## Info tabella

| Info                     | Descrizione                                                                                                                                                                   |
|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nome tabella Dremio      | ASSET_STRUTTURE_ASSOCIAZIONE_TERMINALI_NOLEGGI                                                                                                                                |
| Space Dremio             | fbk_test1__MASTER_DATA                                                                                                                                                        |
| Nome completo            | fbk_test1__MASTER_DATA.ASSET_STRUTTURE_ASSOCIAZIONE_TERMINALI_NOLEGGI                                                                                                         |
| Descrizione tabella      |                                                                                                                                                                               |
| Versione                 | 1.0                                                                                                                                                                           |
| Core dataset             | False                                                                                                                                                                         |
| Dataset di origine       |                                                                                                                                                                               |
| Richiede validazione     | False                                                                                                                                                                         |
| Esposta in DSS           | False                                                                                                                                                                         |
| Endpoint DSS             |                                                                                                                                                                               |
| Query name DSS           |                                                                                                                                                                               |
| Formato esposizione      |                                                                                                                                                                               |
| Tipologia autenticazione |                                                                                                                                                                               |
| Tabelle genitrici        | [fbk_test1__CORE_DATASET.FONIA_CONTRATTO](/fbk_test1__CORE_DATASET/FONIA_CONTRATTO/markdown.md)                                                                               |
|                          | [fbk_test1__CORE_DATASET.FONIA_FASCIA_TERMINALE](/fbk_test1__CORE_DATASET/FONIA_FASCIA_TERMINALE/markdown.md)                                                                 |
|                          | [fbk_test1__CORE_DATASET.FONIA_MARCA_TERMINALE](/fbk_test1__CORE_DATASET/FONIA_MARCA_TERMINALE/markdown.md)                                                                   |
|                          | [fbk_test1__CORE_DATASET.FONIA_MODELLO_TERMINALE](/fbk_test1__CORE_DATASET/FONIA_MODELLO_TERMINALE/markdown.md)                                                               |
|                          | [fbk_test1__CORE_DATASET.FONIA_NOLEGGIO_TERMINALE](/fbk_test1__CORE_DATASET/FONIA_NOLEGGIO_TERMINALE/markdown.md)                                                             |
|                          | [fbk_test1__CORE_DATASET.FONIA_TERMINALE](/fbk_test1__CORE_DATASET/FONIA_TERMINALE/markdown.md)                                                                               |
|                          | [fbk_test1__CORE_DATASET.FONIA_TERMINALE_ASSEGNATO](/fbk_test1__CORE_DATASET/FONIA_TERMINALE_ASSEGNATO/markdown.md)                                                           |
|                          | [fbk_test1__CORE_DATASET.FONIA_TIPOLOGIA_TERMINALE](/fbk_test1__CORE_DATASET/FONIA_TIPOLOGIA_TERMINALE/markdown.md)                                                           |
| Tabelle figlie           | [fbk_test1__MASTER_DATA.ASSET_TOTALI_ASSOCIAZIONE_TERMINALI_NOLEGGI](/fbk_test1__MASTER_DATA/ASSET_TOTALI_ASSOCIAZIONE_TERMINALI_NOLEGGI/markdown.md)                         |
|                          | [fbk_test1__VISUALIZATION_TABLES.ASSET_STRUTTURE_ASSOCIAZIONE_TERMINALI_NOLEGGI](/fbk_test1__VISUALIZATION_TABLES/ASSET_STRUTTURE_ASSOCIAZIONE_TERMINALI_NOLEGGI/markdown.md) |
|                          | [fbk_test1__VISUALIZATION_TABLES.ASSET_TOTALI_ASSOCIAZIONE_TERMINALI_NOLEGGI](/fbk_test1__VISUALIZATION_TABLES/ASSET_TOTALI_ASSOCIAZIONE_TERMINALI_NOLEGGI/markdown.md)       |

## Struttura relazionale

![ASSET_STRUTTURE_ASSOCIAZIONE_TERMINALI_NOLEGGI](./graph_png.png)

## Descrizione struttura tabella

| Campo                             | Descrizione                       | Tipo    | Constraints   | Linked data   | errors   |
|:----------------------------------|:----------------------------------|:--------|:--------------|:--------------|:---------|
| terminale_id                      | Terminale id                      | integer | {}            |               | {}       |
| imei                              | Imei                              | string  | {}            |               | {}       |
| terminale_is_riscattato           | Terminale is riscattato           | integer | {}            |               | {}       |
| stato_terminale                   | Stato terminale                   | string  | {}            |               | {}       |
| descrizione_modello_terminale     | Descrizione modello terminale     | string  | {}            |               | {}       |
| descrizione_fascia_terminale      | Descrizione fascia terminale      | string  | {}            |               | {}       |
| descrizione_tipologia_terminale   | Descrizione tipologia terminale   | string  | {}            |               | {}       |
| descrizione_marca_terminale       | Descrizione marca terminale       | string  | {}            |               | {}       |
| caratteristiche_modello_terminale | Caratteristiche modello terminale | string  | {}            |               | {}       |
| peso_modello_terminale            | Peso modello terminale            | string  | {}            |               | {}       |
| codice_riferimento_contratto      | Codice riferimento contratto      | string  | {}            |               | {}       |
| descrizione_contratto             | Descrizione contratto             | string  | {}            |               | {}       |
| contratto_id                      | Contratto id                      | integer | {}            |               | {}       |
| canone_noleggio_terminale         | Canone noleggio terminale         | number  | {}            |               | {}       |
| durata_noleggio_terminale         | Durata noleggio terminale         | integer | {}            |               | {}       |
