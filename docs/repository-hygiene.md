# Bestandsbeleid en voorgestelde LFS-policy

Commit tekstspecificaties, prompts, bronregisters en geselecteerde noodzakelijke assets. Bewaar ruwe tijdelijke renders en omvangrijke afgewezen tussenversies buiten Git of onder een genegeerde `tmp/` of `renders/`-map. Bewaar van behouden varianten metadata en herkomst; verwijder geen bestaande referenties zonder opdracht.

De `.gitignore` sluit tijdelijke/cachebestanden uit, maar negeert niet generiek PNG, JPG, PDF of productiemappen: geselecteerde referenties en goedgekeurde bestanden moeten bewust gevolgd kunnen worden. Controleer vóór iedere commit `git status` en de bestandsgroottes.

Voorstel, nog niet geactiveerd: gebruik Git LFS voor geselecteerde grote binaire illustratiebronnen, bijvoorbeeld PSD/TIFF en hoogwaardige PNG/PDF-productieassets, wanneer de werkelijke omvang en revisiefrequentie dit rechtvaardigen. Beoordeel bestanden vanaf circa 10 MB individueel; dit is een voorgestelde projectdrempel, geen providerlimiet. Kleine previews kunnen gewoon in Git blijven.

Vraag vóór invoering expliciet akkoord op bestandstypen/paden, opslag- en bandbreedtebudget, toegang voor medewerkers, back-up en downloadworkflow. Voeg pas daarna `.gitattributes` en LFS-configuratie toe. Migratie van bestaande geschiedenis vergt afzonderlijk akkoord. Deze wijziging activeert geen LFS en migreert geen bestanden.
