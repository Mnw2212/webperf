import webclient, os

def Menu():
    os.system('clear')
    print """
    ============================================================================
    WEB PERFORMANCE TESTER
    ============================================================================
    1 - Test client connection to external websites
    2 - Test internal web server performance
    3 - Display logfile
    4 - Exit
    ============================================================================
    """

    choice = raw_input("\t Enter a choice and press Enter: ")
    return choice

choice = ""
while choice!='4':
    choice = Menu()
    if choice =='1':
        os.system('clear')
        sites=[]
        print """
        ========================================================================
        WEB PERFORMANCE TESTER - External Site Check
        ========================================================================
        """
        siteresponse = raw_input('\tEnter websites to check, seperated by spaces:\n\n\t')
        sites = siteresponse.split()
        webclient.CheckExternalSites(sites)
    elif choice =='2':
        os.system('clear')
        servers=[]
        print """
        ========================================================================
        WEB PERFORMANCE TESTER - Internal Webserver Check
        ========================================================================
        """
        print """
        Enter the ip addresses of the webserver
        running Python Webserver, seperated by spaces:\n\n\t"""

        serverresponse = raw_input('\t')
        servers = serverresponse.split()
        port = raw_input('Enter the port of the webserver: ')
        webclient.CheckInternalWebServers(servers, port)
    elif choice=="3":
        os.system('gedit logfile.txt')
