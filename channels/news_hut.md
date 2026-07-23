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
<img src="https://cdn4.telesco.pe/file/AKt9Hvo8xGK6wy-8PY0z4DYAr7AuOietYKPee0Aq3adwUfx2SvnK_Ga9pn94wE2I-iNvAXWnKNIcWXrTiwHUafeRSbt8e11Xtf7AMOdULoKGLXMmu7IPTHyBwCkNvYDHB8T0ttuUGxOrGvCxHR9B_Uptim6a_DUSvZjz9sL0VDm5QbznyvdXpFc2MLslpamI2t1X6BzZiVS1t9FJuuJBZ3DrGGggDQziwf4uyLosCLZefObMC7x1NA2dtFUM6r8BJ6ishbBX1mFw0mHDA0wwU-5Ziy3Stvh-y1D0_DrwsCjRm_yvfq633S_dF91Utyd4gBUck2fqxZn4I-v8LiWB3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 151K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 22:30:52</div>
<hr>

<div class="tg-post" id="msg-68879">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇸
ترامپ:
کیرم
تو هرچی کمونیسته
#hjAly‌</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/news_hut/68879" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68878">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند  @News_Hut</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/news_hut/68878" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68877">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند
@News_Hut</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/news_hut/68877" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68876">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">همین الانم ترامپ داره حرف می‌زنه
#hjAly‌</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/news_hut/68876" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68875">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اگه امروز این قطعنامه رای میاورد، ترامپ مجبور بود جنگ رو تموم کنه، یا اینکه قطعنامه رو وتو کنه! #hjAly‌</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/news_hut/68875" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68874">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.  اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/news_hut/68874" target="_blank">📅 22:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68873">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/351349ff2d.mp4?token=bVeuFHRtTLZmm51j1J3vOcRisMne5y6zXrT4XVH4fBqFUdDmWSqgBK1rLYXsya2Q_MYp87PszTwB4W3qogCgu3EIfAK0kzt100yzKOVMgx_oblVS5cXZ-ZKADgDXxt-40rvXtIneSTi4TbQYjFZUuAUH_Mqb5RuWZev7Zsrr8qmndTnmkRQBAflPCPxbCiIKibUX_fttmQB6d1zcbYyMFj6SZtUBijtCY_gb4RPySUUtDzR-Na8J-l9Aj-gej1uUJCAztwQo6EaZZh5v8T0cQb8235YMRZTZh4Ju051GmPJ6Ow0-9clO6YZeU6NAt3cCLnNwDzqslZAQbES9SO4TXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/351349ff2d.mp4?token=bVeuFHRtTLZmm51j1J3vOcRisMne5y6zXrT4XVH4fBqFUdDmWSqgBK1rLYXsya2Q_MYp87PszTwB4W3qogCgu3EIfAK0kzt100yzKOVMgx_oblVS5cXZ-ZKADgDXxt-40rvXtIneSTi4TbQYjFZUuAUH_Mqb5RuWZev7Zsrr8qmndTnmkRQBAflPCPxbCiIKibUX_fttmQB6d1zcbYyMFj6SZtUBijtCY_gb4RPySUUtDzR-Na8J-l9Aj-gej1uUJCAztwQo6EaZZh5v8T0cQb8235YMRZTZh4Ju051GmPJ6Ow0-9clO6YZeU6NAt3cCLnNwDzqslZAQbES9SO4TXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.
اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول از کنگره مجوز می‌گرفت. اما با رد شدنش، چنین محدودیتی اعمال نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/news_hut/68873" target="_blank">📅 22:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68871">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ga9B-y3Ysl2uStvGaxj69vK20jAgVz_z_m8OEj2atBbjUU-FHbwFFwUl5Ip1BRV5P326n8OzBjsQ_BSv8QdNUL4iYnG54pHU6twcwl6sMAvPLD65f2WCrNpRfQKRsBW-73HrnMhzfDbgx3j1xJLv6sA88f4QDj9dywM5JQdMR6wsEDA4UlFDH0dMj1s15qlIfNViPgkxasHC9feztmvRNKJhGschAPmuE4fncEo3T7dOCIFicnpUeD2DgQN-ZlbzJovUFytboM2n5XAsP0SacG_cSh6LTyVAq6a7OaZgbFi3X38cctfkgu398EnEmmbmgIf09UvnTNQHg0-Szx3t9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca0071632.mp4?token=AKxxcx0VuHqjrfh8L_n995W_WiGViIcawK9ICUyIjY4etsu-EHngmTbgBhicqq1HK-l9xor3vlqsczkSf-9K81xZZTISNgzvj6v3KnLPhM2xZhPf9kfEkGFQ7EsGyHoSGDzeY43DcaEJ-ZIVIMt90Fifr72SBqKrlU321z2HrcPK7OPNoGLDk5uTsBUjLE_7T3Po8Wwtzj1cUaRfn0wkgjazXBV0mgBMFr44WyJmqJf7--WA_GdAnyqMozrP6RrtGmc9PEoqTL34jnwRUkHdmwgKrnuvR2L9Tzybk2x8JGwGxgimOOzuRyeKQwpWV1JUF51wMll53hF43E0oY4wVrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca0071632.mp4?token=AKxxcx0VuHqjrfh8L_n995W_WiGViIcawK9ICUyIjY4etsu-EHngmTbgBhicqq1HK-l9xor3vlqsczkSf-9K81xZZTISNgzvj6v3KnLPhM2xZhPf9kfEkGFQ7EsGyHoSGDzeY43DcaEJ-ZIVIMt90Fifr72SBqKrlU321z2HrcPK7OPNoGLDk5uTsBUjLE_7T3Po8Wwtzj1cUaRfn0wkgjazXBV0mgBMFr44WyJmqJf7--WA_GdAnyqMozrP6RrtGmc9PEoqTL34jnwRUkHdmwgKrnuvR2L9Tzybk2x8JGwGxgimOOzuRyeKQwpWV1JUF51wMll53hF43E0oY4wVrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ساعاتی قبل سپاه پاسداران یک نیروگاه برق در کویت را هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/68871" target="_blank">📅 21:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68870">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=HT4MN5d3JUviflvvyy5Qsyh_54bO_zQn-arFelitsUhpyXxpI80L0bvIqs0s8RPbXhQ_FB5YCuMULc2HjnNXBzpiqDgCEkfArzBwlFmM6bLeM8LJx9SCJpV6SRbFTyd3dlJyajxSbTxLsEQ_g8NL70KJzFOGmlcLR_TTQ__qSl_ah-N2llTyG4AVqKejRki_I63AkZDfdJjO7PAfcnn05h127ijmCAaLBaNGOcSFKmG2VxheSNP26mJptPCRWfMNkgacj1PDNyS3Ho6P9-vtB_l-yecLPWL5n-kyUMZ7Qh-rtsYvhK4uM6WHTPEUZj4WH86XL1o340IrnMG7TPrGjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=HT4MN5d3JUviflvvyy5Qsyh_54bO_zQn-arFelitsUhpyXxpI80L0bvIqs0s8RPbXhQ_FB5YCuMULc2HjnNXBzpiqDgCEkfArzBwlFmM6bLeM8LJx9SCJpV6SRbFTyd3dlJyajxSbTxLsEQ_g8NL70KJzFOGmlcLR_TTQ__qSl_ah-N2llTyG4AVqKejRki_I63AkZDfdJjO7PAfcnn05h127ijmCAaLBaNGOcSFKmG2VxheSNP26mJptPCRWfMNkgacj1PDNyS3Ho6P9-vtB_l-yecLPWL5n-kyUMZ7Qh-rtsYvhK4uM6WHTPEUZj4WH86XL1o340IrnMG7TPrGjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب یه دلقکی اینجوری پشت ترامپ اداشو درمیاورد که حسابی وایرال شده
😂
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/68870" target="_blank">📅 20:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68869">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=dqurP8zUe8W2PlykkBVJo-5YbTKNpB4S4Y3lUKlqYscjC_r71jrpBO4zbtj5G5-50sBkBkx-gtVg9isFd9WZjYl4R_tgr2RX9k2qoqSZ0yIw0o3T8UXkCBDwaVypNh4DWl8V65uXIV0j12MoKZ3ah9pYeB8HhM2EUKeM_kh-8F_VVA2AGpm3Tg3IBpk4LAiGHnbhcrcMIz9A-F7vjaepiyiA6E8xcjVg_Q4XF1duP9lIy55MuhUjKLV7e0AsaViDQLJoreY4TSHctB6BdYCKN13eJGk6fWVwUq5O2GwprJI4QTZGsOUWQ-as-5YR86cxRnolin1WIozQu2lUVhl0nI93fVNQTPnd1kse0d-Aq_cW9vsvEQ3-_NrgNXMCrH7cKyOUe2XhZBGGmcHpM9pkRP1zCSzXzuxxqC2WOourAUWKbNXwYfQA7y0vC4W1tiLZNUhCzwb2Zrv1Ziu8iQojWSnX3J6wGwcYz7vUJ-lvWaJ6WxxLTsCA1G4XXlA7uGwwsBlGeG9WO6YCZ8a3j1GHz7P5QdLAHvQwXgiHt4Wkxam4paBkoozp5cfZYcMDZQHIqZuDbQyINKIyQcLRS8HVYnS9mYsH-pcGFjHdH6hmE0zdeeGPRlQXANGoMgA34H7WBVfINz0N64ON_iIfXsGt7Um0KAzaYycdq5SQQ0Pq4-E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=dqurP8zUe8W2PlykkBVJo-5YbTKNpB4S4Y3lUKlqYscjC_r71jrpBO4zbtj5G5-50sBkBkx-gtVg9isFd9WZjYl4R_tgr2RX9k2qoqSZ0yIw0o3T8UXkCBDwaVypNh4DWl8V65uXIV0j12MoKZ3ah9pYeB8HhM2EUKeM_kh-8F_VVA2AGpm3Tg3IBpk4LAiGHnbhcrcMIz9A-F7vjaepiyiA6E8xcjVg_Q4XF1duP9lIy55MuhUjKLV7e0AsaViDQLJoreY4TSHctB6BdYCKN13eJGk6fWVwUq5O2GwprJI4QTZGsOUWQ-as-5YR86cxRnolin1WIozQu2lUVhl0nI93fVNQTPnd1kse0d-Aq_cW9vsvEQ3-_NrgNXMCrH7cKyOUe2XhZBGGmcHpM9pkRP1zCSzXzuxxqC2WOourAUWKbNXwYfQA7y0vC4W1tiLZNUhCzwb2Zrv1Ziu8iQojWSnX3J6wGwcYz7vUJ-lvWaJ6WxxLTsCA1G4XXlA7uGwwsBlGeG9WO6YCZ8a3j1GHz7P5QdLAHvQwXgiHt4Wkxam4paBkoozp5cfZYcMDZQHIqZuDbQyINKIyQcLRS8HVYnS9mYsH-pcGFjHdH6hmE0zdeeGPRlQXANGoMgA34H7WBVfINz0N64ON_iIfXsGt7Um0KAzaYycdq5SQQ0Pq4-E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فاکس‌نیوز در حال بررسی فهرستی از اهداف زیرساختی احتمالی در ایران است که ممکن است مورد حمله ایالات متحده قرار گیرند؛ اینکه کدام نیروگاه‌ها ممکن است هدف قرار داده شوند؟
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/68869" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68868">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nu5kROcIziO2wlKuJs3uw8R3gNNToPC03cvtCe2wrOyoQUZvmm0zGYaXhLCJhf0QsnXNePV_TntYRDwnQ6wIo7zS4zk_xXXwAZySgC_qh7mqw1-sap-NZ0GPajzEJpF4QajOE-p9iXz_pOcRQsWbvUXBBQstY5cERMcZPfbIAk_0YI0Kjp4bXr3GZwlLFzJfyRN4xNx8gtbkggSWASDMOAdpHpDuf3QuT5__Uv106NE31XUYwSXlZb8G04neGAbFkvdEBn-CmJ4llD2uh54YuCi3FQGEQctiK6MyE0zUaC8gnGmJHvYrDEOWblyyQqxXGQdbUwF6yv0V0TbWf85c8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/68868" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68867">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9qbkJ41vI9Lxca8GUDi6Ot3MdZ9e7z4yw-sU5rR9tmMDpSNt2MPQGU276-mL5Jws0YXngle3HKr8HCgTlCln5QUy1pbbZYbP_9Oh6Myknor_o5rTu4EEqPyHxhA35MTzoHQXvD0fCGOGSWdZUmM9rV7vsdOT_mHZ4bqIXm8XnZtYYbP-esngrTFJWLTaCcGjQ0lEbkpbiwaZHBcGRQQZA2dN-3IyUa4jikzT12Ctyy-KAl7CAKl6WUCPxw07g6ed8ub3q4Nu450BFS9Q2_q80AsPsS5hIS057gT1YoUiGTUdddHwPpfy4z3s4-VnWU_RVLkd9AYqJ0GbYkgMim61Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
آنها می‌خواستند ایران را تنبیه کنند. در عوض، خودشان را با نفت سه رقمی تنبیه کردند.
استراتژی ۱۰/۱۰
👏
👏
👏
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/68867" target="_blank">📅 19:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68866">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=q7ewz2-vBLsxv_LTSEg8bk7yUhvL3A-QnSRKbiTC1MjFeHgQOOoClloOxLydg4DTkF9ipaP_a9crpDMJc9tV2AKQ524ALxh6IE89CoSs9adoifF_Z5u7CnKgzjiu4hwApKFAmUO7bNkJmh5zhHJgp2Xb83SNzj8xPBldR8nu6HlXpC54pJIIOV61MUuUwPaPQe0lt65AC9jWX5_KM61zYTQZE58yrWjhWgaRrmXNEDQaSr6tUXeZRAIJhUhhrrcKn0D-Uk6x66teplP4VjHem0Wh__XbhcU5SG-0gAOdGxOQqdihby3tBfzTHYp7WtwLm6JZCm2hsrBGNtOucmX8-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=q7ewz2-vBLsxv_LTSEg8bk7yUhvL3A-QnSRKbiTC1MjFeHgQOOoClloOxLydg4DTkF9ipaP_a9crpDMJc9tV2AKQ524ALxh6IE89CoSs9adoifF_Z5u7CnKgzjiu4hwApKFAmUO7bNkJmh5zhHJgp2Xb83SNzj8xPBldR8nu6HlXpC54pJIIOV61MUuUwPaPQe0lt65AC9jWX5_KM61zYTQZE58yrWjhWgaRrmXNEDQaSr6tUXeZRAIJhUhhrrcKn0D-Uk6x66teplP4VjHem0Wh__XbhcU5SG-0gAOdGxOQqdihby3tBfzTHYp7WtwLm6JZCm2hsrBGNtOucmX8-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العدید هم که تخلیه شده، بنظرم خودمون رو آماده کنیم... #hjAly‌</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/68866" target="_blank">📅 19:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68865">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZLzcJbyylgGGwmMSztt3AUs_l_gjMCORB9BgSwr7ut-jhGXGL35u0Lsk20GW_gutDBPkxTh5VRROTTXrA-kcFCDeBjT01GwXBzBQpfmi_dAlx9aX5hHbuBx5z2scPcQH-1HQafcdiKBi3tpzBkVfr_ZJDuuxmbH46VHGuEjKbZaxRl9WzAaZCBgLThNWmF5WFtlop-aI1rnCkDFYBs1AWOfdT4gbItp9sFnkp2waNKnpBZSRIZxa9RLlgmRgxK4Eky054dx0R3u9cmbqs1XSGws8MJpHXBDUzOlTza6POxbSlcnYehMaiRA760BSE_M5TqQaYg6l0Cg8Rfz_lJ0TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین نشونه های نزدیک بودن حمله، تخلیه پایگاه هاست</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/68865" target="_blank">📅 19:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68864">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ همچنین گفت:  همه چیز برای این حمله آماده است. اگر از اسرائیل بخواهم ظرف دو دقیقه به ما ملحق میشود اما ما به هیچکس نیاز نداریم.  @News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/68864" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68863">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری؛پرزیدنت ترامپ به کانال 12 اسرائیل:   من در حال بررسی یک حمله گسترده هستم - بزرگتر از هر چیزی که قبلاً اتفاق افتاده است. من به تصمیم گیری نزدیک هستم.   @News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/68863" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68862">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBidrgKf0EN04vUFuPuk8uMFbPipG9M5ckqSyl1Kpk8gPVtSs5rAmALma2rAHBi3reLomx9SpVxaxeftulYq9DuLfhSL7Lxi-r8b1VIvgUemq0N7GQMp3B7FQlRF1zPdAaNKgwOytKpXL1Of-6AyKDxuo5jJlWloQ9L1BN-__tuARbWP82wUrsRJYij36ePJ-fNvFkjOYiI9DMniLPGc5JP8QrPIb8Xt5wwqKdFaQizxlAy_sOxxuxgEHEcyLVK4wSkONgLY-ylgReKmQPoNCgkvDk7DzRhUFGZw8ptPYSQB7oyNs31Z3EwTIAIC0qpvuSno6ed7b936pZERnDqxpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری
؛پرزیدنت ترامپ به کانال 12 اسرائیل:
من در حال بررسی یک حمله گسترده هستم - بزرگتر از هر چیزی که قبلاً اتفاق افتاده است. من به تصمیم گیری نزدیک هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/68862" target="_blank">📅 19:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68861">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a86f5d96ba.mp4?token=uK8tIyFB9yX0ub0utXPunW3oS1fJ4cPdtBcRPkj815LfQtPXDekXhwzT1zRDxjEiZNJRnoSeB1iXNSH1TBFs73KnTQWVsRuPh9tfcfBBIr0-ONrimzQaC3AsF5d1vsfdMBKXBaqdHqQ69q7mq3lwPCpjfT1OFxZzuFFIxtsnM2qMUO1xldYtUlXWVvuNqntFKMtXIYyTHgfL7jYs_ZPU1NPiaGu0FWoQVDUBrKLASCbkU9Ar-Tzq9099aduTBRIyu9fMqAivSb0Gc4IGhHEjSaoPro_JieLxMcv3OFEZ7ptIwfgPmLqBEewbQBSW5zGp8bROaePskOmv6b_ijfPi2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a86f5d96ba.mp4?token=uK8tIyFB9yX0ub0utXPunW3oS1fJ4cPdtBcRPkj815LfQtPXDekXhwzT1zRDxjEiZNJRnoSeB1iXNSH1TBFs73KnTQWVsRuPh9tfcfBBIr0-ONrimzQaC3AsF5d1vsfdMBKXBaqdHqQ69q7mq3lwPCpjfT1OFxZzuFFIxtsnM2qMUO1xldYtUlXWVvuNqntFKMtXIYyTHgfL7jYs_ZPU1NPiaGu0FWoQVDUBrKLASCbkU9Ar-Tzq9099aduTBRIyu9fMqAivSb0Gc4IGhHEjSaoPro_JieLxMcv3OFEZ7ptIwfgPmLqBEewbQBSW5zGp8bROaePskOmv6b_ijfPi2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
من بلافاصله پس از انتخابات به دیدار ترامپ رفتم و با هفت اسلاید بزرگ به آنجا رفتم.
اسلاید اول، اسلاید دوم، اسلاید سوم، اسلاید چهارم. "این کاری است که ما انجام خواهیم داد."
نه اینکه بپرسیم "آیا به ما اجازه می‌دهید یا نه؟" بلکه من به او گفتم: "این کاری است که ما انجام خواهیم داد." و ما به اسلاید آخر رسیدیم و من گفتم: "این پیشنهادی است که به شما ارائه می‌دهم."
شما بمب‌افکن‌های B-2 دارید – این بمب‌افکن‌های بسیار بزرگ. یک مکان به نام فوردو وجود دارد. اگر لازم باشد، ما خودمان نیز علیه آن اقدام خواهیم کرد. اما بسیار موثرتر است اگر شما بیایید و به سادگی بمب‌های سنگین خود را آنجا بیندازید.
او گوش داد و در نهایت موافقت کرد. من بسیار خوشحال بودم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68861" target="_blank">📅 18:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68860">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3008b12665.mp4?token=AL0J-FZodkbMRi8I7ffRidj39CNsxB8RMGcHeIdWLa-cVasc2JVRMEYOwdz6VTwIV5SrzP2KNiZ6BJx0EEgBHZsWHo5L1u4JKricvy8Pv8j-0rmD73BJFhbpp_90D5gpUZiaAntLFL506kIzNLA6xCP-d-4AL8Fql7LFgNCo35fpJcWrWab_NYjWDIAwg72sIIbJ6zd8KHng4133Ka8PoIiDxOZGKHMxVdEQoBowNGNSQ3cIKW6JK_bWQJP4XkdRoHsIulKxj4vzOG6OOBWRxP1bsl-PY9xXiEYKnGsZkSQbKuUxxvCq9RxFk_3V7rxV1Zw_Q8_gKhG2p7QdjEkPnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3008b12665.mp4?token=AL0J-FZodkbMRi8I7ffRidj39CNsxB8RMGcHeIdWLa-cVasc2JVRMEYOwdz6VTwIV5SrzP2KNiZ6BJx0EEgBHZsWHo5L1u4JKricvy8Pv8j-0rmD73BJFhbpp_90D5gpUZiaAntLFL506kIzNLA6xCP-d-4AL8Fql7LFgNCo35fpJcWrWab_NYjWDIAwg72sIIbJ6zd8KHng4133Ka8PoIiDxOZGKHMxVdEQoBowNGNSQ3cIKW6JK_bWQJP4XkdRoHsIulKxj4vzOG6OOBWRxP1bsl-PY9xXiEYKnGsZkSQbKuUxxvCq9RxFk_3V7rxV1Zw_Q8_gKhG2p7QdjEkPnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری:
الان تو دنیا کدوم کشور با ما دوسته کدومشون دوسته بجز مردمشون؟
⏺
ثابتی:
اونام دولت هاشون مثل حسن روحانی تفکراتشون امریکاییه
⏺
شهریاری:
توهین نکن حسن روحانی امریکایی نیست بعدم تو در حدی نیستی بخواد بخاطر این حرفت ازت شکایت کنه اگه تفکرات روحانی رو امریکایی میدونی یعنی تفکرات 80 درصد مردم امریکاییه..
⏺
ثابتی:
کی گفته؟
⏺
شهریاری:
کی گفته؟ اگه جرات دارین رفراندوم برگزار کنین تا مردم بگن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/68860" target="_blank">📅 18:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68859">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🇮🇷
هشدار سپاه پاسداران به انگلیس: بیش از این پروندهٔ خود را سنگین نکنید!
به رژیم پادشاهی انگلیس که عامل اصلی بدبختی‌های مردم منطقهٔ ما بوده و سوابق سیاه تجزیهٔ کشورهای اسلامی، کشتارهای گسترده در این کشورها، تحمیل دولت‌های استبدادی و بدتر از همه سازماندهی هدایت عملیات اشغال فلسطین و تشکیل نکبت اسرائیل را در پرونده خود دارد و بیشترین مشارکت را در تجاوزات آمریکا و رژیم صهیونیستی علیه ایران داشته، هشدار می‌دهیم که بیش از این پروندهٔ خود را سنگین نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/68859" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68858">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bypk7hnfNVoiiayhM41YftAGVriNZM_8ak8By9iPavRDC5MD59ZWwwl0bOT3Ub8ht15PvbjQlj1Xn7T2slchbfwhZctV8iPBfealMIJ-h4BGo5YtlqucjxjmWMDHIclBZXbYjXhhBoE10FnVDWGXOQK3U76al2kNGyImB99bywQsoEbCMAccNKJu8iLz4UiOE09oBiCWVW-WuQgNKWOimFI9id94UInjOVYgF9vos8AL0LlS3YXrmr1YqhiJ1eud4ZjvatBKGw4kjjCFH5OtI5A8onhFeGXoxWhBvgfSy2oOsnaD4gUfBglY-FhV_0PsYamFb4ESkaDaP9gMhZZk7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
نفت برنت بعد از تقريبا دو ماه، مجددا 100$ رو رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/68858" target="_blank">📅 17:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68857">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTCU1Ypy9gfBDKNr9WwRr0-zmwMzou74ReYwelKDfQwZsjlSPtmPjfKq5M45hAkhyE0I9qj04t9YqnDh5uTKBVlsC3KxvOEoUQdFDoqFIF9wwZXZWbEwPGi4a-3mghhOmF4aqWXSrYXBY9yv9_KR46Cdfkclfso98icy9dVveS0ageTe3qw9jsajkW__oinfBFtPp02dsTbkcdlWl1BgF1cfw4rYk45kIzdBlvwknHEk5iK7d6Hh0GnyibmHmhqOTv-yi3uQdIQhQ_vAAD4yutJEtrMXLi_UKIQpqftyBvrulpLdhFdjEGXepbjMmw579X81H9NNzrmna7DimikQmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آکسیوس:آمریکا هم‌زمان با تشدید حملات علیه ایران، بمب‌افکن B-1 را مستقر می‌کند.
مقامات آمریکایی اعلام کردند که ارتش ایالات متحده روز سه‌شنبه از یک بمب‌افکن دوربرد «بی-۱» برای حمله به اهداف سپاه پاسداران انقلاب اسلامی در ایران استفاده کرد.این نخستین باری بود که ایالات متحده از زمان ازسرگیری درگیری‌ها با ایران در ۱۲ روز پیش، مأموریتی با استفاده از بمب‌افکن «بی-۱» (B-1) انجام می‌داد.
استفاده از بمب‌افکن‌های «بی-۱» — که قادر به حمل ۲۴ بمب ۲۰۰۰ پوندی یا ده‌ها موشک کروز هستند — نشان‌دهنده تشدید و گسترش قابل‌توجه عملیات نظامی ایالات متحده بود.
هواپیمای «بی-۱» (B-1) می‌تواند در ارتفاع پایین با سرعتی فراتر از سرعت صوت پرواز کند و در عین حال، سنگین‌ترین محموله بمب را در میان انواع هواپیماهای بمب‌افکن حمل نماید.
در بحبوحه تداوم تقویت قوای نظامی آمریکا در منطقه، رئیس‌جمهور ترامپ همچنان بازگشت به عملیات‌های رزمی گسترده علیه ایران را مد نظر دارد. مقامات آمریکایی و اسرائیلی می‌گویند این اتفاق ممکن است ظرف چند روز رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/68857" target="_blank">📅 17:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68856">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d380ae3e6f.mp4?token=HJPex4XPbqnJGMftFuYa6OfsO_abN2mHD8CZi7f-ar-h-V_xgO47Pb2q_BA44UR-efdfct5p89vxem9ZM0nXTlP4baXZPKKdEMo0U4EVRfviiYBWUUDE6pl2p74UAuxB6U3DYQoyhVpRcT3V7TE-isa6cTT89RKSiDV-jHuVYuyPYyyPF2AKPWiT9GOEpMu92zlKdMa4KgXK7-TY1V-oO0O5Tqn0xJ-pgF0BTNIMaR5Z4UGyisVtMvmPk-VxzvisbRVEqJYbcGEIKxWADOyOIghuqajViHak8IvaYjkImZMlG1BHNcCuHpC17Zvrg44yV0v3APXCt37fkZqQjrnR7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d380ae3e6f.mp4?token=HJPex4XPbqnJGMftFuYa6OfsO_abN2mHD8CZi7f-ar-h-V_xgO47Pb2q_BA44UR-efdfct5p89vxem9ZM0nXTlP4baXZPKKdEMo0U4EVRfviiYBWUUDE6pl2p74UAuxB6U3DYQoyhVpRcT3V7TE-isa6cTT89RKSiDV-jHuVYuyPYyyPF2AKPWiT9GOEpMu92zlKdMa4KgXK7-TY1V-oO0O5Tqn0xJ-pgF0BTNIMaR5Z4UGyisVtMvmPk-VxzvisbRVEqJYbcGEIKxWADOyOIghuqajViHak8IvaYjkImZMlG1BHNcCuHpC17Zvrg44yV0v3APXCt37fkZqQjrnR7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پاره کردن امضای ترامپ هنگام شلیک پهپاد به سمت پایگاه های امریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/68856" target="_blank">📅 16:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68855">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:  یک سال پیش، ایالات متحده آمریکا به دلیل اخلال حوثی‌ها در امر تجارت و بازرگانی از طریق تیراندازی به کشتی‌ها، حمله‌ای بسیار قدرتمند علیه آن‌ها انجام داد. از آن زمان و در جریان تنش‌های ما با ایران، آن‌ها بسیار مسئولانه رفتار کرده‌اند. متأسفانه،…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68855" target="_blank">📅 16:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68854">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjjP61JdTVCdNw1PgDMAv7-bevs9mmfasvlwjaJxUjnehxQ67O-iQPhaiE8d8WtxiOzhghnvkE7lSXeNOKJ1xgzIb_jgtm14kfG8TsEn_cFboJVYxW6tGwCwzgfmBA1Dqb04dZVhj3E-0XLFYeRdjAdNiObzpac9SZwN4H1s-7KYOqIqiQiiKW_S84mJ7kHw_tY-QReUmCSg7G9_ccyy7s6W6zu5bcGU6NGYulnMutOo61pI7iH6o0JYA5g0nDC0ZG_q0IaCXJHIivGqEKg1CVpHxqrYhI4oM8cRjND6MV9ZfsMhIeD6MhUQg6g0mwtHG6JMgvEQFAKOnJJO4_rSPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛فرانسه در حال تخلیه کردن کارکنان سفارت خود در تهران است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68854" target="_blank">📅 16:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68853">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J97-xMYL7b5M9xmXHkv28t8eAZfEXCLOGHL8yu4Vxg4RXElx-mGnHcHt0ZfsgP3vrx0ds9oCh1glkfDDGPY-i1Pl6Vbomt4VLqOwzJ3AXCsqwDXYmg4IMgRPqbrFrL5h1CO3_d369nOoszxIh9y-TrewScJQ_aXVdaGOMgBn6G65IDUVvME4hmcLwi1gqko_SgPwa0z_YmrNsUZU7etdwj2tge5IQw3HrI55G48dsQnYeagUXNmt3GulCmqmTHPYRZpjgE5JWeuKGEy0cFWVgW-TNxAM22nTm9cOjcZsHqDICXK4Z3XZQKcFZzIzCRZdrHbrFe1m05UkhMOcQWHXtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت
ترامپ:
یک سال پیش، ایالات متحده آمریکا به دلیل اخلال حوثی‌ها در امر تجارت و بازرگانی از طریق تیراندازی به کشتی‌ها، حمله‌ای بسیار قدرتمند علیه آن‌ها انجام داد.
از آن زمان و در جریان تنش‌های ما با ایران، آن‌ها بسیار مسئولانه رفتار کرده‌اند. متأسفانه، اکنون آن‌ها دوباره فعالیت‌های خود را از سر گرفته و دیشب به دو کشتی عربستان سعودی شلیک کرده‌اند.
لطفاً این واقعیت را مد نظر داشته باشید که اگر آن‌ها دوباره دست به چنین کاری بزنند، ایالات متحده ایران را مسئول خواهد دانست؛ چرا که حوثی‌ها نیروی نیابتی ایران محسوب می‌شوند.
در آن صورت، تنبیه نظامی سنگینی علیه ایران و البته خودِ حوثی‌ها اعمال خواهد شد؛ گروهی که عملکردشان تا پیش از این بسیار حرفه‌ای و هوشمندانه بود و اکنون موجب ناامیدی شدید من شده‌اند.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68853" target="_blank">📅 15:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68852">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n08hvWNXbQH5YYz8XqV0iaLbryDnWUYm9ir1-OyrGUSUMevIWHd8o86fSiHOAAGNisaSsQ1bfxZxNqkiRIcvPbdw5N2Pw-3Yr8N-XmnVg62n7YBvNxzRkHE3Ql-errUwuSZdebZWuYNkz03hRL7O6Njfmkwdu1jITs8uvecoFIg8rQ2veSWqnVlJR8spnuHedcnHIvhXmC0x64H50jaCvN9jLwXSPq-VpM05fZLTWrxsc6MZt3WzXyHg97GRlGsaIqNZakj-s5wF5bCKGfTw0-yVtZyTGq-atRzn4P-1r4WbamfVPGht_vDRrbK7zoj5YSNO3PXDXl3R5AAqseHofA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
توافق هسته‌ای غیرنظامی (که شامل هیچ‌گونه غنی‌سازی مواد نخواهد بود!) میان وزارت انرژی ایالات متحده و عربستان سعودی — که صرفاً به مصارف غیرنظامی، مشابه آنچه ایران و امارات (و دیگران) در اختیار دارند، مربوط می‌شود — تصویب خواهد شد؛
اما این امر کاملاً مشروط به پیوستن عربستان سعودی به «پیمان‌های ابراهیم» است که بسیار محترم و موفق هستند.
ایالات متحده با تأسیسات هسته‌ای غیرنظامی (بدون غنی‌سازی) مخالف نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68852" target="_blank">📅 15:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68851">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ed4a8fc7b.mp4?token=PsqgkhKq0Opxnc_VRTrIb4U_H6uOXKt5icyj2XBCx-fcQ2PzUAIc0pT_YK2VfWAIV4EILY0G25I9yo5B7Pd1EKO1Kan15tKvBvNy44GJD7XBIAAdYlTGmk61bBg1lQQeK83FVnD3eE-iHm7hMMdnyOkj5fLYORrY2srQejfM_OeAn8UUvwGZC1CImOU59ua46rznuK0Ih46QkSRE5lQHKB-DDzAg0pIjpfzxLpik9oU1tqqAReBiZxMaL5LMf3zwX8Ql3UvJuPq3ddmIQrKZw6IZ9kejZTVNHcC_m-dc4DTOQks2-RXBrCq5Dr3AIDA4BSk1Cr83--Fk85NUv8TaIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ed4a8fc7b.mp4?token=PsqgkhKq0Opxnc_VRTrIb4U_H6uOXKt5icyj2XBCx-fcQ2PzUAIc0pT_YK2VfWAIV4EILY0G25I9yo5B7Pd1EKO1Kan15tKvBvNy44GJD7XBIAAdYlTGmk61bBg1lQQeK83FVnD3eE-iHm7hMMdnyOkj5fLYORrY2srQejfM_OeAn8UUvwGZC1CImOU59ua46rznuK0Ih46QkSRE5lQHKB-DDzAg0pIjpfzxLpik9oU1tqqAReBiZxMaL5LMf3zwX8Ql3UvJuPq3ddmIQrKZw6IZ9kejZTVNHcC_m-dc4DTOQks2-RXBrCq5Dr3AIDA4BSk1Cr83--Fk85NUv8TaIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو فروند هواپیمای «EA-37B Compass Call» صبح امروز وارد پایگاه نیروی هوایی سلطنتی بریتانیا در «فِیرفورد» (RAF Fairford) شدند.
این هواپیماها که بر پایه بدنه «گلف‌استریم G550» ساخته شده‌اند، جدیدترین هواپیماهای جنگ الکترونیک نیروی هوایی ایالات متحده محسوب می‌شوند و مأموریت اصلی آن‌ها مختل کردن شبکه‌ها، رادارها و سامانه‌های فرماندهی و کنترل دشمن است.
در حال حاضر تنها
پنج فروند
از این هواپیماها در خدمت عملیاتی قرار دارند و قیمت هر یک از آن‌ها بیش از ۳۰۰ میلیون دلار است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68851" target="_blank">📅 15:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68849">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlJZWBiESMbE_vFnWeXPCkymoNJgXHUvaLC-fJP_KPKztuzskIgaDCna3qBars49gShT0tV5NKewT3RTJvJqkDGdAhFnNLfqjqjCpjVbxSinAkfaFxq_xkmDbxQao1cHYYFnIJ5rHd12yZsjiEaCxz58qgS-WcD-S-OWLh4TLjDY7E68s0MUrO2c1cjotrNQ5-jXoBQzZ7zFgO1T8xeR-rL_LbrGkrG6Z7Vonq6mw7fSWVEo9bn1EEVCvfvzYaFFw-vUJ96SDiaj_McbHMcWi7kvayKP4jm865ITse4YWCPgjkf56indwhYOQXNnj4Bty48_-Er_O-aUZCyl7t03WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c87fead2.mp4?token=HZlWrPiePeA1o5hmlCakb-fif45Yz50l8xzO81VMv5p0MuVePoMwwlwcQfXLzEl4NLNcVPeA3YP33DBhsRjtmWKwhRUCoV_wlizfnBhfiesS4_ufZAom9E2Bi_Eprq9k_FCFfyFmrJvvTGdnRu3vWDbem2Y2RbaA_jrYgXAsMclAgmsJYK3soa_GbvYdhJi0q03RdOUUkgaen5U5fMWaemfLsgkNstx8fyzUC7zg7QtOXlTLfY_NiRQpiAurFfGr7qV_DaBrsPezvfEueCsYtT8pvQPSfEz5wrWWMHyJU2yeea40IWxhlwC4i5W7qt0oLYvBgyj2q9GO5RZfzJkySVaN5sbB5f75WiHaJKgbnHIHEnA_ha54xd4GtPixCwhGB9olHzuH4wDYgZtLdhYP5h8UPrWp4KnbYxLZ9YXHSfg38CoZDdIJbHLUwKPOertt9MVRjVWu16lx1OwLVbzbwnmn4KMrjljR5ledlA8oOe_EiLE-oVuyRdxfiwrwU0wxKhuf07mgnPejv4m4RqQyCyNV2QAfKSu7VGO_3FCWbSoMTQNGHlWz2CgblYap-ctS0Sp1HckXrYKxw5z4DWk17jYGUz7c9Ou5Q4DZqU80bls_LJn7haiMjh86UCqJmwhF_-gwYsNwX-iuES4RCvOSJqG5hGEqvLo584bI3yyCwUs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c87fead2.mp4?token=HZlWrPiePeA1o5hmlCakb-fif45Yz50l8xzO81VMv5p0MuVePoMwwlwcQfXLzEl4NLNcVPeA3YP33DBhsRjtmWKwhRUCoV_wlizfnBhfiesS4_ufZAom9E2Bi_Eprq9k_FCFfyFmrJvvTGdnRu3vWDbem2Y2RbaA_jrYgXAsMclAgmsJYK3soa_GbvYdhJi0q03RdOUUkgaen5U5fMWaemfLsgkNstx8fyzUC7zg7QtOXlTLfY_NiRQpiAurFfGr7qV_DaBrsPezvfEueCsYtT8pvQPSfEz5wrWWMHyJU2yeea40IWxhlwC4i5W7qt0oLYvBgyj2q9GO5RZfzJkySVaN5sbB5f75WiHaJKgbnHIHEnA_ha54xd4GtPixCwhGB9olHzuH4wDYgZtLdhYP5h8UPrWp4KnbYxLZ9YXHSfg38CoZDdIJbHLUwKPOertt9MVRjVWu16lx1OwLVbzbwnmn4KMrjljR5ledlA8oOe_EiLE-oVuyRdxfiwrwU0wxKhuf07mgnPejv4m4RqQyCyNV2QAfKSu7VGO_3FCWbSoMTQNGHlWz2CgblYap-ctS0Sp1HckXrYKxw5z4DWk17jYGUz7c9Ou5Q4DZqU80bls_LJn7haiMjh86UCqJmwhF_-gwYsNwX-iuES4RCvOSJqG5hGEqvLo584bI3yyCwUs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وقوع انفجارها در گذرگاه مرزی «عبدلی» میان عراق و کویت، در سمتِ بصره (عراق)
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68849" target="_blank">📅 14:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68848">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUP5Bp8xcogTptLlrXlfoCYDkVAbYUFJxju5j1cp5gPUSD6URgNT4MmtBT4dl7h-TrL3bJvMIoIbhSnFzC73PNLLfIk9rxSsBCkchgZAF-CAFaa7EM9ikQ-Hjvf4N4QXCm3W_JgiphWNAPBXbMvzjCISi02RePrOK7gjzvVIlfcoCO95y1nAUFgcAJNMKcBg_uqcliCG2v7iKD0MfyXgfwW_vHKFKRZs73aj6y0u-DOR6Wjy1OhCQjwIomPDxzf8Lwsx_DIr_xMGwIaL2V3nHVOB2A-FYjeyI8Yzc3t3G4tugx1EXFpqs-N87dOMPAWaq0rCvggLuTdV5Sa4aEDqSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابوالفضل ابوترابی، نماینده مجلس:
دولت مسعود پزشکیان با ارسال ۲۸ نامه به مجتبی خامنه‌ای، رهبر جمهوری اسلامی، برای مذاکره اصرار کرده و او را «تهدید» کرده است.
قالیباف و پزشکیان در «تله مذاکره» افتادند و «باید به عقل هر کسی که الان حرف از مذاکره می‌زند، شک کرد.»
اگر جمهوری اسلامی «دو هفته دیگر جنگ را تحمل می‌کرد»، آمریکا و دونالد ترامپ، رییس‌جمهوری آمریکا، پیش از آغاز مذاکرات «همه خواسته‌های» جمهوری اسلامی را می‌پذیرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68848" target="_blank">📅 13:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68847">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d3c9fc2c.mp4?token=jVXC7mjqIfu0h8Au4swnQ55mWwRVtCZ5Bbgca7zmCt47gQzamjyYLWdF1QyNHlRKY-pzTv5KjwVvkgEaHELUgweYEoQwmsxfebLo4dVidQB7rpACYaOGqYPdZ_gGi2e_opPQKPV4K6BYht1rNxExqTfVOCmtMN8su6OGvtD-UXuPbK7g15btpQMosCuCddwxyYv9Dqpa8y2zXNlD62bH1fxXYfFjLxAT6OPX9azFWXc2qLo9Jbclzp6kfO5aeSMFIsmQEqjScDm4b71S2iQKCNXtdfpqJxF6Tytx1M_yYWtGpI0huqJqyYPKq5mFA9qj33XCi8GWaSygI6aWrn_scA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d3c9fc2c.mp4?token=jVXC7mjqIfu0h8Au4swnQ55mWwRVtCZ5Bbgca7zmCt47gQzamjyYLWdF1QyNHlRKY-pzTv5KjwVvkgEaHELUgweYEoQwmsxfebLo4dVidQB7rpACYaOGqYPdZ_gGi2e_opPQKPV4K6BYht1rNxExqTfVOCmtMN8su6OGvtD-UXuPbK7g15btpQMosCuCddwxyYv9Dqpa8y2zXNlD62bH1fxXYfFjLxAT6OPX9azFWXc2qLo9Jbclzp6kfO5aeSMFIsmQEqjScDm4b71S2iQKCNXtdfpqJxF6Tytx1M_yYWtGpI0huqJqyYPKq5mFA9qj33XCi8GWaSygI6aWrn_scA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظه حمله آمریکا به حوالی بهبهان
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/68847" target="_blank">📅 13:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68846">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0c9eSdb08r-rVivA52CFnCTIvIqMrpTnKRY0wQnTi1HoXtcBF2v6okkLz7fZ7DdJL3Ys8SZPrKbRyEOodvlSyaxBKZIDfKdtLs-TDexm8yyRs9nfbHuQau0T7sh5pjXkWiZlvhxHkuPiEQyoHEB2ernMof-N71XVj9_Ty3F-cPQ0GUyQFBlzkIchW7ql-qOgHPQS3YNXzhWbt1_OXwX5zwx0CKW2srXGdMmoGUyZxewBpsab4RW439L1sH1WYPCtwjz83fWW7CqnP7p56UTMHooK6P7Cv00t0QA283xiqWOP2TTaP8hV1yF49YPtuPNRQGKw8B7VCYMEGnVOiA6KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68846" target="_blank">📅 13:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68845">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇱
شهردار «رامات گان» در اسرائیل:
«ما تصمیم گرفته‌ایم تمام پناهگاه‌های شهر را باز کنیم. ارزیابی وضعیت نشان می‌دهد که خطر حملات موشکی از سوی ایران در تعطیلات آخر هفته افزایش یافته و دیگر ناچیز نیست؛
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68845" target="_blank">📅 13:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68844">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c953cd20.mp4?token=EIDnlQmKwk1xPO5sMStcXWKdiI2ieroIWEAL01veQD6JmEjnmtT1HzqQVqbiiCPy2gf_1KIA2ywQwPKFJa9pUlLUjkF-EnBLXiyPfnmYYF3_ZZe2da-4vRjzDCZY5naF9PMFoCC_uAbqG53sb56jQCV-n4X0zHtPlhE8zH1-ctlOHOij6ShKPDHdLB3E6mBalME5c5MNzt3ss0O9__WqXpDxcqt4SSjZQ5OWGJQn4iJz7j5RZk9L_e1ibz5Mk_wVCTkk74OBpa86_BaitEmHPIAp5yhxTaV91iK-e65HxcWUNHyhaCOyNQc2vtzHx5XokOjeZjF946uqUxBVA0fj3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c953cd20.mp4?token=EIDnlQmKwk1xPO5sMStcXWKdiI2ieroIWEAL01veQD6JmEjnmtT1HzqQVqbiiCPy2gf_1KIA2ywQwPKFJa9pUlLUjkF-EnBLXiyPfnmYYF3_ZZe2da-4vRjzDCZY5naF9PMFoCC_uAbqG53sb56jQCV-n4X0zHtPlhE8zH1-ctlOHOij6ShKPDHdLB3E6mBalME5c5MNzt3ss0O9__WqXpDxcqt4SSjZQ5OWGJQn4iJz7j5RZk9L_e1ibz5Mk_wVCTkk74OBpa86_BaitEmHPIAp5yhxTaV91iK-e65HxcWUNHyhaCOyNQc2vtzHx5XokOjeZjF946uqUxBVA0fj3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
عراقچی می‌گوید سیاست آن‌ها "چشم در برابر چشم" است.
سیاست ترامپ "سر در برابر چشم" است.
آن‌ها بهای بسیار سنگینی خواهند پرداخت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68844" target="_blank">📅 12:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68843">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzaQu3zoy15SukZGy8R50deJP7Jg7X6b2ZXL0NJNg4G12WRzdFrNch1cbzKKDTs7CTKtaE93cqtczEa39t6JzwsuM7oumJ7wJsdlzGq6U3A8bW6DZhTQdeyfOXfoggIJ6AKWPjofhvv1JfsmQ2i4umGQL8ny3uUzjxn_gdAp3xxvSN-95GndkwQbl3ZmZR3EVj0liyl2KTSLK3RF9_6-HpTpFRhzVHCjcLf4AreT9T6ZgG6J3279XHVudeZ0In5POMcqBvEwUELDW39Qk3i54T6lECYIquv8fE36cN8NVVmyY3a7AXZ-1-1rJry6GtOy_JSt02jq6W5wxVdnM9RCbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پایگاه دریایی ارتش جاسک که صبح امروز مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68843" target="_blank">📅 12:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68842">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c812fbcc36.mp4?token=pj9Fh6QgpeaziedWtui6weQorZEYwvTfx49Gdu3WM7i_6o9Ks3eOPdEs0iS8m-ZlQjbAokWVDdrR8paaz-tq6_ku17Fs_4WEf2gq9fCmhmy226V-pHGqZ94jrEp6Q2XZJPPKbh82u2t13WBj3x2zqOWUnC5wx-UEZaJASWg9QpzXfIqCisAz1AwclfzszTUAaNOgNImnf9c9p69gfyRY1PmKs83bZVQoCxqhORFsoOba1lrcLZgqS3HCOVM_v_Y5CqPWMKkF7Qeq61HqRdbtQcXqeKSgIzwpEuU5UaEL7YLHGTxhDocrKr9xoyoyXITsHaWeeIiNOUNEy44aETBk8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c812fbcc36.mp4?token=pj9Fh6QgpeaziedWtui6weQorZEYwvTfx49Gdu3WM7i_6o9Ks3eOPdEs0iS8m-ZlQjbAokWVDdrR8paaz-tq6_ku17Fs_4WEf2gq9fCmhmy226V-pHGqZ94jrEp6Q2XZJPPKbh82u2t13WBj3x2zqOWUnC5wx-UEZaJASWg9QpzXfIqCisAz1AwclfzszTUAaNOgNImnf9c9p69gfyRY1PmKs83bZVQoCxqhORFsoOba1lrcLZgqS3HCOVM_v_Y5CqPWMKkF7Qeq61HqRdbtQcXqeKSgIzwpEuU5UaEL7YLHGTxhDocrKr9xoyoyXITsHaWeeIiNOUNEy44aETBk8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوای ناموسی در پخش زنده
😃
⏺
امیرحسین ثابتی:
نباید تنگه رو از دست بدیم، نباید تنگه رو بدیم بره. شما می‌ گید تنگه رو باز کنیم، مفت بدیم بره.
⏺
شهریاری، عضو کمیسیون امنیت ملی مجلس وسط پخش زنده :
بدید برررره، تنگه مال ننت بوده که بدید بره؟
مال عمه‌تونه؟ مال کیه؟ ارث باباته؟
⏺
امیرحسین ثابتی :
آقای شهریاری ادب داشته باش چرا وارد بحث ناموسی میشی تو پخش زنده...
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68842" target="_blank">📅 11:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68841">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1ee66466e.mp4?token=ggr8nyNcAOceg5zygr5XkOWo-979ZVTyvXpZBvJX2sew_s1LiUXFxNu5vuEbqhIdWT1v2PertvE7FoqvMJFAJuWPKJp6GnxaR8Ly9e9dGeh1BwVkDMtJ-ie1PzIJjfTxSY1aR8LnwY4qG4JDiiK1QT_-zUiKEADEV9P8FOVFsytuwX-h1YlrPQ9YE-w-K96wM6fToAY0pszdKe72OZu9iDhMYRzFi9ljqahOxhzZk5TBDjXR-v_q30-b5yMucnkoZ45rLP_yazflIgQXsayy_EOVE5kxBVLWzmzye9eiAIzpfj14NYA8oKYukTz-uaRnREEIabDzusgzCwlJ-IZjfoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1ee66466e.mp4?token=ggr8nyNcAOceg5zygr5XkOWo-979ZVTyvXpZBvJX2sew_s1LiUXFxNu5vuEbqhIdWT1v2PertvE7FoqvMJFAJuWPKJp6GnxaR8Ly9e9dGeh1BwVkDMtJ-ie1PzIJjfTxSY1aR8LnwY4qG4JDiiK1QT_-zUiKEADEV9P8FOVFsytuwX-h1YlrPQ9YE-w-K96wM6fToAY0pszdKe72OZu9iDhMYRzFi9ljqahOxhzZk5TBDjXR-v_q30-b5yMucnkoZ45rLP_yazflIgQXsayy_EOVE5kxBVLWzmzye9eiAIzpfj14NYA8oKYukTz-uaRnREEIabDzusgzCwlJ-IZjfoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
دعوا بالا گرفته بین قالیباف و افراد افراطی!
🟡
الله کرم رئیس گروه فشار:
بهتون اصلا اجازه نمیدیم به هیچ وجه اورانیوم بدید بره.
🇮🇷
مشاور قالیباف:
به عنوان کی داری اینو میگی؟ نماینده مردمی؟ اندازه حزبت حرفت بزن زیادی نگو.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68841" target="_blank">📅 10:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68839">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ebdcc84e7.mp4?token=oujL-tBepBqIoJ2fAJHSRXc2m_rcilLaFUuIslYEoAK6LtdVMDcu5vdEbWejJSUEYCV6XZtp5g-CqUTWmB6M25ysDQw7kbi7LFtDpqU5eJMh8Ya7OdXVddy-xcCpfDgJZwJBLd9Vj1QtN4a8DE3eaQQpQELJm5jzLevhtyqDmtc6btu37dpu6BBZAzyK_umjlVRtSLFh11BPWTUbQ3_Qg6VRmZ9uphigVz0k4HKd4HW84M0LrJp5wWaQEF-4NBzJbvQvhRwIWafDtbOeCCvyHmJ5ImILvQGu_mydviscvKwsPlYjac664U8GMJgeAOGyLyW3CrdmYswPmxCQww9Bdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ebdcc84e7.mp4?token=oujL-tBepBqIoJ2fAJHSRXc2m_rcilLaFUuIslYEoAK6LtdVMDcu5vdEbWejJSUEYCV6XZtp5g-CqUTWmB6M25ysDQw7kbi7LFtDpqU5eJMh8Ya7OdXVddy-xcCpfDgJZwJBLd9Vj1QtN4a8DE3eaQQpQELJm5jzLevhtyqDmtc6btu37dpu6BBZAzyK_umjlVRtSLFh11BPWTUbQ3_Qg6VRmZ9uphigVz0k4HKd4HW84M0LrJp5wWaQEF-4NBzJbvQvhRwIWafDtbOeCCvyHmJ5ImILvQGu_mydviscvKwsPlYjac664U8GMJgeAOGyLyW3CrdmYswPmxCQww9Bdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حمله دیشب آمریکا به پاسگاه مرزی شلمچه
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68839" target="_blank">📅 10:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68838">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/soX-Uh6hcLBSm4KxeIhJ5FqjIyKa12R0dYRCknmHJHX8A9FE-f2oNioLlVu0OFFhLwPxyk_WNyfB0z8-MSgPlu-Axn6vWnPSOK3pXpZTenm_dA7dVXrqpkZmwYi40wwC8VbJebAsbVfP5UmMTo9dFkAYVvX9BH8_L3HdRUxRp6mzjDU6fB6GfbPj6bj_HNQGpf-5ogNExsWim6BiBWpAaENzlE7M-A7JnPCUr64q8C3g6-c03MC4hcMvFZWGhZVxmm6eHaqQqHX66o5ShClKfkqVWQKwWuWAF6oCbZSmJRQKHBLWdR8PKkkIJ-Uts1xsa_gio87qnCxEBqd0xnCeTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عکس برگه صحیح شده یکی از دانش آموزا که امتحان نهاییش رو 0.25 شده!
در جواب تمام سوالات نوشته:
با این مملکت درس خوندن جواب نمیده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68838" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68837">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQQ0mVdacPstSJl5xyjsAdRDEOGKZLiMkPy8uotTKSOLo3NWWNfINfXITAQnGLAAIUYMK1RqJEA4UtVp6yJ9YT6Fte9NxmiyvKiKh7jbWErmTxcM-UVntmHluqGuPXotRhhi9_Z9jseckevs22Hq7jGwh20Tu4BaGOTD8k-xkW2k_cxX-8KlA3b3IoX72iNGRsLOrF0ZeXVhs-5bFmTwTtg_vfpxev1Oq87hSMJlb-GtNT45iyq9ME1yl0_1y2xpcohUMGZBXrF3ritGnyI4poICouVv3AyqhdEvX1G1WNP5cjs0qb8qpuTvHSizLAVTapTKsYel_KPmwi-NRNaOTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
👌
وال‌استریت ژورنال: ایالات متحده در حال اعزام گسترده نیروها، کادر درمانی و تسلیحات به خاورمیانه است تا در شرایطی که رئیس‌جمهور ترامپ احتمال گسترش درگیری با ایران را بررسی می‌کند، گزینه‌های نظامی قدرتمندتری در اختیار داشته باشد.
به گفته مقامات، ایالات متحده طی روزهای اخیر پروازهای باری را از پایگاه‌های محل استقرار نیروهای عملیات ویژه به مقصد خاورمیانه انجام داده است. نیروهای عملیات ویژه در مرحله نخست جنگ موسوم به «خشم حماسی» (Epic Fury) در عملیات‌های رزمی جست‌وجو و نجات به کار گرفته شدند، هرچند توانایی اجرای طیف وسیعی از مأموریت‌های دیگر را نیز دارند.
به گفته برخی از این مقامات، بمب‌افکن‌های دوربرد نیز در حال آماده‌سازی برای انجام عملیات‌های رزمی بزرگ هستند؛ از جمله بمب‌افکن‌های «بی-۱» (B-1) که هم‌اکنون در بریتانیا مستقرند.
وال‌استریت ژورنال پیش‌تر گزارش داده بود که ارتش همچنین هواپیماهای سوخت‌رسان، جنگنده‌های «اف-۱۶» (F-16) از پایگاه هوایی «اسپانگ‌دالِم» در آلمان و جنگنده‌های رادارگریز «اف-۳۵» (F-35) از پایگاه هوایی «لیکنهیث» در انگلستان را به منطقه اعزام کرده است. اردن و اسرائیل به عنوان میزبانان احتمالی این هواپیماها در نظر گرفته می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68837" target="_blank">📅 09:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68836">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⏺
فرماندار بوشهر:
روز چهارشنبه، یک نیروگاه در مجاورت نیروگاه هسته‌ای بوشهر در جنوب ایران هدف اصابت موشک قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68836" target="_blank">📅 02:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68835">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a493fb75ae.mp4?token=XKD75xp8apOeMsSmQ3lXsP6cBE7c7w6p0O9m7Vo2y1Tni6JSgKOXMu1DVl7zXQhpCaUpCiJa3udamItfw0vaKEzTpiSoOhaZdWrSYMOkOYUsX-zQS8y3DtbVZHU58vsvXe722hgWBzB2QDDL2qsPf-KLvQS37rcaMMIeHt2tWUOQDNM0DlPWwXYB8pDLmswSScH7ObBsjTuVc6lTSuNxiyYhfMG441jFU6LSFSbDm-7x490Nea2udE5P_dNcH729WheVH--cD5W7LwnzpLs0og3yR0j33icN1slngN691EXVd-dwpPZt-Jaj-xWkWObViU_xjqUNrz9TUypPbqCWjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a493fb75ae.mp4?token=XKD75xp8apOeMsSmQ3lXsP6cBE7c7w6p0O9m7Vo2y1Tni6JSgKOXMu1DVl7zXQhpCaUpCiJa3udamItfw0vaKEzTpiSoOhaZdWrSYMOkOYUsX-zQS8y3DtbVZHU58vsvXe722hgWBzB2QDDL2qsPf-KLvQS37rcaMMIeHt2tWUOQDNM0DlPWwXYB8pDLmswSScH7ObBsjTuVc6lTSuNxiyYhfMG441jFU6LSFSbDm-7x490Nea2udE5P_dNcH729WheVH--cD5W7LwnzpLs0og3yR0j33icN1slngN691EXVd-dwpPZt-Jaj-xWkWObViU_xjqUNrz9TUypPbqCWjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
#فوری
؛مجلس نمایندگان آمریکا لایحه سیاست دفاعی ۱.۱۵ تریلیون دلاری را با اختلاف آرای اندک (۲۱۶ رأی موافق در برابر ۲۱۲ رأی مخالف) تصویب کرد.
این طرح شامل 95 میلیارد دلار بودجه نظامی اضافی است که عمدتاً برای تأمین هزینه‌های مرتبط با جنگ علیه ایران در نظر گرفته شده است.
این لایحه اکنون برای بررسی به مجلس سنا ارجاع خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68835" target="_blank">📅 01:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68834">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0hru1Lr04gM0V5ROdAvYjMji1PHq3SUktopY-J4ywK7ejwlqqXkgwJDgWnMZCBOcutvv1smFexIRz6MDw4cCV_wJyQMGyV_VbdoAXib_8Pj73mjrCJJAD068N2kAmesxSXxWJHQjT0lGTQe8FwSFJp9yiiH-huzGmhShQdzZ1EOrDEKlCnNjyhvP5nle0DfXRI7iRBftgvAGAGFygV3AvfCeiGxvJ886P3SZmfwRj4Qz3X-0hZIwQcVUBJMO_zSiCQRHVu62bxDistTUt_gKWABijX77-H3u-HgK8yamQdJ45e4atW1ZSnbdQs82a3ab4wHoeEV7Is4azi3RRF3FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
ستاد فرماندهی مرکزی ایالات متحده (سنتکام): امروز ساعت ۵:۳۰ بعدازظهر به وقت شرقی، نیروهای آمریکایی به دستور فرمانده کل، حملات بیشتری را علیه اهداف نظامی ایران آغاز کردند.
این مأموریت با هدف تضعیف هرچه بیشتر توانایی ایران در تهدید دریانوردان غیرنظامی و کشتی‌های تجاریِ در حال تردد در آب‌های منطقه، ادامه خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68834" target="_blank">📅 01:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68833">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدید حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68833" target="_blank">📅 01:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68832">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🇮🇷
هم‌اکنون حملات سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68832" target="_blank">📅 01:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68831">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WE6XXiYOJfOUtEcSAnOmAFpkqpH8vWljK7wKoedFK_z7nfspMPFwk7d3hbP1oM5CCZALU-_It733vbxeTnUBNOGkBbofEYCDFjcIO8ZcRSOaVM0qY0LLLdd53Srg8CoYagqOo9b7c9jvXSx7xTZ7Nlr-Po3ZRekxiiurgwEIYhDVhf3AK_Ss5FSC7DrsBBQYRiFFhKqaRqItobCHFOM3F7WSo5QgHUMvM8fvJDnVC2iebZa3mHwwr05pRWxwGMOtrrVzBTW3KR3gUV_Augxay9ahDZsK3htEtifliR5pbdFPb5r1ogESG6rHZA-z8ypO9pgTXV8u4vkHaPbHgbp05w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نقاطی که امشب تا این لحظه هدف حمله قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68831" target="_blank">📅 01:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68830">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0y8WHBInihz3rnEV8GgfwAB6x63gLKtHEr7Ma_d-kj7k6Qc7JGbsvdK2xg05TznN6EgYRZhngTNWsOybuEird5hOzB4dr67DeO3FxEvJKY8InbS2qz-qxvI4kXe3mM5A1ObUlk3r6T2EqDbeafP8mfyH1jhIiRVMh624b0Oc2QB9CdyAXOtw2VD7KOCZI_KYUphl9H9PMQVdgN9eO9j_VvzjiKOGIQA3q8IXe2d9fBoJJlvRznfs2MrJ-BqcHkeBQ1a5rVNUDrgDsC8KOmICHdNz3MgbrA_SKQyKL75d9KWZrFWNUr2YJP9Ilhwg92-EUZg56FUSlDbDsBaeBXi0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
برخی منابع از حملۀ موشکی به یک کشتی نفتی در نزدیکی شمال مرز یمن خبر می‌دهند.  @News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68830" target="_blank">📅 01:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68829">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30afc95033.mp4?token=bDqMy3nW74J_h1UPx7GYkEcIj13REViHq0q5IRSidVjuTHtqVM3_oc2VudLnBOq_MaYtjfHnv6X2j1ruaSKTTZlYNAFCS427R8PDdk7oy8Rwz-YNWquU5LVNfQhEavGcQ1vq734RGD_kEGxLbrau8UR_Xj9UoGfPPn2Bw83jn8mVKMs-azWNfWmdkh1NGxCAOFs9bM3GsC6o2CqB-tUlMp1cHxgzLOEvp5RGNwtcOha-btqKdg8UmYqNt1f_R6kC3tq4EBhib38vE_g_8alsKbv1-37amNFBpph-hIGe9wRcwu_feDpQuI94IDPEZCAyi9jsHHH_smTsR5f_pk0kWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30afc95033.mp4?token=bDqMy3nW74J_h1UPx7GYkEcIj13REViHq0q5IRSidVjuTHtqVM3_oc2VudLnBOq_MaYtjfHnv6X2j1ruaSKTTZlYNAFCS427R8PDdk7oy8Rwz-YNWquU5LVNfQhEavGcQ1vq734RGD_kEGxLbrau8UR_Xj9UoGfPPn2Bw83jn8mVKMs-azWNfWmdkh1NGxCAOFs9bM3GsC6o2CqB-tUlMp1cHxgzLOEvp5RGNwtcOha-btqKdg8UmYqNt1f_R6kC3tq4EBhib38vE_g_8alsKbv1-37amNFBpph-hIGe9wRcwu_feDpQuI94IDPEZCAyi9jsHHH_smTsR5f_pk0kWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
برخی منابع از حملۀ موشکی به یک کشتی نفتی در نزدیکی شمال مرز یمن خبر می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68829" target="_blank">📅 00:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68828">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
صدای دو انفجار در بوشهر شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68828" target="_blank">📅 00:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68827">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
فارس:
حملۀ موشکی دشمن آمریکایی به یک سولۀ انبار آسفالت در اطراف رامشیر استان خوزستان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68827" target="_blank">📅 00:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68826">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqYqdb5BYgyluHpRRz-IDDuYzWSXBC0W6okFgLR3W5CTcuNd0q9Efy-xRvb-Co1NSn19U0M19d6Z-WpnSO5EMwcefYL4WznWZ0p1ghd5Ehg-GK3VVV7t5x4pWY4wxY4hZEzgmvXHLrx53r1E7s76wEfxskNt9e4qtpzAgDU5V8BOcA5OpcU9Ffrj1Ddbm0p0MRqvh5ky-Xvdjv-EDX73BcQ39KcsDr0HkmYAtIU9WVoaRq9jLykqf8Xm8UseI3SJUqDvd3Vu2bw9epjTmZ89zVcvaQHwicT_OoWeSYeggP1KoSFsFdsLH9EB8K3ot0KEew41UeGjuaJnd-JNdKVMuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
یک جریان مداوم از تجهیزات هوایی آمریکایی به سمت خاورمیانه در حال انجام است، که احتمالاً شامل هواپیماهای تانکر سوخت‌رسان نیز می‌شود، در چارچوب آمادگی‌ها برای تشدید عملیات نظامی علیه ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68826" target="_blank">📅 00:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68825">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
پاسگاه دریایی زیارت در سیریک هدف اصابت موشک قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68825" target="_blank">📅 00:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68824">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
دقایقی قبل صدای چندین انفجار در اهواز و ماهشهر نیز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68824" target="_blank">📅 00:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68823">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
صداوسیما:
چند دقیقه پیش، صدای انفجاری در منطقه بمانی، واقع در شهرستان سیریک، شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68823" target="_blank">📅 00:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68822">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/030860acf9.mp4?token=hPO8wYUEir4r2Zl6HyvDwD68dllTD5LQRruHQBnF7nny0YGCqFnubPSbnfKUrCppzMYmHAUvSVt75CleTnUEYLvExOrZSEFDPRH4mhur_lfZHB1jWV7pKb460X0TLqT1cvzbXvE_CWt69UnN6pDm9wWX54klPHMwtuPpPnDtILb1CXEF2hLzA9boJkJqeYUmeBfqNnfzoyz4tkom8lzg7CHRDBARH0P5EU9pw4ND8PEshWnDtDjJ0Ta5GFNlIDWmedQAWAnWLVvYlQqjtoE9z_OUqRuAEIfYktRSaSZfFiMtrtcRO34tBHC9QDNkFfCLDBsXcbcexAq1x8t2el4dKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/030860acf9.mp4?token=hPO8wYUEir4r2Zl6HyvDwD68dllTD5LQRruHQBnF7nny0YGCqFnubPSbnfKUrCppzMYmHAUvSVt75CleTnUEYLvExOrZSEFDPRH4mhur_lfZHB1jWV7pKb460X0TLqT1cvzbXvE_CWt69UnN6pDm9wWX54klPHMwtuPpPnDtILb1CXEF2hLzA9boJkJqeYUmeBfqNnfzoyz4tkom8lzg7CHRDBARH0P5EU9pw4ND8PEshWnDtDjJ0Ta5GFNlIDWmedQAWAnWLVvYlQqjtoE9z_OUqRuAEIfYktRSaSZfFiMtrtcRO34tBHC9QDNkFfCLDBsXcbcexAq1x8t2el4dKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه روز پیش که پل کهورستان رو زدن ، سریع اومدن یه جاده آسفالت از رودخونه خشک شده اونجا کشیدن که رفت‌وآمد متوقف نشه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68822" target="_blank">📅 23:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68821">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b162fcc101.mp4?token=QFgYHxYGLTwAXrIr8tCNaW3T1EfavM4ZeDhBsI1Svib4EyPSXeymBxsi_5chwFYY0YhO5l4iNf7xPc1IM7HF3M2aehne2_Va9rzTRyMkSfTEyDjUJr2MyPqMJ6a22sgVLY8JASdkQqAu_wxK71tkpcjc2rkbYQSiINlBaQuwLAWk8DCH4xfm1F-1D4RKhBNDZjJGobxKBixxjv0bHuiFrGsSECUoCTH7USlLvN9wzSmRhz4F49FHG3E7sshYbqRTIEDtlzOfdAKLGNJujJvqCnB_HfI-WJdKltRYhwJuSFYtI6IFvmbvGWYvv4uXrk_8_0LRXxqYs76Jx05eGVrQKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b162fcc101.mp4?token=QFgYHxYGLTwAXrIr8tCNaW3T1EfavM4ZeDhBsI1Svib4EyPSXeymBxsi_5chwFYY0YhO5l4iNf7xPc1IM7HF3M2aehne2_Va9rzTRyMkSfTEyDjUJr2MyPqMJ6a22sgVLY8JASdkQqAu_wxK71tkpcjc2rkbYQSiINlBaQuwLAWk8DCH4xfm1F-1D4RKhBNDZjJGobxKBixxjv0bHuiFrGsSECUoCTH7USlLvN9wzSmRhz4F49FHG3E7sshYbqRTIEDtlzOfdAKLGNJujJvqCnB_HfI-WJdKltRYhwJuSFYtI6IFvmbvGWYvv4uXrk_8_0LRXxqYs76Jx05eGVrQKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ما به تنگه‌ها احتیاجی نداریم؛ اصلاً به هیچ‌کدومشون نیاز نداریم.
ما نیازی به تنگه هرمز نداریم، اما مجبوریم این کار رو انجام بدیم، چون نمی‌تونیم اجازه بدیم ایران به سلاح هسته‌ای دست پیدا کنه.
من اسمش رو جنگ نمی‌ذارم؛ یه درگیری محدود بین ما و جمهوری اسلامی ایران.
اون‌ها اون‌قدر تحت فشار و ضربه هستن که می‌خوان توافق کنن، ولی به نظر من هنوز آماده توافق نیستن.
الان هنوز آماده توافق نیستن.
ولی خیلی زود آماده می‌شن
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68821" target="_blank">📅 23:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68820">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🇮🇷
ستاد مرکزی خاتم‌الأنبیا:
رئیس‌جمهور ایالات متحده، که رفتاری بی‌منطق و جنایتکارانه دارد و به قتل کودکان متهم است، بار دیگر تهدید کرده است که به زیرساخت‌های این کشور حمله خواهد کرد.
اگر این تهدیدات آمریکا عملی شوند، نیروهای مسلح جمهوری اسلامی ایران اجازه نخواهند داد حتی یک قطره نفت از کشورهای منطقه صادر شود، و زیرساخت‌های نفت، گاز، برق و اقتصادی منطقه هدف قرار خواهند گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68820" target="_blank">📅 23:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68819">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5763ed03e8.mp4?token=lxwXVzQk15MFLDmX7AjdCxjgvj-FW5nfenycsGw6p0FGi87pAasxbQcKPzKuA46jGEHH5C7rxSRXdDbhRAA_mffY4spGHVXGVhAnvf4trKnfuNYThuE6nky9Jvjfs7_LIGcHqd_c2OGSDKpIwKM7qXGklNS-PVxBPX39H0bpDeqMPE3fTNyeemEuaYfbQOgv8byy0lf3ozIL2waOs5ejXkw_a71CRe-PVYr-P3ktRICx6XA8rc6hw9qDhHfV-AKdVhb9STfInCaYSdbec-we8Mv3Zv2esskGwRwFkyPX11x2lR7iJjdsDm3kRQoQ32iA5j-p_Ud9EWd3220Dq_zktA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5763ed03e8.mp4?token=lxwXVzQk15MFLDmX7AjdCxjgvj-FW5nfenycsGw6p0FGi87pAasxbQcKPzKuA46jGEHH5C7rxSRXdDbhRAA_mffY4spGHVXGVhAnvf4trKnfuNYThuE6nky9Jvjfs7_LIGcHqd_c2OGSDKpIwKM7qXGklNS-PVxBPX39H0bpDeqMPE3fTNyeemEuaYfbQOgv8byy0lf3ozIL2waOs5ejXkw_a71CRe-PVYr-P3ktRICx6XA8rc6hw9qDhHfV-AKdVhb9STfInCaYSdbec-we8Mv3Zv2esskGwRwFkyPX11x2lR7iJjdsDm3kRQoQ32iA5j-p_Ud9EWd3220Dq_zktA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو این اوضاع ویدیو های سمی هم وایرال میشه
😔
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68819" target="_blank">📅 22:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68818">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X52L9HESVpRNl38QmNu_UcEpUNz2sYOTxcBD1D2MR3WoDzDlUnrUqdqEB3PsGpFACF--RfqZItd8rdsLB28pUK0JX_uvGeEdsNmXxNtHjhsIvKVMk24_Zq1JkmdM3Ozpbu0mkv_fdJLz_h4EqpBovWGcrF3amM7aApA9kYn0QWBnb5--FUw8YOpo3WvtvDk7spY7kZjH7fQRAuEfezkKLwBm33MkpeYuAUPR97Kp1kfNMiHNvifjqWMzCWyGWpwdxdWysiusXr5jmPPDaJDoMR8gNGIEaHrCA0qdSv-eIBcp5Lb_u6cTotJ5y220IDhPDgfl7m8BObEHQaDseWT36w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مجید موسوی فرمانده هوافضای سپاه:
اگر به پل‌ها و نیروگاه‌های ما حمله بشه
خاموشی برق متحدان و میزبانانِ کودک‌کشان، قطعیه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68818" target="_blank">📅 22:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68817">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad77b1ff68.mp4?token=ON3WwSbuyEGTug8bVLineAN7iM5w4BQ6Dc_RkWGpqBRYwdo9Bu_D9RE5RwUdexy9jWmpNYdQxMO2o8M4o0fKVk-9cKDy-2MMlutl33qjEmglcsmCPEcrBIFQFU5sCTY7qeRUOcqMNhqj3ISr7Th-r9M1EEp8cUaA1XI4tIj65wr8IYia59XSviLZXb9ibukWBRS6lnl4sfFXb2Ksd6VpqoL8LrFZeFtoQuAbuHt3mNK56xW5Ae_E_b8os6AL8okwqvgHnKnu1EGJ4rCTB2v__83s3U-Ri4stF4MLtm9EL6cmW4KkRKBQrAGAt0p-PFY7c7K8QZp0AftxSNL9EGutGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad77b1ff68.mp4?token=ON3WwSbuyEGTug8bVLineAN7iM5w4BQ6Dc_RkWGpqBRYwdo9Bu_D9RE5RwUdexy9jWmpNYdQxMO2o8M4o0fKVk-9cKDy-2MMlutl33qjEmglcsmCPEcrBIFQFU5sCTY7qeRUOcqMNhqj3ISr7Th-r9M1EEp8cUaA1XI4tIj65wr8IYia59XSviLZXb9ibukWBRS6lnl4sfFXb2Ksd6VpqoL8LrFZeFtoQuAbuHt3mNK56xW5Ae_E_b8os6AL8okwqvgHnKnu1EGJ4rCTB2v__83s3U-Ri4stF4MLtm9EL6cmW4KkRKBQrAGAt0p-PFY7c7K8QZp0AftxSNL9EGutGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ظهر چهارشنبه؛ لانچر مستقر در تپه‌های پشت اسکله طاهرویی (سیریک) که روز گذشته مسئولیت شلیک به سمت کشتی‌ها در تنگه هرمز را برعهده داشت، خود هدف اصابت موشک قرار گرفت و یک ستون دود از محل برخورد دیده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68817" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68816">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nl_uHn6XIWcfqPGnsh1sYtFMWtsH_NgNN7wS-ZJ5Y5ALqfUdCtSfZdju9UtWNhMwIm8cEmsZZYiVqZp5n0PVRvlH6ZU42gVKKFdvIpw7oCPx0HCQ4kqCbiBUGuO5ryAVJ3DeW2dF_Y2pWk6Ky6DsX_DiIPfDmOPF_Jb9QIdCuYS0GGw6onuyqC3mYRRme6Oem9Wq8ExEhnTM6QVvmrocTTTN9Xet_FEBbreaaH9fk4DEqA3HXZSjKtIKTg6rAfy8cRPS-mx4eBHK-48-wf5u51lkLZjJaN5pO-pKVUneYsj-fPQY6TC7HfXwQgXjmW2Cd0pu5VjaMgGCwVEDKXpytw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:معادلهٔ این جنگ مشخص است: یا همه یا هیچکس!
در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت.
اگر امنیت ما تأمین نشود، هیچ زیرساختی ایمن نخواهد بود و امنیت تنگه در نبود نیروهای آمریکایی است.
بارها گفته‌ایم که وضعیت تنگه به قبل از جنگ باز نمی‌گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68816" target="_blank">📅 21:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68815">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeVPJkIBru8-yIcBtpzrc_SPI7W31z9x6zTCtZ1Q7eVQ7g_eSe-t6a8DfwDnykDH4ld8rXvAsmb_i_GFNThmfDF1KHL0Vblbaag74k-bblpUPJYGzmO7UWn3ABMEdoQiVVl3VxZEXL3_R4IHE9swQTHS7NmwHxDRbl8wKZyw-4moP48x8erS0ZVwnavWnKtt9dYfu7rDp4NNe8dn6iq9tbhy4E1Dmz1jcXpcBgMDzSjLduSKSKNk32fbBLpWLvWq0fN5Ar-9_DpgZ11OkhM28A84UVFyhdi7Ux0xl5NQjFzC4H0PJ6EIErYj40YWHvyLOULNztl9u3rAJZD92bxXUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست جدید ترامپ در تروث سوشال:
رئیس‌جمهور ترامپ به‌تازگی اعلام کرد که پس از کشته شدن نیروهای آمریکایی، به «سنتکام» (فرماندهی مرکزی ایالات متحده) دستور داده است تا «درهای جهنم» را به روی ایران بگشاید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68815" target="_blank">📅 20:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68814">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای باری نظامی متعلق به ایالات متحده آمریکا به سمت این منطقه، به ویژه اردن، در حال حرکت هستند.  @News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68814" target="_blank">📅 20:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68813">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qls3tdYZPcAi_HEH_kEtzOxSV0OGzlQmA3MHr7etxf9oxoDXkNgWB6j0ZxsYkaWiJIAyTiLcUeJszGpTpYj04B6wigFeaj9qF9C9M55-pHtBDhkRI9AB3A3zYsqT5dDJkpDmkci1Tl52T9S1qFhKlHfOf-Zed9cWqzJivJx6pYuhjp4b1N_go2KfFYvYXfQyK1VkodNNu3I425nFOUvvxkDzCPhiVNcbwvfv-_Sn9kIYWEb2uCvascZz1PsmTAiD7hNiwbxa2AgtnATPVMAfgbRomGWG6kRhJy7ghBYbGKGIBChSYOMUfrNH6l8UMynIteyKym7NWSirGKJ4sJtfmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تعدادی از هواپیماهای باری نظامی متعلق به ایالات متحده آمریکا به سمت این منطقه، به ویژه اردن، در حال حرکت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68813" target="_blank">📅 20:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68812">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdxT0--Yw1ajT091a1aJmmcUWj1lv4C-nAyjL90O7oHpJSLZbOMAJk4UFu8pDxK9D6WfK9Lamqz_FdgBieERBYx0evVZM06PS-7dEh8AybylS_K7TGNLqj-9KzPOXgUQFdvTPMrIAQbw6E0Fu-hU30itguAaFF35BmWEhsXMCRSfExvGR_kY2xkkwX7EpgwUamISsiUA4Uw6PczjLyXD7asC1xtbUb56mwirJK8FHXzQVXhum4BLzsghSw3y0EXkbX7VyDsC0KrLDiyT-zFpR6q78V_zVw5HT63QvXKR98kVkxtHuTnZE8LgSK2Dfn9bon6wg-SgHpPVsyz7fnaQGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
یکی از حملاتی که شب گذشته توسط سنتکام در جریان یازدهمین شب متوالی عملیات علیه ایران اعلام شد، بخش نظامی فرودگاه بوشهر را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68812" target="_blank">📅 19:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68811">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ptzab8kaJM4MkaTuwHCQtk9sck5N5hYuXsT_Vfo7lUcqAtCAk8dmTUymgdRBafMkBYffUUqWlPlzm8PRGot154HKu4NP9bQCwO222HqPWk0FzQs2SJQoSjaRNqUsK4KJQgZGbv4zX8EtjWQQgM3sJNYlf4wSLf7eDaA04uqbrpC0pBodrGWKdEGPZ5IsGn_AbIeMwgYEBSqo1hztUB0y3SJ-_pJBQzLsuCZiQGyrHVaX7eJUA0gYF2h2ymZYmb0kKhHpZBbkpNRTEkO_MbDv6Y0vJBg9u-uBw_hxxffdDEb2EqTg1ex2XQ52pVum28W7PiUXPNJB--N-oL2rOx1w9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
قیمت نفت خام برنت به 93.14 دلار به ازای هر بشکه افزایش یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68811" target="_blank">📅 19:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68810">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaldzV2SYWdwZeWlI15H7Ygw9ASRQhRH6H98f8D9GPAb0bUgPxvXLVDgdB9rYqJ37Dy4JHpfBWSHD42pSTig4Zgse6GEDaeut5qgTD46yg6LCvHaXTdk9uC0ACuIPBhau2GQQBHSH298Wo0XBv-An8S0TIcYCrhYQ38DmMYtznfxhLb5hl4gb0EiG8yH1oEAAYByuF-MxSdtQ2Ff0Bqg2FXv4loXdhZ4XrleIM9khb1YDOcOFoQ9GFRovvLpO-EMZ7FNHTi9GSGCsin31lMSRI_0hAhoYCpuj0dugrBsQHBn7kz7VJvRS58djqhFN54_QkzSN1xuAxXpG4698dRMZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68810" target="_blank">📅 19:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68809">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b26a1fb249.mp4?token=UGfYzpKbZMiwkseUCw60I7n9b9ujvOtDg3m94TkZGxYonHnOpic_zoAZT4E-fundJWwYTNEgZb9ncbBFyMuZCy5ZxVciTajm61MALlIkE6ZOLdkit2BSn59KbRE4nB9s_0dzV3SqxR0Fhoz5fpI_pvRNsYQ5fU8IL9OngqvD32IAwORHWSZYCTlgC8P-wmDhQCvOuEbPiL2RLDQycFSoG0VEPMAPz5GFuu2e34r1HgEXktvAnrPGdRvRWH4vLck_ruwHqdLZO4sSIP5QXjVotrqV3QOr80QWPanelt3bSI2bd9EVXXbXR9eMm2slvGaJaCLcIlwA0lAQ2xOEYvOABw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b26a1fb249.mp4?token=UGfYzpKbZMiwkseUCw60I7n9b9ujvOtDg3m94TkZGxYonHnOpic_zoAZT4E-fundJWwYTNEgZb9ncbBFyMuZCy5ZxVciTajm61MALlIkE6ZOLdkit2BSn59KbRE4nB9s_0dzV3SqxR0Fhoz5fpI_pvRNsYQ5fU8IL9OngqvD32IAwORHWSZYCTlgC8P-wmDhQCvOuEbPiL2RLDQycFSoG0VEPMAPz5GFuu2e34r1HgEXktvAnrPGdRvRWH4vLck_ruwHqdLZO4sSIP5QXjVotrqV3QOr80QWPanelt3bSI2bd9EVXXbXR9eMm2slvGaJaCLcIlwA0lAQ2xOEYvOABw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس انقد کد کد کرد که
کص
از دهنش پرید بیرون
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68809" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68808">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccda4020d0.mp4?token=L2aq_4sYkgHxA1Eh6WAK5UMO3VENqFXqaC4-VVOtoq1OKJr3YSc4vGBQ_9rVqXYSIjQ7vq1LcbUDlxmJop5MB9CjnSsG1GabvFu2T_ZmZpnvaT2Qth1OCh59ZY2_WxpQ2pX5JQ-6AZJh5Ptng9i-h5aQ-KidHjxv5zK0b93MzfCEoYeJoLiy0PMCMwQbpibCf47ay2Q9Aw0tbeeM0_ydB8tCY-xN_xD8PKxn19cvfK1P8pb8OfmtAjPV_wWTHPyk2EuoWb4JDrwh1vEA8QXzi_kV0__49mA6ir9VguBYv1Zp2ZXt27kCwFqczFPpr-GmXkLoggrj9vG7z9oEpoWHpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccda4020d0.mp4?token=L2aq_4sYkgHxA1Eh6WAK5UMO3VENqFXqaC4-VVOtoq1OKJr3YSc4vGBQ_9rVqXYSIjQ7vq1LcbUDlxmJop5MB9CjnSsG1GabvFu2T_ZmZpnvaT2Qth1OCh59ZY2_WxpQ2pX5JQ-6AZJh5Ptng9i-h5aQ-KidHjxv5zK0b93MzfCEoYeJoLiy0PMCMwQbpibCf47ay2Q9Aw0tbeeM0_ydB8tCY-xN_xD8PKxn19cvfK1P8pb8OfmtAjPV_wWTHPyk2EuoWb4JDrwh1vEA8QXzi_kV0__49mA6ir9VguBYv1Zp2ZXt27kCwFqczFPpr-GmXkLoggrj9vG7z9oEpoWHpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
عراقچی: ما به هیچ عنوان غافلگیر نشدیم!
واسه همه سناریوها برنامه داشتیم و کد بندی شده بودن.
سناریو آخر این بود که رهبری (علی خامنه‌ای) رو بزنن که کدش 110 بود.
تو جلسات کسی دلش نمیومد درباره این کد صحبت کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68808" target="_blank">📅 18:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68807">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
یک منبع نظامی به تسنیم:
هر پل و نیروگاهی از ایران هدف قرار بگیرد چندین زیرساخت و تاسیسات انرژی منطقه را می‌زنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68807" target="_blank">📅 18:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68806">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⏺
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:  بنابراین زمان آن فرا رسیده است که کویت، قطر، عربستان سعودی، بحرین، امارات متحده عربی و احتمالاً عمان تخلیه شوند.  @News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68806" target="_blank">📅 18:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68805">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c81b68d9d4.mp4?token=V8eSDz4_ItPrVDhjLXn9SX9zfTq6HLxXh0LeeoyhU4zpjyfHr3rjgUzCtkc9tylJdAZSxnwHOdUyJF8mg1oa0f3UdLDlCOymXiGJRlLHeuXOH0jOd_I9KlElAPyRqXSonLkQwHGUUusoyLAAKn1i19DiAt_CwCVgZBHyPFCMRaKZOTZCVM_UKjE8WG5OQMdeZJ4W1Fybr6FQ-1QjjrKY9YQ6Qxfxch66mwAt75n-BBg9kXAD6_zqPsFSBBL4qEtM4AaM8s5M04YGNc2N_sIjLoWV7M1JM7uB_e99vEq1CXjnUC_Gh3bzq7F7SWTCtPGO2WEGNBrhE856nuXwlOniyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c81b68d9d4.mp4?token=V8eSDz4_ItPrVDhjLXn9SX9zfTq6HLxXh0LeeoyhU4zpjyfHr3rjgUzCtkc9tylJdAZSxnwHOdUyJF8mg1oa0f3UdLDlCOymXiGJRlLHeuXOH0jOd_I9KlElAPyRqXSonLkQwHGUUusoyLAAKn1i19DiAt_CwCVgZBHyPFCMRaKZOTZCVM_UKjE8WG5OQMdeZJ4W1Fybr6FQ-1QjjrKY9YQ6Qxfxch66mwAt75n-BBg9kXAD6_zqPsFSBBL4qEtM4AaM8s5M04YGNc2N_sIjLoWV7M1JM7uB_e99vEq1CXjnUC_Gh3bzq7F7SWTCtPGO2WEGNBrhE856nuXwlOniyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
دونالد ترامپ درباره ایران:
«آن‌ها بهای سنگینی خواهند پرداخت. آن‌ها در حال نابود شدن هستند.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68805" target="_blank">📅 17:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68804">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKheksiqNSpkE4T4ie24sdRHKZkCOfjfTs9QhdWuu2D37X5eq8lHvLCGghUSA0dp8rDCGhX3NjgY8u7LGK72Vv3HgizYdHKVHndT0yGbiBqZb1MrIpPYyHoSSgBsjUlpiVD6OvvmWwU5cB5Ahibja3oHcAQtCNqLzH7-ZP9Gd9j2Zur4Qj8ACkPY2oGbRhc2iTyhn2tlwoJ-xP-t1XH-_Mo5LAMhX8spTl80D9umLadJiyMN3RRX6cvE5ywp8bY8FtmkYajDhSn0M0kfVN8Wl5TtJMd-f1MyJh_ktYmQOpTaSOfpZtciglyHR9Zsnqzkkj5a0UdS4DERE8K-H5wKlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:
بنابراین زمان آن فرا رسیده است که کویت، قطر، عربستان سعودی، بحرین، امارات متحده عربی و احتمالاً عمان تخلیه شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68804" target="_blank">📅 17:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68803">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxbmQuFba9izsQKQ-1qQnl8ghzw35MzN-1Jz7Tap1JknU_n921tQFpfwUtwcyqhpk2xa9RdUNwh5bdHqiAVKLEOk-esR7FqeCowFWDQGugksfq0wZrftkXXWwc-i94-pXPhbS27CgqwHYreApuws5PBO8JqKU27O8f6F-Ju011GogGMUFx8sDY9nT04wGmjQUkGnjoMrhoqvE6QXYVLwlOmPofuT9np9uuvVkauliGaoi7iDe8pdAwzGYUUVUjcMM6yuw8f0oxh51QOrnVxBZv8RGistTds2vLKNV0KZqY4NPgZxlgS2eBetM-l_m5hadmtA7zKGQBhTDS2atYjnig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگه ایران از این به بعد به هر کشتی‌ ای توی تنگه هرمز شلیک کنه، فرقی هم نداره با موشک، پهپاد، راکت یا هر سلاح دیگه‌ای باشه، آمریکا در جوابش یه پل یا نیروگاه برق ایران رو میزنه
حتی اگه نزدیک تهران یا داخل خود تهران باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68803" target="_blank">📅 17:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68802">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d80a636f.mp4?token=nW0UEO5Ef5UpdqhxGH93vU7sWQTJkVd95dPlGZNPbeqQNkDY39FyaEE_Q1cXcvPK8eqiPrMe430yJjxYNX0fGNibtp5_8M3BX49Gb2paN32GXfXFR5koaWWOZUa410JLr0UubywniliTttSp7K4pu_jTsNfmoAy3JgQe_Aus4FPMmJnu3RqlPXz2cz2D9bwtpb6F5pjLWI6E2B132xdChwPBfCee6fI4WPBjZ1Kc0B4y4T86jJ4fPR1AiRDmVRndMUClqHfgMLP4TWEsJicnNP4Irjm8bCC_NiBAdGVDqkTwnf5-kOcBVt2ZiFf72FtT7iKH0a-10E_SvY6FBDLvNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d80a636f.mp4?token=nW0UEO5Ef5UpdqhxGH93vU7sWQTJkVd95dPlGZNPbeqQNkDY39FyaEE_Q1cXcvPK8eqiPrMe430yJjxYNX0fGNibtp5_8M3BX49Gb2paN32GXfXFR5koaWWOZUa410JLr0UubywniliTttSp7K4pu_jTsNfmoAy3JgQe_Aus4FPMmJnu3RqlPXz2cz2D9bwtpb6F5pjLWI6E2B132xdChwPBfCee6fI4WPBjZ1Kc0B4y4T86jJ4fPR1AiRDmVRndMUClqHfgMLP4TWEsJicnNP4Irjm8bCC_NiBAdGVDqkTwnf5-kOcBVt2ZiFf72FtT7iKH0a-10E_SvY6FBDLvNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
مقایسه جمعیت ۷۲ هزار نفری در کنسرت فردی مرکوری در ومبلی لندن (تیر 1364)
و جمعیت مراسم نماز و تشییع علی خامنه‌ای در مصلی تهران (تیر 1405)
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68802" target="_blank">📅 16:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68801">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⏸
ویدیو وایرال شده از گریه های یک دختره بخاطر مردن سگش
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68801" target="_blank">📅 16:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68800">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏
🇮🇷
سپاه پاسداران:
«اگر تجاوزات ادامه یابد، آماده عملیات پشیمان‌کننده‌ای می‌شویم که اعلام عزای عمومی در آمریکا را به دنبال خواهد داشت»
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68800" target="_blank">📅 15:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68799">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTkFhBDQmiO6EXcAPrx_nzBEEtsSmeW_hsp5nhsRMhopJDLyKXrhy47FQ-TOgluUCcUovnsagdwX2EhETQo8XWwU6o8PoSAWSUu0JZaHe_jFE_LRCjrtl1Vw3XHxGIXHjW0ULPltlxGMSLZRi1ht1ohz_x-8q2Gk7UA3kxYwQ7Wb8RlwQjIpbnrGMYisqvTA2D3hWIFL6EpONj8s58ox6XInl-gDVafdgOVwAdB-SgfNJxG-2hTDJyO4GxdmVGwHT9PK9VqinFeBG2IsWuEewIRGK1MjoLA3wgTXBzdHtG2cjZlYo4-my12M0OGu13yXifNnd2Kd1sogs8nb0u3QrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فعال شدن آژیر خطر در عربستان سعودی
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68799" target="_blank">📅 15:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68798">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه پاسداران به بحرین و عربستان سعودی حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68798" target="_blank">📅 15:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68797">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a7bb5d120.mp4?token=Yssnp6if9Uf13U0DATHjSmJgeRcVsiUyPZ8yS5ZFu5g0G_jViXKGz6Y9GrbyNLbqllZTc9IJvti-lfAJE-girYH_SysGxtsr6iwzQDu7EcOUW6yEJQhZ43tiNcaxsr0DAZR1XgcDsenJfTxM5cZPjV80Ucs1svBoHVWXgAc0qtFOlfPeLz3iIQFcvc9fsKO2pQb6NB3tUxZXBmavIG2Ct9UIheiKsXWXhGUy-JRRSMtZy3R-nU-2Kr09L5TCStUABQ5wTbPKSexnmWl5TzvVd51Q6WNw6qCA5s4HS3NSCg1fmpYhEh-juK0PGG9erv706uMgmwiWf4cYw__OOSoBzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a7bb5d120.mp4?token=Yssnp6if9Uf13U0DATHjSmJgeRcVsiUyPZ8yS5ZFu5g0G_jViXKGz6Y9GrbyNLbqllZTc9IJvti-lfAJE-girYH_SysGxtsr6iwzQDu7EcOUW6yEJQhZ43tiNcaxsr0DAZR1XgcDsenJfTxM5cZPjV80Ucs1svBoHVWXgAc0qtFOlfPeLz3iIQFcvc9fsKO2pQb6NB3tUxZXBmavIG2Ct9UIheiKsXWXhGUy-JRRSMtZy3R-nU-2Kr09L5TCStUABQ5wTbPKSexnmWl5TzvVd51Q6WNw6qCA5s4HS3NSCg1fmpYhEh-juK0PGG9erv706uMgmwiWf4cYw__OOSoBzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شاهزاده رضا پهلوی:
هم‌وطنای عزیزم، مردم بزرگ و شجاع ایران،
با توجه به اینکه تنش‌ها داره بیشتر می‌شه و احتمال داره حمله‌ها، مخصوصاً تو جنوب کشور، گسترده‌تر بشه، می‌خوام چند دقیقه باهاتون حرف بزنم؛ به‌خصوص با مردم عزیز سیستان‌ و بلوچستان، هرمزگان، بوشهر، خوزستان و همه کسایی که کنار خلیج فارس و دریای مکران زندگی می‌کنن.
🇮🇷
جنگ و بحرانی که الان کشورمون گرفتارش شده، از نگاه من یه مقصر بیشتر نداره؛ جمهوری اسلامی.
ولی جنگ واقعی، یعنی جنگ جمهوری اسلامی علیه مردم ایران، از 47 سال پیش شروع شده و هنوز هم ادامه داره.
همه مردم ایران یه جورایی از این حکومت آسیب دیدن. نذاریم کسی طوری حرف بزنه که انگار جنوب ایران تازه وارد جنگ شده.
جنوب ایران از همون روزی وارد جنگ شد که بچه‌های بلوچ به خاطر نبود آب آشامیدنی و امکانات اولیه، قربانی گاندوها شدن؛ از همون روزی که جوون‌های سیستان و بلوچستان، سرزمین رستم، مجبور شدن برای یه لقمه نون سوخت‌بری کنن؛ از همون روزی که هرمزگان و بندرعباس، با اینکه بزرگ‌ترین بندر ایرانن، تو فقر و محرومیت رها شدن؛ از همون روزی که بوشهر با اون همه منابع گاز، و خوزستان که قلب صنعت نفت ایرانه، خودشون از ثروتی که تولید می‌کنن سهمی نبردن.
👑
اما ایران آزاد یه کشور کاملاً متفاوت خواهد بود.
با روی کار اومدن یه دولت ملی، کاربلد و توسعه‌محور، سیستان و بلوچستان می‌تونه با تکیه به موقعیت راهبردیش، جوون‌های توانمندش و دسترسی به آب‌های آزاد، به یکی از مهم‌ترین موتورهای رشد و پیشرفت ایران تبدیل بشه.
چابهار هم می‌تونه دوباره به قلب تجارت ایران و دروازه اتصال به اقیانوس هند، آسیای مرکزی و بازارهای جهانی تبدیل بشه؛ با احیای همون برنامه‌ای که قبل از انقلاب 57 قرار بود اجرا بشه.
هرمزگان، بوشهر، خوزستان و جزایر خلیج فارس هم با توسعه تجارت، گردشگری، صنعت و جذب سرمایه‌گذاری، می‌تونن به ثروتمندترین و پیشرفته‌ترین مناطق ایران تبدیل بشن.
✊
هم‌وطنای عزیز،
🇮🇷
این حکومت نه برای مردم پناهگاه درست کرده و نه حتی توان دفاع درست از آسمون کشور رو داره. در حالی که خودشون تو پناهگاه‌های زیرزمینی قایم شدن، از مدرسه‌ها، بیمارستان‌ها و مراکز غیرنظامی استفاده نظامی می‌کنن و مردم ایران، حتی سربازای وظیفه، رو به سپر انسانی تبدیل کردن.
توی جنگی که جمهوری اسلامی به کشور تحمیل کرده، اولین و مهم‌ترین وظیفه شما اینه که مراقب جون، امنیت و سلامت خودتون و خانواده‌هاتون باشید. چون شما سرمایه واقعی ایران و نیروهای اصلی برای پس گرفتن کشور هستید.
دفتر ارتباطات و رسانه من هم به‌زودی توصیه‌ها و راهنمایی‌های لازم رو منتشر می‌کنه تا مردم بتونن امنیت خودشون رو بیشتر حفظ کنن.
آماده بودن و ادامه دادن این مسیر، یه مسئولیت همیشگیه. هرچقدر مردم قوی‌تر باشن و جمهوری اسلامی ضعیف‌تر، رسیدن به پیروزی نهایی سریع‌تر و با هزینه کمتری انجام می‌شه.
👑
پاینده ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68797" target="_blank">📅 14:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68796">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8452e3c7c9.mp4?token=XjzSOHqsdx5QZnRC7WC-F7yXEZR1EPu8DaZycHsRCIGPzeZ9y3gX56sELHjeVKtiVxtN8ajnoCWBX8KpO8TiAwjuYXVVjt8yKf_17zD-1OAtUXnptWmGx4cy4vFnGMOygzeaLOMWtdFT0-P9snuZFSOZt2wOSASk1UivQHP9NJOXcihnM7esNMsofiew9gL4waG4hof-0104ZTUV9hswmBbjeS5bkMDAG25OSzGYgg6KkIX579roPG80BrcOwDkDcsiZy6o4p20WEmNBxrHZYFEErgL4UjOFl9XLFnNth9WksRyduPQRSPJ5N223RnGICq7GJSDHenA_bpyOzkqTFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8452e3c7c9.mp4?token=XjzSOHqsdx5QZnRC7WC-F7yXEZR1EPu8DaZycHsRCIGPzeZ9y3gX56sELHjeVKtiVxtN8ajnoCWBX8KpO8TiAwjuYXVVjt8yKf_17zD-1OAtUXnptWmGx4cy4vFnGMOygzeaLOMWtdFT0-P9snuZFSOZt2wOSASk1UivQHP9NJOXcihnM7esNMsofiew9gL4waG4hof-0104ZTUV9hswmBbjeS5bkMDAG25OSzGYgg6KkIX579roPG80BrcOwDkDcsiZy6o4p20WEmNBxrHZYFEErgL4UjOFl9XLFnNth9WksRyduPQRSPJ5N223RnGICq7GJSDHenA_bpyOzkqTFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تفاهم‌نامه هیچ حقی برای حمله ایران به کشتی‌های تجاری قائل نشده است
.
🎙
خبرنگار:
آیا این تفاهم‌نامه (MoU) ذاتاً دچار اشکال نیست؟ چون در بند ۵، به نوعی به ایران نقش و اختیار در تنگه هرمز را به رسمیت می‌شناسد.
🇺🇸
مارکو روبیو:
فکر نمی‌کنم متن تفاهم‌نامه چنین چیزی را بیان کند. این تفاهم‌نامه به ایران حق نمی‌دهد که پهپاد و موشک به سمت کشتی‌های تجاری شلیک کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68796" target="_blank">📅 14:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68795">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44a650cd04.mp4?token=ausK2CvIEridAOMOnFqDUhx64GEIox5A0CWJVf0ZPYPr_9p9tc0ozk2rbSRgjCQfgzVbwsS3rfILLjm4MsrP68LWKrHEUmaBuaVnP4zQJFMRK-3NxXNGgWIQ5Gcm4LDMlMB3s4rpSiykkX9G7DrNNOW5tBm9wFCuvILZjnd7u54IdPYwTY9aCW8vPnFP4JWr6ghIv8Rvuxjs4hypA8VsItcKhu-wvRTxiX2c-p6fsaK3oMjXgY0IZtCHGqq4-VzfqaWCMms8o8PPMzTkDJpJx00WkrgdsN97UGnIgEDJXSNcAbENqnVa55wSL3nM-6IgXGHiR6DDJvdhsGrGX5Y2og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44a650cd04.mp4?token=ausK2CvIEridAOMOnFqDUhx64GEIox5A0CWJVf0ZPYPr_9p9tc0ozk2rbSRgjCQfgzVbwsS3rfILLjm4MsrP68LWKrHEUmaBuaVnP4zQJFMRK-3NxXNGgWIQ5Gcm4LDMlMB3s4rpSiykkX9G7DrNNOW5tBm9wFCuvILZjnd7u54IdPYwTY9aCW8vPnFP4JWr6ghIv8Rvuxjs4hypA8VsItcKhu-wvRTxiX2c-p6fsaK3oMjXgY0IZtCHGqq4-VzfqaWCMms8o8PPMzTkDJpJx00WkrgdsN97UGnIgEDJXSNcAbENqnVa55wSL3nM-6IgXGHiR6DDJvdhsGrGX5Y2og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مراد ویسی:
دیدم مردم به من گفتن عراقچی رو فالو کردی رفتم توییتر نگاه کنم ، دیدم نه تو توییتر ندارمش و رفتم تو اینستا دیدم اره عراقچی رو فالو دارم که احتمالا دستم خورده بود و انفالو کردم.
مرسی که بهم تذکر دادید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68795" target="_blank">📅 13:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68794">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
فارس:
دقایقی قبل صدای سه انفجار حوالی سیریک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68794" target="_blank">📅 13:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68789">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd690bdc0.mp4?token=PpHR8HqxaApiG6CAKfZFPtgBIRvRLQyFI1nCXH8QJjpGfvK3f6LA83uBzxFGFJcMfujuFeuq4C-dRPp5NJzYavzN5TCcjQsq-abJSWwvtaG8SN_5Gpc2ZXRR3l-QFrDn5eVSffoQsY-oMvMP0DZDFXNxdqAIsbi-QhBVYFmGLvhSedA6i5JzuDYcTfkBpSQk0Vwv7Qy25FCWtFM7JIdrzWhNtW6nP9CUx528OhvLQfHAgaJKAXffqzMJaD2AKakoxyp42HPHiryGFrOyonc_DAZ93BAUlc3jxYn0-FmhpOEa9qv_xOEP-ddiI7qrH5hGXAdfpJlYqFtwed12iW9zZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd690bdc0.mp4?token=PpHR8HqxaApiG6CAKfZFPtgBIRvRLQyFI1nCXH8QJjpGfvK3f6LA83uBzxFGFJcMfujuFeuq4C-dRPp5NJzYavzN5TCcjQsq-abJSWwvtaG8SN_5Gpc2ZXRR3l-QFrDn5eVSffoQsY-oMvMP0DZDFXNxdqAIsbi-QhBVYFmGLvhSedA6i5JzuDYcTfkBpSQk0Vwv7Qy25FCWtFM7JIdrzWhNtW6nP9CUx528OhvLQfHAgaJKAXffqzMJaD2AKakoxyp42HPHiryGFrOyonc_DAZ93BAUlc3jxYn0-FmhpOEa9qv_xOEP-ddiI7qrH5hGXAdfpJlYqFtwed12iW9zZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
🚀
حملات شدید پهبادی اوکراین به روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68789" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68788">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/348d732189.mp4?token=ljBYR4E_Wf2_pPDCKhUFILnAwG9FZexxBo80uB8Coz951ftye85V2DAKmzeKadcUlrupk-0M3JWpRewSnyGIQykMV2IZuPIWcHdnMTZ2FJeoluY8H2Jk2vdUKxqKuL2ppywOwTqjZgLNRFjh4cZqxQRjmcP7jLZanKHoQO1n_8YxRlmodiysgIP6ZCr-GZXYopi49nYNoZRQ41EZ3tLSTcbERVY1qZSi3UF1UjBqLmysvk7oo2U4PnrpnTb6-LMes046bkmde9agbZrZ8_OwJNdngDqz_epp0-DzrVJGHyhPWVAB3YBeX_u8hsAhvXHxgWaAfV6AZXBiYp0dMrFHGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/348d732189.mp4?token=ljBYR4E_Wf2_pPDCKhUFILnAwG9FZexxBo80uB8Coz951ftye85V2DAKmzeKadcUlrupk-0M3JWpRewSnyGIQykMV2IZuPIWcHdnMTZ2FJeoluY8H2Jk2vdUKxqKuL2ppywOwTqjZgLNRFjh4cZqxQRjmcP7jLZanKHoQO1n_8YxRlmodiysgIP6ZCr-GZXYopi49nYNoZRQ41EZ3tLSTcbERVY1qZSi3UF1UjBqLmysvk7oo2U4PnrpnTb6-LMes046bkmde9agbZrZ8_OwJNdngDqz_epp0-DzrVJGHyhPWVAB3YBeX_u8hsAhvXHxgWaAfV6AZXBiYp0dMrFHGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی وزارت کشور :
عباس چرت میگه مشهد سقوط کرده بود، تو دی ماه من خودم مشهد بودم خبری نبود اون شب.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68788" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68787">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
💵
پرداخت آسان و سریع با تمامی روش‌های پرداختی
📣
30% فریبت ورزشی برای واریزهای کریپتوباکس (ارز دیجیتال اتوماتیک)
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68787" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68786">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foOguxidSaJnJUc0nYcUs06H-nS2ugjSlQcgT-BD_vsTT4oJUGl3X3CWxKdl1uRyEteAPXlBjWF7z3Ib8JokcuXg_0qoQSajx4SDnV_CIZXV4pESdPyh9mhB-57NFx503h9-Z4SewSDpGtE_BaDkQ1vLlemD_CMNvKp195bHTiMovWlzM_FOvd_qy2tDtcaERMGW3GgufFJsQIPclpczLM9Rt4uoVKMK7GXYoHyJuLEhKemTv8ICpCpxOluH5p3eRfZ1ShjOc-shNYsNNjLfOdr3wiB6kUJiKU9aRQb1npIoM2ftWtWmBdz4bfNmPCMyn5zmG0nV63oQJQ2ZlSfUxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBET
💎
🇪🇺
لیگ قهرمانان اروپا
⏰
شروع بازی ساعت 20:30
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68786" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68785">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22ed6173e8.mp4?token=VciY0o9hVFGdhhLwnToiYvnWwN2nnsYCywQDkR4r82xLQTZJmE3dQgKAQo0zHL9xgxmnxPEfKd7z-Xvs5faAQzw6lIjstSxYf0ZWARW1XT0xRXppXh89kZlIaLe7EkPRXgo6TINUIywHyDx8ZSQ3L7p91k3ExBTOw6N8Kz4dP2IKhvkbEhDiKPI4Bhgpl3ePKsXCtc1Ew0liVFIRhdUrN3bD4qef-DL8z_kaj8S9XvMStUJIA013dOi3427GAveiJZEw0dT0yr5rB9Mktzaqb2qz9uUkhHPm273OK5N8mIxP26IqxA_2jS7SKOGQ3MjX48jgkdL6fjhiqbhaGgK9aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22ed6173e8.mp4?token=VciY0o9hVFGdhhLwnToiYvnWwN2nnsYCywQDkR4r82xLQTZJmE3dQgKAQo0zHL9xgxmnxPEfKd7z-Xvs5faAQzw6lIjstSxYf0ZWARW1XT0xRXppXh89kZlIaLe7EkPRXgo6TINUIywHyDx8ZSQ3L7p91k3ExBTOw6N8Kz4dP2IKhvkbEhDiKPI4Bhgpl3ePKsXCtc1Ew0liVFIRhdUrN3bD4qef-DL8z_kaj8S9XvMStUJIA013dOi3427GAveiJZEw0dT0yr5rB9Mktzaqb2qz9uUkhHPm273OK5N8mIxP26IqxA_2jS7SKOGQ3MjX48jgkdL6fjhiqbhaGgK9aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
این ویدیو از اینکه نشونه آدم پولدار چیه، اخیرا خیلی وایرال شده!
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68785" target="_blank">📅 12:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68784">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-PayzapjyeOFX2Rc16zqzDo0BloVynEuht0mO-HsalyyaKmngD-HV9wjb_jlNay9VXqXet3Z2xSc8Sx_BTKHyMsIpcS9SG-4XgxW6vh7VzWxvVyWceurNBz-YQYewoWcFOE8377cgyFPoq51xza1CA7-orGFbw4reX2th3CKG3OF7zZlTgb7RO5KtmyoRBZz-CsHMCv63R_qe9BMVCE4aJtD1ZJgKZ7r7eU94BwqtEtQkKd0HtF2xdasxJ0XyH9YiRJ63LTWEW_54Ok-tWC4OdjJuKAMHQJzN613z2sUu1FrKvQ1sanuLQMl3FD4ghXVFBlJEAaeBywEF0_fRmDfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
شلیک موشک از کرمانشاه به سمت پایگاه های آمریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68784" target="_blank">📅 11:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68783">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d576bfeb8.mp4?token=mn3exlZoGFiN8ikTZsptYG_P7o8SM2pjhhxxj-32gq02pIheq-s_OTM1wRTMuXhbXLZNlWTQ-A4dUMiXjODa8jtNvi04At5hMvYejNdkUqS9KMxuUY2_sxo8y-WNDKCB0iUCsxv7bLFgaUQOqNS1TnXhZc4xgGGQtQtXTcexa-dyr_SA9eLdfydXSBPR2cE_mEV5qP5am4OLf3CyGbUrfNUQFo8247IIvbvZE9VKDV5YiWOeNe7-i9BQc0hMXVklva_V3cdnUfxinpMsrBYHliBaD64WH6XbtakamhlKYN-4E2YJiDShf1-q_m1cfL_zyjTUQGbTtKSUvRDXevV1Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d576bfeb8.mp4?token=mn3exlZoGFiN8ikTZsptYG_P7o8SM2pjhhxxj-32gq02pIheq-s_OTM1wRTMuXhbXLZNlWTQ-A4dUMiXjODa8jtNvi04At5hMvYejNdkUqS9KMxuUY2_sxo8y-WNDKCB0iUCsxv7bLFgaUQOqNS1TnXhZc4xgGGQtQtXTcexa-dyr_SA9eLdfydXSBPR2cE_mEV5qP5am4OLf3CyGbUrfNUQFo8247IIvbvZE9VKDV5YiWOeNe7-i9BQc0hMXVklva_V3cdnUfxinpMsrBYHliBaD64WH6XbtakamhlKYN-4E2YJiDShf1-q_m1cfL_zyjTUQGbTtKSUvRDXevV1Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
‌علی‌اکبر رائفی‌پور، ازحامیان جمهوری اسلامی:
با شناختی که از سپاه دارم اگر نظام سقوط کند، سپاه پاسداران موشک‌های خود را بر سر شهرهایی خالی خواهد کرد که به کنترل طرف مقابل درآمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68783" target="_blank">📅 11:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68782">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c11f67944.mp4?token=AcAZQjDaMrb2ynCKOkP1swfaOooZN35Z-eGfO2_oMO_D3QwjTIxKPEn5nN7hcknuoqPRLK603PESU5OfI2vRUmYapRp8t-mO0RM6elDFF5TIattrvoNNoS7qCvOFLmQd4hrK_qpZH9xr3T1H53oyYfrTLZlNbuzVcVotiDHPc0hGzYqUd427EcrqaU3Mc3BXMFQWWaa5nAgxUnKFqWDp9CXR1eKyMEmhr0s0KMaxDXQhtcNhCfpgTDYmJ3DsPk-02gCMejuXbaMbuqNqFpW3_MQ7P2boyyDShmj7h0p6PZg__kwUbW-z4iKzTnsZpXwrwlYCpz4s4UsmCrd6ltXJ1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c11f67944.mp4?token=AcAZQjDaMrb2ynCKOkP1swfaOooZN35Z-eGfO2_oMO_D3QwjTIxKPEn5nN7hcknuoqPRLK603PESU5OfI2vRUmYapRp8t-mO0RM6elDFF5TIattrvoNNoS7qCvOFLmQd4hrK_qpZH9xr3T1H53oyYfrTLZlNbuzVcVotiDHPc0hGzYqUd427EcrqaU3Mc3BXMFQWWaa5nAgxUnKFqWDp9CXR1eKyMEmhr0s0KMaxDXQhtcNhCfpgTDYmJ3DsPk-02gCMejuXbaMbuqNqFpW3_MQ7P2boyyDShmj7h0p6PZg__kwUbW-z4iKzTnsZpXwrwlYCpz4s4UsmCrd6ltXJ1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
⭕️
گفته میشه دیشب با وجود اینکه پدافندا توی تهران خیلی فعال بودن اما انفجاری گزارش نشده.
احتمالا دیشب بیشتر پهپادهای شناسایی آمریکا، مثل MQ-1C Gray Eagle و... تو آسمون تهران بودن و پدافندا هم سعی می‌کردن اونا رو بزنن.
احتمالاً مأموریت اصلی این پهپادا دیشب شناسایی بعضی مکان‌ها، مراکز نظامی، محل استقرار پدافندا، و... بوده و ممکنه که آمریکا درحال آماده کردن خودش برای دور جدیدی از جنگ باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68782" target="_blank">📅 10:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68781">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e535968cb3.mp4?token=Fj5Tah-BYQPh2_lOfB8TN5sf4UbJUSazIgsHBEG0eVaQ32cBK6zt5fOlRDM9BXvM3cW1ny1rifNmiCIv7MnEWqJC3eOR7X4Hq9rAYXY_It8V1iTPBmc9zyXgWOG8nVa1oui8xn7uo_VKMURlmBvVrLsb6v3bcfcYbEJe1rwboPcUWDo0mRRvhY_PyjqjWocQAL3be09ZjhNUi2TDqziSFuuSoee2FkJln1RXT3-RjtoegIO0e3aaFN8Cdq4a9F0QgTrWq9HJqekV5sV5CK6fxcZi7PLradl3yXDSOTYKmrKg6S2CIeS6hbY3R3uOtzXLRFMkk7PIcpmpah1Fne6NJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e535968cb3.mp4?token=Fj5Tah-BYQPh2_lOfB8TN5sf4UbJUSazIgsHBEG0eVaQ32cBK6zt5fOlRDM9BXvM3cW1ny1rifNmiCIv7MnEWqJC3eOR7X4Hq9rAYXY_It8V1iTPBmc9zyXgWOG8nVa1oui8xn7uo_VKMURlmBvVrLsb6v3bcfcYbEJe1rwboPcUWDo0mRRvhY_PyjqjWocQAL3be09ZjhNUi2TDqziSFuuSoee2FkJln1RXT3-RjtoegIO0e3aaFN8Cdq4a9F0QgTrWq9HJqekV5sV5CK6fxcZi7PLradl3yXDSOTYKmrKg6S2CIeS6hbY3R3uOtzXLRFMkk7PIcpmpah1Fne6NJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی دو روز قبل یه گونی آدم از مجری‌های صداوسیما ، اعضای پایداری و بعضی ورزشکارها در واکنش به کارزاری که راه افتاده بود، پا شدن رفتن جنوب که بگن ما از جنگ ترسی نداریم و این حرف‌ها؛
حالا کجا رفته باشن خوبه؟
بهمنشیر که تو نزدیکی کویته و 14 ساعت [1125 کیلومتر] با بندرعباس فاصله داره
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68781" target="_blank">📅 10:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68780">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/822c8aa150.mp4?token=sZpnil2hxjXMfouc5tH8JSrFZTXFENZluLNmGpEppogjtdvu3lPEhOkKltFYx4QEFlIY-28Z2k_9QC4xp_1y1pB2aEHnb1BKg-TI7clws3xTCwG2bYzTqFV5SNPrQtL9O5b6NFt8Rtdg_8gLRvFugzngPaRRI2vfrbrZyIRdGpTWoCuKzhZwzkn_Je_2CIlN0T4_qxSnF0S_e15CuCJ3FCWEBlGGvM1XDQo7T-jr1gCeMwNcPbLS7jxL7Ys5NGlQcmri7ygsKm9h7D2PlrdZPBuGDAm2pfhJuYnuceWZl7wuzvgoGu1hmYWJ2f7ISGn33c-4S53vJ2nCF_aIMMlIqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/822c8aa150.mp4?token=sZpnil2hxjXMfouc5tH8JSrFZTXFENZluLNmGpEppogjtdvu3lPEhOkKltFYx4QEFlIY-28Z2k_9QC4xp_1y1pB2aEHnb1BKg-TI7clws3xTCwG2bYzTqFV5SNPrQtL9O5b6NFt8Rtdg_8gLRvFugzngPaRRI2vfrbrZyIRdGpTWoCuKzhZwzkn_Je_2CIlN0T4_qxSnF0S_e15CuCJ3FCWEBlGGvM1XDQo7T-jr1gCeMwNcPbLS7jxL7Ys5NGlQcmri7ygsKm9h7D2PlrdZPBuGDAm2pfhJuYnuceWZl7wuzvgoGu1hmYWJ2f7ISGn33c-4S53vJ2nCF_aIMMlIqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
لحظه‌ای که عادل فردوسی‌پور تو لایو فوتبال 360 بغض و گریه کرد...
اپلیکیشن‌ و سایت فوتبال 360 به علت اینکه عادل و مهمون‌هاش از تیم ملی انتقاد کرده بودن، به درخواست قلعه نویی و باندش فیلتر و از دسترس خارج شده و مجبور شدن برنامه رو تو لایو اینستاگرام و یوتیوب اجرا کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68780" target="_blank">📅 10:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68779">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087e2855d3.mp4?token=PDeyl9WZrD5KR1TLb-urdG9sE4r_Vwhzln8EtPYN_84HejSb8BMOtmQRS_JfIL0Cz0J2kuVGYgwxW9fBjCHAYUjWwiZWgBRNp9JNyBWdbm8PDDfXHS6zezo3Mt4_LH6Hmy-ZMJoVmzrUwF7jcvW5-EE-P6YroUEWGZf5cCtDbaYK9WVMbJJSQFMe1YIKcLmE_5Ssve1Dh0Hq6QTge4719gFLnC9GV1b6tSSuLZEwqtHLCky7urpxbOK9GTWK2B-16twTZ3NEHCOXFArFAwg4TGRY-YlbQwg9DiuI1kFYqD0OFpHJZp37uesjLB7HUQk0Gr-HLa6PrqMOY7Bsh4q8Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087e2855d3.mp4?token=PDeyl9WZrD5KR1TLb-urdG9sE4r_Vwhzln8EtPYN_84HejSb8BMOtmQRS_JfIL0Cz0J2kuVGYgwxW9fBjCHAYUjWwiZWgBRNp9JNyBWdbm8PDDfXHS6zezo3Mt4_LH6Hmy-ZMJoVmzrUwF7jcvW5-EE-P6YroUEWGZf5cCtDbaYK9WVMbJJSQFMe1YIKcLmE_5Ssve1Dh0Hq6QTge4719gFLnC9GV1b6tSSuLZEwqtHLCky7urpxbOK9GTWK2B-16twTZ3NEHCOXFArFAwg4TGRY-YlbQwg9DiuI1kFYqD0OFpHJZp37uesjLB7HUQk0Gr-HLa6PrqMOY7Bsh4q8Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
نظر مارکو روبیو درباره برجام (سپتامبر 2015)
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68779" target="_blank">📅 09:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68778">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
سنتکام: حملات امشب به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68778" target="_blank">📅 04:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68777">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68777" target="_blank">📅 03:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68775">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c46837f26.mp4?token=D9JV_RLjCvT1xazHKSFQqNmz3v4TmRp4shPu9kEVzIvv0m3r1p8HHqoocuHa5YQEt9Q9am_TfDPQjVq7nzlNYWH6zEk1bxqo4Ee_6jz5X2TfLV0tIjOm0tq5rZwedD7W_l77Dc1pq4vDe9C-hLvEQhJjvWqKkatqgyImT_z4nycC6fWxN2FJDtaKkjFvhTtnuIlBQFk3qrTl8xeXGPfdCuyY9WHTW1ikdItalpUSz39N5A8CYhOSj4zb7MBtUPcnNOIksaBcQmq6V7ZX-kzKsWdiOj6asOSWB64yQ2t_kw-LxfJw9mGoc-1n9y25LoPUOoY3toopiU3XI1Sq4N_deQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c46837f26.mp4?token=D9JV_RLjCvT1xazHKSFQqNmz3v4TmRp4shPu9kEVzIvv0m3r1p8HHqoocuHa5YQEt9Q9am_TfDPQjVq7nzlNYWH6zEk1bxqo4Ee_6jz5X2TfLV0tIjOm0tq5rZwedD7W_l77Dc1pq4vDe9C-hLvEQhJjvWqKkatqgyImT_z4nycC6fWxN2FJDtaKkjFvhTtnuIlBQFk3qrTl8xeXGPfdCuyY9WHTW1ikdItalpUSz39N5A8CYhOSj4zb7MBtUPcnNOIksaBcQmq6V7ZX-kzKsWdiOj6asOSWB64yQ2t_kw-LxfJw9mGoc-1n9y25LoPUOoY3toopiU3XI1Sq4N_deQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/68775" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68774">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
❌
🌐
امشب ریزپرنده ها در تهران فعالیت داشتند، احتمال اختلالِ بیشتر در اینترنت وجود داره؛ پروکسی های پرسرعت زیر رو داشته باشید
https://t.me/proxy?server=nab.goooalir.co.uk&port=8443&secret=dd104462821249bd7ac519130220c25d09</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68774" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68773">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در زنجان!
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68773" target="_blank">📅 03:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68772">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DE1x9GER7mmu2IpTEOaeHWfnNWOCfqo4G8RrGbl7PCnP0uV7FS9Aos5Ho7CbbmnjI3ulXpxiPe24-lgbsbeHF_M1tg2KM3W4Xf8j5EsLSBFlYUR5Qs862TENVjlRsqOSDcsTxPS6n5nFst9ZcFalBN6IVNFAY0GttGGmuM4eY4D0t16hrXghvPr_J9dFBo27oFkhb_SHtArOQIv3FKUbJAScB5wY6FODVfJG3vafAR4aqM8h4F41Tpz0V6emOv4AMcJ3HJafcvGzvnExFQbxruENcXq0moYzZJFOIQwec1l-9-JqvAivDVWpAPaCoz1HXACkYTM9ulvRRMTxF7ayMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جالبه هنوزم سنتکام چیزی نگفته!!! #hjAly‌</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68772" target="_blank">📅 03:07 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
