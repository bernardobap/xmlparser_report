import xml.etree.ElementTree as et
from pandas import DataFrame
import feather

tree = et.parse('report.xml')
root = tree.getroot()

# Dicionário para guardar variáveis de Strain com os respectivos valores
strain_dict = {}

# Criar variável nome extraindo do report.xml e adicionar ao dicionário strain_dict
nome_split = str.split(root.find("Patient/Name").attrib['val'], sep=' ')
nome_split.append(nome_split[0])
nome_split.pop(0)
nome = ' '.join(nome_split)
strain_dict['nome'] = nome

# Definição de variáveis que não serão extraídas do Strains de Eixo Longo (LAX)
del_keys_lax = [
    'TimeToPeakStrainRadial',
    'TimeToPeakStrainLongitudinal',
    'PeakDiastolicStrainRateRadial',
    'PeakDiastolicStrainRateLongitudinal',
    'PeakDisplacementRadial',
    'PeakDisplacementLongitudinal',
    'TimeToPeakDisplacementRadial',
    'TimeToPeakDisplacementLongitudinal',
    'PeakSystolicVelocityRadial',
    'PeakSystolicVelocityLongitudinal',
    'PeakDiastolicVelocityRadial',
    'PeakDiastolicVelocityLongitudinal'
]

# Criar dicionário (com variável e valor) para Strain de Eixo Longo extraindo dados do report.xml
lax_dict = {}
segment = int()

for i in root.find("AllMeasurementsReport/LongAxisPolarmapData"):
    if i.tag == 'AHA_segment':
        segment = i.attrib['val']
    elif i.tag in del_keys_lax: # del_keys_lax não serão extraídas do report.xml 
        pass
    else:
        lax_dict['lax_' + i.tag.lower() + '_seg' + str(segment)] = list(i.attrib.values())

for v in lax_dict.values():
    if len(v) == 2:
        v.pop()

del_keys_0_lax = []
for key in lax_dict:
    if len(lax_dict[key]) == 1:
        lax_dict[key] = float(lax_dict[key][0])
    else:
        del_keys_0_lax.append(key)


for key in del_keys_0_lax:
    lax_dict.pop(key)

# Definição de variáveis a serem excluídas do Strains de Eixo Curto (SAX)
del_keys_sax = [
    'TimeToPeakStrainRadial',
    'TimeToPeakStrainCircumferential',
    'PeakDiastolicStrainRateRadial',
    'PeakDiastolicStrainRateCircumferential',
    'PeakDisplacementRadial',
    'PeakDisplacementCircumferential',
    'TimeToPeakDisplacementRadial',
    'TimeToPeakDisplacementCircumferential',
    'PeakSystolicVelocityRadial',
    'PeakSystolicVelocityCircumferential',
    'PeakDiastolicVelocityRadial',
    'PeakDiastolicVelocityCircumferential'
]

# Criar dicionário (com variável e valor) para Strain de Eixo Curto (SAX) extraindo dados do report.xml
sax_dict = {}
segment = int()
for i in root.find("AllMeasurementsReport/ShortAxisPolarmapData"):
    if i.tag == 'AHA_seg':
        segment = i.attrib['val']
    elif i.tag in del_keys_sax: # del_keys_sax não serão extraídas do report.xml 
        pass
    else:
        sax_dict['sax_' + i.tag.lower() + '_seg' + str(segment)] = list(i.attrib.values())

for i in sax_dict.values():
    if len(i) == 2:
        i.pop()

del_keys_0_sax = list()
for key in sax_dict:
    if len(sax_dict[key]) == 1:
        sax_dict[key] = float(sax_dict[key][0])
    else:
        del_keys_0_sax.append(key)

for key in del_keys_0_sax:
    sax_dict.pop(key)

# Criando um dataframe no pandas
strain_dict.update(lax_dict)
strain_dict.update(sax_dict)
strain_df = pd.DataFrame(strain_dict, index=[0])

