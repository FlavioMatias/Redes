## Principais Protocolos da Camada de Rede

### 1. **IP (Internet Protocol)**
O **IP** é o protocolo mais importante da camada de rede. Ele é responsável pelo endereçamento e roteamento de pacotes entre dispositivos em redes diferentes. Existem duas versões principais de IP:

- **IPv4 (Internet Protocol version 4)**: Usa endereços de 32 bits, o que possibilita cerca de 4 bilhões de endereços únicos. Exemplo: `192.168.1.1`.
- **IPv6 (Internet Protocol version 6)**: Usa endereços de 128 bits, o que permite um número praticamente infinito de endereços. Exemplo: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`.

### 2. **ARP (Address Resolution Protocol)**
O **ARP** é usado para mapear endereços de IP para endereços MAC (endereços físicos). Ele é fundamental para que os dispositivos em uma rede local (como LANs) saibam o endereço físico de outros dispositivos a partir de seus endereços IP.

- **Exemplo de funcionamento**: Quando um dispositivo precisa enviar um pacote para outro dentro da mesma rede, ele consulta a tabela ARP para saber o endereço MAC correspondente ao IP de destino.

### 3. **ICMP (Internet Control Message Protocol)**
O **ICMP** é usado para enviar mensagens de controle e erro, como quando um host não pode ser alcançado ou quando um roteador não consegue entregar um pacote. Um dos usos mais comuns do ICMP é o comando **ping**, que verifica a conectividade de rede entre dois dispositivos.

- **Exemplo de uso**: `ping 192.168.1.1` para verificar se o dispositivo com o IP 192.168.1.1 está acessível.

### 4. **IGMP (Internet Group Management Protocol)**
O **IGMP** é utilizado para gerenciar grupos de multicast em uma rede IPv4. Ele permite que dispositivos se inscrevam ou deixem grupos multicast para receber dados.

- **Exemplo de uso**: Quando um roteador precisa enviar pacotes para vários dispositivos, ele utiliza o IGMP para definir quais dispositivos fazem parte de um grupo multicast.

### 5. **RIP (Routing Information Protocol)**
O **RIP** é um protocolo de roteamento de vetor de distância usado para determinar a melhor rota para um pacote de dados. Ele utiliza o número de saltos como critério para calcular a distância até o destino.

- **Exemplo de funcionamento**: O RIP escolhe a rota com o menor número de saltos (hops) entre os roteadores.

### 6. **OSPF (Open Shortest Path First)**
O **OSPF** é um protocolo de roteamento de estado de enlace. Ele utiliza uma abordagem diferente do RIP, calculando a melhor rota com base no estado atual dos enlaces (como a largura de banda ou a latência de uma conexão).

- **Exemplo de funcionamento**: O OSPF envia informações sobre o estado das rotas para todos os roteadores, que então calculam o melhor caminho para os pacotes.

### 7. **BGP (Border Gateway Protocol)**
O **BGP** é um protocolo de roteamento entre sistemas autônomos (ASes), ou seja, entre diferentes redes administradas por diferentes organizações. Ele é fundamental para a troca de informações de roteamento na internet.

- **Exemplo de uso**: O BGP é utilizado pelos provedores de internet para determinar o melhor caminho para enviar dados entre diferentes redes.

### 8. **IPSec (Internet Protocol Security)**
O **IPSec** é um protocolo de segurança usado para proteger a comunicação de dados entre dispositivos na camada de rede. Ele pode criptografar e autenticar pacotes IP para garantir a segurança na troca de dados.

- **Exemplo de uso**: O IPSec é comumente utilizado em **VPNs** (Virtual Private Networks) para criar uma conexão segura entre dois pontos.

---

### Protocolos da Camada de Rede e suas Funções

| Protocolo     | Função                                                | Exemplo de Uso                                           |
|---------------|-------------------------------------------------------|----------------------------------------------------------|
| **IP**        | Endereçamento e roteamento de pacotes                 | Determina o caminho dos pacotes entre dispositivos       |
| **ARP**       | Mapeamento de IP para endereço MAC                    | Resolve o endereço MAC correspondente ao IP             |
| **ICMP**      | Mensagens de controle e erro                          | Usado pelo comando **ping** para testar conectividade   |
| **IGMP**      | Gerenciamento de grupos de multicast IPv4             | Gerencia grupos de dispositivos que recebem multicast    |
| **RIP**       | Roteamento de vetor de distância                      | Determina a melhor rota entre roteadores com base no número de saltos |
| **OSPF**      | Roteamento de estado de enlace                        | Utilizado em redes de grande porte para determinar o melhor caminho |
| **BGP**       | Roteamento entre sistemas autônomos (AS)              | Usado na troca de rotas entre diferentes ISPs            |
| **IPSec**     | Segurança na comunicação de pacotes                   | Criptografia e autenticação de pacotes em VPNs           |

### Comparação entre Protocolos de Roteamento

| Protocolo    | Tipo de Roteamento              | Métrica de Roteamento      | Escalabilidade          | Exemplo de Uso        |
|--------------|---------------------------------|----------------------------|-------------------------|-----------------------|
| **RIP**      | Vetor de distância             | Número de saltos (hops)    | Baixa                   | Pequenas redes        |
| **OSPF**     | Estado de enlace               | Custo do enlace (largura de banda, latência, etc.) | Alta                    | Redes empresariais    |
| **BGP**      | Baseado em políticas           | Caminhos e atributos       | Muito alta              | Roteamento na Internet|

###  Máscaras de Sub-rede Comuns (IPv4)

| Máscara de Sub-rede   | Prefixo CIDR | Endereços de Rede Disponíveis | Intervalo de IPs Disponíveis  |
|-----------------------|--------------|-------------------------------|------------------------------|
| 255.0.0.0             | /8           | 16.777.216                    | 10.0.0.1 a 10.255.255.254    |
| 255.255.0.0           | /16          | 65.536                        | 192.168.0.1 a 192.168.255.254|
| 255.255.255.0         | /24          | 256                           | 192.168.1.1 a 192.168.1.254  |
