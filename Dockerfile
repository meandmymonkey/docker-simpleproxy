FROM meandmymonkey/nginx

MAINTAINER Andreas Hucks "andreas@inputrequired.org"

RUN \
    apt-get -y install python-setuptools && \
    easy_install Jinja2 && \
    rm -rf /var/www

ADD ./util /opt/nginx-config

CMD /bin/bash /opt/nginx-config/run.sh