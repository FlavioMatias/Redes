# Protocolo TCP/IP e Suas Camadas

## Introdução
O TCP/IP (Transmission Control Protocol/Internet Protocol) é o conjunto de protocolos usado na comunicação em redes de computadores, incluindo a Internet. Ele organiza a transmissão de dados em camadas, cada uma com funções específicas.

## Camadas do Modelo TCP/IP
O modelo TCP/IP possui **cinco camadas principais**, que mapeiam de forma funcional as responsabilidades da comunicação de dados. Essas camadas são:

### 1. **Camada de Aplicação**
- **Função:** Proporciona serviços diretamente aos aplicativos e usuários finais, permitindo a comunicação entre dispositivos.
- **Protocolos:** HTTP, HTTPS, FTP, SMTP, DNS, POP3, IMAP.
- **Exemplo de Uso:** Navegação em sites (HTTP/HTTPS) e envio de e-mails (SMTP).

### 2. **Camada de Transporte**
- **Função:** Garante a entrega confiável e ordenada dos dados entre os dispositivos.
- **Protocolos:** TCP, UDP.
  - **TCP (Transmission Control Protocol):** Conexão confiável, controle de erros, segmentação e reordenação.
  - **UDP (User Datagram Protocol):** Transmissão rápida, mas sem confiabilidade.
- **Exemplo de Uso:** Streaming de vídeos (UDP) e downloads de arquivos (TCP).

### 3. **Camada de Rede**
- **Função:** Responsável pelo roteamento dos dados entre redes diferentes e pela identificação dos dispositivos através de endereços IP.
- **Protocolos:** IP (IPv4, IPv6), ICMP, ARP, RARP.
- **Exemplo de Uso:** Comunicação entre dispositivos de redes diferentes usando endereços IP.

### 4. **Camada de Enlace de Dados (ou Acesso à Rede)**
- **Função:** Define como os dados são transmitidos fisicamente através da rede. Trata dos aspectos de hardware, como cabos, switches e placas de rede.
- **Protocolos:** Ethernet, Wi-Fi (IEEE 802.11), PPP, MPLS.
- **Exemplo de Uso:** Comunicação em uma rede local (LAN) através de cabos Ethernet ou Wi-Fi.

### 5. **Camada Física**
- **Função:** Responsável pela transmissão dos sinais brutos (elétricos, ópticos ou de rádio) através do meio físico, como cabos ou ondas de rádio.
- **Aspectos Cobertos:** Tipo de cabo, conectores, frequência de rádio, modulação de sinais.
- **Exemplo de Uso:** Comunicação via cabos de fibra óptica ou ondas de rádio (Wi-Fi).

## Comparação com o Modelo OSI
O modelo TCP/IP é mais prático e amplamente utilizado, enquanto o modelo OSI (Open Systems Interconnection) é uma referência teórica. Algumas diferenças principais:

| Modelo OSI        | Modelo TCP/IP          |
|-------------------|------------------------|
| 7 camadas         | 5 camadas             |
| Mais detalhado    | Mais simplificado     |
| Pouco usado na prática | Base da Internet moderna |

## Resumo das Camadas do TCP/IP
| Camada            | Função Principal                  | Protocolos Exemplo                |
|-------------------|-----------------------------------|------------------------------------|
| Aplicação         | Serviços para os usuários         | HTTP, FTP, DNS, SMTP              |
| Transporte        | Entrega confiável ou rápida       | TCP, UDP                          |
| Rede              | Roteamento e endereçamento        | IPv4, IPv6, ICMP, ARP             |
| Enlace de Dados   | Transmissão física dos dados      | Ethernet, Wi-Fi                   |
| Física            | Transmissão dos sinais brutos     | Cabos, ondas de rádio             |

