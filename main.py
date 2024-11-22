import crmsMdmWs


#resultstart = crmsMdmWs.Crmsmdmws.start('CR_00515')


#resultapcsync = crmsMdmWs.Crmsmdmws.apcsync('CR_00515')

#resultpreuatsucc = crmsMdmWs.Crmsmdmws.preuatsucc('CR_00515')

#resultuatsucc = crmsMdmWs.Crmsmdmws.uatsucc('CR_00515')

resultuatfail = crmsMdmWs.Crmsmdmws.uatfail('CR_00515')


print('Result '+ resultuatfail)
