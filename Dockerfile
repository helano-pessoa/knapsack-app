FROM python:3.7
    
# Install pip requirements
ADD requirements.txt .
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
#---------------------------------------------------------------------------------------------
WORKDIR /knapsack-app
ADD . /knapsack-app

CMD ["/bin/bash"]