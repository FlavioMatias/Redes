FILO (First In, Last Out) e LIFO (Last In, First Out) são conceitos usados em estruturas de dados e gerenciamento de inventário.

1. **FILO**: Significa que o último item adicionado é o primeiro a ser retirado. É menos comum em termos de gerenciamento de inventário, mas pode ser aplicado em certas situações, como em pilhas (stacks) de objetos.

2. **LIFO**: É um método frequentemente utilizado em inventários e refere-se a uma abordagem onde o último item que entrou no estoque é o primeiro a ser vendido ou retirado. É bastante aplicado em contextos onde os itens têm um custo variável e se busca minimizar os impostos sobre lucros.

### Aplicações em Redes

Em redes de computadores, esses conceitos podem ser aplicados na gestão de pacotes de dados:

- **LIFO** pode ser usado em buffers de transmissão, onde os pacotes mais recentes são processados primeiro, o que pode ser útil em situações onde os dados mais recentes são mais relevantes.
  
- **FILO** é menos comum em redes, mas poderia ser aplicado em cenários específicos de gerenciamento de dados temporários.





### Tipos de Redes de Computadores

#### 1. **PAN (Personal Area Network)**
- **Definição**: Redes de curto alcance, geralmente utilizadas para conectar dispositivos pessoais, como smartphones, tablets e laptops.
- **Exemplos**: Conexões Bluetooth entre fones de ouvido e um smartphone, ou uma rede Wi-Fi em casa.
- **Alcance**: Normalmente até 10 metros.
- **Uso**: Troca de dados entre dispositivos pessoais ou controle de dispositivos inteligentes (como smartwatches).

#### 2. **LAN (Local Area Network)**
- **Definição**: Redes que conectam dispositivos em uma área geográfica limitada, como um escritório, escola ou prédio.
- **Exemplos**: Redes de computadores em uma empresa ou em uma residência.
- **Alcance**: Pode variar de alguns metros a vários quilômetros, mas geralmente dentro de um único edifício.
- **Uso**: Compartilhamento de recursos, como impressoras e arquivos, e acesso à internet.

#### 3. **MAN (Metropolitan Area Network)**
- **Definição**: Redes que cobrem uma área geográfica maior que uma LAN, mas menor que uma WAN, como uma cidade ou um campus universitário.
- **Exemplos**: Redes que interconectam várias LANs em uma cidade ou região metropolitana.
- **Alcance**: Varia de 5 a 50 km.
- **Uso**: Conexão entre várias LANs, permitindo comunicação e compartilhamento de recursos em uma área mais ampla.

#### 4. **WAN (Wide Area Network)**
- **Definição**: Redes que abrangem grandes áreas geográficas, como países ou continentes, interconectando LANs e MANs.
- **Exemplos**: A internet é o exemplo mais conhecido de uma WAN.
- **Alcance**: Pode cobrir milhares de quilômetros.
- **Uso**: Conexão de redes em diferentes localidades, permitindo comunicação global.

### Comparação Rápida

| Tipo    | Alcance           | Exemplos                      | Uso Principal                    |
|---------|-------------------|-------------------------------|----------------------------------|
| PAN     | Até 10 metros     | Bluetooth, Wi-Fi pessoal      | Conexão de dispositivos pessoais |
| LAN     | Até vários km     | Redes de escritório, casa     | Compartilhamento de recursos     |
| MAN     | 5 a 50 km         | Redes urbanas, campus         | Conexão de LANs em áreas urbanas |
| WAN     | Milhares de km    | Internet                      | Conexão global de redes          |







# Estrutura e Comunicação da Internet  

## 1. Borda da Rede  
- **Borda da rede** inclui dispositivos finais (**hosts**) que:
  - Executam **aplicações**.
  - Estão localizados nas extremidades da rede.  

### 1.1 Modelos de Comunicação  
1. **Cliente/Servidor**  
   - O **cliente** inicia a comunicação enviando um pedido.  
   - O **servidor** responde ao pedido e fornece o recurso solicitado.  
   - Exemplo: Um navegador pedindo uma página web a um servidor HTTP.  

2. **Peer-to-Peer (P2P)**  
   - Comunicação **simétrica** entre dois ou mais dispositivos.
   - Os dispositivos atuam tanto como **clientes** quanto como **servidores**.
   - Exemplo: Compartilhamento de arquivos entre usuários via torrent.  

---

## 2. Núcleo da Rede  
- Formado por uma malha de **roteadores** e **switches** interconectados.
- **Função**:
  - **Encaminhar pacotes** do remetente ao destinatário, escolhendo a melhor rota disponível.
  - Cada pacote pode percorrer caminhos diferentes para chegar ao destino.  

---

## 3. Meios Físicos de Comunicação  
Os dispositivos se comunicam por meio de diferentes tipos de enlaces:  
- **Fibra óptica**: Alta capacidade e longas distâncias.  
- **Cabo de cobre**: Utilizado em redes locais (LANs).  
- **Rádio**: Usado em redes sem fio, como WiFi e 5G.  
- **Satélite**: Enlaces de comunicação em locais remotos ou para grandes coberturas.  

---

## 4. Comunicação por Pacotes  
- **Transmissão de dados na Internet**:
  - A comunicação ocorre por **pacotes de dados** que viajam entre dispositivos.
  - Cada pacote contém informações sobre:
    - **Endereço de origem e destino**.
    - **Dados da mensagem** e **número do pacote** (para reordenação, se necessário).  
  - Os pacotes podem seguir rotas diferentes e ser reorganizados ao chegar no destino.  

---

## 5. ISP (Provedor de Serviços de Internet)  
- A comunicação entre dispositivos passa por vários níveis de **provedores de serviço**:
  1. **ISP local**: Oferece conexão para residências e pequenas empresas.
  2. **ISP regional**: Conecta redes locais e oferece serviços em áreas maiores.
  3. **Backbones** e **centros de dados**: Infraestrutura que suporta grandes volumes de tráfego de dados entre regiões e países.  

---

Essa estrutura permite que a Internet funcione de forma **distribuída**, rápida e resiliente, com roteadores e enlaces escolhendo as melhores rotas para os dados.
