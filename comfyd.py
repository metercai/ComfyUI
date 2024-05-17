import threading
import asyncio
import logging

def main():
    # 初始化日志记录
    logging.basicConfig(level=logging.INFO)

    # 创建事件循环
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # 创建服务器实例
    server = create_server()

    # 启动服务器
    loop.run_until_complete(server.start())

    # 运行事件循环
    try:
        loop.run_forever()
    finally:
        loop.close()

def run_comfy_server():
    main()

# 创建一个新的线程来运行Comfy服务器
threading.Thread(target=run_comfy_server).start()

