def mc_pi(n, c=2**10):
    stat = 0.0
    for i in range(0, n, c):
        m = min(c, n - i)
        pts = rng.random_sample((m, 2))
        hits = (pts[:,0]**2 + pts[:,1]**2) < 1.0
        stat += np.sum(hits)
    return 4.0*stat/n
