#Math/Statistics #Physics/Experiment

```ad-danger
Still a lot of questions from the main reference, don't trust the my own notes too much. 
```

Main reference: [**CDF note: Everything you always wanted to know about pulls**](https://lucdemortier.github.io/assets/papers/cdf5776_pulls.pdf)

# Theoretical basis

## Some theorem
* [**Continuous mapping theorem**](https://en.wikipedia.org/wiki/Continuous_mapping_theorem)
  > In a nutshell, if a transformation is continuous except for few points, then the transformation could be applied to the PDF. 
  > 
  > Example: If $X$ is a random variable with normal distribution, then the distorted random variable g is still a normal.
  >
  > $$
  g = \frac{X-\mu}{\sigma} \sim N(0, 1)
  $$

* **Classical CLT**
  > If $\{X_i\}$ is a sequence of independent random variables with mean $mu$ and variance $\sigma^{2}$.
  > Define $S_n = \sum_{i=1}^{n}X_{i}$
  > Then
  > $$
  Z_n = \frac{S_n - n\mu}{\sqrt{n}\sigma} = \frac{\bar{X}-\mu}{\sigma/\sqrt{n}} \stackrel{d}\to N(0, 1)
  $$

* [**Lindeberg's CLT**](https://en.wikipedia.org/wiki/Lindeberg%27s_condition)
  > Let $\{X_1, ... ,X_n\}$ is a set of independent random variable. 
  >
  > * They're **not needed to be identical distributed**.
  > * Each of them have finite mean and variance.
  > 
  >
  > If the following **Lindeberg's condition** is satisfied,
  > $$
  \lim_{n\to\infty}\frac{1}{s_{n}^{2}}\sum_{i}^{n}E[(X_i-\mu_{i})^{2}\times{}1_{\{|X_i - \mu_i|>\varepsilon{}s_{n}\}}] = 0, \forall \varepsilon > 0 $$
  > , where $s_{n} = \sum^{n}\sigma_i^{2}$. 
  > Then
  > $$\frac{1}{s_{n}}\sum_{i}(X_{i}-\mu_{i}) \xrightarrow{d} N(0, 1)$$
  > Lindeberg's condition is sufficient but not necessary.
  > A slightly tighter sufficient and necessary condition is
  > $$
  \max_{k=1,..,n }\frac{\sigma_k^2}{s_{n}^2} \to 0,~\text{as}~n\to\infty$$

  Extremely rare we have strange terms break the condition, it's safe to just jump to Gaussian-like behavior with large stat.

----

When a histogram is formed, yields in each bin distributes with Poisson distribution and it behaves like a Gaussian when there are lots of events. We could just standardize the random variable in each bin by
$$
g = \frac{\tau_m - \tau_g}{\sigma_m} \sim N(0, 1)
$$
in which the measured value $\tau_m\pm\sigma_m$ can be refered as a Gaussian around the **true value** $\tau_g$. There's no need to worry about the difference between $\sigma_g$ and $\sigma_m$ since $\sigma_m$ converge to the $\sigma_g$ with large sample.

Following use case could be inferred from the above statement.

* In the case of shape fitting, especially for data, the true value $\tau_g$ is unknown, when estimated value is close enough to $\tau_g$, $g$ distributes as a unit Gaussian. We take advantage of this feature to ensure proper modeling PDFs is used.
* We take advantage of this method to ensure a good fitting procedure in terms of pseudo-experiment test.

## And some of our daily fitting routine

In the case of parameter estimation, we often use $\chi^{2}$ fit or ML fit.

In a least-$\chi^2$ fit, try to minimize

$$
\begin{align*}
\chi^{2}&=\sum_{i}\left(\frac{y_{i}^{e x p}-y_{i}^{pred}(\tau)}{\sigma_{i}}\right)^{2}\\
\frac{\chi^2}{d\tau} &= -2(\sum_{i}\frac{y_{i}^{e x p}-y_{i}^{pred}(\tau)}{\sigma_i^2}\frac{dy_i^{pred}}{d\tau}) = 0|_{\tau=\tau_{m}}
\end{align*}
$$

Or alternatively in ML fit,

$$
\ln{\mathcal{L}} = \sum_{i}\ln{f(y_{i}^{exp}, y_{i}^{pred}(\tau), \sigma_{i})}
$$

* $y_{i}^{exp} \pm \sigma_{i}$: Measured value from experiment.
* $y_{i}^{pred}(\tau)$: Predicted value parametrized with $\tau$.
* $f = P(y^{exp} | y^{pred}(\tau))$, for physics process, this is usually assumed to be Poisson distribution.

And we denote the fit result gives $\tau_{m} \pm \sigma_{m}$. 

----

We often encounter with constrained situation.

In least-$\chi^2$ fit, try to minimize
$$
\chi^{2}=(\frac{\tau - \tau_{c}}{\sigma_{c}})^{2} + \sum_{i}\left(\frac{y_{i}^{e x p}-y_{i}^{pred}(\tau)}{\sigma_{i}}\right)^{2}\\
\frac{\chi^2}{d\tau} = 2\frac{\tau-\tau_c}{\sigma_c^2}-2(\sum_{i}\frac{y_{i}^{e x p}-y_{i}^{pred}(\tau)}{\sigma_i^2})\frac{dy}{d\tau}
$$

Or alternatively in constrained ML fit,
$$
\ln{\mathcal{L}} = -\frac{1}{2}(\frac{\tau-\tau_{c}}{\sigma_{c}})^{2}- \ln({\sqrt{2\pi}\sigma_{c}})+\sum_{i}\ln{f(y_{i}^{exp}, y_{i}^{pred}(\tau), \sigma_{i})}
$$

* $\tau_{c} \pm \sigma_{c}$: Constraint and its error.

In this case, the fit result gives $\tau_f \pm \sigma_f$.

----
# Proper definition of pulls in pseudo-experiments

In pseudo-experiment test, the true values of parameters of interest is known. We generate toy samples with known model and test if the estimated results converge to true values.

## Unconstrained fits

In either of ML fit or least chi2 fit, the sum-over-i term converges to $\chi^{2}_{k}(\tau)$ given each i-terms are independent random variable. When $y(\tau)$ is a continuous mapping, we could replace $y$ with $\tau$ in the sum-over-i term without changing the distribution

$$

$$

# Proper definition to the extended likelihood method

*This section is beyond the main reference*

Start from the likelihood:

$$
\begin{aligned}
    \mathcal{L}(X; \theta) &= e^{-\lambda{}}\frac{\lambda{}^{\tau}}{\tau!}\prod_{i}f(X_{i};\theta{})\\
    \ln\mathcal{L} &= -\lambda +\tau\ln{\lambda} +\sum_{i}\ln{f}-\ln{\tau!}\\
    \partial_{\lambda}\ln{\mathcal{L}} &= -1 + \frac{\tau}{\lambda} + \sum{}\partial_{\lambda}\ln{f} = 0\\
\end{aligned}
$$

, where
* $f$ is the probability density for observing $X_i$ under parameters $\theta$.
* $\lambda$ and $\tau$ are expected and observed yields.

Suppose $\lambda$ is independent from $\theta$, then we have

$$
    \lambda = \tau
$$

But in most case $\lambda = \lambda(\theta)$, corrections are introduced.
Consider a case with large stat, it's suitable for Stirling formula and assuming almost negligible dependence between $\lambda$ and $\theta$.

$$
\begin{aligned}
    \ln{\mathcal{L}} &= -\lambda + \tau\ln{\lambda} - \ln{(\sqrt{2\pi{}\tau}(\frac{\tau}{e})^{\tau})} + \sum{}\ln{f}\\
    &= \tau -\lambda + \tau\ln{\frac{\lambda}{\tau}} - \frac{1}{2}\ln{(2\pi{}\tau)} + \sum \ln{f} \\
    &\stackrel{\lambda = \tau,~\text{by CLT}}{\sim} -\frac{1}{2}\ln{(2\pi{}\tau)} + \sum\ln{f}
\end{aligned}
$$

# Reference
