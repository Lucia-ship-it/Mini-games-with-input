def percenta_HO():
    w=int(input('Hodiny odpracované celkom: '))
    ho= int(input('Hodiny odpracované z domu: '))
    
    print(f'\nZa mesiac máš odpracované {ho*100/w:.2f} % z home office')
    print(f'A to je {100-(ho*100/w):.2f} % práce v kancelárii')

    office = 100-(ho*100/w)
    
    if office > 50:
        print(f'\n--> Výborne, je to v poriadku 😊')
    else:
        print(f'\n--> Treba ísť do kanclu!😎')
        
percenta_HO()
