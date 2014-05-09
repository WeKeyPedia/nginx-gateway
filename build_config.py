import requests
import os


print "cleaning nginx user config"
# L O L
os.system('rm /etc/nginx/sites-enabled/*')

r = requests.get("http://10.1.42.1:4001/v2/keys/subdomains")

for s in r.json()["node"]["nodes"]:
  subdomain = s["key"].replace("/subdomains/", "")
  container = s["value"]

  container_ip = container.split(":")[0]
  container_port = container.split(":")[1]

  print "%s --> %s" % (container, subdomain)

  print "-----"

  template = open("template.conf", "r").read()

  mapping = [
    ["<container_name>", subdomain],
    ["<container_ip>", container_ip],
    ["<container_port>",container_port],
    ["<subdomain>", subdomain]
  ]

  for m in mapping:
    template = template.replace(m[0], m[1])

  print template
  print ""

  o = open('/etc/nginx/sites-enabled/%s.conf' % (subdomain), "w")
  o.write(template)
  o.close()