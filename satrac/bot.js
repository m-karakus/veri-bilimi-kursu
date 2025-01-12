        // Generate piece codes from a given string (for internal piece representation)
        function generatePieceCodesFromString(inputString) {
            const codes = [];
            for (let i = 0; i < inputString.length; i++) {
                codes.push(inputString.charCodeAt(i) - 64); // convert char to code
            }
            console.log("Piece Codes Generated: ", codes);
            return codes;
        }

        // Generate piece codes from FEN notation (for now, using static string)
        function generatePieceCodesFromFEN(fen) {
            // Placeholder logic (expand for real FEN parsing later)

            const pieceRepresentation = {
                p: 1,  // Pawn
                k: 2,  // King
                n: 3,  // Knight
                b: 4,  // Bishop
                r: 5,  // Rook
                q: 6,  // Queen
                P: 9,  // Opponent's Pawn
                K: 10, // Opponent's King
                N: 11, // Opponent's Knight
                B: 12, // Opponent's Bishop
                R: 13, // Opponent's Rook
                Q: 14, // Opponent's Queen
            };

            const codes = [
                53, 51, 52, 54, 50, 52, 51, 53,  // Encoded piece data
                49, 49, 49, 49, 49, 49, 49, 49,  // Pawns
                57, 57, 57, 57, 57, 57, 57, 57,  // Opponent pawns
                61, 59, 60, 62, 58, 60, 59, 61,  // Opponent back rank
                0, 7, 0, 20, 19, 34, 62, -1, 1,  // Movement offsets
                -10, 10, -11, -9, 9, 11, 10, 20, // Knight and king moves
                -11, -9, -10, -20, -21, -19, -12,
                -8, 8, 12, 19, 21, 45, 39, 53, 43,
                39, 39, -32, 15, 10, 14, 13, 12, 11,
                -32, -32, 9, 4, 8, 7, 6, 5
            ];


            // return generatePieceCodesFromString("ustvrtsuqqqqqqqqyyyyyyyy}{|~z|{}@G@TSb~?A6J57IKJT576,+-48HLSUmgukgg OJNMLK  IDHGFE");
            return codes;
        }

        // Piece codes generated from FEN or string
        const pieceCodes = generatePieceCodesFromFEN("your-fen-string-here");

        // Step 2: Initialize Variables for the Game (without affecting piece codes)
        let y = 0, u = 0, previousPosition = 0;
        const boardSize = 10, maxMoves = 15;
        let boardState = [];

        // Populate the boardState based on the piece codes
        //for (let cellPosition = 0; cellPosition <= 120; cellPosition++) {
        //    boardState[cellPosition - 1] =
        //        cellPosition % boardSize
        //            ? (cellPosition / boardSize % boardSize < 2 || cellPosition % boardSize < 2)
        //                ? 7
        //                : cellPosition / boardSize & 4
        //                ? 0
        //                : pieceCodes[u++]
        //            : 7;
        //}

        boardState = [
            7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
            7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
            7, 53, 51, 52, 54, 50, 52, 51, 53, 7,
            7, 49, 49, 49, 49, 49, 49, 49, 49, 7,
            7, 0, 0, 0, 0, 0, 0, 0, 0, 7,
            7, 0, 0, 0, 0, 0, 0, 0, 0, 7,
            7, 0, 0, 0, 0, 0, 0, 0, 0, 7,
            7, 0, 0, 0, 0, 0, 0, 0, 0, 7,
            7, 57, 57, 57, 57, 57, 57, 57, 57, 7,
            7, 61, 59, 60, 62, 58, 60, 59, 61, 7,
            7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
            7, 7, 7, 7, 7, 7, 7, 7, 7, 7
        ]

        // console.log("Board State:", boardState);
        function getPieceCode(piece, pieceType) {
            return 9 - piece & maxMoves ? pieceCodes[61 + pieceType] : 49;
        }
        function getPieceType(currentPiece, playerColor) {
            return currentPiece & maxMoves ^ playerColor;
        }

        function validateMove(targetPiece, pieceType, moveType, playerColor, moveAdjustment) {
            return (!targetPiece && (pieceType || moveType < 3 || moveAdjustment)) || (1 + targetPiece & maxMoves ^ playerColor) > 9 && pieceType | moveType > 2;
        }

        function isForcedMove(targetPiece) {
            return !(2 - targetPiece & 7);
        }

        function evaluateMove(targetPiece, depth, pieceType, validMoves, currentPiece, targetPosition, moveType) {
            return (targetPiece && pieceCodes[targetPiece & 7 | 32] * 2 - depth - pieceType) + (pieceType ? 0 : validMoves - currentPiece & maxMoves ? 110 : (targetPosition && 14) + (moveType < 2) + 1);
        }

        function applyMove(boardIndex, currentPosition, validMoves, targetPiece, moveAdjustment, targetPosition) {
            boardState[currentPosition] = validMoves;
            boardState[moveAdjustment] = boardState[targetPosition];
            boardState[boardIndex] = targetPosition ? boardState[targetPosition] = 0 : 0;
        }

        function revertMove(boardIndex, currentPiece, currentPosition, targetPiece, targetPosition, moveAdjustment, pieceType) {
            boardState[boardIndex] = currentPiece;
            boardState[currentPosition] = targetPiece;
            boardState[targetPosition] = boardState[moveAdjustment];
            targetPosition ? boardState[moveAdjustment] = pieceType ? 0 : 9 ^ playerColor : 0;
        }


        // Step 3: Game Evaluation Logic (Minimax)
        function calculateMove(playerColor, depth, lastPosition, maxDepth, evaluation) {
            playerColor ^= 8;
            //console.log("boardState:", boardState)
            for (
                var currentPosition,
                currentPiece,
                moveScore,
                nextMove,
                targetPosition,
                boardIndex = 20,
                pieceType,
                maxScore = -1e8,
                validMoves,
                moveAdjustment,
                forcedMove = maxDepth && calculateMove(playerColor, 0) > 1e4,
                pieceCode,
                targetPiece,
                moveType,
                evaluationConstant = 78 - depth << 9,
                moveDirection = playerColor ? boardSize : -boardSize;
                ++boardIndex < 99;) {
                if ((currentPiece = boardState[currentPosition = boardIndex]) && (pieceType = getPieceType(currentPiece, playerColor)) < 7) {
                    moveType = pieceType-- & 2 ? 8 : 4;
                    pieceCode = getPieceCode(currentPiece, pieceType);
                    do {
                        targetPiece = boardState[currentPosition += pieceCodes[pieceCode]];
                        moveAdjustment = targetPosition = pieceType | currentPosition + moveDirection - lastPosition ? 0 : lastPosition;

                        isMoveValid = validateMove(targetPiece, pieceType, moveType, playerColor, moveAdjustment);
                        if (isMoveValid) {
                            if (isForcedMove(targetPiece)) return evaluationConstant;
                            for (nextMove = validMoves = pieceType | boardState[currentPosition - moveDirection] - 7 ? currentPiece & maxMoves : 6 ^ playerColor; nextMove; nextMove = !nextMove && !forcedMove && !(moveAdjustment = currentPosition, targetPosition = currentPosition < boardIndex ? moveAdjustment - 3 : moveAdjustment + 2, boardState[targetPosition] < maxMoves | boardState[targetPosition + boardIndex - currentPosition] | boardState[currentPosition += currentPosition - boardIndex])) {
                                moveScore = evaluateMove(targetPiece, depth, pieceType, validMoves, currentPiece, targetPosition, moveType)
                                if (maxDepth > depth || 1 < maxDepth & maxDepth == depth && moveScore > 2 | forcedMove) {
                                    applyMove(boardIndex, currentPosition, validMoves, targetPiece, moveAdjustment, targetPosition)

                                    moveScore -= calculateMove(playerColor, depth + 1, nextMove = pieceType | moveType > 1 ? 0 : currentPosition, maxDepth, moveScore - maxScore);
                                        
                                        
if (!(depth || maxDepth - 1 | currentPosition - boardIndex | moveScore < -1e4)) {
    return renderBoard((y = nextMove)),
        playerColor &&
        setTimeout(() => {
            calculateMove(8, 0, y, 2);
            calculateMove(8, 0, y, 1);
        }, 75);
}

                                        
                                    nextMove = 1 - pieceType | moveType < 7 | targetPosition | !maxDepth | targetPiece | currentPiece < maxMoves || calculateMove(playerColor, 0) > 1e4;
                                    revertMove(boardIndex, currentPiece, currentPosition, targetPiece, targetPosition, moveAdjustment, pieceType)
                                }
                                if (moveScore > maxScore || !depth & moveScore == maxScore && Math.random() < .5) if (maxScore = moveScore, maxDepth > 1) if (depth ? evaluation - moveScore < 0 : (cellPosition = boardIndex, previousPosition = currentPosition, 0)) return maxScore;
                            }
                        }
                    } while (!targetPiece & pieceType > 2 || (currentPosition = boardIndex, pieceType | moveType > 2 | maxMoves < currentPiece & !targetPiece && ++pieceCode * --moveType));
                }
            }
            return_val = -evaluationConstant + 768 < maxScore | forcedMove && maxScore;
            return return_val
        }


