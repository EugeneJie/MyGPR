import random

for i in range(126):

    if i+1<=63:
        while True:
            x1 = random.uniform(0.1,0.16)
            y1 = random.uniform(0.04,0.15)

            x2 = random.uniform(0.16-x1,0.16)
            y2 = random.uniform(0.15-y1,0.15)

            if x2-x1>0.01 and y2-y1>0.01:
                break

        path = 'train/pec/pec%d.in' % i
        with open(path,'w') as f:  
            f.write('#domain: 0.240 0.210 0.002\n')
            f.write('#dx_dy_dz: 0.002 0.002 0.002\n')
            f.write('#time_window: 3e-9\n\n')
            f.write('#material: 6 0 1 0 half_space\n\n')
            f.write('#waveform: ricker 1 1.5e9 my_ricker\n')
            f.write('#hertzian_dipole: z 0.040 0.170 0 my_ricker\n')
            f.write('#rx: 0.080 0.170 0\n')
            f.write('#src_steps: 0.002 0 0\n')
            f.write('#rx_steps: 0.002 0 0\n\n')
            f.write('#box: 0 0 0 0.240 0.170 0.002 half_space\n')
            f.write('#box: %.3f %.3f 0 %.3f %.3f 0.002 pec\n\n' %(x1,y1,x2,y2))
            f.write('#messages: n')

        path = 'train/free_space/free_space%d.in' % i
        with open(path,'w') as f:  
            f.write('#domain: 0.240 0.210 0.002\n')
            f.write('#dx_dy_dz: 0.002 0.002 0.002\n')
            f.write('#time_window: 3e-9\n\n')
            f.write('#material: 6 0 1 0 half_space\n\n')
            f.write('#waveform: ricker 1 1.5e9 my_ricker\n')
            f.write('#hertzian_dipole: z 0.040 0.170 0 my_ricker\n')
            f.write('#rx: 0.080 0.170 0\n')
            f.write('#src_steps: 0.002 0 0\n')
            f.write('#rx_steps: 0.002 0 0\n\n')
            f.write('#box: 0 0 0 0.240 0.170 0.002 half_space\n')
            f.write('#box: %.3f %.3f 0 %.3f %.3f 0.002 free_space\n\n' %(x1,y1,x2,y2))
            f.write('#messages: n')

        path = 'train/coal/coal%d.in' % i
        with open(path,'w') as f:  
            f.write('#domain: 0.240 0.210 0.002\n')
            f.write('#dx_dy_dz: 0.002 0.002 0.002\n')
            f.write('#time_window: 3e-9\n\n')
            f.write('#material: 6 0 1 0 half_space\n')
            f.write('#material: 3.5 0.005 1.0 0.0 coal\n\n')
            f.write('#waveform: ricker 1 1.5e9 my_ricker\n')
            f.write('#hertzian_dipole: z 0.040 0.170 0 my_ricker\n')
            f.write('#rx: 0.080 0.170 0\n')
            f.write('#src_steps: 0.002 0 0\n')
            f.write('#rx_steps: 0.002 0 0\n\n')
            f.write('#box: 0 0 0 0.240 0.170 0.002 half_space\n')
            f.write('#box: %.3f %.3f 0 %.3f %.3f 0.002 coal\n\n' %(x1,y1,x2,y2))
            f.write('#messages: n')


        path = 'train/soil/soil%d.in' % i
        with open(path,'w') as f:  
            f.write('#domain: 0.240 0.210 0.002\n')
            f.write('#dx_dy_dz: 0.002 0.002 0.002\n')
            f.write('#time_window: 3e-9\n\n')
            f.write('#material: 6 0 1 0 half_space\n')
            f.write('#material: 12.0 0.01 1.0 0.0 soil\n\n')
            f.write('#waveform: ricker 1 1.5e9 my_ricker\n')
            f.write('#hertzian_dipole: z 0.040 0.170 0 my_ricker\n')
            f.write('#rx: 0.080 0.170 0\n')
            f.write('#src_steps: 0.002 0 0\n')
            f.write('#rx_steps: 0.002 0 0\n\n')
            f.write('#box: 0 0 0 0.240 0.170 0.002 half_space\n')
            f.write('#box: %.3f %.3f 0 %.3f %.3f 0.002 soil\n\n' %(x1,y1,x2,y2))
            f.write('#messages: n')

    else:

        while True:
            r = random.uniform(0.01,0.03)
            
            x = random.uniform(0.1,0.16)
            y = random.uniform(0.04,0.15)

            if x-r>=0.1 and x+r<=0.16 and y-r>=0.04 and y+r<=0.15:
                break

        path = 'train/pec/pec%d.in' % i
        with open(path,'w') as f:  
            f.write('#domain: 0.240 0.210 0.002\n')
            f.write('#dx_dy_dz: 0.002 0.002 0.002\n')
            f.write('#time_window: 3e-9\n\n')
            f.write('#material: 6 0 1 0 half_space\n\n')
            f.write('#waveform: ricker 1 1.5e9 my_ricker\n')
            f.write('#hertzian_dipole: z 0.040 0.170 0 my_ricker\n')
            f.write('#rx: 0.080 0.170 0\n')
            f.write('#src_steps: 0.002 0 0\n')
            f.write('#rx_steps: 0.002 0 0\n\n')
            f.write('#box: 0 0 0 0.240 0.170 0.002 half_space\n')
            f.write('#cylinder: %.3f %.3f 0 %.3f %.3f 0.002 %.3f pec\n\n'%(x,y,x,y,r))
            f.write('#messages: n')


        path = 'train/free_space/free_space%d.in' % i
        with open(path,'w') as f:  
            f.write('#domain: 0.240 0.210 0.002\n')
            f.write('#dx_dy_dz: 0.002 0.002 0.002\n')
            f.write('#time_window: 3e-9\n\n')
            f.write('#material: 6 0 1 0 half_space\n\n')
            f.write('#waveform: ricker 1 1.5e9 my_ricker\n')
            f.write('#hertzian_dipole: z 0.040 0.170 0 my_ricker\n')
            f.write('#rx: 0.080 0.170 0\n')
            f.write('#src_steps: 0.002 0 0\n')
            f.write('#rx_steps: 0.002 0 0\n\n')
            f.write('#box: 0 0 0 0.240 0.170 0.002 half_space\n')
            f.write('#cylinder: %.3f %.3f 0 %.3f %.3f 0.002 %.3f free_space\n\n'%(x,y,x,y,r))
            f.write('#messages: n')

        path = 'train/coal/coal%d.in' % i
        with open(path,'w') as f:  
            f.write('#domain: 0.240 0.210 0.002\n')
            f.write('#dx_dy_dz: 0.002 0.002 0.002\n')
            f.write('#time_window: 3e-9\n\n')
            f.write('#material: 6 0 1 0 half_space\n')
            f.write('#material: 3.5 0.005 1.0 0.0 coal\n\n')
            f.write('#waveform: ricker 1 1.5e9 my_ricker\n')
            f.write('#hertzian_dipole: z 0.040 0.170 0 my_ricker\n')
            f.write('#rx: 0.080 0.170 0\n')
            f.write('#src_steps: 0.002 0 0\n')
            f.write('#rx_steps: 0.002 0 0\n\n')
            f.write('#box: 0 0 0 0.240 0.170 0.002 half_space\n')
            f.write('#cylinder: %.3f %.3f 0 %.3f %.3f 0.002 %.3f coal\n\n'%(x,y,x,y,r))
            f.write('#messages: n')

        path = 'train/soil/soil%d.in' % i
        with open(path,'w') as f:  
            f.write('#domain: 0.240 0.210 0.002\n')
            f.write('#dx_dy_dz: 0.002 0.002 0.002\n')
            f.write('#time_window: 3e-9\n\n')
            f.write('#material: 6 0 1 0 half_space\n')
            f.write('#material: 12.0 0.01 1.0 0.0 soil\n\n')
            f.write('#waveform: ricker 1 1.5e9 my_ricker\n')
            f.write('#hertzian_dipole: z 0.040 0.170 0 my_ricker\n')
            f.write('#rx: 0.080 0.170 0\n')
            f.write('#src_steps: 0.002 0 0\n')
            f.write('#rx_steps: 0.002 0 0\n\n')
            f.write('#box: 0 0 0 0.240 0.170 0.002 half_space\n')
            f.write('#cylinder: %.3f %.3f 0 %.3f %.3f 0.002 %.3f soil\n\n'%(x,y,x,y,r))
            f.write('#messages: n')
