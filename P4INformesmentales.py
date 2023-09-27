#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!programa para automatizar a traves de una interfas dinamica de ingresos de datos guiada para que se valla creando un reporte en formato MARKDOWN y asi tambien poder realizar con el en XMIND un mapa mental ya estructurado al qeu aparte podriamos personalizar despues con imagenes recolectadas,etc
#! P4INformesmentales.py 2.0v- By P4IM0N

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!TESTEADO EN KALI LINUX, LIBRERIAS E INSTALACION DE LAS MISMAS EN CASO DE NO TENERLAS
# Bibliotecas necesarias para el funcionamientoo:
# -subprocess: Para ejecutar comandos y capturar su la salida.
   #Podes instalarlo con el siguiente comando:
    #? pip install subprocess
# -tabulate: Para crear tablas a partir de datos en listas.
   #Podes instalarlo con el siguiente commando:
    #? pip install tabulate

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Importamos librerias
from tabulate import tabulate
import subprocess

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Códigos de escape ANSI para cambiar el color del texto en la terminal
COLOR_RED = "\033[91m"
COLOR_PURPLE = '\x1b[35m'
COLOR_YELLOW = "\033[93m"
COLOR_RESET = "\033[0m"

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''comandos = {
    "Ping Básico": "ping https://objetivo.com - Realiza un ping simple al sitio web para verificar si está accesible.",
    "Ping con Intervalo de Tiempo Personalizado": "ping -c 5 -i 0.2 https://objetivo.com - Realiza 5 pings con un intervalo de 0.2 segundos entre ellos.",
    "Ping con Tamaño de Paquete Personalizado": "ping -c 5 -s 100 https://objetivo.com - Envía paquetes de 100 bytes al sitio y registra si obtiene respuesta.",
    "Envío Indefinido de Paquetes": "ping -i 1 -s 56 -D https://objetivo.com - Envía paquetes de 56 bytes con intervalo de 1 segundo de forma indefinida.",
    "Registro de Resultados en un Archivo": "ping -c 5 https://objetivo.com > resultados.txt - Realiza 5 pings y guarda los resultados en un archivo llamado 'resultados.txt'.",
    "Supresión de Resolución Inversa": "ping -n -c 5 https://objetivo.com - Realiza pings sin resolver direcciones IP inversas.",
    "Nmap Escaneo Básico de Puertos": "nmap https://objetivo.com - Escanea los puertos abiertos en el objetivo y muestra información básica.",
    "Nmap Escaneo de Servicios y Sistema Operativo": "nmap -sV -O https://objetivo.com - Detecta versiones de servicios y sistema operativo del objetivo.",
    "Nmap Escaneo de Todos los Puertos y Scripts de Detección de Vulnerabilidades": "nmap -p- -sV --script vuln https://objetivo.com - Escanea todos los puertos, detecta versiones y ejecuta scripts de detección de vulnerabilidades.",
    "Nmap Escaneo Rápido de los 1000 Puertos Más Comunes": "nmap -F https://objetivo.com - Realiza un escaneo rápido de los 1000 puertos más comunes.",
    "Nmap Escaneo UDP": "nmap -sU https://objetivo.com - Escanea los puertos UDP abiertos en el objetivo.",
    "Nmap Escaneo de un Rango Personalizado de Puertos": "nmap -p 80,443,8080 https://objetivo.com - Escanea puertos específicos (80, 443 y 8080) en el objetivo.",
    "Nikto Escaneo Básico de Nikto": "nikto -h https://objetivo.com - Realiza un escaneo básico en busca de vulnerabilidades conocidas.",
    "Nikto Escaneo Completo de Nikto": "nikto -h https://objetivo.com -C all - Realiza un escaneo completo, incluyendo todas las pruebas disponibles.",
    "Nikto Escaneo con Plugins de Vulnerabilidades": "nikto -h https://objetivo.com -Plugins +vulnerabilities - Habilita plugins específicos que buscan vulnerabilidades en el sitio web.",
    "Nikto Escaneo SSL": "nikto -h https://objetivo.com -ssl - Realiza un escaneo enfocado en SSL y sus vulnerabilidades.",
    "Nikto Escaneo Proxy": "nikto -h https://objetivo.com -useproxy http://mi.proxy.com:8080 - Utiliza un proxy para realizar el escaneo.",
    "Nikto Escaneo Personalizado de Puertos": "nikto -h https://objetivo.com -port 80,443 - Realiza el escaneo solo en los puertos 80 y 443.",
    "Dirb Escaneo Básico de Directorios": "dirb https://objetivo.com - Realiza un escaneo básico en busca de directorios y archivos ocultos en el objetivo.",
    "Dirb Escaneo con una Lista de Palabras Personalizada": "dirb https://objetivo.com /ruta/a/mi/wordlist.txt - Utiliza una lista de palabras personalizada para buscar directorios y archivos en el objetivo.",
    "Dirb Escaneo con Búsqueda de Extensiones Específicas": "dirb https://objetivo.com -X .php,.html - Busca directorios y archivos con extensiones específicas, como .php y .html.",
    "Dirb Escaneo Recursivo": "dirb https://objetivo.com -r - Realiza un escaneo recursivo para buscar directorios y archivos en profundidad.",
    "Dirb Escaneo de Autenticación Básica": "dirb https://objetivo.com -a usuario:contraseña - Realiza un escaneo en un sitio web que requiere autenticación básica HTTP.",
    "Dirb Escaneo con Límite de Tiempo Personalizado": "dirb https://objetivo.com -t 30 - Establece un límite de tiempo para las solicitudes durante el escaneo.",
    "SQLMap Detección de Bases de Datos": "sqlmap -u 'https://objetivo.com/page?id=1' - Detecta las bases de datos y las vulnerabilidades de inyección SQL en la URL proporcionada.",
    "SQLMap Enumeración de Bases de Datos": "sqlmap -u 'https://objetivo.com/page?id=1' --dbs - Enumera las bases de datos disponibles en el objetivo.",
    "SQLMap Enumeración de Tablas": "sqlmap -u 'https://objetivo.com/page?id=1' --dbs --tables - Enumera las tablas en una base de datos específica.",
    "SQLMap Explotación de una Inyección SQL": "sqlmap -u 'https://objetivo.com/page?id=1' --data 'parametro=valor' --dump - Explota una vulnerabilidad de inyección SQL y recupera datos de la base de datos.",
    "SQLMap Escaneo de Inyección SQL a Ciegas": "sqlmap -u 'https://objetivo.com/page?id=1' --data 'parametro=valor' --level 5 --risk 3 - Realiza un escaneo avanzado de inyección SQL a ciegas en el objetivo.",
    "SQLMap Explotación con Fuerza Bruta de Hashes": "sqlmap -u 'https://objetivo.com/page?id=1' --data 'parametro=valor' --crack - Intenta crackear hashes de contraseñas recuperados de la base de datos.",
    "XSSer Escaneo Básico en Busca de Vulnerabilidades XSS": "xsstrike -u 'https://objetivo.com' - Escanea la URL en busca de vulnerabilidades de Cross-Site Scripting (XSS).",
    "XSSer Escaneo con Enumeración de Enlaces Vulnerables": "xsstrike -u 'https://objetivo.com' -l - Escanea y enumera enlaces vulnerables a ataques XSS en la página.",
    "XSSer Escaneo con Análisis de Todas las Inyecciones de Parámetros": "xsstrike -u 'https://objetivo.com' -p all - Realiza un análisis exhaustivo de todas las inyecciones de parámetros en la URL.",
    "XSSer Escaneo con Filtrado Personalizado de Payloads": "xsstrike -u 'https://objetivo.com' -p all -fp 'mi_payload.txt' - Escanea utilizando payloads personalizados definidos en 'mi_payload.txt'.",
    "XSSer Escaneo con Límite de Tiempo Personalizado": "xsstrike -u 'https://objetivo.com' -t 10 - Establece un límite de tiempo para cada solicitud durante el escaneo.",
    "XSSer Escaneo con Seguimiento de Redirecciones": "xsstrike -u 'https://objetivo.com' -r - Realiza el escaneo siguiendo las redirecciones en la página web objetivo.",
    "Dnsrecon Escaneo Básico de DNS": "dnsrecon -d https://objetivo.com - Realiza un escaneo básico en busca de registros DNS asociados al dominio.",
    "Dnsrecon Escaneo Utilizando Diccionario": "dnsrecon -d https://objetivo.com -t std -D /ruta/a/mi/diccionario.txt - Utiliza un diccionario personalizado para realizar un escaneo exhaustivo de DNS.",
    "Dnsrecon Enumeración de Servidores de Nombres": "dnsrecon -d https://objetivo.com -t brt - Enumera los servidores de nombres relacionados con el dominio.",
    "Dnsrecon Escaneo con un Límite de Tiempo Personalizado": "dnsrecon -d https://objetivo.com -t brt -T 30 - Establece un límite de tiempo para el escaneo.",
    "Dnsrecon Escaneo en Búsqueda de Subdominios": "dnsrecon -d https://objetivo.com -t brt -n - Busca subdominios relacionados con el dominio principal.",
    "Dnsrecon Escaneo Inverso de Direcciones IP": "dnsrecon -r 192.168.1.1 - Realiza un escaneo inverso de una dirección IP específica.",
    "SQLNinja Detección de la Vulnerabilidad": "sqlninja -i https://objetivo.com - Detecta la vulnerabilidad de inyección SQL en el sitio web.",
    "SQLNinja Enumeración de Tablas": "sqlninja -i https://objetivo.com -m t - Enumera las tablas en la base de datos objetivo.",
    "SQLNinja Enumeración de Columnas": "sqlninja -i https://objetivo.com -m c - Enumera las columnas en las tablas de la base de datos.",
    "SQLNinja Explotación de Inyección SQL": "sqlninja -i https://objetivo.com -m s - Explota la vulnerabilidad de inyección SQL y recupera información de la base de datos.",
    "SQLNinja Escaneo de Credenciales": "sqlninja -i https://objetivo.com -m u - Escanea y recupera credenciales de la base de datos.",
    "SQLNinja Explotación con Fuerza Bruta": "sqlninja -i https://objetivo.com -m f - Intenta adivinar contraseñas utilizando un ataque de fuerza bruta.",
    "Gobuster Escaneo Básico de Directorios": "gobuster dir -u https://objetivo.com -w /usr/share/wordlists/dirb/common.txt - Realiza un escaneo básico de directorios en busca de directorios y archivos ocultos en el objetivo.",
    "Gobuster Escaneo con una Lista de Palabras Personalizada": "gobuster dir -u https://objetivo.com -w /ruta/a/mi/wordlist.txt - Utiliza una lista de palabras personalizada para buscar directorios en objetivo",
    "Gobuster Escaneo con Búsqueda de Extensiones Específicas": "gobuster dir -u https://objetivo.com -w /usr/share/wordlists/dirb/big.txt -x .php,.html - Busca directorios y archivos con extensiones específicas, como .php y .html.",
    "Gobuster Escaneo Recursivo": "gobuster dir -u https://objetivo.com -w /usr/share/wordlists/dirb/common.txt -r - Realiza un escaneo recursivo para buscar directorios y archivos en profundidad.",
    "Gobuster Escaneo de Autenticación Básica": "gobuster dir -u https://objetivo.com -w /usr/share/wordlists/dirb/common.txt -U usuario -P contraseña - Escanea un sitio web que requiere autenticación HTTP básica.",
    "Gobuster Escaneo con Límite de Tiempo Personalizado": "gobuster dir -u https://objetivo.com -w /usr/share/wordlists/dirb/common.txt -t 30 - Establece un límite de tiempo para las solicitudes durante el escaneo."
}'''

comandos = {
    "Ping Básico": f"ping {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza un ping simple al sitio web para verificar si está accesible.{COLOR_RESET}",
    "Ping con Intervalo de Tiempo Personalizado": f"ping -c 5 -i 0.2 {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza 5 pings con un intervalo de 0.2 segundos entre ellos.{COLOR_RESET}",
    "Ping con Tamaño de Paquete Personalizado": f"ping -c 5 -s 100 {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Envía paquetes de 100 bytes al sitio y registra si obtiene respuesta.{COLOR_RESET}",
    "Envío Indefinido de Paquetes": f"ping -i 1 -s 56 -D {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Envía paquetes de 56 bytes con intervalo de 1 segundo de forma indefinida.{COLOR_RESET}",
    "Registro de Resultados en un Archivo": f"ping -c 5 {COLOR_RED}https://objetivo.com{COLOR_RESET} > {COLOR_RED}resultados.txt{COLOR_RESET} - {COLOR_YELLOW}Realiza 5 pings y guarda los resultados en un archivo llamado 'resultados.txt'.{COLOR_RESET}",
    "Supresión de Resolución Inversa": f"ping -n -c 5 {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza pings sin resolver direcciones IP inversas.{COLOR_RESET}",
    "Nmap Escaneo Básico de Puertos": f"nmap {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Escanea los puertos abiertos en el objetivo y muestra información básica.{COLOR_RESET}",
    "Nmap Escaneo de Servicios y Sistema Operativo": f"nmap -sV -O {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Detecta versiones de servicios y sistema operativo del objetivo.{COLOR_RESET}",
    "Nmap Escaneo de Todos los Puertos y Scripts de Detección de Vulnerabilidades": f"nmap -p- -sV --script vuln {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Escanea todos los puertos, detecta versiones y ejecuta scripts de detección de vulnerabilidades.{COLOR_RESET}",
    "Nmap Escaneo Rápido de los 1000 Puertos Más Comunes": f"nmap -F {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza un escaneo rápido de los 1000 puertos más comunes.{COLOR_RESET}",
    "Nmap Escaneo UDP": f"nmap -sU {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Escanea los puertos UDP abiertos en el objetivo.{COLOR_RESET}",
    "Nmap Escaneo de un Rango Personalizado de Puertos": f"nmap -p 80,443,8080 {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Escanea puertos específicos (80, 443 y 8080) en el objetivo.{COLOR_RESET}",
    "Nikto Escaneo Básico de Nikto": f"nikto -h {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza un escaneo básico en busca de vulnerabilidades conocidas.{COLOR_RESET}",
    "Nikto Escaneo Completo de Nikto": f"nikto -h {COLOR_RED}https://objetivo.com{COLOR_RESET} -C all - {COLOR_YELLOW}Realiza un escaneo completo, incluyendo todas las pruebas disponibles.{COLOR_RESET}",
    "Nikto Escaneo con Plugins de Vulnerabilidades": f"nikto -h {COLOR_RED}https://objetivo.com{COLOR_RESET} -Plugins +vulnerabilities - {COLOR_YELLOW}Habilita plugins específicos que buscan vulnerabilidades en el sitio web.{COLOR_RESET}",
    "Nikto Escaneo SSL": f"nikto -h {COLOR_RED}https://objetivo.com{COLOR_RESET} -ssl - {COLOR_YELLOW}Realiza un escaneo enfocado en SSL y sus vulnerabilidades.{COLOR_RESET}",
    "Nikto Escaneo Proxy": f"nikto -h {COLOR_RED}https://objetivo.com{COLOR_RESET} -useproxy http://mi.proxy.com:8080 - {COLOR_YELLOW}Utiliza un proxy para realizar el escaneo.{COLOR_RESET}",
    "Nikto Escaneo Personalizado de Puertos": f"nikto -h {COLOR_RED}https://objetivo.com{COLOR_RESET} -port 80,443 - {COLOR_YELLOW}Realiza el escaneo solo en los puertos 80 y 443.{COLOR_RESET}",
    "Dirb Escaneo Básico de Directorios": f"dirb {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza un escaneo básico en busca de directorios y archivos ocultos en el objetivo.{COLOR_RESET}",
    "Dirb Escaneo con una Lista de Palabras Personalizada": f"dirb {COLOR_RED}https://objetivo.com{COLOR_RESET} /ruta/a/mi/wordlist.txt - {COLOR_YELLOW}Utiliza una lista de palabras personalizada para buscar directorios y archivos en el objetivo.{COLOR_RESET}",
    "Dirb Escaneo con Búsqueda de Extensiones Específicas": f"dirb {COLOR_RED}https://objetivo.com{COLOR_RESET} -X .php,.html - {COLOR_YELLOW}Busca directorios y archivos con extensiones específicas, como .php y .html.{COLOR_RESET}",
    "Dirb Escaneo Recursivo": f"dirb {COLOR_RED}https://objetivo.com{COLOR_RESET} -r - {COLOR_YELLOW}Realiza un escaneo recursivo para buscar directorios y archivos en profundidad.{COLOR_RESET}",
    "Dirb Escaneo de Autenticación Básica": f"dirb {COLOR_RED}https://objetivo.com{COLOR_RESET} -a usuario:contraseña - {COLOR_YELLOW}Realiza un escaneo en un sitio web que requiere autenticación básica HTTP.{COLOR_RESET}",
    "Dirb Escaneo con Límite de Tiempo Personalizado": f"dirb {COLOR_RED}https://objetivo.com{COLOR_RESET} -t 30 - {COLOR_YELLOW}Establece un límite de tiempo para las solicitudes durante el escaneo.{COLOR_RESET}",
    "SQLMap Detección de Bases de Datos": f"sqlmap -u {COLOR_RED}'https://objetivo.com/page?id=1'{COLOR_RESET} - {COLOR_YELLOW}Detecta las bases de datos y las vulnerabilidades de inyección SQL en la URL proporcionada.{COLOR_RESET}",
    "SQLMap Enumeración de Bases de Datos": f"sqlmap -u {COLOR_RED}'https://objetivo.com/page?id=1'{COLOR_RESET} --dbs - {COLOR_YELLOW}Enumera las bases de datos disponibles en el objetivo.{COLOR_RESET}",
    "SQLMap Enumeración de Tablas": f"sqlmap -u {COLOR_RED}'https://objetivo.com/page?id=1'{COLOR_RESET} --dbs --tables - {COLOR_YELLOW}Enumera las tablas en una base de datos específica.{COLOR_RESET}",
    "SQLMap Explotación de una Inyección SQL": f"sqlmap -u {COLOR_RED}'https://objetivo.com/page?id=1'{COLOR_RESET} --data 'parametro=valor' --dump - {COLOR_YELLOW}Explota una vulnerabilidad de inyección SQL y recupera datos de la base de datos.{COLOR_RESET}",
    "SQLMap Escaneo de Inyección SQL a Ciegas": f"sqlmap -u {COLOR_RED}'https://objetivo.com/page?id=1'{COLOR_RESET} --data 'parametro=valor' --level 5 --risk 3 - {COLOR_YELLOW}Realiza un escaneo avanzado de inyección SQL a ciegas en el objetivo.{COLOR_RESET}",
    "SQLMap Explotación con Fuerza Bruta de Hashes": f"sqlmap -u {COLOR_RED}'https://objetivo.com/page?id=1'{COLOR_RESET} --data 'parametro=valor' --crack - {COLOR_YELLOW}Intenta crackear hashes de contraseñas recuperados de la base de datos.{COLOR_RESET}",
    "XSSer Escaneo Básico en Busca de Vulnerabilidades XSS": f"xsstrike -u {COLOR_RED}'https://objetivo.com'{COLOR_RESET} - {COLOR_YELLOW}Escanea la URL en busca de vulnerabilidades de Cross-Site Scripting (XSS).{COLOR_RESET}",
    "XSSer Escaneo con Enumeración de Enlaces Vulnerables": f"xsstrike -u {COLOR_RED}'https://objetivo.com'{COLOR_RESET} -l - {COLOR_YELLOW}Escanea y enumera enlaces vulnerables a ataques XSS en la página.{COLOR_RESET}",
    "XSSer Escaneo con Análisis de Todas las Inyecciones de Parámetros": f"xsstrike -u {COLOR_RED}'https://objetivo.com'{COLOR_RESET} -p all - {COLOR_YELLOW}Realiza un análisis exhaustivo de todas las inyecciones de parámetros en la URL.{COLOR_RESET}",
    "XSSer Escaneo con Filtrado Personalizado de Payloads": f"xsstrike -u {COLOR_RED}'https://objetivo.com'{COLOR_RESET} -p all -fp 'mi_payload.txt' - {COLOR_YELLOW}Escanea utilizando payloads personalizados definidos en 'mi_payload.txt'.{COLOR_RESET}",
    "XSSer Escaneo con Límite de Tiempo Personalizado": f"xsstrike -u {COLOR_RED}'https://objetivo.com'{COLOR_RESET} -t 10 - {COLOR_YELLOW}Establece un límite de tiempo para cada solicitud durante el escaneo.{COLOR_RESET}",
    "XSSer Escaneo con Seguimiento de Redirecciones": f"xsstrike -u {COLOR_RED}'https://objetivo.com'{COLOR_RESET} -r - {COLOR_YELLOW}Realiza el escaneo siguiendo las redirecciones en la página web objetivo.{COLOR_RESET}",
    "Dnsrecon Escaneo Básico de DNS": f"dnsrecon -d {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza un escaneo básico en busca de registros DNS asociados al dominio.{COLOR_RESET}",
    "Dnsrecon Escaneo Utilizando Diccionario": f"dnsrecon -d {COLOR_RED}https://objetivo.com{COLOR_RESET} -t std -D /ruta/a/mi/diccionario.txt - {COLOR_YELLOW}Utiliza un diccionario personalizado para realizar un escaneo exhaustivo de DNS.{COLOR_RESET}",
    "Dnsrecon Enumeración de Servidores de Nombres": f"dnsrecon -d {COLOR_RED}https://objetivo.com{COLOR_RESET} -t brt - {COLOR_YELLOW}Enumera los servidores de nombres relacionados con el dominio.{COLOR_RESET}",
    "Dnsrecon Escaneo con un Límite de Tiempo Personalizado": f"dnsrecon -d {COLOR_RED}https://objetivo.com{COLOR_RESET} -t brt -T 30 - {COLOR_YELLOW}Establece un límite de tiempo para el escaneo.{COLOR_RESET}",
    "Dnsrecon Escaneo en Búsqueda de Subdominios": f"dnsrecon -d {COLOR_RED}https://objetivo.com{COLOR_RESET} -t brt -n - {COLOR_YELLOW}Busca subdominios relacionados con el dominio principal.{COLOR_RESET}",
    "Dnsrecon Escaneo Inverso de Direcciones IP": f"dnsrecon -r 192.168.1.1 - {COLOR_YELLOW}Realiza un escaneo inverso de una dirección IP específica.{COLOR_RESET}",
    "SQLNinja Detección de la Vulnerabilidad": f"sqlninja -i {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Detecta la vulnerabilidad de inyección SQL en el sitio web.{COLOR_RESET}",
    "SQLNinja Enumeración de Tablas": f"sqlninja -i {COLOR_RED}https://objetivo.com{COLOR_RESET}-m t - {COLOR_YELLOW}Enumera las tablas en la base de datos objetivo.{COLOR_RESET}",
    "SQLNinja Enumeración de Tablas": f"sqlninja -i {COLOR_RED}https://objetivo.com{COLOR_RESET} -tn - {COLOR_YELLOW}Enumera las tablas en la base de datos vulnerable.{COLOR_RESET}",
    "SQLNinja Enumeración de Columnas": f"sqlninja -i {COLOR_RED}https://objetivo.com{COLOR_RESET} -cn - {COLOR_YELLOW}Enumera las columnas en las tablas de la base de datos.{COLOR_RESET}",
    "SQLNinja Explotación de Inyección SQL": f"sqlninja -i {COLOR_RED}https://objetivo.com{COLOR_RESET} -m {COLOR_RED}POST{COLOR_RESET} - {COLOR_YELLOW}Explota la vulnerabilidad de inyección SQL y recupera datos de la base de datos.{COLOR_RESET}",
    "SQLNinja Escalada de Privilegios": f"sqlninja -i {COLOR_RED}https://objetivo.com{COLOR_RESET} -x {COLOR_RED}'EXEC sp_addsrvrolemember ''sysadmin'', ''usuario'';'{COLOR_RESET} - {COLOR_YELLOW}Realiza una escalada de privilegios para obtener control total del servidor SQL.{COLOR_RESET}",
    "Hydra Ataque de Fuerza Bruta SSH": f"hydra -l usuario -P /ruta/a/mi/lista_de_contraseñas.txt {COLOR_RED}ssh://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza un ataque de fuerza bruta SSH contra un servidor remoto.{COLOR_RESET}",
    "Hydra Ataque de Fuerza Bruta FTP": f"hydra -l usuario -P /ruta/a/mi/lista_de_contraseñas.txt {COLOR_RED}ftp://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza un ataque de fuerza bruta FTP contra un servidor remoto.{COLOR_RESET}",
    "Hydra Ataque de Fuerza Bruta Telnet": f"hydra -l usuario -P /ruta/a/mi/lista_de_contraseñas.txt {COLOR_RED}telnet://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza un ataque de fuerza bruta Telnet contra un servidor remoto.{COLOR_RESET}",
    "Hydra Ataque de Fuerza Bruta HTTP POST": f"hydra -l usuario -P /ruta/a/mi/lista_de_contraseñas.txt {COLOR_RED}http-post://objetivo.com/login{COLOR_RESET} - {COLOR_YELLOW}Realiza un ataque de fuerza bruta HTTP POST contra un formulario de inicio de sesión.{COLOR_RESET}",
    "Gobuster Escaneo Básico de Directorios": f"gobuster dir -u {COLOR_RED}https://objetivo.com{COLOR_RESET} -w /usr/share/wordlists/dirb/common.txt - {COLOR_YELLOW}Realiza un escaneo básico de directorios en busca de directorios y archivos ocultos en el objetivo.{COLOR_RESET}",
    "Gobuster Escaneo con una Lista de Palabras Personalizada": f"gobuster dir -u {COLOR_RED}https://objetivo.com{COLOR_RESET} -w /ruta/a/mi/wordlist.txt - {COLOR_YELLOW}Utiliza una lista de palabras personalizada para buscar directorios en el objetivo.{COLOR_RESET}",
    "Gobuster Escaneo con Búsqueda de Extensiones Específicas": f"gobuster dir -u {COLOR_RED}https://objetivo.com{COLOR_RESET} -w /usr/share/wordlists/dirb/big.txt -x .php,.html - {COLOR_YELLOW}Busca directorios y archivos con extensiones específicas, como .php y .html.{COLOR_RESET}",
    "Gobuster Escaneo Recursivo": f"gobuster dir -u {COLOR_RED}https://objetivo.com{COLOR_RESET} -w /usr/share/wordlists/dirb/common.txt -r - {COLOR_YELLOW}Realiza un escaneo recursivo para buscar directorios y archivos en profundidad.{COLOR_RESET}",
    "Gobuster Escaneo de Autenticación Básica": f"gobuster dir -u {COLOR_RED}https://objetivo.com{COLOR_RESET} -w /usr/share/wordlists/dirb/common.txt -U usuario -P contraseña - {COLOR_YELLOW}Escanea un sitio web que requiere autenticación HTTP básica.{COLOR_RESET}",
    "Gobuster Escaneo con Límite de Tiempo Personalizado": f"gobuster dir -u {COLOR_RED}https://objetivo.com{COLOR_RESET} -w /usr/share/wordlists/dirb/common.txt -t 30 - {COLOR_YELLOW}Establece un límite de tiempo para las solicitudes durante el escaneo.{COLOR_RESET}"
}


tabla_de_comandos = [[comando, COLOR_PURPLE+descripcion+COLOR_RESET] for comando, descripcion in comandos.items()]    #conprension de lista para conseguir la tabla con los colores
tabla_de_comandos_terminada = (tabulate(tabla_de_comandos, headers=['DESCRIPCION','COMANDO','EXPLICACION'], tablefmt='grid'))
#print(tabla_de_comandos_terminada)

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
banner = f'''

