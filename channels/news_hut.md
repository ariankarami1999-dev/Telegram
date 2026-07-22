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
<img src="https://cdn4.telesco.pe/file/L_VAiYb43UDuISIPCzrI39F4AVys2QzoZm7apbs3tVBm7C1w3qk4KlDmbgWgIsJpJof5Aljf1UaxjvloHUg_ew5xB44OFqkVYohS65317mPuyu1phmVb_510ke6iCVLBfdtQmuTKPIexfW4uERORtp7lXUPi1M29njeiqt7YWt_DR4DhLPui4hhAFRpCUlihEImOCZrr8leDR4udRBdkSZGGMOBxwRNRR7I1eKr_3_WvrMyvzt5mVRQDxJmE3meG9_RkLC-Y6KlVi2f_CW15Jm3tlVsKnA720RntwIi9CYB5JH5CYh8w38rj98NwXredkKBmaL_TPC6IdeTbr6BZ-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 154K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 11:22:12</div>
<hr>

<div class="tg-post" id="msg-68782">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c11f67944.mp4?token=Luq85FXg4cYS_D0eT-3upc-sgoeIeAonpIcd82nj-n9el8ITJfTB5lVAT1Yhlok92OTcvgqUOAUSApj2EZLAFK6YrGipbnJzefeMnpddIcCFLH09w6HMlvUk671bQ2b0vcYVeYRBInaKbkR1O700Wd7s1I30lNMpnEYumgHC8kNV0uTmylJSTeuNhzq7YFiYpbrW-H96RVwzODlFbQN6huYi6TIcLTuZNQ1g2-4rhKVfPTJbhwkLYGoOwaa6rsVBpip9e73E0TuAIJ7wPzhJ-buFIKBiUx7EqiIm8h5RaezqWjFM6lX73N5zRPTVZSYFpBmkrNWEP3fpVLkCIKDr5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c11f67944.mp4?token=Luq85FXg4cYS_D0eT-3upc-sgoeIeAonpIcd82nj-n9el8ITJfTB5lVAT1Yhlok92OTcvgqUOAUSApj2EZLAFK6YrGipbnJzefeMnpddIcCFLH09w6HMlvUk671bQ2b0vcYVeYRBInaKbkR1O700Wd7s1I30lNMpnEYumgHC8kNV0uTmylJSTeuNhzq7YFiYpbrW-H96RVwzODlFbQN6huYi6TIcLTuZNQ1g2-4rhKVfPTJbhwkLYGoOwaa6rsVBpip9e73E0TuAIJ7wPzhJ-buFIKBiUx7EqiIm8h5RaezqWjFM6lX73N5zRPTVZSYFpBmkrNWEP3fpVLkCIKDr5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
⭕️
گفته میشه دیشب با وجود اینکه پدافندا توی تهران خیلی فعال بودن اما انفجاری گزارش نشده.
احتمالا دیشب بیشتر پهپادهای شناسایی آمریکا، مثل MQ-1C Gray Eagle و... تو آسمون تهران بودن و پدافندا هم سعی می‌کردن اونا رو بزنن.
احتمالاً مأموریت اصلی این پهپادا دیشب شناسایی بعضی مکان‌ها، مراکز نظامی، محل استقرار پدافندا، و... بوده و ممکنه که آمریکا درحال آماده کردن خودش برای دور جدیدی از جنگ باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/news_hut/68782" target="_blank">📅 10:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68781">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e535968cb3.mp4?token=bBEjoyVgl39rVCr6UX9m6MwD7IWPFCT2Z7kHEauEr02BWA0gP9JNI2MfSAPWlgq_fU7uE65wiKhqGX8LYjqx2sRV_pTSjeQ8MOG57091fw12qPhfSISmN2WLujOKaghdjwwnHrpFmIyN-YzB5L7HioSRxxXdjuIBzkI7ebJ_i8vaVakQkqEJIsqz3uoCz2jFf78fWmd-_ZgMr5JGAP9ut9MdxKQ663uP8sPwFi2fawhvooVVOh3bLekrR5EJoaByS5LVLCaCGwoQjiFJo2yQPm-_ULw5e0A-H3ve5Qgb48GhqD5IbAwvTuuGWBSwu7VXYyLbpdZcby3GOkwkROHBUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e535968cb3.mp4?token=bBEjoyVgl39rVCr6UX9m6MwD7IWPFCT2Z7kHEauEr02BWA0gP9JNI2MfSAPWlgq_fU7uE65wiKhqGX8LYjqx2sRV_pTSjeQ8MOG57091fw12qPhfSISmN2WLujOKaghdjwwnHrpFmIyN-YzB5L7HioSRxxXdjuIBzkI7ebJ_i8vaVakQkqEJIsqz3uoCz2jFf78fWmd-_ZgMr5JGAP9ut9MdxKQ663uP8sPwFi2fawhvooVVOh3bLekrR5EJoaByS5LVLCaCGwoQjiFJo2yQPm-_ULw5e0A-H3ve5Qgb48GhqD5IbAwvTuuGWBSwu7VXYyLbpdZcby3GOkwkROHBUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی دو روز قبل یه گونی آدم از مجری‌های صداوسیما ، اعضای پایداری و بعضی ورزشکارها در واکنش به کارزاری که راه افتاده بود، پا شدن رفتن جنوب که بگن ما از جنگ ترسی نداریم و این حرف‌ها؛
حالا کجا رفته باشن خوبه؟
بهمنشیر که تو نزدیکی کویته و 14 ساعت [1125 کیلومتر] با بندرعباس فاصله داره
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/news_hut/68781" target="_blank">📅 10:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68780">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/822c8aa150.mp4?token=P50h4jODfNPQ_VIEnG00HPx8EP8rBH3hXxWj5pe1YbnbwHaTTkzfCWqrcyZ8ZDlhxJ21yImcovTijuRmEQELvQjt6EYplGq9YU1gW6brDjNuorsag0o3vkAddo1PitxsdhcDZZ3uAKswjFyAFAQ6SO4o6FA0Tjmk7Rpjz6NnMt7coJdsWhY_fSQEKTItt-T0nPJ1Nm_tuJ7AOiKWnhqOugOYnkayoCtsyz1pe2gZcqqlDvKGlUy-X0boM0hT3F-ciDgoXpiF9oeE-0D7j3nH7IXtm46gvtA8bhG94uBDW_Sd10EFiZC1wnRefvk1yXQC4moxgBipy17qS6BjhCci0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/822c8aa150.mp4?token=P50h4jODfNPQ_VIEnG00HPx8EP8rBH3hXxWj5pe1YbnbwHaTTkzfCWqrcyZ8ZDlhxJ21yImcovTijuRmEQELvQjt6EYplGq9YU1gW6brDjNuorsag0o3vkAddo1PitxsdhcDZZ3uAKswjFyAFAQ6SO4o6FA0Tjmk7Rpjz6NnMt7coJdsWhY_fSQEKTItt-T0nPJ1Nm_tuJ7AOiKWnhqOugOYnkayoCtsyz1pe2gZcqqlDvKGlUy-X0boM0hT3F-ciDgoXpiF9oeE-0D7j3nH7IXtm46gvtA8bhG94uBDW_Sd10EFiZC1wnRefvk1yXQC4moxgBipy17qS6BjhCci0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
لحظه‌ای که عادل فردوسی‌پور تو لایو فوتبال 360 بغض و گریه کرد...
اپلیکیشن‌ و سایت فوتبال 360 به علت اینکه عادل و مهمون‌هاش از تیم ملی انتقاد کرده بودن، به درخواست قلعه نویی و باندش فیلتر و از دسترس خارج شده و مجبور شدن برنامه رو تو لایو اینستاگرام و یوتیوب اجرا کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/68780" target="_blank">📅 10:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68779">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087e2855d3.mp4?token=Ep7gUnmikgfoFcSEQt59hm5ZJOP9SE9PUVDpOw6Ho0MUoI16Tn6-WB1YRQNOELGrhFhJt0p1434CjMODJ42T1CcAn1tXD9QP46XOXC2EonrRiKPRhpOANAhXc5CATtnScNineK2SthUgVWKGh6zLdDM6Dm2nxipAkUuS_0dw12rsSfH9hdSpGtIX7Fo_LbgjwCfBRUnOGZGWlShFCPpB9RRQAXvvlGL_ZK04Keja4LA63eoRzA_RUKHkl9Ye96QtUWViHL1SUgKTavLbZ5je6Gpj22J8cYeZe98aN8dHRlDnR9FHFrlVpa56gRl_lKCObNa85YXHLgLzUyfaXaWjxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087e2855d3.mp4?token=Ep7gUnmikgfoFcSEQt59hm5ZJOP9SE9PUVDpOw6Ho0MUoI16Tn6-WB1YRQNOELGrhFhJt0p1434CjMODJ42T1CcAn1tXD9QP46XOXC2EonrRiKPRhpOANAhXc5CATtnScNineK2SthUgVWKGh6zLdDM6Dm2nxipAkUuS_0dw12rsSfH9hdSpGtIX7Fo_LbgjwCfBRUnOGZGWlShFCPpB9RRQAXvvlGL_ZK04Keja4LA63eoRzA_RUKHkl9Ye96QtUWViHL1SUgKTavLbZ5je6Gpj22J8cYeZe98aN8dHRlDnR9FHFrlVpa56gRl_lKCObNa85YXHLgLzUyfaXaWjxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
نظر مارکو روبیو درباره برجام (سپتامبر 2015)
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/68779" target="_blank">📅 09:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68778">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
سنتکام: حملات امشب به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68778" target="_blank">📅 04:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68777">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68777" target="_blank">📅 03:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68775">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c46837f26.mp4?token=CRzvE_Sk52fj7U_6yTp1wlSmVjGqbTrNi2gffbveLzhSY2nCrTnn5_A3DcBxa7xiWSakAmXY-cSypmmuvfJf4jQqZe3IbKuVVnwgb0sXPkc1-UYiTplJss0itzc3eI176evCwsUgIt6Kpt4Py1DbVJx676g0Lx_6NgCU-ftKQUrydKSR-9cHaO1E7Dwxwd5bMvEiyLcetpiJpYCIDIOUvdfLl3-NU6RrnfR5DGxf9SvSqZkAtJwexeMbdPZgDav-Pk8wCysr6oztoZ0ZnK6VpQFzsrH0FxCl-1qm_HMghyyc8Ty6wcSr4Ifhtu9UsPgVeVAg_CMP_IOzVWQejgkJ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c46837f26.mp4?token=CRzvE_Sk52fj7U_6yTp1wlSmVjGqbTrNi2gffbveLzhSY2nCrTnn5_A3DcBxa7xiWSakAmXY-cSypmmuvfJf4jQqZe3IbKuVVnwgb0sXPkc1-UYiTplJss0itzc3eI176evCwsUgIt6Kpt4Py1DbVJx676g0Lx_6NgCU-ftKQUrydKSR-9cHaO1E7Dwxwd5bMvEiyLcetpiJpYCIDIOUvdfLl3-NU6RrnfR5DGxf9SvSqZkAtJwexeMbdPZgDav-Pk8wCysr6oztoZ0ZnK6VpQFzsrH0FxCl-1qm_HMghyyc8Ty6wcSr4Ifhtu9UsPgVeVAg_CMP_IOzVWQejgkJ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68775" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68774">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
❌
🌐
امشب ریزپرنده ها در تهران فعالیت داشتند، احتمال اختلالِ بیشتر در اینترنت وجود داره؛ پروکسی های پرسرعت زیر رو داشته باشید
https://t.me/proxy?server=nab.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68774" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68773">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در زنجان!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68773" target="_blank">📅 03:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68772">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6Mil3TL9-pE2GufdC0RrUDNnIz1FNQdS4Ior7s0TmCBv3I9byN2KOerT42Mc-lFIEcL2P_I534wcZAZLOW0a1yfaiSspQFddnTSM7bDqwNEcO_vBMkrJhrjWmqYIWd3A6BE6_JtyDr9KHJ4U_ueKwT9FtONjOnNBGHJqRaKscJLkUNYPIImxz1tCAVXCH7Cf2100kTGsPrNUzFe0ssOU3rW-eYgg0erHe7bpM5EYFPOMb9Ho4gjlJKdXUlgQX_aIVcGjSBjgqEPPJHZnPkvSzdgjLJv_gJzoj6LlxJmnb5_HCddGw3N9BVwZlFUWo14k70XpE7pHqJMQUbo-vEM1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جالبه هنوزم سنتکام چیزی نگفته!!! #hjAly‌</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68772" target="_blank">📅 03:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68771">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
فعالیت پدافند شرق تهران
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68771" target="_blank">📅 03:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68770">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🇺🇸
هم‌اکنون حملات شدید آمریکا به</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68770" target="_blank">📅 03:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68769">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">جالبه هنوزم سنتکام چیزی نگفته!!! #hjAly‌</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68769" target="_blank">📅 02:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68768">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تا این لحظه سنتکام هیچ خبری مبنی بر آغاز حملات رو اعلام نکرده! #hjAly‌</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68768" target="_blank">📅 02:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68767">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بابت گزارش های لحظه‌ایتون عمیقاً سپاسگزارم، ولی حتما سعی کنید بعدش چنین گزارش هایی رو پاک کنید خدای‌نکرده جایی تو بازرسی گوشی توسط مزدوران ج.ا، مشکلی پیش نیاد
❤️
#hjAly‌
‌</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68767" target="_blank">📅 02:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68766">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
هشت انفجار در تبریز  @News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/68766" target="_blank">📅 02:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68765">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/68765" target="_blank">📅 02:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68764">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مثل اینکه تو غرب تبریز صدا های شدیدی اومده، مشخص نیست حمله‌ست یا شلیک موشک های سپاه #hjAly‌</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68764" target="_blank">📅 02:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68763">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مثل اینکه تو غرب تبریز صدا های شدیدی اومده، مشخص نیست حمله‌ست یا شلیک موشک های سپاه
#hjAly‌</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/68763" target="_blank">📅 02:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68762">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/68762" target="_blank">📅 02:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68761">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/68761" target="_blank">📅 02:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68760">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
انفجار در ماهشهر و بهبان  @News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/68760" target="_blank">📅 02:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68759">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
انفجار در ماهشهر و بهبان
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/68759" target="_blank">📅 02:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68758">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در نارمک!!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/68758" target="_blank">📅 02:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68757">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💥
ارائه مهیج‌ ترین اسلات‌ های جهان
💲
شروعی هیجان‌انگیز با 100% هدیه خوش‌ آمدگویی ورزشی و کازینو تا سقف 100 میلیون ریال
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/68757" target="_blank">📅 01:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68756">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvNcPqPsfZwMLBhutM-_wIoaQeZrCkrtE6Q7hxJe8g4RuFT4brbtvP7nh6SDGQG_wyVl9kALPxVRfZx-5z70uJ1JebNQTlvjEOjmNyw1nhcnkox7rfinDyWS9FDtlFZLoqBAQB1Pnfkq2H9kQ94_lMSQ6vxIZ9Zb9nmIvhgLqW7KwCSugt4cCZ1gI_VAEzB_IVTEBUOZFnRsGhfxz8KdKDjfLYq2f8aMlrrgcLe834gJnHe-lB7QNaQCTga3iEe7QfP2nQdqCyjWPMd7vAfQTeJmUxQlfgHfSkTIEYrAbKqqAMhbZbgKfauO_oCZu2mf6gX_GeW4IQhi4TdVFn6kXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🍾
شب‌های بی‌پایان در یک بت!
🎁
35%
بانس جبران باخت ورزشی و کازینو، شبی پر از هیجان و فرصت‌های جدید
⏰
مختص واریزی‌های ساعت 00 تا 8
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/68756" target="_blank">📅 01:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68755">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f9fa164a6.mp4?token=kgdwK-b9u7MYCtAuKJxGRU3-w6mothBJxjjUvtmivKQT5r3U_PI2digWjHR7NgIc4fQMaBFBjHQ3ciwbGVfn9Fktw5kIXy1svZupOHg3q6_6gR1Vfe1zAANagDIcog1OEanm0xK3mSNFqeY4R1s4FtYc0RRlu37SGdl6UapJgP3HbwaSlVrhwRYHZqQ8T7DwQGevVG7Iad84nQy2EBF9zA8Vm45dbHPH72QhhqydHiedySN9PLennRY1p7J2sPvcX_1kpSUM668VYfohEV6DN3Xe9o7IWgdFhFhfv9-1UPX9NdR4wXwHH_-Wf6Q9b5HBq8vAN3Htlkbg7nQe1ooziA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f9fa164a6.mp4?token=kgdwK-b9u7MYCtAuKJxGRU3-w6mothBJxjjUvtmivKQT5r3U_PI2digWjHR7NgIc4fQMaBFBjHQ3ciwbGVfn9Fktw5kIXy1svZupOHg3q6_6gR1Vfe1zAANagDIcog1OEanm0xK3mSNFqeY4R1s4FtYc0RRlu37SGdl6UapJgP3HbwaSlVrhwRYHZqQ8T7DwQGevVG7Iad84nQy2EBF9zA8Vm45dbHPH72QhhqydHiedySN9PLennRY1p7J2sPvcX_1kpSUM668VYfohEV6DN3Xe9o7IWgdFhFhfv9-1UPX9NdR4wXwHH_-Wf6Q9b5HBq8vAN3Htlkbg7nQe1ooziA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🚀
پهباد‌های انتحاری در آسمان کویت
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/68755" target="_blank">📅 01:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68754">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
جمهوری اسلامی به کویت حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68754" target="_blank">📅 01:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68753">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7d96b014.mp4?token=SzTpZf_vxBL4-k2-AArKIWQ1ER-a90S9CoW6SxQ_DPKhAn-bDTZeWrtstb06wHMH_FCSsl2WpyatG7kUq7cDf81CnfYa-8BkO1jq2pV-4h3CIDj7YQvo3cWrehP4eXhSAcaTxYLrtcleKyBIOGDwJ-R9nfcqrZOnHNJnAxxlOS8_yioqL_p_WuyNKw3QI92Timqmkr9Xd5B07tXVNiQLuBIk_ILiMDf4hOxdZVZMJOBSCgZkzawpnwUEC--CvX9ZOwPoQjEMd80z6WPpwKc85oQTtkZB8tyfaHs8xPSg3dRA27F_3SgDj_B-SD9zz6zb-GhIUCydSf6PLP3rTus19g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7d96b014.mp4?token=SzTpZf_vxBL4-k2-AArKIWQ1ER-a90S9CoW6SxQ_DPKhAn-bDTZeWrtstb06wHMH_FCSsl2WpyatG7kUq7cDf81CnfYa-8BkO1jq2pV-4h3CIDj7YQvo3cWrehP4eXhSAcaTxYLrtcleKyBIOGDwJ-R9nfcqrZOnHNJnAxxlOS8_yioqL_p_WuyNKw3QI92Timqmkr9Xd5B07tXVNiQLuBIk_ILiMDf4hOxdZVZMJOBSCgZkzawpnwUEC--CvX9ZOwPoQjEMd80z6WPpwKc85oQTtkZB8tyfaHs8xPSg3dRA27F_3SgDj_B-SD9zz6zb-GhIUCydSf6PLP3rTus19g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هگست وزیر جنگ آمریکا:
«رئیس‌جمهور ترامپ گفت که ما دوباره درگیر جنگ‌های احمقانه‌ای مانند [عراق و افغانستان] نمی‌شویم، و او این کار را نکرده است.
به همین دلیل است که ما سعی نکرده‌ایم جامعه ایران را از نو بسازیم، بلکه صرفاً، به شیوه‌ای واقع‌گرایانه و با شعار «اول آمریکا»، اطمینان حاصل کنیم که آنها هرگز به بمب هسته‌ای راه پیدا نمی‌کنند - کاملاً متوقف می‌شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68753" target="_blank">📅 01:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68752">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8503f1809.mp4?token=Bgs2QVO_9BXYUwHnjUBH8EhiUwJITvpMn5fF-F1REnKhGWB-eVm-6Ynm5zkJMNC5Qz0mrJGv61MudlcRnZxN6auxYBAFu932ito4Zp2NZrxZiapKL9vN9WdWg867Uo5jXcXqQAIiYAcN3Nb-AC_ioKUUxSnK2MruQTTUjZLoCEHVbbv3jXZPK8AXe2nouMbZP6Wu5hCczABP3dSfZmE5FqyvncPEOWPQ4kz9qUrO4mg70DQc_kqLs49fOBMdMLfD72bmi3gseBYnDTN3FKZb3gyxBEyxkDKnrmlqah8ZvAGVTbqThkSZVPInS2z1_tq63wmy90mrAJGddvYlDYe4Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8503f1809.mp4?token=Bgs2QVO_9BXYUwHnjUBH8EhiUwJITvpMn5fF-F1REnKhGWB-eVm-6Ynm5zkJMNC5Qz0mrJGv61MudlcRnZxN6auxYBAFu932ito4Zp2NZrxZiapKL9vN9WdWg867Uo5jXcXqQAIiYAcN3Nb-AC_ioKUUxSnK2MruQTTUjZLoCEHVbbv3jXZPK8AXe2nouMbZP6Wu5hCczABP3dSfZmE5FqyvncPEOWPQ4kz9qUrO4mg70DQc_kqLs49fOBMdMLfD72bmi3gseBYnDTN3FKZb3gyxBEyxkDKnrmlqah8ZvAGVTbqThkSZVPInS2z1_tq63wmy90mrAJGddvYlDYe4Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاورمیانه هرشب
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68752" target="_blank">📅 00:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68751">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u02vnFI5bMVsNngKesOZ3llT-iGwybNlU9_Z_ELprRtkB48W_vlaQZ7lpVniLSmhuse2-QS8np1MOKvHZy8sqPsVO07rwMzTOtFczIFKQuHLTJBmzbFYVWdHPLASONG8y9Dqa4IUf8-n5GtRkkMu4gNecD4dVCXZ6o_GdVxcz3ANt76nmXOyNvjpR_5xnBtszv5F4SbiOlin-c4fcnLkq4pbpJrORdvozD_WmIgfX65QpED1od4nZO0l61L9ljj0IIwXhmOHePajPfPvDAcl4_5e8DMLFvujr2sw75j5SWKQhx_U7aGRsKd64mKWE3uV0guDdYeNN-w1BcVJ0ZsM4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قرارگاه مرکزی خاتم‌الانبیا:
آمریکای جنایتکار مراکز هسته‌ای و تأسیسات حساس ایران رو تهدید کرده که ممکنه بهشون حمله کنه.
اعلام می‌کنیم اگه ارتش متجاوز و تروریست آمریکا چنین اقدامی انجام بده، این کار رو به‌عنوان گسترش جنگ در منطقه تلقی می‌کنیم و همه منافع آمریکا، همچنین منافع متحدها و حامیان این کشور یاغی و شرور، هدف حملات قدرتمند نیروهای مسلح جمهوری اسلامی ایران قرار می‌گیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68751" target="_blank">📅 00:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68750">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e35b34fa8d.mp4?token=RAG5zMI5CjAMXstOY1QYH27_1mouS8eRuGmZneUYq0u0grakH4M35iakyumcnOr8RcK4AOM5I-vAQj1CXcEzHjrAM0RY9x_m4U6lET6BjyBfEAidWBkB4bVg-wu1_weLzSfe-15hIIji8ahQaLOlZZxcWFG6SmnjKwQXj2V8orzP0J_Zg3XDHJj76f4UgiSn2gAfVxrnA0ncqkY9Ap_9Oycti3md3wx5_T57-CvEFagECjIiQu3xqWanv4vCn2TA2JoNRv4i66AyUI0RcuGoHuihiJg-NuoSG_tanmayEQKzLaJAXBWZwR1d3ZRmAUMkkjW2n-m25n2t-3BlMXdU1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e35b34fa8d.mp4?token=RAG5zMI5CjAMXstOY1QYH27_1mouS8eRuGmZneUYq0u0grakH4M35iakyumcnOr8RcK4AOM5I-vAQj1CXcEzHjrAM0RY9x_m4U6lET6BjyBfEAidWBkB4bVg-wu1_weLzSfe-15hIIji8ahQaLOlZZxcWFG6SmnjKwQXj2V8orzP0J_Zg3XDHJj76f4UgiSn2gAfVxrnA0ncqkY9Ap_9Oycti3md3wx5_T57-CvEFagECjIiQu3xqWanv4vCn2TA2JoNRv4i66AyUI0RcuGoHuihiJg-NuoSG_tanmayEQKzLaJAXBWZwR1d3ZRmAUMkkjW2n-m25n2t-3BlMXdU1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🎙
سناتور:
آیا ما توانایی نابود کردن هر آنچه را که در زیر «کوه پیک‌اکس» (Pickaxe Mountain) ایران قرار دارد، داریم؟
⏺
🇺🇸
هگست:
بسیاری از توانمندی‌های ما طبقه‌بندی‌شده (محرمانه) هستند، سناتور. اما اگر کسی در جهان بتواند به هر نقطه‌ای از این کره خاکی دسترسی پیدا کند، آن ارتش ایالات متحده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68750" target="_blank">📅 00:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68749">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2ac98ac4.mp4?token=IifGDZZlnV_ny1Ifn7gINfIJWbskzSavxmjsPNVjUkHz2a8X2xS3k3RFssgRwfJJn61pOFf2SCVM2ahsF7xM0eDRLdk1UPtRuA7t4qbwhDH8RzFetHyyii_6ZPFpYsHiSYcz2UNJ2G7k96xClqOqxOiBxa4l9smgetUgp9k8z_C_cHBwb7WA7Y9G6pL6j3Huf-O0ywi__C_fsmXrg9kwsOy3syw5kX2bPJ29wFEBuBLuVA6ok7FhAIzhMNOFSzzvAGV7No5OHPhvGEbckspoZh-u8_2akTfDZIMf3jmaaeloAPi4brYQ84O-aJj26x6Di7AxxcNTjZadbNOY-STMnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2ac98ac4.mp4?token=IifGDZZlnV_ny1Ifn7gINfIJWbskzSavxmjsPNVjUkHz2a8X2xS3k3RFssgRwfJJn61pOFf2SCVM2ahsF7xM0eDRLdk1UPtRuA7t4qbwhDH8RzFetHyyii_6ZPFpYsHiSYcz2UNJ2G7k96xClqOqxOiBxa4l9smgetUgp9k8z_C_cHBwb7WA7Y9G6pL6j3Huf-O0ywi__C_fsmXrg9kwsOy3syw5kX2bPJ29wFEBuBLuVA6ok7FhAIzhMNOFSzzvAGV7No5OHPhvGEbckspoZh-u8_2akTfDZIMf3jmaaeloAPi4brYQ84O-aJj26x6Di7AxxcNTjZadbNOY-STMnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هگست:
محاصره ما دوباره اعمال شده و عملاً غیرقابل‌نفوذ است...
بسیاری از حملاتی که دریاسالار کوپر و سنتکام (CENTCOM) انجام می‌دهند، توانایی ایران برای رصد و پایش در تنگه هرمز را از بین می‌برد.
سناتور جان هوون: « هدف از این بودجه‌گذاری همین است... اطمینان از اینکه ما و متحدانمان می‌توانیم در تنگه هرمز عملیات انجام دهیم... و اینکه ایران را وادار کنیم تا در راستای اهداف ما عمل کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68749" target="_blank">📅 00:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68748">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f962f6335.mp4?token=B8lLETyQg28QjKSCH0XoJQGgdCb3dNsGKlLbbmF-3w0Uh4AMh_ySFP2sNMNeDN9xjYVvu8hGUp_IL92MMSse5zT_OM3gorUO5bNHnK5TJs1ThPjCSK71X5pcFty9JyM4A91jeq-Zos1XFzgiYAnl15-P7GA5gy-OwJNAfivG2AUVuwdbNPoUoaRp48aO-YkRaFDldj6pYidVh3oXgpIRAmxjhLhJVxxIJZS6W8V4MyvZSsgEMySq-mbEOQN-OXxE2MuAxORosyUO6HEcvruHA_4DVdj3qVmQczdVmAbNM-44IsyfZnR11b3lJ_8Veks7H1bFW7mLOQZUOd88vZkviA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f962f6335.mp4?token=B8lLETyQg28QjKSCH0XoJQGgdCb3dNsGKlLbbmF-3w0Uh4AMh_ySFP2sNMNeDN9xjYVvu8hGUp_IL92MMSse5zT_OM3gorUO5bNHnK5TJs1ThPjCSK71X5pcFty9JyM4A91jeq-Zos1XFzgiYAnl15-P7GA5gy-OwJNAfivG2AUVuwdbNPoUoaRp48aO-YkRaFDldj6pYidVh3oXgpIRAmxjhLhJVxxIJZS6W8V4MyvZSsgEMySq-mbEOQN-OXxE2MuAxORosyUO6HEcvruHA_4DVdj3qVmQczdVmAbNM-44IsyfZnR11b3lJ_8Veks7H1bFW7mLOQZUOd88vZkviA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست:
من در مقابل یک کمیته نشسته‌ام که می‌خواهد درباره پیروزی در جنگی صحبت کند که چهار سال است ادامه دارد، و درباره شکست استراتژیک درگیری‌ای صحبت می‌کند که چهار ماه است ادامه دارد، تا از دستیابی ایران به بمب هسته‌ای جلوگیری شود.
امیدوارم که در این شهر، دیدگاهی وجود داشته باشد نسبت به اهمیت تاریخی اقداماتی که رئیس‌جمهور ترامپ در حال انجام آن‌ها است.
آیا شما می‌خواهید که گروه‌های افراطی اسلامی به بمب هسته‌ای دست پیدا کنند...؟"
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68748" target="_blank">📅 00:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68747">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/912fcd0888.mp4?token=i1_fCSX0jkyh0CH-NvVisFVMuX282XJXNjIqP3lHo4HihvGKhICCb5HEW4DuL9-gy1Iq3HBqZOaNl6aTWSHXizcjhWw4EpWQA8zAZ7x4bXaK2Oa9xcwvQiUFT8Em2l_0Q8id0eBiIyR3fp00gpwz5gem2KgStDxW1gBRZk3iUromv_gx7AwvBt9o6oy-F89PGr6tz5do91arwDRHgWeDez-Uuln-ATwj71hUDpjDBi9Dme9vqdVuhS5JR_3b0qydOmMWckUEvrXlOET21LFoUP5MIWlG85dNos5ib619Rf2uv31CySREbrTIx72FyWQ9EcSn09Mnpc0zUu9l5wH7-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/912fcd0888.mp4?token=i1_fCSX0jkyh0CH-NvVisFVMuX282XJXNjIqP3lHo4HihvGKhICCb5HEW4DuL9-gy1Iq3HBqZOaNl6aTWSHXizcjhWw4EpWQA8zAZ7x4bXaK2Oa9xcwvQiUFT8Em2l_0Q8id0eBiIyR3fp00gpwz5gem2KgStDxW1gBRZk3iUromv_gx7AwvBt9o6oy-F89PGr6tz5do91arwDRHgWeDez-Uuln-ATwj71hUDpjDBi9Dme9vqdVuhS5JR_3b0qydOmMWckUEvrXlOET21LFoUP5MIWlG85dNos5ib619Rf2uv31CySREbrTIx72FyWQ9EcSn09Mnpc0zUu9l5wH7-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست درباره ایران:
ایران از نظر نظامی در ضعیف‌ترین وضعیت تاریخ خود قرار دارد...
بی‌شک اذعان می‌کنم که آن‌ها همچنان از توانمندی‌هایی برخوردارند، اما حجم خساراتی که ما طی این رشته عملیات به آن‌ها وارد کرده‌ایم، آن‌ها را در بدترین موقعیت تاریخشان قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/68747" target="_blank">📅 00:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68746">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f9adfe1f.mp4?token=jTONwoTcfaCV9W4uo8uNJMgrVqMn3J7mp3O031oT0OAvien_M1w8rBRgw2ipP6oXZNXe9qD4TLGaWayLgutE6ja4_nprYDKiumscmXfxh8PFoCAapxcG-wl_rkp_HTp_euf3cNs6q34fPO6qDaPZd16-THTqT47z08CEPika103WKztZcmxRYKZf5j0Xtx0wGQCc2QaaT6nSK3YepsE78J0jUEkweCj2okVl0eH6jMDCaGAzcbckY6zSmg68p33uf5MHXD03W-y8jIKSXW7vRktRJR_K_obqSSzl4AwBjJH-A1EdbdmNe8UbfEsjcczAihJnUZZ5NIZWtNzCf2ZxKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f9adfe1f.mp4?token=jTONwoTcfaCV9W4uo8uNJMgrVqMn3J7mp3O031oT0OAvien_M1w8rBRgw2ipP6oXZNXe9qD4TLGaWayLgutE6ja4_nprYDKiumscmXfxh8PFoCAapxcG-wl_rkp_HTp_euf3cNs6q34fPO6qDaPZd16-THTqT47z08CEPika103WKztZcmxRYKZf5j0Xtx0wGQCc2QaaT6nSK3YepsE78J0jUEkweCj2okVl0eH6jMDCaGAzcbckY6zSmg68p33uf5MHXD03W-y8jIKSXW7vRktRJR_K_obqSSzl4AwBjJH-A1EdbdmNe8UbfEsjcczAihJnUZZ5NIZWtNzCf2ZxKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت
هگست:
این درخواست تکمیلی دو هدف را دنبال می‌کند: حفظ آمادگی نظامی ما برای پاسخگویی به نیازهای جدید امسال؛ و تسریع قابلیت‌های حیاتی برای جایگزینی و تقویت قابلیت‌هایی که در شرایط اضطراری استفاده کرده‌ایم...
در حوزه آمادگی، ما ۲۱ میلیارد دلار درخواست کردیم. این مبلغ برای تأمین حقوق نظامیان، جایگزینی تجهیزات مورد استفاده در عملیات‌های اخیر، حفظ نیروهای مستقر در خط مقدم و افزایش قدرت نهایی پرسنل در عین تثبیت کمبود سوخت حیاتی ماموریت و پشتیبانی از گارد ملی هزینه خواهد شد.
در حوزه قابلیت‌ها، ما ۴۶ میلیارد دلار درخواست کردیم. این بودجه خطوط تولید را گسترش داده و تحویل مهمات مورد نیاز را تسریع می‌کند. ما در مورد موتورهای موشک سوخت جامد، JADM، موشک‌های مافوق صوت و قابلیت‌های ضد پهپاد صحبت می‌کنیم. علاوه بر این، ما از این سرمایه‌گذاری برای تضمین تسلط دیجیتال و فضایی، از جمله شبکه‌های ماهواره‌ای انعطاف‌پذیر، استفاده خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68746" target="_blank">📅 00:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68745">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b34a86e2.mp4?token=GYmOEJrLW_CUWMsHcgXRI3bJA-IPDvFGf1oZA2eMPfoGeRWH7tyn94p5Td9Ykkty4d_INIUJOjRMSwZFcGsf5mK1wv0YsH6tKVMY3qxVe_25t_qholUIkzAAI1x-reBLDUXooavQQynotHI9TF2PAriiaM4bpt1aaZX_9gTrVHmhaCJn01hOsPLUzb6pdnBITbp0bpPT74Dim4IIblsuDdk0up-siwR8LN6IKRsmSxKYwA2TGDuYVLlCW58gdQis0WsPXVX25ChHoR5P4Qmg4WHKgGwFSXv_oHOP46W7VfA-HszSkvWUhxpg40hBGNhuUyxsEePZy9_EFJ7hu4xw3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b34a86e2.mp4?token=GYmOEJrLW_CUWMsHcgXRI3bJA-IPDvFGf1oZA2eMPfoGeRWH7tyn94p5Td9Ykkty4d_INIUJOjRMSwZFcGsf5mK1wv0YsH6tKVMY3qxVe_25t_qholUIkzAAI1x-reBLDUXooavQQynotHI9TF2PAriiaM4bpt1aaZX_9gTrVHmhaCJn01hOsPLUzb6pdnBITbp0bpPT74Dim4IIblsuDdk0up-siwR8LN6IKRsmSxKYwA2TGDuYVLlCW58gdQis0WsPXVX25ChHoR5P4Qmg4WHKgGwFSXv_oHOP46W7VfA-HszSkvWUhxpg40hBGNhuUyxsEePZy9_EFJ7hu4xw3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست وزیر جنگ آمریکا:
«رئیس جمهور ترامپ از یک منطق ساده پیروی می‌کند - ارتش برای تحقق صلح از طریق قدرت به یک سرمایه‌گذاری نسلی نیاز دارد.
ما می‌دانیم که بهترین راه برای ایجاد صلح، آماده شدن برای جنگ است - برای جلوگیری از آن و این دقیقاً همان کاری است که وزارت جنگ انجام می‌دهد - ایجاد نیرویی چنان توانمند که به چالش کشیدن آن برای هر کسی پوچ و بی‌معنی باشد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/68745" target="_blank">📅 00:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68744">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVfxZn7nMI13gY2NnOMQOELkusOnEWHjjyCIBkvaBnpfblVh-wIrIe5sSS72l-8ek90ilZpORgMmaIXXwsP3hM3O7TgEQcWTQB4kCIM6PNwgjvQwQ-wieVer-GHo85ZJJT7R7IRrgcsdVWvKMM-vb-H44J5aufKOdypri9z8ba7bB1L-pGKlrAcASORTuaYU7sYafLsdACXbFAzyVDdQZpB0Eq6aCAUoyYq0Hf_piCGZ6k0dCwNQbsnwB2jvmTJHqUsZ3wMM05_UQAt7AgXGNvRzQsfgRhTNprWqN6UGsX5y42PFDcC5KkLTGF_wwupnUnxagBjom5fPvremLmDp-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
چند سوخت‌رسان از فرودگاه بن‌گوریون اسرائیل بلند شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68744" target="_blank">📅 23:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68743">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تاسیسات جدید هسته‌ای ج.ا: ۲۰۰ متر زیر کوه کلنگ
پرنفوذ ترین بمب غیرهسته‌ای آمریکا: GBU-57 با ۶۰ متر نفوذ
#hjAly‌</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68743" target="_blank">📅 23:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68742">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uov9ySljvgi5h6e3mIHHq6Osi6dcrAc5jQUdk2_1oaVMBiMK1gf9Ju5iwXQaOTqudgvB6Bs1_5XhXWx8R9l__Tj0xYRgzbi0aA3GVKLxnD4YH1JD34g8iotTyidoJ3-FINFC6RbGUIK6hUCNywgKi06HTZEATXuJ8e06jxv-vlGSqFW56ZvtbEzX4NvwV_mo9H1N_mo3Fg9jPMs-Mr25RhZTmDUFMfybVeKFu9zWMAMpi8dc8BEYvvxo8IPwsWLwaDv1NoHHKFDAciELegnUrTl92qqrQElILbspmNRCmIrRGD5FY1vkviO2RYpozenTjsdLCqdoko5IvfPHXatM6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
جنگ افغانستان: ۲۰ سال، ۲ هزار کشته.
جنگ عراق: ۹ سال، ۴۶۰۰ کشته.
جنگ ویتنام: ۱۹ سال و ۵ ماه، ۵۸۲۲۰ کشته.
جنگ کره: ۳ سال و ۱ ماه، ۳۶۵۷۴ کشته.
درگیری‌ها در ونزوئلا: ۱ روز، ۰ کشته.
درگیری‌های نظامی با ایران: ۴ ماه، ۱۸ کشته.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68742" target="_blank">📅 23:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68741">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab2e49c2e.mp4?token=nvQsucOn7VxJ8X2HYJpbp4zwuuvz2CQfLhpOJmQzvYg7QOYWfCLibyBG9WypU7gGkKwFhEBooOQuRzFUYFtlsIDy20XTMOuI1_1SfCOjMRwbN0RT6YaUCUY2t46aLeZ_QecKMjeGFdt1GFCIC0b46r274kVjyYrQOCtMg8Wf79E6YoCVXMFuyWRlgOr2vWMWxL7o2Qg3Mha3TtKNhcfRei43GkYBbqI2q7xJFnS_J4NDH2UhlNBzyryWpjcjDpZ7N7qX5gcLJnQbFQiqsyqvgWgO-gDBtYjsQSnRlLMN77LL2_IRidCJettz9l3_xltOxctIf8R4tjLjfxTyd9WXCZTZTX5w_mCJlghrtA11MJl0e7-BVAmvGJUSrpElT0cl4ynMW-sirXOQsto_IQfnrtvjZ2aORP4L3ojg9EQUClZdiQuYyXeL00-V0KVf0aAUR-zYWYDvIF1ae5hym1QxIuE22nx3Yjsl2zqb-QHyJ8Z0d0cqBm5gHaJQOaW5gY1KEKMsbtP7Md1vfQmBAjFgE1ADL8i6drSBIxnaDzF77Ga-CHc6HC9dT55vn1vpm8TEXQJIzwyPbK1vuIR2liXpYU3my-UayOLHEz6JNeRY15-O9EN_RFbtndN-H9HNRkuoWhfHcp5iWNj4tIqOcyYAJ9txMB62b1xGA2w4HOW03cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab2e49c2e.mp4?token=nvQsucOn7VxJ8X2HYJpbp4zwuuvz2CQfLhpOJmQzvYg7QOYWfCLibyBG9WypU7gGkKwFhEBooOQuRzFUYFtlsIDy20XTMOuI1_1SfCOjMRwbN0RT6YaUCUY2t46aLeZ_QecKMjeGFdt1GFCIC0b46r274kVjyYrQOCtMg8Wf79E6YoCVXMFuyWRlgOr2vWMWxL7o2Qg3Mha3TtKNhcfRei43GkYBbqI2q7xJFnS_J4NDH2UhlNBzyryWpjcjDpZ7N7qX5gcLJnQbFQiqsyqvgWgO-gDBtYjsQSnRlLMN77LL2_IRidCJettz9l3_xltOxctIf8R4tjLjfxTyd9WXCZTZTX5w_mCJlghrtA11MJl0e7-BVAmvGJUSrpElT0cl4ynMW-sirXOQsto_IQfnrtvjZ2aORP4L3ojg9EQUClZdiQuYyXeL00-V0KVf0aAUR-zYWYDvIF1ae5hym1QxIuE22nx3Yjsl2zqb-QHyJ8Z0d0cqBm5gHaJQOaW5gY1KEKMsbtP7Md1vfQmBAjFgE1ADL8i6drSBIxnaDzF77Ga-CHc6HC9dT55vn1vpm8TEXQJIzwyPbK1vuIR2liXpYU3my-UayOLHEz6JNeRY15-O9EN_RFbtndN-H9HNRkuoWhfHcp5iWNj4tIqOcyYAJ9txMB62b1xGA2w4HOW03cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
هرگونه موفقیت عملیاتی در خاورمیانه، از جمله در زمینه محاصره ایران توسط ایالات متحده، با عملکرد نیروهای نظامی متمرکز بر مأموریت‌هایشان آغاز و تکمیل می‌شود. تا تاریخ ۲۱ ژوئیه، نیروهای آمریکایی برای اجرای کامل این محاصره، مسیر ۸ کشتی تجاری را تغییر داده و یک کشتی را از کار انداخته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68741" target="_blank">📅 23:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68740">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d66a861bfb.mp4?token=fnmeOj1pyvxAkXVsh2sQWV7eWXIk1pYpkFJ4n-5PpdS8kUdKQGGkpUwbkiU6ps5WQkQvN1DHX0anXtXEYJv-syagFHyUEPXjDa2oaeebcyRMG5aYLKRgGwMab-9_ZPuF3_L0MvDLcUlx2qyF0CZVAB8pP03vHonzN40BiXKQjAfWY-yA8--HhL6MahUWyzhZnm5K6rkoMlZxAPRietOpqQiKtmzA-X29Tt48kiZTw4u-PHPR2cRuDT6auENOwpQ5ciHlGyEtd3zRFA2t-udQUnRgfkZddJTUlWftpcWV1ccdSgyoAe1cQAH6YUsO83R06PsLHkvFXpGk7adN5M_jNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d66a861bfb.mp4?token=fnmeOj1pyvxAkXVsh2sQWV7eWXIk1pYpkFJ4n-5PpdS8kUdKQGGkpUwbkiU6ps5WQkQvN1DHX0anXtXEYJv-syagFHyUEPXjDa2oaeebcyRMG5aYLKRgGwMab-9_ZPuF3_L0MvDLcUlx2qyF0CZVAB8pP03vHonzN40BiXKQjAfWY-yA8--HhL6MahUWyzhZnm5K6rkoMlZxAPRietOpqQiKtmzA-X29Tt48kiZTw4u-PHPR2cRuDT6auENOwpQ5ciHlGyEtd3zRFA2t-udQUnRgfkZddJTUlWftpcWV1ccdSgyoAe1cQAH6YUsO83R06PsLHkvFXpGk7adN5M_jNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
جوزف، رئیس جمهور لبنان:
شما رئیس جمهور بزرگی هستید.
🇺🇸
ترامپ:
ببینید این خیلی خوب بلده خایمالی کنه، الان منم هر چی بخواد بهش میدم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68740" target="_blank">📅 23:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68739">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🇮🇱
کانال 14 اسرائیل:
سپاه سفارت اسرائیل رو تو بحرین زده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68739" target="_blank">📅 22:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68738">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d3140239a.mp4?token=FWT2y6JaGhl0LOfh3Nx8WDkkSpzwqR0-9YCNKKg7pemfFdruM3deyMaDdxVerif8C2X2udtuYzjH-P_LLmWBTIg5DW2AERs7Stl8pbzXzi5VH0a7Sw1jxEy4JHiGJig03NmGbOJ-D1wsI5TzPAdGbgeScVjb8D_2128ep-Npqn8KGw1Yy7S3zov6vQVX5UeoJFZn3c2ljA6Vj3MBfVovR9d9Du44VSrQbRCjndmY60jc5APkQ0f4r6HldIH0iqy-MB8LbVDJRj6civVT7745k3ue1KkSmqwItr3qY1g9M091u-6onb3kje-rPkdOK_waNCiZBJH_LrSMMrFTWIR4nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d3140239a.mp4?token=FWT2y6JaGhl0LOfh3Nx8WDkkSpzwqR0-9YCNKKg7pemfFdruM3deyMaDdxVerif8C2X2udtuYzjH-P_LLmWBTIg5DW2AERs7Stl8pbzXzi5VH0a7Sw1jxEy4JHiGJig03NmGbOJ-D1wsI5TzPAdGbgeScVjb8D_2128ep-Npqn8KGw1Yy7S3zov6vQVX5UeoJFZn3c2ljA6Vj3MBfVovR9d9Du44VSrQbRCjndmY60jc5APkQ0f4r6HldIH0iqy-MB8LbVDJRj6civVT7745k3ue1KkSmqwItr3qY1g9M091u-6onb3kje-rPkdOK_waNCiZBJH_LrSMMrFTWIR4nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
انهدام پهپاد جمهوری اسلامی توسط سامانه آمریکایی برفراز اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68738" target="_blank">📅 22:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68737">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cacafc700.mp4?token=VGM-WOxwQajEhER7RE_lyGMgRUT89jkdbB0FI4n0CJp9-UpnTua0KOR43ufkLjkcifSE0Nur1DnLi0tBqad4vzW-WzpvD1uitoLUwdewEDmpT02qNwmN-QkPLPDtQAAmLGRvycYwnIrk3pyGETXT8vhHItPGZGIuRXlUhP0mIbB6Ncsx6KWqK7cm0jumWhMhwnBRNzpvsOeMocNKDI0NnDTwlltwSXwvcyoLm3DkiybTQDgs0b3uW4_Y41l-O94PANPLjkrno1CYPn2E7LnaatgeXT9DILY6PIxLxWr2rNU7q-9eXmn_n1Iqv5i-EXNr4qzQLILNZNKo3tkaIZLkQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cacafc700.mp4?token=VGM-WOxwQajEhER7RE_lyGMgRUT89jkdbB0FI4n0CJp9-UpnTua0KOR43ufkLjkcifSE0Nur1DnLi0tBqad4vzW-WzpvD1uitoLUwdewEDmpT02qNwmN-QkPLPDtQAAmLGRvycYwnIrk3pyGETXT8vhHItPGZGIuRXlUhP0mIbB6Ncsx6KWqK7cm0jumWhMhwnBRNzpvsOeMocNKDI0NnDTwlltwSXwvcyoLm3DkiybTQDgs0b3uW4_Y41l-O94PANPLjkrno1CYPn2E7LnaatgeXT9DILY6PIxLxWr2rNU7q-9eXmn_n1Iqv5i-EXNr4qzQLILNZNKo3tkaIZLkQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانش آموزی که ۱۹/۷۵ گرفته دانش آموزی که ۰/۷۵ گرفته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68737" target="_blank">📅 22:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68736">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbTohZW8wjm2EtGsK0flKrBe-WwZgSuqttwSNHzjK8iFqTcxtnOYJYct-Z7ZmaSCI11Q7JcQXIE8b1Q6EBJyRknqDAvfAPIOgh9EBfTZ5F83FkDitKDVPCk7wO7qblziZT4i51j9oyfT30BCMOUvb83ogob9D4RvAiRpfFJ2CVE-1zY1uniuNJW9UuWiC-tKJbosNwkXCH9B2MEaHc5MlGxHqu8AcXNdFpcF4EPnBDm6oKqI-kVq-CoemDrRSRqbnAwyU98mkj7rruhjeCYuji-XKi8FTYgvCLrJNePnJI4-BWEeUxyV4mQVSAeBT-HI-KftOirAUUHcLdfY-p-8lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به گفته بعضی از کاربران شیرازی، این اولین بار نیست که چنین اتفاقی می‌افته. ظاهراً چند بار هم دیده شده یه نفر میاد اینجا آتیش روشن می‌کنه و بعد میره؛ اما هنوز معلوم نیست هدفش از این کار چیه...
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68736" target="_blank">📅 21:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68734">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lk2NXXCdLEEQCxkWqy3RMY2orepOBskemT1xWvGoO8StHTNNppONe18A8by2hcM9QQvl-oUEC1jwbcs3XPgQOM5a0lDxIeg0BmzlrOK_8d7IKz6t2yHfZUdMAsBegQCTd5yDu2lqzR0DbjS8vGAlHyYciMetELzTX9Nx8TP1TlFUHz_h4LFFU2nnlDnWU-99vENVkPpLTXKj0t9jNQBudA5vaH1gNDV5V6xk1qOsFaddKPetD7uWWQVIbFMTiYUxoR8dE1nPyR3d74iCbyG6y9nv6y55wDa47dOaEO_xJQyHwxCCQx2R8U_YhlgCyHnCLP0Wz516295FO0Xd1sDyaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OJROh2ynajgk1mdtOvx6eIbUO8x2J1fqjg77ZXjQeLQyazAUhg_SVbVapxPVOY9L-7cnPHz-BftScJugimItoeOijhGO48o-8bB1D4tx42QEX1j6-8j-OAIsesVB-BAR0ctv0vDfokBa97lBlwEC3a3EDFiXM5Puh3n3MXLNgF5YWPAo-_EkFXsPvnUtR5CngnerLkoorr5gT4koWXKL30t5lcNC8IS40XltS_-0Y-GonYsB8cEn0QjNg-mq3C9j95cazGtmLdVIXmSw7URJOpPxgsyl1glzdCeVXZEwlycuoFKDKFJXkZDS9SWCspWvfQ2nUAXOJsAEB_X3_41x3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کوه دراک شیراز در حال آتش‌سوزی به دلایل نامعلوم
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68734" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68733">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EsSI0AVitDYbQajx-7VV73IOKdUxaU433bVXK9DngWihwUL5KF46RIiFm5OEZ2Vs8qtuPUvRE49vLbhO9RliEXWpHdh0nYxgVZnY83I2e8zvmKatc7Bj--uQXHmQlTq0Hi9OAp_3f3EMWmAdAu1kMCJ5csD1CSHgdoIGn35N6fBUD96h9eUBuOLQCHBQnVVhqaFxivSFJPV_K2tPu126khy_vp1acKCxCFXwEZtCpA7tuLDePqcJ6skh_w67cgWLv--dZ_WKlyNKgY6DOONwJpUypUkfgE0Ua5RIkAWVM4ObEZa79INNCXj9xMqGKANBT6BJ2f-M_1keC-JAwmV6Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
گزارش های تایید نشده از آتش‌سوزی در کوه دراک شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68733" target="_blank">📅 20:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68732">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9bba21a8.mp4?token=p_g4M_BShNIn5x_k21N4XP9vefd2V_zvNS5IsGSxo2FtDQQ8mXBq4q5uxcOXMeVManZaJ5IaffKhzo2SG0hnVBVD8CysmyJ8hQVHyhwqsDs3jCyCvuMOU12Mjt3f6j7F2KV94pFf60L2E90nmf0EXIOPtCHo3RBIitJkRT3JFqb3cXoPRi6Hy2jDgOcifC8ULlaFp0_sVEreGld_n7w4i5c-_jwrbYGBx4Q6ApZKh2IdoCA6o0kqqxhsaG8NWmLU8rCFxHzGvI6ecZHBlj-DJ2dAreyqcTAwq_aPWNmhVnVqYDnyf-NbPtuXyM5V1pecuBEFFxXJouSGEa6Syyek8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9bba21a8.mp4?token=p_g4M_BShNIn5x_k21N4XP9vefd2V_zvNS5IsGSxo2FtDQQ8mXBq4q5uxcOXMeVManZaJ5IaffKhzo2SG0hnVBVD8CysmyJ8hQVHyhwqsDs3jCyCvuMOU12Mjt3f6j7F2KV94pFf60L2E90nmf0EXIOPtCHo3RBIitJkRT3JFqb3cXoPRi6Hy2jDgOcifC8ULlaFp0_sVEreGld_n7w4i5c-_jwrbYGBx4Q6ApZKh2IdoCA6o0kqqxhsaG8NWmLU8rCFxHzGvI6ecZHBlj-DJ2dAreyqcTAwq_aPWNmhVnVqYDnyf-NbPtuXyM5V1pecuBEFFxXJouSGEa6Syyek8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
چندی پیش، همزمان با تهدید رئیس جمهور ترامپ به حمله به «کوه کلنگ» مستحکم ایران، چندین بمب‌افکن سنگین B-1 Lancer نیروی هوایی ایالات متحده، خاک بریتانیا را ترک کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68732" target="_blank">📅 20:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68731">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdd4a3d5a.mp4?token=gkZIf30rOg3FUb3qQL2ieMnAKpe2jogi2px5wjxZsj7df0Q-YpPsaqPmM00ikJQcHodDE9zfwWi0MQbYF_B0ALFJTqRZJBcO3M7ryO-P_HYHGOTTlp-oclC9TZKYD2E8jlNfSGWgOmkb20cEEAhSM6ke59fniBsH-ESuFPulxf4QapaVRHDTuvM3H66fj7byj-orfqey32XYUn6QbeSMkj1ehKKSAEHY2JYyZNpbCXK_BWbBktuehmhvSS4oxynpv4lkR5jjUqARQ1BMpsvQZsYxGkdO7bW1yz7h3VgzuTgSFE5mxnk2XeAElrGv-CrW62slG9q0Be06Yr__KJY1Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdd4a3d5a.mp4?token=gkZIf30rOg3FUb3qQL2ieMnAKpe2jogi2px5wjxZsj7df0Q-YpPsaqPmM00ikJQcHodDE9zfwWi0MQbYF_B0ALFJTqRZJBcO3M7ryO-P_HYHGOTTlp-oclC9TZKYD2E8jlNfSGWgOmkb20cEEAhSM6ke59fniBsH-ESuFPulxf4QapaVRHDTuvM3H66fj7byj-orfqey32XYUn6QbeSMkj1ehKKSAEHY2JYyZNpbCXK_BWbBktuehmhvSS4oxynpv4lkR5jjUqARQ1BMpsvQZsYxGkdO7bW1yz7h3VgzuTgSFE5mxnk2XeAElrGv-CrW62slG9q0Be06Yr__KJY1Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست، وزیر جنگ:
به ایران فرصت‌های فراوانی داده شده است تا مذاکره کند و نشان دهد که در قبال تنگه هرمز رفتاری معقول دارد. اما اگر آن‌ها بخواهند به کشتی‌های تجاری شلیک کنند، آن‌گاه ما — همان‌طور که رئیس‌جمهور گفته است — ضربه‌ای ده برابر سنگین‌تر به آن‌ها وارد خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68731" target="_blank">📅 19:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68730">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46342c6e91.mp4?token=SnAyvIU8f4bkD6F6sCFUmb0CzsFsXMJixpBhaWn0EBMUh-eJQHZGomD_xv8Q7zlxdKXCCeYy69cGjo-2Q4k2huAyXWk1eQSzVB3DBoPXs1KIZVAGvY37tfUxPY5Y59k0en2SifDMOQHdo17ihW6MVprdeEeUxujj7y98X0tLgBFt4zvTSR9RzikEdgxs60b88eDXcNOjhSQ9GpXjoNOPOBNOHX70c1DQg_7r9MjfOEpBXOAehZ-q6fMVTJBhN5pzfuVWDUdYlA6DwDaJ15CLeuZgPj8BtQSNHODshnX7TGGW1ScHjCL07K2jsbPKC1a0QbfMRLBuPuewsGiHU6H26w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46342c6e91.mp4?token=SnAyvIU8f4bkD6F6sCFUmb0CzsFsXMJixpBhaWn0EBMUh-eJQHZGomD_xv8Q7zlxdKXCCeYy69cGjo-2Q4k2huAyXWk1eQSzVB3DBoPXs1KIZVAGvY37tfUxPY5Y59k0en2SifDMOQHdo17ihW6MVprdeEeUxujj7y98X0tLgBFt4zvTSR9RzikEdgxs60b88eDXcNOjhSQ9GpXjoNOPOBNOHX70c1DQg_7r9MjfOEpBXOAehZ-q6fMVTJBhN5pzfuVWDUdYlA6DwDaJ15CLeuZgPj8BtQSNHODshnX7TGGW1ScHjCL07K2jsbPKC1a0QbfMRLBuPuewsGiHU6H26w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره حمله سپاه که باعث کشته شدن دوتا امریکایی شد:
«داریم توانشون رو در حدی از بین می‌بریم که هیچ‌کس فکرش رو هم نمی‌کرد ممکن باشه. واقعاً ضربات سنگینی خوردن.
البته تونستن یک مورد رو از اردن رد کنن و اگر افراد دیگه‌ای مسئول عملیات بودن، چنین اتفاقی نمی‌افتاد؛ چون ما بهترین تجهیزات دنیا رو داریم.
ما تقریباً جلوی همه‌چیز رو گرفتیم. اما وقتی کار آمریکا رو می‌سپری به آدم‌های دیگه، بعضی وقت‌ها اون‌طور که باید پیش نمیره.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68730" target="_blank">📅 19:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68729">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3516843a5c.mp4?token=TlO2UEsJbRzB0RHvXoxrGbQIy-k8ureotMcscRPelfb_2hthTzNcGiCkRaMHs7Fh0Rs_ZR7gubt-SDtQo-IBlZ8J3I-7Ab3msCuldZ9Z-MDmpPYIJs9LXh-hZ_5NEz7rN2nJOfOh8FtPrv35F_fTXUSU5o3Uu0euCee6YjsOlpxEq5RYgBzRGPmzouqYyaxuR7IiyidQyYkkNVPCE9Bsov18c_6BuAR2IUGMMB_Z1ET3wInM48t27sjTXUF_vMmBVwz4duLtBDjvrWrHlFAV2SY2NNzMAzvLxtQxQYUG51txpXetceKhSRmf7Iupia_9fOkH9zMxUyjrdPHbTUBt-HjtLY7V4HBfwtLXQU_M-_A7_-SaJC2cvT8GHspGyrriPLs4HZ45RJljB0F9q7QilgIOL1h1ueqixFJWVNTT3210TrC5CO31wAmCOKrxXEKirJIoQ_9YeOGw6cdApxGEcRS9uJX-IcIvUJ-SFirxuT1l1QWiLYgJS7DvywTz8t0ztBCAeRncLjMAdHxcaJt8RT5uPR8YcK7DZGve3w7_FnDlpi3lsoD9IG1rwcBAL85-P4uNEk6WuaUgwePM3Jj9SppRVvsipPA7nRNb_Im-yDSPhhy80VdVvnjh425bt16k5XNVfcoVlMqhbrvWss2wNtu1Cib_OArFThmffby-DC8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3516843a5c.mp4?token=TlO2UEsJbRzB0RHvXoxrGbQIy-k8ureotMcscRPelfb_2hthTzNcGiCkRaMHs7Fh0Rs_ZR7gubt-SDtQo-IBlZ8J3I-7Ab3msCuldZ9Z-MDmpPYIJs9LXh-hZ_5NEz7rN2nJOfOh8FtPrv35F_fTXUSU5o3Uu0euCee6YjsOlpxEq5RYgBzRGPmzouqYyaxuR7IiyidQyYkkNVPCE9Bsov18c_6BuAR2IUGMMB_Z1ET3wInM48t27sjTXUF_vMmBVwz4duLtBDjvrWrHlFAV2SY2NNzMAzvLxtQxQYUG51txpXetceKhSRmf7Iupia_9fOkH9zMxUyjrdPHbTUBt-HjtLY7V4HBfwtLXQU_M-_A7_-SaJC2cvT8GHspGyrriPLs4HZ45RJljB0F9q7QilgIOL1h1ueqixFJWVNTT3210TrC5CO31wAmCOKrxXEKirJIoQ_9YeOGw6cdApxGEcRS9uJX-IcIvUJ-SFirxuT1l1QWiLYgJS7DvywTz8t0ztBCAeRncLjMAdHxcaJt8RT5uPR8YcK7DZGve3w7_FnDlpi3lsoD9IG1rwcBAL85-P4uNEk6WuaUgwePM3Jj9SppRVvsipPA7nRNb_Im-yDSPhhy80VdVvnjh425bt16k5XNVfcoVlMqhbrvWss2wNtu1Cib_OArFThmffby-DC8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ:
«قطعاً به سایت جدیدی که درباره‌اش حرف می‌زنن حمله می‌کنیم. کل این ماجرا به خاطر سلاح هسته‌ایه و اون‌ها دارن تلاش می‌کنن دوباره یک سایت هسته‌ای راه بندازن.
ما اون سایت رو هدف قرار می‌دیم. هر جایی که حتی فکر ساخت سلاح هسته‌ای توش باشه، با قدرت خیلی خیلی زیادی بهش حمله می‌کنیم.
هیچ‌کس، جز خود ایرانی‌ها، نمی‌دونه چه میزان خسارت بهشون وارد کردیم.
اگر همین فردا هم از اونجا خارج بشیم، باز هم یک موفقیت بزرگ به دست آوردیم. ولی ما فردا نمیریم.
راستش رو بخواید، هنوز هیچی ندیدن. ما تا الان باهاشون مدارا کردیم.
من اصلاً باور ندارم که بتونن دوباره خودشون رو بازسازی کنن.»
🎙
خبرنگار: «فکر می‌کنید ایران سانتریفیوژهای هسته‌ای رو جابه‌جا کرده؟»
🇺🇸
ترامپ: «ما مواد هسته‌ای رو ردیابی می‌کنیم. اصل ماجرا هم همونجاست و به احتمال خیلی زیاد، خیلی زود اون منطقه رو هدف قرار میدیم.
کار زیادی هم از دستشون برنمیاد. معمولاً همچین چیزی رو علنی نمیگم.
اگر فکر می‌کردم می‌تونن کاری انجام بدن، هیچ‌وقت این حرف رو نمی‌زدم. ولی خیلی زود اون منطقه رو هدف قرار میدیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68729" target="_blank">📅 19:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68728">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0f808d08.mp4?token=HzG0fwOQWhNrhJPSsW9cvrRxp0TZvvLrUirzfQxbo5KS9E_7inN3J2JihIvSV13tc04U2T2AA27U5tiSAQyHpH-fkidCaL2mR-1QMrzp8BWibxILucDTSi_hhvsKr0soWzLLy2KRMA_NnulS0mpNOGT8QaDKhh3X5egv0fji_2TdTa4dMiQ9iLhN_MiS5GmfuKN6vzoqLscOBXIGjZNmv_WLdWP4WsjrPbxgI7o-OTQ4lzmpCuUuyqDOpGb5mI-X2tBrje4MWbb_GQSJLm1HP6SF8VV-gaY2Mfi8pki68SKDvMwWd5ThpOqZqXQ5lzb7DFbID5mEM2GQuRXrNaJQSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0f808d08.mp4?token=HzG0fwOQWhNrhJPSsW9cvrRxp0TZvvLrUirzfQxbo5KS9E_7inN3J2JihIvSV13tc04U2T2AA27U5tiSAQyHpH-fkidCaL2mR-1QMrzp8BWibxILucDTSi_hhvsKr0soWzLLy2KRMA_NnulS0mpNOGT8QaDKhh3X5egv0fji_2TdTa4dMiQ9iLhN_MiS5GmfuKN6vzoqLscOBXIGjZNmv_WLdWP4WsjrPbxgI7o-OTQ4lzmpCuUuyqDOpGb5mI-X2tBrje4MWbb_GQSJLm1HP6SF8VV-gaY2Mfi8pki68SKDvMwWd5ThpOqZqXQ5lzb7DFbID5mEM2GQuRXrNaJQSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ :
«جوون‌ها رو می‌کشن؛ انگار هیچ ارزشی ندارن، انگار آب‌نباتن. واقعاً آدم از کاراشون شوکه می‌شه.
همین‌جوری الکی مردم رو می‌کشن؛ بیش از
52 هزار نفر
کشته شدن و هیچ‌کس هم درباره‌ش حرفی نمی‌زنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68728" target="_blank">📅 19:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68727">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18745bb1ea.mp4?token=oGsCLJDDHXkJfqUjhFF5sGyrr9NDya12og5rbWXk-MpICpge19wWiQPuImC3hfPueE5iMRAK3fYH9ee1xeV-oAY0utxPpf3mtTVP2DK3z2AsEkAjSZfMzrhFeuWk0bbHCbV-kfKfyulNnIqcFkGsjxRY4pHF7rYPpj6W5g_uzJXTw55Plkd71BYDQ7BCxSwMOeTlzcuW3YrOtMy21eQJzQKBDKpUTiK0sz-7c5a7o9QKGajU-5srsZeTUTwi1OZV3GeLPoL5BQAOI9po_iOvNIlxvhdWP5KcmpmX_H8CzgnEiGyEFmJt4XfYWU7xJO7DRiiRGZ55aj7I4UXgiRc6bjtkaITA7dxXX0EVuS_U4q7bzA8nAAyS_IlYuCP0TptUVoLA9yCCyBoJqBH51XgIT7KejhyClpmuUubKJKtLJJ339DC7MvCRayMMP3F7rzCTtzEkDP0S9gLTx7k-OejTh2mlUYesGpRuHDeOERTN7ZK8QnA7p2m_WJwpliNG9rHiMTP5kV_LxJyzcGxEKL8JJ7g3QAumwopzTxBeJ1uYdfkNxEIVsP-UwrDZ9nQQFwuFyw_oi0Nt988Pq79wYTJRYcPIPc1t2OzhDWO9aRmQ1t7_ZIs2pc1AGbNWYkPTIWdqT3RBiqA9RKLFRAyIfT42g8MCYNq4rsNbFSYBAceWZOs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18745bb1ea.mp4?token=oGsCLJDDHXkJfqUjhFF5sGyrr9NDya12og5rbWXk-MpICpge19wWiQPuImC3hfPueE5iMRAK3fYH9ee1xeV-oAY0utxPpf3mtTVP2DK3z2AsEkAjSZfMzrhFeuWk0bbHCbV-kfKfyulNnIqcFkGsjxRY4pHF7rYPpj6W5g_uzJXTw55Plkd71BYDQ7BCxSwMOeTlzcuW3YrOtMy21eQJzQKBDKpUTiK0sz-7c5a7o9QKGajU-5srsZeTUTwi1OZV3GeLPoL5BQAOI9po_iOvNIlxvhdWP5KcmpmX_H8CzgnEiGyEFmJt4XfYWU7xJO7DRiiRGZ55aj7I4UXgiRc6bjtkaITA7dxXX0EVuS_U4q7bzA8nAAyS_IlYuCP0TptUVoLA9yCCyBoJqBH51XgIT7KejhyClpmuUubKJKtLJJ339DC7MvCRayMMP3F7rzCTtzEkDP0S9gLTx7k-OejTh2mlUYesGpRuHDeOERTN7ZK8QnA7p2m_WJwpliNG9rHiMTP5kV_LxJyzcGxEKL8JJ7g3QAumwopzTxBeJ1uYdfkNxEIVsP-UwrDZ9nQQFwuFyw_oi0Nt988Pq79wYTJRYcPIPc1t2OzhDWO9aRmQ1t7_ZIs2pc1AGbNWYkPTIWdqT3RBiqA9RKLFRAyIfT42g8MCYNq4rsNbFSYBAceWZOs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار: هیچ نشونه‌ای نیست که ایران بخواد جنگ رو تموم کنه. پس برنامه‌تون چیه؟
🇺🇸
ترامپ: تو از کجا می‌دونی؟ چطوری می‌دونی که نشونه‌ای وجود نداره؟
چرا تو چیزی رو می‌دونی که من نمی‌دونم؟
تو نمی‌دونی چه گفت‌وگوهایی پشت صحنه در حال انجامه. اون‌ها به شدت می‌خوان ملاقات کنن تا بتونن این قضیه رو تموم کنن.
اون‌ها به شدت می‌خوان ملاقات کنن.
تا وقتی که آماده نباشن به شکل معناداری ملاقات کنن، ما هیچ علاقه‌ای به ملاقات نداریم.
ما دارم اون‌ها رو به سطحی پایین میاریم که هیچ‌کس فکرش رو هم نمی‌کرد. واقعاً دارن به شدت ضعیف می‌شن.
البته یه چیزی رو تو اردن رد کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68727" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68726">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/68726" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68725">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXcaO_bZ62-ZOWK0KAVev3X9JQ9eFPcEZeO7z-Rri483ncPQmvEbI2P4-94Mq2-vCGcFt0ThTx8V_JCmA2WDsx11E7kpR7kLqbPhimT1HjLdsq1m-bdxwZ98-z6ueLfbzTGpQOgP9w6cmZ_FS9sOSi3_Ioafw1NDTms6dSp75jMhhdw-kRNzgN4_Dq1a3hUNVJiuO1hpRqgkzXXCHVTFrx0917FclhwbBLI-01kEsFEYhuDvWoF2-h3OMjnIO9AdlgpiH3-uV-h5u8da7I82becVrfHIWsWNVMMR-tBwyGDGmYbdN0RdIEcGDWKsAAW8IcUehtThn_n01zTH6EkU-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68725" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68724">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d3d23d787.mp4?token=r0kflE5_bySR5nIi5EZpsdSfsU97_TKzocJy4faAEfL8YN_mewPp3vutqafDJwLY_US4xVH18nTzmXydAKvJ2N89oSTCpL8F_XOBGMjgPouUPv_XzYHwNIC4-9EX_xqWMGqOzDMQulIbZqjmxZw-GoWDWYOmXHC4HOHDrms3_A33uuoUmYL0O0Y3waJUknTVVw_mKisXXVQNpsVPx4j3_0sOiKZ-gKF-r4QNmz2VjFy_NAi7bYO63e6zSP4skVeL9-WYQGnFX6pmIuCU2qyn-LqxDz1jui5vyrODoFqmTLT8SkoM7meuiVuVmJjI3ApcfXZ681hBnhwb5uPVFJGnwYLHYkFvxPwvFcD8uukNDCePP3iGzexfNEDkLi28T4Qeri9dp_r1UG-PaoLPOVaRe5JSav-guru39BFitxqVQ7_XZx0dLay1dduBWdIF0OsNufv9ZAF74OSfdSHelbGXjqq4xdfI5NaXsO5O-ASUg05Q9vs8JzFglNOATfpCbaThxaU3i1R1v8WSOQYvSewxEzthyQoHBqeQxwvCp8qsMMhnDx5pQEUZi1cam9HjH52r16JicLbmkYtI_bq-kdX3of0XBoK23rCBuX-8iZvky-fZzZ3G4rvvsGqA4GcBQK5CyGTn2H2JonC-si876M16GW1AFJ1OpJuh7uASvyOmneg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d3d23d787.mp4?token=r0kflE5_bySR5nIi5EZpsdSfsU97_TKzocJy4faAEfL8YN_mewPp3vutqafDJwLY_US4xVH18nTzmXydAKvJ2N89oSTCpL8F_XOBGMjgPouUPv_XzYHwNIC4-9EX_xqWMGqOzDMQulIbZqjmxZw-GoWDWYOmXHC4HOHDrms3_A33uuoUmYL0O0Y3waJUknTVVw_mKisXXVQNpsVPx4j3_0sOiKZ-gKF-r4QNmz2VjFy_NAi7bYO63e6zSP4skVeL9-WYQGnFX6pmIuCU2qyn-LqxDz1jui5vyrODoFqmTLT8SkoM7meuiVuVmJjI3ApcfXZ681hBnhwb5uPVFJGnwYLHYkFvxPwvFcD8uukNDCePP3iGzexfNEDkLi28T4Qeri9dp_r1UG-PaoLPOVaRe5JSav-guru39BFitxqVQ7_XZx0dLay1dduBWdIF0OsNufv9ZAF74OSfdSHelbGXjqq4xdfI5NaXsO5O-ASUg05Q9vs8JzFglNOATfpCbaThxaU3i1R1v8WSOQYvSewxEzthyQoHBqeQxwvCp8qsMMhnDx5pQEUZi1cam9HjH52r16JicLbmkYtI_bq-kdX3of0XBoK23rCBuX-8iZvky-fZzZ3G4rvvsGqA4GcBQK5CyGTn2H2JonC-si876M16GW1AFJ1OpJuh7uASvyOmneg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای، (خرداد1384):
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68724" target="_blank">📅 19:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68723">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇷
ابوالفضل بازرگان تحلیلگر سیاسی وابسته به حکومت :
⏺
بی تعارف نشستن منتظرن جزیره بوموسی و خارک و لاوان بگیرن
دارن ماه ها روش تمرین میکنن برای اشغال این جزایر
برای اینکه یک هفته دو هفته نگهش دارن و یک کارت جدید بزارن رو میز دیگه برای گرفتن ذخایر هیچ مشکلی ندارن
🎙
مجری : یعنی پی تلفات انسانی به خودشون میمالن؟
🔵
بازرگان : اره!
اولن که تو جزایر ما هلی بورن بشن ما متاسفانه باید از خاک خودمون جزایر خودمونو بزنیم
به ویژه بوموسی که فاصلش دوره
اگر صبر کنیم اونقدر که برسیم به جایی که یکی از جزایر گرفته بشه ، بگن حالا اگه میخوایی جزیره پس بگیری باید تنگه باز بشه ، تنگه هم باید تحت مدیریت من باشه یعنی مثلا من باید بیام تو بندرعباس پایگاه نظامی بزنم و ذخایر اورانیوم هم باید بدی
الان میگن تنگه نگهدار ، ذخایر بده حالا اون موقع فک کنید میگن خارک یا ذخایر ؛ دیگه اون موقع مگه میشه ذخایر ندی ؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68723" target="_blank">📅 18:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68722">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQ7XCuVrl5ZJK247cjswoK60s70y3GbxMJ5iUZYKBmt2ZpPuzsYHuah-cSWtZ0FQIpYO70INUf6SJt3hqGwwWR-S5r6TluTRnLdoA-K3bOvwDscEA2sRsVv6zYKayvxil52xUm95liU9OzsJi4li5bPHRINpzjjU9tdnMFn9-9ut5uvRAu3Ij4rzTY1oaXpXLHXCETZRvkcLb5uVc4IeJ-pw_h20JrankoZlT7QhpqLxASVcfAhuoEnEfpAlDLEkjDpxh-1sYLpgO9GAs_tOa4NdDTlQh_K9EHz5xS-9lJHx8s0IlMhTMyrFEdSKqz3_0NN0OCRl89Ocm7Ci1NDlkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پست جدید ترامپ در تروث:  این آخرین نفر از بین بیش از 52 هزار معترض بی‌گناهه. وحشی‌ان!!! دموکرات‌ها کی می‌خوان بالاخره بیدار بشن؟؟؟ این گل‌محمد محمدی، 23 ساله هس. امروز صبح توسط حکومت جمهوری اسلامی اعدام شد. تنها. بی‌گناه.  @News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68722" target="_blank">📅 17:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68720">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/f0IPxxrypcKrYFdw9WVWQbdBJL19pI6HFL0bo77QCiYlg_F9pepplWtCVKM5uoTZ13ty02ErdRgBoj9xTRysVeFi6GOWHyQVM97L2IU2sjmtcE6RbewVxdBhsnI-4S0ZsHrpHHqQ-1OVGEqPvngAx8utgTvQn2kEwVfT7ONpWNniAJ9zhHkxdI4IuZNnoBP7ceBeS903Igkvxf6KRqcuchOIOXX_rfCBBplz_2tXpJBJ-85WIY7Zf2-aGUpl0zkHz3p0n3m4raXxFv4gMRz0mGNuN7tR9AsKrP5n2_TCxE7LkF_PlicSdpIVgLYFR5KQQT5hnZvcd2fC6kpVeIfnNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/cHJau6wFAOw4kuOSAizkP5Ob3P5I_rNAQHseCLVXal2zFhdcDGSOMZuc1Blah5IVrRn5LuHKt0yTeD6sMimpsCfiCJ7x9_TcZSWIF9imMaXAUJ5LZ_bavZ9DmgeyHP9LJ5gtvbSpH51_Qv3uPcxsVigZDVJVlMlILjbyf1e4FADECIH1MOyeY7p_PGuaNMpUXyFjMvpbbsPi4iCv0AHqX_7r5qN-81hySsJzM7EjOo5ybd04iCyDQrDPEvf8Kv_6GK_ZsoT_1rnO6IApzvOXvLkGtCkUMp7E4wxgNHI_Ew1qnH_gizTLuGfzbVUXxKijx0gFxgLyIfPWyAsLeoRnWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پست جدید ترامپ در تروث:
این آخرین نفر از بین بیش از 52 هزار معترض بی‌گناهه. وحشی‌ان!!! دموکرات‌ها کی می‌خوان بالاخره بیدار بشن؟؟؟
این گل‌محمد محمدی، 23 ساله هس.
امروز صبح توسط حکومت جمهوری اسلامی اعدام شد.
تنها. بی‌گناه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68720" target="_blank">📅 17:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68719">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c7e1427c7.mp4?token=GguankMbnORhSmYavvBC37a2ha7jJYa2Z04GsV_DCosjJWl0O_LCLArnppPYRKmllx80kkzeKu6huSS4UBiKKs0s19PdtFjIjZ7jlHCcQXxW8bzdJm9Z6tvx7E9ILWx931DUWjp5qHA5dErrBX-Gnv_qLLE3xpLJc5H57lk3d4c-_kD-rWd0l6UiZXvpBGl4yhPPhomHLxZciyjf77WcsBVqb2MB7a-DuzlpdRe0xq8GdtSsU8EB6g6PknQenxdPMV9brqixIFv7UctE7wPpl122ppIhIsWhwdTeCcQf148ImoOBA7VL8bgKUZkYFpWRxzXr_LmR4D9SP9KwJ8oP6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c7e1427c7.mp4?token=GguankMbnORhSmYavvBC37a2ha7jJYa2Z04GsV_DCosjJWl0O_LCLArnppPYRKmllx80kkzeKu6huSS4UBiKKs0s19PdtFjIjZ7jlHCcQXxW8bzdJm9Z6tvx7E9ILWx931DUWjp5qHA5dErrBX-Gnv_qLLE3xpLJc5H57lk3d4c-_kD-rWd0l6UiZXvpBGl4yhPPhomHLxZciyjf77WcsBVqb2MB7a-DuzlpdRe0xq8GdtSsU8EB6g6PknQenxdPMV9brqixIFv7UctE7wPpl122ppIhIsWhwdTeCcQf148ImoOBA7VL8bgKUZkYFpWRxzXr_LmR4D9SP9KwJ8oP6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمعات شبانه
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68719" target="_blank">📅 17:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68718">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaTtsbWQ_e8aR4eep3A67xI5ouTAkIJk6txnk9C-4cIIgtVbnBoJDT2NWNaskDHnvG2mgW0s1X-fSYhYmp2TjD0Lv62_E32CY-lmNTTKhYj3vihlvjogKz6Ifg632uZmx4ksO3HnmbI_fibYwdEsljKTQrQIsiPxX8iGULD5ZS0L0zgIh5ukjfuBXwDCQKQZzpV9u4Mp0Ww_xrBmwC7rJpyjZeeBNjMrTsRtZ-P4IGjja9kOYeJSGdRinOh8s-5KWF50mAfy6GPkjvqlDX3biC0I1Ar0Rwuf7AKlwa9-dZr0UUzZ43iXPoacO9yrKqx_7SdxZ-ALAUQvl8NiqxGlIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
هویت نظامی آمریکایی که در جریان انهدام کنترل‌شدۀ یک پهپاد تهاجمی ایرانی در پایگاه هوایی اربیل در تاریخ ۱۹ ژوئیه کشته شد، گروهبان «مایکل سوینتون»، ۳۰ ساله و اهل فایت‌ویل در ایالت کارولینای شمالی، اعلام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68718" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68717">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da37587eed.mp4?token=ECn6ke_OaqmQWM5Y_JHpidV3iZfUvvEKEQ1MMbuMQLRQo0o9XXRv_W5pK4ykDbsmiEhlxzol8euaAd3tNtvNVUL02buNiHs6Q3Wt9Xx-4jSzMS1Vn-7sMhV-FImruG2hQ6K0FmpAF4LVkfy8oW13lykYjOK26a7xMy2buGAanvfP2JNMMyv0nuKqR0Wa_pOTUSPIvvC48AlRmK44H_etdgc-SUTk0i8qsk5YpxRCl1edZvaFu122Qqb0tA-Y9jHIVod6rYqdXhN5H0bgVt1WnIk3afzwshg5JzyDDonYQVCMC90qVwKlI_c5aHwbqY_qp3vxjelB-GJxWAh-bMDD9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da37587eed.mp4?token=ECn6ke_OaqmQWM5Y_JHpidV3iZfUvvEKEQ1MMbuMQLRQo0o9XXRv_W5pK4ykDbsmiEhlxzol8euaAd3tNtvNVUL02buNiHs6Q3Wt9Xx-4jSzMS1Vn-7sMhV-FImruG2hQ6K0FmpAF4LVkfy8oW13lykYjOK26a7xMy2buGAanvfP2JNMMyv0nuKqR0Wa_pOTUSPIvvC48AlRmK44H_etdgc-SUTk0i8qsk5YpxRCl1edZvaFu122Qqb0tA-Y9jHIVod6rYqdXhN5H0bgVt1WnIk3afzwshg5JzyDDonYQVCMC90qVwKlI_c5aHwbqY_qp3vxjelB-GJxWAh-bMDD9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شاهزاده رضا پهلوی در گفتگو با رویترز:
«دخالت خارجی در ایران لازمه. این مداخله در واقع می‌تونه باعث بشه جان آدم‌های بیشتری نجات پیدا کنه؛ آدم‌هایی که در غیر این صورت ممکنه کشته بشن.
جایگاه من به‌عنوان رهبر دوره انتقال اینه که مقصد نهایی نیستم؛ من فقط پلی هستم برای رسیدن به اون مقصد.
برای اینکه بتونم نقش یه داور بی‌طرف رو داشته باشم، خودم رو وارد هیچ جناحی نمی‌کنم. نه طرفدار پادشاهی هستم، نه جمهوری.
وظیفه من اینه که مطمئن بشم یه بحث سالم شکل می‌گیره و در نهایت، این مردم هستن که تصمیم می‌گیرن چه نوع حکومتی رو برای آینده‌شون می‌خوان.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68717" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68716">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🎁
بهترین اسلات‌ها با چرخش‌های رایگان یک بت
💥
تسویه سریع و آنی جوایز شما
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💯
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68716" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68715">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDsQ6Eo4Wx4JL4Ms77Sc95Ml9oBmK4lGgWO4l4lnNjcnOU-lgTSvXakoJwduLRe6SrtGb4CKrhWwRQVX1rVkh7_8ducelPX--Jl9f8TPJOV7YXenipJ_QxADRyv-fSVwFCd1aF_OuV4gPWB7eRi8nGz-3s0vW3DdRXPgI3FcjFegjUCHOvJlvj_mhxv2Dc72tVTn9oZc4MMzzIjf82PZrtde5joBlhD-YfWRq4FF7D0tEvS-pyel4Ci6wIvpAA6oae3ynR5-qzKaIerTiTdpyazFpMht1yeRkpPM4lXaRcnf1t6cP-x8CTHLFqUYH7qQ6DznK5ysoyUM3DaluHIMLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
فری اسپین‌های بیشتر، هیجان بیشتر!
🎰
با واریز از طریق کریپتو، ووچر پریمیوم، ووچر اتوپیا و اتوپیا، بیشترین پاداش را دریافت کنید!
✨
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68715" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68714">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCFM4Z-OXPSz49y2bEbHU0Ac0KRYQQA9P5BF9gzBGxLlQfIOEPBQUVNbAdXRFuVidbQAHM17B3gcPAPlgdF6Mxa8k16KI8SKGmHsqNe9y5m8Gh8BIbPvimsbsyUYBGq49_AAqkgu0R_bPyMivrVVVtMNXaCsKYwznewVioyt1XJtb2LEzCmQ0derr-YeTrK_uBgan28UO8m__TWvdU2IyDTHaZyUqPVqfMXDWiAvG_VhjPKwKnBlryoR3y0YV9rhnY9Q7GvQ42qPW-jlImUZvFzODHPzuXXR83zpqqVI3fNhZT-Ql2pd45dU25HyjGSTt_Rg7XI8ilqST4fb0LgNaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مراد ویسی، عباس عراقچی رو فالو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68714" target="_blank">📅 15:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68713">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‼️
🤩
عکس یامال و تیم ملی اسپانیا روی پهباد شاهد چسبوندن که بفرستنش سمت مواضع آمریکا تو منطقه  @News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68713" target="_blank">📅 15:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68712">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6161f8d4.mp4?token=WArrSPx1E7ZmF_KxdHyfj1pnzYPKBXg0Oq11MeaSqEnZipHWWgcEaA-8aAt47FFLB78se6whC0_gGoZQaPVr26sTzxmgrH6gRlwYDqwnAf2yXtIcOaIOKITSeVuYsX-XGvvtwxpIV0vYnCU3RV-kmIIodj13rnrrwLroPvHw34oFA4ef3uO1B8iIAvSeKGYEazEmItaW5Xe-bskSWE-kZynwl3a34F-o1hTHTAGa45YXw6Vap-bPeMdo-sJ4XJM0kS-pgaf5XI9jM6OjtxUoR78lC5lfROdhYb-t4D7uLPwbFI2Wz0nrHBDIt5-_StpqePTfY-BReypeHmOyNk4XgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6161f8d4.mp4?token=WArrSPx1E7ZmF_KxdHyfj1pnzYPKBXg0Oq11MeaSqEnZipHWWgcEaA-8aAt47FFLB78se6whC0_gGoZQaPVr26sTzxmgrH6gRlwYDqwnAf2yXtIcOaIOKITSeVuYsX-XGvvtwxpIV0vYnCU3RV-kmIIodj13rnrrwLroPvHw34oFA4ef3uO1B8iIAvSeKGYEazEmItaW5Xe-bskSWE-kZynwl3a34F-o1hTHTAGa45YXw6Vap-bPeMdo-sJ4XJM0kS-pgaf5XI9jM6OjtxUoR78lC5lfROdhYb-t4D7uLPwbFI2Wz0nrHBDIt5-_StpqePTfY-BReypeHmOyNk4XgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤩
عکس یامال و تیم ملی اسپانیا روی پهباد شاهد چسبوندن که بفرستنش سمت مواضع آمریکا تو منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68712" target="_blank">📅 15:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68711">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVGjYCWe33vJ66vsxyBHJyx0wBRBENyTr91YFNyFll72VQqIgMbRs79Ytt9i_mrF-sWx-zORXioZiIAAfrDEldUpWQe26oXGXUaq4it8qr238c323zEP4TZ62sU1BAuctR-rjdU4qDnEnFEBL1STH9csebcLBec89zBidwYVCLyoUJurMNMuC4HZBoAgWwB4QiGwiCubFUOKC5Y5ae3XPdb0CXeywHI4kOZE3c68bYuuqJLPAIxmfEwvHDzP8T2vxLRJL6UGtMty55oQIYjgouvJSYU6G6xjt6lrfcg0XTeDwyTeLdIZ1wRM8HeNWLfdoZF3NW1yQz0RvyDCYlOpJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
با اعلام مقام‌های کویتی ،  چندین نیروگاه برق و تأسیسات آب‌شیرین‌کن این کشور در جریان حملات روز دوشنبه جمهوری اسلامی هدف قرار گرفته‌اند و دچار خسارات عمده‌ایی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68711" target="_blank">📅 15:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68710">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd31fc49e.mp4?token=cgyXeV0JOGD4jstzYp3jua1dTTIKTa8BMlRfEpTrpe4Ock24w282Php2tvtAfWcA272mRjUVoV82_Kzz-4PIZyETH7Myibu4y5C56EkTsEbWsTTK9aMuB-Jq-d1CO1ZTQ-NqW_DuLqpUAgjX11clgfOC7-SgBOxMu6aL-cGv5r2BfvR57nUn1Dy7FZXeUqhltOLm4hmXVrwvNoCOLdbFryhC3zBzQwGirFCGhteaxBANjWrqYceaf3Qiz-ergj_drmygUS4FN1HfVXbzCBBj8vperVG_ZGGVvzD8KIl64gSSeopgXuj_W5TdausOmDYZ0RmxC95RfBEBRspAfDtP9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd31fc49e.mp4?token=cgyXeV0JOGD4jstzYp3jua1dTTIKTa8BMlRfEpTrpe4Ock24w282Php2tvtAfWcA272mRjUVoV82_Kzz-4PIZyETH7Myibu4y5C56EkTsEbWsTTK9aMuB-Jq-d1CO1ZTQ-NqW_DuLqpUAgjX11clgfOC7-SgBOxMu6aL-cGv5r2BfvR57nUn1Dy7FZXeUqhltOLm4hmXVrwvNoCOLdbFryhC3zBzQwGirFCGhteaxBANjWrqYceaf3Qiz-ergj_drmygUS4FN1HfVXbzCBBj8vperVG_ZGGVvzD8KIl64gSSeopgXuj_W5TdausOmDYZ0RmxC95RfBEBRspAfDtP9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ها؟
درست شنیدم؟
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68710" target="_blank">📅 14:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68709">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
صداوسیما:
دقایقی قبل نقطه‌ای در ارتفاعات خرم‌آباد هدف حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68709" target="_blank">📅 14:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68708">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🇮🇱
وای‌نت:
مقامات ارشد اسرائیلی مدعی‌اند که تیم «جی‌دی ونس» مانع از برگزاری دیدار میان نتانیاهو و ترامپ می‌شود تا از اتخاذ مواضع تند و جنگ‌طلبانه علیه ایران توسط ترامپ جلوگیری کند.
نخست‌وزیر اسرائیل قصد دارد این سفر را با مراسم خاکسپاری سناتور گراهام در ۲۷ ژوئیه هماهنگ کند، اما تا زمانی که از قطعی شدن دیدار با ترامپ اطمینان حاصل نکند، به این سفر نخواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68708" target="_blank">📅 13:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68707">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f5cc929c.mp4?token=W281K74lRxgwKXZ-MRWO5V1xXKVuMZvImcQzwyc4CZrNQ4_wm4FWXPSImyOgLl9hYOlAP2DD5NP5dg7_f1Q3JpIB5-1OsBFbGQfACbCSUZRaEwgHUBJ1dB8rL_QEd2tQjuwFrDXDul7XmKOoaIaMTN_jDqWSzOwmN2l2TUPs6EvJIL3gr9LepFF__T9eIL058hoDDVq666vWK58i8QtfBYxTxFCH_jXA9kNktLhFdL18roD3dpm4_Uy0XMv-VaaIPm9fuFtcIISrOPzm5FGYpyhPFkZ97BAsj7qkAUd48iss6qp4hxwO8peVHRw4SGT6oXoJsa4h5O7tluM6ZwcBsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f5cc929c.mp4?token=W281K74lRxgwKXZ-MRWO5V1xXKVuMZvImcQzwyc4CZrNQ4_wm4FWXPSImyOgLl9hYOlAP2DD5NP5dg7_f1Q3JpIB5-1OsBFbGQfACbCSUZRaEwgHUBJ1dB8rL_QEd2tQjuwFrDXDul7XmKOoaIaMTN_jDqWSzOwmN2l2TUPs6EvJIL3gr9LepFF__T9eIL058hoDDVq666vWK58i8QtfBYxTxFCH_jXA9kNktLhFdL18roD3dpm4_Uy0XMv-VaaIPm9fuFtcIISrOPzm5FGYpyhPFkZ97BAsj7qkAUd48iss6qp4hxwO8peVHRw4SGT6oXoJsa4h5O7tluM6ZwcBsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پاسخ دفتر شاهزاده رضا پهلوی به صحبت‌های عباس عراقچی درمورد توافق پهلوی با اسرائیل برای تجزیه ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68707" target="_blank">📅 13:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68706">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427c084f6e.mp4?token=gzG0hEFVK0Fe4rt4Ta1y8xKSV2cbwZG_DDu0kfjEuMYE5VRAwFCcizHuUvgHYv8F-erR3ZsVRRv1RjbOFtq6HlXModIo-2QyxmlS2FmEp8q93CR5CwcFM0AEiaxD9boH0nZKzwHeYRR15OYGHlEG-7O33zTnqlZ1a056maDOup1HqYxcktlUyIGr6DxETuCOwlCwT91cyTwPXsP7o9SVxLS1A7L-uqmgCKq1B6MuStKSqwrYi1vQ8I8Ll6NPbzNMYhjEGsP9qMcas7cNSsJFXm0lKd0ulbUndig1qtM4TZ_rWmyAsOwsDbVaM43s6Efvn58Ub8YI_AMuA9sn3Io0lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427c084f6e.mp4?token=gzG0hEFVK0Fe4rt4Ta1y8xKSV2cbwZG_DDu0kfjEuMYE5VRAwFCcizHuUvgHYv8F-erR3ZsVRRv1RjbOFtq6HlXModIo-2QyxmlS2FmEp8q93CR5CwcFM0AEiaxD9boH0nZKzwHeYRR15OYGHlEG-7O33zTnqlZ1a056maDOup1HqYxcktlUyIGr6DxETuCOwlCwT91cyTwPXsP7o9SVxLS1A7L-uqmgCKq1B6MuStKSqwrYi1vQ8I8Ll6NPbzNMYhjEGsP9qMcas7cNSsJFXm0lKd0ulbUndig1qtM4TZ_rWmyAsOwsDbVaM43s6Efvn58Ub8YI_AMuA9sn3Io0lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حملات دیشب سنتکام به مراکز فرماندهی نظامی، توانایی‌های دریایی، سایت‌های پرتاب موشک و پهپاد و سیستم‌های دفاع هوایی جمهوری اسلامی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68706" target="_blank">📅 12:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68704">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YAhHs0x4dsqZzgQSzu5h4p8pxiX6RKmZ3plWNLD56YglWKVzi9aJDjMq_GIGgL8JzdWlaLE08O2AXoGhNoXZ_8KZFJEPMFjAMRIABavVtaSVZQwTqq6iS2EsWPMLk9ekPm60lwPKMzP2ywjo040gmvg3wYC3vr6eit7VCG57jD2mERuI0L4ATjcxrNtdUH20adnVIF7geFLY-6WEgqGIsO95owYRdpbgWJbns0igWFbfOc_JRAihpq3JSY-sUCCNUMoHj7D_QR4jQWYI29Gnplm9CRgJr8mX7uD1qz49EAx5DRAnRY9mRYjNcTxEvGxil-KObQqUo-PkXR5fyEP3Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UOlYnPCct0FS0I5V_SJr5DuHPZWLy-AWsfNw6yFz8c5fhMi7hT5NIGskaiE02BJVDCcMYoM1_8KJc-UFN1B-ZCbuCrdOVKGFjFF0j8rfYOMuSHV-GVrYF8bH11Xc2unvXc3NZHQUNwyycbzfE-oEKkxJXf8FsgyDaCaNSdWsp1kMyYDt09DSmgSAjXgCcdi9vnoAaEZHD8fqca5ETG4t9IS_2pGFEXsRXvoWLgVAWn6I4RuBZl5ihSMq8I955FbL9sHyVLcX_FG1k3D1LZwElsUb44FqsDfO_Doy52v0sIG4PN57TwyiK8WpqnjFV8RE6fIkrBqUq9Up9PdOX9zaeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
دقایقی قبل سپاه از زنجان و همدان به سمت پایگاه آمریکا در اردن موشک شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68704" target="_blank">📅 12:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68703">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLFTn9JBd3_WQ5uvbE7JkQ_7Kk9iwbNA5ZDqXZHQn-1WRRZRGr0VCBRONJ83Na5CAhjNeWBkF7du-lgEvGaGSdP_Rr8sDK2zdiwUb3It0vGxsbAabZKZaIvKKN7XCoV0egIpa-gWTQHGzw7eVy16APAwrvT-paDXAytCo_gJ6ucEr7g_DmuvGZ19_LqDf5Ik695INUFVTmpSmmxNqyyIwtkCBir48fpFokViur6klL6TbIVwWretc3fGvYbYW-s71jVDOnhapVA9glQegRUfGskT8H2GATLMLU4hlSZU3AAwinbHV_D0rv_Gw63rdWYAlO36v-ga3oihgBl0ByjyLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
در خصوص مناقشه با ایران، مقامات ارشد آمریکایی و اسرائیلی استدلال می‌کنند که تنها دو گزینه واقع‌بینانه پیش روی ترامپ وجود دارد:
پیگیری یک آتش‌بس ۱۰ روزه جدید با هدف بازگشایی تنگه هرمز
آغاز یک عملیات نظامی گسترده و جدید به همراه اسرائیل برای وادار کردن تهران به تسلیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68703" target="_blank">📅 11:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68702">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⁉️
مقایسه ایران و نروژ:
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68702" target="_blank">📅 11:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68701">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b4d07166.mp4?token=WC48M-fcG5EnTPnzanPJio4yISCh0ySq7ChBsnqMI6Mkw25a4-PlSYlrLbPmmQ_Ek4YSHcFYZ-d25Yrpv-n_BcuoP_yZywpB1Sgaxy4YZk0KRHvSAodlSiPT9vUnlGj14FTUhb1hLSYt5D1gS4MFX8tcQ5HsxyfkH6ZbTmuI5kMW2mpyXwKGdHmPzH6le5n4uF-T-tU11jZsR9-rwxTDrupRopcn43CVkixYUDuLGlKGfhqGT0erqmlP2liQlTwPeEL_8nXm9VJP6pLtuNPfGkagbzxcLtbEKQxK1gkiEV9lcG9A7FjUZFxOW_uUkwHLObS8jXZABYxzFXoy7sqHRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b4d07166.mp4?token=WC48M-fcG5EnTPnzanPJio4yISCh0ySq7ChBsnqMI6Mkw25a4-PlSYlrLbPmmQ_Ek4YSHcFYZ-d25Yrpv-n_BcuoP_yZywpB1Sgaxy4YZk0KRHvSAodlSiPT9vUnlGj14FTUhb1hLSYt5D1gS4MFX8tcQ5HsxyfkH6ZbTmuI5kMW2mpyXwKGdHmPzH6le5n4uF-T-tU11jZsR9-rwxTDrupRopcn43CVkixYUDuLGlKGfhqGT0erqmlP2liQlTwPeEL_8nXm9VJP6pLtuNPfGkagbzxcLtbEKQxK1gkiEV9lcG9A7FjUZFxOW_uUkwHLObS8jXZABYxzFXoy7sqHRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
اکرمی‌نیا، سخنگوی ارتش:
اگه پای آمریکا به بخشی از خاک کشور برسه، منطقِ جنگ اینه‌ که اون منطقه رو هم بزنیم و هدف قرار بدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68701" target="_blank">📅 10:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68700">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c2573b8c6.mp4?token=F9f3bkRtHY9-M9wcmzm9Dwx1mPW9rn3grqfDmtsZFHSvUQbPk5pEMJmgcwcVf_t63Q3x3xE_7ceZfpLYTr8vbM2_-yXg62kL_041K0VCjy7uFZZxa0LPrEjsabhm7aJsRMeuldxwM0X2409Qpjy3OI_N23hremFAlf4Q6vroJhaPQS_dGtT6o8aJGvr2Glcy920RoCJz-kz8vyhGHKwx8BJEKwLcyvxViIn_qGRKHVrxIWDF3GKhyBHAhxlOgpsXKvSMQyEGqQjDDHTxQ5DqkrIFQPv4ryvS0926DSYTd93jdcIfFtxvt51mpban3wjwFtOl3nShViabmd5txXjGHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c2573b8c6.mp4?token=F9f3bkRtHY9-M9wcmzm9Dwx1mPW9rn3grqfDmtsZFHSvUQbPk5pEMJmgcwcVf_t63Q3x3xE_7ceZfpLYTr8vbM2_-yXg62kL_041K0VCjy7uFZZxa0LPrEjsabhm7aJsRMeuldxwM0X2409Qpjy3OI_N23hremFAlf4Q6vroJhaPQS_dGtT6o8aJGvr2Glcy920RoCJz-kz8vyhGHKwx8BJEKwLcyvxViIn_qGRKHVrxIWDF3GKhyBHAhxlOgpsXKvSMQyEGqQjDDHTxQ5DqkrIFQPv4ryvS0926DSYTd93jdcIfFtxvt51mpban3wjwFtOl3nShViabmd5txXjGHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در سال ۲۰۰۵، نیروی دریایی آمریکا ناو هواپیمابر USS America را هفته‌ها زیر شدیدترین آزمایش‌های انفجاری قرار داد؛ انفجارهایی که حملات اژدر، مین دریایی و آسیب‌های واقعی میدان نبرد را شبیه‌سازی می‌کردند.
هدف یک چیز بود:
فهمیدن اینکه یک ناو هواپیمابر تا کجا مقاومت می‌کند، چگونه آسیب می‌بیند و در نهایت چگونه غرق می‌شود.
این ناو بعد از حدود 4هفته آزمایش با انفجار های کنترل‌شده و بررسی مقاومت سازه در14مه2005 عمدا در اقیانوس اطلس غرق شد.
نتایج این آزمایش بعدها در طراحی و افزایش مقاومت نسل جدید ناوهای هواپیمابر آمریکا به کار گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68700" target="_blank">📅 10:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68699">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9ecf589fd.mp4?token=pkTmx6-l46EMHaMGGJR0ltZxlhv8sw-XDywrf1W--sk0ofKxsKSSPc2zJ1EFWjXKtROBEgHVGxH-yxVIRzhIu3pqC6amlJIwiPtSK4HzHg2eWNu2bKzcdNDtGz3er1zjhTSjCcSoeafm1FnNNKhYz56xKDukDElICb7bHbNPbEUAlwG8Jgmzv8Woiza9i5Z_AxTnyBcOvF8Qz2aG64zFFvsu_4znBIy1ujXeU4PhaHoWNcz34XSdbPjsN1T4blE-EdLKUEPievytwORfvtjO4yAbt99jrYDnsVABZU-XsXahWXezJabSVXo-4G4X5k50pUWFKP6b-76KoKYssEH-OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9ecf589fd.mp4?token=pkTmx6-l46EMHaMGGJR0ltZxlhv8sw-XDywrf1W--sk0ofKxsKSSPc2zJ1EFWjXKtROBEgHVGxH-yxVIRzhIu3pqC6amlJIwiPtSK4HzHg2eWNu2bKzcdNDtGz3er1zjhTSjCcSoeafm1FnNNKhYz56xKDukDElICb7bHbNPbEUAlwG8Jgmzv8Woiza9i5Z_AxTnyBcOvF8Qz2aG64zFFvsu_4znBIy1ujXeU4PhaHoWNcz34XSdbPjsN1T4blE-EdLKUEPievytwORfvtjO4yAbt99jrYDnsVABZU-XsXahWXezJabSVXo-4G4X5k50pUWFKP6b-76KoKYssEH-OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
موگویی:
تونل رفتی؟یه تونل تهِ پیروزیه ، اون یکی هم بالای دربنده ، فرمانده‌ها توی این دوتا تونل زیاد میرن میان!
🇮🇷
عراقچی :
حالا
کونده‌‌خان
انقدر دقیق نگو شاید دوباره جنگ شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68699" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68698">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68698" target="_blank">📅 04:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68697">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDVZYJSCXhx_TurpcKGECzkU58Ykiyn6vtdC1HWytFsL47kPAuXK1HQ82ccEdUKayPB0TfH8277bneEz_um1PSAT7QhSvU_CFFDo7Aav3C1DWH2bhXe4MTVRS-GJyr_-IsgJBsQjMGhHmlMore16h0szB7AmjQWvT1jnnY8oek_HixzLNwCvQ5mCa3G4_Yw8dLFYb3jFBhZcl8MoJI_NzgR4TwyVy_D3MXDSiGyMoFq-7_XWdRRvHNIi0XpWHMPU6l2TGRM4pOt9FdYemIYWhRFqu5QMcvs4Z3unbvA1KqKm0aqzqfBpP3uWX8GUSBZk5BFKAWWLGfFOn4_eoKdAFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68697" target="_blank">📅 04:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68696">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j87-faYY3FPVrbVSr2waVTsM6_mkijt3ORuhpu9l3DtSi0ZK6j2uCPWEwYSggIce15vdU53pvpzTdRUOA6n21SQVoUqsN0RPcBVhSXxWpW92D5a4DGJVyQwJTLWWTOloXIN0VyKNciTR-67HP48ZOwlvYnifNvaz_JCYdGPMRypOTJCHZEJm2g8wM4dnXHh9LJU0ylUS8aKbd-gtiMREt2EIn1smkNp5vwqCcaAt6YGmgADDb_Gk4wMmMWXZew5FeocXM3Db3H7I-HK3yFJ__sasWcBKKa4_OH1UijkPZONyAlmpvAKJCZR6aXzITfBl1MhBhkeKV2501W9YJsV8zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68696" target="_blank">📅 02:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68694">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcfX5MLRxKkGI1d1rf5h3WMobzXfTOWe5pifZXR5poAsLSigFtLQgikNeI2ZzxppjscgDwcG9LhsYg-6PjLtgAK4HsmhETFQIL1_APmBrCAR_8-Nkl82uHdI8JdQimxNKORgwjUAOCV8HC2FtnKjEpZra5LGk4FOUm6EcT-yF4mi4R3JgHRKWe4_AMHgi3jOpORXGR25UZEBKxEcaMS7HgYdExKlXNHFJXH-nsa0R61hAu94yCGK2v6q2J7HrJiTWpejUKlMmiypr2HX0v8APiMjK3idlnApL8NE0S11VFs4iRIfFCKS6CRz8NWELAbJ1cy5PIcul8U5udaS-RpQGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ:
"من گفتگوی بسیار خوبی با نخست وزیر جدید بریتانیا، اندی برنهام، داشتم.
ما در مورد موضوعات زیادی از جمله روابط برجسته‌ای که با بریتانیا داشته‌ایم، بحث کردیم.
ما در آینده‌ای نه چندان دور برای موضوعات مورد علاقه مشترک دیدار خواهیم کرد.
نخست وزیر کار بزرگی پیش رو دارد، اما او قادر به انجام آن خواهد بود و البته ایالات متحده آمریکا برای کمک آنجا خواهد بود!
ما در مورد نفت دریای شمال، تجارت، ائتلاف نظامی، مین‌زدایی تنگه هرمز و بسیاری از موضوعات دیگر صحبت کردیم.
تماس تلفنی جالب بود و خیلی خوب پیش رفت. من برای نخست وزیر برنهام آرزوی موفقیت و پیروزی دارم! رئیس جمهور دونالد جی. ترامپ"
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68694" target="_blank">📅 01:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68693">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
پایگاه هوایی بندرعباس رو زدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68693" target="_blank">📅 01:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68692">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
دو انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68692" target="_blank">📅 01:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68691">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5RXuHo2sBzGR09FE4YLWRm1As6T_yNk_s0wVBGlPvHNLKjKD_T6hhc7VRjHnBl_A1i56QA0abdzkGlVrz4EaH24LF8fyquuR3pqs9JQ29qfP__stLVfEqUUy4XEoRP2mDBZrrAKVtUxMmu_BiKKQL7jpfAm2djhN1Hs4QJLODeTiRqIX7IaHyrHeLhZhXgD2RGXDtpzEhm0RZhi7ouj_bYbqzrkoPeMsS4mIwJUofflphjC_tbh22VJ5wxH2KHIr5srQ0rxFWlfXzo8B4v2IQHLU3RGB9fIjDSUL8LcYYqTTpd4povzYG31xMxdsecV5hs82JqvROvhfqFkUkMWkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سازمان تجارت دریایی بریتانیا (UKMTO):
یک حادثه در ۸ مایل دریایی شمال شرق LIMAH، عمان گزارش شده است. UKMTO گزارش‌های متعددی دریافت کرده است مبنی بر اینکه یک نفتکش از طریق کانال ۱۶ رادیویی VHF اعلام کرده که مورد اصابت یک شیء ناشناس قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68691" target="_blank">📅 01:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68690">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
مجدد انفجار در بندرلنگه
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68690" target="_blank">📅 01:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68686">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MeFE6ZOs68ECuYr2XK4IhxzXQ2TWCYpnIyHVA_c1DE3ex6_3f1gJWkXbauewc6SFogYVqABWcBPs2IF7kb_F4zSh9SukrQtz06P5LbzACrqxgqYwdr8AsXkdUTbgBhys7trbQDfloFweosWEKhDR41-UmkRWJLBtjryDxLPdJvaoYcVSH_sNEzKTSvnMoqBBcYZpCUSMGrDfjxKIa95wXpQ5EldK8BZfGNe1nrBnWoRwYPZ8AoZwUlyJMbdEtD-HsaXNRxFqr7bOsQ_q-IKtx0o52i5BgjniKJQtxcdbKq5mShI9xc1L_6fQdNdvAtF_tD2ITNYvTum687nPzstysw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UmPLott4P5QNrJQafONDALqqxtwXGOJ1Kqb8X7yN_6JIVm2G2dN1XkztNnk6HcyShIaZ7d0e3mR7hTYtJcbOQKiQF-ax405sePbPlNfnlvDUJ5IVN3QAYoNwKBDJhthuJ1H7Vk9MpK3iWa7hKZ44RbP7IELsWIPUQnjFsCQuip_kmTJcSIccFYzvcA8PTyhXurPn2XfbXj-ItLp2MrtQt2Ma5hckCSgBfG9JIUilquZTrFcjlLYFgIVhBc64IJNb1hmfpc0wIYtxeaiJNHXKTOC3XM9gjhNGLly6ktJkHzUgE5o5dz4yzbRlQ7oJNf7lNk2chkP-uzQS-PPWovW_-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Rfl89zWuTTEIpZQnMnStBGm4imPmllCgrsb91X42wGeN4_fjwXCNe5VlMviWHGt2WfOcfnZolsXPMCOzIwGUWZ2q96AxMlT3TMgMgIqF_eRkmknIjGairekQ7FoQSZqN0YBH3jjYmdQ8zaW60P-oyQ0g9f0u70Njn5SCJLLj9PEZohCPq71ZLSWCPKv6q7yIhbJU1TXMH-I2G5z4MCxzXSPt90goZtmgn3ugQG-z8uw4dpIjAkwamHpqWEFF6S0P010C7Ue82_Cu4XnyUb0M9NWWk-AdT94eZgPajXFiGBYci0tFdH-L0vCrNO-W8TM7-Y-dFg0rg1BPSSCYKQnRZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FKYDwunQs0mD3WCJBahu2Xe-j2-kPaMLspjK1seJaOLP848qKzS1QlgkLT8VGWyB8jlfUOQ61XDONnmc-9WqFTUHIpLYqFk21VQ_n-WMioapJyvx3hZdbgfrHtf6ChY142wQ1P5HuAdgKe76nBN_Gl4R37Mdh9tGIwMpCriHGyeZ8J8giNvBxggGYLRWEFQrwf0q0DQQVD6yx0_pG1MIRGpweZkxGWEBKu0SG7fyMOFMNTaTLFftlUCPIOrGADkT8JoMfqUuExhdWs7_e1ZmE1LNJGi9GKnJo8PNGed6m1Bt6jxGjIvElOwNOS-AC6hXf-76Up4Z91BurPYSRkPkJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کوه دراک شیراز زدن
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68686" target="_blank">📅 01:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68685">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6bdf4b6292.mp4?token=ebQ60m5XUXIJ6CijY7kpjB6_EzGQw84hyVNlgISZEsTF8h5ZKKfyq3w52rVTNTNwkTt9wc6JeAtXc3KUvrVce723cLXVHF9tbuzAhvFmb4j7GfeHBvrzWdo5h6CF7rk-YwlwQsfyn0s89hLfgjpM7Q5_9ROYCrbbqxsWq-0I6IT227YGkaLGj58dwgAOMF6QMLIky0AS8tdVZFwbwAHVuZIZLJfQN_IS_fcEQ7FdGZ0dkYBbEbNFMJd4_gJUIQggOOZBPN7H8xpHkzgubZSw4dxdfw4kofk6eEGrqFaYPMDxzWA-HjJB3j_am81ys56Te28QO3gkPqTqkyRT4lbHzw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6bdf4b6292.mp4?token=ebQ60m5XUXIJ6CijY7kpjB6_EzGQw84hyVNlgISZEsTF8h5ZKKfyq3w52rVTNTNwkTt9wc6JeAtXc3KUvrVce723cLXVHF9tbuzAhvFmb4j7GfeHBvrzWdo5h6CF7rk-YwlwQsfyn0s89hLfgjpM7Q5_9ROYCrbbqxsWq-0I6IT227YGkaLGj58dwgAOMF6QMLIky0AS8tdVZFwbwAHVuZIZLJfQN_IS_fcEQ7FdGZ0dkYBbEbNFMJd4_gJUIQggOOZBPN7H8xpHkzgubZSw4dxdfw4kofk6eEGrqFaYPMDxzWA-HjJB3j_am81ys56Te28QO3gkPqTqkyRT4lbHzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فعالیت پدافند در کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68685" target="_blank">📅 00:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68684">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o55KoMVr8UcWuYLp_KYm4KuXEr45iEYGkyYhLTUhkLdeb1uNEXzq3zAgmGKoFC2dnrFIdULKSZd7LBUI64hF1vp-yAOvKsB7PqoLiPOCzJxbLj7qy8odVBsDJ9m2GjToogIsCWJIPdziSsBrTx-ZpIEYsY36hvrlzoFqRFMkUpjgj8m0tCvdCUimHjnArkRanbscEIxEApVmCXlyF1vcr3ZbE5DQw1uwuQHmC_E8p3G3FXqmATu6unG5p37tBWx0DEnIBdx1xfpFTtfbZ2L8OQpcMsupc1JambPlBKfU6uONLt90VzhnUCaCDvsLPv90eTlfl5PyjEibYh0dCQGB5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژیر ها در کویت به صدا درآمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68684" target="_blank">📅 00:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68683">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6040eb52.mp4?token=sp6xWj1r_fzFYnN41bapJGblA58QTcQJjPaA3iNfnRSLspzSzyKfu4wzun4hYb-C-UTHx7tX3WfMRMnoGINs_LZ-bongL-lBH1h_9Urx8YdzQUqs8cHdozQ6klYOiGmMAs5QU9Vm-V-OrdLw1a_25Q9tyfjbtE73royjxaB2c-29RjwrcF3IVukjLdWDXyp-oM50dXENfJ64RySS31MBZuWuAjB4KMFfDZx7x5_jKiPg0IAcLjDgLA8Mf0ytu9CXNND6oT0-TNZvLPJ0MfgGCDgG2KNqZRkx1h9x_tsugEtesv5fLhzX6wHiBalL7hF4XGj6r28rLeaIsq5Dwd2rZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6040eb52.mp4?token=sp6xWj1r_fzFYnN41bapJGblA58QTcQJjPaA3iNfnRSLspzSzyKfu4wzun4hYb-C-UTHx7tX3WfMRMnoGINs_LZ-bongL-lBH1h_9Urx8YdzQUqs8cHdozQ6klYOiGmMAs5QU9Vm-V-OrdLw1a_25Q9tyfjbtE73royjxaB2c-29RjwrcF3IVukjLdWDXyp-oM50dXENfJ64RySS31MBZuWuAjB4KMFfDZx7x5_jKiPg0IAcLjDgLA8Mf0ytu9CXNND6oT0-TNZvLPJ0MfgGCDgG2KNqZRkx1h9x_tsugEtesv5fLhzX6wHiBalL7hF4XGj6r28rLeaIsq5Dwd2rZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68683" target="_blank">📅 00:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68682">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
مجدد بندرعباس و بندرلنگه انفجار رخ داد
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68682" target="_blank">📅 00:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68681">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
انفجار در اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68681" target="_blank">📅 00:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68680">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
انفجار شدید در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68680" target="_blank">📅 00:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68678">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d45723674d.mp4?token=mcKUp0vZ8zV0BVVCVjEJdkPLgg74lfbkzIOYQevncDu06YhqajYlXCObQfTN0Ugzf48fYd6C9przUYvlD9mCTpVISqC5tqcQqTVVQUluVll0Xax9_3_ACcyPiT7GMiN2QawbRENZvAxYI5rtenKjrBNjBadtlkDtLBJJt2DM_-26XctdViiNMDd_Mf5aqv5l0nBwOBpOTZqKqVyhuVZi9vvd1cMOQrqLdXRoZWv-2NooEuKZaeIy2Y7Z_S3zflt99m1eaAavQTxnAfftz6ly8qFtOuNON4CSUzX2Yyn5VcdLulIFenY-87ePwVXhYM5lPB7VSmnzYGy8cR3vBugpLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d45723674d.mp4?token=mcKUp0vZ8zV0BVVCVjEJdkPLgg74lfbkzIOYQevncDu06YhqajYlXCObQfTN0Ugzf48fYd6C9przUYvlD9mCTpVISqC5tqcQqTVVQUluVll0Xax9_3_ACcyPiT7GMiN2QawbRENZvAxYI5rtenKjrBNjBadtlkDtLBJJt2DM_-26XctdViiNMDd_Mf5aqv5l0nBwOBpOTZqKqVyhuVZi9vvd1cMOQrqLdXRoZWv-2NooEuKZaeIy2Y7Z_S3zflt99m1eaAavQTxnAfftz6ly8qFtOuNON4CSUzX2Yyn5VcdLulIFenY-87ePwVXhYM5lPB7VSmnzYGy8cR3vBugpLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
منتسب به چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68678" target="_blank">📅 00:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68677">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
ایرنا:
در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68677" target="_blank">📅 00:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68676">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">امشب دهمین شب حملات به جنوبه، اگه این حملات یکسال طول بکشه، هیچ مسئولی حتی آخ هم نمی‌گه، چون اینا با حرومزاده هاشون راحت تو پنت‌هاوس‌شون دراز کشیدن و می‌دونن کشته نمی‌شن، پس تهش میان می‌گن چند تا #پرتابه بوده، دوای درد اینا همون مردیه که الان تو اورشلیم نشسته،…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68676" target="_blank">📅 00:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68675">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
انفجار در بخش بمانی سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68675" target="_blank">📅 00:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68674">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
سنت‌کام:  دور جدیدی از حملات به ایران آغاز شد.  @News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68674" target="_blank">📅 00:14 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
