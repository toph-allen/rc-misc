myLast [] = []
myLast (a : []) = [a]
myLast (_ : as) = myLast as

myLast2 :: [a] -> Maybe a
myLast2 [] = Nothing
myLast2 (a : []) = Just a
myLast2 (_ : as) = myLast as
