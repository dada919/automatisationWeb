import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@pytest.mark.usefixtures("setup")
class TestCommande:
    def test_commande_process(self):
        # Lien du site
        self.driver.get('http://gamingavenue.ddns.net/')
        
        # Connexion
        login_link = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/login"]')))
        login_link.click()        
        
        email_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
        email_field.send_keys('damienraunier@gmail.com')
        
        password_field = self.driver.find_element(By.NAME, 'password')
        password_field.send_keys('Damien')
        
        login_button = self.driver.find_element(By.CSS_SELECTOR, '[data-cy=login-submit]')
        login_button.click()
        
        # Vérifier la connexion
        try:
            # Attendre le message de bienvenue
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Bienvenue dans le paradis du gamer")]')))
            print("Connexion réussie")
        except TimeoutException:
            print("Connexion échouée.")
            assert False, "Connexion échouée"
        
        # Effectuer une recherche de produit
        search_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.p-2.border.rounded')))
        search_field.send_keys('a')
        
        search_button = self.driver.find_element(By.CSS_SELECTOR, 'button.p-2.bg-primary-700.text-white.rounded.hover\\:bg-primary-800.focus\\:outline-none')
        search_button.click()
        
        # Cliquer sur le premier produit rechercher
        first_product = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.w-full.max-w-sm.bg-white.border')))
        first_product_link = first_product.find_element(By.CSS_SELECTOR, 'a[href^="/produit/"]')
        first_product_link.click()
        
        # Ajouter au panier
        add_to_cart_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Ajouter au panier")]')))
        add_to_cart_button.click()

        # Attendre la disparition du message de succès
        try:
            success_message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.fixed.top-4.right-4.z-50.flex.items-center.p-4.mb-4.text-sm.rounded-lg.bg-green-100.text-green-700.border.border-green-400')))
            WebDriverWait(self.driver, 10).until(EC.staleness_of(success_message))
        except TimeoutException:
            print("Le message de succès n'est pas apparu ou n'a pas disparu à temps.")
        
        # cliquer sur panier
        cart_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/panier"]')))
        cart_button.click()
        
        # Procéder à la commande
        self.driver.find_element(By.XPATH, '//button[contains(text(), "Étape suivante")]').click()
        
        # Passer à l'étape de paiement
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), 'France'))
        self.driver.find_element(By.XPATH, '//button[contains(text(), "Étape suivante")]').click()
        
        # Passer la commande
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), 'Raunier'))
        self.driver.find_element(By.XPATH, '//button[contains(text(), "Procéder au paiement")]').click()
        
        # Vérifier que la commande est terminée
        WebDriverWait(self.driver, 10).until(EC.url_contains('/thanks'))
        assert 'Merci pour votre commande !' in self.driver.page_source
        print("Commande passé avec succès!")
