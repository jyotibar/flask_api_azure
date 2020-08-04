from flask import Flask, jsonify, request, abort

# initialize  Flask application
app= Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]


@app.route('/', methods=['GET'])
def home():
    
    return '''
    <h2> Mills test API</h2>
     <p> Hello, This is test api. I added this line to check CI/CD. In software engineering, CI/CD or CICD generally
    refers to the combined practices of continuous integration and either continuous delivery or continuous deployment. CI/CD bridges the gaps between development and operation activities 
    and teams by enforcing automation in building, testing and deployment of applications. </p>'''
    
    



@app.route('/get-task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)  # "Resource Not Found",
    return jsonify({'task': task[0]})


@app.route('/add-task', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201



if __name__ == '__main__':
    app.run(debug=True)
