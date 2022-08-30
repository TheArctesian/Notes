A bit of dense calculus here but here we go [[13]]

Using the simple formula for work [[2.4 Work Energy and Power]]
$$
W_{total} = \sum_{i} W_{i} = \sum_{i} F_i\cdot\Delta r_i
$$
We know [[6.2 Newton's law of gravitation]]

$$F = G\frac{Mm}{r^2} $$
And imaging we are trying to pull a mass M from a infinitely far distance, we take the integral of the F from R(radius of earth) to infinity in respect to r 
$$
\int_{R}^{\infty} G\frac{Mm}{r^2} \,\mathrm{d}r
$$
As G, M and m are constant we can get rid of that 

$$
GMm\times\int_{R}^{\infty}\frac1{r^2} \,\mathrm{d}r
$$
We evaluate the integral
$$

\int_{R}^{\infty}\frac1{r^2} \,\mathrm{d}r
= \int_{R}^{\infty}r^{-2}\mathrm{d}r

$$
Now we can integrate
$$
GMm
\left[\frac{1}{r}+r^{-1}\right]_R^\infty
$$
$$
GMm(\frac{1}{-\infty}+\frac{1}{R})
$$
As 1 \ infinity is 0 
$$
W = G\frac{Mm}{r}
$$
and as 
$$
PE\lim_{\rightarrow\infty} = 0
$$
$$
\therefore PE = -G\frac{MM}{R}
$$
[[Gravitational Energy]]
The GPE at a point is the work done in moving a point mass from infinity to the point

$$
PE_\infty = 0 \; PE_\infty = 0
$$
$$
TE_{surface} = GPE + KE 
$$
$$
TE_\infty = 0 = \frac12mv^2_{esc}-(G\frac{Mm}r)=\frac12v^2_{esc} - G\frac{M}R
$$
$$
\therefore v_{esc} = \sqrt{\frac{2Gm}{R_e}}
$$
In an orbit  F is a centripetal force which is [[6.2 Newton's law of gravitation]]
$$
F=G\frac{Mm}{r^2} = ma
$$
$$
a = rm^2=\frac{v^2}r=\frac{4\pi^2r}{T^2}
$$
$$
F=G\frac{Mm}{r^2} = m\frac{v^2}{r}

$$
$$
\therefore v^2=G\frac{m}r
$$
$$
V_{orb}=\sqrt{\frac{GM}{r}}
$$
TE of 