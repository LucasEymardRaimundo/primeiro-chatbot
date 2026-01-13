import os
import streamlit as st
from google import genai

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL_NAME = "models/gemini-flash-latest"

# ---------------- CONFIGURAÇÃO ----------------
st.set_page_config(page_title="Chatbot de Materiais", layout="centered")
st.title("🤖 Atendimento – Materiais Educacionais BCV")

# ---------------- MEMÓRIA ----------------
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": (
            "Olá 👋 Sou o chatbot do professor **Marcelo Trindade**.\n\n"
            "Aqui você pode conhecer todos os nossos materiais educacionais.\n\n"
            "Digite **menu** para ver as opções disponíveis.\n\n"
            "Se tiver uma dúvida especifica conte com a nossa **IA**.\n\n"
            "👉 Ver loja completa: https://www.marcelotrindade.com/category/impressos\n\n"
        )
    }]

# ---------------- DADOS DOS MATERIAIS ----------------
MATERIAIS = {
    "1": {
        "nome": "Alfabetização BCV – Volume I",
        "imagem": "https://static.wixstatic.com/media/161cac_63da0babbd2d487885231e06017d6dee~mv2.jpeg",
        "link": "https://www.marcelotrindade.com/product-page/alabetiza%C3%A7%C3%A3o-bcv-caderno-1-impresso-frete-gr%C3%A1tis",
        "texto": """📘 **Alfabetização BCV – Volume I**

👶 Idade recomendada: a partir de 3 anos e meio  
faixa etária: entre 3 e 5 anos  

⏳ Duração média: 6 meses  
📄 Quantidade de páginas: 384 (Novas edições poderão ter até 400 páginas)

🎯 Objetivo pedagógico:
Introduzir a criança no processo de alfabetização, desenvolvendo o reconhecimento
das letras, sons e a leitura das primeiras palavras de forma gradual e lúdica.

📚 O que a criança vai aprender:
- Vogais e consoantes
- Associação letra–som (fonemas)
- Formação de sílabas simples
- Leitura de palavras básicas
- Desenvolvimento da lógica inicial

⭐ Diferenciais do material:
- Método progressivo e estruturado
- Indicado para uso diário
- Pode ser usado em casa ou na escola
- Material testado em alfabetização infantil

🖨️ Impressão:
- Frente e verso
- Totalmente colorido
- Papel 90g
- Frete grátis para todo o Brasil
"""
    },

    "2": {
        "nome": "Alfabetização BCV – Volume II",
        "imagem": "https://static.wixstatic.com/media/161cac_3187b64714d642f8bdf2307ae8254924~mv2.jpeg",
        "link": "https://www.marcelotrindade.com/product-page/alfabetiza%C3%A7%C3%A3o-bcv-caderno-ii-impresso-frete-gr%C3%A1tis",
        "texto": """📘 **Alfabetização BCV – Volume II**

👶 Idade recomendada: a partir de 4 anos  
faixa etária: entre 4 e 6 anos 

⏳ Duração média: 6 meses  
📄 Quantidade de páginas: 384 (Novas edições poderão ter até 400 páginas)

🎯 Objetivo pedagógico:
Aprimorar a leitura por meio da construção de sílabas complexas e palavras maiores,
ampliando o vocabulário da criança.

📚 O que a criança vai aprender:
- Revisão das sílabas simples
- Sílabas complexas
- Leitura de palavras longas
- Números de 1 a 10
- Lógica e atenção

⭐ Diferenciais do material:
- Evolução natural da alfabetização
- Conteúdo organizado por dificuldade
- Reforço contínuo da leitura

🖨️ Impressão:
- Frente e verso
- Totalmente colorido
- Papel 90g
- Frete grátis para todo o Brasil
"""
    },

    "3": {
        "nome": "Alfabetização BCV – Volume III",
        "imagem": "https://static.wixstatic.com/media/161cac_bffa1ae0730647e386b7adece569cfdc~mv2.jpeg",
        "link": "https://www.marcelotrindade.com/product-page/alfabetiza%C3%A7%C3%A3o-bcv-caderno-iii-frete-gr%C3%A1tis",
        "texto": """📘 **Alfabetização BCV – Volume III**

👶 Idade recomendada: a partir de 5 anos  
faixa etária: entre 5 e 7 anos  

⏳ Duração média: 6 meses  
📄 Quantidade de páginas: 384 (Novas edições poderão ter até 400 páginas)

🎯 Objetivo pedagógico:
Estimular a leitura de frases curtas e iniciar o desenvolvimento da escrita cursiva.

📚 O que a criança vai aprender:
- Sílabas complexas avançadas
- Leitura de frases
- Introdução à escrita cursiva
- Soma simples
- Interpretação básica de textos

⭐ Diferenciais do material:
- Estímulo à leitura compreensiva
- Desenvolvimento da coordenação motora

🖨️ Impressão:
- Frente e verso
- Totalmente colorido
- Papel 90g
- Frete grátis para todo o Brasil
"""
    },

    "4": {
        "nome": "Alfabetização BCV – Volume IV",
        "imagem": "https://static.wixstatic.com/media/161cac_0b66d0520c054a199d51ae51b0fe2e6a~mv2.jpeg",
        "link": "https://www.marcelotrindade.com/product-page/alfabetiza%C3%A7%C3%A3o-bcv-caderno-iv-impresso-frete-gr%C3%A1tis",
        "texto": """📘 **Alfabetização BCV – Volume IV**

👶 Idade recomendada: a partir de 6 anos  
faixa etária: entre 6 e 8 anos  

⏳ Duração média: 6 meses  
📄 Quantidade de páginas: 384 (Novas edições poderão ter até 400 páginas)

🎯 Objetivo pedagógico:
Consolidar a leitura e a escrita cursiva, ampliando a capacidade de interpretação.

📚 O que a criança vai aprender:
- Escrita cursiva completa
- Leitura de sentenças longas
- Números de 1 a 100
- Soma e subtração
- Interpretação de textos

⭐ Diferenciais do material:
- Conteúdo interdisciplinar
- Evolução contínua da alfabetização

🖨️ Impressão:
- Frente e verso
- Totalmente colorido
- Papel 90g
- Frete grátis para todo o Brasil
"""
    },

    "5": {
        "nome": "Alfabetização BCV – Volume V",
        "imagem": "https://static.wixstatic.com/media/161cac_4869345ad2d5432d853b9e17e5ffc144~mv2.jpeg",
        "link": "https://www.marcelotrindade.com/product-page/alfabetiza%C3%A7%C3%A3o-bcv-caderno-v-impresso-frete-gr%C3%A1tis",
        "texto": """📘 **Alfabetização BCV – Volume V**

👶 Idade recomendada: a partir de 7 anos  
faixa etária: entre 7 e 9 anos 

⏳ Duração média: 6 meses  
📄 Quantidade de páginas: 384 (Novas edições poderão ter até 400 páginas)

🎯 Objetivo pedagógico:
Desenvolver a interpretação de textos e a escrita de frases completas.

📚 O que a criança vai aprender:
- Leitura e interpretação de textos curtos
- Escrita cursiva de frases
- Números até 1000
- Horas e xadrez
- Geometria básica e lógica

⭐ Diferenciais do material:
- Estímulo ao raciocínio lógico
- Conteúdo mais desafiador

🖨️ Impressão:
- Frente e verso
- Totalmente colorido
- Papel 90g
- Frete grátis para todo o Brasil
"""
    },

    "6": {
        "nome": "Alfabetização BCV – Volume VI",
        "imagem": "https://static.wixstatic.com/media/161cac_adcbcf91abcf42c597807ce7f1394b85~mv2.jpeg",
        "link": "https://www.marcelotrindade.com/product-page/alabetiza%C3%A7%C3%A3o-bcv-caderno-vi-impresso-frete-gr%C3%A1tis",
        "texto": """📘 **Alfabetização BCV – Volume VI**

👶 Idade recomendada: a partir de 8 anos  
faixa etária: entre 8 e 10 anos  

⏳ Duração média: 6 meses  
📄 Quantidade de páginas: 384 (Novas edições poderão ter até 400 páginas)

🎯 Objetivo pedagógico:
Introduzir conceitos gramaticais e ampliar o domínio da língua portuguesa.

📚 O que a criança vai aprender:
- Classes gramaticais
- Uso correto dos porquês
- Homônimos e parônimos
- Uso do ábaco (soroban)
- Introdução à música e piano

⭐ Diferenciais do material:
- Base sólida em gramática
- Conteúdo interdisciplinar

🖨️ Impressão:
- Frente e verso
- Totalmente colorido
- Papel 90g
- Frete grátis para todo o Brasil
"""
    },

    "7": {
        "nome": "Alfabetização BCV – Volume VII",
        "imagem": "https://static.wixstatic.com/media/161cac_491413454eed46f18a15901b0b5d218e~mv2.jpeg",
        "link": "https://www.marcelotrindade.com/product-page/alfabetiza%C3%A7%C3%A3o-bcv-caderno-vii",
        "texto": """📘 **Alfabetização BCV – Volume VII**

👶 Idade recomendada: a partir de 8 anos  
faixa etária: entre 8 e 10 anos  

⏳ Duração média: 6 meses  
📄 Quantidade de páginas: 384 (Novas edições poderão ter até 400 páginas)
        
🎯 Objetivo pedagógico:
Aprimorar a leitura crítica, a escrita avançada e o domínio da língua portuguesa.

📚 O que a criança vai aprender:
- Interpretação de textos longos
- Ortografia e figuras de linguagem
- Escrita cursiva avançada
- Quatro operações matemáticas
- Introdução à astronomia

⭐ Diferenciais do material:
- Preparação completa para níveis avançados

🖨️ Impressão:
- Frente e verso
- Totalmente colorido
- Papel 90g
- Frete grátis para todo o Brasil
"""
    },

    "8": {
        "nome": "Matemática BCV – Volume I",
        "imagem": "https://static.wixstatic.com/media/161cac_f08b5807882243e5a8d29d2f2f4ed835~mv2.jpeg",
        "link": "https://www.marcelotrindade.com/product-page/matem%C3%A1tica-bcv-caderno-i-impresso-frete-gr%C3%A1tis",
        "texto": """📕 **Matemática BCV – Volume I**

👶 Idade recomendada: a partir de 7 anos  
faixa etária: entre 7 e 9 anos  

⏳ Duração média: 6 meses  
📄 Quantidade de páginas: 364 (Novas edições poderão ter até 400 páginas) 

🎯 Objetivo pedagógico:
Consolidar o raciocínio lógico e o domínio das quatro operações matemáticas.

📚 O que a criança vai aprender:
- Soma e subtração
- Multiplicação e divisão
- Tabuada completa
- Leitura de horas no relógio
- Números romanos

⭐ Diferenciais do material:
- Exercícios progressivos
- Desenvolvimento do raciocínio lógico

🖨️ Impressão:
- Frente e verso
- Totalmente colorido
- Papel 90g
- Frete grátis para todo o Brasil
"""
    },

    "9": {
        "nome": "Matemática BCV – Volume II",
        "imagem": "https://static.wixstatic.com/media/161cac_e2b4edef843a4dbfb6d147ed3d179d13~mv2.jpeg",
        "link": "https://www.marcelotrindade.com/product-page/matem%C3%A1tica-bcv-caderno-ii-impresso-frete-gr%C3%A1tis",
        "texto": """📕 **Matemática BCV – Volume II**

👶 Idade recomendada: a partir de 8 anos  
faixa etária: entre 8 e 10 anos 

⏳ Duração média: 6 meses  
📄 Quantidade de páginas: 364 (Novas edições poderão ter até 400 páginas) 

🎯 Objetivo pedagógico:
Desenvolver a capacidade de resolver problemas matemáticos mais complexos.

📚 O que a criança vai aprender:
- Expressões numéricas
- Expressões algébricas
- Propriedades matemáticas
- Resolução de problemas
- Abstração numérica

⭐ Diferenciais do material:
- Preparação para matemática avançada

🖨️ Impressão:
- Frente e verso
- Totalmente colorido
- Papel 90g
- Frete grátis para todo o Brasil
"""
    }
}

