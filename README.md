# P1-Square-Pyramid
Write a python program to calculate the surface area and volume of a square pyramid.

|------   Problem:   ------|
Write a program to calculate the surface area and volume of a square pyramid.
A square pyramid has a base that is square and all triangle faces are congruent isosceles triangles. (An isosceles triangle is a triangle in which two of the sides are equal.)
For this program you are to determine two things about a square pyramid:
1) the surface area of the four sides, and 2) the volume. 
 	
Length of base: a      Height of the pyramid: h
Volume = a2h/3         Slant height, s  = sqrt(h2 + (a/2)2)  
Area of one pyramid side = s*a/2

|------  Test Cases:  ------|
Pyramid #1:	  Height:  5.0’ 		Base: 2.5’
Pyramid #2:	  Height:  2.5’ 		Base: 4.3’


|------ Hand Calculations:  ------|

The volume of any pyramid is 1/3 the area of the base times the height. 
                      b = length of base side 
  V = 1/3 b**2 * h    B = area of the base (b*b) 
                      h = height of pyramid

  |--- Volume:  ---|

    Pyramid #1:
            1. H = 5’               2. B = (2.5’)(2.5’) = 6.25sq.ft.
      3. V = 1/3 (2.52)(5) =        4. V = 1.6667(6.25) = 10.416667ft**3 (ft.sq.)
        
        The volume of Pyramid #1 = 10.416667ft**3 (ft.sq.)
  
     Pyramid #2:
             1. H = 2.5’             2. B = (4.3’)(4.3’) = 18.49sq.ft
        3. V = 1/3 (4.32)(2.5) =     4. V = 0.8333(18.49) = 15.408333ft**3 (ft.sq.)
         
         The volume of Pyramid #1 = 15.408333ft**3 (ft.sq.)
         
         
   |--- Pythagorean Theory: ---|
          a2 + b2 = c2

      Pyramid #1:
        (1/2 * base)**2 + (height**2) = c**2 
            1.25**2 +5**2 = c**2
            1.5625 + 25 = c**2
            √26.5625 = c
            C = 5.153882 (Slant Height)
      
      Pyramid #2:
        (1/2 * base)**2 + (height**2) = c**2 
            2.15**2 +2.5**2 = c**2
            4.6225 + 6.25 = c**2
            √10.8725 = c
            C = 3.2973474188 (Slant Height)
            
   |--- Area: ---|
     Area = 2bs + b**2
     
      Pyramid #1:
        A = 2 * (2.5 * 5.153882032) + (2.52) = 32.01941016 ft2.
        
      Pyramid #2:
        A = 2 * (4.3 * 3.2973474188) + (4.32) = 46.847187802 ft2
