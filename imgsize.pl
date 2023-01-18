#!/usr/local/bin/perl
######################################################################
#  IMGSIZE  Ver.1.71   (�摜�̃X�N���[���T�C�Y��́��ύX�j          ##
#                 -- Last Updated 2003/03/21 --                     ##
######################################################################
#                                                                     
# imgsize.pl - show screen size of image
# Copyright (C) 1998 TANAKA Katsunori <tkatsu@mx2.nisiq.net>
# Copyright (C) 1998-2002 Kenta Ogo  <ogo@ta2.so-net.ne.jp>
# Copyright (C) 2001 �@��B��iTED�j <ted@uranus.interq.or.jp>
#
# (http://www.big.or.jp/~talk/t-club/soft/)
#
# <���ϗ���>-03/21/03
#  2003/03/21 JPEG�w�b�_�̒T���͈͂Ƀ��~�b�^������
#  2002/09/02 Perl4�ł����Ȃ�500�G���[�ŔY�ސl���������̂ŁAmy�ϐ�����߂�
#  2002/08/21 BMP�t�@�C���Ή��B
#  2002/08/21 �ϐ������d�Ȃ�ɂ��������Bmy�ϐ��𑝂₵���i�vPerl5�j
#  2001/03/01 TED����̋��͂ɂ��PNG�ɑΉ��BTED����Ɋ��ӂł�
#
# [�C���[�W�T�C�Y�Ƃ�]
# GIF,PNG,JPEG,BMP�摜�̏c���̃s�N�Z���l���킩��Perl���C�u�����ł�
# �摜�t�@�C���̃w�b�_���o�C�g��ǂ݁A�������͂���
# GIF/JPEG/PNG/BMP/OHTER ���ʁA�y�сA�c���s�N�Z���l�����o�͂��܂�
#
# [�g�p���@]
# perl�X�N���v�g����imgsize.pl��require���A�T�u���[�`��
# &imgsize("target_file");�����s����
# ��͂ɐ������A�T�C�Y�l������ꂽ��1�A
# �T�C�Y�l�������Ȃ����0���Ԃ�܂�
#
# [�g�p��]
# &imgsize("test.gif");
# if($IMGSIZE{'result'}==1){
#     print "<IMG SRC=test.gif height=$IMGSIZE{'height'} width=$IMGSIZE{'width'}>\n;
# }
#	���ʂ͈ȉ��̕\�L�ŌĂяo�������ł��܂�
#	$IMGSIZE{'result'}	 �T�C�Y�l�擾����=1�A���s=0
#	$IMGSIZE{'type'}	 �摜�̃^�C�v[GIF|PNG|JPEG|BMP|OTHER]
#	$IMGSIZE{'width'} 	 �摜�̉���[xx|no_data]
#	$IMGSIZE{'height'} 	 �摜�̏c��[xx|no_data]
#	$IMGSIZE{'file_name'} 	 ���t�@�C����
#	$IMGSIZE{'hw_racio'} 	 �c����(1:1=100)
#	$IMGSIZE{'zoom'} 	 �Y�[����(1:1=100)
#	$IMGSIZE{'max_length'} 	 ���ӂ̒���
#	$IMGSIZE{'square'} 	 �ʐ�(dot)
#	$IMGSIZE{'error_message'}�G���[���b�Z�[�W�i�ʏ�͋�j
#
#
# [���p�K��]
# [1]���R�s�[���C�g���A�^�C�g�����ȊO�̃v���O�������́A�l�Ŏg�p����
#    ����ɂ����āA���R�ɉ������Ă�����č\���܂���  �܂������Ŏg�p��
#    ���܂�  
# [2]���������쌠�͕������Ă܂���̂ŁA�����A��������킸���f�ł�
#    �Ĕz�z�͌ł��֎~���܂�  �i���k����ΉɂȂ�ꍇ����j
# [3]�c���ړI�Ɏg�p���邱�Ƃ��֎~���܂�  
# [4]���ꂱ��CGI�ɂ�葹�Q��s���v�󂯂��Ƃ��Ă��A�����͈�؂��̐ӔC�𕉂�
#    �`���������܂���  ���炩���߂�������������  
# [5]���R�̔@�����킸�A���̃^�C�g�����A�y�сA�R�s�[���C�g���͍폜�A
#    ���H���邱�Ƃ��֎~���܂�  ���������ꍇ�͗��O�ɒǋL���Ă�������  

######################################################################

$imgsize_version='20020902';	#imgsize�̃o�[�W����
$imgsize_lib_flag='1';		#���̃t���O�ŃT�u���[�`���̑��݊m�F


