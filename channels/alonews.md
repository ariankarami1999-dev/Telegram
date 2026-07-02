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
<img src="https://cdn4.telesco.pe/file/YI0GtSt8hTVbTAqnttD0ozQm4pszOccuYQS7N5l55qH5Px_ViJ04Kn5PvRar7_yLyWxoWPM-Mm2pcaZ-dJXiicUEct6eh0D8_jzHi2NJzBs7Ss9QATfHfdbXStRwaC5XPLaOmvToElmZMI3WHPyXGxWmJtxAjiKp3XVawBmRVcRFCUbboR3akn0YKTpFH1j1VqUqUSewsPwLACHUi23iRMI-04tuxwwQdzzW3QWOzPzQyAMoSuNyyq6ufeeB8rdWFqvS2-g-U-UIJgUEyv3uZBCJQ5dqS8428KLi6UsuP5sM0rl0aAB-GFxoUmLLOoj7qsy3LyS8wWDje21pTCWDrg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 941K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 18:05:51</div>
<hr>

<div class="tg-post" id="msg-131453">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
بلومبرگ: قیمت نفت خام برنت به زیر ۷۱ دلار در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/alonews/131453" target="_blank">📅 18:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131452">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aqa1rBPHk9izG5SMrissy4ZcppN9_jpA1G0OLAX6jsA7gI95Tke592qDk-XiWbUx7LjL28r3Oi_Odv_aTWapbN9vdQxfZw6mDVG0E_qZs0VpMYemEAUQJcKSMvwrAMoZqhWHWodGF9FSvojE4xmjKPKY4wYy0QbaAVu0KMKKHpWmRo_Gn-vm2hQWxElApP-zAZW6ApAl_vl2hZ7GLijc0vNYJDICYK_g8zr5DXX3rgbT3Fwo3wnjRzgsiSsI-C7KC8XaK4yQZYgOh5m0UFtVwDYzTIn5DPtTYOESLbkF-o5jsXEcn3oYhdBvIZvOS0OeuOPsElob-UHZC4uGOCAgoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قائم پناه، معاون پزشکیان: قرار باشه هرچی رهبر بگه رو اجرا کنیم که باید در تمام نهادها رو ببندیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/131452" target="_blank">📅 17:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131451">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_2nvHTonx-6dIYpr7rbAYIkHe7_aPbADDP6A-ZXKauzzaHRgNScGgBpxjOsaZdykTkQHvl155Vm_zs4BTLdlY_RFRTo8GH2OB7KYu60XGJMdLxhGjk-XGVi90svefEs54UdBoB3WcwsUfG4TZ-rHYEq9XEqqIT_LQY0aCO6UwUX_HLwN11AdYYKd7ovdZJJTMjE0J4eCvRHTwaZzjWN5KFkloSYqunp1xjb5dVdvqRg_q8kuyqnKtHmp9wAmZzP7gzg7_dT_T3L7tPzTmTnZvuWsQMN3R5obXhqSBELj2dPu3qSiNajDesFlRiJ13erCfCQDQ78n3XjyuNSZ26HxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهردار نیویورک، زهران ممدانی، از هر کسب‌وکار و هر نیویورکی درخواست کرده است که با تنظیم ترموستات‌های خود روی ۷۸ درجه فارنهایت (۲۶ درجه سانتی‌گراد) و خودداری از استفاده از وسایل بزرگ تا اوایل صبح یا اواخر شب در موج گرما، در حفظ پایداری شبکه انرژی نقش خود را ایفا کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/alonews/131451" target="_blank">📅 17:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131450">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سید عباس عراقچی، وزیر امور خارجه ایران و امیرخان متقی، وزیر امور خارجه حکومت سرپرست افغانستان امروز دیدار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/alonews/131450" target="_blank">📅 17:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131449">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkvjRhhG04Q86D1Y_zk7tend07h7ojHnZTBE_xKMTURRvgKhWJrjw3s2o_KZPe-laTXfoRf5UNZJ9FSIUaqM2dZhh9i8vO2PknRP353XgnKLAdtSjmEgO3t8dqP8GwIX8BW6A97cBSE28-kWwJASc2qGOgGIlV_P8t4Ro90pCYgZ2455aMB-ZM1v4YB5GwhOZhyo4_cfYlDfbW8_0S0MhfFMuMgds4NA9hE3K5-EmHxgRaR_hQE25SKOgsC5hBIdkwdLhGxQLZCqIzFk9isrQK6o5wreV2Pk1e1su9GEkzNclqvYPYRcp7wALzyiN284QQ4rAxEi-tM5MqQ0wqugGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی مجلس از تذکر مقام عالی به نبویان خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/131449" target="_blank">📅 17:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131448">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
روسیه برای واردات بنزین دریایی به هند روی آورده و ۵۰,۰۰۰ تن متریک از قزاقستان تأمین کرده است، زیرا حملات مداوم پهپادی یک سوم ظرفیت پالایشگاهی روسیه را فلج کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/131448" target="_blank">📅 17:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131447">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
سرکرده حزب دموکرات کردستان:
به آمریکا گفتیم به شرطی به ایران حمله می‌کنیم که کل ارومیه و آذربایجان غربی را به ما بدهید
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/131447" target="_blank">📅 17:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131446">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=CuzC9lGD7OvqkELYU9mJva4q7aDLPs4djIqb8FdEETaClY0OyCLS7JDhMp0NOl2FEonJk-1IPGR6Dh8zSPEpO3eMUcOleYCcT0Ivt6XerHFnqiVmz7vvZjvYeI2HSdSp0pMu-tcVS95m8VvEGTH8doyor60QcRDk0qSGXBwiDFWY9JSu-nZlWJ-vHwsORv14FFXApxu98-k_sSCMhUCOM_z9akGuy50VxhOtXrMBNpOC1Ccs-2QS5_JhSOZxru3Q565oBRVwY8c15BmGtT4PJkIxsTBuoWd_fcqYRyaX6CDd1mQyiQs5xHYtwCk2RB2G_0K8RF62WqBBNzesrKhIHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=CuzC9lGD7OvqkELYU9mJva4q7aDLPs4djIqb8FdEETaClY0OyCLS7JDhMp0NOl2FEonJk-1IPGR6Dh8zSPEpO3eMUcOleYCcT0Ivt6XerHFnqiVmz7vvZjvYeI2HSdSp0pMu-tcVS95m8VvEGTH8doyor60QcRDk0qSGXBwiDFWY9JSu-nZlWJ-vHwsORv14FFXApxu98-k_sSCMhUCOM_z9akGuy50VxhOtXrMBNpOC1Ccs-2QS5_JhSOZxru3Q565oBRVwY8c15BmGtT4PJkIxsTBuoWd_fcqYRyaX6CDd1mQyiQs5xHYtwCk2RB2G_0K8RF62WqBBNzesrKhIHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس شبکه افق، به قالیباف: این مسیر به جایی نمی‌رسه، حالا دیگه خود دانید
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/131446" target="_blank">📅 17:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131445">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
طبق گزارش ها برخی از مقامات ارشد سیاسی و نمایندگان پارلمان عراق از کشور به صورت پنهانی فرار کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/131445" target="_blank">📅 16:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131444">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47920d202.mp4?token=PXZTpgbdDfpPSCzAEANzjpCTA3U4rU_1HikkMaALiItOksmXfvF2meyi0UOSP3pLznEToTpY77d8oM1gesJL-lAQGAkmv6j7kCgWpcHRFj9ydv_p1WxqLjyHkM9e48c9cf8BLkyjIeqC5eSc1PHSBm9G9_HqM2JbhhaTaLlxuCgYZFSTO1I3ofiK5T40R_xMIAzjT3bJvFpsJNI2RCl4GpCgDj3fSxj-AxDBg8ZsDyYGjI82AVj2Fs0zMnxCqXYFYtmtvz1_z3l4Cq-HAaDS6gyEuA_Ap_iQWU7WcagZoSN7pcYbPSbhwcx_evjPjpwNIYeIrs1HOmYfrd8k1Jna1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47920d202.mp4?token=PXZTpgbdDfpPSCzAEANzjpCTA3U4rU_1HikkMaALiItOksmXfvF2meyi0UOSP3pLznEToTpY77d8oM1gesJL-lAQGAkmv6j7kCgWpcHRFj9ydv_p1WxqLjyHkM9e48c9cf8BLkyjIeqC5eSc1PHSBm9G9_HqM2JbhhaTaLlxuCgYZFSTO1I3ofiK5T40R_xMIAzjT3bJvFpsJNI2RCl4GpCgDj3fSxj-AxDBg8ZsDyYGjI82AVj2Fs0zMnxCqXYFYtmtvz1_z3l4Cq-HAaDS6gyEuA_Ap_iQWU7WcagZoSN7pcYbPSbhwcx_evjPjpwNIYeIrs1HOmYfrd8k1Jna1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله یک مداح به مذاکره‌کنندگان: رهبرتونو زدن هنوز خاکش نکردن، چیکار دارید می‌کنید؟ چرا راستشو نمیگید که سر هسته‌ای هم مذاکره کردید/ ۱۰۰ میلیارد دلار بدهی دارن بعد ۶ میلیارد سویا و ذرت می‌خوان بگیرن
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/131444" target="_blank">📅 16:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131443">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fe0d83ee9.mp4?token=lP-qAqSHcNOpq94AVZZJ4_mZkhw6Xit8K5c8Gea3XfrGOCp-I4QSJq5qoMF_YZE0vGK-HnkleN-8clVzzhYn6NymutFSu00y1RXihh8bljcjM4TkpGtrpQ5EhWVlBzeDS5XXe6JUrblpihPeQx1tJq67xJWwc9vx1w--0_wbMBCd1cLid-p_GbAnw7w4lowQQMKkQYGTQEuplFm4OHgANexphc_LJbAhPy9Az4OhlK2ZNlCNsoCLfOu5tqI1gSdcz5JYULmaCLSvhC5PEsMOEL1T4iU3-txYchiB0WyC96j5kqPBYuC-3IH4_Itebrwl2hgbMvr5cgTwDZ89EHbyHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fe0d83ee9.mp4?token=lP-qAqSHcNOpq94AVZZJ4_mZkhw6Xit8K5c8Gea3XfrGOCp-I4QSJq5qoMF_YZE0vGK-HnkleN-8clVzzhYn6NymutFSu00y1RXihh8bljcjM4TkpGtrpQ5EhWVlBzeDS5XXe6JUrblpihPeQx1tJq67xJWwc9vx1w--0_wbMBCd1cLid-p_GbAnw7w4lowQQMKkQYGTQEuplFm4OHgANexphc_LJbAhPy9Az4OhlK2ZNlCNsoCLfOu5tqI1gSdcz5JYULmaCLSvhC5PEsMOEL1T4iU3-txYchiB0WyC96j5kqPBYuC-3IH4_Itebrwl2hgbMvr5cgTwDZ89EHbyHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مصاحبه وایرال شده از یک تریاکی:
+نظرت راجب مذاکرات چیه؟
- ما با کسی که پدرمون رو کشته حرفی نداریم و باید تا نابودی اسرائیل بجنگیم
+اینجوری ممکنه زیر ساخت هامون رو بزنن
- بزنن ما هم زیر ساخت هاشونو میزنیم
+اینجوری ممکنه وارد بحران برق و آب بشیم
-مهم نیست برای ما ، ما کف خیابون اماده شهادتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/alonews/131443" target="_blank">📅 16:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131442">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
آموزش‌وپرورش:
امتحانات نهایی به‌هیچ‌وجه به تعویق نمی‌افتد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/131442" target="_blank">📅 16:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131441">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHk-keGrjliKZ86q5PdzyYG2lV4ZjRkYqswiC9lyXoGbWpTzd73a9699mO0OjYFc_RcC5KhMoUg9M3srmyg9RtWWWCrQBoS5h95njxsfW8vqMz3GFd-7yL_mvf7YH7qrbbhoK1yYpHGdX8CcenmPIINSim3XUI8wum134iXAR2hFbGJNCxb--vJPdeLKMtfqFPKcYHPGeKlSt7XKPGFxw4nTjNwd0YWsEtPQqhGbo8zgPUBqn5_eqFwzGt1rsh_ciXuX27A8bjxwbXSu2jamP39Y4edtDEJbMVAEpvrkWeqwa-poUXRcxcrxRJLWm0rRadPvMV55fusqePezjFkQxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لارا لومر، فعال سیاسی آمریکایی خواستار بمباران تشییع جنازه سیدعلی خامنه‌ای توسط ارتش اسرائیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/131441" target="_blank">📅 15:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131440">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFXi_R3ng2N-rZL1TK-GEisJmtQ_jbNm64vUPtzYHgsvHYw7JX35pvFEq02xRqCHyQHbFCej-nXKPF6uj9THy9GhzNvAAUmcLiwp5GLJPyQnEMZLRvxkDnwQF6i562Rm_WgRfUZZtoqz6SRY-QsHO_Utriz0tr0v__CZwL_8ub0hOU5WuV1hJFVs8InVXB356HyW6Di2ZuOVxvBxm5gJ8p8r-KyXzOUQmjjWajCEB-lw673oXR2rAtOnDQxRHTVeG0Vgl_CqebJXEQPimzYJQs4EG9jLzaogXiWuKHxI5rQpE00BWqUHtYaBKDtRTj_FmODZckc_Sfn_3HRdJRuSIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فواد ایزدی:
مشاورین قالیباف کصخول هستن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/131440" target="_blank">📅 15:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131439">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmIv8HuaxmQuHKu5B62gNp795n4bV4-8E4gEhkTmlsiYa_xTrGjBJRz93GkYixHZSVkOH-goB7kn47nZrmJS_G2CA7Ie56glLf7iShHRIzD8DWA3-Agllhg-XJVK42J-RI_Mdo9doWxNHO1fuwX3h2bYiCVpKO1Cx9OwP97mW0I850p63A5JXRDK29Ed4EJvMSFUWCLCAC8Z3Q9u04mclP8s-XDRahs6sSPKTLSF2hh2oDnCmaluXHdRvXNxPC38S2jY2L86CNAG3MXlBIInDKAzinLXVX-lwOipdEQMIb8g6wZSpPGjMsDXgzeJ63uU5Kzs5ByoUyronyhMMsztHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
ایالات متحده تاکنون بیش از هر کشور دیگری برای محافظت از ناتو هزینه کرده است، بدون اینکه هیچ سودی از این کار ببرد:
🔴
ایالات متحده ۹۹۹ میلیارد دلار، بریتانیا ۹۰.۵ میلیارد دلار، فرانسه ۶۶.۵ میلیارد دلار، ایتالیا ۴۸.۸ میلیارد دلار، لهستان ۴۴.۳ میلیارد دلار.
🔴
دیگر کشورها، از جمله آلمان، بسیار کمتر از این هستند. (۲۰۱۴-۲۰۲۵) مسخره است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/131439" target="_blank">📅 15:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131438">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noNeHlVVZPPmcDU6PgYNdmW7jM2alrvJJOg_VUIDocU-J4r4XuRNnmYfreMjncx8qUaEc5KC_9E4YHtla3Md8brbuiOA-JpjQeIRrGNlUolPuYuHzhv77gGvoCrVXJ1kCIa-tC5fwJjfmofFVYY3LhQC6fOoYK1L8hzEBkaOc22wQRm_fEKJB6VpCQAmx7EMo7O-0TC1a2KWlzbsHt7TLP4Qu9WB4IM0P6qrNZQ5_Wa0ppWzRlGY0h4xnfxkc5cCeahi41oDyJdZiSDqH8ToBdwMaAqlW050sQvTSXOMtuVZeX2YxEUTLAqVJfp77BJMJA2gyXMo5-MhXCsIQNXewA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی : طرحی جدید و فوری برای قطع اینترنت بین المللی بدلیل حفظ جان رهبر و فرماندهان در جز اولین اولویت های مجلس قرار خواهد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/131438" target="_blank">📅 15:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131437">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
زلنسکی از آمریکا مجوز تولید موشک پاتریوت خواست
🔴
در پی حملۀ شبانه سنگین روسیه به کی‌یف و مناطق اطراف آن، رئیس‌جمهور اوکراین از آمریکا خواست به اوکراین برای تولید موشک‌های سامانه پدافند هوایی پاتریوت مجوز دهد.
🔴
روسیه و اوکراین دیشب هم به حملات دوربرد علیه اهدافی که فاصله زیادی از خطوط مقدم جنگ دارند، ادامه دادند که تلفاتی در هر دو کشور داشت.
🔴
ستاد کل نیروهای مسلح اوکراین اعلام کرد که در حملات شبانه روسیه ۱۳ نفر کشته شدند. در مقابل، مقام‌های روسیه از کشته شدن چهار نفر در حملات پهپادی اوکراین خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/131437" target="_blank">📅 15:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131436">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93d606e626.mp4?token=ps_Xore-vwgKqhhzN2TmOeHxlYvb7Mv5FRj2Pi51WoOheG8-nIa60npRsmxRfCCUKy2mVOq6N_hR58762EZBkaan3ddvwhizW7a5x2cPqr3O_vKfSGRe0rlhSTI3e98dhcCa8vDHktHTCeCYXAyrKl0AUHJDkVpFxrOMZVk2geajl79aTflDpWuAe29BhaPYM9ROBNnseWNpZh6h_aavc4ulZWrcuQmDR_lJC-SFDgbfP42JRntn2CWoPlLza5NPI_9rPZxc8WOXn9y5_w2GDgQK28aarfiifumR4Lm-_H1iUgYhGBAAHoy6dSo5eZoKfCmDTTvCIqWqrb0opCO_IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93d606e626.mp4?token=ps_Xore-vwgKqhhzN2TmOeHxlYvb7Mv5FRj2Pi51WoOheG8-nIa60npRsmxRfCCUKy2mVOq6N_hR58762EZBkaan3ddvwhizW7a5x2cPqr3O_vKfSGRe0rlhSTI3e98dhcCa8vDHktHTCeCYXAyrKl0AUHJDkVpFxrOMZVk2geajl79aTflDpWuAe29BhaPYM9ROBNnseWNpZh6h_aavc4ulZWrcuQmDR_lJC-SFDgbfP42JRntn2CWoPlLza5NPI_9rPZxc8WOXn9y5_w2GDgQK28aarfiifumR4Lm-_H1iUgYhGBAAHoy6dSo5eZoKfCmDTTvCIqWqrb0opCO_IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بزودی در تهران، مشهد و قم
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/131436" target="_blank">📅 15:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131435">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4392bc1c10.mp4?token=Tg655rhCVI-UToPFS2mED1ClFaRxyIpJe64sM6gn2bZ33P5JyUULRpVILPEuFN26tNaQO45B-J6BhsQTo8fyo36zT4APInJg1jStYP7_yoJEOHdqj9_UMay-YSKcQqqaA4vNxJPY5KtWLyYRAWDXOfFZLrA61CbAayQZYDlh9JW3IH-k_wBo12QWtKmrojOlOVVQIhflBfnXA0n-ijlMqCUSAbcL_LhsvuIGU2n4eo5kCck93nH4EFrU_fJ0SoiCr3RKQuyB1J--XH-sbmCaPhgM6T8Ht-NfXeeryawHsTVUqw-53Mgvmz9eY7XCofpuFcmK4D7KwhAokJZIkxC4BRefFYyRgxAWbqmC832XimnLpdEyfQth8MZRpHpTNf_-ydByxM_n9YdAOM8Sk4fDKoZO1-7DmlDAI3hMVNRu2kujRnGAB5l4hxSOv4AGVBAYZWoamCQGtQ8vuOnyHkTv0aT44WlfE96fzhAW_RnlRO4D7yZeAFvchr2Brt-v32kVAjrUleNBc1lrOD4Dd5kd6UK1OY07mwrwlznxaZKcXjzbIXvItR6NK0s9XYHaRN6jTJ-TrjlSbPmv946arHpW1nkU6QrnzDydlsrIsqZRIUlD3pgmMjiHfEQV0O4hUB-I0_6RNmX8LB0R8GLF1ge9vws0_ZviAeAek3DU3TeUfVI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4392bc1c10.mp4?token=Tg655rhCVI-UToPFS2mED1ClFaRxyIpJe64sM6gn2bZ33P5JyUULRpVILPEuFN26tNaQO45B-J6BhsQTo8fyo36zT4APInJg1jStYP7_yoJEOHdqj9_UMay-YSKcQqqaA4vNxJPY5KtWLyYRAWDXOfFZLrA61CbAayQZYDlh9JW3IH-k_wBo12QWtKmrojOlOVVQIhflBfnXA0n-ijlMqCUSAbcL_LhsvuIGU2n4eo5kCck93nH4EFrU_fJ0SoiCr3RKQuyB1J--XH-sbmCaPhgM6T8Ht-NfXeeryawHsTVUqw-53Mgvmz9eY7XCofpuFcmK4D7KwhAokJZIkxC4BRefFYyRgxAWbqmC832XimnLpdEyfQth8MZRpHpTNf_-ydByxM_n9YdAOM8Sk4fDKoZO1-7DmlDAI3hMVNRu2kujRnGAB5l4hxSOv4AGVBAYZWoamCQGtQ8vuOnyHkTv0aT44WlfE96fzhAW_RnlRO4D7yZeAFvchr2Brt-v32kVAjrUleNBc1lrOD4Dd5kd6UK1OY07mwrwlznxaZKcXjzbIXvItR6NK0s9XYHaRN6jTJ-TrjlSbPmv946arHpW1nkU6QrnzDydlsrIsqZRIUlD3pgmMjiHfEQV0O4hUB-I0_6RNmX8LB0R8GLF1ge9vws0_ZviAeAek3DU3TeUfVI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: اگر ایالات متحده آمریکا دولت لبنان را تحت فشار قرار دهد تا دخالت سوریه در خلع سلاح حزب‌الله را بپذیرد، آیا شما با آن موافقت می‌کنید؟
🔴
نواف سلام، نخست‌وزیر لبنان: نه، نه، نه او و نه من به این سؤال پاسخ نخواهیم داد. من معتقدم که رئیس‌جمهور احمد الشراع قبلاً به این سؤال و بیشتر از آن پاسخ داده است.
🔴
از طرف وزیر اسعد الشیبانی، چیزی برای افزودن به آنچه رئیس‌جمهور احمد الشراع گفته است وجود ندارد و من هم چیزی برای افزودن ندارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/131435" target="_blank">📅 15:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131434">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
پاکستان: دیشب طالبان بهمون حمله پهپادی کرد ولی همه رو رهگیری کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/131434" target="_blank">📅 15:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131433">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcwiCJQ3XmW6ozv3CH7OyDLgWmQf29ewHJcyONqmwyGc1bTYY9xAy3rHLVjvN6ILlaWFhnn45FUL0N5DNjcwwYKM1c0W3UA9fQRuFsOUJVx69229Q3r8nl0itVS1nPr6WI0pTU3K5tc8ydxbogGJgXtVKEN0taOR5_EhxjGkdXmzWw-5rUW4bvypDVrRkJcGNdjFAq4GTsO5ojHAJT-A-nG-AQlckUXPqPS3Fh8CpZ1W8UbuBI7o3CXNtarR0VZ5aRtzUefjxQEgaRkwkKksAfqIS8Ce4eN1Yq94EH-DFmyiktO9xqKD1EKuJGzi9ex37bHB8vxhrf1Xm8o4Bw-asA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آلمان درخواست ترامپ برای وفاداری بی‌قید و شرط به ناتو را رد کرده است، و وزیر دفاع بوریس پیستوريوس در مصاحبه‌ای با اشپیگل تأکید کرده است که این اتحاد بر اساس اجماع ساخته شده است نه اطاعت
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/131433" target="_blank">📅 15:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131432">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
سفارت روسیه در سوئد اعلام کرد که دوباره با پهپادهایی که یکی از آنها حامل یک بمب ساختگی بود، مورد حمله قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/131432" target="_blank">📅 15:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131431">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gg7K3Wj8HDNSRiRLV_myEeAaL-f2tVqslUaWlHxkdnVYQgTp4G9j7niLAKK9Lm6B24SietE4755O42cfmOsd7z4GfznZfnWAVX9YCJyIC5ne4CEjYkOb5epyFPhNP1Eh_Yzlh-Fr4XgJRa8DHhZxHl0TFSByBoDV74ijglVzmJJ8vtHsJ1ugF17yz2NLzO_8gjN3CnkAyqdKwUMtToRykuMdb_YhnlPbb2HETQtxdPuFW6o-EVzD54N7m3hotZRTsozrz8wgkTdBDYbdZe-FWxdBi-IIgfN8DqqLtDxlyo3PP1HmfXLgFor3D81Sga6K-IqKaFgG7doDkHw9yKNi1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشته های گرمایی در اروپا از 2129 نفر گذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/131431" target="_blank">📅 15:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131430">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
نیویورک‌تایمز: جنگ ایران چگونه به دلخوری شدید ترامپ و بن سلمان منجر شد؟
🔴
ترامپ هر چه کرد، ولیعهد سعودی نظرش را تغییر نداد
🔴
از لحظه‌ای که ایران تنگه را بست، کل روانشناسی اعراب خلیج‌ فارس تغییر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/131430" target="_blank">📅 14:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131429">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8uR1pBGEder_nMvXzB6KTQpiK3b8xe97Cr0NjqTZz5t8J_KnYKr9GUpzaQPagvDoHW4nGtPOnCho9Nea7gbvboqROvWkBhC9GAH1vWqORnmOqbUwSrs4_oSCO2AL2Ku_3JhWFKs1zlrbgCB01Lah6XE2r27PogKRzlAD3mJaY6X93lSlA1jPMpNkhzo5FpZlPT4axdptDW2aDif-JVBJb_KRAtvvrf0qRRiXhuTyQgdidiMn6LpjPvbZMCruNYl8nKnK7HaO2O4Tuc_tV2trjkd6YV-VG2BZr5QlzZEwbmspVX0BfzQxAq4AHhwhPRS0dO6Tp10ZJKrWcqIZ5MiKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر اقتصاد لبنان، عامر بیسات، می‌گوید خسارات ناشی از جنگ از سال ۲۰۲۴ ممکن است بیش از ۱۶ میلیارد دلار باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/131429" target="_blank">📅 14:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131428">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQH7YCkMLR1KZlUOn0wXFCSFozrnl80oZ7tG-YC4OmefDVszZ655rSu5Q8pbEJC-Lse2O4XT5DAIp-z3WR6cG182EXKqAIuAre9HRlG5UbyLPT9oltD65tyVJHBRTUVTtyo-WTOEKJDnuUJJIbz9RCZ6bJrewMcP5gQnI47Gf_wT6WAzI4eyMjFBfMk8cZaPOvoSZ0MYr4AiGKOL7Ojd1GCeTA8BNTZIk7juS9YFN87jgxR8ae16aGf9FX_Rz2sALKdDNT0lSw7x1dvgrZA2cvB2JYKTxLxBfZ-IO1JX1uu0_93AncDTjry23XNPNbRyIvAofabX50AdER79tLnHAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش شده است که نیروهای روسیه یک هلیکوپتر تهاجمی Ka-52 را از دست داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/131428" target="_blank">📅 14:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131427">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
الحدث مدعی شد: دور بعدی مذاکرات هفته آینده با حضور عراقچی و قالیباف در  در بورگن اشتوک براگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/131427" target="_blank">📅 14:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131426">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سخنگوی ارتش : مذاکره، جنگ در سنگری دیگر است
🔴
دست بر روی ماشه، چشم به روی دشمن و گوش به فرمان فرمانده معظم کل قوا هستیم و هر لحظه اراده کنند، وارد جنگ با دشمنان خواهیم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/131426" target="_blank">📅 14:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131425">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
گزارش جروزالم‌پست، پس از وارد شدن خسارت‌هایی در جریان جنگ ایران، سنتکام در حال بررسی انتقال پایگاه‌های آمریکا از منطقه خلیج فارس به صحرای نقب در اسرائیل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/131425" target="_blank">📅 14:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131424">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/c4dfc3f2bb.mp4?token=tOS52m3PLEpHj9RCfAP34sR8lSczxzPv5z-jRcDHmha79Mkv3HF7Mp5Q3MotIg9F7jN8emfaON_cxVmgd9q9c0TpH_ZMIT6kwTyzmWyJweyxJvXnx9P_wfRHJHtjYYVma4tQz8vqQ6fXM28sWrNOr2pcESlLtI_gUEbhbkTnNmrVv3jyZDR-hbZBy8dAqaILoQs8pzkiptYFJ7Nsawq1TCrvvxCr9G1mH-KVCdk-dqplXl1N_wd1GGfBiG_gRO2WqSt3fFvzaEs-XVyIYcmWf90EcJSoY3A1ShIkSenhwOi_XsFxKF0-e-fqBGFcU7GsVAuLCWF_lhqE4yY0sDuDRw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/c4dfc3f2bb.mp4?token=tOS52m3PLEpHj9RCfAP34sR8lSczxzPv5z-jRcDHmha79Mkv3HF7Mp5Q3MotIg9F7jN8emfaON_cxVmgd9q9c0TpH_ZMIT6kwTyzmWyJweyxJvXnx9P_wfRHJHtjYYVma4tQz8vqQ6fXM28sWrNOr2pcESlLtI_gUEbhbkTnNmrVv3jyZDR-hbZBy8dAqaILoQs8pzkiptYFJ7Nsawq1TCrvvxCr9G1mH-KVCdk-dqplXl1N_wd1GGfBiG_gRO2WqSt3fFvzaEs-XVyIYcmWf90EcJSoY3A1ShIkSenhwOi_XsFxKF0-e-fqBGFcU7GsVAuLCWF_lhqE4yY0sDuDRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آمار تلفات زلزله ونزوئلا به ۲۲۹۵ کشته و ۱۱۲۶۷ زخمی رسیده است و نزدیک به ۵۰ هزار نفر هنوز ۹ روز پس از وقوع اولین زلزله مفقود هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/131424" target="_blank">📅 14:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131423">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
فوری / العربیه: دور بعدی مذاکرات آمریکا و ایران در ۱۸ ژوئیه برگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/131423" target="_blank">📅 14:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131422">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
استاندار تهران: اینترنت قطع نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131422" target="_blank">📅 13:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131421">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
ادعای شین‌بت اسرائیل : یه شهروند تاجیکستانی رو به بخاطر جاسوسی برای ایران، دستگیر کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131421" target="_blank">📅 13:49 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131420">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
استاندار تهران: اینترنت قطع نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131420" target="_blank">📅 13:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131419">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd28bd491.mp4?token=OBnOfBZsWuYD5dxCMPMEgK59kUig9Lp8dzUG7JsJkBIkH1zq85QVRHaSD_fimOq61kqd7H2QlF0IS7zj771Ks34hemchobAzc2VqhmKiwT4rYs4YcxJNl_SvfjGjaoI6zRIa2PfVDfst_nbuKXwNf6L678QLd30JSpnviieX8scDRZR8cnr71BIR5ynuGFUM_RV90Mt2sVkWdY6LvXfioLpQTgkN9TpMQZIrz5AGVs6QjmSuAxMzETB3dQU27ojc4keLtBCt24hemmYksrNZmeVRGeBaJoKJpPeYt4yNcnACkcSKO9jaBk1SMw4yXjjqqLgi1340hdqaljKYySQmZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd28bd491.mp4?token=OBnOfBZsWuYD5dxCMPMEgK59kUig9Lp8dzUG7JsJkBIkH1zq85QVRHaSD_fimOq61kqd7H2QlF0IS7zj771Ks34hemchobAzc2VqhmKiwT4rYs4YcxJNl_SvfjGjaoI6zRIa2PfVDfst_nbuKXwNf6L678QLd30JSpnviieX8scDRZR8cnr71BIR5ynuGFUM_RV90Mt2sVkWdY6LvXfioLpQTgkN9TpMQZIrz5AGVs6QjmSuAxMzETB3dQU27ojc4keLtBCt24hemmYksrNZmeVRGeBaJoKJpPeYt4yNcnACkcSKO9jaBk1SMw4yXjjqqLgi1340hdqaljKYySQmZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از وقوع آتش سوزی در یکی از محله‌های نجف
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/131419" target="_blank">📅 13:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131418">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
پست جدید ترامپ در تروث سوشال ...
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131418" target="_blank">📅 13:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131417">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7644c63d7d.mp4?token=S1zEctqrbYpKym34DMs6KvDZSQOb96WA9sdWx8t1uGqSrHrwkYq6yJ1a0fMZ_gPvPY0rgnsGaYZldpj_nTfd4QKpksj1_3R5HAMKPp-pTM0oWyN9SKbx5nS9anMI_Xk0opX_RcYRP7V5wFlC6j1s_ybeVIBRpQVb8w1GboyS7Yl2__LulFOyKjChEQJRRIkD-FCQyyV_Ws1b747Sj96lu8lbaa-PgD8GVmYloPGBLtrW_ApmhGVildApwlAMCRLim3JkcEhFm6BY8yduT3e_l25HY-LXI2gXxFcinYkVRjSKE93UdF--wtKASyaytlHDXas9zrdcUTBnR4QtljPrrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7644c63d7d.mp4?token=S1zEctqrbYpKym34DMs6KvDZSQOb96WA9sdWx8t1uGqSrHrwkYq6yJ1a0fMZ_gPvPY0rgnsGaYZldpj_nTfd4QKpksj1_3R5HAMKPp-pTM0oWyN9SKbx5nS9anMI_Xk0opX_RcYRP7V5wFlC6j1s_ybeVIBRpQVb8w1GboyS7Yl2__LulFOyKjChEQJRRIkD-FCQyyV_Ws1b747Sj96lu8lbaa-PgD8GVmYloPGBLtrW_ApmhGVildApwlAMCRLim3JkcEhFm6BY8yduT3e_l25HY-LXI2gXxFcinYkVRjSKE93UdF--wtKASyaytlHDXas9zrdcUTBnR4QtljPrrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گذاشتن جایزه ۱۰۰ کیلو طلا برای کشتن ترامپ و نتانیاهو
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131417" target="_blank">📅 13:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131416">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
دلار هم اکنون 176,000 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131416" target="_blank">📅 13:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131415">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c41d4e2cd.mp4?token=KZMj15YyejJLXn7fMOeUnP5EWMjhLVOiKlR2IiitUct7qe3KTB3Bfp0h6rX03CxUPQMibjs7-YI-0ncsxbZoOh_Hai130Qs3BFNkblU3W91UQCrRUORmOpYNB-vAXaowlZ1oR8gy50PXZApkdlsfJNit4FZBa25ETCSha-GV7-IVwRM8gGSbLiGjXEZ8st-_GmSlYD6cAWQ9hQQVPiPvPEOimhZZbClaIlZytJSscuJvPLwXUklM-Oc2jAD7m86cFQ3onafy4IfcsNRBIjJEA7yC-FVfT02VzOmF9piN-FGiaGcx-1i-bAOK5dzcZSwGGGrAVpZc-PZBXdildAZ5V1s4JtVFcXz-XwtByqI6l5CWQpG7N_XfYg288hTbiRMP233lz8Q62Cd8aBHWbor0fWc3zm-LgDXaa64iBswePGZT7wY7lZUGRCQZDEvROfzHwKqpve9VGToJ6bZHXQDlN0VIU5iCrH_yfDJSqRteVYvb34mRFlXJSI3ZNSIslaZ0lriZw5bt8JEw6HjnWQ3Uj6H4e-AJKs88PpGmcyP1B7hJ6HiMKIcuPsyz8u0o6SNhveip7G0vXIgu8IWTxyPM6chMsqIRvxVmeuJEiCVqzAC8NL5OceId9jmEqO7dXzAnyG3jhKU7kuvWTgV12hRi286D9xSEkFYeMDaRdYj4shc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c41d4e2cd.mp4?token=KZMj15YyejJLXn7fMOeUnP5EWMjhLVOiKlR2IiitUct7qe3KTB3Bfp0h6rX03CxUPQMibjs7-YI-0ncsxbZoOh_Hai130Qs3BFNkblU3W91UQCrRUORmOpYNB-vAXaowlZ1oR8gy50PXZApkdlsfJNit4FZBa25ETCSha-GV7-IVwRM8gGSbLiGjXEZ8st-_GmSlYD6cAWQ9hQQVPiPvPEOimhZZbClaIlZytJSscuJvPLwXUklM-Oc2jAD7m86cFQ3onafy4IfcsNRBIjJEA7yC-FVfT02VzOmF9piN-FGiaGcx-1i-bAOK5dzcZSwGGGrAVpZc-PZBXdildAZ5V1s4JtVFcXz-XwtByqI6l5CWQpG7N_XfYg288hTbiRMP233lz8Q62Cd8aBHWbor0fWc3zm-LgDXaa64iBswePGZT7wY7lZUGRCQZDEvROfzHwKqpve9VGToJ6bZHXQDlN0VIU5iCrH_yfDJSqRteVYvb34mRFlXJSI3ZNSIslaZ0lriZw5bt8JEw6HjnWQ3Uj6H4e-AJKs88PpGmcyP1B7hJ6HiMKIcuPsyz8u0o6SNhveip7G0vXIgu8IWTxyPM6chMsqIRvxVmeuJEiCVqzAC8NL5OceId9jmEqO7dXzAnyG3jhKU7kuvWTgV12hRi286D9xSEkFYeMDaRdYj4shc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
غضنفری نماینده مجلس : یک کودتا علیه رهبر مجتبی خامنه ای در جریان هست
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/131415" target="_blank">📅 12:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131414">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
شاخص کیفی هوای اصفهان با رسیدن به عدد ۵۰۰، در وضعیت «خطرناک» قرار گرفت
🔴
برخی مناطق این کلان‌شهر، در وضعیت «بنفش» و «بسیار ناسالم» هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131414" target="_blank">📅 12:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131413">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
بلومبرگ:جمهوری اسلامی کنترل مؤثر خود بر تنگه هرمز را از دست داده است.مقام آمریکایی اعلام کرد حمایت نظامی آمریکا و کمک به احیای جریان نفت و تجارت از تنگه هرمز در هفته‌های اخیر به بیش از ۱۰ میلیون بشکه در روز افزایش یافته است.
🔴
این افزایش ایران را غافلگیر کرده، توانایی آن برای کنترل ترافیک را محدود و به حملات اخیر اطراف تنگه کمک کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131413" target="_blank">📅 12:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131412">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
نیویورک پست: تنش در روابط عربستان و آمریکا بر سر ایران و نگرانی از جنگ و تهدید منافع نفتی با احتمال بسته شدن تنگه هرمز افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131412" target="_blank">📅 12:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131411">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kiGRzAHiWE6QRsRHRp8G9vimR2b7yOjonx8nY5anUk7oG9w3hNYBQhHxo-s1qRrBbVUW12jyt86br0-fXlPPEQTQ6_j2PItuVCvvwKoa5IxgoGxX0FxlWBlQ3PMFuKH_Z4CQojKqgw5vlCYJBQmc6zoQ0ERA6uGV-jiEnwlcJGPcSaA_4qFKPnKLcJpPhXDcyIidsRnwTzae1VSDe7NsGIacXipnNBfS-p-F6A8fIfnzzpUCMhjYG6XYgO1EFQvXf52JBluVE3je4ByQLFybnDM_OWO-6FqBdMZ5d2Nhz3TnXnTGShRlJ4uCm8dNJUF-ajJnm7s0DfBtOMbYLu_66g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دکل ارتباطی در سیریک که آمریکا در جریان اتفاقات هفته پیش سه مرتبه بهش حمله کرده بود، امروز دوباره سرپا شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/131411" target="_blank">📅 12:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131410">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
رئیس مجلس ونزوئلا: در پی افزایش شمار قربانیان زلزله که تاکنون دست‌کم دو هزار و ۲۹۵ کشته و ۱۱ هزار و ۲۶۷ زخمی بر جای گذاشته است، هفت روز عزای عمومی اعلام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131410" target="_blank">📅 12:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131409">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
الحدث به نقل از منبع آگاه از مذاکرات دوحه: آمریکا به ایران گفته که پیشرفت در پرونده دارایی‌های مسدود شده، منوط به پایبندی کامل تهران به یادداشت تفاهم است و تغییر در وضعیت تنگه هرمز، نقض تفاهمات تلقی می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131409" target="_blank">📅 12:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131408">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
رئیس اتحادیه کشوری کسب‌وکارهای مجازی: امکان صدور مجوز فروش آنلاین مصنوعات طلا در درگاه ملی مجوزها فراهم شده است و متقاضیان طی روزهای اخیر می‌توانند درخواست خود را ثبت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131408" target="_blank">📅 12:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131407">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
قرارگاه مرکزی خاتم الانبیا: حضور جنگنده‌های آمریکا بر فراز تنگه هرمز امنیت منطقه را به خطر خواهد انداخت
🔴
استمرار حضور جنگنده‌های آمریکا، اعم از با سرنشین و بدون سرنشین، بر فراز تنگه هرمز، موجبات ناامنی این آبراه گردیده و امنیت منطقه را به خطر خواهد انداخت.
🔴
ایران در صیانت از حق حاکمیت خود در تنگه هرمز، از هیچ اقدامی برای درهم‌کوبیدن هرگونه تعدی و تجاوز توسط ارتش آمریکا و حامیان آن، دریغ نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/131407" target="_blank">📅 12:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131406">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c8ff9a7ef.mp4?token=tw4zY5y5ZUdjdnK04w7tpnMQKjUTDOfBq6T1Sth87MyPWbLcfFcCp7wuD4i3SK4Sva9zfvmvY4tjRHlMbFWVxUEEYawYOyWV_5m5i_v7RnFdDPPDCMzHz-LcFyNsPyWZHrfnjfJnAC_ZP1GGfs14jG3EbH_TGxZBgnp8FJVk3-QjHnls7zGEATpzqPbFR9EhU-agKn8FPbmPGnkzPogTjj6_1H0F47cVrS6DYLThl-CTacxSvaIMDm6rMOSq_51rFBLJ2dwsdNg8uU18DzXQ_tc_MOr3pi2KF9QI0OM2mymnOP45Gd1coKlJGprTGpBqQvI7XEfQvZ1Gwy9G2SeoYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c8ff9a7ef.mp4?token=tw4zY5y5ZUdjdnK04w7tpnMQKjUTDOfBq6T1Sth87MyPWbLcfFcCp7wuD4i3SK4Sva9zfvmvY4tjRHlMbFWVxUEEYawYOyWV_5m5i_v7RnFdDPPDCMzHz-LcFyNsPyWZHrfnjfJnAC_ZP1GGfs14jG3EbH_TGxZBgnp8FJVk3-QjHnls7zGEATpzqPbFR9EhU-agKn8FPbmPGnkzPogTjj6_1H0F47cVrS6DYLThl-CTacxSvaIMDm6rMOSq_51rFBLJ2dwsdNg8uU18DzXQ_tc_MOr3pi2KF9QI0OM2mymnOP45Gd1coKlJGprTGpBqQvI7XEfQvZ1Gwy9G2SeoYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز F-35 های آمریکایی برفراز ورزشگاه لیوایز کالیفرنیا قبل‌ از شروع بازیشون مقابل بوسنی هرزگوین
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131406" target="_blank">📅 12:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131405">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36d4fc7f4a.mp4?token=iW5JpdzvV9btOMOQ9wROvw0V1zxdZ4M5KYwq2l50zhuJy4pdbxgmB1ILxP165bRRO-_XBiR8o9SBWloBn1Ipx4tinL-U0jJcWeXrmV5xE3vPTqamgGu8RHEVZ4YGaflHnEnGJscPemjhUWRiAdSdhd0-zDxbUk7XTfD1l-Am0CFlXxczdW-RcycCCw7qj8g7Li-zc6TEK5UdlF2ANmvD1VfjZaAvRNiBSnCq3SwVgqjuXc1tEPYoh-3A6f9J4Aagb-DM6lY6-74VJrl0RMegtvjQNPIvO8vZekUiJOBqQGadoFtj2sJkGokyJu3TQNmscWqMK567sdQClYwT7BFsgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36d4fc7f4a.mp4?token=iW5JpdzvV9btOMOQ9wROvw0V1zxdZ4M5KYwq2l50zhuJy4pdbxgmB1ILxP165bRRO-_XBiR8o9SBWloBn1Ipx4tinL-U0jJcWeXrmV5xE3vPTqamgGu8RHEVZ4YGaflHnEnGJscPemjhUWRiAdSdhd0-zDxbUk7XTfD1l-Am0CFlXxczdW-RcycCCw7qj8g7Li-zc6TEK5UdlF2ANmvD1VfjZaAvRNiBSnCq3SwVgqjuXc1tEPYoh-3A6f9J4Aagb-DM6lY6-74VJrl0RMegtvjQNPIvO8vZekUiJOBqQGadoFtj2sJkGokyJu3TQNmscWqMK567sdQClYwT7BFsgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قائم‌پناه، معاون پزشکیان: اگر قرار باشد نظر رهبری هر آنچه که می‌گوید اجرا کنیم که دیگر نهادی نباید وجود داشته باشد، دیگر مجلس و شعام معنا ندارد.
🔴
رهبر نظر می‌دهد و نظرش کارشناسی می‌ شود؛ دوباره بر میگردد یا می پذیرند یا نمی پذیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131405" target="_blank">📅 12:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131404">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb1b5f1dc8.mp4?token=A13bc789g6IzEN7QRPIZnPfE22JuaCuJWhFdvp3OdgBJRN6XSw49SYTdDJxpiwwgsyLXNFI09Whm5k4WKhvn_ZKbJAucEj9OkbY6A_YJ2JGw6jBE22vX22bY_8cmptWxfHTO-QcXWakySOi_m9RlZa6QzTJY1WZa3IJZT9pB6N8H9jF6RHql_K6DKduf00MPUNWSVvDGVaA0NdBwtk6H2Z32BfPX8SCSwOTLto4wfvSBKkBZVYBqqKtv7i1Oysrbqrd04Rv2dk3OvtjCtzqDpbUDhY1bSWFrvAS0Dv_ieQfuVAlRB7zp635AbWS8gMejklCG25Ob-m09pxhFcP0y0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb1b5f1dc8.mp4?token=A13bc789g6IzEN7QRPIZnPfE22JuaCuJWhFdvp3OdgBJRN6XSw49SYTdDJxpiwwgsyLXNFI09Whm5k4WKhvn_ZKbJAucEj9OkbY6A_YJ2JGw6jBE22vX22bY_8cmptWxfHTO-QcXWakySOi_m9RlZa6QzTJY1WZa3IJZT9pB6N8H9jF6RHql_K6DKduf00MPUNWSVvDGVaA0NdBwtk6H2Z32BfPX8SCSwOTLto4wfvSBKkBZVYBqqKtv7i1Oysrbqrd04Rv2dk3OvtjCtzqDpbUDhY1bSWFrvAS0Dv_ieQfuVAlRB7zp635AbWS8gMejklCG25Ob-m09pxhFcP0y0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اتفاقی جالب در تجمعات شبانه
مردها: گندم و جو ارزونیتون
زن‌ها: تنگه، نمیدیم بهتون
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/131404" target="_blank">📅 11:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131403">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
خنده لیونل مسی از بازرسی بدنی او توسط آمریکایی‌ها روی باند فرودگاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131403" target="_blank">📅 11:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131402">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
الجزیره: حمله روسیه با موشک‌های بالستیک و پهپاد به کی‌یف و دیگر مناطق اوکراین
🔴
۱۳ نفر کشته و ۵۶ تن دیگر زخمی شدند
🔴
مسکو: تأسیسات نظامی و انرژی و فرودگاه‌های نظامی در چندین منطقه را هدف قرار دادیم
🔴
زلنسکی: پوتین مدت‌ها است که خود را برای این حمله گسترده آماده می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131402" target="_blank">📅 11:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131401">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/143916ad31.mp4?token=lyKUcrIPdqOscxlbVKIKlOlftokXCJKIegBT2eWPJcF7HpC3MZ5LhuGdz12WdgteuusBuA1T4-a_tbxS4uuT9dtlUMO09bLFZBZsmjWyvrhgVn9FlXN90fYdi-K5Kwse6UCGplPP6QrOKElUF2WvQbcvbZY4Roh_SDuVp0bIyK1yo6msMPyqT94qzoNKiaUELtVO6-BwfPUJVQnW9DfSBJnK0J5scdapd4wGDbhiZ9ohhBDYS2WJ6Fw0dU0LMQxOehXEDqLUldeONvlsUOzAwq5GsUAIF3wEj74efYCAiM_XnMofhKekiobU3DlHzOowrVCwoxdMqFSF7VpNiRrwNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/143916ad31.mp4?token=lyKUcrIPdqOscxlbVKIKlOlftokXCJKIegBT2eWPJcF7HpC3MZ5LhuGdz12WdgteuusBuA1T4-a_tbxS4uuT9dtlUMO09bLFZBZsmjWyvrhgVn9FlXN90fYdi-K5Kwse6UCGplPP6QrOKElUF2WvQbcvbZY4Roh_SDuVp0bIyK1yo6msMPyqT94qzoNKiaUELtVO6-BwfPUJVQnW9DfSBJnK0J5scdapd4wGDbhiZ9ohhBDYS2WJ6Fw0dU0LMQxOehXEDqLUldeONvlsUOzAwq5GsUAIF3wEj74efYCAiM_XnMofhKekiobU3DlHzOowrVCwoxdMqFSF7VpNiRrwNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روضه یک مداح نریمانی برای جنوب لبنان: ۱۱هزار خونه صاف شده؛ آقایان چرا نمیزنید زیر میز مذاکره!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/131401" target="_blank">📅 11:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131400">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-c7PyPd_IZLx_wqIwytSWyac9l-8EP-hMsX-FalBRaN9Ype-pUzy4RttMH5pDjF69JatDB8z0O1hpfbca1zHWIObAb1-zuWijaow58qnlIjOpdb7gTHtCggbMbltUSDm04wEtiYrxs3nDuNcJHrWlizizO_ItLMIs-6099R6GYUTWCefXXFP-xXsbqi-v2HcqGAvJwPckBdTc6ktudi_7kA7QXkwAyqmDu9xhF4CtyJUl28zaMfbjTP6mlIpXHGVht7ScNed2otNMwohDYNKMA77CfLX0_DWCBUrHnG2H9QC1ErFv_yq_adXZENnbfR3iX87UDKBiXlw2XqeBA6Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عبور تتر از ۱۷۷ هزار تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131400" target="_blank">📅 11:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131399">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0_r7IsEl2iHHDBF7ESFa04gUBOZQQ2bUr9pE4sizZ2gw4KwRccLGipHl5lNNPbsjLZc0C9znGByU1Hf2wJD5W-GvwHVY38py-9ElzRbb1V0ucoOedhjJE_je6YfwVGFZwn0DQB24MWvVv5KBc4BMsfw2slkkESSNdsC0KWsKa7BzFdtZ31wpXcXA3nloZxGcKQ5lFFX4VBIHrhF1724o6F0Oys9WEXrQbdwsnbot8Lo_wu4Zq66Fbb0uT4IA2U7zqQyG1ArijGtkG7iM-O350womt_Tg-g4ZjMQLlgrkQDhcb2_R639gWb3ybhLxC6tgVwR0c3C7OSGEExd-ilTGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت
🔴
وزارت امور خارجه پاکستان اعلام کرد ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند.
🔴
طبق اعلام اسلام‌آباد، زمان برگزاری نشست بعدی در اولین فرصت ممکن پس از برگزاری مراسم تشییع رهبر سابق ایران تعیین خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131399" target="_blank">📅 11:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131398">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQSScnDmzD0U9Bl3O7YyobI9QN9JxlyI5Gko82JgMyGzEPtpgbgDDyckaMIvY6FcjrnO-DvLCOhDwr84DNLbXY_gcNLAjuR-IoLGmketm9LLDbgf5otY0uHPDatEUQ0Akb3Dfd3aMMoleCdSpmnrStmbDX4sNOutSu8_QoRemLmlShBRTPNKRpA1BzVaPaLklaMkiCioPy8zmoMT2NWvwMJofNvX_okLJHgyFXpu60oHBXE2b9dY_zQcJy6f6OFJdFR1ReHFlak-T22jOQMFVb8C5RxxFlfNmwdYqK7jYACwhOnMBTptCe-LTWr6MKsEaeCSbINwKglewB0pEVJzDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تیتر عجیب ایسنا درباره مذاکرات دیروز در قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131398" target="_blank">📅 11:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131397">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ایران و مصر رکورددار شد
🔴
طبق اعلام فیفا دیدار ایران و مصر، پربیننده‌ترین مسابقه جام جهانی با ۱۰۷.۴ میلیون بیننده بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131397" target="_blank">📅 11:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131396">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
منبعی بلندپایه به العربیه: توافق شده است که امکان استفاده از بخشی از دارایی‌های مسدودشده ایران فراهم شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131396" target="_blank">📅 11:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131395">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
فوری / توی تجمعات شبانه، برای کشتن ترامپ و نتانیاهو، صد کیلو جایزه تعیین شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/131395" target="_blank">📅 10:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131394">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
عراقچی : هر تهدیدی علیه مردم یا رهبری ایران، با یه پاسخ فوری و خیلی قوی روبه‌رو می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/131394" target="_blank">📅 10:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131393">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
سقوط قیمت نفت برنت به کانال ۷۰ دلار
🔴
بعد از افزایش عبور از تنگه هرمز، قیمت هر بشکه نفت WTI به ۶۷ و هر بشکه نفت برنت نیز به ۷۰ دلار کاهش پیدا کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/131393" target="_blank">📅 10:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131392">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
وزارت امور خارجه قطر: مذاکرات آمریکا و ایران پس از تشییع جنازه رهبر سابق ایران ادامه خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/131392" target="_blank">📅 10:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131391">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce007c4843.mp4?token=URR9fD-KCCilgeHEhP0yA5V9J41hJSc5M9seCYJ5V5tyOnN4V-6CcJueqz6GcV7t9yhyh9BjFagrT5iL8NUPVkXvQER5Vp5fudpCMXwTmZsNAa50l82QiefR0A56LGQijjgB7PmxYI79ZfV5EMLS8sRxRbtOg2lhvsT8JxSR6q60CpuvOIcqM3Gt6HFtGl0zWwjy2w7a2snfFb9XgwuzLai6rIw9XCV8VHCWfx-BXeddv9_qm6ZypUW2ekO-hjv0YD8g_IYWx-bawhTgR3YvzU20S8AsIu-_t436XA1cqX7ir3rupX_9rHOfREZEBCW5BxQPe-6uT2FTs6Nje4mNqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce007c4843.mp4?token=URR9fD-KCCilgeHEhP0yA5V9J41hJSc5M9seCYJ5V5tyOnN4V-6CcJueqz6GcV7t9yhyh9BjFagrT5iL8NUPVkXvQER5Vp5fudpCMXwTmZsNAa50l82QiefR0A56LGQijjgB7PmxYI79ZfV5EMLS8sRxRbtOg2lhvsT8JxSR6q60CpuvOIcqM3Gt6HFtGl0zWwjy2w7a2snfFb9XgwuzLai6rIw9XCV8VHCWfx-BXeddv9_qm6ZypUW2ekO-hjv0YD8g_IYWx-bawhTgR3YvzU20S8AsIu-_t436XA1cqX7ir3rupX_9rHOfREZEBCW5BxQPe-6uT2FTs6Nje4mNqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک پمپئو، وزیر خارجه پیشین آمریکا: نباید انتظار داشته باشیم که ایران به شرایط تفاهم‌نامه پایبند باشد، زیرا جمهوری اسلامی هرگز به وعده‌های خود عمل نمی‌کند. آنها فکر می‌کنند اهرم فشاری برای مقابله با ایالات متحده دارند؛ بر عهده ماست که خلاف آن را ثابت کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/131391" target="_blank">📅 10:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131390">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
کی‌یف ایندپندنت: حداقل ۱۱ کشته و ده‌ها زخمی، پس از حمله روسیه  به کیف . روسیه یکی از بزرگ‌ترین حملات ترکیبی موشکی و پهپادی خود را در طول شب به کی‌یف و دیگر شهرهای اوکراین انجام داد.
🔴
این حمله به ساختمان‌های مسکونی، یک هتل در مرکز کی‌یف و زیرساخت‌های غیرنظامی آسیب رساند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/131390" target="_blank">📅 10:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131389">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
رئیس سازمان وظیفه عمومی فراجا: مشمولان دارای سه فرزند و بیشتر تا پایان سال ۱۴۰۷ فرصت دارند از معافیت سربازی بهره‌مند شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/131389" target="_blank">📅 09:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131388">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
آمریکا: در پی فرود اضطراری یک فروند بالگرد «ام اچ-۶۰ اس سی هاوک» در دریای عرب، یک نظامی آمریکایی مفقود شده و سه تن دیگر زخمی شدند
🔴
تحقیقات درباره چگونگی وقوع این اتفاق ادامه دارد
🔴
هیچ دلیلی در دست نیست که نشان دهد این حادثه، ناشی از اقدام خصمانه بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/131388" target="_blank">📅 09:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131387">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
واژگونی قایق گردشگری در پاکستان با ۷ کشته و یک مفقودی
🔴
پلیس پاکستان اعلام کرد که روز گذشته (چهارشنبه)، پس از واژگونی یک قایق گردشگری در ایالت «خیبر پختونخوا» در این کشور، هفت نفر جان باختند و یک نفر دیگر نیز مفقود شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/131387" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131386">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
بلومبرگ: عبور نفت از تنگه هرمز، ۱۰ میلیون بشکه را رد کرد
🔴
یک مقام آمریکایی شامگاه چهارشنبه مدعی شد که حمل و نقل روزانه نفت از طریق تنگه هرمز، از ۱۰ میلیون بشکه فراتر رفته و ۵ میلیون بشکه نفت دیگر هم از طریق مسیرهای جایگزین منتقل می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/131386" target="_blank">📅 09:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131385">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
انتقام روسیه از حملات کی‌یف
🔴
روسیا الیوم با اشاره به حملات روسیه به اوکراین اعلام کرد: حملات شبانه روسیه به کی‌یف یکی از شدیدترین عملیات‌های اخیر مسکو بوده و در واکنش به حملات کی‌یف علیه زیرساخت‌های غیرنظامی روسیه صورت گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/131385" target="_blank">📅 09:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131384">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
سایت The War Zone با استناد به گزارش‌های محلی اعلام کرده است که هر شش بمب‌افکن استراتژیک B-52H Stratofortress حاضر در پایگاه RAF Fairford در بریتانیا، پایگاه را ترک کرده‌اند و احتمالاً به ایالات متحده بازگشته‌اند.
🔴
دوازده بمب‌افکن استراتژیک B-1B Lancer همچنان در پایگاه باقی مانده‌اند که این تعداد نسبت به هجده بمب‌افکن استراتژیک قبلی کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131384" target="_blank">📅 09:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131383">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeVTa6l2K-TQxLZtxVZIf33FV-lQEpeY1wmaIt9fUsTIWQnmz2sI4vUJIvIcGjPr-_8gL3uKJ3iqsL6gIjUdM-tPVGj_nlJ7L2fxBrH7ZcZZ3VSg7mFaZNWh7bFd8pHrsFqAHD92TJrc7muTvGRawDHHfQ3RVk4NBlg5k4z3RVu9jqD2JiGWxvKjSuCMzEzATlY-QEsVU4DwlJIR_UFJUSahuJ_tZfSwwWBNJngUfvU4wypB6gVavXVDWhBePVUAW7JfYfPmSeSeaHeEmq1Ezk7xD8Yc6ExJ_IFmNCrFLNzQtB9poLhBMWOtAByTIcGp2GYZ6IIdIiMXXCxVgp2GcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی خطاب به قالیباف: هوچی‌گری هم حدی داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131383" target="_blank">📅 09:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131382">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سی‌ان‌بی‌سی: ایران از زمان لغو محاصره دریایی توسط آمریکا در ۲ هفته پیش، بیش از ۴۰ میلیون بشکه نفت خام صادر کرده است.
🔴
‌تهران اکنون نفت را با ۲۰ درصد حق بیمه می‌فروشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131382" target="_blank">📅 09:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131380">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3197e89311.mp4?token=JPXYth-jF3CRxNotxnD-CDxXhas_ejAXRqd8YZn9HkKQIVaIc7r8PiN1WzhSlTM3h45oMnNwUuprQKaclbcqWAZ1PAMg4evtnfnA_W56DZKexsh69Xg7JZqsYYtN8m2hJEJBoNBo4AhyTuYoDMo3dOcAzIWg41ED24PJ45q1Iywy34cVNwmlU7FMBuZ2nAH71tGMZkcPBfA97o-8XsL6NXkEPUJCwS_RljjtLiOjrSZ9zNYHVCA5NfenfF6SyWwkngdv1R4QasNddfQPA9n94IKtCQHJwPMezhBk0aemYFUzIzj0Ee3-RBOjVStjqEBRKtKYDV4yVa5uy6BJka5E9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3197e89311.mp4?token=JPXYth-jF3CRxNotxnD-CDxXhas_ejAXRqd8YZn9HkKQIVaIc7r8PiN1WzhSlTM3h45oMnNwUuprQKaclbcqWAZ1PAMg4evtnfnA_W56DZKexsh69Xg7JZqsYYtN8m2hJEJBoNBo4AhyTuYoDMo3dOcAzIWg41ED24PJ45q1Iywy34cVNwmlU7FMBuZ2nAH71tGMZkcPBfA97o-8XsL6NXkEPUJCwS_RljjtLiOjrSZ9zNYHVCA5NfenfF6SyWwkngdv1R4QasNddfQPA9n94IKtCQHJwPMezhBk0aemYFUzIzj0Ee3-RBOjVStjqEBRKtKYDV4yVa5uy6BJka5E9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوکراینی‌ها پیش از حمله گسترده موشکی و پهپادی ترکیبی روسیه، در متروی زیرزمینی کی‌یف پناه گرفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131380" target="_blank">📅 08:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131379">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
رسانه‌های محلی فلسطین گزارش دادند : قایق‌های جنگی اسرائیل به سوی سواحل «خان‌یونس» در جنوب نوار غزه تیراندازی کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131379" target="_blank">📅 08:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131378">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
نیویورک‌تایمز به نقل از دستیاران نخست‌وزیر عراق مدعی شد: ایالات متحده انتقال دلار به عراق را از سر گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131378" target="_blank">📅 08:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131377">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سازمان امنیت دولتی یمن در سازمان ملل: حوثی‌ها با حمایت ایران بیش از ۱۸۰ حمله به کشتی‌ها انجام داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131377" target="_blank">📅 08:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131376">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGUZfsWpTIxHVLRCBotc7YyAowkh7iBqZXtBpvLfYixio_aL9p2OQe419JdkMWW2s3Dn_Zx2RB4LBw3NEZVw-iGbXW5QFzB4-upsxO6bCpY41sQFifppcoqh_2HGMSetbrOTmUBGZGsQMJf_ePRndLddJWpsL6GsTFIJTO7hmVlPubPbSQ1gD0C40aPzwYHkoroOcxD90JsCk9IU5AozTEUSWW4EWVHhxy3gwJBnEfLFjrnXP3iIuyLvWES1WmmcjZ3XssFmp1VzzIU7Y95aH2yvJAZMV_V3oujeOTi6T-ZDI0QtVhjBfwDt5JdryQJvKmyIC0XEIokrwv8BB-Z-2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب آبادی: تنگه هرمز زیر فرمان ایران تعریف می‌شود نه سنتکام
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/131376" target="_blank">📅 08:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131375">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
الجزیره: ایران پس از مذاکرات دوحه، کانال ارتباطی برای نظارت بر تفاهم‌نامه با آمریکا ایجاد می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/131375" target="_blank">📅 08:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131374">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
یک منبع ارشد به العربیه: به ایران اجازه داده خواهد شد تا محصولات کشاورزی آمریکایی را با بخشی از پول‌های مسدود شده‌اش خریداری کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/131374" target="_blank">📅 08:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131373">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
بخشایش اردستانی،نماینده مجلس: تجمعات شبانه باید فورا جمع بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/131373" target="_blank">📅 02:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131372">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2A6Vo2cqMC49_0wOOjhlh4wpL6wVjAicoguzQTiTUMO4k_t1xNfuHirL9bD8cr7-W-8fJoyeBlWc3DanG7P3tKb7B7b_zUuCu-Vwxpr0xGL031YSkmidNAHvc3bqn_T7KYilvGRdYx6fqKQt2x8lID7BrwV7Bdy_50bN8md2ev1BstXWBhrJKUPtu6XxZhPjlrhXFYkS9Ln-RqBtcNMSPiC3M0AghkBWiBg2fGnVGsm5AY-WLIPCxJyKFUZECqkjYy4_L1mTPtt4Uvs810SpnR_T2bpQtJQFYyL5xahD6piOltuJEkXz1Dm1brkyNcHs5J-DeGJ_v5k3hE_e7aqfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش ایالات متحده آمریکا اعلام کرد که در پی فرود اضطراری یک فروند بالگرد از نوع «ام اچ-60 اس سی هاوک» در دریای عرب، یک نظامی آمریکایی مفقود شده و سه نظامی دیگر خدمه این بالگرد نیز زخمی شده اند که وضعیت جسمانی آن ها پایدار گزارش شده است.
خبرگزاری «رویترز» به نقل از ارتش آمریکا همچنین تاکید کرد که هیچ دلیلی در دست نیست که نشان دهد این حادثه ناشی از اقدام خصمانه بوده است.
در بیانیه ناوگان پنجم نیروی دریایی آمریکا آمده است: «شناورهای نیروی دریایی هم اکنون در حال انجام عملیات جست وجو در منطقه برای یافتن یکی دیگر از اعضای خدمه پروازی هستند که همچنان مفقود است. همچنین تحقیقات درباره چگونگی وقوع این حادثه ادامه دارد.»
در این بیانیه همچنین آمده است که این بالگرد در منطقه بر روی ناو هواپیمابر «یواس اس جورج اچ. دبلیو. بوش» مستقر و به مأموریت اعزام شده بود.
فرود اضطراری بالگردها روی آب می تواند حتی برای خلبانان با تجربه نیز بسیار خطرناک باشد؛ زیرا بالگردهایی که بخش فوقانی آن ها سنگین تر است، هنگام برخورد با آب معمولاً به واژگون شدن متمایل می شوند و ممکن است به حالت وارونه در آب قرار گیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/131372" target="_blank">📅 02:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131371">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
حادثه امنیتی در ناو هواپیمابر جورج اچ دبلیو بوش در نزدیکی ایران و دریای عرب.
🔴
نیروهای نیروی دریایی آمریکا در جستجوی یک عضو خدمه مفقود شده از هلیکوپتری هستند که از ناو هواپیمابر جورج بوش برخاسته و در دریای عرب به صورت اضطراری فرود آمده است.
🔴
سه نفر از چهار عضو خدمه هلیکوپتر با موفقیت نجات یافته‌اند و در عرشه ناو هواپیمابر در حال بهبودی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/131371" target="_blank">📅 02:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131370">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6VfnJdwUgASkjsL2zVcTPkQfcmzDHsKVNFFAbgyeX898uthxREQTvxxcuxyG3bybDGvWzsZj7XrBkwrvdPwyJfnABbLgrolMvv1vewFeMLcdqcTXzC3LDWLZkn9ycHC46g1OsNim2enSudoVXR5IYTjkEX8CyadpBBXTvppbc7NAVxDBQDCtx3g_HD8NknLyooyaakhwoJyN9dSYncJeaGYxfw2PAXNYf-9nOgHU4rrXJWtaDOoM1NZjq9TOGHwLDFAZz2w6YXeTCFyRYJPyr_JNLEzEb_FCCvmWnLdOyjTaIXvYW5BZ7tVzCYMDqUp7dG8Box63VXV2EhE9vDG3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: برای مراسم‌ تشییع، همه مردم بیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/131370" target="_blank">📅 02:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131369">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromm.m</strong></div>
<div class="tg-text">کشور ایران از بیخ فاسده
میترسن یکیو برکنار کنن اونیکیارو لو بده
پس نتیجه میگیرن داخل ی سفره بشینن و بدزدنو بخورن
فوتبال هم اینطور شده</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/131369" target="_blank">📅 01:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131368">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
وزیر ورزش عربستان سعودی پس از حذف تیم ملی این کشور از جام جهانی، رئیس فدراسیون و چند مدیر ورزشی این کشور را عزل کرد، همچنین سرمربی تیم هم اخراج شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/131368" target="_blank">📅 01:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131367">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: مرکز فرماندهی منتسب به سپاه پاسداران در لبنان توسط ارتش اسرائیل (IDF) تصرف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/131367" target="_blank">📅 01:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131366">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnkZvk6f4GOCUF5KoSUvKk0aIx9kfcw8fTvvvQph6YMoDak4FAJymAYbT41dbt2hIbdYvPIPeuDJgLBSVRwCfY8bWYjgwTHMYmJSiBIfHoi_6jGIUsikaTQgrvPeSyaZnSxfDA8vmqsNUD_pei9BfqZdryIIsz0s66RCXiCOoMddVn3RAxPgz4KdKYLcAyFuGWt3w2gL5Y7K7NHQ0G7zJ269VRqsmBCYY_GmBAOSkMH3zs3inmU7wDIlf6-9LB_G-hYolt-LV2ecZHYRtnt6DCevvypjrcV8Q2TPSLWFW6SY5NA8oEd6bqCbv8MaqpFiF1UDAj6Fdc_V4-m-9WkOpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به تاج و اعضای فدراسیون که رفتن به جام جهانی مجموعا بیش از 50میلیارد تومان حق ماموریت داده شده
🔴
فک کن بری جام جهانی و بهترین هتل مفت بخوری و تیمت هم برینه و ۵۰میلیارد هم بگیری
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/131366" target="_blank">📅 01:49 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131365">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
تاچ: پیگیر هستیم تا به افتخار آفرینان تیم ملی خودرو یا ویلا به عنوان پاداش داده بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/131365" target="_blank">📅 01:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131364">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vobQxTGXFGK7vxa4sIXMRVRRjwkIqvW2Yzpq5Hu-EGqJpuKCVWExPjPI7_5CSO8UWysbeKH0p_2sNEA_7Mp1OIq0ZJ6P5qzS6zdYv-4JJ8dsXzeQ_Vc8zwv2x3WleeNW5ygYDVumlEW_cU1XOk7lEe8RttrNjY0fP0rFKA8qHLvndE3Raj0jOADHU2jbQiYoJjWcJ8VMm_PA8kSUB0eCBpwvX8LEXWaJFMLH8vxpHKSybcijOnd-qzf8rk8T8RKQSSN03iwzDQqA1mVREyHGwybNouQKN9dBYQxRVgqkVse1nHNMwQVSg4g3RIPDHjkw_cmIt2Ngi_yl-eFvuKwkpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تاچ: پیگیر هستیم تا به افتخار آفرینان تیم ملی خودرو یا ویلا به عنوان پاداش داده بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/131364" target="_blank">📅 01:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131363">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">🎙
فردوسی پور:
نکنه پس‌فردا صبح با سوییس بازی داریم ما خبر نداریم اینا خبر دارن که مراسم استقبال گذاشتن!
@AloSport</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/131363" target="_blank">📅 01:22 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131362">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3740efe365.mp4?token=h15ygkxo9hdf536b1TFuUveRGEjAQmfsRbiK6nA7g6Vouu20Fza0bQ37i-orHYqKI6waPpTq-hB5x27lZktgSaTIDyhHO4goTvjs7MaS92AQ6i7W1WJsFdb0s9d2BrBCFAQEKNEzgApCxdA4k4Knn0c_PouvA-SHhaG7nezn7qOZE6O6lqMBWs5dVUNqXn79KKUYagcKKWSHYt8q39BovycYuFlhE1B0V7GHCm5f5ucori9Gw2LZfTK-_kj2C1qDHqcHleQwCbvCYacYWF71pnZPr6_H0zUnqPf0-HWz7L7ZvdHwyYEBs1Q1J4yB7G9vKQy3pcUvWTOQwro-LRVLFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3740efe365.mp4?token=h15ygkxo9hdf536b1TFuUveRGEjAQmfsRbiK6nA7g6Vouu20Fza0bQ37i-orHYqKI6waPpTq-hB5x27lZktgSaTIDyhHO4goTvjs7MaS92AQ6i7W1WJsFdb0s9d2BrBCFAQEKNEzgApCxdA4k4Knn0c_PouvA-SHhaG7nezn7qOZE6O6lqMBWs5dVUNqXn79KKUYagcKKWSHYt8q39BovycYuFlhE1B0V7GHCm5f5ucori9Gw2LZfTK-_kj2C1qDHqcHleQwCbvCYacYWF71pnZPr6_H0zUnqPf0-HWz7L7ZvdHwyYEBs1Q1J4yB7G9vKQy3pcUvWTOQwro-LRVLFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری صداوسیما جوری داره از قلعه‌نویی تعریف میکنه که خود قلعه‌ هم تعجب کرده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/131362" target="_blank">📅 01:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131361">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=KIs_p6tWEUN7xETc3HuZKpyusfbemj_1EOEuvbOT8kasaDQFjDEJ2ATwrAsSm1kdB1vR1AXTF88PtVODiTpb1kFq2qMXU70SxSQHWcGsWG2FoyMQtwvX1rrJIBO7AQGuyC7bErColOFV_hfCLA6vRXQtcf0GrPJX4bPDBdkTbfWnae2pJGI_8nt-49rZ8bG7Getwc-KozRsvAl2n3gDn8PoZ_R53ei6_qV2amn5FBEs9_W8Hxhli3J2Zic7khLxoPFDQ2uCffuNfKBormMGDpPZ8jsH6OSmvwRJzdhGQozcz8vsa4foTUc5O7_xHUDSVfbpGIB95yh_5zWF4Ea1AtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=KIs_p6tWEUN7xETc3HuZKpyusfbemj_1EOEuvbOT8kasaDQFjDEJ2ATwrAsSm1kdB1vR1AXTF88PtVODiTpb1kFq2qMXU70SxSQHWcGsWG2FoyMQtwvX1rrJIBO7AQGuyC7bErColOFV_hfCLA6vRXQtcf0GrPJX4bPDBdkTbfWnae2pJGI_8nt-49rZ8bG7Getwc-KozRsvAl2n3gDn8PoZ_R53ei6_qV2amn5FBEs9_W8Hxhli3J2Zic7khLxoPFDQ2uCffuNfKBormMGDpPZ8jsH6OSmvwRJzdhGQozcz8vsa4foTUc5O7_xHUDSVfbpGIB95yh_5zWF4Ea1AtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشک‌های مهدی تاج پس از کسب قهرمانی در جام جهانی فوتبال 2026
@AloSport</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/131361" target="_blank">📅 01:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131360">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiJyVK_HWOVmrj6mAp4ypUFtU3ljrux8Dxis1362Lzrn9enXBBfkZDIITRNmvsjhHZdy1NYlySjZlpt8bMRyFukHKL8h84NdOJ4Rj6HsfDNMLbXNYo7KRyVbSJKR1pl-bvTW9RYVIUz2fmpK9RF1R-ZD6LUKrbY1aga0Qi14joXhS7YNZ6xmQCV6dyC5DlahAkhVr9NUWj9nMHn-4feNZR947R3ck_SC7esZnIUxfS6j3fPfAE6jlJUhnao9a_YWc_AVfD01mdzsSBkM8lifEdPnmCRHe45mzNTzGiF1IvNZlYYoIA85TL5b38dHXb483n9MKOYikSj9dv4cjaWC2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع رسانه‌ای گزارش دادند: مقر احزاب تجزیه‌طلب در منطقة «ديكلة» واقع در شمال عراق هدف دو حمله پهپادی قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/131360" target="_blank">📅 00:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131359">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
هم اکنون حمله پهپادی به سمت اقلیم کردستان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/131359" target="_blank">📅 00:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131358">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ترامپ:  در مورد کوبا، پس از دهه‌ها و دهه‌ها، به سمت ما می‌آید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/131358" target="_blank">📅 00:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131357">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/386c345efc.mp4?token=cT95tthDFhXP6ibOcu9xj0FGDoVyAnxBiydgnytc9mJ8QpeHBTHLTQmijx0cdJS-0C2_G3J4sKUyD63kkhteBAPYAZVwl0IK6Bpi3nnO6b0m3oP3YiVlxg3Ux1EeuBnPzkCiuoKsYMCR5maAF-69gYlTtIbnCNuJkBFr1P5_uikPWHcJIcrMLyOJaXL363AJTyT4z2x2d2nNS1rRD1AvQSvk6R5_vn22sbIrJ5ALpwwoNFMaWdFvwEhfJceVGHtzUmKPu0of9xaUi1HWqQh-JspB5NBETInecI59VRLTbVBvS8nFZcXm7ArEaxTBt0a7wHFOfGhEW90t9bVc9QcNI3oMt0qM4quLE684MsrFJCKwkXhUL2ypuaMgekYqatPsHVor1ewqnCbFKeNjX2WPV_Yx0KLvOkltXNObOJMbKNMXVTPFbb3gjvuxkvLRotJhtrh-YNAdMgzFlZZj1uOiXr4VLBSjuPqaMLcYpscpnjToYWw5kT1h411jq3G2WYjd9TqGG6oeLWGdTGuhE906EvurTg3RJpbbXZrVQuyyD0DxihM6tuw7XH_boiQ1u8vxp-UY1mLhkP1AVTMuuhxlKUNWu3Jn9gG8Sqm-lcbiNSOxavLS89VR-LEmnTIZ_p7DYuNyYf8dpQdqPxkL7TSMZattcpI-p9CWXEsQzEum0Ws" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/386c345efc.mp4?token=cT95tthDFhXP6ibOcu9xj0FGDoVyAnxBiydgnytc9mJ8QpeHBTHLTQmijx0cdJS-0C2_G3J4sKUyD63kkhteBAPYAZVwl0IK6Bpi3nnO6b0m3oP3YiVlxg3Ux1EeuBnPzkCiuoKsYMCR5maAF-69gYlTtIbnCNuJkBFr1P5_uikPWHcJIcrMLyOJaXL363AJTyT4z2x2d2nNS1rRD1AvQSvk6R5_vn22sbIrJ5ALpwwoNFMaWdFvwEhfJceVGHtzUmKPu0of9xaUi1HWqQh-JspB5NBETInecI59VRLTbVBvS8nFZcXm7ArEaxTBt0a7wHFOfGhEW90t9bVc9QcNI3oMt0qM4quLE684MsrFJCKwkXhUL2ypuaMgekYqatPsHVor1ewqnCbFKeNjX2WPV_Yx0KLvOkltXNObOJMbKNMXVTPFbb3gjvuxkvLRotJhtrh-YNAdMgzFlZZj1uOiXr4VLBSjuPqaMLcYpscpnjToYWw5kT1h411jq3G2WYjd9TqGG6oeLWGdTGuhE906EvurTg3RJpbbXZrVQuyyD0DxihM6tuw7XH_boiQ1u8vxp-UY1mLhkP1AVTMuuhxlKUNWu3Jn9gG8Sqm-lcbiNSOxavLS89VR-LEmnTIZ_p7DYuNyYf8dpQdqPxkL7TSMZattcpI-p9CWXEsQzEum0Ws" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره مدال افتخار
:
من پسران زیبایم را می‌بینم. فکر می‌کنم می‌خواهم یکی را به خودم و یکی را به آن‌ها بدهم و یک سه‌نفره خواهیم داشت.
🔴
من به آن‌ها مدال افتخار کنگره را برای چیزی می‌دهم... برای نبوغ آن‌ها در شکار.
🔴
و من یکی را برای پذیرش «روسیه روسیه روسیه» یا چیزی شبیه به آن دریافت خواهم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/131357" target="_blank">📅 00:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131356">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ترامپ: کشتی‌ها با تعداد بی‌سابقه‌ای که تا به حال کسی ندیده است از تنگه هرمز خارج می‌شوند، ما در حال ثبت آمارهای بی‌سابقه هستیم و قیمت نفت در حال کاهش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/131356" target="_blank">📅 00:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131355">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ce1f21322.mp4?token=aE8IxnsNEdNScSibPo9Y6hzqos4Pl5Onr95aS05B10z4_vUpZzpzDq0BIHK27CVeyomT1qR0nZqDx2AFRh6sck5uCtiig45DemtptAGz-JWwEXrd3r7cL0mBmegd3__ptipERegcQROcbowxSB0xbBl3pyRbh00037t5i3fts0nUPS0pTtnWSDIpONdf8ZIiiMRREwGrlQvMZWU2jRLexv65PQsbn_5wnlF7W_8a2a62o_8g5pVtXw9GMn6yNV-vafKxM7sOXGc0TQMJLTj2JhFb55iiSC4a43ZAsQ7ZKrlPL326cFluut4I_I5zVP9k822rjL6vWPQyduxBLHSmZYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ce1f21322.mp4?token=aE8IxnsNEdNScSibPo9Y6hzqos4Pl5Onr95aS05B10z4_vUpZzpzDq0BIHK27CVeyomT1qR0nZqDx2AFRh6sck5uCtiig45DemtptAGz-JWwEXrd3r7cL0mBmegd3__ptipERegcQROcbowxSB0xbBl3pyRbh00037t5i3fts0nUPS0pTtnWSDIpONdf8ZIiiMRREwGrlQvMZWU2jRLexv65PQsbn_5wnlF7W_8a2a62o_8g5pVtXw9GMn6yNV-vafKxM7sOXGc0TQMJLTj2JhFb55iiSC4a43ZAsQ7ZKrlPL326cFluut4I_I5zVP9k822rjL6vWPQyduxBLHSmZYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : کنترل کامل. ما کنترل کامل همه چیز را داریم.
🔴
این فقط آغاز دوران طلایی آمریکا است.
🔴
بهترین‌ها هنوز در راه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/131355" target="_blank">📅 00:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131354">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a937d249f5.mp4?token=nlViZtUqYIzSbiwANi32cTUZ2Pm0uT7V3IfB1Y5yCqr5xoQMP_Zy_wJ_t907iT9SOsq-_oQIGvCSCVMEhZ6p1WG-G8jufoSfR4o_wszK1F7eCCcR6b0ASOX7C2JrsWOfnZAIwJfBvGkZkHdsyKt26WEJ6CBdukHRMYxaLOoDx-BqNC4aae1lN2JiE-BL1FJtVtKf12GOhb02vApxEAw40fXj24d4J_tByTUryZeRgxyK_c-amAq-m1rmxObNv970KW18BsJRKPXhU8ye4EVzbU-FSKxMSrRiBwYYRQm4TlT74D7z_-bY05uqpuZQr9Us7BfiPHvGFwLLD6bwM2jyFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a937d249f5.mp4?token=nlViZtUqYIzSbiwANi32cTUZ2Pm0uT7V3IfB1Y5yCqr5xoQMP_Zy_wJ_t907iT9SOsq-_oQIGvCSCVMEhZ6p1WG-G8jufoSfR4o_wszK1F7eCCcR6b0ASOX7C2JrsWOfnZAIwJfBvGkZkHdsyKt26WEJ6CBdukHRMYxaLOoDx-BqNC4aae1lN2JiE-BL1FJtVtKf12GOhb02vApxEAw40fXj24d4J_tByTUryZeRgxyK_c-amAq-m1rmxObNv970KW18BsJRKPXhU8ye4EVzbU-FSKxMSrRiBwYYRQm4TlT74D7z_-bY05uqpuZQr9Us7BfiPHvGFwLLD6bwM2jyFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما بزرگ‌ترین زیردریایی‌های جهان را می‌سازیم.
🔴
ما در زمینه زیردریایی‌ها و دیگر موارد ۱۵ سال جلوتر هستیم
🔴
ما دوباره با کشتی‌ها شروع خواهیم کرد. قبلاً روزی یک کشتی می‌ساختیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/131354" target="_blank">📅 00:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131353">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
اکسیوس: آمریکا تلاش دارد ایران را از دریافت عوارض از تنگه هرمز منصرف کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/131353" target="_blank">📅 23:56 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
