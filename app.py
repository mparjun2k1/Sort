from flask import Flask, render_template, request

app = Flask(__name__)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_numbers = request.form.get('numbers')
        if input_numbers:
            numbers = [int(num) for num in input_numbers.split( )]
            bubble_sort(numbers)
            sorted_numbers = ', '.join(map(str, numbers))
            return render_template('C:\\Users\\drpmp\\OneDrive\\Desktop\\bubble_sort_app\\template\\index.html', sorted_numbers=sorted_numbers)
    return render_template('C:\\Users\\drpmp\\OneDrive\\Desktop\\bubble_sort_app\\template\\index.html', sorted_numbers=None)

if __name__ == '__main__':
    app.run(debug=True)
