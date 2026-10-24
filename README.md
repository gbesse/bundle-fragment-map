# bundle-fragment-map

## Français

Reconstituer les octets manquants et contradictoires des fragments.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m bundle_fragment_map examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Assemble les octets de fragments déclarés, fusionne les recouvrements identiques et conserve les contradictions avec leurs identifiants. Différent du suivi envoi/ACK de packet-custody-replay : vérifie ici le contenu.

### Limites

Un seul payload déclaré, sans CBOR/BPv7 ni identité/authenticité de bundle vérifiée. Le hachage est absent si un octet manque ou se contredit.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Reconstruct missing and conflicting bytes across fragments.

Synthetic data; no network access or secret required.

```sh
python -m bundle_fragment_map examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Assembles declared fragment bytes, merges identical overlaps and retains conflicts with their identities. Unlike packet-custody-replay send/ACK tracking, this checks payload content.

### Limits

One declared payload, no CBOR/BPv7 or verified bundle identity/authenticity. No payload hash is emitted while any byte is missing or conflicting.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Reconstruir bytes ausentes y contradictorios entre fragmentos.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m bundle_fragment_map examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Ensambla bytes declarados, combina solapamientos idénticos y conserva conflictos con sus identidades. A diferencia de packet-custody-replay, comprueba contenido y no envío/acuses.

### Límites

Un único contenido declarado, sin CBOR/BPv7 ni identidad/autenticidad verificada. No se emite hash si falta un byte o existe conflicto.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://www.rfc-editor.org/rfc/rfc9171
