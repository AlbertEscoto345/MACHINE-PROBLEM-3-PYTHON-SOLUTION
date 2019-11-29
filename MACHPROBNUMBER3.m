format long e;
user_input_matrix = input('Input data in the form [Xi;Yi] (Sample input: [1 2 3 4; 1 2 3 4]) \n');
x=user_input_matrix(1,:)
y=user_input_matrix(2,:)

p1x=polyfit(x,y,1);
Ep1x=y-[(p1x(1)).*x+(p1x(2))];
error_of_p1x=norm(Ep1x);

p2x=polyfit(x,y,2);
Ep2x=y-[(p2x(1)).*(x.^2)+(p2x(2)).*x+(p2x(3))];
error_of_p2x=norm(Ep2x);

p3x=polyfit(x,y,3);
Ep3x=y-[(p3x(1)).*(x.^3)+(p3x(2)).*(x.^2)+(p3x(3)).*x+(p3x(4))];
error_of_p3x=norm(Ep3x);

p4x=polyfit(x,y,4);
Ep4x=y-[(p4x(1)).*(x.^4)+(p4x(2)).*(x.^3)+(p4x(3)).*(x.^2)+(p4x(4)).*x+(p4x(5))];
error_of_p4x=norm(Ep4x);

p5x=polyfit(x,y,5);
Ep5x=y-[(p5x(1)).*(x.^5)+(p5x(2)).*(x.^4)+(p5x(3)).*(x.^3)+(p5x(4)).*(x.^2)+(p5x(5)).*x+(p5x(6))];
error_of_p5x=norm(Ep5x);

p6x=polyfit(x,y,6);
Ep6x=y-[(p6x(1)).*(x.^6)+(p6x(2)).*(x.^5)+(p6x(3)).*(x.^4)+(p6x(4)).*(x.^3)+(p6x(5)).*(x.^2)+(p6x(6)).*x+(p6x(7))];
error_of_p6x=norm(Ep6x);

p7x=polyfit(x,y,7);
Ep7x=y-[(p7x(1)).*(x.^7)+(p7x(2)).*(x.^6)+(p7x(3)).*(x.^5)+(p7x(4)).*(x.^4)+(p7x(5)).*(x.^3)+(p7x(6)).*(x.^2)+(p7x(7)).*x+(p7x(8))];
error_of_p7x=norm(Ep7x);

p8x=polyfit(x,y,8);
Ep8x=y-[(p8x(1)).*(x.^8)+(p8x(2)).*(x.^7)+(p8x(3)).*(x.^6)+(p8x(4)).*(x.^5)+(p8x(5)).*(x.^4)+(p8x(6)).*(x.^3)+(p8x(7)).*(x.^2)+(p8x(8)).*x+(p8x(9))];
error_of_p8x=norm(Ep8x);

p9x=polyfit(x,y,9);
Ep9x=y-[(p9x(1)).*(x.^9)+(p9x(2)).*(x.^8)+(p9x(3)).*(x.^7)+(p9x(4)).*(x.^6)+(p9x(5)).*(x.^5)+(p9x(6)).*(x.^4)+(p9x(7)).*(x.^3)+(p9x(8)).*(x.^2)+(p9x(9)).*x+(p9x(10))];
error_of_p9x=norm(Ep9x);

p10x=polyfit(x,y,10);
Ep10x=y-[(p10x(1)).*(x.^10)+(p10x(2)).*(x.^9)+(p10x(3)).*(x.^8)+(p10x(4)).*(x.^7)+(p10x(5)).*(x.^6)+(p10x(6)).*(x.^5)+(p10x(7)).*(x.^4)+(p10x(8)).*(x.^3)+(p10x(9)).*(x.^2)+(p10x(10)).*x+(p10x(11))];
error_of_p10x=norm(Ep10x);

All_error_vectors=[error_of_p1x error_of_p2x error_of_p3x error_of_p4x error_of_p5x error_of_p6x error_of_p7x error_of_p8x error_of_p9x error_of_p10x];
Sorted_all=sort(All_error_vectors);

format short e;
if Sorted_all(1)==error_of_p10x
    fprintf('The coefficients of the 10th degree polynomial f(x) that would best approximate the data are: \n');
    disp(p10x)
elseif Sorted_all(1)==error_of_p9x
    fprintf('The coefficients of the 9th degree polynomial f(x) that would best approximate the data are: \n');
    disp(p9x)
elseif Sorted_all(1)==error_of_p8x
    fprintf('The coefficients of the 8th degree polynomial f(x) that would best approximate the data are: \n');
    disp(p8x)
elseif Sorted_all(1)==error_of_p7x
    fprintf('The coefficients of the 7th degree polynomial f(x) that would best approximate the data are: \n');
    disp(p7x)
elseif Sorted_all(1)==error_of_p6x
    fprintf('The coefficients of the 6th degree polynomial f(x) that would best approximate the data are: \n');
    disp(p6x)
elseif Sorted_all(1)==error_of_p5x
    fprintf('The coefficients of the 5th degree polynomial f(x) that would best approximate the data are: \n');
    disp(p5x)
elseif Sorted_all(1)==error_of_p4x
    fprintf('The coefficients of the 4th degree polynomial f(x) that would best approximate the data are: \n');
    disp(p4x)
elseif Sorted_all(1)==error_of_p3x
    fprintf('The coefficients of the 3rd degree polynomial f(x) that would best approximate the data are: \n');
    disp(p3x)
elseif Sorted_all(1)==error_of_p2x
    fprintf('The coefficients of the 2nd degree polynomial f(x) that would best approximate the data are: \n');
    disp(p2x)
else
    fprintf('The coefficients of the 1st degree polynomial f(x) that would best approximate the data are: \n');
    disp(p1x)
end
    