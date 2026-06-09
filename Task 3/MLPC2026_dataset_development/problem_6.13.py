import numpy as np

# Rosenbrock function (p. 7)
def f(x):
    return 100*(x[1] - x[0]**2)**2 + (1 - x[0])**2

# Gradient of Rosenbrock
def grad_f(x):
    dfdx1 = -400*x[0]*(x[1] - x[0]**2) - 2*(1 - x[0])
    dfdx2 = 200*(x[1] - x[0]**2)
    return np.array([dfdx1, dfdx2])

# Armijo backtracking (Algorithm 6.11, step 3, p. 6)
def armijo_backtracking(x, p, grad, alpha0=1, rho=0.5, c1=0.01):
    alpha = alpha0
    while f(x + alpha*p) > f(x) + c1 * alpha * np.dot(grad, p):
        alpha *= rho
    return alpha

# Inverse BFGS update (6.8, p. 5)
def update_S(S, s, y):
    """S^+ = S + ((s - Sy)s^T + s(s - Sy)^T)/(y^T s) - ((s - Sy)^T y)/(y^T s)^2 * s s^T"""
    sy = np.dot(y, s)
    if sy <= 0:
        return S  # reset if condition fails (p. 6, step 4)
    S_y = S @ y
    s_minus_Sy = s - S_y
    term1 = np.outer(s_minus_Sy, s) + np.outer(s, s_minus_Sy)
    term1 /= sy
    term2 = (np.dot(s_minus_Sy, y) / (sy**2)) * np.outer(s, s)
    S_new = S + term1 - term2
    # Ensure symmetry (numerical)
    return (S_new + S_new.T) / 2

# BFGS method with globalization (Algorithm 6.11, p. 6)
def bfgs(x0, S0, eta=1e-4, tol=1e-12, max_iter=100):
    x = x0.copy()
    S = S0.copy()
    history = []
    for k in range(max_iter):
        g = grad_f(x)
        fx = f(x)
        norm_g = np.linalg.norm(g)
        # Compute search direction (Algorithm 6.11, step 1, p. 6)
        p = -S @ g
        # Angle condition check (Algorithm 6.11, step 2, p. 6)
        if np.dot(g, p) > -eta * norm_g * np.linalg.norm(p):
            p = -g
            S = np.eye(len(x0))  # S^k = S^0 (p. 6)
        # Armijo backtracking (Algorithm 6.11, step 3, p. 6)
        alpha = armijo_backtracking(x, p, g)
        x_new = x + alpha * p
        s = x_new - x
        y = grad_f(x_new) - g
        # Update inverse Hessian approximation (Algorithm 6.11, step 4, p. 6)
        if np.dot(y, s) > 0:
            S = update_S(S, s, y)
        else:
            S = np.eye(len(x0))  # reset if condition fails (p. 6, step 4)
        # Record history
        x_star = np.array([1.0, 1.0])
        dist = np.linalg.norm(x_new - x_star)
        q = dist / np.linalg.norm(x - x_star) if k > 0 else np.nan
        history.append([k, fx, norm_g, np.linalg.norm(x - x_star), alpha, q])
        # Check convergence
        if norm_g < tol:
            break
        x = x_new
    return np.array(history)

# Parameters from Table 6.1 (p. 7)
alpha0 = 1
rho = 0.5
c1 = 0.01
eta = 1e-4
tol = 1e-6  # stopping tolerance as in Chapter 4 (p. 15)
S0 = np.eye(2)

print("=" * 60)
print("Table for x0 = (-1.0, 1.2)  (should match Table 6.1, p. 7)")
print("=" * 60)
x0_table = np.array([-1.0, 1.2])
hist_table = bfgs(x0_table, S0, eta, tol, max_iter=40)
for row in hist_table[:5]:
    print(f"{int(row[0]):d}  {row[1]:8.4f}  {row[2]:8.4f}  {row[3]:8.4f}  {row[4]:5.2f}  {row[5]:8.4f}")
print("...")
for row in hist_table[-4:]:
    print(f"{int(row[0]):d}  {row[1]:8.4e}  {row[2]:8.4e}  {row[3]:8.4e}  {row[4]:5.2f}  {row[5]:8.4f}")

print("\n" + "=" * 60)
print("Table for x0 = (-1.2, 1)  (Problem 6.13)")
print("=" * 60)
x0_prob = np.array([-1.2, 1.0])
hist_prob = bfgs(x0_prob, S0, eta, tol, max_iter=40)
for row in hist_prob[:5]:
    print(f"{int(row[0]):d}  {row[1]:8.4f}  {row[2]:8.4f}  {row[3]:8.4f}  {row[4]:5.2f}  {row[5]:8.4f}")
print("...")
for row in hist_prob[-4:]:
    print(f"{int(row[0]):d}  {row[1]:8.4e}  {row[2]:8.4e}  {row[3]:8.4e}  {row[4]:5.2f}  {row[5]:8.4f}")