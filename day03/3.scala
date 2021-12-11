import scala.io.Source

val file: String = "D:\\aoc\\day3\\input.txt"
val lines: Iterator[String] = Source.fromFile(file).getLines()

val first_line: String = lines.slice(0,1).next()

var array: Array[Int] = new Array(first_line.trim().length())
var lines_count = 0

for(line <- lines){
    val characters: Array[Char] = line.toArray
    val ints: Array[Int] = characters.map(char => char.toInt-48)
    for(i <- 0 until ints.length){
        array(i) += ints(i)
    }
    lines_count += 1
}
array = array.map(value => (value.toDouble/lines_count.toDouble).round.toInt)
var reverse_array: Array[Int] = array.map(value => {
    if(value == 0)
        1
    else 0
})
val gamma: Int = Integer.parseInt(array.mkString(""),2)
val epsilon: Int = Integer.parseInt(reverse_array.mkString(""),2)

print(gamma*epsilon)