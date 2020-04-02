#include <iostream>
#include <cstdlib>
#include <cmath>
using std::cout, std::string,std::endl;
const long double e=2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274274663919320030599218174135966290435729003342952605956307381 ;


int main(){
    int training_set_inputs[4][3]= {{0,0,1},
                                    {1,1,1},
                                    {1,0,1},
                                    {0,1,1}};
    int training_set_outputs[4][1]={{0},
                                    {1},
                                    {1},
                                    {0}};
    long double synaptic_weights[3][1]= {{-0.16595599},
                                    {0.44064899},
                                    {-0.99977125}};

    srand(1);
        long double output[4][1];
        long double a[4][1];
        for(ulong _=0;_!=100000;++_){
        for(short i=0;i!=4;++i){
            output[i][0]=1/(1+exp(-(training_set_inputs[i][0]*synaptic_weights[0][0]+
            training_set_inputs[i][1]*synaptic_weights[1][0]+
            training_set_inputs[i][2]*synaptic_weights[2][0])));};
        for (short i = 0; i!=4; ++i){
            a[i][0]+=(training_set_outputs[i][0]-output[i][0])*output[i][0]*(1-output[i][0]);};
        for(short i=0;i!=3;++i){
            synaptic_weights[i][0]+=training_set_inputs[0][i]*a[0][0]+
                                    training_set_inputs[1][i]*a[1][0]+
                                    training_set_inputs[2][i]*a[2][0]+
                                    training_set_inputs[3][i]*a[3][0];}
                                    cout<<_<<endl;
        }
        long double answer = 1/(1+exp(-(1*synaptic_weights[0][0]+
                                    1*synaptic_weights[1][0]+
                                    0*synaptic_weights[2][0])));
        cout<<answer<<endl;
}
