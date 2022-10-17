import os

sites=[
{'api_key': os.environ['WISC_API'],
        'prjlabel': "UW_Flywheel Body Region identification",
        'sublabel': "WS24-Chest-Effusion-00559",
        'seslabel': '"2021-01-01 20_47_23"',
        'acqlabel': "1 - AP Detector"},

{'api_key': os.environ['FWGA_API'],
        'prjlabel': "ADNI",
        'sublabel': '"135_S_6110"',
        'seslabel': "y2",
        'acqlabel': "3 - Accelerated Sag IR-FSPGR"},

{'api_key': os.environ['GRONDDEV_API'],
        'prjlabel': "project100k",
        'sublabel': '"2022-04-15 08:45:52.056829+00:00"',
        'seslabel': '"2022-04-15 08:45:52.056921+00:00"',
        'acqlabel': '"2022-04-15 08:45:52.056970+00:00"'},

{'api_key': os.environ['UPENN_API'],
        'prjlabel': "test_excel_ingest",
        'sublabel': '"7101051139"',
        'seslabel': '"96459129"',
        'acqlabel': "CT CHEST W IV CONTRAST PULMONARY EMBOLUS"},

{'api_key': os.enciron['CNI_API'],
        'prjlabel': "hypno",
        'sublabel': "R33s101",
        'seslabel': "poststroop",
        'acqlabel': "T1w .9mm sag"},
       ]
