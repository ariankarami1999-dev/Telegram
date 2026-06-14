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
<img src="https://cdn4.telesco.pe/file/puVy353vPb7d6UE4Gagx_fYfykHBsEkUqxeYAxpYXLs243-rOQSgE-wioe724d4EHr1uHyCnXaHVC0GBlUj2UEfKHZJPMi6qSMDFkYT1qvxbIZiIFct2pR1bKZYxB4FQYKFhCsHhch2xIc-H9-gX0sq4ItrSWywfIHgQXI5L5Wd7iXf6GbbdXaC8eqv8pnqz_PeGj4ht8v3labKRbIdtZUIUjLNu3I7wm7fF1RPcmy1NsFiDRHcuGaQRJuoCkPAcnTAiQ16QjuHcY-fHA_9updrAW63PsugthGpRpkyGy48KYAf70-HAtSdFtuqyPL8ATWsOguX1957MytrI_eFdfg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 225K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 18:06:42</div>
<hr>

<div class="tg-post" id="msg-66082">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بی‌بی همیشه دقیقه ۹۰ دست بکار می‌شه مثل ماجرای فخری‌زاده و برجام، باید ببینیم حملات امروز به ضاحیه ترور مقام بلند پایه مثل نعیم قاسم به همراه داشته یا نه! #hjAly‌</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/news_hut/66082" target="_blank">📅 18:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66081">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بی‌بی همیشه دقیقه ۹۰ دست بکار می‌شه مثل ماجرای فخری‌زاده و برجام، باید ببینیم حملات امروز به ضاحیه ترور مقام بلند پایه مثل نعیم قاسم به همراه داشته یا نه! #hjAly‌</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/news_hut/66081" target="_blank">📅 18:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66080">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
سخنگوی ارتش اسرائیل:
احتمالا طی ساعات آینده ایران به خاک ما حمله کند
@News_Hut</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/news_hut/66080" target="_blank">📅 17:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66079">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5H5jA9VDGtBNEsbtswQ6loF8cm1jElc6yhSqvyTH18y-LKo3c8rD-uFUMHQS7ugpbpdsYB43YZABoq9KmLi1CJ-jI1IHEkY565tflngS6bkZc5HvCnL9ZuoNzrf04s3nsUwzTqvKk5UdlJk7-SpV86fBFbDrOOUXFlKs8P2J60F3akBFhlkLsThJ2ZttQwQYciZ6TFPFrbAjJVsbOGuWE8XGuYxHICtPsBipDMPS4Ixm82PZfEjOcLrjvhD2t51dLSiqBglI1SeRsdUnfBIwcvDfH8rMTjzcOcnTyS13m7NgK9M8HNup3QO_tvT9lOZJ4GRpvll3h7bhtqMlnMj5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی کمیسیون امنیت ملی:
حتی اگه توافقم بخوایم بکنیم باید اسرائیل رو بزنیم تا ادب شه.
@News_Hut</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/news_hut/66079" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66078">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXE9j7TV7p3hR-vXlvNbHVhMe_IEZCgRwJ5Sa0Ex7qtPBsAJrAEF3RKBBsblp7q3mk-g9kht-9KKoFrzU4_ypZqn6n_KMdP_XEbM0gQcS7mVFo4yPKIHzaw__yomgrCvP7DVZv85xCCfxcckjMHKwKCJAzirXAJmfaQz3ECVWIMxVKlKNSzyv0aFr4d0RwaWKfYn7eKTsPp3uzs9H2WKBi_MhedndwDtVekawdBwsG49ty76SsMJVHuVDzdustCNtvrxjP9O7LLBRT1P6JoEMCwdUK2c7ldBapeHlbZdYT_u_oS4BAKEYNcXuD4Ufi7y5S8BDkmd9A7e4Ze6i4NHrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
مرندی عضو تیم مذاکره کننده:
فعلاً مذاکره دیگری در کار نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/news_hut/66078" target="_blank">📅 17:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66077">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e954c10201.mp4?token=Az7HmaS3V97Ujw9QVYxfld3t-Qk83bQQ-r3cczxjUtQbOvJwJujZD3ZoGREY_COHGU_5OEI-VUusBwF4NbekCWWs9XHXgV1fIeYiDrrdiNSAaN5FmeKcUwHZfyNiYTE2bzT26eGf-_ds6O_oXyLfe5jgcuaLPs0cZl4BF-ofoICjuyB71zCRzFBfgxNxw4mRuFgH7LVC9HOqOqVyYHjZ9PrMOeFekz18AMOJWpS8Ye2q-6ZWtByfC4bYRobZvbFvq3ElYgAD0_8ZrT74WkG_dOGeFjek-ZHjVPV7YUMpYetWq25dfwFtC_6JIP-6_BrI0naLX7DB4H8dlr8UqIloyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e954c10201.mp4?token=Az7HmaS3V97Ujw9QVYxfld3t-Qk83bQQ-r3cczxjUtQbOvJwJujZD3ZoGREY_COHGU_5OEI-VUusBwF4NbekCWWs9XHXgV1fIeYiDrrdiNSAaN5FmeKcUwHZfyNiYTE2bzT26eGf-_ds6O_oXyLfe5jgcuaLPs0cZl4BF-ofoICjuyB71zCRzFBfgxNxw4mRuFgH7LVC9HOqOqVyYHjZ9PrMOeFekz18AMOJWpS8Ye2q-6ZWtByfC4bYRobZvbFvq3ElYgAD0_8ZrT74WkG_dOGeFjek-ZHjVPV7YUMpYetWq25dfwFtC_6JIP-6_BrI0naLX7DB4H8dlr8UqIloyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت اعراب حاشیه خلیج‌فارس توی این جنگ
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/66077" target="_blank">📅 17:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66076">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بی‌بی همیشه دقیقه ۹۰ دست بکار می‌شه مثل ماجرای فخری‌زاده و برجام، باید ببینیم حملات امروز به ضاحیه ترور مقام بلند پایه مثل نعیم قاسم به همراه داشته یا نه! #hjAly‌</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/66076" target="_blank">📅 17:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66075">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بی‌بی همیشه دقیقه ۹۰ دست بکار می‌شه مثل ماجرای فخری‌زاده و برجام، باید ببینیم حملات امروز به ضاحیه ترور مقام بلند پایه مثل نعیم قاسم به همراه داشته یا نه!
#hjAly‌</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/66075" target="_blank">📅 16:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66074">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60a237733a.mp4?token=BU46FiS7NG0c89kpZ85fSJjj2M2JtrN7ZO99pCOydA0IIhTSmtcejf6jIgDs4ZRQh04SaW0GsWIZLxyD2lYAoZEoq83pHBNUA_VogVVbKHbu_mkcnS7IooIwwqTtpevWgqkk8hp0QMm1hfVmJxROmow6gqdTkCI7KUZC8fkOCj8I5ynylFxRWbhRviWFReU_Wax12EUitFjrXqXjFpUexj4blJYWsRzKzgNwTnTKm-fcxfzh9i2kUWoVGzTQdE4JP8Ww-6xCeF3Tbahz5Afob_BF6hNnZw4O6b6lQj3Fz3OagA1IXfEJYmVUn34k2uqy2BBzpzRLMbQ_nYqf8lZzeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60a237733a.mp4?token=BU46FiS7NG0c89kpZ85fSJjj2M2JtrN7ZO99pCOydA0IIhTSmtcejf6jIgDs4ZRQh04SaW0GsWIZLxyD2lYAoZEoq83pHBNUA_VogVVbKHbu_mkcnS7IooIwwqTtpevWgqkk8hp0QMm1hfVmJxROmow6gqdTkCI7KUZC8fkOCj8I5ynylFxRWbhRviWFReU_Wax12EUitFjrXqXjFpUexj4blJYWsRzKzgNwTnTKm-fcxfzh9i2kUWoVGzTQdE4JP8Ww-6xCeF3Tbahz5Afob_BF6hNnZw4O6b6lQj3Fz3OagA1IXfEJYmVUn34k2uqy2BBzpzRLMbQ_nYqf8lZzeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسایی نماینده مجلس:
اگه میخواید این تجمعات شبانه تموم بشه باید انتقام خون نائب امام زمان رو بگیریم و این انتقام تنها با محو کردن اسرائیل از کره زمین به دست خواهد آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/66074" target="_blank">📅 16:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66073">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyM8K7LK7oveGtSlA-TQaZE8QRPZRpcwLv2s8Bs2p91Ei038XMAVbYvvQFa_6isgTYMrrEi2cB4ejLNNzC7m3u337F7RhJihR1JVBlWKC9vL358nCwrOX3V_u5ARt_U0tVRaoDq5E6InhN6WKZJyJsTM6sTfaoute4z-5fADBjHIEHmpsmMcjfHbxdkXgZIBkojdrYA7AGVRzd-wI-uoUYHBblpamMtigiOEoGNXXr96-wKvS9hm7OkDnnkDGXIw9FiIjO183vAhWH1V5FjBp2CTE-Ms8PQPIW3XZORSYC-3G1yFGXmkyHIFHTJpF9ABDM5ByJCcgaa-espLq7iw5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قالیباف:
تجاوز صهیونیست‌ها به ضاحیه باردیگر نشان داد آمریکا یا اراده‌ای برای اجرای تعهدات خود ندارد یا توان آن را. با چراغ سبز نشان دادن به رژیم نمی‌توانید امتیاز بگیرید. بازی پلیس بد و پلیس خوب قدیمی شده است.
اگر اراده و توان اجرای تعهدات خود را ندارید، سخن گفتن از ادامه مسیر ممکن نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/66073" target="_blank">📅 16:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66072">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل از مقامات آمریکایی و اسرائیلی:
ارتش اسرائیل،فرماندهی مرکزی ایالات متحده (سنتکام)را اندکی پیش از حمله به بیروت مطلع کرده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/66072" target="_blank">📅 16:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66070">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa7b240724.mp4?token=XufJCEUxH12hbA6lpnk0Ll7dAeCxEuAbmDzILRpBSJaxn3WT93oH7Efz5oLgkLbR56-ol2rOCwXloKK91PBZy77ezRfcCA7xitQz7RpLnc-zgAzb3DxxBte3s1BHcQ5-ebGVhGqTus9nWhtuwKN_pIvSolQYJdPMycn2uwKeskSPuhtAq6r4fHapV9UnfdOqYW0ds-ZzL43ine7JgV6DqPFCM-27c0Sb2S1B7C6IuLBaUhxdD6lNUVPlfp35gqKjYkl8kiHnS4XmdmZhLDVDrN6Z0q4EwXr_n4bo76emJFr2yAmVcLR-ED727hb4BGw0-WwCAwOf3EQl4wxjT-fr9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa7b240724.mp4?token=XufJCEUxH12hbA6lpnk0Ll7dAeCxEuAbmDzILRpBSJaxn3WT93oH7Efz5oLgkLbR56-ol2rOCwXloKK91PBZy77ezRfcCA7xitQz7RpLnc-zgAzb3DxxBte3s1BHcQ5-ebGVhGqTus9nWhtuwKN_pIvSolQYJdPMycn2uwKeskSPuhtAq6r4fHapV9UnfdOqYW0ds-ZzL43ine7JgV6DqPFCM-27c0Sb2S1B7C6IuLBaUhxdD6lNUVPlfp35gqKjYkl8kiHnS4XmdmZhLDVDrN6Z0q4EwXr_n4bo76emJFr2yAmVcLR-ED727hb4BGw0-WwCAwOf3EQl4wxjT-fr9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هم اکنون واکنش نتانیاهو به توافق
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66070" target="_blank">📅 15:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66069">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">طبق گزارشات رسانه های لبنانی حداقل یک نفر کشته و چهار نفر در طی حمله هوایی اسرائیل به ضاحیه بیروت زخمی شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66069" target="_blank">📅 15:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66068">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">Live Volleyball</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66068" target="_blank">📅 15:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66067">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d546d16a9c.mp4?token=U0SQg6Fy6-fv6T6Phkj2R87V6x9MTaI7f6JrIiPB2KMJLsMxLZl3s-TDSmnhJgfWAyl96-0CPoiSfTrJxACj_ph6cLSUbQRj-My3qBtsetcD1Yii_t41E710pF5eF5FzoHnCc6bjcAUXVQuyQtshpCr2GSqD-XKiHVblpv6dwikIvwRoneZ2upLWUSd_JBroLsEKlbrZfjjritCRd-AuAdgx0iCZGNXLtJ4lSVZQ06USHqTa1G6V5Xf4hX1WOtK_ElRnkDRDUXNxoHXzgeW1X5MBFBd5O7kN23hgQNHFSr9uEv90ERhnL-bI-AXtkDHryF7Eq7sIoN3JnAPbem6_XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d546d16a9c.mp4?token=U0SQg6Fy6-fv6T6Phkj2R87V6x9MTaI7f6JrIiPB2KMJLsMxLZl3s-TDSmnhJgfWAyl96-0CPoiSfTrJxACj_ph6cLSUbQRj-My3qBtsetcD1Yii_t41E710pF5eF5FzoHnCc6bjcAUXVQuyQtshpCr2GSqD-XKiHVblpv6dwikIvwRoneZ2upLWUSd_JBroLsEKlbrZfjjritCRd-AuAdgx0iCZGNXLtJ4lSVZQ06USHqTa1G6V5Xf4hX1WOtK_ElRnkDRDUXNxoHXzgeW1X5MBFBd5O7kN23hgQNHFSr9uEv90ERhnL-bI-AXtkDHryF7Eq7sIoN3JnAPbem6_XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: رسول خدا و همراهانش در جنگ لت و پار شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66067" target="_blank">📅 15:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66064">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea6b9063a8.mp4?token=nVtNhlJateqBmbPj7dPxDiCL2Htao0HVB7vEPRZtfCARnnCZsYANPabYhzSo4AoziEvYs91NwZlIJaNr7oL9A_xMrgTTOj8Yc2VFL_4-TDvBQpeSSN8oz5Ce-5hr5r7InBwTtEwxHFiukOEUvPQJAOBPpi8IJdgq68gSjf7JfStsc-KhOHB4TrzSqyElwQI_pxObQySYrf3h3YJpOqGqN2oHCZRkuoQpwTNaZq3Qo46eshVemTCUJ2o1gIHpiz-z_Hj5uItiQynVMyT_fZUNDj9GeVB8w_7P07kZkmwF4yifYGXbbIzJgzkWD4WAaVWE9zoRRxJEnRMbbEysEeTy3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea6b9063a8.mp4?token=nVtNhlJateqBmbPj7dPxDiCL2Htao0HVB7vEPRZtfCARnnCZsYANPabYhzSo4AoziEvYs91NwZlIJaNr7oL9A_xMrgTTOj8Yc2VFL_4-TDvBQpeSSN8oz5Ce-5hr5r7InBwTtEwxHFiukOEUvPQJAOBPpi8IJdgq68gSjf7JfStsc-KhOHB4TrzSqyElwQI_pxObQySYrf3h3YJpOqGqN2oHCZRkuoQpwTNaZq3Qo46eshVemTCUJ2o1gIHpiz-z_Hj5uItiQynVMyT_fZUNDj9GeVB8w_7P07kZkmwF4yifYGXbbIzJgzkWD4WAaVWE9zoRRxJEnRMbbEysEeTy3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای که ارتش اسرائیل از حمله به ساختمان حزب‌الله در ضاحیه بیروت منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66064" target="_blank">📅 14:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66063">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
کانال 12 اسرائیل به نقل از یک مقام امنیتی:
این بار، ما حتی پرتاب یک موشک از ایران به خاک اسرائیل را تحمل نخواهیم کرد.
اگر چنین اتفاقی بیفتد، اسرائیل آماده است تا یک حمله نظامی گسترده و خردکننده علیه زیرساخت‌های نظامی و اقتصادی ایران انجام دهد
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66063" target="_blank">📅 14:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66062">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
کانال ۱۲ اسرائیل:
هدف در حمله به ضاحیه جنوبی نعیم قاسم بوده است
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66062" target="_blank">📅 14:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66061">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دیشب تو بازی قطر سوئیس، یکی از هواداران(خانوم) شرتشو در اورده بود انداخته بود وسط زمین
⚽️
@fotbal_xc</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66061" target="_blank">📅 14:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66060">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31239b7a33.mp4?token=UQHk3uNCUvUgRvDOWxHvyFmnakkJ9lXHWQkHtfRFQYjNMrZmqgRy2rRXtkvMheJTTMO4BQ9yxOG3oJ_sANwNqPFqbuvccxNyhZt-91EhtSbMp1mgerzYiU2vtZvwItF1c2vkvwJXA08L5E2bEnJw3CsjOOCoOSZQ7NHHa-7d-mbcvuRlb38kPoJRjLlWn8sNHes5n_CyjFOGMrNFRruzqolCIfvn6Bv9BdES_ZKyDdwfAoIjgXbweorZRgRIvXP7tGGhDBo6JtVVWEd_Ub_uckUvvN7LSaQrTw07T-A0VJMP3HzNrYu2X74F4jYQQgaKUNqt7krfE3dHzJdU9q6zkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31239b7a33.mp4?token=UQHk3uNCUvUgRvDOWxHvyFmnakkJ9lXHWQkHtfRFQYjNMrZmqgRy2rRXtkvMheJTTMO4BQ9yxOG3oJ_sANwNqPFqbuvccxNyhZt-91EhtSbMp1mgerzYiU2vtZvwItF1c2vkvwJXA08L5E2bEnJw3CsjOOCoOSZQ7NHHa-7d-mbcvuRlb38kPoJRjLlWn8sNHes5n_CyjFOGMrNFRruzqolCIfvn6Bv9BdES_ZKyDdwfAoIjgXbweorZRgRIvXP7tGGhDBo6JtVVWEd_Ub_uckUvvN7LSaQrTw07T-A0VJMP3HzNrYu2X74F4jYQQgaKUNqt7krfE3dHzJdU9q6zkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چندساعت قبل، اصابت پهباد حزب‌الله به منطقه ای در شمال اسرائیل.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66060" target="_blank">📅 14:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66059">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
حمله سنگین اسراییل به بیروت  @News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66059" target="_blank">📅 14:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66058">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07e4fa5e8a.mp4?token=jL0BwH4Ddwim3R9DTk2re9reBe0EyvSLJsBB7dLcgSsYD3szu8xmjQFa5prfIKmGxFLdXJwYU80xQPVRDfQpfUyFLGTOPyjfhDOGeGh7oa0L27k1e8_QN9nWWxbFT1GxBqo_TBPv6fY2AvTQdTZ_FcQ41daU7VnIWodtZzEzlk576vcALjgFVOuVoH1M0xMd0rFYr6rlyv7h2rDFZP_mY59ioFyaHk5PJi3ysgrdr8tOpSY7argLQwM60CoG7obieQGfF5-3A9rVBsPlWXyR1CFxdj-EiNZmnL0r_flbAvw-hTIrygGB72fKFX-_19wWI1Ko8jQfbq_cnfyBCeeaDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07e4fa5e8a.mp4?token=jL0BwH4Ddwim3R9DTk2re9reBe0EyvSLJsBB7dLcgSsYD3szu8xmjQFa5prfIKmGxFLdXJwYU80xQPVRDfQpfUyFLGTOPyjfhDOGeGh7oa0L27k1e8_QN9nWWxbFT1GxBqo_TBPv6fY2AvTQdTZ_FcQ41daU7VnIWodtZzEzlk576vcALjgFVOuVoH1M0xMd0rFYr6rlyv7h2rDFZP_mY59ioFyaHk5PJi3ysgrdr8tOpSY7argLQwM60CoG7obieQGfF5-3A9rVBsPlWXyR1CFxdj-EiNZmnL0r_flbAvw-hTIrygGB72fKFX-_19wWI1Ko8jQfbq_cnfyBCeeaDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله سنگین اسراییل به بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66058" target="_blank">📅 14:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66057">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
ارتش اسرائیل:
حزب‌الله با نقض آتش‌بس، سه موشک به سمت شهرهای شمالی اسرائیل شلیک کرد و ما در پاسخ به بیروت حمله کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66057" target="_blank">📅 14:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66056">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByvB7J-leWaci0SuRs49SrrYIqH627pZjuixEuLY_-KTduQFOzscwSQZlmsUXgtGpKnrvO6a9Xw0FFRoYvxPk2WwWcUBMF0Z8zwIs44Z94r4YtLqYdltVcbHrJb3V4jVajqmjQKJSniWeP2uN9Llx_tmfUWc7hDgDkbVbqK2lPLlkazMk9HxjLGq0-m82K3zVCNp48dBDWxEyN2b2ej9IKLn4MJUUqxTAExgpBXj2Vs89i_cC2DWOdL68AUnC79XOPWeYCUtkhv_0Qb3bdQotjQUGYCLdMwKgThUchfu69w90pc7jtA7d6j9rlOIRZKIq9ZmcRvfEQc0zG_v1J-_RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بیانیه نتانیاهو و کاتس:
ارتش اسرائیل اهدافی متعلق به سازمان تروریستی حزب‌الله در ضاحیه جنوبی را هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66056" target="_blank">📅 14:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66054">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3UGAzIxB5VH57Ca91n2LMOen03ZxRhAfgt4TtrIdD8bHOMudYEsHp94789XHQ9jNoFCkOyR7xIkLjU8Wy5L8FPgo30JZadD70emoVmFdUyjiyplK0sfKD65KKBQyGIoU_EZ_oUQ-vCDZVfQRR42h_0TPDB_sZQmQr9jOQEjHd7RoSay0b1OpDLXIdnBGYzDR_7ZmNe8vTPl4TbNLVXg9cHlZ7q414HUSh06e902doOleXf_m7fYWJQUsBi4vnffdjmXk033TrDjui_Xda_hl4MhhJW998lPVC64M2qm64_Novt-NY-BK_ahu8hIRtiSz_CixPKA4HysF9ZtaDcUDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش ها ازحملات اسرائیل به ضاحیه بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66054" target="_blank">📅 14:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66053">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0119b4719.mp4?token=g9Xgy10Jt85Yb-_tCOYcuRw7Doqm3Flf_PHdqG3JSe9QsMb6B7DkrXT7NzzqGKd0kVaRowG-pB3A9pLqo2l0CLuW0C8vjZ8fRXQ2uvZcqG4oJGLculJut34Z0HnTwr9cJv_pO86qSAw5e4CDUjFOxPMyoT79hkt1V5P4hkZTmscPzZqs02laxflTHmefnYKbfB6iHk2TmSi16F6Nx_t2F-f35vMVQyZ-CaILzGOG5pXEnmYis3kk8ItNx9R7Vb9HdDtEu4BoTMRf-JWPJOJWzZQJ-5anSHaWJmH7SLFVKlRBE0o_u_AMpds8xty2qwlFXrxQIGeRfnbOr12NFUUGnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0119b4719.mp4?token=g9Xgy10Jt85Yb-_tCOYcuRw7Doqm3Flf_PHdqG3JSe9QsMb6B7DkrXT7NzzqGKd0kVaRowG-pB3A9pLqo2l0CLuW0C8vjZ8fRXQ2uvZcqG4oJGLculJut34Z0HnTwr9cJv_pO86qSAw5e4CDUjFOxPMyoT79hkt1V5P4hkZTmscPzZqs02laxflTHmefnYKbfB6iHk2TmSi16F6Nx_t2F-f35vMVQyZ-CaILzGOG5pXEnmYis3kk8ItNx9R7Vb9HdDtEu4BoTMRf-JWPJOJWzZQJ-5anSHaWJmH7SLFVKlRBE0o_u_AMpds8xty2qwlFXrxQIGeRfnbOr12NFUUGnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
▶️
تصاویری ترسناک از لحظه بمباران یک نمایندگی خودرو در تهران
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66053" target="_blank">📅 13:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66052">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17f35bf38.mp4?token=eYyRBur4vVejowzv5ZvSHkvIwJo1BoOXVZKLF0miiFdV3f0afYkgs4_Am2_rM6G3C_IgZp3lIdsBBTug4hSYmbTxqRfcLG_tj6-ChMg_ZYY3N7pIaMb8316NkkLKd1nlen1X2kElKLLxg_vBQnEA8nAg8YWB_eaMdRBoFMuEyHm4MNO5A9Ft8qV4eYDnYUm0t-iUhdPgasjk7jNzTeFNtPTHCiQ88LE6UECnA7KT9Z9q1-QUub-wPvOCQFM1RgF_wbBp2rsIe2T44n1CDYOZZIvEw8qGi5cyPGOjOqa7EQYCd6kS7EymJbgUClOGDwfFbDppRxdML7-GIg_qH9v5Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17f35bf38.mp4?token=eYyRBur4vVejowzv5ZvSHkvIwJo1BoOXVZKLF0miiFdV3f0afYkgs4_Am2_rM6G3C_IgZp3lIdsBBTug4hSYmbTxqRfcLG_tj6-ChMg_ZYY3N7pIaMb8316NkkLKd1nlen1X2kElKLLxg_vBQnEA8nAg8YWB_eaMdRBoFMuEyHm4MNO5A9Ft8qV4eYDnYUm0t-iUhdPgasjk7jNzTeFNtPTHCiQ88LE6UECnA7KT9Z9q1-QUub-wPvOCQFM1RgF_wbBp2rsIe2T44n1CDYOZZIvEw8qGi5cyPGOjOqa7EQYCd6kS7EymJbgUClOGDwfFbDppRxdML7-GIg_qH9v5Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تو برزیل یه دختر 21 ساله رفته بانجی جامپینگ یادشون رفته براش طناب ببندن و انداختنش دختره هم فوت شده
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66052" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66051">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66051" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66051" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66050">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngrUYdhk21sZf3FflWgS_LvwBfNASWr0QNTqZ4j8wzdwN8bm3bDIn-xbQz2RrwI5ZAeRlgbasB_IKTy3AST1ZBUcT1JJAlErvqgNZIeUAhHx0VSlda-dLf4ERFuCsNMXehsSl7r0dhIZTIsgYUXGtYzG8Y6Ntjp0_bGdl3-SmglxHV6VXZezgaU2tI5hIDsqQ_pH3TRSqXw1Edc_cKF_YosjyqlMn1wpXtHcA63e8BuKMWj8pnu9WZlTcChb7lbo63wZUOoQpETtEEHf0fxXDP2gpwABAY0Ie1tNbbEA5vz9nwCiAzQYHIXGV-HJ2m57R0fKQI6jg7yR7LkSnXAktA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66050" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66049">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db36249809.mp4?token=uOVYpJSoELrII_ozC8fNUYAxBOVsshc9HHWXYj6yrZ_butjv41zIta5Kgfj4pnVBK1MIACWy2rvOrwXL15j4uKwjhClfRtKsnWkUO8kxjsOG-7Cqf8oZpHfgqvN9N93uF7Z8TqHFjv_n4bVDfjCqJZmvfEYMyQVtTruE7W6kTBWTGY5pbH4GgR8IsRAnbQ-DZlJvL5pQwf637sYHQC5v7XTsqPoT33YEwkvdvqIbVnpYaD53dwLF5UeWoAzhQFCwrIJUgPpPwQNse14JMdKM9J8Xd-2NBGezUTrpjDKyuSPEweLWq5OZmSCQwtWsiYsxojnuMnO68G_yXKAGofyuGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db36249809.mp4?token=uOVYpJSoELrII_ozC8fNUYAxBOVsshc9HHWXYj6yrZ_butjv41zIta5Kgfj4pnVBK1MIACWy2rvOrwXL15j4uKwjhClfRtKsnWkUO8kxjsOG-7Cqf8oZpHfgqvN9N93uF7Z8TqHFjv_n4bVDfjCqJZmvfEYMyQVtTruE7W6kTBWTGY5pbH4GgR8IsRAnbQ-DZlJvL5pQwf637sYHQC5v7XTsqPoT33YEwkvdvqIbVnpYaD53dwLF5UeWoAzhQFCwrIJUgPpPwQNse14JMdKM9J8Xd-2NBGezUTrpjDKyuSPEweLWq5OZmSCQwtWsiYsxojnuMnO68G_yXKAGofyuGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۱۵ سال پیش زنده‌یاد مانوک خدابخشیان جنگ میان جمهوری اسلامی و آمریکا رو اینجوری پیش بینی کرده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66049" target="_blank">📅 12:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66048">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
امتحانات نهایی پایه‌های یازدهم و دوازدهم به دلیل مراسم تشییع علی خامنه ای، یک هفته به تعویق افتاد.
پایه یازدهم: شروع از ۲۰ تیر ۱۴۰۵
پایه دوازدهم: شروع از ۲۱ تیر ۱۴۰۵
جدول زمان‌بندی دقیق به‌زودی اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66048" target="_blank">📅 12:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66047">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e28745391f.mp4?token=YwxXNRiKPzqKhmiT6JOT2PmKK3yPyZOXsRoMpI7mW4j7mWgqOg41TVtUog1IGykAfRq77THMiBaEq2_sbx4PyAgJe6fDbN6PBFfNj721nRYvvoY4Oa3utC972Z98RvI8FdTveRJ1OnzHiTTrwSZfT3I1lYnNxShuS1RCs3v4sH82yaVI7F6g1SPHtbNNAXN3onKEgaqyYsHlhyEm4R11IjPkotcsXnScpoCV5r76nVyJckUx07YbuNQst2-bnAVclzDvLiAJgJf7l8Wyw2HOz9nZUy_4A82P_dsCCorTTXZwdsqAnGvtjI5ASh19ErT4eTy-sr1IRNeu_1ABqt725Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e28745391f.mp4?token=YwxXNRiKPzqKhmiT6JOT2PmKK3yPyZOXsRoMpI7mW4j7mWgqOg41TVtUog1IGykAfRq77THMiBaEq2_sbx4PyAgJe6fDbN6PBFfNj721nRYvvoY4Oa3utC972Z98RvI8FdTveRJ1OnzHiTTrwSZfT3I1lYnNxShuS1RCs3v4sH82yaVI7F6g1SPHtbNNAXN3onKEgaqyYsHlhyEm4R11IjPkotcsXnScpoCV5r76nVyJckUx07YbuNQst2-bnAVclzDvLiAJgJf7l8Wyw2HOz9nZUy_4A82P_dsCCorTTXZwdsqAnGvtjI5ASh19ErT4eTy-sr1IRNeu_1ABqt725Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
صحبت‌های حمید رسایی علیه مذاکرات نمایندگان جمهوری اسلامی با آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66047" target="_blank">📅 11:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66046">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
ثابتی دیشب تو تجمعات بسیجیا: عراقچی خائنه و من طرح استیضاح رو به مجلس ارائه میدم
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66046" target="_blank">📅 11:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66045">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GeNp1UCi-EiqDfG6LhxyBt4gTC4JJkR9y6izCoNeEm-lCwHDBuKu1FyCa4YLS7hqyz8FXie8oxdOUUmc_ymiiyjl5Pvw3G2jlP8Q6BrAWX4SBxjEYA8ytSR4RIPUlZITWe1qlcz9qnnneP0krsNDvN4S0YECyDATwd3S5E9BVLEWqn4wfvHJHV7hC9weX41l-oNZx9OTbNSFKFchHIy6RRzcrrXhOT6czyJnc8dcueKHHKAWmjWtxgo5zQyLwikAP2LZ9qBjE6kXlKeLnWaavw16IqEn_8e_csqeAJXKvyK6GvFXNyQz0hPxo2enBWViSDJ_HBp5lEjsqKju3kGILg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچی والا مام خوبیم
بابامو کشتن
زنمو کشتن
بچمو کشتن
«ولی رفتم باهاشون توافق کردم.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66045" target="_blank">📅 10:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66044">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/375671acc0.mp4?token=MNvHg7oCOXdgPlArhkBdRVQP6uc2kWR4MtGiVhlcFongeIjI86OrSeJrLk2zR2epnDQkUxXcrjF6n_d27iMzOaj93n4Gc2d3KOnSPzR-RRaEbytsLO7kbcmh3MPVQYloXyQXbTN5igpvTr_M2foIyvWKzD_VW4qHaO3nB-LfXhKFHu2i9DcMIyANml-Xu_ix6HOZdplAenn_XJNXnXZ4gXNGCBR1svCYoi6I9qItH7QA8IEzI1r6A08wmnYFjDJv2uHVrxGGZrqzZ10iyPlGAhG_YSEBT8U_LHdzBckCPf_ZEK-GDxzvHKOoYHAAiprUQ8W7Gz6UFhOjVmNj8SV0bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/375671acc0.mp4?token=MNvHg7oCOXdgPlArhkBdRVQP6uc2kWR4MtGiVhlcFongeIjI86OrSeJrLk2zR2epnDQkUxXcrjF6n_d27iMzOaj93n4Gc2d3KOnSPzR-RRaEbytsLO7kbcmh3MPVQYloXyQXbTN5igpvTr_M2foIyvWKzD_VW4qHaO3nB-LfXhKFHu2i9DcMIyANml-Xu_ix6HOZdplAenn_XJNXnXZ4gXNGCBR1svCYoi6I9qItH7QA8IEzI1r6A08wmnYFjDJv2uHVrxGGZrqzZ10iyPlGAhG_YSEBT8U_LHdzBckCPf_ZEK-GDxzvHKOoYHAAiprUQ8W7Gz6UFhOjVmNj8SV0bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ١ دقیقه رو گوش بدید
زنده یاد مانوک خدابخشیان میگه :
رژیم اگر توافق رو بپذیره به جاکشی می افته !
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66044" target="_blank">📅 10:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66043">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsgPiQqjtZj3S62EcpBvsmSxA8npS4Rj9RBJNx2Y2A4gRntMdaz_0Q6wirjlp8t1NM5frp3Q94PFI_C8LCgLOFmOf7qvgZVI_6TThQ008iD1nYpMEQY76ht_rVtLgtjM_wIshTFoEZxa_BQUSVO-VzLMBPUPbVqU5ivMPGyZEGtMHs1WrHTYSQx99XD2mkcDLCt2XUhf9NpjJbUswT8-1ZxvQ8moCFjeLT_B9GIJAdN4VSEQ_ClX8PNWBkP_qWSSr6r7YWoLDpe5uyRgmD-9fOM7haty41YQIMctKykGOpJHsfG_3Fbzd27hdMq4tAaiu6chpt49nkLbCvbNy6HTmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط عباس میتونه جوری توافق کنه که:
جمهوری اسلامی ناراضی باشه
مخالف جمهوری اسلامی ناراضی باشه
اسرائیلی‌ها ناراضی باشن
آمریکایی‌ها ناراضی باشن
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66043" target="_blank">📅 09:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66042">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/518512af42.mp4?token=deRmKgarxBqdyXixQ9x6QXgOZq_krR6Eg0dgewnujGUWp9OqpjcaroNVr7a19_sDrKt2tPOeAsqVKsL0ZiyeRSieU7hqH_DgRvNbG8nCer_YnUHB3SxlJ7vygNend1grBKlFcqtBvgaerx4NfUYgP51Slf7wLGfWdZhQBWUfQ-6h7t9U7joQwfShw46E1_pdrqorrSmnlMdpvRgPu-234kGtJJRnY-B2ikpWdBLu55tUAmWfc6rZztLWbkcfgoxuwopuUlTZSxyYV30lJpZ5iMb4xxzK_Z4P-MN1EpI0_w8Hq1m52XKGRZklg3Z_OcYBe0BVQgyRJPsBUGfHmRmk-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/518512af42.mp4?token=deRmKgarxBqdyXixQ9x6QXgOZq_krR6Eg0dgewnujGUWp9OqpjcaroNVr7a19_sDrKt2tPOeAsqVKsL0ZiyeRSieU7hqH_DgRvNbG8nCer_YnUHB3SxlJ7vygNend1grBKlFcqtBvgaerx4NfUYgP51Slf7wLGfWdZhQBWUfQ-6h7t9U7joQwfShw46E1_pdrqorrSmnlMdpvRgPu-234kGtJJRnY-B2ikpWdBLu55tUAmWfc6rZztLWbkcfgoxuwopuUlTZSxyYV30lJpZ5iMb4xxzK_Z4P-MN1EpI0_w8Hq1m52XKGRZklg3Z_OcYBe0BVQgyRJPsBUGfHmRmk-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه آخوند آوردن صداوسیما داره میگه به پیر به پیغمبر اماما همشون با دشمناشون صلح کردن شما هم شل کنید دیگه.
«
واقعا بی شرف تر از آخوند هیچ جای دنیا پیدا نمیشه»
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66042" target="_blank">📅 09:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66041">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66041" target="_blank">📅 01:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66040">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UuEQlWNq-SXNBecLCO6GBTS2ZPNtuHdo4l1B8PoJf_MuWvxtBYxBsYySBrnv2uVJkRyJihAfkTziUuupCidzf-6fAoJ0aS20dWgoZC9CR6C0zJkFu4FIvnxowUImwOSqw2bPNyjtPA9GJYzdrdoMMa6TE5_3_s9kI2Gxswfys7iUy0E-vsZkeJqpE1q1c8sZ-v2MFo5mmO_ZJI4R1d5zv2nOpZ_Xdtkzwda4v4G7-yu4MPRBE8-UUzAdB8tE55NyPLZR0G8QlDoXMTv1NFwxY-85ygzw9quvLdHpfLOYG_HEiCvj7mW-NGIgBK0W7QA6t2x9PL774ZKmVbDyxwEtDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/66040" target="_blank">📅 01:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66039">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoeKF-1ASyjiXx2pRZ-DnEGjPEgSpS1lRvQenEGro5fVMqXCYBmq8rha2uX9XzMKnJfuFXiUqD0JuNsMVB870jamyuObwjLeK32VfFAFVhPu2DUORvAQK7paV2ZWOwPeHJ2uVdl_LdV4Oc8vjvqEPOqMyiWdlPz6X36y_fTqcPQRdgAvJPU4S9OSA0mMJ_e83wa85qK6z3xNKaXyqcJDm8jUZKXmcrbzyYDZY2A0ZEFQvof5ZWblRiA5wjsDbd16T4urZSPpvpilfTJy9NGIyqppSQdvfkd8aBNg2MULy4UurEe2BiOlHC3Wt9CjGXU989I1keJJgijf3fT7YfhZ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
دریافت مدرک رسمی «دیپلم تا دکتری» فقط در ۱۰ روز!
✅
قانونی، قابل استعلام، کاملاً غیرحضوری
✅
مناسب مهاجرت، استخدام، ارتقاء شغلی و ادامه تحصیل
✅
ترجمه رسمی و تأیید توسط تمامی نهادها
☎️
مشاوره تخصصی و رایگان
:
https://t.me/irantahsilat_chat
📺
عضویت در کانال
:
https://t.me/+1I9Ex4YFtcZkOTY0
https://t.me/+1I9Ex4YFtcZkOTY0</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66039" target="_blank">📅 01:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66038">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d1d99919.mp4?token=UKynp_fqx8FsXAUz5h0568nJ5k3Z9vdpjYfxyOaMgA5yC0fmimIYWNXJ0xfYTLyCl8s1Wqr0y28VBY39Dn_ovVb3US8BPlaoDlWLScLlvOT1loplq0khOxwbEmdmSbMC64Bgh-k4wmekzp5yqfZGMkPsnif9HAMFRt_uMSH9RF1zMCG3Y6Uv1ZCaSpu9YXIi9AjLHXkwMkj01jsj9TzX9342SUv8kKNfQB58mL2APvGVzm_bW_-d9qcYfYAHYU9QV7D9Lh2KRSfOV6V4IaHr8PVRw-DFXvHLUvZ4bIG1GY6wKzBIjLpYncDyv9HgpG2GniLt7Laqbz4celzlYtrvzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d1d99919.mp4?token=UKynp_fqx8FsXAUz5h0568nJ5k3Z9vdpjYfxyOaMgA5yC0fmimIYWNXJ0xfYTLyCl8s1Wqr0y28VBY39Dn_ovVb3US8BPlaoDlWLScLlvOT1loplq0khOxwbEmdmSbMC64Bgh-k4wmekzp5yqfZGMkPsnif9HAMFRt_uMSH9RF1zMCG3Y6Uv1ZCaSpu9YXIi9AjLHXkwMkj01jsj9TzX9342SUv8kKNfQB58mL2APvGVzm_bW_-d9qcYfYAHYU9QV7D9Lh2KRSfOV6V4IaHr8PVRw-DFXvHLUvZ4bIG1GY6wKzBIjLpYncDyv9HgpG2GniLt7Laqbz4celzlYtrvzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
شعارهای معترضین به مذاکرات با آمریکا
اگر چیزی امضا شه، مسعود باید کشته شه
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/66038" target="_blank">📅 00:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66037">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
⭕️
شعارهایی که در تجمعات امشب حامیان حکومت سر داده شد:
۱_ تا باقر کفن نشود، این وطن وطن نشود.
۲_ مرگ بر سه لاشی، قالی مسعود عراقچی.
۳_ این توافق خونیه، باقر خودش کونیه.
۴_ خایه بخور با سینی، عباس بچه قینی.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/66037" target="_blank">📅 00:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66036">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZow31F7gCnPn9CxO9ic0uOyF1kEPyEOeG8e2RJsoSyxDiGurjdIla80IhRQ5aUzy0LAcsqSfHjmPwIuwM3GAnhnpJPy-CvcPUaqiOeA8IdOawygjwN3OjCl3qIWFhnGgwtOQpbJ6TuYL6OfdQ23W6FJI9u6jmXvpUbFgd1xVHmZugAaNb4ZJud5_dt63AsQdmb0hYUNPkMAvIc9fzb_MgVXOdjjdb_oPGLbTgAS5bu7VIdrZUgxxmtZSMtKPqHsf1RvdaCHNEmTvGiIz9Z_XKCn1tIN1jynvK4JcmxGT8EiB_t4DOAtE6CCxXSAOo5LIcr-X373rbVcr8kNvZK7og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ و پیت هگست در موکب هیئت محبان امام صادق (ع) کاخ سفید:
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/66036" target="_blank">📅 00:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66035">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQLLHhZUQlPtI0cgMlfJPGx33FKi1b9LYZ9Ao36kYVsVQlpMAqqNx_51DvmbFu4N4qC0IHPlSdAunV0VbKlHtp3eU7DsztRYlXexx6_Fz92ky2nUq8lgOpw9-YqNe9qFPR-fkdbcNuhmM1l0H_wkWd4rkmEVdUFowjraBbVLdR2LOJwNZuTuVJOEohnkBYO9r2F9D3r4FaFsWVdeITgkBcq1emsUvbUvmLwemOq4uDaUv4mNW-PX1k1fWYYZKnyLfN-Opn62LJbmNxoWiuPqgbMSoEAivGQzif3jrqpgaZ7abkfrFtE5BqT8LS6YGxQB5VDR4STzOJ9tT9wCFDIA3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
توهین و کنایه بسیجی‌ها به آقا مژتبی
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/66035" target="_blank">📅 23:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66034">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
نبویان :
امریکا اومده به اینا گفته 300 میلیارد دلار بودجه بازسازی مملکت رو از عربستان و امارات میگیریم تامین میکنیم که خب مشخصه نمیده
اگه آمریکا بعداً بگه ما از عربستان خواستیم پول بده ولی نداد، شما می‌خواید چیکار کنید؟
«وقتی توی متن نوشته شده هزینه‌ها باید با توافق دو طرف انجام بشه، یعنی آمریکا هم باید درباره محل خرج شدن پول نظر بده. حالا اگه آمریکا بگه این پول نباید فلان جا خرج بشه چون ممکنه به دست سپاه برسه، اون وقت می‌خواید چیکار کنید؟
من بهتون قول میدم نه پولی واقعاً وارد کشور میشه و نه اختیار کامل دارید که خودتون تصمیم بگیرید این پول‌ها کجا خرج بشن
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/66034" target="_blank">📅 23:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66033">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxjXgnGFhZrrTotQGrrb2sSmei__lTz5kxxOHFX0JKGL5xQPawrlsc9QJF9Lj94WfC6LzYj1khtZSy0SIzDuU0vryZTTaLIv-XdeVn2HBws6KKOFP00CVDkf2TPZrhHUU7s6Q2s1-yJjeyBip1FwTAAr7eWbygUjkqQa0pAQ3Kl6WYa3CqN1iQdmhO3G07XhwKK8KtFKc31h76P-_4JJ-gqxnRHhCnkRIUDtwbk9ClNM7O9oi_Eu6xKJz1nvdhsCy3UsKr2SekRb9D9w5lykv8sMGwEbS76xmbztLv2b9mLwfd1CnpNP-9_BP1gTcwH4_0evOEwsBkTol9STdoyx0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز دفنت نکردن فردا هم قراره با قاتلانت توافق نامه رو امضا کنن
😂
...
«چقد تو مظلومی»
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/66033" target="_blank">📅 23:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66032">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‼️
ثابتی نماینده مجلس:  طبق اطلاعاتی که به دستم رسیده توافق احتمالی بدتر از برجام است. نه احتمال جنگ را از بین میبرد و نه گشایش اقتصادی دارد.  @News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/66032" target="_blank">📅 23:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66031">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/077634d539.mp4?token=vVRNa2v8v3Gg766yawPIbT45ATE8gZGK-iSotCdynb5Asc2Zk40F1wy-HqZ_WuFXJU3TaOdvsJq1N63c5TCdpX3RUFbvqkRw-nTMMLU5gNL3YPLvNmaEgjoC46kXYzbhNuY_Jac_jHsFHY1AUDpinhD4IOOxZcTawv9XuHpqsWha2rUQaFmzUmnKZ7jkfD3RBf3tUTsrdSqYo0yBH3wG3fCPhzbm3nTUC9U4PTbR-z_3cL8Mre8djYWfSEZ3kBjOBH-nbLV4D-Lzv3e_r9Nd0HXQ6BeFK3m5iBCLu3T-aF6wkJd_j54JLQLvrww5E1Em5TjhSU6g5PHbGByBQvN9aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/077634d539.mp4?token=vVRNa2v8v3Gg766yawPIbT45ATE8gZGK-iSotCdynb5Asc2Zk40F1wy-HqZ_WuFXJU3TaOdvsJq1N63c5TCdpX3RUFbvqkRw-nTMMLU5gNL3YPLvNmaEgjoC46kXYzbhNuY_Jac_jHsFHY1AUDpinhD4IOOxZcTawv9XuHpqsWha2rUQaFmzUmnKZ7jkfD3RBf3tUTsrdSqYo0yBH3wG3fCPhzbm3nTUC9U4PTbR-z_3cL8Mre8djYWfSEZ3kBjOBH-nbLV4D-Lzv3e_r9Nd0HXQ6BeFK3m5iBCLu3T-aF6wkJd_j54JLQLvrww5E1Em5TjhSU6g5PHbGByBQvN9aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طرفداران رژیم دارن شعار مرگ بر سازشگر رو سر میدن
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/66031" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66030">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9383ea7d9.mp4?token=QdOjKngEYuOIUUeM_fspHg03G3RF2KicYvbh9ZUnzcs5WiILwTCztPyHgKaxb36fgH_WYqZygUrbBmlpBSt9VTs9CnhPHhi0XBhy3WYYE6YFI5kg7jmaqYh6bonXVrbwIU2g09w2jLISpjamo-hgYgOc_TLC_-ke7eXsYr515INX_flz14eSgiusJ5WfPTCI12RJ-8CTS9t1Pi5UykEUqvSmshO7d0QL1xIV4gpjN5lBojKBcPl37_tOAkmysY-iJ9FVbFvcZayQANMag9Kfg4CWBrKFfi8qJRXdwGigZgrSXTyebwV_2ZzvbPKubopg9KVOPVNJj2pNHMHu2MHS-wr-SWgYaw5y1Lq-umt37Sf-Nk2c6mlIeo_bTX01wKSZRuA-EYIH7DwANmQLRR7VxGNfat9zF7AeolIoamXEjeMYE7Vx1BFkepXvibHC_4JEw25SQgvHhIib3-Unrjk0a7L0tSqBvsYCIEB53JLluyfRH6kX7FEIOWFDCJ9KvD4N-afB3t08AyyLmvNohjPeq2ogqVKULsjS0sS78VJGHTL3srC6dfv83DmUKzaUKJPYNuAXmtUmEg_r6NkQdHHTrRmlh7i5ICVvCyyLqlcSrD5L5iWUuZhAV_0qrYmJvbkycixk035gSequ7Q1Y3gagS0-LqEzeKjMjN-qUCiOFVvk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9383ea7d9.mp4?token=QdOjKngEYuOIUUeM_fspHg03G3RF2KicYvbh9ZUnzcs5WiILwTCztPyHgKaxb36fgH_WYqZygUrbBmlpBSt9VTs9CnhPHhi0XBhy3WYYE6YFI5kg7jmaqYh6bonXVrbwIU2g09w2jLISpjamo-hgYgOc_TLC_-ke7eXsYr515INX_flz14eSgiusJ5WfPTCI12RJ-8CTS9t1Pi5UykEUqvSmshO7d0QL1xIV4gpjN5lBojKBcPl37_tOAkmysY-iJ9FVbFvcZayQANMag9Kfg4CWBrKFfi8qJRXdwGigZgrSXTyebwV_2ZzvbPKubopg9KVOPVNJj2pNHMHu2MHS-wr-SWgYaw5y1Lq-umt37Sf-Nk2c6mlIeo_bTX01wKSZRuA-EYIH7DwANmQLRR7VxGNfat9zF7AeolIoamXEjeMYE7Vx1BFkepXvibHC_4JEw25SQgvHhIib3-Unrjk0a7L0tSqBvsYCIEB53JLluyfRH6kX7FEIOWFDCJ9KvD4N-afB3t08AyyLmvNohjPeq2ogqVKULsjS0sS78VJGHTL3srC6dfv83DmUKzaUKJPYNuAXmtUmEg_r6NkQdHHTrRmlh7i5ICVvCyyLqlcSrD5L5iWUuZhAV_0qrYmJvbkycixk035gSequ7Q1Y3gagS0-LqEzeKjMjN-qUCiOFVvk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
نبویان: من خیلی ناراحتم این چیزی نبود که آقا گفت. پیش‌نویس توافق بازتاب خواسته‌های آمریکا است
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/66030" target="_blank">📅 22:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66029">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/722ec8c49a.mp4?token=Q6SJzv0mrSdNWusS3HzCceXagXayD_HjZivTNuujObiJ4GpttKNP9Iww_7Dm5Nno7ZFOVoPEcrKQZIc7UruqTglxq6mIS7Gn70tp02fNhIz6aybxh9Vi63dSPppDCsRHS0p5t75duFl6ZZ9zIzoHWVbvrhLaaQ5VMqvDW9PtqKkDCpRJoTeiRs48h13LdxGNPXVTBiDREw0VY6nlWBMdJpZFJ_5lb14skxDxwYv8gCXrKKmMj3SpzFU5Dc_wczzDK4xKrvT7KbLDKT6lQFGNkZDIYnbIrr25xdqsvyPYAReDisOHR5GjKtrnMOf05tf8jdnEY156xKhuegLgB863fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/722ec8c49a.mp4?token=Q6SJzv0mrSdNWusS3HzCceXagXayD_HjZivTNuujObiJ4GpttKNP9Iww_7Dm5Nno7ZFOVoPEcrKQZIc7UruqTglxq6mIS7Gn70tp02fNhIz6aybxh9Vi63dSPppDCsRHS0p5t75duFl6ZZ9zIzoHWVbvrhLaaQ5VMqvDW9PtqKkDCpRJoTeiRs48h13LdxGNPXVTBiDREw0VY6nlWBMdJpZFJ_5lb14skxDxwYv8gCXrKKmMj3SpzFU5Dc_wczzDK4xKrvT7KbLDKT6lQFGNkZDIYnbIrr25xdqsvyPYAReDisOHR5GjKtrnMOf05tf8jdnEY156xKhuegLgB863fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازگشایی تنگه‌ی هرمز که قبل جنگ باز بود الان شده‌ی آرزوی ترامپ، آدم می‌مونه چی بگه، دهن تحلیلگری که بگه آخوند تسلیم شد رو باید گِل گرفت، می‌دونیم که این تفاهمه و توافق نیست و توافق اصلی در طی دو ماه آینده مورد بحث قرار می گیره ولی همین تفاهم هم فقط و فقط به بقای جمهوری اسلامی کمک می‌کنه نه تضعیفش دقیقا به مانند برجام.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/66029" target="_blank">📅 22:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66028">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lsc467aUeOUgHDEGmV9JavDvh4kXu7B-yTEHZvk2yCCK_aFTTw29Py5nKI1_RxbNS2rtJ_paQkh5AOX159NSCl_to8_YeKyuMxwdlf78VTmyAPatbj473qmrIW5gvXvgJ58P_q7yoaWspAZ80zYmCoOsX7B9GctDNZ2_eryziXur1ZC1g0hkJZBMckv0IPo9bChZSJ94O5iXkO_Uya5YzWBfKp3wFtub1TXRbNHi-br8LRp_829tIYh0C5FEiviNCF2yGxzQMlzrWv3WYrzjAxb9I4T-2vuaolipArgohNfwGTyMuyB4oxGRr4e0RQLx7yytFOnlEWT08TbOLDq7xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فراخوان اعتراضی نمایندگان مجلس علیه مذاکرات و توافق
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66028" target="_blank">📅 22:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66027">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
رادان: هر فردی که در تجمعات شبانه برعلیه تصمیمات حکومت حرفی بزند یا شعاری دهد به عنوان تفرقه افکن با او برخورد خواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66027" target="_blank">📅 21:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66026">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3933369d.mp4?token=UGjD0JPPjGeHZkPVkbx3uFJo3CtywMVzRqjzP2on2IYqaZDRbo6LkM8OdrkxiCbFwOFLHFzsQEJVsqNNWNkVIqR0a-Snr58HQeUaa5EU8JpH-W_rQk3-v1XmaKwJv6f3FLoNIJxHCQqZ4bNP8gyiq9YON56Xm7jAphqfvRZIfOataiWiEMpgeam2MgKNIGKFcHhTmJcG5bC7SVRvNTSAd_Zg2a5ssVWvvhsurvYbSVp_LgrXRTXhLJY-d3ZDYftwX-DcPgDaQjW1w6O2jDS8GK4kJwnOucL_bzGrbierh4-KjlGDt0AoyKd17LF-VBAQPynIT4uoV_ZHeUFzyD6eag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3933369d.mp4?token=UGjD0JPPjGeHZkPVkbx3uFJo3CtywMVzRqjzP2on2IYqaZDRbo6LkM8OdrkxiCbFwOFLHFzsQEJVsqNNWNkVIqR0a-Snr58HQeUaa5EU8JpH-W_rQk3-v1XmaKwJv6f3FLoNIJxHCQqZ4bNP8gyiq9YON56Xm7jAphqfvRZIfOataiWiEMpgeam2MgKNIGKFcHhTmJcG5bC7SVRvNTSAd_Zg2a5ssVWvvhsurvYbSVp_LgrXRTXhLJY-d3ZDYftwX-DcPgDaQjW1w6O2jDS8GK4kJwnOucL_bzGrbierh4-KjlGDt0AoyKd17LF-VBAQPynIT4uoV_ZHeUFzyD6eag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
در تجمعات شبانه:
عراقچی حیا کن
امریکارو رها کن
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66026" target="_blank">📅 21:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66025">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‼️
⭕️
🚬
🚬
فرهنگستان زبان فارسی: از این به بعد بجای کلمه هدفون باید بگید گوشینه
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66025" target="_blank">📅 21:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66024">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVIUow26mfejFtK_-_8Vujb58Jj5hlJp6afUCqeEchPm02mywL-3fUH52vxkW0ww4yUzYpMXWz3ufPsU26ANyKtPJ43Ws26hUt3mv3tBILuEHGnIA8s-FG3qnJBZP3DVXTYqQIXjugL5wkCIaUDZqIsz_PHvQVFkKm_lc7XiXsJ4xqZzUI0JGFDvw-bHt-M9MYImp5F0UTuw_7G_Q6Z1EQ11JjLP0RIrR8DkDISJynPhhERqBgw6ULkg6Csusv7lI75lR9eZRhMXFp-Ti5oo5f5Q8nxqPkU2BGZzJVUi9UhwvzT9Tzv9DEA2W2PzPvZVlX66Of3bZZrhQXdfutRMoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
⚠️
سردبیر مشرق: رهبری در کدام پیام ده شرط را اعلام کردند؟
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66024" target="_blank">📅 21:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66021">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71f300a74.mp4?token=tG1ZJl72bwLWJFGtraR76R4QP5BS4P4uRHQWr9SEvb76LEyFh4RNiuFEeWirfHuyFqGgHL7YJR6aZDPjuFCr0qxiRyzFvgr-CauSDNtsPGbVStvZa4cDg0HTTcbY0LHxhmVLBDVADP0928aQsuM23lObp061gjArK7NWPNkwWlnf18KWh3aeH3JQ8LvsalYI6pvCJ8ovSq0sP8CtFVWY7dXm9xHZ2t0tVkD6OFzHyUtd-oNOxKdaDA-t6m1coDiAJV2f50LOZ-cp6nX_bBuxpeR2Dp0wQC29a02KA24nP09p-xSMFP1WhPFiwJe2vrfavuJCbHUznWJiAOpqIuxUKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71f300a74.mp4?token=tG1ZJl72bwLWJFGtraR76R4QP5BS4P4uRHQWr9SEvb76LEyFh4RNiuFEeWirfHuyFqGgHL7YJR6aZDPjuFCr0qxiRyzFvgr-CauSDNtsPGbVStvZa4cDg0HTTcbY0LHxhmVLBDVADP0928aQsuM23lObp061gjArK7NWPNkwWlnf18KWh3aeH3JQ8LvsalYI6pvCJ8ovSq0sP8CtFVWY7dXm9xHZ2t0tVkD6OFzHyUtd-oNOxKdaDA-t6m1coDiAJV2f50LOZ-cp6nX_bBuxpeR2Dp0wQC29a02KA24nP09p-xSMFP1WhPFiwJe2vrfavuJCbHUznWJiAOpqIuxUKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عربا با ماشینایی که تو ایران شده هرکدوم۱۵/۱۰میلیارد و شده حسرت برا مردم از این کارا میکنن واسه سرگرمی...
💔
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66021" target="_blank">📅 21:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66020">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">هات نیوز | HotNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/news_hut/66020" target="_blank">📅 20:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66019">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری؛ ترامپ: فردا توافق با ایران امضا می‌شود  توافق باراک حسین اوباما با ایران، برجام، مسیری آسان، زیبا و هموار به سوی سلاح هسته‌ای بود، که ایران شش سال پیش به آن دست می‌یافت و مدت‌ها پیش از این از آن استفاده می‌کرد. توافق من با ایران دقیقاً برعکس…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66019" target="_blank">📅 20:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66018">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATsjtSbq488oLc2QPHUF15bcd4H-MaKy69AfgNfPhWRK-srHjEhOBzQb4dv7lQMaEWvTWSV7XVwY50aT5cKGCdv8Mt9ZSSuR0wo-hEgYwQreqenbLxphNE5rFO1w6tLQkP5zOSqyTvmQY2m9JrgOmg3gxdaCHZZpC5OV3ziUvmQlPX2P49QYciAnrnfym_vQ4xgbISzm7Di6P8p89AWI1CwWnCkRJpppHJ4dyyQiI2YOJrFfBMOgSlH_4is6heDiEWhzMkHRVVtBGD2KnoCYE_JnPARVSRCzYZClFxbe0NmcmBL2cBXFRyUWNw0jpz154Ba97Fk7QE8TX5it0YlGxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری
؛ ترامپ: فردا توافق با ایران امضا می‌شود
توافق باراک حسین اوباما با ایران، برجام، مسیری آسان، زیبا و هموار به سوی سلاح هسته‌ای بود، که ایران شش سال پیش به آن دست می‌یافت و مدت‌ها پیش از این از آن استفاده می‌کرد.
توافق من با ایران دقیقاً برعکس است، دیواری برای نداشتن سلاح هسته‌ای! در واقع، آنها دیگر سلاح هسته‌ای نمی‌خواهند و نخواهند داشت، چه از طریق خرید، توسعه یا هر نوع دیگری از تدارکات. قرار است این توافق فردا امضا شود و بلافاصله پس از امضای آن، تنگه هرمز به روی همه باز خواهد بود. رابطه ما با ایران بسیار متفاوت و بهتر از روابط دولت‌های قبلی است. برخلاف صدها میلیارد دلار پرداخت اوباما به آنها، از جمله ۱.۷ میلیارد دلار پول نقد سبز و سرد، هیچ پولی رد و بدل نخواهد شد. در زمان مناسب، وقتی همه چیز آرام است، ما به لطف بمب‌افکن‌های زیبای B-2 و خلبانان درخشان آنها، وارد عمل می‌شویم و گرد و غبار هسته‌ای را که در اعماق کوه‌های گرانیتی قدرتمند و غرق شده دفن شده است، جمع‌آوری و نابود می‌کنیم، چه در ایران و چه در ایالات متحده.  ما مشتاقانه منتظر همکاری با ایران و کل خاورمیانه در آینده‌ای طولانی هستیم. امیدواریم که این روند به سرعت، به راحتی و به راحتی پیش برود. اگر این اتفاق نیفتد، ما یک جایگزین نهایی داریم که امیدواریم دیگر هرگز مورد استفاده قرار نگیرد!
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66018" target="_blank">📅 20:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66017">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b00aed34f.mp4?token=O_x48gOrXxO-AeHGaHXszKNvtEVv-EROF9edXOV6BrWtCU3GgF7ae7E2vh1PFLsSvf0VPhq90XTNx8UEwr5lnYjemkLUVSLsHFt4G78_IHN-pJglR5oYJjP7lDDWyzzOAEfrWmYF5EIwuniLGUkhKkKsgamPOz1WSl6lNLhU0n0AjAsMlakt-pStrCiiwtaDRe2XNxpEcKuYF3kIWwaiX8_48Twre0FI58Ds8fVYueUThazpwL118qvA8Br2K1KBfuqb8h2Ea6ah6bhUaJjpKhYJxCGMENuaJq78lgzy7SkIPWxdTbdDU8CfKB8XQ2eCS9aWMw0tdJdVAOrSqQOLxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b00aed34f.mp4?token=O_x48gOrXxO-AeHGaHXszKNvtEVv-EROF9edXOV6BrWtCU3GgF7ae7E2vh1PFLsSvf0VPhq90XTNx8UEwr5lnYjemkLUVSLsHFt4G78_IHN-pJglR5oYJjP7lDDWyzzOAEfrWmYF5EIwuniLGUkhKkKsgamPOz1WSl6lNLhU0n0AjAsMlakt-pStrCiiwtaDRe2XNxpEcKuYF3kIWwaiX8_48Twre0FI58Ds8fVYueUThazpwL118qvA8Br2K1KBfuqb8h2Ea6ah6bhUaJjpKhYJxCGMENuaJq78lgzy7SkIPWxdTbdDU8CfKB8XQ2eCS9aWMw0tdJdVAOrSqQOLxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
⭕️
تجمع هواداران جمهوری اسلامی مقابل وزارت امور خارجه: مرگ بر عراقچی بیشرف نفوذی!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66017" target="_blank">📅 20:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66014">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe4e2f8eb4.mp4?token=SbVz1obcJhHqtljLRUOnplPjdB89tWDVISyE1y0VjyGL7Ya8MedDXBO0fuiJteGEUNmlZtoX69MYU1INK_0G6NI11ab-scTJxEJuhcgyU9pIUV21hQO0VmiEi1Dw8oBYXPqtBxyQwiwL6D7zhvEOa4zzKNeWPW-4alffBdeh38o1I6PY3fSkafXA7hd2lglRTIHnQfWap80awca4K3avo5_l1xNLOgYPzCzdyzwEqcu6SZ6aFajVFLVFIhHIQe9_le-or-assgKCgzhFz8BhjCEhbnhLma-_NxmDf6yhZ65CpcRMhWe4gThvBPuN_jsAkNUnfNHaKeCmuk_EJuerzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe4e2f8eb4.mp4?token=SbVz1obcJhHqtljLRUOnplPjdB89tWDVISyE1y0VjyGL7Ya8MedDXBO0fuiJteGEUNmlZtoX69MYU1INK_0G6NI11ab-scTJxEJuhcgyU9pIUV21hQO0VmiEi1Dw8oBYXPqtBxyQwiwL6D7zhvEOa4zzKNeWPW-4alffBdeh38o1I6PY3fSkafXA7hd2lglRTIHnQfWap80awca4K3avo5_l1xNLOgYPzCzdyzwEqcu6SZ6aFajVFLVFIhHIQe9_le-or-assgKCgzhFz8BhjCEhbnhLma-_NxmDf6yhZ65CpcRMhWe4gThvBPuN_jsAkNUnfNHaKeCmuk_EJuerzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی وایرال شده از کیوماسا، گوریل باغ‌وحش ژاپن بعد از دعوا با دوس‌دخترش
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66014" target="_blank">📅 19:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66013">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwXKRGOI6lGpKI9MhLY6j5X6CKYIWKvnO-Nmi-bY80QGLKL1oazeeQauCcb1JhsbkznH-bP_dH_x3xU8lwxLSS0I0Uh4a1NKDxmIcmSW9vpOvQ7Cf0O_J7GevjEw7_VOZKeT5lSmhMhBiIOiiylI5WnaCrVBHztMj6Z5Uc2f_oHGe_uwSffWT5qQW1PtqbXfO-VS0S9vQHn2B2RlZ3tyMnaLKJbr-Ti_u9T9T_Hy3ccgtJ42e33hocxCpgXMcCe6zi8HxuPJ8TLvI8L_nvbKA3SYMhAX6Rc0MlejoljzrhzFqGD7B2GCtVndUbynMjjVSLkOdxJnbdDGXV7ZBzu7hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید به نقل از یک مقام آمریکایی:
پرزیدنت ترامپ روز سه‌شنبه در حاشیه اجلاس گروه هفت، دیدارهای دوجانبه جداگانه‌ای با رهبران قطر، امارات و مصر خواهد داشت. نتانیاهو در این نشست شرکت نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66013" target="_blank">📅 19:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66012">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHNBpNNtRRjCrKPqM2xh8zQZsyILD__MHUY-k1fikMn3jkYzbldCJIzTR8Ox8aWiphVq0OdVWpH2hciOjh_VPRVgPsBTjW4N0v0Agqh26Uh2CUozOX-QAzx-AbzERws88k72ObVRVx8oZPhtbBjmbQMqpYoMooaucDTDvWsb2X11SYOV7m9qSp7GlJN1PsobewtXG4yITA4Oz6HaTTh3ltAhtA1jmvZCtlJpmW5kqPyp_H2a-VTE_pYF7Sg4kC9N0aTSf4wOTNlGASqEdp-WwHGq98GLWCZdhsf0_PvNyZWpzBgN3ohzYI_lxXD6KrfqpuaksMJuJl3_-RCue94IYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تجمع اعتراضی مردم تبریز به دلیل توافق با قاتل خامنه ای
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66012" target="_blank">📅 18:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66011">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
#فوری
؛پاکستان:
توافق آمریکا و ایران فردا بصورت الکترونیکی امضا خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66011" target="_blank">📅 18:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66010">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBt-tOnNiz3bup3DI3NWRFN2u5g9ddAckR9g0ee5h_FTPZbFKQDbbrnPlT2kRpEuKv7m-hX8kof3qF-gGQBoEuvYYCl9ESl8G1cJWbNbKbsgsz2Uu1GJrYEnv_Zl-zm-LHOqj2A6iEOkHyN7QHu5hmUYJyvh8XFxrKYPFbSIks_fuGDksEeXNyJpuYyE2xPC6TLUVVaGuWHFLfk1SxdsTTayfWp3iV6wqt6thSPnkc-bEo0aTb8Clzg78kP-lc4GtrQm3GdXFA_bxM5ZQB5_hP3J-YE_COd-2DpBUW1DBdErtOrm5FP_l9hS63PwSpO-ZrNxRpAWSdFti6P30S2o_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ توییت شهباز شریف نخست وزیر پاکستان درباره احتمال توافق تا ۲۴ ساعت آینده را در صفحه خود بازنشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66010" target="_blank">📅 17:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66006">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kJtEgZiVYaQa7CNp3A5e5UMe1Df17hqsvMLa4XLOh-EFVFjf8U_cW8BjqqGA-yuJvJtamaAz_QmXVOojTtKykYoy3nOrKsdfbthAf3Uq_E-QEg0ajxifoGVQ75oazB9Yg2Wwfqr6-COz-tVyLpTpaDnV8T27QxpoGnGM90iKMVZ59zBGkIVy0zQN1JUrxNSVimtjTl7AfOfp9nNojYAk6-4zv-Jq4HEPeBKHQRXIANMEtkdH50JmKKSHZtGVEE7d9NnO7HZy81cslgRbM_TJgl0B_8PyFnqVZ1ueEMhLGgQDtqIgUhGKmTflRe1U12OIh9VTAu4OsIvJyp6vwD4tPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EY6c1BaJiQYHv4VRVZx0YWcVvcdWdT8DcJUIjwM7xDIMS5XZUbSEHOUbRQ7pmZpj7xf2r_HKvKbqNxoLzTWzfqBNuj0g6MCY3pki4a3qb8FTfXRsR10BDeLUe-4atyD6Tzz9Rk-hhJ6ZstCWnspatA2CxXZST56UY_vcnP7EZ619VBEeqqgcKXrqZ-mORmRDLGFEtkxNEz5XdoSquQTc0tjXXAtEk_P2d_G2knxoDP5wSaVqaCSt80yHcZkesoCxaCZcbTML6Kag1jfsFAahJxqP9fFfXLMhvU2SzkMxATsyNG02KnqhoLxLBdRewmpZ37bVm5orNNCTIQW5D4MMMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zwc27b-nDRUFxkg1vR2VZANHljaEMcDZOyHhwbpE3fRWNTXKioyh-HM8IzGn6YGOZPbd9sQUU9Y9UsWC_gF7Yty3ZHpPERNuQn4gVF7PlKhC8dxmpVoqqVVDUIPwip4c6ov7tqT48NyZLoqt2Zh5GTQEUZ8ukmMDLLGVRU_15Hx2OowvIV6Cg2R0vYFGoVpyG9e4Uizpei1GRQ93bbyM9nMX-YLPBBp6O5gsBzxDH4VNzk8ZWYtJmk_fKh1Gcwca5bM6t4WwueyLHa-zdynviwTYyKdAAT7R_SffSuVofpTu9G_j9XwvN3N5ikec_rsXDUK9-Ce-rVbb26bHgGL1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tsCBfSK0cNn3GQPjKxgzo4c57lPh1YOR7zyPBpdkVNTcjwv716nseRAoj2joUpqyj-Wx5eL3COjZ3rEAiZXuMl-8uySnvKYGknIhUIPaqDvXAIdV7cX7dOj19nQaguvG9xMta9zMwVnur5_YWDLUCSjlBB10umc18v8Brp2JJGnP9PIrNNSry5nsBX1nvQy6kv4uPrIIHHFjLmgBPFMgLSNpM2g4FO7_R_kG5o4OJQaN_9vwgSk9N6ZAMR3W_AJNqYxSlRqhSFbkGAg6jKBiMYIoPihx7VDHlsb08n2vbb6iMF-cmn-mEBvoRFKBVHVY4ZEjtoP42dG2LNv_y1DrPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
جت‌های جنگنده نیروی دریایی ایالات متحده و هواپیماهای فرماندهی و کنترل آماده می‌شوند تا همزمان با عبور ناو هواپیمابر آبراهام لینکلن (CVN 72) از دریای عرب، از روی آن بلند شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66006" target="_blank">📅 17:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66003">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2UioC6Q0x4gluf03rFa5CX-7vL0KzoX8OOuE8BROpxjxemzvOKNLKg3fXlXoPfn_gJBKk9zVKfp_jKEZhg-Hd5JCsCC2qxSIYYeh3zZMBDkE3YKvXRi9PG-B5FCEmylujHzu0VrwUhavDLCHR7XKd_CmKRO0DF7UG2tKP7jDmqU92iy_v6iOm52QdHIdvKfaUhv5nY4GX8ywRWhJE2M1l6CoWTPZWJT8Uadkoq5IJWI9346WPScgqsboYsvuuiBjmmmbC8s8JOAqdB_3qC4kwe8GfcWBx57F3hbuwmkMCn8s6qTsdaGsUjCvmH1HT7IS-fqftslD_A_nrCeNDNxqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعدادی از نمایندگان مجلس به همراه قشر تندرو امشب جلوی وزارت خارجه تجمع اعتراضی برگزار میکنن و به روند مذاکرات اعتراض میکنن‌
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66003" target="_blank">📅 17:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66002">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZ8TO5UFlkOd53B4TMcUuDsT-U2ep7uAqwDMS1fy1SH9VG5xYvBpDnugLeSMlK9pSGWU7ItGGdagAr5J1HQsvf4C9a0Km4E1E8Sp3nxiin6SG-HGZ_N1UrzGt3Pod1OLZ085XiGsjQrJy2SI-0vTgrr1e_HG1eAXq5_wyJNsKcVWhuUECe7AecZNcbwqVE-sCFx5pFela_RUaqjPoMNnXG2KshssH9R7ne-Ob3rdywfAMT7spGoKTEUUkLVUbDXPzWx9lyqwcqY2zkCt7JZ13P-42OiouCdhgRIiJeV-hoMa0FyQUoI3QOKitEGFHYKWC0DTm1lnjNZELGDRNKy0Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اواخر بهمن ماه پارسال، ترامپ مصاحبه شمخانی که گفته بود «اگه آمریکایی ها سر حرفاشون باشن میتونیم رابطه خوبی داشته باشیم» رو بازنشر کرد ولی هفته بعد کشتش ، حالا دیشب هم صحبت های عراقچی که گفته به «توافق نزدیکیم» رو بازنشر کرده
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66002" target="_blank">📅 16:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66001">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41b2c6552b.mp4?token=VsQ81d9ONve4C4H74aax0tKm8ABzztPvc5QAFNDfKQHGsR1C9HYhyw_sFU72-MpgoiwmcfhSyDB2IDa6rCr99x71HGxegc5cjKlkt0otGm5l9Lia-2AZMICentZ06LqvUgbSaBUATLGi-EiZyMDHQcHwLZMqgZukUe9m7pIC_pOY50PVEkiCDd-N1sBK5Ww-PdE-QLnKQ94Gxwh2MOff0xdXAoDwedw1zJchg_aBC1ZVeVnVKvZQQ6hCn_H1VbtKoSOx23oZNcm98VGFV1ooMUv-RalmY55K5chjko44aK7Qdrbulj4htMSFwVze_4EA51iLMp1rA76qeh66E5C-Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41b2c6552b.mp4?token=VsQ81d9ONve4C4H74aax0tKm8ABzztPvc5QAFNDfKQHGsR1C9HYhyw_sFU72-MpgoiwmcfhSyDB2IDa6rCr99x71HGxegc5cjKlkt0otGm5l9Lia-2AZMICentZ06LqvUgbSaBUATLGi-EiZyMDHQcHwLZMqgZukUe9m7pIC_pOY50PVEkiCDd-N1sBK5Ww-PdE-QLnKQ94Gxwh2MOff0xdXAoDwedw1zJchg_aBC1ZVeVnVKvZQQ6hCn_H1VbtKoSOx23oZNcm98VGFV1ooMUv-RalmY55K5chjko44aK7Qdrbulj4htMSFwVze_4EA51iLMp1rA76qeh66E5C-Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه هدف قرار گرفتن راکت انداز Tos-1A روسی توسط پرتابه FPV اوکراینی
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66001" target="_blank">📅 15:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66000">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ic1ZWqEX9BHDGEQZNL6jmANX0YNdf-RjLMUTUZC_OtOdXSzRpzu_hmmQAOtCCzEY2ghfWIiWjBOEMC5-rpSiFQprvHUp8RstJi55CQKG85lPiWTPCiYnJ3xFEH4PGB6r8BNtni8B9kVZ7gyvzm3eytxAQrmkUJfHFSplBs5Mcnc3pWdo7xNGLtXLB1WWg2wG9klkBLT3FC27goXG9BcZmiBn-X80W6FFc1UHZC7eK-TGSsXF8_G-nllpX0BlvM_9vQHfdpXC-dweUVsNCyReIzKhipAzdU_shBUwjCuyDoE6GIm6ErHNVnHaJWjTwa-9s8I2I7d75gNsiKdGfpKl5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقایقی قبل سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارشی از حادثه‌ای در ۶ مایل دریایی شرق عمان دریافت کرده است.
گزارش شده است که یک نفتکش توسط یک پرتابه ناشناخته در دماغه بندر مورد اصابت قرار گرفته است.
خدمه در سلامت هستند و هیچ گونه آسیب زیست‌محیطی گزارش نشده است. نفتکش در حال حرکت به سمت بندر بعدی خود است.
@News_Hut
﻿</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66000" target="_blank">📅 14:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65999">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
شهباز شریف:
من مطمئنم که توافق تاریخی بین واشنگتن و تهران، پایه و اساس صلح پایدار را بنا خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65999" target="_blank">📅 14:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65998">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
شهباز شریف:
مذاکرات فنی هفته آینده پس از امضای الکترونیکی توافق آمریکا و ایران برگزار می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65998" target="_blank">📅 14:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65997">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
شهباز شریف:
پاکستان در حال آماده شدن برای امضای الکترونیکی توافقنامه صلح آمریکا و ایران ظرف ۲۴ ساعت است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65997" target="_blank">📅 14:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65996">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر پاکستان:
ایالات متحده و ایران بر سر چارچوبی برای یک توافق صلح که به ماه‌ها درگیری در خاورمیانه پایان می‌دهد، به توافق رسیده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65996" target="_blank">📅 14:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65995">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوری
؛نخست وزیر پاکستان:
ما بیش از هر زمان دیگری به توافق صلح نزدیک شده‌ایم و احتمالاً ظرف ۲۴ ساعت آینده نهایی خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65995" target="_blank">📅 14:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65994">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">شهر عجیبیه! تریسام بروبچ دهه نودی  @sammfoott</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65994" target="_blank">📅 14:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65993">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
⭕️
مراسم خاکسپاری علی‌خامنه‌ای روز ۱۸ تیرماه در مشهد برگزار خواهد شد. از روزهای ۱۳ تا ۱۷ تیر هم مراسم‌هایی برای رهبر دوم جمهوری اسلامی در تهران و قم برگزار می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65993" target="_blank">📅 14:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65992">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
از امروز صبح خدمات الکترونیکی برخی بانک های کشور از جمله ،تجارت،ملی،صادرات و توسعه صادرات با اختلال مواجه شده است.
خبرگزاری فارس اعلام کرد برخی منابع از احتمال وقوع حمله سایبری خبر داده اند اماهنوز منابع رسمی این موضوع را تایید یا رد نکرده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65992" target="_blank">📅 13:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65989">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwYJKvGBJy1h-oqgKZZX5w2Y8M8eJb3w2cMkB_rhpL0gqLkq7zfr90M0cmng_qoWA8cnrNWXCDx9Qewm_5bGoSKyYVkXfd3Pd-KftFID6II60ET_JixY3Me8TmpMzeoQpKoPpcETyzrRgi2Nn_6nFe6RvX9sRF5wK4AQJkjYEec1zmx_6asa9GAX5iJLBQfu8naVB0d837VktHfyQSdEKhFDdnQRwC3BQuw2tN6d0Uy-PdXXo41y8GATaFePjMlEZ9ewltZ1q8FeJckRNzrJwizdr7Z0ZdyNGhbQvUr4iBw5ixOlUIW01n9Gl8eTDXS5kkGHmx1QposUBS6QppVMQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
جنوب لبنان؛ارتش اسرائیل پرچم این کشور رو روی تپه العویدات و کنار سازه یا حسین نصب کرده
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65989" target="_blank">📅 13:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65988">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_isxliuHbjGo5qkEF_hdNBiz9Su1flnWZD0jHuKm-eoPCjuJiDkUgRTQOqYorxx_YP3rwlXByNQN0Kuuif61dn0sg3RyY6jh4Gz9ZTC5qGnVsAs9o5wfBGiZD0RmyVASTEEwj32jB7eMPAmjDvUPFRGaK8lubMAJ9u1jAh8oeRFgaxTbyx62smFnxLwMSlSBQXJN3xHDTke9C5fnWQ0_C2AN49-v1JPCsBYQL1Z1CLhHsNVD72mxgdo1Qc1dl4a9ehfTi2HT6YoVE6fA9vie2sz1S5yhJ7fQXBr3-Z2iDRQVH3uGscRKyNp-dOb3zXWutDaAU_C8u9kqDNrSe81zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ایران تو هفته‌های اخیر حسابی دسترسی به انبارهای اورانیوم غنی‌شده رو سخت‌تر کرده
- طبق گفته چند منبع اطلاعاتی آمریکا؛
- ایران بعضی از تونل‌ها رو عمداً ریزش داده و ورودی‌هاشون رو با مواد منفجره مین‌گذاری کرده
به گفته این منابع؛
- الان رسیدن به این انبارها نسبت به یک ماه پیش خیلی سخت‌تر، خطرناک‌تر و زمان‌برتر شده -
CNN
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65988" target="_blank">📅 12:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65987">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85b34abe01.mp4?token=D5OmqUYaLx9_YeSFMhgIK206hLqLhKlTHP59nzVcelnYwXu2oXNcI_Cu8mO4zSeR_O72qbL4O0lKDQok_GQSWe_wzXSjtY3w8Fh2zWJ9KcrS0IkpRzCLcLtqD8jGSfCR8iBRZUGU5di0fONhP9D2T7YPNe-47Yx8y3MRP4h_W9Wj1qyIfU0UNAuDh_uhoEnhnf5KPXRBzc8drrdDXJZ4OaPbh3JZiSz9nbOi69OE6_K8ZcCQmQGLhdrlobwHHLB_XRLnKBucpHcSSSc2NWJbvYc8xMRsQy_Gs-XHLpm4-elyOmOFYwl4VCY5OQL5Rgop9tX7uV7WCxhNdqKYB-7xXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85b34abe01.mp4?token=D5OmqUYaLx9_YeSFMhgIK206hLqLhKlTHP59nzVcelnYwXu2oXNcI_Cu8mO4zSeR_O72qbL4O0lKDQok_GQSWe_wzXSjtY3w8Fh2zWJ9KcrS0IkpRzCLcLtqD8jGSfCR8iBRZUGU5di0fONhP9D2T7YPNe-47Yx8y3MRP4h_W9Wj1qyIfU0UNAuDh_uhoEnhnf5KPXRBzc8drrdDXJZ4OaPbh3JZiSz9nbOi69OE6_K8ZcCQmQGLhdrlobwHHLB_XRLnKBucpHcSSSc2NWJbvYc8xMRsQy_Gs-XHLpm4-elyOmOFYwl4VCY5OQL5Rgop9tX7uV7WCxhNdqKYB-7xXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انفجار شدید تانکر حامل سوخت در مکزیک
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65987" target="_blank">📅 12:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65986">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a45e16c46.mp4?token=JvZuBpucNs58jEtSg0oUCKZEhmiqrvdgWmn_i2X1FE2E_Q75mjLFB3KA6pbEjw9wsq32LrdGutMTipqpubXu_LYRHSFzPL3TmtFqsMk6PgumACGlGnUH7jl4fGl-x9kGlxKbVjuknbgCkjEOyYrwQUU6w3e7Y2kFWMn0zL_h0vCwIFxoQDtnHtndmgRu-Wi8qmrLUYKrW5RbF1uVglxjXuismYXNOTsrKIKXR3MGv5o-LiDTZ77Kc1bACuKGaTaL8hLdCayv2SnwX2V08srWZDIua3-zpsYS7DBgX5_YLUm3mLvkHynetY7h83u5qoRSNQmlAlqvuj2P--acoC0oEjRZkwKX7B6SqEKVTidQOiYyKDHrQd7ZyXXNHbG788nwEe1x4PM7WbyNLpmISsey3FX9dX1ow9Ui5IUa_g9NUomi5fudc8pvdIblGQo91tV49cWM-zpJ91NEo29roLGG2kfyUiUuiWO7JNMmLqDr9YA2T4-nEbvq4066R3A0VT9DsS89MLHAd2-HZ1RGNm1ASAGxRp2GNbl9gDXKqkOLLaMwrpTNr6Ay1NPA5k8oMSN7aQehtw7BEq2EU9WSFxmW1xgXPJ_1eJ9BCio9ZCQoA0N1we8ehtkBPPq7j_rh8gLq4Rc3YDaBEpn5GbrvqrBpCgL_CL_KTHDH6LgFyOLHNh0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a45e16c46.mp4?token=JvZuBpucNs58jEtSg0oUCKZEhmiqrvdgWmn_i2X1FE2E_Q75mjLFB3KA6pbEjw9wsq32LrdGutMTipqpubXu_LYRHSFzPL3TmtFqsMk6PgumACGlGnUH7jl4fGl-x9kGlxKbVjuknbgCkjEOyYrwQUU6w3e7Y2kFWMn0zL_h0vCwIFxoQDtnHtndmgRu-Wi8qmrLUYKrW5RbF1uVglxjXuismYXNOTsrKIKXR3MGv5o-LiDTZ77Kc1bACuKGaTaL8hLdCayv2SnwX2V08srWZDIua3-zpsYS7DBgX5_YLUm3mLvkHynetY7h83u5qoRSNQmlAlqvuj2P--acoC0oEjRZkwKX7B6SqEKVTidQOiYyKDHrQd7ZyXXNHbG788nwEe1x4PM7WbyNLpmISsey3FX9dX1ow9Ui5IUa_g9NUomi5fudc8pvdIblGQo91tV49cWM-zpJ91NEo29roLGG2kfyUiUuiWO7JNMmLqDr9YA2T4-nEbvq4066R3A0VT9DsS89MLHAd2-HZ1RGNm1ASAGxRp2GNbl9gDXKqkOLLaMwrpTNr6Ay1NPA5k8oMSN7aQehtw7BEq2EU9WSFxmW1xgXPJ_1eJ9BCio9ZCQoA0N1we8ehtkBPPq7j_rh8gLq4Rc3YDaBEpn5GbrvqrBpCgL_CL_KTHDH6LgFyOLHNh0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
خبرگزاری فرانسه:
روز جمعه، از کشف یک جسد در صندوق‌عقب خودرویی در مجاورت محل تمرینات تیم ملی فوتبال ایران در جریان مسابقات جام جهانی ۲۰۲۶ خبر داد. بر اساس این گزارش، بازرسان و کارشناسان پزشکی قانونی مکزیک در حال بررسی جسدی هستند که در یک خودروی متوقف‌شده در پارکینگ بیرونی استادیوم «کالینته» در شهر تیخوانا پیدا شده است؛ استادیومی که به عنوان اردوی تمرینی تیم ملی فوتبال ایران در این دوره از رقابت‌ها استفاده می‌شود. این حادثه تکان‌دهنده تنها یک روز پس از افتتاحیه و آغاز رسمی مسابقات جام جهانی ۲۰۲۶ رخ داده و پلیس محلی هنوز جزئیات بیشتری درباره هویت مقتول یا انگیزه احتمالی این جنایت منتشر نکرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65986" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65985">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1ac66f6c0.mp4?token=j7by50TnnVWSSGTd3g75Re6nqTCFubgIHRQmMT41gHPwrEgIq_Tt9TqDosVEYkygdaOdyYfcOgcyT-6tk4zi7mxbwfJIZwjEVUVzEs5mc20KT1gMdLGmT3y_DIsaODtaDFOa0S9A64aRwhPYuzvdfUeVCJSvZdieDXPUr6LtfEasAqlBNfGKXGzOFm-OLorV70r-jx_dAs4-n6YVmtTbMT25KVlZe2fZ1Y4U3sxnp-g-_KGBYLQIMJj4H3w5kfQPFg7PBX67go66IFFT3i_munoETOviVcWs_0Zux5is5V_1Jthj-xl2knyzhSD9QzRgMQ_24696TeL_KnYUYcu0BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1ac66f6c0.mp4?token=j7by50TnnVWSSGTd3g75Re6nqTCFubgIHRQmMT41gHPwrEgIq_Tt9TqDosVEYkygdaOdyYfcOgcyT-6tk4zi7mxbwfJIZwjEVUVzEs5mc20KT1gMdLGmT3y_DIsaODtaDFOa0S9A64aRwhPYuzvdfUeVCJSvZdieDXPUr6LtfEasAqlBNfGKXGzOFm-OLorV70r-jx_dAs4-n6YVmtTbMT25KVlZe2fZ1Y4U3sxnp-g-_KGBYLQIMJj4H3w5kfQPFg7PBX67go66IFFT3i_munoETOviVcWs_0Zux5is5V_1Jthj-xl2knyzhSD9QzRgMQ_24696TeL_KnYUYcu0BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند تا پسر اهوازی وسط جنگ وقتی رفیقشون خواب بود این شاهکار رو خلق کردن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65985" target="_blank">📅 11:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65984">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11109e09bd.mp4?token=I4RyN4RMfaB75p9G5pNh0xAO_XCQ47yg_XsbhJJNha1M6FE4GbFkPgeX1Q6eYdXoUDg5dc-NGXImHk-Td8tj1X8xQv9l0B2zWAKsfkrkgg9t9hMu-TSRbbpPVRjNXzcCVvuwnFGJpzEAP7vhVU81k--ZDaLOGYZEpJsebTlOdh_ObvX3DyFv7c4lD0ZnO-YvVkJ7mQE40Z2myGiPsk3XufV2Z6OleMggFTBMkPOV_6IiV_z2z0SLsz7xPsnZqazJPCKaBefQk1OaEB98fYVl_mwRrwPT9o3zay6xiTfa3su3ollSyo-7cJVB28Tag0Ok4iVWVkWKsykiewHiyvjcDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11109e09bd.mp4?token=I4RyN4RMfaB75p9G5pNh0xAO_XCQ47yg_XsbhJJNha1M6FE4GbFkPgeX1Q6eYdXoUDg5dc-NGXImHk-Td8tj1X8xQv9l0B2zWAKsfkrkgg9t9hMu-TSRbbpPVRjNXzcCVvuwnFGJpzEAP7vhVU81k--ZDaLOGYZEpJsebTlOdh_ObvX3DyFv7c4lD0ZnO-YvVkJ7mQE40Z2myGiPsk3XufV2Z6OleMggFTBMkPOV_6IiV_z2z0SLsz7xPsnZqazJPCKaBefQk1OaEB98fYVl_mwRrwPT9o3zay6xiTfa3su3ollSyo-7cJVB28Tag0Ok4iVWVkWKsykiewHiyvjcDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ربات گدا در چین دیده شد
یک ربات انسان‌نما که از چندین روز بدون شارژ ماندن شکایت می‌کرد تا همدردی رهگذران را جلب کند، در شبکه‌های اجتماعی چین مشهور شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65984" target="_blank">📅 10:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65983">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a77f6aacbc.mp4?token=ur7tbb9ZDRy26B3R1PYjaFPPaOGaIqti7oFKF62iR1Vj-ZejIJ6tJpE8alS0SMThlDoQHWMnDY-381qP3FRxfNxZVW6A9aC6eVXPFAXgt7Mj3yzxRZd9iU2A14Ah5Z_EaWc2VoFJLE9mqiWbN00_aGvMT05hxUad5EYdGg63FOmfc0A8t3Q9aeNiNDcceUOZ4GyGb0vJNcKS8Qx8axkr42rD4BsqEi9Kp0vZXd8FAuXppSqAeYD2b3C7Y2kVnDQ_i1tlU6I-DWhg3mpJniINs6aJ6tbnZ7QcfApG5IOaMKWTthBHaSIlg9jE2bn0RE4i7hiIGV2WU6wLEcNTBTUkEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a77f6aacbc.mp4?token=ur7tbb9ZDRy26B3R1PYjaFPPaOGaIqti7oFKF62iR1Vj-ZejIJ6tJpE8alS0SMThlDoQHWMnDY-381qP3FRxfNxZVW6A9aC6eVXPFAXgt7Mj3yzxRZd9iU2A14Ah5Z_EaWc2VoFJLE9mqiWbN00_aGvMT05hxUad5EYdGg63FOmfc0A8t3Q9aeNiNDcceUOZ4GyGb0vJNcKS8Qx8axkr42rD4BsqEi9Kp0vZXd8FAuXppSqAeYD2b3C7Y2kVnDQ_i1tlU6I-DWhg3mpJniINs6aJ6tbnZ7QcfApG5IOaMKWTthBHaSIlg9jE2bn0RE4i7hiIGV2WU6wLEcNTBTUkEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ بعد دیدن این ویدیو از مسعود فهمید جز توافق راهی نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65983" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65982">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kurCHKFhpg1_4MZldB6NrFiGY5-FkfgA9PmjNzTTg78AGLchwSIzueJrXOqEsbwZll_kE0mKfnwAIWPtkuQT2dA2hBHoZgERHBaqfDAMcpmQIwMbH-mhOvqX3EcYSqmjzurQPAeXTB2MTYgX0Rv6gIXBgWcfaDb0ja40vD-FPzjRxqI-Me-gPrRIHEaeZ76BDO9rhrh5YsEZGDDVJWtNC34qcZUE8xS2iVIgN2FUgeKGYYLocHYAldRyHq3vGo5FllNl-fj8-zJxBBqbltZnXwWJObAHsezgoddnk4zMZ8M21vjM-QbfEAUaS0WF-FaDt-Jf0k9CtTLCoSl0ZgzxkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سنتکام:
ایران چندین پهپاد تهاجمی یک‌طرفه را در تلاش برای حمله به کشتی‌های تجاری در حال عبور از تنگه هرمز به پرواز درآورد. نیروهای آمریکایی در ساعات اخیر همه آنها را سرنگون کرده‌اند، در حالی که جریان ترافیک از طریق تنگه بدون مانع ادامه دارد. این کریدور تجاری بین‌المللی همچنان برای ترانزیت باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65982" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65979">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIQNYp_06Dbwt-PZVjgSmVebsJdVRO5V5Ed2Tv9cZP-Msc9ulj0ysx2auYtkfRyxRg83xOYZqyhlWZdkZq2uGRBpM39y3EafGPxpKAptieNHuIS_XHF2YxXIQnqA6gpLJ2ZmkkFfH4SIk8nagxG-C_foQMTq65Mf5iBf-h8MBMyZFayyWV65rA8VdNw-A291HCqx27CM4zy5X21GO0HTtvl97Ig4-pfpttxF4znyPArvl9ON4AIc9131tOmvkfomqKxYJrrd2mn0B2byzruVFqX7Ndzm7tUtsVBx1feSFEY3u4mW9y4CWULHz7HROhvQ0OgtDazXj5QjY3kDMisStQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روح الله خمینی:
اگر آمریکا و اسرائیل «لا اله الا الله»بگویند ما قبول نداریم چون که آنها میخواهند سر ما کلاه بگذارند
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65979" target="_blank">📅 09:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65978">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b92693abb1.mp4?token=hBFzLJAb28kRC3kvoGISonI021g9sRbWbJPzq4I-K3REwlalUdMEpYLMR0qNS_kS8EVk936p2t2ZvgK1GKm4wIMNg5Wgm1J6uM1GA2jMNQL8nYykYUOlEZGC5DhAtUG2dm-m07Cywxendr2R6-syff5OaG5aL0O2Z-31u7KSw0vACPJ5ONmoTWLKp4vmf_GarFsBsNiAeG6rXg5VCQXUXzIr9wvGHYbc0eWALePI0JbvW5EIEPbfbQock0ki4tnX3zk1_GF-BWp9dKdfzMdrpDtYN564G3uJGHD9RctWJIk9s20nG32ggatB-WN3blvNDCp4Yn_uBP9eOMb0BbMp5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b92693abb1.mp4?token=hBFzLJAb28kRC3kvoGISonI021g9sRbWbJPzq4I-K3REwlalUdMEpYLMR0qNS_kS8EVk936p2t2ZvgK1GKm4wIMNg5Wgm1J6uM1GA2jMNQL8nYykYUOlEZGC5DhAtUG2dm-m07Cywxendr2R6-syff5OaG5aL0O2Z-31u7KSw0vACPJ5ONmoTWLKp4vmf_GarFsBsNiAeG6rXg5VCQXUXzIr9wvGHYbc0eWALePI0JbvW5EIEPbfbQock0ki4tnX3zk1_GF-BWp9dKdfzMdrpDtYN564G3uJGHD9RctWJIk9s20nG32ggatB-WN3blvNDCp4Yn_uBP9eOMb0BbMp5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مراد ویسی تحلیلگر ارشد اینترنشنال:
جمهوری اسلامی خامنه ایش رو میکشن، مقاماتشو میکشن وتحقیرش میکنن بعد میزنن تو سرش میگن بیا بشین سر میز امضا کن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65978" target="_blank">📅 09:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65975">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1pRa1-3BllA0uL2P-QLFWqs5Ke7wwwz_r9gZeA0gSM_m6aayY0iCRe2oYhGBrBuL73QYqayJ4nr-OpxRbNw1GPCZqAHbuNFsJXIO3-3lvMVIL0ui4ReTlmhYFozO09LmZmdqxE6w6ira539VzGYvFLWxrsFByKeCDRFNABKWeobfBwvOrVWzTX4zuoZF74g_dlw7yIziRz4FrnXBcBZLf_D6ICQ4taGxx4luQcYj62784VkwStu8szKuIauqczY7ziDQ7nV9yt4YmX87wB6jkkAtkl3hkQU1evowrM4Q9SKebeKeTPT6tehSvIJIlWQ5oXCwG4fkK37iJepl2vLgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تندروها گرفتن رو قالیباف
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65975" target="_blank">📅 01:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65974">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
سپاه:
کشتی هایی سعی کردند بدون مجوز از تنگه هرمز عبور کنند و مورد هدف قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65974" target="_blank">📅 01:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65972">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
نایا خبرگزاری عراق: شنیده شدن صدای انفجار در قشم و سیریک  @News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65972" target="_blank">📅 00:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65971">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
نایا خبرگزاری عراق: شنیده شدن صدای انفجار در قشم و سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65971" target="_blank">📅 00:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65970">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f73bf5f98.mp4?token=lR3fEah8T7XRFRBxZwCCqBnzNbYZMf3fs3dZZ1yuK0z5ncmmY_qGoy0z8lJl7M34f68Q6_15HNqywzkXjLlnCCFk8-rZ7HPjbSMRF-9cAVcRimoCw0wIJbWQlnZJiDCmdpBamAVh4mZ_uF8idfgxKYuyvklfhvdf7Mz_iAQmeMVNirvAllOsctDzD1oOR5D9jcsD9X_g-CRqCoef2E51AfVoZKYpziGTCND6JaDra_IPSZ7Rd7FQc6yuNnedljOovYUWnbjqb8gN_Qrc3lE9maPiM6_Js9YaCqQKmxZWdMfQdazWoy39zxNSF69Hck2FCKtF8TjNEeGJNiWGTOSHJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f73bf5f98.mp4?token=lR3fEah8T7XRFRBxZwCCqBnzNbYZMf3fs3dZZ1yuK0z5ncmmY_qGoy0z8lJl7M34f68Q6_15HNqywzkXjLlnCCFk8-rZ7HPjbSMRF-9cAVcRimoCw0wIJbWQlnZJiDCmdpBamAVh4mZ_uF8idfgxKYuyvklfhvdf7Mz_iAQmeMVNirvAllOsctDzD1oOR5D9jcsD9X_g-CRqCoef2E51AfVoZKYpziGTCND6JaDra_IPSZ7Rd7FQc6yuNnedljOovYUWnbjqb8gN_Qrc3lE9maPiM6_Js9YaCqQKmxZWdMfQdazWoy39zxNSF69Hck2FCKtF8TjNEeGJNiWGTOSHJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صدا سیما: هک تصویر انفجار اتمی در تلویزیون، سیگنال آمریکا بود
!
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65970" target="_blank">📅 00:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65969">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060800d75a.mp4?token=hQHMpnHDBBD-I3cYRGho7r2mA9xcLtwCPMiWTkaIm03O1wJYM0sbxdPrOD3OF5IuAFIVuX7h75tXdFD5srt_oOxSdEQMZ1E241FY-ROxFQ904J_ql9wA-fhC64SgU0KSXJoXzvvmFfdJvwO4CaY36UGKoZslgpq0btu-5oXVV4CDyWs8Fz5Khq9ieU9-F3mHSANi0BcrMMgQoi45ecp2F09__HYLfIfesxXRKZayp9Ff32MIvtQmyCcEtsGtu5NItLaOfFgNpmB9PTzhg8iZViEjJuRkO9kqQ_UbnwkfCSjw-Ywl77M4CF0UIAMIVRqkR37ee8d7vJgVoQZYFDzNww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060800d75a.mp4?token=hQHMpnHDBBD-I3cYRGho7r2mA9xcLtwCPMiWTkaIm03O1wJYM0sbxdPrOD3OF5IuAFIVuX7h75tXdFD5srt_oOxSdEQMZ1E241FY-ROxFQ904J_ql9wA-fhC64SgU0KSXJoXzvvmFfdJvwO4CaY36UGKoZslgpq0btu-5oXVV4CDyWs8Fz5Khq9ieU9-F3mHSANi0BcrMMgQoi45ecp2F09__HYLfIfesxXRKZayp9Ff32MIvtQmyCcEtsGtu5NItLaOfFgNpmB9PTzhg8iZViEjJuRkO9kqQ_UbnwkfCSjw-Ywl77M4CF0UIAMIVRqkR37ee8d7vJgVoQZYFDzNww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
گفتگوی عراقچی هم اکنون شروع شد.  @News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65969" target="_blank">📅 23:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65968">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
عراقچی:
محاصره دریایی آمریکا اولین چیزی است که در این توافق به آن اشاره و تاکید شده است که باید رفع شود
دارایی‌های مسدود شده طبق یادداشت تفاهم اگر امضا شود، آزاد خواهد شد
هیچ‌یک از دارایی‌های ما نمی‌تواند مجددا مسدود بماند
برای جبران خسارت ایران طرح بازسازی در نظر گرفته شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65968" target="_blank">📅 23:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65967">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
عراقچی:
به زودی ایران و عمان بیانیه ای مشترک در رابطه با تنگه هرمز منتشر خواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65967" target="_blank">📅 23:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65966">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
عراقچی:
به طور قطع تنگه هرمز به شرایط قبل از جنگ باز نخواهد گشت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65966" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65965">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
عراقچی:
پایان جنگ در توافق همچنین به معنای خروج اسرائیل از مناطق اشغالی در جنوب لبنان است و ما این موضوع را صراحتاً به طرف مقابل اعلام کرده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65965" target="_blank">📅 23:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65964">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJwjYCtfezB-sOo3TTDLIkoZBEbcdmjjmMMaXuSAvykf0COT-S8fFg_Czr3HWqcT_owy62GLGexLmee4A60uNi7Ntmo1TbkFdSVEzmRkZ6IZ_Q-Nd65DdFmeQojrblOxZRtdSfqFc9HBazL_04Nv7Oag9cdVsagg5DSLq74-1z5HQIA_c0AMzmfL7FhRgflGKDrbhU3HjHae2xUs2d9GsjJE0FlBLn4p5_4_TP5lLse7fiUAbzrLEjgwIM4woSUfgsha0F5_Rw_Fe4yC8qOi3WP8_jFDXaMTcsG4VeP9WYmzlmVwD9inW1d0gG1io4QLNOH85Vk5rfBcHHzrZ4V_Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
تعهداتی که داده شده باید حفظ شود. نه اگر و نه اما و نه بهانه‌ای. برای معامله نزدیک پیش رو، راه دیگری وجود ندارد.
هر چه بکاری، همان را درو می‌کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65964" target="_blank">📅 22:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65963">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‌
🚨
🚨
عراقچی:
نتیجهٔ تفاهم یک یادداشت ۱۴ ماده‌ای است و وقتی نهایی شد تک‌تک آن را به مردم می‌گوییم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65963" target="_blank">📅 22:44 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
