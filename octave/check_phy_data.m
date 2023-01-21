pkg load io


clear all;
#close all;


# data collected via limeSDR 
# head -10000 IQData.csv > ../../802_22_Testing/octave/iq.txt
IQ = csv2cell('t.csv');

n = size(IQ)(1)

s_hat_arg = []
s_hat_abs = []
tau_hat = []

for i = 1:n
  s_hat_abs(end+1) = IQ{i,3};
  s_hat_arg(end+1) = IQ{i,4};
  tau_hat(end+1) = IQ{i,5};
endfor

#figure
#subplot(2,1,1)
#plot(1:n,s_hat_abs(1:n))
#subplot(2,1,2)
#plot(1:n,s_hat_arg(1:n))

figure
subplot(2,1,1)
plot(1:n,s_hat_abs)
ylabel('s hat')
xlabel('STS sync hit')
subplot(2,1,2)
plot(1:n,tau_hat)
ylabel('tau prime')
xlabel('STS sync hit')


