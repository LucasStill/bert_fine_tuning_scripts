# coding=utf-8
# test file for drive/io google colab functions

import logging
  
logger = logging.getLogger(__name__)


main():

  print('lets go')


  # Setup logging
      logging.basicConfig(
          format="%(asctime)s - %(levelname)s - %(name)s -   %(message)s",
          datefmt="%m/%d/%Y %H:%M:%S",
          level=logging.INFO if args.local_rank in [-1, 0] else logging.WARN,
      )

  logger.info('hey lets go')
  logger.warning('hey this time')




if __name__ == "__main__":
    main()
