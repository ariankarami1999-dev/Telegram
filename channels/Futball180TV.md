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
<img src="https://cdn5.telesco.pe/file/u27T9V7IaRsiPBUvXS96LN-zjhow6FxtK0YToFOB7ecvSRivQpKuilZMyYH3kmczdXmIaoXm3DeLPho1L7LOMhimYGAIAOyuAQADQvA4yTdN14pipRYbXLPwiuqIsFcglK3nI6nGKsUFbqpRoYrXS9SwireRiXO_6Rh5NNyugSq95E3oSmr0HDZ6xTdLzQRi-ypcvPP8967hn-nNoaO-SonX5AAerUV48TfkfT-xEygyK0LN5-yRtRrXNwM4SByULmb91k3NxTQ4n_hjOaFk54sDMecpXa_yvjtlnuhRiBnK2BH4_JyIaNg2wNH-WufhhajrG6DxHxc2kMoILBHgWA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 413K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 15:26:15</div>
<hr>

<div class="tg-post" id="msg-106568">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec515fb788.mp4?token=LioFSCRauiysqYvcyTyVd5raOH0CZySXM0VALhRFZEbIUL1Hq4k9U1B_aRa5dEJzPg_5UswCazcw1r8MCTSOKsjM9UEBvunkOTIwR4HZ5OwGp8JndHebnYmI3FcqeNCJ78ogiwFpbGy_HSKqK-eyrMtE_njZqO7KsssE7hVy-I1n0qiew24PoW32L9AM0wUjZ6YFmjz5Heh_CDrfOuYiE09QT8vpymKmbshM45gCBfPSO9tDRuK4dPVUBIcXhiIX7YzBdGc1E5sF5SPYPZWva3JBlKUDttj0aYaJxzTbGYdr1F155kFvAz5Cmp1vC1chYH3lxK4ukNbx7YP8qJOQhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec515fb788.mp4?token=LioFSCRauiysqYvcyTyVd5raOH0CZySXM0VALhRFZEbIUL1Hq4k9U1B_aRa5dEJzPg_5UswCazcw1r8MCTSOKsjM9UEBvunkOTIwR4HZ5OwGp8JndHebnYmI3FcqeNCJ78ogiwFpbGy_HSKqK-eyrMtE_njZqO7KsssE7hVy-I1n0qiew24PoW32L9AM0wUjZ6YFmjz5Heh_CDrfOuYiE09QT8vpymKmbshM45gCBfPSO9tDRuK4dPVUBIcXhiIX7YzBdGc1E5sF5SPYPZWva3JBlKUDttj0aYaJxzTbGYdr1F155kFvAz5Cmp1vC1chYH3lxK4ukNbx7YP8qJOQhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
حمله تند مصطفی هاشمی‌طبا رئیس اسبق فدراسیون فوتبال به علیرضا فغانی عزیز!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/Futball180TV/106568" target="_blank">📅 15:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106567">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64d6b37a2c.mp4?token=bO6-Es7wbmqINC8srGpTmG-wK5uDmdQlLKQPXQMpBpbBssicHiR_f5SRij2NvWlZDhXZX_ECZF_WXqWejS4TFGxz7bjnNLftJLpcrU-bMD3zAqReVlJl7h8cnj5iGPRKtfZEeONlbcry6BpJqZ0DRv5YV5K4HmvgYXdh8nqli45_81FfSHHl3AlLRTCc11zYBjwh_KaCkoWyjSZ-E5_kcTAmv2NRrmQ1OZpKNqpqvlHlUi5nmruvRSpKUjQy-Jw96YB2CPzv0wK3Sm4jl9K3DsmuMA0Xz9Rp4ORK-1Cn6UkIw36nClxJgqifGHHZa9kewKJ4UXtxhXtfyh9c-KEpyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64d6b37a2c.mp4?token=bO6-Es7wbmqINC8srGpTmG-wK5uDmdQlLKQPXQMpBpbBssicHiR_f5SRij2NvWlZDhXZX_ECZF_WXqWejS4TFGxz7bjnNLftJLpcrU-bMD3zAqReVlJl7h8cnj5iGPRKtfZEeONlbcry6BpJqZ0DRv5YV5K4HmvgYXdh8nqli45_81FfSHHl3AlLRTCc11zYBjwh_KaCkoWyjSZ-E5_kcTAmv2NRrmQ1OZpKNqpqvlHlUi5nmruvRSpKUjQy-Jw96YB2CPzv0wK3Sm4jl9K3DsmuMA0Xz9Rp4ORK-1Cn6UkIw36nClxJgqifGHHZa9kewKJ4UXtxhXtfyh9c-KEpyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
کل کل خبرنگاران استقلالی و پرسپولیسی در نشست خبری امروز سخنگوی دولت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/Futball180TV/106567" target="_blank">📅 14:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106566">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdGcMHYoGfPNCB8R_36ShF94sg7zivmrT4pL0iLj6SCRAakqMHeCgg98CRr6C1ovdL-IBLwShNgg9r214_ZR1Azs9Vz6en-NchGSE2i7SA-cgd-6OP1E_Rng1jK4bcn2AduPQHtVORISGPe2_k7ss9Um0ToGrdgt7LpEBY0GS9IbxN4Yn0t8UQaOGz8JqxzV0RM_tmL1Qkmh77VJk0wDscXN9zb0AqUUmANJPkAAp8S7wVzUDw7klntvlDU32fTtQWMypG0ZjCuVkEF0uogvPy4UsP3VYZaSeIVfJMzUzSnhEtMkYtjbZR5xilS_5OoMbVr6L3EThflK7hyQDGDq0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🇪🇸
هانسی‌فلیک: مطمئن‌باشید تا سه سال دیگر حتما حداقل یک‌بار قهرمان اروپا خواهیم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/Futball180TV/106566" target="_blank">📅 14:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106565">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaKmMNiMmNJDQg-lzBjUnwz5H03k2SId5LPegueRHpXM5tacc0qbvL0xier2x81sqNrOwuc9bK0-7JBfYTQK4OABq_indNK9rgqQkr9vWzFLVGNY_SSTS7XHo7re5bzGgnqgX-9jYpQg8RQWQMvUwwzz0heiDWnMszwOvgTOXVKgCbNaIA26XV3yno_DRmzd-m4jq-XGkuasFbHUIi-pQO_PpUkBjQjyIiEomqqCo9gjCeyjqPcfxrXXkuHr7xo9RlBQubM9DzhJHV5PZVIjs6od91ADeD886OlciPuFesRoajubxIEv1EqMowR6blM0D8kWBqqXUz7jG9dsOX--yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
اظهار نظر عجیب و معرکه از پیمان حدادی مدیرعامل پرسپولیس: چرا استقلال سه بازیکن تیم خود را به اردوی امید نفرستاد که امشب دو نفر از آنها گلزنی کنند؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/Futball180TV/106565" target="_blank">📅 14:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106564">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Py4SojlfAfQfV-Mc5R2AppQIiYDC_cdv8YnnLsjOiVb3I9h60WO3tCuMz9O7A4hqS2Jfqg8awD9AcGw0zNGHsyYPDoRIlxBlVxgjR_jACGgF-qDCjpuzeRRUCjaSMR4oCfQ9O3C7J6EPYtB-QSZ-c7iEP6NwXqvT68AB0Ldq9s0qzu4xf6D3UzcuQpq5ThcVXaeETK7hasNpsagpcp0hsw41fIBKICPy1PkQEwwJYxWTHHCdBYP_8v4uKeluFD6l_ns2szYi6lgyRlx4u80TU9i2tPqi8OiLvDS6OBXB7awHiVbd82yNeoAhx7QxH_bJRqTp-Mi8SYnRR6f02P6rKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
تا ساعاتی دیگر میزبان فینال لیگ قهرمانان اروپا در سال ۲۰۲۹ اعلام خواهد شد. نیوکمپ گزینه اصلی میزبانی از این فیناله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/Futball180TV/106564" target="_blank">📅 14:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106563">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed1f3faef6.mp4?token=oguduUb27TBSaK7t5-ljZFn2FnG4fBjmS9bv8Gi8q2OSGy0KBhXKeIzAGVBqrtmi01otlTlYZRNjEnx4mpxRptnx3cB9NqqS5VPSE8ORvQrGEPRlodPabLL0x3rBpPHRoyUkIfK1IoK1mZW1Uq3w_Ar21V-_bHRFMLd6_MUEAaCmfNhK_TcPIFp-zueqCCyDtQYTUdJvVaeKZhM5K47zBX7zyxf-fF8dZwizJUIrRwzW1cTbxKMC1bF61_YiRlBKcVRqSL15-4R8yfHxztgQ3pgh7maGVC5MiGuMfXsycVRYDTFHWsDFv57f5idHjSTxo55FtrbJHlhItdVdI9RHTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed1f3faef6.mp4?token=oguduUb27TBSaK7t5-ljZFn2FnG4fBjmS9bv8Gi8q2OSGy0KBhXKeIzAGVBqrtmi01otlTlYZRNjEnx4mpxRptnx3cB9NqqS5VPSE8ORvQrGEPRlodPabLL0x3rBpPHRoyUkIfK1IoK1mZW1Uq3w_Ar21V-_bHRFMLd6_MUEAaCmfNhK_TcPIFp-zueqCCyDtQYTUdJvVaeKZhM5K47zBX7zyxf-fF8dZwizJUIrRwzW1cTbxKMC1bF61_YiRlBKcVRqSL15-4R8yfHxztgQ3pgh7maGVC5MiGuMfXsycVRYDTFHWsDFv57f5idHjSTxo55FtrbJHlhItdVdI9RHTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
حمله تند و‌ عجیب یک آخوند در صداوسیما به صحبت‌های لاله‌مرزبان در حمایت از مردم مظلوم ایران در جشنواره ونیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/106563" target="_blank">📅 14:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106562">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589bf63655.mp4?token=bf96zCcLWUT-r3tsWz5eEGqZTSKFcoGHlQfOztJC1HnBUmfQcjQq69tKbTAOaIv5xX1RnhPAEJjfFtJWynQYkPOHdtwLOqQCVzuVgmjnjvzFM9NUO3AHANrqqwMcwi1e91KdBsNJawY4jtm1VScXjiKHWwr03Qair3ixllqY4t-Jl-pk4u_Y71atOx6zayPlG1Ps_1PDHqz1wQbXkwoYSEcllQ6iEGX4zIOgIcnxsgR3g00mPv_F6acJkEu5ho4KOT0Y1m_uWaohrW3UQ6AGbocxhM8BZyZGOjYb7aMiUVXFy3Xhn2lojrD79H3u5AQF8GP9PL5qzeYqzr1vxaudPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589bf63655.mp4?token=bf96zCcLWUT-r3tsWz5eEGqZTSKFcoGHlQfOztJC1HnBUmfQcjQq69tKbTAOaIv5xX1RnhPAEJjfFtJWynQYkPOHdtwLOqQCVzuVgmjnjvzFM9NUO3AHANrqqwMcwi1e91KdBsNJawY4jtm1VScXjiKHWwr03Qair3ixllqY4t-Jl-pk4u_Y71atOx6zayPlG1Ps_1PDHqz1wQbXkwoYSEcllQ6iEGX4zIOgIcnxsgR3g00mPv_F6acJkEu5ho4KOT0Y1m_uWaohrW3UQ6AGbocxhM8BZyZGOjYb7aMiUVXFy3Xhn2lojrD79H3u5AQF8GP9PL5qzeYqzr1vxaudPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
🎙
رضا شاهرودی بازیکن سابق پرسپولیس: نعیمه نظام‌دوست گفت هروقت احمدرضا اومد پیشت، بهم زنگ بزنید تا بیام چون خیلی دوسش دارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/106562" target="_blank">📅 13:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106561">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a994c05864.mp4?token=VEfIWbwSq7iiwgdfxA1vG1ZvkXGu6LYEt6_Q7Uqfh_JNYRGWlDFLlz1ok_Ylqt8VNxnHRr70-qOpU5X7b_YXsSM9HVwYUEXanEblL-f_TIZq8icOLZ8E923yzI_vBU0E5v2Evw2ShgvGBqZpdQueQFESNVSx8eyEkMcRbfn3WVS9foEIuqy5LsbvylfyvHPLepdivyStwroBV9IoYU6xOB4BLErK6STnWr5MUrB58zSta0CSU2o-jkbGaT-kjBefwAmPKmpFDsaUpYhnMd6N-5JpiEW1_ZkJbBr15a8e1jGuTHww-vgszKuYrI4aRzzrh4B82fDdolRvwc8yJsV7Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a994c05864.mp4?token=VEfIWbwSq7iiwgdfxA1vG1ZvkXGu6LYEt6_Q7Uqfh_JNYRGWlDFLlz1ok_Ylqt8VNxnHRr70-qOpU5X7b_YXsSM9HVwYUEXanEblL-f_TIZq8icOLZ8E923yzI_vBU0E5v2Evw2ShgvGBqZpdQueQFESNVSx8eyEkMcRbfn3WVS9foEIuqy5LsbvylfyvHPLepdivyStwroBV9IoYU6xOB4BLErK6STnWr5MUrB58zSta0CSU2o-jkbGaT-kjBefwAmPKmpFDsaUpYhnMd6N-5JpiEW1_ZkJbBr15a8e1jGuTHww-vgszKuYrI4aRzzrh4B82fDdolRvwc8yJsV7Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇮🇷
🇶🇦
توصیه جالب صالح حردانی به نیمکت استقلال بعد از درگیری با بازیکنان السد برای سنگین کردن جو علیه حریف قطری: همه بریزید داخل زمین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/106561" target="_blank">📅 13:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106560">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fe5inIDUH4ofwJSMZzGbTqsT2DFZjJZSgWQILLPkbY7FKyN0fTRuZ6xyrCxkJgddhYp73d-ZPItul2xqtTdgAw6dsJHiQ1vkrsR16dlxvWPxf25gD23ddxoiIFdAowSBl6NyFzTQOkJX66r0TYQsDSkIDLGy23uPFSNGmYbs5maHdXLz5IxLbQpSe293zf2niADrBgqUItrUvbyxeEDWlzq8dAiwKYgrBscoSAHjluBa-lBYXnlRbtWaYrSfPMyJRvAc_ECUOCjT7VAw-t4adVDWkMgurXAuKOv8qYGYcwa2pEPXmScmHF61souTrPTBUeSaTmEmOcnrUWNWDZL_uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🇪🇸
آنتونی گوردون:
من با این باور اومدم بارسلونا که می‌تونیم تمام بازی‌ها رو ببریم، ولی خودمم فکر نمی‌کردم قرار باشه همه بازی‌ها رو با ۵ گل ببریم. ​الان واقعاً هیچ‌کس نمی‌تونه جلوی گل زدن ما رو بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/106560" target="_blank">📅 12:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106559">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKK9rM40etGjIc6rEzheY5gFFn4wOZodRalIM_bxgJ1KUdqphetTWMuwjr_9Sgt1phXb5fbiKBs_XCptuYctjgMzB3wRJOmjKjrVUhXYm5HPVJbnIFUUeoqHIN194x7CFvsiMeRUxDYE7DLKzuTAlEY0xrpi8nHcvTVcbGdMFt-xPOTDMaVbijPgrHCDzkwnpR3j6FA_7bTmOTXbPs88ssMjGD-u6ECx9qTki7Zyc2HJvl79efguzjbz5rPDJn8VDaExoDBpvHvgvr2XVJgFYRzF0HGq-9NOiF8SGiQ0X03SLNKvysN4ds3drlH-CNShIlAZ5eErBTuSqyFr3k37UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
برنامه‌مرحله گروهی گل‌گهر در لیگ‌قهرمانان آسیا ۲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/106559" target="_blank">📅 12:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106558">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106558" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/106558" target="_blank">📅 12:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106557">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhC-_JCzCX7lQT8wKDxEE7i4uf1zxTXcBk51vUCNRxTh-6fq6FmReV5FihbaXTLBepauR2JfTQj1JGZl4joyGMOjlHh-AB2S8X8vx4N-ZXKJPgHYHrhQ91gXr57K0d54TEVsoAK6POmX8QdAxGtzJLSl_1yTtydKi9hYZtSgwSqM7um1n1kn7VEYPdIu1UepL3PqI4tFINYOUKYACZSx3T-bdKvcMXfd89Dgve3T-UilZifemZ7WqedMDd29RB0WaR6Wi7CACA96OC40Adm3-JES5aAmHbMOCCa5RTiPPJQeoYHjuBJodSUMzWJc4N6T14Nca8agIbfBLJ76bpQWlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
رئال مادرید
🆚
الچه
⚽️
را در TrexBet پیش‌بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
رئال مادرید: ۴ برد، ۱ شکست و ۱۴ گل زده
⚽️
الچه: ۲ تساوی، ۳ شکست و ۶ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/106557" target="_blank">📅 12:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106556">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/851e159f48.mp4?token=S5t00ue30oOqbbG4FqA9enQALW40OQoOiLZNrEY_ToQhF-aqpaiQ-qTtbiIYusxFaA3pButrQnqh7oU32_ZHToz1kGlbYghLyKyn2lzcP0Zv3cSHXcdABb9Jry5pKwh-0zrHGEiu8J0sfBb45EOnxVzLwW4BDQsJerU49cSvVgGCOJOxYyZ-jk-5HHV0zkrYWcLf39J6Sm4FzYrI3qvPmeEeZHGJMTIlSdZu8XXpl75WqINs5vFPz-sDbpT75fS5rymUUepMntW-HdPmJAWVVnoQLkkiWHhw-Pw3aJA8IDoovM6ki3EcTytH3sJ-qRfRsoqBe2QRU9VoJ0n8E3-yRjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/851e159f48.mp4?token=S5t00ue30oOqbbG4FqA9enQALW40OQoOiLZNrEY_ToQhF-aqpaiQ-qTtbiIYusxFaA3pButrQnqh7oU32_ZHToz1kGlbYghLyKyn2lzcP0Zv3cSHXcdABb9Jry5pKwh-0zrHGEiu8J0sfBb45EOnxVzLwW4BDQsJerU49cSvVgGCOJOxYyZ-jk-5HHV0zkrYWcLf39J6Sm4FzYrI3qvPmeEeZHGJMTIlSdZu8XXpl75WqINs5vFPz-sDbpT75fS5rymUUepMntW-HdPmJAWVVnoQLkkiWHhw-Pw3aJA8IDoovM6ki3EcTytH3sJ-qRfRsoqBe2QRU9VoJ0n8E3-yRjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حواشی فوق‌العاده زشت لیگ‌نوجوانان گیلان و کتک‌زدن داور مسابقه مقابل چشم دخترش!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/106556" target="_blank">📅 12:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106555">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
‼️
🇮🇷
ادعای رسانه‌های عراقی: استانداری بصره تمامی هزینه‌های مربوط به میزبانی استقلال در بازی دیشب مقابل السد را پرداخت کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/106555" target="_blank">📅 12:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106554">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1348b5a435.mp4?token=kDQz0b1jVZ4a85pVT4HguQmhdH_M1E9MGByp-h68iO4Uz2GL5KEnvmxAuCcftE6-SgkZVsrNNTeaLJOff8BsQj4LeSDeUqesmdM0Yc11_9kNMC1jIVPlFxrutWnP1cfx_pf1epf6ohQtGl89MKolC5dOArQNDphY80pz6rS2rr_TaaHetitJWPvI1VrP9rMEZFp6CeEbemQXgB9JLUSlV56Anra89C50KggyVGuytd_yreS_OfbLC-rhlvIVG_yEER4hgwyA2n3RY3l-Zt9AjEH81gsFpsL0QdE9VqFLyGMN8SmD8zQiZsnPXqrK3ThKLVanx2meij9M-T-odHa-jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1348b5a435.mp4?token=kDQz0b1jVZ4a85pVT4HguQmhdH_M1E9MGByp-h68iO4Uz2GL5KEnvmxAuCcftE6-SgkZVsrNNTeaLJOff8BsQj4LeSDeUqesmdM0Yc11_9kNMC1jIVPlFxrutWnP1cfx_pf1epf6ohQtGl89MKolC5dOArQNDphY80pz6rS2rr_TaaHetitJWPvI1VrP9rMEZFp6CeEbemQXgB9JLUSlV56Anra89C50KggyVGuytd_yreS_OfbLC-rhlvIVG_yEER4hgwyA2n3RY3l-Zt9AjEH81gsFpsL0QdE9VqFLyGMN8SmD8zQiZsnPXqrK3ThKLVanx2meij9M-T-odHa-jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیرقلعه‌نویی سرمربی فداکار تیم‌ملی تا پایان جام ملت‌های آسیا ماهانه ۱۵ میلیارد دستمزد می‌گیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106554" target="_blank">📅 11:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106553">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVDT5X4KDn3GYFTFquZFPGzWVC7voiastGlgjrLHtj-r_vbeRDfVttrVg2NII5EI_QT3ry-98jAndPISqPCoZXU7BS0e58XtXdjZzYpgoMkaLEaEl4iYZeSMmO8IGQPm-BnnlTdbBDrgorq3yfnxSbZw9fr8x-w-xjz3rEGP2AhDV8EGxiDfCjDAnWAtPbFkih2o_wV77sxik0eoe4KgKp59Dp-_PTf9l2bHPHcv-FrA_jhqehNvcvWt6lca-dCiXyBOOQqzS7tFVBccGODYmMqGlWWsu6WkLgxhgSHse8ZFNjck6Um-UvinZW2S5ePucfECL64xpZmk9dS_REm7xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
‼️
مقایسه آمار چهار مدعی اصلی توپ‌طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106553" target="_blank">📅 11:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106552">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d711d850a.mp4?token=KZPAjU39U5lrW1HqTsrNOS-93UHx57myrKSlh3MGD4OI3gNuS6XacEv7Jfoam-7J4-aHhr4XLrDSqDlOxaWy9XeaDo9uRk3CrMNQl-BZsXjYvag49vUgh2URIUhNVjG87T-U59WjAQ2lAqAlYxrJUDvmO14GtcooFdE3feQKg_JN3jdrgQ9ufQims19MZtjlsTXvGlYO6wr1GSE0ojqn_mHKo-N293WFG0NiZ5WcISZWA4kvhpVfNktOe4PtG5yaQo3r0N6XC1Lfso3u3mzMrzQSSSuRrdzJ0m-XzP_VzqP_EP-59Ena-tsHs32BQFWmP3CZiHyCWbcWHFErCd6I8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d711d850a.mp4?token=KZPAjU39U5lrW1HqTsrNOS-93UHx57myrKSlh3MGD4OI3gNuS6XacEv7Jfoam-7J4-aHhr4XLrDSqDlOxaWy9XeaDo9uRk3CrMNQl-BZsXjYvag49vUgh2URIUhNVjG87T-U59WjAQ2lAqAlYxrJUDvmO14GtcooFdE3feQKg_JN3jdrgQ9ufQims19MZtjlsTXvGlYO6wr1GSE0ojqn_mHKo-N293WFG0NiZ5WcISZWA4kvhpVfNktOe4PtG5yaQo3r0N6XC1Lfso3u3mzMrzQSSSuRrdzJ0m-XzP_VzqP_EP-59Ena-tsHs32BQFWmP3CZiHyCWbcWHFErCd6I8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
سکانس جنجالی مرد سه‌هزارچهره در کنایه به فساد بی اندازه مسئولین مملکت جمهوری اسلامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106552" target="_blank">📅 11:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106551">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46287e0aa8.mp4?token=CZ1nlAJUnKLoiohYy9NE-9aCMPo7IpEI73fqYp6FAPFypXlBE6S8dH75ksFpD-Jr3JFTU-14IXanNGEP2MtDWzXIfM2yawZq-3EcXFzNZmAKgdIBHqmi9ZmF1_dINgzSf7sZQPBQIGcoyTp5EY1CuGSAAZa8heZHdcbyrq7mAaaZrVTlxfvvmKfCJCJI5AVpkjfGtMljR29OQfw9PVslWXYGnMYA2p4OoDILIH88t-QZgpN46fyg2PlDQHZC3njAJSBx2LXroGzLl5czw4_rJZFKwjVQFgwSYKjfHnpVgTysQ08CTgxjYzpvhzBQzLZWUqdQYtKxhILz97IwNgsEWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46287e0aa8.mp4?token=CZ1nlAJUnKLoiohYy9NE-9aCMPo7IpEI73fqYp6FAPFypXlBE6S8dH75ksFpD-Jr3JFTU-14IXanNGEP2MtDWzXIfM2yawZq-3EcXFzNZmAKgdIBHqmi9ZmF1_dINgzSf7sZQPBQIGcoyTp5EY1CuGSAAZa8heZHdcbyrq7mAaaZrVTlxfvvmKfCJCJI5AVpkjfGtMljR29OQfw9PVslWXYGnMYA2p4OoDILIH88t-QZgpN46fyg2PlDQHZC3njAJSBx2LXroGzLl5czw4_rJZFKwjVQFgwSYKjfHnpVgTysQ08CTgxjYzpvhzBQzLZWUqdQYtKxhILz97IwNgsEWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
تعریف و تمجید میثاقی از امیرمحمد رزاقی‌نیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106551" target="_blank">📅 10:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106550">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7c06af095.mp4?token=GUtGImjkVVpBXf7PdOYW3fn-5YUFXjNPuXFGwlNVrUgyfabh1926YTR0dF5U8xio1SDCyiGuBYruz2e0yxs-RMbs_WvVrPl6uM6902q_UKJFDdlKnXoy7Ipsxi6pnrcCs7ImKQDa-bf40OLcochXR6MeUUjBB5drkPwXeuGeyKufJqqFvmO1djwmtt-XnrOPTYtTsNTyUoKWP6itn72HvHSClFwQgYtPonPR8SEuDMF-sS_vO0EteD5KzCDSButMOZ6QlHItfZg3RUxOsf-oEMSHG2OdvDRtpNCsb9c2LnS7Q4Xp0zjFo4iiU-d_BSURyq_qy8C778aMxdWn_CFIYWqCk86T1neKkYZ0--bBYiUedEJiDhmOHQHmWd5xVL2m3xTdMkhQ1vswkvILN3Pzlwj1k3IU0xaUmOlsWhV29Lll-hBLKqNRjl8oTYQPFLxDospK9Ta6uVD_H4_zQ6dmaG5ZnNu34Cyu1-IGmydzOnaywn5bLIrt1DEenF2_m1mr7g9Bp6Uoof-bznYKzOGeDvB0pgQ_jOuxQypLkYbk_rksMw-fI3-zKit0R10mbGr2Jc_bb42gYPTfgTLO8SzWH5Ci-l0GiYbGmv6auVFrLS1O2hLy4CaZrrjLha_enjlriKl8cygFSCTawoq2TWDmm5Z1uV64uBGeIIqJ7urpbt0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7c06af095.mp4?token=GUtGImjkVVpBXf7PdOYW3fn-5YUFXjNPuXFGwlNVrUgyfabh1926YTR0dF5U8xio1SDCyiGuBYruz2e0yxs-RMbs_WvVrPl6uM6902q_UKJFDdlKnXoy7Ipsxi6pnrcCs7ImKQDa-bf40OLcochXR6MeUUjBB5drkPwXeuGeyKufJqqFvmO1djwmtt-XnrOPTYtTsNTyUoKWP6itn72HvHSClFwQgYtPonPR8SEuDMF-sS_vO0EteD5KzCDSButMOZ6QlHItfZg3RUxOsf-oEMSHG2OdvDRtpNCsb9c2LnS7Q4Xp0zjFo4iiU-d_BSURyq_qy8C778aMxdWn_CFIYWqCk86T1neKkYZ0--bBYiUedEJiDhmOHQHmWd5xVL2m3xTdMkhQ1vswkvILN3Pzlwj1k3IU0xaUmOlsWhV29Lll-hBLKqNRjl8oTYQPFLxDospK9Ta6uVD_H4_zQ6dmaG5ZnNu34Cyu1-IGmydzOnaywn5bLIrt1DEenF2_m1mr7g9Bp6Uoof-bznYKzOGeDvB0pgQ_jOuxQypLkYbk_rksMw-fI3-zKit0R10mbGr2Jc_bb42gYPTfgTLO8SzWH5Ci-l0GiYbGmv6auVFrLS1O2hLy4CaZrrjLha_enjlriKl8cygFSCTawoq2TWDmm5Z1uV64uBGeIIqJ7urpbt0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
وضعیت سربازی بیرو: واکسن اعزام به خدمت را زده اما درخواست تعویق پزشکی یک‌ماهه داده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106550" target="_blank">📅 10:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106549">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd9668387e.mp4?token=iK16T_7ngfuQbrVZNQ8S4msrpjqAXyYCBqchxjFzy7GV8nGSRH0oMOE9SH1TYhtzDsc00Ku7di7v6UOllpleb_Tu5rUDzYMK-4EtPiLf4SkcA_I1hTzfI2xV3QBiblQJYpyOnma8k6rSyylAoWI9fOcNNzR8z1nKDaioINeWq2ItLtXvll14Ze2kg1cfB-mEKXwjLtGt4wLdwx2MyP7gHI4YqJD_MVGKERN6SmEDDFOaFSVsyCjME_yqhJzVRFUir_-4syuqE2HXJGLX0hcQoCJKbv1EBd2iV_v8wgd_7Xg_Mji0OS7i08wRwCImRsjszNYx-65Bu7DukjkKRM5-_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd9668387e.mp4?token=iK16T_7ngfuQbrVZNQ8S4msrpjqAXyYCBqchxjFzy7GV8nGSRH0oMOE9SH1TYhtzDsc00Ku7di7v6UOllpleb_Tu5rUDzYMK-4EtPiLf4SkcA_I1hTzfI2xV3QBiblQJYpyOnma8k6rSyylAoWI9fOcNNzR8z1nKDaioINeWq2ItLtXvll14Ze2kg1cfB-mEKXwjLtGt4wLdwx2MyP7gHI4YqJD_MVGKERN6SmEDDFOaFSVsyCjME_yqhJzVRFUir_-4syuqE2HXJGLX0hcQoCJKbv1EBd2iV_v8wgd_7Xg_Mji0OS7i08wRwCImRsjszNYx-65Bu7DukjkKRM5-_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🎙
آیسان‌اسلامی: هانی‌رامبد بخاطر مسائل ایدئولوژیکی از هادی‌چوپان جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106549" target="_blank">📅 09:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106548">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqHkKhZtSndrU-aiU8SSow2esqinr0OOI1o-KcAshnl-vOeZeu3jOZDizP70qZhb8Uo6qVSN5m1jbLDELVPpN9F8_JB0vTLKuZiSbYOJ3auGHAd6okuM0iu6Hz7BBmsSzuyL8YEo932dBUprjs1PQBz0EoQrTNNb1CIggL8BNfQSGW-N_5TjghgSxi3l38WPvUXhgoKxNJF4TALseasqECbPrpmHQX2EKb_CuZE0DkXQkcq9Gk1BTxuXQqNrHnPe5e5x12y6DFY9F5twZFxR6xBqGMO60iTXjPeLD9Pw1UvS_weu2J_4ZNsQkfSr8HXV-qGDtjn85i4DfP08EiRD8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🟣
عملکرد فوق‌العاده یاسر‌آسانی در تاریخ مسابقات لیگ‌نخبگان آسیا که تنها ۳ گل تا بهترین گلزن تاریخ آسیا فاصله داره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106548" target="_blank">📅 09:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106547">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKedEFxFYCUjgHIHY92eBSOWGBnqwNiHJJoqWuG0TR3HVdULfwt1JuH2JOF3sFhVWKs1bV7Dk70t9KJgUd8KeNIlqlNXxK9UPpHpie4ytgRI434JTLHcd1nGIzfemiiDSwjAoQgY9zNOsL8z64pQlO9rpDLX-xy48y06r3soR97WDcqoqUMM0kPtkT8wJPbsoJwV6oeWK6Q5Orwok9gN6Xp7aCyW8A_pQRVbWw6uZ72nkz8b0fhwLxDCs_8hP78ZKLFQ1hw4NwvJ4sCG8NfqVjfVpXtb9JFaRWPYGH990b1Mplt6KKnGK42wnUYBTXGiX6N2k-tRQdRyMmykP_aACQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
‼️
مارکا|باشگاه‌بارسلونا قصد داره یک‌کمپین تبلیغاتی فوق‌العاده سنگین در حمایت از لامین‌یامال برای کسب عنوان توپ‌طلا آغاز کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106547" target="_blank">📅 09:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106546">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6843e64d1e.mp4?token=p1M7NRLLCyXub0bJpiEnDtU9kNKN5MHYhc-MAy6t79ov6HHNbR-31JZcx1qsRvjNYIp5dj5xXtJOLlkYvUWI3NpGtQRCGHPvARLsZeb2v6KGYbiWHACBOn-X0QUvfUJDvqmCn3Z7iGqeiuk7cdXO-Yr8YAzp01QNHnz3IFcz9kl-rnRNWscLeb5n8o1hf4k2x3zfcEHriqb5JohYmDl3tPlE3Djjo7L7YSj7hrGS2uokKzKMDtInSkhe_YrGNIbenTjTevCh7kXJWditlWMuJt0pgy9cqCP5-ZLmTjACelnefAtGYzJtN6JkU32JO0MitU33vhuKYvlKRBOP-quiOSuXmqN5EpX1-tha0XFS92NZQiBmNeH2nBSyqN3P7mLIG6tc6r8B-e63raMhYkuAbsOPULB_s0bDr9BoTDz5nozPQImd89ZqScFascIJB7QXBynLwUqD8jnI1ZmCK5TMCp4wggzeNRYQXXyioy0rDhRMQvT3iTE3AGEMPVOnPWEYbBL_zjkM5o1TL-FmiZrroqOrhdRVOHF4CR0RYNdjLIywwlxu6f4nSwURz1u4922kulcxDoRGCrtibAXM_wrXrFXsci5hb99Qv_kD_1G3zIWzSmNSxOCsntNCLMN4bEBoQfsM0mubPaL9ypluEMUwsu84lCQKMH7HofgiiXR6S4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6843e64d1e.mp4?token=p1M7NRLLCyXub0bJpiEnDtU9kNKN5MHYhc-MAy6t79ov6HHNbR-31JZcx1qsRvjNYIp5dj5xXtJOLlkYvUWI3NpGtQRCGHPvARLsZeb2v6KGYbiWHACBOn-X0QUvfUJDvqmCn3Z7iGqeiuk7cdXO-Yr8YAzp01QNHnz3IFcz9kl-rnRNWscLeb5n8o1hf4k2x3zfcEHriqb5JohYmDl3tPlE3Djjo7L7YSj7hrGS2uokKzKMDtInSkhe_YrGNIbenTjTevCh7kXJWditlWMuJt0pgy9cqCP5-ZLmTjACelnefAtGYzJtN6JkU32JO0MitU33vhuKYvlKRBOP-quiOSuXmqN5EpX1-tha0XFS92NZQiBmNeH2nBSyqN3P7mLIG6tc6r8B-e63raMhYkuAbsOPULB_s0bDr9BoTDz5nozPQImd89ZqScFascIJB7QXBynLwUqD8jnI1ZmCK5TMCp4wggzeNRYQXXyioy0rDhRMQvT3iTE3AGEMPVOnPWEYbBL_zjkM5o1TL-FmiZrroqOrhdRVOHF4CR0RYNdjLIywwlxu6f4nSwURz1u4922kulcxDoRGCrtibAXM_wrXrFXsci5hb99Qv_kD_1G3zIWzSmNSxOCsntNCLMN4bEBoQfsM0mubPaL9ypluEMUwsu84lCQKMH7HofgiiXR6S4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😳
بانوی استقلالی ساعاتی پیش: به فرودگاه آمدم تا جلوی آقا سهراب زانو بزنم و پای او را ببوسم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106546" target="_blank">📅 08:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106545">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mv7K5MsrSBoZMfWcqm07YROEG4JEf9u5Ilfe5Ozn_UBAmOvEC9ricnrnLmFVrck54t_oq-PccS5dqm_PScluhrlWU6ty-NfCRqBqyKFHcudJbK0hjt-36upX6tLOuve4H7rS4ODz7PriSjzLKl2ScrUQjFFQo7i9tLb8RTFwxHKrWuDpIrDpLw3EpAb_zc7LNbwGXKOQD6LUo4HKo6PED04RVuvQFWpDibpFcMRdftNgPm2pepJe8Wm08l9nQdhKlpthIBQvex2Hsgr6r5tuP6v5D-AHxQ3lOhC25Gc4XazBgReiPaa6ITVV8Rnz14ROczO09Pm7r-wvAjnZGEjLVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
تا ساعاتی دیگر میزبان فینال لیگ قهرمانان اروپا در سال ۲۰۲۹ اعلام خواهد شد. نیوکمپ گزینه اصلی میزبانی از این فیناله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106545" target="_blank">📅 08:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106541">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HptjNHfoQIIUDc7ciqnrab6rNb-CTNSZlyVZ4e3FMiPf-JqiuP9a3MEJ2avqv8cWPcSMI4lMMGSjg8dpPl90ejRK9i0LA_fxgEmeO1EV3RGDqXUzYfZwPkk_usDTsnjHqpkCkEOXZSZh9snzP1dkmYBmeenyQ7HzJA-Fi0EZ2ZmYIRu7NzuSF7URIjfpC772tWk1r3Nj8VVMy1gKFY-_73NDfiAVkmfrnvKgDUZ5W8NUujhltJQvWucarcT1g9xhXKqKrTAHRA2Zix3nepOIIAAl6ZcAXoA_CEqdqIGdrELuSpg04a91lT7CACO_tUARrGvlQqE5H1lyVoQSTJP0dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
تمجید لوچسکو سرمربی السد از استقلال
:
🔺
مقابل تیمی قدرتمند و باسابقه قهرمانی در آسیا بازی کردیم که از حضور نفرات هرچند محدودش به نحو احسن استفاده کرد و مطمئنا رقیب آسانی برای سایر تیم‌ها حاضر در جام نخواهند بود. متاسفانه بازی ضعیفی ارائه دادیم و چیزی بیشتر از این برای گفتن ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/106541" target="_blank">📅 01:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106540">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b135c8df42.mp4?token=VC8qMBhNbQmLZtHidmWeXsn7M4n_eL5v932D5mKnkZ_KUVQIdcKrlMkmTEnjAoAZ91w_inCWOdmYp98-41tl8vT72mb6xJqo9xi_aJqxY1qcR2THTEnyNGhReVKlo3ndDahx5f7fFHwfLYIzvK2Z5z4lgODN5L5kWRlPRA_yB1Kvtnvj930zfLS81JCIYVejfCq61UNKjYgNJzoQEu4Kn3hjxwOCxmaD3nRNUDiwTxml2wA5BTvkpA5rcBwoSO8cETe9Obw01sMvAgQjtSWc7B9Aav2vkCLcxXn19TjZy9WvOQkYMupZeGkPcEMSYRLJ8RMU3-ISWNsq4mJ8CvEi_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b135c8df42.mp4?token=VC8qMBhNbQmLZtHidmWeXsn7M4n_eL5v932D5mKnkZ_KUVQIdcKrlMkmTEnjAoAZ91w_inCWOdmYp98-41tl8vT72mb6xJqo9xi_aJqxY1qcR2THTEnyNGhReVKlo3ndDahx5f7fFHwfLYIzvK2Z5z4lgODN5L5kWRlPRA_yB1Kvtnvj930zfLS81JCIYVejfCq61UNKjYgNJzoQEu4Kn3hjxwOCxmaD3nRNUDiwTxml2wA5BTvkpA5rcBwoSO8cETe9Obw01sMvAgQjtSWc7B9Aav2vkCLcxXn19TjZy9WvOQkYMupZeGkPcEMSYRLJ8RMU3-ISWNsq4mJ8CvEi_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇶🇦
روحیه‌دادن لوچسکو سرمربی السد به بازیکنان تیمش پس از شکست مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/106540" target="_blank">📅 01:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106539">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlTt2tyBqymOcxG2LHdt6MNpuYTIpNjaP0dmpsE6h6qn46oaH80-MB7VJnv5ggVrwcBIpHQLO0txHLxfKL9pL8smhWEO4VA03HO97Pf0-QM184ZYHxfTF1DhmyegRh-JsDElMfIgVoFrvcwP8E0sxVjzyFQihljo0HcN9dTToqpEEp1q-9Gjw-s36xOQQC4p7Ger6oGhzcmwiKwYCICAb-90ODrSBksBAosGweD7FNi2vUHwKGJQEG4KnEUkRQ9YqFshTWZRDqOe4Cqgqs1vBEsJtUZvgZCkxCJFbNdVy6uT2BuRaC3Cvi8RnG2wx8Ip-D0IhDs8Lsa1h1NIAqjWow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🇮🇷
پست جدید یاسر‌آسانی ستاره استقلال: این فقط شروع کار است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/106539" target="_blank">📅 00:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106538">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1214641e23.mp4?token=DG0kpB0HEONf54wD-Hp_dInoOca0DTVWOcj-LipU68XJXOZ8J9657itIeMvunpnBp3m9r-OuypoDvz6Kst__89sxNEz7-8xE19Vv7K3FFv66_AWJXuY1paRk_oKZBOgkYif4YiE7zJFfOXznAXilvq6suGFlWUScNhnI7C5M7uq22QuSKiITon-E0Glhw_yM44eyWd1lRBcyWWW3YZOLCUqge1DqKfVmQOMnsFiihq56SodMDVE9b0B7wN10EzPcet5rb8OupJI9qEB3RhuOZcnc6-FpgT0_cR44SaYzaG5RGvpHh5H-6KllISm8KkgZ0XsYrZnTzF5CxZTYNQEgzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1214641e23.mp4?token=DG0kpB0HEONf54wD-Hp_dInoOca0DTVWOcj-LipU68XJXOZ8J9657itIeMvunpnBp3m9r-OuypoDvz6Kst__89sxNEz7-8xE19Vv7K3FFv66_AWJXuY1paRk_oKZBOgkYif4YiE7zJFfOXznAXilvq6suGFlWUScNhnI7C5M7uq22QuSKiITon-E0Glhw_yM44eyWd1lRBcyWWW3YZOLCUqge1DqKfVmQOMnsFiihq56SodMDVE9b0B7wN10EzPcet5rb8OupJI9qEB3RhuOZcnc6-FpgT0_cR44SaYzaG5RGvpHh5H-6KllISm8KkgZ0XsYrZnTzF5CxZTYNQEgzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇶🇦
میثاقی: بازی مقابل آسانی آسان نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/106538" target="_blank">📅 00:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106537">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArvtPaXvLCPN_RBjEi_gdxQ6rlTLlXSA_3AQzjGmQYIarj1ariR_NwInmr_MRMs2l8UXXsayJCILPcwwSO4uMiZkyoqNDRH1cjxyQ4_yJgXOoYlMHraYE1QxwdpUCJxONwG5zG8DSLV93TRZuzjN3Jsrc7J25WCBfU_o2vOf-dujnsk1EY1pc_4iUaErWD9tpEoHcOZZkA1LKQhE1r2keFVwruD-JNSnF-OVFwYUvnJ2eLmGr1t4MvNcHBVZbjKWf5SR3kuZpBcVUIPxmtg8NmZsj4PQpPu57wacMDjudOdI4Pq699vXXMlzQaMTeuPUTyjPRrh_VFeAvaxM_hJuhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
کنایه عثمان‌دمبله به امباپه: برای بردن توپ‌طلا نیاز به جنجال ندارم. تلاشم را در زمین میکنم و امیدوارم بهترین اتفاق برایم رقم بخورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/106537" target="_blank">📅 00:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106536">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
🎙
صحبت‌های سهراب بختیاری‌زاده سرمربی استقلال در نشست خبری
:
🔺
ضمن خسته نباشید به تیم السد که از بهترین تیم‌های آسیاست، به بازیکنان تبریک و خسته نباشید می‌گویم. بازیکنان استقلال امروز فوق‌العاده‌ بودند. به هواداران پرشور استقلال تبریک می‌گویم. امیدوارم این روند را ادامه دهیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/106536" target="_blank">📅 00:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106535">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDwRBgH9lBhspGgJrM_1ndHaoquoc1Hp5Uvvlah2mLTS1W8nL3LyOy6Z6JXW6XFLdWcqdVKW61c5xpUiNUlNXPOnWMnhXzbFyUxgIUGeFXqP30pq9bDjvA0G9jA8IxYx6LgLEBcNkb8UQ78E2ZWZAdvXvs3BkHW7q73WjCd_5ihg0OrZh_mIWpKrYVKbZlDz5Mw-EY0P6ORo0AbxPm6SwaTl0JS7ySbfhUq1mD19DSnehAHdP8-BTUkXkSxUeUFp6fSoFVkRo6ny0G29nZzh7Oz9NZ6C6UvpHoQ8DsUDh3hKkwmfi2nHXQDv-Ap8h3yUeT5kcso4zNx3ciqwjntVQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر بالا خوشحالی اکرم عفیف بعد از گلزنی مقابل استقلال در لیگ نخبگان 2024
تصویر پایین بعد از دریافت سه گل از استقلال در لیگ نخبگان 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/106535" target="_blank">📅 00:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106534">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd294b65c6.mp4?token=F1EAivt35yC59SPODjtouIVEqGxGxD3NvW5iO-v3JnAgZV1nAjF3TpmqFtMO2Gvcf0ll0AFMew2iuUPTfQZ-0OsL53-J__QkJ4SLqBxs3H0GHzRvZ5I2uC011aiWcdy72I_d-wv-5XJiTKYRnrlj94fmybAtCuwzYciyiJPjaHScf7-rJsDUr8xIZiXcLtIYK4Ssfal8m5IQKgCGZC0Ptkk3rWzFH_eSkYY0FyoRq_oGc0O3ny-6o1Dio36gDSMCCcEzvt3jzi5B2nzVSAzRJ0h_u9n6zHJ5am9AMVRYFYJzFqZh5gakrjM-MYTwFf9rXPwu2eLOI7jAaBmiH7sp6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd294b65c6.mp4?token=F1EAivt35yC59SPODjtouIVEqGxGxD3NvW5iO-v3JnAgZV1nAjF3TpmqFtMO2Gvcf0ll0AFMew2iuUPTfQZ-0OsL53-J__QkJ4SLqBxs3H0GHzRvZ5I2uC011aiWcdy72I_d-wv-5XJiTKYRnrlj94fmybAtCuwzYciyiJPjaHScf7-rJsDUr8xIZiXcLtIYK4Ssfal8m5IQKgCGZC0Ptkk3rWzFH_eSkYY0FyoRq_oGc0O3ny-6o1Dio36gDSMCCcEzvt3jzi5B2nzVSAzRJ0h_u9n6zHJ5am9AMVRYFYJzFqZh5gakrjM-MYTwFf9rXPwu2eLOI7jAaBmiH7sp6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇷
جو فوق‌العاده رختکن استقلال در بصره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/106534" target="_blank">📅 00:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106533">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8nIqswHgVdmvuWiYATg-h_0mHEMRbfO9ZoT1KItfUx3GUci_Ud_b2999pxwBqcA8tsq5WjmJ4QHKLYo9EtbgxQ6kietzltmohmkUPDj1ddN7TLlIQVR85-syDLD2lGIzdFQSwVyw1sHUcYka9c6F5sB-SA9lGqvuy5cWQl2jpeqrCkw9b16pP46nHNNIbhLZQGbk_ybnFty6FnHKC3dfZvgZNciS3h6WPdu2Hwvx_fAZru9Pi7vwpqt9rt9iV2WWryA7lvZ0H0mkvkSzr4EEFcuL2KAHIPTKKZYWEgyeLJB5YgYzhe13gQHnpH6FXFgoAIqNfkxBWA_ZvN9M62N2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📱
استوری کنایه‌آمیز با چاشنی کری‌خوانی میلاد میداووی مربی استقلال برای پرسپولیسی‌ها
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/106533" target="_blank">📅 00:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106532">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_FAo5r5Yvccddoquu9c748m2eYhi0W1jbiey2E6sT0tZzJsYv1YUClcplOqvk5YhDDHhB0qBTeoisQmzQrOy8Emwk_g23Wg8J_kow3qGIiv3kksc__DNDPE_zyPB3zReRtRuZZiJD5QBj2me4sXbf0dxOw6ypaVvhVrDOuH8pAHs5Y0BVpcyZnbyVpOm19gwT8OB76Zq0dUnONmUWGhK4kdIx2g0gnQ6STZEnVe9WKCaarYGd__qjWTmu4rlbLUFb5bBY69pyY9DPOVlX_TCalAcv14k8WYkM4OirrKBVdTdzg20AHl2BngXSTg2lanImawWAVAQgkbzIbUJzYIFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇶🇦
السد قطر که در تمامی مسابقات این‌فصل خود حداقل سه گل زده بود، مقابل استقلال موفق به ثبت‌‌گلزنی نشد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/106532" target="_blank">📅 00:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106531">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXlLlykCYiuiTctftmoKn9kVpDTPqn8dGhzDeBSB02X78wTYWv95skWp9qTZircstKN88-biXlkBYAJAh67TPyOmWsC-XLsVZLgYisOOHTztagreWX88ddXDf8xzm5oCCSl-Xbwwaog8fy3MEm-rwk65M5N-l_ZRjjtINmcs2iK-X-btTXG2eY_JekC-WER1Pc6yMH6914YJ4NOCxGwP3ni50C0XycsmEEVNOYVGoXRlcvRpKdMWS4FquWphlJIi8XYYvMNmswpri38UR4PU2R5xOMPJR66y5SaX3zirajPjUc6AMEuXLUCx06X8Iyd5aVdS1VeT62bzpvHnwpNMMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
توییت فوق‌العاده سنگین باشگاه استقلال به پرسپولیس با کنایه به تورنمنت غیرقانونی سه‌جانبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/106531" target="_blank">📅 00:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106530">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXOB1myBjDMbPXocD98n3Z5HGvM5OUiQwcx_YL58PwSnI0BqUb3xa4fIpD8GVibc4CAf31y6HUo_zpBzFCFq3Hnygexiim5Q8WKq1oFD0GkmwdP0W9mp17b4Gha21aCCIaEVmnEYhfMwnPltwhB3-zMjvpvnX5hx-fj2GCxVVqc1cDoFqaOzVaWFkrl_VH6ifcQdAiueFsSNPYgxl34QUISagVgy5rS0_fJ_qVj9PAQqokHokBEu2FWgHQEZIsmQae34m7CPZoioxdVeEW2qSb_GlFGAinSlscDjl4jpfq6Uy0sXkGaCYJhJKR9br0V7fbv_7-HcDxovL7sfTOMm_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
✔️
صدرنشینی قاطعانه استقلال در پایان روز اول از هفته‌اول لیگ‌نخبگان آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/106530" target="_blank">📅 00:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106529">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/u05Q0R8gX_wfD1xyF2xzWZDGtQ-C2Nbtd2WRQvrV1ctsrXzc6ieSoMtIBtagxKtEuJGSiuzdTc1EMUVZLzcxecjH-mIOHRg2VYWPS3Dwo-Fd-gvvb1PXMexRgU4SIc1BCgLetJMVqmIWr_sSt17D3ze-05yEDPEwGpGjL6oskJvEmwxGtvaN5hXcFslIM2cJlTU_d_ZHSXBysKpGDXa_Ia0ItppaZlU3HJNJmBIOXJ4esx4WrKfTo0nMsrOO7SQErp93HrkEFzUMTDhYBnBChwF1So3p88ev-jaev9o8KqH28l-oeKW4aAXPJjMJVIrGZha-wOBQQNbGL0Z9T7VHCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
توییت کنایه‌آمیز باشگاه استقلال بعد از برد قاطعانه و پرگل مقابل السد قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/106529" target="_blank">📅 23:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106528">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGFVakFJa_jUbeHr-DTbLmSeOTUGfZw7Uiw-rbz5crcCLRxRzYwjhBbra8nCU2I0Xdt-7COMPua6RbinQZQZmQhUqfXqvifxEmYML_0nw8HYD4DECotSX1stpEPyJGyH85I_csJjsW4MnyJrjLGwAXZtG5ntpbyTK5QBTs7rvLPO06h6qY_KG4YgxkK6kmyPPUUs1U26BAEGRiW3rurAxXSS-JOshL1SUq8lZ6WkEXu4Msoy19SqeSj6n2M4ddyNT5gZMI6udut4-7gW_Lpk7TOVgdYypEYVL4A7tVbsq4Lydj0QChbaVm3EIlPKdhU8RfnQWldmp5Ba0RmtsJUBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇶🇦
باشگاه‌السد قطر پس از اعلام غیرقانونی بودن یاسر‌آسانی از سوی هواداران پرسپولیس درحال تکمیل و بررسی مدارک برای شکایت از ستاره استقلال خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/106528" target="_blank">📅 23:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106527">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqfgf8UvjjG2z4Uu1XGv6MW9XkkWQ3JUHLHjnbLLdd4_wgwmQFSKhuZaA7A4W1BWtdDc5rRNLkYiJpgM19TgN3-naydoR3uUliw-KsmYG6GLe4sN_fSmpyG6pmnn8yVkj6MSNMU-SxOKW9lsNWgxCECVS0gQG_vxr75p2IUYNQrtpxtYmuxHlGr_yEjuKI-RLohtKHhW1_gT-z0q7rkVrgrtv59KIieBF5T_dN-Mc4AU8Iqk0Q3ULyrh58pJssRc0Y4agRYY6SflxWWzNjq0ubbgc548zyz0PaSnCngji-5r0LiXS9QV8RDNG7fK3MXY_vixBsxfaVg6vgB_bGsnMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
هفته‌اول لیگ‌نخبگان آسیا|غلبه تاکتیک‌های سهراب به ریال‌های فراوان قطری؛ استقلال قهرمان ایران در نخستین گام مقابل قهرمان قطر پیروز شد
🇮🇷
استقلال ایران
😆
-
😏
السد قطر
🇶🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/106527" target="_blank">📅 23:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106526">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
✔️
▶️
خلاصه بازی جذاب و تماشایی و دیدنی استقلال ایران و السد قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/106526" target="_blank">📅 23:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106525">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8H_PV7Lm5-6kMxaHbUkLqDO1ljW0b_JIMwxC6tgZ2OvMbkNsHpxjCIsN1CHXjsAE7dNoPvPgqcnyxt1_p2H0oPE1mrn63fZ0eatXykLfFhhLaJPqhZAzEJtNy1wdXKeWm3POIlBirFy2S0JRk6CdjsJWS5TCsB7t4XoK9kvvmc0C9BJ1vnzOcFwPsCp56R2zfDO1EhPPT28qqpvAzPyyEycgUTfFUgRbkEhTOUnPz5HxWuGXgF-8JVdRXwHuBMi4B7fdb7f2izW2dJUmndiHMkihcDmco1kRjoS8fJZnr0FcQsbbV-UugIf1JXdG062fhypu0wVjtbJQzEBM-rUIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
اظهار نظر عجیب و معرکه از پیمان حدادی مدیرعامل پرسپولیس: چرا استقلال سه بازیکن تیم خود را به اردوی امید نفرستاد که امشب دو نفر از آنها گلزنی کنند؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/106525" target="_blank">📅 23:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106524">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
‼️
🇮🇷
اظهار نظر عجیب و معرکه از پیمان حدادی مدیرعامل پرسپولیس: چرا استقلال سه بازیکن تیم خود را به اردوی امید نفرستاد که امشب دو نفر از آنها گلزنی کنند؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/106524" target="_blank">📅 23:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106523">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKJm7YKP6Q7r2gsNW5LnGSDgKqov2CiGS3C2n0QJYoT1a99Chuq3i8nqSEVIH6F5urvjcNoE7o4RPrHnejunFz2AcChL9o6CM8LHK3YQQhZ0Ax1DJhm2AyWJEmJpbks1vSRudHYeMQuyUgKOUZxx--n00q0IkVnefrf7nPzjlTwcvEDzxibtQNqf1bEW5HpQjv_k-wLloAZYxBRaYyKvirt0Rm_XmQ8qDnEZ95DbgYXb1DHdmcJJKSCsLL3F02MEMwCQWQ7V8BNDvRQnUQ66DgCzHjrnDUaQaYpuAWye1fJ7NwrIFpywahLzlyxEYXpGU1JIcAHjxFivoBhT3ABE9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
هفته‌اول لیگ‌نخبگان آسیا|غلبه تاکتیک‌های سهراب به ریال‌های فراوان قطری؛ استقلال قهرمان ایران در نخستین گام مقابل قهرمان قطر پیروز شد
🇮🇷
استقلال ایران
😆
-
😏
السد قطر
🇶🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/106523" target="_blank">📅 23:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106522">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766e5c50db.mp4?token=EFAklK5c2cehbCuiTYGJWwBiXimitLXcgHOr6_MuH3L3sAKp9D2cHuTCbaP7VphOHldSs7sZczgkSvvkifJ0o1bo-PFYx6NaM-4dueSfpHFD-atI5jr90kck_RLM7k_NAR0ABqz1efhT3fJQJm8f4zePP3VMbnrQfbd7rv6zhmRRPZpMAqic-JAfLWeAVY63UQve0f289lt8zOh8Eqp3WqmOD6nM_DJRKnlOieZ1bwH6s4fJ3e7nNmUuw6G5GE2JjbIwaQEiXlz8SDge_eKTXh0GmyZDkVdmv97j1YBuVUYq233F9BTVzpOhRsu7VST3tIr1Hh_lQ3eBczT1Tm9nZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766e5c50db.mp4?token=EFAklK5c2cehbCuiTYGJWwBiXimitLXcgHOr6_MuH3L3sAKp9D2cHuTCbaP7VphOHldSs7sZczgkSvvkifJ0o1bo-PFYx6NaM-4dueSfpHFD-atI5jr90kck_RLM7k_NAR0ABqz1efhT3fJQJm8f4zePP3VMbnrQfbd7rv6zhmRRPZpMAqic-JAfLWeAVY63UQve0f289lt8zOh8Eqp3WqmOD6nM_DJRKnlOieZ1bwH6s4fJ3e7nNmUuw6G5GE2JjbIwaQEiXlz8SDge_eKTXh0GmyZDkVdmv97j1YBuVUYq233F9BTVzpOhRsu7VST3tIr1Hh_lQ3eBczT1Tm9nZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
پیمان حدادی دقایقی‌پیش: قطعا از یاسر‌آسانی به فیفا و CAS شکایت خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/106522" target="_blank">📅 23:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106520">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/106520" target="_blank">📅 23:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106519">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اسماعیل قلی‌زادههههههههههه
😳
😳
😳
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/106519" target="_blank">📅 23:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106518">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">چیکار کرد امشب استقلال
😂
😂
🔥
😳
😳
😳</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/106518" target="_blank">📅 23:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106517">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پشماممممم از سهراب بختیاری‌زاده
😐
😳</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/106517" target="_blank">📅 23:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106516">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">استقلال زددددددددددد</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/106516" target="_blank">📅 23:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106515">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">االلللللههههههه</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/106515" target="_blank">📅 23:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106514">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گلگلگلگگلگلگلگگلگلگاگل</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/106514" target="_blank">📅 23:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106513">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گلگگلگلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/106513" target="_blank">📅 23:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106512">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گلگگلگلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/106512" target="_blank">📅 23:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106511">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">السد از کوووووون آوردددددد</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/106511" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106510">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/106510" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106509">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">فیرمینو دروازه خالی نزددددد</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/106509" target="_blank">📅 23:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106508">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">استقلال از باسنننونن آوردددددد</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/106508" target="_blank">📅 23:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106507">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/106507" target="_blank">📅 23:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106506">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">چه توپی گلرشون گرفت
😐
😐
😐
😳
😳
😳
😳</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/106506" target="_blank">📅 23:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106505">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">السدددد کوووووون آورد</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/106505" target="_blank">📅 23:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106504">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گلگلگگلگالگ نشددددددد</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/106504" target="_blank">📅 23:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106503">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ماشاریپوف بجای رزاقی‌نیا وارد زمین شد</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/106503" target="_blank">📅 23:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106502">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">حسن‌الهیدوس ۳۶ ساله هنوز برا السد بازی میکنه
😳</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/106502" target="_blank">📅 23:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106501">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حردانی امشب بهترین بازیکن استقلال بوده</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/106501" target="_blank">📅 23:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106500">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">۱۵ دقیقه تا پایان</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/106500" target="_blank">📅 23:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106499">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آب درنگ
😆</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/106499" target="_blank">📅 23:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106498">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">صداوسیما حداقل با یه دقیقه تاخیر بازیو نشون ملت میده</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/106498" target="_blank">📅 23:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106497">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">استقلال کوووووون آورد</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/106497" target="_blank">📅 23:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106496">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حردانی میگه اگه دعوا شد کادرفنی بریزه وسط زمین
😂
😐</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/106496" target="_blank">📅 23:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106495">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
🚨
گل السد هندددد شددددد</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/106495" target="_blank">📅 23:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106494">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">صحنه داره بررسی میشه</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/106494" target="_blank">📅 23:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106493">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">السد زدددددد</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/106493" target="_blank">📅 23:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106492">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گلگگلگلل</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/106492" target="_blank">📅 23:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106491">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86d2b781d1.mp4?token=Fdbg4bivtyQyoO1YSDz1X51bYcVkQ7pKo5S2SU0UAHwnkPpgWTBml3Mc9gJJt5RyWvsFlIpiekxLBqncG8Ge32HN6EjAwiaisCryGyZu8tPbXDfr7m5QcFwb-FR9dIRvGRk35PZ5HM990SJt2RAQWkLzxz4qCZqcL4VfjOZjFDDgWQdApJxVX_3xKjUPQVA_zay5YSp4ixjZEzIpA-9A4dABTe2vovuz6K3AB-74xHaY5y7aidPFmDdliPw23x7bXwY19z2zqsROTR3Thn9UKq5v4qOkufeeevV4ezlKUK91hQXDBt_CA6kt_jzVLFbRr3j1xRxf8Pf_gPxu3_UJ9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86d2b781d1.mp4?token=Fdbg4bivtyQyoO1YSDz1X51bYcVkQ7pKo5S2SU0UAHwnkPpgWTBml3Mc9gJJt5RyWvsFlIpiekxLBqncG8Ge32HN6EjAwiaisCryGyZu8tPbXDfr7m5QcFwb-FR9dIRvGRk35PZ5HM990SJt2RAQWkLzxz4qCZqcL4VfjOZjFDDgWQdApJxVX_3xKjUPQVA_zay5YSp4ixjZEzIpA-9A4dABTe2vovuz6K3AB-74xHaY5y7aidPFmDdliPw23x7bXwY19z2zqsROTR3Thn9UKq5v4qOkufeeevV4ezlKUK91hQXDBt_CA6kt_jzVLFbRr3j1xRxf8Pf_gPxu3_UJ9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🔥
گل دوم استقلال به السد توسط سحرخیزان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/106491" target="_blank">📅 22:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106490">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سوپرپاس گل یاسر‌آسانی
😐
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106490" target="_blank">📅 22:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106489">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سعید سحرخیزان
😂
😂
😂
😂
🔥</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106489" target="_blank">📅 22:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106488">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دومییییییییییییی</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106488" target="_blank">📅 22:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106487">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">استقلاللللللللللللل ایرااااااللن</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106487" target="_blank">📅 22:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106486">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اااااللللللله الکبررررررررر</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106486" target="_blank">📅 22:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106485">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گلگلگلگلگگلگلگلگگلگلگل</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106485" target="_blank">📅 22:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106484">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xw_e8LQ_mOFoTCnoNQBPTG_ZkPL2bUhJ0So4O4kVrZC19MQIHr7lkzbw2zKJv1AKb487cquEu2Uf3PYDrlV5KihcIWvC3ve5O0rciisV6twm0XotVCYqqTPCIwI2ORzB0k7fJ_mKJlT8_zydoI3DhguCMaVvPlS4dx8r0PK1pbcLi8hKC1jgGNDN80gWKunFH33C-MTSnMubp-LR4chmjA-bKOFCvTssrQAPSmVCU9MGBtZ6iFoypik7HU05JZO4jpI7RfO4ZR4pnKRzgDW_m6Vwak0haSjkEU2SXKfI7UrIHBsIMIl-dTMl3_kWCLIu0lLsFS_JpgTc3yeLAkjb0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇮🇷
آمار نیمه‌اول بازی استقلال و السد قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106484" target="_blank">📅 22:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106483">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/323962117f.mp4?token=sJ2psTP0FFOanU4Q7u6D5eCrLv-DEOFyg0oxgB316EJAytS6aZsqQlmMfGZ5mOxHeV8fe-IfgieZ6XA2LpVd1Ei_8Cf629K8gWIBnTmmYaAYRsnJhuPwOU0jBhZxv1x4I_VroIMFpd51mki3fGexUGU3430SHymHsGX0R-yUlq2yTorpDweUXxewScS4FvnpykXd_3OtqgWTFaYC_OasEZR6_jLHjvqy61xH1a3-6Qs_JAI2kqaJL6qTkXR_8wExcRdcQra8US_qfcQnsWi_MEJfB9g4dLxMn1xz5T53yX1CYcBiot-_Q0tiikotwsP_GCMoe6RFYRQPDr-r27V1vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/323962117f.mp4?token=sJ2psTP0FFOanU4Q7u6D5eCrLv-DEOFyg0oxgB316EJAytS6aZsqQlmMfGZ5mOxHeV8fe-IfgieZ6XA2LpVd1Ei_8Cf629K8gWIBnTmmYaAYRsnJhuPwOU0jBhZxv1x4I_VroIMFpd51mki3fGexUGU3430SHymHsGX0R-yUlq2yTorpDweUXxewScS4FvnpykXd_3OtqgWTFaYC_OasEZR6_jLHjvqy61xH1a3-6Qs_JAI2kqaJL6qTkXR_8wExcRdcQra8US_qfcQnsWi_MEJfB9g4dLxMn1xz5T53yX1CYcBiot-_Q0tiikotwsP_GCMoe6RFYRQPDr-r27V1vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
🇮🇷
درگیری بهروز سلطانی و وحید قلیچ دو پیشکسوت پرسپولیس بر سر علی‌پروین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106483" target="_blank">📅 22:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106480">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76510c3fac.mp4?token=ugHYWThqpgLDcKI6rCwpr1HaMsGCOpDvjXbomRpZu-ghdshUb1daCSI0xUZ984iPmlmCaOHszlSnpEOZ78MYVBw-bCpXu16r7s5dyOtsx2HJJqwU2KDwzUKO1S6sm5L621G7VGsJ6Azq8-r83BbUAIhV8w2yPB_w2l07IfhNoWietm98RPmkSOUD0LD_ANt7vId7aBBZ4hStm-D2BM15lmtn8Kb_wXPW3_16e2fovdwITfBPdwLTXdqV8FTBzNmIbEThovRHMCxD1O5ZaY6Xawdm4EMcut6_E3ii7XiNitgjfQGm7ca_VzqM5-RqNyxlYvSTpRfaxkM6KBL66J3hFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76510c3fac.mp4?token=ugHYWThqpgLDcKI6rCwpr1HaMsGCOpDvjXbomRpZu-ghdshUb1daCSI0xUZ984iPmlmCaOHszlSnpEOZ78MYVBw-bCpXu16r7s5dyOtsx2HJJqwU2KDwzUKO1S6sm5L621G7VGsJ6Azq8-r83BbUAIhV8w2yPB_w2l07IfhNoWietm98RPmkSOUD0LD_ANt7vId7aBBZ4hStm-D2BM15lmtn8Kb_wXPW3_16e2fovdwITfBPdwLTXdqV8FTBzNmIbEThovRHMCxD1O5ZaY6Xawdm4EMcut6_E3ii7XiNitgjfQGm7ca_VzqM5-RqNyxlYvSTpRfaxkM6KBL66J3hFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوت رزاقی‌نیا با واکنش دیدنی گلر السد تبدیل به گل نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106480" target="_blank">📅 22:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106479">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">استقلال چه ضد حمله‌هایی میزنه
😐
😐
😐</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106479" target="_blank">📅 22:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106478">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106478" target="_blank">📅 22:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106477">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">استقلال بدشانسسسسسسس</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106477" target="_blank">📅 22:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106476">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وااااااای</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106476" target="_blank">📅 22:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106475">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aebefadf88.mp4?token=coIVNsxPjbLNrosMtsxsWa7Ct8eVCefkZKwkEkXwsqElxLaSaI2bQnQDzIK0Vwdvlf08j5a0QDc94xzbQwC6-YIFDEUwk8wfufDpqnWZk-SwVvYJzlRDWCkBh3CQRDJ1MV0gKEvEsKLfBADFd3KvcaN40PRwZQOkDkhYwrkXAZFp50bkYwokmv0SJtV-GRe3DDG3jrMKA64FubSe4Q-AshBq7S0fHp8nN7rR4_OQVFxK9sbhDiFUHp0FPoqP1hzW_fIOG7E4J00o33rwPI9yo2hVFNPeDz3wLJ-q1zoiZvV19A8rl7RjJ9Ai4v3NCQxf6zjpWeewn85SQJ7TlpW2Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aebefadf88.mp4?token=coIVNsxPjbLNrosMtsxsWa7Ct8eVCefkZKwkEkXwsqElxLaSaI2bQnQDzIK0Vwdvlf08j5a0QDc94xzbQwC6-YIFDEUwk8wfufDpqnWZk-SwVvYJzlRDWCkBh3CQRDJ1MV0gKEvEsKLfBADFd3KvcaN40PRwZQOkDkhYwrkXAZFp50bkYwokmv0SJtV-GRe3DDG3jrMKA64FubSe4Q-AshBq7S0fHp8nN7rR4_OQVFxK9sbhDiFUHp0FPoqP1hzW_fIOG7E4J00o33rwPI9yo2hVFNPeDz3wLJ-q1zoiZvV19A8rl7RjJ9Ai4v3NCQxf6zjpWeewn85SQJ7TlpW2Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
استقلال از کووووووون آورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106475" target="_blank">📅 22:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106474">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9bbd3ca42.mp4?token=KtfZJReq3vxBFA346RN4tg2Byv96WD6PenQlPnx3P1EY-A7tpKIuXUBw04Au_0Nv5sRTkdokaaYL-svcgHabkuyziVm5f4MA9u-mh7t-zxQGJ9szSXFzNc7scKeUcGhaatAFJhxiq0F3LeV52M4-Xyn95ucq_bAU7nI2NLbrgA4RUUt-apnEBD3Zm5WnzP5hP_J_-6CdWDBRCtTkeaGxMSGAhx3ki26jcZzRj4cP7pDfqlNi37ZJICECHNf7mU-Q-zwW3eiWrOPyMCjrVorYK0MKQuenQuvN1f2OBdxuvTPEe1K5VFPwnX_0y6oON8MQ4fz_7OxaG2HkJ4nQIFnVLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9bbd3ca42.mp4?token=KtfZJReq3vxBFA346RN4tg2Byv96WD6PenQlPnx3P1EY-A7tpKIuXUBw04Au_0Nv5sRTkdokaaYL-svcgHabkuyziVm5f4MA9u-mh7t-zxQGJ9szSXFzNc7scKeUcGhaatAFJhxiq0F3LeV52M4-Xyn95ucq_bAU7nI2NLbrgA4RUUt-apnEBD3Zm5WnzP5hP_J_-6CdWDBRCtTkeaGxMSGAhx3ki26jcZzRj4cP7pDfqlNi37ZJICECHNf7mU-Q-zwW3eiWrOPyMCjrVorYK0MKQuenQuvN1f2OBdxuvTPEe1K5VFPwnX_0y6oON8MQ4fz_7OxaG2HkJ4nQIFnVLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گلگلگلگگلگلگل اول استقلال توسط یاسر‌آسانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106474" target="_blank">📅 21:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106473">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">استقلالللللللللللل زددددددددد
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106473" target="_blank">📅 21:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106472">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">😂
😂
😂
😐
🔥</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106472" target="_blank">📅 21:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106471">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آسانی زدددددددد</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106471" target="_blank">📅 21:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106470">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گلگلگگلگلگلگگل</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106470" target="_blank">📅 21:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106469">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfJiqgtHyy5NVFRBsP4CGchMOXker4mrYHgJY-nGfPOxHCmfjdGgXVeZUnFO0s5f8_sZ7FPmmtiKV1fGHIsWpwplWeEcoWuT287Jfk7uZtESY5QXHUOPU2Mw0PYddepD_hUgiMpF8IoTJN1jhM-j7AHtVc3mGx-udJwyBauG1quH8qqvMFmZ_SWq2n6M0qEXfKiqHC0lv-08MNiIhuSmXrh_E0jFgFawx-HzbEU3iy6XZ1o0HMadUwTb6G6BLndOOumYpRjfpr1PEcT7OdrX6xr8wuCprQ5iZRVZIE0UQz-37yl-dvNAUxNKO1wzR322b778zGHhSdu9CzmCdZVJpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رودری:
🔻
فکر نمی‌کنم ما مدعی اصلی قهرمانی در لیگ قهرمانان باشیم!
🔻
این تیم هنوز باید روی چند چیز کار کنه و خودش رو به سطحی برسونه که بتونه قهرمان بشه.
🔻
فکر می‌کنم بازیکنانی مثل من برای همین هدف به تیم اومدن، چون به نظرم لیگ قهرمانان مسابقه‌ای نیست که همیشه بهترین تیم قهرمان بشه؛ این رقابت، تورنمنتِ لحظه‌هاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106469" target="_blank">📅 21:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106468">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGXD-lZru2MIRaRKTC3sSuyAlozWsALIPYqUnYVEXpiZ3OcNTKmiMKLyk3U4kF5-Z--pNyAZf79Pyabt9c5C8HA0Er8Ld4-5dPqIOBYdDMF8QUBBMduFFfitZqabBYflUulE6sJYnKmPLOS37Rsv1Y6n1fN8uegnZ6_pKabP3a0n7JP4ASLU_1F_d8oV_ONNn3z-LdlDCSIEc9_ZqXHpcuIInqSQySlfn8ZM48ZtWaqygOsF0fP7cygg-TKmw1wwQqHfu_2ICUdz-VH-ZY9wAqIu3zxarZL5AefQx-NzF5UY_gexDxA8EOeEuwS3ddvoV1KlRocONWbGcc9Lh4bN7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇪
گل اول شباب الاهلی به تراکتور توسط سزار روی پاس سردار آزمون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106468" target="_blank">📅 21:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106467">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5473152a76.mp4?token=j4jrd60FH0D57EUgYPbcC33tDxY88Aurnh4l04nFbnz75KJMAsfqiN1QteF5aFPTfhYFv1cit1IAtANFa_xLB53rByUxvC40JKKn7aPH6UCIl3p3CD7f2T7dy0NunfryWySOGb8WbMeMKHgD08Z7P52XNPOyeDSWgrSKQEnh5JT3iUvOWHfUI5vWzyglIuIiCcsWIUkuwqT3oGcRi8z4SIc4F-0oxZxkaW0Fl7hQm5Fsh7AAAWLbZ64iddA9LSbFkPe202wyPZQD7Ws97MMSvip2sKgMih91OYdDnCPVcB3vl40iuZlxjGxo0tXBhiSGyLbd-8p2W9Y8CKa826AYPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5473152a76.mp4?token=j4jrd60FH0D57EUgYPbcC33tDxY88Aurnh4l04nFbnz75KJMAsfqiN1QteF5aFPTfhYFv1cit1IAtANFa_xLB53rByUxvC40JKKn7aPH6UCIl3p3CD7f2T7dy0NunfryWySOGb8WbMeMKHgD08Z7P52XNPOyeDSWgrSKQEnh5JT3iUvOWHfUI5vWzyglIuIiCcsWIUkuwqT3oGcRi8z4SIc4F-0oxZxkaW0Fl7hQm5Fsh7AAAWLbZ64iddA9LSbFkPe202wyPZQD7Ws97MMSvip2sKgMih91OYdDnCPVcB3vl40iuZlxjGxo0tXBhiSGyLbd-8p2W9Y8CKa826AYPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شوت فوق‌العاده شیری راهی گل نشددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106467" target="_blank">📅 21:13 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106466">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تراکتور تیرررررر زدددددددد</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106466" target="_blank">📅 21:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106465">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106465" target="_blank">📅 21:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106464">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d61b23910d.mp4?token=DCZJ-lAG1HN0Ulzui73bAH-EUvgtkx_EqkCTxVNz4hJtTcZUyi_iC8Uai1RmeE_bQ9_fo2PD2LFYPBVSH20cgJXHzitAxixjlVtDb9qA9cyXG_A2Zie5qEz1rTvhDDYpt-i-2-EJuSw0HIib5WgC1mQN-dwTR0oSyXndN8NfLBNk7OQbtRZR5rA4Ntr5KFfWNCMVm8LVgrsXg0jSCPH02rkhoMQ7AeF5QXDEUEgSlYpatkmuNafDV8FNGDWpS6DCZNiainxpLnDtYJ-BNGIdMrN2-GVvTL3m2KL0okeHGSwpXpa1gZgKJgM_e7eDatLtHh1XWAezBwp56WgAnPUreg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d61b23910d.mp4?token=DCZJ-lAG1HN0Ulzui73bAH-EUvgtkx_EqkCTxVNz4hJtTcZUyi_iC8Uai1RmeE_bQ9_fo2PD2LFYPBVSH20cgJXHzitAxixjlVtDb9qA9cyXG_A2Zie5qEz1rTvhDDYpt-i-2-EJuSw0HIib5WgC1mQN-dwTR0oSyXndN8NfLBNk7OQbtRZR5rA4Ntr5KFfWNCMVm8LVgrsXg0jSCPH02rkhoMQ7AeF5QXDEUEgSlYpatkmuNafDV8FNGDWpS6DCZNiainxpLnDtYJ-BNGIdMrN2-GVvTL3m2KL0okeHGSwpXpa1gZgKJgM_e7eDatLtHh1XWAezBwp56WgAnPUreg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناراحتی دانیال اسماعیلی‌فر از تعویض شدنش
ایرانی جماعت هرجا باشه غیر حرفه‌ای رفتار میکنه
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106464" target="_blank">📅 21:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106463">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9nI_dF0av-IOIQ3Esv7XWtrqLTu5L8DakDSaWW7E-fx60HDMPMO55_AsKGJhV68h7vPRIMPHlEu-IlntyuFvCPy-7YWF8QVwKaNeaN-tBSTCftXRlhH8x8eOvXVkUfQ1-2qPeCe-qUVZfo8vM1AGoJlYaCQSoDX8jacGB7ouGWsLmCca0rwgsaTMYwCARHuSlmMs5cw28VZaxYv7pdSaBoWQizZq6vS8yQGtfpvH8klXu3tORQOwn76FiOFc6UwYQ9xCwMGCqtYp0_o5LBQbNxMsdWbNRL2TByhXZiKPA1vvgWKhR864yNpJXzZKTQYpMFzjyzkgUAeLkjKPtDGLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
شماتیک ترکیب استقلال مقابل السد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106463" target="_blank">📅 20:58 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
