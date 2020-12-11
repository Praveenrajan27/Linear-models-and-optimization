
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import sys
def fit_predict(X_train, y_train, X_test, degree=4):
    poly_features=PolynomialFeatures(degree)
    X_poly=poly_features.fit_transform(X_train)
    X_reg = LinearRegression()
    X_reg.fit(X_poly,y_train)
    print(X_reg.predict(X_test))


stdin_line = sys.stdin
f= int(stdin_line[0].strip().split(' ')[0])
n= int(stdin_line[1].strip().split(' ')[0])
t= int(stdin_line[1].strip().split(' ')[n])
X=[]
y=[]
for line in range(1,n+1):
    X.append(line[:-1])
    y.append(line[-1])
for line in range(n+2,n+2+t):
    x.append(line)

fit_predict(X,y,x)
    
    