from filas.celery import app

@app.task(bind=True)
def print_for_loops(self, interations_amount):
    for i in range(interations_amount):
        print(f'Iteração: {i}')
        