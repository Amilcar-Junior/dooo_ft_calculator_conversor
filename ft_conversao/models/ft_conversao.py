# -*- coding: utf-8 -*-

from odoo import models, fields, api
import math

class ft_conversao(models.Model):
    _name = 'ft_conversao'
    _description = ''

    name = fields.Char(string="name")
    potencia_dBw = fields.Float(string='potencia_dBw',required=False)
    potencia_dBv = fields.Float(string='potencia_dBv',required=False)
    potencia_dBm = fields.Float(string='potencia_dBm',required=False)
    potencia_dBu = fields.Float(string='potencia_dBu',required=False)
    potencia_dB = fields.Float(string='potencia_dB',required=False)
    potencia_uW = fields.Float(string='potencia_uW',required=False)
    potencia_mW = fields.Float(string='potencia_mW',required=False)
    potencia_W = fields.Float(string='potencia_W',required=False)
    potencia_kW = fields.Float(string='potencia_kW',required=False)
    potencia_MW = fields.Float(string='potencia_MW',required=False)
    potencia_GW = fields.Float(string='potencia_GW',required=False)
    potencia_TW = fields.Float(string='potencia_TW',required=False)
    tensao_v = fields.Float(string='tensao_v',required=False)
    potencia_saida = fields.Float(string='potencia_saida',required=False)
    potencia_entrada = fields.Float(string='potencia_entrada',required=False)

    #fields FM
    expressao_frequencia_fm = fields.Float(string='Expressão Frequencia do Sinal Modulado',required=False)
    frequencia_fo = fields.Float(string='frequencia_fo',required=False)
    tempo = fields.Float(string='tempo',required=False)
    constante_kf = fields.Float(string='constante_kf',required=False)
    amplitude_Am = fields.Float(string='amplitude_Am',required=False)
    amplitude_Ao = fields.Float(string='amplitude_Ao',required=False)
    frequencia_Wm = fields.Float(string='frequencia_Wm',required=False)
    desvio_frequencia = fields.Float(string='Desvio_frequencia_Δf',required=False)
    frequencia_fm = fields.Float(string='frequencia_fm',required=False)
    indice_modulacao = fields.Float(string='indice_modulacao_β',required=False)
    largura_banda = fields.Float(string='largura_banda',required=False)
    sinal_fm = fields.Float(string='sinal_fm',required=False)
    n_pares_bandas_laterais = fields.Float(string='n',required=False)
    jn_b = fields.Float(string='jn_b',required=False)
    An = fields.Float(string='An',required=False)
    frequencia_Wo = fields.Float(string='frequencia_Wo',required=False)

    # fields AM
    indice_modulacao_am = fields.Float(string='indice_modulacao_u',required=False)
    frequencia_fc = fields.Float(string='frequencia_fc',required=False)
    comprimento_onda = fields.Float(string='comprimento_onda_λ',required=False)
    velocidade_luz_c = fields.Float(string='velocidade_luz_c',required=False)
    potencia_Pp = fields.Float(string='potencia_portadora_Pp',required=False)
    potencia_Pbl = fields.Float(string='potencia_banda_laterais_Pbl',required=False)
    potencia_Ptotal = fields.Float(string='potencia_Ptotal',required=False)
    largura_faixa_sinal_modulado_Bam = fields.Float(string='largura_faixa_sinal_modulado_Bam',required=False)


    def converter(self):
        print("Converter")

    def calcular_potencia_dBw(self):
        self.potencia_dBw = 10 * math.log10(self.potencia_W / 1)

    def calcular_potencia_dBv(self):
        self.potencia_dBv = 20 * math.log10(self.tensao_v / 1)

    def calcular_potencia_dBm(self):
        # Calcula a potência em decibéis miliwatt (dBm)
        self.potencia_dBm = 10 * math.log10(self.potencia_mW / 1)

    def calcular_potencia_dBu(self):
        # Calcula a potência em decibéis micro (dBu)
        self.potencia_dBu = 20 * math.log10(self.potencia_uW / 1)

    def calcular_relacao_potencia_dB(self):
        # Calcula a relação de potência em decibéis (dB)
        self.potencia_dB = 20 * math.log10(self.potencia_saida / self.potencia_entrada)

    def dBw_para_dBm(self):
        # Converte a potência em decibéis watt (dBW) para decibéis miliwatt (dBm)
        self.potencia_dBm = self.potencia_dBw + 30

    def dBw_para_dBu(self):
        # Converte a potência em decibéis watt (dBW) para decibéis micro (dBu)
        self.potencia_dBu = self.potencia_dBw + 60

    def dBu_para_dBw(self):
        # Converte a potência em decibéis micro (dBu) para decibéis watt (dBW)
        self.potencia_dBw = self.potencia_dBu - 60

    def dBm_para_dBw(self):
        # Converte a potência em decibéis miliwatt (dBm) para decibéis watt (dBW)
        self.potencia_dBw = self.potencia_dBm - 30

    def converter_potencia_W(self):
        # Converte a potência em watts para outras unidades
        self.potencia_uW = self.potencia_W * math.pow(10, 6)
        self.potencia_mW = self.potencia_W * math.pow(10, 3)
        self.potencia_kW = self.potencia_W * math.pow(10, -3)
        self.potencia_MW = self.potencia_W * math.pow(10, -6)
        self.potencia_GW = self.potencia_W * math.pow(10, -9)
        self.potencia_TW = self.potencia_W * math.pow(10, -12)

    def converter_potencia_uW(self):
        # Converte a potência em micro watts para outras unidades
        self.potencia_W = self.potencia_uW * math.pow(10, -6)
        self.potencia_mW = self.potencia_uW * math.pow(10, -3)
        self.potencia_kW = self.potencia_uW * math.pow(10, -9)
        self.potencia_MW = self.potencia_uW * math.pow(10, -12)
        self.potencia_GW = self.potencia_uW * math.pow(10, -15)
        self.potencia_TW = self.potencia_uW * math.pow(10, -18)

    def converter_potencia_mW(self):
        # Converte a potência em miliwatts para outras unidades
        self.potencia_W = self.potencia_mW * math.pow(10, -3)
        self.potencia_uW = self.potencia_mW * math.pow(10, 3)
        self.potencia_kW = self.potencia_mW * math.pow(10, -6)
        self.potencia_MW = self.potencia_mW * math.pow(10, -9)
        self.potencia_GW = self.potencia_mW * math.pow(10, -12)
        self.potencia_TW = self.potencia_mW * math.pow(10, -15)

    def converter_potencia_kW(self):
        # Converte a potência em kilowatts para outras unidades
        self.potencia_W = self.potencia_kW * math.pow(10, 3)
        self.potencia_uW = self.potencia_kW * math.pow(10, 9)
        self.potencia_mW = self.potencia_kW * math.pow(10, 6)
        self.potencia_MW = self.potencia_kW * math.pow(10, 3)
        self.potencia_GW = self.potencia_kW * math.pow(10, -3)
        self.potencia_TW = self.potencia_kW * math.pow(10, -6)

    def converter_potencia_MW(self):
        # Converte a potência em megawatts para outras unidades
        self.potencia_W = self.potencia_MW * math.pow(10, 6)
        self.potencia_uW = self.potencia_MW * math.pow(10, 12)
        self.potencia_mW = self.potencia_MW * math.pow(10, 9)
        self.potencia_kW = self.potencia_MW * math.pow(10, 3)
        self.potencia_GW = self.potencia_MW * math.pow(10, -3)
        self.potencia_TW = self.potencia_MW * math.pow(10, -6)

    def converter_potencia_GW(self):
        # Converte a potência em gigawatts para outras unidades
        self.potencia_W = self.potencia_GW * math.pow(10, 9)
        self.potencia_uW = self.potencia_GW * math.pow(10, 15)
        self.potencia_mW = self.potencia_GW * math.pow(10, 12)
        self.potencia_kW = self.potencia_GW * math.pow(10, 6)
        self.potencia_MW = self.potencia_GW * math.pow(10, 3)
        self.potencia_TW = self.potencia_GW * math.pow(10, -3)

    def converter_potencia_TW(self):
        # Converte a potência em terawatts para outras unidades
        self.potencia_W = self.potencia_TW * math.pow(10, 12)
        self.potencia_uW = self.potencia_TW * math.pow(10, 18)
        self.potencia_mW = self.potencia_TW * math.pow(10, 15)
        self.potencia_kW = self.potencia_TW * math.pow(10, 9)
        self.potencia_MW = self.potencia_TW * math.pow(10, 6)
        self.potencia_GW = self.potencia_TW * math.pow(10, 3)

    def calcular_expressao_frequencia_fm(self):
        self.expressao_frequencia_fm = self.frequencia_fo * self.tempo + \
                                       self.constante_kf * self.amplitude_Am * \
                                       math.cos(self.frequencia_Wm * self.tempo)

    def calcular_desvio_frequencia(self):
        # Δf = Kf * Am
        self.desvio_frequencia = self.constante_kf * self.amplitude_Am

    def calcular_indice_modulacao_fm(self):
        # β = Δf / fm
        self.indice_modulacao = self.desvio_frequencia / self.frequencia_fm

    def calcular_largura_banda(self):
        # B = 2(β + 1)fm
        self.largura_banda = 2 * (self.indice_modulacao + 1) * self.frequencia_fm

    def calcular_largura_banda_2(self):
        # B = 2Δf + 2fm
        self.largura_banda = 2 * self.desvio_frequencia + 2 * self.frequencia_fm

    def calcular_sinal_fm(self):
        # Sfm(t) = Ao * cos[2π fo t + β * sin(2π fm t)]
        self.sinal_fm = self.amplitude_Ao * \
                        math.cos(2 * math.pi * self.frequencia_fo *
                        self.tempo + self.indice_modulacao *
                        math.sin(2 * math.pi * self.frequencia_fm * self.tempo))

    def calcular_Wm(self):
        # Wm = 2π fm
        self.frequencia_Wm = 2 * math.pi * self.frequencia_fm

    def calcular_n_pares_bandas_laterais(self):
        # n = β + 1
        self.n_pares_bandas_laterais = self.indice_modulacao + 1

    def calcular_espectro(self):
        self.An = self.jn_b * self.amplitude_Ao * math.cos(self.frequencia_Wo * self.tempo)

    def calcular_espectro_resumido(self):
        self.An = self.jn_b * self.amplitude_Ao

    def calcular_indice_modulacao_am(self):
        # μ = Am / Ap
        self.indice_modulacao_am = self.amplitude_Am / self.amplitude_Ao

    def calcular_comprimento_onda(self):
        # λ = c / fc
        self.comprimento_onda = self.velocidade_luz_c / self.frequencia_fc

    def calcular_potencia_portadora(self):
        # Pp = Ap² / 2
        self.potencia_Pp = pow(self.amplitude_Ao, 2) / 2

    def calcular_potencia_bandas_laterais(self):
        # Pbl = (Ap * U)² / 4
        self.potencia_Pbl = pow(self.amplitude_Ao * self.indice_modulacao_am, 2) / 4

    def calcular_potencia_total(self):
        # Ptotal = Pp + Pbl
        self.potencia_Ptotal = self.potencia_Pp + self.potencia_Pbl

    def calcular_largura_faixa_sinal_modulado(self):
        # Bam = 2fm
        self.largura_faixa_sinal_modulado_Bam = 2 * self.frequencia_fm