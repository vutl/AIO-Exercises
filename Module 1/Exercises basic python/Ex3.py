import math
import random

def calculate_loss(loss_name, sample, loss):
    predict = random.uniform(0,10)
    target = random.uniform(0,10)
    loss = abs(target - predict)
    print(f"loss name : {loss_name}, sample : {sample}, pred : {predict}, target : {target}, loss : {loss}")
    return loss

def compute_MAE(loss_name, num_samples, loss):
    for i in range (num_samples):
        loss += calculate_loss(loss_name, i, loss)
    loss *= (1 / num_samples)
    print(f"final {loss_name} : {loss}")

def compute_MSE(loss_name, num_samples, loss):
    for i in range (num_samples):
        loss += calculate_loss(loss_name, i, loss) ** 2
    loss *= (1 / num_samples)
    print(f"final {loss_name} : {loss}")

def compute_MSE(loss_name, num_samples, loss):
    for i in range (num_samples):
        loss += calculate_loss(loss_name, i, loss) ** 2
    loss = math.sqrt(loss * (1 / num_samples))
    print(f"final {loss_name} : {loss}")


def regression_lost():
    num_samples = input("Input number of samples ( integer number ) which are generated : ")
    
    if (num_samples.isnumeric()):
        num_samples = int(num_samples)
        loss = 0
        loss_name = input("Input loss name : ")
        loss_name = loss_name.upper()

        if (loss_name == "MAE"):
            compute_MAE(loss_name, num_samples, loss)

        elif (loss_name == "MSE"):
            compute_MSE(loss_name, num_samples, loss)

        elif (loss_name == "RMSE"):
            compute_MSE(loss_name, num_samples, loss)

        else:
            print(f"{loss_name} is not supported")

    else:
        print("number of samples must be an integer number")


regression_lost()