import scala.io.Source
import scala.collection.mutable.ListBuffer

val file: String = "D:\\aoc\\day3\\input.txt"
val lines: Iterator[String] = Source.fromFile(file).getLines()

val first_line: String = lines.slice(0,1).next()



def determine(index: Int, remaining_strings: List[String], condition: Int): List[String] = {
    var array: Array[Int] = new Array(first_line.trim().length())
    var lines_count = 0
    var indexis0: ListBuffer[String] = new ListBuffer()
    var indexis1: ListBuffer[String] = new ListBuffer()

    for(line <- remaining_strings){
        val characters: Array[Char] = line.toArray
        val ints: Array[Int] = characters.map(char => char.toInt-48)

        if(ints(index) == 0){
            indexis0 += line
        } else {
            indexis1 += line
        }

        for(i <- 0 until ints.length){
            array(i) += ints(i)
        }
        lines_count += 1
    }
    array = array.map(value => (value.toDouble/lines_count.toDouble).round.toInt)

    //tu sie nie patrzec
    if(indexis1.length >= indexis0.length){
        if(condition == 1){
            return indexis1.toList
        }else{
            return indexis0.toList
        }
    }else{
        if(condition == 1){
            return indexis0.toList
        }else{
            return indexis1.toList
        }
    }

}

var remaining_strings_oxygen: List[String] = List(first_line) ::: lines.toList
var remaining_strings_co2: List[String] = remaining_strings_oxygen

var i : Int = 0
while(i!=first_line.trim().length() && remaining_strings_oxygen.length != 1){
    remaining_strings_oxygen = determine(i,remaining_strings_oxygen,1)
    i += 1
}
i = 0
while(i!=first_line.trim().length() && remaining_strings_co2.length != 1){
    remaining_strings_co2 = determine(i,remaining_strings_co2,0)
    i += 1
}
val oxygen: Int = Integer.parseInt(remaining_strings_oxygen(0),2)
val co2: Int = Integer.parseInt(remaining_strings_co2(0),2)

print(oxygen*co2)