import scala.io.Source

val file: String = "D:\\aoc\\day2\\input.txt"
val lines: Iterator[String] = Source.fromFile(file).getLines()
var horizontal: Int = 0
var depth: Int = 0
var aim: Int = 0


for(line <- lines) {
  val command: String = line.split("\\s+")(0)
  val amount: Int = line.split("\\s+")(1).toInt
  command match{
    case "up" => aim -= amount
    case "down" => aim += amount
    case "forward" => {
      horizontal += amount
      depth += (aim*amount)
    }
  }
}

print(horizontal*depth)