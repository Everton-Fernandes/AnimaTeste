# AnimaTeste - Exibição de Eventos com Microsoft Graph API (Python)

Este projeto é uma aplicação em Python que exibe os próximos eventos do calendário do Microsoft 365, utilizando dados de exemplo ou consumindo a API Microsoft Graph, e apresenta uma interface mock no estilo Microsoft Teams.

---

## 📋 Descrição

- A aplicação lê eventos de um arquivo JSON local (`sample_events.json`) para simular a lista de próximos eventos.
- Opcionalmente, pode consumir a API Microsoft Graph real para obter eventos do calendário do usuário, usando um token de acesso (`GRAPH_TOKEN`) fornecido via variável de ambiente.
- O projeto inclui um mock HTML estilizado para simular uma aba do Microsoft Teams com os eventos exibidos de forma amigável e responsiva.
- Tem foco em ser facilmente extensível para futura integração real como aba do Teams.

---

## 🚀 Como executar

### Pré-requisitos

- Python 3.8+ instalado
- `pip` para instalar dependências
- (Opcional) Token válido do Microsoft Graph API (veja abaixo)

### Passos

1. Clone este repositório:

   ```bash
   git clone https://github.com/Everton-Fernandes/AnimaTeste.git
   cd AnimaTeste

   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt

   ```

3. Configure a variável de ambiente para usar a API Microsoft Graph:

- Obtenha um token válido no Graph Explorer (login com sua conta Microsoft).

- No terminal:

- Windows PowerShell:

  ```powershell
  $env:GRAPH_TOKEN="seu_token_aqui"

  ```

- Linux/macOS:
  ```bash
  export GRAPH_TOKEN="seu_token_aqui"
  ```

4. Execute a aplicação Python:

   ```bash
   python app/main.py

   ```

5. A aplicação exibirá os próximos eventos formatados em tabela no console.

## 🛠 Decisões técnicas

- Linguagem Python: escolhida pela facilidade na manipulação de JSON, requisições HTTP e variáveis de ambiente, além da simplicidade para demonstrar a solução rapidamente.

- Uso do arquivo JSON local: para garantir funcionamento básico e offline, essencial para o baseline do teste (fornecido).

- Integração com Microsoft Graph API: feita via requisição HTTP GET com token OAuth Bearer, retirado da variável de ambiente GRAPH_TOKEN, para manter segurança e evitar exposição de tokens no código.

- Apresentação dos dados: uso da biblioteca tabulate para exibir uma tabela legível no console.

- Mock de interface web: arquivo HTML estilizado no padrão Microsoft Teams com ícones, pronto para futura integração real como aba do Teams.

## 🔜 Possíveis melhorias / próximos passos

- Implementar backend web simples (ex: Flask) para servir dados via API REST e integrar com frontend mock via AJAX.

- Publicar o app como aba real no Microsoft Teams usando manifest e hospedagem segura.

- Aprimorar a interface visual com frameworks como React e Fluent UI.

- Incluir testes automatizados para garantir qualidade.

## 📄 Licença

Este projeto está aberto para uso e modificação conforme sua necessidade.
