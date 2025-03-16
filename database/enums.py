from enum import Enum
from typing import Self
from database.models import (
    RegiaoNotif,
    UFNotif,
    MunicipioNotif,
    CapitalNotif,
    MacrorregNotif,
    MicrorregNotif,
    RegMetropNotif,
    TerritCidadaniaNotif,
    MesorregiaoNotif,
    AmazoniaLegalNotif,
    SemiaridoNotif,
    FaixaFronteiraNotif,
    ZonaFronteiraNotif,
    MunExtremaPobrezaNotif,
    UFResid,
    MunicipioResid,
    CapitalResid,
    RegiaoSaudeResid,
    MacroRegSaudeResid,
    MicroRegSaudeResid,
    RegMetropResid,
    TerritCidadaniaResid,
    MesoRegiaopPNDRResid,
    AmazoniaLegalResid,
    SemiaridoResid,
    FaixaFrontResid,
    ZonaFrontResid,
    MunExtremaPobrResid,
    ZonaResid,
    FxEtaria,
    FxEtaria7,
    FxEtaria13,
    Raca,
    Sexo,
    TipoEntrada,
    Institucionalizado,
    PopSitRua,
    ProfSaude,
    BenefGoverno,
    Forma,
    ExtraPulm1,
    ExtraPulm2,
    Aids,
    Alcoolismo,
    Diabetes,
    DoencaMental,
    DrogasIlicitas,
    Tabagismo,
    OutraDoenca,
    ConfirmacaoLaboratorial,
    BacEscarro1,
    BacEscarro2,
    CulturaEscarro,
    TesteRapidoTB,
    TesteSensibilidade,
    HIV,
    Antirretroviral,
    TDORealizado,
    Bacilosc2Mes,
    Bacilosc6Mes,
    SituacaoEncerra,
    PPL,
    Imigrante,
)
from database.models.dimensions import Ano, Mes, RegiaoResidencia, RegiaoSaudeNotif

class DimensionEnum(Enum):
    """
    Represents the dimensions for the fact table.

    Each entry is structured as: (name, model, foreign_key_column)
    """
    from enum import Enum

