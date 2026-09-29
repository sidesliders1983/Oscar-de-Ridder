# Oscar de Ridder

Productierepository voor de prentenboekenreeks **Oscar de Koene Ridder**.

## Huidige productie

**Boek 3 — Gebulder in de Bergen**

Deze repository wordt gebruikt voor canon, storyboard, artwork-referenties, productie-instructies en samenwerking met Codex.

## Bron van waarheid

1. Definitieve character sheets en expliciet goedgekeurde canon
2. `canon/` documenten
3. Definitief storyboard
4. Goedgekeurd artwork
5. Werkbestanden en experimenten

Bij conflicten geldt de hoger geplaatste bron. Codex mag canon niet zelfstandig herinterpreteren.

Zie `AGENTS.md` voordat je wijzigingen maakt.

## Productiewegwijzer

Lees bij iedere nieuwe sessie eerst [AGENTS.md](AGENTS.md), deze README en alle bestaande canon. De bestaande verhaal- en stijldocumenten blijven op hun huidige pad staan.

| Pad | Doel |
| --- | --- |
| `canon/` | Verhaal, stijl en registers voor personages, locaties, objecten en boeken; zie [canonbeleid](canon/README.md) |
| `references/characters/` | Enige ingang voor definitieve character sheets: [register](references/characters/README.md) |
| `references/previous-books/` | Continuïteitsbronnen uit boek 1 en 2, niet opnieuw ontwerpen |
| `references/locations/`, `references/style/`, `references/cover/` | Bronnen met herkomst en expliciete goedkeuringsstatus |
| `storyboard/book-3/spreads/` | Eén specificatie per spread, gebaseerd op de [template](storyboard/templates/spread-template.md) |
| `prompts/illustration/`, `prompts/characters/` | Versies van werkelijk gebruikte prompts en referenties |
| `artwork/book-3/concepts/` | Gegenereerde varianten voor review |
| `artwork/book-3/approved/` | Alleen expliciet door de auteur goedgekeurde beelden |
| `artwork/book-3/production/` | Afgeleide productiebestanden met herleidbare bron |
| `production/book-3/print/`, `production/book-3/exports/` | Drukspecificaties en gecontroleerde exports |
| `docs/` | [Workflow](docs/production-workflow.md), [metadata](docs/illustration-metadata.md), [bestandsbeleid](docs/repository-hygiene.md) en [ontbrekende input](docs/author-input.md) |

Werkvolgorde: story canon → spreadspec → referenties → prompt → concept → menselijke review → revisie → goedgekeurd artwork → productie-export.

Codex mag structuur, specificaties en concepten binnen goedgekeurde uitgangspunten voorbereiden. Codex mag geen ontbrekende canon invullen, referenties vervangen, beelden zelf goedkeuren of boek 1/2 herontwerpen. Bij ontbrekende creatieve informatie: `CANON QUESTION`; vraag de auteur vóór afhankelijke productie. Deze inrichting bevat nog geen ingevulde spreads of geïmporteerde beeldreferenties.
