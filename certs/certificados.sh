# Función para crear un certificado de autoridad de certificación (CA)
crear_certificado_CA() {
    local ca_name="$1"
    openssl genrsa -out "$ca_name.key" 2048
    openssl req -new -x509 -key "$ca_name.key" -out "$ca_name.crt" -subj "/CN=$ca_name"
    echo "Certificado de Autoridad de Certificación $ca_name creado exitosamente."
}

# Función para crear un certificado de servidor
crear_certificado_server() {
    local server_name="$1"
    local ip_address="$2"  # Se agrega la dirección IP como argumento
    openssl genrsa -out "$server_name.key" 2048
    openssl req -new -key "$server_name.key" -out "$server_name.csr" -subj "/CN=$server_name"
    openssl x509 -req -in "$server_name.csr" -CA ca.crt -CAkey ca.key -CAcreateserial -out "$server_name.crt" -days 365 -extfile <(printf "subjectAltName=IP:$ip_address")
    echo "Certificado de servidor $server_name creado exitosamente."
}


crear_certificado_Dallas() {
    
    local client_name="$1"
    local ip_address="$2"  # Se agrega la dirección IP como argumento
    openssl genrsa -out "$client_name.key" 2048
    openssl req -new -key "$client_name.key" -out "$client_name.csr" -subj "/CN=$client_name"
    openssl x509 -req -in "$client_name.csr" -CA ./ca.crt -CAkey ./ca.key -CAcreateserial -out "$client_name.crt" -days 365 -extfile <(printf "subjectAltName=IP:$ip_address")
    echo "Certificado de cliente $client_name creado exitosamente."
}

crear_certificado_LasVegas() {
    
    local client_name="$1"
    local ip_address="$2"  # Se agrega la dirección IP como argumento
    openssl genrsa -out "$client_name.key" 2048
    openssl req -new -key "$client_name.key" -out "$client_name.csr" -subj "/CN=$client_name"
    openssl x509 -req -in "$client_name.csr" -CA ./ca.crt -CAkey ./ca.key -CAcreateserial -out "$client_name.crt" -days 365 -extfile <(printf "subjectAltName=IP:$ip_address")
    echo "Certificado de cliente $client_name creado exitosamente."
}

crear_certificado_Portland() {
    
    local client_name="$1"
    local ip_address="$2"  # Se agrega la dirección IP como argumento
    openssl genrsa -out "$client_name.key" 2048
    openssl req -new -key "$client_name.key" -out "$client_name.csr" -subj "/CN=$client_name"
    openssl x509 -req -in "$client_name.csr" -CA ./ca.crt -CAkey ./ca.key -CAcreateserial -out "$client_name.crt" -days 365 -extfile <(printf "subjectAltName=IP:$ip_address")
    echo "Certificado de cliente $client_name creado exitosamente."
}

crear_certificado_Denver() {
    
    local client_name="$1"
    local ip_address="$2"  # Se agrega la dirección IP como argumento
    openssl genrsa -out "$client_name.key" 2048
    openssl req -new -key "$client_name.key" -out "$client_name.csr" -subj "/CN=$client_name"
    openssl x509 -req -in "$client_name.csr" -CA ./ca.crt -CAkey ./ca.key -CAcreateserial -out "$client_name.crt" -days 365 -extfile <(printf "subjectAltName=IP:$ip_address")
    echo "Certificado de cliente $client_name creado exitosamente."
}

crear_certificado_Seattle() {
    
    local client_name="$1"
    local ip_address="$2"  # Se agrega la dirección IP como argumento
    openssl genrsa -out "$client_name.key" 2048
    openssl req -new -key "$client_name.key" -out "$client_name.csr" -subj "/CN=$client_name"
    openssl x509 -req -in "$client_name.csr" -CA ./ca.crt -CAkey ./ca.key -CAcreateserial -out "$client_name.crt" -days 365 -extfile <(printf "subjectAltName=IP:$ip_address")
    echo "Certificado de cliente $client_name creado exitosamente."
}

crear_certificado_NewYork() {
    
    local client_name="$1"
    local ip_address="$2"  # Se agrega la dirección IP como argumento
    openssl genrsa -out "$client_name.key" 2048
    openssl req -new -key "$client_name.key" -out "$client_name.csr" -subj "/CN=$client_name"
    openssl x509 -req -in "$client_name.csr" -CA ./ca.crt -CAkey ./ca.key -CAcreateserial -out "$client_name.crt" -days 365 -extfile <(printf "subjectAltName=IP:$ip_address")
    echo "Certificado de cliente $client_name creado exitosamente."
}
# Crear certificado de autoridad de certificación (CA)
crear_certificado_CA "ca"

# Crear certificado de servido
crear_certificado_server "server" "0.0.0.0"

crear_certificado_LasVegas "LasVegas" "192.168.208.2"

crear_certificado_Dallas "Dallas" "192.168.208.3"

crear_certificado_Denver "Denver" "192.168.208.4"

crear_certificado_NewYork "NewYork" "192.168.208.5"

crear_certificado_Portland "Portland" "192.168.208.6"

crear_certificado_Seattle "Seattle" "192.168.208.7"



echo "Todos los certificados han sido creados correctamente."

