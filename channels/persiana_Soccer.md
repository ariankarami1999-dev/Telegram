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
<img src="https://cdn4.telesco.pe/file/IDlIcgVzMC4pt-LUkL68bFxexMQ55XE5dU7OKE9PK8O5hOlBj3zUxsmfyp7hUjR_IvosrcnS3bgIo0bJgHepZqZON23PGvpHckxqKM2XqndUBST1OZuvrSNplbttYq_A2a9h4wge3yb5GS5YQr9608ZqGT34Petkh2D9MooMv5kvqg52t-wCvP1M7-RKVoFJ_LZ9LGYEQEV6Shse8m1_CeQsVuCyjbbgyHx6Yu-hgTBdXtx0Ah_FSf9cW_7Ca9QwljBjUNJpbZK4t49-PfF_PaVn6jirZs8W5Ik9xQ7oIMp2bhk8NGsaI2CqwjH0O-tHlFszLgocRnZDdpMuR7pIEg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 626K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 08:27:26</div>
<hr>

<div class="tg-post" id="msg-27130">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7ky3MnN16YfvEYwMV67zXITc0tkBtoGTHMDWvMLr5DQ-RbIjbHwo9n1p_UkVmXk6If4ojOA7GeuHMgrsajjtj5r7HszA0stC4lhDA5r1m7_Wlzqv1XeuaX4XLwe0wxyWpbwGH-SatELoo_UQTqZ5lLDusVzvgvQCoGlfOiCExRdtm7kCz6Mtsq2bj8KXfGYY9iVRzt7R93qkp8hX03jTSdGPL8IkQY0lfmOO7TGnznDPPkif7hHu50kIISxU-GxUCO3_YxRZM9sg9EKEN8GRm_0vkIQhQoeS8UIRRtUzO0_VUtVojcng095rJFXjTY9UV4w3jRvr1fcILm94m7g0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
درحالی‌تموم‌اخبار این روزهای نقل و انتقالات شده انتقال وینیسیوس به آرسنال؛ ستاره برزیلی رئال مادرید بی توجه به این اخبار با دوست دخترش در تعطیلات به سر میبرد و در حال عشق و حاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/27130" target="_blank">📅 02:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27129">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVrL2ZVHZdjWtce5zjjZEFDHo7RBwsTKHmuSghvyMmXA3-3bQIprdSPMqE49o6pdjBBc3E2o8CgU39zgft9EDxUzYLRjLD5FhQnTfTxd0LheDxTXpoarYSgLfk1Lck9ZVpkZDBOP5tp56pgnMM1yH1l5TWVNxIzJDLRiUuysTzf-HZQYsJmrZT9ilH-f2yVG1BS2QVztH8UxEYSV5g0qw68yVGmT8oyBMZMrARj7BUAne-aLgpvCH6aFb1Hyny8K9N5h9-KpCmhqmjuBioJ4WUGduz7gqncA_hiQgiS7m9PS6CN1rzG_GEevAucyqvzVINv8NrhsbsWJLiEO14gRGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بهترین‌و‌باکیفیت ترین ابزارهای هوش مصنوعی که از همه آن‌ها رایگان میشه استفاده کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/27129" target="_blank">📅 01:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27127">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnHb91UhO4uAYUrEC3XHp-156xTpKIPsITwEzJvAFP6VpGDrF8lv6veEASWVchPoYbvKvxpPDZZmhHoLznFlIDwyVBMWYbQl1qEtbvi1Z-NvM0_jFOiqBui9hKA9e5Ba9Ce0u900vA1ArwumthEoWsDwDeQxHzJFpC0vSytJJNtkU-79PtdUIdHJipcjTMGE3E00Vge3xuGqLzr1OCYqDqdLMWwuWqcBdQ4Rz4oDw1I_3Z9DQ9VdjMRDH4ToevUNAxif4uJnlPq3Z6c44ZTlVUF9x1JQGs-FD0rG8v5q0yrO9MI-1Dmpk9ZfqBDElg1cR4eqAvtKUUhUKXLOleOsXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
ازدربی‌دوستانه دلامادونینا تا دوئل شاگردان ژابی و اسپالتی در کشور هنگ کنگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/27127" target="_blank">📅 01:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27126">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfiPNVkQ6cn_Nqu90YM9A6cNW_cCqfSipXNFgquHphgb5BfnvKWtU0obNBLIvvG2xc5L4X-5K2fGfg7DdJ29YtNFNbCHX-f1R3kUrbHj3CFPPwMEx0Xc1C7_5aNGLC71kIMzkvAhz01o4ixSvBsMmRywNHFIMnt2yp4dcAiortv-sj9UYZQD0LUfn_o8uIfGsT-p14ajsMXvhdbFR7SIy2vu_26B94eu5Lp7VDgIG7XipGMWtqwf8XNvDLB_WNhei7eyDd47ayPTAgchvjxVaTJtvfF-GcNc606GgLkMr8SmpFIaIWaituRC2irpw9AXHNQ6VkSOxUDGUTxlM584CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
از باخت ماخاچ‌ قلعه با حسین‌ نژاد تا برتری بایرن و رم در بازی‌های دوستانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/27126" target="_blank">📅 01:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27125">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roXqTXiM32UW6_i4clNY1rEwASB0BRtbpzHQEr98PL5krpYGIMJyiJygVStDoftcss7U92Xi1wJJ_yQgAk7_d6KKfppsoZTEckImt-Hz2pQYO47-lD6G1HpCmsDMSXRFnu2e-EIXkR6wLXHH6fB92xyxYMM34JO7amsYRUzkg1uA9JvLMyOZtGcPwF8FH3wiM0j_r6wpgqDwj8bWtU5t3nNkQpFVLoIoBs31mFaCgrduT6vXVSJzScmoTEWXX_mfBmMyCRdDGUXNg0RUBKxl90moIYPomPsluAznme2ljKMB60GQ_lehT3Ue-24csr8iTsC8TO6wsqc4yBvBhpwo5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/27125" target="_blank">📅 01:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27124">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1X_JJEipGV5I_k4zJT99ZBtsMCsDUjgfgvkBC_TVhvekglmbehdrCK2FNbj6mD0tZyr-CyUbH3B9r4ccDIhjTcwyW7deFH6ptsIeEA56SP6rBnQvpEPkslvhBpEvb440yM8DoAxBYymXc07SownFjQrDFtckZFMyJlWXmKWA61vrDkfCYnb0LwFyYhi867Yy4g5fNYoepEjaFGA4U6CcIg_vw22SSJJ53PBJz8XDyV7GduvIlgZ7BAXRDrrPHTgmkJX6xyd7_v3H5i8TZSollYAVwenEty48fFDtXyWVFXLIphTP3eWqzoC9HruV6Pwa4KAYfsn5N0aCAIgXBNOFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تموم‌ شد؛ صلاح رفت سوپرلیگ ترکیه! با اعلام فابریزیو رومانو؛ محمد صلاح فوق‌ستاره مصری 34 ساله سابق لیورپول به ترابزون اسپور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/27124" target="_blank">📅 01:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27123">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjvSYGksE8eLNsCszDCJdUSLXrsw1r8knbFNYHHNRRc9KgRVsDw2aSRjRNQsaEwmWqyt52hl5Jm-VDyZf7mlVEYbJf9g95VpiWx8saIme1T-fq8BKHiXvBkjvSVlDuk38SSyqbuqJWd6SYxwENbEg0ibEqwkEJxfF4Z02JXEgydhDNuyumNT8kolG4Wz6IjnM8OIrxhWDF3Fn_qS9gzuhK_pg10-jMrJ8vw7GBNsoixGZQHttulWn_qHfZSiUB5NgtfoCdE1K1756nKaa8ZQMVJXqVF_nLDlhIzo2lBV48K4RpC15hYe7kAqI9rhntikadauvFPONS6B3wfx_179Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال: مسی؟ فوق‌العاده‌ست. من به نصف دستاورد هایی که او رسیده بتونم برسم بسمه. یامال برای رسیدن به نصف دستاوردهایِ لئو‌ مسی فقط به 455 گل، 205 پاس‌گل،660 تاثیر مستقیم روی گل، 22 جام، 4 توپ طلا، 3 کفش طلا، 4 پیچپیچی، 6 قهرمانی لیگ، 2 لیگ‌قهرمانان،1…</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/27123" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27122">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9Px2pTfHuSEjQ3yW49ToX5BpYq1i7SArOJfRSQ7GcLM9IEZy5pO0ckAe3nBcOZjuqSP5uqKSdyi6jCPnQRHohHTsDJso8yvqVBrT8hTq6pHVWfMyBG_vD3Z7UyIcNlCNGbLK4aBbq2URZUTEFmgcrvCCRWJxmsYJ0PXWRw6zlXUJ-1de05axC2sBSaZLkVhXYm7P3UbjUz11AMluokcywrCdErIUhIYO_hwo92G7G6XnduPqBJubYio76jDuQCVGxgGI1m_tScK99oUeF2gBcNpzemRIBzSb5LKma1cx88MBqnSi3BB2AuyxKA-1jTXAfCNBZ5LhfSCYf04CUeEYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سعیدفتاحی معاون‌ورزشی‌باشگاه استقلال: قرار شده بود امروز عصر آقای رامین رضاییان همراه‌ با مدیر برنامه‌هایش به ساختمان باشگاه مراجعه کنند تا ‌اقدامات مربوط به بازگشت او به این تیم رو انجام بدهیم اما برخلاف قولی که داده بودند عمل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/27122" target="_blank">📅 00:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27121">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c01adXPElgswivrea1atQ8Jgvpu7GfRC_3GZ8HmdY4N0TnruDSfvQflb3zYhtJFOudhpXqTAENP2iqNq6fUnXDOKGRw9z3T6wmjdslhrj57WTqslVN3tzHTdBoC5Ie27noTSWtT5zys5M1uTQa7XTLEqnEbzoML8TZ6ngUqAq7oL4PhIEOWa5_kl9IdMSyCVdkp5bQTD1E0bRdiEVkP71VlgfrmUPp7uUi9Km7NIZtniZMxjajgtmhkOUEpSQ-qzze23i6iFUkbLuRLOHzyeoJk1lwdDofAVhJJ0w_cR5OqWeOaqGs6IrmbmUAFSsk2Bcko76MJxRhYzMkGbZ0Hv8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
طبق‌اعلام‌رسانه‌های ترکیه‌ای، محمد صلاح فردا ساعت 12 ظهر به‌استانبول خواهد رسید تا کار های نهایی برای عقد قرارداد نهایی با ترابزون‌اسپور انجام شود. ازطرفی‌هم رسانه های عربستانی میگن الاتحاد میخواد بارقم بالاتری هایجک کنه صلاح رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/27121" target="_blank">📅 00:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27120">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cu57dAGB7x7AARZXE_ePRBDSbGS_PYFJhs1_P8YrBRhvC-FrZ24cWYLQjGa93MFIrluHHAS32D72Pfc8dLkDEWAgG_Ujk_pSmvBamT4yHo7o_MrYovGFpTyRb1lw6CxtaYklfJkkr9nLNrgwk-Kzlx1erjgT9BPb8w4PWbguQq88SaD_iCaqsHztHSLQRr3-6Ye_ffyv949HHS_0tp1q4iwqwwwzEv9Zmu_9EUv_zLUTkNOLfx_uJRpelwKDnA87rfSNNagFKhGa-ihtqEapI_b8baNSDU2CgRqVE6CPAlnIg4WZOOya6u--Hj54CpEc6-Rkq5vP5lSiUqUwGfNzxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال:
مسی؟ فوق‌العاده‌ست. من به نصف دستاورد هایی که او رسیده بتونم برسم بسمه. یامال برای رسیدن به نصف دستاوردهایِ لئو‌ مسی فقط به 455 گل، 205 پاس‌گل،660 تاثیر مستقیم روی گل، 22 جام، 4 توپ طلا، 3 کفش طلا، 4 پیچپیچی، 6 قهرمانی لیگ، 2 لیگ‌قهرمانان،1 لاریوس نیاز داره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/27120" target="_blank">📅 00:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27118">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8a21ccb63.mp4?token=mJvBxqyQ_QAvl-0n3F59ZYCqZAJIfeats5ES13XbvgYMGKYj9fE4zSMvfoFEw3E3WExwvSr2KaEeL76mQNOpQYJsMMM-131SpJnaeJVRvkT4flv4wRb8azxvoTYRzDfRbYow3BjCet-5lsAupaYXw2cngj23FTM019mG2sXxsbdjpeeJkNaP0lOyjBSybhIHBmtLn5RvY3dk413Tf09ataKq0BTOQNHgUvQcnU6Gz8iwXkSFdUC9v_Pyoz-m7fN-Yyjo7LswxdbBxN7_Tep9361Q-yKymIu4BtqB2B2EgRnxjwJPuz4K6Rqmjr-hxOScwgcv0jyA_zU-EF_tShQeEiuSaVd0uWL-_yXg0dx-AobQN9FbTHLX9LK5rhlwbQ0JFep5FE3DN71h9JvCxdJEWPsjtGs_5c6YlTwAdSSEFC9zF1eQKjlxNxN87NCTaqix6AptsAKJX3zLj0_Izu6UCzPW3mvSah5-tQ64VtSO3TjEEglkZ54oP87ncHHubw9x2Jkw69q_aDVuelsAKE-JXMI7BoKo16RgTsXDEB5o82d36Praz72azwIq4nwhd88bTxgjJdv_bt6qaNZrCNd_3xCNiLv_HNc1JS9jWqXteaQRy8nKLiE4HSIJqdKEduLhX3NqRzucLUaG0yC4i_56kjAcZXu-fcQN6t8QJ1flhys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8a21ccb63.mp4?token=mJvBxqyQ_QAvl-0n3F59ZYCqZAJIfeats5ES13XbvgYMGKYj9fE4zSMvfoFEw3E3WExwvSr2KaEeL76mQNOpQYJsMMM-131SpJnaeJVRvkT4flv4wRb8azxvoTYRzDfRbYow3BjCet-5lsAupaYXw2cngj23FTM019mG2sXxsbdjpeeJkNaP0lOyjBSybhIHBmtLn5RvY3dk413Tf09ataKq0BTOQNHgUvQcnU6Gz8iwXkSFdUC9v_Pyoz-m7fN-Yyjo7LswxdbBxN7_Tep9361Q-yKymIu4BtqB2B2EgRnxjwJPuz4K6Rqmjr-hxOScwgcv0jyA_zU-EF_tShQeEiuSaVd0uWL-_yXg0dx-AobQN9FbTHLX9LK5rhlwbQ0JFep5FE3DN71h9JvCxdJEWPsjtGs_5c6YlTwAdSSEFC9zF1eQKjlxNxN87NCTaqix6AptsAKJX3zLj0_Izu6UCzPW3mvSah5-tQ64VtSO3TjEEglkZ54oP87ncHHubw9x2Jkw69q_aDVuelsAKE-JXMI7BoKo16RgTsXDEB5o82d36Praz72azwIq4nwhd88bTxgjJdv_bt6qaNZrCNd_3xCNiLv_HNc1JS9jWqXteaQRy8nKLiE4HSIJqdKEduLhX3NqRzucLUaG0yC4i_56kjAcZXu-fcQN6t8QJ1flhys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
فدراسیون‌ والیبال‌ ترکیه‌ به‌ این‌ شکل از زهرا گونش و خانواده‌اش بعداز قهرمانی در لیگ ملت‌ ها تجلیل کرد. گونش با درخشش در لیگ ملت‌ها یک تنه تیم ملی ترکیه رو قهرمان رقابت‌ها کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/27118" target="_blank">📅 23:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27117">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBk-DGzMHI1C3v6qzozIqC6zcMlfw-_VcQ4vfTSr4NR-4h91M8Od_zdBmYQ2jjwZvLm2EVdTDy22siyZAPck2xtNR_ZWAm1VlFizwQBTIiM6P7Wt3C6lafJDxLfvT5hWp77WqoXmFGJKCrSrDbOo19NP3zEJ9PdkFV8EK3pVTtM5aEh3e2LUu61gdkKdM9eP6SpUCIvCdXgi_y2_5IR6Lk4myjE9iVIWoBwaWFs9gYkeWj9RvHyMw1zapOq83nl2Tx25kSoPraaAmCHWAV4uxGJdsduCWh-ZK2zlHV8m0hLexYp4EpKuomGgb2i4lkaxFKcnEPRTuL_vIUTxsE9DGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
رئیس باشگاه اتلتیکو مادرید به زبان عامیانه گفته؛ خولیان آلوارز خودشم‌بکشه نمیزاریم از اتلتیکو جدا بشه. 100 میلیون یورو که هیچی 200 میلیون یورو هم بارسا بهمون بده آلوارز رو بهشون نمیدیم. مصاحبه های آلوارز اهمیت نداره. او موندنیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/27117" target="_blank">📅 23:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27116">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAbD3C145jxhbnWFCJmbqcOQ_tdXfrF1UK4aN48q6DCP-Ot1HWpT4glmz000nrVRaNU-q-b4311BCy-NWHNfKAkuzzhE3D_rrjlXzGkRuyPNWOm7uweoYzCHh3pAg9-j3qGhJyNG4P0H0rk0H1boaphGnnVSeiSis2C7egV2ma_pjgGQeOT8b928FyCJ2WvWqcmAudbQZVs1mr4JjlEm8LgjAS9T_NfoRjbX7GJW6HSAMQuFPtowEGeaV-qCu2MtrXz_QrSA2BZ2rDLRZzmfoqDuHZ_UlF6WFWMyS27t3LhAWY2-Aoi7RCyiLazsJQzEQ4WhCfSTn_Yr5x5XgpFC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ مدیربرنامه‌ های رامین رضاییان امروز با مدیریت باشگاه استقلال مذاکرات مثبتی بر سر رقم قرارداد این بازیکن داشته و قرارشده‌ که رامین رضاییان عصر امروز برای انجام مذاکرات نهایی و عقدقراردادجدید با باشگاه استقلال وارد ساختمان این…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/27116" target="_blank">📅 22:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27115">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52510ee628.mp4?token=rr--AiL2JPfaLwGgC_AIS5yjzdB5xXh1foiUN9-RrJs8-4GFiO31YahcD8YtIkV5dKEtN9PtLmrx7Rp9jBeZaEBW8tO2H-3ZUEwnYOE0JTT2nSEGp-9b4q3jj3lop9fToSFUsBkqMyVAhlLgKVwQfUr5p8QVmt9VRvwnQw-6Ok8hmrW6iT_SRRihXfW1cuzkUuoavVxpJ243pOTE98zLtoDqFuIQ9UV2bT8d2s2z_UC3BIciOzGZcl0eYCv2XNNWF8ncgfTsusH9qZZDaZqzOdEYgINRkfQcUbydbO4yhCJBnJGIPGzfnTPUYbH-kxYNTZNSu9RumgE6ohpfMBxHiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52510ee628.mp4?token=rr--AiL2JPfaLwGgC_AIS5yjzdB5xXh1foiUN9-RrJs8-4GFiO31YahcD8YtIkV5dKEtN9PtLmrx7Rp9jBeZaEBW8tO2H-3ZUEwnYOE0JTT2nSEGp-9b4q3jj3lop9fToSFUsBkqMyVAhlLgKVwQfUr5p8QVmt9VRvwnQw-6Ok8hmrW6iT_SRRihXfW1cuzkUuoavVxpJ243pOTE98zLtoDqFuIQ9UV2bT8d2s2z_UC3BIciOzGZcl0eYCv2XNNWF8ncgfTsusH9qZZDaZqzOdEYgINRkfQcUbydbO4yhCJBnJGIPGzfnTPUYbH-kxYNTZNSu9RumgE6ohpfMBxHiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
درمصاحبه‌جدیدخانواده‌نیمار؛همسر نیمار از قلب بزرگ او گفت؛ ازکمک‌هایی‌که حتی دور از چشم همه برای اطرافیان و گاهی حتی غریبه‌ها انجام می‌دهد.
‼️
البته ستاره واقعی این مصاحبه شیرین، شیطنت‌ های بامزه دخترکوچولوی فوق ستاره سابق بارسلونا بود که تمام مدت توجه‌ها را به خودش جلب کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/27115" target="_blank">📅 22:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27114">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfkCS9H68mU_PJJtPR1dOj_zvtBqLmWrHEBgmfGKBzOrx8zItRR1UIjCV41Cdo9kd9W5ZpdUS6OFTBHGUEzQCkXovolfusvDX29tFSviGG38CfqP6z-kIABjDh-bT5pHioP94zmJswh9i371SyM_0tyg5EOWiWIyYgB5KVUPCz7onqdJnxgIRvAbkMIUWCl71pxKr_OaOFEIW5ko0J8tcPCCq37A0sWbgYWVfk09JyIOl-HJ0abi40KoA0xaFRNBPkmnc1gFaAOXa0Z7gR1Bda1f1-V1zImoo0gqqs894k3JXsOxrpPsbb_LqBmEZg3CuD5nb7SCtSmYBnzKzQXRoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌انتقالات|نشریه‌ سان: سران آرسنال به درخواست میکل آرتتا به‌دنبال جذب یان کوتو مدافع راست 23 ساله دورتموند در پنجره ژانویه هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/27114" target="_blank">📅 21:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27113">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWGgN0qtBBCTMP_re3UDCOz8IgBCMni7cgENy8NjJmaZRx2YzWfvdGL2ElgugbNdXJ7TBFE9RwtxWk4VLKaXK42-SejSVIYcPs0Y2NRH1rm799-KACoJfQoAqe9TG_6bcWBeB_Xm-MExwJh0WNv2VowYgZNdwxEyAsRm2H-OBwZkdaUkoZ5MZMHK8bWcxDTa7OBxsZ1uMhgXJv4WpeW_1CgGNLM3C4ze4P2iShQlNEHpJVfKTr8CpKD3yNwkTJ_bx7Q749Yf4Uhj4Y0mq-pyyacQ5_Jy4mlpolISTnQmhwWwQtHkDY1FUF7iHw-UWn5-dZzNPwbv9N7fj4eF0EXXQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس اسپی مهاجم رئال مادرید:
الگوی من در رئال‌مادرید کریم بنزماست. میخوام با گل‌هایی که میزنم همچون او در مادرید محبوب بشم. برای دیدار مقابل بارسلونا در الکلاسیکو لحظه شماری میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/27113" target="_blank">📅 21:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27112">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q42LjlUXyZKsYxEcyOkQ4OAsqVN1BZXGncGQNwkfjawuPGyr8C3hE_2zQQ3O5V0gI3MaND3-dPr2ir2Ag_X9v_GA9g9kabdr3qktNI44Q_O19vYezQIq9wi57U_aZSRlcD8V2gYsxpjJystLiUt575-ASyMbHnbAg43-QZSPT1nHJ4B7ywMPzdqQyzj41MWN1s3psmuwOMHoF1Bk3GQtBoEXKorHYUnJyG81cEYu3SPREVDYYiEcKTG2q6tSZPaUv9FQQHbdKKxnP1TDao92Yi_2fSVBKjmctvmWziAJ3-zNzXdBnfpng-wg8bczxYHLp7kk9CRUI6EpqBT8xIguQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ مدیربرنامه‌ های رامین رضاییان امروز با مدیریت باشگاه استقلال مذاکرات مثبتی بر سر رقم قرارداد این بازیکن داشته و قرارشده‌ که رامین رضاییان عصر امروز برای انجام مذاکرات نهایی و عقدقراردادجدید با باشگاه استقلال وارد ساختمان این…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27112" target="_blank">📅 20:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27111">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfAbLigdGpwzS_SYmd_1vgERTjy0PmcML2IPdP_qvpouPooVLwk16OtQ29vLshI7Ci-ubf5gRc0g-kxeDvG4JVIGBsCz_F3mBd630hgHDNT3u_ymPD7iGfIrLFnFiikU6Nh67mm2AqVOEuPH8UHdI-fyIluAcGBOym0KmvZ26_U-JFXe0IojGMIsnaGpk8_M4g-SOHxXPzog78uhSA8KzrenlMS-wvf0NwAaknVo6pbiiN5nzKD3VDGtuYhV05LNVyz24K9ar9PagXygk7FyNAZCMz65gMgv0s6yNwEZess_unswvs6VSqmsv23aKnji96rHmlCmGss-X2slisS73w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: باشگاه ترابزون اسپور ساعاتی قبل‌پیشنهادی دوساله به محمد صلاح ستاره مصری سابق لیورپول داده و منتظر پاسخ این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/27111" target="_blank">📅 20:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27110">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMQyx7PA-jBPQvZFi3GpzPsRZUeE2yT817Y65ilecfajIxOcqqEhZJxS7iiZfm5xshl-3HXG9boPpHW9Nl1ytXCgrZZ-_qW1pEozmfZff8nbLa9kvVuKdqmSFVqaS_J2f5MYLakmrM7l1Rar-w_JWX_xTCTg7j-u7P0jcaCmjJ2thf_Yn2R7HbA6Rk6Pmfi5BUHPHrvGXcKj-JrzVu4S1qGZs5b6GgtSZvI20O6niV0-Qj5WOawq8e3iKkJnArAB11rxuzHWvuEF4u72HSoY6m5LOztnhi49zKfZ_SB2vIMhmyi0sKTzNB09TQn1ig9nkLC5cDI97aZbbWRLmbpOMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
استوری جدید آلن هلیلوویچ هافبک تهاجمی کروات سابق تیم بارسا و مدنظر باشگاه پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/27110" target="_blank">📅 20:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27109">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/St3TS7ZhautjT2ckPJwIiaQU2fsKPAfhod6KrA4CKqgNwVkwuiCi39UBREVRgKMxJ5fHPOsGypjqvtjLOdhYODbppXu2KQUR9T-oNVSl-OlcalTKoh7lMOueDVa0nVV45IPYlTI6hkUNr2Wg4ww7IhLhXyiGR386JDtjG83CbyzTiavImulp4gPno2vn_6YTk7YvyKqa7UkerG4jEsjNinX0r9XiEF0HC5p9Eh1BmXqRLXnoZZ_oVlgY5N8NHuPs_gZasAVY6vwnSRckL_2G8697oIIlrk1Nr58VOVcN9IqZwqnu-KI355ObxgwvzzuP3Cs2kJL-pdigVjktOYgc6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
نشریه‌مارکا: انتقال رودری و یان دیومانده به باشگاه رئال مادرید نهایی شده است. بعد از رونمایی از این دو بازیکن پرز پیگیر باستونی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/27109" target="_blank">📅 20:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27108">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWWYupexukNNBV-_I7mZoohWSz0Vl7sUyAQ190tOTdnuaLgNAF-uNpGkKsT6n_24lWbWdVTKBnVEePd7YkQHtszi6ysyPQTa_ce7KkILcxzeHAKgJczeSJX8B0P4oLys4oc772Tk7n-2KN5DNZBZcj5ax25f-37_5ExI0Qct8mYLDoEC3nBukSeHw0YrxEiUUa871cyvYjgrUTQ0fjRDjW1J_VmC9s59saWFJr_y60VAfp4isUBjh5LTacKcJkJLwW0DWd0WfBsghjD7rlx8DRAl2lqCyYLtzLlA-Igo37L8iRRbfVjsJhG6DEj-gO3wT_jwmg6w5kmWNItL6kopcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
پاسخ‌نهایی باشگاه‌فولادخوزستان به پیشنهاد باشگاه‌پرسپولیس‌برای‌خریدابوالفضل رزاق‌پور مدافع چپ‌فولادی‌‌ها: 200 میلیاردتومان نقدبدهید تا ما هم رضایت نامه رزاق پور رو براتون صادر خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27108" target="_blank">📅 20:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27107">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtnEIbR83MrbJpjsDoxH6kHY5mweSj7Hv3dPEi0V85QKnYS-6ZQExnRZD3kQAYaUEfsoLihvka9UFpSLUNNQrIquhVtI7isS4kU8xK4SpZIx5db0iur16bgSB5UOKNO340dmyjZwChgkVieTeF1vDJGnqygGWL1T3Hol1N-MMkjbWK0gkEMJTrX1YocReize_-62EcAvfDfWmp5i5D4d31eFyIQXQy8fgtO8C3mIxpHa6nBeXtyoratOxNjhSRA5hJWzF1yO0n1iP6RgiDbyJla552XjG3UVk8hq5u-nyl3wOETM4tkes7lJjgs2Jqd0rN1Un6RwCZDdxOueq2Mclg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/27107" target="_blank">📅 19:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27106">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6169d08e.mp4?token=HK8pVCyOu5Kt2cvZjlFypSxXu_gJaWGums6yKfw80I_Pg9U_nwpFxOYcgkQ6zUJQd_o2ASSQolhLuaZYYiCnC7ync8G-87zauYJTik9HjiA9ZYJBeIBma06myeR3JJJ2Wlv7ewLbAd0Ft6Yiid1Lq2H9bflog1nZKaxB15C0oGIa4QPgyvCMdOeXKqFElg0fZxmNm2HHD3C9MtD7gGzAnbVeLoK0A3Fawre51yDaQ692VNJXuBeg9nuD0Y7RTK58J6AR3yn68TbB0eX05ArkXgNZSZanBEDj371Tzb0r30u5i_wG4gM85mXntAu5h141eXo8MTPf8CMkBjBbZl8GVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6169d08e.mp4?token=HK8pVCyOu5Kt2cvZjlFypSxXu_gJaWGums6yKfw80I_Pg9U_nwpFxOYcgkQ6zUJQd_o2ASSQolhLuaZYYiCnC7ync8G-87zauYJTik9HjiA9ZYJBeIBma06myeR3JJJ2Wlv7ewLbAd0Ft6Yiid1Lq2H9bflog1nZKaxB15C0oGIa4QPgyvCMdOeXKqFElg0fZxmNm2HHD3C9MtD7gGzAnbVeLoK0A3Fawre51yDaQ692VNJXuBeg9nuD0Y7RTK58J6AR3yn68TbB0eX05ArkXgNZSZanBEDj371Tzb0r30u5i_wG4gM85mXntAu5h141eXo8MTPf8CMkBjBbZl8GVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی عجیب احسان علیخانی که چند سال بعد به واقعیت‌تبدیل‌شد! حدود ۱۰ سال پیش، زمانی‌ که عادل‌فردوسی‌پور و محمدحسین‌میثاقی هنوز در کناریکدیگر در برنامه«نود»فعالیت میکردند، احسان علیخانی با لحنی شوخی گفت: «میثاقی رو آوردن که‌بشوننش جای فردوسی‌پور!»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27106" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27105">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qViPoyhAKcyGDIGj8HrUC-WKhfRq6ZFY4OJ5voLu29LRw_kv8_k6bG4ucQoLC4q6pKFReMvqwek0KWXeNPF9STGF-1rtOpQ7ET7IgEm8MTnJwj2aPqvp-0DA-PRJwkS_2cFt90Utq7BvE1aEm_5vN-e6FgwRPmI-1UXZqmvc0o7MZiVM2EnNNLA44iVR1qo2VceoHbe2XRy8NXE-P0y0lsusAR_hmqpu5Rn5u0zndELr6ScbLF6OfhQ5SHA7aLRVtzI7Bhv8AZ93n8_yzCPbp0HQkmpWoszV6msQRr9RJy9bo8YMN7APvngZ1A7YZRJAkGhSLoaIs_VgujQWqaW43g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
سانتی‌آئونا: محمد صلاح ستاره‌مصری سابق تیم لیورپول برای‌عقدقراردادی یک‌ساله به ارزش 12 میلیون‌یورو بامدیران تیم بشیکتاش به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27105" target="_blank">📅 19:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27104">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe05053c48.mp4?token=spbmxaiU1X2Ny2waH22WB-N1KTFNOa2ddzmhd5afZ_mjDkfb_7UAVB20OneEEf1lkV3e8n3z9BOXh7JxOgZmKIkBKavTbOgJ_iDwxmcjbBnnrjqQVEc49crFobwx3rYnI-rnpl-ImOpCkoMCxAwlrXgZqxqoK0IntxaqyqLYxc51UjwqPrjkjoBtBOCEDKdjGdcTxfpqZpl8-Ea7Mw1m5sDVrxmah9-vVbpweG2va8ftnOfo1HX4qYHI9NzOAtTpkFM_MW4yriX7h2LstPPCh8gkf9a2qFiLZmNXE9Ro-ge3_uMbH6_Lh_y9o4YDEuJud8pITSggOqAqfNECC4FJQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe05053c48.mp4?token=spbmxaiU1X2Ny2waH22WB-N1KTFNOa2ddzmhd5afZ_mjDkfb_7UAVB20OneEEf1lkV3e8n3z9BOXh7JxOgZmKIkBKavTbOgJ_iDwxmcjbBnnrjqQVEc49crFobwx3rYnI-rnpl-ImOpCkoMCxAwlrXgZqxqoK0IntxaqyqLYxc51UjwqPrjkjoBtBOCEDKdjGdcTxfpqZpl8-Ea7Mw1m5sDVrxmah9-vVbpweG2va8ftnOfo1HX4qYHI9NzOAtTpkFM_MW4yriX7h2LstPPCh8gkf9a2qFiLZmNXE9Ro-ge3_uMbH6_Lh_y9o4YDEuJud8pITSggOqAqfNECC4FJQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترِکپی برابر اصل نیمار جونیور!
ماوی، دختر سه‌ساله نیمار باشیطنت‌های بامزه‌اش وسط مصاحبه اجازه نداد پدرش‌راحت‌صحبت کند؛ همچنین حرکات شیرین و بازیگوشی‌های او دیشب بازتاب های زیادی در فضای مجازی داشت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27104" target="_blank">📅 17:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27103">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835360d02b.mp4?token=pJcMFkVMdxvQsv7jjRkpadJ_lm56GjR7qQIiuC1lD5Rw2AtgXTLvfqSPYRathAd54D3Lpw_y9YkH8dX1_UtHaRvy-YexkXvNHrcga6KJMDO4GVTEzL4464u4VNgeofO9raSG1dmkfP6R23DCTdMVKmFV1DHHwpucfTYjFTLMk4xZCBFlXekx_JuOKRRr9xICSEbHQKh0c3HzCUi0eQjpqUVGOGvpo8BUJiC9HZ--eQhbpw650MCuWUeAa3njvLGJXRSNEKMBsQN-ASPIR_W_xh4ME47xL6zMn7fFxZPN1XUCbK8XHNHfYxz26GTz1suFxF7t4WP8vRefPxct9EcBbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835360d02b.mp4?token=pJcMFkVMdxvQsv7jjRkpadJ_lm56GjR7qQIiuC1lD5Rw2AtgXTLvfqSPYRathAd54D3Lpw_y9YkH8dX1_UtHaRvy-YexkXvNHrcga6KJMDO4GVTEzL4464u4VNgeofO9raSG1dmkfP6R23DCTdMVKmFV1DHHwpucfTYjFTLMk4xZCBFlXekx_JuOKRRr9xICSEbHQKh0c3HzCUi0eQjpqUVGOGvpo8BUJiC9HZ--eQhbpw650MCuWUeAa3njvLGJXRSNEKMBsQN-ASPIR_W_xh4ME47xL6zMn7fFxZPN1XUCbK8XHNHfYxz26GTz1suFxF7t4WP8vRefPxct9EcBbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنظرم‌جذابتر از گزارشگران ماگزارش کرد در حد همین چندثانیه؛ گزارش فوق‌العاده گزارشگر زن لیگ MLS روی‌اولین‌گل‌لواندوفسکی برای شیکاگو فایر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27103" target="_blank">📅 16:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27102">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ub71iKPswRgLY_pqQAnpWF1mflkhQfAMMTwaxcRGo2Ng5c5OUfApefUoJ8Kj5ymojBSskX9ufMRSGhTNRs4zM2XGCCoaIxiuS26aC1BgDYt7d4SSMLHcNMT72J_sye3JPROBZ9_8gU_5MpPoiL-5gHu5foc_WDiE56gaBw_6xNDpHZobpluluHvCLHtMFuYIKG_Kg1zdMXMNTfWarTxP-h9dH8bjl-ePOVU3zv6Hzrml_nunFTbTLcjNBs1ZQwnT_aXUVzyAhGSpDh0gn9TcVkDw_SKlPZoiRada1EkVwLKkDdXaiSTpOeKNktQgr7XA3VJplk79uvllVWnKCI2AbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
رتبه‌بندی با سابقه‌ترین سرمربیان حاضر در لیگ برتر انگلیس براساس‌تعدادروزهای‌حضور مداوم روی نیمکت باشگاه فعلی‌؛ میکل آرتتا با بیش از ۲۴۰۰ روز هدایت آرسنال، با فاصله‌ای چشمگیر در صدر جدول تکیه زده است. اونا امری در رتبه دوم قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27102" target="_blank">📅 16:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27101">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f136b3eb.mp4?token=tJMs9_a1C74XTqOA17GB10lRolWV-6sQaXzb6dgPSxnwzxHeLn7dtwToeE1zza4SC9_QRGRWkdu7hPcl5tvv3gKm2pt6rhKB6O90_WkYRo7JBedVvKY9n8fBFW1MmobDvj1VWjSoMAoHKR10x5DG5aCrmoJob24pbgHWPicweh8xPhiF8mldaTCLNq9_M6QazZJyBItI_7xINyK2HI3sIJYUzzJsvBvPmy_4aS2Brhj07VDByQamFC3ocJl1pOP_cFrMVzLj3JBba2rh3mXJEFPxYI7v6AVaD7x-07wygC371F6BKv4IDODWwxCaJH9Zj6uUYbGVYcEd-MtVMmDR-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f136b3eb.mp4?token=tJMs9_a1C74XTqOA17GB10lRolWV-6sQaXzb6dgPSxnwzxHeLn7dtwToeE1zza4SC9_QRGRWkdu7hPcl5tvv3gKm2pt6rhKB6O90_WkYRo7JBedVvKY9n8fBFW1MmobDvj1VWjSoMAoHKR10x5DG5aCrmoJob24pbgHWPicweh8xPhiF8mldaTCLNq9_M6QazZJyBItI_7xINyK2HI3sIJYUzzJsvBvPmy_4aS2Brhj07VDByQamFC3ocJl1pOP_cFrMVzLj3JBba2rh3mXJEFPxYI7v6AVaD7x-07wygC371F6BKv4IDODWwxCaJH9Zj6uUYbGVYcEd-MtVMmDR-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو تو چند روز اخیر بیشتر از 12میلیون ویو خورده؛ رونالدو بفهمه تو ایران دارن باهاش چه تبلیغ‌هایی میسازن میاد از همه‌مون شکایت میکنه. طبق گفته رسانه های معتبر، کریستیانو رونالدو و جورجینا قراره بزودی بالاخره باهم ازدواج کنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27101" target="_blank">📅 15:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27100">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ntd67xHqISAR5W5dG0dF_bUYZBjbSpxtrsw6x2qduNwK2hgzj0Tqv4M7euBEHTRXQaV-rG6a99RjIHAQylbiani7fIGSqHgXI8ppN_EoaX4xmIrq_fluY9Sz-MH7B7_IewnkUP2FHIkB7URKePcMkkTiY54yvSOu8ZaKNlAID5kR0Vcsf_YPfWL-_-p85N46yjDW5NpdqMqCu-HFZyVc7t7w8XflhItvEe_XKUgobp6P5HewTvtZ7PyHZBR_OGk25ZmX7UjcUO7xXWa8qTY9Go4HoMMofecTWpGuzoPcReVwNiGCXzaFAL875fHALPY4KNCvoFiRMR2sgZ00Qgkmdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنایی که بهترین بودن ولی از تیم ملی شانس نداشتن و از داشتن یه تیم ملی خوب محروم بودن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27100" target="_blank">📅 15:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27099">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">قیمت محصولات ایران خودرو و سایپا 13مرداد
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27099" target="_blank">📅 15:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27098">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTDN_x3QE3uP_JvF5TFkLLB_EDGieavdvxyAiiUNzkwZRYWXRHGjRpPOXXt_qLs8_IQ3zgky-brhVtANdzf-b8L7pPcB1oZGHxto3-QpDTlmIw5pSHrP69e7mVasqT1zi_ohujOJKubVXNvvNxvEgLgsYnb_MIzA8HEwxMZ-_prg4Ma2xxJR2Yhhn8-MEvXaISn1ljunE8Plg7RHv1rsLkzg6fK7ylENKqcLIyXx_HPAVzEq9pQcamPPv0suS1Qiwy53mjCkZbO_eNxPdxBOL6TMXcEH5v_W9rSYtfAt6trkCcNwI0Vtn8J4Ulyum160n7RhzKHS2JkpauHF5iwMuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کاپیتان‌ های پرسپولیس در فصل جدید:
حسین کنعانی زادگان، علی علیپور و اوستون اورونوف.
🔵
کاپیتان‌های‌استقلال‌درفصل‌جدید:
روزبه چشمی، صالح حردانی و امیر محمد رزاقی نیا. البته درصورت تمدید قرارداد رسمی رامین رضاییان با آبی‌ها، رامین کاپیتان دوم آبی‌پوشان در فصل جدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27098" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27097">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3q5es5ZJXPzY9caEIVD3wd1NdShJci-46wmrakSzImGF2hLeVYNM7CuohQdGg8ZRr013ukL6yDFJvkFgrQOVoLRz6wp-ba5lGo5xpbIjJ6FeukO7GOCLw5sQcCYwiyxby2SY-y8biayJMUypirmSbzWUdFGoFhPvxbCvz80fsKa2icAh9wgQSDz5yARiefEXL_p2OEq2o6dHP6x3Ebrx5CxMCLO4nev4HIxI4q_ypw5OpGPpkPJJdqT9S3TAO0mnzC79yWxn7N--17Y_rZYc12V2wQSjhXMat_Fzn5iPYxQM7OlJw_OkJXfEVYFk5ecEuoeeHXwzl2U9-nwetPBYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
عبدالله‌ویسی سرمربی‌ذوب‌آهن: دوست دارم کاری که‌سال 95 بااستقلال خوزستان کردم رو با ذوب‌آهن تکرارکنم. بسیارسخته‌امانشدنی نیست. امید عالیشاه مذاکراتی‌بامدیریت‌باشگاه‌داشت اما درجریان مذاکرات نیستم. امیدوارم که قرار داد منعقد بشه و این بازیکن با تجربه رو…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27097" target="_blank">📅 15:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27096">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/retUssdp_gfhy1ihfY55xqHPDRHRLzKuragYTz6un0tFHl38XQYOQq30ZqpDPzrqw19b79sv67Q9VgUn92AopM_3qfoRAzJDgMgGzeRUxtfk7bqhUPwVLHWmPMOqyZxmQFnGBNVHV27DdjbOCZwVyJ9F4FJUTyvL9rth2xNl2tk_cZ_mXxyP85fCPHPPlcvds4zX796obyFqZPaeosf8U5DPJGw-62eKV5thTGHRLb-XRmdD8RSGluQE3inAbi4BJ_oNHqIM-l2rEslYLyQfU5xHJ3a76GfaoAGLjKApcX4CuB8mOzqjujyJoU05wovyWRaFqkz_3MJ5h1ZKkbzIkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛مدیرعامل‌ تیم پرسپولیس امروز به حمیدرضا گرشاسبی مدیرعامل فولاد خوزستان اعلام کرده حاضر است برای خرید ابوالفضل رزاق پور 120 میلیاردتومان‌پرداخت کند. گرشاسبی به حدادی اعلام کرده تلاش خواهدکردکه مطهری رو راضی کنه تا این انتفال انجام بشه. مدیریت پرسپولیس…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27096" target="_blank">📅 14:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27095">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d39tCvmdr27z7WLjfXiQOkJGi8rrSlvAu-JmpU_in267MKkDSvnH9stfeOJN3g0ekJJrA5FSBzoOnZuP88U8Z5VG70IkUIvA-MCVxa0R7PTW630ta57ldh1g1mJRS7NkCyamAQP5VddPerTDPq375TVhZA94-cbYso1DqGQMRm2NVV8V8XPoLM5K-oJWWE8YpM4uT4eu_DGSgzNQdt72QIDVDIXr32nmTSGx-YudUDAWvhTakMko9tRnCx5enbmwcsBOXwpxJc8kIMME_AGckdsgKq5OVJJcs3scUiMjQyuZte4Nkecr69vWV68WrYvzMTlTwjYjB0hH3shCqzEnPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌_پرشیانا؛ آفر جدید استقلال به رامین رضاییان برای یک فصل حضور در این‌تیم 150 میلیاردتومان + 50 میلیاردتومان آپشن گل و پاس گل و قهرمانیه. رضاییان قراره ظرف 48 ساعت آینده پاسخ نهایی خود را به این آفر بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27095" target="_blank">📅 14:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27094">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYTRdXCs3BXfRJb1LPdWxP0KEliF41D-w_dOG95CjOIIymS-NgEpoOesPNa7PgN5PZaZgQ92pPv_VVRb5X_BXI7BK-KjPVQQsoFkkBFCHh-MJmS1GxUcdcQ6vPmr0-i5BvwAbCg1Aivn9sFVOJ83sf_nj2nLrQ6vrFI0v1IxD_oRqzKeSOC9Qr9c84PB4V5HF99wiPlJxYcG7QI3ewYJcUM7rRpHztU1CJN4HjAVyk46-xflrmxDVDFUxuHiFHEGY7bKYjsBiWZC5tnQ-LnIZ39jcEg4-0azeBZw3rMreWWA0uk1iVu3qpiMsfXXOJddrZwsBdgm_fK6yaXuLRVvWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
عملکرد نیمار جونیور فوق ستاره سابق بارسا و PSG در کل دوران حرفه ایش در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27094" target="_blank">📅 13:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27093">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJvdcyCSPugtiPgFv6dr4N-G3hcs7QcHiyeoYlY5edVAcfvCI41c-G5jDLnaemM7fMJVHZ5iBBYl3iZV643wZ0i2O-4Epa3Vmb1d6HB69S5_l99O0810ZuyvSU2MXuI3DSC97dDFLL8oKxZp8mGgu9BED8iO-y3ZznuDau8sSypIdTdq-fRAclbzf1WNV55uueEwiJZmLnllJwPAXtGdO2enwwo0CYfm1ER6p3iF-pnrI26UGN_8JfeaTM0E94KrSPSjVQLR92eLPiVr2tnNKQ0YW2jYv1TnCbTEN-m8b9FgjXcHKV0wcDA-nwsH7SLrAPNc-oi6XAL3VAAwZYvA8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روز گذشته شایعاتی بود که فصل جدید رقابت های لیگ‌برتر یه‌هفته‌تعویق میخوره که سازمان لیگ تکذیب کرد. لیگ برتر 10 روز دیگه شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/27093" target="_blank">📅 13:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27092">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fgc-Z9q_aOBXjeeBHJzmOKKhsLkP0WEB1VeDH7C_pWmOXZQwfjm-r9BPAcq6so5MrW7Aycbu_9pGvcNs82CfNFacUEIm2f9pQkopzTYydY_h7vFev9gyRdhyPtk070JCgdhX1z57vwvuMVluTE3tRno_mpKlkQX8ctn6PUYH2tja1zxgDj3ahbQy3EUsQ2ZYkoIR5nxCY3V85DyggXzJXAGIPofxTEzIgskfSUAsJwYjvyAMIolR4-GwmSV8LuYsM2WQwNePsPgxu_4LZPaDTtpwXOyvswB1GUthSKVmjbCMtchUDh7lkSh8Y05VaWmPBwoEdm5sOHZM98DuVFRBNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
استوری محمد جواد حسین نژاد ستاره ایرانی ماخاچ‌قلعه: پروردگارا بخواه برای من که مسیرهایی نروم که باقلبی‌زخمی‌بازگردم. کمکم کن جایی برم که دوست دارم اونجا باشم تا همیشه شکر گزارت باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/27092" target="_blank">📅 13:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27091">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9be54cc9.mp4?token=XrplykliL1HXjaLDUnCNlpIH_D2Eg5VZRMX-hiPakKmu9NEjLcTkGLR0EVfK7RCICswB-lPRP8iKYjhUj6Hk6CRDiTVqwvb0gdIFBb972eJFwTXhIBnlglXfke-krCpnmoqkqJ44J1zKMKj3_36i3CdbyRwVlD_iyMocOogtVMr4st2mgDclCNuWlg7cuCDeSLF35pG-557bc2atZE3rBbvh7iosZZEdYNVSAfp_oQD7V3S52mscKD_rOU75HikAobTcs6_vKHq-3hw4cCyE07kz4JphklFWrhcA69Zvh0RRtmjwzMK0AnGWTLwdA_Ji8mjzuG9t4HtlFTWQPInBwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9be54cc9.mp4?token=XrplykliL1HXjaLDUnCNlpIH_D2Eg5VZRMX-hiPakKmu9NEjLcTkGLR0EVfK7RCICswB-lPRP8iKYjhUj6Hk6CRDiTVqwvb0gdIFBb972eJFwTXhIBnlglXfke-krCpnmoqkqJ44J1zKMKj3_36i3CdbyRwVlD_iyMocOogtVMr4st2mgDclCNuWlg7cuCDeSLF35pG-557bc2atZE3rBbvh7iosZZEdYNVSAfp_oQD7V3S52mscKD_rOU75HikAobTcs6_vKHq-3hw4cCyE07kz4JphklFWrhcA69Zvh0RRtmjwzMK0AnGWTLwdA_Ji8mjzuG9t4HtlFTWQPInBwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌جالب‌ببینید از نحو پنالتی زدن برخی از فوق ستاره های فوتبال دنیا و واکنش دروازه‌بانان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/27091" target="_blank">📅 12:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27090">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17e27275fb.mp4?token=cbIq-mxaHRHcedyn8yCBQHo5uwW5YnQdgnOyuqEvDMQ2J5p366t0ExVi-Sx2Gi7qrcmOULpiR83eMVwBAvDPJJ9Fm9vJJWX7YE_ZJEEJkwRR6qAK13iVi_-v4k1cFSivHX63WpEXdyqSZUrOprUpU3o2NkLRRiq-E4L9KmNKbVmohXxz-kttWufLhtVrbGQmmrC5vcJ0Y8Qwk0F7n4wfl74HFE4SXl-5YOvjeH2izDA1Az1b5xho8KaWBreefM0GKOGA6-wekPfYSftRf_fUeKaetlHxUoJmb-8sekl7_Vq1rE1mbBZnkm37i3aWl1bhHqDyS3r9TMKrAMmzGK9zFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17e27275fb.mp4?token=cbIq-mxaHRHcedyn8yCBQHo5uwW5YnQdgnOyuqEvDMQ2J5p366t0ExVi-Sx2Gi7qrcmOULpiR83eMVwBAvDPJJ9Fm9vJJWX7YE_ZJEEJkwRR6qAK13iVi_-v4k1cFSivHX63WpEXdyqSZUrOprUpU3o2NkLRRiq-E4L9KmNKbVmohXxz-kttWufLhtVrbGQmmrC5vcJ0Y8Qwk0F7n4wfl74HFE4SXl-5YOvjeH2izDA1Az1b5xho8KaWBreefM0GKOGA6-wekPfYSftRf_fUeKaetlHxUoJmb-8sekl7_Vq1rE1mbBZnkm37i3aWl1bhHqDyS3r9TMKrAMmzGK9zFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام رسانه‌های افریقایی؛ پیتسو موسیمانه در آستانه عقدقراردادی چهارساله با تیم ملی آفریقاست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27090" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27089">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370ff98a06.mp4?token=CwGjIp9Imw5JEBWb2nViqiJkAzYOz6AFOWMAcLIrbsQwKIze5UFGhtymwKipVDtCrHV3cxsRRz0Agj3077gFmzqzjfHLzQCfjwnb3Izxtzt_bSH2uOH2UHC5RAeTY9LAhkRyZ2gKPjsvyoEnRb3JgbbyiMjwauUhn4YVguezaCGut6Xx8mQHAJ_i8KHWl-ppwDuxw7YCUDdJl4AO9dois9dwRNZlShkhySSswjONR6i1CTIoc8eeHms5IZcb85dvaJZc24aZr5otfyjU4lH3ElARJi__OcKFvIK16GfA2RAdBVGb_j3nSzO9VxrVTuva-f4vVJ0OuMv1OPMW7DeI-ndWL0x6t5fuhsDOdgVWHuv1SPu4wKVe3yKiVgl1JFuhHjSNdiLD5AJiDYekRZqA7QaIf5Y6Mk1y3dQjI_zo90IQ7BCKkL8RA1ZU43iwLiHuOkX6MNBq6G6gXhDnXcHxg3oPPFgBbx1rzoKkuWiU040EJZk-l_j6zSMfbaAIdRyaIfHAqhW6jt3pejFBagLluDJTH3yersQ7ewlR2z9W8DI91B8wMmgeSd_PlgGPekhEW4vbs47vG1FG1z1YjI0BYr2Gn5tspJume8cOJIzWyUdlHrReYfRzEp-p-jZuovxXELxPRywl46z7feqPvBzzkq7pLSMYdvNkmjVlSRvPN1s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370ff98a06.mp4?token=CwGjIp9Imw5JEBWb2nViqiJkAzYOz6AFOWMAcLIrbsQwKIze5UFGhtymwKipVDtCrHV3cxsRRz0Agj3077gFmzqzjfHLzQCfjwnb3Izxtzt_bSH2uOH2UHC5RAeTY9LAhkRyZ2gKPjsvyoEnRb3JgbbyiMjwauUhn4YVguezaCGut6Xx8mQHAJ_i8KHWl-ppwDuxw7YCUDdJl4AO9dois9dwRNZlShkhySSswjONR6i1CTIoc8eeHms5IZcb85dvaJZc24aZr5otfyjU4lH3ElARJi__OcKFvIK16GfA2RAdBVGb_j3nSzO9VxrVTuva-f4vVJ0OuMv1OPMW7DeI-ndWL0x6t5fuhsDOdgVWHuv1SPu4wKVe3yKiVgl1JFuhHjSNdiLD5AJiDYekRZqA7QaIf5Y6Mk1y3dQjI_zo90IQ7BCKkL8RA1ZU43iwLiHuOkX6MNBq6G6gXhDnXcHxg3oPPFgBbx1rzoKkuWiU040EJZk-l_j6zSMfbaAIdRyaIfHAqhW6jt3pejFBagLluDJTH3yersQ7ewlR2z9W8DI91B8wMmgeSd_PlgGPekhEW4vbs47vG1FG1z1YjI0BYr2Gn5tspJume8cOJIzWyUdlHrReYfRzEp-p-jZuovxXELxPRywl46z7feqPvBzzkq7pLSMYdvNkmjVlSRvPN1s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ رافائل لیائو ستاره‌پرتغالی سابق آث میلان در آستانه عقدقرارداد چهار با باشگاه منچستر یونایتد قرار داره و توافقات درحال نهایی شدنست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27089" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27088">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKA5Nx577lVIQpa1BqEE68BCWiSYC6cbIs6lUA0Y4jM05x2hDAr3VIHpvFFY5W-AXc2CBi3l-bsCYrPKA04F8uc_8zkxwRtwfjszX4p3fYnQl67aslEmyUet1_R0zl0C_GMbB6CfugYkEcK0-UXP3WDLaTn64QVA74OtusYwp5ez0OrJ0mDIY325GCzQXl6aYnsRUt9NNCaawVo0_3h59Kb9i7iZ2s7-c68TGPwFjNym7eRHmhonMk5dUPx6gPHKwhVYUT5WyWo2fsaEfxAARY4OEUq5dfPkx2zqhrLRxyziuIXM2qZeqqAIg7wbu8gOcTpkoAJZZJnnTHCwgGisUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه همیشگی شما
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27088" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27087">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFGPBChoz1tQC4CJ5fGzY0Ax0FnCLMU9zr2OAZA1rM6vjNzc3H1YZvhlrw_ncEFANfnoEYL5R_yuvFak66ekPrU30GkAZqh5XtL8z58-8s63k50-R6JSNZzZeZF5WJp1CDWve55BV6pln5daMO3-C5VtvdJX32jo5fhCaQkB2NAKXBUwYIenhHCfydsNOXJjAFcztZnL1mGzEB-nknqLrrGf-VIOW8ViSySSQJ2SESmfrDGfrT2A8PSaAAWhDNrDZXDhinRp65dFbD7ZJ3gOscIMp8FfMsJeymOa0300cyXUOQvZsCpmuqOdO8Oe-ab1xPYSlY1Hc9rXk8K6xdR70w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینکه‌گفته‌میشه؛ باشگاه ماخاچ‌قلعه رقم رضایت نامه محمدجواد حسین‌نژاد رو 4 میلیون دلار تعیین کرده کذب محضه. بار ها این باشگاه به مدیر برنامه این ستاره اعلام کرده هر تیم ایرانی دو میلیون دلار پرداخت کند و خودِ حسین نژاد هم راضی باشد این انتقال انجام خواهد…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27087" target="_blank">📅 12:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27086">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7kInltQnZitUpPE3rBlOE0CHQQ2mL-DguptyD7ePWVRXIj2TN6fUc8wZZpIDHJaHcuTggICeAcCq5WswGHXghokJpfr4yEBm-mb43osMRTeGpMDicj1G55W_zJpr_vm4xS2Jemx---8ENobTJhh2saxCOd8yPGYUey0f3qd_ByYKD0AVypujkjmUhVdXcPbUteqTLtEoEla3rQy3iZWd403XzB6zFWDw1hWkPDo5G_EcodHyEfhlVvHfc-IcrDid8TnAR1zKLPKhybno0X3M5H21vzjBaaTO6k5Gx6m7hz8iAOLANtfRW7cb4SwApyh7H7l6WvkPTD_YtDtAZqQmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رودری ستاره اسپانیایی 30 ساله باشگاه منچسترسیتی:من‌تمام‌پیشنهاداتم‌از تیم‌های بارسلونا، پاریسن‌ژرمن و منچسترسیتی ردکرده‌ام و تنها هدفم دراین‌تابستون پیوستن به باشگاه رئال‌مادرید است و مطمئن هستم که این انتقال‌بزودی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27086" target="_blank">📅 11:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27085">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vz_h5oWkQoJei4d8EFySMhfiRRYiNhFfbtwVoKCLOFu1cETFLQlWynW1MX5SFL1RuoPqNHx4nN5UTrV3tsR2Yd-Lt0VHNjRhu-59LFdQmty8FizZPsVT3ruGDCyAFFxLTmk_dRMGUP1sSLr90fpHxgWB5jRZy5yL8v1AvA2lHd0YSlEuxJbYGi_JbMSvjj_UdU1YuJHLp3cbWVZW7xS9t3J2MH0yH8i3fYu6s-Ga3TKMCcHM9FQp9zOWmhnqHv_TDdaOGo4VXQ09ot_NeUWBBQi8BBi9zgvcwBxDIVWtKaW_Jb0VWGVneip5r5mxlB9RSabgT2L4fhBncnLEhCtxvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیویی یک دقیقه‌ای از سوپرسیوهای تماشایی مارک آندره‌ ترشتگن در دوران حضورش در بارسلونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27085" target="_blank">📅 11:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27084">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjerXJSK2j6_mZJaTJICVMs4NWIWT2WeuHl2aP5Uy4oJ22Kq-0Xr555cjbKhZ7S1ejl01WvpOCAWefFxNwTS4JuP3cv0u-I39i8g8mhZwGrw4REC5cu-SkWzmBZHu3rRE6Bi7FFwHzCyBPCJ9GxndZyr6jG5Wuk-ZQU6uhezjpcuxz9TRKhxNuNT6y5ZlOy0FV1HMSUai7eWss6vNPtKpEJaOZJzUQNXBvUKP5zj0AQ4l5aaY-YBHtSkLjw5rluN6cjQH43ToWTZp5kSJ_gUGUOvtevQBXy1mg5v4uz0fFqUMvUTBZVWIAuzxYfiWVoGgmMeQf0wDjb_ryJ5KdURNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27084" target="_blank">📅 10:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27083">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=fnuhmhj_aiPpibHors_6D4Aj7oIZIHaLuzVA4HvqqvXDYG2SbA4ib_Oeptwspu68NYT2sK73-GOzMkkNlzawajvgE6-dpMENRB0W8Dq5cnGfQjYUZBDDM-q0QoHxhEO8BknXE0DNBWvrHfqiUU4DXO84BpJ1vkTBT7KQh43V23j2uONiPCFD6irKqTQ1SLWVOZprTEbK6bRyL6vdbwbgju_nQ2mPd9Ke1euWjruLNVFD4XdTffHrwxdav1BsgNAc0bcu5mro-gvwsY6X602g8W9fuXkbhwO6nrQem1_lHEZrjl1bF5jY87tBSAODsnTXBG1VdZQRZ8aOxxh2CMPf8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=fnuhmhj_aiPpibHors_6D4Aj7oIZIHaLuzVA4HvqqvXDYG2SbA4ib_Oeptwspu68NYT2sK73-GOzMkkNlzawajvgE6-dpMENRB0W8Dq5cnGfQjYUZBDDM-q0QoHxhEO8BknXE0DNBWvrHfqiUU4DXO84BpJ1vkTBT7KQh43V23j2uONiPCFD6irKqTQ1SLWVOZprTEbK6bRyL6vdbwbgju_nQ2mPd9Ke1euWjruLNVFD4XdTffHrwxdav1BsgNAc0bcu5mro-gvwsY6X602g8W9fuXkbhwO6nrQem1_lHEZrjl1bF5jY87tBSAODsnTXBG1VdZQRZ8aOxxh2CMPf8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هونگ‌میونگ‌بو سرمربی‌کره‌جنوبی درجام جهانی ۲۰۲۶ مجبور شد دربرابرمجلس ملی کره حاضر شود! او توسط نمایندگان مجلس کره جنوبی درباره تک‌تک تصمیمات تاکتیکی‌ اش بازخواست شد. از تعویض‌‌ها و دعوت بازیکنان گرفته تا ترکیب اصلی تیم و سایر تصمیمات فنی اش، همه‌چیز زیر ذره‌بین پارلمان قرار گرفت. هونگ در ابتدای جلسه هم از تمام مردم کره عذرخواهی کرد و مسئولیت نتایج را برعهده گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27083" target="_blank">📅 10:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27082">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCRmZe_LKHdUMGPvHHGqUzauQukFYdY49Nkv043SzQg4LWtQnAHi7pHG_2wN-0ubHLAX5hAImZTOO1-yd0_yUxJNU-FdHQMzbHpEkG6Ha4YvtFmLDl7s2W5UMy4_ATB97nFZznpymnshPUljEymbFDXOgkFXoppaxJkUScqGysItSFSyDWPW8USI-Su6Td9IT-KfovvpMVKTPu4KvHYo3h9iUNXQcQLVYhzLuYgWDW-FnVRixrpaEfFIQVBOJTveMKIuZ11xJqB1brAMhsHEnowrPfT-QkScdJqnBJigMiBI2Bedp3Uej8z_Rc3TpUUilTbGUhaJZbu4k0dY9ekIZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
نشریه‌مارکا: انتقال رودری و یان دیومانده به باشگاه رئال مادرید نهایی شده است. بعد از رونمایی از این دو بازیکن پرز پیگیر باستونی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/27082" target="_blank">📅 10:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27080">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0hub9yQ0YJ1yJvtR6-Z9KiAza10A6iNcbxDW0XcADwNbgwe3YAb5eZncnI1ZPiSDWP8w-hUtjY6AZ_I4uyNAYqcGg5QwHjVxeBVCdYNbqkqO9npGnl_O3OlVW3ZpoL8iuYkEwWFk2VzGO7XmaqQ9cyZYnALSsR9cxo-GM5HCXwY2MCyJtdzH30ilNhnA9yWtHGATT-rUddcdrvf5P6FkxDTmhgFYNArePav7PUaRSRpWY1S9i4KhI5TAL3V5E1rxYX2NGw4-GqSENnAk-U0G2TZWZW250sP9t8C0wJlTJsZgv1WvbmHmbsSCEiTy1uiKpx2Wa3tCBT-iH3EQJmXXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جایگاه‌جهانی تیم‌های ایرانی در رتبه بندی قدرت اپتا؛ تراکتور تبریز درصدرتیم‌های ایرانی قرار گرفت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/27080" target="_blank">📅 10:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27079">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXpgzN3Y3cG06A4c0q8AR0REf301MDFh1YJeymoMv9dqTgin7wtA4g542-Vqlzx5v2r2JkxVlzYC5KnbH8VVT6wnrFQxgsC6u63fj4DD6XBppj30OFdNcofdAJbCCJEu6TLxiZI81M-S2AmVasbw-jJW5gIk_vmZzYqJfkyki76OlhyiDxj79zptKqGqbW7tuAjUuQxucQQtnjcHlqWHQ4KdgAhwAfhFvHvlfz7KLroxpaOq7tjU2_UHvXEfkTnzV0MHqa07KGUzrUWmUv27B1EVGcwqpt5s9SuXyVTPuer63_kbWxPqJX5_sLeVIH3hH1R-JC3mxZPOHDUYG_rd_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق اخبار دریافتی رسانه پرشیانا؛
سعید واسعی هافبک تهاجمی‌سابق تراکتور و مس برای عقد قراردادی دو ساله با سپاهان با مدیریت این باشگاه به توافق رسیده‌است و بزودی باحضور در دفتر مدیریت قراردادش رو امضا خواهدکرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/27079" target="_blank">📅 01:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27077">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLjgwdgTc6hqhBdTjGFqaNREo0k5uwLcw430sO2yoob3z-dz6A_qh8175IiorAqCS0ZLFJSGZvP7NQefYsi4BQpWYZ4-LT5Xi2j4UhR_-oBj-SSsocnQhbZPDMcN14lQSYutjx6wlKr_A0P0_8PrxACLk5RmT88MBiBI2ZtRBDYyPWCjLKThL5Yy6UACoDQ20LnSrjgLgs3U0iz7UdVZd6CCaIoYLmgdlyYhdlhvOYMDllKDKeDdX88nX6N9GjYmwJnJfe05sMcpLyuG9NAw6Lnse08BL9DUjo93l52dP-MV11Kuiu7es-tkx_hxvkrBKYrRR5TIzuLwyapBoHPUHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌ امروز؛
مصاف تدارکاتی و راحت باواریایی‌ها با تیم میانه‌جدولی کی‌لیگ کره‌جنوبی
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/27077" target="_blank">📅 00:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27076">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCgeNq7NqK30MGcm0Y3LeXkY9YNDa5NQrEsL-ipsKO5N_XoUJSgHwBXa8oqPc15uSyM--8rK1YbbW6GJQihdTqOcA2nnDeexEVmF1DtfkuvmrTyb0ImCyAsIu_DYaiBS1GnGb1We3MgR5KIHelrUEadeBXLGopGYB6E835U4kI7R9FzR7sNUQmHCNqD5_tovSq553ezvGo6ssupD6efBpIVq1HHSlMjzjVTiEc-MNb1X5yUWJky_sPn685V4MSp7ivdoZ0fEFh9_2o1fXzwnqDZzfBD5NVUz6vhuZZdH4SQ9OISlBj6rke5bvA5q0yRafmfA0kSfDJUEoF-4a8kV_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
روایتی‌جالب‌از آیمن حسین ستاره تیم ملی عراق و زننده دومین گل تاریخ عراق درجام جهانی: در سن 12 سالگی یتیم شد و پدرش رو از دست داد. بعدش داعشی‌ها داداش دو دزدیدن و هنوز هم پیدا نشده. بعد بخاطر جنگ آواره شد و یه‌مدت هم بخاطر اینکه مخارج خانوادشو قید فوتبال…</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/27076" target="_blank">📅 00:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27075">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mREO0kSN2ovoaxJqC4YZvoj_nJvLgGfKs6V_TrrVLXjOlaUMKh0rDhqfEwGU2C6gh6wQy00n7HpX7p05WYlDb6zpHEC5OXpksa6etXpYkATd68uVwhdMtMdPWxHBchWleIWB8CZ-OLhLNfeXAo1sC1QKU4YroB7lOmPbczZ6Jk9YvpruH3cNQsKBLeR6aHX5jlWctPIhwUsaa93BYjN2XsBvqEit94d3LlrjmUVMpYQrUvd1sBIqLV9_iXod8n5-6yAC5JfxDs2Zk6ktK4m77-Is432oPh_qQA4kR1R2xyk8yNWLQsvaAPzhwtSPQTDS_vtqYLtpzt1NYJ3pc-jQGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
محمد قربانی میگه‌الگوی من از بچگی تا حالا کریم باقری بوده. حسین‌نژادمیگه‌من از بچگی طرفدار مجتبی جباری و فرهادمجیدی بودم. خودشون با زبان خودشون دارند میگن که دقیقا فن کدوم تیم بودیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/27075" target="_blank">📅 00:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27074">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYBZTI2I1O79JM6pR2yAarFz_gk7YSlBaFA5ke15mOmNck8uvSVVE7H7p_ozwfIRIQQI1Wbh83BJWsZZ4nHBGYpxBxv81my-37DuZn7nc1pi1i3J290U4GZdvZQtWs0akiLa0XOiaTeogoTkYY5RXd51IK9eCoHZUi3wJCDcuKLh79oEj7naazx7MEry2IkQcpqUcfgYcCCSbFW1USgDBT-58Nnuec60davlctHs-ath0chyxGTR9Zucm7EbXsCv6u8VKP_Qqtzc5xsAvFO9wh8ELOLjkvki_IeUqCWu7yHwp3PkKYcvaqXPi3z8u3_mBUtA9rRkAmUYdeatsC2DZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/27074" target="_blank">📅 23:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27073">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8BF_W24KbIi26CLAswoww03XtqNl5Z6ajsHy0ePBD9i-WnGB8xKmONYeoFwHraMWxrPZdhxQfSwspUS83nEQSiPzXyowZ-9LQtd9sNlG88a8pJt7meuz1oH-UMW47L1OuwYWXChxI1DneDf-Vv-GbiOcoRqZizO-nFPHGPYTLe5QrUsEdJBr74BgPkT_xBwIDt9X-pYrE91q1Z2C7bFZCMxBnjd6wkhiL5iz5Pks-UTNcSxalS5Un3UHFmZRUYyAqpfRGV67IN0I5QJut0NzVGMj9XAy1_Q8-FIUsSfZN3ytAsQLFxHGM_5xKGbuDQV1Hdfiq06u65qgvgYkRKvOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دادگاه‌عالی‌ورزش "CAS" روز سه‌شنبه پیش رورای نهایی‌خود را درخصوص‌پنجره نقل و انتقالاتی باشگاه استقلال خواهد داد. اگر رای مثبت باشد فیفا پنجره رو بازمیکنه. اگرهم رای منفی باشد این پنجره نیزبسته خواهد ماند و با شروع نقل و انتقالات نیم فصل پنجره آبی‌ها توسط…</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/27073" target="_blank">📅 23:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27072">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szZoBX0M02-UboudNUPwXCoeWcQPiAwZGXPnActfrd026Z2G54lS2qGDL7-BRqr0IOv0Mx9q4jJasApIbY54cLBvRqFwtGCI0P_H67XJkkWiG026qJGJaDvR2IWZjA7euDNx5_xrHpbOxuXC7uDPwu5gXPFPzH0dCmvQuPAyaQqydLbHG2E1M6iwc8WwLmbamoNG56Whe6HrI1nqhxiQbev-pmyl2CeCAXgZXtz5ZORdd0Orr40E8z6PJp553kfzL_dsrCQCODC1gycxbThrjncmSJgOZpFrKzsa9Mceq6iZc0keqmG5XJ7zili7xSZ4K9cr18nIQXjj_FVu9CY0HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
اسکای‌اسپورت:الساندرو باستونی مدافع 27 ساله تیم ملی ایتالیا درخواست جدایی از اینترمیلان داده و به مدیریت افعی‌ها اعلام کرده با جدایی او و پیوستنش به رئال مادرید دراین‌پنجره موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/27072" target="_blank">📅 23:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27071">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDj6r0CCzr0rPJSYaKg9OmN7kY1ej5WdOUpVVRAgT37DJRKVSgiXtRN0xqFmQgrTKrNa7pKMrgt3erLSiTpO_KHaq5t80_KAkvXYT1axU1rQieqMqFROBKjWGBR9T1Hg2QzWVkj-5izPFveUUQBxILU1I9Gfy5OdXkYUNfTn8lTEXOrde3Uczice9ODHPappsUHIcGG5CMMv-RnjD9ZKf2pV-6t2WsDFq_xGRvG_kcZzDfkEgtFLUbQzyrVndOhCNkqhwhGMKgEE9YWXC2hQnuvMixA_agUDOn5Gy0JUq9jrLOcRnCHpfjGJ5p_0d9IRcYe_SbFd910KTKjW2FsouA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/27071" target="_blank">📅 22:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27070">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/US5UXCbdPa7G-fiYPThNytNUB4DfGAM1Y9Gz5EwBNT9leeuIK3iJNeLWf4aP15IqYPexrjaeobyffA87h3-VdckY3dh-A_MrlaJ6T0n4vcZiBmVojnSPWN6v5-2QGPdRTtlh62SU4OPh8QV7XKC8nc59xcnMyR6FzdJGwfhtrKwL_GO95Kt_wLFe3WdJ3X4UPwa7SsOXYjWBkqdYJReLOSD0YiG8mT8YEfdd5tjZrn1f8wtAYFK3TfAMMD1kPiR33K0xDJMuXEw3DhLUQq-Ep2xx16SFge2fOLKax7DGE4XHAPGLVxIcO4YD0p5vI13Z2Q-3e0ZkEYAAp-a5UAgQ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ دونالد ترامپ: این آخرین فرصت ایران برای امضای یک توافقنامه خوب است. امروز یا فردا می‌فهمید که چی میگذره. قراره به زودی و به یشکل دیگه، مذاکرات پیش بره. کار خییییلی پیچیده‌ای هم نیست. قراره فرداتنگه هرمز رو کامل باز کنیم. بعدش هم در مورد ظرفیت هسته‌ای…</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/27070" target="_blank">📅 22:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27069">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHP3ZuX5gADFWobjmtzotaerPMXA592Q8cXAcORQDlPDx0n9zc8ywDZi4fKOzhRmT9j3JIF4ncgXZ1tPCXEYF0cnYST9ek4gYIZFbkb1Wvtxj7HaFrHrx30jZXWxc-hKmCwFtp2yfH4RyND8i-ywRWjD0a174sIZww_rdvrW9muh9PQ9HjF3CiEcV_8zmDCTcy6ioEOGrCZTJnNhbPnTk-Zq-uNm0OsehCV9ieMI6t_AUUbMv-0hMuzyss4zZVIJLxiINIAr7lwq2KP_3BdWEKQqT27iWMr_70rJ35fdh7krdSe8NkdEMCa-wMzAEtaV7nDod5NiyLcENCdIoWEYYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/27069" target="_blank">📅 21:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27068">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97c6b80b0.mp4?token=AxZmd6ikRPE1A2-h8c7EhkqE9R1hQhoT-dSBt3qiWc7YbycofIawbSx3kv_5C7c9Pj59mLhhtMSKBpNMIvPqmGCFyAy6lpjCQVvj8qNk95hCDld-amZLsc8SNqgCf1lfJQc781ni23juSKGVs8BHIffM2B57xqtqfsanmWhHggJOetXw7TinGwpxJLuQVf0Xexq2CtqsqhMG0Q4rOOFDCConLoPxCQEqKZqzCrU5-GaYBNeYFaT3ZtDxgREbPAmT6rbsVQ3NBRtugPZG_e9grp1uVLiyrdIKTkEPvMo9J_vD56kmFd0oTLTI7u8XgIyf_DpaOOVSUgYm1EhXO4aH9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97c6b80b0.mp4?token=AxZmd6ikRPE1A2-h8c7EhkqE9R1hQhoT-dSBt3qiWc7YbycofIawbSx3kv_5C7c9Pj59mLhhtMSKBpNMIvPqmGCFyAy6lpjCQVvj8qNk95hCDld-amZLsc8SNqgCf1lfJQc781ni23juSKGVs8BHIffM2B57xqtqfsanmWhHggJOetXw7TinGwpxJLuQVf0Xexq2CtqsqhMG0Q4rOOFDCConLoPxCQEqKZqzCrU5-GaYBNeYFaT3ZtDxgREbPAmT6rbsVQ3NBRtugPZG_e9grp1uVLiyrdIKTkEPvMo9J_vD56kmFd0oTLTI7u8XgIyf_DpaOOVSUgYm1EhXO4aH9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فصل آینده تو بارسلونا میمونی؟ فران تورِس:
‏من‌قراردادی با بارسلونا دارم، اما در فوتبال نمیتوان پیش‌بینی‌کرد چه‌اتفاقی دقیقا خواهد افتاد. من هم فقط منتظر هستم تا تصمیم درستی بگیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27068" target="_blank">📅 21:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27067">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d787366ec9.mp4?token=sOhWdqyJy2wQodtMvHLh1K-Z7LpEQKGYM5arK7-c6tpUAjH--QRCJgJNfuEhrs86L2l53LcHbuUMFmwI64PqlBVDkFPt4C0c6QUO2k6_9jYsVowDt2T14qq0YiltwXHDrE3y_KcWhYkv-hEG1QTLzNGNXvCiuafiDIKrZofuoSD3vFQ0rgfz5eOlpaQkFkrs7W7Fy4DFGOFINc7j0QQLVkNznnN4iXQfC4FuF_zpzdjzk3cVaqfnP2l-XFlAnGSyM11nvZdHjV1jJgyKPMxYb72toExgzQdu8Tl9CXIwv2jIafiGyVVzESS1kYEGhONEUHyPGsO8N7rVMROiWB3q7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d787366ec9.mp4?token=sOhWdqyJy2wQodtMvHLh1K-Z7LpEQKGYM5arK7-c6tpUAjH--QRCJgJNfuEhrs86L2l53LcHbuUMFmwI64PqlBVDkFPt4C0c6QUO2k6_9jYsVowDt2T14qq0YiltwXHDrE3y_KcWhYkv-hEG1QTLzNGNXvCiuafiDIKrZofuoSD3vFQ0rgfz5eOlpaQkFkrs7W7Fy4DFGOFINc7j0QQLVkNznnN4iXQfC4FuF_zpzdjzk3cVaqfnP2l-XFlAnGSyM11nvZdHjV1jJgyKPMxYb72toExgzQdu8Tl9CXIwv2jIafiGyVVzESS1kYEGhONEUHyPGsO8N7rVMROiWB3q7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
دلیل ازدواج کریستیانو مشخص‌شد! حتی قیچی‌ برگردون تماشایی به یووه هم‌به‌پای جورجینا نرسید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/27067" target="_blank">📅 20:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27066">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cObgWUvlnbK-WWkoUBk8SSOSJ_T7cKetvdyuu68x-IvCMEppIae69TJma_dC3fzrQNwRr7a2HVR9dC2kujw9AGZubQSV4hafvnwgIOqS_cvfNDGugAc2-DyX4SL16uvA_3Rl1PTOTkjZ32HcQoRzsP_GSAP2tD-chc6gbWVcguEh7KIbksDc4_Sl2qzQzpy6iUWakSh9mVKmntw53Vwj-FtUdoIHrlYgvh7W8DlyZjQuS-osK3RFnQV7X8h0mJpACy6l_bTCtNgPCdCK44sNHV_eCMeC6Y2WkdiplJlOsGRHG8TFBVhUUdO-RKHR7wAzBmxJ9ezAcaH6oMxxPL_AbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
طبق شنیده‌ های رسانه پرشیانا؛
یاسین جرجانی مدافع‌میانی22ساله‌سابق آلومینیوم اراک که فصل‌درخشانی دراین‌تیم داشت با نساجی مازندران و سپاهان اصفهان مذاکراتی داشته و بزودی راهی یکی از این دو تیم خواهد شد. شانس نساجی بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27066" target="_blank">📅 20:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27065">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xe-rrW1N6MgiZ-pck2a_zr_c5uidxc6BAUczC5302JQ07xA_T6Cl0PJ1Ymc0kW6bGMGUWgpX64Mn59wUJLdcbHin1MmBBH-YETflvlF2YoGu5boJiUA2hj9JJxOfFFnhxYNCu0MknuqwWqc93y0wH5BsTd3Bed-DgHRlyetJ-LnlHscPIuhFewPzdP3xcTrbaTs8Tq8YGhnCTgUbsnqeZF0VuIJn6N-xDEPhFdzuAwIyIbqzOrRuO8s7MsSc9Il-c7ZtjWimnOjPlbZHaQ-1snnAzO23sLeuqp-LHxOSiXih7nJsYEVsv2E5R5kbogbHTcOZ40pZeDbF6krXAUKWOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
طبق‌اخباردریافتی‌پرشیانا؛بعداز عدم توافق با مدیران سپاهان و فولاد؛ امید عالیشاه عصر امروز با مدیران باشگاه ذوب اهن جلسه داشت و برای عقد قراردادی دو ساله با گاندوها به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27065" target="_blank">📅 20:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27064">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAoSeJiSjLyVOqyxrlfWaE926WRkFi1LuOK76cCL99Nb5UIoqxUmn3-AtGsaBPmpwWtVL39FYyZjLA9ZISAQ2dDVxwPOjInA_s8LsuiLQHcrAcJF2Tu4Wg8xIrhLqhlF76yvvhdL2kCNpw8w2dDe8F7drqOVo-cbeUIPtBHQKKeXp0-S2cST2pT23afcZS0L5okSQcySMU4sM7AmpwsoPI2pgd_eDl18lHDBr8QjZ3wnCcwnLh3wx3VHVMwUaW6LbVNWi7U-lDdPIYWe-CU_eNro4yUdo3r6Xp4qm6Pm_azMTRkAWurs9Y8F2F7y5yOH-izLrnhdjpcsLrDsKWsYFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
تایید خبر اختصاصی‌پرشیانا بعنوان اولین رسانه؛ اولیه هدیه ارزشمند سعادتی به زنوزی؛ هادی حبیبی نژاد ستاره فصل گذشته چادرملو با عقد قرار دادی 2 ساله‌رسما به باشگاه تراکتور تبریز پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27064" target="_blank">📅 20:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27063">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9EuOUZMYW77le1-LOzoJqXSmWKwzuGQMiPz4aOWkNwhGcWK5rf1O790u07LU7mNJlGRWIfP_PZOG14HTG5xkpmFGkNg3GOXlYUh7Oz9R2w-tlZCaETpwFMpo2TVO7_Erb9TahH2YF68060F4RFTg6FrtoNHBxMLRttTkMnkYQlYT1Huc6B9Om02f3Fkl1n9UQIAr2zsHKFarc19p5qy0xliYIUznrPxeLGQCF1yI0YjjkCCGOc2w36Qdo-3yU1fW6OpHNc-sajUrfU_uhdcdrlBD3iJ4A8A0HsaaZZ2ZyE6TyN_fA8rBmTtxac-DXBp8k0ioo1elbjCCDpsI2YcMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27063" target="_blank">📅 19:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27062">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab970d5a0.mp4?token=l2k84PC5xcOrmfezRwg-ZH-rrqRp3M8TKamRjPNi0OV5-j2EDudnZ66rLNLxycfGbGS3d8UgfhidQjFLSsjwXRoJGHFH0fvtA9aKCr9NpvNh1knXOaeVsvEBqpBDDASLfBxWvJ3Za_NSlhcX-rTygUrPKEbsq3Q94XnZdQe3-MW6qWhdWM5g-MM1mIVS7p_m-0rqodoR5UqqyaN_DBZDZsxZIFVMtv2R7v5H-r2D6qDZSsnTklBBnPhBMFoK9khmYI61PBsINrE9VJ6RGeGTthMh3GthNzL8G3MsJifINSv7w0zh8r0fq1zDWoCHPUfiuFhVUogp4MYy70TgG1PbEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab970d5a0.mp4?token=l2k84PC5xcOrmfezRwg-ZH-rrqRp3M8TKamRjPNi0OV5-j2EDudnZ66rLNLxycfGbGS3d8UgfhidQjFLSsjwXRoJGHFH0fvtA9aKCr9NpvNh1knXOaeVsvEBqpBDDASLfBxWvJ3Za_NSlhcX-rTygUrPKEbsq3Q94XnZdQe3-MW6qWhdWM5g-MM1mIVS7p_m-0rqodoR5UqqyaN_DBZDZsxZIFVMtv2R7v5H-r2D6qDZSsnTklBBnPhBMFoK9khmYI61PBsINrE9VJ6RGeGTthMh3GthNzL8G3MsJifINSv7w0zh8r0fq1zDWoCHPUfiuFhVUogp4MYy70TgG1PbEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ویدیو بازی‌بیلیارد تو اینستاگرام 224 میلیون ویو واقعی خورده بود که یه رکورد محسوب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27062" target="_blank">📅 19:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27061">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvvS8P9kuQaMBxMiRRuIStoWXTcwpvXIMpXzzcQZCoT_yHtnfP0FEGB1zeWPLosLdCI4qEyTvvw_drUQZ5h-QRaIdCcjiSN1JepuAYsTTjdaMykg1HAjVhqxFo6UwF-nmiPJ-bVVjAMH6N6SlfULO8S--Lj-Jkg18Wvyl8kDA_LGAvQWMTdTIr_HCnNujvuLDuVbZeS6u4DLc7eR9j5CBTw-dMXqkPBGNOzTVpR9XqeVG6h_Z2SyyzeeWcJAvEPzZW_rqyaQydKuq-OErrQmybCVzpDTgbJQPNuLjkELKl1yb0h2YPp753H0ZJTHs9_9x7LtMbNwGxVWvQYQYyT7iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27061" target="_blank">📅 18:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27060">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bm7zWTtG70DwcFgfd0xVYip2GGItfFL43B2oHmCtUPP7MbK2a0vXmtBH1yV2HQh_HqeCcGRk8tpV-kl0HfOPwxmzIoBQMu67JW_M1rG-DqLpUhdkpTykA0l6xlbIigD5nUJOMFcYH9uVYOtqI2uq-D7qfbgdJ661PGbIfbUeTepHJAdRQLo30COd2vYM--zR_mm6KMYCwvOyCONze41VETUZcEFcnh5VkMwTld6SyS-D1oBDEdT9jzhRnVle_SyuWe9K4emozaiMi5v2qf3v7VYjqYFQReRwBHhJc1bgneJlyfmImc79nLShOVfN8OT-eCBfyQOvx_mcX48xp4E31g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ نگاهی به کارنامه لیونل مسی در دوران حضورش در پاری سن ژرمن در تمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27060" target="_blank">📅 18:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27059">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqktcWHLZvJspKlDh3QNhGMY2CZFHZ3bbbiKf9kBLMjrBeKEdTtWcfHx6HKaSxP0e37HWnrwQvbNnDvkx7-BPfFlx2OKu327f3eFpTqAgMUGKbQGPMupVuBeZ_E_DpuIDa5BJqzCWFuOWZWK0FsdE8MlwjI5OYFlXE2yI8pIj3glPgzsfnV2W7M2WIa95b3gAWchwuvtlcF4brYoapOw2HP-rkX6AHefWHVW22LFUVkDx7KXDmQfSyYP-bwzIk0hGsBBzgiPLke_fzjc93eCrTKYpt7M6PVzUnbxRcDShMYFjITAc-Sta3lrNOZZB19YfpRglQ6tp4RyPV-smM49kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛بااعلام‌فیفا؛ دیدیه‌اندونگ هیچ مشکلی برای عقد قرار داد با تیم استقلال ندارد و این بازیکن بزودی قراردادش رو با آبی‌ها تمدید خواهد کرد و از هفته اول رقابت‌ها در خدمت این تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27059" target="_blank">📅 17:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27058">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nodPV8jBy1hDv4VWtEl1pBD7q876CjWKn_nHy76kpUU5cb3BsRTp2dAPZxXnO_Tz1i7JFiU4shwRWSlxnV0PeDWTrdUN8Qk3dOmQrC2xAxXL6NPUzwo3BRabpAh_zthjroGnCWxik69bDYOlUTiTiyiqkZLVzBI87VZB8nxqqWaK4WQQglHdJLIgy0noN26mbUsKWsHNRNk1VXjtHjElz-NciCIO_nWXLImVmPixZ4Vo06yJNOK4YxTCyUVOMJ0aPtifWORe0tLudOn6vCho-Us1yW0PD4ZTO0zyHhOAolHbFN3oMgktjwElPdq2KPb2aKdVySfhoWTxSHCeg0UfNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هانده ارچل: من از بین تیم های اروپایی طرفدار منچستریونایتد هستم. علاقه من به یونایتد به زمانی برمیگرده که کریس رونالدو در آن حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27058" target="_blank">📅 17:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27057">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvRzwmSPpyq8I3yR89dGNjhUVl0QKD_mlMr812AxoAXdZLEY8f6zi5IvDVeop4aFd_Zjs64TVk2ypFVNF6GHfEvpC8hlYEjCvWxmsOrBlpHCc1q_HO3Fd7D1QPzQVUgEAZUqPVFYzWQKWM2xP-h_dvxcuDiPUsNPWJei7vb9ov1JAAhj7UqP27Tu8GT6CP9fJy9_fvHfR35Gdi2vOiu-JNXw9YQ97v6tiUHFbLVeZ9uqZTV2bcaXBqNCsl-aZ235tuShYYlt3Y-VStfC9iBhdcExqQNmE_2zOwZ0wiW-ZtCrylBFeJZvPhOqGGoPdDAUIYTrAfRHOb4jeFNIByxADQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27057" target="_blank">📅 16:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27056">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmkghedVlwCSGfj8gknl7ZjHAPOct3lHZsUop6fpm02n4ovdpHtpoh0HvXINTRvRBcgWj-C8aAw6bgGk8Vojz4pUOh8PUxNlWBpj_aS_C008HKoCjrVqE1d4esJpJPDm2AWngrorTAb0GuoiYHYbDrGCwU1k2B2n5juvkLyDDDVrh01SKIUR1B9cdRjUfls9j2nmMXRGUSo66V2X-SDpASOG1UuG-xhhr_J2zC4X5wWVI5J-tcC_6w446UU_oG_951Fb6fUyhPQyOj93hVvQLoeehV-CmeAY_o5nnVw8GdYQAslFvrjSY5AA8kmbDLM-Vbdjg21LdX9JJJO-7HF6_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ سید مهدی رحمتی سرمربی‌گلگهر ساعتی قبل در تماس با مهدی گودرزی شاگرد سابق خود در خیبر به او اعلام کرده که پنجره باشگاه استقلال باز نخواهد شد و قید عقد قرارداد با استقلال رو بزند و راهی تیم گل گهر شود.
‼️
رحمتی پیش‌تر نیز مانع حضور…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27056" target="_blank">📅 16:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27055">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrCkJiRt5unp7mtxJtnlfHYz3N2ZI6bvyzekGqJslgX_-2d3WX82zuDQ0W_RPnGyT_kr9YmJFe6amVi_ZY29_Zi6pWMA5RGwyxPtHxRk5v7bNRpvbnu8CUnFSIQEzjA_Xitbh6C-EhMzdqKWld_0KGdB-DvXLfp9qmQgaQC7wkB-9xlHLkqI3dvOmCD57KsgDrvR_XqfM19EYtFhAvMAvI1dUJVtXdE-18hJvQDMDomzD5qDglS4k1koqRd5Sjvyayr-WuR3WWLA3EKw8NHcVSe9HaeATEdT4DAbO9sucJf8B0P1UMsKXnTT2X2U1_QgjPXR2jf95yL7RAzIpyJRRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔴
یکی‌ازمسئولان‌باشگاه‌ملوان‌انزلی در گفتگو با پرشیانا مذاکرات و توافق باباشگاه پرسپولیس بر سر انتقال فرهان جعفری به این تیم رو تایید کرد و گفت تنها مانع این انتقال مدت باقی مانده خدمت سربازی اوست. درصورتی که فرهان جعفری بتواند کسری از خدمت بگیرد این انتقال…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27055" target="_blank">📅 15:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27054">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2279080601.mp4?token=PMFfSndACuqoWX5iqIRFYSoyPj61qly50k3-D3JWAAAMKqQvwwGB1fpNmVCFdDOUrPNq4cmH2t6vXZA6I7wQ8kdb-S4DuNfti0pJMNxnwNXcj4whfuzWvEprAC3yy2UTrDQRaTPcpubtwGHOZaWW6Tmoaujhna4HLwEnwEJgGplgtN51KB3Mr9fbyrbYdtuw4oE-mM2EjROeaqDqMSY1ge00eOenTdI9OR683czviYIEe_2tzPIWbmNkF9JLSifML4arAS6MmlhL63aKKRHWV0gY7EiGiz_yCU9pWUlLi4oS_cAcB19vQgl1nc3wIFMUH1hGJZlDbQXn7jLGApndJDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2279080601.mp4?token=PMFfSndACuqoWX5iqIRFYSoyPj61qly50k3-D3JWAAAMKqQvwwGB1fpNmVCFdDOUrPNq4cmH2t6vXZA6I7wQ8kdb-S4DuNfti0pJMNxnwNXcj4whfuzWvEprAC3yy2UTrDQRaTPcpubtwGHOZaWW6Tmoaujhna4HLwEnwEJgGplgtN51KB3Mr9fbyrbYdtuw4oE-mM2EjROeaqDqMSY1ge00eOenTdI9OR683czviYIEe_2tzPIWbmNkF9JLSifML4arAS6MmlhL63aKKRHWV0gY7EiGiz_yCU9pWUlLi4oS_cAcB19vQgl1nc3wIFMUH1hGJZlDbQXn7jLGApndJDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقادحديث‌میرامینی‌ازشرایط‌سخت‌اقتصادی:
یه‌جوون‌چقدر باید کار کنه تا بتونه یه ماشین بخره؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27054" target="_blank">📅 15:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27053">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXV6XQno9nZwCTSfkUj6aRDNDMA5h4ws1tif5IMXELWV2JOlE-TQMRdHWRw_r3M4GX7Tit8avqJmK2pmJOBZ-yWcjH1-5x8Z4q0PfJaezIC9L87ZEqFIXUQ1x9HoCTSxbv6sy8vYuP4fLekKpBYnxFOPP8IDkhB5UbLdfY_xjf7qBQ776RDhe4AE0gEFt_QnxW5OLOCprY6A2Fwj52szsbXQ68oqNp0Adrt4iSDqbN9ViVVfBi-g0K2ymWlKpzu-uDpfPKFlh7lBFwn8_q0dRKYdX6kiEldSiyks7vUyydjA8AmXVPoE1-j9s33alUuvKMxjbCseDcKc02pyciuoWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27053" target="_blank">📅 14:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27052">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkS2JDPdywB7tLeuyTjF3Mf0S0yA2qBB90_6Z5MVut_II6rWfoow7GKVlWaEmbMJL4HikpZAQbm7X_sUmwrGg7rhw-SqPeAD3Se_LPy0rDqatJNClfMU215OlmVrv2-Z6-0-VNkU14502e0aPT6XpDTRk5ZLuZ5unOup1_m0jdCLajdEYPK6-Jxyh5C0OpWO2sY-iDrXFFsIMwoUfAbZ8xxA_3jGXB3kC3ehPmekShNdmFoiT4hlDylil01_O_jt7vLGMFvSnX5uNR1pKbVp53E3pX9Gm-aKEgsJpUm_OzWXnyDFtu-KP_LnS7pbpJF93S8rz_TdUD94aOFpDTE6_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
احمد گوهری دروازه‌بان‌سابق‌پرسپولیس‌با باشگاه صنعت نفت آبادان به توافق نهایی رسیده و بزودی با عقد قراردادی یک ساله راهی این تیم میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/27052" target="_blank">📅 14:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27051">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_mFzcOZrb9FSqDJvEaOhbtIN9kwIDclDhcMcgagCaYPN2eO1X4mcP45AXbDm9zpRgA9hzYuf8f7CES_4ZDjHtG7q4RMH0ut4-BMPuKB_xPRndkA7XqUab3cncOGpcnQjUaRINsYtwEI76AyJ7yEwnobO8CpAu06Ic8eZAkenFbrU-jVQV1mkHJbzJlJZmWz13xsmvf6QqVb3hlN6hQ4xADwPb91jwBP0Byty7UfnA4TMyKLUV15QmXm9Yx03I0zFqqyC_1DwGPtUxr6Sy7U-rH1B2H-xXRnLxzLYSHAPBzlVQl4QvxwMTfAJlAf4rkit-MvAmTP2GWXwmXf3yjwKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌_پرشیانا؛ آفر جدید استقلال به رامین رضاییان برای یک فصل حضور در این‌تیم 150 میلیاردتومان + 50 میلیاردتومان آپشن گل و پاس گل و قهرمانیه. رضاییان قراره ظرف 48 ساعت آینده پاسخ نهایی خود را به این آفر بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/27051" target="_blank">📅 14:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27050">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCBbWxsDSvDiZA7zjWc_J54REUnB5DoHArfrUZsbFeXTksZP3LFrAZzqgvayzFge3Mg379A9gp2Rr_ybq5SRZywDxf2yRuBQ8ELhxL-i7MVPvjbW3SOCEq3kFynaM-kWsttF_s7CVu46gjCGe2LOB2Pc2B23xg9eRu7tbUedClhuSKHmcOehHQWAW2UhIisKYPM_4Yka04a3j6gKbqTw7oCJXwTiKSNBOxdGRQtleJZwCq0HRM42r8yJYHpyXoEiZvpB-YB0ZVXKbsZTyVHK0js3rM14EjIhbLKTgrb9Ypq5KtYKGJ6DAePiFOJ2aoM64nlrPjPL5SrVUOZ17GvbuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ جلسه پیمان حدادی با مدیریت فولاد خوزستان به صورت ویدیو کال و حوالی ظهر برگزار خواهد شد. حدادی امشب به تارتار قول داده تا پایان هفته پرونده‌نقل‌وانتقالات‌رو با جذب 3 بازیکن ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/27050" target="_blank">📅 13:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27049">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dac122529.mp4?token=V30TSmidXx0tBxH1tD9ONR5nOFrq4Os5bZjPFpVzHtJQmBUrkUDZ_utNDLBouY2H1yorMi5Ia3uelpNS8EVWtV-aH2lxd6ATo2ray8rNCRGn-4sjta7Fxy85x3leguxl-prEC6nkWzTDR4HKwpVQoy658tQuiVY1u6nk3eSAIJy2TkegUKW_qC4Jtl578XIhyAi8xxaLOm9rdIO1hqrkGqRcxu42f_2PhCcVQUcwsOG3w99IdVkp2u1DEh4w7FiPQaADW2aHvA7ttxVr8i1Up4QyxKtytghrOcmfL5BpniajEpvBTKzt-yRKERpwK_gOpzgSMk-0SaRY_wLPnOUK3FkAru9CH5pLiqMPVSWlbu9jMpDFBRX0NzTGhob5vJpT2uXhrecJTOYhzkgtaExE8PANj4jFdSP9EulOepTzEESHZhcccdzwPyVm5sE9VKFh9p7y5Ulej42Qjitpof9lvqnPmbF3Mu1FfjZWBt26Dqzm46qyHUPWCIUAk9Efp1sG3KRrztWs_aADqhmhkKdt2gFM7SPfuOseNqJB0o44HysZFxBI147ImKwgxmoOVPjtowDUh1v_eEtXHgTNmYFYUHRDfu5tnNcx48E8rjwXPFlhKdEXS49QfmclvujqLBp3LS2_p46QroI3cYyJJEjLl6HT5VMcdCeNJfhCnO8c3b4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dac122529.mp4?token=V30TSmidXx0tBxH1tD9ONR5nOFrq4Os5bZjPFpVzHtJQmBUrkUDZ_utNDLBouY2H1yorMi5Ia3uelpNS8EVWtV-aH2lxd6ATo2ray8rNCRGn-4sjta7Fxy85x3leguxl-prEC6nkWzTDR4HKwpVQoy658tQuiVY1u6nk3eSAIJy2TkegUKW_qC4Jtl578XIhyAi8xxaLOm9rdIO1hqrkGqRcxu42f_2PhCcVQUcwsOG3w99IdVkp2u1DEh4w7FiPQaADW2aHvA7ttxVr8i1Up4QyxKtytghrOcmfL5BpniajEpvBTKzt-yRKERpwK_gOpzgSMk-0SaRY_wLPnOUK3FkAru9CH5pLiqMPVSWlbu9jMpDFBRX0NzTGhob5vJpT2uXhrecJTOYhzkgtaExE8PANj4jFdSP9EulOepTzEESHZhcccdzwPyVm5sE9VKFh9p7y5Ulej42Qjitpof9lvqnPmbF3Mu1FfjZWBt26Dqzm46qyHUPWCIUAk9Efp1sG3KRrztWs_aADqhmhkKdt2gFM7SPfuOseNqJB0o44HysZFxBI147ImKwgxmoOVPjtowDUh1v_eEtXHgTNmYFYUHRDfu5tnNcx48E8rjwXPFlhKdEXS49QfmclvujqLBp3LS2_p46QroI3cYyJJEjLl6HT5VMcdCeNJfhCnO8c3b4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇧🇷
#تقویم؛ 9 سال پیش در چنین روزی؛ PSG نیمار را با مبلغ 222 میلیون یورو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27049" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27048">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gF76gJYZJsXRlmeniOo60tkZ4Iq8i6kVeAmF78UvrVysa-jt-OMq5lEDjjlD3GWN9q57yimdEPh7_q-rHptHkD6FVCmTI2eKFBKq_fNFmuKvcLzNcI3mdgKHUGiLDEN-uFMue_pstB61RS513jZPlT1_oH576RPOGjF4zbgSlp-jUkaEKMYIEs9FVoH5TAb7aAGX4L3XPoQHTH-0mqG1_PO-bDrFvPkdoZUJ8O_cOKehajg1rEZkc7k0vlfVIvuv5mQpSQcT8HXKFJKLI7dfsWio46XDwr22ydDZzgv3TDxrHrI0ErGDyJfSe_I0-ciJ3dVEgEVKn5R3jga1GChFgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باارزش‌ترین بازیکنان بر اساس سال تولد از سال 1985 تا سال 2008 با نظر سایت ترنسفرمارکت
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27048" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27046">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpheXvL3YoWPX18aMKxpXq8GRtSxEmJy-pgUNRNkbcBbzD4XxP_dnoCreXHf9p-2YrZ00jAAKTimhpPva1gktvaMSvje2xXeAeBi2e3YvlkQDOSkQo6WpirIU36K0E4xKyqV-Exd51XtUQP3_lVvWbq4LcOoHYeF-SR1beJO8OxnF9mVi8sfHLCm-mTap163dMlUIjoAM2twErdOluQdqkyHRqcez2MtI0wdJ3ogZi0r-RCHrTyqH4fXjHZrLgu_S04ojoHf53LmX_fEIib38VX9QeQs17TVf4glM-Ptg1qakxZ4-p2LZ5NIA5x19pszwMlwht2TNBcdEsAA31hLeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛دیدیه اندونگ بزودی با حضور درساختمان باشگاه استقلال قرار داد جدید خود را به‌مدت دوفصل امضا خواهد کرد. تمام توافقات لازم بین اندونگ و باشگاه انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27046" target="_blank">📅 12:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27045">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7UZxIGloveyy_p_y1_Ug2Zz6gnwj0xziTxOHfHOSfvDspj0nqY2xTuuEzlIaMBf3fNmyOtoT4kSlS1UWS5vJ2rm7rfyXOKot34bczdndVRk6l19p4zC4Eg5YwwL0K540p5JP-oDF4Cin8rmsDYfMCvDNwIQ6xi4cPsgDTRGhxqOv6yJ1oyMtmW4vn1EzSmSonnY9quJueCyaUcj-ewwQ1Nnho3aRsXP8hS2o1YbYGNN0CzAs2FabLkEPLdv88JvB_ccE1vV8hRds24w6SYC_yv7MKOM4FJEUQCQjwL6e1i3ZBcu5qKPnV-P-h9ApCF3_Hdn9vgtnYV06lBqp8SCCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات مطرح شده؛ فسخ قرارداد یاسر آسانی با باشگاه استقلال در فیفا و سازمان لیگ ثبت نشده است و درواقع‌فسخ او یک‌نوتیس ساده به باشگاه استقلال بوده و با بازگشت‌ او به‌جمع‌آبی‌ها او هیییچ مشکلی برای همراهی تیمش از ابتدای شروع فصل جدید رقابت های لیگ برتر…</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27045" target="_blank">📅 12:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27044">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7821302722.mp4?token=opyj7JQJ8WGE5_qpTwzYPrv70JlC6vWBQh0tvlEvn9Hv_oV3XePGENoxLqfHR7RXRWwqrmHyrBy0gGjta6-h7mwk2L5BfUEqWC1D54e-Yn6U6J0C5aSfnClN_7gBDKgSjXG5MN49oKnrthEtYOLq9pvW2-23gPTRpHBL3IePcGhtbXfapIDxt7UXsu8Z5s5td_On3_BMnfAywrl9MvCqYGXCqeX612hMaFkIC_csrNE0DymoRvtSk5-Y7Trh5ztEBxBN3gKl3fZst2_y0bulXJtGpuGrxD3eHyo2-k8c0DTUPZj0IZR_i64YYeZsozcgH7swMk08BY8ek296dxBk7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7821302722.mp4?token=opyj7JQJ8WGE5_qpTwzYPrv70JlC6vWBQh0tvlEvn9Hv_oV3XePGENoxLqfHR7RXRWwqrmHyrBy0gGjta6-h7mwk2L5BfUEqWC1D54e-Yn6U6J0C5aSfnClN_7gBDKgSjXG5MN49oKnrthEtYOLq9pvW2-23gPTRpHBL3IePcGhtbXfapIDxt7UXsu8Z5s5td_On3_BMnfAywrl9MvCqYGXCqeX612hMaFkIC_csrNE0DymoRvtSk5-Y7Trh5ztEBxBN3gKl3fZst2_y0bulXJtGpuGrxD3eHyo2-k8c0DTUPZj0IZR_i64YYeZsozcgH7swMk08BY8ek296dxBk7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
ویدیویی‌خاطره‌انگیز از شوتای‌ فوق‌سنگین و برگ ریزون کریس‌رونالدو در دوران‌حضور در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27044" target="_blank">📅 12:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27043">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtukNXdqiugYU8r4kGDdTzZEUWY-S1OUYq75UFydZZFJf7fS8I_UT4XITkgwlMJBARunLuuWOXbsDCOaQIHwmtdPDTvMLdGSrTuR7oLKkiYS2JPdbYe-izifpld5P7-s3kMdpkhfoyHFVD6bgHpeSo4TYUv5nroilrutJFqZWvA1VDljoZlgnkmmP-1EoJ1UTpLLQhpaP13uvXYAkWa6m9k02FFRYQ8OdvHEt1HM81GSXCJZSQA93ihuAA81aF_yxu51G3N02t0WX-9dswiARrYgfX_6qaiRctfcMg0JdgzUNIrCY8YjRH2yeyr2wt5CUDk7XZxhKO3jjcR8qhfL8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ویدیویی‌از تکنیک ناب‌وفوق‌العاده تماشایی نیمار جونیور در دوران حضورش در بارسلونا؛ حیف صد و حیف که به اون چیزی که لایقش بود نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27043" target="_blank">📅 12:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27042">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGQCYBdrhKWLCmlqy1kDUFKJ2_SPDoEuJ-u7Gq358eEA-rpSrh0znu9iVSihIJfsT378JHhfCfraZGkKo8yuQJfi1nTtUP5SCWqVZ1mt0BqMfmoqHKSRvlPViWQKUqqfr9A71ote5rkAqlIyS4-HVFiDww4KhFVd4Z7u96diJH3pEtIJdKKKZLcd4mi2_xQTwfjzxtTW6Vy5i5zM5ovFciNbNX4m5hN1paDXQAoa2qMzgXF2xpquVa3pJmUdES68-904raKOWSvdkpa9fkWHy4zTbTdhNVEAB71lJSJrEzkY-CrCGFUvbSzBl8z54d2pTK04SUfZ_EGFiss4yRwByA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
💰
#تکمیلی؛ بعداز موافقت مهدی گودرزی با درخواست سیدمهدی رحمتی برای پیوستن به گل گهر سیرجان؛ مدیریت این باشگاه 80 میلیارد تومان بابت رضایت نامه گودرزی به تیم خیبر خرم آباد پرداخت خواهد کرد و بزودی این انتقال رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27042" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27041">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBDLuoHPRMz-uEWBUfLbxOvS67yjBQ7eQ1jhV9w-Y3DVnGBI7IrIbd8IKy91evBM73VDXicF7q6pX0ci7y-0eziZbB0CIkhEtDasn0brOIQyXSMtkYXx3-6JGBcbpVaswzVhxKN0Lit0Q0NbDJA_6zv2zDLKGUaWNfLROkcCFGYaNUMF4aN79_SqmXQHrzBK2wmaaNqHKUU8xcYoeyjq2lemaWG4qmW-EzlLvZ_vXRaEpLIixRxd7OyfwP4Pl2AL9_Wj5FJCF8gpoxnuL1G2jikZPoZ-hbkFE-8pjpEg8mQk29vizLY7GzQdCkBtZpIqLfgxjRkTbkkEKZtZAQnCnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت‌هایی که توی ۲۰۲۶ درآمدشون میترکونه!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27041" target="_blank">📅 11:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27040">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgWSta5lK_KvcCK8S54R_PW6f9xy_pxru6pP6z6g6E2I_r8qu6vdt_3G6_ZEWlotocvEAZ48TOSa2Jrzlb43-OQRAKFG6t1hHDkxpx9OGu_VnXWIieYAhlRy-3-1z3k4WVombgxWf-cvEnibCyuWXT2_U9Wk2FhCAHDfVkE4h4rKsCRZO2Tgn_PaDRsekSP8WqlXW7MP0swulVGCZE5ZnOi1bLz1Xj4Q0dy68g-kfaG3-A7L6w30FaPhi6Yk28L316LdcGcKccrO6yvPSIEvzIZpoHEEDxXrwGjVsPIUZxUbNLwvPiFVw7VhMOvVmXEHqZd4Kkd054FrInFuglzx1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27040" target="_blank">📅 10:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27039">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXJBBOXKUtZgYPcEdVaJAQ974r0ECqHtSQCFpXi5HQpA_sew7wBXi_rzLcfhdlQvVpWtdx-cvO6LN_93lc78ruHm84SZ_IrJGP_HKIfajhgz_vYMcsBPwcqV1JsNZicirI1qf7bk8jeiM2ppe6nPnnbPqo4A8oE_37NmHIN_urVHAA-X5UxpMf71MNlkcMkRo_DcP1qw8vtDjyG1g9c-ZBhidMHTXUN59dEopFkR3gwZzQUzxsRHvot59SFLbiOVo8CgPmnrCBB4dYvBikuLT5fKiDWGs3XyLHuWUHg1-Kb_kpTUoyVjPjZRg0b_rrCR3aN7mmelUf_3oDQDfv7iJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27039" target="_blank">📅 10:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27037">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgQ3oq-ciASjSe7roGitlJkh-cZngfvuRldcQZYXx6nCJ89YO2dMH5bs47_8hkNAyvwoImc48_6eE3b_9b_DPtfPPvx1XsY51LZajAdhfvAS6-JEzjbi6JGMmT1MxkBlJ9NDlrYGjYr56k_Hp8G9Oqw7Z3QyHoAzlthisK6KUrjjJ2XXsl_Oy2QMy9jf_HLTkF49x-kSJ_tEQPX3F1xaeBcqUYhFSYnuduRmVkptP1CmXAFjFB7bb3aVtf0YzswZqnE3VXT9mYTc-sHZsz_nUCRfzwA2VGI52USGadCRQvHFnilu1Zz_XeS13ZZ3AB49BOyLNOayMSBD01LEI4jdrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هانده ارچل بازیگر معروف ترکیه‌ای که گفته درفصل‌جدید رقابت‌ها طرفدار منچستریونایتده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27037" target="_blank">📅 10:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27036">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdiQlDEWUveBv6GXBG0mXOdMM1nzNe7Ij76CXO8impaOVtZA3_f0b9nblx0IPoWcgQoel8nhCaoiwYg8jpIPpospfoeVeZU81VH83RiW5tf2A4OWu3FS1JuFlng8BbjUVw_RRyJLGgVw5UZuU1ff4ESMcsKjwakNsLe1_hCY9Rv4RRzKQGjO3pWKSp1I9_iMAMTWIReRESU13Y3pREK0Lc0UNypVbpw7YSjgWitJn8cD-G1OiKscRr37Ffcsl6ESyCks36RGbbc8vQdDSY9dL33OscmbU63mmEmI3w7pf1o75_9OZd2-qvms7Q0X5Bs2UqQxulX3PZOIHldZIwI-bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27036" target="_blank">📅 09:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27035">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hL6yibbBkosMIrCZBzkKI4CtIZVxeG9t60k32Cth4V3UGWm9FA3ZEi_WDDacAnftKMYSqSkjITjDT9StVdMRWn96zhJcMba_sXW9_j7tTR4RVWOHnUAm29GB64n5JWKAYN2TVE-L-Aba1KH_zenKqF4X-CgwomQsvNJlIFlTn9t-VlmaB3CXSKjwTC2IvCojjWXG9mZhJoL6wyN50bJXotuqNu0FwTZuK5ellOyBEsnmPDK2CbkNVosCkaNECcygnc5id-qw_YG43vdGnvKYkumCHAETP_amQbYitqADP3yVxKQLh-_Y-hZyvnBeah1UJ_xTrlFishMqb0D8o73Fcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27035" target="_blank">📅 09:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27034">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f85ecaf4a.mp4?token=lSPbwXdl5Pa7qVZH1COwgKgO-AZcTl61cYaT8nGwO_muAQwlSmGNfCKa081y-A_kBO0sfZL70QdZXahh_QYUuaOu_HhQH2UyFdpzkAr0VcAOIQTZAcl3ibp9HIZchZRO_zE98MU0TiHfzVHmQJWo-vaEo7PrJKaVitgbPBLBz_KE7S3EBMQqSLdBG5dXcv1wUNQVaKgFDFU_NcHmbcXh77czp7gxhT5ocvsHEg4-NlxQuBNzOGmtLz4CIse4o_nrszJWezgvt1CGseApazPB_deQ4PAO-ZEX5dD9eLznO2EaIkyyMFbWex3BnmYbQNT11r1K6ujUYSCpAtO3Nytvtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f85ecaf4a.mp4?token=lSPbwXdl5Pa7qVZH1COwgKgO-AZcTl61cYaT8nGwO_muAQwlSmGNfCKa081y-A_kBO0sfZL70QdZXahh_QYUuaOu_HhQH2UyFdpzkAr0VcAOIQTZAcl3ibp9HIZchZRO_zE98MU0TiHfzVHmQJWo-vaEo7PrJKaVitgbPBLBz_KE7S3EBMQqSLdBG5dXcv1wUNQVaKgFDFU_NcHmbcXh77czp7gxhT5ocvsHEg4-NlxQuBNzOGmtLz4CIse4o_nrszJWezgvt1CGseApazPB_deQ4PAO-ZEX5dD9eLznO2EaIkyyMFbWex3BnmYbQNT11r1K6ujUYSCpAtO3Nytvtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27034" target="_blank">📅 09:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27033">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/371eeda394.mp4?token=UYu7FOcDiCk5unoSNLVXGnjP5Yc2EkJu6k5drN_jfiktwwkRGe93g92AcWof-oB4hHH8TUCJtUmkwlnTTvFH6abNW5inORXVUP6lK6hjqO0NpgRPpzLL6mIrPw7ACBSHj3D-UA7P0s4Ktl9T_2poD8zMTOIhhqjk_rb2L05hVO6QS8DddCRN3bde2H-y7xrlfgNB0vfGX0KkQZrykzLDaJ14IEpMFS4k2fGrGytvjuTZdSiTG940duL4RZtuSGVx-cUk-pWz4TEdQ1I4bpfEsrtB5SIQ8T2NncwNhWDGJ72GKhShoy1hFJ_eOcK5KchqCsb995-phw9jFzDD-Fzpzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/371eeda394.mp4?token=UYu7FOcDiCk5unoSNLVXGnjP5Yc2EkJu6k5drN_jfiktwwkRGe93g92AcWof-oB4hHH8TUCJtUmkwlnTTvFH6abNW5inORXVUP6lK6hjqO0NpgRPpzLL6mIrPw7ACBSHj3D-UA7P0s4Ktl9T_2poD8zMTOIhhqjk_rb2L05hVO6QS8DddCRN3bde2H-y7xrlfgNB0vfGX0KkQZrykzLDaJ14IEpMFS4k2fGrGytvjuTZdSiTG940duL4RZtuSGVx-cUk-pWz4TEdQ1I4bpfEsrtB5SIQ8T2NncwNhWDGJ72GKhShoy1hFJ_eOcK5KchqCsb995-phw9jFzDD-Fzpzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
آرتور ویدال ستاره شیلیایی سابق یوونتوس یکی ازبهترین‌ پنالتی‌ زن‌های تاریخ. ببینید چجوری میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27033" target="_blank">📅 09:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27032">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiLvWGaQ4CIhKi9OyRItd6_eqLdoTQ1XSsb0DDQvkA7J98af2_uBBdZ_vjdzgyRWxPSWnL_BSRSdXYjljAmJegZeHiNPEkfH0fsaCFhrtRbYLfLa0x2041o0Z36dDV2r1z_RnH1rTiEQBG7dE-8tjL_MafHYWXsnPeOsZJDX6tfh46ghcyBKT_nQAg5KCRhGuEDAnEfHOApJ56IHzRAJ_klTsMxZrSlqbJ82bubHOt9k3WvcmSiaNa6eFcXMvNF5pInEk4Xg8tsoOUzcpqbdAWo-mvmlsZWJVV3izPxuOagGi8k9Q9P7DYlfpoFO7QY1VOROqUiwN0ToDVYYEiZLJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
درخشش‌ادامه‌دار سوارز در میامی و شکست عجیب شاگردان ایرائولا مقابل لیدز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27032" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27031">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e2aeddb1.mp4?token=XnSmb6JPGV2McFW1CObPAg60lVO4H3aV5W5t-ekk8OGenOYHCISSQvm1nVqyj3_vzkfXZzgnRxia9qx59InKiyMuL8KCYt4v5fVHNh5yxjNJQ7B9J5UEWkYXbhhsPl3lNG85IiPh36pPdw_c5RHQq-vgTEobztypgahnVBrO2-SFOMqMaCI5bfKIYG7V7kQH-ECHIpY678aMeQNapAWOqGNgj59eOI52vTz6VjUeSdpEQgA__zZO9njSxD3Umm06uL28wUpvIgqHY3uRW6f7OLbkNxpJJFVz8ZvQBqSLFxwo7YWrRk5gLkysANGvvah3qox_YADPtT7zV9wEutBoqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e2aeddb1.mp4?token=XnSmb6JPGV2McFW1CObPAg60lVO4H3aV5W5t-ekk8OGenOYHCISSQvm1nVqyj3_vzkfXZzgnRxia9qx59InKiyMuL8KCYt4v5fVHNh5yxjNJQ7B9J5UEWkYXbhhsPl3lNG85IiPh36pPdw_c5RHQq-vgTEobztypgahnVBrO2-SFOMqMaCI5bfKIYG7V7kQH-ECHIpY678aMeQNapAWOqGNgj59eOI52vTz6VjUeSdpEQgA__zZO9njSxD3Umm06uL28wUpvIgqHY3uRW6f7OLbkNxpJJFVz8ZvQBqSLFxwo7YWrRk5gLkysANGvvah3qox_YADPtT7zV9wEutBoqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛ با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/27031" target="_blank">📅 01:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27030">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enCYCM3IBu4qJIIzYZcNQVp1gwM-HrtlR7Jibc9EDikKUT-gSb7cttV4Xt_1oI7n6xuohHNAdgG9bZQuP4nX-afYknVtwfO66G7x6fnyreDcF664ai3JWKVTMM5XYCDsJiolfN7MqTDKoEPLxl2zJenVvn1VMySpPBCn02RG9gaNLTFbTnTQ6f2sjaoEQP-BRJHwKpvLS5M-a1ceVd9RGgT9yNEhgJ7kiPxbSFbTbbPI_H0ZSuQht76yODBDc7JZ-C21m2cm1Has_J7egKhtHV1sI8pKJuRY0bann8X3HXORz4IPMjPa2UQV_fpJbztiGAdtD_XwhtC1tC-xkCVV8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
آمادگی فوق‌العاده لوئیز سوارز در 39 سالگی؛ تو بازی بامدادامروز اینترمیامی‌این‌گل خوشگل رو بثمر رسوند. کاسمیرو هم‌که‌گفته‌بود اومدن‌اینترمیامی که به مسی برای بردن جام‌های بیشتر کمک کنم تو اولین بازی اش برای این تیم در دقیقه 34 گل بخودی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/27030" target="_blank">📅 01:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27029">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCd-V7V5Kpe74NEwCrPq0_3S6PDCmpa_sgZ26X489ubuLfMOWfXGhwHrHmVXKk4FiB5Pn_ueY66P69BFs3vaoTJcZt9G_LtyvZZFy0GX2tbvqRxShg6JW2AX01hHHyFzSLXPB8l3DmtZOz_34omigtY0a60oGJUkwdThmuFjyG0l1o7DTIGz3Z1B2IlQIJpuJyKOK42qipy_7-j-TBKdHiGEXJu8ghfqfVIK1-_2soj9fY5phpj_MOXCN1OcTI0RHsHB8M3g9T1BiJwurN5xv3bySuvmTkmAyKRD6iVVtfHL-mIsJRXYbB14RTP9g1OtYoAk5Gd1qkmvfQpeRfsQTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطورهفته‌پیش‌ازتغییرات مدیریتی باشگاه استقلال خبر  دادیم و امروزهمه رسانه‌ها این خبر رو پوشش دادند. حالاطبق اخبار دریافتی رسانه پرشیانا؛ مالکان باشگاه پرسپولیس درپایان‌نقل‌وانتقالات قصد دارند تغییراتی در مدیریت سرخپوشان ایجاد کنند.
🔴
طبق‌شنیده‌های‌مو…</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/27029" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27028">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnySH50IXwIRCcXKmyav4XREZO9jYbCKca71vztV23-ifxifXVzw0pJTZuBlznsr4Wk3bNLmH1N4yA354AverqDImUlmn_oFnYz6q6rIA5ZVartPgs9k3nN9hAgxVq5GkoAQnU2yR0jCUUxwf8hLVM7JB7l8avItd9sDrIK_3BWNnqUkgeSnLMwEKKnsC7J1J4Y4oPLtAGJuG0f0yrUYkdEBFUtvyIM0gsM3Q454PDMp_2MGEiwvrQx-TaPPWivMcliRDAUJsvyT0TAzcirS1UOyhF1V1vQb7Cky1qzwIoKkzdyvgcFPWPqOC1PB0ny9t3RDyxaimT7a2A3EofA8mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/27028" target="_blank">📅 00:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27026">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiJRHdnhBl4xKi-lOPq6Mth1-xFg2pff3oQ3IPLS3tLCTBipkoxy-qTVYGx8nqVqQMAc4uyJEYI31-o9gYagwrN3UEqENrThwvTTf8tBn3N0FiG10jmVh_4bivKKZdt_F8RL1GGTds5KvF2LU7o0Fta9s4kxt0ZgGtgcXXm0yXysxYcz8m8a_d5MpuZonBwVX-M6GhGQ6gwVehVGok93EiRDlbV5BnG8I_YzGRMsxckniydkOdFXBLrhLnzZwkAuY5uZJmNLiRO3UTJtOrrOSSJT1E6uvCbRyyNerWIdaP5HBqrfzmh9TudnvsL4YkQo8x66RjRde1hPKbypLI2W5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شروع‌رویایی‌پرسپولیس‌ِ تارتار در پیش فصل؛ پنج مسابقه، پنج‌پیروزی، پنج کلین‌شیت؛ امروز هم باشش گل تیم ترکیه‌ای ارزروم رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/27026" target="_blank">📅 00:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27025">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewracpY52nLtmx9z-wQ7dDcD0CG4OWJJn75fYC7fDVExkYCN8NL_-Ie5-du-hajjzbSv5H_nFuPxxoikvq4x6ZpusGMUpfQI2s9f725jJzK2-3dE8wF8KfNHrgJmw-Wey_XP_GUhGhfoenI6Adi76uGY-ny7xLu9qJyZAohg-ZSU1KVOSbdhfUYisTrAdAL6uhc3sMakYIvWzy5-YKy6ZvB-Isk6xZ13okWu4TnuRpOX7lSJ3H8u09dPrRc2j9-W0VVVcnZjvzg3gGa5EvOlsEIWrY0WrIaijNMOjLjy3GZpqmRbXlMdW-dIWNXev5PauS1gvo9Pw1NQo7-3uEt3Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
الهلال برای جذب رایان، استعداد ۱۹ ساله برزیلی باشگاه بورنموث و تیم‌ملی‌برزیل آماده آغاز مذاکرات شده و این انتقال را بعنوان جانشین احتمالی مالکوم دنبال‌میکند. رایان جوان یکی‌از استعدادهای آینده‌دار فوتبال برزیل به شمار میرود و درسال ۲۰۲۶ باانتقالی به ارزش ۳۵ میلیون یورو راهی تیم بورنموث شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/27025" target="_blank">📅 23:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27024">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XArdQ_udHxbmRUZ3vlJvlKRR-NvRjPW63f0PzoF6zh_3gv9qXAAjTDSdQIan-ZcT9UM1_NLIl7H9P81mOdBMJcyAD1qd0geTRXv4Mc7ZwEcHqraBn_mXFkjncSj5OCWuFI5LZTo7mHWqMZcD1ofADoX3Om8MnafFk0dz6i7hTSl2lS6bvPzdAVVIYlMZZVJC9qvMANND3fLPLEEAr5tw-EsNsX7Fu_L3QOYrAz7Q0V8exGaoOVPqO_06JqqBwhjX1g0FlOHIPBmzgZszt_Jq9QpAM3E7wMmO76ayB0lO2vc8k4nMuBfFGF2niM1fwXwr--bvGGnQ8ddsRIc6itlmBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ پیمان‌حدادی‌مدیرعامل‌پرسپولیس فردا بامدیریت باشگاه فولاد خوزستان جلسه خواهد داشت تا آخرین تلاش‌های خود را برای متقاعد کردن فولادی‌ها برای‌فروش ابوالفضل رزاق پور ستاره چپ پای این تیم به کار ببرد. گزینه دوم امیر جعفریه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/27024" target="_blank">📅 23:03 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
