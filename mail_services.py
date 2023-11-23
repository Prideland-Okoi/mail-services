import os
from flask import Flask, request, jsonify, make_response
from flask_mail import Mail, Message
from flask_restful import Api, Resource
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

# Configure email settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'prideland.okoi@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = 'prideland.okoi@gmail.com'

mail = Mail(app)

class EmailResource(Resource):
    def post(self):
        """
        Send an email
        ---
        tags:
          - Email
        parameters:
          - name: subject
            in: formData
            type: string
            required: true
            description: Email subject
          - name: recipient
            in: formData
            type: string
            required: true
            description: Recipient email address
          - name: body
            in: formData
            type: string
            required: true
            description: Email body
        responses:
          200:
            description: Email sent successfully
          400:
            description: Missing required fields
          500:
            description: Internal Server Error
        """
        try:
            subject = request.form.get('subject')
            recipient = request.form.get('recipient')
            body = request.form.get('body')

            if not (subject and recipient and body):
                response = {'error': 'Missing required fields'}
                return make_response(jsonify(response), 400)

            message = Message(subject=subject, recipients=[recipient], body=body)
            mail.send(message)
            response = {'message': 'Email sent successfully'}
            return make_response(jsonify(response), 200)

        except Exception as e:
            response = {'error': str(e)}
            return make_response(jsonify(response), 500)

api.add_resource(EmailResource, '/send_email')

if __name__ == '__main__':
    app.run(debug=True)
