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
<img src="https://cdn4.telesco.pe/file/DhagzxL07yQhsjYeVb6Gs0aKX4GzOiQdpKhqv-EjXOUxuHVS55sxq4mM5JXB9cvkAAorSaJU1cVQ4ls4AYxarIGINnruzNKjr2rjVoDK43vWQ_dG6GB_M_NBlzEygyi92G2-TzbamMu6BJVLiKekOB6i0-DH0kVir0RziioBAAOKDXrFwAS30QYKRYmaP4e16SfwGy4lBmwUkfk0kt94upjrDDcamoX_rN70jGsTJ-Y_13HF5EJ56gb04UKFPDAb8Wfn9_3TURZVRd3p7R9dT5wZuvHX2YcnkDnjCfT9r-S8MgRxPtRWQu3xGdkNZwzkuMulOBSYX4jB1ZleeQAfRw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 11:37:42</div>
<hr>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=AM5aqFRw48bWB3Aug0gRhMlTLAP7WdvAd8VUYcgBJMIUlH2HWvhoobesVRdDp8q5L74GzzV8gMUKUMXySSfhNHWGWmDogwnWFncWrbKMMXPKtBM_FgcEwoaAFb0rxk9MKzUH5WUvEDP4VvqSApvqCS3rda9MIDMuhCUYhrA9kSCr4gqCYB_wtuYAaf_bGd45aRCQ98iU9L8DIthkTNpTsEevNN5nqQh98O1lzowGUP_mJc0EXW3XGAYB9rju0yEvG9bTvCWqmuCqjo3fixjWKJVAm_xtw0evH2e_8nur7Cq89Ir0cLAi1ryG6TugqzHluikFbVnw2aJYUKfkesrNcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=AM5aqFRw48bWB3Aug0gRhMlTLAP7WdvAd8VUYcgBJMIUlH2HWvhoobesVRdDp8q5L74GzzV8gMUKUMXySSfhNHWGWmDogwnWFncWrbKMMXPKtBM_FgcEwoaAFb0rxk9MKzUH5WUvEDP4VvqSApvqCS3rda9MIDMuhCUYhrA9kSCr4gqCYB_wtuYAaf_bGd45aRCQ98iU9L8DIthkTNpTsEevNN5nqQh98O1lzowGUP_mJc0EXW3XGAYB9rju0yEvG9bTvCWqmuCqjo3fixjWKJVAm_xtw0evH2e_8nur7Cq89Ir0cLAi1ryG6TugqzHluikFbVnw2aJYUKfkesrNcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okuTdKje8YFPAFaFtT8iK04tvGrvGBhCNweAigICTl9Ss3tUNEnsWFHD3T8lwxrziHEaL7O7HnifRaA5bKCU7hyJUfEPc9iO6bvbB1i9qyudjd762YYstJ-EEWxNljb0gQnRllat5LadLyshVFo7sPM7NMe3zPLXFpfSXZAsodvNPMUf1xwvDbM37nYdMMJxWqkLYVArVb0icyZcVGKPskPw-fT6JP17nxMInNiwrkuKv0thzA7i_SuzJn1ATvKYmWRnFk2A1elhgbvJXmYlTQ7VlmXkZsGZZGdFrvsrLBoV1rgq-UQuOLIJACpGEZexpFm7kscXgtjXwtPOLpbedw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6HOGWW58Ca8r-IfC0ijyKWBEbOMY0OfGjz7IobZkHa-aFb8m-FOHAs580oxjfI-FLULgtoG-ornyIyE6DwdizY-8jXfwlEU96jGIkjEhRK4-uB62C8Uu5FxtP6EM3yTYj805it_LJZM-BBU2IGV_xlASohq3YLaMouLrpXlq4FtHiw97YPKktgC_kN5p2NOltNH62ffMmoGfdHTK4ISX_vAd0Kfe6QcXpqMmstJ5pXI4LRBg_Jxu9qhLbRR6MenRjkUEj8p4K7e3tUIDy73L7ZcW6eOrH_r_hmBpUgANFCbiO-dcOY_CuyWzvk9QIU9TO2DfIrggBBt5vWDe1aHzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sDHceAws_DgHKJfPyxY_hbQFOKydTvRD8S_cgOocirT6Wx-ywl0KRXHQf6OhMNN3zocsp_m-f-qXQ5LsVUrIyAVJFqfaNc5rw6pss_ec7QVWAkSntWb2KwTWP8YwjbBOOMihz8GGAkNdJ8ch25z8QrdZado7tnLzBnW5Qe5efpv584P6L5_V7miT_QLG-SBABYenMKGWGB1YzjZ8woeN7pf2VImgkxl39Tm3qZ9YAEcN39WQJMSSSDCbPBI85r5LMCrbsCFz60xSY9D4pxmoZcKLUvjGJq3yRKS9pgyas2mT1tB2gou46k1MEs9KDv2QarRE2KF4-LjKR8PvP9KJuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JQTm-GORMQsHyoQA2Jfe9odBDfnVbM5wg4V5gYjcyBNcP5-N-mcPzn6CoE9Wb0cNKNhboYrr5VmCWpbBjgOua9Da7F7pXnc9pWvx_vqb95Pfy8J98qtAB8y40-DEhbThH_fxPQLv2PYX4I9L13zNe27kGLwMlHl-GrBtyRKIA5R91UYA6PSdBGFbhCoCpBOhNRMWNP6cblMKBmYyAMdgwixCp0ghnR92N84suRuHUGRzNK65D8nvMayKqteTQavqfCoYy5TsGTJYAM7_EJxKtZl9BRA_QIDnyWNICKImpt4obdRBKdmm2EDSgv7fODc27_CpxORuOeWjHQR4hFgyyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
یک نظامی آمریکایی در عراق کشته شد
به‌ گزارش سنتکام :
یک نظامی آمریکایی در شمال عراق دیروز  ۱۸ ژوئیه، هنگام انجام عملیات انفجار کنترل‌شده مهمات منفجرنشده باقی‌مانده از یک پهپاد تهاجمی یک‌طرفه ایرانی که سرنگون شده بود، در جریان عملیات کشته شد.
روز گذشته نیز سنتکام اعلام کرد که در پی حمله ایران در تاریخ ۱۷ ژوئیه،
دو نظامی آمریکایی در اردن کشته شدند و یک نظامی دیگر در وضعیت مفقودی قرار دارد
.
پس از یک عملیات جست‌وجوی گسترده، نیروهای ارتش آمریکا امروز بقایای ناشناس یک فرد را در محل حادثه پیدا کردند. روند بررسی برای تأیید هویت این بقایا همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIOQVfZhz0XXHmouuOFUMaUiXc2QtDnpHgcvJ_6lMyLvPvs8vAbQMS96y4x7Fu4lDImcltyaeO8qcsieUdVVrjqKvLhVz07RWiYvEFnCkc5oEGMA-lLoYN5cDatcaY-zGj6oPI7Qm46NNOvRDBhCi4U1Jlq8OEUBy_4XnOo1zaqrfKEbt0K5KwyvFFMkdEg4g67rxaIVirQN9_0UIn_o8wFWi8hihh2gx97z3j5bs0XutuWDNU7b4xStT6ya4yX8-Ag8dIL_Q6WPFsMnI9tyJXPXa5_fgJOgJpUDHnJ7_LSTh7ubMeAxPL1wUlAXvn9ggmQQZSi1SaUNzFZR-02frg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyuCq6tEiv8NQL36SMUIf6ZA9QmVBh8SCbwnL5bDZah_QiIqzuYa2DZqZUYv6w2wlal-eKGaYKY_bgFyXVslqJCEQlIxO2p0mgaDotC9QI6xJ6TgWcRy7yfZ_Eao7vev0eRndXnW3uzS3FgHwfbe24eB0Oham2-4aRyTdUaqFg_u2xvjHlvzEywVAs-V7t2-T5B9Od0diDdmUHH6fgZkL994Hn6-t58TdqGgq0md9BETc67g3OVakxf466Vp6v23kWISRTizM719UWroRY-PA8av6oi2Jh262UPS6QRsr8lCNK-tDOR7H1x6OiKC9Zp5tDWw2PIzBWQd_Ep3RirYgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر گروه تروریستی حزب‌الله
به وبسایت خامنه‌ای :
خامنه‌ای گفته بود سوریه
ستون خیمه مقاومت است!
امروز نه از خامنه‌ای خبری است،
نه از نصرالله نه از بشار اسد و خیمه‌اش!
ظاهرا ستونش رو برای
بازماندگانشون نگه داشتن :)
یک «هفت اکتبر » راه انداختن و همگی با هم رفتن!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6259" target="_blank">📅 20:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKb2WoAYB2BfZWkNY37IBbkbjJc4SIQ1g5XruVQSrsNKs3qgofww7iRVf2qoHSMHt6t6iMSSSuI5_6vfGuhUR14Gj-tuEAUG7WOMbKyyWwtPM770N2Kf7em2Ts-reWnN13h58cs7C2vy2zGJaFZBJg9S4K7sWOw2xdY7vpCzU8FrGrZBPb4ZBv2JGSw1BdmJmBzcJ5JxWICl5QqD8l_FZ-hXN96hAPs-knwNk1QmApMnpJMp45YZSZiJZLYuw5X3NAHMPzlMKAR0HCu4nBM-LypbT-i9VR58PTd4ID9ZsTDQmszlfFOJ-ihl0o_I2WCB1dabJaw2OWhHUsecid3pIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای ۶ اسفند ۱۳۹۷ در دیدار با بشار اسد : «جنابعالی با ایستادگی که از خود نشان دادید به
قهرمان جهان عرب
تبدیل شدید و
مقاومت در منطقه به‌ وسیله شما قدرت و آبروی بیشتری یافت
.» !
قهرمان جهان عرب!
که مقاومت به وسیله او در منطقه قدرت و آبرو یافت! امروز در مسکو به سر میبره و حتی در تشییع جنازه خامنه‌ای هم شرکت نکرد!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6258" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6257">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=iGQ7uWuF4IVbYvQBAeK_vgUaE4-VNFQ-gV4mPYw-ZFL1BaoWz9I2FloV4rf_Nb-or4n6ZX_ASuO4PB_sbhewHP8KNgWxRZolYOvUNmd9Htb3L8I0ip88MHjoNBWAp2NrHrVaIJTUx4Ercy8-le1pv5vPWBeuAzXtfRMjtQ0Tp1BWQwW_6O7iTm2aTlcqp4IiWUxYpgENc_Q7iAHgYrtNgW8U4d9XRbCo-Hp8HovZiLInUONHY6yLY4vQtwVBcwX2ov4-WUGR1Ow6-de4wxvWnWr0bUsQm3glRxV042sOZlWAaYpgMCx3qzd5UofghkrX5Ahne90_XWKjZUrhfYeQcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=iGQ7uWuF4IVbYvQBAeK_vgUaE4-VNFQ-gV4mPYw-ZFL1BaoWz9I2FloV4rf_Nb-or4n6ZX_ASuO4PB_sbhewHP8KNgWxRZolYOvUNmd9Htb3L8I0ip88MHjoNBWAp2NrHrVaIJTUx4Ercy8-le1pv5vPWBeuAzXtfRMjtQ0Tp1BWQwW_6O7iTm2aTlcqp4IiWUxYpgENc_Q7iAHgYrtNgW8U4d9XRbCo-Hp8HovZiLInUONHY6yLY4vQtwVBcwX2ov4-WUGR1Ow6-de4wxvWnWr0bUsQm3glRxV042sOZlWAaYpgMCx3qzd5UofghkrX5Ahne90_XWKjZUrhfYeQcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltal-iHqkU0t-EHVYH8ZhpAgiCYVDQtn3wBr7TH3XJndSFkvIyRCPZ7zD4r5YX4kbOKH1uxuN0aLUrdvaiiZTEoSzNZpoffNDc2_btwlxDopv2nx1EuZK7zQKhImefrntwGTuCWlVk8JL3jrKujqo28IxRtltUndl-jkDKS6HthSH3-KuA9yb7C_HZNa1CcmWzIbu_YSpKmlDbatnlbpWPi5RndPAmT28vdaaz_DHYC652KN-h6kuBlgGPP0mmG6N1O3jrbzsdTdyzK9fn6dqim164x3MJ5s6xVPdUukpyCJQxYlLT0On-Pej-4U6cNmNE8H4PAstP0gws1XZx8qzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=pjKFM_g2BzC6PkoJ_mpKjPzwJXBmwAeTlKUK2QYYEQuyj8kZq69a2eMQBnLal6gUe1r28kiwkZO7M6NkxlFU4sALXxrnOHWSvf6aYqygft9k_YfycmtwU5q4hLkKQv5OsDR-T91ThEqRiuzGrJL0e5x2uyh1JGP_B-ygBlG02Qp1Jq6DtHm5D8T6yOgjOM1b-rQ-LiBfLSwlz6xN9sRXN1ZOOyYHC8K-GTSCFsbLXDDpUEvZp1e1RMvhEOvLfGepNv9PWYlosPwZlT3NmZtuLC7GhnX5wyR6137xsZXJBw9iFj0IMVWiCZt5dMAq-wisEvqmcLmnV5bslAI8TrvHJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=pjKFM_g2BzC6PkoJ_mpKjPzwJXBmwAeTlKUK2QYYEQuyj8kZq69a2eMQBnLal6gUe1r28kiwkZO7M6NkxlFU4sALXxrnOHWSvf6aYqygft9k_YfycmtwU5q4hLkKQv5OsDR-T91ThEqRiuzGrJL0e5x2uyh1JGP_B-ygBlG02Qp1Jq6DtHm5D8T6yOgjOM1b-rQ-LiBfLSwlz6xN9sRXN1ZOOyYHC8K-GTSCFsbLXDDpUEvZp1e1RMvhEOvLfGepNv9PWYlosPwZlT3NmZtuLC7GhnX5wyR6137xsZXJBw9iFj0IMVWiCZt5dMAq-wisEvqmcLmnV5bslAI8TrvHJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-poll">
<h4>📊 دوست داری کدوم تیم برنده بشه؟</h4>
<ul>
<li>✓ اسپانیا</li>
<li>✓ آرژانتین</li>
</ul>
</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6254" target="_blank">📅 19:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vePYIbbQEwynV-7B2RkzH5C3mr1Q5w7kHCHnK5PJCd4YY06NF-GY1o3h0SRArCsTzRt107NdjpYHEWMaBlBWQkbdv6njrX2PfAUMWv6v3SKai2D-jrv65yfZNIkT_aBoJpLZcvDp8_682xnjfPcM7Fq8DlbjmgKtfsky4QJ9qBG7rfJ9KAeSmqzbhu6OmqaE6aaTsvMaaFV9QCuPdooG3e8nEVJLsMcj81Gy2F87sHjCkO8tDh6ptnOup3dDPV03QCqG7_ftwwcbl2NVoWuEOmSdMsYlkchfJ1VOgBch7Tf-UqOX_lnRaczn-AcQZ8eO1ERyN9WRePy2hx2pA-iZ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نتایج دیدارهای آرژانتین و اسپانیا تاکنون،
۶ بار اسپانیا برنده شده و ۶ بار  آرژانتین
و ۲ بار هم مساوی شدند.
🔺
از اونجایی که تیم ایتالیا سااالهاست!
که دیگه توی جام جهانی نیست،
و از اونجایی که نیمی از مردم آرژانتین
ایتالیایی هستند، اغلب ایتالیایی‌ها
علاقمند به پیروزی تیم آرژانتین هستند.
🔺
آرژانتین ۳۰۰ سال، بخشی از اسپانیا بوده،
و زبانش هم‌ اسپانیایی است.
🔺
نام پایتختش (بوینس آیرس) اما از منطقه‌ای در ایتالیاست (جزیره ساردنیا)
🔺
گاه برای شوخی به آرژانتینی‌ها میگن : «ایتالیایی‌هایی هستند که اسپانیایی حرف میزنند»، فرهنگ غذایی، صحبت کردن به دست، تلفظ کلمات و آهنگ زبان و….. متاثر از ایتالیا است
🔺
پیش‌بینی برد اسپانیا ۵۸٪ و آرژانتین ۴۲٪  است.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGL28nxqRl72dzJvRCB1QjfSfvzXqXHyOQ-TSOsFSyWdNUimWAwq0dNuOlUuPdbqr1VpstCOOcxlW9d3lllg0Sa55tcidKvAs4DHxy7jPUTH9TxDgbyK6UkofC237gxdTbfKzclOez6r0ydNp0LvlgPsus-uLlnZ_e9O7Co6LZIOdCGqZtRFlFtIKGdaXgob9Cdr_FSIyBju3rPuAWDPdrzWBcBi8clna0ahmSqiQRSruOQ6KKaiYDUstVlqJ-OBPS1JBL2fGWnwhX416irY7XjV2BFRxmu32abwX6krQfIoSDXeLV9NmglSPCpHO_V0wtT1PT5heNWgQ51eqjacFWdk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGL28nxqRl72dzJvRCB1QjfSfvzXqXHyOQ-TSOsFSyWdNUimWAwq0dNuOlUuPdbqr1VpstCOOcxlW9d3lllg0Sa55tcidKvAs4DHxy7jPUTH9TxDgbyK6UkofC237gxdTbfKzclOez6r0ydNp0LvlgPsus-uLlnZ_e9O7Co6LZIOdCGqZtRFlFtIKGdaXgob9Cdr_FSIyBju3rPuAWDPdrzWBcBi8clna0ahmSqiQRSruOQ6KKaiYDUstVlqJ-OBPS1JBL2fGWnwhX416irY7XjV2BFRxmu32abwX6krQfIoSDXeLV9NmglSPCpHO_V0wtT1PT5heNWgQ51eqjacFWdk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی وزیر خارجه جمهوری اسلامی :
[ در این ۱۳۵ روز ] تاکنون مجتبی خامنه‌ای را ندیده‌ام
!
خیلی مهم بود این پیام را به دنیا بدهیم که سیاست‌های ما تغییر نکرده و تغییر نخواهد کرد.
درست میگه، جمهوری اسلامی هیچ وقت اصلاح نمیشه! نه با انتخابات، نه با اعتراضات و کشته‌های زیاد، نه جنگ.
تا باشه همینه!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=NAFJtT3zz_ZCpAXOod8HoER1UO_jxXFb1-cWMuScsEJc6909wYikC9suYK3cT98sVfEst2HfrO1ipFCPUbyCFUBnRgBCS8AySS8UYW4rm_lWsVo5MwOZAh0h01zfK-wCEkbycdgFX8PcYMs11ddSXBxXipGVQCXZ7g8zZrWdnsyYzcvVcSzPXDMLPGXJU-6hzWlzRezqSMjYR0yagp1-1JFewIi3ihLQKYuXixfVzh6H-lO5EHBHSzoprh6tFQGkh45WhvPMrTevyRZIRfPguaa72hlT7n2hmh6_YzGXgCc7Z8cZ46LvAa5zBvTDNFMjoMKZXRkNAw-EO1FIR58cCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=NAFJtT3zz_ZCpAXOod8HoER1UO_jxXFb1-cWMuScsEJc6909wYikC9suYK3cT98sVfEst2HfrO1ipFCPUbyCFUBnRgBCS8AySS8UYW4rm_lWsVo5MwOZAh0h01zfK-wCEkbycdgFX8PcYMs11ddSXBxXipGVQCXZ7g8zZrWdnsyYzcvVcSzPXDMLPGXJU-6hzWlzRezqSMjYR0yagp1-1JFewIi3ihLQKYuXixfVzh6H-lO5EHBHSzoprh6tFQGkh45WhvPMrTevyRZIRfPguaa72hlT7n2hmh6_YzGXgCc7Z8cZ46LvAa5zBvTDNFMjoMKZXRkNAw-EO1FIR58cCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BXC5Ix_IXsg9CsdsepoYgyEF-EXknSmsTkR-sjq4z8BDN9eeM6Hcvr7cU-pKcXL5HUcH8V12buag7yNQiHB2Ix9z32qN-3raXzLtxP1VJPUl3fweVtoeCQMWcK2ooHSIYgJ6t6LU1zCBQJJtO5v4vl9p1_NZ2Z9Rf2IFwsyV4QNjYJMrdFDsZTK-0fRnhtfd5679dE1gMfRcONBQw-CV9CIqJOopRUZK1XbRM4ZCi4zDQUAaHnmcWn-oQMboD0gZyfsk-GfZF3hYPV1u8naqxw4voSnAkxE5log14WpntcO3cndWgaeL1-P5_fwZnCqPmvPFVTpt1dYqqwZSFahSBlM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BXC5Ix_IXsg9CsdsepoYgyEF-EXknSmsTkR-sjq4z8BDN9eeM6Hcvr7cU-pKcXL5HUcH8V12buag7yNQiHB2Ix9z32qN-3raXzLtxP1VJPUl3fweVtoeCQMWcK2ooHSIYgJ6t6LU1zCBQJJtO5v4vl9p1_NZ2Z9Rf2IFwsyV4QNjYJMrdFDsZTK-0fRnhtfd5679dE1gMfRcONBQw-CV9CIqJOopRUZK1XbRM4ZCi4zDQUAaHnmcWn-oQMboD0gZyfsk-GfZF3hYPV1u8naqxw4voSnAkxE5log14WpntcO3cndWgaeL1-P5_fwZnCqPmvPFVTpt1dYqqwZSFahSBlM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار غلامعلی رشید ، فرمانده قرارگاه مرکزی خاتم (مسئول اصلی جنگ) که در جنگ ۱۲ روزه به دست اسرائیل کشته شد:
«زمان شاه فضا چنان  پر از خوف و رعب و وحشتی بود که حمل یک سلاح! یک سلاح ، دشوار بود! »
برای «دینامیت» افتادن زندان
و بعدهم آزاد شدن!
توی حکومت اسلامی ولی برای آتش زدن
سطل آشغال و یا داشتن سنگ در دست
حکم اعدام دادن.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6248" target="_blank">📅 17:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCvSTOYx0zKLF6l_OFyPakkn2mIljlAQ2ei1ijJNIOnMpO6xaZnv4HyU4NOOPb9DsmNH6A742oDAcg7myl5cYjcUh41dcTXPkl9NQ2ttOaIYpqXYhnwzc0ojH39gBYH0zKrTPD2GMgmwLRLIXNn5lZxeBhwhDrZbu1nW9caz59WbNV8ZpU-MY5tl5E8ajtUmg0QZjFeJ8eYR-LMARvphq0A4xgENyxI33uCge6fS5GDlw5svNmLNklBik2fhNgL2MpIvrBv1OJhoHCxDez6Uv_t6t6Xxurhw7bIrmsSO4uTfKGLbZ4ofTk7ei8NuevxjRE0WCp3yNGMGSXOkXU-xow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrbvwW5TFtN1xp5JsOyer-DdQvSbUfRuv19jr0R9qkQUDpk1TUOn5-PGGVZxwpSPlGE1cdjxXV42L1aehjOP-69ckQhXGMMr1mFhDY4bytXZTVwByDklhnNR3lEoF_dV3VL9FOBeOWY_aPf_ZyHkPuMbzRBDjMHxomcbVOfUwi0sDQDnFvdn2GGn0INtr2-74PenIpDe_BxhZhg_RYyHLRiUB57OoHWqAyOZQ_9NB5OBq0T6KxAIj9WYlLaN6WI-dT4CtfhtikNBI3RqcoOoUu5Ub7yOT3gWnQHNCsOE29jC14mT3uHaHITZFLsJtVZ7L7yfh50X01h1JMEsP8GZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Td9i8uvGwxLXeXqyRK_7BL_11V8XGhy28qSqHQg48UtHBNy_9F8dBJdmZWN9gzmqQVrYEGjMcJ4XTsBAWBnbfGUeAHCrWZXCO5H0jXHw26fdrjGhZcf4I4N3W31YDLQoJw_uMN_WiIR86Mssj4NQ9Lmxfr8y4Lx3r9z-bwTac9djpM769DoyQfqukwwKa0C7JkGiNhCqlxc71U66CP3Fk4YQ4GYBjFIxDPyc-pogRYaCIFihw48uCsKTs7JShFyGGlF4PD1K63cO091sniRQii5_Qr_iyz_jRCXNjzfMC_is_W1vt0Ephu-kSDHmZoYaGup70WALWM6oi7H8pcPg8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
‏
آغاز دور تازه حملات آمریکا در نهمین شب حملات
اطلاعیه سنتکام : «امروز ساعت 6 بعد از ظهر به وقت شرق آمریکا ، ( ۱:۳۰ بامداد به وقت ایران) ، نیروهای آمریکایی حملات هوایی جدیدی را علیه ایران به دستور فرمانده کل قوا آغاز کردند.
این حملات برای کاهش بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و
مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی
که دیشب به نیروهای آمریکایی در اردن حمله کردند، طراحی شده است.»</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6237" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">فرداشب اسپانیا و آرژانتین
در مرحله نهایی جام جهانی
به مصاف هم میرن.
در یکسال اخیر، دولت اسپانیا به یکی
از مهم‌ترین منتقدین اسرائیل
و دولت آرژانتین به یکی از مهم‌ترین مدافعین اسرائیل تبدیل شده‌اند.
نتانیاهو در دیدار با سفیر آرژانتین
گفت که فردا از آرژانتین حمایت خواهیم کرد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6236" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6235">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cq4CZ1apj11KAd3wsQpOP_pT25HNXmBsaAba_Sa4MFjyTuWYyYuOcdkautv4yWWX4eYGkU6EUqcHbhUUCQfAVeAGmyXpE74MM0hHpxY2BLf8H4O5J_pNItjjkJqXnDz4Hr_t5Y6Ja30A0kes47e3E5ui0ZrzlEzLm93yKE3F46FPNPnqAmkpnDXDUiQqNJCyQkb7-3ZeVjHpcG-56gXGMVKcShzn7asifF_pfZiGjlKG2BMbxZ4Rd9iu4sumAna-8pEQPC2PRWLi51gt5BG_74uENSmDx6mVEQ6yebodOFaT9mLKjviyBU9UFM5rRYz0qQ3muZ9OR4GLIu4ynZsp5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pl6jo-Jnh05x95gSSdIEIChndYRcIUXO46QKAtkml6V7QchvTsu_8xztTa5aa_ZeQGAVw9Nsn2ZVqyWrAv_dOMBHk-LIUUkX73GyytWMggND63goKtGWkCgMcEthhWn-_R_kbm8NEA58gWOPlhgf3thM1VTF_DVpgwaFGbr0JWF70zEmcwsa9-RdIzm5L-nhqGinFCjuT7mnlQ36kaa9moGee_L68gik4t2okpyVJmB-zVYag7JrrglRPcxFSidkqnMAhf51zed_fySwUA9UqYI2zm3B1HyAZ3Fs76UdUnCj4xseGaVZc7t1AgXQGBpo7EVeshhAdKd6GxpeyGC19g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXvrvd9OGqJj75e4NYSEUMbUFHid5Yx4sV41qybk1uyi8FSEeWwXEoHePNTCAQurxr-O34BiwIpzwNtA6I2d_k8pxc_pfYjnFISMCQ1TOJVTDaPUu2SqZ-9yLxhMXUceIaFYvNdicwhRaBMio2gRVqATYqpZI92_ChqJ4znEWoSkQKqzCZC0uP6p9NGRIt-ywYVJoo7JdyU_9XpSyqgK8X0zLsSp48h0BafY7s_D4UyAbpolZG0K4cT30MuCSY0kt3sQGMDNLxGpH3x66WFvuxes3gdD1sjt0YXlxaa1Qi3KWVC3WaCtRp0mRCCn_M614sdNF5cN1ukZkPnGWxgRXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-6L5K8NUO_peFtMihg0k4aTZFZ0UpcDQ2ACwPC0K16ofj6hlMA0MQKpn_ihHd9ftuQ7VNvuePGP0CBJRZTeAE1jKo3dd1P6XxDy-GvjvQysRtu3nDF8-tahLxY4fXKwEWp0zrM01ibfjCvuCw9B1bgDVXPMnkaNa5diPqwEaJM2fx7uVpUc01ZBVaMkifP1J4UyK8C-zbGl-9nerQB70G1spzg4IobIc7DIlzpHWgFwttqYvpeSge4KUJhjTg8LFeYTrPIQssKHdXg_k3OCo-Jz90_JV4wdvHitVLw10u0_mZbWV6_lCAA0Ir5jWKZFLlBRtEeccEeIoxKaXuuK6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIUrfD2Vs9shJasfXDPbh__udNzLCKJdWsI3HZxPPuDwJzXUqXNxPxUHhJEDpuodYdqSD-JfMIxgIdTzh-m5mrO_cim7AkKAfRMLNcCyw8t-K8Eoonv5PoCeI8mCj67kesgysGkXiZxKXSdkYifdcXP6wAssDT-LVZu3OeQOCHLMtlwCAV5Ln-pLnrmSAr0Ow3iqkQU_gy7oaUdfzuMU1z4RPSa7Hv3zkAJpkQu5wQpbhQMETwkdd43qKxMEH3LGPaQ1gZY4FVPoJvCsrKG1YVXcnvArOfneB08pLM5_pUA28SqTb6tg7sJ_YXoZt4J0VlZO_amSjMEfQADbLXYb3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2Zkz2QXaaghYbD2mA8WsGK3m7H8_adB4IV8AAzH4hyAEt1Ht0WSNRdvY5AS-1BcKM0EOlxHKRmRA0m1BVK5Av_3dnSvc8ApWFAzpRDFrWdJYZd5GvVwVgChLH0zxfarZaOHOJ-wx0Dkte8OccBW0Es9DkLmZe2b-FJJEq7rELA1jUxFt6OJX3w5JJFTMXpdgNrB2x2AeCNV9nLRAd-GCxAFNkOIgyH6WKp1fO4hsKS1JW95uFRf_cL8J8dnDEpceBFHImM3kSkOGFdboAdeJGrnIdEiQYuy3B3rSJfYM-wuvPtZB21WDT7Viq6arjS7FgHxpkFTkVIALrL_xrYjew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استادیوم ۱۵ هزار نفری «بنت جبیل»
در جنوب لبنان که با هزینه ایران ساخته شد.
این همان ورزشگاهی است که
حسن نصرالله، رهبر گروه تروریستی حزب‌الله لبنان در آنجا در یک سخنرانی گفت «اسرائیل از خانه عنکبوت سست‌تر است.»
همان ورزشگاهی است که احمدی‌نژاد در سال ۲۰۱۰ در آنجا سخنرانی کرد و گفت : « تمام جهان باید بداند که صهیونیست‌ها از بین خواهند رفت.»
امروز نه خامنه‌ای وجود داره،
نه حسن نصرالله و نه استادیوم!
و احمدی‌نژاد هم متهم به همکاری با اسرائیل شده است.
در
تهران اما شعار می‌دهند که جنوب لبنان
الگو و اسوه‌ای است برای جنوب ایران
.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6227" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
پیام منتسب به مجتبا خامنه‌ای : نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد. برای دشمن آمریکایی درس‌های فراموش‌نشدنی داریم.
احتمالا به مجتبی نگفتن خودشون به سه کشتی حمله کردن و جنگ رو راه انداختن.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6225" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
بر اساس اعلام ارتش اسرائیل، ده‌ها فروند هواپیمای سوخت‌رسان هوایی دیگر آمریکا که راهی اسرائیل هستند، به‌جای فرودگاه بن‌گوریون در پایگاه‌های هوایی اسرائیل مستقر خواهند شد.
هدف از این تصمیم، باز نگه داشتن مسیرهای پروازهای غیرنظامی است. وزارت حمل‌ونقل اسرائیل پیش‌تر برای کاهش اختلال در پروازهای تابستانی، تعداد هواپیماهای سوخت‌رسان مستقر در فرودگاه بن‌گوریون را به ۲۰ فروند محدود کرده بود.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6224" target="_blank">📅 21:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZ9HKTtli_YHCVU_lbp-DPWXfs0SQNH4O_24DNpKUIo0s_Lk1-6HFPq9PL1eKT2noItoy0EDUNCQ-EkxAUrqebo1TZSdF9qY4UCvuqXeH5E0PQVFqXn_V45v8p3uOvC1C2aQNinlVSsfT1OwsmCfvK3t893cChy9O-Gg-C9BNLjBgp_K2z_LL_Tynb8FDyHnS_MxOyq_I1aqC3pndFE0OUB7BCGkeNbYjA3aeieujYe9K3OE54LYTYWKUo9o1TazNqD77A5v8OYL3mHHBoV0YWIgD8wtO2Chw0u-Or7plo3xHzbtr8o38Kj3LYicuZibVUq5j_NWQGZey3I3j4iOug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بنا بر گزارش سنتکام (فرماندهی مرکزی ایالات متحده)، در پی حمله موشکی جمهوری اسلامی به یک پایگاه نظامی آمریکا در اردن، دو سرباز آمریکایی کشته شدند.
🚨
همچنین یک سرباز دیگر مفقود شده است. چهار سرباز دیگر نیز زخمی شده‌اند
و برای دریافت خدمات درمانی به پایگاه دیگری منتقل شده‌اند.
🚨
با این حادثه، شمار کشته‌شدگان نیروهای آمریکایی از ابتدای آغاز  این جنگ
به ۱۶ نفر افزایش یافت.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6223" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏
🚨
حمله سپاه به یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6222" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiKxjosD0juZqgZSISziPiNPtCSyQuatfPQnN5WlYhFzYt1_wF3V9_agnN-Wogf1tfbwdzmHZiRaMFTDbBpb4KqAuvpL_qauuKh7EPQCxBQ0E8UWEdqMsrbyBRx2rX2UjDhpL14g4kvOWx2Zo_TjsKMf3kWYZTwM-5Sgtb4LowiHyVTgjU1w05w6MUPKQHB2QwKy9SL-gdQyggFWYrIBjblQCdpqsqGT9GhZ1desWY_mMltNsnNts40L1FlKrFWVeGGDIksGEawtbsQTXOEer22nuulOWDn09fMSQCFKh_MMHHDk1EUJrL30bIp-2nP2T1-oNkng0J72LwpW-KHPQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4tzHjWuI8vVzpX5yilBOrQzIBoupKR87moYs7STI593UKGTMUNfjOVHdM9DueH-iWHs9oyvg63y_w97WTTp-N5TZBoCnl5Lo5QqQDDbYfF3flNM1eQoQzLVr_HFC9QSiIr81SFdkcEn9_KO8Rcg1J__-UvubuVt9k_FfxLhq0oRYztxTG0ru32s3aGnHdxgzLeZ6V8zmhDqdDA59J12Hh2KeeLAgYMVGg_CM13yS3rSTl4TCiervKwrMGzY2y-q7ItCaPc_36INnqReyU_H1Okxouq7NrFy2iv-LlVFyS696Yx1DRKsKH1_T3ffvDR7WFNC3W9xUX0dy5BXutZ7-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استانداری هرمزگان: در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6220" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">- اگر در سوریه نجنگیم باید در ایران بجنگیم.
در سوریه جنگیدیم اما در ایران هم جنگیدیم پس
❌
اما یک گزاره هست که دقیق تر به نظر می‌رسد و باید بررسی شود:
- چون در سوریه، غزه و لبنان جنگیدیم، و همزمان دنبال موشک تل‌آویو‌ زن بودیم و برنامه هسته‌ای، مجبوریم در ایران بجنگیم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMDnqOmvpxEbIVc4zWcDYi3iTx1BQ56ln8rFL3mOn41RhFjcmSb2MCZMvbtREejuX3lfG3_0IPkVD_ocr91WiTJGb4z4Zwa039T8tQ1d2zvLptdITgo4Biv3hNtrrpVDwMhKOoj9KmHYDkCwI7dnX5VwRDNXIVEQ4xXjYSxPlXxunqE2RItMg96xaZ_dbPXD-YGOKkqrm9DJguBqHENlospm_Upb7xZiEDiAk7sS4IjFYEwjNN3Y0yrCMl6GIAx59joaVptfm_ZFu_Q-WwAaSYJtMElvUJ2VKxrwp5lOv81ygNb3JNSbIpBuhLAPzXwAgUzYhmIkxBsEUjdOKbmV_qcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMDnqOmvpxEbIVc4zWcDYi3iTx1BQ56ln8rFL3mOn41RhFjcmSb2MCZMvbtREejuX3lfG3_0IPkVD_ocr91WiTJGb4z4Zwa039T8tQ1d2zvLptdITgo4Biv3hNtrrpVDwMhKOoj9KmHYDkCwI7dnX5VwRDNXIVEQ4xXjYSxPlXxunqE2RItMg96xaZ_dbPXD-YGOKkqrm9DJguBqHENlospm_Upb7xZiEDiAk7sS4IjFYEwjNN3Y0yrCMl6GIAx59joaVptfm_ZFu_Q-WwAaSYJtMElvUJ2VKxrwp5lOv81ygNb3JNSbIpBuhLAPzXwAgUzYhmIkxBsEUjdOKbmV_qcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=jOC2T0RogTMIlAVw6B4X6TXepWadGHMSjG6bJ5pZPOVTz6RQHX16M4eo7pSgCpBySl7hCPNt3t1aNryjHtE5eyluI1WL0NQpl-J6Gmk6uUow51tB-cEk-qsSk5ZxX1Uf2GBYuigD_0WY1EuHoR96ojuMi8OH-lQ9LR4vGOAAT3BS3JnS2fconwU08mhXo4yPmVd01E9ceBCZnXb3XbLc12kgs3iAT5wC_jQtkrQQEVhN1pH6VUjzkxuB_01THLWJSEqFNEqGx-gLNqtQdhknFVjyldkZ2z6Y8jbs7E7YHlxBKz_FCX0rfSztdh6O8OK_RLzQZ2HTpE-3BnuRg1y5rYlSZ-5Ct_QppwYRpiMjk9LJkv7VTXMtNVm7H8llC3M_o_cKVwLkf4GGh542LejVWTFJzOEZ_dYrja1YMejZZ6_bjEGfcTc1khqDQF-yvq8_JOoGlPRVNgZM3O0dnjtS9bqpPXuaCDeBCgX0lkr1z_qQ5sudHPJafiWKWRBd_TbcjZ27h8f3fZ3UazP8zF4A9HwT35vg-nXRAPogBjdiuC871T-f_qTBD7K6zaXNS_pTFBozbTA4VNUfxPJIoZooI4JOCZmlWP90iWBd5i12B4Qh-XVfVOi5W9zZnEJ9ZKBHWjKgd1j6W1wzYmBlSz6uVIK6qOETtrZf6HS7GzuRtfY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=jOC2T0RogTMIlAVw6B4X6TXepWadGHMSjG6bJ5pZPOVTz6RQHX16M4eo7pSgCpBySl7hCPNt3t1aNryjHtE5eyluI1WL0NQpl-J6Gmk6uUow51tB-cEk-qsSk5ZxX1Uf2GBYuigD_0WY1EuHoR96ojuMi8OH-lQ9LR4vGOAAT3BS3JnS2fconwU08mhXo4yPmVd01E9ceBCZnXb3XbLc12kgs3iAT5wC_jQtkrQQEVhN1pH6VUjzkxuB_01THLWJSEqFNEqGx-gLNqtQdhknFVjyldkZ2z6Y8jbs7E7YHlxBKz_FCX0rfSztdh6O8OK_RLzQZ2HTpE-3BnuRg1y5rYlSZ-5Ct_QppwYRpiMjk9LJkv7VTXMtNVm7H8llC3M_o_cKVwLkf4GGh542LejVWTFJzOEZ_dYrja1YMejZZ6_bjEGfcTc1khqDQF-yvq8_JOoGlPRVNgZM3O0dnjtS9bqpPXuaCDeBCgX0lkr1z_qQ5sudHPJafiWKWRBd_TbcjZ27h8f3fZ3UazP8zF4A9HwT35vg-nXRAPogBjdiuC871T-f_qTBD7K6zaXNS_pTFBozbTA4VNUfxPJIoZooI4JOCZmlWP90iWBd5i12B4Qh-XVfVOi5W9zZnEJ9ZKBHWjKgd1j6W1wzYmBlSz6uVIK6qOETtrZf6HS7GzuRtfY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشت ۹۰ میلیون ایرانی افتاده دست این جماعت  متوهم</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnnHT3sVOWz3i-gJXYlkkqH9oSPCtAEDeowKy4SBbUDXIvE3ixtwiaHFA-L2Bn5X7W9Dt1hXIHR2xNOhDAOAv_Ygrb7AWICMBVT3bm1PyYqkNzY6qQFPXVv831xRlUn9qslGjU0xpGXFfxCPjrdFvJ8k7qJNUA_smzcFTTuWwym1DZNBbbaw4wgdSQfW3ol6X3AjWQHYSQ8JwLVw6fSD-RfydubJCJik31YV4HguRGJxE3tTXcpWjYzzgiNR8ZBxi6UT6s6GxP0ClxK1AaguSj1zNBxMDvQq0MmjQb5nJQRXNyTwrzSJj7406o96WIPSmTX8cagq8v8KV2lKdpMnVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یه مرد هندی دیده یه تیکه یخ توی فریزش شبیه فرم مجسمه «شیوا» شده، یکی از خدایان هندی! رفته به همسایه‌ها گفته، ملت هم اومدن دعا و نیایش و اینکه این یک نشانه است و بردن غذاهای نذری و…..  :)
شیر، شیرینی، غذا، میوه و..
صبح یخچال پر میشد، شب خالی میشد!
و مرد هندی میگفت، شیوا، نذری‌ها رو پذیرفته.
در عوض مرد هر روز چاق‌تر میشد
این داستان‌ها براتون آشنا نیست؟</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">💔</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6210" target="_blank">📅 10:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27e890899.mp4?token=otHXu4Gq1hSbK0z7d-e8YoEttpy5Ay-4SELo230MM48LgDZKi_d2q_Nxd3M0WtHnAjrBvTz4tD6cJR8ksNwDzL5EU6-s9ZsUXBPfxrOfnzx0cvwmO3T69P1RhPuMM1sd816FFS5DSqkh5ueI1TtW3ynx65PtwyyKR8dqlRcpYJO5A80Y6vs4OpprzevWMEdrjEcMNDKj28u5vkhp4MurcepK_LsMRiRB4hQkv2Tf7V1UctXguOvfJUy850XcF5t4YwmavXcrT-xeNL1AmelSZSraV3NRsIqZ3-yap3qXw2U-7lZC2fbwQTAbj05yTH1ELJXHMB_imt1t9F3W3spAqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27e890899.mp4?token=otHXu4Gq1hSbK0z7d-e8YoEttpy5Ay-4SELo230MM48LgDZKi_d2q_Nxd3M0WtHnAjrBvTz4tD6cJR8ksNwDzL5EU6-s9ZsUXBPfxrOfnzx0cvwmO3T69P1RhPuMM1sd816FFS5DSqkh5ueI1TtW3ynx65PtwyyKR8dqlRcpYJO5A80Y6vs4OpprzevWMEdrjEcMNDKj28u5vkhp4MurcepK_LsMRiRB4hQkv2Tf7V1UctXguOvfJUy850XcF5t4YwmavXcrT-xeNL1AmelSZSraV3NRsIqZ3-yap3qXw2U-7lZC2fbwQTAbj05yTH1ELJXHMB_imt1t9F3W3spAqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از پل‌های غرب استان هرمزگان</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6209" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6208">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!  این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6208" target="_blank">📅 10:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6206">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان می‌گوید که چند موشک به تاسیسات برق و پمپ‌های آب‌شیرین‌کن مستقر در اسکله روستای بونجی در جاسک اصابت کرده است.
گقته می‌شود که این آبشیرین‌کن، آب حدود ۲۰ روستا را تامین می‌کرد.
🔺
شب گذشته کویت نیز اعلام کرد که جمهوری اسلامی همچون پریشب، به یکی از تاسیسات آب شیرین کن این کشور حمله کرده.
🔺
ارتش اردن اعلام کرده است که سامانه‌های پدافند هوایی آن کشور ۱۰ موشک ایرانی را که وارد حریم هوایی اردن شده و خاکش را هدف گرفته بودند، رهگیری و سرنگون کرده‌اند.
🔺
ارتش جمهوری اسلامی نیز با صدور بیانیه‌ای از حمله به پایگاه آمریکا و چند پل در بحرین خبر داده است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6206" target="_blank">📅 09:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
وزارت آموزش و پرورش:
🔺
با توجه به استمرار شرایط ناپایدار در جنوب کشور، آزمون های نهایی تمامی رشته های تحصیلی پایه یازدهم و  دوازدهم در روزهای یکشنبه و دوشنبه،  ۲۸ و ۲۹ تیر ۱۴۰۵ صرفاً در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می گردد.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6205" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=p3FzJq3QrLP4mnNebbXD3NLdqDl9EBntlawVW3s6HU4lcaKF44UTR8UmtLi8nzCJz4Wa59iXhNXA7QqJ93dCYIaMc9JPcc-GUuDFyVCSUxwLDjsiK4hlxq2CK-XKXtk-rHohC0ScAXDcBpL9g4AwBTvSWHok2CQZYzK7Fj1A3r_L1OcYeuNsPpPEm498TS3L-WnHjSjlgsjX2stwvGuc9VCCJmLBvwEpLT3Q1EBjZg0ga819mQyUZ4Ek3ZffUihtOjZCNzj9o746dCTuf3JfFUzG4Kp372FpLtvGPaATOX-q-KPYol2BeOUqix3vvwuys5QUjgJ9_9_RqN4Y6spYGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=p3FzJq3QrLP4mnNebbXD3NLdqDl9EBntlawVW3s6HU4lcaKF44UTR8UmtLi8nzCJz4Wa59iXhNXA7QqJ93dCYIaMc9JPcc-GUuDFyVCSUxwLDjsiK4hlxq2CK-XKXtk-rHohC0ScAXDcBpL9g4AwBTvSWHok2CQZYzK7Fj1A3r_L1OcYeuNsPpPEm498TS3L-WnHjSjlgsjX2stwvGuc9VCCJmLBvwEpLT3Q1EBjZg0ga819mQyUZ4Ek3ZffUihtOjZCNzj9o746dCTuf3JfFUzG4Kp372FpLtvGPaATOX-q-KPYol2BeOUqix3vvwuys5QUjgJ9_9_RqN4Y6spYGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مسیر ترانزیتی بندرعباس - سیرجان که در ادامه این مسیر به تهران وصل میشه.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6204" target="_blank">📅 09:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRyEMCL9SuotHyDYvavW4bBP-tsDae_asZtdlXm2kKAB-FvpzBZw9tWUiMNuQLqeFeZbHNcxbQnnSDVRXL91tkv6BkyNJG5GJqvvvfW60HmxoQAWB8vwBICM5X9ZJLv2JE17vNDcK1edJbI24aLnVdp-w618oWYURhJTdLkMFHE76ZxroRxq4Z8DOFdzjIsr54cL9pyLr8JYu2AV8fDVHxf6ghmleLgGczkMrtLMsAVXuGEmLuypgwEpMqvABlOCp9kGRCsNhMqIazzWOYGgjFaqgZJKxSxqU1igwM_PObtcJK54eLlNOuTuEI4WBRw1wlJMpvMQ8r_O4M_dDk-JtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سپاه که میگه شب گذشته ۴ کشتی با کمک ارتش آمریکا قصد عبور از تنگه هرمز داشتند که سپاه بهشون حمله کرده و متوقفشون کرده.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6203" target="_blank">📅 09:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqKmZ8-ctMnkINazjp1od95fWnjPVzqUjXs1M7MHaisXyGS84_pxg43TEcymQ0henOwYiaQkFssqN01sxTNUqBrO2ddJxp7x2XF-f40hXICtPT8UtDHU7_GXBr7qovNAP0wV1LQWIxVunhw8td952MuZ-S2sic_gcsr-XaZ0S-wJJIjP3V8TVHcpaWCV3lmr92Tbm2HHWg3EIDRaKp2_1LcrXE_cdZU1-o02A5gf-MmSw3EwpiZLW_I9e1tXa5KiEoU3iS_MwQk_hduEHGDOVeFPt0uwgP6JHxQZh29qTRa4-E02RCU723EQm8cU6ZCOu7tSl2vnIX_waioPfpulUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا شب گذشته با موشک
به دکل مرکز کنترل ترافیک دریایی جزیره لارک، واقع در میانه تنگه هرمز حمله کرد.
این مرکز برای ایران یکی از مهم‌ترین مراکز دیدبانی و کنترل عبور و مرور کشتی‌ها در تنگه هرمز بود،که اکنون کنترل تنگه را برای ج‌ا سخت‌تر می‌کند.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6202" target="_blank">📅 09:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!
این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.
🔺
ارتش آمریکا همچنین دیشب به چند پل دیگر در شمال بندرعباس حمله کرد تا ارتباط زمینی بندرعباس با بقیه مناطق کشور دچار اختلال شدید بشه.
🔺
بین ۸۵ تا ۹۰٪ واردات کانتینری کشور از بندرعباس (بندر رجایی) صورت میگیره. ماشین‌آلات، قطعات خوردو، تجهیزات الکترونیکی (لپ تاپ، گوشی و…) مواد شیمیایی، مواد و تجهیزات بیمارستانی و… همه از این بندر وارد ایران میشه.
🚨
کالاهایی چون گندم و روغن، برنج ، ذرت و…عمدتا از بندر خمینی (شاهپور) وارد می‌شوند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6201" target="_blank">📅 09:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6200">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=PQOyu-wVeCa0Aj9-_cr1knRHM9YXK2qQD_0s_Qipny6y82cobga6F2s0ZaAie_2sDXN_NAwiEknh-kPYFgIRlkJI7gSQjkrvotJy2GwytuU2v5tbnhuyd06URTyUi5R_BXQBEsCePUtL2i76fdoHGbeDjKVQSu8a6rIHZ0oqgSwo13A5wF5gRvYhQ5mbg_iyH-xnaXHmYDZTB3_i4aqSe6MSZI_agceWcOfJ4UWLM8fn3AygSM6gB9jxo3VGny6CGGF-sGX9hXTRBeyThokAXdNSB526ySCA57nOaTW1Mofo88RDXu7Lqh9L0G8V8Fv7z1Mh1w4ytZFG4LBJ02CJtImDRn621Och2fsXHXdYNIUjYekud8ibav7hBqUkNp7IrgTJab9xMujaDvd3ThZoIpreWnOue3eO7hjGnnZl-lEnd_eZFxr1wxtwT7Z-Z14hOqQ3ORZo7ufKEvS08dzzrs8aAiXlK7ikedGrTgwuhxNCTImg8Am8nniGDYNlT-32UZoL2CSqeSWpxLnKv1BSQEixVytdTqz0thGMqt89qr1kiwPY9q6vELG8KAccxOysAx7zSDohJykhzr2AWhwKgGmlfd9m58agayMwCmIb7kc1O4yxlT-EDMGKhFDdMXbtaA-ifYPTAPt4qGU_zXh4DwPJBl1jOzzVSaeZXxK9I48" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=PQOyu-wVeCa0Aj9-_cr1knRHM9YXK2qQD_0s_Qipny6y82cobga6F2s0ZaAie_2sDXN_NAwiEknh-kPYFgIRlkJI7gSQjkrvotJy2GwytuU2v5tbnhuyd06URTyUi5R_BXQBEsCePUtL2i76fdoHGbeDjKVQSu8a6rIHZ0oqgSwo13A5wF5gRvYhQ5mbg_iyH-xnaXHmYDZTB3_i4aqSe6MSZI_agceWcOfJ4UWLM8fn3AygSM6gB9jxo3VGny6CGGF-sGX9hXTRBeyThokAXdNSB526ySCA57nOaTW1Mofo88RDXu7Lqh9L0G8V8Fv7z1Mh1w4ytZFG4LBJ02CJtImDRn621Och2fsXHXdYNIUjYekud8ibav7hBqUkNp7IrgTJab9xMujaDvd3ThZoIpreWnOue3eO7hjGnnZl-lEnd_eZFxr1wxtwT7Z-Z14hOqQ3ORZo7ufKEvS08dzzrs8aAiXlK7ikedGrTgwuhxNCTImg8Am8nniGDYNlT-32UZoL2CSqeSWpxLnKv1BSQEixVytdTqz0thGMqt89qr1kiwPY9q6vELG8KAccxOysAx7zSDohJykhzr2AWhwKgGmlfd9m58agayMwCmIb7kc1O4yxlT-EDMGKhFDdMXbtaA-ifYPTAPt4qGU_zXh4DwPJBl1jOzzVSaeZXxK9I48" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب گروه موسیقی پاپ «BTS» کره جنوبی در پاریس کنسرت ۸۰ هزار نفره برگزار کرده !  شخص رئیس جمهور و همسرش هم مشارکت کردن.
راه کره شمالی : موشک، جنگ، مقاومت ، تحریم، فقر، گرسنگی
راه کره جنوبی: احترام در جهان، تولید بهترین کالاها ، رفاه مردمش.
مردم کره یک ملت هستند، با یک تاریخ و فرهنگ و زبان مشترک،
اما در دو حکومت متفاوت!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6200" target="_blank">📅 09:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5132059c16.mp4?token=v6ez71q2kozRtjbUOF_oXEWz6ICVBNDavEgtKH00tzCchsqN5e6D0k_7td1Kikr-hICKcZWqe1A5hy7yfY3OLIdpybp-ADc2T9H3ZHtrT9xev8a1uUzYhrZ12HI0pSOBFnPH2zq1r8RcmgJESg9CH7C3GARwA6iDZy98roPzzzls0efjUGA2S4fADlsJB4j0DUeXKHmUTVqBu2HSNC3TooOccqOwTJSG3Mk46htk--s8Pcp0Hkjd3i2KI3dBs_slKKkFHTD_qMEEprTHKPlqAcOvFgzq_QYQ2TrMnI0FtljeC_muwtSyOPZXQhnA6mGjOmlrG86SQqcRVOqhOygMLrGWAQwFgF8IdElZcUWxQamWuHEizHwcOJnFC-JfwBpwmfy6ezkBE-dfPJ40Wnrl7BtvIxplhcIXtKFHgqGDiCkgX137mgk5SjgyAn1256UzGc_hqg2kcVVT0Uid-KYqKZ_Mq76KqSfr1lahwaag7vMZy53tXXLygdG-loEjUo0BW6kMorRkZKZ_TZUWjVwmg3lTc5y_dmMr7rZil_Yelr_4Szm_XIrweLUuTc8dQb6dhZgTZt0d-MF3LO2jBKXcNxJ7OjPfaho3w9C_FjP7eupgvnOH4Ox2t2bC3L-G_HF3tC2_6_YvToZtcUbVmpKqd6FYY8x3lA11jHGmIUX71kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5132059c16.mp4?token=v6ez71q2kozRtjbUOF_oXEWz6ICVBNDavEgtKH00tzCchsqN5e6D0k_7td1Kikr-hICKcZWqe1A5hy7yfY3OLIdpybp-ADc2T9H3ZHtrT9xev8a1uUzYhrZ12HI0pSOBFnPH2zq1r8RcmgJESg9CH7C3GARwA6iDZy98roPzzzls0efjUGA2S4fADlsJB4j0DUeXKHmUTVqBu2HSNC3TooOccqOwTJSG3Mk46htk--s8Pcp0Hkjd3i2KI3dBs_slKKkFHTD_qMEEprTHKPlqAcOvFgzq_QYQ2TrMnI0FtljeC_muwtSyOPZXQhnA6mGjOmlrG86SQqcRVOqhOygMLrGWAQwFgF8IdElZcUWxQamWuHEizHwcOJnFC-JfwBpwmfy6ezkBE-dfPJ40Wnrl7BtvIxplhcIXtKFHgqGDiCkgX137mgk5SjgyAn1256UzGc_hqg2kcVVT0Uid-KYqKZ_Mq76KqSfr1lahwaag7vMZy53tXXLygdG-loEjUo0BW6kMorRkZKZ_TZUWjVwmg3lTc5y_dmMr7rZil_Yelr_4Szm_XIrweLUuTc8dQb6dhZgTZt0d-MF3LO2jBKXcNxJ7OjPfaho3w9C_FjP7eupgvnOH4Ox2t2bC3L-G_HF3tC2_6_YvToZtcUbVmpKqd6FYY8x3lA11jHGmIUX71kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا قبل از جمهوری اسلامی
ایران همین جغرافیا رو داشت، همین تمدن همین مردم و همین نسبت جمعیتی،
اسرائیل باهاش دوست بود و آمریکا پیشرفته ترین  سلاح‌ها و تکنولوژی
رو بهش میداد و اسرائیل برای کشاورزی
و آبیاری به ایران کمک می‌کرد.
شما اومدید شعار محو دادید و پول و سلاح ریختید توی لبنان و فلسطین و…….
🔺
همون روز ۲۲ بهمن به دفتر اسرائیل در تهران حمله کردید !
🔺
اردیبهشت ۵۸ رابطه با مصر رو به خاطر فلسطین قطع کردید!
🔺
دو ماه بعدش روز قدس رو راه انداختید!
اینها کم آوردن ، میخوان مردم رو فریب بدن و بگن «مسئله ایرانه و تاریخ و تمدنشه»!
نه خیر! مشکل جمهوری اسلامیه</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6198" target="_blank">📅 08:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔺
سپاه : به انبار دپوی قایق‌های بدون سرنشین آمریکا در بحرین حمله کردیم.
🔺
حملات ج‌ا به کردستان عراق</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6197" target="_blank">📅 01:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
وقوع ۵ انفجار در یزد
برخی گزارش‌ها می‌گویند که حملات در پارک کوهستان یزد بوده (منطقه سایت موشکی)
🚨
گزارش ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6196" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6195">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=E8HWUo3Kj1F7SjHFZqo1U2Z5iHOmX2DYjBaZFxpctX36_3hVOBOUcanxlhpugS-OrSPgZ346MOBd0StU4uQz3KfG5ToFYWWvtbYONmRzO_hi1nSLl0x0jOZCTdQL_SMijomOHO5GBrIJ4xB_cBiIRD6eS2LHa9zZ0qUGyGG5M-GOWRbp8iw-Jl3X-tKjUp06hSUz4trkfVoc9se8vzqVX2cd_FHCj7HjAIxGBnqHKyyCVgaZzc6QfK24yelh_YcnbmiT0m4iBd7dKoq7QN1OdiXOKa1V44XttzxM-UByC1E6KZlnJ0QkwFAsclDflse0hFQQA0N0pkbIXahF55GE_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=E8HWUo3Kj1F7SjHFZqo1U2Z5iHOmX2DYjBaZFxpctX36_3hVOBOUcanxlhpugS-OrSPgZ346MOBd0StU4uQz3KfG5ToFYWWvtbYONmRzO_hi1nSLl0x0jOZCTdQL_SMijomOHO5GBrIJ4xB_cBiIRD6eS2LHa9zZ0qUGyGG5M-GOWRbp8iw-Jl3X-tKjUp06hSUz4trkfVoc9se8vzqVX2cd_FHCj7HjAIxGBnqHKyyCVgaZzc6QfK24yelh_YcnbmiT0m4iBd7dKoq7QN1OdiXOKa1V44XttzxM-UByC1E6KZlnJ0QkwFAsclDflse0hFQQA0N0pkbIXahF55GE_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش چندین انفجار در لار
برخی گزارش‌ها از حمله به سایت موشکی لار خبر می‌دهند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6195" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6194">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9Du2Lr3LeYJu6XgLqKQEo8w874IdQPQKCxZbHFz-Qlb3JBcCNnA7lsj-UDYbsN-mAYOuzCXDS-SI4xHyWrqjOTCp0Tw6UH-UL9SdXna6S38oBJbre1NhmLBo1Jhx4CcSVYjjlbWwOviAL45dvtxf3ytPULj7MA1vL161yIUxeHKN6bOULQ-nM92h3cGV37mT368kbYboYGFTkk7B4npSypL6klkaVQ4CYIrjc8sb-oOKatIdwCj-uJmlB9uIoo8xk_qGXyt0eH0wAjFw-hFga4twiBBdxyTsm8CFC5I3SgEDvJWvtM8Fij74uqA2Z0quaqNX-z6WM0pRXuquVJxhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش حملات ارتش آمریکا به بندرعباس، قشم، سیریک، بوشهر و اهواز</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6194" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6193">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
سنتکام: ‏امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی،
[۲۲:۳۰ به وقت ایران - یک ساعت پیش] برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6193" target="_blank">📅 23:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6192">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029791358c.mp4?token=c9f-3xnUXqMHHEus29qevtShjka43Pj5MTJ_Q3jOL5I_2fEfm4FJ_8jQ2HnJrnTZ9lCtCFrgZNAO8R_wM9KyADHqTHW858BTOPI8Huqx-nOjs0WUcEvyuVeCPhEWJgHJ1pMJjJleYPbtzMlulUuWK7nl8A8KuNcDv6RVd3HNChffUXpKNHqs34pC5yaUMJMjffPqeHukIWzyen2awk2di5T7oLNKlfTPHuztSNXfEfRxhfjafJ2VSFHm80DPbGPeVeb0WxKhQAfS7u2oHbMv0s5UPYNAGb4kv5FKKCvXmfGBsuXhGT8fnZ74MN3tykDbP57sKu2evNsoDXRhZYWcGLUHTJqtTw3SHrikRYmLioKuyMCchEyylBNVY1gRFspOwJnz0_1oqxokN9A_nQ4RXZex7zqtoAbOrio09Un75yofGmfGFnjULpRMiWGwnBBWd6VilWfaYUwfagQn7-NHO-EQ-CbymFeoO2AVRcGN8Qjk7j6QVX1YvBhRxDnhyHeztHSfwzrbBvjh0B3bd6V39wHt_0qtEJouveimKoqH7Psx-0iMHta4YNWfGnPl4xeg8VY9yP2Sr_ipmZaAnBBapI2beSq3OretNqd9A42_jlDxFFHBgC09wMTTC2Ft3NqdNGyrY4gJPr9IY9DgL07RKFsbeNmPVC7sDyYk-zozb5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029791358c.mp4?token=c9f-3xnUXqMHHEus29qevtShjka43Pj5MTJ_Q3jOL5I_2fEfm4FJ_8jQ2HnJrnTZ9lCtCFrgZNAO8R_wM9KyADHqTHW858BTOPI8Huqx-nOjs0WUcEvyuVeCPhEWJgHJ1pMJjJleYPbtzMlulUuWK7nl8A8KuNcDv6RVd3HNChffUXpKNHqs34pC5yaUMJMjffPqeHukIWzyen2awk2di5T7oLNKlfTPHuztSNXfEfRxhfjafJ2VSFHm80DPbGPeVeb0WxKhQAfS7u2oHbMv0s5UPYNAGb4kv5FKKCvXmfGBsuXhGT8fnZ74MN3tykDbP57sKu2evNsoDXRhZYWcGLUHTJqtTw3SHrikRYmLioKuyMCchEyylBNVY1gRFspOwJnz0_1oqxokN9A_nQ4RXZex7zqtoAbOrio09Un75yofGmfGFnjULpRMiWGwnBBWd6VilWfaYUwfagQn7-NHO-EQ-CbymFeoO2AVRcGN8Qjk7j6QVX1YvBhRxDnhyHeztHSfwzrbBvjh0B3bd6V39wHt_0qtEJouveimKoqH7Psx-0iMHta4YNWfGnPl4xeg8VY9yP2Sr_ipmZaAnBBapI2beSq3OretNqd9A42_jlDxFFHBgC09wMTTC2Ft3NqdNGyrY4gJPr9IY9DgL07RKFsbeNmPVC7sDyYk-zozb5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت شانه خاکی موقت کنار پل بندرعباس</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6192" target="_blank">📅 23:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6191">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏یک گزارش محرمانه که برای رئیس جمهور ایران تهیه شده است، نشان می‌دهد که تنها ۹٪ از ایرانیان از وضع موجود حمایت می‌کنند و تقریباً سه چهارم آنها یا اصلاحات ساختاری عمیق یا جایگزینی کامل نظام سیاسی را ترجیح می‌دهند - فاکس نیوز</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6191" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:  ترامپ به ما نامه‌ای داده و صراحتاً نوشته است: «بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6190" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6189">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a688590cec.mp4?token=QMqymyYY-OE_tqoMQ7h0B4uirk3I5mZSblHaKXiM127IuXH3WjGXFo44rxbOYtbh0KKP7cx1HFxpcrwWkMFR9vmG_GGL_WgOqSBKGvJL4FqD51j29iKFf8H6Snj-bq9che2RySfmwNTCBk0xSu4MFcH5hjQab8BhtlHsgUc3qIuInJw5yoBnj6SCtvx22OjwswPcfi-Y9BRNP9krrl9CckI-_ih2p8JwzN5dl7EXCIaVV9BixlENXW-1u4ab6B7UWpv0oEDi8baIv5XskCRg0LqKM4veID5yQsEhIuMoIEWIFkeYztVwJSNo65fCmpcdWBbPbIcSQS1qcV9cUUbr6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a688590cec.mp4?token=QMqymyYY-OE_tqoMQ7h0B4uirk3I5mZSblHaKXiM127IuXH3WjGXFo44rxbOYtbh0KKP7cx1HFxpcrwWkMFR9vmG_GGL_WgOqSBKGvJL4FqD51j29iKFf8H6Snj-bq9che2RySfmwNTCBk0xSu4MFcH5hjQab8BhtlHsgUc3qIuInJw5yoBnj6SCtvx22OjwswPcfi-Y9BRNP9krrl9CckI-_ih2p8JwzN5dl7EXCIaVV9BixlENXW-1u4ab6B7UWpv0oEDi8baIv5XskCRg0LqKM4veID5yQsEhIuMoIEWIFkeYztVwJSNo65fCmpcdWBbPbIcSQS1qcV9cUUbr6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:
ترامپ به ما نامه‌ای داده و صراحتاً نوشته است:
«بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6189" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pf0c1KdMNMNHMS7XFagDI-wJdZ-MJ0k6OEt7_H7oS5z_yw8TM9a3yFiTf6jNaaBDTI-L3Siw9qkNDt-qltOMu9ESQt2qu1eJlj1bvyUdZRo4QQ-YdBUnE1VlhzZxz_eTWfTCNTkETRW6UmqYOiu_naH_ZYKxG3jUDXf3l0Az8tsxLq6NjJtj8vUmdtolTvyhEWMMla2qNgc5aKm7Vw716xWy_EsngZYa2lng_C-DAZODmwgYBbUoLqnRkG3ls_ks6gUwoyySUi4JNp6SBvu3XDglZ23IzqIDbzsUW3W0e4S6wLI7GCGTCovEosGb_u656_bqGz49hfSZRv47Sjt9Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ایستگاه مترو در تهران با مجسمه مریم و عیسی درست کردن (که عجیب هم نیست،
نصف قرآن داستان‌های مریم و عیسی
و قوم یهوده) و پروپاگاندایی راه انداختن
که ما چقدر احترام میگذاریم به بقیه مذاهب.
بعد همزمان کلیساها رو مصادره میکنن
و صدها نفر به جرم مسیحی بودن
توی زندانهای ج‌ا هستن و اجازه داشتن
یک مسجد به سنی‌ها رو هم نمیدن!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6188" target="_blank">📅 18:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rx8vkuX4WhaJ_Wi2jASDkPeaIZaogHwe8K00v2zFSusePPdRHMEUwbb0pN529Y6XBe_uXinwlZACfxnCUG1KS3_wAJuMQVXI8NN-TV9WimCkGUJgVufoC1Bk8Bp8P_F9-IwZQC0kRbDIz-Y5PfRgPDqaQs6Ubbv3lJUA2ohlw3aP9nETpWu-esGg3kqstLiVWldu-yUJTWWQHxSEHqMZPJMBgqcP9-RilRTZAkkqvaNSXcZGLc_lY7THcSEh_cVbYzT_1mD8Mb4wsZlLnKReB-r5QofS1obCkAOOQb5Vz4Uq9a1Z7AZPVxaX6a60lGflNI4w3bDjeMOlC0gR-k_h2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeSG9LQpjUY0FfS02sThxXn_H2T3Q6a_y6kR1L4gBWUcqEina1DeKqK6W5iA4dVyCRwYFXbGlBsogxqSVVZDzScgV2ku5H4m0YwP66qF_B7X13XWI7oYTSFXmP43xfypJ5hYWmmhwmPheBBb1JBRPZInjAOt-CUXyxDt2hBZGNAhi0z31Z4fNOP0HR3Ori_D43xCg8yEK02p700cpHggzD_13xLNsod_4Vw1kLc3lGKsY4naL6rcYuldJY3FqWc4On-FJMoWLvF0VaHzoGogllbtA4Wxy1-kfmbyk-hvBdeuRhBs3aLYUo7M06o2YLs1XQDA4zg20CRAKDpLVQZtCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل عرزشی !
من میگم اینها شکست‌های تاریخ
رو پیدا میکنن و به عنوان الگوی خودشون معرفی می‌کنید باور نمیکنید :)
تنگه احد! که نماد بزرگ‌ترین شکست و عقب نشینی مسلمانان در تاریخ صدر اسلامه،
رو شباهت سازی میکنن با تنگه هرمز
‌‌میگن همونطور که اونو در سیطره داشتیم
اینو در سیطره خواهیم داشت.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6186" target="_blank">📅 17:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JlAy9Z5zCvSJK-hYhGsfURKwneC2keFPKBOXBTH1_BQ2lgZ-kTs9jaYXDJLc6GP3eKhWgfgpxxb94Erti12H_O6SLyjCVRagmcixUFvAqNEtXnCONISQ_HdkUEvoUCPjJpkH8Kyq1C04T-AtX6dlRBYfQI8hjz2nnql4cMtqwpju8DQwrcrzNC_gAJaugsPkpyhSmbJHIWZCWC-NIlfDP_qbl7vhMt0_2WVQGK8DeryVtDVu3rYERdzap35WL38LO-WuQAKi8eJSxCGkMIe7Syy7HBbNOPXdaIFQNqlpJ8NnlGbRJzecYetUUeKcDcJQTmScB5gCaQ3fmnJjdhMhpwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JlAy9Z5zCvSJK-hYhGsfURKwneC2keFPKBOXBTH1_BQ2lgZ-kTs9jaYXDJLc6GP3eKhWgfgpxxb94Erti12H_O6SLyjCVRagmcixUFvAqNEtXnCONISQ_HdkUEvoUCPjJpkH8Kyq1C04T-AtX6dlRBYfQI8hjz2nnql4cMtqwpju8DQwrcrzNC_gAJaugsPkpyhSmbJHIWZCWC-NIlfDP_qbl7vhMt0_2WVQGK8DeryVtDVu3rYERdzap35WL38LO-WuQAKi8eJSxCGkMIe7Syy7HBbNOPXdaIFQNqlpJ8NnlGbRJzecYetUUeKcDcJQTmScB5gCaQ3fmnJjdhMhpwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا بودن شعار به زبان عربی میدادن؟
چی میگفتن؟ میگفتن  سرباز ایران و وطن هستیم؟
نه میگفتن «سرباز دین و عقیده» شون هستن!
و کنار لبنان هستن! و مسیرشون همیشه مقاومته!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7Hss2rpgeDTHJAbfEBG3jsgw8bfAPbgrLdw7dVk06GopEH9Ll-_6m1bxehT0LFftLk0IcvxdFhuRwNWZ-J6cqWnsvjDJPJQPWL65C8zOrOQEeHGk6IZWEYrHiA5bHBalaJoHYk1LIURpM8cRIJvWpjBremGLfxF5Gp7XPSxNZIa1QKNIoX0Eqwjx77XAXOpJ4_BqQqD9xzCHTK7PU65Hc3n96W9jl_KePVZHxDmP1t_oMCcWLC5MbnWnvStqqrAXtT1TwahTUnh_ADdLvUoCt9aHe6nAI_CNQ_jCXo0GCQfuzFCImTiJCbb3aLmCaR63z69kgpzi1grWJEqTQXakw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6183">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=HJ4Bb55WpRYWwdLR08WL1Oywaw_gZjEYI_lss3Blr9lLx-BIZGnE196eSJmIQRyuu7QGBGXwMbjl2K9pBmPdM-857fQKAwJJORjYDu4q5et0UrmlWLe_JGuOm5eXk3q-_RN9MyPsB7chtlUCkXJVfl1V8trsM9rPUsnOmyQ5q5bY8Hblpy081lSg-wplLbSxDRqkgwl289JLJDNcR1eyCoKmTg-kOepJIX-8ViMe9cChkjaRHnl1aEt8rE3FNvcT1YDyXjKDyLEDKa-hsComlPl8cU3_ZidEdT1CMHPAzMoGyL3H6e8TS_hpQ95BqMgQCSQt0EVDFaZDY3hpyiu6mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=HJ4Bb55WpRYWwdLR08WL1Oywaw_gZjEYI_lss3Blr9lLx-BIZGnE196eSJmIQRyuu7QGBGXwMbjl2K9pBmPdM-857fQKAwJJORjYDu4q5et0UrmlWLe_JGuOm5eXk3q-_RN9MyPsB7chtlUCkXJVfl1V8trsM9rPUsnOmyQ5q5bY8Hblpy081lSg-wplLbSxDRqkgwl289JLJDNcR1eyCoKmTg-kOepJIX-8ViMe9cChkjaRHnl1aEt8rE3FNvcT1YDyXjKDyLEDKa-hsComlPl8cU3_ZidEdT1CMHPAzMoGyL3H6e8TS_hpQ95BqMgQCSQt0EVDFaZDY3hpyiu6mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!  ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟  به خاطرش حتی موشک به اسرائیل نزدید؟  (که اونهم اومد در پاسخ ماهشهر رو زد؟)  خب جنگیدید و شکست خوردید!!! هم در لبنان،  هم ‌در سوریه…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6183" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6182">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902cf63917.mp4?token=hz6VJAEcEKBPsDutYGhnJI7GrXE4HKXOzWgwMM5UMLFsRv5_UHynWjwOOcfeglXpBOWomcAiEEkezgtasH56vQFRsrgWU8NYU1liNj0C7hc_kvgAWhyXoSATSe5h4gQsdy9_302m4NCwsr1s2tylPi44cc9qmIGPJQEcQIVnszkGXkKTX4KEYHhGbQKxiQfqKTDyv4Q3zuBV1_sseivKLeBTqH1uFCR6vw6iVGUAPc9WjHA3L3WsDmeUEVGoYpYXQn46d-_556bZWHIwB7khKB2P6CD81UiczszKOeq1vCXBLwlWF_3XsfSoTZmawUVuBu5kMYs21MphR8lx-EJIaaDuRkINBfe6eeYzV4BqXGBg9ptDnGO-IvFz19Ch5ddaTFAAUYB-bcI8FRtJD6T81QM_A055hJrXKVrPeDxVN12VxIkdWhbWQqbt3ft528LZSbWQ7kDkLMtc9DogT--FxPIRGiLWSb4dKSs-Pwr8yrZvQf1BstiERGxtzp2hqfsQWwBGBrlSXS9jcpSM9A_SuBalkxj-uxgcRDnonF2ht7yrOfZLUa3Kk3izIUcKNVope1am8PAIRzth-KOxZDwRXWRyQq7C55BEdxAYMDTQGJEMcorWlubUqqos0ltvuCfR8JKgcpmeLr9HOOFo7uwcU5L-qR4M_uNr1rPQxl5_EBE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902cf63917.mp4?token=hz6VJAEcEKBPsDutYGhnJI7GrXE4HKXOzWgwMM5UMLFsRv5_UHynWjwOOcfeglXpBOWomcAiEEkezgtasH56vQFRsrgWU8NYU1liNj0C7hc_kvgAWhyXoSATSe5h4gQsdy9_302m4NCwsr1s2tylPi44cc9qmIGPJQEcQIVnszkGXkKTX4KEYHhGbQKxiQfqKTDyv4Q3zuBV1_sseivKLeBTqH1uFCR6vw6iVGUAPc9WjHA3L3WsDmeUEVGoYpYXQn46d-_556bZWHIwB7khKB2P6CD81UiczszKOeq1vCXBLwlWF_3XsfSoTZmawUVuBu5kMYs21MphR8lx-EJIaaDuRkINBfe6eeYzV4BqXGBg9ptDnGO-IvFz19Ch5ddaTFAAUYB-bcI8FRtJD6T81QM_A055hJrXKVrPeDxVN12VxIkdWhbWQqbt3ft528LZSbWQ7kDkLMtc9DogT--FxPIRGiLWSb4dKSs-Pwr8yrZvQf1BstiERGxtzp2hqfsQWwBGBrlSXS9jcpSM9A_SuBalkxj-uxgcRDnonF2ht7yrOfZLUa3Kk3izIUcKNVope1am8PAIRzth-KOxZDwRXWRyQq7C55BEdxAYMDTQGJEMcorWlubUqqos0ltvuCfR8JKgcpmeLr9HOOFo7uwcU5L-qR4M_uNr1rPQxl5_EBE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!
ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟
به خاطرش حتی موشک به اسرائیل نزدید؟
(که اونهم اومد در پاسخ ماهشهر رو زد؟)
خب جنگیدید و شکست خوردید!!!
هم در لبنان،
هم ‌در سوریه هم در غزه به مردم گوش ندادید
جنگیدید و شکست خوردید!
۲- اتفاقا چون رفتید توی لبنان و غزه و…… دنبال کشیدن «دیوارهای آتشین» علیه اسرائیل و نابودی اسرائیل بودید، و افتخار میکردید که  بهشون
موشک میدید، از طرف دیگه دنبال اتم
و هسته‌ای بودید، اومدن و ایران رو زدن!
هم اونجا شکست خوردید و شهرهاشون نابود شدند
هم ایران داره نابود میشه!
نتیجه ۴۷ سال اسرائیل و آمریکا ستیزی شما!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6182" target="_blank">📅 14:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=ZzVDuxvgDz2foUrX0UEKbgm7sV4H_LHVVbqY4xsjbwnl2no1-y0hkdyRPC-JobIbonzgff0lzPHmIqp8uZz75ytA1R73Q-TJ-T8SgIS_vSM2Yxgrm1br55WN_5niT89xnFvoAm8pAEkXM0oprpWEoB0UIFUS1Xm7X8EUDlbTRup-8gArTJ6oGHh8jTDDcVOhd-flcDOyGgQwBohPs82uQvzcivNJpWU7UOGvr3XDspv-rAOT9D-K4Sx2Vk5IjUTC28nxAYWm9oUVQk9B67X-OzEfebGm8rnZAk8-QNFnFtXtKKUwfvNU4dNnd6nTH3hskBb2uC4AIWAmqoBhmzJfwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=ZzVDuxvgDz2foUrX0UEKbgm7sV4H_LHVVbqY4xsjbwnl2no1-y0hkdyRPC-JobIbonzgff0lzPHmIqp8uZz75ytA1R73Q-TJ-T8SgIS_vSM2Yxgrm1br55WN_5niT89xnFvoAm8pAEkXM0oprpWEoB0UIFUS1Xm7X8EUDlbTRup-8gArTJ6oGHh8jTDDcVOhd-flcDOyGgQwBohPs82uQvzcivNJpWU7UOGvr3XDspv-rAOT9D-K4Sx2Vk5IjUTC28nxAYWm9oUVQk9B67X-OzEfebGm8rnZAk8-QNFnFtXtKKUwfvNU4dNnd6nTH3hskBb2uC4AIWAmqoBhmzJfwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت وراثتی بود
یکی می‌مرد یکی رو به جای خودش
معین می‌کرد
مردم هیچ نقشی نداشتن!
میخواستن، نمیخواستن باید قبول میکردن.
🔺
خودش چطور رهبر شد؟
با نقل یک جمله شفاهی از خمینی!
گفتیم بعد از شما چه کنیم؟
گفت : همین آقای خامنه‌ای»
🔺
حکومت وراثتی بود : مثل پسرش مجتبا!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6181" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLABPYg0PSMfAKfGDFzCL6xZHo-3CtlLD70G_RV7NKaQ7m2-k7C_w8w29A7_O58sgH4AAO_EYi38eIB1LXS1enyl3zYZul2IBtGbAlD5YlAzBbWJpEAtHWBwPiFLdndlAgdQMuTY-M4Oz9CZMyp9rKk3bIX6gudAlnXNe4nfDsYYvwlLfxEfnwyyevFJ-rQpNDkIt9PAnneX0CDN-S0JqjomazBc0fdavn7lcZKWS4yx14IaDGVOcbACcPslv8ihLxMjsKfIDBdkNt9_bFMVICG008ZdyCRTIOxr9VSB-mjJ87waKEtZOQ-HWAjr59qEQjv5f7cSiOrBnpgM6oKLeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تاریخ هزار سال پیش نیست!
که هر چی دوست دارند روایت می‌کنند.
داستان همین روزها و جلوی چشم همه ماست!
گروهی برای خونخواهی خامنه‌ای
دست به حمله به اسرائیل زدند،
اسرائیل برگشت و ضربه‌ای بهشون زد
که یک میلیون نفرشون آواره شدن!
و همین امروز و بعد از ۵ ماه، هنوز نیمی از این افراد آواره هستند!
۴ هزار نفرشون از جمله ۷۰۰ کودک کشته شدن (خود قالیباف و خود حکومت گفتن اینها برای جمهوری اسلامی کشته شدند)
بخش بزرگی از جنوب لبنان رفت
زیر چکمه سربازان اسرائیل،
رهبرانشون حذف شدند.
دستاوردش چی بود؟ افتادن به التماس
و زور و خواهش برای «آتش‌بس»!
الان میگن این «اسوه و الگوی مبارزه دلیران» است!
این اتفاقا آینه عبرت و نتیجه گنده‌گویان‌است!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6180" target="_blank">📅 11:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d198d21980.mp4?token=QMhUPEhAMPB10EwIQ_Enb6sGyGX30uz4hG8WgrPKCaWbXfgNqw4vi965y7JwT2Nlr9vDGyjWgB2dOvvcOTkjIB_Cp5I3qwz9cGkBLNfYnHGJ1L8jZ3eHtAUzK51XAeKCWnSRVPA5K-dsWN-IFoek1T2QfDK7iIOgmQgYACXK9XqSJv2frvw3f_hecpqdFVEymywY6yTXhdU7SSJUWBTyKpvUKIPOsLWD5CvZMyMv2IkaGbN-6RJB4jl0HP0XQqg3jcrRfWNJK-3ueQBw900T-YQwe1jjPR7g1cbovJqNWu89Xbt-j5mO_WBfkDb-R57SYXmt4lbXPprDNO-GgilCi2NNnXFUgJMFeZVHlq4xcju2CPCp3k-GAHKz4WUZJZDpoyB4sfnZY81jSvGN1_kw87WipM_nynR-YH2CfsvCnSUKcUEVE4CnjUbkDFsbV4L0PyhYAE0vJMMbdPEXTcaNWfaGUYXDm_D1G26LSqc-uNh59RqCrBy3T8h5q5qkyP-XrJ0u1Dy-drXhL6MLjkixCNDJyi0dYJZqSVTW1RLNpIWGxuN5oJZh0RDWK4DxLOJkHE-dCRI94QubWVRijmlgr1XxYqw5ATSoO_c5igNDcGZm1cwkaYtp7SC9eDhO_nrbc0rKnlq7HPiqsNXB-3NNQ9TylmfPXvWQPZU8-XFrzzs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d198d21980.mp4?token=QMhUPEhAMPB10EwIQ_Enb6sGyGX30uz4hG8WgrPKCaWbXfgNqw4vi965y7JwT2Nlr9vDGyjWgB2dOvvcOTkjIB_Cp5I3qwz9cGkBLNfYnHGJ1L8jZ3eHtAUzK51XAeKCWnSRVPA5K-dsWN-IFoek1T2QfDK7iIOgmQgYACXK9XqSJv2frvw3f_hecpqdFVEymywY6yTXhdU7SSJUWBTyKpvUKIPOsLWD5CvZMyMv2IkaGbN-6RJB4jl0HP0XQqg3jcrRfWNJK-3ueQBw900T-YQwe1jjPR7g1cbovJqNWu89Xbt-j5mO_WBfkDb-R57SYXmt4lbXPprDNO-GgilCi2NNnXFUgJMFeZVHlq4xcju2CPCp3k-GAHKz4WUZJZDpoyB4sfnZY81jSvGN1_kw87WipM_nynR-YH2CfsvCnSUKcUEVE4CnjUbkDFsbV4L0PyhYAE0vJMMbdPEXTcaNWfaGUYXDm_D1G26LSqc-uNh59RqCrBy3T8h5q5qkyP-XrJ0u1Dy-drXhL6MLjkixCNDJyi0dYJZqSVTW1RLNpIWGxuN5oJZh0RDWK4DxLOJkHE-dCRI94QubWVRijmlgr1XxYqw5ATSoO_c5igNDcGZm1cwkaYtp7SC9eDhO_nrbc0rKnlq7HPiqsNXB-3NNQ9TylmfPXvWQPZU8-XFrzzs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو‌شب پیش شعار میدادن که
:
«
جنوب ایران نکند جنوب لبنان شود»!
حالا دیشب شعار دادن
«جنوب لبنان و جنوب ایران
اسوه! رزم همه دلیران! »
خودشون می‌دونن جنوب لبنان ویرانه است و
مر‌دمش هم‌ آواره! فعلا هم زیر چکمه‌های سربازان ارتش اسرائیله. برای همین اولش میگفتن
«نکنه مثل جنوب لبنان بشیم!»
حالا میخوان هندونه بگذارن که جنوب ایران «اسوه رزم » است و برید جلو!! بشو شبیه جنوب لبنان!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6179" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=M3Gc2ETHkfhbv8sLXWMwGjTatugggn8cr7dUWFEYyEN7Mq3048Y0fDGqbIh8yc0p1PYlJPVlIABY1yOLAyKxEylkh7z1FQElDK-i5nFH6O_5OTcytQHmezVMaiQfZS3zCJg24eOh2QdeXQAIbPM666IghJSxveLHznPoi0wXHmabpKHpGTTM0drKuPpYf9FKLsyEwF_0ZQfL4k1ZtI-20K7eqOEl0OnDbT59806HdghydhdZLPwF9pdYJWlgQDQwbFCicXYJbss0fDF_AhaQ9Q3vW3W1OAqqpOn4LhrsufxKrPVW5PY84yjc7v5SyppCioqYnT8bIHSl5R0MU1Qw5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=M3Gc2ETHkfhbv8sLXWMwGjTatugggn8cr7dUWFEYyEN7Mq3048Y0fDGqbIh8yc0p1PYlJPVlIABY1yOLAyKxEylkh7z1FQElDK-i5nFH6O_5OTcytQHmezVMaiQfZS3zCJg24eOh2QdeXQAIbPM666IghJSxveLHznPoi0wXHmabpKHpGTTM0drKuPpYf9FKLsyEwF_0ZQfL4k1ZtI-20K7eqOEl0OnDbT59806HdghydhdZLPwF9pdYJWlgQDQwbFCicXYJbss0fDF_AhaQ9Q3vW3W1OAqqpOn4LhrsufxKrPVW5PY84yjc7v5SyppCioqYnT8bIHSl5R0MU1Qw5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی از سخنان سردار نقدی : اگه حتی به آمریکا حمله کنیم، قدرت پاسخ‌گویی هم ندارند!
با کدام پشتوانه اقتصادی میخواهند بجنگند؟ با کدام پشتوانه مردمی خودشان؟ همه جا در محاصره ما هستند.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=krS9IWYYaCMX3SA2KtVmWcnIDErQ7UWVaaBA4uCG_SMNOJeda8YXmZaV6YXVBu4R2h2fpgl9f_6ho0NBpswptJje0MFBUIDK30jroGN-GeOmgVGjH3D45PODmCJYJZ4EwixOjL2aEPVl3bnGBrFmw16EZzeIfSU_SVf6AJ8MtQ1ye1pr8QAzpoA74WF7uQ0ewvNJta0Ox9A-DtkZyFN85sSB3sYl15wM3zlg79JWQVE0-z1Y9THKVKCuM3W09_E5ALJ5pZrF4YK42t8BS12i3rNUa_aM520CguUG5P2wzDXAEPrnXw8Es2xh3HMu38c5GoBXJWOiUwX0eiQ8Ef_ICw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=krS9IWYYaCMX3SA2KtVmWcnIDErQ7UWVaaBA4uCG_SMNOJeda8YXmZaV6YXVBu4R2h2fpgl9f_6ho0NBpswptJje0MFBUIDK30jroGN-GeOmgVGjH3D45PODmCJYJZ4EwixOjL2aEPVl3bnGBrFmw16EZzeIfSU_SVf6AJ8MtQ1ye1pr8QAzpoA74WF7uQ0ewvNJta0Ox9A-DtkZyFN85sSB3sYl15wM3zlg79JWQVE0-z1Y9THKVKCuM3W09_E5ALJ5pZrF4YK42t8BS12i3rNUa_aM520CguUG5P2wzDXAEPrnXw8Es2xh3HMu38c5GoBXJWOiUwX0eiQ8Ef_ICw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل  کهورستان در اطراف بندرعباس
که شب گذشته مورد حمله ارتش آمریکا قرار گرفت</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6177" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6176">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار …</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6176" target="_blank">📅 08:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGyDqkZwzWxxjpdfelXctD0QeJnaJ4VF-PxaRsAQ6F8z7tze96IFoYBBOMt3ZKtOhdRWuNObBH4VNDtTHgTnRqKVPMeBLd6STxgLve0oR38huYnqrmSFpel_KsrxGYSnmWK1lzdQT_fqr-ABN1fhx8Zdnc0KlsFlzfiyldAd7MtwmVQxR-8ZcK88bLbsJmANarbWqo7M9Kin0tcOxOMN1p-4UDD00QTIlK98sYkyXjhEEkUq3tH1qJy7vq4CrpWRgOExpfY19jA8e_w3g40vW1lP4Atr7by0opV1yNpqQLJ12glBGj4rBzT4xsVbiNfFCWgadXi_bcqltacHiIxuiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار - شیراز
🔺
تعداد کشته‌های حمله به پل‌های بندر خمیر به ۷ نفر افزایش یافت
🔺
تفنگداران آمریکا : یک نفتکش ایرانی را توقیف کردیم.
🔺
دیشب برای نخستین بار جمهوری اسلامی به خاک سوریه هم حمله کرد، هدف : پایگاه آمریکایی در التنف
🚨
تصویر : آمریکا برای سومین بار به برج مراقبت دریایی چابهار حمله کرد و این بار آنرا منهم کرد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6175" target="_blank">📅 08:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6174">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
حملات شدید به بوشهر</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6174" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=e1j3B-zTqY76bTFoT9EGS6br6SwPnkiruEzG4At2Z3Z9lUJOf9tW8ewy95qlZZljGFpjplh3pbjGvO8qlVWmiM8G1QTrt1dSehToJiYraAShGgCDRZQj3-Sth4ZNehttzkA1TY5EucPMHwX0TUjQlljUaAUSl39kajXlvc58uwBIqfUfbdhNtZ4MbIg_YyumjzWs2cOZ6nLeF7Yzd6yw02lt5GizAkkEUCaK-64xVESsHWsc__qnGPG5-AM7Nnk_08zg6bkIAPTrvVXuiIc8LuO0MRKtMSo5Gyk5SV_LzTGZ-BZRN7DkW-aSrYA_wRjPatAKc81SUSsGKom0H00jyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=e1j3B-zTqY76bTFoT9EGS6br6SwPnkiruEzG4At2Z3Z9lUJOf9tW8ewy95qlZZljGFpjplh3pbjGvO8qlVWmiM8G1QTrt1dSehToJiYraAShGgCDRZQj3-Sth4ZNehttzkA1TY5EucPMHwX0TUjQlljUaAUSl39kajXlvc58uwBIqfUfbdhNtZ4MbIg_YyumjzWs2cOZ6nLeF7Yzd6yw02lt5GizAkkEUCaK-64xVESsHWsc__qnGPG5-AM7Nnk_08zg6bkIAPTrvVXuiIc8LuO0MRKtMSo5Gyk5SV_LzTGZ-BZRN7DkW-aSrYA_wRjPatAKc81SUSsGKom0H00jyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏فارس: جزییات حملۀ   آمریکا به پل‌هایی در شهرستان خمیر؛ ۲ نفر شهید و ۴ نفر مجروح شدند</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6173" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jH4SkmiHK9upOFSuAfwSKCzjcz2iMjPMjbmlnOy0JWPOmB7E-6A13t-0Td5UUjRhwrBFMmZ2TxgWtznRvUgCWzWHJTWnrsUqh8dnMaqjrb4K8NNs8ay6AK3qKL027kUnVMyvEFOkegma3oD_pHt955cEDpfDCMbPxjQ6UaLHkVTg6JGDQ9g_I0BxnRvctXkJ-f7akWGXV3Y012HQMT8r-DxHf_-d7D1MzQ8FBZwgmA3_qwsyyt5lBKSFtVHNr-TjcZ3zzzt72xzwpPtqiobi86SmfFjyCqVhXKjcBiqPGE7GAarxhwuQWC-LwbhmpE5io9FfY5kUnUdkzT33xIhDew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6172" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
