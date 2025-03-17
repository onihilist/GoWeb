import os

template_file = 'docker-compose.template.yml'
output_file = '../compose.yml'

def read_env_file(file_path):
    env_vars = {}
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    env_vars[key.strip()] = value.strip()
    return env_vars

golang_env = read_env_file('golang.env')
maria_env = read_env_file('maria.env')
nginx_env = read_env_file('nginx.env')
postgresql_env = read_env_file('postgresql.env')

include_golang = golang_env.get('INCLUDE_GOLANG', 'false').lower() == 'true'
include_mariadb = maria_env.get('INCLUDE_MARIA', 'false').lower() == 'true'
include_postgresql = postgresql_env.get('INCLUDE_POSTGRESQL', 'false').lower() == 'true'
include_nginx = nginx_env.get('INCLUDE_NGINX', 'false').lower() == 'true'

with open(template_file, 'r') as file:
    template_content = file.read()

if include_golang:
    template_content = template_content.replace('{{IncludeGolang}}', '- docker.conf/compose-golang.yml')
else:
    template_content = template_content.replace('{{IncludeGolang}}', '# - docker.conf/compose-golang.yml')

if include_mariadb:
    template_content = template_content.replace('{{IncludeMariaDB}}', '- docker.conf/compose-maria.yml')
else:
    template_content = template_content.replace('{{IncludeMariaDB}}', '# - docker.conf/compose-maria.yml')

if include_postgresql:
    template_content = template_content.replace('{{IncludePostgreSQL}}', '- docker.conf/compose-postgresql.yml')
else:
    template_content = template_content.replace('{{IncludePostgreSQL}}', '# - docker.conf/compose-postgresql.yml')

if include_nginx:
    template_content = template_content.replace('{{IncludeNginx}}', '- docker.conf/compose-nginx.yml')
else:
    template_content = template_content.replace('{{IncludeNginx}}', '# - docker.conf/compose-nginx.yml')

with open(output_file, 'w') as file:
    file.write(template_content)

# if os.path.exists(template_file):
#     os.remove(template_file)
#     print(f"Deleted template file: {template_file}")

print(f"Generated {output_file} with the following settings:")
print(f"IncludeGolang: {include_golang}")
print(f"IncludeMariaDB: {include_mariadb}")
print(f"IncludePostgreSQL: {include_postgresql}")
print(f"IncludeNginx: {include_nginx}")