import random

def generate_data():
    sicaklik = round(random.uniform(20,80),2)
    basinc   = round(random.uniform(1,10),2)
    uretim   = random.randint(0,20)

    return sicaklik, basinc, uretim