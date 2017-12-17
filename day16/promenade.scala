import scala.io.Source
import scala.collection.mutable.{Map => MutaMap}

object Promenade {
  // val/var changes scope of member into public, otherwise it's private
  class DanceMove(val action: Char, val x: Int, val a: String, val b: String) {
    override def toString: String =
    s"($action, $x, $a, $b)"
  }

  // Important that we use List and NOT Iterator
  // Iterator will only allow you to traverse the sequence once, and doesn't throw errors
  // in a foreach loop
  def getInput(): List[DanceMove] = {
    Source.fromFile("input").getLines.take(1).flatMap {
      _.split(",").map { word =>
        val action = word(0)
        if (action == 's') {
          new DanceMove(action, word.substring(1).toInt, "","")
        } else {
          val params = word.substring(1).split("/")
          new DanceMove(action, -1, params (0), params(1))
        }
      }
    }.toList
  }

  def spinDict(progToIndx: MutaMap[Char, Int], indxToProg: MutaMap[Int, Char], amount: Int) = {
    for ((prog, index) <- progToIndx) {
        val newIndx = (progToIndx(prog) + amount) % progToIndx.size
        progToIndx(prog) = newIndx
        indxToProg(newIndx) = prog
    }
  }

  def swapInDictByIndx(progToIndx: MutaMap[Char, Int], indxToProg: MutaMap[Int, Char], aIndx: Int, bIndx: Int) = {
    val a = indxToProg(aIndx)
    val b = indxToProg(bIndx)
    progToIndx(a) = bIndx
    progToIndx(b) = aIndx
    indxToProg(aIndx) = b
    indxToProg(bIndx) = a
  }

  def swapInDictByName(progToIndx: MutaMap[Char, Int], indxToProg: MutaMap[Int, Char], a: Char, b: Char) = {
    val aIndx = progToIndx(a)
    val bIndx = progToIndx(b)
    progToIndx(a) = bIndx
    progToIndx(b) = aIndx
    indxToProg(aIndx) = b
    indxToProg(bIndx) = a
  }

  def main(args: Array[String]): Unit = {
      val input = getInput()
      val progToIndx = MutaMap[Char, Int]()
      val indxToProg = MutaMap[Int, Char]()
      val AtoP = "abcdefghijklmnop".toList
      AtoP.zipWithIndex.foreach {
        case(c, i) => {
          progToIndx(c) = i
          indxToProg(i) = c
        }
      }
      // We notice there is a pattern and that the answer will become abcdefghijklmnop every 24 iterations
      // Therefore we only have to calculate 1000000000%24 iterations!
      for (k <- 1 to (1000000000%24)) {
        input foreach { danceMove: DanceMove =>
          if (danceMove.action == 's') {
            spinDict(progToIndx, indxToProg, danceMove.x)
          }
          else if (danceMove.action == 'x') {
            swapInDictByIndx(progToIndx, indxToProg, danceMove.a.toInt, danceMove.b.toInt)
          }
          else if (danceMove.action == 'p') {
            swapInDictByName(progToIndx, indxToProg, danceMove.a(0), danceMove.b(0))
          }
        }
        /**
        var answer = new StringBuilder()
        for (i <- 0 to 15) {
            answer += indxToProg(i)
        }
        if (answer.toString == "abcdefghijklmnop") {
          println(k)
        }
        **/
      }

      var answer = new StringBuilder()
      for (i <- 0 to 15) {
          answer += indxToProg(i)
      }
      println(answer)
      //assert(answer.toString == "dcmlhejnifpokgba")
  }
}