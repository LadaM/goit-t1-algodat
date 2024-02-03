import pulp


def main():
    model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)
    juice = pulp.LpVariable("Fruit_Juice", lowBound=0)
    lemonade = pulp.LpVariable("Lemonade", lowBound=0)

    # Resource limitations
    max_water = 100
    max_sugar = 50
    max_lemon_juice = 30
    max_fruit_puree = 40

    # Constraints
    # Since we cannot put the recipe of lemonade and juice production into our objective function directly,
    # we include the formula of lemonade production -- (2*water + 1*sugar + 1*lemon_juice)
    # and juice production -- (2*fruit_puree + 1*water) into our constraints
    # From the formulae of production, we can deduce that since sugar and lemon_juice are used only for lemonade,
    # in proportion 1:1, we will be limited by the smallest of them.
    # Even without running the optimisation solver, we can see that the maximum possible production is limited by
    # the lemon_juice resource, since it's smaller than the sugar resource (30 < 50).
    # => We can produce max 30 units of lemonade.
    # Similar is true for the juice production.
    # => We can produce max 20 units of juice, because we only have 40 units of fruit_puree.
    model += 2 * lemonade + juice <= max_water, "WaterConstraint"
    model += lemonade <= max_sugar, "SugarConstraint"
    model += lemonade <= max_lemon_juice, "LemonJuiceConstraint"
    model += 2 * juice <= max_fruit_puree, "FruitPureeConstraint"

    # Objective function
    model += lemonade + juice, "MaximizeProduction"

    model.solve()
    print(f"Optimal juice production: {juice.varValue} units")
    print(f"Optimal lemonade production: {lemonade.varValue} units")


if __name__ == "__main__":
    main()
