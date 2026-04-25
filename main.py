from fastapi import FastAPI
from fastapi.responses import FileResponse
# Corrigido: Importando das rotas, não do controlador
from routes.livro_routes import router as livro_router

app = FastAPI()

# Integrando as rotas da camada 'routes'
app.include_router(livro_router, prefix="/api")

@app.get("/")
async def read_index():
    # Apontando para a camada de apresentação/aplicação
    return FileResponse('presentation/index.html', media_type='text/html')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)