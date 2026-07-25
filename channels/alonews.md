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
<img src="https://cdn4.telesco.pe/file/iAxVfNDfbUhAPEbjiIMNtdLkwvqpQHsCe0S8vEat5uo-iijOSsuWHSiq4GvpfneEbRlmUFO7yGEftEiNAO_iR2XgfkdYB9ZPThUSwqJCEVLY4h0tXkvca3AuUU6J9hzoWvrayX6hDOZeeoilcw31Tw7I_m4h9k0FIJ8nGOZOdZFOjDaRv6QsdaW_ClIl_cBpinRveKR5B09GvVcGSIDljUzHuGwdGOQL-VSkwL5d-ilgxI3FgaAf-yVYQgLmynJySXAk6pAygGxPLEFHUqtJcWoyCCkAmBaKKvxU9CL0RILHTv8vowh2fo-XsHUcEMFF3x2vq84yxCI4ZbJZEdb3KA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 937K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 23:36:33</div>
<hr>

<div class="tg-post" id="msg-137576">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxCJKKbwRKQ5ivGWPAbJ0t5D15cBmUGqTtU_LY42yQlrUB0KRlHEG4rNfBoPkszW38ttYvc4oH2MKiD2H5zf3xPEHWvlM4gVAfKUZt_LnELhMfVU4oIuVUBwLNFopYmvGCxEvHd5PyXWIv53BjoVvAo88hW8xsGQ1wps_aItGThustvZh37i1YjwpznRC2zVw3lnGDyxkLOHTbWE9xXUXeYdm-vBbJBvg3tv_jl-oGwKs7eppih2ykSSHr6T5t7ci_fOzhlU6xu-E2aJWC3q9aRtjunIplkarObrKV4DOHnjjohze0v6ZX2mtPvu9R3INqNhfuMfQQ4IAtKJ6I6wdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف:  حملات ایران به اهداف آمریکایی در منطقه، تا زمان تسلیم کامل دشمن و به عنوان انتقام خون کودکان بی‌گناه در میناب، لامرد و سایر مناطق، ادامه خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/alonews/137576" target="_blank">📅 23:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137575">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اینجوری که قیمت تتر هم داره نشون میده، تا یه حدی دوباره به یه تفاهم نصفه و نیمه رسیدن!  ولی صداشون در نمیاد…
✔️
@mahaneconomy</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/137575" target="_blank">📅 23:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137574">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
رسانه های عبری: کابینه امنیت ملی اسرائیل، فردا تشکیل جلسه میده
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/137574" target="_blank">📅 23:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137573">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
فوری / شبکه ۱۲ اسرائیل: نتانیاهو قصد دارد در جریان دیداری در کاخ سفید، اطلاعاتی را در خصوص احیای فعالیت‌های هسته‌ای ایران به ترامپ ارائه دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/137573" target="_blank">📅 23:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137572">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4RiTD5hkb7oIT_1E8rzDmz_aWnmAnbir3Tl5U4XbZmTM6uk2PuHNWE--wis9U5s_2nmdQD2Q-zhyYO3fZ0whfjuL07OILLwJOc0zTrx62fCnMcyNFxAibM0LrP3nlzl2YYkXYRCejuAMaAP-WOuoL4mlngaDjISzewmERde3lRHctsnxETtJFUmyUhn30CRHBtcZj2gxa3WqSa-i-aLjzn7rrzEuO7SJOIR4EjIOeBOLj1YTMBK081JNOp6Xuhawjya5GBkKY4UL1rRSrqMkvhGpEmZTiZtg_Xe85Fn1xwQZwVpWKn2szxjcBZW-1vxOy6CZ74qKF_zSSs-UmnbAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زلنسکی مدعی شد: روسیه به ایران در تصاویر و دیتای ماهواره‌ای کمک می‌کند!
🔴
رئیس جمهور اوکراین: از ابتدای ماه جولای، ما نظارت ماهواره‌ای فعال روسیه بر کشورهای حوزهٔ خلیج فارس و تأسیسات نظامی آمریکا مستقر در آنجا را ثبت کرده‌ایم. این تصاویر متعاقباً در ایران ظاهر می‌شوند. همزمان، همبستگی آشکاری بین تصاویر ماهواره‌ای روسیه از این مکان‌ها و حملات ایران وجود دارد – هم پیش از حملات، در مرحلهٔ آماده‌سازی، و هم پس از آن، برای ارزیابی خسارت واردشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/137572" target="_blank">📅 23:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137571">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-k4W4vydaLoz7E8uUSdVzCaRjgraDkSR3gzTVKiLMHOU1Ma7rKLu48D7pO7tNtPexzp_DZC5KReh2O3n5xYncNPamQK4Bh4xMiW0qHOmLCD6Zus5quSeW8l-jwbNBPhJ_wclt_SYT7K70Xn2TTiOj5jrU39wZJwH2vg-epQpvZEH6B-BcBbfzjvoDyr33rUDRHiz6I-0e34s4hIv4b-KcGBG3VAg1RW1pR0U0pIyWiUz2leUjNB7C65RJF2IxIM_Nuwq0fHqlipEQjKdBhVkAmSKNTvMN15e0M8PATipspPPMXxlo6v1E0fx56xaA5HYA_HUKLAKKOiXYZTdCQo6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل:
یک پهپاد در نزدیکی خانه بن گویر در هبرون سقوط کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/137571" target="_blank">📅 23:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137570">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
سخنگوی ارتش: بخشی از پدافند که آسیب دیده بود را بازسازی کردیم؛ همچنین تجهیزات جدید وارد کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/alonews/137570" target="_blank">📅 23:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137569">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ادامه آزار و اذیت ماهیگیران ایرانی توسط نیروهای دریایی کویت به مدت چند روز متوالی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/137569" target="_blank">📅 23:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137568">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
پیت هگست، وزیر دفاع ایالات متحده، به MTV گفت: ایالات متحده در روزهای آینده حمایت خود را از ارتش لبنان افزایش خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/137568" target="_blank">📅 23:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137567">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBIr_lQ_BphHMQxLxlU4S36XmcNNNsima-nE_fkNJw_aQDKgWxPSMyLfLYAn0G9_dKu8Bvmhgqi8IMMrX4lU22Sgv2tXSOr7NH1WTZOo6xaVL_MQ5eZESnpkopUPDp10lBUZWKd-pKjpvnXMh9bRGaJOAyyJHbAjIvJJkSxHCMF4gdsqo1IaWPsak6YJ0peYEPaa7zrTmPrgqRvKvbze5oE9tuVr_GkXgwDNhSz9v_pWOkJaCluuRK6CrYr4lMixrWq-hlMTPPhOmK-7ywnxcoRxfE2yAg7eEd73unedhrNBH7HpHAgsS7ZRZIIzCTEIja8G4TgHSFOxfjzp0FN3rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
تماشا برای زیر 18سال ممنوع
‼️
❌
ویدیویی منتشر شده از سواستفاده جنسی از کودکان در جزیره
اپستین
!
🚨
مشاهده برای افراد زیر ۱۸سال و افراد دارای مشکلات قلبی ممنوع است
◀️
مشاهده فوری فیلم</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/137567" target="_blank">📅 23:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137566">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8N6WT5bSfN2zuEkJl7uqpCb3TPQgsmQPW5eE4SBLmaRhoxtfKG0bzJz2nM3x-oI8RFxMTriMR5crV0Tq_WLbVSmwCNAq38vnmagRrTp0weFeEqzxENS8tPblrioXVvO9RSs9dWFE4dJIhHY6mBdUp-TKH1MIbARSV1ZPLaQtyyfjuNSDZkfI4B_lc_4f6ap-jV4qWmXPdJYSzmYhuPhJyz0cKY22-_k1dkyURMAoxyhR7CaZC2vBqbvr1xkGpzNiP0X8kFbXg0C1hT7Wvxm5U3pi3JZN0VsE-TfR6h7HGy_nK6SyKfi7ytsMkc63V-ZNhsZABj9fvOBnPqWcx34uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهریاری، گوینده جمله تنگه ارث مامان ثابتی:
اونایی که شب‌ها تو خیابون ول هستن، شعارهای
کصشعر
و متوهمانه میدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/137566" target="_blank">📅 22:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137565">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل:
نتانیاهو قصد دارد در جریان دیداری در کاخ سفید، اطلاعاتی را در خصوص احیای فعالیت‌های هسته‌ای ایران به ترامپ ارائه دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/137565" target="_blank">📅 22:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137564">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/137564" target="_blank">📅 22:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137563">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/137563" target="_blank">📅 22:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137562">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIU1C4EHsnAOqnbdnKL8F3LyC7-CJyzGEK2A2e8afdCe7trSyCga7E0MQUmvJIhxEZTBUS0QBEGZYRNS65xBd3GFn_VRu_ogPs_BIxrbA0gHV3P7QABgIZWscUfNvcIvmoPILTRHlomVYsl5G4BunuDgmoDHBTjmgzIbUp5wqzHpht7QZrNzdMO4hpwt1Wx42iFX1wK-YLshUNMrjHcG6koSi-8Im9O64_6dmEDnuZ2qSVZyJ5YZXQa5ycnFe4hLYUFkJErAhtPw-ZtptQHH9cCCGBB_Wq-w2-uvq5mOa_XdwP9_4tpuFTrj9XDIfoTytFmf72Z6JEMu-9oDF8R6QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
وزارت خارجه:
حمله اوکراین به یک کشتی تجاری ایران در دریای خزر که منجر به شهادت یک ملوان و زخمی شدن یک ملوان دیگر شد را به شدت محکوم می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/137562" target="_blank">📅 22:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137561">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzeUPMyP6kXQYnKtGwFZli7vq42HIuje8H-egxDTRlneRKzT8dokvrnUODi82jKhPH8huxVmOX9cH8nHo77wpOErtlT7Dj1SWBFf_PaoKXmcOz_ruMpIkuL55e0SWAf63T4MYcWo-SZP-WvEAs4lAVwdwCjOmGmAZpd2NY7goWNtXD6ExSkRhDQCgD8z2lAsis4PABw51J0VWsiA94BbglXsuJyO4G8x9SU92JLas73BdjteB094FlUr_40b4klLkYjbehM5Mt-tahhhYHl1DOvnSknZ17Um4ZXXF58Pt2G4eBstaX2n_0sXly5rfffKL20beSRPYREUIg2dMzsXgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دقت کردید از وقتی سوریه دست جولانی افتاده دیگه کسی نگران حرم نیست و امنیت دمشق رفته بالا و زائر هم اونجا بیشتر شده؟
🔴
پ.ن:قبلا میگفتن دار و دسته جولانی میخواد اونجا رو منفجر کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/137561" target="_blank">📅 22:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137560">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سخنگوی ارتش: تمام پایگاه‌های آمریکا در اربیل عراق نابود شده است
🔴
‏دیگر توان عملیات نظامی از پایگاه‌های اربیل وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/137560" target="_blank">📅 22:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137559">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzezwKAFoS7bm-AWDhhBwUgKXfSV76kMr9e1J4AusYmCDrCOOtbsIhltP47U4VsYIIjWbPzCjp6ykbXU7TNeX0lVsfwPumc9Xp_st7cpJSTSAIr7q_CfEhmf40ecaoRMEkxkSyX117vT0RBr9TSbaEESzArrsp7eBJLATPt4mVRwU0EO4l5mavYZZ-et52uG8cz2EAOLOcN43L-YF35_QcDbLHZHm5vLxbvAOQBDt9dRWoUF7aufI4MArTXshyqs6G7eAWYvVzsgOP2JJpZJHizjeiQkyuK62q8akuSyGYe3SvWRJbUOM93SO8TFnx7t5WFDV8l0LNVjoJ1aMY4V3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاهش محسوس در ارسال ترابری‌ها به منطقه؛ به نظر می‌رسد هر چیزی که باید به منطقه منتقل می‌شد، شد
🔴
بیش از ۲۴ ساعت از آخرین شلیک آمریکا می‌گذرد و گام بعدی مشخص نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/137559" target="_blank">📅 22:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137558">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45fbc06d1c.mp4?token=XpKmUtr5Dl0hHS37Bp2Pnd6B9rFpMODFt957k-UWL7HhJNqTCqfv5jsiRlsQhLJqhfWIMYqcwroqJ5zeEW12HwsGkOX9AwGWK7Xcxf4-hpogdZ8V-tgWnkYEq7mJAjE9RokONNs8LktHbU_ymLcrvbM7dZk2RLSjm5jOVZujia-FOcXfg7bKIE7KxOUAqYXOmiLFbwwxLv_vT8E_q_q6XxYRNsgE8p1FDK0-UQGPzEiwd0lI909WVbDd1PPzZ7Mi0hYmDKo0DakKDHwRJHr0RStj9veMjMFofDuZBUELOTp1dxYPQbL5_6AuIJZ-BZKaNXxh32XAUkyXf4PbbkE6Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45fbc06d1c.mp4?token=XpKmUtr5Dl0hHS37Bp2Pnd6B9rFpMODFt957k-UWL7HhJNqTCqfv5jsiRlsQhLJqhfWIMYqcwroqJ5zeEW12HwsGkOX9AwGWK7Xcxf4-hpogdZ8V-tgWnkYEq7mJAjE9RokONNs8LktHbU_ymLcrvbM7dZk2RLSjm5jOVZujia-FOcXfg7bKIE7KxOUAqYXOmiLFbwwxLv_vT8E_q_q6XxYRNsgE8p1FDK0-UQGPzEiwd0lI909WVbDd1PPzZ7Mi0hYmDKo0DakKDHwRJHr0RStj9veMjMFofDuZBUELOTp1dxYPQbL5_6AuIJZ-BZKaNXxh32XAUkyXf4PbbkE6Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
‏مجری صداوسیما میگه موساد بچه هامون رو در دی‌ماه کشته بعد احمد قدیری کارشناس میگه در دی‌ماه در یک اقدام انقلابی گفتیم کف خیابان بکشید چون دستگیری و دادگاهی و اعدام دنگ و فنگ داره و مجامع بین‌المللی هم گیر میدن! همونجا کف خیابون برای حفظ« پرستیژ» بزنید بکشید و خلاص...!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/137558" target="_blank">📅 22:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137557">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">📱
لطفا توییتر الونیوز رو دنبال کنین
🔴
پست های انگلیسی در رابطه با جنایت های حکومت به انگلیسی نوشته شده و افراد مهم منشن و هشتگ های مهم قرار داده شده.
🔴
ریپست کنین. مهمترین کمک این روزها جلوگیری از پروپاگاندا حکومت علیه این قتل عام مردم هستش. خونشون نباید پایمال…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/137557" target="_blank">📅 22:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137556">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IR05YcAzkVQlyHOuC-i-m5vqOi3NpfeaDM9b62jv1_RRabE8612ygQ1tSg2wm5LGDTXvgr1EIvz9C4MTXALKObrq4blTZhpVzDgsertXEyZXqqbx4V27frZlQHhQ4KeXDdFV0rjPLDOBBu11eNodnFyEO1bCouVIGA3qQhQUdvqb3xQMfBN7fyt3CwkkUvZEuLtIYpFLw1KCdSRGia0npTgKccCZTBWqIQOmWK5xJv79b4rt1_8m-jJrYZ03Mys7HjXu4bsB3y2pxJeN9aFfQg05hf_CABReuFd4Lkx8xunoEbZkY_3K9NXIjnQu94ni465N0LrrJmzGakGfzL3oLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ژیلا صادقی: شیر تو آمریکا لیتری ۶۰۰ هزارتومنه ولی تو ایران خیلی ارزون تره
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/137556" target="_blank">📅 22:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137555">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/137555" target="_blank">📅 22:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137554">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db14df2e2d.mp4?token=vnGqq12YgQoFBnPpugP29o0akisERkMYHp98rfz1iTwRp9A9fsOspKJYoUWeSMR8Tdj1I0c4Uc8YQGwrXZ-TbcTbyBXcgZw5ApkUFYi1led_9Wb3aI34ZT9nx0oMb_lToA8-unMCs9WyaHwxT1CHoBg1yfYWzcu4YXdSerlHNsuixisLwu51eHZue20kM89Xq79KVBlt19_QX5qQY18kz8EMfAOwmrznYlicLvpQuKGAkSHC-t7qnm2opQeR5_-rxcFVBcpojhwnAMt8IotC-MRmToqghZHisq7wyefZw0iX2w8XdwhpwUnPB4fb-WFu4QTXEQvhryLyHOWjn2XBMZnygXA8nzSLDMNETQ6qPFinIWl2b45yexYcDR33SIq-7LV8w91zi8N1p37GNcX620q58PFw_btjxASFHarLpkCeMxdFP6HOR2FLT7ojHfilTS9elw_wKr-oqSNxypeQBYSvrilitLelI20RadiC865LQLNb_ccn9sSL8Ucfkl_mVmkTwzfz2mCIejWGLtE0riyzhWCkujkgxPla5avH6e0VnSFD_boxGT1yysfm9ar4lgGzdGB7Phi50jE1nN6_xQ7hUhemwl89gGGLQnmDLRh12V7IzYZJ-8P-IXo1DMSlOBd8SRfw4XN6LM8ONfujKmi9WnR0knUepQlgkw9ZjrY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db14df2e2d.mp4?token=vnGqq12YgQoFBnPpugP29o0akisERkMYHp98rfz1iTwRp9A9fsOspKJYoUWeSMR8Tdj1I0c4Uc8YQGwrXZ-TbcTbyBXcgZw5ApkUFYi1led_9Wb3aI34ZT9nx0oMb_lToA8-unMCs9WyaHwxT1CHoBg1yfYWzcu4YXdSerlHNsuixisLwu51eHZue20kM89Xq79KVBlt19_QX5qQY18kz8EMfAOwmrznYlicLvpQuKGAkSHC-t7qnm2opQeR5_-rxcFVBcpojhwnAMt8IotC-MRmToqghZHisq7wyefZw0iX2w8XdwhpwUnPB4fb-WFu4QTXEQvhryLyHOWjn2XBMZnygXA8nzSLDMNETQ6qPFinIWl2b45yexYcDR33SIq-7LV8w91zi8N1p37GNcX620q58PFw_btjxASFHarLpkCeMxdFP6HOR2FLT7ojHfilTS9elw_wKr-oqSNxypeQBYSvrilitLelI20RadiC865LQLNb_ccn9sSL8Ucfkl_mVmkTwzfz2mCIejWGLtE0riyzhWCkujkgxPla5avH6e0VnSFD_boxGT1yysfm9ar4lgGzdGB7Phi50jE1nN6_xQ7hUhemwl89gGGLQnmDLRh12V7IzYZJ-8P-IXo1DMSlOBd8SRfw4XN6LM8ONfujKmi9WnR0knUepQlgkw9ZjrY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایلان ماسک: در سیاست زیاده‌روی کردم!
🔴
بهتر بود به جای دخالت در امور اجرایی واشنگتن، تمام تمرکز خودم را روی مدیریت شرکت‌هایم می‌گذاشتم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/137554" target="_blank">📅 22:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137553">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وای‌نت: قطر و عمان تهران را تحت فشار گذاشتند تا سازش کند و از یک عملیات تقریبا قطعی و بزرگ آمریکا جلوگیری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/137553" target="_blank">📅 21:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137552">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ترامپ در گفتگوی تلفنی با شبکه فرانسوی «ال‌سی‌آی» (LCI) اظهار داشت که اگر «صددرصدِ آنچه را می‌خواهیم به دست نیاوریم»، «قطعاً» گزینه ازسرگیری جنگ تمام‌عیار علیه ایران را مد نظر دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/137552" target="_blank">📅 21:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137551">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vohlvh_cj8t_s9laa9W00N_yd7qPDW9BCvBXV6iqVSjZfoVfvNA6dalY-MwrOpzh5oQ8l94EVipSrDhMyFQSD4Hd58KuxBU9B-jzGiyxePs_gDWjBFufncsl-8rczsKZPZ9fKNxE4uLCDIze_iEv_Qv1lE8gHX_fSQR-Di7pvxcAmj6AoaDFBn0d7WOVWfsuGlNtmSYwtaZoBeij2WpDFejNHms4hx_gzgPPFhjwv6ZRlVpOu-fw7DGGfb88GmpZgOt-Yhj9NQkXSnCEHZ4PijraSfZv2zEg6-ZBHAsOuyGBikTxn-uTCVoBtqbYezna5X308iKsJCWtFaVf9ZIqDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای آواکس E-3G Sentry متعلق به نیروی هوایی ایالات متحده در آسمان منطقه به پرواز درآمد.
🔴
این هواپیما شب گذشته حضور نداشت، اما امشب دوباره در آسمان درحال پرواز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/137551" target="_blank">📅 21:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137550">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmuZ2h_ysEGyEyKzg5o2q144qt7KaIoiECuVlNXxWhu9No6Lg-B2yfhUkmSi7I9di-iN-bkuercov9r0yfuWtnGlXaxCo79fmJALHSulWqeUwfLB92_JDqf8QBEWwiRmHP0-_sWrv71uzTOMhT9yVzuPN1ctC6bQ8SEvQE9N5ew6gql6JTr3D8fh852Bz1e6hdYqGHpwMuFmGzbe8SFcCil2MQyYmvq5nT93r7JibnovfQyPJVXypE7J5mttm8oEukHl5fCubpSSPzWyjVMPtA5ZSzQ5pmbig5D6YkgHFmJgI9T8jFHDuVlG2f4J94I2APqnLJsgVk9SCJSfjKS8ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به نظر میرسه عملیات پل هوایی آمریکا به پایان رسیده؛ درحال حاضر فقط 4 فروند C-17A در حال پرواز هستن. هر چیزی که باید به منطقه منتقل میشد، منتقل شده حالا بعد از حدود 18 ساعت بدون حتی یک شلیک، مشخص نیست گام بعدی چه خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/137550" target="_blank">📅 21:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137549">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
منابع وابسته به سپاه : کل خاک اوکراین در دسترس موشک‌های بالستیک ایران قرار داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/137549" target="_blank">📅 21:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137548">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7f5eac88.mp4?token=OOl0AxjHPvf4PToLoNocUQCYpcBqHnzAE0_7bOSEHATkVJuJZMAYcbZigd87y6eJp3kVPGGcfGZGrJ4kweWMSlOM_SFlZ2WtCVE3U3zksg43ovwTDm8daiZE__0O-aeLMYVuGp8qPu3UjV1SmsLH2nRTdOAviWoNpfhJ60Uoz4SpaKTqYrMLNc-vGn3RRuCmCOakavWrTfNve2pyj_ANpTcqHv4HLNWNVtWgeTbLexDmrlfE0SgOd8td5_fj1tOlvnJkjeWt003eYLQ1jvdzLhMhRDogodKaQML3uup7LUElA6CVZ1fPwuIQM4liM9pjtBcR3XvnZl29WjolPYCT0oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7f5eac88.mp4?token=OOl0AxjHPvf4PToLoNocUQCYpcBqHnzAE0_7bOSEHATkVJuJZMAYcbZigd87y6eJp3kVPGGcfGZGrJ4kweWMSlOM_SFlZ2WtCVE3U3zksg43ovwTDm8daiZE__0O-aeLMYVuGp8qPu3UjV1SmsLH2nRTdOAviWoNpfhJ60Uoz4SpaKTqYrMLNc-vGn3RRuCmCOakavWrTfNve2pyj_ANpTcqHv4HLNWNVtWgeTbLexDmrlfE0SgOd8td5_fj1tOlvnJkjeWt003eYLQ1jvdzLhMhRDogodKaQML3uup7LUElA6CVZ1fPwuIQM4liM9pjtBcR3XvnZl29WjolPYCT0oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بزالیل اسموتریچ، وزیر اقتصاد اسرائیل:
خداوند در دهه‌های گذشته، کارهای شگفت‌انگیز و معجزه‌های فراوانی برای ما انجام داده است.
🔴
پس از 2000 سال تبعید، آزار و رنج و سرگردانی، ما به سرزمین اسرائیل بازگشته‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/137548" target="_blank">📅 21:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137547">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae537cb11c.mp4?token=MLsuYai9aYgtThjzINMZwPXOo_cbX6vhEvSRAfd4dEuUNQTFs5V1xlQUMQ1QQjzhoBZNZltLjl5UdXVXD7jL8nVVRP_M38olt0tCQfgR5neC1m_dqgWgiKgr5oG8AIHCGFaXe-dXLIe5SaFodPm8DN2hD9IX--AcYj-h-pG1FKz1n82o6PwISIj_s8OVPwhXF42Z3JiLhXQ5X5MV3Pa86aTgomy3vbUg0gKy8si9GVErO26dQSzMxCiDYQqmEQ6GxsXNi6_lXx3VbhdH_HMjjyXAh-KIjltCtb-QMNlGYqjlpk1wlcOXKGyvcGEJDysVvzCrwHkcYTznlR1Vovod0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae537cb11c.mp4?token=MLsuYai9aYgtThjzINMZwPXOo_cbX6vhEvSRAfd4dEuUNQTFs5V1xlQUMQ1QQjzhoBZNZltLjl5UdXVXD7jL8nVVRP_M38olt0tCQfgR5neC1m_dqgWgiKgr5oG8AIHCGFaXe-dXLIe5SaFodPm8DN2hD9IX--AcYj-h-pG1FKz1n82o6PwISIj_s8OVPwhXF42Z3JiLhXQ5X5MV3Pa86aTgomy3vbUg0gKy8si9GVErO26dQSzMxCiDYQqmEQ6GxsXNi6_lXx3VbhdH_HMjjyXAh-KIjltCtb-QMNlGYqjlpk1wlcOXKGyvcGEJDysVvzCrwHkcYTznlR1Vovod0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بزائل اسموتریچ، وزیر مالیه اسرائیل:
درسته که محور تحت رهبری ایران تضعیف شده، اما احتمالاً یک محور سنی جدید شکل خواهد گرفت و ما باید با آن مقابله کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/137547" target="_blank">📅 21:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137546">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb3075e4fb.mp4?token=qYlm8AyVa9VeQU1aO-y0XZ2aGdP4cAA6-vTzeFOxqQ5iLlYA8do4tDRNyuALmw3rro6e-8EGaC4eCMUjwzWkukCtgOw0GZLv2Dn1WD5YkhQjWKdTjyAMGCnK6fROdcB3zVmE5Zl2sMuALpX0alUbHb2HvFb47FQcDLL4-gStSjdlHrG3TOcSo-GdcfwcRrTe6r4scOipbYPjgHjrGPvOimxRVR28-BipoFkNSzEPiQCBzWQMyKILkpWbT35BnPpEWTMd5opiBslpX3dkXlCj3AOlGa6_ol3sukXPfYeyH-0CNF-EeDImG9GXt0aDdKA9c6MWHNX98O_LWDYRGNrJxYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb3075e4fb.mp4?token=qYlm8AyVa9VeQU1aO-y0XZ2aGdP4cAA6-vTzeFOxqQ5iLlYA8do4tDRNyuALmw3rro6e-8EGaC4eCMUjwzWkukCtgOw0GZLv2Dn1WD5YkhQjWKdTjyAMGCnK6fROdcB3zVmE5Zl2sMuALpX0alUbHb2HvFb47FQcDLL4-gStSjdlHrG3TOcSo-GdcfwcRrTe6r4scOipbYPjgHjrGPvOimxRVR28-BipoFkNSzEPiQCBzWQMyKILkpWbT35BnPpEWTMd5opiBslpX3dkXlCj3AOlGa6_ol3sukXPfYeyH-0CNF-EeDImG9GXt0aDdKA9c6MWHNX98O_LWDYRGNrJxYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بزالیل اسموتریچ، وزیر اقتصاد اسرائیل:
رقابت جهانی در زمینه تسلیحات، فرصت بسیار بزرگی برای اقتصاد اسرائیل و صنایع دفاعی این کشور است. ما در این زمینه، پیشروهای جهانی هستیم.
🔴
حتی کشورهایی که از نظر سیاسی یا دیپلماتیک، تمایلی خاص به ما ندارند، باز هم در این حوزه به ما نیاز دارند.
🔴
ما شاهد حجم سفارش‌های بسیار زیادی برای شرکت‌های دفاعی اسرائیل هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/137546" target="_blank">📅 21:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137545">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
اکسیوس: به احتمال زیاد، مسقط و تهران امشب یا فردا به توافقی در مورد هرمز خواهند رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/137545" target="_blank">📅 21:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137544">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا اعلام کرد یک پرتابه به یک نفتکش در ۷۰ مایلی دریایی منطقه «الشقیق» در سواحل عربستان سعودی اصابت کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/137544" target="_blank">📅 21:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137543">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDZ7lZykvzN7mAi9BLJ2_5CLOu8MbE_HvBx9JX02H4lkETIIOK4w2RkPnAMuPXBymyVfpNEDx4GQuOzJ78p3k-aDa5uNNnWl5mL4pVSoIp9rMLr204bR2OZJ-UFsB6pyy6Rr2obUhot9bsdU1mqk4v3Fr7wVT3SJtqQvRPZqoqI12fQVD_pJy5ocdyiyat111x4t253hP2UaJeVNJ2s04hDB-bXCDaAEOmMSNIykEE9jIKwOe3mN4zPepf86bhn2-kwRZciVa_bmSZ8t1mY9rkzHN8gT8d5gGjtnH25Qll-chpwBW0lloFliiHUzQgR0meZZog48LerbNwetkBBJxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انتقاد کتی پری از کاخ سفید بخاطر استفاده از آهنگش در ویدئویی از حمله به ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/137543" target="_blank">📅 21:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137542">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سازمان رادیو و تلویزیون اسرائیل: در حال حاضر بیش از 90 هواپیمای سوخت رسان آمریکایی در اسرائیل مستقر شده اند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/137542" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137541">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
گزارش زلنسکی از برنامه های روسیه برای ادامه جنگ: پوتین در حال آماده‌سازی مقدمات برای یک بسیج گسترده‌تر است.
🔴
ما همچنین شاهد همکاری روسیه با کره شمالی هستیم. روسیه قصد دارد 30 هزار سرباز دیگر را از کره شمالی دریافت کند و آمادگی‌ها برای پذیرش آن‌ها از ماه ژوئن در منطقه وورونژ آغاز شده است.
🔴
کره شمالی نیز در حال آماده‌سازی برای انتقال سامانه‌های پرتاب جدید برای موشک‌های بالیستیک به روسیه است.
🔴
روسیه به کره شمالی کمک می‌کند تا نحوه جنگیدن را بیاموزد، سلاح‌های آن‌ها را بهبود می‌بخشد و به آن‌ها تجربه استفاده عملی از این سلاح‌ها را در دنیای واقعی می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/137541" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137540">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ad5f15cf.mp4?token=GcrzXgwWGGm7v2nAUZf09DXz1jOQKjeLIBuKGXYR-QGbUO3psimBox4PGNc3_mRNZw3qiHpSugz33rJ6R8dUdiY_g5tjiYs5Rhy3elvpR1LnOH-piv1JZ-JMUGv-UUjXL1WF8bJ4zTXSjYiiiMKZtwimq5WQLboPebMtAkY2OcwUHcGoNdZ7gEcsUn5vZEeT63QDu5N57Gf3y9yHQg8vowOayh7_hj-c26vOeAwyjphqLTA0svdrhoDuXqs3bS9RQNsHCQaD-l_9kXJB3dNhmkpQI-7_Woo_sWi6YK-vp2rTHuRoh4qBIJlnl8VKqqwHmACrET9DjE_91PZayiQeO2AgfYBdxgEYFQfGZMZIj43uy9zFBKUS2TSNIIipxhNFO1H2Aa-_b7Mpy56YxgrnSRBE8IP4LPiWjwUsAT-l_Og78MEb_XLvxUP3K7gZA9RgyeHqvSlyYlgryFwS_kyI8bzZO0VmYtppT4bnDYtQ5nwzgc9IZUO-RQr_xeZw-LFVi61nE5vzRCwbDrYdpuKx10SK0PeBYCUPg5udAtuGyzins76LThQy6QlqzQ4k7YP6F4ZwkN0vUWUn7KQo5WvqPw69xx_44HV7C4VCEV6N8zW16moL-W2MWz5I9gJpRFb8uCmAQLRfXQwzGT_V9cOTBuM73UcIY2WBO_v2_Te5Eyo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ad5f15cf.mp4?token=GcrzXgwWGGm7v2nAUZf09DXz1jOQKjeLIBuKGXYR-QGbUO3psimBox4PGNc3_mRNZw3qiHpSugz33rJ6R8dUdiY_g5tjiYs5Rhy3elvpR1LnOH-piv1JZ-JMUGv-UUjXL1WF8bJ4zTXSjYiiiMKZtwimq5WQLboPebMtAkY2OcwUHcGoNdZ7gEcsUn5vZEeT63QDu5N57Gf3y9yHQg8vowOayh7_hj-c26vOeAwyjphqLTA0svdrhoDuXqs3bS9RQNsHCQaD-l_9kXJB3dNhmkpQI-7_Woo_sWi6YK-vp2rTHuRoh4qBIJlnl8VKqqwHmACrET9DjE_91PZayiQeO2AgfYBdxgEYFQfGZMZIj43uy9zFBKUS2TSNIIipxhNFO1H2Aa-_b7Mpy56YxgrnSRBE8IP4LPiWjwUsAT-l_Og78MEb_XLvxUP3K7gZA9RgyeHqvSlyYlgryFwS_kyI8bzZO0VmYtppT4bnDYtQ5nwzgc9IZUO-RQr_xeZw-LFVi61nE5vzRCwbDrYdpuKx10SK0PeBYCUPg5udAtuGyzins76LThQy6QlqzQ4k7YP6F4ZwkN0vUWUn7KQo5WvqPw69xx_44HV7C4VCEV6N8zW16moL-W2MWz5I9gJpRFb8uCmAQLRfXQwzGT_V9cOTBuM73UcIY2WBO_v2_Te5Eyo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار علیه شهریاری در تجمعات شبانه؛ مرگ بر جیره خور آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/137540" target="_blank">📅 21:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137539">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
وای‌نت: اسرائیل خود را برای حمله گسترده آمریکا به ایران در فاصله شب جمعه تا بامداد شنبه آماده کرده بود، اما دونالد ترامپ برای دادن فرصت بیشتر به مذاکرات، این اقدام را به تعویق انداخت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/137539" target="_blank">📅 21:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137538">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
تايمز  اسرائیل: ترامپ از ارتش آمریکا درخواست کرده بود که حمله به ایران را به تعویق بیندازد. او در حال حاضر ترجیح می‌دهد که به مذاکرات ادامه دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/137538" target="_blank">📅 20:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137537">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سخنگوی سپاه: طی ۱۵ روز نبرد (از ۱۷ تیر تا ۳۱ تیر)، ۱۱ هواپیمای جنگنده و بالگرد آمریکایی را روی زمین و در حالی که در پایگاه‌های آمریکایی در منطقه مستقر بودند، منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/137537" target="_blank">📅 20:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137536">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
آکسیوس به نقل از دو منبع: ارتش آمریکا در حال کار بر روی طرح‌هایی برای عملیات بزرگ احتمالی علیه ایران است، اما ترامپ هنوز دستوری نداده است.
🔴
تصمیم ترامپ برای توقف حملات در روز شنبه، ساعاتی پس از ورود هیئت عمانی به تهران برای مذاکره در مورد تنگه هرمز اتخاذ شد./ ممکن است تا پایان هفته، توافقی بین ایران و عمان در خصوص تنگه هرمز حاصل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137536" target="_blank">📅 20:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137535">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
دو شرکت زیرمجموعه لوفت‌هانزا آلمان پروازهای تل‌آویو را تا سه‌شنبه لغو کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/137535" target="_blank">📅 20:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137534">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF):  در پی گزارش در مورد یک تیراندازی در منطقه جامعه سوسیا، کمی پیش از این یک درگیری خشونت‌آمیز بین شهروندان اسرائیلی و فلسطینیان در منطقه شکل گرفت، که در آن هر دو طرف سنگ پرتاب کردند. این یک حادثه تیراندازی نبود.
🔴
سپس یک تروریست سلاح یکی از شهروندان را دزدید و به سمت آسمان شلیک کرد. علاوه بر این، یک شهروند اسرائیلی در نتیجه پرتاب سنگ‌ها مجروح شد و برای دریافت درمان پزشکی تخلیه شد.
🔴
سربازان IDF در حال تعقیب تروریست هستند و در منطقه چک‌پوینت‌های جاده‌ای برپا کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/137534" target="_blank">📅 20:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137533">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
معاون نخست‌وزیر و وزیر امور خارجه پاکستان، ایزاک دار، با شاهزاده فیصل بن فرحان آل سعود، وزیر امور خارجه عربستان سعودی، گفتگو کرد تا در مورد آخرین تحولات منطقه‌ای تبادل نظر کنند.
🔴
آن‌ها همچنین در مورد امنیت مسیرهای کشتیرانی در خلیج فارس و دریای سرخ گفتگو کردند.
🔴
هر دو طرف مجدداً بر روابط نزدیک بین پاکستان و عربستان سعودی تأکید کردند و بر اهمیت ادامه دیپلماسی تأکید نمودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/137533" target="_blank">📅 20:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137532">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
الحدث: وزیر خارجه عربستان تماس تلفنی از همتای پاکستانی خود دریافت کرد و درباره تلاشها برای کاهش تنش در منطقه گفت‌وگو کردند.
🔴
وزیر خارجه عربستان و همتای پاکستانی‌اش درباره تلاش‌ها برای تأمین امنیت و ایمنی آبراه‌ها بحث و تبادل نظر کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/137532" target="_blank">📅 20:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137531">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
رسانه‌های عبری: احمد وحیدی و مجید موسوی در صدر فهرست اهداف ترور اسرائیل قرار دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137531" target="_blank">📅 20:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137530">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gU7T2uI8ochagAYINdINXI_FKYp4Ef3T8Mcif86IizbrOgvu3nhJoKbEao0n7QJD40lazc2-vfVRNeDtmI0p1aWOervYZJO12uIYj6z2aelci_mNnR4KsZZUpoJK7hAv_Fech_Xkv2ulw65nOTdUMyvOX5scUKz7xAD4boJmKH4nL5bouQBexn0iJg1iHrS9DTSL7jznNg8jT9A1_Wyypx5BA_jkljrrU_zlZmoHArp12-F-EEHoSW_T_nKC9-RxEvyI2rH6LoHrbEQz8wG0lxQklxfTDVsOWpORoVtB5E2ed-FjsRCgLbo3vbpdujh7sJyxFMIDboTdVVcg9PxYDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صفحه رسمی سفارت آلمان در تهران شایعات تخلیه کارکنان این نمایندگی دیپلماتیک رو تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137530" target="_blank">📅 20:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137529">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80c6d15482.mp4?token=fcn5F9m5FEn9BPfFNxLkqZKsyJX0VHVwixMvFiYUZClbWb93IrvZ4nzQHO_OmyB2oept68szq1dQF4HZM4T0uBCzhHT5NaqZpBxKW88woP4JM7BziB6aWxDs2Pcq7Ic5tD28ELf13eGLcdt3rh_Pvae8WIUIwZJRpLAyNsRAiqmpskbqCcNurO2al8NsZCyTAa5IHp6XYq2sMLBdhaXpY57zHivKnmY-0Yi94Gn9A5_oTeyZDJioimNHoRk4ZeRi75kGcHT7x6BAkxAxkE1ntSQT7IBms88vD0BAlVgwG2qOAXLqnlv4qB1Wt1MGacOOLQQARFethYgYvIzodoTKFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80c6d15482.mp4?token=fcn5F9m5FEn9BPfFNxLkqZKsyJX0VHVwixMvFiYUZClbWb93IrvZ4nzQHO_OmyB2oept68szq1dQF4HZM4T0uBCzhHT5NaqZpBxKW88woP4JM7BziB6aWxDs2Pcq7Ic5tD28ELf13eGLcdt3rh_Pvae8WIUIwZJRpLAyNsRAiqmpskbqCcNurO2al8NsZCyTAa5IHp6XYq2sMLBdhaXpY57zHivKnmY-0Yi94Gn9A5_oTeyZDJioimNHoRk4ZeRi75kGcHT7x6BAkxAxkE1ntSQT7IBms88vD0BAlVgwG2qOAXLqnlv4qB1Wt1MGacOOLQQARFethYgYvIzodoTKFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ موقع تعریف‌کردن ماجرای تیراندازی در ضیافت شام خبرنگاران کاخ سفید یاد نیکی میناژ افتاد: «بعد از اینکه صدای تیر اومد، مردم داد زدن: "بخوابید زمین! بخوابید زمین!" همین باعث شد نیکی میناج شروع کنه به رقص و تکون دادن و قر دادن! باورتون میشه؟ خدایی فقط اون بود که فهمید منظور اصلی “Get down” چی بود!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/137529" target="_blank">📅 19:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137528">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
برخی منابع می گویند:  با افزایش احتمال شدت‌گیری قابل توجه تنش‌ها، بار دیگر میانجی‌های مختلف پاکستانی، عمانی، قطری و... هر یک با موضوعات و طرح‌های مختلف در ۴۸ ساعت گذشته فعال شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/137528" target="_blank">📅 19:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137527">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
پس از اتریش و ایتالیا، دو شرکت دیگر از گروه لوفت‌هانزا پروازهای تل‌آویو را لغو کردند
🔴
پس از شرکت‌های هواپیمایی اتریش و ایتالیا، دو شرکت دیگر زیرمجموعه گروه هواپیمایی لوفت‌هانزای آلمان نیز تمامی پروازهای رفت‌وبرگشت خود به تل‌آویو را تا روز سه‌شنبه لغو کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/137527" target="_blank">📅 19:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137526">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
مقاومت عراق: هیچ عملیاتی علیه اربیل و کویت انجام نداده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/137526" target="_blank">📅 19:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137525">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
حوثی های یمن دقایقی پیش یه کشتی دیگه نزدیک عربستان رو مورد هدف قرار دادن
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/137525" target="_blank">📅 19:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137524">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e37e5e25.mp4?token=UrbXwah1TACZKycEf8uSlf910Jui9HcMJ-ExtY7XQJnt94s-Qjtw6XGsO2s1roauVS7AiZnvvePIsfzG6Q9bnbX3iFM_CU7LR2ARtOdIvldG3uLYYUELgehY0KrTFblHK00Laj_4gKVyjUGWOb7BvFQ632F6BYrnHIXNUQrpvxMl39Tm5UEVjF7h2gftfvJFYDMVVU-oIS6DChVbXj9yU5IgiVmpWpddbYxkFptUBJp-x0fu81FLyQdLdj0O0DpAJe4QdJWfCoYkkhOrETAqx2TlvQQzeeXdjoMznKFdhPoRMl1b6w7k3_ZcF_Mt7dExFezD3Sd2b1vQWPoHKBV-WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e37e5e25.mp4?token=UrbXwah1TACZKycEf8uSlf910Jui9HcMJ-ExtY7XQJnt94s-Qjtw6XGsO2s1roauVS7AiZnvvePIsfzG6Q9bnbX3iFM_CU7LR2ARtOdIvldG3uLYYUELgehY0KrTFblHK00Laj_4gKVyjUGWOb7BvFQ632F6BYrnHIXNUQrpvxMl39Tm5UEVjF7h2gftfvJFYDMVVU-oIS6DChVbXj9yU5IgiVmpWpddbYxkFptUBJp-x0fu81FLyQdLdj0O0DpAJe4QdJWfCoYkkhOrETAqx2TlvQQzeeXdjoMznKFdhPoRMl1b6w7k3_ZcF_Mt7dExFezD3Sd2b1vQWPoHKBV-WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو عجیب منتشر شده توسط وزارت جنگ اوکراین از سرنگونی یک پهپاد شاهد در آسمان کی‌اف
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/137524" target="_blank">📅 19:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137523">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1gwe0D34HU7MnnO_CgLXAwHr8gS0PpjTkj1uFzw5fLZi_idrA2Br4VIYG4-t6zf_r73rERqTNEQrX_vsv_IgVRJa6JIfmYU_cfB_i6Yr0USeWAcaOE2eT8tWfJ-Le2roYYM1PmKjxFklAexB9FIi17v-Clf45iE6vUGazGx3ckL3gvgr0C1bZ3JxpY0JUDHOfAJ7AtsG-4ox0pmawkTd884mSBrrTvo8_KrbUJTIhqsnai0ZmJyc3QpOQ-rX8vaC6Gz_XwTqB_Ldyp2S9Fu7zq4SNQATblpMDfLaMnDZXzzPEtn7W4gU2wky608y6JJMrobrUKKeguOXO9DoTikXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر منتشرشده از فرودگاه اربیل نشون میده ده‌ها فروند هواپیمای نظامی آمریکا در حال فرود و برخاست هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/137523" target="_blank">📅 19:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137522">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXsiKbPRJGpPCMIsSnD_p6iwfE-KgMEWc6HZj2z7TUH4-4zIEkKnT24gWh3B6EbkdqCttmolhN6oclGiHvH5s7bOSW79vA0upWc81v6eLkVW3EvXCQB7h2lSJXEVrpnCnR59ed6cFa8QRtU9ReOn-spc0NVNNJXdxHM07E7_rp74NK4yGANGAhpoc8kGsXAtU5SQmYAGpjBB7L-2Ml_2LLx2z0dBJrXSKDP8O-p6bExdeYuzBSoUo2CVPXRsCEOwO_Hd8Vz5RboLNQh5uNFgMipp9OSeQDnuyZR-CZ3hoSV8VzwGlNlLCbjhJvHbZYVz6teabuhPg1T5_fPVTaLncQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تروث سوشال ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/137522" target="_blank">📅 18:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137521">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
عراقچی: ما در تماس مستمر با کشورهای منطقه هستیم و توضیح می‌دهیم که هیچ دشمنی با آنها نداریم.
🔴
برخی کشورهای منطقه اکنون دریافته‌اند که حضور پایگاه‌های آمریکایی در برخی موارد به عاملی تهدیدکننده برای امنیت آنها تبدیل شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/137521" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137520">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
اردستانی، عضو کمیسیون امنیت ملی:
شاید آمریکا با سرگرم کردن ما به «تنگه هرمز» و «کوه کلنگ»، یک رده از مسئولان را بار دیگر ترور کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/137520" target="_blank">📅 18:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137519">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
اکسیوس : آمریکایی‌ها دیشب برای عملیات بزرگ‌تر علیه ایران آماده نشده بودند
🔴
برنامه‌شون فقط حمله‌ای در همون حد و اندازه حمله‌های دو هفته قبل بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/137519" target="_blank">📅 18:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137518">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سپاه: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در غرب زنجان در روز یکشنبه
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/137518" target="_blank">📅 18:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137517">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فوری/ کانال۱۱ عبری: ترامپ، شب گذشته یک حمله بسیار گسترده در سراسر ایران را به تعویق انداخت، به این امید که بتواند به مذاکرات بازگردد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/137517" target="_blank">📅 18:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137516">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
وزارت حمل و نقل قطر: فعالیت‌های کشتیرانی برای تمامی انواع حمل و نقل دریایی و شناورها از ۲۶ جولای به طور کامل از سر گرفته می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/137516" target="_blank">📅 18:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137515">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upjVtKGkC1wYUHxyNgr7IIjjbhbKQLJL7TS18adKS9H9jbhou5vbWIOY1w8c-1nR1HrqZo9e9nXIDkwh4ZzZBe69JJtvvKSI8XKMRn_Zst9Ll-oKEK34F6K1eCoV8LtSATo5OwGqPXTJQZ3gWy5s_XoQmIiHZRXGH3CviMvTEWSP3888m7TzWWNQ1eVembp8g6fTLdD1W14c4kOE6NsIUUM72qdDBiZxaljYM3G1SQxXKmMjUacv3xGSLxO6J0GkmYG462oNyxM_XcDgBEYFGnfQJEwO24UVPYa_T1aiIjAkxt858UA8vEnPeZxkyuVn6YOdPaH6jtobsINSHBC6xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبری مبنی بر " ارائه طرح جدید آتش‌بس از سوی میانجی‌ها به امریکا و ایران" در فضای مجازی درحال وایرال شدن است، بایستی اشاره کرد که این طرح و خبر جدید نیست و مربوط به هفته قبل (۲۰ جولای) است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/137515" target="_blank">📅 18:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137514">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ادعای کانال ۱۲ اسرائیل: آماده‌باش در سطح بالا در اسرائیل برقرار است؛ آنها منتظر تصمیم ترامپ در مورد آینده رویارویی با ایران هستند
‏
🔴
شرکت‌های هواپیمایی خارجی لغو پروازهای خود به مقصد و از مبدأ اسرائیل را آغاز کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/137514" target="_blank">📅 18:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137512">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKoaSGPvYyqgM6x7bAts-L90SLIdCvs34YgoVSsapqJ-2bn3D6VOmrJr8IcqasmEH7P1JRsIuxHCyJTy89eX4DsHmTqWqvVPkHp8DtWktbp5rUVhS_Tmylb5jMedMxpkyb9GU4lR4G-Rz5NNlEMtIYmCW6hXE0smk2XGud_2mJ1OEUAfop5GIksnJ9C81QeBfuv8x4_Djsoc8eVxhMBchEZkPSy9qdb58pSI_5TGjvdgV4Fv310FzW6QNTOCBOJBcXshO17tsPPI2WyjoAieUAiDF7ItB_-3ruHVBsTUI7AuQO-Lx3lcsPoZcWiB_UVy-t4UvksWRs-PXvd-fnGkZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZEpoeKHHNICx2at2eJGpeXoUS40q4DycT2f0ZUuILJBv0JWfw5Dihno8LrtsgOVsQbQvXaxRZxduhQOMfN-LTSASfy2bxaP4Q_llDWnEiKNVdIHSekxaf0mAa4lLiPoThP8oIi_TGv6-RUJKpZrSTF1XuMyrDIIbAFMR3GV5t-_uAcP_nbr1AKPKIlg_csoZBAOxCCvmxAWNdnDiGPKvhgUxMTwzl2w67FpZyHMQJCbJsNeZb7mwbauv1fD7OEofQ4dzErX5Me5550B_4aW1vUCUh3jK_15EA4-zjrsz7wI8DaRTv2gt-PY3ftZ6i_ZcjFjWM79nL7F_FWV_NxzaZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
فردا و پس فردا هوای گرمتر از نرمال میشه و دیگه بعدش برای یه دوره طولانی کاهش محسوس دما و دمای خنک‌تر از نرمال برای اکثر نقاط کشور داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/137512" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137511">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f0579d0de.mp4?token=S_FFb5sj2jfhZ4yDgvjw7ME1xvoue1-4vT1H0tCQUofTFaftgMSJ9u9G9sdP3T40KTYa4baIuCpT-7sSmQWBkqFSB1F5A-9OMFq6TgoujovDCd9gNc49uPQ0pHrHQx8wcf5b0mX2Fu1CvTVl2VllXw3kai7FAIHN4Zg6qMt8itw5aShzLP4F4dm52LDFHYaJi86sGSJggEucBH8TkTxm_Ykf9_vAlW4KKMzwc48e_Gxz5c2ooG1AG5Lt0-OEecdfI59TqAl6qIJMWnVmCeTyp6Ch18DhGn6SoTtKbWKt9aP-ZYbg9dEvOzPz5LIZqVZ8aE3UIU6ZIj0fSD6MHauNlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f0579d0de.mp4?token=S_FFb5sj2jfhZ4yDgvjw7ME1xvoue1-4vT1H0tCQUofTFaftgMSJ9u9G9sdP3T40KTYa4baIuCpT-7sSmQWBkqFSB1F5A-9OMFq6TgoujovDCd9gNc49uPQ0pHrHQx8wcf5b0mX2Fu1CvTVl2VllXw3kai7FAIHN4Zg6qMt8itw5aShzLP4F4dm52LDFHYaJi86sGSJggEucBH8TkTxm_Ykf9_vAlW4KKMzwc48e_Gxz5c2ooG1AG5Lt0-OEecdfI59TqAl6qIJMWnVmCeTyp6Ch18DhGn6SoTtKbWKt9aP-ZYbg9dEvOzPz5LIZqVZ8aE3UIU6ZIj0fSD6MHauNlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواپیمای آمریکایی اکنون در فرودگاه بین المللی جده فرود آمده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/137511" target="_blank">📅 18:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137510">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLi6jc7bql_z7-z3Y4Rsg9lvSqmMykBdKCNWoUvt2uoIQ5HTCT30FonqEOaZzJGZhbfjhJbQ1GRxfUq5DnhiRSJ6ULP8keFIk_rpim0sxNQNAN0q1-rck2tiqObh65GmDwWGuwVpPPqZuiqRgXbu38OlxWyxQcHdBeAPtn2uGq4QCxQxUMVDG1sLRvGd7SksiaX3dlyQwuJ-1LOH_W6lvzXC9h0f2DWceXVpJAUgNxAv5SAi78jIx86YtIuIpS4--1F5xR_2so0ZUm6bpcis0-4SnzI13jNelqUTAOIQynxqYgzTYtR52J9HUa-eSlqKnLQlYMNn00ZYMb76WJjJEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
آموزش تیراندازی با سلاح به کودکان در میدان آزادی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137510" target="_blank">📅 18:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137509">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLLPVZM7HGJrePOthYQHr6J3kqu3ETOQByioUIynFzIKv9wxYUoHdZ5OxwnL_zd8WJimTOf2_a4hIit2nnxiD4IrvLp4LUOZEfakEZHAzDt_j8Rw4VdA1SseBMk-tKXOTTZzykPhGOH7zdM6chxZQt4hukr8i_rT6MernoLneNu35c1dhim-27q9kymqfQK83kflBsFy_niZce5FjVKieRTr4-OSrzy5yEgmQaJWImz94x7fiSogPwEkJqvtQ_L4A-CqtzYLPlK5p_nlz-svcx8RpXMXmuzzh3eOrgy5UaTrWqLU8HHNwOndubxcm0HhAi2LvSZYnNme5LK14W5-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
لورا لومر خبرنگار نزدیک به ترامپ:
‏در اعتراضات دی ماه ایران، 100 هزار نفر کشته شدن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/137509" target="_blank">📅 18:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137508">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
حملات اسرائیل به شهرک کونین در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/137508" target="_blank">📅 17:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137507">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OS3P0tkWgV86zKFvsXDZ1blB_JU7qB_ag1i3LsHuevi3SzzGhqHS0bgCIwNkcfgdumu-3m_DucSmgoZ8su3lFYgIFI3iguQjrLpwb9UvnPHL0CJLCrkDtq3wn9YRiMdTVHrSWkmX25hmSNZbWyenEh_HrmRz4fe7YnDUeJO6m50Dm9jlpHNxZLwQ_bl06U5w364l2GYPoA-bN00N04sBFHB7QQRNqLbod9Hg85q6w-53MnM-27iYJr-dc6oVhOUnVGJL3_OfBAmyZR-h5OrKrAoAIjSVdYhs9Q2xA5uDQphb26KN49AKXIOF7pRlhFU7lLYYVvV3LUOtxujsWRFEhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قاسمیان، موسس
شلتر
:
اول اسرائیل رو نابود میکنیم بعد میریم سراغ عربستانی‌ها و بعد امام زمان میاد
🔴
پ.ن: عجب پوست شفافی داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/137507" target="_blank">📅 17:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137506">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل:
لغو پروازها به مقصد یا از مبدأ اسرائیل آغاز شده؛ این احتمالاً نشانه‌ای است از آنچه در راه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/137506" target="_blank">📅 17:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137505">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
شهریاری: ثابتی با فساد وارد مجلس شده و هیچ رزومه‌ای نداره و با رانت اسم خودشو جزو ۳۰تا نخبه تهران رد کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/137505" target="_blank">📅 17:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137504">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXT6-bA6UUg10KSE4ood6GgToEJ49JxF9OAdMXnWE8ysJrL2nN-EyOMPQ3BImXfAK3bPoKDfz0F_LeE3Mn45x-CHtwXRFPnndV-1FZulk81-_GJ9i_tXGGlJQqf5GN3oUr6JeHDlo6czm6v7T1q2Z7ORi5fXrU5BxfVe_REohYNmeg6jSVC35L42sKYww9LkEX-969IqOCdSesmeJ4JmdBH4RC9A2veDk-XLiQNIK1vojvmXixHMlmwisEcBaMqvpj0LyGUiGX7ZxEWOLz9YdRONnxFcJsbgJGWiitH1pCSsmeDsKHYLiyfY-cexsOIEQ_kysme8ficlgBXtgia93Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ام‌جی لاریجانی:
آقای شهید اینترنت رو به کشور آورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/137504" target="_blank">📅 17:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137503">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHQoFRl7Qv5dCWZJ99Mlh3DRkOryBh8FoL3S4VkakdSaj8nMmiptLY4j3_ebnh3uw8P7lLA5H9OoK5z_4uKsxAtuzFFLwVW5QZ8QX0xTBsOOPbIwA_vhn6hWt_zv6yNQjvGJLU5Tpg5N4hCE3q2eNI9efsCpXHI8bW2QZgElakTN61F8UDbnpR-7YhK-JBj4hwR1kLWAiHAX3m6CNa5FcTCW7WnaOyduJxgcTJp4-kYfsF1C7v2giddoSokU_TQMaE5195453GAfUnAaZMp60NhrXdDxAu0hOiRR2hy6tjDxujoAtpwpXaO8ElfpCG_ZHbAazCqdRK6Jbve_Wxp3HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکسیوس :  ایالات متحده درخواست آتش‌بس موقت با ایران را مطرح کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/137503" target="_blank">📅 17:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137502">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
نیویورک پست:
ایالات متحده در حال بررسی طرحی برای خارج کردن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/137502" target="_blank">📅 16:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137501">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JS6oQQ7sIDlQraeeJWxnCTomcUCP2J74LTwX0gJqH5UDgg9OI4A4G--kT_7Irn4J9XwLyBQGWr-fd_EBA0Xw_G6wXDWJRCoNAKO1LZR4ikwcpxtIv5A9czproEtlvg6kSfWVeVuzZ2R9cBBGKK2MJCwE9hYsELPfnLuCIYZUp2CeGRgpXBPtKBuXrkSqjC50sTWadZetMuxMihIvyWfe5sd_Hzd4CxY1C75W7tbOJCTBxHDofIzImYuHMHr8JVpug4psM0aXoCVoIT0Wb0O5oiefv5Uo3a-9GwUpDBMA0oGcuf79p0tJWf-O0viuo_nmGpMzxjdQpyEi0ahK9PJmYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قدیری ابیانه: آمریکا برای حمله زمینی به ایران آماده شده و این حمله ممکنه پیش از انتخابات کنگره آمریکا و حتی در روزهای آینده انجام بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/137501" target="_blank">📅 16:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137500">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
دختر ۲۰ساله‌ای که تو خراسان اقدام به تهیه فیلم‌های جنسی ارباب و برده میکرد بازداشت شده
🔴
محتوای چنلش هم تو بات گذاشتیم و میتونید ببینید  زیر ۱۸سال
⚠️
⚠️
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/137500" target="_blank">📅 16:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137499">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فوری/باراک راوید:
طرحی جدید میانجی‌ها به امریکا و ایران ارائه شده که شامل رفع محاصره بنادر ایران، بازگشایی تنگه هرمز و پیشنهاد دریافت «عوارض تأمین امنیت» توسط تهران از کشتی‌های عبوری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/137499" target="_blank">📅 16:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137498">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74e22034d8.mp4?token=UDCyPOn4lKTq0ZPGkX2xZTVRPXwCqKnT5HaqYl0CSpjFtiK3cspL1mO8Ft1IhWdx_b-KD7Luxim0GxpYHDl2upTs4lsg7dvDgb6w40I_oiRbU-HFl7XVDrx9tAP2YflmchYDfTjYxsKVtpJlI-l1DFyIQADaZ2PsGJ1G9duOnSPHluC2X4ejxspYmSNfSBVepV16moIDcgTYTVh5f6N4hJKVvfuufzBb4cHV_DJCwvsFGFFN54XT-FNYz7qL6hKlQx5Z0pdXzMyMh8NBdxC7vvMLgB2N2beT5fFJnkO3MMhBeH9bsKNMZc0brMXQQ3TSFBK2ircrSxh8wv7sNHQ7zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74e22034d8.mp4?token=UDCyPOn4lKTq0ZPGkX2xZTVRPXwCqKnT5HaqYl0CSpjFtiK3cspL1mO8Ft1IhWdx_b-KD7Luxim0GxpYHDl2upTs4lsg7dvDgb6w40I_oiRbU-HFl7XVDrx9tAP2YflmchYDfTjYxsKVtpJlI-l1DFyIQADaZ2PsGJ1G9duOnSPHluC2X4ejxspYmSNfSBVepV16moIDcgTYTVh5f6N4hJKVvfuufzBb4cHV_DJCwvsFGFFN54XT-FNYz7qL6hKlQx5Z0pdXzMyMh8NBdxC7vvMLgB2N2beT5fFJnkO3MMhBeH9bsKNMZc0brMXQQ3TSFBK2ircrSxh8wv7sNHQ7zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محمد یاراحمدی، دوبلور پیشکسوت سینما و تلویزیون درگذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/137498" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137497">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
رادیو رسمی اسرائیل: ارتش در کرانه باختری دستور گسترش دامنه عملیات‌های تهاجمی خود را دریافت کرد.
🔴
ارتش اسرائیل تصمیم به استقرار ۸ گردان در لبنان، ۵ گردان در غزه و ۲۶ گردان در کرانه باختری گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/137497" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137496">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
اکسیوس:  طرحی جدید میانجی‌ها به امریکا و ایران ارائه شده که شامل رفع محاصره بنادر ایران، بازگشایی تنگه هرمز و پیشنهاد دریافت «عوارض تأمین امنیت» توسط تهران از کشتی‌های عبوری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/137496" target="_blank">📅 16:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137495">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8e4bbc306.mp4?token=sCw6nGG3kqeYVAKq8Lksn-VyYU-XyIJrG3HR_u6si1gHRbYh2_kKJ5-aOGLqdK51qubS5hAvdGbqso_zZOvaz-9n6zKifd9yDR6DXPkbWknAg6oZVH_Naq06xAi3IcJ7IgAtbo2GMRohTgRbge2AH9xrNSUHpR6d4ul9hroE9TKktnC4Cy0fQYRMNfTIF4FX8U8QNngpwq1eFzneLk05Q4uAUOLD4juGRKqFaUmJFyK3iOoc3IJI-PblBL4BCVYPIYWWcX-vhWOzVHGCmTZvqumwVzr5goHMyLgcmyMK4CbPCCAa0T52UuJI_y3NWey4Gre4ZvSdAp170rBUCmrfTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8e4bbc306.mp4?token=sCw6nGG3kqeYVAKq8Lksn-VyYU-XyIJrG3HR_u6si1gHRbYh2_kKJ5-aOGLqdK51qubS5hAvdGbqso_zZOvaz-9n6zKifd9yDR6DXPkbWknAg6oZVH_Naq06xAi3IcJ7IgAtbo2GMRohTgRbge2AH9xrNSUHpR6d4ul9hroE9TKktnC4Cy0fQYRMNfTIF4FX8U8QNngpwq1eFzneLk05Q4uAUOLD4juGRKqFaUmJFyK3iOoc3IJI-PblBL4BCVYPIYWWcX-vhWOzVHGCmTZvqumwVzr5goHMyLgcmyMK4CbPCCAa0T52UuJI_y3NWey4Gre4ZvSdAp170rBUCmrfTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوکراین تصاویری را منتشر کرده که نشان می‌دهد چگونه پهپادهای روسی با شلیک از سلاح‌های سبک از داخل یک هواپیمای یاک-52 سرنگون کرده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/137495" target="_blank">📅 16:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137494">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/exW9rCBxfJmlvtYoaGUgBMXPIT8FuHZKdQak_xmI19xeR5OVQk8QRhsrW_fDMIXWxGMIi8LbAf2rp9weNpHJBhJ-lCydc6I2hjG9Q3HKfOZFYgZxGwCaDn2lIKtf-MJgiiqCCVy8Z1xFUm6stIbqNTSB7oWMQ76zSYHggUivLTkeOu-th6A35SNpChKCmp-mrzne_dnMOQ6P3ZTMJSA0JeLsteMWvDz1a6Us-yeeucYQsdnYxUhw3CP6bUqj8d7ZXOvCNHG_fyuD_Ws7f61_-UdcI6QJBKHI_UnQPjBmp4s2xxGebZUr3B2hg9loUqdFeUEggnqwodVbhT-D3dZamw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله عربستان سعودی به هدفی در مأرب یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/137494" target="_blank">📅 16:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137493">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
منابع عربی از حمله به پایگاه آمریکا در نزدیکی فرودگاه اربیل خبر می‌‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/137493" target="_blank">📅 16:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137492">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
سخنگوی نیروهای مسلح یمن:
دو عملیات منحصر به فرد علیه عربستان انجام دادیم
🔴
اهداف حساسی در تأسیسات آرامکو در جیزان و ینبع هدف قرار گرفت
🔴
محاصره دریایی اعمال شده نیز همچنان پابرجا است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/137492" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137491">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی: مذاکرات در هماهنگی با مسئولان ارشد کشوری انجام می‌شود
🔴
عباس گلرو: مذاکرات در هماهنگی با مسئولان ارشد کشوری انجام می‌شود و مذاکرات اخیر نیز در نهایت تصمیم نظام بود.
🔴
آمریکایی‌ها پس از مذاکرات اسلام‌آباد نیز دوباره مرتکب نقض تفاهمنامه شدند، بدیهی‌ست که در مقابل ما نیز تفاهمنامه را نقض کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137491" target="_blank">📅 16:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137490">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuBPF0pdOitz5Dnp2ArlfZ-TNfwSz5bloSpNqel7UcMqaUyOTCqr6Pgd_Oo95ksdT7LfzryTVhBN6T4N3Za8_cplCeQJ6vY69mOqJxbhKFmLFNvaaRJ5K_tbP6zI5naUYGFg2tlIrGHzHbKkgqCzeFdnF7xXY_FlPYH2rx4PZta1xmLVcMXBfGbEP_ucMrqW_SLYTmHZG4_lvMmHC-LHFuRUwdJby8cAWv5M8XmluwzxuT-_cj9LQqii7BtX26rzNnYem4-diNuKd4pi4h8orXklWx7qcKT5xU8SM4O0dlv-inGL7hnVbO-5-ZAJnRsSbwLHMBJipWRX2MdySA_6ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آتش‌سوزی‌های گسترده، 200 هزار نفر را در فرانسه و اسپانیا به فرار وادار کرد.
🔴
آتش‌سوزی‌ها در فرانسه و اسپانیا شدت گرفته است. آتش‌سوزی‌های نزدیک به مادرید از کنترل خارج شده‌اند و 141 هزار نفر در مناطق ژیِروند و لاند فرانسه به تنهایی تخلیه شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/137490" target="_blank">📅 16:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137489">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRZV4srZASgqSel_4uEISgF_pv-tiqTQGcinizpJ23KIrb0CoYXIoteE6cIFyVQWhnZiChJlSoBpHG05AAhvfh_8M8liI6OwzSniz4DkImFR9wfGW0r2bguy4yEtFXPDZkMnwW5Y0ZLSSf4FF1DWQZ0Lajhw0lLUbn-qdTXMhCAa5FztZQdx1ElUeBcvmE96MD2PutHtO6VL2Ytx5gmjTW9H3in3cW_PXg5ZYaP8II-AuqMqH2Pd9h-R2S2lRGNcB8VRRo8qQObwJWOBA-2wu6gogAuwr9cG1Xgnb8bUD4JZ-b7_5uC6irq66Croor_8qk0Z0_fOfB8RJ-HQ2OT3Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رصد پرواز نظامی آمریکا به سمت شمال عراق
🔴
برای نخستین بار، یک فروند هواپیمای ترابری راهبردی C-17 Globemaster III متعلق به نیروی هوایی آمریکا به‌صورت آشکار در حال پرواز به سمت اربیل عراق مشاهده شده است.
🔴
این هواپیما که از اصلی‌ترین ستون‌های لجستیکی ارتش آمریکا به شمار می‌رود، توانایی حمل بیش از ۷۷ تن تجهیزات و محموله نظامی را دارد.
🔴
بر اساس ارزیابی‌ها، احتمال می‌رود این پرواز با هدف انتقال تجهیزات یا مهمات به نیروهای مستقر در اقلیم کردستان عراق انجام شده باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137489" target="_blank">📅 15:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137488">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
نیویورک تایمز: ایران در ماه‌های اخیر برای مقابله با یک حمله احتمالی، با تقویت استحکامات و ایجاد موانع و تله‌های انفجاری در اطراف برخی از تاسیسات هسته‌ای خود، آمادگی لازم را کسب کرده است. این امر، اجرای هرگونه عملیات زمینی را بسیار پرخطر می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/137488" target="_blank">📅 15:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137487">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/878fcc76b7.mp4?token=B-sC4z6xCSEauzKhjJthkVNYMyzDGnE9-sy9-DhTjwi0yIx2GOJYWunbuAJ7bTOYwYlg4at0dLtkciKae6CMJFJNlKCA-Hf4iDDV38tVnPmb2MErmCzATDm7D_F622N2IDNu4RUh3up8Xs-xPVAlyji6_TKbkQNWuEG909fJGAb21gKz7crtV2pYNakDDe1ffPP_e1x3bZIDQlGMX_F9PguwRIQTW1S4IEuFfuhsslY_UgkK8N_uVq8mT6pUzDPPDfwr8t1Vn2JXOyv4kjGwjG1vdhJ0mwvFPwYuA-JAJk1gNsLLIu5LIJCkJPaK0lSeSSvVxYYTbbGEXKSiq5kymQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/878fcc76b7.mp4?token=B-sC4z6xCSEauzKhjJthkVNYMyzDGnE9-sy9-DhTjwi0yIx2GOJYWunbuAJ7bTOYwYlg4at0dLtkciKae6CMJFJNlKCA-Hf4iDDV38tVnPmb2MErmCzATDm7D_F622N2IDNu4RUh3up8Xs-xPVAlyji6_TKbkQNWuEG909fJGAb21gKz7crtV2pYNakDDe1ffPP_e1x3bZIDQlGMX_F9PguwRIQTW1S4IEuFfuhsslY_UgkK8N_uVq8mT6pUzDPPDfwr8t1Vn2JXOyv4kjGwjG1vdhJ0mwvFPwYuA-JAJk1gNsLLIu5LIJCkJPaK0lSeSSvVxYYTbbGEXKSiq5kymQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای که اخیراً گرفته شده‌اند، نشان می‌دهند که یک نقطه برخورد مستقیم وجود دارد. به نظر می‌رسد این نقطه، ناشی از اصابت موشک‌های بالستیک ایرانی جدید باشد که به ظاهراً به مخازن سوخت در پایگاه هوایی موفق السلطی در اردن برخورد کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137487" target="_blank">📅 15:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137486">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d777d53bf.mp4?token=hjTLiroKnKL6tiRS9xpdBvfd0WbO4AHTODFThTrY-fh1lxKNpyeu0cnW2nQRakIeZTP51UwUmjH4Yq0L9kqGuh2mGG5Kb1ZhmvknXh7Clep4RTudH0Hxd7VxYMnzG295HD0dSy46VD0GZrqbTNTEVPeJ3RBctHL59d0SPlDHakVCk8uKieeyxoBBlMAKcYMnB5-H9D6uH7JOEUTq4z26clxi-jGhvIMfETlp1KQjRCbAe28k3wC1s9b0ov7uHKeUQabtEBIgA3lFGb18JxU1-axcxKjrZ0reVG9SVJK1BoYtQL7odRVCzxMWVZGRDILkJYVkKAYn_RRmgpatbYesBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d777d53bf.mp4?token=hjTLiroKnKL6tiRS9xpdBvfd0WbO4AHTODFThTrY-fh1lxKNpyeu0cnW2nQRakIeZTP51UwUmjH4Yq0L9kqGuh2mGG5Kb1ZhmvknXh7Clep4RTudH0Hxd7VxYMnzG295HD0dSy46VD0GZrqbTNTEVPeJ3RBctHL59d0SPlDHakVCk8uKieeyxoBBlMAKcYMnB5-H9D6uH7JOEUTq4z26clxi-jGhvIMfETlp1KQjRCbAe28k3wC1s9b0ov7uHKeUQabtEBIgA3lFGb18JxU1-axcxKjrZ0reVG9SVJK1BoYtQL7odRVCzxMWVZGRDILkJYVkKAYn_RRmgpatbYesBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سپاه با انتشار این ویدئو، آمادگی برای نبرد زمینی با ارتش آمریکا را به نمایش گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/137486" target="_blank">📅 15:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137485">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75853bc80.mp4?token=lhO4N1uMtRgT-JRAMzoCZeMMFYhLeb-iOOwKZu7F3zro75ICV6e6OFSYgBD9a33m1ffI4MOTqZz2pbcwuniQx3t1Mvn_hlPao26NHWGnHXzEkwUiE1pKFECRR51jyB-w20FTKRcwb-SW094a2FjPQXD3aAD4fFR0KQvKBBdQvW87kXZ69l3xtYcIBKyjp_pOjvkd_zVNl8fceEOORRQZFkStQ4s0UhHZsLq9cx9hvFXboDN8tqwtuXo7ITeT2ns33E6RixymN29jo_JhljtjNvpVExBTfn3kD7rmb3eHJxKKXbdxn3R_9SIhj7lRlT-oHkNzdlLJGY-oJasJ_PtdOAFgdyZRXbN3CDZ6YtB8HgvLQOu3ktX6fzfa3wVaTSEIS8MJcMxwJclZqD05ylFIgXJBKxLl3l2gNm5huS0aj8bFcBtUr4G8_z-x8arJfN6OeX4yDxoUW6dYSgYrWugba5N9vK_noxZTQ4YwaRPir-Mu737rG-1yzNmY5FC9CPOVVxCRowmZHLr-WcyWhbZH1BEg1nPUwucGTN3Dm4cDHtj8BTj6UfKVhXK2S0a76Pc7TN3iNA3WLRAy-U4E4BOmUOFTaY9uVdii3wtcgLwG37GSXHQRpfb4Qxe31fWY1YJjpcgHwCB70J5YiJM6TCN-Atx049bMb8LCQz2JXuZiqMk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75853bc80.mp4?token=lhO4N1uMtRgT-JRAMzoCZeMMFYhLeb-iOOwKZu7F3zro75ICV6e6OFSYgBD9a33m1ffI4MOTqZz2pbcwuniQx3t1Mvn_hlPao26NHWGnHXzEkwUiE1pKFECRR51jyB-w20FTKRcwb-SW094a2FjPQXD3aAD4fFR0KQvKBBdQvW87kXZ69l3xtYcIBKyjp_pOjvkd_zVNl8fceEOORRQZFkStQ4s0UhHZsLq9cx9hvFXboDN8tqwtuXo7ITeT2ns33E6RixymN29jo_JhljtjNvpVExBTfn3kD7rmb3eHJxKKXbdxn3R_9SIhj7lRlT-oHkNzdlLJGY-oJasJ_PtdOAFgdyZRXbN3CDZ6YtB8HgvLQOu3ktX6fzfa3wVaTSEIS8MJcMxwJclZqD05ylFIgXJBKxLl3l2gNm5huS0aj8bFcBtUr4G8_z-x8arJfN6OeX4yDxoUW6dYSgYrWugba5N9vK_noxZTQ4YwaRPir-Mu737rG-1yzNmY5FC9CPOVVxCRowmZHLr-WcyWhbZH1BEg1nPUwucGTN3Dm4cDHtj8BTj6UfKVhXK2S0a76Pc7TN3iNA3WLRAy-U4E4BOmUOFTaY9uVdii3wtcgLwG37GSXHQRpfb4Qxe31fWY1YJjpcgHwCB70J5YiJM6TCN-Atx049bMb8LCQz2JXuZiqMk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صف بنزین در اربیل، طبق گزارش ٩٠ درصد پمپ بنزین ها بنزین تموم کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/137485" target="_blank">📅 15:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137484">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
رسانه‌های لبنانی از حمله توپخانه‌ای اسرائیل به کفرتبنیت در جنوب لبنان خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137484" target="_blank">📅 15:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137483">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
آنتونیو گوترس، دبیرکل سازمان ملل متحد: نقض‌های اسرائیل در منطقه جولان سوریه غیرقابل قبول است.
🔴
جولان، خاک سوریه است و سازمان ملل متحد از تمامیت ارضی، استقلال و حاکمیت خاک سوریه حمایت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/137483" target="_blank">📅 15:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137482">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
آکسیوس خبری درباره آتش بس منتشر نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/137482" target="_blank">📅 15:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137481">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وزارت بهداشت: در سال ۱۴۰۴، ۴۹ مورد ابتلا به تب کریمه کنگو و ۵ مورد مرگ ناشی از آن در هرمزگان، فارس، کرمان و اصفهان گزارش شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/137481" target="_blank">📅 15:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137480">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
نیویورک پست:ایالات متحده در حال بررسی طرحی برای تصرف اورانیوم غنی‌شده از تاسیسات هسته‌ای ایران است.
🔴
جوزف رودجرز، معاون مدیر مرکز مطالعات استراتژیک و بین‌المللی، گفت: "متاسفم که این را می‌گویم، اما به نظر من محتمل‌ترین راه، اعزام هزاران نیروی زمینی به تاسیسات هسته‌ای ایران است - با در نظر گرفتن تله‌های انفجاری، استفاده از تیم‌های ساختمانی و حفظ یک نیروی دفاعی بزرگ که اطراف این مکان‌ها را محاصره کند.
🔴
از آنجا، یک تیم کوچک از نیروهای ویژه، عملیات واقعی تصرف را انجام خواهد داد - که عملیاتی "بسیار خطرناک"، از نظر لجستیکی پیچیده و در یک محیط پر تنش، دشوار است. ارتش ایران تا حد زیادی نابود شده است، اما هنوز از نظر تجهیزات، پیشرفته‌تر از نیروهایی است که مادورو را محافظت می‌کردند."
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/137480" target="_blank">📅 15:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137479">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZO8AVzHsABkEf2BsebM-u-ROFw14tWna8TM4EbhHQFcetcDxWmYGAfG7eO6W5xTMYHZ0UWZlw7NLcSAeh8Lux79KiQA3MTmAB_QVoNlPaocugcEPgJQ9j79AYdCddDv6PEUIED4PdI3AehWMgpbxKoMc7BqiMjM28S3GNTIpfKqfFcsJGI7UOAG8-hze7WUX0yM835-I1IQmOTZmxEe5CBjQk6C_16yhPwwbbj7IDCdl9ojXo6Kq_RJbui6jo2Trb_g5RB75JoOpG5Pcfc84kzuuzc5_PRRO16byS31ZHfXdSG7ruAlHdo0jZzXce3zpky-1mmFNiQowsfzCCgg6EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برخورد دو اتوبوس مسافربری در مسیر دیر الزور- دمشق در سوریه باعث کشته شدن ۱۹ نفر و زخمی شدن ۲۷ نفر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/137479" target="_blank">📅 15:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137478">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/entDWYFI7SPLuyR1i9rweZlBptxZv8rikO1M5mYemB0ikASRIzwNNrmQ6bSdABuMdgEKYIkg5lx4cNAetsaPXqN5Fdz8uhyAnrSEnaQT9DhcKDA7HVwuVPBdCQpY4tO86zsmvHn2hNMCv_R-le8xzb82iI6BMK38uEhK8whoV2hf396m6Lv9FGe3SfOgNT_IRGBFL8DcKuFis-3uoxBgqEyisyZX03YE4KLGomIM7Q9SY9ippepesSg9mgDmNsV3fANXTCg9x8WqZ2END_TfSO3ze8TfkyzG8_3r4p7Eeo2HX1QEwnJtaWmE3SzFn3NDs9tWldtdvbht0VwPmcTIpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: اگه وزیر نبودم میرفتم پشت لانچر
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/137478" target="_blank">📅 15:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137477">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42a782cab2.mp4?token=V1oD-uQbYbk4UZ9jSqJEzRVZ5ee2p5KyoC9jKdXHHe5R43VK8-V_elMReM7K_TFR81QRPncJTsz6fU6A8nPunRkS8lcV3IPeFEIuOnBZxjwYW2lYJgY3eg80yLrvbxAByjRCSZk-pkRvN03_YuX6yXLmKdre6teauYJMzajk0je1kx1v6ZT7WmR0QqF9652RKVzL9CifC1rZJp8L-NyoQ0Kzc7Lz4uQNLQCmFijykKqJ46NRylpVvQ1RZZ1YZH8Ue_2nNguAOS1U5t-cuioy4bDe0BelulLimO2NJjdFuIDyPiG1yew2q7yTGGIjBZXkB_voxNU26MTSFDMfsCcN0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42a782cab2.mp4?token=V1oD-uQbYbk4UZ9jSqJEzRVZ5ee2p5KyoC9jKdXHHe5R43VK8-V_elMReM7K_TFR81QRPncJTsz6fU6A8nPunRkS8lcV3IPeFEIuOnBZxjwYW2lYJgY3eg80yLrvbxAByjRCSZk-pkRvN03_YuX6yXLmKdre6teauYJMzajk0je1kx1v6ZT7WmR0QqF9652RKVzL9CifC1rZJp8L-NyoQ0Kzc7Lz4uQNLQCmFijykKqJ46NRylpVvQ1RZZ1YZH8Ue_2nNguAOS1U5t-cuioy4bDe0BelulLimO2NJjdFuIDyPiG1yew2q7yTGGIjBZXkB_voxNU26MTSFDMfsCcN0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ثابتی: بعد از جنگ با عرب‌ها کار داریم و نباید اجازه دهیم تنگه هرمز را از طریق خاک خودشان دور بزنند
🔴
شهریاری، عضو کمیسیون امنیت ملی مجلس: به چه حقی؟
🔴
ثابتی: چون قدرت داریم و رئالیست هستیم!
🔴
شهریاری: خدا نکنه قدرتِ آمریکا دست شماها بیفته وگرنه پدر دنیا رو درمی‌آوردین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/137477" target="_blank">📅 15:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137476">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
وال استریت ژورنال: موشک‌های خیبرشکن ایرانی با ترکیبی از مسیر‌های پروازی، مانور‌ها و سرعت‌ها، سامانه‌های پدافند هوایی را گیج می‌کنند
🔴
تهران از این موشک‌ها در حملات پیچیده استفاده می‌کند
🔴
خیبرشکن‌ها می‌توانند مسیر خود را بیش از برخی موشک‌های بالستیک دیگر تغییر دهند تا تشخیص آن‌ها دشوارتر شود
🔴
این موشک‌ها همچنین بسیار ارزان‌تر از رهگیرهایی هستند که برای انهدام آن‌ها استفاده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/137476" target="_blank">📅 14:58 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
