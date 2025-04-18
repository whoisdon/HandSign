from sklearn.ensemble import RandomForestClassifier

def treinar_modelo(dados, rotulos):
    clf = RandomForestClassifier()
    clf.fit(dados, rotulos)
    return clf