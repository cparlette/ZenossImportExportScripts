for ec in dmd.Events.getSubOrganizers():
    if ec.transform:
        print "= %s ===" % ec.getOrganizerName()
        print ec.transform
        print
    for i in ec.instances():
        if i.transform:
            print "= %s/%s ===" % (ec.getOrganizerName(), i.id)
            print i.transform
            print
