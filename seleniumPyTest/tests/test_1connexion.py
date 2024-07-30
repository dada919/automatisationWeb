import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@pytest.mark.usefixtures("setup")
class TestConnexion:
    def test_connexion_process(self):
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
        
        # Test du message de succès ou d'erreur
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div.fixed.top-4.right-4.z-50.flex.items-center.p-4.mb-4.text-sm.rounded-lg'))
            )
        except TimeoutException:
            print("Aucun message de succès ou d'erreur trouvé")
            assert False, "Connexion échouée: Aucun message de succès ou d'erreur trouvé."
        
        # S'il y a un message d'erreur
        error_message = self.driver.find_elements(By.CSS_SELECTOR, 'div.bg-red-100.text-red-700')
        if error_message:
            assert False, "Connexion échouée: Identifiants incorrects."
        
        # S'il y a un message de succès
        success_message = self.driver.find_elements(By.CSS_SELECTOR, 'div.bg-green-100.text-green-700')
        if not success_message:
            assert False, "Connexion échouée: Message de succès non trouvé."
        
        # Attendre la disparition du message
        WebDriverWait(self.driver, 10).until(EC.staleness_of(success_message[0]))
