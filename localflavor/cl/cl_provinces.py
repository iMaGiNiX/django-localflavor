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


#   A list of Chilean provinces as `choices` in a formfield.
#  "CUT Province" , " Province Name "
PROVINCES_CHOICES = (
    ('151' , 'Arica'),
    ('152' , 'Parinacota'),
    ('011' , 'Iquique'),
    ('014' , 'Tamarugal'),
    ('021' , 'Antofagasta'),
    ('022' , 'El Loa'),
    ('023' , 'Tocopilla'),
    ('031' , 'Copiapó'),
    ('032' , 'Chañaral'),
    ('033' , 'Huasco'),
    ('041' , 'Elqui'),
    ('042' , 'Choapa'),
    ('043' , 'Limarí'),
    ('051' , 'Valparaíso'),
    ('052' , 'Isla de Pascua'),
    ('053' , 'Los Andes'),
    ('054' , 'Petorca'),
    ('055' , 'Quillota'),
    ('056' , 'San Antonio'),
    ('057' , 'San Felipe de Aconcagua'),
    ('058' , 'Marga Marga'),
    ('061' , 'Cachapoal'),
    ('062' , 'Cardenal Caro'),
    ('063' , 'Colchagua'),
    ('071' , 'Talca'),
    ('072' , 'Cauquenes'),
    ('073' , 'Curicó'),
    ('074' , 'Linares'),
    ('081' , 'Concepción'),
    ('082' , 'Arauco'),
    ('083' , 'Biobío'),
    ('084' , 'Ñuble'),
    ('091' , 'Cautín'),
    ('092' , 'Malleco'),
    ('141' , 'Valdivia'),
    ('142' , 'Ranco'),
    ('101' , 'Llanquihue'),
    ('102' , 'Chiloé'),
    ('103' , 'Osorno'),
    ('104' , 'Palena'),
    ('111' , 'Coyhaique'),
    ('112' , 'Aysén'),
    ('113' , 'Capitán Prat'),
    ('114' , 'General Carrera'),
    ('121' , 'Magallanes'),
    ('122' , 'Antártica Chilena'),
    ('123' , 'Tierra del Fuego'),
    ('124' , 'Última Esperanza'),
    ('131' , 'Santiago'),
    ('132' , 'Cordillera'),
    ('133' , 'Chacabuco'),
    ('134' , 'Maipo'),
    ('135' , 'Melipilla'),
    ('136' , 'Talagante'),
)
