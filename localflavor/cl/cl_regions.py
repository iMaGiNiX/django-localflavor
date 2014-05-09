# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Territorial Unique Code
#   Código Único Territorial ( CUT ) 2010
#
#       source information
#       - http://www.ine.cl/canales/chile_estadistico/territorio/division_politico_administrativa/division_politico_administrativa.php

#  Ex:
#   Comune      15101   "Arica"
#   Provinces   151     "Arica"
#   Regions     15      "Región deArica y Parinacota "


#   A list of Chilean regions as `choices` in a formfield.
#  "CUT Region" , " Region Name "
REGION_CHOICES = (
    ('15' , 'Región de Arica y Parinacota'),
    ('01' , 'Región de Tarapacá'),
    ('02' , 'Región de Antofagasta'),
    ('03' , 'Región de Atacama'),
    ('04' , 'Región de Coquimbo'),
    ('05' , 'Región de Valparaíso'),
    ('06' , 'Región del Libertador Gral. Bernardo O’Higgins'),
    ('07' , 'Región del Maule'),
    ('08' , 'Región del Biobío'),
    ('09' , 'Región de La Araucanía'),
    ('14' , 'Región de Los Ríos'),
    ('10' , 'Región de Los Lagos'),
    ('11' , 'Región de Aysén del Gral. Carlos Ibáñez del Campo'),
    ('12' , 'Región de Magallanes y de la Antártica Chilena'),
    ('13' , 'Región Metropolitana de Santiago'),
)
