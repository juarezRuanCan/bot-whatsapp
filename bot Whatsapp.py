#bot Whatsapp.py

#importamos la libreria y le asignamos un "alias", que en este caso es "clip"
import pyperclip as clip
#importamos la libreria "pyautogui" y le asignamos un "alias", que es "bot"
import pyautogui as bot

#importamos de la libreria "time" la funcion sleep unicamente
from time import sleep
import random

#le asignamos el valor False a esta variable para evitar que el programa se llegue a bloquear
bot.FAILSAFE = False

#esta variable, se encargara de seleccionar las respuestas correspondientes a los mensajes recibidos
def logica(msj):
	#esta es la logica, para ello se utilizan "if"
	if 'hola' in msj or 'holi' in msj or 'holis' in msj:
		#le asignamos a una variable, varias posibles respuestas
		respuestas = ['hola','hola, ¿que tal?','hola, ¿que hay?','¿que hay?']
	elif 'que tal' in msj or 'como estas' or 'como andas':
		#le asignamos a una variable, varias posibles respuestas
		respuestas = ['estoy bien','bien, gracias','muy bien']
	else:
		#en el caso de que el mensaje no sea identificado, aqui se le asigna una respuesta por defecto.
		respuestas ['lo siento, no te entendi, intenta con esto:\ntal\ntal\ntal\ntal']

	#en esta parte, seleccionamos una de las respuestas y se lo asignamos a otra variable llamada "respuesta".
	respuesta = random.choice(respuestas)
	#con la libreria pyperclip, copiamos en el portapapeles la respuesta
	clip.copy(respuesta)
	
#esta funcion sirve para reducir las probabilidades de que no identifique un mensaje por mala ortografia
#por este proceso es que en la logica de respuestas, no hay que poner los posibles mensajes recibidos con mayusculas 
#o acentos, asi reconocera mejor los mensajes recibidos

def limpiarLaFrase(msj):
	#transforma la el contenido de "msj" a minusculas
	msj = str(msj).lower()
	remplazar = (
		('á','a'),
		('é','e'),
		('í','i'),
		('ó','o'),
		('ú','u'),
	)
	#remplaza las vocales con acento por unas sin acento
	for a, b in remplazar:
		msj = msj.replace(a,b).replace(a.upper(), b.upper())
	#retorna el resultado
	return msj


def guardarMensaje():
	#da un triple click, para seleccionar todo el mensaje
	bot.tripleClick()
	#presiona control y c, para copiar el mensaje
	bot.hotkey("ctrl", 'c')
	#guarda en una varable llamada "mensaje" lo que copio 
	mensaje = clip.paste()
	#limpia el mensaje con la funcion creada arriba
	mensaje = limpiarLaFrase(mensaje)
	#retorna el valor para que sea usado por la variable de logica
	return mensaje


def enviarRespuesta():
	#movemos el cursor hacia la caja de texto de whatsapp
	bot.moveTo(955,987)
	#da un click
	bot.click()
	#presiona control y v para pegar la respuesta asignada en logica
	bot.hotkey('ctrl', 'v')
	#presiona enter para enviar el mensaje
	bot.hotkey('enter')
	#duerme el programa durante .2 segundos para evitar que envie doble mensaje
	sleep(.2)


while True:
	#inicializa una variable en True para que el bucle se repita hasta que la variable sea cambiada
	entrada=True
	while entrada:
		#definimos las coordenadas del mensaje dentro del chat
		mensaje=(721,913)
		#movemos el cursor a esas coordenadas
		bot.moveTo(mensaje)
		try:
			#dentro del try ponemos este if con la condicion de que el pixel de las coordenadas "mensaje" sea blanco
			#se mete dentro del try para evitar que de error
			if bot.pixelMatchesColor(mensaje[0],mensaje[1],(255,255,255), tolerance=10):
				#se ejecutan estas variables, creadas mas arriba
				logica(guardarMensaje())
				enviarRespuesta()
			else:
				entrada=False
		except:
			pass
	#creamos una variable coordenada a la que le asignamos en valor que retorna la funcion "locateCenterOnScreen"
	#esta funcion busca una imagen con un parecido del 85%.

	coordenadas = bot.locateCenterOnScreen('mensaje.png', confidence=.85)

	# si la funcion no retorno un valor "None", entonces posiciona el curson encima y hace un movimiento relativo 
	# hacia la izquierda para posteriormente dar click.
	if coordenadas is not None:
		bot.moveTo(coordenadas)
		bot.moveRel(-50,0)
		bot.click()


