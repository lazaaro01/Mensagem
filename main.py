import pywhatkit
phone_number = '' # Coloque qualquer número para que a mensagem seja evnviada
message = 'Isso é uma mensagem teste ' 
hours = '' # Escolha uma hora 
minutes = '' # Escolha oa minutos
pywhatkit.sendwhatmsg(phone_number, message, hours, minutes)
print('Mensagem enviada!!!')