sub imgsize{

# imgsize.pl - show screen size of image
# Copyright (C) 1998 TANAKA Katsunori <tkatsu@mx2.nisiq.net>
# Copyright (C) 2001 TED <ted@uranus.interq.or.jp> (PNG support)
#
# I wrote the subroutine jpeg_size, referring to rdjpgcom.c
# contained in the Independent JPEG Group's software.
#
# $Id: imgsize.pl,v 1.5 1998/08/20 13:17:24 tkatsu Exp $

# constants.

    local($IMGSIZE_READ_HEAD) = 10;
    local($GIF_SKIP_HEAD)  = 6;
    local($GIF_SIZE_INFO)  = 4;
    local($JPEG_SKIP_HEAD) = 2;
    local($JPEG_SKIP_LENGTH_AND_BPS) = 3;
    local($JPEG_SIZE_INFO) = 4;
    local($JPEG_LENGTH)    = 2;
    local($PNG_SKIP_HEAD)  = 12;
    local($PNG_SIZE_INFO)  = 12;
    local($BMP_SKIP_HEAD)  = 18;
    local($BMP_SIZE_INFO)  =  8;

# main routine.

	# �ϐ������d�Ȃ�ɂ������̂ɕύX(2002.09)
	local($imsz_smooze_mode);
	local($imsz_file)	="$_[0]";       #File name
	local($imsz_action)	="$_[1]";	#action
	local($imsz_parameter1)	="$_[2]";	#parameter1
	local($imsz_parameter2)	="$_[3]";	#parameter2
	local($imsz_parameter3)	="$_[4]";	#parameter3

	$imsz_parameter1		=~ s/\%//g;	#remove character "%"
	$imsz_parameter2		=~ s/\%//g;	#remove character "%"
	$imsz_parameter2		=~ s/dot//g;	#remove character "dot"
	$imsz_parameter2		=~ s/pixel//g;	#remove character "pixel"


	local($imsz_width,$imsz_height);
	undef $e_mes;
	undef $p_type;
	undef %IMGSIZE;

    # return status: 1 for success, 0 for failure.
    local($imsz_status) = 1;
    local($imsz_current_status) = 1;
    local($imsz_type);

    $ddd="imgsize skip success!!";
 
  if($imsz_file ne 'dummy'){
    $ddd="imgsize done..";
    unless (open(FILE, $imsz_file)) {
	$e_mes.= "$0: can't open $imsz_file<BR>\n";
	$imsz_current_status = 0;
    }
	binmode(FILE);	# �����ӏ�

    &ident_type == 0 && ($imsz_current_status = 0);

    if ($imsz_current_status == 1 && $imsz_type == 1) {
	&gif_size == 0 && ($imsz_current_status = 0);
    } elsif ($imsz_current_status == 1 && $imsz_type == 2) {
	&jpeg_size == 0 && ($imsz_current_status = 0);
    } elsif ($imsz_current_status == 1 && $imsz_type == 3) {
	&png_size == 0 && ($imsz_current_status = 0);
    } elsif ($imsz_current_status == 1 && $imsz_type == 4) {
	&bmp_size == 0 && ($imsz_current_status = 0);
    }

    unless (close FILE) {
	$e_mes.= "$0: can't close $imsz_file<BR>\n";
	$imsz_current_status = 0;
    }

    unless ($imsz_current_status == 0) {
	&output_info;
    }
  
    &check_results ==0 && ($imsz_current_status =0);
    unless ($imsz_current_status == 0){
	&other_parameters;
    }
  }else{
    &input_prefetched_data;
  }

    unless ($imsz_current_status == 0){
	&imgsize_change_size_parameters;
    }

    undef $imsz_parameter1;
    undef $imsz_parameter2;
    undef $imsz_action;
    undef $imsz_height;
    undef $imsz_width;

    $imsz_current_status == 0 && ($imsz_status = 0);

    $IMGSIZE{'result'}=$imsz_status;	# �T�C�Y�l�擾����=1�A���s=0
    return $imsz_status;
}

# identify the image format.
sub ident_type {

    # Modified 99.09.01 by ogo
    local($in);
    local($r_HEAD);

    $r_HEAD=read(FILE, $in, $IMGSIZE_READ_HEAD);

#    if($r_HEAD != $IMGSIZE_READ_HEAD) {
#
#		$e_mes.= "$0: can't read $r_HEAD bytes from $imsz_file. <BR>\n";
#		return 0;
#    }

    if ($in=~ /^GIF/i) {
	$imsz_type = 1;
    } elsif ( $in=~ /\xff\xd8/ ) {
	$imsz_type = 2;
    } elsif ( $in=~ /^\x89PNG\x0D\x0A\x1A\x0A/ ) {	# �����ӏ�
	# ���������\r\n�������Ă���̂�UNIX�n�ȊO�ł�binmode�ɂ���K�v����B
	#   /^\x89PNG/�ŏ\�������m��܂��񂪁c�c(TED)
	$imsz_type = 3;
    } elsif ( $in=~ /BM/i ) {
	$imsz_type = 4;
    } else {
	$imsz_type = 0;
    }
    return 1;
}

# get the screen size.
sub gif_size {
    local($in, $w1, $w2, $h1, $h2);
    seek(FILE, $GIF_SKIP_HEAD, 0);
    unless (read(FILE, $in, $GIF_SIZE_INFO) == $GIF_SIZE_INFO) {
	$e_mes.= "$0: can't read $GIF_SIZE_INFO bytes from $imsz_file<BR>\n";
	return 0;
    }
    ($w1, $w2, $h1, $h2) = unpack("CCCC", $in);
    $imsz_width = $w1 + $w2 * 256;
    $imsz_height = $h1 + $h2 * 256;
    return 1;
}

