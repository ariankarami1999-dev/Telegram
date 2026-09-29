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
<img src="https://cdn4.telesco.pe/file/piD4lcIqYLobH8lH4Y7HkE_clKNZ6ybcG2Y1CwbQjhNN05YyuJN6If-r9CxZsi5V5_VmQqCgi-CV3pmOA0bCibVZ0H2hctQMHBAEHafqb0q2srCP0HzYinBh4SWyxmkt0WGbawyRKo1R1TjawOwKvxFyOhoQ8M-cGkWpFG2E9fsMm8JouzJoc4mmnbhxK9wEiWVQk4-fW7FpffzPGPc0oQsLH0JHbQL3vS2OGJR9llZdWAd_oos1Bp4eAUFtfL2PRKGGMOlUp2IlW4UrdhngFe_J54wGbEp4q-svt_InxqBGqah_VDUFx1ila9l9nqC-vWMMHpjyyxSNzfzYu2012Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 12:18:18</div>
<hr>

<div class="tg-post" id="msg-72456">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a809065ce.mp4?token=DQSGRWS5hOVq6ssSC1KzxAgpmjx2bxHynjrUa9DhUdJEalGS37pAlvGXttcjinS3GbPQnL73hYhIwzyBP7VryGlHnLZH_FNv5P4BQIrq8snLlaXP8othOsfdT0UPRe1q4uY3eCM90s3VSeEMoKPSF-nv2HsjXf3BySWgPYVLqBtxXR8JK4VYZBDk28_QqLts30yOsaqXLp8HvrbH4s0TTG95OIZY0qCFXHBNo-3EQvVWD0AAyC3Jx9gSS5qSTJwfgrG7ZhucegW0lLkXe4dzvXDy2YyQEKqe4JchYluEDycLsLK8cVxwansrrcI7odIMngsdaZCHUp49FBOWTqQ6zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a809065ce.mp4?token=DQSGRWS5hOVq6ssSC1KzxAgpmjx2bxHynjrUa9DhUdJEalGS37pAlvGXttcjinS3GbPQnL73hYhIwzyBP7VryGlHnLZH_FNv5P4BQIrq8snLlaXP8othOsfdT0UPRe1q4uY3eCM90s3VSeEMoKPSF-nv2HsjXf3BySWgPYVLqBtxXR8JK4VYZBDk28_QqLts30yOsaqXLp8HvrbH4s0TTG95OIZY0qCFXHBNo-3EQvVWD0AAyC3Jx9gSS5qSTJwfgrG7ZhucegW0lLkXe4dzvXDy2YyQEKqe4JchYluEDycLsLK8cVxwansrrcI7odIMngsdaZCHUp49FBOWTqQ6zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط ۷ سال گذشته! وقتی همه می‌خندیدند که این ربات‌ها چقدر دست‌وپاچلفتی بودند. با نگاهی به اینکه مدل‌های هوش مصنوعی در همین مدت چقدر پیشرفت کرده‌اند، واقعا کنجکاویم تا ببینیم ربات‌ها تا کجا پیش خواهند رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/news_hut/72456" target="_blank">📅 12:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72455">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kmp0KF6zo9TlRsVdsq7vu57Zy3oMgaquohJBX-QeqVYGvLfXyp37mTnd6lO1AoJOoF_S5FiQ_CKxhFqLKyiy73ZztkSQL9KcWBOSHUqJVfp99z4sZpA09H-raxlgOT3YYCXK6edgT8HgZmqiDoNtJH7omlyRlgaviFAPSI6hU75GXkSAZ0104BSvXrWe4HkYRAyGTQ9v87_Zix47NfQa_Hh5-w8VHj2wI1JqrBRCM4gWxdmed68nuGG_FD1bJJVMwFqQuRWfT_lFvCCew5bpY9Tv5AxopVo5TwYBu4X7C59B3RplwAzAwV_9EVRFJX_FXwz1yuDfuUinbxwqjH-4Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
قوه قضائیه جمهوری اسلامی: رای پرونده ترور قاسم‌سلیمانی صادر شده و بر این اساس دولت آمریکا موظف به پرداخت ۴۸ میلیارد دلار است!
@News_Hut</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/news_hut/72455" target="_blank">📅 11:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72454">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72454" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/news_hut/72454" target="_blank">📅 11:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72453">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFoY0CXx_-e6CUtBlvm6HJRmQJdJoHORZx9ADWw_K2aA6XQkFt1pgEXe_29m7WNvaAWTLD9Mz_ihTXRQu0gQp1jTi6D1OTnpa0CnTdL2U9Kk3q7Z5RAVGSIfNxBDDsa9WGvAhgqn48i0qWHJoJAn0gbIzWv72m0rwZ2DCLLoLoAF6RTIKTM4Cj4g35UrouVnVAsGeTuCzO9JqR0LCj1GotHcJCX1VPNDJ_PoGn0nGluT0JWUxC0dLNBx-6ZdYS-FUcQ_e_tW2NAA-18sTQMWjxM-YI8NrkfOK-h8z220_MlmEdedEdwUHuZYDyy80pIzRP4fI8KoKQHsRC17PQsNTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
انگلیس
🆚
چک
کرواسی
🆚
اسپانیا
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/news_hut/72453" target="_blank">📅 11:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72452">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دلار ۲۸ تومن شد</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/news_hut/72452" target="_blank">📅 11:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72451">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/375e130021.mp4?token=tF1hiazSuripnNVbeD05_4Jk4wE1AUPNlvW0eFD5XDU7iATSdnfYMy-kjR7FTVDwqO6z3BynGThOS0F0qaHfwvOYFO-aF5kQjqfMcmX59rl2cWsfr0PmcH96KRxgjmOuqk_R2Racs8iOoDojPOFvO8eyaxHaJqtyvcUs3omsIUD5Kj3EjSKuyQt23Mk1Pf7PBwvAXyQXkQfAAWqnOGIIPUO2ZjMheAlO5zBXIoDuC6-YzTlM8vT5RCXstY5vHJJUKNVKMC3jLREHIfC8rU4nTvuWJnrbTboy4wC2vR3F8uFul9Obx1ef7AJEXo9mSeyI1n1W2lctKNnYfOE9A23aPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/375e130021.mp4?token=tF1hiazSuripnNVbeD05_4Jk4wE1AUPNlvW0eFD5XDU7iATSdnfYMy-kjR7FTVDwqO6z3BynGThOS0F0qaHfwvOYFO-aF5kQjqfMcmX59rl2cWsfr0PmcH96KRxgjmOuqk_R2Racs8iOoDojPOFvO8eyaxHaJqtyvcUs3omsIUD5Kj3EjSKuyQt23Mk1Pf7PBwvAXyQXkQfAAWqnOGIIPUO2ZjMheAlO5zBXIoDuC6-YzTlM8vT5RCXstY5vHJJUKNVKMC3jLREHIfC8rU4nTvuWJnrbTboy4wC2vR3F8uFul9Obx1ef7AJEXo9mSeyI1n1W2lctKNnYfOE9A23aPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنندج؛ ضرب و جرح شدید سه نوجوان توسط ماموران انتظامی
@News_Hut</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/news_hut/72451" target="_blank">📅 11:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72450">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16f0cd62a0.mp4?token=MyrSEcHza9PSEbvpHn7WV_Fe6I_bSXui-Hi_AN5mRb5gsKYzBjdDX9AvmunHlYAInqeEGSEc_BYNbyOfzYVMKcL8Wd2PdJgJ2A6Y9ZFlOHH0nUJrTaXPfGFXFDDlH3hd1sqoRPw9BqaGGQLV-5WiTMZtKci8XkDJYt_jC38Xx_MAhUpIRNf7gLH16NUA_8ky4Z4kVlojVhDvKZen_LDfTPvBkD-OiNQDbw6OytQBo-zQ82unVNMo9ZKnMT7Y6mlvLudDakHcZ1V0plrXceHlgraKJMcUuNf2a2NylumkhrNtd167a_tSgqZlUgvMlqwJasrZjbSLKkTuwCCAQ22N5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16f0cd62a0.mp4?token=MyrSEcHza9PSEbvpHn7WV_Fe6I_bSXui-Hi_AN5mRb5gsKYzBjdDX9AvmunHlYAInqeEGSEc_BYNbyOfzYVMKcL8Wd2PdJgJ2A6Y9ZFlOHH0nUJrTaXPfGFXFDDlH3hd1sqoRPw9BqaGGQLV-5WiTMZtKci8XkDJYt_jC38Xx_MAhUpIRNf7gLH16NUA_8ky4Z4kVlojVhDvKZen_LDfTPvBkD-OiNQDbw6OytQBo-zQ82unVNMo9ZKnMT7Y6mlvLudDakHcZ1V0plrXceHlgraKJMcUuNf2a2NylumkhrNtd167a_tSgqZlUgvMlqwJasrZjbSLKkTuwCCAQ22N5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از یک سگ که بر اثر صدای انفجارها وحشت‌زده شده بود، در جریان حملات روسیه در اوکراین ضبط شد:
@News_Hut</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/news_hut/72450" target="_blank">📅 11:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72449">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8923a23fa4.mp4?token=M5PSG9yIBhMsvoJOU6XDNZ71N45EMdszhpuSoJvgf_8gdMQhVyyartrH-LvFoJ6E3y3RySNIeEh7v2LYb3Y1KiJFXlDT6pxA_KbNfIRK1_TxIRKwzgbZgUpbSymcKh3OlbehmrGIxliaOoqCBFqzYJ1bUGk58Lk2E5f_vinEH4lXY5oy3XeWBB7WY9Pp5lOcT6EQjHvXH8jxJBACQd04IlEru8KdDO57kIqinmHG0RC2JCZ7uS9TEcSJd148b2jJ59T2c8u_pJqqTMpUoz6BE1aYhtUNichobFATi05tbmuziUtjWkIAmT12zfNAGm4l93GfcTsYFAEXwsT0JGf-t2Rjbh44SNNO3Dv6o1jV5kZg_cCFewjvwjnASOH8H1Kx4gWnLphQZBHhUYiTkx2P4Kn20fKuvs-SKJQm5b0yPhzjrt3gFN9sDIXJUfNL2M8vQG_r-vZZ9I-GBvSQJu08BYzAJXE25OeCglXcxx4_qdftHO4jHMVQsv-St4OQN1DY99WzdO_ZmOlc6PcvSTo3Z1PRxHb_wPzjJwj_Fnn-oAV8c71ooCPdiKLljgJGUAvlDJSB9bQTCwx92lG8xDr35XefInxVXe0UIsYLPAzr1tqNsJsUYeooCWxi26SA3mSZj22-ME4KYwciAmg1mxHd8XhO4b1pjsNsr7XQrZIlh34" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8923a23fa4.mp4?token=M5PSG9yIBhMsvoJOU6XDNZ71N45EMdszhpuSoJvgf_8gdMQhVyyartrH-LvFoJ6E3y3RySNIeEh7v2LYb3Y1KiJFXlDT6pxA_KbNfIRK1_TxIRKwzgbZgUpbSymcKh3OlbehmrGIxliaOoqCBFqzYJ1bUGk58Lk2E5f_vinEH4lXY5oy3XeWBB7WY9Pp5lOcT6EQjHvXH8jxJBACQd04IlEru8KdDO57kIqinmHG0RC2JCZ7uS9TEcSJd148b2jJ59T2c8u_pJqqTMpUoz6BE1aYhtUNichobFATi05tbmuziUtjWkIAmT12zfNAGm4l93GfcTsYFAEXwsT0JGf-t2Rjbh44SNNO3Dv6o1jV5kZg_cCFewjvwjnASOH8H1Kx4gWnLphQZBHhUYiTkx2P4Kn20fKuvs-SKJQm5b0yPhzjrt3gFN9sDIXJUfNL2M8vQG_r-vZZ9I-GBvSQJu08BYzAJXE25OeCglXcxx4_qdftHO4jHMVQsv-St4OQN1DY99WzdO_ZmOlc6PcvSTo3Z1PRxHb_wPzjJwj_Fnn-oAV8c71ooCPdiKLljgJGUAvlDJSB9bQTCwx92lG8xDr35XefInxVXe0UIsYLPAzr1tqNsJsUYeooCWxi26SA3mSZj22-ME4KYwciAmg1mxHd8XhO4b1pjsNsr7XQrZIlh34" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه امیرحسین قیاسی با پسری که رتبه ۹۲ کنکور شد ولی معتقد بود ریده و پشت کنکور موند!
@News_Hut</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/news_hut/72449" target="_blank">📅 10:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72448">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvkX-Don22xBCwUJIh0RPD9Nv3p1mSwaMigFYdHhuPEQHOFeyU6qpwg0KgEU6qxgICQboHkVQbtLWiTEyvzONv3oQa1583IMyERe8n5_bVlWMwdzrwz293WYg8rf7cIzmqnjW2CUIy1gw0-YRhOkMo_jsmQz37nyu5z9uzVqtN4ffiekvI-AeShFIL_pylU0mj-PJ3BY6G3mHlIDE1j8uDXGFJyWK-gbSpv7ZwVeFTKPX4aMbt0Zv3o9hb4u9MXoQ2WIczjUqK3vhBDKuuIAefCxdtkBhq8SoSifzxs34rgm02BjoCd4O8xp1MLc1OL2dynlHRRzb-43V0TUG7Q2og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛به گزارش شبکه خبری «کان»، سفر روز یکشنبه بنیامین نتانیاهو، نخست‌وزیر اسرائیل، به امارات متحده عربی که در اصل برای هفته گذشته برنامه‌ریزی شده بود، در آخرین لحظات و پس از اعلام عدم امکان دیدار با رئیس‌جمهور امارات (محمد بن زاید) از سوی مقامات این کشور، به تعویق افتاده بود.
مقامات ارشد چندین کشور حوزه خلیج فارس، از جمله نمایندگان کشورهایی که روابط رسمی با اسرائیل ندارند، در گفتگوهایی با نتانیاهو که بر موضوع ایران متمرکز بود، شرکت کردند. نشست منطقه‌ای مشابهی نیز در جریان سفر قبلی نتانیاهو به امارات در ماه مارس (هم‌زمان با تنش‌ها و درگیری‌های مرتبط با ایران) برگزار شده بود.
هم‌زمان با سفر نتانیاهو، هواپیماهای مرتبط با نیروهای حفتر در لیبی، مراکش، قطر و امارات در ابوظبی حضور داشتند؛ از جمله یک هواپیمای دولتی امارات که از مبدأ ریاض وارد شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/72448" target="_blank">📅 09:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72447">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2070144954.mp4?token=uoed3p2z2QrlNt70-8SnCa0VI5W7de6BPSM-HjkJGzrMYPyiMzqD1pEJfJ2WmpYkJuuCLX07xGqUiVN9e4cW4qZPEV1fax_Ph4aC6ketHlMb5Fd2bNG-Ehs1Q5AzIIR76_d0_JyUFDSS0feFtHwY75oI9whvLlmOjzyT1Big2NX8zzwnWW5lOJXQNov0yCoL5yOfeq9weoHxlL_OrDilMIjgW9HL7Ks41btaZtgwFcOZ8D813FH1JzLNAvhC8mCJ3V-HmUpyp9UKD4a_TH2jfcmtkAmzMNm2temV0__-60NiWzGRm9kHd34fAsx8mNlyNh6LQbUGXZmTj9XFVKR8MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2070144954.mp4?token=uoed3p2z2QrlNt70-8SnCa0VI5W7de6BPSM-HjkJGzrMYPyiMzqD1pEJfJ2WmpYkJuuCLX07xGqUiVN9e4cW4qZPEV1fax_Ph4aC6ketHlMb5Fd2bNG-Ehs1Q5AzIIR76_d0_JyUFDSS0feFtHwY75oI9whvLlmOjzyT1Big2NX8zzwnWW5lOJXQNov0yCoL5yOfeq9weoHxlL_OrDilMIjgW9HL7Ks41btaZtgwFcOZ8D813FH1JzLNAvhC8mCJ3V-HmUpyp9UKD4a_TH2jfcmtkAmzMNm2temV0__-60NiWzGRm9kHd34fAsx8mNlyNh6LQbUGXZmTj9XFVKR8MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو به‌تازگی در برابر دیدگان میلیون‌ها نفر فاش کرد که باراک حسین اوباما به تأمین مالی رژیم تروریستی ایران و مرگ هزاران نفر کمک کرده است.
«در مورد هر دلاری که ایران در اختیار دارد، کاری که آن‌ها طی ۳۰ سال گذشته انجام داده‌اند این بوده که هر زمان پولی به دست آورده‌اند — چه در جریان لغو تحریم‌ها توسط اوباما، چه از طریق فروش نفت و گاز و غیره — آن پول را صرف ساخت بیمارستان برای مردم خود نکرده‌اند.»
«آن‌ها این پول را صرف دو کار می‌کنند: ساخت سلاح برای خودشان و صدور انقلاب!»
«آن‌ها این پول را صرف تأمین مالی حزب‌الله می‌کنند. صرف تأمین مالی حماس می‌کنند. صرف تأمین مالی شبه‌نظامیان شیعه در عراق می‌کنند. بله، این‌گونه آن را خرج می‌کنند. آن‌ها این پول را برای حمایت از تروریسم و توطئه‌های ترور در سراسر جهان به کار می‌گیرند!»
«[ما] مانع دسترسی آن‌ها به پولی می‌شویم که قرار است برای کشتن آمریکایی‌ها استفاده کنند.»
اوباما پول نقد و لغو تحریم‌ها را برای ایران فرستاد و آیت‌الله‌ها آن را به موشک و تروریسم تبدیل کردند.
رئیس‌جمهور ترامپ دقیقاً برعکس عمل کرد و جریان پول را قطع نمود و...
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/72447" target="_blank">📅 09:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72446">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb7b6e5b41.mp4?token=KST8wMGGynLPDrlymE6LEWJrkEWMx7vxApQvazxMYPHKAHOzPlG_I8PFm6UrZyDE7Kp39yQwHBdEfRaDWztGy1fDcBSFwXHSOBhxIfLVZeHancUIhwjRACNzbuTlPw632TVOEUdkIXCJRiCuda9Lkr_aIIciD8KvAnf9ga6SokrBipFr1PYxxvL3d0cRy-KB4FWZDcLPJpiD7EtS_1qjX5oM7XRimYIYvOIUfw8fYPVtHSRbJ4FULoMa3qxBH4kbzf2kaLqw6oFrMrKGpIoul-0L3OEs6MPjYC3FEIkx8vbPZD2RcuLZNc_O3NI6MiY-JsGE-axSrKIBfxWGhGllQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb7b6e5b41.mp4?token=KST8wMGGynLPDrlymE6LEWJrkEWMx7vxApQvazxMYPHKAHOzPlG_I8PFm6UrZyDE7Kp39yQwHBdEfRaDWztGy1fDcBSFwXHSOBhxIfLVZeHancUIhwjRACNzbuTlPw632TVOEUdkIXCJRiCuda9Lkr_aIIciD8KvAnf9ga6SokrBipFr1PYxxvL3d0cRy-KB4FWZDcLPJpiD7EtS_1qjX5oM7XRimYIYvOIUfw8fYPVtHSRbJ4FULoMa3qxBH4kbzf2kaLqw6oFrMrKGpIoul-0L3OEs6MPjYC3FEIkx8vbPZD2RcuLZNc_O3NI6MiY-JsGE-axSrKIBfxWGhGllQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
مشکل اصلی در مورد ایران، «انقلاب» است؛ نه آن مقامات دولتی کت‌وشلوارپوشی که در برنامه (Meet the Press) شبکه ان‌بی‌سی ظاهر می‌شوند و در رسانه‌های آمریکا بی‌هیچ دردسری تریبون رایگان در اختیار می‌گیرند!
«بحث ما درباره آن‌ها نیست؛ کسانی که در ایران حرف آخر را می‌زنند، روحانیون شیعه تندرویی هستند که دیدگاهی آخرالزمانی نسبت به آینده دارند.»
«آن‌ها معتقدند که رسالت مذهبی‌شان این است که آغازگر وقایع پایان جهان و آخرالزمان باشند.
این واقعیت است؛ این هدفِ اعلام‌شدۀ انقلاب آن‌هاست. چنین افرادی هرگز نباید به سلاح هسته‌ای دست پیدا کنند، چرا که از آن برای باج‌گیری از جهان و کشتار مردم استفاده خواهند کرد. این ریسکی غیرقابل‌قبول است.»
ترامپ دارد کار درستی برای جهان انجام می‌دهد. او اکنون به دنبال کسب پیروزی کامل بر ایران است، زیرا این تنها راه چاره است!
بانک‌های مرتبط با ایران در حال تعطیلی هستند، ترامپ عقب‌نشینی نمی‌کند و ایران قادر به صادرات نفت نیست.
اوضاع کاملاً علیه آن‌هاست. هرگز نباید سلاح هسته‌ای داشته باشند!
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/72446" target="_blank">📅 09:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72445">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c2b12f18e.mp4?token=WveYKojzOEZvI0lfABEFwI-mkbRZ0FAWO-scA-JGZ16-Mo3xfvp2FO5a_a_76ofuCFxjLFiOD1i1D-8a7_SOM-i5JKV3gWAZ36PoNKQa_dSedn52u4DKkW7wNZQOaWlsqLQrmZoXCpLTglXLRSFvh6S_QWBtFSjY8c-iEKbD-D69Jh9WWcO_4HDf3clIoVVkwV9gohC89_eH5WZngTciqU590j1OX4RSolUkck45b2k2ByX7EohC7QzwLpCvWrT055u2t02c249BW2gEi2vK_KrJsMONMIQa4bDJt-X_ncPxKnfPwYnjTNLmf3uGZwloiPbnlfDCI7xAtloSqTRqiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c2b12f18e.mp4?token=WveYKojzOEZvI0lfABEFwI-mkbRZ0FAWO-scA-JGZ16-Mo3xfvp2FO5a_a_76ofuCFxjLFiOD1i1D-8a7_SOM-i5JKV3gWAZ36PoNKQa_dSedn52u4DKkW7wNZQOaWlsqLQrmZoXCpLTglXLRSFvh6S_QWBtFSjY8c-iEKbD-D69Jh9WWcO_4HDf3clIoVVkwV9gohC89_eH5WZngTciqU590j1OX4RSolUkck45b2k2ByX7EohC7QzwLpCvWrT055u2t02c249BW2gEi2vK_KrJsMONMIQa4bDJt-X_ncPxKnfPwYnjTNLmf3uGZwloiPbnlfDCI7xAtloSqTRqiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
اگر رئیس‌جمهور ترامپ اجازه می‌داد ایران به سلاح هسته‌ای دست یابد، نه تنها همه او را مقصر می‌دانستند، بلکه ایران کنترل کامل تنگه هرمز را در دست می‌گرفت.
درحال حاضر تقریباً همان‌قدر نفت که پیش از این مناقشه جریان داشت، از تنگه‌ها عبور می‌کند؛ به استثنای نفت ایران.
«آن‌ها می‌توانستند تنگه‌ها را کنترل کنند، حق عبور (عوارض) تعیین نمایند و تصمیم بگیرند که چه کسی در این سیاره انرژی دریافت کند و چه کسی نکند. اگر آن‌ها سلاح هسته‌ای داشتند، دقیقاً همین کارها را می‌کردند.»
«اگر ایران سلاح هسته‌ای داشت که می‌توانست با آن همسایگان و جهان را تهدید کند، هیچ‌کس نمی‌توانست در مورد تنگه‌ها کاری انجام دهد.»
«۵ سال دیگر، همه می‌گفتند: "باورم نمی‌شود که اجازه دادند ایران در پناه یک سپر متعارف، برنامه تسلیحات هسته‌ای خود را بسازد و توسعه دهد!" وحالا شاهد حضور یک کره شمالی دیگر در خاورمیانه بودیم. ما در آستانه چنین وضعیتی بودیم! این همان چیزی است که رئیس‌جمهور مانع وقوع آن شد.»
«وبدتر اینکه، صحبت از رژیمی است که در جریان آن به اصطلاح انقلاب، ده‌ها و شاید صدها هزار نفراز مردم خود را قتل‌عام کرده است!».
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/72445" target="_blank">📅 09:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72444">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">عراقچی:
امروز (دوشنبه) یکی از واسطه های قطری دیدار مجددی با ما داشت، بحث هایی را انجام دادیم . روی ایده هایی صحبت کرد و اینکه چگونه می شود برای تحقق شروط ایران راهگشایی کرد و چگونه این شروط را محقق کرد.
ایده هایی داشتند و بحثی را داشتیم که باز با طرف آمریکایی هم مطرح خواهند کرد و بعد پاسخ نهایی طرف آمریکایی پس از آن به ما منتقل می شود که امیدوارم تا فردا (سه شنبه) این کار انجام شود.
من چند ساعت دیگر به سمت تهران پرواز می کنم و پاسخ را قطری ها هر موقع که داشته باشند، می دانند که چگونه به دست ما برسند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/72444" target="_blank">📅 06:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72443">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72443" target="_blank">📅 01:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72442">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/72442" target="_blank">📅 01:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72441">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRfqPP-OFb2FkeT4WVYAWqS-6ymgO0ppSlGMzs_tlZPqqmCfYkX8bDHqpnwGXNHdUkd_VQGUV9SrS9z1-OmvTJrsLkx3jEoKLq0Tiw3XcKUCk1fFCjfQppjQPVLhcZPWvTxf-5467fwb13nDZcLzeiTlKNIr32NB3nS25xIQOzi6iCIlXwKf6BcYEpPq7sw-ob5f1RO33OH0woBPmFVuCrMXBAg2OlRfYWqy1UOsMzvJX8VSW03MSyT0ueKNY7K7B90VvNsZoIocVCf-9RXMAxKrolfoGTz_Ua8EJp6excTrx3tD30WsagW3MbpvFxfBnceTFmeEnx-nMoY-nJnhJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام امریکایی به باراک راوید گفت:   رئیس‌جمهور ترامپ مایل است در ازای پیشرفت‌های ملموس در پرونده هسته‌ای، تحریم‌های ایران را کاهش دهد و وجوه مسدودشده را آزاد کند.  @News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72441" target="_blank">📅 01:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72440">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLr6PtJKMNyuB49FEOCfaLPbaMoZzHNPPUa5AfdMCRmla30ryaQqm3lDiEpHLlK0Enr6pfSdyi4We8qy-AmptUi_n6Bolx6PI_oiiALcWHcQ70n0ByDsLB0ydB5rGM2YzyujjgY3VuI2jmG8VLRjG1-oC7etNLtfYteuWN5xuV3QCbe7pNEthPQYoQwFzbl2YXX9BefTacykTFitimKkOVVckLpM7DMHgvx11sA6pl1gTt9fyjA-RvUo0saiFlTj2obLnjhYsPcQ1JBtmGi-kwhMuFnON9YB79qVc4z_VTIGqzns0Lo8nVyP9CBLvLCsqAEldUErkeQYFaCRF34gFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر نخست‌وزیر نتانیاهو:
نتانیاهو و همسرش دیروز به دعوت شیخ محمد بن زاید، رئیس امارات متحده عربی، از این کشور دیدار کردند.
در این سفر، رئیس شورای امنیت ملی، رئیس موساد، منشی نظامی و مشاور سیاست خارجی، نتانیاهو را همراهی می‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72440" target="_blank">📅 00:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72439">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نقشه‌های گوگل تصاویر ماهواره‌ای پیش‌فرض خود برای غزه را به تصاویر ژانویه-فوریه ۲۰۲۶ به‌روزرسانی کردند و مقیاس تخریب را بلافاصله برای هر کسی که برنامه را باز می‌کند، قابل مشاهده ساختند.
کاشی‌های ۲۰۲۶، بلوک‌های مسکونی متراکم در رفح و خان یونس را نشان می‌دهند که به مزارع آوار خاکستری تبدیل شده‌اند، منطقه بیمارستان الشفا به شدت تغییر یافته است و اردوگاه‌های چادری عظیم در زمین‌های باز باقی مانده قرار دارند.
آخرین آمار UNOSAT: ۲۰۱,۲۹۰ سازه آسیب‌دیده (۸۲٪ از کل ساختمان‌ها)، ۱۳۴,۴۲۲ سازه تخریب شده.
این تصاویر حدود ۲۳۵ کیلومتر مربع را با وضوح حدود ۱۳ سانتی‌متر پوشش می‌دهند - به اندازه‌ای واضح که می‌توان دیوارهای جداگانه و خوشه‌های چادر را مشاهده کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72439" target="_blank">📅 23:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72438">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa72acf92f.mp4?token=ahFLedcwVzS5YryEku8pAEPU8bFwhp_mYg1uH8TOwBNI82kCqfcC3IPKVveAaHjm2OnuJEqk6EUZay4HOnakxpEfhMVq0zTlDLD7je64zknQ29DOo962AkmnDPaepuWswRzaOkHjKo4bK0FR8UxSSmwSYufWoqaQ_EeRekzgNx-_CtZLoHf8aM12U2y4r4zJXuVwm6AmIq2XbPIu6S7S4_VNnILiMVtBmwCIryOm9SWTtSncqTuh1I8dbUKPwrRdv9sKA6JWasgBNS7PvDX5wy0fcPFgxBX07xENAjJbfkP8U0xvvDH2XupkvrKy-bmypnRThM6yqmS679djjs6Eow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa72acf92f.mp4?token=ahFLedcwVzS5YryEku8pAEPU8bFwhp_mYg1uH8TOwBNI82kCqfcC3IPKVveAaHjm2OnuJEqk6EUZay4HOnakxpEfhMVq0zTlDLD7je64zknQ29DOo962AkmnDPaepuWswRzaOkHjKo4bK0FR8UxSSmwSYufWoqaQ_EeRekzgNx-_CtZLoHf8aM12U2y4r4zJXuVwm6AmIq2XbPIu6S7S4_VNnILiMVtBmwCIryOm9SWTtSncqTuh1I8dbUKPwrRdv9sKA6JWasgBNS7PvDX5wy0fcPFgxBX07xENAjJbfkP8U0xvvDH2XupkvrKy-bmypnRThM6yqmS679djjs6Eow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن‌ها دیوانه‌اند. هیچ شکی در آن نیست. آدم‌های بسیار دیوانه‌ای هستند.
من همیشه به آن‌ها می‌گویم: «شما دیوانه‌اید، رفیق.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72438" target="_blank">📅 22:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72437">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de98b8705f.mp4?token=UgsTrndmpljjO_A4Uq3l70U_0-3poavg_ta6u8unf84JkZfd03oaF-Ol2_9uj28-O391NfxT90ZGGvaDK98W0c6z2kTmOG6UVv1am2JsjL6kudGGNStwPmrkb1Z5prRe2zTdV4uYaUmPS3kp8ns8m1bXCq4-X4XrJajrvkgG4zli7-mNjla_BlQ6YNKGlq3d_xbp_pcYB25RvxflCArZwEM_X-nTZt-_XBpdBU7xP1hPLw8BOdDYvXolQcYt5ON0Vpe6TyMbQ0aFknKbym9_pwm-aTBxRupPQJd9PR7_PEho1xcJrg0WLxDM0QcKHllZuVOteENlmxQrT91-589pbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de98b8705f.mp4?token=UgsTrndmpljjO_A4Uq3l70U_0-3poavg_ta6u8unf84JkZfd03oaF-Ol2_9uj28-O391NfxT90ZGGvaDK98W0c6z2kTmOG6UVv1am2JsjL6kudGGNStwPmrkb1Z5prRe2zTdV4uYaUmPS3kp8ns8m1bXCq4-X4XrJajrvkgG4zli7-mNjla_BlQ6YNKGlq3d_xbp_pcYB25RvxflCArZwEM_X-nTZt-_XBpdBU7xP1hPLw8BOdDYvXolQcYt5ON0Vpe6TyMbQ0aFknKbym9_pwm-aTBxRupPQJd9PR7_PEho1xcJrg0WLxDM0QcKHllZuVOteENlmxQrT91-589pbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
اگر می‌خواهید هرج‌ومرج را ببینید، بگذارید شهری را با سلاح هسته‌ای نابود کنند.
من فقط درباره اسرائیل و بخش‌های وسیعی از خاورمیانه صحبت نمی‌کنم.
بگذارید با سلاح هسته‌ای به ما حمله کنند؛ خطاب به همه آن آدم‌های احمقی که فکر می‌کنند این کار اشکالی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72437" target="_blank">📅 22:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72436">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/530a31d83d.mp4?token=jZuzhUaXNFFtM47QKe-Gx_hmBDjhGhnNJW-gdmiJ2hMsxk0CLGxHdPSWi4JB597q-p58dXIPL53CP6EBE-YiGq6Cggo9VxipBiZKCTLg4YvmzVQpnccH_lM_aQXm32mlXutmuUkUW-MyCcrzsfqDqBEKz5tMuVq18Y_y78l1VP7gg5mhkcbkQl614BAuXjapBOwWrNxhouZdkAjHksMClPojX4oewz5hjmRClDDZF_fEQh3jyf3Wjb3NxyLrVengFqiVgXbWjGE9AlGZrOW4-V6RhpcBJCUDyW07le6dHfzcaqjkF4spqxZh4sE-1XPQRbaEBngIzXCWN6ub9eFpyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/530a31d83d.mp4?token=jZuzhUaXNFFtM47QKe-Gx_hmBDjhGhnNJW-gdmiJ2hMsxk0CLGxHdPSWi4JB597q-p58dXIPL53CP6EBE-YiGq6Cggo9VxipBiZKCTLg4YvmzVQpnccH_lM_aQXm32mlXutmuUkUW-MyCcrzsfqDqBEKz5tMuVq18Y_y78l1VP7gg5mhkcbkQl614BAuXjapBOwWrNxhouZdkAjHksMClPojX4oewz5hjmRClDDZF_fEQh3jyf3Wjb3NxyLrVengFqiVgXbWjGE9AlGZrOW4-V6RhpcBJCUDyW07le6dHfzcaqjkF4spqxZh4sE-1XPQRbaEBngIzXCWN6ub9eFpyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا رویداد پایگاه «آر.ای.اف. فیرفورد» (RAF Fairford) به ایران ارتباطی دارد؟
ترامپ: ممکن است مرتبط باشد، اما باید بگویم از اینکه آن‌ها را آزاد کردند، تعجب کردم. من چنین کاری نمی‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72436" target="_blank">📅 22:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72435">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ccb54f2ff.mp4?token=FlI6QPD5OIjc3DBpn-OQpPP102oPA1rLM_9j8izDV9s8-HoTzCBIlrkcI9ZuLILShXmG1getqItR6erLTOZqcf9ASgA3PAtj41mkOcI3uoP0QPYlyC1WqcRGMgPOyIxhfnQQtmdG5EDhaVfFBlN3TjfLS7AsfwEymwk-O71P7xbtEsiMLQzt20aEDSRtYpL7EyZ0QLkhtK6_seBCop_8Wt6B3lpwDzettCGdqimxk2WzdYVUUXke-gNGANrKK5Vf5Dz2rDJCL9UPSeOhfZHdNXbtA0SE-l9bnvl-UPigY04OMhk5pQMyAQFs72OgCGPYtJi8K1auTUyhe8nS3Rrh7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ccb54f2ff.mp4?token=FlI6QPD5OIjc3DBpn-OQpPP102oPA1rLM_9j8izDV9s8-HoTzCBIlrkcI9ZuLILShXmG1getqItR6erLTOZqcf9ASgA3PAtj41mkOcI3uoP0QPYlyC1WqcRGMgPOyIxhfnQQtmdG5EDhaVfFBlN3TjfLS7AsfwEymwk-O71P7xbtEsiMLQzt20aEDSRtYpL7EyZ0QLkhtK6_seBCop_8Wt6B3lpwDzettCGdqimxk2WzdYVUUXke-gNGANrKK5Vf5Dz2rDJCL9UPSeOhfZHdNXbtA0SE-l9bnvl-UPigY04OMhk5pQMyAQFs72OgCGPYtJi8K1auTUyhe8nS3Rrh7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره ایران:
ما خیلی زود در آن جنگ پیروز خواهیم شد. ماجرا تمام می‌شود و قیمت بنزین به‌شدت سقوط خواهد کرد.
هیچ‌کس دیگری نمی‌توانست چنین کاری انجام دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72435" target="_blank">📅 22:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72434">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/323953406a.mp4?token=JBKI3ELqpQ4DNKmMbgcbebpuFSkk4LG8giTdF6ZB29Y7e9_00z5jr7FOHCj6Njf7F2LUEQsc8pom4lhA2IK7hONr64s9vlHCi771KexxT_dKVmB-OmVFT3x078oHoo1UYHyq6QmgyVR5w_2Lp-8hMfFEWxIbKWnGscBwjasLl8-D8Rws-vkOTWy6e0XzV0pG6DXfHwve__0ohzzutA-dwEyq0swJpqY-SxkzEwrbzGB8mQB3NAULFG7iWqWMsBCxsBIhkVHeIsUgo1xFHiT2nmMjJPK4UMQQYRt4j7wMTzF5K8PD4Pu-YYhpJsT3s9ZxonPaBw965zUNrFGSnAwckg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/323953406a.mp4?token=JBKI3ELqpQ4DNKmMbgcbebpuFSkk4LG8giTdF6ZB29Y7e9_00z5jr7FOHCj6Njf7F2LUEQsc8pom4lhA2IK7hONr64s9vlHCi771KexxT_dKVmB-OmVFT3x078oHoo1UYHyq6QmgyVR5w_2Lp-8hMfFEWxIbKWnGscBwjasLl8-D8Rws-vkOTWy6e0XzV0pG6DXfHwve__0ohzzutA-dwEyq0swJpqY-SxkzEwrbzGB8mQB3NAULFG7iWqWMsBCxsBIhkVHeIsUgo1xFHiT2nmMjJPK4UMQQYRt4j7wMTzF5K8PD4Pu-YYhpJsT3s9ZxonPaBw965zUNrFGSnAwckg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
اگر جمهوری‌خواهان کنترل مجلس نمایندگان و سنا را به دست بگیرند، به هر فرد بزرگسال پنج هزار دلار پرداخت خواهد شد؛ و ما می‌توانیم این کار را انجام دهیم.
دموکرات‌ها نمی‌توانند چنین کاری کنند، چون هیچ درآمدی ندارند و ما را به سمت رکود اقتصادی سوق خواهند داد؛ آن‌ها پولی در بساط نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72434" target="_blank">📅 22:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72433">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/979f299405.mp4?token=aWgkFLSPEuTK-zLnY5G8-iNEXLcef8wB9r7DWVuQWL0XHjQorYWUrb6jkYlvgbGcbktdeqdxt-Lpvc4RtK91qxC2F1SDt3g1AocfE98SMfPOKDPsFKB9YUpnjOmj_5vf1TTCca7QzuX0FwWV--GxcrlL7TTRJNyv2hNCXiF3rQTZOK1h4wncOJH-LebKgvL3DIi2HgEH4b-TZEWbJfBlxwgwjDYtPNp7lyrKAzbNToeINgYEFldBNUef98vH1oLYYwVpCzN86cbFf9gBi45_o_2xtnbjJqFF9XwWpqvVkPG5NsT32cEwaE1p3t7OZlXjhgpoSlDleGmBmvDRTwVUWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/979f299405.mp4?token=aWgkFLSPEuTK-zLnY5G8-iNEXLcef8wB9r7DWVuQWL0XHjQorYWUrb6jkYlvgbGcbktdeqdxt-Lpvc4RtK91qxC2F1SDt3g1AocfE98SMfPOKDPsFKB9YUpnjOmj_5vf1TTCca7QzuX0FwWV--GxcrlL7TTRJNyv2hNCXiF3rQTZOK1h4wncOJH-LebKgvL3DIi2HgEH4b-TZEWbJfBlxwgwjDYtPNp7lyrKAzbNToeINgYEFldBNUef98vH1oLYYwVpCzN86cbFf9gBi45_o_2xtnbjJqFF9XwWpqvVkPG5NsT32cEwaE1p3t7OZlXjhgpoSlDleGmBmvDRTwVUWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یستنیتیاساتتیاایایایایایایایتبتیتیایتتیتیابتیتبتیتبتیتیتنین</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72433" target="_blank">📅 21:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72432">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLbV8WX7CrQDm-GkboSWJBrimaQ4r1dPQmmxstmj97hplDgmDxQluwKim_TgT3CkV5_RVRwaPUClzmsR5XoGsGQplVMcEsO-vSY5Qj4nolfm90o_qZmWbyzKFDhiuYQUCno8ddpk6dEksNokLWsXoWyg_cOulyaPe0yxwzWvLm__bYAkNVm7XBZQTD95Wkpb2JkipbUR3DGG6tfSuJ2TziTfjVjKXIAXn7ZeV_1A9RaT6vDw2NRFlHih3u1m4KWL-D50Z0RHMzplp1Qk74dgneinUV6utvEjNdjaMzB9zeKdvjQbJ5UIGkz35C8ZdRBW_lSQALwY4cYsgxHU93ODZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
«عملیات طرد اقتصادی» باعث شده است ارزش ریال به پایین‌ترین حد تاریخی خود برسد.
ما به تضعیف توانایی رژیم ایران برای تأمین مالی تروریسم و توسعه سلاح هسته‌ای ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72432" target="_blank">📅 21:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72431">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heTpWD5H-YvquWoVYxwE6K_TdCJ1SmlWVV1hA1tOEDnkqa9mU77hA4mtLldsFVbHjvEsdCpYe0n7lAZsR5Uu5VEMcniaj6e6lowX6kY4Hn5kt1xsx4kuyHx8FKxGl6JAQ2toF-m6vm_uTSi5fjqedWyVayQVJ9WaIUeXUbKqmJaFgSs9BlSG0v-OZ9KlnkuzC6_axkSJMO84m7YueGXa6jMIXN0uGx0LDji_k5-LuJ0pExrIpzpkJFWD_jEPK2d1zgq_sLgSiamGR4vCelOFnGt4o5IYvIrXWpkIHW0214qMZsHoy4uUVX6k3Uk0xc-VruCuu2DYrJ2f_Ptmo_i1Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک منبع آمریکاییِ دخیل در مذاکرات با ایران به العربیه گفت: احتمال دستیابی به توافق بسیار ناچیز است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72431" target="_blank">📅 20:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72430">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dwi15ds9jGud7dqj7PeA7U5HF4Nvsl9bvBcRyaHDvLwfbF3N5-h2L1HRzDZ_vQVN6ATeMx8pUOB-Yv1kZJLoJIa6dL7ct4ZTtmlTFbPTfuk0k8VtcK3hSdZfxMaHHFGQt1V4Yh9gLmw2YBuRm9bqQu-wl_IxTQ48QRr0usE9m17cWxGwW-C4axb_BVlVxNjsu-r-zYln0k3fiUSmAMFrrqwxRejU2a9bHAiKDy--aEAs9OGqZroc5uTnh0bMVQl1d0revh0eW230ig0a4tpkKMMQ8d1SQ8ZUziC8xCdJYLmq4DvdgIPGZKh7waLu5RuF7l_GQ48n79Jxds9JNFUECQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام امریکایی به باراک راوید گفت:   رئیس‌جمهور ترامپ مایل است در ازای پیشرفت‌های ملموس در پرونده هسته‌ای، تحریم‌های ایران را کاهش دهد و وجوه مسدودشده را آزاد کند.  @News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72430" target="_blank">📅 20:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72429">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291ffe2bc9.mp4?token=ctiW7clvt5ef5V2tPgz0wI2m8wjepNfIa9V5kJ8HDiMOVM42KkJBi534Z-VRGZOmoE57rGjJyiFiw4_IdBExAUvLnicGSQ9vubQTjAoPkbkhcKXqpviNyRjegOyCVLY07yvlkquSmWUth3mZQAPG1HDLggCvJ1vtGRuRpIczKnERbE6lQP8E9bLLZVobNEb-VjA4Lee1GsgwFrfHF5AHXkBSCtJganGSBDSnlQYpko6rOciYsOVhv4hr9KGvYT07BlXnWCOofWy2cKTXyZ8Qu5BB92PVo-Ouc3v6TCHErajTZhEd0V8TC_u-5PUzo3-hcvrS9I2oJo1eND9eHWmdHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291ffe2bc9.mp4?token=ctiW7clvt5ef5V2tPgz0wI2m8wjepNfIa9V5kJ8HDiMOVM42KkJBi534Z-VRGZOmoE57rGjJyiFiw4_IdBExAUvLnicGSQ9vubQTjAoPkbkhcKXqpviNyRjegOyCVLY07yvlkquSmWUth3mZQAPG1HDLggCvJ1vtGRuRpIczKnERbE6lQP8E9bLLZVobNEb-VjA4Lee1GsgwFrfHF5AHXkBSCtJganGSBDSnlQYpko6rOciYsOVhv4hr9KGvYT07BlXnWCOofWy2cKTXyZ8Qu5BB92PVo-Ouc3v6TCHErajTZhEd0V8TC_u-5PUzo3-hcvrS9I2oJo1eND9eHWmdHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ساعتی پیش سرمایه دارای میلی گلد ریختن تو شرکت میلی گلد و رسما دارن مسولین شرکتو کتک میزنن و هر چی میبینن خرد میکنن و فقط صدای عربده و ناله از توی میلی گلد شنیده میشه :
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72429" target="_blank">📅 20:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72427">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یک مقام امریکایی به باراک راوید گفت:
رئیس‌جمهور ترامپ مایل است در ازای پیشرفت‌های ملموس در پرونده هسته‌ای، تحریم‌های ایران را کاهش دهد و وجوه مسدودشده را آزاد کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72427" target="_blank">📅 20:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72426">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سرعت آپلود بین‌الملل رو انقدر آوردن پایین که عملا دیگه نمی‌شه چیزیو تو تلگرام آپلود کرد!
#hjAly‌</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72426" target="_blank">📅 19:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72425">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DfSCzyHogaR6TOj6w26aN50H3bAJu8w_d84JH_3_ISkD_FdhIjVQlm0m8BETCwxRiuWDN4T96Ym7wtbePtcn1U-Fv-wwWCJtSlkpQj7WvemjGN9uR5CeI8_0ChLHpnfCop1TKeNq6fDhBB5xK815-KccnDkkKaC3hfw8iOFWpast0-ud0cDUQI2QshUKuG-7M3_lBaTCNMk-ewB8Re2uVP0CNhUF2ulIHH2UXzgtX2ZBbQYb9H-Fz704-mCWGEgbOhJ-tfTJf2u4zudnm3-bZAY2-bJi_iK9FzCY83g2IkFrQQvcsTvXHrIno_6gKjNIbe5ZIUorqzgJjw9uVNB6Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهریه بین عرزشیا
❌️
مذاکره بر سر تنگه هرمز
✅️
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72425" target="_blank">📅 19:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72424">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دونالد ترامپ امروز دوشنبه ۲۸ سپتامبر ۲۰۲۶ ساعت ۲ بعدازظهر به وقت شرق آمریکا (ET) در دفتر بیضی‌شکل یک «اعلامیه» (Announcement) خواهد داشت و خبرنگاران کاخ سفید نیز در آن حضور دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72424" target="_blank">📅 19:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72423">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCpPN75qewa55-ilUPG0SjeRRFl_wBrBAtjrjURwbP68lVb69fDLm31AsZkyAA2C0YYQzWSFLFtGlHID-4I6v9zARkPvjP-yRBdKiBRCL5et6_X2XaagmE-B9TlkUNJMeaiIClgsZlX9EfDpZNM-TE0N8wT2oXN2A5VG-pSht0HgNv7YvCvgsLr4NZf_6PwmuqGrph53z1t24v3dIg1bkRRX5_ZTewbf2J4xaudSNYk1o0xvXIwIFQch21ASY9be2C0cGAwoF2KRbQtetgYth6UKD79B-2s50qQM32z9_ntqjGDkkqtPj7kulFlt_aMbo-CD6pQeu-rPYAtT7mRluA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی به زندان اوین تحویل داده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72423" target="_blank">📅 18:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72421">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">#مهم
:چندین فروند جنگنده F-22 Raptor طی ۳۰ دقیقه گذشته از پایگاه نیروی هوایی «لنگلی» (Langley) برخاسته‌اند. (1)
علاوه بر این، سه فروند هواپیمای سوخت‌رسان KC-46A نیروی هوایی ایالات متحده نیز در آسمان هستند که احتمالاً وظیفه پشتیبانی از انتقال این جنگنده‌های رپتور به خاورمیانه را بر عهده دارند (2):
- GOLD21: KC-46A (شماره ثبت: 17-46034)
- GOLD22: KC-46A (شماره ثبت: 16-46021)
- GOLD31: KC-46A (شماره ثبت: 18-46051)
@News_Hut
| AirAssets</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72421" target="_blank">📅 18:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72420">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72420" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72420" target="_blank">📅 18:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72419">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLtRuj0cIeja9XDfSCyXlU-SjFXymLafLVnZW71FudimNNW3LtObY1Tf0quW37Yvia5Ue7GHtuA7DEwVobURBIMx_dbb_AHQlovVNRrbPtMVDS1W2GLsYt1ihSS-rPpESyD4Pu5OorzQNIFLt2qyNoxPcaTPfIQ80K-NBDlTWxaipB4CYWJgLWyao6YvJzeYGzqCTqZfv9JCICyKo1u675xEsZZA5Mhft1ADMhGY4b6bXbjeVMIUVgOjx8PsX_T-gdBhc5nr_u6991tFykht7NC8Wu2RkvzP6l9CUvS-IGQNnqtGs_L3YE8wsQfScKPYDHpr67SXWt_qa_VPchd9-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72419" target="_blank">📅 18:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72418">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdfe5220c3.mp4?token=jgMCpDAMdZDslUobBE6yeLu3ZKczoC9cMOa_fhzZryV1W3R_fWI1wYJPk-xFKLI8ULt3Ym7rcpSBeLjoMtH_6kIiwMCXm0MXcQxwTTdsCgOyMbrsvXLRR9YnEVEb0SN4uRS29qiDBD0rpOXge8C7TjROk4n7vB6SLiJ19nTDWnY-TfKqnlZuFfb4nZLX95bz5_zdfEeiO10S9px-OSwK5GW0j9kixaoO8fvz_XYN6OVHt49Ynd0SvgUIhsGa0pvY79CsZr4_rbaDaNY1nQkFSXPosfalO62WbercdDGYzne9gWM6sL4NtJWyy2-daAa4gODwzMRHiRlaasnL4oeV4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdfe5220c3.mp4?token=jgMCpDAMdZDslUobBE6yeLu3ZKczoC9cMOa_fhzZryV1W3R_fWI1wYJPk-xFKLI8ULt3Ym7rcpSBeLjoMtH_6kIiwMCXm0MXcQxwTTdsCgOyMbrsvXLRR9YnEVEb0SN4uRS29qiDBD0rpOXge8C7TjROk4n7vB6SLiJ19nTDWnY-TfKqnlZuFfb4nZLX95bz5_zdfEeiO10S9px-OSwK5GW0j9kixaoO8fvz_XYN6OVHt49Ynd0SvgUIhsGa0pvY79CsZr4_rbaDaNY1nQkFSXPosfalO62WbercdDGYzne9gWM6sL4NtJWyy2-daAa4gODwzMRHiRlaasnL4oeV4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردادن شعار«تا آخوند کفن نشود این وطن، وطن نشود»در اعتراضات امروز دانشجویان دانشگاه علامه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72418" target="_blank">📅 17:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72414">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb09e58e0.mp4?token=XGTMMIHEze8PBkIGeN1K0rolyuEHJ8nH0yxe3mBvUhdCGNO0zYYtg2XTcmZZe-gdMLQklZXW2HMc_XmNlBI-5EC6_7_jf_6Mfc0ka-ozGIdxSdGoCgyGTW1x2BB1cuQU60VhxDV4Y26fs1xDFCgp0NJl35ysKLUPIux05TJa8Xdfi1TDbqFwXXNLDXobkuGcCfzYvqetYaz8raHdlhAwU-0UHMJpeyWI5Sc5GK3vy2TjaEY5D9X3Z2NpJPCx_Nx5UmefWdMybjvVnUpzUUdjYCLWNN947nDTYrXLil6tq0ANEvaijSMWr1Ra95mvaA60PHBgA3ujlTnFPLCSalgh6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb09e58e0.mp4?token=XGTMMIHEze8PBkIGeN1K0rolyuEHJ8nH0yxe3mBvUhdCGNO0zYYtg2XTcmZZe-gdMLQklZXW2HMc_XmNlBI-5EC6_7_jf_6Mfc0ka-ozGIdxSdGoCgyGTW1x2BB1cuQU60VhxDV4Y26fs1xDFCgp0NJl35ysKLUPIux05TJa8Xdfi1TDbqFwXXNLDXobkuGcCfzYvqetYaz8raHdlhAwU-0UHMJpeyWI5Sc5GK3vy2TjaEY5D9X3Z2NpJPCx_Nx5UmefWdMybjvVnUpzUUdjYCLWNN947nDTYrXLil6tq0ANEvaijSMWr1Ra95mvaA60PHBgA3ujlTnFPLCSalgh6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛گزارش‌ها از شروع اعتراضات در دانشگاه علامه تهران حکایت دارد؛اعتراض علیه حکومت، گرانی و...
جمهوری دروغی نمیخوایم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72414" target="_blank">📅 17:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72413">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a13c699acc.mp4?token=U83MTsq6Mxqa84ush5P9ShRMSB72sDazITKECaVp7ZueS4d4m47wyc_04CNo6pspAOlkvWbauNEPQvg4-lVwB_6yUj6cAfvNpZg0eTyopBGjzyWQx6gTAeRCRGUohoUVPOa8NGGSF8YUTNWefaAaFfy05zg9F2AWGTvGqIxDbR-3XAWbZRbB4lmiRxNil0h57aRD0HL9OnicK4T8sz_teJBezAgpIUiL-XWKBchPJsY7aKNgStw_JyMRN1f6IUjVK5uS_WlMe5We-tNedmgeVVRFoeVbWjVCjawa3_24zVTbvRNdhPeqx77DP5Ols0gG6T60uRVRKMJQ9E3M-XbO7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a13c699acc.mp4?token=U83MTsq6Mxqa84ush5P9ShRMSB72sDazITKECaVp7ZueS4d4m47wyc_04CNo6pspAOlkvWbauNEPQvg4-lVwB_6yUj6cAfvNpZg0eTyopBGjzyWQx6gTAeRCRGUohoUVPOa8NGGSF8YUTNWefaAaFfy05zg9F2AWGTvGqIxDbR-3XAWbZRbB4lmiRxNil0h57aRD0HL9OnicK4T8sz_teJBezAgpIUiL-XWKBchPJsY7aKNgStw_JyMRN1f6IUjVK5uS_WlMe5We-tNedmgeVVRFoeVbWjVCjawa3_24zVTbvRNdhPeqx77DP5Ols0gG6T60uRVRKMJQ9E3M-XbO7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی هیچ چیز سر جای خودش نیست. مهندسی نفت از امیرکبیر، رتبه ۱۰۶۵ کارشناسی، رتبه ۱۵ ارشد، ببینید شغلش چیه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72413" target="_blank">📅 17:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72412">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0ea1d7769.mp4?token=f7TU_N8elK02hDGa0ULhSd0_jILcPhvkb9InxIf3ZeW7AFynIUwG4zfekDrZiiHJyaXtYZrupwloPqlDq3u0UKawaa25R9a8CsWJta0xEpbu1LP_5rJMDFygRnfTkGQEYcRJfifLFbSIKfM3aKeHZzTThXGJcEcBGJ3iHhKRBzvD_ONiKRi3FzZo0n8s2My93LG9MvEPoQCo9qFWZPWp7UpV3HrzWjb1iCB01U1faDg-FC3u27KpSeKRkDzLSzh7ZzZn_ia-uJFVveL6ntp-9BQKjAeraE_AoyvtgtceGrQo_G3oaued7H1BvWMYA4CkC-KK_ETf73mSbcWs4s5WqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0ea1d7769.mp4?token=f7TU_N8elK02hDGa0ULhSd0_jILcPhvkb9InxIf3ZeW7AFynIUwG4zfekDrZiiHJyaXtYZrupwloPqlDq3u0UKawaa25R9a8CsWJta0xEpbu1LP_5rJMDFygRnfTkGQEYcRJfifLFbSIKfM3aKeHZzTThXGJcEcBGJ3iHhKRBzvD_ONiKRi3FzZo0n8s2My93LG9MvEPoQCo9qFWZPWp7UpV3HrzWjb1iCB01U1faDg-FC3u27KpSeKRkDzLSzh7ZzZn_ia-uJFVveL6ntp-9BQKjAeraE_AoyvtgtceGrQo_G3oaued7H1BvWMYA4CkC-KK_ETf73mSbcWs4s5WqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکیه: تحقیقات با هدف یافتن «کشتی نوح» در محوطه‌ای نزدیک به کوه آرارات آغاز شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72412" target="_blank">📅 16:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72411">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/883c91f5fc.mp4?token=c2QjDoNO1GHQkTkGqQwm89fnQ732OO5Uzf_x7l_tm0JnYmnS4mQYvqXSiiyYVaZmDDFMle5cCRpbgPrJdeD1aVqd2oHZc5T0qaxAtFOm8oz_-sHmAmVm7E5JcuBEiyFYGRJ6ZFZnmgmfFfJWlmILt1bxlEZYUpCWWlYWSABJBtm4jG5k-PvfFsPMZ7dX-MEpnb7e0GfOUOZoIGeW_xrFqLQfSWplRWIsYcGjpzckGc0roqdAQiAIfFcfskdiOFG4f42XDEM6N5tUOhnCwqrl9_RGHx_eAXS0LFWb0yJLoBnkokkgpfByrg1K_O1VHlK_74eBsuuLmPdzuvxpXC8Klg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/883c91f5fc.mp4?token=c2QjDoNO1GHQkTkGqQwm89fnQ732OO5Uzf_x7l_tm0JnYmnS4mQYvqXSiiyYVaZmDDFMle5cCRpbgPrJdeD1aVqd2oHZc5T0qaxAtFOm8oz_-sHmAmVm7E5JcuBEiyFYGRJ6ZFZnmgmfFfJWlmILt1bxlEZYUpCWWlYWSABJBtm4jG5k-PvfFsPMZ7dX-MEpnb7e0GfOUOZoIGeW_xrFqLQfSWplRWIsYcGjpzckGc0roqdAQiAIfFcfskdiOFG4f42XDEM6N5tUOhnCwqrl9_RGHx_eAXS0LFWb0yJLoBnkokkgpfByrg1K_O1VHlK_74eBsuuLmPdzuvxpXC8Klg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمید رسایی، نماینده تهران در مجلس، اعلام کرده است که در پی صدور حکم ۱۰ ماه حبس تعزیری، خود را برای اجرای حکم معرفی خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72411" target="_blank">📅 16:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72410">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee8b26464.mp4?token=BH3VHWzz-K9kZvMdcGcFfbFb6VAx4PzFIkhIn_oTXi7eGgJMbKLnMqODKRpZKqYrHrLTbNT7k7esEHmr-bY-CY6b7gOoFgbAbQEdIjNdiEG3fcDXJnSIXwuodrYB1HqZwEuCVypg6v1-25rFYwfnELKd60YuKVb8klFSEGIYfwmHiYqtWWfVnzryD1JSpidwNoK2Q639POwZEwsTx7Ldol0eoAHjIcUPHz7WoC1UAAy7V-innz5KzA_kD0KHoYKO-UGdB17hvqYMBVaDxR6C1njJ5J-i5KK9SbbuK-yFMimCoWPzAKH4pOwSP0tMOyvwc-USLg1rnNsDOu5URfUTjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee8b26464.mp4?token=BH3VHWzz-K9kZvMdcGcFfbFb6VAx4PzFIkhIn_oTXi7eGgJMbKLnMqODKRpZKqYrHrLTbNT7k7esEHmr-bY-CY6b7gOoFgbAbQEdIjNdiEG3fcDXJnSIXwuodrYB1HqZwEuCVypg6v1-25rFYwfnELKd60YuKVb8klFSEGIYfwmHiYqtWWfVnzryD1JSpidwNoK2Q639POwZEwsTx7Ldol0eoAHjIcUPHz7WoC1UAAy7V-innz5KzA_kD0KHoYKO-UGdB17hvqYMBVaDxR6C1njJ5J-i5KK9SbbuK-yFMimCoWPzAKH4pOwSP0tMOyvwc-USLg1rnNsDOu5URfUTjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری:چرا هیچ نشانه ‌ای که ثابت کنه رهبر ج ا زنده اس، منتشر نشده؟
عباس: به دلایل امنیتی!
مجری: خب چرا یه ویدیو ازش نمیاد بیرون؟!
عباس: به دلایل امنیتی! شواهد زیادی وجود داره که نشون میده آمریکایی‌ها ایشون رو تهدید میکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72410" target="_blank">📅 15:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72409">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04d82e25d0.mp4?token=ZW597dbRzQhZcF5T02dtEWnyoo2rB2W1FPrawASKBhq84_DEpyvt9JrWwx0NRxqG2MgEDlDWO306LnxqoDVyG7ynL9nlBwFtIEFH6THs3spd0JPKfOz0X4q_YecLsu8f5ws6a2jQCDkDD2j9JcEbw4b2mtG_QeH559rh1BAyTojbrwj6XIZQrccwhsM8rVi0aTYjM7fRdyszt7qgSxUnjtqLOkzvBYfSiX7GEJXcXb9rRWb7H62P3YtrJMnJmM44rQDuFYeDIYzoeTwU2A3j5IkyMAI0k2PgyK2A_mDkG4NyCYycNWCRPR0JU-wOvTUn2zx_qSVD7Mhxy25vmPYIdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04d82e25d0.mp4?token=ZW597dbRzQhZcF5T02dtEWnyoo2rB2W1FPrawASKBhq84_DEpyvt9JrWwx0NRxqG2MgEDlDWO306LnxqoDVyG7ynL9nlBwFtIEFH6THs3spd0JPKfOz0X4q_YecLsu8f5ws6a2jQCDkDD2j9JcEbw4b2mtG_QeH559rh1BAyTojbrwj6XIZQrccwhsM8rVi0aTYjM7fRdyszt7qgSxUnjtqLOkzvBYfSiX7GEJXcXb9rRWb7H62P3YtrJMnJmM44rQDuFYeDIYzoeTwU2A3j5IkyMAI0k2PgyK2A_mDkG4NyCYycNWCRPR0JU-wOvTUn2zx_qSVD7Mhxy25vmPYIdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان درباره استخاره روز اول مهر :
قرآن رو باز کردم دیدم خدا میگه بازم باید صبر کنید؛
«وَأَطِيعُوا اللَّهَ وَرَسُولَهُ وَلَا تَنَازَعُوا فَتَفْشَلُوا وَتَذْهَبَ رِيحُكُمْ ۖ وَاصْبِرُوا ۚ إِنَّ اللَّهَ مَعَ الصَّابِرِينَ»
از خدا و پیامبرش اطاعت کنید و با هم دعوا و اختلاف نکنید چون سست و ضعیف می شوید و قدرت و هیبت تان از بین میرود. صبر و پایداری کنید، چون خدا با صابران است.
اینا خیال می‌کردن بد اومده بابا خیلی خوب اومده که...
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72409" target="_blank">📅 15:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72408">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مجتبی خامنه‌ای:براساس محاسبات الهی، ایران قدرت اول جهان است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72408" target="_blank">📅 14:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72407">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c75d2b725.mp4?token=eGPcsw1FvD3evnEaCjGqP9piKYHvX-qO5zJPHqd9pLsGwkBE8BRO0ms2KG506i88e3aI617jAJ1Xws6Sh_JI3HCyEwQ4zNeA4gY6-nKGKOCki8HHntz_MGxSL2K-3A4Rtw9_mGvM9Hx6zrsL7dGEahy_332GQ8U8gEBBjRiMT0e5Gqa5uYGOjO9Knwz22Pb3FtmKbxny2zKSlBM8gqOx9a7AabKxEPvw4Hu5YjSxa4fFsQ_4Jafcnq9SIaxHk3VgAw4QYEhi4VYCxMlI6iOyePuPV6Vn14mIWA7ye5OImvp-TyU6mfBw1Juy6_84SbT8zDOZX4cLXDrH-DLMJp2IEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c75d2b725.mp4?token=eGPcsw1FvD3evnEaCjGqP9piKYHvX-qO5zJPHqd9pLsGwkBE8BRO0ms2KG506i88e3aI617jAJ1Xws6Sh_JI3HCyEwQ4zNeA4gY6-nKGKOCki8HHntz_MGxSL2K-3A4Rtw9_mGvM9Hx6zrsL7dGEahy_332GQ8U8gEBBjRiMT0e5Gqa5uYGOjO9Knwz22Pb3FtmKbxny2zKSlBM8gqOx9a7AabKxEPvw4Hu5YjSxa4fFsQ_4Jafcnq9SIaxHk3VgAw4QYEhi4VYCxMlI6iOyePuPV6Vn14mIWA7ye5OImvp-TyU6mfBw1Juy6_84SbT8zDOZX4cLXDrH-DLMJp2IEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند نفر داشتن با ذوق توی جاده میرفتن سفر که یه گوسفند یدفعه برعکس اومد و باعث این تصادف وحشتناک شد!
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/72407" target="_blank">📅 14:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72406">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">۱دلار=۲۴۰.۰۰۰ هزار تومان  @News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72406" target="_blank">📅 13:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72405">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRRFGaboAL3mNT8sSXpuN9NAsvtOjuqqhfqmCr14bDvTglNiZI6z141cW12vsImbcJnqJ4SQQBOVliSGHB3187D4RLXDwi5GO5q69kzFYdbo2XUx7gi_Syk9kD4Cbwg825twfPEXE9e_EyAMnVjwq-5aqOOSYtzqRxk4DvIHM3V9-7_YQK9pH9i1K3X8yr1gbeEzYpKN2rOIEpEpzyTB97-LPdybEsMjJ2T9Hs9wZv9f2zsnS4oPR8G-zy-EdBRJHKRmseany-DBXP_apY4jh3JRtejFM8oMqg2MKbAaYlrH14QmYl9L84sumbMOAwCpbQTHloi3cSDbNAq6kAwSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان هواشناسی:موج رطوبتی از شمال آفریقا در حال حرکت به سمت خاورمیانه و ایران است و می‌تواند زمینه‌ساز افزایش بارش در بخش‌هایی از کشور شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72405" target="_blank">📅 13:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72404">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b839fcae.mp4?token=I2c8ymcaEn1wseZFePzf0l5YuTgm1ZaGlTJE3Ad2Qys12B24AQ1C0DKRb9mQ6DV2fuBeKGz_D994UfMRRWc9nVW4Ss8xRSbKg4xayOJw96RzWXrZYkLdGIV8IroFNFt0kKlIgW056covGBZl1RAc7hMC6AR6nU71v_NUDrfjZzlZHrItje16OuCGNv92-bbnwdVsJ8tvGLdMWNdoh2_MdgBGJYJJk9YcVxgyoHWXZowV-G8HKrwqHBXp9rHXmF_M5PqNNnxOeIMBe3yUdjaKprNb_vs15pfct4j_fDmLskPuIP2gLeUIXMlrVKwjvme996SMDzPQKu3jVDT_dCLmLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b839fcae.mp4?token=I2c8ymcaEn1wseZFePzf0l5YuTgm1ZaGlTJE3Ad2Qys12B24AQ1C0DKRb9mQ6DV2fuBeKGz_D994UfMRRWc9nVW4Ss8xRSbKg4xayOJw96RzWXrZYkLdGIV8IroFNFt0kKlIgW056covGBZl1RAc7hMC6AR6nU71v_NUDrfjZzlZHrItje16OuCGNv92-bbnwdVsJ8tvGLdMWNdoh2_MdgBGJYJJk9YcVxgyoHWXZowV-G8HKrwqHBXp9rHXmF_M5PqNNnxOeIMBe3yUdjaKprNb_vs15pfct4j_fDmLskPuIP2gLeUIXMlrVKwjvme996SMDzPQKu3jVDT_dCLmLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحلیلگر نظامی وابسته به حکومت:
یادتون باشه تو جنگ ۱۲ روزه میگفتن هی F35 زدیم ولی در واقع ماکت اونارو میزدیم
این جنگنده ها از طریق الکترومغناطیس یه شبح بعد عبورش می‌ساختن
ما داشتیم پاد های F35 رو میزدیم یعنی امواج های رادیویی اونو خلاصه بگم هوا رو میزدیم
در نتیجه هیچی نزدیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72404" target="_blank">📅 12:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72403">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72403" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72403" target="_blank">📅 12:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72402">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lq7BVjC4JpGi3LOlJ4-JcTfOImxIuxoRiC8t9UfAx468DHld7IYMJykVm3VPFnyT13bkVwB8g5NwS_Gp6CggFOIF-gC4OfrihMmTZqv_uVkOYZ1Ur58dKycuA2ZMkCI9w6u8ae5-JdB3qMBm4qOIG2XwDXjWVjc4j_PW7rbadm1bGkt2_sdUZ3QAJiMaYgQrW_vIMGUwH3zQbKTeCYeJJRyTORtSCm74MSGx8onpTZj6FvSHB7KPxFVpxZB1spc8bG9lJT3QVdR2bhIX8MHhXAJswpW9Rmr4c-BIg1rINhLhHr5HiWKbuXwR-7E77EOagPXXRNe5ERJnubUQSvO4pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
فرانسه
🆚
بلژیک
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
فرانسه: ۳ برد، ۲ تساوی و ۸ گل زده
بلژیک: ۴ برد، ۱ شکست و ۱۵ کل زده
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72402" target="_blank">📅 12:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72401">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCWmKfLgAnPn76J_sPqZo5J3aFVNqZFsd2-UWUq9MiUmQV0Oa0db_ksh-4rekdhj1cfjPrgZ0xJAeXv0lQ0SlV2VzI9y_MbTzUfOrfyE607srjA8uGfPAcBBoqg9hCJmN2s1gOFy2alo5jYFJw0qv-iruliFsbu1EGqyrvC7AwYj-i-AUqFC82iE2H4BGtmqzi6f3ntY8xmFtmnlHOc9hYeIDe73gm9Fz3Hc-JWp4a1KKViODnIeMv1zztb2v_Qh9JjsD7Yi4mvo-mq7GJvWyP9TFRfu0F3aeHFKfR_XDvPz_5MFcWGDYjQHGZO1hudtLL7FalLquEOHeXPh_m7AaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی قلهکی، فعال رسانه‌ای :
همه‌ی شرایط منطقه شبیه به بهمنِ ۱۴۰۴ است!
یعنی چند هفته قبل از حمله ۹ اسفند...
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72401" target="_blank">📅 12:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72400">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">۱دلار=۲۴۰.۰۰۰ هزار تومان
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72400" target="_blank">📅 12:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72399">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc45d0630.mp4?token=iLZ6slQbXtTq0BJgt0JrbVkR7oWWlIdZ01iFw0W96Qrd7bl6tlmLg86DrEaldOIzO6nLmKELoIIFv0kJIARmgO12iX2Md1FHiVtKfYJuVTVr4Jh2SZIIKPdXSFOjX0j28dvMn2NHj5qdo2Zm13vx26_EHtgiamFEUTXPX6PoWSiq8SsBdN2ZVe0VpVhJrKs-d1EbH7RoFQWmRVikSsA3NdafU8UdDZqakESWcbyPiA_o2hIb5xt8uZI1uRqc1NB6t5F_G2_cMEWB8VvSRezfog-dASoui1POcwZqxPe7jmDqoR5PwfeRuJLgcxjD6GXOeMIYqIg2FdHCfQ7B8nPnMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc45d0630.mp4?token=iLZ6slQbXtTq0BJgt0JrbVkR7oWWlIdZ01iFw0W96Qrd7bl6tlmLg86DrEaldOIzO6nLmKELoIIFv0kJIARmgO12iX2Md1FHiVtKfYJuVTVr4Jh2SZIIKPdXSFOjX0j28dvMn2NHj5qdo2Zm13vx26_EHtgiamFEUTXPX6PoWSiq8SsBdN2ZVe0VpVhJrKs-d1EbH7RoFQWmRVikSsA3NdafU8UdDZqakESWcbyPiA_o2hIb5xt8uZI1uRqc1NB6t5F_G2_cMEWB8VvSRezfog-dASoui1POcwZqxPe7jmDqoR5PwfeRuJLgcxjD6GXOeMIYqIg2FdHCfQ7B8nPnMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلما، ماده‌یوزپلنگ هفت‌ساله ایرانی، چهار توله‌اش را به‌دنیا آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72399" target="_blank">📅 11:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72398">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پرزیدنت ترامپ:
به‌جز نفت — که [قیمت آن] پایین‌تر از دوران دولت بایدن است — و این واقعیت که دیگر لازم نیست نگران سلاح‌های هسته‌ای ایران باشیم چون [آن‌ها] از بین رفته‌اند، قیمت همه چیز در حال کاهش است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72398" target="_blank">📅 11:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72397">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe7cda202a.mp4?token=E__SxBLEmkyWY-64CBaUwk45z3zbvvLOYxmVFgU8WdJfIwYFhaJX7ZLOhmfx7DR0KoqceYmIFB0Cft8tnTs7GruoBjBY7rFsJFj84qjCDplcUABQt7reaVkoDZ6qdCPGGszNy3nx2KuzgvqZkSd8rXDJd2fOQv8sFArjMVumCG3eunwn-BnHjIsVROfNuHPnZbqCwXpWBo2OMDq3DF5iIerK2ahzkQdIq5pBDAREHzbnSQ4YeCgsGQbCK1kQj03Y7lj0QPXkCphI3IzsFX8Jso79H3H39EK4T18YQLgyLqUrj0GQJuWZ2Xx1lJT7HD_ys8jW7GtzIQH9wP-vKMFQmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe7cda202a.mp4?token=E__SxBLEmkyWY-64CBaUwk45z3zbvvLOYxmVFgU8WdJfIwYFhaJX7ZLOhmfx7DR0KoqceYmIFB0Cft8tnTs7GruoBjBY7rFsJFj84qjCDplcUABQt7reaVkoDZ6qdCPGGszNy3nx2KuzgvqZkSd8rXDJd2fOQv8sFArjMVumCG3eunwn-BnHjIsVROfNuHPnZbqCwXpWBo2OMDq3DF5iIerK2ahzkQdIq5pBDAREHzbnSQ4YeCgsGQbCK1kQj03Y7lj0QPXkCphI3IzsFX8Jso79H3H39EK4T18YQLgyLqUrj0GQJuWZ2Xx1lJT7HD_ys8jW7GtzIQH9wP-vKMFQmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداوسیما:
در مقابل محاصره هوایی، می‌ توانیم بین پروازهای غرب و شرق کره زمین دیوار ایجاد کنیم و روزانه ۲۵۰۰ پرواز را مختل کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72397" target="_blank">📅 10:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72396">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb550a215f.mp4?token=kKS77gdBTbudxARoku9o-gGgZtKZ7B0F85XX-hsI1RnCmrEBufL0j_ogb2RLdv-qqQxHaGG_GTvbGbayyHrHxky189sg0Dy546SMYSx5mbaTVaVR0YR-hGozFqiOse3ip5I6r23LeCQ8X7T_8cdZIWdxquuXdy60IHGWOHI89a0NAQoKuT_WuDbmOcPwcvJPPyRohvkDC4VhNsntfF35iGONVeivM52FF7_6HDb6O9n8Wg96pyqtPHFsYjhIRZyUEJragm4zINO-g-zmQaaroPKGQOCi7E1Yrj4GDy8E4gWzxUuvX2ISYm_axuFF-uS7Gx_xfZHLGh_R3ghZugORYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb550a215f.mp4?token=kKS77gdBTbudxARoku9o-gGgZtKZ7B0F85XX-hsI1RnCmrEBufL0j_ogb2RLdv-qqQxHaGG_GTvbGbayyHrHxky189sg0Dy546SMYSx5mbaTVaVR0YR-hGozFqiOse3ip5I6r23LeCQ8X7T_8cdZIWdxquuXdy60IHGWOHI89a0NAQoKuT_WuDbmOcPwcvJPPyRohvkDC4VhNsntfF35iGONVeivM52FF7_6HDb6O9n8Wg96pyqtPHFsYjhIRZyUEJragm4zINO-g-zmQaaroPKGQOCi7E1Yrj4GDy8E4gWzxUuvX2ISYm_axuFF-uS7Gx_xfZHLGh_R3ghZugORYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:ما هرگز به مردم خودمون حمله نمی‌کنیم
ویدئویی از شلیک مداوم از روی کلانتری به سمت مردم ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72396" target="_blank">📅 10:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72395">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bebdd4e5.mp4?token=NFIFSZ7Df-XIrPpmPbq2qoC87y7VnKFpTrp_LUh3ntDhb_arEfsLYjor3MFkV2VgU5a80FWAnfuNLX-x-G1jXgb3iBKKIRZDmjNZ6oqVFVg5gDWCJkGVsGQTnMnte2K4TM1LhKhu8-VykRJMmUYRYuIShz9_ogdITPx2QLTY2kpYRqc8Y8Vs2HxN8wmLeIq5j4DA1ZUyghgrAaCrqaU35COp6RFgwSBstC4lms1qMnVIPB4IT45kFihTZHHsaScz7qkR__CRsTtIxxqKyUi8ntZr482dNdaMhHZDz4oEVcXVpTecDEUTGTATcHA2pEj1AWexcXP9eqbntXLEdsmvDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bebdd4e5.mp4?token=NFIFSZ7Df-XIrPpmPbq2qoC87y7VnKFpTrp_LUh3ntDhb_arEfsLYjor3MFkV2VgU5a80FWAnfuNLX-x-G1jXgb3iBKKIRZDmjNZ6oqVFVg5gDWCJkGVsGQTnMnte2K4TM1LhKhu8-VykRJMmUYRYuIShz9_ogdITPx2QLTY2kpYRqc8Y8Vs2HxN8wmLeIq5j4DA1ZUyghgrAaCrqaU35COp6RFgwSBstC4lms1qMnVIPB4IT45kFihTZHHsaScz7qkR__CRsTtIxxqKyUi8ntZr482dNdaMhHZDz4oEVcXVpTecDEUTGTATcHA2pEj1AWexcXP9eqbntXLEdsmvDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از ۵۰۰ بیلبورد تو سطح نیویورک دارن خطر ایران هسته ای رو نشون میدن ، این میتونه آماده سازی افکار عمومی رو برای شروع یه جنگ بزرگ باشه
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72395" target="_blank">📅 09:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72393">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/398d534a8b.mp4?token=My9AuQOureYgd0S5PxkYX_8sGnqwSrIOECNxKs0WCRd_kc4sPFKVsCdlyHEaJiX1FOVjpTk2gC9NEKLMDYsPiU6a03FwJzJ6s6HUyUpYsSwrn4pka2GUIAej-9e1J-Pg4s1FyTC2MAvAFdRVVpuC6IQYl2_1Qi3d-VaU4ksO342gY8IL5Z1wZxLsC2FNsuXEAVfoQQDdbkbK1RjrnPPuNCEe3oJPX2aq0aFoNixU9VkGliM0KT1tsGy0beaPyeEgy2UIdPf2axuf1w6oUpHmQ0ns_vJZmmlxaZjnYobn_asOs9yysjDWx29eSSrwlxNKcKvyhITIsZx7mo_lRHXapg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/398d534a8b.mp4?token=My9AuQOureYgd0S5PxkYX_8sGnqwSrIOECNxKs0WCRd_kc4sPFKVsCdlyHEaJiX1FOVjpTk2gC9NEKLMDYsPiU6a03FwJzJ6s6HUyUpYsSwrn4pka2GUIAej-9e1J-Pg4s1FyTC2MAvAFdRVVpuC6IQYl2_1Qi3d-VaU4ksO342gY8IL5Z1wZxLsC2FNsuXEAVfoQQDdbkbK1RjrnPPuNCEe3oJPX2aq0aFoNixU9VkGliM0KT1tsGy0beaPyeEgy2UIdPf2axuf1w6oUpHmQ0ns_vJZmmlxaZjnYobn_asOs9yysjDWx29eSSrwlxNKcKvyhITIsZx7mo_lRHXapg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ناو هواپیمابر «یو‌اس‌اس تئودور روزولت» (CVN-71) از کلاس نیمیتز، در چارچوب استقرار برنامه‌ریزی‌شده نیروی دریایی آمریکا در حال حرکت به سمت خاورمیانه است. این ناو پیش‌تر از سن‌دیگو خارج شده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72393" target="_blank">📅 06:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72392">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72392" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72392" target="_blank">📅 01:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72391">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_vpSPpRU4Zi1UTVFKXaXQzaMys2zdgmBllmZxN80e0bQ06FC_dLpZLAfnpSqu5A3H5euIAVYohxehQWHLhqfUCWgEXjhfVrTQeS94HUBghAFGlx13zhf6Bii1-eeb3Z_IN-AXAgz5kY5jsL-IOKDQtxWiQL8DEdB4cG5G2bV7uwKi0F0v6gpw9cKKJQlcO53jOFSz-7iA2vgD1a9XFSI6tt2lAXXwKiHTOn0UcPTvzlqKcbdA7k7kwbTRFTi1Z29ZRC1HarjrOu4P48mly6rMafEzWvxocQPVkfzOX0rTUExdB2nQpSmoFzheQ5B3JKeBdeAylgyzoimLiBEC4elA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/72391" target="_blank">📅 01:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72390">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b361018705.mp4?token=QzMiiKcQHAI0uYba3vVw_am95Nc6qm0ghZsnHejB5PIbrndR_OQhaYmkL7LaBTOCCaUMc4jLWTG9tid2UD-eLiE2Lojg9Xq2syBdtQTb38QfeL2vKgM4MRWOhOcv9IWgeef9ofVHI4NIVcYO6cegUGMWQK72pDBSV1c5HauwQ_BsqbeaKFodTk3cdtH7HYIgWkYBL1IKMLyl1poWG-ivnrJ2Yw1FtsxrMTc5ZP8Rj0_BUzPP5aseHkPwENPgYIhYNx1Yh5NWM1065BkcimNpXYnW-9tUCwNW-bfhfYPUMrMvKW39pfTeJCME60_wQdXJtZzTPuMbC9LzeOsrcGsjXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b361018705.mp4?token=QzMiiKcQHAI0uYba3vVw_am95Nc6qm0ghZsnHejB5PIbrndR_OQhaYmkL7LaBTOCCaUMc4jLWTG9tid2UD-eLiE2Lojg9Xq2syBdtQTb38QfeL2vKgM4MRWOhOcv9IWgeef9ofVHI4NIVcYO6cegUGMWQK72pDBSV1c5HauwQ_BsqbeaKFodTk3cdtH7HYIgWkYBL1IKMLyl1poWG-ivnrJ2Yw1FtsxrMTc5ZP8Rj0_BUzPP5aseHkPwENPgYIhYNx1Yh5NWM1065BkcimNpXYnW-9tUCwNW-bfhfYPUMrMvKW39pfTeJCME60_wQdXJtZzTPuMbC9LzeOsrcGsjXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز:
آیا انجام حملات پیش از انتخابات میان‌دوره‌ای همچنان برای شما مطرح است؟
ترامپ:
نمی‌خواهم چنین حرفی بزنم. یعنی، ممکن است [چنین اتفاقی بیفتد]، اما صرفاً نمی‌خواهم آن را به زبان بیاورم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72390" target="_blank">📅 01:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72389">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13e157d195.mp4?token=T7MkeJ5iwsJWe98sZ8vU50RI_ljMBcLqlqgq0TE-bxUI8NA4-B4RPReyECBabIicxUIx98TD8mG-5_k0yCtAA7XsdRGAHfllFUvtfuQPOPOxynr6JaP-JWbXtwDycKWHnqoY0A5DEeNO8SV6OvzqPJdfXVn6Su-5C4gHRWpRlpqG72AtdAB7nE4KCZXBh63n_ex24a3QpWzR8msW9FUuU_EbB1btdiJWHnW8Ibu0QWfoEk5gtY_COX9I-uma7djiiu0Z9mma4hyz-mwEeI-iQbUatcClqa93iYH_qaMXSkQaRgC3g8pFE7RUYJsA6Ra2GiV7YfH5HQ689GE6surp3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13e157d195.mp4?token=T7MkeJ5iwsJWe98sZ8vU50RI_ljMBcLqlqgq0TE-bxUI8NA4-B4RPReyECBabIicxUIx98TD8mG-5_k0yCtAA7XsdRGAHfllFUvtfuQPOPOxynr6JaP-JWbXtwDycKWHnqoY0A5DEeNO8SV6OvzqPJdfXVn6Su-5C4gHRWpRlpqG72AtdAB7nE4KCZXBh63n_ex24a3QpWzR8msW9FUuU_EbB1btdiJWHnW8Ibu0QWfoEk5gtY_COX9I-uma7djiiu0Z9mma4hyz-mwEeI-iQbUatcClqa93iYH_qaMXSkQaRgC3g8pFE7RUYJsA6Ra2GiV7YfH5HQ689GE6surp3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
آیا فکر می‌کنید ما در این جنگ [با ایران]، از طریق جنگ اقتصادی که وزارت خزانه‌داری به راه انداخته یا با حملات نظامی پیروز خواهیم شد؟
ترامپ:
فکر می‌کنم هر دو. به نظرم از هر دو طریق پیروز می‌شویم. از منظر نظامی که عملاً پیروز شده‌ایم، اما این بدان معنا نیست که آن اقدامات را متوقف کرده‌ایم.
ولی قطعاً داریم با اقتدار کامل در آن پیروز می‌شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72389" target="_blank">📅 01:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72388">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3da141396.mp4?token=cxOE6J0PP4IIQ6Iwx19bzLU9rpf1udHkUZwA_LkLEFjWUQadg9ADMTEdsSghtR-GwoJYlRfoh4U__RUMou9l6H742-G8hXi_gWwZ5YvVaAJEqNu4jbLJKTMnpx4uMU0-BFTt7kFZNQJRKQP9_MeM8ICS26CSOlHVIfiIKfeqWqR514yIYkljCLb7Tag1RbzHZDBJlh8Si9OhND5Aqu7sF_LG83W5GpUyZVMVHOVkUCfNs1SKeeSu5GhKnL9nQhWadYWMnpD-QJlwgUmEmwbEana3T3C48OHL7PBiEcpmNK7kgRQllUBgNAOaBzSy7-Llbkok7jvs1vJeIUfD-Lmzdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3da141396.mp4?token=cxOE6J0PP4IIQ6Iwx19bzLU9rpf1udHkUZwA_LkLEFjWUQadg9ADMTEdsSghtR-GwoJYlRfoh4U__RUMou9l6H742-G8hXi_gWwZ5YvVaAJEqNu4jbLJKTMnpx4uMU0-BFTt7kFZNQJRKQP9_MeM8ICS26CSOlHVIfiIKfeqWqR514yIYkljCLb7Tag1RbzHZDBJlh8Si9OhND5Aqu7sF_LG83W5GpUyZVMVHOVkUCfNs1SKeeSu5GhKnL9nQhWadYWMnpD-QJlwgUmEmwbEana3T3C48OHL7PBiEcpmNK7kgRQllUBgNAOaBzSy7-Llbkok7jvs1vJeIUfD-Lmzdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایران:
به گمانم آنچه رخ خواهد داد این است که ما خیلی زود در این جنگ پیروز خواهیم شد؛ و به محض پیروزی، قیمت نفت کاهش می‌یابد و به شدت افت می‌کند تا به سطحی برسد که پیش از جنگ بود.
و نکته کلیدی این است که ایران به سلاح هسته‌ای دست نخواهد یافت. این کلیدِ ماجراست.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72388" target="_blank">📅 01:16 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72387">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91575662ab.mp4?token=jLLttQgQ7bMqYITTJCL6jGAn2qxGf3aFHNEfXcdhOJ0fIrkIqF8lCCD8Kna77BiphqO1m-0XxcIN6bzejAKBhG2KzAgDezStNCEbXgftH1sVXmyjU1cQ5JVcV_l9FHuRk8gT6qWyQqTzJsQ4uI1akGP_C8vxSN9otWQ3F0Z_8ihhwh9nqziJYXuTDK302-_ZnvV651Yg3-YvDpQvgd_5rafPZh4EZkmc7b31-p2WwWHa8w63wRm0aOlWuLtYJQza-6ZY0T3p550_EIvzyfd-xY_ojVmQIrgEUuXjJezOqjj2FGNQ2sMoDYHR8xLhXu0jry_KzZLyae2SNwccJWM8Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91575662ab.mp4?token=jLLttQgQ7bMqYITTJCL6jGAn2qxGf3aFHNEfXcdhOJ0fIrkIqF8lCCD8Kna77BiphqO1m-0XxcIN6bzejAKBhG2KzAgDezStNCEbXgftH1sVXmyjU1cQ5JVcV_l9FHuRk8gT6qWyQqTzJsQ4uI1akGP_C8vxSN9otWQ3F0Z_8ihhwh9nqziJYXuTDK302-_ZnvV651Yg3-YvDpQvgd_5rafPZh4EZkmc7b31-p2WwWHa8w63wRm0aOlWuLtYJQza-6ZY0T3p550_EIvzyfd-xY_ojVmQIrgEUuXjJezOqjj2FGNQ2sMoDYHR8xLhXu0jry_KzZLyae2SNwccJWM8Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو سالگرد ترور نصرالله رو با انتشار چنین کلیپی به مردم اسرائیل تبریک‌گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72387" target="_blank">📅 23:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72386">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lz2h3ycqI7ZHONKqibSqsMiiEnbYVXmu-CDYciTPo7oiwCKoQnY6lNAVpa_-aGRcBm5XKy1-0M25dlspKZju5Lt9nsPQ84XxpWqFBMIdz_z1STrNtmjKWGyNSQQ9u7mqkTTse7ZeUgQirKNyo6ff3SQTqKXUHxpoN91qsO2HuBdhFe2xAlOrOkDdXRKeJHVGfz33eJRm-GW4ZWMf0JYgYhfzQEMWhNzHHYF6EzdPhChKL8sJ4XyybOMjwWMvPjeD4lp-4sHR-TDbmQ7i1ltxXVN3b6NCU80VH4uleVwW1wIYDyhzkbdmQWbH87RYV4dB8ibWiW68UMZ9Nn5kvug58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛به گزارش شبکه ۱۲ اسرائیل، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، امروز سفری محرمانه به ابوظبی داشت و با محمد بن زاید، رئیس امارات متحده عربی، دیدار کرد.
نتانیاهو صبح امروز با یک جت اختصاصی سفر کرد و بخش عمده‌ای از روز را در امارات گذراند.
محور اصلی این دیدار، ایران بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72386" target="_blank">📅 23:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72385">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z_FXAMPKsJFZImv3vBpUhAsp8XtQo6TOjCc116MsHoptIi6RhFKUpPT7jER2Re09npF7p0dSDfsyHNUJ4KOYEjt5tbwxsaWKhSbKo2pYy6oXXo-pIEkav31APRigP60fmtm5qk2YWA2AlBfQ4Mp9sZMpN4hAHF9d2izTa1cnbOAmpaC-pWaNpFeAZpIbfjDlzS_WEI4YU-nWvDC9tI84JP4T2JmwyrZYbFYTQ1OguaMo8rl8rw8C-ppkT3HTwGK4OlagHc_d-tNPo_ak7GYh6CcLaoffuxkROt76JFiurIv4kQnjX157yFWMGgQ6Ks0BHpIeaV3mpQrbMs9Mu3Xr-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حق‌ترین و مفهومی‌ترین عکسی که میتونین ببینین:
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/72385" target="_blank">📅 23:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72384">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">الکساندر ووچیچ، رئیس‌جمهور صربستان، استعفا داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/72384" target="_blank">📅 22:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72383">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">شلیک چندین موشک ضد کشتی به سمت شناورها در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/72383" target="_blank">📅 21:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72382">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/824029a6f9.mp4?token=R7v5cq8d9aljmPLE6M8Iii5B82bl3JQPeOX7Tb2_NXaretpRfsFlaEu4nxdJd_eMicv9J-w1-iifdh9q_kQD3afPYRvA3QvalrQG0sZ6aIUTph5klopXceN94Ef3JHQbedI09VMPFdHZA8aDD1HNiXVOntnPWSDNuErP5r2LDL3Cz5gMVrEeyIps15MKFobPBkU6CyrSF2dyrz6cWSZGW_TPkP2GI4z2ztORqLwwH_6Bk9kIXA8e8To9PfRBBpEzXDWfjo_Oy6zUEt-sDGCFmK22bn1rRAI3h2vq558EfovK6bfvb78cWIO6hntgss-CKDbJeUwNuUK732NV7ei2FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/824029a6f9.mp4?token=R7v5cq8d9aljmPLE6M8Iii5B82bl3JQPeOX7Tb2_NXaretpRfsFlaEu4nxdJd_eMicv9J-w1-iifdh9q_kQD3afPYRvA3QvalrQG0sZ6aIUTph5klopXceN94Ef3JHQbedI09VMPFdHZA8aDD1HNiXVOntnPWSDNuErP5r2LDL3Cz5gMVrEeyIps15MKFobPBkU6CyrSF2dyrz6cWSZGW_TPkP2GI4z2ztORqLwwH_6Bk9kIXA8e8To9PfRBBpEzXDWfjo_Oy6zUEt-sDGCFmK22bn1rRAI3h2vq558EfovK6bfvb78cWIO6hntgss-CKDbJeUwNuUK732NV7ei2FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازم یه حماسه‌سازی دیگه از مسعود :
🎙
مجری شبکه فاکس نیوز:
آیا شما اورانیوم غنی سازی شده 60 درصد رو تحویل میدین؟
مسعود پزشکیان: بلهههه
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/72382" target="_blank">📅 21:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72381">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51ab5c624e.mp4?token=g5IjXcJA2zbxIRP-7wFH4Ml3x2tTm_Sx4fEFoP45hdHAhbEWOuRSUyMlBEUAwCO5qAo34d66V6LFncdt_0G-FZzJe1EYwoGLSJ3A-9AlssvsPdiXCQDAkAR_lpNEW_mZj2fdbE9O7nNYqSdidUDfDxGxuIOaDzrto6NgQBm-uRRPYeKbfKOaBBsQGfFvU_tq2-KGsBmXhze4kvRzksDDeFZZV0gLIxNeBLSZacvgxesBZbD0XgoMpkleNTUHJRr1edGakesUjHTnk7KF8y0dX1wcMuGZKWLRZgtsaqjOT1WL7JBzTgX3v3RFddWM_TLqspdjauIZ-q89FYAs1UHz9YkhhMpXjWTXhjfmCcPogOedcGUhVywwTw6OYCkYbuhVnmbd6El11TkEBFbGGCBi1TkW2nsAjlyfSwIdJhIj1kAS5LTQyAVuexnNYSm7gUBrN_U70ErnbBajsOrPdWTBmoOuKKNQ9f1ZOTmT0_rEhTumAYQCQ8i5SIp9VPgZb32bWQy2x_Tiue_C2JZSRG7jhTcwKl0BT-IwIWz-m4uqKGo_wn7r2xdIJcefIYURqGPwf5-kvmJo2km9OfgCGqUuOZfdOFoUONEoEtogxR8F1y4UsfrashW0jiFTGC3GuyB-tgnQetDFkBaw64IKXHM52TUw7eH6SzB7SDkof4JyZ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51ab5c624e.mp4?token=g5IjXcJA2zbxIRP-7wFH4Ml3x2tTm_Sx4fEFoP45hdHAhbEWOuRSUyMlBEUAwCO5qAo34d66V6LFncdt_0G-FZzJe1EYwoGLSJ3A-9AlssvsPdiXCQDAkAR_lpNEW_mZj2fdbE9O7nNYqSdidUDfDxGxuIOaDzrto6NgQBm-uRRPYeKbfKOaBBsQGfFvU_tq2-KGsBmXhze4kvRzksDDeFZZV0gLIxNeBLSZacvgxesBZbD0XgoMpkleNTUHJRr1edGakesUjHTnk7KF8y0dX1wcMuGZKWLRZgtsaqjOT1WL7JBzTgX3v3RFddWM_TLqspdjauIZ-q89FYAs1UHz9YkhhMpXjWTXhjfmCcPogOedcGUhVywwTw6OYCkYbuhVnmbd6El11TkEBFbGGCBi1TkW2nsAjlyfSwIdJhIj1kAS5LTQyAVuexnNYSm7gUBrN_U70ErnbBajsOrPdWTBmoOuKKNQ9f1ZOTmT0_rEhTumAYQCQ8i5SIp9VPgZb32bWQy2x_Tiue_C2JZSRG7jhTcwKl0BT-IwIWz-m4uqKGo_wn7r2xdIJcefIYURqGPwf5-kvmJo2km9OfgCGqUuOZfdOFoUONEoEtogxR8F1y4UsfrashW0jiFTGC3GuyB-tgnQetDFkBaw64IKXHM52TUw7eH6SzB7SDkof4JyZ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری:
رئیس‌جمهورایران این هفته اظهار داشت که ایران هرگز به دنبال سلاح هسته‌ای نبوده است؛ با این حال، ایران اورانیوم را تا سطح ۶۰ درصد غنی‌سازی کرده که این میزان ۲۰ برابرِ درصدِ غنی‌سازیِ مورد نیاز برای تولید برق است. چرا ایران به ذخیره‌ای ازاورانیوم با غنای ۶۰ درصد نیاز دارد؟
عباس عراقچی:
اولاً، غنی‌سازی تا سطح ۶۰ درصد غیرقانونی نیست و همچنان در چارچوب معاهده منع گسترش سلاح‌های هسته‌ای (NPT) و برنامه صلح‌آمیز ما قرار دارد؛ ما این کار را برای اهداف مشخصی، از جمله مصارف پزشکی و دیگر مقاصد، انجام داده‌ایم. با این حال، ما پیشنهادی برای تعیین تکلیف مواد غنی‌شده تا سطح ۶۰ درصد در سال‌های ۲۰۲۵ و ۲۰۲۶ ارائه کرده‌ایم؛ موضوعی که اگر آن‌ها حسن نیت و عزم واقعی خود را برای صلح ثابت کنند، قابل بررسی است. پیشنهاد ما این است که مسائل پیچیده‌تر به مراحل بعدی موکول شوند و در این مرحله بر اعتمادسازی تمرکز کنیم. به همین دلیل، ما این طرح هفت‌روزه را بر اساس تفاهمی‌که در گذشته با صاحب‌نظران آمریکایی داشتیم، ارائه کردیم. نخستین گام این است که دارایی‌های ما که به‌طور غیرقانونی مسدود شده‌اند، آزاد شوند؛
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/72381" target="_blank">📅 20:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72380">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">صدای انفجاری از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72380" target="_blank">📅 20:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72379">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxUPR4gLYbRmi23Y1pt-s2km32JUvX302Kpx3zrcktvSRn-Ee5icQDgYo-G0tkPQZcCeU-AQJNsSoxC8jKwSfBCOjq-xowJlk28SSdp7QYoklO-ydXzhtIKMQCqHnAUs_KWK9zbTIoAB6aN1DRUC78XPRgsEcNAbC9KddcxKYbiDWmu9pgGF_D2sbCtdkQZHzHQJOYU5PcDLSkx76Ib6Q1udhbVx5kC7nGIBrs3j8_CPZWnMsfYNnNXphmVYOV_WJCDgMcutA5L3LlRz0G1Lp07jGClKMqEPnlf6R5jsMcLzady4tLJq7yMadb2hYiP3TR7w2xy3RvExceMB-ElPrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای آوش به نقل از اداره حقوقی مجلس: حمید رسایی به ده ماه زندان محکوم شد
آوش:
این پرونده که دوبخش دارد مربوط به سال ۱۴۰۲ و زمانی است که حمید رسایی هنوز نماینده مجلس نبود.
حمید رسایی که از حکم شعبه دوم دادگاه ویژه روحانیت تهران، برای عذرخواهی نسبت به انتشار مطالب خلاف واقع درباره مجلس شورای اسلامی امتناع کرده، با حکم قاضی برای تحمل ۱۰ ماه حبس تعزیری به اجرای احکام احضار شده است.
بخش اول پرونده مربوط به انتشار مطلبی با تیتر «دستکاری قالیباف در اسناد مجلس» در صفحه اول نشریه «۹ دی» است، و بخش دوم مربوط به انتشار کلیپی تصویری در کانال تلگرامی متهم که رسایی در آن از تعبیر «دیکتاتور پارلمانی» برای باقر قالیباف می‌کند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72379" target="_blank">📅 20:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72375">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZCf8gpksvL4UDee_gLiBiGlrDnBJLjOz0KXV22CfCngiytJ4iry0PyqvQPuyeCcyA6Y8WMERdw1SZLrKH4E8unJTCB2IpcfNTN33eswTfa3FdUL4yJZE-BIB1kQlrafvxrPXnXLv44TUYpa75Mihy7SgI2FAXHwHkB1J2QvZZxyZJ9Y9TK9BUJW5BIzTfOnRCZNCsgWG7_TD5WXYNf43WxvcuShnATaYP8GfQHYkIAjnIuSQQiEURIs5iEB1DMwdybA1W4emWhH63cqCrp4rchl36AKrK_L13YbgzzUbYrcevQ7aW28qUzomK2Sp8ri9u_mRO0voGDC_L7qvuR8jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_Rw--Q6FseD4NesRskktH39S1grem0qFIzUaHMJ51qxzIMl-RDpnYVyOx_DaOuROBAU2mqFBzHUYD52c3gOyf4k9GZx96xSo7bLnQVZPF3sEUBMkSte9bqiJZw0a_6fkrbSXGfVoJWGQQdQKx4nnd4i0TBfq706rTy5RyiYVNXOhGYX6to4AgVEk-zMJn3a2bf1vV8vjQTpcpA2lDJsRZVV-8YY3NDvMhGDGWPxk7JcCB03T-8rr7HbeusIfL8FsofLAAm_M2wweoQtFz0rW8wYshr3PHwJJHJOUGBpqABeALC_FQ0KmUVSUxpfL5p6lfPSDQyUszxG1lCkCai8dQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b78db64d5d.mp4?token=mf0db_FvslR1IwQgQvFPcUv3h6A4OjcE-s0y1Fo8ki8Lrk64_oIiECorfUDDu2BMrd_0agyGGBx9Jk9AslSTBNBE0mTlpSiCTpwPA7x3eUEwYmWnf5WKyG5Z6O4lpvgxBYPDhCJK3SHD5ui8dkWEW6Gh4vSULsC3fAyheh7aU9eveeBFpEqSs8hnYO5ejRIEzjtgwsofGi3n19A5-RJEfAaK6Qa7X7Ii7c4QFjMrp0y99I6luf9Lf5wQZUUCJwHmk8B33gM8E4TKQnWdthZmARf8bZCido701nF8h7iAUhJw2Lulbhc0NN4Q-BFo1U4hH4R1JGtwORUabLAncNOwUFHDrp0_UGYOMxKhFzWhSxrYNlVzDmb6ZO3agOGeS-302EL-ge1g3eiyFQV7K5UucE-rEyW3YG2iPR9xwwuZN8bQ1RSUKRGomAYDXdKm8ml91S98MhCguHdcEler5WczIuS9HtqzoxAwGzWAu8IyUMx-BK-lx_TOaVmxZQE6SlUTPTt4OjiQTOK6-HOSrFzVf2m3cQWb4uBeEWZaTmaM2307BrpTeT2UWrgn_f-ak0GlVhpPsmjuDlsnb6c2XEhmFl9O_-7CoCMdRT3sHBHWQjpS5kNvSMUmApeNZZuXbCpu0GYPJgL19Hyreytb7huFmb-JlKU5aOKvunkzg1DM3Eo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b78db64d5d.mp4?token=mf0db_FvslR1IwQgQvFPcUv3h6A4OjcE-s0y1Fo8ki8Lrk64_oIiECorfUDDu2BMrd_0agyGGBx9Jk9AslSTBNBE0mTlpSiCTpwPA7x3eUEwYmWnf5WKyG5Z6O4lpvgxBYPDhCJK3SHD5ui8dkWEW6Gh4vSULsC3fAyheh7aU9eveeBFpEqSs8hnYO5ejRIEzjtgwsofGi3n19A5-RJEfAaK6Qa7X7Ii7c4QFjMrp0y99I6luf9Lf5wQZUUCJwHmk8B33gM8E4TKQnWdthZmARf8bZCido701nF8h7iAUhJw2Lulbhc0NN4Q-BFo1U4hH4R1JGtwORUabLAncNOwUFHDrp0_UGYOMxKhFzWhSxrYNlVzDmb6ZO3agOGeS-302EL-ge1g3eiyFQV7K5UucE-rEyW3YG2iPR9xwwuZN8bQ1RSUKRGomAYDXdKm8ml91S98MhCguHdcEler5WczIuS9HtqzoxAwGzWAu8IyUMx-BK-lx_TOaVmxZQE6SlUTPTt4OjiQTOK6-HOSrFzVf2m3cQWb4uBeEWZaTmaM2307BrpTeT2UWrgn_f-ak0GlVhpPsmjuDlsnb6c2XEhmFl9O_-7CoCMdRT3sHBHWQjpS5kNvSMUmApeNZZuXbCpu0GYPJgL19Hyreytb7huFmb-JlKU5aOKvunkzg1DM3Eo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ساعات اولیه ۲۷ سپتامبر ۲۰۲۶، ساکنان از سه وسیله نقلیه مشکوک که به سمت پایگاه نیروی هوایی سلطنتی فیرفورد در حرکت بودند، خبر دادند.
یک توطئه تروریستی برای انفجار پایگاه نیروی هوایی سلطنتی فیرفورد وجود داشت.
پنج مرد در منطقه ویلفورد به ظن ارتکاب جرائم تحت قانون مواد منفجره دستگیر شدند.
پایگاه نیروی هوایی سلطنتی توسط بمب‌افکن‌های آمریکایی برای حمله به ایران استفاده می‌شود.
پلیس مبارزه با تروریسم در حال بررسی این موضوع است که آیا ایران پشت یک توطئه بمب‌گذاری مشکوک با هدف قرار دادن یک پایگاه نیروی هوایی سلطنتی مورد استفاده نیروهای آمریکایی بوده است یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72375" target="_blank">📅 19:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72374">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9233dc65e9.mp4?token=klBtLA96IeZKfDT0krf7otmswMZktCaUgZlHlS9yKi31DZeyIUs7gMPQI7NFSbTaOD7FOQ8wmAATp9APpc69XmN3nVq_0qbt1X9fqp8PofzFzikNSMTvI5SS2J3NOoxRdrqZGWlym4Nc5iEegUJfqnJJWUQo4xXUgjApVq5vy27iV6iKqwVMWPiNoycWhCfhhw2ydMWInnqrElWV3_1qgfbJMiIldBzkdbZ6TvPnqlN5qs1Fugp-JLhfSMLaavBkCMM7CdDoAp1tjJu6Zzba_oHSjxpAiHrxZ5UVaNqIUNGgspon1ILw4pyxjQLUoadSXksy_8rJ35F_R8x8noy0nE3TbtZm5eQgj_WgFJ_-u2Ze9notw-GtZXxAsJwvAlrkv6vJ3vTZGMDzvrMYQdaM9B7JTO_cgnc4jiIUR5A7AALS2XoMvGsW53KbwW0sGJnffwnXgZQbQzW8ybqg7RHLmxeuFJH8pl2qZL6kw2JqOQBxq8V9A_YzpG7iWy8nziP2VSNjy7GHFSCiCZgAqygVqc35T-ZoMrWlBEHzVfwLiiSDWAwvIcUM02K-9PF9URfyqzku_eSqisA-4fDC_NM8VT0rhaUOwiVSdQrh7YEYmnxZEOt9TLkdKPPFn1YIk62z072_JRzVrqBUpy__SvC_Uwo5mtW785deHdbeJxAJdv0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9233dc65e9.mp4?token=klBtLA96IeZKfDT0krf7otmswMZktCaUgZlHlS9yKi31DZeyIUs7gMPQI7NFSbTaOD7FOQ8wmAATp9APpc69XmN3nVq_0qbt1X9fqp8PofzFzikNSMTvI5SS2J3NOoxRdrqZGWlym4Nc5iEegUJfqnJJWUQo4xXUgjApVq5vy27iV6iKqwVMWPiNoycWhCfhhw2ydMWInnqrElWV3_1qgfbJMiIldBzkdbZ6TvPnqlN5qs1Fugp-JLhfSMLaavBkCMM7CdDoAp1tjJu6Zzba_oHSjxpAiHrxZ5UVaNqIUNGgspon1ILw4pyxjQLUoadSXksy_8rJ35F_R8x8noy0nE3TbtZm5eQgj_WgFJ_-u2Ze9notw-GtZXxAsJwvAlrkv6vJ3vTZGMDzvrMYQdaM9B7JTO_cgnc4jiIUR5A7AALS2XoMvGsW53KbwW0sGJnffwnXgZQbQzW8ybqg7RHLmxeuFJH8pl2qZL6kw2JqOQBxq8V9A_YzpG7iWy8nziP2VSNjy7GHFSCiCZgAqygVqc35T-ZoMrWlBEHzVfwLiiSDWAwvIcUM02K-9PF9URfyqzku_eSqisA-4fDC_NM8VT0rhaUOwiVSdQrh7YEYmnxZEOt9TLkdKPPFn1YIk62z072_JRzVrqBUpy__SvC_Uwo5mtW785deHdbeJxAJdv0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:
ایرانی‌ها می‌گویند که تنگه‌ها را ظرف ۷ روز باز خواهند کرد؛ [در حالی که] تنگه‌ها باز هستند.
ما اکنون به‌طور میانگین روزانه ۱۵ تا ۲۲ میلیون بشکه [نفت] صادر می‌کنیم.
نتیجه این است: ایالات متحده بیش از ۱ میلیارد بشکه صادر کرده، و ایران صفر.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72374" target="_blank">📅 19:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72373">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15b7065503.mp4?token=lyHaGD-JYwd4GecizV2cJMw6FCms-6s0CZQ8DtweJAKk39xwnoOvo0Y0ez4llwju0t5Ov1GyPkOOoW68UurvZOLvmNgJLQjYbPTLQePLGKK8b5yPW_NnZBwq5ZHT3tWScdCO6ITJCYDEkpyaoK_hps1Y0hhsu-1tMrLTJbi3deav6JJU7OP7Fy5WQWcrBGxfEfLGXo17FvnuWwSQ9DY8XzYDFHo9gPg-2gMwWJ1KNoiBDzCNOd-YIkOBAUCbjO00KPCy2tFkUSISs9rmWjwp8TuGgEQfZ-xq9Dei6KJCJg-e8Otl_GFGWmja8mFFh6vRQ76kb6YX9z4OOouNk7_DOIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15b7065503.mp4?token=lyHaGD-JYwd4GecizV2cJMw6FCms-6s0CZQ8DtweJAKk39xwnoOvo0Y0ez4llwju0t5Ov1GyPkOOoW68UurvZOLvmNgJLQjYbPTLQePLGKK8b5yPW_NnZBwq5ZHT3tWScdCO6ITJCYDEkpyaoK_hps1Y0hhsu-1tMrLTJbi3deav6JJU7OP7Fy5WQWcrBGxfEfLGXo17FvnuWwSQ9DY8XzYDFHo9gPg-2gMwWJ1KNoiBDzCNOd-YIkOBAUCbjO00KPCy2tFkUSISs9rmWjwp8TuGgEQfZ-xq9Dei6KJCJg-e8Otl_GFGWmja8mFFh6vRQ76kb6YX9z4OOouNk7_DOIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت درباره ایران:
تنها ۱۵ میلیون بشکه دیگر از نفت ایران روی آب باقی مانده است. ایران دیگر چیزی برای معاوضه یا دادوستد نخواهد داشت.
احتمالاً ظرف دو هفته آینده، آن‌ها آخرین محموله‌های نفت خود را به چین تحویل خواهند داد و پس از آن، دیگر چیزی در اختیار نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72373" target="_blank">📅 18:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72372">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBSj7Il9UdKeTue6aNkCTXLWNYEFRB81VMtDC1Y9eRT26D6QKcWrpfqnaVDaKG1HCsbW8FlyQAmiEkm3WnN6OyyP00EXi2lrYolaVmi4ymqph5X2e1nx5Ob7sWhyIfTXj27PZmrA0G2r5qoz_Aj9D9117uRdhrUmjW7wYjI9DQRqQ85_m8bEfNSyG6HI1jAB8RWOM_SbgTRoh69dZkO61JtqEmYIjcrM4n-nm89MgQOnq-9KJTOpMUiyXy37nRi8VsRTC088JXA40_58PHJ7jRKIQ-ZPeVTk_YMS0SoHdPshyI4gNDKtVX7_COwkhOLraqfuaswQEWyDw4A3p8Jeww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به «اکسیوس» گفت که با وجود رد پیشنهاد ایران، انتظار دارد در هفته جاری مذاکرات بیشتری میان آمریکا و ایران انجام شود:
آن‌ها خواهان توافق هستند، اما این آن توافقی نیست که من می‌خواهم. آن‌ها در بازی خود زیاده‌روی کردند.
ترامپ در پاسخ به پرسشی درباره ازسرگیری حملات:
همواره به آن فکر می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72372" target="_blank">📅 18:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72371">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd27ff889b.mp4?token=rTCUwEbEHc5hLBI9KXsjraqlsWqkASwc9ENMce3NcYeQfD4GtREbF3vK_yW6thp90PfbJDquSAAN9bySwQnICGmTvxw59MKMx4OUPiIhJXvq4OxV_9Xezi9e42u8o7yIR2FikUtqwrPEWUCvtlAxdwvTD1y9O5Npx8eSDUcWNl7hgdsxL0q1NphMmenNcke0wxDXcEq0un5er0tDd2wxvqQLgpOn7mJZqrgEoqX46VRKR4Ss7R5lloHjxx_e3bM2GGs9kOXnOEPK3umnR46DfDMwlt8_J9XbWrGxmFbMsQBjeH4qBtaTYDw1tTMLPTMojoju1y8MExq4BQkng4vk5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd27ff889b.mp4?token=rTCUwEbEHc5hLBI9KXsjraqlsWqkASwc9ENMce3NcYeQfD4GtREbF3vK_yW6thp90PfbJDquSAAN9bySwQnICGmTvxw59MKMx4OUPiIhJXvq4OxV_9Xezi9e42u8o7yIR2FikUtqwrPEWUCvtlAxdwvTD1y9O5Npx8eSDUcWNl7hgdsxL0q1NphMmenNcke0wxDXcEq0un5er0tDd2wxvqQLgpOn7mJZqrgEoqX46VRKR4Ss7R5lloHjxx_e3bM2GGs9kOXnOEPK3umnR46DfDMwlt8_J9XbWrGxmFbMsQBjeH4qBtaTYDw1tTMLPTMojoju1y8MExq4BQkng4vk5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی:
ما همان‌قدر که برای مذاکره آمادگی داریم، برای رویارویی با هر چالشی نیز آماده‌ایم.
ما در برابر هرگونه تجاوزی علیه خود قاطعانه می‌ایستیم، حتی اگر کار به جنگی آخرالزمانی بکشد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72371" target="_blank">📅 18:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72370">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حملات اخیر پهپادهای جت‌سوز روسی «گران-۴/۵» (Geran-4/5)، یازده مرکز داده اوکراین را هدف قرار داده است که شامل ۱۰ مرکز در کی‌یف و یک مرکز در دنیپرو می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72370" target="_blank">📅 18:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72369">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c66f5a0a1.mp4?token=QG-QpkRJJNj7FK5elUXgoNhS_7tjDkDSdtbi_6W2P7iulzf07xVqktQ5WKVAZmIas7p8GCNNJfcKB5pIWmm6rFRBziFWUnHvVnoEqRKxIYUgx4BzmltomkXdMkhFusssrSoGODmm4eMu5eQlIm4jNxYLKHdJxUjAReMmnDOm8ejPxt_z22zZ5lhr8kGxsVYk0hZFYXHjIerbmSodXVFI3eBzZHD79_xx91DvUC-Yj08YNRwkjHnvmQtqjZiX9sHXvhEXs70G1mwOoYTswXzrF08ly1yeW_KFtjrkdf0auvRxiiaAe_eTrj2fqv61rmx_ACQS22lCIOJ4aDXa04kCvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c66f5a0a1.mp4?token=QG-QpkRJJNj7FK5elUXgoNhS_7tjDkDSdtbi_6W2P7iulzf07xVqktQ5WKVAZmIas7p8GCNNJfcKB5pIWmm6rFRBziFWUnHvVnoEqRKxIYUgx4BzmltomkXdMkhFusssrSoGODmm4eMu5eQlIm4jNxYLKHdJxUjAReMmnDOm8ejPxt_z22zZ5lhr8kGxsVYk0hZFYXHjIerbmSodXVFI3eBzZHD79_xx91DvUC-Yj08YNRwkjHnvmQtqjZiX9sHXvhEXs70G1mwOoYTswXzrF08ly1yeW_KFtjrkdf0auvRxiiaAe_eTrj2fqv61rmx_ACQS22lCIOJ4aDXa04kCvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جعفرقائم پناه؛ معاون اجرایی پزشکیان:
به عربستانی‌ها گفتم انشاءالله برد موشک‌های ما به آمریکا برسد تا دیگه به پایگاه‌ آمریکا تو کشور شما حمله نکنیم بلکه مستقیماً به خود کاخ سفید موشک بزنیم
😐
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72369" target="_blank">📅 18:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72368">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72368" target="_blank">📅 18:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72367">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fjQAFv8yezfmSEfi6j7FFs9gqScjjMNWdiMIIQdJ0lxrEAm6I9_Wh2KBpQiwkNaaQY1nW6bx_e0SNwQZjjpIKw4vjcRo7VBQISQHKJkRDpJe3cjcCWyXFKk20yaKJcPjjntb8W2fqZSCNbYN4G7VJcBe38bijEzPf4wQzE2Oy65htUlMKOIpbbmK3TEH_WqhiDnYr6JxAzsRCL3vCmyiwqxJzskYrcgRwAp0jniYw9z-9ENNjTTGH7Ul4B5IarpGJxQag5IwHm-Rws0M3bBQ2HDuxzfXZ7BriEq0b5fWarYVPQvmLMQk8hjpiwFYV0L9N0ADpGYlLY763CfztPtADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72367" target="_blank">📅 18:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72366">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a495b9a3cc.mp4?token=qEc6hFofHPa5toSPNYCnWCS9XpvPduxv-oUkFeQs4PwIYftDCCI_OAvOa7V7L7xNUgFHx2nMt9mw2WbKhvLxCRjt8iIy_RHTdYu3Jbu-XPS8eJtWJIK5nNJRPMnwfGqhr4RWLKoBUT7sZc5hhj6yq-O42LqVxMJXO65eH3bxdEMpbgJ3w_OkGCMNBZt84wHWukOAacl3ppnRndb9Oxh5KOVob57sVbWAYniqX6h9KmxCr3k_Y0aVLyfEwAwuWjVV3Y6Y3vgPHwNGKYasYX8T_bHodrY7fkTMkTpES5-VptneboBIiGJIdFvBCJkzvshijExMzMubYzeZQQWyCHJdAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a495b9a3cc.mp4?token=qEc6hFofHPa5toSPNYCnWCS9XpvPduxv-oUkFeQs4PwIYftDCCI_OAvOa7V7L7xNUgFHx2nMt9mw2WbKhvLxCRjt8iIy_RHTdYu3Jbu-XPS8eJtWJIK5nNJRPMnwfGqhr4RWLKoBUT7sZc5hhj6yq-O42LqVxMJXO65eH3bxdEMpbgJ3w_OkGCMNBZt84wHWukOAacl3ppnRndb9Oxh5KOVob57sVbWAYniqX6h9KmxCr3k_Y0aVLyfEwAwuWjVV3Y6Y3vgPHwNGKYasYX8T_bHodrY7fkTMkTpES5-VptneboBIiGJIdFvBCJkzvshijExMzMubYzeZQQWyCHJdAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایران:
به‌محض اینکه ایران تسلیم شود و جنگ پایان یابد — که به‌زودی هم چنین خواهد شد — قیمت نفت به‌شدت کاهش خواهد یافت.
قیمت نفت سقوط خواهد کرد و قیمت همه کالاها پایین می‌آید؛ البته قیمت مواد غذایی هم نسبت به دوران بایدن بسیار کاهش یافته است. تقریباً قیمت همه چیز پایین آمده است.
قیمت نفت اکنون نسبت به دوران دولت بایدن کمتر است.
ما مقادیر عظیمی نفت استخراج و عرضه می‌کنیم؛ دیشب رکورد جدیدی در انتقال نفت از تنگه هرمز ثبت کردیم؛ مقداری بیش از آنچه پیش از آغاز جنگ از آنجا عبور می‌دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72366" target="_blank">📅 17:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72365">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ccd821b0.mp4?token=jhNJN_TA7c7_6hSFo6uU7RZ8dp2Nb4u05c3Ludkt74B2_kqbZjKSGYc4eTgkSehjbw2bKrfsMwsi2lk4YwGTbXWBSbTNSVozdgEU8DsYWEqtFV1VUlxV-hlYdQbsc-yGNuKGSzGE2HgLqs8h-pCexlCAtWpiLWbc7Ur75BllCxHUU6WVqSBkwkCz_oB_nXIZMwuFaWgz7IyHoIgkp781JfGDP0pg2ZhJUrG7Fqe3fPLqjc8cdwKhhlrEWhYOCihNcwc2UMQpUG_bta_oAgwVTMmDOKA-SKgmqjlWNaK6H8OcWVDOfTht1tesmohcyTNXSMbgsiBGnu1p_EdX4AUjeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ccd821b0.mp4?token=jhNJN_TA7c7_6hSFo6uU7RZ8dp2Nb4u05c3Ludkt74B2_kqbZjKSGYc4eTgkSehjbw2bKrfsMwsi2lk4YwGTbXWBSbTNSVozdgEU8DsYWEqtFV1VUlxV-hlYdQbsc-yGNuKGSzGE2HgLqs8h-pCexlCAtWpiLWbc7Ur75BllCxHUU6WVqSBkwkCz_oB_nXIZMwuFaWgz7IyHoIgkp781JfGDP0pg2ZhJUrG7Fqe3fPLqjc8cdwKhhlrEWhYOCihNcwc2UMQpUG_bta_oAgwVTMmDOKA-SKgmqjlWNaK6H8OcWVDOfTht1tesmohcyTNXSMbgsiBGnu1p_EdX4AUjeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمود کریمی، مداح حکومتی، در مراسمی برای علی خامنه‌ای نوحه‌ای به زبان انگلیسی خواند
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72365" target="_blank">📅 16:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72364">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94d47f6b44.mp4?token=UhRdCgACTkMz6e2QPBMbDeAFpeklRs2bl2pL5ycugUpXR82AhPpgf1fOai5AES_9DrMG0e5uehOjwHGHQTKXv-6PUKQ4QDL5LFY6iwpab4mPYqXsEP4Epskr5Z2PwwaEpdarY9EBqAj02dGpHAtWX0MVixQdfKbTGcUdZPPF-taHWD7bwYbl85JnKwnd20XYiCZmhdQ8ywt4ae-4F_KlDfjqnYwXeyb1A3KD3CCsdmQwSXfOxw36ssTK2v99Jt75VcutK8-TVb549Dj8LZ69YrLBVOrnyArKqFNXRLxF4Sy0penlA9xiFJnZVHxEsPaEpk-UUH6-scrl-NloKMEjWJ4lW5p2iiY3BS1ZbXPLj_pLub4fSIaZek3fzZLi_5SIaS-8KUWcypQgMnaC6ZTQGlGWPyEwa5xVzhiKQ8sP7c-96DWDPA3cbVbSTHHZDqGxahRLLEDzhgt2EbEwclSxx-aJaEFTAGTexlPR_8-uDlbe7ABXM0YJbGpZ3HyxCQmIFaAF8JWHNhEmCMtEIGithmV_nzqK3VtdTIvxNO3agMl76gJXN7HNNXeDj5B6zuxXEnoIIk8gFGb5UVm6tzP21yQReEUJEyetbGwXWgWBLQe5d2uhlWzs-tLY7HINh7KwgDkHNDO7p8kv6eg7udXcIM20WKVgDqIFA6mnV2Hu1-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94d47f6b44.mp4?token=UhRdCgACTkMz6e2QPBMbDeAFpeklRs2bl2pL5ycugUpXR82AhPpgf1fOai5AES_9DrMG0e5uehOjwHGHQTKXv-6PUKQ4QDL5LFY6iwpab4mPYqXsEP4Epskr5Z2PwwaEpdarY9EBqAj02dGpHAtWX0MVixQdfKbTGcUdZPPF-taHWD7bwYbl85JnKwnd20XYiCZmhdQ8ywt4ae-4F_KlDfjqnYwXeyb1A3KD3CCsdmQwSXfOxw36ssTK2v99Jt75VcutK8-TVb549Dj8LZ69YrLBVOrnyArKqFNXRLxF4Sy0penlA9xiFJnZVHxEsPaEpk-UUH6-scrl-NloKMEjWJ4lW5p2iiY3BS1ZbXPLj_pLub4fSIaZek3fzZLi_5SIaS-8KUWcypQgMnaC6ZTQGlGWPyEwa5xVzhiKQ8sP7c-96DWDPA3cbVbSTHHZDqGxahRLLEDzhgt2EbEwclSxx-aJaEFTAGTexlPR_8-uDlbe7ABXM0YJbGpZ3HyxCQmIFaAF8JWHNhEmCMtEIGithmV_nzqK3VtdTIvxNO3agMl76gJXN7HNNXeDj5B6zuxXEnoIIk8gFGb5UVm6tzP21yQReEUJEyetbGwXWgWBLQe5d2uhlWzs-tLY7HINh7KwgDkHNDO7p8kv6eg7udXcIM20WKVgDqIFA6mnV2Hu1-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک بالگرد رسانه‌ای تصاویری از بمب‌افکن‌های B-1B نیروی هوایی ایالات متحده ثبت کرده است که در محوطه‌های پارکینگ شرقی پایگاه نیروی هوایی سلطنتی بریتانیا در «فِیرفورد» (RAF Fairford) مستقر شده‌اند؛ این در حالی است که یگان‌های خنثی‌سازی بمب همچنان مشغول عملیات پاکسازی مهمات منفجرنشده در منطقه «وِل‌فورد» (Whelford) در مجاورت این پایگاه هوایی هستند.
این پایگاه برای ایالات متحده در جریان جنگ علیه ایران، نقشی حیاتی داشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72364" target="_blank">📅 16:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72362">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7NpwbLIfsbKaLpkMXZgnK7Wix7fNxJFpw_d6293VVgF_mUpnCCpM0zPycMdIGA6Tn9HSyCYOC_2SE5lUCP-KiLyy1Ctd9wSaG6VrM3ZdOLIpyKFw4n78FXGkOYjLuL0mjVBut73NEbz4giK6VP5hjwNXNPYvvWhKOABKsvo_vIl79N9bVJbr2csdtxf9jEi9g8fv32eGWzgswi_CA_3qs66sigHGT_OcBtUAyLk0NfjbvWYFlu5_bFolrNi1YAeK_RMBVXmB14u8WKZYZPf8Vl2n5O1pwFmuWBr_Mkkv35QduDMc14tiyizShm7fddW9fpe68FWyxITMnr6YxtKNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a6bd02b6.mp4?token=lAgN5d-Y1jVBf7kJLbmEIEMXxgv8xaA2aS572ZO76m40Ep8H1rz9M4u75kfHZN5xNihYEawcdGw9PBkYydXst01yOxMwZuujqCJRxj8-se8bgGJ1TCZYtLsn92cdcDBp29AEKuX9mSwwmUl21fXNWoCdr_h7v0iSa1IAmcOFk5yjL8Js7YxuG_QFIzG1yWbGO8Ddl3SN1UQY2sNzxDmrNfhopKVzgBNX6OjehtaeRQ38AnMLU7ULeYHr3qQrvmAqmjyLX4LhWN727EHD0rT4iuJKwJn5fjAyzHDz0um0aS7Ac3MuJEFbNHSaFlMjQD5SyCIkZTEhPo8AOwT3KZM64Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a6bd02b6.mp4?token=lAgN5d-Y1jVBf7kJLbmEIEMXxgv8xaA2aS572ZO76m40Ep8H1rz9M4u75kfHZN5xNihYEawcdGw9PBkYydXst01yOxMwZuujqCJRxj8-se8bgGJ1TCZYtLsn92cdcDBp29AEKuX9mSwwmUl21fXNWoCdr_h7v0iSa1IAmcOFk5yjL8Js7YxuG_QFIzG1yWbGO8Ddl3SN1UQY2sNzxDmrNfhopKVzgBNX6OjehtaeRQ38AnMLU7ULeYHr3qQrvmAqmjyLX4LhWN727EHD0rT4iuJKwJn5fjAyzHDz0um0aS7Ac3MuJEFbNHSaFlMjQD5SyCIkZTEhPo8AOwT3KZM64Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی ارتش اسرائیل لحظاتی پیش منطقه «حداثا» در جنوب لبنان را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72362" target="_blank">📅 15:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72361">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a85f2632d6.mp4?token=LxXqK9rm19_EakoiMdLX-z4P4-qnF92EW2rieTZUGExXg8QAGEvUUKg_pUOd7rOdJwhubk1VP5DT-iLLhV2-MfoUn05doFaX2WDtcLAf3VZPsq8FejwjOwXj8hep58vgDdcN_Ufsas16pzkPoqlsqV2pdD9SuSLSRCxKPtOvGrUDBvac-juPkJ99jmok6Qhl5Y-d18TB9WVX5AZWIybOAURU5A9miG5CGLN3C4Ps76ZctCVzGEPpQ0d9U04M4rQW-e_olHn3IbI-ZXOhLDLEuM0tAmEGB92JGs3CvWgewmVkjlZSLQ07dHfo_gegFhpWxyy-TEvm4Zbz26KdZ60jzDcl7yF8hUMpTFLSaa8DV2j2HTbPLQncqInH-meSDPsJbN6zm6JmqNowIpJZ8rw5v6ss8eoFIHKXJb_0Xe1kO-iemAsTtlI3MRclgi_lSg3mz_EkIhNGmKwPZd0IHX73eTRIJbj4UbL79zrjp8fE7omIaQ3V4Kyj2jqEqrAmGLFMVkc-8dG1W5ISmdVapeXEJpJ1zneTsZo7PNJdBSm9aiCEjXrLE_ha9GLH_Q0TTN5lzWzUczEdYZMvvVnLTTmikuvNYJxs9tMsZXnhCGVPgkat8lrSo87g9LfmK7saozmPR8wtvUxaqB8PLhIeCMzWgWduR6fq4oR0Dnmu-Zq_S5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a85f2632d6.mp4?token=LxXqK9rm19_EakoiMdLX-z4P4-qnF92EW2rieTZUGExXg8QAGEvUUKg_pUOd7rOdJwhubk1VP5DT-iLLhV2-MfoUn05doFaX2WDtcLAf3VZPsq8FejwjOwXj8hep58vgDdcN_Ufsas16pzkPoqlsqV2pdD9SuSLSRCxKPtOvGrUDBvac-juPkJ99jmok6Qhl5Y-d18TB9WVX5AZWIybOAURU5A9miG5CGLN3C4Ps76ZctCVzGEPpQ0d9U04M4rQW-e_olHn3IbI-ZXOhLDLEuM0tAmEGB92JGs3CvWgewmVkjlZSLQ07dHfo_gegFhpWxyy-TEvm4Zbz26KdZ60jzDcl7yF8hUMpTFLSaa8DV2j2HTbPLQncqInH-meSDPsJbN6zm6JmqNowIpJZ8rw5v6ss8eoFIHKXJb_0Xe1kO-iemAsTtlI3MRclgi_lSg3mz_EkIhNGmKwPZd0IHX73eTRIJbj4UbL79zrjp8fE7omIaQ3V4Kyj2jqEqrAmGLFMVkc-8dG1W5ISmdVapeXEJpJ1zneTsZo7PNJdBSm9aiCEjXrLE_ha9GLH_Q0TTN5lzWzUczEdYZMvvVnLTTmikuvNYJxs9tMsZXnhCGVPgkat8lrSo87g9LfmK7saozmPR8wtvUxaqB8PLhIeCMzWgWduR6fq4oR0Dnmu-Zq_S5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریه های یک خانم به خاطر شرایط اضطراری که واسش به وجود اومده و عدم وجود سرویس بهداشتی در مترو.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72361" target="_blank">📅 15:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72360">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تمسخر پزشکیان در شبکه فاکس‌نیوز؛
در مصاحبه ای که با رئیس جمهور ایران پژاکیان(پزشکیان) کردیم همش جوابای مبهم و بی معنی میداد.
اصلا اون به هیچ سوالی جواب نداد.
حتی نتونست بگه رهبر رو دیده یا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72360" target="_blank">📅 14:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72358">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2lmjQVNtPmE0_pna8iphJMizllKlK3E3ZMyttCnW3M894tus8ppxjdOAmh3GwnmLoUpHdA-_BDO30Y55FmHgu5OGd3WJ_bKa1vDyQvGrZzMsuOas5Hd8VjxXSC4Lx6eSAZU6SmmMbBm4q39QdirMxWT0PBh7ni6w3ZsnVQyYEdppnuIcQ-ZSl3qOkIUxldG0mw8OGCv6cRROr7w-nw73PfMlHQ9Fji35GMrbpcQL7s2UiwhaiVUwExX59He4XPqCfrxuvoaUb9bznCkza23OroV_9xQmQBuhap9F7U2q5CvXRHPvapRkVVbNnsa6B7HXrsA2tvGTvNCDxYtKzsReg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2634d568.mp4?token=FbqxVP7dqrrItdoeD-uoeZbbQA8ohAIeK-3hwfhtrK6qdIqH6spUP1WB2FUkxDxnpKGsR4oGZNPl_ViOWgvKiP7LuEDd9OVVXHIA9xgTuXDv32XlsEQ3PnwEe2iVbvIqLFcz-VSufh0E1sgI9HoOg7RyM8mG7h7SK0d65O7D9gg0OgeBMWYHDz7LEm-pTmC0Dth0ubr4VFABlo7CHUlc7wZWmp5yDNAD5IFrFhUpehHxB5LRZyoteNUgWYXaTsINJH28JpJmiZNGns34gaz5IoiiJOXZYeF10JBpkPFI8Lold3fyOft5Tf9dJEGPBTnt-4mBATDE4W7vYocgQQ8A7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2634d568.mp4?token=FbqxVP7dqrrItdoeD-uoeZbbQA8ohAIeK-3hwfhtrK6qdIqH6spUP1WB2FUkxDxnpKGsR4oGZNPl_ViOWgvKiP7LuEDd9OVVXHIA9xgTuXDv32XlsEQ3PnwEe2iVbvIqLFcz-VSufh0E1sgI9HoOg7RyM8mG7h7SK0d65O7D9gg0OgeBMWYHDz7LEm-pTmC0Dth0ubr4VFABlo7CHUlc7wZWmp5yDNAD5IFrFhUpehHxB5LRZyoteNUgWYXaTsINJH28JpJmiZNGns34gaz5IoiiJOXZYeF10JBpkPFI8Lold3fyOft5Tf9dJEGPBTnt-4mBATDE4W7vYocgQQ8A7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی
سپاه پاسداران:دومین زهپاد(زیرسطحی )ارتش آمریکا در تنگه هرمز شکار شد.
شناور توقیف‌شده از نوع پیشرفته «Remus 600» است که به گفته سپاه، متعلق به «ارتش آمریکا» بوده و با اهداف جاسوسی فعالیت می‌کرده است.
این شناور طی یک عملیات هماهنگ و با بهره‌گیری از قابلیت‌های اطلاعاتی و جنگ الکترونیک توقیف شد و هم‌اکنون برای استخراج اطلاعات در اختیار کارشناسان سپاه قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72358" target="_blank">📅 14:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72356">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4389424237.mp4?token=Wi6da4WltoNoustOGX8TV3OnHk6wSh2zSCyz1BbUXHW7Owv-l8XpRRmzeJoZcELv19ezuEElhH18zqhLbIyzc62wSz5LfQqvR8n5mldi8Pf0r1WJjlCYlZwh2Dhgou3RDESLQcBREMU2cdWAOhqNVMdogtE6GtwzhvziAVbNmTRgvRjI6CraKk3-IefEsZgNcyk7Fc3nTe5-qggMdhK8PhyMHxT1CMg9qDIjTWHUgtUQpVoj9E3cVZ0mQIc6B4BImF2cFJjSEypkZ7_CHAHpGQ--W0RJ1QtzKp4l5yelkZ3KfFGgDCxrtz4xHG4mIDdFs0P_CCClbGoYPdp3TvhVBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4389424237.mp4?token=Wi6da4WltoNoustOGX8TV3OnHk6wSh2zSCyz1BbUXHW7Owv-l8XpRRmzeJoZcELv19ezuEElhH18zqhLbIyzc62wSz5LfQqvR8n5mldi8Pf0r1WJjlCYlZwh2Dhgou3RDESLQcBREMU2cdWAOhqNVMdogtE6GtwzhvziAVbNmTRgvRjI6CraKk3-IefEsZgNcyk7Fc3nTe5-qggMdhK8PhyMHxT1CMg9qDIjTWHUgtUQpVoj9E3cVZ0mQIc6B4BImF2cFJjSEypkZ7_CHAHpGQ--W0RJ1QtzKp4l5yelkZ3KfFGgDCxrtz4xHG4mIDdFs0P_CCClbGoYPdp3TvhVBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال پیش در چنین روزی سید حسن نصرالله به همراه چند فرمانده ارشد حزب‌الله و سپاه پاسداران در حمله نیروی هوایی اسرائیل کشته شدند.
در آن عملیات ۸۳ بمب سنگرشکن ۲۰۰۰ پوندی به مقر فرماندهی زیرزمینی حزب‌الله در زیر یک شهرک ضاحیه بیروت اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72356" target="_blank">📅 13:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72355">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a6a80862.mp4?token=rZEjokzEv1aEg8i4uYcGaidGLUwy4wRO1-sqI9V7CbgZ3gWGGZ7jzxmL8TW18SkALSNYXJ0qXxop4T8K7Zk_LLyRt_ktEE1FTtPbvumwc3yLF3_OJeqYzT-g6WeNsF0O61_6nGZbt232w1Wg52pcyD_5axm03XS_k10MWVjBsh9_8OkRYnCFy55evEvU-YwCnuC_xoJd1lPeBRoyXLCqaXE6B9AYtlCQLqAViVDVSPIN_r1swZVRvzaZ-txTsxiDCbeplaaa0sjJluqSy-QEk6uMuXv78Ao8rOwKub1OMZt--pKBvQh0zVeCVDux___hZcuS_gynVnurF9j-NFxVbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a6a80862.mp4?token=rZEjokzEv1aEg8i4uYcGaidGLUwy4wRO1-sqI9V7CbgZ3gWGGZ7jzxmL8TW18SkALSNYXJ0qXxop4T8K7Zk_LLyRt_ktEE1FTtPbvumwc3yLF3_OJeqYzT-g6WeNsF0O61_6nGZbt232w1Wg52pcyD_5axm03XS_k10MWVjBsh9_8OkRYnCFy55evEvU-YwCnuC_xoJd1lPeBRoyXLCqaXE6B9AYtlCQLqAViVDVSPIN_r1swZVRvzaZ-txTsxiDCbeplaaa0sjJluqSy-QEk6uMuXv78Ao8rOwKub1OMZt--pKBvQh0zVeCVDux___hZcuS_gynVnurF9j-NFxVbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابطحی میگه: سال ۸۸ توی زندان گفتند اعتراف کن که خاتمی به اسرائیل سفر کرده
گفتم خب سفر نکرده
گفتند اگر بگویی که به اسرائیل سفر کرده، آینده دینی ایران را ایمن نگه می‌داریم...!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72355" target="_blank">📅 13:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72354">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnfS08iQdqJT0DVmcfpiceIuMx33VyoB8RkxQoARfe5I92vpN1dYrZ9Mb-UeLyy8cQokPV-CH0d2s4UcidbS7KSGX0AlGm-XS9lvdFdJqoCiERJiMgCFTprM3LBrlUJYi1km3oOO5WB24viHivroCySV-QnWkzN7N13TdVnDEosEzldBAfIfSKFNZ8WewDT_mHQJBi7E7rXOZWfvkcRDXj6bz9HMlma4WNDpONU7VEzUES0sHe23RjrARXttuDgj5_X_Zq0hM2pXoj1w68u0KMqSkb3ebTjpJw63ovGlHqXe7Ef_BysUt4IpDo-PqmCP-0SAjQagIZG9XygEYKRtgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت وزیر خزانه‌داری آمریکا:
در پی آغاز «عملیات طرد اقتصادی» (Operation Economic Outcast)، وزارت خزانه‌داری ایالات متحده اقدامات مالی هدفمندی را علیه بانک‌ها و شرکت‌های ارائه‌دهنده خدمات هوانوردی اعمال کرد. به دستور من، تیم‌هایی به سراسر جهان اعزام شدند تا با کشورها رایزنی کرده و خواستار اقدام علیه رژیم ایران شوند.
این تلاش‌ها در حال به ثمر نشستن است. ترکیه و عمان از توقف پروازهای «هواپیمایی ماهان» به کشورهای خود خبر دادند. امارات متحده عربی نیز تمامی پروازهای شرکت‌های هواپیمایی ایرانی را متوقف کرده و بانک‌های تجاری بزرگ در امارات و ترکیه، انجام هرگونه تراکنش مالی با ایران را متوقف ساخته‌اند.
حتی رهبران ایران نیز به پیامدهای اقتصادی این وضعیت اذعان کرده‌اند، چرا که ارزش ریال به پایین‌ترین حد تاریخی خود سقوط کرده است.
من از دولت‌های بریتانیا، ترکیه، عمان و امارات متحده عربی قدردانی می‌کنم. ما به همکاری‌های خود ادامه خواهیم داد، زیرا برای جلوگیری از پیشبرد دستورکار تروریستی تهران، هنوز کارهای بیشتری باید انجام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72354" target="_blank">📅 12:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72353">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72353" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72353" target="_blank">📅 12:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72352">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1DY_iBEECvQ5-HaHpFT1lDrG4yGmLXgdg-D4shS24TLrih4lu5eEuqJGYsgbQSFP38WAadQ-vsoG7husd57ifrCEFJh7FzxcltUsyYBn4g9bmpGdKZ0ln_rUPL-HBiePTZe3xhmqxnVUEKQJXeU93ksrElwtHKZSEIOp534LTyfa7xN3Ao1cegN6eLs_Qd04aS0mG95i6Ypc9Yrnl8Tct00hg0jTgG0ajeT1u8UTo0w4YCHvejqeAKRe_Mv4E5PUmDKfaRfPjqLutCVM6Hjro3nZEUXNNs5U1dzXxy8AZ7KEFAgt6mStHGfxUYSilNP-UgM7VMcWpDe_ataVU4B_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
پرتغال
🆚
نروژ
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
پرتغال: ۳ برد، ۱ تساوی، ۱ شکست و ۸ گل زده
نروژ: ۳ برد، ۲ شکست و ۹ کل زده
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72352" target="_blank">📅 12:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72351">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مدارس ریاض به دستور مقامات سعودی و بدون اعلام دلیل رسمی، به مدت یک هفته به آموزش از راه دور روی آورده‌اند.
این تصمیم یک روز پس از آن اتخاذ شد که پدافند هوایی عربستان دو پهپاد حوثی را که ریاض را هدف قرار داده بودند، رهگیری و منهدم کرد؛ اقدامی که در بحبوحه تشدید حملات حوثی‌ها به این پادشاهی صورت گرفت.
در دو پیام جداگانه که خبرگزاری فرانسه (AFP) آن‌ها را مشاهده کرده، آمده است: «به‌تازگی از سوی مقامات سعودی مطلع شدیم که مدارس باید در تمام طول هفته تعطیل بمانند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72351" target="_blank">📅 11:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72348">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NY6uhe5EovcTeqNqxkF_57M4tpWIL1onz_Gf3EgBkojeJ_33M-s9XBXJ_69Zf2mSLY-Mq10LvINfRxSwj0AvZYytlFEsotg9ZY-B6GARS6DLXqmUG4OxHF6GeopP_EXFItZmkBc-o0QQ69EAYLzAOxKZnrfFo7y_Id0z7YkGS79wUPjnldOEq52RgHTpDqVGBj4ddGlTECuajpsQ-CcGoPwxl_0hItlNNvRs1_jl6FCg-QQU0ZCe-gSoniRgY8BY2jlV5neHqhwRxaRIdPYJGb1GCUDyeKuGYdmGr7gvUmNCONGEnOm4unI2aCbJfxGYFyry-BtDk_7COnuXKwz9Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3GUBh2mSZgFl0BF_xsvvMa7yYRm7hjmbU9-L5vWl4EY6dCHr_x_d5HT4jES6jToGpzIA3uG3TOerfQDLwkhBEJIrThg3xWMkY_Pvrvu90jCLt1bG8ewp8SK5ZVutVUYCQFVDW49VNSL5y76z8OoiOgrf1zNsmeVC8F_AxW994ZARlPO33QtSruzEuRGT2J3eT2Q_EiOrP53Fhzmh7tIRSjjhayQN4J60krX5ZhylFJxR-IErsfuMFM54BBaemlq7MwlP913lV_cdX_6eGWzjVljUW42yuL6qZnlJ-o9Ea7iCnZvqHETgqPa2Hh11o1MD-4mSNjlghqOcmu_YzurSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sOiR41_RFh4gwbdBHyUSm-tSspHshHiHwb0v7PF-xrcn-vjXSoIuxk4yXVTRg8ORl9YsV5F8mPtNkVhmR8CIj2uIDfm_Va_cfzq32EJ2qUAzgfs8vcVxd3MK7oDTdfETzdbEP_r8D8NmSkyzWpBIl8fiaJOq9jVHdwCz4qveQ3Cd3ZHRmXJ9EajMGoQB6SgMIK8HpfeyDefQt5wEHUnfZ3GlNW3WZqG0_lEAz-P2WVr3r7AMb98WPX-mYDP30r2fyHbtd-pjQQdBz6LEzYtjpUX6XhdGdlZ0znXG8JmEyW2ut7Wczy_pz8DNpzdVXMVD8yiKWkJAUH_K29JfLBu__w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رژیم جمهوری اسلامی که خودش فرودگاه نجف را ساخته بود و هزینه‌ی آن را تقبل کرده بود، از استفاده از این فرودگاه محروم شد!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72348" target="_blank">📅 11:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72347">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7c28b66c8.mp4?token=nNYhUdP63u2Lz-RTmxmElz_O03h_8DYx7JWFZBbYgGoB0iPZV3-_0CgtJ_BX3mZKMVKVubEwC0mkeT3ac4-UGjfK39YAqljdBJDZlQuAujvIb3cEH2YMToHC52U07fNwJmJvsJsPaB1E_Co07CK14DyMTk_Wvi6gU4nLaYqpcCpzDsv8QbWyBNH7ZBPj33vpqGzIvKPBDbbeTQE25p0yFqBvyPL6z4cYKVE5s7HFu6H81U-MrIjESrHdC45bmVtfcQO2bxk7xGMCkM2L0KQVTECy41rh7QhNKVCQ2X6A9V4keW1Z5MKc2N5arYrycZ9vrQ17VEkcUFGS1rB07G4ijg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7c28b66c8.mp4?token=nNYhUdP63u2Lz-RTmxmElz_O03h_8DYx7JWFZBbYgGoB0iPZV3-_0CgtJ_BX3mZKMVKVubEwC0mkeT3ac4-UGjfK39YAqljdBJDZlQuAujvIb3cEH2YMToHC52U07fNwJmJvsJsPaB1E_Co07CK14DyMTk_Wvi6gU4nLaYqpcCpzDsv8QbWyBNH7ZBPj33vpqGzIvKPBDbbeTQE25p0yFqBvyPL6z4cYKVE5s7HFu6H81U-MrIjESrHdC45bmVtfcQO2bxk7xGMCkM2L0KQVTECy41rh7QhNKVCQ2X6A9V4keW1Z5MKc2N5arYrycZ9vrQ17VEkcUFGS1rB07G4ijg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌سخنگوی ارشد نیروهای مسلح ج ا :
آمریکایی‌ها باید خواب این را ببینند که در مدیریت تنگهٔ هرمز دخالت کنند و در صورت دخالت سیلی از نیروهای مسلح ایران خواهند خورد؛ آن‌ها باید از منطقهٔ ما بروند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72347" target="_blank">📅 11:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72346">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/58f2375d54.mp4?token=soyGepN27iKZSMrFWIrro5kBQZGqCYqJ4B4neJIKYS7YiD6N1HthihnJErGobN36sDrf6U0Z3D78UWBu76kUhrJ4dm9JpIystuGc3k0dyQ0aOIrX7l52TNNdfcqq8fjW432aduuoo6TtgW33Xt_H_jOZaUGDwxPN-Yvn51IZgtOLJnwE8zTKFrFbJQJp-B5Gv2AzltlxR9RXnMTOSENbe5KBqmlR4WeMKHKGPGRpWiVyAioRrFHFlI4WUQejU1hO8FUgpoHGmAH0rPWhgvJKqaBNSp6rVIfEpy0nGEOvBJCHrs7DTZ3UUjhOryK4XWvfVZ0JKseSCbj_F6piYHjo1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/58f2375d54.mp4?token=soyGepN27iKZSMrFWIrro5kBQZGqCYqJ4B4neJIKYS7YiD6N1HthihnJErGobN36sDrf6U0Z3D78UWBu76kUhrJ4dm9JpIystuGc3k0dyQ0aOIrX7l52TNNdfcqq8fjW432aduuoo6TtgW33Xt_H_jOZaUGDwxPN-Yvn51IZgtOLJnwE8zTKFrFbJQJp-B5Gv2AzltlxR9RXnMTOSENbe5KBqmlR4WeMKHKGPGRpWiVyAioRrFHFlI4WUQejU1hO8FUgpoHGmAH0rPWhgvJKqaBNSp6rVIfEpy0nGEOvBJCHrs7DTZ3UUjhOryK4XWvfVZ0JKseSCbj_F6piYHjo1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبتای ایشون در مورد مظلومیت پسرا، بیشترین لایک ۲۴ ساعت اخیر رو داشته:
پسرا از یه جایی به بعد، از بس کار دارن و به فکر آینده‌ان، حتی یادشون نمیاد که کِی تولدشونه!
ولی همینکه یکی باشه و بهشون بگه تو چقدر برام مهم و با ارزشی، اندازه هزاران کادوی میلیاردی براشون ارزش داره!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72346" target="_blank">📅 10:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72345">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaefEfNVs-z-Az2KQFNoQstELDh9mIu280ApjGii_LFw0rSQi5yG8kKNiGfUrnq9i1rOLQQ5pEojkoj2ngCUeKTH9FpxdVvEvt8G8nS5YMJyrV_EHTlC0J2v67XLB9DRoevPgY7bGS_2DA92spbHPKRoIVG9FVbUBx-6oYNHqJ2hONcHXA5DFFUrzOXTwhzYCxwUmtbsuY2WmapyfVm8bP9kUdg9TXep9v2XBWvApXmHB7sBG9jmd_aUol9X5Yx-9iR6gYNbb2vgn519HbJ61NCurdving4M6tNaAY2_9MX6YKCJ_erRCKgbHdx_hcFMb00pXn41txn29ietKWeOZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارشد نیروهای مسلح جمهوری اسلامی :
قدرتمندترین ارتش جهان مقابل نیروهای مسلح ایران زانو زد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72345" target="_blank">📅 10:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72344">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c277f60d17.mp4?token=pJaQZXlj-kGqydgk62EkUBcf3FmlrIJYTGjn3pT6eVWB0mn87UjQbu884Zozw0tQ_ebwMZ3WUP-ChRtu7Nj_gtxd80uwrWDVRN_sPya0KlpxmFghkrNKBaR4xXwot1qUgG516nDi8IXaIrrS3xSJm01G4oYLzozSwbWhHGjh8BfHj_bmk8URUhuVFlnVcrSb45Y1WqOvWyAOIdoFFPECBs9E9s95QCvAxk2pu_qldsSALOcwS3g3YsDOkki2fLd5Kf4EMSWni1u83W84B3Sd-tDF0hd9Wew_6IQqsd-OzY2HDEInvp1H98LiCz46KBoCCPXP26x93NRW9VoI-qgrzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c277f60d17.mp4?token=pJaQZXlj-kGqydgk62EkUBcf3FmlrIJYTGjn3pT6eVWB0mn87UjQbu884Zozw0tQ_ebwMZ3WUP-ChRtu7Nj_gtxd80uwrWDVRN_sPya0KlpxmFghkrNKBaR4xXwot1qUgG516nDi8IXaIrrS3xSJm01G4oYLzozSwbWhHGjh8BfHj_bmk8URUhuVFlnVcrSb45Y1WqOvWyAOIdoFFPECBs9E9s95QCvAxk2pu_qldsSALOcwS3g3YsDOkki2fLd5Kf4EMSWni1u83W84B3Sd-tDF0hd9Wew_6IQqsd-OzY2HDEInvp1H98LiCz46KBoCCPXP26x93NRW9VoI-qgrzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آقای سفیر، پیام دولت آمریکا به مردم ایران چیه؟؟
سفیر آمریکا در سازمان ملل: این رژیم تروریستی باید بره راهی دیگه نیست
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72344" target="_blank">📅 09:30 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72343">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8SfoZvF6Zb2JL_2YTzX6W1KdVoFWjWmYj11VxV29rr525RAG8e8oNxa24hyNoZTc897fbaud8XH8ySE3dgjGpHDm4ktbHufRBlhWaKf40aASLXR_fMCdurVkdxxhcTZBrQogGJtznPFGgcUmgeFgHG4iPUav5wbaKvDaSEnDfg-ObjntdP-yBg6ZrrDzHle5lSNOCydXtMneNN-jslWgT-KFH-LNatkkU6571GwRejRhmHHj2vHUDMYn88nBMyGEqnPSk3P-3VpDW-nU6p-cq4B4qPZqkw_qYGGwJqcVTGPuC0KQfbxm0RtCQksYJ9-t3oKCAfBYstpXIw6UHK5PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وال‌استریت ژورنال، دولت ترامپ فشار اقتصادی خود را بر ایران افزایش داده و از کشورها در سراسر خاورمیانه و اروپا می‌خواهد تا روابط هوایی و بانکی خود را با تهران قطع کنند.
جاناتان برک، مسئول ارشد وزارت خزانه‌داری آمریکا، این ماه از چندین کشور بازدید کرد و به شرکای تجاری ایران هشدار داد که باید بین انجام تجارت با تهران یا واشنگتن یکی را انتخاب کنند.
در پی این کمپین دیپلماتیک، عمان، امارات متحده عربی و ترکیه، پروازهای ایران را محدود کردند، در حالی که مقامات امارات، تراکنش‌های مرتبط با ایران را توسط بانک ملی مسدود کردند و ترکیه، مجوز فعالیت بانک ملت را لغو کرد.
آذربایجان و گرجستان نیز پروازهای شرکت‌های هواپیمایی ایران را محدود کرده‌اند، در حالی که بریتانیا قصد دارد معافیت‌های بانکی را که به موسسات مالی ایران اجازه فعالیت در لندن را داده بود، لغو کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72343" target="_blank">📅 09:01 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
