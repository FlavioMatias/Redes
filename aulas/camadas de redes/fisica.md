# Camada Física e Protocolos

A camada física é a primeira camada do modelo OSI (Open Systems Interconnection) e também a camada mais próxima do hardware, sendo responsável pela transmissão de bits brutos através do meio físico. Ela define as características elétricas, mecânicas e funcionais do meio de comunicação.

### Funções da Camada Física

A principal função da camada física é garantir que os dados sejam fisicamente transmitidos entre os dispositivos, seja por fios, ondas de rádio ou fibras ópticas. As suas principais responsabilidades incluem:

- **Transmissão de Bits:** A camada física transmite os bits (0s e 1s) ao longo do meio físico.
- **Codificação de Dados:** Converte os dados binários em sinais elétricos, ópticos ou de rádio.
- **Controle de Acesso ao Meio:** Embora o controle de acesso ao meio seja geralmente responsabilidade da camada de enlace, a camada física pode influenciar as técnicas de transmissão de dados.
- **Definição de Características do Meio:** Define os cabos, conectores e outros elementos físicos necessários para a comunicação.

### Tipos de Meio de Transmissão

A camada física pode usar diferentes tipos de meios para transmitir dados, que podem ser divididos em dois grandes grupos: **meios guiados** e **meios não guiados**.

#### Meios Guiados

São aqueles que utilizam um condutor físico para transmitir os sinais. Exemplos incluem cabos e fibras ópticas.

| Tipo de Meio | Descrição |
|---------------|-----------|
| **Cabo de Par Trançado (Twisted Pair)** | Consiste em pares de fios de cobre entrelaçados. Comum em redes Ethernet (ex: CAT5, CAT6). |
| **Cabo Coaxial** | Fio de cobre no centro, isolado e rodeado por uma camada condutora. Usado em TVs a cabo e algumas redes antigas. |
| **Fibra Óptica** | Utiliza sinais de luz para transmitir dados. Muito eficiente em longas distâncias e com alta largura de banda. |

#### Meios Não Guiados

São aqueles que transmitem sinais sem a necessidade de condutores físicos. Incluem sinais de rádio e micro-ondas.

| Tipo de Meio | Descrição |
|---------------|-----------|
| **Ondas de Rádio** | Usadas em redes sem fio como Wi-Fi, Bluetooth e comunicação de rádio. |
| **Micro-ondas** | Comunicação ponto a ponto, muito utilizada em links de longa distância. |
| **Infravermelho** | Usado em transmissões de curta distância, como controles remotos. |

### Codificação e Modulação de Sinais

A camada física também lida com a codificação e modulação dos sinais para a transmissão de dados.

| Técnica | Descrição |
|---------|-----------|
| **Codificação de Manchester** | Técnica em que cada bit de dados é representado por uma transição no meio do sinal (exemplo: 1 = transição de alto para baixo, 0 = transição de baixo para alto). |
| **Modulação de Amplitude (AM)** | A amplitude do sinal portador é variada para representar os dados. |
| **Modulação de Frequência (FM)** | A frequência do sinal portador é variada para representar os dados. |
| **Modulação por Fase (PM)** | A fase do sinal portador é variada para representar os dados. |

### Características da Camada Física

A camada física define várias características dos sinais e do meio de transmissão:

| Característica | Descrição |
|----------------|-----------|
| **Taxa de Transmissão** | Define a quantidade de dados que podem ser transmitidos por segundo (ex: 1 Gbps, 10 Gbps). |
| **Distância** | A camada física também especifica as distâncias máximas que os sinais podem percorrer, dependendo do meio utilizado. |
| **Largura de Banda** | Refere-se à quantidade de dados que podem ser transmitidos em um dado período de tempo. Quanto maior a largura de banda, maior a capacidade de transmissão. |
| **Imunidade a Ruídos** | Alguns meios físicos são mais suscetíveis a interferências do que outros. Por exemplo, cabos coaxiais são mais resistentes a ruídos do que cabos de par trançado. |

### Exemplos de Protocolos da Camada Física

A camada física não lida diretamente com a transmissão de dados de forma organizada (isso é responsabilidade de camadas superiores), mas alguns protocolos definem as regras para a transmissão física, como:

| Protocolo | Descrição |
|-----------|-----------|
| **Ethernet (IEEE 802.3)** | Define as características físicas de redes com fio, como cabos de par trançado ou coaxiais, e as taxas de transmissão. |
| **Wi-Fi (IEEE 802.11)** | Define as características físicas de redes sem fio, como a modulação e a frequência de operação. |
| **Bluetooth** | Define como os sinais de rádio de baixa potência são usados para a comunicação de curto alcance. |
| **DSL (Digital Subscriber Line)** | Usado para transmissão de dados de alta velocidade sobre linhas telefônicas. |
