import time
from datetime import datetime, timedelta

from telethon.sync import TelegramClient
from telethon.tl.types import PeerChannel
from app.configurations.ApiAuth import API_ID, API_HASH, CHANNEL_ID


with TelegramClient('TelegramClient - Scrapping Message', API_ID, API_HASH) as client:
    # Linha de código puramente por estética, odeio quando o Python perde o typeHint.
    client: TelegramClient = client
    scrapping_group = client.get_entity(PeerChannel(CHANNEL_ID))

    print('♾️  Início da coleta de dados. A verificação será periódica a partir desse ponto. Se atente as mensagens.\n')

    while True:
        messages = client.get_messages(scrapping_group, 5)

        # Intera sobre cada mensagem obtida com a linha de código acima.
        for message in messages:
            if "⚪" in message.message:
                # Linha de código puramente por estética, odeio quando o Python perde o typeHint.
                message: str = message.message

                # Obtenho a posição de início da bola branca com o horário;
                # Então eu obtenho a última ocorrência e somo com a posição do horário.
                start, end = message.index('⚪'), message.rindex('⚪') + 6

                # Por fim removo a bola branca da string e a transformo em um array.
                message = message[start:end].replace('⚪', '').split()

                times_in  = [datetime.strptime(time, '%H:%M')
                            for time in message]
                times_out = []

                # Área onde verificamos se algum horário do sinal já não foi ultrapassado;
                # Caso algum sinal tenha sido ultrapassado — ele é inserido na lista de remoção.
                for v in times_in:
                    time_now = datetime.now().strftime('%H:%M')

                    if time_now >= v.strftime('%H:%M'):
                        moment = v.strftime('%H:%M')
                        times_out.insert(0, v)
                        print(f'⚠️  O horário de entrada para às \033[31m{moment}\033[0;0m passou.')

                for moment in times_out:
                    times_in.remove(moment)

                while times_in:
                    time_now = datetime.now() + timedelta(minutes=1)
                    time_now = time_now.strftime("%H:%M")
                    time_target = times_in[0].strftime("%H:%M")

                    if time_now == time_target:
                        # Inserir a parte da lógica do disparo de opção de compra aqui.

                        print(
                            f'\n✅ Entrada \033[32mconcluída\033[0;0m para o sinal do horário \033[32m{time_target}\033[0;0m.\n')
                        times_in.pop(0)
                        continue

                    # A cada vinte segundos verificará se se está na hora de fazer a entrada
                    # enquanto a lista não estiver vazia.
                    times_remains = [time.strftime("%H:%M") for time in times_in]
                    print(
                        f'\n⌛ Aguardando o horário de \033[31m{time_target}\033[0;0m para próxima entrada.\nAs próximas estradas serão em: \033[33m{times_remains}\033[0;0m')
                    time.sleep(20)

                print(
                    '\n✅ Todos os horários de entradas do sinal da última mensagem válida foram ultrapassados.\n')

        # Aguarda dez segundos antes de obter a próxima mensagem;
        print(
            '⌛ Aguardando a próxima mensagem com os horários dos sinais antes da execução do programa. Próxima verificação em vinte segundos.')
        time.sleep(20)