# Organizando a ordem das variáveis no dataframe
strain_df = strain_df[[
    'nome',
    'lax_peakstrainlongitudinal_seg1',
    'lax_peakstrainlongitudinal_seg2',
    'lax_peakstrainlongitudinal_seg3',
    'lax_peakstrainlongitudinal_seg4',
    'lax_peakstrainlongitudinal_seg5',
    'lax_peakstrainlongitudinal_seg6',
    'lax_peakstrainlongitudinal_seg7',
    'lax_peakstrainlongitudinal_seg8',
    'lax_peakstrainlongitudinal_seg9',
    'lax_peakstrainlongitudinal_seg10',
    'lax_peakstrainlongitudinal_seg11',
    'lax_peakstrainlongitudinal_seg12',
    'lax_peakstrainlongitudinal_seg13',
    'lax_peakstrainlongitudinal_seg14',
    'lax_peakstrainlongitudinal_seg15',
    'lax_peakstrainlongitudinal_seg16',
    'lax_peakstrainradial_seg1',
    'lax_peakstrainradial_seg2',
    'lax_peakstrainradial_seg3',
    'lax_peakstrainradial_seg4',
    'lax_peakstrainradial_seg5',
    'lax_peakstrainradial_seg6',
    'lax_peakstrainradial_seg7',
    'lax_peakstrainradial_seg8',
    'lax_peakstrainradial_seg9',
    'lax_peakstrainradial_seg10',
    'lax_peakstrainradial_seg11',
    'lax_peakstrainradial_seg12',
    'lax_peakstrainradial_seg13',
    'lax_peakstrainradial_seg14',
    'lax_peakstrainradial_seg15',
    'lax_peakstrainradial_seg16',
    'lax_peaksystolicstrainratelongitudinal_seg1',
    'lax_peaksystolicstrainratelongitudinal_seg2',
    'lax_peaksystolicstrainratelongitudinal_seg3',
    'lax_peaksystolicstrainratelongitudinal_seg4',
    'lax_peaksystolicstrainratelongitudinal_seg5',
    'lax_peaksystolicstrainratelongitudinal_seg6',
    'lax_peaksystolicstrainratelongitudinal_seg7',
    'lax_peaksystolicstrainratelongitudinal_seg8',
    'lax_peaksystolicstrainratelongitudinal_seg9',
    'lax_peaksystolicstrainratelongitudinal_seg10',
    'lax_peaksystolicstrainratelongitudinal_seg11',
    'lax_peaksystolicstrainratelongitudinal_seg12',
    'lax_peaksystolicstrainratelongitudinal_seg13',
    'lax_peaksystolicstrainratelongitudinal_seg14',
    'lax_peaksystolicstrainratelongitudinal_seg15',
    'lax_peaksystolicstrainratelongitudinal_seg16',
    'lax_peaksystolicstrainrateradial_seg1',
    'lax_peaksystolicstrainrateradial_seg2',
    'lax_peaksystolicstrainrateradial_seg3',
    'lax_peaksystolicstrainrateradial_seg4',
    'lax_peaksystolicstrainrateradial_seg5',
    'lax_peaksystolicstrainrateradial_seg6',
    'lax_peaksystolicstrainrateradial_seg7',
    'lax_peaksystolicstrainrateradial_seg8',
    'lax_peaksystolicstrainrateradial_seg9',
    'lax_peaksystolicstrainrateradial_seg10',
    'lax_peaksystolicstrainrateradial_seg11',
    'lax_peaksystolicstrainrateradial_seg12',
    'lax_peaksystolicstrainrateradial_seg13',
    'lax_peaksystolicstrainrateradial_seg14',
    'lax_peaksystolicstrainrateradial_seg15',
    'lax_peaksystolicstrainrateradial_seg16',
    'sax_peakstraincircumferential_seg1',
    'sax_peakstraincircumferential_seg2',
    'sax_peakstraincircumferential_seg3',
    'sax_peakstraincircumferential_seg4',
    'sax_peakstraincircumferential_seg5',
    'sax_peakstraincircumferential_seg6',
    'sax_peakstraincircumferential_seg7',
    'sax_peakstraincircumferential_seg8',
    'sax_peakstraincircumferential_seg9',
    'sax_peakstraincircumferential_seg11',
    'sax_peakstraincircumferential_seg12',
    'sax_peakstraincircumferential_seg13',
    'sax_peakstraincircumferential_seg14',
    'sax_peakstraincircumferential_seg15',
    'sax_peakstraincircumferential_seg16',
    'sax_peakstrainradial_seg1',
    'sax_peakstrainradial_seg2',
    'sax_peakstrainradial_seg3',
    'sax_peakstrainradial_seg4',
    'sax_peakstrainradial_seg5',
    'sax_peakstrainradial_seg6',
    'sax_peakstrainradial_seg7',
    'sax_peakstrainradial_seg8',
    'sax_peakstrainradial_seg9',
    'sax_peakstrainradial_seg11',
    'sax_peakstrainradial_seg12',
    'sax_peakstrainradial_seg13',
    'sax_peakstrainradial_seg14',
    'sax_peakstrainradial_seg15',
    'sax_peakstrainradial_seg16',
    'sax_peaksystolicstrainratecircumferential_seg1',
    'sax_peaksystolicstrainratecircumferential_seg2',
    'sax_peaksystolicstrainratecircumferential_seg3',
    'sax_peaksystolicstrainratecircumferential_seg4',
    'sax_peaksystolicstrainratecircumferential_seg5',
    'sax_peaksystolicstrainratecircumferential_seg6',
    'sax_peaksystolicstrainratecircumferential_seg7',
    'sax_peaksystolicstrainratecircumferential_seg8',
    'sax_peaksystolicstrainratecircumferential_seg9',
    'sax_peaksystolicstrainratecircumferential_seg10',
    'sax_peaksystolicstrainratecircumferential_seg11',
    'sax_peaksystolicstrainratecircumferential_seg12',
    'sax_peaksystolicstrainratecircumferential_seg13',
    'sax_peaksystolicstrainratecircumferential_seg14',
    'sax_peaksystolicstrainratecircumferential_seg15',
    'sax_peaksystolicstrainratecircumferential_seg16',
    'sax_peaksystolicstrainrateradial_seg1',
    'sax_peaksystolicstrainrateradial_seg2',
    'sax_peaksystolicstrainrateradial_seg3',
    'sax_peaksystolicstrainrateradial_seg4',
    'sax_peaksystolicstrainrateradial_seg5',
    'sax_peaksystolicstrainrateradial_seg6',
    'sax_peaksystolicstrainrateradial_seg7',
    'sax_peaksystolicstrainrateradial_seg8',
    'sax_peaksystolicstrainrateradial_seg9',
    'sax_peaksystolicstrainrateradial_seg10',
    'sax_peaksystolicstrainrateradial_seg11',
    'sax_peaksystolicstrainrateradial_seg12',
    'sax_peaksystolicstrainrateradial_seg13',
    'sax_peaksystolicstrainrateradial_seg14',
    'sax_peaksystolicstrainrateradial_seg15',
    'sax_peaksystolicstrainrateradial_seg16'  
]]

# Criando arquivo feather para análise estatística
path = 'strain_ve.feather'
feather.write_dataframe(strain_df, path)