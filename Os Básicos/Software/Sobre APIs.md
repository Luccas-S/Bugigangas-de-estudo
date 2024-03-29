Nesse texto estarei estudando a respeito de 
APIs(Application Programming Interface), API Rest e afins na área
de TI(Tecnologia da Informação).

APIs são padrões de interfaces programáveis que facilitam a criação de 
plataformas, essas sendo aplicativos, complementos, scripts e webhooks.
Esses padrões estão presentes em diversos lugares, um exemplo simples são
apps feitos para android que utilizam padrões do sistema operacional. Isso
se extende para outras plataformas, existem APIs para grandes sites como
o Twitter/X usadas para criar scripts e aplicações que complementam a
experiência de uso do mesmo, é uma relação majoritáriamente cooperativa
apesar de suas nuances e termos relacionados a pagamento de royalties e 
tokens.

Da mesma forma que drivers permitem que softwares usem subsistemas de 
hardware sem precisar saber de cada detalhe operacional do mesmo, APIs
desempenham funções parecidas, usando funcionalidades do PC(Personal Computer) 
e do sistema operacional sem necessáriamente precisar acompanhar todos 
os detalhes de operação da CPU(Central Processing Unit) ou 
da plataforma usada.

APIs são conjuntos de padrões e normas a seguir para comunicação com sistemas 
diversos, podemos compreender como aplicação programável à interfaces. Através
delas podemos criar aplicações e extensões para aplicativos já existentes 
economizando o tempo de os desenvolver do zero, já que com elas ja temos
estruturas prontas para uso. A função principal de APIs é facilitar o trabalho
de programadores com economia de tempo, já que corta a necessidade de criar
códigos personalizados para cada função do aplicativo que criam.

A seguir, um exemplo de funcionalidades escrito por Curt Franklin e
Chris Pollette no site www.howstuffworks.com e traduzido por mim:

"Vamos ver um exemplo de criar um arquivo num HDD(Hard Disk Drive) para
vermos o porquê isso pode ser importante.

Um programador escrevendo uma aplicação para armazenar dados de um
instrumento cientifico pode querer permitir o cientista de especificar
o nome do arquivo criado. O sistema operacional pode prover uma função
API chamada "MakeFile" para criar arquivos. Enquanto escreve o programa, o 
desenvolvedor usaria uma linha que se parece com isso:

MakeFile[1, %Name,2]

Nesse exemplo, a instrução diz ao sistema operacional para criar um arquivo
que permitirá acesso aleatório de seus dados(sinalizado pelo 1 - a outra
opção poderia ser 0 para um arquivo serial(Um tipo de arquivo sequêncial
que consiste de multiplos armazenamentos de dados com o mesmo espaço na 
memória.)), terá um nome digitado pelo usuário(%Name) e ocupará um espaço
variável dependendo de quantos dados estão guardados no arquivo(Indicado 
pelo 2 - outras opções podem ser 0 para um tamanho fixo, e 1 para um
tipo de arquivo que usa mais espaço quanto mais dados são adicionados mas
não usa menos espaço quando esses dados são removidos). Agora, vejamos o que
o sistema operacional faz para transformar essa instrução em ação.

O sistema operacional manda uma instrução para o HDD para identificar a
localização do primeiro espaço livre de armazenamento.

Com essa informação, o sistema operacional cria uma entrada no sistema de
arquivos mostrando a locação inicial e final do mesmo arquivo, o nome,
o tipo de arquivo, se o arquivo foi armazenado, que usuários tem permissão
de olhar ou modificar o arquivo e por fim a data e horário de criação do
arquivo."

O uso da API para armazenamento em disco torna o trabalho do programador mais
simples e dinâmico, a necessidade de acompanhar instruções, códigos responsivos
e tipagem de dados é nulificada, deixando o desenvolvedor com mais tempo para
outras tarefas. Uma parte do trabalho é delegada ao sistema operacional, o 
mesmo conectado a diversas subrotinas do hardware vai lidar com os detalhes
operacionais e detalhes repentinos do hardware. O programador passa a precisar
apenas escrever seu código na API e o sistema operacional cuidará do resto.

