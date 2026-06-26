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
<img src="https://cdn4.telesco.pe/file/VrBFWjSZbQjpGI-RwGZ3wZ8ONwVzniD9FjofM5M4RgAWAiF3Wpo3uJhOkKs5Hgwvlio9mZLO-yS7ya62T-XTzWczpeKGg3n8nNCB4hRqA_ABka4eZ7Q3_gjANNpehDnXAa_SCvtY1wXtFVeUVDHl_qRotquHBbtLGXlCL5Ofnjp4rjfosSxgVkb3y1wIa-WEZZ29wIUHp0SVi6Dzxx9kqG3uf-MNKMUpKOMHhWt6A98XD0tCM668mIV5eBv0NVk235ruDSvmV48OY6Alc88tFORcGabjDRgCgYaFGPEwHK7sJVmr7ivoHyvu2RjSn83pW6UxaOIotbgg9btlYJsmRw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 330K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 18:41:18</div>
<hr>

<div class="tg-post" id="msg-15855">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دولت امارات: در حال رسیدگی به یک مشکل فنی در سامانه هشدار زودهنگام هستیم.
@withyashar</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/withyashar/15855" target="_blank">📅 18:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15854">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlppBr5-tCcHGnsA2cbRF_pF1nyVhzGondo8wT1NYCbeNOF6fEa14k43w9nPCqJHlbyfLd7s-qdWi1FVY6ztDDRoAPmdCPrw0jRqCb6pJHfElMEIn1IwwXaAf59Ni5cRhkptUXkR0GCUkKHMUmPAR1QnBtoONudh90tlW7xyzWR2ISelBoNTYZp2UPkJi5glzZkbia2PzOzgE6uKvMg9uEwd_l2Ijadv6OJWv-rqKFCMUv-4vHpwGiVxF0BPk1MCveH1ecMCDaZxKgzyk07fBncft5Y18hnMlAH-dTqem4XYU0gLt5N6Nbpu6MqVVux3wCdjM6q1prK7NTTjDLWKow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو سیاتل همجنسگرایان دارن از الان گرم میکنن آماده بازی ایران و‌ مصر بشن
@withyashar</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/withyashar/15854" target="_blank">📅 18:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15853">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">جان بولتون، مشاور سابق امنیت ملی آمریکا، در پرونده نگهداری غیرقانونی اسناد طبقه‌بندی‌شده متهم بود که بخشی از یادداشت‌ها و اطلاعات محرمانه دولت را خارج از سیستم رسمی و در محیط شخصی نگه داشته و در برخی موارد برای امور شخصی استفاده کرده است. او برای جلوگیری از دادگاه طولانی، یک اتهام سوءمدیریت اسناد محرمانه را پذیرفت و با دادستان‌ها به توافق رسید. طبق این توافق، به جای زندان، حدود ۲ تا ۲.۲۵ میلیون دلار جریمه پرداخت کرده و پرونده با توافق قضایی بسته شد.
@withyashar</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/withyashar/15853" target="_blank">📅 18:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15852">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دقایقی پیش وزیر دفاع اسرائیل در پستی به زبان فارسی و بسیار غیر معمول تهدید به جنگ با ایران کرد و گفت: فرمانده نیروی قدس سپاه اخیراً تهدیدهای متعددی علیه اسرائیل مطرح کرده است، به هر حال، اگر ایران به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد،…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/withyashar/15852" target="_blank">📅 18:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15851">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اتاق جنگ با یاشار : بررسی وضعیت پروازها
@withyashar</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/withyashar/15851" target="_blank">📅 17:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15850">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">۲۲ خدمه ایرانی نفتکش توقیف شده توسط آمریکا، در کراچی به سرکنسولگری ایران منتقل شدند
@withyashar</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/withyashar/15850" target="_blank">📅 17:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15849">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">امارات : لطفاً هشدار قبلی را نادیده بگیرید.
@withyashar</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/withyashar/15849" target="_blank">📅 17:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15848">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وضعیت عادی شد
بر اساس الگوهای پیشین، در مواردی که در امارات آژیر هشدار فعال شده و سپس به‌سرعت وضعیت «عادی» اعلام می‌شود، معمولاً این شرایط با رخدادهایی مرتبط بوده که در نزدیکی سواحل یا مسیرهای دریایی و در اثر حمله یا حادثه برای یک شناور رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/withyashar/15848" target="_blank">📅 16:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15847">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">احتمالاً پهپادهایی که از جنوب ایران به سمت کشتی‌ها در تنگه هرمز پرتاب شده‌اند.
گاهی اگر مسیر پرواز مشابه باشد، باعث فعال شدن هشدارها در امارات می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/withyashar/15847" target="_blank">📅 16:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15846">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/withyashar/15846" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15845">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هشدار موشکی در امارات</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/withyashar/15845" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15844">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/withyashar/15844" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15843">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دقایقی پیش وزیر دفاع اسرائیل در پستی به زبان فارسی و بسیار غیر معمول تهدید به جنگ با ایران کرد و گفت:
فرمانده نیروی قدس سپاه اخیراً تهدیدهای متعددی علیه اسرائیل مطرح کرده است،
به هر حال، اگر ایران به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد،
هیچ چیزی ما را متوقف نخواهد کرد،
نیروهای ما آماده‌اند تا وارد جنگ شوند.
@withyashar</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/withyashar/15843" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15842">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0BOvKTQrBIlfzpW7BHJfqgbJzkBet6OEsHv1bXH7DyAFLEkIsZfbBgWUCCRfhYfrE72AxHZ_rXwTIK4SDnJMLylTF9xwFX7tl9aSbCUMnFj-mHsbf4qaA1Mj-X-8VFcplrbsBG4HaEe2WK4u0zIuaUanFSIA3XrU8dKT--rLjH7x5F3H52gL2HnEL6lX1QnTrnsIwtSEZT5YE76oJXO2C6-2IhH0grEvtkYXRU54KO4oGjAVbH3GcwdyUnkFm46sqzHQjRZY1lf16dz-Hc3ae5QC2qJTh67HxFQZAick_9uZX-vdjCOo4uWmzLgJQt9XXOVAEhooncmY1xw8IjX-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت اعزامی به انبارهای گندم ترامپامون
@withyashar</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/withyashar/15842" target="_blank">📅 16:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15841">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">العربیه: دور بعدی مذاکرات آمریکا و ایران در ۲۸ و ۲۹ ژوئن در بورگنشتوک برگزار می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/withyashar/15841" target="_blank">📅 16:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15840">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6b7f6c830.mp4?token=nohB6lI4aW_xDH99rNTmCYucy29Ib-6TOGEKQMpIcwgwWkezHMWWrsHg216hhBrIkTWsd6pjGKK7jzQ_0ClTvFit8w0FO_9lU0U_xVkZDZXCPqyEzkf1E0EnrIxRAptA7huIAxt_UwFo3644bKOuK-77qMfDFLhh4qB2qyTmmc1hud4BeIUeop_tix-yLP95H1RluXcjeROH-lNoPTdW_sNK4bnaxBtYjVmJuqyaHQsiunAsdMrQn6HffQlkMwqEwCk_BLxAtCpzd8GKhF76ww02mrdyh-DopLSzff-bjCagY96gdnhNmhjqZIgPUtFaz1X239GsNwDmWFbsPNaMMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6b7f6c830.mp4?token=nohB6lI4aW_xDH99rNTmCYucy29Ib-6TOGEKQMpIcwgwWkezHMWWrsHg216hhBrIkTWsd6pjGKK7jzQ_0ClTvFit8w0FO_9lU0U_xVkZDZXCPqyEzkf1E0EnrIxRAptA7huIAxt_UwFo3644bKOuK-77qMfDFLhh4qB2qyTmmc1hud4BeIUeop_tix-yLP95H1RluXcjeROH-lNoPTdW_sNK4bnaxBtYjVmJuqyaHQsiunAsdMrQn6HffQlkMwqEwCk_BLxAtCpzd8GKhF76ww02mrdyh-DopLSzff-bjCagY96gdnhNmhjqZIgPUtFaz1X239GsNwDmWFbsPNaMMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل برگه‌هایی را بر فراز شهر المنصوری در جنوب لبنان انداخت و از ساکنان خواست تخلیه کنند، که این اولین دستور تخلیه از زمان آتش‌بس است.
@withyashar</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/withyashar/15840" target="_blank">📅 15:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15839">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ارتش اسرائیل برای شهر منصوری در‌جنوب لبنان هشدار تخلیه صادر کرد
@withyashar</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/withyashar/15839" target="_blank">📅 15:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15838">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">صدا و سیما : سه نفتکش خارجی که قصد عبور غیرقانونی از تنگه هرمز را داشتند، پس از هشدار سپاه پاسداران به بنادر خود بازگشتند.
@withyashar</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/15838" target="_blank">📅 14:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15837">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1wrbtUEDw5jrpiwDYQmbiFAyVK0cvVv4C82-Oee2cAODE2S5cZZhlOpKtyMipnBSJ54zb63zaxp8qszlYBWSCtsbBK0l8Z4QMUhwxIuzyG1ZpuIH37vO8lNQDN-qFSs40Mw8qOLMQENDVejSC1Y7HFVS9hjHC13xU6HYC5vhCKZnfog1v5_BHjsgTr4bSE0grq0jITqcOP5XoooDpwS9fzhpgT-wctk8E-XaaGF8_X4p3gqYqBnBcZU8FntsmlYm8nMa5zyXYHm8hjxCIZtrH54OlviQpLw8ZYhBliiwbNGglRNDT0Xvu0ig8WHKxEDoenxwOwFFaHzKVCYsdcxtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارداد 35 میلیاردی پنتاگون برای خرید موشک‌های رهگیر سامانه پدافندی تاد
وزارت جنگ آمریکا قرارداد بزرگی به ارزش 35 میلیارد دلار با شرکت لاکهید مارتین امضا کرده تا تولید موشک‌های رهگیر پیشرفته THAAD را به‌طور قابل توجهی افزایش دهد.
بر اساس اعلام پنتاگون، این قرارداد 7 ساله قرار است تولید سالانه موشک‌های THAAD را از 96 فروند به حدود 400 فروند افزایش دهد.
@withyashar</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/withyashar/15837" target="_blank">📅 14:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15836">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">برادر زاده اسماعیل هنیه در حمله به نوار غزه کشته شد.
@withyashar</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/withyashar/15836" target="_blank">📅 14:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15835">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فارس: درب تاسیسات فردو، نطنز و اصفهان به روی بازرسان آژانس تا زمان رسیدن به توافق نهایی بسته است
@withyashar</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/15835" target="_blank">📅 14:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15834">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ly7WhgeZPx7BijlTSQ2RQjYFfJ-KaO7r4R4s6NRJyXgbpgZw5avOrkIyMQSM5y2qdiWSTYOknKmpTwJTVb1ED6XDeHCbIVQSoUA83rTq9eKwNqKubPc0PRyXfVu3APJx7F3712cXGz8907GLYklzElUy6e19x1mX8nRRVtkly74PTlxgFQnQhKliUk5WEuKeyWx_z8VizPmrJ5WYpW9ObIu2d2C2Irvr_3Mc_EwVO7CGEwa-5lfaXrFveAxRufzF2jqCvNNM2dVfQ9ABdxxgZicp_X6oXCRDvFocH2UVAze3XKZ-ifMVyLMeHEEzLJU10vHNMAmVVcM3LwYpoMQQFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما با کپی‌برداری از اینترنشنال اومده کنار پخش تلوزیون، عکس کشته شده‌های لبنان رو گذاشته.
@withyashar
۱۸ مدل هم اتاق جنگ کپی‌کردن‌
🤣
کلا کپی‌ هم بلد نیستن</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/15834" target="_blank">📅 14:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15833">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09e2d351d6.mp4?token=ScYovpsUNwrYVH1cEl4aGuaZgzRXx3mpJkwmiwP1dkvZWnSDD2z-cTb-u9O_jPp4pfHuQOUM9NOryfzGAAA3_bcnOEdVgQTE1kM-vL9JYhtLA8dIHjBAbopNt-3o_kdwXWuWI5GadlXloba8IAPEQfNeLp_a5F7cu8MPnlKtFzuw6-i3JqE5qVEeJC0c-gAZFn2e5ENK37aoG8AJCFmGzcJBwWhzbeomnk1uuyaAvDh6Tz7617hkOIiMGhbtHLiVT3jbk7g1qhZ3PZYBmD2fX6nFB8Zdf1i1-6BLvhAkI93Mll9eEdnq2V7g2jZqGArijDpSuGxNkbzX4ye66mdgXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09e2d351d6.mp4?token=ScYovpsUNwrYVH1cEl4aGuaZgzRXx3mpJkwmiwP1dkvZWnSDD2z-cTb-u9O_jPp4pfHuQOUM9NOryfzGAAA3_bcnOEdVgQTE1kM-vL9JYhtLA8dIHjBAbopNt-3o_kdwXWuWI5GadlXloba8IAPEQfNeLp_a5F7cu8MPnlKtFzuw6-i3JqE5qVEeJC0c-gAZFn2e5ENK37aoG8AJCFmGzcJBwWhzbeomnk1uuyaAvDh6Tz7617hkOIiMGhbtHLiVT3jbk7g1qhZ3PZYBmD2fX6nFB8Zdf1i1-6BLvhAkI93Mll9eEdnq2V7g2jZqGArijDpSuGxNkbzX4ye66mdgXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درود یاشارجان
اینجا بندرعباس جایی که تنگسیری تبدیل به کتلت شد , عرازشه شب شام‌غریبان اومدن شمع روشن کردن
@withyashar</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/15833" target="_blank">📅 13:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15832">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21dc4232c0.mp4?token=cNOtWSRvaxTHPhqpdR4IrNskNRrVG-vD9sKePNJtNT9u_pS0Is9eYa6C8te8-_Xtw8plIEmwr2AYwoVkgRWbrLML-wFCugm-joxiQXMgVzEL7ivplTElpYjtpVlkmYv2PMvAHuE4omNicvbCfpqKiDfucTx-5UVtsER7vjUxHfGz54AnhF70YuGu5DfnKpF4CwvnQQmeu-GHD4pWkWhxeyzkCIJXOQmk3XCmMJjwNDf4oo-K7GT5lz96TCOdNCeZHFJMYfCkYzB2hcuAlADdPTlSgcb_vMJOLCBxkPfaonczSIvu-r7m975d6C7ZVz7Tv1R0mc0zWLXbAs4LaOEzQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21dc4232c0.mp4?token=cNOtWSRvaxTHPhqpdR4IrNskNRrVG-vD9sKePNJtNT9u_pS0Is9eYa6C8te8-_Xtw8plIEmwr2AYwoVkgRWbrLML-wFCugm-joxiQXMgVzEL7ivplTElpYjtpVlkmYv2PMvAHuE4omNicvbCfpqKiDfucTx-5UVtsER7vjUxHfGz54AnhF70YuGu5DfnKpF4CwvnQQmeu-GHD4pWkWhxeyzkCIJXOQmk3XCmMJjwNDf4oo-K7GT5lz96TCOdNCeZHFJMYfCkYzB2hcuAlADdPTlSgcb_vMJOLCBxkPfaonczSIvu-r7m975d6C7ZVz7Tv1R0mc0zWLXbAs4LaOEzQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنوز خوراکی خودش را معرفی نکرده بود که حلوا است یا
💩
. بدم می‌آد ازتون. گشنه‌ها. خجالت می‌کشه آدم اینو استوری کنه. می‌گن سهام برند طلا و جواهرات ونکلیف آرپلز ۵۰٪ ریخت، بعد این ویدیو.
@withyashar</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/15832" target="_blank">📅 13:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15831">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">شبکه ۱۳ عبری به نقل از یک افسر ارشد اسرائیل: فروش جنگنده‌های اف-۳۵ توسط واشنگتن به ترکیه، آزادی عمل نیروی هوایی اسرائیل در خاورمیانه را تهدید خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/15831" target="_blank">📅 13:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15830">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/withyashar/15830" target="_blank">📅 13:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15829">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">https://t.me/boost/withyashar
بوست (Boost) در کانال‌های تلگرام به‌صورت مستقیم هیچ درآمدی برای مالک کانال ایجاد نمی‌کند و قابل فروش هم نیست. بوست‌ها را کاربران دارای Telegram Premium به کانال می‌دهند تا قابلیت‌هایی مثل استوری کانال، ایموجی‌ها و ری‌اکشن‌های سفارشی و همچنین ارتقای سطح (Level up) کانال فعال شود؛ یعنی بوست بیشتر یک سیستم امتیازدهی و فعال‌سازی امکانات است و نه پول. بنابراین مالک کانال هیچ مبلغی دریافت نمی‌کند و بوست‌ها تبدیل به پول نمی‌شوند، قابل برداشت نیستند. در جمع‌بندی، بوست فقط برای افزایش امکانات و اعتبار کانال است، نه برای درآمد یا فروش</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/withyashar/15829" target="_blank">📅 13:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15828">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12c8cc82c5.mp4?token=uKmdDnq6Lay62mJg4TTZ3bDBTFPiasuOvhWyh_ZwPBudH66t_tCMPiUsUT8x-btTrE9OlQocRQUGloowKGoKeLSg2a9klo42rG5rSy513RUrhmgYVvZHoJQW0eRFHGbjSHz7UjFHtJA6NlY1fjb9cSMu8Li-1Hpy8luyby0Tk-0z681KqNEDjw38fBnENWR2B-_Ho7E-oyA-QD70QjxywUcT4_PGMmPWePGppJ9HoMmB5wMY-GoVpftQeKCFTNhzEB7zYr1wOteSjneIcfUw52K7F4vD7PYDaQnJPMy_7t2ZwS7DVSaQA6kfEr64G5XrrUsUrC9Z4rOCG4Y0A0OplA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12c8cc82c5.mp4?token=uKmdDnq6Lay62mJg4TTZ3bDBTFPiasuOvhWyh_ZwPBudH66t_tCMPiUsUT8x-btTrE9OlQocRQUGloowKGoKeLSg2a9klo42rG5rSy513RUrhmgYVvZHoJQW0eRFHGbjSHz7UjFHtJA6NlY1fjb9cSMu8Li-1Hpy8luyby0Tk-0z681KqNEDjw38fBnENWR2B-_Ho7E-oyA-QD70QjxywUcT4_PGMmPWePGppJ9HoMmB5wMY-GoVpftQeKCFTNhzEB7zYr1wOteSjneIcfUw52K7F4vD7PYDaQnJPMy_7t2ZwS7DVSaQA6kfEr64G5XrrUsUrC9Z4rOCG4Y0A0OplA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش بسیار از مشاهده شدن دود حجیم در تهران
@withyashar</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/withyashar/15828" target="_blank">📅 13:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15827">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بازداشت یک هکر رژیم در مونته‌نگرو با درخواست اف‌بی‌آی
پلیس مونته‌نگرو به درخواست اف‌بی‌آی، یک تبعه ایرانی را به اتهام حملات هکری گسترده علیه دانشگاه‌های آمریکا و آنچه «خدمت به سپاه» خوانده شده، بازداشت کرد.
اداره پلیس مونته‌نگرو  امروز در بیانیه‌ای مدعی شد این فرد از سال ۲۰۱۳ تاکنون حملات هکری گسترده‌ای را علیه بیش از ۱۵۰ دانشگاه در ایالات متحده انجام داده و خسارتی بالغ بر ۳.۴ میلیارد دلار به بار آورده است.
@withyashar</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/15827" target="_blank">📅 12:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15826">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تسنیم:دیشب یک گروه مسلح در نزدیکی مسجد جامع شهر سراوان تیراندازی کردند و از محل متواری شدن
@withyashar</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/15826" target="_blank">📅 12:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15825">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">زمین‌لرزه‌ای به بزرگی ۷.۸ ریشتر سواحل جنوبی جزیره میندانائو در فیلیپین را لرزاند.
@withyashar</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/15825" target="_blank">📅 11:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15824">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌: تحرکات و حضور هواپیماهای نظامی ارتش اسرائیل در آسمان برخی کشورهای همسایه به سمت ایران، اقدامی خطرناک و تهدید علیه جمهوری اسلامی ایران می‌دانیم.
اعلام می‌داریم چنانچه آمریکا قادر به مهار و کنترل اسرائیل نباشد، جمهوری اسلامی ایران هرگونه تهدیدی را علیه خود تحمل نخواهد کرد و پاسخ به این اقدامات خطرناک را حق خود می‌داند.
@withyashar</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/15824" target="_blank">📅 10:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15823">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نادرشاه افشار در مبارزه با هوتکی‌ها بود تا اصفهان را از اشغال آنان بیرون آورد، در یکی از روزهای نبرد چشمش به پیرمردی افتاد که با وجود سن بسیار زیاد، شمشیر به دست گرفته بود و با چنان قدرت و مهارتی می‌جنگید که گویی جوانی نیرومند است. گفته می‌شود چندین تن از جنگجویان افغان به دست او کشته شدند و همین موضوع باعث شگفتی نادر شد.
بعد از پیروزی و آزادی اصفهان نادر دستور داد پیرمرد را نزد او بیاورند. وقتی او را آوردند، نادر با تعجب به قامت خمیده و چهره سالخورده‌اش نگاه کرد و گفت: «تو با این سن و سال چنین دلاورانه می‌جنگی و این همه نیرو داری؛ پس چرا وقتی افغان‌ها به ایران حمله کردند، اصفهان را گرفتند، مردم را کشتند و کشور را به این روز انداختند، تو کجا بودی؟ چرا آن زمان نجنگیدی تا کار به اینجا نکشد؟»
پیرمرد بدون آنکه هراسی به خود راه دهد، سرش را بلند کرد و با آرامش پاسخ داد: «
من آن روز هم بودم؛ این تو بودی که نبودی.»
می‌گویند نادر با شنیدن این پاسخ لحظه‌ای سکوت کرد، سر به زیر انداخت و دیگر سخنی نگفت؛ زیرا دریافت منظور پیرمرد این نبود که مردم ایران ناتوان یا ترسو بودند، بلکه می‌خواست بگوید مردم آماده دفاع از سرزمین خود بودند، اما فرمانده‌ای نداشتند که آنان را گرد هم آورد و رهبری کند. با آمدن نادر، همان مردم پراکنده به نیرویی منسجم تبدیل شدند و توانستند اشغالگران را از ایران بیرون برانند
@withyashar</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/withyashar/15823" target="_blank">📅 10:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15822">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDjgbV-Y17PK7vqtDAt_rFVfTQ7BfDys_MFO9zrlSBUFXfHrFLJWyidmJXjaqO13RAadIpVo59jICJamyiTc9RbaVkyyhlahfGn7M22PvnkZC5LjlMbwJ4Dm8H1QtfnzNHeRGqwxrgMNRkYl_nJiN7B_FrLLrQwOC-usXlKZx2d8K_7SNnu_661cNYTjv-kZ1hKtRS8L2uJHqEYZG7LMeR-tKgiAEnsKVQ7KYKeSNNI96M8Oi235BIqlokth2dzVrFrh2fvb2vs0Sgwt_QPbutwXxXlqZv9sIwnERor9gA8TwDzhviyryAgYw1h3W6Q1L1N-OOCzTAhasKNEuXBUSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله اسرائیل به جنوب لبنان، ساعتی پیش
@withyashar</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/withyashar/15822" target="_blank">📅 10:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15821">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سیدمحمود نبویان، نایب‌رئیس کمیسیون امنیت ملی مجلس : چرا برای هفته بعد قرار مذاکره گذاشتید؟
مسئولان محترم مذاکرات: مگر نگفتید بندهای ۱،۴،۵،۱۰،۱۱ پیش‌شرط ادامه‌ی مذاکرات است و تا عملی نشود، مذاکرات متوقف می‌شود.
این بندها کامل اجرایی و عملی نشده است.  چرا برای هفته‌ی آینده قرار مذاکراتی گذاشتید؟
@withyashar</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/15821" target="_blank">📅 09:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15820">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آخرین آمار رسمی، حاکی از کشته شدن دست‌کم ۲۳۵ نفر در پی دو زمین‌لرزه شدید در این کشور است. وزارت بهداشت ونزوئلا همچنین از زخمی شدن بیش از چهار هزار شهروند این کشور در دو زمین‌لرزه به بزرگای ۷.۲ و ۷.۵ که شامگاه چهارشنبه رخ دادند، خبر داده است.
سازمان زمین‌شناسی آمریکا هشدار داده است که شمار قربانیان به احتمال زیاد به هزاران نفر خواهد رسید و احتمال زیادی وجود دارد که آمار کشته‌ها از ۱۰ هزار نفر فراتر رود.
@withyashar</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/withyashar/15820" target="_blank">📅 09:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15819">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بیانیهٔ تیم ملی نسبت به احتمال تبلیغات همجنس‌‌بازی در بازی مقابل مصر
فیفا به هر دو تیم شرکت‌کننده اطمینان داده است که هیچ‌گونه مراسم یا فعالیت تبلیغاتی مرتبط با این موضوع در داخل ورزشگاه یا به‌عنوان بخشی از برنامه رسمی مسابقه برگزار نخواهد شد.
موضع ایران این است که هیچ‌گونه مراسم یا فعالیت تبلیغاتی مرتبط با این پروژه نباید در داخل ورزشگاه یا به عنوان بخشی از فضای مسابقه برگزار شود.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/15819" target="_blank">📅 08:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15818">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تحقیقات وال استریت ژورنال نشان می‌دهد: خسارات وارده به پایگاه نیروی دریایی ایالات متحده در بحرین در جریان حملات ایران از اواخر فوریه تا ژوئن بسیار بیشتر از آن چیزی است که گزارش شده است. طبق تحقیقات، ستاد ناوگان پنجم، تأسیسات ارتباطات ماهواره‌ای، انبارها و ساختمان‌های مسکونی آسیب دیده‌اند , که برخی از آنها دیگر قابل استفاده نیستند. تحقیقات هزینه بازسازی را حدود ۴۰۰ میلیون دلار تخمین زده است، اما انتظار می‌رود هزینه کل بسیار بیشتر باشد.
@withyashar</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/15818" target="_blank">📅 08:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15817">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ: ما یک بازار جدید داریم که به آن کشور دوست‌داشتنی ایران می‌گویند. جای زیبایی است، آیا کسی دوست دارد به آنجا برود؟ آنها در تامین غذا مشکل دارند و ما قرار است مقداری از پولشان را بگیریم و آن را خرج کنیم و گندم، سویا و ذرت زیادی بخریم و این روند به زودی آغاز خواهد شد. این کار بزرگ خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/15817" target="_blank">📅 07:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15816">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfef2bc8f0.mp4?token=mIkr-vGckFqYZyxxDc0AENku4fJp-mIwdLLxRW62zc7W16S7O5bvXOVyyw8n3oTOIecDqVoGnbD_FUBYmOB7Cwr0fnDGjKq2mq15z_Xjvz2zCGzYB6gtf4AWMMS_uQbFNBa1ZN8Gml2NfteF-wLWT_oecM1dUkXZh9WwZR6ry9T5ueVDjJQCHg15Q7J6NYtqpUEzcz_MA3lUHEVNnEFls1hvlyAuRQYd2yQ9dVWXFyF58p8SX6laydmBJQYqYpll9MMG2CWHRaCO2wY9kXb8Sj_9HCiMXziluJjCCnxN0JI28WPXsui7jiZFFi3iK5lEiAeZcf5xI6b0dXEoTTn_Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfef2bc8f0.mp4?token=mIkr-vGckFqYZyxxDc0AENku4fJp-mIwdLLxRW62zc7W16S7O5bvXOVyyw8n3oTOIecDqVoGnbD_FUBYmOB7Cwr0fnDGjKq2mq15z_Xjvz2zCGzYB6gtf4AWMMS_uQbFNBa1ZN8Gml2NfteF-wLWT_oecM1dUkXZh9WwZR6ry9T5ueVDjJQCHg15Q7J6NYtqpUEzcz_MA3lUHEVNnEFls1hvlyAuRQYd2yQ9dVWXFyF58p8SX6laydmBJQYqYpll9MMG2CWHRaCO2wY9kXb8Sj_9HCiMXziluJjCCnxN0JI28WPXsui7jiZFFi3iK5lEiAeZcf5xI6b0dXEoTTn_Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف با روسی
🧕🏻
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/15816" target="_blank">📅 00:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15815">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">شبکه المنار : توپخانه ارتش اسرائیل مناطقی بین دو شهرک بیت‌یاحون و برعشیت‌ را مورد حمله قرار داد.
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/15815" target="_blank">📅 23:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15814">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">جنگنده های اسرائیل بر فراز جنوب لبنان به پرواز درآمدند
@withyashar</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/15814" target="_blank">📅 23:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15813">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پرواز مستقیم تهران-دوبی از ۱۰ تیر ماه برقرار می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/15813" target="_blank">📅 22:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15812">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اسرائیل و لبنان، عقب‌نشینی نیروهای اسرائیلی از جنوب لبنان را تکذیب کردند
یک مقام ارشد ارتش اسرائیل گفت که این کشور از منطقه حائل عقب‌نشینی نخواهد کرد. یک مقام نظامی لبنان نیز گفت که تحولات میدانی روزهای اخیر «خلاف عقب‌نشینی را نشان می‌دهد.»
ارتش اسرائیل هم در بیانیه‌ای اعلام کرد که تغییری در محل استقرار نیروهایش در جنوب لبنان ایجاد نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/15812" target="_blank">📅 22:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15811">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">هشدار نهاد مدیریت آبراهه خلیج فارس(PGSA) در‌مورد تبعات
تردد شناورها خارج از مسیر اعلام شده ایران
نهاد مدیریت آبراهه خلیج فارس‏ در پاسخ به استعلام‌های مکرر اعلام میکند:
هرگونه تردد از مسیرهای خارج از چارچوب تعیین‌شده PGSA، مشمول تضمین عبور ایمن نبوده و از پوشش بیمه و مسئولیت‌های مرتبط برخوردار نخواهد بود.
تبعات ناشی از تردد از مسیرهای غیرمجاز، برعهده مالک، بهره‌بردار و فرمانده شناور خواهدبود.
@withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/15811" target="_blank">📅 22:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15810">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9xWb3_US6h8KPfzsm1QdXBCn7uq9XftCseHRxuhqd11v4Iy7NfFmnGfAwjUnpEKQd7WoTLKhjFQvtc82kXAmeyyMAKXfy7fC2eKjQv-Ul0ieEv1W__5OMfa4flYLyQ3KDEwYYThbsUPHp4xMinN6Gn6kTKU9-UsyhSpTOpxBC4IiEOTCO9gtGDPQUT4rPdmzb3-KXUwF3VetSNoO62B7UQa8ICvbtVImgvByIMC318Ve6blwQ9nY8i-GjV5XMG0IQbO7OgARV4DNTyuNU9QXk_HHV7j8kq0oMrXG3q_bwUN6-Xvjsm0ArPFpIxMb2nEmfOX_COspWR1jTv1PTL1ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتشسوزی منطقه ویژه بوشهر الان
دوران جنگ دوبار زده بودن اینجارو
@withyashar
🚨</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/15810" target="_blank">📅 22:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15809">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ورود نیروهای اسرائیل به خاک سوریه
یک گشتی نظامی ارتش اسرائیل با عبور از خط مرزی، به حومه غربی شهرک «الرفید» در ریف جنوبی قنیطره حمله کردند.
نیروهای اسرائیل در جریان این حمله، تعدادی را بازداشت و آن‌ها را مورد بازجویی قرار دادند.
@withyashar</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/15809" target="_blank">📅 21:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15808">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نهاد دریایی بریتانیا :  خدمه یک کشتی از اصابت آن به وسیله یک پرتابه ناشناس در جنوب شرقی عمان خبر دادند @withyashar
🚨</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/15808" target="_blank">📅 21:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15807">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نهاد دریایی بریتانیا :  خدمه یک کشتی از اصابت آن به وسیله یک پرتابه ناشناس در جنوب شرقی عمان خبر دادند @withyashar
🚨</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/15807" target="_blank">📅 21:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15806">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وزیر انرژی آمریکا به سی‌ان‌ان:
لغو تحریم‌ها بر نفت ایران، امکان فروش آن در بازارهای دیگر و دریافت وجه آن به دلار را فراهم می‌کند.
دارایی‌های ایران که مسدود شده بودند آزاد خواهد شد و تحت نظارت شدید در مورد نحوه هزینه‌کرد قرار خواهند گرفت
@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/15806" target="_blank">📅 21:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15805">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">برخی از منابع محلی در لبنان و سوریه، گزارشاتی از تجمع نیروهای جولانی در مرز جنوب لبنان را داده اند
@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/15805" target="_blank">📅 21:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15804">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">moamelegari-trump(@withyashar).pdf</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/withyashar/15804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کتابی از دونالد ترامپ یکی از بحث برانگیز ترین شخصیت های سیاسی جهان.
رئیس جمهور آمریکا دونالد جی ترامپ ، جهان بینی حرفه ای و شخصی خود را در این کتاب جذاب و خواندنی بیان می کند، روایتی دست اول از ظهور مهمترین معامله گر آمریکا.
دونالد ترامپ : هنر معامله گری
🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/15804" target="_blank">📅 20:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15803">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اینم کتاب ترامپ دوباره</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/15803" target="_blank">📅 20:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15802">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گزارش شبکه کان اسرائیل : آمریکایی‌ها در حال ترک فرودگاه بن‌گوریون هستند   ایالات متحده ۲۸ فروند هواپیمای سوخت‌رسان را تخلیه کرده و اسرائیل نیز به‌دلیل نگرانی از اختلال در پروازهای غیرنظامی در طول تابستان، اسرائیل خواستار تخلیه حدود ۲۰ هواپیمای دیگر شده است.…</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/15802" target="_blank">📅 20:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15801">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بالگرد نظامی (بلک هاوک) نیروی هوایی ارتش اسرائیل که حامل «اسحاق هرتزوگ» رئیس جمهور این کشور بود، به دلیل نقص فنی ناشی از برخورد با پرنده در آسمان، مجبور به فرود اضطراری شد.
@withyashar</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/15801" target="_blank">📅 20:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15800">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">شکست شاگردان پیاتزا مقابل آمریکا
🏐
جمهوری اسلامی ۰ - ۳
آمریکا
🇮🇷
۲۳|۲۰|۲۹
🇺🇸
۲۵|۲۵|۳۱
@withyashar</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/15800" target="_blank">📅 20:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15799">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یدیعوت آحارانوت:نتانیاهو موفق شد ترامپ را متقاعد کند که اسرائیل را از جنوب لبنان خارج نکند
@withyashar</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/15799" target="_blank">📅 20:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15798">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پایان ست دوم , لیگ ملت های والیبال
آمریکا
2️⃣
- جمهوری اسلامی
0️⃣
🇺🇸
25 | 25
🇮🇷
23 | 20
@withyashar</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/15798" target="_blank">📅 19:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15797">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کانال 12 ، نتانیاهو :
هنوز ماموریت‌هایی برای انجام دادن وجود دارد، هنوز کارهایی علیه ایران و حماس باید انجام شود. ما تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهیم ماند
@withyashar</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/15797" target="_blank">📅 19:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15796">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نهاد دریایی بریتانیا :
خدمه یک کشتی از اصابت آن به وسیله یک پرتابه ناشناس در جنوب شرقی عمان خبر دادند
@withyashar
🚨</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/15796" target="_blank">📅 18:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15795">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ارتش اسرائیل: اگر به دلیل عملیات ما در لبنان مورد حمله ایران قرار بگیریم، با تمام قوا به آن حمله خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/15795" target="_blank">📅 18:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15794">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تلگراف: فیفا درخواست جمهوری اسلامی و مصر برای ممنوعیت پرچم‌های رنگین‌کمان در بازی دو تیم را رد کرد
@withyashar</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/15794" target="_blank">📅 18:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15793">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کتلین تایسون، بانکدار و تحلیلگر نظام پولی بین‌الملل بریتانیایی :هیچ بانکی برای ایران، صرفاً به‌خاطر مجوز ۶۰ روزه تجارت نفت، حساب دلاری باز نخواهد کرد. تسویه‌حساب محموله‌های نفتی همچنان با ارزهای جایگزین انجام خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/15793" target="_blank">📅 17:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15792">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">جی دی ونس معاون ترامپ: دستاوردهای مذاکرات سوئیس، توافق در اصل برای ایجاد یک کانال ارتباطی نظامی مستقیم بین ایالات متحده و ایران برای کمک به جلوگیری از تشدید آینده بود.
«یکی از چیزهایی که می‌خواستیم به دست آوریم، یک کانال در سمت ایران برای کاهش درگیری بود.»
«آن‌ها گفتند: "باشه، ما کسی از سپاه پاسداران را می‌فرستیم تا در دوحه با کسی از فرماندهی مرکزی (سنتکام) باشد و این همان راهی است که بسیاری از این اختلافات را حل می‌کنیم."»
@withyashar</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/15792" target="_blank">📅 17:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15791">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af0b1ba54a.mp4?token=jPERDN50nI6Yee6_n1XvR3zFFW2yvmd4mFdgAUSPmqgKgFz59WkdxUUEmZHzf0ZDTAVGJnT1GRq7eQ4dFEfA8O4MW0zb9m0NqQJq_HmleBc5aHlagv5JOVx_tHlfX60xfabAmWX4OPKZxdqzImpOQuBGhQR0IY-Vo-_RLqXJHDS-p7U0MAkDZqoBp-QJICa-fyR7XnIvQv3aEF2cp_eqONfEV5sXuzH8IOEGEuac1xKT2J0bMqyyBBgZOnmnja0Kon4TKBY1IFVZZdKS2EJN7m5nzxv0eARrf2otuBNpv9fz40g3DCnH7Bu7s6HeODx2ekBBfxbz9vRIk1WPPSyaSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af0b1ba54a.mp4?token=jPERDN50nI6Yee6_n1XvR3zFFW2yvmd4mFdgAUSPmqgKgFz59WkdxUUEmZHzf0ZDTAVGJnT1GRq7eQ4dFEfA8O4MW0zb9m0NqQJq_HmleBc5aHlagv5JOVx_tHlfX60xfabAmWX4OPKZxdqzImpOQuBGhQR0IY-Vo-_RLqXJHDS-p7U0MAkDZqoBp-QJICa-fyR7XnIvQv3aEF2cp_eqONfEV5sXuzH8IOEGEuac1xKT2J0bMqyyBBgZOnmnja0Kon4TKBY1IFVZZdKS2EJN7m5nzxv0eARrf2otuBNpv9fz40g3DCnH7Bu7s6HeODx2ekBBfxbz9vRIk1WPPSyaSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۶ VHF نیروی دریایی سپاه:«عبور و مرور در تنگه هرمز فقط با اجازه نیروی دریایی سپاه و در مسیرهای تعیین شده امکان‌پذیر است.
اگر هر کشتی‌ای بدون اجازه ما، با سیستم شناسایی خودکار خاموش یا خارج از مسیر تعیین شده اقدام به عبور کند، مسئولیت هرگونه عواقبی بر عهده آن کشتی خواهد بود.»
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/15791" target="_blank">📅 16:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15790">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">قالیباف: آمریکا به دروغ ادعا می‌کند که دارایی‌های آزاد شده ما صرف خرید محصولات کشاورزی آن‌ها خواهد شد. جالب است؛ تنها محصولی که ما در حال برداشت آن هستیم، همان چیزی است که شما کاشته‌اید: دهه‌ها بی‌اعتمادی. این محصول، ارگانیک، فراوان و بومی است. اما ظاهراً آمریکا تنها سویاهای تراریخته، وعده‌های شکسته شده و یاوه‌گویی صادر می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/15790" target="_blank">📅 15:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15789">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e51659f85.mp4?token=nUdXdvGMbgz3t-mbGWfM4AqK0zZJrOZZtXrmCvS_SFKG1Y7LyLd4Nw08fRXi-vtxLMLEs2qaM7IWj5iei05rhnp2a67tzPAyP1f3DScBbzk-VQzwdQS9yjA4gkww373bgAS8WYgSMdQuqh7RkjM2dddX-IgXxXuIpt9E7y5LeYkS5pquQh_ocrVd7YW3762G_OzQvwW_1bpCTDbRS97Oib6D34IpSdYb4-fu9Au2mMUHmpOLfJxMLxIo-zSVfJNsm75XrPAglrYZLMc0H00TlC9jgw82LFJqVMH84PyyGmy_YimEgiAEZkgBgqd3K7aSHrFflS0asyT_cF2J2F-3aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e51659f85.mp4?token=nUdXdvGMbgz3t-mbGWfM4AqK0zZJrOZZtXrmCvS_SFKG1Y7LyLd4Nw08fRXi-vtxLMLEs2qaM7IWj5iei05rhnp2a67tzPAyP1f3DScBbzk-VQzwdQS9yjA4gkww373bgAS8WYgSMdQuqh7RkjM2dddX-IgXxXuIpt9E7y5LeYkS5pquQh_ocrVd7YW3762G_OzQvwW_1bpCTDbRS97Oib6D34IpSdYb4-fu9Au2mMUHmpOLfJxMLxIo-zSVfJNsm75XrPAglrYZLMc0H00TlC9jgw82LFJqVMH84PyyGmy_YimEgiAEZkgBgqd3K7aSHrFflS0asyT_cF2J2F-3aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی: هنوز مطمئن نیستم همه‌چیز تموم شده باشه، چون هر چند ساعت یه توییت جدید از ترامپ منتشر می‌شه و با هر توییت، تیتر خبرها عوض میشه؛
واسه همین فعلاً روی هیچ‌کدوم از حرف‌هایی که ترامپ زده حساب باز نمیکنم.
@withyashar</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/15789" target="_blank">📅 15:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15788">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اختلال بانک‌ها بعد از چندین روز همچنان ادامه دارد
رصد گزارش‌های مردمی در شبکه‌های اجتماعی، کانال‌های اطلاع‌رسانی و بازخورد کاربران نشان می‌دهد شبکه بانکی ایران از فاز اختلال شدید عبور کرده و بخش عمده خدمات به وضعیت عملیاتی بازگشته است.
در میان بانک‌های بزرگ، بانک ملی همچنان بیشترین حجم شکایت کاربران را به خود اختصاص داده است.
@withyashar</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/15788" target="_blank">📅 14:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15787">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">روبیو: آمریکا خواهان توافق با ایران است، اما توافق به هر قیمتی را نمی‌پذیرد
@withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/15787" target="_blank">📅 14:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15786">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فرمانده نیروی قدس خطاب به اسرائیل:
اگر امروز با اختیار خود عقب‌نشینی نکنید، فردا با خواری و شکست ناگزیر به فرار خواهید شد
@withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/15786" target="_blank">📅 14:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15785">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04b7288a91.mp4?token=TgxLAvSKMFuIMzusDCj-tjofo32-aj3zUo-KHHyZt1AKVmtILvSCiSZ06dGebEpT0I_f2kDDx85YjIw_TyY-1DUsdZoYew2Nv7l4Cl-eJmboECvTN175Hb4uyNKvuZ1KGqwtzQkGEQ06_IDhseTDDzoV2PmbtxyH6Tuju4oAOhwtrcfZoDIFWLXzj0Pvyci_31NU9HhegVpq429Kv2fBomrCg3bou6H7qCM6L75rZrGpfAWxzly69cqthLoVelPgUL_V5aUi-0QkRF9Jk5UN07Q0nvf0K_9XH8IrskFzoiMbM_CD4Em7eGvbA1WyOmMrhanzYbG3RUfoRFjUBJ81fjq6QsSbvIIlJyP6DzEuiC65fU0hK2bxTKCQA3R4RH-BSFVBa7kpEeJttPGaNo7h-TFpfdBA1JOo-WqtNp721H6d5vlbw7Lw7ML4t4z7ELa2yhgsfWQwloq1MroOd3RNHVSFEXsqsAosVkTffWRPKcVriFK_XQTE-EiTdKZlYnhH8RtMX0bvNwe_rutrPjDpujizCCfn3stR1tRAUrFPOW2wJdJxTLHQtgdryh1wUIpCICBA21TFHfId3KSP5jb0ehOyQ0TGjLPtAs01koRKNVm0P8rlJvpNf-9o9N_yiT5ijNbNx1XQw7vPWShTs0ACv4BTm22K07DOfIUSJHf4dZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04b7288a91.mp4?token=TgxLAvSKMFuIMzusDCj-tjofo32-aj3zUo-KHHyZt1AKVmtILvSCiSZ06dGebEpT0I_f2kDDx85YjIw_TyY-1DUsdZoYew2Nv7l4Cl-eJmboECvTN175Hb4uyNKvuZ1KGqwtzQkGEQ06_IDhseTDDzoV2PmbtxyH6Tuju4oAOhwtrcfZoDIFWLXzj0Pvyci_31NU9HhegVpq429Kv2fBomrCg3bou6H7qCM6L75rZrGpfAWxzly69cqthLoVelPgUL_V5aUi-0QkRF9Jk5UN07Q0nvf0K_9XH8IrskFzoiMbM_CD4Em7eGvbA1WyOmMrhanzYbG3RUfoRFjUBJ81fjq6QsSbvIIlJyP6DzEuiC65fU0hK2bxTKCQA3R4RH-BSFVBa7kpEeJttPGaNo7h-TFpfdBA1JOo-WqtNp721H6d5vlbw7Lw7ML4t4z7ELa2yhgsfWQwloq1MroOd3RNHVSFEXsqsAosVkTffWRPKcVriFK_XQTE-EiTdKZlYnhH8RtMX0bvNwe_rutrPjDpujizCCfn3stR1tRAUrFPOW2wJdJxTLHQtgdryh1wUIpCICBA21TFHfId3KSP5jb0ehOyQ0TGjLPtAs01koRKNVm0P8rlJvpNf-9o9N_yiT5ijNbNx1XQw7vPWShTs0ACv4BTm22K07DOfIUSJHf4dZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اردوغان می‌خواست برای کمک به ایران وارد جنگ شود، من نگذاشتم
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/15785" target="_blank">📅 14:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15784">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اسرائیل هیوم: به ارتش اسرائیل هیچ دستوری مبنی بر عقب‌نشینی داده نشده
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/15784" target="_blank">📅 13:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15783">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مخالفت شدید چین با اقدامات آمریکا علیه کوبا
وزارت خارجه چین بیان کرد: چین همواره با تحریم‌های یکجانبه غیرقانونی که هیچ پایه و اساسی در قوانین بین‌المللی ندارند، مخالفت کرده است.
پکن از واشنگتن می خواهد تا فوراً به تحریم کوبا و هر نوع اجبار یا فشار پایان دهد. ما حمایت بی‌دریغ خود را از کوبا در جستجوی مسیر توسعه سوسیالیستی متناسب با شرایط ملی آن مجدداً تأیید می‌کنیم
@withyashar</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/15783" target="_blank">📅 13:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15782">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">moamelegari-trump(@withyashar).pdf</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/15782" target="_blank">📅 13:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15781">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رویترز
:
اسرائیل به نشانه حسن نیت از بخشی از منطقه امنیتی جنوب لبنان عقب‌نشینی کرد
@withyashar</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/15781" target="_blank">📅 13:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15780">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سی‌ان‌ان: متحدان ترامپ در کشورهای حاشیه خلیج فارس بیم دارند که توافق او با ایران سرآغاز تحولی فاجعه‌بار باشد
@withyashar</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/15780" target="_blank">📅 12:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15779">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏وو باهیانا، پیشگوی برزیلی مدعی شده است که در جریان دیدار برزیل و اسکاتلند در جام جهانی ۲۰۲۶ که بامداد پنجشنبه در فلوریدا برگزار می‌شود، فضایی‌ها به زمین حمله خواهند کرد. او که بیش از ۲۳ میلیون دنبال‌کننده دارد، حتی ویدیویی تولیدشده با هوش مصنوعی از ربوده…</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/15779" target="_blank">📅 12:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15778">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ: به لطف قدرت و مهارت نیروهای مسلح ایالات متحده، امروز ایران نیروی دریایی، نیروی هوایی، پدافند ، پرتاب موشک، و تولیدی ندارد و رهبری آن نابود شده است. برای اولین بار در ۳۰۰۰ سال، ما بالاخره صلح را در خاورمیانه خواهیم داشت. @withyashar</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/15778" target="_blank">📅 12:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15777">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edea42e58c.mp4?token=YjNRjUompG9Es6h2dtCijaAueCuXYJ6N-2yM25ps9w21gV1-gaa3xIpal8sb1NExQE1mg_onMjtCNhsXCcYg2vYbmysVjbOUXCfAltZeLabTUQrWuQL8fmFPu4vPwlc9OLmLsU-PTZ_peIKvHmO-RVNZUp34LmayuEdju0F2t8QZUKTG2hbtulFukxVqwR_FZ90ISKsSV9tpZl50mk0ee7WKzfcBXQJPx9BfDoY1aLomVV7qPMED2Aoe8zoK8DZU6A54IoH_CiqewyR5BQ6EIMjWxA2F3AnOGjQL-uWFsCrrNZbkA4w8KdST7MXi_-0eGUvF0HmYrzyp9T1AlfaV-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edea42e58c.mp4?token=YjNRjUompG9Es6h2dtCijaAueCuXYJ6N-2yM25ps9w21gV1-gaa3xIpal8sb1NExQE1mg_onMjtCNhsXCcYg2vYbmysVjbOUXCfAltZeLabTUQrWuQL8fmFPu4vPwlc9OLmLsU-PTZ_peIKvHmO-RVNZUp34LmayuEdju0F2t8QZUKTG2hbtulFukxVqwR_FZ90ISKsSV9tpZl50mk0ee7WKzfcBXQJPx9BfDoY1aLomVV7qPMED2Aoe8zoK8DZU6A54IoH_CiqewyR5BQ6EIMjWxA2F3AnOGjQL-uWFsCrrNZbkA4w8KdST7MXi_-0eGUvF0HmYrzyp9T1AlfaV-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: به لطف قدرت و مهارت نیروهای مسلح ایالات متحده، امروز ایران نیروی دریایی، نیروی هوایی، پدافند ، پرتاب موشک، و تولیدی ندارد و رهبری آن نابود شده است.
برای اولین بار در ۳۰۰۰ سال، ما بالاخره صلح را در خاورمیانه خواهیم داشت.
@withyashar</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/15777" target="_blank">📅 12:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15776">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">حمله اسرائیل به جنوب لبنان
@withyashar
🚨</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/15776" target="_blank">📅 12:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15775">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وال استریت ژورنال:
ایران ۳.۸۴ میلیارد دلار را از طریق صرافی رمزارز CoinEx منتقل کرده تا تحریم‌های آمریکا را دور بزند
@withyashar</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/15775" target="_blank">📅 11:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15774">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ایلان ماسک در پی سقوط سهام تسلا و اسپیس ایکس در معاملات روز چهارشنبه که ارزش دارایی او را به ۹۷۰.۲ میلیارد دلار کاهش داد، عنوان «تریلیونر» را از دست داد.
@withyashar</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/15774" target="_blank">📅 11:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15773">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZ-wmmP8hG8ffqLtKzq0n_EVz6iH1yxWHpQhfyX1ARTQU8sCwvm5TVUBJwBy-gg33ELjsF0Gbx9MuB3yl1gJ_Phy9TDdrxniauadouVmvFkUYCubzk8UCk-y5c-xg95BjurxDatW_A_x-3iEFVd59hItrYfTjzPzy2L-4-NKQtvr6EFzzfrtIfUuAflAvALZm9Uwjn1jtHlxs4FukvC4MNdazOVPrk9VScmdkqNbR3l3epWSShrg1Cx8LSxXhksyFX4wb0u5VpV9NSrhhI6_NbLSLIO59JHk7WaBrGyV-2RxG2IN97xJWYIiGlfHmXo2YZOoeiu0tFFN_26qLoUMxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:وای! سنا رأی خود در مورد ایران را از ۵۰ به ۴۸ مخالف به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر کردند. از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه متشکرم.
این رأی، ایران را در معرض توجه قرار می‌دهد! رئیس جمهور دونالد جی ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/15773" target="_blank">📅 11:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15772">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2960b1463d.mp4?token=gddzvWbil5F1ePjse29jmSBFfdCIPDeM2ESWy0-lCY9xY0pgdiZ2BLBKuTZ9YaTmFhHz1zXfPUnPE1Y-nRUMx2T0sQFAlHj7g0H9KzTIViWniCjC3uTfhWBpHFcGHvnXdaVYPlOpGt3J_7W8zx5TYr4yx0Bq0-l6atJryorZGTzRs3R-hp1ZSgD8fiqspKAXBFSvtsE_tLTv6scXAYaIBm3GC8By0GX5QXVxB6FLnNJtqCYrC7_ZpS5Hv4f18CcjqS6dbqwgHM8KjqUqrckcAh917Pn4rs6TxxUG-TlVUI33JAESnmy7w3k11cRf23xkjPgbJv92FEbS7iWtM5tmpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2960b1463d.mp4?token=gddzvWbil5F1ePjse29jmSBFfdCIPDeM2ESWy0-lCY9xY0pgdiZ2BLBKuTZ9YaTmFhHz1zXfPUnPE1Y-nRUMx2T0sQFAlHj7g0H9KzTIViWniCjC3uTfhWBpHFcGHvnXdaVYPlOpGt3J_7W8zx5TYr4yx0Bq0-l6atJryorZGTzRs3R-hp1ZSgD8fiqspKAXBFSvtsE_tLTv6scXAYaIBm3GC8By0GX5QXVxB6FLnNJtqCYrC7_ZpS5Hv4f18CcjqS6dbqwgHM8KjqUqrckcAh917Pn4rs6TxxUG-TlVUI33JAESnmy7w3k11cRf23xkjPgbJv92FEbS7iWtM5tmpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما در دو جنگ جهانی پیروز شدیم، فاشیسم و ​​کمونیسم را شکست دادیم.
ما باید دوباره این کار را انجام دهیم.
@withyashar</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/15772" target="_blank">📅 11:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15771">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">«قطعنامه اختیارات جنگی ایران» متوقف شد
‏ سنای آمریکا با ۵۰ رای مخالف، ۴۷ رای موافق و یک رای ممتنع، با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد.
‏ جمهوری‌خواهان و ترامپ استدلال کرده بودند، تصویب این قطعنامه می‌تواند اهرم فشار آمریکا در مذاکرات جاری با جمهوری اسلامی را تضعیف کند.
‎
@withyashar</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/15771" target="_blank">📅 10:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15770">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ درباره ایران: هفته گذشته، ما یک توافق تاریخی برای پایان دادن به درگیری با ایران امضا کردیم، تنگه هرمز را کاملاً باز کردیم و کاری را انجام دادیم که هیچ رئیس‌جمهوری قبلاً نتوانسته بود انجام دهد.
@withyashar</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/15770" target="_blank">📅 10:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15769">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lof8R2B9Iqw8OS0zrV68BR6ulmjkbgMLzR4YWRpbs1cdR7ThGJsL5BMwVZG8x7yRNEGf0pZ-VSTAufkmpYEXqw0OA2-Z3p5qPJRtsfcwTg641T2vUgE3qW8xHRORUx1YzUqR8ndsKaEpAsq8lBzCW0WTte-t6qcHtW8E6WNEVlMoTL8PRNPSn8kVQsInuQ8btlLw_yEpwBCcBLuKGQ9FMtdZ2eZfH-PSYeKMAss0ZAl0-nNyn1r_dQ5on7tABMNFwMsZMOlN14F_GKe_6AInAba-IE5-iGjIyCdiSQxY-S-FXT7-sBMu_32TozZZ6GRAr6P-CJ7et-sabl_noEu5Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ در‌ تروث : دو زلزله بزرگ که به تازگی مردم بزرگ ونزوئلا را لرزاندند، هر دو در مقیاس وسیع بوده و تعداد زیادی کشته به جا گذاشته‌اند. ایالات متحده آماده، مایل و قادر به کمک است! من به تمام نهادهای دولتی دستور داده‌ام که برای اقدام سریع آماده باشند. ما در کنار دوستان جدید و بزرگ خود خواهیم بود. گزارش‌های اولیه خوب نیستند.
@withyashar</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/15769" target="_blank">📅 09:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15768">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هشدار سونامی در ونزوئلا، بعد از زمین‌لرزه۷ ریشتری، ویدیو منتشرشده از کاراکاس، برخاستن دود و گردوغبار از مناطق مختلفی را در پی این زمین‌لرزه شدید نشان می‌دهد. @withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/15768" target="_blank">📅 02:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15767">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5061be29e3.mp4?token=L2P9v86X9vlgeUlch_TlX7EmVIWp7eWV0ybnWSLkIBN0Ru1GUNXqP01nzh6bjMFsDh1eW5sE7tRT8CPOGkNqgJu5peTDxZJUNd5G22cNQQ5q7_fYhbwRNJx3bEV_SsQXw8bF-7KKUQ0OkJiAc_DblZwjzMKr_jk3hZF3OtQZlS1XI_atMXA1Uxvw2UBWqXWR9WMVSC_8HSpYe19RKzQ-QgTielIqGvvInHfn6gGYAIdxye6yFgNC_Bii26MVmGt7J4lnanNXT2Sou2L65opmD_BF9UFeyT19uY8g6FRx8SzC3nh4l1z9jHdJwtjXg7--RmzPkTSalA9w-XKjuUgP5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5061be29e3.mp4?token=L2P9v86X9vlgeUlch_TlX7EmVIWp7eWV0ybnWSLkIBN0Ru1GUNXqP01nzh6bjMFsDh1eW5sE7tRT8CPOGkNqgJu5peTDxZJUNd5G22cNQQ5q7_fYhbwRNJx3bEV_SsQXw8bF-7KKUQ0OkJiAc_DblZwjzMKr_jk3hZF3OtQZlS1XI_atMXA1Uxvw2UBWqXWR9WMVSC_8HSpYe19RKzQ-QgTielIqGvvInHfn6gGYAIdxye6yFgNC_Bii26MVmGt7J4lnanNXT2Sou2L65opmD_BF9UFeyT19uY8g6FRx8SzC3nh4l1z9jHdJwtjXg7--RmzPkTSalA9w-XKjuUgP5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هشدار سونامی در ونزوئلا، بعد از زمین‌لرزه۷ ریشتری، ویدیو منتشرشده از کاراکاس، برخاستن دود و گردوغبار از مناطق مختلفی را در پی این زمین‌لرزه شدید نشان می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/15767" target="_blank">📅 02:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15766">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏وو باهیانا، پیشگوی برزیلی مدعی شده است که در جریان دیدار برزیل و اسکاتلند در جام جهانی ۲۰۲۶ که بامداد پنجشنبه در فلوریدا برگزار می‌شود، فضایی‌ها به زمین حمله خواهند کرد. او که بیش از ۲۳ میلیون دنبال‌کننده دارد، حتی ویدیویی تولیدشده با هوش مصنوعی از ربوده شدن مردم منتشر کرده است.
‏گفته می‌شود بابا وانگا، پیشگوی مشهور بلغاری هم، وقوع یک تهاجم فضایی در جریان یک رویداد بزرگ ورزشی را پیش‌بینی کرده بود.
@withyashar</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/15766" target="_blank">📅 01:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15765">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">طارمی و الهویی دوباره در مرز آمریکا «معطل شدند»
ایرنا از معطلی کاروان تیم ملی پس از ورود به خاک آمریکا از مرز مکزیک خبر داده و نوشته مانند دو سفر قبلی، روند عبور مهدی طارمی و سعید الهویی، توسط ماموران مرزبانی طول کشیده است.
دیدار با مصر در سیاتل (ایالت واشنگتن) که مرز شمال غربی آمریکا با کانادا است برگزار می‌شود.
تیم ملی برای صعود مستقیم به دور حذفی باید مصر را شکست دهد اما با تساوی مقابل این تیم هم می‌تواند به صعود به عنوان تیم دوم یا سوم باقی امیدوار بماند.
@withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/15765" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15764">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVmW_1Lbhb9Ybc03RwWpFPXeYZbKAZTdPnRVKoVfSeE2A9ku9ibDCk-5hbi-65DAunBFElEeNi2yRRokP7_ES6KrDT6of2ql3TOEIOlgjXbkv7ky86ssswOhPRaownQCs7Mum4E-W7KrzXNOFOW0wkvn7C3beaOtPcsrwCJwwpkpumZFj8ALmJR719AO4b9BKbqS0J7WEjqcJdCjcsYJoACMuC1rGtVwOWjKkvScX9oyVAnNzshHHxGLi5L806Jz9GY7FOKJY9TNeHscCFTK1mRcq0bIa5HuCttv8fa-PYgSVN9RKXR__UMvWVbIPfJ35Zf1QWPuJ7Ts_zm9LD080A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو هواپیمابر «آبراهام لینکلن (CVN-72)» نیروی دریایی آمریکا در تصاویر ماهواره‌ای در فاصله ۱۴۰+ کیلومتری بندر چابهار ایران مشاهده شد.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/15764" target="_blank">📅 23:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15763">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فاکس‌نیوز : ترامپ به دنبال تأمین ۶۷۲ میلیون دلار برای حذف مواد هسته‌ای ایرانی است
@withyashar</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/15763" target="_blank">📅 23:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15762">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وزارت امور خارجه ایران: واشینگتن باید از تفسیرهای متناقض با مفاد یادداشت تفاهم بپرهیزد.
@withyashar</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/15762" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15761">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گزارشهای زیاددددد از صدای انفجار دوباره  در بندر عباس
🚨
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/15761" target="_blank">📅 22:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15760">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/15760" target="_blank">📅 22:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15759">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">جنجال در ایتالیا پس از افشاگری درباره همکاری پنهان در جنگ علیه ایران پولیتیکو: افشاگری مارک روته، دبیر کل ناتو در خصوص استفاده آمریکا از پایگاه‌های ایتالیا در جنگ علیه ایران واکنش تند گوئیدو کروستو، وزیر دفاع ایتالیا را در پی داشت.  گوئیدو کروستو گفت: تنها…</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/15759" target="_blank">📅 22:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15758">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">جنجال در ایتالیا پس از افشاگری درباره همکاری پنهان در جنگ علیه ایران
پولیتیکو: افشاگری مارک روته، دبیر کل ناتو در خصوص استفاده آمریکا از پایگاه‌های ایتالیا در جنگ علیه ایران واکنش تند گوئیدو کروستو، وزیر دفاع ایتالیا را در پی داشت.
گوئیدو کروستو گفت: تنها پروازهای مطابق با معاهدات مجاز بوده‌اند؛ پیام روته کاملا اشتباه است.
احزاب مخالف در ایتالیا از این توضیحات قانع نشدند. آنجلو بونلی، نماینده سبزها گفت: ملونی به ایتالیایی‌ها و پارلمان دروغ گفت. ملونی باید فورا روشن کند چه اتفاقی افتاده و به پارلمان گزارش دهد.
@withyashar</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/15758" target="_blank">📅 22:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15757">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فردا فرمانده ستاد فرماندهی مرکزی ایالات متحده(سنتکام( به اسرائیل خواهد رسید
@withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/15757" target="_blank">📅 22:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15756">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نعیم قاسم ، رهبر حزب الله ، اعتراف کرد که یک گروهک تروریستی نمی تواند ارتش اسرائیل را در رویارویی مستقیم نظامی شکست دهد
@withyashar</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/15756" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
