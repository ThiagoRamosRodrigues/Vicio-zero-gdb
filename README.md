Caminho para executar o projeto: Django-Doctor-Website-main\Gdb-Saude\django> Python manage.py runserver
Descrição do Fluxo Inicial da Página HOME: ![image](https://github.com/ThiagoRamosRodrigues/Vicio-zero-gdb/assets/112834625/eeb8443b-7061-4057-9652-e3b439f99a35) ![image](https://github.com/ThiagoRamosRodrigues/Vicio-zero-gdb/assets/112834625/5bbc1137-e807-4d43-ad7b-769dc69b72cf)
![image](https://github.com/ThiagoRamosRodrigues/Vicio-zero-gdb/assets/112834625/ba38a973-e247-4276-a89d-ef20d95a1ad2)



Nossa página inicial é projetada para facilitar o acesso e a interação dos usuários com os serviços médicos oferecidos.

Formulário de Consulta: ![image](https://github.com/ThiagoRamosRodrigues/Vicio-zero-gdb/assets/112834625/ed426598-be84-465f-b4f6-a22ba23642a9)


Ao clicar no botão para marcar uma consulta, os usuários são direcionados para preencher um formulário abrangente, incluindo campos para Nome, Sobrenome, Email, Número de Contato e um campo de Pedido, permitindo que eles forneçam detalhes adicionais relevantes para o médico. Uma vez enviado, esses dados são armazenados em nossa notificação de página, permitindo que os médicos acessem e revisem a lista de consultas pendentes.

Melhoria Adicional: Implementamos um painel de acesso restrito exclusivamente para médicos cadastrados, garantindo a segurança e a privacidade dos dados dos pacientes.

Formulário de Triagem: ![image](https://github.com/ThiagoRamosRodrigues/Vicio-zero-gdb/assets/112834625/ed3b132d-60e8-4f21-abc2-8fcf5b629b02)


Para clientes que não têm certeza sobre qual profissional procurar, oferecemos um formulário de triagem. Os clientes podem compartilhar suas preocupações e sintomas, e nossos administradores conduzem uma triagem, encaminhando-os para o médico especializado mais apropriado.

Melhoria Adicional: Desenvolvemos uma automação para identificar automaticamente o profissional mais adequado com base nas informações fornecidas, e enviamos aos clientes detalhes do médico, incluindo localização, área de atuação, número de contato e pré-agendamento para consulta.

Formulário de Consulta de Profissional: ![image](https://github.com/ThiagoRamosRodrigues/Vicio-zero-gdb/assets/112834625/bdd80574-aa07-4e51-856b-0e11f7c94584)


Para usuários que já têm uma preferência por um profissional específico, oferecemos um formulário de consulta dedicado. Eles podem usar filtros para localizar rapidamente o médico desejado e entrar em contato para marcar uma consulta.

Melhoria Adicional: Implementamos um sistema automatizado para adicionar novos profissionais diretamente ao nosso sistema por meio de um CASE, garantindo uma atualização contínua da lista de profissionais disponíveis. Além disso, integramos uma API de MAPS para exibir a localização de cada médico com base no CEP, facilitando a localização para os usuários.

Tecnologias Utilizadas:

Nosso sistema é desenvolvido principalmente em Python para a lógica do banco de dados (models.py) e em JavaScript para a lógica do formulário, utilizando HTML, CSS e Bootstrap para o design e a interface do usuário. Além disso, integramos uma API de MAPS para melhorar a experiência do usuário na localização dos médicos.

Melhoria Adicional para a Receita do Sistema:

Para garantir a sustentabilidade do nosso sistema, implementamos um formulário para que os médicos interessados em se cadastrar possam entrar em contato conosco. Oferecemos hospedagem e destaque aos médicos cadastrados, promovendo uma parceria benéfica para ambas as partes e garantindo uma fonte de renda para manter e aprimorar nossos serviços.