Mesmo com essas vantagens, é necessário ressaltar que o acesso aos softwares
que APIs oferecem pode ser uma fraqueza de segurança e pode oferecer vantagem
para hackers usarem a aplicação por benefício próprio ou até ganhar acesso
a computadores pessoais de terceiros. De toda forma, isso não quer dizer que
o uso de APIs é ruim, ele mantém sua utilidade mas ao mesmo tempo devemos
enfatizar a necessidade de identificar vulnerabilidades e corrigir elas
conforme forem detectadas. Da mesma forma que são inerentemente vulneráveis,
APIs de forma contraditória também são poderosas ferramentas para a segurança
digital, já que as mesmas podem bloquear acesso e permissões à dados de
softwares importantes e hardwares essenciais.

Existem essencialmente quatro tipos de APIs que são definidos pelas suas
políticas de compartilhamento e uso. A seguir quatro definições dos tipos
de API a partir dessas políticas descritas pelo blog do site www.syndle.com:

1. APIs públicas ou abertas
As APIs públicas são também conhecidas como APIs abertas e estão disponíveis 
para outros usuários ou programadores utilizarem com restrições mínimas ou, 
em alguns casos, de forma totalmente acessível.

2. APIs privadas ou internas
As APIs privadas ou internas são ocultadas aos usuários externos e são 
expostas apenas para os sistemas internos de uma organização. São utilizadas
para o desenvolvimento interno da empresa, otimizando a produtividade e a 
reutilização dos serviços.

3. APIs de parceiros de negócio
As APIs de parceiros comerciais são aquelas que são expostas entre os 
membros de um acordo comercial. Uma vez que não estão disponíveis para 
todos, é necessária uma autorização especial para sua utilização.

4. APIs compostas
As APIs compostas utilizam diferentes dados ou APIs de serviços e permitem 
aos programadores acessar múltiplos pontos finais.

Existem também definições diferentes para cada caso de uso de API, abaixo
seguem ditas definições de acordo com o blog do site www.syndle.com:

1. API de dados
As APIs de dados fornecem a vários bancos de dados ou provedores 
SaaS (Software as a Service ou Software como Serviço) um acesso 
CRUD (Create, Read, Update, Delete) a conjuntos de dados subjacentes, 
permitindo a comunicação entre uma aplicação e um sistema de gestão de base 
de dados.

2. API de sistemas operacionais
Este grupo de APIs define como as aplicações utilizam os recursos e serviços 
disponíveis do sistema operacional. Assim, cada OS (Operative System) 
possui um conjunto de APIs, por exemplo, a API do Windows ou a API do Linux 
possuem kernel-user space API e kernel internal API.

3. APIs remotas
Este grupo define os padrões de interação que as aplicações têm em 
diferentes dispositivos, ou seja, um software acessa determinados recursos 
localizados fora do dispositivo requerente, como o nome indica. Como duas 
aplicações se ligam remotamente através de uma rede, as APIs remotas 
utilizam protocolos para conseguir a ligação.

4. APIs web
Esta classe de APIs é a mais comum, uma vez que as APIs web fornecem dados 
que os dispositivos podem ler e transferir entre sistemas baseados na web ou 
arquitetura cliente-servidor.

Além de suas diferentes definições, APIs também possuem diferentes protocolos
que possibilitam normatizar trocas de dados e instruções entre serviços.
Desta forma as APIs adquirem a capacidade de acessar as capacidades de
variados tipos de sistema e serviço, por entre linguagens de programação
diferentes e sistemas operacionais diferentes. Dentre esses protocolos os
mais conhecidos e importantes são:

REST(Representational State Transfer)

REST é um protocolo de arquitetura de software com seis restrições para
o desenvolvimento de aplicações que correm sobre HTTP, com destaque para
serviços web.

REST é um dos protocolos mais populares e é considerado uma alternativa mais
rápida para o protocolo SOAP já que muitos desenvolvedores têm dificuldade
em usa-la por ter que tecer muitas linhas de código para apenas uma tarefa 
enquanto que REST segue uma linha diferente, provendo disponibilidade de
dados como recurso.

SOAP(Service Object Access Protocol)

