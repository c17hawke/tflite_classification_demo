echo [$(date)]: "START"
export _VERSION_=3.7
echo [$(date)]: "creating environment with python ${_VERSION_}"
conda create --prefix ./env python=${_VERSION_} -y
echo [$(date)]: "activate environment"
source activate ./env
echo [$(date)]: "install requirements"
pip install -r requirements.txt
# echo [$(date)]: "export conda environment"
# conda env export > conda.yaml
echo [$(date)]: "create an src directory"
mkdir -p src && touch src/__init__.py src/main.py
# echo [$(date)]: "initialize git repository"
# git init
# echo [$(date)]: "add env to gitignore"
# echo "env/" >> .gitignore

# to remove everything -
# rm -rf env/ .gitignore conda.yaml README.md .git/
echo [$(date)]: "Now we can activate our environment"
echo [$(date)]: "by using below command"
echo [$(date)]: "conda activate ./env"
echo [$(date)]: "END"
