#!/usr/bin/perl
#
#
#          imgboard.cgi (Rev.6.1v4c yTube)
#
#		Copyright(C)	imgboard.com
#		 Origin Program	to-ru@big.or.jp
#		 Updated by 	talk@big.or.jp
#
#		 Support site URL http://imgboard.com
#
#
# <Modification History>-03/28/2015/01
# 2015/03/28 Fixed the problem that videos are no longer embedded due to the change in Youtube's shortened URL specification.
# 2014/07/14 Strengthening measures against SPAM related to counterfeit brand products and counterfeit products originating in China
# 2014/02/16 Theta, Niconico's RICOH adjusted comments to the right
# 2014/02/14 RICOH's all-around camera Theta supports image embedding
# 2014/02/14 Explanation correction that guides how to embed Youtube (guide the URL of "Shared" instead of the embed code youtu.be ）
# 2014/02/11 Support for Youtube's "Play from the middle" designation
# 2014/02/11 Update fix for iOS7 (wording correction)
# 2013/03/05 Added a new setting that posters have a password and replies do not require a password
# 2013/02/11 Bug fix for TEXT link fixation and icon size fixed mode by administrator setting
# 2013/01/14 Fixed the function to automatically recognize addresses and link them to Google Maps
# 2012/10/28 SPAM detection logic enhancement Ver. 2.7 (detection is OK even if the case is different from the NG word)
# 2012/10/24 ALIGN and HSPACE designations for IMG and IFRAME tags are now listed with CSS, and safari and
# The layout of comments is now less likely to collapse even in Chrome
# 2012/10/21 Modified the layout so that the comment part wraps around to the right on Youtube 
# 2012/10/06 (2012.10.1) Video & audio file posting will be turned off as standard due to DL illegalization
# 2012/10/06 Added ON/OFF display of post description
# 2012/10/06 Cleaned up and deleted web slice compatible parts
# 2012/09/06 iOS6 Optimized (supports uploading from safari on iPhone)
# 2012/08/08 Fixed link destination of image reduction software for Mac and Android
# 2012/08/08 Comic Book Archive (.cbr .cbz)
# 2012/05/09 How to post from iPhone/iPad is now automatically displayed
# 2012/05/07 User ICON limit increased from 10 to 150
# 2012/05/01 Updated SPAM filter settings
# 2012/04/29 Due to the unpopularity of some buttons that have become larger for smartphone support, we have changed the same as before on PC.
# 2012/04/29 Fixed compatibility issue with GoogleMap
# 2012/04/18 (CGI Installation Caution!!) Changed script newline code from CR+LF to LF
# 2012/04/18 (CGI Installation Caution!!) Change perl path from /usr/local/bin/perl to /usr/bin/perl
# 2012/04/18 Enhanced XSS (Cross-Scripting) Countermeasures
# 2012/04/18 Automatic address link correction
# 2011/12/20 Fixed a bug that adult videos such as xvideos.com could be embedded even if the video site was limited to yotube, etc.
# 2011/12/15 Added option to accept 2MB class posts directly from Android smartphone
# 2011/12/15 Fixed with XSS (Cross-Scripting) countermeasures
# 2011/12/15 Added option to accept 2MB class posts directly from Android smartphone
# 2011/11/20 New embed URL "youtu.be" support for YouTube
# 2011/11/20 Nico Nico Douga's "Video Information" iframe embed URL support
# 2011/06/10 Youtube,dailyMotion,ustream,nicovideo migrated to iframes.
# 2011/06/10 fmt specification function abolished due to YouTube API change
# 2011/06/08 Changed parameters for new twitter API
# 2011/02/05 Support for Niconico Douga external player (embedded playback)
# 2011/02/04 Added judgment process to say that Flash is not supported in Android 2.1
# 2010/08/18 Support for loading external files and spam word lists (spamword .cgi)
# 2010/07/08 Imgboard's built-in FLV player is now compatible (mp4, mov, flv can be embedded playback)
# 2010/07/08 HTML5 video support on iPad/iPhone
# 2010/07/08 Enhanced SPAM Countermeasures 2.5 (URL hexadecimal notation is supported)
# 2010/04/24 Improved 1920x1080 LCD to make images and Flash movies look larger.
# Specifically, when viewport is specified, a function to automatically increase and decrease the image size by horizontal fixing, automatic (automatic), etc. has been added.
# 2010/04/24 Added direct page specification link
# 2010/04/24 Fixed a bug that caused token timeout error
# 2010/04/24 Added a feature to introduce image threads on Twitter
# 2010/03/31 Fixed an error with anti-SPAM one-time tokens when HTML cache output for high-load sites is turned on
# 2010/03/30 Revived the old layout where comments wrap around articles
# 2010/03/28 Increased button size for iPhone/iPad touch panel operation
# 2010/03/28 For SPAM prevention, few people put in email, so it was omitted by default.
# 2010/02/22 Added SPAM countermeasures using escape function
# 2010/02/17 Test implementation of trip function (anti-spoofing)
# 2010/02/15 Added wine time token function to SPAM countermeasures
# 2010/02/15 Added IP Addressing SPAM Filter Function
# 2010/02/05 Significantly updated SPAM ad list and strengthened measures against SPAM posting
# 2010/01/23 Added CGI code for Android
# 2009/12/18 Epub format for e-books
# 2009/12/18 Added a function to recognize addresses in articles and link them to GoogleMap
# 2009/12/18 Strengthening measures against SPAM from Chinese-speaking countries
# 2009/12/18 Added the act of downloading to the notice on copyright (revision of the law)
#  2009/12/09 Windows版safariの文字化け対策を追加
#  2009/12/03 iPod/iPhoneのメール投稿に対応
#  2009/10/22 AES暗号化アーカイブソフト、アタッシュケース(ATCファイル）に対応
#  2009/10/22 m4v対応を追加
#  2009/06/15 XPS形式ファイル(MS版PDF)対応
#  2008/08/18 GoogleMAPストリートビュー(日本)埋め込みに対応
#  2008/07/16 youTubeをiPod/iPhoneで見た場合に、記事が出ないバグを修正
#  2008/06/26 iPod/iPhoneで見やすくするためＨＴＭＬ小変更
#  2008/06/25 PSPでyouTube動画を直接見えるように改良
#  2008/06/24 iPod/iPhoneでyouTube動画を直接見えるように改良
#  2008/06/20 iPod/iPhoneの文字化け現象に対処
#  2008/06/03 906i/706i以降の2MB画像アップ機用に携帯モジュール説明変更
#  2007/06/05 SPAMと誤解された投稿時、戻るボタンで記入内容を復元可能に
#  2007/06/05 自称されたメールアドレスの国チェック機能を追加
#  2007/05/23 英語のみの投稿を除外するようにした(SPAM対策)
#  2007/05/20 URLリンク列挙型SPAM対策を標準でONにした(従来はOFF)
# 2007/05/20 URL links can no longer be embedded in titles and email fields (SPAM countermeasures)
# 2007/05/18 PC playback link of 3gpp file was pocketPC software. correction
# 2006/12/13 FLV (Flash Video) video data support
# 2006/12/13 Increased upload limit (30MB)
# 2006/10/23 Deleted 10 SPAM words such as "Video" and "New" from the default.
# 2006/10/20 SoftBank Mobile Support
# 2006/06/29 Added a function to limit the number of URL links to 3 in bulletin board SPAM countermeasures
# 2006/05/01 Added SPAM_WORD specification field to prevent false recognition of canonical posts and SPAM.
# 2005/01/15 When the image upload limit is exceeded, the reduction software is indicated.
# 2005/01/09 m4a file (MPEG-4 AAC Audio) support
# 2004/12/12 Added sage function
# 2004/08/28 Support for send imitation other than blatj
# 2003/07/21 Fixed compatibility between Apache and blatj for Windows
# 2003/03/15 Support for blatj so that post notification emails can be sent even in Win environment
# 2001/09/20 The following functions have been fixed in consistency with mobile phone modules.
# 2001/08/13 When using a membership pass, posting is allowed with either a membership pass or a managed pass.
# 2001/02/24 Special ReportOther than deleting guest password by unique IP authentication (strongly recommended), other
# Enabled you to select the "delete key method" commonly used on bulletin boards
# 2001/02/18 Supports various mobile data such as ringtones
# 2001/02/18 Accepted GIF, JPEG, PNG as default image files
# 2000/01/08 Measures against "vandalism" such as filters by prohibited words and continuous posting limiters
# Major enhancements (Rev.4)
# 1999/11/18 www5x.biglobe.ne.jp (Rev.3)
# 1998/09/20 Resize function added. Administrator email function added.
# 1998/07/10 CGI-only directory type provider support 
# 1998/01/24 v0.9 completed by to-ru@big.or.jp
#
# <Acceptable Use Policy>
# 1. (Copyright)
# 1.1 The copyright and license rights of this CGI are owned by the imgboard.com (hereinafter referred to as "us").
# .
# 2. (License)
# ・This CGI is only available to individuals and corporations if they comply with all of these Terms of Use.
# Nevertheless, you can customize it freely and use it free of charge.
# ・ If there is even one item that cannot be satisfied, the use of it is basically permitted.
# No, Please check carefully.
# ・ Even if all the items are satisfied, if we deem the use inappropriate, the
# Please note that we may discontinue use.
#
# 2.1 License Agreement
# A. The title part of this explanation (line 1-9X of the script: especially the acceptable use section (script
# lines 5X - 9X)) and modified the copyright notice at the bottom of the bulletin board
# Not
# B. Deleting or modifying advertising parts such as "purchase price .com" at the bottom of the bulletin board,
# Do not process it to a state that is difficult to see.
# C. Do not modify or redistribute customized scripts without permission.
# In particular, if conditions A, B, and C are not satisfied, their use is strictly prohibited.
#
# 3. (Restrictions)
# 3.1 Redistribution, modified or non-modified, without our permission, is strictly prohibited.
# 3.2 Prohibit the use of bulletin boards targeting users of nationalities other than Japan.
# 3.3 Alter and delete this copyright notice and the copyright notice and link at the bottom of the bulletin board
# Doing so is strictly prohibited.
#
# 4. (Non-restrictions)
# 4.1 You are free to modify (but please note 3.3)
# 4.2 Commercial use is free (but please note 3.3)
# 4.3 Allow Personal Use and Corporate Use. (However, please note 3.3)
#
# 5. (Disclaimer)
# 5.1 Responsibility for the management of the bulletin board shall be 100% with the person who installed the bulletin board. This site is
# We are not responsible for its management.
# 5.2 Even if you suffer damage or disadvantage due to this CGI, we will be fully responsible for it.
# We have no obligations.
# 5.3 If there is a bug, missing function, bug, etc. in this CGI, we are obliged to fix it.
# Not to be liable.
#
# 6. (Other)
# If we deem its use inappropriate, we will stop using it.
# Please note.
# These Terms of Use are subject to change or addition without notice. Please note.
#
###############################################################################
# Basic configuration (initial settings are explained on the premise of this configuration)
#
# public_html (Homepage Directory)
# |
# |-- cgi-bin (arbitrary directory 705)
#   |
# |--img-box(757 or 707)(image storage directory)
#   |
# |-- jcode_sj.pl (755 or 705) (lite Japanese library)
# |-- imgboard.cgi (755 or 705)(console)
# |-- imgsize.pl (755 or 705) (Image Size Analysis Library)
# |-- file.dat (666 or 606) (for storing article data)
# |-- fileback.dat (666 or 606) (backup of the above file)
# |-- icon.dat (666 or 606) (for storing WebParts data)
#
# ・ ( ) is an attribute (permission). First, try with the left number in parentheses,
# Check if it works. Once confirmed, change the middle of the three numbers to 0,
# Check if it works. If either can work normally, as much as possible
# Use the value on the right.
# (In general, in providers, setting the middle number to 0 is more secure
# Stricter and less likely to be rewritten by others and increased safety
# . However, some providers stop CGI from working, so in this case
# Please use the value on the left)
#
# ・file.dat,fileback.dat,icon.datは中身が空の同名ファイルをパソコン上で作成．
#   ftpで転送する(同封のファイルをそのまま使っても良い)
#
# ・FFFTPの場合、自動文字コード変換の副作用でスクリプトが動かなくなるので、
#   cgi本体をSHIFT-JIS,改行コードLF「B」バイナリー転送すること。
#
# ・jcode_sj.plは中身を全くいじらずにそのままアスキー転送すること。
# ・これら４つのファイルはアスキーモード（テキスト）で転送すること。
# ・＠nifty,wakwak,biglobe等は、上記基本構成とは異なるファイル配置や設定が必要に
#   なります。新FAQ掲示板に情報があるので、それを参考にして下さい
#
###############################################################################

#=======================================================================#
#  初期設定
#=======================================================================#
#
#  先頭に#のある行は読み込まれません．
#
#==================================#
#        <必須設定項目>            #
#==================================#
#
$admin_passwd = 'gochi';		# 管理人による記事削除時のパスワード
#					# (必ず変更してください)
#
$title 	= "画像掲示板(Light)";	
#  ↑「お気に入り or ブックマーク」保存時のタイトルになります。
#
#  ■<終了時戻り先ＵＲＬ>
#
#  掲示板の「終了ボタン」を押したときに、下記ＵＲＬへ戻ります。
#  (URLを下記デフォルトURLから変更しますと、ページにボタンが自動的に出現)
$back_url ='http://あなたのプロバイダ/あなたのディレクトリ/index.html';
#
#
#  ■<投稿画像の格納ディレクトリ>
#
#  投稿された画像ファイルを保存しておく場所です．整理を簡単にするため、また
#  セキュリティ確保のために、imgboard.cgiと同じディレクトリではなく,直下に
#  新規ディレクトリを作成し,そこにアップロードファイルを保存することを強く
#  おすすめします．
#  なお,場所の指定方法ですが,通常は相対パス*で指定して下さい．
#  ---解説----
#  相対パスとは、imgboard.cgi(以下cgiと呼ぶ)から見た相対的な位置を指定する方法
#  です。以下の設定はcgiのあるディレクトリ直下にimg-boxという名前の新規ディレ
#  クトリを作成し、そこを保存ディレクトリとした場合の相対パス指定例です（ピリ
#  オドはcgiが置いてあるディレクトリを意味します。)。
#  相対やら、絶対やら、なんか難しくてよくわからない・・という方は、このまま指
#  定を変更しないで、指示通りの位置にimg-boxディレクトリを作ってください。
$img_dir = './img-box';		# デフォルト位置
#
#  (補足事項/一部該当者のみ読んでください)
#  あなたのプロバイダが、cgiとデータファイルを同じ場所に置くことが出来ない
#  特殊なプロバイダ(hi-ho等）で、cgiと同じディレクトリやcgi直下に保存
#  用ディレクトリを作れない場合、絶対パスによる指定が必要となる場合があります。
#  この場合、５行ほど前にある$img_dirを絶対パス*指定に書換えて下さい。
#  ---解説----
#  絶対パスとは、そのコンピュータ上のファイルシステムの一番上の階層から
#  そのファイルの置いてある位置までのすべての階層をちゃんと指定したもの
#  になります。
#  絶対パス例・・・・$img_dir = '/home/usr5/talk/photo_bbs/img-box';
#  （注：通常はできるだけ相対パス指定をして下さい）
#  絶対パスがわからない場合、プロバイダのユーザサポートページのＣＧＩ関連情
#  報のコーナ等に情報がたいていありますので、これを探してください。またtelnet
#  してシェルが使えるプロバイダの場合はpwdというunixコマンドを該当ディレクト
#  リに移動後、入力すると現在いるディレクトリまでの絶対パスが表示されます。
#  なお、絶対パス指定をした場合、同imgファイル保存ディレクトリのURL指定も併
#  せて行って下さい．
#  （注：img_url指定は一部の該当者のみ設定する項目です。通常は設定不要なので
#    当補足事項は無視して下さい。なお、＠nifty,wakwak,biglobe等は、ここで説明
#    したものとは異なるさらにまた別の設定が必要になります。新FAQ掲示板に情報が
#    あるので、それを参考にして設定して下さい）
$img_url ='http://あなたのプロバイダ/あなたのディレクトリ/img-box';
#
#
#  <携帯対応>
#  ガラパゴス携帯(iモード,FOMA,SoftBank,au)からアクセスがあると、
#  下記ファイル名のCGIを探します。同じディレクトリに存在した場合は、
#  下記CGIへユーザを転送するようにナビゲートするページを自動で出し
#  ます。
#  ガラパゴス携帯ユーザを携帯アクセスCGIへ自動転送する(1=yes,0=no)
$imode_redirect=1;
#
# 探すCGI名
$imode_cgi_name= './im.cgi';
#
# 案内する携帯アクセスCGIのURL
$PM{'im_cgi_url'}='http://www.aaa.bbb.com/~myname/im.cgi';
#
#  <掲示データ保存ファイル名>
#
#  テキストデータの保存用ファイルの名前です．
#  imgboard.cgiと同じ場所に入れる場合はこのパス指定のまま.
$file= './file.dat';
#
#  <WebPartsデータ保存ファイル名> (R6 NEW)
#
#  管理者モードで使うWebPartsデータを保存するためのファイルの名前です．
#  imgboard.cgiと同じ場所に入れる場合はこのパス指定のまま.
$PM{'icon_data_file'}	= './icon.dat';
#
#  <日本語コード変換ライブラリ>
#
#  imgboard.cgiと同じ場所に入れる場合は、このパス指定のまま.
#  注:jcode_sj.plはjcode.plの機能限定スリム版です。SJISへの変換機能のみ。
$jcode_name= 'jcode_sj.pl';
#
#  <画像プロパティ認識ライブラリ>
#
#  imgboard.cgiと同じ場所に入れる場合はこのパス指定のまま.
$imgsize_prog="imgsize.pl";
#
#
#  <掲示板SPAM対策> 2006.03 new /2014.07 update
#
#  掲示板SPAMによる自動書き込み
#  (0=制限しない,1=制限する（デフォルト）)
$limit_bbs_spam_flag=1;	
#
#  上で"1"にした場合、隠しキーワードを決めてください。
#  掲示板SPAMは英語圏が多いので、彼らの苦手な間違いやすい、
#  日本語ひらがなを含めるのが良いでしょう。
#  日本語の場合１２文字までにしてください。
#
#  また、中国からの日本語SPAMに困っている場合は、
#  "天安門事件"などの政治ワードを以下文字列に含めると
#  経験的に当局側FWの自動遮断で防げる場合があります。
#  特定のカタカナや半角文字は文字化けを生みCGIエラーに
#  なるので基本NGです。
#  変更は１文字毎に試して、問題のなく投稿できる文字列を
#  探してください。
#
$spam_keyword="天安門事件ろゆシ";	
#
#  禁止単語によるSPAM制限 (SPAM_WORD) 2006.04 New
#
#  URLリンクやメールアドレスがあり、かつ、特定の単語を本文に含む記事のみ
#  投稿を失敗させます。NGワード指定では、広告でない記事がSPAMとして
#  誤認識されて会話に不都合が出る場合、こちらを使ってみてください。
#
#  (1=制限する(推奨),0=制限しない)
$PM{'no_upload_by_spam_word'}=1;
#
# 注：先頭に#のある行は無効です。
#
@SPAM_WORD=(" 飢えた女性 ", " 女の子検索 ", " 超高収入 ", " ヤリ放題 "
," 割り切 ", " パラダイス ", " 副収入 ", "  ", " お小遣い "
," 完全無料 "," 推薦枠 "," 逆援 "," 女性会員 "," 好みの女性 "," 極秘情報 "
," 妊娠契約 "," 素人女性 "," 女性登録者 "," 登録無料 "
," 逆指名 "," サイトだよ "," 見放題 "
# アダルト系
#," セックス "," 無修正 "," 調教 "," セフレ ", " 人気ＡＶ "
#," 女性が "," エッチ "," ゲット "," ご指名 "," 援交 ", " ヤリマン "
#," 若い女性 "," 童貞 "," 出会い "," 人妻 "
#," 旦那 "," サイトだよ "," 援助 "," 若妻 "
#
# 海外
# アダルト系
#," fuck "," porn "
#," fetish "," pics "," adult "," teen "," stripper "
#
# ブランドコピーSPAM
," クス専売 "," ハイレプ "," copy33 "," brand188 "," スーパーコピー "
," louis "," vuitton "," taschen "," fossil  "," ローレックス "," ロレックス "
," cartier "," カルティエ "," 高級腕時計 "," S級  "," N級 "
#," check "," thank "," More "," free "
#," online "," site "," visit "
# 勧誘系
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
# 熊本デリヘル系 by http://whois.domaintools.com/b-blooming.com
," bigbaito.com "," deli-rakuten.com "
," firstlips.com "," forfun.jp "," hey-sey.com "," nn7.biz "
# 精力剤系
," internut "," seiryokuzai "," khonsys "
," diet-live "," vigrx "," hirugouhan "," kanpo.com "
," 精力剤 "," 精力減退 "," 不感症 "," 媚薬 "," 激安サンプル "," 中国漢方 "
," 便宝 "," 催淫 "," バイアグラ "," シアリス "," ダイエットサプリ "
," 勃起不全 "," リドスプレー "
# Foreign spam word
," serwis "," miejsca "," serwery "," Internecie "
# 中国語含む広告をはじく
," 湜 "," 浯 "," 胛 "," 萵 "," 趺 "," 瑙  "," 濵  "," 小妹  "," 跪  "," 頌  "
," 模擬器 "," 軟件 "," 鰀 "," 肛裨 "," 褊 "," 舮 "," 竟 "," 碌  "," 轢  "
," 颪 "," 恷詰 "," 爾芦 "," 原奉 "," 滯 "," 圦 "," 錚 "
," 哈 "," 斌 "," 椶 "," 發 "," 秘塞 "," 蠅泙 "," 欄瓶 "
," 瑪 "," 鈔 "," 韲 "," 瑩 "," 糒 "," 黑 "," 淲 "
," 鴾 "," 汳 "," 沃 "," 鱚"," 穉 "," 諷"," 糂 "," 冢 "," 厠 "," 誾 "
# SPAMが多い国へのリンクを含む投稿をSPAMとする
# ロシア(ru) 中国(cn)  韓国(kr) 香港(hk) 台湾(tw)
# アルゼンチン(ar)、ブラジル(br)、イギリス(uk)
," .ru/ "," .cn/ "," .kr/ "," .fi/ "," .hk/ "," .tw/ "
," .ar/ "," .br/ "," .uk/ "
," 偽善者 "," 捏造 "," 無料配布中 "
," 素人娘 "," 大放出 ");
#
# IPアドレス指定型 SPAMフィルタ機能の追加について(2010.02 )
#
# ドメイン名を５０以上(中には１００以上）持つ業者も多いですが、
# リンク先の実IPアドレスは1、あるいは数個以下の固定IPである
# ケースがほとんどです。
# 従って、ドメイン名をリストに追加して一つ一つ排除する方法より、
# リンク先の固定IPを調べ、禁止リストに追加して、SPAMを排除した方が、
# 50～100倍効率が良いです。
# ドメイン名からIPアドレスを調べるには、ネットに接続した状態で、
#  MS-DOSコマンドラインで「ping ホスト名」を入力すれば、結果として表示されます。
# そのIPアドレスを@SPAM_HOSTS_IPに追記してください。
#
@SPAM_HOSTS_IP=("74.207.24?.","174.122.10?.","66.71.24?.","66.71.25?.","221.231.138.","18.243.22.64"
,"210.173.241.","209.160.32.22?","58.1.229.8?","202.172.28.15?"
,"69.64.147.","203.135.19?.?","198.143.162.");
#
# 2006.06 URLリンク列挙型SPAM対策
#
#  SPAMワードがひっかからなくても、本文中にURLリンクが4つ以上ある場合は
#  書き込めないようにします。
#  (1=制限する(推奨),0=制限しない)
$PM{'spam_url_link_limit_4'}=1;
#
# 2007.05 外国からのSPAM
#
#  英語のみの投稿は書き込めないようにします。
#  外国からのSPAM防止に有効です。
#  (1=制限する(推奨),0=制限しない)
$PM{'spam_limit_non_japanese'}=1;
#
#  日本語コメントを含まない動画埋め込み投稿は書き込めないようにします。
#  外国からの広告動画SPAM防止に有効ですが、投稿者からはめんどくさがられ投稿が減ります。
#  どうしても困った場合のみ、1にしてみてください。
#  (1=制限する,0=制限しない(推奨))
$PM{'spam_limit_non_japanese_movie'}=0;
#
# 2013.02 外国からのSPAM
#
#  SPAMが多い昨今、メールアドレスをインターネットで晒す人もいないので
# 現在デフォルトではメール欄がコメントアウトされていますが、スパム側は
# 自動でメールアドレス欄を読み取って、メールを記載して投稿してきます。
#  そこで、メールアドレス付きの投稿が来たらスパムとして判別することができます。
#  メール欄記入した投稿をSPAMとしてみなす。
#  (1=SPAMとする(推奨),0=しない(コメントアウト外してメール欄を生かす場合はこっちを選んでください))
$PM{'no_post_by_form_email_post'}=1;
#
# 2007.06 SPAMらしきメールアドレス
#
#  メール欄のメールアドレスがSPAMに多い国のドメインの場合
#  投稿を書き込めないようにします。
#  外国からのSPAM防止に有効です。
#  (1=制限する(推奨),0=制限しない)

$PM{'no_upload_by_spam_country_mail'}=1;
#
# SPAMが多い国へのメールアドレスを自称する投稿をSPAMと判定する
# ロシア(ru) 中国(cn)  韓国(kr) 香港(hk) 台湾(tw)
# アルゼンチン(ar)、ブラジル(br)、イギリス(uk)
@SPAM_MAIL_COUNTRY=(".ru",".cn",".kr",".fi"
,".hk",".tw",".ar",".br");
#
#  以上の様々な対策を指定しても効果がない場合、
#  まずは、投稿パスワード制にすることを考えてください。
#  SPAMはロボットで何万もの掲示板に自動投稿してきますので、
#  パスワードを類推されにくい位置に記述しておけば、解読される
#  可能性は低いです。
#
#  さらに、以上の様々な対策を指定しても効果がない場合、
#  あらゆるSPAMをとにかく問答無用で排除したい場合は
#  以下のフラグを使ってください。（通常は指定しないこと）
#
#  URLリンクやメールアドレスのある書き込みを、問答無用ですべて廃棄
#  (0=廃棄しない（デフォルト）,1=廃棄する)
$filter_bbs_spam=0;
#
#=====================================================================#
#  <以下,必要に応じて設定>                                             #
#
#  以下の設定は,すべてオプションです。
#
#  大抵のプロバイダの場合、特に変更しなくてもスクリプトは動きますので,
#  一度この状態でスクリプトを動かしてみてください。
#  1.正常に動かなかった場合,
#  →新サポート掲示板や新FAQをみて,問題を解決してみてください。
#
#  2.正常に動いた場合
#  →いろいろ細かくアレンジできるようになっていますので, 以下のオプション
#  項目へ進み、自分流にオプションを設定し,アレンジしてみてください。
#=======================================================================#
#================================#
#   <掲示板機能 基本オプション>  #
#================================#
#
#  ■<転送許可画像サイズ上限>
#
#  ファイル投稿時、このＣＧＩは他のテキスト系ＣＧＩよりも多くのメモリリソース
#  を必要とします。これはアップロードしたファイルの復元処理にバッファが必要な
#  ためであり、必要なメモリ量は転送された画像サイズに比例します。非力なサーバ
#  を使用している場合は、自然とアップロードサイズを小さくする必要があり、そう
#  しないと処理はタイムアウトして止まりますのでご注意下さい。
#
#  サイズ制限(画像以外)
#  デフォルト9000ＫＢ(99000KB以上にはしないこと。)
$max_upload_size 	= 9000;	# 単位KB
#
#  サイズ制限(画像)
#  デフォルト200ＫＢ(埋めこみ表示が遅くなるので500KB以上にはしないこと。なお
#  ユーザが下記で指定したサイズ以上の画像をアップロードしようとすると、投稿
#  できないというメッセージが表示されると同時に、PCやMac、Androidスマフォで
#  使える無料の画像縮小ソフトの案内が自動で出るようになっています。)
$max_upload_img_size 	= 500;	# 単位KB
#
# 2011.12 新機能
#  Androidスマフからの画像投稿は、特別にサイズ制限を大きくする
#
#  Androidスマフォのカメラ写真は平均1～3MBと大きいため
#  相手の機種がAndroidの場合だけ、サイズ制限をゆるくします。
$max_upload_Android_img_size 	= 5000;	# 単位KB
#
#
#  ■<推奨画像サイズ表記の値を決める>(R6 NEW)
#
#  R6では、本当のリミッタとは別に「推奨サイズ」を掲示板下部の注意文に表示
#  することができるようになりました。管理人が最も歓迎する画像のサイズを書いて
#  と良いでしょう。なお、この値はただ表示されるだけです。
#  (1=注意文のところに推奨サイズを出す（推奨）,0=出さない)
$disp_rcmd_upload_size_flag 	= 1;
#
#  デフォルト80KB
#  (通常ホームページ上でのJPEG画像のサイズは25－50KB程度です。また携帯等では
#  100KB以上のデータが表示できない機種が多いので、100KB以下に設定すると良いで
#  しょう)
$rcmd_upload_size 	= 80;	# 単位KB
#
#  ■<保存記事数>
#
#  この件数を超えると、古いものから記事は削除されます.(記事と画像は
#  同時に消えます)。
#  デフォルトは150．極端に増やすとHP容量を圧迫しますので、ご注意ください。
#
#  --注意点--
#  画像データ削除時は、掲示板を用いて削除して下さい。
#
#  (ワンポイント)返信には画像を添付できませんが記事としては、１記事として
#  カウントされます。したがって返信機能をオンにされる場合は、保存記事数を、
#  従来の2-3倍にしておくと良いでしょう。
$max_message 		= 350;	
#
#  ■<1ページに表示する 親メッセージ数>
#
#  デフォルト10
#  １ページに表示する親メッセージの数です。IEの場合、数を多くすると、
#   表示時に少し時間がかかりますので、10程度を推奨します
#
#   なお、画像でなく、埋め込み動画の投稿比率が多い場合
#   Flashプレイヤーがメモリを使い尽くしてブラウザが
#   クラッシュする可能性がありますので、15以下にしてください。
$disp_message 		= 10;
#
#  ■<返信機能>(R6 NEW)
#
#  返信機能を使うことができます。
#  (1=返信機能あり(推奨),0=返信機能なし)
$PM{'use_rep'} 		= 1;
#
$PM{'allow_res_upload'} = 0;
#
#  古い記事に最近ついた返信を見過ごさないように、返信がついた記事の
#  スレッドを自動的に先頭へ持って行くことができるようになりました。
#  (1=先頭へ持って行く(デフォルト),0=持っていかない)
$PM{'res_go_up'} = 1;
#
#  古い記事に返信しても先頭へ持っていかないように
#  ユーザが投稿時に選ぶようにもできます。
#  （いわゆる「sage」機能です）
#  (1=sage有効(デフォルト),0=sage無効)
$PM{'use_sage'} = 1;
#
#==================================#
#     <imgboard 特殊オプション>    #
#==================================#
#
#  ■ <画像表示モードのユーザ選択>
#
#  imgboardでは、画像の表示モードをユーザ側が自由に選択できるようになってい
#  ます。つまり、絵を直接貼り付ける、貼り付けない（リンクのみ）、アイコンサイ
#  ズにする、固定サイズにする等の「表示モード」の選択を、アクセスするユーザ自
#  身が自由選択できます。(ADSL/光/3G/LTE等の通信速度、環境等の条件により、最
#  適表示モードはユーザ毎に異なりますので）。
#  なお、一度選択した表示モード設定は、クッキーに記憶され、次回アク
#  セスから、それが相手のデフォルトとして選択されるようになります。
#
#  この機能を無効化して、掲示板管理者の方で表示モードを固定したい場合は、0を
#  指定してください。
#  (1=ユーザ選択メニューを出す（強く推奨）,0=ユーザ選択メニューを出さない)
$user_selected_view_mode=1;
#
#  ■ <画像表示モードの管理者設定>
# 
#  ユーザ選択に任さないで、表示モードを管理者側で固定する場合、
#  その画像表示モードを以下の部分で決めてください。
#
#  画像を直接掲示板に貼り付ける、貼り付けない。
#  (1=yes,0=no)デフォルトは1
$show_img_on_board=1;
#	
#  上で1を選択した場合，その埋め込みサイズを選択。  
#  (0=iconサイズ,1=auto,2=横固定,3=原寸サイズ,5=極端に大きな画像のみ縮小)
$on_board_img_size=2;	# デフォルトは2
#
#  --注意点--
#  埋め込みする場合は，ページのロードが遅くなりますので、１ページ当たりの発言
#  表示個数を少なめ(5程度)にした方がいいでしょう．画像の大きさも小さ目(100KB)に
#  制限した方が運営が経験上うまくいくようです。
#
#  ■ <IE用リサイズ時のサイズ微補正> R5 NEW
#
# 2=画質最優先し、imgsizeが、かなり補正することを許可する。
# 1=画質優先し、imgsizeが、少しだけ補正することを許可する(推奨)
# 0=指定サイズの正確さを重視して、一切補正はしない
$CIMGSIZE{'smooze_mode'}=0;
#
#  ■ <マルチデータアップロード可能にする>
#  当掲示板は、GIF,JPEG,PNG以外に様々なタイプのデータも投稿できるようにすること
#  ができます。(動画，音声，ZIP,PDF,その他)
#  なお、セキュリティ保全のため、アップロードできるデータは我々があらかじめ
#  リストアップされたものに限られています。特定のタイプのデータを、投稿禁止
#  したい、あるいは追加したい場合は、スクリプト中のサブルーチン
#  (additional_content_types)内で変数をコメントアウトor追加してください．
#  (詳細はサポート掲示板を参照)
#
#  マルチデータアップロードを
#  (1=可能にする,0=可能にしない)デフォルトは0
$allow_other_multimedia_data=0;	
#
#   <2012.10.1以降のDL違法化対策として、動画、音楽のアップロードを禁止する>
#  2012.10.1以降、違法な動画、音声のダウンロードに罰則が適用されます。
#  (対象は、動画、音声だけで、YouTubeなどの埋め込み動画は対象外です。)
#  マルチデータアップロードを上で1を指定して許諾したけれども、
#  余計なトラブルを防止するために、動画と音声ファイルのアップロードを
#  ピンポイントで禁止したい場合、以下で設定してください。
#
#  動画と音声のアップロードを
#  (1=可能にする,0=可能にしない)デフォルトは0
$allow_video_and_audio_data=0;	
#
#  ■ <保存ファイル名の指定>
#
#    当掲示板ではセキュリティ保全のため、自動的にファイルのリネームをします。
#    ファイル名の重複を防ぐために、1.20以降では,時刻ペースの命名法をするように
#    なりました。
#
#   ○ <元のファイル名を使用する>
#    imgboardをバイナリファイルのアップロードツールとして使用し、ファイル共有
#    用途に用いる場合、imgXXXX.XXXと勝手にリネームされると面倒で困る等の要望が
#    ありました。そこで、アップロード前のパソコン上でのファイル名をそのまま使っ
#    て保存することができる機能がimgboardにはありましたが、
#    1.22 Rev.4以降、imgboardからは、この機能は削りました。同機能をご利用され
#    たい場合は、姉妹スクリプト「imgboard2015」をご利用ください。imgboard2015では
#    デフォルトでオリジナルファイル名で保存でき、かつ、そのとき考慮すべきセキ
#    ュリティ問題に関しても大幅強化されております。
#
#  ■ <フォーム入力項目のデータ有無チェック>
#
#  フォームの各入力項目の記入について、必須にするかどうかを指定できます。
#  必須にした入力項目が空の場合、記事は登録はされません。
#
#  1=必須,0=省略を許可
$CHECK{'name'}		=1;	# 名前 （デフォルト1）
$CHECK{'email'}		=0;	# email（デフォルト1）
$CHECK{'subject'}	=0;	# 題名 （デフォルト0）
$CHECK{'body'}		=0;	# 本文 （デフォルト0）
$CHECK{'img'}		=0;	# 添付画像（デフォルト0）
$CHECK{'rmkey'}		=0;	# 削除キー（デフォルト0）# ←現在未使用
#
#  必須項目が入力されなかった場合は、警告を出して、ユーザに
#  入力を促すことになりますが、そのときに出すメッセージの
#  内容を以下で変更できます。
#
$CHECK_E{'name'}	=qq|名前がありません。<BR>|;
$CHECK_E{'email'}	=qq|emailがありません。現在の設定ではemailは必須項目となっています。<BR>|;
$CHECK_E{'subject'}	=qq|題名がありません。<BR>|;
$CHECK_E{'body'}	=qq|本文がありません。<BR>|;
$CHECK_E{'rmkey'}	=qq|削除キーがありません。<BR>|;
$CHECK_E{'img'}		=qq|添付画像がありません。<BR>|;
#
#  以下は入力項目を増やす機能(imgboardでは６つまで入力項目を増やせます)を使っ
#  て、項目を増やした場合用 (増やしていないユーザは設定しても関係ありません)。
#
#
$CHECK{'optA'}		=0;	# 追加項目optA	（デフォルト0）
$CHECK{'optB'}		=0;	# 追加項目optB	（デフォルト0）
$CHECK{'optC'}		=0;	# 追加項目optC	（デフォルト0）
$CHECK{'optD'}		=0;	# 追加項目optD	（デフォルト0）
#
$CHECK_E{'optA'}	=qq|optA がありません。<BR>|;
$CHECK_E{'optB'}	=qq|optB がありません。<BR>|;
$CHECK_E{'optC'}	=qq|optC がありません。<BR>|;
$CHECK_E{'optD'}	=qq|optD がありません。<BR>|;
#
#
#  ■ <時差>
#
#  海外サイトに設置した場合、投稿時刻が現地時刻になってしまいます。
#  これを日本時刻に修正する場合には、以下の項目で時差を設定してください。
#  (設定例) 時差を15時間にする場合 $gisa=15;という風に設定してください。
#
$gisa=0;		# 時差(h)
#
#  ■ <自動URLリンク>
#
#  記事中にURLや住所等が含まれる場合、自動的にリンクにします。
#  なお、youTubeタグ埋め込み機能利用時は必ず1に設定してください。
#  (1=自動リンク(推奨),0=自動リンクしない)
$auto_url_link=1;
#
#
#  ■ <twitter紹介用リンク> 2010NEW
#
#  記事スレッドをtwitterで紹介しやすくする
#  リンクを、各スレッドにつける場合は、
#  以下のフラグをONにしてください。
#  (1=リンク表示(推奨),0=表示しない)
$PM{'use_twitter_link'} = 1;
#
# 追加のハッシュタグを定義(5文字以内)
# 末尾は必ず半角空白を１つ入れてください
#(例)$PM{'twitter_hash01'}="#dog ";
$PM{'twitter_hash01'}="";
#
# テキスト(英半角文字5文字以内)
# 
#$PM{'twitter_mes01'}="Watch it";
$PM{'twitter_mes01'}="";
#
#  ■ <新着表示>
#
#  最新投稿5記事に(new)を添えて表示します
#  (1=表示する(デフォルト),0=表示しない)
$PM{'disp_new_notice'} = 1;
#
#==================================#
#     <セキュリティ オプション>    #
#==================================#
#
#  <投稿者用パスワード>
#
#  投稿時にパスワードをチェックし、正しい場合だけ登録するようにできます．
#  掲示板の完全公開運営に不安がある場合は、この機能を用いて会員制にする
#  ことをおすすめします．パスワードは一度入力するとクッキーに記憶されま
#  すので、次回投稿から入力は不要です。なお、1を指定すると自動的に項目が
#  フォーム欄に出現します。
#  (1=使用,0=使用しない)
$use_passwd_flag=0;	
#
#  (201402NEW!)
#  返信はパスワード不要の場合は、以下で設定してください
#  (1=不要(デフォルト),0=必要)
$PM{'res_no_passwd_flag'} = 1;
#
#  会員パスワード
@MEMBER_PASSWD=("mikumiku","","","");
#
#  <タグ使用許可>
#
#  コメント中にタグを許可するかどうかを指定できます。許可すればユーザ表現の
#  自由度は上がりますが、タグの閉め忘れ等によりトラブルが発生する可能性が
#  あります。なお、タグを許可する指定にしても、掲示板に対するイタズラ予防のため
#  ActiveX,Javascript等や、危険性のあるタグ、いたずらによく使われるタグ
# （約22種類）は自動フィルタされ、無効化されますので、あらかじめご了承くださ
#  い。（詳細はsub form_checkを参照）  
#  デフォルトはタグ使用可です。(1)
#  (1=使用可能,0=使用不可)
$use_tag=1;
#
#  <IMGタグ許可・非許可>
#
#  タグを許可した場合、特に、IMGタグの埋込み可否を以下で指定して下さい。
#  (1=許可,0=非許可(強く推奨))
$use_img_tag_in_comment=0;
#
#  <youTube等、動画共有サイト関連タグ許可・非許可>
#
#  動画共有サイトの埋め込みタグの許可を例外的に
#  認める場合は、以下のフラグをONにしてください。
#  (1=許可,0=非許可(推奨))
$use_youtube_tag_in_comment=1;
#
# URLチェック
#
# 許可する動画共有サイトのドメイン名を指定してください。
# アダルト審査が甘いサイトを許可した場合、管理リスクや
# 動画スパムの脅威が高まります。荒れる場合はyoutubeだけ許可されるとよいでしょう。
@DOUGA_KU_DOMAIN=('www.youtube.com','www.dailymotion.com','www.ustream.tv','');
#
# 2=厳密(上記で許可したドメインのみ)(推奨)
# 1=に限定しない
#  なお、2以外にした場合、セキュリティ的にリスクが
#  増大しますので、覚悟の上で設定してください。
#$yt_check_level=2;
$yt_check_level=1;
#
#
# 返信記事に動画共有サイトのタグ埋め込みを許可するかどうか
# ルールを決めてください。
#  (1=許可,0=非許可(推奨))
$allow_youtube_tag_in_res=1;
#
#
# （注意）返信への埋め込み許可等はyouTubeの設定と同じポリシになります。
#
#  <ニコニコ動画関連タグ許可・非許可> NEW
#
#  ニコニコ動画の埋め込みを例外的に認める場合は、
#  以下のフラグをONにしてください。
#  (1=許可,0=非許可(推奨))
$PM{'auto_nicovideo_find'}=1;
#
#  <Google MAP ストリートビュー関連タグ許可・非許可> NEW
#
#  ストリートビューの画像埋め込みタグの許可を例外的に認める場合は、
#  以下のフラグをONにしてください。
#  (1=許可(推奨),0=非許可)
$use_stview_tag_in_comment=1;
#
#  <Google MAP 自動住所リンクのオンオフ> 
#
#  本文中にある住所らしき文字を拾って、Google Mapのリンク化する自動住所リンクは
#  デフォルトでONです。オフにしたい場合は、以下のフラグを変更してください。
#  (1=ON(推奨),0=OFF)
$PM{'auto_japanese_address_find'}=1;
#
#
#  <リコーTheta360関連タグ許可・非許可> NEW
#
#  リコーのパノラマカメラThetaの埋め込みを例外的に認める場合は、
#  以下のフラグをONにしてください。
#  (1=許可(推奨),0=非許可)
$PM{'auto_theta360_find'} = 1;
#
#  <各種掲示板荒し対策> 
#
#  (レベル１）ホスト名による制限 (BLACK_LIST)
#
#  以下のパターンを名前に含むプロバイダに属するユーザから登録できないように
#  します．悪質な掲示板荒しが頻発する場合、その対抗策としてご利用ください．
#  *はワイルドカードです。０文字以上の任意パターンにマッチします。
#  ?は一文字分の任意の文字にマッチします (詳細はサポート掲示板にて)
#
@BLACK_LIST=("rr.com","anonymizer.com","utm4*.bekkoame.or.jp","nasuinfo.or.jp",
"123.123.123.123","123.123.123.2??",
"66.71.248.21?","osaka.nt.ftth?.ppp.infoweb.ne.jp","oska.nt.adsl.ppp.infoweb.ne.jp",
".yournet.ne.jp","dy.bbexcite.jp",".u-netsurf.ne.jp","kcn.ne.jp",".u-netsurf.ne.jp",
"wave.home.net","202.231.144.1??",
"agcs.com","utsunomiya-ppp-*.interq.or.jp","198.143.162.");
#
# イタズラをするユーザの中には、ホスト名による制限を逃れるために、自分のホスト
# 名情報を出さない設定にしている人がいます。これらホスト名を出さないユーザから
# の投稿を禁止するかどうかを以下で決めて下さい。(1=禁止する,0=禁止しない(推奨))
$no_upload_by_no_RH_user=0;	
#
#  (レベル２）禁止単語による制限 (BLACK_WORD)
#
#  特定の単語を本文に含む記事の投稿を失敗させます。前述の手段を用いても"荒し"
#  や "宣伝広告の嵐" がどうしても収まらない場合、あるいは、ホスト名を頻繁に変
#  えるユーザからしつこいイタズラを受けている場合に、最終手段として使ってみて
#  ください。
#  (1=制限する,0=制限しない(推奨))
$PM{'no_upload_by_black_word'}=0;	
#
#   マッチした場合のエラーメッセージ（変更可）
#   （排除されたことが相手にわからないように、できるだけ、
#    無意味なものにしてください）
$PM{'error_message_to_black_word'}="CGI error code 2244 NBW";	
#
@BLACK_WORD=(" しねしね "," 死ね "," 制裁 "
," ユダヤ "," ごみ以下 "
," 雑魚 "," 童貞 "
," 女性登録者 "," 調教 "
," porn "," ウンコ "
," 偽善者 "," わらい "," 捏造 "," adult "," teen "," stripper "
," fetish "," pics "," peachs "
," 素人娘 "," ビデオを大放出 ");
#
#  <連続投稿回数制限>
#
#  イタズラを防ぐために、同一ユーザからの連続投稿回数を掲示板側
#  で制限できます。
#  (1=制限する（デフォルト）,0=制限しない)
$limit_upload_times_flag=1;	
#  
#  上で"1"にした場合、どれだけのサンプリング期間の間に最大何回までアップ
#  ロード許可するかを決めてください。（オーバすると投稿エラーになります）
#
# サンプリング期間 (day,1hour,10min,2min,1minを選択可。デフォルトは2min)
$upload_limit_type="2min";	
# 回数。デフォルトは5回
$upload_limit_times="5";
#
#  <超長文テキスト投稿による荒らし対策> 2004.05 new
#
#  無意味な超長文のテキストを投稿し、いたずらする人への対策です。
#  その場合は、入力フォームのHTMのTEXTAREAタグにおいて、MAXLENGTHを
#  小さくしてください(デフォルトは10000文字になっています)。
#  なお、MAXLENGTHで指定する文字数は英語換算ですので、日本語だと１文字
#  で２になります。つまり、MAXLENGTH=10000なら、日本語で5000文字までです。
#
#  <連続改行による荒らし制限> 2004.05 new
#
#  文字数制限をすると、無意味な連続改行だけしたテキストを投稿して
#  いたずらする人がいるそうです。そういう人に困っている場合はテキ
#  スト部分の総行数を制限する機能を使ってください。
#  (0=制限しない（デフォルト）,1=制限する)
$limit_body_cols_flag=0;	
#
#  上で"1"にした場合、どれだけの行数まで許可するかを決めてください。
#  （オーバすると投稿エラーになります）
#
# 本文の改行許可数
$body_text_max_cols="40";
#
#  <トリップ機能による、なりすまし防止> 2010.02new
#
# 名前#任意のワードでトリップを表示できるようにしてみました。
# 他人のなりすましで、掲示板が荒れる場合は、これをお使いください。
#
#  (1=トリップ機能を使えるようにする(推奨),0=しない)
$PM{'use_trip_flag'}=1;	
#
#  <自動バックアップ> 
#
#  定期的に記事を自動バックアップする機能がつきました。前回バックアップファ
#  イルを作成した日から間隔日以上空いて、新規登録があると、そのタイミングで
#  バックアップファイルを更新します。なお、バックアップは記事が５件以上ある
#  場合にのみ動作します。
#
#  自動定期バックアップを使用#
#  (1=使用する（デフォルト）,0=使用しない)
$PM{'make_backup_file'}	= '1';
#
#  バックアップする間隔(日)
$PM{'backup_day_interval'}  = '7';		
#
# Backup file name (recommended to change as appropriate for security reasons)
$PM{'backup_file_name'} = 'fileback.dat';
#
# <Admin Auto Email> sendmail
#
# When a new article is registered, you will be notified by e-mail to the following e-mail address.
# If you want to use this feature, make sure you provide all three of the following information:
# If you make a mistake in this information, it will cause trouble to the server administrator, so be sure to check with the administrator.
# and then configure carefully. Note that this function can only be used by providers
# is for UNIX-like users only. (Mac, Win is not possible) Use if you are not sure of the settings
# Don't.
# 
$use_email =0; # (1=yes,0=no)Default is 0
#
# Mail program path
# For normal providers, it would be '/usr/lib/sendmail' or '/usr/sbin/sendmail', etc. (professional
# It depends on the vida, so ask the provider where the CGI is installed for details).
# For home Windows server, set 'C:\blatj\blatj.exe', etc.
$mail_prog = '/usr/lib/sendmail'; # Path on old server
#$mail_prog = '/usr/sbin/sendmail'; # There are many passes here these days
#
# Administrator email address (your email address)
$recipient = 'yourname@your_provider.ne.jp';
#
# To create an image URL link in the body of the email, please specify the URL of the image storage directory.
$img_dir_url='http://yourprovider/yourname/imgboard/img-box/';
#
# <Good night> oyasumi
#
# Please set it to 0 when you want to take a break from the bulletin board for a while, such as going on a trip.
$bbs_open_flag=1; #(1=yes,0=no)Default is 1
# Bedtime message (change as appropriate)
#
$oyasumi_message=qq|
I will take a break for a while because the administrator is traveling. <BR>
We look forward to seeing you again.
|;
#
#
# Initializing Other Variables
$PM{'flock'} = '1'; # Using flock
$PM{'use_crypt'} = '1'; # Use encryption
#
#===============================================#
# < Load external configuration files (1.21 or later)> #
#===============================================#
#
# Load customized HTML and set parameters from outside.
# Moving and customization will be easier by upgrading the version.
#
# Use an external configuration file (1=yes,0=no)
$load_ext_config	=0;
#
# (Example) External configuration file that can be changed to a bulletin board with a mascot icon
$ext_config_name ="set_icon624.cgi"; # Configuration file name (extension must be cgi)
#
#
#=========================================#
# <HTML Advanced Settings Options> #
#=========================================#
#
#==========================#
# Overall HTML design
#==========================#
#
# < ELEMENTS IN BODY >
#
$PM{'body_bgcolor'} ="#FAF0E6"; # Overall background color
$PM{'body_text'} ="#2A3A3A"; # Base font color
$PM{'body_link'} ="#6060FF"; # Link color
$PM{'body_vlink'} ="#4040FF"; # Existing link color
$PM{'body_background'} =""; # Background Image Name
#
# (One point) The background color of general bulletin boards is often light colors, but
# If so, choose a darker background color to make your photos and images easier to see
#
# (Note) The basic font color of the reply field is specified in the "Design of the reply field" section.
#
#==========================#
# Design at the top of the bulletin board
#==========================#
#
# < Top Text Title >
# Top image title < >
# < Top Embedded Banner >
#
# <HTML excerpt> please specify it directly in HTML in the sub top_html below.
# (It seems that there are cases where extracting it makes it difficult to edit on the contrary)
#
#==========================#
# Form Entry Design
#==========================#
#
# < Display the form entry part on the bulletin board>
$form_disp_on_board =1; # (1=yes,0=no)Default is 1
#
#--Note If the above number is set to 0 and the input form is set to a separate window, the internal processing
# The display is a little slow due to the relationship. Leave as much as possible 1.
#
# < TABLE SHAPE >
#   
$table_bgcolor =""; # Background color of form parts
$table_background_image=""; # Form background image
$table_border ="0"; # Height of form frame
$table_cellspacing ="1"; # Width of the frame of the form part
$table_cellpadding ="0"; # Form frame margin
#
# < Font color and size in form >
#
$font_option ="color=#810808 size=+0"; # Parts other than the following
$font_option2 ="color=#9E8857 size=+0"; # "Image Selection" and "Title"
#
# < Font color and size of required/optional auto display >
#
# According to the setting in "Check the presence or absence of data in the form input item",
# Optional/optional automatic display can be automatically displayed next to form fields
#
$auto_disp_omit_frag ="1"; # Auto display (yes=1,no=0)
$f_param ="color=#555555 size=-1"; # Font color and size
#
# < Form field background color >
#
$ie_bg ="bgcolor=#ECAC8E"; # Basic background color of the field (for IE)
$ie_bg2 ="bgcolor=DEB887"; # "Select Image" field
$ie_bg3 ="bgcolor=DEB887"; # "Image Title" field
#
#
# < Do not let cookies remember (title) of form fields >
#
# Since R5.2, the default is not to remember titles.
# If you want to set this to remember, set the following flag to 0.
#
$no_cookie_for_subject=1;
#
#==========================#
# Article Department Design
#==========================#
#
# < HTML excerpt > specified directly below.
#
#==========================#
# Reply field design
#==========================#
#
# < Specify the background color/background image of the reply field >
#
# You can specify the background color/background image of the reply field here
$res_table_sitei="bgcolor=#F0E0D6";
#
# (One Point)
# How to write when specifying a background image "$res_table_sitei="bgcolor=#F0E0D6";"
# How to write when specifying a background image "$res_table_sitei="background=res_haikei.gif";"
#
# Basic font color of the reply field
$res_base_font_color="color=#404040";
#
#
#==========================#
# HTML--Bottom Design
#==========================#
#
# Banner advertisements at the bottom of bulletin boards are required on free CGI sites, etc.
# If you want to write the HTML source here. The insertion point is the delete button
It will be directly above the #. In addition, be sure to specify additional Height and Width in the banner.
# Dasai
#
$html_for_bottom_banner=qq|
<!--
If you want to add an additional banner ad at the bottom, remove the "comment-out tag" at the top and bottom,
Write your HTML password here.
-->
<!-- The following links are prohibited from being deleted: If you use this script for free, you can include additional ads, but please leave the link below. If you really want to remove it at a company, you can remove it by paying 20,000 yen. -->
<a href="http://xn--1sq65hw3win8a.com"> ( Highest discarded → purchase price.com ) </a> &nbsp &nbsp &nbsp &nbsp <a href="http://xn--xck0d2a9bc6737f2g4b.com"> ( ★ ★ Utilizing popular cloud & word of mouth to consider crisply →condominium consideration .com ) </a><BR>
|;
#
#=============================#
# HTML--Button Design
#=============================#
# 2014.10 Button style can be specified by CSS. The designation must be made within the sub top_html.
# 2012.10 With the installation on the button, direct link can be turned on / off with an argument
# 2012.04 The buttons were enlarged on smartphones, but in the case of PCs, the buttons were restored to normal
# 2010.04 Page can be specified directly
#
sub output_button_HTML{
#
local($PM{'use_direct_page_link'})=$_[0];# 引数1として取得
# (0=表示しない。1=表示する。2=逆にダイレクトリンクだけ表示する)
# ボタンのサイズ
local($ttmp_output_button_px)="style=\"font-size: 16px\"";

	# スマフォ/タブレットでボタンを大型化する
	if($output_button_px ne ""){
		$ttmp_output_button_px="$output_button_px";
	}
	

	if($PM{'use_direct_page_link'} != 2){

	# スマフォでスペースを入れる
	print "$output_button_space";

	print "<TABLE border=0 CELLSPACING=6 CELLPADDING=4><TR>";

	if($pre_page > 0){

	   # 先頭へジャンプ
	   if($pre_page > 0){

		print "<TD>";
		print "<FORM ACTION=\"$cgi_name\" METHOD=\"POST\">";
		print "<INPUT TYPE=\"HIDDEN\" NAME=\"page\" VALUE=1>\n";
		print "<INPUT TYPE=\"HIDDEN\" NAME=\"amode\" VALUE=$FORM{'amode'}>\n";
		print "<INPUT TYPE=\"HIDDEN\" NAME=\"p1\" VALUE=$FORM{'p1'}>\n";
		print "<INPUT TYPE=\"HIDDEN\" NAME=\"p2\" VALUE=$FORM{'p2'}>\n";
		print "<INPUT TYPE=\"HIDDEN\" NAME=\"bbsaction\" VALUE=\"page_change\">\n";
		print "$POSTADDP{'BUTTONTOPFORM'}\n"; # 将来拡張用

		# ワード検索時のページ変更ボタンは検索パラメータを引きずっていく
		if($FORM{'mode'} eq "search_menu"){
		 print "<INPUT TYPE=\"HIDDEN\" NAME=\"mode\" VALUE=\"search_menu\">\n";
		 print "<INPUT TYPE=\"HIDDEN\" NAME=\"SearchWords\" VALUE=\"$FORM{'SearchWords'}\">\n";
		 print "<INPUT TYPE=\"HIDDEN\" NAME=\"MatchMode\" VALUE=\"$FORM{'MatchMode'}\">\n";
		}
		print "<INPUT ID=\"btnPtop\" TYPE=\"SUBMIT\" VALUE=\" First \" $ttmp_output_button_px>\n";
		print "</TD>";
		print "<\/FORM>\n";
	   }

	   # 前の？件へジャンプ
		print "<TD>";
		print "<FORM ACTION=\"$cgi_name\" METHOD=\"POST\">";
		print "<INPUT TYPE=\"HIDDEN\" NAME=\"page\" VALUE=$pre_page>\n";
		print "<INPUT TYPE=\"HIDDEN\" NAME=\"bbsaction\" VALUE=\"page_change\">\n";
		print "<INPUT TYPE=\"HIDDEN\" NAME=\"amode\" VALUE=$FORM{'amode'}>\n";
		print "<INPUT TYPE=\"HIDDEN\" NAME=\"p1\" VALUE=$FORM{'p1'}>\n";
		print "<INPUT TYPE=\"HIDDEN\" NAME=\"p2\" VALUE=$FORM{'p2'}>\n";
		print "$POSTADDP{'BUTTONPREVFORM'}\n"; # 将来拡張用

		# ワード検索時のページ変更ボタンは検索パラメータを引きずっていく
		if($FORM{'mode'} eq "search_menu"){
		 print "<INPUT TYPE=\"HIDDEN\" NAME=\"mode\" VALUE=\"search_menu\">\n";
		 print "<INPUT TYPE=\"HIDDEN\" NAME=\"SearchWords\" VALUE=\"$FORM{'SearchWords'}\">\n";
		 print "<INPUT TYPE=\"HIDDEN\" NAME=\"MatchMode\" VALUE=\"$FORM{'MatchMode'}\">\n";
		}
		print "<INPUT ID=\"btnPback\" TYPE=\"SUBMIT\" VALUE=\" ＜Previous $disp_message case \" $ttmp_output_button_px>\n";
		print "</TD>";
		print "<\/FORM>\n";
	}else{
		print "<TD></TD>";
	}

	# 下部のページ切替えボタンのHTML
	if($next_page <= $total_page){

		print "<TD>";
		print "<FORM ACTION=\"$cgi_name\" METHOD=\"POST\">\n";
		print "<INPUT TYPE=\"HIDDEN\" NAME=\"page\" VALUE=$next_page>\n";
		print "<INPUT TYPE=\"HIDDEN\" NAME=\"bbsaction\" VALUE=\"page_change\">\n";
		print "<INPUT TYPE=\"HIDDEN\" NAME=\"amode\" VALUE=$FORM{'amode'}>\n";
		print "<INPUT TYPE=\"HIDDEN\" NAME=\"p1\" VALUE=$FORM{'p1'}>\n";
		print "<INPUT TYPE=\"HIDDEN\" NAME=\"p2\" VALUE=$FORM{'p2'}>\n";
		print "$POSTADDP{'BUTTONNENTFORM'}\n"; # 将来拡張用

		# ワード検索時のページ変更ボタンは検索パラメータを引きずっていく
		if($FORM{'mode'} eq "search_menu"){
		 print "<INPUT TYPE=\"HIDDEN\" NAME=\"mode\" VALUE=\"search_menu\">\n";
		 print "<INPUT TYPE=\"HIDDEN\" NAME=\"SearchWords\" VALUE=\"$FORM{'SearchWords'}\">\n";
		 print "<INPUT TYPE=\"HIDDEN\" NAME=\"MatchMode\" VALUE=\"$FORM{'MatchMode'}\">\n";
		}
		print "<INPUT ID=\"btnPnext\" TYPE=\"SUBMIT\" VALUE=\"Next $disp_message case >\" $ttmp_output_button_px>\n";
		print "</TD>";
		print "<\/FORM>\n";
	}else{
		print "<TD bgcolor=\"#808080\">No further pages available </TD>";
	}

		print "</TR></TABLE>";

	}

	# ページ指定：ダイレクトリンク 2010.04
	# 2014.11 検索ワードがあるときは、ダイレクトリンクを出さないことにした
	# なお、URLエンコードすれば検索ワードを入れることはできるが、
	# ユーザの入れたパラメータをGETに直接入れると脆弱性のリスクが増すため、しないことにする

	if(($PM{'use_direct_page_link'} >= 1)&&($FORM{'mode'} ne "search_menu")){
	
		if($total_page >= 1){	# 2012.10 Update

			if($PM{'use_direct_page_link'} == 2){
				print " &nbsp&nbsp Pages：[ "; 
			}else{
#				print "<BR><HR> &nbsp&nbsp ページ指定：[ "; 
				print "<HR> &nbsp&nbsp Pages：[ "; 
			}

			for($i=1;$i<=$total_page;$i++){

			# スマホのタッチ用にスペースを広げる
			print "$output_link_space"; 

			 local($tttt_ldflag)=0;
			 if($i == $disp_page){
					 $tttt_ldflag=0;
				print "<B>$i</B> $output_link_space/\n"; 
			 }else{
				$tttt_ldflag=0;
			 	if($i <= 20){
					$tttt_ldflag=1;
				}elsif($i <= 50){
					 $tttt_ldflag=1 if(($i % 5) == 0);
				}elsif($i <= 100){
					 $tttt_ldflag=1 if(($i % 10) == 0);
				}elsif($i <= 400){
					 $tttt_ldflag=1 if(($i % 50) == 0);
				}elsif($i <= 1000){
					 $tttt_ldflag=1 if(($i % 100) == 0);
				}elsif($i <= 10000){
					 $tttt_ldflag=1 if(($i % 1000) == 0);
				}elsif($i > 10000){
					 $tttt_ldflag=1 if(($i % 1000) == 0);
				}
			 }
			 if($tttt_ldflag==1){
					 print "<A HREF=\"$cgi_name?amode=$FORM{'amode'}&p1=$FORM{'p1'}&p2=$FORM{'p2'}&bbsaction=page_change&page=$i\">$i</A> $output_link_space/\n";
			 }
			}
			print "] <br>";
		}
	}

}
#
#==========================#
# その他のデザイン
#==========================#
#
# <ＨＴＭＬ抜粋>以下で直接指定してください。
#
#  ===================<ＨＴＭＬ抜粋>==========================================
#
#  ユーザサイドでＨＴＭＬを変更しやすいように,スクリプト中のＨＴＭＬ定義部分を
#  プログラムから以下に抜き出し列挙してあります．それぞれ,print<<HTML_END;行の
#  次の行からHTML_END記号の前行までは、通常ＨＴＭＬとして編集可能なので,ワード
#  パット(Win系) Jedit(Mac系)等のエディタでご自由に書き換えて、カスタマイズして
#  ください．ただし先頭に$がついているもの($body_bgcolor等)は変数なので、消す
#  場合は十分注意してください．
#  なお、当スクリプトはSJISコードを用いているため,「表示,申す,機能」等の特定の
#  文字がインターネット経由で見ると化けてしまう現象があります。この手の漢字や
#  文字を使用して文字化けが発生した場合は、文字化けした文字の前後に\マークを
#  入れて区切れば文字化けは出なくなります。なお、この場合、\はPerlでは文字区
#  切り記号として働き、Web上には表示されません。
#
#=====================================#
#     <ＨＴＭＬ--画面最上部>          #
#=====================================#
#
#  ＨＴＭＬヘッダ,ボディ指定．タイトル等画面最上部のＨＴＭＬです
#
#  print<<HTML_END;の次行から"HTML_END"のある行までは、通常のＨＴＭＬ
#  として編集可能です． 
sub top_html{

if($COOKIE{'viewport_set'} eq 'as_cgi_defined'){
 $top_html_vp_set='960';
}elsif($COOKIE{'viewport_set'} ne ""){
 $top_html_vp_set="$COOKIE{'viewport_set'}";
}else{
 $top_html_vp_set='960';
}

print<<HTML_END;
<HTML lang="ja">
<HEAD><TITLE>$title</TITLE>$top_html_header
<meta name="viewport" content="width=$top_html_vp_set,
 maximum-scale=1.0,minimum-scale=0.27, ">
<link rel="apple-touch-icon" href="./apple-touch-icon.png" />
<STYLE>
<!--
select { 
background-color:#8B0000;
font-size:18px;
font-family : MS UI GOTHIC ; 
color:#FFFFFF
}
input { 
background-color:#ffffff;
font-size:16px;
color:#606060
}
textarea { 
background-color:#ffffff;
font-size:14px;
color:#606060
}

$PM{'top_style_option'}

-->
</STYLE>
</HEAD>
<BODY BGCOLOR="$PM{'body_bgcolor'}" BACKGROUND="$PM{'body_background'}" TEXT="$PM{'body_text'}" LINK="$PM{'body_link'}" VLINK="$PM{'body_vlink'}">$body_tag_f
$PM{'counter_main_html'}


<!-- <BASEFONT SIZE="3"> -->
<!-- 基本フォントサイズ指定(使用する場合は上記コメントアウトを外す) -->

<!-- 掲示板最上部タイトルエリア・・画像や絵を入れることができます -->$PM{'INS_POINT_TOP01'}
<!-- (アドバイス)画像やカウンタを入れる場合はheight,widthを指定するとレイアウトが非常に早くなります -->

<CENTER>$PM{'INS_POINT_TOP02'}
<!-- バナーや、トップ位置の画像はここへHTMLを書いてください -->

</CENTER>

<UL>
 <H3>Image Upload Board</H3>
 Smartphone(iPhone,Android),Galapagos version & Anti-spam Ver.5.0 
</UL>
HTML_END
}
#
#=====================================#
#     <ＨＴＭＬ--アンカーリンク部分>  #
#=====================================#
#
#  フォームの下にある[ワード検索]、[携帯対応]、[管理等]のアンカーリンクを
#  作る部分のＨＴＭＬです。
#
#  (ワンポイント) 他にリンク等を追加したい場合はここへリンクを
#   追加すると収まりが良いでしょう。
#
# 2010.03 Windows7/iPhone/iPad/Android等のタッチ液晶対応のためリンク文字を離した
#
sub link_top_html{

print<<HTML_END;
<DIV align=right>
<BIG>
$cm_out_exit_h [ <a href="$back_url">Back to Top</a> ] $cm_out_exit_f
[ <a href="$cgi_name?mode=search_menu&amode=$FORM{'amode'}&p1=$FORM{'p1'}&p2=$FORM{'p2'}$GETURLADDP{'WS'}&page=$FORM{'page'}">Search</a> ]
[ <a href="$cgi_name?mode=keitai_menu&amode=$FORM{'amode'}&p1=$FORM{'p1'}&p2=$FORM{'p2'}&page=$FORM{'page'}">"Galapagos" support</a> ]
[ <a href="$cgi_name?mode=disp_admin_check_menu&amode=$FORM{'amode'}&p1=$FORM{'p1'}&p2=$FORM{'p2'}&page=$FORM{'page'}">Ad,om</a> ]
&nbsp&nbsp&nbsp
</BIG>
</DIV>
HTML_END
}
#
#=====================================#
#     <ＨＴＭＬ--画面中央の説明>      #
#=====================================#
#
#  真ん中の説明部分のＨＴＭＬです．
#
#  (ワンポイント)
# 「パソコン」の部分に「\」が入っているのは文字化け防止のためです。
#  文字化けする場合はこの例のようにテキストの間に「\」を入れると良い
#  でしょう。
#
sub middle_A_html{
  local($mes_01);
  if($allow_other_multimedia_data==1){
	$html_mA01="File";
  }else{
	$html_mA01="Image";
  }
  if($disp_rcmd_upload_size_flag==1){
	$mes_01=qq| 推奨<B>$rcmd_upload_size KB</B>以下\/|;
  }

  # 省略のときは出さない
  if($COOKIE{'middle_html_disp'}==1){
   return;
  }

print<<HTML_END;
<HR>
<!--掲示板中央部の説明部分A-->
<font size=-1>
 <UL>
<LI>You can upload $html_mA01 on your PC, iPhone, Android, or mobile phone. ($mes_01 image maximum <B>$max_upload_img_size KB (Android available)</B>/non-image up to <B>$max_upload_size KB</B>)
 <LI>Please do not upload (including embedding) or download anything that is copyrighted. Posting advertisements are also prohibited.
 <!--タグ使用上の注意が自動で入ります-->$tag_siyou_tyuui
</UL>
</font>
HTML_END
}

sub middle_B_html{

  # 省略のときは出さない
  if($COOKIE{'middle_html_disp'}==1){
   return;
  }

#  追加説明
 if($HTTP_USER_AGENT=~ /ipad/i){
if($MYCGI_ENV{'iOS_VER'} < 6){
$iPhone_mes_01=qq|
<font color=red>(Images posted on iPhone/iPad with iOS.Ver.5 or lower)</font><BR>
 (Method\.1) If you update to iOS.Ver.6 or later, you can \post\directly in safari<BR>
 (Method \.2) For iOS Ver.5 or lower: <a href="http://itunes.apple.com/jp/app/simple-resize/id327776379?mt=8&uo=4" target="itunes_store">Simple Resize</a> to reduce the photo (strictly below 640 size).<a href="http://itunes.apple.com/jp/app/opera-mini-web-browser/id363729560?mt=8&uo=4" >Opera Mini</a>(File attachments OK) to access the Web and submit your manuscript. 
|;
}else{
$iPhone_mes_01=qq|
<font color=red>(iOS.Ver.6以降のiPhone/iPadで画像投\稿\)</font><BR>
 iOS.Ver.6以降は、safariで直接投\稿\できます<BR>
 <a href="http://itunes.apple.com/jp/app/simple-resize/id327776379?mt=8&uo=4" target="itunes_store">Simple Resize</a>で写真を縮小(640サイズ以下厳守)してから投\稿\! 
|;
}
 }

 
print<<HTML_END;
<font size=-1>
<UL>
<!--掲示板中央部の説明部分B-->
  <LI><B> $disp_message </B> page by new article. A maximum of <B>$max_message</B> articles will be logged,
      Exceeding it will delete the oldest articles</LI>
  </UL>
</font>
$iPhone_mes_01
HTML_END
}
#
#=====================================#
#     <ＨＴＭＬ--投稿記事部分>        #
#=====================================#
#
#  imgboard allows users to select "display mode".
# So, you have to change the layout of each article section according to each "display mode" such as text link, icon size, fixed size, full size, etc.
# Each "display mode" requires a different layout for each article section.
# but since they are very similar, here are the basic layouts
# of the two basic layouts (basic layout for small images / basic layout for large images).
# and replace a part of it ($html_block_A).
# to cover all "display modes". Layout.
# If you want to change the layout yourself, please understand the above points before editing.
# 1.
# 1. Layout pattern 1/ Layout for articles with small images
# (---- for text articles, text link display, and icon size display)
#
# (Note: $html_block_A in the layout is assigned the block described below.

Translated with www.DeepL.com/Translator (free version)
#
sub kiji_base_html{

print<<HTML_END;
<!--記事レイアウト テキスト記事、テキストリンク\表\示、アイコンサイズ\表\示用-->
<FONT SIZE="+1" COLOR="#FF0000"><B>$tmp_subject</B></FONT>
$icon_html
 <FONT COLOR="#00FF00"><B>$mail_a_start $tmp_name $mail_a_end</B></FONT>
$tmp_date $auto_user_IP $disp_seq_no $disp_re
$tmp_url_link
<BLOCKQUOTE $tmp_bq_opt><!-- body_start -->
	$tmp_body <!-- $ddd -->
</BLOCKQUOTE>
$html_block_A
$keitai_env_link
HTML_END
}
#
#  テキスト、テキストリンク、アイコンサイズ、各表示モードに
#  より以下のＨＴＭＬが上記レイアウトのhtml_block_Aに代入されます。
#  以下でその代入ブロックを編集できます。
#
sub set_html_block{
# 変数の準備
$img_dsize="$IMG_PARAMETERS{'dsize'}";
#
# 2009.12 update
  $ttmp_target_sitei=qq|TARGET="top"|;
  if($HTTP_USER_AGENT=~ /ipod|iphone|android|PSP/i){
		$ttmp_target_sitei="";
  }

#  1.1テキスト/テキストリンクモード時用の $html_block_A
$textlink_html_block=qq|
<BLOCKQUOTE> $data_type： 
 <A HREF="$tmp_img_location" $ttmp_target_sitei>
  $tmp_imgtitle
 </A>-$img_dsize 
</BLOCKQUOTE>
|;
#  1.2アイコンサイズモード時用の $html_block_A
$icon_html_block=qq|
<BLOCKQUOTE> 画　像： 
 <A HREF="$tmp_img_location" TARGET="top">
  <img src="$tmp_img_location" $w_set $h_set border="0">
   $tmp_imgtitle
 </A>-$img_dsize 
</BLOCKQUOTE>
|;
}
#
#   2.レイアウトパターン2/ 画像がメインな記事系レイアウト
#  (------横固定サイズ表示＆オート＆オリジナルサイズ表示用--------）
sub kiji_base2_html{

  local($ttmp_img_location)="$tmp_img_location";
  if($tmp_snl_location ne ""){
   $ttmp_img_location="$tmp_snl_location";
  }

  if($HTTP_USER_AGENT=~ /ipod|iphone|ipad|android/i){
   &kiji_base2_ipod_html;
   return;
  }


print<<HTML_END;
<!--記事レイアウト 横固定サイズ＆オート＆オリジナルサイズ用-->
Image Title：<A HREF="$tmp_img_location" TARGET="top">$tmp_imgtitle
<IMG SRC="$ttmp_img_location" BORDER="0" $size_sitei ALIGN="LEFT" HSPACE="12" style="margin: 12px;float: left">
</A>-$img_dsize<BR>
<BR>
<FONT SIZE="+1" COLOR="#FF0000"><B>$tmp_subject</B></FONT>
$icon_html <FONT COLOR="#00FF00"><B>$mail_a_start $tmp_name $mail_a_end</B></FONT>
$tmp_date $auto_user_IP $disp_seq_no $disp_re
$tmp_url_link
<BLOCKQUOTE $tmp_bq_opt><!-- body_start -->
$tmp_body
</BLOCKQUOTE>
$keitai_env_link
$br_auto_clear
HTML_END
}
#
#   2.レイアウトパターン2/ 画像がメインな記事系レイアウト(ipod/iPhone/Android)
#  (------横固定サイズ表示＆オート＆オリジナルサイズ表示用--------）
sub kiji_base2_ipod_html{

  local($ttmp_img_location)="$tmp_img_location";
  if($tmp_snl_location ne ""){
   $ttmp_img_location="$tmp_snl_location";
  }

  if($HTTP_USER_AGENT=~ /ipad/i){
print<<HTML_END;
<!--記事レイアウト 横固定サイズ＆オート＆オリジナルサイズ用-->
Image Title：<a href="$cgi_name?bbsaction=disp_fullscr&timg_location=$tmp_img_location&timg_w=$IMG_PARAMETERS{'width'}&timg_h=$IMG_PARAMETERS{'height'}&timg_dsize=$IMG_PARAMETERS{'dsize'}&timg_type=$IMG_PARAMETERS{'type'}">$tmp_imgtitle
<IMG SRC="$ttmp_img_location" BORDER="0" $size_sitei ALIGN="LEFT" HSPACE="12" ALT=" クリックで拡大 " style="margin: 12px;float: left"></A>
-$img_dsize<BR>
HTML_END
  }else{
print<<HTML_END;
<!--記事レイアウト 横固定サイズ＆オート＆オリジナルサイズ用-->
Image Title：<a href="$cgi_name?bbsaction=disp_fullscr&timg_location=$tmp_img_location&timg_w=$IMG_PARAMETERS{'width'}&timg_h=$IMG_PARAMETERS{'height'}&timg_dsize=$IMG_PARAMETERS{'dsize'}&timg_type=$IMG_PARAMETERS{'type'}">$tmp_imgtitle</A>
<IMG SRC="$ttmp_img_location" BORDER="0" $size_sitei ALIGN="LEFT" HSPACE="12" ALT=" ダブルタップで拡大 " style="margin: 12px;float: left">
-$img_dsize<BR>
HTML_END
  }
print<<HTML_END;
<BR>
<FONT SIZE="+1" COLOR="#FF0000"><B>$tmp_subject</B></FONT>
$icon_html Name：<FONT COLOR="#00FF00"><B>$mail_a_start $tmp_name $mail_a_end</B></FONT>
$tmp_date $auto_user_IP $disp_seq_no $disp_re
$tmp_url_link
<BLOCKQUOTE $tmp_bq_opt><!-- body_start -->
$tmp_body
</BLOCKQUOTE>
$keitai_env_link
$br_auto_clear
<BR CLEAR="LEFT" style="clear :left">
HTML_END
}
#   3.レイアウトパターン3/ 返信記事レイアウト
sub kiji_rep_html{

	# 旧外部ファイルとの互換部分(指定がない場合はpinkにする)
	$res_base_font_color="color=pink" if($res_base_font_color eq "");

print<<HTML_END;
<!--返信用 ↓全体のフォントはここで指定 -->
<font $res_base_font_color>
<FONT SIZE="+1" COLOR="#FF0000"><B>$tmp_subject</B></FONT>
$icon_html Name：<FONT COLOR="#00FF00"><B>$mail_a_start $tmp_name $mail_a_end</B></FONT>
$tmp_date $auto_user_IP $disp_seq_no 
$tmp_url_link
<BLOCKQUOTE $tmp_bq_opt><!-- body_start -->
	$tmp_body
</BLOCKQUOTE>
$keitai_env_link</font>
HTML_END
}
#=========================================#
#     <ＨＴＭＬ--入力フォーム部>          #
#=========================================#
#
#  記事入力フォーム部のＨＴＭＬ．入力項目を増やしたり、減らしたりしたい
#  場合はここを変更してください。だだし、変更によりＣＧＩがうまく動かな
#  くなる可能性がありますので,ここは変更する時は十分注意してください．
#  なお、URL等の項目を追加したいなど、よくある希望に対しては、外部設定
#  ファイルというカスタマイズした設定ファイルを使うことにより、より簡単
#  に実現できますので、自分でカスタマイズするよりも、それを使った方が楽
#  でしょう。なお、同ファイルはサポートサイトの方で配布しています。  
#
sub form_html{
&ext_config_form_pre if($EXTSUB{'form_pre'} == 1 );
&auto_omit_disp;
$COOKIE{'subject'}="" if($no_cookie_for_subject ==1);

# 2008.06.25
&auto_cols_change;

sub auto_cols_change{
	if($HTTP_USER_AGENT=~ /ipod|iPhone|android/i){
          $form_textarea_cols="50";
	}elsif($HTTP_USER_AGENT=~ /PSP/i){
          $form_textarea_cols="40";
	}else{
          $form_textarea_cols="56";
    }
}

print<<HTML_END;
<!-- フォーム入力部・・・ここはあまり変更しない方がいいでしょう -->
<FORM ACTION="$cgi_name" METHOD="POST" ENCTYPE="multipart/form-data" style="display: inline">
<INPUT TYPE="HIDDEN" NAME="bbsaction" VALUE="post">
<INPUT TYPE="HIDDEN" NAME="page" VALUE="$FORM{'page'}">
<INPUT TYPE="HIDDEN" NAME="view_mode" VALUE="$COOKIE{'view_mode'}">
<INPUT TYPE="HIDDEN" NAME="form_mode" VALUE="$COOKIE{'form_mode'}">
<INPUT TYPE="HIDDEN" NAME="middle_html_disp" VALUE="$COOKIE{'middle_html_disp'}">
<INPUT TYPE="HIDDEN" NAME="blood" VALUE="$FORM{'blood'}">
<INPUT TYPE="HIDDEN" NAME="parent" VALUE="$FORM{'parent'}">
<INPUT TYPE="HIDDEN" NAME="prebbsaction" VALUE="$FORM{'bbsaction'}">
<INPUT TYPE="HIDDEN" NAME="amode" VALUE="$FORM{'amode'}">
<INPUT TYPE="HIDDEN" NAME="p1" VALUE="$FORM{'p1'}">
<INPUT TYPE="HIDDEN" NAME="p2" VALUE="$FORM{'p2'}">
<INPUT TYPE="HIDDEN" NAME="target" VALUE="$FORM{'target'}">
<INPUT TYPE="HIDDEN" NAME="target_no" VALUE="$FORM{'target_no'}">
$POSTADDP{'UPLOADFORM'}<!-- 将来拡張用 -->
<UL>
<TABLE ID="uploadmain" BORDER="$table_border" CELLSPACING="$table_cellspacing" CELLPADDING="$table_cellpadding" bgcolor="$table_bgcolor" background="$table_background_image">
<!-- 投稿用パスワード。会員制にするときに使用 -->
<!-- ＄cm_out_xx_xは設定モードにより、自動的にＨＴＭＬコメントアウト記号＜！ーー等が代入されます -->
$cm_out_pw_h
<TR $ie_bg >
 <TD ALIGN=CENTER><font $font_option>会員パスワード： </font></TD>
 <TD colspan=2><INPUT TYPE="PASSWORD" NAME="entry_passwd" SIZE=15 VALUE="$COOKIE{'entry_passwd'}" MAXLENGTH="20">*NECCESSARY $POSTADDP{'MEMBERPASS'}</TD>
</TR>
$cm_out_pw_f
<TR $ie_bg>
 <TD ALIGN=RIGHT><font $font_option>Name： </font></TD>
 <TD colspan=2><INPUT TYPE="TEXT" NAME="name" SIZE=30 VALUE="$COOKIE{'name'}" MAXLENGTH="40"> $DISP_OMIT{'name'}</TD>
</TR>
<!-- SPAM予防のため,最近は掲示板にemailアドレスを入れる人がまずいないので、デフォルトは省略とした
<TR $ie_bg >
 <TD ALIGN=RIGHT><font $font_option>e-mail： </font></TD>
 <TD colspan=2><INPUT TYPE="TEXT" NAME="email" VALUE="$COOKIE{'email'}" SIZE=30 MAXLENGTH="50"> $DISP_OMIT{'email'}</TD>
</TR>
-->
<TR $ie_bg >
 <TD ALIGN=RIGHT><font $font_option>Name： </font></TD>
 <TD colspan=2><INPUT TYPE="TEXT" NAME="subject" VALUE="$COOKIE{'subject'}" SIZE=30 MAXLENGTH="60"> $DISP_OMIT{'subject'}</TD>
</TR>$PM{'INS_POINT_FORM01'}<!-- ←将来拡張用 -->

HTML_END
&ext_config_form_opt if($EXTSUB{'form_opt'} == 1 );# 外部設定ファイルによる将来拡張用
print<<HTML_END;

<!-- 予\備の入力項目パラメータ・入力項目を増やしたい場合に使用 -->
<!-- なお、ここで有効化した項目のデータは、記事部分のHTML(kiji_base_html/kiji_base2_html)内に、$OPTDATA{'optA'}等の記号を書くと、書いた位置に代入され、表\示されます -->

<!-- 項目A入力欄ここから 使用時は下の＜！--を取る -->
<!--
<TR $ie_bg >
 <TD ALIGN=RIGHT><font $font_option>Input data A  $DISP_OMIT{'optA'}</font></TD>
 <TD colspan=2><INPUT TYPE="TEXT" NAME="optA" VALUE="$COOKIE{'optA'}" SIZE=55 MAXLENGTH=100></TD>
</TR>
-->
<!-- 項目A入力欄ここまで 使用時は上の--＞を取る -->
<!-- 項目B入力欄ここから 使用時は下の＜！--を取る -->
<!--
<TR $ie_bg >
 <TD ALIGN=RIGHT><font $font_option>Input data B $DISP_OMIT{'optB'}</font></TD>
 <TD colspan=2><INPUT TYPE="TEXT" NAME="optB" VALUE="$COOKIE{'optB'}" SIZE=32 MAXLENGTH=100></TD>
</TR>
-->
<!-- 項目B入力欄ここまで 使用時は上の--＞を取る -->

<!-- 項目C入力欄ここから 使用時は下の＜！--を取る -->
<!--
<TR $ie_bg >
 <TD ALIGN=RIGHT><font $font_option>Input data C $DISP_OMIT{'optC'}</font></TD>
 <TD colspan=2><INPUT TYPE="TEXT" NAME="optC" VALUE="$COOKIE{'optC'}" SIZE=32 MAXLENGTH=100></TD>
</TR>
-->
<!-- 項目C入力欄ここまで 使用時は上の--＞を取る -->

<!-- もっと増やしたい場合は、D,E,F....と同様に追加して増やしてください -->

<TR $ie_bg >
 <TD ALIGN=RIGHT><font $font_option>本文：</font></TD>
 <TD colspan=2>
<TEXTAREA ID="uploadmainTAREA1" NAME="body" COLS="$form_textarea_cols" ROWS=6 MAXLENGTH=10000 WRAP=SOFT>$COOKIE{'body'}</TEXTAREA>$DISP_OMIT{'body'}</TD>
</TR>

$cm_out_img_h
<TR $ie_bg2 >
 <TD ALIGN=RIGHT><font $font_option2 >Image Selection </font></TD>
 <TD colspan=2><INPUT TYPE="FILE" NAME="img" VALUE="" SIZE=30> $DISP_OMIT{'img'}</TD>
</TR>
<TR $ie_bg3 >
 <TD ALIGN=RIGHT NOWRAP><font $font_option2 > &nbsp&nbspTitle of image </font></TD>
 <TD colspan=2><INPUT TYPE="TEXT" NAME="imgtitle" SIZE=30 MAXLENGTH=60><font $f_param>*省略可</font></TD>
</TR>
$cm_out_img_f
HTML_END

if($use_guest_passwd=='-1'){
 $rmkey_default_checked="CHECKED" if($COOKIE{'rmkeym'} eq "on");

 if($FORM{'bbsaction'} ne "edit_form"){
print<<HTML_END;
<!-- 削除キー -->
<TR $ie_bg >
 <TD ALIGN=RIGHT><font $font_option>Deletion Key </font></TD>
 <TD><INPUT TYPE="PASSWORD" NAME="rmkey" VALUE="$COOKIE{'rmkey'}" SIZE=4 MAXLENGTH=16>
  $DISP_OMIT{'rmkey'} Used when deleting posts. Numbers, up to 4 digits.</TD>
 <TD ALIGN=LEFT>
 <INPUT TYPE="CHECKBOX" NAME="rmkeym" $rmkey_default_checked>Memorize key</TD>
</TR>
HTML_END
 }else{
print<<HTML_END;
<!-- 削除キー -->
<INPUT TYPE="HIDDEN" NAME="rmkey" VALUE="$COOKIE{'rmkey'}">
<INPUT TYPE="HIDDEN" NAME="rmkeym" VALUE="$COOKIE{'rmkeym'}">
HTML_END
 }
}

print<<HTML_END;
<TR ID="uploadmain_submit">
 <TD>
 $form_sage_checkbox_html
 </TD>
 <TD><INPUT ID="btnS1" TYPE="SUBMIT" VALUE=" Send "><INPUT ID="btnR1" TYPE="RESET" VALUE="Reset">
 </TD>
 </FORM>
 <TD align=center></TD>
</TR>
</TABLE>
</UL>
HTML_END
}
#
#===================================================#
#     <ＨＴＭＬ--画像フルスクリーン表示部>          #
#===================================================#
# 2008.06 new
#
#  iPod Touch/iPhone/Androidで画像だけを呼び出した場合、小さく表示されてしまうため、
#  フルスクリーンに出すために新設したＨＴＭＬ部です。
#
#  print<<HTML_END;の次行から"HTML_END"のある行までは、通常のＨＴＭＬ
#  として編集可能です． 
sub disp_fullscreen_html{

    local($tmp_title)=$_[0];# 引数1として取得
	local($tmpp_img_location)=$_[1];# 引数2として取得
	    local($tmpp_img_width)=$_[2];# 引数3として取得
		local($tmpp_img_height)=$_[3];# 引数4として取得
		local($tmpp_img_dsize)=$_[4];# 引数4として取得
		local($tmpp_img_type)=$_[5];# 引数4として取得

		    print<<HTML_END;
<HTML lang="ja">
<HEAD><TITLE>imgboard iPad/iPhone/Android AUTO FULLSCR</TITLE>
$top_html_header
<meta name="viewport" content="width=768">
</HEAD>
<BODY BGCOLOR="#444444" TEXT="$PM{'body_text'}">
<img src="$tmpp_img_location"  width="100%" hspace=0 vspace=0 border="1" alt="$tmp_title" bordercolor="#FFFFFF"  align="left" style="margin: 0px;float: left">
<BR CLEAR="LEFT" style="clear :left">

<FORM>
<INPUT TYPE="button" VALUE=" Back " onClick="history.back()" $output_button_px>
$tmpp_img_type - w $tmpp_img_width/h $tmpp_img_height - $tmpp_img_dsize

</FORM>
<NOSCRIPT>
<a href="$ENV{'HTTP_REFERER'}">Back</a>
</NOSCRIPT>



</BODY>
</HTML>
HTML_END
}
#
#------------ＨＴＭＬ抜粋ここまで------------#
# cfg_end


    #=================================================================#
    #     以上でユーザカスタマイズ部分である初期設定は終わりです      #
    #     以下はプログラムになります．                                #
    #=================================================================#


#=======================================================================#
# メインルーチン
#=======================================================================#

&init_valiables;			# 初期化

&check_open;				# 開店確認

&read_input;				# フォームの内容とクッキーを読み込む

&ext_config_amode if($EXTSUB{'amode'}==1);# 外部設定による将来拡張用

&amode_done;				# 管理者画面の処理

&ext_config_bbsaction if($EXTSUB{'bbsaction'}==1);# 外部設定による将来拡張用

if($FORM{'bbsaction'} eq 'post'){		# モードが投稿モードの場合
	&check_post_browser_type;		# ブラウザチェック
	&check_entry_passwd;			# 会員チェック
	&protect_from_BBS_cracker;		# 荒し対策

	&read_cookie;				# クッキーを読込む
	&limit_upload_times;			# 連続投稿回数チェック


	if($FORM{'prebbsaction'} eq 'edit_form'){# 置換モードの場合
		&replace_data("$FORM{'target'}","$file");# 修正処理
	}else{
		&check_double_post("$FORM{'email'}","2","1");# 2重投稿チェック
		&post_data("$file");		# 投稿処理
		&set_cookies;			# クッキーをセット
	}

	&send_mail;				# 管理者へメール	
	&jump_html;				# パラメータクリア用ＨＴＭＬ
	exit;					# 終了

}elsif($FORM{'bbsaction'} eq 'remove'){	# モードが削除モードの場合

	if($FORM{'passwd'} eq $admin_passwd){
		$remove_mode="admin";		# 削除モード
		&remove_data("$file");		# 削除処理
		&jump_html;			# パラメータクリア用ＨＴＭＬ
		exit;				# 終了
	}elsif(($FORM{'passwd'} eq $guest_passwd)&&($use_guest_passwd ==1)){
		$remove_mode="guest";		# 削除モード
		&remove_data("$file");		# 削除処理
		&jump_html;			# パラメータクリア用ＨＴＭＬ
		exit;				# 終了
	}elsif($use_guest_passwd =='-1'){
		$remove_mode="rmkey";		# 削除モード
		&remove_data("$file");		# 削除処理
		&jump_html;			# パラメータクリア用ＨＴＭＬ
		exit;				# 終了
	}else{
		&error("Wrong password. Deletion has been canceled.");
	}

}elsif($FORM{'bbsaction'} eq 'pf_change'){# モードがプロファイル変更の場合
	&set_cookies;				# クッキーをセット
	&jump_html;				# パラメータクリア用ＨＴＭＬ
	exit;					# 終了

}elsif($FORM{'bbsaction'} eq 'page_change'){# モードがページ変更の場合
	&read_cookie;				# クッキーを読込む

}elsif($FORM{'bbsaction'} eq 'disp_form_only'){# フォームウィンド表示の場合
	print "Content-type: text/html"."$Netscape4x_ch_set"."\n\n";
	&top_html;
	&output_form_html;			# 入力フォームを表示
	print "</BODY></HTML>\n";
	exit;
}elsif($FORM{'bbsaction'} eq 'disp_rep_form'){# 返信用ウィンド表示の場合
	print "Content-type: text/html"."$Netscape4x_ch_set"."\n\n";
	&top_html;
	print "<UL><H2>Reply to article No. $FORM{'parent'} <font size=-1 color=gray> (Recommended: 200 characters or less)</font></H2>\n";
	print "[<a href=\"$cgi_name?amode=$FORM{'amode'}&p1=$FORM{'p1'}
&p2=$FORM{'p2'}&page=$FORM{'page'}\">Back without reply</a>]</UL>\n";
	$form_sage_checkbox_html=qq|<INPUT TYPE="checkbox" NAME="sage" VALUE="1">sage| if($PM{'use_sage'} == 1);
	&output_form_html;			# 入力フォームを表示
	&protect_from_BBS_cracker if($PM{'no_disp_for_cracker'}==1);# 荒し対策
    	&output_html("$file");			# 掲示板を表示
	exit;
# twitter用API	
}elsif($FORM{'twi'} ne ""){# twitter用処理の場合
	# twitter用の短縮URLパラメータを復元
	# http://myhost.jp/imgboard.cgi?twi=b100411033041p1024drfx
# twitterっぽい雰囲気で違和感をなくすかな
$PM{'top_style_option'}=qq|
body { 
background: #C0DEED url('http://www.big.or.jp/~talk/t-club/soft/img/twitter_bg.png') repeat-x;
}
|;
	if($FORM{'twi'}=~ /b(\d+)p(\d+)(p*)(\d*)(\w+)x(\w*)/i){
		$FORM{'blood'}	="$1";		# 復元
		$FORM{'parent'}	="$2";		# 復元
		$FORM{'page'}	="$4";		# 復元
		$FORM{'twia'}	="$5"; 		# twitter actionを復元	
		$FORM{'twip'}	="$6"; 		# twitter parameterを復元	
	}
	if($FORM{'twia'} eq "drf"){
		$FORM{'bbsaction'}='disp_rep_form'; # 復元
	print "Content-type: text/html"."$Netscape4x_ch_set"."\n\n";
	&top_html;
	print "<UL>from twitter<BR><H2>It'll comment on the image thread. <font size=-1 color=gray> (Recommended: 200 characters or less)</font></H2>\n";
	print "[<font size=+1><a href=\"$cgi_name?amode=$FORM{'amode'}&p1=$FORM{'p1'}
&p2=$FORM{'p2'}&page=$FORM{'page'}\">←Back to Bulletin Board</a></font>]</UL>\n";
	$form_sage_checkbox_html=qq|<INPUT TYPE="checkbox" NAME="sage" VALUE="1">sage| if($PM{'use_sage'} == 1);
	&output_form_html;			# 入力フォームを表示
	&protect_from_BBS_cracker if($PM{'no_disp_for_cracker'}==1);# 荒し対策
    	&output_html("$file");			# 掲示板を表示
	exit;
	}
# 2008.06.26 for ipod/iPhone
}elsif($FORM{'bbsaction'} eq 'disp_fullscr'){# フルスクリーン表示の場合
    print "Content-type: text/html"."$Netscape4x_ch_set"."\n\n";
    &protect_from_BBS_cracker if($PM{'no_disp_for_cracker'}==1);# 荒し対策
    &disp_fullscreen_html($FORM{'timg_location'},$FORM{'timg_location'},$FORM{'timg_w'},$FORM{'timg_h'},$FORM{'timg_dsize'},$FORM{'timg_type'});
exit;

# 配布版では未使用
}elsif($FORM{'bbsaction'} eq 'remove_select'){	# 削除記事の選択
	print "Content-type: text/html"."$Netscape4x_ch_set"."\n\n";
	$title=qq| 削除確認 |; 
	&top_html;
	&output_remove_select_html;		# 削除パス確認画面を出す
	print "</BODY></HTML>\n";
	exit;

}elsif($FORM{'bbsaction'} eq 'edit_form'){	# 記事編集画面
	print "Content-type: text/html"."$Netscape4x_ch_set"."\n\n";
	$title=qq| 修正フォーム |; 

	&edit_top_html;
	&load_target_kiji("$FORM{'target'}","$file");

	if($FORM{'amode'} eq "icon_edit"){
	 &output_wp_upload_form;		# WP入力フォームを表示
	}else{
	 &output_form_html;			# 入力フォームを表示
	}

	print "</BODY></HTML>\n";
	exit;

}

# アクションが何も指定されていない時は、表示となる
# 各モードにより表示画面の種類を分岐させて表示させる

  &ext_config_mode if($EXTSUB{'mode'}==1);	# 外部設定による将来拡張用

  if($FORM{'mode'} eq "disp_admin_check_menu"){
	# 管理者確認メニュー表示
	print "Content-type: text/html"."$Netscape4x_ch_set"."\n\n";
	&output_admin_check_HTML;
	exit;
  }elsif($FORM{'mode'} eq "disp_icon_list"){
	# アイコン一覧を表示
	print "Content-type: text/html"."$Netscape4x_ch_set"."\n\n";
	&output_icon_list_HTML;
	exit;
  }elsif($FORM{'mode'} eq "disp_admin_menu"){
	# 設定変更メニューを表示
	if(&check_passwd("$FORM{'apasswd'}","$admin_passwd","0")==1){
		&set_admin_cookies; # 管理者パスを一時記憶
		print "Content-type: text/html"."$Netscape4x_ch_set"."\n\n";
		&output_admin_menu_HTML;
	}else{
		&error("パスワードが違います．処理を中止しました．","","1");
	}
	exit;
  }elsif($FORM{'mode'} eq "search_menu"){
	# ワード検索メニュー表示
	print "Content-type: text/html"."$Netscape4x_ch_set"."\n\n";

	# 2010.04 ワード検索メニューにおける、
	# クロスサイトスクリプティング対策を追加
	&form_check;

	&output_search_menu_HTML;
	if($FORM{'SearchWords'} ne ""){
	    &protect_from_BBS_cracker if($PM{'no_disp_for_cracker'}==1);# 荒し対策
    	    &output_html("$file");		# 掲示板を表示
 	    exit;				# 終了
	}else{
		print " 検索ワードが何もありませんでした．入力してください \n";
	}
	&output_search_menu_HTML2;
	exit;
  }elsif($FORM{'mode'} eq "keitai_menu"){
	# 携帯対応メニューを表示
	print "Content-type: text/html"."$Netscape4x_ch_set"."\n\n";
	&output_keitai_menu_HTML;
	exit;
  }else{
    # モードが指定されてない場合,掲示板を表示
	&protect_from_BBS_cracker if($no_disp_for_cracker==1);	# 荒し対策

	print "Content-type: text/html"."$Netscape4x_ch_set"."\n\n";
	# HTMLヘッダ,ボディ．（書換えは初期設定の所で行う）
	&top_html;
	$COOKIE{'body'}="";
	&output_form_html;					# フォームを表示
	&output_html("$file");					# 掲示板を表示
	exit;
  }

exit;

#=======================================================================#
# サブルーチン
#=======================================================================#

#================#
# 初期化
#================#

sub init_valiables{

	$vip_n			="11020609";
	$imgboard_ver		="2001101501";
	$EXTCFG{'ext_config_ver'}="100";
	$HTTP_USER_AGENT	=$ENV{'HTTP_USER_AGENT'};
	$REMOTE_HOST		=$ENV{'REMOTE_HOST'};
	$SERVER_NAME		=$ENV{'SERVER_NAME'};
	$HTTP_REFERER		=$ENV{'HTTP_REFERER'};

# iPod Touch
#$HTTP_USER_AGENT="Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A100a Safari/419.3";

	undef $tok2_cookie;

	# 2010.06 add FLVPlayer用に独自のCGI環境変数を作る
	undef %MYCGI_ENV; # 初期化
	# CGI本体のURL
	$MYCGI_ENV{'cgi_url'}='http://'."$ENV{'HTTP_HOST'}"."$ENV{'REQUEST_URI'}";
	# CGIの本体のあるディレクトリのURL
	$MYCGI_ENV{'cgi_base_url'}="$MYCGI_ENV{'cgi_url'}";
	$MYCGI_ENV{'cgi_base_url'}=~ s/^(.*)(\/)([^\/]*)$/$1$2/g;
#&error("MYCGI_ENV{'cgi_url'} $MYCGI_ENV{'cgi_url'} MYCGI_ENV{'cgi_base_url'} $MYCGI_ENV{'cgi_base_url'}");

	# 2012.09 iOS6以降検出
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

	if($HTTP_USER_AGENT=~ /iPhone|iPod|iPad|PSP|Android 1\.|Android 2\.1/i){
		$MYCGI_ENV{'flash_object_tag_support'}='false';
	}else{
		$MYCGI_ENV{'flash_object_tag_support'}='true';
	}

	# ボタンのサイズ
	$output_button_px="style=\"font-size: 16px\"";
	$output_button_space="";
	$output_link_space="";

	# スマフォ/タブレットでボタンを大型化する
	if($HTTP_USER_AGENT=~ /iPad|tab/i){
		$output_button_px="style=\"font-size: 18px\"";
#		$output_button_space="<BR>";
		$output_link_space="&nbsp&nbsp&nbsp";
	}elsif($HTTP_USER_AGENT=~ /ipod|iPhone|android/i){
		$output_button_px="style=\"font-size: 24px\"";
		$output_button_space="<BR>";
		$output_link_space="&nbsp&nbsp";
	}

	if(int($])<5){
		&error(" Configuration error. The Perl version $] specified for the path in the first line of the script is too old. imgboard1.22R5 or later requires Perl5 or higher due to the version of jcode.pl. Find a path with Perl5 or higher and change it to that, or get R5\(for Perl4 \) and jcode_sj.pl at imgboard.com. ");
	}

	&check_browser_type;	# ブラウザチェック
	&check_RH;		# Apache1.3.x対策
	&check_ISP;		# プロバイダをチェックして、アドバイスを出す
	&check_imode;		# iモードからのアクセスなら指定URLへ飛ばす

	$cgi_name=&get_script_name;
	#========= 以下はマイナーオプションです ( 0=no,1=yes)==========#

	# ブラックリスト関連の追加設定
	$no_disp_for_cracker	=0;	# リスト上のサイトには掲示板を見せることも禁止する。
	$use_ext_blacklist	=1;	# 外部にblacklist.txt,blkword.txt
					# があれば,そのリストをロードする

	# スパムリスト関連の追加設定
	$use_ext_spamlist	=1;	# 外部にspamlist.cgi,spamword.cgi
					# があれば,そのリストをロードする

	# ゲストパスワード機能（PPP対応-IP認証型）
	# 投稿者自身が記事を削除できる機能です。詳細はサポート掲示板を参照してください。
	#
	$use_guest_passwd	=1;	# ゲストパスワード機能を使用
	# （-1 削除キー式にする,0使用しない（この場合は管理者のみ削除可能）、1ゲストパスワードを使用する(強く推奨)）
	$guest_passwd		='guest';	# 記事削除時の ゲストパスワード(変更は必要ありません)
	# IPが完全一致しなくても、同じサブネットからのアクセスは同一人物とみなし、削除を許可する
	$gp_allow_subnet	=1;


	# その他
	$no_disp_RH_in_HTML_sorce=0;	# HTMLソースにリモホを表示しない
	# -1=常時IP表示,0=HTMLソースのみIP表示,1=IP完全非表示
	$auto_ip_if_danger_datatype=1;	# 危険なデータタイプの時は、投稿者のIPを自動表示する
	$use_ip_privacy_filter=1;	# プライバシー保護のためIPアドレスの一部を伏せ字に
	$use_sjis_header_for_Netscape4X ='0';# Netscape4.X文字化け対策(def=0)
	$force_www_server_os_to='';	 # 未使用パラメータ(指定しないこと) 

#------------------ 以下はプログラム -----------------------------	
	undef $call_from_imgboard_flag;
	$call_from_imgboard_flag=1;

	require "$imgsize_prog" if(-e "$imgsize_prog");

	if(($load_ext_config == 1)&&(-e "$ext_config_name")){
		require "$ext_config_name";
		if($EXTCFG{'ext_config_ver'} < 2001101500 ){
			&error(" External configuration file version $ext_config_name is too old to use. Please obtain the latest version or set it not to be loaded.");
		}
		if($imgboard_ver < $EXTCFG{'support_imgboard_ver'} ){
			&error(" This external configuration file (for $EXTCFG{'ext_config_ver'}-imgboard $EXTCFG{'support_imgboard_ver'} or later) is not available for this imgboard (version $imgboard_ver). Please obtain the latest version of the external configuration file or set it not to be loaded.");
		}


	}

&make_uniq_onetime_id;

#======================#
# SPAM対策用トークン
#======================#
# 2010.02 SPAM対策のため、掲示板固有のワンタイムIDを作成する
# 2010.04 softbankのスマートフォン対策でロジック変更

sub make_uniq_onetime_id{

	local($ttmp_uniq_char)="";

	# perl5のDigestやSHA256モジュールを使えないプロバイダが多いので、
	# 独自ロジックで類推しにくいHASH代用計算をすることにした

	if(-e "$img_dir/index.html"){
	 @UNQ_FILE_STAT=stat("$img_dir/index.html");	# 属性を調査
	 $tttmp_pick_file_size		=substr($UNQ_FILE_STAT[7],-1,1);		# ファイルサイズを取得
	 $tttmp_pick_file_lastupdate=substr($UNQ_FILE_STAT[9],-1,1);
	}else{
	 $tttmp_pick_file_size		=3;
	 $tttmp_pick_file_lastupdate=4;
	}

	$tmp_token_time= substr(time,-7,2); #27.7時間単位

	$tmp_alphabet_sn	="$ENV{'SCRIPT_FILENAME'}";
	$tmp_alphabet_sn	=~ s/[^a-zA-Z0-9]//g;

	$tmp_alphabet_sa	="$ENV{'SERVER_ADMIN'}";
	$tmp_alphabet_sa	=~ s/[^a-zA-Z0-9]//g;

	$tmp_alphabet_saddr ="$ENV{'SERVER_ADDR'}";
	$tmp_alphabet_saddr =~ s/[^a-zA-Z0-9]//g;
	
#$admin_passwd = 'biko';	

	# HTC disire対策でロジック変更(１文字長くしておく)
	$tttmp_pick_sa_base=substr($tmp_alphabet_saddr,-3,1)."$tttmp_pick_file_lastupdate".substr($admin_passwd,-1,1).substr($tmp_alphabet_sn,5,1).substr($tmp_alphabet_sa,5,1)."$tttmp_pick_file_lastupdate"."$tttmp_pick_file_lastupdate";

#&error("$tttmp_pick_sa_base  $tmp_alphabet_sn $tmp_alphabet_sa s $tttmp_pick_file_lastupdate");

	$tttmp_salt="$tttmp_pick_file_lastupdate"."$admin_passwd";# salt作成
	$tttmp_pick_sa		=  substr(time,-7,2)."$tttmp_pick_sa_base";
	$tttmp_pick_sa_old	= (substr(time,-7,2)-1)."$tttmp_pick_sa_base";

# token動作確認test用(100秒単位で無効に)
#	$tttmp_pick_sa		=  substr(time,-4,2)."$tttmp_pick_sa_base";
#	$tttmp_pick_sa_old	= (substr(time,-4,2)-1)."$tttmp_pick_sa_base";

	
	$uniq_token		=crypt($tttmp_pick_sa		,$tttmp_pick_sa);# HASH代用文字列作成
	$uniq_token_old	=crypt($tttmp_pick_sa_old	,$tttmp_pick_sa_old);# HASH代用文字列作成 27.7時間単位で一つ前

	# saltを切り落とす
	$uniq_token		=substr($uniq_token,2,11);
	$uniq_token_old	=substr($uniq_token_old,2,11);

	# URLと相性の悪い文字を除く
	$uniq_token 	=~ s/[^a-zA-Z0-9]//g;
	$uniq_token_old =~ s/[^a-zA-Z0-9]//g;

#&error("$uniq_token");	
#	$ttmp_uniq_char="$uniq_token - $uniq_token_old - salt $tttmp_salt - sa $tttmp_pick_sa - saold $tttmp_pick_sa_old - $ENV{'SERVER_ADDR'} "."$ENV{'REMOTE_ADDR'} "."$ENV{'SERVER_ADMIN'}"." $tttmp_pick_file_size $tttmp_pick_file_lastupdate";
#&error("ttmp_uniq_char $ttmp_uniq_char");

}

	# 2006.03 SPAM対策
	if($spam_keyword ne ""){
		$POSTADDP{'UPLOADFORM'}="$POSTADDP{'UPLOADFORM'}\n"."<INPUT TYPE=\"HIDDEN\" NAME=\"sf\" VALUE=\"$spam_keyword\">\n<INPUT TYPE=\"HIDDEN\" NAME=\"onetime_token\" VALUE=\"$uniq_token\">";
	}


# 2006.10.14 Bug fix
#	if($limit_bbs_spam_flag==1){
	if($filter_bbs_spam==1){
		if($CHECK{'email'}==1){
			&error(" Admin configuration error. If you have set Email Required, you will not be able to post if you use the SPAM setting to discard all posts with URL links or email addresses, no questions asked. Please review your settings. ");
		}
	}

	if(($jcode_name ne '')&&(-e "$jcode_name")){
	    require "$jcode_name";
	    eval &jcode'init('tokuho_check');
	    # 成功
	    if($@ eq ""){
		    $jcode_sj_version =&jcode'init('tokuho_check');
		    if($jcode_sj_version < 2001070701 ){
			&error(" 管理者設定のエラー。処理を中止しました。<BR>
			jcode_sj.plのバージョン $jcode_sj_version は古過ぎます。
			最新版をご利用ください。");
	    	    }
	    }else{
	    # 失敗
		&error(" 管理者設定のエラー。処理を中止しました。<BR>
			jcode_sj.plは古過ぎるか、あるいはマッチしていないタイプの物です。
			最新版をご利用ください。");
	    }
	}else{
	}

}

#================#
# 開店確認
#================#

sub check_open{
	&error("$oyasumi_message") if($bbs_open_flag !=1);
}

#=====================#
# 入力データを読む
#=====================#

sub read_input{

	# 変数の初期化
	local($name);
	undef $img_data_exists;
	undef @NEWFNAMES;
	undef $jcode_eval_check_flag;

	# リロード＆GETでかつ返信なしの場合は以下の処理をスキップ
	if($ENV{'CONTENT_LENGTH'}==0){	# リロード時 & GETの場合
		&read_cookie;		# クッキーのロード
		if($PM{'use_rep'}==1){	# 返信ありの場合
					# ウィンド描画のためにGET受け入れ
		}else{			# 返信なしの場合
#			return	if($form_disp_on_board==1);
		}
	}

	# データの取得＆転送データのサイズをチェック
    	$ENV{'REQUEST_METHOD'} =~ tr/a-z/A-Z/;

	if(($ENV{'SERVER_SOFTWARE'}=~ /BlackJumboDog/i)&&($allow_other_multimedia_data==1)){
	  # 自宅サーバは他人に迷惑をかけないので、規制を緩くする
	  if($max_upload_size > 218000){$max_upload_size='218000';}# 変更禁止
	}elsif(($ENV{'SERVER_SOFTWARE'}=~ /AnWeb/i)&&($allow_other_multimedia_data==1)){
	  # 自宅サーバは他人に迷惑をかけないので、規制を緩くする
	  if($max_upload_size > 218000){$max_upload_size='218000';}# 変更禁止
	}elsif(($ENV{'SERVER_SOFTWARE'}=~ /04WebServer/i)&&($allow_other_multimedia_data==1)){
	  # 自宅サーバは他人に迷惑をかけないので、規制を緩くする
	  if($max_upload_size > 218000){$max_upload_size='218000';}# 変更禁止
	}else{
	  if($max_upload_size > 118000){$max_upload_size='118000';}# 変更禁止
	}

		$max_content_length	=($max_upload_size + 1)*1000;
		$max_content_limit	="$max_upload_size";

	if($ENV{'REQUEST_METHOD'} eq "POST"){

		# OSの種別を判別
		$www_server_os =&check_www_server_os;

		if($www_server_os=~ /win/i){
			binmode(STDIN);
		}

		if($ENV{'CONTENT_LENGTH'} > 120000000){
		# Unixは正常。Win は下記メッセージを出さずに終了するようだ
			&error(" Data size is too large. Please keep it under $max_content_limit KB please. p");
			exit;
		}

		# 2000/02/02 変更
		read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});

		if($ENV{'CONTENT_LENGTH'} > $max_content_length){
			&error(" Data size is too large. Please keep it under $max_content_limit KB right?");
			exit;
		}

   	 }elsif($ENV{'REQUEST_METHOD'} eq 'GET'){
		$buffer = $ENV{'QUERY_STRING'};

		# XSS対策 2012.04.18
		# onClick等javascriptイベントを除去(クロスサイトスクリプティング対策)		
		$buffer =~ s/(onClick|onblur|onchange|onmouse|onError|onload|onfocus|onselect|onsubmit|onunload|onreset|onabort|ondblclick|onkey|ondragdrop)(\w{0,8})(\s*)(\=|%3d)/RemovebyImgboardSecurityCheck_JS/ig;
		$buffer =~ s/(<|%3C)/RemovebyImgboardSecurityCheck_3C/ig;
		$buffer =~ s/(>|%3E)/RemovebyImgboardSecurityCheck_3E/ig;

	 }else{
		return 0; 
	 }

	# 日付関連

	# 時差ー入力パラメータをチェック
	if(($gisa=~ /^(\d+)$/)&&($gisa != 0)){
		$gisa=$gisa;
	}else{
		$gisa=0;
	}

	($sec,$min,$hour,$mday,$mon,$year,$wday,$yday) = localtime(time + $gisa*60*60);

	$year += 1900;				# 2000年対策

	$month = $mon + 1;
	if ($month < 10) { $month = "0$month"; }
	if ($mday  < 10) { $mday  = "0$mday";  }
	if ($sec   < 10) { $sec =  "0$sec";    }
	if ($min   < 10) { $min =  "0$min";    }
	if ($hour  < 10) { $hour = "0$hour";   }

	$unq_id="$year"."$month"."$mday"."$hour"."$min"."$sec";

	# -----フォームのデコード処理------#

	# 非マルチパート時のフォーム処理
	# 削除,ページ変更時等
	if($ENV{'CONTENT_TYPE'} !~ /multipart\/form-data/){
    		@pairs = split(/&/,$buffer);
    		foreach $pair(@pairs){
    			($name,$value) = split(/=/,$pair);
    			$value =~ tr/+/ /;
    			$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
    			&jcode'convert(*value, 'sjis','','z');	# sjisに変換
    			
    			# 2011.12.15 XSS対策
				$value =~ s/(%3C|<)(\s*)script//ig;		# scriptタグ禁止
				$value =~ s/(%3C|<)(\s*)EMBED//ig;		# EMBEDタグ禁止
				$value =~ s/(%3C|<)(\s*)OBJECT//ig;		# OBJECTタグ禁止
				$value =~ s/(%3C|<)(\s*)iframe//ig;		# SCRIPTタグ禁止

				$value =~ s/(%3C|<)(\s*)/&lt;/ig;		# タグ禁止
				$value =~ s/(%3E|>)(\s*)/&gt;/ig;		# タグ禁止
				
    			$FORM{$name} = $value;
    		}

	# マルチパート時のフォーム処理
	# 記事投稿用のフォーム
	}else{
		# METHODのチェック	
		&error(" multipart\/form-dataMETHOD should be set to POST when using ") if($ENV{'REQUEST_METHOD'} ne "POST");

		# multipart/form-dataの場合の処理
		$buffer =~ /^(.+)\r\n/;
		$boundary = $1;
		@pairs = split(/$boundary/, $buffer);
		foreach $pair(@pairs){
			$check_count++;
                        $pair=~ s/\r\n$/\r\nD_End/;
			@vars = split(/\r\n/, $pair);
			$vars = @vars;

			#---サポート用----#
			if(($check_count=='7')&&($FORM{'email'} eq "mt1")){&error(" デバックモードall-$vars,vars0- $vars[0]<BR>,1-$vars[1]<BR>\n,2-$vars[2]<BR>\n,3-$vars[3]<BR>\n,4-$vars[4]<BR>\n,5-$vars[5]<BR>\n,6-$vars[6]\n<BR>,7-$vars[7]\n. <BR>SAL $vip_n<BR>,Perl ver $] <BR>@vars test ");}
			#-----------------#

			if(($vars > 4)&&($vars[1] =~ /name\=\"(.+)\"\;\sfilename\=\"(.+)\"/)){

				# ファイルアップロードの処理
				$name  = $1;
				$fname = $2;
				$content_type = $vars[2];

				# --- サポート用 2 ----#
				if($FORM{'email'} eq "mt2"){&error("デバックモードall-$vars,name $name fname $fname content_type $content_type ");}
				#-----------------#


                      		# 特例処理（マイムが不明な場合）

				if(($fname ne "")&&($content_type eq "")){

# 以下の３ケースが想定される．
# ケース１）Macユーザがファイル名に拡張子のないファイルをアップロード
# ケース２）Mac,Win,Unixユーザがブラウザの知らない(Plug-inのない)データをアップロード

# この場合はデータのヘッダ部分のテキスト解析からの自動判別を試みる（GIF,JPEG,PNG）．
# 失敗したら拡張子が存在するかどうかをチェック
# 存在したら後の拡張子による判断に任せる．
# 存在しない場合警告を出し終了．

					# データヘッダから画像の種類を自動判別
					if($vars[3] =~ /^GIF8/i){
						$check_m .=" ヘッダー分析の結果４はGIF <BR>";
						$content_type="image/gif";
					}elsif($vars[3] =~ /^(.+)JFIF/i){
						$check_m .=" ヘッダー分析の結果４はJPEG <BR>";
						$content_type="image/jpeg";
					}elsif($vars[3] =~ /^\x89PNG/i){
						$check_m .=" ヘッダー分析の結果４はPNG <BR>";
						$content_type="image/png";
					# 拡張子らしき物がついている場合
					}elsif($fname=~ /\.(\w){1,4}$/){
						$content_type="unknown";#後の拡張子による判断に任せる
					}else{
						if($HTTP_USER_AGENT =~ /MAC/i){
							&error("Upload error. Attribute of upload data cannot be determined. <BR>\nIf you are a Mac user, the filename you are uploading may not have an <BR>\nextension (such as gif.jpeg.png). <BR>\nPlease add an appropriate extension to the file name.<BR><!--fname,$fname,Mime_types,$content_types,Mes.$check_m-->");	
						}else{
							&error(" Upload error. Attribute of upload data cannot be determined. <BR>\nThe file name may not have an <BR>\nextension (such as gif.jpeg). <BR>\nPlease add an appropriate extension to the file name.<BR><!--fname,$fname,Mime_types,$content_types,Mes.$check_m-->");	
						}
					}

					# マイムタイプより、拡張子を作る
					$ext = &content_type_check($content_type);

					# 画像データのみを抽出
					# ($vars[3]に実体,4=D_End $vars 5)
					foreach($i=3; $i<$vars;$i++){
						if($data eq ''){
							$data = $vars[$i];
						}else{
							$data .= "\r\n$vars[$i]";
						}
					}
					$data=~ s/\r\nD_End$//;
				# 通常のアップロードの場合（マイムデータが通知された場合）
				}else{


                         	       # マイムタイプより、拡張子を作る
					$ext = &content_type_check("$content_type");

					# 画像データのみを抽出
                        	        #($vars[4]に実体,5=D_End,$vars 6)
					foreach($i=4; $i<$vars; $i++){
						if($data eq ''){
							$data = $vars[$i];
						}else{
							$data .= "\r\n$vars[$i]";
						}
					}
					$data=~ s/\r\nD_End$//;
                        	}

				$img_dir = '.' if($img_dir eq '');

				# 画像保存ディレクトリの確認
				if($img_dir=~ /^http\:\/\//i){
					&error(" img_dir is specified incorrectly. <BR> Directories and URLs are different concepts. A directory specification never begins with http. <BR> Please change the settings.");
				}
				if(-d "$img_dir"){
				}else{
					&error(" The image data saving directory \"$img_dir\" cannot be found. <BR>The specified directory \"$img_dir\" may not exist.<BR>Please check the path setting for the directory for saving images. ");
				}

				# パスを消して、ファイル名のみを残す。
				#95/NTからのアップロードに対応
				$fname=~ s/^(.*)\\//;
				# UNIX からのアップロードに対応
				$fname=~ s/^(.*)\///;

				#&error("ファイル名 $fname");

				$use_orig_name=0;		# オリジナルファイル名保存機能削除			
								# 今後は imgboard2015でのみサポート
				if($use_orig_name==1){				
				#	&use_orig_name;
				}else{
				# 時刻でファイル名を付けるオプション。
				# ファイル名のコンフリクトを防ぐ

					$date_count="19981204201523";
					$date_count="$year"."$month"."$mday"."$hour"."$min"."$sec";


					# ファイル名が重なる場合変更する
					if( -e "$img_dir/img$date_count\.$ext"){
						$date_count++;
						$unq_id++;
					}elsif( -e "$img_dir/img$date_count\.$ext"){
						$date_count++;
						$unq_id++;
					}elsif( -e "$img_dir/img$date_count\.$ext"){
						&error(" An error occurred during the file naming process. Time-based mode ");
					}

					$new_fname = "img$date_count\.$ext";
				}

				# 複数アップロード対応用
				push(@NEWFNAMES, $new_fname);

				# 画像サイズ専用リミッタによるチェック
				if($max_upload_img_size ne ""){
				
					# 2011.12 Androidの場合、大きな画像も許可する
					if($HTTP_USER_AGENT=~ /Android/i){
				 	 if($max_upload_Android_img_size > $max_upload_img_size){
				 		$max_upload_img_size=$max_upload_Android_img_size;
				 	 }
					}
				
				 if($ENV{'CONTENT_LENGTH'} > $max_upload_img_size*1024){
				  if($new_fname=~ /\.gif$|\.jpe?g$|\.png$|\.bmp$/i){
					&error(" The data is too large. Please set the image size to $max_upload_img_size KB or less before posting. <BR><BR>Recommended image reduction tool<BR> For Windows: <a href=http://www.vector.co.jp/soft/win95/art/se153674.html target=_blank>Reduction tool</ a><BR> For Mac OS : <a href=http://itunes.apple.com/jp/app/resizeit/id416280139?mt=12 target=_blank>ResizeIt</a> <BR> For Android : < a href=https://play.google.com/store/search?q=Image+Shrink+Lite&c=apps target=_blank>Image Shrink Lite</a> Please change the image quality from FINE to normal and try again<BR>");
					exit;
				  }
				 }
				}

				open(OUT, ">$img_dir/$new_fname")|| &error("An error occurred while saving image data to $img_dir. <BR>You may not have write permission in the specified directory \"$img_dir\".<BR>Please check the permission settings for the directory.");
				# IIS,PWS(NT/95)対策
				if($www_server_os=~ /win/i){
					binmode(OUT);
				}
				  eval "flock(OUT,2);" if($PM{'flock'} == 1 );
				  print OUT $data;
				  eval "flock(OUT,8);" if($PM{'flock'} == 1 );
				close(OUT);

				# テンポラリアップロードデータの存在確認フラグ
				# 後処理で,登録中断エラー発生時に画像ファイルを削除するために使用。
				# 削除はsub errorルーチン内で行う。
				$img_data_exists=1;
	
			}elsif(($vars > 3) && ($vars[1] =~ /name\=\"(\S+)\"/)){
                                # 画像データ以外のフォームの処理
                                #&error("varsデータ<BR>$vars $1-$vars[3] test");	
				# その他のフォームデータの処理
				$name =$1;
				$value = "$vars[3]";

				# テキストエリアに関する処理
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

				# sjisに変換 (imgboard1.22 Rev.3)
				# jcode_sj.pl関連の設定ミスをトラップして検出
				# (一度成功すればスキップして高速化)
				if($jcode_eval_check_flag != '1'){
					eval "&jcode'convert(*value, 'sjis','','z');";
					if($@ eq ""){
					    $jcode_eval_check_flag=1;
				 	    # 成功
					}else{
				 	    # 失敗
	    					&error(" CGI setting error Failed to load the Japanese library "$jcode_name" for some reason. <BR> The name such as jcode_sj.pl is not specified correctly, or the corresponding file does not exist in the specified path "$jcode_name", or the permission seems to be incorrect. ");
					}
		    		}else{
					&jcode'convert(*value, 'sjis','','z');
		    		}
				$FORM{$name} = $value;		# valueを返す

			}
		}
	}
}

#=========================#
# 記事データの追加
#=========================#

sub post_data{

	local($tmp_file)	= $_[0];# 処理するログファイル名

	undef @HEAD_MESSAGE;
	undef @MESSAGE;
	undef @NEW_MESSAGE;
	local($old_seq_no,$new_seq_no,$tmp_mes_line,$mes_counter);
	local($img_data_size_num);
	local($sage_flag);

  	if($ENV{'REQUEST_METHOD'} ne 'POST'){
		&error(" Security warning <BR> Article submission by GET is NG ");
	}

	&form_check;

	if($error_message ne ''){
		&rm_tmp_uploaded_files;
		&set_cookies;		# クッキーをセット(120Rev5以降)
		&error($error_message);
		exit;
	}

	# 記事の日付表示（変更可能)
	$date_data = "\[$year/$month/$mday,$hour:$min:$sec\]";

        if(($img_location ne '')&&($imgtitle eq '')){
	# タイトルがない場合はファイル名がタイトル
		$imgtitle="$img_location";
	}
	# 投稿画像の容量を計算
	if($img_location ne ''){
		$content_length="$ENV{'CONTENT_LENGTH'}";
		$content_length="$content_length"-800;
		$content_length_kb=int($content_length/1024);

		# R7 new Webでゲットしたファイルにサイズに差換え
		if($web_get_file_size > 0){
			$content_length_kb=int($web_get_file_size*10/1024);
			$content_length_kb=($content_length_kb / 10);
		}

		if(("$content_length" > 0)&&("$content_length_kb"==0)){
	        	$img_data_size=1;
		}else{
        		$img_data_size="$content_length_kb";
		}
		if($FORM{'amode'} eq "post_webparts"){
		 if($img_data_size > 52){
			&error(" Error。 Please keep part images under 50KB. <BR>	");	
		 }
		}
		$img_data_size_num="$img_data_size";
		$img_data_size="($img_data_size KB)";

#		# 原画のダイエット機能 2005.09
#		if(($content_length_kb > 30)&&($tcontent_length_diet > 0)){
#  		  $content_length_diet_kb=int($tcontent_length_diet/1024);
#		  $img_data_size="(Diet $img_data_size_num KB→$content_length_diet_kb KB)";
#		}
	}

	# imgsizeのバージョンをチェック
	if($imgsize_lib_flag ==1){
		unless($imgsize_version >=20010301){
			&error(" 
Error in admin settings. Processing aborted. <BR>
The imgsize.pl version $imgsize_version is too old. Please use the latest version.");
		}
	}

	# 投稿画像のプロパティを取得
	&check_uploaded_img_property;
	sub check_uploaded_img_property{
	if((-e "$img_location")&&($imgsize_lib_flag== 1 )){	
		&imgsize("$img_location");
		if(($IMGSIZE{'result'} ==1)&&($img_data_exists==1)){
			$img_type	="$IMGSIZE{'type'}";
			$img_width	="$IMGSIZE{'width'}";
			$img_height	="$IMGSIZE{'height'}";
			$img_hw_racio	="$IMGSIZE{'hw_racio'}";
		}
		undef %IMGSIZE;
	}
	}

	# セパレータとして問題あるものを、事前に置換
	$subject=&Enc_EQ("$subject");

	undef $tmp_data;

	foreach $p_key(keys %FORM){
		if($p_key=~ /opt_data_(.+)/){
			$tmp_data=&Enc_EQ($FORM{$p_key});
			# 書き出しデータは従来互換が必要
			$opt_data.="opt_data_"."$1"."\="."$tmp_data"."\;";
			undef $tmp_data;
		}elsif($p_key=~ /^opt(.{1,2})$/){
			$tmp_data=&Enc_EQ($FORM{$p_key});
			$opt_data.="opt_data_"."$1"."\="."$tmp_data"."\;";
			undef $tmp_data;
		}
	}

	if(-e "$tmp_file"){
	}else{		# コメント保存ファイルがない場合,自動作成を試みる
		open(NEWFILE,">$tmp_file")||&error("Setting error. The data save file \$tmp_file\" was not found. An attempt was made to create it automatically, but it failed. Processing was interrupted.");
		close(NEWFILE);
 	}

	# 準備完了

	# メッセージを読み込む
	open(IN, "$tmp_file")|| &error("Setting error. Cannot find the data save file \"$tmp_file\". Processing was interrupted.");

	   eval "flock(IN,1);" if($PM{'flock'} == 1 );
	   while(<IN>){

		# HEADER保存 (将来への拡張もここで対応)
		if($_ =~ /^\#?\,param_/i){

			# (#でコメントアウトしたものを含む)
			if($_ =~ /^\,param_seq_no(\s*)=(\s*)(\d+)(\s*)/i){
				# 連番を取得する
				$old_seq_no="$3";
			}elsif($_ =~ /^\,param_last_backup_date(\s*)=(\s*)(\d+)(\s*)/i){
				# 最終更新日を取得する
				$HEAD_MESSAGE{'last_backup_date'}="$3";
			}elsif($_ =~ /^\,param_last_bloods(\s*)=(\s*)([^\;]*)(\;+)(\s*)/i){
				# 最新の記事の親を取得する
				$HEAD_MESSAGE{'last_bloods'}="$3";
				$HEAD_MESSAGE{'last_bloods'}=&Dec_EQ("$HEAD_MESSAGE{'last_bloods'}");
			}else{
				push(@HEAD_MESSAGE, $_);
			}

		}

		# 記事をバッファに入れる
		if($_ =~ /^([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]*)\t([^\t]*)/){
			$tmp_mes_line="$_";
			chop($tmp_mes_line);
			push(@MESSAGE, $tmp_mes_line);
			$all_message++;
		}
	   }

	eval "flock(IN,8);" if($PM{'flock'} == 1 );
	close(IN);


	# 連番処理
	if($old_seq_no eq ""){# ない場合は作る
		$old_seq_no='0';
	}
	$new_seq_no=$old_seq_no+1;

	# WebPartsがオーバーしないように警告する
	if($limit_wp_max_message ne ""){
	  if(($limit_wp_max_message-1) < $all_message){
	    &error("error. In imgboard, web parts can only be saved up to $limit_wp_max_message. <P>If you want to save more parts and icons, please use sister script imgboard2010.");
	  }
	}

        # 暗号化
	if(($rmkey ne "no_key")&&($rmkey ne "")){
		$rmkey		= &make_pass("$rmkey");
	}

	# SNLとして存在するデータのリストを作る
	foreach (@SNL_MADE_DATA){
#		$existing_snl_type_list.="$_"."\/";
	}

	# 輸入URLでタブと;をエスケープ
	$img_import_url=~ s/\t//g;
	$img_import_url=~ s/\;//g;
	$img_import_url=~ s/\s+$//g;

	# sage機能
	if(($PM{'use_sage'} == 1)&&($tt_email=~ /^sage$/i)){
		$tt_email="";
		$sage_flag=1;
	}

	# 新しいメッセージを作る（imgboard1.22新形式）
	$new_message = "$subject\t$name\t$email\t$date_data\t$body<\!--opt\:$opt_data-->\t$img_location\t$imgtitle<\!--dsize=$img_data_size;type=$img_type;width=$img_width;height=$img_height;hw_racio=$img_hw_racio;size=$img_data_size_num;-->\t$new_seq_no\t$FORM{'blood'}\t$rmkey\t$unq_id\t";


	# レスの付いた記事を上へ持って行くために、親スレッドリストへ追加する
	# 2004.12 sage機能を追加
	if(($FORM{'sage'} == "1")||($sage_flag == 1 )){
	  # リストに記録しない
	}else{
	  &update_bloods_list;
	}

	# 記事データを追加する
	if($FORM{'parent'} eq ""){
	# 親記事の場合
		unshift(@MESSAGE, $new_message);
		$all_message++;	# 記事数は一つ増


	}else{
	# 子記事の場合
		# 記事データを探索する

		$mes_counter=1;
		$last_child_number=0;

		foreach(@MESSAGE){
			if($_ =~ /$FORM{'blood'}/){
				$last_child_number=$mes_counter;
			}
			$mes_counter++;
		}

		# 記事データを追加する
		$mes_counter=1;

		foreach(@MESSAGE){
			push(@NEW_MESSAGE, $_);
			if($mes_counter==$last_child_number){
				push(@NEW_MESSAGE, $new_message);
				$all_message++;	# 記事数は一つ増
			}
			$mes_counter++;
		}
		@MESSAGE=@NEW_MESSAGE;

	}

	# 古い画像を削除

	if($all_message > $max_message){
		for($i=$max_message; $i<$all_message; $i++){
			if($MESSAGE[$i] =~ /^([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]*)\t([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)/){

				local($remove_file) 		= $6;
				local($remove_imgtitle) 	= $7;
				local($tmp_unq_id)  		= $11;

				if($remove_file ne '' && -e $remove_file){
					unlink($remove_file);
					# メタファイルも削除する
					&rm_meta_file("$remove_file");

					# 携帯用ファイルも削除する
					if($remove_file=~ /\.(jpe?g|gif|png|bmp|mng)$/i){
					  # SNLのパスを調べる
					  if($remove_imgtitle ne ''){
					    &parse_img_param($remove_imgtitle);
					  }
					  &rm_snl_file("$tmp_unq_id","$IMG_PARAMETERS{'snl_dir'}","$IMG_PARAMETERS{'exist_snl_type'}");
					}


				}
			}

		}
	}

	# 新しいファイルとして出力
	if($all_message > $max_message){
		$repost_message = $max_message;
	}else{
		$repost_message = $all_message;
	}

	if($PM{'make_backup_file'}== 1 ){
 	 &make_backup_file; # バックアップファイル自動作成
	}

	# 書き出し処理
	open(OUT, "> $tmp_file")|| &check_file_open_error("$tmp_file");
	eval "flock(OUT,2);" if($PM{'flock'} == 1 );

		$HEAD_MESSAGE{'last_bloods'}=&Enc_EQ("$HEAD_MESSAGE{'last_bloods'}");

		# HEAD部分
		print OUT "\,param_seq_no=$new_seq_no\n";
		print OUT "\,param_last_backup_date=$HEAD_MESSAGE{'last_backup_date'};\n";
		print OUT "\,param_last_bloods=$HEAD_MESSAGE{'last_bloods'};\n";
		foreach(@HEAD_MESSAGE){
			print OUT "$_"; 
		}

		# 記事部分
		for($i=0; $i<$repost_message; $i++){
			print OUT "$MESSAGE[$i]\n";
		}


	eval "flock(OUT,8);" if($PM{'flock'} == 1 );
	close(OUT);
}

sub check_file_open_error{

  local($tmp_ffile)= $_[0];	# メッセージを引数として取得
  unless(-e "$tmp_ffile"){
	&error(" Configuration error. Could not write data to the data save file \"$tmp_ffile\". \The reason is that the file named "$tmp_ffile\" could not be found in the correct location. Please recheck the path setting. The submission process has been aborted.");
  }

  unless(-w "$tmp_ffile"){
	&error(" Configuration error. Could not write data to the data save file \"$tmp_ffile\". This is because there is no permission to write to $tmp_ffile. Please recheck the permission settings. The submission process has been aborted.");
  }
  if($ENV{'OS'}=~ /Windows_NT/i){
	&error(" Configuration error. If you are using the NTFS file system with IIS, please recheck your directory permission settings. The submission process has been aborted.");
  }
  &error(" Configuration error. Could not write data to the data storage file \"$tmp_ffile\". Please recheck your permission settings. The submission process has been aborted.");
}
#
# 最近の記事とその血統(スレッド)を記憶するサブサブルーチン
# imgboardR6のログにおいては１５記事分の記事ＩＤと
# 親の血統(スレッド)をパラメータとして覚えておくことにする。
#
sub update_bloods_list{

	local ($b_new_list);

#	return if($HEAD_MESSAGE{'last_bloods'} eq "");

	# 親記事追加の場合,親ー親で追加する
	if($FORM{'parent'} eq ""){	
		  return if($unq_id eq "");
		  $b_new_list="$unq_id-$unq_id"."\,"."$HEAD_MESSAGE{'last_bloods'}";
	}else{ 			
	# 子記事の場合、子ー親で追加する
	  return if($unq_id eq "");
	  return if($FORM{'blood'} eq "");
	  $b_new_list="$unq_id-$FORM{'blood'}"."\,"."$HEAD_MESSAGE{'last_bloods'}";
	}

	# １５以上になれば、１６以降は捨てる
	if($b_new_list=~ /^(\,*)([\d|\-]*)\,([\d|\-]*)\,([\d|\-]*)\,([\d|\-]*)\,([\d|\-]*)\,([\d|\-]*)\,([\d|\-]*)\,([\d|\-]*)\,([\d|\-]*)\,([\d|\-]*)\,([\d|\-]*)\,([\d|\-]*)\,([\d|\-]*)\,([\d|\-]*)\,([\d|\-]*)(.*)/){
		$b_new_list="$2"."\,"."$3"."\,"."$4"."\,"."$5"."\,"."$6"."\,"."$7"."\,"."$8"."\,"."$9"."\,"."$10"."\,"."$11"."\,"."$12"."\,"."$13"."\,"."$14"."\,"."$15"."\,"."$16"."\,";
	}

	$HEAD_MESSAGE{'last_bloods'}=$b_new_list;	
}
#
#
#===================================#
#  自動バックアップ作成処理(R6 new)
#===================================#
# 2001.07(ver.0.7)
# 万一のサーバのファイル出力中ダウンや投稿によるログ消失事故に
# 備えて、$PM{'backup_day_interval'}で指定された間隔日でfile.datの
# 自動バックアップを作る機能を追加する。
#
# 2001.07 空ファイルのバックアップによるファイル消去を防止
sub make_backup_file{

# sub post_data内で呼ばれる
# $HEAD_MESSAGE{'last_backup_date'}に最終バックアップ日時が
# unq_id と同じ形式で入っている。
# $PM{'backup_day_interval'}  でバックアップ間隔を設定し
# $PM{'backup_file_name'} にバックアップファイル名を指定し、作っておくこと

	local($do_backup_flag);
	local($today_day_count);
	local($tmp_day_count);

	# 設定されてないときは処理しない（互換性）
	if(($PM{'backup_day_interval'} eq "")||($PM{'backup_file_name'} eq "")){
	  return;
	}

	# 記事が5件以下の場合は、処理しない
	#（空ファイルのバックアップによる、バックアップファイル消滅を防ぐ）
	if($all_message < 6 ){
	  return;
	}


	# 初回用
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

	# このフラグが1ならバックアップを作る
	if($do_backup_flag ==1){
#&error("$unq_id-$HEAD_MESSAGE{'last_backup_date'}");
		if(-e "$PM{'backup_file_name'}"){
		   $HEAD_MESSAGE{'last_backup_date'}=$unq_id;# 最終バックアップ日を更新

#		   &write_file_data("$PM{'backup_file_name'}");

# 上のsub write_file_dataの代用（R5.2用の互換部分）================
	# 書き出し処理
	open(OUT, "> $PM{'backup_file_name'}")|| &check_file_open_error("$PM{'backup_file_name'}");
	eval "flock(OUT,2);" if($PM{'flock'} == 1 );

		$HEAD_MESSAGE{'last_bloods'}=&Enc_EQ("$HEAD_MESSAGE{'last_bloods'}");

		# HEAD部分
		print OUT "\,param_seq_no=$new_seq_no\n";
		print OUT "\,param_last_backup_date=$HEAD_MESSAGE{'last_backup_date'};\n";
		print OUT "\,param_last_bloods=$HEAD_MESSAGE{'last_bloods'};\n";
		foreach(@HEAD_MESSAGE){
			print OUT "$_"; 
		}

		# 記事部分
		for($i=0; $i<$repost_message; $i++){
			print OUT "$MESSAGE[$i]\n";
		}


	eval "flock(OUT,8);" if($PM{'flock'} == 1 );
	close(OUT);
# ==========================================================
		}else{
	   	&error("Configuration error. Post processing was interrupted. Data could not be written to the article backup data storage file \"$PM{'backup_file_name'}\". <BR>The file named \"$PM{'backup_file_name'}\" was not found in the correct location. If you haven't created the file yet, copy $PM{'file'}, name it $PM{'backup_file_name'}, put it in the same directory, and set the permissions to 606, etc. If you put it, but you get this error again, please check the path settings again.");
		}
	}
}
#
#=================================#
#  記事データの削除 (メイン部)
#=================================#
#
sub remove_data{

	local($tmp_file)	= $_[0];# 処理するログファイル名

	@remove_list=@_;# 引数 削除リスト(新モード 今は未使用)
	$tmpnum=0;
	local($tmp_blood_name)=0;
	local($killed_blood_name);# 消された親記事の血統を一時記憶
	undef @HEAD_MESSAGE;

	# ■セキュリティチェック
 	if($ENV{'REQUEST_METHOD'} eq 'GET'){
	  &error("
error. To prevent tampering, it is designed so that it cannot be deleted with the GET method.");
	}

	# ■複数の削除指定を受け取り、配列にする
	# rmid旧連番S新固有IDをチェックボックスからもらう
	# R4形式を@old_remove_list R6形式を@remove_listへ入れること

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

	$remove_article_number= @remove_list;	# 削除予定数

	# データを読み込みながら、削除するものはスキップし、最後に書き出す。
	open(IN, "$tmp_file")|| &error(" Setting error. Cannot find file "$tmp_file\" for data storage. The process was aborted.");
	eval "flock(IN,1);" if($PM{'flock'} == 1 );
	while(<IN>){

		if($_ =~ /^\,param_last_bloods(\s*)=(\s*)([^\;]*)(\;+)(\s*)/i){
				# 最新スレッドリストを取得する
				$HEAD_MESSAGE{'last_bloods'}="$3";
				$HEAD_MESSAGE{'last_bloods'}=&Dec_EQ("$HEAD_MESSAGE{'last_bloods'}");
		}elsif($_ =~ /^\#?\,param_/i){
			# HEADERを保存する(#でコメントアウトしたものを含む)
			push(@HEAD_MESSAGE, $_);
			next;
		}

		if($_ =~ /^([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]*)\t([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)/){


			$tmpnum++;
			undef @LDATA;

			$tmpdata 	= $_;	# 全体データを保存
			chop($tmpdata);		# 改行コードを除く
			@LDATA 	= split(/\t/,"$_");	# 切断して配列に入れる
			$tmp_body	= $LDATA[4];	# check_guest_passwdへ渡す
			$tmpimg  	= $LDATA[5];	# 画像
			$tmp_imgtitle 	= $LDATA[6];
			$tmp_seq_no  	= $LDATA[7];	# 連番
			$tmp_blood_name	= $LDATA[8];	# 親の血統ID(子供のみ持つ)
			$tmp_rmkey	= $LDATA[9];	# 削除キー
			$tmp_unq_id	= $LDATA[10];	# 固有ID(時刻ベース)

			$flag_remove	= 0;
			undef $host_flag;
			undef $allow_remove_flag;

			# 親が消えた場合は子記事は問答無用で全部消す
			if($killed_blood_name ne ""){
				if($killed_blood_name eq "$tmp_blood_name"){
				# 正規に消えた親と血統が一致した場合、子も消す
				# （@TMPMESSAGEへ保存しないで次のループへ行く）

				  # 子記事の画像データを消す
				  if($tmpimg ne ""){ # 子記事に添付画像があれば
				    # 画像ファイルを削除する
				    if(-e $tmpimg){
					unlink($tmpimg);
					# メタファイルも削除する
					&rm_meta_file("$tmpimg");

					# 携帯用ファイルも削除する
					if($tmpimg=~ /\.(jpe?g|gif|png|bmp|mng)$/i){
					  # SNLのパスを調べる
					  if($tmp_imgtitle ne ''){
					    &parse_img_param($tmp_imgtitle);
					  }
					  &rm_snl_file("$tmp_unq_id","$IMG_PARAMETERS{'snl_dir'}","$IMG_PARAMETERS{'exist_snl_type'}");
					}

				    }
				  }
				# 記事が削除されたらスレッドリストから削除する
				  $HEAD_MESSAGE{'last_bloods'}=~ s/$tmp_unq_id\-(\d+)\,//gi;	

				  # 親なしの子記事の削除に成功
				  next;
				}
			}

			undef @do_remove_list; # 初期化する

			# ここで新旧の指定の違いを吸収する
			if($tmp_unq_id ne ""){	
			# R6形式のログの場合
			# 固有IDで消す(より安全)
				$tmp_rm_num="$tmp_unq_id";
				@do_remove_list=@remove_list;
			}else{
			# R4以前の旧形式のログの場合
			# ページ中の連番で消す
				$tmp_rm_num="$tmpnum";
				@do_remove_list=@old_remove_list;
			}

			# この行が削除リストにあるか検索
			foreach $tmp_list(@do_remove_list){

				if($tmp_rm_num == $tmp_list){

				  if($remove_mode eq "guest"){
				    # ゲストパスワードをチェック
					&check_guest_passwd;
				  }elsif($remove_mode eq "rmkey"){
				    # 削除キーをチェック
					&check_rmkey("$tmp_rmkey");
				  }else{
					$allow_remove_flag=1;
				  }

				  if($allow_remove_flag ==1){

					$flag_remove = 1;
					# 子記事に添付画像があれば
					if($tmpimg ne ""){ 
					  # 画像ファイルを削除
					  if(-e $tmpimg){
						unlink($tmpimg);
						# メタファイルも削除する
						&rm_meta_file("$tmpimg");

						# 携帯用ファイルも削除する
						if($tmpimg=~ /\.(jpe?g|gif|png|bmp|mng)$/i){
						  # SNLのパスを調べる
						  if($tmp_imgtitle ne ''){
						    &parse_img_param($tmp_imgtitle);
						  }
						  &rm_snl_file("$tmp_unq_id","$IMG_PARAMETERS{'snl_dir'}","$IMG_PARAMETERS{'exist_snl_type'}");
						}
					  }
					}
				  }
				}
			}
			# 結果の処理
			if($flag_remove == 0){
				# 削除に失敗したときは、バッファに入れて保存、記事を残す
				push(@TMPMESSAGE, $tmpdata);
			}else{
				# 削除に成功

				# 記事が削除されたらスレッドリストから削除する
				$HEAD_MESSAGE{'last_bloods'}=~ s/$tmp_unq_id\-(\d+)\,//gi;	

				if($tmp_blood_name eq ""){ # 親の場合
			# 親だった場合は、その血統を記憶しておく
			# 消された親の血統を持つ子は後のループで全部消える
					$killed_blood_name="$tmp_unq_id";
				}else{ # 子の場合
			# 子記事単独消去（親は残る）の場合、ここを通る
			# 特になにもしない
					$killed_blood_name="";
				}
			}
		} #End of if
	} #End of While
	eval "flock(IN,8);" if($PM{'flock'} == 1 );
	close(IN);


	# データを書き込む
	open(OUT, "> $tmp_file")|| &error("設定エラー．テキストデータ保存用ファイル\"$tmp_file\"にデータを書込むことができません．<BR>おそらくファイルに対して書込み許可がないためだと思われます．処理は中断されました．");
	eval "flock(OUT,2);" if($PM{'flock'} == 1 );

	$HEAD_MESSAGE{'last_bloods'}=&Enc_EQ("$HEAD_MESSAGE{'last_bloods'}");
	print OUT "\,param_last_bloods=$HEAD_MESSAGE{'last_bloods'};\n";

	foreach(@HEAD_MESSAGE){		# HEAD部分
		print OUT "$_"; 
	}
	foreach(@TMPMESSAGE){		# 記事部分
		print OUT "$_\n"; 
	}
	eval "flock(OUT,8);" if($PM{'flock'} == 1 );
	close(OUT);

}
#
#====================================#
# 親スレッド新着順UIDリストを取得する
#====================================#
# $HEAD_MESSAGE{'last_bloods'}を入力として
# @NEW_BLOODS として親スレッド新着順UIDリストを出す
# @RECENT_MESSAGE_UID として最近の記事の新着順UIDリストを出す
#（@RECENT_MESSAGE_UIDは副産物。今は(new)表示に使っている）
sub output_new_bloods_list{

	undef @NEW_BLOODS;
	undef @RECENT_MESSAGE_UID;

	local (@SEP_FAMILY);
	local ($b_child,$b_parent,$already_find_flag);

	return if($HEAD_MESSAGE{'last_bloods'} eq "");

	# 子（親）ー親のペアに分解する
	@SEP_FAMILY=split(/\,/,$HEAD_MESSAGE{'last_bloods'});

	for($numb=0;$numb < scalar(@SEP_FAMILY) ;$numb++){
	  ($b_child,$b_parent)=split(/\-/,$SEP_FAMILY[$numb]);
	  if($b_parent ne ""){
		$already_find_flag=0;
		# 既に親リストにあれば追加しない
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

#==================================================#
#  記事データの削除 (ゲストパスワードチェック部)
#==================================================#
sub check_guest_passwd{

# ゲストパスワード機能を有効にすると,投稿者 ,削除者 のIPが一致する場合
# ゲストパスワードで記事の削除ができる。
# チェックlを行い,条件を満たせば$allow_remove_flag=1となる。

	# 投稿者のホスト名を取得
	if($tmp_body=~ /user：\s([^>]*)(\s*)--/){
		$tmp_user_IP="$1";
		$tmp_user_IP=&tiny_decode("$tmp_user_IP"); #2002.02

		#PPP&DHCP対策
		# リモートホストが数字のみの場合
		if($tmp_user_IP=~ /^(\d+)\.(\d+)\.(\d+)\.(\d+)$/){
			#$gp_allow_subnet=1にすると,完全一致しなくても
			# 同一サブネットなら削除できる。 (PPP,DHCP対策)
			if($gp_allow_subnet==1){
				$kkk=" 部分一致 ";
				$tmp_user_IP="$1.$2.$3";
			}else{
				$kkk=" 完全一致 ";
				$tmp_user_IP="$1.$2.$3.$4";
			}
			$host_flag=1;
		# リモートホストがホスト名の場合
		}elsif($tmp_user_IP=~ /(\w+)\.(\w+)$/){
			@DOMAINS = split(/\./,$tmp_user_IP);	# ブロックに分割
			$block_number= @DOMAINS;		# ブロック数を取得
			if($block_number ==0){$block_number=20; }
				undef $tmp_user_IP;
			if($gp_allow_subnet == 0 ){
				$kkk=" 完全一致 ";
				$bc_start=0;
				$tmp_user_IP=$DOMAINS[$bc_start];
			}else{
				$kkk=" 部分一致 ";
				$bc_start=1;
				$tmp_user_IP="."."$DOMAINS[$bc_start]";
			}
			for($i="$bc_start"+1; $i< $block_number;$i++){
				$tmp_user_IP .= "."."$DOMAINS[$i]";
			}
			$host_flag=1;
		}elsif($tmp_user_IP=~ /^(\w+)$/){
			$tmp_user_IP="$1";
			$host_flag=1;
		}
			$host_flag=1;
	}else{
	   	$tmp_user_IP="No IP info";
		$host_flag=0;
	}
	# 記事登録者と guest削除者のREMOTE_HOSTが一致すると削除できる
	$tmp_user_IP	=~ s/\./\\./g;
	if(($host_flag==1)&&($REMOTE_HOST=~ /$tmp_user_IP/)){
		$allow_remove_flag=1;
	}else{
		$skipped_guest_remove++;	# ゲスト権限で削除失敗した記事の数
		if($remove_article_number=='1'){
			&error(" ゲストパスワードによる削除は,投稿者 ,削除者 のIPが $kkk する場合のみ有効です<!-- b $bc_start \n $block_number \n P-IP $tmp_user_IP \n RH- $REMOTE_HOST-->");
		# すべての削除指定がゲスト権限で削除できないものだった場合のみ,エラーを出す
		# 削除可能,不可能なものがどちらもある場合はエラーを出さないで,処理を最後まで進める
		}elsif($remove_article_number == "$skipped_guest_remove"){
			&error(" ゲストパスワードによる削除は,投稿者 ,削除者 のIPが $kkk する場合のみ有効です<!-- b $bc_start \n $block_number \n P-IP $tmp_user_IP \n RH- $REMOTE_HOST-->");
		}
	}
}

#==================================================#
#  記事データの削除 (削除キー部)
#==================================================#
# 2001.02(暗号化対応) 
sub check_rmkey{

# 削除キー機能を有効にすると,削除キーが一致する場合、記事の削除ができる。
# ゲストパスワードとの同時使用はできない。削除キーが設定されてない場合は、
# 記事の削除ができる。チェックを行い,条件を満たせば$allow_remove_flag=1となる。

	local($ttmp_rmkey) = @_;	# 記事中に埋め込まれた削除キー
	# フォームで入力された削除キー（暗号化前）
	local($tmp_form_rmkey)=$FORM{'passwd'};	

	# フォームで入力された削除キー（暗号化したもの）
	local($cpt_form_rmkey);	
	$cpt_form_rmkey=&make_pass($tmp_form_rmkey);

	if(($ttmp_rmkey eq "")||($ttmp_rmkey eq "no_key")){
		# 削除キーがログにない古い記事の場合、削除を不許可
		# 削除キーがログにない記事の場合、削除を不許可
		$skipped_rmkey_remove++;	# 削除失敗した記事の数

		if($remove_article_number=='1'){
			&error(" パスワードが違います．削除を中止しました ");
		}elsif($remove_article_number == "$skipped_rmkey_remove"){
			&error(" パスワードが違います．削除を中止しました ");
		}
		return;
	}else{
		# 削除キーがログに存在する場合
		if($tmp_form_rmkey eq ""){
			&error(" 削除キーが入力されていません。削除できませんでした。<BR>この記事には投稿者により、削除キーが設定されています。記事投稿時に用いた削除キーを入力してください。なお、削除キーを忘失した場合は、掲示板管理者に頼んで削除してもらってください ");
		}elsif($tmp_form_rmkey eq "$ttmp_rmkey"){
			$allow_remove_flag=1;
		}elsif($cpt_form_rmkey eq "$ttmp_rmkey"){
			$allow_remove_flag=1;
		}else{
			$FORM{'passwd'}="****(←セキュリティ対策のため非表\示\)" if($FORM{'passwd'}=~ /ZzZ/);
			&error(" 入力された削除キー「$FORM{'passwd'}」が違います。削除できませんでした。<BR>この記事には投稿者により、削除キーが設定されています。記事投稿時に用いた削除キーを入力してください。なお、削除キーを忘失した場合は、掲示板管理者に頼んで削除してもらってください ");
		}
	}

}

#=====================#
# クッキーを読む
#=====================#

sub read_cookie{

	local($ttt_cookie)=$ENV{'HTTP_COOKIE'};

	# URLデコードをする(2002.08.12)
	$ttt_cookie=~ s/%([0-9A-Fa-f][0-9A-Fa-f])/pack("C", hex($1))/eg;

    		@pairs = split(/\;/,$ttt_cookie);
    		foreach $pair(@pairs){
    			local($name,$value) = split(/\=/,$pair);
			# エンコードしたセパレータ＝を戻す．	
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
		foreach ( split(/\,/,$COOKIES{'imgboardad121'})){
    			local($name,$value) = split(/\:/);
			$value=&Dec_EQ($value);
    			$COOKIEAD{$name} = $value;
		}
}

#========================#
# クッキーを書く(R6aVer)
#========================#

sub set_cookies{

	undef $set_value;

	# セパレータと区別できなくなる＝を事前にEnc_eqに置換

	$FORM{'utc'}=$new_utc_set;	# 連続投稿カウンタ

	# 削除キーの記憶、非記憶
	$FORM{'rmkey'}=&make_pass("$FORM{'rmkey'}");	# 暗号化
	$FORM{'rmkey'}="" if($FORM{'rmkeym'} ne "on");	# Clear	

	&CEnc_EQ('subject');
	&CEnc_EQ('name');
	&CEnc_EQ('email');
	&CEnc_EQ('view_mode');
	&CEnc_EQ('viewport_set');

	# 2014.02 追加
	&CEnc_EQ('form_mode'); 
	
	&CEnc_EQ('optA');
	&CEnc_EQ('optB');
	&CEnc_EQ('optC');
	&CEnc_EQ('optD');
	&CEnc_EQ('imgtitle');
	&CEnc_EQ('utc');
	&CEnc_EQ('entry_passwd');
	&CEnc_EQ('rmkey');
	&CEnc_EQ('rmkeym');
	# 2012.10 説明省略対応
	&CEnc_EQ('middle_html_disp');

	foreach $p_key(keys %T_COOKIE){
		# パスワードはXXXpasswdというNAMEにする
		# これは暗号化される
		if($p_key=~ /_passwd$/){
			$T_COOKIE{$p_key}=&make_pass("$T_COOKIE{$p_key}");
		}
		$set_value.="$p_key"."\:"."$T_COOKIE{$p_key}"."\,";
	}
	$set_value.="end\:end";

	&set_cookie("imgboard121","$set_value");
}

#=================================#
# クッキーを書く(管理メニュー用)
#=================================#

sub set_admin_cookies{

	undef $set_value;

	# セパレータと区別できなくなる＝を事前にEnc_eqに置換
	&CEnc_EQ('apasswd');

	foreach $p_key(keys %T_COOKIE){
		# パスワードはXXXpasswdというNAMEにする
		# これは暗号化される
		if($p_key=~ /passwd$/){
			$T_COOKIE{$p_key}=&make_pass("$T_COOKIE{$p_key}");
		}
		$set_value.="$p_key"."\:"."$T_COOKIE{$p_key}"."\,";
	}
	$set_value.="end\:end";

	&set_cookie("imgboardad121","$set_value");
}

# 繰り返し
sub CEnc_EQ{
	local($p_name)=$_[0];
	$T_COOKIE{$p_name}	=$FORM{$p_name};
	$T_COOKIE{$p_name}=&Enc_EQ($T_COOKIE{$p_name});
	return("$T_COOKIE{$p_name}");
}

sub Enc_EQ{
	# セパレータと区別できなくなる文字を事前に置換
	local($tmp_data)=@_;
	$tmp_data	=~ s/\=/Enc_eq/g;
	$tmp_data	=~ s/\:/Enc_cln/g;
	$tmp_data	=~ s/\;/Enc_scln/g;
	$tmp_data	=~ s/\,/Enc_km/g;
	return($tmp_data);
}

sub Dec_EQ{
	# セパレータと区別できなくなる文字を復元
	local($tmp_data)=@_;
	$tmp_data	=~ s/Enc_eq/\=/g;
	$tmp_data	=~ s/Enc_cln/\:/g;
	$tmp_data	=~ s/Enc_scln/\;/g;
	$tmp_data	=~ s/Enc_km/\,/g;
	return($tmp_data);
}

sub set_cookie{

	#Copyright(C) to-ru@big.or.jp (1.20以降 2000年対応 NEWバージョン)
        local($name,$value) = @_;
        local($sec,$min,$hour,$mday,$mon,$year,$wday,$date);
        local($days) = 180;      # Expire Date(有効期間。デフォルト180日)

        ($sec,$min,$hour,$mday,$mon,$year,$wday) 
                        = (localtime(time+$days*24*60*60))[0,1,2,3,4,5,6];
        $sec   = "0$sec"  if($sec  < 10);
        $min   = "0$min"  if($min  < 10);
        $hour  = "0$hour" if($hour < 10);
        $mday  = "0$mday" if($mday < 10);
        $year += 1900;
        $wday  = ("Sun","Mon","Tue","Wed","Thu","Fri","Sat")[$wday];
        $mon   = ("Jan","Feb","Mar","Apr","May","Jun",
                  "Jul","Aug","Sep","Oct","Nov","Dec")[$mon];
        $date = "$wday, $mday\-$mon\-$year $hour:$min:$sec GMT";

	# 2002.08.12 Opera対策で日本語をURLエンコードすることにした
	$value =~ s/(\W)/sprintf("%%%02X", unpack("C", $1))/eg;
        print "Set-Cookie: $name=$value; expires=$date\n";      # クッキー出力
#&error("Set-Cookie: $name=$value; expires=$date\n");

	# tok2対応
	if($SERVER_NAME=~ /tok2\.com/){
	  $tok2_cookie="$name=$value; expires=$date\n";
	}
}

#=========================#
# Content-type のチェック
#=========================#
sub content_type_check{

	local($content_type) = @_;

# 画像
	$ext{'image/jpg'}	= 'jpg'; 
	$ext{'image/jpeg'}	= 'jpg'; 	# for NN
	$ext{'image/pjpg'}	= 'jpg';
	$ext{'image/pjpeg'}	= 'jpg';	# for IE
	$ext{'image/gif'}	= 'gif';	# for NN&IE

	$ext{'image/x-png'}	= 'png';	# for PNG  file
	$ext{'image/png'}	= 'png';	# for PNG  file

	# gif,jpeg以外に以下のタイプのデータも投稿できるようにするには
	# 初期設定にて$allow_other_multimedia_dataを1にしてください．
	if($allow_other_multimedia_data ==1){
		&additional_content_types;
	}
	# imgタグで埋め込み可能なタイプ
	foreach(keys %ext){
		if($content_type =~ /$_/ig){
			return $ext{$_};
		}
	}
	# imgタグで埋め込むと危険なタイプ
	foreach(keys %ext2){
		if($content_type =~ /$_/ig){
			return $ext2{$_};
		}
	}
        # これでも駄目なら拡張子から判断
	 if($fname=~ /\.gif$/i){return 'gif';}
	 if($fname=~ /\.jpe?g$/i){return 'jpg';}

	# gif,jpeg以外に以下のタイプのデータも投稿できるようにするには
	# 初期設定にて$allow_other_multimedia_dataを1にしてください．
        if($allow_other_multimedia_data ==1){
         # (自分でリストをさらに追加する場合の注意)
         # cgi,asp,pl,sh,exe.shtml,js,jse,vbs,vbe,hta,wsh,xlm等の拡張子はセキ
	 # ュリティ上危険なので絶対追加しないこと（特にWindowsユーザ）

	# IMAGE
	 if($fname=~ /\.png$/i){return 'png';}	# PNG      形式
#	 if($fname=~ /\.bmp$/i){return 'bmp';}	# Win BMP  形式
	 if($fname=~ /\.pict$/i){return 'pict';}# Mac PICT 形式
	 if($fname=~ /\.pdf$/i){return 'pdf';}	# Adobe PDF形式
#	 if($fname=~ /\.xps$/i){return 'xps';}	# XPS(MS-PDF)形式 2009.06 add
	 if($fname=~ /\.epub$/i){return 'epub';}# 電子書籍ファイル 2009.12

	 if($fname=~ /\.cbz$/i){return 'ebz';}	# Comic Book Zip 2012.08 add
	 if($fname=~ /\.cbr$/i){return 'ebr';}	# Comic Book RAR 2012.08 add

	# MS_OFFICE
#	 if($fname=~ /\.ppt$/i){return 'ppt';}	# PowerPoint
#	 if($fname=~ /\.rtf$/i){return 'rtf';}	# Word98
#	 if($fname=~ /\.doc$/i){return 'doc';}	# Word
#	 if($fname=~ /\.xls$/i){return 'xls';}	# 表計算(excel)
#	 if($fname=~ /\.csv$/i){return 'csv';}	# データベース
#	 if($fname=~ /\.mht$/i){return 'mht';}	# MS Web 単一アーカイブ

	# MS_OFFICE2007
#	 if($fname=~ /\.pptx$/i){return 'pptx';}	# PowerPoint2007(XML)
#	 if($fname=~ /\.docx$/i){return 'docx';}	# Word2007(XML)
#	 if($fname=~ /\.xlsx$/i){return 'xlsx';}	# excel2007(XML)
#	 if($fname=~ /\.pptm$/i){return 'pptm';}	# PowerPoint2007(XML)Macro有効
#	 if($fname=~ /\.docm$/i){return 'docm';}	# Word2007(XML)Macro有効
#	 if($fname=~ /\.xlsm$/i){return 'xlsm';}	# excel2007(XML)Macro有効

	# Archive
	 if($fname=~ /\.lzh$/i){return 'lzh';}	# LHA
	 if($fname=~ /\.zip$/i){return 'zip';}	# ZIP
	 if($fname=~ /\.tar$/i){return 'tar';}	# Tar File
	 if($fname=~ /\.tar\.z$/i){return 'tar.Z';}
	 if($fname=~ /\.tar\.gz$/i){return 'tar.gz';}
	 if($fname=~ /\.tgz$/i){return 'tgz';}  # 200509 add
	 if($fname=~ /\.rar$/i){return 'rar';}  # RAR形式

	# 暗号化Archive
	 if($fname=~ /\.atc$/i){return 'atc';}  # アタッシュケース形式
	 if($fname=~ /\.7z$/i){return '7z';}  # セブンジップ形式

	# 有償の動画、音楽の違法DL罰則化2012.10.01に対応
	if($allow_video_and_audio_data == 1){

	# WindowsMedia
	 if($fname=~ /\.wma?$/i){return 'wma';}	# Windows Media Audio
	 if($fname=~ /\.asf$/i){return 'asf';}	# Windows Media (ASF形式)
	 if($fname=~ /\.asx$/i){return 'asx';}	# Windows Media (ASF形式 Redirecter)
	 if($fname=~ /\.wmv$/i){return 'wmv';}	# Windows Media オーディオ/ビデオ ファイル

	# Other Audio
	 if($fname=~ /\.at3$/i){return 'at3';}	# ATRAC3 ファイル

	# 携帯（FOMA) new
	 if($fname=~ /\.mp3$/i){return 'mp3';}	# MP3データ
	 if($fname=~ /\.mp4$/i){return 'mp4';}	# MP4データ(iモーション)

	 
	 # スマートフォンやimgboard FLV Playerとの互換性対策
	 if($ENV{'CONTENT_LENGTH'} < 10000*1024){
	  # 10MB以下の場合
	  if($fname=~ /\.3gp$/i){return '3gp';}	# MP4データ(iモーション)
	  if($fname=~ /\.3gpp$/i){return '3gpp';}# MP4データ(iモーション)
	  if($fname=~ /\.3gp4$/i){return '3gp4';}# MP4データ(iモーション)
	 }else{
	  # どうせiムービーでは再生できない。
	  # よって、スマートフォンやFlv Playerと互換性の良いmp4にする
	  if($fname=~ /\.3gp$/i){return 'mp4';}	# MP4データ
	  if($fname=~ /\.3gpp$/i){return 'mp4';}# MP4データ
	  if($fname=~ /\.3gp4$/i){return 'mp4';}# MP4データ
	 }

	 # 2010.08 iPhoneの動画対応
 	 if($fname=~ /\.mov$/i){return 'mp4';}
	 
	 # 2009.10 iPhone対応追加
	 if($fname=~ /\.m4v$/i){return 'm4v';}	# M4vファイル


	# 2009.06追加
#	 if($fname=~ /\.ogm$/i){return 'ogm';}	# ogg Vorbis
#	 if($fname=~ /\.mkv$/i){return 'mkv';}	# MKVコンテナ(DivX7等)
#	 if($fname=~ /\.ogv$/i){return 'ogv';}	# ogg Theora (VP3 for HTML5)


	 # その他細かい物は削除。今後は imgboard 2010をご利用ください。

	 if($fname=~ /\.avi$/i){return 'avi';}
	 if($fname=~ /\.mpg$/i){return 'mpg';}

	# 2006.12.13 Flash Movie追加
	 if($fname=~ /\.flv$/i){return 'flv';}	# Flash Video

	# 2010.06.08 imgboard FLV Player用に追加
	 if($fname=~ /\.f4v$/i){return 'mp4';}	# Flash Video
	 if($fname=~ /\.f4a$/i){return 'mp4';}	# Flash Video
#	 if($fname=~ /\.f4b$/i){return 'mp4';}	# Flash Video(保護付きなので再生できない)

	} #end of $allow_video_and_audio_data
        } #end of allow_other_multimedia_data == OK

	$unknown_data_exit=1;

# データタイプ不明の場合の最終判断
	if($unknown_data_exit==1){
		&error(" 現在の設定では、このタイプのデータはアップロードできません．");
	}else{
		return 'dat';
	}
}

#==========================#
# Content-type の自動補完
#==========================#
sub additional_content_types{

# 拡張子がないファイルがアップロードされた場合、ブラウザから通知された
# マイムタイプから拡張子を決定します。Macユーザからの拡張子なしファイル
# のアップロードに対応するための部分です。

# 画像系（その他）
#	$ext{'image/x-png'}	= 'png';	# for PNG  file
#	$ext{'image/png'}	= 'png';	# for PNG  file
	$ext{'image/pict'}	= 'pict';	# for PICT file
#	$ext{'image/bmp'}	= 'bmp';	# for BMP  file
	$ext2{'application/pdf'}= 'pdf';	# for PDF  file

#	$ext2{'application/zip'}= 'cbz';	# for Comic Book zip Archive
#	$ext2{'application/x-rar-compressed'}= 'cbr';# for Comic Book rar Archive

	$ext2{'application/epub'}= 'epub';	# for kindle(epub) 2009.12

# アーカイブ系
	$ext2{'application/zip'}= 'zip';	# for ZIP   (Win)
	$ext2{'x-zip'}= 'zip';			# for ZIP   (Win)
	$ext2{'compressed/lha'}= 'lzh';		# for LZH   (Win)
	$ext2{'x-tar'}= 'tar';			# for TAR   (Unix)
	$ext2{'application/x-7z-compressed'}= '7z';	# for 7ZIP

	# 有償の動画、音楽の違法DL罰則化2012.10.01に対応
	if($allow_video_and_audio_data == 1){

# 3D & ビデオ系
	# TODO movも小さいときは3GPにリネームした方がいいかも
	$ext2{'video/quicktime'}	= 'mov';# for QuickTime  file
	$ext2{'video/(.*)mpeg'}	= 'mpeg';	# for MPEG file
	$ext2{'video/(.*)msvideo'}= 'avi';	# for AVI  file
	$ext2{'video/(.*)-asf'}= 'asf';		# for NetShow file
	$ext2{'video/avi'}= 'avi';		# for AVI  file
	$ext2{'video/x-ms-wvx'}= 'wvx';    # Windows Media オーディオ/ビデオ ショートカット
	$ext2{'video/x-ms-wmv'}= 'wmv';    # Windows Media オーディオ/ビデオ ファイル
	 # スマートフォンやimgboard FLV Playerとの互換性対策
	if($ENV{'CONTENT_LENGTH'} < 10000*1024){
	 # 10MB以下の場合
	 $ext2{'video/3gpp'}	= '3gp';	# for i-Motion file
	 $ext2{'video/3gp'}	= '3gp';	# for i-Motion file
	 $ext2{'audio/3gpp'}	= '3gp';	# for i-Motion file
	 # 10MB以上だと、どうせ再生できないので、
	 # FLVPlayerやiPhone/iPadと互換性の高いmp4拡張子にする
	}else{
	 $ext2{'video/3gpp'}	= 'mp4';	# for i-Motion file
	 $ext2{'video/3gp'}	= 'mp4';	# for i-Motion file
	 $ext2{'audio/3gpp'}	= 'mp4';	# for i-Motion file
	}

# 2006.12.13 追加
	$ext2{'video/x-flv'}	= 'flv';	# Flash Videoデータ
	$ext2{'video/x-m4v'}	= 'm4v';	# M4v データ

# 音楽系
	$ext2{'audio/mpeg'}= 'mp3';			# for MPEG Audio
	$ext2{'audio/x-mpegurl'}= 'm3u';		# for MPEG Audio
	$ext2{'audio/x-wav'}= 'wav';		# for WAV Audio

	} #end of $allow_video_and_audio_data

# 会社で仕事に役立ち系
#	$ext2{'text/html'}= 'html';	 	# HTMLテキスト
#	$ext2{'text/plain'}= 'txt'; 		# テキスト
#	$ext2{'msword'}= 'doc';			# MS_WORD
#	$ext2{'excel'}= 'xls';			# MS_Excel
#	$ext2{'powerpoint'}= 'ppt';			# MS_PowerPoint

}
# 2009.10 new
#=========================================#
#  拡張子からマイムを計算するルーチン
#=========================================#
# HTML5の埋め込み用に、拡張子からマイムを計算するルーチン
#  
#
sub make_html5_mimetype{

    local($tmpp_check_ctype)		=$_[0];# 引数1として取得
	local($tmpp_img_location)		=$_[1];# 引数2として取得

	 if($tmpp_check_ctype=~ /video/i){
	# video
		if($tmpp_img_location=~ /\.3gp?p$/i){return 'video/3gpp';}
		if($tmpp_img_location=~ /\.3gp?p?2$/i){return 'video/3gpp2';}
		if($tmpp_img_location=~ /\.mov$|\.qt$|\.mqv$/i){return 'video/quicktime';}
		if($tmpp_img_location=~ /\.mp4$/i){return 'video/mp4';}
		if($tmpp_img_location=~ /\.m4v$/i){return 'video/x-m4v';}
		if($tmpp_img_location=~ /\.mp4$/i){return 'video/mp4';}
	 }
	 
	# audio
	 if($tmpp_check_ctype=~ /audio/i){
	  if($tmpp_img_location=~ /\.mp3$/i){return 'audio/mp3';}
	  if($tmpp_img_location=~ /\.m4a$/i){return 'audio/x-m4a';}	# AAC audio
	 }	 
	 return 'nomatch';
}
#
#=========================#
# html出力
#=========================#

#====================================#
# フォーム部分のＨＴＭＬを出力する
#====================================#

sub output_form_html{

	# 表示モード以外ならフォームを出さない
	if($FORM{'mode'} ne ""){
		return;
	}

	# 修正記事選択画面ならフォームを出さない
	if(($FORM{'amode'} eq "select_edit")&&($FORM{'bbsaction'} ne "edit_form")){
		return;
	}

	# 代入する変数を準備

	# 表示モード・デフォルト選択値
	if($COOKIE{'view_mode'} ne ""){
		&select_default_view_mode;
	# 2010.06.23 未投稿経験者にFLV Playerが表示されない問題に対処
	}else{
		if($show_img_on_board == 1){
			$COOKIE{'view_mode'}='as_cgi_defined';
		}
	}

	# フォーム欄の色
	if($HTTP_USER_AGENT =~ /IE/i){
		$bgcolor_ie="bgcolor=GRAY";
	}

   #==================================================#
   # 同一ウィンド表示時（デフォルト）の掲示板の先頭
   #==================================================#

	if(($form_disp_on_board ==1)||($FORM{'bbsaction'} eq 'disp_form_only')||($FORM{'bbsaction'} eq 'disp_rep_form')||($FORM{'bbsaction'} eq 'edit_form')){

		# 前処理（埋込みデータを加工）

		# 会員パスワード設定をしてない場合、項目は出さない。
		if(($use_passwd_flag != 1)||(($PM{'res_no_passwd_flag'}== 1)&&($FORM{'bbsaction'} eq 'disp_rep_form'))){
			$cm_out_pw_h='<!--';
			$cm_out_pw_f='-->';
		}

		# タグを許可する場合、注意書きを追加しミスを予防する。
		if($use_tag == 1){
# 普通機能なので、説明やめた(2012.10)
#			$tag_siyou_tyuui='<LI>タグ使用可。使用する場合、閉じ忘れにご注意ください';
		}

		# youTubeタグを許可する場合、説明を表示する
		if($use_youtube_tag_in_comment == 1){
			$tag_siyou_tyuui="$tag_siyou_tyuui".'<LI><a href="http://www.youtube.com/?gl=JP&hl=ja">youTube</a>の場合は、"共有"の<B>youtu . be</B>のURLを ,<a href="http://www.nicovideo.jp/">ニコ動</a>,ustream上の動画を掲示板に埋込表示する場合は、"埋め込みコード"を1個、そのまま本文欄にコピペしてください </LI>';
		}

		# 返信・編集フォーム時は画像アップロードさせない
		if(($FORM{'bbsaction'} eq 'disp_rep_form')||($FORM{'bbsaction'} eq 'edit_form')||($COOKIE{'form_mode'} =~ /movie/i)){
			$cm_out_img_h='<!--';
			$cm_out_img_f='-->';
		}


		# 初期設定を変更してない場合、終了ボタンは出さない。
		if(($form_disp_on_board==0)||($back_url eq 'http://あなたのプロバイダ/あなたのディレクトリ/index.html')){
			$cm_out_exit_h='<!--';
			$cm_out_exit_f='-->';
		}

	# 入力フォーム部form_htmlのHTMLを出力（書換えは初期設定の所で行う）
	&form_html;

	# 修正ウィンドの時は以下を出さない
	return if($FORM{'bbsaction'} eq "edit_form");
	
	if($FORM{'bbsaction'} eq 'disp_rep_form'){

print<<HTML_END;
<HR>
<!--掲示板中央部の説明部分A-->
<font size=-1>
 <UL>
   <LI><!--タグ使用上の注意が自動で入ります-->$tag_siyou_tyuui
</UL>
</font>
HTML_END

	}else{

		# アンカーリンク部分を出力（書換えは初期設定の所で行う）
		&link_top_html if($form_disp_on_board ==1);

		# 入力フォーム下の説明部分を出力（書換えは初期設定の所で行う）
		&middle_A_html;
	}

	&middle_B_html if($form_disp_on_board ==1);

   #================================#
   # 別ウィンド表示時の掲示板の先頭
   #================================#

	}else{
		#初期設定を変更してない場合、終了ボタンは出さない。
		if($back_url eq 'http://あなたのプロバイダ/あなたのディレクトリ/index.html'){
			$cm_out_exit_h='<!--';
			$cm_out_exit_f='-->';
		}

	&middle_B_html if($form_disp_on_board ==0);

	# アンカーリンク部分を出力（書換えは初期設定の所で行う）
	&link_top_html;

print<<EOF;

<TABLE border="1" cellspacing="0" cellpadding="0">
<TR bgcolor=gray>
 <FORM METHOD=GET ACTION="$back_url">
 <TD>
  <FONT SIZE=-1>
   $cm_out_exit_h<INPUT TYPE=SUBMIT VALUE="トップページへ戻る" $output_button_px>$cm_out_exit_f
  </FONT>
 </TD>
</FORM>
EOF

print<<EOF;
<FORM>
 <TD>
  <FONT SIZE=-1>
   <INPUT TYPE="button" VALUE="投稿" $output_button_px 
onClick="input_form=window.open('$cgi_name?bbsaction=disp_form_only&page=$disp_page&p1=$FORM{'p1'}&p2=$FORM{'p2'}&amode=$FORM{'amode'}','form_window','toolbar=no,status=yes,menubar=yes,scrollbars=yes,resizable=yes,close=yes,width=730,height=400');">
  </FONT>
 </TD>
</FORM>

<NOSCRIPT>
<!-- Javascript非対応ブラウザ用 -->
<FORM action="$cgi_name" method=GET TARGET="form_window">
<INPUT TYPE=HIDDEN NAME="bbsaction" VALUE="disp_form_only">
<INPUT TYPE=HIDDEN NAME="page" VALUE="$disp_page">

 <TD>
  <FONT SIZE=-1>
   <INPUT TYPE=SUBMIT VALUE="投稿(Javascript 非対応ブラウザ用)" $output_button_px>
  </FONT>
 </TD>
</FORM>
</NOSCRIPT>

</TR>
</TABLE>
<BR>

EOF
	}
   #============================================#
   # 別ウィンド表示時の掲示板の先頭ここまで
   #============================================#

}

#====================================#
# 記事部分のＨＴＭＬを出力する
#====================================#

sub output_html{

	local($tmp_file)	= $_[0];# 処理するログファイル名

        # cgi_wrap使用プロバイダ対策
	# 古いプロバイダの中にはcgi_wrapを使っているプロバイダがあります。
	# 相対パス指定を使用する場合、下記の数値を1にして、そのイメージ
	# 保存ディレクトリのURLを$img_urlで指定することにより、掲示板を
	# 使用する事ができます。それ以外の人は必ず0に指定してください。
	# なお、1を指定した場合は$img_urlの設定が必須になります。   

	$using_cgi_wrap=0;#(デフォルト0)

	# メッセージを読み込む
	# 読込みながらページ生成に必要な情報を作る

	undef	@HEAD_MESSAGE;
	undef	@GOUP_MESSAGE;	  # 上へ持って行くメッセージ(ただ抜いたもの)
	undef	@LATEST_MESSAGE;  # 上へ持って行くメッセージ(ソート後)
	undef	@RECENT_MESSAGE_UID;  # 最近登録されたメッセージ

#$PM{'res_go_up'} = 1;

	undef	@MESSAGE;
	undef	$all_message;
	local($tmp_parent);


	undef	@PAGE_START;	# ページスタートの記事番号情報を保存する配列
	undef	@PAGE_END;	# ページエンド  の記事番号情報を保存する配列
	undef	$page_parent_counter;	# 親記事を数える
	$total_counter="0";		# 親＋子の記事を数える

	# 検索用変数
	local($search_words)	= $FORM{'SearchWords'};
	local($match_mode)	= $FORM{'MatchMode'};	# 検索タイプ(AND OR)
	local($match_flag);

	# 返信記事を作成する場合は検索機能を流用する
	# 親記事の血統を持つ記事を表示する
	if($FORM{'bbsaction'} eq 'disp_rep_form'){
		$search_words		="$FORM{'blood'}";
		$match_mode		="AND";
	}

	# ループに入る前にチェック＆下処理をしておく
	if(($FORM{'mode'} eq "search_menu")||($FORM{'bbsaction'} eq 'disp_rep_form')){
	    if($search_words eq ""){
		&error(" 検索ワードが入力されていません ");
	    }else{
		$search_words =~ s/　/ /g;
		@tmp_search_words = split(/\s+/, $search_words);
	    }
	}

	open(READ, "$tmp_file");
	eval "flock(READ,1);" if($PM{'flock'} == 1 );

	push(@PAGE_START,0);

	# 条件に一致するものを@MESSAGEに入れる
	while(<READ>){

		# HEADER保存 (将来への拡張もここで対応)
		if($_ =~ /^\#?\,param_/i){

			if($_ =~ /^\,param_last_update(\s*)=(\s*)(\d+)(\s*)/i){
				# 最終更新日を取得する
				$HEAD_MESSAGE{'last_update'}="$3";
			}elsif($_ =~ /^\,param_last_bloods(\s*)=(\s*)([^\;]*)(\;+)(\s*)/i){
				# 最新記事のスレッドのリストを取得する
				$HEAD_MESSAGE{'last_bloods'}="$3";
				$HEAD_MESSAGE{'last_bloods'}=&Dec_EQ("$HEAD_MESSAGE{'last_bloods'}");
				&output_new_bloods_list;
			}else{
				push(@HEAD_MESSAGE, $_);
			}

		}
# Debug
#	&error("nw @NEW_BLOODS");

		if($_ =~ /^([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]*)\t([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)/){
			undef $match_flag;

			# 検索時
			if(($FORM{'mode'} eq "search_menu")||($FORM{'bbsaction'} eq 'disp_rep_form')){

			  $tmp_line_data=$_;	# 検索するラインを保存

			  foreach $tmp_search_word(@tmp_search_words) {
#&error("$tmp_search_word");

				# 2004.05
				$tmp_search_word=~ tr/A-Z/a-z/;	# 小文字に統一
				$tmp_line_data	=~ tr/A-Z/a-z/;	# 小文字に統一

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
				push(@MESSAGE, $_);
				$all_message++;
			  }else{
				next;
			  }
			# 非検索時
			}else{
				# レスのついた記事を上へ持って行くために
				# @MESSAGEへ入れずに、@GOUP_MESSAGEへ
				if($PM{'res_go_up'} == 1){
					undef $tp_match_flag;
					local($tp_loop_counter)=0;
					foreach $tmp_parent(@NEW_BLOODS){
					  # 5スレッドまで上へ持って行く
					  # それ以上にすると負荷が上がるのでやめる
					  last if($tp_loop_counter >= 5);
					  if(($tmp_parent eq "$9")||($tmp_parent eq "$11")){
						$tp_match_flag = 1;
						last;# 検出したら抜ける
					  }
					  $tp_loop_counter++;
					}
					if($tp_match_flag == 1){
					  push(@GOUP_MESSAGE, $_);
					  $all_message++;
					}else{
					  push(@MESSAGE, $_);
				  	  $all_message++;
					}
				}else{
				  push(@MESSAGE, $_);
				  $all_message++;
				}
			}

		}
	}
	eval "flock(READ,8);" if($PM{'flock'} == 1 );
	close(READ);

# Debug
#	&error("gup @GOUP_MESSAGE");



	# レスのついた記事を上へ持って行くために、
	# @MESSAGEの先端に足す
	# 高速化、低負荷化のために、リストに入れてから、ソートする

	if($PM{'res_go_up'} == 1){
	  # 検索とレスの場合は足さない
	  if(($FORM{'mode'} ne "search_menu")&&($FORM{'bbsaction'} ne 'disp_rep_form')){
	      local($tmp_goup_line);
	      $tp_loop_counter=0;
	      foreach $tmp_parent(@NEW_BLOODS){
		  # 5スレッドまで上へ持って行く
		  last if($tp_loop_counter >= 5);
	       foreach $tmp_goup_line(@GOUP_MESSAGE){
		if($tmp_goup_line =~ /^([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]*)\t([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)/){
		  if(($tmp_parent eq "$9")||($tmp_parent eq "$11")){
			push(@LATEST_MESSAGE,$tmp_goup_line);
		  }
	        }
	       }
		$tp_loop_counter++;
	      }
		# @MESSAGEの先端に足す
		unshift(@MESSAGE,@LATEST_MESSAGE);
# Debug
#	&error("mes @MESSAGE");
#	&error("latest @LATEST_MESSAGE");
	  }
	}


	# ページ情報を作る
	foreach(@MESSAGE){

		if($_ =~ /^([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]*)\t([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)/){

			# 記事閲覧、ページ生成に必要な情報(@PAGE_START)を用意する
			if($9 ne ""){
#				$child_kiji_flag="1";	# 子記事確認用フラグ
			}else{
				$page_parent_counter++;
			}
			if($page_parent_counter > $disp_message){
				push(@PAGE_START,$total_counter);
				push(@PAGE_END,$total_counter-1);
				$page_parent_counter=1;
			}
			$total_counter++;
		}
	}

	push(@PAGE_END,$total_counter);
	
#&error("start @PAGE_START end @PAGE_END");

	# ページを決める
	$total_page=@PAGE_START;

	if($FORM{'page'} > 0){
		if($FORM{'page'} > $total_page){
			$disp_page = $total_page;
		}else{
			$disp_page = $FORM{'page'};
		}
	}else{
		$disp_page = 1;
	}
	$next_page 	= $disp_page + 1;
	$pre_page 	= $disp_page - 1;

	&output_kiji_html;

   #====================================#
   # 記事部分のＨＴＭＬを出力する
   #====================================#

sub output_kiji_html{


	# ユーザプロファイル指定部分のＨＴＭＬ（書換えはsub form_usr_profile_htmlの所で行う）
	if($user_selected_view_mode==1){
		&form_user_profile_html;
	}

	&output_button_HTML(2);

	if($FORM{'mode'} eq "search_menu"){
	  print"<CENTER>\n";
	  print"$TOTAL_COUNTER Articles hit \n";
	  print"</CENTER>\n";
	}elsif($FORM{'bbsaction'} eq 'disp_rep_form'){
	  print"<UL>\n";
	  print" ↓ The form content will be added to the following article thread ";
	  print"</UL>\n";
	}

	# 外部ファイル用の処理をロード（将来拡張用）
	if($EXTSUB{'kiji_pre_loop'} == 1){
		 &ext_config_kiji_pre_loop;
	}

	# 管理者モード解除用のリンクを出す
	if($FORM{'amode'} ne ""){
	  print qq| <P><CENTER>\n|;
	  print qq| <TABLE bgcolor=yellow><TR><TD><B>---- The board is currently in admin mode $amode_done_mes01 -----</B></TD><TD><A HREF="$cgi_name?page=$FORM{'page'}&p1=$FORM{'p1'}&p2=$FORM{'p2'}"> [管理者モード終了] </a></TD><TR></TABLE> \n|;
	  print qq| </CENTER>\n|;
	}


	# 記事削除指定用のフォーム開始部
	print"<!-- 記事削除指定用のフォーム開始部 -->\n";
	print"<FORM ACTION=\"$cgi_name\" METHOD =\"POST\" style=\"display: inline\">\n";
	print"<INPUT TYPE=HIDDEN NAME=\"page\" VALUE=$disp_page>\n";
	print"<INPUT TYPE=HIDDEN NAME=\"amode\" VALUE=$FORM{'amode'}>\n";
	print"<INPUT TYPE=HIDDEN NAME=\"p1\" VALUE=$FORM{'p1'}>\n";
	print"<INPUT TYPE=HIDDEN NAME=\"p2\" VALUE=$FORM{'p2'}>\n";
	print"$POSTADDP{'REMOVEFORM'}<!-- 拡張用 -->\n";
	print"<!-- 以降記事部です -->\n";

	# 2008.08
	$oya_kiji_embed_flag=0;		# 親記事がEMBED系確認用フラグ
	$child_kiji_embed_flag=0;	# 子記事がEMBED系確認用フラグ

	# 記事部 inu
	for($i=$PAGE_START[$disp_page-1];$i<=$PAGE_END[$disp_page-1];$i++){
		if($MESSAGE[$i]	=~ /^([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]*)\t([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)/){

			# パラメータの準備
			undef $child_kiji_flag;	# 子記事確認用フラグ
			undef $old_kiji_flag;	# 旧形式確認用フラグ

			undef $tmp_seq_no;
			undef $tmp_blood_name;
			undef $tmp_rmkey;
			undef $tmp_unq_id;
			undef $tmp_snl_location;

			undef $new_kiji_flag; # 最近の記事フラグ

			$tmp_subject		= $1;
			$tmp_name		= $2;
			$tmp_email		= $3;
			$tmp_date		= $4;
			$tmp_body		= $5;
			$tmp_img_location	= $6;
			$tmp_imgtitle		= $7;
			$tmp_seq_no		= $8;	# 連番
			$tmp_blood_name		= $9;	# 親の血統ID(子供のみ持つ)
			$tmp_rmkey		= $10;	# 削除キー
			$tmp_unq_id		= $11;	# 固有ID(時刻ベース)
			$new_p1			= $12;
			$new_p2			= $13;


			$tmp_rm_number		= $i+1;

			# 準備

 			if($tmp_unq_id eq ""){
				$old_kiji_flag="1";	# 旧形式確認用フラグ
			}

			if($tmp_blood_name ne ""){
				$child_kiji_flag="1";	# 子記事確認用フラグ
			}else{
#				$parent_counter++
			}

			# 回りこみレイアウト用
			$tmp_bq_opt		= "";

# Debug
# &error("rmid @RECENT_MESSAGE_UID");

			# 最新投稿記事にはフラグを立てる
 			if($PM{'disp_new_notice'}==1){
			    $tp_loop_counter=0;
			    foreach $recent_uid(@RECENT_MESSAGE_UID){
				# 上げスレッド数1～10。増やすと遅くなるので注意。
 			     last if($tp_loop_counter >= 5 ); # 2014.02 change
 			     if($recent_uid == $tmp_unq_id ){
				$new_kiji_flag="1";	# 最近の記事フラグ
				last;
			     }
			     $tp_loop_counter++;
			    }
			}

			$tmp_subject=&Dec_EQ("$tmp_subject");

			undef %IMG_PARAMETERS;

			undef %YOUTUBE_VIDEO;# 2008.06.25
			undef %DAILYMOTION_VIDEO;# 2009.12
			undef %USTREAM_VIDEO;	# 2010.05
			undef %HTML5_PARAM;		# 2010.05

			# imgtitleから情報を抜き出す
			if($tmp_imgtitle ne ""){
				$tmp_imgtitle=&parse_img_param("$tmp_imgtitle");
			}


			# 予備入力項目パラメータを復元
			# bodyの中に、コメントアウト形式でデータは隠し保存されている
			# 書式<!--opt:パラメータ名=値;パラメータ名2=値2・・・-->
			#<!--opt:と-->を除きパラメータ部を抽出する処理
			if($tmp_body ne ''){
				($tmp_body,$opt_form_data)	=split(/<\!--opt:/,$tmp_body);
				$opt_form_data			=~ s/-->//g;
			}
			#パラメータ$opt_form_dataが追加されている場合．

		        undef %OPTDATA;		# 新R6
		        undef %OPT_FORM_DATA;	# 旧R5互換用

			if($opt_form_data ne ''){
				foreach ( split(/;/,$opt_form_data)){
					local($name,$value) = split(/\=/);
					$value=&Dec_EQ("$value");
					if($name=~ /^opt_data_(.+)$/){
					  $OPTDATA{"opt$1"}	= $value;
					  $OPT_FORM_DATA{"opt$1"}= $value;# 旧R5互換用
					# 徐々にこちらへシフト
					}elsif($name=~ /^opt(.+)$/){
					  $OPTDATA{"$name"}	= $value;
					  $OPT_FORM_DATA{"$name"}= $value;# 旧R5互換用
					}
				}
			}

			# 相手のホスト名を変数$user_IP に代入
			# （なりすまし防止などの事情で相手のＩＰを表示したい場合はこの変数を使って下さい）
			if($tmp_body=~ /user：\s([^>]*)(\s*)--/){
			    $user_IP="$1";
			    $user_IP=&tiny_decode("$user_IP"); #2002.02

			    # $user_IP情報をプライバシー保護のため、一部マスクして隠す
			    if($use_ip_privacy_filter==1){
			       &user_IP_privacy_filter;
			    }
			}else{
			    $user_IP="No IP info";
			}

			if($no_disp_RH_in_HTML_sorce==1){
				$tmp_body=~ s/user：\s([^>]*)(\s*)--/user： na --/g;
			}else{
			    $tmp_body=~ s/user：\s([^>]*)(\s*)--/user： $user_IP--/g;
			}


			# disp_mode(表示モード)を決定

			undef $disp_mode;

			&check_mode;


			# テキストリンク用ＨＴＭＬ指定部に代入する$data_typeを選択
			# （ポリシー）悪意のあるアップロードデータをユーザが
			# うっかりクリックしてトラブルに巻き込まれることがないように、
			# データの種類を拡張子から自動的に解析、表示し、注意を喚起する。

			$disp_ip_flag=0;
			undef $data_type;

			if($tmp_img_location ne ""){
			  if($tmp_img_location=~ /\.gif$|\.jpe?g$|\.png$/i){
				$data_type=" 画　像 ";
			  }elsif($tmp_img_location=~ /\.aiff?$|\.aifc$|\.snd$|\.au$|\.midi?$|\.wav$/i){
				$data_type=" 音　声 ";
			  }elsif($tmp_img_location=~ /\.mp4$/i){
				$data_type=" 動画\/音声 [MP4形式→QuickTime再生 (<a href=http://www.apple.com/jp/quicktime/ target=_blank>PC再生</a>)] ";
			  }elsif($tmp_img_location=~ /\.mp3$/i){
				$data_type=" 音　声 (MP3形式) ";
			  }elsif($tmp_img_location=~ /\.wma?$/i){
				$data_type=" 音　声 (Windows Media Audio) ";
			  }elsif($tmp_img_location=~ /\.at3$/i){
				$data_type=" 音　声 (ATRAC3形式) ";
			  }elsif($tmp_img_location=~ /\.ogg$/i){
				$data_type=" 音　声 (ogg Vorbis 形式) ";
			  }elsif($tmp_img_location=~ /\.te?xt$|\.html?$/i){
				$data_type=" テキスト ";
			  }elsif($tmp_img_location=~ /\.pdf$/i){
				$data_type=" Adobe PDF 書類 ";
			  }elsif($tmp_img_location=~ /\.xps$/i){
				$data_type=" XPS MS版PDF 書類 ";
			  }elsif($tmp_img_location=~ /\.epub$/i){
				$data_type=" 電子書籍 epub書類 ";
			  }elsif($tmp_img_location=~ /\.cbr$|\.cbz$/i){
				$data_type=" 電子マンガ書類 [Comic Book (<a href=http://blog.kowalczyk.info/software/sumatrapdf/free-pdf-reader.html target=_blank>PC閲覧</a>)] ";
			  

			  # 2009.10 アタッシュケース対応
			  }elsif($tmp_img_location=~ /\.atc$/i){
				$data_type=" 圧縮デ\ータ [AES暗号化 (<a href=http://www.forest.impress.co.jp/library/software/atasshecase/ target=_blank>PC解凍</a>)] ";
			  }elsif($tmp_img_location=~ /\.7z$/i){
				$data_type=" 圧縮デ\ータ [7zip暗号化 (<a href=http://lhaz.softonic.jp/ target=_blank>PC解凍</a>)] ";
			  }elsif($tmp_img_location=~ /\.(zip|tar|rar|arj|tar.g?z)$/i){
				$data_type=" 圧縮デ\ータ($1形式) ";

			# 携帯 2002.04.05 update

			  }elsif($tmp_img_location=~ /\.mng$/i){
				$data_type=" 動　画 [JSKY-Animation]";
			  }elsif($tmp_img_location=~ /\.amc$/i){
#				$data_type=" 動　画 [ezmovie形式]";
				$data_type=" 動　画/着ムービ [ au ezmovie形式(<a href=http://www.au.kddi.com/ezfactory/mm/ezmovie1.html target=_blank>PC再生</a>)]";
			  }elsif($tmp_img_location=~ /\.3gp$/i){
				$data_type=" 動　画 [iモーション or 着ムービ or  QuickTime圧縮 (<a href=http://www.apple.com/jp/quicktime/ target=_blank>PC再生</a>)] ";
			  }elsif($tmp_img_location=~ /\.flv$/i){
# 2006.12.13 FLV対応
				$data_type=" 動　画 [Flash Video形式→FLV再生 (<a href=http://www.gomplayer.jp/ target=_blank>PC再生</a>)] ";
			  }elsif($tmp_img_location=~ /\.mkv$/i){
				$data_type=" 動　画 [MKV形式→PC再生 (<a href=http://www.gomplayer.jp/ target=_blank>PC再生</a>)] ";
			  # 2009.06 OGM対応
			  }elsif($tmp_img_location=~ /\.ogm$/i){
				$data_type=" 動　画 [OGM形式→PC再生 (<a href=http://www.gomplayer.jp/ target=_blank>PC再生</a>)] ";
			  }elsif($tmp_img_location=~ /\.ogv$/i){
				$data_type=" 動　画 [OGV形式→PC再生 (<a href=http://www.gomplayer.jp/ target=_blank>PC再生</a>)] ";
			  # 2009.12 m4v対応
			  }elsif($tmp_img_location=~ /\.m4v$/i){
				$data_type=" 動　画 [M4V形式→QuickTime再生 (<a href=http://www.apple.com/jp/quicktime/ target=_blank>PC再生</a>)] ";
			  }elsif($tmp_img_location=~ /\.mmf$/i){
				$data_type=" 音　声 [着うた/着メロ(Docomo)(<a href=http://www.vector.co.jp/soft/win95/net/se211027.html target=_blank>PC再生</a>)] ";
			  }elsif($tmp_img_location=~ /\.pmd$|\.qcp$/i){
				$data_type=" 音　声 [EZ音声/きゃらメロ]";
			  }elsif($tmp_img_location=~ /\.mld$/i){
				$data_type=" 音　声 [着うた/着メロ(Docomo)]";
# 2009.12 add
			  }elsif($tmp_img_location=~ /\.m4a$/i){
				$data_type=" 音　声 [MPEG-4 AAC Audio(<a href=http://www.apple.com/jp/itunes/download/ target=_blank>PC再生</a>)]";
			  }elsif($tmp_img_location=~ /\.m4b$/i){ # 2009.06 add
				$data_type=" 音　声 [MPEG-4 AAC DRM Audio(<a href=http://www.apple.com/jp/itunes/download/ target=_blank>PC再生</a>)]";
			  }elsif($tmp_img_location=~ /\.m4p$/i){ # 2009.06 add
				$data_type=" 音　声 [MPEG-4 AAC iTune DRM Audio(<a href=http://www.apple.com/jp/itunes/download/ target=_blank>PC再生</a>)]";
			  }elsif($tmp_img_location=~ /\.amr$/i){ # 2009.12 add
				$data_type=" 音　声 [AMR形式→QuickTime再生 (<a href=http://www.apple.com/jp/quicktime/ target=_blank>PC再生</a>)]";
			  }elsif($tmp_img_location=~ /\.ppt$|\.xls$|\.csv$|\.rtf$|\.doc$/i){
				$data_type=" OFFICE 書類 ";
			  }elsif($tmp_img_location=~ /\.pptx$|\.xlsx$|\.docx$/i){
				$data_type=" MS OFFICE2007 書類 ";
			  }elsif($tmp_img_location=~ /\.pptm$|\.xlsm$|\.docm$/i){
				$data_type=" OFFICE2007書類(Macro有効) ";
			  }elsif($tmp_img_location=~ /\.slk$/i){
				$data_type=" 表計算汎用交換デ\ータ 書類 ";
			  }elsif($tmp_img_location=~ /\.wri$/i){
				$data_type=" Windows ワ\ードパット書類 ";
			  }else{
				$disp_ip_flag=1;
				$data_type=" データ ";
			  }
			}

#========================#
# CGIのURLを決める
#========================#
# imgboard FLV Player 2010.06.02 update
# メールリンク/imgboard FLV Player用
# 
sub make_contents_url {

	if($tmp_img_location ne ""){
		$MYCGI_ENV{'img_box_base_url'}="$MYCGI_ENV{'cgi_base_url'}"."$tmp_img_location";
		$MYCGI_ENV{'img_box_base_url'}=~ s/\.\///g;
	}
}
#
&make_contents_url;

# 3GPはFlashPlayerで再生できなかった
			if((($COOKIE{'view_mode'} eq "")&&($show_img_on_board == 1))||($COOKIE{'view_mode'}=~ /as_cgi_defined$|text_img_type12$|text_img_type13$|text_img_type2$|text_img_type3$|text_img_type4$|text_img_type5$/i)){ #オート（おまかせ)

			  # 動画のリンクを作る。動画は単独でなく、スレッド単位で引用、参照される仕様とする（話題を発散させないため）
			  # FlashVarsの区切りが&なので、urlに&を含むものを入れるとおかしくなる。ここだけは、URLエスケープしておこう
			  $HTML5_PARAM{'thread_link'} 		="http://"."$ENV{'SERVER_NAME'}"."$ENV{'SCRIPT_NAME'}"."?twi=b"."$tmp_unq_id"."p"."$tmp_seq_no"."p"."$disp_page"."drfx";
		      $HTML5_PARAM{'thread_link'} 		=~ s/(\W)/sprintf("%%%02X", unpack("C", $1))/eg;
			  $HTML5_PARAM{'img_box_base_url'}	="$MYCGI_ENV{'img_box_base_url'}";
		      $HTML5_PARAM{'img_box_base_url'}	=~ s/(\W)/sprintf("%%%02X", unpack("C", $1))/eg;
		      $HTML5_PARAM{'token_time'} 		= substr(time,-7,2); #27.7時間単位

			  if($MYCGI_ENV{'flash_object_tag_support'} eq 'true'){
			    if($tmp_img_location=~ /\.flv$|\.f4v$|\.f4a$|\.f4b$|\.mp4$|\.mov$/i){
				$data_type=qq|<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" width="640" height="360" id="obj$tmp_unq_id">
				<param name="FlashVars" value="src=$HTML5_PARAM{'img_box_base_url'}&thread_link=$HTML5_PARAM{'thread_link'}&locale=ja_JP&tkn=$HTML5_PARAM{'token_time'}"/>
				<param name="allowfullscreen" value="true"/>
				<param name="play" value="true"/>
				<param name="allowscriptaccess" value="always"/>
				<param name="quality" value="AUTOHIGH"/>
				<param name="movie" value="http://s01-imgboardFLVPlayer.app-flash.com"/>
				<embed flashvars="src=$HTML5_PARAM{'img_box_base_url'}&thread_link=$HTML5_PARAM{'thread_link'}&locale=ja_JP&tkn=$HTML5_PARAM{'token_time'}" width="640" height="360" allowfullscreen="true" allowscriptaccess="always" src="http://s01-imgboardFLVPlayer.app-flash.com" type="application/x-shockwave-flash" />
				</embed>
				</object><BR>|;
				}
			  # imodeとHTML5で共通する書き方をしたいが。objectタグにすると、マイムの宣言エラーに厳しくなるのでやめた。
			  # http://www.html5.jp/html5doctor/the-video-element.html	
			  }elsif($HTTP_USER_AGENT=~ /^docomo/i){
			  # http://www.nttdocomo.co.jp/service/imode/make/content/imotion/mp4/distribution/index.html
#			    $HTML5_PARAM{'object_tag_type'}=&make_html5_mimetype('video',"$tmp_img_location");
			    if($tmp_img_location=~ /\.mp4$|\.3gp$/i){
				$data_type=qq|<object declare id="obj$tmp_unq_id" width="640" height="360" data="$MYCGI_ENV{'img_box_base_url'}" type="video/3gpp">
				</object><A href="#obj$tmp_unq_id">iモーション</A><BR>|;
				}
			  }else{
			    # HTML5 for iPhone/iPod/iPad
			    if($tmp_img_location=~ /\.mp4$|\.m4v$|\.mov$|\.3gp?p$|\.3g2$/i){
				# videoタグ記述
				# http://dev.opera.com/articles/view/introduction-html5-video/
				$data_type=qq|<video width="640" height="360" src="$tmp_img_location" id="obj$tmp_unq_id" controls poster>
				<p>HTML5のvideoに対応したブラウザーをご利用下さい</p>
				</video><BR>|;
				}
			  }
			}

			
			#危険度の高いデータの場合はIPを自動表示する
			undef $auto_user_IP;
			if(($auto_ip_if_danger_datatype==1)&&($disp_ip_flag ==1)){
				$auto_user_IP="（"."$user_IP"."）";
			}elsif($no_disp_RH_in_HTML_sorce=='-1'){
				$auto_user_IP="（"."$user_IP"."）";
			}else{
				$auto_user_IP="";
			}

			if($tmp_img_location ne ''){
				# 画像タイトルがない場合,画像名をタイトルに
				$tmp_imgtitle = $tmp_img_location if $tmp_imgtitle eq '';
				$tmp_imgtitle =~ s/^(.*)\///;	# パスを消去して名前のみにする
	
			}

			undef $ddd;	#デバッグ用パラメータ
			undef %KIJI_LAYLOUT; #記事最適化用のレイアウト(回り込みレイアウト判断用）

			# 画像のサイズ変更
			if(($tmp_img_location!~ /\.dat$/)&&($tmp_img_location=~ /\.gif$|\.jpe?g$|\.png$|\.bmp$/i)){
				$KIJI_LAYLOUT{'exist_image'}=1;
				&check_img;
			# imgboard FLV Player 対策（ここで引っ掛けてリサイズする）
			}elsif($tmp_img_location=~ /\.flv$|\.f4v$|\.f4a$|\.f4b$|\.mp4$|\.3gp$/i){
					&check_flash_and_iframe_img('flash');
		    }else{
		    	# 埋め込みFlash動画のサイズ変更
				if($tmp_body=~ /<object(.|\n)*application\/x\-shockwave\-flash/i){
					&check_flash_and_iframe_img('flash');
				# 2011.02.04 ニコニコ外部埋め込み
				}elsif($tmp_body=~ /\.nicovideo\.jp\//i){
					&check_flash_and_iframe_img('ext_nicovideo');
				# 2011.12.15 YouTube/GoogleMap iframe埋め込み対応
				}elsif($tmp_body=~ /<iframe(.|\n)*src\=\"(https?\:\/\/|\/\/)/i){
					&check_flash_and_iframe_img('iframe');
				# 2014.02.14 Theta360埋め込み対応
				}elsif($tmp_body=~ /https?\:\/\/theta360\.com/i){
					&check_flash_and_iframe_img('ext_theta360');
				# 2014.02.24 FC2埋め込み対応
				}elsif($tmp_body=~ /<script(.|\n)*fc2.com\//i){
					&check_flash_and_iframe_img('script_fc2');
		    	}
		    }

			#=============================================================#
			# CGI別ディレクトリサイト、cgiwrapサイト対策(imgboard1.22 Rev.3)
			#=============================================================#

			# 互換性のため
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

			if(($tmp_img_location =~ /^\/(.+)\/(.+)$/)||($using_cgi_wrap==1)){
				# 絶対パス指定の場合はURL指定に変更
				if($using_cgi_wrap==1){
					$tmp_img_location=~ s/^(.+)\///g;
			    	}else{
					$tmp_img_location=~ s/^\/(.+)\///g;
			    	}

				$tmp_img_location="$img_url/$tmp_img_location";
			}


			# 自動URLリンクをする
			if($auto_url_link==1){
				$tmp_body=&set_auto_url_link($tmp_body);
			}

			# メールアドレスがある場合のみリンクにする
			if(($tmp_email ne " no_email")&&($tmp_email!~ /^(\s+)$/)){
			  $mail_a_start	="<A HREF=\"mailto:$tmp_email\">";
			  $mail_a_end	="</A>";
			}else{
			  $mail_a_start	="";
			  $mail_a_end	="";
			}

			# HTMLブロックの初期化
			undef $html_block_A;
			undef $size_sitei;
	
			undef $disp_seq_no;	

			# 携帯からの投稿の場合、種類を表示する
			undef $keitai_env_link;
			if($OPTDATA{'optKeitaiFlag'} ne ""){

			  # 2003.12 SoftBank対策
#			  if($OPTDATA{'optKeitaiMachineType'}=~ /v/i){
			   if($OPTDATA{'optKeitaiFlag'}=~ /J\-PHONE|SoftBank/i){
				$OPTDATA{'optKeitaiFlag'}="SoftBank";
	   		   }
#	  		  }

	  		  $keitai_env_link=qq|$OPTDATA{'optKeitaiFlag'}：$OPTDATA{'optKeitaiMachineType'}|;
			}

			if($tmp_seq_no ne ""){
				$disp_seq_no="No\."."$tmp_seq_no";
			}

			# html_block_Aに代入する要素を呼び出し（変更は初期設定でおこなう）
			&set_html_block;

			# 外部ファイル用の処理をロード
			# アイコン付き掲示板等に対応
			if($EXTSUB{'kiji'} == 1){
			 &ext_config_kiji;
			}

			# 2006.10 ダイジェストモードの障害回避 2011.06修正
	  		if(($tmp_body=~ /<object/i)||($tmp_body=~ /https?\:\/\/youtu\.be\//i)||($tmp_body=~ /nicovideo\.jp/i)||($tmp_body=~ /\<iframe/i)||($tmp_body=~ /\<script/i)){
			 $digest_flag=0;
			}

			# 2004.07 ダイジェストモードを追加
			if($digest_flag==1){
				$tmp_digest_limit=300;
				# 初期設定で設定した制限より長い場合 
				if(length($tmp_body) >$tmp_digest_limit){
 				 # 先頭から指定バイトまでのみ残す
				 $tmp_body =substr("$tmp_body",0,"$tmp_digest_limit");
				 $tmp_body .=" .... ";
				 if($child_kiji_flag != '1' ){	# 親の場合
				   $tmp_body .=" <BR>(<a href=\"$cgi_name?mode=search_menu&amode=$FORM{'amode'}&SearchWords=$tmp_unq_id\" target=_blank>このスレッドの全文を表\示</a>)";
				 }
				}
			}


			# 2008.08 レイアウト適正化
			if($child_kiji_flag != 1){
			  # 親記事にyoutubeタグ等が含まれる場合 (2011.06修正)
		  		if(($tmp_body=~ /<object/i)||($tmp_body=~ /https?\:\/\/youtu\.be\//i)||($tmp_body=~ /nicovideo\.jp/i)||($tmp_body=~ /\<iframe/i)||($tmp_body=~ /\<script/i)){
					$oya_kiji_embed_flag=1;
				}else{
					$oya_kiji_embed_flag=0;
				}
			}else{
		  		if(($tmp_body=~ /<object/i)||($tmp_body=~ /https?\:\/\/youtu\.be\//i)||($tmp_body=~ /nicovideo\.jp/i)||($tmp_body=~ /\<iframe/i)||($tmp_body=~ /\<script/i)){
					$child_kiji_embed_flag=1;
				}else{
					$child_kiji_embed_flag=0;
				}
			}

			# 準備終わり

	#------------------------------------------------------------------#
	# 記事部分のＨＴＭＬ(編集は初期設定部でおこなってください)
	# １．テキスト記事・・・・・&kiji_base_html;
	#
	# ２．画像のある記事の場合(３種類から選択)

	undef $disp_re;

	if($child_kiji_flag == '1' ){	# 子の場合
		$disp_re="";

# TODO親が画像をもっているスレッドで、子記事で自分に埋込み画像がなければ、親記事に回り込んで、コメントを表示したい

# 2012.10 HTML非推奨タグの互換性問題をCSSで改善
$br_auto_clear="<BR CLEAR=\"LEFT\" style=\"clear :left\">";

		if(($FORM{'mode'} eq "search_menu")&&($FORM{'SearchWords'} ne "$tmp_blood_name")){
		  print"<BR CLEAR=\"left\" style=\"clear: left\">\n";
		  #2004.05 検索時に親子関係が紛らわしいのでセパレータを追加
		  print"<HR SIZE=5>|\n";
		}

		# 2006.10.29 youTube対応

		# 子記事に画像、あるいはyoutubeタグが含まれる場合 (2008.08修正)
		if($oya_kiji_embed_flag == 1){
		  	if(($child_kiji_embed_flag == 1)||($KIJI_LAYLOUT{'exist_image'} == 1)){
			  print"<BR CLEAR=\"left\" style=\"clear: left\">\n";
		  	}else{
	
#			  print"<BR CLEAR=\"left\" style=\"clear: left\">\n";
		  	}
		  }else{
		  	if($child_kiji_embed_flag == 1){
			  print"<BR CLEAR=\"left\" style=\"clear: left\">\n";
		  	}else{
			  print"\n";
		  	}
		}

		# 2010.03 レイアウト改良(親の画像大きい場合は回り込む)
		# 親がデカイ場合は回り込み解除
		if($oya_kiji_img_width > 800){
			if($KIJI_LAYLOUT{'out_img_width'} > 100){
#				&error("oya over 800 $oya_kiji_img_width");
			  	print"<BR CLEAR=\"left\" style=\"clear: left\">\n";
			}
		}elsif($oya_kiji_img_width > 500){
			# 親＋子がデカイ場合は回り込み解除
			if($KIJI_LAYLOUT{'out_img_width'} > 300){
			  print"<BR CLEAR=\"left\" style=\"clear: left\">\n";
			}
		}

		print"<TABLE border=0>\n";
		print"<TR><TD NOWRAP ALIGN=RIGHT VALIGN=TOP $tmp_td_width>&gt&gt</TD><TD $res_table_sitei>\n";

	}else{				# 親の場合

		# 幅を指定する
		$tmp_td_width="";

# TODO子記事の上位３つ以下に埋込み画像がなければ、親記事はbr_clearしないで、コメントを回り込ませたい
$br_auto_clear="";
$oya_kiji_img_width="$KIJI_LAYLOUT{'out_img_width'}"; # グローバルで記憶
$oya_kiji_img_height="$KIJI_LAYLOUT{'out_img_height'}";# グローバルで記憶

		if(($disp_mode eq "text_only")||($disp_mode eq "img_icon")||($disp_mode eq "img_text_link")){
			$tmp_td_width=qq|WIDTH="7%"|;
		}

		if(($PM{'use_rep'} == 1)&&($FORM{'bbsaction'} ne 'disp_rep_form')&&($FORM{'amode'} ne 'select_edit')&&($FORM{'amode'} ne 'show_ip')){
		  $disp_re=qq|<a href="$cgi_name?bbsaction=disp_rep_form&amode=$FORM{'amode'}&page=$disp_page&blood=$tmp_unq_id&parent=$tmp_seq_no">返信</a>|;
		  if($PM{'use_twitter_link'} == 1){
		  # API変更に伴い修正 2011.06.08
		  # http://watcher.moe-nifty.com/memo/docs/twitterAPI.txt
			# 日本語は不可(UTF-8はPerl本体にモジュール追加が前提になり環境依存するため)
		    $disp_twia="IMAGE #imgboard "."$PM{'twitter_hash01'}"."$PM{'twitter_mes01'}"." http://"."$ENV{'SERVER_NAME'}"."$ENV{'SCRIPT_NAME'}"."?twi=b"."$tmp_unq_id"."p"."$tmp_seq_no"."p"."$disp_page"."drfx";
		    $disp_twia =~ s/(\W)/sprintf("%%%02X", unpack("C", $1))/eg;
		    $disp_re="$disp_re "." (<a href=\"http://twitter.com/?status="."$disp_twia"."\" target=\"twitter01\">t</a>)";
		  }
		}
		print"<BR CLEAR=\"left\" style=\"clear: left\">\n";
		# 2010.06 add iPhone/iPadでレイアウトが乱れる事があるのでさらに回り込み解除を重ねる
		if($HTTP_USER_AGENT=~ /ipod|iphone|ipad/i){
			print"<BR CLEAR=\"all\"  style=\"clear: left\">\n";
		}
		print"<HR>\n";
	}

	$disp_re="" if($old_kiji_flag == '1');# 旧形式なら返信リンクを出さない

	if($FORM{'bbsaction'} ne 'disp_rep_form'){
#	print"<INPUT TYPE=\"CHECKBOX\" NAME=\"rm_number_$tmp_rm_number\" VALUE=\"1\">\n";
	# R6 new
	# 旧連番 S 新固有IDを送る(Sはセパレータ)
	$mes_rmid="rmid"."$tmp_rm_number"."S"."$tmp_unq_id";
	$disp_rm_cbox=qq|<INPUT TYPE="CHECKBOX" NAME="$mes_rmid" VALUE="1">\n|;
	print "$disp_rm_cbox";
	 if($new_kiji_flag ==1){
	  print "<font color=red size=-1>(new)</font>";
	 }
	}

	print" <!--$disp_mode-->\n";

	# 子記事
	if($child_kiji_flag == '1' ){
		# 返信記事（書換えは初期設定の所で行う）
		&kiji_rep_html;
		print"</TD></TR></TABLE>\n";
	# 親記事
	}else{

	  if($disp_mode eq "text_only"){
		# テキスト記事（書換えは初期設定の所で行う）
		&kiji_base_html;
	  }elsif($disp_mode eq "img_icon"){
		# アイコン貼付け（書換えは初期設定の所で行う）
		$html_block_A="$icon_html_block";
		&kiji_base_html;
	  }elsif($disp_mode eq "img_auto"){
		# オートリサイズ貼付け（書換えは初期設定の所で行う）
		$size_sitei="$w_set $h_set";
		&kiji_base2_html;
	  }elsif($disp_mode eq "img_w_static"){
		# 横固定サイズ貼付け（書換えは初期設定の所で行う）
		$size_sitei="$w_set $h_set";
		&kiji_base2_html;
 	  }elsif($disp_mode eq "img_h_static"){
 		# 縦固定サイズ貼付け（書換えは初期設定の所で行う）
 		$size_sitei="$w_set $h_set";
 		$html_block_A="$icon_html_block";
 		&kiji_base_html;
	  }elsif($disp_mode eq "img_original"){
		# 元サイズ貼付け（書換えは初期設定の所で行う）
		$size_sitei="$w_set $h_set";
		if($FORM{'amode'} eq "remove_webparts"){
			&kiji_base_icon_html;
		}else{
			&kiji_base2_html;
		}
	  }elsif($disp_mode eq "img_limit_max"){
		# 最大サイズ制限貼付け（書換えは初期設定の所で行う）
		$size_sitei="$w_set $h_set";
		&kiji_base2_html;
	  }elsif($disp_mode eq "img_text_link"){
		# 画像はリンク
		$html_block_A="$textlink_html_block";	#（書換えは初期設定の所で行う）
		&kiji_base_html;
	  }else{
		# テキスト記事（書換えは初期設定の所で行う）
		&kiji_base_html;
	  }

	}
# 返信に入るためのリンク
if($FORM{'amode'} eq "select_edit"){

print<<HTML_END;
<BR>[<a href="$cgi_name?bbsaction=edit_form&target=$tmp_unq_id&target_no=$tmp_seq_no&p1=$FORM{'p1'}&p2=$FORM{'p2'}&page=$FORM{'page'}&amode=select_edit">\↑Modified the above article ↑Positive\</a>]
HTML_END

}	
	}
	}# forループの終了

	# 返信のときの参考記事用のＨＴＭＬ下部
	if($FORM{'bbsaction'} eq 'disp_rep_form'){
print<<HTML_END;
	<BR CLEAR="left" style="clear: left">
	</FORM>
	<HR>
	[<a href="$cgi_name?amode=$FORM{'amode'}&page=$FORM{'page'}">Back without reply</a>]
	</BODY></HTML>
HTML_END
	exit;
	}


	# フッターを表示

	# 下部にバナー広告を義務付けられている場合は、設定部の$html_for_bottom_bannerにHTMLソースを書いてください    


 	$dd_guest_passwd="$guest_passwd";

print<<HTML_END;
	<BR CLEAR="left" style="clear: left">
	<HR>
	$html_for_bottom_banner
	<INPUT TYPE="HIDDEN" NAME="bbsaction" VALUE="remove">
	<font size=-1>
	削除方法 <BR>
	◆Manager: Check the left column for the deletion target (multiple designation possible), enter the dedicated password in the lower column, and press "Delete". <BR>
HTML_END

	if($use_guest_passwd =='1'){

print<<HTML_END;
	◆Contributors: Access with the Contributor: Check the left column for the deletion target (multiple designation possible), enter the deletion key entered at the time of submission in the lower column, and press "Delete"..com you used to post your article, check the left column of your article and press "Delete" (no password required!).<BR>
HTML_END

        }elsif($use_guest_passwd =='-1'){
		$dd_guest_passwd="$COOKIE{'rmkey'}";
	 if($COOKIE{'rmkey'} ne ""){
print<<HTML_END;
	◆ Submitter: Check the left column for the deletion target (multiple designation possible), enter the deletion key entered at the time of submission in the lower column, and press "Delete" <BR>(If the key is memorized, it will be entered automatically).<BR>
HTML_END
	 }else{
print<<HTML_END;
	◆Contributor: Check the left column for the deletion target (multiple designation possible), enter the deletion key entered at the time of submission in the lower column, and press "Delete".<BR>
HTML_END
	 }
        }

print<<HTML_END;
	<INPUT TYPE="PASSWORD" NAME="passwd" SIZE="10" VALUE="$dd_guest_passwd">
	</font>
	<INPUT TYPE="SUBMIT" VALUE="削除">
	</FORM>
<BR>
<BR>
HTML_END

&output_button_HTML(1);
	
	# 改造,非改造を問わず,クレジットの変更は固くお断りします。（著作権侵害となります）
	# なお,当スクリプトの一部,あるいは全部を利用,あるいは参考にしたスクリプトを作成された場合も,
	# かならず当リンクをその掲示板に付加してください。
	print "<HR>\n";
	print "<DIV ALIGN=\"RIGHT\">";
	print "<B>FREE <A HREF=\"http:\/\/www.big.or.jp\/~talk\/welcome\/welcome7mey2.cgi?v=v04c\">imgboard R6.1v4c <\/A> (jp)!!<\/B><BR>\n";
	print "<\/DIV><BR>\n";
}

	print "<BR>\n"; # マルチタッチ非対応の拡大ボタン対策(XPERIA)
	print "<\/BODY>\n<\/HTML>\n";

}

#====================================#
# disp_mode（表示モード）を選択する
#====================================#

sub check_mode{		

	# テキストのみ
	if($tmp_img_location eq ""){
		$disp_mode="text_only";
	# データ付き
	}else{
		# ユーザがクッキーで表示モードを以前選択している場合,それを優先
		if(($COOKIE{'view_mode'} ne "")&&($COOKIE{'view_mode'} ne "as_cgi_defined")&&($user_selected_view_mode==1)){
			if(($tmp_img_location!~ /\.dat$/)&&($tmp_img_location=~ /\.gif$|\.jpe?g$|\.png$|\.bmp$/i)){
				$disp_mode="img_icon" if($COOKIE{'view_mode'} eq "text_img_type1");
				$disp_mode="img_w_static"  if($COOKIE{'view_mode'} eq "text_img_type2");
				$disp_mode="img_original"  if($COOKIE{'view_mode'} eq "text_img_type3");
				$disp_mode="img_auto"      if($COOKIE{'view_mode'} eq "text_img_type4");
				$disp_mode="img_limit_max" if($COOKIE{'view_mode'} eq "text_img_type5");				$disp_mode="img_text_link" if($disp_mode eq "");
			}else{
				$disp_mode="img_text_link";
			}

		# 以前選択してない場合,初期設定の通り
		}else{
			if(($show_img_on_board ==0)||($tmp_img_location=~ /\.dat$/)||($tmp_img_location!~ /\.gif$|\.jpe?g$|\.png$|\.bmp$/i)){
				# テキストリンク
				$disp_mode="img_text_link";
			}else{
			# ＢＢＳ上に直接貼付		# クッキー未使用時の固定指定 neko
				if($on_board_img_size==0){	# アイコン
					$disp_mode="img_icon";
				}elsif($on_board_img_size==1){	# オート
					$disp_mode="img_auto";
				}elsif($on_board_img_size==2){	# 横固定
					$disp_mode="img_w_static";
				}elsif($on_board_img_size==3){	# オリジナル
					$disp_mode="img_original";
				}elsif($on_board_img_size==4){	# 縦固定
					$disp_mode="img_h_static";
				}elsif($on_board_img_size==5){	# 極端に大きな画像のみ縮小
					$disp_mode="img_limit_max";
				}else{
					$disp_mode="img_icon";	# error時はアイコンにしとく
				}
			}
		}
	}
}
#
#==============================================#
# IMGプロパティ判別 ＆ 表示サイズ変更処理部
#==============================================#

# $disp_modeに従い、表示サイズの変更を実際に行うルーチン
sub check_img{

	$use_imgsize=1;

	undef $orig_width;
	undef $orig_height;
	undef $w_set;
	undef $h_set;
	# file.datにheight,width情報があるかどうかをチェック。
	if(($IMG_PARAMETERS{'width'}>2)&&($IMG_PARAMETERS{'height'}>2)&&($IMG_PARAMETERS{'hw_racio'}>1)){
		    $img_parameters_exist=1;
	}else{
		    $img_parameters_exist=0;
	}

	if(($use_imgsize ==1)&&($imgsize_lib_flag==1)){

		$check_img_location="$tmp_img_location";

# 記事投稿時に画像の高さ、幅情報を解析し、記事データと共に記録しておく。
# 表示時、解析結果が既に記録されている場合はimgsizeによる解析をスキップ。
# これにより画像解析回数を減らし負荷軽減すると共に、超高速レイアウトを
# 実現する。なお、imgsize.plには、file名をdummyとして通知。

		$check_img_location='dummy' if ($img_parameters_exist==1);

		if($disp_mode eq 'img_icon'){
		# アイコン化。引数３は基本サイズ（省略可）	
			&imgsize("$check_img_location",'iconize','4000');
		}elsif($disp_mode eq 'img_w_static'){
		# 横サイズ固定。引数３は横サイズ、引数４は最大縦limit（省略可）	
			# レイアウトを揃えることができる。	
			if($COOKIE{'viewport_set'}=~ /(\d{3,5})/){
			 if($1 > 2400){ #2560dot
			  &imgsize("$check_img_location",'static_width','1800','2400');
			 }elsif($1 >= 2048){	# 2048(QXGA)
			  &imgsize("$check_img_location",'static_width','1600','2048');
			 }elsif($1 >= 1920){	# 1920(FullHD)
			  &imgsize("$check_img_location",'static_width','1440','1920');
			 }elsif($1 >= 1600){	# 1600,1680等 横長PC
			  &imgsize("$check_img_location",'static_width','960','1280');
			 }elsif($1 >=  1366){	# 1366,1368,1440 横長 AV Note等
			  &imgsize("$check_img_location",'static_width','960','1280');
			 }elsif($1 >=  1280){	# 1280 横長Note等
			  &imgsize("$check_img_location",'static_width','800','1280');
			 }elsif($1 >  1024){	# 1152等(TVが多い)
			  &imgsize("$check_img_location",'static_width','640','960');
			 }elsif($1 == 1024){	# XGA
			  &imgsize("$check_img_location",'static_width','560','896');
			 }elsif($1 >= 960){		# XGA相当NoteやNetBook タブレット
			  &imgsize("$check_img_location",'static_width','480','896');
			 }elsif($1 >=  800){	# ゲーム機、MIDデバイス
			  &imgsize("$check_img_location",'static_width','384','512');
			 }else{
			  &imgsize("$check_img_location",'static_width','384','512');
			 }
			}else{
#2010.10.15 test			
#			  &imgsize("$check_img_location",'static_width','440','640');
			  &imgsize("$check_img_location",'static_width','640','960');
			}
		}elsif($disp_mode eq 'img_original'){
		# オリジナルサイズ。引数３は表示倍率(倍率変更可能)	
			&imgsize("$check_img_location",'x_per','100%');
		}elsif($disp_mode eq 'img_h_static'){
		# 縦サイズ固定。引数３は縦サイズ、引数４は最大横limit（省略可）
			# 以下パラメータで画像は1024x768画面でジャスト表示になる	
			if($COOKIE{'viewport_set'}=~ /(\d{3,5})/){
			 if($1 > 2400){ #2560dot
			  &imgsize("$check_img_location",'static_height','980','1800');
			 }elsif($1 >= 1920){	# 1920(FullHD)
			  &imgsize("$check_img_location",'static_height','900','1600');
			 }elsif($1 >= 1600){	# 1600,1680等 横長PC
			  &imgsize("$check_img_location",'static_height','810','1400');
			 }elsif($1 >=  1366){	# 1366,1368,1440 横長 AV Note等
			  &imgsize("$check_img_location",'static_height','680','1000');
			 }elsif($1 >=  1280){	# 1280 横長Note等
			  &imgsize("$check_img_location",'static_height','680','1000');
			 }elsif($1 >  1024){	# 1152等(TVが多い)
			  &imgsize("$check_img_location",'static_height','680','1000');
			 }elsif($1 == 1024){	# XGA
			  &imgsize("$check_img_location",'static_height','680','1000');
			 }elsif($1 >= 960){		# XGA相当NoteやNetBook タブレット
			  &imgsize("$check_img_location",'static_height','680','1000');
			 }elsif($1 >=  800){	# ゲーム機、MIDデバイス
			  &imgsize("$check_img_location",'static_height','480','780');
			 }else{
			  &imgsize("$check_img_location",'static_height','360','600');
			 }
			}else{
			  &imgsize("$check_img_location",'static_height','680','1000');
			}
		}elsif($disp_mode eq 'img_auto'){
		# インテリジェントオートリサイズ。引数３は面積系のパラメータ（省略可）
			if($COOKIE{'viewport_set'}=~ /(\d{3,5})/){
			 if($1 > 2400){ #2560dot
			 	&imgsize("$check_img_location",'auto_resize','600000000');
			 }elsif($1 >= 1920){	# 1920(FullHD)
				&imgsize("$check_img_location",'auto_resize','240000000');
			 }elsif($1 >= 1600){	# 1600,1680等 横長PC
				&imgsize("$check_img_location",'auto_resize','96000000');
			 }elsif($1 >=  1366){	# 1366,1368,1440 横長 AV Note等
				&imgsize("$check_img_location",'auto_resize','16000000');
			 }elsif($1 >=  1280){	# 1280 横長Note等
				&imgsize("$check_img_location",'auto_resize','12000000');
			 }elsif($1 >  1024){	# 1152等(TVが多い)
				&imgsize("$check_img_location",'auto_resize','7200000');
			 }elsif($1 == 1024){	# XGA
				&imgsize("$check_img_location",'auto_resize','6400000');
			 }elsif($1 >= 960){		# XGA相当NoteやNetBook タブレット
				&imgsize("$check_img_location",'auto_resize','3200000');
			 }elsif($1 >=  800){	# ゲーム機、MIDデバイス
				&imgsize("$check_img_location",'auto_resize','1600000');
			 }else{
				&imgsize("$check_img_location",'auto_resize','1600000');
			 }
			}else{
			 &imgsize("$check_img_location",'auto_resize','6400000');
			}
		}elsif($disp_mode eq 'img_limit_max'){
		# 極端に大きな画像のみ縮小。引数３は縦制限サイズ、引数４は横制限サイズ（省略可）
			if($COOKIE{'viewport_set'}=~ /(\d{3,5})/){
			 if($1 > 2400){ #2560dot
				&imgsize("$check_img_location",'limit_by_max_size','960','1800');
			 }elsif($1 >= 1920){	# 1920(FullHD)
				&imgsize("$check_img_location",'limit_by_max_size','960','1600');
			 }elsif($1 >= 1600){	# 1600,1680等 横長PC
				&imgsize("$check_img_location",'limit_by_max_size','640','1200');
			 }elsif($1 >=  1366){	# 1366,1368,1440 横長 AV Note等
				&imgsize("$check_img_location",'limit_by_max_size','640','900');
			 }elsif($1 >=  1280){	# 1280 横長Note等
				&imgsize("$check_img_location",'limit_by_max_size','640','900');
			 }elsif($1 >  1024){	# 1152等(TVが多い)
				&imgsize("$check_img_location",'limit_by_max_size','600','800');
			 }elsif($1 == 1024){	# XGA
				&imgsize("$check_img_location",'limit_by_max_size','560','720');
			 }elsif($1 >= 960){		# XGA相当NoteやNetBook タブレット
				&imgsize("$check_img_location",'limit_by_max_size','480','640');
			 }elsif($1 >=  800){	# ゲーム機、MIDデバイス
				&imgsize("$check_img_location",'limit_by_max_size','480','480');
			 }else{
				&imgsize("$check_img_location",'limit_by_max_size','480','480');
			 }
			}else{
				&imgsize("$check_img_location",'limit_by_max_size','480','480');
			}
		}

		$orig_width	= "$IMGSIZE{'width'}";
		$orig_height	= "$IMGSIZE{'height'}";
		$w_set= "width=$IMGSIZE{'out_width'}"		if($IMGSIZE{'out_width'} !=0);
		$h_set= "height=$IMGSIZE{'out_height'}"		if($IMGSIZE{'out_height'} !=0);

	# imgsize未使用時 or imgsize.plが見つからない場合 neko
	}else{
		if($disp_mode eq 'img_icon'){
		# アイコン化。
			$w_set= "width =60";
			$h_set= "height=45";
		}elsif($disp_mode eq 'img_w_static'){
		# 固定サイズ化
			$w_set= "width =256";
			$h_set= "height=192";
		}elsif($disp_mode eq 'img_original'){
		# オリジナルサイズ化	
			undef $w_set;
			undef $h_set;
		}
	}
	# 2010.03 add レイアウト改良
	if($w_set=~ /(\d+)/){
		$KIJI_LAYLOUT{'out_img_width'}= $1;
	}
	if($h_set=~ /(\d+)/){
		$KIJI_LAYLOUT{'out_img_height'}= $1;
	}
#&error("$KIJI_LAYLOUT{'out_img_width'}-$KIJI_LAYLOUT{'out_img_height'}  ");
}
#
#==============================================#
# Flashビデオやiframeの表示サイズ変更処理部
#==============================================#
# view_modeに従い、表示サイズの変更を実際に行うルーチン
sub check_flash_and_iframe_img{

	undef $orig_width;
	undef $orig_height;
	undef $w_set;
	undef $h_set;
	

		if((($COOKIE{'view_mode'} eq "")&&($show_img_on_board == 1))||($COOKIE{'view_mode'}=~ /as_cgi_defined$|text_img_type12$|text_img_type13$|text_img_type2$|text_img_type3$|text_img_type4$|text_img_type5$/i)){ #オート（おまかせ)

			if($COOKIE{'viewport_set'}=~ /(\d{3,5})/){
			 if($1 > 2400){ #2560dot
				&change_flash_and_iframe_embed_size('1920','1080');
			 }elsif($1 >= 2048){	# 2048(QXGA)
				&change_flash_and_iframe_embed_size('1440','810');
			 }elsif($1 >= 1920){	# 1920(FullHD)
				&change_flash_and_iframe_embed_size('1280','720');
			 }elsif($1 >= 1600){	# 1600,1680等 横長PC
				&change_flash_and_iframe_embed_size('854','480');
			 }elsif($1 >=  1366){	# 1366,1368,1440 横長 AV Note等
				&change_flash_and_iframe_embed_size('854','480');
			 }elsif($1 >=  1280){	# 1280 横長Note等
				&change_flash_and_iframe_embed_size('854','480');
			 }elsif($1 >  1024){	# 1152等(TVが多い)
				&change_flash_and_iframe_embed_size('640','360');
			 }elsif($1 == 1024){	# XGA
				&change_flash_and_iframe_embed_size('640','360');
			 }elsif($1 >= 960){		# XGA相当NoteやNetBook タブレット
				&change_flash_and_iframe_embed_size('640','360');
			 }elsif($1 >=  800){	# ゲーム機、MIDデバイス
				&change_flash_and_iframe_embed_size('480','270');
			 }else{
				&change_flash_and_iframe_embed_size('640','360');
			 }
			}else{
				&change_flash_and_iframe_embed_size('640','360');
			}
		}

		$orig_width		= "640";
		$orig_height	= "385";
		$w_set= "width=$tmp_cfds_width"		if($tmp_cfds_width!=0);
		$h_set= "height=$tmp_cfds_height"	if($tmp_cfds_height!=0);

	# 2010.03 add レイアウト改良
	if($w_set=~ /(\d+)/){
		$KIJI_LAYLOUT{'out_img_width'}= $1;
	}
	if($h_set=~ /(\d+)/){
		$KIJI_LAYLOUT{'out_img_height'}= $1;
	}
#&error("$KIJI_LAYLOUT{'out_img_width'}-$KIJI_LAYLOUT{'out_img_height'}  ");
}
#
#==================================#
# Flashビデオの埋込みサイズの変更 
#==================================#
# youtube,dailymotion,imgboard FLV playerに有効
# ストリートビューにも有効
#
sub change_flash_and_iframe_embed_size{

	$tmp_cfds_width 	= $_[0];# 引数 2 指定横サイズ
	$tmp_cfds_height	= $_[1];# 引数 3 指定縦サイズ
	
#TODO
# 16:9でなく、4:3埋め込みしたい動画サイトはここで指定 
@DOUGA_43_DOMAIN=('www.nicovideo.jp','video.fc2.com','xvideos.com');
	
	undef @TMP_DOUGA_43_DOMAIN;
	@TMP_DOUGA_43_DOMAIN=@DOUGA_43_DOMAIN; # 縦横4:3動画サイトドメイン

	if($COOKIE{'view_mode'}=~ /as_cgi_defined|text_img_type13/i){ #サムネイル-大小Mix
		if($child_kiji_flag == '1' ){	# 子の場合
			return(0);
		}
	}
	
	# iframeタグによる埋込みの場合 2011.06
	if(($tmp_body=~ /<iframe(.|\n)*src\=/i)||($tmp_body=~ /<object/i)){
		# youtubeの場合はGUI分調整 2011.06.08修正
		if($tmp_body=~ /\/\/www\.youtube\./i){
			$tmp_cfds_height = $tmp_cfds_height + 25 ;
		}
		# ustreamの場合は4:3にする
		if($tmp_body=~ /http\:\/\/www\.ustream\./i){
			$tmp_cfds_height = int( $tmp_cfds_width*0.75 ) + 26 ;
		}
	}

	# 特定のiframe埋め込みサイトは4:3にする

	# @TMP_DOUGA_43_DOMAINと一致したらOK
	local($ttmp_43_dmatch)=0; # matchフラグ
	foreach (@TMP_DOUGA_43_DOMAIN){
		next if($_ eq "");
    	# 正規表現をPerlパターンマッチへ変換
	    $w_pattern=&change_pattern_match($_);
		if($tmp_body=~ /$w_pattern/i){
			$ttmp_43_dmatch=1;
		}
	}
	# 4:3にする
	if($ttmp_43_dmatch == 1){
		$tmp_cfds_height = int( $tmp_cfds_width*0.75 ) + 16 ;
	}
	

	# width指定3つなら,想定外の影響を防ぐためにアボート
	if($tmp_body=~ /(\s)width(\s*)=(.|\n)*(\s)width(\s*)=(.|\n)*(\s)width(\s*)=/i){
		return(0);
	}

#&error("aayady");

	$tmp_body=~ s/(\s)width(\s*)=(\s*)(\"?)(\d+)(\%?)(\"?)/ width=\"$tmp_cfds_width\"/ig;
	
	if($tmp_body=~ /12px;float: left\"/i){
	 $tmp_body=~ s/(\s)height(\s*)=(\s*)(\"?)(\d+)(\%?)(\"?)/ height=\"$tmp_cfds_height\"/ig;
	}else{
	$tmp_body=~ s/(\s)height(\s*)=(\s*)(\"?)(\d+)(\%?)(\"?)/ height=\"$tmp_cfds_height\" align=\"left\" style=\"margin: 12px;float: left\"/ig;
	}

	# imgboard FLV Player対応 2010.06
	# objectタグによる埋込みの場合
	if($data_type=~ /<object(.|\n)*application\/x\-shockwave\-flash/i){
		$data_type=~ s/(\s)width(\s*)=(\s*)(\"?)(\d+)(\%?)(\"?)/ width=\"$tmp_cfds_width\"/ig;
		$data_type=~ s/(\s)height(\s*)=(\s*)(\"?)(\d+)(\%?)(\"?)/ height=\"$tmp_cfds_height\" align=\"left\"/ig;
	}

	# theta360対応 2014.02
	# blockquoteタグによる埋込みの場合
	if($tmp_body=~ /<blockquote(.|\n)*data\-width/i){
		if($tmp_body=~ /https?\:\/\/theta360\.com/i){
			# Thetaの場合は臨場感を増すためにシネマスコープ21:9にする
			$tmp_cfds_width = int( $tmp_cfds_width*1.31 ) ;
		}
		$tmp_body=~ s/(\s)data\-width(\s*)=(\s*)(\"?)(\d+)(\%?)(\"?)/ data\-width=\"$tmp_cfds_width\"/ig;
		$tmp_body=~ s/(\s)data\-height(\s*)=(\s*)(\"?)(\d+)(\%?)(\"?)/ data\-height=\"$tmp_cfds_height\"/ig;
	}

	# scriptタグによる埋込みの場合
	if($tmp_body=~ /<script(.|\n)*w\=/i){
		# FC2対応 2014.02
		$tmp_body=~ s/(\s)w=(\s*)(\"?)(\d+)(\%?)(\"?)/ w=\"$tmp_cfds_width\"/ig;
		$tmp_body=~ s/(\s)h=(\s*)(\"?)(\d+)(\%?)(\"?)/ h=\"$tmp_cfds_height\"/ig;
	}

	# 全チェック通過ならOK
	return(1);
}
#
#=========================================#
# 表示モード設定用/フォームＨＴＭＬ
#=========================================#

sub form_user_profile_html{

	local($tmp_page_disp)="$FORM{'page'}";
	$tmp_page_disp=1 if($tmp_page_disp eq "");

	# 返信の時は変更されるとパラメータが抜けてしまうので
	# 表示させない
	if($FORM{'bbsaction'} eq "disp_rep_form"){
		return;
	}

	# 検索の時は変更されるとパラメータが抜けてしまうので
	# 表示させない
	if($FORM{'mode'} eq "search_menu"){
		return;
	}

if($CIMGSIZE{'smooze_mode'} > 0){
	$yoko_sub_setumei=" をほぼ ";
}

if($COOKIE{'middle_html_disp'} == 1){
	$CHECKED_PARAM{'middle_html_disp'}="checked";
}else{
	$CHECKED_PARAM{'middle_html_disp'}="";
}

print<<HTML_END;
<!--訪問ユーザが個々にＢＢＳに画像埋込みするかどうかを判断．
希望ユーザにのみ画像を埋込み\表\示\する,-->
<FORM ACTION="$cgi_name" METHOD="POST" style="display: inline">	
<DIV align=right><INPUT TYPE="CHECKBOX" NAME="middle_html_disp" VALUE="1" $CHECKED_PARAM{'middle_html_disp'}><font size="+1"> 次回から説明省略(適用で反映)</font><HR>
<TABLE BORDER=1 CELLSPACING=2 CELLPADDING=1>
<TR $bgcolor_ie></TR>
<TR>
<TD WIDTH="8"></TD>
<TD bgcolor="gray">
<font size="-1" color="lightgreen">表\示モード <BR></font>
<INPUT TYPE="HIDDEN" NAME="bbsaction" VALUE="pf_change">
<INPUT TYPE="HIDDEN" NAME="page" VALUE="$tmp_page_disp">
<INPUT TYPE="HIDDEN" NAME="amode" VALUE="$FORM{'amode'}">
<INPUT TYPE="HIDDEN" NAME="p1" VALUE="$FORM{'p1'}">
<INPUT TYPE="HIDDEN" NAME="p2" VALUE="$FORM{'p2'}">
$POSTADDP{'DISPMODE'}
</TD>
<TD width="8"></TD>
<TD></TD>
<TD align=center>
<SELECT NAME="view_mode" $output_button_px>
<OPTION $selected_1 value="as_cgi_defined">管理者推奨に従う
<OPTION $selected_2 value="1-text_only">テキストのみ（軽い）
<OPTION $selected_3 value="text_img_type1">アイコンサイズ
<OPTION $selected_4 value="text_img_type2">横サイズ $yoko_sub_setumei 固定
<OPTION $selected_7 value="text_img_type5">大きいものだけ縮小
<OPTION $selected_5 value="text_img_type3">原寸表\示
<OPTION $selected_6 value="text_img_type4">オート（おまかせ）
</SELECT>
HTML_END

if(($COOKIE{'view_mode'} eq 'as_cgi_defined')||($COOKIE{'view_mode'} eq 'text_img_type2')||($COOKIE{'view_mode'} eq 'text_img_type4')){
print<<HTML_END;
<SELECT NAME="viewport_set" $output_button_px>
<OPTION $selected_01 value="as_cgi_defined">横幅値 (推奨ﾃﾞﾊﾞｲｽ)
<OPTION $selected_vps{'no'} value="">指定なし
<OPTION $selected_vps{'480'}  value="480">480
<OPTION $selected_vps{'640'}  value="640">640
<OPTION $selected_vps{'720'}  value="720">720
<OPTION $selected_vps{'768'}  value="768">768 (iPhone3GS)
<OPTION $selected_vps{'800'}  value="800">800  (Netbook)
<OPTION $selected_vps{'854'}  value="854">854
<OPTION $selected_vps{'864'}  value="864">864
<OPTION $selected_vps{'960'}  value="960">960 (iPhone4/4S)
<OPTION $selected_vps{'980'}  value="980">980
<OPTION $selected_vps{'1024'} value="1024">1024 (XGA/iPad)
<OPTION $selected_vps{'1136'} value="1136">1136 (iPhone5/5S)
<OPTION $selected_vps{'1152'} value="1152">1152
<OPTION $selected_vps{'1280'} value="1280">1280 (iPhone6/Galaxy系)
<OPTION $selected_vps{'1368'} value="1368">1368 (Note PC)
<OPTION $selected_vps{'1440'} value="1440">1440
<OPTION $selected_vps{'1600'} value="1600">1600
<OPTION $selected_vps{'1680'} value="1680">1680
<OPTION $selected_vps{'1920'} value="1920">1920 (ﾌﾙHD)
<OPTION $selected_vps{'2048'} value="2048">2048 (QXGA)
<OPTION $selected_vps{'2560'} value="2560">2560
<OPTION $selected_vps{'device-width'} value="device-width">Dot by Dot
<OPTION $selected_vps{'auto'} value="auto">AUTO
</SELECT>
</TD><TD>
HTML_END
}else{
print<<HTML_END;
<INPUT TYPE="HIDDEN" NAME="viewport_set" VALUE="$COOKIE{'viewport_set'}">
HTML_END
}

print<<HTML_END;
<INPUT TYPE="HIDDEN" NAME="entry_passwd" VALUE="$COOKIE{'entry_passwd'}">
<INPUT TYPE="HIDDEN" NAME="name"  VALUE="$COOKIE{'name'}">
<INPUT TYPE="HIDDEN" NAME="email" VALUE="$COOKIE{'email'}">
<INPUT TYPE="HIDDEN" NAME="subject" VALUE="$COOKIE{'subject'}">
<INPUT TYPE="HIDDEN" NAME="imgtitle" VALUE="$COOKIE{'imgtitle'}">
<INPUT TYPE="HIDDEN" NAME="form_mode" VALUE="$COOKIE{'form_mode'}">
<INPUT TYPE="HIDDEN" NAME="utc" VALUE="$COOKIE{'utc'}">
<INPUT TYPE="HIDDEN" NAME="optA" VALUE="$COOKIE{'optA'}">
<INPUT TYPE="HIDDEN" NAME="optB" VALUE="$COOKIE{'optB'}">
<INPUT TYPE="HIDDEN" NAME="optC" VALUE="$COOKIE{'optC'}">
<INPUT TYPE="HIDDEN" NAME="optD" VALUE="$COOKIE{'optD'}">
<INPUT TYPE="HIDDEN" NAME="rmkey" VALUE="$COOKIE{'rmkey'}">
<INPUT TYPE="HIDDEN" NAME="rmkeym" VALUE="$COOKIE{'rmkeym'}">
<input ID="btnVS1" type=submit value="適用" $output_button_px>
<!-- $vip_n --></TD>
</FORM>
</TR>
</TABLE>
</DIV>
<HR>
HTML_END
}
#
#====================================================#
# 上記フォームにおいて、デフォルトのボタン位置を指定
#====================================================#

sub select_default_view_mode{

		if($COOKIE{'view_mode'} eq "as_cgi_defined"){
			$selected_1='selected';
		}elsif($COOKIE{'view_mode'} eq "1-text_only"){
			$selected_2='selected';
		}elsif($COOKIE{'view_mode'} eq "text_img_type1"){
			$selected_3='selected';
		}elsif($COOKIE{'view_mode'} eq "text_img_type2"){
			$selected_4='selected';
		}elsif($COOKIE{'view_mode'} eq "text_img_type3"){
			$selected_5='selected';
		}elsif($COOKIE{'view_mode'} eq "text_img_type4"){
			$selected_6='selected';
		}elsif($COOKIE{'view_mode'} eq "text_img_type5"){
			$selected_7='selected';
		}else{
			$selected_1='selected';
		}

		if($COOKIE{'viewport_set'} eq "as_cgi_defined"){
#			$selected_01='selected';
			$selected_vps{'1024'} = 'selected';
		}elsif($COOKIE{'viewport_set'} =~ /(\d{3,4})/i){
			$selected_vps{$1}='selected';
		}elsif($COOKIE{'viewport_set'} =~ /device\-width/i){
			$selected_vps{'device-width'}='selected';
		}elsif($COOKIE{'viewport_set'} =~ /no/i){
			$selected_vps{'no'}='selected';
		}elsif($COOKIE{'viewport_set'} =~ /auto/i){
			$selected_vps{'auto'}='selected';
		}else{
			$selected_01='selected';
		}
}
#
#=====================================================#
# その他のサブルーチン
#=====================================================#
#
#=========================#
# フォームのチェック
#=========================#

sub form_check{

	local($crypt_RH)=$REMOTE_HOST;

	foreach $form(sort keys %FORM){

		# フォームの整形
		# タグ禁止の場合
		if($use_tag !=1){
			$FORM{$form} =~ s/</&lt;/g;		# タグ禁止
			$FORM{$form} =~ s/>/&gt;/g;		# タグ禁止


			# Style指定	禁止
			$FORM{$form} =~ s/style(\s*)=(.|\n)*/
			Sorry..You can not use style in comment./ig;

		}else{
		# タグ許可の場合

# (掲示板イタズラ対策) 各種危険タグを除去

# 2011.12.14 XSS対策で修正
if(($FORM{$form}=~ /</)||($FORM{$form}=~ /%3C/i)||($FORM{$form}=~ />/)||($FORM{$form}=~ /%3E/i)){
# タグがあった場合のみチェックする(高速化)
$FORM{$form} =~ s/<!--(.|\n)*-->//g;			# SSI等	除去
$FORM{$form} =~ s/<IM(A?)G(E?)(\s|\n)*SRC(.|\n)*\.(cgi|pl)(\s*)>/ig
Sorry..You can not load IMG tag CGI in comment./ig;	# IMGタグ CGI	除去
$FORM{$form} =~ s/<(\/?)COMMENT(.|\n)*>(\s*)(\n?)/
Sorry..You can not use COMMENT tag in comment./ig;	# COMMENTタグ	除去
$FORM{$form} =~ s/ActiveXObject/
Sorry..You can not use ActiveXObject in comment./ig;# ActiveXObject	除去
$FORM{$form} =~ s/document\.cookie/
Sorry..You can not use cookie in comment./ig;		# 不正クッキー参照	除去
$FORM{$form} =~ s/<(\/?)BGSOUND(.|\n)*>(\s*)(\n?)/
Sorry..You can not use BGSOUND tag in comment./ig;	# BGSOUND	除去
$FORM{$form} =~ s/(<|%3C)(\/?)FORM(.|\n)*(>|%3E)(\s*)(\n?)/
Sorry..You can not use FORM tag in comment./ig;		# FORM		除去
$FORM{$form} =~ s/<(\/?)MARQUEE(.|\n)*>(\s*)(\n?)/
Sorry..You can not use MARQUEE tag in comment./ig;	# マーキー	除去
$FORM{$form} =~ s/(<|%3C)(\/?)INPUT(.|\n)*(>|%3E)(\s*)(\n?)/
Sorry..You can not use FORM element tag in comment./ig;# FORM要素	除去
$FORM{$form} =~ s/(<|%3C)(\/?)SELECT(.|\n)*(>|%3E)(\s*)(\n?)/
Sorry..You can not use FORM element tag in comment./ig;# SELECTタグ	除去
$FORM{$form} =~ s/(<|%3C)(\/?)applet(.|\n)*(>|%3E)(\s*)(\n?)/
Sorry..You can not use JAVA in comment./ig;		# APPLET 除去
$FORM{$form} =~ s/(<|%3C)META(.+)Refresh(.|\n)*(>|%3E)(\s*)(\n?)//ig;#METAタグ飛ばし禁止
# youTubeの埋め込みで対応
# embed とか、objectタグは危険なので、チェックは厳密にする
if(($use_youtube_tag_in_comment == 1)&&($form=~ /body/i)&&($FORM{$form}=~ /application\/x-shockwave-flash/i)){
 if(&check_youTube_tag("$FORM{$form}","$yt_check_level")==1){
	# チェック免除

 }else{
$FORM{$form} =~ s/(<|%3C)(\/?)OBJECT(.|\n)*(>|%3E)(\s*)(\n?)/
Sorry..You can not use OBJECT tag in comment./ig;	# OBJECT(ActiveX) 除去
$FORM{$form} =~ s/(<|%3C)(\/?)EMBED(.+)SRC(.|\n)*(>|%3E)(\s*)(\n?)/
Sorry..You can not use EMBED tag in comment./ig;	# EMBEDタグ	除去
 }

# 基本は禁止
}else{
$FORM{$form} =~ s/(<|%3C)(\/?)OBJECT(.|\n)*(>|%3E)(\s*)(\n?)/
Sorry..You can not use OBJECT tag in comment./ig;	# OBJECT(ActiveX) 除去
$FORM{$form} =~ s/(<|%3C)(\/?)EMBED(.+)SRC(.|\n)*(>|%3E)(\s*)(\n?)/
Sorry..You can not use EMBED tag in comment./ig;	# EMBEDタグ	除去
}

# iframeタグのチェック 2011.06
# youtube,Dailymotion,ustream,nicovideoなどを許可する
if(&check_iframe_tag("$FORM{$form}","$yt_check_level")==1){
	# チェック免除

# 基本は禁止
}else{
$FORM{$form} =~ s/(<|%3C)(\/?)iframe(.|\n)*(>|%3E)(\s*)(\n?)/
Sorry..You can not use IFRAME tag in comment./ig;	# IFRAMEタグ	除去
}

# scriptタグのチェック（sub check_script_tagとして独立させた）
# ニコニコの外部プレイヤー埋め込みとリコーTheta360等で発火する
if(&check_script_tag("$FORM{$form}","$yt_check_level")==1){
	# チェック免除(実際はこのケースはない)
}else{
# 2011.12.14 XSS対策で修正
$FORM{$form} =~ s/(<|%3C)(\/?)script(.|\n)*(>|%3E)(\s*)(\n?)/
Sorry..You can not use SCRIPT tag in comment./ig;	# Javascript,VBscript 除去
}

$FORM{$form} =~ s/(<|%3C)(\/?)SERVER(.|\n)*(>|%3E)(\s*)(\n?)/
Sorry..You can not use SERVER tag in comment./ig;	# SERVERタグ	除去
$FORM{$form} =~ s/<(\/?)plaintext(.|\n)*>(\s*)(\n?)/
Sorry..You can not use plaintext tag in comment./ig;	# PLAINTEXTタグ	除去
$FORM{$form} =~ s/<(\/?)xmp(.|\n)*>(\s*)(\n?)/
Sorry..You can not use xmp tag in comment./ig;		# XMPタグ	除去
$FORM{$form} =~ s/<(\/?)strike(.|\n)*>(\s*)(\n?)/
Sorry..You can not use strike tag in comment./ig;	# STRIKEタグ	除去
$FORM{$form} =~ s/<s>/
Sorry..You can not use strike tag in comment./ig;	# STRIKEタグ	除去
$FORM{$form} =~ s/<(\/?)listing(.|\n)*>(\s*)(\n?)/
Sorry..You can not use listing tag in comment./ig;	# LISTINGタグ	除去
$FORM{$form} =~ s/(<|%3C)(\/?)BODY(.|\n)*(>|%3E)(\s*)(\n?)/
Sorry..You can not use BODY tag in comment./ig;		# BODYタグ	除去
$FORM{$form} =~ s/<(\/?)TITLE(.|\n)*>(\s*)(\n?)/
Sorry..You can not use TITLE tag in comment./ig;	# TITLEタグ	除去
$FORM{$form} =~ s/<(\/?)BASEFONT(.|\n)*>(\s*)(\n?)/
Sorry..You can not use BASEFONT tag in comment./ig;	# BASEFONTタグ	除去
$FORM{$form} =~ s/(<|%3C)(\/?)frame(.|\n)*(>|%3E)(\s*)(\n?)/
Sorry..You can not use FRAME tag in comment./ig;	# FRAMEタグ	除去
$FORM{$form} =~ s/(<|%3C)(\/?)HTML(.|\n)*(>|%3E)(\s*)(\n?)/
Sorry..You can not use HTML tag in comment./ig;		# HTML閉タグ	除去
$FORM{$form} =~ s/(\/?)COMMENT(.|\n)*>(\s*)(\n?)/
Sorry..You can not use COMMENT tag in comment./ig;	# COMMENTタグ	除去
	}
# タグがあってもなくても調べる
#unless(($form eq "body")||($form eq "subject")||($form eq "view_mode")||($form eq "name")){
if($FORM{$form} =~ /style(\s*)(\=|%3d)(.|\n)*font\-size:(\s*)(\d+)px/){
 if($4 > 48){
$FORM{$form} =~ s/style(\s*)(\=|%3d)(.|\n)*/
Sorry..You can not use style in tag on comment./ig;	# Style指定	禁止
 }
}
if($FORM{$form} =~ /style(\s*)(\=|%3d)(.|\n)*script/){
$FORM{$form} =~ s/style(\s*)(\=|%3d)(.|\n)*script/
Sorry..You can not use style in tag on comment./ig;	# Style指定	禁止
}
# visibility悪用等
if($FORM{$form} =~ /style(\s*)(\=|%3d)(.|\n)*bility/){
$FORM{$form} =~ s/style(\s*)(\=|%3d)(.|\n)*bility/
Sorry..You can not use style in tag on comment./ig;	# Style指定	禁止
}

# アダルト動画サイトタグのチェック
#&check_douga_tag("$FORM{$form}");

$FORM{$form} =~ s/(.|\n)*(onClick|onblur|onchange|onmouse|onError|onload|onfocus|onselect|onsubmit|onunload|onreset|onabort|ondblclick|onkey|ondragdrop)(\w{0,8})(\s*)(\=|%3d)/
(imgboardセキュリティ保護システム)Sorry..You can not use char <B><font color=red>$2<\/font><\/B> in comment./ig;	# onClick等javascriptイベントを除去(クロスサイトスクリプティング対策)
#}
#危険タグ除去ここまで
			# IMGタグの埋込みを可否？
			if($use_img_tag_in_comment !=1){
#				$FORM{$form} =~ s/<IM(A?)G(E?)(\s|\n)*SRC(.|\n)*>(\s*)(\n?)/Sorry..You can not use IMG tag in comment./gi;#IMGタグ除去
				$FORM{$form} =~ s/<IM(A?)G(E?)(\s|\n)*SRC(.|\n)*?>/Sorry..You can not use IMG tag in comment./gi;#IMGタグ除去
			}else{
			# IMGタグを埋込む場合は外部画像画像であることを明記する。
				if(($form eq 'body')&&($FORM{$form}=~ /<IMA?GE?(\s)*SRC(.*)>/i)){
					$FORM{$form} =~ s/ALT(\s)*=(\s)*\"(.+)\"/ /ig;	#ALT除去
					$FORM{$form} =~ s/ALT(\s)*=(\s)*([^>]+)/ /ig;	#ALT除去
					$FORM{$form} =~ s/border(\s)*=(\s)*([^>]+)/ /ig;#Border除去
					$FORM{$form} =~ s/<IMA?GE?\s*SRC\s?=\s*(\S*)(\s*)>/<IMG SRC=$1 ALT="この画像は外部ＷＷＷサーバの画像です" Border=0>外部画像 /ig;
				}
			}
		}
		$FORM{$form} =~ s/\r//g;		#CR除去
		$FORM{$form} =~ s/\n/<BR>/g;		#LFを<BR>に
		$FORM{$form} =~ s/\t//g;		#TABの除去
	}

	# フォームの値を代入
	$name      	= "$FORM{'name'}";
	$email     	= "$FORM{'email'}";
	$subject   	= "$FORM{'subject'}";
	$body      	= "$FORM{'body'}";
	$rmkey		= "$FORM{'rmkey'}";
	$imgtitle 	= "$FORM{'imgtitle'}";
	$img_location	= "$img_dir/$new_fname" if $new_fname ne '';

	#<フォームの有無のチェック>
	# 基本的にチェックする。ただし、プロファイル登録だけを行う
	# ユーザの場合は名前やemailをチェックしない。
	if($FORM{'bbsaction'} ne 'pf_change'){
		&check_form_data_exist;
	}

	#<総改行のチェック> 2004.05
	# 無意味な連続改行対策で、総行数をチェックする。
	if($limit_body_cols_flag ==1){
#		&check_max_cols($body,$body_text_max_cols);
	}

	# 2011.09 youbu.be埋め込み二つならアボート
	if($body=~ /youtu\.be(.|\n)*youtu\.be/i){
		&error(" エラー。youtu.beのURLは複数埋め込みできません。ひとつにしてください。 ");
	}

	# 2013.02 mailアドレスがある場合は、おそらくスパムなのでアボート
	if(($PM{'no_post_by_form_email_post'} == 1)&&($email ne '')){
		&error(" エラー。スパムの疑いがあるので、投稿が失敗しました。 ");
	}

	$name	 =' 無名 '      if $name eq '';
	$email   =' no_email'   if $email eq '';
	$subject =' 無題 '      if $subject eq '';
	$body    =' 本文なし '  if $body eq '';
	$rmkey  ='no_key'  	if $rmkey eq '';

# 追加項目に未記入の場合のデフォルト値は以下の書き方を参考にしてください
#	$FORM{'optA'} =' 無題 '      if $FORM{'optA'} eq '';

	# 本文にユーザ情報を含める

	# 暗号化
 	if($crypt_RH ne ""){
		$crypt_RH=&tiny_encode("$crypt_RH");
	}
	$body    = "$body<!-- user： $crypt_RH-->";

        # いたずら防止 (99/12/01 追加分)
        $email   =~ s/"/&quot;/g;
        $email   =~ s/style(\s*)=(.|\n)*//ig;
	
	if($PM{'use_trip_flag'}==1){

		# 修正記事選択画面なら偽判定しない
		if(($FORM{'amode'} eq "select_edit")&&($FORM{'bbsaction'} ne "edit_form")){
		# 通常なら偽判定する
		}else{
	  		$name =~ s/◆/◇偽/g; # 偽物は白◇にする
		}

		#2010.02 trip機能(なりすまし防止)をつける
		if($name=~ /^(.+)\#(.+)$/g){
			$name		=$1;
			$trip_plain =$2;
			$trip_plain 	=~ s/　//g;# 全角フィルタ
			$trip_plain 	=~ s/\s//g;
 		
			if($trip_plain ne ""){
		 		$trip_plain=substr($trip_plain,1,8);
		 	$salt=substr($trip_plain,2,2);
		 	$salt =~ s/[^\.-z]/\./go;
		 	$salt =~ tr/:;<=>?@[\\]^_`/ABCDEFGabcdef/;
		 	$trip = crypt($trip_plain,$salt);
		 	$trip = substr($trip,-5);
		 	$trip = '◆'."$trip";
		 	$name="$name"."$trip";
#&error("$name");
			}
		}
	}
	
	undef $p_key;	
	foreach $p_key(keys %FORM){
		if($p_key=~ /^opt/){
			$FORM{$p_key}=~ s/style(\s*)=(.|\n)*//ig;
			$FORM{$p_key}=~ s/"/&quot;/g;
		}
	}
}
#
#========================#
# 暗号化パスワードを作成
#========================#
#
sub make_pass{

	local($plain) = @_;# 引数
	local($salt);
	local($tmp_pass);

	# 2002.02 UPDATE
	if($PM{'use_crypt'} != 1){
		return($plain);
	}

	$salt="$ENV{'PROCESSOR_REVISION'}"."$plain";
	if($plain=~ /^ZzZ/){	# 2重暗号化を防ぐ
		$tmp_pass = "$plain";
	}elsif($plain=~ /^(\s*)$/){
		$tmp_pass = "";
	}else{
		$tmp_pass = crypt($plain, $salt);
		$tmp_pass = "ZzZ"."$tmp_pass";
	}
	return ($tmp_pass);
}
#
sub tiny_encode{
	local($plain) = @_;# 引数
	 return($plain) if($plain=~ /\,/);
  	 $plain =~ s/n/\,/ig;
    	 $plain =~ tr/a-m/b-n/;
   	 $plain =~ tr/A-M/B-N/; # 2002.12 自宅サーバ対応で追加
  	 $plain =~ s/\,/a/ig;
   	 $plain =~ s/4/\,/g;
    	 $plain =~ tr/0-3/1-4/;
  	 $plain =~ s/\,/0/g;
 	 $plain ="T-Enc"."$plain";
	 return($plain);
}

sub tiny_decode{
	local($plain) = @_;# 引数
	 if($plain=~ /T-Enc(.*)$/){
	  $plain = $1;
	  $plain =~ s/a/\,/ig;
    	  $plain =~ tr/b-n/a-m/;
   	  $plain =~ tr/B-N/A-M/; # 2002.12 自宅サーバ対応で追加
  	  $plain =~ s/\,/n/ig;
   	  $plain =~ s/0/\,/g;
    	  $plain =~ tr/1-4/0-3/;
  	  $plain =~ s/\,/4/g;
	 }
	 return($plain);
}
#===============================#
# フォームの入力項目のチェック
#===============================#
# 2001.03.11 返信に対応
# 2001.09.20 エラーメッセージを設定エリアへ移動
# 2002.06.07 画像を必須にした時に、記事の修正でエラーが出るバグに対処
#
sub check_form_data_exist{
#
	# 予備パラメータを必須にした場合のためのエラー
	local($tmp_p_key);
	foreach $p_key(keys %CHECK){
	  if($CHECK{$p_key} == 1 ){
	   if($p_key=~ /opt(.+)$/){
	    $tmp_p_key="opt"."$1";
	    if($FORM{$tmp_p_key} eq  ''){
		$error_message .= "$CHECK_E{$p_key}";
	    }
	   # 添付画像のエラーは、必須設定なのに
	   # 画像がなくて、親の時だけエラーを出す
	   # 修正画面の時は、エラーを出さない(2002.06.07)
	   }elsif($p_key eq "img"){
	    if(($img_data_exists != '1')&&($FORM{'parent'} eq "")&&($FORM{'prebbsaction'} ne 'edit_form')){
		$error_message .= "$CHECK_E{'img'}";
	    }
	   }else{
	    if($FORM{$p_key} eq  ''){
		$error_message .= "$CHECK_E{$p_key}";
	    }
	   }
	  }
	}
}
#
#==========================================#
# フォームの入力項目の省略可・必須を自動表示
#==========================================#
#
sub auto_omit_disp{

	# パラメータデフォルトを指定
	if($auto_disp_omit_frag ne '1'){
		$auto_disp_omit_frag=0;
	}
	local($html_h)="<font $f_param>*必要</font>"; 		# 必須の場合
	local($html_s)="<font $f_param>*省略可</font>";  	# 省略可能な場合
	if($auto_disp_omit_frag eq "1"){
		foreach (keys %CHECK){
		    if($CHECK{$_}==1){
			$DISP_OMIT{$_} .="$html_h";
		    }else{
			$DISP_OMIT{$_} .="$html_s";
		    }
		}
	}
}
#
#============================#
# 登録会員パスワードチェック
#============================#
# 会員パスが一致しないときだけ、エラーを出してアボートする
# 2002.03.24 update
# 会員パスワードを複数設定できるようにした
sub check_entry_passwd{

	local($w_pattern);

	# 会員パスワードチェック
	if($use_passwd_flag==1){

	  # 管理者パスでも投稿できるようにした
	  if(&check_passwd("$FORM{'entry_passwd'}","$admin_passwd","0")==1){
		return;
	  }
	  
	  # 返信はパスワード不要の場合、スキップ
	  if(($PM{'res_no_passwd_flag'}== 1)&&($FORM{'prebbsaction'} eq 'disp_rep_form')){
		return;
	  }
	  
	  if("$FORM{'entry_passwd'}" eq ""){
	    &error(" 会員パスワードを入力してください．投稿はキャンセルされました．","","1");
	  }

	  if($member_passwd ne ""){ # 過去ルーチン互換にする
		push(@MEMBER_PASSWD,$member_passwd);
	  }
	  foreach (@MEMBER_PASSWD){
	    $w_pattern="$_";
	    if($w_pattern ne ""){
	     if(&check_passwd("$FORM{'entry_passwd'}","$w_pattern","0")==1){
		return;
	     }
	    }
	 }
	 &error(" 会員パスワードが違います．投稿できませんでした．","","1");
	}
}
#
#============================#
# パスワード照合
#============================#
# 2002.04.01 UPDATE
# 引数1,2を照合する。一致なら1,不一致なら2が返る
sub check_passwd{

	local($cp1_passwd)=$_[0];	# 引数1として取得
	local($cp2_passwd)=$_[1];	# 引数2として取得
	local($match_level)=$_[2];	# 厳密さ（１なら厳密）
	local($cpt_cp1_passwd);		# 引数1を暗号化したもの
	local($cpt_cp2_passwd);		# 引数2を暗号化したもの

	$cpt_cp1_passwd=&make_pass($cp1_passwd);
	$cpt_cp2_passwd=&make_pass($cp2_passwd);

	# パスワード照合
	# 厳密
	if($match_level == 1){
	 if($cp1_passwd eq "$cp2_passwd"){
		return 1;
	 }else{
		return 2;
	 }
	}


	# 普通
	if($cp1_passwd eq "$cp2_passwd"){
		return 1;
	}elsif($cp1_passwd eq "$cpt_cp2_passwd"){
		return 1;
	}elsif($cpt_cp1_passwd eq "$cp2_passwd"){
		return 1 ;
	}elsif($cpt_cp1_passwd eq "$cpt_cp2_passwd"){
		return 1 ;
	}else{
		return 2;
	}
}
#
#=======================================#
# 掲示板荒し対策２(1.22Rev6 機能強化版)
#=======================================#

sub protect_from_BBS_cracker{
#
# （悪質掲示板荒らし対策です）
#
# 相手のプロバイダ名により登録を禁止．(悪質掲示板荒らし対策)
# 禁止したいユーザのいるプロバイダ名の一部を,で区切って""で囲み、
# @BLACK_LISTに入力．(リストは初期設定のところにあります)．マッ
# チするとそのユーザは登録できなくなります．
#
# 禁止単語による制限機能を追加しました。ホスト名を頻繁に変更する
# 相手等、高度な「荒し技」を持つ相手からのイタズラが続く場合に、これを
# 使ってください。 リストは初期設定のところにあります。

       undef $bad_user_flag;
	local($error_mes_bl);
	local($error_mes_type);
	local($w_pattern);

	# デフォルトのダミーエラーメッセージ
	$error_mes_bl="CGI error 223458 BLT Default";

	#外部のブラックリストファイル（ホスト名）を読込む
	if($use_ext_blacklist ==1){
	  $add_black_count=&load_ext_list('blacklist.txt','BLACK_LIST');
	}

	#外部のブラックリストファイル（禁単語）を読込む
	if(($use_ext_blacklist ==1)&&($PM{'no_upload_by_black_word'}==1)){
	  $add_black_word_count=&load_ext_list('blkword.txt','BLACK_WORD');
	}

	#外部のスパムリストファイル（ホスト名）を読込む
	if($use_ext_spamlist ==1){
	  $add_spam_count=&load_ext_list('spamlist.cgi','SPAM_HOSTS_IP');
	}

	#外部のスパムリストファイル（禁単語）を読込む
	if($use_ext_spamlist ==1){
	  $add_spam_word_count=&load_ext_list('spamword.cgi','SPAM_WORD');
	}

	foreach (@BLACK_LIST){
	    next if($_ eq "");
	    # 正規表現をPerlパターンマッチへ変換
	    $w_pattern=&change_pattern_match($_);
		if($REMOTE_HOST=~ /$w_pattern/i){
			if($no_disp_for_cracker==1){	# 荒し対策
				&error(" CGIエラー．<!-- $add_black_count --> ");
			}else{
				&error(" CGIエラー．投稿できませんでした． ");
			}
		}
	}

 	# 投稿時以外(view時など)は、ホスト名以外のフィルタはスキップして負荷軽減（ここから）
	if(($FORM{'bbsaction'} eq 'post')&&($FORM{'amode'} ne "select_edit")){

	# 2006.03 add 掲示板SPAM対策
	# 2006.04 修正
	if(($limit_bbs_spam_flag==1)&&($FORM{'amode'} eq "")){
		if($FORM{'sf'} eq "$spam_keyword"){
			# OK
		}else{
			&error(" CGIエラー500．投稿できませんでした． ");
		}

		# 2010.02 onetime_tokenによるSPAM対策
		if($FORM{'onetime_token'} eq "$uniq_token"){
#&error("同じtoken  ttmp_uniq_char $ttmp_uniq_char--$FORM{'onetime_token'} - $uniq_token");
		}elsif($FORM{'onetime_token'} eq "$uniq_token_old"){
#&error("一つ前token ttmp_uniq_char $ttmp_uniq_char--$FORM{'onetime_token'} - $uniq_token");
		}else{
			if($PM{'make_bbs_html_top'}!=1){
#&error("CGIエラー tokenが時間切れになりました。ttmp_uniq_char $ttmp_uniq_char--$FORM{'onetime_token'} - $uniq_token");
			&error(" CGIエラー．tokenが時間切れになり、投稿できませんでした．SPAM対策のため投稿は、24時間以内に記入し、投稿してください ");
			}
		}

	}

	# 2006.03 add 掲示板SPAM対策
	# 2006.04 修正
	if(($filter_bbs_spam==1)&&($FORM{'amode'} eq "")){
		$PM{'no_upload_by_black_word'}=1;
		push(@BLACK_WORD,"ttp:");
		push(@BLACK_WORD,"\@");
		push(@BLACK_WORD," ｔｔｐ ");
		push(@BLACK_WORD,"\[url=");# 2007.05 追加
#		push(@BLACK_WORD," ＠ ");
	}

	# 2008.06 ニコニコの仕様変更に対応 2011.06修正
	if($FORM{'body'}=~ /iframe.*src="https?:\/\/([\-a-zA-Z0-9]+)\.nicovideo\.jp\/thumb\/([\-a-zA-Z0-9_]+)"/i){
	 if($PM{'auto_nicovideo_find'}==1){
# 2014.02 コメント回りこみのために再度iframe許可することにした
# 2014.02 orz..コメント付きでサムネイル絵が超小さくなるので、再度やめた
		&error(" 操作エラー。ニコニコ動画のリンクはIFRAMEタグを使わず、 http://www.nicovideo.jp/watch/$2 と本文にURLだけを記載すると、自動的にきちんと埋め込み表\示\されます。同記載方法に変更し、再投稿してください ","","1");
	 }else{
		&error(" 操作エラー。IFRAMEタグはセキュリティ上問題あるため、本文中に使えません。","","1");
	 }
	}

	# 2009.12
	if($FORM{'body'}=~ /src\=\"http\:\/\/www\.dailymotion\.com/i){
		$PM{'spam_url_link_limit_2'}=0;
		$PM{'spam_url_link_limit_3'}=0;
		$PM{'spam_url_link_limit_4'}=0;
		$PM{'spam_url_link_limit_5'}=1;
	}


	# エラーで出る説明で誘導する
	if(($PM{'allow_res_upload'} != 1)&&($FORM{'prebbsaction'} eq "disp_rep_form")){
	 if($FORM{'body'}=~ /ttp:\/\/([\-a-zA-Z0-9]+)\.nicovideo\.jp\/watch\//i){
		&error(" ユーザー操作エラー。現在、返信記事にはニコニコ動画URLの埋め込みはできない設定になっています。<BR>動画埋め込みは、親記事でおこなってください。 ","","1");
	 }
	}

	if($PM{'no_upload_by_black_word'}==1){

	  foreach (@BLACK_WORD){

	    $w_pattern="$_";
	    $w_pattern=~ s/\s//g;
	    $w_pattern=~ s/　//g;

	    if($w_pattern ne ""){
		$blkw_count++;
		#記事すべての項目をチェックする
		local(@ALL_ITEM)=('body','name','subject','email','imgtitle','optA');
		local($ttt_form)="";
		foreach $form(@ALL_ITEM){
		        $ttt_form = $FORM{"$form"};
			$ttt_form =~ s/\s//g;
			$ttt_form =~ s/　//g;
			if (index($ttt_form,$w_pattern) >= 0){
				$error_mes_type="black_word";
				$bad_user_flag=1;
				last;# 検出したら抜ける
			}
		}
	    }
	  }
	}

	# 2006.04 SPAM対策
	if(($PM{'no_upload_by_spam_word'}==1)&&($bad_user_flag != 1)){

	  # 2006.06 SPAM対策 URLリンク列挙型SPAM対策
	  # 2007.05 5,6まで指定できるようにした
	  if($FORM{'body'}=~ /ttp(.*)/is){

		 if($1=~ /tp:(.*)/is){
		    if($PM{'spam_url_link_limit_1'}==1){
		     &error("URLリンクはひとつまでにしてください。");
		    }
		  if($1=~ /tp:(.*)/is){
		    if($PM{'spam_url_link_limit_2'}==1){
		     &error("URLリンクはふたつまでにしてください。");
		    }
		   if($1=~ /tp:(.*)/is){
		    if($PM{'spam_url_link_limit_3'}==1){
		     &error("URLリンクはみっつまでにしてください。");
		    }
		    if($1=~ /tp:(.*)/is){
		     if($PM{'spam_url_link_limit_4'}==1){
		      &error("URLリンクはよっつまでにしてください。");
		     }
		    }
		    if($1=~ /tp:(.*)/is){
		     if($PM{'spam_url_link_limit_5'}==1){
		      &error("URLリンクはいつつまでにしてください。");
		     }
		    }
		    if($1=~ /tp:(.*)/is){
		     if($PM{'spam_url_link_limit_6'}==1){
		      &error("URLリンクはむっつまでにしてください。");
		     }
		    }
		   }
		  }
		 }
	  }


	  # 2007.05 英語のみの投稿を排除
	  if($PM{'spam_limit_non_japanese'}==1){
	   if($img_data_exists == 1){
	   }else{
	    if($FORM{'body'} eq ""){
		&error(" スパム対策により、本文が空の投稿はできません。 ");
	    }elsif($FORM{'body'}=~ /^[\x00-\x7f]+$/){
	    # 2011.03.30改良
	    
	     # 2014.02 英語のみの埋め込み動画投稿を排除
	  	 if($PM{'spam_limit_non_japanese_movie'}==1){
			&error(" スパム対策により、英語のみの文字投稿はできません。日本語の文字を追記して、本文に日本語を含めるようにしてください。 ");	  	 
		 }

	     # 2014.02 利便性向上のため、動画埋め込みは英語のみでも基本認める	 
		 if($FORM{'body'}=~ /<iframe(.|\n)*src=(\")?(https?\:\/\/|\/\/)www\.youtube\.com\//i){
#Youtubeの短縮URLは認める
		 }elsif($FORM{'body'}=~ /youtu\.be\//i){
#旧Youtubeは認める
		 }elsif($FORM{'body'}=~ /<object(.|\n)*<embed(.|\n)*src=(\")?http\:\/\/www\.youtube\.com\/(.|\n)*application\/x-shockwave-flash/i){
#FC2は認める
		 }elsif($FORM{'body'}=~ /video\.fc2\.com\//i){
#ニコニコ動画は認める
		 }elsif($FORM{'body'}=~ /\.nicovideo\.jp/i){
#Ustreamは認める
		 }elsif($FORM{'body'}=~ /\.ustream\.tv\//i){
#その他はチェックする
		 }elsif($FORM{'body'}=~ /<iframe(.|\n)*src=(\")?(https?\:\/\/|\/\/)/i){
			if($FORM{'name'}=~ /^[\x00-\x7f]+$/){
# 救済開始：名前も英語の場合ダメ
			 &error(" スパム対策により、英語のみの文字投稿はできません。日本語の文字を前後に追記して、名前や、本文に日本語を含めるようにしてください。 ");
			}else{
#救済開始：名前が日本語なら認める
			}
		 }else{
			&error(" スパム対策により、英語のみの文字投稿はできません。日本語の文字を追記して、本文に日本語を含めるようにしてください。 ");
		 }
	    }
	   }
	  }

	  #2007.05 タイトルなどにURLを埋め込むSPAM対策
	  if($PM{'no_upload_by_spam_word'} == 1){

	      local(@LINKCHK_ITEM)=('name','subject','email','imgtitle');

	      foreach $form(@LINKCHK_ITEM){
	        $ttt_form = $FORM{"$form"};
		$ttt_form =~ s/\s//g;
		$ttt_form =~ s/　//g;
		if($ttt_form=~ /tp:\/\/(.*)/is){
		      &error("URLリンクはこの欄($form)には埋め込めません ");
		}
		# 2007.06.05 タグ埋め込みSPAM対策を追加
		if($ttt_form=~ /<\//g){
		      &error("タグはこの欄($form)には埋め込めません ");
		}
		# XHTML対策
		if($ttt_form=~ /\/>/g){
		      &error("タグはこの欄($form)には埋め込めません ");
		}
		# Webエスケープ対策
		if($ttt_form=~ /&#\d+/g){
		      &error("Webエスケープ文字＆＃XXXはこの欄($form)には埋め込めません ");
		}
	      }
	  }

	  #2007.05 SPAMによるメールアドレス投稿をブロック
	  if(($PM{'no_upload_by_spam_word'} == 1)&&($PM{'no_upload_by_spam_country_mail'} == 1)){

	      local(@LINKCHK_ITEM)=('name','subject','email');

	      foreach $form(@LINKCHK_ITEM){
	        $ttt_form = $FORM{"$form"};
		$ttt_form =~ s/\s//g;
		$ttt_form =~ s/　//g;
	        if(($ttt_form=~ /\@/g)||($ttt_form=~ /＠/g)){
		 foreach (@SPAM_MAIL_COUNTRY){
		    $w_pattern="$_";
		    $w_pattern=~ s/\s//g;
	    	    $w_pattern=~ s/　//g;
		    if($ttt_form=~ /$w_pattern/ig){
		      &error("スパムフィルター設定により、このメールアドレスは($form)欄に書き込めません。 ");
		    }

		 }
		}

	      }
	  }

	  # 2010.02

			#2010.02 kisaragi-SPAM対策
			if($FORM{'body'} ne ""){
			 $ttmp2_form_data="$FORM{'body'}";
	    	 $ttmp2_form_data=~ s/\s//g;
	    	 $ttmp2_form_data=~ s/　//g;

			 # 新kisaragi-SPAM対策
			 # Webエスケープ対策をする
			 if($ttmp2_form_data=~ /&#\d+/g){
		      &error("SPAM対策により、Webエスケープ文字＆＃XXXは本文には埋め込めません ");
			 }
			 # 2010.07
			 if($ttmp2_form_data=~ /&#x/gi){
		      &error("SPAM対策により、Webエスケープ文字＆＃xは本文には埋め込めません ");
			 }

			 $ttmp_host_addr="";
			 $ttmp_host_ip="";
			 # 2010.09 update SPAM業者ドメインの多様化に対処
			 # 2010.12 update 顔文字の誤検出に対処
			 # 2012.05 update 専用ドメインを持つタイプに対処
			 if (@URL_HOST_LINKS =  $ttmp2_form_data =~ /\/+([^\)\/]+[\.com|\.net|\.org|\.info|\.biz|\.uk|\.name|\.in|\.tk|\.be|\.mobi|\.co|\.asia|\.jp])/) {
  				foreach (@URL_HOST_LINKS) {
				 next if($_ eq "");
				 # ドメインからIPアドレスを得る(API非公開プロバイダを配慮)
				 $ttmp_host_addr = gethostbyname($_);
  				 $ttmp_host_ip = join('.', unpack("C*", $ttmp_host_addr));
	  			 push(@URL_IP_LINKS, $ttmp_host_ip);  # IPアドレスを配列に保存する。
#&error("SPAM = URL_IP_LINKS - @URL_IP_LINKS - URL_HOST_LINKS - @URL_HOST_LINKS - SPAM_HOSTS_IP - @SPAM_HOSTS_IP");
  			 	}
  			 }
  			 
		 	 foreach (@URL_IP_LINKS){		 	 
				next if($_ eq "");
				$ttmp_link_url_ip="$_";
		 	 	foreach (@SPAM_HOSTS_IP){
				 next if($_ eq "");
			    # 正規表現をPerlパターンマッチへ変換
	    		$ip_pattern=&change_pattern_match($_);
				   if ($ttmp_link_url_ip =~ /^$ip_pattern/i){
					$error_mes_type="black_word";
					$bad_user_flag=1;
#2008.08.08 temp あとで必ず削除
#&error("SPAM検出 = URL_IP_LINKS - @URL_IP_LINKS - URL_HOST_LINKS - @URL_HOST_LINKS - ttmp_link_url_ip $ttmp_link_url_ip ip_pattern $ip_pattern -");				
					last;# 検出したら抜ける
		 	 	   }
		 	    }
		 	    last if($bad_user_flag==1);
 			 }
 			}

	  foreach (@SPAM_WORD){

	    $w_pattern="$_";
	    $w_pattern=~ s/\s//g;
	    $w_pattern=~ s/　//g;

		# 2012.10 SPAMノーマライズ処理追加
	    $w_pattern=lc("$w_pattern");
#		$w_pattern =~ tr/A-Z/a-z/;

	    if($w_pattern ne ""){
		$blkw_count++;
		#記事すべての項目をチェックする
		local(@ALL_ITEM)=('body','name','subject','email','imgtitle','optA');
		local($ttt_form)="";
		$spam_link_find_flag=0;# URLリンクがあるかどうか（グローバル）
		foreach $form(@ALL_ITEM){
			$spam_link_find_flag=0;	# 初期化
		        $ttt_form = $FORM{"$form"};
			$ttt_form =~ s/\s//g;
			$ttt_form =~ s/　//g;
			if($ttt_form=~ /tp:/i){
				$spam_link_find_flag=1;
			}elsif($ttt_form=~ /ｔｔｐ/i){
				$spam_link_find_flag=1;
			}elsif($ttt_form=~ /\@/i){
				$spam_link_find_flag=1;
#			}elsif($ttt_form=~ /＠/i){
#				$spam_link_find_flag=1;
# 2007.05 修正
			}elsif($ttt_form=~ /\[url=/i){
				$spam_link_find_flag=1;
			}else{
				$spam_link_find_flag=0;
				next;	# URLリンクがない場合はチェックしない
			}

# 2014.02 scriptタグのurl指定をSPAM判定してしまう問題対策 パターンマッチはノーマライズ後で空白なしな点に、注意
			# fc2であることを厳密にチェック
			if($ttt_form=~ /(<|%3C)script(.|\n)*src\=\"https?\:\/\/static\.fc2\.com\/(.|\n)*url\=\"(.|\n)*(<|%3C)\/script(>|%3E)/i){
			# そこそこチェック
#			if($ttt_form=~ /(<|%3C)script(.|\n)*url\=\"(.|\n)*(<|%3C)\/script(>|%3E)/i){
				$spam_link_find_flag=0;
				next;	# チェックしない
			}else{
			
			}
			
			# 2012.10 SPAMノーマライズ処理追加
	    	$ttt_form=lc("$ttt_form");

			if (index($ttt_form,$w_pattern) >= 0){
				$error_mes_type="black_word";
				$bad_user_flag=1;
#2008.08.08 temp あとで必ず削除
#&error("SPAM = $w_pattern");
				last;# 検出したら抜ける
			}
		}
	    }
	  }
	}

	# 問題点を検出した場合の処理
	if($bad_user_flag==1){
		# ダミーのエラーメッセージを出す
		if($error_mes_type eq "black_word"){
			# 設定で指定している場合はそれを使う。ないならデフォルト	
			if($PM{'error_message_to_black_word'} ne ""){
				$error_mes_bl="$PM{'error_message_to_black_word'}";
			}
		}
		# 2007.06.05 SPAMワードにより内容が消えてしまう問題に対処
       		&error("$error_mes_bl $blkw_count<!--abwc $add_black_word_count asc $add_spam_count aswc $add_spam_word_count abuc -->","","1");
	}

	}	# 投稿時以外(view時など)は、ホスト名以外のフィルタはスキップ（ここまで）
}

# 外部リストをロードする部品

sub load_ext_list{

	local($list_fname)	= $_[0];	# リストの名前
	local($array_name)	= $_[1];	# 配列の名前
	local($add_count)	= 0;		# リストから追加された項目数

	if(-e "$list_fname"){
	open(IN, "$list_fname")|| &error("設定エラー．ファイル\"$list_fname\"を読込めません．処理は中断されました．");
	eval "flock(IN,1);" if($PM{'flock'} == 1 );
		while(<IN>){
			if($_ =~ /^([^#])(.*)$/){	#コメントアウトは除く
				if($_ =~ /^(\s*)(\S+)(\s*)(\#?)(.*)$/){
					# Perl4でも動く書き方にする（長くなるけど）
					if($array_name eq 'BLACK_LIST'){
						push(@BLACK_LIST, $2);
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
	return($add_count);	# リストから追加された項目数
}

sub change_pattern_match{

	# 正規表現をPerlパターンマッチへ変換
	local($d_pattern)	= $_[0];
	$d_pattern=~ s/\s|\r|\n|\;|\)//g;	# 念のため
	$d_pattern=~ s/\./\\./g;
	$d_pattern=~ s/\?/\./g;
	$d_pattern=~ s/\*/\.\*/g;
	$d_pattern=~ s/P_TAIL$/\$/i;
	$d_pattern=~ s/P_END$/\$/i;
	$d_pattern=~ s/^P_HEAD/\^/i;
	$d_pattern=~ s/P_SPACE/\\s/i;
	return($d_pattern)
}

#========================#
# IP情報を一部伏せ字にする
#========================#

# $user_IP情報をプライバシー保護のため、一部伏せ字にするフィルタ

sub user_IP_privacy_filter{

    local($local_ip,$other_ip,$company_name,$org_local_ip,$org_other_ip);

    # リモートホストがIPアドレスの場合
    if($user_IP=~ /^(\d+)\.(\d+)\.(\d+)\.(\d+)$/){
	$user_IP="$1.$2.$3.\*";
    # リモートホストが携帯アドレスの場合
    }elsif($user_IP=~ /-KSN-/i){
	# 数字を隠す。
	 $other_ip=~ tr/0-4/\?/;
    # リモートホストが論理ホスト名の場合
    }elsif($user_IP=~ /(\w+)\.(\w+)$/){
      if($user_IP=~ /^([^\.]+)\.(.*)$/){
	$local_ip="$1";
	$other_ip="$2";
	$org_local_ip="$1";
	$org_other_ip="$1";

	# 最もローカル側のipの頭を１文字隠す。あと数字は意味ないので隠す。
	$local_ip=substr($local_ip,1);
	$local_ip="\?"."$local_ip";
	$local_ip=~ tr/0-9/\?/;
	# 会社から掲示板にアクセスしていることがバレるといやな人は多いと
	# 思われるので、会社の場合は社名を削る。しかし、あんまり削ると
	# イタズラ予防効果がなくなるので、お尻を２文字だけ削ることにする
	if($other_ip=~ /^(.*)(\.?)([^\.]+)\.(co)\.(jp)$/){
	    $company_name="$3";
#	    $company_name=substr($company_name,1);
	    chop($company_name);
	    chop($company_name);
	    $other_ip="$1$2$company_name\?\?.$4.$5";
	}
	# 政府機関は頭を２文字、お尻を１文字削る
	if($other_ip=~ /^(.*)(\.?)([^\.]+)\.(go)\.(jp)$/){
	    $company_name="$3";
	    $company_name=substr($company_name,2);
	    chop($company_name);
	    $other_ip="$1$2\?\?$company_name\?.$4.$5";
	}
	# 大学は、悪い人?がよくJUMPに使い、悪用されることが多いので、
	# 下部はそのまま削らない・・・(^_^)
	if($other_ip=~ /ac\.jp$/){
		$other_ip="$org_other_ip";
	}
	if(($other_ip=~ /ne\.jp$/)||($other_ip=~ /or\.jp$/)){
	 # プロバイダは、もともと匿名性が高いので、最初の１文字削りと
	 # 数字消しで充分かな・・・ということだったが、
	 # サードドメインの数字だけ消しておく
	 $other_ip=~ tr/0-9/\?/;
	}
	$user_IP="$local_ip"."\."."$other_ip";
      }
    }
}

#============================#
# ＪＵＭＰ用ＨＴＭＬ
#============================#

sub jump_html{

#	$gvar_cgi_add_url;			# URLに足すべきもの(グローバル変数)
	local($tmp_cgi_add_url)	= $_[0];	# URLに足すべきもの(将来拡張用)

	local($mes_01);

	if($SERVER_NAME=~ /tok2\.com/){
	  $mes_01=qq|<META http-equiv="Set-Cookie" content="$tok2_cookie">|;
	}else{
	  undef $mes_01;
	}

	print "Content-type: text/html"."$Netscape4x_ch_set"."\n\n";

	if(($form_disp_on_board==0)&&($FORM{'bbsaction'} eq 'post')&&($FORM{'prebbsaction'} ne "disp_rep_form")&&($FORM{'prebbsaction'} ne "edit_form")){

# フォーム別ウィンド時のためのメニュー
		print<<EOF;
<HTML lang="ja">
<HEAD>
 <TITLE>Imgboard - Message </TITLE>
 $mes_01
 <META HTTP-EQUIV="Refresh" CONTENT="20; URL=$cgi_name?bbsaction=disp_form_only">
<SCRIPT language="javascript">
<!--
timerID		=10;
var timer_a	=0;
var timer_b	=0;


function reload_bbs_window(){
	clearTimeout(timerID);
	timerID =setTimeout("reload_bbs_window()",1000);
	if(timer_a ==7){	//7秒後にフラッシュ
		location.href="$cgi_name?bbsaction=disp_form_only&p1=$FORM{'p1'}&p2=$FORM{'p2'}&amode=$FORM{'amode'}";//入力ウィンドをロード
	}
	if(timer_b ==5){	//5秒後にフラッシュ
		window.opener.location.href="$cgi_name?&p1=$FORM{'p1'}&p2=$FORM{'p2'}&amode=$FORM{'amode'}";	//親ウィンドをリロード
	}
	if(timer_b ==120){	//120秒後にループ自動停止
		clearTimeout(timerID);
	}
	timer_a+=1;//１秒に一回インクリメント
	timer_b+=1;//１秒に一回インクリメント
}

//-->
</SCRIPT>
</HEAD>
<BODY BGCOLOR="#D0D0D0" onLoad="reload_bbs_window();">
<table border="1" cellspacing="10" cellpadding="10">
 <TR bgcolor="#0000B0">
  <TD bgcolor="#0000B0" NOWRAP>
   <font size="-1" color="white"><B>Imgboard - Message</B></font>
  </TD>
 </TR>
</table>
<UL><BR><BR>
<font color=black>
<blink>処理中......</blink><BR><BR>
10秒間このままお待ちください．
</UL>
</BODY>
</HTML>

EOF

	}else{

	  # 引数で指定された場合はそれを使う
	  if($tmp_cgi_add_url ne ""){
		$cgi_add_url="$tmp_cgi_add_url";

	  # グローバル変数で指定された場合はここで拾う
	  }elsif($gvar_cgi_add_url ne ""){
		$cgi_add_url="$gvar_cgi_add_url";

	  # 引数で指定されない場合はケース別にここで対処を分岐
	  }else{
		$cgi_add_url="";

		# 返信時にページを記憶する
		if(($FORM{'bbsaction'} eq "post")&&($FORM{'prebbsaction'} eq "disp_rep_form")){
			if($FORM{'page'} ne ""){
				$cgi_add_url="\?page=$FORM{'page'}&p1=$FORM{'p1'}&p2=$FORM{'p2'}&amode=$FORM{'amode'}";
			}
			# レスを上に持って行く設定の場合スレッドが先頭へ行くので、先頭へジャンプ
			if($PM{'res_go_up'} == 1){
				$cgi_add_url="\?page=1&p1=$FORM{'p1'}&p2=$FORM{'p2'}&amode=$FORM{'amode'}";
			}
		# 削除時 / ページ変更時
		}elsif(($FORM{'bbsaction'} eq "remove")||($FORM{'bbsaction'} eq "pf_change")){
		   # 2003.06 変更
		   # 削除、表示モード変更時の飛び先PAGEを計算
		   if($FORM{'page'}>1){
				$tmp_jump_page=$FORM{'page'};
		   }else{
				$tmp_jump_page=1;
		   }
		   $cgi_add_url="\?page=$tmp_jump_page&p1=$FORM{'p1'}&p2=$FORM{'p2'}&amode=$FORM{'amode'}";
		# WebParts情報修正時
		}elsif(($FORM{'prebbsaction'} eq "edit_form")&&(($FORM{'amode'} ne "post_webparts"))){
		  $cgi_add_url="\?page=$FORM{'page'}&p1=$FORM{'p1'}&p2=$FORM{'p2'}&amode=$FORM{'amode'}"
		}
	  }

		print<<EOF;
<HTML lang="ja">
<HEAD>
 <TITLE>wait..</TITLE>$top_html_header
 $mes_01
 <meta name="viewport" content="width=480">
 <META HTTP-EQUIV="Refresh" CONTENT="2; URL=$cgi_name$cgi_add_url">
</HEAD>
<BODY BGCOLOR="#D0D0D0">
<table border="1" cellspacing="10" cellpadding="10">
 <TR bgcolor="#0000B0">
  <TD bgcolor="#0000B0" NOWRAP>
   <font size="-1" color="white"><B>imgboard - Message</B></font>
  </TD>
 </TR>
</table>
<UL><BR>
<font color=black>
<blink>処理中......</blink><BR><BR>
３秒間このままお待ちください．
</UL>

</BODY>
</HTML>

EOF

	}
}
#
#================================================#
# オリジナルファイル名使用希望者用追加サブルーチン
#================================================#
#
sub use_orig_name{
	&error("オリジナルファイル名で保存する機能はimgboardから削除されました。<BR>同機能は、今後は imgboard2015でサポートします ");
}
#
#============================#
# エラーの出力
#============================#

sub error{

	local($error_message)	= $_[0];# メッセージを引数として取得
	local($error_message2)	= $_[1];# メッセージを引数として取得
	local($js_back_flag)	= $_[2];# Javascriptで戻るボタンを出したい場合は1に

	#for Form window
	if(($form_disp_on_board ==0)&&($FORM{'bbsaction'} ne 'remove' )){
		$error_bbsaction="disp_form_only";
	}

	print "Content-type: text/html"."$Netscape4x_ch_set"."\n\n";

print<<EOF;
<HTML lang="ja">
<HEAD>
<TITLE>Error Message from Imgboard</TITLE>
<meta name="viewport" content="width=480">
$top_html_header
</HEAD>

<BODY BGCOLOR=\"#D0D0D0">
<table border="1" cellspacing="10" cellpadding="10">
 <TR bgcolor="#0000B0">
  <TD bgcolor="#0000B0" NOWRAP>
   <font size="-1" color="white"><B>Imgboard - Error Message</B></font>
  </TD>
 </TR>
</table>

<UL>
 <H4> $error_message </H4>
 $error_message2 <BR>
</UL>
<BR>
<UL>
EOF

# 返信の時、修正の時、アイコン登録時に記入ミスがあると戻れないバグに対応
    if((($FORM{'bbsaction'} eq 'post')&&(($FORM{'prebbsaction'} eq 'disp_rep_form')||($FORM{'prebbsaction'} eq 'edit_form')))||($FORM{'amode'} eq "icon_admin")||($js_back_flag == 1 )||($FORM{'amode'} eq "post_webparts")){

print<<EOF;
<FORM>
<INPUT TYPE="button" VALUE=" もどる " $output_button_px onClick="history.back()">
</FORM>
<NOSCRIPT>
<a href="$ENV{'HTTP_REFERER'}">もどる</a>
</NOSCRIPT>
EOF
    }else{
print<<EOF;
<FORM METHOD="GET" ACTION="$ENV{'HTTP_REFERER'}">
<INPUT TYPE="HIDDEN" NAME="page" VALUE="$FORM{'page'}">
<INPUT TYPE="HIDDEN" NAME="amode" VALUE="$FORM{'amode'}">
<INPUT TYPE="HIDDEN" NAME="p1" VALUE="$FORM{'p1'}">
<INPUT TYPE="HIDDEN" NAME="p2" VALUE="$FORM{'p2'}">
<INPUT TYPE=\"HIDDEN\" NAME="bbsaction" VALUE="$error_bbsaction">
<INPUT TYPE="SUBMIT" VALUE=" もどる " $output_button_px> 
</FORM>
EOF
    }
print<<EOF;
</UL>

</BODY>
</HTML>
EOF
	&rm_tmp_uploaded_files;			# 一時保存された画像データを削除
	exit;
}
#
#===================================#
# 一時登録された画像ファイルの削除
#===================================#

sub rm_tmp_uploaded_files{
	if($img_data_exists==1){
		foreach $fname_list(@NEWFNAMES){
			if(-e "$img_dir/$fname_list"){
				unlink("$img_dir/$fname_list");
				# メタファイルも削除する
				&rm_meta_file("$img_dir/$fname_list");
			}
			# 携帯用ファイルも削除する
			if($fname_list=~ /\.(jpe?g|gif|png|bmp|mng)$/i){
				  &rm_snl_file("$unq_id","$img_dir","$existing_snl_type_list");
			}
		}
	}
}
#
#=============================#
# 携帯用ファイルの削除(R7)
#=============================#
#
# 将来の全携帯対応を考えて拡張子は
# いろいろできるようにしておく
#
sub rm_snl_file{

	local($tmp_rm_snl_unq_id)	=$_[0]; # 引数1はUID
	local($tmp_rm_snl_dir)		=$_[1]; # 引数2はパス
	local($tmp_rm_snl_exist_type)	=$_[2]; # 引数3はSNL存在リスト

	local($snl_future_bit);		# 携帯用ファイル名の将来拡張ビット
	local($snl_ext);		# 携帯用ファイルの実際の拡張子

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
#====================================================#
# imgtitleから、$IMG_PARAMETERS{name}情報を抜き出す
#====================================================#
# 引数はコメントアウト付きの$tmp_imgtitle
# 返値はコメントアウトなしの$tmp_imgtitleと連想配列 $IMG_PARAMETERS{$name}
sub parse_img_param{

	local($ttmp_imgtitle)= $_[0];	# 引数として取得

	# imgtitleの中にsize,height,width等のパラメータを格納
	# 書式<!--パラメータ名=値;パラメータ名2=値2・・・-->
	# <!--と-->を除きパラメータ部を抽出
	if($ttmp_imgtitle ne ''){
		($ttmp_imgtitle,$img_parameters)=split(/<\!--/,$ttmp_imgtitle);
		$img_parameters=~ s/-->//g;
	}

	# パラメータ$img_parametersが追加されている場合．
	if($img_parameters ne ''){
		foreach ( split(/;/,$img_parameters)){
			local($name,$value) = split(/\=/);
			$IMG_PARAMETERS{$name} = $value;
		}
	}
	return($ttmp_imgtitle);
}
#
#===================================#
# ASX メタファイルの削除
#===================================#
# Winodows Mediaのストリーム再生やeggy/FOMAのストリーム再生対応のために
# 機能拡張した。 削除するファイルがメタファイルを持っていそうな
# 名前だったらメタファイルらしきファイルを探し、もしあれば消しておく
sub rm_meta_file{

	local($tmp_rm_meta_file)=$_[0]; # 引数は削除するファイル名本体（パス付き）

	# asx等に対応
	if($tmp_rm_meta_file=~ /^(.*)\.(asf|wma|wmv?)$/){
	   if(-e "$1\.asx"){
		unlink("$1\.asx");# ASF(古い表記の仕方)
	   }
	   if(-e "$1\.wax"){
		unlink("$1\.wax");# ASF&WinMediaAudio(一時的に使われた)
	   }
	   if(-e "$1\.wvx"){
		unlink("$1\.wvx");# ASF&WinMediaAudio/Video(現在はこれが推奨らしい)
	   }
	}
}
#
#=======================#
# 投稿ブラウザチェック
#=======================#
#
sub check_post_browser_type{
	if($HTTP_USER_AGENT=~ /icab/i){
	    &error(" エラー このブラウザでは記事の投稿はできません ");
	}
}
#
#====================#
# ブラウザチェック
#====================#
#
sub check_browser_type{

	# Apache 1.3.12 以降で発生する、Netscape 4.x文字化け問題対策
	if($HTTP_USER_AGENT!~ /compatible/i){
	 if($HTTP_USER_AGENT=~ /Mozilla\/4\.(\d)/i){
	  if( $use_sjis_header_for_Netscape4X == 1){
	   if( $1 >= 5 ){
		$Netscape4x_ch_set="; charset=Shift_JIS";
#		$Netscape4x_ch_set="; charset=ISO-2022-JP";
	   }
	  }
	 }
	}

    #ipod/iPhone文字化け対策 2008.06.20 update 2012.05.07
	if($HTTP_USER_AGENT=~ /ipod|iPad|iPhone|safari|Firefox/i){
		$Netscape4x_ch_set="; charset=Shift_JIS";
	}
	
}
#
#=====================#
# iモードチェック(R6)
#=====================#
# 2010.01.23 アンドロイド対応で小修正
# 2001.05.25 (iモード以外もリダイレクトするようにした)
sub check_imode{

	if($imode_redirect==1){
	   if(-e "$imode_cgi_name"){
	   # 2010.01 android新ファーム1.6のUSER_AGENTにdocomoの文字が！！(従来はFullブラウザ系にはDoCoMoの文字はないのが通例だった)。
		if($HTTP_USER_AGENT=~ /^docomo/i){ 
		  print "Content-type: text/html"."$Netscape4x_ch_set"."\n\n";
		  &simple_HTML(""," 転送 "," <a href=\"$imode_cgi_name\"\> iモードユーザ専用アクセスページ </a> をどうぞご利用ください ");
		  $keitai_flag="imode";
		}elsif($HTTP_USER_AGENT=~ /^kddi/i){
		   print "Content-type: text/html"."$Netscape4x_ch_set"."\n\n";
		   &simple_HTML(""," 転送 "," <a href=\"$imode_cgi_name\"\> au ユーザ専用アクセスページ </a> をどうぞご利用ください ");
		   $keitai_flag="imode";
		# 2006.10.20 Update
		}elsif(($ENV{'HTTP_X_JPHONE_MSNAME'} ne "")||($HTTP_USER_AGENT=~ /Vodafone/i)||($HTTP_USER_AGENT=~ /^SoftBank/i)){
		  print "Content-type: text/html"."$Netscape4x_ch_set"."\n\n";
		  &simple_HTML(""," 転送 "," <a href=\"$imode_cgi_name\"> SoftBankユーザ専用アクセスページ </a> をどうぞご利用ください ");
		  $keitai_flag="J-PHONE";
		}else{
		  $keitai_flag="pc";
		}
	   }
	}
}
sub simple_HTML{

 local($tmp_tm)		=$_[0];
 local($tmp_mes01)	=$_[1];
 local($tmp_mes02)	=$_[2];
 local($tmp_exit_f)	=$_[3];


print<<HTML_END;
<HTML>
<HEAD><TITLE>$tmp_tm</TITLE>$top_html_header
<meta name="viewport" content="width=480">
</HEAD>
<BODY BGCOLOR=#B0B0D0>
$tmp_mes01<P>
$tmp_mes02
<P>
HTML_END

print "$output_simple_block01_HTML\n";

if($tmp_exit_f == 1){
print<<HTML_END;
<CENTER>
[<a href="$cgi_name?page=$FORM{'page'}">$tmp_tm 終了</a>]<BR>
</CENTER>
HTML_END
}
print<<HTML_END;
</BODY>
</HTML>
HTML_END

undef $output_simple_block01_HTML; # 初期化
exit;

}
#
#====================#
# プロバイダチェック
#====================#

sub check_ISP{

	if($SERVER_NAME=~ /bekkoame\./){
		&error(" CGI設定エラー。imgboardがサポート外サイトを検出しました。<BR>「$SERVER_NAME」は、CGIに関して特殊な制約があるため、残念ながらimgboardを利用することができません。他のプロバイダをご利用ください ");
	}

	if($SERVER_NAME=~ /prohosting\.com/){
		&error(" CGI設定エラー。imgboardが非推奨サイトを検出しました。<BR>「$SERVER_NAME」は、広告挿入用のJavascriptに特殊な制約があり、残念ながらR6以降のimgboardを利用することができません。freeweb,トクトク等、他の無料プロバイダをご利用ください ");
	}

	if(($SERVER_NAME=~ /hi\-ho\.ne\.jp/)||($SERVER_NAME=~ /\.nifty\.com/)||($SERVER_NAME=~ /\.wakwak\.com/)){
	# img_url設定が必要なサイトで設定が未設定の場合は警告を出す
		if($img_url eq 'http://あなたのプロバイダ/あなたのディレクトリ/img-box'){
			&error(" CGI設定にエラーがあります。<BR>あなたが設置しようとしているプロバイダ
			「 $SERVER_NAME 」では特殊な設定が必要になります。新FAQ掲示板を参照して、これを設定してください ");
		}
	}

	if($SERVER_NAME=~ /www5.\.biglobe/){
	# img_url設定が必要なサイトで設定が未設定の場合は警告を出す
		if($img_url eq 'http://あなたのプロバイダ/あなたのディレクトリ/img-box'){
			&error(" CGI設定にエラーがあります。<BR>あなたが設置しようとしているプロバイダ
			「 $SERVER_NAME 」では＄img_urlの設定が必要になります。これを設定してください。
			なお、設定方法がわからない場合はサポート掲示板の過去ログを参照してください ");
		}
	}
}
#
#====================#
# Apache1.3.x対策
#====================#

sub check_RH{
	if(($REMOTE_HOST eq "")||($REMOTE_HOST =~ /^null$/i)){
	    $REMOTE_HOST = "$ENV{'REMOTE_ADDR'}";
	}
	# 1.22 Rev4 イタズラ投稿防止策
	# リモートホストがない場合は登録させない。メッセージはダミー
	if(($REMOTE_HOST eq "")&&($no_upload_by_no_RH_user=='1')){
	    &error("CGIエラー No REMOTE_HOST <BR>現在、リモートホスト情報がない場合は、投稿できない設定になっています。 ");
	}
}

#================================#
# 連続投稿制限 メイン(1.22 Rev4)
#================================#
#
sub limit_upload_times{
	if($limit_upload_times_flag==1){
	 # 連続投稿カウンタを実行
	 # $new_utc_setはクッキーに設定される。
	 # 引数は設定部で設定。デフォルト値を持つので空でもいい。
	 $new_utc_set=&count_upload_times("$upload_limit_type","$upload_limit_times");
	}
}
#
#================================#
# 連続投稿制限 サブ(1.22 Rev4)
#================================#
#
sub count_upload_times{

	# 連続投稿カウンタ
	# 引数は時刻レンジ、制限回数
	# 返値は新カウンタセット値,グローバル変数の$now_up_counterに現在の連続回数

	#初期化
	local($upload_limit_type)	= $_[0];# 時刻レンジを引数として取得
	local($upload_limit_times)	= $_[1];# 制限回数を引数として取得
	local($tmp_up_counter);

	# デフォルト値をセット
	$upload_limit_type="2min" if($upload_limit_type eq "");
	$upload_limit_times="5" if($upload_limit_times eq "");

	local(@NOWTIME)	= localtime(time);
	local($yday)		= $NOWTIME[7];

	# 時刻データからタイムベースナンバーを作る
	if($upload_limit_type eq "day"){		# 1日当たり？回で制限
		$up_base_num=35+$yday;
	}elsif($upload_limit_type eq "1hour"){	# 1時間当たり？回で制限
		$up_base_num=35+$yday+$hour;
	}elsif($upload_limit_type eq "10min"){	# 10分当たり？回で制限
		$up_base_num=35+$yday+(int(($min+1)/10));
	}elsif($upload_limit_type eq "2min"){	# 2分当たり？回で制限
		$up_base_num=35+$yday+(int(($min+1)/2));
	}elsif($upload_limit_type eq "1min"){	# 1分当たり？回で制限
		$up_base_num=35+$yday+(int(($min+1)/1));
	}else{						# デフォルトは2分	
		$up_base_num=35+$yday+(int(($min+1)/2));
	}

	if($COOKIE{'utc'} eq ""){
		# クッキーの値がない場合はセット
		$tmp_up_counter=$up_base_num;
		$now_up_counter=1;

		return($tmp_up_counter);
	}else{
		$tmp_up_counter=$COOKIE{'utc'};	# クッキーからカウンタ値を読む
	}		

	# エラーチェック
	if($tmp_up_counter=~ /^(\d+)$/){
		# なにもしない
	}else{
		# ０あるいは、数字以外の異常値になっている場合リセットする
		$tmp_up_counter=$up_base_num;
		# これをクッキーにセットする
		return($tmp_up_counter);
	}
	return(1) if($up_base_num==0);		# ０除算予防(通常はない)

#&error("up base $up_base_num yday $yday utc $COOKIE{'utc'} tmp_up $tmp_up_counter");

	# メイン処理
	if(($tmp_up_counter % $up_base_num)==0){
		# タイムベースが一致する場合はカウントアップする
		$tmp_up_counter+=$up_base_num;
		$now_up_counter=int($tmp_up_counter/$up_base_num);
		if($now_up_counter > $upload_limit_times){
			&error(" CGIエラー overtimes 掲示板管理者が設定した連続投稿
回数をオーバーしました。<BR>しばらく投稿できません ");
			exit;
		}
	}else{
		# タイムベースが一致しない場合はカウンタをリセットし、新タイムペースを設定
		$tmp_up_counter=$up_base_num;
		$now_up_counter=1;
	}
	# これをクッキーにセットする
	return($tmp_up_counter);
}
#
#=====================================#
# 自動URLリンク機能 Ver0.99 (R6 NEW)
#=====================================#
# 2011.09.24 update
# セキュリティ上の理由とダイアルアップユーザ減少の
# 昨今のネット事情より、PCからのtel自動リンクは廃止。
# telリンクはiアクセスの方だけ実装すれば十分だろう。
# 2007.08 Secondlife対応
# 2008.06 iPod/iPhone対応
#
sub set_auto_url_link{

	# 引数１は処理したいデータ;
	# 返値は処理後のデータ;
	local($tmp_data)=@_;
	local($tmp_yb_url)="";
	local($no_object_to_text_link)=0;# OBJECTをテキストリンクにするかどうか
	local($no_iframe_to_text_link)=0;# iframeをテキストリンクにするかどうか 2011.06
	local($tmp_youtube_snl_url)="";

	# アンカータグを書くユーザなら自動リンクをオフにする
	# ない場合のみ処理
	$PM{'auto_mail_find'}=1;


#  上で1を選択した場合，その埋め込みサイズを選択。  
#  (0=iconサイズ,1=auto,2=横固定,3=原寸サイズ,5=極端に大きな画像のみ縮小)
#$on_board_img_size=5;	# デフォルトは5

	# 外部サムネイルの埋込サイズ
	$tmp_snl_url_imgsize="";

	# objectタグを使うかどうかと、外部サムネイルのサイズを決めておく
	if($user_selected_view_mode == 1){
 	  if($COOKIE{'view_mode'} eq '1-text_only'){
		$no_object_to_text_link=1;
		$no_iframe_to_text_link=1;
		$tmp_snl_url_imgsize="";
 	  }elsif(($COOKIE{'view_mode'} eq 'text_img_type1')||($COOKIE{'view_mode'} eq 'text_img_type11')||($COOKIE{'view_mode'} eq 'text_img_type20')){
		$no_object_to_text_link=1;
		$no_iframe_to_text_link=1;
		$tmp_snl_url_imgsize=" height=\"98\" width=\"120\" border=5";
	  }else{
		# 2008.08 PSPの画面サイズを考慮
		if($HTTP_USER_AGENT=~ /PSP/i){
			$tmp_snl_url_imgsize=" height=\"120\" width=\"160\" border=5";
		}else{
			$tmp_snl_url_imgsize=" height=\"334\" width=\"415\" border=5";
		}
		
	  }
	}else{
	  # 管理者viewmode設定
 	  if($show_img_on_board==0){
		$no_object_to_text_link=1;
		$no_iframe_to_text_link=1;
		$COOKIE{'view_mode'}='1-text_only'; 	# 2013.02 add for R6
#		$COOKIE{'view_mode'}='text_img_type20'; # 2013.02 add for 2013
	  }else{
#		if(($on_board_img_size==0)||($on_board_img_size==11)||($on_board_img_size==12)||($on_board_img_size==13)){
		if($on_board_img_size==0){		# iconサイズ
		 $no_object_to_text_link=1;
 		 $no_iframe_to_text_link=1;
		 $tmp_snl_url_imgsize=" height=\"98\" width=\"120\" border=5";
		 $COOKIE{'view_mode'}='text_img_type1'; 	# 2013.02 add for R6		 
#		 $COOKIE{'view_mode'}='text_img_type11'; 	# 2013.02 add for 2013 
		}else{
			# 2008.08 PSPの画面サイズを考慮
			if($HTTP_USER_AGENT=~ /PSP/i){
				$tmp_snl_url_imgsize=" height=\"120\" width=\"160\" border=5";
			}else{
				$tmp_snl_url_imgsize=" height=\"334\" width=\"415\" border=5";
			}
		}		
	  }
	}
	
	if($MYCGI_ENV{'flash_object_tag_support'} ne 'true'){
		$no_object_to_text_link=1;
	}



	# 余計なものをフィルタ TODO 保存前に削除しておいたほうがいいかも
	# dailymotionの付録を削除
	# 2011.06 update
	if($tmp_data=~ /iframe.*src="http:\/\/www\.dailymotion\.com\/embed/i){
		$tmp_data =~ s/\<i\>(.|\n)*(\<a href\=\"https?\:\/\/www\.dailymotion\.com\/)(.|\n)*<\/i\>//ig;
		$tmp_data =~ s/\<a href\=\"https?\:\/\/www\.dailymotion\.com\/(.|\n)*<\/a\>//ig;
	}

	# ustreamの付録を削除
	$tmp_data =~ s/<a href\=\"http\:\/\/www\.ustream\.tv\/\" (.|\n)*\/a>//ig;

	# 2008.08 PSPがIFRAMEで固まる現象に対処
	if($HTTP_USER_AGENT=~ /PSP/i){
		$tmp_data =~ s/<(\/?)iframe(.|\n)*iframe>(\s*)(\n?)/
	    \[PSPでは表\示できないHTML記述です\]./ig;       # IFRAMEタグ    除去
	}
	# フィルタここまで

	
	$DAILYMOTION_VIDEO{'id'}	="";
	local($tmp_dailymotion_snl_url)="";

	$USTREAM_VIDEO{'id'}	="";
	local($tmp_ustream_snl_url)="";

	# クラウドサービスのURLを短くする 2009.12
	local($tmp_google_ap)="";
	if($tmp_data=~ /\"http\:\/\/www\.google\.co\.jp\/(\S*)\?/i){
	
	 # iframe埋込とかなので、何もしない
	 
	}elsif($tmp_data=~ /http\:\/\/www\.google\.co\.jp\/(\S*)\?/i){
	 $tmp_google_ap="$1";
	 if($tmp_google_ap=~ /maps/i){
		$tmp_data =~ s/(https?\:\/\/www\.google\.co\.jp\/maps)([\-_\.\!\~\*\'\(\)a-zA-Z0-9\;\/\?\:\@\&\=\+\$\,\%\#]*)/<A HREF="$1$2" TARGET="_blank">[google地図\]<\/A>/ig;
	 }
	}elsif($tmp_data=~ /([^\"])http\:\/\/maps\.google\.co\.jp\/(\S*)\?/i){
		$tmp_data =~ s/(https?\:\/\/maps\.google\.co\.jp\/maps)([\-_\.\!\~\*\'\(\)a-zA-Z0-9\;\/\?\:\@\&\=\+\$\,\%\#]*)/<A HREF="$1$2" TARGET="_blank">[google地図\]<\/A>/ig;
	}

	# 2011.06 YouTubeAPI変更対応
	# 2014.02 途中再生対応 クロスドメインスクリプトセキュリティ対策でパターンは厳しくする
	if($tmp_data=~ /http\:\/\/www\.(youtube|youtube\-nocookie)\.com\/watch\?v\=([\-_\.a-zA-Z0-9]+)(\&*)([\&\=\-_\.a-zA-Z0-9]*)(.|\n)*/ig){
		if($2 ne ""){
			 $YOUTUBE_VIDEO{'id'}	="$2";
			 $YOUTUBE_VIDEO{'idtype'}='url01';

			# 2014.02 途中再生対応
			if($4 ne ""){
				# 2014.02 その他のGETパラメータ
				$YOUTUBE_VIDEO{'otherRESTDATA'}="$3"."$4";

				# 2014.02 クロスドメインスクリプトセキュリティ対策でパターン判定は厳しくする

				if($YOUTUBE_VIDEO{'otherRESTDATA'}=~ /(\&t\=)(\d+h)*(\d+m)*(\d+s)*/ig){
					$YOUTUBE_VIDEO{'startRESTDATA'}	="$1"."$2"."$3"."$4";
					$YOUTUBE_VIDEO{'startCHR'}		="$2"."$3"."$4";
					$YOUTUBE_VIDEO{'startH'}		="$2" if($2 ne "");
					$YOUTUBE_VIDEO{'startM'}		="$3" if($3 ne "");
					$YOUTUBE_VIDEO{'startS'}		="$4" if($4 ne "");
					$YOUTUBE_VIDEO{'startH'}		=~ s/h//i;
					$YOUTUBE_VIDEO{'startM'}		=~ s/m//i;
					$YOUTUBE_VIDEO{'startS'}		=~ s/s//i;
					$YOUTUBE_VIDEO{'startNUM'}		=$YOUTUBE_VIDEO{'startH'}*3600 + $YOUTUBE_VIDEO{'startM'}*60 + $YOUTUBE_VIDEO{'startS'};

				# 2014.02 記述ミスも拾う
				}elsif($YOUTUBE_VIDEO{'otherRESTDATA'}=~ /(\&t\=)(\d+)/ig){
					$YOUTUBE_VIDEO{'startS'}		=$2;
					$YOUTUBE_VIDEO{'startNUM'}		=$2;
					$YOUTUBE_VIDEO{'startCHR'}		="$2"."s";
				}
			}
			 
		}else{
			 $YOUTUBE_VIDEO{'id'}	="";
		}
	# 2011.06 YouTube短縮URL表記対応
	}elsif($tmp_data=~ /https?\:\/\/youtu\.be\/([\-_\.a-zA-Z0-9]+)(\?*)([\&\=\-_\.a-zA-Z0-9]*)(.|\n)*/ig){
		if($1 ne ""){
			 $YOUTUBE_VIDEO{'id'}	="$1";
			 $YOUTUBE_VIDEO{'idtype'}='youtu_be01';

			# 2014.02 途中再生対応
			if($3 ne ""){
				# 2014.02 その他のGETパラメータ
				$YOUTUBE_VIDEO{'otherRESTDATA'}="$3";

				if($YOUTUBE_VIDEO{'otherRESTDATA'}=~ /(t\=)(\d+h)*(\d+m)*(\d+s)*/ig){
					$YOUTUBE_VIDEO{'startRESTDATA'}	="$1"."$2"."$3"."$4";
					$YOUTUBE_VIDEO{'startCHR'}		="$2"."$3"."$4";
					$YOUTUBE_VIDEO{'startH'}		="$2" if($2 ne "");
					$YOUTUBE_VIDEO{'startM'}		="$3" if($3 ne "");
					$YOUTUBE_VIDEO{'startS'}		="$4" if($4 ne "");
					$YOUTUBE_VIDEO{'startH'}		=~ s/h//i;
					$YOUTUBE_VIDEO{'startM'}		=~ s/m//i;
					$YOUTUBE_VIDEO{'startS'}		=~ s/s//i;
					$YOUTUBE_VIDEO{'startNUM'}		=$YOUTUBE_VIDEO{'startH'}*3600 + $YOUTUBE_VIDEO{'startM'}*60 + $YOUTUBE_VIDEO{'startS'};

				# 2014.02 記述ミスも拾う
				}elsif($YOUTUBE_VIDEO{'otherRESTDATA'}=~ /(t\=)(\d+)/ig){
					$YOUTUBE_VIDEO{'startS'}		=$2;
					$YOUTUBE_VIDEO{'startNUM'}		=$2;
					$YOUTUBE_VIDEO{'startCHR'}		="$2"."s";
		  }
			}

			}else{
			 $YOUTUBE_VIDEO{'id'}	="";
		        }
	# 2014.02.11 update
	}elsif($tmp_data=~ /(https?\:\/\/|\/\/)www\.(youtube|youtube\-nocookie)\.com\/(embed|v)\/([\-_\.a-zA-Z0-9]+)(\?*)([\&\=\-_\.a-zA-Z0-9]*)(.|\n)*/ig){
		if($4 ne ""){
			 $YOUTUBE_VIDEO{'id'}	="$4";
			 $YOUTUBE_VIDEO{'idtype'}='iframe';

			# 2014.02 途中再生対応
			if($6 ne ""){
				# 2014.02 その他のGETパラメータ
				$YOUTUBE_VIDEO{'otherRESTDATA'}="$6";

				# 2014.02 クロスドメインスクリプトセキュリティ対策でパターン判定は厳しくする

				if($YOUTUBE_VIDEO{'otherRESTDATA'}=~ /(start\=)(\d+)/ig){
					$YOUTUBE_VIDEO{'startNUM'}="$2";
					$YOUTUBE_VIDEO{'startCHR'}="$2"."s";					
					$YOUTUBE_VIDEO{'startRESTDATA2'}="$1"."$2";				
				}elsif($YOUTUBE_VIDEO{'otherRESTDATA'}=~ /(t\=)(\d+h)*(\d+m)*(\d+s)*/ig){
					$YOUTUBE_VIDEO{'startRESTDATA'}	="$1"."$2"."$3"."$4";
					$YOUTUBE_VIDEO{'startCHR'}		="$2"."$3"."$4";
					$YOUTUBE_VIDEO{'startH'}		="$2" if($2 ne "");
					$YOUTUBE_VIDEO{'startM'}		="$3" if($3 ne "");
					$YOUTUBE_VIDEO{'startS'}		="$4" if($4 ne "");
					$YOUTUBE_VIDEO{'startH'}		=~ s/h//i;
					$YOUTUBE_VIDEO{'startM'}		=~ s/m//i;
					$YOUTUBE_VIDEO{'startS'}		=~ s/s//i;
					$YOUTUBE_VIDEO{'startNUM'}		=$YOUTUBE_VIDEO{'startH'}*3600 + $YOUTUBE_VIDEO{'startM'}*60 + $YOUTUBE_VIDEO{'startS'};
				# 2014.02 記述ミスも拾う
				}elsif($YOUTUBE_VIDEO{'otherRESTDATA'}=~ /(t\=)(\d+)/ig){
					$YOUTUBE_VIDEO{'startS'}		=$2;
					$YOUTUBE_VIDEO{'startNUM'}		=$2;
					$YOUTUBE_VIDEO{'startCHR'}="$2"."s";					
	    }

			}

		}else{
			 $YOUTUBE_VIDEO{'id'}	="";
		      }
			}
	# サムネイルのURL作成（youTubeのサムネイル画像のURLは適宜アップデートしてください）

	if($YOUTUBE_VIDEO{'id'} ne ""){
     $tmp_youtube_snl_url="\<img src\=http:\/\/i\.ytimg\.com\/vi\/$YOUTUBE_VIDEO{'id'}\/default\.jpg\ $tmp_snl_url_imgsize>";		    
 		}
		
	 # objectタグのアドレスを取得 旧YouTube/FC2
# 2014.02修正
	 if(($tmp_data=~ /<object(.|\n)*<embed(.|\n)*application\/x-shockwave-flash/i)||($tmp_data=~ /<object(.|\n)*classid/i)){
	  if($tmp_data=~ /<object(.|\n)*<embed(.|\n)*src=(\")?(http\:\/\/)([^\"]*)?(.|\n)*/i){

		# youTubeの場合
		$tmp_yb_url="$4"."$5";

		# すげ替える2011.09修正
		if($tmp_data=~ /http\:\/\/www\.youtube\.com\//i){

		  if($tmp_data=~ /http\:\/\/www\.youtube\.com\/v\/([\-_\.a-zA-Z0-9]+)(\&*)(.|\n)*/ig){
			if($1 ne ""){
			 $YOUTUBE_VIDEO{'id'}	="$1";
			}else{
			 $YOUTUBE_VIDEO{'id'}	="";
			}
		  }
		# 2009.12 new 2010.11.29修正
		# DAILYMOTION埋め込み(idを取得)
	    }elsif($tmp_data=~ /(http\:\/\/www\.dailymotion\.com\/video\/)([_\-a-zA-Z0-9]+)/ig){
			# 置き換える
			$tmp_yb_url="$1"."$2";
			if($2 ne ""){
			 $DAILYMOTION_VIDEO{'id'}	="$2";
			}
#&error("DAILYMOTION_VIDEO $DAILYMOTION_VIDEO{'id'}");

		}
		
		# テキストモード時は、OBJECTをテキストリンクにする
		if($no_object_to_text_link==1){
		
            # 2008.07 fix bug
            # オブジェクトタグを削除して置き換える(旧youTube/dailymotion/ustream等)
			$tmp_data =~ s/\<(\s*)OBJECT(.|\n)*(\/OBJECT\>)(\s*)(\n?)/$tmp_yb_url /ig;

			if(($DAILYMOTION_VIDEO{'id'} ne "")&&($COOKIE{'view_mode'} ne '1-text_only')){
			# サムネイル表示（DAILYMOTIONのサムネイル画像のURLは適宜アップデートしてください）
			 $tmp_dailymotion_snl_url="\<img src\=\"http:\/\/www\.dailymotion\.com\/thumbnail\/160x120\/video\/$DAILYMOTION_VIDEO{'id'}\" $tmp_snl_url_imgsize>";
		     $tmp_data =~ s/(\<a href\=\"https?\:\/\/www\.dailymotion\.com\/video\/[_\-a-z0-9]+\"\>)/$1 $tmp_dailymotion_snl_url/ig;
			}

 		}
		
#		return($tmp_data);
	  }
	 }

	if($PM{'auto_nicovideo_find'}==1){
	 if($tmp_data!~ /<A(\s)(\n?)|<IMA?GE?(.*)|=(\"?)http/i){

	  if($tmp_data=~ /ttp:\/\/([\-a-zA-Z0-9]+)\.nicovideo\.jp\/watch\/([\-a-zA-Z0-9_]+)/i){
          $tmp_data =~ s/[\x80-\x9f\xe0-\xff]./$&\x01/g; # 2バイト文字
	  # 2007.06
	  # 自動ニコニコ動画リンク
	  # IFRAMEだとコメント付きの超小さいリンクになるので、ここで対応
	  # なお、イタズラ防止のため、埋め込み化はひとつだけにする。

		$tmp_bq_opt		.= " style=\"margin: 12px;float: left\"";

		#2011.02.04 ニコニコ外部プレイヤーのテスト
		if($COOKIE{'view_mode'} eq '1-text_only'){
		  $tmp_data =~ s/(http:\/\/[\-a-zA-Z0-9]+\.nicovideo\.jp\/watch\/)([\-a-zA-Z0-9_]*)/\<A HREF="$1$2">\ニコ動 $1$2 \<\/A>/;
		}elsif($MYCGI_ENV{'flash_object_tag_support'} eq 'false'){
		# 旧IFRAME版の仕様
	  		$tmp_data =~ s/http:\/\/([\-a-zA-Z0-9]+)\.nicovideo\.jp\/watch\/([\-a-zA-Z0-9_]+)/\<iframe src="http:\/\/$1\.nicovideo\.jp\/thumb?v=$2" width="440" height="295" scrolling="no" border="1" frameborder="1" align="left" style="margin: 12px;float: left">iframe対応ブラウザでご覧下さい。<\/iframe><P>/;
		}elsif(($COOKIE{'view_mode'} eq 'text_img_type1')||($COOKIE{'view_mode'} eq 'text_img_type11')||($COOKIE{'view_mode'} eq 'text_img_type20')){
		  $tmp_data =~ s/(http:\/\/[\-a-zA-Z0-9]+\.nicovideo\.jp\/watch\/)([\-a-zA-Z_]*)([0-9]*)/\<A HREF="$1$2$3">\<IMG src="http:\/\/tn-skr4\.smilevideo\.jp\/smile\?i=$3" width="128" height="96">ニコ動 \<\/A>/;
		}else{
		  $tmp_data =~ s/http:\/\/([\-a-zA-Z0-9]+)\.nicovideo\.jp\/watch\/([\-a-zA-Z0-9_]+)/\<script type="text\/javascript" src="http:\/\/ext.nicovideo.jp\/thumb_watch\/$2\?w=$tmp_cfds_width&h=$tmp_cfds_height"><\/script><noscript><a href="http:\/\/www.nicovideo.jp\/watch\/$2">【ニコニコ動画】<\/a><\/noscript><BR>/;
		}
		
		$tmp_data =~ tr/\x01//d;
	  }
	 }
	}

	
	# 自動URLリンク

	# 事前準備
	# 2011.09 update
	local($ttmp_youtube_target_sitei)=qq|TARGET="_blank"|;
  		if($HTTP_USER_AGENT=~ /ipod|iphone|android|PSP/i){
  			# ブラウザが複数起動すると閉じるのがしんどい
			$ttmp_youtube_target_sitei="";
  	}

	# テキスト表示の場合
	if(($COOKIE{'view_mode'} eq '1-text_only')||($COOKIE{'view_mode'} eq 'text_img_type20')){

		 # iframe埋め込みをTEXTリンクに戻す
		 # 2014.02 途中再生対応
	     if($YOUTUBE_VIDEO{'idtype'} eq 'iframe'){
	     	# 2014.02.11 update 
			$tmp_data =~ s/<iframe(.|\n)*src\=\"(https?\:\/\/|\/\/)www\.(youtube|youtube\-nocookie)\.com\/embed\/([\-_\.a-zA-Z0-9]+)(\?*)([\&\=\-_\.a-zA-Z0-9]*)(.|\n)*<\/iframe>/https\:\/\/youtu\.be\/$4$5$6/ig;
		 	# 2014.02 途中再生対応
		 	$tmp_data =~ s/start\=(\d+)/t\=$1s/ig;
	     }

			# xvideo等もテキストにする
			$tmp_data =~ s/<iframe(.|\n)*src\=\"https?\:\/\/(.*)\.(xvideos)(\.com|\.jp)\/embedframe\/(\d+)(\?*)([\&\=\-_\.a-zA-Z0-9]*)(.|\n)*<\/iframe>/http\:\/\/www\.xvideos\.com\/video$5/ig;

			# Dailymotion等もテキストにする
			$tmp_data =~ s/<iframe(.|\n)*src\=\"(https?\:\/\/www\.dailymotion\.com\/embed\/video\/)([\&\=\-_\.a-zA-Z0-9]*)\"(.|\n)*<\/iframe>/$2$3/ig;

			# FC2等もテキストにする
			# セキュリティを配慮しつつ、多少のサイト仕様変更には影響されないようにする
			$tmp_data =~ s/<script src\=\"https?\:\/\/static\.fc2\.com\/video\/js\/[\/\-_\.a-zA-Z0-9]{2,40}\.js\"(.|\n|\s)*url\=\"(https?\:\/\/video\.fc2\.com\/ja\/[\/a-zA-Z0-9]{0,10}\/content\/[\/a-zA-Z0-9]{3,30})\"(.|\n|\s)* tl\=\"([^\"]*)\"(.|\n|\s)*charset\=\"UTF-8\"><\/script>/$4 <BR> $2/ig;

			# 未知のサイトもある程度の型にはまっていればテキストにする iframe
			$tmp_data =~ s/<iframe(.|\n)*src\=\"(https?\:\/\/)(.*)(\.com|\.net|\.org|\.tv|\.me|\.jp)\/([\/\?\&\=\-_\.a-zA-Z0-9]{5,40})\"(.|\n)*<\/iframe>/(外部URLです。クリック注意) <BR> $2$3$4\/$5/ig;
			# 未知のサイトもある程度の型にはまっていればテキストにする script
			$tmp_data =~ s/<script(.|\n|\s)*url\=\"(https?\:\/\/)(.*)(\.com|\.net|\.org|\.tv|\.me|\.jp)\/([\/\?\&\=\-_\.a-zA-Z0-9]{5,40})\"(.|\n|\s)*><\/script>/(外部URLです。クリック注意) <BR> $2$3$4\/$5 </ig;


	# アイコン or サムネイル小の時
	}elsif(($COOKIE{'view_mode'} eq 'text_img_type1')||($COOKIE{'view_mode'} eq 'text_img_type11')){

			if($YOUTUBE_VIDEO{'idtype'} eq 'youtu_be01'){
		      $tmp_data =~ s/(https?\:\/\/youtu\.be)([^\s|\:|\<]+)/<A HREF="$1$2" $ttmp_youtube_target_sitei>$tmp_youtube_snl_url .<\/A> \(YouTube\)/ig;
		    }elsif($YOUTUBE_VIDEO{'idtype'} eq 'iframe'){
if($tmp_data =~ /aban503/){
#&error("a-$tmp_data");
}
			  $tmp_data =~ s/<iframe(.|\n)*src\=\"(https?\:\/\/|\/\/)www\.(youtube|youtube\-nocookie)\.com\/embed\/([\-_\.a-zA-Z0-9]+)(\?*)([\&\=\-_\.a-zA-Z0-9]*)(.|\n)*<\/iframe>/<A HREF="https\:\/\/youtu\.be\/$YOUTUBE_VIDEO{'id'}\?t\=$YOUTUBE_VIDEO{'startCHR'}" $ttmp_youtube_target_sitei>$tmp_youtube_snl_url .<\/A> \(YouTube\)cf/ig;
		    }
		    
		    if($tmp_data=~ /\<iframe/){
			 	# 2014.02 xvideo,xhamster等サムネイルが得られないサイト対策
		 		$tmp_data =~ s/ width\=(\"?)(\d+)(\"?) / width\=\"140\" /ig;
		 		$tmp_data =~ s/ height\=(\"?)(\d+)(\"?) / height\=\"125\" /ig;
		    }		    
		    
		    if($tmp_data=~ /\<script/){
			 	# 2014.02 FC2対策
		 		$tmp_data =~ s/ w\=(\"?)(\d+)(\"?) / w\=\"140\" /ig;
		 		$tmp_data =~ s/ h\=(\"?)(\d+)(\"?) / h\=\"125\" /ig;
		    }
		    
	# 通常の埋め込み表示レイアウトモード
	}else{
	
			# Youtubeのサムネイル表示
			# youtu.beをiframeにしてあげる
			if($YOUTUBE_VIDEO{'idtype'} eq 'youtu_be01'){
			 # アイコン or サムネイル小の時
			 if(($COOKIE{'view_mode'} eq 'text_img_type1')||($COOKIE{'view_mode'} eq 'text_img_type11')){
		      $tmp_data =~ s/(https?\:\/\/youtu\.be)([^\s|\:|\<]+)/<A HREF="$1$2" $ttmp_youtube_target_sitei>$tmp_youtube_snl_url .<\/A> \(YouTube\)aaa/ig;
		     }else{
		      if($tmp_data !~ /\<iframe/){
		      # youtu.beをiframe化する
	       		# 埋め込みサイズ補正ルーチンを流用する
	       		&check_flash_and_iframe_img('iframe');
			# 2012.10.19変更(回り込みデザイン)
		        $tmp_data =~ s/(https?\:\/\/youtu\.be)([^\s|\:|\<]+)/\<iframe $w_set $h_set src\=\"http\:\/\/www.youtube.com\/embed\/$YOUTUBE_VIDEO{id}\?start\=$YOUTUBE_VIDEO{'startNUM'}\" frameborder\=\"0\" allowfullscreen align\=\"left\" HSPACE=\"12\" VSPACE=\"6\" style=\"margin: 12px;float: left\"\>\<\/iframe\> /ig;
		        # 影響を防ぐため変数を初期化
		        undef $w_set;
		        undef $h_set;
		      }
		     }
			}

		# 2014.02 Theta360
		if($tmp_data=~ /\-scrt_here_Theta360\-/i){
		# scriptタグは危険だからエスケープしたやつを戻す
		$tmp_data=~ s/\-scrt_here_Theta360\-/<script async src=\"https\:\/\/theta360.com\/widgets.js\" charset=\"utf-8\"><\/script>/ig;
			# レイアウト回りこみを指定
			$tmp_bq_opt		.= " style=\"margin: 12px;float: left\"";
		}

		# 2014.02 FC2等
		# scriptタグがあって、かつそれがビデオ関係っぽいスクリプトの時だけ以下の処理をする
		if($tmp_data=~ /<script(.|\n|\s)*(video|player)(.|\n|\s)*<\/script>/i){

			# 2014.07 update / 2014.11.10 Bug Fix
			# FC2でCSSでfloat指定をすると、先方のスクリプトとの相性で
			# 動画が超小さくなってしまう問題に暫定対処 TODOレイアウト崩れ
			if($tmp_body=~ /<script(.|\n)*fc2.com\//i){
				$tmp_bq_opt	.= " style=\"margin: 12px\"";
			}else{
				# レイアウト回りこみを指定
				$tmp_bq_opt	.= " style=\"margin: 12px;float: left\"";
			}
		}

	}


	# iframeタグがある場合は、elsifへ飛ぶことに注意
	if($tmp_data!~ /<A(\s)(\n?)|<IMA?GE?(.*)|=(\"?)http/i){

	    $tmp_data =~ s/[\x80-\x9f\xe0-\xff]./$&\x01/g; # 2バイト文字

		# 自動URLリンク
		# 日本語ドメインに対応するとこんなかんじ？？
                # 2001.04.10 小修正（改行後を無効にした）
                # 2001.08.20 小修正（tripod等で認識ミスがあるので訂正）
                # 2006.10.11 youTube対策で小修正

		# 従来通り自動URLリンク
		# ただし、クラウドに多い、長いURLエンコード部分は短くする（表示しても人間が判読できないし、safariでレイアウトも乱れるため）
		if($tmp_data =~ /(\=|\/)([\%a-zA-Z0-9]{42})/g){
	     $tmp_data =~ s/(https?\:\/\/[^\s|\:|\<]+)\.(\/?)([\-_\.\!\~\*\'\(\)a-zA-Z0-9\;\/\?\:\@\&\=\+\$\,\%\#]*)(\=|\/)([\%a-zA-Z0-9]{36,330})([\-_\.\!\~\*\'\(\)a-zA-Z0-9\;\/\?\:\@\&\=\+\$\,\%\#]*)/<A HREF="$1.$2$3$4$5$6" $ttmp_youtube_target_sitei>$1.$2$3$4%E6%F3.. $6<\/A>/ig;
		}else{
	     $tmp_data =~ s/(https?\:\/\/[^\s|\:|\<]+)\.(\/?)([\-_\.\!\~\*\'\(\)a-zA-Z0-9\;\/\?\:\@\&\=\+\$\,\%\#]*)/<A HREF="$1.$2$3$4" $ttmp_youtube_target_sitei>$1.$2$3$4<\/A>/ig;
		}
		
		$tmp_data =~ s/(r?ftp\:\/\/[\-_\.\!\~\*\'\(\)a-zA-Z0-9\;\/\:]+)/<A HREF="$1" TARGET="_blank">$1<\/A>/g;

		$tmp_data =~ tr/\x01//d;

#$PM{'auto_japanese_address_find'}=1;

		# 自動住所リンク（Google Map & ストリートビュー） 2013.01 Google API仕様変更を反映
		if($PM{'auto_japanese_address_find'}==1){
# 20120425 update
		    if(($tmp_data=~ /東京|区|市|郡|府|県|北海道|字|町|番地/i)&&($tmp_data!~ /https?\:\/\//i)){

		     # 東京都千代田区内幸町1-1-1
		     if($tmp_data=~ /(東京都|大阪府|京都府|[^\s\>\d]+県|北海道)([^\s\>\d]+)(市|区)([^\s\>\d]+)([0-9０-９]+)(\-|－|丁目|の|ノ)([0-9０-９]+)([\-|－|の|ノ]?)([0-9０-９]?)/ig){
		       $ttmp_jp_geoname="$1$2$3$4$5$6$7$8$9";
		       # iPhoneでおかしくなるのでURLエンコード
		       $ttmp_jp_geoname=~ s/(\W)/'%'.unpack("H2", $1)/ego;
		       $tmp_data =~ s/(東京都|大阪府|京都府|[^\s\>\d]+県|北海道)([^\s\>\d]+)(市|区)([^\s\>\d]+)([0-9０-９]+)(\-|－|丁目|の|ノ)([0-9０-９]+)([\-|－|の|ノ]?)([0-9０-９]?)/<A HREF\=\"http\:\/\/maps.google.co.jp\/maps\?q=$ttmp_jp_geoname&hl=ja\" TARGET=\"_blank\">$1$2$3$4$5$6$7$8$9 <\/A>/ig;
		     }elsif($tmp_data=~ /([^\s\>\d]{1,10})(区|市)([^\s\>\d]{1,10})([0-9０-９]+)(\-|－|丁目|の|ノ)([0-9０-９]+)([\-|－|の|ノ])([0-9０-９]+)/ig){
		       $ttmp_jp_geoname="$1$2$3$4$5$6$7$8$9";
		       # iPhoneでおかしくなるのでURLエンコード
		       $ttmp_jp_geoname=~ s/(\W)/'%'.unpack("H2", $1)/ego;
		       $tmp_data =~ s/([^\s\>\d]{1,10})(区|市)([^\s\>\d]{1,10})([0-9０-９]+)(\-|－|丁目|の|ノ)([0-9０-９]+)([\-|－|の|ノ])([0-9０-９]+)/<A HREF\=\"https\:\/\/maps.google.co.jp\/maps\?q=$ttmp_jp_geoname&hl=ja\" TARGET=\"_blank\">$1$2$3$4$5$6$7$8$9 <\/A>/ig;
		     }
		    }
		}
    # iframeタグがある場合は、ここで初めて処理される
	# youTubeの埋め込みタグ(iframe)対策 2011.06 
	}elsif(($tmp_data!~ /<A(\s)(\n?)|<IMA?GE?(.*)/i)&&($tmp_data=~ /<iframe(.|\n)*src\=\"http:\/\//i)){
			# サムネイル表示（youTubeのサムネイル画像のURLは適宜アップデートしてください）
#		    $tmp_data =~ s/<iframe(.|\n)*src\=\"(https?\:\/\/|\/\/)www\.(youtube|youtube\-nocookie)\.com\/embed\/([\-_\.a-zA-Z0-9]+)(\?*)(.|\n)*<\/iframe>/<A HREF\=\"https\:\/\/youtu\.be\/$2" $ttmp_youtube_target_sitei>$tmp_youtube_snl_url<\/A> \(YouTube\)cd/ig;
	}
	return($tmp_data);
}
#
#=========================#
# 記事データの置換
#=========================#
# 後から記事を編集する場合に用いる
# R6NEW 2001.08.25
# 2002.10 改良

sub replace_data{

	local($target_tid)	= $_[0];# 引数 ターゲット記事のID
	local($tmp_file)	= $_[1];# 処理するログファイル名

	local($tmp_rm_key);	# 記事に設定されていた削除キー

  	if($ENV{'REQUEST_METHOD'} ne 'POST'){
		&error(" セキュリティ警告 <BR> GETによる記事投稿はＮＧです ");
	}

	&form_check;

	if($error_message ne ''){
		&error($error_message);
		exit;
	}

#	# 記事の日付表示（変更可能)
#	$date_data = "\[$year/$month/$mday,$hour:$min:$sec\]";

	# セパレータとして問題あるものを、事前に置換
	$subject=&Enc_EQ("$subject");

	undef $tmp_data;

	$all_message=0;


	# データ読込み
	open(IN, "$tmp_file")|| &error(" 設定エラー．データ保存用ファイル\"$tmp_file\"が見つかりません．処理は中断されました．");
	eval "flock(IN,1);" if($PM{'flock'} == 1 );

            	@main = <IN>;

	eval "flock(IN,8);" if($PM{'flock'} == 1 );
	close(IN);

        # 暗号化
	if(($rmkey ne "no_key")&&($rmkey ne "")){
		$rmkey		= &make_pass("$rmkey");
	}

	undef $match_count;
	undef @SEP_DATA;
	local($tmp_opt_form_data);

	foreach $file_line(@main){

		# HEADER保存 (将来への拡張もここで対応)
		if($file_line=~ /^\#?\,param_/i){

			push(@TMPMESSAGE, $file_line);

		}elsif(($file_line=~ /$target_tid/)&&($match_count < 1)){

			$match_count++;
			@SEP_DATA=split(/\t/,$file_line);# TABで一度分解する

			$tmp_rm_key="$SEP_DATA[9]";

#&error("$subject $target_tid mc $match_count 9 $tmp_rm_key");

			# 上書きするものはここで上書き代入
			# 前のデータ保存をそのまま保存するものはコメントアウト
			$SEP_DATA[0]="$subject";
			$SEP_DATA[1]="$name";
			$SEP_DATA[2]="$email";
#			$SEP_DATA[3]="$date_data";

			 # optは保存する必要がある
			 if($SEP_DATA[4]=~ /(.*)<!--opt\:(.*)-->/i){

				$tmp_opt_form_data="$2";

				# 旧データを取得して保持
			        undef %OPTDATA;
				foreach ( split(/;/,$tmp_opt_form_data)){
					local($name,$value) = split(/\=/);
					$value=&Dec_EQ("$value");
					if($name=~ /^opt(.+)$/){
					  $OPTDATA{"$name"}	= $value;
					}
				}
				# 上書きすべきパラメータは、適宜上書き
				foreach $p_key(keys %FORM){
				  if($p_key=~ /^opt(.+)/){
					$OPTDATA{$p_key}="$FORM{$p_key}";
				  }
				}
				# 結合して$opt_dataを作る
				foreach $p_key(sort keys %OPTDATA){
				  $tmp_data=&Enc_EQ($OPTDATA{$p_key});
				  $opt_data.="$p_key"."\="."$tmp_data"."\;";
				  undef $tmp_data;
				}
			        undef %OPTDATA;
				$SEP_DATA[4]="$body<\!--opt\:$opt_data-->";
			}else{
				# ここは通らないはず
				$SEP_DATA[4]="$body<\!--opt\:-->";
			}
#			$SEP_DATA[5]="$img_location";
			if($FORM{'amode'} eq "post_webparts"){
			# WebPartsの場合、タイトルだけ交換するケースが必要
			  if($SEP_DATA[6]=~ /(.*)<!--(.*)-->/i){
				$SEP_DATA[6]="$imgtitle"."<!--"."$2"."-->";
			  }
			}else{
#			$SEP_DATA[6]="$imgtitle<\!--dsize=$img_data_size;type=$img_type;width=$img_width;height=$img_height;hw_racio=$img_hw_racio;-->";
			}
#			$SEP_DATA[7]="$new_seq_no";
#			$SEP_DATA[8]="$FORM{'blood'}";
#			$SEP_DATA[9]="$rm_key";
#			$SEP_DATA[10]="$unq_id";
			$SEP_DATA[11]="";

			# 結合して復元する
			for($numb=0;$numb < scalar(@SEP_DATA) ;$numb++){
				$new_message.="$SEP_DATA[$numb]"."\t";
			}
			push(@TMPMESSAGE, $new_message);
		}else{
			push(@TMPMESSAGE, $file_line);
		}
	}

	# パスワードをチェック(修正は厳密にチェック。生パス必要)
	if((&check_passwd("$FORM{'entry_passwd'}","$tmp_rm_key","0")==1)||(&check_passwd("$FORM{'entry_passwd'}","$admin_passwd","1")==1)||($FORM{'amode'} eq "post_webparts")){
#		&error("一致しました。既削除キー $tmp_rm_key 入力されたパスワード$FORM{'rm_key'} ");
	}else{
		&error("パスワードが違います。","記事の修正には管理者パスワード、あるいは投稿時に投稿者が入力したパスワードが必要です。<BR>再度パスワードを入力してください ");
	}

	# データ書き出し開始
	open(OUT, "> $tmp_file")|| &error(" 設定エラー．データ用保存ファイル\"$tmp_file\"にデータを書込むことができませんでした．<BR>\"$tmp_file\"という名前のファイルが正しい位置に存在しないか、あるいは、書込み許可がないためだと思われます．<BR>処理は中断されました．");

	eval "flock(OUT,2);" if($PM{'flock'} == 1 );
	foreach $file_line(@TMPMESSAGE){
		$file_line=~ s/\n//g;
		$file_line=~ s/\r//g;
		print OUT "$file_line"."\n";
	}
	eval "flock(OUT,8);" if($PM{'flock'} == 1 );
	close(OUT);
#&error("$subject $target_tid mc $match_count");
}
#
#=========================#
# 記事データの並び替え
#=========================#
# 後から記事の順番を変更する場合に用いる
# R6NEW 2002.07.20
sub sort_kiji{

	local($target_tid)	= $_[0];# 引数1 順番変更するターゲット記事のID
	local($target_ins_tid)	= $_[1];# 引数2 挿入POINTのID
	local($tmp_ins_p)	= $_[2];# 引数3 挿入POINTの後ろか前か
	local($tmp_file)	= $_[3];# 引数4 処理するログファイル名

	local($store_file_line)	= "";	# 一時保存
	local($ins_p_find_flag)	= "";	# 挿入個所確認フラグ（安全のため）

	# 事前チェック
  	if(($target_tid eq "")||($target_ins_tid eq "")){
		&error(" エラー <BR> 該当記事idがありません ");
	}

	$all_message=0;

	# データ読込み
	open(IN, "$tmp_file")|| &error(" 設定エラー．データ保存用ファイル\"$tmp_file\"が見つかりません．処理は中断されました．");
	eval "flock(IN,1);" if($PM{'flock'} == 1 );
       	@main = <IN>;
	eval "flock(IN,8);" if($PM{'flock'} == 1 );
	close(IN);

	undef $match_count;
	undef @SEP_DATA;

	foreach $file_line(@main){

		# HEADER保存 (将来への拡張もここで対応)
		if($file_line=~ /^\#?\,param_/i){
			push(@TMPMESSAGE, $file_line);
		}elsif(($file_line=~ /$target_tid/)&&($match_count < 1)){
			$match_count++;
			@SEP_DATA=split(/\t/,$file_line);# TABで一度分解する
			if($target_tid eq "$SEP_DATA[10]"){
				$store_file_line="$file_line";
			}else{
			 push(@TMPMESSAGE, $file_line);
			}
		# 挿入ポイントの存在も確認しておく
		}elsif($file_line=~ /$target_ins_tid/){
			@SEP_DATA=split(/\t/,$file_line);# TABで一度分解する
			if($target_ins_tid eq "$SEP_DATA[10]"){
				$ins_p_find_flag=1;
			}
			push(@TMPMESSAGE, $file_line);
		}else{
			push(@TMPMESSAGE, $file_line);
		}
	}

	# 処理前チェック。挿入ポイントがないときはソートを中止（安全のため）
	if($ins_p_find_flag != 1 ){
		&error(" エラー 。順番変更中にデータ矛盾発生。データ保全のため処理を中止します ");
	}

#&error(" $target_tid-$target_ins_tid-$tmp_ins_p-$tmp_file-$store_file_line");


	# データ書き出し開始
	$store_file_line=~ s/\n//g;
	$store_file_line=~ s/\r//g;

	open(OUT, "> $tmp_file")|| &error(" 設定エラー．データ用保存ファイル\"$tmp_file\"にデータを書込むことができませんでした．<BR>\"$tmp_file\"という名前のファイルが正しい位置に存在しないか、あるいは、書込み許可がないためだと思われます．<BR>処理は中断されました．");

	eval "flock(OUT,2);" if($PM{'flock'} == 1 );
	foreach $file_line(@TMPMESSAGE){
		if($file_line=~ /$target_ins_tid/){
		  @SEP_DATA=split(/\t/,$file_line);# TABで一度分解する
		  if($target_ins_tid eq "$SEP_DATA[10]"){
		  # ターゲットの前に挿入
		  	if($tmp_ins_p eq "pre"){
		   	  print OUT "$store_file_line"."\n";
		 	}

		 	$file_line=~ s/\n//g;
		 	$file_line=~ s/\r//g;
		 	print OUT "$file_line"."\n";

		 	# ターゲットの後ろに挿入
		 	if($tmp_ins_p ne "pre"){
		 	  print OUT "$store_file_line"."\n";
		 	}
	  	  }else{
		 	$file_line=~ s/\n//g;
		 	$file_line=~ s/\r//g;
		 	print OUT "$file_line"."\n";
		  }
		}else{
		  $file_line=~ s/\n//g;
		  $file_line=~ s/\r//g;
		  print OUT "$file_line"."\n";
		}
	}
	eval "flock(OUT,8);" if($PM{'flock'} == 1 );
	close(OUT);
}
#
#==================================#
# 同一人物からの２重投稿の防止
#==================================#
# 一人１エントリしか作れないようにする。
# 出会い掲示板用。配布版では未サポート
#
sub check_double_post{
#	&error(" 配布版では未サポートの機\能\です ");
	# メールアドレスをチェックし、既に掲示板上にあるエントリの
	# メールアドレスと重なる場合は新規投稿を失敗させる。
}
#
#==================================#
# 記事を削除して良いかを確認させる
#==================================#
# 選択された記事一つを表示して、その記事を消すための
# 削除パスワードの入力を促す。
# 出会い掲示板SP用。配布版では未サポート
#
sub output_remove_select_html{
	&error(" 出会い掲示板SP用。配布版では未サポートの機\能\です ");
}
#
#=======================================#
# <ウェブパーツデータファイルを読込>    #
#=======================================#
#
sub read_web_parts_data{

	local($tmp_mes_line);
	local($tmp_file)	= $_[0];# 処理するログファイル名

	# メッセージを読み込む
	open(IN, "$tmp_file")|| &error(" 設定エラー．データ保存用ファイル\"$tmp_file\"が見つかりません．処理は中断されました．");

	   eval "flock(IN,1);" if($PM{'flock'} == 1 );
	   while(<IN>){

		# HEADER保存 (将来への拡張もここで対応)
		if($_ =~ /^\#?\,param_/i){
			push(@WP_HEAD_MESSAGE, $_);
		}
		# 記事をバッファに入れる
		if($_ =~ /^([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]*)\t([^\t]*)/){
			$tmp_mes_line="$_";
			chop($tmp_mes_line);
			push(@WP_MESSAGE, $tmp_mes_line);
		}
	   }
	eval "flock(IN,8);" if($PM{'flock'} == 1 );
	close(IN);
}
#
#===============================================#
#     <編集するために、記事データを呼び出す>    #
#===============================================#
# R6NEW (正式版では機能を削除する)
# 記事データを編集・修正するために、UIDをキーにして呼び出す
# 出力は編集入力フォームの初期値としてロードする
#
sub load_target_kiji{

	local($t_pattern)=$_[0];	# 記事UIDを引数として取得
	local($tmp_file)= $_[1];	# 処理するログファイル名

	undef @T_MESSAGE;
	local($tc_message);
	local($tmp_unq_id);

	# IDを持つ記事を一つ選択する
	open(READ, "$tmp_file");
		eval "flock(READ,1);" if($PM{'flock'} == 1 );
		while(<READ>){
			if($file_line=~ /^\#?\,param_/i){
			}elsif($_ =~ /^([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]*)\t([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)/){
			  $tmp_unq_id		= $11;	# 固有ID(時刻ベース)
			  if($tmp_unq_id eq "$t_pattern"){
				push(@T_MESSAGE, $_);
				$tc_message++;
			  }
			}
		}
		eval "flock(READ,8);" if($PM{'flock'} == 1 );
	close(READ);

	# 一つだけ選択できたか、エラーチェックする
	if($tc_message > 1){
	  &error(" 複数の記事とマッチ。異常のため、終了します <BR>検索パターン $t_patterm ");
	}elsif($tc_message==0){
	  &error(" マッチする記事がありませんでした。<BR>検索ID $t_patterm ");
	}

	# 正常なら、記事データを分解する
	if($T_MESSAGE[0] =~ /^([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]+)\t([^\t]*)\t([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)\t?([^\t]*)/){
		$tmp_subject		= $1;
		$tmp_name		= $2;
		$tmp_email		= $3;
		$tmp_date		= $4;
		$tmp_body		= $5;
		$tmp_img_location	= $6;
		$tmp_img_title		= $7;
		$tmp_seq_no		= $8;	# 連番
		$tmp_blood_name		= $9;	# 親の血統ID(子供のみ持つ)
		$tmp_rm_key		= $10;	# 削除キー
		$tmp_unq_id		= $11;	# 固有ID(時刻ベース)
		$new_p1			= $12;
		$new_p2			= $13;

		$tmp_subject=&Dec_EQ("$tmp_subject");

		# 予備入力項目パラメータを復元
		# bodyの中に、コメントアウト形式でデータは隠し保存されている
		# 書式<!--opt:パラメータ名=値;パラメータ名2=値2・・・-->
		#<!--opt:と-->を除きパラメータ部を抽出する処理
		if($tmp_body ne ''){
		  ($tmp_body,$opt_form_data)	=split(/<\!--opt:/,$tmp_body);
		  $opt_form_data		=~ s/-->//g;
		}

		$tmp_body=~ s/\<!-- user：\s([^>]*)(\s*)--\>//g;

	# 入力フォームのCOOKIEの初期値として出力する

		#パラメータ$opt_form_dataが追加されている場合．
		if($opt_form_data ne ''){
			foreach ( split(/;/,$opt_form_data)){
				local($name,$value) = split(/\=/);
				$value=&Dec_EQ("$value");

				if($name=~ /^opt_data_(.+)$/){
				  $OPTDATA{"opt$1"}	= $value;
				  $OPT_FORM_DATA{"opt$1"}= $value;# 旧R5互換用
				  $COOKIE{"opt$1"}	="$value";
				# 徐々にこちらへシフト
				}elsif($name=~ /^opt(.+)$/){
				  $OPTDATA{"$name"}	= $value;
				  $OPT_FORM_DATA{"$name"}= $value;# 旧R5互換用
				  $COOKIE{$name}	="$value";
				}
			}
		}else{
			undef %OPTDATA;
	        	undef %OPT_FORM_DATA;# 旧R5互換用
		}

		$COOKIE{'subject'}	="$tmp_subject";
		$COOKIE{'name'}		="$tmp_name";

		$COOKIE{'email'}	="$tmp_email";
		$COOKIE{'email'}	=~ s/(\s+)no_email//i;

		$COOKIE{'body'}		="$tmp_body";
		$COOKIE{'body'}		=~ s/<BR>/\n/gi;

		# WebPartsの場合は、画像のタイトル名を変更できる
		if($FORM{'amode'} eq "icon_edit"){
		  $tmp_img_title=~ s/\<!--(.*)--\>//g;
		  $COOKIE{'imgtitle'}	="$tmp_img_title";
		}

		$no_cookie_for_subject=0;	# 題名クッキーの無効化を解除
		$use_passwd_flag=1;
		 # 2006.04 SPAM対策で修正
		 $POSTADDP{'UPLOADFORM'}="$POSTADDP{'UPLOADFORM'}\n"."<INPUT TYPE=\"HIDDEN\" NAME=\"apasswd\" VALUE=\"$COOKIEAD{'apasswd'}\">";
	}
}
#
#===================================#
# 管理者画面のメイン処理部
#===================================#
sub amode_done{

    # 管理モード色にする
    $PM{'orig_body_bgcolor'}="$PM{'body_bgcolor'}"; # 旧全体の背景色を記憶

    if($FORM{'amode'} ne ''){
	$PM{'body_bgcolor'}	="#B0B0D0";		# 全体の背景色
	$PM{'body_text'}	="#000000";		# 基本フォント色
	$PM{'body_link'}	="#4040FF";		# リンク色
	$PM{'body_vlink'}	="#0000FF";		# 既アクセスリンク色
	$PM{'body_background'}	="";			# 背景画像名

	$res_table_sitei="bgcolor=#F0E0D6";		# 返信背景色

	# 2014.11.14 修正(削除済み動画の管理効率アップのために、管理メニュー時は１ページあたりの親記事表示数を15に増やす)
	# ただし、20以上にすると、埋め込み動画が多い場合、Flashプレイヤーがメモリを使い尽くし
	# ブラウザがクラッシュする可能性があるので、15固定にする。

	$disp_message 		=15;


	&read_cookie;# クッキーを読込む(パスの関係でPOST渡しするが、その場合は読まれないため)
	if(&check_passwd("$COOKIEAD{'apasswd'}","$admin_passwd","0")!=1){
	    &error(" 管理者メニュー パスワードエラー ","","1");
	}
    }

    if($FORM{'amode'} eq 'icon_admin'){
      if($EXTCFG{'type'}!~ /icon/i){
	    &error(" この掲示板には、<a href=http://www.big.or.jp/~talk/t-club/soft/mini_r6/imgboard_newicon.cgi target=_blank>アイコン付き掲示板</a>化用外部設定ファイルがまだ追加されていませんので、この機\能\は使えません。 ","","1");
      }
	$use_passwd_flag=1; # パスワード欄を出す
	$POSTADDP{'MEMBERPASS'}=qq|←ここは自動で管理パスワードが入ります。もし空欄になっていた場合は、「<B>管理者パスワード</B>」を入れてください（ 管理者専用アイコンを一般ユーザが無断使用しないように、管理者本人であることを厳正にチェックします） |;
	$COOKIE{'entry_passwd'}="$COOKIEAD{'apasswd'}";
	$amode_done_mes01=" (管理者専用アイコンを選べるモード) ";

	# jump_htmlの飛び先を指定
	$gvar_cgi_add_url="\?page=1&p1=$FORM{'p1'}&p2=$FORM{'p2'}&amode=icon_admin"; 

    }elsif($FORM{'amode'} eq 'select_edit'){

	$amode_done_mes01=" (内容修正・編集モード)(1ページ$disp_message件) ";
	$POSTADDP{'MEMBERPASS'}=qq| ←内容修正・編集時は、イタズラ防止のため、管理者本人で<BR>あることを厳正にチェックします：お手数ですが、会員パス欄に「<B>管理者パスワード</B>」を入れてください |;

	# 修正時はクッキーの交換を防ぐため、記憶しない。従って、補助しない。
	$COOKIE{'entry_passwd'}="";

	# 修正は厳密にチェック。生パス必要。チェックはreplace_data内

    }elsif($FORM{'amode'} eq 'show_ip'){

	if(($FORM{'mode'} eq "keitai_menu")||($FORM{'mode'} eq "disp_admin_check_menu")){
	    &error(" IP表\示\モードの場合はこのメニューは無効です。一度管理者モードを終了してください  ","","1");
	}
	$no_disp_RH_in_HTML_sorce=-1;	# HTMLソースにリモホを表示しない
	$use_ip_privacy_filter=0;	# プライバシー保護のためIPアドレスの一部を伏せ字に
	$amode_done_mes01=" (投稿記事<a href=http://www.mse.co.jp/ip_domain/ target=_blank>IP確認</a>モード) ";
    }elsif($FORM{'amode'} eq 'post_webparts'){

	# 初期値の上書き
	$CHECK{'name'}		=1;	# 名前 （デフォルト1）
	$CHECK{'email'}		=0;	# email（デフォルト1）
	$CHECK{'subject'}	=0;	# 題名 （デフォルト0）
	$CHECK{'body'}		=0;	# 本文 （デフォルト0）
	$CHECK{'img'}		=1;	# 添付画像（デフォルト0）
	$CHECK{'rmkey'}		=0;	# 削除キー（デフォルト0）# ←現在未使用
	$CHECK_E{'img'}		=qq|エラー。添付画像は必須です。<BR>|;
	$CHECK{'optA'}		=0;
	$CHECK{'optB'}		=0;
	$CHECK{'optC'}		=0;
	$CHECK{'optD'}		=0;

	$list_max_message=309;			# 3x70 レイアウト程度
	$list_max_message=$list_max_message-8;	# bit誤差修正
	$max_message=int($list_max_message/2);#
	$limit_wp_max_message=$max_message;#
	$allow_other_multimedia_data=0;	# セキュリティ対策

	if($FORM{'prebbsaction'} eq 'edit_form'){# 置換モードの場合
		$CHECK{'img'}		=0;	# 添付画像（デフォルト0）
		&replace_data("$FORM{'target'}","$PM{'icon_data_file'}");# 修正処理
	}else{
		&check_double_post("$FORM{'email'}","2","1");# 2重投稿チェック
		&post_data("$PM{'icon_data_file'}");	# 投稿処理
	}
	# jump_htmlの飛び先を指定
	$gvar_cgi_add_url="\?page=1&p1=$FORM{'p1'}&p2=$FORM{'p2'}&amode=disp_webparts"; 
	&jump_html;				# パラメータクリア用ＨＴＭＬ
	exit;					# 終了

    }elsif($FORM{'amode'} eq 'remove_webparts'){

	$file		= "$PM{'icon_data_file'}";

	# jump_htmlの飛び先を指定
	$gvar_cgi_add_url="\?page=1&p1=$FORM{'p1'}&p2=$FORM{'p2'}&amode=disp_webparts"; 

    }elsif($FORM{'amode'} eq 'icon_sort_up'){

	# jump_htmlの飛び先を指定
	$gvar_cgi_add_url="\?page=1&p1=$FORM{'p1'}&p2=$FORM{'p2'}&amode=disp_webparts#$FORM{'target'}"; 

	# target_uid,inspoint_uid,pre_or_after,target_logname
	&sort_kiji("$FORM{'target'}","$FORM{'insuid'}","pre","$PM{'icon_data_file'}");

	&jump_html;				# パラメータクリア用ＨＴＭＬ
	exit;					# 終了

    }elsif($FORM{'amode'} eq 'icon_edit'){

	$file		= "$PM{'icon_data_file'}";


    }elsif($FORM{'amode'} eq 'disp_webparts'){

	$amode_done_mes01=" パーツ（アイコン・背景画像等）管理モード  ";
	$FORM{'amode'} 	= "remove_webparts";	# フォーム実行後のアクションを指定
	$show_img_on_board=1;
	$on_board_img_size=3;
	$CIMGSIZE{'smooze_mode'}=0;
	$user_selected_view_mode=0;
	$PM{'use_rep'} 		=0;
	$PM{'res_go_up'} 	=0;
	# 2013.01.10 修正
	$disp_message 		=301;
	$CHECK{'img'}		=1;	# 添付画像（デフォルト0）
	$PM{'INS_POINT_TOP02'}  =qq|ーーーー管理者だけが投稿・削除のできる画像パーツ置き場ですーーー</center><BR><TABLE border=1 bgcolor=white><TR><TD>表\のimgboardで使うアイコン・背景画像等の（半永続的な）置き場としてご利用いただけます。
<LI>パーツは表\のimgboardの画像アップロード先($img_dir)と同じフォルダに保存されますが、<BR>
表\のimgboardの記事とは別管理になります（表\の記事と無関係に半永続的に保存されます）。
<LI>パーツは最大150個まで、ここに保存できます
<LI>パーツの削除は必ずこの画面から行ってください。
<LI>ユーザが既にアイコンとして使っている画像を不用意に削除すると、過去の記事に付いているアイコンが「X状態」になるのでアイコンを削除する場合はその点に注意してください。
<LI>ここでアイコン画像として分類して登録した画像は、アイコン付き掲示板化用外部設定ファイルを使うと、表\のimgboardにおいてアイコン選択メニューに自動ロードされます。
<LI>表\のimgboardの背景画像等として使う場合は、パーツのURLを以下で確認してどこかにメモし、適宜HTMLにURLを埋め込んで使ってください（すいません。背景画像は手動です）。
</TD></TR></TABLE><CENTER>|;

#
	if($COOKIE{'entry_passwd'} eq ""){
	  $COOKIE{'entry_passwd'}="$COOKIEAD{'apasswd'}";
	}

	print "Content-type: text/html"."$Netscape4x_ch_set"."\n\n";
	&top_html;
	&output_wp_upload_form;			# 入力フォームを表示
	&output_html("$PM{'icon_data_file'}");		# 掲示板を表示
	exit;

    }elsif($FORM{'amode'} eq 'change_set'){
	if(&check_passwd("$FORM{'apasswd'}","$admin_passwd","0")!=1){
	    &error(" パスワードエラー ","","1");
	}
    }else{
	$amode_done_mes01="";
    }
}
#===================================================#
#     <ＨＴＭＬ--管理メニュー(共通ベース)>          #
#===================================================#
#
#
sub output_admin_base_HTML{

 local($tmp_tm)		=$_[0]; # タイトル
 local($tmp_mes01)	=$_[1]; # メッセージ１
 local($tmp_mes02)	=$_[2]; # メッセージ２
 local($tmp_exit_f)	=$_[3]; # 終了ボタンを出す
 local($tmp_exit_mes)	=$_[4]; # 終了ボタンのタイトル
 local($tmp_no_bodyf_f)	=$_[5]; # 下部の</BODY>を入れないときは1
 local($tmp_send_pass)	=$_[6]; # パスワードをカスケードする時は1

 local($mes_p2);

 if($tmp_send_pass==1){
	$mes_p2=qq|<INPUT TYPE=HIDDEN NAME="apasswd" VALUE="$COOKIEAD{'apasswd'}">\n|;
 }

print<<HTML_END;
<HTML>
<HEAD>
<meta name="viewport" content="width=480">

<!-- スタイルとJavascriptはtop_css_and_jscript_htmlで定義してください -->
HTML_END

#&top_css_and_jscript_html;

print<<HTML_END;
</HEAD>
<BODY BGCOLOR=#B0B0D0>
<TABLE bgcolor=blue width="99%">
<TR>
 <TD>
  <B><font color=white> 画像Upload掲示板</font></B>
 </TD>
</TR>
</TABLE>

<BR>
<UL>
$tmp_tm <BR>
<P>
$tmp_mes01
<P>
$tmp_mes02
<P>
HTML_END

print "$output_admin_block01_HTML\n";

if($tmp_exit_f == 1){
print<<HTML_END;
<CENTER>
<FORM METHOD=GET action="$cgi_name">
<INPUT TYPE=HIDDEN NAME="page" VALUE="$FORM{'page'}">
<INPUT TYPE=HIDDEN NAME="amode" VALUE="$FORM{'amode'}">
<INPUT TYPE="HIDDEN" NAME="p1" VALUE="$FORM{'p1'}">
<INPUT TYPE="HIDDEN" NAME="p2" VALUE="$FORM{'p2'}">
$mes_p2
<INPUT ID=btnAE1 TYPE=SUBMIT VALUE="$tmp_exit_mes 終了" $output_button_px>
</FORM>
</CENTER>
HTML_END
}

if($tmp_no_bodyf_f != 1){
print<<HTML_END;
</BODY>
</HTML>
HTML_END
}

undef $output_admin_block01_HTML; # 初期化

}
#
#===============================================#
#     <ＨＴＭＬ--管理メニュー(ワード検索)>      #
#===============================================#
#
#  管理メニュー(ワード検索メニュー)用のＨＴＭＬです．
#
sub output_search_menu_HTML{

	local($mes_p1);
	local($mes_p2);

	if($FORM{'MatchMode'} eq "OR"){
		$mes_p1="selected";
	}

	if($FORM{'amode'} eq "show_ip"){
		$mes_p2=qq|<INPUT TYPE=HIDDEN NAME="apasswd" VALUE="$COOKIEAD{'apasswd'}">\n|;
	}

$output_admin_block01_HTML=qq|<FORM METHOD=POST action="$cgi_name">
<INPUT TYPE=HIDDEN NAME="mode" VALUE="search_menu">
<INPUT TYPE=HIDDEN NAME="amode" VALUE="$FORM{'amode'}">
$mes_p2<INPUT TYPE="HIDDEN" NAME="p1" VALUE="$FORM{'p1'}">
<INPUT TYPE="HIDDEN" NAME="p2" VALUE="$FORM{'p2'}">

<BR>
<CENTER>
<TABLE border=0 bgcolor=#999999>
<TR>
<TD><INPUT TYPE=TEXT SIZE=25 NAME="SearchWords" $output_button_px MAXLENGTH=40 VALUE="$FORM{'SearchWords'}">
<SELECT NAME="MatchMode" $output_button_px>
<OPTION VALUE="AND">AND 検索
<OPTION VALUE="OR" $mes_p1>OR 検索
</SELECT>
</TD>
</TR>
<TR>
<TD>
<INPUT ID=btnSS1 TYPE=SUBMIT VALUE="検索実行" $output_button_px>
</TD>
</TR>
</TABLE>
</CENTER>
<BR><BR><BR>
</UL>
</FORM>|;

&output_admin_base_HTML(" ワード検索 "," 記事の全文検索を行います。複合のワードを入力する場合は半角スペースで各単語を区切って入力してください ","","1"," ワード検索 ","1","0");

}
#
sub output_search_menu_HTML2{
print<<HTML_END;
</BODY>
</HTML>
HTML_END

}
#=====================================#
#     <ＨＴＭＬ--管理者確認>          #
#=====================================#
#
#  管理者確認用のＨＴＭＬです．
#
sub output_admin_check_HTML{

$output_admin_block01_HTML=qq|<CENTER>
<FORM ACTION="$cgi_name" METHOD="POST" NAME="admincheck">
管理者パスワード\*<BR>
<INPUT TYPE="password" NAME="apasswd" $output_button_px SIZE="10" VALUE="$COOKIE{'apasswd'}">
<INPUT TYPE="hidden" NAME="mode" VALUE="disp_admin_menu">
<INPUT TYPE="hidden" NAME="amode" VALUE="$FORM{'amode'}">
<INPUT TYPE="HIDDEN" NAME="p1" VALUE="$FORM{'p1'}">
<INPUT TYPE="HIDDEN" NAME="p2" VALUE="$FORM{'p2'}">
<BR>
<INPUT TYPE="submit" $output_button_px VALUE="OK">
</FORM>
</CENTER><P>
<UL><font size=-1 color=gray>
＊管理ができるのは、管理者のみです<BR>
＊これ以降のメニューはクッキー必須です。クッキーを有効にしてください<BR>
＊<font color=red>記事の削除機\能\は、管理メニューにはありません。<BR>掲示板から直接削除できますので、掲示板下部の説明をお読みください</font><BR>
</font>
</UL><P><P>|;

&output_admin_base_HTML(" -管理者確認- "," 管理者パスワードを入れて下さい ","","1"," 管理者確認 ","");

}
#
#=====================================#
#     <ＨＴＭＬ--管理メニュー>        #
#=====================================#
#
#  管理メニュー用のＨＴＭＬです．カスタマイズの必要はありません。
#
sub output_admin_menu_HTML{

	$FORM{'apasswd'}=&make_pass($FORM{'apasswd'});

# 2002.05.18 add for トクトクユーザ
	local($mes_01);
	if($SERVER_NAME=~ /tok2\.com/){
	  $mes_01=qq|<META http-equiv="Set-Cookie" content="$tok2_cookie">|;
	}

print<<HTML_END;
<HTML lang="ja">
<HEAD>
$mes_01
<meta name="viewport" content="width=480">
</HEAD>
<BODY BGCOLOR=#B0B0D0>

<TABLE bgcolor=blue width="99%">
<TR>
<TD>
<B><font color=white> 画像Upload掲示板</font></B>
</TD>
</TR>
</TABLE>

<P>
<UL>
管理者メニューです<BR>
</UL>
<P>

<CENTER>
<FORM ACTION="$cgi_name" METHOD="POST" NAME="admincheck">
メニューを選択して、OKを押してください\*<BR>
<P>
<INPUT TYPE="HIDDEN" NAME="p1" VALUE="$FORM{'p1'}">
<INPUT TYPE="HIDDEN" NAME="p2" VALUE="$FORM{'p2'}">
<SELECT name=amode>
<OPTION value="icon_admin">管理者専用のアイコンを使って、新記事を投稿する
<OPTION value="select_edit">既存の記事を編集・修正する（文章のみ可）
<OPTION value="show_ip">記事投稿者のＩＰ情報を調べる
<OPTION value="disp_webparts">Webパーツ（アイコン・背景画像）管理画面を出す
</SELECT>
<BR>
<INPUT TYPE="submit" $output_button_px VALUE=" OK ">
</FORM>
</CENTER>

<CENTER>
<BR>
<BR>
<BR>
[<a href="$cgi_name?page=$FORM{'page'}">戻る</a>]<BR>
</CENTER>

twitter（ログイン後クリックしてください）<BR>
<a href="http://twitter.com/search?q=%23imgboard" target="_blank">画像掲示板(一般向け)情報をtwitterで検索(#imgboard)</a><BR>
<BR>

その他<BR>
→<a href="http://www.big.or.jp/~talk/t-club/soft/faq01/bbs.cgi">特報CGIのFAQを検索(全文検索可\能\)</a><BR>
→<a href="http://www.big.or.jp/~talk/t-club/soft/mini_r6/index.cgi#hist">R6の更新情報をチェック</a><BR>
→<a href="http://www.big.or.jp/~talk/t-club/soft/mini_r6/index.cgi#hist">特報からのお知らせ</a><BR>
→<a href="http://www.big.or.jp/~talk/t-club/soft/room01/imgboard_ftp.cgi">最新の外部設定ファイルを探す</a><BR>
<BR>
他の特報製CGIの紹介<BR>
[<a href="http://www.big.or.jp/~talk/t-club/soft/mini_2013/imgboard.cgi">画像自動リサイズ、ガラパゴス携帯データ対応、オリジナル名で保存・HTMLキャッシュ作成、imgboard 2015の紹介</a>]<BR>

</BODY>
</HTML>
HTML_END
}
#
#=======================================================#
#     <ＨＴＭＬ--Webパーツ投稿用フォーム>               #
#=======================================================#
#
sub output_wp_upload_form{
&ext_config_icon_form_pre if($EXTSUB{'icon_form_pre'} == 1 );
&auto_omit_disp;

# 修正時は画像をアップロードさせない
 if($FORM{'bbsaction'} eq 'edit_form'){
	$cm_out_img_h='<!--';
	$cm_out_img_f='-->';
 }
 $SEL{'icon_admin'}="";
 $SEL{'icon_norm01'}="";
 $SEL{'sozai_background'}="";
 $SEL{'other'}="";

 # icon名
 local($ie_tmp_img_title)="$COOKIE{'imgtitle'}";
 if($ie_tmp_img_title=~ /img200/i){
	$ie_tmp_img_title="";
 }

 foreach(keys %SEL){
  if($COOKIE{'subject'}=~ /$_/i){
	$SEL{$_}="selected";
	last;
  }
 }
 if($COOKIE{'name'} eq ""){
   $COOKIE{'name'}=" --- ";
 }

print<<HTML_END;
<!-- フォーム入力部・・・ここはあまり変更しない方がいいでしょう -->
<FORM ACTION="$cgi_name" METHOD="POST" ENCTYPE="multipart/form-data">
<INPUT TYPE="HIDDEN" NAME="bbsaction" VALUE="post">
<INPUT TYPE="HIDDEN" NAME="amode" VALUE="post_webparts">
<INPUT TYPE="HIDDEN" NAME="apasswd" VALUE="$COOKIEAD{'apasswd'}">
<INPUT TYPE="HIDDEN" NAME="email" VALUE="$COOKIE{'email'}">
<INPUT TYPE="HIDDEN" NAME="name" VALUE="$COOKIE{'name'}">
<INPUT TYPE="HIDDEN" NAME="middle_html_disp" VALUE="$COOKIE{'middle_html_disp'}">
<INPUT TYPE="HIDDEN" NAME="blood" VALUE="$FORM{'blood'}">
<INPUT TYPE="HIDDEN" NAME="parent" VALUE="$FORM{'parent'}">
<INPUT TYPE="HIDDEN" NAME="prebbsaction" VALUE="$FORM{'bbsaction'}">
<INPUT TYPE="HIDDEN" NAME="target" VALUE="$FORM{'target'}">
<INPUT TYPE="HIDDEN" NAME="target_no" VALUE="$FORM{'target_no'}">
$POSTADDP{'ICONUPLOADFORM'}<!-- 将来拡張用 -->
<UL>
<TABLE BORDER="$table_border" CELLSPACING="$table_cellspacing" CELLPADDING="$table_cellpadding" bgcolor="$table_bgcolor" background="$table_background_image">

<TR $ie_bg >
 <TD ALIGN=RIGHT><font $font_option>分類： </font></TD>
 <TD colspan=2>
 <SELECT name=subject>
 <OPTION value="icon_norm01" $SEL{'icon_norm01'}> icon_norm01 (一般ユーザ用アイコンとして使う)
 <OPTION value="icon_admin" $SEL{'icon_admin'}>icon_admin (管理者専用アイコンとして使う)
 <OPTION value="other" $SEL{'other'}>other (ただの画像置き場として使う)
 </SELECT>
</TD>
</TR>

<TR $ie_bg >
 <TD ALIGN=RIGHT><font $font_option>メモ：</font></TD>
 <TD colspan=2>
<TEXTAREA NAME="body" COLS=60 ROWS=1 WRAP=SOFT>$COOKIE{'body'}</TEXTAREA>$DISP_OMIT{'body'}</TD>
</TR>
$cm_out_img_h
<TR bgcolor="#FDFDFD">
 <TD ALIGN=RIGHT><font $font_option2 >画像選択 </font></TD>
 <TD colspan=2><INPUT TYPE="FILE" NAME="img" VALUE="" SIZE=30> $DISP_OMIT{'img'}</TD>
</TR>
$cm_out_img_f
HTML_END

if(($FORM{'amode'} eq "icon_edit")&&($COOKIE{'subject'}=~ /icon/i)){
print<<HTML_END;
<TR  bgcolor="#FDFDFD">
 <TD ALIGN=RIGHT NOWRAP><font $font_option2 > &nbsp&nbsp画像のタイトル </font></TD>
 <TD colspan=2><INPUT TYPE="TEXT" NAME="imgtitle" SIZE=30 MAXLENGTH=60 VALUE="$ie_tmp_img_title"><font $f_param>＊必要（アイコン時）<BR>（記事投稿フォームでアイコンを選択するときの呼出し名に対応します）</font>
</TD>
</TR>
HTML_END
}

print<<HTML_END;
<TR >
 <TD>
 </TD>
 <TD><INPUT TYPE="SUBMIT" $output_button_px VALUE=" 登録する "><INPUT TYPE="RESET" $output_button_px VALUE="中止">
 </TD>
 </FORM>
 <TD align=center></TD>
</TR>
</TABLE>
</UL>
HTML_END
}
#
#   
#======================================================================#
#     <ＨＴＭＬ--2.レイアウトパターン4/ アイコン確認用レイアウト>      #
#======================================================================#
#
sub kiji_base_icon_html{
local($ie_bg01)="bgcolor=#A0A0A0";
local($wp_tmp_subject)="$tmp_subject";


 if($tmp_subject eq "icon_admin"){
  $tmp_subject=" 管理者アイコン ";
 }elsif($tmp_subject eq "icon_norm01"){
  $tmp_subject=" 一般ユーザ用アイコン ";
 }elsif($tmp_subject eq "sozai_background"){
  $tmp_subject=" 背景画像用素材 ";
 }elsif($tmp_subject eq "other"){
  $tmp_subject=" その他 ";
 }


if(($wp_tmp_subject=~ /icon/i)&&($old_tmp_unq_id ne "")){
print<<HTML_END;
<P><a name=$tmp_unq_id></a>
[<a href="$cgi_name?page=$disp_page&amode=icon_sort_up&target=$tmp_unq_id&insuid=$old_tmp_unq_id&bbsaction=icon_up&p=$FORM{'p1'}&p2=$FORM{'p2'}">↑このアイコンの表\示\順をひとつ上へ変更する</a>]<BR><BR>
HTML_END
}

print<<HTML_END;
<table border=0 bgcolor="#909090" width="80%">
<TR>
<TD rowspan=7>
<IMG SRC="$tmp_img_location" BORDER="0" $size_sitei ALIGN="LEFT" HSPACE="12" style="margin: 12px;float: left">
</TD>
<TD bgcolor="#CDCDEF" colspan=2>Webパーツ $disp_seq_no のプロパティ
[<a href="$cgi_name?bbsaction=edit_form&target=$tmp_unq_id&target_no=$tmp_seq_no&p1=$FORM{'p1'}&p2=$FORM{'p2'}&page=$FORM{'page'}&amode=icon_edit">\修\正\</a>]
</TD>
</TR>
<TR>
<TD bgcolor="#CDCDEF">[分類]</TD>
<TD bgcolor="#CDCDEF"> $tmp_subject </TD>
</TR>

<TR>
<TD bgcolor="#CDCDEF">画像のタイトル：</TD>
<TD bgcolor="#CDCDEF">$tmp_imgtitle
</TD>
</TR>

<TR>
<TD $ie_bg01>[ファイルタイプ/サイズ]</TD>
<TD $ie_bg01> $IMG_PARAMETERS{'type'}-$img_dsize</TD>
</TR>
<TR>
<TD $ie_bg01>[縦横ドット数]</TD>
<TD $ie_bg01> $w_set x $h_set</TD>
</TR>
<TR>
<TD $ie_bg01>[管理者のメモ]</TD>
<TD $ie_bg01> $tmp_body </TD>
</TR>
HTML_END

if($wp_tmp_subject=~ /other/i){
print<<HTML_END;
<TR>
<TD $ie_bg01>このファイルを呼出す時のURL</TD>
<TD $ie_bg01><A HREF="$tmp_img_location" TARGET="top">
クリック</A>してブラウザのURL欄を見るとわかるよ！</TD>
</TR>
HTML_END
}
print<<HTML_END;
<TR>
<TD $ie_bg01>[その他]</TD>
<TD $ie_bg01 colspan=2> 投稿者：$tmp_name $auto_user_IP  $disp_re</TD>
</TR>                              
</TABLE>
HTML_END


 # 一つ前のアイコンのunq_idを記憶する
 if($wp_tmp_subject=~ /icon/i){
  $old_tmp_unq_id="$tmp_unq_id";
 }

}
#
#===============================================#
#     <ＨＴＭＬ--携帯対応メニュー>              #
#===============================================#
#
#  携帯対応メニュー用のＨＴＭＬです．
#
sub output_keitai_menu_HTML{

	local($tmp_imode_flag)=0;

   	local($mail_link_pc)="";
   	local($tmp_script_path)="$ENV{'SCRIPT_NAME'}";
  	local($tmp_imode_cgi_name)="$imode_cgi_name";

	$tmp_script_path	=~ s/$cgi_name//i;
	$tmp_imode_cgi_name	=~ s/.*\///i;

	 if($PM{'im_cgi_url'}=~ /www\.aaa\.bbb\.com/i){
	   # デフォルトのままなら、自動作成して補完する
	   if($ENV{'SERVER_SOFTWARE'} =~ /Apache/i){
	     $PM{'im_cgi_url'}="http://$ENV{'SERVER_NAME'}"."$tmp_script_path"."$tmp_imode_cgi_name";
	   }else{
	   # そのまま表示して未設定を気付かせる
	   }
	 }

	if($ENV{'HTTP_X_JPHONE_MSNAME'} ne ""){
		$mail_link_pc="このURLを<a href=\"mailto:-\@-\" mailbody=\"$PM{'im_cgi_url'}\">メールで友達へ教える</A><BR><BR>";
	# PC
	}else{
		$mail_link_pc="このURLを<A HREF=\"mailto:-\@-?subject=新しい携帯掲示板のｱﾄﾞﾚｽ!&body=$PM{'im_cgi_url'}\">メールで友達へ教える</A><BR><BR>";
	}

	# 判定
	if(-e "$imode_cgi_name"){
		$tmp_imode_flag=1;
print<<HTML_END;
<HTML>
<HEAD>
<TITLE>imgboard ガラパゴス系携帯ユーザ向け案内ページ</TITLE>
<meta name="viewport" content="width=480">
</HEAD>
<BODY>
<a href=\"$imode_cgi_name\"> ガラパゴス系携帯ユーザ用アクセスページ</a>をどうぞご利用ください<BR>
<BR>
<BR>
$mail_link_pc
</BODY>
</HTML>
HTML_END
		return;
	}

$output_admin_block01_HTML=qq|<HTML><HEAD><TITLE>imgboard 携帯ユーザ向け案内ページ</TITLE>
<meta name="viewport" content="width=480">
</HEAD>
<BODY>
<B>(imgboard製作元からのお知らせ)</B>「ガラパゴス携帯\からも、掲示板の記事をチェックしたい」という皆様のご要望に応え、ガラパゴス系携帯\からのアクセスを可\能\にする機\能\追加モジュールを用意しています。現在、特報CGIにてβ版を無償配布していますので、良かったらご利用ください。<BR>
<PRE>----携帯アクセス仕様(ガラパゴス系)-------

1.<B>(だれでもアクセス)</B>以下のガラパゴス系携帯機種から、投稿、返信、閲覧、削除等ができます。
   ドコモ (iモード\,FOMA)
   SoftBank
   au by KDDI
2.<B>(ガラパゴス系携帯からの写真UP対応)</B> 以下の機\種\からは、ファイルアップロードも\可\能\です。
  動画・画像2MBアップロード対応の906i/706i以降シリーズ
* SoftBankのカメラ付携帯\ (3G,Vシリーズ以降）
* auのカメラ付携帯\ 
  注：その他のガラパゴス系携帯(旧ishot機/旧au機)対応は<a href="http://www.big.or.jp/~talk/t-club/soft/mini_2013/" target=_blank>次のimgboard 2015</a>以降で対応しています。このR6シリーズでは対応できません。
3.<B>(簡単アクセス)</B>携帯専用のURLを周知し忘れても、imgboard用のURLに携帯でアクセスすると
  自動的に携帯用ページにナビゲートする機\能\があります。
4.<B>(簡単アクセス2)</B> 携帯の種類や機種を自動判別し、それに適したページを出すようになっています。
5.<B>(組み込み簡単)</B> 基本的にはim.cgiモジュールをimgboard.cgi本体と同一ディレクトリに入れるだけです。
6.以下は動作デモのサンプル掲示板です。
<FORM> <INPUT TYPE="button" VALUE="サンプル" onclick="imode_window=window.open('http://www.big.or.jp/~talk/t-club/soft/mini_r6/im.cgi','imode_window','directories=no,location=no,toolbar=no,status=no,menubar=no,scrollbars=yes,resizable=yes,close=yes,width=220,height=530');"> <NOSCRIPT><A HREF="http://www.big.or.jp/~talk/t-club/soft/mini_r6/im.cgi"><B>サンプル</B></a></NOSCRIPT></FORM></BODY></HTML>|;

&output_admin_base_HTML(" エラー。この掲示板にはまだ携帯対応用追加モジュール、「携帯アクセス」が組み込まれていません "," ","  ","1"," 携帯対応 ");
}
#
#============================================#
#     <ＨＴＭＬ--アイコン一覧 >              #
#============================================#
#
#  アイコン一覧ウィンド用のＨＴＭＬです．
#
sub output_icon_list_HTML{
	&error(" 設定エラー。アイコン付き掲示板化するには、外部設定ファイルset_iconXXX.cgiが必要です。特報CGIにて入手してください ");
}
#
#===============================#
# 修正ウィンドのＨＴＭＬトップ
#===============================#
#
sub edit_top_html{
#
print<<HTML_END;
<HTML lang="ja">
<HEAD><TITLE>$title</TITLE>
<meta name="viewport" content="width=480">
</HEAD>
<BODY BGCOLOR="$PM{'body_bgcolor'}" BACKGROUND="$PM{'body_background'}" TEXT="$PM{'body_text'}" LINK="$PM{'body_link'}" VLINK="$PM{'body_vlink'}">
<FORM>
<INPUT TYPE="button" VALUE="修正せずに前のページへ戻る" $output_button_px onClick="history.back()">
</FORM>
<HR>
<UL>
 <H3>記事$FORM{'target_no'}を修正します </H3>
 <LI>記事を修正して投稿ボタンを押してください
 <LI>会員パスには管理者パスか、投稿時に設定した削除ＩＤを入れてください
</UL>
HTML_END
}
#
#========================#
# CGI名をとりだす
#========================#
#
sub get_script_name {

	local($file_name) = $0;
	local($path_name);
	local($script_name);

	# パスがある場合は削る
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
	$script_path_name="$path_name";
	return("$script_name");
}
#
#
#===================================#
# プロバイダのOSを判定する
#===================================#
# 引数なし、返値はＯＳの種類(win,mac)
# Perl for Winは新しいOS(NT SP4,Windows2000等)を検出
# できないバグがある そのため、いろんなヒントから、
# Windowsであることを検出するものとする。なお、強制
# 的に設定することもできるようにする。これらのフラグ
# はbinmode切替えやメール処理で用いる。
sub check_www_server_os{

	local($tmp_www_server_os)="";

	# 事前準備（エラーチェック）
	$tmp_www_server_os= $^O;

	# Win98 & NT4(SP4)対策
	$tmp_www_server_os= $ENV{'OS'} if($tmp_www_server_os eq "");

	# AnHTTPd /OmniHTTPd/IIS対策
	$tmp_www_server_os= 'win' if($ENV{'SERVER_SOFTWARE'} =~ /AnWeb|Omni|IIS\//i);

	# Win Apache 対策
	$tmp_www_server_os= 'win' if($ENV{'WINDIR'} ne "");

	# Perlが新OSを検知できない場合,強制的に指定する
	if($force_www_server_os_to =~ /win/i){
		$tmp_www_server_os = 'win';
	}elsif($force_www_server_os_to =~ /mac/i){
		$tmp_www_server_os = 'mac';
	}
	return($tmp_www_server_os);
}
#
#===================================#
# 記事登録時に管理者にメール
#===================================#

sub send_mail{

	local($tmp_mail_prog)="";		# sendmail以外のプログラム名
	local($tmp_mail_data)= "./$$\.dat";	# 一時ファイル名

	if ($use_email==1){

		# OSの種別を判別
		$www_server_os =&check_www_server_os;

		# メールプログラムの種別を判別
		if($mail_prog =~ /blat/i){
			$tmp_mail_prog="blatj";
		}elsif($mail_prog =~ /sendmane/i){# 2004.08
			$tmp_mail_prog="sendmane";
		}

		# OSをチェック、Windows,Macの初心者ユーザには警告を出す
		# ただし、BlackJumboDog等の利用者には警告を出さない。
		if(($www_server_os=~ /win/i)&&($tmp_mail_prog eq "")){
			&error("管理者設定にエラーがあります<BR>メール通知\機\能\はWindowsサーバでは「blatj」か「sendまねーる」しか使用できません。これらのソフトがない場合はメール通知をオフにしてください。");
			return;
		}elsif($www_server_os=~ /mac/i){
			&error("管理者設定にエラーがあります<BR>メール通知\機\能\はMacサーバでは使用できません。オフにしてください。");
			return;
		}

		# パラメータチェック（セキュリティチェック）
		if($email=~ /.*\@.*\..*/){
			$eemail_address=$email;
		}else{
			$eemail_address="dummy\@dummy.co.jp";
		}

		$eemail_name="$name";
		$eemail_subject	="$subject";
		$eemail_imgtitle="$imgtitle";

		# 本文が長すぎる場合はカットする。メール爆弾系のイタズラ対策。
		$eemail_body=$body;
		$eemail_body=~ s/\<BR\>/\n/gi;
		$eemail_body=~ s/<!-- user：\s([^>]*)(\s*)-->//ig;
		$eemail_body="$eemail_body"."\n"."$REMOTE_HOST";

		if($PM{'mail_body_limit'}){
			$tmp_mail_body_limit="$PM{'mail_body_limit'}";
		}else{
			$tmp_mail_body_limit='360';
		}

		# 初期設定で設定した制限より長い場合 
		if(length($body) >$tmp_mail_body_limit){
 			# 先頭から指定バイトまでのみ残す
			$eemail_body =substr("$body",0,"$tmp_mail_body_limit");
			$eemail_body .=" \/\/長過ぎますので、以後はカットしました.<!-- user： $REMOTE_HOST --> - $HTTP_REFERER ";
		}

  		# URLが指定されている場合はフルURL表記にする。
		$eemail_img_location="$img_location";
		if($img_dir_url!~ /http:\/\/yourprovider\/yourname\/imgboard\/img-box\//){
			$eemail_img_location="$img_dir_url"."$new_fname";
		}

		# セキュリティ対策のため、問題のある文字をフィルタ
		$eemail_address		=~ s/\,|\;|\://g;
		$eemail_name		=~ s/\,|\;|\://g;
		$eemail_subject		=~ s/\,|\;|\://g;
		$eemail_imgtitle	=~ s/\,|\;|\://g;

		# メール文面ここから
$mail_hmes .= "MIME-Version: 1.0\n";
$mail_hmes  = "Reply-to: $eemail_address\n";
$mail_hmes .= "From: $eemail_address\n";
$mail_hmes .= "Subject: \[imgboard\]New article is added \n";
$mail_hmes .= "Content-Type: text/plain; charset=iso-2022-jp\n";
$mail_hmes .= "Content-Transfer-Encoding: 7bit\n\n";

$mail_mes .= "imgboardに新しい記事が投稿されました。\n\n";
$mail_mes .= "[ Date ] $date_data\n";
$mail_mes .= "[ 名前 ] $eemail_name\n" 		if($eemail_name ne "");
$mail_mes .= "[e-mail] $eemail_address\n"	if($eemail_address ne "");
$mail_mes .= "---------------------------------------\n";
$mail_mes .= "[タイトル] $eemail_subject\n" 		if($eemail_subject ne "");
$mail_mes .= "[  本文  ] \n $eemail_body\n"		if($eemail_body ne "");
$mail_mes .= "[Image Title]  $eemail_imgtitle\n" 	if($eemail_imgtitle ne "");
$mail_mes .= "[Image URL  ]  $img_data_size\n" 		if($img_location ne "");
$mail_mes .= "        $eemail_img_location \n"		if($img_location ne "");
$mail_mes .= "[使用プラウザ] $HTTP_USER_AGENT\n"		if($HTTP_USER_AGENT);
$mail_mes .= "[連続] $now_up_counter 回 [リミッタの現在設定] $upload_limit_times / $upload_limit_type \n"	if($limit_upload_times_flag==1);
$mail_mes .= " 以上 \n";

	# メール文面ここまで

	# 送出開始

	# blatjの時
	 if($tmp_mail_prog eq "blatj"){

	  # 一時ファイルに書き出す
	   open  (OUT,">$tmp_mail_data") || &error("Write Error : $tmp_mail_data");
	   print  OUT $mail_mes;
	   close (OUT);


	  # メールを送出
	  open  (MAIL,"| $mail_prog $tmp_mail_data -t $recipient $attach_option_mes -q -s imgboard_New_article") || &error(" 管理者設定にエラーがあります<BR>メールプログラム$mail_progが見つかりません。メールプログラムのパスを再確認してください。<BR>またWebサーバとメールサーバが別のサーバの場合使用できません。\n");
   	  close (MAIL);

	  # 一時ファイル削除
	  unlink($tmp_mail_data);

	# 普通のsendmailの時
	 }else{

	  # メールヘッダと本文を結合する
	  $mail_mes="$mail_hmes"."$mail_mes";

	  # メールで標準の形態、漢字コードJIS、改行コードLFに変換する。
	  $mail_mes=~ s/\r\n/\n/g;		# 改行コードを変換
	  $mail_mes=~ s/\r/\n/g;			# 改行コードを変換
	  &jcode'convert(*mail_mes, 'jis');	# 漢字コードをJISに(修正99.11)

	  # メールを送出
	  open (MAIL, "|$mail_prog $recipient") || &error(" 管理者設定にエラーがあります<BR>メールプログラム$mail_progが見つかりません。メールプログラムのパスを再確認してください。<BR>またWebサーバとメールサーバが別のサーバの場合使用できません。\n");
		print MAIL "$mail_mes";	
   	  close (MAIL);

	 }

	}
}
#
#========================#
# perl -wc 警告対策 
#========================#
#
sub disp_unused_parameters{
  print "Content-type: text/html"."$Netscape4x_ch_set"."\n\n";
print<<HTML_END;
<PRE>
body_text_max_cols $body_text_max_cols
dummy $dummy
attach_option_mes $attach_option_mes
existing_snl_type_list $existing_snl_type_list
SNL_MADE_DATA @SNL_MADE_DATA
script_path_name $script_path_name
WP_MESSAGE $WP_MESSAGE
WP_HEAD_MESSAGE $WP_HEAD_MESSAGE
GETURLADDP $GETURLADDP
body_tag_f $body_tag_f
$tttmp_salt
$ttmp_uniq_char
$tmp_token_time
$oya_kiji_img_height
</PRE>
HTML_END

}
#
#==================================#
# youTubeタグの判定(旧objectタグ系) 
#==================================#
# 2014.02 youtube,dailymotion,ustreamは古いobjectタグを使わないように誘導するようにした
# 2010.05 ustream対応で修正
# 2009.06 dailymotion等の他動画共有サイトに対応できるように
# ロジックを変更した
#
sub check_youTube_tag{

	local($TCY_form)	= $_[0];# 引数 FORMの内容
	local($tmp_yt_check_level)	= $_[1];# 引数 2 チェックレベル

	undef @TMP_DOUGA_KU_DOMAIN;
	@TMP_DOUGA_KU_DOMAIN=@DOUGA_KU_DOMAIN; # 動画共有ドメイン

	if($use_youtube_tag_in_comment != 1){
		# 無駄な処理をしないようにする
		return(0);
	}

	# 本文以外は埋め込み禁止
	if($form!~ /body/i){
		return(0);
	}

	# objectタグ二つならアボート
	if($TCY_form=~ /<object(.|\n)*<object/i){
		&error(" エラー。OBJECTタグは複数埋め込みできません。ひとつにしてください。 ");
		return(0);
	}

	# EMBEDタグ二つならアボート
	if($TCY_form=~ /<embed(.|\n)*<embed/i){
		&error(" エラー。EMBEDタグは複数埋め込みできません。ひとつにしてください。 ");
		return(0);
	}

	# objectタグにクラスID特定があるなら危険なのでアボート
	# ustream対応で修正 (2010.05.27)
	if($TCY_form=~ /<object(.|\n)*classid/i){

	 # FlashPlayerのクラスIDは許す。それ以外は危険なのでダメ
	 if($TCY_form=~ /clsid:([a-zA-Z0-9\-]+)\"/i){
	  # FlashPlayerの場合は許可する
	  if($1 =~ /^d27cdb6e\-ae6d\-11cf\-96b8\-444553540000$/i){
	    # 許可する
	  }else{
		&error(" セキュリティエラー。OBJECTタグに、このクラスIDを指定できません。埋め込みタグ内でFlashPlayer以外のクラスは指定しないでください。 ");
		return(0);
	  }
	 }else{
		&error(" セキュリティエラー。OBJECTタグのクラスID指定が不正です。HTMLタグの記述を見直してください。 ");
		return(0);
	 }
	}

	# objectタグにcodebase特定があるなら危険なのでアボート
	if($TCY_form=~ /<object(.|\n)*codebase/i){
		&error(" セキュリティエラー。OBJECTタグにcodebaseを指定できません。埋め込みタグ内でcodebaseは指定しないでください。 ");
		return(0);
	}

	if($new_fname ne ''){
		&error(" ユーザー操作エラー。画像をアップした記事には、動画埋め込みはできません。どちらかひとつにしてください。 ");
		return(0);
	}

	if(($allow_youtube_tag_in_res == 0)&&($FORM{'prebbsaction'} eq "disp_rep_form")){
		&error(" ユーザー操作エラー。現在、返信記事には動画埋め込みはできない設定になっています。動画埋め込みは、親記事でおこなってください。 ");
		return(0);
	}

	# 古いobjectタグを使えるけど、やめた方がいい場合は、新しいものへ誘導
	if($TCY_form=~ /<object(.|\n)*<embed/i){
	  if($TCY_form=~ /http\:\/\/www\.dailymotion\.com\//ig){
		&error(" dailymotionは、新しいiframeタグの埋め込みコードを使ってください。objectタグは古いので利用できません。 ");
	  }
	  if($TCY_form=~ /http\:\/\/www\.ustream\./ig){
		&error(" ustreamは、新しいiframeタグの埋め込みコードを使ってください。objectタグは古いので利用できません。 ");		  
	  }
	  if($TCY_form=~ /\/\/www\.youtube\.com\//ig){
			&error(" YouTubeは、youtu . be の短縮URLか、iframeタグの埋め込みコードを使ってください。objectタグは古いので利用できません。 ");	
	  }
		return(0);
	}

	# 埋め込みサイズのチェック(巨大サイズ埋め込みイタズラ防止)
	# 2008.08子記事の場合を考慮しサイズ縮小
	if($FORM{'prebbsaction'} ne "disp_rep_form"){
		$FORM{body}=~ s/(\s)width(\s*)=(\s*)(\"?)(\d+)(\%?)(\"?)/ width=\"640\"/ig;
		$FORM{body}=~ s/(\s)height(\s*)=(\s*)(\"?)(\d+)(\%?)(\"?)/ height=\"385\" align=\"left\" style=\"margin: 12px;float: left\"/ig;
	}else{
		# 2008.08子記事の場合を考慮しサイズ縮小
		$FORM{body}=~ s/(\s)width(\s*)=(\s*)(\"?)(\d+)(\%?)(\"?)/ width=\"425\"/ig;
		$FORM{body}=~ s/(\s)height(\s*)=(\s*)(\"?)(\d+)(\%?)(\"?)/ height=\"344\" align=\"left\" style=\"margin: 12px;float: left\"/ig;
	}

#@DOUGA_KU_DOMAIN=('www.youtube.com','www.dailymotion.com','www.ustream.tv','');

	# youtubeだけ許可したい人は4を指定する
	if($tmp_yt_check_level >= 4){
	 if($TCY_form!~ /<object(.|\n)*<embed(.|\n)*src=(\")?http\:\/\/www\.youtube\.com\/(.|\n)*application\/x-shockwave-flash/i){
		return(0);
	}

	# @DOUGA_KU_DOMAINで指定済みのFQDNドメインだけ許可する場合（推奨）
	}elsif($tmp_yt_check_level >= 2){

		# @DOUGA_KU_DOMAIN名と一致したらOK
		local($ttmp_dmatch)=0; # matchフラグ
		foreach (@TMP_DOUGA_KU_DOMAIN){
			next if($_ eq "");
	    	# 正規表現をPerlパターンマッチへ変換
	    	$w_pattern=&change_pattern_match($_);
	    	# 2011.09.24 Ustreamのclassid記述に対応(classid自体はチェック済み)
	    	# 2010.11.29 embedタグ内の記述順に影響を受けないよう修正(DailyMoiton対策)
			if(($TCY_form=~ /<object(.|\n)*<embed(.|\n)*(\s)type=(\")?application\/x-shockwave-flash(\")(\s)/i)||($TCY_form=~ /<object(.|\n)*classid/i)){
			 if($TCY_form=~ /<object(.|\n)*<embed(.|\n)*src=(\")?http\:\/\/$w_pattern(.|\n)*/i){
				$ttmp_dmatch++;
	 		 }
	 		}
		}
		# １件もマッチしなければアウト
		if($ttmp_dmatch == 0){
			&error(" ユーザ操作エラー。あなたの指定した「動画サイト」の、タグ埋め込みは許可されていません。現在の掲示板設定(埋込みタグチェックレベル $tmp_yt_check_level)では、管理者が事前に許可した@TMP_DOUGA_KU_DOMAINのFlashビデオタグ埋込みのみ、可\能\です。 ");
			return(0); 
		}
	
	# ゆるいチェック(他の投稿サイトも許す)
	}elsif($tmp_yt_check_level >= 1){
	 if($TCY_form!~ /<object(.|\n)*<embed(.|\n)*src=(\")?http\:\/\/(.|\n)*(\s)type=(\")?application\/x-shockwave-flash(\")(\s)/i){
	return(0);
}
	}

	# 全チェック通過ならOK
	return(1);
}
#
#==================================#
# iframeタグの判定 
#==================================#
# 2011.06
# YouTube,DailyMotion,Ustream,Nicovideoがiframeに移行したので独立させた
sub check_iframe_tag{

	local($TCY_form)	= $_[0];# 引数 FORMの内容
	local($tmp_check_level)	= $_[1];# 引数 2 チェックレベル

	undef @TMP_DOUGA_KU_DOMAIN;
	@TMP_DOUGA_KU_DOMAIN=@DOUGA_KU_DOMAIN; # 動画共有ドメイン

	if($use_youtube_tag_in_comment != 1){
		# 無駄な処理をしないようにする
		return(0);
	}

	# 本文以外は埋め込み禁止
	if($form!~ /body/i){
		return(0);
	}

	# iframeタグ二つならアボート
	if($TCY_form=~ /<iframe(.|\n)*<iframe/i){
		&error(" エラー。iframeタグは複数埋め込みできません。ひとつにしてください。 ");
		return(0);
	}


	if($new_fname ne ''){
		&error(" ユーザー操作エラー。画像をアップした記事には、iframeタグによる画像や動画の追加埋め込みはできません。どちらかひとつにしてください。 ");
		return(0);
	}

	if(($allow_youtube_tag_in_res == 0)&&($FORM{'prebbsaction'} eq "disp_rep_form")){
		&error(" ユーザー操作エラー。現在、返信記事にはiframeタグによる画像や動画の埋め込みはできない設定になっています。動画埋め込みは、親記事でおこなってください。 ");
		return(0);
	}

	# Google MAPのStreetview埋め込みで対応
	if(($use_stview_tag_in_comment == 1)&&(($FORM{$form}=~ /src\=\"http\:\/\/maps\.google\./i)||($FORM{$form}=~ /src\=\"http\:\/\/www\.google\.co\.jp\/maps/i))){
		# 許可する
		return(1);
	}

	# 埋め込みサイズのチェック(イタズラ防止)
	# 2008.08子記事の場合を考慮しサイズ縮小
	if($FORM{'prebbsaction'} ne "disp_rep_form"){
		$FORM{body}=~ s/(\s)width(\s*)=(\s*)(\"?)(\d+)(\%?)(\"?)/ width=\"450\"/ig;
		$FORM{body}=~ s/(\s)height(\s*)=(\s*)(\"?)(\d+)(\%?)(\"?)/ height=\"340\" align=\"left\" style=\"margin: 12px;float: left\"/ig;
	}else{
		$FORM{body}=~ s/(\s)width(\s*)=(\s*)(\"?)(\d+)(\%?)(\"?)/ width=\"360\"/ig;
		$FORM{body}=~ s/(\s)height(\s*)=(\s*)(\"?)(\d+)(\%?)(\"?)/ height=\"300\" align=\"left\" style=\"margin: 12px;float: left\"/ig;
	}


#@DOUGA_KU_DOMAIN=('www.youtube.com','www.dailymotion.com','www.ustream.tv','');

	# youtubeだけ許可したい人は4を指定する
	if($tmp_check_level >= 4){
	# 2014.02.11 update 
	 if($TCY_form!~ /<iframe(.|\n)*src=(\")?(https?\:\/\/|\/\/)www\.(youtube|youtube\-nocookie)\.com\/embed\//i){
		return(0);
	 }

	# @DOUGA_KU_DOMAINで指定済みのFQDNドメインだけ許可する場合（推奨）
	}elsif($tmp_check_level >= 2){

		# @DOUGA_KU_DOMAIN名と一致したらOK
		local($ttmp_dmatch)=0; # matchフラグ
		foreach (@TMP_DOUGA_KU_DOMAIN){
		next if($_ eq "");
    	# 正規表現をPerlパターンマッチへ変換
    	$w_pattern=&change_pattern_match($_);
  		 if($TCY_form=~ /<iframe(.|\n)*src=(\")?(https?\:\/\/|\/\/)$w_pattern(.|\n)*/i){
			$ttmp_dmatch++;
 		 }
		}
		# １件もマッチしなければアウト
		if($ttmp_dmatch == 0){
			&error(" ユーザ操作エラー。あなたの指定した「動画サイト」の、タグ埋め込みは許可されていません。現在の掲示板設定(埋込みタグチェックレベル $tmp_check_level)では、管理者が事前に許可した@TMP_DOUGA_KU_DOMAINのFlashビデオタグ埋込みのみ、可\能\です。 ");
			return(0); 
		}
		
	# ゆるいチェック(他の投稿サイトも許す)
	}elsif($tmp_check_level >= 1){
#	 if($TCY_form!~ /<iframe(.|\n)*src=(\")?(https?\:\/\/|\/\/)/i){
	# 2014.02.21 セキュリティ対策である程度の型に入っているものに限定する
	 if($TCY_form!~ /<iframe(.|\n)*src\=(\")?(https?\:\/\/|\/\/)(.*)(\.com|\.net|\.org|\.tv|\.me|\.jp)\/([\/\?\&\=\-_\.a-zA-Z0-9]{5,40})\"(.|\n)*<\/iframe>/i){
			$tmp_data =~ s//(未知のURLです。クリック注意)$2$3$4\/$5/ig;

		return(0);
	 }
	}

	# 全チェック通過ならOK
	return(1);
}
#
#==================================#
# scriptタグの判定 
#==================================#
# 2014.02 Theta360対応
# 2011.06
# 独立させた
sub check_script_tag{

	local($TCY_form)	= $_[0];# 引数 FORMの内容
	local($tmp_check_level)	= $_[1];# 引数 2 チェックレベル

	if(($PM{'auto_nicovideo_find'} == 1)&&($FORM{$form}=~ /<(\/?)script(.|\n|\s)*src\=\"http\:\/\/ext\.nicovideo\.jp\/thumb_watch\/([\-a-z0-9_]+)/i)){
		&error(" 操作エラー。SCRIPTタグはセキュリティ上問題あるため、本文中に使えません。<BR>なお、
		このニコニコ動画のリンクは http://www.nicovideo.jp/watch/$3 だけを本文中に記載すると、自動的にきちんと埋め込み表\示\されますので、その記載法で埋め込んでください ","","1");
	}

	if(($PM{'auto_theta360_find'} == 1)&&($FORM{$form}=~ /<(\/?)script(.|\n|\s)*src\=\"https?\:\/\/theta360\.com\/(.|\n|\s){26,40}<\/script>/i)){

		# scriptタグは危険だからエスケープする
		$FORM{$form}=~ s/<(\/?)script(.|\n|\s)*src\=\"https?\:\/\/theta360\.com\/(.|\n|\s){26,40}<\/script>/\-scrt_here_Theta360\-/g;


		# blockquoteの埋め込みサイズのチェック(イタズラ防止)
		# 2008.08子記事の場合を考慮しサイズ縮小
		if($FORM{'prebbsaction'} ne "disp_rep_form"){
			$FORM{$form}=~ s/(\s)data\-width(\s*)=(\s*)(\"?)(\d+)(\%?)(\"?)/ data\-width=\"450\"/ig;
			$FORM{$form}=~ s/(\s)data\-height(\s*)=(\s*)(\"?)(\d+)(\%?)(\"?)/ data\-height=\"340\"/ig;
		}else{
			$FORM{$form}=~ s/(\s)data\-width(\s*)=(\s*)(\"?)(\d+)(\%?)(\"?)/ data\-width=\"360\"/ig;
			$FORM{$form}=~ s/(\s)data\-height(\s*)=(\s*)(\"?)(\d+)(\%?)(\"?)/ data\-height=\"300\"/ig;
		}
		
		return(1);
	}
# TODO
$PM{'auto_fc2_find'} = 1;

	# FC2対策 scripitタグなので厳密にやる。TODO BlackWordのurl=の解除を忘れないこと
	if(($PM{'auto_fc2_find'} == 1)&&($FORM{$form}=~ /<(\/?)script src\=\"https?\:\/\/[\-_\.a-zA-Z0-9]{3,16}\.fc2\.com\/video\/js\/(.){3,20}\.js\"(.|\n|\s)*<\/script>/i)){


		# 埋め込みサイズのチェック(イタズラ防止)
		# 2008.08子記事の場合を考慮しサイズ縮小
		if($FORM{'prebbsaction'} ne "disp_rep_form"){
#			$FORM{$form}=~ s/(\s)w(\s*)=(\s*)(\"?)(\d+)(\%?)(\"?)/ w=\"450\"/ig;
#			$FORM{$form}=~ s/(\s)h(\s*)=(\s*)(\"?)(\d+)(\%?)(\"?)/ h=\"340\"/ig;
			$FORM{$form}=~ s/(\s)w(\s*)=(\s*)(\"?)(\d+)(\%?)(\"?)/ w=\"600\"/ig;
			$FORM{$form}=~ s/(\s)h(\s*)=(\s*)(\"?)(\d+)(\%?)(\"?)/ h=\"400\"/ig;
		}else{
			$FORM{$form}=~ s/(\s)w(\s*)=(\s*)(\"?)(\d+)(\%?)(\"?)/ w=\"360\"/ig;
			$FORM{$form}=~ s/(\s)h(\s*)=(\s*)(\"?)(\d+)(\%?)(\"?)/ h=\"300\"/ig;
		}
		
		return(1);
	}

	# 埋め込み禁止
		return(0);
}
#
# スクリプト終端です

