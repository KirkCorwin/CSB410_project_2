PROJECT_NAME="asl_project"
CONDA_ENV_NAME="asl_project"
CONDA_ENV_PYTHON="3.12"
CONDA_FILE=""
PIP_REQUIREMENTS=""

echo "Creating a conda environment"
if [ -z "$CONDA_FILE" ]; then
    conda create -y -n $CONDA_ENV_NAME Python=$CONDA_ENV_PYTHON
else
    conda env create --name $CONDA_ENV_NAME -f $CONDA_FILE
fi

. $(conda info --json | jq -r '.root_prefix')/etc/profile.d/conda.sh
conda activate $CONDA_ENV_NAME

echo "Installing core dependencies"
conda install -y \
    numpy \
    pandas \
    matplotlib \
    seaborn \
    scikit-learn \
    tensorflow \
    -c defaults \
    -c conda-forge

echo "Installing Jupyter kernel"
conda install -y jupyter ipykernel

if [ -n "$PIP_REQUIREMENTS" ]; then
    pip install -r $PIP_REQUIREMENTS --quiet
fi

python -m ipykernel install --user \
    --name $CONDA_ENV_NAME \
    --display-name "Python ($CONDA_ENV_NAME)"

echo "Configuring PYTHONPATH for the project"
PYTHON_SITE=$(python -m site --user-site)
mkdir -p $PYTHON_SITE
cat >> $PYTHON_SITE/$PROJECT_NAME.pth <<EOF
$PWD/src
EOF

echo "Setup complete."
echo "Activate with: conda activate $CONDA_ENV_NAME"
