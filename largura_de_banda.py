#Para monitorar a largura de banda da rede e exibir os resultados em gráficos, podemos utilizar a biblioteca psutil para obter informações sobre o tráfego de rede e a biblioteca matplotlib para gerar os gráficos. Certifique-se de ter essas bibliotecas instaladas antes de executar o código. Você pode instalá-las usando os comandos pip install psutil e pip install matplotlib.


import psutil
import matplotlib.pyplot as plt
import time

def monitorar_largura_banda(intervalo_segundos, duracao_segundos):
    tempos = []
    envio_bytes = []
    recebimento_bytes = []

    tempo_inicial = time.time()
    tempo_final = tempo_inicial + duracao_segundos

    while time.time() < tempo_final:
        tempo_atual = time.time() - tempo_inicial
        tempos.append(tempo_atual)
        
        estatisticas = psutil.net_io_counters()
        envio_bytes.append(estatisticas.bytes_sent)
        recebimento_bytes.append(estatisticas.bytes_recv)

        time.sleep(intervalo_segundos)

    plt.plot(tempos, envio_bytes, label='Envio')
    plt.plot(tempos, recebimento_bytes, label='Recebimento')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Bytes')
    plt.title('Monitor de largura de banda da rede')
    plt.legend()
    plt.show()

intervalo_segundos = 1  # Intervalo entre as medições em segundos
duracao_segundos = 10  # Duração total do monitoramento em segundos

monitorar_largura_banda(intervalo_segundos, duracao_segundos)


#Neste exemplo, a função monitorar_largura_banda recebe dois parâmetros: intervalo_segundos, que define o intervalo entre as medições, e duracao_segundos, que determina a duração total do monitoramento.

Dentro da função, um loop é executado durante o tempo especificado. Em cada iteração do loop, as estatísticas de tráfego de rede são obtidas usando a função psutil.net_io_counters(), e os valores de bytes enviados e recebidos são armazenados em listas.

Após o loop, os gráficos são gerados usando a biblioteca matplotlib. Os tempos são plotados no eixo x, enquanto os bytes enviados e recebidos são plotados nos eixos y. Os gráficos são exibidos usando a função plt.show().

Você pode ajustar os valores de intervalo_segundos e duracao_segundos de acordo com as suas necessidades. O exemplo acima monitora a largura de banda da rede por 10 segundos, com medições a cada 1 segundo.
