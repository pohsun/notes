-- vim: set sts=2 sw=2 noet:

main :: IO ()
main = do
  let showEval :: Int -> IO ()
	showEval expr = do
	  let result = expr
	  putStrLn (show result)

  showEval 10
  showEval ((+) 5 3 4)
--  --showEval ((-) 10 1)
--  --showEval ((/) 6 2)
--  --showEval ((+) ((*) 2 4) ((-) 4 6))
--  --let a = 3
--  --let b = ((+) a 1)
--  --showEval b


--main :: IO ()
--main = do
--    let printAndDouble :: Int -> IO ()
--        printAndDouble x = do
--            putStrLn ("Received: " ++ show x)
--            let result = x * 2
--            putStrLn ("Result: " ++ show result)
--    putStrLn "Starting..."
--    printAndDouble 5
--    putStrLn "Done."

