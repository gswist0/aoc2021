import scala.io.Source
import scala.collection.mutable.ListBuffer
import util.control.Breaks._

val file: String = "D:\\aoc\\day4\\input.txt"
val lines: Iterator[String] = Source.fromFile(file).getLines()

val numbers_called: String = lines.slice(0,1).next()
var boards: ListBuffer[Array[Array[Int]]] = new ListBuffer()

var temp_board:Array[Array[Int]] = Array.ofDim[Int](5,5)
var i:Int = 0

for(line <- lines){
    if(line == ""){
        if(i!=0) boards += temp_board
        i = 0
        temp_board = Array.ofDim[Int](5,5)
    }else{
        val line_split: Array[String] = line.trim().split("\\s+")
        for(j <- 0 until line_split.length){
            temp_board(i)(j) = line_split(j).toInt
        }
        i += 1
    }
}
boards+=temp_board

def checkIfWon(boards: ListBuffer[Array[Array[Int]]], numbers: Array[Int]) : (Boolean,Array[Array[Int]]) = {
    var winner_board: Array[Array[Int]] = Array.ofDim[Int](5,5)
    var any_winners: Boolean = false
    for(board <- boards){
        var board_wins: Boolean = false
        var rows: ListBuffer[Array[Int]] = new ListBuffer()
        var columns: ListBuffer[Array[Int]] = new ListBuffer()


        for (i <- 0 until 5){
            rows += board(i)
        }
        for (i <- 0 until 5){
            var column:Array[Int] = Array(0,0,0,0,0)
            for (j <- 0 until 5){
                column(j) = board(j)(i)
            }
            columns += column
        }
        
        for(row <- rows){
            var full_row: Boolean = true
            breakable{
                for(element <- row){
                    if(!numbers.contains(element)){
                        full_row=false
                        break
                    }
                }
            }
            if(full_row){ 
                any_winners = true
                winner_board = board
                return (any_winners,winner_board)
            }
        }
    
    
        for(column <- columns){
            var full_column: Boolean = true
            breakable{
                for(element <- column){
                    if(!numbers.contains(element)){
                        full_column=false
                        break
                    }
                }
            }
            if(full_column){
                any_winners = true
                winner_board = board
                return (any_winners,winner_board)
            }
        }
        
    }
    return (any_winners,winner_board)
}

var all_numbers: Array[Int] = numbers_called.trim().split(",").map(value => value.toInt)
breakable{
    for(i <- 1 until all_numbers.length){
        if((checkIfWon(boards,all_numbers.slice(0,i)))._1) {
            var winner_board: Array[Array[Int]] = checkIfWon(boards,all_numbers.slice(0,i))._2
            var winner_numbers: Array[Int] = all_numbers.slice(0,i)
            var count_unmarked: Int = 0
            for (i <- 0 until 5){
                for (j <- 0 until 5){
                    if(!winner_numbers.contains(winner_board(i)(j))){
                        count_unmarked += winner_board(i)(j)
                    }
                }
            }
            print(all_numbers(i-1)*count_unmarked)
            break
        }
    }
}