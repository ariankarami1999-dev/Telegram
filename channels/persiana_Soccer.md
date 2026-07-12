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
<img src="https://cdn4.telesco.pe/file/BeLSskF5GDFEfoeftmQ0aCWSxrsQ31UgjHXCXaY0nEdiz6N_AHst36mPCFvflWGfT_sKxfd0M1SdUXMTwMOYxOG32_sCyBDEyM0DsnZe3ejmQaXDJ-XitrhcNCma3EddPN5CbKH3Xg4hM54nRn-bIw4wj6dHgAw32DZRNkeMgsIxJFDPWDzrIOCxINE7dVQkVWIi0oOo_2Ef2-CGobgzd8Pc3MfNDoBw7YHiu301sczTvW_fzSvilswaJ5WBKE4Tc0fYW8glcBG2s_-1h00Srg4Z4ULxm3VKKtdrJrJ_axQxZ5bgH_FzVdUnyu46SfELSRPyKGvDfE673w2k0-IJhA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 435K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 23:32:14</div>
<hr>

<div class="tg-post" id="msg-25553">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQMammMSGbIEN0zu0eXYpe7mH7S0vEW6UMyjsJ0OUsxHDvNoOEjdtKa7VQkw7VABwUkpQoFJDYfnizh2IALb4a8gB-NBY6mjhG88bCab3Ijph7Tw7d98NpmGklarHVux-Mf-ejh6HVDAclM7nK3fLorfbEIgRWKYaZIqBujmTQGaiOm14CEGC--UQiMW4FsrSfuLPMXFkgHI4hrT3lS5vxpViIr6cR4-GTd1Sakc_2YYpNFvfT6FEeRCMAxzXf01cl0Pc4UUimzMDwftXEIUttmXTJIYHujSplwaIlTwU9NpRPWFX6eN9N7CuhP4rF2TpxDsBYVVaMwv5UAiEMDAwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/persiana_Soccer/25553" target="_blank">📅 23:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25552">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcFgNrvzTPws02Iigu9fSoxh2CHi14cV2aZbNEV3SD_a2zSIoKIyMkJe0KY8UqyNzNANCGpC1atT64hd2agJEPNrmTWjyz5FOiErYcHmQYNMsA2iLfiwyHlD7unooqQ6Qf36I2uZuOIhesPnmvERJaA4IpDSvvUjOeqpwk8KbQ00u_nFvVuM8p0k_L7PXfmlNOXM02HTSAaeMTNb-Oc2qQAsJ7_DkVZwM2xwrRFA2hHF999ZMntBhTJ12-Xf3JVQQpWSm_2gXhsdK_zeT7I1pXItrcopaJFmyYqCpAv3n_iBg2y2ARiz2gjOQKxRvlQ7sPCbGD6iqFoY8qfsp8MMMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لقب جالب لوکاکو از زبان فیروز کریمی؛ جالبه بدونید که برای ایشان به‌خاطر شرکت تو برنامه جام جهانی شبکه جم‌ تی‌وی پرونده قضایی تشکیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/persiana_Soccer/25552" target="_blank">📅 23:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25551">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">📊
🔵
عملکرد مهدی تیکدری ستاره جدید سرخ‌ها در باشگاه گل‌گهر سیرجان:  ۱۳۰ بازی، ۱۵ گل، ۷ پاس‌گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/25551" target="_blank">📅 22:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25550">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GP9VVbBkx-rFjbAwESiLHmm2PtNAl1UJrjYrFWWRyeFa_1SfluVsrAPEAuwwTxsqkLPcFtktRmjpI-aC6d0FuUwiGlKxnx19qQkkZVIrS9P2_yDkoqx5oxn3sqtgUAdA7-y9tP21IFXwvAH9dhQ4unhTv6ObWJypLkUtwFagBurdrFCeuL1y7xSFWNezL6Ymc9d9v5SpbRa2DEkyID1u9riUDUWniMpVZ3cu8KaMgpfUJYBsrLkObnhssmiK1MGpfFX02NLfQU3URAJ1G5v1LPsLx3XZTKhRGv2uIeri91jB10-tzG_t6L-0io5BEKaj_es_74bEaV29W-DMUyWPfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/25550" target="_blank">📅 22:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25549">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fu5ai3V-NXiQ3DUxdCQDTPMi-B7QzA5GiO4nUGtYoOiJ7CwcBSWVMXLR3JlVKa-IZCMbfDalHWOYeim-EQP5zW_26v6n8YZdudJRXbWozB26mIScS2Jngo6rG5OzzyixoNu-ZjFYeVPD5XVzc5rQBxg8AuyYGUKHLuWFK6CjW6m1MGrWxBZroLkPk6N23QeNrapwIK3i6Y6rQBw_xB_t2YsAVoGLVjy3b2K5FsyVOEnvCW7oxwHEk_uTK6380j38nIyV9JGl6q99wBQ51jEEQKHUTJgpMEVN57ZZWyJllHPG4_IEHI09IUfEr5uHWL5n3G7z7jlu27vYVX5uXWiByw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس ساعتی‌ قبل با پرداخت 700 هزار دلار به باشگاه‌روبین‌کازان؛ کسری طاهری رو باعقد قراردادی یک‌ ساله قرضی همراه با بند خرید قطعی به ارزش 500هزار دلار دیگر به خدمت گرفت. بخش رسانه ای باشگاه بزودی پوستر طاهری رو منتشر…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/25549" target="_blank">📅 21:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25548">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfD-FvGdc7KuBykd-fFXj60v-5Ei7lttpgpdTHGrbDqhsqRtgtEJdqupnK0R0ahhMs6kt18EUiocnL8_XVm_dmfRltYXhUZoXEYrYsx3lrp0fV11Bf4zmIsFre47m5nr2ymWbEXwviUdGgy16-EgxtVcijsbzdFpbdT3gPRXVToN8S04tpcnyI9g-uyi13XeC_SOetEgxPOJA4IeBtYg7vvxjeMYhJuKCvCGyB_FOwJBUgyrxhtucMVeMOIPmkCK5fX_QNhGbd8wfHMptQLckZSYAGNk5ksuwUFp30MGLE0Tddux5x60Yt8VLlUEEGys9aBm99eSPJQACB_2Pmtiig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇱
فرانکی دی‌یونگ و همسرش که در تعطیلات بسر میبرند از چلسی پیشنهاد رسمی دریافت کرده. ژابی آلونسو درخواست جذب این بازیکن رو داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/25548" target="_blank">📅 21:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25547">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROSfb8TzjmxrcgEVvg3p4innSQgYNZglWDg0BjyJc6MmIeOXMZKj-2rV1LkqlmxXYMY-OFhlGHlVGFVSQhgBMroIT3AmgjGR5luhs3mzN9AttzK617Fi_i-a_tX2koAwpUPGIhZCusRDW3W4VWl84DjjNQsfi2q7NS2utWMQnEP4rg8_ZqeEwQmAridD8uRPUKby7NLi-4qpbL_0xydukkIQ6iFsLWlf5JMalToACe6zN-pvecS2uJLKggEDgKrSGb_CbsbEcEuRh9GUOOHyHZy9FGH6OweF40Wx6DFOVGdz1a3ZQqUn41GamgBkZK6quiEkd1B9djJQqC16nK_Rgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌جزئیات‌ عملکرد لئو مسی فوق‌ستاره تیم ملی آرژانتین در رقابت‌های 2 دوره اخیر جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/25547" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25546">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1YRQG2FkIxRs0A8uM7K0WPBwGYnihXivtREEAlmnEMt0Rzleyxx1JsbekvjUMM3g1D_fPgP1ZmPeN4JGBnL8VFpTw6v8DEhWD6WHv-LIukVF2IIyTj2-2AN_aRqDyj7fuDuPHZ2aoEskq7c5rnZdFkOgh4yANUBXO8vJ-v6v4WE0yWab-WnBs6MfHe5Xi-6Yyr7FSRNm9OsVUJeOcmDvJW2W6LJy655fbjnYsOjTAG0pljYUwqzcjURnww97p6-vy-2XAGyUUXhn4ctT_arBgd9aN0ncaQpNNiQGiX6veHIJ7zky0zWQb52KuvIMFkjJjs0lsCpK1IighuGWAVjmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اینفانتینو میخواد فشار بیاره تا جام جهانی ۲۰۳۰ با ۶۴ تیم برگزار شه. و ارژانتین و پاراگوئه و اروگوئه هم یک بازی به شکل افتخاری میزبان باشن. مشخص نیست فقط برای یک جام میخواد این کارو بکنه ولی ظاهرا عزم راسخی داره که این پروژه سنگین رو در سال ۲۰۳۰ انجام بده. جام‌جهانی ۲۰۳۰ با میزبانی سه کشور پرتغال اسپانیا و مراکش قراره برگزار شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/25546" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25545">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXNEgaKKyDACKqU4tgkpG5YzcTBeB4dPVeH8x5BDvF_Q6tzqF1wso8Oj9vOIK2LOcA1ZSqAeLatov0UrVK1LYXM6s_NydzEwTj9LwlIZC_q9e2Kp8hBs8jDjWNBKWDH3hBBnbsRzWQ4o7fcoosDS8y9Z9bAkKMJCku5gndgUQs3FUv5ureXroPTSr6OetmBfaceJ2Ptswr7k6eKG8YC4hNQ9gA02_ghEiWit-AqnnMv48NUSV8YwdEgJ62KIPXnUfYBCb3mC81wiQTX_5dbhIb_FHl3IWsIVqUMDzworR-IHSfgVuF1qZXNdwanK6hnA4UFtXLv_HLqL5S8av7B_Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🆚
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
🆚
🇪🇸
🏅
تکرار فینال دوره قبل یا شگفتی در راه هست؟
🔥
🏆
اسپانیا و فرانسه از یک سمت و آرژانتین و انگلستان از سوی دیگری برای رسیدن به افتخار حضور در فینال جام جهانی ۲۰۲۶ با هم مبارزه میکنند.
👀
⚡️
آیا این بار هم یاران مسی و امباپه در فینال بهم میرسند یا مسیر فینال متفاوت خواهد بود؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/25545" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25544">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d86d8e16.mp4?token=FXbRifL0KOPWq5uHkEHy-8OFFDTpY4u0UPZZgmx3fCzcUYwGJ2WVT_zCsPtiRxF3to-_lAFlJupS80ak_XwBYakL010KJ-iq4OXN7Zwrn9_W74hmmLjJESruQETaGqt09s8q53qY_kUplG4QBstfP4hN49q_kqnrECrNv1SqIagBqDDyAmsehbTwWXePbgB6S-8oDQi4W9Qrs6nxbSL4VlFRy3-mSwS9TWSEhHBIhYtTSQSWGeDsUg7qqhClfmf4fXjhQwfjje6JB2fbbUU430NVSnYeGvP54wkNLcDWu_y4xoB2D_HrVijC6fOAWpQsha-KCUATyUO3uZCj0_ao0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d86d8e16.mp4?token=FXbRifL0KOPWq5uHkEHy-8OFFDTpY4u0UPZZgmx3fCzcUYwGJ2WVT_zCsPtiRxF3to-_lAFlJupS80ak_XwBYakL010KJ-iq4OXN7Zwrn9_W74hmmLjJESruQETaGqt09s8q53qY_kUplG4QBstfP4hN49q_kqnrECrNv1SqIagBqDDyAmsehbTwWXePbgB6S-8oDQi4W9Qrs6nxbSL4VlFRy3-mSwS9TWSEhHBIhYtTSQSWGeDsUg7qqhClfmf4fXjhQwfjje6JB2fbbUU430NVSnYeGvP54wkNLcDWu_y4xoB2D_HrVijC6fOAWpQsha-KCUATyUO3uZCj0_ao0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌بامداد‌فردا؛از نبرد انگلیس مقابل وایکینگ‌ها تا جدال مسی و یارانش با سوئیس
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/25544" target="_blank">📅 21:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25543">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aY2FGKQBNHpJtxLsMxLq5N_D5mc7yhgOCexPviESN0L5wZ7h568TXZPn5OefyXglZRtmBmPrQlOzFKdeWgvqHuBj80PkvuECVAVhXoxfucWq_uCRvxK4DVz6iHuEWBBZ1daJZfr-6OpXwfmNphgiljyLke0AQzBCgvR_4_TpbGIWCgkXorMy430eIj2eYyJnfdjwtq3j6MyRdvN75C2roHGfMhGjZPCq0t_gwC231tavb-jB-rnQO-kvND6u5TvZ19ZvHTMQs31UEK0Swi4tWbKcc75dKb_rmCdyPwaopX-CxG9OfKVo45JM7kxh4MrSikXdGIEil7rwC1UyNqpgTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طوری‌که سورلوث در بازی با انگلیس؛ نروژی‌ هارو به فنا داد؛ وایکینگ فن‌ها عکس رو میفهمن. برگ‌های هالند از خودخواهی سورلوث ریخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/25543" target="_blank">📅 20:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25542">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlta18X9RDKHdT5ctvHdXHZJeYtW1mCawL4hLOjuDMo9LApgJ4k5gLa84SeBnniJ9I-lN8s_D9klpmH_va1ER2us0oGdGDhLOxNdD_0eISvqduxgftTuMRhZxRcUcbeMuVmM8wtDIlWLdyz_cHnZVCi3mEyxBKBXYKjd7lmPHY24eTy-sP0ivYXHe1e3UEz10Sysl9XjJ2puRxa9lRorR7WeI_LNKgH-asqqyYATz8B9HB7ccDDWc0vlTbB_65gqCc6pYayqLIt2UFtrHzrGJrq4WSZv-Q9GvbKhGdhDJWsDZT7pfaV2OPyGFmArX0WRQwxdZaj_JtA0ivg4CeeHSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دو انتقال مهم امروز؛
آرسنال 20 میلیون یورو گرفت‌و لئاندرو تروسارد روبه‌بشیکتاش‌داد و مارکوس لئوناردو ستاره الهلال هم رفت آژاکس؛ هلندی‌ها بابت این انتقال 17.5 میلیون یورو به الهلالی‌ها دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/25542" target="_blank">📅 20:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25541">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/104d086276.mp4?token=JLoAyFFCLKXF6R5VT_H7rVSTEVq1IlFpLoCoN59_AGL1LdBgZkqralzYqGqvRpNZ1kJmCMaQfoEzMaRy1u8mX_KcjH_FeYVKmb0u7Hj3CCjRgZCDbzffa2fcBRm0w8sRXVj87vT-XgHo8yv4MaixFMpji5ktMeBimJocaBN_4GlhQEB7I5bdfv8yB42Zpp1hgoHGv7bjgpfEVgxZ8RhJXtv0PBEV7DTL43iGW0dsab7AGQUMaVbxLRF1cl9ErJ9TT8z_rZ--f5W_iV_6KPqzta3wI9mnZ86yUYi866OvpPCy-0-bUfRqS88mGU9HoKDGuIe4JftEo-pOH4ymx4R7Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/104d086276.mp4?token=JLoAyFFCLKXF6R5VT_H7rVSTEVq1IlFpLoCoN59_AGL1LdBgZkqralzYqGqvRpNZ1kJmCMaQfoEzMaRy1u8mX_KcjH_FeYVKmb0u7Hj3CCjRgZCDbzffa2fcBRm0w8sRXVj87vT-XgHo8yv4MaixFMpji5ktMeBimJocaBN_4GlhQEB7I5bdfv8yB42Zpp1hgoHGv7bjgpfEVgxZ8RhJXtv0PBEV7DTL43iGW0dsab7AGQUMaVbxLRF1cl9ErJ9TT8z_rZ--f5W_iV_6KPqzta3wI9mnZ86yUYi866OvpPCy-0-bUfRqS88mGU9HoKDGuIe4JftEo-pOH4ymx4R7Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کنایه جواد خیابانی به قلعه نویی و کادرفنی تیم ملی به‌دلیل‌عملکرد ضعیف در جام جهانی: فکر کردی منم عین مربیای تیم‌ملی‌ام که 180 میلیارد بگیرم؟
‼️
هومن‌افاضلی‌خیلی‌جدی‌داره میگه فکر میکردیم که میتونیم تا فینال جام جهانی 2026 پیش بریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/25541" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25539">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2qRFCsvvmoXcPcpaOteUXJB0Q86EKl_YlbmeYtyuzQJsWu97wxWzFRnE6KeclpDNEFzrJDMRUlU82eXvi7Jjc2jDSRp748RqKSLWz20jcDs61OQXEwO7hOcbAqZhdVwbXQ381Vu4FrjBFTLejA1OYrK7yceK7KKXdoD0Y7d7bpAUzHNBBzK2PHP3hCX0TA13FE9AUGobxhS4J6t7EnkhBTNi9zO1oUIqcBBXqEGxvENbQ-X2GLNcjYIrSuVguWwf3FTZV8IOSUIdmGMxRyZsHUIffIHIhHZG9apIkP8TogATGOK2eIS5zUqOaqacXDHAo_fXXVxlb7j1J1i6BmiZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/25539" target="_blank">📅 19:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25538">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmHK0Nv7Ar_sqCUtuG_HRUv3m15unE4eR_WEV5g7n0uIfnA-sDTKa6WHlNsx_h9i9q14YFS5UEExjZIBddGeE_Pl_j7QzIThpn5r7JRi3D1Lre-X2mhXc4x4yGjb2kIjA-C_QCIQ964k930p17jaD9MEbE2DjxwmuXqxROOsmJ0shmsAyjA0-alvQZJ07uV1gyXV2P0Ar6Vak4D6Ar6QciLHG4tJ9waVdzO9mZC7tHXnBTO00Uswo4JSLgVORZkc8RPLcol6CSqCyWdHBQogKlDQPSRjkGuqCQTzB6VNcPIvTXLq_YSmDuQI_4TpggPiH2CZcSNNWVScqttQlkV4nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسینی در سپاهان موندنی شد.</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/25538" target="_blank">📅 19:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25537">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QT8lysGTSIcySF5T6-moibako0eIPYYtwpqzqet3cdYaa2vsy2jSXd1Qy2b1W6nu8e1RxEmjBLkM4z03OTKHhV5E0yjt5X9Tpvy_Pkd39VvueivwqYCAy23e_4DVSaQ9PFXBYMwBwoST2fGlJ_x02KTI4-Q3JKGtes8xJtEtC7c5612f7bALddACDLvs3Ei-UvKgYvylBbGG2QTmF1-pUo8OBzG4_VYe1Y0oJdCzph3giM43Nl2iWurdlFb3xrkC5gV_hzK3pG5F5j70UTfhFdj0hSSI94DD11ecL91xVcLAiZc-nL2LGD5DDf3dVtKV2ErkufsM-Xfd1ylirzMR9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/25537" target="_blank">📅 19:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25536">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146af45fcc.mp4?token=BlNTkQsQs-M7BMVSqdtSnsr8uVIWOqJTom4bHGu1nx_XjpFyeO3lMEMq_U7IY8TCZvjFWs0mqa7XbCTJwNxdI_0AFyFAL6LfSeTCBwWoewDhkZqmHXNDho0eeqerL92q8yNz9_Vjx5CYcSezG13W4RX53Fzy08Zc-fV7yk_4SI-SeVISyBWNXMknzgkDuJpIujA-9CuG27_NTd3mzfP725L9Hp5US0e0zO0xOi-_IB2jqYU7MvaVjJzl0eznh5RWoPA9MT_jyEIDOjx6s2GF1SGC6_Cbwvp_69T2_WlIwxpvoaC-hMSTBLFpioVfWXptq7INoaAVwM-xBZHA4FNcwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146af45fcc.mp4?token=BlNTkQsQs-M7BMVSqdtSnsr8uVIWOqJTom4bHGu1nx_XjpFyeO3lMEMq_U7IY8TCZvjFWs0mqa7XbCTJwNxdI_0AFyFAL6LfSeTCBwWoewDhkZqmHXNDho0eeqerL92q8yNz9_Vjx5CYcSezG13W4RX53Fzy08Zc-fV7yk_4SI-SeVISyBWNXMknzgkDuJpIujA-9CuG27_NTd3mzfP725L9Hp5US0e0zO0xOi-_IB2jqYU7MvaVjJzl0eznh5RWoPA9MT_jyEIDOjx6s2GF1SGC6_Cbwvp_69T2_WlIwxpvoaC-hMSTBLFpioVfWXptq7INoaAVwM-xBZHA4FNcwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلینگهام ستاره انگلیس در پایان دیدار با نروژ:
مادرم یه هفته‌کامل بهم میگفت مراقب زبونت باش، نه فحش بده، نه به‌داور گیر بده که کارت زرد نگیری. آخرش هم مثل همیشه حرف مادرم اجرا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/25536" target="_blank">📅 19:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25534">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHVBM1Osdcs32c4gYd1_TwttiU6nhkWtAYJQXR2Tam3TbXnVrQpT7ulbaSuhewIEBYKtYShD4cmUX7HTjM2Gl-fZ0pSePrr-Uy_StuPWecrilG2FDR9AMEyMJ3r2V0Ix0KLehRFYZYt7N0Bxg1NgweRN7d_dECKbHA-sGC2ZuTwly0lkYNXcPLFmRI7tuso0nJ0L_Aj2uBVry2c6ELY107sJtMpq--Bx0dVpIXHCeG5gjYtCEydIPc-mOWokGdiorjzjwi8V0HzZtpqELgJZWYDS91rwnvAe4mMikQ-lKodgjn0DJWXrXOX3EwgUZxLiV1biAyAmqI5xUFDXgPc62Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوسمار ویرا سرمربی‌سابق‌پرسپولیس در انتخابی عجیب با عقد قراردادی بعنوان سرمربی جدید به دوا یونایتدبنتن انتخاب‌شد. تیم‌یونایتد بنتن فصل گذشته درلیگ 18 تیمی اندونزی‌رتبه 7ام راکسب کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/25534" target="_blank">📅 19:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25533">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iyi03NHvRJKZWB8-FK86aXpbipTzw2obiaQerUYCwKWF_PT4sw4072m0MDWEWT150XK31QLz2s7YeiOn4uys3_QllsWU2cGkFelUw0X3pz0QIxay0F9D5a3z5mPrSK4XGXyT5_Dv7scMrVRMiCKkXTyyQIdp50ks76EXkCYI9QwI4KF9R0O0mNXxpuOOb0R7Ws7bWlAc-2OeXcZq_NU6U6CBtBSC39zr6unzb5LhQ9hgUXGeYtKpR0hcLbMhfHtn_Xoz4O2t8zmqXlVNXnZ-s5_eIBxHaxNUnCYF-Tx-rzn_JRFPQNqma5u6vVvxR786VWPYzJrt3M1z77Gtxkf29A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برترین گلر های فعلی فوتبال جهان که بیشترین فالور رو دراینستاگرام‌دارند؛وزینیا بادرخشش در تنها یک بازی‌مقابل‌اسپانیانزدیک 16 میلیون فالور گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/25533" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25531">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nm4dKF9netNceUd1VQonlbmfyjr-FE8titpYNJ3BPLMOQlHxh043OXgcEZNnso8szDnNS92X4NbQ3X-26w2JH69VQiLNIpgRfZSJxFAfjz07nyDMt9Q8kVe0lYZx99E2bs7zsW5k5D57F3iTX9r3WQb_EoozphQ3kO4Ar0kgjj3EdL4GuRyBxRzAz6wjKyuQWbYaMGt6zP8v-seUHRujnBJgSlgDfchR26QEB2MdAY84lu3YGEvLQZ0NP50jrAYKC2iBIqS2aV5DEFlYcRa1UjlJ0NkcoVw3q5cCVfiY2oYUkEkNl1lIbMmUKbQuBD8frCtpNXoTrkAY-aD_pmG19A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec951e804.mp4?token=sqrRDSudeuhmXjY9ZIvXPAGWlr_JAYczpXmhgMWgi0kehHwZVzQbUaQgCiORt8sBV_ll9cDjur0hPh4EGxxgbs7ium4msfBGwTZn29HUaL1eJyEIzcLeCSRtF92gB6EIOTh8uodaIpx60kjygbyNVYoS_KUqZ62auRn_WVUVlf-ywRoykoJeefxnosoQ7_nXLeoJRfSNtZPj3DIp0ImbaAB7rJySyScrzFxQ9XQ-f0INmcLxLmGbT-iaQ7MLS4WKoXT-FfKn6XTHoDoTxoBOOq1x8siwQ3Y4VtIMabob7fR6gh2EiOLaWrE8DS51Zi8yFwtcEtIeiJD6OCTCT1aPcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec951e804.mp4?token=sqrRDSudeuhmXjY9ZIvXPAGWlr_JAYczpXmhgMWgi0kehHwZVzQbUaQgCiORt8sBV_ll9cDjur0hPh4EGxxgbs7ium4msfBGwTZn29HUaL1eJyEIzcLeCSRtF92gB6EIOTh8uodaIpx60kjygbyNVYoS_KUqZ62auRn_WVUVlf-ywRoykoJeefxnosoQ7_nXLeoJRfSNtZPj3DIp0ImbaAB7rJySyScrzFxQ9XQ-f0INmcLxLmGbT-iaQ7MLS4WKoXT-FfKn6XTHoDoTxoBOOq1x8siwQ3Y4VtIMabob7fR6gh2EiOLaWrE8DS51Zi8yFwtcEtIeiJD6OCTCT1aPcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/25531" target="_blank">📅 18:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25530">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2121b6e4e.mp4?token=hXTGJqEWJ4CmsAnXhFr30iXXUfqRXqVNzZTaiO747OOAVydX7PtpIvtJm8ft8o_nV7Fs4Jj3fQynLUsX3xDVMobqs3nbh0dM7gV-hFn4IWhI9hutV-b8AVA0Of2CD-CNGl7AGAYJavoCDLhrYctgpexwqmTqv7SGVto92ekdFzaAS2RTjBk0tC5yEz1NtmNv0dss5rQ1kW1Z30DrstzBJ2oEwprYPcnJEguZpgDMBkUAKuSkNZjozK2-7qigXhR_Tfg-Bb-NXQBA1GaR44t_346ZLcp8ZHegLTp-X6ayPFGN7pg-bs77RAlJzgkk0B3UDfY0tPgxZA9nHdZhGpXquQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2121b6e4e.mp4?token=hXTGJqEWJ4CmsAnXhFr30iXXUfqRXqVNzZTaiO747OOAVydX7PtpIvtJm8ft8o_nV7Fs4Jj3fQynLUsX3xDVMobqs3nbh0dM7gV-hFn4IWhI9hutV-b8AVA0Of2CD-CNGl7AGAYJavoCDLhrYctgpexwqmTqv7SGVto92ekdFzaAS2RTjBk0tC5yEz1NtmNv0dss5rQ1kW1Z30DrstzBJ2oEwprYPcnJEguZpgDMBkUAKuSkNZjozK2-7qigXhR_Tfg-Bb-NXQBA1GaR44t_346ZLcp8ZHegLTp-X6ayPFGN7pg-bs77RAlJzgkk0B3UDfY0tPgxZA9nHdZhGpXquQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسی تو نیمه اول با پینیرو داور پرتغالی بحثش شد دیشب: بامن‌درست‌صحبت‌کن، بی احترامی نکن. من باتومحترمانه‌صحبت‌میکنم تو هم باید همینکارو بکنی. انگار نمیدونی‌چجوری باید بابقیه حرف بزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/25530" target="_blank">📅 18:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25529">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0b0e1c0d.mp4?token=mr2IuP2M0p3UJttxJr5Q0vB1qUfZebylnA-BuiIBhJJk5GbAulX81006LP_K3G2_15RAaYLldK27cKLCH-NaGiQjmUFeZX4hJUVA0QTajclOQ9h2CofH1K-LvASm5vCxBV8C6nd9tMccs5P1gqRFRKz1e4wu_i37iFFFEjfwyc_kmicRiQGYP5oQlDNNkDMalklzGO7XziLuroHXESno5UefK_IUb6bS4UTWZ3iURbU_MuYHNZkdHFwhrkR6JHj1RDhxthnpknOjBhn9GbEAJ04LWSiMqvFFX24xRXAP5USsicKr57lmOf1mtsnOeGTypH5ETS6Lmuf-alqwG6zgIzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0b0e1c0d.mp4?token=mr2IuP2M0p3UJttxJr5Q0vB1qUfZebylnA-BuiIBhJJk5GbAulX81006LP_K3G2_15RAaYLldK27cKLCH-NaGiQjmUFeZX4hJUVA0QTajclOQ9h2CofH1K-LvASm5vCxBV8C6nd9tMccs5P1gqRFRKz1e4wu_i37iFFFEjfwyc_kmicRiQGYP5oQlDNNkDMalklzGO7XziLuroHXESno5UefK_IUb6bS4UTWZ3iURbU_MuYHNZkdHFwhrkR6JHj1RDhxthnpknOjBhn9GbEAJ04LWSiMqvFFX24xRXAP5USsicKr57lmOf1mtsnOeGTypH5ETS6Lmuf-alqwG6zgIzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیوزیبا از لحظاتی فان و با مزه لامین یامال و داداش کوچیکش که این روزها سوژه رسانه‌‌ها شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/25529" target="_blank">📅 18:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25528">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPoD2Tq8mNs9nAZlbr9UNWNJAIqSGuJXrWTNk_Zu18Yhu9YMaOdbnH7kNkqW7c2k024jKqT_KJRBRTVF3LDYNrmKzcEfARX3xd1mzeNHH6WEtWf2cJ9NoaS_soFIEe0rdVk1075AWxs9DmlWYqTA9FuaUmB_soqFKXjZrMWY6e5Bf_dtLGp4Izbqecfqzyf6fvDKViUQ_SeccpHYYfK1bpc5i5o4-X3YMG6L1gPt2maibCea4irKVmIkTm27npgkp0naeN_gZdQryEjkWj7DOWYXNA6ufarMhXZK1pa-WiAccIJJC_aMgxhPwanDg-xTA52x4ifXtm4wn_nIkJfKaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخباردریافتی‌ پرشیانا از اصفهان؛
مدیریت‌ تیم سپاهان‌ با‌ حسین ابرقویی مدافع میانی 29 ساله باشگاه پرسپولیس مذاکرات مثبتی داشته و درصورتیکه حسین‌ابرقویی بتونه رضایت‌نامه اش رو از سرخپوشان بگیره راهی اصفهان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/25528" target="_blank">📅 18:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25527">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‼️
تو یکی‌از خانوادهای‌عشایری یه دختر بچه حالش بد میشه، بعدمیبرنش‌بیمارستان تست میگیرن میبینن باردار شده؛ میپرسن کار کیه!؟ میگه پسرعموم، دعوا میشه بین خانوادهاشون؛ برادر دختره که بازم زیر سن قانونی بوده میزنه پسر عموش‌رو میکشه، میبرنشون دادگاه خانواده عموش…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/25527" target="_blank">📅 17:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25526">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZQumKjx26UpqqAOTYbfEpRrljlXPfesSi_6u0FN8efem4n7tiWGVTsyjb_64pb7tmzvxvSFbTEVgslZpd7OQ4nHes-Ji-_H2nilTVFLHrLsA8p-ZPXlWcnWTgoryQH9RJ2Z_KsKSGxng2RyJ2xm1MFdbHaP2UBBB_3Rp_XTqdBk1ev7rgIEru-a7gKXbp3ApAyxeIPCDF8KoSj2ciQGJUh6mILmEHCuxBvMDJ9ja-nvJpfckG4FJ3kyvja-K9zmBn-hsd1FeLBvo8sLruBiXinz3VNToOsQZ-dI-cKIvtNSwUjqhUARaON13ob0NLGhNG_0tNIJT928USBKTh1cCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تقویم
؛ پنج‌سال‌پیش درچنین‌روزایی؛
مدیریت باشگاه استقلال تهران هفته‌ای یک الی دو بار از سجاد شهباززاده مهاجم جدید خود رونمایی میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/25526" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25525">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmAHBY5sCU8uBAqN538y_CH5Up0j0uNrulI0dnlK03greAV1Y89HhPaNDBisucl9YPLlkH8_L-PE4BmV1uFCOi_6f6_b0QigEhufJGKl9jEOaa3Yyh-XsIS8EACmxhpqEmyKJo7ZiBFt1M9od-2pLbMV_5iYHRekYFVwRxQTwMurnmiMmnoxAGPYAJZLUCWjDRnzBqv5ZcI6GfUxgRTg2FmQ2lWN29nmNZpm2Q6wBs0ptG5TcmJakirjah7vnJJUkcSMbs2CoNF2gd0YiyWX5ST12StOnSp1ssHY6xu7ekHzxOtgcZ_hFCDcW3d49uomzAqskvTyktI1RewWe7RcRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/25525" target="_blank">📅 17:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25524">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqOZU71ORilO7d2VasL5btJ1pauFafUYnvUQLJk2Q12KtmD7MF4T96qs-3JeiYMPTFLIqY3o-eZT3q3orEZLcZO0Y0860fAS5-jialIX5gRaXfstRDmFv3IhcePuA28Il20aIbIX_OkDfl7yh-oNGs7mmMT9oY2FwucBXWhLfVQSuyu75vOVut265YTcEA9Dg3AYsW4UETmaQV4YmFiuph7RTmTib5eAjU2i5GF3jDO_E7JiAgv1cHSiX0VFHtSbpGEHYtPhYWMzn_eFIFHCZorYyJzfa24FeW6wkqfj-8dtdZyvNOWZKs7U6MPUqchr-N4O4stu6InLcDkLag8Rsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
عارف حاجی‌عیدی هافبک‌جنگنده سپاهان که مدنطر مهدی‌تارتار و پرسپولیس بود بامخالفت شدید محرم نوید کیا در جمع طلایی پوشان ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/25524" target="_blank">📅 17:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25523">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9c9cac2a.mp4?token=D0a5folWIUZNOM5ZUgJwBUcrvEfUQo-3k2Kh2kStte3n895AhmUMD31TKKZUcrNJOZ5Unym16ClJN_aaJXaQXC6cqI7mV8Rm22PIhgIq9Efaz-kHGPs0EbRooDvPn6hWHtOmZLHK7y0s8h4eXDWKr5OAkFhBqKoZ6n5hasoCUR1iruk7evwOH6cEpkEigg2AJRVQrjDY2oYDsw1L_-iKO2bFM6H67WjzNzH2KZj_MzRhYV-_xyERmz4oELjJtNWPcH2kk5rmCrt8IERkFl0ZYuYrfl78QyatNu6Jld4cNHd3vuecppiuT5Zu3ZRLAg3sIw385YVkLsIC3m28X_4sZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9c9cac2a.mp4?token=D0a5folWIUZNOM5ZUgJwBUcrvEfUQo-3k2Kh2kStte3n895AhmUMD31TKKZUcrNJOZ5Unym16ClJN_aaJXaQXC6cqI7mV8Rm22PIhgIq9Efaz-kHGPs0EbRooDvPn6hWHtOmZLHK7y0s8h4eXDWKr5OAkFhBqKoZ6n5hasoCUR1iruk7evwOH6cEpkEigg2AJRVQrjDY2oYDsw1L_-iKO2bFM6H67WjzNzH2KZj_MzRhYV-_xyERmz4oELjJtNWPcH2kk5rmCrt8IERkFl0ZYuYrfl78QyatNu6Jld4cNHd3vuecppiuT5Zu3ZRLAg3sIw385YVkLsIC3m28X_4sZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هومن‌افاضلی‌از کادرفنی تیم قلعه‌نویی:
شجاع پاهاش پرانتز برعکسه اگه پرانتزی بود پاهاش اون گل‌هم افساید نمیشد ما میرفتیم مرحله بعد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/25523" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25522">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=oBuYJHdFlRMGumMPQU89r8LLdug22zIBasq6Xnkz7iHqrLXPRO5yWlOJK2E55065D1e2x55FZVbVuh9bvkgsForuezMyJVy25s_RqH2KwOua43BrJEx7XXR_2HQvjh4NV7LT4PQ_ta2MOkhjfp-K1EJZybSPqkgHtl4UaJ4MeLat2D3zzqWYzTmkNnKLKM53jINIQa3HQ_UIGtXba2Cd9hp6vhpNSN3AHYAPJIsOw-QqGgOg53WgqJ0TidRNOiRAjLSjmyuSnS19yS298x_5kVF2Vv0-ngaEvqFsiX6mPEi-GkR25Ax76bjSo3Nq9vhfBM3Ka13nvMAUkzhy4h32vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=oBuYJHdFlRMGumMPQU89r8LLdug22zIBasq6Xnkz7iHqrLXPRO5yWlOJK2E55065D1e2x55FZVbVuh9bvkgsForuezMyJVy25s_RqH2KwOua43BrJEx7XXR_2HQvjh4NV7LT4PQ_ta2MOkhjfp-K1EJZybSPqkgHtl4UaJ4MeLat2D3zzqWYzTmkNnKLKM53jINIQa3HQ_UIGtXba2Cd9hp6vhpNSN3AHYAPJIsOw-QqGgOg53WgqJ0TidRNOiRAjLSjmyuSnS19yS298x_5kVF2Vv0-ngaEvqFsiX6mPEi-GkR25Ax76bjSo3Nq9vhfBM3Ka13nvMAUkzhy4h32vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل فردوسی پور
: آقای اژدهایی، خبرنگار صداوسیما وقتی‌صدتا موشک‌خوردیم و صدنفر آدم کشته شده ‌میاد میگه که همه چیز عادی است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/25522" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25521">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4009214e91.mp4?token=E88X_iDvQLL0u9NC-JDM05S83JqK5LM0aOA0b10zkzRCy36Auj-JQl_LchpHtsM9t-9iSxgb2WpCd8LhenhuyXpKqm7cmCqmlLY1Aots0HzIkLyNLzcc4D1G8cWOsUC7FBKL6vdpSTOHVUSUQ3-PCikAYFjIfYh7Df9PpkcTxRtUFb3KuNkSHCRTyytKGPpeeIZhK5FTuTvTMKv867vxF8rjJQ6u8qMDB7LufjO-0TjpQvnmWOHPpF-4rrczo2Wf7a7wpJnPh4AdIrt-3Ps1YBnRTM0O4jm8K4qwIhGfYgaaPga7ojLsHQRIMhjDI1aBfI3_1BECLldZ1YF1Dnj7SA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4009214e91.mp4?token=E88X_iDvQLL0u9NC-JDM05S83JqK5LM0aOA0b10zkzRCy36Auj-JQl_LchpHtsM9t-9iSxgb2WpCd8LhenhuyXpKqm7cmCqmlLY1Aots0HzIkLyNLzcc4D1G8cWOsUC7FBKL6vdpSTOHVUSUQ3-PCikAYFjIfYh7Df9PpkcTxRtUFb3KuNkSHCRTyytKGPpeeIZhK5FTuTvTMKv867vxF8rjJQ6u8qMDB7LufjO-0TjpQvnmWOHPpF-4rrczo2Wf7a7wpJnPh4AdIrt-3Ps1YBnRTM0O4jm8K4qwIhGfYgaaPga7ojLsHQRIMhjDI1aBfI3_1BECLldZ1YF1Dnj7SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بازی های جذاااب
جام جهانی فوتبال
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
⚽️
🔥
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🌐
دانلود مستقیم اپلیکیشن اندروید
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای‌مطمئن و درکلاس‌جهانی پیشبینی کنید!
برای‌ورود بسایت‌فیلترشکن خود را خاموش کنید!
▶️
‌
Link
🔜
MelBet1.net
▶️
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/25521" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25520">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=M3gfPj0qur9j9R_4fVk4FF_RUlKj29xInrNnYqUN7GT7soVoy2h_-d1Saoto57WqFFFqKLaA_2RRxHMErJtoD9bR8A8YghQhGhgFs8X9XT6gvbAxg_894Ew8s1GT827LRdk0CpjoqBTBybF-NiRaNKWSeCBZDwbFm7BPRGI2ioTAvy4fvPq9nIYRv9An6OkwPCQY5w6hdCO_d5E2wpMDTu8gbaSxRLM2Bn7Bwwgsce_XhBVDPatCJrpS8IgvsK5NhsGKC1XXEKdx6vNsmKVF2SOCNt1LWNyNnmdznbe6TXLYwmtQPAQQzHf4d7ESRTqQ8tLYyavp_vtISgbcTErkew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=M3gfPj0qur9j9R_4fVk4FF_RUlKj29xInrNnYqUN7GT7soVoy2h_-d1Saoto57WqFFFqKLaA_2RRxHMErJtoD9bR8A8YghQhGhgFs8X9XT6gvbAxg_894Ew8s1GT827LRdk0CpjoqBTBybF-NiRaNKWSeCBZDwbFm7BPRGI2ioTAvy4fvPq9nIYRv9An6OkwPCQY5w6hdCO_d5E2wpMDTu8gbaSxRLM2Bn7Bwwgsce_XhBVDPatCJrpS8IgvsK5NhsGKC1XXEKdx6vNsmKVF2SOCNt1LWNyNnmdznbe6TXLYwmtQPAQQzHf4d7ESRTqQ8tLYyavp_vtISgbcTErkew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
شوخی‌جودبلینگهام‌ و ارلینگ‌هالند در حاشیه دیدار شب گذشته انگلیس
🆚
نروژ در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/25520" target="_blank">📅 16:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25519">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oq51a8ytesgIiIJzIduduT4jmc7R1tFrDq2evNI8pz8T1eh89SU0y8DVeYbKe7FStUO11h9IC1GxvsAOl4MO5sT2i6XjxK0TGarYArozHWX9jjSRnwVPcC_XnVAQPrDzunafvSNu395YH1u-Gr9LDhL9MyUSa4jYNjxExlFtZyxg6zA4FJ9hqw5Jg5V2vhl06QjyKeO7qrP7FMG8wrpstrIeFYB740oZsL8pxbVDPkWrjf76QmCtGUcPk7fcWkkqukG9U5abbpNnNHQ9ddQeGgHcmLUpFim4lDOeuex0_BRjxrxiqQu78GHcIaRCOg4Srr5eIueaA0Ejp3ZtsaxRqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/25519" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25518">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEzz7l1TrbKJBSz4ksbS-iBaAUaqLETpx8ZrZEw42SanaaxNH1au8eMIR5VSO6IxM9s5BrD0IB-WpPIb-5QwcdqGSGq_5AXFrZQKVc6nl5k2osX_e2Spr8GlWDtqkMHhKtR3VkWDvwhJdLnQ05AyTdOCq6_967qyx5XF2HT7YtCPFeZXZM_kjGMAjpIO8fyKNSeWpgiG9_3ZmVe_bMjF71oXJB2kqw00VzOENqyZlnPYTBTZLXQEbQMU9hbOQodaISC5Ii0lnck_AbTSa-h-eR4l5jxsNKLbO0wvij04HFgeSIStj2X7VidxvGnZkMp-WH4OklQ3ojuSKv3qk6kAbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دو تقابل جذاب بامداد امروز مرحله یک‌چهارم‌نهایی رقابت های جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25518" target="_blank">📅 15:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25517">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HR-Ya7jPtEVUDY_6o7KAptaCbjNhVifM2rkX__-HBGjI_sk2sAzjZxBapvG9_lKJdQYfaSaThkEh1_5RXInbifakPw10nx-yYCSCuEcBnQIX4phN5a61f-Yq2pCjQbJN6KsKGaoY8gvUW7k7aWteJkNhcgOr-LcpYRu8q8AecHr0ePN7w5Deu0W0lp8xNh0SBm3pzgCBnKDlx46E5DMhplmOnYuxaNWbwTZQ6VPyXPY8HFVHMDG2FmdSS_Z-zjSe58KYUuhx5cLdHDH39PauFpUZbDOH3dOPfanJOvEcTnkQ4SDSWBot8XDVwj9vhc-iayeD5HlwOJ1HrJgHFOXnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی پرسپولیس؛ بعنوان سرپرست مدیر فنی سرخپوشان انتخاب شد. نهادهای ذیربط مجوز افشین پیروانی رو صادر نکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25517" target="_blank">📅 15:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25515">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25515" target="_blank">📅 15:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25514">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsYI-he_HZoYeeak7KKBSfQWjzVGvOabKA-ZMEw8qXY1aJAzaC-8bayX0Zj0HCoFmWlchXS4UPix7zh968aeTOPZA4U8lqrlFxDstR2VFUEEwXKLprsy6dzSLeJwCxwrcINCEnNyJT_rbNQXnzYs54-VsHCPSvcdHZeOrMVGka1UV9mbST7XQOQqZ6-xkRtciYVuckM8mZJQr9uP0ZwFIjzUy_4ftrc6hTAKCRBfpI7Nh_4lSBOX7i5PNs1itbGJMte1waRAESKPM21gnSqn2COeag2avJdGE0rHdppEBD8dEZSJWHTgULFwMwzXgmcQ8dShJ7Pa5Uey0kZNuuWZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا
#فوری
؛
یکی از بازیکنان فصل قبل پرسپولیس از دست مدیریت این باشگاه بشدت دلخور است و به دوستان نزدیک خود گفته اگر پنجره استقلال باز میبود تا حالا قراردادش رو با آبی‌پوشان امضا کرده بود و یاغی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25514" target="_blank">📅 14:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25513">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vroh8Ynj6cWDEzcv90TfAw6mWBgbh8Zi_TWif1hYZD_3_FjOaf4CHelWKF4ppNMNLTd0EISyl0J6JXbRWR3uvI9z5wTWcJeC6GHMZCpaL40rlS4oatLm6BUIDSxPLqHUg5b4Og_vLFaX8bEcEqYJVJyRGNtkgBfnkerAHiXAB2mmGXx26P49btPQJddh6QhuTCGW2ab18Wv8nkTQDW2PXlhLzbKdGcW9byjGr0eXa8mEnJqhsQL0X45gLo4Y5N79r2WfDurIOOHy3UdCmN6JUiuWGWLlWYdvgAZMhpigTzu-e4CD7DBrBGnVHNDBY4CgAXS2FT3vNqBPeRzzq96j-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25513" target="_blank">📅 14:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25512">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=WaArUAwRCY0s1JNqpV7IBYXbuz6bTWdnzNvjdSwocTVSwxIltRzXhwnM_L_J3_-nxNw5gYjuhpz2xRVt8SSu-HrNFfNp3w-hLbkw0ReZBfP1UbmbfQ8X8vJ7okomP8wYlGSIop428T5mHBzceRaApI0oJbMSFdlaEGs55asStFNbfXZw0QniUVc3RFWIdFZ1f2hSQfq2mYuJfc8C8h46BR3csbaU1SxqOPRw7bw_-0QoTnkSS9CAKnqS3G_hJ4CqMq0YxxwP4L0F4skZiTrZjLULCf4mzVznmCwUsI-4A4I1auNL1A7TGLW4aWRTMbEwqTP08cM1M1paQOZh1xy5RVKDI5T9sqE3wk-uVKs8rsjYq1J8CXlDhuvPs-0f1kriQIMHV3moLOZTVieALQn67J3FWo0bBh-5433FM3yHLY1vNR0v48ZG3_TkQotycM36tVMrtAyhp09mAVxoVa2lzsVVsMJIoSdRSwajmA4GTjWf54pqBIV5vfrvbnlUNjQ-I-IdJHlaicwPgBPM27vXR5Y4da6SX71qH01rzODZVWBlblJDqPfL5g0_bfx-p3oywgYaEp2NAm29OhZoawj6L7qlKWb-DsMhLvJx4_moau35f0qzGam1Zvu85DSNxF_i2M9AkAdCDSeWNJrjQSFvr0czCntyRHcloMMB6Grct3Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=WaArUAwRCY0s1JNqpV7IBYXbuz6bTWdnzNvjdSwocTVSwxIltRzXhwnM_L_J3_-nxNw5gYjuhpz2xRVt8SSu-HrNFfNp3w-hLbkw0ReZBfP1UbmbfQ8X8vJ7okomP8wYlGSIop428T5mHBzceRaApI0oJbMSFdlaEGs55asStFNbfXZw0QniUVc3RFWIdFZ1f2hSQfq2mYuJfc8C8h46BR3csbaU1SxqOPRw7bw_-0QoTnkSS9CAKnqS3G_hJ4CqMq0YxxwP4L0F4skZiTrZjLULCf4mzVznmCwUsI-4A4I1auNL1A7TGLW4aWRTMbEwqTP08cM1M1paQOZh1xy5RVKDI5T9sqE3wk-uVKs8rsjYq1J8CXlDhuvPs-0f1kriQIMHV3moLOZTVieALQn67J3FWo0bBh-5433FM3yHLY1vNR0v48ZG3_TkQotycM36tVMrtAyhp09mAVxoVa2lzsVVsMJIoSdRSwajmA4GTjWf54pqBIV5vfrvbnlUNjQ-I-IdJHlaicwPgBPM27vXR5Y4da6SX71qH01rzODZVWBlblJDqPfL5g0_bfx-p3oywgYaEp2NAm29OhZoawj6L7qlKWb-DsMhLvJx4_moau35f0qzGam1Zvu85DSNxF_i2M9AkAdCDSeWNJrjQSFvr0czCntyRHcloMMB6Grct3Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اگه ایران میزبان رقابت های جام جهانی 2026 بود؛ این مسابقات جذاب چطوری برگزار میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25512" target="_blank">📅 14:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25511">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdDmRaKwvehqe0OxtAsXvqsND3sOtsGiD8wQrI-NB1qwZU2GHNd4uuxbzWVxazLwZqZTtVqsXXfb6XCGabyhUbldXjm_uH8YKJhJDYVIYOfiie2F123bN8zu0BzfmsV1M1xopsSt0LOJF87x4Ihx5iVt6QKEZtcBFO_q7dTv_TGvsJqRspedwUB3DkOGsM-4OAaGTDbeC0ELIkuMbSkwQCZ2jwWxaj7J6ybayPa3bmVu3PJvIVoQYl2Z_2kYXuDiSOQSUP_oDcX_D6jOqkWAOAw61qiALM5NViNnSXLKvwGGB---gcpMQtd6J_iCk3kpSJJoacMyYvlrjghFoexJfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25511" target="_blank">📅 13:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25510">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1lSpETA1Hzy7ApcS7leSEysoZ-SekuIkfmC0cpUGP73kyBOtVJzQslNefVuIs1gHUhLWkdnk2fIYoNJsAFN6Km-fjGeXVvGKDxepSt0eyGIW7QxZRBIxGnN5blX94r-zGkwV-p1-3nXtXsstk74ZOGeRCursKErjze_ld8q719tyTLFwSKnAaTPrN6oKDdwWvCHlmkIAo7kRxxGUrKxlekpw6qyRrl7pwXJuWne-cNiSWuLJ10Mf-9vvwn3a4p6twFuVTfE14NpPxp-Ms6ErcyBya_QPLl44EBCZlJg5f4H6AjFH9BX3WrLNMnHwK9g7RBM4DC2Ua7DUp5GdIJbGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25510" target="_blank">📅 13:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25509">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLKLU6qx9m1NN9MGIZQs2TpJ_xctI63SK_F1oAmAgCdxGUFOlIP53spV6msnTFLgvLnGyIX8A9qGK5Qs3AXJjLhcFlPwJYxnEpcBk22svGVMm7boV6AKr7ZfKDWoiHaD1ZiN003D5SFo2XZ9AVGgF9HwF6vkswfNYxOUFIvtWrI4aqi4Ygc_J5f1byKI4FZBnNCVI3oecEFAfRlLg6GSWpb0bPdzZFMbNNnjPm6BxZQFOKnFE-so-Qwc642RvkJxlLuDU1KFFrLMmAEwah49Y3U4G2EOdo6qbXXoLi1_5PNlcVFbtR6dJBady2GT-HX4_KSRaqFfAbfDUHnFlfjLHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25509" target="_blank">📅 13:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25508">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uh5EH8dhijdLQ6wOwYuCbxCnAaE9SYS9NgrNAygDILktrhnhNuegAANdy9OHesKrjulJwjx00oUdDmvw6A2wael-mClU07pCgSV7Y2Tl7kpUUdzljruE78tidNl0EWX_elN9YTpkqjEzaVEnb2_Sm9klojJ4yohmwqkdWwMWAu5QkmnKNAAsiBsZOMJb7HRx24I-9-D-LLPtomMAm67Y_uPEc3WkuQkBCW_cJc8YZDyJzYBAyby8RXSw0pmUdjM_fnGLi7soX3fY7GMVjehietkYKZzrGBFTEiWfaoMQVrqK8m9pXM6WBR0oxpaqJn0H5bZSk9pR5kPtBvjs1GCz8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25508" target="_blank">📅 12:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25507">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUYJ6y0C_X88HQTuG5ZkIJ_sWH87S0rREW0FGjdcpZEpm7dqp2Q54D684YiW-riEbo-ce_YaV7ydm3oXJQL7PBhnBZCk3DtSd3Ly2Z-p6f_TkNTPuFbBPOse6MMfyLezy2JJe_IXTdIqwTH3AI7P0NDANu3sCw_jHnTJ1wCXM5ywyu3TtWm5YxMorC742PT8JB8wwrGyqaJfFmOM2CoWaA_8eGSq12fRMnxNX4B7g6lCyj-Gg1MaGkvFuqGauOl6omSckVvPo3WWLILl66gTo33Np6crWHo4dEb02QtEPEuH46amGCSvb4zPGzk1kIlkXYJb0Kb_VlyKekgmWlCXyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عادل خان فردوسی‌پور پیرو خبر دو روز پیش پرشیانا؛ مهدی ترابی برای عقد قراردادی دو ساله با مدیریت باشگاه پرسپولیس به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25507" target="_blank">📅 12:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25506">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6pirnEhanEAfdU1fFgMrlDSrHTWqVc9_8CX53tnuyVivvqxBNwVT59aRqjAxaQ3z1nNDHZv_q6gqS4DHE4E925jLKZv2EPdYWXGjaXa9z16Ekk2bviYc67MKKkEMaWlzEyCqPqR7yGjShx_Ca-t1Aeudy5vkljMhhjnGsAA2hw-6c9yExYQIIa91AJT9AJHwyvklPzk1N6K-0c6UmIGICYbC1QXlooidCx8602rrpoO7LAl5xwUzdZ82EHmh16xv-Dd2mHY3Ga778z-k7BacvvDz3ACqSdyFVFiuEkAdRxjPdfaz4JDU0Qbwe7tIdZQux4cqg7svitn8QYZ8vWS7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا
#فوری
؛
سهراب‌بختیاری زاده سرمربی‌تیم‌استقلال روی جلال‌الدین ماشاریپوف نظر مثبت‌داره و به مدیریت‌آبی‌ها اعلام کرده قرارداد این ستاره 30 ساله‌ازبکستانی رو دوساله تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25506" target="_blank">📅 11:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25505">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=SsipUoyPrUHi1SfCueCNb19D-USrWFZICEmRnXrcvtPkaa4yCxPje7cwzf61slJOe7OUcFdOkpvR2DfBayKN9ZUskYgpxDL6_18UfFsMCtKn932WZKZllgabbFA1lbvy-IZ17HxIjQoPvsw0l1A-7ngcNNSZEHH94gFs-ce2VG5kZDJdBrP-4NDuvN0ikY9sOq2XZhQZ5iCvZD3qK28zdQ7LNczUFEDNB8KfzmPTOupbUW4r1ox7h2OZ00XKyF0b7hF8gFgxsqvaT9hygiP5kQVnaikSeUkn-YRYtpfRmnQpMs8cTNPc0div23XIsnBQQLnSdXpdxDPgmDysOhKiXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=SsipUoyPrUHi1SfCueCNb19D-USrWFZICEmRnXrcvtPkaa4yCxPje7cwzf61slJOe7OUcFdOkpvR2DfBayKN9ZUskYgpxDL6_18UfFsMCtKn932WZKZllgabbFA1lbvy-IZ17HxIjQoPvsw0l1A-7ngcNNSZEHH94gFs-ce2VG5kZDJdBrP-4NDuvN0ikY9sOq2XZhQZ5iCvZD3qK28zdQ7LNczUFEDNB8KfzmPTOupbUW4r1ox7h2OZ00XKyF0b7hF8gFgxsqvaT9hygiP5kQVnaikSeUkn-YRYtpfRmnQpMs8cTNPc0div23XIsnBQQLnSdXpdxDPgmDysOhKiXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25505" target="_blank">📅 11:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25504">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgkCuafBk5fXHakIxFsfz0ZEbxDHLlw_2qfmTP4CToEUXCxpFfEf8r-K6Af20MNBKJbUZIEnOVXRrt8BtEFxj58Ar_ckpn_ivTBsY-Gbdf4KxI8FTZ1-beUWJgu0F7MXA9lfRybSa8RD-3bPKJaYQ9zIHMirEkE_Nd16b9dHyLdr2Bz37lOYS8yxKsbsQbnu88qzQd1qlTGTMb10UTMavZRgsPRs91nwxc41Xzji_GxhmmyUFaSurJBtNTvrrqgRmbT0oTLCB38tCfcb5HbxWb-UqNiAWfquWMrQDI9EuDe7WSPPH3iI9anaYBlPFnhKuOPouLiPirrbyKt1GE28Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25504" target="_blank">📅 11:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25503">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mw5MD1o9_sCkorxAy8vGfvwm8NibUrqRqE5TS_S1Iq4b-y7rTJj9uB1qltY61BA4Z9WS0oD5PTa8sZ39dfZOlLBG8SL0B56xwbKX_vZMrjeFigf4ILAtqeQYbQP7T48hc_egiJ3v-aOcdiQGCX2ZB-ZKYQQaV5aFi4CrDouQsGbc6Ypqx60E4TGe7IhIS3Gwb5j6tkeYjdjC5whLhP71R8_vw-GLNlvudhDapK1Y08FAOvUmJmc9J1RfC4DlYUhbbvXPqm6Jhkhfsz37ayOxlW3MV6YWcgHu2Ku9me0o3mdqcocRQ5U0AnaWC4wR-8YT9Yoe33fLr_tSj-UQK__6FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25503" target="_blank">📅 11:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25502">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=jJIOZ4OYEm3dRpZRfLH7wcHsIT9sO136YcCSOYiSKDDuZAVrlMIGQfXlqSGkooMVKanRsBL3tJ6howeWpKMGcnme4RPY1T8vYk0LCS0HD853GIVWPHLwf33xeZ8LGhOLJnlCfsc_cg7g14a6lb1yjkEmGSKw11Uz229B9E-e6XVh8sXPebX9nN7H8EKJry30OoJY3C5tdLSCa-XbxGtdZ0be-sopPtGquwOXhlS7ACzpM9dfFoMZcm9k1EaT_CJaZ2lMsbQERZUX7ryiA-EDi7FX6Ky6e6SZK2nMXIZ2RM3ChxjLgdQLDSf9R11r_mLxD75kLX_TzNm36Ci-xCCbNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=jJIOZ4OYEm3dRpZRfLH7wcHsIT9sO136YcCSOYiSKDDuZAVrlMIGQfXlqSGkooMVKanRsBL3tJ6howeWpKMGcnme4RPY1T8vYk0LCS0HD853GIVWPHLwf33xeZ8LGhOLJnlCfsc_cg7g14a6lb1yjkEmGSKw11Uz229B9E-e6XVh8sXPebX9nN7H8EKJry30OoJY3C5tdLSCa-XbxGtdZ0be-sopPtGquwOXhlS7ACzpM9dfFoMZcm9k1EaT_CJaZ2lMsbQERZUX7ryiA-EDi7FX6Ky6e6SZK2nMXIZ2RM3ChxjLgdQLDSf9R11r_mLxD75kLX_TzNm36Ci-xCCbNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
نروژفراموش‌نشدنی‌ترین‌تیم‌جام‌جهانی۲۰۲۶ بود. جسارت‌وجنگندگی‌کم‌نظیری‌داشتن و شدیدا دل‌همه فوتبال‌ دوستان رو بردن. به قول یه بنده‌ خدایی اگه ایتالیا مدل گتوزو تو اون گروه اول میشد جای اینا میومد احتمالا این مراحل رو به چشم نمیدید. من خودم بشدت فن ایتالیام ولی خب مدل اسپالتی و گتوزو افتضاح بود ولی مانچینی درستش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25502" target="_blank">📅 10:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25500">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9pSD5WDS4E05Z0HYoVCck35J_3XZlLnnqrpLT7gBfjC74QHhoHdTaZ7CXk9owauV1cNXZAEUDJR3ZlMY_vMRAocLtqF70XUdU3naUCYTkGuzgJdqCOvw8v-sfBUFQuOKb3ygmcy8anqM0fe2uRL1nNWx_QJT-ONvDvQYwe1XjbRyt-2QZyoQxtPv7NhRT-HihmiDkPiAHnruHBsu6gqTHkRtHHwIWkQxeBSAb1zYYpIC81_vgJ5eJ0udRDc4IZM3sDhAiRG2H5hHNDQHfNLNRL6yi5LZy0QFGZthwSYAv4ffDuwaZr4Rj9zailUaIpKLTBFXhqh76M-xHm2jnppCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=CMsaqtl6jV-ytyz5Ff1SXZyj7SrTDDQ_RTfiKPsk1RFAL9U-Dstq6miyMttzxdlDWyzkq-pjV6l3Tb-rgVsGitt5iR4B3dPAuEIw70FZc2XAo6mdLRPJVXcFcuY1b_YOoXJ18EBHP-5gu-wfQNZOk5tFSuv22Wqm11nhFSrNxGRFUKKJ7Npk6iWnbAKuvDHb-prXimnv_uAqjVcsAvatUVioHJhrZbHN0pNlwKdx5P8qM-jYWnbFIK4-WSP-8DgiJo9iAtCifFSGp877yvM3yY2nD5VPHkjz_1xo5inuOGsaYkvCXcKPTJ2DNRF5f3idPIlth0pwvpeaEr1Gm5-J-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=CMsaqtl6jV-ytyz5Ff1SXZyj7SrTDDQ_RTfiKPsk1RFAL9U-Dstq6miyMttzxdlDWyzkq-pjV6l3Tb-rgVsGitt5iR4B3dPAuEIw70FZc2XAo6mdLRPJVXcFcuY1b_YOoXJ18EBHP-5gu-wfQNZOk5tFSuv22Wqm11nhFSrNxGRFUKKJ7Npk6iWnbAKuvDHb-prXimnv_uAqjVcsAvatUVioHJhrZbHN0pNlwKdx5P8qM-jYWnbFIK4-WSP-8DgiJo9iAtCifFSGp877yvM3yY2nD5VPHkjz_1xo5inuOGsaYkvCXcKPTJ2DNRF5f3idPIlth0pwvpeaEr1Gm5-J-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25500" target="_blank">📅 10:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25499">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_l-clUmbiYj222O0s_cqt6JVlGyEwLrDD-SdZqFetAJeK5jhf8ojsYs-FmmP5f90JIBeWTLQeypTnGDeqwKdFYn1-cmmNdbfImt8vCETlaE5aB7NNmBmYt0nTG9QUg17UjSd_92Y3FHoSNcxvkJ-jvjFA0-hN99OcPK3w78BsQIvVI6vRGTZ2q-8uCV6SDRl2Zna-2D37JzA0SOA1I58G2cJdWF9qK-3YfUkErTMWGrRcr7X7aHKly1msl_klj5TF8DpQTyMrBLABaxQjv1ZY4wMwONYzVXODAUMwyXTxhfKfBvLoa4_V1nOBv0VPOzNvNglHk3jbA3sXUr_oBJ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25499" target="_blank">📅 10:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25498">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xb9DXRW2tNg0REjliZicIvG_t8F4NRd_lvyK75Gn3FAP37yciE-b3DmPcdcQWKICm4Umt6SJcoa92vfQjt1aWyB9TGnb_JLRqqK-1eG1EyDWyApMJMCmqK-ngkaXrCBsZI1nrX-W4cAWJRSXLiBh-B2EF6b68ITVlB9_c7uTUB6PdYksW1K0WrD2heWdF5SQSleeeAIftB0ej9CPMgN5LqFa5X1MByWYauZ1tPUS8j7jjMFY86isP11t4ugJSn1NDzZwggRD7li5PmZDTWGZBsZx6wxXwAlnPqKaQQ6QLtc83eiHXXd9D8DMEHdQjLjlHyE4G9Jc-e_4LdpfXx7bag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ جلسه مدیران دوتیم‌پرسپولیس‌ونساجی‌دقایقی‌قبل به اتمام رسید؛ نساجی‌رقم‌رضایت‌نامه رو550 هزار دلار اعلام کرده که حدادی‌امروز درجلسه‌به مدیرعامل‌باشگاه نساجی گفته تا400 هزار دلار حاضر است به باشگاه نساجی پرداخت کنه. قرار شده که ایری…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25498" target="_blank">📅 10:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25497">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=eqjFYblgChwLbYARCcVnqQ4RpxVS1MKtJCXIjDQOCzvd-DSuP6vtLUy9jabv6uPD_fIOape1POum7ecVzAgIcxmm11umkQPivErVxqL35clue--DAS-tb6Iu0HGCn78j1eCOc6yUL0L_MZG21tC22E1nRW-cTOPkAY3rT_CYjQo0Fy1KAkET04DOMciFyvKqtbt_BjYODFpRMUg8cPN1XNmIEBiQiF57rvpVIvgQJs35WcGH6zreEXj1gIX9h9iuuSsAiqiKeETk8EH-diYokZ0UPBiv-BLYz_TEBirewtL1AS4bhyDgHpDVOUZw88YZo9HXbGoY-1DtnT8PtGrmwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=eqjFYblgChwLbYARCcVnqQ4RpxVS1MKtJCXIjDQOCzvd-DSuP6vtLUy9jabv6uPD_fIOape1POum7ecVzAgIcxmm11umkQPivErVxqL35clue--DAS-tb6Iu0HGCn78j1eCOc6yUL0L_MZG21tC22E1nRW-cTOPkAY3rT_CYjQo0Fy1KAkET04DOMciFyvKqtbt_BjYODFpRMUg8cPN1XNmIEBiQiF57rvpVIvgQJs35WcGH6zreEXj1gIX9h9iuuSsAiqiKeETk8EH-diYokZ0UPBiv-BLYz_TEBirewtL1AS4bhyDgHpDVOUZw88YZo9HXbGoY-1DtnT8PtGrmwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس‌جونیور ستاره‌برزیلی رئال مادرید امروز 26 ساله شد. او تا کنون موفق به زدن 128 گل برای کهکشانی‌ها شده و همچنین برای تمدید قرارداد بااین تیم با فلورنتینو پرز به توافق کامل رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25497" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25496">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnF9hzkJc9k3bU4fwSMcIvq3LpRZOJiutzNyc8DHUJs7VGLC9LvwPc0IzipISB3qj7CapObzALxBRChAKz5HmPz0bPXR7gioEVjq5C2uAWK2wx9B9LtT0oBFDvQYgbwfJn3y7SCvxxRkkJ0n-3Slal1aqvrQC22zuYMQZmXdDGQdLIInX_Kw-fck5tcRK_BiEdzNgEOfvY0WS3DJB_X16sSaKI55GHIeN5Jo5HfYCyE-lyGQgcwvuuo1QXBM24NMcIjfxusroC6GP3CEnyU2YX-BQTgQqXZnk9dPp-N0GW62F1eGQo_ufCiYCcBlOyQGDOoSaPJMCpigU8r3K7tn6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
5️⃣
میلیون‌ریال‌فری بت ویژه ی فینال ویمبلدون
🎲
بدون ریسک در وینرو پیشبینی کنید و از تماشای تنیس لذت ببرید
🎁
🎾
فینال تنیس ویمبلدون
🎾
🎾
زوروف
🇩🇪
✖️
🇮🇹
سینر
⏰
امروز ساعت 18:40
🚨
ورزشگاه سنتر کورت
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
بابیش‌از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده!
📩
Winro.io
معتبرترین سایت ایران
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr21
📩
@winro_io</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25496" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25495">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=cIJHE-queF-sbvlLJrvuwSk2MRMiIzZ8PXsESWYiOE6Nh9SfCa2JnXnIuydL_2uCu1whPGd0VoAcFdiwgg_bL2xTnnp6RLOp7emVvrb8lzLHuTjLlCzKuNL6ZGXiKnhF7DhdQ-vFIOjvZMaUbuVIFimivUM-KdZyLsq3FyTOr21NgZtovXk9dHm-BJQYQk2bqaSosKJPAz_hHYg2D39gc1dvjR8TWkwyCrdWQD-SbuzhQWSendfaIE-BrG5T8gpW66crX7b8yo3cRxZA1L4y9XFM-hRT8KKEg08j3HCweH_hPNfL9ErQLenWcQvYMmC8_6DoRpGkvKvj3KsIhXOkxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=cIJHE-queF-sbvlLJrvuwSk2MRMiIzZ8PXsESWYiOE6Nh9SfCa2JnXnIuydL_2uCu1whPGd0VoAcFdiwgg_bL2xTnnp6RLOp7emVvrb8lzLHuTjLlCzKuNL6ZGXiKnhF7DhdQ-vFIOjvZMaUbuVIFimivUM-KdZyLsq3FyTOr21NgZtovXk9dHm-BJQYQk2bqaSosKJPAz_hHYg2D39gc1dvjR8TWkwyCrdWQD-SbuzhQWSendfaIE-BrG5T8gpW66crX7b8yo3cRxZA1L4y9XFM-hRT8KKEg08j3HCweH_hPNfL9ErQLenWcQvYMmC8_6DoRpGkvKvj3KsIhXOkxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25495" target="_blank">📅 09:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25494">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsHEWqDWVZfwCXzEb4VjN1yVAnxOYrhUNvesRwUFMABHcPOtJQ0znOO8xllMmpfNXhR9qim1IDAkXwBIQ3UFo8oozJy5wvR0RBJNRNajD5h4op2SoUwVIcg_1sF4HNUMPKkKZRVrdZCuwMDInVvdZ6vN_HHDlDXPPjw0s3TZ39dQ_ggPkEt5Ck7VU73ZzYlbRnCUF7P57Yp6bvqSPp9jLcGjd8YaeotgwxbdLGlQ0riW-oDlfgiIAktSu6bLBMI4YTLrv6pCzLliJkdue_hlDE2yfWfVVMVtHmMCqzZOsX_6xg3X0KfUWo7TDQbBnXS93pnCy9znsdwc-StvvMy1rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25494" target="_blank">📅 09:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25493">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYZYAUuIaOG490jBEQfT9IJmZkFbs7wvJYsHKbssui04aazKfpVq5J5XNqqwsJoNTPKoWywcBwqBLeLC3_CnHK_AWmAVAxQOHkgZhE6zvZI42DTa6RrZ39gzbw6cS7siqaywHmv3E7_cEWgvVvNaglujs_Z4NKP9MlPm9ydZUo9ukbPrXm9b8aplqpEiDqUwhaAPvcj7E8y4AvAMcaaUWU04HarE1A6qY6AHXIVthW2GeZI6nZpeZFlTk_wYrmd1ed3fJ9faaZ_TsERUZBnFL7QuoJ2x8MtfP_NoI1CiPBad2bek-tGJpCBqxQ136XwC0U28qX6i1K5wjOokXU69tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی‌رسانه‌پرشیانا
؛ فرزین معامله گری مدافع چپ پرسپولیس بعد از تمدید قراردادش باسرخپوشان راهی سربازی شد و در فصل آینده در یکی از دو تیم فجر یا ملوان بازی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25493" target="_blank">📅 09:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25492">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c6aec402.mp4?token=M5kLQDvcMNUECai2meJKXaOSiHrfhGlxMv5WyRX0bop9rSL0ZDq72EDivja5JIYbwfUN5fXFS0qoHX090zF1EXMHmCqrG4tx-jPfbzEcdqRCYZpFRMaH2m8HHa7Arkvv2sjZANlmaXlCzA95QMi23FWCWmVwDP2H-6pZtPRKCK7s9aceFUkBM0l990X9CSib_Ab6w0lK1jIdfHs6M0JduNt4R-cXh4tRTXtyXEyhAicZdgZ0q0hCUC_IO5Snwv31Pg8XVsegi9gWvcC6_yq6vSIPu5c9Ggnmjvuf30DCdBau7wm3-VD4cDBHFI2NhImmiwWfOZrm3VLe6AQMHMQHbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c6aec402.mp4?token=M5kLQDvcMNUECai2meJKXaOSiHrfhGlxMv5WyRX0bop9rSL0ZDq72EDivja5JIYbwfUN5fXFS0qoHX090zF1EXMHmCqrG4tx-jPfbzEcdqRCYZpFRMaH2m8HHa7Arkvv2sjZANlmaXlCzA95QMi23FWCWmVwDP2H-6pZtPRKCK7s9aceFUkBM0l990X9CSib_Ab6w0lK1jIdfHs6M0JduNt4R-cXh4tRTXtyXEyhAicZdgZ0q0hCUC_IO5Snwv31Pg8XVsegi9gWvcC6_yq6vSIPu5c9Ggnmjvuf30DCdBau7wm3-VD4cDBHFI2NhImmiwWfOZrm3VLe6AQMHMQHbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25492" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25490">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c5mrcLrdIRjKwpBKAKtOmQtolJrFHlWuWZ6-w3W8FplrzGelVs0mTsMwgaG1paHIK5QUWkzWtYfmRAy4xr9Zag3lSadPY0AJslvnB6r-2nPQJHY-HJJ5HqzTFaA0fdy7vKko_ihDEd-lTqx9KkKzXlPjQXDxtFxQDOcDgUiDyPV0z5haDKEp9ZhFlLYLSrC2QTMZbbN5RfZ_heaXSoSHzOd5TT2OAq_xzCtPkZjfRghVQcRi7so5PpI5hrWDqeVclfZ7p23BjhQvsc8acmBmb0NeucPvRdGnJQ_oYuZVHnGrelXD2PY82BgTYSRmnnsbhghOMk4uqWPPgZFRdyfVDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bp9jMaelNWyNmGPzpE8CpjephtpOVUrSPNfkdnKxk4Bxqt92UQHeLvw6GDsc27EVt-KTYxt2N1HNY_XPtQWE21zFvfFk4peImEKKrOUycBplf0UyUj4wY8HauSOS-xLRIDW9e5YnCpSXu9jOQLEtznDnMP1Om8rhjEYbmCBYhKj5nKU68XTjuRVJCuA68lJZd4kd1aDkpxHeCJJ3cEfps4RmNEA8odDlAbqB-yk25q0p7XjaGWb7PkLwLX_d90U-DW5i7WWCZpc9pMJN0s-Eievi1_PMt7a9Tp2x5GulnvmhAUbhSWuuZCpEkFdr6wnpe9biJi79u7tq1MHBhR-vaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25490" target="_blank">📅 07:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25489">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dW3KyXhICx3YHk5cxUz_b0ztigmJW75hIkicXKrm_pEoOuLmL7FsivvN0zffffzHgguyNqStrlPWWyCi7SgKtQcCLDkxDQyKX6P8x7X2zw67ofemaiHlf5ZUkG3LYEVvp7SVPyQn3XY9qDi_a2vtpMWmUMbwbOiff5DgfT_xqzAzjeq8HWQxYycEKNpmB3U6XNJ_8ql1k6OHMnofUtx2T03MH6dxB747_OGAg0vhXPJvFxDChBq3rx432boyNzI2axvz__H3yjSJAd9Wp141nMxh8Hb4Sa8FKaRsQcbADonqe8cqitEKDFUVPGMd0dbeYdvHRCsldkGACEulL0OkaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25489" target="_blank">📅 07:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25488">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQg-xkCLXS2Ebu2I8mNPkiMKelfeloBBxawBgIN1GQwrtoEryZDpNW7EWe5UYrf0ZDSwXwPH37ygyzKZo0lrqgVcO15O_YesX8-WzECSYfkMTZIh_ylV8vtfF9Jx3rCDkWb6G88yR97UyrVPRb4IjNOyPpmFYB4pKPyFeKJC-U8krZAazNto-wVQUJDWPf_pxq36qs6RgEIH144m1N081fvsN_DBisWc7wZp_jV34yZWmJt-5N2dkHsKX11lb2soCmSQq2B8oEuZv0LvcrBACok7d7XtDImu-ikwZ0VVRRes8MzWy0T_Q_ygA4R4SVcV6tN1JgCMO7gvQGdjkXLQgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25488" target="_blank">📅 06:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25487">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0qgIUOQhK5LYwT8ihzh0TeWxkRpGVxIk75NF7hMcMcNzySF2G3vxV-5YUS2tgRS6webadm5VpW0eadP2TtXjQ9jWg-0niIrkRqyyqEhsp522WxkGONgjGt7xxrdkBMWGANQMhbFECFs0sECnt7rK3Avjx_bmqySWeWEvkr4H4M4Asm6kTIfBek5uY4JZDTm_FDn-ZcrxBWe1uGgbmc91v0CM-b40-S3MadX3chdqgW6sbvNGUKXo-FZyz22ObKfUdDWMZUUuU4mROitptTNFjpyFsRaLlW4DxOzOaSiNlm4keRWbC3S_nZ-XOF25fTJYDf36-qSX0yIVkdmx5MMTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25487" target="_blank">📅 06:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25486">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBHitqgukVdG_wQWzvbwgHkwWVrbvBUXz4o0SKPu2k3S4Ug_2INHZ7oHaaGbBqdoDvZXNW0vG9DTgqG_XEErOsshYcOevN1s3bd1H_emeKSQkMirrB7J6ACYjm5EplPXVwwN41h0cCwfbjG2eoagWgQrzW8E0NMxDqil0num2XaIIm4Dx8EN_h57K1yaU1kP5g6jwbTlCURLOPVE0uVcgQMK0DuvgtqZ_5eLnp2awcJCTVJvJuBQirgk0HcaFAJMZ4lgsNpUKcgKZnlTQrAxvY3HIZFs0CL_4-KVntU2fuS5E4goLdWatYmvN_dqopmQL59z0B32dJlQDoLSLWLpzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داش‌چیشد که به این روز افتادی؟
چیبگم اون شب جای‌درس‌خوندن‌نشستم‌بازی آرژانتین-سوییس دیدم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25486" target="_blank">📅 01:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25485">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=hHruqTTTtutf7WSVyGQ6cyUVNy3lEVnOdekfLdbv5fYWW4w8OkhxceOvWp6vGYTUtoJicChi3Z_AwbsG_nI1FdUwWFK0JpCdstWo7dZhqXBoD1fpkO52RNDePPqdjnGlwUBbMcUfxlydKfEzRFZUM1vCCYsubC6tTyYjD9Gp8yrDgJncAi3Q2EDp837BxpkJNQZudPMhlDYGzTC9ZHnu7FEf5mHRAQ-3M_1Cr0AeVlRAjVnq-GhkjEBIkslnnKHfJrbjuGPwlJC-IBRu1uwiKEnbRvAhNPkRqZAeaoXnr26wUM8yWEgNyrrzsvo-SlAsg0mndvcTHxbaVfGDpwT7RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=hHruqTTTtutf7WSVyGQ6cyUVNy3lEVnOdekfLdbv5fYWW4w8OkhxceOvWp6vGYTUtoJicChi3Z_AwbsG_nI1FdUwWFK0JpCdstWo7dZhqXBoD1fpkO52RNDePPqdjnGlwUBbMcUfxlydKfEzRFZUM1vCCYsubC6tTyYjD9Gp8yrDgJncAi3Q2EDp837BxpkJNQZudPMhlDYGzTC9ZHnu7FEf5mHRAQ-3M_1Cr0AeVlRAjVnq-GhkjEBIkslnnKHfJrbjuGPwlJC-IBRu1uwiKEnbRvAhNPkRqZAeaoXnr26wUM8yWEgNyrrzsvo-SlAsg0mndvcTHxbaVfGDpwT7RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
واکنش‌جالب ابوطالب‌حسینی از رابطه سرد بازیکنان تیم ملی پرتغال با کریس رونالدو در پایان دیدار مقابل اسپانیا و حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25485" target="_blank">📅 00:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25484">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwTi0_9YK_tYc7x6G6DjPN45RDPMWMMQbF_sXSrWwtSU-b8bC-BkScm6t7Beh2F78Sizgqik8Mzf_nwHjiOLL_A_fd7AEJBuaTJnLhmHi32t8w_qDIpiINsg-7ECONr32EKhTBTuLMI-mipDgFOOJFt6o6x0f7sIpbu5BBm_fmRH_fHPCCu9J9w2Hr8m3694S36RqucX7nw53trQHz3Cy3mpfLZ2tGbS-WOBPQ_Fgg_k_k9Qlzcz-62CnN5jCXGFtrG1HPdOkuA5HopfLO5nqJXXuII9keryr4pNyHglPclTs4OWK1Mi6NrYaEx3q4UezvGpurCjIPuNtCeol_r6jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25484" target="_blank">📅 00:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25483">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXitswh4vg7hbhT39vf41Ga80J9IFBlOVyaHsMRmlktqBHAtofO9KPe1jZSFySXpJnvqzK_DFkMSR5i8J0JEavW8jWhz-w7w5iBI5Gsn7DCEWB6AO5mFUyXJLjALGPvvGrChWr8x2VlcLyeyoY8Iu6ZCvqLtWVe9-jVTddPeEOiT_QLgAo7C5ZkvJ_ca1ImoO9AvEiROSB8Ej6HaWDpm4k0F-A4mWrmrZFq9DUxyxn_xM6atGEkJiUHaIPew_aKmB2FqXEcXTF-cFy6eMhRYUDpQ-5fAoOJ9dmkqcK5RN8kAbClZTnld_rGH3xtZ4HcOtLgAl3qtZ4hfm--QOWq0pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25483" target="_blank">📅 00:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25482">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjX2qNkvlFnEBIN0pf0OQphDRtJxbneeuVUp0XaJxEImRr-hOCGdf5lLACBF3d2Uc6C_atPHVXJXOmbTIms3RZsvb3m0f9YSkdoFQtVx2xa3fqyBg-4KVVy9x4APJYtHXoLnwvwT7eCLavC9_oP_8FtUJaiqVRTP1p1YgKaib2BBdkyesl40gMsQSSApMz053wGn-5RxcwRCeQ4KxLai7osMBK-PKXGRqsPP2XnrFsObFa7EdZowwbgrTAvU1OMx8B26BlhBx1pJfxq_1UhqTKpEch-CvxqPSKeLOyTJAUQk-jINgHr5kIciv01Dp3eJKe2u0yR7HsOK4OLI_V66Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25482" target="_blank">📅 00:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25481">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bx-rtEg-QlQgHhtYjAoA7THNK4hgrINqTCI6feslDCetmi2OnKQAQhqhqwN4k-rPAk4iYjLQogKwONPhUd69c_mNzy9XqlYl41lUF3-ayc1a0u_M9mShp4pUCV6EStbl1T2SRFtwkAxCDJGg_A72-SG1O0LEVKplVSUDoT-v4YLjxksI5wTshq33czcLknnajZG_TXrdwqJsXmrMx6mJIDoG4GEeP-hl06A9TVQL7HGFNGJGtDLGjHdO9G9Qm-r_mlTsvELQivkZk9ShkVn4cqAfZKdxijaqeyyKreUpd8scA_1z1XSrF3BKLR8T4BFZc1UFg0lZMvrMg13rnbAyKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25481" target="_blank">📅 23:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25479">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YVbzoIgKnGz7d_6JYV5xjvNrO7It2R9qWDJD4Mg2ob-fitP7tEuHgXb8UbGZlSGWdWDw0EejbKSkUqAYXTpQ7HPL7fcXdyDSfAWytX_3fsneB-S9e4yR4k16Gro0uu32AZUYRCwCg8uNr1yZbN0oPkobW0ogahuzkk6hrt-dQq12aayhgK9OfBlLnnBD8FAbjwSwi_JNwusIKKQxdmBhcZ6UWxkXHppGJH_-0ultF3Thux1lAzn-oTYsdVigfHneeepXSAPoxWAugQG-WTRLpB-4f_Rlripwzr7nMJWdMd9l8WupPcolzOHUUERMGYwecJqAHePmn7Ak0q5V9qD7hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vehHeOjuMFT9iJAv61AnqHNN4rkGZwG3YuXQfS1CB7IMCCVJ6QmJ8FLQjXeQZoBrPJ-Sk3Cb2oCXrmHmwOAz4BHrA_z1duvc5r75soWUXVnef-ec68xQulGwAmHW8pp4z2dRk6qe9wvo3glgYzH8gz5byJOJhLhmLArdz1Osx6r3JfwrVSxDSLnjepDItbrPIrCykiq3DY9hwnn_UYU7nIusyOUf8e7n9IJsR8QaYJzDP_lSJq_xwbdka97hPcul1xXEDYEzwl7_pwm3XMPiSkueHr6-_iS6KNx1kzn4Rq6n952HIAnKFCTTX3t9el9vqmt7QEIhohX-DJBvwKPDOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25479" target="_blank">📅 23:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25478">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_QHR4oPYGYyFchgn8Mrg8A7qwx9cIal18vkvY9W2yXjq05SvyErYNinHycjl2Sn-JtdyjqRR6nT6-9yFvvm5z7xleL37uA3rDlfO_hHTPuxjzxjYchEO3LH0Zd7-5A0Hce4Ce7mQqfT5Ff2xWcFiKvVI6COHnywxG3v0e8OdJQIaYCYRHpWc8L2bxoB3NsmOeeIkd0xnFE7uUn18h0bIu1luDdySrWREQJZvCuDMwYvb1YVeQ8Zz2TM5kcS22I7VINpx_5YnOkXgBp15D99iEt9FV7cB2wIfluQHWcOsut_7quhwHzTuGfF1NrU2vi4lbCKXu_geMJqtVaDStOgqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد سرلک در حال مذاکره با باشگاه فولاد خوزستان تا درصورت توافق مالی بین طرفین به این تیم اهوازی بپیوندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25478" target="_blank">📅 23:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25477">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JATtMHIFAwh87FChSJZtrTJlYyA6Y7UcgzAXQtNfnG61S8oO7hdaQpakYbdoM41An_xgBN7KzR-ZN_x0LO-bW5ifsK2jRP01h_vrLpUEulGarVKaaupN74WqgaEwDvBNqrbbzH4AOQys2oyqEjSTKk4XVo28yxCDb1ke0FOUUpwCnSUccU9NAnlcLffh0_IJbTHX-38y-Ht0jSfi97ri6JrSGSHR67B6fcETpIgf9RLP3PfMu-YT6FN7jdFLwmJaRY3IAu5YEG7fVtjYKDykRixGTWpZMddnRvRlSY8JtuC5_-D0ur1Qv6u6IgdRCzSA6_d_4JZ5812Su56_VDvf2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25477" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25476">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBlAVs4yJyUx4_LZH3OW5e-dWncvbfybG4q6OLPIyHLJBgJuMWTPe1OBX2s58btbK3HpYwMskqJhODhoYPKENfTgHWqu1_ny6v6JKKbKHHJChrLxnG1l-oVLIpw7C3E9VEEs7n_gvvJ3Q-NbLmPTBTLllMj7OtgHxV5dgFJB-YtZZUg_y0i8fz2RwYGjgV1CHb2C2TRCKgvhOlO-3WAyycZYjz57Z5RJ4pNsGB994E-LxD22TGpFN59Cge0XzyK4qP5Ts_CwWnIT4EeNaKEnJ4pzDsJ9xBOquFL4BaYZeBTHL4qrJ7OwZgCCZMsxfAD9ReM0E91dAM5oFL8lLz1wvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ روبرتو مانچینی برای‌عقدقرارداد چهار ساله با تیم ملی ایتالیا با فدراسیون فوتبال این کشور به‌توافق نهایی رسید و انتظار میره به زودی پوستر رونمایی از او نیز منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25476" target="_blank">📅 22:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25475">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=XQw6sSDe5u8PLScH5b9rOmkxhXUJM4qUTqGPvAGegkzzBSK3OLtX75RHG9zP60z4ZZ25RTvAHlv-h-VFGsG7YTUSVwQwqR3VTS2nMwQu8PZiPgbRbvryH5mcsQOeA7sGyokI86ZzAP3x-Tdc6Vtgvi8Hg5WriWsaEwYo5RiuDT9NvnEW333d4xhl23E7E_aLMhfKOrgkVl-4xkxX7LjErv7oM4Q8n0aoDZIB2omSPa8zUtT17AEMGtn5FNHiY-iuYdqrxzmU2S0Sq-nah3lxB0W18V6Vjy1L_tw-RLgwgp2h5aXMfUJ55bQfcfeezHKZYKVWQy156HIapdaPoEwqaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=XQw6sSDe5u8PLScH5b9rOmkxhXUJM4qUTqGPvAGegkzzBSK3OLtX75RHG9zP60z4ZZ25RTvAHlv-h-VFGsG7YTUSVwQwqR3VTS2nMwQu8PZiPgbRbvryH5mcsQOeA7sGyokI86ZzAP3x-Tdc6Vtgvi8Hg5WriWsaEwYo5RiuDT9NvnEW333d4xhl23E7E_aLMhfKOrgkVl-4xkxX7LjErv7oM4Q8n0aoDZIB2omSPa8zUtT17AEMGtn5FNHiY-iuYdqrxzmU2S0Sq-nah3lxB0W18V6Vjy1L_tw-RLgwgp2h5aXMfUJ55bQfcfeezHKZYKVWQy156HIapdaPoEwqaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
روزی‌فهمیدم مسی هیچوقت‌تسلیم نمیشه که بعد دعوت به این برنامه‌ازمجریای حشریش جون سالم به در برد. لعنتی‌ها ببینید چه گیری بهش داده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25475" target="_blank">📅 22:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25474">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEQEEJRoePi-NlmHBy2c-2Foy3E_GD-wotAQehJehLbAo5Y9PtufVlF8PsqOZwYg9qcVPWYj9Th3JE0FAz3HZsw_cpiyXYrwbjyDIQVw_Ivws7vyw1aI8OTkz2_Qa5RJvxEKw7TeAnHTFrKV3F_9zSYwEYUNhmM96SYhyOcMXONUNS5qNUbXz1Xj88AZO1NMWUyIxpaLtR8lqLsnvpOzxR-0W-duL7fpZ5vreYPJ7tb0F7tnXULVwj6389mhd4r0jwKDAQ3v-XLakolTszqyn0oPbGtbcGqH3Q_dwevbQbbBdns-qPF6rchXwp6ybjHn1_I5tQn9JKnORuL5w7lVHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی پرشیانا توسط پیمان حدادی مدیر عامل سرخ‌ها درباره وضعیت علیپور و محمدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25474" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25473">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=W5RKszkJlfJ7B9isBMaW_6ooDQcsorKwpd5I2WE1QvRv_z1fgFzswprszUyorjeJ8YFZzlnB4LZdalVMdg1z8T06ffSmhrV28_bByUbIrI511Bq74BRb0rjSsMPjNgedQ61tnCBH8v4-2EDjl-X0vRaayfUmNqSjv9b0VuSqQajYOS_lz5lDb59Ssm1h10YK5fkMpmNGJZTuBXPR_zqRNX4zvMAFi5ukl-PkbN6qSx_gvBWJNiJH0G5GwEQs11ko7slZ_kyHnln1t0FQhJw7W6OTSaayWeUcHEWbOEl53w4RwTNk2REXi1QDn9FE0Hex6MWV36WW3hQzHp7LM68YPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=W5RKszkJlfJ7B9isBMaW_6ooDQcsorKwpd5I2WE1QvRv_z1fgFzswprszUyorjeJ8YFZzlnB4LZdalVMdg1z8T06ffSmhrV28_bByUbIrI511Bq74BRb0rjSsMPjNgedQ61tnCBH8v4-2EDjl-X0vRaayfUmNqSjv9b0VuSqQajYOS_lz5lDb59Ssm1h10YK5fkMpmNGJZTuBXPR_zqRNX4zvMAFi5ukl-PkbN6qSx_gvBWJNiJH0G5GwEQs11ko7slZ_kyHnln1t0FQhJw7W6OTSaayWeUcHEWbOEl53w4RwTNk2REXi1QDn9FE0Hex6MWV36WW3hQzHp7LM68YPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
صحبت‌های‌ندیم‌امیری‌بازیکن‌افغانستانی تیم ملی آلمان در رقابت های جام جهانی 2026؛ این بازیکن از دو تیم آرسنال و چلسی آفر دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25473" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25472">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifCsjtqtSJ_ctQmw5Yw9TZ7xWaUoo36cMOfuH2KJZf0p7LyzGxrxSMxAJvx4ph-va04lmGatjJhD_gwbR_3FjLxEppqYv4NudHMurIIrrszmjscJwitkteqnf1GqckqxNJP9hg16nMV0gJ-vxn3AFeDdC0hEnklQ8nQMW-0SlcQBRGN5xbFZqheraOzbA8vvfviZEHzzPumbm0wyyJw-24_dmUJUFeWTn83p95Mp0TLnTgh7K7pvOR4kcdPQ9N1-PDRNL1uC8EzX5UoQ87gMxUsPayrgtzN2VPcebDKMa0CbQ7bFQ6jlSQF4TE_-wpyUu-KwWxEp25YdYpH4kctwkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
قدرت پیش‌بینی‌ات رو ثابت کن!
⚽
🔥
دو مسابقه جذاب:
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🇳🇴
نروژ
🆚
انگلستان
🏴
🎁
500 دلار فری‌بت
بین تمام کاربرانی که نتایج را به‌درستی پیش‌بینی کنند،
مطابق قوانین سایت
تقسیم می‌شود.
🤖
پیش‌بینی خودت رو از طریق ربات تلگرام ثبت کن:
👉
https://t.me/betegram_bot?start=p6_r4EF37DCE
⏳
فقط تا قبل از شروع مسابقات فرصت داری!
موفق باشی!
🍀
⚽</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/25472" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25471">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dG6KHI1q2oTfFri6nJmT_y_DPoMg2AApk-V4cxsgQanf7eZCY_ywTo0gvjklC7XW7saiVHe-IklNH2pfXJnjB-C1Jb7K0tda0YV04aXsxXjvWFtdB4zCTKz5q48st0kTJei1Fhd3LmCzBJVxRD8XgczCMXXAvhUva_Nq5abfGHbww9QZtb-21DQwrZLjqoO0zfJcAIFuND7H-h_9vKxrjSiCKa3K_VbXbx9x-BlmP1L2nQp2aUr-_hDwuY29fUEv2sOTTJl78OLIM9rROEaHLzYVbxU8jMnmmf-eoj0o5sEhnc7nNoRFCVjIwab571OGIMp30Az3YCKXcZsU4RZ02Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25471" target="_blank">📅 22:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25470">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhHBNwe6K6N7yV_9gx0T1LCYLZJ4b_J47fZQN42dw8UaRe2UvFucK_AyFbtlqWGWSP96ixQD6eY5RRiZKkRTBSfPujjIFkrbJ80Ok00UokWxYAPxeZOxmB5dnPD8RHtQuiCbYRRPbve10_vLKkrFKEfPTUEjdHiCrHARZPMvxzyJemk3UDHJ26Ao_kso79pBT6Nyo_6ArG7B0Is8I11btQWZf_BwIaCmwRtFbtb2S9m9Ye-Q0n2-hJDnQ9s97GFxT5qO5xJhXGdPcOV0SJQzG7GVvuDLDSbc5Mfw62sbOz6_rgJqZSBzeVrNAzzGz9snS6c63qrEPkXu5U3l_eu7rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جالبه بدونید بازی‌هایی که تو این جام به ضربات پنالتی کشیده شدن در نهایت تیمی که پنالتی دوم رو زده برده که این‌فکت هم درنوع خودش جالبه واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25470" target="_blank">📅 21:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25468">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=LaTKAZgPQnLBS8K9gRnW-r5kdve0xBYsRCUuITZbpP-msYK276R1GPHt4Om0aW-uqoHXhN7AG66T-k1sIHuVpvwrLFKciL-ZmDx3uvIFzsSkyKRkkrgD_zsSgNjpOeHx3x3oRieHS_OQzNO-LuN34O16BOjRDqjMi34tIgceCmywqwX7qT6oI4GwzKb0sjYCl2KLi7cCmRwu0cJFeQ3D2s68HMNOozanRZmv6NIBFweBhd2pF9Imo8qy_buzYkUW7K65sjP3XmJfbI9cv2ZbfimvgKYboJa175cOA9NMXXglr8PhfWJtLXm_6At_EUPCm61n0r33Dp04RYPEhNB5Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=LaTKAZgPQnLBS8K9gRnW-r5kdve0xBYsRCUuITZbpP-msYK276R1GPHt4Om0aW-uqoHXhN7AG66T-k1sIHuVpvwrLFKciL-ZmDx3uvIFzsSkyKRkkrgD_zsSgNjpOeHx3x3oRieHS_OQzNO-LuN34O16BOjRDqjMi34tIgceCmywqwX7qT6oI4GwzKb0sjYCl2KLi7cCmRwu0cJFeQ3D2s68HMNOozanRZmv6NIBFweBhd2pF9Imo8qy_buzYkUW7K65sjP3XmJfbI9cv2ZbfimvgKYboJa175cOA9NMXXglr8PhfWJtLXm_6At_EUPCm61n0r33Dp04RYPEhNB5Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌پرسپولیس که دوهفته پیش با ایجنت علی علیپور به توافق شفاهی رسیده بود حالا 72 ساعت به‌این‌مهاجم 30 ساله فرصت‌داده که برای تمدید قراردادش به ساختمان‌باشگاه برود در غیر این صورت قید او رو خواهند زد. درباره میلاد محمدی او تمام توافقات لازم رو…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25468" target="_blank">📅 21:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25467">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmtAENkC-RyDq4o9_JijI1zroJyOrrldBg4cf_PmINxV17V5kH8PEgysZvv_j9qTbeD5YupSPd-JtRtAw3unh_szKj3QzuMyyNTVjjJosLWIgKUdB71xPKWnZNSd0i2gcYvb6R38CVV6P9oorSCPJRHlIL2hFXHhzGa4ksT34miG-HgK3uZkiTTqy3X8gqU0qzF4xzFQhyA4cnhGZ-64vuLz1yep49Lusd7pWGFVJnPY1JcplFoT5k-nGW39SghaN2em_0RuYGoPRA7wC7_7r2EX8OYSE8HvWNpkKuyXj2sNPJXKYxC5aEYTCQOSJadgnd_rDKANklyAD5F40d5JXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25467" target="_blank">📅 21:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25466">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2KOuyDI5E08WsjBhJZHsLvDwXNXgP5IGWHB4AOf7W3z3V4IxwTqudxAAeflvGFmy9iNLkkB6UGBJ3mHlXfueCfuniltAd40c5fzzzVaWBb5ynwtSLUU9av-MYUNhhpQ3pPavxk-2ZweunS_jWoEuQg5pq1Kmg56wiFlQjhFEInnU1-0v74jtefZWGKQ365W55MK0IX6FsT78dOlXEIXSKS7qy9uqJBXXpvfNuSEJgMYGtR7bS37S8EEGpFkswQDvG8Vfngfhd66axiAEDojivHcxcmvVrly3GrGrDRSjiOUOe7T4HxZ-dgL0fRmn2Pwwe3AM5d8ycRVaFfLUNFuVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25466" target="_blank">📅 21:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25465">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kusHXodACvkSxRU_s1iY-82Y_eFGGd7qB2rzsN7THOEX5jnk0ChFLCepOVV4kIMziafpcrf0SBfue4_kSzILY1tAg9SJqd-JvcHP90_UMRqRGmeS6MoEZqmqHjNKH-ZFz5JmlaFjRDrHrXS3-GulUPkt04RFtaJdvNsLxjr7A3-SVltRqCboxZM-mzENNrJIFo2fcz5hlj8gYnMXTpHTEXhAtP1cUVeA7Qcvj2ERrOrZ2Nr7Ib7nWz4QDbb2T4myDs6ZI4rG9DW03L4VhJv3Q_tnRfKi_3QuXA9P5tDWg-54vx4ytgzTIRRVeRaku9-_U7ERCFnXYZ8OLz-Hgzq2cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل سرمربی تیم ملی انگلیس روش جالبی‌برای‌انگیزه‌دادن‌به‌بازیکنان تیمش در جام جهانی کشف‌کرده که چون یخورده 18+ عه تو کانال دوم‌راجبش‌گفتیم. حالا فهمیدم بلینگهام چرا یهو اوج گرفت. بعدجالبه بدونید 10 گل از 11 گل انگلیس در بازیای اخیر توسط هری…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/25465" target="_blank">📅 20:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25464">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMwTW24JhwEkB7aVhT-6sOGvDdY8oIEjKsKZaLPXRGn26w8gEFx0A0tQJ-nq9jZaqXde2bRP-e1TgQ_m_5HO3IbTnq6_0S-2oWMyZiaNOUeJWg4SZ0eSGxLylslIVGt6cULGqhHzg7YAArT7AAqEk9vf6oU65KGhvXVx2kC9m1T8sVhQdtmAdNn1qeb2hNMhbRieIAkhcccOr3uVrkhqjJclnKtepaOFGv0ZMI_abbUsoqt3afWf7ER00YfG4VITWW5HAZ2-DfzyF28m8dRm1NCAus9U2W6d4gUU27LbpJP_8w4QIZx-PhleEe8mjRWZdEVeJwBaZ3UAo6t7jGMA0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعداز موافقت مهدی‌تارتار سرمربی جدبد تیم پرسپولیس؛کریم‌باقری بزودی‌به کادرفنی سرخپوشان اضافه خواهد شد و قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25464" target="_blank">📅 20:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25463">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRVR9YgFuLozkNlJBDoIAmAsLSM6ZFQzmvUp4pmyJoFyG0y4ZtMb3jbDjX-kiuYElNXWNmtNSzdZuxZmB70ipEWkeHn5eX0KTb8SfxlIRQOQLFKhA-Biw28mG3aOLHnmYVvpzJXhVIiFEuGnILBkWEJBXGiIXbt7x6qhzjai6TGz2iT4i1-G44olyT_Caiip4RrxyNU3gWP9K33-zzZqzbBx18Y-56HDUIaXRXcl4LmPoLmV342MF-9DsLvL2PdToUS0hn5yPxZ5AQuILfD-XPJ62go_YsfQ-Ljb--zv3-roQ1Gb-TvRVHOFjJpYw7Np83d2c9TbzAzlZ5zLTW__Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌اخباردریافتی‌رسانه پرشیانا؛ امیر هوشنگ سعادتی ایجنت معروف فوتبال ایران با مالک باشگاه تراکتور آشتی کرد و در اولین اقدام قصد داره هادی حبیبی نژاد که روز گذشته در باشگاه سپاهان جلسه داشت و توافق نیز حاصل شد رو به تبریز ببره. اگه این اتفاق رسما بیفته یکی…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25463" target="_blank">📅 20:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25462">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oI0dVS928wMF6KH6CjSDD5OwhfI1qVXaGLNXL2jEj-r35x1ynB-bmBvKRBsXGFcLQo9a9ZJNxV66D6TrzyX3IZEsKT14EDt1yobue5qNsgYrc21URv_1oUfQrvCYxukLZ3fHyZOsnE4Pkc3zMh37TTCPNI8EBbDx1EBV6qmtpsSqpbWB2WNuyBmO-hgcBG5oEE9LGY4nnRO4XbOUvNtXrUY3qg96l5oqeJu5oo5epraged8El7jSYfDcB2aHC1Hey-HS52Er8exp3XQnUfw5BG2K63vqeNuPGQ7Cc8mxADH6i1zRkIpfRy5A68MCYV_ZFIubi2lvVSM-ZZUXlNrHFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25462" target="_blank">📅 20:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25460">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAYx_vSkGhHaktbbe23_hXE-EOQS0VYPeReDHQuWLoyxl17cx_EURoiQO2BtXCEqBLxJ-2BusEL8WoxsKBeq-nFZXglTJO3XVPHYPm4tiwQ4tQSLgOx9uDOV3G-9b_EyOvV70hiCnMpHjItk63xwNBWQCjGa-krT1PlWn09Fu9ixeWDcFnpVlG13TBtsehmcBn7e25pYU-ZxM05YVkkukSo7fxcLWSG5VVAvwLS6aapPbwtSvlNJk3hh4bt1C6Aesi8aV0Nvd25R0bzWBsu8gC2KOu6B_qr_5jMSJ6p1bZmdfzOIFVaMvRouyPcR-QskJ9b9VysP7JO7k6inmySnaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25460" target="_blank">📅 19:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25459">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTszcWIY12lK2wjslNsl4urtkl3_YTi_eOZHtv-L7maSmzdvg5bCrcyXqPS1idIu_0Br1K45ksuScs64BQf5o1hMobJkc_ehyvwvGrfCr4Ukf1pYi8a5S86nOhYJRHqd_um_ZxLbbuh5bEioKM1shPkh9Fr9R2lJcYIHfYLYoDx3tBhk7oPeBsvfSrsvCwE4ztpMPdUHWdYipZuqdfN9R4jtSAMYI-4fdXuHkWma6r2C8ygf3lwPhky-5_zOuhct2Z1gZUVVtj6_kGBsxS_72A1SdwRhuAz9Q1Jl2jMFFx-iqPJo-cZQTVU9b5qwb-CCqY2AlYYor4VJbBZZM_zvQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تقویم
؛ 12سال‌پیش‌درچنین‌روزی؛
بارسلونا با پرداخت تنها75میلیون‌یورو لوییز سوارز فوق ستاره خط حمله لیورپول رو بخدمت گرفت. آمار سوارز در بارسا: 283 بازی، 195 گل‌زده،113پاس‌گل، 13 جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25459" target="_blank">📅 19:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25457">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=Xxqwl6bAeFvgeOk0z8Iriki2SCMQ08qyfI1l5z_-F7k42ZiUmvvWxJwtfq0owYpZ7KhMzqFbDB6izUxogzWMwYn3s4v1P8ma0H9dMYXyeiKNbsgIpPmD87RXZTEHKtW9hDMxb0D9mWuAgnY4LcvCNDoAKMm4qOa4Zq-K1WYEgScNs8fxWUVH5gDVPXGPKUT9NXFZBHqpX6LSseGSK6S0cU9JkLJ5RnNpTvt5XuYRFz0NkRXnlfTxHpeJDgGo7qAsXoIGA9iHxE7HPrAHR7nXw7O9HaRDsOLSRutRbOok9-l1kyTLzWfRQRirQ3u5WfqVWIYcIQWRCyNdfbmuSJ77wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=Xxqwl6bAeFvgeOk0z8Iriki2SCMQ08qyfI1l5z_-F7k42ZiUmvvWxJwtfq0owYpZ7KhMzqFbDB6izUxogzWMwYn3s4v1P8ma0H9dMYXyeiKNbsgIpPmD87RXZTEHKtW9hDMxb0D9mWuAgnY4LcvCNDoAKMm4qOa4Zq-K1WYEgScNs8fxWUVH5gDVPXGPKUT9NXFZBHqpX6LSseGSK6S0cU9JkLJ5RnNpTvt5XuYRFz0NkRXnlfTxHpeJDgGo7qAsXoIGA9iHxE7HPrAHR7nXw7O9HaRDsOLSRutRbOok9-l1kyTLzWfRQRirQ3u5WfqVWIYcIQWRCyNdfbmuSJ77wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لقب جالب لوکاکو از زبان فیروز کریمی؛
جالبه بدونید که برای ایشان به‌خاطر شرکت تو برنامه جام جهانی شبکه جم‌ تی‌وی پرونده قضایی تشکیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25457" target="_blank">📅 19:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25456">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIeEh1AZH6So7k5w3FGnJhYpx-c8hcT1_Xq-grhMOvsKCoMz0j8yerGwQBlkRim6SStBPUqTjtOQdrkBquxjQanMrwBmpjqYBCLv1E9K3lQRxNNTSalarQbih121GzGQwp2V5v5P7awuELauueJBj76BrFRSbV5JD-Dl3vcDP_KCKTqVqhbLur-e_kajkibwRtvMakU8IwQW3uGuNE9W98Trh4cxBS8PCCaWoDzrLjBBH-rqkXRVJ1J_VDnC0beZAwCE6M0uAp16tEZvnl-VYGJnYnH8D3ZEJ_IpJG37SLFc1KNilSKFvYt8r6OlAoPBQrGUevSjE1QGVtEiHQrYJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام AFC مراسم قرعه‌کشی لیگ نخبگان و سطح 2 آسیا سه‌شنبه27مرداد درکوالالامپور برگزار میشه: استقلال و تراکتور درلیگ‌نخبگان و چادرملو درسطح دو آسیا به عنوان نماینده های ایران حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25456" target="_blank">📅 19:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25455">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJ5Nx2ZG07mfPDJcMVk59vN4sKyg0C1b88Z2PQ8mkQuMLIt2YC0MYNvH0pdqdLG69h8HWFhn2Vgnh1GrHmlwoxBavo1B17ycNMfZDaYeKtESMvJkeYC5ShHLZhOxX0H4L4GOexAdICfRf5-ZwSCQWVspCTHA1wTbU3i2fA7JgS993iG-WKukEXd2Q1n9gFINL5GyBYBuC6lWnk8-Je2jaLmJTy4euf3jhOQ0QbieTMcx2uBoRK4YoTHgrQjTbDomXlxN7Z2HNgSHKTcDmc611V6bG-yjmru4cBbhhB1Y0dolSwMpmmgDatA5wCtjaqA232VAFQV5GR0RRYhhcRwTkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
کریم بنزما اسطوره رئال مادرید: به کیلیان امباپه گفتم الان‌بهترین‌زمان‌ممکن برای انتقام گرفتن ازاسپانیاست. به‌هیچ‌عنوان نباید این فرصت طلایی رو از دست داد. اسپانیا برتر  از فرانسه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/25455" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25454">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‼️
خاطره فیروز کریمی از حموم عمومی در برنامه دیشب ویژه برنامه جام جهانی شبکه جم اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/25454" target="_blank">📅 18:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25453">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tif6-Q1etKm-G4OwhoH_DNiiTJoZISMhr8YXBHN_Gmt8vPtTsU6qMhHOGim4es3bEMXScih8UlruCcges1Vorr0Luj-LYk_EmhGRx4nYEs7H7-CGU4bgNyB-89JrlFNEMS20NgXFhAsCPpFph7IlsiBqM0RnDkXUknp7TeyAha9ReNKVwPhEU5C6o5L5OrDoyweiIqGLRUYrr17i5mqZezpi6YbAnrQAjdMMLF5P97uoqTs6Z-ooDtVHRinWdiLtcT5Csc47FeJkKD8gGau5SQIb6YeTgVLEhD2DlHEPJ9BAzOsaJoOSlHjDti_51QhaY4Zdf04EwyO0dXgVOCvHWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/25453" target="_blank">📅 17:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25452">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HN5vMXqGzMbPPWlUW89nBCQUYK5jcwUf5g3unmYmioiV5Xi8V3ufcRjVHc3SfzQZ79X5V8JTkJVjXeaqEwDU8CtH4_5nFfOecbfoZcf4Y6FBDcT32JfE5-NJ6FYuW9SXxmMKCbZdcSoBVMjj8XDie_BAeO2JksxYVifEdsJpQ7jvHfJZYKyBC4Dze52rfH0PKEG3yiOR9h2FcLqE9vlbEQzYG5osGvm14JPugTEurTKTwhwtxb20zJbC1vELbPhnJ0_PiOE2q_yQNv72K9glkZ-r6A3_BPnlyMw3xfXOC4dZDJxjVUCPL-tVZoKQwTYSbe1orGvX6s3FwEIoijThxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25452" target="_blank">📅 17:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25451">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uqor2rNXclAvS20ijbqeFgVJfWO7nUlEAg7ipPlDewSK0cKxdpfMdiZVrvVdbwgWMnbHEZP3XFqju693Bzt71b_KFO5tikrDx7-VutqLPCJ-AZc0FUs4VfXysLIDOotWnCM4NvUcm0SCs3hUu66YF5Limgh2vULEumNZfH2aCLppcubyQt3zcaUIoE_VxKa6AVhDYfrns8V0vcvcDnyvoPgJXgk2nsTNJfRpzhOZBQydW2dw5fVYCveRqbLMIhO9zvn07EhDgfYSHPIpVnrX4lXJU8SS9kA5Ouu5igb-szZp8hM00l7_uwyRv1xHgP1PjmbdmFUQOr84SDNHt2IL4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علیرضا بیرانوند دروازه‌بان ملی پوش تراکتور: اگر در تیم پرسپولیس میماندم شک نداشتم یه روزی مدیریت با من هم مثل وحید امیری رفتار می‌کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/25451" target="_blank">📅 17:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25450">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEHIgxE4lvHMODpNtF_Qpn5gsQFP5SbnKUE1yPRsrBVBLv1I8_Diq7tHjoZMaMuuIjtXNFSrWbD_1Ho4WCl6MMWLlfNUUgcCHfbZR6D2pzzPUnhxGVX480StITj3pBaJyumtUMw5EpqasTK68_cVHFPKn370VeTwcZ5VnfI36UDItZI-88OJiAgCUSQBR67k8Yo60Ynh4pl4JeV0zqbyX_972wRCjHccbvXjjyV6q0vF2SMBFEqW2UjrxvLF7P-zqAMB3_3hBme5dINtjp_dmAQIdtIwl3dy8VWMzF5dGurnU-N8WWd-mcODRLO1fHdAx5zsk2UzFY4V0ttYP6f8fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/25450" target="_blank">📅 17:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25449">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIT38tw4KrhSPiF5fjQ6wpOPRtovxZTb8wxngWERGea3X6X3UKw0f5mscD6BTIHkXhzJmq8LJ93WKqd2-qJKeUsJQ5IfTX1eL17CIJa3avFHYCK2XerGesWfD7lK2RRb1PpmirbMiI2YZntXuVzPOQlh2BM3z1_5bGsUjQjCrUevP2jR-3tcsUI5FlUELtBUFI2sKLTKj-Nsc6WiBPsnIxuHG7aOuLv2dc5iFB1spKMBS5T_f6p4zwtNj6lnoiUTHgRbMqdRab4rpyY75uk2BrJXbMTTk8KeIwqGsuSrX-yXcivuSzcTxYd9turBh73ICZddQkL7IQO7-kG73zK44Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
خبر شوکه‌کننده دنیای فوتبال
؛ جیدن آدامز بازیکن ۲۵ ساله تیم‌ملی‌آفریقای‌جنوبی که همین چند هفته پیش در رقابت‌ های جام جهانی ۲۰۲۶ هم به میدان رفت، به علت افسردگی خودکشی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/25449" target="_blank">📅 16:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25448">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfiifr3z-O7TGdlOizgJRis8vTN82gRzQU4cc5YJ1Y_0ThhsSkpxM_gvsbb9rW4YEqkeSnWSWi1FwCfPVr96TTMchYIE7s2gieb8OJahZh_UCFJGUarHAzRH10rsTWIBmwQW68Z-A8z0jABimzCXsh08EifTyPQmCA0SytiOdh1Z6U4j2gYZvdYAwQRWU0Uh8iq3_4bFuQmRHqpQTlpdpsbvcV3xi1epDS96-2Qee1akL0cPReejBLvZ3XpJLZ8SOBFNHyORpKS8NH4X0GLBw-u2RphWhl_X1p7cTtUkUzY58f2HvmtL4CKtlaDTeLPhdmTVW5aaoGhZ7oJWLTS2sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#اختصاصی‌پرشیانا
#فوری
؛ باشگاه گل‌ گهر بدرخواست سیدمهدی‌رحمتی خواستار جذب ضرغام سعداوی مدافع‌میانی 20 ساله تیم استقلال شد که با مخالفت کادرفنی آبی پوشان این انتقال انجام نشد؛ بختیاری‌زاده به سعداوی گفته به.سبک بازیش اعتقاد داره و در فصل جدید بیشتر بهش بازی خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/25448" target="_blank">📅 16:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25447">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UR5EHpCn1Y9zBge8GrmUthWlpFE12JponLnQ_CZmbeMd5rvfODZIg9kpuiF8vV_juRYzRJCqwGyZ1YhyhZiSSSBnXUMrifFsLKYn_9x5Rf83wS48bWCx_k9DZPkGEnATawY1rjaf3QTPMpx-jQ_rqnUA1hfMVqTqzDlR6Ia0lBL5eZ_RD5ZdhkUBYsKPOzhJmfjrZkvyl_6lSu3Yau6nr0EVQ_c4_lh4FDso6nxabgF6TeRSl20JA99yxqltmyJqbWFmtEPdlNRp_C563xOwuRzOPVfD7yk5Oo8RuGNyrB1gmmm7OEONUZgd-esf7zYSv6tu5mfXLeQrJde7upwXaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/25447" target="_blank">📅 16:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25446">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDEctkkB32MJCczzCXERaT20AHKyQvdU0-zUIFHPn-U3DAaIfTvE7KXPJ2qJcT-Wb3mKcWDpSTWNZaU2Uw1dwnlqvjfl4z2lit8HttHgi7p2um7E3QPHPqFX8QygeAAR0H_aVzPg3QH2Duo0Hg_S65fVCRyT-3zrqeh40PEdqUzRp4FyUQxC8NoyZR0ZGKrYAtvtrKs4DEbz6wUUvbv3xMBj4LFVUGOMiBDuZ2mYYztLM9YHdPusp5B5tdbCVh6Aze-zWgbTxZLPd7sj0ygFJclS009OXJ1c4PdfB3YaDkeXGdLOMTElt3oUyQntlN7jAJhnxeyogWuxqWvGXLHB3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛ باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/persiana_Soccer/25446" target="_blank">📅 16:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25445">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcZo9T9P3akd59sAHL3FoHP7-MCcxoMozG_esF1qDkDJdTAwkQiuzCVDV-2f2-loF3ZlMNXufttEuvNhmE2XNHklyroP40DZQuBMab3kIdlXS6IbJX4ZkNHvOk-Wsy8uoJQs8TC3LRC3T7vdINy_Ladn_ihVeiAB2k4VGtQz_V3_98VnDS7jpWpySQJO40X1jMAEkZNc_zve2fwsZqWfqRODS1YhSyTsdB0p82XGDJHjtrNcDokF32P-IG6mQ0E2Xutq6rk0PMWzzpcnmdENXSn7S1K-mr98snj4VIrW51pDHO3-JsMR5b1kJXnuHDyafWi8I3D11pB4yLnxrtuv3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/persiana_Soccer/25445" target="_blank">📅 16:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25444">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZKaqYNoPjEpRFRspVdJjMvih49j7vB-Nqs5p7tZuSFjmSa5KIMd-Q8NWXVRZWuVV-aA2nYkeTGv4jn5yKD-OYXivjAmfRm-2pTucIlUwxtj4_lLWt6Bj1qej4V9KDQV8xfwJSVeF6VY407eRsaMSymDJpuMhFcpoU3nG7owefSoE2bQWpiDzbKn8Z4FYb1ONLzTnrCk-vzuoGoSKY7_WBfUo3MHiwjOqTNQoLSQHGc8oeGqtvVLfgeEIRA7cQBc4_Q7YBDigf1PsyvJubLaBsL-37J-hrtktLBst_ram9ws58rMPRPbCEsdBYXfB1H1H6G1I9E31fFBmat2Vvx3Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/persiana_Soccer/25444" target="_blank">📅 16:13 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
