import os

sub_networks = {
    "core": [
        "neuro-hub",
        "bio-copilot",
        "neuro-pipeline",
        "biogpt-lit"
    ],
    "genomics": [
        "genomegpt",
        "gene-analysis",
        "gene-explorer",
        "dark-genome",
        "rna-decoder",
        "deepsplice",
        "openclinvar",
        "str-scope",
        "codon-opt"
    ],
    "crispr": [
        "crispr-opt",
        "crispr-cargo",
        "crispr-muse",
        "epi-edit",
        "prime-design"
    ],
    "chemistry": [
        "chemgpt-engine",
        "bio-material"
    ],
    "proteins": [
        "alpha-fold-ui",
        "docking-studio",
        "evofold-4d",
        "mutdock",
        "protein-painter"
    ],
    "synbio": [
        "synbio-wizard",
        "syn-bio-studio",
        "metabodesigner",
        "promoter-lib",
        "synthetic-life",
        "living-computer",
        "bio-switch"
    ],
    "automation": [
        "biofactory-1a",
        "robotic-flow",
        "cell-free-opt",
        "syn-stab-ai",
        "stability-ai"
    ],
    "cellular": [
        "cell-twin",
        "fate-predictor",
        "cellfatenet",
        "organoid-ai",
        "virtual-cell",
        "bioimage-ai",
        "cellpainter",
        "cellpainter-4d",
        "syndroid",
        "tissue-eng"
    ],
    "therapeutics": [
        "phageforge",
        "infinite-diagnosis",
        "car-t-designer",
        "living-tx",
        "neohunter"
    ]
}

base_dir = "modules"

for network, modules in sub_networks.items():
    network_path = os.path.join(base_dir, network)
    os.makedirs(network_path, exist_ok=True)
    
    # Create a README for the network
    with open(os.path.join(network_path, "README.md"), "w") as f:
        f.write(f"# {network.capitalize()} Sub-network\n\n")
        f.write(f"Contains {len(modules)} specialized modules.\n")
    
    for module in modules:
        module_path = os.path.join(network_path, module)
        os.makedirs(module_path, exist_ok=True)
        
        # Create a basic README for each module
        with open(os.path.join(module_path, "README.md"), "w") as f:
            f.write(f"# {module.replace('-', ' ').title()}\n\n")
            f.write(f"Part of the {network} sub-network of SugarCode AI.\n")

print("Scaffolding complete.")
