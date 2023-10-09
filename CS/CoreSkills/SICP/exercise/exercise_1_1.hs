--vim: set sts=4 sw=4 noet:

main :: IO ()
main = do
    let showEval x = do
        putStrLn (show x)

    showEval 10
    showEval ((+) 5 3 4)
    --showEval ((-) 10 1)
    --showEval ((/) 6 2)
    --showEval ((+) ((*) 2 4) ((-) 4 6))
    --let a = 3
    --let b = ((+) a 1)
    --showEval b
