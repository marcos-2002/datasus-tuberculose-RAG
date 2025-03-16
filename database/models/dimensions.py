from tortoise.models import Model
from tortoise import fields

class Ano(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=255)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "anos"

    def __str__(self):
        return self.nome

class Mes(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=255)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "meses"

    def __str__(self):
        return self.nome
    
class RegiaoNotif(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=255)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "regioes_notif"

    def __str__(self):
        return self.nome


class UFNotif(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "ufs_notif"

    def __str__(self):
        return self.nome
    
class MunicipioNotif(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "municipios_notif"

    def __str__(self):
        return self.nome
    
class CapitalNotif(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "capitais_notif"

    def __str__(self):
        return self.nome
    
class MacrorregNotif(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "macrorregs_notif"

    def __str__(self):
        return self.nome
    
class MicrorregNotif(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "microrregs_notif"

    def __str__(self):
        return self.nome

class RegMetropNotif(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "reg_metrop_notif"

    def __str__(self):
        return self.nome
    

class TerritCidadaniaNotif(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "territ_cidadanias_notif"

    def __str__(self):
        return self.nome

class MesorregiaoNotif(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "meso_regioes_notif"

    def __str__(self):
        return self.nome

class RegiaoSaudeNotif(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "regioes_saude_notif"

    def __str__(self):
        return self.nome
    
class AmazoniaLegalNotif(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "amazonia_legal_notif"

    def __str__(self):
        return self.nome
    
class SemiaridoNotif(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "semiaridos_notif"

    def __str__(self):
        return self.nome
       
class FaixaFronteiraNotif(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "faixa_fronteiras_notif"

    def __str__(self):
        return self.nome

class ZonaFronteiraNotif(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "zona_fronteiras_notif"

    def __str__(self):
        return self.nome
    
class MunExtremaPobrezaNotif(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "mun_extrema_pobreza_notif"

    def __str__(self):
        return self.nome
    
class RegiaoResidencia(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "regioes_residencia"

    def __str__(self):
        return self.nome

class UFResid(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "ufs_resid"

    def __str__(self):
        return self.nome
    
class MunicipioResid(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "municipios_resid"

    def __str__(self):
        return self.nome
    
class CapitalResid(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "capitais_resid"

    def __str__(self):
        return self.nome

class RegiaoSaudeResid(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "regioes_saude_resid"

    def __str__(self):
        return self.nome

class MacroRegSaudeResid(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "macro_regioes_saude_resid"

    def __str__(self):
        return self.nome
    
class MicroRegSaudeResid(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "micro_regioes_saude_resid"

    def __str__(self):
        return self.nome
    
class RegMetropResid(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "regioes_metrop_resid"

    def __str__(self):
        return self.nome
    
class TerritCidadaniaResid(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "territ_cidadania_resid"

    def __str__(self):
        return self.nome

class MesoRegiaopPNDRResid(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "meso_regioes_PNDR_resid"

    def __str__(self):
        return self.nome
    
class AmazoniaLegalResid(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "amazonia_legal_resid"

    def __str__(self):
        return self.nome

class SemiaridoResid(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "semiarido_resid"

    def __str__(self):
        return self.nome
    
class FaixaFrontResid(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "faixa_front_resid"

    def __str__(self):
        return self.nome

class ZonaFrontResid(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "zona_front_resid"

    def __str__(self):
        return self.nome

class MunExtremaPobrResid(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "mun_extrema_pobr_resid"

    def __str__(self):
        return self.nome

class ZonaResid(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "zona_resid"

    def __str__(self):
        return self.nome

class FxEtaria(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "fx_etarias"

    def __str__(self):
        return self.nome

class FxEtaria7(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "fx_etarias7"

    def __str__(self):
        return self.nome

class FxEtaria13(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "fx_etarias13"

    def __str__(self):
        return self.nome

class Raca(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "racas"

    def __str__(self):
        return self.nome

class Sexo(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "sexos"

    def __str__(self):
        return self.nome

class TipoEntrada(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "tipos_entrada"

    def __str__(self):
        return self.nome

class Institucionalizado(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "institucionalizado"

    def __str__(self):
        return self.nome

class PopSitRua(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "pop_sit_rua"

    def __str__(self):
        return self.nome

class ProfSaude(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "prof_saude"

    def __str__(self):
        return self.nome

class BenefGoverno(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "benef_governo"

    def __str__(self):
        return self.nome

class Forma(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "formas"

    def __str__(self):
        return self.nome

class ExtraPulm1(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "extra_pulm1"

    def __str__(self):
        return self.nome

class ExtraPulm2(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "extra_pulm2"

    def __str__(self):
        return self.nome

class Aids(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "aids"

    def __str__(self):
        return self.nome

class PPL(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "ppl"

    def __str__(self):
        return self.nome
    
class Alcoolismo(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "alcoolismo"

    def __str__(self):
        return self.nome

class Imigrante(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "imigrante"

    def __str__(self):
        return self.nome

class Diabetes(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "diabetes"

    def __str__(self):
        return self.nome

class DoencaMental(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "doenca_mental"

    def __str__(self):
        return self.nome

class DrogasIlicitas(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "drogas_ilicitas"

    def __str__(self):
        return self.nome

class Tabagismo(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "tabagismo"

    def __str__(self):
        return self.nome

class OutraDoenca(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "outra_doenca"

    def __str__(self):
        return self.nome

class ConfirmacaoLaboratorial(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "confirmacao_laboratorial"

    def __str__(self):
        return self.nome

class BacEscarro1(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "bac_escarro1"

    def __str__(self):
        return self.nome

class BacEscarro2(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "bac_escarro2"

    def __str__(self):
        return self.nome

class CulturaEscarro(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "cultura_escarro"

    def __str__(self):
        return self.nome

class TesteRapidoTB(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "teste_rapido_tb"

    def __str__(self):
        return self.nome

class TesteSensibilidade(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "teste_sensibilidade"

    def __str__(self):
        return self.nome

class HIV(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "hiv"

    def __str__(self):
        return self.nome

class Antirretroviral(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "antirretroviral"

    def __str__(self):
        return self.nome

class TDORealizado(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "tdo_realizado"

    def __str__(self):
        return self.nome

class Bacilosc2Mes(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "bacilosc_2mes"

    def __str__(self):
        return self.nome

class Bacilosc6Mes(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "bacilosc_6mes"

    def __str__(self):
        return self.nome

class SituacaoEncerra(Model):
    id = fields.BigIntField(primary_key=True)
    nome = fields.CharField(max_length=5000)
    criado_em = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "situacao_encerra"

    def __str__(self):
        return self.nome