# get the screen size.
sub jpeg_size {
    local($in, $w1, $w2, $h1, $h2, $l1, $l2, $length,$max_loop_limit);
    seek(FILE, $JPEG_SKIP_HEAD, 0);

    # 2003.03 ���S���u��ǉ�
    for($max_loop_limit=0;$max_loop_limit < 100000000 ;$max_loop_limit++){
	$in = getc(FILE); # 1�����ǂݍ���
	if (!$in) {
	    return 0; # getc�œǂݍ��݂��ł��Ȃ��Ȃ�����A���[�v�I��
	} elsif ($in eq "\xff") {
	    $in = getc(FILE);
	    if ($in eq "\xc0" || $in eq "\xc1" || $in eq "\xc2" ||
		$in eq "\xc3" || $in eq "\xc5" || $in eq "\xc6" ||
		$in eq "\xc7" || $in eq "\xc9" || $in eq "\xca" ||
		$in eq "\xcb" || $in eq "\xcd" || $in eq "\xce" ||
		$in eq "\xcf") {
		seek(FILE, $JPEG_SKIP_LENGTH_AND_BPS, 1);
		unless (read(FILE, $in, $JPEG_SIZE_INFO) == $JPEG_SIZE_INFO) {

		    $e_mes.= "$0: can't read $JPEG_SIZE_INFO bytes from $imsz_file<BR>\n";

		    return 0;
		}
		($h1, $h2, $w1, $w2) = unpack("CCCC", $in);
		$imsz_height = $h1 * 256 + $h2;
		$imsz_width = $w1 * 256 + $w2;
		return 1;
	    } elsif ($in eq "\xd9" || $in eq "\xda") {
		return 0;
	    } else {
		unless (read(FILE, $in, $JPEG_LENGTH) == $JPEG_LENGTH) {
		    $e_mes.= "$0: can't read $JPEG_LENGTH bytes from $imsz_file<BR>\n";
		    return 0;
		}
		($l1, $l2) = unpack("CC", $in);
		$length = $l1 * 256 + $l2;
		seek(FILE, $length - 2, 1);
	    }
	}
    }
    return 0;
}

# �����ӏ� / PNG�摜�̃T�C�Y��ǂݎ��ǉ��T�u���[�`��
# �c�܂��͉��T�C�Y��65536���z����摜�ɂ��Ή�
sub png_size {
    local($in, $dummy);
    seek(FILE, $PNG_SKIP_HEAD, 0);
    unless (read(FILE, $in, $PNG_SIZE_INFO) == $PNG_SIZE_INFO) {
	$e_mes.= "$0: can't read $PNG_SIZE_INFO bytes from $imsz_file<BR>\n";
	return 0;
    }
	unless ($in =~ /^IHDR/) {
	return 0;
	}
	($dummy, $imsz_width, $imsz_height) = unpack("a4N2", $in);
	return 1;
}

sub bmp_size {
    local($in, $dummy);
    seek(FILE, $BMP_SKIP_HEAD, 0);
    unless (read(FILE, $in, $BMP_SIZE_INFO) == $BMP_SIZE_INFO) {
	$e_mes.= "$0: can't read $BMP_SIZE_INFO bytes from $imsz_file<BR>\n";
	return 0;
    }
    ($imsz_width, $imsz_height) = unpack("V2", $in);
    return 1;
}

# output result
sub output_info {

	undef %IMGSIZE;
	undef $imgsize_result;

    if ($imsz_type == 1) {
	$imgsize_result="$imsz_file: $imsz_width"."w "."$imsz_height"."h "."GIF\n";
	$IMGSIZE{'type'} 	='GIF';
	$IMGSIZE{'width'} 	="$imsz_width";
	$IMGSIZE{'height'} 	="$imsz_height";
	$IMGSIZE{'file_name'} 	="$imsz_file";
	$IMGSIZE{'zoom'} 	="100";
    } elsif ($imsz_type == 2) {
	$imgsize_result="$imsz_file: $imsz_width"."w "."$imsz_height"."h "."JPEG\n";
	$IMGSIZE{'type'} 	='JPEG';
	$IMGSIZE{'width'} 	="$imsz_width";
	$IMGSIZE{'height'} 	="$imsz_height";
	$IMGSIZE{'file_name'} 	="$imsz_file";
	$IMGSIZE{'zoom'} 	="100";
    } elsif ($imsz_type == 3) {
	$imgsize_result="$imsz_file: $imsz_width"."w "."$imsz_height"."h "."PNG\n";
	$IMGSIZE{'type'} 	='PNG';
	$IMGSIZE{'width'} 	="$imsz_width";
	$IMGSIZE{'height'} 	="$imsz_height";
	$IMGSIZE{'file_name'} 	="$imsz_file";
	$IMGSIZE{'zoom'} 	="100";
    } elsif ($imsz_type == 4) {
	$imgsize_result="$imsz_file: $imsz_width"."w "."$imsz_height"."h "."BMP\n";
	$IMGSIZE{'type'} 	='BMP';
	$IMGSIZE{'width'} 	="$imsz_width";
	$IMGSIZE{'height'} 	="$imsz_height";
	$IMGSIZE{'file_name'} 	="$imsz_file";
	$IMGSIZE{'zoom'} 	="100";
    } else {
	$imgsize_result="$imsz_file: OTHER\n";
	$IMGSIZE{'type'} 	='OTHER';
	$IMGSIZE{'file_name'} 	="$imsz_file";
    }
    $IMGSIZE{'error_message'} 	="$e_mes";
}

#===================================#
#  ���ʂ̃`�F�b�N(0���Z������h��)
#===================================#

sub check_results{
    local($tmp_status)=1;	#1=ok,0=cannot_use_size_parameter
    unless($IMGSIZE{'width'} > 0 ){
	$tmp_status=0;
	$IMGSIZE{'width'}=1;
    }
    unless($IMGSIZE{'height'} > 0 ){
	$tmp_status=0;
	$IMGSIZE{'height'}=1;
    }
    return $tmp_status;
}

