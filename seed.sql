-- Inserções para a tabela tipo_entrada
INSERT INTO tipo_entrada (id, nome) VALUES (1, 'Caso Novo');
INSERT INTO tipo_entrada (id, nome) VALUES (2, 'Recidiva');
INSERT INTO tipo_entrada (id, nome) VALUES (3, 'Reingresso após Abandono');
INSERT INTO tipo_entrada (id, nome) VALUES (4, 'Não Sabe');
INSERT INTO tipo_entrada (id, nome) VALUES (5, 'Transferência');
INSERT INTO tipo_entrada (id, nome) VALUES (6, 'Pós-óbito');

-- Inserções para a tabela ppl
INSERT INTO ppl (id, nome) VALUES (1, 'Sim');
INSERT INTO ppl (id, nome) VALUES (2, 'Não');
INSERT INTO ppl (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela pop_sit_rua
INSERT INTO pop_sit_rua (id, nome) VALUES (1, 'Sim');
INSERT INTO pop_sit_rua (id, nome) VALUES (2, 'Não');
INSERT INTO pop_sit_rua (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela prof_saude
INSERT INTO prof_saude (id, nome) VALUES (1, 'Sim');
INSERT INTO prof_saude (id, nome) VALUES (2, 'Não');
INSERT INTO prof_saude (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela imigrante
INSERT INTO imigrante (id, nome) VALUES (1, 'Sim');
INSERT INTO imigrante (id, nome) VALUES (2, 'Não');
INSERT INTO imigrante (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela benef_governo
INSERT INTO benef_governo (id, nome) VALUES (1, 'Sim');
INSERT INTO benef_governo (id, nome) VALUES (2, 'Não');
INSERT INTO benef_governo (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela forma
INSERT INTO forma (id, nome) VALUES (1, 'Pulmonar');
INSERT INTO forma (id, nome) VALUES (2, 'Extrapulmonar');
INSERT INTO forma (id, nome) VALUES (3, 'Pulmonar + Extrapulmonar');

-- Inserções para a tabela extra_pulm1
INSERT INTO extra_pulm1 (id, nome) VALUES (1, 'Pleural');
INSERT INTO extra_pulm1 (id, nome) VALUES (2, 'Gang. Perif.');
INSERT INTO extra_pulm1 (id, nome) VALUES (3, 'Geniturinária');
INSERT INTO extra_pulm1 (id, nome) VALUES (4, 'Óssea');
INSERT INTO extra_pulm1 (id, nome) VALUES (5, 'Ocular');
INSERT INTO extra_pulm1 (id, nome) VALUES (6, 'Miliar');
INSERT INTO extra_pulm1 (id, nome) VALUES (7, 'Meningoencefálico');
INSERT INTO extra_pulm1 (id, nome) VALUES (8, 'Cutânea');
INSERT INTO extra_pulm1 (id, nome) VALUES (9, 'Laringea');
INSERT INTO extra_pulm1 (id, nome) VALUES (10, 'Outra');

-- Inserções para a tabela aids
INSERT INTO aids (id, nome) VALUES (1, 'Sim');
INSERT INTO aids (id, nome) VALUES (2, 'Não');
INSERT INTO aids (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela alcoolismo
INSERT INTO alcoolismo (id, nome) VALUES (1, 'Sim');
INSERT INTO alcoolismo (id, nome) VALUES (2, 'Não');
INSERT INTO alcoolismo (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela diabetes
INSERT INTO diabetes (id, nome) VALUES (1, 'Sim');
INSERT INTO diabetes (id, nome) VALUES (2, 'Não');
INSERT INTO diabetes (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela doenca_mental
INSERT INTO doenca_mental (id, nome) VALUES (1, 'Sim');
INSERT INTO doenca_mental (id, nome) VALUES (2, 'Não');
INSERT INTO doenca_mental (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela droga_ilicita
INSERT INTO droga_ilicita (id, nome) VALUES (1, 'Sim');
INSERT INTO droga_ilicita (id, nome) VALUES (2, 'Não');
INSERT INTO droga_ilicita (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela tabagismo
INSERT INTO tabagismo (id, nome) VALUES (1, 'Sim');
INSERT INTO tabagismo (id, nome) VALUES (2, 'Não');
INSERT INTO tabagismo (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela outra_doenca
INSERT INTO outra_doenca (id, nome) VALUES (1, 'Sim');
INSERT INTO outra_doenca (id, nome) VALUES (2, 'Não');
INSERT INTO outra_doenca (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela raio_x
INSERT INTO raio_x (id, nome) VALUES (1, 'Suspeito');
INSERT INTO raio_x (id, nome) VALUES (2, 'Normal');
INSERT INTO raio_x (id, nome) VALUES (3, 'Outra patologia');
INSERT INTO raio_x (id, nome) VALUES (4, 'Não realizado');

-- Inserções para a tabela hiv
INSERT INTO hiv (id, nome) VALUES (1, 'Positivo');
INSERT INTO hiv (id, nome) VALUES (2, 'Negativo');
INSERT INTO hiv (id, nome) VALUES (3, 'Em andamento');
INSERT INTO hiv (id, nome) VALUES (4, 'Não realizado');

-- Inserções para a tabela antirretroviral
INSERT INTO antirretroviral (id, nome) VALUES (1, 'Sim');
INSERT INTO antirretroviral (id, nome) VALUES (2, 'Não');
INSERT INTO antirretroviral (id, nome) VALUES (9, 'Ignorado');

-- Inserções para a tabela cultura_escarro
INSERT INTO cultura_escarro (id, nome) VALUES (1, 'Positiva');
INSERT INTO cultura_escarro (id, nome) VALUES (2, 'Negativa');
INSERT INTO cultura_escarro (id, nome) VALUES (3, 'Em andamento');
INSERT INTO cultura_escarro (id, nome) VALUES (4, 'Não realizada');

-- Inserções para a tabela teste_molec
INSERT INTO teste_molec (id, nome) VALUES (1, 'Detectável sensível à Rifampicina');
INSERT INTO teste_molec (id, nome) VALUES (2, 'Detectável resistente à Rifampicina');
INSERT INTO teste_molec (id, nome) VALUES (3, 'Não detectável');
INSERT INTO teste_molec (id, nome) VALUES (4, 'Inconclusivo');
INSERT INTO teste_molec (id, nome) VALUES (5, 'Não realizado');

-- Inserções para a tabela teste_sensibilidade
INSERT INTO teste_sensibilidade (id, nome) VALUES (1, 'Resistente somente à Isoniazida');
INSERT INTO teste_sensibilidade (id, nome) VALUES (2, 'Resistente somente à Rifampicina');
INSERT INTO teste_sensibilidade (id, nome) VALUES (3, 'Resistente à Isoniazida e Rifampicina');
INSERT INTO teste_sensibilidade (id, nome) VALUES (4, 'Resistente a outras drogas de 1ª linha');
INSERT INTO teste_sensibilidade (id, nome) VALUES (5, 'Sensível');
INSERT INTO teste_sensibilidade (id, nome) VALUES (6, 'Em andamento');
INSERT INTO teste_sensibilidade (id, nome) VALUES (7, 'Não realizado');

INSERT INTO banco_metadados (nome_tabela, descricao_tabela, categorias) VALUES (
'situacao_encerra', 
'Situação de Encerramento refere-se ao motivo pelo qual um caso foi finalizado no sistema de acompanhamento', 
'Os tipos possíveis de encerramento são:
GN/Branco: Caso sem informação de encerramento registrada.
Cura: Paciente completou o tratamento e foi considerado curado.
Abandono: Paciente interrompeu o tratamento antes da conclusão.
Óbito por tuberculose: Paciente faleceu devido à tuberculose.
Óbito por outras causas: Paciente faleceu por motivos não relacionados à tuberculose.
Transferência: Paciente foi encaminhado para outra unidade de saúde.
TB-DR (Tuberculose Drogarresistente): Caso identificado como tuberculose resistente a medicamentos.
Mudança de Esquema: Alteração no tratamento devido a necessidade clínica.
Falência: Falha no tratamento, sem resposta ao esquema terapêutico.
Abandono Primário: Paciente diagnosticado, mas não iniciou o tratamento.'
);

INSERT INTO banco_metadados (nome_tabela, descricao_tabela, categorias) VALUES (
'bacilosc_2mes',
'Baciloscopia no 2º Mês refere-se ao resultado do exame de baciloscopia realizado dois meses após o início do tratamento para tuberculose',
'Os possíveis resultados são:
Ign/Branco: Informação não registrada ou ignorada.
Positivo: Baciloscopia detectou a presença do bacilo da tuberculose, indicando possível falha no tratamento.
Negativo: Baciloscopia não detectou o bacilo, sugerindo boa resposta ao tratamento.
Não realizado: Exame não foi feito por qualquer motivo.
Não se aplica: Situação em que a realização do exame não é necessária para o caso.'
);

INSERT INTO banco_metadados (nome_tabela, descricao_tabela, categorias) VALUES (
'tdo_realizado',
'TDO Realizado refere-se à observação direta do tratamento da tuberculose, em que um profissional de saúde supervisiona a administração dos medicamentos pelo paciente',
'As possíveis situações são:
Sim: O paciente realizou o tratamento diretamente observado (TDO) conforme recomendado.
Não: O paciente não realizou o tratamento sob observação direta.'
);

INSERT INTO banco_metadados (nome_tabela, descricao_tabela, categorias) VALUES (
'antirretroviral',
'Uso de Antirretroviral refere-se à administração de medicamentos antirretrovirais para pacientes com tuberculose que também vivem com HIV',
'As possíveis situações são Ign/Branco. Sim: O paciente faz uso de terapia antirretroviral (TARV) para o tratamento do HIV.
Não: O paciente não faz uso de terapia antirretroviral.'
);

INSERT INTO banco_metadados (nome_tabela, descricao_tabela, categorias) VALUES (
'hiv',
'Status de HIV refere-se ao resultado do teste para o vírus da imunodeficiência humana (HIV) em pacientes com tuberculose.',
'As possíveis situações são:
Ign/Branco: Informação não registrada ou ignorada.
Positivo: Paciente testou positivo para HIV.
Negativo: Paciente testou negativo para HIV.
Em andamento: Teste foi realizado, mas o resultado ainda não está disponível.
Não realizado: Teste não foi feito por qualquer motivo.'
);

INSERT INTO banco_metadados (nome_tabela, descricao_tabela, categorias) VALUES (
'teste_sensibilidade',
'Teste de Sensibilidade refere-se à análise laboratorial que avalia a resposta da tuberculose aos medicamentos usados no tratamento.',
'Os possíveis resultados são:
Ign/Branco: Informação não registrada ou ignorada.
Resist Isoniazida: Tuberculose resistente ao antibiótico Isoniazida.
Resist Rifampicina: Tuberculose resistente ao antibiótico Rifampicina.
Resist Ison e Rifa: Resistência simultânea à Isoniazida e Rifampicina, caracterizando Tuberculose Multirresistente (TB-MDR).
Resist drogas 1ª linha: Resistência a outros medicamentos da primeira linha do tratamento da tuberculose.
Sensível: Bacilos da tuberculose são sensíveis aos medicamentos testados, indicando que o tratamento padrão deve ser eficaz.
Em andamento: Teste foi realizado, mas o resultado ainda não está disponível.
Não realizado: O exame não foi feito'
);

INSERT INTO banco_metadados (nome_tabela, descricao_tabela, categorias) VALUES (
'teste_rapido_tb',
'Teste Rápido para Tuberculose (TB) refere-se a um exame molecular utilizado para detectar a presença do bacilo da tuberculose e sua resistência à Rifampicina, um dos principais medicamentos do tratamento.',
'Os possíveis resultados são:
Ign/Branco: Informação não registrada ou ignorada.
Detect Sensível Rifampicina: Tuberculose detectada, mas o bacilo é sensível à Rifampicina, indicando que o tratamento padrão deve ser eficaz.
Detect Resistente Rifampicina: Tuberculose detectada com resistência à Rifampicina, podendo indicar um caso de Tuberculose Multirresistente (TB-MDR).
Não Detectável: Bacilo da tuberculose não foi identificado na amostra testada.
Inconclusivo: O exame não forneceu um resultado definitivo, podendo ser necessário repeti-lo.
Não realizado: O teste não foi feito.'
);

INSERT INTO banco_metadados (nome_tabela, descricao_tabela, categorias) VALUES (
'cultura_escarro',
'Cultura de Escarro é um exame laboratorial utilizado para diagnosticar a tuberculose, detectando a presença do Mycobacterium tuberculosis em amostras de escarro',
'Os possíveis resultados são:
Ign/Branco: Informação não registrada ou ignorada.
Positivo: A cultura detectou a presença do Mycobacterium tuberculosis, confirmando o diagnóstico de tuberculose ativa.
Negativo: A cultura não detectou o bacilo da tuberculose na amostra testada.
Em andamento: O exame foi realizado, mas o resultado ainda não está disponível.
Não realizado: O teste não foi feito.'
);

INSERT INTO banco_metadados (nome_tabela, descricao_tabela, categorias) VALUES (
'bac_escarro2',
'2ª Baciloscopia de Escarro refere-se a um segundo exame de baciloscopia realizado para monitoramento ou confirmação da tuberculose',
'Os possíveis resultados são:
Ign/Branco: Informação não registrada ou ignorada.
Positivo: O exame detectou a presença do bacilo da tuberculose, indicando possível falha no tratamento ou persistência da infecção.
Negativo: O exame não detectou o bacilo, sugerindo boa resposta ao tratamento.
Não realizado: O teste não foi feito.'
);

INSERT INTO banco_metadados (nome_tabela, descricao_tabela, categorias) VALUES (
'confirmacao_laboratorial',
'Confirmação Laboratorial refere-se à verificação da presença do Mycobacterium tuberculosis por meio de exames laboratoriais',
'Os possíveis status são:
Com Confirmação Laboratorial: Casos em que a tuberculose foi diagnosticada por meio de exames como baciloscopia, cultura, ou teste molecular.
Sem Confirmação Laboratorial: Casos diagnosticados clinicamente, sem confirmação por exames laboratoriais.'
);

INSERT INTO banco_metadados (nome_tabela, descricao_tabela, categorias) VALUES (
'outra_doenca',
'Presença de Outra Doença indica se o paciente com tuberculose possui outra condição de saúde associada',
'Os possíveis status são:
Ign/Branco: Informação não registrada ou ignorada.
Sim: O paciente possui outra doença além da tuberculose.
Não: O paciente não apresenta outra doença associada.'
);

INSERT INTO banco_metadados (nome_tabela, descricao_tabela, categorias) VALUES (
'tabagismo',
'Tabagismo refere-se ao histórico de uso de tabaco pelo paciente com tuberculose.',
'Os possíveis status são:
Ign/Branco: Informação não registrada ou ignorada.
Sim: O paciente é ou foi fumante.
Não: O paciente não tem histórico de tabagismo.'
);

INSERT INTO banco_metadados (nome_tabela, descricao_tabela, categorias) VALUES (
'drogas_ilicitas',
'Uso de Drogas Ilícitas refere-se ao histórico de consumo de substâncias ilícitas por pacientes com tuberculose.',
'Os possíveis status são:
Ign/Branco: Informação não registrada ou ignorada.
Sim: O paciente faz ou fez uso de drogas ilícitas.
Não: O paciente não tem histórico de uso de drogas ilícitas.'
);

INSERT INTO banco_metadados (nome_tabela, descricao_tabela, categorias) VALUES (
'doenca_mental',
'Doença Mental refere-se à presença de transtornos psiquiátricos diagnosticados em pacientes com tuberculose.',
'Os possíveis status são:
Ign/Branco: Informação não registrada ou ignorada.
Sim: O paciente possui diagnóstico de doença mental.
Não: O paciente não apresenta histórico de doença mental.'
);

INSERT INTO banco_metadados (nome_tabela, descricao_tabela, categorias) VALUES (
'diabetes',
'Diabetes refere-se à presença de diabetes mellitus em pacientes com tuberculose.',
'Os possíveis status são:
Ign/Branco: Informação não registrada ou ignorada.
Sim: O paciente tem diagnóstico de diabetes.
Não: O paciente não tem histórico de diabetes.'
);

INSERT INTO banco_metadados (nome_tabela, descricao_tabela, categorias) VALUES (
'imigrante',
'Imigrante indica se o paciente é estrangeiro e reside em outro país ou se mudou recentemente para a região.',
'Os possíveis status são:
Ign/Branco: Informação não registrada ou ignorada.
Sim: O paciente é imigrante.
Não: O paciente não é imigrante.'
);

INSERT INTO banco_metadados (nome_tabela, descricao_tabela, categorias) VALUES (
'alcoolismo',
'Alcoolismo refere-se ao consumo excessivo e contínuo de álcool pelo paciente com tuberculose.',
'Os possíveis status são:
Ign/Branco: Informação não registrada ou ignorada.
Sim: O paciente faz ou fez uso abusivo de álcool.
Não: O paciente não tem histórico de alcoolismo.'
);

INSERT INTO banco_metadados (nome_tabela, descricao_tabela, categorias) VALUES (
'ppl',
'PPL refere-se a pacientes que encontram-se ou já estiveram em situação de privação de liberdade, como em presídios.',
'Os possíveis status são:
Ign/Branco: Informação não registrada ou ignorada.
Sim: O paciente é ou foi privado de liberdade.
Não: O paciente não tem histórico de privação de liberdade.'
);

INSERT INTO banco_metadados (nome_tabela, descricao_tabela, categorias) VALUES (
'aids',
'AIDS refere-se ao diagnóstico de Síndrome da Imunodeficiência Adquirida (AIDS) em pacientes com tuberculose.',
'Os possíveis status são:
Ign/Branco: Informação não registrada ou ignorada.
Sim: O paciente tem diagnóstico de AIDS.
Não: O paciente não tem diagnóstico de AIDS.'
);

INSERT INTO banco_metadados (nome_tabela, descricao_tabela, categorias) VALUES (
'extra_pulm1',
'Extra Pulmonar indica se a tuberculose do paciente tem manifestação fora dos pulmões, como em ossos, rins ou sistema nervoso.',
'Os possíveis status são:
Ign/Branco: Informação não registrada ou ignorada.
Sim: O paciente tem tuberculose extrapulmonar.
Não: O paciente não tem tuberculose extrapulmonar.'
);

INSERT INTO banco_metadados (nome_tabela, descricao_tabela, categorias) VALUES (
'benef_governo',
'Benefício do Governo indica se o paciente recebe algum tipo de auxílio financeiro ou social do governo.',
'Os possíveis status são:
Ign/Branco: Informação não registrada ou ignorada.
Sim: O paciente recebe benefício governamental.
Não: O paciente não recebe benefício governamental.'
);

INSERT INTO banco_metadados (nome_tabela, descricao_tabela, categorias) VALUES (
'pop_sit_rua',
'População em Situação de Rua indica se o paciente está ou esteve em situação de rua.',
'Os possíveis status são:
Ign/Branco: Informação não registrada ou ignorada.
Sim: O paciente está ou esteve em situação de rua.
Não: O paciente nunca esteve em situação de rua.'
);

INSERT INTO banco_metadados (nome_tabela, descricao_tabela, categorias) VALUES (
'prof_saude',
'Profissional de Saúde indica se o paciente trabalha ou já trabalhou na área da saúde, possivelmente com exposição à tuberculose.',
'Os possíveis status são:
Ign/Branco: Informação não registrada ou ignorada.
Sim: O paciente é ou foi profissional de saúde.
Não: O paciente não tem histórico de atuação na área da saúde.'
);

INSERT INTO banco_metadados (nome_tabela, descricao_tabela, categorias) VALUES (
'institucionalizado',
'Institucionalizado refere-se a pacientes que vivem ou viveram em instituições de longa permanência, como abrigos ou casas de repouso.',
'Os possíveis status são:
Ign/Branco: Informação não registrada ou ignorada.
Sim: O paciente vive ou viveu institucionalizado.
Não: O paciente não tem histórico de institucionalização.'
);

INSERT INTO banco_metadados (nome_tabela, descricao_tabela, categorias) VALUES (
'tipos_entrada',
'Tipos de Entrada refere-se à forma como o paciente foi identificado e inserido no sistema de acompanhamento da tuberculose.',
'Os possíveis status são:
Ign/Branco: Informação não registrada ou ignorada.
Novo Caso: Paciente diagnosticado pela primeira vez com tuberculose.
Recidiva: Paciente que já teve tuberculose anteriormente e apresentou novo episódio.
Reingresso após Abandono: Paciente que abandonou o tratamento e retornou para continuidade.
Pós-Tratamento de TB-DR: Paciente que finalizou tratamento para Tuberculose Drogarresistente e está sendo monitorado.
Transferência: Paciente transferido de outra unidade ou local para continuidade do tratamento.'
);

INSERT INTO banco_metadados (nome_tabela, descricao_tabela, categorias) VALUES (
'sexo',
'Sexo refere-se à identificação de gênero do paciente com tuberculose.',
'Os possíveis status são:
Ignorado: Informação sobre o sexo do paciente não registrada ou desconhecida.
Masculino: O paciente se identifica como do sexo masculino.
Feminino: O paciente se identifica como do sexo feminino.'
);