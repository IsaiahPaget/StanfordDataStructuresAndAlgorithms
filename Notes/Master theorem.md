T(n) = aT ( ceil( n / b )) + O(n^d)

Time complexity T(n) = O(n^d) if d > log<sub>b</sub> a
	else O(n^d log n) if d = log<sub>b</sub> A
	else O(n^log<sub>b</sub> A) if d < log<sub>b</sub> A

Tip:

"when I have a recurrence of this rough form, I look at the amount of work done at the first and second level and I ask myself. Is it the same amount of work done? If it's the same amount of work then we are going to be in case two ^. If the first term is larger than the second term, and we are in the first case ^. Else if the first term is less than the second then we are in the last case ^.