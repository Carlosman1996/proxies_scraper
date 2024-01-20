from flask import Flask, request, jsonify
from main import get_proxies  # Import the function or module that provides the proxies


app = Flask(__name__)


@app.route('/proxies', methods=['GET'])
def proxies():
    # Extract query parameters
    country_codes_filter = request.args.get('country_codes_filter')
    anonymity_filter = request.args.get('anonymity_filter')
    https_filter = request.args.get('https_filter')

    # Call your module's function to get the list of proxies
    proxy_list = get_proxies(country_codes_filter, anonymity_filter, https_filter)

    # Convert the list to JSON and return it
    return jsonify({'proxies': proxy_list})


if __name__ == '__main__':
    app.run(debug=True)
