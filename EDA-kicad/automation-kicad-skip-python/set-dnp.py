import skip

# the list of all schematics
schematics = ['audio.kicad_sch',
              'fingerprint.kicad_sch',
              'screen.kicad_sch',
              'buttons.kicad_sch',
              'flashlight.kicad_sch',
              'USB-C.kicad_sch',
              'camera.kicad_sch',
              'GSM-GPS.kicad_sch',
              'vibration.kicad_sch',
              'cm5-carrier.kicad_sch',
              'power.kicad_sch'
              ]

# the list of schematics to set DNP = True
selected_schematics = ['audio.kicad_sch',
              'fingerprint.kicad_sch',
              'screen.kicad_sch',
              'buttons.kicad_sch',
              'flashlight.kicad_sch',
              # 'USB-C.kicad_sch',
              'camera.kicad_sch',
              'GSM-GPS.kicad_sch',
              'vibration.kicad_sch',
              # 'cm5-carrier.kicad_sch',
              # 'power.kicad_sch'
              ]

# set all DNP = False
for schem in schematics:
    path = f'../{schem}'
    schem = skip.Schematic(path)
    for symbol in schem.symbol:
        symbol.dnp.value = False

    schem.write(path)

# set selected DNP = True
for schem in selected_schematics:
    path = f'../{schem}'
    schem = skip.Schematic(path)
    for symbol in schem.symbol:
        symbol.dnp.value = True

    schem.write(path)



