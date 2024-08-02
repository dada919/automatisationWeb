## Automatisation Web Raunier Damien



# Selenium

### Installation des outils

Outils nécessaires:
- Python
- pip
- Selenium
- Pytest

Télécharger la version compatible de Chrome Web Driver: [Télécharger Chrome Web Driver](https://googlechromelabs.github.io/chrome-for-testing/)
 

### Installation et configuration des dépendances

Ce placer dans le répertoire **seleniumPyTest**
```bash
cd .\seleniumPyTest\
```

Installez les dépendances nécessaires à partir du fichier `requirements.txt` :
```bash
pip install -r requirements.txt
```

### Exécuter les tests

Commande pour éxécuter les tests dans le répertoire **seleniumPyTest**
```bash
pytest tests/
```


# Cypress

### Installation des outils

Outils nécessaires:
- Node.js (https://nodejs.org/) - recommandé d'utiliser la version LTS
- npm (installé avec Node.js)


### Installation et configuration des dépendances

Ce placer dans le répertoire **cypress**
```bash
cd .\cypress\
```

Installez toutes les dépendances nécessaires à partir du fichier `package.json` :
```bash
npm install
```


### Exécuter les tests

Ouvrir l'interface graphique de Cypress :
```bash
npx cypress open
```

Exécuter les tests en mode headless :
```bash
npx cypress run
```