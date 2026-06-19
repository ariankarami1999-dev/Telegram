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
<img src="https://cdn4.telesco.pe/file/QaoBuVEt99TBzrx6dV-H0yO5HdA8xW7baC-_WwLhwodXWBpHTCyZILZFrbxYwmldB2jwWKjTmOgGXLovN5UzrxMqPG5oJbWwMjRgXnnVy6D8WzIWyRZyIG6z87rNv5Bu2SmxxhctnfZhvdLdEEh-jr_Ob95MdO-lgCPHE-V1f822Bl6A0liuAbiA7RaaWhfIMRhZf1PnEKULEYxLtT6fkLjhMZ6OIREXOkalBAZ6Hbrr7wQcdgpgxuA-fYmxqNvXtWIQbTSi9dwwMRG1hFWuDYa4DkrptynwXXUZrGZ0rjV9_boP5GJzjyiTVmeQ9HPmignyS6-veLKQ7WMeERPCoA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 170K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 13:44:06</div>
<hr>

<div class="tg-post" id="msg-78243">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">معاون راهبردی پزشکیان: تجمعات شبانه باید جمع شود. آنها سلامت روانی جامعه را بر هم می‌زنند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/funhiphop/78243" target="_blank">📅 13:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78242">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مادر اشکان لئو رو گاییدن الان تو کماس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/funhiphop/78242" target="_blank">📅 12:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78241">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kABgFYkt7yQ0mUnUn83awhITkBfu423t9waadZxRK_8GDAorcW6SsK2i7GPcSk-2o_g6EMoXoU0TwDADjf08fFD-8_u5AnxR_fpvWWCY5VaeWz5_wfV18XExTLEMWhIrfSQqgD051Eh16Bphi1I1_nIz6umG9wzNvtrTH_uwh0DKuTxun1iji6K65nkgCYtx6N6NWzNZvFLH1pF_VkgG7-m8nfKPN8L63WTPqmqZLDVW3Ek9BXEXaXg9pZ8Ocdcfbgp3QrtjbJMFUzrPFbQWHsXSR38hLtxDuzonoHJxEGx-0kDcVzdDV8a4VWOBBUx2K_ri05cuPGa1GgHPM_UtGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم ترین دغدغه این روزام اینه که بدونم این یارو پایین تنه چی میپوشه میاد جلو دوربین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/funhiphop/78241" target="_blank">📅 12:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78240">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">جنوب لبنان چرا منهدم نمیشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/funhiphop/78240" target="_blank">📅 11:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78239">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b546bT_-TiaZ4vLlz82O_mq6Fs2hiJBYsaKVX76W9a00WDUMZ7T3s4lWa4HdUvBsh0L8r5lrTrbaElvyLRlKMoFEoHOZx1Tf7-CVq9OYW3Y4ERi-XSngwGt5H7IsdQsTPuOxUKmmUbwKQqERUUinyzNZLwF0bWEFr0R_S8sHV5_niNjJUhbCwZy925wiF5sEyWq1oe-g5ET8mJIz0IWxRGbPyHgvEGvdrv2AG3F17ZP4NEb6YdZ3qKL27lMDWEulgCpaZBdFuuyD6Ob5R51ELbzDoCVKJ0mGLjPJRGHRHLeR-eQXaKwOSCQBGItcq3LSYhQmjaIK7f153a0V8plaOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبلنا که ترک پوریو میذاشتم آرشیو تو کمتر از ۲۴ ساعت بالای ۲۰۰۰ تا فوروارد میشد، امارش تقریبا یک سوم شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/funhiphop/78239" target="_blank">📅 11:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78238">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7wGi5ZtL15kd4buEiDMFwbkfLPWWAfmYJjQNsnT9OrzyNWvxR-hG7sllFkjhgvvPMonVqFqBwk5hQKpiVq8Pahnd2b_oeZ5usMn-OhSAFK06OeMHU_YE7W8FJFE8mUv6A4x82e3UNI-a8l9tN8hBbimYCuw2buzbQJZGLYkZgWCihM4pU-wNQPkSRBS_Iv0fIr5SH20gMS1AzrDx7-IJmZpzp9-ugF7zojPbC8VWK3sdLDqB7CPmTv0KvK0xf3JL17YfaiEdk5f2se2Dj9zValsH30HZDdPLIAfB7qzlZP_AljbTMdqOSq5Yt2trh7_LgTlWBcvzV6p6Tav7vZsZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای مادرجنده
💔
آقای مادرجنده چقد فید شدی آقای مادرجنده
💔
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/funhiphop/78238" target="_blank">📅 11:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78237">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/78237" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/funhiphop/78237" target="_blank">📅 11:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78236">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkCKu_I6KOmaOf1wx2D3Ny1wnURQtbhqGcKvKHuUwF3AQiO4D65AjTmL56qwoxavPJQs1RjBKi-Nxp5GhQPqicianlkUUnhJkRQoMrZUKx6ItjYM_LC8TmLbaHJp38aRL94g8gJ8nAkPorA4SWdcf0IbH6GyZEX2CgcQs4R7oHAPhSaQgSXqL40l4yPeJ3IbI7CaAT7shTR91QRIChfWss2eHe3VHJMPlvR0NkODo4YsNIGchx5ZueFigd8uJVA8A3CTMfacZ9zhe1szWdvKA1Uu8cpfbhR67HWVUSx-iMwvPwZ6jEZp_0FImr9AnWUIXHj7usGbfGFXo95cXIxKvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r29
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/funhiphop/78236" target="_blank">📅 11:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78235">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سوییس کنسل شد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/funhiphop/78235" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78234">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ولی سکانس به درک واصل شدن حرمله >>>>
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78234" target="_blank">📅 02:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78233">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دوستان کسی از ساعت دقیق پخش مختارنامه خبر داره؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78233" target="_blank">📅 02:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78230">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فردای شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78230" target="_blank">📅 00:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78229">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اون سازمان دریانوردی که اسمش یادم نیس: تنگه هرمز گشاد شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78229" target="_blank">📅 23:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78228">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تروخدا وضعیتو المیادین: هیئت ایرانی به دلیل ادامه حملات اسرائیل در جنوب لبنان، سفر خود به سوئیس برای مذاکرات را به تعویق انداخت.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78228" target="_blank">📅 23:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78227">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تروخدا وضعیتو
المیادین:
هیئت ایرانی به دلیل ادامه حملات اسرائیل در جنوب لبنان، سفر خود به سوئیس برای مذاکرات را به تعویق انداخت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78227" target="_blank">📅 23:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78226">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شجاع خلیلزاده به عنوان مادرکسه ترین موجود هفته اول جام جهانی انتخاب شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78226" target="_blank">📅 23:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78225">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-y9e07eDS1IA4ncIAWn8sMIigJeZgh97kEeoQ_LgK15y0LAw8ejpWS2RqkaYD1ZJEsS45zVUbcFjny4nuV3UkDovybqcAsdShsl_tRAJvXcjaVYwaad2ezRIk8A5v0RxkqY-TP30m-5XLHBoO6lCdW3eJlwF9VSufG9NywhyU1nZ-T75Fcqq9F8ruaig9LJTnZ1HnL50aLm409vJ8dfQtJ3WcoA0kAjLSPSkDx_wdca7ZyS8nZ2lXQDitGUVllQo1jLgxPGXX9jWNCwHKBSJxTCMVnpUenj2m7SIZQ_QyDsLP0AFhzkQC1XuHHI4r5ttc72ePHyAH9QczLhxBUsvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستاگرام چه داره پیشرفت میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78225" target="_blank">📅 23:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78224">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78224" target="_blank">📅 23:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78223">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWeera news | ویرا نیوز</strong></div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78223" target="_blank">📅 23:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78222">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuqi0Kww1Dafb3yw0ebwMeDtTIuY6n9uHiT2ADu7S_w6YyfFFXsGrWFGvfPUSnE5LjwYI58Zdr3aTuP_G8EThxMZJ9mjpEbXgNQnTxxnmB8BoVheNNqyqq0B1btqmUm6ok67yToK6b0pAKH6yTV5_M-lwm8gyJoJw2HfqZhlV-rtYHsB5a_kdLRePqfZk0G2SxmTg1gjjwP4xFiUm7tKbgMC0-oSkP60dmeYJhKgQWuxFanPDjchhi5l444acYHtuVvhgJLgzb_h16ZnC-tqfFb5d8GFnqw53KpglBtJ3B6DFFOanLFf1FLWoX5yWTycOXVVdN0fkiEH0j2ljq_XKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون ۱۰ نسل قبل یارو نسل کشی کردن یعنی این دختره خوشگل نیست؟ خار منطق
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78222" target="_blank">📅 22:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78221">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خب حل شد</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78221" target="_blank">📅 21:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78220">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">شما جنبه افغانستان ندارید، بزار یچی دیگه بزارم</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78220" target="_blank">📅 21:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78219">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پوری کیرم دهنت کاش خایمال نبودی</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78219" target="_blank">📅 21:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78218">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تنها کسی که میتونه برینه وسط مذاکرات تندرو های داخلی ایرانن، تحلیلای مرادویسی من‌باب نتانیاهو همه کاره اس رو جدی نگیرید، نتانیاهو خیلی وقته قدرتش تو لابی کردن در آمریکا از دست داده و توهم اینکه آمریکا سگِ اسرائیله هم از تفکرات رائفی پور طوره
ونس امشب یه حرف حقی زد، نتانیاهو بدون ترامپ و آمریکا(عملا یعنی بدون جمهوری خواه ها) هیچه.
تا فردا صبحم لبنانو بزنن هیچ آتش بسی نقض نمیشه، ولی تندرو ها تنها کسایی هستن که میتونن کیر کنن تو توافق بین ایران و آمریکا
اینکه مجتبی خامنه ای امشب همه چیو ریخت رو پزشکیان اگه نتونن جو رو کنترل کنن میتونه استارت یه درگیری داخلی بین موافقان و مخالفان مذاکره باشه
تنکس فور یور اتنشن تو دیس متر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78218" target="_blank">📅 21:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78217">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پی دی اف جدید مقام معظم رهبری در کمتر از یک ساعت دیگه منتشر خواهد شد  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78217" target="_blank">📅 21:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78216">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a862002bab.mp4?token=HMa-hmv33eHIqF1AeewIieO8JSzcjNPTV37-Qud1Pg9aegWab25s55QxQl11AnXDWKNoIyFGLTeTa0Tj3WqVS4wne1zYjnLRgs6RDzqFtgY-w73MI9d_ANepqFnTGzgeayvq9_IoOIQcQceWqEUDaGpT_3PI2a1P2dXQkwTjnyZX9_jZXsyPAz_VebuJwb1iOzepQTRlYWy268l8vKJXS4IB9rrJV8pnr-mdXD2FeKyqRSSJdHicCI3mCgTKM3oOB4stpBisr4cwSYxRxB4plOHtVJYaUJGL2y2TzHIh2_wvq4aJDHL9ylXv1xwyWZualOJfIy5FbPaBmEzeUXRtcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a862002bab.mp4?token=HMa-hmv33eHIqF1AeewIieO8JSzcjNPTV37-Qud1Pg9aegWab25s55QxQl11AnXDWKNoIyFGLTeTa0Tj3WqVS4wne1zYjnLRgs6RDzqFtgY-w73MI9d_ANepqFnTGzgeayvq9_IoOIQcQceWqEUDaGpT_3PI2a1P2dXQkwTjnyZX9_jZXsyPAz_VebuJwb1iOzepQTRlYWy268l8vKJXS4IB9rrJV8pnr-mdXD2FeKyqRSSJdHicCI3mCgTKM3oOB4stpBisr4cwSYxRxB4plOHtVJYaUJGL2y2TzHIh2_wvq4aJDHL9ylXv1xwyWZualOJfIy5FbPaBmEzeUXRtcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظریه داروین درمورد تکامل انسان
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78216" target="_blank">📅 20:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78215">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">محاصره دریایی تموم شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78215" target="_blank">📅 20:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78214">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پی دی اف جدید مقام معظم رهبری در کمتر از یک ساعت دیگه منتشر خواهد شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78214" target="_blank">📅 20:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78213">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYji21JbIu5BQbdj27Gy1USRQGyFQyr_f2wIJ6mRo0y1xFfhQI6R23M1F0JDUm5PYuYpSaEhBeIqUPtzkNYEzX1nn5Yvgw5g_7ox8h1sQsIlX8PqxvLHE_M19CiLlhDRjyEaQZd9-gvYuniSqqjXKxN1PJra20ehCinwBhF7JCueBFnBrZIgEmLjm3xVQdDOo5_99iABcsRfpt4vOIgwFXUJj0dcVjPZb7tdc-PzOoBXkZxNnR6KdOYJiMoJREpJnKppQBR_BkqLn9Dm7jgi5G19jS2nNEGr5HPqMZQ9NyVMzsmNMTGDRp7RI_WJBnvhrq1mC_m1nYPfnLmkZd-UJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتو جدید ممد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78213" target="_blank">📅 19:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78212">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7_FEa52T75--2v6nyTSTu2MeEPNNwF8VjUrb2LCEIFYz9XMYF6nktQ1di6V4sDgpwDFRm5BfwWTv4BhyxamqR7Yy6XRe6tdjX-yjo4cUh3KAPC3yi1PTPGLtjswQm9fPpIi7uUgTt52qZpEWIDRKijBYRZ1QnsFaE-MaWBFhS4pxOYs_i8YZu-6Db2K7AKtL2F96Z2rBUGmg8I2tbtiFwzdPH0XpzISoVaskgKUZjSfLIHnO8pcyZ75J1r-yWzr4hjPJIpfBaGYN0JmPTfd0rolXnagQf5PYYZsg9tUmp3gaTYako6h_8BWeHTl4XVkEvaoapES7P8H-5IBs4AdNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری عماد قویدل برای پوری
@FunHipHop
| Behi</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78212" target="_blank">📅 19:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78211">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klkcTpO8l-FGJNXt2YJXScF4aBKKfrMohhc1e7IErt2UwmkOUsXpD-PVToVIUgexfJjMC6n_53UxjA7zWeBCEPO-Tu3Jgh9NxgK4vO5Q7XlFwPMq59wHLIEWMX-IqX8oTR-7gRY1-59Ea2ugzdVk_48LL6VwPEu7NE5Wtu_ZaCm9t55DigK0bROjsQz3aZtdtGrcn4ST2EfjU6864dJjmVfoFG1_bqFIh7ZdcTNz5YrYipkZ8BOad3ANG0qt3RzUvS3PorBI9CfAYuLLuEHinXIwjDFFfY2zl6kYrFVJ4Xjr7xBqx0qcxSfb0Xy5MqoFm_lZDa0ZdW3veEeRfwBvCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4 کامیون ایموجی خنده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78211" target="_blank">📅 19:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78210">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تیم منتخب هفته اول جام جهانی 2026  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78210" target="_blank">📅 19:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78209">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDtWMv2J8FRy9fZ4WH0lJjoRGOfKiHVZ1rDNWQaDkRpEC1tuSoxv66-7_YIWKefKOO8m6Wf3YQpzlViA2Yv3BXmNC5rSw99Plm1Ihd-PEaUdkNYgAD8FIR19XnkWmct9u0AMMrOQ61zTWdj-lX1rZV6NXGP3wxFR5TxJYNmGjCcPP0mcvySjbbTCqE2dxVwU1LybYnuwImYKGqgi6IiY1vLw-2m6JZjLVjp3ZspOkyoFJwBq7f25PHHA5k9o-l3L7nTrR6w5JwHpvEKZ8SYztCXQTahLwGptQ6IifSvZCBeHp-hOoT7p3p9KH0Rck5OUXWyhEbjA68Pq9Lmt8-joTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم منتخب هفته اول جام جهانی 2026
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78209" target="_blank">📅 19:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78208">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTGFztXsyUYrrMCOdpCQOphlUbIsIvPW6TOTiAawqgSA89D4XHbWRBnHwml4LDwmN7IcwFPcHP115Dd589BGNOjhVpHVj5tBxBBSIW-sFQNtlgCj_xphUeL11n4znqcrQVI5-jK-Fata6zU4GnQDXTYP79DB3ou1W1nUbobXM6rk8fq3SUS5bsSFSLMqwBd24uspCtGazwT8ExallQF-fQGLucD3Owv_hi1GUkyWDHpKJlUTD85KzXWnQY97rX90tDd_0COAGo_x0T9KeVX0-vq_nct-R3HyygkmHT-PMIS9efhfRuR6gMTxBomGTsStCC5E6HOHZBIfqwVuQcRSUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند ساله ترجیح دادم پول سیگار
بشه غذا واسه حیوونای تو خیابون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78208" target="_blank">📅 18:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78207">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گویا پوری و تیمش این مدت توسط موساد تحت تعقیب بودن
🙏
@Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78207" target="_blank">📅 18:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78206">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QowG3OdZACr1ULVQwMsQRWn-2jufp18xMtZXYCmOTCOpi7TFX0B7zVYC_Gkd2LgjMsW3abDwcoCOBVp4pxwLugQBglG7vuokMwluK1S-KElq67TrthcebeH-N6XaORMeBQGQSBLTQFEN8PRgJIQ_paNuvKdLYYUt36hGBSLcR5uUL3s3BgAfakkAG1_lu9xsN_uU7qHnGVjaFUYjG_pDSZDMdZ1Wvnw9Zk36iWrGO0xm31ak_CwGACatGLLX42pD69NBgzBtNZmz9iuyW_Ri8uVsZC5msjGSHJDGSVEKoNQ77aALZHxe95dWbuM1NmxLz4XM9j7dh6X88P3wg7svqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از عجایب جام‌جهانی
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78206" target="_blank">📅 18:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78205">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLk</strong></div>
<div class="tg-text">بچه بودم دوست داشتم مثل رونالدو بازی کنم،
الان رونالدو مثل من بازی می‌کنه</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78205" target="_blank">📅 17:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78204">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLfAR7p287HmiiGGT_nZ5mMBX3AcEIweRufz8vD7rMOYfajn4NjBXyWq1jIZodcE909PCINcHf_vvXJO0n2-21FKJsncOkGnfOHvaQ6TLbPpxM0z7JMJ3zOBzLgYmuJ1_1CY9qu7bDLkXE5DqmfH21iY-ZdZ6K9LVINbcJ3Q1ZPln9cp2-reZc9kZhzUQl1C9zr0zLU4P07NbIADHemGsRcwxNoyT_F2pYVh6PvS_WZqx-4Wmoo6qlmKBbme6h4FRnrHwJkSGa9uF9rq-axVTU0fqXenaUrBYMVcq0dKUWtPt0cOGBdhZ2jAe0pFW9CQFQMpdJiXYq_S2nN-GGGsrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای تاپ دنیا توی اولین بازیشون درخشیدن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78204" target="_blank">📅 17:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78203">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78203" target="_blank">📅 17:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78202">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYE-3BbXA5RKvLiFDuTVMtqEjhfdmSJDIfQD094nFAn_AdsDmJldmIVAEL8CerIq9LiWnuFFR-f7sSxlEHXzVzqt3_f1af3yurfZh6pgjrzEFXRemB0oivI_h_MDpi0VZEz1kCw8LRw_3RmwmbKWBLg8JIfTOsJhBLbv2p1lybKpJaCfsoCxWhwK6HRLp0tuxf3up677PWegmosPlZGIFfaaq3AWhQvxoW6lzBsBxqfNPeETYEvG9TWK45x-SLq5IR_161NLSUH6QJzA6W1wuJnTRlcOiBX2_x-34jfKmjJARIFugjzZWFd39og-5X1kttMFC2XtR1sSrCJOmatJTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g28
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78202" target="_blank">📅 17:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78201">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گویا پوری و تیمش این مدت توسط موساد تحت تعقیب بودن
🙏
@Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78201" target="_blank">📅 17:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78200">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2CDLb5hQxEOGleWDR9KYcPC716oa5IvbCfzqNi3evpV3hOocrjIRIxj278CqpEzWMlJPUdajWJFSzBmoHzUHkQxBixSAPLBwY_upzJ7_1Go8S5jV56qHB1wTf2peB-ZgH2A-5FMNct2X__5DWmvm7JkU-DlTyQ4qu006IDIKNOZ7jqqPRYJjMbbwKGoP8lrsnpg10DsPVXr6G7oQWkhOkVXigd7_d2JnziS6JZD8frngYf89vBuL2cZfIWWcnbIoTrgxBydZknJ1JdO9u7NOmp_5WhXCWHOR-Njx36Q5RsV-EyJonsGWvhroI5W_AE_4iUFQN1JPqyNi_rpKnXUZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید پوری به اسم سرپا ریلیز شد   YouTube  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78200" target="_blank">📅 17:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78199">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ifn9JWyVd1GbvnbNosnxeiky3ueb1ukVeW8CBE52ssdPNcn0NY399RTuGWF2lGSYNz_AZheoOzYRDzTK7GwzTTjs9aG2OZow-Vf3ZnpT37a7oFjW0Ac10_0V7QezGHduKekpGljzzXk_dI91yjILMVdrYo9KHibKbLdR-kdcOY762gVqA2aOP8es8W9j2ij9nXHsar0uCTWJ9yOio2XOtR-UL4mHEvUXsxqNVp1RFT20XfMOyQ8fE4IVQ84tgP4Be0fo8OrxucNCOtYCb_RvSnxpvx2eJPk0lOy6vN-rqGLmsXG6NH488I_ldgjz_WBezPtoa1UYbNhOnV0LKgtH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید پوری به اسم
سرپا
ریلیز شد
YouTube
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78199" target="_blank">📅 17:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78198">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وقتی مردم ایران صدای بمب‌ها را نمی‌شنوند، ناراحت می‌شوند؛ آن‌ها می‌خواهند همچنان صدای بمب‌ها را بشنوند. چون آن‌ها می‌خواهند آزاد شوند.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78198" target="_blank">📅 17:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78197">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ: فقط مردمان دیوانه میگویند کشورم را بمباران کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78197" target="_blank">📅 16:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78196">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTSd382Zm1Raz4X0V-p8G9rqJHSqMhxYs5yZesM6TH_Wz2JZhnntSX9D3l4npo3KiEbGPyIYgw-Vk5kT_fngVE9HIb7Ga9StHUibAgdF8WfuDhy61MDSrAa797zYwzy55DqIUvv3adQEY2-oSHwy0jIJAQm0QB0wHfVcBhSJoV_ncSuf3_ljr1p_CAiFKphChNZDq8i3qjFHKRUErTr2xAyvL8yvhKIRzV9XkxaLutrCzuj6QMHQXgLe4PE5viOFxzmEJQZvniOGXpQcFAvRavoIyDn5duJ3P3jRmtp7QwBR6nBt_NCk5Sd4rYu9yirXB1gR9Wlujm1XPfO4J7C4yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78196" target="_blank">📅 16:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78195">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKUo2NzpYLpgKI4vX1uoJtNDMKXN2DwwgFHpET-99ZwH3r8IPQDTtG-bzmYuYMhWQEsTXAvj7Myuu7ck5kJtAgFbDjX0C8z4eRcP8qUAUtrQd39vC0p4Ic_uFFDAE3FBB3Sy6-UeZ3JXq1hOaZwlBhmumTrt94qQY7dMnE87LVprflyth3hEe_jXNhy2dtJeT7SobJ07Ru9AuRLz5xXXMDRjyzgMs2gDETJWd_aN_Uf_Dxb6AqVTcdrTH4PXDDXU4PQtrhsZc0KAQz3G9GxjfocCbfvbUgwnvxtLfWwysA6k8wpRN0iZG7yd7nwLlkLm8qohhe6DbIpnOHJEmvX6Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سنت خجالت بکش کصکش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78195" target="_blank">📅 16:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78194">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پوری میخوام برم بیرون، سریع تر ترکو ریلیز کن یکم بخندم برم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78194" target="_blank">📅 15:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78193">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromuıǝssoɥ pɐɯɯɐɥoW</strong></div>
<div class="tg-text">مهدی واقعا افغانیه؟ آگه آره که کیرم دهن صاحب کانال که یه سگ افغان و ادمین کرده</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78193" target="_blank">📅 15:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78192">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06ef661660.mp4?token=J4wW-NudWGfZrFMmTrXnLDuh9-G-8CtaCl5odPbOjQfaJPsOBJH7F4JnBLmJHorfn2OGm4uQYF4OxH7UL9wabVCdZkhEt3rS3tC2Oe7O2xle5J8tU4F2NoXZeHQ6xlFE3SOyswEHPCqnFNR22PiJpds7Yw3cmw-2c_X0L1itbnAe3M9F85J7wqHGdIGu75GCuWSHW5EOUfbiqiwmynYoR3VZmJNZsyuhp4l6e8C1G1I3eRh9f8hUBiklPQhG9GxDV9GjrZIbhJeSSKGbbZfgfMC9QtDSa0Dq5qvWjj2KZacn3vjIQtZXhCRKvQNo55YbV8ufKcDjyipqejkfJaiakg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06ef661660.mp4?token=J4wW-NudWGfZrFMmTrXnLDuh9-G-8CtaCl5odPbOjQfaJPsOBJH7F4JnBLmJHorfn2OGm4uQYF4OxH7UL9wabVCdZkhEt3rS3tC2Oe7O2xle5J8tU4F2NoXZeHQ6xlFE3SOyswEHPCqnFNR22PiJpds7Yw3cmw-2c_X0L1itbnAe3M9F85J7wqHGdIGu75GCuWSHW5EOUfbiqiwmynYoR3VZmJNZsyuhp4l6e8C1G1I3eRh9f8hUBiklPQhG9GxDV9GjrZIbhJeSSKGbbZfgfMC9QtDSa0Dq5qvWjj2KZacn3vjIQtZXhCRKvQNo55YbV8ufKcDjyipqejkfJaiakg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریچ یک کانادا و حومه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78192" target="_blank">📅 15:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78191">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">راستی محرمه، پرچم عوض شد</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78191" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78190">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انقد همه پرچم گذاشتن جلو اسمشون منم تصمیم گرفتم بزارم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78190" target="_blank">📅 14:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78189">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRq72pWX_eM7Sco_XCXw75iC8CFsnXZMZFZEddqa0ZeXF4gHspuxl1yGnr3E7S74OBjGYprQrg9Szjs0KKbGOx_PShZuZe_ecBBmck_SIyr8lOG2PGPKVcQXd1kRDO29UC20Crp0kwrXityeBXoOqTcpewMyUpO8WhEZiEiaM6OZsJNAsvDXByI6gYzrpq03KA5Wz_PSWaranqFFncMMlQZhyQxAXfwH6MaXNTm87JZurP2ApU3kubBSQPfj626FiqZ_KiFCRTX9Ol5qnK3Br09WvU5e8fjWFgieUR8F5yPZKFZmac-RpawAeuWXqWxPC7_65CHVVU9pVqqjkHKm5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت اوردم براتون که توش میتونید خودتونو درحالت امضای توافق با آمریکا قرار بدید
پرامپتش:
A tight close-up mirror selfie, black and white, grainy backstage aesthetic.
Subject 1 (Foreground): A young man with messy, sweaty wavy hair. He is wearing a tight superhero suit with a web texture. His face has realistic battle-damage makeup (cuts, dirt, bruises) and he looks exhausted but calm.
Subject 2 (Right): A girl leaning her chin heavily on the man's shoulder, snuggling in very close. She is holding a small retro silver camera directly to her eye, covering half her face, smiling.
The lighting is harsh and direct (flash photography style), creating strong shadows. The background is cluttered with a hanging white t-shirt and messy towels. High noise, raw, candid snapshot.
‌
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78189" target="_blank">📅 14:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78186">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کصخلا فریب و فرید دو تا انسان متفاوتن  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78186" target="_blank">📅 13:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78185">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کصخلا فریب و فرید دو تا انسان متفاوتن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78185" target="_blank">📅 13:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78184">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lche-75mK3y0Bi9vuLO19mSEIgd5vKDs79mw9oer7awVwkzAvRSaYv6evvr60VsrDsPYzAg82S5STZFReNdD3CglCuZEfjIBqYqhOBXxNeC5Ep4VFwgNl1WGuTX1aZRubrcu8GyjM7Cu_TyOziXxbKfh8IrnYJvA0Tz5uj8X0sFkOKyfNVOfnwcNEy9NVs5saGS1TbeVGCxBkJUaIubX0pb1mKAtpfPvvOvnza8XweECT3ybCuvViw5iJ8MGr8eqWX9zogy8a5dlx9qojig-FeVUadJ4PhptYF5srzaVkUnmmKxvibHVBiWFEhjy-Us1EVdTtN2Jsv-nw3u6M2eWOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78184" target="_blank">📅 13:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78182">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خب دیگه توافق هم امضا شد و مانعی برای سخنرانی مقام معظم رهبری در ملا عام وجود ندارد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78182" target="_blank">📅 13:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78181">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترک جدید هودادکا به نام Best In The Game ریلیز شد.
🎵
SoundCloud  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78181" target="_blank">📅 12:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78180">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqJWH84wxNGtZP-yJyaLj__5dNaLpM1Bix7FGiGcDNzGw-s814iKl8de6xebPqvwGFJdzqNvjaMlnkCn7hQ29VsmBfipUKG3Z91wqcEj9Rn6JJuxbJLBzgxNlsqhqEs9cDAFbkGr_JZq5dF21h5iF_xnVdPOYxJc5xTmQ2MW-1mOoE36E4S258v5IUlNB3bwPqfl6I-XW_ME-c8UhWXtn8SxG8dDvUZudtV12CXevRgcVibUmKjJA0f54pYYEt9jZOJm0vq-76_Ce9hyVs1KAG50XfWBQyzdrhv3yjbhcVWPamBsKupz8tdd92LLoo-_vMEApb_FxhnuV7RziyOLBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزان ببخشید من یه لحظه حواسم پرت شد این قسمت از بازی شطرنج مرگ و زندگی رو از دست دادم، لطفاً راهنمایی کنید این چندمین تاس ترامپ می‌شد؟  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78180" target="_blank">📅 12:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78179">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عرفان چطوری میتونی انقد کصشر باشی داداش</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78179" target="_blank">📅 12:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78178">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آرتا:‌ کصه بشینه نمیره عین جمهوری اسلامی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78178" target="_blank">📅 12:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78177">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترک جدید آرتا، کوروش، ویناک، عرفان و کچی به نام میتونی مگه؟ منتشر شد.  Download Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78177" target="_blank">📅 12:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78176">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترک جدید آرتا، کوروش، ویناک، عرفان و کچی به نام میتونی مگه؟ منتشر شد.  Download Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78176" target="_blank">📅 12:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78174">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHMCOISKP9i63-NJ_q_46TrIiSxIWP8Axdfg0upCKz3MowvEH20iNSiKEhfOkRRIv8YRCVHvYI-pyBtq4eGzBgW6sN7VKlg04tfPMDwyCxEIIAb1Zo9M9E7h7lVZKdZROzfrShOlluNiJEri4LeuWjbHVMNO7Yn6tpYKe7CcStHwrRY00y4LVQgWlYwAUbbwtovwYpTyv_OyxdyxphTX6sRmSR1eV7r1gpozX2kj46qEy8WSW3tTdOhr8eEfTeG0qP5Wd-Y_4C_0VfHw0bYurwU12gUYXUHFwNz_62ullCYU4W6a0BZMsz_4-ThfhXZSIyMM6MCEou7A82BHcDnhjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید آرتا، کوروش، ویناک، عرفان و کچی به نام میتونی مگه؟ منتشر شد.
Download
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78174" target="_blank">📅 12:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78173">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آرتا، ویناک، عرفان پایدار، کوروش و کچی فیت دادن</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78173" target="_blank">📅 12:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78172">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBtC3erAJoTjVhv0tJQP0-ap3yzV9xTsbbiqr75xijlEJeLNeWGnQB-RYA3TdwIGMc75ZPuhej-l9eFyYDj0vTpycUxvlwyssMJ8QHdT2TrDFpdUX9TFzFSz9y2fXMZ98JEfhe9Z7qCMbJCKGRWaOLm-LqlfQ2aWuj7Ov2aeCDMfct6KZ5AkVi90K75WoO2UNGkZ8sp1sf2gQaMOzoqSOe1yevcd0HMnx4dh_PrSsc472Aq1Jp-v8A2g6xRgYbIy97eU5AfEjJrwi5wFlmF7eJv98y5Up1B8KeZLbtNe0UeHjLd7F_0aO3WwnLnv2edUNXkSqVws8R8yrVuolYRaiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایرانی بدون خایه نمیمونه، بالاخره یه جفت خایه پیدا میکنه برا مالیدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78172" target="_blank">📅 12:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78171">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">آیت الله سید دونالد الدین ترامپ(دالگخیز): عادلانه نیست تمام کشورها موشک داشته باشند اما ایران نداشته باشد
آنها باید بتوانند دفاع کنند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78171" target="_blank">📅 12:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78170">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">رائفی پور: اگر میخواستین توافق کنید قبل از ۹ اسفند میکردین حداقل رهبرمون زنده بمونه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78170" target="_blank">📅 11:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78169">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رائفی پور: اگر میخواستین توافق کنید قبل از ۹ اسفند میکردین حداقل رهبرمون زنده بمونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78169" target="_blank">📅 11:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78168">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شاهین نجفی نوستراداموس   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78168" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78167">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c40ff98049.mp4?token=NZazm3IAekpeHDprNdA89mHTCwXYKWZSK-MdQfkLR1d7G-Fm7ItBKTUcwUhlmK67A2H62ay-LbxQE2LWa85uw7kUy_RmYt_fC7-UFdM7-8LAiDM3M_8a25Whc5q41k7g3NSK5bBEIo4fBuZ4j62NzjffrudSCZQWpu-IFYQxuSZRgNqsbcrIqSxunHHFXBNMNwdN-j5RKgSr_T8e9iBoGzwSY6Z__tVVIX0DzZaWUxJFXu-M6lTYdWfLhKx99Gg9bTZ-YlfQ1xNfD2e4DQN7-vFmafZbU7P9nxu-jIhht4AYCoHBvpERLSlkOWuTUCsi-F9mvZTelyV1XQJvIaRS3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c40ff98049.mp4?token=NZazm3IAekpeHDprNdA89mHTCwXYKWZSK-MdQfkLR1d7G-Fm7ItBKTUcwUhlmK67A2H62ay-LbxQE2LWa85uw7kUy_RmYt_fC7-UFdM7-8LAiDM3M_8a25Whc5q41k7g3NSK5bBEIo4fBuZ4j62NzjffrudSCZQWpu-IFYQxuSZRgNqsbcrIqSxunHHFXBNMNwdN-j5RKgSr_T8e9iBoGzwSY6Z__tVVIX0DzZaWUxJFXu-M6lTYdWfLhKx99Gg9bTZ-YlfQ1xNfD2e4DQN7-vFmafZbU7P9nxu-jIhht4AYCoHBvpERLSlkOWuTUCsi-F9mvZTelyV1XQJvIaRS3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهین نجفی نوستراداموس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78167" target="_blank">📅 11:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78166">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2kwgJ-3sa1DGI-y9NizE47kIK2Bsn0kjBRxQAMJN4HX5XoX5LvgOXl3KrFu2RMBaZgxTzw7n_OONZTRC4gYd_TBfB3OFGZ4LDpn2MMOwqTaNdcpn2v4XDD20ndFiUFALpcMBJmYjKO88f350yG7jAp8FLTE-Wh3wC4wGcf3wjrczvGbn3Ew7JqhoPc2cD5GJmZlwqdim18593QIACzP4Ad90U8mInjbOibpux7pVSdZOwj7kMYytJZlWMisrt-IxYUPgEAKkZ99f_0orzQAdQRHZ_oDMxO4GbHQs-CVOzPAmi1rovfP1v4EnISCM9Fh_Gd7bZL-0uvgOWiHp8gUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین ها درحال درخشیدن....
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78166" target="_blank">📅 11:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78165">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/78165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/78165" target="_blank">📅 11:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78164">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wjtwokid3OvpE_9gD1uC34LG5Qyy8KtJDuc_DDRXT7ABFFnl38OVQHAikNMwZYIrIFEETtjOQZ4WeKLkZP14LpkY8hzOUh2iRFbnZDdwN54wBmUJNnsMHRJOB9n73Mtucc5o-MWFCthyP67EHk8LCUlTOXNyGRJQ851SveDswcdjxk84eirCIPO6G5I-XnDxXEejhmYeJ1KSPyW_JZwCv6agcB2ALlEa4EPwGfnlpWCx0HK_MiAD2iCtBPsO16zhh5DiGaD7iQTSQcpHpz49ntrua3UIyKuhvvOMtxBtwbisGZmhrBOuZYyOuCT6kj32xCZzK-15tNC-YkyympCsmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r28
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78164" target="_blank">📅 11:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78163">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be730c80f1.mp4?token=VkmPOGUv1NK2YAtKicxpUk5b2xXVt_DxLTZr7guy1VKR1W6floqrVKDpYPoAgA-6GkSUKrP3S7LksOY8UsIdvmdzw2QEsB3GKkoqmtR0HbeBs2tvn5mC6B2bSlUSu-G1aJBSdKOTEJ4iEuqgJwKBxpkx5nIZpxi-CZAJot-piw0fQYZEKCJ5_mBplTCoLAm9Nlw65-K6XQwzPhJZLUJdlPKXeo-R1vB5eikliykure5EySAOM5SnJZfqINLmFil1Y7zAPLz9B_MG13X_aDD38pIitYIIFnzq8qKJC1ibN6ecfaAhae-lQIwnhKs5wdv32esWSgq04lG1pIfqQETsQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be730c80f1.mp4?token=VkmPOGUv1NK2YAtKicxpUk5b2xXVt_DxLTZr7guy1VKR1W6floqrVKDpYPoAgA-6GkSUKrP3S7LksOY8UsIdvmdzw2QEsB3GKkoqmtR0HbeBs2tvn5mC6B2bSlUSu-G1aJBSdKOTEJ4iEuqgJwKBxpkx5nIZpxi-CZAJot-piw0fQYZEKCJ5_mBplTCoLAm9Nlw65-K6XQwzPhJZLUJdlPKXeo-R1vB5eikliykure5EySAOM5SnJZfqINLmFil1Y7zAPLz9B_MG13X_aDD38pIitYIIFnzq8qKJC1ibN6ecfaAhae-lQIwnhKs5wdv32esWSgq04lG1pIfqQETsQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
یک انسان خردمند در ژانویه ۲۰۲۰ گفت: «ایران هرگز در هیچ جنگی پیروز نشده، اما هرگز در هیچ مذاکره‌ای هم شکست نخورده است».
ترامپ:
این را چه کسی گفته است؟
خبرنگار:
دونالد ترامپ
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78163" target="_blank">📅 08:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78162">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nILx-KGWoSuFn0NTkCqvjN_LqHOfLg4QEuAKMiwWp8ExJkfrBmVBHp2-P6hYIWvK1Ia93LXtURJIfwUDuM7GZf7yzpzn7-zmOygfTqYwxt80Um0_hS7qoYFoTUAEIfDcDmwFWlLlM7DR67GqDbLe52OfJbC_evZ9yTLh9NQg-j16deGy7tiixDzuLA9KPplGrb1FI7PHZvFHJ1YyK651uWQo9lLjr9NKTsFz6fAeeqcGasbFOoCePNMH8xP4VDXI8WF49yyqTTqyzT8jjCFn73LgFvkQQy-mvOn_1ng5LPvzMx3kizj0CnxgzdXShblsunvCRtCGexDbQVZOEuMFeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزان ببخشید من یه لحظه حواسم پرت شد این قسمت از بازی شطرنج مرگ و زندگی رو از دست دادم، لطفاً راهنمایی کنید این چندمین تاس ترامپ می‌شد؟  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78162" target="_blank">📅 06:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78160">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XyOdPd_s5gQKnXZzPLVuZ7LcR3LBSUMQhYC34zbBFad_faQvJxebx4PTAS0lBs6w-TQrgGuWZaslHPX0Nljfj13gSgqjj14002rqz6egFgba2MKHysEeXDT3-WXumLwIWX114Gb2QgBvh8gMltyX5U4Pg5G8iD-U10NUya4KDch8pYxuptAjuVMTIPvP350H6v8Zh7qaKrcJCdguh1cglBrM_gKjOp-mXOceQ62XMgPdPcwWA1m9Gf7yUR5gb1ldPy1ydomA53B0z1vEMkhYWBOqLPIr9MWM8oKK0_9hGZva8E1zPpZnGZtakdn9Zew5Vxym9kZZqK1VmqfKcwT-0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bMvoF_J42VdlivVSRH6Y0DNuDJvzzn_n38rr10cYKMbTuKNmNyq_Bmqym_Uoddz9ERMTglGTGFIb9NkpCMAPtm-QcGITsCbymqC543aS3PwhFonQH5X2DMo5cxyeGjyfCk31xOX_8MwVccQ1FPS8Ikm1iyt1_fAHmrcDPlg8fUREE5p0FggrGGCrVK2dJxLiRw0fLlDhEKjLyT8PeycQxTVlbM0qNknElUvLC22qX5wsOrfYnFQOqBjuPJlBVydEgrDUKX8IbagRFS8FwhHPiNJFI8P2GoUIUv2DTIz3Ly7jvZjwmsG6IQEceszQa64Pvi1ngF0WJ4Md5PyPpbvWZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزیزان ببخشید من یه لحظه حواسم پرت شد این قسمت از بازی شطرنج مرگ و زندگی رو از دست دادم، لطفاً راهنمایی کنید این چندمین تاس ترامپ می‌شد؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78160" target="_blank">📅 06:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78159">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">جی‌دی ونس دو سه روز پیش اومد گفت تمام بندهایی که از توافق تو رسانه‌های مختلف پخش میشه پروپاگاندای سپاه پاسدارانه.
امشب خودش از رو تک تک همون بندها خوند و تاییدشون کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78159" target="_blank">📅 02:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78158">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سخنگوی وزارت خارجه:
ایران دو قدرت هسته‌ای را که توسط برخی کشورهای دیگر نیز حمایت می‌شدند را شکست داد.
ما شعار نمی‌دهیم؛ ما واقعاً یک ابرقدرت هستیم.
روند تعلیق تحریم‌های نفتی از امشب آغاز می‌شود.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78158" target="_blank">📅 02:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78156">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کاخ سفید جدی جدی حسینیه شد؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78156" target="_blank">📅 01:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78154">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رشفورد چهارمی رو زد و تمام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78154" target="_blank">📅 01:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78153">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خب طبق بررسی های میدانی و حضوری تیم من در ژنو، تفاهم نامه به صورت دیجیتالی توسط پزشکیان و ترامپ امضا شده؛ ارزش قرارداد سیصد میلیارد دلار با بند فسخی که بعد شصت روز فعال میشه.
Here We Go.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78153" target="_blank">📅 01:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78152">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">میگن که تفاهم نامه رو امضا کردن ولی فعلا بچسبید به بازی انگلیس کرواسی این مهم تره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78152" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78150">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">عجب سیو پشم ریزونی کرد گلر کرواسی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78150" target="_blank">📅 00:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78149">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بلینگهام گل سوم رو زد برای انگلیس
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78149" target="_blank">📅 00:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78148">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VC8gruY65DKYUooixEcTNK2lh7L0VqmFsuXBspeQP7YMoSHWz1wlgknzSQdkBtGRQzJ3sKXezr58VwM7EdE-PauP6Ny3RuABZifccj27PbcQqAbfcNArslefAhjfhHHChkvvHOhMnU8lBLhyhw7PwA4o0tjK1R9tZoaATAf-cIVzeQdm-QSxDsTa8ZncW7NdELd_sjs0I9QFkt8XWVTtF2ZRpiE3qX1tGSryUvQ_SkiF6kNmWbNTSZU7oBUjEu3OY1-JlorJU2NmQ1QMUB81v2eHnmRfSFAnORl5Htvy43sXCrCO0TEgZHyAS48dMzlMs_t_4SVxOMoytaVvSppFMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمتر از یک هفته تا منتشر شدن فصل سوم سریال خاندان اژدها مونده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78148" target="_blank">📅 00:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78146">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBtCakjxHwAyN3c1Irjsasfzf4FID26orqPPpJmFIexes1gqcLwkKMylsRLkY-7H8zTbIFYWINHU8vEeqt5Xb3IOjt-8SsAjx1QxuMOiI9dwYNgqC9lUZFkt0PSBGR1a4B2aNPtpX6jTyhXW1tVSXiflcZ1OST8ZMY0q1ciPtwC-6c_X64f10lOWKwgF_PDEpV72db3mXDHru9pu7B4akkEcoQ6mDfmk38_QT8_mAPuyNv8Jc52B00bazJ-l_Uo4Map5sYtRZ1jASNg77h7P-ky9MmJOuTxu6hjkq_qMyBNTmXUNat7YaSYzyDPCZlvUXkght4L54a48XoEvNH0gFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری مامان پوری از مهدی طارمی.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78146" target="_blank">📅 00:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78145">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کرواسی زد
۲ ۲ شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78145" target="_blank">📅 00:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78144">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مثکه متن تفاهم نامه منتشر شده ترامپ قمبل سیاسی کرده برا جمهوری اسلامی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78144" target="_blank">📅 00:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78142">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">این بازی داره قشنگ افتضاح بازی قبل رو میشوره میبره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78142" target="_blank">📅 00:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78141">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7dd58a539d.mp4?token=o9hKEHl9LY5nkIHRncQoAghiKkjDSlahgxc-GVA4ICCxaFosCqnOfE1x7diQ7pIeIQNHMk3uEkT9cZ7Dy1ErTJs8I4VSqSo-0sJWw58-14Fq1Dun4M_tDEuztjB_DLGhhB44X8YF6cwZS-7lHu5Xto_RWielYcWe1zvd5dHriFzUCreAiJkbgfQETOL5xOqzu2L22nEz2k6x1ZvMiaEPySQZCpyvtSULiHlhBGPWhuMANzJbT3jJUKT5ve_UOCbih5BZzc_8W2S6wPLzf_oG98R8RAB9LjOztVDfX7lVWEa4DWEU4s4YIm82-7FY3zVpI5OtBdnoYzcH9BNzIpbqWw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7dd58a539d.mp4?token=o9hKEHl9LY5nkIHRncQoAghiKkjDSlahgxc-GVA4ICCxaFosCqnOfE1x7diQ7pIeIQNHMk3uEkT9cZ7Dy1ErTJs8I4VSqSo-0sJWw58-14Fq1Dun4M_tDEuztjB_DLGhhB44X8YF6cwZS-7lHu5Xto_RWielYcWe1zvd5dHriFzUCreAiJkbgfQETOL5xOqzu2L22nEz2k6x1ZvMiaEPySQZCpyvtSULiHlhBGPWhuMANzJbT3jJUKT5ve_UOCbih5BZzc_8W2S6wPLzf_oG98R8RAB9LjOztVDfX7lVWEa4DWEU4s4YIm82-7FY3zVpI5OtBdnoYzcH9BNzIpbqWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خخخ:
وقتی همه‌ی کشورهای همسایه ایران غنی‌سازی دارند، منطقی نیست که به ایران بگوییم به طور کامل غنی‌سازی خود را برچیند به گونه‌ای که برای تولید برق اتمی هم غنی سازی نداشته باشد؛
درمورد موشک‌ها هم همین است، وقتی همه‌ی کشورهای خاورمیانه موشک دارند، خب عقلانی نیست فقط به سپاه پاسداران بگوییم موشک نداشته باشد.
بیایید کمی عاقلانه‌تر با آتها مذاکره کنیم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78141" target="_blank">📅 00:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78140">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">شما یادتون نیست ولی دالیچ یزمان کنار شفر گزینه سرمربی استقلال بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78140" target="_blank">📅 00:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78139">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کرواسی لاشی همیشه جام جهانی غول میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78139" target="_blank">📅 00:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78137">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">انگلیس چه خوشگل بازی میکنه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78137" target="_blank">📅 23:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78135">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ: ما حتی ۱۰ سنت هم در ایران سرمایه‌گذاری نمی‌کنیم /از یادداشت تفاهم، بد برداشت شده است
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78135" target="_blank">📅 23:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78134">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vmd7aPvMvpFIoB3mrwBpbG6vYi4fLFG7vYJMH1Nnj1WvC0AaqPsjvnGoot7EU4FxBYJ_KCz1mtwMQGfdcWbYicIbnZCzwg68QdyZOqhTDHpmAfKRc9ZHR7CPaTZs85W31UCNKyVN-d2LS3dLOY-MOWBkFJS_Pir_d3o6bTy6IVaBstlbUpTxwEfzal4NGgZ_0g8JvbxUgDsMezLPWmllV6alrT7WKXjoT4hMJHkw0zy3WIpa-XP8cQ3-EfCSinw_jyfQ6pwUCqd0u79Cxh7jTVqXO63jriNyyfeOeMPYGbXyURYweJOCo3vPPzOoTyIE8yW1393X_R8mhEbEE3Oy-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکوادو
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78134" target="_blank">📅 22:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78133">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">☁️
✨
HappyCloud
✨
☁️
🔥
تخفیف‌های فوق خفن
🔥
⚠️
فقط برای مدت محدود
⚠️
+
⚡
قوی • سریع • پایدار  +
🌍
مولتی لوکیشن واقعی در ۶ کشور:
🇩🇪
آلمان
🇳🇱
هلند
🇦🇹
اتریش
🇫🇷
فرانسه
🇫🇮
فنلاند
🇺🇸
آمریکا  +
🛜
تمامی سرویس‌ها آیپی ثابت هستند.  +
🎛️
پنل کاربری اختصاصی و حرفه‌ای…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78133" target="_blank">📅 22:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78132">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">☁️
✨
HappyCloud
✨
☁️
🔥
تخفیف‌های فوق خفن
🔥
⚠️
فقط برای مدت محدود
⚠️
+
⚡
قوی • سریع • پایدار
+
🌍
مولتی لوکیشن واقعی در ۶ کشور:
🇩🇪
آلمان
🇳🇱
هلند
🇦🇹
اتریش
🇫🇷
فرانسه
🇫🇮
فنلاند
🇺🇸
آمریکا
+
🛜
تمامی سرویس‌ها آیپی ثابت هستند.
+
🎛️
پنل کاربری اختصاصی و حرفه‌ای
📦
20 گیگ --->
❗
فقط ۴۹ تومن
📦
30 گیگ --->
❗
فقط ۷۲ تومن
📦
50 گیگ --->
❗
فقط ۹۹ تومن
💎
100 گیگ --->
❗
فقط ۱۶۹ تومن
💎
150 گیگ --->
❗
فقط ۲۳۹ تومن
💎
200 گیگ  --->
❗
فقط ۲۹۹ تومن
💢
تمامی سرویس ها
۳۰ روزه
و
بدون محدودیت کاربر
هستند.
✅
خرید فوری از طریق بات
👇🏻
🤖
@HappySmileVPNBot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78132" target="_blank">📅 22:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78131">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یه صحنه گلر پرتغال هم اومد پاس به عقب بده به خودش اومد دید خودش آخرین نفره
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78131" target="_blank">📅 22:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78130">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تخمی ترین بازی جام با اختلاف
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78130" target="_blank">📅 22:28 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