# ---------------- CONHECIMENTO DA IA ----------------

def base_conhecimento():
    texto = ""
    for v in MATERIAIS.values():
        texto += f"""
MATERIAL: {v['nome']}

IMAGEM_DISPONIVEL: SIM
LINK_IMAGEM: {v['imagem']}

LINK_COMPRA: {v['link']}

DESCRIÇÃO:
{v['texto']}

--------------------
"""
    return texto

def perguntar_gemini(pergunta):
    try:
        contexto = base_conhecimento()

        prompt = f"""
Você é um atendente educacional profissional e educado.

OBJETIVO:
Ajudar o cliente a encontrar informações, links e imagens dos materiais disponíveis.

REGRAS GERAIS:
- Use SOMENTE as informações fornecidas
- NÃO invente dados
- NÃO use conhecimento externo
- NÃO faça suposições

REGRAS PARA AMBIGUIDADE:
- Se a pergunta corresponder a MAIS DE UM material:
  - informe de forma educada que existem múltiplas opções
  - apresente TODOS os materiais correspondentes
  - nunca escolha apenas um quando houver mais de um

REGRAS PARA COMPRA:
- Quando o cliente demonstrar intenção de compra (ex: "quero comprar"):
  - responda de forma profissional e acolhedora
  - apresente os materiais disponíveis relacionados à pergunta
  - para cada material, informe:
    - nome
    - breve descrição (se disponível)
    - link

REGRAS PARA IMAGENS:
- SOMENTE envie imagens ou links de imagem se o cliente pedir explicitamente
- Se houver mais de um material com imagem:
  - informe isso em uma frase clara e educada
  - liste todas as imagens com o nome do material e o link
- Se houver apenas um:
  - informe que o material possui imagem
  - mostre o link da imagem

RESTRIÇÕES:
- NÃO use botões
- NÃO use markdown
- Seja objetivo, claro e profissional
- NÃO repita informações
- Se a resposta não estiver claramente nas informações, responda exatamente:
"Não possuo essa informação nos materiais disponíveis."


INFORMAÇÕES:
{contexto}

PERGUNTA DO CLIENTE:
{pergunta}
"""

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:
        return f"Erro da IA: {e}"

