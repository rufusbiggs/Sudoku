from flask import Flask, jsonify, request
from sudoku import Board

app = Flask(__name__)

@app.route('/generate', methods=['GET'])
def generate_sudoku_board():
    difficulty = int(request.args.get('difficulty', default = 1))

    board_instance = Board()
    board, solution = board_instance.generate_board_to_solve(difficulty)
    return jsonify({
        'board': board,
        'solution': solution 
    })

if __name__ == '__main__':
    app.run(debug = True)



