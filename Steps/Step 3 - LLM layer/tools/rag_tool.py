from pydantic_ai import Agent, RunContext

async def rag_tool_router(ctx: RunContext[None], data_to_retrieve: str) -> dict:
    """
        Herramienta: obtiene información relevante de la BBDD.

        Ejecuta un agente que crea las distintas consultas SQL para obtener la información solicitada de la BBDD.

        Args:
            ctx: Estado del agente.
            data_to_retrieve: La información solicitada.

        Returns:
            dict: Un diccionario que contiene la información requerida y las consultas lanzadas.
    """

    chunks = []

    # Insert the similar chunks into text
    retrieved_text = """"""
    for i, c in enumerate(chunks):
        retrieved_text += f"[{i+1}] {c['file']}, page {c['page']}, block: {c['block']}\n{c['chunk']}\n\n" 
        
        return retrieved_text
    
    return {'data': 'Test_data', 'SQL': 'SELECT * FROM precio_vivienda_2024'}

    