pkg load io


clear all;
close all;

n=10000

# data collected via limeSDR 
# head -10000 IQData.csv > ../../802_22_Testing/octave/iq.txt
IQ = csv2cell('iq.txt');

iq_data = []
for i = 1:n
  iq_data(end+1) = IQ{i,1} + IQ{i,2}*I;
endfor

figure
subplot(2,1,1)
plot(1:n,iq_data)
subplot(2,1,2)
plot(1:n,real(iq_data),imag(iq_data))


f = fft(iq_data);

figure
plot(1:n,fftshift(abs(f)))


