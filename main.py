import sys
from multiprocessing import Process

from channels.telegram_bot import run as run_telegram
from channels.whatsapp_bot import run as run_whatsapp


def main():
    # se passar argumento, roda so o canal escolhido
    arg = sys.argv[1].lower() if len(sys.argv) > 1 else "todos"

    if arg == "telegram":
        run_telegram()
        return
    if arg == "whatsapp":
        run_whatsapp()
        return

    # sem argumento: roda os dois em processos separados
    processos = [
        Process(target=run_telegram, name="telegram"),
        Process(target=run_whatsapp, name="whatsapp"),
    ]

    for p in processos:
        p.start()
        print(f"[main] processo '{p.name}' iniciado (pid {p.pid})")

    try:
        for p in processos:
            p.join()
    except KeyboardInterrupt:
        print("\n[main] encerrando...")
        for p in processos:
            p.terminate()

if __name__ == "__main__":
    main()