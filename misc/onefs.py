class OneFS:
    def __init__(self, admin_ip, admin_user, admin_password):
        self.admin_ip = admin_ip
        self.admin_user = admin_user
        self.admin_password = admin_password
        self.session = requests.Session()
        self.session.auth = requests.auth.HTTPBasicAuth(self.admin_user, self.admin_password)
    def backend(self):
        return self.session
    def _url(self, path):
        return 'https://%s:8080%s' % (self.admin_ip, path)
    def _request(self, method, path, json=None, headers=None):
        if not self.admin_ip:
            return {}
        response = self.backend().request(
            method,
            self._url(path),
            headers=headers,
            json=json,
            verify=False
        )
        # in case of DELETE with Not FOUND, don't raise exception
        if method != 'DELETE' or response.status_code != 404:
            response.raise_for_status()
        print("Response: ", response)
        return response.json() if response.content else {}
    def get(self, path):
        return self._request('GET', path)
    def put(self, path, headers=None, json=None):
        return self._request('PUT', path, headers=headers, json=json)
    def post(self, path, json):
        return self._request('POST', path, json=json)
    def delete(self, path):
        return self._request('DELETE', path)

