import ssl, socket
def get_ssl_info(host):
    try:
        ctx=ssl.create_default_context()
        conn=ctx.wrap_socket(socket.socket(),server_hostname=host)
        conn.settimeout(5)
        conn.connect((host,443))
        cert=conn.getpeercert()
        return {"issued_to":cert.get("subject"),"expire":cert.get("notAfter")}
    except Exception as e:
        return {"error":str(e)}