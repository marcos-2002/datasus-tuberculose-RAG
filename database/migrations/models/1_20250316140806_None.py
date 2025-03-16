from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "aids" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "alcoolismo" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "amazonia_legal_notif" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "amazonia_legal_resid" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "anos" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(255) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "antirretroviral" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "bac_escarro1" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "bac_escarro2" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "bacilosc_2mes" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "bacilosc_6mes" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "benef_governo" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "capitais_notif" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "capitais_resid" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "confirmacao_laboratorial" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "cultura_escarro" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "diabetes" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "doenca_mental" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "drogas_ilicitas" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "extra_pulm1" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "extra_pulm2" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "faixa_front_resid" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "faixa_fronteiras_notif" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "formas" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "fx_etarias" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "fx_etarias13" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "fx_etarias7" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "hiv" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "imigrante" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "institucionalizado" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "macro_regioes_saude_resid" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "macrorregs_notif" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "meses" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(255) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "meso_regioes_PNDR_resid" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "meso_regioes_notif" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "micro_regioes_saude_resid" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "microrregs_notif" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "mun_extrema_pobr_resid" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "mun_extrema_pobreza_notif" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "municipios_notif" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "municipios_resid" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "outra_doenca" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "ppl" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "pop_sit_rua" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "prof_saude" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "racas" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "reg_metrop_notif" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "regioes_metrop_resid" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "regioes_notif" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(255) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "regioes_residencia" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "regioes_saude_notif" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "regioes_saude_resid" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "semiaridos_notif" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "semiarido_resid" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "sexos" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "situacao_encerra" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "tdo_realizado" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "tabagismo" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "territ_cidadanias_notif" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "territ_cidadania_resid" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "teste_rapido_tb" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "teste_sensibilidade" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "tipos_entrada" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "ufs_notif" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "ufs_resid" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "zona_front_resid" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "zona_fronteiras_notif" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "zona_resid" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "nome" VARCHAR(5000) NOT NULL,
    "criado_em" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "fact_table" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "criado_em" TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    "aids_id_id" BIGINT REFERENCES "aids" ("id") ON DELETE CASCADE,
    "alcoolismo_id_id" BIGINT REFERENCES "alcoolismo" ("id") ON DELETE CASCADE,
    "amazonia_legal_notif_id_id" BIGINT REFERENCES "amazonia_legal_notif" ("id") ON DELETE CASCADE,
    "amazonia_legal_resid_id_id" BIGINT REFERENCES "amazonia_legal_resid" ("id") ON DELETE CASCADE,
    "antirretroviral_id_id" BIGINT REFERENCES "antirretroviral" ("id") ON DELETE CASCADE,
    "bac_escarro1_id_id" BIGINT REFERENCES "bac_escarro1" ("id") ON DELETE CASCADE,
    "bac_escarro2_id_id" BIGINT REFERENCES "bac_escarro2" ("id") ON DELETE CASCADE,
    "bacilosc_2mes_id_id" BIGINT REFERENCES "bacilosc_2mes" ("id") ON DELETE CASCADE,
    "bacilosc_6mes_id_id" BIGINT REFERENCES "bacilosc_6mes" ("id") ON DELETE CASCADE,
    "benef_governo_id_id" BIGINT REFERENCES "benef_governo" ("id") ON DELETE CASCADE,
    "capital_notif_id_id" BIGINT REFERENCES "capitais_notif" ("id") ON DELETE CASCADE,
    "capital_resid_id_id" BIGINT REFERENCES "capitais_resid" ("id") ON DELETE CASCADE,
    "confirmacao_laboratorial_id_id" BIGINT REFERENCES "confirmacao_laboratorial" ("id") ON DELETE CASCADE,
    "cultura_escarro_id_id" BIGINT REFERENCES "cultura_escarro" ("id") ON DELETE CASCADE,
    "diabetes_id_id" BIGINT REFERENCES "diabetes" ("id") ON DELETE CASCADE,
    "doenca_mental_id_id" BIGINT REFERENCES "doenca_mental" ("id") ON DELETE CASCADE,
    "drogas_ilicitas_id_id" BIGINT REFERENCES "drogas_ilicitas" ("id") ON DELETE CASCADE,
    "extra_pulm1_id_id" BIGINT REFERENCES "extra_pulm1" ("id") ON DELETE CASCADE,
    "extra_pulm2_id_id" BIGINT REFERENCES "extra_pulm2" ("id") ON DELETE CASCADE,
    "faixa_front_resid_id_id" BIGINT REFERENCES "faixa_front_resid" ("id") ON DELETE CASCADE,
    "faixa_fronteira_notif_id_id" BIGINT REFERENCES "faixa_fronteiras_notif" ("id") ON DELETE CASCADE,
    "forma_id_id" BIGINT REFERENCES "formas" ("id") ON DELETE CASCADE,
    "fx_etaria13_id_id" BIGINT REFERENCES "fx_etarias13" ("id") ON DELETE CASCADE,
    "fx_etaria7_id_id" BIGINT REFERENCES "fx_etarias7" ("id") ON DELETE CASCADE,
    "fx_etaria_id_id" BIGINT REFERENCES "fx_etarias" ("id") ON DELETE CASCADE,
    "hiv_id_id" BIGINT REFERENCES "hiv" ("id") ON DELETE CASCADE,
    "imigrante_id_id" BIGINT REFERENCES "imigrante" ("id") ON DELETE CASCADE,
    "institucionalizado_id_id" BIGINT REFERENCES "institucionalizado" ("id") ON DELETE CASCADE,
    "macro_reg_saude_resid_id_id" BIGINT REFERENCES "macro_regioes_saude_resid" ("id") ON DELETE CASCADE,
    "macrorreg_notif_id_id" BIGINT REFERENCES "macrorregs_notif" ("id") ON DELETE CASCADE,
    "meso_regiao_pndr_resid_id_id" BIGINT REFERENCES "meso_regioes_PNDR_resid" ("id") ON DELETE CASCADE,
    "mesorregiao_notif_id_id" BIGINT REFERENCES "meso_regioes_notif" ("id") ON DELETE CASCADE,
    "micro_reg_saude_resid_id_id" BIGINT REFERENCES "micro_regioes_saude_resid" ("id") ON DELETE CASCADE,
    "microrreg_notif_id_id" BIGINT REFERENCES "microrregs_notif" ("id") ON DELETE CASCADE,
    "mun_extrema_pobr_resid_id_id" BIGINT REFERENCES "mun_extrema_pobr_resid" ("id") ON DELETE CASCADE,
    "mun_extrema_pobreza_notif_id_id" BIGINT REFERENCES "mun_extrema_pobreza_notif" ("id") ON DELETE CASCADE,
    "municipio_notif_id_id" BIGINT REFERENCES "municipios_notif" ("id") ON DELETE CASCADE,
    "municipio_resid_id_id" BIGINT REFERENCES "municipios_resid" ("id") ON DELETE CASCADE,
    "outra_doenca_id_id" BIGINT REFERENCES "outra_doenca" ("id") ON DELETE CASCADE,
    "pop_sit_rua_id_id" BIGINT REFERENCES "pop_sit_rua" ("id") ON DELETE CASCADE,
    "ppl_id_id" BIGINT REFERENCES "ppl" ("id") ON DELETE CASCADE,
    "prof_saude_id_id" BIGINT REFERENCES "prof_saude" ("id") ON DELETE CASCADE,
    "raca_id_id" BIGINT REFERENCES "racas" ("id") ON DELETE CASCADE,
    "reg_metrop_notif_id_id" BIGINT REFERENCES "reg_metrop_notif" ("id") ON DELETE CASCADE,
    "reg_metrop_resid_id_id" BIGINT REFERENCES "regioes_metrop_resid" ("id") ON DELETE CASCADE,
    "regiao_notif_id_id" BIGINT REFERENCES "regioes_notif" ("id") ON DELETE CASCADE,
    "regiao_resid_id_id" BIGINT REFERENCES "regioes_residencia" ("id") ON DELETE CASCADE,
    "regiao_saude_notif_id_id" BIGINT REFERENCES "regioes_saude_notif" ("id") ON DELETE CASCADE,
    "regiao_saude_resid_id_id" BIGINT REFERENCES "regioes_saude_resid" ("id") ON DELETE CASCADE,
    "semiarido_notif_id_id" BIGINT REFERENCES "semiaridos_notif" ("id") ON DELETE CASCADE,
    "semiarido_resid_id_id" BIGINT REFERENCES "semiarido_resid" ("id") ON DELETE CASCADE,
    "sexo_id_id" BIGINT REFERENCES "sexos" ("id") ON DELETE CASCADE,
    "situacao_encerra_id_id" BIGINT REFERENCES "situacao_encerra" ("id") ON DELETE CASCADE,
    "tabagismo_id_id" BIGINT REFERENCES "tabagismo" ("id") ON DELETE CASCADE,
    "tdo_realizado_id_id" BIGINT REFERENCES "tdo_realizado" ("id") ON DELETE CASCADE,
    "territ_cidadania_notif_id_id" BIGINT REFERENCES "territ_cidadanias_notif" ("id") ON DELETE CASCADE,
    "territ_cidadania_resid_id_id" BIGINT REFERENCES "territ_cidadania_resid" ("id") ON DELETE CASCADE,
    "teste_rapido_tb_id_id" BIGINT REFERENCES "teste_rapido_tb" ("id") ON DELETE CASCADE,
    "teste_sensibilidade_id_id" BIGINT REFERENCES "teste_sensibilidade" ("id") ON DELETE CASCADE,
    "tipo_entrada_id_id" BIGINT REFERENCES "tipos_entrada" ("id") ON DELETE CASCADE,
    "uf_notif_id_id" BIGINT REFERENCES "ufs_notif" ("id") ON DELETE CASCADE,
    "uf_resid_id_id" BIGINT REFERENCES "ufs_resid" ("id") ON DELETE CASCADE,
    "zona_front_resid_id_id" BIGINT REFERENCES "zona_front_resid" ("id") ON DELETE CASCADE,
    "zona_fronteira_notif_id_id" BIGINT REFERENCES "zona_fronteiras_notif" ("id") ON DELETE CASCADE,
    "zona_resid_id_id" BIGINT REFERENCES "zona_resid" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
