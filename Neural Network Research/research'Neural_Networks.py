function researchNeuralNetworks() {
  // Define the neural network architecture
  const inputLayerSize = 2;
  const hiddenLayerSize = 3;
  const outputLayerSize = 1;

  // Initialize the neural network weights and biases
  const weights0 = new Matrix(hiddenLayerSize, inputLayerSize);
  const weights1 = new Matrix(outputLayerSize, hiddenLayerSize);
  const biases0 = new Matrix(hiddenLayerSize, 1);
  const biases1 = new Matrix(outputLayerSize, 1);

  // Initialize the input and output data
  const inputData = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
  ];
  const outputData = [
    [0],
    [1],
    [1],
    [0]
  ];

  // Train the neural network using backpropagation
  for (let i = 0; i < 10000; i++) {
    for (let j = 0; j < inputData.length; j++) {
      const input = inputData[j];
      const output = outputData[j];

      // Forward pass
      const layer0 = Matrix.multiply(weights0, input);
      const layer1 = Matrix.add(layer0, biases0);
      const layer2 = Matrix.sigmoid(layer1);
      const layer3 = Matrix.multiply(weights1, layer2);
      const layer4 = Matrix.add(layer3, biases1);
      const prediction = Matrix.sigmoid(layer4);

      // Calculate the error
      const error = Matrix.subtract(output, prediction);

      // Backpropagation
      const delta4 = Matrix.multiply(error, Matrix.sigmoidGradient(prediction));
      const delta3 = Matrix.multiply(Matrix.transpose(weights1), delta4);
      const delta2 = Matrix.multiply(delta3, Matrix.sigmoidGradient(layer2));
      const delta1 = Matrix.multiply(Matrix.transpose(weights0), delta2);

      // Update the weights and biases
      weights0.add(Matrix.multiply(delta1, Matrix.transpose(input)));
      weights1.add(Matrix.multiply(delta4, Matrix.transpose(layer2)));
      biases0.add(delta1);
      biases1.add(delta4);
    }
  }

  // Test the neural network
  for (let i = 0; i < inputData.length; i++) {
    const input = inputData[i];
    const output = outputData[i];

    // Forward pass
    const layer0 = Matrix.multiply(weights0, input);
    const layer1 = Matrix.add(layer0, biases0);
    const layer2 = Matrix.sigmoid(layer1);
    const layer3 = Matrix.multiply(weights1, layer2);
    const layer4 = Matrix.add(layer3, biases1);
    const prediction = Matrix.sigmoid(layer4);

    console.log(`Input: ${input}, Output: ${output}, Prediction: ${prediction}`);
  }
}
