#A função ping recebe um endereço IP ou nome de host como entrada e envia um pacote ICMP para o destino. Em seguida, a resposta é exibida, mostrando o tempo de resposta em milissegundos.

import ping3

def ping(host):
    try:
        delay = ping3.ping(host)
        if delay is not None:
            print(f'Resposta de {host}: tempo = {delay:.4f}ms')
        else:
            print(f'Não foi possível alcançar o host {host}.')
    except ping3.errors.PingError as e:
        print(f'Um erro ocorreu: {e}')

host = input("Digite o endereço IP ou nome do host: ")
ping(host)


