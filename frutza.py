from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import matplotlib.pyplot as plt

# Initialize the Firefox driver
driver = webdriver.Firefox()

# Navigate to the website
driver.get("https://frutza.com/home?lang=sq")

sleep(10)
# Printojme titullin e Web faqes!
titulli = driver.find_element(By.XPATH, "/html/head/title").get_attribute("innerHTML");
print(titulli)

# Printojme gjuhet ne te cilat disponohet ky web!
gjuhet = driver.find_element(By.XPATH, "/html/body/nav/div/div/div[1]").get_attribute("innerHTML");
print(gjuhet)

# Gjejme sezonet e frutave qe disponon ky web!
sezonet = driver.find_element(By.XPATH, "/html/body/nav/div/div/div[2]").get_attribute("innerHTML");
print(sezonet)

# Ky biznes operon vetem per qytetin e Tiranes!
operon = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/p").get_attribute("innerHTML");
print(operon)

# Slogani i ketij biznesi!
slogani = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/h1").get_attribute("innerHTML");
print(slogani)

# Shkrimi i banerit!
banner = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/p").get_attribute("innerHTML");
print(banner)

# Si funksionon ky sherbim!
function = driver.find_element(By.XPATH, "/html/body/div[2]/div/h2").get_attribute("innerHTML");
print(function)

# Zgjidh Planin per frutat qe deshiron!
plani = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/h3").get_attribute("innerHTML");
print(plani)

# Detaje 
detaje = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/h3").get_attribute("innerHTML");
print(detaje)

detaje = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/p").get_attribute("innerHTML");
print(detaje)

# Detajet e shportes
shporta = driver.find_element(By.XPATH, "/html/body/div[3]/div/h2").get_attribute("innerHTML");
print(shporta)

# Pershkrimi per shporten
pershkrim = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div[1]/p").get_attribute("innerHTML");
print(pershkrim)

# Funksioni per te konvertuar çmimin
def clean_price(price_str):
    # Remove 'Lek' and '/100 g'
    return float(price_str.replace("Lek", "").replace("/100 g", "").strip())

# Mbledhja e te dhenave per secilen pako
bundle_data = []

# Funksioni per te mbledhur te dhena per nje pako
def collect_bundle_data(index):
    try:
        name_xpath = f"/html/body/app-root/div/div/app-bundle-details/div/div/div[3]/div[{index}]/app-bundle-detail-card/div/div/div[2]/h4"
        price_xpath = f"/html/body/app-root/div/div/app-bundle-details/div/div/div[3]/div[{index}]/app-bundle-detail-card/div/div/div[1]/div[2]/div[1]/div[2]/p"
        description_xpath = f"/html/body/app-root/div/div/app-bundle-details/div/div/div[3]/div[{index}]/app-bundle-detail-card/div/div/div[1]/div[2]/div[2]/p"
        
        name = driver.find_element(By.XPATH, name_xpath).get_attribute("innerHTML")
        price = driver.find_element(By.XPATH, price_xpath).get_attribute("innerHTML")
        description = driver.find_element(By.XPATH, description_xpath).get_attribute("innerHTML")
        
        price = clean_price(price)
        bundle_data.append({"name": name, "price": price, "description": description})
    except Exception as e:
        print(f"Error collecting data for bundle {index}: {e}")

# Navigimi ne faqen e kutive
driver.get("https://app.frutza.com/bundle-detail?lang=sq")
sleep(30)

# Mbledhja e te dhenave per kutiet 1, 2, and 3
for i in range(1, 4):
    collect_bundle_data(i)

# Printimi i te dhenave te mbledhura per kutite
print("Të dhënat e mbledhura për kutitë e frutave:")
for item in bundle_data:
    print(f"{item['name']}, Çmimi: {item['price']} Lek, Përshkrimi: {item['description']}")


# Plotting with Matplotlib
if bundle_data:
    fig, ax = plt.subplots(figsize=(10, 5))
    
    bundle_names = [item['name'] for item in bundle_data]
    bundle_prices = [item['price'] for item in bundle_data]

    ax.bar(bundle_names, bundle_prices, color='orange')
    ax.set_xlabel('Emri i Kutisë')
    ax.set_ylabel('Çmimi (Lek)')
    ax.set_title('Çmimet e Paketave të Frutave')

    plt.tight_layout()
    plt.show()
else:
    print("Nuk u mblodhën të dhëna për kutitë e frutave për të krijuar grafikun.")