#==================#
#  ���̕ϐ��̌v�Z
#==================#

sub other_parameters{
	if(($IMGSIZE{'height'} > 0 )&&($IMGSIZE{'width'} > 0 )){
		$IMGSIZE{'hw_racio'} 	=int(100*$IMGSIZE{'height'}/$IMGSIZE{'width'});
	}
	$IMGSIZE{'hw_racio'}=100 unless($IMGSIZE{'hw_racio'} > 0 );
	# 0�̎���100�ɂ���  (0���Z�h�~)

	if($IMGSIZE{'hw_racio'} >= 100){
		$IMGSIZE{'max_length'}=$IMGSIZE{'height'};
	}else{
		$IMGSIZE{'max_length'}=$IMGSIZE{'width'};
	}

	$IMGSIZE{'square'}=$IMGSIZE{'width'}*$IMGSIZE{'height'};
}

#================================================================#
# �C���[�W�T�C�Y���H���C�u����
# Copyright (C) 1998,2001 Kenta Ogo <ogo@ta2.so-net.ne.jp>
#
# [�C���[�W�T�C�Y���H���C�u�����Ƃ�]
# sub imgsize�œ���GIF�APNG�AJPEG�摜�̏c���T�C�Y��������
# ������ނ��̉��H�p�^�[�����{�����C�u�����ł�  
# Web�ł悭�g�p���鏈�����܂Ƃ߂܂���  
#
#
# [�g�p���@]
# �{������imgsize.pl��require���A�T�u���[�`��
# &imgsize("����1","����2","����3","����4","����5")�����s����;
#
# ����1�̓t�@�C�����A����2�͏�����ʁi�A�N�V�����j�A����3,4�̓p�����[�^�ł�
# ����5�͎w��l�̍ŏI�␳(smoozer����)�����邩�ǂ����̎w��ɗp���܂��B0��
#�u���g�p�v�A1�́u�掿�D��v,�Q�́u�掿�ŗD��v�ł��B����5��p�����ꍇ�́A
# �\������r�I���ꂢ�ɂȂ�܂����A�c���̎w��l�͋ߎ��l�����ɂȂ�A�w��l��
# �قȂ����l�ɃZ�b�g����܂��̂ł����ӂ��������B
#							
# �����Q		�����R		�����S		�����T		�Ӗ�	
# �������						�X���[�U		
# x_per			�{����		�Ȃ�		0,1,2		�w��{���֕ύX
# iconize		�x�[�X�T�C�Y	�Ȃ�		0,1,2		�A�C�R����
# static_width		���Œ�T�C�Y	�ő�c		0,1,2		���T�C�Y�Œ艻
# static_height		�c�Œ�T�C�Y	�ő剡		0,1,2		�c�T�C�Y�Œ艻
# limit_by_max_size	�c�������l	���������l	0,1,2		�ɒ[�ɑ傫�ȉ摜�̂ݏk��
#
#	���ʂ͈ȉ��̕\�L�ŌĂяo���Ă�������  
#
#	$IMGSIZE{'type'}	 �摜�̃^�C�v[GIF|PNG|JPEG|BMP|OTHER]
#	$IMGSIZE{'width'} 	 �摜�̉���[�I���W�i��]
#	$IMGSIZE{'height'} 	 �摜�̏c��[�I���W�i��]
#	$IMGSIZE{'out_width'} 	 �摜�̉���[���H��]
#	$IMGSIZE{'out_height'} 	 �摜�̏c��[���H��]
#	$IMGSIZE{'out_hw_racio'} �c����(1:1=100)
#	$IMGSIZE{'zoom'}	 ���H�O�Ɖ��H��̔�(1:1=100)
#
#     [��]test.gif�̃T�C�Y��50%�ɕύX���ĕ\��
#     &imgsize(test.gif,x_per,50%,,0)�����s����;
#
#     <IMG SRC=test.gif width=$IMGSIZE{'out_width'} height=$IMGSIZE{'out_height'}>
#
#    $imsz_action	="$_[1]";	#
#    $imsz_parameter1	="$_[2]";
#    $imsz_parameter2	="$_[3]";
#    $imsz_parameter3	="$_[4]";
#
#=====================#
#  ���C���v���O����
#=====================#

