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
<img src="https://cdn4.telesco.pe/file/uY-NJy5aX6_IqawzALUZWRvW8UT_wjYfLj7vF5MtjvImJiXn9QHV1oBolL-j9sGN9TMfeQabH6eUjCUHpfCKA72Avr7eY-V_etHhNwCtn2787CMAzlOo7ltq8Wss_26SnJFXjJJkV_Jk-L1_mD5KOE9jDvWSYxBhtahc15vcW5zwjlIoIQpMdxvog04vRRgQLPuzsk0SKc1tHB-Q-zdjYndrhQR8kBnTwQ_eYlEFF2nE1nywKPpf7wRaWim3sQEYx9cP0Lp0lYYtCHCA__KNi9C2BCV9WzLVJqy70X3RNPKRIw3jk2l8pmQ7XZ8nQkdcNiAlUXDa8ptNF171hM8BDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 977K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 23:20:10</div>
<hr>

<div class="tg-post" id="msg-138546">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/104ed50ea0.mp4?token=G4n_Xs7XdM9d1i_-z2ZaGY2tw7xuUzkB3D0Le-uY9hBut5XQFwQMi4ee1NYRGBC2keDnVOWCKjTucpPf6hF7sZoKEFoCzIy9n16RLb0lGpDjmXK4yH49i6fPOw1cqpYJqxO_u3Z16hO6ljIFsfcpLA6tavTOki5K33_afiMVmHAP-8zNSiywd4wk_olqvTsPWrioBc7AK-rD9dJ1vB4QeeIca3-N_bQSikdy-EAmGIFqmummvIC4ZpfZ52XhakARSaIuaS8EhXiZvcesAY_h9R27j4H3GDCoKp3HHklFeBt4u8NEL9qgsHycwwDqEQxxBu0A_CXsJC7QLIuvNxmIjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/104ed50ea0.mp4?token=G4n_Xs7XdM9d1i_-z2ZaGY2tw7xuUzkB3D0Le-uY9hBut5XQFwQMi4ee1NYRGBC2keDnVOWCKjTucpPf6hF7sZoKEFoCzIy9n16RLb0lGpDjmXK4yH49i6fPOw1cqpYJqxO_u3Z16hO6ljIFsfcpLA6tavTOki5K33_afiMVmHAP-8zNSiywd4wk_olqvTsPWrioBc7AK-rD9dJ1vB4QeeIca3-N_bQSikdy-EAmGIFqmummvIC4ZpfZ52XhakARSaIuaS8EhXiZvcesAY_h9R27j4H3GDCoKp3HHklFeBt4u8NEL9qgsHycwwDqEQxxBu0A_CXsJC7QLIuvNxmIjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: شی به شما گفته بود که چین هیچ سلاحی به ایران نخواهد داد یا نخواهد فروخت. اما گزارش جدیدی می‌گوید ایران قرار است ۴۰۰ پرتابگر راکتی از چین دریافت کند.
🔴
ترامپ: اگر چنین باشد، برایم تعجب‌آور خواهد بود. او به من گفته بود که در این موضوع مشارکت نخواهد کرد.
🔴
او می‌داند که اگر این اتفاق بیفتد، من به‌شدت ناامید خواهم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/alonews/138546" target="_blank">📅 23:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138545">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56586855d6.mp4?token=Z0dJBogQ1tp3xNeeAF6A9RqVitSUzUJD9frSEV_f7kE385_zFf6EK_PwaK7rSXLfwNb703IVE8MEG6mlfRx4_4mjEC5-3ma9kkQkHGLMj-P6neSjhEmk1UI5biNdybGCZNLhoCEK0f2WFrWsTxBQpNl19pZGFtHfyFUJuOKzcYWF3K-lSSbjgtQsdR2qk1m5zBZefEgesKD7c9pTa6N7Sh3N6EYH7o2_y7oVIEN97bTzXlQiQfyuOv4OtXAPj4ND588hjiX0gvY3X-yPE0uXaPO7W_J6t_iSRXy4YMKoXdOArvQv6MklDdYgf3-jhmobaxYl5I2ajb0t5O0Jtfuq1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56586855d6.mp4?token=Z0dJBogQ1tp3xNeeAF6A9RqVitSUzUJD9frSEV_f7kE385_zFf6EK_PwaK7rSXLfwNb703IVE8MEG6mlfRx4_4mjEC5-3ma9kkQkHGLMj-P6neSjhEmk1UI5biNdybGCZNLhoCEK0f2WFrWsTxBQpNl19pZGFtHfyFUJuOKzcYWF3K-lSSbjgtQsdR2qk1m5zBZefEgesKD7c9pTa6N7Sh3N6EYH7o2_y7oVIEN97bTzXlQiQfyuOv4OtXAPj4ND588hjiX0gvY3X-yPE0uXaPO7W_J6t_iSRXy4YMKoXdOArvQv6MklDdYgf3-jhmobaxYl5I2ajb0t5O0Jtfuq1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من مایلم تعرفه‌هایی علیه ایران اعمال شود.
🔴
لیندسی این را می‌خواست
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/alonews/138545" target="_blank">📅 23:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138544">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3813e2cc66.mp4?token=YKayfAWES3MIbeFwUaRVzyrhOFtcr1i8Lw4V9d-qSsmVnczve_LXFtlMymEKIg6BBPpYj9Gg74diTk77pmQ-E_dijpWPKjOgl7Lk47oeNG5lkVUltCHk7S59dUR5RLVwzaT3SOYsECQVGhmtWIE_7Fvdun_dCHJRpAOrOh1UeOu1FKTVni1cHVnaMt-dQ2qwBQQcGNf44QYwyB3KuvmPFwX2eMiCXowWT5iK3uONZz_mmFKt9k7f1Y8Tzohmmp5qkMZVt18Kf5qtbzd0AcwZ8PcQuUoe9P0PESwB7nQM7zuqu-h3F1On3HXRHY0ASwrlolyoxRCquZIfur5MVt03mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3813e2cc66.mp4?token=YKayfAWES3MIbeFwUaRVzyrhOFtcr1i8Lw4V9d-qSsmVnczve_LXFtlMymEKIg6BBPpYj9Gg74diTk77pmQ-E_dijpWPKjOgl7Lk47oeNG5lkVUltCHk7S59dUR5RLVwzaT3SOYsECQVGhmtWIE_7Fvdun_dCHJRpAOrOh1UeOu1FKTVni1cHVnaMt-dQ2qwBQQcGNf44QYwyB3KuvmPFwX2eMiCXowWT5iK3uONZz_mmFKt9k7f1Y8Tzohmmp5qkMZVt18Kf5qtbzd0AcwZ8PcQuUoe9P0PESwB7nQM7zuqu-h3F1On3HXRHY0ASwrlolyoxRCquZIfur5MVt03mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: این گروه با گروهی که ما با آن سر و کار داریم متفاوت بود.
🔴
آنها قبلاً عذرخواهی کرده‌اند، اما، می‌دانید، ما باید کمی آنها را تنبیه کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/138544" target="_blank">📅 23:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138543">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86d931d8c3.mp4?token=bizowNkfn_xFr4qXHguRTSlhvzVikConYYTBoRfRFoihRIPyZiKl_av8A0AEjDxr9-5OEChUfrzzuHKWuYC0t5DjMIviSh9h6FzGpdzAgK6NFI9g4tkJ6797Sz5n5XH1u8j_HJYO8RI-s9pfWAwm9Ri-Hxub-rMYpxVKWtdTH4wj_6jX_FXqYBMfsnLhnChLrKoxOhkFWpfFa5XdYAS1bbdAqzn5C90804fOl2uq2AHDlvqaqt7s2ltyoQ46wIkqcAb8q1Zs_4_EkiAphl4qoUNE_otHkgx-B7ozLAmNzPycO1anvXxfZkSu3kP2sadFUoNN2Di0ouD8yLPKBDY0Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86d931d8c3.mp4?token=bizowNkfn_xFr4qXHguRTSlhvzVikConYYTBoRfRFoihRIPyZiKl_av8A0AEjDxr9-5OEChUfrzzuHKWuYC0t5DjMIviSh9h6FzGpdzAgK6NFI9g4tkJ6797Sz5n5XH1u8j_HJYO8RI-s9pfWAwm9Ri-Hxub-rMYpxVKWtdTH4wj_6jX_FXqYBMfsnLhnChLrKoxOhkFWpfFa5XdYAS1bbdAqzn5C90804fOl2uq2AHDlvqaqt7s2ltyoQ46wIkqcAb8q1Zs_4_EkiAphl4qoUNE_otHkgx-B7ozLAmNzPycO1anvXxfZkSu3kP2sadFUoNN2Di0ouD8yLPKBDY0Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
آن‌ها از آفریقا، آمریکای جنوبی و بخش‌های مختلف آسیا می‌آیند و در حال هجوم به اروپا هستند.
🔴
این یک تهاجم است و بریتانیا یکی از اهداف اصلی آن به شمار می‌رود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/138543" target="_blank">📅 23:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138542">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ترامپ: ما ضربه بسیار سختی به آن‌ها خواهیم زد. این را می‌توانم بگویم، چون آن‌ها عملاً کار زیادی برای مقابله با آن نمی‌توانند انجام دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/138542" target="_blank">📅 23:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138541">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
عارف: پس‌از ۲ جنگ تحمیلی اخیر ایران‌هراسی شکست خورده و اکنون فرصت طلایی برای گسترش روابط، به‌ویژه با کشورهای آفریقایی فراهم شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/138541" target="_blank">📅 23:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138540">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ترامپ: اندی برنهام باید درباره مهاجرت صحبت کند، چون مهاجرت در حال نابود کردن بریتانیاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/138540" target="_blank">📅 23:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138539">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0225a170.mp4?token=O59ZGEZqXtRUw0XVsOWzR-EqId3JXp_8qaUP6z5z03Jk7nde9Zj4CTm4BZ1xlSFrEcVR6LHuUArzgRWh_SyHg12BP0_rs9SLzlznt_ZUiHu-DchF6Bd79xoDaGzcICJ2yEmOCgtTMJ3NY6EOMYLFcCrwD7D1LsC5mh12jPi4Syx1m0N14RUBp9bP_0HNmsJM843-SovX7mjigc7uhflqP1bUeu1naXovuhvQlOTAvS7yiXo0xtydhPvhIefXuz7s1BM3SxokYwa1lFzh4zhiPpP73BOnVUbws-kbucUSum_yZZYvqlnOo3jTp8Ktqp8fkX2hFVg3A9FQ-Q-lefoPBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0225a170.mp4?token=O59ZGEZqXtRUw0XVsOWzR-EqId3JXp_8qaUP6z5z03Jk7nde9Zj4CTm4BZ1xlSFrEcVR6LHuUArzgRWh_SyHg12BP0_rs9SLzlznt_ZUiHu-DchF6Bd79xoDaGzcICJ2yEmOCgtTMJ3NY6EOMYLFcCrwD7D1LsC5mh12jPi4Syx1m0N14RUBp9bP_0HNmsJM843-SovX7mjigc7uhflqP1bUeu1naXovuhvQlOTAvS7yiXo0xtydhPvhIefXuz7s1BM3SxokYwa1lFzh4zhiPpP73BOnVUbws-kbucUSum_yZZYvqlnOo3jTp8Ktqp8fkX2hFVg3A9FQ-Q-lefoPBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
هر زمان که آسیاب‌های بادی را می‌بینید، یعنی با یک کشور رو به افول روبه‌رو هستید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/138539" target="_blank">📅 23:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138538">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9dd98031e.mp4?token=mmks4nvF-4VbAonhIh8IHDk-EMqT3lmHOZVk_VmmTvz8astfq8pHraLOoLCLakrXFtfGGC60RYOkWcUfwAnBt7QatMPqQ1BC-8RT3O78jTN2sWuH4lb1ZsMgN1muNPKbISC6Bdtmua3IqdUf3Q9UXjaePbLuP9JYuQAk2XyP8oWGpHMwgu4NWUF9mOeiuzbEHMSeq3sRNEWoaZ_D--SOyINBtT8YzaM7k1xEkiXmsSPS_9wdfGhXTOhXOMP-15PmNNCJimFyexZR0GOu5a3YrjuLnasJJM9c0K_eE4UdI5zXgEzc3KGoeSbm32Z42PWGSMMkfoxpfMrkKHCH-4ZRTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9dd98031e.mp4?token=mmks4nvF-4VbAonhIh8IHDk-EMqT3lmHOZVk_VmmTvz8astfq8pHraLOoLCLakrXFtfGGC60RYOkWcUfwAnBt7QatMPqQ1BC-8RT3O78jTN2sWuH4lb1ZsMgN1muNPKbISC6Bdtmua3IqdUf3Q9UXjaePbLuP9JYuQAk2XyP8oWGpHMwgu4NWUF9mOeiuzbEHMSeq3sRNEWoaZ_D--SOyINBtT8YzaM7k1xEkiXmsSPS_9wdfGhXTOhXOMP-15PmNNCJimFyexZR0GOu5a3YrjuLnasJJM9c0K_eE4UdI5zXgEzc3KGoeSbm32Z42PWGSMMkfoxpfMrkKHCH-4ZRTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
ترامپ: آبردینِ اسکاتلند زمانی پایتخت نفت اروپا بود؛ در واقع، پایتخت اروپا محسوب می‌شد.
🔴
حالا دیگر آنجا نفت استخراج نمی‌کنند و هیچ‌کس هم نمی‌تواند بفهمد چرا.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/138538" target="_blank">📅 23:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138537">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ترامپ:خواهیم دید که آیا در نهایت به توافقی می‌رسیم یا خیر، اما ما قرار است به شدت به آن‌ها ضربه بزنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/138537" target="_blank">📅 23:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138536">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ترامپ: تعداد افرادی که در دوران ریاست جمهوری بایدن بر اثر کووید جان باختند، بسیار بیشتر از تعداد افرادی بود که در دوران ریاست جمهوری ترامپ بر اثر کووید جان باختند.
🔴
کووید یک فاجعه بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/138536" target="_blank">📅 23:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138534">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87407dbb4d.mp4?token=gl5UtZj5KhY7lrLG30tWVmhXUJu8oiyaKLDLFcf9yuz-H2LUIluJMKnfYtwyqibgmtpvKWoqa1hxjY0aK2rA8ZFBScSjypomhes4aTVmLVGo0DhAZ4geD9bDhv4Uyy0kUVOMNuE6jIps1i4rgxhRK5d_SucH05TfsUWKL18acofGTzGRTKpXxWdJEf-bfSvwEtN6hvaQ3TU4dQi3YoZG_7gKv7cIatgiI73_e_-g0P5jVt4hTKa0tQCMZSk5ogvwgjfRbsb9NWw5zv0zsAFi77YC-cK0jtBBjz7ppxSjyEAJ3OL3T-W4_GqJXLUgVS0h-Li5JZN1sea3A234X3R7dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87407dbb4d.mp4?token=gl5UtZj5KhY7lrLG30tWVmhXUJu8oiyaKLDLFcf9yuz-H2LUIluJMKnfYtwyqibgmtpvKWoqa1hxjY0aK2rA8ZFBScSjypomhes4aTVmLVGo0DhAZ4geD9bDhv4Uyy0kUVOMNuE6jIps1i4rgxhRK5d_SucH05TfsUWKL18acofGTzGRTKpXxWdJEf-bfSvwEtN6hvaQ3TU4dQi3YoZG_7gKv7cIatgiI73_e_-g0P5jVt4hTKa0tQCMZSk5ogvwgjfRbsb9NWw5zv0zsAFi77YC-cK0jtBBjz7ppxSjyEAJ3OL3T-W4_GqJXLUgVS0h-Li5JZN1sea3A234X3R7dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار:
آیا اندی برنهام همان فردی است که می‌تواند بریتانیا را به سوی شکوفایی هدایت کند؟
🔴
ترامپ: او یک حرف بسیار خوب زد؛ گفت که می‌خواهد استخراج نفت از دریای شمال را آزاد کند.
🔴
اگر این کار را انجام دهد، بریتانیا به کشوری ثروتمند تبدیل خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/138534" target="_blank">📅 23:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138533">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991ae12297.mp4?token=v3ZfTtuih9V8V9shcWCxBBB3ksCjNb0BcusIJVGcfI9U0bxx3d24O8Ha2tDn8qt6s_cIWfZzljpJYQhc8GgrYND-uTsh0s9NkSBFklC7gySGzUnOeB5w__RjNPRdGAIpqoYX9uzzJrNZll3Jb3ifSJWTTIOWsmVnVta9_Ph7h-WFZREUqTh5mJiS77E-2a_4-CjETptGd76Ee51tVFDyjLeqeh6ViD8QzcxOBiq5Ndjbbv8hFFI7Tt5-yROnbxjnPFlEb5hOZpzDvzWA3k0attVtEoaxyU5ld5qjnnxyxFAp57She4ik380WtI5AJAMnAiT-E93Jn27yRL7zNfrT6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991ae12297.mp4?token=v3ZfTtuih9V8V9shcWCxBBB3ksCjNb0BcusIJVGcfI9U0bxx3d24O8Ha2tDn8qt6s_cIWfZzljpJYQhc8GgrYND-uTsh0s9NkSBFklC7gySGzUnOeB5w__RjNPRdGAIpqoYX9uzzJrNZll3Jb3ifSJWTTIOWsmVnVta9_Ph7h-WFZREUqTh5mJiS77E-2a_4-CjETptGd76Ee51tVFDyjLeqeh6ViD8QzcxOBiq5Ndjbbv8hFFI7Tt5-yROnbxjnPFlEb5hOZpzDvzWA3k0attVtEoaxyU5ld5qjnnxyxFAp57She4ik380WtI5AJAMnAiT-E93Jn27yRL7zNfrT6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر
: چه چیزی می‌توانید درباره حمله به نفتکش در مصر به ما بگویید؟ آیا این موضوع به ایران مربوط است؟
🔴
پرزیدنت ترامپ
: من در جریان قرار گرفته‌ام. این کمی بیشتر از همان چیزهای تکراری است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/138533" target="_blank">📅 23:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138532">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c51700e6e1.mp4?token=jCmwXicvdzk2PogLFQvIkbi6SHIrTWCRRoufnSzXW8I6bSp3TbCsee3BzL426al80ep4i8iQTu-piStduYypnTceGTKa-a_MLpGI8riuzdxEn4m8iQnLj4Zwd309pqpaVrlHnPcWvUYhHef30qVTzovm45cia-WSpaVuY39nT-REZ1kav-Pa6myGimUwrMtFn59iDPRLMD0M4y1GakLg7MC7lebAeiGf1okeH-ztAa-QqnsfCiIHCFxgvt5ONVhIJtpYJg5G6XZ1QaTGYjMd5lO3cQqJ8Hkm-y_zIRMR-NrRIw64VKBQ-w2QoAejtdWJ4Kc9Nw8bmXzdmVNy6w9hFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c51700e6e1.mp4?token=jCmwXicvdzk2PogLFQvIkbi6SHIrTWCRRoufnSzXW8I6bSp3TbCsee3BzL426al80ep4i8iQTu-piStduYypnTceGTKa-a_MLpGI8riuzdxEn4m8iQnLj4Zwd309pqpaVrlHnPcWvUYhHef30qVTzovm45cia-WSpaVuY39nT-REZ1kav-Pa6myGimUwrMtFn59iDPRLMD0M4y1GakLg7MC7lebAeiGf1okeH-ztAa-QqnsfCiIHCFxgvt5ONVhIJtpYJg5G6XZ1QaTGYjMd5lO3cQqJ8Hkm-y_zIRMR-NrRIw64VKBQ-w2QoAejtdWJ4Kc9Nw8bmXzdmVNy6w9hFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ:
ما می‌خواهیم آن‌ها را بسیار سخت بزنیم زیرا نوبت ماست که آن‌ها را بزنیم.
آن‌ها می‌دانند که این در راه است. آن‌ها از ما می‌خواهند که این کار را نکنیم.
آن‌ها دیشب سعی کردند با ۵ موشک به ما شلیک کنند. ما همه آن‌ها را رهگیری کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/138532" target="_blank">📅 22:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138530">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
نیویورک‌تایمز: آمریکا تلاش‌های خود را برای یافتن کشور‌های سومی که مایل به پذیرش مهاجران اخراج شده از آمریکا باشند، گسترش داده
🔴
دولت ترامپ با اروگوئه درباره پذیرش اتباع کوبایی اخراجی از ایالات متحده، مذاکره می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/138530" target="_blank">📅 22:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138529">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
گزارش ها از سفر ناگهانی وزیر دفاع عربستان سعودی به آمریکا درباره تشدید تنش قریب‌الوقوع در خاورمیانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/138529" target="_blank">📅 22:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138528">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H5LNbfjtFFzVcuCKNRR4bl0YUrLgSbOEv6KQcPfI9OyXvOYVinQz0PYKVfgmRuen5fZwwQtu5s0chXm54zzHH6izDkpz8JpMdI680FOwn7R9U9FCa8f3zrOr8MtAAX0AmCre6w3hPD3nna-1W9T637wYPcLcBGTp4_t3trFIcj87Rjc_OXzNLEDcyKVZOSe4Y8CVEry5WuRRp0knIHkVM-QYkKO5NdME_ej-CTZROVZeVWAjc4k1S6sWDfdUffgUZF8xyJ-N1tkATkwZ2mwBp-UNggNxC8Iyh6PWLLPjMbeBAEJaiEGGZuUn0AP5IDvZkyhebdq-Mw_EF3HteZ7smA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محسن چاووشی ۴۸ساله شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/138528" target="_blank">📅 22:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138527">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
تصویری از ماهرخ عشق ابدی تو خونه تتلو که....... خیلیا نمیدونستن اونه اما خودشه
😂
◀️
مشاهده فوری</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/138527" target="_blank">📅 22:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138526">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
دادستان مشهد : افرادی که چند روز پیش تو بلوار سرافرازان مشهد 2 تا بسیجی رو با تیراندازی به قتل رسونده بودن، دستگیر شدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/138526" target="_blank">📅 22:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138525">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
روایت اکسیوس از پشت پرده دیدار نتانیاهو و ترامپ
: ترامپ ۳ گزینه در قبال ایران در نظر دارد؛ توافق، محاصره و جنگ تمام عیار
🔴
نتانیاهو به ترامپ گفت «راه‌هایی برای افزایش بیشتر فشار بر اقتصاد ایران وجود دارد»
🔴
ترامپ نگرانی خود را نسبت به تأثیر جنگ بر بازار‌های انرژی مطرح کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/138525" target="_blank">📅 22:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138524">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
خبرنگار اجتماعی:
یه پسر ۳۹ ساله تو تهران که یه دوس دختر ۳۵ ساله داشت و ۱۶ سال باهم بودن و هر چقدر تلاش کردن به هم نرسیده بودن، در نهایت بالاخره پدر دختره راضی میشه و باهم نامزد میکنن و قرار بود این هفته عقد کنن که پسره دچار سکته قلبی میشه و جونشو از دست میده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/138524" target="_blank">📅 22:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138523">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
کانال ۱۴ (عبری):
تحقیق: کوه تبر؛ مهمترین دارایی استراتژیک ایران در برنامه هسته‌ای‌اش.
- این ویدئو به طور کامل از عبری ترجمه شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/138523" target="_blank">📅 22:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138522">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df71c5ea6d.mp4?token=N0uTENz5a-55C3jZ87-wsfqxEkQJ1AyxSYmvtfZWy07uZYD6BAjgsop6ikRrYzUMcBk7J9vqfv10NeKAtS9-lO8eFaybxSzdVn1JVJXSH5fs6-WyoQsgERIFJgQ64UticcNmAsV1d6dD7tRKEZNZEmjQ1Gs7J1CADfi-QXeFgNvhZPWYhAkyBZfqVsFtrs0YqsCXkHBUktb_Yh9N3jbib8dnLM6JacCZMi3bxZb4WeaDeLg48nrJZOSiGsue4XllTjzC-CxJQ8cg6bRjl6b5m9QbS51U6RWt__1oD76iUP4_k9jxyF2h3iJge0WEOHBCs0iDy7rizkJH9xbREF_Vwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df71c5ea6d.mp4?token=N0uTENz5a-55C3jZ87-wsfqxEkQJ1AyxSYmvtfZWy07uZYD6BAjgsop6ikRrYzUMcBk7J9vqfv10NeKAtS9-lO8eFaybxSzdVn1JVJXSH5fs6-WyoQsgERIFJgQ64UticcNmAsV1d6dD7tRKEZNZEmjQ1Gs7J1CADfi-QXeFgNvhZPWYhAkyBZfqVsFtrs0YqsCXkHBUktb_Yh9N3jbib8dnLM6JacCZMi3bxZb4WeaDeLg48nrJZOSiGsue4XllTjzC-CxJQ8cg6bRjl6b5m9QbS51U6RWt__1oD76iUP4_k9jxyF2h3iJge0WEOHBCs0iDy7rizkJH9xbREF_Vwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خفت کردن عجیب بازیگران در مراسم ختم اکبر عبدی
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/138522" target="_blank">📅 22:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138521">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⭐️
اگه فیلترشکنتون اذیت میکنه پیشنهاد میکنیم یکبار امتحان کنید
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید (برای شرایط اینترنت ملی هم اوکیه)
خرید وتحویل فوری از ربات زیر :
🤖
@SafeVPNXBot
✅</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/138521" target="_blank">📅 22:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138520">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">📍
تعرفه سرویس‌های مولتی و تک لوکیشن SafeVPN
📆
پلن های یک‌ماهه
📍
10 گیگ
➡️
35,000   T
📍
20 گیگ
➡️
50,000   T
📍
30 گیگ
➡️
75,000    T
📍
40 گیگ
➡️
100,000  T
📍
50 گیگ
➡️
125,000  T
📍
100گیگ
➡️
250,000  T
📍
نامحدود
➡️
400,000  T
📆
پلن های دوماهه
📍
10 گیگ
➡️
75,000    T
📍
20 گیگ
➡️
110,000  T
📍
30 گیگ
➡️
145,000   T
📍
40 گیگ
➡️
180,000   T
📍
50 گیگ
➡️
215,000   T
📍
100گیگ
➡️
390,000   T
📍
نامحدود
➡️
550,000   T
﻿
✨
ویژگی‌ها
✅
اتصال پایدار روی تمامی اپراتورها
✅
مناسب استفاده روزمره و شبکه‌های اجتماعی
✅
دارای ساب‌لینک جهت مشاهده حجم و تاریخ انقضا
✅
تک لینک اختصاصی بدون نیاز به بروزرسانی
✅
حجم واقعی بدون ضریب مصرف
━━━━━━━━━━━━━━
کانال اطلاع رسانی
📣
@safevpn_suportt
✅
مشاوره و خرید
🏪
@safevpn_secureSupport
✅</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/138520" target="_blank">📅 22:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138519">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
فایننشال تایمز: ذخایر نفت آمریکا به سطحی "خطرناک" کاهش یافته است، زیرا جنگ ایران، عرضه نفت را مختل کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/138519" target="_blank">📅 21:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138518">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
دومین حمله پهپادی در دیماط مصر
🔴
شرکت امنیت دریایی امبری خبر داد که کشتی حمل گاز طبیعی مایع یونان حامل پرچم برمودا در دیماط مصر مورد حمله پهپادی قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/138518" target="_blank">📅 21:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138517">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
مجدداً چندین انفجار در سلیمانیه عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/138517" target="_blank">📅 21:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138516">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
رایزنی نخست‌ وزیر قطر و وزیر خارجه آلمان درباره کاهش تنش‌ها در منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/138516" target="_blank">📅 21:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138515">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
حشدالشعبی: برای حفظ امنیت زائران، پاسخ به حملات آمریکا رو به پس از مراسم اربعین موکول کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/138515" target="_blank">📅 21:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138514">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHPfVn2v4WMY08UnChw83IU6HhXM0pFUEwsr_4SsPnSiBh4sUlN6s6o0H_L92M0INQdSXahGJXkjur_ImF5zJ9F-Gd7xvyuRN_w8qBrjfzGk-DXvOJEyReI2qxygkjbXqXymhJlV-u4c2o42WvO68dWNC7xcIBtv4A_g3rzhBq6XR6EMgQU06CSFjSyIUf-xYrMd4AqhtvRzfIGQDDwTXnWmWHJX0tqCZONfNOIAlni7ko5B_z7XV4lvi95_T6UgkaTdGrbUtfkpJpcsftdruKqIBrYu9DthMe65d8JDXb5xsOSjBB-9oEm2vYY0DW1IcwdNduhJicIcFBIROIPHeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقتدی صدر از رهبران شیعه عراق:
از سپاه پاسداران میخواهم سرزمین ما را هدف حملە قرار ندهد و از گروەهای شبەنظامی میخواهم کشورهای عربی منطقە را هدف قرار ندهند.
🔴
من هدف قرار دادن سرزمین‌های مقدس عراق که مرکز تشیع در عالم است را از سوی هر کشور یا هر طرفی را محکوم می‌کنم و همچنین اقدامات شبه‌ نظامیان افسار گسیخته (حشد الشعبی) را که عراق را به جنگی بی‌حاصل می‌کشانند، محکوم می‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/138514" target="_blank">📅 21:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138513">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
انفجار در سلیمانیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/138513" target="_blank">📅 21:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138511">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/608d0ac375.mp4?token=s10-Fs1XH4eqkaksSbUgZua_rlh_TKPTri3_WH4LpcP78lVASynHNz5XsYc_LM4wJqa2k-VemiTSKjULbkrAEEnNS4i4y7dB6Y2UEeGIB1StohP_S5X2fRdCZibMtk61eWIS6p5Z81-GhT2AB1s5UH3JMkoGy4xzxClWVHIR-_Zf6Qw9I12l1Fo1DEqaLQJmgtaFcqv65QptpPYZy-ZoGbw25RVBCfJAQyzn8a9H6yKgzrQF1M1THQE0qhI3K3V13zgDro-L868MPZVDwsXK3NlcxSznOqf3_jmrircks9MPV1kpZsCNYa_j6aYIIilm-8L49gk1MgoySrQ7T8oWlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/608d0ac375.mp4?token=s10-Fs1XH4eqkaksSbUgZua_rlh_TKPTri3_WH4LpcP78lVASynHNz5XsYc_LM4wJqa2k-VemiTSKjULbkrAEEnNS4i4y7dB6Y2UEeGIB1StohP_S5X2fRdCZibMtk61eWIS6p5Z81-GhT2AB1s5UH3JMkoGy4xzxClWVHIR-_Zf6Qw9I12l1Fo1DEqaLQJmgtaFcqv65QptpPYZy-ZoGbw25RVBCfJAQyzn8a9H6yKgzrQF1M1THQE0qhI3K3V13zgDro-L868MPZVDwsXK3NlcxSznOqf3_jmrircks9MPV1kpZsCNYa_j6aYIIilm-8L49gk1MgoySrQ7T8oWlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های F-16 در مراسم تشییع جنازه سناتور فقید لیندسی گراهام در کارولینای جنوبی مانور برگزار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138511" target="_blank">📅 21:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138510">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فوری / وقوع چندین انفجار در سلیمانیه در شمال عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138510" target="_blank">📅 21:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138509">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPtQLairJoH8pvHNUkmjptApASvEsOFPx4lNTZddoQA1Rxwbjn2ddPl1UNjD2U_UMH7r5kvcJGXvYEfYLqP3lU0GJp5utN14fl9zmR5LsjXnAldWclobcjG5NsRo56FqgG-SE09kmH-U7h_6F_B7Z4MhpMF8THF92qOIN35E_63zDcABD7a9OD1-6kGqoZqvqb95BhMYpTC677xPWEvwsDAIXugmvQJqNcLY1rsYkagJIjsx4HvEbwYoNJF5FxtntByResqnFBWe673Y-QY-Nhf-1HGDnnyzibLNJ1xqzxGiJmf7VjTxQt_VO8LtXDFDZDCEQ1mgK4kXVwAcX5x3HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا چهار نفر از اعضای سپاه، در حمله عربستان و آمریکا به عراق کشته شدند:
🔴
علی اصغر آسِتانه / مجتبی اکبری
🔴
ابوالفضل صفری / امیر عباس مهراب پور
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138509" target="_blank">📅 21:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138508">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔎
فهرست ربات های کاربردی تلگرام
🔎
🤥
می‌خوای هر چیزی رو دانلود کنی؟
✅
@Peechdownload_bot
🤥
خواب بد دیدی؟ فال می‌خوای؟ با کسی که فال و تعبیر خوابش شبیه توئه چت کن.
✅
@Peechfaal_bot
🤥
ادعا می‌کنی سلیقه موسیقیت خوبه؟
آهنگ بفرست تا بقیه رای بدن، رقابت کن و جایزه بگیر.
✅
@Peechmusicbot</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138508" target="_blank">📅 21:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138507">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
فردریک مرز، صدر اعظم آلمان، درباره اسرائیل: آلمان مسئولیت ویژه‌ای در قبال کشور اسرائیل دارد.
🔴
ما نه می‌توانیم و نه قصد داریم از یک رژیم تحریم عمومی علیه اسرائیل حمایت کنیم.
🔴
این موضع در آینده نزدیک نیز تغییر نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138507" target="_blank">📅 21:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138506">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
قطر ضمن اظهار نگرانی حملات ایران به اردن را محکوم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/138506" target="_blank">📅 21:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138505">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
فرمانده ارتش اسرائیل :  اگه لازم باشه وارد مناطق دیگه هم می‌شیم، ما برای مقابله با سناریوهای مختلف آماده‌ایم
🔴
عملیات تو همه جبهه‌ها هنوز تموم نشده اگه لازم باشه، می‌تونیم دستاوردهای خودمون رو در اونجا هم بیشتر کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138505" target="_blank">📅 20:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138504">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
فرمانده ارتش اسرائیل :  اگه لازم باشه وارد مناطق دیگه هم می‌شیم، ما برای مقابله با سناریوهای مختلف آماده‌ایم
🔴
عملیات تو همه جبهه‌ها هنوز تموم نشده اگه لازم باشه، می‌تونیم دستاوردهای خودمون رو در اونجا هم بیشتر کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138504" target="_blank">📅 20:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138503">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c0eb94e88.mp4?token=GjSi2NhHl_i1_AgZwchXPYqER5OUwVhrsuFip2AzQEQmmd5JkY43Ws6aGVdcD_QDgTuKuzvO1GHlkww4wSmi91UdsOV-_k0JxlYM5z755IrH7Lhf0gFneUp3FTl-QMSjAezXAV_Ms6vMwG22aSAhAgNBEBdV86VcgkSjJxbZNB-cywOdzPJFM4vhVhjCRQbYmWg0yAfMR3Aa9DunNRZMFoWhuecCyj1kCOj9tS2NxR9bADwKQ-fZKWUCnC_V6Zm1MeZY1LTH3SDgP8TV_v0KXT8gFU95VHG8MLm9SE_DnkDjULIKElz7fq_EoUWN4Mm2kKTCMtXY1FB9LWhXU49ihZF5YMz9LgBd3mLWFhjIj0eCLYRPDwtHsJWcANhQn72O-Rwph2CnoVzhu9B9F07Yu4RiF7zBL67d-Q9Zf2QYoPQKNj7VrPNy4yvgZPZdoGNJQ4zrpmaej9z5VjxhLjy1SGv0VhlmBjsxePyqWoXBGz0HUrotFP6c4lZ4UVxwoNftHLqRRwSdvZDRjrguUELj0H5h5xc3sQb2E2OJCG1Ht-cWZj_cCMufL12I5rsbun5YDjOqiocVk5G5yDgkOtzprmt6C9AKx6gFeI_FPqPTmIclYXgmLuGrNta-jMB2IhS0MyjG3Scm7Wvob8B-i8D0Du8U-K4EZ4w7o6v896mvZ-s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c0eb94e88.mp4?token=GjSi2NhHl_i1_AgZwchXPYqER5OUwVhrsuFip2AzQEQmmd5JkY43Ws6aGVdcD_QDgTuKuzvO1GHlkww4wSmi91UdsOV-_k0JxlYM5z755IrH7Lhf0gFneUp3FTl-QMSjAezXAV_Ms6vMwG22aSAhAgNBEBdV86VcgkSjJxbZNB-cywOdzPJFM4vhVhjCRQbYmWg0yAfMR3Aa9DunNRZMFoWhuecCyj1kCOj9tS2NxR9bADwKQ-fZKWUCnC_V6Zm1MeZY1LTH3SDgP8TV_v0KXT8gFU95VHG8MLm9SE_DnkDjULIKElz7fq_EoUWN4Mm2kKTCMtXY1FB9LWhXU49ihZF5YMz9LgBd3mLWFhjIj0eCLYRPDwtHsJWcANhQn72O-Rwph2CnoVzhu9B9F07Yu4RiF7zBL67d-Q9Zf2QYoPQKNj7VrPNy4yvgZPZdoGNJQ4zrpmaej9z5VjxhLjy1SGv0VhlmBjsxePyqWoXBGz0HUrotFP6c4lZ4UVxwoNftHLqRRwSdvZDRjrguUELj0H5h5xc3sQb2E2OJCG1Ht-cWZj_cCMufL12I5rsbun5YDjOqiocVk5G5yDgkOtzprmt6C9AKx6gFeI_FPqPTmIclYXgmLuGrNta-jMB2IhS0MyjG3Scm7Wvob8B-i8D0Du8U-K4EZ4w7o6v896mvZ-s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هجوم عجیب مردم به سمت علی دایی تو مراسم خاکسپاری اکبر عبدی
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138503" target="_blank">📅 20:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138502">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
اردوغان: لوایح قانونی در مورد انحلال حزب کارگران کُردستان را طی روزهای آینده به پارلمان ارسال خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/138502" target="_blank">📅 20:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138501">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjE_GBjQpHIxnC8miM9jaE3K8OK4sfgVvvevBZ4dDWaFRcEKiZjeTbOH2ghT9Tx6MsiL2lGdEEe9mok0jlMBK2bZMv5c179F5j6Ra_3c-Q032WP8aT1VGKHM9DG7T0SznoRNqnISJlYjPHmIBk5rK64eW9_NTcnphIO87uXm4OUShZnqvYGnzQvvZrTZ4z0V4RnI8Cg7VQsMTtH2WhwlIx_Mtc8pg4nW-lcLQXd7l0NvZDpWFwL3itnURfwhTBdMU0GZq8i-wGY8PHCu9ZfGTM2i3zYrsNAOdFdT154PEgf5MdHViLXBAIQeiaVjd08Eax9vWwgnSogfC75-BSKv9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش مخبر به حمله آمریکا و عربستان به عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/138501" target="_blank">📅 20:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138500">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
به گزارش واشنگتن تایمز، وزارت خزانه‌داری آمریکا اعلام کرد دو نهادی را که به گفته این وزارتخانه از سوی ایران برای کنترل تردد در تنگه هرمز مورد استفاده قرار می‌گیرند، تحریم کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138500" target="_blank">📅 20:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138499">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوری / منابع سوری از حمله توپخانه‌ای ارتش اسرائیل به اطراف شهرک عابدین در منطقه حوض الیرموک در حومه استان درعا خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138499" target="_blank">📅 20:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138498">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
پرواز چهار فروند بمب‌افکن استراتژیک Tu-160M نیروی هوافضای روسیه از پایگاه هوایی اوکرایینکا. این بمب‌افکن‌های استراتژیک در یک ماموریت رزمی حضور دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/138498" target="_blank">📅 20:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138497">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ea4a001fb.mp4?token=LLEoeP6jcjlMZ2Xgx8BCqPDaqI7dfR3cUyEG3a5q4OL92E5kUw_EBSHX3wWa61XbMsPuPvhegDrgRPuTEqKve-Tr4AKoa_65uCxqicr1GTjDFUiC2yoNBzl-3yzbNfdzz8iJLNWNFarDW9PXyCyya4Tt1Q_jbJIxaXUq9hDbdxV5Jyz-jKb14PplEdSbIXOWGdXiuhsCXRHME76gvEiCNWRBbf_F1-WyeWpmFEOYYh3kaTH0hGZlgXQiv0nHFm7YIaCkEvG24sMAcHidhx5_pqsISGu0X8dSyBNWXo1O7sVh5ZDtfC1UGnLtYPnlTsNIv_klcYERuN-kW_gOhKxRsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ea4a001fb.mp4?token=LLEoeP6jcjlMZ2Xgx8BCqPDaqI7dfR3cUyEG3a5q4OL92E5kUw_EBSHX3wWa61XbMsPuPvhegDrgRPuTEqKve-Tr4AKoa_65uCxqicr1GTjDFUiC2yoNBzl-3yzbNfdzz8iJLNWNFarDW9PXyCyya4Tt1Q_jbJIxaXUq9hDbdxV5Jyz-jKb14PplEdSbIXOWGdXiuhsCXRHME76gvEiCNWRBbf_F1-WyeWpmFEOYYh3kaTH0hGZlgXQiv0nHFm7YIaCkEvG24sMAcHidhx5_pqsISGu0X8dSyBNWXo1O7sVh5ZDtfC1UGnLtYPnlTsNIv_klcYERuN-kW_gOhKxRsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر دیگر از تأسیسات گاز مایع آمریکا در مصر
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138497" target="_blank">📅 20:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138496">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
وضعیت کشتی آمریکایی هدف قرار گرفته در مصر
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/138496" target="_blank">📅 20:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138495">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb7b2109b.mp4?token=EbQJy3iBv-2Zp_9rdE8kdz9cxi6DWtg_egTr4MCOUwFESQlBIdubpYWvS6DK8Fhl8JdZXyyrCibMLFazBRyVRRra-1w5CtKJPdCwfR84rZ7hUyYHiamTzmJcmTF75IcvkOyjEH0JrD45tb0LLiFoAEUCpONRyTvn5Mt-9RAprhKo_m_HePXMmGPMTI5PAHfJ-P1CwBkMgVe-6kZMKCgSnF95GYON1uowFdFSCD4ZfPP4Jbx68C2byQ5AA6wAoMQRT5RvnKnsQwmcppzzKRdR8sHy0PZBar-60z01lmCsoziNdJXOQvl_lP7uR_Y8Cu64vYm0AZJQ1wy3pHehUi_7eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb7b2109b.mp4?token=EbQJy3iBv-2Zp_9rdE8kdz9cxi6DWtg_egTr4MCOUwFESQlBIdubpYWvS6DK8Fhl8JdZXyyrCibMLFazBRyVRRra-1w5CtKJPdCwfR84rZ7hUyYHiamTzmJcmTF75IcvkOyjEH0JrD45tb0LLiFoAEUCpONRyTvn5Mt-9RAprhKo_m_HePXMmGPMTI5PAHfJ-P1CwBkMgVe-6kZMKCgSnF95GYON1uowFdFSCD4ZfPP4Jbx68C2byQ5AA6wAoMQRT5RvnKnsQwmcppzzKRdR8sHy0PZBar-60z01lmCsoziNdJXOQvl_lP7uR_Y8Cu64vYm0AZJQ1wy3pHehUi_7eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه نفر تو هواپیما یک کتاب خالی با جلدی که روش نوشته بزرگترین دستاوردهای کامالا هریس رو به ترامپ میده و واکنش ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138495" target="_blank">📅 20:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138494">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
سی ان ان: ارتش آمریکا اکنون کمتر از ۸۲۷ موشک رهگیر پاتریوت و کمتر از ۲۷۸ موشک رهگیر تاد (THAAD) در اختیار دارد؛ در حالی که پیش از آغاز جنگ، این ذخایر حدود ۲۲۰۰ موشک پاتریوت و ۴۵۲ موشک تاد برآورد می‌شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/138494" target="_blank">📅 20:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138493">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
فرمانده ارتش اسرائیل :  اگه لازم باشه وارد مناطق دیگه هم می‌شیم، ما برای مقابله با سناریوهای مختلف آماده‌ایم
🔴
عملیات تو همه جبهه‌ها هنوز تموم نشده
اگه لازم باشه، می‌تونیم دستاوردهای خودمون رو در اونجا هم بیشتر کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/138493" target="_blank">📅 20:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138492">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca7b1b38e0.mp4?token=kDuZa-fBGDUOU1vTH7oH3r73tEBnCFGBOrbe8gcz1zjm5MCV5Qyyb_feebBYjIfF5pb7yikNlmFQ42uB1Jf7kxPUBHJLVjUQqsnk9DRl7hqLHJ54UifFrZxYYiKlzwrNfa4Rozwo4BWpOOxqZDN_qdSzgH8Y6WUFVzIhmJ0o0w7NndpJD147XzuYL4uXqcoUuZWn7V1oRUOXmTMKkFusXpjSKfmEE2G1ywQJyxyD7u-Eq4XMuzUBkasMsi6lqkqKL4U5qF6wG4MOPVl5OGPai4uKhO3bszTmt4tOVCgbA0ESuKrKPBgbht-jORrGHFgObbWRvJPt3PAZLq7h4QTuWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca7b1b38e0.mp4?token=kDuZa-fBGDUOU1vTH7oH3r73tEBnCFGBOrbe8gcz1zjm5MCV5Qyyb_feebBYjIfF5pb7yikNlmFQ42uB1Jf7kxPUBHJLVjUQqsnk9DRl7hqLHJ54UifFrZxYYiKlzwrNfa4Rozwo4BWpOOxqZDN_qdSzgH8Y6WUFVzIhmJ0o0w7NndpJD147XzuYL4uXqcoUuZWn7V1oRUOXmTMKkFusXpjSKfmEE2G1ywQJyxyD7u-Eq4XMuzUBkasMsi6lqkqKL4U5qF6wG4MOPVl5OGPai4uKhO3bszTmt4tOVCgbA0ESuKrKPBgbht-jORrGHFgObbWRvJPt3PAZLq7h4QTuWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تشییع جنازه شبه نظامیان حشدالشعبی در عراق که دیشب تو حمله آمریکا و عربستان کشته شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138492" target="_blank">📅 20:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138491">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: نتانیاهو نهادهای امنیتی را برای تدوین طرحی جهت انجام عملیات نظامی در کرانه باختری مأمور کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/138491" target="_blank">📅 20:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138490">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
کانال ۱۱ اسرائیل: در آمریکا، از اظهارات کاتز، وزیر جنگ اسرائیل که فاش کرده بود هواپیماهای آمریکایی از اسرائیل برای بمباران ایران پرواز می‌کنند، خشمگین شده‌اند.
🔴
رئیس ستاد مشترک ارتش اسرائیل، از آمریکایی‌ها عذرخواهی کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/138490" target="_blank">📅 20:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138489">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
نقدعلی، نماینده مجلس: یک نماینده مجلس به من گفت از درد بی حجابی در خانه گریه میکند !
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138489" target="_blank">📅 20:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138488">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
نتانیاهو : سفرم به آمریکا خیلی عالی بود
همه دائم از موج نفرت علیه اسرائیل تو آمریکا حرف می‌زنن
🔴
اما شاید از موج‌های عشق و حمایتی که وجود داره خبر ندارید
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138488" target="_blank">📅 20:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138487">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
بنیامین نتانياهو: من همین‌جا با وزیر دفاع، پیتر هگستث، گفتگویی را به پایان رساندم.
🔴
او نکته جالبی به من گفت. گفت: «ما به جهان نگاه می‌کنیم و کشورهایی وجود دارند که اراده مبارزه در کنار ایالات متحده را دارند، اما توانایی آن را ندارند. و کشورهایی وجود دارند که توانایی را دارند، اما اراده را ندارند.»
🔴
او گفت: «فقط در اسرائیل است که ما هم اراده و هم توانایی را می‌بینیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/138487" target="_blank">📅 20:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138486">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gI0ZL81ywTD9N_H39XsJwj_GmnKcuIdYSPl5H486r5B2V_ddlf86uZQi-oJ7hHmlTL6Yej0ocRlDFYtstpHwfk_9LZ6vuPL-jeZI8y9I9U5XTkWTUBshAO894nRf_nvSn-58CifmrOKLwKkJjDXptQYADUEDLOP7K33vvQvzwXHQXn_lIa63dGSil5YySoPnjLuIfkx2QenBDoNok_uyMdWYXujmyU2fHiALZXJCkHv-rp1Gp2Opr9vTtKjokiJH7zmiURyOv1RpouJf2PutAW57_YDqO3zESbh_1VnF5Vn-t65vNKHUu8wQja1-_GhnMHCulTVs6iL5ejGZusz2wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر منتسب به لحظه خاموش کردن آتش کشتی حامل LNG آمریکایی توسط مصری‌ها در بندر دمیاط
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/138486" target="_blank">📅 19:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138485">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc310ff270.mp4?token=nqjwmwa0-FZ5cgtRfCtawsGqaZmpG4u22VcQk8_lNF-TdE2pYxxclIJWAPBHFEnv4pvWTwirE2ESVfmIf9koaUws67128QI_ceEiTzgsxKfYCE5tmqWLIVqG-J0J6XoqaM3hRKIdDzV4kZyRTJH9naA3kL7gPD-Drd9lQ3vJ7uLGF1NItcKuuQe7CbA-A6Y1z1ejP_MfcG4dO1hPL-Gn1vRaJ3Ok7CE2_0t5DJtIaY8hBHZyrXq9P8kkSx9RichRLfIfflYo1jDKG2vgbjohc5gd-iWrkwprSq_MN9kmQS_Ollw2_ZyxmUY3KNRlUBCdbtI7o2Ls96MTfkCyVK4zXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc310ff270.mp4?token=nqjwmwa0-FZ5cgtRfCtawsGqaZmpG4u22VcQk8_lNF-TdE2pYxxclIJWAPBHFEnv4pvWTwirE2ESVfmIf9koaUws67128QI_ceEiTzgsxKfYCE5tmqWLIVqG-J0J6XoqaM3hRKIdDzV4kZyRTJH9naA3kL7gPD-Drd9lQ3vJ7uLGF1NItcKuuQe7CbA-A6Y1z1ejP_MfcG4dO1hPL-Gn1vRaJ3Ok7CE2_0t5DJtIaY8hBHZyrXq9P8kkSx9RichRLfIfflYo1jDKG2vgbjohc5gd-iWrkwprSq_MN9kmQS_Ollw2_ZyxmUY3KNRlUBCdbtI7o2Ls96MTfkCyVK4zXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت کشتی آمریکایی هدف قرار گرفته در مصر
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/138485" target="_blank">📅 19:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138484">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
کوثری عضو کمیسیون امنیت ملی:
حمله آمریکا به عراق مانند حمله به خاک خودمان است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/138484" target="_blank">📅 19:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138483">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
رویترز: یک تأسیسات شناور ذخیره‌سازی گاز طبیعی مایع (LNG) متعلق به آمریکا و تحت بهره‌برداری این کشور، هنگام استقرار در بندر دمیاط مصر هدف حمله پهپادی قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/138483" target="_blank">📅 19:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138482">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
الجزیره: شرکت امنیت دریایی امبری گفت که حداقل یک حمله پهپادی به یک تأسیسات ذخیره‌سازی گاز طبیعی مایع ایالات متحده در دمیاط، مصر اتفاق افتاد
🔴
تأسیسات ذخیره‌سازی شناور مورد هدف قرار گرفته متعلق به یک شرکت آمریکایی در دمیاط مصر است و توسط آن اداره می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/138482" target="_blank">📅 19:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138481">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
بلومبرگ: ایران معتقد است که توانایی ترامپ برای تشدید این کارزار به دلیل کاهش ذخایر جهانی نفت و مهمات آمریکایی محدود است - ذخایر استراتژیک نفت اکنون پس از کاهش ذخایر برای کنترل قیمت سوخت، در پایین‌ترین سطح خود از دهه ۱۹۸۰ قرار دارد
🔴
بعید به نظر می‌رسد ترامپ تا زمانی که ایران از موضع خود در قبال هرمز کوتاه نیاید، عقب‌نشینی کند، اما ایران همچنان به دنبال کنترل تنگه هرمز و مطالبه هزینه‌های عبور است. مقامات انتظار دارند که درگیری‌های سطح پایین برای مدتی ادامه یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/138481" target="_blank">📅 19:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138480">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqnz6sO-liifwUxtxawZlnIFwsy_3Bd2AvZV-qf8mDrikPhS4k05FcR1vqWP5_vCxOyBCaM363s3Qj82y79XgJTVVbRXkxbw7aMy9O9j3MypKs4EmN7TnsXbHCWRpCYnodO1SHCJAT-8pE97d8z3ZS6GoXreiD8QOpB1jXmJWiOPiix2K0rt_lkPSAT1Bwm6JPxHsKG3UUO_NpJoF2sqE0mldShEk2WAir875vMWM_v-bcPoapYjM8ImoDlXFK-Jrt-5LAfE21qdmkpiTNAcUe9PBVkP6rV4gpbOMAiHSUN0MB7YYgqglygrtheIAgCk0_FSVSxGIID7YvYBwc-qJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گاردین: تحلیلگران هشدار می‌دهند که حملات مشترک آمریکا و عربستان سعودی در عراق، منطقه را به سمت یک "ناآرامی و بی‌ثباتی" سوق داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/138480" target="_blank">📅 19:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138479">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPO_ojrACqki-zlDuEnVtHJnnn2iVTFn-adHLvYGKvWIxnn-vD1iIkXOQ0NRGkQeY4WtnsH7qdR0W-HvmBT9ha2Dcpy5w_gtxzgpDwXHUunuuMJosvJ25H2zKoBLh8Z07xkkj_aC7fksulU8dGxDXuliq1lexmM9uV8A3bFVmCDCYcKHSKiZ0hU-zzDkxnOqBYaqufHOWDAogiETW6x-XGIAhIVHX-Uc56ipWVq479ZNjVeejsvqhrHokubbrVCmORC_43KGzMcjZSkQNSsqxN25Dm3V9Rrm6RqCpCkuaR2xdKF-Xx0FFnoMiqH4rOWDpV9377RRdY61BPjldVw6eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت، ۹۰.۲۴ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/138479" target="_blank">📅 19:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138478">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
پس از حمله مشترک عربستان و آمریکا به نیروهای حشدالشعبی، نخست وزیر عراق، علی الزیدی، خواستار دیدار با محمد بن سلمان، ولیعهد عربستان سعودی، در جده و در روز پنجشنبه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/138478" target="_blank">📅 19:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138477">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzrAjDfJH0QbiPBniqnZQtRBLruFmDlw5T9dvKTbl4s9-wJ4l_E1IxRQaWaVE1VDesZkyqBhaahMGgwP0pGa3D9kkBi-azRD67b6j3rPQLr0R78GV7jx7fHZN0Yxc6yNdEg8bxfXJSXlUr8wPwCnC7K_dALGf9_E8-TF6V-YB-RsV7XAxF-wZv591d2g6aE6amjqDJRk02KHEukugt2rHGbw8harohBWptZz_mxeWLFFE4t6k-y1Z5S9nTT09ojQQdYLU4Pr9atZvVAgjMkjl7grvoYLHR5mCUe-5QcKVumkULo3Lnt_rU0yXI3zA5dOGIebbF9D7KJHUlbxgeQapw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
تنگه هرمز یک آبراه بین‌المللی است.
🔴
سپاه هیچ اختیاری برای تعیین مسیرهای تردد برای جریان آزاد و باز ندارد. کشتی‌های تجاری همچنان از این تنگه با حمایت نظامی ایالات متحده استفاده می‌کنند.
🔴
از اوایل ماه مه، نیروهای سنتکام به عبور تقریباً ۱۰۰۰ کشتی و ۵۰۰ میلیون بشکه نفت خام از این آبراه باریک کمک کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/138477" target="_blank">📅 19:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138476">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
یک مقام ارشد اسرائیلی : مجتبی خامنه‌ای قطعاً زنده‌ست؛ ایران در حال حاضر تقریباً ۱۵۰۰ موشک بالستیک در اختیار داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/138476" target="_blank">📅 19:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138475">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فوری / نتانیاهو : ایران غنی سازی را در زیر کوه کلنگ آغاز کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/138475" target="_blank">📅 18:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138473">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G-bLYmS7rgACOSNr-GVyERA9kL3LEqnGQBKlbdQpFaFOZf4DYrNdz5NY6hAORdULZV_xzgnZiA6-YSQAGzTpRhAbk8u74pmAJwdqj33ZjGsRySDMsKr0isAgmd9AgklBDre5osWzR-fiwI9_2W44YCwbsle8QloK21YesdSIIkUwF03JeVLQShxkFiaKgaTToVDe_fUzElZ0DBnNaHLqp_uVWxd7UcFHNKv1dqIC_BJ10hw07OM8kG-lSd7-tQQkzsBjJww4isCtJFTJC5jk7QyL95dKT5U2ih-d1o3zfOr3ToqbfX7gZFfIlxHaFr8ZL93XjWTjR6RT0zUmwRMLuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PallF82-k0IRhQAMLn5NIyKxPL1Tl0tSJ7excsvGV2_1QEOa9pY3VuhVvgJPVoWOuy5VoWZqrdM_cNlhL8-yipRIiNyi_5Q2-jF-sCbtouyesirP83fjnC3iBkjuXJLwAfSM2sGmw_qtgi4yZaMtTcBMSlubEug2XWNlq8Pg-baF7sVbln0NvE_dAWOfBC2_IvLy00v7-OgHQqNRfuHpqbBvOk3BOqo6DPSgjByQwiGPmYmvqtvNthbN4qkX_h92ELHAcEw8hmnMBGcCaD-xtB-LRtrwE-poP_X_DHfbqSq1SP-f56JUc7Xds7ezecCA4qNmk1-vOMmwk7E1tWdBWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
فعالیت‌های گسترده آمریکا در خاورمیانه، به منظور آماده‌سازی برای حمله به ایران.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/138473" target="_blank">📅 18:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138472">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e95b6749bb.mp4?token=QhIzAmu0sTAzM-7rL-DyM_sJ1XRL0siSwxxFxTcoFJTlekYsRhXYrqipuIGwZX-FmFJqK3jXhcyUJpsLnSTuvPZfDXxZoYUyh1AzMy9x_S2mYjpFVwen7zGFmaSWKlagpDmyWxtZUFPr_EjceQBwh7s-Wj4L_4fJhhUU6K2Im1FtW8Qo8FJ31HRr9K3TgDR-U0L15ZMFeTyVgFeuHuUEcfe7mtipdcuBX6djZyGhliYqJnPfsFUKO022X7lNaNy9vRQPTrex2VGZyInUNJtc5Yh3-pOHEQLbEQWrHsWNT2vJFE4XHqlnCn2tzw_7WP8YcTRT0ns7bEv7vxHs2gfjlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e95b6749bb.mp4?token=QhIzAmu0sTAzM-7rL-DyM_sJ1XRL0siSwxxFxTcoFJTlekYsRhXYrqipuIGwZX-FmFJqK3jXhcyUJpsLnSTuvPZfDXxZoYUyh1AzMy9x_S2mYjpFVwen7zGFmaSWKlagpDmyWxtZUFPr_EjceQBwh7s-Wj4L_4fJhhUU6K2Im1FtW8Qo8FJ31HRr9K3TgDR-U0L15ZMFeTyVgFeuHuUEcfe7mtipdcuBX6djZyGhliYqJnPfsFUKO022X7lNaNy9vRQPTrex2VGZyInUNJtc5Yh3-pOHEQLbEQWrHsWNT2vJFE4XHqlnCn2tzw_7WP8YcTRT0ns7bEv7vxHs2gfjlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، بنیامین نتانیاهو، با پیتر هگست، مشاور وزیر دفاع، در واشنگتن دیدار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/138472" target="_blank">📅 18:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138471">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
روزنامهٔ هاآرتص: دو سرباز زن اسرائیلی این هفته خودکشی کردند
🔴
از ابتدای سال دستکم ۱۶ سرباز جان خود را گرفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/138471" target="_blank">📅 18:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138470">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GlfkpGK7VZNrMNmI7RcegcSNmsVPxzl1GmaBBadVl95rdjMeqGVHbvFA8MhjoMnhpQDRZVTZQUTKJRwfyeg92F0tUUqVXByOhhunnXNJlYLO0MAOApavFgFoKDR1XR0_mTo6o8Ui7OGqz1rJET0AntleLSb2BvDsODPSvl3TjbDZLa7RAH5g2ypiBXRJg9bnvLq4wr8_BGqUZqzFzba2sgq_p2YbOE-PISPFY4E2IIcEdgzsUsC-ws-IDJTWEYyP2wbLscAZ54MHNqGZcNUmXgTV8ASCHCilJSh76MGFNwxSPPgSDsgMYZ66gNEF6W6mc3fMdP6enf5gebweVoKt9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنبش حزب‌الله نجبا بیانیه‌ای صادر کرد و در آن به حملات هوایی اخیر عربستان سعودی و آمریکا در سراسر عراق اشاره کرد.
🔴
این جنبش خواستار اخراج تمامی نیروهای آمریکایی از عراق، قطع هرگونه همکاری با عربستان سعودی و همچنین درخواست از دولت عراق برای تهیه سامانه‌های پیشرفته پدافند هوایی به منظور حفاظت بیشتر از عراق شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138470" target="_blank">📅 18:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138469">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
مقام ارشد اسرائیلی به i24 news :هنوز غنی‌سازی اورانیوم تو سایت «کوه کنلگ» شروع نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/138469" target="_blank">📅 18:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138468">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39fa80d3ba.mp4?token=nKtTWrtsnrTqbpXVasw1eoqtcWCNraodxoELnsL0JuFnWTxqJFF3fBRTIdzF9n87yKgCkqlpmmx1YT43Vkgg4JysMvGzPv6DGh5orbHYyJEkxrQv1sUAoiBxVgpaE9H2S30HBxlrTNFORlol0XhXIRHJXhbjeETkKByWDcL1uLmBOwzHFMKdZrlnRdIhIBYjshDRrRP1Z0pOMZHi0H8AKMlB65NszfxUVffeGPA9VuPMZhFckV-a7KOVSM3dpT_0WK161V0qFk8Zq5y0IsZcQg7C_FAyUmpc34-WyBZ9jc-88oD6qQEzAtmeugEIFM1GiY_NNcjFGvnp4yAlWSQisg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39fa80d3ba.mp4?token=nKtTWrtsnrTqbpXVasw1eoqtcWCNraodxoELnsL0JuFnWTxqJFF3fBRTIdzF9n87yKgCkqlpmmx1YT43Vkgg4JysMvGzPv6DGh5orbHYyJEkxrQv1sUAoiBxVgpaE9H2S30HBxlrTNFORlol0XhXIRHJXhbjeETkKByWDcL1uLmBOwzHFMKdZrlnRdIhIBYjshDRrRP1Z0pOMZHi0H8AKMlB65NszfxUVffeGPA9VuPMZhFckV-a7KOVSM3dpT_0WK161V0qFk8Zq5y0IsZcQg7C_FAyUmpc34-WyBZ9jc-88oD6qQEzAtmeugEIFM1GiY_NNcjFGvnp4yAlWSQisg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رونمایی چین از موشک بالستیک هایپرسونیک YJ-۲۰
🔴
ارتش چین برای نخستین‌بار تصاویر شلیک موشک بالستیک هایپرسونیک ضدکشتی YJ-۲۰ را از روی ناوشکن مجهز به موشک‌های هدایت‌شونده تیپ ۰۵۲D منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/138468" target="_blank">📅 18:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138467">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
یک مقام ارشد اسرائیلی به رادیو ارتش اسرائیل: تصمیم‌گیری درباره اینکه آیا به ایران حمله شود یا نه، بر عهده رئیس‌جمهور ترامپ است، مگر اینکه ایران تصمیم به حمله به اسرائیل بگیرد.
🔴
هیچ حمله بی‌جوابی وجود ندارد، و ایرانی‌ها می‌دانند که اسرائیل پاسخ خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/138467" target="_blank">📅 18:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138466">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5fJ_H9c0w4EjMhGOq0Frcct2bC5AuzMqjRgDe65HQ5am5UuWUOvmuckETSzQEEVFTNnj01eoMLB5TC9N8LlaxSGQs1h-a2MCv5xSrzU83LZgEZ_1QvXf6XzRmwVdxyNek1S11vrc-KCpOv4r_1OEw0lR7Nhz2YQws9T_eCQddZqCWM5h5wFHlFddhGMmi76lK_Gy9X1KqSNcZ8edcll7zlGVaQ-HoxfqNnlbe7d4m7bz2qMtC_TCebUoPxze114Eg4HC_ep_Mcle4fsFY9lmrYyzogC87tf7fm01mlBtySWC2foTDzz_80fDDCaEJB380rPshtqOyKvBOfDSCJvNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کوثری، عضو کمیسیون مجلس : جنگ تموم نشده، نباید جنگ رو قطع کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138466" target="_blank">📅 18:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138464">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
برخی منابع عراقی ادعا کردن که سردار حاج علی اقبال پور، فرمانده ارشد قدس و مسئول پرونده کرکوک ۲۰۱۷، به همراه تعدادی از نیروهای یگان قدس هدف قرار گرفتن؛ البته این خبر هنوز تایید نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/138464" target="_blank">📅 18:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138463">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
روزنامه هاآرتص به نقل از منابع آگاه گزارش داد که «بنیامین نتانیاهو»، نخست‌وزیر اسرائیل در جریان سفر خود به آمریکا از دیدار با «ولودیمیر زلنسکی»، رئیس‌جمهور اوکراین در واشنگتن خودداری کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/138463" target="_blank">📅 18:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138462">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
قیمت نفت خام برنت با ۷ درصد افزایش، از مرز ۹۰ دلار در هر بشکه گذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/138462" target="_blank">📅 18:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138461">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d19039aae.mp4?token=rw2I2Qu_cT0xUCsuz4-G5io-IB1nT7xIw0Xv6jrT9i2eT0oQISQTzr4j0aBcCwMYFwsj8Oujz__eaegrJZ5wQV8zR4rvxF6Vzn0YAuiHp7hHxMBYaywW76KsMJSPyH4E5N8dvak_VVQ2R9mAoEYY0N5-BHisEfy4VomO1fZ96o65WFzXtQ2aPcYk3JwWxw32qDUEePHhiK4iqb0ss9q3bwoNXFCFaBP5QJsquTJonKyrQrKr29DbAJ40M-rS888XNgYh4cWqbycMh_INQOtU7aykrmo7a2aVhN5Ogqnsu3kcaKnTBBrHimGEeZrB2nbKgv_4C-hKW60OwsLWA5DvKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d19039aae.mp4?token=rw2I2Qu_cT0xUCsuz4-G5io-IB1nT7xIw0Xv6jrT9i2eT0oQISQTzr4j0aBcCwMYFwsj8Oujz__eaegrJZ5wQV8zR4rvxF6Vzn0YAuiHp7hHxMBYaywW76KsMJSPyH4E5N8dvak_VVQ2R9mAoEYY0N5-BHisEfy4VomO1fZ96o65WFzXtQ2aPcYk3JwWxw32qDUEePHhiK4iqb0ss9q3bwoNXFCFaBP5QJsquTJonKyrQrKr29DbAJ40M-rS888XNgYh4cWqbycMh_INQOtU7aykrmo7a2aVhN5Ogqnsu3kcaKnTBBrHimGEeZrB2nbKgv_4C-hKW60OwsLWA5DvKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوکراینی ها امروز هم بدین شکل یکی دیگر از مراکز وایلدبریز روسیه (بزرگترین مراکز خرده‌فروشی)، را پودر کردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/138461" target="_blank">📅 18:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138460">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGUvhC8Zppt9XnuuqgrPaoqo_kPAPjlajZ-I9D_7zmJ8TXLp1IupgDwkTjugJPp26aZ-ZJTzJDRtYFiEwfer-pURXLx2j8PgA-18b16vqV3t9jb-cTgm-30BhrZYubuwbCrUIOt441jlDPnfjJOqHfm1b2Izsh_d4nkHRSNQyrjlAnJdI3GZOR_pPTKEJksArCXZ5e5YmSQczZKo-vwJfqZZWRFsyZmYBiyKcvN7ZwGGyH7kj2bpKY8G0ykREmbSp-tWPjNHsuZtOJgnmeC5FnX_RYIZR3mW6gX1J2rnLBWHJDFtGmSaPhaHhtQp8f2e8RDDnxIOCfzZ51RfYfYoPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/138460" target="_blank">📅 18:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138459">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQ9ZH08KHbYJ-RK1aFyQNZPlQ4XZ6Y4qxHXWzWv5YbY31n_Nsmg_HcB9dMRDeg9K1n96cG7EUYF0I4WpUdlrrIgBLEA3d7oxQo-qo5g8-970qpe2SLH2GHCEIgDAiJTwkOh2eQ5pO3ejc71r6b-lTxFKzrjzl183uAOSIOEThIOGURts5HnUNQtJm6OXhdaSKgrJcm7-l2QRcB7zCekp5U2yYMb4AXu2zmzFGW_A1DV4QdNPpKUiVYnLCApOXeY-R37HHWo7pqQbcV-lc8ZaKnV8xkNvhG4LkUZBEVPEduT6tinitw8-m_AN9TYJYL1tvlXM1ESbZbx5X1WP2lIdVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وثیقۀ تحصیل در خارج به ۲۰۰ میلیون رسید
🔴
براساس به‌روزرسانی سامانۀ سخا، مبلغ وثیقۀ مورد نیاز برای خروج از کشور با هدف ادامۀ تحصیل از ۸۰ میلیون به ۲۰۰ میلیون تومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138459" target="_blank">📅 18:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138458">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
پزشکیان: ما با دشمنان می‌جنگیم تا زیر بار ظلم و زور نرویم، پس نمی‌توانیم خودمان به مردم زور بگوییم یا ظلم کنیم
🔴
اگر معیشت و سطح زندگی مردم را بهبود نبخشیم، خداوند از ما نخواهد گذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/138458" target="_blank">📅 18:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138457">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
زلنسکی: از ترامپ درخواست کردم که یک «بسته اضطراری زمستانی»، شامل ۳۰۰ موشک رهگیر پاتریوت را در اختیار اوکراین قرار دهد
🔴
اگر مشکل کمبود این موشک‌ها برطرف نشود، حملات روسیه نیروگاه‌های برق ما را نابود و یک بحران انسانی ایجاد می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/138457" target="_blank">📅 18:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138456">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا از اعمال تحریم‌های جدیدی علیه شرکت‌های مرتبط با ایران خبر داد!
🔴
وزارت خزانه‌داری آمریکا ۸ کشتی و ۱۰ شرکت از ایران، چین و چند کشور دیگر را به بهانۀ ارتباط با ایران تحریم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138456" target="_blank">📅 18:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138455">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22502e2a34.mp4?token=Xn_jCSSSpBaoUmV2OErwNhKrCkl98KEIlqA9hwIMa7tRpKYY7H5P_XK24ElNlEBMV5hGxYpgW-k_gquEF46FJn66EbE8OH0WlH_HSW7Ku-2F4LD-6ff-udr-qYg3xnYWyW5dmpdepTp0w6yFPwfccrPXIHSlYEow1ftX-iw830lNOr13pXW8cqtHnyOWyDf6TZr_knP9TwqblWuRFkmGDDkldqHv3SKyCrLN23ZDTKD7cE1daPcpAOcvAIHLZ2NppumJDFg1kIweUyDeAJPsZXzP2nhVZaPFVwz1U91AegaOC2iGRp4XXNCnbhw7YVu8dhLjdyOhuqDnszAEvqhk-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22502e2a34.mp4?token=Xn_jCSSSpBaoUmV2OErwNhKrCkl98KEIlqA9hwIMa7tRpKYY7H5P_XK24ElNlEBMV5hGxYpgW-k_gquEF46FJn66EbE8OH0WlH_HSW7Ku-2F4LD-6ff-udr-qYg3xnYWyW5dmpdepTp0w6yFPwfccrPXIHSlYEow1ftX-iw830lNOr13pXW8cqtHnyOWyDf6TZr_knP9TwqblWuRFkmGDDkldqHv3SKyCrLN23ZDTKD7cE1daPcpAOcvAIHLZ2NppumJDFg1kIweUyDeAJPsZXzP2nhVZaPFVwz1U91AegaOC2iGRp4XXNCnbhw7YVu8dhLjdyOhuqDnszAEvqhk-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امام جمعه رشت: بابت اعدام‌ها تشکر میکنم و امیدوارم همشون اعدام بشن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/138455" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138454">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
تلگراف: چین قصد داره راکت‌انداز به ایران ارسال کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138454" target="_blank">📅 17:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138453">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOlRvc3FSkMr7Ap2x_E4nX1ycm3F8jnLLYhaFlMy44BBLRs-l22GiIYYumpztLcR8k7EEw1rA2s2u-rWMoaVp66H0tB0Flh3xoG9ict-1chXIoyLz3zG9yWw0oUEav9RPV4fcNcNMuxjsbLOH4F1Lys9QZFBtXR7w1yAwfIijmB5Ribbp0dbq6h3_H9Arc4AA7vpHK1YEiykIuryv1MIXjY9Vul1-iFGKKn-oXq0ziLTxLRf8bfTASUKR2UU74RgzkCpThOSkZJ6xfPSZ1rInV4ckqQcjFDWLNuKUfvcaPsW1rP8RXnYQxvt0elfPXvoKtv1eEq8WvG1L659xQcQBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چند روز پیش این مرد تو آمریکا یهویی روانی میشه و اول زنشو با تفنگ میکشه بعد ۶ تا از بچه هاس که همشون زیر ۱۵ سال بودن رو میکشه و آخرشم تو خونه آتیش درست میکنه و خودشم با تیر میزنه تو سرش خودش و خودکشی میکنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/138453" target="_blank">📅 17:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138452">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
اینترنت استارلینک در عراق فعال شد
🔴
سرویس ماهواره‌ای استارلینک رسما در عراق راه‌اندازی شد. دولت عراق و کمیسیون ارتباطات این کشور با هدف بهبود دسترسی به اینترنت، مجوز فعالیت اسپیس‌ایکس را صادر کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/138452" target="_blank">📅 17:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138451">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
سفارت آمریکا در عراق هشدار امنیتی برای شهروندان آمریکایی صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138451" target="_blank">📅 17:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138450">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزارت خارجه روسیه در پیامی کشته شدن تعدادی از عضو های گروه حشدالشعبی توی حمله دیشب آمریکا و عربستان رو تسلیت گفت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/138450" target="_blank">📅 17:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138449">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G31nKiRz2FrYrObdpT_MY1ZY1w3iwYQ2vRMLYvaBuk9bET7KhXr47nHP0KhNWEwmppkoqS7xjJoqdkDmW3pJCswhXudIja6majPonZbayIUoxwyLG41lhqoQXKRSmQOXtU4TWhBC_fp7CyJCEUpYfud55G96L0qHbvtHJ0FWkTL6UplQS93CUXdzIm3jWbeTmMhp3GnCu4ZrqTOykaTCFbDrnTem7v5t3ddQD9YiQ4MlLUhQa2-_edzQUaB5BI5Jv5lOmxsO4wdFYdCdTx9wxr4l6iM7a1CjCfX8wRVgWp25TGXYGhR5H1u4G3_qp2DA4s4Q_c2d-MtW5vnrdgFL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای آمریکایی تانکربنزین (برای سوخت‌رسانی هوایی) در حال حاضر در نزدیکی سواحل سینای مصر در حال عملیات است، که یک اتفاق نادر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/138449" target="_blank">📅 17:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138448">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqEc5snmcZjyB1KfTQDjeH59XX-Ybyfl4lKhYM2_TkHkZOEwOwRDLbMZciJ_dVla411TBjeBhgoHCJiQJXXM3Pcw6JmGkNcVw6e5KLBIyky4AwV8c_JZ1P-RIaCFwZUYylBa4s5Y_qXLd0i-OwQvgiNNhuK1bqyGAT06B6w8RBs19CtUoSN6OKHsDZ8PJA0Gopfyx0eEE6b3mN7Kv1SFxoruqzhDrQeXa7ijLrapLHPfsft6Fgzmh2w3gxujGG4KY3zxE_4M-nLW2FpfOdI3NpcDUqZDg8JNylDAR7bTC9Yw8NeS_p7qA1Owu3B5GSIKD8t3OjO7seUflC763AK_ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
پروفایل عجیب پاول دوروف مالک تلگرام در واکنش به تحت تعقیب قرار گرفتنش
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/138448" target="_blank">📅 16:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138447">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
این حرومزاده به اسم نوید زیاد خان قره باغی، با شیرین زبونی برا دخترا می‌برشون‌ خونه‌اش و داخل لایو می‌زنه و تحقیرشون می‌کنه.
🔴
تو این ویدیو که از لایو هاشه یه دختر اینقد می‌زنه خون بالا میاره و گریه می‌کنه و یه دختر دیگه اینقد می‌زنه بیهوش میشه.
🔴
روحیه حساسی…</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/138447" target="_blank">📅 16:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138446">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
این حرومزاده به اسم نوید زیاد خان قره باغی، با شیرین زبونی برا دخترا می‌برشون‌ خونه‌اش و داخل لایو می‌زنه و تحقیرشون می‌کنه.
🔴
تو این ویدیو که از لایو هاشه یه دختر اینقد می‌زنه خون بالا میاره و گریه می‌کنه و یه دختر دیگه اینقد می‌زنه بیهوش میشه.
🔴
روحیه حساسی دارید ویدیو رو نبینید.
آدرس این بیناموس: تهران،۱۶متری امیری، کوچه بهفر پلاک ۷۰۱
کد ملی ۰۰۱۲۰۸۴۸۶۷
+989351197525شمارش
برسونید دست پلیس فتا
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/138446" target="_blank">📅 16:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138445">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c546530197.mp4?token=LrhQ5HyCnG3tacJNF-YJJYR8ZjqdltGM-M6APmxfuuHS61z-o-PeQHvCCHrfeNWLPIDyCqhfMTxg4pqQb9xRrxjLaJ2iXIwLY7Tg8PxgEKpEEgEGbynVF-zHKc8vHmgUUdVCpspEcftoMDxEmzNoo85Oi3YAcX-z1aMQIJNYG0Ea8ZFNJ_tL5b5vbwAfrjCwk5PdH-xegwrN3D1JaCR5EWpf6nR-8QwHN9jP_vtf0sMStx_pWd7tURRdKXDSDpAm-9e5p9kQUzrGtYJiA3d00IMTt3Gbq2wrnMdsIUinYUraqQJEucSSeLJKwfy4IZ6X4STpFe5dsx2utdCbKDcY8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c546530197.mp4?token=LrhQ5HyCnG3tacJNF-YJJYR8ZjqdltGM-M6APmxfuuHS61z-o-PeQHvCCHrfeNWLPIDyCqhfMTxg4pqQb9xRrxjLaJ2iXIwLY7Tg8PxgEKpEEgEGbynVF-zHKc8vHmgUUdVCpspEcftoMDxEmzNoo85Oi3YAcX-z1aMQIJNYG0Ea8ZFNJ_tL5b5vbwAfrjCwk5PdH-xegwrN3D1JaCR5EWpf6nR-8QwHN9jP_vtf0sMStx_pWd7tURRdKXDSDpAm-9e5p9kQUzrGtYJiA3d00IMTt3Gbq2wrnMdsIUinYUraqQJEucSSeLJKwfy4IZ6X4STpFe5dsx2utdCbKDcY8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور جمهوری‌خواه، تد کروز: فیدل کاسترو یک میلیاردر بود. پوتین یک میلیاردر است.
🔴
رهبران رژیم‌های کمونیستی همیشه ثروتمند هستند. آن‌ها از کسانی که بر آن‌ها حکومت می‌کنند، دزدی و غارت می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/138445" target="_blank">📅 16:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138444">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/280385abd0.mp4?token=cQG0Q-9rZGZq2s28RCZfGE4_EgFxevW_z6135syVPeSkULRe9q93NIHgSzkqzdF6N5vlbv5eI-uw_y9vknGnlrgi6NO8WXufDDlzvMGNHN1U2S-Rmuq9-lrIqnw8vrm4UMIdPNbbtqD5gmD6LeAKwgWRgoaTRMb23LFIZZqKB6qb7q1LuiJLy_PdFQIWZZNXtYGE92cyx07Q7rfYkcPBnR9X-5JADYOD8s6URewOZOfmlzAaeymHVcrBqppRSugML47C5t14IsJzLXiGDwR5_zQA-QGUUcNHO-zcULENrhJK-J7F9x07VHO-uxgHQR5rZwf1hDezxLxTs2cPgDAtxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/280385abd0.mp4?token=cQG0Q-9rZGZq2s28RCZfGE4_EgFxevW_z6135syVPeSkULRe9q93NIHgSzkqzdF6N5vlbv5eI-uw_y9vknGnlrgi6NO8WXufDDlzvMGNHN1U2S-Rmuq9-lrIqnw8vrm4UMIdPNbbtqD5gmD6LeAKwgWRgoaTRMb23LFIZZqKB6qb7q1LuiJLy_PdFQIWZZNXtYGE92cyx07Q7rfYkcPBnR9X-5JADYOD8s6URewOZOfmlzAaeymHVcrBqppRSugML47C5t14IsJzLXiGDwR5_zQA-QGUUcNHO-zcULENrhJK-J7F9x07VHO-uxgHQR5rZwf1hDezxLxTs2cPgDAtxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد دیدار خود با نتانیاهو:
این یک دیدار عالی بود. او اکنون همه چیز را متوجه شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/138444" target="_blank">📅 16:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138443">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
در جلسه امروز هیئت دولت عباس عراقچی وزیر خارجه، گزارشی از تماس تلفنی وزیر خارجه اوکراین و آخرین وضعیت مذاکرات با عمان ارائه کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/138443" target="_blank">📅 16:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138442">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFRqFp53FEzZVCo-De6pLVNsNOzpftmkGn7BoWCL-1tm3iRTx_4VD50nWC3sGR-TKOVFQ_R2_l0YJR_7JIS3uX_NwaZ40BcEKvWxjIRGsNb6-_ccLKyjSoopvelkdO00rnGjqv20bFeNqpdbw4L2XsTsyw98KF6AI5uuDh7YfBPywFi1R5tHzlS-uO_T1H4UFcsgJiVVo5s18w8VmOF3QE7UjUQJjyyZ3mBIS-NkoqMlBrNLSCnU2G7m5yg3LBFXCGcd57jZPYLAnDJih4p_Kz3kwepihR9Kmp1bs7NJPgHIv9i571b_zYpfSkB7zQPcRbjcnqIow-zElIeF1tBujg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت هم اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/138442" target="_blank">📅 16:23 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
