# Canon en status

De hiërarchie uit `AGENTS.md` is leidend: definitieve character sheets / expliciet goedgekeurde visuele referenties → `canon/` → definitief storyboard → goedgekeurd artwork → concepten. Het plaatsen van een bestand in een map geeft het nooit automatisch autoriteit.

| Status | Betekenis |
| --- | --- |
| CANON | Expliciet vastgesteld; leg bron en goedkeuring vast |
| WORKING CANON | Werkbasis met expliciete open punten; geen toestemming die zelf in te vullen |
| CONCEPT | Voorstel of gegenereerde variant, nog niet goedgekeurd |
| OPEN QUESTION | Ontbrekende of conflicterende informatie; markeer als `CANON QUESTION` |
| APPROVED ARTWORK | Expliciet goedgekeurd beeld; verandert op zichzelf geen canon |

Gebruik deze exacte waarden in nieuwe metadata. Bestaande documenten behouden hun inhoud en status: [boek 3](book-3-story-canon.md) is working canon; [visuele stijl](visual-style.md) bevat de bestaande artworkregels. Introduceer geen tweede kopie van deze bronnen.

`characters/`, `locations/`, `objects/` en `books/` bevatten tekstuele registers en verwijzingen, geen concurrerende definitieve character sheets. De enige ingang naar die sheets is `references/characters/README.md`.

Een canonwijziging vereist een afzonderlijk, herkenbaar voorstel met reden, oude/nieuwe tekst, bron, betrokken spreads en referenties. Vraag expliciete auteursgoedkeuring en noteer wie, wanneer en waar goedkeurde. Pas daarna de canon en afhankelijke registers aan in een controleerbare commit. Bewaar oude referentieversies; wijs de nieuwe actieve versie expliciet aan. Een goedgekeurd conceptbeeld of productie-export vervangt nooit stilzwijgend canon.

Bij conflicten of ontbrekende feiten: documenteer `CANON QUESTION`, vraag bevestiging en stop alleen het werk dat daarvan afhangt. Zie `docs/author-input.md` voor de huidige open punten.
