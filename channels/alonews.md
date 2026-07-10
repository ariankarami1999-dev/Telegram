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
<img src="https://cdn4.telesco.pe/file/t-ntRuMLm1TDik2h166rImzeEhnqVseHb8kNpeQG2Tqsf22YWyOZhmSBGMzBoTRtTDMAE3nJY0uxRP2XctEDIO5MCrCiZEwK5vFLh4isulif_Hh_bh-tynZirV-RFhe8rKljUNi7yJgmTyrsCG0ruO4ImiSgB-zVUWrfCYu_5jmcdfHrZqPwKeU2OSVJ1_DVHR-ICDt9ROO56XVQr27h9haOAIhlt_5rU3v44OEXtSn7r5iLqgwfo58uJQiB9ywpEWFyjQQc_VFVRGqg472E6qnWMwVurAXsv_SeQiCK4g1nF_TOXs32gDpKS7eod2vsIj03qKJ1aiXs9JMTBAjcjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 924K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 13:54:21</div>
<hr>

<div class="tg-post" id="msg-133027">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
عملیات دریایی بریتانیا: سطح تهدید امنیتی دریایی در تنگه هرمز همچنان در بالاترین سطح خود قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/alonews/133027" target="_blank">📅 13:53 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133026">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
کاخ کرملین اعلام کرد که ولادیمیر پوتین، رئیس‌جمهور روسیه، تا کنون با دونالد ترامپ، رئیس‌جمهور ایالات متحده، تماس نگرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/alonews/133026" target="_blank">📅 13:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133025">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ga3QA03utp3wEzBuKJJz35U5zU8XepPKXy2s9hpA4TbisVDnbY7IKoXF_xlRndO9PpxomwlugSIm8xbtYZsocYy2Qtdq8xwL8dvB_1riidJ3heIHjVmDYqaoYgAYsLdatGKOejcLF8k4PsTs7YRe7szkp5QyvWpM77MJhF_xH0jKDItLRpRAxpNhQWdUBVQe12QcEl03STUp1KXUb5HGvKs5Y9FOis3R0tKqqe4E37VPQtIqYZmrri-YpDJ8cb9FKgrNfgG3PUkxgmKDdL85KKqMd8V2x55MLuV30fyl95IRJtJp8hHcXh2QCxJKjXX621ln_9AA680CNV3G7R5ugw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قائم پناه، معاون پزشکیان: بعضی مداح‌ها یه میکروفون بهشون رسیده هرچی دلشون میخواد میگن
🔴
اونا هیچی نیستن اما جو گرفتشون و فکر میکنن تئوریسین دین و سیاستن
#مداح_بیسواد
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/133025" target="_blank">📅 13:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133024">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
گویا فرمانده نیروی دریایی سپاه به دلیل حملات به کشتی‌ها، توسط شورای عالی امنیت ملی توبیخ شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/133024" target="_blank">📅 13:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133022">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
فوری/اکسیوس:  ایران و آمریکا از طریق میانجی‌ها توافق کردن فعلاً به همدیگه حمله نکنن و برای حل اختلاف‌هاشون، به‌خصوص درباره تنگه هرمز، دوباره پای میز مذاکره برن
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/133022" target="_blank">📅 13:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133021">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJLgv2v4kK2LHl-ysYZANQXKQfb-83YgkKCu9LerQtBbd_Ny_lKcdf3q5CQ6GrLqYGTTI5gBHrJM6ytajk1mQNRi3SC6NgpK2cyB1R16ztfDv7AdinXklJsA8JMTiw9o4b3f0SNAKIIiJgD0W3YpC9XU_hyJFhyciLCpoG_HcaY77_pDfspzkx3nNkkpO9nQ0_NuKq3JoNl81C_zTvB4UCa6j1-Ow_zmDRAGW4GuRGkWinU6N_vtMsZhTQHnv51QmGbXG1qE5uQ_L1u0JwfpEct4XlRuqDn7PJ9fU9vSIGQGH4IgjEpKqhYhKFKHDM2pt_wGIfeN7JR-0WAoAdxuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: یه انتقام مشتی از ترامپ تو راهه
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/alonews/133021" target="_blank">📅 13:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133020">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
مدیرکل هواشناسی خوزستان گفت: تا پایان هفته آینده روند افزایش دما در استان پیش‌بینی می‌شود به‌طوری که از روز دوشنبه وقوع دماهای ۴۹ درجه و بالاتر در اغلب نقاط استان مورد انتظار است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/alonews/133020" target="_blank">📅 13:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133019">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
فرمانده ناو هواپیمابر «لینکلن» در دریای عرب به خدمه خود دستور داده است که آمادگی خود را حفظ کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/alonews/133019" target="_blank">📅 13:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133018">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eULMZy23s3cp71tk6MUBuXF6kZCuneMH-Sez22iNj-kLCez97bW7KBnlp5oZycqrgWE3byjKWm2Hx_sspaJyIln4lYLrzGbqI5xYy31G_CXVhhTFqTxTNA0H7kKcph1kytWeGACZh-S1ctcRLbtF6B60Liapt5X_IjgQiyy3CVXwMN9g2wUD9zws4_M2m8aIsrQuIewKqP3Yjjc1iYf12GEKm13YuBp9ZG2Hewiq5v9zg9r2aPPOpg7klvenkiLuaHjpArzQTZ4g2dalCC1Bn2J4SgIlkGW8xGiUCy733zTvhQmNJBJPgDsWX_82Fi33muclxIku8A7LGIU-Y-aBrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بابک زنجانی: در خصوص (راه آهن) آق قلا حرف و حدیث‌هایی از خرابکاری به جای حمله دشمن البته وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/133018" target="_blank">📅 13:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133016">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d5ace0db3.mp4?token=c3cM215dLMDCOs8Sh4wzCt3P1H-4fSJwmGnq7uhvq3M5AsCmNIUuv_FtPW2qmK1OErv68GqrMdrUpbtIYX7LHamPdKlgn8oEuBZnkk1mqvA4boAyhlSFJt3HlYvUGkpYBfefnp38jRFMWXN-VEu6fXJShdf2zgUAvOwbF11DaIKc5lkS_h8M6yGwuxIJzEbRUDQ3raGPa9Pu4Az8H5jHLd31OgYdU3D3C1cyJ-t97DgTG-D3BrbITTNctYjRKD0zaqHgfphAn694Y9eKusj3VxxdNTNwJbeWPgCmfc2MUSDBSIPqfwhBAs_9pi_rG1ykWpc5tLYxJ0URgY3H-sD8rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d5ace0db3.mp4?token=c3cM215dLMDCOs8Sh4wzCt3P1H-4fSJwmGnq7uhvq3M5AsCmNIUuv_FtPW2qmK1OErv68GqrMdrUpbtIYX7LHamPdKlgn8oEuBZnkk1mqvA4boAyhlSFJt3HlYvUGkpYBfefnp38jRFMWXN-VEu6fXJShdf2zgUAvOwbF11DaIKc5lkS_h8M6yGwuxIJzEbRUDQ3raGPa9Pu4Az8H5jHLd31OgYdU3D3C1cyJ-t97DgTG-D3BrbITTNctYjRKD0zaqHgfphAn694Y9eKusj3VxxdNTNwJbeWPgCmfc2MUSDBSIPqfwhBAs_9pi_rG1ykWpc5tLYxJ0URgY3H-sD8rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی در کارخانه کفش چین دست‌کم ۲۸ کشته بر جای گذاشت
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/133016" target="_blank">📅 13:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133015">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aa971ff94.mp4?token=k6-powcpr1ao2HvCO6LzKDhlHZCKuWmq4TRNfscxQv_p338j-j7AemqGjOkLk1sXwxjVsT5q8Xvi95fPErS9o6jVe0SvZBOcp_XwyQHcz2H50JT0nX_D4CSgQCWfOFh6OEBKdIdb7yLOgS2EdW3OTPswHGr8hM-_4N0z6Gfu9lZihfMx-bQGtaDgSdKpqCOUFROivY66EkmSo75b8Q_5j9yXNpTVe_76Y7NfyYCXht2q95Wq0-DkyM3eV3q1DItaZlXsplUwaBKz8D_Pigr5LvLRkMX0kGW4_r4dIbMltj0rY5b7JS0qq29pT6Q8HJMNc_X3HWuA9j1fiFS0RdKfCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aa971ff94.mp4?token=k6-powcpr1ao2HvCO6LzKDhlHZCKuWmq4TRNfscxQv_p338j-j7AemqGjOkLk1sXwxjVsT5q8Xvi95fPErS9o6jVe0SvZBOcp_XwyQHcz2H50JT0nX_D4CSgQCWfOFh6OEBKdIdb7yLOgS2EdW3OTPswHGr8hM-_4N0z6Gfu9lZihfMx-bQGtaDgSdKpqCOUFROivY66EkmSo75b8Q_5j9yXNpTVe_76Y7NfyYCXht2q95Wq0-DkyM3eV3q1DItaZlXsplUwaBKz8D_Pigr5LvLRkMX0kGW4_r4dIbMltj0rY5b7JS0qq29pT6Q8HJMNc_X3HWuA9j1fiFS0RdKfCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداوسیما: نگاه کلیشه‌ای به زن در جامعه خیلی زنان را اذیت میکند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/133015" target="_blank">📅 13:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133014">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
الجزیره: تنگه هرمز اکنون «کارت اصلی درگیری» میان آمریکا و ایران است
🔴
تهران به دنبال افزایش حاکمیت خود بر تنگه بیش از آنچه پیش از جنگ از آن برخوردار بود، است
🔴
آمریکا نیز می‌خواهد اطمینان حاصل کند که هرگونه رقابت با حضور آمریکا در تنگه هرمز، به تهدیدی امنیتی مستقیم علیه ایران تبدیل خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/alonews/133014" target="_blank">📅 13:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133013">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02f442a510.mp4?token=jzXojyv1qsx3EEdqmIxxbvie4Zt9zar4fhKhPmYiCrzgQSZ_rdvakOpsARxf0ND0AMTWSXGiHbPgFUwnNNF0qM1S3JvRPGpNoW6sitw_Ah9_9LHuNIujZAAEKbg5IF6xdghPLakWzNUiyKS3i4HVETX-e4k7hsoCEVHu8-4kUcSQZxn6sVmt54mRGkIy49yKJB3pvL98Mz4N_se3r6ynRIQE2Nbayug_frPqwhhQlUnmcLFkN6-ENDhOfScBpBzy9pxUPK_tp_9E-9bubZzXuQB_MMAIyup48d8wObm24BDv6phYMYq1yxeB06R8eDuwm7LHlVV2ZNqV0qX_aI6TcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02f442a510.mp4?token=jzXojyv1qsx3EEdqmIxxbvie4Zt9zar4fhKhPmYiCrzgQSZ_rdvakOpsARxf0ND0AMTWSXGiHbPgFUwnNNF0qM1S3JvRPGpNoW6sitw_Ah9_9LHuNIujZAAEKbg5IF6xdghPLakWzNUiyKS3i4HVETX-e4k7hsoCEVHu8-4kUcSQZxn6sVmt54mRGkIy49yKJB3pvL98Mz4N_se3r6ynRIQE2Nbayug_frPqwhhQlUnmcLFkN6-ENDhOfScBpBzy9pxUPK_tp_9E-9bubZzXuQB_MMAIyup48d8wObm24BDv6phYMYq1yxeB06R8eDuwm7LHlVV2ZNqV0qX_aI6TcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پالایشگاه نفت مسکو تو روسیه از صبحِ تو آتیش می‌سوزه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/133013" target="_blank">📅 13:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133011">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpO25LrVN-H4BXZ0-C_ja9-w6-u9nFyCOsiiK6KtDhbVoxeaXz55ojrwxuNG0OjTODl2_aB1B2onFQAE4X8oqW4hdsqZKcHi53G3SEh2_rGZusj9XyLtB8tiGNtXoJmH5kGy4QHIZKGGN8GycpQH7eUC5JeF1oyZvgoMP-5KA8h4IOmSZB5tilPj24NGpgx7KdM8ZaGaiYqR_a2t08Pv_v02lwyxyZuMHf_10H6sp8By-kkD2d4omkv5cPKZ5Lyvc9_iYvdaBpwwNqKDH_igSDH0LRZS309UUTwIcGUiskxqaffcXq2TAA0oPdOUdC_yghhIO_FrJsIwBmprfK2L9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bae26a6683.mp4?token=EthmZS1zOIMh6ldbgTcClf0NGMRcjJhQ0NsvrwfwUkYwpEnCHKhmFW0Lw3Tktb_PXsbQSect2YvCuwG5npjzHYDs8VrhxHmk2FCkpD_fqOmQSjFvHdk0Mohx6_cyAfaDuAQ8NJeqn16U0FcB34XJO9Qe8hcqb0dv_qNQWyp0xMZw-9bCWBIWm7lhzkzrzUMXiE177id5JLZDOasUM6bv-XyaSC8AjOoJH61EKkX-v801zRfZSalAcFxsBbvSw4h17H5kfzSap80kz0TEK8YEhArtC3DNjhhh4a2iSAG22FqPrHhYQwLUtQMPs2TWTMVjzNFTW-drd9iwotYv85OAwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bae26a6683.mp4?token=EthmZS1zOIMh6ldbgTcClf0NGMRcjJhQ0NsvrwfwUkYwpEnCHKhmFW0Lw3Tktb_PXsbQSect2YvCuwG5npjzHYDs8VrhxHmk2FCkpD_fqOmQSjFvHdk0Mohx6_cyAfaDuAQ8NJeqn16U0FcB34XJO9Qe8hcqb0dv_qNQWyp0xMZw-9bCWBIWm7lhzkzrzUMXiE177id5JLZDOasUM6bv-XyaSC8AjOoJH61EKkX-v801zRfZSalAcFxsBbvSw4h17H5kfzSap80kz0TEK8YEhArtC3DNjhhh4a2iSAG22FqPrHhYQwLUtQMPs2TWTMVjzNFTW-drd9iwotYv85OAwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیشب عده‌ای داشتن شعار علیه قالیباف میدادن که مهدی رسولی مداح خیلی سوسکی این شعارها رو تبدیل کرد به حیدر حیدر
🔴
الانم تندروها دارن بهش حمله میکنن و میگن خایمال
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/133011" target="_blank">📅 13:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133010">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46be7e5d32.mp4?token=hJHLEFMmxQhKK42mQdBfuX-Jt_YqIYNqY2vqy2xHL2LqdJ9LXHs3EKbMDanSsXoI545QKe_vs3gspyJ0CIoplBY93t6U3UN4K6E6j0mNYqhFsCo95VTK-OtNR6OkCcR9sEFj34WPiGBluXW4b8OqPkxIFtIcCiTZ5WjnlLF06JZtk2xwgMujUVgTFBQh2cd5pEOhv5BJGErqSq8muGstIgzLvopNH6OKggJzA1-Ym3UXQ_wVC_FWw-8tPDS6vN6lUxfsuVfnZ0dTCqITmpfT6wkg7rDKDGilZwv1XDLVvlCB_nRFNUTocoqSpN9_x0oANFZjHwbFuDJ6xRoZVr9Vk72Rdx22ywdkQHtI1lc9E5OFArvi38XXDBqP1Gpj2EezvRrf_wGupvCZ40CCKo_Uz-ZnP4TFIY3dvdIOtiV_0Tr8DC8GL_O5VxPSzIOoLY-E83v9qIgXX9deZ2VRMVVvyeFuWg7O7do-WYxaSTGdc_9pO1HFFqXY4EgnEXtnlq6wmuxvgoYC4bDa4v7Iwx5jYttDPO5y8tM60TaYkRBKk5obMcLwf1w-B9mLwgNHYdDhrdzkNu0-9ZbVEEvdFeJ95IZu9zaG_gNuwym7kFCFHmyBGXUiUJlUp32wYyJC6Kj-1kzLijUl1Cwx5hKx-tAPhiGNuXDXp1yB6_YJAXi6bco" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46be7e5d32.mp4?token=hJHLEFMmxQhKK42mQdBfuX-Jt_YqIYNqY2vqy2xHL2LqdJ9LXHs3EKbMDanSsXoI545QKe_vs3gspyJ0CIoplBY93t6U3UN4K6E6j0mNYqhFsCo95VTK-OtNR6OkCcR9sEFj34WPiGBluXW4b8OqPkxIFtIcCiTZ5WjnlLF06JZtk2xwgMujUVgTFBQh2cd5pEOhv5BJGErqSq8muGstIgzLvopNH6OKggJzA1-Ym3UXQ_wVC_FWw-8tPDS6vN6lUxfsuVfnZ0dTCqITmpfT6wkg7rDKDGilZwv1XDLVvlCB_nRFNUTocoqSpN9_x0oANFZjHwbFuDJ6xRoZVr9Vk72Rdx22ywdkQHtI1lc9E5OFArvi38XXDBqP1Gpj2EezvRrf_wGupvCZ40CCKo_Uz-ZnP4TFIY3dvdIOtiV_0Tr8DC8GL_O5VxPSzIOoLY-E83v9qIgXX9deZ2VRMVVvyeFuWg7O7do-WYxaSTGdc_9pO1HFFqXY4EgnEXtnlq6wmuxvgoYC4bDa4v7Iwx5jYttDPO5y8tM60TaYkRBKk5obMcLwf1w-B9mLwgNHYdDhrdzkNu0-9ZbVEEvdFeJ95IZu9zaG_gNuwym7kFCFHmyBGXUiUJlUp32wYyJC6Kj-1kzLijUl1Cwx5hKx-tAPhiGNuXDXp1yB6_YJAXi6bco" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چندین تُن از کمک‌های بشردوستانه ایران به زلزله زدگان ونزوئلا اهدا شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/133010" target="_blank">📅 13:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133009">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19f47e808.mp4?token=EVuSf3j9KyEYSW5EBHTKuyL5hmRMRlysPf1i43KldOZg5_MghW6fRBuDpuuSz3tyX5xwjVz3Iw6TlaUoovsoatkxwUtk2S4dYcmnh2W8zvDwTPD6jE2HsyPydnt6nFKN72ixie7MKmd-JyaDh_alrLicJfQV5r_GIULyWdDbfRFYXGroBWNd-NdtJRDuuPYMspU0Dh97qCv271lR-WW1EaO4oQSjxJE_ckJvVlbrJgwAxMsvk8zlksbTRfIBVsAnFUzu8IoY4RpCLkkpxn1cGANahkvWHSx5Mbzf3NyJ8IGCyp6eRpnvq3-Dyy5erZsS1UIcC4P4hW_65KlYwO-fVVg5uqhaXLpj4QkWp3pjsMgwylrxpU96RH3oU1F9M-83IA6It1RG_VHQhkxILPl0sL-U2b7cU75iguekuF8_8mu-uGKxZdrRflRxi1wA3g1TUr0XkrFdC36hE9CjO1hgPLfO4N1-I_wQT6XnYf_O2HeIXt4oH0PnJLQDnl9yH0f1ZY3AlWQQNJPwbnHhBQYInMedzKoi8vkm0jZuZDDW5PG6iXgUmtdcdk0aDFIK03KwDMEnMXTKO28Tw0tVBEkKcYi6xkHo3YDbZT4Qm3nhk6v3CVgPCCGok6RpGMJVcApzcFp1ZEIeIiH8eg1BloO3AQCfn0QgXW3vPpBJYTS8KwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19f47e808.mp4?token=EVuSf3j9KyEYSW5EBHTKuyL5hmRMRlysPf1i43KldOZg5_MghW6fRBuDpuuSz3tyX5xwjVz3Iw6TlaUoovsoatkxwUtk2S4dYcmnh2W8zvDwTPD6jE2HsyPydnt6nFKN72ixie7MKmd-JyaDh_alrLicJfQV5r_GIULyWdDbfRFYXGroBWNd-NdtJRDuuPYMspU0Dh97qCv271lR-WW1EaO4oQSjxJE_ckJvVlbrJgwAxMsvk8zlksbTRfIBVsAnFUzu8IoY4RpCLkkpxn1cGANahkvWHSx5Mbzf3NyJ8IGCyp6eRpnvq3-Dyy5erZsS1UIcC4P4hW_65KlYwO-fVVg5uqhaXLpj4QkWp3pjsMgwylrxpU96RH3oU1F9M-83IA6It1RG_VHQhkxILPl0sL-U2b7cU75iguekuF8_8mu-uGKxZdrRflRxi1wA3g1TUr0XkrFdC36hE9CjO1hgPLfO4N1-I_wQT6XnYf_O2HeIXt4oH0PnJLQDnl9yH0f1ZY3AlWQQNJPwbnHhBQYInMedzKoi8vkm0jZuZDDW5PG6iXgUmtdcdk0aDFIK03KwDMEnMXTKO28Tw0tVBEkKcYi6xkHo3YDbZT4Qm3nhk6v3CVgPCCGok6RpGMJVcApzcFp1ZEIeIiH8eg1BloO3AQCfn0QgXW3vPpBJYTS8KwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زرشناس کارشناس مسائل سیاسی در صدا سیما: آنقدر تنگه هرمز را باز و بسته کردیم که اثرگذاری آن سست شد
🔴
باید مواضع اقتصادی منطقه را بزنیم؛ یکی زدند ۵ تا باید جواب دهیم تا بازدارنده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/133009" target="_blank">📅 13:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133008">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فووووری/نخستین تصویر از فرد تیرانداز
◀️
مشاهده عکس بدون سانسور</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/133008" target="_blank">📅 12:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133007">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
جوزف عون، رئیس‌جمهوری لبنان و ژنرال رودولف هیکل، فرمانده ارتش، آمادگی‌ برای استقرار نیرو در مناطق جنوبی را بررسی کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/133007" target="_blank">📅 12:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133006">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی: تشدید تنش‌ها بین واشنگتن و تهران ممکن است به عرضه مازاد مورد انتظار در بازار نفت در سال ۲۰۲۷ آسیب برساند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/133006" target="_blank">📅 12:53 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133005">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
پاکستان: حملات تروریستی از افغانستان سازماندهی می‌شود
🔴
نخست‌وزیر پاکستان مدعی شد حملات اخیر در بلوچستان و خیبرپختونخوا از خاک افغانستان هدایت می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/133005" target="_blank">📅 12:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133003">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
پاکستان: حملات تروریستی از افغانستان سازماندهی می‌شود
🔴
نخست‌وزیر پاکستان مدعی شد حملات اخیر در بلوچستان و خیبرپختونخوا از خاک افغانستان هدایت می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/133003" target="_blank">📅 12:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133002">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_adI2mKgxsLbX9aKlGouHSVlHsTELADBgI6yYCAOKjQw8O6QLs7V8cuPyBcVbvcxJbJRtHoweR_DoGv2pSHy-EC8yXfGn5BO7zIVIUrgYufFsgIo9Rh-Q3l5aWyZ5u_s4qtMdgdkjEW1eY01hLFoJjIGyX7AsWaQvOSUUfS52krdFb9UpKJbMr-TekRKgvuj6rBpoS2AB2q7LeJ1HBnOOnVIc92uv-MbrU48Z4yiR8scnGl8UbudSrWUu8L_gbhkHFYTDNh3S1vaDWVmQTsb7ziPw1tw2kCSpj1drM_o1yu92e4Ep1wbkZKweUJxPPV50XX1Q0URanSHxn-NY6G5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت عضو تیم مذاکره‌کننده: تفاهم خوب بود و شیوه اجرای آن هم تا الان خوب است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/133002" target="_blank">📅 12:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133001">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQAdBiJPHfoWU-DR-d9RANRoCKd4hf2mGMs-01iZExwSXtSM4_Luq-DelmrbDSycw9RNGW4yh7uJCnV16TbHHNtR3xUtao9v4Gv_En78R7I4CCYjuZcYHWo9X_gYMHSyzx_ezchXWGN26MnfuEwfdMPZaQenFhPGT4qscTDOX3EbHN4Vd6jDCKhtuV6e2n7CQe1ZfefQ5WAiE-7TfFcpYZ6PapWsKjsVEoDErrFyr-4wf3SmvMZ23aJxxW2yIlg7UmcqQEWdIBQTeIoYi0kOND17FZq1YupD7HvWncDKU3893rkmFzrCGaNH6FRbdCF2ZV_AovvvB03U3I9qcNtOdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاهش ۴ درصدی قیمت نفت پس کاهش تنش‌ها در خلیج فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/133001" target="_blank">📅 12:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133000">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سیتی ژورنال: وزارت خارجه آمریکا جلوی دیدار مقام ارشد تیم زهران ممدانی با سفیر ایران در سازمان ملل را گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/133000" target="_blank">📅 12:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132999">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/177af0ba50.mp4?token=kh5M4Kozg4GN2WWNG2cfJHy2YWhL0luzCQvA95PzMRfo4yZyifTGVIgAW4r3cME8Izglx8-8S72O3YfDuVudhL-WcCqQuXF1l__B9y19QEGAMGHmHC5W8QlVrQ4Vgf65IEgQ-2AKsBns3HDbzHNEVoZ7h-bULvmSUIdqK-CyjWCLLvg1-UKioLEhNQn_tF6prZt4zzasd8KYWqKbq0uE3-4ngBLnFYnk0gRnJlDd8gd29MGv1Ak62_7G3PfJJ8vLRzuOH6NfomNtkGLS7MusXeljfkCMPDs4tqzL8Q1OvrSqt9MKhkw0g2ZlL8Sal4XD4QRTFWFHfYxY1EYMUZvvfEPW9gBuG3XTuBp5u87nye-ebkjxJV5ojb1zrfcfUTBGz2tbcP1DZc1SL21y5hTmxhXlmDbFhC9PEmG07729l_-7XRDW6b3E6tO_SQVNkGgvLq8BsWZ8guL_t8jLyR_FLITvHBtQB6EKrCwzxybX3Bw-72XX72a1Wvfc2u0pLZ8EubY_5qnnc7BACrS_HTVp8bLLVUrNle78o9PFmsWTcgoZfnmkBotR1EH22ZHMtgkDWzeiY4zP3IL-7zDwEiT1gmWV-oTbiSfYnhkeAB041X-QyHr6z7E0fuUmlN8OFejtvSg-jAQWvCNoRjkgJBd_TGh_fjt7XH6Nc1ndX3AOtwE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/177af0ba50.mp4?token=kh5M4Kozg4GN2WWNG2cfJHy2YWhL0luzCQvA95PzMRfo4yZyifTGVIgAW4r3cME8Izglx8-8S72O3YfDuVudhL-WcCqQuXF1l__B9y19QEGAMGHmHC5W8QlVrQ4Vgf65IEgQ-2AKsBns3HDbzHNEVoZ7h-bULvmSUIdqK-CyjWCLLvg1-UKioLEhNQn_tF6prZt4zzasd8KYWqKbq0uE3-4ngBLnFYnk0gRnJlDd8gd29MGv1Ak62_7G3PfJJ8vLRzuOH6NfomNtkGLS7MusXeljfkCMPDs4tqzL8Q1OvrSqt9MKhkw0g2ZlL8Sal4XD4QRTFWFHfYxY1EYMUZvvfEPW9gBuG3XTuBp5u87nye-ebkjxJV5ojb1zrfcfUTBGz2tbcP1DZc1SL21y5hTmxhXlmDbFhC9PEmG07729l_-7XRDW6b3E6tO_SQVNkGgvLq8BsWZ8guL_t8jLyR_FLITvHBtQB6EKrCwzxybX3Bw-72XX72a1Wvfc2u0pLZ8EubY_5qnnc7BACrS_HTVp8bLLVUrNle78o9PFmsWTcgoZfnmkBotR1EH22ZHMtgkDWzeiY4zP3IL-7zDwEiT1gmWV-oTbiSfYnhkeAB041X-QyHr6z7E0fuUmlN8OFejtvSg-jAQWvCNoRjkgJBd_TGh_fjt7XH6Nc1ndX3AOtwE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک روحانی:
قالیباف شاشیدم وسط اتحادی که درست کردی
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/132999" target="_blank">📅 12:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132998">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
پرواز‌های فرودگاه مشهد از سر گرفته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/132998" target="_blank">📅 12:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132997">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPU0zKS1znyzE1FznM5JQVj4-YQJ2lmpLEEjILiLCIe1hsqoNrxI1f6sWrseQoywAvYLMhTF3cUYaf8wroCjhXdRAvhkQH3QeLIYtuGo9O-2JQKs5uKHVLOGW8-4FR1vFxyz8eIoH3lKFkIr5OYINZKOJu22pIkJfz7WcVOsi5Vq7For0srx7C0QcUh_DIK8XysjY1CBVcYsIY-z8GYPzfb8je_e6DvjpJXtRZLLyafZIwRACsmT4L8YQDlMv1YTctbRZ_ImowUO0NMIP7Dh3giIZ4E2ndN3b-3AtW5KRTH_c-dOSKc6BqwxBwPvkdGHRTIANR-IGhiBGaqfyrg_Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زیرنویس شبکه خبر : آزمون‌های نهایی بدون تغییر و براساس برنامه ابلاغی از ۲۱ تیر آغاز می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/132997" target="_blank">📅 12:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132996">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
شرکت آسلسان قراردادی به ارزش ۱.۴۷ میلیارد یورو با شرکت SSB ترکیه برای تولید انبوه سامانه‌های پدافند هوایی امضا کرد
🔴
این قرارداد تحت برنامه گنبد فولادی، طرح چندلایه پدافند هوایی/موشکی ترکیه  قرار می‌گیرد که اردوغان اخیراً با ۲۴ میلیارد دلار بودجه اضافی از آن حمایت کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/132996" target="_blank">📅 12:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132995">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b00498f39.mp4?token=SCgn0wvimO9hQuXyR3oHEBQCBuoEk5ICA6_VsEbW3-8qsWEiMjP_IyFwybMud8xljhpRL56lc7Zp3a0-qNILVhRvhlpVKJvl3NpvVVU_XswKG5QaqfWYB3OAgck9HMR_K0_nZuL-3I-rXaT8nZFbgbiwaqYjlN2W-6O84nxjSVmbWk-N08_1gKjSDZXsR7pH4dleefXLxzKzwdzri_RlPJqSfL1TFlPurFNgbHeoxdXQhPa5x6UyktST160czzH9riRZyIGwJJIbwaL_chyrdPMQgfjU1huIrJcQkmAz29xhTTuUKxn6OucqHawc3UbZf9i6g4bKlNB8VA61JNkE9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b00498f39.mp4?token=SCgn0wvimO9hQuXyR3oHEBQCBuoEk5ICA6_VsEbW3-8qsWEiMjP_IyFwybMud8xljhpRL56lc7Zp3a0-qNILVhRvhlpVKJvl3NpvVVU_XswKG5QaqfWYB3OAgck9HMR_K0_nZuL-3I-rXaT8nZFbgbiwaqYjlN2W-6O84nxjSVmbWk-N08_1gKjSDZXsR7pH4dleefXLxzKzwdzri_RlPJqSfL1TFlPurFNgbHeoxdXQhPa5x6UyktST160czzH9riRZyIGwJJIbwaL_chyrdPMQgfjU1huIrJcQkmAz29xhTTuUKxn6OucqHawc3UbZf9i6g4bKlNB8VA61JNkE9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انتقاد نماینده مردم تهران از تعطیلی دنباله‌دار مجلس: قانون‌گذاری تعطیل است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/132995" target="_blank">📅 11:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132994">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی: انتظار می‌رود تقاضای جهانی نفت در سال ۲۰۲۶ حدود یک میلیون بشکه در روز کاهش یابد.
🔴
عرضه جهانی نفت در سال ۲۰۲۶، ۳.۷ میلیون بشکه در روز کاهش خواهد یافت.
🔴
عرضه نفت در ماه ژوئن ۴.۱ میلیون بشکه افزایش یافت اما همچنان پایین‌تر از سطح قبل از جنگ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/132994" target="_blank">📅 11:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132993">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
آمریکا اعلام کرد همچنان به تفاهم‌نامه با ایران متعهد است و به دنبال مسیر دیپلماتیک است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/132993" target="_blank">📅 11:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132992">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ترکیه اس-۴۰۰های روسیه را به کشورهای خلیج فارس فروخت
🔴
یک روزنامه نزدیک به دولت ترکیه گزارش داده که آنکارا سامانه‌های پدافند هوایی اس-۴۰۰ خریداری‌شده از روسیه را به یکی از کشورهای حاشیه خلیج فارس واگذار کرده تا راه را برای دریافت جنگنده‌های اف-۳۵ از آمریکا هموار کند.
🔴
عبدالقادر سلوی، نویسنده روزنامه حریت ترکیه، افزود که امارات متحده عربی و قطر از جمله گزینه‌های مطرح به‌عنوان خریدار این سامانه‌ها هستند، اما تأکید کرد که باید منتظر اعلام رسمی ماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/132992" target="_blank">📅 11:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132991">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
شرکت بین‌المللی انرژی: پیش‌بینی می‌شود در سال 2026 عرضه جهانی نفت با کمبود 860 هزار بشکه در روز مواجه شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/132991" target="_blank">📅 11:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132990">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
عضو هیئت‌مدیره تعاونی صیادان گفت: در جریان حملات روز‌های ۱۷ و ۱۸ تیرماه به نوار ساحلی استان هرمزگان و در پی اصابت دو پرتابه ارتش آمریکا به اسکله صیادی پنج‌پله بندرعباس، دست‌کم ۳۰ فروند قایق صیادی به‌طور کامل از بین رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/132990" target="_blank">📅 11:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132989">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
بیت‌کوین ، بزرگ‌ترین رمزارز جهان ۳.۵ درصد در روز جمعه رشد کرد و به نزدیک ۶۴۰۰۰ دلار رسید و ۴.۲ درصد طی یک هفته رشد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/132989" target="_blank">📅 11:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132988">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/996091c351.mp4?token=J1zftGxeJqpr_9OUmwY0jpp2OrcyrmA05pprJ1zu5T-xZxSmWpo3OXCusdUpSOhCgIMA-6W3DvaD0a2XSMYYyQ6kbGOmRhYuf4fZRfR211_39WbgStnsGyLQeMmAkFguI0TtNB_oZqUM_FdZImAoGJi2j1kn9IQjVwOwMU9hJK2L4BHJFR9JLAPF4lJdA2fNgmajkI-JjRMOxaXo_-5WbE6HPq2SYgWs74AO6yXSOXaB0M3vbNXeIDURF0KRmt-ssLetobwZtYhmdJInjNZyUIIQupTeGqWIKFZr2z_CbSfpCI6D2h_QAXAoj3KqinCXe1x3BphlnnJUshNCWRItEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/996091c351.mp4?token=J1zftGxeJqpr_9OUmwY0jpp2OrcyrmA05pprJ1zu5T-xZxSmWpo3OXCusdUpSOhCgIMA-6W3DvaD0a2XSMYYyQ6kbGOmRhYuf4fZRfR211_39WbgStnsGyLQeMmAkFguI0TtNB_oZqUM_FdZImAoGJi2j1kn9IQjVwOwMU9hJK2L4BHJFR9JLAPF4lJdA2fNgmajkI-JjRMOxaXo_-5WbE6HPq2SYgWs74AO6yXSOXaB0M3vbNXeIDURF0KRmt-ssLetobwZtYhmdJInjNZyUIIQupTeGqWIKFZr2z_CbSfpCI6D2h_QAXAoj3KqinCXe1x3BphlnnJUshNCWRItEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتیش سوزی سنگین تو منطقه آلمریا، اسپانیا
🔴
دست‌کم ۱۱ نفر بخاطر آتیش‌سوزی‌ جون خودشون رو از دست دادن
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/132988" target="_blank">📅 11:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132987">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
کره شمالی از تقویت کمی و کیفی توان هسته‌ای خود خبر داد
🔴
رسانه دولتی کره شمالی اعلام کرد این کشور در نشست کمیسیون مرکزی نظامی به ریاست «کیم جونگ اون» تصمیم به تقویت کمی و کیفی نیروهای هسته‌ای خود گرفته است.
🔴
بر اساس این گزارش، پیونگ‌یانگ در نظر دارد زیرساخت‌های فنی سامانه‌های رزمی را ارتقا دهد، پایگاه‌های نظامی را نوسازی کند و فرآیندهای تولید نظامی را استانداردسازی کند.
🔴
کیم جونگ اون نیز بر افزایش توان واقعی رزمی ارتش خلق کره و تسریع «انقلاب در آموزش نظامی» تأکید کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/132987" target="_blank">📅 11:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132986">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c52LRx1b9xEiF1L_OeOIeysJhBJOamb1XQXgHxMuhNBRJnD9KGLioqKHeOYMPm0xuVhtWNBJcOLjbRqHRkyGd3D5_sFJQ78p2qfpPTPNbbstRNliHG8bPHSVx8i3PNAUCNDKddRf9FIlJpPkulViQyK7X7SraR3rHl-U-7ZvAHfs1XxqqrXN9bgfNNhMfPb6-Jd3qnSZWO1lPssxo4cdA46dwpt8GHqyB6LNKs0OSjjoFXSlQinIx8EecXI-zPFKYwMotjrSAMcXb7lA0nlgyyDU0HJoX_USeLXyZLC1GZr2LppeArUguMDhhn1fHEZQmzALMUUEEMOlM0_LtR-RDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مردم ایران نسبت به همسایگان چقدر بنزین مصرف می‌کنند؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/132986" target="_blank">📅 10:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132985">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ارتش اسرائیل: ما به عملیات خود برای از بین بردن هرگونه تهدید ادامه خواهیم داد و اجازه نخواهیم داد حزب الله به ما آسیبی برساند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/132985" target="_blank">📅 10:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132984">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوری / فاکس نیوز: یک مقام آمریکایی به من گفت مذاکرات با ایران در هفته پیش رو ادامه خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/132984" target="_blank">📅 10:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132983">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
آموزش‌وپرورش: زمان‌بندی امتحانات نهایی تغییر نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/132983" target="_blank">📅 10:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132982">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
شبکه CNN به نقل از یک مقام آمریکایی گزارش داد: شرایط به‌ سرعت در حال تغییر است و در صورت لزوم، حملات از سر گرفته خواهد شد و ایالات متحده فهرستی از اهداف را حفظ کرده است
🔴
همچنین فرمانده ناو هواپیمابر آبراهام لینکلن در دریای عرب به خدمه این ناو دستور داده…</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/132982" target="_blank">📅 10:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132981">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
شبکه CNN به نقل از یک مقام آمریکایی گزارش داد: شرایط به‌ سرعت در حال تغییر است و در صورت لزوم، حملات از سر گرفته خواهد شد و ایالات متحده فهرستی از اهداف را حفظ کرده است
🔴
همچنین فرمانده ناو هواپیمابر آبراهام لینکلن در دریای عرب به خدمه این ناو دستور داده است آمادگی کامل خود را حفظ کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/132981" target="_blank">📅 10:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132980">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvv0wufAJ2iSXM45kYMm9bJVfqZjwfntSV-VTQ8UzIbrfMLVPN62XMoV1gypjz1cVNIgIV1Uwuqm3iNt7NNcx1yVlbyJzjLP2rv6B2FB9orQezynWI6Zj6hMZiLqzTV4yH3m6YYvnkDDAXfECE-nQKSkDYQtpXdKNRFhO0oF8Q_26rzUfiTWSfK9qQFJVHF127Lh3b_YQH4Qqpvjx1zPBerToLUmd_CcFGnSYyBEzfEgGQTksWepodIA313_pGeQJGjdDBDc4xA1BQsmYXE7c0uyncBQRNcw1LitPCgnoIE-J_qhlwTyWEMFWeLXRt2o415h_sdAs4UucJiU9_H-oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت ۷۶ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/132980" target="_blank">📅 10:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132979">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSpvnlXACu-QBkw0d19xR2YOaRnbA-Uh6GHek47OIQzr4MnKxP5BHuWunPD0aG42x0CUj_-dw1EAcCKHNgAwBcpTbF5y2cf6bBrK3md5vdw0DXqFjtSS9FqoOBXWPG8Zea7rnpv2RBwO24BhYajiCy1NkqmSaUW0Vn-4vtZFpRTpqlhVZtUPBxWxIbD9YbUUWvW71gSu_eBO4Um74cfppCXRiWxXhS5dA3WJaFc8tvH_Fk6OykfZQYy4phNEXVcnNcHzPZiPDjL8SGNOYv4ggGzpjqgdeOk-Yfu2LlklBiiGJO6ozkW0_j3lW3hFX5CGmOqaY65WmM5bmaN0qwHOzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق شبکه Truth Social:
امروز روز بسیار مهمی در پالم بیچ، فلوریدا بود، و افتخار بزرگی برای من بود که فرودگاه بین‌المللی پالم بیچ، با رأی قاطع، به نام "فرودگاه بین‌المللی دونالد جی. ترامپ" تغییر نام داد.
🔴
این منطقه بسیار پرطرفدار است، موقعیت مکانی عالی است، و بازسازی آن فوق‌العاده خواهد بود. از همه مردم پالم بیچ به خاطر رأی و اعتمادتان سپاسگزارم.
🔴
به زودی این یکی از بزرگترین و باشکوه‌ترین فرودگاه‌های جهان خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/132979" target="_blank">📅 10:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132978">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل: تل‌آویو اطلاعات استخباراتی درباره ترور ترامپ را با واشنگتن به اشتراک گذاشته، اما سازمان اطلاعات آمریکا این اظهارات را به عنوان یک هشدار جدی تلقی نکرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/132978" target="_blank">📅 10:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132977">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
رییس ستاد کل ارتش اسرائیل، ایال زامیر روز گذشته در مراسم فارغ‌التحصیلی خلبانان، اینچنین گفت:  کارزار در ایران تمام نشده است. بر روی میز، طرح‌های جدیدی وجود دارد. عملیات‌های بزرگی همچنان در پیش روی ما هستند. آماده باشید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/132977" target="_blank">📅 10:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132976">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ff64c02f.mp4?token=lsJAgTSr6kenoZLlQV-TjDCaUMAW4ry23gsiLLJDEZqS68JqCUcN8m6CTFXzlfujk5yAAaMFrvj4AE-wsi8L_6seG_ulRvDaHW_7AeEI5koTkudKoun-8uVzAeUlnddDLW-QSJhqndSXS1CuRHxptlqZi5lLXTOd4cEL1pCbMUTDfXuXxmeb--D-1a9OOTG-UDrMWVlPmdmyh8JmZa_pkGDk_vil3JxLhwYsxsZaM6Pb-HX1GGuzPUjJ93shEM3QoyoEeg1SdyS4MQMPrgKrK7-nUy2GdLmMcq0d1rK3Ta2PqXewMKaxEilVEqyU1fWDTyyKBxv2EONjPXokIQd3XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ff64c02f.mp4?token=lsJAgTSr6kenoZLlQV-TjDCaUMAW4ry23gsiLLJDEZqS68JqCUcN8m6CTFXzlfujk5yAAaMFrvj4AE-wsi8L_6seG_ulRvDaHW_7AeEI5koTkudKoun-8uVzAeUlnddDLW-QSJhqndSXS1CuRHxptlqZi5lLXTOd4cEL1pCbMUTDfXuXxmeb--D-1a9OOTG-UDrMWVlPmdmyh8JmZa_pkGDk_vil3JxLhwYsxsZaM6Pb-HX1GGuzPUjJ93shEM3QoyoEeg1SdyS4MQMPrgKrK7-nUy2GdLmMcq0d1rK3Ta2PqXewMKaxEilVEqyU1fWDTyyKBxv2EONjPXokIQd3XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک خبر خوب و زیبا
🔴
نارین و آیلین دختران سنندجی بعد از مداوا و درمان دیروز از بیمارستان مرخص شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/132976" target="_blank">📅 10:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132975">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ترامپ اعضای کمیسیون فدرال را برکنار کرد
🔴
دونالد ترامپ، رئیس‌ جمهور آمریکا، در اقدامی جنجالی دو عضو دموکرات و یکی از اعضای جمهوری‌خواه کمیسیون کمک به انتخابات آمریکا (EAC) را برکنار یا وادار به استعفا کرد؛ اقدامی که این نهاد فدرال را تنها چند ماه پیش از انتخابات میان‌دوره‌ای ۲۰۲۶ بدون هیچ کمیسیونری باقی گذاشته است.
🔴
بر اساس گزارش‌ها، «توماس هیکس» رئیس کمیسیون و «بنجامین هوولند» دو عضو دموکرات این نهاد از سمت خود برکنار شدند و «کریستی مک‌کورمیک» عضو جمهوری‌خواه نیز اجازه یافت از سمتش استعفا کند.
🔴
کاخ سفید این تصمیم را تأیید کرده و اعلام کرده است رئیس‌جمهور اختیار دارد افرادی را که با مأموریت «تضمین امنیت انتخابات و شمارش آرای قانونی» همسو نیستند، از سمت خود برکنار کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/132975" target="_blank">📅 10:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132974">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ادعای آمریکا درباره خنثی‌سازی طرح ترور ترامپ در کاخ سفید
🔴
مقام‌های آمریکایی مدعی شدند ۸ نفر را به اتهام برنامه‌ریزی برای حمله‌ای تروریستی در جریان یک رویداد هنرهای رزمی در کاخ سفید تحت پیگرد قرار داده‌اند.
🔴
به گزارش الحدث، وزارت دادگستری آمریکا ادعا کرده هدف این طرح، ترور دونالد ترامپ، جی‌دی ونس و چند شخصیت برجسته دیگر بوده است.
🔴
در ادعای اف‌بی‌آی، مهاجمان قصد داشتند با استفاده از پهپادهای حامل مواد منفجره و استقرار تک‌تیراندازان این حمله را اجرا کنند.
🔴
مقام‌های آمریکایی همچنین اعلام کرده‌اند این طرح پیش از اجرا شناسایی و خنثی شده و تمامی متهمان بازداشت شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/132974" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132973">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeG5iv64o_6SRC56OPL7kcormvHkHbHgJsywDP4axK-IfBgqGoPxYICdyRKe1E3Wjtyt-PxhrZyPf6VI_XGHLcy-_pwKoA6xWWDKbn9Rounr2Vn4weWZbrB8g2sinNSC8ut-3QS4c4_H2u9pWHy5mBWtylwMPmBcAhNi46R-qiHQU_byT5XAOifjUT04hZSh2_3gKhd6EjEfNuaJju6kd5ECi0ernKXvJcUuidS11yqasR5smOnlWYKmXxVSz5ncpjTQsBAQyoiZ4X61k3N09ZTNp5tM3kXVZIX8qnMmq9I83CYBOROwBxo8wguIUdl-IJZrWr5loYuuf-k1LtbqaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: آقای جبلی! هرکس به شما دستور داده شعار مرگ بر سازشکار مردم مبعوث‌شده رو تو صداوسیما سانسور کنید، حتما عامل دشمنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/132973" target="_blank">📅 09:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132972">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: ایران با جذب شهروندان و اتباع خارجی، اطلاعات و تصاویر مراکز حساس از جمله اطراف وزارت جنگ و مجموعه نظامی‌«کریاه» را جمع‌آوری کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132972" target="_blank">📅 09:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132971">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
رویترز: جنگ ایران، جهان را تا آستانه یک بحران غذایی پیش برد
🔴
درگیری بعدی در خلیج فارس نیز می‌تواند همین پیامد را داشته باشد.
🔴
کشاورزی مدرن به کودهای شیمیایی ارزان‌ قیمت وابسته است. این جنگ با گرفتار شدن کشتی‌ها، تعطیلی کارخانه‌های تولید کود، هراس کشاورزان و افزایش شدید بهای کودهای شیمیایی، تولید جهانی غذا را در معرض خطری جدی قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/132971" target="_blank">📅 09:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132970">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c042252ee.mp4?token=cgC45eXn5WOaz4ABXNB_-zTRAKnF4bctfMFZMVLPR1E2tVs-ui3lLbl6M9AX19I7UsSr-1PmQ8U-TgAA20At64xbNYGRZsYq2SEDbPgjCxGWV4Kx-oCnKbvg83a87T0b4DZX8S4Jd4BZ2UjXrW7gNj6Y2hxLHfrknZC-PrQAgQdKg2TqAtbZB5trr19VBaspYmeBZEsI-lDwp9MpP0ZR9A5AQ30ahQUXGBlQZW43uXg-7-BTaRTaRZz4_QW2JtgZR8cEInpG1yYRE5NkZ8khQIlf52SiXNPDtNPA8ixEsy9TkXdFSwSVQYqvc2AcSy0t7wthb-UXpIkrpK3iB9oCShdhkWskCc5T8--thDgnLyX2tv7aDV3wsE1Ib2-qV8uRih3q0uJU08XvH1RPIsXP05_-KoxYz6qd1S0uGK_cZ4Oc_0xoUTAZdVfz37n_rBn9FZFwbE01hvywKWUxy-iP-csvbhMZokBALDcHNnJRBsZd2grtN90A6y5XYc2hNvShSA_Pt3iVl649FnMfaA3CiQHHQA71L1U1tiv8N5S3oqAJ8Gl0XXC8qO950F00reBdkzE4dqqsBfTv-ca3uORi0Ha4wrZ_hzCOd2ugbTEW5IEBA_lkeSM5Btp4CGRYX7kNzKicglsBER76RuiqkXp_9JZT5a_fjrb4M1C43Gjdlys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c042252ee.mp4?token=cgC45eXn5WOaz4ABXNB_-zTRAKnF4bctfMFZMVLPR1E2tVs-ui3lLbl6M9AX19I7UsSr-1PmQ8U-TgAA20At64xbNYGRZsYq2SEDbPgjCxGWV4Kx-oCnKbvg83a87T0b4DZX8S4Jd4BZ2UjXrW7gNj6Y2hxLHfrknZC-PrQAgQdKg2TqAtbZB5trr19VBaspYmeBZEsI-lDwp9MpP0ZR9A5AQ30ahQUXGBlQZW43uXg-7-BTaRTaRZz4_QW2JtgZR8cEInpG1yYRE5NkZ8khQIlf52SiXNPDtNPA8ixEsy9TkXdFSwSVQYqvc2AcSy0t7wthb-UXpIkrpK3iB9oCShdhkWskCc5T8--thDgnLyX2tv7aDV3wsE1Ib2-qV8uRih3q0uJU08XvH1RPIsXP05_-KoxYz6qd1S0uGK_cZ4Oc_0xoUTAZdVfz37n_rBn9FZFwbE01hvywKWUxy-iP-csvbhMZokBALDcHNnJRBsZd2grtN90A6y5XYc2hNvShSA_Pt3iVl649FnMfaA3CiQHHQA71L1U1tiv8N5S3oqAJ8Gl0XXC8qO950F00reBdkzE4dqqsBfTv-ca3uORi0Ha4wrZ_hzCOd2ugbTEW5IEBA_lkeSM5Btp4CGRYX7kNzKicglsBER76RuiqkXp_9JZT5a_fjrb4M1C43Gjdlys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری فاکس‌نیوز: آنها آدم توافق با ایران نیستند
🔴
برایان کیلمید
:
من فکر نمی‌کنم که ویتکاف و کوشنر باید کسانی باشند که این کار را انجام می‌دهند. آنها تاجر هستند.
🔴
آنها در اوکراین مؤثر نبوده‌اند، در غزه مؤثر نبوده‌اند. آنها در این مورد مؤثر نبوده‌اند.
🔴
ما به دلیلی روشن وزارت امور خارجه داریم، مارکو روبیو را داریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/132970" target="_blank">📅 09:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132969">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
اکسیوس: میانجی‌ها معتقدند که با وجود تشدید اخیر تنش‌ها، دو طرف در دیدار های پیشین برای رسیدن به یک توافق هسته‌ای پیشرفت‌هایی داشته‌اند و می‌خواهند مانع فروپاشی تفاهم‌نامه شوند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132969" target="_blank">📅 09:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132968">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
محمد» در صدر نام‌های کودکان انگلیسی برای سومین سال پیاپی
🔴
بر اساس جدیدترین آمار منتشر شده از سوی ادارهٔ آمار ملی بریتانیا (ONS)، نام «محمد» برای سومین سال متوالی، محبوبترین نام برای پسران متولدشده در انگلستان و ولز باقی مانده است.
🔴
در سال ۲۰۲۵، نزدیک به ۶۰۰۰ پسر با این نام ثبت شده‌اند که تقریباً ۲۰۰۰ نفر بیشتر از نام رتبهٔ دوم، یعنی «نوح» است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/132968" target="_blank">📅 09:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132967">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLGJXmz2ZkZTn0742yyLucS91cy1aZbJSDbVvNoAs3S_1njMojh_ZmxceJo_WeJWieGbnNYk7n-1NMUeC4tK4eD5O9ln_R-84FYvJArQUMZn_ZyyNniPdJ0kSj5nuhByJFQW9o-sQG-mHWY9vaaKZOtL2PVsrZUqaOWS3TagQXwivEgSg7UE3JvahPOOmu8igiMXks2poiZ8YzK65n90K_dlxNShhf8OQNQYWL4sfZ-HKDORn0GzqldFZf_4HYKFgbtiFcJoSaHDXPw-v_365ohu3wwVSXadk6HoTuw43AsncFau9Rcao6GK6pILgODepilpWDjgW5PKJeagN5PoEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اینستاگرام در اقدامی عجیب، قابلیتی اضافه کرده که با آن بقیه می‌توانند از عکس‌های شما برای ساخت تصاویر هوش مصنوعی استفاده کنند
!
🔴
اگر اکانتتان پابلیک می‌باشد، این قابلیت به‌صورت پیش‌فرض فعال است؛ به این‌صورت آن را خاموش کنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/132967" target="_blank">📅 09:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132966">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
تصاویر وحشتناک از آتش‌سوزی در منطقه لوس گالاردوس در اسپانیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132966" target="_blank">📅 09:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132965">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
الجزیره: تردد کشتیرانی در هرمز به دلیل ازسرگیری درگیری‌های آمریکا و ایران متوقف شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/132965" target="_blank">📅 09:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132964">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
اکسیوس: ترامپ روز پنجشنبه بعدازظهر با تیم ارشد امنیت ملی خود درباره تنش‌ها با ایران و مسیر پیش‌رو جلسه برگزار کرد
🔴
پس از این جلسه، یک مقام آمریکایی گفت دولت ترامپ «همچنان متعهد به یافتن یک راه‌حل است و مذاکرات در سطح فنی برای رسیدن به یک توافق هسته‌ای ادامه دارد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/132964" target="_blank">📅 09:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132963">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
صندوق بین‌المللی پول اعلام کرد که بازار جهانی نفت تحت تأثیر تداوم تنش‌ها، تا مدت‌ها شاهد ثبات و قیمت‌های پیش از عملیات‌ نظامی‌علیه ایران نخواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/132963" target="_blank">📅 09:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132962">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
بلومبرگ: روسیه به دلیل فروش نفت در جریان جنگ ایران، کسری بودجه نادر خود را جبران کرد
🔴
پس از امضای تفاهم‌نامه بین ایران و آمریکا قیمت نفت خام روسیه از ۸۶.۵۲ دلار در ماه مه به ۶۳.۵۲ دلار در هر بشکه کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/132962" target="_blank">📅 09:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132961">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
الجزیره : قیمت نفت اندکی کاهش یافت اما در مسیر افزایش هفتگی با وجود حملات جاری آمریکا و ایران قرار دارد
🔴
قیمت نفت خام در معاملات اولیه روز جمعه کاهش یافت، هرچند همچنان در مسیر افزایش هفتگی در میان حملات تلافی‌جویانه جاری میان آمریکا و ایران قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/132961" target="_blank">📅 09:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132960">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از مقامات آمریکایی ادعا کرد: در صورت نیاز، مقدمات حمله به ایران در حال انجام است، اما تمرکز در حال حاضر بر دیپلماسی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/132960" target="_blank">📅 09:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132959">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
یک مقام امریکایی در گفتگو با آکسیوس:
حملات اخیر ایران به کشتی‌های تجاری در تنگه هرمز، توسط گروه‌هایی در داخل ایران صورت گرفته است که با تفاهم نامه شدیدا مخالفت دارند و قصد دارند آن را تضعیف کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/132959" target="_blank">📅 03:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132958">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de4e6346b4.mp4?token=CiSuMFop-rs6yISSxM2QP6Ow7x0V36qrTNpUhMT35c_G1rlUkNd5Ycw1DKr4Q9Cmn9Khj8oCq2abvcxWqB321olG5UmumvhSaXSkPABi49Ikc_i63SswXUMEEns3CoJWLbZjS-gJKqHV2IUeRE7pTNt4ma1FiCBHYhAGYBRWcvwN2B4tpZA9GYXIZ_KGqMpVW2vC3q8re5P8utBxK7YuhGx15HCwg0ZxAKuWpWTdSsidPTD9S9dgrEwL8lQtvIh9lftGuRsmYoUUN5YEIKPGBPhr16XTAwglkaaXS3HhEFKbTI4XF314LGTDZTqm0U65uVyRXCwvU8XFsg4e4nCADw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de4e6346b4.mp4?token=CiSuMFop-rs6yISSxM2QP6Ow7x0V36qrTNpUhMT35c_G1rlUkNd5Ycw1DKr4Q9Cmn9Khj8oCq2abvcxWqB321olG5UmumvhSaXSkPABi49Ikc_i63SswXUMEEns3CoJWLbZjS-gJKqHV2IUeRE7pTNt4ma1FiCBHYhAGYBRWcvwN2B4tpZA9GYXIZ_KGqMpVW2vC3q8re5P8utBxK7YuhGx15HCwg0ZxAKuWpWTdSsidPTD9S9dgrEwL8lQtvIh9lftGuRsmYoUUN5YEIKPGBPhr16XTAwglkaaXS3HhEFKbTI4XF314LGTDZTqm0U65uVyRXCwvU8XFsg4e4nCADw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حضور مجتبی خامنه‌ای در مراسم
‼️
🔴
امشب، موقع برگزاری نماز میت برای علی خامنه‌ای تو مشهد، یه فرد با صورت پوشیده و ماسک، سمت راست تصویر و بین جمعیت دیده شد
🔴
اطراف این شخص هم چندین محافظ ایستاده بودن و همین موضوع باعث شد توجه خیلی از کاربران فضای مجازی بهش جلب بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/132958" target="_blank">📅 03:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132957">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
قبلیه بنی اسد یمن علیه آمریکا اعلان جنگ کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/132957" target="_blank">📅 02:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132956">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmRq0kHgsfFuGS_b-wDLixui7MsPSCkYGJEcOy0Nf9YM0_Pt7-Tmwtm_SsKFYQIl-CXGktdMc5wSbIRiD3G80qo171zzU9ECh0EFn2OqXsAwgH3VDvaQLm-FybRxK_ZlCS6VaHO6-rVZ5H7XqgduOfpxYuj5-0_gTKCYMGuPvQMX0q0XXjWx2OlCzW0oE455w0lIyZ9IPrVblzJEFvgOm6MxOdJJebsLixawdcMOHjQzZpSmAfPLQwjIX7DXoSc0LUpUq9wpixnHgkX_SjF-EgSX9atWLydygZiaUDGyOVl-Ffv3EyNnzNVNoMEycmxGJNjdyhbnWs9A7tIVwIcPMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام:
🔴
ادعا: رسانه‌های دولتی ایران مدعی هستند که عبور از تنگه هرمز فقط از مسیرهایی که ایران تعیین کرده، مجاز است.
🔴
واقعیت: ایران کنترل تنگه هرمز رو در اختیار نداره. از اوایل ماه مه تاکنون، نیروهای آمریکا به عبور موفق بیش از 800 کشتی تجاری و انتقال 380 میلیون بشکه نفت خام از این گذرگاه حیاتی تجارت بین‌المللی کمک کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/alonews/132956" target="_blank">📅 02:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132955">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
رویترز به نقل از یک مقام آمریکایی در امور ایران: واشنگتن همچنان به یافتن راه حل متعهد است و مذاکرات فنی ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/alonews/132955" target="_blank">📅 02:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132954">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c3af8da2d.mp4?token=n8gK0TaZTaA1bZzcqG1JnHcR0B1fbFgnqBxNHZvgfTypaDjD4pMOhlBsyQ5K6VRA5dTp3KaHH6TUwB_8HmsZlYaYZQ8KQ7vn78_hqI2RvH6dDtNgPeubtLxrhNxT00R60LCfHT9Ot_OkYV_u2AiqAuKmQsahseHH3lNyVCPi2tvFvkLqsl3ndIMqvKAxWvP1Cy4KoOmaeT3sHFrDoD5WoWMv8QDqyEDro4HlDGN571_i3ZNWigi7yjco9X_mvYVXxd25EZx4XGG8Ohp_t4kkHSHOk3zKiNMdyS8WO93URPfR9mBnKHWN9p37FpX9q7BCT-6L1UDlxc4XlSOE2vnTeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c3af8da2d.mp4?token=n8gK0TaZTaA1bZzcqG1JnHcR0B1fbFgnqBxNHZvgfTypaDjD4pMOhlBsyQ5K6VRA5dTp3KaHH6TUwB_8HmsZlYaYZQ8KQ7vn78_hqI2RvH6dDtNgPeubtLxrhNxT00R60LCfHT9Ot_OkYV_u2AiqAuKmQsahseHH3lNyVCPi2tvFvkLqsl3ndIMqvKAxWvP1Cy4KoOmaeT3sHFrDoD5WoWMv8QDqyEDro4HlDGN571_i3ZNWigi7yjco9X_mvYVXxd25EZx4XGG8Ohp_t4kkHSHOk3zKiNMdyS8WO93URPfR9mBnKHWN9p37FpX9q7BCT-6L1UDlxc4XlSOE2vnTeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مردم غزه گوشت‌های ارسالی سازمان ملل رو به دلیل ذبح غیراسلامی ریختن‌کف خیابون
✅
@AloNews</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/alonews/132954" target="_blank">📅 01:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132953">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MXwIdhSsFFprI_Dmsmap8bbIn_HKRsyvjCnkoE1E9RYyBnAfsm5mgsGid5zCLKCYEyEyyBjiGEhX6SsqcKp7mSP0JOzInL8SrfnpQzjcqh-4T3g45KH8n_fWGjy94jgliwZLOaj-nOyQLw5KP9zn7jb-2YFM2_4WL9IX8Jpz7_j_-rfGdUlhsSGaMoi4Ts3500kRgKL-V9GzP7qp8qKcJRdzmYdr8db7sm27Pge-qo-USss3G88ur8nJ869b8dW56E_zRPRXnR-BoUie3Nt1JpGfQCaGQzp8jz2dD6HMnYE3fhFVopmr6KqJM9Vjmum-_PBBT4RsoFzVcrRcXBYztg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون سید علی خامنه‌ای پس از ۱۳۱ روز، در مشهد، به خاک سپرده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/alonews/132953" target="_blank">📅 01:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132952">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d9ef6e045.mp4?token=SrAC89yOUNZh5zdbL0jsLFr7fddM7eeP9DvSRWa26zanW66mtVAga6XbQlt9-ji5Yqdp8QxKZneao2L5OkZvYe94jdIskGngguZjMtOTXBIeozgegVq5WKFl_u40lm06oyhweCl4N1J7XYYjf-iahCBNi8DTYqclDJglyAHiylBSq2AtQj6kOGB8cTUl0-VhrbF2B2uABvWqCL7uNylaRPvVfOvqzWtyIHM8_sVu-dUZ6T_u_Sjx1UVKg8E_VYVOKbhtvkFi32cao7FyGvjWHqiSh3sLLJ446qQpdoxzm7XOUZh8bgHaDSvdZxyDhqiGasMvekQAN-ZUZdIqbS0pNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d9ef6e045.mp4?token=SrAC89yOUNZh5zdbL0jsLFr7fddM7eeP9DvSRWa26zanW66mtVAga6XbQlt9-ji5Yqdp8QxKZneao2L5OkZvYe94jdIskGngguZjMtOTXBIeozgegVq5WKFl_u40lm06oyhweCl4N1J7XYYjf-iahCBNi8DTYqclDJglyAHiylBSq2AtQj6kOGB8cTUl0-VhrbF2B2uABvWqCL7uNylaRPvVfOvqzWtyIHM8_sVu-dUZ6T_u_Sjx1UVKg8E_VYVOKbhtvkFi32cao7FyGvjWHqiSh3sLLJ446qQpdoxzm7XOUZh8bgHaDSvdZxyDhqiGasMvekQAN-ZUZdIqbS0pNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مشهد به دار کشیده و سوزانده شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/alonews/132952" target="_blank">📅 01:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132950">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فووووری/نخستین تصویر از فرد تیرانداز
◀️
مشاهده عکس بدون سانسور</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/alonews/132950" target="_blank">📅 00:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132949">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtV1PVl5rxL7iP17XVaoiduh3EuQUlMt0_YvytcX9OCEJEnL57g8aTtydr-NGF9QZvSC0XNXyk33D5Kj30CPMC9Kv8v-2cHbQj2OKAHC8rr-XbJ-TT5pJTlaN79mVbNO4T0w8NbUWXMd5roT6ihyVSTl_d4GYsfa4VksttIkCM1aHkZUus6crr0nOnnTwUtva1B4eMWFfeQUG5G9lqqOfOWxb56wNCC1YTwtrwZnTa8Wsu7G0j0TfNYkNUg2S60O_bgwMnOhV2p4FlDS8gXJ0XBxPwQsi6xe2bSMAaijUwK8MBf37cbeOUwjbyJSfEk-Gt2e8e6QjMhlHRFom0DFrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/اولین تصاویر از پاسداران کشته شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/alonews/132949" target="_blank">📅 00:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132948">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
هم اکنون تماس تلفنی میان نتانیاهو و ترامپ.
✅
@AloNews</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/alonews/132948" target="_blank">📅 00:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132946">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i1a1QRi0Azl0RZqkYu0Z__fFW9zlsQT-QzU6rjHSm5PoFS5LIhWccLaKYpcGOfa8IdYCQdTFSv39-lJ4MJyG8g5p0VLhDFUN9X7uzzkzkBBnJv3pTioSCPIg91ShBVfnHmtutbzxGr1b5PXulRNqSvubx2OSVT5GLSdWh4oy0XHO0jGlKFqjxmsf7P7H3mBsA1K4A4XyxPIUhmRZ0_duxN5_NPhy6WA1jbbhZf_qip-fQuv8TwqHIpbpiNewn6VR1SLnnkCEPvsNoK4kvcv7VmKMtf4NuCo8IqOodYp3GaMAj_BOWM4SDD2UCPQW7Fl-fcj7OKv7vRS43w4WRYcMiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ul-BweJvTceMtV_U6RPC2EQ1oKvFj5Tnp4YNdoK8DyIctIxs-gsO0sGPXmTC9QtbQD4DWhGN35JVA4HLPldr4-kISKeS_GrSDWDslOUdtLPj7dpFeHcduOowhJhzsLAMtNsaBJFvWQ3ODr9BUADQMRt82Kxl5sxNZCESZ695CxZdPrkxeGoYdKG-H24TyMZG8dzEftpdaiyWenSnvMvxzn8VFbOrtnfFSGIR_MJ2WQjFOpsaMObG4c2LvGZhD9lLtFj1KiXpFxH__WeSENwot_3miZ2KgNB6KlI2GkRfRoEKZWeAtXMBKSdNzhAIDMvSWj64XKRlntp5kRKwyG1PxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
فوری/اولین تصاویر از پاسداران کشته شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/alonews/132946" target="_blank">📅 00:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132945">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHzELXH6yWcyYDAz6K6LoqvhjMQAp4o5GBzA2CNFNQ5I1mDSe_Tnn17SUR4V07PPEAH2r1K-oR2OyqZZJJCtQSy7O7dsWvUlnmM3aGj5uREkuoW9RIHbk6XwjB0AeGZqyQ7_cfwrANaofmj1eEo3P1xJXhJSym3Q9_ZAz6GaXQhOHSBZ6yCxepGm0q_Og5woN9VfNCuWSFewspaizIVPN5gugkQNBhLyiunj_PXLY40-0FTDh7ooUFValB76mtaMoVBhrOo8rUdcmkZn1OUQqZhNyHu9Z7KV5qh4pOzK9NyOGN9TkMaDQ6Whx3MXrK1joKIlcIaHXbNYzXf5EO9vMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امجد طاها؛ روزنامه‌نگار معروف عرب ۳ساعت قبل توئیت زد که۳ ساعت دیگه اتفاقات جالبی میفته و واقعا هم افتاد
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/alonews/132945" target="_blank">📅 00:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132944">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
افرادی که امشب به ایست بازرسی مشهد حمله کردن لباس نظامی به تن داشتند و بعد از زدن نیروهای امنیتی فرار کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/alonews/132944" target="_blank">📅 00:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132943">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فوری/گزارش تایید نشده از کشته شدن حداقل 3 نیروی سپاه در مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/alonews/132943" target="_blank">📅 00:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132942">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
فوری/تلفات بالا گزارش شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/alonews/132942" target="_blank">📅 00:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132941">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
فوری/یک فرد مسلح به کلاشینکف اعضای سپاه در یک ایست بازرسی در مشهد را به رگبار بست
✅
@AloNews</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/alonews/132941" target="_blank">📅 00:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132940">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
فوری/گزارشات تایید نشده از حمله به یک ایست بازرسی در مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/alonews/132940" target="_blank">📅 00:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132939">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
ادعای فارس: 45میلیون نفر به تشییع اومدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/alonews/132939" target="_blank">📅 00:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132938">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
فوری/گزارشات تایید نشده از حمله به یک ایست بازرسی در مشهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/alonews/132938" target="_blank">📅 00:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132937">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
آی۲۴ عبری:  عربستان سعودی در تلاش است تا اسرائیل را از پروژه کریدور اقتصادی هند -خاورمیانه-اروپا (IMEC) کنار گذاشته و مسیر آن را به سمت سوریه و ترکیه تغییر دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/alonews/132937" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132936">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
دفتر نتانیاهو: امروز یک تماس تلفنی بین نخست‌وزیر و رئیس‌جمهور ترامپ برقرار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/alonews/132936" target="_blank">📅 23:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132935">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
پاسخ ایران به بیانیه ناتو: اتهامات مطرح‌شده درباره برنامه هسته‌ای صلح‌آمیز ایران و وضعیت کشتیرانی در تنگه هرمز را بی‌اساس، سیاسی و مردود دانست.
🔴
برنامه هسته‌ای ایران کاملاً صلح‌آمیز بوده و ایران به‌عنوان عضو معاهده منع گسترش سلاح‌های هسته‌ای (NPT)، بارها اعلام کرده سلاح هسته‌ای هیچ جایگاهی در دکترین دفاعی کشور ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/alonews/132935" target="_blank">📅 23:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132934">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsAxjhmHrL9apngOHUvzEwZuHXdljb8hFVYL8oCF05WhncLgWDFOj_dNoz75YjmCk5vplgxkDkf5fNUr-gSgQizGSFits2IvkOt9fHzcSqk1vGh2XHrPC1Y_kADX84y7Qa4ZAwH5FS2aAu5UvAlF9C2IsLjMBuI__HpAfapi6wPXhDM9d3P89ixPVGJGEMKZVj-p464D68oXtvCv7NXq1elWHgEmb7JA1-W3Lr1sp-6B9_hg0I6CvEqUxvunRhONWnyB8yECFxutr5gwH1pOvn0y-cN2VUi8juf1SSOqw8zealUoDnXLkkfOuVYsUenZlOzsYh9QzqW0T0hLH0QRcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حجت الاسلام میرباقری: مشکلی نداره امام مجتبی(خامنه‌ای۲) هم مثل امام زمان به غیبت بره
✅
@AloNews</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/alonews/132934" target="_blank">📅 23:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132933">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
فرماندار کنارک: منطقه نظامی نیروی دریایی در دو مرحله هدف حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/132933" target="_blank">📅 23:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132932">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=UcwjdUEh2qxKqv2ABRASR9fRYeg0MnW44rwtbk1yRFdbPMTnltH_dSnb2TGXp_L939_eBuydEgy9Q_tRcFEBNIfF5YFIqNYs8SmudtZ1b_h6t8bfn-naz5znvfRedZ5J90sTNADiTe8hB_79_3MwopVI2UBSsEshe0OCrKXm0RlThAXoxmuJf_7gnBeK2odYpZ7EbJZFKIefl7qWbWOzyh4f9TStbWR1H0_urXAV-3e-isca1SlwWutg5SZ5odoY8Pgic2f4n1_wDqAzIftR-qc-wXVR6YDHo2AT7eVQ9b00eOHiACxs28KOCBeZwWspog9JrLyMJzdZkqt64We6HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=UcwjdUEh2qxKqv2ABRASR9fRYeg0MnW44rwtbk1yRFdbPMTnltH_dSnb2TGXp_L939_eBuydEgy9Q_tRcFEBNIfF5YFIqNYs8SmudtZ1b_h6t8bfn-naz5znvfRedZ5J90sTNADiTe8hB_79_3MwopVI2UBSsEshe0OCrKXm0RlThAXoxmuJf_7gnBeK2odYpZ7EbJZFKIefl7qWbWOzyh4f9TStbWR1H0_urXAV-3e-isca1SlwWutg5SZ5odoY8Pgic2f4n1_wDqAzIftR-qc-wXVR6YDHo2AT7eVQ9b00eOHiACxs28KOCBeZwWspog9JrLyMJzdZkqt64We6HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امشب تو مراسم تشییع تو مشهد یکی اومد علیه قالیباف و پزشکیان شعار بده که گونی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/alonews/132932" target="_blank">📅 23:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132931">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
دفتر نتانیاهو : ترامپ، نتانیاهو رو در جریان اقدام‌ها و تحرکات آمریکا علیه ایران قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/132931" target="_blank">📅 23:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132930">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiYrQdwoXEuZMRt-9Dhx2K7M7zldGi2pW7EqDnDQK33pCm7DNLfjo1oNzucpeaziidTJOsS4odfogV8Buina4kBlXjuLkYk6Uqhq3HO9ehutG49taswKE3hBQtpFRv-iZIGBt1Vx9tAXk0c5NnJsPugmrhXuadv5H3gqKD2JJXVJr9mDzVPfgc9c6XCeicEiAU5r8zr_synLGV3oWW8PNkQ8NbFZgt0umHidw5E-8-75LwPMGS1S40LZLHHVOg7RKayHrbBXnCHoVN2hruF8xrSJL36674r3Yk6qpiHuDCLnC2CzTLW-S5SeAF3YzpfP4bpeWiJNUvmGqOu76atPSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اختلال شدید GPS در سواحل عربستان سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/132930" target="_blank">📅 23:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132929">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kOI3jOE_emzU42KFdjrvy88rI8N4vKK4fdEHcGwIk3KvxQg9GcPV_YjALZqRHny72f8Tie6-CiAq79v2xvy5Tv-z-nuB7sIsREm6PXC0h7v6LHxCQmpE5YhC8uSDDpWT9d8iQOW7iUfFoiNC71Xeez26fijA7qL4D6YI_l_igyteLqDJxnd3_8HY0ADKwAbz3H5PjHi8Gf2tHcSFj54fS4RfgwDrOxtj-e15Fj9S_Ga976xOCJYyuHpO_M6ZFVjuhVBiAXxsv31_v9C9GwhGFuEep4X1tARKEL6DP6dawRqpGWFWciwsAdEVOiusp022uYMpiShvISHjD95f7SH_pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رصد اتش سوزی در بندر عسلویه توسط ماهواره جاسوسی اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/alonews/132929" target="_blank">📅 23:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132928">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
خبرگزاری ایرنا :  یه پایگاه نظامی تو حومه شهر بوشهر مورد حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/132928" target="_blank">📅 23:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132927">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgcqCcU2AmaDzjt4TRiZy09KmBUj_KcrVwq0LJAGF2x5w7VGxUGwzNVxv0Qq1Qv8h2wbTpTirlX2KpS9gPlAL4ViuXT5OuEGibY9GH8Fw7tDyL_Oyf7M49UNRPskxcXu1xJsrjNWs-DMRCrvbnpqWliKHred-sLfgWbjnc0xDxzq5qbn7aB71LbRuUVxI9lLQSIZDs7nDxriFaY2J1AjwfnbqTYXyx23Xc79X8zCAeOrrhuhEkKc0FVrrOAG0DIvlPisTbo73WpXXwYvm-p8uIu6uKWJa8NoeZhKCfs6Lt0-2-Rq3QNYRppaIs0qxgOOJCit1b2rE4qgg5dlTwiDrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اردوغان: من معتقدم که گفتگوهای سازنده و مثبتی که با رئیس‌جمهور ایالات متحده، دونالد ترامپ، داشتیم، به نتایج ملموسی منجر خواهد شد که انتظارات کشور ما را در صنعت دفاعی، به ویژه در رابطه با هواپیمای جنگنده ملی ما، "کان"، و برنامه "اف-35" برآورده می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/alonews/132927" target="_blank">📅 23:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132926">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ایرنا: صدای انفجار شنیده شده در بوشهر متاثر از واکنش پدافند هوایی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/alonews/132926" target="_blank">📅 22:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132925">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
فیدان: آتش‌بس میان ایران و آمریکا پایان نیافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/132925" target="_blank">📅 22:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132924">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">از بندرعباس فقط عباس مونده
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/alonews/132924" target="_blank">📅 22:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132923">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">💢
فوووووووووری/پرواز جنگنده‌های اسرائیلی به مقصد نامعلوم
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/132923" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132922">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWNHInSj0Gr5ogGweoZdnyfhmknfTFrarXsaI3i3u-9OZ8GKYBQqfE9EPlR9nUMAnWyykRS9wtTcL9SRTEV_0hYVVPhZThBH79oOPvNPKl0IVQ3tmFJvWsE3XL_qVP_35i8W3UBo0ygV236FslFH3SpKCmrGxr7M7VzvB33Kgk2o6YcyYQY6RSX2vabdlAE0fWmjdTVmoNlBatgXt406hGH10lSCHi9RV_xQOdk3o_W3Gc_Hm9A-wtrTY5Ss50sY7QcndKFkCAYV1AOXtMNIPfymtHUhii625ZMkEpJrcFp12qUtuPSO_gdkAHcSNBbpp6FuaHaIowCCfPbxPvq8LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از اتاق عملیات کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/alonews/132922" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
