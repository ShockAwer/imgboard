#!/usr/bin/perl
#
# ==== �f�o�b�N�p�p�����[�^�ύX���Ȃ�����
# (�f�o�b�N��3 ,�ʏ��1�ɂ��邱��)
$debug_mode=1;
#
# ==== �f�o�b�N�p�p�����[�^�����܂�
#
#
#     �摜�A�b�v���[�h�f���� �g�уA�N�Z�XCGI(v)
#
#       im.cgi v1.22 (imgboard Rev.6 Base)
#
#	 Copyright(C)1998-2010	1998����!!��y��
#	 Origin Program		to-ru@big.or.jp
#	 Updated by 		imgboard.com�X�^�b�t talk@big.or.jp
#
#		 Support site URL http://imgboard.com
#
# (����)���X�N���v�g��i���[�h�p�̌f����Free�̉摜�A�b�v���[�h�f���A
# imgboard.cgi���^�c����Ă���f���Ǘ��҂₻�̂��F�B�̃��[�U���X���A
# i���[�h������A�R�����g���e�A�{���A�Ǘ����ł���悤�ɍ�����@�\�ǉ��X�N��
# �v�g�ł��Bimgboard.cgi�Ɠ����f�B���N�g���ɓ���Ďg���܂��B���X�N���v�g�P
# �̂ł͓��삵�܂���̂ł����ӂ��������B
#
#  <���ϗ���>-11/10/2014/01
#  2014/11/10 �������̋U�u�����h�i�A�R�s�[���i�n��SPAM�΍������
#  2012/09/06 iOS6�œK��(iPhone�̕W��safari����̃A�b�v���[�h�ɑΉ�)
#  2012/05/01 SPAM�t�B���^�̐ݒ���X�V
#  2012/04/18 (CGI�ݒu����!!)�X�N���v�g�̉��s�R�[�h��CR+LF����LF�ɕύX
#  2012/04/18 (CGI�ݒu����!!)perl�̃p�X��/usr/local/bin/perl����/usr/bin/perl�ɕύX
#  2012/04/18 XSS�i�N���X�X�N���v�e�B���O�j�΍������
#  2012/04/18 �����Z�������N�C��
#  2011/12/15 XSS�i�N���X�X�N���v�e�B���O�j�΍�ŏC��
#  2010/10/05 docomo�t���u���E�U�Ńy�[�W����p�{�^������ʉE�[�ɏ����錻�ۂɑΏ�
#  2010/08/18 �O���t�@�C���A�X�p���P�ꃊ�X�g(spamword.cgi)�̓ǂݍ��݂ɑΉ�
#  2010/05/27 ustream.tv�̃��C�u�����ݍĐ��ɑΉ�
#  2010/04/24 token�̃^�C���A�E�g�G���[���o��s����C��
#  2010/04/09 ���[�h�������j���[�ɂ�����N���X�T�C�g�X�N���v�e�B���O�̉\���ɑ΂��΍������
#  2010/04/05 SoftBank desire�΍������
#  2010/03/31 �����׃T�C�g�pHTML�L���b�V���o�͂�ON�ɂ����SPAM�΍��p�����^�C���g�[�N���ŃG���[���o������C��
#  2010/03/10 SPAM�΍�\�t�g�̃o�O���C��
#  2010/02/17 �g���b�v�@�\(�Ȃ肷�܂��h�~�j���e�X�g����
#  2010/02/15 SPAM�΍�Ƀ��C���^�C���g�[�N���@�\��ǉ�
#  2010/01/23 android�p��CGI�R�[�h��ǉ�
#  2010/01/23 android Ver1.6��USERAGENT���g�тƌ�F����������imode���蕔���C��
#  2009/12/18 �d�q���Ђ�epub�`���ɑΉ�
#  2009/12/18 �L�����̏Z����F�����AGoogleMap�����N������@�\��ǉ�
#  2009/12/18 �f�R���A�Z���^�f�[�^���ւ̑Ή���ǉ�
#  2009/12/18 �����ꌗ�����SPAM�΍������
#  2009/12/18 ���拤�L�T�C�gdailymotion.com�̖����݂ɑΉ�
#  2009/12/08 docomoCHTML7.2�ȍ~(906�`)��Softbank,au�ŐV�@��Ńu���E�U���璼�ړ��e�\��
#  2009/12/08 iphone��imode2.0,Softbank,au�̌��s�@���cookie�L���ɁB���͂��y��
#  2009/12/08 �@�\������:imode2.0��cookie���������ꂽ�Bicookie�@�\��p�~�B
#  2009/12/08 �T�[�r�X�I���ɔ��Ȃ�Ezweb�p��HDML�����A H"�Ή��������폜
#  2008/07/16 youTube��iPod/iPhone�Ō����ꍇ�ɁA�L�����o�Ȃ��o�O���C��
#  2008/06/26 iPod/iPhone�Ō��₷�����邽�߂g�s�l�k���ύX
#  2008/06/25 PSP��youTube����𒼐ڌ�����悤�ɉ���
#  2008/06/24 iPod/iPhone��youTube����𒼐ڌ�����悤�ɉ���
#  2008/06/20 iPod/iPhone�̕����������ۂɑΏ�
#  2008/06/16 iPhone/iPod�̉摜�A�b�v���[�h�p�R�[�h��ǉ�
#  2008/05/28 youTube����̈ꕔ(ID�� _ �����������̓�)���g�тŎ����ł��Ȃ��_���C��
#  2008/04/07 youtube(jp)�̌g�ю���URL�ɑΉ�
#  2007/06/05 ���̂��ꂽ���[���A�h���X�̍��`�F�b�N�@�\��ǉ�
#  2007/05/18 @�ʃ��[���I���ɔ���,�X�N���v�g����
#  2006/12/13 Softbank,au��Flash��������悤�ɂ���
#  2006/10/21 SoftBank�Ή�
#  2006/10/21 youTube�^�O�Ή�
#  2006/03/27 �f����SPAM�΍��ǉ�
#  2005/01/16 au_3G�łP�y�[�W������̋L�����w�肪�������������C��
#  2004/12/12 sage�@�\��ǉ�
#  2003/07/23 PC���猩���Ƃ��ɁA�G����������ƕ�����������_���C������
#  2002/03/14 �當���g�p���ɁAAU�ŃR���p�C���G���[���o��P�[�X���������_���C��
#  2002/03/14 ���p�҂����Ȃ��悤�Ȃ̂ŁA�G�����A�C�R���@�\���폜����
#  2002/03/14 PC����A�N�Z�X�������ɁA�U�������N���o�Ă��Ȃ������_���C��
#  2001/12/08 ���S�̂��߁A�Ǘ��p�X���[�h���ύX���͋L���폜���ł��Ȃ��悤�ɂ���
#  2001/07/31 imgboard_im.cgi����im.cgi�֖��O�ύX�ɔ����A�֘A�����̋L�q�ύX
#  2000/12/10 �E�F�u�o�R�ňꕔ�̐ݒ��ύX�ł���悤�ɂ���
#  2000/09/28 imgboard1.22R5�ȍ~�̃��O�`���ɑΉ�
#  2000/04/05 i���[�h�Ή��ł����V�тō�������A(1)�������򂪑����A�X�N���v�g��
#  ���G�ɂȂ艘���Ȃ���(2)�p�P�b�g�ۋ��Ȃ̂ŃR�����g�A�E�g�����炳�Ȃ��Ƃ�
#  �������������Ȃ��炵��,���󋵂���ʃX�N���v�g�Ƃ��ă����[�X���邱�Ƃɂ����B
#
# <���p�K��>
#  1.(���쌠�ɂ���)
#   1.1��CGI�̒��쌠�y�юg�p�������́Aimgboard.com�i�ȉ� �����j����L���Ă�
#      ��܂��B
#  2.(�g�p����)
#        ����CGI��,�����p�K�肷�ׂĂɏ]���Ă��������ꍇ�Ɍ���,�l,�@�l�ɂ�
#        ����炸,���R�ɃJ�X�^�}�C�Y���A�����ŗ��p���Ă������������ł��܂��B
#        �ЂƂł����ڂ��𖞂����Ȃ��ꍇ��,��{�I�ɁA���̗��p���������܂���B
#        �܂��A���ڂ����ׂĖ��������ꍇ���A���������̎g�p��s�K�����ƔF�߂�
#        �ꍇ,���̎g�p�𒆎~�����Ă��������ꍇ������܂��D���炩���߂�������
#        �������D
#
#  2.1 �g�p��������
#    A.���X�N���v�g�̗��p�K�蕔�A���쌠�\�����A���^�C�g�����̉��ς����Ă��Ȃ�
#      ����
#    B.��������сA�J�X�^�}�C�Y�����X�N���v�g�̖��f�Ĕz�z�����Ȃ����ƁB
#      ���ɁA����A,B�𖞂����Ȃ��ꍇ��,���̗��p����؋֎~���܂��B
#
#  3.(���������ɂ���)
#   3.1 �����A��������킸�A�����ɖ��f�ōĔz�z���邱�Ƃ��ł��֎~���܂��B
#   3.2 ���{�ȊO�̍��Ђ̃��[�U��Ώۂɂ����f���ł̗��p���֎~���܂��B
#   3.3 �����쌠�\���Ȃ�т�,�f�������̒��쌠�\���ƃ����N�����ϋy��,�폜
#       ���邱�Ƃ͌ł��֎~���܂��B
#
#  4.(�񐧌������ɂ���)
#   4.1 �����͌䎩�R�ɂ��Ă��������č\���܂���    �i������3.3�ɒ��ӂ��ĉ������j
#   4.2 ���p���p�͌䎩�R�ɂ��Ă��������č\���܂���i������3.3�ɒ��ӂ��ĉ������j
#   4.3 �l�̗��p�A����і@�l�̗��p�������܂��B�i������3.3�ɒ��ӂ��ĉ������j
#
#  5.(�Ɛӎ���)
#   5.1 �f���̊Ǘ��ӔC��,100%���̌f���̐ݒu�҂ɂ�����̂Ƃ��܂��B���T�C�g��
#       ���̊Ǘ��ӔC����ؕ����܂���B
#   5.2 ���ꂱ��CGI�ɂ�葹�Q��s���v�󂯂��Ƃ��Ă��A�����͈�؂��̐ӔC�𕉂�
#       �`���������܂���D���炩���߂��������������D
#   5.3 ��CGI�ɕs��A�@�\�s���A�o�O�Ȃǂ��������ꍇ���A�����͂��̏C���̋`����
#       ����Ȃ����̂Ƃ��܂��B
#
#  6.(���̑�)
#    �����p�K��͗\���Ȃ����ρA�ǋL�����ꍇ������܂��B���炩���߂��������������D
###############################################################################
# ��{�\���i�����ݒ�͂��̍\����O��ɉ�����܂��j
#
# (���X�N���v�g�͂��Ƃ���imgboard.cgi���^�c����Ă���f���Ǘ��҂₻�̂��F�B
# �̕����Aimode���瓊�e�A�{���A�Ǘ����ł���悤�ɍ�����ǉ��X�N���v�g�ł��B�P
# �̂ł͓��삵�܂���̂ł����ӂ�������)
#
# public_html�i�z�[���y�[�W�f�B���N�g���j
# |
# |-- cgi-bin�i�C�ӂ̃f�B���N�g��705�j
#   |
#   |--img-box(757 �܂��� 707)(�摜�ۑ��p�f�B���N�g���j
#   |
#   |-- jcode_sj.pl  (755 �܂��� 705)(���C�g�ł̓��{�ꃉ�C�u����)
#   |-- imgboard.cgi (755 �܂��� 705)(imgboard�{��)
#   |
#   |-- im.cgi (755 �܂��� 705)(i���[�h����̃A�N�Z�X�p�{��) <===���X�N���v�g
#   |
#   |-- imgsize.pl   (755 �܂��� 705)(�摜�T�C�Y��̓��C�u����)
#   |-- file.dat     (666 �܂��� 606)(�L���f�[�^�ۑ��p)
#   |-- fileback.dat (666 �܂��� 606)(��L�t�@�C���̃o�b�N�A�b�v)
#   |-- icon.dat     (666 �܂��� 606)(WebParts�f�[�^�ۑ��p)
#
# �E( )���͑����i�p�[�~�b�V�����j�ł��B�ŏ��A���ʓ��̍��̐����Ŏ���,
#  �������ǂ����m�F���ĉ������B�m�F���Ƃꂽ��A�R�����̐����̐^�񒆂�0�ɕύX��,
#  ���삷�邩�`�F�b�N���ĉ������B�ǂ���ł����퓮��ł���Ȃ�΁A�ł��邾��
#  �E�̕��̒l���g���Ă��������B
#  (��ʂɃv���o�C�_�ɂ����ẮA�^�񒆂̐�����0�ɂ���ƁA�Z�L�����e�B�I�ɂ��
#  �������Ȃ�A���l����t�@�C������������ꂽ�肷��댯���������Ĉ��S�x���オ��
#  �܂��B���������ɂ�CGI�������Ȃ��Ȃ�v���o�C�_������܂��̂ŁA���̏ꍇ��
#  ���̒l�����g�p���������j
#
#
###############################################################################

#=======================================================================#
#  �����ݒ�
#=======================================================================#

#  �擪��#�̂���s�͓ǂݍ��܂�܂���D

#==================================#
#        <�K�{�ݒ荀��>            #
#==================================#
#
$PM{'admin_passwd'} = '1464';		# �Ǘ��l�ɂ��L���폜���̃p�X���[�h
#					# (�ύX���Ă�������)
#
$PM{'title'} 	= "�摜�f����(�g�їpURL)";	
#  ���u���C�ɓ��� or �u�b�N�}�[�N�v�ۑ����̃^�C�g���ɂȂ�܂��B
#
#  ��<�I�����߂��t�q�k>
#
#  �f���́uHOME�v���������Ƃ��ɁA���L�t�q�k�֖߂�܂��B
#  (URL�����L�f�t�H���gURL����ύX���܂��ƁA�y�[�W�Ƀ����N�������I�ɏo��)
#
$PM{'back_url'} ='http://���Ȃ��̃v���o�C�_/���Ȃ��̃f�B���N�g��/index.html';
#
#  ��<imgboard�{�̖̂��O>
#
#  �p�\�R�����[�U���g�уA�N�Z�X��URL�ɃA�N�Z�X�����ꍇ�A������������o���A
#  �uPC�A�X�}�z�̕��͂�����ցv��imgboard�{�̂�URL���Љ��悤�ɂȂ��Ă��܂��B
#  ����URL����邽�߂ɁAimgboard.cgi�{�̂����L�Ŏw�肵�Ă��������B�Ȃ��{��
#  ��CGI�����f�t�H���g����ύX���ĂȂ��ꍇ�́E�E���ɐݒ�̕K�v�͂���܂���
#
$PM{'cgi_hontai_name'}	= 'imgboard.cgi';	# imgboard�{�̖̂��O
#
#  ��<�T�[�o�ۑ����b�Z�[�W��>	
#    ��imgboard�̃T�[�o�ۑ����b�Z�[�W���̂Q�|�R�{�ɂ��Ă�������
#
#  ���̌����𒴂���ƁA�Â����̂���폜����܂�.�L���Ɖ摜�͓����ɏ����܂��B
#  �f�t�H���g��600�D
#
#
$PM{'max_message'} 		= 600;
#
#  �� <����>	# imgboard�Ɛݒ�����킹�Ă�������
#
#  �C�O�T�C�g�ɐݒu�����ꍇ�A���e���������n�����ɂȂ��Ă��܂��܂��B
#  �������{�����ɏC������ꍇ�ɂ́A�ȉ��̍��ڂŎ�����ݒ肵�Ă��������B
#  (�ݒ��) ������15���Ԃɂ���ꍇ $PM{'gisa'}=15;�Ƃ������ɐݒ肵�Ă��������B
#
$PM{'gisa'}=0;		# ����(h)
#
#  ��<���e�t�@�C���̊i�[�f�B���N�g��>
#
#  �J�����t���̌g�т��瓊�e���ꂽ�t�@�C����ۑ����Ă����ꏊ�ł��B
#  imgboard��$img_dir�Ɛݒ�����킹�ĉ������B
#  �Ȃ��A�悭�킩��Ȃ��ꍇ�̓f�t�H���g�̂܂ܐݒ��ύX���Ȃ���
#  ���̂܂܂ɂ��Ă����Ă��������B
#
$PM{'img_dir'} = './img-box';		# �f�t�H���g�ʒu
#
#  ��<���e�t�@�C���ɕt����URL�O����>
#
#  �A�b�v���[�h�����t�@�C���̓��ɂ���URL�O�������w�肵�Ă��������B
#  (�f���̉摜�t�@�C����URL)=(�����Ŏw�肵��URL�O����)+(�t�@�C����)��
#  �Ȃ�܂��B���Ƃ��΁A�A�b�v���[�h�����t�@�C�����u���E�U�Ō���Ƃ���URL��
#  http://www.big.jp/~talk/imgboard/img-box/img200101281010.jpg�ɂȂ�Ȃ�
#  http://www.big.or.jp/~talk/imgboard/img-box��O�����Ɏw�肵�Ă��������B
#  (�Ȃ��A�Ō��/�͕t���Ȃ��ł�������)
#
$PM{'img_url'} ='http://���Ȃ��̃v���o�C�_/���Ȃ��̃f�B���N�g��/img-box';
#
#  <�f���f�[�^�ۑ��t�@�C����>	# imgboard�Ɛݒ�����킹�Ă�������
#
#  �e�L�X�g�f�[�^�̕ۑ��p�t�@�C���̖��O�ł��D
#  imgboard.cgi�Ɠ����ꏊ�ɓ����ꍇ�͂��̃p�X�w��̂܂�.
$PM{'file'}= './file.dat';
#
#  <���{��R�[�h�ϊ����C�u����>
#
#  imgboard.cgi�Ɠ����ꏊ�ɓ����ꍇ�́A���̃p�X�w��̂܂�.
#  ��:jcode_sj.pl��jcode.pl�̋@�\����X�����łł��BSJIS�ւ̕ϊ��@�\�̂݁B
$PM{'jcode_name'}= 'jcode_sj.pl';
#
#  <�摜�v���p�e�B�F�����C�u����>
#
#  imgboard.cgi�Ɠ����ꏊ�ɓ����ꍇ�͂��̃p�X�w��̂܂�.
$imgsize_prog="imgsize.pl";
#
#  <�f����SPAM�΍�> 2006.03 new
#
#  �f����SPAM�ɂ�鎩����������
#  (0=�������Ȃ�,1=��������i�f�t�H���g�j)
$limit_bbs_spam_flag=1;	
#
#  ���"1"�ɂ����ꍇ�A�B���L�[���[�h�����߂Ă��������B
#  �f����SPAM�͉p�ꌗ�������̂ŁA�ނ�̋��ȓ��{�ꂪ
#  �ǂ��ł��傤�B���{��̏ꍇ�S�����܂łɂ��Ă��������B
#  �Ȃ��A����̕����̓G���[���ł�Ǝv���܂��̂ŁA
#  ���܂������Ȃ��ꍇ�͕�����ύX���Ă��������B
#  �J�^�J�i��NG�ł��B���������B���낢�뎎���Ė��̂Ȃ�
#  �������T���Ă��������B
#
$spam_keyword="�V���厖������";	
#
#  �֎~�P��ɂ��SPAM���� (SPAM_WORD) 2006.05 New
#
#  URL�����N�⃁�[���A�h���X������A���A����̒P���{���Ɋ܂ދL���̂�
#  ���e�����s�����܂��BNG���[�h�w��ł́A�L���łȂ��L����SPAM�Ƃ���
#  ���F������Ď��R�ȉ�b���ł��Ȃ��ꍇ�A��������g���Ă݂Ă��������B
#
#  (1=��������(����),0=�������Ȃ�)
$PM{'no_upload_by_spam_word'}=1;
#
# ���F�擪��#�̂���s�͖����ł��B
#
@SPAM_WORD=(" �Q�������� ", " ���̎q���� ", " �������� ", " �������� "
," ����� ", " �p���_�C�X ", " ������ ", "  ", " �������� "
," ���S���� "," ���E�g "," �t�� "," ������� "," �D�݂̏��� "," �ɔ��� "
," �D�P�_�� "," �f�l���� "," �����o�^�� "," �o�^���� "
," �t�w�� "," �T�C�g���� "," ������ "
# �A�_���g�n
#," �Z�b�N�X "," ���C�� "," ���� "," �Z�t�� ", " �l�C�`�u "
#," ������ "," �G�b�` "," �Q�b�g "," ���w�� "," ���� ", " �����}�� "
#," �Ⴂ���� "," ���� "," �o� "," �l�� "
#," �U�� "," �T�C�g���� "," ���� "," ��� "
#
# �C�O
# �A�_���g�n
#," fuck "," porn "
#," fetish "," pics "," adult "," teen "," stripper "
#
# �u�����h�R�s�[SPAM
," �N�X�ꔄ "," �n�C���v "," copy33 "," brand188 "," �X�[�p�[�R�s�[ "
," louis "," vuitton "," taschen "," fossil  "," ���[���b�N�X "," �����b�N�X "
," cartier "," �J���e�B�G "," �����r���v "," S��  "," N�� "
#," check "," thank "," More "," free "
#," online "," site "," visit "
# ���U�n
," links "," insurance "," cheap "," buy "
," Molto "," cheap "," Airfare "," Furniture "," Ashley "
," Casino "," Foxwoods "," Brighton "," Horseshoe "," Gambling "," Avalon "
," impresionado "," Sunglass "," Ringtones "," Loans "," Cingular "
," Insurance "," Lottery "," Highlander "," Cruise "
," merchand "," stock "," investment "," diabet "
# TODO
," [url= "," [URL= "
," viagra "," hydro "," store "," valium "
," generic "," drug "," prozac "," travel "," agency "
," medication "," Jewelry "," campaign "," advertisement "," Footwear "," C:\\ "
," mortgage "," gym "," mexico "," insurance "
," discount "," escort "," camsex "," livecam "
# Other SPAM
," yumenokuni.net "," pikavip "
," au-au-a.net "," candypop.jp "," yourfilejk.com "
," bagshop2008.com "," yahoo-sale.net "
# �F�{�f���w���n by http://whois.domaintools.com/b-blooming.com
," bigbaito.com "," deli-rakuten.com "
," firstlips.com "," forfun.jp "," hey-sey.com "," nn7.biz "
# ���͍܌n
," internut "," seiryokuzai "," khonsys "
," diet-live "," vigrx "," hirugouhan "," kanpo.com "
," ���͍� "," ���͌��� "," �s���� "," �Z�� "," �����T���v�� "," �������� "
," �֕� "," �È� "," �o�C�A�O�� "," �V�A���X "," �_�C�G�b�g�T�v�� "
," �u�N�s�S "," ���h�X�v���[ "
# Foreign spam word
," serwis "," miejsca "," serwery "," Internecie "
# ������܂ލL�����͂���
," �G "," �� "," �� "," �� "," �� "," ��  "," �M  "," ����  "," ��  "," ��  "
," �͋[�� "," � "," �F "," ���� "," �� "," � "," �� "," ��  "," �  "
," �C "," ���l "," ���� "," ���� "," �� "," �� "," �B "
," �� "," �k "," �� "," � "," ��� "," 墟� "," ���r "
," �� "," �� "," �� "," �� "," �� "," �K "," �D "
," �� "," �� "," �� "," ��"," �o "," �"," �� "," �n "," �� "," �� "
# SPAM���������ւ̃����N���܂ޓ��e��SPAM�Ƃ���
# ���V�A(ru) ����(cn)  �؍�(kr) ���`(hk) ��p(tw)
# �A���[���`��(ar)�A�u���W��(br)�A�C�M���X(uk)
," .ru/ "," .cn/ "," .kr/ "," .fi/ "," .hk/ "," .tw/ "
," .ar/ "," .br/ "," .uk/ "
," �U�P�� "," �s�� "," �����z�z�� "
," �f�l�� "," ����o ");
#
# IP�A�h���X�w��^ SPAM�t�B���^�@�\�̒ǉ��ɂ���(2010.02 )
#
# �h���C�������T�O�ȏ�(���ɂ͂P�O�O�ȏ�j���Ǝ҂������ł����A
# �����N��̎�IP�A�h���X��1�A���邢�͐��ȉ��̌Œ�IP�ł���
# �P�[�X���قƂ�ǂł��B
# �]���āA�h���C���������X�g�ɒǉ����Ĉ��r��������@���A
# �����N��̌Œ�IP�𒲂ׁA�֎~���X�g�ɒǉ����āASPAM��r�����������A
# 50�`100�{�������ǂ��ł��B
# �h���C��������IP�A�h���X�𒲂ׂ�ɂ́A�l�b�g�ɐڑ�������ԂŁA
#  MS-DOS�R�}���h���C���Łuping �z�X�g���v����͂���΁A���ʂƂ��ĕ\������܂��B
# ����IP�A�h���X��@SPAM_HOSTS_IP�ɒǋL���Ă��������B
#
@SPAM_HOSTS_IP=("74.207.24?.","174.122.10?.","66.71.24?.","66.71.25?.","221.231.138.","18.243.22.64"
,"210.173.241.","209.160.32.22?","58.1.229.8?","202.172.28.15?"
,"69.64.147.","203.135.19?.?","205.209.172.135","205.209.174.28","198.143.162.");
#
# 2006.06 URL�����N�񋓌^SPAM�΍�
#
#  SPAM���[�h���Ђ�������Ȃ��Ă��A�{������URL�����N��4�ȏ゠��ꍇ��
#  �������߂Ȃ��悤�ɂ��܂��B
#  (1=��������(����),0=�������Ȃ�)
$PM{'spam_url_link_limit_4'}=1;
#
# 2007.05 �O�������SPAM
#
#  �p��݂̂̓��e�͏������߂Ȃ��悤�ɂ��܂��B
#  �O�������SPAM�h�~�ɗL���ł��B
#  (1=��������(����),0=�������Ȃ�)
$PM{'spam_limit_non_japanese'}=1;
#
# 2007.06 SPAM�炵�����[���A�h���X
#
#  ���[�����̃��[���A�h���X��SPAM�ɑ������̃h���C���̏ꍇ
#  ���e���������߂Ȃ��悤�ɂ��܂��B
#  �O�������SPAM�h�~�ɗL���ł��B
#  (1=��������(����),0=�������Ȃ�)

$PM{'no_upload_by_spam_country_mail'}=1;
#
# SPAM���������ւ̃��[���A�h���X�����̂��铊�e��SPAM�Ɣ��肷��
# ���V�A(ru) ����(cn)  �؍�(kr) ���`(hk) ��p(tw)
# �A���[���`��(ar)�A�u���W��(br)�A�C�M���X(uk)
@SPAM_MAIL_COUNTRY=(".ru",".cn",".kr",".fi"
,".hk",".tw",".ar",".br");
#
#  �ȏ�̗l�X�ȑ΍���w�肵�Ă����ʂ��Ȃ��ꍇ�A
#  �܂��́A���e�p�X���[�h���ɂ��邱�Ƃ��l���Ă��������B
#  SPAM�̓��{�b�g�ŉ������̌f���Ɏ������e���Ă��܂��̂ŁA
#  �p�X���[�h��ސ�����ɂ����ʒu�ɋL�q���Ă����΁A��ǂ����
#  �\���͒Ⴂ�ł��B
#
#  ����ɁA�ȏ�̗l�X�ȑ΍���w�肵�Ă����ʂ��Ȃ��ꍇ�A
#  ������SPAM���Ƃɂ����ⓚ���p�Ŕr���������ꍇ��
#  �ȉ��̃t���O���g���Ă��������B�i�ʏ�͎w�肵�Ȃ����Ɓj
#
#  URL�����N�⃁�[���A�h���X�̂��鏑�����݂��A�ⓚ���p�ł��ׂĔp��
#  (0=�p�����Ȃ��i�f�t�H���g�j,1=�p������)
$filter_bbs_spam=0;
#
#
# ============�ȉ��̓I�v�V�����ł��B�K�v�ɉ����ăJ�X�^�}�C�Y================#
#
#
#================================#
#   <�f���@�\ ��{�I�v�V����>    #
#================================#
#  ��<1�y�[�W�ɕ\�����郁�b�Z�[�W��>
#
#  �f�t�H���g7
#  �P�y�[�W�ɕ\�����郁�b�Z�[�W�̐��ł��B
$PM{'message_per_page'} 		= 7;
#
#  �� <�g�тŕ\������ꍇ�́A�P�L��������̍ő啶����>
#
#  �\������1�L���̒����̍ő�\����������ݒ肵�Ă��������B
#  �g�т���A�N�Z�X�������Ɍ���A���̒����ȏ�̏ꍇ�́A�L���̌㔼��
#  �\����A�J�b�g����ĕ\������܂��B1�y�[�W������̕��������I�[�o����
#  ���悤�ɁA��L�p�����[�^�Ɠ��p�����[�^�œK�X�������Ă�������)
#
$PM{'kiji_disp_limit_imode'}=600;
#
$PM{'kiji_disp_limit_foma'}=3000; # FOMA�ȍ~�̏ꍇ
#
#  ��<�ԐM�@�\>(R6NEW!!)
#
#  �ԐM�@�\���g�����Ƃ��ł��܂��B
#  (1=�ԐM�@�\����(����),0=�ԐM�@�\�Ȃ�)
$PM{'use_rep'} 		= 1;
#
#  �ԐM�̂����L����擪�֎����čs�����ǂ��������߂Ă�������
#  (1=�擪�֎����čs��(�f�t�H���g),0=�����Ă����Ȃ�)
$PM{'res_go_up'} = 1;
#
#  �Â��L���ɕԐM���Ă��擪�֎����Ă����Ȃ��悤��
#  ���[�U�����e���ɑI�Ԃ悤�ɂ��ł��܂��B
#  �i������usage�v�@�\�ł��j
#  (1=sage�L��(�f�t�H���g),0=sage����)
$PM{'use_sage'} = 1;
#
#  �� <���� �S�p�J�i�����p�J�i�ϊ�>
#
#  imode�\�����̉�ʂ͋����A�����ł������̕������\�����ꂽ��������
#  �Ƃ����������悤�Ȃ̂ŁA�����I�ɑS�p�J�i�𔼊p�J�i�ɕϊ����Ă�
#  ��\������@�\��ǉ����܂����B
#
#  1=�ϊ����Ă���\��(����),0=�Ȃɂ����Ȃ�
$PM{'hankaku_filter'}=1;
#
#  �� <PC����̓��e������>
#
#  PC����A�g�уA�N�Z�X�o�R�œ��e����s�ׂ������邩�ǂ�����ݒ肵�Ă��������B
#
#  1=�����Ȃ�(����),0=������(�f���p)
$PM{'no_upload_from_pc'}=0;
#
#  �� <PC����̉{��������> 2002.04 new
#
#  PC����A�g�уA�N�Z�X�o�R�ŉ{������s�ׂ������邩�ǂ�����ݒ肵�Ă��������B
#
#  1=�����Ȃ�,0=������(����)
$PM{'no_view_from_pc'}=0;
#
#  �� <�t�H�[�����͍��ڂ̃f�[�^�L���`�F�b�N>
#
#  �t�H�[���̊e���͍��ڂ̋L���ɂ��āA�K�{�ɂ��邩�ǂ������w��ł��܂��B
#  �K�{�ɂ������͍��ڂ���̏ꍇ�A�L���͓o�^�͂���܂���B
#
#  1=�K�{,0=�ȗ�������
$PM{'form_check_name'}	=1;	# ���O �i�f�t�H���g1�j
$PM{'form_check_email'}	=0;	# email�i�f�t�H���g1�j
$PM{'form_check_subject'}=0;	# �薼 �i�f�t�H���g0�j
$PM{'form_check_body'}	=0;	# �{�� �i�f�t�H���g0�j
#$PM{'form_check_img'}	=0;	# �Y�t�摜�i�f�t�H���g0�j
$PM{'form_check_rmkey'}		=0;	# �폜�L�[�i�f�t�H���g0�j# �����ݖ��g�p
#
#  �ȉ��͓��͍��ڂ𑝂₷�@�\(imgboard�ł�6�܂œ��͍��ڂ𑝂₹�܂�)���g��
#  �āA���ڂ𑝂₵���ꍇ�p (���₵�Ă��Ȃ����[�U�͐ݒ肵�Ă��֌W����܂���)�B
#
$PM{'form_check_optA'}	=0;	# �ǉ�����optA	�i�f�t�H���g0�j# URL
$PM{'form_check_optB'}	=0;	# �ǉ�����optB	�i�f�t�H���g0�j
$PM{'form_check_optC'}	=0;	# �ǉ�����optC	�i�f�t�H���g0�j
$PM{'form_check_optD'}	=0;	# �ǉ�����optD	�i�f�t�H���g0�j
$PM{'form_check_optE'}	=0;	# �ǉ�����optE	�i�f�t�H���g0�j# tel
$PM{'form_check_optF'}	=0;	# �ǉ�����optF	�i�f�t�H���g0�j
#
#================================#
#   <�f���@�\ ��{�I�v�V����>    #
#================================#
#
#  ��<�]�����摜�T�C�Y���>
#
#  Docomo��906i/706i�ȍ~�@��Sofbank3G�@����JPEG�摜,3GP���擙��
#  �A�b�v���[�h����ꍇ�̓]�����~�b�^��ݒ肵�Ă��������B
#
#  �Ȃ��A�Y�t�t�@�C������̌f�����^�c����ꍇ�́A
#  �L���������炵�ăT�[�o�����^���G���A���e�ʃI�[�o�ɂȂ�Ȃ��悤��
#  �C��t���ĉ������B
#  �f�t�H���g6000�j�a
#
#  �T�C�Y����(�摜�ȊO)
#  �f�t�H���g6000�j�a(80000KB�ȏ�ɂ͂��Ȃ����ƁB)
$PM{'max_upload_size'} 	= 6000;	# �P��KB TODO
#
#  �T�C�Y����(�摜)
#  �f�t�H���g500�j�a(���߂��ݕ\�����x���Ȃ�̂�500KB�ȏ�ɂ͂��Ȃ����ƁB)
$PM{'max_upload_img_size'} 	= 500;	# �P��KB
#
#  ��<�e��}���`���f�B�A�f�[�^�i��Q�O��ށj�̃A�b�v���[�h>
#
#  �f�t�H���g�ł�GIF/JPEG/PNG/3GP����/ezmovie/
# �ʃ��[��(JPEG)/WMV/MP4/MP3/WMA/PDF�̓��e���󂯕t���A����ȊO�̃f�[�^�͎������W�F�N�g���܂��B
# ���̑��̊e��}���`���f�B�A�f�[�^
# �i�e�L�X�g,HTML�Ai�����f�B�Ȃǎ��O�o�^���ꂽ��Q�O��ށj�̓��e��
#  ���������ꍇ�͈ȉ��̃t���O��1�ɂ��Ă��������B
#
#  (1=������,0=�����Ȃ�(����))
$PM{'allow_other_multimedia_data'}	= '0';	
#
#  �� <����URL�����N>
#
#  �L������URL,���[���A�h���X�����܂܂��ꍇ�A�����I�Ƀ����N�ɂ��܂��B
#  (1=���������N(����),0=���������N���Ȃ�)
$PM{'auto_url_link'}=1;
#
#
#
#  �� <�V���\��>
#
#  �ŐV���e3�L����------(new)------��Y���ĕ\�����܂�
#  (1=�\������(�f�t�H���g),0=�\�����Ȃ�)
$PM{'disp_new_notice'} = 1;
#
#==================================#
#     <�Z�L�����e�B �I�v�V����>    #
#==================================#
#
#  <����p�X���h>
#
#  �������瓊�e��h�����߁A���e���ɂS�����̐����L�[���`�F�b�N���A
#  ���ꂪ�������ꍇ�����o�^����悤�ɂł��܂��B
#
#  (1=�g�p,0=�g�p���Ȃ�)
$PM{'use_post_password'}=0; #
#
# (��)imode�͑������肷���i���܂������Ȃ����߁A�A�����e�C�^�Y���ɑ΂�
# �đ΍R�����i������܂���B�摜�t���̋L��������Ă��܂����Ԃ�h�����߂�
# ����p�X���h���ł��邾���g�p���Ă��������B
# �g�p���Ȃ��ꍇ��
# �P�D�ۑ��L�����𐔔{�ɑ��₷�B
# �Q�D�o�b����̓��e���֎~����
# �ݒ�ɂ��Ă��������B
#
#  ����p�X���h(4���ȏ�̐���)
$PM{'post_passwd'}="1234";
#
#  <�^�O�g�p����>
#
#  �R�����g���Ƀ^�O�������邩�ǂ������w��ł��܂��B������΃��[�U�\����
#  ���R�x�͏オ��܂����A�^�O�̕ߖY�ꓙ�ɂ��g���u������������\����
#  ����܂��B�Ȃ��A�^�O��������w��ɂ��Ă��A�f���ɑ΂���C�^�Y���\�h�̂���
#  ActiveX,Javascript����A�댯���̂���^�O�A��������ɂ悭�g����^�O
# �i��22��ށj�͎����t�B���^����A����������܂��̂ŁA���炩���߂�����������
#  ���B�i�ڍׂ�sub form_check���Q�Ɓj  
#  �f�t�H���g�̓^�O�g�p�ł��B(1)
#
#  (1=�g�p�\,0=�g�p�s��)
$PM{'use_html_tag_in_comment'}=1;
#
#  <IMG�^�O���E�񋖉�>
#
#  imode�łł͐ݒ肷��K�v����܂���
#  ���̐ݒ�l�͕ύX���Ȃ��ł��������B
#
#  (1=����,0=�񋖉�(��������))
$PM{'use_img_tag_in_comment'}=0;
# 
#  <�e��f���r���΍�> 
#
#  �i���x���P�j�z�X�g���ɂ�鐧�� (BLACK_LIST)
#
#  �g�т̃z�X�g���͓��I�ɕς�邽�߁A���@�\�͊O���܂����B
#
$PM{'no_upload_by_no_RH_user'}=0;	# imode �g�p���͕ύX���Ȃ�����
#
#
#  ���x���Q�j�֎~�P��ɂ�鐧�� (BLACK_WORD)
#
#  ����̒P���{���Ɋ܂ދL���̓��e�����s�����܂��B�O�q�̎�i��p���Ă�"�r��"
#  �� "��`�L���̗�" ���ǂ����Ă����܂�Ȃ��ꍇ�A���邢�́A�z�X�g����p�ɂɕ�
#  ���郆�[�U���炵�����C�^�Y�����󂯂Ă���ꍇ�ɁA�ŏI��i�Ƃ��Ďg���Ă݂�
#  ���������B
#  (1=��������,0=�������Ȃ�(����))
$PM{'no_upload_by_black_word'}=0;	
#
#   �}�b�`�����ꍇ�̃G���[���b�Z�[�W�i�ύX�j
#   �i�r�����ꂽ���Ƃ�����ɂ킩��Ȃ��悤�ɁA�ł��邾���A
#    ���Ӗ��Ȃ��̂ɂ��Ă��������j
$PM{'error_message_to_black_word'}="CGI error code 2244 NBW";	
#
@BLACK_WORD=(" ���˂��� "," ���� "," ���� "
," ���_�� "," ���݈ȉ� "
," �G�� "," ���� "
," �����o�^�� "," ���� "
," porn "," �E���R "
," �U�P�� "," ��炢 "," �s�� "," adult "," teen "," stripper "
," fetish "," pics "," peachs "
," �f�l�� "," �r�f�I�����o ");
#
#  <�A�����e�񐔐���> 
#
#  �C�^�Y����h�����߂ɁA���ꃆ�[�U����̘A�����e�񐔂��f����
#  �Ő����ł��܂��B
#  (1=��������i�f�t�H���g�j,0=�������Ȃ�)
$PM{'limit_upload_times_flag'}=1;	
#  
#  ���"1"�ɂ����ꍇ�A�ǂꂾ���̃T���v�����O���Ԃ̊Ԃɍő剽��܂ŃA�b�v
#  ���[�h�����邩�����߂Ă��������B�i�I�[�o����Ɠ��e�G���[�ɂȂ�܂��j
#
# �T���v�����O���� (day,1hour,10min,2min,1min��I���B�f�t�H���g��2min)
$PM{'upload_limit_type'}="2min";	
# �񐔁B�f�t�H���g��5��
$PM{'upload_limit_times'}="5";
#
#
#  <�g���b�v�@�\�ɂ��A�Ȃ肷�܂��h�~> 2010.02new
#
# ���O#�C�ӂ̃��[�h�Ńg���b�v��\���ł���悤�ɂ��Ă݂܂����B
# ���l�̂Ȃ肷�܂��ŁA�f�����r���ꍇ�́A��������g�����������B
#
#  (1=�g���b�v�@�\���g����悤�ɂ���(����),0=���Ȃ�)
$PM{'use_trip_flag'}=1;	
#
#  <�����o�b�N�A�b�v> 
#
#  ����I�ɋL���������o�b�N�A�b�v����@�\�����܂����B�O��o�b�N�A�b�v�t�@
#  �C�����쐬����������Ԋu���ȏ�󂢂āA�V�K�o�^������ƁA���̃^�C�~���O��
#  �o�b�N�A�b�v�t�@�C�����X�V���܂��B�Ȃ��A�o�b�N�A�b�v�͋L�����T���ȏ゠��
#  �ꍇ�ɂ̂ݓ��삵�܂��B
#
#  ��������o�b�N�A�b�v���g�p#
#  (1=�g�p����i�f�t�H���g�j,0=�g�p���Ȃ�)
$PM{'make_backup_file'}	= '1';
#
#  �o�b�N�A�b�v����Ԋu(��)
$PM{'backup_day_interval'}  = '7';		
#
# �o�b�N�A�b�v�t�@�C����
# (�Z�L�����e�B��̗��R���A���[�U���K�X�ύX���邱�Ƃ𐄏�)
$PM{'backup_file_name'} = 'fileback.dat';
#
#  <�Ǘ��Ҏ������[��> sendmail
#
#  �V�K�L�����o�^�����ƁA���L���[���A�h���X�Ƀ��[���Œʒm���܂��B
#  ���̋@�\���g�p����ꍇ�́A�ȉ��̎O�̏������ׂĊm���Ɏw�肵�Ă��������B
#  �����̏����ԈႦ��ƁA�T�[�o�Ǘ��҂֖��f��������̂ŁA�K���Ǘ��҂Ɋm�F
#  ���Ă���T�d�ɐݒ���s���Ă��������B�Ȃ��A���̋@�\���g����̂̓v���o�C�_
#  ��UNIX�n�̃��[�U�݂̂ł��B(Mac,Win�s�j�ݒ肪�悭�킩��Ȃ��ꍇ�͎g�p��
#  �Ȃ��ł��������B
# 
$PM{'use_email'} =0;	# (1=yes,0=no)�f�t�H���g��0
#
#  ���[���v���O�����̃p�X�i�v���o�C�_�̊Ǘ��҂ɕ����j
$PM{'mail_prog'} = '/usr/lib/sendmail';
#
#  �Ǘ��҂̃��[���A�h���X�i���Ȃ��̃��[���A�h���X�j
#  �����̈���Ƀ��[���𑗂肽���ꍇ�͐VFAQ�y�[�W�Q��
$PM{'recipient'} = 'yourname@your_provider.ne.jp';
#
#  ���[���{���Ɍf���ւ̃V���[�g�J�b�gURL�����N����邽�߁A
#  CGI�̓����Ă���f�B���N�g����URL���w�肵�ĉ�����(�Ō��/�͕s�v)�B
#
$PM{'cgi_link_url'}='http://yourprovider/yourname/imgboard';
#
#  ���[���{���̒����̃��~�b�^�[��ݒ肵�Ă��������B
#
#  (���̒����ȏ�̏ꍇ�́A���e���J�b�g����܂�)
$PM{'mail_body_limit'}=300;
#
#  <������Ƃ��₷��> oyasumi
#
#  ���s�ɏo�����铙�A���΂炭�f�������x�݂���������0�ɂ��Ă��������B
#
$PM{'bbs_open'}=3;          #(1=yes,0=no)�f�t�H���g��3
#
# 0=���S�_�E��
# 1=�Ǘ����j���[�̂ݓ���
# 2=����ɉ{�����\(ReadOnly)
# 3=����ɏ����݂��\(�ǂݏ����\=�ʏ�̃��[�h)
#
#  ���₷�ݎ��̃��b�Z�[�W(�K�X�ύX)
#
$PM{'oyasumi_message'}=qq|
�Ǘ��җ��s���̂��߁A���΂炭���x�݂��܂��B<BR>
�܂��̂��z�������҂����Ă���܂��B
|;
#
#
# ���̑��ϐ��̏�����
$PM{'use_crypt'}	= '1';		# �Í�����p����
$PM{'read_config'}	= '1';		# config��ǂ�
$PM{'flock'}		= '1';		# flock���g��
$PM{'auto_nicovideo_find'}=1;	# nicovideo
$allow_nicovideo_in_res=1;		# �ԐM��nicovideo
#
#=========================================#
#     <�g�s�l�k�ڍאݒ荀�ڃI�v�V����>    #
#=========================================#
#
#==========================#
# �t�H�[�����͕��̃f�U�C��
#==========================#
#
#
# < �K�v/�ȗ��̎����\���̃t�H���g�F�ƃT�C�Y >
#
#  "�t�H�[�����͍��ڂ̃f�[�^�L���`�F�b�N"�ł̐ݒ�ɏ]���A
#  �K�v/�ȗ��̎����\�����A�t�H�[�����̘e�Ɏ����\�����邱�Ƃ��ł��܂�
#
$PM{'auto_disp_omit_frag'}	="1";		# �����\������(yes=1,no=0)
#
#
#  �� <�g�s�l�k����>
#
#  ���[�U�T�C�h�łg�s�l�k��ύX���₷���悤��,�X�N���v�g���̂g�s�l�k��`������
#  �ȉ��ɔ����o���񋓂��Ă���܂��D���ꂼ��,print<<HTML_END;�s�̎��̍s����
#  HTML_END�L���̑O�s�܂ł́A�ʏ�g�s�l�k�Ƃ��ĕҏW�\�Ȃ̂�,���[�h�p�b�g(Win�n)
#  Jedit(Mac�n)���̃G�f�B�^�ł����R�ɏ��������āA�J�X�^�}�C�Y���Ă��������D��
#  �����擪��$�����Ă������($im_body_bgcolor��)�͕ϐ��Ȃ̂ŁA�����ꍇ�͏\����
#  �ӂ��Ă��������D�Ȃ��A���X�N���v�g��SJIS�R�[�h��p���Ă��邽��,�u�\��,�\��,
#  �@�\�v���̓���̕����������Ă��܂����ۂ�����܂��B���̎�̊����╶�����g�p
#  ���ĕ������������������ꍇ�́A�����������������̑O���\�}�[�N�����ċ�؂�
#  ��Ή����ł��܂��B���̏ꍇ�A\��Perl�ł͕�����؂�L���Ƃ��ē����AWeb��ɂ�
#  �\������܂���B
#
#=====================================#
#     <�g�s�l�k--��ʍŏ㕔>          #
#=====================================#
#
#  �g�s�l�k�w�b�_,�{�f�B�w��D�^�C�g������ʍŏ㕔�̂g�s�l�k�ł�
#
#  print<<HTML_END;�̎��s����"HTML_END"�̂���s�܂ł́A�ʏ�̂g�s�l�k
#  �Ƃ��ĕҏW�\�ł��D 
sub top_html{

 	# �����O����(�ύX���Ȃ�����)
	local($mes_p1)="";
	$PM{'title'}="" if(($keitai_flag eq "J-PHONE")&&($jstation_flag < 3));
	$mes_p1=qq|<BR>*PC�A�X�}�z�̕���<a href="$PM{'cgi_hontai_name'}" target=_blank>������</a>��<BR><BR>| if($keitai_flag eq "pc");
	$mes_p1="" if($FORM{'mode'} ne "");

	#�J���[i���[�h�̔���т�h��
	$PM{'im_body_text'}="#000000" if($PM{'im_body_text'} eq "");
	$PM{'im_body_bgcolor'}="#FFFFFF" if($PM{'im_body_bgcolor'} eq "");

 	# ���g�s�l�k��(�J�X�^�}�C�Y�\)
print<<HTML_END;
<HTML>
<HEAD><TITLE>$PM{'title'}</TITLE>$top_html_header</HEAD>
<BODY BGCOLOR="$PM{'im_body_bgcolor'}" BACKGROUND="$PM{'body_background'}" TEXT="$PM{'im_body_text'}" LINK="#6060FF" VLINK="#4040FF">
�摜Upload�f����<BR>
$google_ad01
<CENTER>
(�g�ѱ���) -$ACCESS_COUNTER{total}-<BR>
</CENTER>

$mes_p1

HTML_END
}
#
#=====================================#
#     <�g�s�l�k--��ʍŏ㕔�{�^��>    #
#=====================================#
#
#  ��ʍŏ㕔�̃{�^���ł�
#
#  print<<HTML_END;�̎��s����"HTML_END"�̂���s�܂ł́A�ʏ�̂g�s�l�k
#  �Ƃ��ĕҏW�\�ł��D 
sub top_button_html{

 	# �����O����(�ύX���Ȃ�����)
	# �����ݒ��ύX���ĂȂ��ꍇ�A�I���{�^���͏o���Ȃ��B
	if($PM{'back_url'} eq 'http://���Ȃ��̃v���o�C�_/���Ȃ��̃f�B���N�g��/index.html'){
		$cm_out_exit_h='<!--';
		$cm_out_exit_f='-->';
	}

 	# ���g�s�l�k��(�J�X�^�}�C�Y�\)
print<<HTML_END;
$cm_out_exit_h<a href="$PM{'back_url'}">HOME</a>$cm_out_exit_f
|<a href="$cgi_name?mode=disp_attach_confirm&page=$FORM{'page'}&viewpass=$FORM{'viewpass'}">���e</a>
|<a href="$cgi_name?mode=search_menu&page=$FORM{'page'}&viewpass=$FORM{'viewpass'}">����</a>
|<a href="$cgi_name?mode=disp_admin_menu&page=$FORM{'page'}&viewpass=$FORM{'viewpass'}">�Ǘ�</a>|<BR>
 <a href="$cgi_name?mode=disp_up_help&page=$FORM{'page'}&viewpass=$FORM{'viewpass'}"> *���ӎ���</a><BR>
HTML_END
}
#
#
#=====================================#
#     <�g�s�l�k--��ʒ����̐���>      #
#=====================================#
#
#  �^�񒆂̐��������̂g�s�l�k�ł��D
#
sub middle_A_html{
# �^�O�g�p��̒��ӂ������œ���܂�
print<<HTML_END;
$HR
HTML_END
}

sub middle_B_html{
print<<HTML_END;
<!--�f���������̐�������B-->
<center>
�ő�ۑ�$PM{'max_message'}��<BR>
$KEITAI_ENV{'MACHINE_TYPE'}
</center>
HTML_END
}
#
#=====================================#
#     <�g�s�l�k--���e�L������>        #
#=====================================#
#
#
sub kiji_base_html{

    # �����O����(�ύX���Ȃ�����)
    local($mail_link)="";
    local($tel_link) ="";
    local($keitai_env_link) ="";
    local($tmp_parent_seq_no) ="";
    local($tmp_1,$tmp_2,$tmp_3) ="";
    local($tmpp_1,$tmpp_2,$tmpp_3) ="";
    local($rec_size1,$rec_size2) ="";
    local($resize_link) ="";
    local($tttmp_imgtitle) =""; # 2009.12 ����
    undef %METAP;
    &make_url_link;

    #  ���t�f�[�^��imode�p�ɒZ������
    if($LDATA{'date'}=~ /\[(\d+)\/(\d+)\/(\d+)\,(\d+)\:(\d+)\:(\d+)\]/){
	$LDATA{'date'}="$2\/$3"."_"."$4\:$5";
    }

   #  ���[���A�h���X������ꍇ���������N����

       if(($LDATA{'email'} eq "")||($LDATA{'email'}=~ /no_email/i)||($LDATA{'email'} eq "none")){
	   $mail_link="$LDATA{'name'}";
       }else{
	  # �������[���@�\ 2003.04
	  if($LDATA{'email'}=~ /^tkml\-/){
	   $mail_link="$LDATA{'name'}";
 	  }else{
	   $mail_link="<A HREF=\"mailto:$LDATA{'email'}\">$LDATA{'name'}</A>";
	  }
       }

	if($OPTDATA{'optKeitaiFlag'} ne ""){
#	  $OPTDATA{'optKeitaiServiceCompany'}
#	  $OPTDATA{'optKeitaiHttpVersion'}
#	  $OPTDATA{'optKeitaiMachineType'}
#	  $OPTDATA{'optKeitaiOtherParam'}
#	  $OPTDATA{'optKeitaiMelodyType'}

	  # 2003.12 vodafone�΍�
	   if($OPTDATA{'optKeitaiFlag'}=~ /J\-PHONE/i){
		$OPTDATA{'optKeitaiFlag'}="SoftBank";
	   }

	  # 2009.12 au�΍�
	   if($OPTDATA{'optKeitaiMachineType'}=~ /^au/i){
		$OPTDATA{'optKeitaiFlag'}="au";
	   }

	  $keitai_env_link=qq|<BR>$OPTDATA{'optKeitaiFlag'}�F$OPTDATA{'optKeitaiMachineType'}|;
	}

	# ���[�h�������̎��͂ǂ�̃��X�����������

	if(($FORM{'mode'} eq "search_menu")&&($LDATA{'blood_name'} ne "")){
		$tmp_parent_seq_no=$BLOOD2SEQNO{"$LDATA{'blood_name'}"};
		if($child_kiji_flag == '1' ){	# �q�̏ꍇ
		  $disp_seq_no="$disp_seq_no".")(��$tmp_parent_seq_no�ւ̃��X";
		}else{
		  undef $tmp_parent_seq_no;
		}
	}

	# �^�C�g�����̏���
    if($LDATA{'imgtitle'} !~ /^img(\d+)/){
		$tttmp_imgtitle="$LDATA{'imgtitle'}";
	}

# ���g�s�l�k��(�J�X�^�}�C�Y�\)
print<<HTML_END;
($disp_seq_no)$LDATA{'date'}<BR>
<FONT COLOR="#FF0000">$LDATA{'subject'}</FONT>
($mail_link$tel_link)$tmp_url_link $disp_re<BR>
<BR>
$LDATA{'body'}<BR>
<BR>
HTML_END

    # �Y�t�f�[�^���������ꍇ��print<<HTML_END;����HTML_END�܂ł�HTML���o�͂�
    # ��� 
    if($LDATA{'img_location'} ne ""){
	  if($can_handle_flag == 1 ){	# ������ꍇ�̓����N�\��
       #2009.12.07 iPod/iPhone�Ńt���X�N���[����
	    if(($HTTP_USER_AGENT=~ /iPhone|iPod|iPad|android/i)&&($LDATA{'img_location'}=~ /jpe?g|gif|png|bmp$/i)){
print<<HTML_END;
<a href="$cgi_name?bbsaction=disp_fullscr&timg_location=$LDATA{'img_location'}&timg_w=$IMG_PARAMETERS{'width'}&timg_h=$IMG_PARAMETERS{'height'}&timg_dsize=$IMG_PARAMETERS{'dsize'}&timg_type=#$IMG_PARAMETERS{'type'}">$data_type $tttmp_imgtitle</A>
-$IMG_PARAMETERS{'dsize'}
<BR>
$resize_link
HTML_END

       #2009.12.07 iPod/iPhone/Android�Ńt���X�N���[����
	    }elsif(($au_3G_flag >= 1 )&&($LDATA{'img_location'}=~ /\.3g2$|\.swf$|\.mp4$|\.m4a$/i)){
#TODO
#	    }elsif(($au_3G_flag >= 0 )&&($LDATA{'img_location'}=~ /\.3g2$|\.swf$|\.mp4$|\.m4a$/i)){

&output_au_object_tag_html("$LDATA{'img_location'}","$tttmp_imgtitle");

print<<HTML_END;
<A HREF="$LDATA{'img_location'}">$data_type�F $tttmp_imgtitle
</A>-$IMG_PARAMETERS{'dsize'}
<BR>
$resize_link
HTML_END

	  	}else{
print<<HTML_END;
<A HREF="$LDATA{'img_location'}">$data_type�F $tttmp_imgtitle
</A>-$IMG_PARAMETERS{'dsize'}
<BR>
$resize_link
HTML_END
		}
	}else{				# �����Ȃ����͔̂񃊃��N�\��

print<<HTML_END;
$data_type�F $tttmp_imgtitle-$IMG_PARAMETERS{'dsize'}
HTML_END

	  } #if($can_handle_flag == 1 )
 
	} # $LDATA{'img_location'}������

 print<<HTML_END;
$keitai_env_link
HTML_END
#print "$HR\n";
}
#
#  URL�����N���L������Ă��Ȃ��ꍇ�̓����N��\�����Ȃ��悤�ɂ���
#
sub make_url_link{
 if($OPTDATA{'optA'} ne ""){
	$tmp_url_link=qq|(<a href="$OPTDATA{'optA'}" target=_blank>HP:</a>)<BR>|;
 }else{
	undef $tmp_url_link;
 }
}
#
# http://www.au.kddi.com/ezfactory/tec/spec/wap_tag5.html
# http://www.au.kddi.com/ezfactory/tec/dlcgi/download_1.html
#================================#
# au�p�̃_�E���[�h�����N��HTML�ŏo�� 2010.01 new
#================================# 
sub output_au_object_tag_html{

	local($ttmp_au_img_location)	=$_[0];
	local($ttmp_au_imgtitle)	=$_[1];	

	local($ttmp_au_mime_type)		='video/3gpp2';	
	local($ttmp_au_copyright)		='no';	
	local($ttmp_au_disposition)		='devmpzz';	

	$ttmp_au_copyright='yes';	

	if($ttmp_au_img_location=~ /\.3gp?p$/i){
		$ttmp_au_mime_type		='video/3gpp';
	}elsif($ttmp_au_img_location=~ /\.3gp?p?2$/i){
		$ttmp_au_mime_type		='video/3gpp2';
#		$ttmp_au_mime_type		='audio/3gpp2';
	}elsif($ttmp_au_img_location=~ /\.m4a$/i){
		$ttmp_au_mime_type		='video/3gpp2';
#		$ttmp_au_mime_type		='audio/3gpp2';
	}elsif($ttmp_au_img_location=~ /\.swf$/i){
		$ttmp_au_mime_type	='application/x-shockwave-flash';
		$ttmp_au_disposition	='devfl8r';# ���A�j��Flash
		$ttmp_au_disposition	='devfl7z';# Flash�i����ȊO�j
	}elsif($ttmp_au_img_location=~ /\.mp4$/i){
		$ttmp_au_mime_type		='video/mp4';
	}else{
		return;
	}

	if(-e "$ttmp_au_img_location"){
		@AU_FILE_STAT=stat("$ttmp_au_img_location");
	    $ttmp_au_file_size=$AU_FILE_STAT[7];	# �t�@�C���T�C�Y���擾
	}else{
&error("au�T�C�Y�擾���s $ttmp_au_img_location");
		return;
	}
	
print<<HTML_END;
<object data="$ttmp_au_img_location" type="$ttmp_au_mime_type" copyright="$ttmp_au_copyright" standby="au��pDL�����N">
<param name="disposition" value="$ttmp_au_disposition" valuetype="data" />
<param name="size" value="$ttmp_au_file_size" valuetype="data" />
<param name="title" value="$ttmp_au_imgtitle" valuetype="data" />
</object>
HTML_END
}
#========================================================#
#     <�g�s�l�k--���̓t�H�[����(imode,J�t�H��)>          #
#========================================================#
#
#  �L�����̓t�H�[�����̂g�s�l�k�D���͍��ڂ𑝂₵����A���炵���肵����
#  �ꍇ�͂�����ύX���Ă��������B�������A�ύX�ɂ��b�f�h�����܂�������
#  ���Ȃ�\��������܂��̂�,�����͕ύX���鎞�͏\�����ӂ��Ă��������D
#  �Ȃ��AURL���̍��ڂ�ǉ��������ȂǁA�悭�����]�ɑ΂��ẮA�O���ݒ�
#  �t�@�C���Ƃ����J�X�^�}�C�Y�����ݒ�t�@�C�����g�����Ƃɂ��A���e��
#  �Ɏ����ł��܂��̂ŁA�����ŃJ�X�^�}�C�Y��������A������g���������y
#  �ł��傤�B�Ȃ��A���t�@�C���̓T�|�[�g�T�C�g�̕��Ŕz�z���Ă��܂��B  
#
#
# imode�p�t�H�[�����j���[
sub form_imode_html{

	# ���O����
	&auto_omit_disp;
	$COOKIE{'body'} =~ s/<BR>/\n/g;		#<BR>��LF��
	$COOKIE{'optF'} =~ s/<BR>/\n/g;		#<BR>��LF��
	local($mes_p1) ="";
	local($mes_p2) ="";
	local($mes_p3) ="";
	local($mes_p4) ="";
	local($mes_p5) ="";
	local($mes_p9) ="";
	local($mes_p10) ="";
	local($cm_out_img_h) ="";
	local($cm_out_img_f) ="";
	local($back_page) ="1";

	# 2004.06.20 �g�тŒ����e�L�X�g��łl�������Ă������߁A��������
	local($textarea_maxlength) ="420";

	# TEXTAREA�̓��e�������𒲐�
	if($KEITAI_ENV{'OTHER_PARAM'} eq "FOMA"){
		$textarea_maxlength ="2500";
	# Softbank 2009.12 update	
	}elsif($jstation_flag >= 5){
		$textarea_maxlength ="2500";
	}elsif($keitai_flag eq "pc"){
		# PC����̂�������΍�
		$textarea_maxlength ="430";
	}else{
	  # 2004.06.20 add
	  if(($KEITAI_ENV{'CACHE_SIZE'} >= 20)||($ishot_flag == 1)){
		$textarea_maxlength ="2500";
	  # J-Phone�p�P�b�g�@
	  }elsif(($KEITAI_ENV{'CACHE_SIZE'} >= 12)||($jstation_flag >= 3)){
		$textarea_maxlength ="900";
	  # au 3G�@�΍�
	  }elsif(($KEITAI_ENV{'CACHE_SIZE'} >= 10)||($ishot_flag == 1)||($au_3G_flag >= 1)){
		$textarea_maxlength ="900";
	  }else{
	  }
	}

	# cookie�ɖ{����ۑ��������Ȃ��l�̂��߂ɁA�I�v�V������ǉ�
	$COOKIE{'body'}="";


	# �e������Ƃ��͕ԐM
	if($FORM{'parent'} ne ""){
		if($PM{'use_rep'} == 1 ){
		  $mes_p1 =qq| �L��NO. $FORM{'parent'}�ɕԐM���܂� |;
		  $mes_p4 ="disp_rep_form";
		  $mes_p10 =qq|<INPUT TYPE="checkbox" NAME="sage" VALUE="1">sage<BR>|if($PM{'use_sage'} == 1);
		  $back_page ="$FORM{'page'}";
		}
	# �ԐM����Ȃ���΁A�摜�A�b�v���[�h����
	}else{
	  # 906/706i�ȍ~�̓���E�摜�Q�l�a�A�b�v���[�h�ɑΉ�
	  # iPhone/iPod/android�Ή�
	  if(($http_upload_ok_flag == 1)&&($FORM{'up'} ne "text_only")){
		$mes_p2 =qq|���摜�Y�t<BR><INPUT TYPE="FILE" NAME="img" VALUE="">$DISP_OMIT{'img'}<BR><BR>|;
		$mes_p3 =qq|ENCTYPE="multipart/form-data"|;
	  }
	}


#�ȉ��̍s����"HTML_END"�̂���s�܂ł͒ʏ�̂g�s�l�k�Ƃ��ĕҏW�\�ł��D
print<<HTML_END;
$HR
<center>
[<a href="$cgi_name?mode=disp_member_check&page=$FORM{'page'}&blood=$FORM{'blood'}&parent=$FORM{'parent'}" accesskey=0>�߂�</a>]
</center>

$mes_p1

<FORM ACTION="$cgi_name" METHOD="POST" $mes_p3>	
<INPUT TYPE="HIDDEN" NAME="bbsaction" VALUE="post">
<INPUT TYPE="HIDDEN" NAME="page" VALUE="$back_page">
<INPUT TYPE="HIDDEN" NAME="up" VALUE="$FORM{'up'}">
<INPUT TYPE="hidden" NAME="blood" VALUE="$FORM{'blood'}">
<INPUT TYPE="hidden" NAME="parent" VALUE="$FORM{'parent'}">
<INPUT TYPE="HIDDEN" NAME="prebbsaction" VALUE="$mes_p4">
<INPUT TYPE="HIDDEN" NAME="viewmode" VALUE="$COOKIE{'viewmode'}">
<INPUT TYPE="HIDDEN" NAME="optB" VALUE="">
<INPUT TYPE="HIDDEN" NAME="optC" VALUE="">
$cm_out_pw_h
<INPUT TYPE="hidden" NAME="entrypass" SIZE=4 VALUE="$FORM{'entrypass'}">
$cm_out_pw_f
<INPUT TYPE="hidden" NAME="memberID" VALUE="$FORM{'memberID'}">
<INPUT TYPE="hidden" NAME="rmkey" VALUE="$FORM{'memberID'}">
$POSTADDP
*�͕K�{����<BR>
Ȱ�<BR>
<INPUT TYPE="TEXT" NAME="name" SIZE=15 VALUE="$COOKIE{'name'}" MAXLENGTH="22" istyle="1" MODE=hiragana>$DISP_OMIT{'name'}<BR>
Ұ�<BR>
<INPUT TYPE="TEXT" NAME="email" VALUE="$COOKIE{'email'}" SIZE=15 MAXLENGTH="55" istyle="3" MODE=alphabet>$DISP_OMIT{'email'}<BR>

�薼<BR>
<INPUT TYPE="TEXT" NAME="subject" VALUE="$COOKIE{'subject'}" SIZE=15 MAXLENGTH="20" istyle="1" MODE=hiragana>$DISP_OMIT{'subject'}<BR>


$mes_p2
$mes_p5
�{��$DISP_OMIT{'body'}<BR>
<TEXTAREA NAME="body" COLS="14" ROWS="6" wrap="on" MAXLENGTH="$textarea_maxlength" istyle="1" MODE=hiragana>$COOKIE{'body'}</TEXTAREA>
(URL�͎����I���ݸ����܂�)<BR>

$mes_p10
<INPUT TYPE="SUBMIT" VALUE="���M">
</FORM>

HTML_END
}
#
#=====================================================#
#     <�g�s�l�k--���e���̒���>                        #
#=====================================================#
#
#  �J�X�^�����j���[(���R��`)�p�̂g�s�l�k�ł��D
#
sub output_up_help_HTML{
print<<HTML_END;
<html>
<head>
<title>�g��-����</title>
$top_html_header
</head>
<body bgcolor="PINK">
��__���Ӂ�������<br>
<br>
�� ���쌠���肪������̂̓A�b�v���[�h�i�����\\��\�܂ށj�A����сA�_�E�����[�h���Ȃ��ł������� �B<br>
<br>
�E�f���̂���ɍ��킹���摜�̓��e�����肢�v���܂��B<br>
�E���C���摜�E�����|���m���A�@���ŋ֎~����Ă���摜�̓\\��t���͋֎~�ł��B<br> 
�E�܂��O���摜�Ȃǌ�����ɕs����^����摜���������摦���폜���܂��B<br>
�E��`�̏������݂���؋֎~�ł��B<br>
</body>
</html>
HTML_END
}
#
#=====================================================#
#     <�g�s�l�k--USER��`01(���D���ɃJ�X�^�}�C�Y)>    #
#=====================================================#
#
#  �J�X�^�����j���[(���R��`)�p�̂g�s�l�k�ł��D
#
sub output_user_01_HTML{
print<<HTML_END;
<HTML>
<HEAD>$top_html_header</HEAD>
<BODY BGCOLOR=PINK>
�摜Upload�f����<BR>
<CENTER>
(�g�ѱ���)<BR>
<BR>
<a href="http://xn--t8j6c7d124mi51a.jp">���C�ɓ���.jp</a><BR>
�g�т������߃����N<BR>
by ���C�ɓ���.jp<BR>
</CENTER>
$HR
(����)<BR>
<a href="http://www.google.co.jp/custom">Google</a><BR>
<a href="http://ff2ch.syoboi.jp/"> 2ch���� </a><BR>
<a href="http://xn--t8j734jntm.com"> ���V�C.com </a><BR>
<a href="http://mobile.gnavi.co.jp/"> ����Ȃ� </a><BR>
<a href="http://ktai.st/~toriyama/muryou/"> �������޽���� </a><BR>
<a href="http://www2.kget.jp/mobconduct/"> �̎�GET </a><BR>
<BR>
(�ړ��E�޵��ި�)<BR>
<a href="http://www.jorudan.co.jp/jm/"> �抷�ē� </a><BR>
<a href="http://m.tabelog.com/"> �H�׃��O </a><BR>
<a href="http://www.16t.jp/m//"> �g�є� ������� </a><BR>

<BR>
(�����E������)<BR>
<a href="http://amazon.jp"> amazon��޲� </a><BR>
<a href="http://www.japannetbank.co.jp/service/mobile/index.html"> JNB��s </a><BR>
<a href="http://m.kakaku.com/pc/"> ���i.com PC </a><BR>
<a href="http://xn--1sq65hw3win8a.com"> ���承�i.com(�e�I�N���i��r��)  </a><BR>

(�Э�è)<BR>
<a href="http://m.mixi.jp/"> mixi��޲� </a><BR>
<a href="http://m.youtube.jp/"> YouTube ��޲� </a><BR>
<a href="http://m.cookpad.com"> ����߯�� </a><BR>
<a href="http://yahoo-mbga.jp/"> Yahoo!��޹ް </a><BR>
<a href="http://m.gree.jp/"> GREE </a><BR>
<a href="http://hangame.jp/"> �ݹް� </a><BR>
<a href="http://ip.tosp.co.jp/"> ��\�@\ i </a><BR>
<a href="http://m.ameba.jp/"> �A���[�o </a><BR>
<a href="http://blog.fc2.com/"> FC2�u���O </a><BR>
<a href="http://m.nicovideo.jp"> �j�R�����o�C�� </a><BR>
<a href="http://pr.cgiboy.com/"> �O���v���t </a><BR>
<a href="http://peps.jp/"> @ peps!(�z���y) </a><BR>
<BR>
(��)<BR>
<a href="http://c.2ch.net/"> 2ch </a><BR>
<a href="http://iaozora.net"> �g�� �󕶌� </a><BR>
<a href="http://www.cmoa.jp"> �R�~�b�Ni/�V�[���A </a><BR>
<a href="http://mechacomi.jp"> �߂���R�~ </a><BR>
<a href="http://www.k-manga.jp"> �P�[�^�C�܂񂪉��� </a><BR>
<a href="http://erogamescape.com"> �������Ɏg����G���Q�[��]��� </a><BR>
<a href="http://cinema.intercritique.com/"> CinemaScape�|�f���]��ԁ| </a><BR>
<a href="http://www.sjk.co.jp"> �ʋ΃u���E�U </a><BR>
<BR>
$HR
$accesskey_p1<a href="$cgi_name?page=$FORM{'page'}&viewpass=$FORM{'viewpass'}&mode=disp_admin_menu" accesskey=0>�߂�</a><BR>
$HR

���̃y�[�W�̓����N�t���[�ł�<BR>
</BODY>
</HTML>
HTML_END
}
#
#=====================================================#
#     <�g�s�l�k--USER��`02(���D���ɃJ�X�^�}�C�Y)>    #
#=====================================================#
#
#  �J�X�^�����j���[(���R��`)�p�̂g�s�l�k�ł��D
#
sub output_user_02_HTML{
print<<HTML_END;
<HTML>
<BODY BGCOLOR=PINK>
�摜Upload�f����<BR>
<CENTER>
(�g�ѱ���)<BR>
<BR>
</CENTER>

�����R�ɃJ�X�^�}�C�Y���āA���g����������<BR>
*���[�U��`�f��<BR>

$HR
<BR>

$accesskey_p1<a href="$cgi_name?page=$FORM{'page'}&viewpass=$FORM{'viewpass'}&mode=disp_admin_menu" accesskey=0>�߂�</a><BR>
$HR
</BODY>
</HTML>
HTML_END
}
#
#=====================================================#
#     <�g�s�l�k--USER��`03(���D���ɃJ�X�^�}�C�Y)>    #
#=====================================================#
#
#  �J�X�^�����j���[(���R��`)�p�̂g�s�l�k�ł��D
#
sub output_user_03_HTML{

    	local($mail_link_pc)="";
 
	if($PM{'cgi_url'} eq "http://www.aaa.bbb.com/~myname/im.cgi"){
	   # �f�t�H���g�̂܂܂Ȃ�A�����쐬���ĕ⊮����
	   $PM{'cgi_url'}="http\:\/\/"."$ENV{'SERVER_NAME'}"."$ENV{'SCRIPT_NAME'}";
	}

	if($keitai_flag eq "J-PHONE"){
		$mail_link_pc="<a href=\"mailto:-\@-\" mailbody=\"$PM{'cgi_url'}\">���[��</A><BR><BR>";
	# PC
	}else{
		$mail_link_pc="<A HREF=\"mailto:-\@-?subject=�f���̱��ڽ&body=$PM{'cgi_url'}\">���[��</A><BR><BR>";
	}

print<<HTML_END;
<HTML>
<HEAD>$top_html_header</HEAD>
<BODY BGCOLOR=PINK>
�摜Upload�f����<BR>
<CENTER>
(�g�ѱ���)<BR>
<BR>
�F�B�ɋ�����<BR>
</CENTER>
<BR>
�̱��ڽ�����m<BR>
<BR>
$mail_link_pc

$HR
<BR>

$accesskey_p1<a href="$cgi_name?page=$FORM{'page'}&viewpass=$FORM{'viewpass'}&mode=disp_admin_menu" accesskey=0>�߂�</a><BR>
$HR
</BODY>
</HTML>
HTML_END
}
#
#================================#
#     <�g�s�l�k--����>           #
#================================#
#
#  �t���[��CGI�T�C�g���Ōf�������ւ̃e�L�X�g�L�����`���t�����Ă���
#  �ꍇ�́A������HTML�\�[�X�������Ă��������B�}���|�C���g�͍폜�{�^��
#  �̒���ɂȂ�܂��B(�ŏ��̂����O�I�[�N�V�����̍L���͏����Ȃ�����)
#  �y�[�W���߂����Ă����ƍL����1,2,3�E�E���ɏo�܂��B�Ȃ��Ȃ�Ɛ擪��
#  �L���ɖ߂�O���O�����܂��B���₵�Ă����v�ł��̂ŁA�L���̐���
#  ���₵�����l��4,5.6�ƃo�i�[���䎩�R�ɍ���ĉ������B(��������ڂ�
#  �ύX�s��)
#
# �o�i�[�P�ځi�ύX�s�j
$B_BANNER{'1'}=qq|
<A HREF="http://www.big.or.jp/~talk/welcome/welcome_imr7.cgi">[(�L)NEW!�K���g.���UP�Ή�imgboard2015�̓R�R]</a>
|;

# �o�i�[�Q�ځi�ύX�s�j
$B_BANNER{'2'}=qq|
<A HREF="http://www.big.or.jp/~talk/welcome/welcome_kabu.cgi">[(�L)����-��޳��ފ��I]</a>
|;
#
# �o�i�[�R�ځi���R�ɕύX���Č��\�ł��j
$B_BANNER{'3'}=qq|
|;
#
# �o�i�[�S�ځi���R�ɕύX���Č��\�ł��j
$B_BANNER{'4'}=qq|
|;
#
#
#===================================================#
#     <�g�s�l�k--�摜�t���X�N���[���\����>          #
#===================================================#
# 2008.06 new
#
#  iPod Touch/iPhone/Android�ŉ摜�������Ăяo�����ꍇ�A�������\������Ă��܂����߁A
#  �t���X�N���[���ɏo�����߂ɐV�݂����g�s�l�k���ł��B
#
#  print<<HTML_END;�̎��s����"HTML_END"�̂���s�܂ł́A�ʏ�̂g�s�l�k
#  �Ƃ��ĕҏW�\�ł��D 
sub disp_fullscreen_html{

    local($tmp_title)=$_[0];# ����1�Ƃ��Ď擾
	local($tmpp_img_location)=$_[1];# ����2�Ƃ��Ď擾
	    local($tmpp_img_width)=$_[2];# ����3�Ƃ��Ď擾
		local($tmpp_img_height)=$_[3];# ����4�Ƃ��Ď擾
		local($tmpp_img_dsize)=$_[4];# ����4�Ƃ��Ď擾
		local($tmpp_img_type)=$_[5];# ����4�Ƃ��Ď擾

		    print<<HTML_END;
<HTML lang="ja">
<HEAD><TITLE>imgboard iPod/iPad/iPhone/Android AUTOFIT</TITLE>
$top_html_header
</HEAD>
<BODY BGCOLOR="#444444" TEXT="$PM{'body_text'}">
<img src="$tmpp_img_location"  width="100%" hspace=0 vspace=0 border="1" bordercolor="#FFFFFF"  align="left">
<BR CLEAR="LEFT">
<FORM>
<INPUT TYPE="button" VALUE=" ���ǂ� " onClick="history.back()">
$tmpp_img_type - w $tmpp_img_width/h $tmpp_img_height - $tmpp_img_dsize

</FORM>
<NOSCRIPT>
<a href="$ENV{'HTTP_REFERER'}">���ǂ�</a>
</NOSCRIPT>



</BODY>
</HTML>
HTML_END
}
#
#
#------------�g�s�l�k���������܂�------------#
# cfg_end



    #=================================================================#
    #     �ȏ�Ń��[�U�J�X�^�}�C�Y�����ł��鏉���ݒ�͏I���ł�.     #
    #     �ȉ��̓v���O�����ɂȂ�܂��D                                #
    #=================================================================#




#=======================================================================#
# ���C�����[�`��
#=======================================================================#

&read_config;				# �L������ݒ�����[�h

&init_valiables;			# ������

&check_open;				# �J�X�m�F

&check_browser_type;			# �u���E�U�`�F�b�N

&read_input;				# �t�H�[���̓��e�ƃN�b�L�[��ǂݍ���

if($FORM{'bbsaction'} eq 'post'){		# ���[�h�����e���[�h�̏ꍇ

	&check_entrypass;			# ����`�F�b�N
	&protect_from_BBS_cracker;		# �r���΍�
	&read_cookie;				# �N�b�L�[��Ǎ���
	&limit_upload_times;			# �A�����e�񐔃`�F�b�N
	&make_memberID;				# rmkey&i�N�b�L�[�ԍ쐬
	&post_data;				# ���e����
	&set_cookies;				# �N�b�L�[���Z�b�g
	&send_mail;				# �Ǘ��҂փ��[��	

	# �p�����[�^�N���A�p�g�s�l�k
	&jump_html(" �o�^���� <BR>");
	exit;					# �I��

# 2008.06.26 for ipod/iPad/iPhone/android
}elsif($FORM{'bbsaction'} eq 'disp_fullscr'){# �t���X�N���[���\���̏ꍇ
	&output_Content_type;
    &disp_fullscreen_html($FORM{'timg_location'},$FORM{'timg_location'},$FORM{'timg_w'},$FORM{'timg_h'},$FORM{'timg_dsize'},$FORM{'timg_type'});
	exit;

}elsif($FORM{'bbsaction'} eq 'remove'){	# ���[�h���폜���[�h�̏ꍇ

	if($PM{'admin_passwd'} eq "1684"){
	  &error(" �G���[�B�Ǘ��p�X���[�h���f�t�H���g�̂܂܂ł���A���ݒ�ł��B�Z�L�����e�B�΍�̂��߁A�폜\�@\�\\�͗��p�ł��܂���B�Ǘ��p�X���[�h��ύX���Ă��������B ");
	}

	if($FORM{'passwd'} eq $PM{'admin_passwd'}){
		$remove_mode="admin";		# �폜���[�h
		&remove_data;			# �폜����
		&jump_html(" �폜���� ");	# �p�����[�^�N���A�p�g�s�l�k
		exit;				# �I��
	}elsif(($FORM{'passwd'} eq $PM{'guest_passwd'})&&($PM{'use_guest_passwd'} ==1)){
	        &error(" �G���[�B�Q�X�g�p�X���[�h�@�\��i���[�h����͗��p�ł��܂��� ");
		$remove_mode="guest";		# �폜���[�h
		&remove_data;			# �폜����
		&jump_html(" �폜���� ");	# �p�����[�^�N���A�p�g�s�l�k
		exit;				# �I��
	}elsif($PM{'use_guest_passwd'} =='-1'){
		$remove_mode="rmkey";		# �폜���[�h
		&remove_data;			# �폜����
                &jump_html(" �폜���� ");       # �p�����[�^�N���A�p�g�s�l�k
		exit;				# �I��
	}else{
		&error("�p�X���[�h���Ⴂ�܂��D�폜�𒆎~���܂����D");
	}

}elsif($FORM{'bbsaction'} eq 'change_config'){	# ���[�h���ݒ�ύX���[�h�̏ꍇ

	if($PM{'admin_passwd'} eq "1684"){
	  &error(" �G���[�B�Ǘ��p�X���[�h���f�t�H���g�̂܂܂ł���A���ݒ�ł��B�Z�L�����e�B�΍�̂���Web���j���[�ɂ��ݒ�ύX�ł��܂���B��ɊǗ��p�X���[�h��ύX���Ă��������B ");
	}

	if($FORM{'passwd'} eq $PM{'admin_passwd'}){
		&change_config;			# �ݒ�ύX����
		&jump_html(" �ݒ�ύX���� ");	# �p�����[�^�N���A�p�g�s�l�k
		exit;				# �I��
	}else{
		&error("�p�X���[�h���Ⴂ�܂��D�ݒ�ύX�𒆎~���܂����D");
	}
}elsif($FORM{'bbsaction'} eq 'pf_change'){# ���[�h���v���t�@�C���ύX�̏ꍇ
	&set_cookies;				# �N�b�L�[���Z�b�g
        &jump_html(" �ύX���� ");       	# �p�����[�^�N���A�p�g�s�l�k
	exit;					# �I��

}elsif($FORM{'bbsaction'} eq 'page_change'){# ���[�h���y�[�W�ύX�̏ꍇ
	&read_cookie;				# �N�b�L�[��Ǎ���

}elsif($FORM{'bbsaction'} eq 'disp_form_only'){# �t�H�[���E�B���h�\���̏ꍇ
	&output_Content_type; 
	&top_html;
	&top_button_html;
	&output_form_html;			# ���̓t�H�[����\��
	print "</BODY></HTML>\n";
	exit;
}

# �A�N�V�����������w�肳��Ă��Ȃ����́A�\���ƂȂ�
# �e���[�h�ɂ��\����ʂ̎�ނ𕪊򂳂��ĕ\��������

  if($FORM{'mode'} eq "disp_admin_menu"){
	# �Ǘ����j���[�\��
	&output_Content_type;
	&output_admin_menu_HTML;
	exit;
  }elsif($FORM{'mode'} eq "disp_input_menu"){
	# ���̓t�H�[����\��
	&protect_from_BBS_cracker if($PM{'no_disp_for_cracker'}==1);	# �r���΍�
	&read_cookie;				# �N�b�L�[��Ǎ���
	&check_entrypass;			# ����`�F�b�N
	&output_Content_type; 
	&top_html;
	&output_form_html;	# ���̓t�H�[����\��
	print "</BODY></HTML>\n";
	exit;
# R7new
  }elsif($FORM{'mode'} eq "disp_attach_confirm"){
	# �摜�𓊍e���邩�m�F����B
	&check_upload_from_pc; 
	&output_Content_type;
	&top_html;


	if(($http_upload_ok_flag == 1)||($file_attach_mail == 1)){
		&output_attach_confirm_HTML;
	}elsif($ishot_flag > 0){
		&output_attach_confirm_HTML;
	}else{

	  if($PM{'use_post_password'} == 1 ){ 
		$FORM{'mode'}="disp_member_check";# mode���㏑��
		&output_member_check_HTML;
	  }else{
		&output_attach_confirm_HTML;
	  }

	}
	exit;
  }elsif($FORM{'mode'} eq "disp_mail_form"){
	# ���[���Y�t������ʁBTODO
	&check_upload_from_pc;
if($au_3G_flag >= 1){ 
&error("�i�A�h�o�C�X�jau��3G�g�т̏ꍇ�AEZweb�u���E�U�łȂ��APC�T�C�g�r���[�A�[���g���APC�p�̕��̌f���փA�N�Z�X����Ɖ摜���ȒP�ɃA�b�v���[�h�ł��܂��i2007�t�ȍ~���f���B�������A�A�b�v���[�h�͍ő�80KB�Ȃ̂œ��e�O�ɏk����ƕK�v�j�B�Ȃ��A���[���Y�t�������ƁA���Â��@��ł����e��\�\\�ł����A���̏ꍇ�A���[���Y�t���e�ɑΉ��������V�����f���X�N���v�gimgboard 2010�ȍ~���K�v�ł��D���̃o�[�W����(imgboard R6�n)�ł͓��e�ł��܂���D");
}elsif($HTTP_USER_AGENT =~ /^DoCoMo/i){
&error("���[���Y�t�ɂ��ʐ^���e�@�\\���g�����߂ɂ́A���[���Y�t���e�ɑΉ��������V�����f���X�N���v�gimgboard 2010�ȍ~���K�v�ł��D���̃o�[�W����(R6�n)�ł͓��e�ł��܂���D�i�A�h�o�C�X�j906i/706i�ȍ~�̏ꍇ�A1.1�̓��e���@�����I�т��������B����ȑO��docomo��FOMA�g�т̏ꍇ�A�t���u���E�U���g���Ɖ摜���A�b�v���[�h�ł���ꍇ������܂��B�t���u���E�U�g�тŃA�N�Z�X�������Ă݂Ă������� ");
}else{
&error("���[���Y�t�ɂ��ʐ^���e�@�\\���g�����߂ɂ́A���[���Y�t���e�ɑΉ��������V�����f���X�N���v�gimgboard 2010�ȍ~���K�v�ł��D���̃o�[�W����(R6�n)�ł͓��e�ł��܂���D");
}
	&output_Content_type;
	&top_html;
#	&output_mail_attach_form_HTML;
	exit;
  }elsif($FORM{'mode'} eq "disp_member_check"){
	# �����o�[�m�F�t�H�[����\��
	&check_upload_from_pc; 
	&output_Content_type;
	&top_html;
	&output_member_check_HTML;
	exit;
  }elsif($FORM{'mode'} eq "change_set"){
	# �ݒ�ύX���j���[��\��
	&output_Content_type;
	&output_change_set_HTML;
	exit;
  }elsif($FORM{'mode'} eq "change_set2"){
	# �ݒ�ύX���j���[��\��
	&output_Content_type;
	&output_change_set2_HTML;
	exit;
  }elsif($FORM{'mode'} eq "change_set3"){
	# �ݒ�ύX���j���[��\��
	&output_Content_type;
	&output_change_set3_HTML;
	exit;
  }elsif($FORM{'mode'} eq "change_set4"){
	# �ݒ�ύX���j���[��\��
	&output_Content_type;
	&output_change_set4_HTML;
	exit;
  }elsif($FORM{'mode'} eq "search_menu"){
	# ���[�h�������j���[�\��
	&output_Content_type;

	# 2010.04 ���[�h�������j���[�ɂ�����A
	# �N���X�T�C�g�X�N���v�e�B���O�΍��ǉ�
	&form_check;

	&output_search_menu_HTML;
	if($FORM{'SearchWords'} ne ""){
	    &protect_from_BBS_cracker if($PM{'no_disp_for_cracker'}==1);# �r���΍�
    	    &output_html;			# �f����\��
 	    exit;				# �I��
	}else{
		print " �������[�h����������܂���ł����D���͂��Ă������� \n";
	}
	&output_search_menu_HTML2;
	exit;
  }elsif($FORM{'mode'} eq "show_howto"){
	# �g������\��
	&output_Content_type;
	&output_show_howto_HTML;
	exit;
  }elsif($FORM{'mode'} eq "whats_imgboard"){
	# imgboard�Ƃ�
	&output_Content_type;
	&output_whats_imgboard_HTML;
	exit;
  # 2007.06 �ǉ�
  }elsif($FORM{'mode'} eq "disp_up_help"){
	# upload�̐���
	&output_Content_type;
	&output_up_help_HTML;
	exit;
  }elsif($FORM{'mode'} eq "user_01"){
	# ���R��`�i���D���ɃJ�X�^�}�C�Y���Ă��������j
	&output_Content_type;
	&output_user_01_HTML;
	exit;
  }elsif($FORM{'mode'} eq "user_02"){
	# ���R��`�i���D���ɃJ�X�^�}�C�Y���Ă��������j
	&output_Content_type;
	&output_user_02_HTML;
	exit;
  }elsif($FORM{'mode'} eq "user_03"){
	# ���R��`�i���D���ɃJ�X�^�}�C�Y���Ă��������j
	&output_Content_type;
	&output_user_03_HTML;
	exit;
  }elsif($FORM{'mode'} eq "check_env"){
	# ���`�F�b�N�i�f�o�b�N�p�j
	&output_Content_type;
	&output_check_env_HTML;
	exit;
  }else{
    # ���[�h���w�肳��ĂȂ��ꍇ,�f����\��
    &protect_from_BBS_cracker if($PM{'no_disp_for_cracker'}==1);	# �r���΍�
    &output_Content_type; 
    &top_html;
    &top_button_html;
    &output_html;						# �f����\��
    exit;
  }

#=======================================================================#
# �T�u���[�`��
#=======================================================================#

#======================#
# Content-type�̏o��
#======================#
sub output_Content_type{

    if($au_3G_flag >= 1){
    # 2004.06.13 add au3G�΍�
	print "Cache-Control: no-cache\n";
	print "Content-type: text/html\n\n";
    # 2008.06.20 iPod/iPad/iPhone/android�΍� update 2009.12.07
    }elsif($HTTP_USER_AGENT=~ /iPhone|iPod|iPad|safari/i){
	print "Content-type: text/html; charset=Shift_JIS\n\n";
    }else{
	print "Content-type: text/html\n\n";
    }

}
#
#================#
# ������
#================#

sub init_valiables{

	# �L���f�[�^�t�H�[�}�b�g
	@IM122R6DATA=('subject','name','email','date','body','img_location','imgtitle','seq_no','blood_name','rmkey','unq_id','permit','other');
	$ext_config_ver		="100";
	$real_page_num		="1";	# �^�̃y�[�W��
	$HTTP_USER_AGENT	=$ENV{'HTTP_USER_AGENT'};
	$HTTP_REFERER		=$ENV{'HTTP_REFERER'};
	$HTTP_REFERER 		=~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	$form_method		="POST";
	$HR=qq|<HR>|;
	$ex_h=" �x���F���ł̗L�� ";

	$REMOTE_HOST		=$ENV{'REMOTE_HOST'};
	$SERVER_NAME		=$ENV{'SERVER_NAME'};


	if(int($])<5){
		&error(" �ݒ�G���[�B�X�N���v�g�̂P�s�ڂŃp�X�̎w�肳�ꂽPerl�̃o�[�W���� $] �͌Â����܂��Bimgboard1.22R5�ȍ~�ł�jcode.pl�̃o�[�W�����̊֌W��Perl5�ȏオ�K�v�ł��BPerl5�ȏ�̃p�X��T���Ă���ɕύX���邩�APerl4�ł�����R5\(for Perl4\)��jcode_sj.pl������y���ɂē��肵�Ă��������B ");
	}

	&check_RH;		# Apache1.3.x�΍�
	&check_ISP;		# �v���o�C�_���`�F�b�N���āA�A�h�o�C�X���o��

	$cgi_name=&get_script_name;
	#========= �ȉ��̓}�C�i�[�I�v�V�����ł� ( 0=no,1=yes)==========#

	# �Q�X�g�p�X���[�h�@�\
	# ���e�Ҏ��g���L�����폜�ł���@�\�ł��B�ڍׂ̓T�|�[�g�f�����Q�Ƃ��Ă��������B
	#
	$PM{'use_guest_passwd'}	=0;		# �Q�X�g�p�X���[�h�@�\���g�p
	# �i-1.�폜�L�[�����ɂ���,0.�g�p���Ȃ��A1.�Q�X�g�p�X���[�h���g�p����j
	$PM{'guest_passwd'}		='guest';	# �L���폜���� �Q�X�g�p�X���[�h(�ύX���Ă�������)
	# IP�����S��v���Ȃ��Ă��A�����T�u�l�b�g����̃A�N�Z�X�͓���l���Ƃ݂Ȃ��A�폜��������
	$PM{'gp_allow_subnet'}	=1;

	# ���̑�
	$PM{'no_disp_RH_in_HTML_sorce'}=1;	# HTML�\�[�X�Ƀ����z��\�����Ȃ�
	$PM{'no_disp_for_cracker'}=0;		# BlackList�҂Ɍf���������Ȃ�
	$PM{'force_www_server_os_to'}='';		# ���g�p�p�����[�^(�w�肵�Ȃ�����) 

	# �X�p�����X�g�֘A�̒ǉ��ݒ�
	$use_ext_spamlist	=1;	# �O����spamlist.cgi,spamword.cgi
					# �������,���̃��X�g�����[�h����

	# �O���̐ݒ�t�@�C���̃��[�h(1.21�ȍ~)
	# �J�X�^�}�C�Y����HTML��ݒ肵���p�����[�^�����O�����烍�[�h���܂��B
	# �o�[�W�����A�b�v�ɂ����z����J�X�^�}�C�Y���y�ɂȂ�܂��B

	# �Ȃ��A�J������imgboard�̐ݒ��HTML���A�����W�������O���ݒ�t�@�C����
	# �z�z���\�肵�Ă��܂��̂ŁA�������ʓ|�E�E�E�Ƃ������́A����������p����
	# �����Ǝ�Ԃ��Ȃ��ėǂ��ł��傤�B
	# �i���j�����A�h�ȗ���URL���ڕt��Ver�ɕύX�ł���O���ݒ�t�@�C��

	$PM{'load_ext_config'}	=0;		# �O���ݒ�t�@�C�����g��(1=yes,0=no)
	$PM{'ext_config_name'}	="set_imode01.cgi";	# �ݒ�t�@�C�����i�g���q�͕K�� cgi�Ɂj

	# �O���ݒ�t�@�C���ɏ������p�����[�^�͏㏑������܂��B

#------------------ �ȉ��̓v���O���� -----------------------------	
	undef $call_from_imgboard_flag;
	$call_from_imgboard_flag=1;

	require "$imgsize_prog" if(-e "$imgsize_prog");

	if(($PM{'load_ext_config'} == 1)&&(-e "$PM{'ext_config_name'}")){
		require "$PM{'ext_config_name'}";
	}

&make_uniq_onetime_id;

#======================#
# SPAM�΍��p�g�[�N��
#======================#
# 2010.02 SPAM�΍�̂��߁A�f���ŗL�̃����^�C��ID���쐬����
# 2010.04 softbank�̃X�}�[�g�t�H���΍�Ń��W�b�N�ύX

sub make_uniq_onetime_id{

	local($ttmp_uniq_char)="";

	# perl5��Digest��SHA256���W���[�����g���Ȃ��v���o�C�_�������̂ŁA
	# �Ǝ����W�b�N�ŗސ����ɂ���HASH��p�v�Z�����邱�Ƃɂ���

	if(-e "$PM{'img_dir'}/index.html"){ # 2010.04imgboard�{�̂ƕϐ������Ⴄ�̂��C��
	 @UNQ_FILE_STAT=stat("$PM{'img_dir'}/index.html");	# �����𒲍�
	 $tttmp_pick_file_size		=substr($UNQ_FILE_STAT[7],-1,1);		# �t�@�C���T�C�Y���擾
	 $tttmp_pick_file_lastupdate=substr($UNQ_FILE_STAT[9],-1,1);
	}else{
	 $tttmp_pick_file_size		=3;
	 $tttmp_pick_file_lastupdate=4;
	}

	$tmp_token_time= substr(time,-7,2); #27.7���ԒP��

	$tmp_alphabet_sn	="$ENV{'SCRIPT_FILENAME'}";
	$tmp_alphabet_sn	=~ s/[^a-zA-Z0-9]//g;

	$tmp_alphabet_sa	="$ENV{'SERVER_ADMIN'}";
	$tmp_alphabet_sa	=~ s/[^a-zA-Z0-9]//g;

	$tmp_alphabet_saddr ="$ENV{'SERVER_ADDR'}";
	$tmp_alphabet_saddr =~ s/[^a-zA-Z0-9]//g;
	
#$admin_passwd = 'biko';	

	# HTC disire�΍�Ń��W�b�N�ύX(�P�����������Ă���)
	$tttmp_pick_sa_base=substr($tmp_alphabet_saddr,-3,1)."$tttmp_pick_file_lastupdate".substr($admin_passwd,-1,1).substr($tmp_alphabet_sn,5,1).substr($tmp_alphabet_sa,5,1)."$tttmp_pick_file_lastupdate"."$tttmp_pick_file_lastupdate";

#&error("$tttmp_pick_sa_base  $tmp_alphabet_sn $tmp_alphabet_sa s $tttmp_pick_file_lastupdate");

	$tttmp_salt="$tttmp_pick_file_lastupdate"."$admin_passwd";# salt�쐬
	$tttmp_pick_sa		=  substr(time,-7,2)."$tttmp_pick_sa_base";
	$tttmp_pick_sa_old	= (substr(time,-7,2)-1)."$tttmp_pick_sa_base";

# token����m�Ftest�p(100�b�P�ʂŖ�����)
#	$tttmp_pick_sa		=  substr(time,-4,2)."$tttmp_pick_sa_base";
#	$tttmp_pick_sa_old	= (substr(time,-4,2)-1)."$tttmp_pick_sa_base";

	
	$uniq_token		=crypt($tttmp_pick_sa		,$tttmp_pick_sa);# HASH��p������쐬
	$uniq_token_old	=crypt($tttmp_pick_sa_old	,$tttmp_pick_sa_old);# HASH��p������쐬 27.7���ԒP�ʂň�O

	# salt��؂藎�Ƃ�
	$uniq_token		=substr($uniq_token,2,11);
	$uniq_token_old	=substr($uniq_token_old,2,11);

	# URL�Ƒ����̈�������������
	$uniq_token 	=~ s/[^a-zA-Z0-9]//g;
	$uniq_token_old =~ s/[^a-zA-Z0-9]//g;

#&error("$uniq_token");	
#	$ttmp_uniq_char="$uniq_token - $uniq_token_old - salt $tttmp_salt - sa $tttmp_pick_sa - saold $tttmp_pick_sa_old - $ENV{'SERVER_ADDR'} "."$ENV{'REMOTE_ADDR'} "."$ENV{'SERVER_ADMIN'}"." $tttmp_pick_file_size $tttmp_pick_file_lastupdate";
#&error("ttmp_uniq_char $ttmp_uniq_char");

}

	# 2006.03 SPAM�΍�
	if($spam_keyword ne ""){
		$POSTADDP="$POSTADDP\n"."<INPUT TYPE=\"HIDDEN\" NAME=\"sf\" VALUE=\"$spam_keyword\">\n<INPUT TYPE=\"HIDDEN\" NAME=\"onetime_token\" VALUE=\"$uniq_token\">";
	}

	if(($PM{'jcode_name'} ne '')&&(-e "$PM{'jcode_name'}")){
	    require "$PM{'jcode_name'}";
	}else{
	    &error(" CGI�ݒ�G���[���o�I<BR>���{�ꃉ�C�u����$PM{'jcode_name'}���w�肳�ꂽ�ꏊ�Ɍ�����܂���ł����B�p�X�̐ݒ���������ĉ����� ");
	}
}

#================#
# �J�X�m�F
#================#

sub check_open{

    if($PM{'bbs_open'} ==0){
	&error("$PM{'oyasumi_message'}");
    }

}

#=====================#
# ���̓f�[�^��ǂ�
#=====================#
# 2000.12
# �g�ѐ�p���x�[�X��J-PHONE����摜�A�b�v���[�h�ɑΉ�����������
# PC/Mac����̃A�b�v���[�h�֘A�̃R�[�h�͍폜���Ă���܂��B
#
sub read_input{

	# ���ϐ��̏�����
	local($name);
	undef $img_data_exists;
	undef @NEWFNAMES;
	undef $jcode_eval_check_flag;

	# ���f�[�^�̎擾���]���f�[�^�̃T�C�Y���`�F�b�N
   	$ENV{'REQUEST_METHOD'} =~ tr/a-z/A-Z/;
#TODO
#	if($PM{'max_upload_size'} > 2200){$PM{'max_upload_size'}='2200';}# �ύX�֎~
	if($PM{'max_upload_size'} > 110000){$PM{'max_upload_size'}='110000';}# �ύX�֎~
	$max_content_length	=($PM{'max_upload_size'} + 1)*1000;
	$max_content_limit	="$PM{'max_upload_size'}";

	if($ENV{'REQUEST_METHOD'} eq "POST"){

		# OS�̎�ʂ𔻕�
		$www_server_os =&check_www_server_os;

		if($www_server_os=~ /win/i){
			binmode(STDIN);
		}

		if($ENV{'CONTENT_LENGTH'} > 210000000){
			&error(" �f\�[�^�e�ʂ��傫�����܂��B�摜�⓮��̃T�C�Y��$max_content_limit KB�ȉ��ɂ��Ă���A���e���Ă��������B�Ȃ��A�ʃ��̏ꍇ�A�B�e�掿��FINE����m\�[�}���ɕύX���čĎB�e����Ƒ啝�ɃT�C�Y���������Ȃ�܂��B����̏ꍇ�́A�B�e���Ԃ�Z������ƃT�C�Y���������Ȃ�܂��Becode=pre ");
			exit;
		}

		# 2000/02/02 �ύX
		read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});

		if($ENV{'CONTENT_LENGTH'} > $max_content_length){
			&error(" �f\�[�^�e�ʂ��傫�����܂��B�摜�⓮��̃T�C�Y��$max_content_limit KB�ȉ��ɂ��Ă���A���e���Ă��������B�Ȃ��A�ʃ��̏ꍇ�A�B�e�掿��FINE����m\�[�}���ɕύX���čĎB�e����Ƒ啝�ɃT�C�Y���������Ȃ�܂��B����̏ꍇ�́A�B�e���Ԃ�Z������ƃT�C�Y���������Ȃ�܂��Becode=after ");
			exit;
		}

	}elsif($ENV{'REQUEST_METHOD'} eq 'GET'){
		$buffer = $ENV{'QUERY_STRING'};

		# XSS�΍� 2012.04.18
		# onClick��javascript�C�x���g������(�N���X�T�C�g�X�N���v�e�B���O�΍�)		
		$buffer =~ s/(onClick|onblur|onchange|onmouse|onError|onload|onfocus|onselect|onsubmit|onunload|onreset|onabort|ondblclick|onkey|ondragdrop)(\w{0,8})(\s*)(\=|%3d)/RemovebyImgboardSecurityCheck_JS/ig;
		$buffer =~ s/(<|%3C)/RemovebyImgboardSecurityCheck_3C/ig;
		$buffer =~ s/(>|%3E)/RemovebyImgboardSecurityCheck_3E/ig;

	}else{
		return 0; 
	}

	# ���t�@�C�����Ɏg���A���t�֘A�̃p�����[�^�����

	# �p�����[�^���`�F�b�N
	if(($PM{'gisa'}=~ /^(\d+)$/)&&($PM{'gisa'} != 0)){
		$PM{'gisa'}=$PM{'gisa'};
	}else{
		$PM{'gisa'}=0;
	}

	($sec,$min,$hour,$mday,$mon,$year,$wday,$yday) = localtime(time + $PM{'gisa'}*60*60);

	$year += 1900;				# 2000�N�΍�

	$month = $mon + 1;
	if ($month < 10) { $month = "0$month"; }
	if ($mday  < 10) { $mday  = "0$mday";  }
	if ($sec   < 10) { $sec =  "0$sec";    }
	if ($min   < 10) { $min =  "0$min";    }
	if ($hour  < 10) { $hour = "0$hour";   }
	if ($yday  < 400){ $yyday= 385+"$yday";}
	$unq_id="$year"."$month"."$mday"."$hour"."$min"."$sec";

	# -----��������-------------------------------------------------------

	# ���ȉ��t�H�[���̃f�R�[�h����


	# ���}���`�p�[�g����Ȃ����̃t�H�[������
	# (�ʏ�͂���ł�)

	if($ENV{'CONTENT_TYPE'} !~ /multipart\/form-data/){

	   @pairs = split(/&/,$buffer);

	   foreach $pair(@pairs){
	     ($name,$value) = split(/=/,$pair);
	     $value =~ tr/+/ /;
	     $value =~ s/%([0-9a-fA-F][0-9a-fA-F])/pack("C", hex($1))/ego;
	     # sjis�ɕϊ� (imgboard1.22 Rev.3)
	     # jcode_sj.pl�֘A�̐ݒ�~�X���g���b�v���Č��o
	     # (��x��������΃X�L�b�v���č�����)
	     if($jcode_eval_check_flag != '1'){
	       eval "&jcode'convert(*value, 'sjis','sjis','z');";
	       if($@ eq ""){
	 	 $jcode_eval_check_flag=1;
		 # ����
	       }else{
		 # ���s
		 #&error(" CGI�ݒ�G���[ ���炩�̗��R�œ��{�ꃉ�C�u�����u $PM{'jcode_name'} �v�̓ǂݍ��݂Ɏ��s���܂����B<BR> jcode_sj.pl���̖��O���������w�肳��Ă��Ȃ����A���邢�͎w��p�X�u $PM{'jcode_name'} �v�ɊY���t�@�C�������݂��Ȃ����A���邢�̓p�[�~�b�V�������������Ȃ����̂Ǝv���܂� ");
	       }
	     }else{
		&jcode'convert(*value, 'sjis','sjis','z');
	     }

    	# 2011.12.15 XSS�΍�
		$value =~ s/(%3C|<)(\s*)script//ig;		# script�^�O�֎~
		$value =~ s/(%3C|<)(\s*)EMBED//ig;		# EMBED�^�O�֎~
		$value =~ s/(%3C|<)(\s*)OBJECT//ig;		# OBJECT�^�O�֎~
		$value =~ s/(%3C|<)(\s*)iframe//ig;		# SCRIPT�^�O�֎~

		$value =~ s/(%3C|<)(\s*)/&lt;/ig;		# �^�O�֎~
		$value =~ s/(%3E|>)(\s*)/&gt;/ig;		# �^�O�֎~

	     $FORM{$name} = $value;
    	   }# end of foreach

	}else{
	# ���}���`�p�[�g���̃t�H�[������
	# (J-PHONE�̃p�P�b�g�@�A�h�R����i�V���b�g�T�[�r�X�@�ȍ~)

#	  &error(" $cgi_name ��imode��p�ł���A����o�R�ł̉摜�f�[�^�̃A�b�v���[�h�͂ł��܂���B�摜�A�b�v���[�h�@�\���g�����߂ɂ̓p�\�R���ŃA�N�Z�X���A<a href=\"$PM{'cgi_hontai_name'}\">imgboard.cgi</a>�{�̂ɃA�N�Z�X���ăA�b�v���Ă������� ");

	  # ���Z�L�����e�B�`�F�b�N	
	  # ��METHOD�̃`�F�b�N	
	  &error(" multipart\/form-data���g���Ƃ��� METHOD��POST�ɂ��Ă��������B ") if($ENV{'REQUEST_METHOD'} ne "POST");


	  # ���g�шȊO�̉摜���e�����W�F�N�g����
	  if($keitai_flag eq "J-PHONE"){
		if($jstation_flag >= 4){
		  # J-SKY�p�P�b�g�@ �Ή�
		}else{
		  &error(" SoftBank(J-PHONE)�ŁA�摜�𒼐ڱ���۰�ނł���̂́A51�ذ�ވȍ~�̃p�P�b�g�Ή��@\�ł��B����ȊO�̋@\��łͱ���۰�ނł��܂��� ");
		}
	  }elsif($keitai_flag eq "imode"){
		if($http_upload_ok_flag == 1){
		  # 906/706i�ȍ~�̓���E�摜2MB�A�b�v���[�h�@
		}else{
		  &error(" �h�R���ŁA�摜�𒼐ڱ���۰�ނł���̂́A906/706i�ذ�ވȍ~�̓���E�摜2MB�A�b�v���[�h�Ή��@\�ł��B����ȊO�̋@\��łͱ���۰�ނł��܂��� ");
		}
	  }elsif($keitai_flag eq "pc"){
		if(($KEITAI_ENV{'MACHINE_TYPE'} eq "iPod")||($KEITAI_ENV{'MACHINE_TYPE'} eq "iPad")||($KEITAI_ENV{'MACHINE_TYPE'} eq "iPhone")||($HTTP_USER_AGENT=~ /android/i)){
		  # iPhone/iPod/Android�͋���
		}else{
#TODO		&error(" PC����́A�摜���A�b�v���[�h���󂯕t���܂���B ");
		}
	  }else{
		&error(" ���̌g�т���́A�摜���A�b�v���[�h���󂯕t���܂���B ");
	  }

	  # ��multipart/form-data�̏ꍇ�̏����J�n
	  $buffer =~ /^(.+)\r\n/;
	  $boundary = $1;
	  @pairs = split(/$boundary/, $buffer);

	  foreach $pair(@pairs){
		$check_count++;
		$pair=~ s/\r\n$/\r\nD_End/;
		@vars = split(/\r\n/, $pair);
		$vars = @vars;

	  	#---�T�|�[�g�p----#
		if(($check_count=='7')&&($FORM{'email'} eq "mt1")){&error(" �f�o�b�N���[�hall-$vars,vars0- $vars[0]<BR>,1-$vars[1]<BR>\n,2-$vars[2]<BR>\n,3-$vars[3]<BR>\n,4-$vars[4]<BR>\n,5-$vars[5]<BR>\n,6-$vars[6]\n<BR>,7-$vars[7]\n.<BR>,Perl ver $] <BR>@vars test ");}
		#-----------------#

		# ���A�b�v���[�h�t�@�C�������Ă���ꍇ

		if(($vars > 4)&&($vars[1] =~ /name\=\"(.+)\"\;\sfilename\=\"(.+)\"/)){

		  $name  = $1;
		  $fname = $2;
		  $content_type = $vars[2];
		  $full_fname = $fname;		# R7 NEW

		  # --- �T�|�[�g�p 2 ----#
		  if($FORM{'email'} eq "mt2"){&error("�f�o�b�N���[�hall-$vars,name $name fname $fname content_type $content_type ");}
		  #-----------------#

        	  # �}�C���^�C�v�ɂ��A�f�[�^�𔻕ʂ��A�g���q�𐶐�����

	       	  # �}�C���^�C�v���s���ȏꍇ
		  if(($fname ne "")&&($content_type eq "")){

# �ȉ��̃P�[�X���z�肳���D
# �P�[�X�P�jJ-PHONE�̎��������������ŁA�}�C���f�[�^�����������Ȃ�
# �P�[�X�Q�jJ-PHONE�̃��[�U���m��Ȃ���������f�[�^���A�b�v���[�h

# ���̏ꍇ�̓f�[�^�̃w�b�_�����̃e�L�X�g��͂���̎������ʂ����݂�iGif,JPEG�j�D
# ���s������g���q�����݂��邩�ǂ������`�F�b�N
# ���݂������̊g���q�ɂ�锻�f�ɔC����D
# ���݂��Ȃ��ꍇ�x�����o���I���D

			# �f�[�^�w�b�_����摜�̎�ނ���������
			if($vars[3] =~ /^GIF8/i){
				$check_m .=" �w�b�_�[���͂̌��ʂS��GIF <BR>";
				$content_type="image/gif";
			}elsif($vars[3] =~ /^(.+)JFIF/i){
				$check_m .=" �w�b�_�[���͂̌��ʂS��JPEG <BR>";
				$content_type="image/jpeg";
			}elsif($vars[3] =~ /^\x89PNG/i){
				$check_m .=" �w�b�_�[���͂̌��ʂS��PNG <BR>";
				$content_type="image/png";
			# �g���q�炵���������Ă���ꍇ
			}elsif($fname=~ /\.(\w){1,4}$/){
				$content_type="unknown";#��̊g���q�ɂ�锻�f�ɔC����
			}else{
				&error(" �A�b�v���[�h�G���[�B�A�b�v���[�h�f�[�^�̑��������f�ł��܂���B<BR>\n�t�@�C�����Ɋg���q(.png.jpeg��)��<BR>\n���ĂȂ���\�\\��������܂��B<BR>\n�t�@�C�����ɓK�؂Ȋg���q�����Ă��������B<BR><!--fname,$fname,Mime_types,$content_type,Mes.$check_m-->");
			}

			# �}�C���^�C�v���A�g���q�����
			$ext = &content_type_check($content_type);

			# �摜�f�[�^�݂̂𒊏o
			# ($vars[3]�Ɏ���,4=D_End $vars 5)
			foreach($i=3; $i<$vars;$i++){
				if($data eq ''){
					$data = $vars[$i];
				}else{
					$data .= "\r\n$vars[$i]";
				}
			}
			$data=~ s/\r\nD_End$//;

		  # �}�C���f�[�^���ʒm���ꂽ�ꍇ
		  }else{

			# �}�C���^�C�v���A�g���q�����
			# ��{���j�̓Z�L�����e�B�d������}�C���^�C�v�D��
			$ext = &content_type_check("$content_type");

			# �摜�f�[�^�݂̂𒊏o
                        #($vars[4]�Ɏ���,5=D_End,$vars 6)
			foreach($i=4; $i<$vars; $i++){
				if($data eq ''){
					$data = $vars[$i];
				}else{
					$data .= "\r\n$vars[$i]";
				}
			}
			$data=~ s/\r\nD_End$//;
                  }

		  # �}�C���^�C�v�ɂ��g���q�����I��

		  # �������t�@�C�������o�������ɂȂ�

		  # �ݒ�~�X���`�F�b�N����
		  $PM{'img_dir'} = '.' if($PM{'img_dir'} eq '');

		  if($PM{'img_dir'}=~ /^http\:\/\//i){
			&error(" img_dir�̎w�肪�ԈႦ�Ă��܂��B<BR> �f�B���N�g���Ƃt�q�k�͕ʂ̊T�O�ł��B�f�B���N�g���w�肪�Ahttp�Ŏn�܂邱�Ƃ͂���܂���B<BR> �ݒ��ύX���Ă��������B");
		  }

		  # �摜�ۑ��f�B���N�g���̊m�F
		  if(-d "$PM{'img_dir'}"){
		  }else{
			&error(" �摜�f�[�^�ۑ��p�f�B���N�g��\"$PM{'img_dir'}\"��������܂���D<BR>�w��f�B���N�g��\"$PM{'img_dir'}\"�����݂��Ȃ���\�\\��������܂�<BR>�摜�ۑ��p�f�B���N�g���̃p�X�ݒ�����m�F���������D");
		  }

		  # �t�@�C���������߂�
		  # �p�X���������āA�t�@�C�����݂̂��c���B
		  #95/NT����̃A�b�v���[�h�ɑΉ�
		  $fname=~ s/^(.*)\\//;
		  # UNIX ����̃A�b�v���[�h�ɑΉ�
		  $fname=~ s/^(.*)\///;

		  #&error("�t�@�C���� $fname");

		  $use_orig_name=0;		# �I���W�i���t�@�C�����ۑ��@�\�폜
						# ����� e_FTPboard�ł̂݃T�|�[�g
		  if($use_orig_name==1){				
		  #	&use_orig_name;
		  }else{
		  # �����Ńt�@�C������t����I�v�V�����B
		  # �t�@�C�����̃R���t���N�g��h��

			$date_count="19981204201523";
			$date_count="$year"."$month"."$mday"."$hour"."$min"."$sec";

			# �t�@�C�������d�Ȃ�ꍇ�ύX����
			if( -e "$PM{'img_dir'}/img$date_count\.$ext"){
				$date_count++;
			}elsif( -e "$PM{'img_dir'}/img$date_count\.$ext"){
				$date_count++;
			}elsif( -e "$PM{'img_dir'}/img$date_count\.$ext"){
				&error(" �t�@�C�������菈�����ɃG���[���������܂����B�����x�[�Xmode ");
			}

			$new_fname = "img$date_count\.$ext";
		  }

		  # �����t�@�C���A�b�v���[�h�Ή��p
		  push(@NEWFNAMES, $new_fname);

				# �摜�T�C�Y��p���~�b�^�ɂ��`�F�b�N
				if($PM{'max_upload_img_size'} ne ""){
				 if($ENV{'CONTENT_LENGTH'} >$PM{'max_upload_img_size'}*1024){
				  if($new_fname=~ /\.gif$|\.jpe?g$|\.png$|\.bmp$/i){
					&error(" �f\�[�^���傫�����܂��B�摜�T�C�Y��$PM{'max_upload_img_size'} KB�ȉ��ɂ��Ă��������B�J�����̎B�e�ݒ���������A�B�e�𑜓x�������Ă��������B ");
					exit;
				  }
				 }
				}

		  open(OUT, ">$PM{'img_dir'}/$new_fname")|| &error(" �摜�f�[�^��$PM{'img_dir'}�ɕۑ����ɃG���[���N���܂����D<BR>�w��f�B���N�g��\"$PM{'img_dir'}\"�ɏ����݋����Ȃ���\�\\��������܂�.<BR>�f�B���N�g���̃p�[�~�V�����ݒ���m�F���Ă݂Ă��������D");
		  # IIS,PWS(NT/95)�΍�
		  if($www_server_os=~ /win/i){
			binmode(OUT);
		  }
		  eval "flock(OUT,2);" if($PM{'flock'} == 1 );
		  print OUT $data;
		  eval "flock(OUT,8);" if($PM{'flock'} == 1 );
		  close(OUT);

		  # �e���|�����A�b�v���[�h�f�[�^�̑��݊m�F�t���O
		  # �㏈����,�o�^���f�G���[�������ɉ摜�t�@�C�����폜���邽�߂Ɏg�p�B
		  # �폜��sub error���[�`�����ōs���B
		  $img_data_exists=1;
	
		# ���A�b�v���[�h�t�@�C���ȊO�̃t�H�[���̏���
		}elsif(($vars > 3) && ($vars[1] =~ /name\=\"(\S+)\"/)){

		  $name =$1;
		  $value = "$vars[3]";

		  # �e�L�X�g�G���A�Ɋւ��鏈��
		  if($vars > 5){
			$value .= "\r\n";
			foreach($i=4; $i<$vars; $i++){
				$value .= "$vars[$i]\r\n";
			}
			$value=~ s/\r\nD_End\r\n$//;
			$value=~ s/D_End//g;
			#$value=~ s/\r/CR/g;
			#$value=~ s/\n/LF/g;
		  }

		  # sjis�ɕϊ� (imgboard1.22 Rev.3)
		  # jcode_sj.pl�֘A�̐ݒ�~�X���g���b�v���Č��o
		  # (��x��������΃X�L�b�v���č�����)
		  if($jcode_eval_check_flag != '1'){
			eval "&jcode'convert(*value, 'sjis','sjis','z');";
			if($@ eq ""){
			    $jcode_eval_check_flag=1;
		 	    # ����
			}else{
		 	    # ���s
				&error(" CGI�ݒ�G���[ ���炩�̗��R�œ��{�ꃉ�C�u�����u $jcode_name �v�̓ǂݍ��݂Ɏ��s���܂����B<BR> jcode_sj.pl���̖��O���������w�肳��Ă��Ȃ����A���邢�͎w��p�X�u $jcode_name �v�ɊY���t�@�C�������݂��Ȃ����A���邢�̓p�[�~�b�V�������������Ȃ����̂Ǝv���܂� ");
			}
		  }else{
			&jcode'convert(*value, 'sjis','sjis','z');
		  }
		  $FORM{$name} = $value;		# value��Ԃ�

		}# ��vars�I���̏I���

	  }# foreach $pair(@pairs)�̏I���

	}# �}���`�p�[�g/��}���`�p�[�g�̑I�𕶂̏I���

	# WindowsCE�΍�̑������ύX�ɂ��O���ݒ�t�@�C���̌݊���
	# �̖����J�o�[����
	$FORM{'bbsaction'}	= "$FORM{'action'}" if($FORM{'action'} ne "");
	$FORM{'pre_bbsaction'}	= "$FORM{'pre_action'}" if($FORM{'pre_action'} ne "");
	$FORM{'prebbsaction'}	= "$FORM{'pre_bbsaction'}" if($FORM{'pre_bbsaction'} ne "");

	# J-Phone��TEXTAREA���g���ƁA���s��������\��������B�����h��
	$FORM{'img'}=~ s/\n//g;
	$FORM{'img'}=~ s/\r//g;

#	&download_from_web("$FORM{'img'}");

}
#
#=========================#
# �L���f�[�^�̒ǉ� (R6)
# 2000.11 (�X���b�h�Ή��^)
#=========================#

sub post_data{

	undef @NEW_MESSAGE;
	local($old_seq_no,$new_seq_no,$mes_counter);
	local($img_data_size_num);

	# ���Z�L�����e�B�`�F�b�N
	#
	# GET�ɓ��e���󂯕t���Ȃ��B(������JSKY�̂݉\)
	# ����$PM{'no_upload_from_pc'} ==1�̏ꍇ��PC���瓊�e�����Ȃ��B
 	&check_form_method(" �Z�L�����e�B�x�� "," GET�ɂ��L�����e�͎󂯕t���܂��� ");

	if($PM{'bbs_open'} == 2){
		&error(" �Ǘ��l�̐ݒ�ɂ��A�f���͏������݂��x�ݒ�(ReadOnly)�ƂȂ��Ă���܂��B�L���̓��e�͂ł��܂���B ");
	}elsif($PM{'bbs_open'} < 3){
		&error(" �Ǘ��l�̐ݒ�ɂ��A�f���͏������݂��x�ݒ��ƂȂ��Ă���܂��B�L���̓��e�͂ł��܂���B ");
	}

	# ���t�H�[���̓��e���`�F�b�N
	&form_check;

	# �t�H�[���`�F�b�N�Ŗ�肪����ΏI������
	if($error_message ne ''){
		&rm_tmp_uploaded_files;
		&set_cookies;		# �N�b�L�[���Z�b�g(120Rev5�ȍ~)
		&error($error_message);
		exit;
	}

	# ���e��`�F�b�N�I���A�������e��ϐ��̏���

	# �L���̓��t�\���i�ύX�\)
	$date_data = "\[$year/$month/$mday,$hour:$min:$sec\]";

	# �摜�^�C�g�����쐬
        if(($img_location ne '')&&($imgtitle eq '')){
	# �^�C�g�����Ȃ��ꍇ�̓t�@�C�������^�C�g��
		$imgtitle="$img_location";
	}

	# ���e�摜�̗e�ʂ��v�Z
	if($img_location ne ''){
		$content_length="$ENV{'CONTENT_LENGTH'}";
		$content_length="$content_length"-800;
		$content_length_kb=int($content_length/1024);

		# R7 new Web�ŃQ�b�g�����t�@�C���ɃT�C�Y�ɍ�����
		if($web_get_file_size > 0){
			$content_length_kb=int($web_get_file_size/1024);
		}

		if(("$content_length" > 0)&&("$content_length_kb"==0)){
	        	$img_data_size=1;
		}else{
        		$img_data_size="$content_length_kb";
		}
		$img_data_size_num="$img_data_size";
		$img_data_size="($img_data_size KB)";
	}
		# imgsize�̃o�[�W�������`�F�b�N
	if($imgsize_lib_flag ==1){
		unless($imgsize_version >=20000509){
			&error(" �Ǘ��Ґݒ�̃G���[�B�����𒆎~���܂����B<BR>
			imgsize.pl�̃o�[�W���� $imgsize_version �͌É߂��܂��B�ŐV�ł������p���������B");
		}
	}

	# ���e�摜�̃v���p�e�B���擾
	&check_uploaded_img_property;

	sub check_uploaded_img_property{
	  if((-e "$img_location")&&($imgsize_lib_flag== 1 )){	
		&imgsize("$img_location");
		if(($IMGSIZE{'result'} ==1)&&($img_data_exists==1)){
		#	$IMGSIZE{'name'}�œn��;
		}else{
			undef %IMGSIZE;
		}
	  }
	}

	# �Z�p���[�^�Ƃ��Ė�肠����̂��A���O�ɒu��
	$subject=&Enc_EQ("$subject");

	undef $tmp_data;

	foreach $p_key(keys %FORM){
		if($p_key=~ /^opt(.+)$/){
			$tmp_data=&Enc_EQ($FORM{$p_key});
			$opt_data.="opt_data_"."$1"."\="."$tmp_data"."\;";
			undef $tmp_data;
		}
	}

	# ��������

	# �����b�Z�[�W��ǂݍ���

	$comment_force_reload =1; # �T�d�ɂ��邽�߁A�����œǂ�
	undef @MESSAGE;	
	&read_file_data("$PM{'file'}");
	 # $HEAD_MESSAGE{'name'}�Ƀp�����[�^������
	 # $REM_HEAD_MESSAGE{'name'}�ɃR�����g�A�E�g�p�����[�^������
	 # @MESSAGE�ɋL�����O������

	$old_seq_no=$HEAD_MESSAGE{'seq_no'};	


	# $all_message �ɋL����������
	$all_message=@MESSAGE;


	# �A�ԏ���
	if($old_seq_no eq ""){# �Ȃ��ꍇ�͍��
		$old_seq_no='0';
	}
	$new_seq_no=$old_seq_no+1;

        # �Í���
	if(($PM{'use_crypt'} == 1)&&($rmkey ne "no_key")&&($rmkey ne "")){
		$rmkey		= &make_pass("$rmkey");
	}

	# SNL�Ƃ��đ��݂���f�[�^�̃��X�g�����
	foreach (@SNL_MADE_DATA){
#		$existing_snl_type_list.="$_"."\/";
	}

	# �A��URL�Ń^�u��;���G�X�P�[�v
	$img_import_url=~ s/\t//g;
	$img_import_url=~ s/\;//g;
	$img_import_url=~ s/\s+$//g;

	# sage�@�\
	if(($PM{'use_sage'} == 1)&&($email=~ /^sage$/i)){
		$email="";
		$sage_flag=1;
	}

	# ���V�������b�Z�[�W�����iimgboard1.22R6.1�V�`���j
	$new_message = "$subject\t$name\t$email\t$date_data\t$body<\!--opt\:$opt_data-->\t$img_location\t$imgtitle<\!--dsize=$img_data_size;type=$IMGSIZE{'type'};width=$IMGSIZE{'width'};height=$IMGSIZE{'height'};hw_racio=$IMGSIZE{'hw_racio'};size=$img_data_size_num;-->\t$new_seq_no\t$FORM{'blood'}\t$rmkey\t$unq_id\t$permit\t$other";

	undef %IMGSIZE;

	# ���X�̕t�����L������֎����čs�����߂ɁA�e�X���b�h���X�g�֒ǉ�����
	# 2004.12 sage�@�\��ǉ�
	if(($FORM{'sage'} == "1")||($sage_flag == 1 )){
	  # ���X�g�ɋL�^���Ȃ�
	}else{
	  &update_bloods_list;
	}

	# �L���f�[�^��ǉ�����
	if($FORM{'parent'} eq ""){
	# �e�L���̏ꍇ
		unshift(@MESSAGE, $new_message);
		$all_message++;	# �L�����͈��
	}else{
	# �q�L���̏ꍇ
		# �L���f�[�^��T������

		$mes_counter=1;
		$last_child_number=0;

		foreach(@MESSAGE){
			if($_ =~ /$FORM{'blood'}/){
				$last_child_number=$mes_counter;
			}
			$mes_counter++;
		}

		# �L���f�[�^��ǉ�����
		$mes_counter=1;

		foreach(@MESSAGE){
			push(@NEW_MESSAGE, $_);
			if($mes_counter==$last_child_number){
				push(@NEW_MESSAGE, $new_message);
				$all_message++;	# �L�����͈��
			}
			$mes_counter++;
		}
		@MESSAGE=@NEW_MESSAGE;

	}

	# ��ԌÂ��L���Ɋ֘A�����摜���폜���Ă���

	if($all_message > $PM{'max_message'}){
		for($i=$PM{'max_message'}; $i<$all_message; $i++){
			if($MESSAGE[$i] =~ /^([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]*)\t([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)/){

				$remove_file = $6;
				local($remove_imgtitle) 	= $7;
				local($tmp_unq_id)  		= $11;

				if($remove_file ne '' && -e $remove_file){
					unlink($remove_file);
					# ���^�t�@�C�����폜����
					&rm_meta_file("$remove_file");

					# �g�їp�t�@�C�����폜����
					if($remove_file=~ /\.(jpe?g|gif|png|bmp|mng)$/i){
					  # SNL�̃p�X�𒲂ׂ�
					  if($remove_imgtitle ne ''){
					    &parse_img_param($remove_imgtitle);
					  }
					  &rm_snl_file("$tmp_unq_id","$IMG_PARAMETERS{'snl_dir'}","$IMG_PARAMETERS{'exist_snl_type'}");
					}

				}
			}

		}
	}

	# ���V�����t�@�C���Ƃ��ďo��

	# �o�͋L���������߂�
	if($all_message > $PM{'max_message'}){
		$repost_message = $PM{'max_message'};
	}else{
		$repost_message = $all_message;
	}

	# �����o���O�Ƀo�b�t�@�ɓ����
	undef @TMP_MESSAGE;
	$HEAD_MESSAGE{'seq_no'}=$new_seq_no;

	for($i=0; $i<$repost_message; $i++){
		$TMP_MESSAGE[$i]="$MESSAGE[$i]";
	}

	# �����o������
	 # �ȉ��̓��e���o�͂���
	 # $HEAD_MESSAGE{'name'}
	 # $REM_HEAD_MESSAGE{'name'}
	 # @TMP_MESSAGE

	if($PM{'make_backup_file'}== 1 ){
 	 &make_backup_file; # �o�b�N�A�b�v�t�@�C�������쐬
	}

	&write_file_data("$PM{'file'}");
}
#
#
# �ŋ߂̋L���Ƃ��̌���(�X���b�h)���L������T�u�T�u���[�`��
# imgboardR6�̃��O�ɂ����ẮA�ŐV��15�L�����̋L���h�c��
# �e�̌���(�X���b�h)���p�����[�^�Ƃ��Ċo���Ă������Ƃɂ���B
#
sub update_bloods_list{

	local ($b_new_list);

#	return if($HEAD_MESSAGE{'last_bloods'} eq "");
	$HEAD_MESSAGE{'last_bloods'} =	&Enc_EQ("$HEAD_MESSAGE{'last_bloods'}");

	# �e�L���ǉ��̏ꍇ,�e�[�e�Œǉ�����
	if($FORM{'parent'} eq ""){	
		  return if($unq_id eq "");
		  $b_new_list="$unq_id-$unq_id"."\,"."$HEAD_MESSAGE{'last_bloods'}";
	}else{ 			
	# �q�L���̏ꍇ�A�q�[�e�Œǉ�����
	  return if($unq_id eq "");
	  return if($FORM{'blood'} eq "");
	  $b_new_list="$unq_id-$FORM{'blood'}"."\,"."$HEAD_MESSAGE{'last_bloods'}";
	}

	# �P�T�ȏ�ɂȂ�΁A�P�U�ȍ~�͎̂Ă�
	if($b_new_list=~ /^(\,*)([\d|\-]*)\,([\d|\-]*)\,([\d|\-]*)\,([\d|\-]*)\,([\d|\-]*)\,([\d|\-]*)\,([\d|\-]*)\,([\d|\-]*)\,([\d|\-]*)\,([\d|\-]*)\,([\d|\-]*)\,([\d|\-]*)\,([\d|\-]*)\,([\d|\-]*)\,([\d|\-]*)(.*)/){
		$b_new_list="$2"."\,"."$3"."\,"."$4"."\,"."$5"."\,"."$6"."\,"."$7"."\,"."$8"."\,"."$9"."\,"."$10"."\,"."$11"."\,"."$12"."\,"."$13"."\,"."$14"."\,"."$15"."\,"."$16"."\,";
	}


	$HEAD_MESSAGE{'last_bloods'}=$b_new_list;	
}
# �ŋ߂̋L���Ƃ��̌���(�X���b�h)���L�����郊�X�g���g��
# �ŐV�̃X���b�hUID���o��
#
sub load_latest_bloods_list{

	local (@LATEST_THREAD);
	local (@SEP_BLOODS);
	local ($child,$my_parent);
	local ($already_parent_exist_flag);

	return if($HEAD_MESSAGE{'last_bloods'} eq "");

	@SEP_BLOODS=split(/\,/,$HEAD_MESSAGE{'last_bloods'});# ��x��������

	# �ŐV�̃X���b�h�̃��X�g�����
	for($numb=0;$numb < scalar(@SEP_BLOODS) ;$numb++){
		($child,$my_parent)=split(/\-/,$SEP_BLOODS{$numb});# ��������
		$already_parent_exist_flag = 0;
		foreach(@LATEST_THREAD){
		    if($_ eq "$my_parent"){
			$already_parent_exist_flag = 1;
		    }
		}
                # ���X�g�ɂȂ��ꍇ�̂ݒǉ����� 
		if($already_parent_exist_flag == 0){
		  push(@LATEST_THREAD,$my_parent);
	        }
	}

	return(@LATEST_THREAD);
}
#
#=============================#
# �t�@�C������L���f�[�^��ǂ�
#=============================#
# �����̓t�@�C����
# 
# ���ŌĂ΂��sub open_comment_file�ɂ��
# 1.@main �ɑS���C���f�[�^������
# 2.$comment_open_flag��1�ɂȂ�
# ���������[�h��$comment_force_reload��1�ɂ���
# $HEAD_MESSAGE{'name'}�Ƀw�b�_�f�[�^
# $REM_HEAD_MESSAGE{'name'}�ɃR�����g�A�E�g���ꂽ�w�b�_�f�[�^
# @MESSAGE�ɋL���f�[�^������

sub read_file_data{
 
	local($tmp_ffile) = @_;	# �����̓t�@�C����
	local($tmp_mes_line);


	# �f�[�^�Ǎ��݁i�������̂��߂�@main�ēǂݍ��݃X�L�b�v�t���j
	# @main�Ƀt�@�C���̓��e���i�[
	if(($comment_open_flag !=1)||($comment_force_reload ==1)){
		&open_comment_file("$tmp_ffile");
	}

	# �o�͕ϐ��Q�����t���b�V������
	undef %HEAD_MESSAGE;
	undef %REM_HEAD_MESSAGE;
	undef @MESSAGE;

	foreach(@main){

		# HEADER�ۑ� (�����ւ̊g���������őΉ�)
		# R6�`���ō��g���Ă���̂͂��ꂾ��
		if($_ =~ /^\,param_seq_no(\s*)=(\s*)(\w+)(\s*)/i){
			$HEAD_MESSAGE{'seq_no'}=$3;
		}
		if($_ =~ /^\#?\,param_/i){
			# R6�`���ō��g���Ă���̂�seq_no����
			# R6�`��������΂����D��B�Ȃ����R6.1�œǂ�
			# ������R6.1�ɂ��ׂĈڍs�ł���悤�ɂ��Ă���
			if($_ =~ /^\,param_seq_no(\s*)=(\s*)(\w+)(\s*)/i){
				if($HEAD_MESSAGE{'seq_no'} eq ""){
					$HEAD_MESSAGE{'seq_no'}=$3;
				}
			# �����R6.1�`���ɕύX(=�̉�����;�܂ł��p�����[�^)
			}elsif($_ =~ /^\,param_(\w+)(\s*)=(.*)\;/i){
				$HEAD_MESSAGE{$1}=$3;
				$HEAD_MESSAGE{$1}=&Dec_EQ("$HEAD_MESSAGE{$1}");
			}elsif($_ =~ /^\#\,param_(\w+)(\s*)=(.*)\;/i){
				# (#�ŃR�����g�A�E�g�������̂��܂�)
				$REM_HEAD_MESSAGE{$1}=$3;
				$REM_HEAD_MESSAGE{$1}=&Dec_EQ("$REM_HEAD_MESSAGE{$1}");
			}else{
#				&error(" �f�o�b�N ����`�p�����[�^���� $_ ");
			}

		}

		# �L�����o�b�t�@@MESSAGE�ɓ����
		if($_ =~ /^([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t/){
			$tmp_mes_line="$_";
			chop($tmp_mes_line);
			push(@MESSAGE, $tmp_mes_line);
		}
	}
}

#=========================#
# �L���t�@�C�����J��
#=========================#
# �w��t�@�C����ǂ݁A@main �o�b�t�@�Ɋi�[����B
# @main �ɑS���C���f�[�^������
# $comment_open_flag��1�ɂȂ�
# ���������[�h��$comment_force_reload��1�ɂ���

sub open_comment_file{

#Debug
$read_file_counter++;

	local($local_file) = @_;	# �����̓t�@�C����
	undef @main;
	open(IN, "$local_file")|| &error(" �ݒ�G���[�D�f�[�^�ۑ��p�t�@�C��\"$local_file\"��������܂���D�����͒��f����܂����D");
	eval "flock(IN,1);" if($PM{'flock'} == 1 );
		@main = <IN>;
	eval "flock(IN,8);" if($PM{'flock'} == 1 );
	close(IN);

	$comment_open_flag	='1';
	$comment_force_reload	='0';
}

#============================#
# �t�@�C���ɋL���f�[�^������
#============================#
# �����̓t�@�C����
# $HEAD_MESSAGE{'name'}
# $REM_HEAD_MESSAGE{'name'}
# @TMP_MESSAGE�i���s�Ȃ��j��
# �L���f�[�^�����ēn������
sub write_file_data{
 
	local($tmp_ffile) = @_;	# �����̓t�@�C����

	# �����o������
	open(OUT, "> $tmp_ffile")|| &check_file_open_error;

	eval "flock(OUT,2);" if($PM{'flock'} == 1 );


		# �w�b�_�p�����[�^���o��(R6�`��)
		foreach $p_key(keys %HEAD_MESSAGE){
		  	if($p_key eq "seq_no"){
	 		  # seq_no�����݊����̂��߂�R6�`���ŏo��
			  print OUT "\,param_seq_no=$HEAD_MESSAGE{'seq_no'}\n";
			}
		}
		# �w�b�_�p�����[�^���o��(R6.1�`��)
		foreach $p_key(keys %HEAD_MESSAGE){
	 		  # seq_no�ȊO��R6.1�`���ŏo��
			  $file_line=&Enc_EQ($HEAD_MESSAGE{$p_key});
			  $file_line=~ s/\n//g;
			  $file_line=~ s/\r//g;
			  $file_line="\,param_"."$p_key"."\="."$file_line";
			  print OUT "$file_line\;\n";
			  undef $file_line;
		}

		# �R�����g�A�E�g���ꂽ�w�b�_�p�����[�^���o��(R6.1�`��)
		foreach $p_key(keys %REM_HEAD_MESSAGE){
			$file_line=&Enc_EQ($REM_HEAD_MESSAGE{$p_key});
			$file_line=~ s/\n//g;
			$file_line=~ s/\r//g;
			$file_line="\#\,param_"."$p_key"."\="."$file_line";
			print OUT "$file_line\;\n";
			undef $file_line;
		}

		# �L���������o��
		foreach $file_line(@TMP_MESSAGE){
		    if($file_line eq ""){
			next;
		    }
		    $file_line=~ s/\n//g;
		    $file_line=~ s/\r//g;
		    print OUT "$file_line\n";
		}
	eval "flock(OUT,8);" if($PM{'flock'} == 1 );
	close(OUT);

	# �f�[�^������h��
	$comment_force_reload=1;
}

sub check_file_open_error{
  unless(-e "$tmp_ffile"){
	&error(" �ݒ�G���[�D�f�[�^�p�ۑ��t�@�C��\"$tmp_ffile\"�Ƀf�[�^�������ނ��Ƃ��ł��܂���ł����D<BR>\"$PM{'file'}\"�Ƃ������O�̃t�@�C�����������ʒu�Ɍ�����Ȃ����߂ł��B�p�X�̐ݒ���Ċm�F���Ă݂Ă��������B���e�����͒��f����܂����D");
  }
  unless(-w "$tmp_ffile"){
	&error(" �ݒ�G���[�D�f�[�^�p�ۑ��t�@�C��\"$tmp_ffile\"�Ƀf�[�^�������ނ��Ƃ��ł��܂���ł����D<BR>$PM{'file'}�ɑ΂��鏑���݋����Ȃ����߂��Ǝv���܂��D�p�[�~�V�����̐ݒ���Ċm�F���Ă݂Ă��������B���e�����͒��f����܂����D");
  }
  &error(" �ݒ�G���[�D�f�[�^�p�ۑ��t�@�C��\"$tmp_ffile\"�Ƀf�[�^�������ނ��Ƃ��ł��܂���ł����D<BR>�ݒ���Ċm�F���Ă݂Ă��������B���e�����͒��f����܂����D");
}

#================================#
#  �L���f�[�^�̍폜 (���C����)
#================================#
# R6Ver(�e�q�X���b�h�Ή��^)
# 2000/11
#
sub remove_data{

	$tmpnum=0;
	local($killed_blood_name);		# �폜�����e�L���̌�����ۑ�
	local($tmp_rm_num);
	@remove_list=@_;# ���� �폜���X�g(�V���[�h)

	# ���Z�L�����e�B�`�F�b�N
 	if($ENV{'REQUEST_METHOD'} eq 'GET'){
	  	if(($keitai_flag eq "J-PHONE")&&($jstation_flag < 3)){
		#  �i�t�H���ł��A�i�r�j�x�̎��������ʂ�GET��F�߂�
		}else{
		  &error(" �G���[�B��������h�~�̂��߁AGET��\�\\�b�h�ł́A�폜�ł��Ȃ��d�l�ɂȂ��Ă��܂� ");
		}
	}

	# �������̍폜�w����󂯎��A�z��ɂ���
	# rmid���A��S�V�ŗLID���`�F�b�N�{�b�N�X������炤
	# R4�`����@old_remove_list R6�`����@remove_list�֓���邱��

	foreach $form(sort keys %FORM){
	   if($form =~ /^rmid/){
		if($FORM{"$form"} == 1){
			($tmp_old_rmid,$tmp_new_rmid)	=split(/S/,$form);
			$tmp_old_rmid =~ s/rmid//g;
			push(@old_remove_list, $tmp_old_rmid);
			push(@remove_list, $tmp_new_rmid);
		}
	   }
	}
	$remove_article_number= @remove_list;	# �폜�\�萔


	# ���f�[�^�Ǎ��݁i�X�L�b�v�t���j
	&read_file_data("$PM{'file'}");

	# �w�b�_�͕ۑ�
	# @MESSAGE�ɋL�����O������

	# ���S�̂𒲂ׂāA�폜���Ȃ����@TMP_MESSAGE�Ɉꎞ�I�ɓ����
	foreach(@MESSAGE){

			$tmpnum++;
			undef @SEP_DATA;
			undef %LDATA;

#	@IM122R6DATA=('subject','name','email','date','body','img_location','imgtitle','seq_no','blood_name','rmkey','unq_id','permit','other');

			$tmpdata 	= $_;	# �S�̃f�[�^��ۑ�

			@SEP_DATA 	= split(/\t/,"$_");	# �ؒf���Ĕz��ɓ����

			$i=0;
			foreach $p_key(@IM122R6DATA){ # init_valiables�Œ�`
				$LDATA{$p_key}=$SEP_DATA[$i];
				$i++;
			}


		#	$tmp_body	= $LDATA{'body'};	# check_guest_passwd�֓n��

		#	$LDATA{'img_location'}	# �摜�̏ꏊ
		#	$LDATA{'seq_no'}	# �A��
		#	$LDATA{'blood_name'}	# �e�̌���ID(�q���̂ݎ���)
		#	$LDATA{'rmkey'}		# �폜�L�[
		#	$LDATA{'unq_id'}	# �ŗLID(�����x�[�X)

			$flag_remove = 0;
		#	undef $host_flag;
			undef $allow_remove_flag;
			undef $tmp_rm_num;

			# �e���������ꍇ�͎q�L���͖ⓚ���p�őS������
			if($killed_blood_name ne ""){
			   if($LDATA{'blood_name'} ne ""){
				if($killed_blood_name eq "$LDATA{'blood_name'}"){
				  # �q�L���̉摜�f�[�^������
				  if($LDATA{'img_location'} ne ""){ # �q�L���ɓY�t�摜�������
				    # �摜�t�@�C�����폜����
				    if(-e $LDATA{'img_location'}){
					unlink($LDATA{'img_location'});
					# ���^�t�@�C�����폜����
					&rm_meta_file("$LDATA{'img_location'}");

					# �g�їp�t�@�C�����폜����
					if($LDATA{'img_location'}=~ /\.(jpe?g|gif|png|bmp|mng)$/i){
					  # SNL�̃p�X�𒲂ׂ�
					  if($LDATA{'imgtitle'} ne ''){
					    &parse_img_param($LDATA{'imgtitle'});
					  }
					  &rm_snl_file("$LDATA{'unq_id'}","$IMG_PARAMETERS{'snl_dir'}","$IMG_PARAMETERS{'exist_snl_type'}");
					}
				    }
				  }
				# �L�����폜���ꂽ��X���b�h���X�g����폜����
				  $HEAD_MESSAGE{'last_bloods'}=~ s/$LDATA{'unq_id'}\-(\d+)\,//gi;	

				# ���K�ɏ������e�ƌ�������v�����ꍇ�A�q������
					next;
				}
			   }
			}

			undef @do_remove_list; # ����������

			# �����ŐV���̎w��̈Ⴂ���z������
			if($LDATA{'unq_id'} ne ""){	
			# R6�`���̃��O�̏ꍇ
			# �ŗLID�ŏ���(�����S)
				$tmp_rm_num="$LDATA{'unq_id'}";
				@do_remove_list=@remove_list;
			}else{
			# R4�ȑO�̋��`���̃��O�̏ꍇ
			# �y�[�W���̘A�Ԃŏ���
				$tmp_rm_num="$tmpnum";
				@do_remove_list=@old_remove_list;
			}

			foreach $tmp_list(@do_remove_list){
				if($tmp_rm_num == $tmp_list){

					if($remove_mode eq "guest"){
#						&check_guest_passwd;# �Q�X�g�p�X���[�h���`�F�b�N
				  	}elsif($remove_mode eq "rmkey"){
						# �폜�L�[���`�F�b�N
						&check_rmkey("$LDATA{'rmkey'}");
					}else{
						$allow_remove_flag=1;
					}

					if($allow_remove_flag ==1){

						$flag_remove = 1;
						# �摜�t�@�C�����폜
						if(-e "$LDATA{'img_location'}"){
							unlink("$LDATA{'img_location'}");
							# ���^�t�@�C�����폜����
							&rm_meta_file("$LDATA{'img_location'}");

							# �g�їp�t�@�C�����폜����
							if($LDATA{'img_location'}=~ /\.(jpe?g|gif|png|bmp|mng)$/i){
							  # SNL�̃p�X�𒲂ׂ�
							  if($LDATA{'imgtitle'} ne ''){
							    &parse_img_param($LDATA{'imgtitle'});
						  	  }
						  	  &rm_snl_file("$LDATA{'unq_id'}","$IMG_PARAMETERS{'snl_dir'}","$IMG_PARAMETERS{'exist_snl_type'}");
							}

						}
					}
				}
			}
			# ���ʂ̏���
			if($flag_remove == 0){
				# �폜�Ɏ��s�����Ƃ��́A�o�b�t�@�ɓ���ĕۑ��A�L�����c��
				push(@TMP_MESSAGE, $tmpdata);
			}else{
				# �폜�ɐ���

				# �L�����폜���ꂽ��X���b�h���X�g����폜����
				$HEAD_MESSAGE{'last_bloods'}=~ s/$LDATA{'unq_id'}\-(\d+)\,//gi;	


				if($LDATA{'blood_name'} eq ""){	# �V���O�`���̏ꍇ
					# �e�ɂ͌������Ȃ��B
					# �e�������ꍇ�́A�������c���Ă���
					# �e���폜�ł����ꍇ�̓p�X���[�h���p��
					# �q�͑S��������B�Ȃ��A�q�ɂ͉摜�͂Ȃ�
					$killed_blood_name="$LDATA{'unq_id'}";
				}else{				# �����O�`���̏ꍇ
					$killed_blood_name="";
				}
			}

	} #End of foreach

	# �������o������������
	# $HEAD_MESSAGE{'name'}�Ƀp�����[�^��
	# $REM_HEAD_MESSAGE{'name'}�ɃR�����g�A�E�g�p�����[�^
	# @TMP_MESSAGE�ɋL�����O
	&write_file_data("$PM{'file'}");
}
#
#====================================#
# �e�X���b�h�V����UID���X�g���擾����
#====================================#
# $HEAD_MESSAGE{'last_bloods'}����͂Ƃ���
# @NEW_BLOODS �Ƃ��Đe�X���b�h�V����UID���X�g���o��
# @RECENT_MESSAGE_UID �Ƃ��čŋ߂̋L���̐V����UID���X�g���o��
#�i@RECENT_MESSAGE_UID�͕��Y���B����(new)�\���Ɏg���Ă���j
sub output_new_bloods_list{

	undef @NEW_BLOODS;
	undef @RECENT_MESSAGE_UID;

	local (@SEP_FAMILY);
	local ($b_child,$b_parent,$already_find_flag);

	return if($HEAD_MESSAGE{'last_bloods'} eq "");

	# �q�i�e�j�[�e�̃y�A�ɕ�������
	@SEP_FAMILY=split(/\,/,$HEAD_MESSAGE{'last_bloods'});

	for($numb=0;$numb < scalar(@SEP_FAMILY) ;$numb++){
	  ($b_child,$b_parent)=split(/\-/,$SEP_FAMILY[$numb]);
	  if($b_parent ne ""){
		$already_find_flag=0;
		# ���ɐe���X�g�ɂ���Βǉ����Ȃ�
		foreach(@NEW_BLOODS){
		  if($_ eq "$b_parent"){
			$already_find_flag=1;
		  }
		}
		if($already_find_flag == 0){
		 push(@NEW_BLOODS, $b_parent);
		}
	  }
	  if($b_child ne ""){
		 push(@RECENT_MESSAGE_UID, $b_child);
	  }
	}
	return(scalar(@NEW_BLOODS));
}
#
#==================================================#
#  �L���f�[�^�̍폜 (�폜�L�[��)
#==================================================#
# 2001.02(�Í����Ή�) 
sub check_rmkey{

# �폜�L�[�@�\��L���ɂ����,�폜�L�[����v����ꍇ�A�L���̍폜���ł���B
# �Q�X�g�p�X���[�h�Ƃ̓����g�p�͂ł��Ȃ��B�폜�L�[���ݒ肳��ĂȂ��ꍇ�́A
# �L���̍폜���ł���B�`�F�b�N���s��,�����𖞂�����$allow_remove_flag=1�ƂȂ�B

	local($ttmp_rmkey) = @_;	# �L�����ɖ��ߍ��܂ꂽ�폜�L�[
	# �t�H�[���œ��͂��ꂽ�폜�L�[�i�Í����O�j
	local($tmp_form_rmkey)=$FORM{'passwd'};	
	# �t�H�[���œ��͂��ꂽ�폜�L�[�i�Í����������́j
	local($cpt_form_rmkey);	

	if($PM{'use_crypt'} ==1 ){
		$cpt_form_rmkey=&make_pass($tmp_form_rmkey);
	}

	if(($ttmp_rmkey eq "")||($ttmp_rmkey eq "no_key")){
		# �폜�L�[�����O�ɂȂ��Â��L���̏ꍇ�A�폜��s����
		# �폜�L�[�����O�ɂȂ��L���̏ꍇ�A�폜��s����
		$skipped_rmkey_remove++;	# �폜���s�����L���̐�

		if($remove_article_number=='1'){
			&error(" �p�X���[�h���Ⴂ�܂��D�폜�𒆎~���܂��� ");
		}elsif($remove_article_number == "$skipped_rmkey_remove"){
			&error(" �p�X���[�h���Ⴂ�܂��D�폜�𒆎~���܂��� ");
		}
		return;
	}else{
		# �폜�L�[�����O�ɑ��݂���ꍇ
		if($tmp_form_rmkey eq ""){
			&error(" �폜�L�[�����͂���Ă��܂���B�폜�ł��܂���ł����B<BR>���̋L���ɂ͓��e�҂ɂ��A�폜�L�[���ݒ肳��Ă��܂��B�L�����e���ɗp�����폜�L�[����͂��Ă��������B�Ȃ��A�폜�L�[��Y�������ꍇ�́A�f���Ǘ��҂ɗ���ō폜���Ă�����Ă������� ");
		}elsif($tmp_form_rmkey eq "$ttmp_rmkey"){
			$allow_remove_flag=1;
		}elsif($cpt_form_rmkey eq "$ttmp_rmkey"){
			$allow_remove_flag=1;
		}else{
			&error(" ���͂��ꂽ�폜�L�[�u$FORM{'passwd'}�v���Ⴂ�܂��B�폜�ł��܂���ł����B<BR>���̋L���ɂ͓��e�҂ɂ��A�폜�L�[���ݒ肳��Ă��܂��B�L�����e���ɗp�����폜�L�[����͂��Ă��������B�Ȃ��A�폜�L�[��Y�������ꍇ�́A�f���Ǘ��҂ɗ���ō폜���Ă�����Ă������� ");
		}
	}

}

#
#=====================#
#  �ݒ�ύX����
#=====================#
# 2000.11(�Í����Ή�) 
sub change_config{

# BestBBS�݂����ɁA�ݒ��Web����ύX�ł���悤�ɂ���B

#	&error(" ���łł͂��̋@\�\\�͎g���܂��� ");# �Վ�

	# �����b�Z�[�W��ǂݍ���

	$comment_force_reload =1; # �T�d�ɂ��邽�߁A�����œǂ�
	undef @MESSAGE;	
	&read_file_data("$PM{'file'}");
	 # $HEAD_MESSAGE{'name'}�Ƀp�����[�^������
	 # @MESSAGE�ɋL�����O������

	 # �㏑������p�����[�^(�Z�L�����e�B�I�ɖ��̂�����̂͒ǉ����Ȃ�����)
	@CHANGABLE_PARA=('bbs_open','title','back_url','message_per_page','kiji_disp_limit_imode','hankaku_filter','form_check_name','form_check_email','form_check_subject','form_check_body','limit_upload_times_flag','upload_limit_type','upload_limit_times','use_email','mail_body_limit','oyasumi_message','use_post_password','post_passwd','station_force_set','keitai_force_set','no_upload_from_pc','no_view_from_pc','use_rep','allow_other_multimedia_data','no_upload_by_black_word','res_go_up','disp_new_notice');


	foreach $p_key(keys %FORM){
	  foreach(@CHANGABLE_PARA){
	    if($_ eq "$p_key"){
	     if($FORM{$_} eq "NULL"){
		$HEAD_MESSAGE{$_}= "";
	     }elsif($FORM{$_} ne ""){
		$HEAD_MESSAGE{$_}=$FORM{$_};
	        # �Í���
		if(($_ =~ /_passwd$/)&&($PM{'use_crypt'} == 1)){
			  $HEAD_MESSAGE{$_}= &make_pass("$HEAD_MESSAGE{$_}");
		}
	     }
	     last;
	    }
	  }
	}

	 @TMP_MESSAGE=@MESSAGE;

	# �����o������
	 # �ȉ��̓��e���o�͂���
	 # $HEAD_MESSAGE{'name'}
	 # @TMP_MESSAGE

	&write_file_data("$PM{'file'}");

}
#
#=====================#
#  �ݒ�Ǎ��ݏ���
#=====================#
# 2000.11(�Í����Ή�) 
# 2001.09(�V���v����������) 
sub read_config{

# �ݒ��ǂ�$PM{name}���㏑������

	# �����b�Z�[�W��ǂݍ���
	&read_file_data("$PM{'file'}");
	 # $HEAD_MESSAGE{'name'}�̘A�z�z��Ƀp�����[�^������

	 # �㏑�����Ă��ǂ��p�����[�^(�I��)
	@OVERWRITE_PARA=('title','im_body_bgcolor','make_backup_file','body_background','im_body_text','im_body_link','im_body_vlink','back_url','max_message','img_url','message_per_page','kiji_disp_limit_imode','hankaku_filter','no_upload_from_pc','no_view_from_pc','form_check_name','form_check_email','form_check_subject','form_check_body','form_check_img','form_check_rmkey','form_check_optA','form_check_optB','form_check_optC','form_check_optD','form_check_optE','form_check_optF','form_check_optG','form_check_optH','max_upload_size','max_upload_img_size','auto_url_link','auto_quote_link','use_post_password','post_passwd','use_html_tag_in_comment','use_img_tag_in_comment','no_upload_by_no_RH_user','no_upload_by_black_word','res_go_up','disp_new_notice','error_message_to_black_word','limit_upload_times_flag','upload_limit_type','upload_limit_times','use_email','recipient','mail_body_limit','bbs_open','oyasumi_message','station_force_set','keitai_force_set','use_rep','allow_other_multimedia_data');

	foreach (@OVERWRITE_PARA){
	  if($HEAD_MESSAGE{$_} eq ""){	# 2002.10�o�O�C��
		next;
	  }
	  if(($HEAD_MESSAGE{$_} ne "default")&&($HEAD_MESSAGE{$_} ne "")){
		  $PM{$_}=$HEAD_MESSAGE{$_};
	  }
	}
}
#
#=================================#
#  �����o�b�N�A�b�v�쐬����(R6 new)
#=================================#
# 2001.07(ver.0.7)
# ����̃T�[�o�̃t�@�C���o�͒��_�E���Ⓤ�e�ɂ�郍�O�������̂�
# �����āA$PM{'backup_day_interval'}�Ŏw�肳�ꂽ�Ԋu����file.dat��
# �����o�b�N�A�b�v�����@�\��ǉ�����B
#
sub make_backup_file{

# sub post_data���ŌĂ΂��
# $HEAD_MESSAGE{'last_backup_date'}�ɍŏI�o�b�N�A�b�v������
# unq_id �Ɠ����`���œ����Ă���B
# $PM{'backup_day_interval'}  �Ńo�b�N�A�b�v�Ԋu��ݒ肵
# $PM{'backup_file_name'} �Ƀo�b�N�A�b�v�t�@�C�������w�肵�A����Ă�������

	local($do_backup_flag);
	local($today_day_count);
	local($tmp_day_count);

	# �ݒ肳��ĂȂ��Ƃ��͏������Ȃ��i�݊����j
	if(($PM{'backup_day_interval'} eq "")||($PM{'backup_file_name'} eq "")){
	  return;
	}

	# �L����5���ȉ��̏ꍇ�́A�������Ȃ�
	#�i��t�@�C���̃o�b�N�A�b�v�ɂ��A�o�b�N�A�b�v�t�@�C�����ł�h���j
	if($all_message < 6 ){
	  return;
	}

	# ����p
	if($HEAD_MESSAGE{'last_backup_date'} eq ""){
	  $HEAD_MESSAGE{'last_backup_date'}='20001112020459';
	}
	if($HEAD_MESSAGE{'last_backup_date'}=~ /^(20..)(..)(..)(..)(..)(..)$/){
		$tmp_day_count=$1*365+$2*31+$3;
		if($unq_id=~ /^(....)(..)(..)......$/){
			$today_day_count=$1*365+$2*30+$3;
			if($today_day_count-$tmp_day_count > $PM{'backup_day_interval'}){
			  $do_backup_flag=1;
			}
		}
	}

	# ���̃t���O��1�Ȃ�o�b�N�A�b�v�����
	if($do_backup_flag ==1){
		if(-e "$PM{'backup_file_name'}"){
		   $HEAD_MESSAGE{'last_backup_date'}=$unq_id;# �ŏI�o�b�N�A�b�v�����X�V
		   &write_file_data("$PM{'backup_file_name'}");
		}else{
	   	&error(" �ݒ�G���[�B���e�����͒��f����܂����B�L���o�b�N�A�b�v�f�[�^�ۑ��p�t�@�C��\"$PM{'backup_file_name'}\"�Ƀf�[�^�������ނ��Ƃ��ł��܂���ł����D<BR>\"$PM{'backup_file_name'}\"�Ƃ������O�̃t�@�C�����������ʒu�Ɍ�����Ȃ����߂ł��B�t�@�C�����܂�����Ă��Ȃ��l�́A$PM{'file'}���R�s�[����$PM{'backup_file_name'}�Ƃ������O�ɂ��āA�����f�B���N�g���ɒu���A�p�[�~�b�V�������U�O�U���ɂ��ĉ������B�u�������ǁA�܂����̃G���[���o���l�́A�p�X�̐ݒ���Ċm�F���Ă݂Ă��������B");
		}
	}
}

#=====================#
# �N�b�L�[��ǂ�
#=====================#

sub read_cookie{

	local($given_cookie_data);
 
	$given_cookie_data="$ENV{'HTTP_COOKIE'}";

	# �f�[�^�����Ȃ����͈ȉ��̏������X�L�b�v
	if($given_cookie_data eq ""){
		undef %COOKIES;
		undef %COOKIE;
		return;
	}
	
	# URL�f�R�[�h������(2002.08.12)
	$given_cookie_data=~ s/%([0-9A-Fa-f][0-9A-Fa-f])/pack("C", hex($1))/eg;

	@pairs = split(/\;/,$given_cookie_data);
	foreach $pair(@pairs){
		local($name,$value) = split(/\=/,$pair);
		# �G���R�[�h�����Z�p���[�^����߂��D	
		$name		=~ s/Enc_eq/\=/g;
		$value	=~ s/Enc_eq/\=/g;
		$name 	=~ s/ //g;
		$COOKIES{$name} = $value;
	}

	foreach ( split(/\,/,$COOKIES{'imgboard121'})){
		local($name,$value) = split(/\:/);
		$value=&Dec_EQ($value);
		$COOKIE{$name} = $value;
	}

}

#========================#
# �N�b�L�[������(R5Ver)
#========================#

# imode�ł̓N�b�L�[�͖����Ȃ̂ŁA�H�v����

sub set_cookies{

	undef $set_value;

	# �Z�p���[�^�Ƌ�ʂł��Ȃ��Ȃ遁�����O��Enc_eq�ɒu��

	$FORM{'utc'}=$new_utc_set;	# �A�����e�J�E���^

	@ENC_COOKIE=('subject','name','email','body','viewmode',
'optA','optB','optC','optD','optE','optF',
'imgtitle','utc','entrypass','importURL');

	# �������G���R�[�h����
	foreach(@ENC_COOKIE){
		&CEnc_EQ($_);
	}

	foreach $p_key(keys %T_COOKIE){
		# �p�X���[�h��XXXpasswd�Ƃ���NAME�ɂ���
		# ����͈Í��������
		if($PM{'use_crypt'} ==1){
		   if($p_key=~ /passwd$/){
			$T_COOKIE{$p_key}=&make_pass("$T_COOKIE{$p_key}");
		   }
		}
		$set_value.="$p_key"."\:"."$T_COOKIE{$p_key}"."\,";
	}
	$set_value.="end\:end";

	&set_cookie("imgboard121","$set_value");
}

# �J��Ԃ�
sub CEnc_EQ{
	local($p_name) =$_[0];
	local($jp_name)=$_[0];
	$jp_name	=~ s/_//g; # J-PHONE�΍�
	$T_COOKIE{$p_name}	=$FORM{"$jp_name"}; # �����ŋz��
	$T_COOKIE{$p_name}=&Enc_EQ($T_COOKIE{$p_name});
	return("$T_COOKIE{$p_name}");
}

sub Enc_EQ{
	# �Z�p���[�^�Ƌ�ʂł��Ȃ��Ȃ镶�������O�ɒu��
	local($tmp_data)=@_;
	$tmp_data	=~ s/\=/Enc_eq/g;
	$tmp_data	=~ s/\:/Enc_cln/g;
	$tmp_data	=~ s/\;/Enc_scln/g;
	$tmp_data	=~ s/\,/Enc_km/g;
	return($tmp_data);
}

sub Dec_EQ{
	# �Z�p���[�^�Ƌ�ʂł��Ȃ��Ȃ镶���𕜌�
	local($tmp_data)=@_;
	$tmp_data	=~ s/Enc_eq/\=/g;
	$tmp_data	=~ s/Enc_cln/\:/g;
	$tmp_data	=~ s/Enc_scln/\;/g;
	$tmp_data	=~ s/Enc_km/\,/g;
	return($tmp_data);
}

sub Enc_EQ2{
	# �Z�p���[�^�Ƌ�ʂł��Ȃ��Ȃ镶�������O�ɒu��(mailto�p)
	local($tmp_data)=@_;
	$tmp_data	=&Enc_EQ("$tmp_data");
	$tmp_data	=~ s/\?/Enc_qt/g;
	$tmp_data	=~ s/\&/Enc_amp/g;
	$tmp_data	=~ s/\</Enc_lt/g;
	$tmp_data	=~ s/\>/Enc_gt/g;
	return($tmp_data);
}

sub Dec_EQ2{
	# �Z�p���[�^�Ƌ�ʂł��Ȃ��Ȃ镶���𕜌�
	local($tmp_data)=@_;
	$tmp_data	=&Dec_EQ("$tmp_data");
	$tmp_data	=~ s/Enc_qt/\?/g;
	$tmp_data	=~ s/Enc_amp/\&/g;
	$tmp_data	=~ s/Enc_lt/\</g;
	$tmp_data	=~ s/Enc_gt/\>/g;
	return($tmp_data);
}
#==============================================================#
# i-shot���k

sub Enc_EQ_Short{
	# �Z�p���[�^�Ƌ�ʂł��Ȃ��Ȃ镶�������O�ɒu��
	local($tmp_data)=@_;
	$tmp_data	=~ s/http:\/\//_Hp/g;	# ���k����
	$tmp_data	=~ s/https:\/\//_Hs/g;	# ���k����
	$tmp_data	=~ s/\-/_Eh/g;		# MailBody���̃Z�p���[�^�Ȃ̂ŃG�X�P�[�v
	$tmp_data	=~ s/\=/_Eq/g;
	$tmp_data	=~ s/\:/_Cln/g;
	$tmp_data	=~ s/\;/_Scln/g;
	$tmp_data	=~ s/\,/_Km/g;
	return($tmp_data);
}

sub Dec_EQ_Short{
	# �Z�p���[�^�Ƌ�ʂł��Ȃ��Ȃ镶���𕜌�
	local($tmp_data)=@_;
	$tmp_data	=~ s/_Hp/http:\/\//g;	# ���k����
	$tmp_data	=~ s/_Hs/https:\/\//g;	# ���k����
	$tmp_data	=~ s/_Eh/\-/g;		# MailBody���̃Z�p���[�^�Ȃ̂�
	$tmp_data	=~ s/_Eq/\=/g;
	$tmp_data	=~ s/_Cln/\:/g;
	$tmp_data	=~ s/_Scln/\;/g;
	$tmp_data	=~ s/_Km/\,/g;
	return($tmp_data);
}

sub Enc_EQ2_Short{
	# �Z�p���[�^�Ƌ�ʂł��Ȃ��Ȃ镶�������O�ɒu��(mailto�p)
	local($tmp_data)=@_;
	$tmp_data	=&Enc_EQ_Short("$tmp_data");
	$tmp_data	=~ s/\?/_Qt/g;
	$tmp_data	=~ s/\&/_Amp/g;
	$tmp_data	=~ s/\</_Lt/g;
	$tmp_data	=~ s/\>/_Gt/g;
	return($tmp_data);
}

sub Dec_EQ2_Short{
	# �Z�p���[�^�Ƌ�ʂł��Ȃ��Ȃ镶���𕜌�
	local($tmp_data)=@_;
	$tmp_data	=&Dec_EQ_Short("$tmp_data");
	$tmp_data	=~ s/_Qt/\?/g;
	$tmp_data	=~ s/_Amp/\&/g;
	$tmp_data	=~ s/_Lt/\</g;
	$tmp_data	=~ s/_Gt/\>/g;
	return($tmp_data);
}

sub set_cookie{

	#Copyright(C) to-ru@big.or.jp (1.20�ȍ~ 2000�N�Ή� NEW�o�[�W����)
        local($name,$value) = @_;
        local($sec,$min,$hour,$mday,$mon,$year,$wday,$date);
        local($days) = 900;      # Expire Date(�L�����ԁB�f�t�H���g180��)

        ($sec,$min,$hour,$mday,$mon,$year,$wday) 
                        = (localtime(time+$days*24*60*60))[0,1,2,3,4,5,6];
        $sec   = "0$sec"  if($sec  < 10);
        $min   = "0$min"  if($min  < 10);
        $hour  = "0$hour" if($hour < 10);
        $mday  = "0$mday" if($mday < 10);
        $year += 1900;				# 2000�N�΍�
        $wday  = ("Sun","Mon","Tue","Wed","Thu","Fri","Sat")[$wday];
        $mon   = ("Jan","Feb","Mar","Apr","May","Jun",
                  "Jul","Aug","Sep","Oct","Nov","Dec")[$mon];
        $date = "$wday, $mday\-$mon\-$year $hour:$min:$sec GMT";

		# 2002.08.12 Opera�΍�œ��{���URL�G���R�[�h���邱�Ƃɂ���
		$value =~ s/(\W)/sprintf("%%%02X", unpack("C", $1))/eg;

	# ���N�b�L�[�o��
	if($cookie_ok_flag >= 1){
	  print "Set-Cookie: $name=$value; expires=$date\n";     
	}
}
#
#==================================#
# i�N�b�L�[�p�̔ԍ���V�K����
#==================================#
# �ԍ�����͂��Ȃ������l(���̏ꍇ$memberID����œ����Ă���)�ɑ΂��āA
# �V�ԍ��������ō쐬����B�����i�N�b�L�[���ʂɎg����B
# ���������$memberID�ɑ���̗���������B
# ����͊���i�N�b�L�[�ԍ��Əd�Ȃ�Ȃ�9998�ȉ��̗����ł���B
# �Ȃ�rmkey���Ȃ��ꍇ(imode�ł͍��ڂ�݂��Ȃ��̂Œʏ�͋�),���̔ԍ���
# sub post_data�Ŏg����B�܂�rmkey�Ƃ��Ă����p�����d�l�Ƃ���B
# ����̓��[�U�̗��֐������߂邽�߂ł���B
sub make_memberID{

         local($new_id_number);
         local($saved_id_number);
	 local($sub_no_used_flag);

	# ���]����i�N�b�L�[�ԍ��Əd�Ȃ�Ȃ��ԍ������
	$exit_flag=0;
	while($exit_flag==0){
		srand(time | $$);

		if(($KEITAI_ENV{'UP_SHORT_SUBNO'} ne "")&&($sub_no_used_flag !=1)){
		# EZ�ɂ́A�T�u�X�N���C�o�[�i���o�[���I�X�X������
			$new_id_number=$KEITAI_ENV{'UP_SHORT_SUBNO'};
			$sub_no_used_flag=1;
		}else{
		 $new_id_number=int(rand(9998));
		}

		# �Í����O�ɂƂ��Ă���
		$saved_id_number=$new_id_number;
		if($PM{'use_crypt'}==1){
        		$new_id_number = &make_pass("$new_id_number");
		}
		foreach(@IMODE_USER_ID){
		  &error("while d_counter $d_counter") if($d_counter >3);
		  if($_ eq "$new_id_number"){
			$d_counter++;
			# ��v������������
			next;
		  }
		}
		$FORM{'memberID'}="$saved_id_number";
		$exit_flag=1;
	}
	$FORM{'memberID'}="$saved_id_number";

	# �����ʂ��O���[�o���ϐ��ɑ��
	# rmkey����̏ꍇ(imode�̎��͏�ɋ�ł���)�A���̔ԍ����폜�L�[�ɂ���
	if($rmkey eq ""){
		$FORM{'rmkey'}="$saved_id_number";
 	}
#		&error(" ;a�f�o�b�N�DmemberID -$FORM{'memberID'}-rmkey $FORM{'rmkey'}");
	return;
}

#=========================#
# html�o��
#=========================#
#
sub output_html{

        # cgi_wrap�g�p�v���o�C�_�΍�
	# �Â��v���o�C�_�̒��ɂ�cgi_wrap���g���Ă���v���o�C�_������܂��B
	# ���΃p�X�w����g�p����ꍇ�A���L�̐��l��1�ɂ��āA���̃C���[�W
	# �ۑ��f�B���N�g����URL��$PM{'img_url'}�Ŏw�肷�邱�Ƃɂ��A�f����
	# �g�p���鎖���ł��܂��B����ȊO�̐l�͕K��0�Ɏw�肵�Ă��������B
	# �Ȃ��A1���w�肵���ꍇ��$PM{'img_url'}�̐ݒ肪�K�{�ɂȂ�܂��B   
	$using_cgi_wrap=0;#(�f�t�H���g0)

	# �\�����b�Z�[�W�̏��߂ƏI�������߂�
	if($FORM{'page'} > 0){
		if($FORM{'page'} < $PM{'max_message'}){
			$start_message = $FORM{'page'};
		}else{
			$start_message = $PM{'max_message'};
		}
	}else{
		$start_message = 1;
	}

	$last_message = $start_message + $PM{'message_per_page'} - 1;
	if($last_message > $PM{'max_message'}){
		$last_message = $PM{'max_message'};
	}

	# ���b�Z�[�W��ǂݍ���
	&read_file_data("$PM{'file'}");
	# $HEAD_MESSAGE{'name'}�Ƀw�b�_�f�[�^
	# @MESSAGE�ɋL�����O������


	# ���[�h�����@�\
	if($FORM{'mode'} eq "search_menu"){
		&word_search("$FORM{'SearchWords'}","$FORM{'MatchMode'}");
	}

	# ���X���������̂����
	if($PM{'res_go_up'} == 1 ){
		&res_message_up;
	}


#===========================#
# ���X�����������̂����
#===========================#

sub res_message_up{

	undef	@TEMP_MESSAGE; 
	undef	@GOUP_MESSAGE;	  # ��֎����čs�����b�Z�[�W(��������������)
	undef	@LATEST_MESSAGE;  # ��֎����čs�����b�Z�[�W(�����ă\�[�g��)
	undef	@RECENT_MESSAGE_UID;  # �ŋߓo�^���ꂽ���b�Z�[�W

	# @NEW_BLOODS �Ƃ��Đe�X���b�h�V����UID���X�g���o��
	&output_new_bloods_list;

# Debug
#&error("NEW_BLOODS @NEW_BLOODS");

	undef $tp_match_flag;		# �eUID���R�܂łɂ��邽�߂̃t���O
	local($tp_loop_counter)=0;	# �eUID���R�܂łɂ��邽�߂̃J�E���^
	local($pre_tmp_parent);		# �O�񔲂����e�X���b�hUID
	local($match_tp_counter)=0;	# MESSAGE���甲�����e�X���b�h��

	# ���X�g���珇�Ԃ�ύX����X���b�h�𔲂�
	foreach $line_data(@MESSAGE){
		$tp_match_flag = 0;
		if($match_tp_counter < 4){ # ���ʉ�]��h��
		 $tp_loop_counter=0;
		 foreach $tmp_parent(@NEW_BLOODS){
		  # 3�X���b�h�܂ŏ�֎����čs��
		  # ����ȏ�ɂ���ƕ��ׂ��オ��̂ł�߂�
		  last if($tp_loop_counter >= 3);
		  if($line_data =~ /^([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]*)\t([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)/){
		    if(($tmp_parent eq "$9")||($tmp_parent eq "$11")){

			$tp_match_flag = 1;

			# �O��}�b�`�Ɛe���Ⴄ�ꍇ�̓J�E���g�A�b�v
			if($pre_tmp_parent ne $tmp_parent){
			  $match_tp_counter++;
			}
			$pre_tmp_parent=$tmp_parent;
			last;# ���o�����甲����
		    }
		  }
		  $tp_loop_counter++;
		 }
		}

		if($tp_match_flag == 1){
		  push(@GOUP_MESSAGE, $line_data);
		  $all_message++;
		}else{
		  push(@TEMP_MESSAGE, $line_data);
	  	  $all_message++;
		}

	}

# Debug
#&error("GOUP_MESSAGE @GOUP_MESSAGE");


	# �������X���b�h���\�[�g����

      local($tmp_goup_line);
      $tp_loop_counter=0;
      foreach $tmp_parent(@NEW_BLOODS){
	# 3�X���b�h�܂ŏ�֎����čs��
	  last if($tp_loop_counter >= 3);
	  foreach $tmp_goup_line(@GOUP_MESSAGE){
		if($tmp_goup_line =~ /^([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]*)\t([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)/){
	  	  if(($tmp_parent eq "$9")||($tmp_parent eq "$11")){
			push(@LATEST_MESSAGE,$tmp_goup_line);
	  	  }
	 	}
	  }
	  $tp_loop_counter++;
	}

# Debug
#&error("LATEST_MESSAGE @LATEST_MESSAGE");

	# �\�[�g�����X���b�h��@MESSAGE�̐�[�ɑ���
	unshift(@TEMP_MESSAGE,@LATEST_MESSAGE);
	@MESSAGE=@TEMP_MESSAGE;
	undef @TEMP_MESSAGE; 
}
#
#=================#
# ���[�h�����@�\
#=================#

sub word_search{


	local($search_words)	= $_[0];	# ������������ł��炤
	local($match_mode)	= $_[1];	# �����^�C�v(AND OR)
	local($match_flag);
	local($tmp_parent_seq_no);


	if($search_words ne ""){

	  $search_words =~ s/�@/ /g;
	  @tmp_search_words = split(/\s+/, $search_words);

	  undef @TEMP_MESSAGE;

	  foreach $line_data(@MESSAGE){
		undef $match_flag;
		undef %LDATA;
		$tmp_line_data="$line_data";	# �������郉�C����ۑ�

		@SEP_DATA 	= split(/\t/,"$line_data");	# �ؒf���Ĕz��ɓ����
		$t=0;
		foreach $p_key(@IM122R6DATA){ # init_valiables�Œ�`
			$LDATA{$p_key}=$SEP_DATA[$t];
			$t++;
		}
		undef $child_kiji_flag;	# �q�L���m�F�p�t���O
		undef $old_kiji_flag;	# ���`���m�F�p�t���O
		if($LDATA{'unq_id'} eq ""){
			$old_kiji_flag="1";	# ���`���m�F�p�t���O
		}
		if($LDATA{'blood_name'} ne ""){
			$child_kiji_flag="1";	# �q�L���m�F�p�t���O
		}else{
			$tmp_parent_seq_no="$LDATA{'seq_no'}";
			$parent_counter++
		}

		# �A�� (���̋L���̐e�L����BLOOD���璲�ׂ�A�z�z��)
		# ���X�̐e�\���Ɏg��
		$BLOOD2SEQNO{"$LDATA{'blood_name'}"}="$tmp_parent_seq_no";

		# �������鍀�ڂ̃G���A���w�肷��
		@WSAREA=@IM122R6DATA;
		foreach $p_key(@WSAREA){
			$tmp_line_data.="$LDATA{$p_key}"."\t";
		}

		foreach $tmp_search_word(@tmp_search_words) {

			$tmp_enc_search_word=&Enc_EQ("$tmp_search_word");

if(($tmp_search_word =~/http/)&&($tmp_line_data =~/http/)){
#&error("tmp_search_word-$tmp_search_word-tmp_line_data-$tmp_line_data");
}
			if (index($tmp_line_data,$tmp_search_word) >= 0) {
				$match_flag=1;
				if($match_mode eq 'OR') {
				 last;
				}
			}elsif (index($tmp_line_data,$tmp_enc_search_word) >= 0) {
				$match_flag=1;
				if($match_mode eq 'OR') {
				 last;
				}
			}else{
				if ($match_mode eq 'AND') {
				  $match_flag=0;
				  last;
				}
			}
		}

		if($match_flag ==1){	
		   push(@TEMP_MESSAGE, $line_data);
		}
	  }

	  @MESSAGE=@TEMP_MESSAGE;
	  undef @TEMP_MESSAGE; 
	}else{
		&error(" �������[�h�����͂���Ă��܂��� ");
	}
}



	undef @main;			# ����������i���Ȃ����ǁj
	undef %LDATA;
	$all_message=@MESSAGE;		# �S�L�������擾


   # �����x�݃��[�h�̐ݒ�
	if($PM{'bbs_open'} < 2){
print<<HTML_END;
$HR
�Ǘ��l�̐ݒ�ɂ��A�f���̉{��/���e���͈ꎞ���x�ݒ��ƂȂ��Ă���܂��B\�\\���󂠂�܂���B
HTML_END
exit;
	}


   # ���폜�̎��̐������o��

	if($FORM{'page'} >= 2){
 
	  if($FORM{'mode'} eq "remove_select"){
	    print "<BR>[�폜MODE] <a href=\"$cgi_name?mode=disp_admin_menu\" accesskey=0>�߂�</a><BR>$HR\n"; 
	  }else{

		print "<HR>\n";

	  }

	}elsif($FORM{'mode'} eq "remove_select"){

	  print "<BR>[�폜�ΏۑI��]<BR><a href=\"$cgi_name?mode=disp_admin_menu\" accesskey=0>�߂�</a><BR>����������(�����w���),�ŉ������߽��ނ����A�폜���݁B\n"; 
	  if($PM{'use_rep'} ==1){
	  print "<BR>\n"; 
	  }

		print "<HR>\n";

	}elsif($FORM{'mode'} eq "disp_input_menu"){

   # ���t�H�[�������̂g�s�l�k���o�͂���
	  &output_form_html;
	}else{
        print "<HR>\n";
	}

#====================================#
# �t�H�[�������̂g�s�l�k���o�͂���
#====================================#

sub output_form_html{

	# �������ϐ�������

		# �O�����i�����݃f�[�^�����H�j

		# ����p�X���[�h�ݒ�����ĂȂ��ꍇ�A���ڂ͏o���Ȃ��B
		if($PM{'use_post_password'} != 1){
			$cm_out_pw_h='<!--';
			$cm_out_pw_f='-->';
		}

		# �^�O��������ꍇ�A���ӏ�����ǉ����~�X��\�h����B
		if($PM{'use_html_tag_in_comment'} == 1){
			$tag_siyou_tyuui=' ��މB�Y�꒍�� ';
		}

		# �ԐM�t�H�[�����͉摜�A�b�v���[�h�����Ȃ�
		if($FORM{'bbsaction'} eq 'disp_rep_form'){
			$cm_out_img_h='<!--';
			$cm_out_img_f='-->';
		}


	# ���̓t�H�[����form_html��HTML���o�́i�������͏����ݒ�̏��ōs���j

	&form_imode_html;	# �t�H�[��(imode�ɓ���2009.12)

	# ���̓t�H�[�����̐����������o�́i�������͏����ݒ�̏��ōs���j

	&middle_A_html;
	&middle_B_html;

}


   # ���y�[�W�ύX�{�^��

	&disp_button;

   # ���L�����o�͂���
	&output_kiji_html;

#====================================#
# �L�������̂g�s�l�k���o�͂���
#====================================#

sub output_kiji_html{

	local($tmp_ldata);

	# �L���폜�w��p�̃t�H�[���J�n��

	if($FORM{'mode'} eq "remove_select"){
		print"<!-- �L���폜�w��p�̃t�H�[���J�n�� -->\n";
		print"<FORM ACTION=\"$cgi_name\" METHOD =\"$form_method\">\n";
		print"<INPUT TYPE=HIDDEN NAME=\"page\" VALUE=$start_message>\n";
	}

	# �L���� inu
	for($i=$start_message-1; $i<$last_message; $i++){

	    if($MESSAGE[$i] eq ""){
		next;
	    }
			undef %LDATA;

			@SEP_DATA 	= split(/\t/,"$MESSAGE[$i]");	# �ؒf���Ĕz��ɓ����
			$t=0;
			foreach $p_key(@IM122R6DATA){ # init_valiables�Œ�`
				$LDATA{$p_key}=$SEP_DATA[$t];
				$t++;
			}

			# �p�����[�^�̏���
			undef $child_kiji_flag;	# �q�L���m�F�p�t���O
			undef $old_kiji_flag;	# ���`���m�F�p�t���O
			undef $new_kiji_flag;	# �ŋ߂̋L���t���O


			#	$LDATA{'img_location'}	# �摜�̏ꏊ
			#	$LDATA{'seq_no'}	# �A�ԁi���̋L���j
			#	$LDATA{'blood_name'}	# �e�̌���ID(�q���̂ݎ���)
			#	$LDATA{'rmkey'}		# �폜�L�[
			#	$LDATA{'unq_id'}	# �ŗLID(�����x�[�X)

			$tmp_rmid		= $i+1;

			# ����

			if($LDATA{'unq_id'} eq ""){
				$old_kiji_flag="1";	# ���`���m�F�p�t���O
			}

			if($LDATA{'blood_name'} ne ""){
				$child_kiji_flag="1";	# �q�L���m�F�p�t���O
			}else{
				$parent_counter++
			}

			# �ŐV���e�L���ɂ̓t���O�𗧂Ă�
 			if($PM{'disp_new_notice'}==1){
			    $tp_loop_counter=0;
			    foreach $recent_uid(@RECENT_MESSAGE_UID){
 			     last if($tp_loop_counter >= 3 );
 			     if($recent_uid == $LDATA{'unq_id'} ){
				$new_kiji_flag="1";	# �ŋ߂̋L���t���O
				last;
			     }
			     $tp_loop_counter++;
			    }
			}

			$LDATA{'subject'}=&Dec_EQ("$LDATA{'subject'}");

			# ��ʂ�����imode�p�ł́A�J�^�J�i�͔��p�ɂ���

			if(($PM{'hankaku_filter'}==1)&&(($keitai_flag eq "imode")||($keitai_flag eq "J-PHONE"))){

			  @HANKAKU_PARA=('subject','name','body','imgtitle');
			  foreach(@HANKAKU_PARA){
			    $tmp_ldata=$LDATA{$_};
			    &jcode'z2h_sjis(*tmp_ldata);
			    $LDATA{$_}="$tmp_ldata";
			    undef $tmp_ldata;
			  }
			}

			# ����

			undef %IMG_PARAMETERS;

			# imgtitle������𔲂��o��
			if($LDATA{'imgtitle'} ne ""){
				$LDATA{'imgtitle'}=&parse_img_param("$LDATA{'imgtitle'}");
			}

			# �\�����͍��ڃp�����[�^�𕜌�
			# body�̒��ɁA�R�����g�A�E�g�`���Ńf�[�^�͉B���ۑ�����Ă���
			# ����<!--opt:�p�����[�^��=�l;�p�����[�^��2=�l2�E�E�E-->
			#<!--opt:��-->�������p�����[�^���𒊏o���鏈��
			if($LDATA{'body'} ne ''){
				($LDATA{'body'},$opt_form_data)	=split(/<\!--opt:/,$LDATA{'body'});
				$opt_form_data			=~ s/-->//g;
			}

			#�p�����[�^$opt_form_data���ǉ�����Ă���ꍇ�D
		        undef %OPTDATA;

			if($opt_form_data ne ''){
				foreach ( split(/;/,$opt_form_data)){
					local($name,$value)	= split(/\=/);
					$value			=&Dec_EQ("$value");
					$OPTDATA{$name}	= $value;
					# �]���p�����[�^�ƌ݊����m��
					if($name=~ /^opt_data_(.+)$/){
						$OPTDATA{"opt$1"}	= $value;
					}
				}
			}

			# ����̃z�X�g����ϐ�$user_IP �ɑ��
			# �i�Ȃ肷�܂��h�~�Ȃǂ̎���ő���̂h�o��\���������ꍇ�͂��̕ϐ����g���ĉ������j
			if($LDATA{'body'}=~ /user�F\s([^>]*)(\s*)--/){
			    $user_IP="$1";
			    $user_IP=&tiny_decode("$user_IP"); #2002.02
			}else{
			    $user_IP="No IP info";
			}

			# �g�т̎��̓\�[�X����Ȃ��̂ŁAIP�o���Ȃ�
			$LDATA{'body'}=~ s/<!-- user�F\s([^>]*)(\s*)-->//ig;

			# �e�L�X�g�����N�p�g�s�l�k�w�蕔�ɑ������$data_type��I��
			&define_data_type_disp;

			if($LDATA{'img_location'} ne ''){
				# �摜�^�C�g�����Ȃ��ꍇ,�摜�����^�C�g����
				$LDATA{'imgtitle'} = $LDATA{'img_location'} if $LDATA{'imgtitle'} eq '';
				$LDATA{'imgtitle'} =~ s/^(.*)\///;	# �p�X���������Ė��O�݂̂ɂ���
	
			}



			#=============================================================#
			# CGI�ʃf�B���N�g���T�C�g�Acgiwrap�T�C�g�΍�(imgboard1.22 Rev.3)
			#=============================================================#

			# �݊����̂���
			if($SERVER_NAME eq ""){
				$SERVER_NAME		=$ENV{'SERVER_NAME'};
			}
			if($SERVER_NAME=~ /\.www5(.?)\.biglobe/){
				$using_cgi_wrap=1;
		        }
			if($SERVER_NAME=~ /\.arena\.ne\.jp/){
				$using_cgi_wrap=1;
			}
			if($SERVER_NAME=~ /\.interq\.or\.jp/){
				$using_cgi_wrap=1;
			}
			if($SERVER_NAME=~ /\.coara\.or\.jp/){
				$using_cgi_wrap=1;
			}

			if(($LDATA{'img_location'} =~ /^\/(.+)\/(.+)$/)||($using_cgi_wrap==1)){
				# ��΃p�X�w��̏ꍇ��CGIWRAP�T�[�o�̏ꍇ��URL�w��ɕύX
				if($using_cgi_wrap==1){
					$LDATA{'img_location'}=~ s/^(.+)\///g;
			    }else{
					$LDATA{'img_location'}=~ s/^\/(.+)\///g;
			    }
				# ���鎞�����A�p������
				if($LDATA{'img_location'} ne ""){
				  $LDATA{'img_location'}="$PM{'img_url'}/$LDATA{'img_location'}";
				}
			}

	if($FORM{'mode'} eq "remove_select"){
	# �폜���[�h���͋L�������Ȃ�Z������
		&cut_long_kiji_for_imode("46");
	}else{
	# imode�ŕ\������ꍇ�ɐ�������蒷���L����Z������
	  if(($keitai_flag eq "imode")||($keitai_flag eq "J-PHONE")){
		# �����ݒ�Őݒ肵��$PM{'kiji_disp_limit_imode'}��蒷���ꍇ�J�b�g
		if($KEITAI_ENV{'OTHER_PARAM'} eq "FOMA"){
		  # FOMA�͗]�T������̂ŃP�`�P�`���Ȃ�
		  &cut_long_kiji_for_imode("$PM{'kiji_disp_limit_foma'}");
		# Softbank 2009.12 update	
		}elsif($jstation_flag >= 5){
		  # softbank��300K.�]�T������̂ŃP�`�P�`���Ȃ�
		  &cut_long_kiji_for_imode(($PM{'kiji_disp_limit_foma'}*3));
		}else{
		  # 2004.06.20 add
		  if(($KEITAI_ENV{'CACHE_SIZE'} >= 20)||($ishot_flag == 1)){
		    &cut_long_kiji_for_imode(($PM{'kiji_disp_limit_imode'}*6));
		  # 2004.06.20 J-Phone�p�P�b�g�@
		  }elsif(($KEITAI_ENV{'CACHE_SIZE'} >= 12)||($jstation_flag >= 3)){
		    &cut_long_kiji_for_imode(($PM{'kiji_disp_limit_imode'}*4));
		  # 2003.03.27 add
		  # 2004.06.20 add au 3G�@�΍�
		  }elsif(($KEITAI_ENV{'CACHE_SIZE'} >= 10)||($ishot_flag == 1)||($au_3G_flag >= 1)){
		    &cut_long_kiji_for_imode(($PM{'kiji_disp_limit_imode'}*3));
		  }else{
		    &cut_long_kiji_for_imode("$PM{'kiji_disp_limit_imode'}");
		  }
		}
	  }
	}


			# ����URL�����N������
			if($PM{'auto_url_link'}==1){
				$LDATA{'body'}=&set_auto_url_link($LDATA{'body'});
			}


			# ���[���A�h���X������ꍇ�̂݃����N�ɂ���
			if($LDATA{'email'} ne " no_email"){
			  $mail_a_start	="<A HREF=\"mailto:$LDATA{'email'}\">";
			  $mail_a_end	="</A>";
			}else{
			  $mail_a_start	="";
			  $mail_a_end	="";
			}

			undef $disp_seq_no;	
			if($LDATA{'seq_no'} ne ""){
				$disp_seq_no="$LDATA{'seq_no'}";
			}

			# 2003.07 add
		  	if($keitai_flag eq "pc"){
			 if ($LDATA{$_} =~ /[\xF8\xF9]/) {
	  			 $LDATA{$_} =&remove_emoji_i("$LDATA{$_}");	 # 2002.05 add
	  		 }
			}

			# �����I���


	#------------------------------------------------------------------#
	# �L�������̂g�s�l�k(�ҏW�͏����ݒ蕔�ł����Ȃ��Ă�������)

	undef $disp_re;
	undef $disp_rm_cbox;

	# R6 new
	if($FORM{'mode'} eq "remove_select"){
		undef $mes_rmid;
		# ���A��SEP�V�ŗLID�𑗂�
		$mes_rmid="rmid"."$tmp_rmid"."S"."$LDATA{'unq_id'}";
		$disp_rm_cbox=qq|<INPUT TYPE="CHECKBOX" NAME="$mes_rmid" VALUE="1">\n|;
	}

	 if($new_kiji_flag ==1){
		$disp_new_kiji=qq| -(new)-<BR>\n|;
	 }else{
	  $disp_new_kiji="";
	 }

	# R6�X���b�h�Ή�
	if($child_kiji_flag == '1' ){	# �q�̏ꍇ
		    if($keitai_flag eq "J-PHONE"){
		      # J-PHONE��HR�̎w�肪����
		      print "<BR>����-----------<BR>\n";
		    }else{
				print "<HR width=\"90%\" color=gray>\n";
		    }
		  print"$disp_rm_cbox";
		  print"$disp_new_kiji";
		# �ԐM�L���i�������͏����ݒ�̏��ōs���j
		print"<BLOCKQUOTE>" if($FORM{'mode'} ne "search_menu");
		&kiji_base_html;# �P�D�e�L�X�g�L��
		print"</BLOCKQUOTE>" if($FORM{'mode'} ne "search_menu");

	}else{				# �e�̏ꍇ
		if($old_kiji_flag == '1'){# ���`���Ȃ�ԐM�����N���o���Ȃ�
		}else{
		    if($PM{'use_rep'} == 1 ){
			 $disp_re=qq|<a href="$cgi_name?mode=disp_member_check&page=$start_message&blood=$LDATA{'unq_id'}&parent=$LDATA{'seq_no'}">�ԐM</a>|;
		    }
		}
		if($PM{'use_rep'}==1){
			print "<HR size=3 color=gray>\n";
		}else{
			print "<HR color=gray>\n";
		}
		print"$disp_rm_cbox";
		print"$disp_new_kiji";
		&kiji_base_html;# �P�D�e�L�X�g�L��
	}

	}# for���[�v�̏I��


	# �t�b�^�[��\��

	# �����Ƀo�i�[�L�����`���t�����Ă���ꍇ�́A�ݒ蕔��$B_BANNER{'2'}��HTML�\�[�X�������Ă�������    

	$dd_guest_passwd="$PM{'guest_passwd'}";
	$dd_guest_passwd="" if($PM{'use_guest_passwd'} =='-1');
	$dd_guest_passwd="" if(($keitai_flag eq "imode")||($keitai_flag eq "J-PHONE"));

 		print "<HR>\n";


	foreach(keys %B_BANNER){
		$b_banner_num++;
	}
	$b_banner_num=1 if($b_banner_num ==0);
	$banner_num=($real_page_num % $b_banner_num);
	$banner_num=$b_banner_num if($banner_num == 0);

print<<HTML_END;
	$B_BANNER{$banner_num}
HTML_END

if($FORM{'mode'} eq "remove_select"){
print<<HTML_END;
        <BR>
	<INPUT TYPE="HIDDEN" NAME="bbsaction" VALUE="remove">
	<BR>
        <INPUT TYPE="password" NAME="passwd" SIZE="6" VALUE="$dd_guest_passwd" istyle="4" MODE=numeric>
	<INPUT TYPE="SUBMIT" VALUE="�폜">
	</FORM>
HTML_END
}

		print "<BR>\n";

# �ŕύX�p�{�^����\������
&disp_button;

sub disp_button{

	local($last_disp_message)="$last_message";
	local($enc_SearchWords)=$FORM{'SearchWords'};
	local($mes_p1);
	local($mes_p2);

	# �^�̃y�[�W�����O���[�o���ϐ��Ƃ��č���Ă���
	if($PM{'message_per_page'} >0){
		$real_page_num=int($start_message/$PM{'message_per_page'})+1;
	}else{
		$real_page_num="1";
	}
	# ���K�̈ʒu���`�F�b�N
	if($last_message > $all_message){
	    $last_disp_message="$all_message";
	}
	
	# 2010.10 docomo�t���u���E�U�Ń{�^������ʉE�[�ɏ����錻�ۂɑΏ�
#	print "<center>\n";

	# ���[�h�������̃y�[�W�ύX�{�^���͌����p�����[�^�����������Ă���
	if($FORM{'mode'} eq "search_menu"){
		# �󔒓���get��SearchWords�������؂�Ȃ��悤��URL�G���R�[�h����
		$enc_SearchWords =~ s/(\W)/'%'.unpack("H2", $1)/ego;
		$mes_p1="&SearchWords=$enc_SearchWords&MatchMode=$FORM{'MatchMode'}";
		$mes_p2="�q�b�g";

	}else{
		undef $mes_p1;
		undef $mes_p2;
	}


	if($start_message != $last_disp_message){
# �ʏ�
print<<HTML_END;
 &nbsp;&nbsp; $start_message-$last_disp_message/$mes_p2$all_message����<BR>
HTML_END
	}else{
# �P�y�[�W�ɂP�L�������Ȃ�
print<<HTML_END;
 &nbsp;&nbsp; $start_message/$mes_p2$all_message����<BR>
HTML_END

	}

	if($start_message > 1){
		$pre_message = $start_message - $PM{'message_per_page'};
		$pre_message =1 if $pre_message < 1;
		$tmp_disp_message=$start_message-1;

	    print " <a href=\"$cgi_name?page=1&mode=$FORM{'mode'}&bbsaction=page_change$mes_p1\"> \<�擪\</a> l\n";
		print " <a href=\"$cgi_name?page=$pre_message&mode=$FORM{'mode'}&bbsaction=page_change$mes_p1\"> �O$PM{'message_per_page'}</a>\n";

		if($all_message > $last_message){
			print "-\n"; # �O�̂T���ƌ��̂T��������Ƃ���separator
		}

	}else{
	}

	# �����̃y�[�W�ؑւ��{�^����HTML
	if($all_message > $last_message){
		$next_message = $last_message+1;
		$last_disp_message=$last_message+$PM{'message_per_page'};
		if($all_message < $last_disp_message){
			$last_disp_message=$all_message;
		}

		print " <a href=\"$cgi_name?page=$next_message&mode=$FORM{'mode'}&bbsaction=page_change$mes_p1\"> ��$PM{'message_per_page'}\> </a>\n";

	}else{
		print "    \n";
	}
#	print "</center>\n";

} # End of disp_button

	
	# ����,��������킸,���L�N���W�b�g�̕ύX�͌ł����f�肵�܂��B�i���쌠�N�Q�ƂȂ�܂��j
	# �Ȃ�,���X�N���v�g�̈ꕔ,���邢�͑S���𗘗p,���邢�͎Q�l�ɂ����X�N���v�g���쐬���ꂽ�ꍇ��,
	# ���Ȃ炸�������N�����̌f���ɕt�����Ă��������B
	print "<HR>\n";
	print "<DIV ALIGN=\"RIGHT\">";
	print "FREE <A HREF=\"http:\/\/www.big.or.jp\/~talk\/welcome\/welcome_im01.cgi\">imgboardR6_v<\/A>!!<BR>\n";
	print qq|�g��3��ر/iPhone/Android/�߿ALL�Ή�<BR>\n|;

	print "<\/DIV><BR>\n";

} #????����͉��H

		print "<BR><BR><BR>\n"; # ��}���`�^�b�`�t�H���Ή�
		print "<\/BODY>\n<\/HTML>\n";
		
} #end of output_kiji_html
#
#======================================================#
# imode�ŕ\������ꍇ�ɐ�������蒷���L����Z������
#======================================================#
#
sub cut_long_kiji_for_imode{

	
	# ���� ������
	local($tmp_imode_kiji_disp_limit)=$_[0];	# ������

	local($tmp_limit);
	local($total_kiji_length);

	if($tmp_imode_kiji_disp_limit){
		$tmp_limit="$tmp_imode_kiji_disp_limit";
	}else{
		$tmp_limit='1000';
	}
	$total_kiji_length=length($LDATA{'body'})+length($LDATA{'subject'})+length($LDATA{'name'})+20;
	# �����ݒ�Őݒ肵��������蒷���ꍇ 
	if(($total_kiji_length > ($tmp_limit-10))&&($tmp_limit > 10)){
#&error("aaaa total_kiji_length $total_kiji_length tmp_limit$tmp_limit");

		$LDATA{'body'}=~ s/\<\!--(\s*)user\�F\s([^>]*)(\s*)--\>//g;

		# �擪����w��o�C�g�܂ł̂ݎc��
		$LDATA{'body'} =substr("$LDATA{'body'}",0,$tmp_limit);

		if($FORM{'mode'} eq "remove_select"){
		  $LDATA{'body'} .=" ...<font color=green>(�ȉ���)</font></B>";
		}else{
		  $LDATA{'body'} .=" ...<font color=green>(�\\�����ށB�ȉ���)</font></B>";
		}
	}

}
#
#===========================================================#
# �e�L�X�g�����N�p�g�s�l�k�w�蕔�ɑ������$data_type��I��
#===========================================================#
#
sub define_data_type_disp{

	# �T���l�C��������ꍇ�͂�������g��
	if($IMG_PARAMETERS{'snl_location'} ne ""){
	 &define_data_type_disp2;
	 return;
	}

	undef $data_type;
	undef $mes_type;
	# ��舵���\����t���O
	undef $can_handle_flag;# 1=OK,2=NO,3,0=�s��
	undef $best_fit_type;	# �����^�C�v

	if($LDATA{'img_location'} ne ""){

	  if(($keitai_flag eq "imode")||($keitai_flag eq "J-PHONE")){	  
	   # �ʏ��imode��Softbank��au_3G�̃P�[�X
	    if($LDATA{'img_location'}=~ /\.bmp$/i){
		$data_type="[PC�摜(BMP�`��)]";
		$can_handle_flag=1;
	    }elsif($LDATA{'img_location'}=~ /\.(png|gif)$/i){
		$mes_type="$1";
	   	$mes_type =~ tr/a-z/A-Z/;
		$data_type="[$mes_type�摜]";
		$can_handle_flag=1;
	    }elsif($LDATA{'img_location'}=~ /\.(jpe?g)$/i){
		 $data_type="[�摜(JPEG�`��)]";
		 $can_handle_flag=1;
	    }elsif($LDATA{'img_location'}=~ /\.(asf)$/i){
		$mes_type="$1";
	   	$mes_type =~ tr/a-z/A-Z/;
		$data_type="[PC����($mes_type�`��)]";
		 $can_handle_flag=1;
	    }elsif($LDATA{'img_location'}=~ /\.m4a$/i){
		# 2005.01 �ǉ�
		$data_type="[����(MPEG-4 AAC�`��)]";
		$can_handle_flag=1;
	    }elsif($LDATA{'img_location'}=~ /\.m4v$/i){
		# 2009.12 �ǉ�
		$data_type="[PC����(H.264�`��)]";
		$can_handle_flag=1;
	    }elsif($LDATA{'img_location'}=~ /\.aax?$/i){
		# 2009.12 �ǉ�
		$data_type="[iPod����(audible�`��)]";
		$can_handle_flag=1;
	    }elsif($LDATA{'img_location'}=~ /\.aiff?$/i){
		# 2009.12 �ǉ�
		$data_type="[Apple����DATA]";
		$can_handle_flag=1;
	    }elsif($LDATA{'img_location'}=~ /\.(mp3|midi?|wav)$/i){
		$mes_type="$1";
	   	$mes_type =~ tr/a-z/A-Z/;
		$data_type="[PC����($mes_type�`��)]";
		$can_handle_flag=1;
	    }elsif($LDATA{'img_location'}=~ /\.wma?$/i){
		$data_type="[WinMediaAudio]";
		$can_handle_flag=1;
	    }elsif($LDATA{'img_location'}=~ /\.wax?$/i){
		$data_type="[WinMediaAudio]";
		$can_handle_flag=1;
	    }elsif($LDATA{'img_location'}=~ /\.mp4$/i){
		$data_type="[MPEG-4����]";
		$can_handle_flag=1;
	    }elsif($LDATA{'img_location'}=~ /\.3gp/i){
		$data_type="[iMotion/�����[�r]";
		$can_handle_flag=1;
	    }elsif($LDATA{'img_location'}=~ /\.pdf/i){
		$data_type="[PDF����]";
		 $can_handle_flag=1;
# 2003.06 �ǉ� 2006.12 �ύX
	    }elsif($LDATA{'img_location'}=~ /\.epub/i){
		$data_type="[epub����]";
		 $can_handle_flag=1;
# 2009.12 �ǉ�
	    }elsif($LDATA{'img_location'}=~ /\.swf$/i){
		$data_type="[Flash�`��]";
		$can_handle_flag=1;
# 2006.12 �ǉ�
	    }elsif($LDATA{'img_location'}=~ /\.flv$/i){
		$data_type="[Flash Video�`��]";
		 $can_handle_flag=1;
	    }elsif($LDATA{'img_location'}=~ /\.kar$/i){
		$data_type="[�J���I�PDATA]";
		$can_handle_flag=1;
	    }elsif($LDATA{'img_location'}=~ /\.txt$|\.html?$/i){
		$data_type="[÷��]";
		$can_handle_flag=1;
	    }else{
		$data_type="[�ް�]";
		$can_handle_flag=1;
	    }
	  }else{
	  # PC����i�f����ʗp ���p�J�^�J�i���g�p���Ȃ��j
		$can_handle_flag=1;
	    if($LDATA{'img_location'}=~ /\.(png|bmp|gif|jpe?g)$/i){
		$mes_type="$1";
	   	$mes_type =~ tr/a-z/A-Z/;
	   	$mes_type =~ s/JPG/JPEG/;
		$data_type="[$mes_type�摜]";
	    }elsif($LDATA{'img_location'}=~ /\.(asf)$/i){
		$mes_type="$1";
	   	$mes_type =~ tr/a-z/A-Z/;
		$data_type="[PC����($mes_type�`��)]";
		# 2009.12 �ǉ�
	    }elsif($LDATA{'img_location'}=~ /\.m4a$/i){
		$data_type="[����(MPEG-4 AAC�`��)]";
	    }elsif($LDATA{'img_location'}=~ /\.m4v$/i){
		$data_type="[PC����(H.264�`��)]";
	    }elsif($LDATA{'img_location'}=~ /\.aax?$/i){
		$data_type="[iPod����(audible�`��)]";
	    }elsif($LDATA{'img_location'}=~ /\.aiff?$/i){
		$data_type="[Apple����DATA]";
	    }elsif($LDATA{'img_location'}=~ /\.(mp3|midi?|wav)$/i){
		$mes_type="$1";
	   	$mes_type =~ tr/a-z/A-Z/;
		$data_type="[PC����($mes_type�`��)]";
#	    }elsif($LDATA{'img_location'}=~ /\.wmv$/i){
		$data_type="[WinMediaVideo]";
	    }elsif($LDATA{'img_location'}=~ /\.wma?$/i){
		$data_type="[WinMediaAudio]";
	    }elsif($LDATA{'img_location'}=~ /\.mp4$/i){
		$data_type="[MP4����]";
	    }elsif($LDATA{'img_location'}=~ /\.mov$/i){
		$data_type="[QuickTime����]";
	    }elsif($LDATA{'img_location'}=~ /\.3gpp?$/i){
		$data_type="[3gp����]";
	    }elsif($LDATA{'img_location'}=~ /\.3gp?p?2$/i){
		$data_type="[3g2����(au)]";
	    }elsif($LDATA{'img_location'}=~ /\.pdf$/i){
		$data_type="[PDF����]";
# 2008.06�ǉ������܂�
# 2009.12�ǉ�
	    }elsif($LDATA{'img_location'}=~ /\.epub$/i){
		$data_type="[epub����]";
		
	    }elsif($LDATA{'img_location'}=~ /\.swf$/i){
		 $data_type="[Flash�`��]";
	    }elsif($LDATA{'img_location'}=~ /\.flv$/i){
		$data_type="[Flash Video�`��]";
	    }elsif($LDATA{'img_location'}=~ /\.kar$/i){
		$data_type="[�J���I�PDATA]";
	    }elsif($LDATA{'img_location'}=~ /\.txt$|\.html?$/i){
		$data_type="[�e�L�X�g]";
	    }else{
		$data_type="[�f\�[�^]";
		$can_handle_flag=1;
	    }
	  }
	}
}
#
#=====================================================#
# ���̑��̃T�u���[�`��
#=====================================================#

#=========================#
# �t�H�[���̃`�F�b�N
#=========================#

sub form_check{

	local($crypt_RH)=$REMOTE_HOST;

	foreach $form(sort keys %FORM){

		# �t�H�[���̐��`
		# �^�O�֎~�̏ꍇ
		if($PM{'use_html_tag_in_comment'} !=1){
			$FORM{$form} =~ s/</&lt;/g;		# �^�O�֎~
			$FORM{$form} =~ s/>/&gt;/g;		# �^�O�֎~


			# Style�w��	�֎~
			$FORM{$form} =~ s/style(\s*)=(.|\n)*/
			Sorry..You can not use style in comment./ig;

		}else{
		# �^�O���̏ꍇ

# (�f���C�^�Y���΍�) �e��댯�^�O������

# 2011.12.14 XSS�΍�ŏC��
if(($FORM{$form}=~ /</)||($FORM{$form}=~ /%3C/i)||($FORM{$form}=~ />/)||($FORM{$form}=~ /%3E/i)){
# �^�O���������ꍇ�̂݃`�F�b�N����(������)
$FORM{$form} =~ s/<!--(.|\n)*-->//g;			# SSI��	����
$FORM{$form} =~ s/<IM(A?)G(E?)(\s|\n)*SRC(.|\n)*\.(cgi|pl)(\s*)>/ig
Sorry..You can not load IMG tag CGI in comment./ig;	# IMG�^�O CGI	����
$FORM{$form} =~ s/<(\/?)COMMENT(.|\n)*>(\s*)(\n?)/
Sorry..You can not use COMMENT tag in comment./ig;	# COMMENT�^�O	����
$FORM{$form} =~ s/(<|%3C)(\/?)FORM(.|\n)*(>|%3E)(\s*)(\n?)/
Sorry..You can not use FORM tag in comment./ig;		# FORM		����

# imode�ł̓}�[�L�[���ǂ��g����Ƃ������ƂƁANetscape�̃V�F�A��2���ȉ���
# �Ȃ��Ă��邱�Ƃ���A�}�[�L�[�������邱�ƂɕύX���܂�(2000.4)
#$FORM{$form} =~ s/<(\/?)MARQUEE(.|\n)*>(\s*)(\n?)/
#Sorry..You can not use MARQUEE tag in comment./ig;	# �}�[�L�[	����
$FORM{$form} =~ s/<(\/?)A(.|\n)*tel\:(.|\n)*>(\s*)(\n?)/
Sorry..You can not use auto-tel tag in comment./ig;	# �����d�b�A���J�[����
$FORM{$form} =~ s/(<|%3C)(\/?)INPUT(.|\n)*(>|%3E)(\s*)(\n?)/
Sorry..You can not use FORM element tag in comment./ig;# FORM�v�f	����
$FORM{$form} =~ s/(<|%3C)(\/?)SELECT(.|\n)*(>|%3E)(\s*)(\n?)/
Sorry..You can not use FORM element tag in comment./ig;# SELECT�^�O	����
$FORM{$form} =~ s/(<|%3C)(\/?)script(.|\n)*(>|%3E)(\s*)(\n?)/
Sorry..You can not use SCRIPT tag in comment./ig;	# Javascript,VBscript ����
$FORM{$form} =~ s/(<|%3C)(\/?)OBJECT(.|\n)*(>|%3E)(\s*)(\n?)/
Sorry..You can not use OBJECT tag in comment./ig;	# OBJECT(ActiveX) ����
$FORM{$form} =~ s/(<|%3C)(\/?)applet(.|\n)*(>|%3E)(\s*)(\n?)/
Sorry..You can not use JAVA in comment./ig;		# APPLET ����
$FORM{$form} =~ s/(<|%3C)META(.+)Refresh(.|\n)*(>|%3E)(\s*)(\n?)//ig;#META�^�O��΂��֎~
$FORM{$form} =~ s/(<|%3C)(\/?)EMBED(.+)SRC(.|\n)*(>|%3E)(\s*)(\n?)/
Sorry..You can not use EMBED tag in comment./ig;	# EMBED�^�O	����
$FORM{$form} =~ s/<(\/?)SERVER(.|\n)*>(\s*)(\n?)/
Sorry..You can not use SERVER tag in comment./ig;	# SERVER�^�O	����
$FORM{$form} =~ s/<(\/?)plaintext(.|\n)*>(\s*)(\n?)/
Sorry..You can not use plaintext tag in comment./ig;	# PLAINTEXT�^�O	����
$FORM{$form} =~ s/<(\/?)xmp(.|\n)*>(\s*)(\n?)/
Sorry..You can not use xmp tag in comment./ig;		# XMP�^�O	����
$FORM{$form} =~ s/<(\/?)strike(.|\n)*>(\s*)(\n?)/
Sorry..You can not use strike tag in comment./ig;	# STRIKE�^�O	����
$FORM{$form} =~ s/<s>/
Sorry..You can not use strike tag in comment./ig;	# STRIKE�^�O	����
$FORM{$form} =~ s/<(\/?)listing(.|\n)*>(\s*)(\n?)/
Sorry..You can not use listing tag in comment./ig;	# LISTING�^�O	����
$FORM{$form} =~ s/(<|%3C)(\/?)BODY(.|\n)*(>|%3E)(\s*)(\n?)/
Sorry..You can not use BODY tag in comment./ig;		# BODY�^�O	����
$FORM{$form} =~ s/<(\/?)TITLE(.|\n)*>(\s*)(\n?)/
Sorry..You can not use TITLE tag in comment./ig;	# TITLE�^�O	����
$FORM{$form} =~ s/<(\/?)BASEFONT(.|\n)*>(\s*)(\n?)/
Sorry..You can not use BASEFONT tag in comment./ig;	# BASEFONT�^�O	����
$FORM{$form} =~ s/(<|%3C)(\/?)frame(.|\n)*(>|%3E)(\s*)(\n?)/
Sorry..You can not use FRAME tag in comment./ig;	# FRAME�^�O	����
$FORM{$form} =~ s/(<|%3C)(\/?)iframe(.|\n)*(>|%3E)(\s*)(\n?)/
Sorry..You can not use IFRAME tag in comment./ig;	# IFRAME�^�O	����
$FORM{$form} =~ s/(<|%3C)(\/?)HTML(.|\n)*(>|%3E)(\s*)(\n?)/
Sorry..You can not use HTML tag in comment./ig;		# HTML�^�O	����
$FORM{$form} =~ s/(\/?)COMMENT(.|\n)*>(\s*)(\n?)/
Sorry..You can not use COMMENT tag in comment./ig;	# COMMENT�^�O	����
	}
# �^�O�������Ă��Ȃ��Ă����ׂ�
#unless(($form eq "body")||($form eq "subject")||($form eq "viewmode")||($form eq "name")){
if($FORM{$form} =~ /style(\s*)(\=|%3d)(.|\n)*font\-size:(\s*)(\d+)px/){
 if($4 > 48){
$FORM{$form} =~ s/style(\s*)(\=|%3d)(.|\n)*/
Sorry..You can not use style in tag on comment./ig;	# Style�w��	�֎~
 }
}
if($FORM{$form} =~ /style(\s*)(\=|%3d)(.|\n)*script/){
$FORM{$form} =~ s/style(\s*)(\=|%3d)(.|\n)*script/
Sorry..You can not use style in tag on comment./ig;	# Style�w��	�֎~
}
# visibility���p��
if($FORM{$form} =~ /style(\s*)(\=|%3d)(.|\n)*bility/){
$FORM{$form} =~ s/style(\s*)(\=|%3d)(.|\n)*bility/
Sorry..You can not use style in tag on comment./ig;	# Style�w��	�֎~
}
$FORM{$form} =~ s/(.|\n)*(onClick|onblur|onchange|onmouse|onError|onload|onfocus|onselect|onsubmit|onunload|onreset|onabort|ondblclick|onkey|ondragdrop)(\w{0,8})(\s*)(\=|%3d)/
(imgboard�Z�L�����e�B�ی�V�X�e��)Sorry..You can not use char <B><font color=red>$2<\/font><\/B> in comment./ig;	# onClick��javascript�C�x���g������(�N���X�T�C�g�X�N���v�e�B���O�΍�)
#}
#�댯�^�O���������܂�
			# IMG�^�O�̖����݂��ہH
			if($PM{'use_img_tag_in_comment'} !=1){
				$FORM{$form} =~ s/<IM(A?)G(E?)(\s|\n)*SRC(.|\n)*>(\s*)(\n?)/Sorry..You can not use IMG tag in comment./ig;#IMG�^�O����
			}else{
			# IMG�^�O�𖄍��ޏꍇ�͊O���摜�摜�ł��邱�Ƃ𖾋L����B
				if(($form eq 'body')&&($FORM{$form}=~ /<IMA?GE?(\s)*SRC(.*)>/i)){
					$FORM{$form} =~ s/ALT(\s)*=(\s)*\"(.+)\"/ /ig;	#ALT����
					$FORM{$form} =~ s/ALT(\s)*=(\s)*([^>]+)/ /ig;	#ALT����
					$FORM{$form} =~ s/border(\s)*=(\s)*([^>]+)/ /ig;#Border����
					$FORM{$form} =~ s/<IMA?GE?\s*SRC\s?=\s*(\S*)(\s*)>/<IMG SRC=$1 ALT="���̉摜�͊O���v�v�v�T�[�o�̉摜�ł�" Border=0>�O���摜 /ig;
				}
			}
		}
		$FORM{$form} =~ s/\r//g;		#CR����
		$FORM{$form} =~ s/\n/<BR>/g;		#LF��<BR>��
		$FORM{$form} =~ s/\t//g;		#TAB�̏���
	}

	# �t�H�[���̒l����
	$name      	= "$FORM{'name'}";
	$email     	= "$FORM{'email'}";
	$subject   	= "$FORM{'subject'}";
	$body      	= "$FORM{'body'}";
	$rmkey		= "$FORM{'rmkey'}";
	$imgtitle 	= "$FORM{'imgtitle'}";
	$img_location	= "$PM{'img_dir'}/$new_fname" if $new_fname ne '';
	$viewmode	= "$FORM{'viewmode'}";
	$memberID	= "$FORM{'memberID'}";

	#<�t�H�[���̗L���̃`�F�b�N>
	# ��{�I�Ƀ`�F�b�N����B�������A�v���t�@�C���o�^�������s��
	# ���[�U�̏ꍇ�͖��O��email���`�F�b�N���Ȃ��B
	if($FORM{'bbsaction'} ne 'pf_change'){
		&check_form_data_exist;
	}
        # �e�p�����[�^�͋�ɂȂ�Ȃ��悤�ɂ���
	$name	 =' ���� '      if $name eq '';
	$email   =' no_email'   if $email eq '';
	$subject =' ���� '      if $subject eq '';
	$body    =' �{���Ȃ� '  if $body eq '';
	$rmkey  ='no_key'  	if $rmkey eq '';
	$memberID='9999'	if $memberID eq '';

        # �V�p�����[�^
	if(($keitai_flag ne "pc")||($HTTP_USER_AGENT=~ /iPhone|iPod|iPad|android/i)){
	  $FORM{'optKeitaiFlag'}			="$keitai_flag";
	  $FORM{'optKeitaiServiceCompany'}	="$KEITAI_ENV{'SERVICE_COMPANY'}";
	  $FORM{'optKeitaiHttpVersion'}		="$KEITAI_ENV{'HTTP_VERSION'}";
	  $FORM{'optKeitaiMachineType'}		="$KEITAI_ENV{'MACHINE_TYPE'}";
	  $FORM{'optKeitaiOtherParam'}		="$KEITAI_ENV{'OTHER_PARAM'}";
	  $FORM{'optKeitaiMelodyType'}		="$KEITAI_ENV{'MELODY_TYPE'}";
	}

# �ǉ����ڂɖ��L���̏ꍇ�̃f�t�H���g�l�͈ȉ��̏��������Q�l�ɂ��Ă�������
#	$FORM{'optA'} =' ���� '      if $FORM{'optA'} eq '';

	# �{���Ƀ��[�U�����܂߂�
	# �Í���
	if($KEITAI_ENV{'SERIAL_LONG'} ne ""){
		$crypt_RH="$KEITAI_ENV{'SERIAL_LONG'}"."-KSN-"."$KEITAI_ENV{'SERIAL_SHORT'}";
	}
 	if($crypt_RH ne ""){
		$crypt_RH=&tiny_encode("$crypt_RH");
	}
	$body    = "$body<!-- user�F $crypt_RH-->";


        # ��������h�~ (99/12/01 �ǉ���)
        $email   =~ s/"/&quot;/g;
        $email   =~ s/style(\s*)=(.|\n)*//ig;

		# 2011.09 youbu.be���ߍ��ݓ�Ȃ�A�{�[�g
		if($body=~ /youtu\.be(.|\n)*youtu\.be/i){
			&error(" �G���[�Byoutu.be��URL�͕������ߍ��݂ł��܂���B�ЂƂɂ��Ă��������B ");
		}
	
	if($PM{'use_trip_flag'}==1){

		# �C���L���I����ʂȂ�U���肵�Ȃ�
		if(($FORM{'amode'} eq "select_edit")&&($FORM{'bbsaction'} ne "edit_form")){
		# �ʏ�Ȃ�U���肷��
		}else{
	  		$name =~ s/��/���U/g; # �U���͔����ɂ���
		}

		#2010.02 trip�@�\(�Ȃ肷�܂��h�~)������
		if($name=~ /^(.+)\#(.+)$/g){
			$name		=$1;
			$trip_plain =$2;
			$trip_plain 	=~ s/�@//g;# �S�p�t�B���^
			$trip_plain 	=~ s/\s//g;
 		
			if($trip_plain ne ""){
		 		$trip_plain=substr($trip_plain,1,8);
		 	$salt=substr($trip_plain,2,2);
		 	$salt =~ s/[^\.-z]/\./go;
		 	$salt =~ tr/:;<=>?@[\\]^_`/ABCDEFGabcdef/;
		 	$trip = crypt($trip_plain,$salt);
		 	$trip = substr($trip,-5);
		 	$trip = '��'."$trip";
		 	$name="$name"."$trip";
#&error("$name");
			}
		}
	}
	
	undef $p_key;	
	foreach $p_key(keys %FORM){
		if($p_key=~ /opt_data/){
			$FORM{$p_key}=~ s/style(\s*)=(.|\n)*//ig;
			$FORM{$p_key}=~ s/"/&quot;/g;
		}
	}


}
#=======================#
# �p�X���[�h�����`�F�b�N
#=======================#
#
# ����1 = �`�F�b�N�������p�X���[�h
# ����2 = �Í����ς݁i��������Ȃ��j�p�X���[�h
# �Ԓl  = ��v=1, �s��v=0
sub check_pass{

	local($guess, $pass) = @_;
	local($crypt_guess);
	local($crypt_pass);

	$crypt_guess	=&make_pass("$guess");
	$crypt_pass	=&make_pass("$pass");

	if($crypt_guess eq "$crypt_pass"){
		return(1);
	}else{
		return(0); # �O�ꂽ�玸�s
	}
}
#
#========================#
# �Í����p�X���[�h���쐬
#========================#
#
sub make_pass{

	local($plain) = @_;# ����
	local($salt);
	local($tmp_pass);

	$salt="$ENV{'PROCESSOR_REVISION'}"."$plain";

	if($plain=~ /^ZzZ/){	# 2�d�Í�����h��
		$tmp_pass = "$plain";
	}else{
		$tmp_pass = crypt($plain, $salt);
		$tmp_pass = "ZzZ"."$tmp_pass";
	}
	return ($tmp_pass);

}
#
sub tiny_encode{
	local($plain) = @_;# ����
	 return($plain) if($plain=~ /\,/);
  	 $plain =~ s/n/\,/ig;
    	 $plain =~ tr/a-m/b-n/;
   	 $plain =~ tr/A-M/B-N/; # 2002.12 ����T�[�o�Ή��Œǉ�
  	 $plain =~ s/\,/a/ig;
   	 $plain =~ s/4/\,/g;
    	 $plain =~ tr/0-3/1-4/;
  	 $plain =~ s/\,/0/g;
 	 $plain ="T-Enc"."$plain";
	 return($plain);
}

sub tiny_decode{
	local($plain) = @_;# ����
	 if($plain=~ /T-Enc(.*)$/){
	  $plain = $1;
	  $plain =~ s/a/\,/ig;
    	  $plain =~ tr/b-n/a-m/;
   	  $plain =~ tr/B-N/A-M/; # 2002.12 ����T�[�o�Ή��Œǉ�
  	  $plain =~ s/\,/n/ig;
   	  $plain =~ s/0/\,/g;
    	  $plain =~ tr/1-4/0-3/;
  	  $plain =~ s/\,/4/g;
	 }
	 return($plain);
}
#
#=========================================================#
#   <����unq_id�̋L������Ăяo���i�L���C���@�\�p�j>    #
#=========================================================#
#
sub load_target_data{

	local($t_pattern)=$FORM{'target'};
	local($found_number)=0;

	undef @T_MESSAGE;
	local ($t_message);

	# �f�[�^�Ǎ���
	&read_file_data("$PM{'file'}");

	undef $match_count;
	undef @SEP_DATA;
	foreach (@MESSAGE){

		$tmpdata 	= $_;	# �S�̃f�[�^��ۑ�
		@SEP_DATA 	= split(/\t/,"$_");	# �ؒf���Ĕz��ɓ����

	#	@IM122R6DATA=('subject','name','email','date','body','img_location','imgtitle','seq_no','blood_name','rmkey','unq_id','permit','other');

		$i=0;
		foreach $p_key(@IM122R6DATA){ # init_valiables�Œ�`
			$LDATA{$p_key}=$SEP_DATA[$i];
			$i++;
		}

		if($LDATA{'unq_id'} eq "$t_pattern"){
				push(@T_MESSAGE, $_);
				last; # ���[�v���甲����
		}
	}

	$found_number=@T_MESSAGE;

	if($found_number != 1){
		&error(" �^�[�Q�b�g�f�[�^�T���ُ�B�T��unq_id $t_pattern ������$found_number");
	}

	# �^�[�Q�b�g�̃f�[�^���N�b�L�[�ɑ�����ăt�H�[���ɕ\�����Č�����

	$LDATA{'subject'}=&Dec_EQ("$LDATA{'subject'}");

	# �\�����͍��ڃp�����[�^�𕜌�
	# body�̒��ɁA�R�����g�A�E�g�`���Ńf�[�^�͉B���ۑ�����Ă���
	# ����<!--opt:�p�����[�^��=�l;�p�����[�^��2=�l2�E�E�E-->
	#<!--opt:��-->�������p�����[�^���𒊏o���鏈��
	if($LDATA{'body'} ne ''){
		($LDATA{'body'},$opt_form_data)	=split(/<\!--opt:/,$LDATA{'body'});
		$opt_form_data			=~ s/-->//g;
	}

	$LDATA{'body'}=~ s/\<!-- user�F\s([^>]*)(\s*)--\>//g;

	#�p�����[�^$opt_form_data���ǉ�����Ă���ꍇ�D
         undef %OPTDATA;

	if($opt_form_data ne ''){
		foreach ( split(/;/,$opt_form_data)){
			local($name,$value) = split(/\=/);
			$value=&Dec_EQ("$value");
			$OPTDATA{$name}	= $value;
			$COOKIE{$name}		="$value";
		}
	}
	$COOKIE{'subject'}	="$LDATA{'subject'}";
	$COOKIE{'name'}		="$LDATA{'name'}";
	$COOKIE{'email'}	="$LDATA{'email'}";
	$COOKIE{'body'}		="$LDATA{'body'}";
}
#
#=========================================================#
#   <����blood_name�̋L���Q���Ăяo���o�b�t�@�ɓ����>    #
#=========================================================#
#
# �ԐM���̎Q�ƋL����\�����邽�߂Ɏg��
sub load_family_data{

# �����͐e�� unq_id(blood_name)�ŗL��A����blood_name�����L����
# @T_MESSAGE�ɓ����ĕԂ����B

	local($t_pattern)=$FORM{'target'};
	local($found_number)=0;
	local($tmp_find_flag)=0;

	undef @T_MESSAGE;
	local ($t_message);

	# �f�[�^�Ǎ���
	&read_file_data("$PM{'file'}");

	undef $match_count;
	undef @SEP_DATA;
	foreach (@MESSAGE){

		$tmpdata 	= $_;	# �S�̃f�[�^��ۑ�
		@SEP_DATA 	= split(/\t/,"$_");	# �ؒf���Ĕz��ɓ����

	#	@IM122R6DATA=('subject','name','email','date','body','img_location','imgtitle','seq_no','blood_name','rmkey','unq_id','permit','other');

		$i=0;
		foreach $p_key(@IM122R6DATA){ # init_valiables�Œ�`
			$LDATA{$p_key}=$SEP_DATA[$i];
			$i++;
		}

		if(($tmp_find_flag==0)&&($LDATA{'unq_id'} eq "$t_pattern")){
			$tmp_find_flag=1;
			push(@T_MESSAGE, $_);
		}elsif(($tmp_find_flag==1)&&($LDATA{'blood_name'} eq "$t_pattern")){
				push(@T_MESSAGE, $_);
		}
	}

	$found_number=@T_MESSAGE;
	return($found_number);
}
#
#====================#
# METHOD�̃`�F�b�N
#====================#
#
# GET�ɓ��e���󂯕t���Ȃ��B(������JSKY�̂݉\)
# ����$PM{'no_upload_from_pc'} ==1�̏ꍇ��PC���瓊�e�����Ȃ��B
#
sub check_form_method{

	local($mes_p1,$mes_p2)=@_;	# ���� �G���[���b�Z�[�W

  	if($ENV{'REQUEST_METHOD'} ne 'POST'){
		# GET�̎�
	  	if(($keitai_flag eq "J-PHONE")&&($jstation_flag < 3)){
		#  �i�t�H���ł��A�i�r�j�x�̎��������ʂ�GET��F�߂�
		}else{
		  &error("$mes_p1<BR>$mes_p2");
		}
	}
	# $PM{'no_upload_from_pc'} ==1�̏ꍇ��PC���瓊�e�����Ȃ��B
	&check_upload_from_pc;

}
#
#====================#
# PC�`�F�b�N
#====================#
#
# $PM{'no_upload_from_pc'} ==1�̏ꍇ��PC���瓊�e�����Ȃ��B
#
sub check_upload_from_pc{

	if($PM{'no_upload_from_pc'} ==1){
	  	if(($keitai_flag eq "imode")||($keitai_flag eq "J-PHONE")||($ENV{'REMOTE_ADDR'} eq "219.119.113.35")){
			# ���e�ł��܂�
		}else{
			&error(" �G���[ ���݂̐ݒ�ł́A�g�т��炵�����e���󂯕t���Ȃ��悤�ɂȂ��Ă��܂��B<BR> PC���瓊�e����ꍇ�͊Ǘ��҂�<a href=\"$PM{'cgi_hontai_name'}\">imgboard�{��($PM{'cgi_hontai_name'})</a>�̃A�N�Z�X��URL�𕷂��A����URL���瓊�e���Ă������� ");
		}
	}else{
		# ���e�ł��܂�
	}
}
#
#====================#
# �L���f�[�^�̏C��
#====================#

sub replace_data{

	local($target_tid)=@_;	# ���� �^�[�Q�b�g��ID
	local($tmp_rmkey);	# �L���ɐݒ肳��Ă����폜�L�[
	local($tmp_crypt_rmkey)=$FORM{'rmkey'};	# �Í�������폜�L�[

	if($PM{'use_crypt'} ==1 ){
		$tmp_crypt_rmkey=&make_pass($tmp_crypt_rmkey);
	}

	# ���Z�L�����e�B�`�F�b�N
 	&check_form_method(" �Z�L�����e�B�x�� "," GET�ɂ�鏑�����݂͎󂯕t���܂��� ");

	# ���t�H�[���̓��e���`�F�b�N
	&form_check;

	if($error_message ne ''){
		&set_cookies;		# �N�b�L�[���Z�b�g(120Rev5�ȍ~)
		&error($error_message);
		exit;
	}

	# �Z�p���[�^�Ƃ��Ė�肠����̂��A���O�ɒu��
	$subject=&Enc_EQ("$subject");

	undef $tmp_data;

	foreach $p_key(keys %FORM){
		if($p_key=~ /^opt(.+)$/){
			$tmp_data=&Enc_EQ($FORM{$p_key});
			$opt_data.="opt_data_"."$1"."\="."$tmp_data"."\;";
			undef $tmp_data;
		}
	}

	$all_message=0;

	# �f�[�^�Ǎ���
	&read_file_data("$PM{'file'}");

	undef $match_count;
	undef @SEP_DATA;
	foreach (@MESSAGE){

	       if(($_=~ /$target_tid/)&&($match_count < 1)){

			$match_count++;

			undef @SEP_DATA;
			undef %LDATA;

#	@IM122R6DATA=('subject','name','email','date','body','img_location','imgtitle','seq_no','blood_name','rmkey','unq_id','permit','other');

			$tmpdata 	= $_;	# �S�̃f�[�^��ۑ�

			@SEP_DATA 	= split(/\t/,"$_");	# �ؒf���Ĕz��ɓ����

			$i=0;
			foreach $p_key(@IM122R6DATA){ # init_valiables�Œ�`
				$LDATA{$p_key}=$SEP_DATA[$i];
				$i++;
			}

	# ���V�������b�Z�[�W�����iimgboard1.22R6.1�V�`���j
#	$new_message = "$subject\t$name\t$email\t$date_data\t$body<\!--opt\:$opt_data-->\t$img_location\t$imgtitle<\!--dsize=$img_data_size;type=$IMGSIZE{'type'};width=$IMGSIZE{'width'};height=$IMGSIZE{'height'};hw_racio=$IMGSIZE{'hw_racio'};-->\t$new_seq_no\t$FORM{'blood'}\t$rmkey\t$unq_id\t$permit\t$other";


#&error("$subject $target_tid mc $match_count 9 $LDATA{'rmkey'}");

			# �㏑��������̂͂����ŏ㏑�����
			# �O�̃f�[�^�ۑ������̂܂ܕۑ�������̂̓R�����g�A�E�g

			$LDATA{'subject'}	="$subject";
			$LDATA{'name'}		="$name";
			$LDATA{'email'}		="$email";
#			$LDATA{'date'}		="$date_data";
			$LDATA{'body'}		="$body<\!--opt\:$opt_data-->";
#			$LDATA{'img_location'}	="$img_location";
#			$LDATA{'imgtitle'}	="$imgtitle<\!--dsize=$img_data_size;type=$img_type;width=$img_width;height=$img_height;hw_racio=$img_hw_racio;-->";
#			$LDATA{'seq_no'}	="$new_seq_no";
#			$LDATA{'blood_name'}	="$FORM{'blood'}";
#			$LDATA{'rmkey'}		="$rmkey";
#			$LDATA{'unq_id'}	="$unq_id";
#			$LDATA{'permit'}	="";
#			$LDATA{'other'}		="";

			# �������ĕ�������
			foreach(@IM122R6DATA){
				$new_message.="$LDATA{$_}"."\t";
			}
			push(@TMPMESSAGE, $new_message);
		}else{
			push(@TMPMESSAGE, $tmpdata);
		}# end of if

	} #end of foreach

	$tmp_rmkey="$LDATA{'rmkey'}";

	# �p�X���[�h���`�F�b�N
	if(($tmp_rmkey eq "$FORM{'rmkey'}")||($PM{'admin_passwd'} eq "$FORM{'rmkey'}")||($tmp_rmkey eq "$tmp_crypt_rmkey")||($PM{'admin_passwd'} eq "$tmp_crypt_rmkey")){
#		&error("��v���܂����B���폜�L�[ $tmp_rmkey ���͂��ꂽ�p�X���[�h$FORM{'rmkey'} ");
	}else{
		&error("�p�X���[�h���Ⴂ�܂��B","�L���̏C���ɂ͓��e���ɓ��͂����p�X���[�h���K�v�ł��B<BR>�ēx�p�X���[�h����͂��Ă������� ");
	}


	# �f�[�^�����o���J�n
	# �����o���O�Ƀo�b�t�@�ɓ����
	undef @TMP_MESSAGE;

	@TMP_MESSAGE	=@TMPMESSAGE;

	# �����o������
	&write_file_data("$PM{'file'}");
#&error("$subject $target_tid mc $match_count");

}

#===============================#
# �t�H�[���̓��͍��ڂ̃`�F�b�N
#===============================#

sub check_form_data_exist{
#

	if(($PM{'form_check_name'}==1)&&($name eq '')){
		$error_message .= "���O������܂���B<BR>";
	}
	if(($PM{'form_check_email'}==1)&&($email eq '')){
	  if($filter_bbs_spam==1){
		# 2006.04 SPAM�΍�̉e��
		$error_message .= "�ݒ�G���[�B���[��,URL�֎~SPAM�΍􎞂�email�͕K�{�ɂł��܂���B<BR>";
	  }else{
		$error_message .= "email������܂���B���݂̐ݒ�ł�email�͕K�{���ڂƂȂ��Ă��܂��B<BR>";
	  }
	}
	if(($PM{'form_check_subject'}==1)&&($subject eq '')){
		$error_message .= "�薼������܂���B<BR>";
	}
	if(($PM{'form_check_body'}==1)&&($body eq '')){
		$error_message .= "�{��������܂���B<BR>";
	}
	if(($PM{'form_check_img'}==1)&&($img_data_exists != '1')){
		$error_message .= "�Y�t�摜������܂���B<BR>";
	}
	if(($PM{'form_check_rmkey'}==1)&&($rmkey eq '')){
		$error_message .= "�폜�L�[������܂���B<BR>";
	}
# �ǉ����ڂɖ��L���̏ꍇ�̌x�����b�Z�[�W�́A�ȉ��́uoptX�v���̕�����K�X
# ���������Ă�������

	if(($PM{'form_check_optA'}==1)&&($FORM{'optA'} eq '')){
		$error_message .= "optA ������܂���B<BR>";# �\��
	}
	if(($PM{'form_check_optB'}==1)&&($FORM{'optB'} eq '')){
		$error_message .= "optB ������܂���B<BR>";# �\��
	}
	if(($PM{'form_check_optC'}==1)&&($FORM{'optC'} eq '')){
		$error_message .= "optC ������܂���B<BR>";# �\��
	}
	if(($PM{'form_check_optD'}==1)&&($FORM{'optD'} eq '')){
#		$error_message .= " �A�C�R���I��������܂���B<BR>";# �\��
	}
	if(($PM{'form_check_optE'}==1)&&($FORM{'optE'} eq '')){
		$error_message .= " �g�єԍ�������܂���B<BR>";# �\��
	}
	if(($PM{'form_check_optF'}==1)&&($FORM{'optF'} eq '')){
		$error_message .= "optF ������܂���B<BR>";# �\��
	}
}

#==========================================#
# �t�H�[���̓��͍��ڂ̏ȗ��E�K�{�������\��
#==========================================#

sub auto_omit_disp{

	# �p�����[�^�f�t�H���g���w��
	if($PM{'auto_disp_omit_frag'} ne '1'){
		$PM{'auto_disp_omit_frag'}=0;
	}

	local($html_h)="*"; # �K�{�̏ꍇ
	local($html_s)="";  # �ȗ��\�ȏꍇ

	if($PM{'auto_disp_omit_frag'} eq "1"){

		foreach(keys %PM){
		    if($_ =~ /^form_check_(.+)$/){
			if($PM{$_}==1){
			  $DISP_OMIT{$1} .="$html_h";
		    	}else{
			  $DISP_OMIT{$1} .="$html_s";
		        }
		    }
		}
	}
}
#
#============================#
# �o�^����L�[�`�F�b�N
#============================#
#
sub check_entrypass{

	local($tmp_entrypass)=$FORM{'entrypass'};
 
	if($PM{'use_crypt'} == 1){
		$tmp_entrypass=&make_pass("$tmp_entrypass");
	}

	# �Q�o�C�g����������A�R���p�C���G���[�ɂȂ錻�ۂ�h��
	if($FORM{'entrypass'}=~ /[\x80-\x9f\xe0-\xff]/){
	  $FORM{'entrypass'}="";
	  &error(" �G���[ ����p�X�ɓ��{��͎g���܂��� "," 4�P�^�ȓ��̔��p�����Ɍ����܂� ");
	}


	# ����L�[�`�F�b�N
	if($PM{'use_post_password'}==1){
	 if($FORM{'entrypass'} eq "$PM{'post_passwd'}"){
		return;	# OK
	 }elsif($tmp_entrypass eq "$PM{'post_passwd'}"){
		return;	# OK
	 }else{
		&error(" ����߽��ށi�����j���Ⴂ�܂��D���e�ł��܂���ł����D<BR>(�ڍ�)�g�т���̓��e�̏ꍇ�A���[�U����肷���i���Ȃ����߁A�f���ɑ΂���A�����e�������瓙��h���܂���B���̂��߁A�g�т���̓��e�ɂ͉���p�X���h���K�{�ƂȂ��Ă��܂��B�g�у��[�U�̕��́A�f���Ǘ��҂������p�X���h�������Ă�����Ă������� ");
	 }
	}
}

#=======================================#
# �f���r���΍�Q(1.22Rev6 �@�\������)
#=======================================#

sub protect_from_BBS_cracker{
#
# �i�����f���r�炵�΍�ł��j
#
# �啝�@�\�ǉ�(1.22 Rev4)
# ���O�A�֎~�P��ɂ�鐧���@�\��ǉ����܂����B�z�X�g����p�ɂɕύX����
# ���蓙�A���x�ȁu�r���Z�v�������肩��̃C�^�Y���������ꍇ�ɁA�����
# �g���Ă��������B ���X�g�͏����ݒ�̂Ƃ���ɂ���܂��B

	undef $bad_user_flag;
	local($error_mes_bl);
	local($error_mes_type);
	local($w_pattern);

	# �f�t�H���g�̃_�~�[�G���[���b�Z�[�W
	$error_mes_bl="CGI error 223458 BLT Default";


	#�O���̃u���b�N���X�g�t�@�C���i�֒P��j��Ǎ���
	if(($use_ext_blacklist ==1)&&($PM{'no_upload_by_black_word'}==1)){
		$add_black_word_count=&load_ext_list('blkword.txt','BLACK_WORD');
	}

	#�O���̃X�p�����X�g�t�@�C���i�z�X�g���j��Ǎ���
	if($use_ext_spamlist ==1){
	  $add_spam_count=&load_ext_list('spamlist.cgi','SPAM_HOSTS_IP');
	}

	#�O���̃X�p�����X�g�t�@�C���i�֒P��j��Ǎ���
	if($use_ext_spamlist ==1){
	  $add_spam_word_count=&load_ext_list('spamword.cgi','SPAM_WORD');
	}

 	# ���e���ȊO(view���Ȃ�)�́A�z�X�g���ȊO�̃t�B���^�̓X�L�b�v���ĕ��׌y���i��������j
	if($FORM{'bbsaction'} eq 'post'){

	# 2006.03 add �f����SPAM�΍�
	if($limit_bbs_spam_flag==1){
		if($FORM{'sf'} eq "$spam_keyword"){
		}else{
			&error(" CGI�G���[�D���e�ł��܂���ł����D ");
		}

		# 2010.02 onetime_token�ɂ��SPAM�΍�
		if($FORM{'onetime_token'} eq "$uniq_token"){
#&error("����token  ttmp_uniq_char $ttmp_uniq_char--$FORM{'onetime_token'} - $uniq_token");
		}elsif($FORM{'onetime_token'} eq "$uniq_token_old"){
#&error("��Otoken ttmp_uniq_char $ttmp_uniq_char--$FORM{'onetime_token'} - $uniq_token");
		}else{
			if($PM{'make_bbs_html_top'}!=1){
&error("CGI�G���[ token�����Ԑ؂�ɂȂ�܂����Bttmp_uniq_char $ttmp_uniq_char--$FORM{'onetime_token'} - $uniq_token");
			&error(" CGI�G���[�Dtoken�����Ԑ؂�ɂȂ�A���e�ł��܂���ł����DSPAM�΍�̂��ߓ��e�́A24���Ԉȓ��ɋL�����A���e���Ă������� ");
			}
		}

	}

	# 2006.03 add �f����SPAM�΍�
	if($filter_bbs_spam==1){
		$PM{'no_upload_by_black_word'}=1;
		push(@BLACK_WORD,"tp:");
		push(@BLACK_WORD,"\@");
		push(@BLACK_WORD,"������ ");
		push(@BLACK_WORD,"\[url=");# 2007.05 �ǉ�
#		push(@BLACK_WORD," �� ");
	}

	# 2008.06 �j�R�j�R�̎d�l�ύX�ɑΉ� 2011.06�C��
	if($FORM{'body'}=~ /iframe.*src="http:\/\/([\-a-zA-Z0-9]+)\.nicovideo\.jp\/thumb\/([\-a-zA-Z0-9_]+)"/i){
	 if($PM{'auto_nicovideo_find'}==1){
		&error(" ����G���[�B�j�R�j�R����̃����N��IFRAME�^�O���g�킸�A http://www.nicovideo.jp/watch/$2 �Ɩ{����URL�������L�ڂ���ƁA�����I�ɂ�����Ɩ��ߍ��ݕ\\��\����܂��B���L�ڕ��@�ɕύX���A�ē��e���Ă������� ","","1");
	 }else{
		&error(" ����G���[�BIFRAME�^�O�̓Z�L�����e�B���肠�邽�߁A�{�����Ɏg���܂���B","","1");
	 }
	}


	# �G���[�ŏo������ŗU������
	if(($allow_nicovideo_in_res == 0)&&($FORM{'prebbsaction'} eq "disp_rep_form")){
	 if($FORM{'body'}=~ /ttp:\/\/([\-a-zA-Z0-9]+)\.nicovideo\.jp\/watch\//i){
		&error(" ���[�U�[����G���[�B���݁A�ԐM�L���ɂ̓j�R�j�R����URL�̖��ߍ��݂͂ł��Ȃ��ݒ�ɂȂ��Ă��܂��B<BR>���斄�ߍ��݂́A�e�L���ł����Ȃ��Ă��������B ","","1");
	 }
	}
	
	# ���Ɍ��o���Ă���ꍇ�̓X�L�b�v���č�����
	if(($bad_user_flag!=1)&&($PM{'no_upload_by_black_word'}==1)){

	  foreach (@BLACK_WORD){

	    $w_pattern="$_";
	    $w_pattern=~ s/\s//g;
	    $w_pattern=~ s/�@//g;

	    if($w_pattern ne ""){
		$blkw_count++;
		#�L�����ׂĂ̍��ڂ��`�F�b�N����
		local(@ALL_ITEM)=('body','name','subject','email','imgtitle','optA');
		local($ttt_form)="";
		foreach $form(@ALL_ITEM){
		        $ttt_form = $FORM{"$form"};
			$ttt_form =~ s/\s//g;
			$ttt_form =~ s/�@//g;
			if (index($ttt_form,$w_pattern) >= 0){
				$error_mes_type="black_word";
				$bad_user_flag=1;
				last;# ���o�����甲����
			}
		}
	    }
	  }
	}

	# 2006.04 SPAM�΍�
	if(($PM{'no_upload_by_spam_word'}==1)&&($bad_user_flag != 1)){

	  # 2006.06 SPAM�΍� URL�����N�񋓌^SPAM�΍�
	  if($FORM{'body'}=~ /ttp(.*)/is){

		 if($1=~ /tp:(.*)/is){ #1
		    if($PM{'spam_url_link_limit_1'}==1){
		     &error("URL�����N�͂ЂƂ܂łɂ��Ă��������B");
		    }
		  if($1=~ /tp:(.*)/is){#2
		    if($PM{'spam_url_link_limit_2'}==1){
		     &error("URL�����N�͂ӂ��܂łɂ��Ă��������B");
		    }
		   if($1=~ /tp:(.*)/is){#3
		    if($PM{'spam_url_link_limit_3'}==1){
		     &error("URL�����N�݂͂��܂łɂ��Ă��������B");
		    }
		    if($1=~ /tp:(.*)/is){#4
		     if($PM{'spam_url_link_limit_4'}==1){
		      &error("URL�����N�͂���܂łɂ��Ă��������B");
		     }
		    }#4
		   }#3
		  }#2
		 }#1
	  }

	  # 2007.05 �p��݂̂̓��e��r��
	  if($PM{'spam_limit_non_japanese'}==1){
	   if($img_data_exists == 1){
	   }else{
	    if($FORM{'body'} eq ""){
		&error(" �X�p���΍�ɂ��A�{������̓��e�͂ł��܂���B ");
	    }elsif($FORM{'body'}=~ /^[\x00-\x7f]+$/){
		&error(" �X�p���΍�ɂ��A�p��݂̂̕������e�͂ł��܂���B ");
	    }
	   }
	  }

	  #2007.05 �^�C�g���Ȃǂ�URL�𖄂ߍ���SPAM�΍�
	  if($PM{'no_upload_by_spam_word'} == 1){

	      local(@LINKCHK_ITEM)=('name','subject','email');

	      foreach $form(@LINKCHK_ITEM){
	        $ttt_form = $FORM{"$form"};
		$ttt_form =~ s/\s//g;
		$ttt_form =~ s/�@//g;
		if($ttt_form=~ /tp:\/\/(.*)/is){
		      &error("URL�����N�͂��̗�($form)�ɂ͖��ߍ��߂܂��� ");
		}
		# 2007.06.05 �^�O���ߍ���SPAM�΍��ǉ�
		if($ttt_form=~ /<\//g){
		      &error("�^�O�͂��̗�($form)�ɂ͖��ߍ��߂܂��� ");
		}
		# XHTML�΍�
		if($ttt_form=~ /\/>/g){
		      &error("�^�O�͂��̗�($form)�ɂ͖��ߍ��߂܂��� ");
		}
		# Web�G�X�P�[�v�΍�
		if($ttt_form=~ /&#\d+/g){
		      &error("Web�G�X�P�[�v��������XXX�͂��̗�($form)�ɂ͖��ߍ��߂܂��� ");
		}
	      }
	  }

	  #2007.05 SPAM�ɂ�郁�[���A�h���X���e���u���b�N
	  if(($PM{'no_upload_by_spam_word'} == 1)&&($PM{'no_upload_by_spam_country_mail'} == 1)){

	      local(@LINKCHK_ITEM)=('name','subject','email');

	      foreach $form(@LINKCHK_ITEM){
	        $ttt_form = $FORM{"$form"};
		$ttt_form =~ s/\s//g;
		$ttt_form =~ s/�@//g;
	        if(($ttt_form=~ /\@/g)||($ttt_form=~ /��/g)){
		 foreach (@SPAM_MAIL_COUNTRY){
		    $w_pattern="$_";
		    $w_pattern=~ s/\s//g;
	    	    $w_pattern=~ s/�@//g;
		    if($ttt_form=~ /$w_pattern/ig){
		      &error("�X�p���t�B���^�[�ݒ�ɂ��A���̃��[���A�h���X��($form)���ɏ������߂܂���B ");
		    }

		 }
		}

	      }
	  }

	  # 2010.02
	  
			#2010.02 kisaragi-SPAM�΍�
			if($FORM{'body'} ne ""){
			 $ttmp2_form_data="$FORM{'body'}";
	    	 $ttmp2_form_data=~ s/\s//g;
	    	 $ttmp2_form_data=~ s/�@//g;

			 # �Vkisaragi-SPAM�΍�
			 # Web�G�X�P�[�v�΍������
			 if($ttmp2_form_data=~ /&#\d+/g){
		      &error("SPAM�΍�ɂ��AWeb�G�X�P�[�v��������XXX�͖{���ɂ͖��ߍ��߂܂��� ");
			 }
			 # 2010.07
			 if($ttmp2_form_data=~ /&#x/gi){
		      &error("SPAM�΍�ɂ��AWeb�G�X�P�[�v��������x�͖{���ɂ͖��ߍ��߂܂��� ");
			 }

			 $ttmp_host_addr="";
			 $ttmp_host_ip="";
			 # 2010.09 update SPAM�Ǝ҃h���C���̑��l���ɑΏ�
			 # 2010.12 update �當���̌댟�o�ɑΏ�
			 # 2012.05 update ��p�h���C�������^�C�v�ɑΏ�
			 if (@URL_HOST_LINKS =  $ttmp2_form_data =~ /\/+([^\)\/]+[\.com|\.net|\.org|\.info|\.biz|\.uk|\.name|\.in|\.tk|\.be|\.mobi|\.co|\.asia|\.jp])/) {
  				foreach (@URL_HOST_LINKS) {
				 next if($_ eq "");
				 # �h���C������IP�A�h���X�𓾂�(API����J�v���o�C�_��z��)
				 $ttmp_host_addr = gethostbyname($_);
  				 $ttmp_host_ip = join('.', unpack("C*", $ttmp_host_addr));
	  			 push(@URL_IP_LINKS, $ttmp_host_ip);  # IP�A�h���X��z��ɕۑ�����B
#&error("SPAM = URL_IP_LINKS - @URL_IP_LINKS - URL_HOST_LINKS - @URL_HOST_LINKS - SPAM_HOSTS_IP - @SPAM_HOSTS_IP");
  			 	}
  			 }
  			 
		 	 foreach (@URL_IP_LINKS){		 	 
				next if($_ eq "");
				$ttmp_link_url_ip="$_";
		 	 	foreach (@SPAM_HOSTS_IP){
				 next if($_ eq "");
			    # ���K�\����Perl�p�^�[���}�b�`�֕ϊ�
	    		$ip_pattern=&change_pattern_match($_);
				   if ($ttmp_link_url_ip =~ /^$ip_pattern/i){
					$error_mes_type="black_word";
					$bad_user_flag=1;
#2008.08.08 temp ���ƂŕK���폜
#&error("SPAM���o = URL_IP_LINKS - @URL_IP_LINKS - URL_HOST_LINKS - @URL_HOST_LINKS - ttmp_link_url_ip $ttmp_link_url_ip ip_pattern $ip_pattern -");				
					last;# ���o�����甲����
		 	 	   }
		 	    }
		 	    last if($bad_user_flag==1);
 			 }
 			}

	  foreach (@SPAM_WORD){

	    $w_pattern="$_";
	    $w_pattern=~ s/\s//g;
	    $w_pattern=~ s/�@//g;

	    if($w_pattern ne ""){
		$blkw_count++;
		#�L�����ׂĂ̍��ڂ��`�F�b�N����
		local(@ALL_ITEM)=('body','name','subject','email','imgtitle','optA');
		local($ttt_form)="";
		$spam_link_find_flag=0;# URL�����N�����邩�ǂ����i�O���[�o���j
		foreach $form(@ALL_ITEM){
			$spam_link_find_flag=0;	# ������
		        $ttt_form = $FORM{"$form"};
			$ttt_form =~ s/\s//g;
			$ttt_form =~ s/�@//g;
			if($ttt_form=~ /tp:/i){
				$spam_link_find_flag=1;
			}elsif($ttt_form=~ /������/i){
				$spam_link_find_flag=1;
			}elsif($ttt_form=~ /\@/i){
				$spam_link_find_flag=1;
#			}elsif($ttt_form=~ /��/i){
#				$spam_link_find_flag=1;
# 2007.05 �C��
			}elsif($ttt_form=~ /\[url=/i){
				$spam_link_find_flag=1;
			}else{
				$spam_link_find_flag=0;
				next;	# URL�����N���Ȃ��ꍇ�̓`�F�b�N���Ȃ�
			}
			if (index($ttt_form,$w_pattern) >= 0){
				$error_mes_type="black_word";
				$bad_user_flag=1;
				last;# ���o�����甲����
			}
		}
	    }
	  }
	}

	# ���_�����o�����ꍇ�̏���
	if($bad_user_flag==1){
		# �_�~�[�̃G���[���b�Z�[�W���o��
		if($error_mes_type eq "black_word"){
			# �ݒ�Ŏw�肵�Ă���ꍇ�͂�����g���B�Ȃ��Ȃ�f�t�H���g	
			if($PM{'error_message_to_black_word'} ne ""){
				$error_mes_bl="$PM{'error_message_to_black_word'}";
			}
		}
       	&error("$error_mes_bl $blkw_count<!--abwc $add_black_word_count-->");
	}

	}	# ���e���ȊO(view���Ȃ�)�́A�z�X�g���ȊO�̃t�B���^�̓X�L�b�v�i�����܂Łj
}

# �O�����X�g�����[�h���镔�i

sub load_ext_list{

	local($list_fname)	= $_[0];	# ���X�g�̖��O
	local($array_name)	= $_[1];	# �z��̖��O
	local($add_count)	= 0;		# ���X�g����ǉ����ꂽ���ڐ�

	if(-e "$list_fname"){
	open(IN, "$list_fname")|| &error("�ݒ�G���[�D�t�@�C��\"$list_fname\"��Ǎ��߂܂���D�����͒��f����܂����D");
	eval "flock(IN,1);" if($PM{'flock'} == 1 );
		while(<IN>){
			if($_ =~ /^([^#])(.*)$/){	#�R�����g�A�E�g�͏���
				if($_ =~ /^(\s*)(\S+)(\s*)(\#?)(.*)$/){
					# Perl4�ł������������ɂ���i�����Ȃ邯�ǁj
					if($array_name eq 'BLACK_LIST'){
# �g�є�Ή�					push(@BLACK_LIST, $2);
					}elsif($array_name eq 'BLACK_WORD'){
						push(@BLACK_WORD, $2);
					}elsif($array_name eq 'SPAM_HOSTS_IP'){
						push(@SPAM_HOSTS_IP, $2);
					}elsif($array_name eq 'SPAM_WORD'){
						push(@SPAM_WORD, $2);
					}
					$add_count++;
				}
			}
		}
	eval "flock(IN,8);" if($PM{'flock'} == 1 );
	close(IN);
	}
	return($add_count);	# ���X�g����ǉ����ꂽ���ڐ�
}

sub change_pattern_match{

	# ���K�\����Perl�p�^�[���}�b�`�֕ϊ�

	local($d_pattern)	= $_[0];
	$d_pattern=~ s/\s|\r|\n|\;|\)//g;	# �O�̂���
	$d_pattern=~ s/\./\\./g;
	$d_pattern=~ s/\?/\./g;
	$d_pattern=~ s/\*/\.\*/g;
	$d_pattern=~ s/P_TAIL$/\$/i;
	$d_pattern=~ s/P_END$/\$/i;
	$d_pattern=~ s/^P_HEAD/\^/i;
	$d_pattern=~ s/P_SPACE/\\s/i;
	return($d_pattern)
}


#============================#
# �i�t�l�o�p�g�s�l�k
#============================#

sub jump_html{

	local($mes_01)	= $_[0];	# ���b�Z�[�W�������Ƃ��Ď擾
	local($mes_02)	= $_[1];	# ���b�Z�[�W�������Ƃ��Ď擾
	local($cgin01)	= "$cgi_name";
	&output_Content_type; 

	# �ԐM���Ƀy�[�W���L������
	if(($FORM{'page'} ne "")&&($FORM{'bbsaction'} eq "post")&&($FORM{'prebbsaction'} eq "disp_rep_form")){
		$cgin01="$cgin01"."?page=$FORM{'page'}";
# ���X����Ɏ����čs���ݒ�̏ꍇ�X���b�h���擪�֍s���̂ŁA�擪�փW�����v
		if($PM{'res_go_up'} == 1){
			$cgin01="$cgin01"."?page=1";
		}
	}

print<<HTML_END;
<HTML>
<HEAD>
 <TITLE>wait..</TITLE>$top_html_header
 <META HTTP-EQUIV="Refresh" CONTENT="5; URL=$cgin01">
</HEAD>
<BODY BGCOLOR="#D0D0D0">
[Imgboard - Mes]<BR>

 $mes_01 $mes_02 <BR>
$accesskey_p1<a href="$cgi_name?page=$FORM{'page'}&viewpass=$FORM{'viewpass'}" accesskey=0>�f���֖߂�</a>
</BODY>
</HTML>
HTML_END

}


#============================#
# �G���[�̏o��
#============================#

sub error{

	local($error_message)	= $_[0];	# ���b�Z�[�W�������Ƃ��Ď擾
	local($error_message2)	= $_[1];	# ���b�Z�[�W�������Ƃ��Ď擾
	local($lform_action);

	if($keitai_flag eq "imode"){
		$lform_action="$ENV{'HTTP_REFERER'}";
	}elsif($keitai_flag eq "J-PHONE"){
		$lform_action="$cgi_name";
	}else{
		$lform_action="$ENV{'HTTP_REFERER'}";
	}

	&output_Content_type; 


print<<EOF;
<HTML>
<HEAD>
<TITLE>Error</TITLE>
$top_html_header
</HEAD>

<BODY BGCOLOR=\"#D0D0D0">
<CENTER>
from imgbd.<BR>
 [�װ�ł�] 
</CENTER>
<BR>
$error_message<BR>/
$error_message2<BR>
<FORM METHOD="GET" ACTION="$lform_action">
<INPUT TYPE="HIDDEN" NAME="page" VALUE=1>
<INPUT TYPE="SUBMIT" VALUE=" �߂� "> 
</FORM>
</BODY>
</HTML>
EOF

	&rm_tmp_uploaded_files;			# �ꎞ�ۑ����ꂽ�摜�f�[�^���폜
	exit;
}

#===================================#
# �ꎞ�o�^���ꂽ�摜�t�@�C���̍폜
#===================================#
# asx/asf�Ή�(2001.01)
sub rm_tmp_uploaded_files{
	if($img_data_exists==1){
		sleep 1;
		foreach $fname_list(@NEWFNAMES){
			if(-e "$PM{'img_dir'}/$fname_list"){
				unlink("$PM{'img_dir'}/$fname_list");
				# ���^�t�@�C�����폜����
				&rm_meta_file("$PM{'img_dir'}/$fname_list");
			}
			# �g�їp�t�@�C�����폜����
			if($fname_list=~ /\.(jpe?g|gif|png|bmp|mng)$/i){
				  &rm_snl_file("$unq_id","$PM{'img_dir'}","$existing_snl_type_list");
			}
		}
	}
}

#===================================#
# ASX ���^�t�@�C���̍폜 & 3GP�g��
#===================================#
# Winodows Media�̃X�g���[���Đ���eggy�̃X�g���[���Đ��Ή��̂��߂�
# �@�\�g�������B �폜����t�@�C�������^�t�@�C���������Ă�������
# ���O�������烁�^�t�@�C���炵���t�@�C����T���A��������Ώ����Ă���
# 3GP�p�Ɋg��
sub rm_meta_file{

	local($tmp_rm_meta_file)=$_[0]; # �����͍폜����t�@�C�����{�́i�p�X�t���j

	# asx���ɑΉ�
	if($tmp_rm_meta_file=~ /^(.*)\.(asf|wma|wmv?)$/){
	   if(-e "$1\.asx"){
		unlink("$1\.asx");# ASF(�Â��\�L�̎d��)
	   }
	   if(-e "$1\.wvx"){
		unlink("$1\.wvx");# ASF&WinMediaAudio/Video(���݂͂��ꂪ�����炵��)
	   }
	}
	# 3gp/3g2�����^�p�ɑΉ�(�d���t�@�C�����폜)
	if($tmp_rm_meta_file=~ /^(.*)\.3g2$/){
	   if(-e "$1\.3gp"){
		unlink("$1\.3gp");# 3gp
	   }
        }
	if($tmp_rm_meta_file=~ /^(.*)\.3gp$/){
	   if(-e "$1\.3g2"){
		unlink("$1\.3g2");# 3g2
	   }
	}
}
#
#
#=============================#
# �g�їp�t�@�C���̍폜(R7)
#=============================#
#
# �����̑S�g�ёΉ����l���Ċg���q��
# ���낢��ł���悤�ɂ��Ă���
#
sub rm_snl_file{

	local($tmp_rm_snl_unq_id)	=$_[0]; # ����1��UID
	local($tmp_rm_snl_dir)		=$_[1]; # ����2�̓p�X
	local($tmp_rm_snl_exist_type)	=$_[2]; # ����3��SNL���݃��X�g

	local($snl_future_bit);		# �g�їp�t�@�C�����̏����g���r�b�g
	local($snl_ext);		# �g�їp�t�@�C���̎��ۂ̊g���q

	$tmp_rm_snl_unq_id="snl"."$tmp_rm_snl_unq_id";

	 @SNL_TYPE=split(/\//,$tmp_rm_snl_exist_type);

	if($tmp_rm_snl_exist_type ne ""){
	   foreach $snl_type(@SNL_TYPE){
	    	($snl_ext,$snl_future_bit,$dummy)=split(/\-/,$snl_type);
		if(-e "$tmp_rm_snl_dir/$tmp_rm_snl_unq_id$snl_future_bit\.$snl_ext"){
			unlink("$tmp_rm_snl_dir/$tmp_rm_snl_unq_id$snl_future_bit\.$snl_ext");
		}
	   }
	}
}
#
#====================#
# �u���E�U�`�F�b�N
#====================#

sub check_browser_type{

	if($HTTP_USER_AGENT=~ /icab/i){
	  # icab�œ��e����ƃG���[�ɂȂ�̂Ŕr������
	  if($FORM{'bbsaction'} eq 'post'){
	    &error(" �G���[ ���̃u���E�U�ł͋L���̓��e�͂ł��܂��� ");
	  }
	}

	$jstation_flag	="1";	# �X�e�[�V�����A�p�P�b�g�Ή��@�t���O(�i�t�H��)

	# 2004.06.01 add
	$au_3G_flag	="0";	# au_3G����(0=�s��,1�ȏ� au_3G)

	$http_upload_ok_flag	="0";# HTTP�A�b�v���[�h�Ή��t���O(R7 NEW)
	$file_attach_mail	="0";# ���[���ɓY�t�t�@�C���\�@��(R7 NEW)

	# 2010.09 add
	$http_upload_fullb_only_flag="0";# �t���u���E�U�̂݁AHTTP�A�b�v���[�h�Ή��̋@��t���O

	# 2008.06.02 add
	$wmv_play_flag	="0";	# WMV�Ή�����(0=�s��,1�ȏ�Ή�)

	# 2009.12.08 add
	$imode_ver	="1";		# imode Version(0=�s��,1�ȏ�Ή�)
	$cookie_ok_flag	="0";	# cookie(0=�s��,1�ȏ�Ή�)

	# QVGA���� 2004.06.20 add update 2009.12
	$KEITAI_ENV{'DISPLAY_WIDTH'}		="240";
	$KEITAI_ENV{'DISPLAY_HEIGHT'}		="320";

	# 2008.06 WVGA�@�푝���ɂ��d�l�g��
	$qvga_flag	="0";	#(0=qvga�ȉ�;1=qvga;2=wqvga;5=vga;6=wvga; qvga�ȏ�)


	undef @TMP_UA;
# saru

# ����`�F�b�N
#$HTTP_USER_AGENT="DoCoMo/1.0/F504i/c10/TB";
#$HTTP_USER_AGENT="UP.Browser/3.04-SN13 UP.Link/3.3.0.5";
#$HTTP_USER_AGENT="KDDI-HI21 UP.Browser/6.0.2.254(GUI) MMP/1.1";
#$HTTP_USER_AGENT="KDDI-KC3G UP.Browser/6.2.0.14.1 (GUI) MMP/2.01"; #upload NG maybe
#$HTTP_USER_AGENT="KDDI-CA3D UP.Browser/6.2_7.2.7.1.K.3.330 (GUI) MMP/2.0";#upload NG
#$HTTP_USER_AGENT="KDDI-SH38 UP.Browser/6.2_7.2.7.1.K.3.330 (GUI) MMP/2.0";#SH001 upload ok
#$HTTP_USER_AGENT="KDDI-TS3N UP.Browser/6.2_7.2.7.1.K.3.330 (GUI) MMP/2.0";#T001 upload ok
#$HTTP_USER_AGENT="KDDI-TS3O UP.Browser/6.2_7.2.7.1.K.4.182 (GUI) MMP/2.0";# upload ok
#$HTTP_USER_AGENT="KDDI-TS3P UP.Browser/6.2_7.2.7.1.K.4.182 (GUI) MMP/2.0";# upload ok
#$HTTP_USER_AGENT="KDDI-TS3R UP.Browser/6.2_7.2.7.1.K.4.303 (GUI) MMP/2.0";#T003 upload ok
#$HTTP_USER_AGENT="KDDI-SH3E UP.Browser/6.2_7.2.7.1.K.3.350 (GUI) MMP/2.0";#SH004

#$HTTP_USER_AGENT="PDXGW/1.0 (TX=8;TY=7;GX=96;GY=84;C=C256;G=BF;GI=2)";
#$HTTP_USER_AGENT="J-PHONE/2.0/J-SH02";
#$HTTP_USER_AGENT="J-PHONE/4.0/J-SH51/SNxxxxx SH/0001a Profile/MIDP-1.0 Configuration/CLDC-1.0 Ext-Profile/JSCL-1.1.0";
#$HTTP_USER_AGENT="J-PHONE/4.2/J-SH53/SNJSHF1002783 SH/0003aa Profile/MIDP-1.0 Configuration/CLDC-1.0 Ext-Profile/JSCL-1.2.1";
#$HTTP_USER_AGENT="J-PHONE/5.0/V801SA/SN*********** SA/0001JP Profile/MIDP-1.0 Configuration/CLDC-1.0 Ext-Profile/JSCL-1.1.0";
#http://developers.softbankmobile.co.jp/dp/tool_dl/web/useragent.php

#$HTTP_USER_AGENT="Vodafone/1.0/V904SH/SHJ001/SN";
#$HTTP_USER_AGENT="SoftBank/1.0/910T/TJ001/SN";
#$HTTP_USER_AGENT="SoftBank/1.0/911T/TJ001/SN*************** Browser/NetFront/3.3 Profile/MIDP-2.0";
#$HTTP_USER_AGENT="SoftBank/1.0/935SH/SHJ001/SN*************** Browser/NetFront/3.5 Profile/MIDP-2.0 Configuration/CLDC-1.1";

#$HTTP_USER_AGENT="DoCoMo/2.0 F906i(c100;TB)";
#$HTTP_USER_AGENT="DoCo/2.0 F03A(c100;TB;W24H17)";
# imode2.0
#$HTTP_USER_AGENT="DoCoMo/2.0 F03B(c500;TB;W24H16)";
#
# 2008.06.13
# iPod Touch
#$HTTP_USER_AGENT="Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A100a Safari/419.3";
# iPhone
#$HTTP_USER_AGENT="Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1C28 Safari/419.3";
# Wii
#$HTTP_USER_AGENT="Opera/9.10 (Nintendo Wii; U; ; 1621; ja)";
# PSP
#$HTTP_USER_AGENT="Mozilla/4.0 (PSP PlayStation Portable); 2.00)";
# Nintendo DS �u���E�U
#$HTTP_USER_AGENT="Mozilla/4.0 (compatible; MSIE 6.0; Nitro) Opera 8.50 [ja]";
# PlayStation 3
#$HTTP_USER_AGENT="Mozilla/5.0 (PLAYSTATION 3; 1.00)";
# X01HT
#$HTTP_USER_AGENT="Mozilla/5.0 (PDA; NF34PPC/1.0; like Gecko) NetFront/3.4";
# 
#Mozilla/5.0 (Linux; U; Android 1.5; ja-jp; HT-03A Build/CDB72) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1
#HT-03A Android 1.5
#$HTTP_USER_AGENT="Mozilla/5.0 (Linux; U; Android 1.5; ja-jp; HT-03A Build/CDB72) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1";
#HT-03A Android 1.6
#$HTTP_USER_AGENT="Mozilla/5.0 (Linux; U; Android 1.6; ja-jp; Docomo HT-03A Build/DRD08) AppleWebKit/528.5+(KHTML, like Gecko) Version/3.1.2 Mobile Safari/ 525.20.1";



	@TMP_UA = split(/\//,$HTTP_USER_AGENT);


	# FOMA�Ή�(2002.09.25)
	# http://www.nttdocomo.co.jp/service/imode/make/content/spec/useragent/index.html

	if($HTTP_USER_AGENT=~ /DoCoMo\/2\.0\s(\w+)\(c(\d+)/i){

	  $keitai_flag="imode";
	  $KEITAI_ENV{'SERVICE_COMPANY'}	='DoCoMo';
	  $KEITAI_ENV{'HTTP_VERSION'}		='2.0';
	  $KEITAI_ENV{'MACHINE_TYPE'}		="$1";
	  $KEITAI_ENV{'CACHE_SIZE'}		="$2"; # KB(N2001�ȊO��100KB)
	  $KEITAI_ENV{'STREAM_SPEED'}		="";
	  $KEITAI_ENV{'OTHER_PARAM'}		="FOMA";

	  $http_upload_ok_flag	="0";
	  $http_upload_fullb_only_flag="0";# �t���u���E�U�̂݁AHTTP�A�b�v���[�h�Ή��̋@��t���O
	  $file_attach_mail	="1";
	  $handle_data_line	="png-jpeg-gif";

	  # QVGA���� 2004.06.20 update
	  if($KEITAI_ENV{'MACHINE_TYPE'}=~ /9..i/i){
		$KEITAI_ENV{'DISPLAY_WIDTH'}		="240";
		$KEITAI_ENV{'DISPLAY_HEIGHT'}		="320";
	  }

	  # 2007,2008�N
	  if($KEITAI_ENV{'MACHINE_TYPE'}=~ /90[5|6]i/i){

		$KEITAI_ENV{'DISPLAY_WIDTH'}		="480";

		if($KEITAI_ENV{'MACHINE_TYPE'}=~ /(D90|SO90|F90)/i){
		    $KEITAI_ENV{'DISPLAY_HEIGHT'}		="864";
		}else{
		    $KEITAI_ENV{'DISPLAY_HEIGHT'}		="854";
		}
		$qvga_flag	="6";	#(0=qvga�ȉ�;1=qvga;2=wqvga;5=vga;6=wvga; qvga�ȏ�)

	  # 706i�V���[�Y
	  }elsif($KEITAI_ENV{'MACHINE_TYPE'}=~ /SH706i/i){
	  
		$KEITAI_ENV{'DISPLAY_WIDTH'}		="480";
		$KEITAI_ENV{'DISPLAY_HEIGHT'}		="854";
		$qvga_flag	="6";	#(0=qvga�ȉ�;1=qvga;2=wqvga;5=vga;6=wvga; qvga�ȏ�)
	  }elsif($KEITAI_ENV{'MACHINE_TYPE'}=~ /706i/i){
		$KEITAI_ENV{'DISPLAY_WIDTH'}		="240";
		$KEITAI_ENV{'DISPLAY_HEIGHT'}		="400";
		$qvga_flag	="2";	#(0=qvga�ȉ�;1=qvga;2=wqvga;5=vga;6=wvga; qvga�ȏ�)
	  # 2008,2009�N
	  }elsif($KEITAI_ENV{'MACHINE_TYPE'}=~ /[A-Z]+(\d+)[A|B|C|D|E]/i){

	    $http_upload_ok_flag	="1";
	    $wmv_play_flag		="1";

	    # 70Xi������QVGA 2010.09fix bug 
	    if($KEITAI_ENV{'MACHINE_TYPE'}=~ /^(N03A|P03A|P03B|F07A|F10A|L01A|L03A|L03B|L04B|N05A|N06B|P04A|P05A|P05B|P06A|P06B|P10A|F05A)/i){
		$KEITAI_ENV{'DISPLAY_WIDTH'}		="240";
		$KEITAI_ENV{'DISPLAY_HEIGHT'}		="320";
		$qvga_flag	="1";	#(0=qvga�ȉ�;1=qvga;2=wqvga;5=vga;6=wvga; qvga�ȏ�)
	    }else{
	    # last update 2010.09.23
	    # N-08B���������L�[�{�[�h�t���ŏc�����΂��B�ǂ����悤���B
	    
		 $KEITAI_ENV{'DISPLAY_WIDTH'}		="480";
	 	 $top_html_header	="<meta name=\"disparea\" content=\"vga\">";

		 if($KEITAI_ENV{'MACHINE_TYPE'}=~ /^(F01A|F06A)/i){
		    $KEITAI_ENV{'DISPLAY_HEIGHT'}		="864";
		 }elsif($KEITAI_ENV{'MACHINE_TYPE'}=~ /^(F01B|F09A|F03A|F04B|F06B)/i){
		    $KEITAI_ENV{'DISPLAY_HEIGHT'}		="960";
		 }elsif($KEITAI_ENV{'MACHINE_TYPE'}=~ /^(L..A|L..B|L..C|F09B)/i){
		    $KEITAI_ENV{'DISPLAY_HEIGHT'}		="800";
		 }elsif($KEITAI_ENV{'MACHINE_TYPE'}=~ /^(F02A|F04A|SH..A|SH..B|N..A|N..B|F02B|F03B|F08A|F08B)/i){
		    $KEITAI_ENV{'DISPLAY_HEIGHT'}		="854";
		 }else{
		    $KEITAI_ENV{'DISPLAY_HEIGHT'}		="854";
		 }
		 $qvga_flag	="6";	#(0=qvga�ȉ�;1=qvga;2=wqvga;5=vga;6=wvga; qvga�ȏ�)
	    }
	  }


	  # 2008.06 FOMA 906i�̓���E�摜2MB�A�b�v���[�h�Ή��ɑΏ�
	  # imode CHTML7.2�ȍ~�̓A�b�v�ł���
	  if($KEITAI_ENV{'MACHINE_TYPE'}=~ /906i/i){
	    $http_upload_ok_flag	="1";
	    $wmv_play_flag			="1";
	  }

	  # 2008.06 FOMA 706i�̈ꕔ�̓���E�摜2MB�A�b�v���[�h�Ή��ɑΏ�
	  # imode CHTML7.2�ȍ~�̓A�b�v�ł���
	  if($KEITAI_ENV{'MACHINE_TYPE'}=~ /(F706|SH706|P706)i/i){
	    $http_upload_ok_flag	="1";
	  }
	  if($KEITAI_ENV{'MACHINE_TYPE'}=~ /(SH706|P706)i/i){
	    $wmv_play_flag			="1";
	  }

	  # 2010.09 imode1.0��XHTML2.3�@��Ώ�
	  if($KEITAI_ENV{'MACHINE_TYPE'}=~ /(F09B|SH0.A|N01A|N02A|N04A|P0.A|P10A|F0.A)i/i){
	    $http_upload_ok_flag	="1";
	  }

	  # Cache500KB�ȍ~�͑S�@��UPLOAD�Ή����낤
	  if($KEITAI_ENV{'CACHE_SIZE'} >= 500){
	    $imode_ver	="2";	# imode Version(0=�s��,1�ȏ�Ή�)
	  }

	  if($imode_ver >= 2){
	    $http_upload_ok_flag	="1";
	    $wmv_play_flag		="1";
		$cookie_ok_flag	="1";# cookie ok	    
	  }

	# 2010.09 �t���u���E�U�֗U������ׂ��@������o
	  # �t���u���E�U����
	  if($KEITAI_ENV{'MACHINE_TYPE'}=~ /(904|905|704|705|706)i/i){
	   #HTTP�A�b�v���[�h�s�̂���
	   if($http_upload_ok_flag != 1){
		  $http_upload_fullb_only_flag="1";   
	   }
	  }

	  # P705i,PROSOLID,P903iX,SH905i,P905i�̓t���u���E�U�̂�WMV�Ȃ̂Ŋ֌W�Ȃ���
	  if($KEITAI_ENV{'MACHINE_TYPE'}=~ /(P705i|PROSOLID|P903iX|SH905i|P905i)/i){
	    $wmv_play_flag			="1";
	  }


	}elsif($TMP_UA[0]=~ /^DoCoMo/i){ # 2010.01.23update

	  $keitai_flag="imode";
	  $KEITAI_ENV{'SERVICE_COMPANY'}	=$TMP_UA[0];
	  $KEITAI_ENV{'HTTP_VERSION'}		=$TMP_UA[1];
	  $KEITAI_ENV{'MACHINE_TYPE'}		=$TMP_UA[2];
	  $KEITAI_ENV{'CACHE_SIZE'}		=$TMP_UA[3];
	  $KEITAI_ENV{'STREAM_SPEED'}		=$TMP_UA[4];
	  $KEITAI_ENV{'OTHER_PARAM'}		=$TMP_UA[5];

	  $KEITAI_ENV{'CACHE_SIZE'}		=~ s/c//ig;#c������

	  if($KEITAI_ENV{'CACHE_SIZE'} eq ""){
	    $KEITAI_ENV{'CACHE_SIZE'}		=5; # 501�̎��̓L���b�V����5KB
	  }

	  # 2002.12 i-shot���ʂ�ǉ�(2009.12�C��)
	  if($KEITAI_ENV{'MACHINE_TYPE'}=~ /504iS|505i|506i|25.i|270./i){
		$ishot_flag=1;
	  }

	  # QVGA���� 2004.06.20 update 2009.12 PDC(504 after)=QVGA ni shita
		$KEITAI_ENV{'DISPLAY_WIDTH'}		="240";
		$KEITAI_ENV{'DISPLAY_HEIGHT'}		="320";

	  $http_upload_ok_flag	="0";
	  $file_attach_mail	="0";
	  $handle_data_line	="gif";

	  $cookie_ok_flag	="0";# cookie NG	    

	# 2009.12 update 2008.03 HDML service haishi wo hanei
	}elsif($TMP_UA[0]=~ /^KDDI/i){ #2010.01.23

		# �u���E�U��/�u���E�U�o�[�W����-�f�o�C�XID UP.Link/UP.Link�o�[�W����
		# KDDI-HI21 UP.Browser/6.0.2.252(GUI) MMP/1.1   # EZ������(���@)

		$keitai_flag="imode";
		$au_3G_flag	="1";	# au_3G����(0=�s��,1�ȏ� au_3G)
		$KEITAI_ENV{'CACHE_SIZE'}=10; # html 10KB IMG 30KB total 50KB

#		$http_upload_ok_flag	="1";	# �ǂ����ł���炵��
		$http_upload_ok_flag	="0";	# �ǂ����ł��Ȃ��炵��

		if($TMP_UA[0]=~ /KDDI\-(..)(.*)7\.2(.*)\.K/i){
		  if($1 eq "TS"){
			$http_upload_ok_flag	="1";	# �ǂ����ł���炵��
		  }elsif($1 eq "SH"){
			$http_upload_ok_flag	="1";	# �ǂ����ł���炵��
		  }
		}

		$file_attach_mail	="1";	# ���ݔ̔�����Ă�����̂͑S�@��n�j

		local($tmp_ez_mc);
		local($tmp_ez_cc);
		if($TMP_UA[0]=~ /^(KDDI)\-(..)(.)(.+)\s(.*)$/i){
			$tmp_ez_mc = $2;# �@��R�[�h
			$tmp_ez_cc = $3;# �L�����A�R�[�h
		}elsif($TMP_UA[0]=~ /^(..)(.)(.+)\s(.*)$/i){
			$tmp_ez_mc = $1;# �@��R�[�h
			$tmp_ez_cc = $2;# �L�����A�R�[�h
		}
		$KEITAI_ENV{'DISPLAY_WIDTH'}		="240";
		$KEITAI_ENV{'DISPLAY_HEIGHT'}		="348";

	  # 2004.06.20 QVGA���� (���ϐ��ɂ�鎩������) 2009.12 update
	  if($ENV{'HTTP_X_UP_DEVCAP_SCREENPIXELS'}=~ /(\d+)\,(\d+)/){
		if(($1 > 110)&&($2 > 150)){# 0,0 mo aru
	  	 $KEITAI_ENV{'DISPLAY_WIDTH'}		="$1";
	  	 $KEITAI_ENV{'DISPLAY_HEIGHT'}		="$2";
	  	}
	  }

	  # 2010.01.25 CACHE���� (���ϐ��ɂ�鎩������)
	  if($ENV{'HTTP_X_UP_DEVCAP_MAX_PDU'}=~ /(\d+)/){
		if($1 > 10000){
		 $KEITAI_ENV{'CACHE_SIZE'}=int($1/1000); 
	  	}
	  }
	  
# http://www.au.kddi.com/ezfactory/tec/spec/4_4.html

	  # �@��R�[�h
	   if($tmp_ez_mc eq "SY"){
	   	$KEITAI_ENV{'MACHINE_TYPE'}="3G_SANYO";
	   }elsif($tmp_ez_mc eq "CA"){
	   	$KEITAI_ENV{'MACHINE_TYPE'}="3G_CASIO";
	   }elsif($tmp_ez_mc eq "TS"){
	   	$KEITAI_ENV{'MACHINE_TYPE'}="3G_����";
	   }elsif($tmp_ez_mc eq "HI"){
	   	$KEITAI_ENV{'MACHINE_TYPE'}="3G_����";
	   }elsif($tmp_ez_mc eq "MA"){
	   	$KEITAI_ENV{'MACHINE_TYPE'}="3G_����";
	   }else{
	   	$KEITAI_ENV{'MACHINE_TYPE'}="3G_";
	   }

	   $KEITAI_ENV{'SERVICE_COMPANY'}="au";
	   $KEITAI_ENV{'HTTP_VERSION'}=$TMP_UA[2];

	   $KEITAI_ENV{'MACHINE_TYPE'}="$KEITAI_ENV{'SERVICE_COMPANY'}"."-"."$KEITAI_ENV{'MACHINE_TYPE'}"."-"."WAP"."2.0";

#	$ENV{'HTTP_X_UP_SUBNO'}="0123456789_c7.ezweb.ne.jp";

	  # i�N�b�L�[�p�̔ԍ����T�u�X�N���C�o�[ID���쐬
	  $KEITAI_ENV{'UP_SUBNO'}=$ENV{'HTTP_X_UP_SUBNO'};
	  # 0123456789_c7.ezweb.ne.jp �̂悤�Ȍ`��������
	  if($ENV{'HTTP_X_UP_SUBNO'}=~ /^.+(\d{4,4})_/i){
	  	$KEITAI_ENV{'UP_SHORT_SUBNO'}=$1;
		$KEITAI_ENV{'SERIAL_SHORT'}=$1;
		$KEITAI_ENV{'SERIAL_LONG'}=$ENV{'HTTP_X_UP_SUBNO'};
	  }else{
#	  	$KEITAI_ENV{'MACHINE_TYPE'}="UP.sim";
	  }

		$cookie_ok_flag	="1";# cookie ok	    

	# 2007.05�C��
  	}elsif($TMP_UA[0]=~ /^J-PHONE/i){

		# http://developers.softbankmobile.co.jp/dp/
	  	$keitai_flag="J-PHONE";
	  	$KEITAI_ENV{'MACHINE_TYPE'}=$ENV{'HTTP_X_JPHONE_MSNAME'};

		# 2004.06.20 QVGA���� (���ϐ��ɂ�鎩������)
		if($ENV{'HTTP_X_JPHONE_DISPLAY'}=~ /(\d+)\*(\d+)/){
		 if(($1 > 110)&&($2 > 150)){# 0,0 mo aru
		  $KEITAI_ENV{'DISPLAY_WIDTH'}		="$1";
		  $KEITAI_ENV{'DISPLAY_HEIGHT'}		="$2";
		 }
		}

		$http_upload_ok_flag	="0";	# ��{�I�ɂł��Ȃ�
	  	$file_attach_mail	="1";	# ��{�I�ɂł���

	  	$KEITAI_ENV{'SERVICE_COMPANY'}=$TMP_UA[0];
	  	$KEITAI_ENV{'HTTP_VERSION'}=$TMP_UA[1];
	  	$KEITAI_ENV{'OTHER_PARAM'}=$TMP_UA[3];
	   	if($KEITAI_ENV{'HTTP_VERSION'} >= 4){
			# �p�P�b�g�Ή��@
			# 2009.12update
			if($KEITAI_ENV{'HTTP_VERSION'} >= 5.0){
				# W type
				$jstation_flag="5";
				$KEITAI_ENV{'CACHE_SIZE'}='200';
				$cookie_ok_flag	="1";# cookie ok	    
			}elsif($KEITAI_ENV{'HTTP_VERSION'} >= 4.3){
				# P2 type
				$jstation_flag="4.3";
				$KEITAI_ENV{'CACHE_SIZE'}='30';
			}else{
				# P1 type
				$jstation_flag="4";
				$KEITAI_ENV{'CACHE_SIZE'}='12';
			}
			$handle_data_line	="png-jpeg-gif";

			# i�N�b�L�[�p�̔ԍ����V���A���ԍ����쐬
	  		# SNXXXXXXXXX SH �̂悤�Ȍ`��������
	  		if($KEITAI_ENV{'OTHER_PARAM'} =~ /^SN(.+)(\d{4,4})\s/i){
	  			$KEITAI_ENV{'SERIAL_LONG'}="$1"."$2";
	  			$KEITAI_ENV{'SERIAL_SHORT'}=$2;
	  		}

			$http_upload_ok_flag	="1"; # 51�n�͒��ڃA�b�v�\

#&error("aagg-$KEITAI_ENV{'SERIAL_LONG'}-$KEITAI_ENV{'SERIAL_SHORT'}");

		}elsif($KEITAI_ENV{'HTTP_VERSION'} >= 3){
			# �X�e�[�V�����Ή��@ C3 type
			$jstation_flag="3";
			$KEITAI_ENV{'CACHE_SIZE'}='6';
			$handle_data_line	="png-jpeg";
		}
  	}elsif($TMP_UA[0]=~ /^Vodafone|^SoftBank/i){

		# http://developers.softbankmobile.co.jp/dp/
	  	$keitai_flag="J-PHONE";
	  	$KEITAI_ENV{'MACHINE_TYPE'}=$ENV{'HTTP_X_JPHONE_MSNAME'};

		# 2004.06.20 QVGA���� (���ϐ��ɂ�鎩������)
		if($ENV{'HTTP_X_JPHONE_DISPLAY'}=~ /(\d+)\*(\d+)/){
		 if(($1 > 110)&&($2 > 150)){# 0,0 mo aru		
		  $KEITAI_ENV{'DISPLAY_WIDTH'}		="$1";
		  $KEITAI_ENV{'DISPLAY_HEIGHT'}		="$2";
		 }
		}
		# �v����
		$http_upload_ok_flag	="1";	# ��{�I�ɂł���
	  	$file_attach_mail	="1";	# ��{�I�ɂł���

	  	$KEITAI_ENV{'SERVICE_COMPANY'}=$TMP_UA[0];
	  	$KEITAI_ENV{'HTTP_VERSION'}=$TMP_UA[1];
	  	$KEITAI_ENV{'OTHER_PARAM'}=$TMP_UA[3];

		$jstation_flag="6";
		# 2009.12 update
		$KEITAI_ENV{'CACHE_SIZE'}='300';
		$handle_data_line	="png-jpeg-gif";

		$cookie_ok_flag	="1";# cookie ok	    

		# i�N�b�L�[�p�̔ԍ����V���A���ԍ����쐬
  		# SNXXXXXXXXX SH �̂悤�Ȍ`��������
  		if($KEITAI_ENV{'OTHER_PARAM'} =~ /^SN(.+)(\d{4,4})\s/i){
  			$KEITAI_ENV{'SERIAL_LONG'}="$1"."$2";
  			$KEITAI_ENV{'SERIAL_SHORT'}=$2;
  		}

	}elsif($HTTP_USER_AGENT=~ /iPhone|iPod|iPad/i){

#iPod
#Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A100a Safari/419.3

#iPhone
#Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1C28 Safari/419.3

	  	$keitai_flag="pc";
	  	$http_upload_ok_flag	="1";
	  	$file_attach_mail	="1";
	  	$handle_data_line	="jpeg-gif-png-bmp";

		$cookie_ok_flag	="1";# cookie ok	    

	  	$top_html_header	="<meta name=\"viewport\" content=\"width=480, maximum-scale=1.0, minimum-scale=0.5, \">";

	  	
	  	if($TMP_UA[0]=~ /iPod/i){
	  		$KEITAI_ENV{'MACHINE_TYPE'}='iPod';
		}elsif($TMP_UA[0]=~ /iPhone/i){
	  		$KEITAI_ENV{'MACHINE_TYPE'}='iPhone';
		  	$KEITAI_ENV{'SERVICE_COMPANY'}='Softbank';
		}elsif($TMP_UA[0]=~ /iPad/i){
	  		$KEITAI_ENV{'MACHINE_TYPE'}='iPad';
#		  	$KEITAI_ENV{'SERVICE_COMPANY'}='Softbank';
			$top_html_header	="<meta name=\"viewport\" content=\"width=640\">";
		}else{
	  		$KEITAI_ENV{'MACHINE_TYPE'}='iPhone';
		}

	# 2012.09 iOS6�ȍ~���o
	if($HTTP_USER_AGENT=~ /iPhone|iPod|iPad/i){
		$MYCGI_ENV{'iOS'}='true';
		if($HTTP_USER_AGENT=~ /OS (\d)\_(\d)/i){
			$MYCGI_ENV{'iOS_VER'}=$1;
		}else{
			$MYCGI_ENV{'iOS_VER'}=3;
		}
	}else{
		$MYCGI_ENV{'iOS'}='false';
	}


	  $KEITAI_ENV{'CACHE_SIZE'}='300';

	  # 2012.10 �C��
	  $qvga_flag	="6";	#(0=qvga�ȉ�;1=qvga;2=wqvga;5=vga;6=wvga; qvga�ȏ�)
	  $KEITAI_ENV{'DISPLAY_WIDTH'}		="640";
	  $KEITAI_ENV{'DISPLAY_HEIGHT'}		="960";

	}elsif($HTTP_USER_AGENT=~ /Android/i){

#HT-03A Android 1.5
#$HTTP_USER_AGENT="Mozilla/5.0 (Linux; U; Android 1.5; ja-jp; HT-03A Build/CDB72) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1";
#HT-03A Android 1.6
#$HTTP_USER_AGENT="Mozilla/5.0 (Linux; U; Android 1.6; ja-jp; Docomo HT-03A Build/DRD08) AppleWebKit/528.5+(KHTML, like Gecko) Version/3.1.2 Mobile Safari/ 525.20.1";

	  	$keitai_flag="pc";
	  	$http_upload_ok_flag	="1";
	  	$file_attach_mail	="1";
	  	$handle_data_line	="jpeg-gif-png-bmp";

		$cookie_ok_flag	="1";# cookie ok	    

		# safari������
	  	$top_html_header	="<meta name=\"viewport\" content=\"width=480\">";

	  	
	  	if($TMP_UA[0]=~ /Android (\d+)/i){
	  		$KEITAI_ENV{'MACHINE_TYPE'}="Android"."$1";
			if($TMP_UA[0]=~ /docomo/i){
		  		$KEITAI_ENV{'SERVICE_COMPANY'}='docomo';
			}
		}

	  $KEITAI_ENV{'CACHE_SIZE'}='300';

	  # 2008.06 �C��
	  $qvga_flag	="6";	#(0=qvga�ȉ�;1=qvga;2=wqvga;5=vga;6=wvga; qvga�ȏ�)
	  $KEITAI_ENV{'DISPLAY_WIDTH'}		="480";
	  $KEITAI_ENV{'DISPLAY_HEIGHT'}		="640";

	}else{
	  # PC
	  $keitai_flag="pc";
	  $http_upload_ok_flag	="1";
	  $file_attach_mail	="1";
	  $handle_data_line	="jpeg-gif-png-bmp";
	  $KEITAI_ENV{'CACHE_SIZE'}='100';
# 	  $KEITAI_ENV{'DISPLAY_WIDTH'}		="240";
#	  $KEITAI_ENV{'DISPLAY_HEIGHT'}		="320";
	  $cookie_ok_flag	="1";# cookie ok	    

	  # �X�}�[�g�t�H���΍� 2010.04
	  $top_html_header	="<meta name=\"viewport\" content=\"width=480\">";

	  # 2008.06 �C��
	  $qvga_flag	="6";	#(0=qvga�ȉ�;1=qvga;2=wqvga;5=vga;6=wvga; qvga�ȏ�)
	  $KEITAI_ENV{'DISPLAY_WIDTH'}		="480";
	  $KEITAI_ENV{'DISPLAY_HEIGHT'}		="854";
	  
	}

	# ���ϐ����󂯂Ă̏���
	if(($KEITAI_ENV{'DISPLAY_WIDTH'} >= 222)&&($qvga_flag == 0)){
	    $qvga_flag	="1";
	}

	# �f�o�b�N�p�Ɍg�уt���O�������Z�b�g����
	# imode,J-PHONE,FOMA���w��APC���[�h������pc���w��
	if($debug_mode >= 3){
	  if($PM{'keitai_force_set'} ne ""){
		if($PM{'keitai_force_set'} eq "FOMA"){
			$keitai_flag="imode";
			$KEITAI_ENV{'MACHINE_TYPE'}="P2101V";
		}else{
			$keitai_flag="$PM{'keitai_force_set'}";
		}
	  }
	  if($PM{'keitai_force_set'} eq "pc"){
		$keitai_flag="pc";
	  }
	}

#$keitai_flag="imode";
#$KEITAI_ENV{'MACHINE_TYPE'}="251i";


	# �e�g�ѕʂ̕ϐ�������Ă���
	# imode
	if($keitai_flag eq "imode"){
		$form_method="POST";
		$accesskey_p1=qq|[0].|;
		$HR=qq|<HR>|;

	# J-PHONE
	}elsif($keitai_flag eq "J-PHONE"){
	   if($jstation_flag >= 3){
		# �X�e�[�V�����Ή��@,�p�P�b�g�Ή��@
		$form_method="POST";
	   }else{
		# J�X�J�C�Ή��@
		$form_method="GET";
	   }
	   $HR=qq|<HR>|;
	# PC
	}else{
		$form_method="POST";
		$accesskey_p1=qq|[0].|;
		$HR=qq|<HR>|;
		if($PM{'no_view_from_pc'}== 1){
			&error(" �x�� <BR> ����URL�͌g�т���̃A�N�Z�X��p�ł��B�p\�\\�R\��������ȊO�̎�i����A�N�Z�X�����ꍇ�́A<a href=\"$PM{'cgi_hontai_name'}\">imgboard�{��($PM{'cgi_hontai_name'})</a>�̃A�N�Z�XURL���Ǘ��҂ɋ����Ă��炢�A�������͂��ăA�N�Z�X���Ă������� ");
		}
	}


}

#====================#
# �v���o�C�_�`�F�b�N
#====================#

sub check_ISP{

	if($SERVER_NAME=~ /bekkoame\./){
		&error(" CGI�ݒ�G���[�Bimgboard���T�|�[�g�O�T�C�g�����o���܂����B<BR>�u$SERVER_NAME�v�́ACGI�Ɋւ��ē���Ȑ��񂪂��邽�߁A�c�O�Ȃ���imgboard�𗘗p���邱�Ƃ��ł��܂���B���̃v���o�C�_�������p�������� ");
	}

	if(($SERVER_NAME=~ /hi\-ho\.ne\.jp/)||($SERVER_NAME=~ /\.nifty\.com/)){
	# img_url�ݒ肪�K�v�ȃT�C�g�Őݒ肪���ݒ�̏ꍇ�͌x�����o��
		if($PM{'img_url'} eq 'http://���Ȃ��̃v���o�C�_/���Ȃ��̃f�B���N�g��/img-box'){
			&error(" CGI�ݒ�ɃG���[������܂��B<BR>���Ȃ����ݒu���悤�Ƃ��Ă���v���o�C�_
			�u $SERVER_NAME �v�ł͓���Ȑݒ肪�K�v�ɂȂ�܂��B�VFAQ�f�����Q�Ƃ��āA�����ݒ肵�Ă������� ");
		}
	}

	if($SERVER_NAME=~ /www5.\.biglobe/){
	# img_url�ݒ肪�K�v�ȃT�C�g�Őݒ肪���ݒ�̏ꍇ�͌x�����o��
		if($PM{'img_url'} eq 'http://���Ȃ��̃v���o�C�_/���Ȃ��̃f�B���N�g��/img-box'){
			&error(" CGI�ݒ�ɃG���[������܂��B<BR>���Ȃ����ݒu���悤�Ƃ��Ă���v���o�C�_
			�u $SERVER_NAME �v�ł́�img_url�̐ݒ肪�K�v�ɂȂ�܂��B�����ݒ肵�Ă��������B
			�Ȃ��A�ݒ���@���킩��Ȃ��ꍇ�̓T�|�[�g�f���̉ߋ����O���Q�Ƃ��Ă������� ");
		}
	}

}


#====================#
# Apache1.3.x�΍�
#====================#

sub check_RH{
	if(($REMOTE_HOST eq "")||($REMOTE_HOST =~ /^null$/i)){
	    $REMOTE_HOST = "$ENV{'REMOTE_ADDR'}";
	}

	# 1.22 Rev4 �C�^�Y�����e�h�~��
	# �����[�g�z�X�g���Ȃ��ꍇ�͓o�^�����Ȃ��B���b�Z�[�W�̓_�~�[

	if(($REMOTE_HOST eq "")&&($PM{'no_upload_by_no_RH_user'}=='1')){
	    &error("CGI�G���[ No REMOTE_HOST <BR>���݁A�����[�g�z�X�g��񂪂Ȃ��ꍇ�́A���e�ł��Ȃ��ݒ�ɂȂ��Ă��܂��B ");
	}
}

#================================#
# �A�����e���� ���C��(1.22 Rev4)
#================================#

sub limit_upload_times{
	if($PM{'limit_upload_times_flag'}==1){
		# �A�����e�J�E���^�����s
		# $new_utc_set�̓N�b�L�[�ɐݒ肳���B
		# �����͐ݒ蕔�Őݒ�B�f�t�H���g�l�����̂ŋ�ł������B
		$new_utc_set=&count_upload_times("$PM{'upload_limit_type'}","$PM{'upload_limit_times'}");
	}
}
#
#================================#
# �A�����e���� �T�u(1.22 Rev4)
#================================#

sub count_upload_times{

	# �A�����e�J�E���^
	# �����͎��������W�A������
	# �Ԓl�͐V�J�E���^�Z�b�g�l,�O���[�o���ϐ���$now_up_counter�Ɍ��݂̘A����

	#������
	local($PM{'upload_limit_type'})	= $_[0];	# ���������W�������Ƃ��Ď擾
	local($PM{'upload_limit_times'})	= $_[1];	# �����񐔂������Ƃ��Ď擾
	local($tmp_up_counter);

	# �f�t�H���g�l���Z�b�g
	$PM{'upload_limit_type'}="2min" if($PM{'upload_limit_type'} eq "");
	$PM{'upload_limit_times'}="5" if($PM{'upload_limit_times'} eq "");

	local(@NOWTIME)	= localtime(time);
	local($yday)		= $NOWTIME[7];

	# �����f�[�^����^�C���x�[�X�i���o�[�����
	if($PM{'upload_limit_type'} eq "day"){		# 1��������H��Ő���
		$up_base_num=35+$yday;
	}elsif($PM{'upload_limit_type'} eq "1hour"){	# 1���ԓ�����H��Ő���
		$up_base_num=35+$yday+$hour;
	}elsif($PM{'upload_limit_type'} eq "10min"){	# 10��������H��Ő���
		$up_base_num=35+$yday+(int(($min+1)/10));
	}elsif($PM{'upload_limit_type'} eq "2min"){	# 2��������H��Ő���
		$up_base_num=35+$yday+(int(($min+1)/2));
	}elsif($PM{'upload_limit_type'} eq "1min"){	# 1��������H��Ő���
		$up_base_num=35+$yday+(int(($min+1)/1));
	}else{						# �f�t�H���g��2��	
		$up_base_num=35+$yday+(int(($min+1)/2));
	}

	if($COOKIE{'utc'} eq ""){
		# �N�b�L�[�̒l���Ȃ��ꍇ�̓Z�b�g
		$tmp_up_counter=$up_base_num;
		$now_up_counter=1;

		return($tmp_up_counter);
	}else{
		$tmp_up_counter=$COOKIE{'utc'};	# �N�b�L�[����J�E���^�l��ǂ�
	}		

	# �G���[�`�F�b�N
	if($tmp_up_counter=~ /^(\d+)$/){
		# �Ȃɂ����Ȃ�
	}else{
		# �O���邢�́A�����ȊO�ُ̈�l�ɂȂ��Ă���ꍇ���Z�b�g����
		$tmp_up_counter=$up_base_num;
		# ������N�b�L�[�ɃZ�b�g����
		return($tmp_up_counter);
	}
	return(1) if($up_base_num==0);		# �O���Z�\�h(�ʏ�͂Ȃ�)

#&error("up base $up_base_num yday $yday utc $COOKIE{'utc'} tmp_up $tmp_up_counter");

	# ���C������
	if(($tmp_up_counter % $up_base_num)==0){
		# �^�C���x�[�X����v����ꍇ�̓J�E���g�A�b�v����
		$tmp_up_counter+=$up_base_num;
		$now_up_counter=int($tmp_up_counter/$up_base_num);
		if($now_up_counter > $PM{'upload_limit_times'}){
			&error(" CGI�G���[ overtimes �f���Ǘ��҂��ݒ肵���A�����e
�񐔂��I�[�o�[���܂����B<BR>���΂炭�������݂ł��܂��� ");
			exit;
		}
	}else{
		# �^�C���x�[�X����v���Ȃ��ꍇ�̓J�E���^�����Z�b�g���A�V�^�C���y�[�X��ݒ�
		$tmp_up_counter=$up_base_num;
		$now_up_counter=1;
	}
	# ������N�b�L�[�ɃZ�b�g����
	return($tmp_up_counter);
}
#
#===================================#
# �v���o�C�_��OS�𔻒肷��
#===================================#
# �����Ȃ��A�Ԓl�͂n�r�̎��(win,mac)
# Perl for Win�͐V����OS(NT SP4,Windows2000��)�����o
# �ł��Ȃ��o�O������ ���̂��߁A�����ȃq���g����A
# Windows�ł��邱�Ƃ����o������̂Ƃ���B�Ȃ��A����
# �I�ɐݒ肷�邱�Ƃ��ł���悤�ɂ���B�����̃t���O
# ��binmode�ؑւ��⃁�[�������ŗp����B
sub check_www_server_os{

	local($tmp_www_server_os)="";

	# ���O�����i�G���[�`�F�b�N�j
	$tmp_www_server_os= $^O;

	# Win98 & NT4(SP4)�΍�
	if($tmp_www_server_os eq ""){
		$tmp_www_server_os= $ENV{'OS'};
	}

	# AnHTTPd /OmniHTTPd/IIS�΍�
	if($ENV{'SERVER_SOFTWARE'} =~ /AnWeb|Omni|IIS\//i){
		$tmp_www_server_os= 'win';
	}

	# Win Apache �΍�
	if($ENV{'WINDIR'} ne ""){
		$tmp_www_server_os= 'win';
	}

	# Perl���VOS�����m�ł��Ȃ��ꍇ,�����I�Ɏw�肷��
	if($force_www_server_os_to =~ /win/i){
		$tmp_www_server_os = 'win';
	}elsif($force_www_server_os_to =~ /mac/i){
		$tmp_www_server_os = 'mac';
	}
	return($tmp_www_server_os);
}
#
#==================================#
# ����URL�����N�@�\ Ver0.99(R5 NEW)
#==================================#
#
sub set_auto_url_link{

	# �����P�͏����������f�[�^;
	# �Ԓl�͏�����̃f�[�^;
	local($tmp_data)=@_;
	local($tmp_yb_url)="";
	local($no_object_to_text_link)=0;# OBJECT���e�L�X�g�����N�ɂ��邩�ǂ���
	local($no_iframe_to_text_link)=0;# iframe���e�L�X�g�����N�ɂ��邩�ǂ��� 2011.06
	local($tmp_youtube_snl_url)="";

	# �A���J�[�^�O���������[�U�Ȃ玩�������N���I�t�ɂ���
	# �Ȃ��ꍇ�̂ݏ���
	$PM{'auto_mail_find'}=1;

	 # youTube�΍� 2010.11.29�C��
	 if($tmp_data=~ /<object(.|\n)*<embed(.|\n)*application\/x-shockwave-flash/i){
	  if($tmp_data=~ /<object(.|\n)*<embed(.|\n)*src=(\")?(http\:\/\/)([^\"]*)?(.|\n)*/i){
		$tmp_yb_url="$4"."$5";

		# Flash�̍Đ��ł��Ȃ�iPhone���́Aflash�p�̖�����URL��u��������K�v������
		if($HTTP_USER_AGENT=~ /iPhone|iPod|iPad|PSP|Android 1\./i){
					$tmp_yb_url=~ s/(http\:\/\/www\.ustream\.tv\/flash\/video\/)(\_a-f0-9)*/http\:\/\/www\.ustream\.tv\/recorded\/$2/ig;
		}

		# 2008.07 fix bug
		$tmp_data =~ s/\<(\s*)OBJECT(.|\n)*(\/OBJECT\>)(\s*)(\n?)/$tmp_yb_url /ig;

		# �]�v�Ȃ��̂��t�B���^
		$tmp_data =~ s/(https?\:\/\/www\.dailymotion\.com\/swf\/video\/)(\S*)(\?)(\S)*/$1$2/i;

		# 2008.04 youtube jp mobile�Ή�
		# http://m.jp.youtube.com/details?v=589Mvlz6LWE
		# http://www.youtube.com/v/589Mvlz6LWE&hl=en
		# http://jp.youtube.com/watch?v=589Mvlz6LWE

		# 2008.05 �ԑgID�� _ ���܂܂��Ǝ����ł��Ȃ������_���C��
		 if($tmp_data=~ /http\:\/\/www\.youtube\.com\/v\//i){
		    if(($KEITAI_ENV{'MACHINE_TYPE'} eq "iPod")||($KEITAI_ENV{'MACHINE_TYPE'} eq "iPhone")||($HTTP_USER_AGENT=~ /android/i)){
#			$tmp_data =~ s/http\:\/\/www\.youtube\.com\/v\/([\-_\.a-zA-Z0-9]+)(\&*)([\-_\a-zA-Z0-9\/\?\&\=\%\n]*)/http\:\/\/www\.youtubemp4\.com\/video\/$1\.mp4 <BR>/ig;
			$tmp_data =~ s/http\:\/\/www\.youtube\.com\/v\/([\-_\.a-zA-Z0-9]+)(\&*)([\-_\a-zA-Z0-9\/\?\&\=\%\n]*)/http\:\/\/m\.youtube\.com\/\?gl\=JP\&hl\=ja\#\/watch\?v\=$1<BR>/ig;
		    }elsif(($KEITAI_ENV{'MACHINE_TYPE'} eq "iPad")||($HTTP_USER_AGENT=~ /android/i)||($HTTP_USER_AGENT=~ /PSP/i)){
			$tmp_data =~ s/http\:\/\/www\.youtube\.com\/v\/([\-_\.a-zA-Z0-9]+)(\&*)([\-_\a-zA-Z0-9\/\?\&\=\%\n]*)/http\:\/\/m\.youtube\.com\/\?gl\=JP\&hl\=ja\#\/watch\?v\=$1\&client\=mv\-google<BR>/ig;
		    }else{
#2009.12 bug fix
			$tmp_data =~ s/http\:\/\/www\.youtube\.com\/v\/([\-_\.a-zA-Z0-9]+)(\&*)([\-_\a-zA-Z0-9\/\?\&\=\%\n]*)/http\:\/\/m\.jp\.youtube\.com\/details\?v\=$1 <BR>/ig;
		    }
		 }else{
			return($tmp_data);
		 }
	  }
	 }

	$tmp_data =~ s/<(\/?)iframe(.|\n)*iframe>(\s*)(\n?)/
	    \[�g�тł͕\\���ł��Ȃ�HTML�L�q�ł�\]./ig;       # IFRAME�^�O    ����

	$tmp_data =~ s/<(\/?)script(.|\n)*script>(\s*)(\n?)/
	    \[�g�тł͕\\���ł��Ȃ�HTML�L�q�ł�\]./ig;       # SCRIPT�^�O    ����

	# �N���E�h�T�[�r�X��URL��Z������ 2009.12
	local($tmp_google_ap)="";
	if($tmp_data=~ /\"http\:\/\/www\.google\.co\.jp\/(\S*)\?/i){
	
	 # iframe�����Ƃ��Ȃ̂ŁA�������Ȃ�
	 
	}elsif($tmp_data=~ /http\:\/\/www\.google\.co\.jp\/(\S*)\?/i){
	 $tmp_google_ap="$1";
	 if($tmp_google_ap=~ /maps/i){
		$tmp_data =~ s/(https?\:\/\/www\.google\.co\.jp\/maps)([\-_\.\!\~\*\'\(\)a-zA-Z0-9\;\/\?\:\@\&\=\+\$\,\%\#]*)/<A HREF="$1$2" TARGET="_blank">[google�n�}\]<\/A>/ig;
	 }
	}elsif($tmp_data=~ /([^\"])http\:\/\/maps\.google\.co\.jp\/(\S*)\?/i){
		$tmp_data =~ s/(https?\:\/\/maps\.google\.co\.jp\/maps)([\-_\.\!\~\*\'\(\)a-zA-Z0-9\;\/\?\:\@\&\=\+\$\,\%\#]*)/<A HREF="$1$2" TARGET="_blank">[google�n�}\]<\/A>/ig;
	}


	if($tmp_data!~ /<A(\s)(\n?)|<IMA?GE?(.*)/i){
	   $tmp_data =~ s/[\x80-\x9f\xe0-\xff]./$&\x01/g; # 2�o�C�g����

	   # ���������N(i���[�h/J�t�H���p)

		local($tmp_youtube_snl_url)="";
		# 2010.02 update
		local($ttmp_youtube_target_sitei)=qq|TARGET="_blank"|;
  		if($HTTP_USER_AGENT=~ /ipod|iphone|android|PSP/i){
  				# �u���E�U�������N������ƕ���̂�����ǂ�
				$ttmp_youtube_target_sitei="";
  		}

		# ����URL�����N
		# ���{��h���C���ɑΉ�����Ƃ���Ȃ��񂶁H�H
		# 2001.04.12 ���s�Ή�
		# 2001.08.20 ���C���itripod���ŔF���~�X������̂Œ����j

		# �N���E�h�ɑ����A����URL�G���R�[�h������Z������i�\�����Ă��l�Ԃ����ǂł��Ȃ����Asafari�Ń��C�A�E�g������邽�߁j
		if($tmp_data =~ /(\=|\/)([\%a-zA-Z0-9]{42})/g){
		     $tmp_data =~ s/(https?\:\/\/[^\s|\:|\<]+)\.(\/?)([\-_\.\!\~\*\'\(\)a-zA-Z0-9\;\/\?\:\@\&\=\+\$\,\%\#]*)(\=|\/)([\%a-zA-Z0-9]{36,330})([\-_\.\!\~\*\'\(\)a-zA-Z0-9\;\/\?\:\@\&\=\+\$\,\%\#]*)/<A HREF="$1.$2$3$4$5$6" $ttmp_youtube_target_sitei>$1.$2$3$4%E6%F3.. $6<\/A>/ig;
		}else{
		     $tmp_data =~ s/(https?\:\/\/[^\s|\:|\<]+)\.(\/?)([\-_\.\!\~\*\'\(\)a-zA-Z0-9\;\/\?\:\@\&\=\+\$\,\%\#]*)/<A HREF="$1.$2$3$4" $ttmp_youtube_target_sitei>$1.$2$3$4<\/A>/ig;
		}
		
		$tmp_data =~ s/(r?ftp\:\/\/[\-_\.\!\~\*\'\(\)a-zA-Z0-9\;\/\:]+)/<A HREF="$1" TARGET="_blank">$1<\/A>/g;
		# ����mail�����N(mailto���[��)		
		$tmp_data =~ s/(mailto\:[\-_\.a-zA-Z0-9\@]+)/<A HREF="$1" TARGET="_blank">$1<\/A>/g;
		# ����tel�����N(tel���[��)		
		$tmp_data =~ s/(tel\:[\-\(\)0-9\+\#\*]+)/<A HREF="$1" TARGET="_blank">$1<\/A>/g;

		# ���������A�h�����N(�������o)
		if($PM{'auto_mail_find'}==1){
		  $tmp_data =~ s/([\-_\.a-zA-Z0-9]+)\@([\-a-zA-Z0-9]+)\.([\-a-zA-Z0-9\.]+)([^a-zA-Z0-9]+)/<A HREF="mailto\:$1\@$2\.$3">$1\@$2\.$3<\/A>$4/g;
		}
	   $tmp_data =~ tr/\x01//d;

$PM{'auto_japanese_address_find'}=1;

		# �����Z�������N�iGoogle Map & �X�g���[�g�r���[�j 2013.01 Google API�d�l�ύX�𔽉f
		if($PM{'auto_japanese_address_find'}==1){
# 20100425 update
		    if(($tmp_data=~ /����|��|�s|�S|�{|��|�k�C��|��|��|�Ԓn/i)&&($tmp_data!~ /https?\:\/\//i)){

		     # �����s���c����K��1-1-1
		     if($tmp_data=~ /(�����s|���{|���s�{|[^\s\>\d]+��|�k�C��)([^\s\>\d]+)(�s|��)([^\s\>\d]+)([0-9�O-�X]+)(\-|�||����|��|�m)([0-9�O-�X]+)([\-|�||��|�m]?)([0-9�O-�X]?)/ig){
		       $ttmp_jp_geoname="$1$2$3$4$5$6$7$8$9";
		       # iPhone�ł��������Ȃ�̂�URL�G���R�[�h
		       $ttmp_jp_geoname=~ s/(\W)/'%'.unpack("H2", $1)/ego;
		       $tmp_data =~ s/(�����s|���{|���s�{|[^\s\>\d]+��|�k�C��)([^\s\>\d]+)(�s|��)([^\s\>\d]+)([0-9�O-�X]+)(\-|�||����|��|�m)([0-9�O-�X]+)([\-|�||��|�m]?)([0-9�O-�X]?)/<A HREF\=\"http\:\/\/maps.google.co.jp\/maps\?q=$ttmp_jp_geoname&hl=ja\" TARGET=\"_blank\">$1$2$3$4$5$6$7$8$9 <\/A>/ig;
		     }elsif($tmp_data=~ /([^\s\>\d]{1,10})(��|�s)([^\s\>\d]{1,10})([0-9�O-�X]+)(\-|�||����|��|�m)([0-9�O-�X]+)([\-|�||��|�m])([0-9�O-�X]+)/ig){
		       $ttmp_jp_geoname="$1$2$3$4$5$6$7$8";
		       # iPhone�ł��������Ȃ�̂�URL�G���R�[�h
		       $ttmp_jp_geoname=~ s/(\W)/'%'.unpack("H2", $1)/ego;
		       $tmp_data =~ s/([^\s\>\d]{1,10})(��|�s)([^\s\>\d]{1,10})([0-9�O-�X]+)(\-|�||����|��|�m)([0-9�O-�X]+)([\-|�||��|�m])([0-9�O-�X]+)/<A HREF\=\"https\:\/\/maps.google.co.jp\/maps\?q=$ttmp_jp_geoname&hl=ja\" TARGET=\"_blank\">$1$2$3$4$5$6$7$8$9 <\/A>/ig;
		     }
		    }


		}
			   
	}
	return($tmp_data);
}

#=========================#
# Content-type �̃`�F�b�N
#========================
#
sub content_type_check{

	local($content_type) = @_;

# �摜
	$ext{'image/jpg'}	= 'jpg'; 
	$ext{'image/jpeg'}	= 'jpg'; 	# for NN
	$ext{'image/pjpg'}	= 'jpg';
	$ext{'image/pjpeg'}	= 'jpg';	# for IE
	$ext{'image/gif'}	= 'gif';	# for NN&IE
	$ext{'image/png'}	= 'png';	# for PNG  file
	$ext{'image/x-png'}	= 'png';	# for PNG  file


	# �t���b�V���ɑΉ�
	$ext{'x-shockwave-flash'}= 'swf';	# for Shockwave_flash

	# gif,jpeg�ȊO�Ɉȉ��̃^�C�v�̃f�[�^�����e�ł���悤�ɂ���ɂ�
	# �����ݒ�ɂ�$PM{'allow_other_multimedia_data'}��1�ɂ��Ă��������D
	if($PM{'allow_other_multimedia_data'} ==1){
		&additional_content_types;
	}

	# img�^�O�Ŗ��ߍ��݉\�ȃ^�C�v
	foreach(keys %ext){
		if($content_type =~ /$_/ig){
			return $ext{$_};
		}
	}
	# img�^�O�Ŗ��ߍ��ނƊ댯�ȃ^�C�v
	foreach(keys %ext2){
		if($content_type =~ /$_/ig){
			return $ext2{$_};
		}
	}
        # ����ł��ʖڂȂ�g���q���画�f
	 if($fname=~ /\.gif$/i){return 'gif';}
	 if($fname=~ /\.jpe?g$/i){return 'jpg';}


	# �g�сiEZ new�j
# 2010.01 update
#	# Document
	 if($fname=~ /\.epub$/i){return 'epub';}# �d�q���Ѓt�@�C�� 2009.12

	 # 2009.10 iPhone�Ή��ǉ�
	 if($fname=~ /\.mp4$/i){return 'mp4';}	# i���[�V��������(ISMA-MPEG4:MP)
	 if($fname=~ /\.m4a$/i){return 'm4a';}	# MPEG-4 AAC Audio(iTunes)
	 if($fname=~ /\.m4v$/i){return 'm4v';}	# M4v�t�@�C��
	 if($fname=~ /\.aa$/i) {return 'aa';}	# audible.com spoken word
	 if($fname=~ /\.aax$/i){return 'aax';}	# audible.com spoken word Enhanced
	 if($fname=~ /\.aiff?$/i){return 'aif';}# AIFF


	 # �X�}�[�g�t�H����imgboard FLV Player�Ƃ̌݊����΍�
	 if($ENV{'CONTENT_LENGTH'} < 10000*1024){
	  # 10MB�ȉ��̏ꍇ
	  if($fname=~ /\.3gp$/i){return '3gp';}	# MP4�f�[�^(i���[�V����)
	  if($fname=~ /\.3gpp$/i){return '3gpp';}# MP4�f�[�^(i���[�V����)
	  if($fname=~ /\.3gp4$/i){return '3gp4';}# MP4�f�[�^(i���[�V����)
	 }else{
	  # �ǂ���i���[�r�[�ł͍Đ��ł��Ȃ��B
	  # ����āA�X�}�[�g�t�H����Flv Player�ƌ݊����̗ǂ�mp4�ɂ���
	  if($fname=~ /\.3gp$/i){return 'mp4';}	# MP4�f�[�^
	  if($fname=~ /\.3gpp$/i){return 'mp4';}# MP4�f�[�^
	  if($fname=~ /\.3gp4$/i){return 'mp4';}# MP4�f�[�^
	 }

	 # 2010.08 iPhone�̓���Ή�
 	 if($fname=~ /\.mov$/i){return 'mp4';}

	 if($fname=~ /\.swf$/i){return 'swf';}	# Flash�f�[�^
	 # 2006.12.13 Flash Movie�ǉ�
	 if($fname=~ /\.flv$/i){return 'flv';}	# Flash Video

	# 2010.06.08 imgboard FLV Player�p�ɒǉ�
	 if($fname=~ /\.f4v$/i){return 'mp4';}	# Flash Video
	 if($fname=~ /\.f4a$/i){return 'mp4';}	# Flash Video

	 # 2008.06.02 906i�V���[�Y��2MB�A�b�v���[�h�Ή�
	 if($fname=~ /\.wmv$/i){return 'wmv';}	# Windows Media
	 if($fname=~ /\.wma$/i){return 'wma';}	# Windows Media
	 if($fname=~ /\.asf$/i){return 'asf';}
	 if($fname=~ /\.pdf$/i){return 'pdf';}	# PDF�t�@�C��
	 if($fname=~ /\.epub$/i){return 'epub';}# �d�q���Ѓt�@�C�� 2009.12

	 if($fname=~ /\.png$/i){return 'png';}
	 if($fname=~ /\.bmp$/i){return 'bmp';}
	 if($fname=~ /\.midi?$/i){return 'mid';}
	 if($fname=~ /\.kar$/i){return 'kar';}

	 if($fname=~ /\.mmf$/i){return 'mmf';}	# J�X�J�C�����f�B



	# gif,jpeg�ȊO�Ɉȉ��̃^�C�v�̃f�[�^�����e�ł���悤�ɂ���ɂ�
	# �����ݒ�ɂ�$PM{'allow_other_multimedia_data'}��1�ɂ��Ă��������D
        if($PM{'allow_other_multimedia_data'} ==1){
         # (�����Ń��X�g������ɒǉ�����ꍇ�̒���)
         # cgi,asp,pl,sh,exe.shtml,js,jse,vbs,vbe,hta,wsh,xlm���̊g���q�̓Z�L
	 # �����e�B��댯�Ȃ̂Ő�Βǉ����Ȃ����Ɓi����Windows���[�U�j

	# Other Audio
	 if($fname=~ /\.midi?$/i){return 'mid';}# Midi 

	 if($fname=~ /\.rtf$/i){return 'rtf';}	# Word98
	 if($fname=~ /\.csv$/i){return 'csv';}	# �f�[�^�x�[�X
#	 if($fname=~ /\.mov$/i){return 'mov';}

	 # ���̑��ׂ������͍폜�B����� e_FTPboard�������p���������B

	 if($fname=~ /\.avi$/i){return 'avi';}
	 if($fname=~ /\.mpg$/i){return 'mpg';}
	 if($fname=~ /\.asf$/i){return 'asf';}
	 if($fname=~ /\.asx$/i){return 'asx';}
	 if($fname=~ /\.txt$/i){return 'txt';}
	 if($fname=~ /\.html?$/i){return 'html';}
        }

	$unknown_data_exit=1;

# �f�[�^�^�C�v�s���̏ꍇ�̍ŏI���f
	if($unknown_data_exit==1){
		&error(" ���̃^�C�v�̃f�[�^�̓A�b�v���[�h�ł��܂���D");
	}else{
		return 'dat';
	}
}

#=========================#
# Content-type �̒ǉ�
#=========================#
sub additional_content_types{

# ���܂��@�\(~_~)
# gif,jpeg�ȊO�Ɉȉ��̃^�C�v�̃f�[�^�����e�ł���悤�ɂł��܂��B
# ���e���������Ȃ��f�[�^�^�C�v�ɂ�#��擪�ɂ��ăR�����g�A�E�g���ĉ������B
#
# 2002.04 �g�тű���۰�ނ��Ȃ����̂������
#
# <�����ӁI>
# �Ȃ����e�����������Ȃ��ꍇ��#��擪�ɂ��ăR�����g�A�E�g���ĉ������B

# �摜�n�i���̑��j
	$ext{'image/png'}	= 'png';	# for PNG  file
	$ext{'image/x-png'}	= 'png';	# for PNG  file
#	$ext{'image/bmp'}	= 'bmp';	# for BMP  file
	$ext2{'director'}= 'dcr';		# for Director
	$ext2{'x-shockwave-flash'}= 'swf';	# for Shockwave_flash(505i�p)
	$ext2{'application/pdf'}= 'pdf';	# for PDF  file
	$ext2{'application/vnd.ms-xpsdocumen'}= 'xps';	# for MS-PDF  file 2009.06 add
	$ext2{'application/epub'}= 'epub';	# for kindle(epub) 2009.12

# �A�[�J�C�u�n
	$ext2{'application/zip'}= 'zip';	# for ZIP   (Win)
	$ext2{'x-zip'}= 'zip';			# for ZIP   (Win)
	$ext2{'compressed/lha'}= 'lzh';		# for LZH   (Win)
	$ext2{'application/x-7z-compressed'}= '7z';	# for 7ZIP

# 3D & �r�f�I�n
	$ext2{'video/(.*)-asf'}= 'asf';		# for NetShow file

	 # �X�}�[�g�t�H����imgboard FLV Player�Ƃ̌݊����΍�
	if($ENV{'CONTENT_LENGTH'} < 10000*1024){
	 # 10MB�ȉ��̏ꍇ
	 $ext2{'video/3gpp'}	= '3gp';	# for i-Motion file
	 $ext2{'video/3gp'}	= '3gp';	# for i-Motion file
	 $ext2{'audio/3gpp'}	= '3gp';	# for i-Motion file
	 # 10MB�ȏゾ�ƁA�ǂ����Đ��ł��Ȃ��̂ŁA
	 # FLVPlayer��iPhone/iPad�ƌ݊����̍���mp4�g���q�ɂ���
	}else{
	 $ext2{'video/3gpp'}	= 'mp4';	# for i-Motion file
	 $ext2{'video/3gp'}	= 'mp4';	# for i-Motion file
	 $ext2{'video/3gpp2'}	= 'mp4';	# EZ���[�r�[�f�[�^
	 $ext2{'audio/3gpp'}	= 'mp4';	# for i-Motion file
	 $ext2{'audio/3gpp2'}	= 'mp4';	# EZ���[�r�[�f�[�^
	}

	# TODO mov���������Ƃ���3GP�Ƀ��l�[������������������
	$ext2{'video/quicktime'}	= 'mov';# for QuickTime  file
	$ext2{'video/x-flv'}	= 'flv';	# Flash Video�f�[�^
# 2009.10 �ǉ�
	$ext2{'video/x-m4v'}	= 'm4v';	# M4v �f�[�^
	$ext2{'video/x-ms-wmv'}= 'wmv';    # Windows Media �I�[�f�B�I/�r�f�I �t�@�C��


# ��ЂŎd���ɖ𗧂��n
	$ext2{'text/html'}= 'html';	 	# HTML�e�L�X�g
	$ext2{'text/plain'}= 'txt'; 		# �e�L�X�g

# ���y�n
	$ext2{'audio/mpeg'}= 'mp3';			# for MPEG Audio
	$ext2{'audio/x-mpegurl'}= 'm3u';		# for MPEG Audio
	$ext2{'audio/x-wav'}= 'wav';		# for WAV Audio
	$ext2{'audio/(.+)mid'}= 'mid';		# for MIDI file
	$ext2{'audio/(.+)aiff?'}= 'aif';	# for AIFF file
	$ext2{'audio/x-ms-wma'}= 'wma';		# for WMA file
	$ext2{'audio/x-ms-wax'}= 'wax';	    # WindowsMedia Audio�V���[�g�J�b�g
	$ext2{'audio/mp4'}	= 'm4a';		# for MPEG Audio AAC
	$ext2{'audio/x-m4a'}= 'm4a';			# for MPEG Audio AAC	
	# 2009.06 �ǉ�
	$ext2{'audio/audible'} = 'aa';		# for audible spoken word file(iPod)
	$ext2{'audio/x-audible'} = 'aa';	# for audible spoken word file(iPod)
}
#
#====================================================#
# imgtitle����A$IMG_PARAMETERS{name}���𔲂��o��
#====================================================#
# �����̓R�����g�A�E�g�t����$tmp_imgtitle
# �Ԓl�̓R�����g�A�E�g�Ȃ���$tmp_imgtitle�ƘA�z�z�� $IMG_PARAMETERS{$name}
sub parse_img_param{

	local($ttmp_imgtitle)= $_[0];	# �����Ƃ��Ď擾

	# imgtitle�̒���size,height,width���̃p�����[�^���i�[
	# ����<!--�p�����[�^��=�l;�p�����[�^��2=�l2�E�E�E-->
	# <!--��-->�������p�����[�^���𒊏o
	if($ttmp_imgtitle ne ''){
		($ttmp_imgtitle,$img_parameters)=split(/<\!--/,$ttmp_imgtitle);
		$img_parameters=~ s/-->//g;
	}

	# �p�����[�^$img_parameters���ǉ�����Ă���ꍇ�D
	if($img_parameters ne ''){
		foreach ( split(/;/,$img_parameters)){
			local($name,$value) = split(/\=/);
			$IMG_PARAMETERS{$name} = $value;
		}
	}
	return($ttmp_imgtitle);
}
#
#========================#
# CGI�����Ƃ肾��
#========================#
#
sub get_script_name {

	local($file_name) = $0;
	local($path_name);
	local($script_name);

	# �p�X������ꍇ�͍��
	if ($file_name =~ /\\|\//) {
	  if ($file_name =~ /^(.*)\\([^\\]*)$/) {
		$path_name	=$1;
		$script_name	=$2;
	  }elsif($file_name =~ /^(.*)\/([^\/]*)$/) {
		$path_name	=$1;
		$script_name	=$2;
	  }else{
		$script_name	="$file_name";
	  }
	}else{
	  $script_name="$file_name";
	}

	$script_path_name="$path_name"; # �O���[�o���ϐ�(�p�X)

	return("$script_name");
}

#===================================#
# �L���o�^���ɊǗ��҂Ƀ��[��
#===================================#

sub send_mail{

	if ($PM{'use_email'}==1){

		# OS�̎�ʂ𔻕�
		$www_server_os =&check_www_server_os;

		# OS�`�F�b�N���ʂ�Windows,Mac���������[�U�ɂ́A�x�����o��
		if($www_server_os=~ /(win|mac)/i){
			&error("�Ǘ��Ґݒ�ɃG���[������܂�<BR>���[���ʒm\�@\�\\�� $1 �T�[�o�ł͎g�p�ł��܂���B�I�t�ɂ��Ă��������B");
			return;
		}

		# �p�����[�^�`�F�b�N�i�Z�L�����e�B�`�F�b�N�j
		if($email=~ /.*\@.*\..*/){
			$eemail_address=$email;
		}else{
			$eemail_address="dummy\@dummy.co.jp";
		}

		$eemail_name="$name";
		$eemail_subject	="$subject";
		$eemail_imgtitle="$imgtitle";

		# �{������������ꍇ�̓J�b�g����B���[�����e�n�̃C�^�Y���΍�B
		$eemail_body=$body;
		$eemail_body=~ s/\<BR\>/\n/gi;
		$eemail_body=~ s/\<\!-- user/\n\<\!-- user/i;

		if($PM{'mail_body_limit'}){
			$tmp_mail_body_limit="$PM{'mail_body_limit'}";
		}else{
			$tmp_mail_body_limit='360';
		}

		# �����ݒ�Őݒ肵��������蒷���ꍇ 
		if(length($body) >$tmp_mail_body_limit){
 			# �擪����w��o�C�g�܂ł̂ݎc��
			$eemail_body =substr("$body",0,"$tmp_mail_body_limit");
			$eemail_body .=" \/\/���߂��܂��̂ŁA�Ȍ�̓J�b�g���܂���.<!-- user�F $REMOTE_HOST --> - $HTTP_REFERER ";
		}

  		# URL���w�肳��Ă���ꍇ�̓t��URL�\�L�ɂ���B
		# �O���摜�Ή��C��
		$eemail_img_location="$img_location";
		if(($PM{'cgi_link_url'}!~ /http:\/\/yourprovider\/yourname\/imgboard/)&&($img_location!~ /^http:\/\//i)){
			$eemail_img_location="$PM{'cgi_link_url'}".""."$img_location";
			$eemail_img_location=~ s/(\/?)\.\//\//g; # ���΃p�X���C��
		}

		# �Z�L�����e�B�΍�̂��߁A���̂��镶�����t�B���^
		$eemail_address		=~ s/\,|\;|\://g;
		$eemail_name		=~ s/\,|\;|\://g;
		$eemail_subject		=~ s/\,|\;|\://g;
		$eemail_imgtitle	=~ s/\,|\;|\://g;

		# ���[�����ʂ�������
$m_mes .= "MIME-Version: 1.0\n";
$m_mes .= "Reply-to: $eemail_address\n";
$m_mes .= "From: $eemail_address\n";
$m_mes .= "Subject: \[imgboard\]New article is added (via imode)\n";
$m_mes .= "Content-Type: text/plain; charset=iso-2022-jp\n";
$m_mes .= "Content-Transfer-Encoding: 7bit\n\n";

$m_mes .= "imgboard�A�N�Z�X��($keitai_flag-$KEITAI_ENV{'MACHINE_TYPE'})�o�R�ŋL�������e����܂����B\n";
$m_mes .= "[URL] \n";
$m_mes .= "$PM{'cgi_link_url'}"."\/"."$cgi_name \n";
$m_mes .= "[DATE] $date_data\n";
$m_mes .= "[NAME] $eemail_name\n" 		if($eemail_name ne "");
$m_mes .= "[e-mail] $eemail_address\n"	if($eemail_address ne "");
$m_mes .= "---------------------------------------\n";
$m_mes .= "[TITLE] $eemail_subject\n" 		if($eemail_subject ne "");
$m_mes .= "[MES] \n $eemail_body\n"		if($eemail_body ne "");
$m_mes .= "[File Title]  $eemail_img_title\n" 	if($eemail_img_title ne "");
$m_mes .= "[File URL  ]  $img_data_size\n" 	if($img_location ne "");
$m_mes .= "        $eemail_img_location \n"	if($img_location ne "");
$m_mes .= "[AGENT] $HTTP_USER_AGENT\n"		if($HTTP_USER_AGENT);
$m_mes .= "[�A��] $now_up_counter �� [���~�b�^���ݐݒ�] $PM{'upload_limit_times'} / $PM{'upload_limit_type'} \n"	if($PM{'limit_upload_times_flag'}==1);
$m_mes .= " �ȏ� \n";

	# ���[�����ʂ����܂�

	# ���[���ŕW���̌`�ԁA�����R�[�hJIS�A���s�R�[�hLF�ɕϊ�����B
	$m_mes=~ s/\r\n/\n/g;		# ���s�R�[�h��ϊ�
	$m_mes=~ s/\r/\n/g;			#���s�R�[�h��ϊ�
	&jcode'convert(*m_mes, 'jis');	# �����R�[�h��JIS��(�C��99.11)

	# ���[���𑗏o
	open (MAIL, "|$PM{'mail_prog'} $PM{'recipient'}") || &error(" �Ǘ��Ґݒ�ɃG���[������܂�<BR>���[���v���O����$PM{'mail_prog'}��������܂���B���[���v���O�����̃p�X���Ċm�F���Ă��������B<BR>�܂�Web�T�[�o�ƃ��[���T�[�o���ʂ̃T�[�o�̏ꍇ�g�p�ł��܂���B\n");
		print MAIL "$m_mes";	
   	close (MAIL);
	}
}

#
#=====================================#
#     <�g�s�l�k--�Ǘ����j���[>        #
#=====================================#
#
#  �Ǘ����j���[�p�̂g�s�l�k�ł��D�J�X�^�}�C�Y�̕K�v�͂���܂���B
#
sub output_admin_menu_HTML{
print<<HTML_END;
<HTML>
<HEAD>$top_html_header</HEAD>
<BODY BGCOLOR=PINK>
�摜Upload�f����<BR>
<CENTER>
(�g�ѱ���)<BR>
<BR>
�Ǘ����j���[<BR>
</CENTER>
$HR
�E<a href="$cgi_name?page=$FORM{'page'}&mode=remove_select"> �L���폜 </a><BR>
�E<a href="$cgi_name?page=$FORM{'page'}&mode=change_set"> �ݒ�ύX </a><BR>
�E<a href="$cgi_name?page=$FORM{'page'}&mode=show_howto"> �g���� </a><BR>
�E<a href="$cgi_name?page=$FORM{'page'}&mode=whats_imgboard"> imgboard�Ƃ�</a><BR>
$HR
�E<a href="$cgi_name?page=$FORM{'page'}&mode=user_01"> �g�т������N! </a><BR>
�E<a href="$cgi_name?page=$FORM{'page'}&mode=user_02"> ---- </a><BR>
�E<a href="$cgi_name?page=$FORM{'page'}&viewpass=$FORM{'viewpass'}&mode=user_03"> �F�B�ɋ����� </a><BR>
$HR
�f�o�b�N<BR>
�E<a href="$cgi_name?page=$FORM{'page'}&mode=check_env">�@���� </a><BR>
<BR>
$accesskey_p1<a href="$cgi_name?page=$FORM{'page'}&viewpass=$FORM{'viewpass'}" accesskey=0>�߂�</a><BR>
$HR

</BODY>
</HTML>
HTML_END
}
#
#===============================================#
#     <�g�s�l�k--�Ǘ����j���[(�ݒ�ύX1/4)>        #
#===============================================#
#
#  �Ǘ����j���[(�ݒ�ύX)�p�̂g�s�l�k�̂P�y�[�W�ڂł��D
#
sub output_change_set_HTML{
print<<HTML_END;
<HTML>
<HEAD>$top_html_header</HEAD>
<BODY BGCOLOR=PINK>
�摜Upload�f����<BR>
<center>
(�g�ѱ���)<BR>
<BR>
�ݒ�ύX���j���[<BR>
(<B>1P</B>/<a href="$cgi_name?page=$FORM{'page'}&mode=change_set2">2P</a>)<BR>
(<a href="$cgi_name?page=$FORM{'page'}&mode=change_set3">3P</a>/<a href="$cgi_name?page=$FORM{'page'}&mode=change_set4">4P</a>)<BR>

</center>
$HR
(�͂��߂�)<BR>
imgboard�͓��ɐݒ肵�Ȃ��Ă���̂̃T�[�o�œ����܂����A
�������̃J�X�^�}�C�Y�p�����[�^���p�ӂ���Ă܂��̂ŁA
��������g�����������Ƃ���Ɏ����D�݂̐ݒ�ɂ��邱�Ƃ�
��\�\\�ł��B�قƂ�ǂ̐ݒ��cgi���ɂ���܂����A�ꕔ�p��
���[�^��Web�ł��ݒ�ł��܂��B
�i�Ȃ��A������cgi���Əd������ݒ肵���ꍇ�A�����ɂ���ݒ肪�D�悳��܂��j

$HR
<FORM action=$cgi_name>
(��{�ݒ�)<BR>
���J���[�h<BR>
<SELECT NAME=bbs_open>
<OPTION SELECTED>$PM{'bbs_open'}
<OPTION VALUE="3">3=�Ǐ�OK(�ʏ�)
<OPTION VALUE="2">2=ReadOnly
<OPTION VALUE="1">1=�Ǘ�MENU�̂�
</SELECT>
<BR>
<BR>
<INPUT TYPE=TEXT VALUE="$PM{'max_message'}" SIZE=3 MAXLENGTH=4>�� �ő�ۑ�<BR> 
<INPUT TYPE=TEXT VALUE="$PM{'gisa'}" SIZE=3 MAXLENGTH=4>(h)����<BR>
<BR>
--�ȍ~1=YES,0=NO<BR>
*����̫�Ēl--<BR>
<BR>
HTML_END

 &show_select_typeA("use_rep","$PM{'use_rep'}"," �ԐM���� ","*","");
 &show_select_typeA("res_go_up","$PM{'res_go_up'}"," �ԐM����� ","*","");
 &show_select_typeA("disp_new_notice","$PM{'disp_new_notice'}"," �ŐV�R�L��Mark","*","");
print<<HTML_END;
$HR
(PC���e����)<BR>
�g�т���̓��e�݂̂��󂯕t�������ꍇ��1
HTML_END
 &show_select_typeA("no_upload_from_pc","$PM{'no_upload_from_pc'}","","*","");

print<<HTML_END;
$HR
(PC�{������)<BR>
�g�т��炾���{���ł���悤�ɂ������ꍇ��1
(PC����͂��̃��j���[�������Ȃ��Ȃ�̂Œ���)
HTML_END
 &show_select_typeA("no_upload_from_pc","$PM{'no_upload_from_pc'}","","*","");

print<<HTML_END;

$HR
(�Y�ţ��)<BR>
�f�t�H���g�ł�GIF/JPEG/PNG/MNG/3GP����/�f�R��/�d�b��/WMV/WMA/PDF/MP4/ezmovie/ASF���ł��B����ȊO�̊e��}���`���f�B�A�f�[�^�i�e�L�X�g,HTML,�������Ȃǖ�R�O��ށj�̓��e��������ꍇ�͈ȉ��̃t���O��1�ɂ��Ă��������B<BR>
HTML_END
 &show_select_typeA("allow_other_multimedia_data","$PM{'allow_other_multimedia_data'}"," ���� ","","*");
 print<<HTML_END;

$HR
(����backup)<BR>
HTML_END
 &show_select_typeA("make_backup_file","$PM{'make_backup_file'}"," ���� ","*","");
 
print<<HTML_END;
<SELECT NAME="backup_day_interval">
<OPTION SELECTED>$PM{'backup_day_interval'}
<OPTION VALUE="2">2��
<OPTION VALUE="3">3��
<OPTION VALUE="7">7��
<OPTION VALUE="14">14��
<OPTION VALUE="30">30��
<OPTION VALUE="60">60��
</SELECT>�Ԋu(��)
$HR
(�������[��)<BR>
HTML_END

 &show_select_typeA("use_email","$PM{'use_email'}"," ���� ","","*");
 &show_text_input_typeA("mail_body_limit","$PM{'mail_body_limit'}","Ұْ����",3,3,"istyle=4");

print<<HTML_END;
$HR
<INPUT TYPE=HIDDEN NAME=bbsaction VALUE="change_config">
<INPUT TYPE=PASSWORD NAME="passwd" SIZE=5 MAXLENGTH=12 istyle=4>
<INPUT TYPE=SUBMIT VALUE="�K�p">
</FORM>

(<B>1P</B>/<a href="$cgi_name?page=$FORM{'page'}&mode=change_set2">2P</a>)<BR>
(<a href="$cgi_name?page=$FORM{'page'}&mode=change_set3">3P</a>/<a href="$cgi_name?page=$FORM{'page'}&mode=change_set4">4P</a>)<BR>


$accesskey_p1<a href="$cgi_name?page=$FORM{'page'}&viewpass=$FORM{'viewpass'}&mode=disp_admin_menu" accesskey=0>�߂�</a><BR>
$HR
</BODY>
</HTML>
HTML_END
}
#

#===============================================#
#     <�g�s�l�k--�Ǘ����j���[(�ݒ�ύX2/4)>     #
#===============================================#
#
#  �Ǘ����j���[(�ݒ�ύX)�p�̂g�s�l�k�̂Q�y�[�W�ڂł��D
#
sub output_change_set2_HTML{
print<<HTML_END;
<HTML>
<HEAD>$top_html_header</HEAD>
<BODY BGCOLOR=PINK>
�摜Upload�f����<BR>
<center>
(�g�ѱ���)<BR>
<BR>
�ݒ�ύX���j���[<BR>
(<a href="$cgi_name?page=$FORM{'page'}&mode=change_set">1P</a>/<B>2P</B>)<BR>
(<a href="$cgi_name?page=$FORM{'page'}&mode=change_set3">3P</a>/<a href="$cgi_name?page=$FORM{'page'}&mode=change_set4">4P</a>)<BR>
</center>
<FORM action=$cgi_name>

$HR
HTML_END

if($debug_mode >= 3){
print<<HTML_END;
(�f�o�b�N)<BR>
�g�у��[�h�Œ�<BR>
�Œ肷��Ƒ��@�킩�炤�܂����e�ł��Ȃ��Ȃ�܂��̂ł����ӂ��������B
�ʏ�͎����F���ɃZ�b�g���A�u�󔒁v�ɂȂ�悤�ɂ��Ă����Ă��������B
�Ȃ��AEZweb�AH�h�ɂ���ƁA���̃��j���[�ɃA�N�Z�X�ł��Ȃ��Ȃ邽�߁A�Œ胂�[�h��Web�ォ������ł��Ȃ��Ȃ�܂��B���̏ꍇ��file.dat�̐擪���ɂ���keitai_force_set�̍s���G�f�B�^�łP�s�����āA�蓮�ŕ��A�����Ă��������B<BR>
<SELECT NAME=keitai_force_set>
<OPTION SELECTED>$PM{'keitai_force_set'}
<OPTION VALUE="imode">i���[�h
<OPTION VALUE="J-PHONE">SoftBank
<OPTION VALUE="EZweb">EZweb�i�����s�\\�j
<OPTION VALUE="H">H�h�i�����s�\\�j
<OPTION VALUE="FOMA">FOMA
<OPTION VALUE="NULL">����*
</SELECT>
<BR>
SoftBank<BR>
<SELECT NAME=station_force_set>
<OPTION SELECTED>$PM{'station_force_set'}
<OPTION VALUE="3">3=�ð��ݑΉ�
<OPTION VALUE="4">4=�߹�đΉ�
<OPTION VALUE="1">1=��ð��ݑΉ�
<OPTION VALUE="">����*
</SELECT>
<BR>
HTML_END
}

 &show_select_typeA("flock","$PM{'flock'}"," flock�g�p ","","");
 &show_select_typeA("use_crypt","$PM{'use_crypt'}","PASS�Í��� ","","");

print<<HTML_END;
$HR
(����è)<BR>
�Ǘ����߽ [�g�p]<BR>
<BR>
(�A������)<BR>
HTML_END

 &show_select_typeA("limit_upload_times_flag","$PM{'limit_upload_times_flag'}"," �A������ ","*","");
 &show_text_input_typeA("upload_limit_times","$PM{'upload_limit_times'}"," ������ ",2,3,"istyle=4");
 &show_text_input_typeA("upload_limit_type","$PM{'upload_limit_type'}"," �����ر ",4,5);
 print "<HR>\n";
 print "(��������΍�)<BR>\n";
 print "�֎~���ɂ�鐧���ł��B�`�F�b�N���鍀�ڂ��ȉ��Ŏw�肵�Ă�������<BR>\n";
 &show_select_typeA("no_upload_by_black_word","$PM{'no_upload_by_black_word'}"," հ�ޖ�/�{�� ","","*");

print<<HTML_END;
<BR>
IP�ɂ�鐧��<BR>
�g�т�IP�͕s��Ȃ��ߓ��@\�\\�͎g�p�ł��܂���<BR>
$HR
<INPUT TYPE=HIDDEN NAME=bbsaction VALUE="change_config">
<INPUT TYPE=PASSWORD NAME="passwd" SIZE=5 MAXLENGTH=12 istyle=4>
<INPUT TYPE=SUBMIT VALUE="�K�p">
</FORM>


(<a href="$cgi_name?page=$FORM{'page'}&mode=change_set">1P</a>/<B>2P</B>)<BR>
(<a href="$cgi_name?page=$FORM{'page'}&mode=change_set3">3P</a>/<a href="$cgi_name?page=$FORM{'page'}&mode=change_set4">4P</a>)<BR>


$accesskey_p1<a href="$cgi_name?page=$FORM{'page'}&viewpass=$FORM{'viewpass'}&mode=disp_admin_menu" accesskey=0>�߂�</a><BR>
$HR
</BODY>
</HTML>
HTML_END
}
#
#===============================================#
#     <�g�s�l�k--�Ǘ����j���[(�ݒ�ύX3/4)>     #
#===============================================#
#
#  �Ǘ����j���[(�ݒ�ύX)�p�̂g�s�l�k��3�y�[�W�ڂł��D
#
sub output_change_set3_HTML{
print<<HTML_END;
<HTML>
<HEAD>$top_html_header</HEAD>
<BODY BGCOLOR=PINK>
�摜Upload�f����<BR>
<center>
(�g�ѱ���)<BR>
<BR>
�ݒ�ύX���j���[<BR>
(<a href="$cgi_name?page=$FORM{'page'}&mode=change_set">1P</a>/<a href="$cgi_name?page=$FORM{'page'}&mode=change_set2">2P</a>)<BR>
(<B>3P</B>/<a href="$cgi_name?page=$FORM{'page'}&mode=change_set4">4P</a>)<BR>
HTML�֘A<BR>
</center>
<FORM action=$cgi_name>
$HR
(HTML)<BR>
����<BR>
<INPUT TYPE=TEXT NAME="title" MAXLENGTH=20 SIZE=22 VALUE="$PM{'title'}">
<BR>
�߂��<BR>
<INPUT TYPE=TEXT NAME="back_url" MAXLENGTH=40 SIZE=56 VALUE="$PM{'back_url'}">
<BR>
<BR>
-�F�w��-<BR>
<INPUT TYPE=TEXT NAME="im_body_bgcolor" MAXLENGTH=10 SIZE=6 VALUE="$PM{'im_body_bgcolor'}">�w�i<BR>

<INPUT TYPE=TEXT NAME="im_body_text" MAXLENGTH=10 SIZE=6 VALUE="$PM{'im_body_text'}">TEXT<BR>
<INPUT TYPE=TEXT NAME="im_body_link" MAXLENGTH=10 SIZE=6 VALUE="$PM{'im_body_link'}">LINK
<BR>

<INPUT TYPE=TEXT NAME="im_body_vlink" MAXLENGTH=10 SIZE=6 VALUE="$PM{'im_body_vlink'}">VLINK<BR>
$HR
(�\\�����)<BR>
��ʋ����̂�(^^)<BR>
HTML_END

 &show_text_input_typeA("message_per_page","$PM{'message_per_page'}"," �L��/�߰�� ",2,2,"istyle=4");
 &show_text_input_typeA("kiji_disp_limit_imode","$PM{'kiji_disp_limit_imode'}"," ����/1�L��",3,3,"istyle=4");
 print "�J�i�������p\n";
 &show_select_typeA("hankaku_filter","$PM{'hankaku_filter'}"," ���� ","*","");
print<<HTML_END;
$HR
(�����ݸ�쐬)<BR>
�ȍ~1=YES,0=NO<BR>
HTML_END

 &show_select_typeA("auto_url_link","$PM{'auto_url_link'}"," URL���� ","*","");
print<<HTML_END;
$HR
(FORM)<BR>
�K�{�w��<BR>
1=�K�{,0=�ȗ���<BR>
HTML_END

 &show_select_typeA("form_check_name","$PM{'form_check_name'}"," �����O ","*","");
 &show_select_typeA("form_check_email","$PM{'form_check_email'}"," �ٱ�� ","","*");
 &show_select_typeA("form_check_subject","$PM{'form_check_subject'}"," �薼�� ","","*");
 &show_select_typeA("form_check_body","$PM{'form_check_body'}"," �{���� ","","*");

print<<HTML_END;

$HR
<INPUT TYPE=HIDDEN NAME=bbsaction VALUE="change_config">
<INPUT TYPE=PASSWORD NAME="passwd" SIZE=5 MAXLENGTH=12 istyle=4>
<INPUT TYPE=SUBMIT VALUE="�K�p">
</FORM>

(<a href="$cgi_name?page=$FORM{'page'}&mode=change_set">1P</a>/<a href="$cgi_name?page=$FORM{'page'}&mode=change_set2">2P</a>)<BR>
(<B>3P</B>/<a href="$cgi_name?page=$FORM{'page'}&mode=change_set4">4P</a>)<BR>


$accesskey_p1<a href="$cgi_name?page=$FORM{'page'}&viewpass=$FORM{'viewpass'}&mode=disp_admin_menu" accesskey=0>�߂�</a><BR>
$HR
</BODY>
</HTML>
HTML_END
}
#
#
#===============================================#
#     <�g�s�l�k--�Ǘ����j���[(�ݒ�ύX4/4)>     #
#===============================================#
#
#  �Ǘ����j���[(�ݒ�ύX)�p�̂g�s�l�k��4�y�[�W�ڂł��D
#
sub output_change_set4_HTML{


print<<HTML_END;
<HTML>
<HEAD>$top_html_header</HEAD>
<BODY BGCOLOR=PINK>
�摜Upload�f����<BR>
<center>
(�g�ѱ���)<BR>
<BR>
�ݒ�ύX���j���[<BR>
(<a href="$cgi_name?page=$FORM{'page'}&mode=change_set">1P</a>/<a href="$cgi_name?page=$FORM{'page'}&mode=change_set2">2P</a>)<BR>
(<a href="$cgi_name?page=$FORM{'page'}&mode=change_set3">3P</a>/<B>4P</B>)<BR>
</center>
<FORM action=$cgi_name>
$HR
����߽(���e�߽)�̗L���̐ݒ�ƁA�߽��ށi�S���̐����j�̐ݒ肪�����łł��܂��B�Ȃ��A������
�ݒ��ύX����ƁA�����ł̐ݒ�̕����D��x���������߁A�X�N���v�g
���Ŏw�肵������߽�֘A�̎w�肪�Ȍ�����Ȃ��Ȃ�܂��̂ŁA������
���������B
�Ȃ��A����߽�������ŕύX���A�����߽��Y��Ă��܂����ꍇ�́A
�����ŐV�߽��ނ�ݒ肵�Ă��������B<BR>

1=YES,0=NO<BR>
*����̫�Ēl<BR>

HTML_END

 &show_select_typeA("use_post_password","$PM{'use_post_password'}"," ���e�߽�g�p ","*","");

print<<HTML_END;


HTML_END

  if($PM{'use_post_password'} == 1){

print<<HTML_END;
<INPUT TYPE=TEXT NAME="post_passwd" MAXLENGTH=10 SIZE=6>���e�߽<BR>
��4���̐���
$HR
HTML_END

  }else{
print<<HTML_END;
$HR
HTML_END

  }

print<<HTML_END;
<INPUT TYPE=HIDDEN NAME=bbsaction VALUE="change_config">
<INPUT TYPE=PASSWORD NAME="passwd" SIZE=5 MAXLENGTH=12 istyle=4>
<INPUT TYPE=SUBMIT VALUE="�K�p">
</FORM>

(<a href="$cgi_name?page=$FORM{'page'}&mode=change_set">1P</a>/<a href="$cgi_name?page=$FORM{'page'}&mode=change_set2">2P</a>)<BR>
(<a href="$cgi_name?page=$FORM{'page'}&mode=change_set3">3P</a>/<B>4P</B>)<BR>


$accesskey_p1<a href="$cgi_name?page=$FORM{'page'}&viewpass=$FORM{'viewpass'}&mode=disp_admin_menu" accesskey=0>�߂�</a><BR>
$HR
</BODY>
</HTML>
HTML_END
}
#
#
sub show_select_typeA{
    # ���� NAME,�f�t�H���g�l�A���ږ��A1�ɐ����A0�ɐ���
    local($value_name)=$_[0];
    local($selected_value)=$_[1];
    local($p_name)=$_[2];
    local($mes_p1)=$_[3];
    local($mes_p0)=$_[4];
print<<HTML_END;
<SELECT NAME="$value_name">
<OPTION SELECTED>$selected_value
<OPTION VALUE="1">1$mes_p1
<OPTION VALUE="0">0$mes_p0
</SELECT>$p_name<BR>
HTML_END
}
#
sub show_text_input_typeA{
    # ���� NAME,�f�t�H���g�l�A���ږ�,�T�C�Y�A�ő�T�C�Y
    local($value_name)	=$_[0];
    local($def_value)	=$_[1];
    local($p_name)	=$_[2];
    local($t_size)	=$_[3];
    local($max_length)	=$_[4];
    local($other_para)	=$_[5];
print<<HTML_END;
<INPUT TYPE=TEXT SIZE="$t_size" MAXLENGTH="$max_length" NAME="$value_name" VALUE="$def_value" $other_para>
$p_name<BR>
HTML_END
}
#
#===============================================#
#     <�g�s�l�k--�Ǘ����j���[(�g����)>          #
#===============================================#
#
#  �Ǘ��p���j���[(�g�������)�p�̂g�s�l�k�ł��D
#
sub output_show_howto_HTML{
print<<HTML_END;
<HTML>
<HEAD>$top_html_header</HEAD>
<BODY BGCOLOR=PINK>
�摜Upload�f����<BR>
<CENTER>
(�g�ѱ���)<BR>
<BR>
�g����<BR>
</CENTER>
$HR
(�{��)<BR>
�L����ǂރ��[�h�ł��B
�ŏ��̉�ʃ��[�h�ł��B
�y�[�W�̕ύX�́u���H���v
�u�O�H���v�u�擪�v�����N��
�g���ĉ������B<BR>
<BR>
(���e)<BR>
�L���𓊍e���郂�[�h�ł��B
�p�X���[�h���ݒ肳��Ă���ꍇ��
�f���^�c�҂������p�X���h��
���Ă���A���e��ʂ֐i��ł��������B
���e��ʂɐi�񂾂�A�e���ڂ𖄂߂�
���e�{�^���������ĉ������B
���e����ƁA�S���̏�A�ԍ��������I��
�U���܂��B������L�����Ă����܂��傤�B
�Q�x�ڈȍ~�̓��͎��ɑO��̓��̓f�[�^��
�����ł���悤�ɂȂ�A���͂��y�ɂȂ�܂�
(i�N�b�L�[�@\�\\)�B
<P>
(�摜/���擊�e)<BR>
51,52,53�ذ�ވȍ~��J-SKY �߹�đΉ�\�@\(Ѱ�ގ�Ұً@)�͒��ڎʐ^����۰�މ�\�\\�ł��B<BR>�Ȃ��A���̑��̎ʃ��[���@�AEZ�̃t�H�g���[���Ai-shot������͉摜�𓊍e�ł��܂���B�����̶�וt���g�тɊւ��ẮA���݊J�����̃X�N���v�g�u�S��וt���g�ёΉ���imgboard 2010�v����̑Ή��ɂȂ�܂��̂ŁA��������g�����������B

<P>
(�폜)<BR>
�Ǘ��l�͊Ǘ����j���[����폜���j���[���o���A��������
�L���̍����Ƀ`�F�b�N�����āA�Ǘ��p�X���h���ŉ�����
�L�����A�폜�{�^���������č폜�B
(�g�т���̍폜�́A�Ǘ��l�̂݉�)<p>

(���̑�)<BR>
���݁A�K���p�S�X�g��(i-mode�ASoftBank�AEZweb)��v�@��S�Ή��B


2012.08����
��ȑΉ��󋵂ł��B
<BR>
<BR>
�h�R��<BR>
�SFOMA<BR>
<BR>
SoftBank<BR>
3G�@ <BR>
<BR>
au(EZweb)<BR>
3G�@ <BR>


<BR>
$accesskey_p1<a href="$cgi_name?page=$FORM{'page'}&viewpass=$FORM{'viewpass'}&mode=disp_admin_menu" accesskey=0>�߂�</a><BR>
$HR
</BODY>
</HTML>
HTML_END
}
#
#===============================================#
#     <�g�s�l�k--�Ǘ����j���[(���[�h����)>            #
#===============================================#
#
#  �Ǘ����j���[(���[�h�������j���[)�p�̂g�s�l�k�ł��D
#
sub output_search_menu_HTML{

	local($mes_p1);
	local($mes_p2);

	if($FORM{'MatchMode'} eq "OR"){
		$mes_p1="selected";
	}else{
		$mes_p2="selected";
	}

print<<HTML_END;
<HTML>
<HEAD>$top_html_header</HEAD>
<BODY BGCOLOR=PINK>
�摜Upload�f����<BR>
<CENTER>
(�g�ѱ���)<BR>
<BR>
���[�h����<BR>
</CENTER>
$HR
�L���̑S���������s���܂��B�����̃��[�h����͂���ꍇ�͔��p�X�y�[�X�Ŋe�P�����؂��ē��͂��Ă�������
<FORM METHOD=GET action="$cgi_name">
<INPUT TYPE=HIDDEN NAME="mode" VALUE="search_menu">
<INPUT TYPE=TEXT SIZE=15 NAME="SearchWords" MAXLENGTH=40 istyle=1 MODE=hiragana VALUE="$FORM{'SearchWords'}">
<BR>
<SELECT NAME="MatchMode">
<OPTION VALUE="AND" $mes_p2>AND ����
<OPTION VALUE="OR" $mes_p1>OR ����
</SELECT>
<BR><BR>
<CENTER>
<INPUT TYPE=SUBMIT VALUE="�������s">
</FORM>
<BR>
$accesskey_p1<a href="$cgi_name?page=$FORM{'page'}&viewpass=$FORM{'viewpass'}" accesskey=0>�����I��</a><BR>
</CENTER>
HTML_END
}
#
sub output_search_menu_HTML2{
print<<HTML_END;
</BODY>
</HTML>
HTML_END
}
#
#===============================================#
#     <�g�s�l�k--�Ǘ����j���[(imgboard�Ƃ�)>    #
#===============================================#
#
#  �Ǘ����j���[(imgboard���)�p�̂g�s�l�k�ł��D
#
sub output_whats_imgboard_HTML{
print<<HTML_END;
<HTML>
<HEAD>$top_html_header</HEAD>
<BODY BGCOLOR=PINK>
�摜Upload�f����<BR>
<CENTER>
(�g�ѱ���)<BR>
<BR>
imgboard�Ƃ�<BR>
</CENTER>
$HR
�摜����۰�ނł���@�\\��������Free�̌f���ł��B�ݒ肪�ȒP�Őݒu���₷���A����\�\\���E���@\�\\�Ȃ̂������ŁA���ݐݒu���͐���Aհ�ނ͐����l����A̧�ٱ���۰�ދ@�\\�������f���̒�ԂƂ��āA�����̊F�l���炲���ڂ��������Ă���܂��B<BR>
<BR>
<CENTER>
�g�ѱ���CGI�Ƃ�
</CENTER>
<BR>
�摜Upload�f����(�g�ѱ���CGI)�́Aimgboard�^�p�҂₻�̂��F�B��հ�ޕ��X����̗v�]�ɉ����āA�K���p�S�X�g�їp�ɊJ�������ǉ������Ăł��B�Ȃ��A���̽����ẮA��{�I�ɂ͒P�̂ł͓����܂���̂ŁAimgboard�Ƒg���킹�Ă��g�p���������B
<BR>

$accesskey_p1<a href="$cgi_name?page=$FORM{'page'}&viewpass=$FORM{'viewpass'}&mode=disp_admin_menu" accesskey=0>�߂�</a><BR>
$HR
</BODY>
</HTML>
HTML_END
}
#
#=============================================#
#     <�g�s�l�k--�摜��Y�t���邩�m�F>        #
#=============================================#
#
#  R7NEW
#
sub output_attach_confirm_HTML{

	local($mes_p1);
	local($mes_p2);
	local($mes_p8);
	local($mes_p9);

	# iOS6�œK��
	if($MYCGI_ENV{'iOS_VER'} > 5 ){
	 $mes_p2 =qq|(��׌g��/au)|;
	}else{
	 $mes_p2 =qq|(��׌g��/au)|;
	}

	if($keitai_flag eq "imode"){
	  if($imode_ver >= 2){
		$mes_p2 =qq|(���^��׌g��/au)|;
	  }
	}elsif($keitai_flag eq "J-PHONE"){
	  if($jstation_flag >= 6){
		$mes_p2 =qq|(���^��׌g��/au)|;
	  }elsif($jstation_flag >= 4){
		$mes_p2 =qq|(��׌g��/au)|;
	  }else{
	  }
	}
	if($FORM{'parent'} ne ""){
	   if($PM{'use_rep'} == 1 ){
		$mes_p8 =qq|�L��$FORM{'parent'}�ɕԐM<BR>|;
	   }
	}

	if($PM{'use_post_password'} == 1 ){ 
		$mes_p9 ='disp_member_check';
	}else{
		$mes_p9 ='disp_input_menu';
	}


print<<HTML_END;
$HR
<CENTER>
$mes_p8
���O�m�F<BR>
</CENTER>
$HR
1.(�摜��)<BR>
<BR>
HTML_END

if($keitai_flag eq "J-PHONE"){
print<<HTML_END;
<FORM ACTION="$cgi_name" METHOD="$form_method">
<INPUT TYPE="hidden" NAME="mode" VALUE="$mes_p9">
<INPUT TYPE="hidden" NAME="up" VALUE="file_tag">
<INPUT TYPE="hidden" NAME="blood" VALUE="$FORM{'blood'}">
<INPUT TYPE="hidden" NAME="parent" VALUE="$FORM{'parent'}">
1.1�߿�݂Ɠ���FILE�^�O�ɂ�钼�ړ��e��(911T�ȍ~��softbank3G*)
<BR>
<INPUT TYPE="submit" VALUE=" GO ">
</FORM>
(��)*Ѱ�ގ�Ұق�FILE�^�O�œ��e�ł��Ȃ��̂ŁAҰٓY�t�œ��e���Ă��������B
<BR>
<BR>
HTML_END
}elsif(($keitai_flag eq "imode")||($keitai_flag eq "pc")){

 if($http_upload_ok_flag == 1){
print<<HTML_END;
<FORM ACTION="$cgi_name" METHOD="$form_method">
<INPUT TYPE="hidden" NAME="mode" VALUE="$mes_p9">
<INPUT TYPE="hidden" NAME="up" VALUE="file_tag">
<INPUT TYPE="hidden" NAME="blood" VALUE="$FORM{'blood'}">
<INPUT TYPE="hidden" NAME="parent" VALUE="$FORM{'parent'}">
1.1�߿�݂Ɠ���FILE�^�O�ɂ�钼�ړ��e��(FOMA906i/706i�ȍ~�̃h�R���g��)
<BR>
<INPUT TYPE="submit" VALUE=" GO ">
(��)*�p�P�㒍�ӁB�p�P�z�_�u���K�{�B�J�����ݒ��FINE�łȂ��A�m�[�}����ݒ�B�t�@�C���T�C�Y��500KB�ȉ��ɂ��邱�ƁB
</FORM>
<BR>
HTML_END

 # 2010.09 �t���u���E�U�֗U������ׂ��@������o
 }elsif($http_upload_fullb_only_flag == 1){
 
print<<HTML_END;
FOMA904/905/704/705/706��imode�u���E�U�ł͉摜���e���ł��܂��񂪁A
�t���u���E�U��PC�p�̌f���ɃA�N�Z�X���āA�t�@�C���Y�t����`�œ��e�\�ł��B
<a href="$PM{'cgi_hontai_name'}" ifb="$PM{'cgi_hontai_name'}">�t���u���E�U </a> �������p���������B
<BR>
(��)*�p�P�㒍�ӁB�p�P�z�_�u���K�{�B�J�����ݒ��FINE�łȂ��A�m�[�}����ݒ�B�t�@�C���T�C�Y��500KB�ȉ��ɂ��邱�ƁB
<BR>
HTML_END
 }

}elsif($keitai_flag eq "pc"){


}

print<<HTML_END;
<FORM ACTION="$cgi_name" METHOD="$form_method">
<INPUT TYPE="hidden" NAME="mode" VALUE="disp_mail_form">
<INPUT TYPE="hidden" NAME="up" VALUE="m2w">
<INPUT TYPE="hidden" NAME="blood" VALUE="$FORM{'blood'}">
<INPUT TYPE="hidden" NAME="parent" VALUE="$FORM{'parent'}">
<BR>
1.2ҰٓY�t2�i��$mes_p2<BR>
<BR>
<INPUT TYPE="submit" VALUE=" GO ">
</FORM>
<BR>
1.3 �t���u���E�U��(iPhone/iPad/iPod)<BR>
<a href="$PM{'cgi_hontai_name'}" ifb="$PM{'cgi_hontai_name'}">�t���u���E�U </a> �������p���������B<BR>
<BR>
<BR>
<BR>
HTML_END

print<<HTML_END;
<FORM ACTION="$cgi_name" METHOD="$form_method">
<INPUT TYPE="hidden" NAME="mode" VALUE="$mes_p9">
<INPUT TYPE="hidden" NAME="up" VALUE="text_only">
<INPUT TYPE="hidden" NAME="blood" VALUE="$FORM{'blood'}">
<INPUT TYPE="hidden" NAME="parent" VALUE="$FORM{'parent'}">
<INPUT TYPE="hidden" NAME="page" VALUE="$FORM{'page'}">
$HR
2.(��������)
<BR>
<INPUT TYPE="submit" VALUE=" GO ">
</FORM>


<BR>
<CENTER>
$accesskey_p1<a href="$cgi_name?page=$FORM{'page'}&viewpass=$FORM{'viewpass'}" accesskey=0>�߂�</a>
</CENTER>
$HR
</BODY>
</HTML>
HTML_END
}
#
#=====================================#
#     <�g�s�l�k--�����o�[�m�F>        #
#=====================================#
#
#  �����o�[�m�F�p�̂g�s�l�k�ł��D
#
sub output_member_check_HTML{

	local($mes_p1);
	local($mes_p2);
	local($mes_p3);
	local($mes_p4);
	local($mes_p5);
	local($mes_p8);
	local($mes_p9);
	local($mes_p10);

	if($keitai_flag eq "imode"){
		$mes_p1=qq|istyle="4"|;
		$mes_p2=qq|istyle="4"|;
	}elsif($keitai_flag eq "J-PHONE"){
		$mes_p1=qq|MODE=numeric|;
		$mes_p2=qq|MODE=numeric|;
	  if($jstation_flag >= 4){
		$mes_p4=qq|�V�^|;
	  }else{
		$mes_p4=qq|���^|;
	  }
	}
	if($FORM{'parent'} ne ""){
	   if($PM{'use_rep'} == 1 ){
		$mes_p8 =qq|�L��$FORM{'parent'}�ɕԐM<BR>|;
	   }
	}
	if($FORM{'up'} eq "m2w"){
		if($FORM{'eURL'}=~ /httpEnc_cln/i){
			$mes_p9=qq| ҰٓY�t�^���e�̑������s���܂� |;
		}
	}


if($PM{'use_post_password'}==1){

print<<HTML_END;
$HR
<CENTER>
$mes_p8
�����o�[�m�F<BR>
</CENTER>
$HR
$mes_p9
<FORM ACTION="$cgi_name" METHOD="$form_method">
����߽���\*<BR>
<INPUT TYPE="password" NAME="entrypass" SIZE=4 VALUE="$COOKIE{'entrypass'}" MAXLENGTH="8" $mes_p1><BR><BR>
HTML_END

$mes_p5=qq|*�^�c�҂���ʒm���ꂽ�߽��ނ����|;

}else{

print<<HTML_END;
$HR
<CENTER>
$mes_p9<BR>
$mes_p8<BR>
$mes_p10 �u���ցv�������Ă�������<BR>
</CENTER>
$HR
<FORM ACTION="$cgi_name" METHOD="$form_method">
<INPUT TYPE="hidden" NAME="entrypass" VALUE="$PM{'post_passwd'}" MAXLENGTH="8">
HTML_END
}

print<<HTML_END;
<INPUT TYPE="hidden" NAME="mode" VALUE="disp_input_menu">
<INPUT TYPE="hidden" NAME="up" VALUE="$FORM{'up'}">
<INPUT TYPE="hidden" NAME="blood" VALUE="$FORM{'blood'}">
<INPUT TYPE="hidden" NAME="parent" VALUE="$FORM{'parent'}">
<INPUT TYPE="hidden" NAME="page" VALUE="$FORM{'page'}">
<INPUT TYPE="hidden" NAME="eURL" VALUE="$FORM{'eURL'}">
<INPUT TYPE="hidden" NAME="sqid" VALUE="$FORM{'sqid'}">
<INPUT TYPE="submit" VALUE="����">
</FORM>

 $mes_p5
<BR>
<BR>
<CENTER>
$accesskey_p1<a href="$cgi_name?page=$FORM{'page'}&viewpass=$FORM{'viewpass'}" accesskey=0>���~</a>
</CENTER>
$HR
</BODY>
</HTML>
HTML_END
}
#
#=====================================#
#     <�g�s�l�k--�����o�[�m�F>        #
#=====================================#
#
#  �����o�[�m�F�p�̂g�s�l�k�ł��D
#
sub output_view_member_check_HTML{

	local($mes_p1);
	local($mes_p2);
	local($mes_p3);
	local($mes_p4);
	local($mes_p5);
	local($mes_p8);

	if($keitai_flag eq "imode"){
		$mes_p1=qq|istyle="4"|;
	}elsif($keitai_flag eq "J-PHONE"){
		$mes_p1=qq|MODE=numeric|;
	}


print<<HTML_END;
$HR
<CENTER>
$mes_p8
�����o�[�m�F<BR>
</CENTER>
$HR

<FORM ACTION="$cgi_name" METHOD="$form_method">
�{���߽���\*<BR>
<INPUT TYPE="password" NAME="viewpass" SIZE=4 VALUE="$COOKIE{'viewpass'}" MAXLENGTH="8" $mes_p1><BR><BR>
<INPUT TYPE="hidden" NAME="mode" VALUE="">
<INPUT TYPE="hidden" NAME="eURL" VALUE="$FORM{'eURL'}">
<INPUT TYPE="submit" VALUE="����">
</FORM>

(���P)���̔ɂ͉{���߽���ݒ肳��Ă��܂��B�^�c���߽��ނ������Ă�����Ă������� �B
<BR>
$HR
</BODY>
</HTML>
HTML_END
}
#
#=============================#
#     <�g�s�l�k--�f�o�b�N>    #
#=============================#
#
#  �f�o�b�N�p�̂g�s�l�k�ł��D
#
sub output_check_env_HTML{
print<<HTML_END;
<HTML>
<HEAD>$top_html_header</HEAD>
<BODY BGCOLOR=PINK>
�摜Upload�f����<BR>
<CENTER>
<BR>
</CENTER>

�f�o�b�N�p<BR>
$HR
<BR>
Debug<BR>
<BR>
HTTP_USER_AGENT<BR>
$HTTP_USER_AGENT<BR>
<BR>
REMOTE_HOST<BR>
$REMOTE_HOST<BR>
<BR>
REMOTE_ADDR<BR>
$ENV{'REMOTE_ADDR'}<BR>
<BR>
SERVER_ADDR<BR>
$ENV{'SERVER_ADDR'}<BR>
<BR>
HTTP_REFERER<BR>
$HTTP_REFERER<BR>
<BR>
TOKEN<BR>
$uniq_token<BR>
<BR>
SERVICE_COMPANY<BR>
$KEITAI_ENV{'SERVICE_COMPANY'}<BR>
<BR>
HTTP_VERSION<BR>
$KEITAI_ENV{'HTTP_VERSION'}<BR>
<BR>
MACHINE_TYPE<BR>
$KEITAI_ENV{'MACHINE_TYPE'}<BR>
<BR>
DISPLAY-WH<BR>
$KEITAI_ENV{'DISPLAY_WIDTH'} x $KEITAI_ENV{'DISPLAY_HEIGHT'}<BR>
<BR>
CACHE_SIZE<BR>
$KEITAI_ENV{'CACHE_SIZE'} KB<BR>
<BR>
STREAM_SPEED<BR>
$KEITAI_ENV{'STREAM_SPEED'}<BR>
<BR>
OTHER_PARAM<BR>
$KEITAI_ENV{'OTHER_PARAM'}<BR>
<BR>
keitai_f $keitai_flag <BR>
jstation $jstation_flag<BR>
au_3G $au_3G_flag<BR>
http_upload $http_upload_ok_flag<BR>
wmv_play $wmv_play_flag<BR>
cookie $cookie_ok_flag<BR>
imode_ver $imode_ver<BR>
<BR>
$accesskey_p1<a href="$cgi_name?page=$FORM{'page'}&viewpass=$FORM{'viewpass'}&mode=disp_admin_menu" accesskey=0>�߂�</a><BR>
$HR
</BODY>
</HTML>
HTML_END
}
#=====================================#
#     <�G�����폜>                    #
#=====================================#
#
sub remove_emoji_i{
 local($target_str)	= $_[0];# �����ł��炤
 $target_str =~ s/\G((?:[\x80-\x9F\xE0-\xEF\xFA-\xFC][\x40-\x7E\x80-\xFC]|[\x00-\x7F]|[\xA1-\xDF])*)(?:[\xf8\xf9][\x40-\xff]|[\xf0-\xf4][\x40-\xff])/$1/go;
 return("$target_str");
}


# �X�N���v�g�I�[�ł�






