const getSomeData = () => {
  try {
    throw new Error("Error occurred");
  } catch (error) {
    console.log(error.message);
  }
};
