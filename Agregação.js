[
  {
    $lookup:

      {
        from: "Montadoras",
        localField: "Montadora",
        foreignField: "Montadora",
        as: "Montadoras",
      },
  },
  {
    $unwind:

      {
        path: "$Montadoras",
      },
  },
  {
    $project:

      {
        Carros: 1,
        Cor: 1,
        Montadora: 1,
        Montadoras: 1,
        País: "$Montadoras.País",
      },
  },
  {
    $group:

      {
        _id: "$País",
        Carros: {
          $push: {
            Carro: "$Carros",
            Cor: "$Cor",
            Montadora: "$Montadora",
          },
        },
      },
  },
]