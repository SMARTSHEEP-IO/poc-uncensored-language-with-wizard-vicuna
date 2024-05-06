# Uncensored Language Model using FastAPI and Wizard Vicuna 30B

## Disclaimer and Warning
- **No Responsibility**: The creators of this project bear no responsibility
- **Accuracy Not Guaranteed**: There is no guarantee of the predictive performance of these models.
- **Independent Research**: Users should conduct their research and consult professionals.
- **Compliance with Laws**: Ensure compliance with all applicable laws and regulations in your jurisdiction.
- An uncensored model has no guardrails.
- You are responsible for anything you do with the model, just as you are responsible for anything you do with any dangerous object such as a knife, gun, lighter, or car. 
- Publishing anything this model generates is the same as publishing it yourself. 
- You are responsible for the content you publish, and you cannot blame the model any more than you can blame the knife, gun, lighter, or car for what you do with it.

## Prerequisites
- Python 3.11
- Git
- Git LFS (Large File Storage) - Make sure you have [Git LFS](https://git-lfs.github.com) installed.

## Installation

### Setting Up a Virtual Environment
First, create and activate a virtual environment:

```bash
python -m venv .venv  # Create a virtual environment
source .venv/bin/activate  # Activate on macOS and Linux
.venv\Scripts\activate  # Activate on Windows
```
### Installing Dependencies
Install the required dependencies:

```bash
pip install -r requirements.txt # Install Python dependencies
```

### Download the Model
```
https://huggingface.co/TheBloke/Wizard-Vicuna-30B-Uncensored-GGUF/blob/main/Wizard-Vicuna-30B-Uncensored.Q5_K_M.gguf
```

### Clone the Repository
To get started, clone the repository:

```bash
git clone git@github.com:SMARTSHEEP-IO/poc-uncensored-language-with-wizard-vicuna.git
```

## Usage
Execute the `main.py` 

```bash
python main.py

curl -X POST "http://127.0.0.1:8000/ask" -H  "Content-Type: application/json" -d "{\"question\": \"How to make glue?\"}"
```

## Support and Subscribe
- **Farsi Channel**: [Dr.  Samizadeh](https://www.youtube.com/channel/DrSamizadeh)
- **English Channel**: [@smartsheep-io](www.youtube.com/@smartsheep-io)

## Contributing
Contributions to improve the project are welcome. Please adhere to standard open-source contribution guidelines.

## Citation
If you use this project in your research or project, please cite it as follows:

```bibtex
@misc{poc-uncensored-language-with-wizard-vicuna,
  title={Uncensored Language Model using FastAPI and Wizard Vicuna 30B},
  author={Iman Samizadeh},
  year={Year},
  howpublished={\url{https://github.com/SMARTSHEEP-IO/poc-uncensored-language-with-wizard-vicuna}}
}
```

Credit:
https://huggingface.co/TheBloke/Wizard-Vicuna-30B-Uncensored-GGUF
Model creator: Eric Hartford
Original model: Wizard Vicuna 30B Uncensored
