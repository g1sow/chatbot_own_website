from flask import Flask, request, jsonify

app = Flask(__name__)

# Our list of services
services = {
    "Web Design": "Beautiful, responsive websites that capture your brand essence and engage your audience.",
    "Web Development": "Custom websites and applications built with modern technologies for optimal performance.",
    "E-commerce Solutions": "Comprehensive online stores with secure payment gateways and intuitive shopping experiences.",
    "CMS Integration": "Easy-to-use content management systems that empower you to update your website effortlessly.",
    "SEO Optimization": "Strategic optimization to improve your website's visibility and ranking in search engines.",
    "Maintenance & Support": "Ongoing website maintenance and technical support to ensure your site runs smoothly.",
    "AI Chatbot": "AI-powered chatbot solutions for 24/7 customer support and engagement.",
    "Business Data Analysis & Dashboard": "Powerful business analytics and dashboards to help you make data-driven decisions.",
    "Logo and Brand Design": "Professional logo and branding design to establish a strong identity."
}

# Endpoint to get a list of services
@app.route('/services', methods=['GET'])
def get_services():
    return jsonify({"services": list(services.keys())})

# Endpoint to get details about a specific service
@app.route('/service-details', methods=['POST'])
def get_service_details():
    data = request.get_json()
    selected_service = data.get('service')

    if not selected_service:
        return jsonify({"error": "Service is required"}), 400

    # Fetch service details
    details = services.get(selected_service)
    
    if details:
        return jsonify({"service": selected_service, "details": details})
    else:
        return jsonify({"error": "Service not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
