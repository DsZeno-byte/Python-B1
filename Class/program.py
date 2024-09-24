import os
address=r"C:\Users\sanwa\Desktop\Python 2024"
dir=os.listdir(address)
folder=os.path.join(address,'Images')
for file_name in dir:
    if file_name.lower().endswith('.png'):
        if not os.path.exists(folder):
            os.mkdir(folder)
            print("Folder %s Created!"%folder)
        else:
            print("Folder already %s Created!"%folder)
