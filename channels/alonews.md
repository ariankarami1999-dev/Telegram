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
<img src="https://cdn4.telesco.pe/file/TYpCHI7OhRB_ihME0vi5QUjmqQTELvdNXq8KuSYTn2eB33Ga3rS6BbRBvQ4zwA8qid5Z4KIdxIaMhRnMvbQ_8RQuY66G-Ks51zhOD1Dca2lqSTcBwJVWzt9ZYTwVHo9JlOetGTJTMYulzgifRZJ4ky47tnqIfuUM0huLnf3Sio9PXPVnZgh5zafwU7zPZE4K6ZDPx4jWgkFomkQs3mDaZ-vpW6OJ_1AZXxdEoq8RYM9YyVQBx1J_gRNeoUU_UryhvLvCEGkiqMu9GgBrCgnHHHqqb80wsW0X8bFeNyyFQM7bRB5RMDbtjh-0tbeegxdt-yHA3_nwNo0HVu68E0KWSQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 20:10:43</div>
<hr>

<div class="tg-post" id="msg-151675">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcZneHbN4FgfhnBMbv22qMmYXvkgLfAziA2zgGKSTLlMfJXuR0sm2YBl2dvjMn0pN_pM39nrWVTG4C3uNxpVQZBCO4BL1DZbwfoFqf7TEiOVbUuCemYYAk7nt3GL7HkMIo-WnhHleW0SSR16HxmWGN9rhi-DNMotjTuJ1d36ngpvy5snnUdLBrIy473VzdGpUsBFhH0se7mXJMylXSo24j58Vd1VnTJ_YRf8OkBUOM295ylHI8DlxY-6Utfdswq791wwIU1H9ol6TwlhKMseRrozA33P5mMHSjpIQmkSLAqZSOyF-NjITsHYoSCqoh6GQ91SmiBg6b5t11nZVw8ZlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آزمایش موشک هایپرسونیک Blackbeard آمریکا از لانچر زمینی
🔴
این موشک ۵ الی ۱۰ ماخ سرعت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/alonews/151675" target="_blank">📅 20:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151674">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4FmqBK1aiWF-Pt4dudKfn8mTbueI2elQ7v6Mptp55BhEKLSI3DgoUMzXoCWR3DFyFAKzv5aJEnx82PyM0DI1VLeF-02X_k2Z-dLEUGzJT1zHYt7cZzPLquZgLYbB9dz5yR4VU1kMlm3GKwyfymk3bb7r7H6k1_8ae_iWBZoGmZw4ySUz-PME04UQjTQxFuxLBQoS6oqGzDdhAPMaqo2qYAzxaGGITUdgN-ZfE_1d98A--BH82wO8TveigAK8qyK6zCGUZu8upY8CbIgxL8pOCI6jcB-3u97pjV5z__gGbWHE7_wxFbRZHr9Qa7pPxZMoPiVeDXFFkfbSXGrKlHrDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش خلبان جنگنده میگ ۲۹ اوکراینی پس از انهدام پهپاد روسی
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/151674" target="_blank">📅 19:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151673">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsRtibgBnZXF6jVnOKwdMOKE7QvqVBAajdcYxyRIVAQ_wUD7zvGYTi_n4_1wHEhEOTJv79N2Pjww9zJA-Gf2Q0KMCSu6PXzUOSGQrjOk8rDiRjylurLbeNoGBmMPsXwypmp-q1IEPO-u5PDrggak8UcwBXVTNs46aWeuUbLdsmQ_UR-fVVkOmAVH0LaenwkX5YkUR18zryYg0emojClSnFcAnyBnh4ifVNIbNw1Je5XzNcZe6kkDZ_jIBCgZdpq-t4J2LFj8hzXssWMHki2l_z_R0DKhKt3NGimL_SMoahvtcomZMGT3E6oC9Am7auZjU3Qnl7QUPhSdszYKPy6-Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : کاخ سفید هر کسی را که از عبارت "هوش مصنوعی" استفاده می‌کند، در حالی که عبارت جدید و دقیق‌تر "هوش فوق‌العاده" به طور گسترده پذیرفته شده است، به عنوان "دشمن" تلقی می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/151673" target="_blank">📅 19:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151672">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D32ZT3oviEdtycZaZ2IhXXBdgJpddZ46sUYuRrkSdTNEwPIkLzZI55-H_7XkMQNOpr-UgB52rNtEumL1dFcoopodrIjEKUFxjikYhG8uEOXYzfjsDdjuZV1goSckYZTfBTLl9w6LMFRbev5wYvUcRuMUeCESzOitJmmK-CBXGuMENAeuJOFI9Kfb74AjQogYzrTe0UL3rnin5RmenV3qBp3a1ECe1_2-gG9-8ZtERryUyudoNVqnIi1hea7WtOWCtpIjoS_2ZWycRtjiW0W_4ZGlJpqQMXfRuXfQpT_7cC97DAf_5Bu5smEx7QkjJ5DSehOg6eSvfOF79DOwaPk1Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : ما در حال انجام مذاکرات سازنده‌ای با جمهوری اسلامی ایران هستیم.
🔴
می‌خواهم به همه این موضوع را به وضوح بگویم که، در حالی که ایران از نظر اقتصادی و نظامی در وضعیت بسیار نامناسبی قرار دارد، و در حالی که تحریم‌ها به طور کامل و با تمام قدرت اعمال می‌شوند، و در حالی که حجم نفت با رکوردهای بی‌سابقه‌ای از طریق تنگه هرمز جریان دارد (دیشب به تنهایی، ۲۲ میلیون بشکه، و هیچ یک از این بشکه‌ها از ایران نبوده و به ایران نیز نرفته است)، ما در هیچ زمانی قبل از انتخابات میان‌دوره‌ای که در سوم نوامبر در ایالات متحده برگزار می‌شود، به ایران حمله نخواهیم کرد.
🔴
ایران هرگز سلاح هسته‌ای نخواهد داشت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/151672" target="_blank">📅 19:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151671">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
کانال ۱۴عبری: مقامات ارشد سپاه خواستار حملات به اهداف مهم در منطقه طی سه هفته آینده شده‌اند. این درخواست با این باور مطرح شده است که دونالد ترامپ قبل از انتخابات میان‌دوره‌ای، به ایران حمله خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/151671" target="_blank">📅 19:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151669">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nr5pciDeG9-lb1_-uZUgmaAaw4bzumECFcH1mdwW3AzGgEWNrjLspAzJKIseMdteN9iZa43MZ_uXx8UtPGDo8ENkQuWNEnAtPjg0FaoO66BHOfrH1-es4AEaFZ5Nb2jmvJvVfunU_y7eTflz2OJTTR2jbdlSiL8jWteWaYnDH8clRt5OUvf_d4yKYZ8o1YLIede36rVrj5NNyvkJ9uXsgPxaGt87FNYlgnss8lc6YQHkjCemX5Q6qDFI0lqmsGJ_1BJV__e-sZpFADQKX6gOqncF_i7uzBd4ckZr4fZWhHcfkJFZ6tN_cTPsC8a5sot3KzeDuoGr9TJubKPaqMdf2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b42cc54c6.mp4?token=tam3t_YNmT8qWmyRMLBZ4xJEXe7I1iiaO_CZBHfLsN65pkZwgD3rZBK8WHKxIgibDNgDhpJCpBXDfTUX6zZ71qyJHRGkeCl18hysZJBYei4HQoGcRNH466jhIufJp42VniA5gf0bDLv-tQnTcba8s4f-BmQFrhcN1L5rtq_nzBLC58JMHuMF--Oqyh_GscM1tQdfh70PPfplS7zxBojQZjdbGv6froTd2y27RIv6Zl53V0lUNa7ydLN1c7bWrMLBZ5GJwKaQjowb4GtJKOhD0IVxzcHNgB0eZER26NzVOsSIMw4cmr_4Kb2-8_KBxKzNZ3yz8pb6w5I4dikwghWFjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b42cc54c6.mp4?token=tam3t_YNmT8qWmyRMLBZ4xJEXe7I1iiaO_CZBHfLsN65pkZwgD3rZBK8WHKxIgibDNgDhpJCpBXDfTUX6zZ71qyJHRGkeCl18hysZJBYei4HQoGcRNH466jhIufJp42VniA5gf0bDLv-tQnTcba8s4f-BmQFrhcN1L5rtq_nzBLC58JMHuMF--Oqyh_GscM1tQdfh70PPfplS7zxBojQZjdbGv6froTd2y27RIv6Zl53V0lUNa7ydLN1c7bWrMLBZ5GJwKaQjowb4GtJKOhD0IVxzcHNgB0eZER26NzVOsSIMw4cmr_4Kb2-8_KBxKzNZ3yz8pb6w5I4dikwghWFjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر نشان می‌دهند که یک هواپیمای ثابت متعلق به خطوط هوایی سعودی در فرودگاه بین‌المللی ملک خالد شهر ریاض، در یک حمله موشکی اخیر توسط حوثی‌ها (انصارالله) مورد اصابت قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/151669" target="_blank">📅 19:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151668">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIEQd0FrfAog4QPya2910RvY_ia9O081AAUJih9bji_n9a4jOuTHmDB8_yqjN4sfv27goRIGlephqfgXKSh1z-phky9OJG_rQtNC_etCoE5QDbeYib2eVfABUoyvr6aG6Toyi76hCnc5njoGOxsgRKO4OlAcgii457QCm9N1m2xgkmrOrrpv6qqKJh4Eb5HmjaT7MOIbjelq0K7zq_301upnjJmd-pc3E1pPesyy-xCYACxvxQS1f7Ym40Cs-eI4EWzc8IkeqLJJr6LH0o3nn3XTjeThH3h0D_fzMNwmb0mQIXwSvWqrSBJqAHgqTbnFEsuGlCItVmyNz3oga6IPhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سهم قطر از صادرات LNG جهان به ۷ درصد کاهش پیدا کرده سهم آمریکا هم شده ۳۱ درصد
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/151668" target="_blank">📅 19:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151667">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzCsLpXBm48PSZXJeWssvFVxtjkcjHv-POKMdu88UBfgE24tkDKH0Ezr-ffRgzXNGr_dL2Id9PC0E-tKfQDXN33mHPmpIJgc97uiXAg36zyMGUfOkITkT8aOokuUZLHxsgLGbgMKk83xTBpErys_OG8PdLHk9HzUaLe1pvxO8jJq22SO22M1URTvdZdvyKZIbemyWwBd-wS_qCpKXqIcY6nI3nwRUlmBkglORHpLeCVw-YN-FdELYWXBHzftiahzj-DpQey-6vqWJYGx8q8GtRHqTmaxf1ZKv_8ViHxrJI7ztodK_kaM2t6SGJCiAlJWG_w7s9nYgJatJgHdDNBozg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیما از نیرو هوایی پاکستان وارد تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/151667" target="_blank">📅 19:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151666">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ebbea01a.mp4?token=boqNhjJu7YD4eCQQLLXJOMAYIA538ecw6P6kKQkius8RH1-kaOPDkfBpTw4gKP664h-k4P_PctXC6LpMRaMjfK3zXQ-cPJhGQGh1y-2z64zGGtLe47kndBnz_mm9B_4QUoN0XT0L6gWdIAlqFQcJ8_rj4VHGR7IV9_c6wxlD5drI5ayOKkg72oX7I33tz2aHCNpkLbGd4KIZ6fZ3iNSp8DChOx0sw_r4lsaN1qC4rJkdnRf_Z7nswVb0rXJGiow7eVEXXm9xzpg2vtK_ZJbpWQ1O8ea6aeMBeEuxdlexLeru8f1RIP4F6EWy-UYqsM9QsBSlQBywnSFSfNyHzKBUKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ebbea01a.mp4?token=boqNhjJu7YD4eCQQLLXJOMAYIA538ecw6P6kKQkius8RH1-kaOPDkfBpTw4gKP664h-k4P_PctXC6LpMRaMjfK3zXQ-cPJhGQGh1y-2z64zGGtLe47kndBnz_mm9B_4QUoN0XT0L6gWdIAlqFQcJ8_rj4VHGR7IV9_c6wxlD5drI5ayOKkg72oX7I33tz2aHCNpkLbGd4KIZ6fZ3iNSp8DChOx0sw_r4lsaN1qC4rJkdnRf_Z7nswVb0rXJGiow7eVEXXm9xzpg2vtK_ZJbpWQ1O8ea6aeMBeEuxdlexLeru8f1RIP4F6EWy-UYqsM9QsBSlQBywnSFSfNyHzKBUKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه برخورد صاعقه به دکل برق فشار قوی در رشت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/151666" target="_blank">📅 19:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151665">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
اگه دنبال درآمد دلاری هستی بیا
👇
https://t.me/+qUvlXmJGb35hZDNk
https://t.me/+qUvlXmJGb35hZDNk</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/151665" target="_blank">📅 19:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151664">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7666e6713c.mp4?token=XA9GZTFYXqlUONsbuq5Oxr0BjgYBJrJ-ep8qV1RhMeONetbOjd9s3wrXH2y3Jm8wzjOF_10oHWpu_BPF9iQtAK7orwCSPrpa2JBrm5j0OI-ayP2k2kjnVUqhdup880O4ATXI4jcRt3h-I0-X3nsDSCw1xWy_JwWEm0dFYk8fs5oW2qNnmW2bDd3eAhHpJ4mPeK792HOj9KC5AZO88ICbHwGwbqAugm_GPhrgd2Bpix_so4P63s-jILt7pmuEIx3opaFjGfi49wvOTV9VKqlNx5LgSNsLkAr7Bey0-FZUxTX16fKgSEhEObrm1gJaYbf8XF9uGpFT0ze4vf3ZUbll9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7666e6713c.mp4?token=XA9GZTFYXqlUONsbuq5Oxr0BjgYBJrJ-ep8qV1RhMeONetbOjd9s3wrXH2y3Jm8wzjOF_10oHWpu_BPF9iQtAK7orwCSPrpa2JBrm5j0OI-ayP2k2kjnVUqhdup880O4ATXI4jcRt3h-I0-X3nsDSCw1xWy_JwWEm0dFYk8fs5oW2qNnmW2bDd3eAhHpJ4mPeK792HOj9KC5AZO88ICbHwGwbqAugm_GPhrgd2Bpix_so4P63s-jILt7pmuEIx3opaFjGfi49wvOTV9VKqlNx5LgSNsLkAr7Bey0-FZUxTX16fKgSEhEObrm1gJaYbf8XF9uGpFT0ze4vf3ZUbll9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تظاهرات ضد سربازی اجباری تو اسرائیل که مشخصاً اکثرا یهودیای متعصب مذهبی و طلاب هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/151664" target="_blank">📅 19:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151663">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
وال استریت ژورنال گزارش می‌دهد: بین ۲۸ سپتامبر تا ۴ اکتبر(۶ تا ۱۲ مهر)، ۱۰ نفتکش در تنگه هرمز مورد حمله قرار گرفتند که بیشترین تعداد حملات در یک هفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/151663" target="_blank">📅 19:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151662">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b43f0ec404.mp4?token=DHwUGFko6uZI1GFeaAA40uAwdYh2KHKdweqbD6cK9Ml3iykfxxyne2lOCW2QraqcqrXS2Cl3llIdm07un0x8cchykL8Rt5D4h0PCW2uFuFdYdrFnAmlFhJvK7hlhIl1SJdxVS7iWlY880fy37-URmkHXZlnEjDiZuMLu7E83P64HV97wolx70Ldig18dkte0SzGB7i-RMx0Tnuz3LeMyK-fOgRF-3C7iCSwTNKmWJXmDvihojTL9EiSqKkWFUiZkcPjKfmSzCqg1-JvQU528pf6RKfH35btSBJXznSR9KnDeUqHCDA8O4wn08hPFogbJh8dfOcEzIGopd9TZE2AbaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b43f0ec404.mp4?token=DHwUGFko6uZI1GFeaAA40uAwdYh2KHKdweqbD6cK9Ml3iykfxxyne2lOCW2QraqcqrXS2Cl3llIdm07un0x8cchykL8Rt5D4h0PCW2uFuFdYdrFnAmlFhJvK7hlhIl1SJdxVS7iWlY880fy37-URmkHXZlnEjDiZuMLu7E83P64HV97wolx70Ldig18dkte0SzGB7i-RMx0Tnuz3LeMyK-fOgRF-3C7iCSwTNKmWJXmDvihojTL9EiSqKkWFUiZkcPjKfmSzCqg1-JvQU528pf6RKfH35btSBJXznSR9KnDeUqHCDA8O4wn08hPFogbJh8dfOcEzIGopd9TZE2AbaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس، معاون رئیس‌جمهور:
به نظر من ۹۹ درصد از شهروندان آمریکایی وقتی به فردی مانند ایلان ماسک یا لیسا سو، مدیرعامل AMD نگاه می‌کنند، می‌گویند: بدیهی است، اگر آن شخص بخواهد وارد شود و چیزهای بزرگی در آمریکا بسازد، ما از او حمایت می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/151662" target="_blank">📅 19:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151661">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
شرکت‌های هواپیمایی ایر ایندیا، ایندیگو و ای‌آی اکسپرس، پروازهای خود به ریاض، عربستان سعودی، را تا تاریخ ۱۰ اکتبر لغو کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/151661" target="_blank">📅 18:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151660">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سخنگوی شرکت هوایی لوفت‌هانزا:
پروازهای لوفت‌هانرا به ریاض را  تا پایان روز ۱۶ اکتبر به حالت تعلیق درخواهیم آورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/151660" target="_blank">📅 18:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151659">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060004b037.mp4?token=A9KJNUXwfGX9N_XK3x5JpOxxAijLbcegw0sGS6e-WzuDqIKqhtOREIM-bBRXBD7u6fUAzlWczgRSEijEunhrKj08diiBhiyKZMoNUs4sFG60zctLWbJc5jUy0TqNHfSBugOnJK0GuqQ-df5Qjr9Cx3LTI03VytHv5hkOSNWIh8xHlLYfZSC7_dVFsIMdD-XqgwA4gWw-s2gMTagVrpnVEDSZfgz5Pj6fStJfoB0nC9giEZRoLVJ_hj9TQBZe5eTQ0m5MeKQ0gjvp68xftB43m1exP5wz3cZ43zRqAOPqDTdG-Wv7k9hPStkeZI5NGmXNdu1oEp1b2Xvt3RopEHd8dzR2afGbd1Xc5vBbWVTRmoIpTh4q3UmmPZJEpKYkOr4xfWWNZlxWJGUKSgQI3OnqWtPZgYmoJZZ6Z-KrI-_SQzaBmIOQuchka6Vmd3BzNXL9fwhBWdGN54ufShxUqs6_hq1pIglEY9Qh_65VQ2VNMCf9LRiMzZ8B8MyxKZ9lUnu-z8zFcsZz0cPi5nLjx2chp6_gfxYdoLTlZVuH0zcIOG8j-BLMe5N2-zYdZDSx-cLdPUNe_hTkhj9sHymPXTfBxSx4hQiJKwcUbMJ8eE2tMf6aIYrBmB6iYCs7j-r-3SG8AyfExIcHTMKtOXyVWgEm5c8eu8O2K7cC7q-X6qkoiUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060004b037.mp4?token=A9KJNUXwfGX9N_XK3x5JpOxxAijLbcegw0sGS6e-WzuDqIKqhtOREIM-bBRXBD7u6fUAzlWczgRSEijEunhrKj08diiBhiyKZMoNUs4sFG60zctLWbJc5jUy0TqNHfSBugOnJK0GuqQ-df5Qjr9Cx3LTI03VytHv5hkOSNWIh8xHlLYfZSC7_dVFsIMdD-XqgwA4gWw-s2gMTagVrpnVEDSZfgz5Pj6fStJfoB0nC9giEZRoLVJ_hj9TQBZe5eTQ0m5MeKQ0gjvp68xftB43m1exP5wz3cZ43zRqAOPqDTdG-Wv7k9hPStkeZI5NGmXNdu1oEp1b2Xvt3RopEHd8dzR2afGbd1Xc5vBbWVTRmoIpTh4q3UmmPZJEpKYkOr4xfWWNZlxWJGUKSgQI3OnqWtPZgYmoJZZ6Z-KrI-_SQzaBmIOQuchka6Vmd3BzNXL9fwhBWdGN54ufShxUqs6_hq1pIglEY9Qh_65VQ2VNMCf9LRiMzZ8B8MyxKZ9lUnu-z8zFcsZz0cPi5nLjx2chp6_gfxYdoLTlZVuH0zcIOG8j-BLMe5N2-zYdZDSx-cLdPUNe_hTkhj9sHymPXTfBxSx4hQiJKwcUbMJ8eE2tMf6aIYrBmB6iYCs7j-r-3SG8AyfExIcHTMKtOXyVWgEm5c8eu8O2K7cC7q-X6qkoiUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه بریتانیا، اد میلیبند:
امروز، ما تحریم‌های بیشتری را علیه ماشین جنگی پوتین، ناوگان مخفی، شرکت‌های نفتی، ارزهای دیجیتال و همچنین تأمین مالی جنگ اعلام می‌کنیم.
🔴
ما خواهر و برادران شما در این درگیری هستیم و تا زمانی که لازم باشد، در کنار شما خواهیم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/151659" target="_blank">📅 18:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151658">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f0003b79a.mp4?token=AsoMlAU3Dyj35fWzs3j6VcYZ-zCsxAfd3__TMcbeRgdLOp7OlS6ouV2APCNUwd5wYjEUQJjlszTCRVV95-HIimTIdmBsDFtxqzjVqQz7nAYSQbiaPjO7GJ7K9_LMTNN19xzFBuULT_5imMtcaTviCHTAfsic78tLZOhnBKr--vhrkwreaOY1zyDkFDFMS0xB6xBQRf7tTguy4VM2H4Iidiy5M3dLdHZMoLE7yUvSMsONwA5Mui8CD9rEgK5BiF740MPg0mvFxsIkqCNoi_rdiM14ww2DUGbNhH856brf5T-ZA-00DMq6EsvuUo_UrrOoM2vvTpD_X9WPR57JYFcCGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f0003b79a.mp4?token=AsoMlAU3Dyj35fWzs3j6VcYZ-zCsxAfd3__TMcbeRgdLOp7OlS6ouV2APCNUwd5wYjEUQJjlszTCRVV95-HIimTIdmBsDFtxqzjVqQz7nAYSQbiaPjO7GJ7K9_LMTNN19xzFBuULT_5imMtcaTviCHTAfsic78tLZOhnBKr--vhrkwreaOY1zyDkFDFMS0xB6xBQRf7tTguy4VM2H4Iidiy5M3dLdHZMoLE7yUvSMsONwA5Mui8CD9rEgK5BiF740MPg0mvFxsIkqCNoi_rdiM14ww2DUGbNhH856brf5T-ZA-00DMq6EsvuUo_UrrOoM2vvTpD_X9WPR57JYFcCGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
با اعلام رسمی سخنگوی قوه قضائیه، بی‌حجابی رسما جرم اعلام شد!
🔴
از این به بعد در سراسر کشور، با خانمای بی‌حجاب برخورد و براشون جرم ثبت میشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/alonews/151658" target="_blank">📅 18:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151657">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqbVrBtcexHPNpFEsGjJf-Q687-1sEJg-q_bFNqnm_1cbRpaef_4hhd698h8r_XOBPkCGrgcxhJm4dE39hbrLHb5jit9XRRqw5rM9C872YBCwAtcjeRX5XYoFn70KCAcNM4ARQd7ORQTKbpq6F3HuR2Ar8hOFqE2rkSmqUEy7TuCk1aiFRgX1pgeICx9K0t7PtXAjQzguI9JUWQh6nItkyMm5iU3xQzKN-ZFSwtYkY1wGfxJm7vq1rveDEWy0iy9oHX4mVLcu4dxFwc1RzxsE9BbUr4noxXjlZebsOk_Si76ZHkOYBSLyNJH8IgvDdk8snRYgNy8QnA9YVi1Puja7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیکلاس مادورو، رئیس‌جمهور سابق ونزوئلا، در یک کیفرخواست جدید که روز پنجشنبه منتشر شد، به اتهام شکنجه و سایر جرایم مربوط به نقض حقوق بشر، مورد پیگرد قانونی قرار گرفته است. این اتهامات به اتهامات قاچاق مواد مخدر قبلی که او با آن روبرو است، اضافه می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/151657" target="_blank">📅 18:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151656">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2HMfbqgyiRV06817BDL_IhE0-vLPgjzi_az74H47CoxMNBL_JVEy5RPcGgUodNhUNA5fV_q4b4MSnKAQpuEpWMZ4lMssBunMJDoM5aDoXk2z8Uii7l_QYvlhL6Lh_OpEe_ao2TUBni97WCYWGkDpu2UwL-KWxiYOuQSTiQEh6nU6GBk-4w487XsKRXTmkEk-Iiw7xZhwBFPqsrmUGhy65J0xNU6BWxItzUMSgqtQ29GYUf9cO1xvCpy8nlfwyvdrTV9klRtabUaf1MtISc7FdxQ4_7NkEPM_RpQO4NMFhv3t8VeQlTA9CqpVquMJkqcR_6-Xn6ZHgr7cBe_ADvb2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
امروز، فرماندهی مرکزی ایالات متحده در یک جلسه مجازی، شرکای بین‌المللی حمل‌ونقل دریایی را در مورد تنگه هرمز آگاه کرد.
🔴
رهبران، بر اهمیت افزایش تلاش‌ها برای تضمین آزادی تردد دریایی با افزایش حجم ترافیک تجاری، تاکید کردند.
🔴
آدمیرال برد کوپر، فرمانده فرماندهی مرکزی، از رهبران صنعت و سایر سازمان‌های دولتی ایالات متحده به خاطر حمایت مستمرشان تشکر کرد و به فداکاری‌هایی که خدمه غیرنظامی به دلیل حملات غیرضروری ایران متحمل شده‌اند، اشاره کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/151656" target="_blank">📅 18:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151655">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/182d6999c7.mp4?token=VYvNUV6-kuaXCO98e8D60aEdLMd49czPm922glTHuwtlvgpfE4l_n3HWub17G57pPkQ96vSmr7lMND7d3yDb5rEcMnYXMLN07I-nkAjHx65EwjZm3bOq7kdkLPSTR8S-PdyMx0vB7K_a-KIDfLYo__9iDYYmd2IdSS7sdzS9CUAIQCp5qkpDKYDLYfo0yutrz8N0nq3ulqiVpT9AzOp1TcVCeSdsiwdWba4BQ3vX1tDrJCEEVEEuGJYvkW1ccB4EA5V7HFMrxRlzyHOUHT53nUl8jIhqgDJbK36WLQamvgsvJjhxanE7yky59juWoJXUkQGL3BdX_xZsW4baEV86gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/182d6999c7.mp4?token=VYvNUV6-kuaXCO98e8D60aEdLMd49czPm922glTHuwtlvgpfE4l_n3HWub17G57pPkQ96vSmr7lMND7d3yDb5rEcMnYXMLN07I-nkAjHx65EwjZm3bOq7kdkLPSTR8S-PdyMx0vB7K_a-KIDfLYo__9iDYYmd2IdSS7sdzS9CUAIQCp5qkpDKYDLYfo0yutrz8N0nq3ulqiVpT9AzOp1TcVCeSdsiwdWba4BQ3vX1tDrJCEEVEEuGJYvkW1ccB4EA5V7HFMrxRlzyHOUHT53nUl8jIhqgDJbK36WLQamvgsvJjhxanE7yky59juWoJXUkQGL3BdX_xZsW4baEV86gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه بریتانیا، اد میلند:
امروز، ما تحریم‌های بیشتری علیه ماشین جنگی پوتین، ناوگان سایه، شرکت‌های نفتی، رمزارزها و تأمین مالی جنگ اعلام می‌کنیم.
🔴
ما برادران و خواهران شما در این درگیری هستیم. و تا زمانی که لازم باشد، همراه شما خواهیم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/151655" target="_blank">📅 18:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151654">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/474de313f9.mp4?token=kRvaEU_IKNZ4gKwnDAYS98vnn58W7hWSZR523e2glGFV6QBJ9Lcrenf79SGjLh65UQA_8tgpSYy7Pbt-sfvWeyRbMev6ZFckGvuLfg_5L9D7Pt0EsPIV4bE0wQnL_LvAVFhBGJamBfTO1B_huZufny07Iw_Y7Ub8McoVv7O3i1e2OgmqYeoW2DzdPdFKgimolZOJwlpIMNEq4mrEso7j1UjCUoYAXXtfjJCyozDduLgEf-Ux-nYbJTXQaDVt8x-syWFnSGtxAY3sQc1_qHAJY4apqhzoQiZ_x5nw_9oO92m3LXOw4Ko-sp3OQ2zVhUEdjEdERMoEDyvUns8Xk2AlTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/474de313f9.mp4?token=kRvaEU_IKNZ4gKwnDAYS98vnn58W7hWSZR523e2glGFV6QBJ9Lcrenf79SGjLh65UQA_8tgpSYy7Pbt-sfvWeyRbMev6ZFckGvuLfg_5L9D7Pt0EsPIV4bE0wQnL_LvAVFhBGJamBfTO1B_huZufny07Iw_Y7Ub8McoVv7O3i1e2OgmqYeoW2DzdPdFKgimolZOJwlpIMNEq4mrEso7j1UjCUoYAXXtfjJCyozDduLgEf-Ux-nYbJTXQaDVt8x-syWFnSGtxAY3sQc1_qHAJY4apqhzoQiZ_x5nw_9oO92m3LXOw4Ko-sp3OQ2zVhUEdjEdERMoEDyvUns8Xk2AlTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طوفان و باران هم‌اکنون در تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/151654" target="_blank">📅 18:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151653">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
برخی از منابع عربی مدعی وقوع چندین انفجار شدید در تنگه هرمز شدند
🔴
برخی منابع رسانه ای از هدف قرار گرفتن یک کشتی در تنگه هرمز خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/151653" target="_blank">📅 18:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151652">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
شرکت Kpler گزارش می‌دهد که برخی تولیدکنندگان نفت در منطقه خلیج فارس
ممکن است به‌طور مخفیانه به ایران عوارضی معادل ۱۰ تا ۲۰ درصد از محموله‌های نفتی خود پرداخت کنند تا در ازای آن، عبور امن محموله‌هایشان از تنگه هرمز تضمین شود.
🔴
این ادعاها هنوز تأیید نشده‌اند، اما Kpler می‌گوید چنین توافق‌هایی می‌تواند به توضیح این موضوع کمک کند که چرا قیمت نفت خام برنت همچنان در نزدیکی ۱۰۰ دلار در هر بشکه باقی مانده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/151652" target="_blank">📅 18:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151651">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc65671ac5.mp4?token=vcctH53XkBEmsdUUpTsagURk2fA8sNV1rvh8JUQ9OCLmTOtupWVXvwhEVt9058I6XG7VAi8Kl0x8HjoaQNlNQicmO9JJVFTW0ExtUhpSrUUUtZujZeBS_T4r_tNwfJYwPFDHCOb_XebRH9gtfYrBf_BJVJ17IwAtYCHdfKU3lTWnxPh14QhARGbNz3aIen_SFA63Gip1dLFk0Z4XFzhxYGw0_PWhHQyYDUB2HjJkVab8h3iKRcz1zO3SJ_rSwv-YQy5Vo-pmOCLuKdIrJEiZyXn-5lYzbj4ivsDm3-EyzEgvCMfG7AupdvTkWf14ln4Y1DWmghei9a601coM0dHBWYxIeHO7V3tH5PGuHneybRfjyWxHPKvqZ_RQGAduU-T0pRLX1k6lDZiabSabSYX9WLwAKHK0pdzW1CcFPY6XG9vB1P-7LDZmXWIWkeo20POEKoDo-ZonvTUXOzLxpHGj6sYJfH_EMhfKKpRbNd1mkxPbCoSzeBbhSpww2u6f1Zxup-DOndsMgKqKt3Ioz-u0lJNVJ_un71VTtS2_Qb26WekXimJcpeUC40w2RwCXLmbeCY8SzBbNn8ronkV1Q9nWf8sJdV72MIAnJRfexIQsj9GmzbWuQ4_z1iQSce3aNVLKCp4f3ECUj9TXHbOKhWigBibIKAFVZtUJAUo71xpxzGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc65671ac5.mp4?token=vcctH53XkBEmsdUUpTsagURk2fA8sNV1rvh8JUQ9OCLmTOtupWVXvwhEVt9058I6XG7VAi8Kl0x8HjoaQNlNQicmO9JJVFTW0ExtUhpSrUUUtZujZeBS_T4r_tNwfJYwPFDHCOb_XebRH9gtfYrBf_BJVJ17IwAtYCHdfKU3lTWnxPh14QhARGbNz3aIen_SFA63Gip1dLFk0Z4XFzhxYGw0_PWhHQyYDUB2HjJkVab8h3iKRcz1zO3SJ_rSwv-YQy5Vo-pmOCLuKdIrJEiZyXn-5lYzbj4ivsDm3-EyzEgvCMfG7AupdvTkWf14ln4Y1DWmghei9a601coM0dHBWYxIeHO7V3tH5PGuHneybRfjyWxHPKvqZ_RQGAduU-T0pRLX1k6lDZiabSabSYX9WLwAKHK0pdzW1CcFPY6XG9vB1P-7LDZmXWIWkeo20POEKoDo-ZonvTUXOzLxpHGj6sYJfH_EMhfKKpRbNd1mkxPbCoSzeBbhSpww2u6f1Zxup-DOndsMgKqKt3Ioz-u0lJNVJ_un71VTtS2_Qb26WekXimJcpeUC40w2RwCXLmbeCY8SzBbNn8ronkV1Q9nWf8sJdV72MIAnJRfexIQsj9GmzbWuQ4_z1iQSce3aNVLKCp4f3ECUj9TXHbOKhWigBibIKAFVZtUJAUo71xpxzGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره مراکز داده:
مردم معمولاً با مراکز داده مشکلی ندارند. خب، مشکل مراکز داده این است که آن‌ها بسیار عالی هستند و کشور ما را به شدت پیشرفت داده‌اند، اما باید به نفع جوامع محلی باشند.
🔴
من چند روز پیش به شرکت‌ها گفتم که آن‌ها پول زیادی دارند. کمک‌هایی به جوامع محلی ارائه دهید و این جوامع عاشق آن‌ها خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/151651" target="_blank">📅 18:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151650">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
خبرنگار: پیروزی جمهوری‌خواهان در ماه نوامبر برای برنامه‌های شما چه معنایی دارد؟
🔴
ترامپ: خب، فکر می‌کنم این به معنای میراث است. فکر می‌کنم بسیار مهم است. داشتن یک پیروزی واقعاً تأییدی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/151650" target="_blank">📅 18:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151649">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ترامپ درباره ایران:
اگر می‌خواهید مشکلات را ببینید، اجازه دهید آن‌ها به لس‌آنجلس حمله کنند یا به مکانی مانند سن دیگو. اجازه دهید به یکی از شهرهای بزرگ ما حمله کنند.
🔴
این همان چیزی است که به آن "مشکل" می‌گویند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/151649" target="_blank">📅 18:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151648">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71498f9e6.mp4?token=XDGzZRWkD8X0HOwa_kEGync9EaFNTeJVO7-R0GWGUMQU7fUac5nsp3IU0zWdDcrxSFzO94Cl2_Nsm0ubEoxavyzHjYaKJSBfMyEs7c0IY44-D1sf5HrOtYayA71G95wEwbJ2T-IPAJhp-nheom_l2eq94Cga9wppaayQzAZ05iTPJ5pRKeHTj1n1R78Ics4dNjUNibwrOcgus5qxDIyzvAPpzX16SnYnPBJIbRbw3cijq6Yf34s0UpBQrdQBAV7SFVpgRf9aohC6X_WJHG4eEpl5ZGmvRMXO6WCJhBG-OVeF1PPpn_XtXvFcIRziBu30F7jTvGHZVaq3UxKJpe7Zug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71498f9e6.mp4?token=XDGzZRWkD8X0HOwa_kEGync9EaFNTeJVO7-R0GWGUMQU7fUac5nsp3IU0zWdDcrxSFzO94Cl2_Nsm0ubEoxavyzHjYaKJSBfMyEs7c0IY44-D1sf5HrOtYayA71G95wEwbJ2T-IPAJhp-nheom_l2eq94Cga9wppaayQzAZ05iTPJ5pRKeHTj1n1R78Ics4dNjUNibwrOcgus5qxDIyzvAPpzX16SnYnPBJIbRbw3cijq6Yf34s0UpBQrdQBAV7SFVpgRf9aohC6X_WJHG4eEpl5ZGmvRMXO6WCJhBG-OVeF1PPpn_XtXvFcIRziBu30F7jTvGHZVaq3UxKJpe7Zug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
ما به شدت در حال شکست دادن ایران هستیم. دیگر هیچ تهدیدی از سوی سلاح‌های هسته‌ای وجود ندارد.
🔴
آنها در حال حاضر در وضعیت بسیار نامناسبی قرار دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/151648" target="_blank">📅 18:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151647">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ترامپ: ما به شدت به ایران ضربه می‌زنیم؛ دیگر هیچ تهدیدی از سوی سلاح‌های هسته‌ای وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/151647" target="_blank">📅 18:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151646">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
به دلیل وقوع طوفان در برخی نقاط تهران برق قطع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/151646" target="_blank">📅 18:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151645">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd3faa3c1.mp4?token=HQvgA2wOfmsXCZ-PEnRILr2zsEpRpFbna_G3T_5blBzT9jlm39fkprV05nxl2gUbn3SgoiPf3V59pR_Bu94wgg1BC53csraUD1lMVGJfPrKOKOJZBtE50pQmCX7Ofx9PzurZeIq_JnaXZ9NQTzptFb4q6WB6jTIqH1Te7hVmkBLD5M2V1lGrSNrLyHBlbsUZ-z3KbqxaR2FZpqh0OtZ-9th687HBfeNmlesB96T4Msiuq8AbQS-TFMbl13pARQwv-c0Gkbna9Tr5Y2WlJy3RCQOKzu_tAqdtnu9SiDCVMkISuhK9eEYm_XnC1El0K0DrcbhnJGLifK6_hWh9S5nTQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd3faa3c1.mp4?token=HQvgA2wOfmsXCZ-PEnRILr2zsEpRpFbna_G3T_5blBzT9jlm39fkprV05nxl2gUbn3SgoiPf3V59pR_Bu94wgg1BC53csraUD1lMVGJfPrKOKOJZBtE50pQmCX7Ofx9PzurZeIq_JnaXZ9NQTzptFb4q6WB6jTIqH1Te7hVmkBLD5M2V1lGrSNrLyHBlbsUZ-z3KbqxaR2FZpqh0OtZ-9th687HBfeNmlesB96T4Msiuq8AbQS-TFMbl13pARQwv-c0Gkbna9Tr5Y2WlJy3RCQOKzu_tAqdtnu9SiDCVMkISuhK9eEYm_XnC1El0K0DrcbhnJGLifK6_hWh9S5nTQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توی تجمعات شبانه یه رپر آوردن و دورهم میخونن و میرقصن
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/alonews/151645" target="_blank">📅 17:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151644">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
پزشکیان عازم ترکمنستان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/151644" target="_blank">📅 17:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151643">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQsigQlomkOaeW19BttkuVN0QRdTGBYTA6FrRds1L8wIhnC8TjtFwuYQp6Ub3xSnDZrRAISAaMPJcuobANljn6Cu_N02o8zBpWS47lPU56m2OSrKR7fsY3xCLZWyAl3tineTUPD-r_q9KYlycok3b3fdvCJXSGQhbjgZNb7QcioaDMIbvavLXt-ZTfnRrWDu_Ibg1z1fQw5rkqPB4hmHu0YtLLorExxkFXMN7o7dNUHMIvt1bs7y3e8NiRwYprkv7mSeqPEKLseiRl1kkhiU-jDIq6MwpVMYxxMf2LJvgToLBZPZNpJUz8OqGI6BQA7oh_ti2fKWWljB6Ktig6kZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دود غلیظی از کارخانه پالایش نفت بقیق در عربستان سعودی به هوا برخاسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/151643" target="_blank">📅 17:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151642">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
انتقاد ایلان ماسک از تبعیض علیه استارلینک
🔴
ایلان ماسک: برخی الیگارش‌ها برای حفظ سلطه انحصاری خود بر مردم هند، مانع فعالیت ما شده‌اند
🔴
دولت هند: مطرح کردن این موضوع که چارچوب مقرراتی هند ناعادلانه یا تبعیض‌آمیز است، بی‌اساس و نادرست است. همچنین، مجوز فعالیت برای سه ارائه‌دهنده جهانی خدمات ارتباطات ماهواره‌ای صادر شده است. تمامی شرکت‌های دارای مجوز باید الزامات امنیتی تعیین‌شده را رعایت کنند. استارلینک نیز سال گذشته مجوز فعالیت در هند را دریافت کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/151642" target="_blank">📅 17:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151641">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
حوثی ها با موشک بالستیک به خمیس مشیط در عربستان سعودی حمله کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/151641" target="_blank">📅 17:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151640">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وزیر خارجه آمریکا: جنگ اوکراین که اکنون در بن‌بست قرار گرفته، یا با مذاکره پایان می‌یابد، یا درگیری‌ها در آن تشدید می‌شود که بسیار خطرناک است
🔴
برای این مناقشه، راه‌حل نظامی وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/151640" target="_blank">📅 17:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151639">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3c124bf523.mp4?token=uoQGLxO-qRIGykJDlxRIhaUs1-co3RJ4f8te2GYMSWwOmlYR7Lq0qsogG3wDPLDjfSmembZFvX2WsW-RjKNWPCcP96k2qEH_5Kr0Eiahm1d9dEIazSNdF3g0_THOKJzcA30pgQEpBT7eVzPTF8F_Pt63W5EBtU8WwT0KdqtWwgmkHi32YKgfN_gDPT7XQBttRXZlbEEg5UZyyn-hTfVdRSuxrobIb4FLKM099Wm1VBZAwNo2eqy7Ud2F78rYQ4nkcohn_Nt6qLNZmAso08Qly4RK-1HFwWJVe-hna6redhiTO04jGx3oIASz5Uk-nYTQ3S4L1YRF2pGsAxt3P2IApA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3c124bf523.mp4?token=uoQGLxO-qRIGykJDlxRIhaUs1-co3RJ4f8te2GYMSWwOmlYR7Lq0qsogG3wDPLDjfSmembZFvX2WsW-RjKNWPCcP96k2qEH_5Kr0Eiahm1d9dEIazSNdF3g0_THOKJzcA30pgQEpBT7eVzPTF8F_Pt63W5EBtU8WwT0KdqtWwgmkHi32YKgfN_gDPT7XQBttRXZlbEEg5UZyyn-hTfVdRSuxrobIb4FLKM099Wm1VBZAwNo2eqy7Ud2F78rYQ4nkcohn_Nt6qLNZmAso08Qly4RK-1HFwWJVe-hna6redhiTO04jGx3oIASz5Uk-nYTQ3S4L1YRF2pGsAxt3P2IApA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
۱۱۰ هکتار از خاکِ ایران به افغانستان واگذار شد!
🔴
محسن زنگنه: قرار شده ۱۱۰ هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.
🔴
البته قرار بود سهم بیشتری بهشون بدیم اما یه سری محدودیت هست و اینکار مشکله، ولی حتما پیگیری میکنیم که حلش کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/151639" target="_blank">📅 17:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151638">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
پاکستان مشارکت خود در حملات به یمن را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/151638" target="_blank">📅 17:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151637">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/974cdbcc57.mp4?token=sjcylSndIpqywBfliHDBcLmK2wDdqluhKOgGKCElojx64Ig4e637U84RWuTl3e90GkaZQKlBzu9Jm6g2ht-iZVpru0seQGo_1sdBapMVuNyplRpNvmuBp4V8TZ01uBVPMHgTsfryJK93WzHRgodVAxgeCNxGDtrfooiQqlJh_pUG2uTBxCvTdaWRVmaOP5_bimhO14OnptUX8CmnUhTriDsiADuyFxxGKi8PZQ-lnJSsL9vmPrYASVFWXjyno1sQfm_UjduKNpEaUYf_dKZNJGX3-1iHNwYxu2CpQgqmVk8tPSucVaIuz1WYDTBkbgzYKn5Zl4tAiya7BNy8uhsnPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/974cdbcc57.mp4?token=sjcylSndIpqywBfliHDBcLmK2wDdqluhKOgGKCElojx64Ig4e637U84RWuTl3e90GkaZQKlBzu9Jm6g2ht-iZVpru0seQGo_1sdBapMVuNyplRpNvmuBp4V8TZ01uBVPMHgTsfryJK93WzHRgodVAxgeCNxGDtrfooiQqlJh_pUG2uTBxCvTdaWRVmaOP5_bimhO14OnptUX8CmnUhTriDsiADuyFxxGKi8PZQ-lnJSsL9vmPrYASVFWXjyno1sQfm_UjduKNpEaUYf_dKZNJGX3-1iHNwYxu2CpQgqmVk8tPSucVaIuz1WYDTBkbgzYKn5Zl4tAiya7BNy8uhsnPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حداد عادل: نتانیاهو تهدید به حمله کرده؟ آزموده رو آزمودن خطاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/151637" target="_blank">📅 17:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151636">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
وزیر اقتصاد: می‌دانیم تورم و گرانی مردم را اذیت می‌کند ولی بسته حمایتی دولت مصوب شود خبرهای خوبی برای مردم خواهیم داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/151636" target="_blank">📅 17:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151635">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
اگه دنبال درآمد دلاری هستی بیا
👇
https://t.me/+qUvlXmJGb35hZDNk
https://t.me/+qUvlXmJGb35hZDNk</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/151635" target="_blank">📅 17:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151634">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0031620b80.mp4?token=kFAh6hzjf93FqT2szeoO-woR_ZHK9v-5NH8Vhj4XJwZ_8xkqg5COyZ5YQ6SjPFTo7ieX53OcZME2kRFcU6YsJnQh3nvXNZUKoHUN371eHjzgR5PoIujtFVhgN6CqJJCR15VBnTRYxsOWy9SeoCdIwixIaX5xsX7I9k4OgIooZZXyWDvbGId9d2Z725T7iXAzr9r43O7UXJ0MLlwgrbvt8UcSTEzap6rUdF3bfPY6V8dfMiDR5kfZUItTlnB20iH1fjR6TVOQLOvi72FjZqu5HCQryxyL4VQpMHOVrr-u_77r7swdGew9j2HSLiC76uFmPru0hNWtTnpZK67fIL_uzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0031620b80.mp4?token=kFAh6hzjf93FqT2szeoO-woR_ZHK9v-5NH8Vhj4XJwZ_8xkqg5COyZ5YQ6SjPFTo7ieX53OcZME2kRFcU6YsJnQh3nvXNZUKoHUN371eHjzgR5PoIujtFVhgN6CqJJCR15VBnTRYxsOWy9SeoCdIwixIaX5xsX7I9k4OgIooZZXyWDvbGId9d2Z725T7iXAzr9r43O7UXJ0MLlwgrbvt8UcSTEzap6rUdF3bfPY6V8dfMiDR5kfZUItTlnB20iH1fjR6TVOQLOvi72FjZqu5HCQryxyL4VQpMHOVrr-u_77r7swdGew9j2HSLiC76uFmPru0hNWtTnpZK67fIL_uzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: ما هرگز حاکمیت هیچ کشوری را نقض نخواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/151634" target="_blank">📅 17:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151633">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b2acefea4.mp4?token=bTk-6l6jYVAzJymUzbTkghvSKMZS4TBwnoKEkJf0J5ZS1fTzaxLlqjpB7dzzZloZc7Pr8GPfOm0aB6juZmYoPmsHph6i42yhlhWDooGl-Fl-lMjuCzf3jyy-rTmkKDXr7d7Vznf-gW3wwreRsZmJtcd0421rVSRRbCZwEGeP6wjAAFqnEt6XjvRnb5iPqqiAMk22RnzzpvyYJTsISB5KGzioVY0uiie7j8i3D0BYvSPEwRSINRyMANFJYkFsZwi5oyMI42rnmXpYVEGN76smH2I9ReSGo61jWKX6JYX4P6ap8s9Qp_zdjLnY_PT_qjxIz8b9iEGfD1j6VDaXBFc_vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b2acefea4.mp4?token=bTk-6l6jYVAzJymUzbTkghvSKMZS4TBwnoKEkJf0J5ZS1fTzaxLlqjpB7dzzZloZc7Pr8GPfOm0aB6juZmYoPmsHph6i42yhlhWDooGl-Fl-lMjuCzf3jyy-rTmkKDXr7d7Vznf-gW3wwreRsZmJtcd0421rVSRRbCZwEGeP6wjAAFqnEt6XjvRnb5iPqqiAMk22RnzzpvyYJTsISB5KGzioVY0uiie7j8i3D0BYvSPEwRSINRyMANFJYkFsZwi5oyMI42rnmXpYVEGN76smH2I9ReSGo61jWKX6JYX4P6ap8s9Qp_zdjLnY_PT_qjxIz8b9iEGfD1j6VDaXBFc_vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: پرتغال باید اف-۳۵ بخرد
ما فکر می‌کنیم پرتغال باید اف-۳۵ بخرد، چون معتقدیم این بهترین جنگنده جهان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/151633" target="_blank">📅 16:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151632">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257d408199.mp4?token=YgIpnYpqsP1qcikCtz8LTzN8JY7-XnBvCX_1WukM7a4dbiFd9k2rWi7mF9_0VPjDDvM9eAuz6H1IzxgV-rls1YbA67n_4Ry6c47F9_yvOUTPfcAzSMGbqvd3-HsLrUEw9UG9Nax-OlWGou5CFNzIv05TJS_FNRyZdWs-VekcN9oBIntfwEY-isKXh9wYXOgYu4v-rsnaPchSktNnWJ887odjvLW_XLvgMiz-xg76lBMnYmq-oyk6rKibpSo420EmslsjpLdhtFqUSiZa72Jgnff_u--exe9KOTrzgk6b2OlCAf6J95AjMbAi9cXsQNGxz9eCURdmN_lonnQmnzPN-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257d408199.mp4?token=YgIpnYpqsP1qcikCtz8LTzN8JY7-XnBvCX_1WukM7a4dbiFd9k2rWi7mF9_0VPjDDvM9eAuz6H1IzxgV-rls1YbA67n_4Ry6c47F9_yvOUTPfcAzSMGbqvd3-HsLrUEw9UG9Nax-OlWGou5CFNzIv05TJS_FNRyZdWs-VekcN9oBIntfwEY-isKXh9wYXOgYu4v-rsnaPchSktNnWJ887odjvLW_XLvgMiz-xg76lBMnYmq-oyk6rKibpSo420EmslsjpLdhtFqUSiZa72Jgnff_u--exe9KOTrzgk6b2OlCAf6J95AjMbAi9cXsQNGxz9eCURdmN_lonnQmnzPN-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: حکومت ایران مجروحان اعتراضات را در بیمارستان‌ها می‌کشد
🔴
حکومت ایران وقتی معترضان زخمی می‌شوند، وارد بیمارستان‌ها می‌شود و آن‌ها را می‌کشد؛ گاهی حتی پزشکان و پرستارانی را که آن‌ها را درمان کرده‌اند نیز به قتل می‌رساند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/151632" target="_blank">📅 16:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151631">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f7fed9dba.mp4?token=P_RI4EX8lhJkbFSlL07DN5gWOizY8rePPHwyf-o4LW11wWxc4_9KJbP0u8KcgaasWXinhqL0n2tsNgtEUf1ztVCl29wyB2ulL9lxUVFCAhnRnExPibxkT0VwP1XT1GQh0ZI6dKyivrDSLH8nvKDYP1eXLFsEVpZk-NZfHLvh-HPYr6W9oM1THYpV656uyQvmApIhTNKmrccqJdVEXuIi852Ky3ePQhgm_5m6trRWqqludtdwjrv593Wou4bENBr14i1fByadwIKQwWXyZvbXiCgpWZri1tseMewPhk41InzvDS93FCpgmYSPYm8QsTVJ_lxw_YybQMVUqkmWeqTlSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f7fed9dba.mp4?token=P_RI4EX8lhJkbFSlL07DN5gWOizY8rePPHwyf-o4LW11wWxc4_9KJbP0u8KcgaasWXinhqL0n2tsNgtEUf1ztVCl29wyB2ulL9lxUVFCAhnRnExPibxkT0VwP1XT1GQh0ZI6dKyivrDSLH8nvKDYP1eXLFsEVpZk-NZfHLvh-HPYr6W9oM1THYpV656uyQvmApIhTNKmrccqJdVEXuIi852Ky3ePQhgm_5m6trRWqqludtdwjrv593Wou4bENBr14i1fByadwIKQwWXyZvbXiCgpWZri1tseMewPhk41InzvDS93FCpgmYSPYm8QsTVJ_lxw_YybQMVUqkmWeqTlSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: نمی‌توانیم همچنان به انرژی بخش‌هایی از جهان که دائماً درگیر درگیری هستند وابسته باشیم
🔴
ما نمی‌توانیم همچنان به این وابسته باشیم که بخش بزرگی از انرژی جهان از منطقه‌ای تأمین شود که اغلب درگیر درگیری و جنگ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/151631" target="_blank">📅 16:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151630">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
پزشکیان عازم ترکمنستان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/151630" target="_blank">📅 16:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151629">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a2ba7726f.mp4?token=oXPFTteWC-eJg9yxYUoUXLjGLKBe8irW_XhMsqy2zffSZVkg8-09FU7LQXxx3dIdPKyhDyDNpsPXxk_0L_xux6cSvBBlizh6EqkwrPXGszC8iTOr8DeC-AzJsJPyeOgsrs61zcsk-p81kLUWeN5wEboaetPan-r-GgfBx7bkxvecllev6C4MMFHme8hcH8PY7K5bNuMRRYX7SS1hbcVojPhGm2nly2hxB3hlOp43psKvjohLW_Tscxg0YPcSrtO3d-5IcD1fUqqn_B2N5M-4fwPjzXqaf9C7cyV06ibQ2tKDBknLg_yeoqP57dsKiW11CP2FHN424sCXO-6Qg2Y8fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a2ba7726f.mp4?token=oXPFTteWC-eJg9yxYUoUXLjGLKBe8irW_XhMsqy2zffSZVkg8-09FU7LQXxx3dIdPKyhDyDNpsPXxk_0L_xux6cSvBBlizh6EqkwrPXGszC8iTOr8DeC-AzJsJPyeOgsrs61zcsk-p81kLUWeN5wEboaetPan-r-GgfBx7bkxvecllev6C4MMFHme8hcH8PY7K5bNuMRRYX7SS1hbcVojPhGm2nly2hxB3hlOp43psKvjohLW_Tscxg0YPcSrtO3d-5IcD1fUqqn_B2N5M-4fwPjzXqaf9C7cyV06ibQ2tKDBknLg_yeoqP57dsKiW11CP2FHN424sCXO-6Qg2Y8fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو: کابل‌های زیردریایی در سراسر جهان بیشتر در معرض تهدید هستند
🔴
کابل‌های زیردریایی در سراسر جهان بیش از گذشته در معرض تهدید بازیگران مخربی قرار دارند که تلاش می‌کنند به آن‌ها دسترسی پیدا کنند یا در زمان درگیری آن‌ها را قطع کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/151629" target="_blank">📅 16:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151628">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
بلومبرگ خبر داد:افزایش ۶ برابری هزینه انتقال نفت از خلیج فارس به شرق آسیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/151628" target="_blank">📅 16:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151627">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
بابک زنجانی: میخوام ماهواره بفرستم فضا تا به مردم اینترنت پر سرعت بدم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/151627" target="_blank">📅 16:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151626">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
رئیس کمیسیون کشاورزی: در صورت جنگ برای ۸ ماه ذخایر کافی غذایی داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/151626" target="_blank">📅 16:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151625">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BG6Y0iZkqjSZJdwdUGTy-_V_uYL03cEGhFTwsFxW2W-ZyuzUVof6_-bQ2u16zavBb2_w9fPtuiQT08bVHqbryIq4HEW1S89BUgMwLywc-gdXqpLOZjAeTttQ30z7-DkpxYkpEroz40uhBcAmXZz9ZFJR19vtNjo874dQuatF7jz3Gqv9unQKFFrL_DtDr2YW2TSnuXvJp8uFH9nD1wRFkUZGLTih59Ky7raUezNQM5wwEjAN3WxS-Df5EgUl8uFKKfUMk3UgQro9LgYxl4g5mlsZ4tdvjgYuQOV29e5Xlncd9ok2azIzBDZlWarKDU47STsc02fxptjjMNdRacR3Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نگاهی کلی به لیست افزایش قیمت خودروهای داخلی در بازه کمتر از یک ماه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/151625" target="_blank">📅 16:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151624">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
رویترز: دود از یک هواپیمای متوقف‌شده در فرودگاه ریاض به هوا برخاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/151624" target="_blank">📅 16:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151623">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
رئیس سازمان انرژی اتمی: مذاکره هسته‌ای در دستور کار نبوده و حرف‌های آمریکایی‌ها از روی استیصال است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/151623" target="_blank">📅 16:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151622">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c568889ae.mp4?token=L3aS8bMbrPZ4lpV5rUFyEbBrqsffK-p8LK33L7AOVGAGUk7YCQ0CDK44V2oABzNvh28_bYEKMfEXQkwVjG8hemz-E3I1MnXBVP1ELShDa_phrkEIITnV04LobKVXKcgLhLZq1fBJmJscyKjkeCeIve4B1AIhRvZF8uf9oCf2yF7vG9oCp99dKAfBn-CvOWUP5ozrKEr-Beodlv1zDjD5L6WTLuJgPp6dfeuzIRRnqsXM-TNIhYtC5jQsGecaNWrpb1lq1xr6fzjY4eFdQPpKSuLpvEQvFaaQNulS4dFE19gNxh0eZKxdkLsffOxKWBoUwZJuruRcyq13HIPw-YsdSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c568889ae.mp4?token=L3aS8bMbrPZ4lpV5rUFyEbBrqsffK-p8LK33L7AOVGAGUk7YCQ0CDK44V2oABzNvh28_bYEKMfEXQkwVjG8hemz-E3I1MnXBVP1ELShDa_phrkEIITnV04LobKVXKcgLhLZq1fBJmJscyKjkeCeIve4B1AIhRvZF8uf9oCf2yF7vG9oCp99dKAfBn-CvOWUP5ozrKEr-Beodlv1zDjD5L6WTLuJgPp6dfeuzIRRnqsXM-TNIhYtC5jQsGecaNWrpb1lq1xr6fzjY4eFdQPpKSuLpvEQvFaaQNulS4dFE19gNxh0eZKxdkLsffOxKWBoUwZJuruRcyq13HIPw-YsdSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو درباره ایران: هیچ کاری نیست که بخواهیم انجام دهیم و هنوز نتوانیم
🔴
مارکو روبیو، وزیر امور خارجه آمریکا، درباره ایران: هیچ کاری علیه ایران وجود ندارد که بخواهیم یا لازم باشد انجام دهیم و هنوز نتوانیم آن را انجام دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/151622" target="_blank">📅 16:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151621">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzmfQ0qlQQulBbGBXW0PohPq16Ru7W5ao9sB4S59HuM5evGDoq9jr0lIJyEQUcknkFUox0EJjtxapzhznVo06tMZzAtwAFgOYLjxAWg-0bHQfs7sCUwCtgDVmQFZlitCA37h2msWLQfYfXEb-mkzDwarcIAXzfpspV3FetgPTZnsgSyFRDmKU4EWEZxyOWf-9nnfSLAHB-y-l71qpF-4NhLe3cUEv2UFdtLG92ICTn6AV8ZNIKbJgsfmHw53s6yvhj2AxogsxIZ3BGpC_MBkCUuySBDUckqLOtu420dIEIwnRTcigL_yOZTSro7FosJp-pVnkz_RZwseI-sNLJlG1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فلایت رادار: فرودگاه ریاض بار دیگر تعطیل شده است. بیش از ۸۰ دقیقه از آخرین فرود هواپیما گذشته و بیش از ۹۰ دقیقه نیز از آخرین برخاست هواپیما سپری شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/151621" target="_blank">📅 15:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151620">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
یحیی فست  خطاب به کارکنان تأسیسات نفتی عربستان: از تأسیسات نفتی دور بمانید
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/151620" target="_blank">📅 15:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151619">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-Wrx7PQ14bjfz6TAbnAWy3lJaJCRWIbTXWa5NdxMzhNOxF7srjghc_zpYvRAedbj5lUYVqHi3tTus72CIK1ysM36AjlH_rXYIUIPq_R-M7G_CCV0VdB06mvEe49RpRCG9TawKKln4_JhfSfgejNxfh4jUZtcL-IJkO5cgFWblsAON9oUFuVw3IbifFzgCVf6fmmBZISyn8MnX_CKIQuC8-onp7Kk8vi0211LacG4Rq3t0s2AHXVvVU5PIoHK3nuq9yEXrwY6mMOCJYDdXyH5951qt92xvxPbqqhWjC-ZtFCr2a1Asue15LNvnxMp8j9GX-_367Sm4cjfekC-CQwjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله خونین روسیه به اتوبوس‌های غیرنظامی در کراماتورسک؛ دست‌کم ۳۳ کشته
🔴
رویترز به نقل از مقام‌های اوکراینی گزارش داده در حمله روسیه به خیابانی در کراماتورسک که دو اتوبوس شهری در آن حضور داشتند، دست‌کم ۳۳ غیرنظامی کشته و ۱۸ نفر دیگر زخمی شدند.
🔴
مقام‌های محلی می‌گویند این حمله با بمب هوایی انجام شده و محل اصابت، ایستگاه و مسیر حمل‌ونقل عمومی بوده است. روسیه تاکنون درباره این حمله اظهارنظر نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/151619" target="_blank">📅 15:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151618">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3IyA29wykPXcceGsM8wm4VXK2BZDbv9nmIeOAyNfOAV65f14uvmt9AZh_lc82SYR-p-HVS8BCInnNKPDPJlU1xfx9OYPVo9Spnd3_rpi1Pe6oXJXovbPyRrIkMVySaGGh0_KP6A715Sz2YqO6d1vhB4pKPRVppxoJKLvdIcY_yWYmwCZrNny1xYJYt_AOiBsFeQn8itEwH4XKw2Jc0wWQrRPCjBTNl3LUtAHJN43CpPvI2dv9NxTXP1GZvhyYjjoVtJRCSqwhCH3RQJfZRJbVpWzYvfZxd9ZRlSaielPattEsUAnMOlLvXdkOECNcz8yoC6D7q0H7Ht6x4byzSZ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: جایگاه اصلی مردم و کشور ما بسیار بالاتر از آنی است که الان در آن قرار داریم.
🔴
همه باید دست به دست هم دهیم و با اتحاد و انسجام و تلاش و کوشش ایران را به جایگاه اصلی خود و قله موفقیت برسانیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/151618" target="_blank">📅 15:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151616">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eb0d3431a.mp4?token=uHi1xMuJKR2YInUGCJ3nzZJJf-nM0akV-yJIf4F1q5JUMdpEPjrwGpYRy4NO6zFtix1WoAohd5cGy5rjmByAxvykMXCaNptrHtnLHrasUyBLUy7B7298DpvLVpdrn50r5qAwoGlmPohnHD4ETgR-0iW3uFKPNXxSNXS7cm5USarjuCbaYPs2wQ2x5TTKRDfYakF1U66h0a9RC5ZjxUOGb7smsyc4PW8ZMBfMhyv8m_f5HkYP4UhCI0GqLHot2RPb8OK72667WmCIefhEdZqgIKjd8aU-ukyIgpzAD6jA8lqnZSL0ExgvenjxO8Nscubk3iaZyhYCi6GnFBD7lr4F1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eb0d3431a.mp4?token=uHi1xMuJKR2YInUGCJ3nzZJJf-nM0akV-yJIf4F1q5JUMdpEPjrwGpYRy4NO6zFtix1WoAohd5cGy5rjmByAxvykMXCaNptrHtnLHrasUyBLUy7B7298DpvLVpdrn50r5qAwoGlmPohnHD4ETgR-0iW3uFKPNXxSNXS7cm5USarjuCbaYPs2wQ2x5TTKRDfYakF1U66h0a9RC5ZjxUOGb7smsyc4PW8ZMBfMhyv8m_f5HkYP4UhCI0GqLHot2RPb8OK72667WmCIefhEdZqgIKjd8aU-ukyIgpzAD6jA8lqnZSL0ExgvenjxO8Nscubk3iaZyhYCi6GnFBD7lr4F1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی: روند مذاکرات ادامه دارد/ ظرف چند روز به پیشنهاد آمریکا پاسخ می‌دهیم
وزیر امور خارجه:
🔴
روند مذاکراتی همچنان ادامه دارد و از طریق میانجی‌ها پیام‌ها در حال رد و بدل شدن است.
🔴
ما طرح خود را که تحت عنوان «طرح هفت‌روزه» ارائه کرده بودیم، مطرح کردیم و دیدگاه‌های طرف آمریکایی را نیز در مقابل آن شنیدیم.
🔴
در حال حاضر مشغول بررسی دیدگاه‌های آمریکایی‌ها هستیم و فکر می‌کنم ظرف چند روز آینده پاسخ خود را ارائه خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/151616" target="_blank">📅 15:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151615">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
بیانیه سازمان انرژی اتمی کشور:
از حق غنی سازی خود به هیچ وجه دست نمی‌کشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/151615" target="_blank">📅 15:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151614">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
اگه دنبال درآمد دلاری هستی بیا
👇
https://t.me/+qUvlXmJGb35hZDNk
https://t.me/+qUvlXmJGb35hZDNk</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/151614" target="_blank">📅 15:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151613">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
عراقچی: روند مذاکرات ادامه دارد؛ ظرف چند روز به پیشنهاد آمریکا پاسخ می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/151613" target="_blank">📅 15:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151612">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
عارف: همین روزها کالابرگ افزایش پیدا می‌کند؛ در مرحله نهایی کردن تامین منابع قرارداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/151612" target="_blank">📅 15:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151611">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
قیمت نفت برنت ۱۰۵ دلار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/151611" target="_blank">📅 15:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151610">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
وزیر خارجه ترکیه: توافق مکه یک توافق دفاعی است، نه تهاجمی، و اگر به یکی از طرفین آن حمله شود، سایر کشورها در کنار آن خواهند ایستاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/151610" target="_blank">📅 14:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151609">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pj4It4jokcEnSlYMuInvrqNbmoir14cWhRnv89a7f7EWVBO9gzAYttYxaDWsyGQjJiBTYSQdVrWKOGIhPcHbzniF78Sec1xQz8n7MrMdX_NpL2oUfzqqUOxTVh9ClcCkV_KrPp-pPHltHzFoQPNPFjchrpgLImtATk6y8EaiBair9mLKwsFplzGEUS_iXS7xaMbhHRsupzvDAWyHpZxuqYZBuMuflwkQjSnaQk60iWW_TuQ07NVPW-O3yzetNt0FIJnhN4lyNqNkl5ox6raDbSGBBrFuKC77F3AnQODpGgajvy5_gmgm_xO5oEBUJTy-Cg0pjEE5S0iMwZweRcG3tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ از طریق شبکه اجتماعی Truth Social
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/151609" target="_blank">📅 14:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151608">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
علی مطهری : در نهایت ترامپ مجبور میشه توافقی رو امضا کنه که خواسته‌های جمهوری اسلامی تو اون تامین شده باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/151608" target="_blank">📅 14:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151607">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
وزیر خارجه ترکیه: نباید اجازه دهیم دریای سیاه به جبهه جدیدی در جنگ روسیه و اوکراین تبدیل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/151607" target="_blank">📅 14:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151606">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mu4Eq8-jATIVNwKC5DnOaf_qyCmxtZcWCnn6HkIokJf1IRgRZwqPnE5v2ro3zHYHzDLVhB1U_ZnsKzjyiis_Ve0-PUi66--EMkm7Zyv_T3GLikscGIF4FXenkG6gwk__BlHix8VDI9KCnkEg8qQ7Cw-62ptBgOWxMY-8B3SRxhSDHe0S-hyByIlPrXju2_Fl86EbV1ZCSYlKKfKLyyGXX47CtgpclTuYHLGsSUmQglwmPBSJ47GFl_08FopOTgGKo0T7RaLjqFOqs36u1mME4lx7xWz_aSok_5Etf4YgBeGpPgiAPx-WBttDzaVzonGgchVSauyTpfyE4pNMJWrkEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این فرد ۳۷ ساله آمریکایی از خانوادش شکایت کرد و تو دادگاه گفت من نمی‌خواستم تو این دنیای مسخره به دنیا بیام شما باید قبل از بدنیا اومدنم ازم سوال میپرسیدید و الان غرامت میخوام
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151606" target="_blank">📅 14:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151605">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
هشدار درباره احتمال حمله به پایگاه‌های آمریکا در آلمان؛ رامشتاین و اشپانگدالم زیر ذره‌بین
🔴
جروزالم پست به نقل از نیویورک‌تایمز گزارش داده اسرائیل به آلمان درباره افزایش خطر حملات احتمالی مرتبط با ایران به پایگاه‌های نظامی آمریکا، به‌ویژه رامشتاین و اشپانگدالم، هشدار داده است.
🔴
ارزیابی‌های اطلاعاتی احتمال استفاده از پهپاد را نیز مطرح کرده‌اند، اما تاکنون زمان یا هدف مشخصی برای حمله اعلام نشده است. هم‌زمان تحقیقات درباره طرح ادعایی حمله به پایگاه آمریکایی فرفورد در بریتانیا نیز ادامه دارد؛ ایران هرگونه دخالت را رد کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/151605" target="_blank">📅 14:17 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151604">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de3d2ed693.mp4?token=TRckK5I217Xuf2hNTpC8q5qivQFHH08_cyIaBFamTTNHdPIRamTZDffpGMaxYihjxZcwOgL454canHRAFWny4ll-71ywsPJ2EFdasFisrP9PKsF8m8fl2NGXknpyEwd2_Jrayyy4wOpwwHbGdhJ9jLU7WRhFj2fVKI90IDmyPKrDmEcZN6Uy1OJev4wrGGiQa7MDNd1hlgRURpzRdamk4O6TrljySB8F44vmD7jPjB8mzpZRwGLqu_HqdWT3ZbQ6omOIYfZgfnhVb7KlRqBB62CK9Zyug_YghWzfq9CKsL321do5WYxxPNl-CPCfYp35mDd-AY1NGxBckiyeJ5Jy_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de3d2ed693.mp4?token=TRckK5I217Xuf2hNTpC8q5qivQFHH08_cyIaBFamTTNHdPIRamTZDffpGMaxYihjxZcwOgL454canHRAFWny4ll-71ywsPJ2EFdasFisrP9PKsF8m8fl2NGXknpyEwd2_Jrayyy4wOpwwHbGdhJ9jLU7WRhFj2fVKI90IDmyPKrDmEcZN6Uy1OJev4wrGGiQa7MDNd1hlgRURpzRdamk4O6TrljySB8F44vmD7jPjB8mzpZRwGLqu_HqdWT3ZbQ6omOIYfZgfnhVb7KlRqBB62CK9Zyug_YghWzfq9CKsL321do5WYxxPNl-CPCfYp35mDd-AY1NGxBckiyeJ5Jy_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همتی خطاب به وزیر خزانه‌داری آمریکا:
🔴
فقط ۳ روز وقت داری!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/151604" target="_blank">📅 14:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151603">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
آکسیوس: نتانیاهو و ترامپ در 72 ساعت اخیر، 2 تماس تلفنی درباره ایران برقرار کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/151603" target="_blank">📅 14:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151602">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20116b71ff.mp4?token=FzuwOJ2GCq2cBMIRJ8NFfuHbs-hFIrbpFzwiGiDQ5lgEoeLYPJZI5jpOBr4DxQr9qNKak6apVziEh1be52ApOiIkb8P_HKiaoQJhHiiwxO2GjrGjuGbDJaQAIwU5Yi62JPLWtIwh6hks5hVCVJTlAUL6S9jYmfhpGJnU9-w9FBXLN_aFxZ5xiRG4hWc9NeC2CvqNbaQc24_hemq1y0dHgY4pIGw_Iyvy-H-JR9RHXB3CfAUgWnxfwCd9rm0iFBQ_opfwxhO11osVRn6HkAeF2UIKr8gMqusxHiE6GNWBetHip8zTyjufUZizCo5asaqSsokz5OJPNGuwGnDACkyJWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20116b71ff.mp4?token=FzuwOJ2GCq2cBMIRJ8NFfuHbs-hFIrbpFzwiGiDQ5lgEoeLYPJZI5jpOBr4DxQr9qNKak6apVziEh1be52ApOiIkb8P_HKiaoQJhHiiwxO2GjrGjuGbDJaQAIwU5Yi62JPLWtIwh6hks5hVCVJTlAUL6S9jYmfhpGJnU9-w9FBXLN_aFxZ5xiRG4hWc9NeC2CvqNbaQc24_hemq1y0dHgY4pIGw_Iyvy-H-JR9RHXB3CfAUgWnxfwCd9rm0iFBQ_opfwxhO11osVRn6HkAeF2UIKr8gMqusxHiE6GNWBetHip8zTyjufUZizCo5asaqSsokz5OJPNGuwGnDACkyJWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک کشتی‌گیر در مکزیک با کوبیدن داور به تشک در داخل رینگ، باعث مرگ او شد
🔴
این داور 75 سال داشت. به گزارش رسانه‌های محلی، ورزشکار مذکور بازداشت شده و پرونده‌ای با موضوع مرگ ناشی از بی‌احتیاطی تشکیل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151602" target="_blank">📅 13:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151601">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
الجزیره به نقل از مقام کاخ سفید: اظهارات ونس، همان موضع دولت ترامپ مبنی بر ضرورت انجام اقدامات ملموس از سوی ایرانی‌ها برای رسیدگی به مسئله هسته‌ای را تکرار می‌کند و چیز جدیدی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/151601" target="_blank">📅 13:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151600">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
پزشکیان: جنگ اقتصادی قابل مشاهده نیست و به‌مراتب سخت‌تر و سنگین‌تره.
باید از برخوردهای تند و سلبی پرهیز کنیم.
مردم باید بدونن که ما برای حکومت کردن روشون نیومدیم، بلکه برای خدمتگزاری اومدیم.
🔴
جنگ اقتصادی  رو با خدمت‌رسانی و همراهی مردم شکست می‌دیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151600" target="_blank">📅 13:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151599">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
اگه نمیدونی دلار و طلا بخری یا بفروشی حتما اینجارو داشته باش
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/151599" target="_blank">📅 13:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151598">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
برخی منابع خبری از شنیده شدن صدای انفجارهای جدید در ریاض پایتخت عربستان سعودی خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151598" target="_blank">📅 13:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151597">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
نیویورک‌تایمز: بر اساس گزارش‌ها، پاکستان به عملیات نظامی عربستان سعودی علیه حوثی‌ها در یمن پیوسته است
🔴
یک مقام ارشد نظامی پاکستان گفته است که جنگنده‌های پاکستانی در حال انجام حملات هوایی علیه مواضع حوثی‌ها هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151597" target="_blank">📅 13:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151596">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayPUd5BJia3fhdQvAzt8jAsmwTJJCGSjk5eED3gS8a9QPyWA-OH2vLfo909INxJsbtpBreWH-pRq6cCkoibXOp-tlWrYG4PeQBHwokYiNoBlXWFAfT5KuDTryfTxiLqSOrfA4MdsDjV6P4I1Tmcp-HtEDMWhDJ6cE_DWk2Og-tFIpfrJ8Ok8bRdotezDni_2KUgULyuXCkzBrNruoFCTZShLICJI894KH7xF9jNjzjmyhA0hoEAg4VaIMhOhiuQC_NjY9hSYcG8zjJGw6FlH8O56ZKTwL-3fRo4ie7YkFLTzu1NdU8IpSecSGZYtMjQ84l7WrmHPuDUyYWnHboeJBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ناو هواپیمابر آبراهام لینکلن آمریکا به سن‌دیگو بازگشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151596" target="_blank">📅 13:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151595">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6H1k8WioKeyZ-b-lkEoeANlqimxXcIENiuSuivkb5EvTF3WtacxTMFNEDoK1z8NagmNndHxnURdrTsz5J5Yj1bxs2aZSDHoZ_0qTVjBo9A9-QmQVeDUXob2vu_mohfu4pygiAn8pbK7VSwCZpz5ZMS5nFAAxlFBK1VU4-vppGIFg_nB4uuVHuH5VMDqz_Ps6GOKRf8ZlYdB9l2GPSXmBhwr1eB0baXqM-LSDvBVEe8tbV7Ry3sfXGlFZdHprI3rpT_8PiHPeN-Qa6krT1sjiQfE7_Pw6P1fyrwaJ1gLIeCLGyADqgmVyfGd7_gN1xRKnRqGRE1EdN6oh5Q3ERhzgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: خطای یک کارمند، قطعات حساس جنگنده اف-۳۵ را به چین رساند!
🔴
چین پس از آنکه یکی از کارمندان شرکت یونایتد پارسل سرویس، ایمیل هشدار مبنی برعدم ارسال محموله از طریق هنگ کنگ را از دست داد، موفق به دریافت قطعات یک جت جنگنده رادارگریز اف-۳۵ شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/151595" target="_blank">📅 13:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151594">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
عارف: می‌دانیم حقوق و فوق‌العاده، کفاف زندگی را نمی‌دهد، اما شرایط، شرایط جنگی است و مشکلات داریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/151594" target="_blank">📅 12:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151593">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbKOnWVqv4pzrjPRkkyMfi76QRQg4ekfYjF7_MLZtjimqWJA-M_mYXqYxxkfIrvIb3URban0iMD0p9cvc_D62-jO9lIsLL8VUQrsoD0HHX0OssZzglMqPiPGn6-tQDiyFGCloZ1g0o6rzgwPJyaIJbUiMkG9CeD-xL7ItuSyQZXXIUHCyhoQQ9wEMATG4_Phap_eJc7XehbZxpmtehCHxS_JHkDyRxoeGFSREjdFtIIhqsl4nLoW6ifD7gsX5fWyBeXxFnnNTHiKGVDjQUe2wAJyDLcQpCbf6KAUOJ7Lv-yEJsXLrb9atg1XXKHVfFGIUImY1rFLmTcW6RISi6CbQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باهنر: عده‌ای در میادین یک دفعه راه می افتند که «آقا ما مذاکره نداریم»؛ بیخود کردید که مذاکره ندارید؛ اصلا نتیجه جنگ در مذاکره مشخص می‌شود
🔴
یک دفعه امام جمعه یک شهرستانی در کرمان گفت «آقا شما چرا دارید مذاکره می‌کنید؟» گفتم «آخر شما سر مذاکره را می‌دانید چیست یا ته آن را؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151593" target="_blank">📅 12:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151592">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLv7KCPIPVFBc7sqK8m_tr7QqvrIUuRIdIaLtlXyZ6nlLEZMnsEi6WhpU_rbxItn8At4vPuBetmhF6BtA5rY1R9LPLuI40efvDk39lZRZRuCCV_l0CP-bJSXkGJsokyQ3iHcjkBaybRTEfgG79NH3ThS3Lg8SJAy9m8yfP3Wx__UGbeGsYg7VS73_AlKixOiG9X3HPzqypqXZguQlsZnHu9_VHdfIM9H6g2-PdN4x1nhZtNNyJHubjdC00-4nAj9COrqWq1lC6peV9hxTCHo-EV1IEgfpkQZuokyIYfCd8pzVEXeBu77ciSvtEJMQf0fvRXMg9TtC2HqJiecyOgnFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز، ۱۶ مهر، روز بزرگداشت داریوش بزرگ است؛ پادشاهی که امپراتوری هخامنشی را به اوج قدرت، نظم و گستردگی رساند و تخت جمشید را بنیان نهاد. یادبود مردی که نامش برای همیشه با شکوه تمدن ایران گره خورده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/151592" target="_blank">📅 12:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151591">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpO7J6KgrGxQFGWMiJo0I7zeX3vD19XQvvXJTniFOjOG9RzYynDlw3pp_6u5QCNEgHZTUtjBkPCrD7PD-6Mf6kjV11UDONLYSnp4UvDeWRgV41LbTICMJ_NMV5bgc_rB76k2DuKjXo_TqLZ5p4J_YN8y_qnmbjQWbnMXbUBNREF-n-DhrIm3ku4t8PUXRkzAhdVl_6RtJA9jGTV051Ys3TG9__jTKsGadllVVwCGeTYXkQwALNu2K0_5L6kuSwQaVap9YYXUzeGS3CRrLOIQl72JXJzBDQXgE1HkPbgM6J2EoKDB2o_eyZlOjgvpisUy-EozSmza4tBYKdwfUzqCQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش آکسیوس و به نقل از مقام‌های آمریکایی: پنتاگون به سنتکام دستور داده که آماده‌سازی‌ها برای احتمال ازسرگیری عملیات‌های جنگی گسترده علیه ایران را نهایی کند. هنوز هیچ تاریخی برای این عملیات تعیین نشده و دونالد ترامپ نیز هنوز تصمیم نهایی را نگرفته است.
‏
🔴
با این حال، منابع آمریکایی و اسرائیلی می‌گویند حملات مجدد ممکن است پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر آغاز شود و حتی احتمال دارد یک هفته زودتر، یعنی پیش از انتخابات اسرائیل، شروع شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/151591" target="_blank">📅 12:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151590">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4v4Mal8v6jOytcxgymVWXi7fsO4tga3MEvhSya6acodMZycaLs7Mc7Qke0tJXllSRvSXuMsm4LN2TM9zgxp7RONxglYbgABsAY2a2a4gLjmgINbwBDesgZkL7Wu-Pew_pau6f-f19aW3C5OuUNIrbjXJDIrtIRFTvzjZtRw7PdG5EXxE3O2B8xN2AkFkbRzgRQVA_GeTAbqBywFwdQSAfn8gFSdcJDV7poD8h5wI_rv--IzIDujuBNogyi1NNkvWhjXusqxC-lo9Orz3Nie4LJPhGqzv1F2FwcJJK7Z2M-cIFm6jvrP6VIqJmS5tTWJDpXpUnkVp2thuvDj4NeMVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای نظامی نوع C-130J متعلق به کویت، به پایگاه هوایی الخرج در عربستان سعودی رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/151590" target="_blank">📅 12:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151589">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5afe7ea756.mp4?token=KNUIzcZ0VS-aVFclAHl3C7GOUaFRfdte85Z_aowWNALHhYTS0pWJgN59v04hu9Z2KRwB5V4YSqJ3fuKmYzvdxUfiEYE0xMuUD5Dq05FxvW9ktj82J9XglXNCo_eJyVxCumj99M05nVzK7o6x_RGpYrh65TGPcS8x1U8lQUzhOrz1aNl9uczIAPOUakYN60JXKE4tGhcwIZOUNhWgk9iVGjG8SFmDoP3KZICyP6xuHEgYTtpbSQznQOd-6HXHi7-HbKxteluXx_Zy94jXPQ1QGo8qW8-YIS1vLGx8R2_ABDYw_aQux0jm6MkwyD4lYOs7qwHXpmQOJDqNwuadeY7Mug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5afe7ea756.mp4?token=KNUIzcZ0VS-aVFclAHl3C7GOUaFRfdte85Z_aowWNALHhYTS0pWJgN59v04hu9Z2KRwB5V4YSqJ3fuKmYzvdxUfiEYE0xMuUD5Dq05FxvW9ktj82J9XglXNCo_eJyVxCumj99M05nVzK7o6x_RGpYrh65TGPcS8x1U8lQUzhOrz1aNl9uczIAPOUakYN60JXKE4tGhcwIZOUNhWgk9iVGjG8SFmDoP3KZICyP6xuHEgYTtpbSQznQOd-6HXHi7-HbKxteluXx_Zy94jXPQ1QGo8qW8-YIS1vLGx8R2_ABDYw_aQux0jm6MkwyD4lYOs7qwHXpmQOJDqNwuadeY7Mug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پل هوایی آمریکا به سمت خاورمیانه همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/151589" target="_blank">📅 12:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151588">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
وزیر خارجه اسرائیل: کنسولگری بریتانیا در قدس امروز فعالیت‌های خود را پایان می‌دهد و در نتیجه آن، انگلیس هیچ اقدامی علیه ما انجام نخواهد داد
🔴
بریتانیا می‌تواند فعالیت‌های محدود خود را در این ساختمان با حضور تنها ۷ دیپلمات ادامه دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151588" target="_blank">📅 12:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151587">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ایلام با تورم نقطه‌ای ۱۱۴.۳ درصد در شهریورماه صدرنشین استان‌های کشور شد و فاصله تورمی استان‌ها به ۳۹.۷ واحد درصد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151587" target="_blank">📅 12:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151586">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
خبرگزاری رویترز:  یک ماه پیش، ایران 200 میلیون دلار به حزب الله کمک کرده.این پول خرج مردم آواره میشه، حزب‌الله قصد داره تو مرحله اول به هر خانواده‌ آواره، 3 هزار دلار پرداخت کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151586" target="_blank">📅 11:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151585">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siF00xEAfrpQXKxsnNZP6fFmDxhxpa9wDP0nEV3rikSGALm7ZBqkioChWX8AUhznzJn7QXOt9Fe8MpCfZ5zvc-SoKNkesI9Sbj2XIrOqjxfE9hwDtnsu_CD8uZrbZ7CZn3T1pALom3grH0Vl6bfNBtG14mb1ygDVaNoPuj_FWmMueyUMuRnxlAOyT5cWlxzQEAN5vrLd_8iyDZXC1mQvR1QwBH7JVwRCCAAGIayluURTTvYqwVXAh8Dtmcif0eVC9nSUNzTx7nad8XFuburZ7zzHC09wAn3aLNgLG_orI98lWK4i2wh9PhFo2coHOiuiKcJXmTmaPUSKOs08XZrqyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مردانی که فقط در برابر خدا زانو می‌زنند؛ تصویری از سال ۲۰۱۵ در سوریه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151585" target="_blank">📅 11:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151584">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4T2oQ6qpTNkoR0nzOm9dfSrAiPRhQVmflEHa6hb5Krl0pSbDCz3AeQUAUA9zSGzcLyiFKK2SNvIgzdLlQWqBUf7uPuwYUyHcPJMNMS0qkXppP6h5cmitTp8-HFtBOHydyKgUYCZqK1cU8NGc4v_XYPfNB4KdbHkibcyD3Mm4fKY8dj4V6UXVUbUDs2YzAYdEqJBcmi_GeMP9i0j4Mi1H2_BUxtQk52qBVWKmAeERHSIYZLc9TwJ_o-thiBD_N4JZ8wO7EjESfK1JYWRifjDtLQKMCGLzMDTF9nWaBJ0oJI_qNP53aByRmB9QQr4Zn3w23FXIzEPrENvEq0QcP5rww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ممنوعیت پروازهای هوایی به فرودگاه بین‌المللی ریاض در یمن همچنان برقرار است. ۱۱ هواپیما از فرود آمدن در این فرودگاه خودداری می‌کنند و مسیرهای دایره‌ای در نزدیکی آن پرواز می‌کنند، و برخی از آن‌ها مسیر خود را به سمت فرودگاه‌های دیگر تغییر داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151584" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151583">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
منابع خبری از شنیده‌شدن صدای چند انفجار در پایتخت عربستان و توقف پروازهای فرودگاه ریاض خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151583" target="_blank">📅 11:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151582">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
شرکت هواپیمایی عراق (Iraqi Airways) پس از ماه‌ها توقف، پروازهای خود از فرودگاه بین‌المللی نجف به تهران را ازسر گرف
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151582" target="_blank">📅 11:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151581">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
دولت سوریه پیوستن این کشور به جنگ علیه حوثی‌ها را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/151581" target="_blank">📅 11:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151580">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc94aa88e0.mp4?token=FJZw9QcsEDJ2pDd5onFs_z-n2MtYcJ59FRHKq71uRrR4vEE-5sUAWv9-YEa7SRZF8HtdK_z_9lMLQGl7Ip5acBBbrT4COVj6jd4ijIlSVaCszDJ7jfDIbOqw8W_ou2numduvsnTE-y_l0et4tbQ4qiQvPRfFVGUVOy_fYI6Av9AfF3JfVMoKF9FYlm7ESE7IO1JQPF-rTjWFFUx6zhAoM3ultwOiAhSxypZGvO5UNdhraaHpYxeCJDGjyfLnGJ_JAOLJxhBxmuDNaHlaICTvlAM_95oBGzDzepifco8dGmRKUO1e7X8rN4kr9NjNDGHFc-tovYzATHcbiZZ-ZoONBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc94aa88e0.mp4?token=FJZw9QcsEDJ2pDd5onFs_z-n2MtYcJ59FRHKq71uRrR4vEE-5sUAWv9-YEa7SRZF8HtdK_z_9lMLQGl7Ip5acBBbrT4COVj6jd4ijIlSVaCszDJ7jfDIbOqw8W_ou2numduvsnTE-y_l0et4tbQ4qiQvPRfFVGUVOy_fYI6Av9AfF3JfVMoKF9FYlm7ESE7IO1JQPF-rTjWFFUx6zhAoM3ultwOiAhSxypZGvO5UNdhraaHpYxeCJDGjyfLnGJ_JAOLJxhBxmuDNaHlaICTvlAM_95oBGzDzepifco8dGmRKUO1e7X8rN4kr9NjNDGHFc-tovYzATHcbiZZ-ZoONBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استاد دانشگاه امام صادق: برای دفاع و حمله دیگه چیزی نداریم و همشو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/151580" target="_blank">📅 11:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151579">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c02b0d385.mp4?token=PbAaA2sxRPfax3qIkzLWgGpp3P_YpPjc-Hl28Ty8Psh0gPFKLkndscls2CXMRLpGOdK-JBv8GwaVJLw4Vbd4WkmEt3hWAj3T9GBcS4PWhelPdpFJTq-GKqj3FKodpGeGtrzNmCrhGbqwDUEIooF1uF9B_27XbgcsYzi1nbEcLL9BHusuTLfTcYLwysg_t_fkc8p-l50GZjkbYvq3XXcKoTFYRibGMOBdMmEs8Gogti8d36H69_VoWJaS3D6m3YjtAm2fswAjV_Z369zfOArKW73cIFGjFMhecJoedagu-4DOg7aPEUhlN623c928UEoXKs9QjPhFzyiP4u9fcXCxCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c02b0d385.mp4?token=PbAaA2sxRPfax3qIkzLWgGpp3P_YpPjc-Hl28Ty8Psh0gPFKLkndscls2CXMRLpGOdK-JBv8GwaVJLw4Vbd4WkmEt3hWAj3T9GBcS4PWhelPdpFJTq-GKqj3FKodpGeGtrzNmCrhGbqwDUEIooF1uF9B_27XbgcsYzi1nbEcLL9BHusuTLfTcYLwysg_t_fkc8p-l50GZjkbYvq3XXcKoTFYRibGMOBdMmEs8Gogti8d36H69_VoWJaS3D6m3YjtAm2fswAjV_Z369zfOArKW73cIFGjFMhecJoedagu-4DOg7aPEUhlN623c928UEoXKs9QjPhFzyiP4u9fcXCxCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه درگیری دیشب در تگزاس وسط سخنرانی ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/151579" target="_blank">📅 10:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151578">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل: پنتاگون به فرماندهی مرکزی آمریکا (CENTCOM) دستور داده است آماده‌سازی‌ها برای احتمال ازسرگیری عملیات‌های گسترده نظامی علیه ایران را تکمیل کند
🔴
بر اساس این گزارش، حملات ممکن است پیش از انتخابات اسرائیل و آمریکا آغاز شوند؛ با این حال، دونالد ترامپ، رئیس‌جمهور آمریکا، هنوز تصمیم نهایی را اتخاذ نکرده و هیچ تاریخی نیز تعیین نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151578" target="_blank">📅 10:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151577">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOG5yGYaE5hQwTaoXHWR7fXMcX_MVh6YMSrFwnGepKClyD6XAnJ10b4cevkQTUWLQT_zqgEeCRB01_CXBngLc_JT7E3Omhtnf0pf9Xg87ixg2FhwZ0oYRBOKsoHlWltubckNTuLhEXJmnwK_pWgdOADu3qv1-Ep7OAZKGSNa5gDxPXRA_fT-P1rTiDibCYuqMldg_wqbOltVmu2wF1hxAiyDl29RYEnajgFkeTz5kPyrNeWTXJPMF7czmMzhQP9QFraf7h14882_HlvqEhXqvmPWJellOqPIlYcrCCV20GzzPFyOVbcR7mZWn_97T1v6dIqQ9jQoqIgBQDAwpTtsvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
اسطوره کریستیانو رونالدو پست لیونل مسی رو لایک کرد و نوشت: «لئو، سال‌های زیادی برای کشورت جنگیدی و میراثی از خودت به جا گذاشتی که برای همیشه ماندگار خواهد بود. تمام احترام من برای تو بابت تمام دستاوردهایی که با آرژانتین کسب کردی. یک بغل گرم!.»
@AloSport</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/151577" target="_blank">📅 10:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151576">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتبلیغات الونیوز</strong></div>
<div class="tg-text">👈
پلن ویژه افزایش ممبر برای کانالهای تحلیلی و اقتصادی داریم جهت اطلاع از شرایط به دایرکت پیام دهید
دایرکت</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/alonews/151576" target="_blank">📅 10:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151575">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ان‌بی‌سی: دولت ترامپ خواهان توافقی است که مسائل مهمی مانند برنامه هسته‌ای ایران، را حل‌ کند
🔴
واشنگتن علاقه‌ای ندارد تا بار دیگر با تهران به یک یادداشت تفاهم درباره تنگه هرمز دست یابد و مذاکرات هسته‌ای را به آینده موکول کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/151575" target="_blank">📅 10:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151573">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c407317afc.mp4?token=Nod0Z4fDa6c6zWZLeAOR_cvhaWQvXWzFW8ayd77ojZuu6YSA0l3MlPV0u_zAgVQbTOdiJ11NUhuEqbvovZebRa7jlh2Njq2JEV6oYhPwxSd1fXhaBH8f2lfIlFHss_mZBSE37fWU-MkaoD6E6mwkpo-aq59BhH49v8T-hMH4O-j9A52pBATQi1IBYGtqBZZlHBwsB3AQuwhB797eaNSs4S2xRzNDc0ZcvzzqeNF4iqu4g7VulpnJ-v3XVPc1F9O6TTQWH10jvnZMXX3lN0F85UOF-7intmFfmhM1ZRcz5Sm2uJE4lVhhhLQMehgKD2qcKVARpB01ydicP0VKFkRU6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c407317afc.mp4?token=Nod0Z4fDa6c6zWZLeAOR_cvhaWQvXWzFW8ayd77ojZuu6YSA0l3MlPV0u_zAgVQbTOdiJ11NUhuEqbvovZebRa7jlh2Njq2JEV6oYhPwxSd1fXhaBH8f2lfIlFHss_mZBSE37fWU-MkaoD6E6mwkpo-aq59BhH49v8T-hMH4O-j9A52pBATQi1IBYGtqBZZlHBwsB3AQuwhB797eaNSs4S2xRzNDc0ZcvzzqeNF4iqu4g7VulpnJ-v3XVPc1F9O6TTQWH10jvnZMXX3lN0F85UOF-7intmFfmhM1ZRcz5Sm2uJE4lVhhhLQMehgKD2qcKVARpB01ydicP0VKFkRU6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای، دود برخاسته از بندر دوحه در قطر را نشان می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/151573" target="_blank">📅 10:28 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
