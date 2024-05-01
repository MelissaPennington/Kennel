from urllib.parse import urlparse, parse_qs
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import (
    get_all_animals,
    get_single_animal,
    create_animal,
    delete_animal,
    update_animal,
    get_animals_by_location,
    get_animals_by_status
)
from views import (
    get_all_locations,
    get_single_location,
    create_location,
    delete_location,
    update_location,
)
from views import (
    get_single_employee,
    get_all_employees,
    create_employee,
    delete_employee,
    update_employee,
    get_employees_by_location
)
from views import (
    get_single_customer,
    get_all_customers,
    create_customer,
    delete_customer,
    update_customer,
    get_customer_by_email
)


class HandleRequests(BaseHTTPRequestHandler):
    """Grabs all of the information"""
    def parse_url(self, path):
        """complies all of the parts of th URL"""
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split('/')
        resource = path_params[1]

        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)

        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass
        return (resource, pk)

    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Access to postman"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        """Pulls current information"""
        self._set_headers(200)
        response = {}

        parsed = self.parse_url(self.path)

        if '?' not in self.path:
            (resource, id) = parsed

            if resource == "animals":
                if id is not None:
                    response = get_single_animal(id)
                else:
                    response = get_all_animals()

            if resource == "locations":
                if id is not None:
                    response = get_single_location(id)
                else:
                    response = get_all_locations()

            if resource == "employees":
                if id is not None:
                    response = get_single_employee(id)
                else:
                    response = get_all_employees()

            if resource == "customers":
                if id is not None:
                    response = get_single_customer(id)
                else:
                    response = get_all_customers()

        else:
            (resource, query) = parsed

            if query.get('email') and resource == 'customers':
                response = get_customer_by_email(query['email'][0])
            if query.get('location_id') and resource == 'animals':
                response = get_animals_by_location(query['location_id'][0])
            if query.get('status') and resource == 'animals':
                response = get_animals_by_status(query['status'][0])
            if query.get('location_id') and resource == 'employees':
                response = get_employees_by_location(query['location_id'][0])
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """New item"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, _) = self.parse_url(self.path)

        if resource == "animals":
            new_animal = create_animal(post_body)
            self.wfile.write(json.dumps(new_animal).encode())

        if resource == "locations":
            new_location = create_location(post_body)
            self.wfile.write(json.dumps(new_location).encode())

        if resource == "customers":
            new_customer = create_customer(post_body)
            self.wfile.write(json.dumps(new_customer).encode())

        if resource == "employees":
            new_employee = create_employee(post_body)
            self.wfile.write(json.dumps(new_employee).encode())

    def do_DELETE(self):
        """delete item"""
        self._set_headers(204)
        (resource, id) = self.parse_url(self.path)

        if resource == "animals":
            delete_animal(id)
        elif resource == "customers":
            delete_customer(id)
        elif resource == "locations":
            delete_location(id)
        elif resource == "employees":
            delete_employee(id)

        self.wfile.write("".encode())

    def do_PUT(self):
        """updates information"""
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        if resource == "animals":
            update_animal(id, post_body)
        elif resource == "customers":
            update_customer(id, post_body)
        elif resource == "employees":
            update_employee(id, post_body)
        elif resource == "locations":
            update_location(id, post_body)
        # set default value of success
        success = False

        if resource == "animals":
        # will return either True or False from `update_animal`
            success = update_animal(id, post_body)
            # rest of the elif's

            # handle the value of success
            if success:
                self._set_headers(204)
            else:
                self._set_headers(404)

            self.wfile.write("".encode())

def main():
    """brings to the main page"""
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()
