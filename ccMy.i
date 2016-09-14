  	loadI   0               =>r20   // Initial value
        loadI   1               =>r19   // Increment amount
        add     r20, r19        =>r0    // Initialize counter
        add     r20, r19        =>r1    // Initialize counter
        add     r20, r19        =>r2    // Initialize counter
        add     r20, r19        =>r3    // Initialize counter
        loadI   1024            =>r20   // Address
        store   r19             =>r20
        output  1024
        add     r19, r0         =>r0
        add     r19, r1         =>r1
        add     r19, r2         =>r2
        add     r19, r3         =>r3
        add     r19, r0         =>r19   // Summation
        add     r19, r1         =>r19   // Summation
        add     r19, r2         =>r19   // Summation
        add     r19, r3         =>r19   // Summation
        loadI   1024            =>r20   // Address
        store   r19             =>r20
        output  1024

