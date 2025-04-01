# README - Aplicativo Oguru Sushi & Bar - Drinks Clássicos

## 📌 Visão Geral
Aplicativo desktop desenvolvido em Python com interface moderna para exibir receitas de drinks clássicos. Desenvolvido para o estabelecimento "Oguru Sushi & Bar", o app apresenta 20 receitas completas com modo de preparo, ingredientes e informações detalhadas.

## ✨ Funcionalidades
- **Lista completa** de 20 drinks clássicos
- **Detalhes completos** para cada drink:
  - Ingredientes com medidas em ml
  - Modo de preparo passo a passo
  - Tipo de copo recomendado
  - Guarnição sugerida
  - Características de sabor e aparência
- **Interface intuitiva** com barra lateral e área de detalhes
- **Design moderno** com cantos arredondados

## 🛠️ Tecnologias Utilizadas
- Python 3.8+
- CustomTkinter (para interface moderna)
- Pillow (para manipulação de imagens)

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8 ou superior instalado
- Pip para gerenciamento de pacotes

### Passo a Passo
1. Clone o repositório ou baixe os arquivos
   ```bash
   git clone [URL_DO_REPOSITORIO]
   cd pasta_do_projeto
   ```

2. Instale as dependências
   ```bash
   pip install customtkinter pillow
   ```

3. Execute o aplicativo
   ```bash
   python drinks_app.py
   ```

4. (Opcional) Para usar o logo personalizado:
   - Coloque o arquivo `oguru.png` na mesma pasta do script

## 🎨 Personalização
Para alterar as cores do aplicativo, modifique as variáveis no início da classe `DrinkApp`:
```python
self.bg_color = "#121212"         # Cor de fundo
self.frame_color = "#1E1E1E"      # Cor dos painéis
self.accent_color = "#4FC3F7"     # Cor de destaque (botões)
self.text_color = "#FFFFFF"       # Cor do texto
self.drink_name_color = "#000000" # Cor do texto nos botões
```

## 📝 Adicionando Novos Drinks
Para incluir novas receitas, edite o método `load_classic_drinks_data()` seguindo o modelo:

```python
{
    "name": "Nome do Drink",
    "ingredients": "Ingredientes\nSeparados por linhas",
    "instructions": "Modo de preparo\nPasso a passo",
    "glass": "Tipo de copo",
    "garnish": "Guarnição",
    "flavor": "Descrição do sabor",
    "appearance": "Descrição visual",
    "ml": 100  # Volume total em ml
}
```

## 📊 Estrutura do Projeto
```
oguru-drinks-app/
├── drinks_app.py      # Código principal
├── oguru.png          # Logo do estabelecimento (opcional)
├── README.md          # Este arquivo
└── requirements.txt   # Dependências
```

## 📜 Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## ✉️ Contato
Para dúvidas ou sugestões, entre em contato com o desenvolvedor:
- Email: Claudio.amorim.dev@gmail.com
- GitHub: @claudio-amorim

---

Desenvolvido com ❤️ para o Oguru Sushi & Bar 🍣🍸
