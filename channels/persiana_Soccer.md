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
<img src="https://cdn4.telesco.pe/file/Y-xPyG9rqL-hC0ltMCK3SbjmOcov35wdwwLIGE56FNxTCMFRxit_kNmZQ9-u5Ht2NEIys3Sk1mSUf-vDwkJJjxky031IVgP-h2lI2kcgvdbuYRAmWrCa1JohOOlyhaRBRo6iZtoMkwCuKhzItLGA0qVho-mbSgbUNnfJrlw9_rCIx70YVBAl-JJGIrOIdvDEVdLi-COfKHMxYCaFsRAtCzKscN3RG5LL8p_0OgsCIkU5LUQOrMQ0JcX5ECnbu5bLzrjV7tuieXqg5vY84JkXGGpGcfKLWq5aGKYIsu6ZwftNiXjEmU9NpzjsKS2MBuq3nMJJHPpIRhKGeYqXmtSNrA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 178K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 18:12:19</div>
<hr>

<div class="tg-post" id="msg-22547">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdSsmIeSqMVM9-5L217aEULWxs3MgOPz8Swsvrf-VbydfJnHCx-oHA5vRyu82AqhWOG7T9Zi9ljLb9yrFYHFlSZQwqCrtRaBhKkqNTWZCi-v1t4XPGKbAyaf5KMCCoQvvtOjWzWNkzd_iJddqKgWhT-j1Uip47C1xqDRpFMFFdKNEIQBb-WPiShO3Ub4r5SnOwkAVUBwZIo2dpB4AuUr88Sf1yWsWtWwMkqZ5MIHK06hOoRL3n9SmgureJe7_wrW8oK-rEQqYaUq-a--_f3yfa2JVHgJvsqDw96m1UW3WXxwwjkSvDnGw8I2bfkJj9EYCRDxIDg4zKoNUoAIYZ2_3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛
مالکان باشگاه پرسپولیس از عملکرد مدیریت سرخپوشان در فصل گذشته‌رضایت‌کافی ندارند و ممکن است بزودی اولویت‌نهایی و آخرین فرصت‌رو به حدادی مدیرعامل فعلی‌این‌تیم بدهند و درصورت‌ادامه عملکرد ضعیفش او رو از مدیرعاملی باشگاه پرسپولیس کنار بگذارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/persiana_Soccer/22547" target="_blank">📅 18:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22546">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa9a136cd.mp4?token=df9ar1NOkmtz_Bxxpd5cleNS336Wy-xHlnDPREr_cNkTbFhcFtoltj078ZSBMBZOS1ckjP8eX6yfbi4ymRNf03DSF_zKs5tcy3719GwzLwODt3-Vlg_0P4dQbAjHxpv3brdPeITkD3VWbjjI5JuhKI4ybYd3os1kmrw4iw9vibpl82pA9MtrAwFJ5Lg-h3PF7oAnqF08Ii8DG4Ild-dvv78Lx9V_NjDvwA_xSEROv83d_5FN8fDfaOwLweNjLkAXCHHfI6Edvm0ONrbHlJAbzccjDYFtWPK8h2OZ50z4Gr_NMvp6w7umjrR4IQ8I-g-fboXe5iHPJ8PaUGZR95OtRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa9a136cd.mp4?token=df9ar1NOkmtz_Bxxpd5cleNS336Wy-xHlnDPREr_cNkTbFhcFtoltj078ZSBMBZOS1ckjP8eX6yfbi4ymRNf03DSF_zKs5tcy3719GwzLwODt3-Vlg_0P4dQbAjHxpv3brdPeITkD3VWbjjI5JuhKI4ybYd3os1kmrw4iw9vibpl82pA9MtrAwFJ5Lg-h3PF7oAnqF08Ii8DG4Ild-dvv78Lx9V_NjDvwA_xSEROv83d_5FN8fDfaOwLweNjLkAXCHHfI6Edvm0ONrbHlJAbzccjDYFtWPK8h2OZ50z4Gr_NMvp6w7umjrR4IQ8I-g-fboXe5iHPJ8PaUGZR95OtRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
آماده‌ترین و بهترین‌خط هافبک حال حاضر در جام جهانی؛ بنظرتون پرتغال میتونی امسال قهرمان بشه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/persiana_Soccer/22546" target="_blank">📅 17:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22545">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lt8RxDaWbZM85ruxIzXeO-0n2CNT4EdFJdTwLsL2T4FWxVKGYikixGoQiXOVLKuLeUVenhTVmcOoayEVw5J_59Qqd-useBIti6t1Kk8VRkpPmo1qXoMpFuVH9qXfQ8bA3Ika9btqG7bDrtWrw4HueLix7mTCuvrYdjxNsT019POzcTQRiXM6uy3vCakhis97656xFjdtu9yRwPSEWBv5Q0J8BJLfWUe6LViL8izYWOhgVmr4VCuex8FFpzfLchcPyG0aGIxiXhNH1P2sqCbv4-71iAkrjQ4Ww-qpb8hS6R9xX59jmmSwiWtXC-XG26ZOdMKKpKt5iQ22lNgGZyqeEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیویی جالب از جمع‌آوری سریع و پشم‌ ریزون صحنه کنسرت فینال دیشب در کمتر از دو دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/persiana_Soccer/22545" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22544">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYSs65hm-hwRxImADxJMdjfddOnsAn70FK9YNDyHJrJTBpzczsxGgVrOgGsoKWFRfp3snWRXtvr1E-hBR4zthtzNLoKAwlfJ5aMbVz2FQnk5dF_XVbHjqfjkg3FZr7IriAvKBcwTUtNPKV7MixiG_J9sJhLCKLD3pyHButsevD9723UpXrYb9-zMhoR2AasGCjHo-GgzHlp4nsMaaMmrSL83mlv1PmVe0DZ_CFNPTNfEvyonH5N9Y8zDd80ZY4LNdTT4KEevpwbBQlUn4FW1Wfg9Iew9iWRMyWCXxV1y8lv6C58ULj2SKkU_-ijD1PF6PS2Bzfp0KgviOVJa2CaxcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|بارسا آمادس که ۱۳ میلیون یورو بابت فعال کردن بند فسخ قرار داد رشفورد به منچستریونایتد پرداخت‌کنه اما شیاطین سرخ مبلغ ۲۲ میلیون یورو برای فروش رشفورد میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/persiana_Soccer/22544" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22543">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfLYbIhvXJce8vMT7Acs4jT83uiDCN0CzCc94O2gksd2usKL_VEeL62Df0jjp0ROYvO9hp66uC2Y_kJwd1Zs5XTBdJSlEHZNxRn82XKGhIdt5AC7QgNNReT2mr2t66neD90gZNEnawn6DQgAdodq77AHvpxSkIvJ4PShi0SPfDAD5_UXhL-6H_HgctDlNWFVXNxIyLeRfTQSOTXWqhV0CCSmsGtZG3XswDm0salxvvQ009R_vLmeGazfgqIrnQ6gxYz_64c8FWN_p9Xfl-mBwRh6BYwR22Y41FTKbziEuyUqIZlT5pjSK3IFWgSNhn6t96vvLX8DNj2_CQd5mYtj-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💩
⚠️
دیگه
#فریب
بونوس‌های الکی سایت های سودجو رو نخورید
❌
💲
بیا توی سایت مورد تایید ما یعنی
#وینرو
و با عضویت 500 هزار تومان‌اعتباربی‌قیدو شرط بگیر
🤩
با عضویت
🤩
🤩
🤩
هزار تومان اعتبار رایگان بگیر!
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g10
📱
@winro_io</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/persiana_Soccer/22543" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22542">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gy6yb2X9ce5yWzmgMFYM0QWUJayv_LqYMBGJpdU_pO6o3TBXvikdb9uZlxczGuXY74bNAkk9VUVBT38MW6eDfnMuFdllPxgFEzUIvIfZe0sQWiemrAgiz-SV_v_Q4OY14Ak1th2H3CyXKlN22l9_MGMmpi5CToOQr7mYR5hltxIHQGM-of1ePkAPabcFjH7JduNjEV0uu77zpISuXM37J8jKhElwNM8aKA_yaXHHts98eO-mQt7mGOfF2iAA0-vG2jXHG-p26R-LnIW2sr7-p5iEEdkHQrLembmxORu13QUtM95iHlUuhs7ViJb5awsqgCZIvXwuWn3FsI95RMWrGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22542" target="_blank">📅 17:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22541">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11672147cd.mp4?token=LTBKQXe5dE7hz57lowOU-s4Qq-E6QrvZsYA9dcPOWN-OZgyIangu14OHo-Gj_D6DOlJuTbCyiRaUptfSVn6dhW2nqAYnMiqQUwN0x_WeqIk7BtlwxUX4GJwyktJMXhXX-j9KHAg56-5tcoszaOG9RK2pTlegawZ5o2H_BTP3HTS3kQu5RVRGXlmN3ZbfMrMCtTUl_UOyLyiDvXz3h91jH_hLfeWx9G_xB-kLvbH7Ef8eM64W4D-cttnod1xgvS2MXMl6HpvQEqNmCLMhivttQCCMrwUhJSKvfXAuPA4dhVpYCqkzZAYjg8D0cGvrxCfOMZ-_K59tvQOFLS5DXBz9XazcIfe1qQRWTdGfPTA15FMyHZox3NKLDh2rlZd5GdaueZ-RwwvzODQJrQVgpm75si3A1hPVk-ZJ5bQY03hQb8ZCkg6mqlp-rNwFMkHiejXuAUe6AvAyZp1JCtXbhjB5pqRzxGzbtvzB7NznyKeSwB0Rs63NwOxCg5yZuk6pK11yz_xUoFfteY8kQYsIB8pGawynPNUiKoEEPRUFJKpLMvpDTbpP6fO5Y0BJpeSDrak3bOTiFimDlRU7-KnFUndTNf2ubGonlzl3V7_5eloIqdCFrdtgUfMsgHTnnrjmnb7LY0wSlz-BJWlp6ZxD9Z8EAF3KPl-9nMWPFgJjq2AXX_Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11672147cd.mp4?token=LTBKQXe5dE7hz57lowOU-s4Qq-E6QrvZsYA9dcPOWN-OZgyIangu14OHo-Gj_D6DOlJuTbCyiRaUptfSVn6dhW2nqAYnMiqQUwN0x_WeqIk7BtlwxUX4GJwyktJMXhXX-j9KHAg56-5tcoszaOG9RK2pTlegawZ5o2H_BTP3HTS3kQu5RVRGXlmN3ZbfMrMCtTUl_UOyLyiDvXz3h91jH_hLfeWx9G_xB-kLvbH7Ef8eM64W4D-cttnod1xgvS2MXMl6HpvQEqNmCLMhivttQCCMrwUhJSKvfXAuPA4dhVpYCqkzZAYjg8D0cGvrxCfOMZ-_K59tvQOFLS5DXBz9XazcIfe1qQRWTdGfPTA15FMyHZox3NKLDh2rlZd5GdaueZ-RwwvzODQJrQVgpm75si3A1hPVk-ZJ5bQY03hQb8ZCkg6mqlp-rNwFMkHiejXuAUe6AvAyZp1JCtXbhjB5pqRzxGzbtvzB7NznyKeSwB0Rs63NwOxCg5yZuk6pK11yz_xUoFfteY8kQYsIB8pGawynPNUiKoEEPRUFJKpLMvpDTbpP6fO5Y0BJpeSDrak3bOTiFimDlRU7-KnFUndTNf2ubGonlzl3V7_5eloIqdCFrdtgUfMsgHTnnrjmnb7LY0wSlz-BJWlp6ZxD9Z8EAF3KPl-9nMWPFgJjq2AXX_Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی جالب از جمع‌آوری سریع و پشم‌ ریزون صحنه کنسرت فینال دیشب در کمتر از دو دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22541" target="_blank">📅 17:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22540">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0b950725.mp4?token=hRX8qmB-R8bvBnocsjvW2usOhVdS0tCIYK7O5u-5rDvwKEEM3CmGoiqnuqhvucILO1ZDwWPFLWtYc710-NPbhUGHXw2LCSWcnagxf-zamRscfj9mfLxZg7R6tBvBHGlsTy4xtmGfcaHZKjyoZYh8ouI0DZF_pa340bprW26rOQmnknNip5ZigWuZ96Bwe2tLxk8HvubJTj5nqP_fuMdN9u-PXe943aeC3FcrJSMB5_VdNn-oXyCmUzBHYxfoGACcEVfcIjp6DI8fHsyhkMmCGtd-NuxmIrEuLu49Pzu0YWaQsUNx0k3z7cp7mI9NUjwIEiDXPm1AUjiqBFjSeexAqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0b950725.mp4?token=hRX8qmB-R8bvBnocsjvW2usOhVdS0tCIYK7O5u-5rDvwKEEM3CmGoiqnuqhvucILO1ZDwWPFLWtYc710-NPbhUGHXw2LCSWcnagxf-zamRscfj9mfLxZg7R6tBvBHGlsTy4xtmGfcaHZKjyoZYh8ouI0DZF_pa340bprW26rOQmnknNip5ZigWuZ96Bwe2tLxk8HvubJTj5nqP_fuMdN9u-PXe943aeC3FcrJSMB5_VdNn-oXyCmUzBHYxfoGACcEVfcIjp6DI8fHsyhkMmCGtd-NuxmIrEuLu49Pzu0YWaQsUNx0k3z7cp7mI9NUjwIEiDXPm1AUjiqBFjSeexAqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
پاریسن‌ژرمن بعدِ قهرمانی در لیگ قهرمانان اروپا فصل ۲۰۲۵/۲۰۲۶ توانست‌درآمدی‌نزدیک‌به ۱۵۰ میلیون یورو از محل جوایز نقدی این رقابت‌ها کسب کند.
🔵
نکته‌قابل توجه اینه طی دو فصل اخیر، مجموع درآمد این باشگاه از UCL به حدود ۳۰۰ میلیون یورو رسیده؛ رقمی که بدون در نظر گرفتن درآمدهای روز مسابقه و فروش بلیت محاسبه شده و صرفاً مربوط به جوایز و سهم‌های مالی یوفا است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/persiana_Soccer/22540" target="_blank">📅 16:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22539">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4b71efa6.mp4?token=LECsO_Grg1fi7fpwJPuoTCiynjTCUDVYPm5Trx_zkrtOG9RwxjiqPwI0QOGOAvaBxDabHlw0fsdNzZmtzdbXD_emiW8HMKDNyAf-18wyBdo5a1nOzc86BO7Ew8hVLYHFS6_BZIZHLTckn6oRamK5A0mKF4Z3Zg9M-j0boxngm5IevpZ512D3vTrsE78XWJpHCUpXag79MAE1IsiB0CEjC3xJ16U6wu8lt-jVsnVrCLyy_NKVvAnqzUVUiPgyMZBPHSfltjshlMj_PQ3vIJZ0n7gmsReS-XkstfgrgfBsKkiuaD3HgRCJ43jjcTZgdfQVvzfLGLr706Ief3SIWBngaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4b71efa6.mp4?token=LECsO_Grg1fi7fpwJPuoTCiynjTCUDVYPm5Trx_zkrtOG9RwxjiqPwI0QOGOAvaBxDabHlw0fsdNzZmtzdbXD_emiW8HMKDNyAf-18wyBdo5a1nOzc86BO7Ew8hVLYHFS6_BZIZHLTckn6oRamK5A0mKF4Z3Zg9M-j0boxngm5IevpZ512D3vTrsE78XWJpHCUpXag79MAE1IsiB0CEjC3xJ16U6wu8lt-jVsnVrCLyy_NKVvAnqzUVUiPgyMZBPHSfltjshlMj_PQ3vIJZ0n7gmsReS-XkstfgrgfBsKkiuaD3HgRCJ43jjcTZgdfQVvzfLGLr706Ief3SIWBngaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ایشون هم یه مدل اسپانیایی هستن که دیشب روقهرمانیPSGمبلغ 3 میلیون‌دلار شرط بسته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/22539" target="_blank">📅 16:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22538">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇮🇹
برترین گل‌های فصل سوبوسلای در لیورپول؛ دومینیک سوبوسلای مجاری از باشگاه میلان نیز آفر رسمی دریافت کرده و احتمال این انتقال بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/22538" target="_blank">📅 16:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22537">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOuOzLee1NBfy67A1oMawMQRh3iW8Dx7uuUU8LqkB_IA8QOHx9woJuhkKp6wz8-bROaYgPzt9pNEtLlRxSCD3tEzv5sFEJ_t66MMAHDEobMI_x9OspQNOLd29TIkkVzDhudH6GfYmuMx-zZAmDt-oskDlAkiH4_ctBk-zb7tF2K0NUpjDHm_8hu-CPOPsbwX45q-dKuq1_Jrm30RZqYhRlVeFXtjDt9oFwB4tRFYYH46xNOIN9XP1391RHbZrCMPf0inu5wyCQoi_7mRCxHesvIYKf_FAh1IkUDWh8y_UqZ1dO91MxwvcY91RVApK3aTS6ogCgN0se8nk-_XMVquKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
یه احتمال فوق‌العاده جذاب؛ اگه پرتغال و آرژانتین در گروه‌ های خود بعنوان صدرنشین صعود کنند و درمراحل حذف بالا بیان در یک چهارم نهایی بهم میخورند و یک جنگ تمام عیار بین یاران کریس رونالدو - لیونل مسی خواهیم‌دید. تقابلی تاریخی که شاید اخرین تقابل این دو…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/persiana_Soccer/22537" target="_blank">📅 15:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22536">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObWD0I5mcTanFCJ-jaYDX6gD5ig7mv9GKZFzpZa8IIBeDhPV9_VYG9zTLXTzXG4SqP9BCACrk_6ZOCFdkFqYW9pey4TULioW92Zt52_4IgnJAMGACLiZamNE_BeORgJARHmtC6VlJTAxqvAxSvWCz2gT_ORnaMn_GcK46YDaZhOMifIqSykJ_mW-sSgybFl9U6_yR1iBBfJ3HtWiZqKLhAVqbi_Ok9T3JpM9LuXY703DfMXCgalWH2NuXugy6N8oZVRUUqx5t6Jh2jY3k3yewj2FrbMof10ddqONIjMFufRyeohRN8hJzcSvKBrpFaM8hz4QyXTDKncWn2Whr6o2dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ علی تاجرنیا صحبت هایی با وکیل علیرضا بیرانوند انجام داده تا درصورتیکه پنجره آبی‌ها در تابستان باز شود بیرو پس‌از کش و قوس های فراوان آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/22536" target="_blank">📅 15:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22535">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYcdx_kxaEKeDpaH7q_Zcp1csFxWNq48Rqq1cZfOUSjeUyp_7blrD0GP387ORH5KUTRYicbvN4rnJEDX27MXxBLxdv2337b5x__U06vEYqpHAZeJdzpm_avycgkIDaj5gAqwP8MiBk7RmtHLOHwB0K30k1I6aB10qodnn-fNKEdpIJYZAgzMH__JxPeMr4NRnV085U7nJqQ-IgnMvFjZnPYuXZ3BTLF_YvdEVlUM5FvgqxrNst3HFxjI4drlsneNtClvFcmq5MX7ZSk44zxoA7n4dJ5OPmvRMDXx6GYpLOysuUOeCDIoIeHc2UAjFeotqxh_kIxlLS-Td_64JjdHoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اکیپ فرانسه: باشگاه رئال مادرید مذاکرات اولیه‌خود را بانماینده مایکل اولیسه وینگر راست فرانسوی بایرن مونیخ آغاز کرده. سران رئال میخوان اولیسه رو در این تابستون جذب کنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/persiana_Soccer/22535" target="_blank">📅 14:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22534">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDi2flK1XL1MM7KsI9U3xss0RLuqgv-eJU5ARfUCmQcKE6nfA-hpjjxXy0B17lZXBIedkUSVtvt2nQDX1m9WBhir9CFaizKfadcm9CrlVZE4FPCDirbowMEDs9vm3AzBRzdho8kLYMAwgdFUHbOsIza8ZrNxIDxoiw4tn-ou3Czir4g7zmIDRsIfQnmVrFkloGrekrbLrQSgov8Q-7-3w89A1GWnd_msBFnZTOyf7NmjCz0bbi9D6IfRGjPusjP-gAqHklrw33x904-F2Nl_9qxUL-_fszZsuJeuxkqHbR-ZHa2yNM1eGVGkYa5Y9StjF71e9Yx3iDctl1bixjTQtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/22534" target="_blank">📅 14:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22533">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇫🇷
عاشقانه‌های‌بازیکنان‌باشگاه پاری‌سن‌ژرمن با زن و بچه هاشون بعد فینال شب گذشته و قهرمانی UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/22533" target="_blank">📅 13:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22532">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpaAFIjeWZ9C4_sepgoHdkChTBrCrvpY1sqtv42eIRRKlrPQQwEfZYzEn6TkHpOI_xfjzBq-Ewbyv9fXdBNEWeqR1ZV-uqPRBp6DQzbwMDer3JWW8HUrop5GJoXamsnQXGW0UWEBJL9MvtArH8AkCHr0gu4ZksiUxyERZQjPVNv4Sauw1yocWBstkXNf7wyx-OHFSUrvvs6E1CsmgJfnZ8A4JfvB4MjqxfTV0zyRNUGn-5gDOemQegc3sdCnkRXbT-La3Gxwte7AwPwQIc9AQRJAMttP9JZGh2ne6vjPTo21qxcgHrHAycSm0bqqoOvqGpHCpiY4k9yFtAtia4-l-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرنوشت عجیب امباپه در UCL: سه فصل آفر رئال مادرید رو رد کرد همون سه فصل رئال قهرمان چمپیونزلیگ شد. بعدش این دو فصله که اومده رئال مادرید که PSG تیمش سابق داره پیاپی قهرمان این رقابت‌ها میشه. دمبله هم تو قهرمانی دبل کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/22532" target="_blank">📅 13:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22531">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">▶️
تعدادی از آیکونیک‌ترین و فوق‌العاده‌ترین گل‌های والی که قبلش هم توپ رد با سینه کنترل کردن.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/22531" target="_blank">📅 13:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22530">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPm6i7XpbuLruXA9KLV6XcDJXgvAwzzIFNkPgHBQF08fYni6aT3fKF2T6JXBNEI7ghE1rFRcR1i4xkKf2gQ9UoZ1bCLL4kqG9PqdjVdWrrRJ6cgNTIn_hvoTyUT9tRwIA2ZW63oWtR8Lv4I5s1c10xxMLpOGp158zNxlyX5StVkSD1kY57t_xA-0en4gWqWeBY9P9A5e5k-dtcK1jBwxBtJfMbKnVoggnWmBG0w0m2lryylajVv-cPgWfFV7pooF5irSYDYDFqMdU-_DenZHnzNGSWOeGcBqwYeZU38uZxF7n1QQPKH1ZbQfPa21doJ9N4OBER2cj7IbxFySzZYIMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇵🇹
#نقل‌وانتقالات|رافائل لیائو به شکل رسمی اعلام‌کرد که‌دراین‌تابستون‌رسما از میلان جدا خواهد شد. مقصد بعدی ستاره تیم ملی پرتغالی یکی از تیم های لیگ برتر انگلیسه. منچستریونایتد اولویت اوله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/22530" target="_blank">📅 13:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22529">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dt4fS0aNTu4n9t1FaBcZnhHDzUi9t6wt1mXIxQzbjZIqukN0jN7tGyXE8ZzFfVNdc3DMkRekdQaZz4RQ44Du2K6Vqm2xeY6QcI5xh9-oUNY6EBLgJ699IZY44QS5Okk6sZnVd3qUL44TNE43r2aIkqlzugXYtd9ZysI3Rc-DCvKxjK7JN9kezxoxOKFg3AaKqtn-e5tQwbKUbiu936nnBLKQ9zG_V9A0nW_CNuiX0HAk_QdftA31JA4px_L-hSLB96gP3xAeqL_exC6lCbjBm0Zcg3Fv-tBZdtd6RegPR6S8xIlQDOaQ8x_kmwXnni-OlQFyH3xWCTlvaDfuG3TeEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو آموزشی‌نحوه‌واردکردن‌فرکانس جدید بصورت دستی در رسیورماهواریاهست؛ شبکه‌های یاهست که بالا معرفی کردیم همشون تاپ ترین هستن که بازیارو باگزارش‌فارسی، کیفیت فوق العاده، بدون سانسور و تبلیغات‌آزاد دهنده و جلوترازصداوسیماپخش میکنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/22529" target="_blank">📅 12:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22528">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaXKoPz53ZbF4WlmVF9O9Fnt23b6JBA-q5BUAm9Rdw0B2DY0MUrapH2UWbBqFJaCZmODwXWNbt8pLHagnBbXr8F9iQzshIEbyxX3bFlq2xt51URNyKETeFbjLOVqbp4arys1WLOrHzBvijVEOgwH1fRky-SFAkVVe7p9QzcxRUgVYG5QIwrZz_e3ifmWVR5HQ7MTj4fQKBy_vBXzuOEFNaWwidQ74fsjeXZ_bmYns8HH0SfCvRQPvPDhK6Ei511FchIE81QHZ2uq9lY8tYeWNOHX17Pcc9-1o8Z4XgQwP0JcR40SCfUpw4UKz57bpTPKfNlKY-H9lKnxbxWzU_J1Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخرین‌اخبار منتشر شده؛ باشگاه بارسا طی ساعات آینده پیشنهاد برگ ریزون 135 میلیون یورو برای جذب خولیان آلوارز به اتلتیکو ارائه خواهد کرد و این بار این باشگاه با این آفر موافقت خواهد کرد و این انتقال رسما انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/22528" target="_blank">📅 12:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22527">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/460d6cadb7.mp4?token=TF3Fn7zwAh2YeFM0ZS0r1R-jcxAjxO576r3sFotzfqZz6LACz8d86G2e3FSndp1BkIZ2xih64JF49g4bS4D2qg9jyBZvq1GpUNeDNrwIJZEdJAiD55-a0K-inUgS7riugHOcdIaHua-0il7XZcMjbXM9rgWUAirdKzBhOZwz-ZKCbolyS9_sKKJnNeNAbn3gYGdOIPVbBGcoVm9lfvT3xFHLoP7FRlFEOdp586mVQnT6dXgCORzWjdnVh7fg8jX5D_b_4jR6imTRTcfgKQ3ZtZDTTHsEiX5r3v0t9k3ex4EvjvpWwSCL8_5wC0arTbGWRX4qywvBIWfaZP6LDjJPNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/460d6cadb7.mp4?token=TF3Fn7zwAh2YeFM0ZS0r1R-jcxAjxO576r3sFotzfqZz6LACz8d86G2e3FSndp1BkIZ2xih64JF49g4bS4D2qg9jyBZvq1GpUNeDNrwIJZEdJAiD55-a0K-inUgS7riugHOcdIaHua-0il7XZcMjbXM9rgWUAirdKzBhOZwz-ZKCbolyS9_sKKJnNeNAbn3gYGdOIPVbBGcoVm9lfvT3xFHLoP7FRlFEOdp586mVQnT6dXgCORzWjdnVh7fg8jX5D_b_4jR6imTRTcfgKQ3ZtZDTTHsEiX5r3v0t9k3ex4EvjvpWwSCL8_5wC0arTbGWRX4qywvBIWfaZP6LDjJPNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بااعتماد به نفس کامل به کراشت گفتی بیاد ورزشگاه بازیتو ببینه که تحت تاثیر قرارش بدی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/22527" target="_blank">📅 12:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22526">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twXSBUkLwHEerxnqFilwM3ItsZEEu1PE5GgrOl-4FAU8SeAaxbfL2so2RdHHUYGsGy5zMeSlra9vQOGOoVx-g8UpqoRcaSQ1LQMIY2MVb-b3SmHs0Ysbxrsrh9-MMc6aJf-iYf2Y7wa_ihlq05osTi9c5ry3iurjf_a1jLqFBF6l08lB72J_GBXIGmSq-WoBh3TQBWaF-wzyZng7bXmNjmxmmkcRxIwZXwLXtr9TyWK0r-iszb9P2Dhd6w9o5OGazpGup-EhKsrnU16pbXSAeud7O-mD8XTL13hwKEdVv--rzUoNADcliRSO0MVlgyJ0OzG5niq63M44ddalU76a7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ به احتمال فراوان فصل اینده رقابت‌های لیگ برتر 18 تیمی خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/22526" target="_blank">📅 12:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22525">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55166b2d48.mp4?token=eAnf6VgxqYKer5nnoAuPulp97gRj5j9HFnj0fMruWxLcNRFVWinr5i5B4qx9wKk-vVIltvld_eGqXYw-H8lbjk8I_5Xr-PfML5IBFDc9rKxuK1cG9LklEZuNlqJlPvea71UXRNogbvE2YE__BH9Zhz2qnCZAxN7eU-xBs8kcqGYPER1ZC2QojKB-dXbF5TXVt9swDlH3xF4D-DQfHCxoer3V2V7lBZPqjh9JPfjgXaYYLdGLATxDD5o4aUqLAu70GHtEOr865ITTAWQZQJG-kg7W1ojRkb7wnmDAJTLLE1LHjhSc1Ga1VKLm7HcoSPmTxJPSUVYMWGhsQIb2iwRM8whRYRBdnQ1KzhgztgfM0uGHYA13EuTNVG7ze7uzlheq7kD-tb62kEStb5yTh_NDEhyRcL60GEko_n-kn0k9XOpQ6d3fBczgkcxH-8I6EeoWoIteIAE3D26P-VUmOVqF8lmEgmckyy3ysmgOpb6-0zJQTc7rw2PEU1-Bk1-vrNPzPut3jR8SaBpCc-SUXv6tLV7D3hkRz36l2RKRLtUF7eYiwKvfFWTuRIpdmF9e10Z91JxaUwTcCoj9gCrd7NIcS8Ho1XCGBzUraWl1E6UodSr5Kzc90F_ov5xXVlt3OqhH7cMaPoHD_p5zPcUET_VPboxusY8P2E_BORfcgMhYydI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55166b2d48.mp4?token=eAnf6VgxqYKer5nnoAuPulp97gRj5j9HFnj0fMruWxLcNRFVWinr5i5B4qx9wKk-vVIltvld_eGqXYw-H8lbjk8I_5Xr-PfML5IBFDc9rKxuK1cG9LklEZuNlqJlPvea71UXRNogbvE2YE__BH9Zhz2qnCZAxN7eU-xBs8kcqGYPER1ZC2QojKB-dXbF5TXVt9swDlH3xF4D-DQfHCxoer3V2V7lBZPqjh9JPfjgXaYYLdGLATxDD5o4aUqLAu70GHtEOr865ITTAWQZQJG-kg7W1ojRkb7wnmDAJTLLE1LHjhSc1Ga1VKLm7HcoSPmTxJPSUVYMWGhsQIb2iwRM8whRYRBdnQ1KzhgztgfM0uGHYA13EuTNVG7ze7uzlheq7kD-tb62kEStb5yTh_NDEhyRcL60GEko_n-kn0k9XOpQ6d3fBczgkcxH-8I6EeoWoIteIAE3D26P-VUmOVqF8lmEgmckyy3ysmgOpb6-0zJQTc7rw2PEU1-Bk1-vrNPzPut3jR8SaBpCc-SUXv6tLV7D3hkRz36l2RKRLtUF7eYiwKvfFWTuRIpdmF9e10Z91JxaUwTcCoj9gCrd7NIcS8Ho1XCGBzUraWl1E6UodSr5Kzc90F_ov5xXVlt3OqhH7cMaPoHD_p5zPcUET_VPboxusY8P2E_BORfcgMhYydI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لحظه پنالتی آخر آرسنال و قهرمانی پاری سن ژرمن در فینال لیگ قهرمانان با گزارش جذاب فرشاد محمدی مرام که یکی‌از آرسنالی‌های دو آتیشه هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/22525" target="_blank">📅 11:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22524">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91b2ba8656.mp4?token=ZiV8r8Zvx-D9mO-BnW1ROUU7vTSXDJsuKN6M_IxxNqg0FbC92VZVEbF8MhwAuhTH3Ihc7wZODruDqxQyeTpCQfhEVdKoIyz1ICHWnKpErsCkCcwRWub_ni4VIIpec0QU02W2ZAh7RfgRQLLnc9i3cARw1207qAhsqZSTXkxknpdSQSSHJ63k2BGTrSg4sbn6nlSD6lc_Oi-Sr0JhYcuScBxkrTXkHrDKj-tdMqQ_rs0uiHlNhQ1V3aSlqug5VNAPJCMCWd1k-Nnogdxx6yMu71d9fSzDvgHHjOpVOTxNuMz7zl7YrQeAcfLL-cQeISKLi802-B-np_4psRnZYidQzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91b2ba8656.mp4?token=ZiV8r8Zvx-D9mO-BnW1ROUU7vTSXDJsuKN6M_IxxNqg0FbC92VZVEbF8MhwAuhTH3Ihc7wZODruDqxQyeTpCQfhEVdKoIyz1ICHWnKpErsCkCcwRWub_ni4VIIpec0QU02W2ZAh7RfgRQLLnc9i3cARw1207qAhsqZSTXkxknpdSQSSHJ63k2BGTrSg4sbn6nlSD6lc_Oi-Sr0JhYcuScBxkrTXkHrDKj-tdMqQ_rs0uiHlNhQ1V3aSlqug5VNAPJCMCWd1k-Nnogdxx6yMu71d9fSzDvgHHjOpVOTxNuMz7zl7YrQeAcfLL-cQeISKLi802-B-np_4psRnZYidQzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
واکنش عجیب ایوان تونی بازیکن تیم الاهلی به قیچی برگردون کریس رونالدو ستاره النصر
😳
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/22524" target="_blank">📅 11:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22523">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlR-izVaYPfLOz03BZFNOMdGXgQMVYM2MlcIpkM2wjSWT6NHtqBqd6ioLZaAjy7B7h5TEPC18QUKTMiRBP2MHuNbLmt_QxDXQoDIn9elChQ-npEpkLCLWIts_bD7-A03x5vVmKQmX3Dj13UzwMMcJ8ABTEJAfUjb7MTdXsfHVZH2rzbwAfl3oyNj08AHce0vXlZ0opkxrEaks2QWskAb_eZvzNnj0zXzhp5LoIi5MbwQkFGNs0MTXz49Mp6OnwIjnkN7zH-oAZJonBO5-GrVpY9yCcbp6qhUHAqABIU6XbxJTCB_F-RDwDAY91izJ19_HgtU59bd4e6c_1ZgVydeXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ مدیر برنامه های الهیار صیادمنش مهاجم24ساله سابق تیم فنرباغچه و هال‌سیتی درگفتگویی‌کوتاه بارسانه پرشیانا اعلام کرد اولویت این بازیکن برای فصل آینده حضور در فوتبال اروپاست اما اگر تصمیم‌به‌بازگشت به لیگ برتر داشته باشد اولویت او باشگاه…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/22523" target="_blank">📅 10:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22522">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1346d9dda7.mp4?token=fMhGrIc12t8cGl9I76IbF822rhnpeSwjR4iS1yAs3Gu2WYVGX5zD55_KMmdeIhFK0T8CCNF9JfuWvgk2kaA5G7aGtkv5CHiayqKhFNN7CaMG-Jyq3sOerNxR71LuVwhkLzJCDsgc6F0Lpo2BghlsCE_OjIvc-h5F5CbbPHvBzMXw9yfJPrGPSiioezMoiqvXiicAtsAQoVLmDxwDs4jVz5y7mvz0E1XZR4iGcmrMaX1Mal1-JkrviHAwpIzRw8M_nuGuwyUZbNN3u5SJRp9Rol5vYs_Kqxe-GwEIhxqpZx7xh3MtJBDzeIWJu74YehuTdOnM93SWSWVtEFPUy_FCNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1346d9dda7.mp4?token=fMhGrIc12t8cGl9I76IbF822rhnpeSwjR4iS1yAs3Gu2WYVGX5zD55_KMmdeIhFK0T8CCNF9JfuWvgk2kaA5G7aGtkv5CHiayqKhFNN7CaMG-Jyq3sOerNxR71LuVwhkLzJCDsgc6F0Lpo2BghlsCE_OjIvc-h5F5CbbPHvBzMXw9yfJPrGPSiioezMoiqvXiicAtsAQoVLmDxwDs4jVz5y7mvz0E1XZR4iGcmrMaX1Mal1-JkrviHAwpIzRw8M_nuGuwyUZbNN3u5SJRp9Rol5vYs_Kqxe-GwEIhxqpZx7xh3MtJBDzeIWJu74YehuTdOnM93SWSWVtEFPUy_FCNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ژوزه مورینیو سرمربی‌ سابق چلسی:
ابراموویچ مالک چلسی به من‌گفت‌که برای مهاجم کی رو در نظر داری؟ منم بهش گفتم دیدیه دروگبا؛ گفت اون کیه؟ کجاست؟ گفتم شما فقط پول بده و حرف نزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/22522" target="_blank">📅 10:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22521">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c743e5df08.mp4?token=qLctV_nQN5iOde_2fpasSzmwPCuVQrTcqcTZIDKySIXi680NsiKGZsagPwQpicEbmlscGOjWR4zovUfG84Jhssqm6M1f3JHk9AndU4b49zagq9EdYdJkd0AP4m7MAXols3kxCtWUXr-Hmu2U5MDCq4Wr8rKQjT3PlSKSSknetkbdYp-Y_z02Zc6A7ArxWunff1BdEfX6-bgECvkz4kylM6vjXSzs1oELLQHQQEQpuZfG85gU1YqlhhHQJW1XDHbWVnH-nsexbPVgqgSQ3Rv_jkCNI9rznb-vQ1aWPkl3FXgoURPcEMtN3dwgkdgIFUQwoYtbduxiQAFEFqYVVyyoKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c743e5df08.mp4?token=qLctV_nQN5iOde_2fpasSzmwPCuVQrTcqcTZIDKySIXi680NsiKGZsagPwQpicEbmlscGOjWR4zovUfG84Jhssqm6M1f3JHk9AndU4b49zagq9EdYdJkd0AP4m7MAXols3kxCtWUXr-Hmu2U5MDCq4Wr8rKQjT3PlSKSSknetkbdYp-Y_z02Zc6A7ArxWunff1BdEfX6-bgECvkz4kylM6vjXSzs1oELLQHQQEQpuZfG85gU1YqlhhHQJW1XDHbWVnH-nsexbPVgqgSQ3Rv_jkCNI9rznb-vQ1aWPkl3FXgoURPcEMtN3dwgkdgIFUQwoYtbduxiQAFEFqYVVyyoKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یجوری هم متعجب شد از اخراج شدنش که فکر کردم یه خطای ساده انجام داده!!! دِ اخه مرد حسابی زمین فوتبال رو با رینگ بوکس اشتباه گرفتی
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/22521" target="_blank">📅 10:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22520">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b417aa36e.mp4?token=qorvY22czpWThaLJuvmllWxFK9h-5NGwmTkJkpurThh0CPd-7FK95q3Ba7cCGUWNRTrQweu1bwRW4U42uLyKe869kGqGuVf3pJgGUdsosrYZY6op5Rq2UXbnuSXx6z7FGtNQnKnSV2rRpmaLC5mO-dOpL5EJsJvmOKQyWsmdYD-3ylJ0PQMrm9dWisZ_XXqXmRruTuzT_3fpS3QNIa1IkMXs6yEtRYQfUyoA_ESSS2ySB-ZHfImOE2TD9bEB_BYjcMoBHDIEWQ92P1P7HIGHVj8bjTT69QQnDCvVftOCFwZVXiTcsUZdvE5zd5tHKklohBbmnyHSR4xQJwLuk7uzXE3wEePplCz9GbRdmiKTXXG2t3h-zFVwF6dnXxuV-ZJg47o4TglgUUT2xsAVXmpWta8f0Zyb_9LxP-H8IysRvt4k-dOr5O9HgGuKDW_pns7YSay5jHPofb6X0fTZ7ktAZMhmz6XMeqGTo1EycB3epVgfSMaOEwvZw4TuM1HQ-usO7hHLzzm4M3fmK8UHYTIIyjA80zp-o3PSMkzntGDpcQ9-kBtXck9a0bWrmIYZoRz7Z3pKQeugvbqGS6Og2CaUdYNMo704rfrtiuDF0OGQYJc9LXq_hxGrswkfG_lw2wO2AcAwpEqg6LCrS9WYSxuW2WLmqTfDTF-EKp3JGgoLIro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b417aa36e.mp4?token=qorvY22czpWThaLJuvmllWxFK9h-5NGwmTkJkpurThh0CPd-7FK95q3Ba7cCGUWNRTrQweu1bwRW4U42uLyKe869kGqGuVf3pJgGUdsosrYZY6op5Rq2UXbnuSXx6z7FGtNQnKnSV2rRpmaLC5mO-dOpL5EJsJvmOKQyWsmdYD-3ylJ0PQMrm9dWisZ_XXqXmRruTuzT_3fpS3QNIa1IkMXs6yEtRYQfUyoA_ESSS2ySB-ZHfImOE2TD9bEB_BYjcMoBHDIEWQ92P1P7HIGHVj8bjTT69QQnDCvVftOCFwZVXiTcsUZdvE5zd5tHKklohBbmnyHSR4xQJwLuk7uzXE3wEePplCz9GbRdmiKTXXG2t3h-zFVwF6dnXxuV-ZJg47o4TglgUUT2xsAVXmpWta8f0Zyb_9LxP-H8IysRvt4k-dOr5O9HgGuKDW_pns7YSay5jHPofb6X0fTZ7ktAZMhmz6XMeqGTo1EycB3epVgfSMaOEwvZw4TuM1HQ-usO7hHLzzm4M3fmK8UHYTIIyjA80zp-o3PSMkzntGDpcQ9-kBtXck9a0bWrmIYZoRz7Z3pKQeugvbqGS6Og2CaUdYNMo704rfrtiuDF0OGQYJc9LXq_hxGrswkfG_lw2wO2AcAwpEqg6LCrS9WYSxuW2WLmqTfDTF-EKp3JGgoLIro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کدبیس سه‌شبکه‌جذاب ماهواره‌ یاهست که بعد بالااومدن نیاز به‌واردکردن‌کدبیس دارند. اولش دکمه F1 میزنید بعدپشت‌بندش‌سه تا 3 بعدش یه صفحه میاد که باید کدبیس رو وارد کنی:  کدبیس شبکه جام جهانی HD:  BISS:2585AB552585CD77  کدبیس شبکه ورزش تاجیک HD: BISS:03A01BBE20C16D4E…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/22520" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22519">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baebe6400d.mp4?token=KyRlNC9MlB7n1P1g3gVOu713wsYXAKdFg4fEUCV8JK4gWy_rPE8LfOKR_5VqIRpCamNqcmnfrCaQpcDNf-CiAuJVBrJNi7COimhkiJw8cDLpxLQfZ3lidecwg_S7JkxSRh52sHw0lgROeW3Z7pzsXdbykEXnnoQFeA2WGRoDGgHMWEXz8z8CcNw4o489zXQ_QO5FlygBoyFGtOuoI-gPj7DJBsy4tujSYdVshJp7XM4WOWBZAw7zuQQQq-JmqTREvRZYKfVVyZRZ-VG7I-fKvLWDkpeGYyrYfXMpEFKQBlpK4IdyFcwAMK0JjGgfqvUbvc0omGs9OOdqaT1b3GgCyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baebe6400d.mp4?token=KyRlNC9MlB7n1P1g3gVOu713wsYXAKdFg4fEUCV8JK4gWy_rPE8LfOKR_5VqIRpCamNqcmnfrCaQpcDNf-CiAuJVBrJNi7COimhkiJw8cDLpxLQfZ3lidecwg_S7JkxSRh52sHw0lgROeW3Z7pzsXdbykEXnnoQFeA2WGRoDGgHMWEXz8z8CcNw4o489zXQ_QO5FlygBoyFGtOuoI-gPj7DJBsy4tujSYdVshJp7XM4WOWBZAw7zuQQQq-JmqTREvRZYKfVVyZRZ-VG7I-fKvLWDkpeGYyrYfXMpEFKQBlpK4IdyFcwAMK0JjGgfqvUbvc0omGs9OOdqaT1b3GgCyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ویتینیا: اونا تا میتونستن وقت تلفی کردن، اما در همچین بازی‌هایی بایدصبورباشی؛
ویتینیا علاوه برکسب‌جایزه بهترین بازیکن فینال یه‌آمار فوق‌العاده هم ثبت کرد؛ هافبک پرتغالی، در فینال لیگ قهرمانان اروپا مقابل آرسنال باثبت ۱۴۱ پاس صحیح، با رکورد تاریخی ژاوی درسال ۲۰۱۱ مقابل‌منچستریونایتد برای بیشترین تعداد پاس‌صحیح دریک‌بازی فینال از زمان شروع ثبت‌دقیق‌داده‌ها درفصل ۲۰۰۳/۰۴ برابری کرد؛ او همچنین باثبت مجموع ۱,۵۸۹ پاس صحیح در این فصل‌از رقابت‌ها و تعداد پاس‌های‌بالای ۱۰۰ در ۹ بازی مختلف، به‌تنها بازیکنی در کنار ژاوی تبدیل شد که به چنین دستاورد بی‌نظیری دست یافته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/22519" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22518">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOJv9pBZD9sn5KPGjoB8XxocNU6fhGHDePicUkeWhCy5-BAmTpc2l3vmVeP9gl3gDVOCK1nNgZfrbX43bp5pDzjswMfcdZAEf6U3HONdVQSQHhNNvRoPMqNjKQyhIQGsGUg4TWw8kDbfuTKopLY3axyAcE6Q6PMD5cSMrkxOqiluhZYPNXG2PBnKMr9aa3OndnvOXxPF3wOgh6M6U5JF5GFVeaZHU3wT7qu_0sQ_M4nXv19aUGN5MA8TJfp_j3V9orRTXbNJHcvlA2xXwYmND0bj_iJF5uMRJyRPnWejq5urwPxoCsXPkHvBsMHBmsmSbGLLSPA66DpsTyqR5TuO_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
🎉
کافی‌فقط‌عضوبشی‌تا
#وینروبهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r10
📱
@winro_io</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/22518" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22517">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSr3i4a88R3odeglq7J6gaDvHX64MeK8nmNhbmXZY-nUI-OaVCNM84sHK4rnPgnex8uC10kNI30i89T3ehQbOTvA1jYEgq0C1DPjLoPE92ZUn1kmwqc1v-9Za8asDSlQk9GUactM-PosXd2aIKQVpTD4a93KnWmFiI-b4K4JBGjjyUo8yUH5ZJ9lZtycUiBkyrxNz20bZPacgfFXpXucpnqPsA7Zj-txRxx01ip9fD-PrHDtK2zlVdDwtDX-l_7aeQSjZ7IgMOTjfVtncZbAbMoGa36tYxbzMrfLZbxPcQnY_6wnExVAI28E9KQq3EfkKshvHvDcYylCqW8czr9wRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با بازگشت نیمار جونیور به تیم ملی برزیل برای جام جهانی؛ وینیسیوس جونیور شماره 10 این تیم رو به نیمار برگردوند و خودش شماره 7 پوشید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22517" target="_blank">📅 09:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22516">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRGtYcYX-xgxwUSkQzt0fUhQYexxA14oAYzBzPX4rZ2q665QVLeqfJxAADY0xkvlnHboXagmqMAfan7YjPefXQ9IQhptxq69PC6oyTX2ZFIOQJAlzNW0gkSqWggjy2aiO20KSmK1ehJzru2nT25MsSWkHGoa2WReu_nh51Zvp2sG-QBKvBVYvPfheH5AJx__7S9i25qGGFe9bOGgm5ZG9gXVH27iq-UTUrohH4IVH_RfGmghItZTqy53RIbW5KPI9EHHwpJPnwMhHpII21yDjSZaCVW6uUOkhqwl9XClNuCwjjTZeJVskaEQWLlOJ0JiMA70D4PqMS7_KhrWp55e9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|گاتزتا:سران‌باشگاه منچستر یونایتد مذاکرات‌رسمی‌خود رابرای جذب رافائل لیائو ستاره پرتغالی‌آث‌میلان‌آغاز کرده‌اند و قصد دارند این بازیکن روبعداز جام جهانی 2026 به خدمت بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/22516" target="_blank">📅 09:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22515">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNMgVMRIBOuuv2oonpJR_rI7ibJgXSvto7ZWH_TO15xYV-KPkC_iSkCOCOOobo1av0tG0Tvl_btwp1_5ok4mrpj_XnUqfYCVLiWYQI3P5twTxTdHxbAtS5YEmL6PbgZ_bL0Vd1b3HZYXGcB2PEKy39KI-VLiGoQnqAJsVyH9OsHXju8no0K3CEdAFzOTJWamhu8K63I6cUhl2WZ0iqQvdV9jq1TBDM-VtiCv5yv4dhLRd_dtj5TTvgJr11G99BUadBDItcH1KYwbi-mZrrGyF3tLo77HJL5xHeHzJCD-glamtCop8nJHeaJxwsRQLv5p-UFCZhR7tII6djM1EQ5Qjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛ برناردو سیلوا ستاره سابق باشگاه منچسترسیتی؛علاوه‌بر بارسا از اتلتیکومادرید نیز آفر دریافت کرده که اعلام کرده اولویتش عقد قرارداد و پیوستن به‌باشگاه بارسلونا است. این انتقال بزودی و به شکل رسمی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22515" target="_blank">📅 09:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22514">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aulmGRz6tDQ-5vyd2wUfdbsGu2GzdAmH2GrleuMJFABplvHyZmdnuDdLEdl8oFGjHBURyZyi_NsyYEOzQu69bfhiQU9TnHGo9zaoTZrwXUyWJ1iOlbT_1OH2V-Nc-nmJmf4JOmJbTKoX08eKfO034ucf6VS3kN0I43wv4wCa6odyfvpUzsj23K0jx7rXzfPRz5YwTvGA_ph1lGmEMAVzEoEMGMx3Lv11I3QUDl3chCECzNc07V05qsw_dKIaX6yCwGvXDmqeeLdgCc3Qn9ESxrF0-x2nVoPitSVFyQnqXac_af3oTnhU-p6YgSjHmwlAKLUT1lwrHHZW5oOOJKdjKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
مدیربرنامه‌‌های دراگان اسکوچیچ سرمربی سابق‌تراکتور: به‌باشگاه‌تراکتور قول دادیم که امسال اسکوچیچ راهی تیمی از ایران نشود اما اسکوچیچ از ابتدای فصل آینده با یکی از سه باشگاه سپاهان، پرسپولیس یا استقلال قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22514" target="_blank">📅 00:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22512">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3mErtgvfzMSL0PqA49tmjNhD72oHRuMLV1hg08yJ2LZGlbDNL-JCtWCFgjCHRs9a2ZjKz04utYkH0r-f2rmZAVLnNbXC2dsBcFim58mevpAHWGSi1HEDobrcqoH2ZOFC3UmGIgogoKj1PF8vrh85MCRxVH4nPpLI5vUDHBqbE6RUfOtarBlQc4z8vNLOdiN3QrB1ixFP2fR5C8BdnAgRJsYiJpTwZw7qlZ0MiIuCBkajbsoG9_NCDMxSnHrQBd_CHNkGABh98jT8EFyFfUIU0KNCcVFk26AdoGYE7g2alTnHdYEWVzO3g9Fxbyu4-tOCWeRZG7ydzEgnXdk9JlSxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌بازی‌های‌مهم‌‌امروز؛
آغاز مسابقات دوستانه ملی پیش از آغاز رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22512" target="_blank">📅 00:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22511">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJm-cTZYycEcTIbfp90RapBSPaFRbD9NGu_ZIanE7yUKgsMRFzgIZfdMBoah4o5xNOtsstOAi-qkK-F8tY3HiYgp1vEqTKg9ru1lov6-_bZEQ0Q7c-E9vkwfd19aXqShBY9VF12ytR__fVHm9FbzMho4aT_5jakeP-H9lh-3PSp2UMXbOlLMqiPdcwOB_2vU5PSfQDw-2wPTcHY8s331qAByZKBX9qyQoz1BgEL2nagwyzaYORzhXstaJAFzoUstPOs8UcY3tB4H9GdCb32w5AQGXN1d4JYjUjVG1hmDVevVvJdqtklr7RC5TJpRhtPnzgpEVjqqa7PLFDRy-UZxwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهادیدارمهم‌دیروز؛
دومین قهرمانی پیاپی شاگردان انریکه در UCL با شکست توپچی‌های لندن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22511" target="_blank">📅 00:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22510">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opNzkJm_reRBq03VhD4Z_sftbTtdCdetrSNz7jGhIrW62xi0DlqYDiKO0kqcvZ-hIm5crqzvq5K6VB6M_ytKnLVjOzbP410dV3IpBKj7TzF3NcZEeeyZFZ72aWihq3Yc8tMDV95NQ6-ID-0g9_sre2PLZGoUOt91cMiaKG5ZdVZLqceOXLqdCWnG3tFzkAWFqq3W6bP7JJo50iLboG9K5Wdj_Hv8dJd5HodgaWYuqCHWDzgzKD98uTjfYwNg3wuTKIEtwdKuRDScf99KA2MHeThDSvuGSdZmZwhdafJYu8RbbJ11iqrIqivYw27p5boiZjdly3Ikdyc3e-0Wp4p_rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
کافیه‌فقط‌عضو‌بشی‌تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست. پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a9
📱
@winro_io</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22510" target="_blank">📅 00:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22509">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tt1bSjJ8RUaie_NuoeqVKUEQmll713ITtsljaSMaLBpu7QgpDv5DZgnNVLT8SFC3DcxQpD9kGuwd7pjoWNDFLIaZP4ISUQfr5jKAmOHyKlStud7RkFSjy7PpQG8RYz5mnUwED8a9ifB-PTC2uxtwpQS0BRizjjT19TkOnrHlno7HbGy6-_TSwYFZZes_rbTxdM6RBMEt8ak5Aue2yrwIUNNubtvN5nrNg2IsKOuwaIQwy58ev1Bv37gFerHumK5tmrOjG8MmNb14sH5zrj4WzvNjMhXxewE9XzLSvekvH274PwY60GhG0uAtPeFow6vtp9D87pFyvSDD8Eo9Yi7mtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های دوران سرمربیگری هانسی فلیک‌ و ژوزه مورینیو سرمربیان فصل‌آینده بارسلونا
🆚
رئال
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22509" target="_blank">📅 00:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22508">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXCd4xbvjB2xJGzXjwnBLaBn__r1B2fL1ZMYJ-lsB-kN7dZNcJxMGEvF2KeYEDA7i90zPpM9g4Vrg4Tmu4RFa6JPgQztNknBb6SaopPqSKJ1kgJ7sAJ81LKmEomimcpvF1UEwaqD5DNOy1l84_R1TPcCvrNwBI__pM2fs2B20N1mI_4Rn0PaIe1nJsG-YevLy-thNwrMulTQNXig7f11SLepIfKxjZCOeMOUr6b5VBtc9fdtz7QEFP96yXDqHsWZH3L9DWRzKD7c9wOmvlbOqCgJPkqZ_dOX3zvDBhqGORBGKKS41WoYgDU6XjszmBwHJ2n6gn2bdkJ36TI3Ny1pMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22508" target="_blank">📅 00:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22507">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zu42il0P5tYgWyD1bHF3ljhiTxSsSK72pTKXmuehZE74bbq2qKggq_Mw4p6D0CRzX-zNYqH7NvbhECecs_gOpjv_WG9RuFm865UjO1APQPv29jLNEL6zc0PQUXi_7Sw6NXU7PjqrL9pXoZHvZDDCkbL6-P4X-_0W99K9C7SDz1E0z8osOwKH4EiRLUvAMyYkPr_03J74_oolTiqHYnQysmjUEevL5gLVAcvfygJOvBIR-XDhPGLgqfINoVue8Ehjrxo6nJWgbA0pYpEMERPGTGatr1B6z0GFt2vYlULXfAp_M-2qPYSpZxZjF-xDRg4pdztWrwwSix9A2nCaSS3HaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
تمامی قهرمانان ادوار مختلف رقابت های لیگ قهرمانان اروپا؛ رئالی‌ها همچنان‌بااختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22507" target="_blank">📅 23:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22506">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMhH7AKb4YvsTp-gDxFVmjm6d2-7qW934cz032BpOu45fepeQur4bysZF7NwqK5lkvhofHyMenbgMkDdSWI2KyJ1PU7JrDiKcMYsE4B3zlXJqn1DKArQ6Xm-09GLMhhbZtbnTxbxg6E-DMiL-3-8l8Th9XgrSs4UEtogbhcBxESgsA2eMLTXIgEUbDaahj7LpHu94aZ_kjrKKcQYvbUYpBqj175tqX1Dd0bZ9xI5Vc5Brj0l2caM69gU7G6E3TkKybOur9YqwsW68887Je3TY7pVmvtAltYsbWiExbupF_gSZ7fjDnk-Scn-Fy88RPgHjTyUOq-IeN054pV-3vOtdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیوکامل‌ضربات‌پنالتی دیدار حساس امشب دو تیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22506" target="_blank">📅 23:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22505">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d5a3b7a3.mp4?token=ZHdDdsFPzFIJ6uL-Udg5ZdzMwzjcgl-cK2VAgn8ez61gjWAXi3br3eguMHUvA5nuLfTmWt8GJSL5i9Ha-NhOtLTu4LAmxlMPUpSHMPkLGBal1OVw_u563CinAecVRa3S807nnSDncNzgeu9JJAirKMGVrldwKGL2o2pcjToVujxubUXPe6x4x4KAV_GudcsJeq2TBfjRvehTpRlOriN7aeIYCDlikwDQL9PWLLKPJ9AFjQob0MXfJ7a-74aRtOEKvrJ-FjIsta00Ws0aaX4wdvpLky0mbFmUHWTYmGzhXbnhpe666In9LxGui_RbstBsLZcJAcaIJf-knjmLwE1L4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d5a3b7a3.mp4?token=ZHdDdsFPzFIJ6uL-Udg5ZdzMwzjcgl-cK2VAgn8ez61gjWAXi3br3eguMHUvA5nuLfTmWt8GJSL5i9Ha-NhOtLTu4LAmxlMPUpSHMPkLGBal1OVw_u563CinAecVRa3S807nnSDncNzgeu9JJAirKMGVrldwKGL2o2pcjToVujxubUXPe6x4x4KAV_GudcsJeq2TBfjRvehTpRlOriN7aeIYCDlikwDQL9PWLLKPJ9AFjQob0MXfJ7a-74aRtOEKvrJ-FjIsta00Ws0aaX4wdvpLky0mbFmUHWTYmGzhXbnhpe666In9LxGui_RbstBsLZcJAcaIJf-knjmLwE1L4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اینم‌نسخه‌اصلی صحبت‌های امشب عادل فردوسی پور برای دوستانی که قصد استوری کردنش رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22505" target="_blank">📅 23:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22504">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a1e84d8c.mp4?token=H17sHIaekiYDQYZJYnwyJw0XGhiVEu90eJbDOpVvP16ET5qV42qkz4F8ueAPY38ERVJH20JeQgJvABnmsfHSoRGEPFGhgtMXxJ4S8FgPytezGudnrNAgx-2fwGQFARBm68cCbGcSFp72Y1pBPlC5sqj1OHqmbCQJn4K8SX-143VHMUFmq-vUpr1Id8fJ3c2-KP02xg8qXzdCYYWKv9fpa7n-5gmImPG5TAQmj8uZHKCEar0alp93qciwWHC4IBtakO_FaPKZgmgIP_AF74eEDqvwaIwK6Xr1OQJZNjeZtaa9a4FE7mpT1yP8ejTulnPQ2cLmrAeilSoeObPDGlwgPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a1e84d8c.mp4?token=H17sHIaekiYDQYZJYnwyJw0XGhiVEu90eJbDOpVvP16ET5qV42qkz4F8ueAPY38ERVJH20JeQgJvABnmsfHSoRGEPFGhgtMXxJ4S8FgPytezGudnrNAgx-2fwGQFARBm68cCbGcSFp72Y1pBPlC5sqj1OHqmbCQJn4K8SX-143VHMUFmq-vUpr1Id8fJ3c2-KP02xg8qXzdCYYWKv9fpa7n-5gmImPG5TAQmj8uZHKCEar0alp93qciwWHC4IBtakO_FaPKZgmgIP_AF74eEDqvwaIwK6Xr1OQJZNjeZtaa9a4FE7mpT1yP8ejTulnPQ2cLmrAeilSoeObPDGlwgPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
صحبت‌‌های فوق العاده ارزشمند و گران‌ بهای عادل خان فردوسی‌پور درشروع‌مسابقه امشب فینال چمپیونزلیگ و تسلیت به خانواده‌های داغدار دی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22504" target="_blank">📅 23:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22503">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVqUl8-pm1K0ZmfQEVRFM9HTiAwRj-K1kiUMIZWF7Prw7ketzkEJXWdXvXN-k-rnEwFnPZxdSqVSNpmoNZ9xGxm6GhTEtcaCsdR-2H670xMoX5QzLn7C9Xt50zBMGpKQ9CToCF-2ugmvNsSLN9k1XcEMKpSw-j753ue8456GBpKkJWplT2O1hE7gr14xHst8WjYR_IZnA9O56WsSRuu_OXfVP34pVer3SPnhvNPp1Q0PkL6wPk48FKZ7IyOxasXH_5OA0DMNRulT3yFsOEgdq4YmlyVZZc610BfFOhMtPoYY-illU_AkF8OiqDLKhR9QpENuRdP7Mw4f_KzPWQ0Xsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22503" target="_blank">📅 22:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22502">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d915ebc4d.mp4?token=O_h3BIez4CzGzhX_XdSdBU_Bu7ET9hJ4AfwIhn6KKAPuJTcKwi2mDtGkA_evsf0AGA7Z2yF9cLCN1f8jZSVoZA3ywIy6OwIoCrBRK6h5AyZ20dgWbkKtU1PE85cqtpmyDqyUcWXhXOrke-7vQjKK9iJH54x1oZakaOSNNf6UjNjhnVW7y-lUmFqDMVJh-FiRj7pzl_VNEPqknwRgRHwMX4GDSJe6S5bROOWaaDH1PCegHmUnxZ76OfcQzH4qGceAObMXwCtE0I5up5O_QPrZmtNA4y-fDE4rUSfP8cyRDhSVrX5BlpORX4gLhQce0Ynzc-ksrA6Gf9ABR8dujBG7JWue82sMGdFxVniEmcy3wId7tiGbSDWVhikpQ3V6nET68lUpT9xFTvYBKxPmVhD3ncYdHH_a3tGtz4qtu1xxyYAmyJydXmKLgX_Nx1KbO3GEmCb4PRa-6fxnalAkQmN11GGs-aTjOQ6qcdELKArfXGNroig_4zv22pYriyPJhUyXm7-l8toIIxaKJg9DQZGeQ6bhbBuQA252rEWj_UCiNigmri1jeq2VFl5tpKLv42Jy_3Z7pjaSJ6Oxmg3NK7cE3aBbGvLPyraTSddfCDMgMXajgRaD7D45yCAl5QjnwVTFkkWz8C84peW5GFznyI2WGkEAlcfi1HZqIlbiWKY8Yvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d915ebc4d.mp4?token=O_h3BIez4CzGzhX_XdSdBU_Bu7ET9hJ4AfwIhn6KKAPuJTcKwi2mDtGkA_evsf0AGA7Z2yF9cLCN1f8jZSVoZA3ywIy6OwIoCrBRK6h5AyZ20dgWbkKtU1PE85cqtpmyDqyUcWXhXOrke-7vQjKK9iJH54x1oZakaOSNNf6UjNjhnVW7y-lUmFqDMVJh-FiRj7pzl_VNEPqknwRgRHwMX4GDSJe6S5bROOWaaDH1PCegHmUnxZ76OfcQzH4qGceAObMXwCtE0I5up5O_QPrZmtNA4y-fDE4rUSfP8cyRDhSVrX5BlpORX4gLhQce0Ynzc-ksrA6Gf9ABR8dujBG7JWue82sMGdFxVniEmcy3wId7tiGbSDWVhikpQ3V6nET68lUpT9xFTvYBKxPmVhD3ncYdHH_a3tGtz4qtu1xxyYAmyJydXmKLgX_Nx1KbO3GEmCb4PRa-6fxnalAkQmN11GGs-aTjOQ6qcdELKArfXGNroig_4zv22pYriyPJhUyXm7-l8toIIxaKJg9DQZGeQ6bhbBuQA252rEWj_UCiNigmri1jeq2VFl5tpKLv42Jy_3Z7pjaSJ6Oxmg3NK7cE3aBbGvLPyraTSddfCDMgMXajgRaD7D45yCAl5QjnwVTFkkWz8C84peW5GFznyI2WGkEAlcfi1HZqIlbiWKY8Yvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیوکامل‌ضربات‌پنالتی دیدار حساس امشب دو تیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22502" target="_blank">📅 22:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22501">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50097d1448.mp4?token=lGNM6E1X3NJLmwAOAcyC6TU-uuDcfX7FvX6UZjwJEd0VzqDsr3N56aBzkuruZZg7yND7L-ZEkTaYtlCFYC8riLXPXbLJfMKj-mKcnTIV6HFeOLZk_W_9RYi5645tM3ZMN6iPZj-FDXMjMAUapvvXJkHQVZD76PfH-MK305rjSCVnC9gFSIA3zqzsj528RMjw7JF1F3AKITTkxTspQByq3wpTxMAU6RkE7cyLwb8vJLHgjuOjly_4mxX5w8EyLcGWZj7Kb_tstH0NmQ1V9vJ65IJiGiw2f5O4xNFvOreiwzSyZTiaMyinzzrSZhc0AKlt7-Fnd_FOHee_aYXIWYrtgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50097d1448.mp4?token=lGNM6E1X3NJLmwAOAcyC6TU-uuDcfX7FvX6UZjwJEd0VzqDsr3N56aBzkuruZZg7yND7L-ZEkTaYtlCFYC8riLXPXbLJfMKj-mKcnTIV6HFeOLZk_W_9RYi5645tM3ZMN6iPZj-FDXMjMAUapvvXJkHQVZD76PfH-MK305rjSCVnC9gFSIA3zqzsj528RMjw7JF1F3AKITTkxTspQByq3wpTxMAU6RkE7cyLwb8vJLHgjuOjly_4mxX5w8EyLcGWZj7Kb_tstH0NmQ1V9vJ65IJiGiw2f5O4xNFvOreiwzSyZTiaMyinzzrSZhc0AKlt7-Fnd_FOHee_aYXIWYrtgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22501" target="_blank">📅 22:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22500">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhQeOU9pq0yJXgU9_FJeqx-2ZvbjHb9xeKLSpOHdoPg7n9ymgL0pPbNvfE3CLootEWJ7bXGR6VtGzgKXKNKaGmvWEzSChQZj4Qz6c4smrufkULGHBTkZlobRUvtx81Q3DzxTXXyhzf7ImGRxGTHfCBYP6mu9-IxKk6G7m0x71VxiaCru3fUNi6vOiRe3hd-CfqtuR3TJZFmKqepY_iPtKdQs44HglIBVyaykDF5kGSrFqaETNV6x-tch3OI7WPIwv6Jn51QNnhXDyhL_zO6qJIrT6q7J4wPVdeuYE1VHyG2JBc4dmhdN-CVQjVm_CcZ4ocpgwu0llFyyYM8N6vIoWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیدار فینال‌لیگ‌قهرمانان‌اروپا مابین تیم‌های پاری‌ سن‌ ژرمن و آرسنال پس از تساوی یک-یک در اوقات قانونی و اضافه، به ضربات پنالتی کشیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22500" target="_blank">📅 22:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22498">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c46R93KJ1KuIHx0rHROguWv4Nm5TVO2od1hT5Sc-L8I-DydwTNUrUSsz2AGlvTkgdTx2Bj4KIgGu8w1M-lt8XqBliwmUoTavfOP9jJLe2NHzNKcFLoXLEuxO49pHnp9pdBDcQDI_lHyZm7uLTW_frUtfUbTGw3gJiWUv6301f5pY-yx1ED5wqdwhKY_w10hqd8OJnbdVg5C3jQuzb3a52lW6OIf-AXWN9WLF0ZoHw0tJtEHWXwxZ5_FtEw8IPzEcanQdyNu01f098lbl1uOOOY8Xbrb60aKKW2jSqdHrLS54DM8x77wJeNI_1phCpzvW_-no0AhmK2QV-6eikojppQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازی مهیج و دیدنی امشب دوتیم ارسنال
🆚
پاری سن ژرمن بوقت‌های اضافی کشیده شد. آمارو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22498" target="_blank">📅 22:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22497">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgqxalB68Es8dsVEO7AvKFtzxoa6wkRtZz0-cJxir3b8RmUlHoFTrNtm4dnlBCyeiYCGEE6uoPrtDWx9Co2QlkrpV3oJ8Xg6PNPHGW47vB5pJeNDgZ4pZzoXz4UuvVt3OBBVYAK9Lw10T3lSZlFlJ2vrYsnJArP34UFzyTPPLSmdT3JS5GkarJHJhpQIGKKtSzPEmLtCDajWzjKlDPE31b6k5p1WfEtYNQYwasXGQyNV94USd8DxjezumxZKJ5xFxdgvg6hxCpFgV2KIyZ3KFr4r9YE_aK3urSE2pO1cJ86L_04v8ZpP3SB3ZPu9_Dw8XtOPlcMT_RlEMICzKrEBoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|سران باشگاه منچستریونایتد به درخواست مایکل کریک سرمربی جوان خود با ارائه پیشنهادی 100 میلیون یورویی بدنبال جذب فرمین لوپز ستاره اسپانیایی باشگاه بارسلوناست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22497" target="_blank">📅 22:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22496">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKuZT08MogQ5Jo_e57mTqNirLQXOlFmut-3QbrH-LC-tYrVUi2IpLyrjSxEIFfLe1xqp7rlM2vZMOYo1enOuZ722qf-7nfPnrK02mKKadJZwXgy3VlLftVv2yDH5ZQ4sqtAe5cAy-mh9nSawDx5y8noZnSsijeaxMuiuEkSgcrnHmbC9Gd8YKYpKPtqADEUJvKNzCNCXdmy1J3wPWR0i08rThDv3sTf_mKnkNF6T3sblWZokvSySLJK3CmzYcXflMRt96fa6UjLCj64kh4vjpBVK5culkmcyGVWX0fGRo4vPA6G3FhQaY6toaf6dva9hiGGeiXYCtf_oLW7jUiX4Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22496" target="_blank">📅 21:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22495">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O96aoxv3S9af4fkRxQ0boK1gm1pA-t9gCTL18oiVnB22MbMYvPaYW8ZpuLge80kvsmNfWo1NG5D6fA2xWkSGKrtDEsrfvtNo_fzCbZrCopjRKZUMF4P5PivPEbv8RSDqtEUzZifjLsCD7T7k8zUi6KgZRTuIq20wp4mU0kP46dE2fef4WPF67pbW0P8Sibo9vElgrywAJTC_fRqiqUJz2j6ew5NtqBPWpuyslmuUgxXL5P0-s5PRkJvUCS0B_ameA011_UwBKcDFnP0k5XVkROEReD8hf3hBmjPabkyG-mVq3okO4jJTd30_dA7xumsGIEPIJGt0XaiXaPmvfu-TqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تنها 45 دقیقه تا قهرمانی تاریخی آرسنال میکل آرتتا درلیگ‌قهرمانان‌اروپا و کسب دومین جام ارزش مند و شیرین فصل؛ جای عارف خیلی خالیه.
💔
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22495" target="_blank">📅 21:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22494">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEx-2LLmFFd_btN2nkiwPEX375rOZy6yb-pAiuHVV1Bopm2X4nLrhwW-Z2I7QqJNcQlUOHI1qxt_osQ0GXF9fIgAD7zRaP-bqSaqHFQWKRUl0EHteEgh8RzK0nIF95Onlays6PrnXG2GRPzmWAPLUm8LhIEZAdZ0p-mIS61tF73glc_FA2rqNcHieE9V2I1wZiXGOW18sm7cvuFArEINNxM1yu_4ezNfYQo3XKs-vz-uFybfQdrqfVc8CDbgN9GV0HGlmIUfuR6rHXSNLZpGUZUYov2fULj_fHlvCjnsZprxabdzTXDPimbNiPNlWIE-W_-ZkbEpJCxcSTvZ1beb_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس پیشنهاد مالی بسیار بالایی رو بمدت‌سه‌فصل به آریا یوسفی داده و احتمال قبول‌کردن‌این‌آفر فوق العاده از سوی این بازیکن ملی‌پوش‌بسیارزیاد است. سالانه 80 میلیارد تومان پایه دستمزد + 20 میلیارد تومان آپشن.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/22494" target="_blank">📅 20:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22493">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYeq9LV6gEt_rNP8D93kora1aSvIgsPp6EfeyL32TQ7zNb1pzMQXGkVUHseOzoFKZBJrGxaBCko35tzBvKnJH9DVZA60ZViS0e3pPAxakh1COzs9hskCka_tYHn99st1GMCVR3YfONgIE-SSMWbdSgSGVf2_KQvSntNzDT2ZYwexY4FKBN_QZHHVA44i84Yc8PO_FLL2wAQ-LQlqNUm1pXVk1vEzJoJ3pKBPLWN8pc4OPXeIHDsWNBLNZX_StT0h7nMmDPtgA-ICpENGH9LwbhtKKyEpgCVjS5Y1OmZAYDVXlgkHwUK3G1f7mhKsr8BX-MnKggR3W9lTK81TX2mypQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
علاوه بر دریک؛ این‌مدل‌انگلیسی طرفدار آرسنال اعلام کرد روی قهرمانی‌این‌تیم درلیگ قهرمانان اروپا دربازی امشب با PSG پنج میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22493" target="_blank">📅 20:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22492">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a443979ea7.mp4?token=PqkzVdUQLOzczJ3OJkEl4x9xnZIOm6hGznyTv7e7qLg7YrJUsdExOPCV9vjlZZG72oTg7U-G-A1V467RaVH1hCSuSTSoubju5pI-uorxgu7l8czc0E7QZP_NYAn7zuBONpsO1iAXZfOaHOA21NpkxFmaC6lVMj3UX1a3xE0_6cJrkGx-0jvQL53Plc80UDclJcA_EVdSSVcGdsthtQSfxrZDiQE-o0VV44AKShWSBqGJCXSi9Gc_0X2kXVivQ9Y0fO8UmXJxbDhChZB4Z0OXb5xI3DMJoBH4_t37pVK6hFoXPGlQjvOPwTlFOLktIeZwcPiVx84SIm14jupr5rrqAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a443979ea7.mp4?token=PqkzVdUQLOzczJ3OJkEl4x9xnZIOm6hGznyTv7e7qLg7YrJUsdExOPCV9vjlZZG72oTg7U-G-A1V467RaVH1hCSuSTSoubju5pI-uorxgu7l8czc0E7QZP_NYAn7zuBONpsO1iAXZfOaHOA21NpkxFmaC6lVMj3UX1a3xE0_6cJrkGx-0jvQL53Plc80UDclJcA_EVdSSVcGdsthtQSfxrZDiQE-o0VV44AKShWSBqGJCXSi9Gc_0X2kXVivQ9Y0fO8UmXJxbDhChZB4Z0OXb5xI3DMJoBH4_t37pVK6hFoXPGlQjvOPwTlFOLktIeZwcPiVx84SIm14jupr5rrqAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دریک رپر معروف کانادایی یک میلیون دلار روی قهرمانی آرسنال تو چمپیونزلیگ شرط‌بندی کرده.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22492" target="_blank">📅 19:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22491">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHt6_Yt6meqrOf4-vGuq-zqiL32jUMI9hhom030SnZOJPEBnjRlGnzkXE5_pzlC6Ijv1F1_fwpo9e6VTjOdMKtRr-pU-AbEqKfr6x6rES4Rms7xWXbt3azwgQgzAMypi9LaRwDFjYKfthox0fxGso7LQkoi0DRNVPnHX4aRZiQ-srVk7YVjzQ45egIJFr5Js8kmUG2shNDmV4vbltGp9D9okffBU2EiHN6gksSo6eqEsiuJHAlufh_YX-9MhLXL6kUHDEKNEuy7K0gjhhdl0PuXcqZpusXgng7Br_0QJPVbwdMjfFkaGdklv1PaY9VMwESLTT6o8M8QX3c9_vAUmLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور در روزهای گذشته نیز خبر دادیم؛ آریا یوسفی و محمدامین حزباوی دوستاره جوان تیم سپاهان مدنظر اوسمار ویرا برزیلی قرار گرفته است. آریا یوسفی علاوه بر باشگاه پرسپولیس از یک باشگاه اماراتی اماراتی نیز آفر رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22491" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22490">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2qMaNCNnmD84eCODEZXhF2EK9G8nIOh5wdrxVwZXYWr_A4VYxvBMPewsJJIDP2SY4Scuy88MAmZ8cX0IjaqTANKnJmzpgWaHufv5V8boGh-0KV-M2q-od9z94XSYL7-cVbbvkh-xoqQOwGkShgc-SfpxvMY_Ta0kPwlkuvmnkbGw9JoYZNYArzxrNpILSEe5OUANYBKlS5CeA8pGtzCELvJKpSfpDRHKcUIZhLv4ypi6Csx2V2Vx7Bf2uvRi5huERKl3fQ5-LuTca_xOy0LjLfA3nmdTLzjM8Wl-x_O_TvFGnFtc3gS4YwAjHytrd05XgS2tj0DH_XPP1mD1Zve_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/22490" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22488">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSseGim6TJb0mxVKoYV-_oF61hJ4-bwX001vLwIl23n7H7_Lg7ZnyfQ3K_YeE3d5abLrT3mL2L3i3V8j9r8kA5NZexvt_6_ZWAzjNQ-1WkI9JhdqrPsNtoE-I_etyGD1_dXFb5giNwNtfxsMvTIQW3t2iMc1lKRLO8BEF3sXUecVCtqA8a9VGuQbFV18rNRaVWsiL-G6KZVdXzMAzIa5rwZUgit4Wa_-7FvKp0sOYruOh2N81UXbDVCHouQ2jwJdpzBlADPDFHf8WARAJxGR_MceULYRqvhnBrWFbyy96Jrty6F2yZ-E9RfcXQSL9u059gMIZ5fRTPwOA-AR_E6H_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور در روزهای گذشته نیز خبر دادیم؛ آریا یوسفی و محمدامین حزباوی دوستاره جوان تیم سپاهان مدنظر اوسمار ویرا برزیلی قرار گرفته است. آریا یوسفی علاوه بر باشگاه پرسپولیس از یک باشگاه اماراتی اماراتی نیز آفر رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22488" target="_blank">📅 18:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22486">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rXrVZLVd6SckaWlbiVOfXLdaiTPRrDHBRphkKN9qPRZV06BNMPEeslvksp8C0B1tYWvhwQzAM-IJdRvDb2bWwW-Nm6zzElNdK0dDU__t6rmnbQ0sRi_ME2PeNgZz59GgJev1gr-4OcwEW2F4VWGD_XCz8hlj57ZU375ajHoYXdVVY5D6hj1i9N9AC42LJyjbZq6mv9-O0zEoa_whOFAyWv-ujJpDocqXNz7vxieYGteHV9-hxWNBky77I3CRkMqZRmtuJ-UbHoYHJ0xZVri-nAaP2MSf6Eg8KjnVAgS150WqU1-z3S7So9eI5m0UpcN29XEluKjNo7GOi8NxEdSUfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bVHhuCLbZYJMPLtQfJBdp2y0b3cawfarSJIZJur33QG5laEJ9mySRBv9cEFAIdCJEaxm7E98GJTs088Cd6Gg1IAAvgxKJX4ETgVsJGrGFbvq6gCf0QM1kkAy63yNp1--7flhLH83ec-Ie7yblgI_iLCqI3lEgrYloLiMYsngVmFLHyzT-yDUxlx4ySb0mA0uLviHewdyl6f0DcTBwm1kpc0EjxwPVCq28h5s80VLIAhSr7axUrCveFXR3Zbun77qeaBvMpGWN4oXFdcuX_RE8tgqdYyucdciYrUe0gn2QdYUEiMcXJ0B1wDmk3m3Ii-fk1K-z2orQrNpnVdAlYhL_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
شماتیک‌‌ترکیب‌دوتیم‌پاریسن‌ژرمن و آرسنال؛ ساعت ۱۹:۳۰ با گزارش عادل‌فردوسی‌پور ببینید‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22486" target="_blank">📅 18:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22485">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THpMoDKupGmfHzlSs3CLF75gskQmV39smeN5O8Rb7mMwSIxYyntYl0rcfmN1IHX7hzFXQaHdxwGriPhKBJvf1qDwPGF6xuqvrf1DI5G6xnRzDln2JUQbiPWNBdVBGVTUF8z9SDcIL1__WaLTrUx7lV7-QhxVr1aOJSAQmEK25MnkqmCW98m1yGnfEWRiSOu2P8l51lUciBK88h2Dhg9yTHfIFixKkr35Stmo2-QqqHumWZRTi50nffa4gfNDmrLb4I-mIL4L3-77UBW0LaKR8KxusnmpoPYqNz9Q1eADhQ0CZG34c0CAcApEhT8GlfgWwflHeEDKAfURMRIes0VueA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکردفوق‌العاده‌داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان‌اروپا؛ رایا درصورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22485" target="_blank">📅 17:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22483">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiSoCaP63f-vwzPcxLgrKSEP-7Q8uDpRTEJshTvTAQZ4h_ZzFDj0H2Ilg3XEtsb__RiR_YFIzrBVHp8G8u7edPoTkQ4j9eNc06vdNmTBetfxiR9CSPdPi_MtbAbCKrIovCzbq0dL3SPfJ0VLE3qiMRDYGstqwlmGjT9sKQOaNSpkwqslemf602HxwJEFn-JUR4fjmAwSpAxacj2mhsKOyHp8JUvQB6MgIqIjy7OpNE3HBPcbjqOagBR4H9U0Lf4_B2ySbN2bb20eLrkLoxnJ_LjlKEzHyd_oZ6e4ZP2BZqBq_0NQzCS9Fh0AkFGFwVwgjEFlLEIX0wOeM2E9QB14YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22483" target="_blank">📅 17:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22482">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cU3I4Rr4kRZgvfMGIOeBuORCUp6095tMHHJoIiqHn8rt404FWkfw8Jq_pvGAWWqqw1xOrLBXms3M2EHB35wVZIRcoGUFPsQ-POb7EcuQfFPuorSHFzw_FAstcnAMxyyGRWFTj8EA3uFqi_QUeq8g4pM9F-U3vRI9iAcmRag_n0wdpWJA3yLuwypdQ30EPzVnG5fdab-9THMzU-A6zL_BeOj3QsCn_H_l3Zqebm05G8LWjGXWFRHY7hAaeCr3l6nPNmvwDEN516xgmztLi-19U1SizR2fNveoiwl6aL1oT_T6Vv_w_hyNsu5HrKxvoJGPvbpcLY_SWPqgW6rtPpcMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22482" target="_blank">📅 17:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22481">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aparat Sport [3.6.2].apk</div>
  <div class="tg-doc-extra">8.2 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/22481" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
