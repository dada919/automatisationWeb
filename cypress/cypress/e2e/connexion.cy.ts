describe('Connexion Test', () => {
    it('connexion réussie lors de l affichage du message de succès', () => {
      // Lien du site
      cy.visit('http://gamingavenue.ddns.net/');
      
      // Connexion
      cy.get('a[href="/login"]').click();
      cy.get('input[name="email"]').type('damienraunier@gmail.com');
      cy.get('input[name="password"]').type('Damien');
      cy.get('[data-cy=login-submit]').click();
      
      // Vérifier le message de succès ou d'erreur
      cy.get('div.fixed.top-4.right-4.z-50.flex.items-center.p-4.mb-4.text-sm.rounded-lg')
        .should('exist')
        .then(($message) => {
          if ($message.hasClass('bg-red-100')) {
            // S'il y a un message d'erreur
            cy.get('div.bg-red-100.text-red-700')
              .should('contain', 'Email ou mot de passe incorrect');
            throw new Error('Connexion échouée: Identifiants incorrects.');
          } else if ($message.hasClass('bg-green-100')) {
            // S'il y a un message de succès
            cy.get('div.bg-green-100.text-green-700')
              .should('contain', 'Connexion réussie');
          } else {
            throw new Error('Connexion échouée: Aucun message de succès ou d\'erreur trouvé.');
          }
        });
      
      // Attendre la disparition du message
      cy.get('div.bg-green-100.text-green-700').should('not.exist');
    });
  });
  