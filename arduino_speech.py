import serial.tools.list_ports
import serial
import speech_recognition as sr

# Función para obtener el puerto COM seleccionado
def get_selected_port(val):
    ports = serial.tools.list_ports.comports()
    ports_list = []

    for port in ports:
        ports_list.append(str(port))

    for port_str in ports_list:
        if port_str.startswith(f'COM{val}'):
            return f'COM{val}'
    
    return None

# Configurar la conexión serial
serial_inst = serial.Serial()
serial_inst.baudrate = 9600

# Obtener el puerto COM seleccionado
while True:
    val = input('Select Port (e.g., 3 for COM3): ')
    port_var = get_selected_port(val)
    if port_var:
        break
    else:
        print("Invalid port. Please select a valid COM port.")

serial_inst.port = port_var
serial_inst.open()

# Definir el diccionario Morse
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', 
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', 
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', 
    ' ': '/'
}

# Función para convertir texto a Morse
def text_to_morse(text):
    morse_word = ""
    for char in text:
        if char in morse_dict:
            morse_word += morse_dict[char] + " "
    return morse_word

# Obtener la entrada de voz y enviar Morse a través del puerto serial
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Hable algo...")
    while True:
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio).upper()
            print("Texto reconocido:", text)
            morse_word = text_to_morse(text)
            print("Morse:", morse_word)
            serial_inst.write(morse_word.encode('utf-8'))
        except sr.UnknownValueError:
            print("No se pudo entender el audio. Intente nuevamente.")
        except sr.RequestError as e:
            print("Error en la solicitud:", str(e))
