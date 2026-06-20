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
<img src="https://cdn4.telesco.pe/file/ohJkvxcbBl1svpoh22ptzIfbPgMl0XMzaWEmrgsnZJpNTCho_HFgis0_dxAbh3Y2ik5ra_6q4R82w0G5X_lEXfsI6FBzaDDr-iWzY98DJLGisDiRf60yITCO8Y23QuXs07LIvJNJAhJArDVCpDaUtvHmk3xm-IUlIMU6dv5z2Bj6lTU59IOBsdUAQgEpIZabcT234PBD4LTbLb0Kr5lQTqNS169P_I_l8enRSHcgAOfKXvIAHjbYmXeVVyor4C25gJhOrbN7m177UJIN8TcIgIMTu7Lcn52Nefzy8412r1EZdgBPLdI2UKl_zfvwkULqxea8V3CUxtKjJNwF7BZd6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 222K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 03:31:43</div>
<hr>

<div class="tg-post" id="msg-66534">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
🔴
فقط نظاره گر فوتبال نباش پیش بینی کن و پول دربیار
💵
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/news_hut/66534" target="_blank">📅 01:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66533">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUqoJ4iOUxQuTDI9k3DMWqxSXpL0MHJjL1pV4eQiOz66lUWSwE1AmTCXK9Q6tB5gHtFCfxGPYj4MBdhO4FcX6TFQFSJSLt3q6vH6fSdBm0q7-Rf9KLcYVXYrMm0rJrgtSUht7kPeLLfcNTy58ng2RYM6Soteui2HhxCKOguB445Be9dVVRAkIHaqfMN_M1OvpzvavVQztecC03tmk0VMjZ0LBsOJLkuUUMUAshLzp7B21ihP4kk3ExW8KDGzjun9txMjL6hVTSpe_NOVkHgT46gWPR86zcgNN40iOb9E85Fnv4TY1tUcJrVzFNmKgqYPSThYNGIg44B1V67IUdYWLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/news_hut/66533" target="_blank">📅 01:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66532">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb104aecb9.mp4?token=NOoE_K6gSOZbFGFlQRl8hvZTi9Qw-43OKUbZEMtPx54VHHYdmZQminRSmKTRLrMVudwarKAuIY4Qgs2Zo1bO9ryTtFCCNUo-vN4iUibdwXCNlalBa8COcz9XNyLy1eNyeEg_F30wwTH7-0dEUCtkKZUhPpiST-M5SSQbIzzJ7r75v76vXgIh0LPJ7hQnusb_BIiz6wD1DwC6glb1bLzlBRRsO1_GZey9ZaX_Jf23DHKekVEPPHDT4wc-j2Ny_sQYhzJ7ASARVwLhlPDJNy6tbF2SIHRbem1wXYZ1YNca0JVaTdpacEwEko3N2xWuE-Xpxz-em8J9IyDNxDXkgOQK4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb104aecb9.mp4?token=NOoE_K6gSOZbFGFlQRl8hvZTi9Qw-43OKUbZEMtPx54VHHYdmZQminRSmKTRLrMVudwarKAuIY4Qgs2Zo1bO9ryTtFCCNUo-vN4iUibdwXCNlalBa8COcz9XNyLy1eNyeEg_F30wwTH7-0dEUCtkKZUhPpiST-M5SSQbIzzJ7r75v76vXgIh0LPJ7hQnusb_BIiz6wD1DwC6glb1bLzlBRRsO1_GZey9ZaX_Jf23DHKekVEPPHDT4wc-j2Ny_sQYhzJ7ASARVwLhlPDJNy6tbF2SIHRbem1wXYZ1YNca0JVaTdpacEwEko3N2xWuE-Xpxz-em8J9IyDNxDXkgOQK4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هم اکنون شیرینی آتش‌بس در لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/news_hut/66532" target="_blank">📅 00:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66531">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d8d08f74c.mp4?token=hkfBz-zGtSfbvRuxM7kWiQPtZro56VDtwpUAJ4QPcC6Mntv5ymBHtXYNtQpazr1t2mivUaCdI4FRfR_GU4wiDs4RWz5XJhHHioABysseZTcIjuRzLHiagtFJNuTkVcozEz9SHWtcXJIbQPLDsONbgYqMSiY8qg33_sK7zYpY2nNk8Iic_393au1wbnJj_1Zi58NLvdccGKErMvWT7dW2mS1FxNJn94a_3pSwcvsbYW1OYvZYfnZ2jswXcR0iSy_-ZoL1IVtnH8DoT-9HBE8eKz7rH1ObfYo1OVGTL-41l8TlSSkVGrsQJ049LyaudXuVtFLdYl_WjCoXidaYPdDWzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d8d08f74c.mp4?token=hkfBz-zGtSfbvRuxM7kWiQPtZro56VDtwpUAJ4QPcC6Mntv5ymBHtXYNtQpazr1t2mivUaCdI4FRfR_GU4wiDs4RWz5XJhHHioABysseZTcIjuRzLHiagtFJNuTkVcozEz9SHWtcXJIbQPLDsONbgYqMSiY8qg33_sK7zYpY2nNk8Iic_393au1wbnJj_1Zi58NLvdccGKErMvWT7dW2mS1FxNJn94a_3pSwcvsbYW1OYvZYfnZ2jswXcR0iSy_-ZoL1IVtnH8DoT-9HBE8eKz7rH1ObfYo1OVGTL-41l8TlSSkVGrsQJ049LyaudXuVtFLdYl_WjCoXidaYPdDWzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت پزشکیان
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/66531" target="_blank">📅 00:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66530">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21fdcbfae8.mp4?token=tM3nc8jODxvczAHNyyUZbU4ecAsazZIOkSnDW_tOW_T42riGwtPYp9e7Gu67vLO0rhLtJmbUiEgcHNEPdr9-VITh6IRtXISRQDDciwOAOvOZ2UW5k3SXwrEudgk5XUtCjBeoYIcfaEl8m8lYCkAu_FwZWEStcBTMWOenpjNwytj_rYqbecCQIlPdiU-jOktn602exo6bGRe2ZZoR7ZLVkWsRK73tIjkzGetD1mtEMbKPqVjA0m1sBMpbJwp-b4Mft7PXn2PnJGQAmMNM0iByovpGeLl4a6eXhzG6AN6TYNNHProhoGzQ6i5lAXu-kM0_oOVIJ2aXtCui4KCNkWaPYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21fdcbfae8.mp4?token=tM3nc8jODxvczAHNyyUZbU4ecAsazZIOkSnDW_tOW_T42riGwtPYp9e7Gu67vLO0rhLtJmbUiEgcHNEPdr9-VITh6IRtXISRQDDciwOAOvOZ2UW5k3SXwrEudgk5XUtCjBeoYIcfaEl8m8lYCkAu_FwZWEStcBTMWOenpjNwytj_rYqbecCQIlPdiU-jOktn602exo6bGRe2ZZoR7ZLVkWsRK73tIjkzGetD1mtEMbKPqVjA0m1sBMpbJwp-b4Mft7PXn2PnJGQAmMNM0iByovpGeLl4a6eXhzG6AN6TYNNHProhoGzQ6i5lAXu-kM0_oOVIJ2aXtCui4KCNkWaPYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد بایدن:
ما مردی داشتیم که نمی‌توانست از پله‌ها بالا برود، و من نمی‌خواهم در مورد این صحبت کنم چون اگر کمی زمین بخورم، می‌گویند: «اوه، این وحشتناک است.»
باشه، می‌تواند اتفاق بیفتد.
اما شما نمی‌توانید هر بار که روی صحنه می‌روید، زمین بخورید.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/66530" target="_blank">📅 23:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66529">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5871cd20e4.mp4?token=IwrTUkyt-LyXeU_S4_zZqlbuMxhy-Z8UBt6c5tE4OlLvRMlFUJQrHlIYFemEqsqlo0F8_u0NueqPNNjG-AyXXQenx-q34eghUFIY7agZ7GJMxrL0qpufmVUcq8EoijBj79t854b-NMVP6mMCtCUqyrBiWY7QwpkTqRlmsyeb8AotVFJkzOG_J8jBAhSoXxvcK85stEqoQLky6wTa3qhzpieJlMWfjRNfyEh0IFTGQUwpF-ET-zMV4NJmWE1XNzVr7IW_jW9azdpiGs6DFBgNiM9o0xzteN64e_JeDjJE0VU_LsbE--1GSrHpFC4BlRGvrmVY6A0WO9grdC_c-RpgJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5871cd20e4.mp4?token=IwrTUkyt-LyXeU_S4_zZqlbuMxhy-Z8UBt6c5tE4OlLvRMlFUJQrHlIYFemEqsqlo0F8_u0NueqPNNjG-AyXXQenx-q34eghUFIY7agZ7GJMxrL0qpufmVUcq8EoijBj79t854b-NMVP6mMCtCUqyrBiWY7QwpkTqRlmsyeb8AotVFJkzOG_J8jBAhSoXxvcK85stEqoQLky6wTa3qhzpieJlMWfjRNfyEh0IFTGQUwpF-ET-zMV4NJmWE1XNzVr7IW_jW9azdpiGs6DFBgNiM9o0xzteN64e_JeDjJE0VU_LsbE--1GSrHpFC4BlRGvrmVY6A0WO9grdC_c-RpgJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت
ترامپ در مورد ایران:
من بزرگترین پل آنها را خراب کردم چون آنها دیر به جلسه آمدند. آنها گفتند که این خیلی خوب نیست.
آن پل، این پل جورج واشنگتن آنهاست. من آن را در سه دقیقه از بین بردم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/66529" target="_blank">📅 23:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66528">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e43d6d5b.mp4?token=b7gfrBqAKQ-Q5gaj2qefWY0zfMDE_OksJytD9fD0VaR9BcdLThEpi36m-b2tuYAXTDdXo_mT_RHNYQX5hpRzmBR7O50vJsHmxlibK8A5tj1PryaSz53leaFWRUti6n_-7ysgB_L8iU-7pElulqB6F__Lo4-KtxLXWm9dwCRx-D3t85mMF2yXha4IjSnN3uQRst8JmGQwEoF4c04Y774vO4GWrZXitbEGOLR2eiVaHynXXbohnQN58CgqdPUyeej1emoi0wKs16YHsGVkyFp0wjQ8QbDT8ykFAnEakNiXM9qAu4rQI_Pnzr3AnF7jd6VJusIYXiGbrXkXRZ2nh1LFKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e43d6d5b.mp4?token=b7gfrBqAKQ-Q5gaj2qefWY0zfMDE_OksJytD9fD0VaR9BcdLThEpi36m-b2tuYAXTDdXo_mT_RHNYQX5hpRzmBR7O50vJsHmxlibK8A5tj1PryaSz53leaFWRUti6n_-7ysgB_L8iU-7pElulqB6F__Lo4-KtxLXWm9dwCRx-D3t85mMF2yXha4IjSnN3uQRst8JmGQwEoF4c04Y774vO4GWrZXitbEGOLR2eiVaHynXXbohnQN58CgqdPUyeej1emoi0wKs16YHsGVkyFp0wjQ8QbDT8ykFAnEakNiXM9qAu4rQI_Pnzr3AnF7jd6VJusIYXiGbrXkXRZ2nh1LFKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگر همین حالا به آن‌ها حمله می‌کردم—در حالی که ما قرار نیست نیروی زمینی بفرستیم، و شما هم نیروی زمینی نمی‌خواهید، درست است؟
اگر نیروی زمینی نفرستیم، احتمالاً همان افراد به اعماق غارها می‌روند. به آن‌ها “غارهای گرانیتی” می‌گویند. آن‌ها بسیار مستحکم هستند.
آن‌ها خیلی عمیق می‌روند، و بعد وقتی ما متوقف شویم، بیرون می‌آیند و احتمالاً همان رهبران قبلی خواهند بود.
در حال حاضر تنگه هرمز کاملاً بسته شده بود.
پر از مین می‌شد و موشک‌ها از بالای کشتی‌های میلیارددلاری عبور می‌کردند. آن کشتی‌ها دیگر هرگز عبور نمی‌کردند.
ما برای ماه‌ها نفت نداشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/66528" target="_blank">📅 23:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66527">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7522060f48.mp4?token=MTHfaxlGCssuos9k2MAgOgonjB7TufQ26ifK7QgdZG3mwdetwbAFBp9-6pJUd7zrKYyCdBb9lxGSnP5T65ugzsEHEZf3Z8fYy9lSiiu6v4UbsQN6r1HfJa15NwbC4hBwwzX2R91HDfMcCc0ZDLVaspmN_Kw9F7DxSmK9VvqgK4qalHxs9JFK3ZrSF02UgtXh7jIA611aHrztaBTAKyzAuRTJCm256_IC0OYo-m5k7C9W9l0WW_TPab-EUOpcDno7KKvDddSoEsL_5bMgv5xM4YEIlw3x_oJVafKRX01fTNb4TZSd2fioYCKvOiTmVHdeD9wntEJgc6NHO-5rDsA0dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7522060f48.mp4?token=MTHfaxlGCssuos9k2MAgOgonjB7TufQ26ifK7QgdZG3mwdetwbAFBp9-6pJUd7zrKYyCdBb9lxGSnP5T65ugzsEHEZf3Z8fYy9lSiiu6v4UbsQN6r1HfJa15NwbC4hBwwzX2R91HDfMcCc0ZDLVaspmN_Kw9F7DxSmK9VvqgK4qalHxs9JFK3ZrSF02UgtXh7jIA611aHrztaBTAKyzAuRTJCm256_IC0OYo-m5k7C9W9l0WW_TPab-EUOpcDno7KKvDddSoEsL_5bMgv5xM4YEIlw3x_oJVafKRX01fTNb4TZSd2fioYCKvOiTmVHdeD9wntEJgc6NHO-5rDsA0dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آتش‌سوزی کلیسا در خیابان بوشویک در بروکلین
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/66527" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66526">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2baf2d277c.mp4?token=OR6nQOY7uTzlOpYyZDyRRt3pcdv1G49NH8bwqnxTpBuXRHq19dG81T6bIQhHGkHeeIUes_CWJIqAsyLo9SS93vDfRGAXcYu1rqfoWtTPmO1gyYSBYf0vjb1bQpy2u6ziPqyDFqHhOUBUAQ8liqqFW3hcaQwv4yg4No0yfEc77Nt7L52h3F2HHzyUomq0Horihr1VwqZTXyEtdzphbB-zvNxTS-TQGQFt8lawxh1Z5H0axryJ5Z2oILzTm1sLkMZ6UAxw1Owxyw8qy9NarIElhEAHClB0-FUFX_4XdQ1_08j3iSATOIUlikj1hHWeEIgYr2T4sFZCXlfZt2dyMNkrbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2baf2d277c.mp4?token=OR6nQOY7uTzlOpYyZDyRRt3pcdv1G49NH8bwqnxTpBuXRHq19dG81T6bIQhHGkHeeIUes_CWJIqAsyLo9SS93vDfRGAXcYu1rqfoWtTPmO1gyYSBYf0vjb1bQpy2u6ziPqyDFqHhOUBUAQ8liqqFW3hcaQwv4yg4No0yfEc77Nt7L52h3F2HHzyUomq0Horihr1VwqZTXyEtdzphbB-zvNxTS-TQGQFt8lawxh1Z5H0axryJ5Z2oILzTm1sLkMZ6UAxw1Owxyw8qy9NarIElhEAHClB0-FUFX_4XdQ1_08j3iSATOIUlikj1hHWeEIgYr2T4sFZCXlfZt2dyMNkrbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارک کاپوتو از اکسیوس:
این چه تغییر رژیمی است که‌ انجام داده اید؟ شما خامنه‌ای جونیور (جوان) را همچنان در ایران دارید.
پرزیدنت ترامپ: خامنه‌ای جونیور با پدر متفاوت است. آن‌ها افراد متفاوتی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66526" target="_blank">📅 22:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66525">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5016d97e5.mp4?token=SYkaDuzatfvNAxLA3tPDNdap8-5JAAEmRUMA3_0k60_OdfbwejDg614k50bqqtpouyxqwTxkf-X-q6TqkleI3o71mmrE2YlCItTUZNKm02ezU_05Z_jwGuehce0D09KHSSSFpDMcho2sTOUFBvK_jjFksmMLhydu1I2v6tj4ZfruF956mpwKhP-qt6zmjCWleIR_oRshGymKmxCVSc00eVbJzyhUUzYD3RW7zhUlvoXgh3c8vPhj5bJqjgrTqC5CjbTYUF-3bHdbnjlTCrcj30MH93m5Q4GB-We6XVZpNSXTzanATDoXf2waevS9lRIaNlNXcA8d4j3uOduCc9Mn1oTz5c2kvlNh4xWOh2wIYYuLm9koViWfktgF-LbZkuwmIxLCc6tyO9WjjS5XppFZ3bL-Lgr_yOdB-ODTudtUkx6QS9l52CkouvjLXWpMJC9bgkL7UXB1UOvGVuD4lo6qhUgXoEeWwbMqjk9TOH8ScUOVLf6_v_v5ZeTe-MLyE2mVEeLONqiP1hPvrrFJ2MS6F_v05orkmAsM4TmIlm0rX3EQkJPJ6-_06eUzr1fW88jwkpDOH0bKdaFgx2HaGGjix-7Yls4Lkn2IfaVvZr0ZOEWMHxfxBjPklNhBMFcHoIHUDaXPPZu9dzRhydIAACpqYOHxFl-Tjio8dWN3n6XJ83o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5016d97e5.mp4?token=SYkaDuzatfvNAxLA3tPDNdap8-5JAAEmRUMA3_0k60_OdfbwejDg614k50bqqtpouyxqwTxkf-X-q6TqkleI3o71mmrE2YlCItTUZNKm02ezU_05Z_jwGuehce0D09KHSSSFpDMcho2sTOUFBvK_jjFksmMLhydu1I2v6tj4ZfruF956mpwKhP-qt6zmjCWleIR_oRshGymKmxCVSc00eVbJzyhUUzYD3RW7zhUlvoXgh3c8vPhj5bJqjgrTqC5CjbTYUF-3bHdbnjlTCrcj30MH93m5Q4GB-We6XVZpNSXTzanATDoXf2waevS9lRIaNlNXcA8d4j3uOduCc9Mn1oTz5c2kvlNh4xWOh2wIYYuLm9koViWfktgF-LbZkuwmIxLCc6tyO9WjjS5XppFZ3bL-Lgr_yOdB-ODTudtUkx6QS9l52CkouvjLXWpMJC9bgkL7UXB1UOvGVuD4lo6qhUgXoEeWwbMqjk9TOH8ScUOVLf6_v_v5ZeTe-MLyE2mVEeLONqiP1hPvrrFJ2MS6F_v05orkmAsM4TmIlm0rX3EQkJPJ6-_06eUzr1fW88jwkpDOH0bKdaFgx2HaGGjix-7Yls4Lkn2IfaVvZr0ZOEWMHxfxBjPklNhBMFcHoIHUDaXPPZu9dzRhydIAACpqYOHxFl-Tjio8dWN3n6XJ83o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره مجتبی خامنه‌ای:
من آیت الله را کشتم و متأسفانه آیت الله دیگر را آزار دادم.
من او را ملاقات نکردم. من با او صحبت نکردم، اما مردم از او صحبت می کردند.
اما او شجاعت خاصی دارد زیرا به شدت مجروح شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66525" target="_blank">📅 22:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66524">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb514f4019.mp4?token=GOwGETRcNY_j_zgpQrTLRL5bf8vUElgL_weQhwgsdTgl5x-rCyr8QkOhlFg0SLY7TWlschYqqVj97viky_kHKTZc27dQ7s5tq1RmNaTwB9RfgRG6uAa_8g70x5z63JzAyx0fBUdGkyQuyJTVI_4uef6S-nNn-2Ipqnk38qT9YSozeEQRxqW-pXSCG3I8hcQ-lTj-vJMy4LlFnHN4u-FY9x97zgIQJs1XW8QXs25_ztAzp5Yd6tyXD-gXo0TJrfLsn97IFh8ewfGlpeVdu5gJlQ-JNTH_-kYljJm4a4P42aInQuV7aGpRJlbJCERLeAwqLBadnfLhl9_TRRxcy9RJSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb514f4019.mp4?token=GOwGETRcNY_j_zgpQrTLRL5bf8vUElgL_weQhwgsdTgl5x-rCyr8QkOhlFg0SLY7TWlschYqqVj97viky_kHKTZc27dQ7s5tq1RmNaTwB9RfgRG6uAa_8g70x5z63JzAyx0fBUdGkyQuyJTVI_4uef6S-nNn-2Ipqnk38qT9YSozeEQRxqW-pXSCG3I8hcQ-lTj-vJMy4LlFnHN4u-FY9x97zgIQJs1XW8QXs25_ztAzp5Yd6tyXD-gXo0TJrfLsn97IFh8ewfGlpeVdu5gJlQ-JNTH_-kYljJm4a4P42aInQuV7aGpRJlbJCERLeAwqLBadnfLhl9_TRRxcy9RJSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره ایران:
این ایده که اماراتی‌ها قرار است یک میلیارد دلار برای ساخت نیروگاه در ایران سرمایه‌گذاری کنند، اگر ایرانی‌ها رفتار خود را تغییر نداده باشند، پوچ است.
آنها این کار را نخواهند کرد. ما اجازه این کار را نخواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/66524" target="_blank">📅 22:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66523">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e9895e96f.mp4?token=nXHTT8xSUn8cl7b0bT-bFTTZjCFMm-cRaiBV-w2_g1qcSFZzaelfT6UFdIYsr_sVZJeDrqZPGXDYTrFMDNwhWbccyfLGtl6BrQ62VRsfL-5x93crJANoQW_x2QidbkyVEbVs-0LWcsN1OXfXxPKZe6dSk_seuB2_fOOUqj2Hb2cKlWIvHDaf_48Q2naxkAfejf3_dps0Kt6wcllms-0pv1Va_M_Fa96k0iqZ5aCGDpsszIjeqzoHSr3YQfdJaO-x0qgh88vic6kBySbVUCvsOvP-T5VhHtZYDfZBaAOOoO9TGBFuHOQWD_hFYHRf7WKSL6CTB5jVY4DMVuqvwtsOPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e9895e96f.mp4?token=nXHTT8xSUn8cl7b0bT-bFTTZjCFMm-cRaiBV-w2_g1qcSFZzaelfT6UFdIYsr_sVZJeDrqZPGXDYTrFMDNwhWbccyfLGtl6BrQ62VRsfL-5x93crJANoQW_x2QidbkyVEbVs-0LWcsN1OXfXxPKZe6dSk_seuB2_fOOUqj2Hb2cKlWIvHDaf_48Q2naxkAfejf3_dps0Kt6wcllms-0pv1Va_M_Fa96k0iqZ5aCGDpsszIjeqzoHSr3YQfdJaO-x0qgh88vic6kBySbVUCvsOvP-T5VhHtZYDfZBaAOOoO9TGBFuHOQWD_hFYHRf7WKSL6CTB5jVY4DMVuqvwtsOPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏پیشنهاد جی‌دی‌ونس به ایران:
گزینه الف این است که شما همچنان مانند یک رژیم تروریستی رفتار کنید، که در این صورت به معنای واقعی کلمه هیچ چیزی به دست نمی‌آورید.
گزینه ب این است که شما مانند یک رژیم عادی رفتار کنید، و ایالات متحده، به عنوان مثال، اگر قطری‌ها یا اماراتی‌ها می‌خواستند در کشور شما سرمایه‌گذاری کنند، در واقع به آنها اجازه می‌داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66523" target="_blank">📅 22:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66522">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f005383e.mp4?token=rhRrvQ-QZuDNg71Kwz4oABbt8EdPy5pe9KaN1TORpzBrpt9YcQfAr9b8rexpndyjHYJZEc0MU0iug_nfSwDhsSShX6RUpT12AF2TTctoWQ3c1PTKtjLbbtnneNPvZZyWhknji8_kT3GYdd2nrAn-dszg-FfJVpkA0N9vuCMStzLhHVdhAKZYYIHgBVU9fap-PQ4FNxdpHkviyiWbo8WXsnEguMJYS_FyZhJm3KIeElHrJxZmoPjkQ8VUnMiSun_wD7V6pY-lxePDXPX62vhiqeUCY1Ix5PWeoOPzidCF6aQIEyIO_LmpBfSE90jc3WOgMGQBt7xf0UFBwetlCkWZsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f005383e.mp4?token=rhRrvQ-QZuDNg71Kwz4oABbt8EdPy5pe9KaN1TORpzBrpt9YcQfAr9b8rexpndyjHYJZEc0MU0iug_nfSwDhsSShX6RUpT12AF2TTctoWQ3c1PTKtjLbbtnneNPvZZyWhknji8_kT3GYdd2nrAn-dszg-FfJVpkA0N9vuCMStzLhHVdhAKZYYIHgBVU9fap-PQ4FNxdpHkviyiWbo8WXsnEguMJYS_FyZhJm3KIeElHrJxZmoPjkQ8VUnMiSun_wD7V6pY-lxePDXPX62vhiqeUCY1Ix5PWeoOPzidCF6aQIEyIO_LmpBfSE90jc3WOgMGQBt7xf0UFBwetlCkWZsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی ونس درباره اسرائیل:
من از تصمیم ترامپ برای پایان دادن به توافق ایران دفاع کرده‌ام و اغلب متوجه شده‌ام که استدلال‌ها این است که «اسرائیل فکر نمی‌کند این خوب است، بنابراین بد است.»
واکنش من این است: نظرات اسرائیل مهم است، اما اساساً آنها از هم جدا هستند
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66522" target="_blank">📅 21:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66521">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ebdd0a4c.mp4?token=oo_ocYEUJD0vHZRZtomHvmYWhx5cqpJiOV9TKnL6qwU8vHTMzsus8N4erCMD3rRvZ9x1TonEP95XZ47nGQPDA7fPYhgrUGp-bv7WrZUQE75zuIu5EbezKs4juo55DIGc0J1aCqZGym-VnBAz0-TJwxSGwx7NMiWjTs4cRwt8FbCNedOKppkhvkUyvAT_HTHZftV2zWD25BqbbvczjDrmo4wkapEXfnKolSf1DdJXZrNPmUiZ6ykk9QcCYWr_TUpjluZNJuqXTcidOk94AG3IZv3LDuAUd90ITvbxZMkUrKO8uXEW7RHaYTUqUBzb-86cVeJgLXluoYlGEG4kgHF_nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ebdd0a4c.mp4?token=oo_ocYEUJD0vHZRZtomHvmYWhx5cqpJiOV9TKnL6qwU8vHTMzsus8N4erCMD3rRvZ9x1TonEP95XZ47nGQPDA7fPYhgrUGp-bv7WrZUQE75zuIu5EbezKs4juo55DIGc0J1aCqZGym-VnBAz0-TJwxSGwx7NMiWjTs4cRwt8FbCNedOKppkhvkUyvAT_HTHZftV2zWD25BqbbvczjDrmo4wkapEXfnKolSf1DdJXZrNPmUiZ6ykk9QcCYWr_TUpjluZNJuqXTcidOk94AG3IZv3LDuAUd90ITvbxZMkUrKO8uXEW7RHaYTUqUBzb-86cVeJgLXluoYlGEG4kgHF_nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره اسرائیل:
اسرائیل شریک خوبی است، همانطور که بریتانیا یا فرانسه شرکای خوبی هستند.
این بدان معنا نیست که ما همیشه منافع همسو خواهیم داشت
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66521" target="_blank">📅 21:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66520">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c3443a503.mp4?token=o5f05IBHt0hKL6QxHLqwQCAT4hclO6s7D0nwa122S0_AVMxA_sKQxDz-L6n9xT8BhWFcwEnbzpiHZXsOyzjPAd7xcBjvT1KfT1coHpDAdrehskoExMMPSZpCmNIzHlnNVYSMF4B5jGVA_KjTm7261Kb979lMuirYEaef-na-uIbFjs5GCIf6SO7fS8IX007We1QBkbpe2Tun_beqtl4T9WpmPSI9BigkD1ysDk9FMhJxis2sXQhYcQNU-DKymk0InWdAh2v4E8jZjT9tvkGvvsEagSpMsa6aGematt8c1tq0Q8O8X5G65c9rTeW098W-8QghmUq24c7eCz_rTcJjvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c3443a503.mp4?token=o5f05IBHt0hKL6QxHLqwQCAT4hclO6s7D0nwa122S0_AVMxA_sKQxDz-L6n9xT8BhWFcwEnbzpiHZXsOyzjPAd7xcBjvT1KfT1coHpDAdrehskoExMMPSZpCmNIzHlnNVYSMF4B5jGVA_KjTm7261Kb979lMuirYEaef-na-uIbFjs5GCIf6SO7fS8IX007We1QBkbpe2Tun_beqtl4T9WpmPSI9BigkD1ysDk9FMhJxis2sXQhYcQNU-DKymk0InWdAh2v4E8jZjT9tvkGvvsEagSpMsa6aGematt8c1tq0Q8O8X5G65c9rTeW098W-8QghmUq24c7eCz_rTcJjvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی ونس درباره ایران:
باز کردن تنگه هرمز دلیل کاهش قیمت نفت از اوج ۱۲۶ دلار به حدود ۷۵ دلار در امروز است.
و همچنین به همین دلیل است که قیمت بنزین، اکنون که ما صحبت می‌کنیم، برای اولین بار از ماه مارس، با وجود افزایش به میانگین حدود ۴.۶۰ دلار، به زیر ۴ دلار رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66520" target="_blank">📅 21:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66519">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q751ZHJaVnZ9QlYe2kZGRIbNSBRhxJrq5Ej1NbU0VsqEls_cF-WKuu_Jmp-yEuFXeUu65aCYJptz8yf2U4Uc1Lbstl3R4pKCZ_s1QnaZ-ACPWLksyHLk61axGK5AtiFcXZQLguYBC8eCsaYZ3hz-i5zGPjw8M7_F981812LJilDy9fwWVA7ZLL8jT64wC22-6JIa19EpAR2qhoyS33Ei0Rkvojv5KeOaxD69LHGZ-F1SKZR-X039sP90Z273EOiCgoZYcbWzJOi7maUCpWZorEd0Fovkf1SXz6Xe5ULmKB3B_Lotu0MiTbe42SWTnqQfOB9187AQ9E1g9OJ8RKOeqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هیئت قطری رفته سوئیس ولی ایران و آمریکا نرفتن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66519" target="_blank">📅 21:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66518">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pB9jbM1WbD2lFuw4E6Mj_LO_zJJRHbvqgKeaCxu-awioBhUDJGMyPey-p15SgAhg7bKxaM5AnFzQjWesTmYeq8AAsXwunPJR90G-0L6XwXGiEN-O0Fi-0X7HL4iYFdmC2QZfGY8H7BqKG0WA2JPga9uQoWmSpw1jFRRn1VZfTWEk4dTcTL6Ugd96irhL3Puv5MBOu6BN64ENNPe_-iEjkUO0MJTwmTB7Qy8oCXT1slFoZ1t6FFEF-IM_WnW380xeXgz2zd3ZojMIjuOoYtsD8AKKmRERd_mKKQPbOe8T8kkv59m8E09ZJFCnTmVKXbk9bkDtOi5oQsaGgM75Xvibtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌پست:
آمریکا ادعای «مزخرف» مبنی بر اینکه امارات متحده عربی - یا هر کشور دیگری - دارایی‌های مسدود شده ایران را آزاد کرده است، رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/66518" target="_blank">📅 21:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66517">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4VamswQSOglcfWTa3CUiVyxNNyxmxkHwr8UUZ94QfLXCMUpiE9w9oruNJ-ZwQdBHppsvkIDLzGbZ1HslCeL-F3Zf_o9_xpRna5o9pGtsQ3D4H-QNCS91HwN0d-ha6oVAvMqXRtmBeJgEdA2fA85Cjk1s4W3A036qB9v0UTPcxVi1KDdFlRPPhvMdESDUC1ftIVo1rb2oaFW7ITpN-a4ad0rN9VSuI4hSh8XIckTFGn2o_XtDiLwQAagqg1X8RlUQXpgzHXOk4tt7AG6pdRWVFyV-altiQ_y7xp4R9NPIEnpz4uoCuSnJu44ObssLi6-O_6ep-G1C1dIm8JZzteR2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سازمان‌های اطلاعاتی ایالات متحده به دولت ترامپ هشدار دادند که نتانیاهو احتمالاً اقداماتی انجام خواهد داد که می‌تواند توافق صلح جدید ایالات متحده و ایران را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66517" target="_blank">📅 20:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66516">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700e55c3c3.mp4?token=pswvFv6J4uqxZiXLAslHA5tALG_dB_kdecdJSojNjdqPkxyBo68Ys57T_PhoiTdQknF0RwCTcVxc3SEMcAXCRgOaEBVYq6LCCD09NJ6vgFsl6L7IMnw4wZj2LHtRmtjfI_3Fxiu8XnEos3b-YfUMVeZ5GNBk13uy_o3TStveIP8ijWqX8JXFNHxfDApCrgTAmtY-PbWcXbV8cWdLgkGk4FGSdjNr5JN9tqlCMuYQ1tZrhhliR5OQB493s7zePLuRUMPMPgHh3TO1t4Y65VBMduA0xoJUizZEDzl0Z0L9rB5tzDeLFPEwO09X0QZadw_KVjujE0QXeSaRb7EzwFmQ8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700e55c3c3.mp4?token=pswvFv6J4uqxZiXLAslHA5tALG_dB_kdecdJSojNjdqPkxyBo68Ys57T_PhoiTdQknF0RwCTcVxc3SEMcAXCRgOaEBVYq6LCCD09NJ6vgFsl6L7IMnw4wZj2LHtRmtjfI_3Fxiu8XnEos3b-YfUMVeZ5GNBk13uy_o3TStveIP8ijWqX8JXFNHxfDApCrgTAmtY-PbWcXbV8cWdLgkGk4FGSdjNr5JN9tqlCMuYQ1tZrhhliR5OQB493s7zePLuRUMPMPgHh3TO1t4Y65VBMduA0xoJUizZEDzl0Z0L9rB5tzDeLFPEwO09X0QZadw_KVjujE0QXeSaRb7EzwFmQ8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم، دبیر کل حزب‌الله:
امروز در لبنان، ما با خطرناک‌ترین مرحله تاریخ خود و بزرگترین توطئه مشترک آمریکایی، اسرائیلی و بین‌المللی روبرو هستیم که آینده کشور و فرزندانمان را تهدید می‌کند.
هدف اصلی این طرح، ریشه‌کن کردن و حذف کامل مقاومت و پایگاه مردمی آن در لبنان است.
دشمنان برای دستیابی به این هدف، ابتدا جنگی جنایتکارانه و بی‌حد و حصر را آغاز کردند و با کشتار غیرنظامیان و تخریب گسترده، مقاومت را به زانو درآوردند.
در گام بعدی، ایالات متحده و رژیم صهیونیستی پس از مشاهده تغییرات در معادلات منطقه‌ای پس از تحولات سوریه، توافقات قبلی را نقض کردند تا موازنه قدرت را به نفع خود تغییر دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66516" target="_blank">📅 20:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66515">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46f332c84e.mp4?token=pWsMSRNpixzPkVhr1fqOnOD7p_REz1VUsUgx5-IpW1xTIYOX0GR26Ml7mPqry7jhwWS8rM3iVLPwW9JrKOvrYCnANR5HORyd4xmPhO3nBdYp2NU8JPSbxnx7PbMUpFJN97HPoFqFE5LpFA4Y6_JInNqGLfrl1DNOCpTWpCPCPOpaevoexHg5YoZKFsiXq_4W0ZqNnFEe8SLKXpmH4AeCGEt7xTwx1h7puNUfEESolQAhRfTtOuMa4-ZR4RGO6cwmvvOckUhJ6MLJJ-QDhNqjRMeb7q-HXIScKbQYarnHvP9wjnhJQOa4agb6d04Ze8Xz24k3A1Ldo-dls_e5sNQ8oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46f332c84e.mp4?token=pWsMSRNpixzPkVhr1fqOnOD7p_REz1VUsUgx5-IpW1xTIYOX0GR26Ml7mPqry7jhwWS8rM3iVLPwW9JrKOvrYCnANR5HORyd4xmPhO3nBdYp2NU8JPSbxnx7PbMUpFJN97HPoFqFE5LpFA4Y6_JInNqGLfrl1DNOCpTWpCPCPOpaevoexHg5YoZKFsiXq_4W0ZqNnFEe8SLKXpmH4AeCGEt7xTwx1h7puNUfEESolQAhRfTtOuMa4-ZR4RGO6cwmvvOckUhJ6MLJJ-QDhNqjRMeb7q-HXIScKbQYarnHvP9wjnhJQOa4agb6d04Ze8Xz24k3A1Ldo-dls_e5sNQ8oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم دبیر کل حزب‌الله:
پروژه نابودی حزب‌الله شکست خورده است، نقشه‌های اسرائیل به بن‌بست رسیده است و پیروزی نهایی، یعنی اخراج کامل و قطعی اشغالگران از هر وجب از خاک لبنان اجتناب‌ناپذیر است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66515" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66514">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66514" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/66514" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66513">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66513" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66512">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
نعیم قاسم، دبیرکل حزب‌الله لبنان:«تا زمانی که توان ایستادگی داریم، چرا باید تسلیم شویم؟.»
حزب‌الله خلع سلاح نخواهد شد. این سلاح‌ها برای مقابله با اسرائیل هستند.ما تصمیمی «به سبک کربلا» گرفتیم و این تصمیم همچنان به قوت خود باقی است.
«ما وحدت نیروهای مقاومت را حفظ کرده‌ایم و وحدت جنبش امل، حزب‌الله و سایر نیروها همچنان در کنار ما برقرار است.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/66512" target="_blank">📅 19:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66511">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nN_ghPHCScaUhPduIgxmi7xH6sLzf3EPsidTDgP61ievoUb1HBeKyz0B8uIn-uoI7-yAty0OSj6HT0rlYp6xNpSoR4j4rUHXJwtDSBo3Xls6J-gYnrPjGuFWdT5w299cvcvIs1UPdEjdMUO4ZZN5gPSVyVzbKFVzgqHr33Q5EZh2YApmex0CuE9DaCJUX9cpZeI10t8Cvt56j2rpsB91YitakIb0skieW0XhHIAGVpV6RgxqRnI568sehW8lJwi08lc7RIeUfGZcjwkv9CyRvrpDSTSAdAiCDwMVA1pKgqh5ag3i52Ue-Q2TjAaOYb1Zjjick1wM-roqRAc5BnQgYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اتاق جنگ اسرائیل:
رژیم تروریستی ایران از نیروی نیابتی خود، حزب‌الله، برای حمله به اسرائیل استفاده می‌کند، به این امید که بتواند وقتی اسرائیل پاسخ می‌دهد، اسرائیل را به خاطر از مسیر خارج کردن مذاکرات سرزنش کند.
ایالات متحده باید به حمایت از حق اسرائیل برای دفاع از خود در برابر رژیم نسل‌کش ایران و نیروهای نیابتی آن ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66511" target="_blank">📅 19:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66510">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d0ea7af18.mp4?token=Mb20T0uqPXDfqVz5-fye3UCzxZ2njVwhFI0zLUXsxk4hb6mwGMTjEFaa2lt8HXrb8HKjm0bfzAbZ3nQQGUtIt9ySFlAqSKNqmEoeIZiUgYLCTvAzdofBcjdk419btM99a2egeRQr4W-LOeYHz7uynqIjk6407FmWxuNny4xoERjfcSiK4YOX7nrHTbIGov5XKS43QVWpeHQhgFGuAQ29c6Bx6usqEGgHtcm1fXNq2TwGLlcT_fAN4XV9SOLo0e7nCZVG7fCVahKXyYX3tnRqpXZSgo0AQp-vJqw_wwdIKXyS4E7mgVtEC8o4xwLafry_lSfe-gKmunT9tGS2EMS42A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d0ea7af18.mp4?token=Mb20T0uqPXDfqVz5-fye3UCzxZ2njVwhFI0zLUXsxk4hb6mwGMTjEFaa2lt8HXrb8HKjm0bfzAbZ3nQQGUtIt9ySFlAqSKNqmEoeIZiUgYLCTvAzdofBcjdk419btM99a2egeRQr4W-LOeYHz7uynqIjk6407FmWxuNny4xoERjfcSiK4YOX7nrHTbIGov5XKS43QVWpeHQhgFGuAQ29c6Bx6usqEGgHtcm1fXNq2TwGLlcT_fAN4XV9SOLo0e7nCZVG7fCVahKXyYX3tnRqpXZSgo0AQp-vJqw_wwdIKXyS4E7mgVtEC8o4xwLafry_lSfe-gKmunT9tGS2EMS42A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
«هر مشکلی در خاورمیانه مستقیماً به ایران برمی‌گردد. حزب‌الله؟ ایران. شبه‌نظامیان شیعه که عراق را نابود و تهدید می‌کنند؟ ایران. حماس؟ ایران. حوثی‌ها؟ ایران. اسد که در سوریه مردم را قتل عام می‌کند؟ ایران. این رژیم هزاران هزار نفر را کشته است.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66510" target="_blank">📅 19:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66509">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ak-uId66iN2xxp0L5tlad5apiQkboWY-P-qji-7U_iWkaKvSI68dBFIY98y9DoPZAfUmLZ4wy2eeZeAxYSwakfEKesv7AG74Ic2I34U0fZ9P-Lz4zGE4BDxU9R-Djb7gda2Ejvka1tHA99ZGFaVg20dVtbmfrFJrmSBrCY4kFlZfoAB9bIqxfCaJiK_UynUBc2IGK1-uodBMOGeNDyZ3ZphcsweF4zjn-jGKg7ygKLcojJXdC4lWj9_kDzbBVZ8P-KIfDRv_VbE2BxiUdh6oPA5gTstaP-jT0QnIgE4hB9klzuAVBjsAdwlJoz5fon92dukicvcws2_hPV4_EMC1lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اسرائیل هیوم به ترامپ:
می‌تونستی بزرگ‌ترین رئیس‌جمهور تاریخ باشی، اما شکست خوردی
شما به منافع جهان متمدن ضربه زدی و ممکنه به‌عنوان رئیس‌جمهوری در یادها بمانی که باعث تحقیر آمریکا شد
به اسرائیل خیانت کردی و حالا تمام تحقیرهایی که قبلا باهاش روبه‌رو بودی، کاملا موجه به نظر می‌رسد
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66509" target="_blank">📅 18:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66508">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ:
ما از روی استیصال پای میز مذاکره نرفته ایم.این ایران بود که از سر استیصال آمد. کارشان تمام شده است!
ما این دوره ۶۰ روزه را تا آخر پیش می‌بریم. آن‌ها هیچ پولی دریافت نخواهند کرد؛ حتی یک سنت هم نه!
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66508" target="_blank">📅 18:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66507">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c09804d09.mp4?token=v9Rykgkj1E6U8L-_UioBcsx86O_1libQv8AAFuhHfIEnMtmLmhC23H3P1CRSuy8XLciAjG3gKJLYCwURScH_hw18nu-2ChuUy4URhLSwx8dlgI5vtKooYWdvHKytsgcf6Vx6rMLp9HqHtvFCI-iVzQ7OJCzQRI-RFECFcSHLHCh-jBzhWb0yuOVPMLVY43mUibzgjbs1EuvzlfQsp1KIx5xkHm7N6WyDTwXC0P39g8Px2xFyfiRh93lxguOLTkcexvW-qqIY_-zNBjWmhfcz29cxgtnPPpS_1NUZk5kXghsiNKzMjHOTCQfDuxkgvoHWXIAjzA5Xd7H7oitKp_u-gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c09804d09.mp4?token=v9Rykgkj1E6U8L-_UioBcsx86O_1libQv8AAFuhHfIEnMtmLmhC23H3P1CRSuy8XLciAjG3gKJLYCwURScH_hw18nu-2ChuUy4URhLSwx8dlgI5vtKooYWdvHKytsgcf6Vx6rMLp9HqHtvFCI-iVzQ7OJCzQRI-RFECFcSHLHCh-jBzhWb0yuOVPMLVY43mUibzgjbs1EuvzlfQsp1KIx5xkHm7N6WyDTwXC0P39g8Px2xFyfiRh93lxguOLTkcexvW-qqIY_-zNBjWmhfcz29cxgtnPPpS_1NUZk5kXghsiNKzMjHOTCQfDuxkgvoHWXIAjzA5Xd7H7oitKp_u-gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
همانطور که دستور دادم، ارتش اسرائیل با قدرت به ۱۵۰ هدف حزب‌الله در لبنان حمله کرد و ده‌ها تروریست را از بین برد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66507" target="_blank">📅 18:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66506">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">Live Tennis</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66506" target="_blank">📅 18:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66505">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faa1be6643.mp4?token=YoeyvmIF4KyMeth-KlrcPOSOC9qB_AyY07ieHLYi9k4Z-T7VASrctArWG-dAwps9M53fD51dZPSarGkEdG52RL8FFd8CMYB_a1fGaMMBXejZrYTqCIXaLxsnHR5tm7GnOV95qPcTPdRiNZbLR9tgmM5pwMxaDctobQA2JtqM4I1F5lef7X0I9itXsFeLQ_10yOMpNzDCbKjRhY3Y50n2IHk949qq0NIgAXCCHX0MQF344ae0E-wbSf5dDVgEDsSyFTl-Jicly1kVYB0eU3s2OsSUlxkTuglO-CmnO4D8vpQGwJELrh9ilmX42CZjZoB8XD44tLsTBfbdWFm0gqOIbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faa1be6643.mp4?token=YoeyvmIF4KyMeth-KlrcPOSOC9qB_AyY07ieHLYi9k4Z-T7VASrctArWG-dAwps9M53fD51dZPSarGkEdG52RL8FFd8CMYB_a1fGaMMBXejZrYTqCIXaLxsnHR5tm7GnOV95qPcTPdRiNZbLR9tgmM5pwMxaDctobQA2JtqM4I1F5lef7X0I9itXsFeLQ_10yOMpNzDCbKjRhY3Y50n2IHk949qq0NIgAXCCHX0MQF344ae0E-wbSf5dDVgEDsSyFTl-Jicly1kVYB0eU3s2OsSUlxkTuglO-CmnO4D8vpQGwJELrh9ilmX42CZjZoB8XD44tLsTBfbdWFm0gqOIbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محکم تر بززززن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66505" target="_blank">📅 18:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66504">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4b87f1a5b.mp4?token=S8L27DTXfSs2VUUThUyDecSSQWKkqaY9YjbAxo2dKy2niCmgYCcoI_OfXBfdyLBtiKDF_BR4JhPhjesrxpqa4eS5Hs-CSAhFdpMODo-M4tsU5NYDZ6Lo2Ef-4Ipod3oU9F14ece2wkzgFEhnKUP5hFYxP_R-XqA523orUjZNEUkK3fXp9vTPe0I_OCzy-LWd-XUSpsTZA98h68O2BprmyVGVbrW24smUmOXtHDTZstpong1qpvRYH2QDywmGAUtPKryyGv00MIeG3bTg4Xy2CftrTc210Yn-k1fuzAYUjusAWZtycy6KfBgfZNrhSFnWAo8uJSz3987u_MPNeZ62IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4b87f1a5b.mp4?token=S8L27DTXfSs2VUUThUyDecSSQWKkqaY9YjbAxo2dKy2niCmgYCcoI_OfXBfdyLBtiKDF_BR4JhPhjesrxpqa4eS5Hs-CSAhFdpMODo-M4tsU5NYDZ6Lo2Ef-4Ipod3oU9F14ece2wkzgFEhnKUP5hFYxP_R-XqA523orUjZNEUkK3fXp9vTPe0I_OCzy-LWd-XUSpsTZA98h68O2BprmyVGVbrW24smUmOXtHDTZstpong1qpvRYH2QDywmGAUtPKryyGv00MIeG3bTg4Xy2CftrTc210Yn-k1fuzAYUjusAWZtycy6KfBgfZNrhSFnWAo8uJSz3987u_MPNeZ62IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از لحظه سوخت‌گیری جت های جنگنده F16در حین انجام عملیات گشت زنی بر فراز خاورمیانه.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66504" target="_blank">📅 17:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66503">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3273d3f5c.mp4?token=IiuT9K_cRo98kxFs9zR1sNaEkPUEVsOEtxq02tlJrh-qgt6ebIQluwNiP0scAi81dilrWmOC4OZ6lPN-l84pMZTdPBEW8cp02isfzEeceTlbJEi8kKekbDjFO4V_N1R0OKk5rEQg3tQUWoBLBbZDQul6kN_-BCQWFctsU-nwnGuWOYQsfWqItDL2hUS2G-LKtmQKAhukQxzqcrSFZui6VUrGcsGKADTFHi6ooL5G7EKIqU1oZ4m5z4ivEdBwKIxWkmPjotii3kc03TfCVuJYsHI1tq4_6eLiEgRzb_kr-2wZCcDDRmBjMv-zxWEKxz38apLE-crFDgIcb9v_LSPq2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3273d3f5c.mp4?token=IiuT9K_cRo98kxFs9zR1sNaEkPUEVsOEtxq02tlJrh-qgt6ebIQluwNiP0scAi81dilrWmOC4OZ6lPN-l84pMZTdPBEW8cp02isfzEeceTlbJEi8kKekbDjFO4V_N1R0OKk5rEQg3tQUWoBLBbZDQul6kN_-BCQWFctsU-nwnGuWOYQsfWqItDL2hUS2G-LKtmQKAhukQxzqcrSFZui6VUrGcsGKADTFHi6ooL5G7EKIqU1oZ4m5z4ivEdBwKIxWkmPjotii3kc03TfCVuJYsHI1tq4_6eLiEgRzb_kr-2wZCcDDRmBjMv-zxWEKxz38apLE-crFDgIcb9v_LSPq2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ بعد از نشست G7 پشت سر جرجیا ملونی نخست وزیر ایتالیا گفته:
این زن همش التماس میکرد باهاش عکس بگیرم. حالا جرجیا در جوابش گفته:دروغه، شوکه شده‌‌م. نمی‌دونم چرا ترامپ با متحدانش این‌طور رفتار می‌کنه؟
ولی یک چیز رو به خاطر داشته باش: من و ایتالیا هرگز التماس نمی‌کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66503" target="_blank">📅 17:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66502">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
سخنگوی ارتش اسرائیل:
منطقه امنیتی در جنوب لبنان ۱۰ کیلومتر امتداد دارد و ما به تقویت نیروهای خود در آنجا ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66502" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66501">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-zPsopdZZ2GY9otJvtp2vV76LUxe-h1DJ9hTptDInNk8pWqPY62nuWrvHEPkvqukU-TkvoPxXZT1JCoU8DL5so7f_3c5vdCMKEyaQ6xYTcrCWzdmNbdpPQqGzUBP9EP2E9QS3YaERRegC-_xHOpepmfGb7Re8pJQGnrRs8lKE0rnIchmaAXBJBE6-Y4xLkvJ5zw9Br2UX1wmDrSN1NWJOzl62L1utqgoA0oKuRrokiAJO-w3iBI5GjgvC8e6Mw99JKwRRrcaxx4mO2Em4tUJiUCJ6QC_dR9BupIY9XIhc7b7MwDQthOhMsXCrBmu1rUwrBHM9Ry6AgogTQzUaPYEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اتاق جنگ اسرائیل:
اسرائیل و حزب‌الله به توافق آتش‌بس جدیدی دست یافته‌اند. حزب‌الله از توقف بمباران اسرائیل و پایبندی به توافق‌های آتش‌بس قبلی خودداری کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66501" target="_blank">📅 16:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66500">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrIq_6E-YWa_euIjaNHjUE79_oonRZ-30DREmiBAufOJKlBoTlaPPbLkeHbpoaxhMSvjhuYFNGotGGpmNEcd8fxL27nL28TVFWJykfqkl8jcHanRVcBsnuwWhV-m2ihC_sbT6IKrjf44tt3xX_6NZHQF_HWRR3vWz680_P2jcF8oFw2Chz-CU86NvlCYIc_lT0dSkUjppsP9xiDLR1MTDbdJMNx59iXMA1CmaYJC6IXGmws1SiKoDY-IA6AP0jXkcf_uEyJpn577qawULy-jqM0YxLWA6CeloEOE7C0V1-H2u7FPS6jWrGnzZgNmXO83uRIazKSUYdf1TrjM0YURrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:
یک مقام ارشد آمریکایی به من گفت: اسرائیل و حزب‌الله بر سر آتش‌بس مجدد از ساعت ۴ بعد از ظهر به وقت اسرائیل توافق کرده‌اند. این توافق جدید با میانجیگری آمریکا و قطر پس از مذاکرات با اسرائیل و ایران حاصل شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66500" target="_blank">📅 16:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66499">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5NCQHU0gKTAeTf6aoIzi-LQbLyd4SCqJuLgBYh-dRPY_arGIeXBgsLTqbV26cbCv7HYt7i1SNcoq7cDfKmpM7J_PX0Y8jUHvKNlBuFH6RzwriGjA1sNSgffqs5aA8vSLwQcNe_RnY-EUmtbPcoRdUIP3p4pvUegQ3nZ3BLMkq61P8g8LMOvTN7E1iIm6KDY2zxpk_ekoS6vCMm_kH4qdnHQ6KokcdjNd8EYYQbZVJ8RNMc2m3QexLus0-pAz1a-8P8VFvm6SQXjb0UPhsmav1egQ4KQ44bNP-PNKEjg3DiVQ9OADIMZAuU8Jy-uumxE-QKCw_8z2bSpRc5dtKjiZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما از روی ناچاری ملاقات نکردیم، ایران این کار را کرد. آنها کارشان تمام است! ما 60 روز را بازی خواهیم کرد. آنها نه پولی می‌گیرند، نه ده سنت!
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66499" target="_blank">📅 16:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66498">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVtiqxjK5VZAqga7kwRQ_LKFeEUZ_qahlcmMJj8azc9kHfmVoSfJkeYOXfx2gFeerq3afAru7vhsS9MhgQUzocojbyPEGaDg9w8a-_ZYuREePUSUXMRu6nQkitr76XTDXr5YLI8CmOmN1HvYbYbuHN8ft01Yw9cB9OWCQcvz_XkE5zOn_cd4oYh-k8RG0kwu0IHMyDt3bbsbvB8Ebqy5g_Do-hrHCB1FyYW3FnGPSK4h4VLs-eTddcl5VOAVHiPgxx7s_7Le8rHFT7eDbMQPtgnGpX5fkoU4wxfyiWx5Ve7NLKZx3neQSiBPJNtrIZpEaXvXeWIyuzLq4yaiS-DH-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
این جنگ ایران را تضعیف کرده است! ایران دیگر نه نیروی هوایی دارد، نه نیروی دریایی، نه تجهیزات پدافند هوایی، نه رادار، و تقریباً هیچ چیز دیگری. با این حال، دموکرات‌ها می‌گویند ایران اکنون نسبت به چهار ماه پیش وضعیت بهتری دارد.
می‌توانید تصور کنید که کسی چنین حرفی بزند و از آن جان سالم به در ببرد؟ بعضی‌ها واقعاً تا چه حد می‌توانند احمق باشند؟
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66498" target="_blank">📅 16:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66497">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
‏اسماعیل بقایی سخنگوی وزارت خارجه:
آمریکا مسئول حملات اسرائیل به لبنان است. جمهوری اسلامی همه تدابیر لازم را برای صیانت از منافع، امنیت و حقوق خود و متحدانش اتخاذ می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66497" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66496">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIHlr2HSB8US79RPb3d_UkSKAQVDrTz3mGhUr9TBUqrnR9ZxHc6cP2fmbxtjglg5BQ2W8qbTwl8Rg3NCiFFpbCx6MZLostuxSDgVgm5CxwDUKum9mnxQQacjkjHmU_mnDE_8y7gjnVzyasehL8HgpZgQk8s2qNXM0rQsUPpVE7s90ZZFPFARWjD2pK1sXJMdj1tArlVGSOfkf4sNHdB7NDWL6ZWrULpVH4VEbAvcEf43Xse8pHKIt1KmesKzNh6HKPyGZD1NFxy0opjWI4H1wTbjXoY3h7N9eiM1OCuMONAp-SoHE9o24G30GT0nPzvTVvDwVNqpyzAqLuKb-djp1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اینفوگرافی خدمات فعال‌شده پس از رفع اختلال فنی</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66496" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66495">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec2c7bdfe.mp4?token=gRDbR22oHuzDClWHnRGNLJ5qs8g4HqzHu4WyfR8wr00awEKGmCsG7QLkXsCl6xk0HNwkD4dkaYzKYb--LTL_Suaj9IHGJUFgCP71ZO9jolMG5CcE_-uVmjN9NhFm0O3AFbxNKnjkMo3dZsGqupx6iAt5diVPUuQHchGnultNKE4i9WZw5QlBUZbS3H7ida40cI1gYsgT3dtOBUILePGCxgtSQP1PEkdud6HYF1lPxmDvIRz6kYHCxaIQjWR0YNFQ5VHHZtky3n-hHx9VPtr-7Zq8I_U1kdum37yLfyChpmhDoz-rfsNbZx1V8oRntW-ihBe01sV97PMXOmQR23_J1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec2c7bdfe.mp4?token=gRDbR22oHuzDClWHnRGNLJ5qs8g4HqzHu4WyfR8wr00awEKGmCsG7QLkXsCl6xk0HNwkD4dkaYzKYb--LTL_Suaj9IHGJUFgCP71ZO9jolMG5CcE_-uVmjN9NhFm0O3AFbxNKnjkMo3dZsGqupx6iAt5diVPUuQHchGnultNKE4i9WZw5QlBUZbS3H7ida40cI1gYsgT3dtOBUILePGCxgtSQP1PEkdud6HYF1lPxmDvIRz6kYHCxaIQjWR0YNFQ5VHHZtky3n-hHx9VPtr-7Zq8I_U1kdum37yLfyChpmhDoz-rfsNbZx1V8oRntW-ihBe01sV97PMXOmQR23_J1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران شهر نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66495" target="_blank">📅 15:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66494">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f017f858a.mp4?token=ClsDAVl1y1Sz7ROUbM-xs9xd027yCNJcmEmju19e-eN2rzVFrrSHAifuvmnTWRrS9dxgJmY7f9JNf34rkXnXmfRQx_deaz4GUct-MjeRoHtqdNiFI_JAHXZqIdOskfWUqoJF0c5bbFKebCMeM3I3Q0tpAGZWy2XYYLYfRsjucsvq7tJS6tTXFzzR8iCjaQbuGB8IQtVb1W5NaAHY6UWbmNSC1RhGOBaZc9Gb7bqumJFEaY6Ua8OlVD7fPRRBaskHR-uKLTnSlVNhV5pz-ZR25XQzYel6sdL-306DNNKaRpubdrnLtDAXkyuAVNPvkcV8FNYnR7IXBhcXzbxhp74Asw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f017f858a.mp4?token=ClsDAVl1y1Sz7ROUbM-xs9xd027yCNJcmEmju19e-eN2rzVFrrSHAifuvmnTWRrS9dxgJmY7f9JNf34rkXnXmfRQx_deaz4GUct-MjeRoHtqdNiFI_JAHXZqIdOskfWUqoJF0c5bbFKebCMeM3I3Q0tpAGZWy2XYYLYfRsjucsvq7tJS6tTXFzzR8iCjaQbuGB8IQtVb1W5NaAHY6UWbmNSC1RhGOBaZc9Gb7bqumJFEaY6Ua8OlVD7fPRRBaskHR-uKLTnSlVNhV5pz-ZR25XQzYel6sdL-306DNNKaRpubdrnLtDAXkyuAVNPvkcV8FNYnR7IXBhcXzbxhp74Asw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آیا می‌توانید جلوی حملهٔ اسرائیل به لبنان را بگیرید؟
ترامپ: «بله. آن‌ها احترام زیادی برای من قائل هستند و هر چه بگویم انجام می‌دهند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66494" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66493">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66493" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66493" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66492">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-JM18jZKYw8bS7yrMsI-1s6LDV11ZjqSwq_FvZKdP0yaPGNEg64thl1TqiLKe0DiiBjRT-sz7mT4NoJfM4ivIOBgDu06Z-s9gz18NdiekjtRqPwmH1ehll9T1zA_hQk5wL_iM7pCyYOkV02zlP0x86fft4XQfatYTU7FJoip03-FsHE-cnCDHMV0QEpUYqzrzC63TquyZ9oOdCGL6PdU3p6Dvbxc_xXM9orFvvO39O0Dysfg8LQN8est-6e_c0Q8qW_U8NiUXK7yD8gKqmmZ3h9FSJIUCGPEdj_JQcT1o9WIBlnTEJHW4Pdxpyk5V-0mx-vGdVqSyiZXoDYEaJVQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66492" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66491">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A04uJpWY5U5PJOTy1FdaqUXjJjlb5XUHar4otgvw2HLyWav1SuesyearFHDsuuhWbfZCVFun5oPHOi6c5He3qwhcC0mLJXbP_AmU7DQKYPFxcreVzewvE9ZrGrbo01tLVK3GZfYP51-WmYz11Rs0oBHf8J6qwR1mRpzw4e0ri_m8tR4_BnDhLwn9bLOlxqRNyplbEj3bvADaXMY2mpZyOJGSEhcU5PaFVWeOB-TWyFkEnGod-rMYC5S41hV3DyviXOLNvB2ni4jKJZk5IXCPLw9eqyQDqiBwEtu_51EkNOilfcPhRPvhpe2b0-c8dPfzZ2bGAwBjSDiCMfTesyHjlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل به فارسی؛نخست وزیر نتانیاهو:
پس از حمله جنایتکارانه حزب‌الله که نقض آشکار آتش‌بس است، دیشب به ارتش اسرائیل دستور دادم که با قدرت به حزب‌الله حمله کند.
ارتش اسرائیل به بیش از ۸۰ هدف تروریستی حمله کرد و ده‌ها تروریست را از بین برد. متعاقباً، ارتش اسرائیل امروز صبح به مقر حزب‌الله در بقاع حمله کرد.
امروز صبح با وزیر دفاع و رئیس ستاد کل، ارزیابی وضعیت را انجام دادم.
دستور من واضح است: اسرائیل حمله به سربازان یا خاک ما را تحمل نخواهد کرد و بهای بسیار سنگینی را برای این حملات از حزب‌الله خواهد گرفت.
ارتش اسرائیل برای خنثی کردن هرگونه تهدیدی علیه نیروها و خاک ما اقدام خواهد کرد.
همانطور که به صراحت تاکید کردم: اسرائیل تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان باقی خواهد ماند تا از شهرهای شمالی محافظت کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66491" target="_blank">📅 15:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66490">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc6524eaa.mp4?token=k-wqQINR6JDp3ucJgnaEW0NeKquzUsj_QxkCs5G2AnNB8zdQiSf1IyHlrukbVHxe5TzP3VZIrhT9d-bPCEMlqnzrQLm5wmzTCSNHgUbHHIAEBuTt6BRIWDmSQZzk3_rsUw-QjjnYGodVexE8HKyy_EcKTaVMZlz52RPj66FXd2FKd-NgogMqKW7F3cYaK0N5aaKWFoZa32r_4Pi-hjzw-eyEv9M05Pi0i_00s5GVscd-Zk7cxw5q50au1ydD2x1iIIrNHmpzyQOhWhpblibWYrgikh5an5_2ZQaWWoD6Sjqpo9iwDRjSTAox5vopWAeReQgOVa2_GaGtllKpG_DLig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc6524eaa.mp4?token=k-wqQINR6JDp3ucJgnaEW0NeKquzUsj_QxkCs5G2AnNB8zdQiSf1IyHlrukbVHxe5TzP3VZIrhT9d-bPCEMlqnzrQLm5wmzTCSNHgUbHHIAEBuTt6BRIWDmSQZzk3_rsUw-QjjnYGodVexE8HKyy_EcKTaVMZlz52RPj66FXd2FKd-NgogMqKW7F3cYaK0N5aaKWFoZa32r_4Pi-hjzw-eyEv9M05Pi0i_00s5GVscd-Zk7cxw5q50au1ydD2x1iIIrNHmpzyQOhWhpblibWYrgikh5an5_2ZQaWWoD6Sjqpo9iwDRjSTAox5vopWAeReQgOVa2_GaGtllKpG_DLig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.  @News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66490" target="_blank">📅 15:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66489">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71570c04a1.mp4?token=YCJMjf-Qg79loyMacNCXOmBFfNPSE3c5rm3f3p_6anN1DTrifHPmLm33xDiND5tG4nCw_YgRna16wB6QLHmZMAg-hnDB52QW8flLHqIMwdwP26ohscQfkMc31UCOoHncuGmTggWnajEtpZxxvhxMbA4D0VHwbTG-3G_DwKMrQphvjUQaWJQsI45Gnd42cUz_Jc4Jo6qtQsV_VMqE8kEHjNj7Vzfn1IqXEosOo4gvNffeRGRvVTvisVhn7Wo5-rlAx2ILoeGgP28Lz9YrH9i6RAisl09549jRoA3a3MFi4gcc3fSbO7lwY5kd1-Jjb_NR2Vlijw1R-wdtAK9XS-167Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71570c04a1.mp4?token=YCJMjf-Qg79loyMacNCXOmBFfNPSE3c5rm3f3p_6anN1DTrifHPmLm33xDiND5tG4nCw_YgRna16wB6QLHmZMAg-hnDB52QW8flLHqIMwdwP26ohscQfkMc31UCOoHncuGmTggWnajEtpZxxvhxMbA4D0VHwbTG-3G_DwKMrQphvjUQaWJQsI45Gnd42cUz_Jc4Jo6qtQsV_VMqE8kEHjNj7Vzfn1IqXEosOo4gvNffeRGRvVTvisVhn7Wo5-rlAx2ILoeGgP28Lz9YrH9i6RAisl09549jRoA3a3MFi4gcc3fSbO7lwY5kd1-Jjb_NR2Vlijw1R-wdtAK9XS-167Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66489" target="_blank">📅 15:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66488">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3bba52e8.mp4?token=thBD3W5jAP6as27clmzxM-6D9duau-j9iU5WvCFzQkVJO8K-O1_b9EKAXweFCgGj9zCRO0d7X9Kn6hGUCr6Ycx23nf6V92uHKFQ2IiMGvKNcTnb4bF1pPh5JtLzmBNwOZ8Kq0_7FSgCuHKk5WBf9BJK3rhL7OhR5KVWDzGigdfA2MkY_KeorrmP1lchXgO4F5TbXfj-8YagqmoDsED0DZro0qt3mFyqfVD7JQtz0mhC8jcqixk2jhqPil95kGulGylj9L0XtueLAqPSoAGJQ1e3DpgWHMZxWAwXXgIrGbNYTombO1Gee6_KCPsXNaj5ERtX_SDy4g8fXauF7xQcPBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3bba52e8.mp4?token=thBD3W5jAP6as27clmzxM-6D9duau-j9iU5WvCFzQkVJO8K-O1_b9EKAXweFCgGj9zCRO0d7X9Kn6hGUCr6Ycx23nf6V92uHKFQ2IiMGvKNcTnb4bF1pPh5JtLzmBNwOZ8Kq0_7FSgCuHKk5WBf9BJK3rhL7OhR5KVWDzGigdfA2MkY_KeorrmP1lchXgO4F5TbXfj-8YagqmoDsED0DZro0qt3mFyqfVD7JQtz0mhC8jcqixk2jhqPil95kGulGylj9L0XtueLAqPSoAGJQ1e3DpgWHMZxWAwXXgIrGbNYTombO1Gee6_KCPsXNaj5ERtX_SDy4g8fXauF7xQcPBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
هم‌اکنون سپاه در بیسیم کانال ۱۶ دریایی.
“از آنجا که خروج اسرائیل از لبنان و لغو کامل محاصره دریایی و خروج نیروهای تروریستی آمریکایی از خلیج فارس و منطقه از جمله شرایط اصلی توافق بین ایران و ایالات متحده است. تنگه هرمز تا زمان تحقق این دو شرط بسته خواهد ماند، به همه کشتی‌ها دستور داده شده برای امنیت و سلامت خود به تنگه هرمز نزدیک نشود، هر شناوری که از این دستور سرپیچی کند مورد هدف قرار خواهد گرفت.”
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66488" target="_blank">📅 14:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66487">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
مرندی عضو تیم مذاکرات :
ترامپ بار دیگر ثابت کرد به تعهداتش پایبند نیست.
رژیم صهیونیستی مجازات میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66487" target="_blank">📅 14:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66485">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">شعارهای دیشب مداح حکومتی در مراسم محرم
😐
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66485" target="_blank">📅 14:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66484">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddac5fcdb8.mp4?token=qC8EPN5-rs74dpWUKLBKgZsv0Z3qINccSgF822U8aGdnjkmRXDUQTCHjx93KQvc9xKpPl4ORSDuM-OrcEbJIQjiLYYVd25TR0SH0arKVZefUVYBRox9dsw_AH0i9mdWoB9HT-3rCZSWnS9E_1zFNTneX-QPKzY5pqgitJUOZkjHK3Wh6EiE-KqTcyswaUBK-Y8486h9is9DqA7u-6aFGEyywDmUerP4EnOGvD4oamc19_2CxhIF4Z0V5yJBs700YL1lCVH8n5CYdBH4wUpXsmvahXLtO7OkhuHZYoGH7DgGWEDdgMcRF4PcmVxz2Rf-Kd6UB01W_kVNjq4lZkt0xCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddac5fcdb8.mp4?token=qC8EPN5-rs74dpWUKLBKgZsv0Z3qINccSgF822U8aGdnjkmRXDUQTCHjx93KQvc9xKpPl4ORSDuM-OrcEbJIQjiLYYVd25TR0SH0arKVZefUVYBRox9dsw_AH0i9mdWoB9HT-3rCZSWnS9E_1zFNTneX-QPKzY5pqgitJUOZkjHK3Wh6EiE-KqTcyswaUBK-Y8486h9is9DqA7u-6aFGEyywDmUerP4EnOGvD4oamc19_2CxhIF4Z0V5yJBs700YL1lCVH8n5CYdBH4wUpXsmvahXLtO7OkhuHZYoGH7DgGWEDdgMcRF4PcmVxz2Rf-Kd6UB01W_kVNjq4lZkt0xCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
املاکی در مراسم اعطای مدال هرکاری کرد نتونست گیره مدال رو بندازه داخل و گفت میخوام یک مدل دیگه برات ببندم و مدال رو گره زد و نزدیک بود طرف رو خفه کنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66484" target="_blank">📅 13:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66483">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
‼️
وزیر خارجه پاکستان: مذاکرات سوئیس بدلیل مشغله کاری مسئولان ایرانی در ایام محرم به تعویق افتاد
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66483" target="_blank">📅 13:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66482">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd02588050.mp4?token=Z1ma5KIM1tYtNqwDhuPu3hWoXnTHtkPsleQUQHgMoxSv6nWQZD5MCAifixgM2B0u_jtT6QV6FUh-8wPqkx4O702i8HDaBibBfb1g6shli8-wEfrtxIOa75ZiVZIbJ5sCJ2o1ruNDTwjKYdJ8HRmIrAA5w34u1AOQxViIMN9vhL8RwVIzX6D0oHUrml0T-xqdBcmxEKUZ29hJbEJ0WXMNySA-Zqyq6jptURdW0-w4y20GHqxo3bb2ZF3-913SZUQC04WXHxNzY1_QEYlMM_3UXXDWN8Z5PjRFB-_a70PU8Kj-hWq1ulZ2rQgmIkDxsOEXrrK13xschReKcok2BJEt0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd02588050.mp4?token=Z1ma5KIM1tYtNqwDhuPu3hWoXnTHtkPsleQUQHgMoxSv6nWQZD5MCAifixgM2B0u_jtT6QV6FUh-8wPqkx4O702i8HDaBibBfb1g6shli8-wEfrtxIOa75ZiVZIbJ5sCJ2o1ruNDTwjKYdJ8HRmIrAA5w34u1AOQxViIMN9vhL8RwVIzX6D0oHUrml0T-xqdBcmxEKUZ29hJbEJ0WXMNySA-Zqyq6jptURdW0-w4y20GHqxo3bb2ZF3-913SZUQC04WXHxNzY1_QEYlMM_3UXXDWN8Z5PjRFB-_a70PU8Kj-hWq1ulZ2rQgmIkDxsOEXrrK13xschReKcok2BJEt0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلاش سربازان روس برای سرنگونی پهبادها
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66482" target="_blank">📅 13:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66481">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d70873ad.mp4?token=XvLtwYGWXt6dqwrne5DFdKhx2ILaht_SYBUlb60FO6fRjGi9bEXMRRjGfWlWFvHBOuYIDxue8Cnh7OqHeQIfQpV2KYCeis3kJmQBpmiQyjxTGxi_WJXw7pmD9OTEoMH-98ddCttqtyT8q0SOhiGEfZXlu_WyMNdNMqbTtVyFChUfe3iE2Su6_y39CznM6dmbLy5wQkM2RQtFTVvFi7_zJkKiFxf34FJM5RPeXZbAX7MDrxHz9ltnvg1IiFzT_s3xag8AaPMi3_nybBc7Izv5A2WctKzG2gfr3cEAy-MN7uB94Yq-4YY0mVGlzw6yyDoflgofJlbvwi_TJsho9d317Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d70873ad.mp4?token=XvLtwYGWXt6dqwrne5DFdKhx2ILaht_SYBUlb60FO6fRjGi9bEXMRRjGfWlWFvHBOuYIDxue8Cnh7OqHeQIfQpV2KYCeis3kJmQBpmiQyjxTGxi_WJXw7pmD9OTEoMH-98ddCttqtyT8q0SOhiGEfZXlu_WyMNdNMqbTtVyFChUfe3iE2Su6_y39CznM6dmbLy5wQkM2RQtFTVvFi7_zJkKiFxf34FJM5RPeXZbAX7MDrxHz9ltnvg1IiFzT_s3xag8AaPMi3_nybBc7Izv5A2WctKzG2gfr3cEAy-MN7uB94Yq-4YY0mVGlzw6yyDoflgofJlbvwi_TJsho9d317Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتز، وزیر دفاع اسرائیل، درباره سوریه:
ما آنجا می‌جنگیم. ما به الجولانی نیاز نداریم. الجولانی، تروریست کت و شلواری، نیازی ندارد که بیاید و به ما کمک کند.
ما سوریه را خوب می‌شناسیم. او قرار نیست در لبنان به ما کمک کند. او باید در سوریه بماند، در کار ما دخالت نکند و ما را مجبور به دخالت در کار خود نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66481" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66480">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15d1aff21.mp4?token=GuuqfKnbPL74ny7sj1r9zmkTVwWzT8asMuqIAMgdEWVKpmX6mvddEZCDeAzLMPadDCrjEpI_dzsGj5alvr4M-s7_P_fcoWblYhrsz2v6plizDcYfJPBGm8UpeXARjCwRc0D-iAXxe31Vx5i9jO2IHCxipA-tdkEPZANmobwCBfqbfU8MhAdLwmjrGWUR1hFAGx4deOZRF4PPre4H1EBdfD1XWNSkUC_TVU3rixGEPM1tNw3tw1CJ0vrRrB1WHc3Ufgx3ybzpMN7TJByn9jYeIc5FiUNK4SqmHG9bGXE8pKQEqtwKD-Gszt3zprEHTUF1fBnpQwGXhQ8wsyAcu5nVOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15d1aff21.mp4?token=GuuqfKnbPL74ny7sj1r9zmkTVwWzT8asMuqIAMgdEWVKpmX6mvddEZCDeAzLMPadDCrjEpI_dzsGj5alvr4M-s7_P_fcoWblYhrsz2v6plizDcYfJPBGm8UpeXARjCwRc0D-iAXxe31Vx5i9jO2IHCxipA-tdkEPZANmobwCBfqbfU8MhAdLwmjrGWUR1hFAGx4deOZRF4PPre4H1EBdfD1XWNSkUC_TVU3rixGEPM1tNw3tw1CJ0vrRrB1WHc3Ufgx3ybzpMN7TJByn9jYeIc5FiUNK4SqmHG9bGXE8pKQEqtwKD-Gszt3zprEHTUF1fBnpQwGXhQ8wsyAcu5nVOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حملات گسترده ارتش اسرائیل به مواضع حزب‌الله
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66480" target="_blank">📅 12:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66479">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae8db95bdf.mp4?token=AyDP9QKDmNz6FOaxSkU1AJe8v6AJnbygZRk1K9H8BA1Ixxa1BQLtt0njND87PxxDY8USKLxH20MFneo9KTugHDx8BQnmmnb2dmR8JWlfILVBNcUIT_AjFRKYO0t5pNyPEnPYOtpHiFT0lMtUr5gtfzl2_BgDxnVkbrFwyjw5PbK1k9ncYIq2G4aY9_-dXjSNngrYmX8IHHMvuZGT6ZuT87oA9b_28Ald_0bjbSpkis4tLRsz8LGlEbDNsRTY2T_qakzLRjt0aMAxcJPniQWWpt-FIe8q_0zhVvPbAIK6B4VVKsTqvSminQJn6h1CKi5yt0JRBhUwPx7hUfG1XfxWeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae8db95bdf.mp4?token=AyDP9QKDmNz6FOaxSkU1AJe8v6AJnbygZRk1K9H8BA1Ixxa1BQLtt0njND87PxxDY8USKLxH20MFneo9KTugHDx8BQnmmnb2dmR8JWlfILVBNcUIT_AjFRKYO0t5pNyPEnPYOtpHiFT0lMtUr5gtfzl2_BgDxnVkbrFwyjw5PbK1k9ncYIq2G4aY9_-dXjSNngrYmX8IHHMvuZGT6ZuT87oA9b_28Ald_0bjbSpkis4tLRsz8LGlEbDNsRTY2T_qakzLRjt0aMAxcJPniQWWpt-FIe8q_0zhVvPbAIK6B4VVKsTqvSminQJn6h1CKi5yt0JRBhUwPx7hUfG1XfxWeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر دفاع اسرائیل:
ارتش اسرائیل باید در آن سوی مرز، فراتر از مرز، از کشور اسرائیل در برابر سازمان‌های جهادی در لبنان، سوریه و غزه دفاع کند.
ما از «مناطق امنیتی» حرکت نخواهیم کرد، نه در سوریه، نه در غزه و نه در لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66479" target="_blank">📅 12:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66478">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaBr_fbTSwujqn6GHEnIgCCmtFnjXrYNM6Ehhd5vw2BFmy8LL88656R3MhJsIG2CZHBUd373sowuObrjfyXym6MuX-TpiBOUAFe8Qd2liJc01GVzD2JjwcomWiy99LqI5GnXmM0WCEpAotSif28oK0MrKNXCqp1a4pgWvblV4yhK2-jsb0b_zR7oHfRodhFjhw3mBwSfW42fJ9mYl4ctpk0EY0HtySiz9-bXpaDtZKoWLZ2N-ayvGKMZzf_JkzlbIm8hc5jf6q-Tt8m6UvKcOAjrSoO2HyB2oCBE7K2L24-f7vWfR8ER0GrGyeBZBn87cb76pXA1Mj9uMkwmCiJDow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
گوش‌بفرمانیم، وظیفهٔ محول‌شده به ما توسط مقام معظم رهبری پیگیری تحقق شروط و بندهای تفاهم است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66478" target="_blank">📅 12:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66477">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c84fc04d4.mp4?token=AjftUWqtZ6dbcyIynsI2omPbhyT4mO_7_8_hw-knY7Yg7L4UQ96p4cJBULi-6Lp-Sb2AdmUBmEOMTlakGOoT9EvOY7go4WyOcbXli0bL8q0UakSf2twueHBo9mv7iu91DMX18XRz5SRDWj6q3qQ6obbX50pSwqAJ63pIWhjMukYTrl-BRH8DVQXSij6sZ9XKUtuG27S26HK8oef5iB-OLPDEaW9-WTccq0QCHUinuiE5GfUndou1I9o7oRntbCaSJiq2hWECbDzBaZ8Hb2dOWTLqMZueQL9lDSbum_6sFIOuP-noPW9Z_H4_J22rzZOKI1_vtlEMwCOBurcIeEpRpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c84fc04d4.mp4?token=AjftUWqtZ6dbcyIynsI2omPbhyT4mO_7_8_hw-knY7Yg7L4UQ96p4cJBULi-6Lp-Sb2AdmUBmEOMTlakGOoT9EvOY7go4WyOcbXli0bL8q0UakSf2twueHBo9mv7iu91DMX18XRz5SRDWj6q3qQ6obbX50pSwqAJ63pIWhjMukYTrl-BRH8DVQXSij6sZ9XKUtuG27S26HK8oef5iB-OLPDEaW9-WTccq0QCHUinuiE5GfUndou1I9o7oRntbCaSJiq2hWECbDzBaZ8Hb2dOWTLqMZueQL9lDSbum_6sFIOuP-noPW9Z_H4_J22rzZOKI1_vtlEMwCOBurcIeEpRpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بمباران شدید نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66477" target="_blank">📅 12:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66476">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cbfc5535.mp4?token=pZrODkL5_a4NOrLLdGoyFu2SmI4hrde35Fx9YmGMxyFzamHbzM5TUShLGrpiSS5I7XYuQC11VjKrLiKVWaoPsmwW6291atbto6hniMZPzvjlkV1DZm0WBICPlUba4sQE_MLgcP2IIr0SY57rLQtnW9LaiGcJpulpbJqhZ8yM69BK6LIzmdStwAseDCtxwKRRRNK_Jq4T-HVjgmxAaz0VtVQ96S6VHcET-I3L-DlOfd2EQkeGtjyVfkQlOoX3oXOaxZAVNxziHTBuiGkxS_aQ3R2YuMXtfnIdRryYscyGOdhTVS95s_tnV6hb_hpCadUwmEwmXfiTY7ZPV8EeLGP3Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cbfc5535.mp4?token=pZrODkL5_a4NOrLLdGoyFu2SmI4hrde35Fx9YmGMxyFzamHbzM5TUShLGrpiSS5I7XYuQC11VjKrLiKVWaoPsmwW6291atbto6hniMZPzvjlkV1DZm0WBICPlUba4sQE_MLgcP2IIr0SY57rLQtnW9LaiGcJpulpbJqhZ8yM69BK6LIzmdStwAseDCtxwKRRRNK_Jq4T-HVjgmxAaz0VtVQ96S6VHcET-I3L-DlOfd2EQkeGtjyVfkQlOoX3oXOaxZAVNxziHTBuiGkxS_aQ3R2YuMXtfnIdRryYscyGOdhTVS95s_tnV6hb_hpCadUwmEwmXfiTY7ZPV8EeLGP3Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتس، وزیر جنگ اسرائیل:«حتی اگر ترامپ چیز دیگری بگوید، هیچ‌کس نمی‌تواند به ما بگوید چه کار کنیم و ما قبلاً این را ثابت کرده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66476" target="_blank">📅 12:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66474">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba86fa7681.mp4?token=LStF7FJhwsQOWBZEkRF8iRCBNU3RgiBJZf2_r9Wiu8muzoHrvGncO14-9GuhDWIILXNVH004zA844DyE9XN5_O9qNOmuYKd5BQ2ODaW7HQ5EW4wvTG37JZyMRpbVFplGP2rP6rCxUqtZvzXwtL5R80sDKkpSZBAfLaaiNIqkOZqa-FSR_5C3sSHhXJ0Od0mCr8i2d1ibaSGwZMWrVj5E0c96O6kfdtfP8k39Kwh-B-IfaKw_VUZWEeshvYp_EHbwaXsqVqtvyfKobrfHUMVMvLu4qYFZe7ruRW1eb1qyGL8BXBWywwFFVX4v25EraAJ9pa7gF5zBsCQ97QyOMEFX_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba86fa7681.mp4?token=LStF7FJhwsQOWBZEkRF8iRCBNU3RgiBJZf2_r9Wiu8muzoHrvGncO14-9GuhDWIILXNVH004zA844DyE9XN5_O9qNOmuYKd5BQ2ODaW7HQ5EW4wvTG37JZyMRpbVFplGP2rP6rCxUqtZvzXwtL5R80sDKkpSZBAfLaaiNIqkOZqa-FSR_5C3sSHhXJ0Od0mCr8i2d1ibaSGwZMWrVj5E0c96O6kfdtfP8k39Kwh-B-IfaKw_VUZWEeshvYp_EHbwaXsqVqtvyfKobrfHUMVMvLu4qYFZe7ruRW1eb1qyGL8BXBWywwFFVX4v25EraAJ9pa7gF5zBsCQ97QyOMEFX_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی شبا میری اعتراضات و روزا میری راهپیمایی:
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66474" target="_blank">📅 12:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66473">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc0be5a6ce.mp4?token=u6q7oV66TqPhQdPilkvpfAj53kk6CbwDYi7qMNkSUVBUJR6rZ0N8oClBDefMknQansBx9yETk8rYDH5tOf776DhzKn8AFqHmirl9Z07XmD9-OEyQUpSJbNfdBG2PQENjhgeH4cbr96q7AVJ7PghqFAB09ERttPu4peh4xhmvm6_hnwIc0cRMByLnbPqF_IFt8HWg4LEmrjrQplXCH5j_wzY9Vsshn7bV8vmPu_buGIDLfZPP98bdoN8r0grJFz68VjWjP-raE6TXKGYIW9YM9Q3ENKcz4ZWsjpmdQ7lqVmsbTvi8ngoXSNN4MXXyDsCmIAas59yzmKrD1-VyXcSrFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc0be5a6ce.mp4?token=u6q7oV66TqPhQdPilkvpfAj53kk6CbwDYi7qMNkSUVBUJR6rZ0N8oClBDefMknQansBx9yETk8rYDH5tOf776DhzKn8AFqHmirl9Z07XmD9-OEyQUpSJbNfdBG2PQENjhgeH4cbr96q7AVJ7PghqFAB09ERttPu4peh4xhmvm6_hnwIc0cRMByLnbPqF_IFt8HWg4LEmrjrQplXCH5j_wzY9Vsshn7bV8vmPu_buGIDLfZPP98bdoN8r0grJFz68VjWjP-raE6TXKGYIW9YM9Q3ENKcz4ZWsjpmdQ7lqVmsbTvi8ngoXSNN4MXXyDsCmIAas59yzmKrD1-VyXcSrFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نبوغ اوکراینی ها در شکار پهباد
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66473" target="_blank">📅 11:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66469">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CHAVNHZCtN-Kpd8GuWCILORG_AMv13X8k32njZIe6AdzaCA4H9UOb9tF_5NYn9fE-cO7rddio_7-eMCwOKxpc51oFQyISlUC8kL_R5cdArb8mJ8e5Zs14PAPCLPfa-mrEeIZ9QMoBKrvbFvOp8XKTlaG3WmfMQmtbnK27EexdcFkDYWMvWp7h07Qh3P7Q-GFYom9ZCEaRWFVBnaC8d5e8HYiubI0M6ICYfIz1Js5vVcKZ4P0tsyfXDKJSQUE_7MHK6GFjG7bL1BPUXJrpWPF5sCBNgd4ljOwRe4uYVaTWiE2SOwvR4eV27w8u-qJCL8yLJHKoZUqkrnuYvGha2Xj1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t93V6j_buzmEiid7DXcfqKo5sKkLWADHoiIdUYtz0NcOWLlJQDHTjMBSu_BdYaE2-3N-EWD3ZnqEkmC8ecgnQfGVBvlXyjfNWOy5JiJNap4bNC1ws8aNukWiZKbJbOkrPVfgIwQLGjRW9d5nzW-6eHqZvXAmDbdlmcX0V2AVJqSMeslpSKxassJeMsCfybHxdTMBDiSDUNG_gRmXLS-93Zja4CVWBCRRIXeVaUEdqd9kH4Yxpt2GHqGkJcK-mgIfJvQw7I_2SMjNIl-A6lVGHIM7Z6YXO47LxkXcDaXBeaIUJJIJX42OjqRZ9ilRic3oAHwo5gHtPYnwQin2BjK_xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-07e-4qTRLvfC0lGgSzddassj9ErmktfFrBRSWXLTDalhanGZWV_JCLAxbSO-zTqVvmgPBYvwlMMNo8iqUrZmQfjW_EzzY_5to9W4cnNQpRTfoepQxAiHc9seDyxOAM_ECDHVwXvyHHvJgzG-1Kg-JIIqoc4defWdfjza-BnD0lvDzFSIYG4LvgXn9E7tcEUMf4l8PfiydR4MH4Wj-or15toSCvSmprKw-yy6GZUFIHJsCeQJbP9nwfd7b-W6iBqajEtF9oXOArg7ZvzUvnbCyl5ZzXTGr3Iy7-UFYOGX_KyOCGLEcg6Z15C-OVBjgA2EPib6YkHE2EyO9Ofza4hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cb0e601ac.mp4?token=LIWwdGXb25p0khs-O-prvGKck4vwlr6uft9Ad9KIWF8EwXiD2Z_Nwc99b8aqawnT1VHhBOm0osfl1owjo1QEarZ7_saOaXhhuX2p2hhkVbDyFreHpmCyJ6Nt7l_Q0tfTj95MIB1NYZcANXcCwWfFnpk3XnD7nuzXkv-xLlONPAGBhZPQb8JgYmugCB6KZAOP7RiyUUB-cw3QdyFZwKz9Z3d0k4fQAEdYcU3YERTwmFqDDuSNNZ4ElLvLwDVa8V7qa6WqtB3hHOJ2zTkM4xh8eMGbWntlpoTjOKdV09itMQ6OjwFPBwzDnZJVMxqz4v2w3Oys-fjMHv6P8DsU21ZjLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cb0e601ac.mp4?token=LIWwdGXb25p0khs-O-prvGKck4vwlr6uft9Ad9KIWF8EwXiD2Z_Nwc99b8aqawnT1VHhBOm0osfl1owjo1QEarZ7_saOaXhhuX2p2hhkVbDyFreHpmCyJ6Nt7l_Q0tfTj95MIB1NYZcANXcCwWfFnpk3XnD7nuzXkv-xLlONPAGBhZPQb8JgYmugCB6KZAOP7RiyUUB-cw3QdyFZwKz9Z3d0k4fQAEdYcU3YERTwmFqDDuSNNZ4ElLvLwDVa8V7qa6WqtB3hHOJ2zTkM4xh8eMGbWntlpoTjOKdV09itMQ6OjwFPBwzDnZJVMxqz4v2w3Oys-fjMHv6P8DsU21ZjLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حملات ارتش اسرائیل به نقاط مختلف در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66469" target="_blank">📅 11:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66468">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qmq3CdNi_RQ7x5UVmhvK4cBvSAWfx5Qo-doNBuWTyKxKP3WocYalxT5KEuc7Ui_xxgD_yEI8XmMZ9RPiXE6kg4Z0Slgi4kLePd2vLdV0RTvlaAAV8ipw8WDhG1woQPyo7hwVQ2VI1BiHjiggpyunoWTZjhjtOBQAK1OE9cOH-0Wxmp94zGazUH9ZuE8yABfzc9BOvnk8ZlAMOqJSPGXeoQbjuhO8wxGrR9OOp7uEmd73DaHK4BqBLdXMDCPaDQWJNV8Kl8RSU1X2rz_pUQqFo_nbjeZ7Wp0bqP6zUfDD1nW63FOvxUTmvNderXvDVsQLtm3K2N7VS8TBKMcnsGg07w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت ‏مسکو، روز ۱۵۷۶م عملیات نظامی ‌ویژه ۳ روزه پوتین در اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66468" target="_blank">📅 10:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66467">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7be955089.mp4?token=VH4yAe1B1EdocCP2wb1f591A52MthOzG7U5sTW0PGyWiNjXL6nJmF7sa4USBUBv69dHqIWzDGJTS-ytCdzfXe49e5elBN0K_4jbHoMSGtvoHhLvdSw403v6c6UqkcTVR9jvQRSJfKfJT0w1Z-0QlhLjYKgCYpaSrlURvzRoCCMaaNqc-SZTGlZiWQcd480aneft9D10MHmAew7cVP_mUZBiWF8hgOgBBtCbmHtI4p98VXTIcdn3jlFb2NcyVROjR2_Tbd-Vlh2V1N0DTNAwqRgKuN0XqYemaaqghtFyczBVu3eeaoBenakILNmoeQfpKgy_pu6NEK3xS07yxsIFFmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7be955089.mp4?token=VH4yAe1B1EdocCP2wb1f591A52MthOzG7U5sTW0PGyWiNjXL6nJmF7sa4USBUBv69dHqIWzDGJTS-ytCdzfXe49e5elBN0K_4jbHoMSGtvoHhLvdSw403v6c6UqkcTVR9jvQRSJfKfJT0w1Z-0QlhLjYKgCYpaSrlURvzRoCCMaaNqc-SZTGlZiWQcd480aneft9D10MHmAew7cVP_mUZBiWF8hgOgBBtCbmHtI4p98VXTIcdn3jlFb2NcyVROjR2_Tbd-Vlh2V1N0DTNAwqRgKuN0XqYemaaqghtFyczBVu3eeaoBenakILNmoeQfpKgy_pu6NEK3xS07yxsIFFmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری: شما گفته بودید که فقط تسلیم بی‌قیدوشرط را می‌خواهید. اما این تفاهم‌نامه شبیه تسلیم بی‌قیدوشرط به نظر نمی‌رسد.
ترامپ: خب، در واقع احتمالا تسلیم بی‌قیدوشرط است.
مجری: واقعا؟
ترامپ: من این‌طور فکر می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66467" target="_blank">📅 10:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66466">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/040ce8f378.mp4?token=SSoSdRqd3CoH8e3hn394VT-d4i9acdwQVEdbufn3ZHhgmJPTp0vdwTldqCI8qa1y897DS7huCIrD891bm6EAI-0WaBHoFVWKoKtBgmFFk-t9DgIOBgnFBFQOFTy8x47rCK46pe1pBr78zw7onxNLGzctayRYkzaevvap6-V4N9YT6exucYubx3XgG3j2wwayDz9biK_kzjQGLPm-5eBchZqor6Ik6zHubhs5On7UVceL4GGG435JZt-n55ODsV0dPQHDnclLTwGgsK9gcS3AeadWfeMw_jPOiYj52BQuPrZy7gX5laHt5ashNN7lxgYTpzP6_im4x_6fxYBadnWAnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/040ce8f378.mp4?token=SSoSdRqd3CoH8e3hn394VT-d4i9acdwQVEdbufn3ZHhgmJPTp0vdwTldqCI8qa1y897DS7huCIrD891bm6EAI-0WaBHoFVWKoKtBgmFFk-t9DgIOBgnFBFQOFTy8x47rCK46pe1pBr78zw7onxNLGzctayRYkzaevvap6-V4N9YT6exucYubx3XgG3j2wwayDz9biK_kzjQGLPm-5eBchZqor6Ik6zHubhs5On7UVceL4GGG435JZt-n55ODsV0dPQHDnclLTwGgsK9gcS3AeadWfeMw_jPOiYj52BQuPrZy7gX5laHt5ashNN7lxgYTpzP6_im4x_6fxYBadnWAnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ به شیخ محمد بن زاید:
وقتی انقدر ثروتمند باشی، میتونی انقدر آروم صحبت کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66466" target="_blank">📅 10:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66465">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/635e862fe5.mp4?token=vsIFxvlhFQQeKJs9hR04s6ujMoezr5T5PPfXLU6wlSPhIdNRMuVLntoX7LAd23SHW5Yw_vvZzfS24HA7cVEz4idFpBT6_0o6d4owxRzXZQfhrewpPZMm1x11vMRWLD4yfIUUA5mka4gq7hH4VDXZvST5JOWleNGWQyMUeXL5yX5FXjTrpJTKqb3MoSRrJBTjcr14Pwv-erZTH2_vTJOlMcp40koLDJSN8OYeO8jKV27K9MdFGxOUjZ947iDva8mlwI-qDg7iRmm55aF1pyKZ4Mvbpj4D-wsxdtNbcbEl4aUIkCJn9VDREu6xYJBRjBgqJDpKPLmh9lmxNffMBltbyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/635e862fe5.mp4?token=vsIFxvlhFQQeKJs9hR04s6ujMoezr5T5PPfXLU6wlSPhIdNRMuVLntoX7LAd23SHW5Yw_vvZzfS24HA7cVEz4idFpBT6_0o6d4owxRzXZQfhrewpPZMm1x11vMRWLD4yfIUUA5mka4gq7hH4VDXZvST5JOWleNGWQyMUeXL5yX5FXjTrpJTKqb3MoSRrJBTjcr14Pwv-erZTH2_vTJOlMcp40koLDJSN8OYeO8jKV27K9MdFGxOUjZ947iDva8mlwI-qDg7iRmm55aF1pyKZ4Mvbpj4D-wsxdtNbcbEl4aUIkCJn9VDREu6xYJBRjBgqJDpKPLmh9lmxNffMBltbyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختران حاج گاسم
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66465" target="_blank">📅 09:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66461">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tl92ZXq3WeXJDc32aMYj3QvfFnv7KFvSPDrPGcuE3welHakCj4V45biKNvxUCvmDrd66HKyf2hSXov39bpCj4MD78JPb9SiHtocOMPso4M5i5fjMd18UI9I7n8ZSSpLlHHyOF41hjrwnTk6kzbsGSP6162GwN2pvT8mp4x2Z2NHWXZ2h7mwdnxunvROPZng0G6TQ8ddrM0D40HfwE_BKRhfVkfZTRagKS69ihX6pU6euePcpD-08_P1zps2Q1Acy0cvOkKJGZVxqW735NVCBNHRhiiW6coxAPJZKgEOiGakPy43N0EbfcODDMfrUTfrVv9ALfIcv9Pn4wtR666Qy5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a17f4667.mp4?token=Uf9SpIwWtePkLRIrMeXrArTtKRbH4zYIDLqBR-otufSDqHD6ZE1EvzfyUZ8SMl0JyQHXg4Kq0pDMrbCGa8RRqUD7osKb0T5_zWjQoCnqGlaTqi-SHFoD8gfWLcRTzfPPPHirDTCZ3xe7nD5LEwUebKTASlfAwXgWx9ppFOvYPHS3N5UAWjXGJtzVHQ_yX_Y9OiQA4VkF63AQTr7YTH36je7JpvceIbGgIjcbRes2YQEPKMSKM1eCoO5r3BcYPIYjbNZmVc1ihm6O8pwL0r9QZcJqt3YMJd2gs-524PCmQ7hRiUDKxdeIrdxGWf1FY97NgJM9Rd4b3QdUtol5El5zrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a17f4667.mp4?token=Uf9SpIwWtePkLRIrMeXrArTtKRbH4zYIDLqBR-otufSDqHD6ZE1EvzfyUZ8SMl0JyQHXg4Kq0pDMrbCGa8RRqUD7osKb0T5_zWjQoCnqGlaTqi-SHFoD8gfWLcRTzfPPPHirDTCZ3xe7nD5LEwUebKTASlfAwXgWx9ppFOvYPHS3N5UAWjXGJtzVHQ_yX_Y9OiQA4VkF63AQTr7YTH36je7JpvceIbGgIjcbRes2YQEPKMSKM1eCoO5r3BcYPIYjbNZmVc1ihm6O8pwL0r9QZcJqt3YMJd2gs-524PCmQ7hRiUDKxdeIrdxGWf1FY97NgJM9Rd4b3QdUtol5El5zrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات شبانه ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66461" target="_blank">📅 09:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66460">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66460" target="_blank">📅 01:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66459">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t60kCgBodKSVVyjnbwfzxGP6Xn9-uUcvNOX6FzBJRshKwUrrYOh9U8ioIHgLBAu_BB21ZhH0VQYjNsPBUOWzIwS3n-bqUo7sL_rIIETj6kVqfFS0atlpjRZKzYMaWFvqneyBgyAQna-NXw3ITdYjalx8BfH2a5Mdk33wl7UkZ7sekUwd7USmylH84Z--bMya4cMjwV3PczbvwmDdxa7sHejcVKTX0aKseEIrHf7Q4xuYDnhcPSs3S9nykyVx4jvt65wD7KpmyLpG9dWUMnmsJt1Sad9clgRCV6veNdNwgcFfcXV1b8kiTfuiQgsdXbHW5XRSDpspd3pYXMZHBiSzpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66459" target="_blank">📅 01:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66458">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
‏به گزارش المیادین، هیات مذاکره‌کننده جمهوری اسلامی در پی تداوم حملات اسرائیل به جنوب لبنان، سفر خود به سوئیس را تعلیق کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66458" target="_blank">📅 00:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66457">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30a4159b30.mp4?token=sYNxi5TYzzCOXr_oN3CdtaKaAiSbkOyWGRm3MtNvWIjo5IW10RHUrLzefSQPZ7XSJpUI-scbMtnChEy5sZf8lFjmO_kS9kjmiZL9aFe2ryUlbsnpsxk3p0d0pcbjPM0fFs0-Z-Ph5KI7AX25KS1hh9ZMyLiC0As0Dyst9-E4TsV0pmZe-tJ6GtOsAGSKj6OFOO_7ZOcbKZxdj10N6cN7pQtFeTm2VYmLS8nOz1S4nhVO_UF2oxw00lr1rQJVycpmmlAuPJWFIQ7PoNu_CUiIa03mIDibxvEHdeUx8yaOr8-SKt0jna9UUeGs0HmerRMYZoRQa1wIOqPJG5Zbnpd2kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30a4159b30.mp4?token=sYNxi5TYzzCOXr_oN3CdtaKaAiSbkOyWGRm3MtNvWIjo5IW10RHUrLzefSQPZ7XSJpUI-scbMtnChEy5sZf8lFjmO_kS9kjmiZL9aFe2ryUlbsnpsxk3p0d0pcbjPM0fFs0-Z-Ph5KI7AX25KS1hh9ZMyLiC0As0Dyst9-E4TsV0pmZe-tJ6GtOsAGSKj6OFOO_7ZOcbKZxdj10N6cN7pQtFeTm2VYmLS8nOz1S4nhVO_UF2oxw00lr1rQJVycpmmlAuPJWFIQ7PoNu_CUiIa03mIDibxvEHdeUx8yaOr8-SKt0jna9UUeGs0HmerRMYZoRQa1wIOqPJG5Zbnpd2kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
آیا در جامعه اسرائیل افرادی هستند که بخواهند ایران را به لیبی تبدیل کنند، یعنی یک دولت شکست‌خورده با ۹۰ میلیون جمعیت؟ احتمالا بله.
اما نمی‌دانم که بی‌بی (نتانیاهو) چنین چیزی بخواهد.
من شخصا هیچ‌وقت چنین گفت‌وگویی با او نداشته‌ام. گفت‌وگوی جالبی هم می‌تواند باشد.
اما همین را الان می‌گویم: آیا تبدیل شدن ایران به یک «لیبی ایرانی» برای ایالات متحده آمریکا خوب است؟ قطعا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/66457" target="_blank">📅 00:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66456">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47cfe42200.mp4?token=LQ1KvDxhxTQIRRnn73dS_4lYdRD-dbF76DZhQQkY0rhGn-0OPRcbB_Po0X7HDTTswaus-mzPmcmZc--Il4gAF5XAAokD4zWC1UKCQWrYrrLAa8-2JGPXaTaYbWJmdp0Vip_1RP4Gc2nvQEX7pP1GuSiexlUYlubUAwBbKp1tTaLDhTS2m5utl9aUZ3AuewsgHVj7E3U4h5NTY4nsnlGZPNVRG996KzmqvlQnjyFlwNEXUiUdGfB_HEQKCR33rVrcm_lnol7TPzo9kmqb4h6p1G7OirOTfibK3ZcTB0vmo-f1JJaggJb__6LUmxCeo99-8IHIXQGm8m-tkVu-MtK87w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47cfe42200.mp4?token=LQ1KvDxhxTQIRRnn73dS_4lYdRD-dbF76DZhQQkY0rhGn-0OPRcbB_Po0X7HDTTswaus-mzPmcmZc--Il4gAF5XAAokD4zWC1UKCQWrYrrLAa8-2JGPXaTaYbWJmdp0Vip_1RP4Gc2nvQEX7pP1GuSiexlUYlubUAwBbKp1tTaLDhTS2m5utl9aUZ3AuewsgHVj7E3U4h5NTY4nsnlGZPNVRG996KzmqvlQnjyFlwNEXUiUdGfB_HEQKCR33rVrcm_lnol7TPzo9kmqb4h6p1G7OirOTfibK3ZcTB0vmo-f1JJaggJb__6LUmxCeo99-8IHIXQGm8m-tkVu-MtK87w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس این انتقام ما چیشد؟
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/66456" target="_blank">📅 23:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66455">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad18edc1d.mp4?token=BWUiIJVadRaJRv3rgW7JRpF77J58863gkCgiCPa6syTe_ovJkdlBCV9soZtbG_9547Mi8C2M9TrAPMTNNLgA28Hx26hdlpjZhNi9dmNLfSGWJmeRH2cTS0wkIDJqymClMni6GnKi8v_wB0Yqyqaau0P7I8Cv0j1zpRZw5HCBOprAGUir2fCj_XZ4lfc92qWbpqXQA7V6KknE5V0JdkiIhJoE023kkPdCwjOYPgM5fR617-Z8o8Xc-lerxD9vrBdRPbm3v2RKH5di5KfSb1B662-S-dxQEwT9h3kapU0-McsL5b--vGOyx3elPmQOUxtiGap2ErgH3rhpenghDog2dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad18edc1d.mp4?token=BWUiIJVadRaJRv3rgW7JRpF77J58863gkCgiCPa6syTe_ovJkdlBCV9soZtbG_9547Mi8C2M9TrAPMTNNLgA28Hx26hdlpjZhNi9dmNLfSGWJmeRH2cTS0wkIDJqymClMni6GnKi8v_wB0Yqyqaau0P7I8Cv0j1zpRZw5HCBOprAGUir2fCj_XZ4lfc92qWbpqXQA7V6KknE5V0JdkiIhJoE023kkPdCwjOYPgM5fR617-Z8o8Xc-lerxD9vrBdRPbm3v2RKH5di5KfSb1B662-S-dxQEwT9h3kapU0-McsL5b--vGOyx3elPmQOUxtiGap2ErgH3rhpenghDog2dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
آنچه من به برخی از منتقدان این توافق که شنیده‌ام می‌گویم این است که آن‌ها می‌گویند: “خب، ایران این همه منفعت به دست خواهد آورد.”
من دوباره همان چیزی را که قبلاً گفته‌ام تکرار می‌کنم و احتمالاً مجبور خواهم بود چندین بار دیگر هم تکرارش کنم: ایران دقیقاً چه منفعتی به دست می‌آورد که قبلاً نداشت؟ پاسخ این است: هیچ چیز.
آن‌ها هیچ چیزی به دست نمی‌آورند مگر اینکه رفتارشان را تغییر دهند. اگر رفتارشان را تغییر دهند، آن چیزی است که باید از آن استقبال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66455" target="_blank">📅 23:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66453">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‼️
یسرائیل کاتز به کانال ۱۴:
ارتش اسرائیل دستورهایی دریافت کرده است تا در صورت لزوم، برای عملیات دیگری در ایران آماده شود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66453" target="_blank">📅 22:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66452">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZDX0DCRQvYNGcegc1Jv4LWiE5uGV34PzcKs16G6eymNT_mXjwBN2YqnxoUpLha-OMYv3ovzJ897SAegFUbvnzsue_D-toNoQ-uYPhFg9R0xE92ZUHILhgQ_KzC_Js4fKnp412bD2J8T529Hu9rRnXwWEVF0IBHF3cjshkyRSyF9Q_qSvBSFNGx82WQd3Fvh-s7t7xvVXEipOxj6p1X5GK3njAZYoHdSTw6bb6pESStNq0Hv5VEtM29lmykbOnVL94Iv3bhq90ByjuRGd6_Sr_-t9xiaTGunaYCfypyYhCeKwHZ9cGy-biVsjPu8WbGMReH3cLooubY4Rr2my9iX_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در تروث سوشال:
ایالات متحده به صلح متعهد است و ما همه را در منطقه خاورمیانه تشویق می‌کنیم که به تعهد خود برای پیشبرد مذاکرات ما به زیبایی پایبند باشند. بازارها از آنچه که با کاهش قیمت نفت و افزایش سهام اتفاق می‌افتد، لذت می‌برند. ما انتظار آتش‌بس کامل در همه جبهه‌ها، از جمله لبنان، حزب‌الله و اسرائیل را داریم. از توجه شما به این موضوع متشکریم!
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66452" target="_blank">📅 21:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66451">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">هات نیوز | HotNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/news_hut/66451" target="_blank">📅 21:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66450">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم  @News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66450" target="_blank">📅 21:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66449">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">این پیام یعنی پایان پزشکیان و جریان اصلاح‌طلب در ایران، و آغاز حکومت نظامیان به سردستگی قالیباف #hjAly‌</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66449" target="_blank">📅 21:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66448">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم  @News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66448" target="_blank">📅 21:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66447">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8zdBurWzLtslhvNWBhDmo7QVeCzmqPO25SE2ct6IPKonE9FQGjLm1DtGH8UYS6GDSF0HW6gMwbuBR918-EpiAV2uaxuzx3tnLeSkQBp30nWyiaoo3_h3F5kspWQDa46ius5QgKdtJq1542_IRPIhUrLWNKVxtXWX9HCPMXEHcIcgy5lOQmVOLQ1q_AtiPQkrl9Su-sVjGt_RmkqBkdu7tWPue0vOnDmKymfYf2UUMGxYRIKx2Z1WCtg4A6QU7eHCvhZ3mjrZbK718uEFEOzHAz-GMmEApehnUIwJEu5jvqDF6nIbRVFhWN7soDrX-arDcA74mvMkbSHDCxeKSdjkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/66447" target="_blank">📅 21:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66446">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3MYBY5JGgi4_TmdtTGAa_V7SLyu4bpMdVfn4RfojIlPI0D1cKsrORUc-qe4wL_nya7W79KCrhdZuO49oM7WFgexLPVuQgZgDXl49vp3l-Tlcmpw7qN4DVhnDs560b05EkAc1VhlqpqkyJJJ3G0fl_qsS3dmBgBuumcQoAc9ckkM62rR1aBVxoVKfI9KIS1v384EI1Cz6iejWJlWCYlOrKwFfizg3cxD8TquzEjeyMu38xBC7eoKS7t2BBuGxtgdva-aoM3uKeoD03qXlkj_vW_lBKlM1QxeB5auJycJ07OUGldWCHcUU3bMD7ccbqQwDcyYtumP2SZlleGeQPMD1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ: آمریکا هیچ پولی به ایران نمی‌دهد. اخبار پرداخت 300 میلیارد دلار به ایران فیک است. تمام آنچه برای آمریکا وجود دارد، موفقیت، کاهش قیمت نفت و پیروزی است. وضعیت بازار سهام را بررسی کنید. پروپاگاندای دموکرات‌ها در کار است!!!
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66446" target="_blank">📅 20:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66445">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏
🚨
🚨
🚨
⭕️
سنتکام اعلام کرد، نیروهای آمریکایی محاصره اعمال‌شده بر تمامی ترددهای دریایی ورودی و خروجی به بنادر و مناطق ساحلی ایران را لغو کرده‌اند
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66445" target="_blank">📅 20:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66444">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f51df7dfe.mp4?token=m9l_GmaJXQUKcJ3fyfniYRHiIHJCq6kEgagYvg2F41qz2l0pH3e8iELMdI6wj3JMzf4zdSnltGZcHSk-C_W6yJeX1qydBeXKruzCYQQUm8Kx7l-tM7AvnxetsR9Vt9prfYxIO4vHOJIuJOFwUlKw0AhuLvVbeqshJFThZ70HsBaC8KmFrtzPDBtgWw7bVPbaFspTDZM0M9YlFAllXf3c7E2iCC3O_LWpRoCQ0wVCXXNU1IT2Avnh6rcJtSrfGj6zlSV267h3Rxt_ILK0eqF7FlsU_bl6fo8jqacpt2NmqGjtq_e8tvwVqI4QHzNotSLrFZXXHmYZlBdNo6_ApCtbjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f51df7dfe.mp4?token=m9l_GmaJXQUKcJ3fyfniYRHiIHJCq6kEgagYvg2F41qz2l0pH3e8iELMdI6wj3JMzf4zdSnltGZcHSk-C_W6yJeX1qydBeXKruzCYQQUm8Kx7l-tM7AvnxetsR9Vt9prfYxIO4vHOJIuJOFwUlKw0AhuLvVbeqshJFThZ70HsBaC8KmFrtzPDBtgWw7bVPbaFspTDZM0M9YlFAllXf3c7E2iCC3O_LWpRoCQ0wVCXXNU1IT2Avnh6rcJtSrfGj6zlSV267h3Rxt_ILK0eqF7FlsU_bl6fo8jqacpt2NmqGjtq_e8tvwVqI4QHzNotSLrFZXXHmYZlBdNo6_ApCtbjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس در مورد اسرائیل:
در طول سه ماه گذشته، دو سوم سلاح‌های دفاعی که از اسرائیل محافظت کرده‌اند، توسط آمریکایی‌ها ساخته شده و با پول مالیات آمریکایی‌ها هزینه شده‌اند.
مشکل اسرائیل دونالد جی ترامپ نیست و هر کسی در اسرائیل که فکر می‌کند بزرگترین مشکلش رئیس جمهور ایالات متحده است، باید از خواب بیدار شود و واقعیت وضعیتی را که کشور در آن قرار دارد، ببیند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66444" target="_blank">📅 20:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66443">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab365474cc.mp4?token=gAGxrJM1dAW3oXjasFDJda6sN11rNFDjimciVp0ecQ8gmXPOlXWtbQOa5a_8VkkkOifs1TDFWothmfiYT6bxMgdI5hD81PtrldtSs0L7nFwNLK9TIrIShPbqCOviR1q4srE-Bri_5GzEyfKYfySxK1TUCaJR0xgRaNgRbBgjAcLKnIhHtyRW6Mgc4tetULRcu0NIFaA-ZC64EL8abheuqABkym9myLbGLY5KEulYkIRbPy6r6-aRDEAJ5m2cSu3kCSv1HFdWKVW14T0B6_3iL8Lt-6RbZQyzxWo4FyjXA-sidvxf_F_rQKTLci_wDk2XuiHx0yeRaUWBNge2E1fuLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab365474cc.mp4?token=gAGxrJM1dAW3oXjasFDJda6sN11rNFDjimciVp0ecQ8gmXPOlXWtbQOa5a_8VkkkOifs1TDFWothmfiYT6bxMgdI5hD81PtrldtSs0L7nFwNLK9TIrIShPbqCOviR1q4srE-Bri_5GzEyfKYfySxK1TUCaJR0xgRaNgRbBgjAcLKnIhHtyRW6Mgc4tetULRcu0NIFaA-ZC64EL8abheuqABkym9myLbGLY5KEulYkIRbPy6r6-aRDEAJ5m2cSu3kCSv1HFdWKVW14T0B6_3iL8Lt-6RbZQyzxWo4FyjXA-sidvxf_F_rQKTLci_wDk2XuiHx0yeRaUWBNge2E1fuLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏جی دی ونس درباره ایران:
آنچه واقعاً اینجا اتفاق افتاد این بود که ما روز یکشنبه تفاهم‌نامه را امضا کردیم. این توافق‌نامه مفاد توافق‌نامه را تثبیت کرد.
چیزی که ایرانی‌ها پیش ما آمدند و گفتند این بود: «ما دوست داریم متن را تا جمعه منتشر نکنیم.» من واقعاً متوجه این موضوع نشدم - می‌خواستم متن را فوراً منتشر کنیم. اما برای اینکه با آنها کنار بیاییم، گفتیم: «مطمئناً، باشه، تا جمعه صبر می‌کنیم.»
و سپس آنچه در روزهای دوشنبه و سه‌شنبه، در حالی که رئیس جمهور در اجلاس گروه 7 بود، اتفاق افتاد این بود که شاید رهبران خارجی با ایرانی‌ها صحبت می‌کردند و آنها را به انجام این کار تشویق می‌کردند.
ما قطعاً به آنها می‌گفتیم: «ما تمایل شما را برای منتشر نشدن متن تا جمعه درک می‌کنیم، اما می‌دانید، ما در یک سیستم دموکراتیک زندگی می‌کنیم. مردم آمریکا می‌خواهند متن این توافق‌نامه را ببینند. ما مطمئناً دوست داریم هر چه زودتر آن را منتشر کنیم.»
و بنابراین آنها به این نتیجه رسیدند که رئیس جمهورشان آن را امضا کند، رئیس جمهور ما آن را امضا کند، و مهمتر از آن، شعار را تکرار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66443" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66442">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66442" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66441">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qtOxsQ0WkN2YuU_hVAoQKdYm00PqVpmt1788d1T-h3ZxXYcNU8-PWO2DrwJYrDR6r9PxxfDUOKb6K1g_YsWKSbwXtenI8fqQPSMGTbalhc1ckHfr9OaUlmEl7Bz7_kNc_8XGbW53NHyM4pnnqnIJmU5LomJzPszeYX-lh43ciWRrtipJ0shZEBsRc7wSm3jsl-yZDQIq_JRG3slrJKrdKD85BrIESo_ZXmCj6bWbUWOyjFCRWMFP451m-LFzPftggZcETgU5BEmyBRRm-9r4cxjQ5uc5gZM5t4FdCb76BK22mK6TGernqQuc9rLyHlful-CULiAHgf1b9A7PLl5q1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66441" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66440">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b31dd3b8.mp4?token=nFXFo-5ttWY2cFzo9S83l1QK0HIeD6QrshoVOv6DUkcr-hTlG0qDV6DTL2h0wk0V7R09ahmyoDV7-iOa20nHKSSzb8Y9kQzBHDyOu_nWMZPQxK1l5CsOM4ONWbWvVniKndzQeTJdzQRKG_D9zifCbu023EnCmXgHVolsUdj6O9pvDIwC_75i8CKl3jBxaS63Cr4TOneNyvB4J0wrDZRvgBoxV_Yz31ZBMfoEeXql3c8cNXmBpEtmrmTMQPnUNJicWVDiUn95HtoJPAd3OwY4i_yOQhRRjniwK2g9POo8lBvUYEdKjshi_qlrokFz8wHdnvU5joTixoC-WuvXtG7JZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b31dd3b8.mp4?token=nFXFo-5ttWY2cFzo9S83l1QK0HIeD6QrshoVOv6DUkcr-hTlG0qDV6DTL2h0wk0V7R09ahmyoDV7-iOa20nHKSSzb8Y9kQzBHDyOu_nWMZPQxK1l5CsOM4ONWbWvVniKndzQeTJdzQRKG_D9zifCbu023EnCmXgHVolsUdj6O9pvDIwC_75i8CKl3jBxaS63Cr4TOneNyvB4J0wrDZRvgBoxV_Yz31ZBMfoEeXql3c8cNXmBpEtmrmTMQPnUNJicWVDiUn95HtoJPAd3OwY4i_yOQhRRjniwK2g9POo8lBvUYEdKjshi_qlrokFz8wHdnvU5joTixoC-WuvXtG7JZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
ایرانی‌ها برای دومین شب متوالی به هیچ کشتی‌ای در تنگه هرمز شلیک نکردند. تا این لحظه، آن‌ها به تعهد خود پایبند بوده‌اند.
سنتکام اجازه داده است دوازده کشتی از محاصره دریایی ما عبور کنند، بنابراین ما نیز به سهم خود به تعهدمان پایبند هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66440" target="_blank">📅 20:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66439">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csl18mIi-LDXt97ed4phJGjzWZN3fC2F_HN1smxTM5g5bmApYWi9h50WnCkXQVL-WhPV91gGE0umnXZONyskZ5ihSQSGuKpq-V8vjBapHgExQ992AlrH1w2RnXfCRzW-g8LN-o0GNC48hoGqyHHd1rG81KCTbrebMLkirI5VYIt3DJMFYwPDEzvFEkKekfXis0VuzY3PGg5xVIKeMT966btIsbkzEWgrQjHf7z8mAkPOQ1fRYxaFUXONVPYZ3dHl2gjhcE2z1HqB4Nkax8pxhGEpuzuhlnQrdVz3lj0SjyQV6qzeIQ9qEqCArNEQ9nwCJDFsf1hHtpPeRoPWQlQk2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
فایننشال تایمز :
گزارش شده است که ایران به ۶ میلیارد دلار از دارایی‌های بلوکه‌شده خود دسترسی خواهد داشت تا کالاهای آمریکایی خریداری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66439" target="_blank">📅 20:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66438">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdafCfjlAxMc8Vn7SDAZjWhWNOA4Yo3Y8dGDaihlvbgiMSRitrLU4Ic5JBYFopfLH4LF_uAlUIU7IYBXebaEp65bZOuQGS4KPOtH5eK7uLBqWLIBZBaR4prUeor848CdRWPHGfydObZagy-EXAGVfBmoPDqJ9E2m1AaKbR0386Xw2QPOay8f9EF6SsYwu53JG_LI6afazb_YY4ojJY9CzydAXsRkcOMHl-xGkUTA7njv_UX3L_p4RheliSVWXuOjMmGqyQanxOtsAnkOTQT0Xe3Ca9yjn-_6OqcNKOQmNY5kiFC5CrdadMw7mI_-e4aqXZhZPWpSxFFk6jeP-87AyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
ونس: کجا می روی دونالد! «امام مجتبی» منتظر توست!
دونالد: از روی امام شرم دارم ونس! شرم! توان دیدن جراحات ایشان را ندارم!
ونس: تو هر کار توانستی کردی! تصمیم امام اصلح است بر ما!
دونالد:‌ چه کنم! چه کنم ونس! با این جماعت هزار رنگ٬ که دروغ را چون «رج قالی» میبافند! امام مان تنهای تنهاست! شرم بر من ونس! شرم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66438" target="_blank">📅 19:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66437">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4fb90d19.mp4?token=eOkcrgaFev78i3oPUOdP63cngFDjpm2XSAHM_2TBtJK1WBnc6YzlbA2EE8UliGWGXh7aj5RxjVvw8z608pPgxC51cGqhBYr9PIpQS9TvgsJMEXn3Jd68RwmZusPv3t5_KgezWKfsSKL59h5n7THTl5gTNb233nEDliReXwvozFLQIbhVRqk9R-yfJeQPAmIbOKQqgHc9Sa_0kXk63zzAmxOxM8ilw_ad5TOaZ5mqROT8a5EuKHYRVaaeJqButyOirLTYi0gJVPBaqZunenu8cmXFTi5d8lxM5L3PqescmpoGSLA0rJu8GPQCj_dAUSWWv3XYk-9lfiCjFxmtkyqyfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4fb90d19.mp4?token=eOkcrgaFev78i3oPUOdP63cngFDjpm2XSAHM_2TBtJK1WBnc6YzlbA2EE8UliGWGXh7aj5RxjVvw8z608pPgxC51cGqhBYr9PIpQS9TvgsJMEXn3Jd68RwmZusPv3t5_KgezWKfsSKL59h5n7THTl5gTNb233nEDliReXwvozFLQIbhVRqk9R-yfJeQPAmIbOKQqgHc9Sa_0kXk63zzAmxOxM8ilw_ad5TOaZ5mqROT8a5EuKHYRVaaeJqButyOirLTYi0gJVPBaqZunenu8cmXFTi5d8lxM5L3PqescmpoGSLA0rJu8GPQCj_dAUSWWv3XYk-9lfiCjFxmtkyqyfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار:یه مرد دانا سال 2020گفت ایران هیچ جنگی رو نبرده اما در هیچ مذاکره ای هم شکست نخورده
ترامپ:کی اینو گفته؟
خبرنگار:دونالد ترامپ.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66437" target="_blank">📅 19:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66436">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhiogrWojxJsw2aC0OItDiJexUMnOan7lkbBNNtcMvolDA9ZkbYAUASi-XnkKegN6mDkDSpOkUMskopCmMFgGmB7XzQ1EvdxfwjO6tWt4V6t5QRfX6SVWP2I5jHN8sxlziv0Kwpw_DCtktRHGNZwZDkq7xD4t_nk6fHUks45Es2PX8p5LfADW-ZAt--wYKMh0-iS5XZkoQrBx2jj6xdhrt55W9tMsdR7JcvQq6MSYRqLg6tfd3ummRfDYkEeM2cateuaiOCXP-FIGSqGPI1Fk2-eV3SM-gKAhOcWSjjQY6sIh_4fXDPCHx76Y-geI8w4eQTYIavZy47mMXtlJuxtRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
الجزیره به نقل از تلویزیون پاکستان:
سفر برنامه ریزی شده شهباز شریف به سوییس بدون ذکر دلیل لغو شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66436" target="_blank">📅 18:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66435">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnsfeQtRhitoskmatdQvbAwcJXVQ3AhK9jeZBthjVZf2k8Oy7mC1GgfZCJxbZstadqKTK9ZUaSc3SJV9deYR1sc59y142cdzSiWvOYkf7Tc3bAHKyC1quWy8-lGbbYuVFll3VJ1Ctg0eBm-CN2iqmmr4MWy779SQpwo-niMiFOvwoWFzfnDk357bAwNH1RHPTaq4EPuQCB2wX3cGz2AzSHeEBIqePqZmvZdjlRe3OiTGzZD3oa9aXgt7Cg4NaJbdffv4Eg1ObLVCg2DnfyltA3xw4-tvwWmQaSLK0h1N06D5YA_NzVN6pPp-rzHZIkLScaXJiaqwRl3N8ioU5ayBbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
نفت جریان دارد، ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد (جهان امن خواهد بود!)، بازارهای سهام در حال رونق هستند، مشاغل رکورد زده‌اند و قیمت‌ها در حال کاهش هستند (قابلیت خرید!). کشور ما قوی، امن و محترم‌تر از همیشه است. «خواهش می‌کنم!» رئیس جمهور دی‌جی‌تی
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66435" target="_blank">📅 18:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66432">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jl3itmAUw2VthTjcWg-agbc7Z9oJHNvUmq62arobMzgMCdxd9GRqls3yyqgC0Nf7YZ-NQFkPb7PV7siQwk9VDDG3P9qRJgzZl6MWiWdUZpixmJEjn6IcDwKZokbz8c4DQ0oMlR24y452T7PkjCVR6FhPoRmu7Q2gWyOGA-4s_2jSiE1Uizlv327H5-Wf1JeFhKrRfA3ZVV-yi_3ilR68-FK8db3IY_svruYCwvTYJ0mzRTzPCbLAe7wF_g_LhyGKv88ffWfMFtpNwcoDe3-LgOWf4G_2Bct2-gSaXMxAWay1Lwgaae2R51NLNA-YTmXeuNLgyzg-rio2fRvdo7ZGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uIoc6pNd5FVcWhOPvf4Gi26l2lJwBXqjdK38sPWan9-Kn1QSEvRfPiZExMB55s5BJCiMg6-oVRuBrQWTmxg5do_pRgs4ywXbnMpOPsk_sXcwLyYJtQ8epU3s-Tdhm41qnXh1efQPchMgSphzekPzXxODmKLZm2EqR758zHz6V_klAOUaI104y4d0wAIb0lryb2E_t95U0uWR3iULBtidyT0heE6_BfOCsrzibSc-lTih6W6U8h3E0C7rBX8sLb077FuaMI09wg2SWmtaaLKkOJqrUYmMY61e1J_clQ3cIlMxuRyJ7gkDJghT8pBYgkmQL7bhLNSFNAN10vKcuu1SEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13c6e64c5c.mp4?token=iMFeXjxmkxrUjf_j1kCicfLwF5SPIORoDYwyOpIIfdGfj3MbaGkbdmwU2dm4jdzlDTFBkauruVrJOKbD0zioKfo6gWoMj7Ec25ayzDxsJqqv6RgKJoAkqjsMhejP74LY2DVccQBd-xp_CjrpuKA8QKCE7F1xSGacDGh5VVAf88v4pGOMEm0v3JbVewbkW-RmEQ1CJJ4Om7huDnbGLu-qCkmHIuntwBuU5QH9GYljvTI-PuWD9A6Sr5r9PNjl7lsGdhIx1w4tSJ-01fz7fiwNXglS3KRHrrP_2_fGZ0HpEHnfv6pAMKcBHhpNqHCWhGmc3_3a9_qjsocE5vOOQIHB2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13c6e64c5c.mp4?token=iMFeXjxmkxrUjf_j1kCicfLwF5SPIORoDYwyOpIIfdGfj3MbaGkbdmwU2dm4jdzlDTFBkauruVrJOKbD0zioKfo6gWoMj7Ec25ayzDxsJqqv6RgKJoAkqjsMhejP74LY2DVccQBd-xp_CjrpuKA8QKCE7F1xSGacDGh5VVAf88v4pGOMEm0v3JbVewbkW-RmEQ1CJJ4Om7huDnbGLu-qCkmHIuntwBuU5QH9GYljvTI-PuWD9A6Sr5r9PNjl7lsGdhIx1w4tSJ-01fz7fiwNXglS3KRHrrP_2_fGZ0HpEHnfv6pAMKcBHhpNqHCWhGmc3_3a9_qjsocE5vOOQIHB2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پختو پز اوکراین در مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66432" target="_blank">📅 17:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66431">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bf3ba597d.mp4?token=Rpwl-vo733ZCwe39qeOKts1RZYCmnpzCHsCVBnDsiq3J_mCpDXy63q4D7utX7S6qHIHtnn9J1_ls_bcqM3GR-u-ZIZWIqsbot9SjzFVLsyY26ne28uWT2zM1LVPaAsTlIuKq5cKyt37fWdlgWQ5YRy-clnalvBH34aQjtAhaAG6iEs7RhBdK4lyj0bUzXvTMqeICKXomhpLKB2Cfvr5ILeTAy4MqxbjBj9OWe4n_GDspdJRi8N5QeDUsR1O4vmIs8JJwNbi7DA-Rkre5HeUeHaB6pgrv4awJKyjcIGOkFjwhehC1v-glpzO4vzcxhgwATtHSEYebdSZ09AhEEw21_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bf3ba597d.mp4?token=Rpwl-vo733ZCwe39qeOKts1RZYCmnpzCHsCVBnDsiq3J_mCpDXy63q4D7utX7S6qHIHtnn9J1_ls_bcqM3GR-u-ZIZWIqsbot9SjzFVLsyY26ne28uWT2zM1LVPaAsTlIuKq5cKyt37fWdlgWQ5YRy-clnalvBH34aQjtAhaAG6iEs7RhBdK4lyj0bUzXvTMqeICKXomhpLKB2Cfvr5ILeTAy4MqxbjBj9OWe4n_GDspdJRi8N5QeDUsR1O4vmIs8JJwNbi7DA-Rkre5HeUeHaB6pgrv4awJKyjcIGOkFjwhehC1v-glpzO4vzcxhgwATtHSEYebdSZ09AhEEw21_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تردد کشتی ها در تنگه هرمز پس از امضای توافق
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66431" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66430">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8kXgPhpaM3J5v4cCAfs8QbnOZJeARRCm6PW6-GEsXaTIUODa3OjXsiS_1HlHFD6v-UvdFwWbkhJ2tPOms-7TkhdAWOERJ1D_ShEPqCnVQvt9nDUHmCbGhUqqSoUnOPQNtPrwIBnH8Z5MSYFiDVJt_TTHrW5UvjDQNNIHBA3PKl8H9ADp_5OWClfa3ydEMqiHC3yjXspFF2cnUzKmXAp1G7QjMQnNVJNZMF7TZcjT49hWSI_Ep6GPMHrFh-PfRdDVo6eKKjH6rF750ZbVvWfM_g7zJEOknM2kBgm3hOTofgPkq2kVLFQhENkQic2QcVpuMbsA9BhCUxO1GOu9YxB1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ارتش اسرائیل؛منطقه امنیتی فوری در جنوب لبنان:
نقشه منطقه‌ای که نیروهای دفاعی اسرائیل در جنوب لبنان در آن فعالیت می‌کنند
بر اساس نیازهای عملیاتی، نیروهای دفاعی اسرائیل در منطقه امنیتی واقع در حدود 10 کیلومتری داخل خاک لبنان مستقر شده‌اند.
نیروهای ارتش اسرائیل در منطقه عملیاتی جنوب لبنان مستقر شده‌اند و به تلاش برای از بین بردن تهدیدها و بهبود دفاع از جمعیت شمالی ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66430" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66429">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ub1X20Oli052NheEPSyskOGBpgTbtMnry3M0G-6SFwuPXmeXorN0_4F3qSMmwnBlwLJGawyY1crPn4EOHkx6N38GhpwwXdaLMOkdLwGjzTb2K9HQBcFOvPXmhzCzqdHcE--nR9xphuQTHQoX3ywlyt3rKOWgfJQsc552zONiJlR6AoHRHtfeEiVNjXyTZ9-OHmP20DaiaARZxKb2hvI1djt6gHp46dQaPM6W4ZU4rJVSBbvVded_IYyAT0SGulFaS9k4m8HDL4mCylie9kU-jIAJZzg-1_YQhwy4D5D_2wnUkPMBG6tY0trhA3oO4K7F1aLVRbSO8PY-NLfg22L2ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان؛این یک سند تاریخی و پیامی از ایران مقتدر است:
صلح در سایه احترام متقابل تحقق خواهد یافت.
جمهوری اسلامی ایران به صلح جهانی با حفظ عزت و استقلال، پیشرفت و همکاری منطقه‌ای همواره متعهد و پایبند است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66429" target="_blank">📅 16:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66428">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/622db6728d.mp4?token=ZjORRs2iPt0ZAoPgIiZ5a8uvtuKwgi5IWOLAnl4xNt-I1HM6A9h69Rq8DpZyC8ZTIKMncKOm3UHttXKvp4kTpp8MLlTBFrbaisAlUVyq8gYh5xRCn82UH5ERImKps5CjVZb_0JxQG5R78wGcGIj5vm6-1aW56J3AfPpr1tPcRkesLvjaEnndekBVS-ygWeu3-sO3A_hj5IU9GAYs42hC8hvXvUy_zDl5R18OIhzhtlUF80uYhBbXsn78TDv6zhtjxXOrZP7Mj8-G1O7ytSy9mFA52-XUutOv9Rz0wcREacUnXQN1GUb5qLJQ1LI4LymJPqS2mcJQlsxZMFVbHDqXWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/622db6728d.mp4?token=ZjORRs2iPt0ZAoPgIiZ5a8uvtuKwgi5IWOLAnl4xNt-I1HM6A9h69Rq8DpZyC8ZTIKMncKOm3UHttXKvp4kTpp8MLlTBFrbaisAlUVyq8gYh5xRCn82UH5ERImKps5CjVZb_0JxQG5R78wGcGIj5vm6-1aW56J3AfPpr1tPcRkesLvjaEnndekBVS-ygWeu3-sO3A_hj5IU9GAYs42hC8hvXvUy_zDl5R18OIhzhtlUF80uYhBbXsn78TDv6zhtjxXOrZP7Mj8-G1O7ytSy9mFA52-XUutOv9Rz0wcREacUnXQN1GUb5qLJQ1LI4LymJPqS2mcJQlsxZMFVbHDqXWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بعد سه ماه هرشب توی خیابون موندن و پرچم تکون دادن ، بهت میگن اقلیتی تندرو و خون رهبرتم پایمال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66428" target="_blank">📅 15:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66425">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4faedc1ad.mp4?token=OWVKgw06detPoNgVDWUITYoKvdE4cmoFs3js75S4lSlBMuDZe5QHdLg84Lf80XMhsPRQiKqCG6qJOIZp3g2h3ES4fIrGLuWfaSE5t_WTaDnu8aa3FyPc0ZLPyXRP-IdJpnZL_w3BXDLl_AHhAo2ORAfd5BZnCWiouEbFB8PSnR5HcKIklXC1mFuODku4tj4PDfAwraKii_udKIQkA4Tr-9ph6hPbYy8uv6lNAwrPEN9_ARdnXHy5FMzdp-f5vdpZ4ueVRK8dhcCAPD-nke4MI1165y6vw8r1NPaWysbywvCQmegmg4DvTScMt63AJ467S4gC9VPcMebj-OBZ6Nr7sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4faedc1ad.mp4?token=OWVKgw06detPoNgVDWUITYoKvdE4cmoFs3js75S4lSlBMuDZe5QHdLg84Lf80XMhsPRQiKqCG6qJOIZp3g2h3ES4fIrGLuWfaSE5t_WTaDnu8aa3FyPc0ZLPyXRP-IdJpnZL_w3BXDLl_AHhAo2ORAfd5BZnCWiouEbFB8PSnR5HcKIklXC1mFuODku4tj4PDfAwraKii_udKIQkA4Tr-9ph6hPbYy8uv6lNAwrPEN9_ARdnXHy5FMzdp-f5vdpZ4ueVRK8dhcCAPD-nke4MI1165y6vw8r1NPaWysbywvCQmegmg4DvTScMt63AJ467S4gC9VPcMebj-OBZ6Nr7sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات سنگین اوکراین به مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66425" target="_blank">📅 14:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66424">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92b0722cb.mp4?token=Xn16RIuIajIYB5NH5qE7npTHlFeoeJYVoLmrwUkzx6V-q0uQFDCVd10jb9yXDNmGk0QXe2S1D2cspVYVNHFzfezCMidpsZM78Gs3fJq475zmdZ20G9skAm6GHuHzbMHhuZRB5MIHko1fL9vxtAU7w816s4vXhXQNRV2sOYda_GqRS-JbVuteTRch_R3qg28GVLMi5JxBwjbunPADE8xRRpd1OhP2PRtVp68ws53zD0zOWECkxticpjmS8wAW0uc4xR9VmY_n4vy142pcy7fml-hQyFN6F_l1XsqhO6D76W58V9lpKVVcUoj06WFtmU00ju_K1kjhsht9jr_EY8xLEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92b0722cb.mp4?token=Xn16RIuIajIYB5NH5qE7npTHlFeoeJYVoLmrwUkzx6V-q0uQFDCVd10jb9yXDNmGk0QXe2S1D2cspVYVNHFzfezCMidpsZM78Gs3fJq475zmdZ20G9skAm6GHuHzbMHhuZRB5MIHko1fL9vxtAU7w816s4vXhXQNRV2sOYda_GqRS-JbVuteTRch_R3qg28GVLMi5JxBwjbunPADE8xRRpd1OhP2PRtVp68ws53zD0zOWECkxticpjmS8wAW0uc4xR9VmY_n4vy142pcy7fml-hQyFN6F_l1XsqhO6D76W58V9lpKVVcUoj06WFtmU00ju_K1kjhsht9jr_EY8xLEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏جی دی ونس در مورد مسلح کردن معترضان ایرانی:
در واقع تا حدودی دشوار است. می‌دانید، نمی‌توانید همین‌طوری از آسمان سلاح پرتاب کنید. واقعاً زیرساخت لازم برای رساندن سلاح به قلب مردم ایران وجود ندارد.
یکی از چیزهایی که رئیس جمهور خیلی نگرانش بود، همه این معترضان بی‌گناهی بودند که توسط افرادی که چند ماه پیش مسئول بودند، قتل عام می‌شدند.
آن افراد اکنون رفته‌اند. اما خواهیم دید: آیا این رهبران جدید با مردم متفاوت رفتار می‌کنند؟ مطمئناً امیدواریم که اینطور باشد.
و اگر اینطور نباشد، می‌توانیم وقتی رفتار واقعی آنها را ببینیم، بفهمیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66424" target="_blank">📅 14:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66423">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GT_ccbKwRwpxUJ7lakSjw_lo1c313CUTiw9OnNIh8mZ2GVSJfv4B89QZYwwHUhT5bWgiFnijMlj_CzFYSLwvAfJ783eToh76RJr6bgqcTVDO4_b7SntfZLo7w6mCNPBsYxVA9aEAnUu8Xr-olfLBJ4NVMedjd_VwxRcWCgnatMY9_iJGVcSIqiWLdfJbBU60W_lWCjGWxCyqdVoDnnxAc_YYWtx7WAfFulDa24ZhP6UUIvXHGK15qRcVR0b5hLuDOxkcA35qBkhtZtg8NfF-h8XJj7Hi0Fl7VRN_DYHDWMfY53InFqWLjKKtybX0oNGc6CNApsQmFj5akOBAnL9EFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حملات اسرائیل به جنوب لبنان همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66423" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66422">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66422" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66422" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
