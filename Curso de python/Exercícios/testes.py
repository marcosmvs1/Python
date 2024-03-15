from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

# Importar lista de contatos
contatos = ["+5512997922958"]  # Insira os números de telefone aqui, sem espaços ou caracteres especiais.

# Configurar mensagem
mensagem = "Olá! \n\nEstou enviando esta mensagem automaticamente para todos os meus contatos. \n\n[Insira a sua mensagem aqui]"

# Abrir o navegador
driver = webdriver.Chrome(ChromeDriverManager().install())

# Acessar o WhatsApp Web
driver.get("https://web.whatsapp.com/")

# Esperar até que o usuário escaneie o QR Code
input("Por favor, escaneie o QR Code e pressione Enter após o login...")

try:
    # Aguardar até que a página seja completamente carregada
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "side")))

    # Loop para enviar mensagens
    for contato in contatos:
        print("Enviando mensagem para:", contato)

        try:
            # Buscar contato
            campo_busca = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='_2_1wd copyable-text selectable-text']")))
            campo_busca.clear()
            campo_busca.send_keys(contato)

            # Aguardar a seleção do contato
            contato_xpath = f"//span[@title='{contato}']"
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, contato_xpath))).click()

            # Escrever mensagem
            campo_mensagem = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='_2A8P4']/div/div[@contenteditable='true']")))
            campo_mensagem.send_keys(mensagem)

            # Enviar mensagem
            driver.find_element(By.XPATH, "//span[@data-icon='send']").click()
            print("Mensagem enviada com sucesso!")
        except TimeoutException:
            print(f"Falha ao enviar mensagem para {contato}: Tempo limite excedido")
        except Exception as e:
            print(f"Erro ao enviar mensagem para {contato}: {str(e)}")

except TimeoutException:
    print("Tempo limite excedido ao tentar carregar a página.")

finally:
    # Fechar o navegador
    driver.quit()

# Mensagem de sucesso
print("Mensagens enviadas para todos os contatos com sucesso! ")
