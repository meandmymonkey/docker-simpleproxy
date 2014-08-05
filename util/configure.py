import jinja2
import json
import os

loader = jinja2.FileSystemLoader(searchpath='./')
env = jinja2.Environment(loader=loader)
template = env.get_template('default.j2')

rawConfig = json.loads(os.getenv('PROXY_MAP', '{}'))
hostMap = {}

for prefix, host in rawConfig.items():
    hostMap[host] = {}
    hostMap[host]['ip'] = os.environ[prefix.upper() + '_PORT_80_TCP_ADDR']
    hostMap[host]['port'] = os.environ[prefix.upper() + '_PORT_80_TCP_PORT']

with open('/etc/nginx/sites-enabled/default', 'w') as f:
    f.write(template.render(servers=hostMap.items()))
    f.close()