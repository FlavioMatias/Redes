# Camada de Enlace de Dados e Protocolos

A camada de enlace de dados é a segunda camada no modelo OSI (Open Systems Interconnection) e a primeira camada do modelo TCP/IP. Ela tem como principal objetivo garantir uma comunicação livre de erros entre dispositivos conectados diretamente, como computadores ou roteadores, na mesma rede local.

### Funções da Camada de Enlace de Dados

A camada de enlace de dados possui diversas responsabilidades, incluindo:

- **Encapsulamento de Dados:** Ela pega os dados da camada de rede e os encapsula em quadros (frames) para serem enviados pela rede física.
- **Controle de Erros:** A camada de enlace verifica se os dados foram corrompidos e solicita retransmissões, caso necessário.
- **Controle de Fluxo:** Ela gerencia o fluxo de dados entre dois dispositivos para evitar congestionamento.
- **Endereçamento Físico:** A camada de enlace usa endereços físicos (MAC) para identificar dispositivos.

### Protocolos da Camada de Enlace de Dados

A camada de enlace de dados pode ser subdividida em dois subníveis: o **Controle de Acesso ao Meio (MAC)** e o **Controle de Enlace Lógico (LLC)**.

#### Protocolos de Controle de Acesso ao Meio (MAC)

O **MAC** é responsável pela forma como os dispositivos acessam e compartilham o meio físico. Alguns dos principais protocolos da camada MAC incluem:

| Protocolo | Descrição |
|-----------|-----------|
| **Ethernet** | O protocolo mais comum em redes locais (LANs). Utiliza endereços MAC e opera no padrão de comunicação CSMA/CD. |
| **Wi-Fi (IEEE 802.11)** | Usado em redes sem fio, define como os dispositivos acessam e compartilham o meio de comunicação sem fio. |
| **Bluetooth** | Tecnologia de comunicação de curto alcance, geralmente usada para conexões pessoais entre dispositivos próximos. |
| **Token Ring** | Um protocolo onde os dispositivos enviam dados usando um token para controlar o acesso à rede. |

#### Protocolos de Controle de Enlace Lógico (LLC)

O **LLC** atua como uma interface entre a camada de enlace de dados e a camada de rede. Ele é responsável por fornecer serviços de comunicação e controle entre os dispositivos.

| Protocolo | Descrição |
|-----------|-----------|
| **IEEE 802.2 LLC** | Oferece serviços de comunicação orientados à conexão, com controle de fluxo e erros. |
| **Frame Relay** | Protocolo de rede de longa distância que utiliza encapsulamento de dados na camada de enlace. |
| **ATM (Asynchronous Transfer Mode)** | Usado em redes de alta velocidade, oferece serviços de transmissão com diferentes tipos de tráfego. |

### Estrutura de um Quadro (Frame)

Um quadro é a unidade de dados que a camada de enlace de dados transmite. Ele contém diversas partes importantes:

| Campo          | Descrição |
|----------------|-----------|
| **Endereço de Destino (MAC)** | Endereço físico do dispositivo de destino. |
| **Endereço de Origem (MAC)** | Endereço físico do dispositivo de origem. |
| **Tipo de Protocolo** | Indica o protocolo da camada superior (ex.: IPv4, ARP). |
| **Dados** | A carga útil do quadro, ou seja, os dados sendo transmitidos. |
| **Cheksum / CRC** | Campo de verificação de erros para garantir a integridade dos dados. |

### Exemplos de Protocolos da Camada de Enlace

- **Ethernet:** A Ethernet é o protocolo mais comum em redes locais e usa a técnica CSMA/CD para controlar o acesso ao meio.
- **Wi-Fi:** Com o aumento das redes sem fio, o Wi-Fi (IEEE 802.11) tornou-se um dos principais protocolos na camada de enlace, usando a modulação e técnicas de segurança para garantir a comunicação.
