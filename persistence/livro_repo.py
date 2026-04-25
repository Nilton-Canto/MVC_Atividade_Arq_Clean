# persistence/livro_repo.py
import os
from models.livro_model import Livro


class LivroRepository:
    # Aponta para o arquivo que criamos na raiz
    ARQUIVO = "banco_livros.txt"

    @classmethod
    def _ler_arquivo(cls):
        """Método interno para ler o TXT e converter em objetos."""
        livros = []
        if not os.path.exists(cls.ARQUIVO):
            return livros

        with open(cls.ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    # Separa os dados pelo ponto e vírgula
                    id_str, titulo, preco_str, sinopse = linha.split(";")
                    # Instancia a entidade pura do Model
                    livro = Livro(int(id_str), titulo, float(preco_str), sinopse)
                    livros.append(livro)
        return livros

    @classmethod
    def buscar_todos(cls):
        return cls._ler_arquivo()

    @classmethod
    def filtrar_por_titulo(cls, termo: str):
        livros = cls._ler_arquivo()
        termo = termo.lower()
        return [l for l in livros if termo in l.titulo.lower()]

    @classmethod
    def buscar_por_id(cls, livro_id: int):
        livros = cls._ler_arquivo()
        for l in livros:
            if l.id == livro_id:
                return l
        return None