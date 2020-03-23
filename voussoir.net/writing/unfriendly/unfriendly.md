# Unfriendly

## mega.py

@voussoir

> **Fix RSA Invalid Condition on login**

> Fixes #10

> First of all, thanks for this library. I was having some unicode issues with megatools and decided to give mega.py a shot.

> mega.py was using a hardcoded RSA public exponent of 257. But this was raising an RSA Invalid Condition exception. According to MEGA's webclient js:

> ```
> // MEGA.nz -- crypto.js
> var q = privkey[0],
>     p = privkey[1],
>     d = privkey[2],
>     u = privkey[3],
>     q1 = q.subtract(1),
>     p1 = p.subtract(1),
>     m = new asmCrypto.Modulus(p.multiply(q)),
>     e = new asmCrypto.Modulus(p1.multiply(q1)).inverse(d),
>     dp = d.divide(p1).remainder,
>     dq = d.divide(q1).remainder;
> ```

> The public exponent `e` needs to be calculated from the inverse of `(p-1)*(q-1)`.

> This pull request:

> - implements modular_inverse and calculates the public exponent
> - clarifies the private_key decoding by de-golfing that code
> - clarifies the RSA construct by assigning each piece to a named variable first

> If this pull request is accepted, I would like to make some followup pull requests to further increase clarity, add comments and docstrings, move API calls into named functions with docstrings, and de-golf complicated lines.

> This is my first time using gitlab instead of github so please let me know if I did anything wrong. Everything is similar but... different.

[screenshot](megapy_1.png)

---

@richardARPANET

> > ```
> > def modular_inverse(a, m):
> > '''
> > Thank you Mart Bakhoff for this solution.
> > '''
> > ```

> can you remove the thanks? Thank them on stackoverflow instead if you like

[screenshot](megapy_2.png)

---

@voussoir

> Hi,

> Stackoverflow says

> > As noted in the Stack Exchange Terms of Service and in the footer of every page, all user contributions are licensed under Creative Commons Attribution-Share Alike. Proper attribution is required if you republish any Stack Exchange content.

> https://stackoverflow.com/help/licensing

> For this reason I always include a thanks comment. Sometimes there is a threshold of triviality to not give credit but I'd rather be more friendly than less.

> I switched the docstring quotes.

---

@richardARPANET

> I'm not interested in advertising stackoverflow for free. I'll remove it in master.

---

@voussoir
> RIP the rest of pull requests I was going to make.


[he bans my account](megapy_3.png)

[and deleted my final comment](megapy_4.png)

[and does some 'linting'](megapy_5.png)


### Final thoughts

I think my use of the term "de-golf" in the original PR was offensive by implying richard had shortened the code on purpose. In fact, much of MEGA's own source code is highly compacted and much of the python code was simply transliterated from that.

I will publish the remainder of my work [here](https://github.com/voussoir/mega.py).