O SOAP é um protocolo considerado dos mais leves para movimentação de dados
em ambiente descentralizado e distribuído. O mesmo possui especificações de
regras para sintaxe de pedidos e para as respostas enviadas pelos pedidos.

Aplicações que usam essas normas permitem o envio de mensagens 
XML(Extensible Markup Language) pelo sistema usando 
HTTP(Hypertext Transfer Protocol) ou SMTP(Simple Mail Transfer Protocol).

RPC(Remote Procedure Call)

O procedimento remoto ou RPC se baseia no uso do intercâmbio de recursos em
APIs web e seu principal objetivo é definir as interações entre aplicações
em um programa que solicita dados(cliente) e outro que fornece(servidor)
remotamente.

GraphQL

Nascido da necessidade de desenvolver mais rápido, o GraphQL tem um 
carregamento de dados mais eficiênte com mais adaptabilidade móvel.

Nessa linguagem de consulta de API, o cliente pode solicitar dados mais
detalhadamente e auxilia na adição de informação através de simplicidade
por meio de diversas fontes.

Entraremos mais a fundo em APIs do protocolo REST abaixo usando os textos
explicativos do blog do site da IBM www.ibm.com:

"Uma API de REST é uma API que se adéqua aos princípios de design do REST ou 
o estilo de arquitetura do Representational State Transfer.  Por esta razão, 
as APIs de REST são muitas vezes chamadas de APIs de RESTful.
Definido pela primeira em 2000 pelo cientista de computação Dr. Roy Fielding 
em sua dissertação de doutorado, o REST proporciona um nível relativamente 
alto de flexibilidade e liberdade para desenvolvedores. Essa flexibilidade 
é apenas uma razão pela qual as APIs de REST surgiram como um método comum 
para conectar componentes e aplicativos em uma arquitetura de microsserviços.

Basicamente, uma API é um mecanismo que permite que um aplicativo ou serviço 
acesse um recurso dentro de outro aplicativo ou serviço. O aplicativo ou 
serviço que está realizando o acesso é chamado de cliente, e o aplicativo 
ou serviço contendo o recurso é chamado de servidor.

Algumas APIs, como SOAP ou XML-RPC, impõe um framework restrito para os 
desenvolvedores. Porém, as APIs de REST podem ser desenvolvidas usando 
praticamente qualquer linguagem de programação e oferecem suporte a uma 
variedade de formatos de dados. O único requisito é que eles devem alinhar 
aos seis princípios de design de REST a seguir, conhecidos como restrições 
de arquitetura:

1. Interface uniforme. Todas as solicitações da API para o mesmo recurso devem 
ser iguais, não importa a origem da solicitação. A API de REST deve garantir 
que a mesma parte dos dados dados, como o nome ou endereço de e-mail de um 
usuário, pertença a apenas um identificador de recurso uniforme (URI). 
Os recursos não devem ser muito grandes mas devem conter todas as 
informações que o cliente pode precisar.

2. Desacoplamento do cliente-servidor. No projeto da API de REST, os 
aplicativos cliente e servidor devem ser completamente independentes um do 
outro. A única informação que o aplicativo cliente deve receber é o URI do 
recurso solicitado. Ele não pode interagir com o aplicativo do servidor de 
qualquer outra forma. Da mesma forma, um aplicativo do servidor não deve 
modificar o aplicativo cliente, exceto para transferi-los aos dados 
solicitados via HTTP.

3. Sem estado definido. As APIs de REST não possuem estado definido, o que 
significa que cada solicitação precisa incluir todas as informações 
necessárias para processá-lo. Em outras palavras, as APIs de REST não 
requerem nenhuma sessão do lado do servidor. Os aplicativos do servidor não 
tem permissão para armazenar nenhum dado relacionado a uma solicitação de 
cliente.

4. Capacidade de armazenamento em cache. Quando possível, os recursos devem 
ser armazenados em cache pelo cliente ou servidor. As respostas do servidor 
também precisam conter informações sobre as permissões de cache do recurso 
fornecido. O objetivo é melhorar o desempenho do cliente, além de aumentar 
a escalabilidade do servidor.