sub imgsize_change_size_parameters{


        # �ʏ�̗��p�`�Ԃ̏ꍇ
	  # �T�C�Y�擾�ɃG���[�̂��鎞��0���Z�ɂ��
          # �X�g�b�v��h�����߁A�ȉ��̏��������Ȃ�
	if($imsz_current_status == 0){
		$IMGSIZE{'out_result'}=0;
		return 0;
	}

	# �S�ڂ̈����̓X���[�U
	if($imsz_parameter3 ne ""){
		$imsz_smooze_mode="$imsz_parameter3";
	}else{
	# �w��
		if($CIMGSIZE{'smooze_mode'}==2){
			$imsz_smooze_mode=2;
		}elsif($CIMGSIZE{'smooze_mode'}==1){
			$imsz_smooze_mode=1;
		}elsif($CIMGSIZE{'smooze_mode'}==0){
			$imsz_smooze_mode=0;
		}else{
			$imsz_smooze_mode=0;
		}
	}

	&check_icon_files;	# �A�C�R���t�@�C�����ǂ������f����
				# �A�C�R���͊g��k�����Ă����ɂ�������
				# �Ȃ̂ŁA�g��k�����Ȃ�  

	# �ȉ��A�A�N�V�������ɉ��������H���s��  

	if($imsz_action eq 'x_per'){
		&change_x_per;		# �{���ύX
	}elsif($imsz_action eq 'iconize'){
		&iconize;		# �A�C�R����
	}elsif(($imsz_action eq 'auto_resize')&&($p_type ne 'icon')){
		&auto;			# �I�[�g
	}elsif(($imsz_action eq 'static_width')&&($p_type ne 'icon')){
		&static_width;		# �������w��T�C�Y�ɑ�����
	}elsif(($imsz_action eq 'static_height')&&($p_type ne 'icon')){
		&static_height;		# �c�����w��T�C�Y�ɑ�����
	}elsif($imsz_action eq 'limit_by_max_size'){
		&limit_by_max_size;	# �ɒ[�ɑ傫�ȉ摜�̂ݏk��
	}else{
		$IMGSIZE{'out_width'} =$IMGSIZE{'width'};
		$IMGSIZE{'out_height'}=$IMGSIZE{'height'};
	}
        # ���ʂ�Ԃ��i����=1;���s=0�j
	if(&check_out_results==0){
		$IMGSIZE{'out_result'}=0;
	}else{
		$IMGSIZE{'out_result'}=1;
	}
	&other_out_parameters;	

	return $IMGSIZE{'out_result'};
}


#=======================#
# �{��(%)�ŃT�C�Y�ύX
#=======================#

sub change_x_per{
# &imgsize("����1","����2","����3");�����s����
# �����P �摜�t�@�C����
# �����Q x_per
# �����R �g�k�{��(%)

		if($imsz_smooze_mode > 0){
			# IE �p�ߎ��v�Z�ɂ��掿�␳
			$imsz_parameter1=&img_smoozer_for_ie($imsz_parameter1,$imsz_smooze_mode);
		}
		$IMGSIZE{'out_width'} 	=int($imsz_parameter1*$IMGSIZE{'width'} /100);
		$IMGSIZE{'out_height'} 	=int($imsz_parameter1*$IMGSIZE{'height'}/100);
		$IMGSIZE{'zoom'} 	="$imsz_parameter1";
}

#============#
# �A�C�R����
#============#

sub iconize{
# &imgsize("����1","����2","����3");�����s����
# �����P �摜�t�@�C����
# �����Q iconize
# �����R �A�C�R���T�C�Y(�ȗ���)

	# �A�C�R���̑傫����ς������ꍇ�͈ȉ��̐��l��ύX
	local($base_size)='6000';#(default)
	local($tmp_x_per)  	="100";		#(default)

	# �����ɏd�݂����Čv�Z  ��ۂ��قړ��T�C�Y�ɂ���  	
	if($imsz_parameter1=~ /\d+/){
		$base_size  ="$imsz_parameter1";	
	}		

	local($now_size) =$IMGSIZE{'height'}*$IMGSIZE{'width'}*$IMGSIZE{'width'}*$IMGSIZE{'width'};
	$now_size=1 if($now_size <1); #0���Z�h�~
	local($area_racio)=sqrt(sqrt(10000*$base_size/$now_size));
	local($tmp_x_per)  	=int(100*$area_racio);		
	
	if($imsz_smooze_mode > 0){
		# IE �p�ߎ��v�Z�ɂ��掿�␳
		$tmp_x_per=&img_smoozer_for_ie(int($tmp_x_per),$imsz_smooze_mode);

		$IMGSIZE{'out_height'} 	=int($tmp_x_per*$IMGSIZE{'height'}/100);
		$IMGSIZE{'out_width'} 	=int($tmp_x_per*$IMGSIZE{'width'}/100);
		$IMGSIZE{'zoom'}	=int($tmp_x_per);
	}else{
		$IMGSIZE{'out_height'} 	=int($tmp_x_per*$IMGSIZE{'height'}/100);
		$IMGSIZE{'out_width'} 	=int($tmp_x_per*$IMGSIZE{'width'}/100);
		$IMGSIZE{'zoom'}	=int($tmp_x_per);
	}	
}

#================#
# �I�[�g���T�C�Y
#================#

sub auto{
# �A�C�R���Ƃ܂���������  �Ⴂ�̓f�t�H���g�̖ʐϐ��l���傫����  
# &imgsize("����1","����2","����3");�����s����
# �����P �摜�t�@�C����
# �����Q iconize
# �����R �A�C�R���T�C�Y(�ȗ���)

	# �A�C�R���̑傫����ς������ꍇ�͈ȉ��̐��l��ύX
	local($base_size)  ="600000";#(default)
	local($tmp_x_per)  	="100";		#(default)

	# �����ɏd�݂����Čv�Z  ��ۂ��قړ��T�C�Y�ɂ���  	
	if($imsz_parameter1=~ /\d+/){
		$base_size ="$imsz_parameter1";	
	}		


	local($now_size) =$IMGSIZE{'height'}*$IMGSIZE{'width'}*$IMGSIZE{'width'}*$IMGSIZE{'width'};

	$now_size=1 if($now_size <1); #0���Z�h�~

	local($area_racio)=sqrt(sqrt(10000*$base_size/$now_size));
	local($tmp_x_per)  	=int(100*$area_racio);		

	if($imsz_smooze_mode > 0){
		# IE �p�ߎ��v�Z�ɂ��掿�␳
		$tmp_x_per=&img_smoozer_for_ie(int($tmp_x_per),$imsz_smooze_mode);

		$IMGSIZE{'out_height'} 	=int($tmp_x_per*$IMGSIZE{'height'}/100);
		$IMGSIZE{'out_width'} 	=int($tmp_x_per*$IMGSIZE{'width'}/100);
		$IMGSIZE{'zoom'}	=int($tmp_x_per);
	}else{
		$IMGSIZE{'out_height'} 	=int($tmp_x_per*$IMGSIZE{'height'}/100);
		$IMGSIZE{'out_width'} 	=int($tmp_x_per*$IMGSIZE{'width'}/100);
		$IMGSIZE{'zoom'}	=int($tmp_x_per);
	}	

}

