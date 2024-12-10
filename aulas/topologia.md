# Topologias de Rede

A topologia de rede define como os dispositivos em uma rede estão conectados entre si. Cada tipo de topologia possui vantagens, desvantagens e casos de uso específicos.

---

## Principais Tipos de Topologia

### 1. Topologia em Estrela

Na topologia em estrela, todos os dispositivos são conectados a um dispositivo central (geralmente um switch ou hub).

| Característica      | Descrição |
|---------------------|-----------|
| **Vantagens**       | - Fácil de configurar e expandir. <br> - Um problema em um cabo não afeta toda a rede. |
| **Desvantagens**    | - Dependência do dispositivo central. <br> - Custo mais alto devido à quantidade de cabos. |
| **Exemplo de Uso**  | Redes locais (LANs) modernas. |

---

### 2. Topologia em Anel

Na topologia em anel, cada dispositivo é conectado a dois outros, formando um círculo.

| Característica      | Descrição |
|---------------------|-----------|
| **Vantagens**       | - Transmissão eficiente de dados em uma direção. <br> - Todos os dispositivos têm o mesmo acesso ao meio. |
| **Desvantagens**    | - Se um dispositivo falhar, pode interromper toda a rede. <br> - Difícil de expandir. |
| **Exemplo de Uso**  | Redes Token Ring antigas. |

---

### 3. Topologia em Barramento

Na topologia em barramento, todos os dispositivos compartilham um único cabo central (barramento).

| Característica      | Descrição |
|---------------------|-----------|
| **Vantagens**       | - Custo baixo devido ao uso de menos cabos. <br> - Simples de implementar em redes pequenas. |
| **Desvantagens**    | - Conflitos de transmissão (colisões) podem ocorrer. <br> - Um problema no cabo afeta toda a rede. |
| **Exemplo de Uso**  | Redes antigas e pequenas LANs. |

---

### 4. Topologia em Malha (Mesh)

Na topologia em malha, cada dispositivo está conectado a vários outros dispositivos, criando várias rotas possíveis para os dados.

| Característica      | Descrição |
|---------------------|-----------|
| **Vantagens**       | - Alta redundância e confiabilidade. <br> - Ideal para redes críticas onde falhas precisam ser evitadas. |
| **Desvantagens**    | - Custo elevado devido à grande quantidade de conexões. <br> - Configuração complexa. |
| **Exemplo de Uso**  | Redes industriais e de telecomunicações. |

---

### 5. Topologia em Árvore

A topologia em árvore é uma combinação hierárquica de várias topologias em estrela. Os dispositivos são organizados em camadas.

| Característica      | Descrição |
|---------------------|-----------|
| **Vantagens**       | - Fácil de gerenciar grandes redes. <br> - Boa escalabilidade. |
| **Desvantagens**    | - Se um nó principal falhar, uma parte da rede pode ficar inativa. |
| **Exemplo de Uso**  | Redes corporativas ou escolares. |

---

### 6. Topologia Híbrida

Uma topologia híbrida combina dois ou mais tipos de topologias (por exemplo, estrela e barramento) para atender a necessidades específicas.

| Característica      | Descrição |
|---------------------|-----------|
| **Vantagens**       | - Flexível e pode ser adaptada para diferentes cenários. |
| **Desvantagens**    | - Configuração e manutenção complexas. |
| **Exemplo de Uso**  | Grandes redes empresariais. |

---

## Comparação dos Tipos de Topologia

| Topologia   | Custo  | Complexidade | Tolerância a Falhas | Exemplo de Uso          |
|-------------|--------|--------------|---------------------|-------------------------|
| **Estrela** | Médio  | Simples      | Moderada            | Redes LANs modernas     |
| **Anel**    | Baixo  | Moderada     | Baixa               | Redes Token Ring        |
| **Barramento** | Baixo | Simples    | Baixa               | Redes pequenas          |
| **Malha**   | Alto   | Complexa     | Alta                | Redes industriais       |
| **Árvore**  | Médio  | Moderada     | Moderada            | Redes organizacionais   |
| **Híbrida** | Alto   | Complexa     | Variável            | Grandes redes corporativas |
