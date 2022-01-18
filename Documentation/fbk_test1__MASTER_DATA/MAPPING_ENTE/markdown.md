# MAPPING_ENTE

## Info tabella

| Info                     | Descrizione                                                                                                                                                             |
|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nome tabella Dremio      | MAPPING_ENTE                                                                                                                                                            |
| Space Dremio             | fbk_test1__MASTER_DATA                                                                                                                                                  |
| Nome completo            | fbk_test1__MASTER_DATA.MAPPING_ENTE                                                                                                                                     |
| Descrizione tabella      |                                                                                                                                                                         |
| Versione                 | 1.0                                                                                                                                                                     |
| Core dataset             | False                                                                                                                                                                   |
| Dataset di origine       |                                                                                                                                                                         |
| Richiede validazione     | True                                                                                                                                                                    |
| Esposta in DSS           | False                                                                                                                                                                   |
| Endpoint DSS             |                                                                                                                                                                         |
| Query name DSS           |                                                                                                                                                                         |
| Formato esposizione      |                                                                                                                                                                         |
| Tipologia autenticazione |                                                                                                                                                                         |
| Tabelle genitrici        |                                                                                                                                                                         |
| Tabelle figlie           | [fbk_test1__MASTER_DATA.PERSONA_ANAGRAFICA_RCE](/Documentation/fbk_test1__MASTER_DATA/PERSONA_ANAGRAFICA_RCE/markdown.md)                                               |
|                          | [fbk_test1__MASTER_DATA.PERSONA_ANAGRAFICA_S1P](/Documentation/fbk_test1__MASTER_DATA/PERSONA_ANAGRAFICA_S1P/markdown.md)                                               |
|                          | [fbk_test1__MASTER_DATA.PERSONA_ASSEGNAZIONE_ORARIO](/Documentation/fbk_test1__MASTER_DATA/PERSONA_ASSEGNAZIONE_ORARIO/markdown.md)                                     |
|                          | [fbk_test1__MASTER_DATA.PERSONA_ASSEGNAZIONE_STRUTTURA_RCE](/Documentation/fbk_test1__MASTER_DATA/PERSONA_ASSEGNAZIONE_STRUTTURA_RCE/markdown.md)                       |
|                          | [fbk_test1__MASTER_DATA.PERSONA_ASSEGNAZIONE_STRUTTURA_S1P](/Documentation/fbk_test1__MASTER_DATA/PERSONA_ASSEGNAZIONE_STRUTTURA_S1P/markdown.md)                       |
|                          | [fbk_test1__MASTER_DATA.PERSONA_CATEGORIA_ORARIO](/Documentation/fbk_test1__MASTER_DATA/PERSONA_CATEGORIA_ORARIO/markdown.md)                                           |
|                          | [fbk_test1__MASTER_DATA.PERSONA_CONTRATTO](/Documentation/fbk_test1__MASTER_DATA/PERSONA_CONTRATTO/markdown.md)                                                         |
|                          | [fbk_test1__MASTER_DATA.PERSONA_FORMAZIONE](/Documentation/fbk_test1__MASTER_DATA/PERSONA_FORMAZIONE/markdown.md)                                                       |
|                          | [fbk_test1__MASTER_DATA.PERSONA_MAIL](/Documentation/fbk_test1__MASTER_DATA/PERSONA_MAIL/markdown.md)                                                                   |
|                          | [fbk_test1__MASTER_DATA.PERSONA_QUALIFICA](/Documentation/fbk_test1__MASTER_DATA/PERSONA_QUALIFICA/markdown.md)                                                         |
|                          | [fbk_test1__MASTER_DATA.PERSONA_TELELAVORO](/Documentation/fbk_test1__MASTER_DATA/PERSONA_TELELAVORO/markdown.md)                                                       |
|                          | [fbk_test1__MASTER_DATA.PERSONA_TITOLO_STUDIO](/Documentation/fbk_test1__MASTER_DATA/PERSONA_TITOLO_STUDIO/markdown.md)                                                 |
|                          | [fbk_test1__MASTER_DATA.STRUTTURA_RESPONSABILE_ASSEGNAZIONE_STRUTTURA](/Documentation/fbk_test1__MASTER_DATA/STRUTTURA_RESPONSABILE_ASSEGNAZIONE_STRUTTURA/markdown.md) |

## Struttura relazionale

![MAPPING_ENTE](./graph_png.png)

## Descrizione struttura tabella

| Campo              | Descrizione        | Tipo    | Constraints   | Linked data   | errors   |
|:-------------------|:-------------------|:--------|:--------------|:--------------|:---------|
| codice_ente        | Codice ente        | integer | {}            |               | {}       |
| prefisso_matricola | Prefisso matricola | string  | {}            |               | {}       |
