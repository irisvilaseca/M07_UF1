import pandas as pd
import random
import matplotlib.pyplot as plt

def generar_4_mesos_aleatoris():
    """Generar quatre mesos aleatoris."""
    return random.sample(range(1, 13), 4)

def load_data():
    """Carregar les dades des del CSV."""
    use_cols = ["location", "date", "total_cases", "total_deaths", "reproduction_rate"]
    df = pd.read_csv("./df_covid19_countries.csv", usecols=use_cols)
    df["date"] = pd.to_datetime(df["date"])
    return df

def casos_totals_per_mes_i_pais(df):
    """Calcular els casos totals per mes i país."""
    paisos = df["location"].unique()[:10]
    mesos = generar_4_mesos_aleatoris()
    dades_filtrades = df[(df["location"].isin(paisos)) & (df["date"].dt.month.isin(mesos))].copy()
    dades_filtrades["mes"] = dades_filtrades["date"].dt.month
    casos = dades_filtrades.groupby(["location", "mes"])["total_cases"].sum().reset_index()
    return casos

def morts_totals_mes_pais(df):
    """Calcular les morts totals per mes i país."""
    paisos = df["location"].unique()[:10]
    mesos = generar_4_mesos_aleatoris()
    dades_filtrades = df[(df["location"].isin(paisos)) & (df["date"].dt.year == 2021) & (df["date"].dt.month.isin(mesos))].copy()
    dades_filtrades["mes"] = dades_filtrades["date"].dt.month
    morts_totals = dades_filtrades.groupby(["location", "mes"])["total_deaths"].sum().reset_index()
    return morts_totals

def reproduction_rate(df):
    """Calcular la taxa de reproducció per mes i país."""
    paisos = df["location"].unique()[:10]
    mesos = generar_4_mesos_aleatoris()
    dades_filtrades = df[(df["location"].isin(paisos)) & (df["date"].dt.month.isin(mesos))].copy()
    dades_filtrades["mes"] = dades_filtrades["date"].dt.month
    taxa_reproduccio = dades_filtrades.groupby(["location", "mes"])["reproduction_rate"].sum().reset_index()
    return taxa_reproduccio

def plot_data():
    """Generar els gràfics dels casos totals, morts i taxa de reproducció."""
    df = load_data()
    fig, axs = plt.subplots(3, 1, figsize=(10, 15))

    # Primer gràfic: Casos totals
    casos = casos_totals_per_mes_i_pais(df)
    for pais in casos["location"].unique():
        data_pais = casos[casos["location"] == pais]
        data_pais = data_pais.sort_values(by="mes")
        axs[0].plot(data_pais["mes"], data_pais["total_cases"], marker='o', label=pais)
    axs[0].set_title("Casos totals per mes i país")
    axs[0].set_xlabel("Mes de l'any")
    axs[0].set_ylabel("Casos totals")
    axs[0].grid(True)
    axs[0].legend()

    # Segon gràfic: Morts totals
    morts = morts_totals_mes_pais(df)
    for pais in morts["location"].unique():
        data_pais = morts[morts["location"] == pais]
        data_pais = data_pais.sort_values(by="mes")
        axs[1].plot(data_pais["mes"], data_pais["total_deaths"], marker='o', label=pais)
    axs[1].set_title("Morts totals per mes i país")
    axs[1].set_xlabel("Mes")
    axs[1].set_ylabel("Morts totals")
    axs[1].grid(True)
    axs[1].legend()

    # Tercer gràfic: Taxa de reproducció
    taxa = reproduction_rate(df)
    for pais in taxa["location"].unique():
        data_pais = taxa[taxa["location"] == pais]
        data_pais = data_pais.sort_values(by="mes")
        axs[2].plot(data_pais["mes"], data_pais["reproduction_rate"], marker='o', label=pais)
    axs[2].set_title("Taxa de reproducció per mes i país")
    axs[2].set_xlabel("Mes")
    axs[2].set_ylabel("Taxa de reproducció")
    axs[2].grid(True)
    axs[2].legend()

    # Ajustar el disseny per evitar sobreposicions i afegir espai vertical
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.4)  # Ajustar l'espai vertical entre els gràfics
    plt.show()

if __name__ == '__main__':
    plot_data()