import struct
import socket
import sys
import threading
import time

# --- constants ---

HOST = ''   # local address IP (not external address IP)

            # '0.0.0.0' or '' - conection on all NICs (Network Interface Card),
            # '127.0.0.1' or 'localhost' - local conection only (can't connect from remote computer)
            # 'Local_IP' - connection only on one NIC which has this IP

PORT = 11100 # local port (not external port)

# --- functions ---

def handle_client(conn, addr):
    data = conn.recv(1024)
    #request_string = data.decode("utf-8")
    try:
        while True:
            conn.send(data)
            #conn.send(request_string.encode("utf-8"))
            time.sleep(5)
    except BrokenPipeError:
        print('[DEBUG] addr:', addr, 'Connection closed by client?')
    except Exception as ex:
        print('[DEBUG] addr:', addr, 'Exception:', ex, )
    finally:
        conn.close()

# --- main ---

#all_threads = []         

try:
    # --- create socket ---

    print('[DEBUG] create socket')    

    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s = socket.socket() # default value is (socket.AF_INET, socket.SOCK_STREAM) so you don't have to use it

    # --- options ---

    # solution for "[Error 89] Address already in use". Use before bind()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # --- assign socket to local IP (local NIC) ---

    print('[DEBUG] bind:', (HOST, PORT))

    s.bind((HOST, PORT)) # one tuple (HOST, PORT), not two arguments

    # --- set size of queue ---

    print('[DEBUG] listen')

    s.listen(1) # number of clients waiting in queue for "accept".
                # If queue is full then client can't connect.

    while True:
        # --- accept client ---

        # accept client and create new socket `conn` (with different port) for this client only
        # and server will can use `s` to accept other clients (if you will use threading)

        print('[DEBUG] accept ... waiting')

        conn, addr = s.accept() # socket, address

        print('[DEBUG] addr:', addr)

        t = threading.Thread(target=handle_client, args=(conn, addr))
        t.start()

        #all_threads.append(t)

except Exception as ex:
    print(ex)
except KeyboardInterrupt as ex:
    print(ex)
except:
    print(sys.exc_info())
finally:
    # --- close socket ---

    print('[DEBUG] close socket')

    s.close()

    #for t in all_threads:
    #    t.running = False # it would need to build own class Thread
    #    t.join()