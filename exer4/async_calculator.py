import asyncio 

async def async_add(a, b): 
    """Addition asynchrone avec délai simulé""" 
    await asyncio.sleep(0.1) 
    return a + b 
async def async_multiply(a, b): 
    """Multiplication asynchrone avec délai simulé""" 
    await asyncio.sleep(0.2) 
    return a * b 
async def calculate_complex(a, b, c): 
    """Calcul complexe utilisant les fonctions async""" 
    sum_result = await async_add(a, b) 
    final_result = await async_multiply(sum_result, c) 
    return final_result 