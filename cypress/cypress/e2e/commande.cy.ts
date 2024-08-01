import 'cypress-xpath';

describe('Commande Test', () => {
  it('Passage d une commande réussie lors de l affichage de la page "thanks"', () => {
    // Lien du site
    cy.visit('/');
    
    // Connexion
    cy.xpath('//a[contains(@href, "/login")]').click();
    cy.login();
    
    // Vérifier la connexion
    cy.xpath('//div[contains(@class, "fixed top-4 right-4 z-50 flex items-center p-4 mb-4 text-sm rounded-lg")]')
      .should('exist')
      .then(($message) => {
        if ($message.hasClass('bg-red-100')) {
          // S'il y a un message d'erreur
          cy.xpath('//div[contains(@class, "bg-red-100 text-red-700")]')
            .should('contain', 'Email ou mot de passe incorrect');
          throw new Error('Connexion échouée: Identifiants incorrects.');
        } else if ($message.hasClass('bg-green-100')) {
          // S'il y a un message de succès
          cy.xpath('//div[contains(@class, "bg-green-100 text-green-700")]')
            .should('contain', 'Connexion réussie');
        } else {
          throw new Error('Connexion échouée: Aucun message de succès ou d\'erreur trouvé.');
        }
      });
    
    // Effectuer une recherche de produit
    cy.xpath('//input[contains(@class, "p-2 border rounded")]').type('a');
    cy.xpath('//button[contains(@class, "p-2 bg-primary-700 text-white rounded hover:bg-primary-800 focus:outline-none")]').click();
    
    // Cliquer sur le premier produit recherché
    cy.get('div.flex.flex-wrap.justify-center').find('a[href^="/produit/"]').first().click();
    
    // Ajouter au panier
    cy.xpath('//button[contains(text(), "Ajouter au panier")]').click();
    
    // Attendre la disparition du message de succès
    cy.xpath('//div[contains(@class, "fixed top-4 right-4 z-50 flex items-center p-4 mb-4 text-sm rounded-lg bg-green-100 text-green-700 border border-green-400")]', { timeout: 10000 })
      .should('exist')
      .wait(5000) // delay
      .should('not.exist', { timeout: 10000 });
    
    // Cliquer sur le panier
    cy.xpath('//a[contains(@href, "/panier")]').first().click();
    
    // Procéder à la commande
    cy.xpath('//button[contains(text(), "Étape suivante")]').click();
    
    // Passer à l'étape de paiement
    cy.contains('France');
    cy.xpath('//button[contains(text(), "Étape suivante")]').click();
    
    // Passer la commande
    cy.contains('Raunier');
    cy.xpath('//button[contains(text(), "Procéder au paiement")]').click();
    
    // Vérifier que la commande est terminée
    cy.url().should('include', '/thanks');
    cy.contains('Merci pour votre commande !');
  });
});
