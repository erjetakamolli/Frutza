from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import matplotlib.pyplot as plt

# Inicializimi i driver-it
driver = webdriver.Chrome()

# Navigimi ne faqen e frutave te thata
driver.get("https://app.frutza.com/bundle-detail/custom-box?lang=sq")
sleep(10)

# Funksioni per te konvertuar çmimin
def clean_price(price_str):
    # Remove 'Lek' and '/100 g'
    return float(price_str.replace("Lek", "").replace("/100 g", "").strip())

# Mbledhim te dhenat per frutat e thata
seasonal_data = []
try:
    # Loop per elementet qe permbajne informacione per per frutat e thata
    for i in range(1, 8):  # Numri aktual i te frutave te stines te shfaqura
        name_xpath = f"/html/body/app-root/div/div/app-custom-box/div/div[2]/div/div/div/div[3]/div[{i}]/div[1]/div/p[1]"
        price_xpath = f"/html/body/app-root/div/div/app-custom-box/div/div[2]/div/div/div/div[3]/div[{i}]/div[1]/div/p[2]"
        
        name = driver.find_element(By.XPATH, name_xpath).get_attribute("innerHTML")
        price = driver.find_element(By.XPATH, price_xpath).get_attribute("innerHTML")
        
        price = clean_price(price)
        seasonal_data.append({"name": name, "price": price})
except Exception as e:
    print(f"Error collecting data for seasonal fruit: {e}")

# Mbyllja e driver-it
driver.quit()

# Printimi i te dhenave te mbledhura
print("Te dhenat e frutave te thata:")
for fruit in seasonal_data:
    print(f"Emri: {fruit['name']}, Cmimi: {fruit['price']} Lek/100g")

# Renditja e te dhenave sipas çmimit ne rend rrites
seasonal_data = sorted(seasonal_data, key=lambda x: x['price'])

# Ndertimi i grafikut me matplotlib
names = [fruit["name"] for fruit in seasonal_data]
prices = [fruit["price"] for fruit in seasonal_data]

# Bar chart per krahasimin e çmimeve te frutave te thata
plt.figure(figsize=(10, 6))
plt.barh(names, prices, color='orange')
plt.xlabel('Çmimi (Lekë/100g)')
plt.title('Krahasimi i Çmimeve të Frutave të Thata')
plt.xticks(rotation=45)
plt.show()

