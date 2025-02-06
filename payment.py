import qrcode  

# Taking UPI ID as input  
upi_id = input("Enter Your UPI ID: ")  

# Define UPI URLs  
Phonepe_url = f'upi://pay?pa={upi_id}&pn=Recpient%20Name&mc=1234'
Paytm_url = f'upi://pay?pa={upi_id}&pn=Recpient%20Name&mc=1234'
Googlepay_url = f'upi://pay?pa={upi_id}&pn=Recpient%20Name&mc=1234'
Supermoney_url = f'upi://pay?pa={upi_id}&pn=Recpient%20Name&mc=1234'

# Create QR codes  
qr_phonepe = qrcode.make(Phonepe_url)  
qr_googlepay = qrcode.make(Googlepay_url)  
qr_paytm = qrcode.make(Paytm_url)  
qr_supermoney = qrcode.make(Supermoney_url)  

# Save QR codes as images  
qr_phonepe.save('phonepe_qr.png')  
qr_googlepay.save('googlepay_qr.png')  
qr_paytm.save('paytm_qr.png')  
qr_supermoney.save('supermoney_qr.png')  

# Display QR codes  
qr_phonepe.show()  
qr_googlepay.show()  
qr_paytm.show()  
qr_supermoney.show()  
