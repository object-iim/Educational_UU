import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    await asyncio.sleep(0.5) # для красоты, чтобы силачи начали соревнования одновременно
    for numer in range(1, 6):
        print(f'Силач {name} поднял {numer}')
        await asyncio.sleep(8/power)
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Александр', 4))
    task_2 = asyncio.create_task(start_strongman('Саша', 13))
    task_3 = asyncio.create_task(start_strongman('Шура', 20))
    await task_1
    await task_2
    await task_3

asyncio.run(start_tournament())