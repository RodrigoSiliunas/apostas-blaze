import time
from datetime import datetime, timedelta

from telethon.sync import TelegramClient
from telethon.tl.types import PeerChannel
from app.configurations.ApiAuth import API_ID, API_HASH, CHANNEL_ID

with TelegramClient(CHANNEL_ID, API_ID, API_HASH) as client:
    # Linha de código puramente por estética, odeio quando o Python perde o typeHint.
    client: TelegramClient = client
    scrapping_group = client.get_entity(PeerChannel(1531006312))

    while True:
        messages = client.get_messages(scrapping_group, 1)

        # Intera sobre cada mensagem obtida com a linha de código acima.
        for message in messages:
            if "⚪" in message.message:
                # Linha de código puramente por estética, odeio quando o Python perde o typeHint.
                message: str = message.message

                # Obtenho a posição de início da bola branca com o horário;
                # Então eu obtenho a última ocorrência e somo com a posição do horário.
                start, end = message.index('⚪'), message.rindex('⚪') + 6

                # Por fim removo a bola branca da string e a transformo em um array.
                message = message[start:end].replace('⚪', '')
                times_in = message.split()

                while times_in:
                    time_now = datetime.now() + timedelta(minutes=1)
                    time_now = time_now.strftime("%H:%M")

                    if time_now == times_in[0]:
                        # Inserir a parte da lógica do disparo de opção de compra aqui.

                        times_in.pop(0)

                    # A cada dez segundos verificará se se está na hora de fazer a entrada
                    # enquanto a lista não estiver vazia. 
                    time.sleep(10)

        # Aguarda dez segundos antes de obter a próxima mensagem;
        time.sleep(10)
