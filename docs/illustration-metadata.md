# Illustratiemetadata

Elke spread krijgt één Markdown-specificatie met YAML-frontmatter volgens `storyboard/templates/spread-template.md`. Deze specificatie is het manifest: boek, nummer, story beat, personages, canonieke objecten, locatie, compositie, camera, expressies, tekstgebied, middenvouw, bronnen, prompt, revisies, status en goedgekeurd asset staan bij elkaar.

Gebruik repository-relatieve paden en versies zoals `book-3_spread-NN_v001`. Het spreadnummer is geen besluit over het aantal spreads. `null` betekent nog niet bekend; nooit een verzonnen standaardwaarde. Markeer ontbrekende creatieve keuzes als `OPEN QUESTION` / `CANON QUESTION`.

`source_reference_images` bevat per bron `path`, `version_or_commit`, `status`, `origin` en `purpose`. Neem voor ieder aanwezig personage de actieve sheet uit het characterregister op. `generation_prompt` verwijst naar de laatste gebruikte prompt; oudere pogingen blijven in `revision_notes` terugvindbaar.

Bewaar per generatie een afzonderlijk Markdown-bestand in `prompts/illustration/` (characterexperimenten in `prompts/characters/`) met:

- spreadspec-pad en commit/versie;
- exacte volledige prompt, inclusief verwijzingen naar canon en gebruikte character references;
- exacte referentiepaden en versies, in de volgorde waarin ze zijn meegestuurd;
- generator/model en beschikbare instellingen, seed en run-id indien beschikbaar; anders expliciet `niet beschikbaar`;
- datum, outputpad en assetversie;
- revisiereden en bronversie; reviewresultaat en eventuele goedkeuringsbron.

Een identieke prompt garandeert geen identiek beeld. Bewaar daarom ook de geselecteerde output en beschikbare generatiegegevens.

`revision_notes` bevat per poging `version`, `prompt`, `asset`, `reason`, `review` en `date`. Overschrijf eerdere pogingen niet. Bij `APPROVED ARTWORK` moeten `approved_asset` en `approval.by/date/evidence` ingevuld zijn en naar de exact goedgekeurde versie verwijzen. Bij een nieuwe revisie blijft de eerdere goedkeuring alleen voor het oude asset gelden; de nieuwe variant is `CONCEPT`.

Productie-afgeleiden krijgen een begeleidend Markdown-record met bronasset/commit, bewerkingen, uitvoerpad, afmetingen, kleurprofiel, bleed, controledatum en reviewer. Wijzigingen aan personages of inhoud gaan opnieuw naar menselijke review.