__________  _____ .___ _______   _____                                                         __         .__                 
\______   \/  |  ||   |\      \_/ ____\___________  _____   ____   ______ _____   ____   _____/  |______  |  |   ____   ______
 |     ___/   |  ||   |/   |   \   __\/  _ \_  __ \/     \_/ __ \ /  ___//     \_/ __ \ /    \   __\__  \ |  | _/ __ \ /  ___/
 |    |  /    ^   /   /    |    \  | (  <_> )  | \/  Y Y  \  ___/ \___ \|  Y Y  \  ___/|   |  \  |  / __ \|  |_\  ___/ \___ \ 
 |____|  \____   ||___\____|__  /__|  \____/|__|  |__|_|  /\___  >____  >__|_|  /\___  >___|  /__| (____  /____/\___  >____  >
              |__|            \/                        \/     \/     \/      \/     \/     \/          \/          \/     \/ 
{COLOR_PURPLE}By P4IM0N{COLOR_RESET}'''
print(banner)

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    try:
        # Crear o abrir el archivo en modo de escritura
        with open('P4InformeMentalPentesting.md', 'a') as archivo:
            # Recopilar información sobre la máquina objetivo
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO INGRESA LA EMPRESA O MAQUINA OBJETIVO: "+ COLOR_RESET)
            maquina_o_empresa_objetivo = ingresa_multipleslineas()
            archivo.write(f"# {maquina_o_empresa_objetivo}\n")  # Escribir el título de la máquina objetivo
            archivo.flush()
            
            # Agregar un cartel de "Descripción" antes del bucle de reconocimiento
            archivo.write("## DESCRIPCION\n")
            archivo.flush()
            
            sub_banner_menu = f'''
███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██{COLOR_PURPLE}█{COLOR_RESET} ██▌░░░▐██{COLOR_PURPLE}█{COLOR_RESET} ██│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
████████████████{COLOR_PURPLE}By P4IM0N!!!{COLOR_RESET}
            '''
            menu_de_opciones = [[" 1. MANUAL"], [" 2. OSINT"], [" 3. AUTOMATIZADO"], [" 4. INGENIERIA SOCIAL"], [" 5. MIXTO"],[" 6. VISTA PREVIA"],[" 7. AYUDA"],[" 8. FINALIZAR PENTESTING"]]
            
            while True:
                # Recopilar descripciones o información sobre la máquina objetivo
                print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_RED+"INGRESE DESCRIPCIONES O INFORMACION EXTRA DE LA EMPRESA O MAQUINA A REALIZAR EL PENTESTING: "+COLOR_RESET)
                description = ingresa_multipleslineas()
                print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
                # Agregar la descripción al nivel de la sección de "Descripción"
                archivo.write(f"{description}\n")  # Escribir la descripción
                archivo.flush()
                
                # Agregar un cartel de "Reconocimiento" después de la descripción
                archivo.write("#### RECONOCIMIENTO\n")
                archivo.flush()
                
                while True:
                    
                    tabla_de_opciones = tabulate(menu_de_opciones, ['Nº OPCION'], tablefmt='grid')
                    print(sub_banner_menu)
                    print(tabla_de_opciones)
                    
                    print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
                    elige_opcion = input(COLOR_RED+"ELIJA EL TIPO DE RECONOCIMIENTO QUE REALIZARA: "+COLOR_RESET)

                    if elige_opcion == '1':
                        archivo.write("##### MANUAL\n")
                        investigacion_manual(archivo)  # Llamar al método para procesar el análisis manual
                        archivo.flush()
                    elif elige_opcion == '2':
                        archivo.write("##### OSINT\n")
                        investigacion_osint(archivo)  # Llamar al método para procesar el análisis OSINT
                        archivo.flush()
                    elif elige_opcion == '3':
                        archivo.write("##### AUTOMATIZADO\n")
                        investigacion_automatizada(archivo)  # Llamar al método para procesar el análisis automatizado
                        archivo.flush()
                    elif elige_opcion == '4':
                        archivo.write("##### INGENIERIA SOCIAL\n")
                        investigacion_ing_social(archivo)
                        archivo.flush()
                    elif elige_opcion == '5':
                        archivo.write("##### MIXTO\n")
                        investigacion_mixto(archivo)
                        archivo.flush()
                    elif elige_opcion == '6':
                        investigacion_vista_previa()
                    elif elige_opcion == '7':
                        leer_ayuda()
                    elif elige_opcion == '8':
                        print("Pentesting finalizado.")
                        return
                    else:
                        print("Opción no válida 8( ")

                

    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error Manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        
#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#permite ingresar multiples lineas, signos, hacer saltos de lineas, maneja limites de escrituras OK
def ingresa_multipleslineas(max_chars_per_line=100):
    try:
        lista_lineas_ingresadas = []
        print(COLOR_PURPLE+'---------------------------------------------'+COLOR_RESET)
        print(COLOR_PURPLE+'Manito preciona (f) y ENTER para continuar /'+COLOR_RESET)
        print(COLOR_PURPLE+'-------------------------------------------'+COLOR_RESET)
        while True:
            linea = input()
            linea = linea.strip()  # Eliminar espacios en blanco y saltos de línea al principio y al final
            # Eliminar almohadillas, guiones, signos más y espacios al principio de cada línea
            linea = linea.lstrip('#-+ ')
            
            if linea.upper() == 'F' or linea.upper() == 'STOP':
                break
            
            
            # Dividir la línea en segmentos más pequeños si supera el límite de caracteres por línea
            while len(linea) > max_chars_per_line:
                segmento = linea[:max_chars_per_line]
                lista_lineas_ingresadas.append(segmento)
                linea = linea[max_chars_per_line:]
            
            lista_lineas_ingresadas.append(linea)
            
        
        return '\n'.join(lista_lineas_ingresadas)
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error al ingresar texto en bruto Manito, proba sacar algun simbolo que este causando el conflicto: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        return ""


#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Permite ingresar comandos en tiempo real y ser mostrados y guardados en el .md
def ejecutar_comandos():
    try:
        print(tabla_de_comandos_terminada)
        archivo_nombre = 'P4InformeMentalPentesting.md'
        with open(archivo_nombre, "a") as archivo_mapa:
            archivo_mapa.write("- COMANDO:\n")
            archivo_mapa.write('''  - ┌──(root㉿kalipaimon)-[/]
  - └─# ''')
            
            while True:
                print(COLOR_PURPLE+'----------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_PURPLE+"MANITO, INGRESA EL COMANDO A EJECUTAR (o escribe 'fin' para salir): /"+COLOR_RESET)
                print(COLOR_PURPLE+'---------------------------------------------------------------------'+COLOR_RESET)
                comando = input(f'''- {COLOR_YELLOW}┌──{COLOR_RESET}{COLOR_PURPLE}({COLOR_RESET}{COLOR_RED}root{COLOR_RESET}{COLOR_PURPLE}㉿{COLOR_RESET}{COLOR_RED}kalipaimon{COLOR_RESET}{COLOR_PURPLE}){COLOR_RESET}{COLOR_YELLOW}-[{COLOR_RESET}{COLOR_RED}/{COLOR_RESET}{COLOR_YELLOW}]
- └─{COLOR_RESET}#  ''')
                if comando.lower() == 'fin':
                    break

                archivo_mapa.write(comando + '\n')

                proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                for linea in proceso.stdout:
                    print(linea, end='')  # Imprime en tiempo real en la terminal
                    archivo_mapa.write('  - ' + linea)  # Escribe lo de la terminal en el archivo

        print(COLOR_YELLOW+"\n\nManito el resultado quedo guardado en"+COLOR_RESET, archivo_nombre)

    except subprocess.CalledProcessError as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print("Error al ejecutar el comando manito:", error)
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
    except KeyboardInterrupt:
        print(COLOR_PURPLE+'---------------------------------------------'+COLOR_RESET)
        print("\n\nComando cancelado.")        

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Metodo para procesar el analisis MANUAL      
def investigacion_manual(archivo):
    try:
        while True:
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO DECIME EL TIPO DE ANALISIS [[MANUAL]] QUE VAS A HACER: "+COLOR_RESET)
            tipo_de_analisis = ingresa_multipleslineas()
            archivo.write(f"###### {tipo_de_analisis}\n")  # Escribir el título del tipo de análisis
            archivo.flush()
            
            # Agregar para ejecutar comandos y guardar con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
             
            print(COLOR_RED+"MANITO, ¿QUERES EJECUTAR UN COMANDO? (s/n): "+COLOR_RESET)
            ejecutar_comando = input()
            if ejecutar_comando.lower() == 's':
                print(COLOR_PURPLE+'-----------------------------------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_RED+"MANITO, PARA INGRESA EL COMANDO A EJECUTAR PRESIONA ((ENTER)),(o escribe 'fin' para salir): /"+COLOR_RESET)
                print(COLOR_PURPLE+'----------------------------------------------------------------------------------------------'+COLOR_RESET)
                comando = input()
                if comando.lower() == 'fin':
                    break  # Salir del loop si se ingresa "fin"
                ejecutar_comandos()
            
             
            # Agregar resultados como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO INGRESA RESULTADOS COMPLETOS: "+COLOR_RESET)    
            resultados = ingresa_multipleslineas()
            archivo.write("- RESULTADOS:\n")
            for cada_linea_resultados in resultados.splitlines():
                archivo.write(f"  - {cada_linea_resultados}\n")  # Escribir resultados como listas
                archivo.flush()

            # Agregar conclusiones como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO INGRESA LO IMPORTANTE QUE SACASTE DE LOS RESULTADOS: "+COLOR_RESET)
            conclusiones = ingresa_multipleslineas()
            archivo.write("- RESULTADOS IMPORTANTES:\n")
            for cada_linea_conclusiones in conclusiones.splitlines():
                archivo.write(f"  - {cada_linea_conclusiones}\n")  # Escribir conclusiones como listas
                archivo.flush()
        
                    
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            otro_analisis = input(COLOR_RED+"¿MANITO QUERES HACER OTRO ANÁLISIS MANUAL? (s/n): "+COLOR_RESET)
            if otro_analisis.lower() != 's':
                break
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error al procesar el análisis MANUAL Manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
          
#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------        
# Método para procesar el análisis OSINT
def investigacion_osint(archivo):
    try:
        while True:
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO DECIME EL TIPO DE ANALISIS OSINT QUE VAS A HACER: "+COLOR_RESET)
            tipo_de_analisis = ingresa_multipleslineas()
            archivo.write(f"###### {tipo_de_analisis}\n")  # Escribir el título del tipo de análisis
            archivo.flush()
            
            # Agregar para ejecutar comandos y guardar con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
             
            print(COLOR_RED+"MANITO, ¿QUERES EJECUTAR UN COMANDO? (s/n): "+COLOR_RESET)
            ejecutar_comando = input()
            if ejecutar_comando.lower() == 's':
                print(COLOR_PURPLE+'-----------------------------------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_RED+"MANITO, PARA INGRESA EL COMANDO A EJECUTAR PRESIONA ((ENTER)),(o escribe 'fin' para salir): /"+COLOR_RESET)
                print(COLOR_PURPLE+'----------------------------------------------------------------------------------------------'+COLOR_RESET)
                comando = input()
                if comando.lower() == 'fin':
                    break  # Salir del loop si se ingresa "fin"
                ejecutar_comandos()
            
            # Agregar resultados como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"INGRESA LOS RESULTADOS COMPLETOS MANITO: "+COLOR_RESET)
            resultados = ingresa_multipleslineas()
            archivo.write("- RESULTADOS:\n")
            for cada_linea_resultado in resultados.splitlines():
                archivo.write(f"  - {cada_linea_resultado}\n")  # Escribir resultados como listas
                archivo.flush()
            
            # Agregar conclusiones como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"DAME TUS CONCLUSIONES MANITO: "+COLOR_RESET)
            conclusiones = ingresa_multipleslineas()
            archivo.write("- CONCLUSIONES:\n")
            for cada_linea_conclusiones in conclusiones.splitlines():
                archivo.write(f"  - {cada_linea_conclusiones}\n")  # Escribir conclusiones como listas
                archivo.flush()
            
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            otro_analisis = input(COLOR_RED+"¿MANITO QUERES HACER OTRO ANALISIS OSINT? (s/n): "+COLOR_RESET)
            if otro_analisis.lower() != 's':
                break
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error al procesar el análisis OSINT Manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------        
# Método para procesar el análisis automatizado
def investigacion_automatizada(archivo):
    try:
        while True:
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO DECIME LA HERRAMIENTA QUE VAS A USAR: "+COLOR_RESET)
            herramienta = ingresa_multipleslineas()
            archivo.write(f"###### HERRAMIENTA: {herramienta}\n")  # Escribir el título de la herramienta
            archivo.flush()
            
            # Agregar para ejecutar comandos y guardar con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
             
            print(COLOR_RED+"MANITO, ¿QUERES EJECUTAR UN COMANDO? (s/n): "+COLOR_RESET)
            ejecutar_comando = input()
            if ejecutar_comando.lower() == 's':
                print(COLOR_PURPLE+'-----------------------------------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_RED+"MANITO, PARA INGRESA EL COMANDO A EJECUTAR PRESIONA ((ENTER)),(o escribe 'fin' para salir): /"+COLOR_RESET)
                print(COLOR_PURPLE+'----------------------------------------------------------------------------------------------'+COLOR_RESET)
                comando = input()
                if comando.lower() == 'fin':
                    break  # Salir del loop si se ingresa "fin"
                ejecutar_comandos()
            
            # Agregar resultados como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"INGRESA LOS RESULTADOS COMPLETOS MANITO: "+COLOR_RESET)
            resultado = ingresa_multipleslineas()
            archivo.write("- RESULTADOS:\n")
            for cada_linea_de_resultado in resultado.splitlines():
                archivo.write(f"  - {cada_linea_de_resultado}\n")  # Escribir resultados como listas
                archivo.flush()
            
            # Agregar resultados importantes como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO INGRESA LO IMPORTANTE QUE SACASTE DE LOS RESULTADOS: "+COLOR_RESET)
            resultados_importantes = ingresa_multipleslineas()
            archivo.write("- RESULTADOS IMPORTANTES:\n")
            for cada_linea_resultado_importante in resultados_importantes.splitlines():
                archivo.write(f"  - {cada_linea_resultado_importante}\n")  # Escribir resultados importantes como listas
                archivo.flush()
            
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            otra_herramienta = input(COLOR_RED+"¿QUERES USAR OTRA HERRAMIENTA MANITO? (s/n): "+COLOR_RESET)
            if otra_herramienta.lower() != 's':
                break
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error al procesar el análisis AUTOMATIZADO Manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Método para procesar el análisis Ingenieria social
def investigacion_ing_social(archivo):
    try:
        while True:
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO DECIME EL TIPO DE ANALISIS DE [[INGENIERIA SOCIAL]] QUE VAS A HACER: "+COLOR_RESET)
            tipo_de_analisis = ingresa_multipleslineas()
            archivo.write(f"###### {tipo_de_analisis}\n")  # Escribir el título del tipo de análisis
            archivo.flush()
            
            # Agregar para ejecutar comandos y guardar con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
             
            print(COLOR_RED+"MANITO, ¿QUERES EJECUTAR UN COMANDO? (s/n): "+COLOR_RESET)
            ejecutar_comando = input()
            if ejecutar_comando.lower() == 's':
                print(COLOR_PURPLE+'-----------------------------------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_RED+"MANITO, PARA INGRESA EL COMANDO A EJECUTAR PRESIONA ((ENTER)),(o escribe 'fin' para salir): /"+COLOR_RESET)
                print(COLOR_PURPLE+'----------------------------------------------------------------------------------------------'+COLOR_RESET)
                comando = input()
                if comando.lower() == 'fin':
                    break  # Salir del loop si se ingresa "fin"
                ejecutar_comandos()
            
            # Agregar resultados como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"INGRESA LOS RESULTADOS COMPLETOS MANITO: "+COLOR_RESET)
            resultados = ingresa_multipleslineas()
            archivo.write("- RESULTADOS:\n")
            for cada_linea_resultados in resultados.splitlines():
                archivo.write(f"  - {cada_linea_resultados}\n")  # Escribir resultados como listas
                archivo.flush()
            
            # Agregar conclusiones como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO INGRESA LO IMPORTANTE QUE SACASTE DE LOS RESULTADOS: "+COLOR_RESET)
            conclusiones = ingresa_multipleslineas()
            archivo.write("- RESULTADOS IMPORTANTES:\n")
            for cada_linea_conclusiones in conclusiones.splitlines():
                archivo.write(f"  - {cada_linea_conclusiones}\n")  # Escribir conclusiones como listas
                archivo.flush()
            
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            otro_analisis = input(COLOR_RED+"¿MANITO QUERES HACER OTRO ANLISIS DE INGENIERIA SOCIAL? (s/n): "+COLOR_RESET)
            if otro_analisis.lower() != 's':
                break
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error al procesar el análisis de INGENIERIA SOCIAL Manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Método para procesar el análisis mixto
def investigacion_mixto(archivo):
    try:
        while True:
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO DECIME EL TIPO DE ANALISIS [[MIXTO]] QUE VAS A HACER: "+COLOR_RESET)
            tipo_de_analisis = ingresa_multipleslineas()
            archivo.write(f"###### {tipo_de_analisis}\n")  # Escribir el título del tipo de análisis
            archivo.flush()
            
            # Agregar para ejecutar comandos y guardar con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
             
            print(COLOR_RED+"MANITO, ¿QUERES EJECUTAR UN COMANDO? (s/n): "+COLOR_RESET)
            ejecutar_comando = input()
            if ejecutar_comando.lower() == 's':
                print(COLOR_PURPLE+'-----------------------------------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_RED+"MANITO, PARA INGRESA EL COMANDO A EJECUTAR PRESIONA ((ENTER)),(o escribe 'fin' para salir): /"+COLOR_RESET)
                print(COLOR_PURPLE+'----------------------------------------------------------------------------------------------'+COLOR_RESET)
                comando = input()
                if comando.lower() == 'fin':
                    break  # Salir del loop si se ingresa "fin"
                ejecutar_comandos()
            
            # Agregar resultados como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"INGRESA LOS RESULTADOS COMPLETOS MANITO: "+COLOR_RESET)
            resultados = ingresa_multipleslineas()
            archivo.write("- RESULTADOS:\n")
            for cada_linea_resultados in resultados.splitlines():
                archivo.write(f"  - {cada_linea_resultados}\n")  # Escribir resultados como listas
                archivo.flush()
                
            # Agregar conclusiones como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO INGRESA LO IMPORTANTE QUE SACASTE DE LOS RESULTADOS: "+COLOR_RESET)
            conclusiones = ingresa_multipleslineas()
            archivo.write("- RESULTADOS IMPORTANTES:\n")
            for cada_linea_conclusiones in conclusiones.splitlines():
                archivo.write(f"  - {cada_linea_conclusiones}\n")  # Escribir conclusiones como listas
                archivo.flush()
            
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            otro_analisis = input(COLOR_RED+"¿MANITO QUERES HACER OTRO ANALISIS MIXTO? (s/n): "+COLOR_RESET)
            if otro_analisis.lower() != 's':
                break
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error al procesar el análisis MIXTO Manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#abrir XMIN para vista previa
def investigacion_vista_previa():
    archivo = "P4InformeMentalPentesting.md"
    # Comando para abrir el archivo .md con Xmind
    comando = ["xmind", "open", f'/home/paimon/cursopythonhacking/herramientaparainformesYmapamental/{archivo}.md']

    # Ejecuta el comando
    try:
        subprocess.run(comando, check=True)
    except subprocess.CalledProcessError as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Error al abrir el archivo con Xmind manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ver menu de AYUDA
def leer_ayuda():
    try:
        # Abrir el archivo en modo de lectura ('r')
        with open('ayuda.txt', 'r') as archivo:
            # Realiza las operaciones de lectura aquí
            contenido = archivo.read()
            return print(COLOR_YELLOW+contenido+COLOR_RESET)  # Esto imprimirá el contenido 
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f'Se produjo un error manito: {error}')
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------        
if __name__ == "__main__":
    main()


#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
