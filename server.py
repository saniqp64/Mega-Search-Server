import asyncio

CURRENT_VERSION = "0.1"  #Используем строку для корректного сравнения

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Подключен: {addr}")

    try:
        data = await reader.read(1024)
        version = data.decode().strip()

        if version != CURRENT_VERSION:
            writer.write(b"update")
        else:
            writer.write(b"ok")
        
        await writer.drain() #Ждем отправки данных
    finally:
        writer.close()
        await writer.wait_closed()

async def main():
    #Запускаем сервер на всех интерфейсах (0.0.0.0) или конкретном IP
    server = await asyncio.start_server(handle_client, '192.168.100.3', 8080)

    addr = server.sockets[0].getsockname()
    print(f'Сервер запущен на {addr}')

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass