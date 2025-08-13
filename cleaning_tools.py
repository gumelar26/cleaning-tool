file = open('pendaftaran.log')
output = open('pendaftaran.csv', 'w')

def process_data() :
    for line in file:
        bagian = line.split(" | ")
        tanggal = bagian[0].replace('"',"")
        email = bagian[1]
        kota = bagian[2].lower()
        status = bagian[3].replace('"\n',"")
        
        if email.endswith('.com') != True:
            if email.endswith('.COM') != True:
                email = email + '.com'
        
        print(f'{tanggal},{email},{kota},{status}')
        output.write(f'{tanggal},{email},{kota},{status}\n')

    file.close()
    output.close()

process_data()