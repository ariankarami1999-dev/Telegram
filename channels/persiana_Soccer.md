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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 22:22:48</div>
<hr>

<div class="tg-post" id="msg-25549">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fu5ai3V-NXiQ3DUxdCQDTPMi-B7QzA5GiO4nUGtYoOiJ7CwcBSWVMXLR3JlVKa-IZCMbfDalHWOYeim-EQP5zW_26v6n8YZdudJRXbWozB26mIScS2Jngo6rG5OzzyixoNu-ZjFYeVPD5XVzc5rQBxg8AuyYGUKHLuWFK6CjW6m1MGrWxBZroLkPk6N23QeNrapwIK3i6Y6rQBw_xB_t2YsAVoGLVjy3b2K5FsyVOEnvCW7oxwHEk_uTK6380j38nIyV9JGl6q99wBQ51jEEQKHUTJgpMEVN57ZZWyJllHPG4_IEHI09IUfEr5uHWL5n3G7z7jlu27vYVX5uXWiByw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس ساعتی‌ قبل با پرداخت 700 هزار دلار به باشگاه‌روبین‌کازان؛ کسری طاهری رو باعقد قراردادی یک‌ ساله قرضی همراه با بند خرید قطعی به ارزش 500هزار دلار دیگر به خدمت گرفت. بخش رسانه ای باشگاه بزودی پوستر طاهری رو منتشر…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/25549" target="_blank">📅 21:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25548">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfD-FvGdc7KuBykd-fFXj60v-5Ei7lttpgpdTHGrbDqhsqRtgtEJdqupnK0R0ahhMs6kt18EUiocnL8_XVm_dmfRltYXhUZoXEYrYsx3lrp0fV11Bf4zmIsFre47m5nr2ymWbEXwviUdGgy16-EgxtVcijsbzdFpbdT3gPRXVToN8S04tpcnyI9g-uyi13XeC_SOetEgxPOJA4IeBtYg7vvxjeMYhJuKCvCGyB_FOwJBUgyrxhtucMVeMOIPmkCK5fX_QNhGbd8wfHMptQLckZSYAGNk5ksuwUFp30MGLE0Tddux5x60Yt8VLlUEEGys9aBm99eSPJQACB_2Pmtiig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇱
فرانکی دی‌یونگ و همسرش که در تعطیلات بسر میبرند از چلسی پیشنهاد رسمی دریافت کرده. ژابی آلونسو درخواست جذب این بازیکن رو داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/persiana_Soccer/25548" target="_blank">📅 21:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25547">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROSfb8TzjmxrcgEVvg3p4innSQgYNZglWDg0BjyJc6MmIeOXMZKj-2rV1LkqlmxXYMY-OFhlGHlVGFVSQhgBMroIT3AmgjGR5luhs3mzN9AttzK617Fi_i-a_tX2koAwpUPGIhZCusRDW3W4VWl84DjjNQsfi2q7NS2utWMQnEP4rg8_ZqeEwQmAridD8uRPUKby7NLi-4qpbL_0xydukkIQ6iFsLWlf5JMalToACe6zN-pvecS2uJLKggEDgKrSGb_CbsbEcEuRh9GUOOHyHZy9FGH6OweF40Wx6DFOVGdz1a3ZQqUn41GamgBkZK6quiEkd1B9djJQqC16nK_Rgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌جزئیات‌ عملکرد لئو مسی فوق‌ستاره تیم ملی آرژانتین در رقابت‌های 2 دوره اخیر جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/persiana_Soccer/25547" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25546">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1YRQG2FkIxRs0A8uM7K0WPBwGYnihXivtREEAlmnEMt0Rzleyxx1JsbekvjUMM3g1D_fPgP1ZmPeN4JGBnL8VFpTw6v8DEhWD6WHv-LIukVF2IIyTj2-2AN_aRqDyj7fuDuPHZ2aoEskq7c5rnZdFkOgh4yANUBXO8vJ-v6v4WE0yWab-WnBs6MfHe5Xi-6Yyr7FSRNm9OsVUJeOcmDvJW2W6LJy655fbjnYsOjTAG0pljYUwqzcjURnww97p6-vy-2XAGyUUXhn4ctT_arBgd9aN0ncaQpNNiQGiX6veHIJ7zky0zWQb52KuvIMFkjJjs0lsCpK1IighuGWAVjmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اینفانتینو میخواد فشار بیاره تا جام جهانی ۲۰۳۰ با ۶۴ تیم برگزار شه. و ارژانتین و پاراگوئه و اروگوئه هم یک بازی به شکل افتخاری میزبان باشن. مشخص نیست فقط برای یک جام میخواد این کارو بکنه ولی ظاهرا عزم راسخی داره که این پروژه سنگین رو در سال ۲۰۳۰ انجام بده. جام‌جهانی ۲۰۳۰ با میزبانی سه کشور پرتغال اسپانیا و مراکش قراره برگزار شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/25546" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25545">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/25545" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25544">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/25544" target="_blank">📅 21:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25543">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aY2FGKQBNHpJtxLsMxLq5N_D5mc7yhgOCexPviESN0L5wZ7h568TXZPn5OefyXglZRtmBmPrQlOzFKdeWgvqHuBj80PkvuECVAVhXoxfucWq_uCRvxK4DVz6iHuEWBBZ1daJZfr-6OpXwfmNphgiljyLke0AQzBCgvR_4_TpbGIWCgkXorMy430eIj2eYyJnfdjwtq3j6MyRdvN75C2roHGfMhGjZPCq0t_gwC231tavb-jB-rnQO-kvND6u5TvZ19ZvHTMQs31UEK0Swi4tWbKcc75dKb_rmCdyPwaopX-CxG9OfKVo45JM7kxh4MrSikXdGIEil7rwC1UyNqpgTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طوری‌که سورلوث در بازی با انگلیس؛ نروژی‌ هارو به فنا داد؛ وایکینگ فن‌ها عکس رو میفهمن. برگ‌های هالند از خودخواهی سورلوث ریخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/25543" target="_blank">📅 20:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25542">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlta18X9RDKHdT5ctvHdXHZJeYtW1mCawL4hLOjuDMo9LApgJ4k5gLa84SeBnniJ9I-lN8s_D9klpmH_va1ER2us0oGdGDhLOxNdD_0eISvqduxgftTuMRhZxRcUcbeMuVmM8wtDIlWLdyz_cHnZVCi3mEyxBKBXYKjd7lmPHY24eTy-sP0ivYXHe1e3UEz10Sysl9XjJ2puRxa9lRorR7WeI_LNKgH-asqqyYATz8B9HB7ccDDWc0vlTbB_65gqCc6pYayqLIt2UFtrHzrGJrq4WSZv-Q9GvbKhGdhDJWsDZT7pfaV2OPyGFmArX0WRQwxdZaj_JtA0ivg4CeeHSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دو انتقال مهم امروز؛
آرسنال 20 میلیون یورو گرفت‌و لئاندرو تروسارد روبه‌بشیکتاش‌داد و مارکوس لئوناردو ستاره الهلال هم رفت آژاکس؛ هلندی‌ها بابت این انتقال 17.5 میلیون یورو به الهلالی‌ها دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/25542" target="_blank">📅 20:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25541">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/25541" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25539">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2qRFCsvvmoXcPcpaOteUXJB0Q86EKl_YlbmeYtyuzQJsWu97wxWzFRnE6KeclpDNEFzrJDMRUlU82eXvi7Jjc2jDSRp748RqKSLWz20jcDs61OQXEwO7hOcbAqZhdVwbXQ381Vu4FrjBFTLejA1OYrK7yceK7KKXdoD0Y7d7bpAUzHNBBzK2PHP3hCX0TA13FE9AUGobxhS4J6t7EnkhBTNi9zO1oUIqcBBXqEGxvENbQ-X2GLNcjYIrSuVguWwf3FTZV8IOSUIdmGMxRyZsHUIffIHIhHZG9apIkP8TogATGOK2eIS5zUqOaqacXDHAo_fXXVxlb7j1J1i6BmiZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/25539" target="_blank">📅 19:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25538">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmHK0Nv7Ar_sqCUtuG_HRUv3m15unE4eR_WEV5g7n0uIfnA-sDTKa6WHlNsx_h9i9q14YFS5UEExjZIBddGeE_Pl_j7QzIThpn5r7JRi3D1Lre-X2mhXc4x4yGjb2kIjA-C_QCIQ964k930p17jaD9MEbE2DjxwmuXqxROOsmJ0shmsAyjA0-alvQZJ07uV1gyXV2P0Ar6Vak4D6Ar6QciLHG4tJ9waVdzO9mZC7tHXnBTO00Uswo4JSLgVORZkc8RPLcol6CSqCyWdHBQogKlDQPSRjkGuqCQTzB6VNcPIvTXLq_YSmDuQI_4TpggPiH2CZcSNNWVScqttQlkV4nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسینی در سپاهان موندنی شد.</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/25538" target="_blank">📅 19:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25537">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QT8lysGTSIcySF5T6-moibako0eIPYYtwpqzqet3cdYaa2vsy2jSXd1Qy2b1W6nu8e1RxEmjBLkM4z03OTKHhV5E0yjt5X9Tpvy_Pkd39VvueivwqYCAy23e_4DVSaQ9PFXBYMwBwoST2fGlJ_x02KTI4-Q3JKGtes8xJtEtC7c5612f7bALddACDLvs3Ei-UvKgYvylBbGG2QTmF1-pUo8OBzG4_VYe1Y0oJdCzph3giM43Nl2iWurdlFb3xrkC5gV_hzK3pG5F5j70UTfhFdj0hSSI94DD11ecL91xVcLAiZc-nL2LGD5DDf3dVtKV2ErkufsM-Xfd1ylirzMR9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/25537" target="_blank">📅 19:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25536">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/25536" target="_blank">📅 19:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25534">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHVBM1Osdcs32c4gYd1_TwttiU6nhkWtAYJQXR2Tam3TbXnVrQpT7ulbaSuhewIEBYKtYShD4cmUX7HTjM2Gl-fZ0pSePrr-Uy_StuPWecrilG2FDR9AMEyMJ3r2V0Ix0KLehRFYZYt7N0Bxg1NgweRN7d_dECKbHA-sGC2ZuTwly0lkYNXcPLFmRI7tuso0nJ0L_Aj2uBVry2c6ELY107sJtMpq--Bx0dVpIXHCeG5gjYtCEydIPc-mOWokGdiorjzjwi8V0HzZtpqELgJZWYDS91rwnvAe4mMikQ-lKodgjn0DJWXrXOX3EwgUZxLiV1biAyAmqI5xUFDXgPc62Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوسمار ویرا سرمربی‌سابق‌پرسپولیس در انتخابی عجیب با عقد قراردادی بعنوان سرمربی جدید به دوا یونایتدبنتن انتخاب‌شد. تیم‌یونایتد بنتن فصل گذشته درلیگ 18 تیمی اندونزی‌رتبه 7ام راکسب کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/25534" target="_blank">📅 19:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25533">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iyi03NHvRJKZWB8-FK86aXpbipTzw2obiaQerUYCwKWF_PT4sw4072m0MDWEWT150XK31QLz2s7YeiOn4uys3_QllsWU2cGkFelUw0X3pz0QIxay0F9D5a3z5mPrSK4XGXyT5_Dv7scMrVRMiCKkXTyyQIdp50ks76EXkCYI9QwI4KF9R0O0mNXxpuOOb0R7Ws7bWlAc-2OeXcZq_NU6U6CBtBSC39zr6unzb5LhQ9hgUXGeYtKpR0hcLbMhfHtn_Xoz4O2t8zmqXlVNXnZ-s5_eIBxHaxNUnCYF-Tx-rzn_JRFPQNqma5u6vVvxR786VWPYzJrt3M1z77Gtxkf29A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برترین گلر های فعلی فوتبال جهان که بیشترین فالور رو دراینستاگرام‌دارند؛وزینیا بادرخشش در تنها یک بازی‌مقابل‌اسپانیانزدیک 16 میلیون فالور گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/25533" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25531">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/25531" target="_blank">📅 18:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25530">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/25530" target="_blank">📅 18:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25529">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0b0e1c0d.mp4?token=ZMoDFPWNraue4r34TJUFOlsuByTk_GU50R9p72Gc7s3nCaROU1fpuNrA2QYBSNGBi2QJLDI-KN7wYcwhRqHX_ooVSclZHXM7Vr2vsVZQD5OqcU3oK5KPl00KGOT9pjsJ4grt_AkUKE0a790b7Y9Gap-hThm75E3UOpvursLImaYtV3q4Yl4YTX6IM6CvX2FWoLqZx4egEaB3eSEur53WSUZql7Yms0m2fc9wXcF0-uGs-ri6R7U-11Lw8Bj0Xf7ok4HcpVn5rp0ScpsoMB6VQblWQKeMNI-cNax4xXxbvffYCZ0mUlYpMxSH3xu0Oze5PWDXq_rmwzgeMMmUUa43HTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0b0e1c0d.mp4?token=ZMoDFPWNraue4r34TJUFOlsuByTk_GU50R9p72Gc7s3nCaROU1fpuNrA2QYBSNGBi2QJLDI-KN7wYcwhRqHX_ooVSclZHXM7Vr2vsVZQD5OqcU3oK5KPl00KGOT9pjsJ4grt_AkUKE0a790b7Y9Gap-hThm75E3UOpvursLImaYtV3q4Yl4YTX6IM6CvX2FWoLqZx4egEaB3eSEur53WSUZql7Yms0m2fc9wXcF0-uGs-ri6R7U-11Lw8Bj0Xf7ok4HcpVn5rp0ScpsoMB6VQblWQKeMNI-cNax4xXxbvffYCZ0mUlYpMxSH3xu0Oze5PWDXq_rmwzgeMMmUUa43HTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیوزیبا از لحظاتی فان و با مزه لامین یامال و داداش کوچیکش که این روزها سوژه رسانه‌‌ها شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/25529" target="_blank">📅 18:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25528">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8eD4u8ga_x2Syi5_AyL3wlv7Akdxrwa2eKDzjJj1G1mMAHzeM3nbXc3zb8WqUO1vwkl9dP6qorm0sfKg2nqRwZzKDRbJRW2yXfx-1LnEXwF9aG5wdCj_vFhowSa8IH25c6x96Y-ZUarABPpLDL4G0brOKYod7JElOZG8eSdCiQP8GXycHL52sjKMPj9bk45HKBwjA9Snv8dprl3VjAV8fRNIRt_sJJ1cHfRNR3BrreB0smQluVGCPZluH1Qq96U7nMvgpx4znrK53dIpSwNJyYRpHRW5hJ9YRHVC-RjAUu2ToQoC0SbTwu2YkVBvwL73h0vojpY2nBEjKtZ9tjXjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخباردریافتی‌ پرشیانا از اصفهان؛
مدیریت‌ تیم سپاهان‌ با‌ حسین ابرقویی مدافع میانی 29 ساله باشگاه پرسپولیس مذاکرات مثبتی داشته و درصورتیکه حسین‌ابرقویی بتونه رضایت‌نامه اش رو از سرخپوشان بگیره راهی اصفهان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/25528" target="_blank">📅 18:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25527">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‼️
تو یکی‌از خانوادهای‌عشایری یه دختر بچه حالش بد میشه، بعدمیبرنش‌بیمارستان تست میگیرن میبینن باردار شده؛ میپرسن کار کیه!؟ میگه پسرعموم، دعوا میشه بین خانوادهاشون؛ برادر دختره که بازم زیر سن قانونی بوده میزنه پسر عموش‌رو میکشه، میبرنشون دادگاه خانواده عموش…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/25527" target="_blank">📅 17:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25526">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZQumKjx26UpqqAOTYbfEpRrljlXPfesSi_6u0FN8efem4n7tiWGVTsyjb_64pb7tmzvxvSFbTEVgslZpd7OQ4nHes-Ji-_H2nilTVFLHrLsA8p-ZPXlWcnWTgoryQH9RJ2Z_KsKSGxng2RyJ2xm1MFdbHaP2UBBB_3Rp_XTqdBk1ev7rgIEru-a7gKXbp3ApAyxeIPCDF8KoSj2ciQGJUh6mILmEHCuxBvMDJ9ja-nvJpfckG4FJ3kyvja-K9zmBn-hsd1FeLBvo8sLruBiXinz3VNToOsQZ-dI-cKIvtNSwUjqhUARaON13ob0NLGhNG_0tNIJT928USBKTh1cCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تقویم
؛ پنج‌سال‌پیش درچنین‌روزایی؛
مدیریت باشگاه استقلال تهران هفته‌ای یک الی دو بار از سجاد شهباززاده مهاجم جدید خود رونمایی میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/25526" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25525">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q63fuPO1L7sq3ISMPCOzUANcRTtNHHzpKJiZfMT6P4wVOmIfUwOgSjPVd_KzysJ6Jd4EIfwldpoWKzC6uDbsdibs9fNkgx4hYP-xwG7VTokcvnyhHn0XTeKlzddi5OWJMy1ZE5r-AwzsOGix5RYegtPesvcaY-k_2u-IKvowAZKtmJB63jMkcKfdDF14twBRuXtZGaaaXsY5Dk_XNyaIVZNLCPZ86TCFmhHA_b2M0vo5_XmCNAySP35VuBHlEN0UaQOmhQaP4bc2_w05y4gW0tv9aX2adHvXbb0SoLAOOMroT7Y0SElbV4-bU8_OSUlqKuLVPNFgzPZYrmN0E_nw9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
آرژانتین‌نخستین تیمی‌درتاریخ جام‌جهانی شد که بدون مواجهه با هیچ تیمی که در رتبه ده تیم برتر فیفا قرار داشته باشد، به نیمه‌نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/25525" target="_blank">📅 17:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25524">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhaR5RRxBQakZE8NvFYjHMFZN4RrVkySacKs4JVcPc3iWgJVyG7kD9ACSKvi5kfNpUUTuztbCh3VadptPIVQ1_LqmSoWvV3MvjdTj5iHBKIWzrzesxEFRtxn9ZfOxlxrYEu2ISNz8XOndhgZLDfJ3DGjb582wC4jyBSC2k0l3uZ3QXgNfeuGEDwGzpRMd_mvyKB89Al1N3l52-Xmbc5PoKc5DfZMisLsYz6vlC_a_20_yayxaMkg5WXzTzbYO5Du-qJQDXesPmCKHdUAuWyL1neXj4o-D3N3yVMhu0vekMJNASW8h6bgFwZrx1d1tzG4wZpi9hCgohBJbWXcWdpwlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
عارف حاجی‌عیدی هافبک‌جنگنده سپاهان که مدنطر مهدی‌تارتار و پرسپولیس بود بامخالفت شدید محرم نوید کیا در جمع طلایی پوشان ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/25524" target="_blank">📅 17:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25523">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9c9cac2a.mp4?token=dDP6Cj7FuGB04YixsAahLKYKoJs3OfSlCpOGHfdr9QX-LJlUEG4gGV6neDOryB5Acb47aZLO9FLHG0hRfOCi4MoyqMPLC5LeiUniY5i6kFD50x1KryVCguZEvaLAzhKLi6wk8gWHlhctXLI_w4JW0mhwiYDbnDD_kLjrSYU0U2BNW1mlX9tAEvFaLGDRYEKPJBAv9W7nI6r1XZeshtFP24pG72kf-2XYOVxwDAOW1ULhtEIhKXAI9An5PluacdQFiD6vSfwfDBGMLOKk3m9lr15NavnjT5BTfvUg9tipx3R_4ewJwHFjFfn9Nw9n9xp4wQajFbMfrceFftZXlT79oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9c9cac2a.mp4?token=dDP6Cj7FuGB04YixsAahLKYKoJs3OfSlCpOGHfdr9QX-LJlUEG4gGV6neDOryB5Acb47aZLO9FLHG0hRfOCi4MoyqMPLC5LeiUniY5i6kFD50x1KryVCguZEvaLAzhKLi6wk8gWHlhctXLI_w4JW0mhwiYDbnDD_kLjrSYU0U2BNW1mlX9tAEvFaLGDRYEKPJBAv9W7nI6r1XZeshtFP24pG72kf-2XYOVxwDAOW1ULhtEIhKXAI9An5PluacdQFiD6vSfwfDBGMLOKk3m9lr15NavnjT5BTfvUg9tipx3R_4ewJwHFjFfn9Nw9n9xp4wQajFbMfrceFftZXlT79oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هومن‌افاضلی‌از کادرفنی تیم قلعه‌نویی:
شجاع پاهاش پرانتز برعکسه اگه پرانتزی بود پاهاش اون گل‌هم افساید نمیشد ما میرفتیم مرحله بعد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/25523" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25522">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=Dw6QTlRJ1n0BszrXWZoATGh8KVaT29sA6_dvJPTd3R0VxkdP1rDYMRXivLbpE0ZgIBczLIg54GYZIKS_UYmoYy9LQ0XIVWy4dUkVgjN8TheMu9zZ93J3COMPaNofCtGbBG7IISAumkbeldFSZs3lfnO6u15r86ZmNHk2ofpkSrWiL2kdo6GfmG4uuHu5K-wIXAfXUKO44C1KmiZfZIzO3GMDBO81MSInoOg59CkKrK9M9sBT6YL7vMxNVHvkxOLjZjHZU1PrtmPDuQ0zk8vtz2sPLxU8XAaX1wn737Ay_EmzjODYSgKx_6Yo2qvdrGiyCh467hfMv-tFmRwxvsfi4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5608c7ac3c.mp4?token=Dw6QTlRJ1n0BszrXWZoATGh8KVaT29sA6_dvJPTd3R0VxkdP1rDYMRXivLbpE0ZgIBczLIg54GYZIKS_UYmoYy9LQ0XIVWy4dUkVgjN8TheMu9zZ93J3COMPaNofCtGbBG7IISAumkbeldFSZs3lfnO6u15r86ZmNHk2ofpkSrWiL2kdo6GfmG4uuHu5K-wIXAfXUKO44C1KmiZfZIzO3GMDBO81MSInoOg59CkKrK9M9sBT6YL7vMxNVHvkxOLjZjHZU1PrtmPDuQ0zk8vtz2sPLxU8XAaX1wn737Ay_EmzjODYSgKx_6Yo2qvdrGiyCh467hfMv-tFmRwxvsfi4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل فردوسی پور
: آقای اژدهایی، خبرنگار صداوسیما وقتی‌صدتا موشک‌خوردیم و صدنفر آدم کشته شده ‌میاد میگه که همه چیز عادی است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/25522" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25521">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4009214e91.mp4?token=ecUV0J42y8k5AeUCYxZ-zeYOYOKUw1GqC5PNFFV8r6d5gUfFwZL8OzuJLXasN_g4XUwvMfqz66Qug2M4jeRoAj6FDGkWSFpeiSCicXVjIcRwYbh7-HCjOAlJZKxn2SYYT5z6fvxdOuZYeWFxNGEy9dv1qOSTPPAz8R6kYF5LauNkmH55U_KbgWoWjS0vtS2-tLx8dAMEBHQIzYpeu44y8FWWC8DGcoDA8GHg0uNTwlgLLVcVIWK1DJW1PKW2cDdIbAnApXwP1kjIXzP3jb0qMEQVoRGhWHJ6yItrrYoGzMimUPZT2o1Q6M61QtrCkGR46rLPT29kZXXSC03MZ7MGCA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4009214e91.mp4?token=ecUV0J42y8k5AeUCYxZ-zeYOYOKUw1GqC5PNFFV8r6d5gUfFwZL8OzuJLXasN_g4XUwvMfqz66Qug2M4jeRoAj6FDGkWSFpeiSCicXVjIcRwYbh7-HCjOAlJZKxn2SYYT5z6fvxdOuZYeWFxNGEy9dv1qOSTPPAz8R6kYF5LauNkmH55U_KbgWoWjS0vtS2-tLx8dAMEBHQIzYpeu44y8FWWC8DGcoDA8GHg0uNTwlgLLVcVIWK1DJW1PKW2cDdIbAnApXwP1kjIXzP3jb0qMEQVoRGhWHJ6yItrrYoGzMimUPZT2o1Q6M61QtrCkGR46rLPT29kZXXSC03MZ7MGCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/25521" target="_blank">📅 17:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25520">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=hP9HqhiJqfyHLOwRLpc2qZsLGBXRou7b3cHktEf4o3__gFsS60ec66cpsJEWRBvq-kqW8npcGqHaoOzEaL4hIyvJDHtZtwyIlQ-16bBas2ByPx8Oec3BBvhhZLcpIT8xD6SfCVYVxBstxz0W6yYugj_pAh7IZr295Viz-XDkVVBBuKGYgINpXOQlH5n4lNuru3aQBmvxvRrbsKuINeopP4-SsthEb1NVCkYTvoSYd9OHtZWRmXAruq8J4KXqFO496CIhLERQjqgQc1WMAgAgN49pWc83n3mbUgpVQdOKQkd_aLk4DN3HgnZ_udANXzPnQJxjtDGtuA6gcWaUCrF2ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ef9dd527.mp4?token=hP9HqhiJqfyHLOwRLpc2qZsLGBXRou7b3cHktEf4o3__gFsS60ec66cpsJEWRBvq-kqW8npcGqHaoOzEaL4hIyvJDHtZtwyIlQ-16bBas2ByPx8Oec3BBvhhZLcpIT8xD6SfCVYVxBstxz0W6yYugj_pAh7IZr295Viz-XDkVVBBuKGYgINpXOQlH5n4lNuru3aQBmvxvRrbsKuINeopP4-SsthEb1NVCkYTvoSYd9OHtZWRmXAruq8J4KXqFO496CIhLERQjqgQc1WMAgAgN49pWc83n3mbUgpVQdOKQkd_aLk4DN3HgnZ_udANXzPnQJxjtDGtuA6gcWaUCrF2ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
شوخی‌جودبلینگهام‌ و ارلینگ‌هالند در حاشیه دیدار شب گذشته انگلیس
🆚
نروژ در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/25520" target="_blank">📅 16:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25519">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzQYIxNDOpDwhMGCc1lOqc52vwcKIwgkekNLuRC2BnlWdUrGvweLD5BRvvSyqVTY43P6wWwJ9A3PVxYQ0-BXyyZZsYpWxpIXCc5qTwgt5-j2qYTfx2rUh2HOX9TwTWBepQAXAOd8qh4B7Y3pagJIQ4N16_YYgHkpHLrjAvqdaIGAccVMColHb6FVA_B_24yNUs31giYju0yYInu3Kd8nQbBXZTOTPqv4xDTcoeVELgxIYC4rXGoCx7OQS0oD_3DcrveiHUqYf3l6OCzqCS5NO53DKuNJWzmzoZlkKXm5OEXGPQ3LEPCQDtCUdTdqzueO_PjXD4MTca00YNWitXSiug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/25519" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25518">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIKTPDMiCKQwoyBOutVg-E_eVDluAPb1BCq1dTOU-qzXfVFTqwupWBnjNPDj_FCzYyWpOAl7JwKFEZxBMNVBONCY2k4K66P76fSSLJlH8KV-KZLCiwcTxlF7NihxiIneD7xYICgcSJo2aXs1NXe6nIxELfK10E5c-4nThYHKjNBlUbJ1wjoQuS2g526oJkUMMF4oDopc975Jq7m-BDL59IWmKXJpuu3ne5B5kWZOsRhG4RZ7VMQ_qCk8h9sTzPrGcooR-7CULohscx1kph-f_UNo1VKU9_6hWhdVscMeCAqFP0LekGBvqyTR5hEo3s7xf1mMJOIUzdfNesb5_vyK0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دو تقابل جذاب بامداد امروز مرحله یک‌چهارم‌نهایی رقابت های جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/25518" target="_blank">📅 15:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25517">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HR-Ya7jPtEVUDY_6o7KAptaCbjNhVifM2rkX__-HBGjI_sk2sAzjZxBapvG9_lKJdQYfaSaThkEh1_5RXInbifakPw10nx-yYCSCuEcBnQIX4phN5a61f-Yq2pCjQbJN6KsKGaoY8gvUW7k7aWteJkNhcgOr-LcpYRu8q8AecHr0ePN7w5Deu0W0lp8xNh0SBm3pzgCBnKDlx46E5DMhplmOnYuxaNWbwTZQ6VPyXPY8HFVHMDG2FmdSS_Z-zjSe58KYUuhx5cLdHDH39PauFpUZbDOH3dOPfanJOvEcTnkQ4SDSWBot8XDVwj9vhc-iayeD5HlwOJ1HrJgHFOXnGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی پرسپولیس؛ بعنوان سرپرست مدیر فنی سرخپوشان انتخاب شد. نهادهای ذیربط مجوز افشین پیروانی رو صادر نکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25517" target="_blank">📅 15:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25515">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25515" target="_blank">📅 15:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25514">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUyJ_OWYNvDsD9tSratFzjwUpkLuUx3E1CCFXU3F-EYn2RtdH9aBqu_WBKTUawRHhzrowyKMwkAl1SF0GdZHyQOwQ1TFjIXomliw2l5OkALVPpDMYKbtvx7_i1Kk0sZGWFQw0B31QYWlsrnh0V0RLtjHp7wijABoun7CmkLExTYzdf2KH2uUP_0-_uILO2TUrMjtGVNfTiVD4G2RWoZVOZ85JmbT1nX94CQuWZR1rb-_yYJxLhjDFgeHtIAbXGkNQ3iUYaDGthHVJY-4GyCGGMhpyIdxEl9Nx21ew2PClGyU39TcChBWGe_jbM0J2bGwG0mhdYppga0MubtnIpcALA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا
#فوری
؛
یکی از بازیکنان فصل قبل پرسپولیس از دست مدیریت این باشگاه بشدت دلخور است و به دوستان نزدیک خود گفته اگر پنجره استقلال باز میبود تا حالا قراردادش رو با آبی‌پوشان امضا کرده بود و یاغی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25514" target="_blank">📅 14:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25513">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FI3BrGEhhQH6_F7beWpHGlANfAj-66f2EPozfNlr1ltDE034-svBqKpIhsG2BBr7pTYMjOfce2yeqsockapeWcJQBhyRGfL0G4bz8U0yG_jPxBxnQHkVWv0gw8_Dmin1wLnyxgoPVdVA_2qsbp7e_dt7KrlA_AR2mdIbIL1zpAXafESpeAW3ne2CInMMoOn81-H6rQIqhk8Ao_egrJVnwIk5AT6DpVZ-CW7ZGIa4Gj5LEoczRbuS763FGwFQ54IpO-HnAg2EqnAEWVnZszC4o7fI-LaTbzZk8oyXfETy59s8UMLFNsYwXXoYhQsNa4pu1bRSRcKfX_p-7LO9K54vBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد کلی کریس رونالدو، لیونل مسی، کیلیان امباپه و هری کین در تاریخ رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25513" target="_blank">📅 14:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25512">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=Nu__eBxEqdYyyz6RvD7exTpCwSHPthbmYgdomxrnhV3BrPoTIXUHIwmFajCyoil4zBwpSbGvaii-X8PvhumoUewHf-4k2RgIMbLrlB5tsdr3H6rdnNN8VC8b2kWQdHOtXxfjVJ7FXGYeep6LF9VMm05BlfHWL5loxy2K0B3e9EejQWg9htEKGX6ga8ekc_rnDyJmKuZk3gry3fu-k5np_wXamkvXCZiHwT9xUNkC2Fw_VWLcG5Sb2D70-SzaOHBR-d-a4m_6f92hhYz483n5iR71KkwwqxPKBmKK05INn8lxMWIv4DgPPURjnJQJy85LtQ8OL-QRgYRws1OUP_W0nqKsHm5d69YRndr6u6Kx7_Giny_xHX0b7sQhO-iwb3z-e8jat0_X6wj8wulL6QZ8xXCpNC2uKmiJQcm9JRfdLKpPEIWUI9MwdE663Jg98z0fB8_uM34polG7QywUw_XKx3pWHVrg4Hx6DGaRNuTEbBnhVa6uxyP0hP25wJ6KOVEBG29bnOm42rjz2XyTHFkA86XTPdliltJA3m7frfYenTUQ6jWnw7IYxmJqJRdSeDRc9Nq3vp3jjqtlKFICuI_ZW_qAgLTb9ojkgRSBR5tRJfK3YUpkkn6xXBaP-SOuXD1idBKO8nLemsjYETMbuEOpnckW-PPzauf9sa-gJYfOzhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60fb9d0fb5.mp4?token=Nu__eBxEqdYyyz6RvD7exTpCwSHPthbmYgdomxrnhV3BrPoTIXUHIwmFajCyoil4zBwpSbGvaii-X8PvhumoUewHf-4k2RgIMbLrlB5tsdr3H6rdnNN8VC8b2kWQdHOtXxfjVJ7FXGYeep6LF9VMm05BlfHWL5loxy2K0B3e9EejQWg9htEKGX6ga8ekc_rnDyJmKuZk3gry3fu-k5np_wXamkvXCZiHwT9xUNkC2Fw_VWLcG5Sb2D70-SzaOHBR-d-a4m_6f92hhYz483n5iR71KkwwqxPKBmKK05INn8lxMWIv4DgPPURjnJQJy85LtQ8OL-QRgYRws1OUP_W0nqKsHm5d69YRndr6u6Kx7_Giny_xHX0b7sQhO-iwb3z-e8jat0_X6wj8wulL6QZ8xXCpNC2uKmiJQcm9JRfdLKpPEIWUI9MwdE663Jg98z0fB8_uM34polG7QywUw_XKx3pWHVrg4Hx6DGaRNuTEbBnhVa6uxyP0hP25wJ6KOVEBG29bnOm42rjz2XyTHFkA86XTPdliltJA3m7frfYenTUQ6jWnw7IYxmJqJRdSeDRc9Nq3vp3jjqtlKFICuI_ZW_qAgLTb9ojkgRSBR5tRJfK3YUpkkn6xXBaP-SOuXD1idBKO8nLemsjYETMbuEOpnckW-PPzauf9sa-gJYfOzhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اگه ایران میزبان رقابت های جام جهانی 2026 بود؛ این مسابقات جذاب چطوری برگزار میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25512" target="_blank">📅 14:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25511">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrEm-rmbxFBxth1VzwCb6qJiURxM3SNZp_iyUDgzUcp98RHk1mLUslTRWyNZnIdl0YFOmrVDSyK8MxRg3coZnbV_bfl-sBSERitbsPmkIEIMGy1tS5wvEHMpEvSs6p35VCBrapGqtq4-EneifS0QhpxNi4BE7tFLsHE2HgXz8rIE3BfOgAgaEj9q1-Xia6oWnw-wTtzb1qBmMDt3Qyf2G_Ao74SxgxWdkyQkcmDpmwEL20nsx-r8VIgmOHcgSyfQYhVYsMwG85Vp9GLsTTNpcJjq83VdramuuGX9pLfHSKvNuVP76BPm9QFsKu1dkbeHAQIYOJpvIFZbqANEMyF3HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25511" target="_blank">📅 13:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25510">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abiqQHOIoreesN12cDf-z7VwL0oXPALiO0Ek9ZKyKJ7ziZiJhm3ZrW3FwQ9QHYrUtWQDV5HKnzdNi_zzhmbwGXwEFuXXCuEBpdwQ_BfKg94PJHK3PncIIUSmKYuH3xS7XUgucMHB_AlxnxOTztaaVIWf-F_j8B8ke8DWtq_bS7tYJUjqJC37hvzsftGHHxQUK-8KAzuPbxSOSVrP9HIzzuEXpc_WeNEYlYW3rdLHVcKjpBj-o8ZFo17B_ECpAZwcIPBTfpTwgu3wOI1VPhNLuuTObFj53cwQR_0tQEU9SQLmn1FrlkKjkrtgTPj28IwitX2wtG9DORFK4UpNidXr1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25510" target="_blank">📅 13:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25509">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmGfO8_fHcDwRQC62TF0CXz1QvxeqMPSPBsRARS4u1CR3wec302kg77vevAMQW6fGKidaE_I7BXyZ7db0ZYyCyQcyoEAiFKRhbYnQw3_9aHwBk4OGxFAbDoKhRlP4dFOezzO8DjxEi3aJBbLGHgCew9Dh5Aqsr9bsTsdk3z7InzdSHBCxBz3MBapBGhKjw-mHCmmKxNfveWTTAz8Ne7xBzeqq8GXkpQQdMdA_DsQMYIJ76kJtGrFe5KFyUZjWALin7ClUTvfWNSuBdpuC3OdUdZzdi3YV2ZBqGSeeJdncrz26kjPtSnz6dyIl53097B984DAfqpDABYjt3sOsSOWIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25509" target="_blank">📅 13:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25508">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBeTdb6sXeOjux2qF3b4RUGHcMDSvRZxYipPH1JM-HMGPfn2lsz5kezIbxoSheWpoS33Ppe9BgV3HlK0NMTt0McHXl8I5MamBtre2OFeljCQGep0EQNtUgTN_zApgHSS--py181jBG_kqE_p-VgKKDLA6EZ7k1AiVgC-CxhBtOhO-3gZ7i4pCYXMBfg6RdbnYkZK84y102axmdizk3qXC3A0LSvticD0aaSOAKdezJm1bOtb7K3wSTM5ajDw1gLWvS457PC6ufGBw7Gv-MlojZsmVKLp6JKLoQJTa5Hj9wbXPV0qbnUS4T0nSadysbcK9AeFIxbLpL1WP7iy3x2QIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25508" target="_blank">📅 12:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25507">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXtTEfmEgh8OFzGaOTWyErnTHzg51nnf2F70PMipIOmC9CCkf7OLkVSnWFG-8gU2AmRz-B_VxC1Im661F-zrMPdzsQlzmSldp0GNPZmijujrAnzKZZppKeALExpVQzgkfx0qohF7e2FwTyEYOEJlMyNih7l8zF6JRKaPut1MtRBMw8EqL-2uMGftMJJkar7D6G1B8QmbFbgDPKAR_74h6he71xsVxp2TgmBvIWj5-IHjOchxmd-x4Xzfk-laCX47-rF5_Xen2KWePLIdah2rHiehBC496KakfwYaRaLHb4gA7Fs1kbdu2Ql1-kMVslRPIFkIdpuEoNrdBeQL9DOj9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عادل خان فردوسی‌پور پیرو خبر دو روز پیش پرشیانا؛ مهدی ترابی برای عقد قراردادی دو ساله با مدیریت باشگاه پرسپولیس به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25507" target="_blank">📅 12:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25506">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6pirnEhanEAfdU1fFgMrlDSrHTWqVc9_8CX53tnuyVivvqxBNwVT59aRqjAxaQ3z1nNDHZv_q6gqS4DHE4E925jLKZv2EPdYWXGjaXa9z16Ekk2bviYc67MKKkEMaWlzEyCqPqR7yGjShx_Ca-t1Aeudy5vkljMhhjnGsAA2hw-6c9yExYQIIa91AJT9AJHwyvklPzk1N6K-0c6UmIGICYbC1QXlooidCx8602rrpoO7LAl5xwUzdZ82EHmh16xv-Dd2mHY3Ga778z-k7BacvvDz3ACqSdyFVFiuEkAdRxjPdfaz4JDU0Qbwe7tIdZQux4cqg7svitn8QYZ8vWS7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا
#فوری
؛
سهراب‌بختیاری زاده سرمربی‌تیم‌استقلال روی جلال‌الدین ماشاریپوف نظر مثبت‌داره و به مدیریت‌آبی‌ها اعلام کرده قرارداد این ستاره 30 ساله‌ازبکستانی رو دوساله تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25506" target="_blank">📅 11:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25505">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=R9TW80hO69-Yv8KPtKcUpk_fp4JWDY_tBGCFnhLMDbKu2nOrUusomzAuZHfbU0JTKd1R652My3QFl7Qqx5XN2Te0H7S8XPrDoMj3usGYPR1xoM8p7ETHTWKC7a7guUTTHexCu-U3cB8ypdIJ4VjcN-786a9cQsA_uZmbblxRrqI5_pyigdmOc9s9_HTSOX79d_y7uBXP8qTSKzQFYvM0_TbxwlYQTnmkiiliWXDAe-03FaAUmPUMUOdA9p96sI96X7LVGATNsZd84zP7WA7M_rGOTCaB1Gr3hpFGisDTc9_cNce8YHaDH8YZj89ARB9f4IYq6k_Mg2-WCI1YCwumAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5482437b.mp4?token=R9TW80hO69-Yv8KPtKcUpk_fp4JWDY_tBGCFnhLMDbKu2nOrUusomzAuZHfbU0JTKd1R652My3QFl7Qqx5XN2Te0H7S8XPrDoMj3usGYPR1xoM8p7ETHTWKC7a7guUTTHexCu-U3cB8ypdIJ4VjcN-786a9cQsA_uZmbblxRrqI5_pyigdmOc9s9_HTSOX79d_y7uBXP8qTSKzQFYvM0_TbxwlYQTnmkiiliWXDAe-03FaAUmPUMUOdA9p96sI96X7LVGATNsZd84zP7WA7M_rGOTCaB1Gr3hpFGisDTc9_cNce8YHaDH8YZj89ARB9f4IYq6k_Mg2-WCI1YCwumAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25505" target="_blank">📅 11:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25504">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_AM3tX2sGaZm-CwFvO5BlncSTR0yMU1YV-jjryfWn6YAz34KGbc4O_skplNfGQM0TcEXBVQs9IvX2-4hB6T_Q2PGhKW0iaAkGoX1QYxeQrtkMfjvQt7zf9LIy8WP-r3UdT5Xmcyv8ZoeKT1IzI-wmYr476CLuJJuZUp4Hmb1GdSAKiATGan6X026KqOM3HB-6RShYLLTIp_w5GTMkTWdc-PvBq23JVsL-LuzwauHbuakMR7KkkA2GhZ8yEV_yWoDuUIuXK7mEh5Z-KUq48YfyGp3jFE5ImoI0vZnAoQWGi4ynGHDu6TXJYmtNQLU96jOofPwfODLqSuHsra8FyFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25504" target="_blank">📅 11:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25503">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHCBish77gbNrGk3GbMZcCqmkJ4mjS3ryC0eaiRLu5EJr4WIL_Oj31kLCwh3Ng3TZv_XKVmIzrmC3QhqxgyOTbnx08_gjA6kyF5NPLaa3N5vHnRajW-bHJ6PjunryDQBobH_bQi8DKrh3VHFEojx6pj7w7rrk9YdLfpIfllDBmAk5BaG9WVInH9MneUPj56eTXz-sJNZ7GPr1vcophnnFopl5ZeFFAGSNgpYImYpQ4CPzslliPZ4KuOY53jYvZRpKRYBDIoDiALZH3Jk0byIP422sNWq__IO_HrK-net2lPJlZA0Srw1z3haVT0FxuAG_qTCdoX12980mEu_mz7v9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25503" target="_blank">📅 11:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25502">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=vmPK4lMAfCrnCbdMThdEN4Enwn0DxLFALNhu3zrsECijt2iYAdyovUKFd5FUqQvwk4Uzk3M9qiexMthvCjlqKjSFKNOBBOMyyIEsvSQo8TDxGVv3dG2IUAp-jME5brS30hJWG0V2Ixfjg99ruiwsCifdlDAV6vh_xuz10U6ZVFkkBbmbSHvozx5KH0FnSxG5V6e0AmkXHjMYtvr7xKXDcf-U4mKI41rgdI_att_T41rM7ZDo7c7J4py-jB_gQJoZ6p2I6GkBj_0TyWne2fZ_T5R6RFC85u7AaMYJCX7UH-pp1B5Qtn6zu9FHdDX1Hvj7rN3TmimyaPK_E36V3Cca4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=vmPK4lMAfCrnCbdMThdEN4Enwn0DxLFALNhu3zrsECijt2iYAdyovUKFd5FUqQvwk4Uzk3M9qiexMthvCjlqKjSFKNOBBOMyyIEsvSQo8TDxGVv3dG2IUAp-jME5brS30hJWG0V2Ixfjg99ruiwsCifdlDAV6vh_xuz10U6ZVFkkBbmbSHvozx5KH0FnSxG5V6e0AmkXHjMYtvr7xKXDcf-U4mKI41rgdI_att_T41rM7ZDo7c7J4py-jB_gQJoZ6p2I6GkBj_0TyWne2fZ_T5R6RFC85u7AaMYJCX7UH-pp1B5Qtn6zu9FHdDX1Hvj7rN3TmimyaPK_E36V3Cca4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
نروژفراموش‌نشدنی‌ترین‌تیم‌جام‌جهانی۲۰۲۶ بود. جسارت‌وجنگندگی‌کم‌نظیری‌داشتن و شدیدا دل‌همه فوتبال‌ دوستان رو بردن. به قول یه بنده‌ خدایی اگه ایتالیا مدل گتوزو تو اون گروه اول میشد جای اینا میومد احتمالا این مراحل رو به چشم نمیدید. من خودم بشدت فن ایتالیام ولی خب مدل اسپالتی و گتوزو افتضاح بود ولی مانچینی درستش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25502" target="_blank">📅 10:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25500">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlpakZm6OxMzsson_Ihw9qG2ucNPqSb0pcw20eNNGQ2kwZIUN7DXBwffAYcpKC73hxqOColYmH1Fth3qLR9V_90Ox86My3mMLXSVqltU05-LWEJV2jUwvaioT5W3TakrzctJbkD77GPnzawJJWR5ZHvKdai3wrPRc5ZZHR-6VBBTpQ1Anil8rl8Nm8n-MKeykEyKBpQOZIyZAXzH_LZyqiLNnyJw8rY6T-S2bEHz9-lCMYPvWkMsfsLMZCwhsIO0p5VB99zUWQC0GyfBxhdbSVQRuhVNqA5E4QWGige-ryV1xb43oX9WYoT-yVi5uNAN2bqattICziria4L64qZNXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=LBUEb5FYtcsh-9yAuJ19mBcIGDA-CXJoGYgqnfDbsG1M91WSFmTkd3QYyXnONrDGLipIQrbmg3osRqYgb1xU_sEaDdA7KC0e7DBpGw1viag_sNtsTYqVdlI1buBJx5Nxb_ECJQQvd5oN3lrcVzDaV8luFDTy7p5Jh9Fu3XNIbqSlglG7ITYMvq_jbq7MSwGhdXmwcXSFURSL4QrAlHCWhUo0BIFN1RzPB-4xBjVOYkduKx4qcTBTQCAAnoMYJfR-7KVQkcAFyLBGnS4Ge6FgpaEVIw_okmVIMOGlHkO7RewwRDBFOKI3MCmRFEBmbIWUE9Ri8_VcQzzslUZbG_pYiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=LBUEb5FYtcsh-9yAuJ19mBcIGDA-CXJoGYgqnfDbsG1M91WSFmTkd3QYyXnONrDGLipIQrbmg3osRqYgb1xU_sEaDdA7KC0e7DBpGw1viag_sNtsTYqVdlI1buBJx5Nxb_ECJQQvd5oN3lrcVzDaV8luFDTy7p5Jh9Fu3XNIbqSlglG7ITYMvq_jbq7MSwGhdXmwcXSFURSL4QrAlHCWhUo0BIFN1RzPB-4xBjVOYkduKx4qcTBTQCAAnoMYJfR-7KVQkcAFyLBGnS4Ge6FgpaEVIw_okmVIMOGlHkO7RewwRDBFOKI3MCmRFEBmbIWUE9Ri8_VcQzzslUZbG_pYiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25500" target="_blank">📅 10:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25499">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osNzQ4r-AjWl0XkViU4AfjzS_euMR6qSjke8sREExKboNn1ySPVPJ-XVHvR7m0L3uD81heQ6GYPgaoETZI8t0kLfz8aG4p8sNq1stVQBE64rQdouptDHn12dIqO2ESbKgzRztgu_eyz5_CV6_GdJvn02etHXs-tlIjA_lHixH0ho7mMB_34RDAaRyk7Lqq688rdVbHCoU9R7pWEtJE_VGmyiraFX78jjx4Huva2EI1mvs_428XUGGSjtzQUeeRUPnz_6Hsq1IgZaGZyEZ0sDTBr7MSlI7CkftRs8f1IX5e5fCdwJattXCrWWD9bA6ORJPaIICF1o5MLxUuPwQrTnnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25499" target="_blank">📅 10:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25498">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMP1CEQC6d28nppgkY_c0AC0r_cpv_jmw76DvMGh0B-2l2o4HfnO8PBxGyNNCrp0ouvNUNgkL69_VuLZ8NJ9Fpe0cfW56M6b15aUzCIrglSfpp5NM1TD6ljaOfr8zjQLoKsw4ZC8RFtfKFEBlCi-2BQvB4kcxv0hZyAmrQfYC7zf_rK-r31Bj6c_dhaPpv9ADI_mfQ3W39dITDiDavu2Zhj9h6dRnKmeC-8u0L5tZECNbUE21zZu2iNh6QJ5YfkihwraisuDQdf1htDwrrx3aaEtT0c7DBb6_wncKRF_mfZfKKKTK073184B1NifwkqDoEhmTF3UJm4NsRsAbXq4aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ جلسه مدیران دوتیم‌پرسپولیس‌ونساجی‌دقایقی‌قبل به اتمام رسید؛ نساجی‌رقم‌رضایت‌نامه رو550 هزار دلار اعلام کرده که حدادی‌امروز درجلسه‌به مدیرعامل‌باشگاه نساجی گفته تا400 هزار دلار حاضر است به باشگاه نساجی پرداخت کنه. قرار شده که ایری…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25498" target="_blank">📅 10:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25497">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=s1Su0akzdk5JL1Cyx68l_thLPhUbgkj1VCzJCg8agKMGG20dJVFucHY0Y3hC1qb25DkTZQhYcamLfj3Ehldxo2wjCRip6NTaT_LoMRpuQXIlQjy6hYKXBApFdUy1os-s5F5fK81cCxEUtAiaJeoiwH8eBfpKefQxSUBz9kENcvWoUOwDhHNqshxIFhIR3kSbcToqkTG-HUXyNTg2FxPh33iJ4hyLTCoTASIvQdGrLINPMCrVq4c0G5nKhcJLuATU_PsJ6iLOR-Pg3IuBDKhhUhLKxOpKi2bUlOlZnfEFv9LAhQXltZzfYbY8D_m83iYWSlNDE42jcgfmNzgd_-yGCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=s1Su0akzdk5JL1Cyx68l_thLPhUbgkj1VCzJCg8agKMGG20dJVFucHY0Y3hC1qb25DkTZQhYcamLfj3Ehldxo2wjCRip6NTaT_LoMRpuQXIlQjy6hYKXBApFdUy1os-s5F5fK81cCxEUtAiaJeoiwH8eBfpKefQxSUBz9kENcvWoUOwDhHNqshxIFhIR3kSbcToqkTG-HUXyNTg2FxPh33iJ4hyLTCoTASIvQdGrLINPMCrVq4c0G5nKhcJLuATU_PsJ6iLOR-Pg3IuBDKhhUhLKxOpKi2bUlOlZnfEFv9LAhQXltZzfYbY8D_m83iYWSlNDE42jcgfmNzgd_-yGCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس‌جونیور ستاره‌برزیلی رئال مادرید امروز 26 ساله شد. او تا کنون موفق به زدن 128 گل برای کهکشانی‌ها شده و همچنین برای تمدید قرارداد بااین تیم با فلورنتینو پرز به توافق کامل رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25497" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25496">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_K3xfKYdSEqF4KMen79VBDYBGlUyJtT9nQvGTQk9dQZyKRwB924-bPoo_QCjZRZYZx6B5lg5jfLqPnFA7vvE78h5-p7fdT1tlvzOwoIZeX2O-B2O6i7XBFL57jGYIzvS3AjuhSL8QIpYomc4QjKu2ug7ZXMeE5AInf5JTJS2KE8cVx1H86OBbjPSBGSzTRO5bNLmZoSpvOONqHiSEKBEu4lilRy5r12TzpC1E3kDayYPZaY_DUsGrhSFy0fjQEJZlgr7f5Ch32wSrWM6u9OEAdZXbAA2XMfk5hxHUhQTTcCRgHfPP_1EnSWfyBxLhll2qkpymwojSSqgyy9pyyS5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25496" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25495">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=UqO90rfV9rfU5ABqM0-BlWgDbrvtdDGOBZij2P1rzsJ6lbnr-OcjgiG7CT1xVojqri6vIksLURgMBKjFPC76oihkt7LY9PsVGRYain0o3MZklaAGIDaUNdeYQr7jy8l2aj6tMfELAWvNW0NN0ftP6lVs6WOyP1sZjdZ9Vhg6GHuRaxta6GITdQ5LdhtA6yq7v7f3ci4Zyr1Izv6PPO4o2Io5j7wl0FA7KL384fFf7Xv7VmuvUe2ucggGOXOZ3C-L5jEz90CvLGFuBFY6Hi7s7_ab45gTIZGfxiujk4yJ2b45Gsn3BPXdyzPen5iFe3kJmXkKiwogORbgt3a1JyzMXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=UqO90rfV9rfU5ABqM0-BlWgDbrvtdDGOBZij2P1rzsJ6lbnr-OcjgiG7CT1xVojqri6vIksLURgMBKjFPC76oihkt7LY9PsVGRYain0o3MZklaAGIDaUNdeYQr7jy8l2aj6tMfELAWvNW0NN0ftP6lVs6WOyP1sZjdZ9Vhg6GHuRaxta6GITdQ5LdhtA6yq7v7f3ci4Zyr1Izv6PPO4o2Io5j7wl0FA7KL384fFf7Xv7VmuvUe2ucggGOXOZ3C-L5jEz90CvLGFuBFY6Hi7s7_ab45gTIZGfxiujk4yJ2b45Gsn3BPXdyzPen5iFe3kJmXkKiwogORbgt3a1JyzMXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25495" target="_blank">📅 09:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25494">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7uNKiDfTwsDzi0NjnqzyGuoq8QtYPSz7iWiZMsUD2GqeNeoHDxSdSRotOkEC5CaBBf3CIKiuaKOuTCWyzQfGqxmetcpjOJvvJvF3lJeoIosA276RU1yvxOgevngnBK2jbtuX08Gnf1-i-oFgZ2PQ4Nj2fcNIxxYg0vhf6Wia5ll2N7Aai0Q0eTfSZFjcF20S916e4hqDEc0dEQeddV2ktwfN1kaQJ2DX-dQqERSH3GU1v4ClY0VRIVrjUJR17ymuTr672eyYeFzvRfVJxqedF0y8J-vCZ3rxHd6GiPDCIJjCj7hZ6iIQ4pMf8_aVZR-aiaCPSt-2vMVABf6MgXcqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25494" target="_blank">📅 09:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25493">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1rlfcj1wdK86ZxvjmyFrxjw10E9fe5yg-CRQjtGpg-iAchg0dQLppWvM1tcHqa2FpVqvuteE6236Bk45XHRndOo3n6IHhHc15gbQBamJWP_cur9z7KSQuxu2pWLNkjDyBZd4LtrTbh8uxOwtzuW1fYAls8ecaYMwKLvgwFVGrcnjUBlLHHXcY8mUtmG6b2DqUUBe0wpB4Ibc1T2KoEWUfkTbnqqfTlBmBNbrsWxDQ-Oet5tmNun7tUauumJ_4EGRVvk5W_R5mW1NlrKenY6JqG-aapsR1Jvq0-6KkfJZsjz03x7csiM_EUqOeFsdiX5Q65xIlDRXsLn9bU7NzA4VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی‌رسانه‌پرشیانا
؛ فرزین معامله گری مدافع چپ پرسپولیس بعد از تمدید قراردادش باسرخپوشان راهی سربازی شد و در فصل آینده در یکی از دو تیم فجر یا ملوان بازی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25493" target="_blank">📅 09:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25492">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QD0-QWQc90EbjRUHPGc3gufaTEBDnMl-TBK-tOhUFIhGkl-kz6krBCvew0HdUh0A6A4KJIfTJyvrfBbQY5HmaApfGsrk7SMJt12R2DBXM3C86hvwXQkSqIJ8NaiI7dwoO7tPOX5fYd8Xz36js809mPlnO-rn5cS9N6WDtG1LbxM0IcYOgbjb7txqQs15QYqgeurgP6ApVPSm2IjU9BWZqQ2sJAc_DhObKnCfMntwW9WXG2qJrdsdBP9-6PQywha6CumsWMlbgg_WDM7JhqPDIQj04Z138z0-CYi4DOlRI_FxAlLJEI-w7_Z-t32p2NKKwXF3-JwyFKqygki9kzGToA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NzqjFCe4rSw1BY5HMdyrfwuQ4X3XsNRmoZXXF9PvZJOwxgGOb12uTfgxEjDpZIjyXlbxXX8yXdB7mzEwjAKyRBLFR8C3JuIetBfdW0PUl3wjZofVCt1kGsT-0t8qqKmcXs0DuJrfrjKhGvsqQKgOrraz6VuphffEIFpk47jS5aikpVoyjgKqTC-RRDYeiG9-5dN0tuDIXr46EjArKt5KeNRsX4oMUBy4s2LehcFef9lFdaM0LZ0G8wS0TGg9VWxwgJ9iDGgtCCvIGG1RZwfwVc5vEUM0yEal-3ZtlExtkGiHGS0_PolRKsI4Gc6nKfrRrTZipYQhR447mG6iDimSrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25490" target="_blank">📅 07:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25489">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dW3KyXhICx3YHk5cxUz_b0ztigmJW75hIkicXKrm_pEoOuLmL7FsivvN0zffffzHgguyNqStrlPWWyCi7SgKtQcCLDkxDQyKX6P8x7X2zw67ofemaiHlf5ZUkG3LYEVvp7SVPyQn3XY9qDi_a2vtpMWmUMbwbOiff5DgfT_xqzAzjeq8HWQxYycEKNpmB3U6XNJ_8ql1k6OHMnofUtx2T03MH6dxB747_OGAg0vhXPJvFxDChBq3rx432boyNzI2axvz__H3yjSJAd9Wp141nMxh8Hb4Sa8FKaRsQcbADonqe8cqitEKDFUVPGMd0dbeYdvHRCsldkGACEulL0OkaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25489" target="_blank">📅 07:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25488">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hN85r-p57mJkvGfvaFgE0tQC8mRBhe67VwY4-10616pqwCdPWQs6cDRXyXe_omThS7eBFF_gLBZ0rbSYc1bMgWxJHfqA1mfP45vdLi0EQqhgovKOpgdsXUOs2Ko0Ox4EsjVFsnNyIX0ioxXDHyXMbf6zOFphs9emqxDVmVcZN0BJQ4jaftNDmh-Bu79w6ncSpNR8lvdMiUqgGlHhH0lO7vtA3pLeHA6x3c1gOJPChfryJcm199of9NzZA4jGGnwYpsv_7nhm6WD7EpTnFwusk2GHEjOkMZxgnBsVKVVV1oL0rEiUtpGS2V0XNS-Of69j10amYrwEPbMzgbtIk7cTNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25488" target="_blank">📅 06:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25487">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWvNkgGe7pfEpUHi25fHJvFehsa1fQkFVr2Ga_zoWfBcKxphzP3ccMuSLh5fMHPq5pYjI96Ob9zXz-N8necTULYNpYZ1m4LRpW5Hxu_zlNhdUzyrUBUgwqtTRbVGe_jW6aHeL1gOGRM0_d0pUdgq_VG9mrF5mI6MWIh9sjyKmVNPlSQyuzkTlkZnhy2SQoW9zEGP9isxfF7KyB7ImBOilbbgtvC-dWCqZGsQhOyLlGA-NNz9WxhIK84Nvg2GpFaTzDvZpdLfeVr4t5dyCcY8PFOf949eqo6XMOfdcjZd4Rx0DcYjZiKKtMdrLTGu89cTEuO926UntBfL8OFqDudkeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25487" target="_blank">📅 06:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25486">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBHitqgukVdG_wQWzvbwgHkwWVrbvBUXz4o0SKPu2k3S4Ug_2INHZ7oHaaGbBqdoDvZXNW0vG9DTgqG_XEErOsshYcOevN1s3bd1H_emeKSQkMirrB7J6ACYjm5EplPXVwwN41h0cCwfbjG2eoagWgQrzW8E0NMxDqil0num2XaIIm4Dx8EN_h57K1yaU1kP5g6jwbTlCURLOPVE0uVcgQMK0DuvgtqZ_5eLnp2awcJCTVJvJuBQirgk0HcaFAJMZ4lgsNpUKcgKZnlTQrAxvY3HIZFs0CL_4-KVntU2fuS5E4goLdWatYmvN_dqopmQL59z0B32dJlQDoLSLWLpzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داش‌چیشد که به این روز افتادی؟
چیبگم اون شب جای‌درس‌خوندن‌نشستم‌بازی آرژانتین-سوییس دیدم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25486" target="_blank">📅 01:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25485">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=JU8NAaklYU_34SyO-pw6Ni9CGAuGDrfrhqPxSFX3Un4vV2SYijiU_dZP_ti-ViRNs1U7srPwpQ63Ub_FYTU019bIym7tI5VHIf_3Y_H54GRv7BZRrxZMd9_CVbl4IZluGJGfDyAY_GDMlo6etwMgqXOww0WDmGESrUTt9bdp5YDeki8lJPl-6tSypqn6wmKyTisRCQrj2kT3e4pf_vce-3SvJVovYIcTBjHVt5-ztVTM65vVZfFMJAq71pE9OzFKI0GXDawMU3jO_jT1CxUu-1mI9mfnjnDR1HFHu5CqCKFyTS1V6XbcJzbxkIxpE36HZ-g7TdkmqLUR1-ugFimqdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=JU8NAaklYU_34SyO-pw6Ni9CGAuGDrfrhqPxSFX3Un4vV2SYijiU_dZP_ti-ViRNs1U7srPwpQ63Ub_FYTU019bIym7tI5VHIf_3Y_H54GRv7BZRrxZMd9_CVbl4IZluGJGfDyAY_GDMlo6etwMgqXOww0WDmGESrUTt9bdp5YDeki8lJPl-6tSypqn6wmKyTisRCQrj2kT3e4pf_vce-3SvJVovYIcTBjHVt5-ztVTM65vVZfFMJAq71pE9OzFKI0GXDawMU3jO_jT1CxUu-1mI9mfnjnDR1HFHu5CqCKFyTS1V6XbcJzbxkIxpE36HZ-g7TdkmqLUR1-ugFimqdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
واکنش‌جالب ابوطالب‌حسینی از رابطه سرد بازیکنان تیم ملی پرتغال با کریس رونالدو در پایان دیدار مقابل اسپانیا و حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25485" target="_blank">📅 00:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25484">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRr8KddaVnTCBYWX7QnsDRjCJ78NVcLPMpOJOv26hRs9_Wyw9NZuHYpC9Yw5sKrFrIkKPmjFvsQwJsL3IRKnxOtaEf9TKK6KApGmDUicBIu5BTmPAlSr3bAr35y5bu949In9LP3VEpt1gFpo7rFed480MOBTderqm8H1vHs09Ey9JLWojoXodx3MGzMHc9fJnTZ4Cnh9xVCwjqM_ExWA1Iv5zf6O1Gqk8fdNpsJGuuy3thWthht5y_oQvTElcSsqP5GhxMwIeHyK5eNEpGXFut3xMTvwfY9Ua9s7fFtY1Bf8C6ZaeSQCmo7qxIO67Si5TiJiuRkwzKUR32lImXC7sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25484" target="_blank">📅 00:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25483">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLAcsmM_5Pyr_HIA8ku3s555WRycjsACGhxQhf7TnPv43Fo45sMQ4Js3nGaBIskhVt_Y2nBLCC-_f-gQCwXA9SXI2XhugyfTdJXlfRtMzTdDu9uMHGa440ePCoB97NTsCqm5S08LOsnNKH7ljdL4D-72L6IVZoViJESoWi2nriHMnd16lejFfR4Cp4vINk9QrSS_mdifG_iYOxwn1gJ5M1Vyn4jTCyKfhCTNmrN5tvnTfs4AS_ZJ0jfNH7WZbRVbP7ebiztm2Xe0velXg5IWCMePHf8j_Fv-SZ3h9BmNsRsFPh0MLWGHNst6NPNPccSEauSkIR15D1jH2czzRFanYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25483" target="_blank">📅 00:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25482">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3GZ-4sf4au5pOuqzVdvsi1XmGJwBan5YZHOkR2WWdtcTtLCEOVB0ktKH4KVLvNAFxGMEHiL0hkOXL3DeU0bO2llgda-phXY5N4UXctrHD_xxm2QBsjlq1mLJ07LiC9PgpbHVE9lQiqKtZm9uabFS3RerASqbj3mV43IEzdfPY4YmXEDTWD-0ZnYKjzfv_ihxKTduM84PqPNOlIfRFFGI70Xu3XOHAvzYPejgl6xkkd9Ynl8ad5hOFHeDFNIJt8pmTIiysE_hPVH-w2P__z2o7ghoCOurgdbtShdwLyCCfpAhJ38xIwLfKvB68WGqrAKDvYRFGpNQ6NR9x7U72g2RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25482" target="_blank">📅 00:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25481">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3wgCpUJWdcxpL0aWs2J2i2wFnptAHnM8fMXQexf-vor-n9NVqrkXpM7UxM44dRtJhNNRZgHEBbrEaW9qQLIPMAkLxKo1qQnS7qQ7a7Fv0a670ebN40vPXW4rndvCP0e_AYR0XzfHWLvrNAjhninYB9A7cHVdHNmTtZ91UmGzxx-opKz_F-_gOug_tz0DZFGwdwB62rtzl2lQ-r5TGNYwz5QjWqL6ClouGnvH7ItdRnVwioJZXPiaVj28_uJKa42RpZ5hrOETSN7QaOf1EaM1ypZKEDnmUKc6GZpqbC2tyqdBkuNBpiIhtIOM9r826GUREb5NTH6_x-Tw5WRwQ0xAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25481" target="_blank">📅 23:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25479">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v-oNwRsRWkUHcjztrynMfjR5jQKDgeFJ6MfK6-mQhrJ0reATYHKXRUecYqD0jDCuxEKo8VtHvfyTnmAHYd_8zZsYbIDuruwvlDFAWJGViXabFzS07eZ4RveJgRDlXR35JvWL83_uT_uhE3iC_aGEyCmvtjMxA_Jue4zk8Ndx4uK9iOc7JjvLyfzsmpmkUf9TZBvyusKi5j5m01_96pvRVcrBv5p8Eo9sCkzPJ4R_t82CXyCCKS_oRRA5ccHTor9JWRru10xVIrcL8LdrfIY8GMxneZ5kCkgbZ_EPL1MTkzYa-COOi9XMhkvhCzWy-Ej6OYr0X0yMN3ww-nRtjCbRYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k6I2tVyjH_8ExymAmoov7a6JupXTSqLQjxyxO8OsUXcHjWDjjIIB2IhpwelLH09moj-gglmbKUEUp1iQk4XERY6MszLwlLFwzbw1idFIzQml-H3yH8OGWZp4cjppfQwobxuX5VK7LPdM8NWlQ-1YW6XhMviyl6SlSJ1xP4REXeEgcHWc4rZEvd2Wdu5gt-Qp39oAAgtGk6OC6NRdE7dVoLNTxkNiYnpbJIVQgXvBODGh_NwfisgnZdaMO2eomwhNwHvl69XDYVaofm1Mq_NF2PJqifwK_zBWkVr1mGlOPyqONm84VPjB3TidAXpGJVhtlPxP33eJ5GA5UgJnnGQ1BQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25479" target="_blank">📅 23:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25478">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pI8jsCwC3YoiI3B6bK7z0qUrpnTCu_cqSENCD3i91WkQTfabV-rWrC1EF0zKy-_LfuhYVcWG_xYDXKXrqqBh8vPyhnFTttI2VQ0li-8voKV720qnVLa7Bqm2i4DQg3E7L6GIyysvAuWZHsnV7Ww3haKBAwF2QPoP6faZ_bXED_Z7FaGauiGKqL0K32rQ-QDJ1aiiu86DOU-TTzVaCAhnK-yzr6WyBayN5Xr29h7PRceH_m6GbfjtY5oitpXZ_PcRRHiYfW2k3Bk2_pOX5OZHETE_WXZaPuqwbcCXBR_6d2_N3F6lO4bAA5RlzT48GNX4S8GveeTjm3y5QmzpqZBR4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد سرلک در حال مذاکره با باشگاه فولاد خوزستان تا درصورت توافق مالی بین طرفین به این تیم اهوازی بپیوندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25478" target="_blank">📅 23:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25477">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwDGf87YpWNkL_0JqDbkVVsDQ-ZfZ449qSuvDvsx0QY3m6xhzgNnQewfKihDTfCZOX7iyuXGUVsQg0z8woINrW9KQIchhna3E6VIPTnow0TU4oNlf1-mSGeKlEB1WagrxuK9iTIJr6kyAgpl0swGYLFy5_BnXCQd06zEfQ0VPC_buL2zk5Jn_mOFrjO1fzjDM_nBHIbiyasu6em9H7HUKuxWm5A8QZ0EXdKindb8HB3xT0tWgsS_WkUB9aJNPYgelKnYZp5yAqjqX_Wd-ZT65xBv3G5E7GXn_Gh80Joy7S37626ypM7iLHjKWvBybzwzg5lA52F8Os7BEyzCHVmiTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25477" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25476">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fD1aEkPYxVgeM8AFof2BdbKoF9vcLssZqpyWT4cAmuuxQw4ftHYe7Krv95fG__Vx47ZLH0PDbG-goEKrhtYW1sR7Y-Q-f6b_sPr0hVhV8yGztZw9v-xaPQEDo1CLE1lRB4Srce0hu4rVd7eX4tkrgjk8UijZir_LeFT-qLW-SfIvxLRFmMSgv4V22uV2c2p47JdTNm9027kcZaGcVHE6SjMIn67AA2SqI5vKWhzaxsfi2c8aPQ5RkGf1vXd3shpdkYfdr1HpTBqQyE9BRYuAJKJcFvkyP7tCBtSp59V5sWG5ycdGJPcH4Clqj80T9jCTSuG5kVWXUBvxUD6448yCbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ روبرتو مانچینی برای‌عقدقرارداد چهار ساله با تیم ملی ایتالیا با فدراسیون فوتبال این کشور به‌توافق نهایی رسید و انتظار میره به زودی پوستر رونمایی از او نیز منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25476" target="_blank">📅 22:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25475">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=qgo9TMsl6IgB0LGjisvMPbylHSlpUtjypMYqG6rlEaMlSt6MYcpNGoOLlxgsF5fD6AAM3M285HnNQOZs8gewKk_Zjphf8jIu3GuwOF1AuBpaZzMChZXEzTuO8SP_7H04jzI2v4j8xNgCfa_y_LKt7ExDbwPLD5_Oxtfp5cug_m6q9Lg0m4s1ldwWD4D4brNiACoOsu8b3SF458r0lXyk4gt9QG8O19FJccmqpNESFSn0OAB0567T7Uj0hYPb7yQ8nKy-WiFZFoamK9VHJo-V5euTKiv5QOoNLZjw4uj1lF4JvbJeOxAZCxUkMfHesBFIVYX8_xNQ25wNYbpmFXomng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=qgo9TMsl6IgB0LGjisvMPbylHSlpUtjypMYqG6rlEaMlSt6MYcpNGoOLlxgsF5fD6AAM3M285HnNQOZs8gewKk_Zjphf8jIu3GuwOF1AuBpaZzMChZXEzTuO8SP_7H04jzI2v4j8xNgCfa_y_LKt7ExDbwPLD5_Oxtfp5cug_m6q9Lg0m4s1ldwWD4D4brNiACoOsu8b3SF458r0lXyk4gt9QG8O19FJccmqpNESFSn0OAB0567T7Uj0hYPb7yQ8nKy-WiFZFoamK9VHJo-V5euTKiv5QOoNLZjw4uj1lF4JvbJeOxAZCxUkMfHesBFIVYX8_xNQ25wNYbpmFXomng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
روزی‌فهمیدم مسی هیچوقت‌تسلیم نمیشه که بعد دعوت به این برنامه‌ازمجریای حشریش جون سالم به در برد. لعنتی‌ها ببینید چه گیری بهش داده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25475" target="_blank">📅 22:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25474">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLAUOHA7gS_DvvcltU3S5NE3DbqTm8bF-0l_qhuJlbhsinc3Ht3ar6IIP4sh7YJX-qtSmpW-mBHSQ-0mRC3wkWlDxZ9sX7c_Zx5LS-Wiptmrm4ZfNRJvg2kbm1u3cguKLOO5SZxvbT9HNIHTHpPteSSEtjSs_TG-0n6y9Z5dEXX7IJ0LEYU8aCij3dI5HK93UZV0jadPGZwcLZQIE1kUjtm65OjdXnHY5_JsC7OEisCPSvTH1WOFnwPZ97NmvsjNFSQp1FR0Igaeihu2bX78hitzuTKHxDAnOk_K8Tqd7TqowOfLrL-8sEh_XPl2tI-VUofmHi6pB97j3ubvH2xuHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی پرشیانا توسط پیمان حدادی مدیر عامل سرخ‌ها درباره وضعیت علیپور و محمدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25474" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25473">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=gkU9B7Xmu6Ur8J0eyYH2rpIcc5bp88OQcUkTODpSgiURpHQoOqejPG70F8zhhsyGjHFcQWMaKmKyDjBtXtE2R84_KpXs_CWbprhTmDTmdiuapdYuHF1KrZnfWy5Z6BnTCo14OkR7PFnXTVKhBtdILvA2_GDViBAuIDg6haT5M0oBu-1UN-m5huWvZHY1mTMfmdrucQErc4vNyfM-gV8n8rkUeirAsptP3kaHVXXZ4Y_2VqsqIcH0qckOYUj1IIMxOkGdtucpvuhr3jStR07kIht_aCS_ZJBG6GZL9H9933NJV1KtLw1mT-s7f7_HkHy7P5jlmCC_H1zPaOOZJpdHVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=gkU9B7Xmu6Ur8J0eyYH2rpIcc5bp88OQcUkTODpSgiURpHQoOqejPG70F8zhhsyGjHFcQWMaKmKyDjBtXtE2R84_KpXs_CWbprhTmDTmdiuapdYuHF1KrZnfWy5Z6BnTCo14OkR7PFnXTVKhBtdILvA2_GDViBAuIDg6haT5M0oBu-1UN-m5huWvZHY1mTMfmdrucQErc4vNyfM-gV8n8rkUeirAsptP3kaHVXXZ4Y_2VqsqIcH0qckOYUj1IIMxOkGdtucpvuhr3jStR07kIht_aCS_ZJBG6GZL9H9933NJV1KtLw1mT-s7f7_HkHy7P5jlmCC_H1zPaOOZJpdHVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
صحبت‌های‌ندیم‌امیری‌بازیکن‌افغانستانی تیم ملی آلمان در رقابت های جام جهانی 2026؛ این بازیکن از دو تیم آرسنال و چلسی آفر دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25473" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25472">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mS0VpDA00eZxsZnruclkh-fldm2f-Ghgu7ukiwAWm32u1xyA7UU3Pqg_o0JSxSNM1LLeAfuzhJqKHUtu-a9Ft91haCf8PStwmFdYOjUppNCsW7Fc3m1KjeW5mOUzaidtQRkl9p8nk2QaInx2dupvqhKjfxPirBmcDgq9QfyqoxrVjO6o321PnH27vbEQPq7JeQ74LrlYmprEq8HDyoi8gAQccBul9pY64hB0fuhCt4ZabdBUjT2cSHsgcZ5TtmmY4xFZS3nYjv84kHklnr7dVwqNk2bwm1RUxMAjf6TTt5LHszELpMMh-Pvcy-xG6DO48qeBv1zi27yhDSQLDkcyRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGbxRau9pYhFovZGwvIhzqgrDnQRbs0BDmTem7Id28xs5xG1l6PqZmYPnZBXJYPZUvxG7T8D60_LY16fF8FdY4T5cOKfy21t_i--bjUmfNfpHH_rowJfGTN7VowCI401tzF_ElV4UpXcKTaCl0p00HS2ePy5eu8Msz5ETTqvG7rpBfisrQfywnvRr5dDy10RcbH4EZFAL72ZmPfirrMlrkqlLQafduUicxRIlml3fcoG0SYSYO1lJoQthEJtJ7_sVFDkJ4g2QoVZXrnWDwN6xTrkiiutlv74ZzfH_rV2raKVRYLCk5Vo_sZy42oeDO2hBI-k79gTQ21tzcebSscs7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25471" target="_blank">📅 22:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25470">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSyBtACWeBZM5TvlAIjMvLTDMw_TKRBHcVrRoydyLPCGNpioceBVQUloPG576garHSkpiR1LVqaswwzuPhtI50nrnlktpXGXrD_xx6O2u8SSatILw0rs1KpmpAFm6qnJuvIlPWm8TP0PJQs52g2wOSFrYyv5J8UuLxEHsPB_XE-PH6I6StEngIsVc8pK2kKJL32mLPcvmb06qFjubWXYnIGCZfh1iBUzYiqUB2KLuS3sv3ULFrii3Z-wx0kSn_39VaNc990yyHZa74ubjc_B5r_869Sd1UAuOMw4F67Oxelh5IJnp202B1LVdV5-LQ9KOdBgt-27HihVY9o5GnrKfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جالبه بدونید بازی‌هایی که تو این جام به ضربات پنالتی کشیده شدن در نهایت تیمی که پنالتی دوم رو زده برده که این‌فکت هم درنوع خودش جالبه واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25470" target="_blank">📅 21:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25468">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=GoRW60I_uU6NePLi7uQUndURFp-wjCuJY6q-i9FDn6V5O2BA9OcUuERzsOh2dPu3EUDhA_Q2Gq0WVaV0C5shDT5wUnJo-2c2JE-aHTUCwkZkw1oE7bLfsCz67BorYgoh982EN3d-MWInibwbdBkVhYrZN8VEd_0iseA8hk-JRwY0PZAVya2JhNvUMBTbpNJt3p-l75wHDmwivS74C_IVHs3OeVG1_HWW0zhUo4ds24QkCKy0KQ4v6F8fGmfxVELCKuMtkx6vSVonMM2NToa5qk_gz1XMwHREFXGi4hRbAee8t64HgtkaQXza8CHVpvS48CdCYTiu4PVOHUBnL7HgiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=GoRW60I_uU6NePLi7uQUndURFp-wjCuJY6q-i9FDn6V5O2BA9OcUuERzsOh2dPu3EUDhA_Q2Gq0WVaV0C5shDT5wUnJo-2c2JE-aHTUCwkZkw1oE7bLfsCz67BorYgoh982EN3d-MWInibwbdBkVhYrZN8VEd_0iseA8hk-JRwY0PZAVya2JhNvUMBTbpNJt3p-l75wHDmwivS74C_IVHs3OeVG1_HWW0zhUo4ds24QkCKy0KQ4v6F8fGmfxVELCKuMtkx6vSVonMM2NToa5qk_gz1XMwHREFXGi4hRbAee8t64HgtkaQXza8CHVpvS48CdCYTiu4PVOHUBnL7HgiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌پرسپولیس که دوهفته پیش با ایجنت علی علیپور به توافق شفاهی رسیده بود حالا 72 ساعت به‌این‌مهاجم 30 ساله فرصت‌داده که برای تمدید قراردادش به ساختمان‌باشگاه برود در غیر این صورت قید او رو خواهند زد. درباره میلاد محمدی او تمام توافقات لازم رو…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25468" target="_blank">📅 21:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25467">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MY3CN5iifdI1mgmn82jWtH_zMgKOBiqgHdzsFgZaEp3cZ_gr1px3_tBUSBfXhg4Yr9Q-BnO6RwOf72rRIeitT0NHTDTv6H0ymdmQeRmdWnC3dO_oxhm1_Y42QsU96NxmS8IYkOiIiYS8yVKOyG3uP2tpyRty9tnHR1tb6M1-QvBZQB7UhIW9W4fGyZFlOvAyxzBKwdgciG5sb3dXWbG2ouRysKMW5EChrHd4T1YWc8ZCzgwGmgNYD8upqswOC4g8KRqJDz02fyL0jQWagyMkE7b9KTKYTVke-Pge6QX3qr0LEw2PL00rCpkgKJWRHP3uXqwSmlI1lifxDsugbtGDBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25466" target="_blank">📅 21:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25465">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLmfrYsIh-oCDVLJB6D7vhAf4xoX0u4QqxeSBepqmWL065BtcIUy0T-s_kIoUebrZbclHcEal1V1kx9dqZ8aj-zccRC7Q1yUj_OQ9ioxxYPO4SKTwJX7JXp5MFP7iF-oefICAfZGt6xXrey4SFP0-fWN35vSOZetgc8jBFDqOuNJPZq63D3DTJGSrpvG-1uUG1qhtSqOb737dmJ0Z0crBdU7WgOet6uFlN2N8WYUQyU3rOmsCBh7Eyp91P8X_9GNuk_kI77Q9qqYqxzxBIH9z3NQuhoTm8s5NklDhsjEj6OVDjIVtI-h6SvtxaFI8JLv9b-Zfad0X4Q1Jl0CEt3uJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل سرمربی تیم ملی انگلیس روش جالبی‌برای‌انگیزه‌دادن‌به‌بازیکنان تیمش در جام جهانی کشف‌کرده که چون یخورده 18+ عه تو کانال دوم‌راجبش‌گفتیم. حالا فهمیدم بلینگهام چرا یهو اوج گرفت. بعدجالبه بدونید 10 گل از 11 گل انگلیس در بازیای اخیر توسط هری…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/25465" target="_blank">📅 20:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25464">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkRdjuWwi7itQwu6V9TxBItWOiECKXwCg6U2TbR2lmnGahNIzUcXyviQ6Rp4uLaZmhgo99xojq0UVycuySqFT_k5lqRXtccgqebKpl7e6pdaoNJvI5Bq4-wgf3fV0vIPrsFyI1Bqv6ucmREhDmPitN2-2GV-_FwL1770jd6tz56oN4toN154R8k3iPhcDiaZbjDQFxmZUu0xhB830THf6_MXWghWxAmUuNUBkTB8mYZw5TnkSACynwQktj42AhsNm0JI5JA1GMcfQSbZd1ZuGKm44HTlFoGJIyu4RAxZGj72njtD6wivpffaP7OlMTn_YrtPbVTmubBqEwVMjCCQSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعداز موافقت مهدی‌تارتار سرمربی جدبد تیم پرسپولیس؛کریم‌باقری بزودی‌به کادرفنی سرخپوشان اضافه خواهد شد و قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25464" target="_blank">📅 20:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25463">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tL21yHvx8FohOT33ziDd3k8daNm8_BA9aEfrGUS5ZQLBXLxMJbvR5gP6KYDsErLbncV0QdjEltrscaeOGGsNgebHENAGPQsUxSRzZV95ZlqYfcrQJo62RySzIrIkk9Eyq_Qe9GO2sc8G3XIBGq1Rgdewc15mKuMHRf_Z6jXyg5_JYUa6jaBOe7vJaujw356Z4Wzi1IRCfDeA2-OmyYzYLybrqnsCa6WJ5HBAdZlvRdQnk29ZkyDfN9kf5cENtyPytTyEpzsh0hApVvc_5HM5qNx6DH2uROAL77sbEbPw0pCdbQtci4kRcgMhpl8NJg5nmxlX_A0_9eDmRKZ5NeXhNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌اخباردریافتی‌رسانه پرشیانا؛ امیر هوشنگ سعادتی ایجنت معروف فوتبال ایران با مالک باشگاه تراکتور آشتی کرد و در اولین اقدام قصد داره هادی حبیبی نژاد که روز گذشته در باشگاه سپاهان جلسه داشت و توافق نیز حاصل شد رو به تبریز ببره. اگه این اتفاق رسما بیفته یکی…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25463" target="_blank">📅 20:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25462">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oj_g27S8GbZJresGGphTRG9Nadzk_GZQa07e7ZbOoe3Vz70U96jIDzjgncx4mvHzd2VTPH85-pdBQ_IY-8jXiEAWxIK64RbFiccEXmAEojNXgOVwHnYsfrrIQq4kSfv-SBNoO7C4LjuOUqPw1a8X5c6xTogUkkvEpoSw8i1qofByhWiZ-XgkSLxIrTRZcsKAg56AzNGRTb50qLoSJmu_VCEpbwe2ZDG5VFSZnzhT9DVQEGOS56R6VXxXTYdFIfSymm8_SFuEZeDMufh6unNL9yO7nn7DQ5x5L4cI075lytfn6MS8BNKF_x3yGlRC0kQG_3_t98dM0tFPCZp8MPgi8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25462" target="_blank">📅 20:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25460">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMGSV_9NzkubvVAhA1Dnayx5N4JZ5TRE5M_xIEW5t8HtSBpECWte16X4y6j8RL5Efncr9JjkMCzd-rSaZHBOFxIv136kEWVscAG0mmqcA8KmAaUxY27-tvHK2Xnfu3-f-DNUZP_iCZOvXpTJEuUGN05-Pvdvhc_5NO94ZGhQS_pj8mWdF34H2SvW9eD2fpPhPRCoue1_j0ZU20PO0i5e0XoRyjINcmQiOd9WFVLNujW2Ze1DXpuDvKitip4aplmQtCRZSPnpmFHOUu5z1qCojuIj38G77C6yhGHcZ7VHHRLRjlPWTGZfCVgeQfDVRVB6NOqF-y4db1dd7FzGvL2etQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25460" target="_blank">📅 19:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25459">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXJgQFqSr-v0Z5_I2Hmd1MeRP5Lz-fRuS5vf--pcEQG_EicuNW-oRy79uquLo2x3GfeYEWrrJzgx9g1j0uvMrDsqESOthS2hCCUGFCy2AtnzGX3ZC7RiExY9hz4t3OsYS7ApuJ9pfqFVcZ_KaRt7ETmxzQv6abf6dBw_C6IBjBBJgRij0X2HqXL13ilNYpISBVZwE8mBbho2ohU2y8lBs6eueV0bL8iy4s2rwK-s12oRNiDXSuLSRyukqgyTa7Q7jYdtYuhD5X9Y0IYd6mSh-Gf3RXFRbmWFn6MZuorpMMrUabe5ygvmpqiOYmwVYNj1X-f2RefHguJmj_bOHP2Eow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تقویم
؛ 12سال‌پیش‌درچنین‌روزی؛
بارسلونا با پرداخت تنها75میلیون‌یورو لوییز سوارز فوق ستاره خط حمله لیورپول رو بخدمت گرفت. آمار سوارز در بارسا: 283 بازی، 195 گل‌زده،113پاس‌گل، 13 جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25459" target="_blank">📅 19:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25457">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=dGQChByR7RbkLKEiUt5NHZR8YcCzjPOnrP-oE9-NGh5rxMiJAMwnEDZU7oBsUU1PUKKdMtCL7iUk666ZG8ggEh_AGMC_3zAAZsUHcSTmDeLGlytQFmmmKSmHibVoMLRongKYbfusb3cWd6-3zjHbe17GqrnJgrFGmuHGacolT5WR4okSKAlEuxFLuE_hW72IB_RuQoj0f5fLCNLXtU2FTZ28vPaqgYneE4S7NUz0P9p6-Mr4Axy2EjAQrfPgYIjSVvWzEKuht2TKxMAAJUYmp58UgZ9tg6LySQKEHIn0HRb0Tl6b2oHfCxXKwiAaSSYO3EY9SaA0EAAcyezj5Ts4xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=dGQChByR7RbkLKEiUt5NHZR8YcCzjPOnrP-oE9-NGh5rxMiJAMwnEDZU7oBsUU1PUKKdMtCL7iUk666ZG8ggEh_AGMC_3zAAZsUHcSTmDeLGlytQFmmmKSmHibVoMLRongKYbfusb3cWd6-3zjHbe17GqrnJgrFGmuHGacolT5WR4okSKAlEuxFLuE_hW72IB_RuQoj0f5fLCNLXtU2FTZ28vPaqgYneE4S7NUz0P9p6-Mr4Axy2EjAQrfPgYIjSVvWzEKuht2TKxMAAJUYmp58UgZ9tg6LySQKEHIn0HRb0Tl6b2oHfCxXKwiAaSSYO3EY9SaA0EAAcyezj5Ts4xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لقب جالب لوکاکو از زبان فیروز کریمی؛
جالبه بدونید که برای ایشان به‌خاطر شرکت تو برنامه جام جهانی شبکه جم‌ تی‌وی پرونده قضایی تشکیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25457" target="_blank">📅 19:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25456">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pi0ATtEpQkrOTvPGQxriXxJqzNTcgUa45EyvAUc81mH0Q9R2y1JKlwOb90CwWEReI5QCWRg1IA7QeLnxdEJR7ZSUoBxfE29T6S-TPUR_F-pY_RJVKMe4KGlpKSvm1JTbSpmd6xAqq_G4Zz_IJtI3tiVrMGNRmziXoHN1PxuDRuPf9zo-G3yM8eHQivinSKcJqdg8sYYCstbBgof1CYGDPFPE3PH5pucxIS-P7doNEb4bGBUKuhRBeXy2-Pvf-J_9g0D68gbpma3u7gdCLQrp26y88TB-ustMsU5ShYYdkYesYs0s_mSenX-XD9EDQ4QKASBH6BwiW9_Up2AAikvamA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام AFC مراسم قرعه‌کشی لیگ نخبگان و سطح 2 آسیا سه‌شنبه27مرداد درکوالالامپور برگزار میشه: استقلال و تراکتور درلیگ‌نخبگان و چادرملو درسطح دو آسیا به عنوان نماینده های ایران حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25456" target="_blank">📅 19:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25455">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJ5Nx2ZG07mfPDJcMVk59vN4sKyg0C1b88Z2PQ8mkQuMLIt2YC0MYNvH0pdqdLG69h8HWFhn2Vgnh1GrHmlwoxBavo1B17ycNMfZDaYeKtESMvJkeYC5ShHLZhOxX0H4L4GOexAdICfRf5-ZwSCQWVspCTHA1wTbU3i2fA7JgS993iG-WKukEXd2Q1n9gFINL5GyBYBuC6lWnk8-Je2jaLmJTy4euf3jhOQ0QbieTMcx2uBoRK4YoTHgrQjTbDomXlxN7Z2HNgSHKTcDmc611V6bG-yjmru4cBbhhB1Y0dolSwMpmmgDatA5wCtjaqA232VAFQV5GR0RRYhhcRwTkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
کریم بنزما اسطوره رئال مادرید: به کیلیان امباپه گفتم الان‌بهترین‌زمان‌ممکن برای انتقام گرفتن ازاسپانیاست. به‌هیچ‌عنوان نباید این فرصت طلایی رو از دست داد. اسپانیا برتر  از فرانسه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/25455" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25454">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‼️
خاطره فیروز کریمی از حموم عمومی در برنامه دیشب ویژه برنامه جام جهانی شبکه جم اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/25454" target="_blank">📅 18:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25453">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akmjK3aU2jwP8SBgXeuNedBQv8VmD3IaHphPi3_i0V8K8-nhbvjMqLW-TK-60evt21CSOmENJTZW-_NmAIMjop64zuMPB1SXRzi-yTkdRVPXLhAeH_BAPe6vOczKzRYAp2mFEDC1XDNEPvE2Bvhkx-faychsVyxMyTQ_SpiFLuhf24gl-Z9ktzlIt1QXxo943k3CrIxbHdEO50XNNrOdnUSaHvG5ADBTS3XpVk4_D0DbiQqanDvn9JtcFkEZFqL6Uz3m9PNiKK35d5ZrXsg3wF37a023TuxFbv32w6Qv7OOgkJU45h54W4BnEZmyJ61WzOEqbqkdUjnxENHGS7mAJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/25453" target="_blank">📅 17:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25452">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6qHVo71OAObzbyWHr84WECKKhb-OF136x5cIcImGfA7-Rr84ggR0Sc5rkrC2mVAYOAHzKii9B56EfGehec9EBgtKJD9_jYM0CCldnW1spDDf2FQRxv96ISqe9LhzLLG_8x5Pb4Em32YRkJedpWw0FSjv7DViVAQGIcvSWacoN1ik5ceN5nJwiQOnRG-aAic2BRIvced1jDz1-TqxBkT3zudUA-z_0nGH2IHbTdvLnlZZOt1t3sGefIk1QSU9fGHMhnDUvv1xkFeJCWwONEciQoP17Em_WVTgyoHMnQ74CQK_Zz0DPgyCtp8DUQHPt1xfjMBl_vSo8lra11OeA1EWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25452" target="_blank">📅 17:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25451">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnhBG1_6hf6LrhzKiJiQxI7clH2VUahT9NJu7M2b3N09xItAYuyyLa2AKi9AKMbkZpOX9_DXJz6oaQLI1ow4oiOmNt-8y2OG_Lhq-DZD3scgU947A6FxNDjRpAO3S4kJ3zVSTjlVUHPXpLivCDfOMQ1iPmuSuseoysr5J7IWjlvZq-ijraCPreu8DzX7kLHkI46wvrCxgIPfp1yk-osL3csPPvTRKcbiB2J1hUvMMKTgFoTjIHe4gmE3xxEps1xT0uElXoAcOBgbh035Q02M49mBH8RzBawVhyFVDr0towaKJDkL-9tDjj9EV6MYm74boXR9_lRuaJlgvwqvN67btQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علیرضا بیرانوند دروازه‌بان ملی پوش تراکتور: اگر در تیم پرسپولیس میماندم شک نداشتم یه روزی مدیریت با من هم مثل وحید امیری رفتار می‌کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/25451" target="_blank">📅 17:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25450">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEHIgxE4lvHMODpNtF_Qpn5gsQFP5SbnKUE1yPRsrBVBLv1I8_Diq7tHjoZMaMuuIjtXNFSrWbD_1Ho4WCl6MMWLlfNUUgcCHfbZR6D2pzzPUnhxGVX480StITj3pBaJyumtUMw5EpqasTK68_cVHFPKn370VeTwcZ5VnfI36UDItZI-88OJiAgCUSQBR67k8Yo60Ynh4pl4JeV0zqbyX_972wRCjHccbvXjjyV6q0vF2SMBFEqW2UjrxvLF7P-zqAMB3_3hBme5dINtjp_dmAQIdtIwl3dy8VWMzF5dGurnU-N8WWd-mcODRLO1fHdAx5zsk2UzFY4V0ttYP6f8fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/25450" target="_blank">📅 17:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25449">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zk6yt2YNZh9e3ano43E04R1oBMzQo56eM5Mm7AbO5Q1dvvGeoJkbS8SzVaRahKZr0oeXmt-fOZl0G-L2Jcg2xS6D4zoMGjAXpqiJQ6oNp8ZEsTNSzSJ9y13YIUX4zyll_pOH8lGQDJkb2bRl14RRaOLr5jVmVnK50mFFd_1Fyv9b6TSVCGu4S4PDYXMcDKsYgVXu5iopftb64UjD2LJb-x0ehnYITNtGRmJoPe8bglQlZK4T3y6Q-AhGuhYZpkFpC0tZDkycG4a3XBTPNhYQsAjTGdhUzm4l2UFt1lJE2tfv9yJt-P3z7JkG441BnCOQTl3Abr9CEmvMV0_bDVdz_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
خبر شوکه‌کننده دنیای فوتبال
؛ جیدن آدامز بازیکن ۲۵ ساله تیم‌ملی‌آفریقای‌جنوبی که همین چند هفته پیش در رقابت‌ های جام جهانی ۲۰۲۶ هم به میدان رفت، به علت افسردگی خودکشی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/25449" target="_blank">📅 16:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25448">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyVcpXACrrdmhRAaZep5zFJA7hXIbjRGFQylK-Dy4H39_MloliVTm34GVV8tr1499idra8Kbn79w8cb5-6GVf_U-OSFFF4tMBnhvxsLQ2ERoEPAiRhZiZPVoaq-vHW6xkDwLuc5bx9P4WtY0Y7HifJIbc-hByc1yT9uAxtX3Gl5wMoYabpl3A-0-_0gD9E0CRBQfosF3LlaEBOarLLS2iDQU4lZf4k57kUCWaGitSr5ntKGFjl1O4IbhrgIQBvIkYuxbYhGwCFUK2Ok3sdy7RZLugGvFGtLSb4oEm-6PrNmt1VEWwgoBHQr_hod4cpG4FAF7FvqhZeyqwN2mY4r0iQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOnXrKvLO2Hsz-lHIXxpDckRgj1uGGdNW2R7YMgm2weVoekpUOLuR_ut4MvPfrrVjMQvkCqcON9dhpln2anv7QM91F1JA51TvQ3ezZyueUQLJU4Wg7EbkZ9AlKhYVMWbFBYVdfKLIpH_uMrGYiPsH-NMAXQ4y1eKTyrdd7l0_0alWpwoYpQ464T92zv8iF9aT2ISLDM_eZQEf6bdrMyLgVwL8yhtIsQA9-iK_ZnknV4nqTu-e6CF_pMaqf5fVTxNYaj2EUZ7Jya0-2MGpmLGjJbA6nma1WKCB_YqKMLugkoUGUVBQP-GSEn3ffWMwmFn6xZ4zeOQpgU0hnHLylSshQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/25447" target="_blank">📅 16:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25446">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCyh-ZWY-_CvSSdGEqIeEOdYlSmNmDEmGO0dfQupD_dtxMFP-32VsDZ1kiftvo3eWsZQkHViAAK-cihxrgb3_2bOjFeyN-Ejd2StfusJ0K24MLwyroAlaI0XORYQ4zHv5HBOo-X0PuASkZvkFIsg55Uxa9yQnL1i5FwRxsQdjbrx9fbDGwMwdli9T6PeKq_sTDzpwHih9WD1E55lsOsNQbRZJdoMN1ioS5Ros3l2eMrsCgXdn9l32K5cbzktRMRnLky23mSV70mWLLyUdBkKmvDwN_OVLOQ6tQGkLOx2KuaLAIZZFg519VhjiMh8VeNMF-NFcKvxycvkOHEzDmq8Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛ باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/persiana_Soccer/25446" target="_blank">📅 16:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25445">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/to1TVTyMsFfr3HoFgeE48sLdcz3SkV7L7nhcuvHAA4Mlck5iyjVkf2R85uicsdJaTIpLXuVXW9J59CxksEN2BBXxD3_J9aZpeqC8ldNpvL3TbCML_6KDIWAHL6qIMcqiSuckrmC5rCNB4-QVCTOKJXjlXGe6l5yL1eX09sp_zrxBnkkbvAw3XR0bDypHZKeBo29Y-oy4acfx9hkspoh84DSmJ2fgMjDUzq3C6CAWm6cZD6EpwYh4XFMRIWWu892w_lySwI1PXLuBjdj-eXNQlNnCQkKIx9429bhv1u3-DnQcBf2Si-7qFd94isIOtw2vgDqI_ISxUj-zVJupZil_4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/persiana_Soccer/25445" target="_blank">📅 16:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25444">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lE06cigNGihNOiErRun6PpNN7BFsVgAejUhgiqO3S-VTNQKHrZAYs-17Y0FM3FuwiTF5iOPt5YnyXpGovPAMOhxAssxuDgxTou3E5JAt03sXurG-QOmkrtfzTZMSy-Ug9A44e9TIrRIeW-e_uvHnRTIfDxAwh_zCp6sKF05V-tPRmXOipyU9c07ixUDd0U_DxSu1qxMKhb-dQy6NUTvJLNY3st07WRM5qfIoofHZbGJ2xnlMNkA1c4s-tf_jhCqEIYhUCrj6hu5KBjo_w2IBckRAjQEXldft-puusrnvzUN3YQUyiM2x-7XMSUrnFg-TJ9tBQ4dQz4X_xyBfQ8N9hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/persiana_Soccer/25444" target="_blank">📅 16:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25443">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3YgrMUIb8tUT6urxidSJB6PqEy0KsjE4FXvOYIs4nOyOo5FCCneXF6wSerHZqHlM7IvrzEybMPk0QE9F68PhqXxD0POonFglWoLcVVUokgvxi_YC5Q5FZcBSVUwfLB27gohmYuD1f_4ixq-PKUHajEJt_zr5_8VliQNMroHpbHpZOyg8OYoKlgMmC1YESL76ZLRWPKvFa31Q5jIkZMCmGAJj90m37sy_3lg0yvlpL23w3yXhThOhZSSC6R3m6Hn_tPBszEyF_m4bsty_kucYcAT0w_PEhh19vnX41iE0HmY_qRk2g8fmMGRehROuzk2FhUSRFhCjnJNX1k0xD07EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/persiana_Soccer/25443" target="_blank">📅 16:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25442">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVI8daDCmmgkQVVY9M_GmScvW6yT-3k6ZIHxUo8DNuLFeCxhZoooK6-9MuAwQE7eHmJUTcqrDu6tY66rlbwqlCDeSyLsBcKi_gY_oDY3vxAMF1RGSrEG-7iz1WKh_XbzKVg-peoM3AAKb3-lhw9TPhpaIo2PB2ZkjggIfNymCNhrNQUK4gdcwkwouQuvcv8h2O_fMYlZ34biOT6-IPFYH7IDokHVlqElr9EWtKcXzuZWjypXCdK-4PvpVOE9wBq3h_WTpw0IBOtJZofYcH_uPDmA9e7EsWPMN7W1ynlNr3e_wyxBrKdcY_60fY8zIviOEYCycVQ9omPEPhwun1lTrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛
رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/persiana_Soccer/25442" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25441">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8ad7a6bb4.mp4?token=nIhLHATEdwI9YiGxBVruEmSHMagab4jmvLDrcfl6Vftw3IhFLBcHKTBZgl2zm7WHI5z5RW2WYemqCi1XsHM6fDMjw7xcwtwDkOlctvsoIvdzFSTNl8uLvxNYzQBxTFlrZjCYcD4Hsc0n9LMRZxUtTjRTHUDE5p-BoWdqjKd4-QV-OualpI69CA4rrW6dOWqU271aKuGqbQrxJ0c7mhgUTMwIrTy7PjdMBxGFo2w3tuJqVzoqc72JmTriQtTjlZj8KE5ot6V4PBWO4TFxFQwkutyMxiqP-CCIySiOkZqBzWC5RRNsmD0zDuT1rUp9LdFvNxp1l-p3JAO5Y048akgzBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8ad7a6bb4.mp4?token=nIhLHATEdwI9YiGxBVruEmSHMagab4jmvLDrcfl6Vftw3IhFLBcHKTBZgl2zm7WHI5z5RW2WYemqCi1XsHM6fDMjw7xcwtwDkOlctvsoIvdzFSTNl8uLvxNYzQBxTFlrZjCYcD4Hsc0n9LMRZxUtTjRTHUDE5p-BoWdqjKd4-QV-OualpI69CA4rrW6dOWqU271aKuGqbQrxJ0c7mhgUTMwIrTy7PjdMBxGFo2w3tuJqVzoqc72JmTriQtTjlZj8KE5ot6V4PBWO4TFxFQwkutyMxiqP-CCIySiOkZqBzWC5RRNsmD0zDuT1rUp9LdFvNxp1l-p3JAO5Y048akgzBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
خواسته‌تموم‌پسرای‌فوتبالی؛ روزی‌بخوان ازدواج کنند و بچه‌داربشن، بچشون‌حتماباید اینجوری باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/25441" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25440">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآپارات اسپرت | AparatSport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kR_Ycr2tOZTdNDOF2mfSZTaDxXj3fTtpaFzGLava0erh8uWGI_foRFhjTpShkX3PZOMFFT_hdYkHo4h8O8qCdkMH7Z_sVgvIJ6UGkHmZ4Dnd31Up9gf-T0l1J_oTGAY3wjJK6Ukp5xX8tQcU4pJfuvJEcqpklbAttLqmzXBml9KTIHzU4mmLTAej37Fy2NTExW7okiE6XNOLPVxBA3lQUQxaxPm9yDYqHfjR4ehz0zZHk435E2jaxKMgFjJ_-Lv3fu2fLaF8V4Udl2jugp7qVTOpvv_RHXT1ZWGYnV_0qPWkTDfhWPbWczfXglQFlIrN2vy_vaxqmpjxpZcJnFvDHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده و اختصاصی بازی نروژ و انگلیس با گزارش محمدرضا احمدی در آپارات اسپرت
📅
یکشنبه
👈
ساعت ۰۰:۳۰
🔗
لینک تماشای مسابقه
(بدون فیلترشکن وارد شو)
@aparatsport</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/25440" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
