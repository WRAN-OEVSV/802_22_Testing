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


s = 1;
e = length(s_hat);

#t_l = 10700;
#t_h = 11000;

t_l = max(abs(s_hat))-1500;
t_h = t_l+300;

thresh = [];

for i = 1:e
 thresh(end+1) = 0;
endfor

i = s;
frame_start = 0;

while i < e
  if((abs(s_hat(i)) > t_l) && (abs(s_hat(i)) < t_h) )
    i
    # are we on the up slope?
    if(abs(s_hat(i+10)) > abs(s_hat(i)))
       frame_start = round(i - (-1*((arg(s_hat(i))/(2*pi))*256-127)) - 256)
       thresh(i) = abs(s_hat(i));
       thresh(frame_start) = abs(s_hat(i));
       thresh(frame_start+1024) = abs(s_hat(i));
       i += e
    endif
  endif
  i += 1;
endwhile

s=frame_start-1500;
e=frame_start+1024+1500;



figure
subplot(2,1,1)
plot(s:e,abs(s_hat(s:e)),s:e,thresh(s:e))
grid on
grid minor on
subplot(2,1,2)
plot(s:e,-1*((arg(s_hat(s:e))/(2*pi))*256-127),'bx')
grid on
grid minor on



