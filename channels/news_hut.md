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
<img src="https://cdn4.telesco.pe/file/AE87toM8i7I9Ik1m3PaE6sNXKVe3IRgfBmbi12Bb4NiikBVO8P3-lUz3eKg4XT15Ou3140QyTohdD_np1ZuiaGpf5-ljR30M9-N-nPwN2Pjlmb42z3JogbkAM8cvdQLziDvBZmim1rYzk5umJp4UQZJtmwWQ2M0pdxQLEdOD7mgojhHtKTyde_zUXWeeGRkIYjBCcsTfwODpJkk0Z3a4T5-sUVRegbcSKF9Z2RG0G7IcBp3YH4voAytJO8Vjjmc6_6ynvy6VXyEuusMso3AjmKOKWZBywJXFLUojiU0ngNNUI3sCHghz5U4Xu0tFmk9tbyxHCMoXRPyZDGim97q_2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 19:28:13</div>
<hr>

<div class="tg-post" id="msg-66824">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO9aANO2Rp94H8_pHpOZD1OWzEquun0J1w1KPfUkLywkaOM2ad9Z5BfC-rHcLCwc8kgvNMSGESoraTu6vIyTNZ3uteyA-POYR5EbghfQtD_k1VpgK-AeIngy9U12aRAJzdodlpMSLr7pYdVsLQ9aru9E7CwcIPYtEDawqoFbTNjEMBZJTUU_l_2XjReMGnI6RAmJMHqxpACdwbVdoZObedPN2ypUzV4A0Rq3PLv97ULb3ixi8S4qkE2Z0Yyz2ZfuUiue7Q-bXX1p2Ohb-62gw6JZHF4Rv-C3uqnLiBksZxJiq1kYcuO_g82RHW_Cp7R1v_eRNNXdCbYFqnlGgPZWQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=fDlCVhdwwJakdI0qt23JHOP17ZKO4_QDgaxWYAKllzSDjUCn4yuAXJWVVBLhWhioqDXVLiZ6MFKi8ONMiIxQV_v8_NwUgHyvBH0uXLlGtAbks_4rroLi3A6KlMDVMyXJBbXbYrLC1-eZR2lH731vbPz9c9Ty5n1wXdoBGQCqFgI0V_3I4fyuAU33ZQONebllJvkHo0ROdV1kjwzS_vs0J2ZxqPtLmTF_DnFw4jz3R0y_LqDLIXo6bNVNoU-8BTn1145vVygZWKfj2tQeZ5U9UQBC78TMamfMZVPA8Yet1pqw-PSZUdQoCxG_k0IH6VPpCwC5Ao4Y64F8KUe8QfK6lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=fDlCVhdwwJakdI0qt23JHOP17ZKO4_QDgaxWYAKllzSDjUCn4yuAXJWVVBLhWhioqDXVLiZ6MFKi8ONMiIxQV_v8_NwUgHyvBH0uXLlGtAbks_4rroLi3A6KlMDVMyXJBbXbYrLC1-eZR2lH731vbPz9c9Ty5n1wXdoBGQCqFgI0V_3I4fyuAU33ZQONebllJvkHo0ROdV1kjwzS_vs0J2ZxqPtLmTF_DnFw4jz3R0y_LqDLIXo6bNVNoU-8BTn1145vVygZWKfj2tQeZ5U9UQBC78TMamfMZVPA8Yet1pqw-PSZUdQoCxG_k0IH6VPpCwC5Ao4Y64F8KUe8QfK6lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فستیوال محرم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/news_hut/66824" target="_blank">📅 19:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66823">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=UsBpEaMyDCTCDtrZDLoHtEuNRKLPnzErlz4oji0z4tPlBb3hYqaPY07VQFWmLiWUzwUCUA-W9AxoX7ZvioHQN8pbiDsiPW78Y_XHt3Lm5QVr3o4t6wMiDR20toPGtF5u1klrCgsstidVXwu5aTtPNXC8bf0wRnfH9fTG_B_EVzI66y9FSKxFBg5e1FXrSwgkY-cMiY87ILRp9En1sAKng4KVuEyPWkrBaX7MY6OvGnTwPmE5hfopB8WxIae2ESsR3JNdbnl7kOJOG1mFU-EdRLs98_Fw67Z5ddyCKDein0oG1m-Z4PTepEVpnSPgg0BvGJLV73x9Wal4X22ySAXpmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=UsBpEaMyDCTCDtrZDLoHtEuNRKLPnzErlz4oji0z4tPlBb3hYqaPY07VQFWmLiWUzwUCUA-W9AxoX7ZvioHQN8pbiDsiPW78Y_XHt3Lm5QVr3o4t6wMiDR20toPGtF5u1klrCgsstidVXwu5aTtPNXC8bf0wRnfH9fTG_B_EVzI66y9FSKxFBg5e1FXrSwgkY-cMiY87ILRp9En1sAKng4KVuEyPWkrBaX7MY6OvGnTwPmE5hfopB8WxIae2ESsR3JNdbnl7kOJOG1mFU-EdRLs98_Fw67Z5ddyCKDein0oG1m-Z4PTepEVpnSPgg0BvGJLV73x9Wal4X22ySAXpmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قالیباف پاسخ مجری صدا و سیما رو داد
@News_Hut</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/news_hut/66823" target="_blank">📅 18:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66822">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0453856b46.mp4?token=J7uWg2SH8lrpIpAkMbkoxcD-9GP32YGDHGVBReZ8do1fvg7mZQrlnKYLEs5zeywbZBw4vr-qKQVzGuhW4PViaket8Px8xKHTwJlGZgFJ0w0FMqaipwtbSSRgOrqf5A5hqB0bPu1HFY52GVQNOkcSF8MEMqX-OKlb9Jy0-xIeUIMzZJyJyBqYdJgHxksUFZT_n3Ryi5RFEiXyJu_x1_5ppX_7cQev_U6s7dhYjo_bJKomFFj4CRE9XZAwA29yeTT3-KQjNobpyRBB4-DcoYJOMKAIfhnuOQTuLok9VwylRn0jsMd2Fos1IBFlDyqiZWlghgYiywk2MiXrFZCdkyvtKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0453856b46.mp4?token=J7uWg2SH8lrpIpAkMbkoxcD-9GP32YGDHGVBReZ8do1fvg7mZQrlnKYLEs5zeywbZBw4vr-qKQVzGuhW4PViaket8Px8xKHTwJlGZgFJ0w0FMqaipwtbSSRgOrqf5A5hqB0bPu1HFY52GVQNOkcSF8MEMqX-OKlb9Jy0-xIeUIMzZJyJyBqYdJgHxksUFZT_n3Ryi5RFEiXyJu_x1_5ppX_7cQev_U6s7dhYjo_bJKomFFj4CRE9XZAwA29yeTT3-KQjNobpyRBB4-DcoYJOMKAIfhnuOQTuLok9VwylRn0jsMd2Fos1IBFlDyqiZWlghgYiywk2MiXrFZCdkyvtKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
اگر کشتی‌ها در حال حرکت باشند، واکنش ما هم بر همان اساس خواهد بود.
اما اگر کشتی‌ها حرکت نکنند، این نقض توافق محسوب می‌شود و در آن صورت با یک مشکل جدی روبه‌رو خواهیم شد
@News_Hut</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/news_hut/66822" target="_blank">📅 17:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66821">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50938460f0.mp4?token=i7qWMzA2gdXFZOJ0RUtdPlmlyvJCaND5_8ZDH0x22fVcr9ijWtRK2LC2UN6YYmeQDrnI-3bbgLzCx1Vk7TJhGlRyorox4rACP3uSokT-wL1L78ytg6LIhkbGWM5dDApbnfMa-s5FrOoKUEm-pd4fcFIvcupaq1EUWFNUtHQ4ZxJLUeYbJn4UP4qvZ0Vu-c6f4aDnqid8ENWmxSNh67jz8O_mKYJnoFVSQtzTwjyJXOozLyM0xv1BX2TDa2uv6Muf2Fy8PR4u7_OgXoVTNoNGQ6Xyjl_mFZrLvhh8iE8mgogDt_WdbfX9wFD4br2Ajv7BWiPr9N0Wb2isJMybHSKpRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50938460f0.mp4?token=i7qWMzA2gdXFZOJ0RUtdPlmlyvJCaND5_8ZDH0x22fVcr9ijWtRK2LC2UN6YYmeQDrnI-3bbgLzCx1Vk7TJhGlRyorox4rACP3uSokT-wL1L78ytg6LIhkbGWM5dDApbnfMa-s5FrOoKUEm-pd4fcFIvcupaq1EUWFNUtHQ4ZxJLUeYbJn4UP4qvZ0Vu-c6f4aDnqid8ENWmxSNh67jz8O_mKYJnoFVSQtzTwjyJXOozLyM0xv1BX2TDa2uv6Muf2Fy8PR4u7_OgXoVTNoNGQ6Xyjl_mFZrLvhh8iE8mgogDt_WdbfX9wFD4br2Ajv7BWiPr9N0Wb2isJMybHSKpRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
فرض کنیم که ما کاملاً دیوانه شده‌ایم و عقل‌مان را کاملاً از دست داده‌ایم و تصمیم گرفته‌ایم با ایجاد یک سیستم عوارض یا دریافت هزینه موافقت کنیم.
این قرار است چطور کار کند؟ اصلاً شدنی نیست. چون اگر کسی هزینه را نپردازد، چه اتفاقی می‌افتد؟
فرض کنید یک کشتی بگوید: “من این هزینه را نمی‌پردازم.” این مثل عوارضی یک جاده نیست که بعداً یک قبض جریمه برایش ارسال شود. به آن شلیک می‌کنند.
اگر به یک کشتی شلیک شود یا یک کشتی غرق شود، دیگر هیچ کشتی دیگری حرکت نخواهد کرد.
بنابراین چنین سیستمی نه‌تنها غیرعاقلانه است، بلکه اصلاً نمی‌تواند اتفاق بیفتد.
حتی قابل اجرا هم نیست. پس بهتر است همین حالا این خیال‌پردازی را کنار بگذارید.
@News_Hut</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/news_hut/66821" target="_blank">📅 17:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66820">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJ6praqAha_MBkP65yUkrEm0NDEHf-w-hwTOqXynpVQWId-ECFXV0LLaYegWfNVSHUDWkxJRYEHj7N8gFukJ4u2MBFOYhko2b0UZMQaqZi2YlWkjP4vG0ctFbIubsWBHZwX70UglUX-kibrLuh_QK42Q729HP4vKsrrbkRrUpxEa3AcpcJFH4SMxVIKs8LmtgzIcqnrydAlFxL4l5UjqakNWUVdniOYUxdrPlvnruESood_klGSO3Lfw6QnocfOiKQiGsNdLLvfGGfbrMcCp8vW2UAYS-tBp9dh9bYq56pukMeYmeG1HmtRZgDsC3zAdENd1sHjT6nzbWXmQ0N_Cjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
آمریکا به دروغ ادعا می‌کند که دارایی‌های آزاد شده ما، کشاورزی آنها را می‌خرد. جالب است. تنها محصولی که ما برداشت می‌کنیم همان چیزی است که شما کاشتید: دهه‌ها بی‌اعتمادی. این محصول ارگانیک، فراوان و تولید داخل است. اما ظاهراً ایالات متحده فقط سویای تراریخته، وعده‌های عمل نشده و حرف‌های بی‌اساس صادر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/66820" target="_blank">📅 17:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66819">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477cde7837.mp4?token=jh_jiZAGx0grdWvEHb7QUEEUWsl9bEnFUdBZFyv4zkcr23xgXtM3EG3Z-7MRQiCV58gW95GFTBHuj4X7CBCjP92a5RMVwRLGWx-LVIZkTbz7R_EAA-xr_xg_mT1Wt7y3t3tz7mXJKQamo4wMDVrK60BrtaXbmjzuVeywgcqTUhfeBRPuLt57JtunjHMaC4Fb55SIj1SwyepNf8YGolCRIRaycsb_jrHtGrAFoGLPx9R1ySKn0sBSN4UhONyMwOQIaViJs4mCwJm-gNGSNb548KjAlJzMJSOHZfacY0iGbujrD85aOo4IhG_ZyI0hoorXTdhTpvjkw0seSLclOSyDyjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477cde7837.mp4?token=jh_jiZAGx0grdWvEHb7QUEEUWsl9bEnFUdBZFyv4zkcr23xgXtM3EG3Z-7MRQiCV58gW95GFTBHuj4X7CBCjP92a5RMVwRLGWx-LVIZkTbz7R_EAA-xr_xg_mT1Wt7y3t3tz7mXJKQamo4wMDVrK60BrtaXbmjzuVeywgcqTUhfeBRPuLt57JtunjHMaC4Fb55SIj1SwyepNf8YGolCRIRaycsb_jrHtGrAFoGLPx9R1ySKn0sBSN4UhONyMwOQIaViJs4mCwJm-gNGSNb548KjAlJzMJSOHZfacY0iGbujrD85aOo4IhG_ZyI0hoorXTdhTpvjkw0seSLclOSyDyjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویرانی‌های بر جای مانده از زلزله مهیب ونزوئلا در شهر کاراکاس
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/66819" target="_blank">📅 17:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66818">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K30xs3ZTn23nz0dITGwVfHrF8RqJPQiEmvRPou8SMslr9ukPTeWUpsAWuq0_k8VnMdm6PN1E5Hy6LKvy8pORRi2IJIJiqqHDvT9gFWIALQRl4UARH8n4k3KrDsVtF9TdQLyv01QDnZUUNQAyPEm5fNX4BE6jA7TD0BxoQLgHIIpFQ87UfK4_BfkC8lcFpByV7lcWbd5CVMlQOFa0QC25bp2QNGLqFUfx8IK81PfBpS5m-XNWzQoTH2RHAatVAWVQR2gSlzcegOuukbJmVV7zdGfb9dHNcinjfpDO8s2-A8O5P7H7rJ6aF-Hrh3PHQaVnvbhwwUaNTLqvTWrjWhV_vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل قاآنی فرمانده نیروی قدس سپاه پاسداران:
اگر اسرائیل امروز داوطلبانه از جنوب لبنان عقب‌نشینی نکند، فردا مجبور به فرار با تحقیر و شکست خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/66818" target="_blank">📅 16:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66817">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=cEq7FKT7yvdPFdoL-tuMYmZHGfGBww2bLMCleOH73Bs0aPTG5rPzX8ZjC-Qp0-PMPq98B8N89c7LgDc9gkrK7D3E46QGpmf9_FsWOMGs-7rKr4wxTgMXiin69s1nm2zf6xvLPznVirlrdpbS7TQ_EZ6Y2vpS16YtwkuACPMdDfI9iKxIngdMkbrxJuGEcCIKAh_Hvm-XKjAWJys6BC3i-5cl5bvaQ9JEwntTPLbMZxlHqRSMIH3wOeEw_kbjXZIMdAoj41_EuxhjlWPVQIPM1qORUWU8ayQnebowCTqMLj5EZhPOvnpIDDg6ZPQH47LSIrjk0UOGAOWk971nBWawXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=cEq7FKT7yvdPFdoL-tuMYmZHGfGBww2bLMCleOH73Bs0aPTG5rPzX8ZjC-Qp0-PMPq98B8N89c7LgDc9gkrK7D3E46QGpmf9_FsWOMGs-7rKr4wxTgMXiin69s1nm2zf6xvLPznVirlrdpbS7TQ_EZ6Y2vpS16YtwkuACPMdDfI9iKxIngdMkbrxJuGEcCIKAh_Hvm-XKjAWJys6BC3i-5cl5bvaQ9JEwntTPLbMZxlHqRSMIH3wOeEw_kbjXZIMdAoj41_EuxhjlWPVQIPM1qORUWU8ayQnebowCTqMLj5EZhPOvnpIDDg6ZPQH47LSIrjk0UOGAOWk971nBWawXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
نیروی دریایی سپاه:
تنها کشتی هایی که از تهران مجوز دریافت کرده اند حق عبور از تنگه هرمز را دارند و با هر شناوری که از این دستور تبعیت نکند برخورد خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/66817" target="_blank">📅 16:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66816">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksv8ucyY7cqxMjW4uDN_eW4l5Ng2YImpSqJPuco_l-hounYGsZ9uYNfKDxL9tlnFzxuRdv85by9rU8EKvUeMiW7cNxzGYR9GBjHC9IyKnxNdelw6WZpATnRmERm-Tl6KRYIKXaFw6eyIxoqmsM37z9YADNNToxla5R_bWunTMih_lqAyDHZaTbbhlLigKL0dxmilXRlynzKeTmroAu-h3KKBpgwbVNaaASrObFXQYF597c2pUd0_uAIjQS0RGUsliCOc2kfHgjKVHs4SHf3PJcXKEa7A_pdmmdGFQVV1chSuaJgfAdFiqtiFutz852K-EoImEEJcRcizv7fTtwLOOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت
ترامپ در تروث سوشال:
«شگفت‌انگیز! سنا رای خود درباره ایران را از ۵۰ در برابر ۴۸ مخالف، به ۵۰ در برابر ۴۷ موافق تغییر داد. رند پال و بیل کسیدی رای خود را تغییر دادند. از جان تون، لیندزی گراهام، برنی مورنو و همه سپاسگزارم. این رای به ایران هشدار می‌دهد.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/66816" target="_blank">📅 15:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66815">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
خبرگزاری رسمی عمان:
وزیر خارجه عمان اعلام کرد ترتیبات آینده برای تنگه هرمز شامل دریافت عوارض از کشتی‌های عبوری نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/66815" target="_blank">📅 14:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66814">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=h6kBrE2L0a0hiRzYQ08GjuWOZbuSthoZNvQFarnXcucW41VNZkfuWI2JnOIh01E2CkszgvV68DFUKmYFBEIr3eUbQpzn2yIgwrIfPHn4_dAo2n-FUZZmZsYsRw8QOwti3hNl-_5Hr-VMLDHMI7ZZYwR5o9lQNE4eV2dz60ehistFuaILsmuyouqsmhIaslprF1LcibclgimNz-w0XtG1fOQBNcno4Ugx1aY2znu0xW52ld3hVvN60PHoxWPQm1Aia59kP9wAy8iEY-fZVTYFGFHs78O3s4DDWHToWBaVwtFuxf619-WQjzo82lziMpILdLRGlkMqCtIlkkFIjb3osg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=h6kBrE2L0a0hiRzYQ08GjuWOZbuSthoZNvQFarnXcucW41VNZkfuWI2JnOIh01E2CkszgvV68DFUKmYFBEIr3eUbQpzn2yIgwrIfPHn4_dAo2n-FUZZmZsYsRw8QOwti3hNl-_5Hr-VMLDHMI7ZZYwR5o9lQNE4eV2dz60ehistFuaILsmuyouqsmhIaslprF1LcibclgimNz-w0XtG1fOQBNcno4Ugx1aY2znu0xW52ld3hVvN60PHoxWPQm1Aia59kP9wAy8iEY-fZVTYFGFHs78O3s4DDWHToWBaVwtFuxf619-WQjzo82lziMpILdLRGlkMqCtIlkkFIjb3osg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره اردوغان:
🔴
او دوست من است و از جنگ دور ماند.
می‌دانید، او یکی از اصلی‌ترین گزینه‌ها برای ورود به جنگ با ایران بود.
شاید هم در طرف ایران، چون همان‌طور که می‌دانید، او طرفدار  اسرائیل نیست.
و من از او خواستم که وارد جنگ نشود. او هم وارد نشد
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/66814" target="_blank">📅 14:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66813">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYD-DYtfItoUyj8v7PTcK0dgY7cD2tJggh1TBCltZ4tCBDS6SBknPFlVC-5Ic9HxQVkXQMDBi02_myktZI03vyt1trsDtLeuK4wMdDt1P4ta4n2vQSesPIy7oo6Tma-3Or9pSJuPDQTYKLgurMW2_WWevhpbxzYyEv_Jve2KYSyQaSAvE9LEcJdYTw7AG22_-odlEJThjsb4qaZOJn_30cC_Ya-UdB9mp83l_ur3UJqHEXM1IZVImspAOqq6xwQP0H8neDCzPsPjcXdrg5CcTXyHKrYxkyH1eQ6HI3riOo95rPyLc-qKq4oT7O9BAeVGYfthqOgb69ZyewVNaUVfAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو:
🔴
واشینگتن خواهان توافق با رژیم  جمهوری اسلامی است، اما نه به هر قیمتی.  هر توافقی باید واقعی، قابل راستی آزمایی و همراه با پایبندی کامل به تعهدات باشد. اگر رژیم جمهوری اسلامی به جای صدور ایدئولوژی بر رفاه مردم ایران تمرکز کند، آمریکا و شرکایش آماده همکاری خواهند بود، اما انتخاب مسیر کنونی نتیجه مثبتی نخواهد داشت. هیچ توافقی نباید امنیت، ثبات و شکوفایی شرکای آمریکا در منطقه خلیج فارس را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/66813" target="_blank">📅 14:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66812">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=mrdDGrj1QN5_019VRvywM-G4jjXKWx4QrKhDVkybbfZGEuYJtqoAVgof_9Ad7_LI8KcEILwznnRisCFhpaxrPufbUbn_LMTeTzRRoLW8BYc_m7jV7xpARLzqiHPm2s-d7csyYBE_ZW8I7i2tKlgvLaLA0YWsfrIiEjBfX9NsXG2xI0jTURLu8oYejVRVu-oyQTwLo-L3bcUtQSg82tLyT50Gfud30ZaymwSkt_G76aakmRZa8fIroRPECQLTaygW-FLNCsUVkX6kinIQgYMDhYnS99gaetgs1mEiwYUwDElR1WLrSeoBAtvYOYkduOo--hVIMlZ74eA_wlwbilqUfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=mrdDGrj1QN5_019VRvywM-G4jjXKWx4QrKhDVkybbfZGEuYJtqoAVgof_9Ad7_LI8KcEILwznnRisCFhpaxrPufbUbn_LMTeTzRRoLW8BYc_m7jV7xpARLzqiHPm2s-d7csyYBE_ZW8I7i2tKlgvLaLA0YWsfrIiEjBfX9NsXG2xI0jTURLu8oYejVRVu-oyQTwLo-L3bcUtQSg82tLyT50Gfud30ZaymwSkt_G76aakmRZa8fIroRPECQLTaygW-FLNCsUVkX6kinIQgYMDhYnS99gaetgs1mEiwYUwDElR1WLrSeoBAtvYOYkduOo--hVIMlZ74eA_wlwbilqUfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حتی در کیس بیماری هم عجیبیم
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/66812" target="_blank">📅 14:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66811">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=Fn5XV2jrqAUZc18FZWYufzlbdAvta5B_hql06ijBe1sHn9TSDRg4694pxEPvgQzvo5jmnPPgeAuMj1XpF_3OzeRDiLnJOUfWao6IyGLfhbOyLSANP82MuhvryPJuVPfzAGIugT8AZFmzlx_ck2se2gg_5eH9dFmAqVvBlC9wUkIWALS7M-u62dXXsuarG9mcdbF-w4jc87Z3gSxAzCbALV2VCNNYsSvAga9RzwoXkJkUxjR4VFlZ_0qCxjUSBqA1acgDny64MKYmdPTu0hel4pjT_Np2CD-6EN9aMpZJC1EHmGlmrqqR_Tnt18A6RXxpvHA5Woag3m2Ewy4PuJdiug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=Fn5XV2jrqAUZc18FZWYufzlbdAvta5B_hql06ijBe1sHn9TSDRg4694pxEPvgQzvo5jmnPPgeAuMj1XpF_3OzeRDiLnJOUfWao6IyGLfhbOyLSANP82MuhvryPJuVPfzAGIugT8AZFmzlx_ck2se2gg_5eH9dFmAqVvBlC9wUkIWALS7M-u62dXXsuarG9mcdbF-w4jc87Z3gSxAzCbALV2VCNNYsSvAga9RzwoXkJkUxjR4VFlZ_0qCxjUSBqA1acgDny64MKYmdPTu0hel4pjT_Np2CD-6EN9aMpZJC1EHmGlmrqqR_Tnt18A6RXxpvHA5Woag3m2Ewy4PuJdiug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود ۷۰کشتی در ۳۶ساعت گذشته از تنگه هرمز عبور کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/66811" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66810">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.2 MB</div>
</div>
<a href="https://t.me/news_hut/66810" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
نسخه آپدیت شده اپلیکیشن ملبت
🔶
• لینک سایت مخصوص کاربران خارجیMELBET:
🌐
t.me/ConnectMELBET
🔶
• آدرس سایتMELBET
🌐
bitly.uk/connectmelbet
🟠
نکته: اپلیکیشن بدون فیلترشکن کار میکنه برای ورود به سایت باید سرور فیلترشکنتون رو کشور های اسیایی یا کانادا یا ترکیه تنظیم کنید</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/66810" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66809">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxEJsDeDnDDRowH5XKeaGL4C0Q9HEtSYpv2nmvfP6ISuOJgi3nCNlvelFa1OUJYQZ-mxN-LStnkDjb_7scTiSDKHJhk1ONRmHSqJ9WetSRzn9zxdZOI3Oq1uvR0wNZ86_T-jxH431gAKDIN1aVmKDLomFZBvyZemd8bTAQyEYM_XBIyFfZHxoRFbLvxStmOqAh7kNQ720WLHy0D7pj0Mx6JgT2DWGMyuoLpeCB7pjOHvywvCAHI7DHz4pq2q_n0LUeZ9OrCsgDYaFC62ZCEie0wdbmgfDS9cTcvbjFFiKbMwdCv0WUJ4SMIm7_wSiTfNnEohJFRr124S-8IDKIxhCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
بهترین سایت برای بت زدن سایت MELBET هست که مورد تایید ماست و خودمونم چندین ساله توش بت میزنیم
💸
با اولین واریز اگر با کد هدیه
ml_459049
ثبت نام کنید تا سقف 100 دلار 130% بیشتر شارژ میشید
واستون لینک و اپلیکیشن ملبت رو میزارم که ثبت نام کنید
🌐
https://refpa3665.com/L?tag=d_3312431m_45415c_&site=3312431&ad=45415</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/66809" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66808">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=K4WjETM-A4qx2PL9OTTysYXTm5tqqwMqkcoF7letTZk7Q7XY4iNtXIC5bC9NR_opB0MF3NhyRvLH-9fFTh5ypPC7PMkC2TiqmXGmtwmDmxdwpGRKX68l9XlfnqaX2G5QOZ7F1OXFRDcppcPRoLnPV4UyNgjDa33yu8ysXHvReGqqJnFkErZZE8BsnhcPibsZwnemONHdZRGrc-LBMokDTR-ozbYg7dAMcvVo8xa-DsDVnf2TI6c0hoHzEg4FWQ1kgS4HbdrYpuqjOJiOP7gTWn0ZpnKvUYPYAKwTRpK2zlU8KztsyIBb81yJxTP7P-fvuX20or5vYSf613QkHISJhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=K4WjETM-A4qx2PL9OTTysYXTm5tqqwMqkcoF7letTZk7Q7XY4iNtXIC5bC9NR_opB0MF3NhyRvLH-9fFTh5ypPC7PMkC2TiqmXGmtwmDmxdwpGRKX68l9XlfnqaX2G5QOZ7F1OXFRDcppcPRoLnPV4UyNgjDa33yu8ysXHvReGqqJnFkErZZE8BsnhcPibsZwnemONHdZRGrc-LBMokDTR-ozbYg7dAMcvVo8xa-DsDVnf2TI6c0hoHzEg4FWQ1kgS4HbdrYpuqjOJiOP7gTWn0ZpnKvUYPYAKwTRpK2zlU8KztsyIBb81yJxTP7P-fvuX20or5vYSf613QkHISJhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
بسیجی‌های صادراتی دیشب تو میشیگان آمریکا نذری بین آمریکایی‌ها پخش کردن
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/66808" target="_blank">📅 13:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66807">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=uJffux244wgCBrBA9_GEdL4NEQxwajbWUZq0Xh_mTBRuzDBBoRAtxVZPVFR_B4qVXzK8yzJmGkTRgrXToPGlw8nk4XKUyo6yrB67ORoT-ESFqysxs9g_7hpmV5Jtli_CuTy-QgMcy5WEEmw07toa5xYNBHRlR8HYedTEBS8twmMxbpbO7qcYMkd3nNfwSEGR9XlbCeCB3U4DhCReN7x20RV2hchx_g7APUHwWN9TEpNY7UW4iqcI8r4pAuUHsU7Zx3c7qf3gPWL2PIHsG5I-OfPkmSb8upwp7EAYwa88oI8AnVrBPBPN-Ty0ZJo0nuRwg4c8rvcqwtDbaFaCYh1QajzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=uJffux244wgCBrBA9_GEdL4NEQxwajbWUZq0Xh_mTBRuzDBBoRAtxVZPVFR_B4qVXzK8yzJmGkTRgrXToPGlw8nk4XKUyo6yrB67ORoT-ESFqysxs9g_7hpmV5Jtli_CuTy-QgMcy5WEEmw07toa5xYNBHRlR8HYedTEBS8twmMxbpbO7qcYMkd3nNfwSEGR9XlbCeCB3U4DhCReN7x20RV2hchx_g7APUHwWN9TEpNY7UW4iqcI8r4pAuUHsU7Zx3c7qf3gPWL2PIHsG5I-OfPkmSb8upwp7EAYwa88oI8AnVrBPBPN-Ty0ZJo0nuRwg4c8rvcqwtDbaFaCYh1QajzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنوز تو این دوره و عصر مدرن یه سری کسخل وجود دارن که با عقاید عصر حجر خودشونو بگا میدن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/66807" target="_blank">📅 13:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66806">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=uUeUaH8ok-ZQw3EeFOYhkm9TrbuXfpDQWUM25px8Rwwyw2rE7VhcWK3Md3i4s6xPWeO2gRdFs_g_wBpvnc3FitccS4d9CgOcuy98qaRYF1_DRpDp974NYupaVFwgEOi7h9_OZU4q_ds43vPc5azW-XLn3qa0TI9RBs0-rXa1eDmh3ym-kptub9nKryPTiwZLEYtLOhcajk2gARX_HknAz54OlhCIY_zu3Bnd1zVoeL2ImdvflIF0MZx9rf48_1_EfVRnynNspoTvuempo5dRg6Y-B-t-YCHI_W88ksfbiLwS1nv7ikVnWxvSEy6hR67Dk-KXniFzzWBZlxregat5lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=uUeUaH8ok-ZQw3EeFOYhkm9TrbuXfpDQWUM25px8Rwwyw2rE7VhcWK3Md3i4s6xPWeO2gRdFs_g_wBpvnc3FitccS4d9CgOcuy98qaRYF1_DRpDp974NYupaVFwgEOi7h9_OZU4q_ds43vPc5azW-XLn3qa0TI9RBs0-rXa1eDmh3ym-kptub9nKryPTiwZLEYtLOhcajk2gARX_HknAz54OlhCIY_zu3Bnd1zVoeL2ImdvflIF0MZx9rf48_1_EfVRnynNspoTvuempo5dRg6Y-B-t-YCHI_W88ksfbiLwS1nv7ikVnWxvSEy6hR67Dk-KXniFzzWBZlxregat5lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرستو نظام با کلی عمل زیبایی که البته هرچیزی شد بجز زیبا: قلب من با امام حسینه
😐
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66806" target="_blank">📅 12:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66805">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f836563943.mp4?token=JsWy0QugrdKNt77q5OeCKV6Nr8pggJqk13vCZ0pQ__7XD5lzm3nqXh24ImOCPo0Zbxjt9mH0UWfxbEMb6uWkiUypmY8wjvk-u3ooZ7L5YpfQttGp2v7O-WKUHZ8k5pWUrUwnKeEJwfDcjxmYQzCHM6zbERfb0UQ4yUChi9DU7QZ0Ryhshc74Pyw6auMuP59KPhdb8l4dH-gPcej0NDrfT5P97WX7Kz0xmCOi2MQK0qakXUtOiFe7mkCeIqHDNxoVRmq5iVrlvUkyshdSIPhuKhVPaAlUM7YhgeWkLzAZjnvpetQx-Zxslx26orN2bUl06N0Xb6znI74fMTQmjkPJVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f836563943.mp4?token=JsWy0QugrdKNt77q5OeCKV6Nr8pggJqk13vCZ0pQ__7XD5lzm3nqXh24ImOCPo0Zbxjt9mH0UWfxbEMb6uWkiUypmY8wjvk-u3ooZ7L5YpfQttGp2v7O-WKUHZ8k5pWUrUwnKeEJwfDcjxmYQzCHM6zbERfb0UQ4yUChi9DU7QZ0Ryhshc74Pyw6auMuP59KPhdb8l4dH-gPcej0NDrfT5P97WX7Kz0xmCOi2MQK0qakXUtOiFe7mkCeIqHDNxoVRmq5iVrlvUkyshdSIPhuKhVPaAlUM7YhgeWkLzAZjnvpetQx-Zxslx26orN2bUl06N0Xb6znI74fMTQmjkPJVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از هیئت‌های گناوه بوشهر یه مداح به این شکل از جاویدنام‌های وطن یاد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/66805" target="_blank">📅 12:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66804">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=bXtVS1wk4QJq4PCSb4Rfh2PjpZL-JiCP616TFiHcos4DBPtnD4blq9oAqwXfdMkZGEekSH8LyZi65X7gkXJcdWMrxORPUFvt5CAe24Z0aKykVDP81Y90gsNPbrSrIAhY0fLs0K4M8Wc4IQh0xjxTh2hWQPv8DmmaYN4zfIcezzLTi1FqNKan832KEc7mH6kD1IasCRPlk6rrebtNR2Aw7L-6ywALW26GTz3fhGuHok_E1QM6ZjLPByK0URCYZ-AoeTijFh9sqXkJEjZeEXgjq8WrDPHDA5zSllcWaZLhhevx5NVl6CDjOQKD3c-DWM1uH6pkJ4SYaZIPls_KwtMA7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=bXtVS1wk4QJq4PCSb4Rfh2PjpZL-JiCP616TFiHcos4DBPtnD4blq9oAqwXfdMkZGEekSH8LyZi65X7gkXJcdWMrxORPUFvt5CAe24Z0aKykVDP81Y90gsNPbrSrIAhY0fLs0K4M8Wc4IQh0xjxTh2hWQPv8DmmaYN4zfIcezzLTi1FqNKan832KEc7mH6kD1IasCRPlk6rrebtNR2Aw7L-6ywALW26GTz3fhGuHok_E1QM6ZjLPByK0URCYZ-AoeTijFh9sqXkJEjZeEXgjq8WrDPHDA5zSllcWaZLhhevx5NVl6CDjOQKD3c-DWM1uH6pkJ4SYaZIPls_KwtMA7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیره چرا شبیه یارو خپله تو آل زبیر نشسته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66804" target="_blank">📅 11:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66800">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=t_-X9r3W7-gwU8ZRMnSydvmvPLTe7-5Ld5YLiGbjoUVFhbOtTYN9R1sQIFFetXglNMg88FgURzU_Y7Qnt4ghFV7t2QxQ5XLtkNJ542NlO8P7WSx1JkLbfVIq656aLMtr4Tjl5-z9w9uUJWXnLmhobi5pvozaXEWiXzRq6OP-uVMSNJ5ldIm00JuEANUxQFDW72gBFjLSS_i8IqIDJGC5u3YFl-RgNW7rOCHT1sTt-39X4XPEDJZXDA6Mq-gnBp7XmLloFXBoYKAXq9UcGlQAHc_NanpSUYAJmYAviSUJ-7IrEg1ep3SYwfO_qQQvE0KyNtnNjRh2P80rr74nGhLe3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=t_-X9r3W7-gwU8ZRMnSydvmvPLTe7-5Ld5YLiGbjoUVFhbOtTYN9R1sQIFFetXglNMg88FgURzU_Y7Qnt4ghFV7t2QxQ5XLtkNJ542NlO8P7WSx1JkLbfVIq656aLMtr4Tjl5-z9w9uUJWXnLmhobi5pvozaXEWiXzRq6OP-uVMSNJ5ldIm00JuEANUxQFDW72gBFjLSS_i8IqIDJGC5u3YFl-RgNW7rOCHT1sTt-39X4XPEDJZXDA6Mq-gnBp7XmLloFXBoYKAXq9UcGlQAHc_NanpSUYAJmYAviSUJ-7IrEg1ep3SYwfO_qQQvE0KyNtnNjRh2P80rr74nGhLe3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تخریب آخرالزمانی در کاراکاس ونزوئلا پس از زلزله7.5 ریشتری
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66800" target="_blank">📅 10:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66799">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=gm_iqpngBWLI5-TmXMx-BUfPJtkDM_pKsQtS4tqz8eYT-0RDCxp5cd7-2lNrMq8sU3Sj3VfYPi_QY8JLyl7JQuZWP8rU7GQQBrDQ72LgzbtF44L0As2fXeLiszSZhE7kursQNJ1HaV86pwf3emnNKPtGWaeqkLz4XIGjb6gFvNO4slMJahyrKpTsrMAODMF6dkTKiTtygk9-EHOYKDa_LX-HiX2x9KQ_BCDv6WW6Yw38ZIDsn2FQtJulm742X7Z6q669tt3p_l2gnTDbI3RTjzdD6b0VqQr2BS_zAeJTHP9521MxMhPJUxBUJ8UvIp9GaJ_GDvM19kkvF6OzOA_ghiVx4633Lc1-IwQLNai_Y9vpTxZGmEelORh3j5duGpcodbUUddALXjzyKl9eQ7bPewYYWUeWCacDYUfYVDd-VwCCZBKM-zrjKhfQ4bA6U4fPX3cdTh-7XfCIgMuIl9Q6sjV6ZI7BnE5mWY9335cZj3Kpn6qIktrDm5aD_kn1lEQI3gRkmyg6VMYYLbuoOsRijqA_QYc8w6KDvMewe5FLbjlFfdti7aKFXIUXB5IM1BMJcq-KrJJQFgV6s6JCeFAg23VvxOhba4D8OythtKh2h4Vd8oiVCoDh3AZgvm12zzFEjI66pgAPTYfcKh6CQAGZA6PuQ9Xjm7mcZMMVCP16hnc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=gm_iqpngBWLI5-TmXMx-BUfPJtkDM_pKsQtS4tqz8eYT-0RDCxp5cd7-2lNrMq8sU3Sj3VfYPi_QY8JLyl7JQuZWP8rU7GQQBrDQ72LgzbtF44L0As2fXeLiszSZhE7kursQNJ1HaV86pwf3emnNKPtGWaeqkLz4XIGjb6gFvNO4slMJahyrKpTsrMAODMF6dkTKiTtygk9-EHOYKDa_LX-HiX2x9KQ_BCDv6WW6Yw38ZIDsn2FQtJulm742X7Z6q669tt3p_l2gnTDbI3RTjzdD6b0VqQr2BS_zAeJTHP9521MxMhPJUxBUJ8UvIp9GaJ_GDvM19kkvF6OzOA_ghiVx4633Lc1-IwQLNai_Y9vpTxZGmEelORh3j5duGpcodbUUddALXjzyKl9eQ7bPewYYWUeWCacDYUfYVDd-VwCCZBKM-zrjKhfQ4bA6U4fPX3cdTh-7XfCIgMuIl9Q6sjV6ZI7BnE5mWY9335cZj3Kpn6qIktrDm5aD_kn1lEQI3gRkmyg6VMYYLbuoOsRijqA_QYc8w6KDvMewe5FLbjlFfdti7aKFXIUXB5IM1BMJcq-KrJJQFgV6s6JCeFAg23VvxOhba4D8OythtKh2h4Vd8oiVCoDh3AZgvm12zzFEjI66pgAPTYfcKh6CQAGZA6PuQ9Xjm7mcZMMVCP16hnc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاروان اجنه و فرشتگان:
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66799" target="_blank">📅 10:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66798">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/638875c442.mp4?token=XjzQIaBPWD1ClMTYgVwDsigQzku09QpxJiOgLM8KN-e3k6coJQRhw9OVg2KqRd-WktOdNxSO66ShPFS69jWyQ6gjBiPwBKxvDFVNiPH1S4K5IvCZfCngpgFyofUvDnQYgADvWy6PMpiDqnEA_NXykS2YEKkiX9sbWNA6oYlc7HU6_hj4jqggrhXQmNf2MnLVysMnfz60SgPCXAD4PlVMbQWoA_DhwT3Yq2qZNes3TUHQr8U8y8l1GskMH-g3lMHlTS-pPIWfQkpFHCbRJq7eqnApvApY3cKMAuu-f0JDwbyim_q4dpBcwlei4TAgaVM2NtMnZ7Lo1S3H-y1XQnX7FA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/638875c442.mp4?token=XjzQIaBPWD1ClMTYgVwDsigQzku09QpxJiOgLM8KN-e3k6coJQRhw9OVg2KqRd-WktOdNxSO66ShPFS69jWyQ6gjBiPwBKxvDFVNiPH1S4K5IvCZfCngpgFyofUvDnQYgADvWy6PMpiDqnEA_NXykS2YEKkiX9sbWNA6oYlc7HU6_hj4jqggrhXQmNf2MnLVysMnfz60SgPCXAD4PlVMbQWoA_DhwT3Yq2qZNes3TUHQr8U8y8l1GskMH-g3lMHlTS-pPIWfQkpFHCbRJq7eqnApvApY3cKMAuu-f0JDwbyim_q4dpBcwlei4TAgaVM2NtMnZ7Lo1S3H-y1XQnX7FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه سریزد  ، یزد
شاهکاری از معماری باستان
جایی که قرن ها پیش مردم اشیاء ارزشمند خود را در اتاقک‌های امن آن نگهداری می‌کردند
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66798" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66797">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqVaJLvGAl3DMspMR8Dw8wMCjDR2FZnhwZuJOE6rmyQpvOZOCWsOATv9th9ceKOYlCHWhBRNiYwcxQvDKxwfmeS8VfpYFhCiKAOk7xU7qHxGzxmVV20YXV8nqeSmr_2aEgtb86B4IRP5epFtTm3iYbZrbCkhiGVPQozRX2WtoLUhO62sJstTeoI1hbQ8ggMxcbbDTaK0yWbCSmNuyaJmCZOmcZfZF5UcaeFhNWapqlbHL_92MUWzPBI2JaI2HThn3n0ecjJRq93YP-2MR4jumqrcUIBB7bvllTxbk2Xw3SPyitd1KtUaf5qeuXeCICahUcyJOr_qTo4xaXEIwkQ68g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
دونالد ترامپ:
دو زلزله بزرگ که اخیراً ونزوئلا را لرزاندند، بسیار عظیم بودند و تعداد زیادی قربانی برجای گذاشتند. ایالات متحده آمریکا آماده ارائه کمک است!
16;من دستور داده‌ام که تمام دستگاه‌های دولتی ما برای اقدام سریع آماده باشند. ما برای حمایت از دوستان جدید و فوق‌العاده‌مان حاضر خواهیم بود. گزارش‌های اولیه امیدوارکننده نیستند!
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66797" target="_blank">📅 09:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66796">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‼️
از ناوشکن هسته‌ای کره شمالی رونمایی شد
🔴
رسانه‌های دولتی کره شمالی گزارش دادند کیم جونگ اون اعلام کرده است نیروی دریایی این کشور به سلاح هسته‌ای مجهز می‌شود و کشتی چوئه هیون رسماً وارد خدمت شده است.
🔴
این ناوشکن ۵۰۰۰ تنی به سلاح‌های ضد هوایی و ضد کشتی مجهز است و قابلیت حمل موشک‌های کروز و بالستیک با توان حمل کلاهک هسته‌ای را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66796" target="_blank">📅 09:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66795">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66795" target="_blank">📅 03:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66794">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66794" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66793">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u3i0I4rrydFkMLEx1JamezkKZspTKrMX0yp-s8e4LTkMyjNwQEg4GCNROPiPhjeynNRUze6-wE_5OI41gjBkO9bP5kgzaZwVcUAH9H9S1yX2UWyFVra8kqP7ijxAE_Cpo2DLs9TPFrNW-6Dv8uw6oSwJXIO3_E7wyD7a74pqb5CVfQ3iJSF7507U25FuOV0BuuyYIQ6ODIDSJfd5ywd_yY9HRy-wLJP0qeb15LsDELFNrUkN0_tdsuOw2iYmDE5VVPix1vGC5KZK6DVi69RT8TAON49-CU24TGAyUahQisUCirNQZcSKcPS0TYG8sGVNjJ_dDTUEQ6CAdwVDJW4NXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66793" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66792">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17bcbdae9.mp4?token=QTE6hLm1Xc_T53sqzxRS1Jt6F1rn6lsDDklost1R_6_vc9j9Y-gHGlFBngXfDzsLLFcDDO3ATO-oOhtLYAg9kre-lBSedKuaqFiTIuH7kMVe0juJ3wZcS3QecD1H-LBHg-Qm-urmSMsDdX8GKVTvmdRAH7fl7Oim0EY45ziY_xBor7fuQvbV3_Nsn81tpgGhMOulO2H05x6aqwu2ByhfMysu6gHbqp-kTohMZ8MWXs7KY8fRvlNuz7v_is69oa0FqGjIeYxXd5qJj9kZmsnvRv71G_c3RUV6gdUelIB4JRD7sJ7mYnCuiLG66XgPizr266W8b917rnOVW6cI0mkmJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17bcbdae9.mp4?token=QTE6hLm1Xc_T53sqzxRS1Jt6F1rn6lsDDklost1R_6_vc9j9Y-gHGlFBngXfDzsLLFcDDO3ATO-oOhtLYAg9kre-lBSedKuaqFiTIuH7kMVe0juJ3wZcS3QecD1H-LBHg-Qm-urmSMsDdX8GKVTvmdRAH7fl7Oim0EY45ziY_xBor7fuQvbV3_Nsn81tpgGhMOulO2H05x6aqwu2ByhfMysu6gHbqp-kTohMZ8MWXs7KY8fRvlNuz7v_is69oa0FqGjIeYxXd5qJj9kZmsnvRv71G_c3RUV6gdUelIB4JRD7sJ7mYnCuiLG66XgPizr266W8b917rnOVW6cI0mkmJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
درست در میانه یکی از مهم‌ترین مسائل، ناگهان خبر فوری منتشر می‌شود: “سنا رأی داده است که می‌خواهد ترامپ جنگ را متوقف کند.”
ایران این را می‌بیند و می‌گوید: این دیگر چیست
؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66792" target="_blank">📅 01:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66791">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6928b1a5c.mp4?token=c2ELWsk_vamlOZ7-ZwljnsOqYzntuehFe2m1HQMFPIbYE69p1PIJTnGQAS5Mqo4RfE1YYLBJ6w3mfRy1Y6h4uuUmKFfU6Sj5GxxFVzGY_65kPcGxdUywgrdkL0_QG6L-uCEM2fSKjX6WmjQmQSNrBElUq6S0kMSJyt0qdEb5up4r5CPZGB4L61wVa3yoCv2AUdblWu6Ae0RMIfP2sRF2fq2kKratYnjEkxR3PND_1mKwqGHtZsdmVvgn4CznLP6A2qKHAvM5qeNyfz8dKm-fw82r3Zz6_yTGtHSEs1l-F-iRkwIsrBmw9HbE3FBQAe61S3Wolk9iD4bfN-d0HzPokg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6928b1a5c.mp4?token=c2ELWsk_vamlOZ7-ZwljnsOqYzntuehFe2m1HQMFPIbYE69p1PIJTnGQAS5Mqo4RfE1YYLBJ6w3mfRy1Y6h4uuUmKFfU6Sj5GxxFVzGY_65kPcGxdUywgrdkL0_QG6L-uCEM2fSKjX6WmjQmQSNrBElUq6S0kMSJyt0qdEb5up4r5CPZGB4L61wVa3yoCv2AUdblWu6Ae0RMIfP2sRF2fq2kKratYnjEkxR3PND_1mKwqGHtZsdmVvgn4CznLP6A2qKHAvM5qeNyfz8dKm-fw82r3Zz6_yTGtHSEs1l-F-iRkwIsrBmw9HbE3FBQAe61S3Wolk9iD4bfN-d0HzPokg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره حمله به مدرسه میناب:
«نمی‌دانم که آیا آن‌ها هرگز خواهند توانست این مسئله را حل کنند یا نه.
موشک‌ها از هر طرف در حال پرواز بودند.
کسی گفت که آن موشک متعلق به ما بوده است. شاید بوده باشد، اما من هیچ چیزی ندیده‌ام که مرا به این باور برساند که واقعاً موشک ما بوده است.
موشک‌های فراوان دیگری هم توسط افراد و طرف‌های دیگر شلیک شده بودند.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66791" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66790">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">Live Volleyball</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66790" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66789">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=kc3_3ofL1SCK1LI-AhqjoWxZ59sQz7s2gGsPdhHIsLkoCo-9uHSq2O-4AFZ416KjyoB4UOs9OVmbI-iFQtwy9NJ9fpvfDF2fyFs-V2uPiRkMw5YgEnGtqM6AWo6vk1J0b7UDSag843LHxSwNBcaANVay6WEHOShoHBlv-5x7VwVf926lX9AtPBB_SYdS_SqUuZiR_DVsN9YQpAlI6of5-HascKf4F85vujA3iZSot4_y4RItwPo3PY_gXea5EO9NXoKVSKri_EnHXr3P4hv-EQ62OnyhlEmYkJSRMLvNOyM0RHDZZpaMpGwKAG_fmwmXg11PAeR8-VGMFy2jaK41wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=kc3_3ofL1SCK1LI-AhqjoWxZ59sQz7s2gGsPdhHIsLkoCo-9uHSq2O-4AFZ416KjyoB4UOs9OVmbI-iFQtwy9NJ9fpvfDF2fyFs-V2uPiRkMw5YgEnGtqM6AWo6vk1J0b7UDSag843LHxSwNBcaANVay6WEHOShoHBlv-5x7VwVf926lX9AtPBB_SYdS_SqUuZiR_DVsN9YQpAlI6of5-HascKf4F85vujA3iZSot4_y4RItwPo3PY_gXea5EO9NXoKVSKri_EnHXr3P4hv-EQ62OnyhlEmYkJSRMLvNOyM0RHDZZpaMpGwKAG_fmwmXg11PAeR8-VGMFy2jaK41wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرچم نروژ فقط یک طرح ساده نیست
🇳🇴
...
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66789" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66788">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=Bi84ngccSn7T0YmKL9FeVGj8zlvwOrOnwqpaL9DUFn1OyLvb9ivCXpUBAwpbV2JHj6VJto_qPCbUMW0dQNixaZbcVS4s8ETyTVCkW_2rkfcD6gaKUYmFLxTOaKnazyHlClDndsTlgXlV9vYEEW4O90uV1YiPSYAvZkEEe-tN9xEhPC3Nq_j521nyHgUHnCX4vAf2CR8jrb0X2mDrfpptlTn-8PxH1bJJhMILq-2_kdPsLTwHkUrHXIZmNTYx_M9LWrNjM90AjWFOmr2vRytrs4htgylOgkg25ujAwfOAHMRR3cYrau_HcIA3ce_30xmTvnyrfeDi5lWB0LkqM-_8yq0H23CzvbE9xnJ_yOSYPU7RWaun9WbIFNA8Z-ByfZEdeIKaVV0kYkrLHB3Q7ZlhbfMyssovKg3IOTaymc4lco2NhjyothfuuLqCCTTXgJgkLXlrObIuWDva23LeLrqIv-KoDFqbBFzrsxTLSTjWztL72vRmviPSo7FJ3QMNqNwNTI-SL58fbJ8pDsT3M9Eh74EQ_UfUABhDYRap_BB5Y0BSdXKqANqXdZS39FzzFFIY7q4BbC-ZQRPgkUvy2Uxmf2qvTgajn73w9UK9ze-96lN4xa_3X3IeldsmoQHqvugZfNaNAKnb0xljk7_Jk9XdsOFdfb6xe9Lc_UtxYL7cX-k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=Bi84ngccSn7T0YmKL9FeVGj8zlvwOrOnwqpaL9DUFn1OyLvb9ivCXpUBAwpbV2JHj6VJto_qPCbUMW0dQNixaZbcVS4s8ETyTVCkW_2rkfcD6gaKUYmFLxTOaKnazyHlClDndsTlgXlV9vYEEW4O90uV1YiPSYAvZkEEe-tN9xEhPC3Nq_j521nyHgUHnCX4vAf2CR8jrb0X2mDrfpptlTn-8PxH1bJJhMILq-2_kdPsLTwHkUrHXIZmNTYx_M9LWrNjM90AjWFOmr2vRytrs4htgylOgkg25ujAwfOAHMRR3cYrau_HcIA3ce_30xmTvnyrfeDi5lWB0LkqM-_8yq0H23CzvbE9xnJ_yOSYPU7RWaun9WbIFNA8Z-ByfZEdeIKaVV0kYkrLHB3Q7ZlhbfMyssovKg3IOTaymc4lco2NhjyothfuuLqCCTTXgJgkLXlrObIuWDva23LeLrqIv-KoDFqbBFzrsxTLSTjWztL72vRmviPSo7FJ3QMNqNwNTI-SL58fbJ8pDsT3M9Eh74EQ_UfUABhDYRap_BB5Y0BSdXKqANqXdZS39FzzFFIY7q4BbC-ZQRPgkUvy2Uxmf2qvTgajn73w9UK9ze-96lN4xa_3X3IeldsmoQHqvugZfNaNAKnb0xljk7_Jk9XdsOFdfb6xe9Lc_UtxYL7cX-k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی که یه عده از طرفداران حکومت با هوش مصنوعی از «مختارنامه» جدید درست کردن
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66788" target="_blank">📅 23:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66787">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLyR5LdwW-KrKfJoE4bKo4w09R-3uMUlx4IhrwwQwIp6-1R1AHXzJdoE3DDKBPcke5bURSH7tfH-CcJ0Dt5etzDrdpDewl91j0jP9SB2yrafNw4Y6-8FVMUMKD9-1vebOj9obrHYtX7ZlEcOXdiGWgfDgfFePhCnVxx9OHs3ElZTJ73YprICUoda2CC1khfcXVlu17GV5lufWNqfUWN2TlLdSpu3wdzF6P4wq4nfNGFypzNEefUXFN0RedkmoGzOyGdWpQ4Z4p2zKt7h6bzCn2RQpbhKSVrxOMRE_5pjGP5wyjFBxfZL-6tKCbfS3GJpJbxFKBTdcxbOjDKvYmnaIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی وزارت امور خارجه:
اظهارات متناقض آمریکا درباره یادداشت تفاهم برای پایان جنگ به کاهش بی‌اعتمادی ایرانیان کمک نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66787" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66786">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66786" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66785">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BYHMob6285KmAALkmOgPY7bx2V6TUV34JbOX7M9RmgX-r9uQ1TbUiG-KXBGkC_NPgolS3TYVLTw_Oz1pc8vge6WSR-I1Lvmvs6gUqelIDGNaaeUn8mnK7-jJWaaXQgOvpF_c_GfrP1W1TIR_5wHZF8RuLbTCUgHC-egVce940EIJj66pCDwrSgZPjkKgji5S35EsQFFHyF1mSxylpYGGuh2xd2vMEyxUP28wvD5OS0ITQBkRE2hluUCVqjbcOuxyhiYA4NI9FTn45RUZb6aDZGaCISJJErEEKp0Zus_u9LJcB2_nxad32AqdU03aPAxn5zshVT7EP6HT0k9aQbInAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66785" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66783">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f56950043.mp4?token=TAjgrxTD9PdDkrG5ODxshSBOlCNafFBHWCEWLRW5GMPXSd4nLgobt5L-eF_xfQ-bkpobiC9oLtXSXUcqBxeEgKGymojEKk04YpCykm1DeQHqj8tfj0AAstDZ450FYC57z8_YdTNYo9pr1-dzKyorG60-yRRae4yTeQcS99T0B49aV6F_Avx8GCk7MG44sYRJCCnAptd8sI84NWIePVju0Bcajn5zPfnpZhIS_Gmv00o2sED8_G00YjssxIrjAKk4jJwe8Zo1CGq8FJpBzfwrziz8vTOLT1v1EV1mM39XNiakbBYNfidHPGIee48BgkV4SfueDlOy5FhEDl9VOtFo2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f56950043.mp4?token=TAjgrxTD9PdDkrG5ODxshSBOlCNafFBHWCEWLRW5GMPXSd4nLgobt5L-eF_xfQ-bkpobiC9oLtXSXUcqBxeEgKGymojEKk04YpCykm1DeQHqj8tfj0AAstDZ450FYC57z8_YdTNYo9pr1-dzKyorG60-yRRae4yTeQcS99T0B49aV6F_Avx8GCk7MG44sYRJCCnAptd8sI84NWIePVju0Bcajn5zPfnpZhIS_Gmv00o2sED8_G00YjssxIrjAKk4jJwe8Zo1CGq8FJpBzfwrziz8vTOLT1v1EV1mM39XNiakbBYNfidHPGIee48BgkV4SfueDlOy5FhEDl9VOtFo2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ازای شهادت مقام معظم رهبری چی از آمریکا گرفتید؟
قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66783" target="_blank">📅 23:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66782">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f387d3e0.mp4?token=bIyOd7cMkK7fBGmMCmRS7k7XZYyzSP80BchZAyy79CRdLSJmm3a8mASo_PYLr5WP42uEIZ2TUzO3y5EmWU2oRnYGRb-2ynd_n_bNlXjpRCENOsBVNN5uVoGQMdWVeY6AXcdpfM5kMJa_mJ7lexdumlJwuymWiWXGLM2rThnkU_ZwOcAZrUdA6atYtsDW7BwL0XaWzRm9eOlmhQuACLIrgO522_7PxsqHdYoGpsjWtch8ojJGKJe0QiLiRb5KoFFHfkLzrSRZBSPkhMGnmDKTtyKFR2g135qU-tfit-K2M6ls4XDj4DEE2t2tP1Ej_qgbK9r7kUEW0qDr5Ifd37p8pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f387d3e0.mp4?token=bIyOd7cMkK7fBGmMCmRS7k7XZYyzSP80BchZAyy79CRdLSJmm3a8mASo_PYLr5WP42uEIZ2TUzO3y5EmWU2oRnYGRb-2ynd_n_bNlXjpRCENOsBVNN5uVoGQMdWVeY6AXcdpfM5kMJa_mJ7lexdumlJwuymWiWXGLM2rThnkU_ZwOcAZrUdA6atYtsDW7BwL0XaWzRm9eOlmhQuACLIrgO522_7PxsqHdYoGpsjWtch8ojJGKJe0QiLiRb5KoFFHfkLzrSRZBSPkhMGnmDKTtyKFR2g135qU-tfit-K2M6ls4XDj4DEE2t2tP1Ej_qgbK9r7kUEW0qDr5Ifd37p8pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد ایران:
ایران خیلی خوب رفتار می‌کند. آنها با هر چیزی که من می‌خواهم موافقت می‌کنند و باید هم موافقت کنند.
در غیر این صورت، ما فقط برمی‌گردیم و کاری را که باید انجام دهیم، انجام می‌دهیم
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66782" target="_blank">📅 22:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66781">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=map3hdh9bFow40Dk60ix75C8bUe-OdJ9XXiJssKbN1l-zSsjX5V6QfsCz5SCDA0Cx_CbYiNYLpJpQy0pEC-_7VAtOirT05ZBGwkP0sHdVhV-FCXEdSIWkCYUC681rzQPXR6nvkFNEF4jVCJHE-xCZlaThJ-CkkttqKNf9F8AAxXbHeqxw9ch9_qV9pZD5VPI8ATU8efPs_4KKMWXiduoEmWzPzQ5bh5LqhYfNqack-sU4q9U-3SrX7-8CQUkmFKJojrJrmB_zqA6Z122uHLkyXs_KnvseMBLJYInVXs3BsHzK2KEgpjzpol1cY12XQK1kqWZ4jTLuPwosxJx2glcnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=map3hdh9bFow40Dk60ix75C8bUe-OdJ9XXiJssKbN1l-zSsjX5V6QfsCz5SCDA0Cx_CbYiNYLpJpQy0pEC-_7VAtOirT05ZBGwkP0sHdVhV-FCXEdSIWkCYUC681rzQPXR6nvkFNEF4jVCJHE-xCZlaThJ-CkkttqKNf9F8AAxXbHeqxw9ch9_qV9pZD5VPI8ATU8efPs_4KKMWXiduoEmWzPzQ5bh5LqhYfNqack-sU4q9U-3SrX7-8CQUkmFKJojrJrmB_zqA6Z122uHLkyXs_KnvseMBLJYInVXs3BsHzK2KEgpjzpol1cY12XQK1kqWZ4jTLuPwosxJx2glcnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«جنگ خیلی خوب پیش می‌رود. همانطور که
می‌دانید، ما با اختلاف زیادی در حال پیروزی هستیم. ایران امتیازات بسیار بزرگی می‌دهد. خواهیم دید چه اتفاقی می‌افتد، اما بسیار، بسیار، بسیار قدرتمند بوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66781" target="_blank">📅 22:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66780">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=rH0R_-dqreYD2EES33LgYbtgD-l6oxF8jqgEELJBJ6-ybqPpO6q7L9YZ_oRdiLqvtqwsvmmpcD0LI0e8qId_WKrWl4rM0p6-mD7GJmkdQYke0L4hsbrmicPibaC2XwoXi6gsGoXauN7epiSJXrnBvTF0c89wVkMoZpvWySuPFT1Em0Eq4gklm-RBBNF0tSgp_92QkogDBD2a3n0o2OvqkBsl5cTpJ0n8fASNH397BUIO2lgy9zTk5hn9CFbOOhbC9HCS_WWTd3_ciF8RCGCEWStEOp5fppf14L5RVU6zrhj9jdCtPrFyuSEkKaROD4ThJUNIrKzgpvHFuhcF_eoWLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=rH0R_-dqreYD2EES33LgYbtgD-l6oxF8jqgEELJBJ6-ybqPpO6q7L9YZ_oRdiLqvtqwsvmmpcD0LI0e8qId_WKrWl4rM0p6-mD7GJmkdQYke0L4hsbrmicPibaC2XwoXi6gsGoXauN7epiSJXrnBvTF0c89wVkMoZpvWySuPFT1Em0Eq4gklm-RBBNF0tSgp_92QkogDBD2a3n0o2OvqkBsl5cTpJ0n8fASNH397BUIO2lgy9zTk5hn9CFbOOhbC9HCS_WWTd3_ciF8RCGCEWStEOp5fppf14L5RVU6zrhj9jdCtPrFyuSEkKaROD4ThJUNIrKzgpvHFuhcF_eoWLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عبدالناصر همتی:
اگه کیفیت ذرت و گندم آمریکا خوب باشه ازشون میخریم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66780" target="_blank">📅 22:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66779">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RN7uGYsz7IOQwrIVXwYKFUecHm5DEIYuKVBoexPqm6IZNeYHGRqGNodx25MgAw4xIJEBhLzbQTVB_IS-BE_ZTXnK94ATFIzVDzI2YUilaveRZy33ifUDNcyLgsLS23c591pgZNAAsypSEzS4J3FGDLsh-GSdng9NzGUIxFcJPajNmShk4mFO1FLs-68H9fFFNeIxmoWhiskl1oqdLQvWWB-cN3F1aAg87Vdjl46OtW4Iq97at6HiSwLhsSxYmWLHhzLaIuKpSnmFdHaR7EcHflI9pJCsQFG4XwSDqaxxufIZlguDnM8tm9OT-6grZf5nIjoJ7R7B95f1q1rgAQs1mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتاق جنگ اسرائیل به مارکو روبیو:
رژیم جمهوری اسلامی و حامیانش در عمان در تنگه هرمز هزینه دریافت میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66779" target="_blank">📅 20:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66778">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=P3-IKCahsXaLmz3-vXT2BIVfu90OflrVpDAn5P9oUTFd5zrHMb0ZAsSlIO86nhBio6RjoaNnnyNGlQ4wQf3UlIs2zwYdQia6cjRhE_Uhp_2umwGHUVoC5zqPysbhyyqA0Vamae3VV-V_ionMct0m6JvCxEeVBLKeNYqtq8QRCncoMNEgHoUZlxs76BqdBxgv6WvuwBBjRbgh2NWwKGfy8Q9HjmC0oxuIuilGCec-bqliuKteIZ2juSpmc_e5UcIZyUWaMQAZ1ObzyjlDBQp6t7rFf3AV55peDyBnwAcCIRGUwX-YM5jOWXVrEJnPsmJs6uAY0cprHj9MNEuhSic5tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=P3-IKCahsXaLmz3-vXT2BIVfu90OflrVpDAn5P9oUTFd5zrHMb0ZAsSlIO86nhBio6RjoaNnnyNGlQ4wQf3UlIs2zwYdQia6cjRhE_Uhp_2umwGHUVoC5zqPysbhyyqA0Vamae3VV-V_ionMct0m6JvCxEeVBLKeNYqtq8QRCncoMNEgHoUZlxs76BqdBxgv6WvuwBBjRbgh2NWwKGfy8Q9HjmC0oxuIuilGCec-bqliuKteIZ2juSpmc_e5UcIZyUWaMQAZ1ObzyjlDBQp6t7rFf3AV55peDyBnwAcCIRGUwX-YM5jOWXVrEJnPsmJs6uAY0cprHj9MNEuhSic5tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
توافقات اخیر با رژیم جمهوری اسلامی بخشی از یک روند مذاکره‌ای و یک اقدام موقت ۶۰ روزه است.واشینگتن انتظار دارد تهران به تعهداتی که در سوئیس پذیرفته پایبند بماند و در غیر این صورت، پرزیدنت ترامپ ابزارها و گزینه‌های مختلفی از جمله بازگرداندن تحریم‌ها را در اختیار خواهد داشت.این تعهدات به صورت روشن و صریح مطرح شده‌اند و ادامه مسیر مذاکرات به میزان پایبندی رژیم جمهوری اسلامی به آن‌ها بستگی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66778" target="_blank">📅 20:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66777">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=djKu-SYvK0E2LmUlMJlWkpJXsp3KwjHmzXEjmcYSjogXkIpAbPk3ymxmJM2Rz78iq42iGq0BzFyerQngCDbK2bQFd_OKEHeI_Vg0rT1o0fr1Qap1BiwlpgmTIG1tn1c9tz8MhjiZ3w5szQXABH1pDC5VYCeGfJ475mKThQ3JgHmlVVkmWj9RDJv8LGgQ7nlRzOUpLgaORIkwmLxJxA7qm0g3X8E3BSssF89PTxRytbGqUpl-d_M2fqYGvAWgtHgYAz8HdKOycHSKiT55PBBEt3Mkv_S8ecE_HS3ul_2km81Gb8BCAV6AMsknTXUKq0EVcQKAvHX4EV5jBYk_fPKUKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=djKu-SYvK0E2LmUlMJlWkpJXsp3KwjHmzXEjmcYSjogXkIpAbPk3ymxmJM2Rz78iq42iGq0BzFyerQngCDbK2bQFd_OKEHeI_Vg0rT1o0fr1Qap1BiwlpgmTIG1tn1c9tz8MhjiZ3w5szQXABH1pDC5VYCeGfJ475mKThQ3JgHmlVVkmWj9RDJv8LGgQ7nlRzOUpLgaORIkwmLxJxA7qm0g3X8E3BSssF89PTxRytbGqUpl-d_M2fqYGvAWgtHgYAz8HdKOycHSKiT55PBBEt3Mkv_S8ecE_HS3ul_2km81Gb8BCAV6AMsknTXUKq0EVcQKAvHX4EV5jBYk_fPKUKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: برخی از عناصر اطلاعاتی ایالات متحده ارزیابی کرده‌اند که اسرائیل علاقه‌مند به تضعیف تفاهم‌نامه فعلی است.
🔴
روبیو: نمی‌دانم در مورد چه اطلاعاتی صحبت می‌کنید. نمی‌دانم این اطلاعات را از کجا می‌آورید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66777" target="_blank">📅 20:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66776">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=TIFBZsv8pWx1UxmrsC66OShIed391hcdszabuRW7tTCwX9ljCydAtXu9lc8pQ6cTMKO_dd3Ha32X3k8wJ_1f-UbnTqZTu1af92DSP9Y6tRFGwZYA2k7V3J4tNKhZHkJYrI3dfweG_YN5CVttwZtSJppoZpX61oxOj_UynDlfDod8MplaEihqM7ZSS-6UcI-GJ9wuTZmK4QiIMcgWk-Y5S2NTwuk_14OEbZeO1UqxV7e85zlgXigRkkWIr6CEyeK09IpLFcOIjUu7GKpO0-BE20eOnKfi3y_g5xq_C4vbAhd7kQ2wVNtVlzHI_VC6lxrtWF9ecBoGv4Gf2OnR1Fpn5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=TIFBZsv8pWx1UxmrsC66OShIed391hcdszabuRW7tTCwX9ljCydAtXu9lc8pQ6cTMKO_dd3Ha32X3k8wJ_1f-UbnTqZTu1af92DSP9Y6tRFGwZYA2k7V3J4tNKhZHkJYrI3dfweG_YN5CVttwZtSJppoZpX61oxOj_UynDlfDod8MplaEihqM7ZSS-6UcI-GJ9wuTZmK4QiIMcgWk-Y5S2NTwuk_14OEbZeO1UqxV7e85zlgXigRkkWIr6CEyeK09IpLFcOIjUu7GKpO0-BE20eOnKfi3y_g5xq_C4vbAhd7kQ2wVNtVlzHI_VC6lxrtWF9ecBoGv4Gf2OnR1Fpn5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
وقتی می‌گوییم تنگه‌ها را باز کنید، منظورمان این است که تنگه‌ها را آزاد باز کنید. آنها آبراه‌های بین‌المللی هستند.
هیچ کشوری روی کره زمین از گرفتن عوارض در تنگه‌ها حمایت نمی‌کند. این اتفاق نخواهد افتاد. ترامپ این را به روشنی بیان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66776" target="_blank">📅 20:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66775">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=jaJ0ZlsbvXPZx0T3j9OPejIoI6Kmextb5OAANwOYPBWA70ak4lhKfiLNkXvJJZjSWp1_ziJ5l8HDnpCMFkNyCibBCr76XNknsigluKKN9UhjL94gy8YStxjuVgmh3VTBORMIuUuJPNyE8d_SpvyUhiNLs64l3a5jSMQ8pbhIRKIyUie0PQ4Why0WesRrA26icl0rIYL2qlRTSqKCcJdnetvuxhlYqhaySzzQM0HARoU0_gwEa1T4CdsLukHtWup2M10sivd3Ubf8SLnYu_hIXVhRoDc8r3VN87yC0Ol2aVqjd5Z3dWzYPCGWz_m4EWLwCoJK6dMWAiRXJ2oa9F2T9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=jaJ0ZlsbvXPZx0T3j9OPejIoI6Kmextb5OAANwOYPBWA70ak4lhKfiLNkXvJJZjSWp1_ziJ5l8HDnpCMFkNyCibBCr76XNknsigluKKN9UhjL94gy8YStxjuVgmh3VTBORMIuUuJPNyE8d_SpvyUhiNLs64l3a5jSMQ8pbhIRKIyUie0PQ4Why0WesRrA26icl0rIYL2qlRTSqKCcJdnetvuxhlYqhaySzzQM0HARoU0_gwEa1T4CdsLukHtWup2M10sivd3Ubf8SLnYu_hIXVhRoDc8r3VN87yC0Ol2aVqjd5Z3dWzYPCGWz_m4EWLwCoJK6dMWAiRXJ2oa9F2T9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
به من گفتند: «وارد رفح نشو.»
می‌دانید چرا این را گفتند؟
چون رئیس‌جمهور ایالات متحده گفته بود ارسال سلاح را متوقف خواهد کرد.
من گفتم: «احترام زیادی برای او قائلم. او در آغاز جنگ کنار ما ایستاد. اما ما چاره‌ای نداریم. وارد رفح خواهیم شد. و اگر لازم باشد، حتی با ناخن‌هایمان هم خواهیم جنگید.»
گاهی باید بدانی چگونه حتی به رئیس‌جمهور ایالات متحده هم «نه» بگویی.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66775" target="_blank">📅 19:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66774">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=VSojIZGlMnNF7nYmql8nDdjfANNaSXgryfj1zcLEMbH-2062ZYdIHDvbyX178OIL9zZHlZQICpEUGgf9dX_RsizYa48AbhBNnCKKqMuo1iGb-1kmlgExM7hJHWenQII0FIPVEEfa9vr1AKMkmW7VjajfezKpH4cxqaPSkZLssvsYNoUysIX2rYzUfIXR2rA7hkdI3hmsqK1QDt4mW1oYInuPWyFn5Vh_7yoYf63w7-pvayomNMxI-W_iHxQK8paPxQT-UfpmSnjc2gFYZ9y6Jn_25tw1HsnpbjdpbtEfkz_MIvnSwpFJzTGD0BB0JczLl7PpbxDXGwx3GJLidi781A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=VSojIZGlMnNF7nYmql8nDdjfANNaSXgryfj1zcLEMbH-2062ZYdIHDvbyX178OIL9zZHlZQICpEUGgf9dX_RsizYa48AbhBNnCKKqMuo1iGb-1kmlgExM7hJHWenQII0FIPVEEfa9vr1AKMkmW7VjajfezKpH4cxqaPSkZLssvsYNoUysIX2rYzUfIXR2rA7hkdI3hmsqK1QDt4mW1oYInuPWyFn5Vh_7yoYf63w7-pvayomNMxI-W_iHxQK8paPxQT-UfpmSnjc2gFYZ9y6Jn_25tw1HsnpbjdpbtEfkz_MIvnSwpFJzTGD0BB0JczLl7PpbxDXGwx3GJLidi781A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست وزیر نتانیاهو:
در عملیات غرش شیران بود که من به ترامپ حمله در ایران را اطلاع دادم و هیچ اجازه  گرفتنی در کار نبود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66774" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66773">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=XlWHWIMSsDAXHZxBHQ-uhVXHXXDogt25dr4657mQw6mhA75rD3FSN7GHuoCZkSyLaIzPwdC5o1gVXWfcCE82zUu-MI_7tA6LXw9Gpt4zcSmUU9yyHtHE_AizjZn52_JHyY7WVLcamppSxwHPdXfdhfXmA5sakt9FaY7U-kT0QhgLqJLFKTwdWe3m_rDd6TCsfF3_-LS-rXX-hulC7khVDDfcDcqgUaSOS-vnEJXOD_PhK2AVlG19LL3Ma31jQqUpzsDQN1CWAn5HrTHmDECmgTYpVmlENYixQre_dYUIyZQWlENddpMoWZ0xtKxqakjDjdhDB6kwiU0BmyH7Bm4Gag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=XlWHWIMSsDAXHZxBHQ-uhVXHXXDogt25dr4657mQw6mhA75rD3FSN7GHuoCZkSyLaIzPwdC5o1gVXWfcCE82zUu-MI_7tA6LXw9Gpt4zcSmUU9yyHtHE_AizjZn52_JHyY7WVLcamppSxwHPdXfdhfXmA5sakt9FaY7U-kT0QhgLqJLFKTwdWe3m_rDd6TCsfF3_-LS-rXX-hulC7khVDDfcDcqgUaSOS-vnEJXOD_PhK2AVlG19LL3Ma31jQqUpzsDQN1CWAn5HrTHmDECmgTYpVmlENYixQre_dYUIyZQWlENddpMoWZ0xtKxqakjDjdhDB6kwiU0BmyH7Bm4Gag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66773" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66772">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66772" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66772" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66771">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=urR2O5N4jSZkLJBsg0iJNGlmuq2cVfT9HLmHweLt8CkQPKwZ1uo4FmhZMFeD42rHhr850leMF2J5IQ5_SxEWb9y3ObQWzuxefgp5ox_gzdJ1aa6UExeQMIOqL4qkQzzaiszM5VXTTajlk02vXGfmQCSZ6OTRDv-N6bCBNuNDVX1ZV4y1n8RyaFXWYCDYBBd6z-StugcTwBqIugnyhoso6qRLMICue68d_TOIbiSiEdiodr961Gf3eUxPQWipZVqGpitZarMbBtGEUjSAjk72X76-09NDvsjVmTvmNWk8LzKzWQBtsPImNYBCFFdIZsueBVjQgzcMCXRxrM_C74ecQyBx0kUeBV97t8BUnsOxO2QcJFYvIfpmMa9sOpEjHcsIr8N-aQ00o_CES7kWcFqK7dkwhwO0OAFxx54_Ma0EpB0pyUXDtRKHO9i6PPVnscxPWEeNJ_NyawAW6p_zq82cu3O7nD727qOYIWn6qASMcxyj5yeWagbvFEH1mzQD5xqbiowCdWRLhTVUPSl-Ir5PIdjwKLRuwwL4b7ZrMycBG5hn6iTYI_KekhWLHhPeymwPxhB0S6HnsG8apUozmjLJEXleYG7FGs9sr6FjvSQkk5_hNM7ga8fgwK4TR7MOSHbekaGCb4QR0Z6h8rEy84LGZ8e6l6X2wQRXUf-x8_SSJ1M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=urR2O5N4jSZkLJBsg0iJNGlmuq2cVfT9HLmHweLt8CkQPKwZ1uo4FmhZMFeD42rHhr850leMF2J5IQ5_SxEWb9y3ObQWzuxefgp5ox_gzdJ1aa6UExeQMIOqL4qkQzzaiszM5VXTTajlk02vXGfmQCSZ6OTRDv-N6bCBNuNDVX1ZV4y1n8RyaFXWYCDYBBd6z-StugcTwBqIugnyhoso6qRLMICue68d_TOIbiSiEdiodr961Gf3eUxPQWipZVqGpitZarMbBtGEUjSAjk72X76-09NDvsjVmTvmNWk8LzKzWQBtsPImNYBCFFdIZsueBVjQgzcMCXRxrM_C74ecQyBx0kUeBV97t8BUnsOxO2QcJFYvIfpmMa9sOpEjHcsIr8N-aQ00o_CES7kWcFqK7dkwhwO0OAFxx54_Ma0EpB0pyUXDtRKHO9i6PPVnscxPWEeNJ_NyawAW6p_zq82cu3O7nD727qOYIWn6qASMcxyj5yeWagbvFEH1mzQD5xqbiowCdWRLhTVUPSl-Ir5PIdjwKLRuwwL4b7ZrMycBG5hn6iTYI_KekhWLHhPeymwPxhB0S6HnsG8apUozmjLJEXleYG7FGs9sr6FjvSQkk5_hNM7ga8fgwK4TR7MOSHbekaGCb4QR0Z6h8rEy84LGZ8e6l6X2wQRXUf-x8_SSJ1M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66771" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66770">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFV6M3eQudQlsrBF9gVrMokBSq8UIGBiW2XyPsTTaj7KtBSh-ul_vryWfPliMw_tHvKkpNZCQ9vliqHSeZzLFmS-Av7uwCTrbAUhDddFfpWYAiTn-QKOrM5ASjDfVrv8XRgJcMMG9JTPD9SMti8dTwSS7awDaFzCbWfM5m2ikrwWu87K-470YlxOurPO70CDIXthycyxyLrbTgcN1HWthvAySstTy8wezib4WN2J29wjvtAx7eXmmqozbDkC0n7ePAqxnGXXrYD5PFjTcRo0MNGeDbCUF8FobhUdPfDKmwcTaOn01YYd8c-_zlUmGphUPkLpnRfQyGTzemMy6rdUnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت
ترامپ:
ایران به آمریکا اطلاع داده که، برخلاف گزارش‌های دردسرساز رسانه‌های فیک‌نیوز، «هیچ عوارضی، هیچ هزینه بیمه‌ای و هیچ نوع هزینه دیگری از هیچ کشتی‌ای که از تنگه هرمز عبور می‌کند، توسط ایران درخواست یا دریافت نمی‌شود. اگر این خبر نادرست باشد، مذاکرات فوراً پایان پیدا می‌کند!
همچنین، آمریکا هیچ پولی به ایران نداده و هیچ بخشی از پول‌های ایران را هم آزاد نکرده است. ما بخشی از پول‌های ایران را که کاملاً تحت کنترل خودمان است، برای حمایت از کشاورزان و دامداران آمریکایی آزاد خواهیم کرد تا با آن ذرت، گندم، سویا و محصولات دیگر خریداری شود. ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد را منحصراً از آمریکا برای آن‌ها خریداری خواهیم کرد.
از توجه شما به این موضوع متشکرم!
— دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66770" target="_blank">📅 17:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66769">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=a5wi0H6GvM5cA6lNs7UQV4ShwDBfFB6_hrCzTg54TniLm03A60cS6fLrS8wYYdVsTobF40oWSuY4Kf04uhD9YkkZ7I6btciRT3vWwge_xBrcU2mWZhlZndoP6qMJKYRwvAa-PXMke8HrvJOWyVIC705dBQAQjUvQAyxbPnfRIAZ68Dil2tn5ddriJ9pNegQrPJPTb7srbwtxi9dKQ82YaHyOtd50w23NgKxKfrqbIPbkTbQ8ry4kytoEtkAj3UmKk6AwYUhXAqofJAHrHX5xNZMU-GienBEV4oA6kwMkt2AMpqcFP2xOBLKLxxiVt2YoSaxT_Fxpk0sI1fJZhvrtoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=a5wi0H6GvM5cA6lNs7UQV4ShwDBfFB6_hrCzTg54TniLm03A60cS6fLrS8wYYdVsTobF40oWSuY4Kf04uhD9YkkZ7I6btciRT3vWwge_xBrcU2mWZhlZndoP6qMJKYRwvAa-PXMke8HrvJOWyVIC705dBQAQjUvQAyxbPnfRIAZ68Dil2tn5ddriJ9pNegQrPJPTb7srbwtxi9dKQ82YaHyOtd50w23NgKxKfrqbIPbkTbQ8ry4kytoEtkAj3UmKk6AwYUhXAqofJAHrHX5xNZMU-GienBEV4oA6kwMkt2AMpqcFP2xOBLKLxxiVt2YoSaxT_Fxpk0sI1fJZhvrtoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اگه
فکر می‌کنید قراره چیزی کسشر تر از این امروز ببینید عرض کنم که سخت در اشتباهید. فقط کافیه موزیک ویدئو شاهکار صداوسیما برای تیم امیر قلعه‌نویی رو ببینید تا بفهمید با کیا شدم ۹۰ میلیون
😐
😐
😐
😐
علی بیرو تو دروازه یا نیازمند ، کنارش شجاع و کنعانی میشن پدافند
تنگه هرمز ما تو دستای سعیده
شوت‌های قدوس و رامین مثل خیبرشکن، مستقیم به قلب دروازه‌ی دشمن میرن
ترابی دریبل‌زنه، نعمتی هم حامیشه، مثل هایپرسونیک از لای دفاع رد میشه
یه طرف میلاد و ازون طرف جهانبخش، پهباد شاهد رو روی دروازه میکنن پخش
حاج صفی ، حردانی و یوسفی مثل شیرن
توپ‌های علی علیپور از پاتریوت هم در میرن...
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66769" target="_blank">📅 17:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66768">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f90bbfd79.mp4?token=uCkBA6pPuQBbFqaLzlDvFnH93-Q4nisIINpU9hxKg-FxDh1lEzCaR_ixajXWvesgTg6k19fI_BBHJX2Swor9206TAq9hz_3PZqywAg_DZnoRbzK2hq-wg3PEaU_PdHek9_ZyieglDuCJxo6EBNCT6vH7WR42QNFWYRjuJvfKO8W50wX5qDaNWpWexBjxyhWwFtCR5aUtNCQcZ_e12u2uSxeJ7LmZloX_xabp6fwtntRVCdgoLQb9BHmQQeH1wD28rGd6Muja1pxzY2J4DNYm3EpC_qkcQlNV3GpshWaMKmXqCmGxkO_10GYuANu6IQuouAR2dOt_iJjiPbBUJtxvS4eAiw4tTCWVh-xQA5gmkDOiXWw6g6N8NHxhirJF1qBqnr9Bd7njrSzgyETntcMLxXg9UNcFMFodD4lPDNgHEx4SVJc6Pd0Hq576hjd6iPEYNlUSIyLxmGH8FQpN19zyQHXzlLR6S3AUjsYLbbPJr_ai7mAmE0MVDDvGC9FTOpBD9ggTLjDb6RDTMrS5et3pWnwqI089-3PFw_siaCwPKpM55Zoc3_Q7x_xjeMAhyUeWG64bxB_k9uE689ngBxFQlEwu0EuWK3qxO0B8HlMYZdKaOaG5_f4rs-8gCnie7nDsCF5_E2bYag-J3fqQzDrb--6g1-t-13FjVOsXE6KMIg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f90bbfd79.mp4?token=uCkBA6pPuQBbFqaLzlDvFnH93-Q4nisIINpU9hxKg-FxDh1lEzCaR_ixajXWvesgTg6k19fI_BBHJX2Swor9206TAq9hz_3PZqywAg_DZnoRbzK2hq-wg3PEaU_PdHek9_ZyieglDuCJxo6EBNCT6vH7WR42QNFWYRjuJvfKO8W50wX5qDaNWpWexBjxyhWwFtCR5aUtNCQcZ_e12u2uSxeJ7LmZloX_xabp6fwtntRVCdgoLQb9BHmQQeH1wD28rGd6Muja1pxzY2J4DNYm3EpC_qkcQlNV3GpshWaMKmXqCmGxkO_10GYuANu6IQuouAR2dOt_iJjiPbBUJtxvS4eAiw4tTCWVh-xQA5gmkDOiXWw6g6N8NHxhirJF1qBqnr9Bd7njrSzgyETntcMLxXg9UNcFMFodD4lPDNgHEx4SVJc6Pd0Hq576hjd6iPEYNlUSIyLxmGH8FQpN19zyQHXzlLR6S3AUjsYLbbPJr_ai7mAmE0MVDDvGC9FTOpBD9ggTLjDb6RDTMrS5et3pWnwqI089-3PFw_siaCwPKpM55Zoc3_Q7x_xjeMAhyUeWG64bxB_k9uE689ngBxFQlEwu0EuWK3qxO0B8HlMYZdKaOaG5_f4rs-8gCnie7nDsCF5_E2bYag-J3fqQzDrb--6g1-t-13FjVOsXE6KMIg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
⚠️
پشمام اینو داشته باشید. تو عراق از معاون وزیر نفت سابق این کشور حدود ۸۵ میلیون دلار اسکناس نقد از زیر زمین کشف کردن که دفن شده بوده!! فساد سیستماتیک تو کشورهای اسلامی ماشالا خوب رونق داره
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66768" target="_blank">📅 17:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66765">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c68737622.mp4?token=jJE0Ol83ERizvwCK9YOEHuTYwa32C-1TNFku6VhSBWa2rQ32GM5CUtdD6sw84B8z9QQladAcJ4fiahnwofDaECh8LxqPtVolIRnULuYFRgbVg1b0QanN3NNU0SbUwmKBu4Kyo7cBxuzaA94BTOKylyYFIkG2joQt1SS-dhkOZ8uq8oX-kLkwgyhhx8YRgiwHli1P74jD8YbxBHLsxC7A8JmpvErCNJd0iYbrXgPklS-m-3W1EggzP2IUtKCbqMO-hY74R6rSkYkQjFTRe4BBYSlLIwD2cFYRn6Av41NLhFsvrKi_kfDgaz1qmcVroRZGKVNa3CRalj_4R5KUbWQ-7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c68737622.mp4?token=jJE0Ol83ERizvwCK9YOEHuTYwa32C-1TNFku6VhSBWa2rQ32GM5CUtdD6sw84B8z9QQladAcJ4fiahnwofDaECh8LxqPtVolIRnULuYFRgbVg1b0QanN3NNU0SbUwmKBu4Kyo7cBxuzaA94BTOKylyYFIkG2joQt1SS-dhkOZ8uq8oX-kLkwgyhhx8YRgiwHli1P74jD8YbxBHLsxC7A8JmpvErCNJd0iYbrXgPklS-m-3W1EggzP2IUtKCbqMO-hY74R6rSkYkQjFTRe4BBYSlLIwD2cFYRn6Av41NLhFsvrKi_kfDgaz1qmcVroRZGKVNa3CRalj_4R5KUbWQ-7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
⚠️
ویدیوهایی که خیلی از دیروز  وایرال شده از کربلا؛
دیروز کاروان شیعه اسماعیلیه که تا امام ششم امام صادق رو قبول دارن، واسه زیارت به کربلا رفته بودن.
از اون طرف کاروان ایرانی ها هرجا اینارو میدیدن واکنش نشون میدادن..
تو یسری جاها هم نزدیک بود دعوا فیزیکی بشه که پلیسِ عراق اجازه نداد...
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66765" target="_blank">📅 16:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66764">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbff1343a7.mp4?token=AjHOErgpKu3lgbxSTOlk6MxmrI3nja1kwisBQMgQNzheTYSSC5gzO3pjpXUPXSy6-GY_Vhab17G9_cZL1UnG9FwQlRjVmGF2zht6tC_7wOIhLBKbREbkOhNRRA0ALkDLjLvAvPXYBnQfATnlT8h6Yqe-J4_Q6y7KZlUmw0hKRN5_NZ5B88vnYRIbTUlSxHM7hvNWO2QaER3YAVUEH3tdrFozrOKw_w_EW9p5CgpuEWzhHT87rEgL0_AFWfFROX54Ccvw8O6J37P9KtRu2qCxt-u4j4TySTHdw3C8W-EC4aaMTYHBo5cQJ2yaw5HQJp1K2JTHfw6f7FPKztAngkPzIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbff1343a7.mp4?token=AjHOErgpKu3lgbxSTOlk6MxmrI3nja1kwisBQMgQNzheTYSSC5gzO3pjpXUPXSy6-GY_Vhab17G9_cZL1UnG9FwQlRjVmGF2zht6tC_7wOIhLBKbREbkOhNRRA0ALkDLjLvAvPXYBnQfATnlT8h6Yqe-J4_Q6y7KZlUmw0hKRN5_NZ5B88vnYRIbTUlSxHM7hvNWO2QaER3YAVUEH3tdrFozrOKw_w_EW9p5CgpuEWzhHT87rEgL0_AFWfFROX54Ccvw8O6J37P9KtRu2qCxt-u4j4TySTHdw3C8W-EC4aaMTYHBo5cQJ2yaw5HQJp1K2JTHfw6f7FPKztAngkPzIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مترجم: «ما هرگز در مورد توانایی‌ها و تجهیزات هسته‌ای خودمون توافق نمی‌کنیم.»
پزشکیان: نه!! موشکی! موشکی را گفتم…!
مترجم: ببخشید موشکی.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66764" target="_blank">📅 16:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66763">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/d59ef82aac.mp4?token=jOBUai93fPzPtjavAIAyBrxE37ccgn6doS0_95mlJddNRyVYKE_kXxPl13HIgWv2Gnq63dTEVQDYc18hcxbdDDlauX7WGzixRj5scYOTN_1twwynVO21GwyabPfbuDtf3rOtXBuikMtqgFE0NtIiZ8m4WX9ju55t29Ux6CtAXZ30REWwm5v2rDiKimU3gpeYoCEaqFjVc_gOqXELGCGj8zTl6rEJp_LIz640Y4451pjX_ejeU1EUh0viGHnPuyu33mMcfjIKJsRCHmI2fgQWzveaQ0ApdcsFAB6b0v6O_8xtHiKzmZe_DtBKpaw21R-Sbtz8LC2AfmNXDFZ1j0DmaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/d59ef82aac.mp4?token=jOBUai93fPzPtjavAIAyBrxE37ccgn6doS0_95mlJddNRyVYKE_kXxPl13HIgWv2Gnq63dTEVQDYc18hcxbdDDlauX7WGzixRj5scYOTN_1twwynVO21GwyabPfbuDtf3rOtXBuikMtqgFE0NtIiZ8m4WX9ju55t29Ux6CtAXZ30REWwm5v2rDiKimU3gpeYoCEaqFjVc_gOqXELGCGj8zTl6rEJp_LIz640Y4451pjX_ejeU1EUh0viGHnPuyu33mMcfjIKJsRCHmI2fgQWzveaQ0ApdcsFAB6b0v6O_8xtHiKzmZe_DtBKpaw21R-Sbtz8LC2AfmNXDFZ1j0DmaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
مراد ویسی: با توجه به تضمین آمریکا، که گفته در جریان مذاکرات ۶۰ روزه مقامات رو ترور نمیکنیم، احتمالا تا ده روز آینده از مجتبی رونمایی بشه.
مجتبی قراره احتمال زیاد تو مراسم تشییع باباش شرکت کنه. اگرم پیداش نشد، یه جای کار میلنگه و مجتبی حالا حالاها پیداش نمیشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66763" target="_blank">📅 15:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66762">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=TnbopaUc2FvmANN8wXFKIu-nELyprntN0a697SV9cP_GrsU_uwyI98L5Itgu8yb3Leedjs0jHo8LvNCshIuKLhopQTmCzbL9qxCmnzPjhON0xTBLc0dYj31TG1VxuFggKPbrw4eyJHuP6Zx8CMNESS9S7WuQuxE6ZrdMLPEmbJ7lMDq7MgCfohL1gw1S1LBrKiXyyRX8t1H6ZC6w96Sz_GBvoWJIgUadCkEPVLDEjW_WSZfqRrin1MVcMWoMVZV1VDoUxxRKGZ2LzKCSprhz781_E8h194IX61TQhY5cOAWvnNylywqsVX6m3sb64zX0MzdA9zi8I70dA-QVX3CQbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=TnbopaUc2FvmANN8wXFKIu-nELyprntN0a697SV9cP_GrsU_uwyI98L5Itgu8yb3Leedjs0jHo8LvNCshIuKLhopQTmCzbL9qxCmnzPjhON0xTBLc0dYj31TG1VxuFggKPbrw4eyJHuP6Zx8CMNESS9S7WuQuxE6ZrdMLPEmbJ7lMDq7MgCfohL1gw1S1LBrKiXyyRX8t1H6ZC6w96Sz_GBvoWJIgUadCkEPVLDEjW_WSZfqRrin1MVcMWoMVZV1VDoUxxRKGZ2LzKCSprhz781_E8h194IX61TQhY5cOAWvnNylywqsVX6m3sb64zX0MzdA9zi8I70dA-QVX3CQbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجری شبکه دو:
کاش قبل از جلسه تفاهم نامه یه سر گلزار شهدای میناب میرفتید.
اگه محصول آمریکایی کیفیتش خوب باشه میخریم یعنی چی؟! یه کم بهتون بربخوره
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66762" target="_blank">📅 15:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66761">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vF-pWh4DFJBQgumbsRhV7JZDPQJSdIbMzghKgcuulufFDFcvklh7AN-lxZKnZdSanvxs2WBjVijU4XsuXIJOKIV-e0DtlVJKcA7fQy7y1H91wLrmd7qm1HKN1lomBka9XA0VAbIqMytrF8v3k5o3rpCKLCHxUIX2nT_sWCThDkyZNqM-sVXRxcy47iLhphslekP0Kc3K4tHM57uOPqLdHFWiv61Dbn-x-RgEyAqXWv7ZamrMdxPJaDtNZSEfBtNcI5p10UMWNzdEAUDy4olbP0242NVlucgOuiNfeG7hhjKcCiNWxNZk0D2aNxGGg9w6TnTaEBPEIJjtr4-Qyuwbhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاله دنیا جهانبخت پاشده رفته کربلا عرض ارادت به امام سوم شیعیان
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66761" target="_blank">📅 14:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66760">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kp-7uXlHAU7hxyy5jypRlEpnxMaistvZ9gt4mKUCQpT9r3ZCdI8JS9D054PB8HWDutDipYlDIVg1tV8IrPd_iUWf8jozI0WQps1S1ljLfOTmylfTUK16-aWDX1SlS0s4Er36Yhr4K7m3yaYBfeUk-JZox3_F6UR7BFs5LVZjoGBKNuk3kh-GtHiBh7F8onXcqramLSd5zfNXWbCPZ3XtpM6-QtfZ-UjOwzfTK701e51vB0z2ohAytCz1oqa3AVwpXVGXna_f-N0MhWr4LTYadTERGkR3HEBu93gFSa9QMI1_G3SPQn5LoIyLLggHDz58gLHnwCuYNtJuEzmhvdL2CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران در آینده‌ی قابل پیش‌بینی به آژانس بین‌المللی انرژی اتمی اجازه‌ی دسترسی به سایت‌های هسته‌ای مورد نظر خود را نخواهد داد. چنین بازدیدهایی مشروط به پیشرفت قابل توجه در مذاکرات است. تبلیغات و تاکتیک‌های فشار بر محاسبات ایران تأثیری نخواهد گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66760" target="_blank">📅 14:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66759">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=sDdXlIUMR46GifBs3BhdpbAOtDhCYZ_OxTFHSitWCZ33_YzME6IXc3jQzbB4sQNzlJYxJEE0gZ7flembKeafMsFPRcgTqjuj28GTeHsX3FWxbS_j_xDQLPu6StuJ5CHfLZbSUyjXTqQmRgqYi0QFNt7CmEPbzTz37j4rykWELwC3lQ95IE41K0Ql7Yw8wC6itvzgj4DWXZUH19GJisn7xO8Cdij7b5WRDsSwGqxgjWFteO-XtP87zQsEkS4D6l89YnnKWyh5us0xLveEks6fRbdEIvyjs4GWciSLueMZp2vHs7xSGzlLSubkKsl30ygSRjnjO8swJAsWNOaaHeb1Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=sDdXlIUMR46GifBs3BhdpbAOtDhCYZ_OxTFHSitWCZ33_YzME6IXc3jQzbB4sQNzlJYxJEE0gZ7flembKeafMsFPRcgTqjuj28GTeHsX3FWxbS_j_xDQLPu6StuJ5CHfLZbSUyjXTqQmRgqYi0QFNt7CmEPbzTz37j4rykWELwC3lQ95IE41K0Ql7Yw8wC6itvzgj4DWXZUH19GJisn7xO8Cdij7b5WRDsSwGqxgjWFteO-XtP87zQsEkS4D6l89YnnKWyh5us0xLveEks6fRbdEIvyjs4GWciSLueMZp2vHs7xSGzlLSubkKsl30ygSRjnjO8swJAsWNOaaHeb1Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
یادداشت تفاهم اسلام آباد به اعلام شکست آمریکا تبدیل شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66759" target="_blank">📅 14:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66758">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdGtrtxy6fRcecuOI0m2qEgYojkltdMMyR93nRtIAx09gnHtSRvLr4za8hXdw7zJH1F1yDNTvQzHxxzXDYN7ubxlMJDFodBy-5D1pjgVaWe6k_lhkHwS8ZwXn2YvpbuGV7x7YWa_A67hfn7ybMTnS6rx6C_sLBYP_V5VKa15-qIfDsetzcwyTYKqym6Fl-Ofq9wDMHIkGiazDk0VqUIhG-llBDmLX5CgokXUsFPUxyD7XqeyBHkxRWNgZCc5tZzGT4MG7CQKAR--BdgbwriTl6z14jnnc3-Su5yrHzO9WPhMVhtdQFR8uk7IXgjZWK67lugh8npacE4Bhxlwva-kyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت فست فود برای دو نفر، قیمت سال ۹۶ !
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66758" target="_blank">📅 13:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66757">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=Gb_-_A3bEkEq0xuHX85XEiPgRexEO-ZwCzE5CXIeiHZp9MADZrR2PsEhT5heimeogR_o4f09RLjJHJ_kyk9Rr6WcMUf0cKVUFigs1hBat0S0NOBG4BVhxL3mGJjBgm0wKkkKfB5fmHpShX80YX9EvVSOiDJMuAiMDVoBkgpeItTFWpmlVMs7bnsnWpI25abk4Fhdd6KbZOABoC9T0MvTy8Jc0l5MyyDdI2_b7CZFM7vhH4w8lDiyfody0ZlbJoIY6pNgXgRnRvA8AJtz1AqWpSaBeC1FzPpRRVHjFWFQrTPRJYZGPUY_vZNTRxboCtHornfn6dQ69xYDddZYs_RrAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=Gb_-_A3bEkEq0xuHX85XEiPgRexEO-ZwCzE5CXIeiHZp9MADZrR2PsEhT5heimeogR_o4f09RLjJHJ_kyk9Rr6WcMUf0cKVUFigs1hBat0S0NOBG4BVhxL3mGJjBgm0wKkkKfB5fmHpShX80YX9EvVSOiDJMuAiMDVoBkgpeItTFWpmlVMs7bnsnWpI25abk4Fhdd6KbZOABoC9T0MvTy8Jc0l5MyyDdI2_b7CZFM7vhH4w8lDiyfody0ZlbJoIY6pNgXgRnRvA8AJtz1AqWpSaBeC1FzPpRRVHjFWFQrTPRJYZGPUY_vZNTRxboCtHornfn6dQ69xYDddZYs_RrAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤯
بلندترین پل جهان که به یک آبشار عظیم تبدیل شده است؛ شاهکار تازه مهندسی چین
تصور کنید روی پلی ایستاده باشید که صدها متر بالاتر از کف دره قرار دارد و در کنار آن، دیواری عظیم از آب از دل کوه به پایین سرازیر می‌شود. این دقیقاً تصویری است که این روزها از پل «هوآجیانگ» در چین توجه کاربران شبکه‌های اجتماعی را به خود جلب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66757" target="_blank">📅 12:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66756">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=NAEsDfz-f16Yaw6tWiD6bNo--Hu328uZo_8Mnf1v4UJBNLNxQksCzivoRynvaM8CUxyrUS39pZrFuWVY9ss5e7n-PtkcY8wfyoSMeZP4QJrp-_TB2t5fhc1jFc8EHk_305DiIFBC0vwyalmHMEx-43YmFxnr3ttajSufKIw8LMVeCDqC0DxK_TTkmk4PHOJRPeL1ZT9qDexuclrBsxg4gI0uPx_knvJnsI1nQL9klavEQUe5jjBMqZMadkGAdtVtL5N8m0Dilk9Ilqho4JlYB1kwVOls6uXdYY8gkMynPMTXCPEbKbL1tC9K7FZVo-7466GpysmqxPi73lBnMzE6bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=NAEsDfz-f16Yaw6tWiD6bNo--Hu328uZo_8Mnf1v4UJBNLNxQksCzivoRynvaM8CUxyrUS39pZrFuWVY9ss5e7n-PtkcY8wfyoSMeZP4QJrp-_TB2t5fhc1jFc8EHk_305DiIFBC0vwyalmHMEx-43YmFxnr3ttajSufKIw8LMVeCDqC0DxK_TTkmk4PHOJRPeL1ZT9qDexuclrBsxg4gI0uPx_knvJnsI1nQL9klavEQUe5jjBMqZMadkGAdtVtL5N8m0Dilk9Ilqho4JlYB1kwVOls6uXdYY8gkMynPMTXCPEbKbL1tC9K7FZVo-7466GpysmqxPi73lBnMzE6bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه سرباز روسی که با پهپاد اوکراینی روبه‌رو شده بود، از اپراتور درخواست کرد که اول دوست کنارش رو بزنه تا بتونه سیگارشو قبل مرگ تموم کنه
اپراتور پهپاد درخواستش رو قبول میکنه، اول سرباز دیگه رو میزنه و بعد سربازی که درخواست کرده بود رو میزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66756" target="_blank">📅 12:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66755">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=Xiy89WSD8maRhUO108utngQBaSH__60snayNYX_0sPrzMxA9Oin316FVo0197B6LID092FY3YcNUxQOfHPPkCWgDbFvOF7oXi_4B9LWLei_9QaDbg_tQGDpC7xXY4spslj1b3yK29Am1nJyxFHPCuCxmhCGSIBJQUdMUORR_HVAqtNj1fR5BcoVkV1bfCvJryPFx5O7bf38OFaWlHoAh74fbfodpsD9IB5Yg-nk-8znltVzV762mn0tWcmdqZeNUl5CiQUUmSxthznTJOzeFbhfWKL2dLnGyiztxpCbCdJ8aTzMpingz2Gw30v2O2jiUEwY9Izmg-5X1ds3DpMVX_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=Xiy89WSD8maRhUO108utngQBaSH__60snayNYX_0sPrzMxA9Oin316FVo0197B6LID092FY3YcNUxQOfHPPkCWgDbFvOF7oXi_4B9LWLei_9QaDbg_tQGDpC7xXY4spslj1b3yK29Am1nJyxFHPCuCxmhCGSIBJQUdMUORR_HVAqtNj1fR5BcoVkV1bfCvJryPFx5O7bf38OFaWlHoAh74fbfodpsD9IB5Yg-nk-8znltVzV762mn0tWcmdqZeNUl5CiQUUmSxthznTJOzeFbhfWKL2dLnGyiztxpCbCdJ8aTzMpingz2Gw30v2O2jiUEwY9Izmg-5X1ds3DpMVX_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
دیروز تو دولت اسلامی عراق یه مسئول دولتی حوصلش سر میره و اینجوری با منشی‌ش کارای ناخوشایند اسلام از جمله
لب گرفتن و ساک‌زدن
رو انجام میدن. میگن که این یارو اخراج و بازداشت شده
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66755" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66754">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b320081976.mp4?token=l28AMWNbCZq6Y4PT49aGQuj_ZPva1FV5ETCTiyoOHVh4obBDZmhLp1lnhHUWB3S96avv0xO-g1KWVZ91Iw1fiwkSl7Rw0zPmGUyom4i75yrCFE7PqLH1aNc7XzYzRJAbSNO6suMqYHhMPirQ3gAaGoZG6jd6sHeaVKOxR7zK-W8ry3KjX4ctjUDY3LPofoLSd4tk2s3u65ui5XaOlaRMvbo4abF-VY6C9f0JGzpDh8Ysx5_Sm9hz3pH8buD38gbk8kqEIqfW4_DSGndthX8CYSdGSRmN1vLEJWwtEKtNqywjVtgGN8nYj7yHWd8a-Ejw5n2JZyYz-7asMwHe9uQAZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b320081976.mp4?token=l28AMWNbCZq6Y4PT49aGQuj_ZPva1FV5ETCTiyoOHVh4obBDZmhLp1lnhHUWB3S96avv0xO-g1KWVZ91Iw1fiwkSl7Rw0zPmGUyom4i75yrCFE7PqLH1aNc7XzYzRJAbSNO6suMqYHhMPirQ3gAaGoZG6jd6sHeaVKOxR7zK-W8ry3KjX4ctjUDY3LPofoLSd4tk2s3u65ui5XaOlaRMvbo4abF-VY6C9f0JGzpDh8Ysx5_Sm9hz3pH8buD38gbk8kqEIqfW4_DSGndthX8CYSdGSRmN1vLEJWwtEKtNqywjVtgGN8nYj7yHWd8a-Ejw5n2JZyYz-7asMwHe9uQAZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ای که مسعود توی مراسم کاشت نهال در پاکستان بیل رو ول نمیداد
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66754" target="_blank">📅 11:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66753">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44438818f9.mp4?token=TUnnpRn2N-KF3DMDgHxydo4qnwWkbwR0UfpbzkUxef4Buda6TwHrbCSJ6yWE0rCBLvMP-5Op58lnxgpt8ad-DpkGPLSS2zlNf8gkoOs1NZqPff24dLxVUwb3Vfsw6lBwmlcICEs0wp_h9-mX6CJNlT6ENcD3X6hrZBbV9dRwJR3k2eWWneXJrH1xU2rU7G2ofy8nTj23MRpbK-8TS5R9KGe2nx77tQMF68gGMf-0FCaJyPv381xDidi6tuAz0FMcz_B_MNbWXVr8wmQ08XrHfpyEpzuxE9VfDvIrpkHoplGTI7d2ycKLdCnDIIdUk_38NcMCMdB8uc6PycSm8NF2bLTdXfABdaz0mRCI7P2sAi_v3lHHPY1_xCNExPvT-y60PbpLItTBsvBh48vyqfAxQC_Pqc299RCko7hafJijiMfos-FkgSFcghszqqgj1jg9v0JXv2n1L0Ju5-rzCPRF8Rde7DJYRioAuxWmDS4I2_M8ND9i2E7SHvC7Bk155kwqZFs92ACG3n2Ri_PGL42Sw0oRK_1u9tv9nfQ7LGMfU4RD5u8yBblV9rzV0PQdYpveTUJD0O4CsDFjdAsXfQeDHd7b_pYWRODZ-HBnT9FGBa99Pi0oxU7ICVEEYsYsOmmvkZWZNXGqHX8wbhID8WUhqwMjtafrN8HB-8_wjOcIF2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44438818f9.mp4?token=TUnnpRn2N-KF3DMDgHxydo4qnwWkbwR0UfpbzkUxef4Buda6TwHrbCSJ6yWE0rCBLvMP-5Op58lnxgpt8ad-DpkGPLSS2zlNf8gkoOs1NZqPff24dLxVUwb3Vfsw6lBwmlcICEs0wp_h9-mX6CJNlT6ENcD3X6hrZBbV9dRwJR3k2eWWneXJrH1xU2rU7G2ofy8nTj23MRpbK-8TS5R9KGe2nx77tQMF68gGMf-0FCaJyPv381xDidi6tuAz0FMcz_B_MNbWXVr8wmQ08XrHfpyEpzuxE9VfDvIrpkHoplGTI7d2ycKLdCnDIIdUk_38NcMCMdB8uc6PycSm8NF2bLTdXfABdaz0mRCI7P2sAi_v3lHHPY1_xCNExPvT-y60PbpLItTBsvBh48vyqfAxQC_Pqc299RCko7hafJijiMfos-FkgSFcghszqqgj1jg9v0JXv2n1L0Ju5-rzCPRF8Rde7DJYRioAuxWmDS4I2_M8ND9i2E7SHvC7Bk155kwqZFs92ACG3n2Ri_PGL42Sw0oRK_1u9tv9nfQ7LGMfU4RD5u8yBblV9rzV0PQdYpveTUJD0O4CsDFjdAsXfQeDHd7b_pYWRODZ-HBnT9FGBa99Pi0oxU7ICVEEYsYsOmmvkZWZNXGqHX8wbhID8WUhqwMjtafrN8HB-8_wjOcIF2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💢
سنای ایالات متحده با رای ۵۰ به ۴۸، قطعنامه‌ای که توسط مجلس نمایندگان تصویب شده بود را برای جلوگیری از اقدام نظامی علیه ایران مگر اینکه رئیس‌جمهور ترامپ ابتدا مجوز کنگره را کسب کند، تصویب کرد.
«همچنان ترامپ میتونه وتو کنه»
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66753" target="_blank">📅 10:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66752">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=mFXIecOFLkOnkpr-EVCz-X2v8_juptsSp-WVBgtAbTwmjLAKDv4NoBnaTOiYMbK2fb03h02Pe0yvLHI-3wwtAZYpX3RhcG6tMno5asNQeI821TgtanSP1cj8dHmYyg9vvJ69y3daW6vU2yPayg_buflhzKw6dhRMov3kGxzNbtivF9jbdpr9rEJM8HLbPHlS1sVGPSOQJQhLb5vRF8EeEaKoa-Xts7Jf_Td5UMXaC9VaJQBzxydAEekJ-wvEJR6XWqvaqakGyZVoELLYUqxlGIxj50Dztknq06qKs5YJhFNFeLDgVFRkn1w9qTMJl7wetUCEMn4CquopgmI5qxROSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=mFXIecOFLkOnkpr-EVCz-X2v8_juptsSp-WVBgtAbTwmjLAKDv4NoBnaTOiYMbK2fb03h02Pe0yvLHI-3wwtAZYpX3RhcG6tMno5asNQeI821TgtanSP1cj8dHmYyg9vvJ69y3daW6vU2yPayg_buflhzKw6dhRMov3kGxzNbtivF9jbdpr9rEJM8HLbPHlS1sVGPSOQJQhLb5vRF8EeEaKoa-Xts7Jf_Td5UMXaC9VaJQBzxydAEekJ-wvEJR6XWqvaqakGyZVoELLYUqxlGIxj50Dztknq06qKs5YJhFNFeLDgVFRkn1w9qTMJl7wetUCEMn4CquopgmI5qxROSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجیا ملونی نخست‌وزیر ایتالیا:
نمی‌توان اجازه داد ایران به سلاح‌های هسته‌ای یا کلاهک‌های هسته‌ای دست یابد، به‌ويژه با توجه به اینکه ایران موشک‌های دوربرد دارد و این مسئله را به وضوح نشان داده است.
ملونی تأکید کرد که این موضوع تنها به ایالات متحده یا کشورهای نزدیک به مرزهای ایران یا اسرائیل محدود نمی‌شود، بلکه مسئله‌ای است که نمی‌توانیم آن را اجازه دهیم یا تحمل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66752" target="_blank">📅 10:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66751">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3361863344.mp4?token=CXAgERUUWRgAyhJtHF5C2mtFVfQGstSq21a1v6Tw0h6PbAGb8d3kV8VkYX8spGCbfD1Ls-ePNzKWo8V_epNQdcUcp-wTCPC24OKffetgv6zX_lPcj-I09EnZ9rijpyzPAxr4mzKycvo9nqDrar-gmR2CzhwWBSkenPw7KDWOnjrKHiyH8cmY4-kwRGVxi6qoVO1mAyj4qDTw1h4nZ8sEbR7zzIR7MmhYR-UJpYQwkfgwea4Kdt2fR0sIvMcwsKsm4WWbbuBd859nqZy4Zil1cPZp05inZHmtrhWZnjmpuRfKBVMulMls2gYRCDAueT8TmNdL3zOCod4W0eDcnfH7TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3361863344.mp4?token=CXAgERUUWRgAyhJtHF5C2mtFVfQGstSq21a1v6Tw0h6PbAGb8d3kV8VkYX8spGCbfD1Ls-ePNzKWo8V_epNQdcUcp-wTCPC24OKffetgv6zX_lPcj-I09EnZ9rijpyzPAxr4mzKycvo9nqDrar-gmR2CzhwWBSkenPw7KDWOnjrKHiyH8cmY4-kwRGVxi6qoVO1mAyj4qDTw1h4nZ8sEbR7zzIR7MmhYR-UJpYQwkfgwea4Kdt2fR0sIvMcwsKsm4WWbbuBd859nqZy4Zil1cPZp05inZHmtrhWZnjmpuRfKBVMulMls2gYRCDAueT8TmNdL3zOCod4W0eDcnfH7TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار «مثل رهبر ما مخالف با تفاهم‌نامه‌ایم»در هیات
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66751" target="_blank">📅 09:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66750">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=cDALF-tP-jg4C8jxc3NX2G50Ehe5O2vd5vfG9YsFysg-SjpTDCcEBFoTRhb0zPk4hy7W_E7SVlRMSnaIW_ahi6QJ4rzRm2SwWO_TTflY68-Jno7EZZ_VlfeVuEYk_JoW-Q2chaOwlAubPBUBbG3OdiOGrGQtgzl2ZEtjtWdtGi_zBkOHDuYkDkba8n1QSXSA8WBZZVa0_-WHrWWdNVvb3HtmBTW01eHGwEOfyP4UaP08_zf9bSaW0k9RiEuEk-z3pV14XHTky4Mc37_HOQ7dEvY78VRUG6iiFwCUu37-oEs2itx5jYGw8kFwfLAQw2qKIAtIMuBkvGK5lxhuJFenig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=cDALF-tP-jg4C8jxc3NX2G50Ehe5O2vd5vfG9YsFysg-SjpTDCcEBFoTRhb0zPk4hy7W_E7SVlRMSnaIW_ahi6QJ4rzRm2SwWO_TTflY68-Jno7EZZ_VlfeVuEYk_JoW-Q2chaOwlAubPBUBbG3OdiOGrGQtgzl2ZEtjtWdtGi_zBkOHDuYkDkba8n1QSXSA8WBZZVa0_-WHrWWdNVvb3HtmBTW01eHGwEOfyP4UaP08_zf9bSaW0k9RiEuEk-z3pV14XHTky4Mc37_HOQ7dEvY78VRUG6iiFwCUu37-oEs2itx5jYGw8kFwfLAQw2qKIAtIMuBkvGK5lxhuJFenig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای وایرال شده از خوشحالی تیم ملی نروژ به سبک وایکینگ ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66750" target="_blank">📅 09:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66749">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66749" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66748">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EbQRPXv0lKOKH-b-9sjyELw9iO0ytkAJorY3gTyZgjUYQ0NEa2msKoE7Vo11JPDLtw9Uee8q9HKbWHeerJEfuaztd3h4v4sxYGsvc56VONKQVDHW5OUFt51PB5V8g-B9QCTSfFyyrhmSvvcZXS3AkFeyZ0yYrL3x4inBD8Vxszay1DEB9ns0SpCidKwL-TanAVH0KFJLGUtQTkDOEiInmbs_nGITNpe94CzEl4CMIJw6SUFApyP02lGyUpJz2E7DwAznyWT83cwRsGg3Zw7HrXQrcEPC6FHXS_ujzpgofW2ciFCvWYJLpJCdHqWBG-t22Sz6Nwjr2eU34Lo6h08SPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66748" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66747">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=E_AN-KCcJXkp1q3fTEhqNRg7r-N1GpYNWhOjuinVLFAqWNgHjQWzBUtiRgdubdYj3iyv1ZjqxfdvvXUf1TMP6qDfHFmUt-3xYE2IG8Cf5GujfhLPPFkdw4pRstX83kYiK24FoBPK2MSEcobKLZtaBbn8UgjZNzfCQu66srrknEEE0aWth9ZfI88SxoqRwtulwIOV3WnvAw_L0VUsTSaUIwhkepnS7MkFgfP1Y7xG6fX9uXJaphz-UxyDKgfTs5R1a6GNWXYeALFUNgvYMdLHD4ZTnLA5st7gj8Ac34KUsJWE7DiVq2RnCZBsl4MoprDkMxTZEQ3q-Sx1PLKGOyVVdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=E_AN-KCcJXkp1q3fTEhqNRg7r-N1GpYNWhOjuinVLFAqWNgHjQWzBUtiRgdubdYj3iyv1ZjqxfdvvXUf1TMP6qDfHFmUt-3xYE2IG8Cf5GujfhLPPFkdw4pRstX83kYiK24FoBPK2MSEcobKLZtaBbn8UgjZNzfCQu66srrknEEE0aWth9ZfI88SxoqRwtulwIOV3WnvAw_L0VUsTSaUIwhkepnS7MkFgfP1Y7xG6fX9uXJaphz-UxyDKgfTs5R1a6GNWXYeALFUNgvYMdLHD4ZTnLA5st7gj8Ac34KUsJWE7DiVq2RnCZBsl4MoprDkMxTZEQ3q-Sx1PLKGOyVVdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«ایران عالی بوده است؛ ایران منطقی رفتار کند و باهوش باشد. در غیر این صورت، مجبور خواهیم شد کار را تمام کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66747" target="_blank">📅 01:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66746">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=Ump3kxeXIaKNKyOZ83NZatvs4s6vtI4z6WhIzn-FlBHIkF8VGmtmZ_mLo0g4YRE1MOMH1c1Tbo-SGOvsqC8rUnu0gkSzTBbNo2-1dWW8t6sLHC8mDEICtHTvsd9TW-lGRmdLQlTTp0i_RV9dKQA0WVzge2vEs3Hy-31lcZ64_mFf9mMBnb--6Jn7VvM5A1vY9pDRbD3_Ft2NXMvTkBhDYkXF9ACrxaKXPp3yT24KidmKRer91IKGe-uaSwVec-Koa5LY3izlMF6B9UE9CivqqNUAQFT73hmi25ClP9gqnPuO9MsnX6Ydpcy-OPqqf7Ssq15OlxgPhiUh0IBa5FNWgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=Ump3kxeXIaKNKyOZ83NZatvs4s6vtI4z6WhIzn-FlBHIkF8VGmtmZ_mLo0g4YRE1MOMH1c1Tbo-SGOvsqC8rUnu0gkSzTBbNo2-1dWW8t6sLHC8mDEICtHTvsd9TW-lGRmdLQlTTp0i_RV9dKQA0WVzge2vEs3Hy-31lcZ64_mFf9mMBnb--6Jn7VvM5A1vY9pDRbD3_Ft2NXMvTkBhDYkXF9ACrxaKXPp3yT24KidmKRer91IKGe-uaSwVec-Koa5LY3izlMF6B9UE9CivqqNUAQFT73hmi25ClP9gqnPuO9MsnX6Ydpcy-OPqqf7Ssq15OlxgPhiUh0IBa5FNWgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران ایدئولوژی بسیار متفاوتی نسبت به ونزوئلا دارد.
ایدئولوژی مسلمانان تا حدی با ایدئولوژی کاتولیک‌ها متفاوت است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66746" target="_blank">📅 01:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66745">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=RXHADveIWyWy55G10coRXwuznZCL4ONIYBFJTu7IeAR4tl4LzbxK7blK1uQvvzj0aCtr6xMdEuaN1y4XTBTmqRefSYjsElKec80yDyCLxQYX1uakZf59kFYBkolXMhhzABxSs7fzVbE0SZ14gszWRgb-N2hZEDOaBIh8N-E9XSPpFDkbRvSjS-Y09pXoQSgDZeqBHtfzsazf-gSly1NdCLc6WjWRrkmznMZucDyzOlbYQdivv96lqPvvNNSq0sOKQPwQ25TCIWmbtOSb7vSl4SvRru7JxvjGKpduLObf89ljDRac385LGwFZs9XX_Jx3syp-KEJnkZX1r_ZaV-85EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a9dbdc564.mp4?token=RXHADveIWyWy55G10coRXwuznZCL4ONIYBFJTu7IeAR4tl4LzbxK7blK1uQvvzj0aCtr6xMdEuaN1y4XTBTmqRefSYjsElKec80yDyCLxQYX1uakZf59kFYBkolXMhhzABxSs7fzVbE0SZ14gszWRgb-N2hZEDOaBIh8N-E9XSPpFDkbRvSjS-Y09pXoQSgDZeqBHtfzsazf-gSly1NdCLc6WjWRrkmznMZucDyzOlbYQdivv96lqPvvNNSq0sOKQPwQ25TCIWmbtOSb7vSl4SvRru7JxvjGKpduLObf89ljDRac385LGwFZs9XX_Jx3syp-KEJnkZX1r_ZaV-85EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این میم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66745" target="_blank">📅 00:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66744">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=o3ovLCTXXbH9eqdNLvV0Cgsc2kWWdEt2TdgnH7Ub8rpYRwcamCLvjLi251fQt7gS5ESfS8aT8Y7ipn-qgsHAPCk-2LKHen-DBlU-TFdsZyZ3gM0JJ4reWtGSO9524B1VMn80c3lTYOgcxjv9HmjTJVhfzBqn-LUYztXtfaPjuIze4Uo9wJGj87c3uF9dn4ujziYmMVZkkGQh83JujBxq0oza20GAmsLtbb9CHipanTd6UsWQlcTmpHqiMuvvbOInVhorfHJAhvNEppmbMZs7VNRZHnXhYuX3gBSA9wasGBDm_8FicCnbl8c0_5w5jEdsF6gyhHV3XcZCsMEf7ybWng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cacbd8e2b7.mp4?token=o3ovLCTXXbH9eqdNLvV0Cgsc2kWWdEt2TdgnH7Ub8rpYRwcamCLvjLi251fQt7gS5ESfS8aT8Y7ipn-qgsHAPCk-2LKHen-DBlU-TFdsZyZ3gM0JJ4reWtGSO9524B1VMn80c3lTYOgcxjv9HmjTJVhfzBqn-LUYztXtfaPjuIze4Uo9wJGj87c3uF9dn4ujziYmMVZkkGQh83JujBxq0oza20GAmsLtbb9CHipanTd6UsWQlcTmpHqiMuvvbOInVhorfHJAhvNEppmbMZs7VNRZHnXhYuX3gBSA9wasGBDm_8FicCnbl8c0_5w5jEdsF6gyhHV3XcZCsMEf7ybWng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
​
اگر ما موشک‌های خود را که برای دفاع شخصی‌مان است نداشتیم، اسرائیل و آمریکا با ایران همان‌گونه رفتار می‌کردند که با غزه رفتار شد و هیچ رحمی به پیر و جوان نشان نمی‌دادند.
​ آن‌ها از حقوق بشر سخن می‌گویند، این یک دروغ بزرگ است.
​ اگر نمی‌توانستیم از خود دفاع کنیم، آن‌ها به کشور ما رحمی نمی‌کردند و قدرت ما را نابود می‌کردند.
​ بنابراین ما تحت هیچ شرایطی با هیچ‌کس درباره توان دفاعی‌مان مذاکره نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66744" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66743">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=AelBRwqsNmqKrSORBlANwx4hF_HsNbUYJQWp4PcezkH3Wzm9J-urxZtOlABvJdMI0mH80DcVnd5kF3Qi4S-bOo66WIubv1ePQJ9tAt9kAPVLon83niEQB3JUT0s_07vEHUmPgXycy7cw9lg1-EmUyMtN8ZxbKmnQ5VQhBIGE5MhDwCHBrruQ0dixfkSQzGJ-nGDyrlbU5uwtITJ6KJ1iDNV8sCArWSZb2MYNJF3g1eRR2tjbtbEyZAyeEvWRoiz2pBBcX6qYCYBOwdwXm5aVszOKlrgVgvp4QGh9E9uLY2w2EK2C9QYql9e4eVEhy_gn_3St3xEze1dIEGTXvVIDGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26c20ba7fc.mp4?token=AelBRwqsNmqKrSORBlANwx4hF_HsNbUYJQWp4PcezkH3Wzm9J-urxZtOlABvJdMI0mH80DcVnd5kF3Qi4S-bOo66WIubv1ePQJ9tAt9kAPVLon83niEQB3JUT0s_07vEHUmPgXycy7cw9lg1-EmUyMtN8ZxbKmnQ5VQhBIGE5MhDwCHBrruQ0dixfkSQzGJ-nGDyrlbU5uwtITJ6KJ1iDNV8sCArWSZb2MYNJF3g1eRR2tjbtbEyZAyeEvWRoiz2pBBcX6qYCYBOwdwXm5aVszOKlrgVgvp4QGh9E9uLY2w2EK2C9QYql9e4eVEhy_gn_3St3xEze1dIEGTXvVIDGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو وزیر امور خارجه آمریکا وارد ابوظبی، پایتخت امارات متحده عربی، شد. جزئیاتی درباره دستور کار، دیدارهای رسمی و محورهای مذاکرات این سفر هنوز منتشر نشده است، اما این سفر در شرایطی انجام می‌شود که پرونده‌های امنیتی و تحولات منطقه‌ای، از جمله موضوع رژیم جمهوری اسلامی، در کانون توجه قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66743" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66742">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=sR1nwvfZQNV5CmpxSqy5Mippl7n024RjAGEGLpyIOR9YEW-kYrkdnx0xFKNtmJYpx04zI2zsbRylUQ7VH4LI94zvknbAp2eBHGUdJfhcOgEKeamwnq-kPV_ZsxAXzTfn0uJmJpdeAuaLz4-bdFq96c5-hvetvXLNQjK1fQT0lBzsesjmQfXk7UQylMPMBzcpCzj7GbolmRw-X3KJYIR4uqBEtQw_BRnUEgGSSo7yUoM3_TDkgoSxxRilsONkBEHqFGPWvX_B7jNdDh65J7-NhvKW41jkOWlvJVimC5CI2ngs_GBv78h87XaR0gbiiO9Wlvj9VDri66aDBxUWQfi8xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4552ac245.mp4?token=sR1nwvfZQNV5CmpxSqy5Mippl7n024RjAGEGLpyIOR9YEW-kYrkdnx0xFKNtmJYpx04zI2zsbRylUQ7VH4LI94zvknbAp2eBHGUdJfhcOgEKeamwnq-kPV_ZsxAXzTfn0uJmJpdeAuaLz4-bdFq96c5-hvetvXLNQjK1fQT0lBzsesjmQfXk7UQylMPMBzcpCzj7GbolmRw-X3KJYIR4uqBEtQw_BRnUEgGSSo7yUoM3_TDkgoSxxRilsONkBEHqFGPWvX_B7jNdDh65J7-NhvKW41jkOWlvJVimC5CI2ngs_GBv78h87XaR0gbiiO9Wlvj9VDri66aDBxUWQfi8xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعرخوانی جالب شهباز شریف به زبان فارسی در حضور پزشکیان
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66742" target="_blank">📅 22:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66741">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما ایران را در وضعیتی بی‌سابقه قرار دادیم که در ۴۷ سال گذشته هیچ‌کس موفق به انجام آن نشده بود. اگر ادعای ایرانی‌ها مبنی بر عدم اجازه ورود بازرسان آژانس بین‌المللی انرژی اتمی به ایران صحت داشت، نشست با آن‌ها را فوراً لغو می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66741" target="_blank">📅 21:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66740">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=sLOLlv4_wVdeulJu8YyLi19Bbp-dB49N-B8gjZRiogMtoxkLYFxv4RICjZU17zVDDzxQm3cv4Xrh-Xr0T7Qz6Wn4GRtQ8B2iXzecAfmBdH0aknJBq9IPQmGzricufT75bR7LGLv84ireNgIjL27qOppGgV8onaZ0OEZPV6Cfvs1FkBJkHEC_ylwXAKkxgY-7YkBGgMP4_XGp1MdQ2AczcVdcKSUhv48BhoqZ-9Qggj_nuIWvJIgjIzZ-l0SdlTD6BBzFh_Fnwrl_B4J3WH19wzbeij6nvKyrokuTC4Wq3vlQPNVIzbwUFHxl7x1Jzp7K63Vb3TfqD8I7BDnp-7JzGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1918a30d5e.mp4?token=sLOLlv4_wVdeulJu8YyLi19Bbp-dB49N-B8gjZRiogMtoxkLYFxv4RICjZU17zVDDzxQm3cv4Xrh-Xr0T7Qz6Wn4GRtQ8B2iXzecAfmBdH0aknJBq9IPQmGzricufT75bR7LGLv84ireNgIjL27qOppGgV8onaZ0OEZPV6Cfvs1FkBJkHEC_ylwXAKkxgY-7YkBGgMP4_XGp1MdQ2AczcVdcKSUhv48BhoqZ-9Qggj_nuIWvJIgjIzZ-l0SdlTD6BBzFh_Fnwrl_B4J3WH19wzbeij6nvKyrokuTC4Wq3vlQPNVIzbwUFHxl7x1Jzp7K63Vb3TfqD8I7BDnp-7JzGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره تنگه هرمز:
این یک آبراه بین‌المللی است. هیچ کشوری اجازه ندارد برای یک آبراه بین‌المللی عوارض یا هزینه دریافت کند.
این همان قانون بین‌المللی موجود است. در تمام آبراه‌های بین‌المللی در سراسر جهان همین‌طور عمل می‌شود و ما انتظار داریم که اینجا هم همین‌گونه باشد
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66740" target="_blank">📅 20:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66739">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=sQDfxnOhMfe2nhiYCd4dXgZ6laQ1K8O7f9Yh2hbTJSkiAv4wnYstVKLvm867WgOUZfeQhJCXANNL_snoSpBpkdENyyW2xARhTMH-rCnIo4ZKcSr5ggXbPHMde_4LOcRmzjizAW19f1nmqTmE_aSIqzyEcVWnkMhu_brFGYpPj4oo5cxeknnXVcoVPH8qs6mXNuvtlURimg0NkWtKb-pmqXM33ApQPo66ruApFI-nLlwOYuy55-GRidf_Lr6kuIt9oEXZfcLMRx0GQD9rdZVBtVN1l0-AT0JU8gqsYgJI8zRXpcnJI9T-TRq1ss5txZMkFBkcYzi0yiUEVUJXEZcybQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8deb9fca75.mp4?token=sQDfxnOhMfe2nhiYCd4dXgZ6laQ1K8O7f9Yh2hbTJSkiAv4wnYstVKLvm867WgOUZfeQhJCXANNL_snoSpBpkdENyyW2xARhTMH-rCnIo4ZKcSr5ggXbPHMde_4LOcRmzjizAW19f1nmqTmE_aSIqzyEcVWnkMhu_brFGYpPj4oo5cxeknnXVcoVPH8qs6mXNuvtlURimg0NkWtKb-pmqXM33ApQPo66ruApFI-nLlwOYuy55-GRidf_Lr6kuIt9oEXZfcLMRx0GQD9rdZVBtVN1l0-AT0JU8gqsYgJI8zRXpcnJI9T-TRq1ss5txZMkFBkcYzi0yiUEVUJXEZcybQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
تا زمانی که نیروهای نیابتی ایران از داخل عراق موشک‌ها و پهپادها را شلیک می‌کنند و در اقداماتی مانند تروریسمی که حماس و حزب‌الله انجام دادند مشارکت دارند، نمی‌توان به پایان خصومت‌ها و درگیری‌ها در منطقه رسید
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66739" target="_blank">📅 20:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66738">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=gaLD9c94WA3YqbKRzNEPEqy71-5ZkL9dRQ15i4ofyhwdCKdpvYE-TeZh4Adv1xmwFix-PaoF-qo84VCzKeUa6AgcgXfDHcxnkrn-PUHBClLSSqnYYUM07BIc7071QR4e_ZLCuS6EdPbq2sWCD_Tf0d0qVC1wPYTN7oDfvEAyRCFf_rtknID9DaCbVJM7d5PNcEMxN98Z647AsX5_q0Na8dx1s-inBLU8_BIV52t0U05jBDuoke6NVlwGnytCk57wzMM4v_gn23kr6FQ3K19NW4s16kKC0ssGXC-gsvIXutYHj-ojes6QNP_N9mhjhX7yr1m2LRI4GRlld20zc1G79Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28eade01e.mp4?token=gaLD9c94WA3YqbKRzNEPEqy71-5ZkL9dRQ15i4ofyhwdCKdpvYE-TeZh4Adv1xmwFix-PaoF-qo84VCzKeUa6AgcgXfDHcxnkrn-PUHBClLSSqnYYUM07BIc7071QR4e_ZLCuS6EdPbq2sWCD_Tf0d0qVC1wPYTN7oDfvEAyRCFf_rtknID9DaCbVJM7d5PNcEMxN98Z647AsX5_q0Na8dx1s-inBLU8_BIV52t0U05jBDuoke6NVlwGnytCk57wzMM4v_gn23kr6FQ3K19NW4s16kKC0ssGXC-gsvIXutYHj-ojes6QNP_N9mhjhX7yr1m2LRI4GRlld20zc1G79Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
اگر رهبری ج ا  تصمیم بگیرد که می‌خواهد یک کشور باشد، نه یک جنبش انقلابی که ترور صادر می‌کند، آن‌ها فرصت خواهند داشت کارهای فوق‌العاده‌ای در ایران انجام دهند.
این فرصت‌ها می‌تواند شامل سرمایه‌گذاری و سرمایه‌گذاری خارجی مستقیم باشد… این پول دولت ما نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66738" target="_blank">📅 20:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66737">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=V6_GHeLnsYV_ll4IW34q4M9K14mJ43zIqF46kUWYfEVPkF6DnIY0-ZYkX4x6zNqTtfWWuqGSdF74VeFbj2cmTy3cRpC92nOaONOYx-6lYSZz6PIdSKCiVOXxX7JcrgIeWSTB7trGuviHH01sXCzBdyjOmXLMAxgIrcWPmhKKb_HLlztJPiVzo0Q3RDhtV7t2BYnpwu9GfytVK5CGILfbA7pvtbBqerIILbzGeRbIiAwS3BeqIxUnYXQ5MsMMT-dy0FblplizVwAnMkSgvz4qhcLOKQ1ipF19HSQr3HyvHewC7XRIUA6R4Nej44PhtDvK_Z966q6fx0mnEZq2eV6POg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966e7cdc8b.mp4?token=V6_GHeLnsYV_ll4IW34q4M9K14mJ43zIqF46kUWYfEVPkF6DnIY0-ZYkX4x6zNqTtfWWuqGSdF74VeFbj2cmTy3cRpC92nOaONOYx-6lYSZz6PIdSKCiVOXxX7JcrgIeWSTB7trGuviHH01sXCzBdyjOmXLMAxgIrcWPmhKKb_HLlztJPiVzo0Q3RDhtV7t2BYnpwu9GfytVK5CGILfbA7pvtbBqerIILbzGeRbIiAwS3BeqIxUnYXQ5MsMMT-dy0FblplizVwAnMkSgvz4qhcLOKQ1ipF19HSQr3HyvHewC7XRIUA6R4Nej44PhtDvK_Z966q6fx0mnEZq2eV6POg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف، به پزشکیان:
لطفاً گرم‌ترین تحیت‌های خود را به مقام معظم رهبری، آیت‌الله مجتبی خامنه‌ای برسانید.به لطف رهبری ایشان، ایران توانسته است این تفاهم‌نامه را به دست آورد و در نتیجه، آتش‌بس را با کرامت و افتخار به دست آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66737" target="_blank">📅 20:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66736">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=OB0WWFV0oDCzX5xc5GGfd-XauQVZsqHczkVI9vdX1hFLSjONHvKbhqh0wPZt-fj94_XiFTw0dsAN-rVSt602H94GECtnAk4GGL6pHQu0pA9E-LFlTgSzFy8JBCfTqtYa3wfhaxW3Ww5Gg7vzXWG-IXdZR8KFZut01E8QZMJmI33puRm-aVlOoKQvmwyB6nTC3yJHDBG30OzkWDkWwonuyONzTmKChESbtHavN2GhKQGfQLWgcf8fApF326ZGkLMgU0XI7OooMXUSl0ZMNubxq27MbUVWhlHK9lssYEqzmu3ZvQXWW6IYI-1fNYnpGZ6h12SMeWZfMeTXLzR3OzBb_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcf82c8e4.mp4?token=OB0WWFV0oDCzX5xc5GGfd-XauQVZsqHczkVI9vdX1hFLSjONHvKbhqh0wPZt-fj94_XiFTw0dsAN-rVSt602H94GECtnAk4GGL6pHQu0pA9E-LFlTgSzFy8JBCfTqtYa3wfhaxW3Ww5Gg7vzXWG-IXdZR8KFZut01E8QZMJmI33puRm-aVlOoKQvmwyB6nTC3yJHDBG30OzkWDkWwonuyONzTmKChESbtHavN2GhKQGfQLWgcf8fApF326ZGkLMgU0XI7OooMXUSl0ZMNubxq27MbUVWhlHK9lssYEqzmu3ZvQXWW6IYI-1fNYnpGZ6h12SMeWZfMeTXLzR3OzBb_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهباز شریف:
این تفاهم‌نامه هیچ اشاره‌ای به موشک‌های بالستیک ندارد.
این موضوع هرگز روی میز نبود؛ هرگز در دستور کار قرار نداشت.
طرف ایرانی هم اصلاً نمی‌خواست درباره آن بحث کند
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66736" target="_blank">📅 20:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66735">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiFs74ajbVasdGLAxr111qmXHYO2xVyPm2EFvV37NaN4lvjCb5cMc0t1cgNYOwh860E5mNvK4yMcM1_YEizMfjfRf285RAmQ-M68Qo2zzXx8wSjA9cmKGThsM0b4UbaO8iZGhW_7Rm0qCE3gMHZU3HbGL3zBbu5pH8jyQhlffeq_mUPprRYClwzLNicml-xs1NUSzX4a6GiM5BeTIMd4UMRx_kWiJ6Pc430n2nDrkAgyCd_D8vUD3yRHcmv5q1TFGACQ2kp3nzGb7mkXsvJJK6XszclvLA-DT9TXzY4nfrg7I0JMmyZIct6HIFRbBDxHpwUWfHXz8IEJvjhu-iD1Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پسر پاسدار کشته شده علیرضا تنگسیری فرمانده سپاه که معلوم شده اینم طوری زدن که فقط یک دستش جا مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66735" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66734">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66734" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66733">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SwRi2F_pbqFquwHXFR095S0KVrww3-qeFISO7UvlzsWgbFrjKiRtbnbsYFVWxV4jgo86PR4ikH0UFYRxvMAF7oCcX_E0M0tygdjlSsmehQlJ1Cmm0PUlZyIZqxWOACCyPwHvsMS9tFH6crd10ousCsuCbPQcpfqz2oVZm5b5YEwSKaAgBf7STUJTk9gb2TP_UKXKZsN6YTFSAHRHXDCrvsh9lDLnb8WipL1GFQTwhBz_7u32FYr_zRTtz_e5rH6_bh4ECZtpdR6dWrwEA0MrWo3T4mQOqgfzQ521Kk9_lRlX-f1P9HAnhTT9TFm6KGagLzT6kWuLJ5fD_da6-x6A0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66733" target="_blank">📅 19:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66732">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=KGXb5jsNWeNSYGvgfDQ91C17efHQawsODnMXCwxXNjs2t5p4ub04_iyoUds2qV0c8IOr-nD1koup3Ltk7uDQfh-EKNt8uWNrp9eUGtJEqw9VQjmvmuOyq_LY71kwLLImjAJDf_y7O3LxapY0SpuoZn60DD6m1_J_9A656eSgQY17kxSu9enMsQMJSulRITQLpIKX0dVjI1EF31hLjX7hO90MpCHT-0Koml25BkFaRRMVqiJOPZkAGMHCTDbIkPmnVGlKeUied74X30yHWTU48jaBaLiAtD9D7AXYreeNUddmoMJuFb6bRXFbdkENRPyvuGWIiaJqXIRZ8LAco3oj7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=KGXb5jsNWeNSYGvgfDQ91C17efHQawsODnMXCwxXNjs2t5p4ub04_iyoUds2qV0c8IOr-nD1koup3Ltk7uDQfh-EKNt8uWNrp9eUGtJEqw9VQjmvmuOyq_LY71kwLLImjAJDf_y7O3LxapY0SpuoZn60DD6m1_J_9A656eSgQY17kxSu9enMsQMJSulRITQLpIKX0dVjI1EF31hLjX7hO90MpCHT-0Koml25BkFaRRMVqiJOPZkAGMHCTDbIkPmnVGlKeUied74X30yHWTU48jaBaLiAtD9D7AXYreeNUddmoMJuFb6bRXFbdkENRPyvuGWIiaJqXIRZ8LAco3oj7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیوی منتشر شده از عباس عراقچی و همتی که وسط مذاکرات با آمریکا پا شدن رفتن بازی ایران و بلژیکو تماشا کردن.
اینجا گفته بودن مذاکرات ترک میکنیم اما رفتن فوتبال ببینن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66732" target="_blank">📅 19:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66731">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=EeYcphVZYuX3zG_D4fOPiaDnoxyJZ11O8VR0fT2d4QjWAUerptr6h8NDyS-DnuF8JpRwXiVgtEaBaUPgiGmH9IbEO7ybRI6cKfI2TU4o83daXNvcP5H9iIBMAI69pNkK204VW7I3DLGfaXRqcSJ5d0dNE_chlEURKT2R9f2T_OSBsU6uu1HvqqtSIcOgh0DFdF8ElrJnZOjmtPKNqCjoL3CYHW7BdTuYSWg5L5XEQqJBG7zPtCHFyBaH2lHm3cUYfBd6qSqCSVjDy5Aq957_PU35C11TcXjjO22i5uRyBkGdpna9x7NV4G3Swrd8iDRWgUIUVUGdj0xXwmtdbgzb9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df51f5307d.mp4?token=EeYcphVZYuX3zG_D4fOPiaDnoxyJZ11O8VR0fT2d4QjWAUerptr6h8NDyS-DnuF8JpRwXiVgtEaBaUPgiGmH9IbEO7ybRI6cKfI2TU4o83daXNvcP5H9iIBMAI69pNkK204VW7I3DLGfaXRqcSJ5d0dNE_chlEURKT2R9f2T_OSBsU6uu1HvqqtSIcOgh0DFdF8ElrJnZOjmtPKNqCjoL3CYHW7BdTuYSWg5L5XEQqJBG7zPtCHFyBaH2lHm3cUYfBd6qSqCSVjDy5Aq957_PU35C11TcXjjO22i5uRyBkGdpna9x7NV4G3Swrd8iDRWgUIUVUGdj0xXwmtdbgzb9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روحانی : اسم بچه‌هاتون رو امیر نزارید، ریشه این اسم بهایی هست
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66731" target="_blank">📅 18:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66730">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9028c70792.mp4?token=twam4DUEAD6fot0jps0yvHg8z9Sf53SQEY7xRkP5AhWgL1G9h_WAx3sHJL46Bv_0x2v6bHZPnt4YKhXM-WamX60YVItrDYr-47GvcQfM6ehqEDq25WW99pSX9n90ep62M0PaU0jJtqMLBRXKNWjvoF_94veIqgGD0FMXoWNsitJBV6MrWXU7_8mKWjFiqfon0G9IgnnGzetP__buLgyyxfDaPHahOrSsY-a2e1ElAtvjd5_qUUlR24tlJG2wbD3t_b2LvwL5CV0kelcdUGtBGiHMXLjpyNxmyW4a36xwtOX2SWdkdGjtisJY5JJcKN4TKAEUfSQF2tXTbjjrj2cjiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9028c70792.mp4?token=twam4DUEAD6fot0jps0yvHg8z9Sf53SQEY7xRkP5AhWgL1G9h_WAx3sHJL46Bv_0x2v6bHZPnt4YKhXM-WamX60YVItrDYr-47GvcQfM6ehqEDq25WW99pSX9n90ep62M0PaU0jJtqMLBRXKNWjvoF_94veIqgGD0FMXoWNsitJBV6MrWXU7_8mKWjFiqfon0G9IgnnGzetP__buLgyyxfDaPHahOrSsY-a2e1ElAtvjd5_qUUlR24tlJG2wbD3t_b2LvwL5CV0kelcdUGtBGiHMXLjpyNxmyW4a36xwtOX2SWdkdGjtisJY5JJcKN4TKAEUfSQF2tXTbjjrj2cjiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ثابتی:مذاکرات به رهبری تحمیل شد وگرنه نظرشون چیز دیگه ای بود
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66730" target="_blank">📅 18:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66729">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=gDEZNTiDCzWVQLX4gyWJqRbAIxsl_5wIhUddDv8EA_5WaAg0gwaF2I7Pm7pvfNqrttoaXB30LXdxJayQE6-EPEdcZfZpPIw-53jBWC2_KM66a4xO4ojCdp7tdm49lwuzXM3-zdbbJrr3adZgm2yr5P8ebDbZTDOVqheococzeAzmkG0UQCFr7HcKerzL-7btTAyzjik24T8WN3tVoVcx5vOZc5bzeV-5NxhOwIF5hnvKic-UQV4Fe77I4X4WyP88POWhx7rWvNiFNOCOrKWR3boghkfnY9r5nZs_7tXJni9karSyH35klG74HW58Uw73Nfpd0HuUWWXbxxSEejEH1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed1cc8a0c1.mp4?token=gDEZNTiDCzWVQLX4gyWJqRbAIxsl_5wIhUddDv8EA_5WaAg0gwaF2I7Pm7pvfNqrttoaXB30LXdxJayQE6-EPEdcZfZpPIw-53jBWC2_KM66a4xO4ojCdp7tdm49lwuzXM3-zdbbJrr3adZgm2yr5P8ebDbZTDOVqheococzeAzmkG0UQCFr7HcKerzL-7btTAyzjik24T8WN3tVoVcx5vOZc5bzeV-5NxhOwIF5hnvKic-UQV4Fe77I4X4WyP88POWhx7rWvNiFNOCOrKWR3boghkfnY9r5nZs_7tXJni9karSyH35klG74HW58Uw73Nfpd0HuUWWXbxxSEejEH1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد مجری صداوسیما از رفتن قالیباف به مذاکرات
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66729" target="_blank">📅 17:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66728">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRgyaEVezT98QIEmaJaSj4Gs9LWW0bHHCWRcypUohhRBeJ7OoNGiscApndS5cgEOHYudRve0BLwXfRznnLsnJENXp76gkbS1pslI0ps4O2Fr3jYPpdMOYG_8b8_06SIIRTdvvZHwS__asUVNyJBGGtG25UbUnDY23WzncEFe4OkNy0auohYN8Uf646fu-OBwjTaX4rjeqhvr3Zbqk04gGY65wT2yE93RfcDxlHPj7ejCeNOV8Z628cw2qkIryW9tt_p8N3niao6zT0AstaLvRoJT3N3JJ_CN-1fXI9oafGejxT5DRcfFbVK32B-ezviKiDgQ82EOq4x_r6WTyjvF2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آناتولی گزارش داده که شهباز شریف گفته قراره درباره برنامه موشکی جمهوری اسلامی هم  مذاکره بشه
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66728" target="_blank">📅 16:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66727">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfcvH1WnhI6DlCksnbb_Q1iW67aUgGdaGs0hxUITWVETKcs0roRXFk7lLvhXLCCI5BQaf385xlZP1ZErWxF21RFb5SXu-UajsxpW1TJSyfq-3w1KOvULw34HEFuEHpO1PiK5GDnL8xraOegnlLg_fyCZoSZOT2KUcLQcvYVfg2aTkW9svWynzDN4GKGIb99ymMqgD7lWFLiPnw4_n99yuTC5zhUQ4Xx-GpNOH8tN9JEOymVpek-Ukhj6FwnJYuAkxl5r-eBosF1-Ilk7PbljF2PVyD_-Zfp78bmvErRAP91v87bJuvIPOhmRvp7KI06PnY7fk_-13JeBCN80q2JUMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ورود عاشقانه مسعود به پاکستان
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66727" target="_blank">📅 15:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66726">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N98PpOC0JFjMR-ah4glBzzw_P31EzKow54D5xzhbBKANMtkj52PpspupXJ0zBk17mIovxYxr788hy8fH_mEC3YpQISAsq8_pGrsYA4OO-hajY-vMhY5zdAjCa2Rsw2dSpYzKqhg9EVREezNRuPTZN9e0foZx0jdnCCFWy2o2fcxjAyxQz81Xnvx1lx3iz-wsVM1qRWZYmxXhLvqP5ZpcaFPDq4pNA3qKnE9LHw-tcETuw0u2mtb1fi7PiYApW24Sy3HMUCd4m_4dJSUeEWR9RZvA2LJLjwxc5ZfA5GPVOvOsTsDPLnsGnVfg_BYDTs0WTfW-Qfu4XJ9h1BmbnolnVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«با وجود اعتراض‌ها و اظهارات نادرست آن‌ها بر خلاف واقع، و همچنین هیاهوی مداوم رسانه‌های جعلی که تمام تلاش خود را می‌کنند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهند، ایران به طور کامل و بدون هیچ ابهامی با بازرسی‌های هسته‌ای در بالاترین سطح و برای مدت بسیار طولانی در آینده (تا بی‌نهایت!!!) موافقت کرده است. این امر “صداقت هسته‌ای” را تضمین خواهد کرد.
اگر آن‌ها با این موضوع موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای در کار نبود! بر اساس این توافق و دیگر امتیازات مهمی که ایران در حال ارائه آن‌هاست، من موافقت کرده‌ام که تنگه هرمز باز بماند و هیچ محاصره دریایی دیگری اعمال نشود.
با این حال، تمام کشتی‌ها در جای خود باقی خواهند ماند تا در صورت لزوم محاصره دوباره برقرار شود؛ هرچند در این مقطع چنین چیزی بسیار بعید به نظر می‌رسد.
پول‌ها و/یا منابعی که وزارت خزانه‌داری آمریکا آزاد می‌کند، در یک حساب امانی (Escrow) تحت کنترل ایالات متحده نگهداری خواهد شد و صرفاً برای خرید مواد غذایی و تجهیزات پزشکی از خود آمریکا استفاده خواهد شد؛ از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما. ایران به شدت به این اقلام نیاز دارد.
این یک بحران انسانی است و من احساس می‌کنم که لازم است همین حالا کمک کنیم، پیش از آنکه خیلی دیر شود.
گفت‌وگوها به خوبی پیش می‌رود!
از توجه شما به این موضوع سپاسگزارم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66726" target="_blank">📅 15:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66725">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e35e4556.mp4?token=Smi48wkfEiwOBvXB3GcYX87oj9uKkZwoGJ5U_CaDgGsQJyYFsW-yO4A4FmY1VI6uxR1zH_vhY78HdGBXYu5trP4eUYix7tWt34_0_bl7PM1OlCtmts2yIAEhsLH6aHeLtK4hzlwuqQynr0DHiNdJ8Rsc_-1ANRBCchoAusnGDaOMFb6louqNQNfiKgBjfqNV7GwAxg4Asn_G5VdearDpkvl5dLL6IFI1-_zu8vT0lC3HADKeuSIx73jxBAZ_mc2ZxuNR_5VWbyrtUWA99-Di1aPbSbSgvToHHDpUtPJpPSuzUV2zodAjuXqc1VVk7OjKKhAoi9VEEzrwc2k9isoe_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e35e4556.mp4?token=Smi48wkfEiwOBvXB3GcYX87oj9uKkZwoGJ5U_CaDgGsQJyYFsW-yO4A4FmY1VI6uxR1zH_vhY78HdGBXYu5trP4eUYix7tWt34_0_bl7PM1OlCtmts2yIAEhsLH6aHeLtK4hzlwuqQynr0DHiNdJ8Rsc_-1ANRBCchoAusnGDaOMFb6louqNQNfiKgBjfqNV7GwAxg4Asn_G5VdearDpkvl5dLL6IFI1-_zu8vT0lC3HADKeuSIx73jxBAZ_mc2ZxuNR_5VWbyrtUWA99-Di1aPbSbSgvToHHDpUtPJpPSuzUV2zodAjuXqc1VVk7OjKKhAoi9VEEzrwc2k9isoe_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
‼️
ارتش اسرائیل در نبطیه الفوقا به افرادی مسلح که در نزدیکی نیروهای این کشور شناسایی شده بودند حمله کرد. بر اساس گزارش‌ها، ۲ نفر کشته و ۲ نفر دیگر زخمی شدند. این نخستین حمله ارتش اسرائیل به لبنان پس از ۳ شبانه روز بدون هیچ حمله‌ای در این جبهه محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66725" target="_blank">📅 14:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66723">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=a0NkFbeTzpVHfKPU2EaJ1fq3BgYeAWQjGb_OzlpQQ-4CfoCX9r-4SoHGdFvXsbKEXLNUBFLVMi7RM4dp9bsaYUrZoBUUdzQKztCNWKM6PwTxI_2NuU3zdtj5R3UQQsRxdKdvvyczQtsz7plI4WzuFC6XTfRe1jLECFOikSR70qhcjOfbkuVQaa1gSif2RfiurHtPM-3pNAGJ4e8_2D5_mzaXjyV7qitPzFfGfdhzaJFEkcr4x79CsxDURxjV2fwnhDEKLd-ePHbZ9YRh_HhuNlHc0Z2GoXevx-j99nzXbY7z6NocM3Y2Tss0aCcD8ejUaFKZk7PSsN1kW0fSC9FE5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f0020b71c.mp4?token=a0NkFbeTzpVHfKPU2EaJ1fq3BgYeAWQjGb_OzlpQQ-4CfoCX9r-4SoHGdFvXsbKEXLNUBFLVMi7RM4dp9bsaYUrZoBUUdzQKztCNWKM6PwTxI_2NuU3zdtj5R3UQQsRxdKdvvyczQtsz7plI4WzuFC6XTfRe1jLECFOikSR70qhcjOfbkuVQaa1gSif2RfiurHtPM-3pNAGJ4e8_2D5_mzaXjyV7qitPzFfGfdhzaJFEkcr4x79CsxDURxjV2fwnhDEKLd-ePHbZ9YRh_HhuNlHc0Z2GoXevx-j99nzXbY7z6NocM3Y2Tss0aCcD8ejUaFKZk7PSsN1kW0fSC9FE5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اوکراین یک پل حیاتی را که به ارتش روسیه کمک می‌کند تا تدارکات را به نیروهای مبارز در منطقه اشغالی زاپوریژیا منتقل کند، تخریب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66723" target="_blank">📅 13:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66721">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/py-Rjj5j1mYgESD0RkHTMumc64f8gOhdQ6zT2CF88S79ZZ2rkFi6cRQgt7wwcb99DYo8sMTl2QoeDT1Sr9JxPAimUK9q6_tACTmEpYYoeq_QX2jOlK-UoNRe4WaSWelisN42c5i0uroAZ1TwiClVPiWyrYjK10SmPtOzn6SX4FzPSR5QoPfOildUpEx9NV-3JJAk-Hu6aNpOhHFcOxyTVTsihqnMc_8ImVWmw88K2ZYev5eFEwjKWzTRJfrD6abTaY4lu8bgrXKeHAxyRXcC0BkohuN0my75jxKuv2F5UOMHCIAogRl7Pka_4pTdiNChp7xCqxZ-6UeG7lYyfqeZ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
اثربخشی مذاکرات به پایبندی کامل به تعهدات توافق‌شده و اجرای دقیق آنها بستگی دارد. پیشرفت در این مسیر با پایبندی عملی به مسئولیت‌های پذیرفته‌شده سنجیده خواهد شد. اظهارات خارج از متن توافق‌شده کمکی به پیشرفت مذاکرات نمی‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66721" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66720">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66720" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66720" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66719">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=oMOsezwkdlGrwvyOpEGM5jYLxvzody0zCuNQNwwXSBKa48hWURl72P6CQsyhOx3nbpgWHITruHD0LmFrk96CRQDjB5uVhZ93Jhtw62NTiB-_OlXUGy5LuUjjHeSYZhhMe_2X5G38faEVY-nMg1D3jEsgfFzL2kTkexli1n1pJcdnN6pQW_NSoeLZyRGRukQNtMfUVXii7cJ8Wdijr32xPB64dj0NyKCuNqbPAbXdsROsJWNx6SxrdRlyB5qIBDkOnb78sIn5EpOIy9qd89soR2kiS3j-_jqFYdJ0zNvc9U94LNRZqKHSRHrLhZ6cdaI_IdQyRYLO5aTVZ44refqIK2192mt4jqCEqx6Ed0tVwLP9qDhCpzFlZmUHk9AOT-9siBC6Jdp-VQLtK8fLlxUtPtbHT67ZWZ23-PUDy7IFfgjQRzbKOAhBCTgHvhgL1FDz54BcP2GpZEx14a0h1AfKwiQEX9CNJcvA0GMun78gWjT2n4h_e3j-0GxwR7Te6meNdRV1BkGxmId6c9aekceAuRp8aQO8o_67gQnGJXoGkVwbP5RiV3tudmpNEKIXyLuTVFyzrqNRj4zbSLrfvVQA37m44u_SmdLiHFCSiB66WGrqR8Aiu_lKza1iytgIXVZm3DB8kaQKMgTQpnKate5jxQeUGzORK4q2ESiO6MOZdoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=oMOsezwkdlGrwvyOpEGM5jYLxvzody0zCuNQNwwXSBKa48hWURl72P6CQsyhOx3nbpgWHITruHD0LmFrk96CRQDjB5uVhZ93Jhtw62NTiB-_OlXUGy5LuUjjHeSYZhhMe_2X5G38faEVY-nMg1D3jEsgfFzL2kTkexli1n1pJcdnN6pQW_NSoeLZyRGRukQNtMfUVXii7cJ8Wdijr32xPB64dj0NyKCuNqbPAbXdsROsJWNx6SxrdRlyB5qIBDkOnb78sIn5EpOIy9qd89soR2kiS3j-_jqFYdJ0zNvc9U94LNRZqKHSRHrLhZ6cdaI_IdQyRYLO5aTVZ44refqIK2192mt4jqCEqx6Ed0tVwLP9qDhCpzFlZmUHk9AOT-9siBC6Jdp-VQLtK8fLlxUtPtbHT67ZWZ23-PUDy7IFfgjQRzbKOAhBCTgHvhgL1FDz54BcP2GpZEx14a0h1AfKwiQEX9CNJcvA0GMun78gWjT2n4h_e3j-0GxwR7Te6meNdRV1BkGxmId6c9aekceAuRp8aQO8o_67gQnGJXoGkVwbP5RiV3tudmpNEKIXyLuTVFyzrqNRj4zbSLrfvVQA37m44u_SmdLiHFCSiB66WGrqR8Aiu_lKza1iytgIXVZm3DB8kaQKMgTQpnKate5jxQeUGzORK4q2ESiO6MOZdoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66719" target="_blank">📅 13:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66715">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=siaKbSAmX0RJEeZ2DbsrnAedsSqOllhkgjGCujPV-osnoHzkT0pus7XbjyIC4nxFOCOF5hPDtywMrqdcd08rWV9Ch7-kJsikS6MUsFORbfA2wCvWeyk7Di5NKKwOccTvms-1HbzZOa3Al69-k2zOZlRby8QHi_nOKnUJTTQfnGezROZDZN5AWO8F9UFMNwuWTGeWks4N0x07Mu7WmXDYbJoIQhpV5ibr8eXdP6sBPbaI6NNRr1ZFV-OQs2R96aWmoZVPZJuUPhGWaFW6RK5QoQi88Kqp-ncMbdf-ij0KbT9qXcNQiwQQm_cUHh0im_EfS0wjWy0-7S7SiINRe-ytKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a715ded5e6.mp4?token=siaKbSAmX0RJEeZ2DbsrnAedsSqOllhkgjGCujPV-osnoHzkT0pus7XbjyIC4nxFOCOF5hPDtywMrqdcd08rWV9Ch7-kJsikS6MUsFORbfA2wCvWeyk7Di5NKKwOccTvms-1HbzZOa3Al69-k2zOZlRby8QHi_nOKnUJTTQfnGezROZDZN5AWO8F9UFMNwuWTGeWks4N0x07Mu7WmXDYbJoIQhpV5ibr8eXdP6sBPbaI6NNRr1ZFV-OQs2R96aWmoZVPZJuUPhGWaFW6RK5QoQi88Kqp-ncMbdf-ij0KbT9qXcNQiwQQm_cUHh0im_EfS0wjWy0-7S7SiINRe-ytKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نخست‌وزیر قطر در گفت‌وگو با الجزیره:
این نخستین بار نیست که نخست‌وزیر اسرائیل با ادامه اشغالگری، گسترش حضور در مناطق لبنان و سوریه، خودداری از پایبندی به خروج از نوار غزه و همچنین عمل نکردن به تعهدات مربوط به توافق‌ها، موجب تشدید تنش در منطقه شده است.»
اقدامات دولت اسرائیل بارها به افزایش تنش‌ها و بی‌ثباتی در منطقه منجر شده و اجرای تعهدات و توافق‌های پیشین همچنان با چالش روبه‌رو است
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66715" target="_blank">📅 12:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66714">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=TfXZDxvb95WlTLItHcMlS9MSW2NJymBL9LUJRR_BH2XzD3mIBcSeOW5UzHG3ZxGqILuDRVBDYzpxMJVogaMmzxhZcNgakACmFLGiJjJynz9imwbuMdOI9Er9YrUZECydyOF3wW9qzWrx5dTGiY8E38uD1dBNlMDnePjTVgpK2TH515p3kYoDfG9r3Olu_gT4OiKMBDWt3QqoqWKsTYyO6l-kOwfChdrTk91M-BUqYLDfIGIjSrlpv8cMR-ipDLqTh4kLXqA3WE4-2fvs7vElfTlFYRrNCoXRthUfalBpiB0OLnoCDztuMts7mwaYcrGfzHVkqz2c_N40nsiO4HScjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71cf4b742.mp4?token=TfXZDxvb95WlTLItHcMlS9MSW2NJymBL9LUJRR_BH2XzD3mIBcSeOW5UzHG3ZxGqILuDRVBDYzpxMJVogaMmzxhZcNgakACmFLGiJjJynz9imwbuMdOI9Er9YrUZECydyOF3wW9qzWrx5dTGiY8E38uD1dBNlMDnePjTVgpK2TH515p3kYoDfG9r3Olu_gT4OiKMBDWt3QqoqWKsTYyO6l-kOwfChdrTk91M-BUqYLDfIGIjSrlpv8cMR-ipDLqTh4kLXqA3WE4-2fvs7vElfTlFYRrNCoXRthUfalBpiB0OLnoCDztuMts7mwaYcrGfzHVkqz2c_N40nsiO4HScjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسایی:
قالیباف و سایر اعضای هیات رئیسه باید پاسخگوی چرایی تعطیلی مجلس باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66714" target="_blank">📅 11:30 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