5. Arquitetura de sistema em camadas. Em APIs de REST, as chamadas e 
respostas passam por diferentes camadas. De maneira geral, não assuma que 
os aplicativos cliente e servidor se conectem diretamente um ao outro. Pode 
haver uma série de intermediários diferentes no loop de comunicação. As APIs 
de REST precisam ser projetadas para que nem o cliente e nem o servidor 
possam dizer se ele se comunica com o aplicativo final ou um intermediário.

6. Código sob demanda (opcional). As APIs de REST geralmente enviam recursos 
estáticos, mas em certos casos, as respostas também podem conter código 
executável (como applets Java). Nestes casos, o código deve ser executado 
somente sob demanda."

APIs de REST funcionam se comunicando usando solicitações em HTTP para
executar funções de banco de dados, funções essas chamadas de CRUD, no caso
são as funções Criar, Ler, Atualizar e Excluir em um recurso. Uma API de REST
poderia usar as instruções de banco de dados através de solicitações em HTTP 
para atingir seu objetivo, como uma solicitação GET para recuperar um 
registro, POST para criar um registro, PUT para atualizar um registro e 
DELETE para excluir um registro. Esses métodos HTTP podem ser usados em
chamadas de API.

A representação de recursos como data, hora, estado do recurso e afins podem
ser entreguer a um cliente em quase qualquer formato, esses sendo JavaScript
Object Notation(JSON), HTML, XLT, Python, PHP ou texto simples. Nesse caso
o JSON é o mais usado por ser legível por pessoas e máquinas.

Os cabeçalhos e parâmetros de solicitação também são importantes em chamadas 
de API de REST, porque incluem informações importantes do identificador como 
metadados, autorizações, identificadores de recursos uniformes (URIs), 
armazenamento em cache, cookies e mais. Os cabeçalhos de solicitação e 
cabeçalhos de resposta, juntamente aos códigos de status HTTP convencionais, 
são usados dentro de APIs de REST bem projetadas.

Finalmente chegamos a um breve estudo sobre as melhores práticas de uso da
API de REST.
Da mesma maneira que a flexibilidade das APIs de REST são uma grande vantagem,
a mesma flexibilidade abre caminho para criação de APIs defeituosas que
performam mal e geram prejuizo no fluxo de trabalho de uma equipe. Assim, se
torna importante a execução das melhores práticas de uso pelos profissionais
que usam APIs de REST em seu trabalho, práticas essas que são aprimoradas e
compartilhadas por todos na indústria.

Para auxiliar no uso das melhores práticas, foi criada a 
OAS(OpenAPI Specification), uma ferramenta que organiza informações chave
numa interface intuitiva, criando acessibilidade aos desenvolvedores e seus
aplicativos para que tenham acesso às principais características de uma 
determinada API, documentando seus principais recursos, normas, terminais,
operações permitidas para determinado terminal, parâmetros das operações,
normas de autenticação e etc...

A segurança também entra como elemento chave para termos boas práticas com
APIs de REST, tendo noção de suas falhas e vulnerabilidades, se torna
necessário o uso de diversos métodos para aumentar a segurança da API, como
JSON Web Tokens, algoritmos de hashing, validação de parâmetros, o próprio
uso de HTTPS para mover dados também ajuda na segurança, além de registros
de data, hora e permissões para aplicativos terceiros, para isso podemos usar
estruturas de autorização como o OAuth 2.0 juntamente do cabeçalho HTTP.

Vemos que APIs se tornaram um pilar da programação e desenvolvimento moderno,
a industria percebeu e adotou seu potencial nos ultimos anos, tornando APIs
em uma das áreas mais competitivas e contestadas da história dos computadores
e da internet. Empresas notaram a capacidade de controlar e lucrar dessa
parte da industria que os desenvolvedores tem usando suas APIs; Ao prover
aplicações gratuitas, os desenvolvedores esperam um maior uso de seus
softwares por parte do publico, ainda que esperem que outros desenvolvedores
paguem royalties para poder usar seus softwares com intuito de criar
ferramentas uteis para os usuários, enquanto outros disponibilizam suas APIs
livremente.
