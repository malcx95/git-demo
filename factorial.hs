import System.IO

factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial(n - 1)

readInt :: IO Integer
readInt = readLn

main :: IO ()
main = do
    putStrLn "Enter a number:"
    n <- readInt
    print $ factorial n

