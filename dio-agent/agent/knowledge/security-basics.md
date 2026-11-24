# Fundamentos de Segurança da Informação

Este documento estabelece a base teórica de cibersegurança e segurança da informação utilizada pelo DIO Agent para fundamentar suas análises defensivas.

---

## 1. Conceitos Fundamentais

### Vulnerabilidade
Uma falha, fraqueza ou brecha no projeto, implementação, configuração ou operação de um sistema, aplicação ou processo que pode ser explorada para comprometer a segurança.

### Ameaça
Qualquer circunstância, evento, ator malicioso ou elemento que possui o potencial de explorar uma vulnerabilidade e causar dano ou interrupção.

### Risco
A probabilidade de uma ameaça explorar com sucesso uma vulnerabilidade somada ao impacto gerado por essa exploração.
$$\text{Risco} = \text{Impacto} \times \text{Probabilidade}$$

---

## 2. A Tríade CIA (Princípios de Segurança)

A base clássica da segurança da informação é composta por três pilares inegociáveis:

1. **Confidencialidade:** Garantir que dados e recursos sejam acessíveis estritamente por usuários, processos e entidades autorizadas.
2. **Integridade:** Garantir a exatidão, consistência e confiabilidade das informações, assegurando que não sejam modificadas, corrompidas ou apagadas indevidamente.
3. **Disponibilidade:** Assegurar que os sistemas, redes e dados estejam operacionais e acessíveis aos usuários autorizados sempre que necessário.

---

## 3. Padrões de Mercado para Classificação

- **OWASP Top 10:** Documento de conscientização da *Open Web Application Security Project* que lista os 10 riscos de segurança mais críticos em aplicações web (ex: Injeção, Quebra de Autenticação, Falhas Criptográficas).
- **MITRE ATT&CK:** Base de conhecimento global que mapeia táticas, técnicas e procedimentos (TTPs) utilizados por adversários reais em ciberataques.
- **CWE (Common Weakness Enumeration):** Dicionário formal de tipos de fraquezas de software e hardware.

---

## 4. Boas Práticas de Segurança Defensiva (AppSec e Infraestrutura)

- **Validação e Parametrização:** Nunca confiar na entrada do usuário. Utilizar *Prepared Statements* (consultas parametrizadas) e validação rigorosa de tipos e formatos.
- **Princípio do Menor Privilégio (*Least Privilege*):** Conceder a usuários, sistemas e processos apenas as permissões estritamente necessárias para cumprirem sua função.
- **Defesa em Profundidade (*Defense in Depth*):** Implementar múltiplas camadas de proteção (firewall, WAF, autenticação multifator, criptografia, monitoramento).
- **Gestão de Atualizações e Patches:** Manter sistemas operacionais, dependências de código e bibliotecas sempre atualizados com os últimos boletins de segurança.
- **Monitoramento e Auditoria:** Registrar logs de eventos críticos e falhas de autenticação para detecção precoce de comportamentos anômalos.
