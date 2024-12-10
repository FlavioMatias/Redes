# Modelo OSI (Open Systems Interconnection)

## Introdução
O modelo OSI (Open Systems Interconnection) é um framework teórico que define como sistemas de redes se comunicam. Ele foi criado pela ISO (International Organization for Standardization) e é dividido em **sete camadas**, cada uma com funções específicas para a comunicação de dados.

## As Sete Camadas do Modelo OSI

### 1. **Camada Física**
- **Função:** Responsável pela transmissão de sinais brutos (elétricos, ópticos ou de rádio) através do meio físico.
- **Exemplos de Tecnologia:** Cabos Ethernet, conectores, fibras ópticas, sinais de rádio.
- **Exemplo de Uso:** Conversão de dados em sinais transmitidos por cabos ou ondas de rádio.

### 2. **Camada de Enlace de Dados**
- **Função:** Assegura que os dados sejam transmitidos sem erros entre dois dispositivos conectados diretamente.
- **Protocolos e Tecnologias:** Ethernet, Wi-Fi (IEEE 802.11), PPP.
- **Exemplo de Uso:** Detecção e correção de erros em uma rede local.

### 3. **Camada de Rede**
- **Função:** Realiza o roteamento e o endereçamento lógico dos pacotes de dados entre redes diferentes.
- **Protocolos:** IPv4, IPv6, ICMP, ARP.
- **Exemplo de Uso:** Determinar o melhor caminho para entregar dados em uma rede global como a Internet.

### 4. **Camada de Transporte**
- **Função:** Garante a entrega confiável ou rápida dos dados entre dispositivos.
- **Protocolos:** TCP, UDP.
  - **TCP:** Conexão confiável, controle de fluxo, segmentação e reordenação.
  - **UDP:** Entrega rápida, mas sem confiabilidade.
- **Exemplo de Uso:** Streaming de vídeos (UDP) e downloads (TCP).

### 5. **Camada de Sessão**
- **Função:** Estabelece, gerencia e encerra sessões de comunicação entre dispositivos.
- **Protocolos:** NetBIOS, RPC.
- **Exemplo de Uso:** Manutenção de uma conexão ativa durante uma transferência de arquivos.

### 6. **Camada de Apresentação**
- **Função:** Realiza tradução, compressão e criptografia dos dados para torná-los compreensíveis ao aplicativo.
- **Exemplos:** SSL/TLS para criptografia, conversão de formatos como JPEG ou PNG.
- **Exemplo de Uso:** Criptografar dados enviados em um site seguro (HTTPS).

### 7. **Camada de Aplicação**
- **Função:** Proporciona serviços diretamente aos aplicativos e usuários finais.
- **Protocolos:** HTTP, FTP, SMTP, DNS.
- **Exemplo de Uso:** Navegação na web, envio de e-mails.

## Resumo das Camadas do OSI

| Camada            | Função Principal                           | Exemplos de Protocolos/Tecnologias     |
|-------------------|-------------------------------------------|----------------------------------------|
| Física            | Transmissão de sinais brutos              | Ethernet, sinais de rádio             |
| Enlace de Dados   | Comunicação entre dispositivos locais      | Ethernet, Wi-Fi                       |
| Rede              | Roteamento e endereçamento lógico         | IPv4, IPv6, ICMP                      |
| Transporte        | Entrega confiável ou rápida               | TCP, UDP                              |
| Sessão            | Gerenciamento de sessões de comunicação   | NetBIOS, RPC                          |
| Apresentação      | Tradução, compressão e criptografia        | SSL/TLS, formatos de dados            |
| Aplicação         | Serviços para usuários e aplicativos       | HTTP, FTP, DNS, SMTP                  |

## Diferenças entre OSI e TCP/IP
Embora ambos sejam modelos de referência, o OSI é mais detalhado e usado como guia teórico, enquanto o TCP/IP é amplamente utilizado na prática. Uma diferença importante é o número de camadas: o OSI possui **sete camadas**, enquanto o TCP/IP possui **cinco camadas**.

### Por que o OSI tem 7 camadas e o TCP/IP apenas 5?
- **Modelo OSI:**
  - Foi projetado como um guia teórico para descrever todos os aspectos possíveis da comunicação em redes.
  - As camadas de **Sessão** e **Apresentação** foram criadas para lidar com funcionalidades específicas, como controle de sessões e tradução de dados, que nem sempre são necessárias ou tratadas separadamente no TCP/IP.

- **Modelo TCP/IP:**
  - Foi desenvolvido com foco na prática e simplificação.
  - As funções das camadas de Sessão e Apresentação foram incorporadas nas camadas de Aplicação e Transporte, reduzindo o número total de camadas.
  - É mais adequado para implementar diretamente os protocolos da Internet, como HTTP, TCP e IP.

| Modelo OSI        | Modelo TCP/IP          |
|-------------------|------------------------|
| 7 camadas         | 5 camadas             |
| Inclui Sessão e Apresentação | Não inclui essas camadas |
| Mais teórico       | Mais prático          |
