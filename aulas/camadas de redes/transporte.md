# Camada de Transporte

## Introdução
A camada de transporte é uma das partes mais importantes do modelo TCP/IP e do modelo OSI. Sua principal função é garantir que os dados sejam transferidos de forma confiável, ordenada e eficiente entre dispositivos conectados em uma rede. Essa camada é responsável por gerenciar a comunicação extremo a extremo, sendo essencial para a interação entre aplicações em diferentes sistemas.

---

## Funções Principais

1. **Multiplexação e Demultiplexação**
   - Permite que várias aplicações utilizem a mesma conexão de rede simultaneamente, identificando-as por meio de números de porta.
   
2. **Controle de Fluxo**
   - Regula a taxa de envio de dados para evitar que o receptor seja sobrecarregado.

3. **Controle de Erros**
   - Garante que os dados sejam entregues corretamente, retransmitindo pacotes perdidos ou corrompidos.

4. **Controle de Conexão**
   - Estabelece, gerencia e encerra conexões entre os dispositivos de forma confiável.

5. **Segmentação e Reordenação**
   - Divide os dados em segmentos menores para transmissão e garante que eles sejam remontados na ordem correta no destino.

---

## Protocolos Principais

### 1. **TCP (Transmission Control Protocol)**
- **Função:** Protocolo orientado à conexão que garante entrega confiável e ordenada dos dados.
- **Características:**
  - Controle de erro e fluxo.
  - Conexão estabelecida por meio de um handshake de três vias.
  - Retransmissão de segmentos perdidos.
- **Aplicações Típicas:**
  - Navegação na web (HTTP/HTTPS).
  - Transferência de arquivos (FTP).
  - E-mails (SMTP, IMAP).

### 2. **UDP (User Datagram Protocol)**
- **Função:** Protocolo sem conexão que prioriza velocidade sobre confiabilidade.
- **Características:**
  - Não realiza controle de erro ou fluxo.
  - Adequado para aplicações em tempo real.
- **Aplicações Típicas:**
  - Streaming de vídeo e áudio.
  - Jogos online.
  - DNS e DHCP.

---

## Comparação Entre TCP e UDP

| Característica         | TCP                                | UDP                            |
|-------------------------|------------------------------------|--------------------------------|
| Tipo de Conexão        | Orientado à conexão              | Sem conexão                  |
| Confiabilidade          | Alta                              | Baixa                         |
| Controle de Fluxo       | Sim                               | Não                          |
| Retransmissão de Dados  | Sim                               | Não                          |
| Velocidade              | Mais lento                        | Mais rápido                  |
| Uso Típico             | Transferência de arquivos, e-mails | Streaming, jogos, DNS         |

---

## Números de Porta
A camada de transporte utiliza **números de porta** para identificar aplicações específicas em um dispositivo. Existem três intervalos principais:

1. **Portas Bem Conhecidas (0 a 1023):** Reservadas para serviços e protocolos conhecidos (ex.: HTTP - porta 80, HTTPS - porta 443).
2. **Portas Registradas (1024 a 49151):** Usadas por aplicações de terceiros (ex.: jogos online).
3. **Portas Dinâmicas ou Privadas (49152 a 65535):** Atribuídas dinamicamente a aplicativos em tempo de execução.

---

## Exemplo de Funcionamento
Quando você acessa um site:
1. Seu navegador (cliente) escolhe um número de porta dinâmico.
2. Ele se comunica com o servidor na porta 80 (HTTP) ou 443 (HTTPS).
3. A camada de transporte usa TCP para garantir que os dados sejam entregues corretamente.