#==================#
# �������Œ艻����  
#==================#

sub static_width{
# �������Œ艻����  
# &imgsize("����1","����2","����3","����4")�����s����;
# �����P �摜�t�@�C����
# �����Q static_width
# �����R ����
# �����S �ő�c���E�l�i�ȗ��j
#
# �����R�Ŏw�肳�ꂽ�����ɌŒ艻  �������A�c���ʐ^�ł�
# �ɒ[�ɏc�������Ȃ��ʂ���͂ݏo��\��������̂ŁA�����S�ōő���E��
# �w��ł���  ���l���w�肳��ĂȂ��ꍇ�͈ȉ��̃f�t�H���g�l���g�p�����  

# width
	local($static_width)	="256";		#(default)
	local($tmp_x_per)  	="100";		#(default)

	if($imsz_parameter1=~ /\d+/){
		$static_width  ="$imsz_parameter1";	
	}		

	# ultimate height
	local($max_height)    =int(2*$static_width);#(default)

	if($imsz_parameter2=~ /\d+/){
		$max_height    ="$imsz_parameter2";
	}		

	if($imsz_smooze_mode > 0){	
	   # IE �p�ߎ��v�Z�ɂ��掿�␳
	   $tmp_x_per	 	=int(100*$static_width/$IMGSIZE{'width'});
	   $tmp_x_per=&img_smoozer_for_ie($tmp_x_per,$imsz_smooze_mode);
	   $IMGSIZE{'out_width'} 	=int($IMGSIZE{'width'}*$tmp_x_per/100);
	   $IMGSIZE{'out_height'} 	=int($IMGSIZE{'height'}*$tmp_x_per/100);
	   $IMGSIZE{'zoom'}	=int($tmp_x_per);	
	}else{
	   $IMGSIZE{'out_width'} 	=$static_width;
	   $IMGSIZE{'out_height'} 	=int($IMGSIZE{'hw_racio'}*$static_width/100);
	   $IMGSIZE{'out_height'}=1 if($IMGSIZE{'out_height'} <1); #0���Z�h�~
	   $IMGSIZE{'zoom'}	=int(100*$IMGSIZE{'height'}/$IMGSIZE{'out_height'});	
	}
	$IMGSIZE{'out_height'}	=$max_height if($IMGSIZE{'out_height'}>$max_height);

}


#==================#
#  �c�����Œ艻
#==================#

sub static_height{
# &imgsize("����1","����2","����3","����4");�����s����
# �����P �摜�t�@�C����
# �����Q static_height
# �����R �c��
# �����S �ő剡���E�l�i�ȗ��j
# �c�����Œ艻����  �����R�Ŏw�肳�ꂽ�c���ɌŒ艻  �������A�����ʐ^�ł�
# �������ɒ[�ɒ����Ȃ�A��ʂ���͂ݏo��\��������̂ŁA�����S��
# �ő剡���E���w��ł���i�ȗ��j  ���l���w�肳��ĂȂ��ꍇ�͈ȉ���
# �f�t�H���g�l���g�p�����  

# height
	local($static_height)  ="540";		#(default)
	local($tmp_x_per)  	="100";		#(default)

	if($imsz_parameter1=~ /\d+/){
		$static_height  ="$imsz_parameter1";	
	}		

	# ultimate width

	local($max_width)    =int(2*$static_height);#(default)

	if($imsz_parameter2=~ /\d+/){
		$max_width    ="$imsz_parameter2";
	}		

	if($imsz_smooze_mode > 0){	
	   # IE �p�ߎ��v�Z�ɂ��掿�␳
	   $tmp_x_per	 	=int(100*$static_height/$IMGSIZE{'height'});
	   $tmp_x_per=&img_smoozer_for_ie($tmp_x_per,$imsz_smooze_mode);
	   $IMGSIZE{'out_width'} 	=int($IMGSIZE{'width'}*$tmp_x_per/100);
	   $IMGSIZE{'out_height'} 	=int($IMGSIZE{'height'}*$tmp_x_per/100);
	   $IMGSIZE{'zoom'}	=int($tmp_x_per);	
	}else{
	   $IMGSIZE{'out_height'} 	=$static_height;
	   $IMGSIZE{'out_width'}   =int(100*$static_height/$IMGSIZE{'hw_racio'});
	   $IMGSIZE{'out_width'}	=$max_width if($IMGSIZE{'out_width'}>$max_width);
	   $IMGSIZE{'zoom'}	=int(100*$IMGSIZE{'width'}/$IMGSIZE{'out_width'});	
	}
	$IMGSIZE{'out_width'}	=$max_width if($IMGSIZE{'out_width'}>$max_width);
}


