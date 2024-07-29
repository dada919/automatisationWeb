import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        password_field.send_keys('Damienn')
        
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
        
        # Aller sur la page d'un produit
        self.driver.get('http://gamingavenue.ddns.net/produit/1')
        
        # Ajouter au panier
        add_to_cart_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Ajouter au panier")]')))
        add_to_cart_button.click()
        
        # Aller sur la page du panier
        self.driver.get('http://gamingavenue.ddns.net/panier')
        
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
