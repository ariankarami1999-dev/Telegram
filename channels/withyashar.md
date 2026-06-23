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
<img src="https://cdn4.telesco.pe/file/vTwKHL0SD_peP_Vtu02mtyH8TQVdJt4TY51i9LYQCvALDmFEe5N6iYyWVlUYK014mVuyrPbRQ5teV-6Sdt4_beW98dJhcioT8Bx_XsXMnriLiNq4_Nu3guGqldaHUHoOj5ergAH9GW5dntAqh5EVYDMxw_XcPRGfIeruc3-Hzp0LOxgLmAsKH7W93QQ1x7rNme36eVVU1-aPEPvnvbi-EKqVGwihkI4_N5ngvWvNNdM_CdXPpCHxm2XZYNBDdsPnQKcumHCS80Zr_T4lIZC9DPaVvSAK-RDNHKd39hf0aLjRrw0BHvza9VNA7KApzvfJSuIie5oLa50JSBGcOBcGdw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 331K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 11:54:03</div>
<hr>

<div class="tg-post" id="msg-15648">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ: خودروسازان آمریکایی تولید سلاح را آغاز خواهند کرد
رئیس جمهور آمریکا در کاخ سفید به خبرنگاران گفت: «آنها برنامه‌هایی برای تغییر کاربری کارخانه‌ها دارند. ما قصد داریم سلاح‌هایی از جمله موشک‌های پاتریوت، موشک‌های تاماهاک و موارد دیگر تولید کنیم.»
@withyashar</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/withyashar/15648" target="_blank">📅 11:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15647">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">هواپیماهای سوخت‌رسان نیروی هوایی ایالات متحده پس از تخلیه از پایگاه هوایی العدید در قطر به دلیل جنگ ایران(یک روز قبل از جنگ)، به این پایگاه بازگشته‌اند. حداقل ۱۲ فروند در حال حاضر حضور دارند.
@withyashar</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/withyashar/15647" target="_blank">📅 11:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15646">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بقایی: توانمندی دفاعی و موشکی ایران هیچگاه موضوع مذاکره با هیچ طرفی نخواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/withyashar/15646" target="_blank">📅 11:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15645">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">الجزیره: «تغییری بزرگ» در سیاست آمریکا؛ ایران اکنون می‌تواند نفت خود را با قیمت کامل بفروشد
این اقدام صد‌ها میلیون دلار درآمد اضافی برای اقتصاد ایران به همراه خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/withyashar/15645" target="_blank">📅 11:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15644">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مایک والتز، سفیر آمریکا در سازمان ملل:
جمهوری اسلامی ایران با بازگشت بازرسان هسته‌ای به ایران موافقت کرده و این اولین گام برای توافقی گسترده‌تره.
برخلاف برجام، این بار بازرسی‌ها باید در هر زمان و هر مکان ممکن باشه.
@withyashar</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/withyashar/15644" target="_blank">📅 11:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15643">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">عماد الدین باقی: طبق بند 2 توافق ایران و آمریکا، از این به بعد شعار مرگ بر آمریکا یا سوزاندن پرچم این کشور و لگد کردنش تو مراسم‌ها و اجتماعات رسمی (مثل نماز جمعه) ممنوعه.
@withyashar</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/withyashar/15643" target="_blank">📅 11:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15642">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">https://t.me/boost/withyashar
یه لول اومدیم پایین ایموجی کم شد لطفا اگر کاربر پرمیوم هستید بوست کنید و اگه نیستید از دوستانتون که هستند درخواست کنید بوست کنند</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/15642" target="_blank">📅 02:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15641">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">@withyashar
FPV  آتش بس و</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/15641" target="_blank">📅 01:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15640">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">@withyashar
شصت روز سنگین</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/15640" target="_blank">📅 01:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15639">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc8773aac7.mp4?token=XIyXD8_Hqkb9cplHl5_bHNfjDTyyQoTPvaQnDIKZJGaZRjHP9S7o6TkTIoEmpTHzFcRCA6XAWCwtYlfgU1MCzdSten1LIqU_tLo7OXeS7mBt21gAYfwb8s_SUTNaa9UDy_QIkTcLVg5FKtGrAG8IZYtekSdFF7bdTNSTbcrtnI1TvBzFrIieEh97wgQS3ewSuUyiARAYwvMawQD0E8vjssucbaLoNaUHz3C8acYolpyZqDmLQzyRaGkQYywEB-i79Y3NGCVnXFPyT2Nlcwsx2nnx-Bv3h5g9b9X98PyH5Shx0jTcs0BJowwBkp__H883xeGV46QEC2zgOHUPgQUypw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc8773aac7.mp4?token=XIyXD8_Hqkb9cplHl5_bHNfjDTyyQoTPvaQnDIKZJGaZRjHP9S7o6TkTIoEmpTHzFcRCA6XAWCwtYlfgU1MCzdSten1LIqU_tLo7OXeS7mBt21gAYfwb8s_SUTNaa9UDy_QIkTcLVg5FKtGrAG8IZYtekSdFF7bdTNSTbcrtnI1TvBzFrIieEh97wgQS3ewSuUyiARAYwvMawQD0E8vjssucbaLoNaUHz3C8acYolpyZqDmLQzyRaGkQYywEB-i79Y3NGCVnXFPyT2Nlcwsx2nnx-Bv3h5g9b9X98PyH5Shx0jTcs0BJowwBkp__H883xeGV46QEC2zgOHUPgQUypw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
آیا می‌توانید تضمین کنید که ایرانی‌ها از سود فروش نفت برای بازسازی ارتش خود استفاده نکنند و فقط برای دولت بعدی آماده شوند؟
ترامپ:
خب، آن‌ها قرار نیست این کار را بکنند، قربان. خواهیم دید، اما قرار است پول را برای خرید غذا برای مردمشان استفاده کنند، چون در حال حاضر مردمشان خیلی گرسنه هستند و آن را فقط از ما می‌خرند — ذرت، سویا.
تباید پول زیادی باشد. امیدوارم پول زیادی باشد.
@withyashar</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/15639" target="_blank">📅 00:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15638">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ: اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من آنچه باید انجام دهم را انجام خواهم داد
با یک تماس تلفنی میتوانم محاصره را برگردانم
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/15638" target="_blank">📅 00:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15637">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ: هیچ‌کس نمی‌خواهد رئیس‌جمهور ایران شود. @withyashar</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/15637" target="_blank">📅 23:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15636">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">قالیباف: اگر به سوئیس نمی‌رفتیم، هر لحظه خون بیشتری از مسلمانان و شیعیان لبنان ریخته می‌شد
@withyashar</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/15636" target="_blank">📅 23:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15635">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ: هیچ‌کس نمی‌خواهد رئیس‌جمهور ایران شود.
@withyashar</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/15635" target="_blank">📅 23:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15634">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خبرنگار: نتانیاهو می‌گوید نیروهایش لبنان را ترک نمی‌کنند
ترامپ: ما قرار است به این موضوع نگاهی بیندازیم. من یک حل‌کننده مشکل هستم؛ می‌توانم مشکلات را سریع حل کنم، از جمله با بیبی.
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/15634" target="_blank">📅 23:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15633">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ: «تا زمانی که ایران به ما احترام بگذارد نمی‌خواهم از واژه “ترس” استفاده کنم چون مناسب نیست تا وقتی به ما احترام بگذارد، ما هیچ مشکلی نخواهیم داشت.
ما کنترل کامل تنگه را در اختیار داریم.»
@withyashar</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/15633" target="_blank">📅 23:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15632">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">قالیباف در سفر به مسقط: در سوئیس توافق کردیم تا 12 میلیارد دلار پول مسدود شده ایران آزاد شود.
@withyashar</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/15632" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15631">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏زنده‌یاد⁧ مانوک خدابخشیان  ⁩: چه کسی می‌خوهد این رژیم را براندازی کند؟ چه کسی می‌خواهد پایه‌های این رژیم را اره کند؟
@withyashar</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/15631" target="_blank">📅 23:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15630">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/15630" target="_blank">📅 23:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15629">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شبکه 14 اسرائیل که به نتانیاهو نزدیکه، مدعی شده ایران از یک «سلاح الکترومغناطیسی با فرکانس پایین» برای تأثیر گذاشتن روی تصمیم‌های ترامپ استفاده می‌کنه!   می‌دانم این حرف طوری به نظر می‌رسد که انگار از یک فیلم علمی‌تخیلی آمده، اما واقعاً وجود دارد و همین حالا…</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/15629" target="_blank">📅 22:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15628">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یک مقام ارشد اسرائیلی به کانال ۱۴ درباره لبنان:
امشب دوباره با ارتش اطمینان حاصل خواهیم کرد که دستورالعمل‌های کابینه برای هر مبارز روشن شده است
ارتش مجاز است هر تروریستی که در منطقه زرد شناسایی شده است و علیه هر تهدید واضح حتی فراتر از آن، ضربه بزند.
@withyashar</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/15628" target="_blank">📅 22:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15627">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وال‌استریت ژورنال:
ترامپ این هفته با رهبران پنتاگون و پیمانکاران بزرگ دفاعی دیدار خواهد کرد تا برای سرعت بیشتر تولید موشک و مهمات فشار آورد
@withyashar</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/15627" target="_blank">📅 22:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15626">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAHgLQ79xrnCf6SAVB3hp9kMs3Qq3iqsfyaXH5EaYyGNtF4xRJhqYElUKdtcqnqKA1_iysM-lKt-zzNG99CgeDurRBK4X7zJ0eaDGu6YY33FPIA7yaxRcGexvIVtOI_PdoqZkPl7-xkDtbJ-0eqFGqHVKXm5DId6n0R4fxPhkyLGTjAtzaLGTeDImWs98dc9G58ie1PvHDsuXRSwV-9piCh4A_Cdtn7-XIlk_QdRziVgC89rujseElLTMZN5usyFhgeRn5DD4DDGa36_a7EGdKpLLJHxLuk5lvUyS2I3t9JjHcigWq5EA3OD9LvKALrARc8c8zYbKZULJtZNq6tYbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای ممباقر (هیئت جمهوری اسلامی) همکنون در مسقط عمان به زمین نشست.
@withyashar</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/15626" target="_blank">📅 22:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15625">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ونس معاون ترامپ لحظاتی پیش سوئیس را به مقصد آمریکا ترک کرد
@withyashar</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/15625" target="_blank">📅 21:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15624">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fe556e38.mp4?token=TlPb2OymtsBAo9mjxrTX62tw0d3p_ZLZpMXEtsYwpb2UpzUSWsN6xJ61k5myb6W2U-BUeOtkjZJByAF9WSf1GbW0aAY9Q7B6pR4ANHEfOetbjZRt54FRsYz2blNq08hgRBq-CiV2phJrTo7_ZkrO-mX_foJZgLotRMUBh50pjCTeyxwRydn32TSdf4UoO-tPwx8HtgJqrnZCnXkv1NPDeHqqN1ZjXtizOvFAl9lz22OD1elRvbHET5353t9Alj3VVrVX_1j0N5t0H1I5y97DRyVoB8v5tY3rvpXAJZ4VB8UZ3SOzZnI6LbIE697rQ3rfc3PqVCnr8bbTMdnPfDnVKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fe556e38.mp4?token=TlPb2OymtsBAo9mjxrTX62tw0d3p_ZLZpMXEtsYwpb2UpzUSWsN6xJ61k5myb6W2U-BUeOtkjZJByAF9WSf1GbW0aAY9Q7B6pR4ANHEfOetbjZRt54FRsYz2blNq08hgRBq-CiV2phJrTo7_ZkrO-mX_foJZgLotRMUBh50pjCTeyxwRydn32TSdf4UoO-tPwx8HtgJqrnZCnXkv1NPDeHqqN1ZjXtizOvFAl9lz22OD1elRvbHET5353t9Alj3VVrVX_1j0N5t0H1I5y97DRyVoB8v5tY3rvpXAJZ4VB8UZ3SOzZnI6LbIE697rQ3rfc3PqVCnr8bbTMdnPfDnVKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف با تقلید از ترامپ دم توالت هواپیما
: حاکمیت ملی لبنان بر تمامیت سرزمین خودش انشاله در این گفتگوها به نتیجه نهایی می‌رسد و تا به نتیجه نرسد، رهایشان نخواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/15624" target="_blank">📅 21:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15623">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOf-Nq-xoyFwcYCX3kWzE_JGbxiNmhupVqe-kF8SLKSRfYu-J0Z2z26RUqWPXeH-uAqHwbg2Sh1r94Tzbkt8YZgtMrbWlG_GyVyYPTA9mLJ1cVW3vNcNeaUbKJ67kMm-pLhfjH_6W7CZ-DAHSOBCky8Rjyof0VAA635zut6F28oyz-ze_6My3GxK9kivroijWX6hu5JoSFTqUd2ATN0IHZqI35thLN_cRmqBOB0zHEUR8-BYmehuSa0iSirErGZWR3kMcPVGq7UlYopBt7Rel1KsXC5JAMCcHhD0hqOyBr00uB7Anleet6Xg10MWreYR1G3CBD4LRfsZ0TrQDzjfcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : همه کاملاً آگاه هستند که ایران برای تضمین «صداقت هسته‌ای» در آینده، با بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد. رئیس جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/15623" target="_blank">📅 20:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15622">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شبکه 14 اسرائیل که به نتانیاهو نزدیکه، مدعی شده ایران از یک «سلاح الکترومغناطیسی با فرکانس پایین» برای تأثیر گذاشتن روی تصمیم‌های ترامپ استفاده می‌کنه!
می‌دانم این حرف طوری به نظر می‌رسد که انگار از یک فیلم علمی‌تخیلی آمده، اما واقعاً وجود دارد و همین حالا هم در حال استفاده است , این امواج رو داخل مغز ترامپ فرستادن. رفتار رئیس‌جمهور به‌وضوح تغییر کرده. چیزی شبیه تله‌پاتیه، اما از نوع الکترومغناطیسی.
روسیه این فناوری رو داره، چین هم داره و ایران هم بهش دست پیدا کرده.
باور کنید یا نه، از من خواسته‌اند این کار را انجام دهم و من هم روی آن کار می‌کنم
@withyashar</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/15622" target="_blank">📅 20:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15621">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مرندی: ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی به ایران صورت نگرفت. تبلیغات غربی را نادیده بگیرید
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/15621" target="_blank">📅 20:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15620">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">شاهزاده رضا پهلوی در اکس : در حالی که فیفا تلاش می‌کند پرچم شیر و خورشید را از ورزشگاه‌ها دور نگه دارد، هزاران ایرانی در ورزشگاه سوفای ثابت کردند که نماد واقعی ایران را نمی‌توان ممنوع کرد.
دفتر شاهزاده پهلوی افزود صدای مخالفان جمهوری اسلامی در جام جهانی بیش از هر زمان دیگری شنیده می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/15620" target="_blank">📅 18:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15619">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تکذیب تعهد جدید هسته‌ای از سوی بقائی
سخنگوی وزارت امور خارجه:
تعامل ایران با آژانس بین‌المللی انرژی اتمی طبق روال جاری و منطبق با مصوبات قانونی ادامه می‌یابد.
بنا بر اعلام منابع مطلع، در مذاکرات ۱۸ ساعته دیروز در سوئیس، هیچ مذاکره‌ای درباره پرونده هسته‌ای انجام نشده و تعهد جدیدی از سوی ایران پذیرفته نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/15619" target="_blank">📅 18:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15618">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">طبق اخبار درز کرده این معافیت تحریمی نفت ایران در ازای بازرسی آژانس از تأسیسات هسته‌ای ایرانه.
@withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/15618" target="_blank">📅 18:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15617">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نتانیاهو: تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهیم ماند
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/15617" target="_blank">📅 17:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15616">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده رسماً معافیت تحریم ۶۰ روزه‌ای برای نفت، محصولات پتروشیمی و گاز ایران صادر کرده است
این معافیت اکنون تا ۲۱ اوت معتبر است و ممکن است تا زمانی که مذاکرات ادامه دارد و توافق نهایی حاصل شود، تمدید شود.
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/15616" target="_blank">📅 17:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15615">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDw1c30AeJACZj4sX_qSXMvQwJDB4SE6Botdydgqjs1TV3dCK7YQJvj0HJJ2bjVQjQ2dVFQyJqf2TVqNcl3MuDFVwNxnR_BzZOUQmII1wWISwZ1Vi4xP-J7cjXRVE1RsYNz-REwuLNHXZxqwal68o9c1r-IXLtPFV0ddu9dJp_cazFbuP27ToHWiQzAhybzbypTVFr_zEzZPS8n99-4rvZ_vgC_KSHGkZsCHRJvzR9a-V5CNttAwMBnwZj2LnLVNVYdpkZ-vuDVYnSGqFLeJtCCuTFEkifQv4jalzEXKuFORnIx3x7o9Y7ho-vUf6TBxxdW1i34o3qCdTI_xllbZmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان بمباران توپخانه اسرائیل منطقه المشعع منصوری و منطقه بیوت السیاد در جنوب لبنان را هدف قرار داده است.‌‌
@withyashar</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/15615" target="_blank">📅 17:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15614">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فاکس نیوز: ایران متعهد شده است که به آژانس بین المللی انرژی اتمی و بازرسانش اجازه دهد تا به ایران بازگردند تا بر روی مکان یابی و برچیدن تاسیسات هسته ای کلیدی کار کنند.
معاون رئیس جمهور ونس توانست به چارچوبی دست یابد که از بودجه مسدود شده ایران برای خرید محصولات کشاورزی آمریکا برای ایران استفاده کند و این محصولات شامل سویا، ذرت و گندم آمریکایی است.
@withyashar</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/15614" target="_blank">📅 17:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15613">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">العربیه:وزارت خزانه‌داری آمریکا مجوز عمومی‌ای صادر کرد که اجازه می‌دهد واردات نفت خام ایران به مدت دو ماه انجام شود
@withyashar</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/15613" target="_blank">📅 16:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15612">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">طوفان در راه تهران
سازمان مدیریت بحران: مناطق نیمهٔ جنوبی، غربی، مرکزی و ارتفاعات تهران در معرض وزش بادهای شدید و گاهی بسیار شدید قرار دارند و احتمال وقوع طوفان در این مناطق از اواخر امروز تا روز پنجشنبه بسیار زیاد است.
@withyashar</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/15612" target="_blank">📅 16:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15611">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72fc6efcdb.mp4?token=VXX-pK-e8Uq1MHAk1pwN088Z8QXNJCSxlnBDDRgMtYpULGgIiIc8eUcWMCONMEpYR7b6HYGUv_DEruQlqm4Taylr2vitdrv63VNz1MK2-_NoEWFuqG1QaDCCOiyD0fltMRabbHAhkHcRcV-iOHEQOjwIJkEKfqvcUv3w-ag7sZYCCuMe99GwbLoCzTcD4e9ES7cBuMoRt8lcBqIyvJNtrhOMtSuEAs30qQpH1MBBiUmfDhRy0ksPSF9EdY_rI__A5o_uJSh_mwVwEPW4coVEDWCwz9_bXUTlwBphM4IZPfPlQ052ZgRD_eMdS7m3Ysuqf8Lrbr8JV8fpp6M_ztKhlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72fc6efcdb.mp4?token=VXX-pK-e8Uq1MHAk1pwN088Z8QXNJCSxlnBDDRgMtYpULGgIiIc8eUcWMCONMEpYR7b6HYGUv_DEruQlqm4Taylr2vitdrv63VNz1MK2-_NoEWFuqG1QaDCCOiyD0fltMRabbHAhkHcRcV-iOHEQOjwIJkEKfqvcUv3w-ag7sZYCCuMe99GwbLoCzTcD4e9ES7cBuMoRt8lcBqIyvJNtrhOMtSuEAs30qQpH1MBBiUmfDhRy0ksPSF9EdY_rI__A5o_uJSh_mwVwEPW4coVEDWCwz9_bXUTlwBphM4IZPfPlQ052ZgRD_eMdS7m3Ysuqf8Lrbr8JV8fpp6M_ztKhlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترافیک قابل مشاهده در تنگه هرمز نشان می‌دهد که حداقل ۲۴ کشتی در ۲۴ ساعت گذشته عبور کرده‌اند که همه آنها به جز یک کشتی با استفاده از طرح تفکیک ترافیک ایران قابل مشاهده بودند. به احتمال زیاد تعداد عبور و مرورها بیشتر از آنچه نشان داده شده است ، زیرا بعضی کشتی‌ها سیستم شناسایی خودکار خود را برای عبور خاموش  می کنند
@withyashar</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/15611" target="_blank">📅 16:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15610">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">معاون رئیس جمهور آمریکا ونس: ایران با ورود بازرسان هسته‌ای در این هفته موافقت کرد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/15610" target="_blank">📅 16:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15609">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLDi6UnW8u74sx-GyFl6y5m9rp7H-jG09FZn8n4bJTtWpbDAQYAnUCa4r7ToQRvEgFozUlsXlj7_11se7mExyj4SVQLt039wF344xXC19uBk34JhqFSZeP2V0iasG7fD3V2wzhsn6MGhsWtS0K4Ocz2fOTgG-iVr7R9dhz1saJWcM39DQB7Q-1g4bEGMB_aXDsMGYOJy1zdk-J2qRTUwxq6dGuyVlPOOS8RneSga_PvYoE841BrGVKxEZSlXlAtpXL4-x1TZGIX6eFMHEvGOuZf0IWj0uz47Y-2YBFWTP_rePKQcTOjqMG3Oti3TGpydnHChz_5VM1O7-U2wi5ljAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : یا هر روز به جون هم میفتیم و به هم فحش میدیم و جونیمون میره یا همه باهم متحد میشیم و این وضعیت رو تموم میکنیم
@withyashar</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/15609" target="_blank">📅 15:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15608">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47d6b1d15d.mp4?token=dz5SZbN-1imxK6xofvL0_JiLo8Wl7WanfD_uaY4M2tudpdLkVvlYZyNc39-gHy8G-WQY-GHpFR84CMpf8-SsCD7ToYG8i2ZImULYrsCQ5caPQ9_2e_k_QpcDsA-V0UE-vYdrS1yXotnHw5SD75tUKFlXQkCQ6Zm935tiVAr71g8SdsIOT_ZSPUIYI1FcwJ5a7-mN4YjL6ROa8_iPJDCcVR96cbLtpuo0e7q20kTm-Y70dSiTgsSsyWzqKtvF-YM4mijdLt0ozfjWK3H9Oj7GTAp8ZxhItOc6XvKKnbc1yOOHsQXZAqGbgEPh4_HobpSfhMe1FlCQI0zc1FwfHXubvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47d6b1d15d.mp4?token=dz5SZbN-1imxK6xofvL0_JiLo8Wl7WanfD_uaY4M2tudpdLkVvlYZyNc39-gHy8G-WQY-GHpFR84CMpf8-SsCD7ToYG8i2ZImULYrsCQ5caPQ9_2e_k_QpcDsA-V0UE-vYdrS1yXotnHw5SD75tUKFlXQkCQ6Zm935tiVAr71g8SdsIOT_ZSPUIYI1FcwJ5a7-mN4YjL6ROa8_iPJDCcVR96cbLtpuo0e7q20kTm-Y70dSiTgsSsyWzqKtvF-YM4mijdLt0ozfjWK3H9Oj7GTAp8ZxhItOc6XvKKnbc1yOOHsQXZAqGbgEPh4_HobpSfhMe1FlCQI0zc1FwfHXubvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسایی : یا در مجلس را باز می کنند یا جلوی مجلس جلسه برگزار می کنیم مردمم ببینند
@withyashar
🤣</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/15608" target="_blank">📅 15:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15607">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دوحه: دیدار وزرای خارجه قطر و فرانسه در سوئیس با محوریت مذاکرات ایران و آمریکا
هدف از این گفت‌وگوها دستیابی به راهکار‌هایی برای حل مسائل باقی مانده است
@withyashar</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/15607" target="_blank">📅 15:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15606">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">جی دی ونس: معامله نهایی، خانه است. ما فونداسیون را بنا نهادیم. ما خانه را نساخته‌ایم، اما فونداسیون موفقی بنا نهادیم. @withyashar</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/15606" target="_blank">📅 15:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15605">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">جی‌دی ونس، معاون ترامپ:
اگر پول‌های بلوکه شده ایران رو هم بخوایم آزاد کنیم شرایط رو جوری فراهم میکنیم که کشاورزان و تولید کننده‌های داخلی آمریکا سود کنند و مواد خریداری شده به دست مردم ایران برسه نه تروریست‌ها!
@withyashar</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/15605" target="_blank">📅 15:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15604">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/15604" target="_blank">📅 15:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15603">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">جی دی ونس: معامله نهایی، خانه است. ما فونداسیون را بنا نهادیم. ما خانه را نساخته‌ایم، اما فونداسیون موفقی بنا نهادیم.
@withyashar</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/15603" target="_blank">📅 15:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15602">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس جمهوری ایالات متحده: به آمریکا بازمی‌گردم، اما تیم‌های فنی به کار خود در سوئیس ادامه خواهند داد. پایه‌های لازم برای دستیابی به یک توافق نهایی با ایران را بنا کردیم.
@withyashar</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/15602" target="_blank">📅 15:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15601">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">عضو کمیسیون اقتصادی مجلس :
ملی، صادرات، تجارت و توسعه صادرات که هک شده بودن تا دو هفته دیگه وصل میشن
@withyashar</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/15601" target="_blank">📅 15:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15600">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ونس دوباره تهدید کرد: اگر صلح در منطقه اتفاق نیفتد رئیس جمهور ترامپ همچنان گزینه‌های زیادی در اختیار دارد
@withyashar</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/withyashar/15600" target="_blank">📅 15:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15599">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ونس: به ایرانی‌ها گفتیم که وقتی شما حرف‌های بیخود می‌زنید نمی‌توانید انتظار داشته باشید که رئیس‌جمهور آمریکا پاسخی ندهد
👨‍💻
ایرانی‌ها تهدید کردند که مذاکره را ترک می‌کنند ولی نرفتند و تیم فنی آنها در حال حاضر در حال کار هستند
@withyashar</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/withyashar/15599" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15598">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">جولانی : در صورت دستور ترامپ، ده ها هزار نیرو رزمی متخصص جنگ شهری برای نابودی کامل حزب الله وارد لبنان خواهند شد.
@withyashar</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/15598" target="_blank">📅 14:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15597">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ونس: «باید سازوکاری وجود داشته باشد که اگر حزب‌الله شلیک کرد یا اسرائیل پاسخ داد، ما با هم صحبت کنیم.»
@withyashar</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/withyashar/15597" target="_blank">📅 14:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15596">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">معاون رئیس جمهور آمریکا ونس: ایران با ورود بازرسان هسته‌ای در این هفته موافقت کرد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/withyashar/15596" target="_blank">📅 14:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15595">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نخست وزیر و وزیر امور خارجه قطر به الجزیره گفتند: این یادداشت تفاهم نیازمند تلاش‌های زیادی با شرکای ما در پاکستان، با حمایت منطقه‌ای، بود.
@withyashar</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/withyashar/15595" target="_blank">📅 14:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15594">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">جی دی ونس همکنون در سوئیس :  دیروز روز خیلی خیلی خوبی بود.  ما پیشرفت خیلی خوبی داشتیم.  ما دقیقاً کاری را که می‌خواستیم انجام دهیم، انجام دادیم. @withyashar</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/withyashar/15594" target="_blank">📅 14:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15593">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8ab5474c.mp4?token=qNVCn1PhIX3UeRpf3y-bWwbwwGJ8sScQxCIxirFamaoZ_7MfTcq07ROieqQFaQrhNOPm04oMd0d_vSD2WDldSeDDJYDRMWfll9Z_hnBTFz9MpsZzoYEfClibnUvWeEMgOws7QYL3zHUJtvSAVUU9A0LLre6i1HvZWt9pspDdA17Qs7cyshz87jEWq09BM36pqtwcwAvo1S_cjg6nHEBvJnxxtgQfG2na8g54lnAyXZnWPWQSAkU_l2CuWZOr08Wt2aMC-h7Ezt-e9_X_3ZmhfdVEchwQ0YMSApMwXpdYVIbvfrBpX0U-tEdvM_pw6mTnxrrUTz6N_A2mUT8QkiLCqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8ab5474c.mp4?token=qNVCn1PhIX3UeRpf3y-bWwbwwGJ8sScQxCIxirFamaoZ_7MfTcq07ROieqQFaQrhNOPm04oMd0d_vSD2WDldSeDDJYDRMWfll9Z_hnBTFz9MpsZzoYEfClibnUvWeEMgOws7QYL3zHUJtvSAVUU9A0LLre6i1HvZWt9pspDdA17Qs7cyshz87jEWq09BM36pqtwcwAvo1S_cjg6nHEBvJnxxtgQfG2na8g54lnAyXZnWPWQSAkU_l2CuWZOr08Wt2aMC-h7Ezt-e9_X_3ZmhfdVEchwQ0YMSApMwXpdYVIbvfrBpX0U-tEdvM_pw6mTnxrrUTz6N_A2mUT8QkiLCqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی دی ونس همکنون در سوئیس :
دیروز روز خیلی خیلی خوبی بود.
ما پیشرفت خیلی خوبی داشتیم.
ما دقیقاً کاری را که می‌خواستیم انجام دهیم، انجام دادیم.
@withyashar</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/15593" target="_blank">📅 14:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15592">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ادعای سی‌ان‌ان : اجرای تفاهم‌نامه میان تهران و واشینگتن به مسیر صحیح خود بازگشته و تنگه هرمز برای دریانوردی باز است
@withyashar</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/15592" target="_blank">📅 14:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15591">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وزیر امور خارجه اسرائیل: قصد عقب نشینی از جنوب لبنان را نداریم.
@withyashar</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/15591" target="_blank">📅 14:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15590">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">المیادین:پزشکیان فردا به اسلام آباد می‌رود
@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/15590" target="_blank">📅 14:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15589">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b3269c0c.mp4?token=Nh89I0Q3CV1agRcKSRCHtMoEnL9zOhPL_Ks4PHxjC0q0YqE2z46t6V9w0uqlBMlgskMOC5UyIrqksvGL2eCrg7d2tmKxe8JOYuInYOWp1Cgw8I530OAbByNxbshzqTdig0CHUDIyc_3eC8plll67n4S2ZVzjbrTU6uvezEbps6AvydMbtDyUX4p8XQcWpPqQd8Wnk2BOs_5v4yrPqyNLR88Fdddz88kzEom0vYiSBL0ceve5UK-f23NxS_MC8GMcVbd6-Ly-X_018vehl9yvjrTaIPFUsKiF1gchkYjAxczommo9S1_sNb5PP9cV2tF8WPQJ2xR6GxYdw7QWkUpHrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b3269c0c.mp4?token=Nh89I0Q3CV1agRcKSRCHtMoEnL9zOhPL_Ks4PHxjC0q0YqE2z46t6V9w0uqlBMlgskMOC5UyIrqksvGL2eCrg7d2tmKxe8JOYuInYOWp1Cgw8I530OAbByNxbshzqTdig0CHUDIyc_3eC8plll67n4S2ZVzjbrTU6uvezEbps6AvydMbtDyUX4p8XQcWpPqQd8Wnk2BOs_5v4yrPqyNLR88Fdddz88kzEom0vYiSBL0ceve5UK-f23NxS_MC8GMcVbd6-Ly-X_018vehl9yvjrTaIPFUsKiF1gchkYjAxczommo9S1_sNb5PP9cV2tF8WPQJ2xR6GxYdw7QWkUpHrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">️ بازسازی پل b-1 کرج
@withyashar</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/15589" target="_blank">📅 13:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15588">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">همتی رئیس کل بانک مرکزی: مقرر شد اوفک معافیت تحریم‌های فروش نفت ایران را صادر کند
بر اساس بند ۱۱ تفاهمنامه ایران و امریکا معافیت (Waiver) باید صادر می‌شد که مقرر شد توسط اوفک عملیاتی شود .البته صادرات نفت ما هم اکنون درجریان است ولی از این پس بدون هزینه های جانبی تحریم خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/withyashar/15588" target="_blank">📅 13:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15587">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سی‌ان‌ان، به نقل از یک منبع اسرائیلی: اسرائیل در حال بررسی اعلام عقب‌نشینی نمادین از سرزمین‌های اشغالی خود در جنوب لبنان است.
اعلام عقب‌نشینی نمادین به عنوان بخشی از مذاکرات پیش‌بینی‌شده در این هفته صورت می‌گیرد.
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/15587" target="_blank">📅 13:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15586">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9abae6608.mp4?token=FwK071_42sAzVyOi_21S_4QFNucUL2w08n17V1XBrYS8qP338oOQqclsLHQIaYrRXTZr9dDaEvQoRCkfNgKxxpobVmQOZQASlcYIkIpoCbk-n8S_PThb1Czey14sd78fkOq9HK_IJOzh_5sOozBQW36kKMGtHak9yBK02ZRupokGgHIiZM-X4Rku_Dwr4Tsi1948n-ScWxU6SW44xKRC_c0l58h7o1OP6h2J7F0kHhSJCl5FL62w3PcASg6UmDyt0-KqRKgJjEHIj42Tl5501UTXiQJiRp3pI02odL_jN2dX7GWUEhl22Oyz66LjdonDPvxGMcf2GZhUus9HhTnyWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9abae6608.mp4?token=FwK071_42sAzVyOi_21S_4QFNucUL2w08n17V1XBrYS8qP338oOQqclsLHQIaYrRXTZr9dDaEvQoRCkfNgKxxpobVmQOZQASlcYIkIpoCbk-n8S_PThb1Czey14sd78fkOq9HK_IJOzh_5sOozBQW36kKMGtHak9yBK02ZRupokGgHIiZM-X4Rku_Dwr4Tsi1948n-ScWxU6SW44xKRC_c0l58h7o1OP6h2J7F0kHhSJCl5FL62w3PcASg6UmDyt0-KqRKgJjEHIj42Tl5501UTXiQJiRp3pI02odL_jN2dX7GWUEhl22Oyz66LjdonDPvxGMcf2GZhUus9HhTnyWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مجلس شورای اسلامی
@withyashar</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/15586" target="_blank">📅 13:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15585">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ایتا رو زدن
پیامرسان «ایتا» دقایقی پیش از دسترس خارج شده است.
@withyashar</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/15585" target="_blank">📅 12:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15584">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-x7kzefvLmSgXIYd0CaXB3h6Zu676rL_DSQW2JaZed4dOi1piPmAqdTBOC1h-TTEkbDwdP2V9K0ZCSLkurOTxeVQgKYLNUflRfpv5FjtjQltKWPZEFhc8qhwT6EoCp_sJBec-YyP5uKLkvP9W-jPUZYAUtMZK5ZzaXXr9DFvKr4tjhnMa2dIrpxXLka4bTHRf4Ef-yZTspd64V3UND6WNJBKAAcoGrk0KuXYEBwQPF10wtIECSu9I7m5UEETWY7AiyKZ6kj8qCGpYgU0iXO7fujwSwTpyg8uoLrLsyuSj-juCTTtG7V98Zlf20SME6F46Gs2pqSeL9ovruPLODDtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاظم غریب‌آبادی دیپلمات ارشد جمهوری اسلامی و از چهره‌های شناخته‌شده پرونده هسته‌ای ایران است. او اهل علی آباد گلستان است و در سال‌های گذشته سفیر ایران در هلند، نماینده ایران در آژانس بین‌المللی انرژی اتمی در وین، معاون بین‌الملل قوه قضائیه و دبیر ستاد حقوق بشر بوده است. اکنون معاون حقوقی و بین‌الملل وزارت امور خارجه و از اعضای اصلی تیم‌های مذاکره و پیگیری پرونده‌های بین‌المللی ایران است. لقب «کاظم دستکج» را کاربران فضای مجازی پس از انتشار ویدئویی از او در یک نشست بین‌المللی رویش گذاشتند؛ در آن ویدئو گفته می‌شد خودنویسی را از روی میز برداشته است، این ماجرا به یک شوخی و کنایه سیاسی در شبکه‌های اجتماعی تبدیل شده
@withyashar</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/15584" target="_blank">📅 12:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15583">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2qpVPKvEpmgKbBkEb0oUvEE_Oai4pVD1zwqhU2GqkOeiG4HI2KHNcYXGEMlXawp9oFlEZ3tZAKZfFYs6KvL5hvYD_SUiQBpNJ9gpZysQEt9OADFYix55OutqcVetOdw2C2_txXRjKr4Q7khL2j1fdgUrWwgEBN8ODS6lJDTDSeLrVQB9LnYHDyJXu6RVTfw1dJKV9CG1XqNUKJgj3LLfWOMGbFZPvoknqUZ5cODe_AamcH3WTkhpXa-n9_U4WXh6HT3BcD_v0Hy5U5BFUkUkU8qwKfnYnQMa7ryrysW6k3wCt57_3A3sN81FvbKwsZXbX3ufc9ZaviMO81AlIcevQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای هیئت جمهوری اسلامی (همه بجز کاظم دست کج) زوریخ را به مقصد تهران ترک کرد
@withyashar</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/15583" target="_blank">📅 12:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15582">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bd0c99669.mp4?token=m0ErSOG9auZx5-ED4Gfp744P10MoG-C_6-1KOUhu-yvpGoIxcrLrrOguuZV_UhQusHRa5OZQ8FBlFyFtTp6_coMLzbMbwQmpLFrwCURJuFjFTUEcQv7FmNGS4Pn4fSswxAELQjDbC65paQtEfHLFr4OzRiWV26GJtImMURMmcQZVA8MSuhw_VE5TYOz2Nm5MSsZcI-WZntbqxXEtq3wPVUYxpQPj89fVjUwdumOir27gGO8B9ZawSk1mQqU6LDm0YWSyvylcUDWg5izdBHbicPUhLeJH23CJoz57YAMpd-IgB29VGEvIe8Mv-tL7AUv7XlOtmynH3ZyDPmfZtEBLCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bd0c99669.mp4?token=m0ErSOG9auZx5-ED4Gfp744P10MoG-C_6-1KOUhu-yvpGoIxcrLrrOguuZV_UhQusHRa5OZQ8FBlFyFtTp6_coMLzbMbwQmpLFrwCURJuFjFTUEcQv7FmNGS4Pn4fSswxAELQjDbC65paQtEfHLFr4OzRiWV26GJtImMURMmcQZVA8MSuhw_VE5TYOz2Nm5MSsZcI-WZntbqxXEtq3wPVUYxpQPj89fVjUwdumOir27gGO8B9ZawSk1mQqU6LDm0YWSyvylcUDWg5izdBHbicPUhLeJH23CJoz57YAMpd-IgB29VGEvIe8Mv-tL7AUv7XlOtmynH3ZyDPmfZtEBLCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیر استارمر از سمت نخست وزیری استعفا داد
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/15582" target="_blank">📅 12:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15581">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خبرنگار الجزیره: یادداشت تفاهمی بین ایران و قطر در مورد اجرای آزادسازی دارایی‌های مسدود شده ایران امضا شد.
وزارت خزانه‌داری ایالات متحده (OFAC) معافیت‌هایی را برای نفت و پتروشیمی به مدت ۶۰ روز صادر کرد.
@withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/15581" target="_blank">📅 12:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15580">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وزیر اقتصاد جمهوری اسلامی : آزادسازی پول های بلوکه شده آغاز شده و بانک مرکزی اقدامات لازم رو برای دریافت پول فراهم کرده
@withyashar</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/withyashar/15580" target="_blank">📅 12:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15579">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">@withyashar
وضعیت</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/15579" target="_blank">📅 11:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15578">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA GH</strong></div>
<div class="tg-text">دارند مین‌های دریایی خنسا میکنم آمریکایی هاااا</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/15578" target="_blank">📅 11:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15577">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS H A Y A N</strong></div>
<div class="tg-text">الان یکی دیگه اومد دوباره پسر
بزن بزنه فکر کنم</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/15577" target="_blank">📅 11:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15576">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اتاق جنگ با شما : دو بار صدا اومد
از تو تنگه بود ، بگو کنترل شده تو آب نیست ، یه خبری شده حتما
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/15576" target="_blank">📅 11:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15575">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حتما تنگه باز دعوا شده
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/15575" target="_blank">📅 11:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15574">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">صدای انفجار در قشم و بندر عباس شنیده شد
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/15574" target="_blank">📅 11:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15573">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPDmIT40KGxIuEufr0TZUuwKsBkJvxNYu2TA7El95eS31ukYxbpmsUdmePfJtk02zEgmNHFS62qU-cpSj5n5t1KMVpMWKKbU0nyjni7kHwTyEjhAMrUV4XBhh-wSMg0VUB0GzsWKajIWc4aurf6MTcr9S-PZqP906U6dEfS4-WuvR9n1O6jrUrvifcoW05iXYmi79Opg8WwsTx8EVkyCX1qDitIaWZQTCqLRlbqjQiCLEpSC7Vsborl5lMsONfqdGkjtFZAcZsxX8Nq6EwGJh-NHtRLHjXJJRDNCECh5DaSmYFVWmIu1Xw8sbg0J-ujF6wZmXkvlcemZ1uJgqrfw1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای هشدار زودهنگام و جاسوسی E3A با رادار آواکس ناتو دوباره در ترکیه بلند شده. این هواپیما طبق الگوی منظم همیشه قبل از اتفاقات مهم برمیخیزد. قبل از ترور قاسم سلیمانی، قبل از جنگ دوازده روزه، قبل از جنگ چهل روزه و حالا دوباره پیدایش شده. معمولاً حدود دوازده تا بیست و پنج روز قبل از حمله اصلی، جنگ حتمی است.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/15573" target="_blank">📅 11:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15572">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">باراک راوید خبرنگار آکسیوس: مقامات ایرانی هنوز نرفتن و مذاکرات همچنان ادامه داره. @withyashar یاشار : این باراک درست نمیشناسه اون که مونده کاظم دست کجه
😂
صبر کرده همه برن سالن رو خالی کنه</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/15572" target="_blank">📅 11:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15571">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آنچه در سوئیس گذشت، به نقل از یک منبع نزدیک به تیم مذاکره کننده ایرانی
یک منبع نزدیک به تیم مذاکره کننده ایرانی:
مذاکرات هیات اصلی ایران در سوئیس پایان یافته است، با این حال کارشناسان همچنان در سوئیس هستند و روند اجرای تفاهمنامه را پیگیری می‌کنند.
تا این لحظه مذاکراتی درباره هسته‌ای صورت نگرفته و ایران منتظر تحقق بند 13 است. تا زمانی که بند 13 محقق نشود، در واقع زمان آغاز مذاکرات هسته‌ای فرانرسیده است.
@withyashar</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/15571" target="_blank">📅 11:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15570">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">هیئت مذاکره کننده جمهوری اسلامی، بعداز 18 ساعت مذاکره، سوئیس رو به مقصد تهران ترک کردن.
@withyashar</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/15570" target="_blank">📅 11:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15569">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P99vtX58iz2NuLst3j6S9TohJCDb3JQh2aDjQUCAa_SgEmzyllrWlYFkwyzrjZ2xjX8lNKfY7mFNtxC_MJdy_Mo8zm5hinFRz8XR6o9n-HklpTDBrz9DYZzRBUzlGPwvYUiTWi_Hqhy_dkr3qshtlF6PYPgWPEbCIV_ARHqU3QvENZKOouvrFuZnxvyhncrhCXA04rjnRHweqhjs9X85qEZ5I6ZrHoS86uDti3b3-xLkxm1IiVWkEWrKSQbTxH9maGz4H_Dlzf14cIdQi9udYcqjeIuxmsu_CrIxWJmMAv01J9rOhDHWnBL5iH6iTMIbkHZFOPMPpejPk4WO6UAfuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکسی عجیبی که نخست وزیر قطر، محمد بن عبدالرحمن بن جاسم آل ثانی بدون دقت، در کنار جی دی ونس، معاون رئیس جمهور ایالات متحده، و جرد کوشنر، داماد رئیس جمهور ترامپ، منتشر کرده است
@withyashar
یاشار : اما چرا جی دی ونس از یک کارت هوشمند امنیتی وزارت دفاع آمریکا CAC با هویت یک زن که  مسلما سطح دسترسی امنیتی و سازمانی متفاوتی دارد استفاده می‌کند؟</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/15569" target="_blank">📅 11:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15568">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خبرنگار آکسیوس: عراقچی نوشت ایران معافیت‌هایی برای صادرات نفت و محصولات پتروشیمی دریافت کرده و برخی از دارایی‌های مسدود شده آزاد شده‌اند.
مقامات آمریکایی این موضوع را تأیید نکرده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/15568" target="_blank">📅 10:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15567">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خبرنگار آسوشیتدپرس گزارش داد، میانجیگران می‌گویند مذاکرات سطح بالای ایران و آمریکا در سوئیس به پایان رسیده است؛ مذاکرات فنی برای دستیابی به توافق نهایی جنگ ایران ادامه خواهد یافت.
همچنين این خبرنگار به نقل از وزیر خارجه ایران اعلام کرد «میانجیگری پاکستان و قطر پیشرفت بزرگی برای پایان دادن به جنگ لبنان به همراه داشته است.»
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/15567" target="_blank">📅 10:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15566">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تانکر ترکرز : ایران از پانزدهم ژوئن سال ۲۰۲۶، بالغ بر ۳۶ میلیون بشکه نفت خام صادر کرده است همچنین معادل همین میزان  به صورت محموله‌های شناور در نفتکش‌های مستقر در آب‌های سرزمینی ایران ذخیره شده است
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/15566" target="_blank">📅 10:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15565">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHS1Z4s5xJPxDgUUh5aQMx2GmY6sj2gKQaLNqlFhXvyBEk0byRQNhpyteI2_h4c-DjiMNrKRTZX8yiulWATh32JsmItMrq1U6Gk4seQvpbENQNC9UfXP0WJ4aR9IEoZZDTWEjbDzDZ9Pgf8rGHQ7UYud3_z_e37RIDuRKI9OFkV5rWVb8v2SWTDbAlBLP_LlTAUigwZZaxg8ZebdwnwwUJI8qnyHJ97UHT5H29dTqSUS7Fe_TX99WuA9-GZCmCUlWWfumt_5tsanihTq-vsrBHL4yzRjoi5B2J4VaoeAhKal9iH8Mr0uCnSpRd0ckN5LEfgzPCq3hLI_X1tYuCBm9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران دیشب رکورد پیرترین ترکیب تاریخ جام های جهانی رو با ۳۲ سال ۱۹۱ روز شکست.
رکورد تا قبل از این دست آلمان در جام جهانی ۱۹۹۸ بود.
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/15565" target="_blank">📅 10:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15564">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سناتور گراهام: به لبنان و مردم لبنان می‌گویم "کمک در راه است."
حزب‌الله مدت زیادی کشور شما را به وحشت انداخته و تحت فشار قرار داده است. این وضعیت در آستانه پایان یافتن است.
@withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/15564" target="_blank">📅 09:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15563">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وزارت کشور قطر:
در انفجار یکی از کارخانه‌های منطقه صنعتی «رأس لفان»، ۵۴ نفر مصدوم و ۱۸ تن مفقود شدند.
این حادثه ناشی از یک نقص فنی در حین عملیات بهره‌برداری بوده.
هیچ‌گونه نشت مواد که خطری برای سلامت افراد داشته باشد، رخ نداده
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/15563" target="_blank">📅 08:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15562">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRyz9aXzy-nMmSatG9MK6A91Swwuf-HBsMFubjJPIa1TafBmL9pXZ_klAbcN1EqYSY1YfnST-TyBqIJF16Sx4Ff9GjvLDlEptVPhoO0tMkjuPjPxZhuwGqiCsQjbyQ7xsRkBWLIgay-c7MuJstbJcajOXs9rjDm0pWaojt8q51VMN0icwDFfU8tqN_AWjFRg8VKbQPtKQQ8S7zJsBidtoedFbtCKuI4yqjXRwWa6mNRe4fzFmgu9aEzO2DmzgUPuS2B_s6Xrk3x01Ht1jFqQPLbe21zJdIxB96SVPrIo7KyH6Cdayxg38qqgc7q3gve_PZ47zCJkdmOH4DC7pgYfIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نحوه پوشش اخبار نیویورک‌تایمزِ فاسد و در حال فروپاشی درباره ایرانِ بسیار آسیب‌خورده و فلج‌شده، از طریق «حقایق» جعلی و ساختگی، به باور من «جنایت علیه کشور» است. من تمام گزارش‌های کذب و بی‌معنی آن‌ها را به شکایت چند میلیارد دلاری خودم علیه آن‌ها اضافه خواهم کرد. آن‌ها مجرم هستند! رئیس‌جمهور DJT
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/15562" target="_blank">📅 02:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15561">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗮𝗯𝗼𝗹𝗳𝗮𝘇𝗹</strong></div>
<div class="tg-text">درود عمو یاشار یه سوال ناراحت کننده و کلی داشتم چرا انقدر کشور ما خیانت کار زیاد داشته تو کل تاریخش</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/15561" target="_blank">📅 01:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15560">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9800d55ebe.mp4?token=YBcwWW_uj9y1D3aQ0V9ZoumHPevwuAmKG-bLjiwKwZhkmKaX3VElBUGNtJfg3hgGnynXsD87DFU_JXIMaQNk5XTAhrm2spAiXZk1hTaLEafwiWpd_xhM7UY2cNGdtixrbZFEp_hsJlRn02fJ8UWzyZYJMEVzRM74hIoj9FrYrz6pHE1Mcd3A0LQWM78T2Ct-3RFYpQKfYmKx6ll3M0ug4L4PNdgsi0w2pl9MMCj3HE_iwtA9l7ZfdAh2-tW-MgO1RFg1vgpRiF6rvDLfiQLYw9KyToZfePlIfw7CRapX_3hV2m9y-Udj79MKKCHLe9CytWme4hcxsItvCQJK61fSVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9800d55ebe.mp4?token=YBcwWW_uj9y1D3aQ0V9ZoumHPevwuAmKG-bLjiwKwZhkmKaX3VElBUGNtJfg3hgGnynXsD87DFU_JXIMaQNk5XTAhrm2spAiXZk1hTaLEafwiWpd_xhM7UY2cNGdtixrbZFEp_hsJlRn02fJ8UWzyZYJMEVzRM74hIoj9FrYrz6pHE1Mcd3A0LQWM78T2Ct-3RFYpQKfYmKx6ll3M0ug4L4PNdgsi0w2pl9MMCj3HE_iwtA9l7ZfdAh2-tW-MgO1RFg1vgpRiF6rvDLfiQLYw9KyToZfePlIfw7CRapX_3hV2m9y-Udj79MKKCHLe9CytWme4hcxsItvCQJK61fSVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیگه مشخصه من چی بگم !
🍑
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/15560" target="_blank">📅 01:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15559">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0f4odg7-ogJbhpz-oSgwqGBc1wheaquQ9F6lNTdTC_jg-CfuUok6d7wlrv-yLUsIovbSOwBycT9HiQAflQC-_PVSA7-P_qNtOi4Wr0ArucSwzJxASqPKuiuWaQVORKO81uwjipUcMcN2uQTqI1Xw4543a36qz7xTD5jzr8VZrRTL9QFJlSwWv1r_sKSXSAIlbfL488NtFEltxrK7Qr_NBjOro7aShfDL-QojC-9_71XiBdZyArxvHEkKuSOnvmv01zaG8KvQbD5z6Zql9imwuvMxTIDeGQUo1F4XPGbRP6TMHB-A3y4-hhKyH43xz8fTrnN_mhHPv6g0SN2kflS6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از زلاتان پرسیدن نظرت راجع به بازی ایران و بلژیک چیه؟ گفت:
نیمه اول نزدیک بود بخوابم
نیمه دوم واقعاً خوابیدم
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/15559" target="_blank">📅 01:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15558">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خب مجوز عبور کشتی های بلژیک صادر شد
🤣
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/15558" target="_blank">📅 00:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15557">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پایان بازی و مساوی در‌جام جهانی مساوی ها
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/15557" target="_blank">📅 00:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15556">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYAMA_1MgnHzQLt53a7XMHYbu_IghG9fFkpQzL9Yk3cOsNVE_tTjt8hoFgOlPbtTD0lK-_JI5DVH_CVLS0hHEvjromb5EKE-EAQsP8Su9He2UhnVrNgeIhVRVC5j9gtEGSRp9ZqQRtT5z4MoOipByIKGtDrNk8FamFmZ58UC0AhiGAF-63scCS8pgGOwgPZsoa27XngRXGEH02fyPMW6y0XUnimK3IM7DxK-TFt-MfpG1s__kMgkM9fD4CHzFkIFgWnffR0y19Xo4xnm4yoU2IzgeyWAaUBy_1CunNopXrJTjBvZPYbx7SH0w_bYt0R-SGvjWRu_r-sDuOQ5nzc6pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عنوان خبرها در نیویورک‌تایمزِ فاسد و در حال فروپاشی: «پس از تقریباً ۴ ماه جنگ چه چیزی تغییر کرد؟ تحلیلگران می‌گویند تقریباً هیچ.» واقعاً؟ نیروی نظامی آن‌ها نابود شده، نیروی دریایی آن‌ها از بین رفته، نیروی هوایی آن‌ها نابود شده، پلتفرم‌های پرتاب، موشک‌ها، پهپادها و تولید همین‌ها، تقریباً کاملاً از بین رفته‌اند، دو گروه برتر از رهبران آن‌ها از بین رفته‌اند، تورم آن‌ها به ۲۵۰٪ رسیده، اقتصاد آن‌ها شکسته شده، سربازان آن‌ها مزد خود را دریافت نمی‌کنند، تنگه هرمز باز است، نفت به شدت در جریان است، و بازار سهام و اشتغال آمریکا در اوج رکورد قرار دارد. این چیزی است که تغییر کرده، شما سگ‌های فاسد و غیراخلاقی، و بیشتر از این هم!!!
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/15556" target="_blank">📅 00:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15555">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آکسیوس از قول یک دیپلمات آمریکایی:
مذاکرات بین تیم‌های فنی ادامه خواهد یافت و آنها احتمالاً برای ادامه کار خود در سوئیس باقی خواهند ماند.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/15555" target="_blank">📅 00:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15554">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بلژیک
❌
موزامبیک
✅
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/15554" target="_blank">📅 00:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15553">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یکی از بازیکنان بلژیک کارت قرمز گرفت درنتیجه باید ده نفره بازی را ادامه بدهند
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/15553" target="_blank">📅 00:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15552">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcfc7af55.mp4?token=V8Pny7ARmMUeKguGz2T2jmyOKlbcXmgm1w5Ea5ej074v5W58mo0Nx_eBNKxTgcvMFA9CLjdnbOEIhH0yCKryoTHqwhpupISZ2BmzH1lz1g3P1BQtU-9zpNLiKHDCaPKeezUymuyY63e8EvfEynIEEGQZr-1UmequA_IVRbkKZhBu0g-V_pV2kc2aiGKh_jF-AgvuoXang3BDjKF2IpRZ3ccqlStpQld7it9bIF65gVA09hyixnkL2r0BsGGg6x-m3zLLYizOPbX414ASla1FUuhZ7C9XnGUJvckA2-uws8FZb0YTM4SzlES5OeyYjovaPiuBvbehrt-S5xt2ZuTbZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcfc7af55.mp4?token=V8Pny7ARmMUeKguGz2T2jmyOKlbcXmgm1w5Ea5ej074v5W58mo0Nx_eBNKxTgcvMFA9CLjdnbOEIhH0yCKryoTHqwhpupISZ2BmzH1lz1g3P1BQtU-9zpNLiKHDCaPKeezUymuyY63e8EvfEynIEEGQZr-1UmequA_IVRbkKZhBu0g-V_pV2kc2aiGKh_jF-AgvuoXang3BDjKF2IpRZ3ccqlStpQld7it9bIF65gVA09hyixnkL2r0BsGGg6x-m3zLLYizOPbX414ASla1FUuhZ7C9XnGUJvckA2-uws8FZb0YTM4SzlES5OeyYjovaPiuBvbehrt-S5xt2ZuTbZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرس تی وی: هیئت ایرانی پس از پایان یافتن مذاکرات چهارجانبه، محل مذاکرات را ترک کرد
یاشار : این ویدیو نزدیک به ساعت یازده شب تهران در زوریخ سوئیس گرفته شده، در نتیجه نشان می‌دهد که تیم در همان زمان محل مذاکرات را ترک کرد و دیگر ادامه نداد.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/15552" target="_blank">📅 23:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15551">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cb0602203.mp4?token=XJZDV7e6sqk9Y7n4fiOyPeo7x5axHkrUoE5E5xMfhfQ4iyYrkB5_3MNftpOLxGFQKZa4orhpWw9U9USvUJLt_9STi2tqW94SxwPnf0QQ_xpx_ioVhSIgKbO0dOZPlDDXP25sN1tWzl97tFwv8pO9Hysv3qsy1isCOl-UZCg5111OcgFG2OAxto73Pf-d5ctpqpK09GOt-kKQoxC9XwTM4K0UXl63jJQfna90w-tSYID8iz1SYN-_oPiKbca3g8XW1RdO3rt6rOPjFK_wk8WSTr9dFrC2PLCvBw53m-Xpw6_3wUFNhvgiYiP5agZO-ZmlXlcVqzwZUwiePYdzF4MVGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cb0602203.mp4?token=XJZDV7e6sqk9Y7n4fiOyPeo7x5axHkrUoE5E5xMfhfQ4iyYrkB5_3MNftpOLxGFQKZa4orhpWw9U9USvUJLt_9STi2tqW94SxwPnf0QQ_xpx_ioVhSIgKbO0dOZPlDDXP25sN1tWzl97tFwv8pO9Hysv3qsy1isCOl-UZCg5111OcgFG2OAxto73Pf-d5ctpqpK09GOt-kKQoxC9XwTM4K0UXl63jJQfna90w-tSYID8iz1SYN-_oPiKbca3g8XW1RdO3rt6rOPjFK_wk8WSTr9dFrC2PLCvBw53m-Xpw6_3wUFNhvgiYiP5agZO-ZmlXlcVqzwZUwiePYdzF4MVGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که شروع انفجار را نشان می‌دهد، در این ویدیو می‌توانید صدای شخصی را بشنوید که در مورد محل انفجار می‌پرسد و سپس با «لوسیل؟» پاسخ داده می‌شود، لوسیل در ۷۰ کیلومتری رأس لفان قرار دارد.
@withyashar</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/15551" target="_blank">📅 23:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15550">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkOLrCy59nYB_HbefVMPGvgT8f3kM0ctdSPWaQC-Zqv1OPyuxOJxL_FkWteZBnKPcdET7RVRTxoD5Y8KsLVRv_QKuXWH1IWYBf3Tc4oCWALKjzLx8bjjArc8cM0miCxsWfluGYHDmHlUjaCSKkSoXdxVyJNPhcv1gyv8hUiIGe-3h_6vdoqQJBNUU12WdMyWuIcjgefTO0QfDhGeKwQyb4Z2KxP_ZJpo8VtYsdRJNg1xExBY1WqAj3c2_lq7hFTWj8w1sMTUozhGlJ9v1aajuD5BxO-MUFVsD3Ig_G8iTUccvlkfJJZ55-fE8pcmFk5Zut1sOcQmWqV7fasFGJNA6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ایتالیا و نخست وزیرش پس از صرف تریلیون‌ها دلار برای ناتو، حتی فکرش را هم نمی‌کنند که درگیر جمهوری اسلامی ایران و تهدید هسته‌ای بسیار جدی آنها شوند. دهه‌هاست که ما از آنها دفاع می‌کنیم، اما وقتی مورد آزمایش قرار می‌گیرند، آنها آنجا نیستند تا از ما و بقیه جهان دفاع کنند. خوب نیست!
@withyashar</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/15550" target="_blank">📅 23:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15549">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMzgjMVTtPKDkNPLQJeI61Rkz6ODOQY9CHdhwfsp2Clwc2R9haoQcz0ox5zm4e9etx39jJSnMiFVH1maI8LSsWzS_s6kw6mtolA6RjVqeE_TEbLeHUybfCQZYSYNvoHlzA9yGWq2gn6eE_f4ixir9sOPRvVbjBZ2wbuO5Unp5T3-5PZIDBDBiASsRzK0pT-X1Khc-5IN8W3aQ7zAngHdsX5iAfOSTzDdjJhSVy7yV1vn_ZJeT2dN52LgB56NUUIaN38tIJMr58UnIyQvwMu4g6-rpxyNQu4YSAtH-8wsDOOYmGi-jlOYtmRtrnPjrKGpnOvW8kHDiKjxCxe6OFkwzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتشسوزی عظیمی در مجتمع گازی راس الفان، در حومه دوحه، پایتخت قطر، رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/15549" target="_blank">📅 23:26 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
