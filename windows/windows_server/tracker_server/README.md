# GPS-Tracker server host on windows server

**PS: This instructions are based  on a azure virtual machine**


## Requiemenst 
1. Pleask Obsidien 18.04
2. php version 7.4.33
3. ASP.NET 
4. Mysql (MariaDB)
---
## Important links
[Install plesk][Plesk]

---


## Steps:
### web app
1. First of all we need a windows server hookedup with a public ip 
2. There are bunch of ways we can do that ssh, azure cli and rdp. Here i will be using rdp to connect to the virtual machine which is by far the easiest way to do that
3. Install plesk obsidien in that windows server while installing the plesk we need to add php and asp.net(required version). [Get Plesk][Plesk]
4. After the successfull installation we can access the plesk obsidien web control panel on port `8443`
5. We can use the public ip to access the default page of plesk installation. For That we need to configure the firewall to access the port 80(http) & 443(https). This inbound and out bound need to be added in vm settings on azure site.
6. Then add the domain in plesk using add a website button in the first menu and configure the dns.
7. The default php version may differ from the requirements; if that is the case we need to change the php version 7.4.33(as it is working)
8. After that we need to make changes in the root directory of the config.php(mendatory) file, web.config(mendatory) and custom.config.php(optional)
9. All the files of the project is is now to be set on the plesk site so it goes under the `C:\\interpub\vhosts\yourdomain\htdocs\`(Default)
10. Now we have to configure the database; add database and and the user as required. Then Import the provided the db.sql
11. We are done with the web app installation and we can access it by the domain/index.php

### gps services 
1. For that we need to allow the inbound and outbound in the for the vm in azure and windows defender firewall.
2. Then we need to add the hw.key(hardware key) which must be same as the web app hardware key.
3. Then all we need to execute the gps.srvice.exe and we are good to go. 

### End 




---

[Plesk]: https://get.plesk.com/
