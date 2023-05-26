from scapy.all import *

def capturar_pacotes(interface):
    sniff(iface=interface, prn=exibir_pacote)

def exibir_pacote(pacote):
    origem = pacote[IP].src
    destino = pacote[IP].dst
    protocolo = pacote[IP].proto

    if protocolo == 6:
        tipo_protocolo = 'TCP'
        porta_origem = pacote[TCP].sport
        porta_destino = pacote[TCP].dport
    elif protocolo == 17:
        tipo_protocolo = 'UDP'
        porta_origem = pacote[UDP].sport
        porta_destino = pacote[UDP].dport
    else:
        tipo_protocolo = 'Outro'

    print(f'Origem: {origem}, Destino: {destino}, Tipo de Protocolo: {tipo_protocolo}, Porta de Origem: {porta_origem}, Porta de Destino: {porta_destino}')

interface = 'en0'  # Nome da interface de rede
capturar_pacotes(interface)


#a função capturar_pacotes é usada para capturar pacotes na interface de rede especificada. A função sniff da biblioteca scapy é utilizada para isso, e o parâmetro prn é definido como a função exibir_pacote, que é responsável por exibir as informações sobre o pacote capturado.

Dentro da função exibir_pacote, as informações do pacote são extraídas usando o objeto pacote retornado pela função sniff. As informações de origem, destino e tipo de protocolo são extraídas dos cabeçalhos IP do pacote. As informações de porta de origem e destino são extraídas dos cabeçalhos TCP ou UDP, dependendo do tipo de protocolo.

Você pode ajustar o nome da interface de rede de acordo com o seu sistema operacional e as suas necessidades. O exemplo acima utiliza a interface 'en0', que é a interface padrão do macOS.
