#CS #Math

# Information Theory

* Textbook: Elements of Information Theory 2nd Ed, by T. M. Cover, J. A. Thomas
    * Check your ebook lib, there's also a solution manual.

# Basics

* [**Information content**](https://en.wikipedia.org/wiki/Information_content)
    * An alternative way to express the probability of a particular event.
    * Also known as **self-information**, **surprisal**, or **Shannon information**.
    * The *AXIOM*s
        1. An event with probability 100% is perfectly unsurprising and yields no information.
        2. The less probable an event is, the more surprising it is and the more information it yields.
        3. If two independent events are measured separately, the total amount of information is the sum of the self-informations of the individual events.
    * By the axioms, the formula is 
        $$
            I = -\log_{b}{P} \text{ for arbitrary } b
        $$
* [**Shannon entropy**](https://en.wikipedia.org/wiki/Entropy_(information_theory))
    * Interpreted as the information of a random variable.
    * Based on the self-information, the definition is
        $$
            H(X) = \mathbb{E}[I(X)] = - \sum P(x_i)\log{}P(x_i)
        $$
    * **differential entropy**: In the discrete case, $H(X)$ is non-negative. However, when we consider the continuous limit:  
        $$\begin{align*}
                H(X) &= \mathbb{E}[I(X)]\\
                    &= \lim_{\Delta\to{}0}\left\{-\sum P(x_i)\Delta\log{}P(x_i)\Delta\right\}\\
                    &= \lim_{\Delta\to{}0}\left\{-\sum P(x_i)\Delta\log{}P(x_i)\right\} - \log{}\Delta\\
                    &= - \int P(x_i)\log{}P(x_i) - \log{}\Delta
        \end{align*}$$ The quantity representing precision $\Delta$ reflects the face that *to specify a continuous variable very precisely requires a large number of bits*. In addition, **differential entropy can be negative** since arbitrary precision factor is removed. The absolute value is therefore not so meaningful.
    * For non-independent r.v., there is [**conditional entropy**](https://en.wikipedia.org/wiki/Conditional_entropy).
        $$
            H(Y|X) = - \sum P(x,y)\log{}P(x,y)/P(x)
        $$
* [**Kullback-Leibler divergence**](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence)
    * Also known as the **relative entropy**.
    * Quantize the difference of two distributions of a random variable.        
        $$
            KL(P||Q) = \mathbb{E}_{x\sim{}P}\left(\log\frac{P(x)}{Q(x)}\right) = \sum P(x)\left[-\log{Q(x)} - -\log{P(x)}\right]
        $$
        * Remark that the formula is *asymmetric* between $P$ and $Q$.
    * Conventions: 
        * PRML: *Consider some unknown distribution $P$, and suppose that we have modelled this using an approximating distribution $Q$. If we use $Q$ to construct a coding scheme for the purpose of transmitting values of $x$ to a receiver, then the average additional amount of information required to specify the value of x (assuming we choose an efficient coding scheme) as a result of using $Q$ instead of the true distribution $P$ is $KL(P||Q)$*
        * PRML: *If we use a distribution that is different from the true one, then we must necessarily have a less efficient coding, and on average the additional information that must be transmitted is (at least) equal to the Kullback-Leibler divergence between the two distributions.*
* [**Mutual information**](https://en.wikipedia.org/wiki/Mutual_information)
    * PRML: *If the sets of variables are independent, then their joint distribution will factorize into the product of their marginals $p(x, y) = p(x)p(y)$. If the variables are not independent, we can gain some idea of whether they are 'close to being independent by considering the Kullback-Leibler divergence between the joint distribution and the product of the marginals*  $$\begin{align}
        I[x, y] &\equiv KL(p(x,y)||p(x)p(y))\\
            &= -\iint p(x,y)\log{}\left(\frac{p(x)p(y)}{p(x,y)}\right)dxdy
        \end{align}$$
    * $I \geq 0$, the equality if, and only if, $x$ and $y$ are independent.
    * $I[x, y] = H[x] - H[x|y] = H[y] - H[y|x]$, where $H$ is the Shannon entropy.
* [**Cross entropy**](https://en.wikipedia.org/wiki/Cross_entropy)
    * Based on the self-information, the definition is
        $$
            H(X) = \mathbb{E}[I(X)] = - \sum P(x_i)\log{}Q(x_i)
        $$
* [**f-divergence**](https://en.wikipedia.org/wiki/F-divergence)