#==================#
#  �傫������
#==================#

sub limit_by_max_size{
# &imgsize("����1","����2","����3","����4");�����s����
# �����P �摜�t�@�C����
# �����Q max_limit_size
# �����R �c�������l
# �����S ���������l
# �����l�𒴂����ꍇ�̂݁A�c������ێ������܂܃T�C�Y���k������
# �����R�͏c�ő吧���l�A�����S�͉��ő吧���l  
# ���l���w�肳��ĂȂ��ꍇ�͈ȉ��̃f�t�H���g�l���g�p�����  
#
#
#
# max height
	local($limit_height)  ="540";		# (default)

	if($imsz_parameter1=~ /\d+/){
		$limit_height  ="$imsz_parameter1";	
	}		

# max width
	local($limit_width)    =780;# (default)

	if($imsz_parameter2=~ /\d+/){
		$limit_width    ="$imsz_parameter2";
	}		

	$IMGSIZE{'height'}=1 if($IMGSIZE{'height'} <1); #0���Z�h�~
	$IMGSIZE{'width'}=1  if($IMGSIZE{'width'} <1);  #0���Z�h�~
	$tmp_height_racio=int(100*$limit_height/$IMGSIZE{'height'});
	$tmp_width_racio =int(100*$limit_width/$IMGSIZE{'width'});

	local($tmp_x_per)  	="100";		#(default)
	
	if($tmp_height_racio < $tmp_width_racio){
	#height is critical
		if($tmp_height_racio < 101){
			#resize by height
			if($imsz_smooze_mode > 0){	
	   		  # IE �p�ߎ��v�Z�ɂ��掿�␳
	   		  $tmp_x_per	 	=int(100*$limit_height/$IMGSIZE{'height'});
	   		  $tmp_x_per=&img_smoozer_for_ie($tmp_x_per,$imsz_smooze_mode);
			  $IMGSIZE{'out_width'} 	=int($IMGSIZE{'width'}*$tmp_x_per/100);
			  $IMGSIZE{'out_height'} 	=int($IMGSIZE{'height'}*$tmp_x_per/100);
			  $IMGSIZE{'zoom'}	=int($tmp_x_per);	
			}else{
			  $IMGSIZE{'out_height'} =$limit_height;
			  $IMGSIZE{'out_width'}  =int(100*$limit_height/$IMGSIZE{'hw_racio'});
			  $IMGSIZE{'out_width'}=1 if($IMGSIZE{'out_width'} <1); #0���Z�h�~
			  $IMGSIZE{'zoom'}	=int(100*$IMGSIZE{'width'}/$IMGSIZE{'out_width'});
			}
	
		}else{
			# no change
			$IMGSIZE{'out_height'} 	=$IMGSIZE{'height'};
			$IMGSIZE{'out_width'}   =$IMGSIZE{'width'};	
			$IMGSIZE{'zoom'}	=100;	
		}
	}else{
	#width is critical
		if($tmp_width_racio < 101){
			#resize by width
			if($imsz_smooze_mode > 0){	
	   		  # IE �p�ߎ��v�Z�ɂ��掿�␳
	   		  $tmp_x_per	 	=int(100*$limit_width/$IMGSIZE{'width'});
	   		  $tmp_x_per=&img_smoozer_for_ie($tmp_x_per,$imsz_smooze_mode);
			  $IMGSIZE{'out_width'} 	=int($IMGSIZE{'width'}*$tmp_x_per/100);
			  $IMGSIZE{'out_height'} 	=int($IMGSIZE{'height'}*$tmp_x_per/100);
			  $IMGSIZE{'zoom'}	=int($tmp_x_per);
			}else{
			   $IMGSIZE{'out_width'} 	=$limit_width;
			   $IMGSIZE{'out_height'}  =int($limit_width*$IMGSIZE{'hw_racio'}/100);
			   $IMGSIZE{'out_height'}=1 if($IMGSIZE{'out_height'} <1); #0���Z�h�~
			   $IMGSIZE{'zoom'}	=int(100*$IMGSIZE{'height'}/$IMGSIZE{'out_height'});
			}
		}else{
			# no change
			$IMGSIZE{'out_height'} 	=$IMGSIZE{'height'};
			$IMGSIZE{'out_width'}   =$IMGSIZE{'width'};
			$IMGSIZE{'zoom'}	=100;
		}
	}
}

#==================#
#  �A�C�R������
#==================#

sub check_icon_files{
# �A�C�R���t�@�C���Ǝʐ^�t�@�C���𔻕ʂ���  

	# ���摜�������̏ꍇ
	if($IMGSIZE{'hw_racio'} >= 100){
			
		if($IMGSIZE{'height'} < 60){
			$p_type="icon";
		}else{
			$p_type="picture";
		}
	# ���摜���c���̏ꍇ
	}else{
		if($IMGSIZE{'width'} < 60){
			$p_type="icon";
		}else{
			$p_type="picture";
		}
	}

}

#==================#
#  ���̕ϐ��̌v�Z
#==================#

sub other_out_parameters{
	if(($IMGSIZE{'out_width'} > 0 )&&($IMGSIZE{'out_height'} > 0 )){
		$IMGSIZE{'out_hw_racio'} 	=int(100*$IMGSIZE{'out_height'}/$IMGSIZE{'out_width'});
	}
	$IMGSIZE{'out_hw_racio'}=1 unless($IMGSIZE{'out_hw_racio'} > 0 );
	# 0�̎���1�ɂ���  (0���Z�h�~)
}

