source ofdmflexframesync_debug.m



x_f = flip(x)

n_fft=272
x_fft = fft(x,n_fft)
x_fft = fft(x_f)

figure
plot([0:(4096-1)],abs(fftshift(x_fft)))

figure 1
plot(0:(n-1),real(x_f),0:(n-1),imag(x_f));

figure
subplot(2,1,1);
plot(0:(M-1),real(G0),'+b',0:(M-1),imag(G0),'xr');
subplot(2,1,2);
plot(0:(M-1),real(G1),'+b',0:(M-1),imag(G1),'xr');

subplot(2,1,1);
plot(0:(M-1),real(G0),'+b',0:(M-1),imag(G0),'xr');
subplot(2,1,2);
plot(0:(M-1),real(conj(G0)),'+b',0:(M-1),imag(conj(G0)),'xr');




figure
plot(0:(M-1),fftshift(abs(G0)),'+b',0:(M-1),fftshift(abs(G1)),'xr');


s_hat = 0;
for i = 1:2:M
  j = mod((i+2),M);
  s_hat += G0(j) * conj(G0(i));
  s_hat
endfor
s_hat
s_hat /= 102
s_hat *= 998.99^2
abs(s_hat)


clear all
close all

t = [ 0 : 0.01 : 200];
M = length(t)-1;

po = 0.05;
fo = 0.0;
p1 = 0;
p2 = 0;
f1 = 1;
f2 = 1;

gain = sqrt(8)/(M/2);

y1 = sin(2*pi*t) + f1*sin(2*pi*4.4*t)      + f2*sin(2*pi*4.6*t)         + sin(2*pi*4.8*t)          + sin(2*pi*5.0*t)        + sin(2*pi*5.2*t)        + sin(2*pi*5.4*t)      + sin(2*pi*5.6*t);
#y1 = sin(2*pi*t) + sin(2*pi*10*t);
y1_fft=fft(y1);
y2 = sin(2*pi*(1+fo)*(t+po)) + sin(2*pi*(4.4+fo)*(t+po))      + sin(2*pi*(4.6+fo)*(t+po)+pi*p1) + sin(2*pi*(4.8+fo)*(t+po)-pi*p2)  + sin(2*pi*(5.0+fo)*(t+po))   + sin(2*pi*(5.2+fo)*(t+po)) + sin(2*pi*(5.4+fo)*(t+po)) + sin(2*pi*(5.6+fo)*(t+po));
y2_fft=fft(y2);

figure
subplot(2,1,1)
plot(t,y1,t,y2,'r')
grid on
grid minor on
subplot(2,1,2)
plot((0:M),fftshift(abs(y1_fft)),(0:M),fftshift(abs(y2_fft)),'r')
grid on
grid minor on

y3 = [];

for i = 1:(M+1)
  y3(end+1)=  (y2_fft(i) * conj(y1_fft(i)))*gain;
endfor

y3_sum = 0;
for i = 1:(M+1)
  y3_sum += y3(i);
endfor

figure
plot((0:M),fftshift(y3))
grid on
grid minor on


s_hat = 0;
for i = M/2:M
  j = mod((i+1),M);
  s_hat += y3(j) * conj(y3(i));
  
endfor
s_hat /= 8

thres = abs(s_hat)
dt = arg(s_hat)/(2*pi)










------
pkg load io


clear all;
close all;

n=10000


IQ = csv2cell( '/home/rainer/rpx-100/rpx/iq11.txt');

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


figure
source s0.m;
s_hat = []

for i = 1 : (n-1024)
  f = fft(iq_data(i:(i+1023)));
  cross = fftshift(f).*conj(S0);
  s = 0;
  for i = 4:4:1020
    s = s + (cross(i)*conj(cross(i+4)));
  endfor
  s_hat(end+1) = s;
endfor
  
subplot(2,1,1)
plot(1:n,real(iq_data),imag(iq_data))
subplot(2,1,2)
plot(1:length(s_hat),abs(s_hat),arg(s_hat))

figure
subplot(2,1,1)
plot(1:length(s_hat),abs(s_hat))
grid on
grid minor on
subplot(2,1,2)
plot(1:length(s_hat),((arg(s_hat)/(2*pi))*256))
grid on
grid minor on


s = 4500;
e = 6500;


thresh = [];

for i = 1:e
 thresh(end+1) = 0;
endfor

for i = s:e
  if((abs(s_hat(i)) > 5500) && (abs(s_hat(i)) < 5600) )
    i
    thresh(i) = abs(s_hat(i));
  endif
endfor



figure
subplot(2,1,1)
plot(s:e,abs(s_hat(s:e)),s:e,thresh(s:e))
grid on
grid minor on
subplot(2,1,2)
plot(s:e,-1*((arg(s_hat(s:e))/(2*pi))*256-127),'bx')
grid on
grid minor on

----