#مهم
؛ رفقای گل این اپ آپارات اسپرته که تموم بازی های مهم روجلوتراز صداوسیما و با کیفیت فوق العاده و با گزارش فارسی پخش میکنههه. یه قسمتی هم داره میزنی رو صفحه میتونی هم زمان هم بازی رو ببینی هم تو تلگرام و اینستا آنلاین باشی. خودمم ساعت 8 نوبت دندون پزشکی دارم از طریق همین برنامه نگاه میکنم. عادل خان‌هم گزارشگر بازیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22481" target="_blank">📅 17:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22480">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmmBiRVpM3FB19W3Yi2AGxKCLp2cqjBVgqxayDDSYBe7w21MrAKScy4Crqt2j4njbA3TDkvBxzggouDaN5eepYbU_OFb2qHRndZDYG_W3lM2BTaR6ZrRJ4ihuP5Q0cKHAW4XFRqn_TFHRQl9raJPqcVHjo5vRZSoR_m1s_zl1Ua4HmwTK1NL6DZqizzAbkIPMI6fuG4CbLbWFyTAKu9BMkg1yZPHGK-TCdS1r2xU37go4Hbdsyu5JIx5Sr_Ynh3quAJInaFAcsCWoMiUhfbt1EzaA4uqIRN6onb5zT5U2YgOxCiZCB2jX2YYsXYZZfLH6jOm7MCYonInxyAUQsb-9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22480" target="_blank">📅 17:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22479">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf37364cd.mp4?token=hizADe3hjA8Pg7H3vw3NQH6VyxFVsDDgVMbSx9_RuGefJhsOvEqX-CdA-r4X1PR76ApaiPvz-ssBcV9ZiEf1ZRzBt6CwMjpYCSDvBJDH6TTiLLO13Dnt3xQz_YrAwfw46dsH8N5mYwHiSK2Z6GF6CWJibI23HhzImXvabKLnntAfOh1mv2AO6IhIN1xSoZLw5kU2n45e76JAwnIGiNL3SwRIS8jFy_o5GWQmqDiyGDhv-aGt7NW6pNV2IdPcFAjduzaHtSDQ5kW6rBCvvRCMGS-Oxo599KPnyy9Q4YyTRL8XsYzd5dVSWRLiGX9UjRoskAWxxasVKYP_n7pNI0TmBGK9APcSpHbxSxdA_2kWFSczVVzdFo6UAGghRAx-mTa5Tz8WJvkpEbHMckV62eBY8NccVtIW18dlwFOTySBfOdkofYW-sihxZylZ_sEePEBYPWxX6nq7ujVlVcCvlgCCh71-Z_2b9DKSncYME2CrCAShlU1S03jAgiJUsRUJ5nUHA0GVaF7DVjiYpEybx9WFEDoiEagiAsFfM17TLMS7lHo3PQcqKA3j2KCApCIcSVetOID7r_c33Ch68P0klpAXgGDo_3-vagTohrePRaCemcUbNXmYTBVnIpQ2eshz3WfJHRIKqZEw14e1m9amPQTz1YpgPrRxD3hWRne3GOtOEuU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf37364cd.mp4?token=hizADe3hjA8Pg7H3vw3NQH6VyxFVsDDgVMbSx9_RuGefJhsOvEqX-CdA-r4X1PR76ApaiPvz-ssBcV9ZiEf1ZRzBt6CwMjpYCSDvBJDH6TTiLLO13Dnt3xQz_YrAwfw46dsH8N5mYwHiSK2Z6GF6CWJibI23HhzImXvabKLnntAfOh1mv2AO6IhIN1xSoZLw5kU2n45e76JAwnIGiNL3SwRIS8jFy_o5GWQmqDiyGDhv-aGt7NW6pNV2IdPcFAjduzaHtSDQ5kW6rBCvvRCMGS-Oxo599KPnyy9Q4YyTRL8XsYzd5dVSWRLiGX9UjRoskAWxxasVKYP_n7pNI0TmBGK9APcSpHbxSxdA_2kWFSczVVzdFo6UAGghRAx-mTa5Tz8WJvkpEbHMckV62eBY8NccVtIW18dlwFOTySBfOdkofYW-sihxZylZ_sEePEBYPWxX6nq7ujVlVcCvlgCCh71-Z_2b9DKSncYME2CrCAShlU1S03jAgiJUsRUJ5nUHA0GVaF7DVjiYpEybx9WFEDoiEagiAsFfM17TLMS7lHo3PQcqKA3j2KCApCIcSVetOID7r_c33Ch68P0klpAXgGDo_3-vagTohrePRaCemcUbNXmYTBVnIpQ2eshz3WfJHRIKqZEw14e1m9amPQTz1YpgPrRxD3hWRne3GOtOEuU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این میم دیکتاتور داره هر روز سمی تر و سمی تر میشه؛ تاثیر کیلیان امباپه روی هم تیمی‌هاش
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22479" target="_blank">📅 16:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22477">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VD0XS_pJZ9XHsKVAHz6_t3HLp-KXw_VEHtDZ9mwjb9oyqOW7fZojyGXdcEcoydIsX_pGlauYttNKAYYY68K9fk8Bh_wU8wHroQrV0-xbi7kLVMqZWYd8yLQCitp-tQm77S0_kw8xv8lpaJDfGKMwyG9JBao5mGnhmb4a7o3skSC4sqgz1cOyjM6PQtueV4sab3E6Rn1e1aqnMWzHnZT_7x7ZUEhnMGOJnOO5Ke4CKjhT5n0NApXW6X1IhMECZAVyaRUKFjflmfhyVMl-UYfi7UElPyJJSe3l-4j5XtJ6qqb2WBcl42kXKIxkZGCsfP9b2sMiPxi2eez-IX6Ufb71vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/an3Ww5d6QFfTZDH9-_Xa_vMQsUTrS7zH7yQtEDqLAJhxBe90YX5sP4gON29E2ORlH04Hj-JT1Q0JMvpa5JMn84V2slWosWeol-V9jbaPBYDstPzP0rbrlqxEmH2_KzhE50eAaYz3xi947RLi6hFRW_1Aqi13a-VhjhCapBrbwxMNzns5pWnKIaB5AHxwWN_f3XqSFeeAw2RYE6K8VV07WxM43q14mI8f_A64I1apGDbUAOQIl-FqUSG2sxxUhrxW-UPLvEj2BQX5QAaS8KnkSA2hbEKwI_P7vo2HF8eW5Uf7ezjfe9hAC-8oRu-EBRGwhc9pvs9Mnh4olbtV5Vxttw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇺
مجری‌ و خبرنگار بازی حساس امشب دوتیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22477" target="_blank">📅 16:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22476">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsnFaurgnny4I3X8R0YX_Ix2VlY7nLGEp2t1aYNlxSNQZB6NQ-NYUaPEtJNW1lEtd8EEYSyTOvxAuUVk6f0gQjhLkdL6OUcQg5y9Dsdd7yHADqd7dzwFYz_ue6mhckUylEBdhTBhBIipcs0WImvWR-okFIw0I0GUhx5cAR1NcT0rW0E3PC8LfLaF4S5IIYDJOYO8jozjcPFT6k9XvVvEk7Z5zDJMApeVgpFNEDMwU2SR8EgZ-Ca6RqCKApctvijhV4769I0TSvrPEUSOgxuhLndz8s03X97ueeTB6fPyBJ7Y5U3ODoiNuHnSsSCPDFn0ROwT4dB2VcFzRLUpVevM2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22476" target="_blank">📅 16:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22475">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d18fefc27.mp4?token=DaZ_LJb0M8cYNeOFudwrx86ToVzPRzflJ0ZfhpdkSc3V7kWiT8nuuv1JPaFZqMfN0x9cU3CJJWHuNYV3vMxsnq38bsr7YrQrrWgJXah0curq91aWfvOEyxYXaHP37sTDPZLoTddk58ZTxtMU5Biy_VdNB69CNxfn9LrYxNNGU6Ca5qXUFugFqQbxYCmHE6yRA9R5q_bg8h6UlYYesKBH7y6U1zEvhejVjAx2bIsnwtlZNENiRMvAe32isC-tVIRar2Ibz7SSs1m3GhNUr0uoQ6zw_Vi6eCyS2I--t8I-RRIckmfMpE76qnNdZ0U-AHR4RVDzfXMl2f8C0WoMO5Ntng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d18fefc27.mp4?token=DaZ_LJb0M8cYNeOFudwrx86ToVzPRzflJ0ZfhpdkSc3V7kWiT8nuuv1JPaFZqMfN0x9cU3CJJWHuNYV3vMxsnq38bsr7YrQrrWgJXah0curq91aWfvOEyxYXaHP37sTDPZLoTddk58ZTxtMU5Biy_VdNB69CNxfn9LrYxNNGU6Ca5qXUFugFqQbxYCmHE6yRA9R5q_bg8h6UlYYesKBH7y6U1zEvhejVjAx2bIsnwtlZNENiRMvAe32isC-tVIRar2Ibz7SSs1m3GhNUr0uoQ6zw_Vi6eCyS2I--t8I-RRIckmfMpE76qnNdZ0U-AHR4RVDzfXMl2f8C0WoMO5Ntng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مورینیو در اولین بازیش روی نیمکت رئال مادرید وقتی دفاع کردن ترنت الکساندر آرنولد رو میبینه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22475" target="_blank">📅 16:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22474">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJ67aD0n1dtfYkIH4aSC1fwnfhXB0ShzROoGEm5N1ERVfGzumrqkDYeveH6jG3SmR1dNXEm0M8yV7_Pk8Ivq7K-9GLkcLjA_Y1g5nhPXU-f2-Gk_U314GM7Y9oX7zY2VRCu_n-645f3IkCoN-Skt07jREE5pCIEZXbzs8jgm5Lk2GAfpcC8-oClYR-bBOmMwaPKWV28-4y2GNH9HIs1GQ5rlPO6ingin09xzfUolBnhymBQcDHs_6T8yjjLC2gvid5PZ0zPEhSHDLdv22JdEXyPZQ--Cgs-2PQ0w4DQxkl8aoVzDvNsJH3447xkXssmqGNJUHcBqn2qkGU5ax4FX6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|ژابی‌آلونسو سرمربی جدید تیم‌چلسی خواستارجذب آردا گولر شده است هرچند رئال‌مادرید این بازیکن راغیرقابل فروش اعلام کرده مگر اینکه رقمی بسیار نجومی پرداخت شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22474" target="_blank">📅 16:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22473">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIYMOYSBW9_AxkPpi67Se1alobuoBDNFT3JdHhVl7MG7lXbT9xrd1rS_n7-Doy2JWzyrZGUpyAbbX8KfzcxlN_G0UxQjo2KpAjLZsanYSN5e0Lv-llAopEOfR-p05SCUDEY8UqBzjfcxQ_4X3B2vSx2lM6gmfCjY7nQCndOxKufFbuV3RgJytinZOb7ApkbprMmopu84t4Z3KKh1w0IBpmREa3qE1nGu05fcTdWpWKzT6KkGJkKTeTfByOL9woibsXw7ILZgykdza4g8zw4bPGb5WXvsTyfMajEwxGH5EDglZ8PDEX9OeaKHD6m59d4yPof8ha-YCY_P_eigVBkNqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکردفوق‌العاده‌داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان‌اروپا؛ رایا درصورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22473" target="_blank">📅 15:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22472">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-5sMwYWK5-DanTJqCbTLHfiWuuYR1PGiutia8VTtmF1naGrYfv8-dZFtf_FbM0HUDJ7jdUWmwYQ0KTaUPWmkxn7Tz5mTJiD8ZEa675Nzl-LOpixie0odR7Cf8oI4Iu6SimtDGHJsBfA7yliFfrBsLUGC6qi2n3ZEx913O75IKuLdvof1ZKiJjOOyjXaO-4uQQJM73JucwuKdzNB7julPdolAAvPITIuGWTJID7IRKodTV5pbLal7xD4oLUH3IGSm2idH_hxAsYH5XjZQ2ipxX8BxytT3vcnhwh6aMM2jdU4rliEGrpcyoHK1rygpA5Fetl4YhG4T6hfuFBOIsUqGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه بعدی اتلتیکو: هیر وی گو؛ برای پیشنهاد دوم به مشکل برخوردیم، بلیط کنسرت فردا تمام شده، بنابراین پیشنهاد قبلی را با ۶ بلیط برای کنسرت یکشنبه بهبود می‌دهیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22472" target="_blank">📅 15:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22471">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4KpKRK9GJrvs2fXRBlDZaWmnqgvY9R2rQfaVmwPlltEfh2bD4h42EVN1vVVn6ZIj1ReAYJ9AkwLLwvl0wNFXSXdfduBKiSeQGdB7WwyFYYTqdPRx-qHqsjmxQSoiFEwT55ukmB5XuMSCiOk0-4oYManLmdPW_f4EdgLMvJtVHvhdYencWArtZb9qmhyejXjPF6K1MHI0gSV8OgAO2bzwYUo4a475qYTDBl9e0RYbWkcZ3oG-MGmvranZMCTqtUItwvrWCzbGs3qYoac1OqI3hfxyxMQK8eUMmlIQRibgJ-oPqg4Rww7PjRNbqZWYy4WcM8lAa4P9H-ZNDVRL1sS1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سیدمهدی رحمتی سرمربی خیبر خرم آباد بعد از اختلاف با مالک این باشگاه از هدایت این تیم استعفا داد و به احتمال فراوان فراز کمالوند یکی از بهترین مربیان ایرانی‌هدایت‌خیبر رو برعهده خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22471" target="_blank">📅 15:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22470">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEf5UPeQCoH2dSMgPcvmS0Ry0j8cKYkJHiisIiDTM-THh_jqMcUbio-Dy5Vcb8vCZwcnGGgOguKcf1PB1OX2xAE6QU5rXcxQe1GrjTVUx5AVxJQfgemHxCE-wpEqKB_kFUaLEoFcfbcDdvuT-a2v0XYsBEd-08s7jrRg9N-mw058Uf8mkLIvNubNL2QyJW7wQWdcMFz1v1mBkUXz3Jvt_rNsUssbAl0HF4bhtwan66u0niWmL9jp8rg0lP43Lr4X0bJssFUzSHGuUeBKiFf3j1daavDeUJvMuZdCqM82t0Z8ufK5ejC4c-iU0gvjDgIaKBUcPPqdL-FnmeOqT5dZUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22470" target="_blank">📅 14:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22469">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6gWsZrxsvIBeeqgI2pQgVtKJnSV3kh3QpDt8N8RlH0NIlvKaB2fw9ChwZPtUr7e7YlRz1UA_SreTUUnqIIpED1V84odZnN5cGPYtlFeAO1TTH8F5ToFT5RA1b_hf2Zuttsbuc1mCZ328KYuVfUg315H9veyb0hwvC4Ch8gt89RoW_cL0TYtK-1EtKdF3XCf9BkyVxvvFyXj0wuz4utGItgkp3PySPTYuRt46joCkXhLUZ6tUyuZyOM_WPkAI1FCemq-SrLtiv7eG0XOm5QmH_jP2VZGDxRpmqDYbyULgZmpotMFLM_q1YSs3IHwq01_r7HE3U23cScdbJOkoOSbkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
#فکت
؛ کریم‌ بنزما یکی از بهترین مهاجمان یک دهه‌اخیر درکل دوران فوتبالی‌اش تنها یک دوره درجام‌ جهانی برای فرانسوی‌ها حضور داشته است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22469" target="_blank">📅 14:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22468">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nN3PcS4YvJke-dA9h8ygbLBNX9Qr_5SAy0c7OIqLnwfc9hgURqL1iVZwgxcETrwzhkp2xyS5nearvExKf-S-r3OsEp2d5XAjZwSpgpXva9jrITNC-SwZ_xiO8qzcVUsR7Bf_Lv5WNRr5aiygP0Fv4sKR1y6PE42xQu8a4NY4xjnL4n6x-R9JNHbs1zjHY2snhmp4EVFTHegbs1v5JGQP1QO_07WWQfZze0KcP5jRNjEJAumu5tFjYXT8nVVvmhYmkpZJUXsvn_pWTHBvTcZRgf3m9ePXt-mSH7gusSIVT88QfRS13Q6rJM1XW_EUtnjDEU6pN9fkYM6EmEsSdI4rtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇪🇸
پیش‌بینی ژاوی سرمربی‌سابق بارسا از نتیجه فینال امشب: PSG بانتیجه 3 بر 1 آرسنال رو میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22468" target="_blank">📅 14:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22467">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIwM2H82nxgPHAvIP5FtPy7sk4PJ8c7onUxB4T77PxamthvEMJksTy0pPj_kZHAbCdEtrj7gJOQ5DkUdlBrBfAWegYjXiVo4mFOoeqNfqDk8zbZIOu3mRYo4zknQclHKxG8v8gE0ThFXwBYmSlaMFa-EBb-t52I_JQY0wJMamJfA6_7goL6ade7GQNQsFU7_uBC_rfCBVqcTQDvHtZXHhAXd-xLRWXMEwq0p1EHhD2qOD2UNo9qe0O-pQmBKPVnivyfvMNdOZMzFNbOHWGYHizu8PTzangi2CawzRjy_Xhsbvlch_UkUgNu40oVFF5ehMW1bgu0DYyOY4KGCFuJ9tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باتوجه‌به‌‌مصدومیت‌های‌پیاپی در فصل قبل؛
احتمال‌اینکه امید عالیشاه درلیست مازاد اوسمار ویرا قرار بگیره و ازجمع سرخپوشان جداشه خیلی زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22467" target="_blank">📅 14:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22466">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjVElY0AsDs7Z5fB08ss1_DbMY5xHkEmu8yoYXi2Zb61GBG_GXcr4AxSztAfnNXzZqxmdUJX4Xhfnqc9MwgPEJ0p9vUrTZn3T0vGuyJ-CWjGdXUV3TFuEj6b3bf7qMg5FxxggjPONTvz99o6GixKT-yTPPmZA5MAqlHQYYl3sSI3tten2FdsEuUCWDxJ8x1_1W50Jb24Cryp476Mf7PphxWXukBZpgIVycmi__8iYtZvro496hJFSoZQaOi222UVKCCod1SQLdOcUXr0gzPExN8AsR8Xl3GMuzC_bm13qKnpVLuBHLyjxXkHavDjpk8ugPTopFrst4rDU-IHPxgRzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
ژول‌کونده مدافع میانی تیم بارسا با پلی استیشن یکش رفته اردوی تیم ملی فرانسه برای جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22466" target="_blank">📅 14:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22465">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_bHTLlqMoyCIupqYgwfuPiOcenns1FZhnPK6_QfWtJUu65msevVCDsYj24cQZYyhUKrFq_T0ES6t-OMlJe3L-aR7t5qSOh4dK1g13S_P3CKbfK6Z8sGqshPd9pvBSDytv6SJh5tHxgMtJraxMV0oWMVBxwmsRapXD9bNphOIuBnHRklYLItUDw45iq4EGwlD1LEXbFet8e6iOWoILXo5fdv5h6A1OrB6DFc_tRWPjKm7oBS5KnrZlIJzktluuyqz1tHayq87V0f9zQNmQAoVxX3TSMxU5lDT-e0X3STKJGHpgif8P_qoxvrndrnVjzP3pCnvdv_TAHQOGHr4EM9Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ علی رغم تلاش علی تاجرنیا برای گرفتن مجوز رسمی فعالیت فرهاد مجیدی در لیگ برتر؛ اسطوره باشگاه استقلال به مدیریت این تیم‌اعلام‌کرده علاقه ای به بازگشت به ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22465" target="_blank">📅 13:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22464">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrFXMTGX4bowt9fzEKfyRkRlQxp7fQ1B1zFRU64_Dw6xxX7ZAltWZBu3vzfd8ov7mcyhwvKSu9awHIhijE_AScwP9P0b4BUv_f_ZT7wnebhRN5ws237yBjaxqLlXlUp80vCgF8WdL4PEVFqkCUKzbY2kOPOx2fI_NxZyxJVPBYxhQABNA0eGgb8PnPXecRLBfdLsDqSW5tW_LeHGLodMNTf6MjipIdMrLlikL4beVsDQumbsBugYvGPpBMPeL7ubd3yuRhAmj60J99rouLDB5QXIbztYmuhRH05S4YGmuaRNYtosslt-Nq94KSNjKL6ufZcn101psHsrcjpeMyde6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ استن کرونکه مالک آرسنال در صورت قهرمانی این تیم تو چمپیونز لیگ قول داده به هر بازیکن آرسنال یه رولز-رویس فانتوم هدیه بده.
💰
این‌جایزه بین 530 تا 580 هزار دلار ارزش داره.
💵
ناصر خلافم قول داده درصورت قهرمانی پاریس به هر بازیکن این تیم یک میلیون پوند…</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22464" target="_blank">📅 13:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22463">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8PU9Ub1IkyCQPwdQE-i-wcO4LKuR6wivPmSwtEWcZPzEGZpJ0dzPQhuTU07nykJ1LK7eSSOWDTRCOV3BGDMnrwXMOiON5Ml2kJnZ5r-mXzt-sp1zrgWjtWNVVpSqrVEU1WMF-bJMn-bTrlBlEWO0WnDNzZPw2WqcMgpv6Bz_JCNSmTcNkMj7e6ZA2xLM-dGiBUYm8KcDaapPz8BuGImfIIy_bMvX2jYsD2TZ2K6POw6BFuXAzdzJghCb6SngGmq7TfHLIKwOh-1td9dB4y5hrZOFxq4KLrUJc-i9zpOzrFuMSfEoxOeMR3hr3_rGvdrqVttwR24oETP9YYytk2o6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ علی علیپور مهاجم 30 ساله پرسپولیس بزودی با حضور در ساختمان این باشگاه قرار داد خود را به مدت دو فصل تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22463" target="_blank">📅 13:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22462">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRFp7Z-nLx7EO7CDEV1hbDageuJT4GAgA2IHPXvQwpG0W1ax1HTYdfC8MKnYGugbwfqmdB-RHR-yhpby1qc7swCkV4nuYXa3E7rj3tAk3Uk8nCn5yIYhjEdXgTmmbV0Yxaux74tqOjtCNuPUgyYdMBUxGM4yrtTGSLjYsbPSz-KtNMRzzJM-5rcRxQ0fJIXHfEz91QAWu4YFrLe-HD8XUDwdsHR_t7rZ1ald8-_QJbXzDwpchivHdL2w51JNvcnVX6k2viWJ9l3USY70kWWlNrErsdzh5w7B3Y53wQ7Z9k1mUMEdWISZmSSjxAtmWG2jaDd6OWwFVKwAhr9RsTtRsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22462" target="_blank">📅 12:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22461">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKfqNDdHfwHm6xgy6ptfDskr5B_x2YTWtgdnx4UKepbk5R7KEkmf2P-J9PrPXfOcIUb1pfiLQ0Msc6xmfwG4HBFN-gIrS6eZzLke7e91EtnCAaPHwOnFwKjh_cgbsEk2HFn_yW2dr6fvuTzRRYam1pnzRpRyukpVLpVtbI4gmt6Qgf9f6lhRMm9Zy5dcU176N24NQH1l4Q5tbCcsffQOBk8zK4uuy1oe8kgFdY0BYBpJ80aMzTOeDns3cam-nyceCVaNyOkiiq9bq5Caum2oEETla_AyhSl4cJa75ig1mPkkSN64M5fciY5BKYf87-lZA7ItXm1Ee8vyWwRbT8886g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ رسانه‌‌های‌اماراتی: علی‌رغم علاقه شدید فرهادمجیدی‌به‌استقلال و هواداران این باشگاه اما اسطوره آبی‌ها به دلیل حکومت جمهوری اسلامی قید بازگشت‌به‌تیم‌رو زد. مجیدی زمانی به این تیم باز خواهدگشت که دیگراین‌حکومت وجود نداشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22461" target="_blank">📅 12:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22460">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atHFtqNyEwnmpFlW3869zMxwywQMOgiIadfD35y7fPQTZNj3wJNzydZS5HL3_badnv-T7R13abfbI78-rnbbf-KIwo5C3LzcdUtYh5eXEOn3KWowHkRiX9MChjTA2ROZX5wt8yeoWo0Soyk9WNb3l3RVB4tGcA4GVazmPjnNrK24KXCpLnKq8cKoIgsDhqsdzunzaRDQFJWacLdz_O1rwptLDliaqcYp10yJdh5UQiX09WBSjGuvLu1fLG3VTAZaENBhv215I5EabCz_lRqxab7sYdjBbt0ZxB6YkqceFD4VnZf8wAP3RvwBLy5K2Qcxh_LL4HTYM5lLPziHgvpPEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب کهکشانی و پرستاره بارسلونا هانسی فلیک در فصل‌اینده رقابت‌ها برای‌فتح UCL؛ به این ترکیب به احتمال فراوان برناردو سیلوا و کوکوریا مدافع چپ اسپانیایی باشگاه چلسی رو نیز اضافه کنید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22460" target="_blank">📅 12:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22459">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5359012d10.mp4?token=stbXFzlXEhokz6w9e-c5f54miP5KE0XD4G_F2ubNGwzls1CAKEdb6XR2MSWo_kSKRi1Xi_aYFU_suEoC2gqcuv2TNHiNpibktFHLV0kB90hRRx4y3515XcLUJv14iJFviADyGNXPiDZQy7z_bqg7INc5Az56KOeLpIj4f9d8acr5aijlTRL79YckFBZfy4owI-frM7CI4q2EK6Ieax_d9DZEUqqnvBBXpWLKRdX7dLWDoeze83ReWzJqisdOdlgy3TZOy9dfrAGQdxUtoB3iDJL9rN3ckmqs-Vl1nidUwPSwJZEQapbnS8vfLHGRg0PQtpP3LcTH_4iwGumumLAUJQS4KS3wfPQBAUHES9c3Fzlpz_y0tCJQl5tGMrwBIrhBZdgX6Ig75_nDGzurWhbWAebnMzkMkQVWMEz_jHBj5QkD5sLjoSZi9rqUFq9Pyf8z_LYVEcYuDJLAqHWV8DBdgwZ9tD2AsxSYhcJz2Dp-ofb7couO-or7TQDatOyrW_vyekdhDOaMOBhAykJY0aKUYteJ_kCsOrQD-98uut5Ig8eCE_8QUUXx3TYym6lLPOZClaLLsrzOPiL3b5oHMEbnosGX8rQzW3AhqQyyWE7JbvW-exaEeg5BrCoXEpCW32qDZUMmSoujjEgg5s8O_7W6r2U8d8kxw5k-lCkhRwFVdMM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5359012d10.mp4?token=stbXFzlXEhokz6w9e-c5f54miP5KE0XD4G_F2ubNGwzls1CAKEdb6XR2MSWo_kSKRi1Xi_aYFU_suEoC2gqcuv2TNHiNpibktFHLV0kB90hRRx4y3515XcLUJv14iJFviADyGNXPiDZQy7z_bqg7INc5Az56KOeLpIj4f9d8acr5aijlTRL79YckFBZfy4owI-frM7CI4q2EK6Ieax_d9DZEUqqnvBBXpWLKRdX7dLWDoeze83ReWzJqisdOdlgy3TZOy9dfrAGQdxUtoB3iDJL9rN3ckmqs-Vl1nidUwPSwJZEQapbnS8vfLHGRg0PQtpP3LcTH_4iwGumumLAUJQS4KS3wfPQBAUHES9c3Fzlpz_y0tCJQl5tGMrwBIrhBZdgX6Ig75_nDGzurWhbWAebnMzkMkQVWMEz_jHBj5QkD5sLjoSZi9rqUFq9Pyf8z_LYVEcYuDJLAqHWV8DBdgwZ9tD2AsxSYhcJz2Dp-ofb7couO-or7TQDatOyrW_vyekdhDOaMOBhAykJY0aKUYteJ_kCsOrQD-98uut5Ig8eCE_8QUUXx3TYym6lLPOZClaLLsrzOPiL3b5oHMEbnosGX8rQzW3AhqQyyWE7JbvW-exaEeg5BrCoXEpCW32qDZUMmSoujjEgg5s8O_7W6r2U8d8kxw5k-lCkhRwFVdMM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
پنج‌ موزیک رسمی‌جام‌جهانی دوره‌‌های اخیر؛ تنها دوازده روز تا شروع داغ رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22459" target="_blank">📅 11:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22458">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiqdIuqCk0GadP-7-J4inKd6wUdiNK12_QgzVpyOqybkbviRcElHhR2elmZvOp_VG7skiAwty-b2liOawiPDdp1WUVWclXRPB1Ttqwa3Pv0vJyuMG5BR8lfgRvo2GSxWUi_K4uuJBrs_KwH_IZH9U4dFNmx5mEorLlA4WntU2F6YzgSLISUMZt3OoBp7zibsv1_bPDvn5QE5MdN5g4p2QHvn45eNC3Z4qp-xAl6JHEIKM4hN2cAMS5LoTWm06AHm-aoCSa-mcRAs36MOGAwJaaXXX8SUTPbDNaQcouftj2rBXJV67bKQdYzO-SryumbNsFG8M2nDRxEqu4H1MKT5cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
مدیر برنامه‌های نیکو پاز: ما با باشگاه رئال مادرید بر سر تمام بندها به توافق کامل رسیده‌ایم و نیکو درپایان فصل‌جاری به این تیم بازخواهد گشت. منچسترسیتی، چلسی، اینترمیلان به دنبال جذب او بودند اما نیکو علاقه داشت به رئال مادرید برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22458" target="_blank">📅 10:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22457">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcJqEQxycYoRaM9znwyOKB7C0oVLlSkSPog7DDXInSrhc3EcZR4V0VzD1_Anaufg5qkViU93I1UV-I7J63omzOVMjqN7Z5PAczDbespS8w8cV52B9MmnjxOZ3owFrWDq8_WWtRt-9va_9dVzJfjtsVtI7_mTG3wdxu146vn92uyZwLjVtqhI9ErIhJehYU8IGspTUVobkb08N3rTOcXYkVj4a_JRLnDYMm_2eegJON5C4V_Hvqry_jQR5qrVkoSEMXgVAr2D0Si2dso3GjDL-Mckf2CkaZMgfe5-3EG9AnvxzW5xO8pQjEsiKUTPcew27HDSe7rYXXROFyjk-eKCRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
به‌مناسبت فینال امشب و حساس، مروری بر فهرست پرافتخارترین سرمربیان تاریخ لیگ‌قهرمانان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22457" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22456">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AG_LdBIVLmfgunWo_F2XF2X7hKrXd0UCqQD_zerkLBgceilQHnkG0BK4qDCnQ-40SVlYWtmK_-3Qnggy3rDxqYZ8ZRwp8nA8szcIefB0exN73RiJVSkzJ8oFDk5f7oniEBihieli5cJGlEIKtq6DXq9y7RyzXDpWvjN6vHdi4rOE1A_x1AX2ZPYqkaaeoiK_ewGvPa9rLQu0uYJxQ55Y8R3_SxISJ80CChJQ9hj926Wq6hR_Vu0UM6Ub0c5WCbelm_dNnyD84OJ8VYEJPfVo0oG6DO8hLtjwE0Y_x3mUQcVi2d7hSA5KbFBcEQcc3PtrT_qW5BoXuYadRDSxOxAJ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لوئیز انریکه‌سرمربی‌تیم PSG: میکل آرتتا گفته قطعا آرسنال قهرمان چمپیونزلیگ میشه؟ اینا همش حرفای هیجانیه امشب‌میبینیم کی قهرمان میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22456" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22454">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d629612bbf.mp4?token=kLJo0yjbm2RG-8WuGZJKyhfl1C4-5y7knnF0hhYapBbTAXUoJ0kYT1SLQfKPo5AxmXx4Ul2I_eOAaUNzKP4bLzCULRmsmDZ8EX6LLmiXJwxdOywgjgwY9kC2KAYxgiY3IEsgKvaEGRKJ5ltymFMAYW1Cn1mKfzCXDMOy9_KluW0_NdpeADaEBgSZtDtNEni1n0ATWC3YkJCuaSsdf0ObqYLFGEjmUZFwfr4jAoE7kNgxWx3dm8GfQWASUBce8xCobz_yUvdvkUGSbHb54vipDLLDLhFgs7Y1pmFZP1GDwXcADQZP_noCZuDzj6zM_0NCvyn6yVprCkbFYZ1FUwy7Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d629612bbf.mp4?token=kLJo0yjbm2RG-8WuGZJKyhfl1C4-5y7knnF0hhYapBbTAXUoJ0kYT1SLQfKPo5AxmXx4Ul2I_eOAaUNzKP4bLzCULRmsmDZ8EX6LLmiXJwxdOywgjgwY9kC2KAYxgiY3IEsgKvaEGRKJ5ltymFMAYW1Cn1mKfzCXDMOy9_KluW0_NdpeADaEBgSZtDtNEni1n0ATWC3YkJCuaSsdf0ObqYLFGEjmUZFwfr4jAoE7kNgxWx3dm8GfQWASUBce8xCobz_yUvdvkUGSbHb54vipDLLDLhFgs7Y1pmFZP1GDwXcADQZP_noCZuDzj6zM_0NCvyn6yVprCkbFYZ1FUwy7Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پدری به‌همراه فران تورس و دوست‌دخترش رفتن شهربازی، اونوقت پدری نشسته کنار فران؛ فقط قیافه پدری که متوجه‌شد شب‌قراره تو پارک بخوابه
😂
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22454" target="_blank">📅 09:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22453">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c867b80a08.mp4?token=R7zKmr3QKS4tMhzjhzMCkQK5BAb-9O0FiznKzlaS1v44F3dex97_TjbjiJIVPF4rZr9rNC_UnUksY16TFfaYGMaU5hXCrm-9L5yaAs4TraDJ_sjrVyTYzeBX2I8qk3vlMxedDYwsoDbawTXXrbI7WYisMvQafYNxWJ0KLvh8ipn0ld0PkfI33CkG1FMl5Ln5eikEOuoCFYdglGzDx8z-2gZCjUBvy1akTVxh6Bw5WHjLQbTDLv4tTXdOUpWwfG4FjcsQGLfm6u5cCSILLkRHtIGiTnGofd4Cne991Or07lCPZL2iP8b-Y0eaT1SmgBnG0WIdE3ikt7QytZHSqmKbebGJNnkmZeIjkOygVnQs3DtqOIunZwd9cCXV3tg1GriM6fBb5l8pPHwxDwyiFPxXLBO_lS86493tCgpaZT_AC0Q8-0V4LgKIFLIUcOKAwlBMvG5oii3AlivcttLxsEC6h-2ZU42Wet0ZSAy8OPMzVzoQ-5Bbz0f-KplRXRZ87kchwvGYanqN62l-22ZGh3l498Rfe-_D-ewAncxOly34BTyT6N2QhFRVwstoY2mBK-XCpKqtsPXwrKmMC9_4_mFaOrO6IHfbfYSrnareBMJjB6RpFolQa1unvyY8TqgFQpMbCOLXIrML4qIeaj6-fTjEs5twjASygCb0gVyAQjCJ1mo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c867b80a08.mp4?token=R7zKmr3QKS4tMhzjhzMCkQK5BAb-9O0FiznKzlaS1v44F3dex97_TjbjiJIVPF4rZr9rNC_UnUksY16TFfaYGMaU5hXCrm-9L5yaAs4TraDJ_sjrVyTYzeBX2I8qk3vlMxedDYwsoDbawTXXrbI7WYisMvQafYNxWJ0KLvh8ipn0ld0PkfI33CkG1FMl5Ln5eikEOuoCFYdglGzDx8z-2gZCjUBvy1akTVxh6Bw5WHjLQbTDLv4tTXdOUpWwfG4FjcsQGLfm6u5cCSILLkRHtIGiTnGofd4Cne991Or07lCPZL2iP8b-Y0eaT1SmgBnG0WIdE3ikt7QytZHSqmKbebGJNnkmZeIjkOygVnQs3DtqOIunZwd9cCXV3tg1GriM6fBb5l8pPHwxDwyiFPxXLBO_lS86493tCgpaZT_AC0Q8-0V4LgKIFLIUcOKAwlBMvG5oii3AlivcttLxsEC6h-2ZU42Wet0ZSAy8OPMzVzoQ-5Bbz0f-KplRXRZ87kchwvGYanqN62l-22ZGh3l498Rfe-_D-ewAncxOly34BTyT6N2QhFRVwstoY2mBK-XCpKqtsPXwrKmMC9_4_mFaOrO6IHfbfYSrnareBMJjB6RpFolQa1unvyY8TqgFQpMbCOLXIrML4qIeaj6-fTjEs5twjASygCb0gVyAQjCJ1mo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
موشک‌های‌گرانیت‌ژاکا بازیکن ۳۳ ساله سوئیسی سابق باشگاه‌های بایر لورکوزن و توپچی‌های لندن.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22453" target="_blank">📅 09:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22452">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/928b5d2877.mp4?token=ENA842HUOiG7PaCJFKsCOfRzCP6Ep9Jdr_Kg_xDvkrpS8lraSWNKewDh4UNwIrJ0B2BYRmd5HdrIBqratHtQLMWLaYRXJWsGP4nIaO-PLaSstlLoyXyMrqBUdfG80U2-looPCBLulrkVBb05L9S9gfog0fHqcGopQt8XOOmSH0qTc5ktbS5s5QkgdJGVfwHqiHI4J5TyQLaVJkzqP4lmOMjIIShCoAmUIBbTtSQZJotdIAfWonPdO0UYGhe_ma95_kGiwPZT_e2G-Z4kiZ2Hpj9ULLAvoA3684jgJmPh18dO_Ef3JoL5k0I9XY4Mm2JLSN-JluHlXHOh8Sv4Ga3jFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/928b5d2877.mp4?token=ENA842HUOiG7PaCJFKsCOfRzCP6Ep9Jdr_Kg_xDvkrpS8lraSWNKewDh4UNwIrJ0B2BYRmd5HdrIBqratHtQLMWLaYRXJWsGP4nIaO-PLaSstlLoyXyMrqBUdfG80U2-looPCBLulrkVBb05L9S9gfog0fHqcGopQt8XOOmSH0qTc5ktbS5s5QkgdJGVfwHqiHI4J5TyQLaVJkzqP4lmOMjIIShCoAmUIBbTtSQZJotdIAfWonPdO0UYGhe_ma95_kGiwPZT_e2G-Z4kiZ2Hpj9ULLAvoA3684jgJmPh18dO_Ef3JoL5k0I9XY4Mm2JLSN-JluHlXHOh8Sv4Ga3jFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لوئیز انریکه‌سرمربی‌تیم PSG
: میکل آرتتا گفته قطعا آرسنال قهرمان چمپیونزلیگ میشه؟ اینا همش حرفای هیجانیه امشب‌میبینیم کی قهرمان میشه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22452" target="_blank">📅 09:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22451">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb17964484.mp4?token=cV0m-Es008FWeMR6kjexNEg7wDcduUEeH-a90mdHVsEThEpVbIJkxv5BQSi-fZD0O8rcv8oltQRaeiarTeBb5qegxwQyxpvtndei0nNu5Zytfl92WzIBIjx9fg0k8AGAvDghAbYvLfW5lZqEJ_x07pgScpnJuvktZLJk_mTFFMty5GB7EhN4R0lG7eHTHJ53lgZh2QYrX3J_LSn5GnHDR6SemKHtywXrXR7BqSKoUgCIVVwUQlsYzI1qpDWh2xQZvBOdEspqFdZ4MYT9NoKh7lShcGte_EL6R6ZM2Kq7MLGmC71AYDbWxMXrDkonzjSvMdFIBdCgRCI4HNMYSg0biQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb17964484.mp4?token=cV0m-Es008FWeMR6kjexNEg7wDcduUEeH-a90mdHVsEThEpVbIJkxv5BQSi-fZD0O8rcv8oltQRaeiarTeBb5qegxwQyxpvtndei0nNu5Zytfl92WzIBIjx9fg0k8AGAvDghAbYvLfW5lZqEJ_x07pgScpnJuvktZLJk_mTFFMty5GB7EhN4R0lG7eHTHJ53lgZh2QYrX3J_LSn5GnHDR6SemKHtywXrXR7BqSKoUgCIVVwUQlsYzI1qpDWh2xQZvBOdEspqFdZ4MYT9NoKh7lShcGte_EL6R6ZM2Kq7MLGmC71AYDbWxMXrDkonzjSvMdFIBdCgRCI4HNMYSg0biQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
وضعیت خوان لاپورتا مدیرعامل باشگاه بارسلونا در روزهای اخیر بعد از پیدا کردن نفت زیر نیوکمپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22451" target="_blank">📅 09:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22450">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pda9VJ-AXSLx5s6m1LC-p9NjBlDlCvVutPoeps3aiBSvup9kBhYQBwKP21FaIBeT_MillXOrtc2vF59tAnLiQTgcreyjQ3bfZsCzezxQLGctF6qWV9WmwSJSxgm1xP6lJmKTCw69FKbjfsd6MMLoptjnFe9nZIrg8Sec0jxXWyXVcSoD8wr-kPX6lLW7O9wbgDaWL8yoQiJh_i2tGQH3Q3wniIEyzSAKbzscgEiWg7vHRtRL_-6FRn_P69tdiDygYADO1fpb0VELmqvyZiOMGDc785tWxLHwrMnZrc0u8f4X3AHSDm7Z3Vc8GoyroTzEXqNNRI7PNHi2-EfhHZejNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22450" target="_blank">📅 01:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22448">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2XYm0gunWg6b6UwARKSTa_184e8tGgmOV-WRfzaTq8KZtTFU21X_zJaNXTLtUg3juab6ICUPMRwcv7EWgXgB9BHAfkah4VZmsfi08KdZVwXMzVPN6RE4T1dRACvcsfBM279gR1OWndf1KK8900eJglY2Z23KApfe_Pb84A1dGKIXhReGesywbzXpL659puC2cOrQhf4mfDJmGOzdKYgZrchz3HLe1foGzezDudfI77Zu3LA4CRQUt6RNTS2Yye6KjuhfLcDzBDyqM4k1pOFZpfzKWVQjM3R6s3ctB6V23qmsjedVgTTkgnPmcDiSg8whhw9YfD6tUAogbvRK0D0aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه تنها بازی مهم امروز؛
پایان فصل باشگاهی 2025/26 با فینال حساس لیگ قهرمانان اروپا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22448" target="_blank">📅 01:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22447">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBDMLUEH27ksuhMdO9_og7aJ50fDfefvgjEdbECN96eLQvc8zTgmyTrJKaPfQujtG6rGgAblbSIrZkrpcge2zOYQDFRSgXLpjLuRjuz09m4UU5ufMtnki7Pf8_cr0sbVv1_R7RXnnILPSWorDmigqdsGlbi8FZgUY-Mg1Snp6tgkilAs80g93xcUSz5qOwYMFIdVjKcY5RjZmntQg7lK_vin_cyO4w4gA3X40KvuA6rjklqzN2maB-hCMmhqLNQIOjT6i4CP-00SIpEp-t5oqowrdIZbQoWhjfFesm7YSj-KcLY_v7IZO--4_TCftXzT-fDDsjZaKmzCerRuLlwesg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل دیدارهای دیروز؛
برد تیم‌های آسیایی در فاصله کمتر از دو هفته مانده به جام جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22447" target="_blank">📅 01:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22446">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ue8hxuh3B9FzhEcKjXpj1YIKb0iuny6D2b-PGamZnviub84CUntx8E1kuAoWdYeAOZGzeuB3DMqRg0C-ypTfjMQbF-FCermzHclMuF9EoPb8DcJq2PEg3dyK7hhV_PX9a8ulN_j0ra7M-IaN8XZe2mpbAPzD8bM2wO1MegWSb22FXNnH8OMHbOsEZ7QvksajleTBo3hitAPYXWV0TvpaVvQq8YSxKFilBfoI85629KepRHk-YV3HnS9GLLwJcPqiP4EB3kumaGDKJzkSPwnM4Y5GaBUQe_NyBxrDJ4bv1BElM7aoCVSqZ46AwiAP_Tq2XZpYzpVoxwAECuOIsIVrvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فواید پیاده روی رو ببینید؛
گشاد بازی رو کنار بزارید؛ فقط یه‌ساعت پیاده روی عادی میتونه بیشتر ازاون چیزیکه فکرش رو میکنی بدنت رو تغییر بده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22446" target="_blank">📅 01:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22445">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEM958fL9Lq-LfWs4wAn_Wvd46r_oz2hUUOvAoFhRr9xNrfBZvVhgWERtWBvqSFnlGmn4uGdaEtpQMoTva55_Xo-yHvu6Bgwz1EWiuP4MOOEY0_kp1L_CXfayfaKyNn4iDAMhZ3T4836aGRn3Fw-kSeOnCJh0mfJVfueG_01tcuK3Y7s9e0C4cAqA4UI7d0aNrtw_QOouxE599ErIWIZPNIOxB8pSCwrCpHAShCTPUbDi7c807wc6VorCTw28Gl4zDPWLpe2chZTTKi4T-M3jlbRoooXZQScUqIHdATANHehKZEwsPI5vSRmcnxUAt47cIluTHc8JdbV5hyy8ujEaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بازی‌فوق‌العاده‌حساس‌وتماشایی فرداشب آرسنال - پاری‌سن ژرمن رو در آپارات اسپرت ببینید. عادل خان هم بازی رو گزارش میکنه. از صداوسیما هم یکی دو دیقه جلو تره. کلا سعی کنید هیچی از این سازمان مزخرف نبینید. لینکشو فرداشب براتون میزارم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22445" target="_blank">📅 01:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22443">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YULn02M-QetsmLolq0JMG7eskvJ50cl3zdCuKlGswpcaj2POOjEuZHiWyFDD3XX0agLC2uMu0I1gTVH69vf3Ny6lSqwPnRPb4OckdevJFQwzfj0KFnsSVzQyPcGBueMqGcM87UWVhHvVpIddBXejVuQyeVZcN4L6BYdMU4q4UdxVJPtUiu3dFQ79YCKo0ARBJoD-iWlKB1QS_xzc27KoCtoC78pnlXDTxcSrXZx6aWmc5F-keGepLvRvRGUDdBM4C0Tx8v95hvBzqQYz5VB2GX0iO5K7mx5c0WmDoGJMf1ud0Z_JmKql4OxfdEEHxsnRDRKBQpeQmx8V-BqSCbIXLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو: آنتونیو رودیگر مدافع میانی رئال مادرید قرار داد خود را یک‌فصل دیگر با این تیم تمدید کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22443" target="_blank">📅 00:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22441">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGHT_faWkLYpTeUizI5fisKR3N7A5YrUPFEpDuZ5qx4LNzZv8rRUGStellaIZovqs_-ARnIZnWB5YX2W6BJqdO_4kAdtYuYxUKJdkRrmh_nru1JyrIcv5_zloYejleiz9ZjwxFIqXC89lWiwGN5zJYMi0YJCD_gClhX4M5nU5LJsXoYDVSmGk0BWykFMurOv_I3rqHSOeFUbTp_FLechWPranpTBw4qTNVzk6Tk21_2F9cz7obYm-mUrAlltUPcJ7knZ2_Ff-NVimSidT4_uUsV4OxI8a2qfr-KiFpjP3lmUc_F7RGozVez8Rrn3Y62j0bDSV8aJQRWe3BL1FB9Y6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FS1B9Si-gCsTYk_JykOyzq5JtUw7viziMZ1-7XPKtTq0UC-iJo-uvVsjhWziLpQPceWg2TR4O5t07Kg9xQqVkQcof9k45m_ZetQ_aiHuKvmCKSTmgYnoeDcr1w4eV-ZdrnQslHEOw_K8iFgaC3QL8jbshDwZMHlEQJIxBNrf0AAbirWtgBjG7lVoIwigzlNvqVgUVIDGCoUusAzlxePDkHKB3F0CnJJuDhnVArpseq6qmCeohtfmgl0fqKK6IunTOHOBqM0zrF4pTrN4npC2R7U5QXDUXw740o0FgXfe4M0Pm6lZ2M0phA7YyEcKyYrBXCyfBmc9OX6Yjctm5rM7Lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
هایلایتی‌از عملکرداستثنایی آنتونی گوردون فوق ستاره جدید بارسلونا در فصل گذشته رقابت ها.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22441" target="_blank">📅 00:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22440">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWSaIK-x6vc9-IhS2iDrSYzUvmNvxoIAng3g22abf73W46oj2L_7V0B2WQsW591UsB4RFVvUt0CGqI3h7PghKOkZUA_VX3vdw7T6CwjOqKV_lI-FRFyRiv6Rnq_g95shY3neg2oZXc4ekky9uam2-psCy7fc6xWZJi9CQbtwulKyaNUbDaRwww4SZnWR6N_OB7YS5iOJH2IOOAAlGexrDrvcJeVsxI56QqG_1Hq0WWpUdWeU6DsI901Mk-WnIlJqMFOcwZr_AZESSzu75qxzs_-XSroJXhTRHrptu43cSIjazpdZ-a9-S8J6gqkiOoC4g0_nH5pdTIsWYHwoMr_cdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ریکاردو ساپینتو سرمربی‌سابق‌استقلال‌که در روز های اخیر با عقد قراردادی به پافوس قبرس پیوست با این باشگاه قهرمان‌جام‌حدفی شد. از معروف ترین بازیکنان این تیم میتوان به داوید لوئیز مدافع سابق چلسی و آرسنال با اون موهای خوشکلش یاد کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22440" target="_blank">📅 00:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22439">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DllBS1SS-Mp89-faZWQvGKMtPmO9rzHMZER6c7dnaBGZ4z8v509Mdv4XtNdNtzpLQ-Wsv1pFQSGUhBF1SVrVJqHAjGpFT6Y8ZQXGu3wFWoj47ocxXsokNP0wG7rT3ZZ5j8MCF1dPWlgov3qNHue3yoJHvLVYxpk0h4_ohPLdYxe55XhQYVkYSU1bxMmxVmhWyr2TsBO-eJ_-3ZUQfAtLL6BjCTmZeUKAWkS4uOZNrCgVNrEyMN_kRh-tvcYhLX0d0rAt6xJhNNsz2W3SeoDSOF7bt-fLeLG7ulK3pjntgjX4cOOcF4-v0kfHUfFP4W7fm5uTR5vOdkUVCX9y5-p40Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کدبیس سه‌شبکه‌جذاب ماهواره‌ یاهست که بعد بالااومدن نیاز به‌واردکردن‌کدبیس دارند. اولش دکمه F1 میزنید بعدپشت‌بندش‌سه تا 3 بعدش یه صفحه میاد که باید کدبیس رو وارد کنی:  کدبیس شبکه جام جهانی HD:  BISS:2585AB552585CD77  کدبیس شبکه ورزش تاجیک HD: BISS:03A01BBE20C16D4E…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22439" target="_blank">📅 21:24 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22438">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYwi89wDP0XLiuI89mFqqBSPJy4tKsdQUEuDdYcnOx49Yj_n0iSV1b146IbAn4RjtVRKAOORGbFgwKpAafakpFQ76PayWORw8avCa_vhmYMyund7bEdncx7Y35wE90Y_K1lDLAh7ryIV2uDWCdn5iOawRRybKDn0xjPlBaLDfLMFhMcfhaym1wslI4-tOEPSPPGejM30HxY6aVfI-yY7AQ9AqBOoZ_VT7WNHcEoS64M9PDRc-66M09ZT4s6w55qI8rzQstk8JlTOS40dgB2NLgYKGkMYNQMWmT1SArJB7bxwQqZqG0CE9rqt5H8RrM3AhnbQdPJ-3w5eXdArOlP7XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛ ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22438" target="_blank">📅 21:19 · 08 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