// Step 4: Render the Board
function renderBoard() {
    console.log("Chessboard (12x10):");
    for (let i = 0; i < 12; i++) {
        let row = boardState.slice(i * 10, i * 10 + 10);
        console.log(row.map(cell => (cell === 7 ? "##" : cell.toString().padStart(2, " "))).join(" "));
    }
}


// Step 1: Input the Board State
const inputBoardState = [
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    7, 53, 51, 52,  53, 50, 52, 51, 53, 7,
    7, 49, 49,  11, 49,  0,  0, 49,  0, 7,
    7,  0,  0,  1,  0,  0,  0,  0,  0, 7,
    7,  0,  0,  0,  0,  1,  1,  0,  1, 7,
    7,  0,  0,  0,  0,  0,  0,  0,  0, 7,
    7,  0,  0,  0,  0,  0,  9,  0, 11, 7,
    7, 57, 57, 57, 57, 57,  0, 57, 57, 7,
    7, 61,  0, 60, 62, 58, 60,  0, 61, 7,
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
];

// Step 2: Update Global Board State
boardState = inputBoardState.slice(); // Copy input state into global boardState

renderBoard(); // Display updated board
// Step 3: Black's Turn (Calculate the Best Move)
function playBlackTurn() {
    console.log("Black's Turn: Calculating the best move...");
    calculateMove(8, 0, 0, 2, 0); // Black's color (8), depth 0, initial settings

    console.log("Board After Black's Move:");
    renderBoard(); // Display updated board
}

// Play Black's Turn
playBlackTurn();
