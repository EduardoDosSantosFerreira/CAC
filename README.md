# README.md

```markdown
# CAC - Crow Auto Clicker 🐦

![CAC Logo](cac.png)

Um auto clicker automático e elegante com interface moderna e tema escuro. Perfeito para automação de cliques em jogos, testes ou qualquer tarefa repetitiva.

## ✨ Características

- 🎯 **Captura de posição** - Capture a posição exata onde deseja clicar
- ⚡ **Atalhos de teclado** - Controle total sem precisar do mouse
- 🎨 **Interface elegante** - Design moderno com tema escuro
- 📊 **Contador visual** - Acompanhe quantos cliques foram executados
- ⏱️ **Intervalo ajustável** - De 0.1s a 10s entre cliques
- 🛑 **Parada de emergência** - Tecla ESC para parar imediatamente
- 🖱️ **Monitor de posição** - Veja a posição atual do mouse em tempo real

## 📸 Screenshots

*[Adicione screenshots da sua aplicação aqui]*

## 🎮 Como Usar

### Atalhos de Teclado

| Tecla | Função | Descrição |
|-------|--------|-----------|
| `F3` | Capturar | Captura a posição atual do mouse |
| `F2` | Iniciar/Parar | Inicia ou para os cliques automáticos |
| `ESC` | Emergência | Para imediatamente todos os cliques |

### Interface

1. **Posição do Mouse** - Mostra as coordenadas X e Y atuais
2. **Capturar Posição** - Clique no botão ou use F3 para capturar
3. **Intervalo** - Ajuste o tempo entre cliques (0.1s a 10s)
4. **Contador** - Mostra quantos cliques foram executados
5. **Botão Iniciar** - Começa os cliques automáticos na posição capturada

## 🔧 Instalação

### Opção 1: Executável (Recomendado)

1. Baixe a última versão em [Releases](link-para-releases)
2. Execute o arquivo `CAC.exe`
3. Pronto! Não precisa instalar nada

### Opção 2: Código Fonte

#### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

#### Passos

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/cac.git
cd cac
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o programa:
```bash
python main.py
```

## 📦 Dependências

```
PySide6>=6.5.0
keyboard>=0.13.5
pyautogui>=0.9.54
winsound (biblioteca padrão)
```

## 🚀 Gerando Executável

Para gerar seu próprio executável com ícone:

1. Instale as ferramentas necessárias:
```bash
pip install pyinstaller pillow
```

2. Execute o script de build:
```bash
python build_exe.py
```

Ou use o comando direto:
```bash
pyinstaller --name="CAC" --windowed --icon=cac.ico --add-data="cac.png;." --noconsole --onefile main.py
```

O executável será gerado na pasta `dist/`

## 📁 Estrutura do Projeto

```
CAC/
├── main.py              # Interface gráfica principal
├── logic.py             # Lógica do clicker
├── cac.png              # Ícone/logo do programa
├── cac.ico              # Ícone para o executável
├── build_exe.py         # Script para gerar executável
├── requirements.txt     # Dependências do projeto
└── README.md           # Este arquivo
```

## 🎯 Como Funciona

1. O programa monitora a posição do mouse em tempo real
2. Você captura uma posição específica (ou usa a posição atual)
3. Ajusta o intervalo entre cliques
4. Ao iniciar, o programa clica automaticamente na posição capturada
5. O contador mostra quantos cliques foram executados
6. Pode parar a qualquer momento com F2 ou ESC

## ⚠️ Avisos

- **Use com responsabilidade** - Não use para atividades maliciosas
- **Jogos online** - Verifique as regras do jogo antes de usar
- **Administrador** - Em alguns sistemas, pode precisar executar como administrador

## 🛠️ Personalização

### Cores e Estilo
O tema escuro pode ser personalizado no método `aplicar_estilo_escuro()` em `main.py`

### Intervalo de Cliques
O intervalo padrão pode ser alterado em:
```python
self.intervalo_spin.setValue(1.8)  # Altere para o valor desejado
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Siga estes passos:

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🙏 Agradecimentos

- [PySide6](https://wiki.qt.io/Qt_for_Python) - Framework GUI
- [keyboard](https://github.com/boppreh/keyboard) - Atalhos de teclado
- [PyAutoGUI](https://github.com/asweigart/pyautogui) - Automação de cliques

## 📊 Versão

**Versão Atual:** 1.0.0

### Histórico de Versões

- **1.0.0** (2024)
  - Versão inicial
  - Interface com tema escuro
  - Captura de posição
  - Cliques automáticos
  - Atalhos de teclado

## 🐛 Problemas Conhecidos

- Em alguns sistemas, pode ser necessário executar como administrador para capturar certos tipos de janela
- O atalho ESC pode não funcionar se outro programa estiver usando o hook de teclado

---

**Desenvolvido com ❤️ para facilitar sua vida**
```

## Arquivo requirements.txt

Crie também um arquivo `requirements.txt`:

```txt
PySide6>=6.5.0
keyboard>=0.13.5
pyautogui>=0.9.54
pillow>=9.0.0
```

## Arquivo .gitignore

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
env.bak/
venv.bak/

# PyInstaller
*.spec
build/
*.exe
*.ico

# IDE
.vscode/
.idea/
*.swp
*.swo

# Logs
*.log
```

Este README.md fornece:
- Visão geral do projeto
- Instruções de instalação
- Como usar
- Screenshots (espaço reservado)
- Estrutura do projeto
- Como contribuir
- Licença
- Informações de contato
- Histórico de versões