class DimensionEnum(Enum):
    """
    Represents the dimensions for the fact table.

    Each entry is structured as: (name, model, foreign_key_column, api_value)
    """
    ANO = "ano", Ano, "ano_id", "ano"
    MES = "mes", Mes, "mes_id", "mes"
    REGIAO_NOTIF = "regiao_notif", RegiaoNotif, "regiao_notif_id", "Região de notificação"
    UF_NOTIF = "uf_notif", UFNotif, "uf_notif_id", "UF de notificação"
    MUNICIPIO_NOTIF = "municipio_notif", MunicipioNotif, "municipio_notif_id", "Município de notificação"
    CAPITAL_NOTIF = "capital_notif", CapitalNotif, "capital_notif_id", "Capital de notificação"
    MACRORREG_NOTIF = "macrorreg_notif", MacrorregNotif, "macrorreg_notif_id", "Macrorreg.de Saúde de notific"
    MICRORREG_NOTIF = "microrreg_notif", MicrorregNotif, "microrreg_notif_id", "Microrregião IBGE de notific"
    REG_METROP_NOTIF = "reg_metrop_notif", RegMetropNotif, "reg_metrop_notif_id", "Reg.Metropolit/RIDE de notific"
    TERRIT_CIDADANIA_NOTIF = "territ_cidadania_notif", TerritCidadaniaNotif, "territ_cidadania_notif_id", "Territ da Cidadania de notific"
    MESORREGIAO_NOTIF = "mesorregiao_notif", MesorregiaoNotif, "mesorregiao_notif_id", "Mesorregião PNDR de notific"
    REGIAO_SAUDE_NOTIF = "regiao_saude_notif", RegiaoSaudeNotif, "regiao_saude_notif_id", "Região de Saúde (CIR) de notif"
    AMAZONIA_LEGAL_NOTIF = "amazonia_legal_notif", AmazoniaLegalNotif, "amazonia_legal_notif_id", "Amazônia Legal de notificação"
    SEMIARIDO_NOTIF = "semiarido_notif", SemiaridoNotif, "semiarido_notif_id", "Semiárido de notificação"
    FAIXA_FRONTEIRA_NOTIF = "faixa_fronteira_notif", FaixaFronteiraNotif, "faixa_fronteira_notif_id", "Faixa de Fronteira de notificação"
    ZONA_FRONTEIRA_NOTIF = "zona_fronteira_notif", ZonaFronteiraNotif, "zona_fronteira_notif_id", "Zona de Fronteira de notificação"
    MUN_EXTREMA_POBREZA_NOTIF = "mun_extrema_pobreza_notif", MunExtremaPobrezaNotif, "mun_extrema_pobreza_notif_id", "Município de extrema pobreza de notificação"
    UF_RESID = "uf_resid", UFResid, "uf_resid_id", "UF de residência"
    REGIAO_RESID = "regiao_resid", RegiaoResidencia, "regiao_resid_id", "Região de residência"
    MUNICIPIO_RESID = "municipio_resid", MunicipioResid, "municipio_resid_id", "Município de residência"
    CAPITAL_RESID = "capital_resid", CapitalResid, "capital_resid_id", "Capital de residência"
    REGIAO_SAUDE_RESID = "regiao_saude_resid", RegiaoSaudeResid, "regiao_saude_resid_id", "Região de Saúde (CIR) de resid"
    MACRO_REG_SAUDE_RESID = "macro_reg_saude_resid", MacroRegSaudeResid, "macro_reg_saude_resid_id", "Macrorreg.de Saúde de residênc"
    MICRO_REG_SAUDE_RESID = "micro_reg_saude_resid", MicroRegSaudeResid, "micro_reg_saude_resid_id", "Microrregião IBGE de residênc"
    REG_METROP_RESID = "reg_metrop_resid", RegMetropResid, "reg_metrop_resid_id", "Reg.Metropolit/RIDE de resid"
    TERRIT_CIDADANIA_RESID = "territ_cidadania_resid", TerritCidadaniaResid, "territ_cidadania_resid_id", "Territ da Cidadania de resid"
    MESO_REGIAO_PNDR_RESID = "meso_regiao_pndr_resid", MesoRegiaopPNDRResid, "meso_regiao_pndr_resid_id", ""
    AMAZONIA_LEGAL_RESID = "amazonia_legal_resid", AmazoniaLegalResid, "amazonia_legal_resid_id", "Amazônia Legal de residência"
    SEMIARIDO_RESID = "semiarido_resid", SemiaridoResid, "semiarido_resid_id", "Semiárido de residência"
    FAIXA_FRONT_RESID = "faixa_front_resid", FaixaFrontResid, "faixa_front_resid_id", "Faixa de Fronteira de residência"
    ZONA_FRONT_RESID = "zona_front_resid", ZonaFrontResid, "zona_front_resid_id", "Zona de Fronteira de residência"
    MUN_EXTREMA_POBR_RESID = "mun_extrema_pobr_resid", MunExtremaPobrResid, "mun_extrema_pobr_resid_id", "Município de extrema pobreza de residência"
    ZONA_RESID = "zona_resid", ZonaResid, "zona_resid_id", "Zona de residência"
    PPL = "ppl", PPL, "ppl_id", "PPL"
    FX_ETARIA = "fx_etaria", FxEtaria, "fx_etaria_id", "Fx Etária"
    FX_ETARIA7 = "fx_etaria7", FxEtaria7, "fx_etaria7_id", "Fx Etária 7"
    FX_ETARIA13 = "fx_etaria13", FxEtaria13, "fx_etaria13_id", "Fx Etária 13"
    RACA = "raca", Raca, "raca_id", "Raça"
    SEXO = "sexo", Sexo, "sexo_id", "Sexo"
    TIPO_ENTRADA = "tipo_entrada", TipoEntrada, "tipo_entrada_id", "Tipo de entrada"
    INSTITUCIONALIZADO = "institucionalizado", Institucionalizado, "institucionalizado_id", "Institucionalizado"
    POP_SIT_RUA = "pop_sit_rua", PopSitRua, "pop_sit_rua_id", ""
    PROF_SAUDE = "prof_saude", ProfSaude, "prof_saude_id", ""
    BENEF_GOVERNO = "benef_governo", BenefGoverno, "benef_governo_id", "Benefic. governo"
    FORMA = "forma", Forma, "forma_id", "Forma"
    EXTRA_PULM1 = "extra_pulm1", ExtraPulm1, "extra_pulm1_id", "Se Extrapulm.1"
    EXTRA_PULM2 = "extra_pulm2", ExtraPulm2, "extra_pulm2_id", "Se Extrapulm.2"
    AIDS = "aids", Aids, "aids_id", "Aids"
    ALCOOLISMO = "alcoolismo", Alcoolismo, "alcoolismo_id", "Alcoolismo"
    DIABETES = "diabetes", Diabetes, "diabetes_id", "Diabetes"
    DOENCA_MENTAL = "doenca_mental", DoencaMental, "doenca_mental_id", "Doença mental"
    DROGAS_ILICITAS = "drogas_ilicitas", DrogasIlicitas, "drogas_ilicitas_id", "Drogas ilícitas"
    TABAGISMO = "tabagismo", Tabagismo, "tabagismo_id", "Tabagismo"
    OUTRA_DOENCA = "outra_doenca", OutraDoenca, "outra_doenca_id", "Outra doença"
    IMIGRANTE = "imigrante", Imigrante, "imigrante_id", "Imigrante"
    CONFIRMACAO_LABORATORIAL = "confirmacao_laboratorial", ConfirmacaoLaboratorial, "confirmacao_laboratorial_id", "Confirmação laboratorial"
    BAC_ESCARRO1 = "bac_escarro1", BacEscarro1, "bac_escarro1_id", "1ªBac Escarro"
    BAC_ESCARRO2 = "bac_escarro2", BacEscarro2, "bac_escarro2_id", ""
    CULTURA_ESCARRO = "cultura_escarro", CulturaEscarro, "cultura_escarro_id", ""
    TESTE_RAPIDO_TB = "teste_rapido_tb", TesteRapidoTB, "teste_rapido_tb_id", "Teste rápido TB"
    TESTE_SENSIBILIDADE = "teste_sensibilidade", TesteSensibilidade, "teste_sensibilidade_id", "Teste sensibilidade"
    HIV = "hiv", HIV, "hiv_id", "HIV"
    ANTIRRETROVIRAL = "antirretroviral", Antirretroviral, "antirretroviral_id", "Antirretroviral"
    TDO_REALIZADO = "tdo_realizado", TDORealizado, "tdo_realizado_id", "TDO realizado"
    BACILOSC_2MES = "bacilosc_2mes", Bacilosc2Mes, "bacilosc_2mes_id", "Bacilosc 2º mês"
    BACILOSC_6MES = "bacilosc_6mes", Bacilosc6Mes, "bacilosc_6mes_id", "Bacilosc 6º mês"
    SITUACAO_ENCERRA = "situacao_encerra", SituacaoEncerra, "situacao_encerra_id", "Situação Encerra."
    
    @property
    def ref(self):
        return self.value[0]

    @property
    def model(self):
        return self.value[1]

    @property
    def column(self):
        return self.value[2]

    @classmethod
    def get_ref_map(self) -> dict[str, Self]:
        map = {}

        for name in self._member_names_:
            enum = DimensionEnum[name]
            map[enum.ref] = enum

        return map