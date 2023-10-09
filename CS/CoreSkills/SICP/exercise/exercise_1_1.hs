-- vim: set sts=2 sw=2 noet:

main :: IO ()
main = do
  putStrLn (show 10)
  --putStrLn (show ((+) 5 3 4))
  --putStrLn (show ((-) 10 1))
  --putStrLn (show ((/) 6 2))
  --putStrLn (show ((+) ((*) 2 4) ((-) 4 6)))
  let a = 3
  let b = ((+) a 1)
  putStrLn (show b)
