from Connection import fileWrite
def getData():
    ad=input('Adinizi daxil edin :')
    soyad=input('Soyadinizi daxil edin :')
    return {
        'ad':ad,
        'soyad':soyad
    }

def addWrite():
    for i in range(5):
        print(f'{i}')
        userData=getData()
        
        fileWrite.write(
            f"""
            Telebenin adi : {userData['ad']} , Telebenin soyadi : {userData['soyad']}
            """
        )

addWrite()