#=============================#
#  �T�C�Y�ύX���[�`���P�Ɨ��p
#=============================#

sub input_prefetched_data{
	# ���ɃT�C�Y��񂪂킩���Ă���A�T�C�Y�ύX���[�`���̒P�Ɨ��p���s�������ꍇ
	# ������$imsz_file��"dummy"�Ƃ������O�����ēn���Ă�������  ���m�̃T�C�Y���
	# �͈ȉ���$IMG_PARAMETERS{'XXX'}�Ƃ����z��œn���Ă�������  
	if(($IMG_PARAMETERS{'height'} > 2)&&($IMG_PARAMETERS{'width'}>2)){
	
		$IMGSIZE{'type'}	=$IMG_PARAMETERS{'type'};
		$IMGSIZE{'height'}	=$IMG_PARAMETERS{'height'};
		$IMGSIZE{'width'}	=$IMG_PARAMETERS{'width'};
		$IMGSIZE{'hw_racio'}	=$IMG_PARAMETERS{'hw_racio'};
		$IMGSIZE{'zoom'}	=$IMG_PARAMETERS{'zoom'};
	}
}

#=============================#
#  ���T�C�Y�摜�X���[�U�[
#=============================#
# 2000/05/01 NEW
# IE�ŃT�C�Y�ύX������ƁA���̃T�C�Y�l�ɂ���ĉ掿���傫���򉻂���ꍇ��
# ����܂��B�����h�����߂̃��[�`���ł��B�򉻂��₷���悤�ȃT�C�Y�p�����[
# �^���w�肳�ꂽ�ꍇ�A�򉻂��ɂ����l�ōł��߂��l�Ɏ����␳���܂��B
#
sub img_smoozer_for_ie{

	local($org_per,$change_pattern)=@_;

	$IMGSIZE{'sm_org_per'}		=$org_per;
	$IMGSIZE{'sm_change_pattern'}	=$change_pattern;

# very good	25,34,50,96-100
# good		11,14,20,21,33,70,72,77,92

	# �ʏ탂�[�h
	if($change_pattern==1){
		if($org_per <= 10){
			$org_per =$org_per;
		}elsif($org_per <=12 ){
			$org_per =11;
		}elsif($org_per <=17 ){
			$org_per =14;
		}elsif($org_per <=20 ){
			$org_per =20;
		}elsif($org_per <=23 ){
			$org_per =21;
		}elsif($org_per <=28 ){
			$org_per =25;		# very good
		}elsif($org_per <=31 ){
			$org_per =30;
		}elsif($org_per <=33 ){
			$org_per =33;
		}elsif($org_per <=43 ){
			$org_per =34;		# very good
		}elsif($org_per <=63 ){
			$org_per =50;		# very good
		}elsif($org_per <=68 ){
			$org_per =70;
		}elsif($org_per <=75 ){
			$org_per =72;
		}elsif(($org_per <=88 )&&($IMGSIZE{'max_length'} > 650)){
			$org_per =77;
		}elsif($org_per <=95 ){
			$org_per =92;
		}elsif($org_per <=97 ){
			$org_per =96;		# very good
		}elsif($org_per <=100 ){
			$org_per =100;		# very good
		}elsif($org_per <=112 ){
			$org_per =100;
		}
	# �掿�D�惂�[�h
	}elsif($change_pattern==2){
		if($org_per <= 10){
			$org_per =$org_per;
		}elsif($org_per <=12 ){
			$org_per =11;
		}elsif($org_per <=17 ){
			$org_per =14;
		}elsif($org_per <=20 ){
			$org_per =20;
		}elsif($org_per <=23 ){
			$org_per =21;
		}elsif($org_per <=28 ){
			$org_per =25;		# very good
		}elsif($org_per <=31 ){
			$org_per =30;
		}elsif($org_per <=33 ){
			$org_per =33;
		}elsif($org_per <=39 ){
			$org_per =34;		# very good
		}elsif($org_per <=63 ){
			$org_per =50;		# very good
		}elsif(($org_per <=68 )&&($IMGSIZE{'max_length'} > 650)){
			$org_per =50;
		}elsif(($org_per <=75 )&&($IMGSIZE{'max_length'} > 650)){
			$org_per =72;
		}elsif(($org_per <=86 )&&($IMGSIZE{'max_length'} > 650)){
			$org_per =77;
		}elsif($org_per <=100 ){
			$org_per =100;
		}elsif($org_per <=124 ){
			$org_per =100;		# very good
		}
	}
	$IMGSIZE{'sm_out_per'}	=$org_per;
	return($org_per) ;	
}

#==============================#
# ���ʂ̃`�F�b�N(0���Z��h��)
#==============================#
#
sub check_out_results{

	local($p_error);
	$p_error=1;		#1=ok,0=cannot_use_size_parameter

	unless($IMGSIZE{'out_width'} > 0 ){
		$p_error=0;
		$IMGSIZE{'out_width'}=1;
	}
	unless($IMGSIZE{'out_height'} > 0 ){
		$p_error=0;
		$IMGSIZE{'out_height'}=1;
	}
	unless($IMGSIZE{'zoom'} > 0 ){
		$p_error=0;
		$IMGSIZE{'zoom'}=1;
	}
	return	$p_error;
}

1;