# ---------------- FUNÇÃO ----------------
def responder(msg):
    msg = msg.lower().strip()

    if msg == "menu":
        texto = "📚 **Materiais disponíveis:**\n\n"
        for k, v in MATERIAIS.items():
            texto += f"**{k}** - {v['nome']}\n\n"
        texto += "\n✏️ Digite o número do material."
        return {"tipo": "texto", "conteudo": texto}

    if msg in MATERIAIS:
        return {
            "tipo": "material",
            "dados": MATERIAIS[msg]
        }

    # 👉 QUALQUER OUTRA COISA → IA
    resposta_ia = perguntar_gemini(msg)
    return {"tipo": "texto", "conteudo": resposta_ia}

# ---------------- CHAT ----------------
for m in st.session_state.messages:
    with st.chat_message(m["role"]):

        st.markdown(m["content"])

        if m.get("imagem"):
            st.image(m["imagem"], use_container_width=True)

        if m.get("link"):
            st.markdown(f"🔗 [Comprar este caderno]({m['link']})")

user_input = st.chat_input("Digite 'menu' ou o número do material")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    resposta = responder(user_input)

    if resposta["tipo"] == "material":
        dados = resposta["dados"]

        with st.chat_message("assistant"):
            st.markdown(dados["texto"])  # 1️⃣ texto primeiro

            st.image(dados["imagem"], use_container_width=True)  # 2️⃣ imagem depois

            st.markdown(f"🔗 [Comprar este caderno]({dados['link']})")  # 3️⃣ link no final

        st.session_state.messages.append({
            "role": "assistant",
            "content": dados["texto"],
            "imagem": dados["imagem"],
            "link": dados["link"]
        })

    else:
        st.session_state.messages.append({
            "role": "assistant",
            "content": resposta["conteudo"]
        })

    st.rerun()
