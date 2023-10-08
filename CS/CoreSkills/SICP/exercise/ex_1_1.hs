main :: IO ()
main = do
    let result = show 10
    putStrLn result

    let result = show (sum [5, 3, 4])
    putStrLn result
