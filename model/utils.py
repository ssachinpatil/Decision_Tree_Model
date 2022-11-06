import pickle,json
import numpy as np

class heart():
    def __init__(self,age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
        self.age=age
        self.sex=sex
        self.cp=cp
        self.trestbps=trestbps
        self.chol=chol
        self.fbs=fbs
        self.restecg=restecg
        self.thalach=thalach
        self.exang=exang
        self.oldpeak=oldpeak
        self.slope=slope
        self.ca=ca
        self.thal=thal

    def load_model(self):
        with open("DT_prun_model.pkl","rb") as f:
            self.prun_model=pickle.load(f)

        with open ("json_data.json","r") as f:
            self.json_data=json.load(f)

    def pred(self):
        self.load_model()
        array=np.array([self.age,self.sex,self.cp,self.trestbps,self.chol,self.fbs,self.restecg,self.thalach,self.exang,self.oldpeak,self.slope,self.ca,self.thal])
        prediction=self.prun_model.predict([array])[0]
        print(prediction)
        return prediction
if __name__=="__main__":
    result=heart(24,1,0,123,213,1,0,150,0,2.1,0,0,1)
    result.pred()