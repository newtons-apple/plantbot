import smbus   # i2c 라이브러리

# 사용할 i2c 채널 번호
I2C_CH = 1
# BH1750 주소
BH1750_DEV_ADDR = 0x23
'''
 측정 모드들
 https://blog.naver.com/chandong83/221602405432
 참고
'''
CONT_H_RES_MODE     = 0x10
CONT_H_RES_MODE2    = 0x11
CONT_L_RES_MODE     = 0x13
ONETIME_H_RES_MODE  = 0x20
ONETIME_H_RES_MODE2 = 0x21
ONETIME_L_RES_MODE  = 0x23

def readIlluminance():
  i2c = smbus.SMBus(I2C_CH)
  luxBytes = i2c.read_i2c_block_data(BH1750_DEV_ADDR, CONT_H_RES_MODE, 2)
  lux = int.from_bytes(luxBytes, byteorder='big')
  i2c.close()
  return lux

'''
 1초에 한번씩 돌면서 조도값 출력
'''
def readIlluminanceThread():
  while True:
    print('{0} lux'.format(readIlluminance()))
    time.sleep(1)

print('starting BH1750')
print('Press Enter key to exit')
readIlluminanceThread()