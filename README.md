# TLSible
TLS + Ansible, is a playbook to automate issuing/renewing of letsencrypt TLS certificates, can secure an infinite number of domains/subdomains.

## Features
* Cron friendly, run daily or hourly doesn't matter :)

## Conventions
* Certificates will be stored in */etc/tls/* directory.
* HTTP Challenges will be stored in a web accessible location by default */var/www/subdmain/* directory.

## Compatibility
* Tested with Ansible 2.6
* Debian 9 (stretch)

## Limitations
* This playbook won't configure your webserver for you.

## Customization
Each host has the following variables available:
* *enable_tls*: (bool) 'yes' to enable tls for this domain, 'no' to skip it.
* *subdomains*: (list) subdomains for your host domain.
* *tls*: (dict) certificate details, like country, state.. etc. (Doesn't seem to have any effect, maybe implemented in the future).
* *account_key*: (str) path where to store letsencrypt account key.
* *account\_email*: (str) email address to get notifications when any certificate needs renewal.
* *agreed*: (bool) say 'yes' to letsencrypt TOS.
* *testing*: (bool) default is 'yes', change to 'no' when you ready for production.

## Usage
* Clone this repository, edit 'hosts' or use it as template.
* To get TLS certificates for your domains: *ansible-playbook -i hosts install\_tls.yaml*
* [WARNING] to delete all certificates run: *ansible-playbook -i hosts uninstall\_tls.yaml*

