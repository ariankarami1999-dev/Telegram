<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/RVZYYWzaUqyi82X1EOAybPjls-dKsXvtMnCEMhggy13j9qS7bVEE8TvubgnSF_Y0eKlxGar7kOgXMHjOreL1uPRB8JdEjgu9DgGXLsw-MoPvTJiDdnPhL6MmRCsj8GxNKyVj6vYgXapDjumHZ-uMD3ZEaXNU5dNPXJ9SXF-VxsPLYWYxFO3CDubf79vtWaxxDuHDOrF_qxEqA9UYgPYcLuPertbA0Jc1fAKVRhOE6EEt2h1t_zqaVePMPIJrJOIMsI6vB0-JaEi2BmYvdzlHeO-xz8xko6SuSCo7pQsReNkte2KcSXANCsI_BgT2SulYw1ox2pPrVNY25_TU6aNsfA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 415K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 16:52:31</div>
<hr>

<div class="tg-post" id="msg-19042">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تحلیلگر نزدیک به سپاه:
پیشنهادات اخیر آمریکا شباهت زیادی با الگوی پیش از دو جنگ 12 روزه و 40 روزه دارد،
اعزام گسترده جنگنده های آمریکایی به خاورمیانه در روز های اخیر از قصد آمریکا برای جنگ جدید خبر می‌دهد
@WarRoom</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/withyashar/19042" target="_blank">📅 16:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19041">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chj2Q4hfxPcaTvyqUK4z_qWwftTy24-SwRbh6swvBVqqKbcOp4iAt3gCqbiF-TabCxXWXkqefXL5V6YxBd8fIrNM-Z338bZvF64ANXC4HRM4xjssuvDwLkOvtUue-pGUsTh0QziN2RawDiRrrjNSbh1d3UKeluAvaaCu3vYFND5mLzhcp6-0uI26GeFCw_PZgU0Gyh87-W3RYPa8nFUGp0c1BzdKRexPwTUxrw3zjNtac0h8esIP6T_8DU7cPfSqR5JOMOa_ajsVVTJU1CCkKOeh89AKLM2157KeT2WIxLmSd8pdWZn6NDXeiCPb26aYUXGcqiMt8atX3URTBxnEzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ توییت مسیح علینژاد درباره اعدام یک جوان ۱۹ ساله ایرانی در جریان اعتراضات دی ماه را بازنشر کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/withyashar/19041" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19040">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">درگیری‌های حوثی-عربستان سعودی:
حوثی‌ها اعلام کردند که محاصره دریایی عربستان سعودی را در تنگه باب‌المندب آغاز کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/withyashar/19040" target="_blank">📅 16:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19039">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نیویورک تایمز: تهران و واشنگتن در آستانه یک «لحظه سرنوشت‌ساز»  بر سر جنگ قرار گرفته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/withyashar/19039" target="_blank">📅 16:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19038">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بحرین : ایران ساعتی پیش به سامانه‌های ناوبری هوایی ما حمله کرد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/19038" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19037">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مقام آمریکایی به CBS:
تشدید تنش به زودی آغاز خواهد شد،
هواپیماهای ترابری و سوخت رسان آمریکایی به صورت پی در پی و بی سابقه در حال ورود به خاورمیانه می‌باشند
@WarRoom</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/19037" target="_blank">📅 14:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19036">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ممباقر بعد از چند ماه عضویت در اتاق جنگ با یاشار : آمریکایی‌ها مدام تجهیزات نظامی جدید به منطقه می‌آورند و می‌گویند دنبال توقف جنگند. روی هوش ما اندازهٔ آی کیوی مختصر خودشان حساب کرده‌اند.
ما در شناخت این آمریکایی‌بازی‌ها به مرحلهٔ استاد تمامی رسیده‌ایم و بر این اساس آماده شده‌ایم. اقدامات باید مؤید ادعاها باشد نه ناقض آن‌ها.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/19036" target="_blank">📅 14:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19035">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyGeEm95MMXQg8DEN5-yqAQUhAYeFAQiHAQn8zgQ12eakiY-SDjZ_H0Dpm0PUuyP1wWRUXn67_RHeXrsXoiEgg36K1jrJaIEwq1SR6B7-wXi-EefJLbAQwjQCk8zcqSwPgUPa1rLX8VkJNoq0A45xGj2tbkJFoaCHXFwpSn8LXjefPXy9jr7vgjJcGhAy2p6SL0htJUvhd2dz7Ce95fi5tE6LlCRXsiK_IZTRrNUC2PoBHZC7NxY6KHbfbmOo3Q4pPU1FObxQiali_JcMQr_H9j9YipjltVmV7tSNctdqFWrHqE4o4HBGYXxDw5x__xddzF8GXvMW-Kk3krVBOCDkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به دنیا آمدن پسر معاون خود جی دی ونس را تبریک گفت.
پسری به نام
Alec Neel Vance (الک نیل ونس)
. در بیانیه مشترکشان اعلام کردند که مادر و نوزاد هر دو در سلامت کامل هستند.
فرزندان جی‌دی و همسرش اوشا ونس(حقوقدان آمریکایی با ریشه هندی) (خانواده‌ای از مهاجران هندیِ تلوگو)
Ewan Vance (ایوان ونس)
– متولد
۲۰۱۷
(پسر)
Vivek Vance (ویوک ونس)
– متولد
۲۰۲۰
(پسر)
Mirabel Vance (میرابل ونس)
– متولد
۲۰۲۱
(دختر)
Alec Neel Vance (الک نیل ونس)
– متولد
۱۹ ژوئیه ۲۰۲۶
(پسر)
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/19035" target="_blank">📅 14:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19034">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STC0mrlK2P7gSfXL5aXKh_lyIJIbiJCcX7dzwi96Rqai8ZnDTquWDALiAHHImOnnhxOUEXKR678CRIGLaZCk0EXZqUZ41gpphAdi7XH-GVoYaRDh57aQBb6l8ZGrZURayMm6qKo_xxBrKkHn2HfpTQHyygOlZgpKIKQ4RTmyLPVy0KD66PjIpM_gdW1uhdG8lXaCo2LTMO2LKF4_vRNOuGgF_qMx6_6kK_40wuvaIlVYLh9ehK8Q2NeC81EQm5-s8KrmVEyaMZSZAp0ImTAJgCRmJJUUGTDvVjtCPfltpiBjnebueoweurHRLk-L-50nCTgEVODarPnP3eZT4bgh2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای نتانیاهو  به مقصد نا معلومی بلند شده سپس چند دور زد تا جهت مقصد گم شود و بعد فرستنده خود را خاموش کرد!
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/19034" target="_blank">📅 14:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19033">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کیر استارمر
امروز،
۲۰ ژوئیه ۲۰۲۶
، در دیدار خصوصی با پادشاه، استعفایش پذیرفته شد. چند دقیقه بعد، جایگزین او
اندی برنهام
، رهبر جدید حزب کارگر مأمور تشکیل دولت شد و قدرت رسماً منتقل شد. این انتقال معمولاً در فاصله حدود ساعت
۱۱:۴۵ تا ۱۲:۰۰ به وقت لندن
انجام می‌شود(حدود ۳۰ دقیقه دیگر بهصورت رسمی)
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/19033" target="_blank">📅 13:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19032">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f8bc26544.mp4?token=TP69k1zV3L9YbESg6fVWKlaOufZK3YXN2HYBL8J50ioGhrazjUJkG2CFS_HZXbe14tuRUPS_uYsHaowur4dtRu6XfYwMXT6pFMsXiqp_WfOQdU7ejNMOZxFA1UPX55oBJnfcH6LMMeRNCdoFOmGrCdR9k56cDf4OTMaddkkZxxJHRBKU-2IdWR0reOcWhmM-2vtnLO74i4Cihwar_Gq14I5OiqQ1jJm3S7MdYK0fjojclx6i1zt0SNjHboKF_hjCFOpHZ2EU9F_c4__HkByk_Sc-CsIeuFsETtCRPrIITpV4QmKBnOLk2y3qoJoCTxAjacBjnxtpsPDV0xl4OAswIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f8bc26544.mp4?token=TP69k1zV3L9YbESg6fVWKlaOufZK3YXN2HYBL8J50ioGhrazjUJkG2CFS_HZXbe14tuRUPS_uYsHaowur4dtRu6XfYwMXT6pFMsXiqp_WfOQdU7ejNMOZxFA1UPX55oBJnfcH6LMMeRNCdoFOmGrCdR9k56cDf4OTMaddkkZxxJHRBKU-2IdWR0reOcWhmM-2vtnLO74i4Cihwar_Gq14I5OiqQ1jJm3S7MdYK0fjojclx6i1zt0SNjHboKF_hjCFOpHZ2EU9F_c4__HkByk_Sc-CsIeuFsETtCRPrIITpV4QmKBnOLk2y3qoJoCTxAjacBjnxtpsPDV0xl4OAswIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روبیو به سی‌ان‌ان: از طریق کانال‌های متعدد، نشانه‌هایی مبنی بر تمایل ایران به مذاکره به دست ما رسیده است، اما شکاف فزاینده‌ای در درون نظام وجود دارد.  اگر ایرانیانِ خواهان مذاکره بر اوضاع مسلط شوند، این یک تحول مثبت خواهد بود، اما چنین چیزی رخ نداده است. @WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/19032" target="_blank">📅 13:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19031">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118dddcf1a.mp4?token=QyN45YNLOTmIqiF3NJsut5hxBMqlYqVRkd1Z1Qw4emlTL6wu-XELx-WdG-Y0FhoZ10slIsDnW-RZOCPpM35GrvrCIZhA8-0XzfOFRGHaj4Fkklu23WAg-ZmNuub_TMxpKbjzW4gGWR1GHnlQ4jcFN9n760UJ2gUhkX2Yk4Cmwpzbf9v1jNFlB9dmtrSZkNdgNrlYdPHrNZKgS3tUm7sBBfQeFZHHvUQvxUWmiIq-9CEtNEgHmKBPGV7QyUkGs-CJ6qntC2cOfV9L2rAwZhwPMLXcnVSU-7F5H0KNsz6ge8xojvBPXA8kBsi6hBzjeKtLDX5C52StNdiYYE0_G7WyC4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118dddcf1a.mp4?token=QyN45YNLOTmIqiF3NJsut5hxBMqlYqVRkd1Z1Qw4emlTL6wu-XELx-WdG-Y0FhoZ10slIsDnW-RZOCPpM35GrvrCIZhA8-0XzfOFRGHaj4Fkklu23WAg-ZmNuub_TMxpKbjzW4gGWR1GHnlQ4jcFN9n760UJ2gUhkX2Yk4Cmwpzbf9v1jNFlB9dmtrSZkNdgNrlYdPHrNZKgS3tUm7sBBfQeFZHHvUQvxUWmiIq-9CEtNEgHmKBPGV7QyUkGs-CJ6qntC2cOfV9L2rAwZhwPMLXcnVSU-7F5H0KNsz6ge8xojvBPXA8kBsi6hBzjeKtLDX5C52StNdiYYE0_G7WyC4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مستند ساز حکومتی در صحبت با عراقچی : ترامپ راست میگفت مشهد سقوط کرد بود !
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19031" target="_blank">📅 13:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19030">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjUrX36Ot1N7J0PPFCsJuOt4-tiD7WokDZkYz9OjFYVhI-En5jpPmHIegh8XPyXCxNfjhxJAXqYj5-rMTYPEyXfyVyZSZqP_xJaTOth_xlmXJ5VgKgzBtBy_ADpQdUQWe0oYYNLfpPYyAQKbNkbLZR0RgWHkZxz54A0TQfeAVQuMdyxuvrPHgzDgWEKtQ6dP4j20DXRLBSF5NqkU_RBrrAGMeDiJRQYGTWWeICK4I42iHLK1m_0Nsaoh45_JLMjfPi25jeipNmVTr9RZ-oQJ9LVgN_5_GTmWsHBRch3u_XEFTUe0LgEx-4HLDaXmrwqWmqNRvj9ZPcyiOUdU8k5SLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون عملیات سنگین اسرائیل در نبطیه، جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/19030" target="_blank">📅 13:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19029">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">روزنامه اسرائیل هیوم : نتانیاهو امشب جلسه‌ای امنیتی را به دلیل تشدید تنش‌ها با ايران برگزار خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/19029" target="_blank">📅 12:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19028">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سازمان دریانوردی بریتانیا: حمله موشکی ایران به یک نفتکش عربستان سعودی در تنگه هرمز ، الان
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19028" target="_blank">📅 12:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19027">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نیویورک تایمز: پنتاگون ده‌ها مجروح از نیروهای ارتش آمریکا در جنگ با ایران را پنهان کرده
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19027" target="_blank">📅 12:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19026">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">عراقچی مدعی شد دونالد ترامپ در روز چهارم جنگ با سران گروه‌های مسلح کُرد مخالف ایران در شمال عراق تماس گرفته و از ورود زمینی آنها به ایران حمایت کرده بود. او افزود پس از اطلاع از این موضوع، با مقام‌های اقلیم کردستان عراق، نخست‌وزیر عراق و هاکان فیدان، وزیر امور خارجه ترکیه، تماس گرفته و نگرانی‌های تهران را منتقل کرده است.
‏به گفته وزیر خارجه ایران، دولت ترکیه در جلوگیری از این اقدام نقش مؤثری ایفا کرد و علاوه بر رایزنی با آمریکا، مواضع محکمی در مخالفت با این طرح اتخاذ کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19026" target="_blank">📅 12:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19025">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">روبیو به سی‌ان‌ان: از طریق کانال‌های متعدد، نشانه‌هایی مبنی بر تمایل ایران به مذاکره به دست ما رسیده است، اما شکاف فزاینده‌ای در درون نظام وجود دارد.  اگر ایرانیانِ خواهان مذاکره بر اوضاع مسلط شوند، این یک تحول مثبت خواهد بود، اما چنین چیزی رخ نداده است.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19025" target="_blank">📅 11:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19024">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f146b0f2.mp4?token=pi5ycDDV4dmwGDLlJNWXwEXd7qI0esPIIMzwiLeNVkaW7FMqB9G928UTbSZLcEzRXjGLujur7fCLitx8AL-t6cgfQgq2RKlcOYHpSfBjkj7tGvu6o9_47bq8leVfcbf7AwNg-RMR7QSBbpdSUDCduLuVioBTUhyyvnuQIkdN4--v_zX78ShAhw8ogVMNosiDXUXDAsHnFFHXLBCgIcrGSIxUXPu_0L6WPipFrGq9P9leqWHFDdTkKS-XDDXactVSkTGgCImNEuIqoKa8GfQHf_wAtJroc0PPABMNJqWC7xP7au-4Kp7o_7LuIeMtj3pm9WiipsSlhjCw5aYzlXMzqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f146b0f2.mp4?token=pi5ycDDV4dmwGDLlJNWXwEXd7qI0esPIIMzwiLeNVkaW7FMqB9G928UTbSZLcEzRXjGLujur7fCLitx8AL-t6cgfQgq2RKlcOYHpSfBjkj7tGvu6o9_47bq8leVfcbf7AwNg-RMR7QSBbpdSUDCduLuVioBTUhyyvnuQIkdN4--v_zX78ShAhw8ogVMNosiDXUXDAsHnFFHXLBCgIcrGSIxUXPu_0L6WPipFrGq9P9leqWHFDdTkKS-XDDXactVSkTGgCImNEuIqoKa8GfQHf_wAtJroc0PPABMNJqWC7xP7au-4Kp7o_7LuIeMtj3pm9WiipsSlhjCw5aYzlXMzqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی وزارت امر خارجه : در شهر به ما پیشنهاداتی شده
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19024" target="_blank">📅 11:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19023">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">صدای انفجار شرق تهران اعلام شده کنترل شده است
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19023" target="_blank">📅 10:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19022">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">عمو یاشار تهران صدای انفجار اومد به جان مادرم راست میگم</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19022" target="_blank">📅 10:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19021">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐂𝐘𝐑𝐔𝐒 ¹⁰:⁴⁸</strong></div>
<div class="tg-text">عمو یاشار تهران صدای انفجار اومد به جان مادرم راست میگم</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19021" target="_blank">📅 10:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19019">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گزارش صدای انفجار جدید تبریز
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19019" target="_blank">📅 10:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19018">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اسکله سپاه طاهرویی سیریک همین الان ساعت ۱۰.۴۱ دو انفجار
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19018" target="_blank">📅 10:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19017">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">صداوسیما : انفجارهای تبریز اولین انفجارها از نوع خود از زمان آغاز حملات جدید آمریکا به ایران در روزهای اخیر هستند. @WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19017" target="_blank">📅 10:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19016">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نهاد دریایی بریتانیایی: یک کشتی که در فاصله ۸ مایلی شمال غربی جزیره "کمزار" در عمان قرار دارد، مورد اصابت یک موشک قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19016" target="_blank">📅 10:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19015">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">روبیو : هیچ تضمینی در مورد عقب‌نشینی اسرائیل قبل از خلع سلاح و انحلال حزب‌الله وجود ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19015" target="_blank">📅 10:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19014">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مهر : اصفهان رو چند دقیقه قبل زدن و یه صدای مهیب به گوش رسیده @WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19014" target="_blank">📅 10:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19013">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hr6WjCC2PGjtPLUpSai4iaYGz4nOsmymTibnSnv8m39c1TL468kT0rSrzeCeFr3n252ApuZNWqh4pDn0zUXzU6mGhsiYU861aSBkT3_mGti_bSu5ZnfUCxHKF2eJ0gDL0XXPCrgQoKQdf0mYyHJNJSsB4gQHNQtvUxFqUA1NnvlYQM4MqMwOalckXUiMeCrjqgBSFYIDPNfdvtyH-dllXkrrcKPmAisJwJC6dOgxdfi0VhuFia1CZEcf2ZLTI_wVmzMmPyANLbC8YojxtF0rOAhTP8OEFvDfA6B3-AZhlrj46qY53bYPqrhSn6HdfGZ6C2YznTkndmo7wtreMLBVvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ماموریت با موفقیت انجام شد . . .
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19013" target="_blank">📅 10:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19012">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مهر : اصفهان رو چند دقیقه قبل زدن و یه صدای مهیب به گوش رسیده
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19012" target="_blank">📅 10:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19011">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اتاق جنگ با یاشار :
امضای لرزه‌ای انفجار هسته‌ای با زلزله طبیعی تفاوت دارد ، ترس به دلتون راه ندید، ایران کشوری زازله خیز است، فقط الان هم زمان شده با جنگ
@WarRoom
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/19011" target="_blank">📅 10:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19010">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وزارت دفاع بحرین:
هدف حملات هوایی شدیدی قرار گرفته‌ایم و سامانه‌های پدافند هوایی در تلاش برای مقابله هستند
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19010" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19009">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گزارش انفجار در کنارک
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19009" target="_blank">📅 10:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19008">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دو انفجار بوشهررررررر @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19008" target="_blank">📅 09:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19007">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نقطه‌ای در حوالی ارومیه نیز هدف حملات آمریکا قرار گرفت
مدیرکل مدیریت بحران آذربایجان‌غربی گفت: بامداد امروز، نقطه‌ای در حوالی بخش سیلوانای ارومیه هدف اصابت پرتابه دشمن قرار گرفت.
در پی این حمله چند نفر مجروح شدند که بلافاصله با حضور نیروهای امدادی جمعیت هلال‌احمر و اورژانس، اقدامات اولیه درمانی برای آنان انجام و مصدومان به مراکز درمانی منتقل شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19007" target="_blank">📅 09:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19006">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVdVVKPqEEw5TaVJ5-feei6VagOejGBhYZESsPnqnmCiCSXtLsKZpObuBDB3BQW696djg-cZWvdCg7bJPYSKSdPJKwXcR3jb13c_oYEN6TIt7BUI_EuWDG7R9aj10GamFkZ7HSVx7ZxWoYgs3bdIb1kjSZpof647yDIK9tUIn7qNRQrjB8zYD3vqxpUUphBOd8ZrBs7-VVNQJaptsGn8EjGXJ1FViWLY7UpuYxG2SbdrzP983fiwMZdc7orynPa-9eLcyl_PrtNkHEo3Bl8yZpyt2wdLpud_-JWj5OkD-9G2pYfGMnTBrQpS_ir6l1qZESf1CKVy3dDb49q_IjgyNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو زلزله شدید ساعتی پیش به بزرگی 5.7 و 5.2 ریشتر در کوزران کرمانشاه به فاصله 5 دقیقه در ساعات ۷:۱۳ دقیقه و ۷:۱۸ دقیقه در عمق ۸ کیلومتری رخ داد
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19006" target="_blank">📅 09:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19005">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">صدای انفجار در بحرین
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19005" target="_blank">📅 09:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19004">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گزارش صدای ‌انفجار اصفهان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19004" target="_blank">📅 09:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19003">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">واشینگتن: سفر رئیس‌جمهور چین، با وجودی که پکن به «دخالت در انتخابات آمریکا متهم شده»، طبق برنامه انجام خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19003" target="_blank">📅 09:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19002">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دو انفجار بوشهررررررر
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19002" target="_blank">📅 09:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19001">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">چابهار آخرین نقطه قبل ناوه دارن برمیگردن رو ناو بشینن هر چیزی مونده خالی میکنند چابهار …
@WarRoom
⚠️</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19001" target="_blank">📅 05:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19000">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">چابهار ۳ انفجار الان و ۲ انفجار کنارک
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19000" target="_blank">📅 05:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18999">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3690b0e4b.mp4?token=c8TDMLVfdY7dnrokmKsZCk8IeEIX-yUQWTx7nGxbeKWP2NOw7HNdRAj8kKWeQXf2LZmuoRqzjsUKZkHmtKAjmehVnH63jz8ctAqSEBlr_mtcblnaPlzodMPj_05Rwto3jCD1lGr9Xg-HnuAXj8bn8moOxlecEZD-iqd0ShXfBFlyEA_MlfgDj4KhHs6BfOGV6ZD474fG8GgFZY96GVDu8ise49YXpdpmAkVEQNfCJ1dLo-ThvDdJNN5bo_ylnmOEsjQupYmBcZaHsOTG8BPnGvS5OFAdEaVR7ZYKYa288cb0o0o936bm-onQsrahf7LtbRRG5kgCdfCsW8KZmgETUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3690b0e4b.mp4?token=c8TDMLVfdY7dnrokmKsZCk8IeEIX-yUQWTx7nGxbeKWP2NOw7HNdRAj8kKWeQXf2LZmuoRqzjsUKZkHmtKAjmehVnH63jz8ctAqSEBlr_mtcblnaPlzodMPj_05Rwto3jCD1lGr9Xg-HnuAXj8bn8moOxlecEZD-iqd0ShXfBFlyEA_MlfgDj4KhHs6BfOGV6ZD474fG8GgFZY96GVDu8ise49YXpdpmAkVEQNfCJ1dLo-ThvDdJNN5bo_ylnmOEsjQupYmBcZaHsOTG8BPnGvS5OFAdEaVR7ZYKYa288cb0o0o936bm-onQsrahf7LtbRRG5kgCdfCsW8KZmgETUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد
نهمین شب متوالی حملات علیه ایران
در
۱۹ ژوئیه، ساعت ۱۰:۰۰ شب به وقت شرق آمریکا (ET) (۰۵:۳۰ بامداد ۲۰ ژوئیه به وقت تهران)
با موفقیت به پایان رسید.
به گفته سنتکام، نیروهای آمریکایی
مراکز فرماندهی نظامی، سامانه‌های پدافند هوایی، مراکز دیده‌بانی ساحلی، توانمندی‌های دریایی، محل‌های پرتاب موشک و پهپاد، و شبکه‌های ارتباطی ایران
را هدف قرار دادند تا توانایی ایران برای حمله به کشتی‌های تجاری و خدمه غیرنظامی عبوری از
تنگه هرمز
بیش از پیش کاهش یابد.
سنتکام افزود که
به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)
، ارتش ایالات متحده ایران را در قبال اقداماتش پاسخگو می‌داند و نیروهای این فرماندهی همچنان در
آماده‌باش کامل، متمرکز، مرگبار و آماده اجرای مأموریت
قرار دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18999" target="_blank">📅 05:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18998">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سپاه:
هواپیماهای ترابری بزرگ C-17 و هواپیماهای فرماندهی و کنترل P-8 ارتش آمریکا با موشک‌های بالستیک در فرودگاه عقبه هدف قرار گرفتند.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18998" target="_blank">📅 05:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18997">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ارسالی : درود بر شما همین الان کلی امبولانس و اتش نشانی دارن میرن سمت خجیر ، انفجار بوده
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18997" target="_blank">📅 05:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18996">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18996" target="_blank">📅 05:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18995">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gA6wOpJ3ruioNd8FMiwP9kvqIjgWw0i1XYEePyr1jUR5bW41WmruUU42NIEpK04qmTfXQQMw8z4OUbt_Hy0RNq8NYWk5LOtQb6hdBrlfsIjQtIrIpmgqOxEsHOj2U7LpyHXt-ZTZwuWY6F9kxZgwQilNkv4pngh3wbOPfBgWsI9uuIiJ75Cml26gQQSa4ShrCn6NGZ2v-kovdIj5NS5er0E9AymuSEaqZ1sYPm8OAa0Tzn3RkIV2ePKPGCQdX2HYb011DHB7zKd_xtHC4Q5d2agjTG-qJQqn6PBi4QwHG4xmUnie-cLqhg-BX7ZukTMR5KgPvl3KNbSMea_DoM_jtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : درود و عرض ادب یاشار جان.
من سمت شرقم و اینجایی که زده سمت خجیر میشه ولی من صداشو نشنیدم ولی دودش معلومه.
تاییده انفجاره شرق
@WarRoom
یاشار: من بالای پانزده پیام دارم که صدای انفجار را شنیده‌اند. حتی یکی از کاربران با ماشین در خیابانها افتاده و دنبال مکان انفجار میگردد. ممکنه حمله هوایی نباشد و یک انفجار دیگری باشد، ولی به هر حال این دود مشاهده میشود و صدا شنیده  شده.</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18995" target="_blank">📅 05:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18994">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">شهرهایی که امشب تا این لحظه مورد هدف حمله قرار گرفتند؛
💥
تبریز
💥
بندرعباس
💥
چابهار
💥
ماهشهر
💥
سیریک
💥
کنارک
💥
جاسک
💥
خورموج
💥
دشت آزادگان
💥
خرم آباد
💥
سربندر
💥
دزفول
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18994" target="_blank">📅 04:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18993">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گزارش انفجار شرق تهران
🤯
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18993" target="_blank">📅 04:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18992">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گزارش انفجار کرمانشاه
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18992" target="_blank">📅 04:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18991">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گزارش انفجار کرمانشاه
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18991" target="_blank">📅 04:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18990">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دقایقی پیش, مرکز تجارت دریایی بریتانیا: گزارشی مبنی بر وقوع یک حادثه در فاصله ۸ مایلی شمال غربی شهر کومزار، عمان، دریافت شده و یک کشتی در حال سوختن است @WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18990" target="_blank">📅 04:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18989">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">به گزارش خبرگزاری صدا و سیما، حملات هوایی ایالات متحده بندر سیریک در جنوب ایران را هدف قرار داد تا عملیات جمع‌آوری اطلاعات ایران در تنگه هرمز را مختل کند.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18989" target="_blank">📅 04:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18988">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رسانه های رژیم : به دستور مجتبی خامنه‌ای ، موشک‌ها و پهپادهای "ولایت" به زودی به پایگاه‌های دشمن آمریکایی در منطقه ضربه خواهند زد.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18988" target="_blank">📅 04:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18987">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ : اگر نگاه کنید، پس از حدود یک هفته و نیم تا دو هفته از آغاز جنگ، احتمالاً جلوی پیشرفت آن‌ها را گرفتیم؛ البته نمی‌خواهم از واژه «احتمالاً» استفاده کنم
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18987" target="_blank">📅 04:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18986">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">صداوسیما : انفجارهای تبریز اولین انفجارها از نوع خود از زمان آغاز حملات جدید آمریکا به ایران در روزهای اخیر هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18986" target="_blank">📅 04:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18985">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دریا بانی گروگ  رو زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18985" target="_blank">📅 04:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18984">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فاکس نیوز : فرمانده کل قوا(ترامپ) هیچگونه مذاکراتی رو قبول نمیکنه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18984" target="_blank">📅 04:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18983">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQ3yW9x_SrRwkTStyjVbgs4mdg87woQFHbFCLpcC7tZOqByeSFoboD8clWwjChyqq_YM7-iix7p451yEOA86dld_rwlUa4siz-pcGAFuKcz3TUD3ysGReTRfbNCKLbEuAHpzTKYcUsLUXaWY7gQjy32xV-WDJPLeYDFo0bskfxrPGfMB6HtuaPxVJ2BK6YESOclnfM0WIFLW9Z2Do0uxtWgberRvEo5hgIDZ9uvSP2N2MNbvrmxVWi_9O1gGKH5x-0-jvmQ0Ii0NeRzoqlybNgzXlj75uLbXBqun8Xyef05ejjl70RsHAz_dqHhEbSn4s6My63Gs1a1EiE67QGzvrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقایقی پیش
,
مرکز تجارت دریایی بریتانیا: گزارشی مبنی بر وقوع یک حادثه در فاصله ۸ مایلی شمال غربی شهر کومزار، عمان، دریافت شده و یک کشتی در حال سوختن است
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18983" target="_blank">📅 04:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18982">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebbc46a29a.mp4?token=VL38bDOYrRQ8_Yg19w9npLFISQri3vY9qg7lGWk2FDA0HAV-7vqN3QzKi7D0QohPxdXWoY0QjIw9ScLZTZXOzvept32Ofa4wf3WJAzcHQR91tez9PkNMclLlWzuwr79OEgdFw5TzYhz0s6hSA75_eMsos8pI-VjjQXKQRcxfRQDNchbCgteLf_Xvi_wyT_Wc77wBDaCxBkRrudOSpLH29vk-sOAagdk7wOrtghEyC1JuWSo9_QFwRGSsn2U_CWjXUtvxCY3mb3nQg9HrKsdVCsmsyhC7ITC7OKLIv79SOKGa0s2J_QFbMaOI5Z5m1McUrU-J51k9DjZVKvhOr1WyLmxotOM3wNLlc720h0WLbfX9Ybac1cY70PjdIqxKiVPHAAU_doaKOCLK5d7xxdqn9CjgqcwV7xUX2hjYcterRzUFV0dXlAWYw3I6LiLIlh9bSn9pbYrCyOfV1D9rpEUsECjEIgMu20qd-6OQokJ9tLVgsWRkmCIbfsIpb_vvNHpKZ24zqMosbSbX1M6Hfz4DFx1FNj9Qtt03UeiiyL4t-a3mbeyEQwSSSAhcfunKbVMesQAo0XnVOQiqfQKpyMTZ_mNrmZh8oOigysGbacsRxP2veWb5q49uCqFKgwEJ53Ah3RS72xmmQ26CJ6Celhu5hIffKcR03SmDMA_GNXfD-Xo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebbc46a29a.mp4?token=VL38bDOYrRQ8_Yg19w9npLFISQri3vY9qg7lGWk2FDA0HAV-7vqN3QzKi7D0QohPxdXWoY0QjIw9ScLZTZXOzvept32Ofa4wf3WJAzcHQR91tez9PkNMclLlWzuwr79OEgdFw5TzYhz0s6hSA75_eMsos8pI-VjjQXKQRcxfRQDNchbCgteLf_Xvi_wyT_Wc77wBDaCxBkRrudOSpLH29vk-sOAagdk7wOrtghEyC1JuWSo9_QFwRGSsn2U_CWjXUtvxCY3mb3nQg9HrKsdVCsmsyhC7ITC7OKLIv79SOKGa0s2J_QFbMaOI5Z5m1McUrU-J51k9DjZVKvhOr1WyLmxotOM3wNLlc720h0WLbfX9Ybac1cY70PjdIqxKiVPHAAU_doaKOCLK5d7xxdqn9CjgqcwV7xUX2hjYcterRzUFV0dXlAWYw3I6LiLIlh9bSn9pbYrCyOfV1D9rpEUsECjEIgMu20qd-6OQokJ9tLVgsWRkmCIbfsIpb_vvNHpKZ24zqMosbSbX1M6Hfz4DFx1FNj9Qtt03UeiiyL4t-a3mbeyEQwSSSAhcfunKbVMesQAo0XnVOQiqfQKpyMTZ_mNrmZh8oOigysGbacsRxP2veWb5q49uCqFKgwEJ53Ah3RS72xmmQ26CJ6Celhu5hIffKcR03SmDMA_GNXfD-Xo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: امشب ایران رو بازم شدید هدف قرار دادیم!
این حمله در پاسخ به کشته شدن نیروهای آمریکایی بود؛ ۳ نفر از نیروهای ما کشته شد
ایران از نظر نظامی تقریباً همه‌چیزش رو از دست داده؛
فقط تعداد کمی موشک، پهپاد و توان تولید براش مونده، ما تنگه رو کنترل می‌کنیم و ایران هیچ کنترلی روی اوضاع نداره
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18982" target="_blank">📅 04:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18981">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ: امشب حمله بسیار قدرتمندی علیه ایران انجام دادیم
ایران آسیب بسیار شدیدی دیده و نمی‌تواند سلاح هسته‌ای داشته باشد.
ایران ممکن است تعدادی موشک و پهپاد داشته باشد، اما تعدادشان زیاد نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18981" target="_blank">📅 04:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18980">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دو انفجار بندر عباس
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18980" target="_blank">📅 03:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18979">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CK2aLGLaso7HgIiMDI7pmW1dRd90q1AJyNdWgsymsTZmsVZgY7sTg2y4gTJxhKtGe8JBiAGPVrPVr9Kj_DLxdBntuwYGwCLUHT1EdTO1PIgaCLhvBRcRXSC-bWRqbdz3gvTI1K2vwqlifMYfD0i6IzDrnqcEPRo8_GsnpUR-PVo1tK3zSPypmGzGcKI5rI7YarB3B37U6OuUUqKM1DziMjkek3QoZfcAF-oLLijg49Ce5Ycvqy7jg-dOg3wTwKKV9G_YOquxqdO93GjH3MOR8EVD55lLnBxKp05GZq_0br_6liyDoVqIe_aqvjy5DZC57vPyYO8N4GDDAl7EqWRP8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کنارک انفجار سنگین
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18979" target="_blank">📅 03:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18978">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTRw6gk0kGOf9dc0PTyH6CMoL_ZMSaiHJzkP35k2DQb9rAO8vX3nZ3d17O37Z9sha_flbAHKsK6vWCz-xHU3-JDIxC0jbp_D5E5u6DwWHTAdq5Vu8SL2BLa40gskssM1x0DzsOj55CFwKI8wkTbi144AbLJpaqO2ZD82Rs4eCcD1ZG8IQw0eU71Epao1fg-56qR_9QMJYDYDUQPDLLKXbJQSQ2ThFA7yjH0q1N24vUmATRA4XXnBeT05dwllbbkWCvbxqLzPsrz-00ilIb5qkyKjMpzySAHJac4A8JfeIl_RQIvtrqe8pDiFuWN6tJs73U0BYmSBUGDKkirnvsNeLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیریک اسکله طاهرویی
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18978" target="_blank">📅 03:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18977">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7dd005bae.mp4?token=g2sN80Z1eJNJCXWsBZx45z-85QUQ_y594AWnSj53NyxcOWtqZVpA8ThZf2iyBWXD03bHEL0TZlkB2jU6-YtwgtT0tNkp93S5ZaqQpdxAugHhrGoxUY_bKYww87MRWtIwBEgb-OWlUYEbPsnMWfXiqWU49-frcqZ90hlaIb5VuceDUWsR11IW6E4QFKOERB6ffUfX1Oi-6Fg0a6gMFxMZ4-m5z4bN9LbWQ8HKnZ8b_ymDEjO_S-xPEFOSSfaFJuW6TTxs_5Pt0htg_Hj4LXz0V7aVL9sPVRZlf_uuK-JMg0q58oRxAHg5fEH66N2q1SWtkSKbwi1iw0eVmtVK6TItOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7dd005bae.mp4?token=g2sN80Z1eJNJCXWsBZx45z-85QUQ_y594AWnSj53NyxcOWtqZVpA8ThZf2iyBWXD03bHEL0TZlkB2jU6-YtwgtT0tNkp93S5ZaqQpdxAugHhrGoxUY_bKYww87MRWtIwBEgb-OWlUYEbPsnMWfXiqWU49-frcqZ90hlaIb5VuceDUWsR11IW6E4QFKOERB6ffUfX1Oi-6Fg0a6gMFxMZ4-m5z4bN9LbWQ8HKnZ8b_ymDEjO_S-xPEFOSSfaFJuW6TTxs_5Pt0htg_Hj4LXz0V7aVL9sPVRZlf_uuK-JMg0q58oRxAHg5fEH66N2q1SWtkSKbwi1iw0eVmtVK6TItOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایگاه امام علی در چابهار
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18977" target="_blank">📅 03:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18976">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18976" target="_blank">📅 03:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18975">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دانش آموز های ساری تهران و اصفهان تبر دارن میزنند ، هیچ خبری نیست</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18975" target="_blank">📅 03:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18974">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdSHSHgHL8Ou4okguhMyPz4ddyEVqiZSUgM8KkRJddB5nT0w0cHBdnBzRTUkKR2h8roRUbAdMKWtiw9w4MLmvLU7DZ5mlbx9r6WhomaETB1QLwQIbX7n8icINmvBBWY0FBAlacGGwCl-3I5tR3Sm9H1guOK1nq5bMzmSTeUhLBuoVpE8JuTy6a0P3kVao5TtovxbiYtRmpVpA3Ml1yPkKS995FLi_NqdeYpvJNXZ_54QuW6t7GS6fMqsra95ISncXBa-AvJo3M5bonk38ohIRol2U35zAkgm0FzI_aN6Knjz_ZRASKmvAOD5t4LglLSS23M9rZfz2X_JqQmAKGwKkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقدر آزارم ندید !
😔
اخبار فیک نفرستید تهران تهران</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18974" target="_blank">📅 03:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18973">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یاشار همین الان جاسک دوتا انفحار وحشتناک به فاصله ۵ دقیقه از هم
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18973" target="_blank">📅 03:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18972">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سیریک رو با جنگنده بد زدن @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18972" target="_blank">📅 03:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18971">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سیریک رو با جنگنده بد زدن @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18971" target="_blank">📅 03:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18970">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cC0qoS9dOS3dXRWLDR4Kur24CN-VxBX5JzOUmBXhDnJFi9rWhrRHHM_xaXLmrJDr2RkMhBKfbS-5APDz2xlHXiqlHp5Dkqz8Uek5-iVqjTm9z126hMXdkDJVAvGYWt-o4Pt3kmG7KJfO3x9WFa2Z2mABRejd914g52YXkXTJ1a7nlxIXHPAAZUMB6yU93uIRbfyjEUYjUQ6hNbHNZ36BABDoc35kTDrNfVQgv9Ag_TjROtNDEEmVBqDzYnaoIyBnBkTMhAAaaAneYB3MP4JWytGiJFW3zT6pAVT_YWcpOpsKp69p2d88J7B9aRvDhE9N6lit7IgfKNZYw580Z1K7OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سربندر / ماهشهر
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18970" target="_blank">📅 03:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18969">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خورموج ، برق رفته و میزنند تند تند
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18969" target="_blank">📅 03:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18968">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سیریک رو با جنگنده بد زدن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18968" target="_blank">📅 03:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18967">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گزارش‌ ۳ انفجار در تکاب آذربایجان غربی
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18967" target="_blank">📅 03:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18966">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4812b607a5.mp4?token=o6tjTxxV0XTUjkCdn2H097VUyNSWbnR24wYant93oUUABlIiNxj08mYgS1aY4L4WBpoH_3LV_PeBbgLDE4I55vzs74-2pQNE5fYo_-uO_Sq6oOf7MRH66W0oPvAAq6nnvQ-kHGgB5TPrUAbpZ2ttQY9b4p3dU6PNvtUFSZz1wstSiX0wR_Aiev1yb3ffZmEthoUnYh12xTAfn2dxdFSSWd_pUlPHajoudBhf-_61nginLuWZLnguc0ZIdhuM2KUdpMZXGf4vIJ5wIfWTbCk2G8y3wiKFNNhFVzx8TWBBf0lihFxiEFzGVkqyyX0v9vrGVMbnXxrIV82cRWSbH31b1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4812b607a5.mp4?token=o6tjTxxV0XTUjkCdn2H097VUyNSWbnR24wYant93oUUABlIiNxj08mYgS1aY4L4WBpoH_3LV_PeBbgLDE4I55vzs74-2pQNE5fYo_-uO_Sq6oOf7MRH66W0oPvAAq6nnvQ-kHGgB5TPrUAbpZ2ttQY9b4p3dU6PNvtUFSZz1wstSiX0wR_Aiev1yb3ffZmEthoUnYh12xTAfn2dxdFSSWd_pUlPHajoudBhf-_61nginLuWZLnguc0ZIdhuM2KUdpMZXGf4vIJ5wIfWTbCk2G8y3wiKFNNhFVzx8TWBBf0lihFxiEFzGVkqyyX0v9vrGVMbnXxrIV82cRWSbH31b1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله آمریکا به سایت موشکی تبریز :
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18966" target="_blank">📅 03:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18965">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خبرگزاری رژیم تسنیم :
از دقایقی قبل صدای انفجار در شهرهای تبریز، چابهار، کنارک، بندر ماهشهر، بندر امام خمینی شنیده شده است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18965" target="_blank">📅 03:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18964">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انفجار سنگین و بی سابقه در ‌سیریک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18964" target="_blank">📅 03:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18963">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q21YNEsFLhONCyuCuhRh9X1XlxE-j043Ht6ucb9yuG2oA75P1_evr7SJy2gbxATFQnBWzzal_LYiNfi6d11msnjSBAEvbsRRNGw_V8OJR4ko54EmUZ0EMbOcVczvpeRFQYOq_1TV_CJbtFujVamnfgAntJoO1h2nszqJX9WBJtROuOU0Y4fy0WPHiYs_18L6rwavbkj7A6m1SUE7vkXWy1aLlNQ4sbGfUHJLFKC9h_ZTELdmDWLW8WX-DbPi6co5F8eImjqmQEXAdeY04F0sJ-kRag46zbAG2tMKDC0kE_XIgIj7m7EA1-2OuflkrShoJIPaHjlNnqrb611zyIzcTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار و ستون دود در جنوب غرب تبریز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/18963" target="_blank">📅 03:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18962">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گزارش از شلیک موشک از کویت به ایران
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18962" target="_blank">📅 03:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18961">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">چابهار همچنان میکوبه
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18961" target="_blank">📅 03:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18960">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">انفجار در بندر ماهشهر و اکام هم گزارش شده
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18960" target="_blank">📅 03:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18959">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تبریز رو زدن بدجوررر
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18959" target="_blank">📅 03:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18957">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گزارش ‌انفجار‌ چابهار
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18957" target="_blank">📅 02:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18956">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سنتکام : امروز، ساعت ۷ بعد از ظهر به وقت شرق آمریکا، موج جدیدی از حملات علیه ایران را برای نهمین شب متوالی آغاز کرد. این حملات به تضعیف قابلیت‌های نظامی ایران که برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامی در حال عبور از تنگه هرمز استفاده می‌شوند، ادامه خواهد داد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/18956" target="_blank">📅 02:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18955">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کویت زیر حملات
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/18955" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18954">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پهپادهای موتور گازی در آسمان شهر سلیمانیه در شمال عراق.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/18954" target="_blank">📅 01:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18953">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پدافند شاهین شهر اصفهان درگیر شده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/18953" target="_blank">📅 01:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18952">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">الان بی بی میاد به جای مسی‌گل میزنه
😂
دقیقه ۱۱۹</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/18952" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18951">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMfhgD9v4VaaesS2YzKxdqE4VmhBrSDLTjomE9unfExNryRgquNwRy8uCAbBUFmxINmbktAA07eHiRH9Fk3Xm79X3BgRY6JFQOGSOpfQ20_Gy5IRiTknkGJ_dVkcMFJeAVEJ4HAn7CY7DcgiBSefkksiRmfJuPKNAw9NsSRfwWPzgXVZG3jCunsWJn3KdHf8eUbFOFY8iimz61T2U9ynMpb9x_y-MGtjnXeMxu1Tq-uSLvl2MDIJZtWInvFjghjPqht1PrMfRLwKZLD0MXWvLSktBwrgAWgDPjGZHoYHNciaBJYSso4P9fJy6DnZbqAARyKW0IKvJ2wVMFrr0d3zUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمام و اسپانیا قهرمان شد
🥲
@WarRoom</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/18951" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18950">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گلللللللللللللللللللللللل دقیقه 105 برای پرتغال توسط رونالدو توی PS5 @WarRoom
🤯</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/18950" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18949">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">من اینجا شوخی‌کردم بخدین وای گل اسپانیا واقعا دقیقه ۱۰۵ زده شد
🤯
🤯
🤯</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/18949" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18948">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گللللللللللل برای اسپانیا
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/18948" target="_blank">📅 01:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18947">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دیدبان اتاق جنگ : انفجار در سیریک تو دو نوبت یکی بین دو نیمه یکی هم وسط نیمه دوم شنیده شد
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/18947" target="_blank">📅 01:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18946">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گلللللللللللللللللللللللل
دقیقه 105
برای پرتغال توسط رونالدو توی PS5
@WarRoom
🤯</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/18946" target="_blank">📅 01:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18945">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15c3751fd1.mp4?token=GrxBXWwDOp6K59SSqKH0AJ9cMeKKf7HCv9uHFT2ahdB-eURYf2pD-codJeZ2N25H05W3zQnKYDL36Z6mHkljxX2-V5JF4V2KVnsYCTDcq57uRdlGvRIa74nvQPQrzbVLTZapeJiHE9EqJCs6iPyWp1WibHnJU2NL0S7WeaqJq22TZxXFJJdCBNJI0V3_dz-LYL21P9r8kl5wXtgEQAUOhNw7jESRRg7wdfhGthMuhWjdrzjftkstmF6wjx5MR6IFjc3Uw7ZkvFsCjb4yIt6FjXAs-68BmE5GDSbzKthdKgsAHQWkSdb6zKIEA24lVU8z3SW2Q5m-XJzByXYSTvaEDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15c3751fd1.mp4?token=GrxBXWwDOp6K59SSqKH0AJ9cMeKKf7HCv9uHFT2ahdB-eURYf2pD-codJeZ2N25H05W3zQnKYDL36Z6mHkljxX2-V5JF4V2KVnsYCTDcq57uRdlGvRIa74nvQPQrzbVLTZapeJiHE9EqJCs6iPyWp1WibHnJU2NL0S7WeaqJq22TZxXFJJdCBNJI0V3_dz-LYL21P9r8kl5wXtgEQAUOhNw7jESRRg7wdfhGthMuhWjdrzjftkstmF6wjx5MR6IFjc3Uw7ZkvFsCjb4yIt6FjXAs-68BmE5GDSbzKthdKgsAHQWkSdb6zKIEA24lVU8z3SW2Q5m-XJzByXYSTvaEDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا چون پرچم پشت دروازه آرژانتین است صدا و سیما نمیتونه سانسور کنه و هی نشون میده
😍
🤣
🇮🇷
@WarRoom</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/18945" target="_blank">📅 01:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18944">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4eO8ptsC40892WJO4mgRBVvxmr8WqWlreHxPDvB6tdRpy3sSbyOZHrMufXzdOoIyyl-gtkk0n4XO-2eU3ko2LCKSw3OrV92Nx5Fii8DsCLMEXQFKpBL5iGs4uzf8QGoks86ATRzAKkozR3DhIo-XhnVmlX5YklBsDNy6_hAxZUolrBMnHk0Md8PLjUCT_aWd34LbrrBQv55C7Q7lZLoaLVlqEbTp1h6RIMCnHcDvgJM9AFPjCQhM6l5IwlC-kfqp3njTddneQ8wgYPw8ULA4yLnxWPifRE1wUn8SFxl9b_L9mKSlp6NG_lq_Ff9IPw80aVN62-ZRWPV1PwFg9MIaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیک موشک همین الان بخش بمانی سیریک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/18944" target="_blank">📅 00:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18942">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6qDMjjGfR0DKdh4S8TselUVQ5hnKJjX5dtKnBGTe3UDC4Y-q15IeBJNM-kX_aHakCnVLp6MCfYU7k9SePtmOLnUBWBmmZhN0Fki-08UmTHAe_qQHDQQg_eokxXoeiPd8D3xkW89DnbTnw0lBk0ECj_xXLU2J8r4BY_e_nruL8E8FvGY8b9MS9oYmrzH0JJrLBB5rPATFvvnAz96KjQH6-Pr9GZ7eGVT9QYdao5j6X6GwL4m2rctjqCTL3SQVGDGeXVdgdDuKITtDyui2KDON35LxLGl8ZOlydXg1bnRB3sACFe3iNYa-EPHxZYsP7yrK9LUxx1j8tmJlBkh2WyT2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از اجرای طاعات و عبادات، هواپیمای E3B آواکس از ریاض عربستان بلند شد و یک سوخترسان هم ، هم اکنون روی باند در حال برخاستن است.
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/18942" target="_blank">📅 00:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18941">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">آرژانتین ۱۰ نفره شد
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18941" target="_blank">📅 00:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18940">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آژیرهای هشدار در بحرین به صدا درآمدند.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/18940" target="_blank">📅 00:38 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
