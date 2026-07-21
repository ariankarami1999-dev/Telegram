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
<img src="https://cdn4.telesco.pe/file/Pn8m4jQS6My3h9qHmJdPGuKEtn33QUv6mPHvJw2mIKjQu1blN-Oo2a2tc3j-mvomdsHFk2aOObrOjHV0ku_qtpRXjiaMHlobajTOKLRfMZACvdqHyikBNcYelQisaRnT07YP43Ys6rMfbUoC8xMu6gNVGhyPX07o3uFUoCzrgOgIQwqvdkCudQBXOBh_Ay-rYEtCqSqJPD3Uo9KuX9TIsrZFLn2yIbK80yGIyqweaCm5Gxwsp-Dj9tQjhVkYFmAdujukDXI6M-gpi5OzmQ2aNhPC9LukYVatM9tjIm0D8kbLGZZl54suE5JlXUfAaCP-4MEVYJnT6cD1ads66cdPHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 155K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 02:21:03</div>
<hr>

<div class="tg-post" id="msg-68758">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در نارمک!!
@News_Hut</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/news_hut/68758" target="_blank">📅 02:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68757">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/news_hut/68757" target="_blank">📅 01:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68756">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/news_hut/68756" target="_blank">📅 01:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68755">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/news_hut/68755" target="_blank">📅 01:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68754">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
جمهوری اسلامی به کویت حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/news_hut/68754" target="_blank">📅 01:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68753">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/68753" target="_blank">📅 01:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68752">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/68752" target="_blank">📅 00:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68751">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W86soodYcI72m1LWG-loExGtGUpM32ganjkTHOj7IvQ7v0HcWWCoHSGtUg1eZLfcgPrZ19V9Zoy3MdSve5z3D2_NNwXdOsflFNvulUPH5bqLWqENW9yNqYYM5VxPWZQeutwr8aA0_amYpBDzUma_i7ziv1jnrt4GoxJG2Jsz8UlVeqB3Gh6tP1Sa7bL61c7On4ihVHq0NRK_lDm9hEB3ayPSQ1lqJcjF-cbyDCpBhC6uzn75r9js21D2red8dWsOXnuW1bMdr8SRcS3EGzNubSzcHN6zr91mLGLY1t1QH4lv_NMf1Md9D1um_p6Zl2A0Ep-Bqpkk-mBLuAcr3KV8jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قرارگاه مرکزی خاتم‌الانبیا:
آمریکای جنایتکار مراکز هسته‌ای و تأسیسات حساس ایران رو تهدید کرده که ممکنه بهشون حمله کنه.
اعلام می‌کنیم اگه ارتش متجاوز و تروریست آمریکا چنین اقدامی انجام بده، این کار رو به‌عنوان گسترش جنگ در منطقه تلقی می‌کنیم و همه منافع آمریکا، همچنین منافع متحدها و حامیان این کشور یاغی و شرور، هدف حملات قدرتمند نیروهای مسلح جمهوری اسلامی ایران قرار می‌گیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/68751" target="_blank">📅 00:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68750">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e35b34fa8d.mp4?token=OMg4z5dQZOu6Xt-pDUPxEJOdIc6FHKQ-Fq3t9reQKGTS-zB1OK_0hlr3dQlSCwfH713Cv0kZDSR1Xw__h2HTaJUExycj3gKzGRjifcRWLdrxWnhN1nglu3E1VxdD1KoC7L_dvCqZ50KB7zXhD8APvQUuq-veOyq0_WAlkCwqoWH16mOlsfVNHMccwj32vwsXR2fGjB89xkgPDJw3_yKUuf42gpAHjXaL7OX3aMgPF3hyKMv8Oz7x1bVVW804TS_h0an7JhsvgcV5ctSqM5IwMWnWCykAtpuqduB8KpARqZ4QWy6itSNhJM0iTXAZ5VUj5ZeqMaV_H6f40t1GdJlXDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e35b34fa8d.mp4?token=OMg4z5dQZOu6Xt-pDUPxEJOdIc6FHKQ-Fq3t9reQKGTS-zB1OK_0hlr3dQlSCwfH713Cv0kZDSR1Xw__h2HTaJUExycj3gKzGRjifcRWLdrxWnhN1nglu3E1VxdD1KoC7L_dvCqZ50KB7zXhD8APvQUuq-veOyq0_WAlkCwqoWH16mOlsfVNHMccwj32vwsXR2fGjB89xkgPDJw3_yKUuf42gpAHjXaL7OX3aMgPF3hyKMv8Oz7x1bVVW804TS_h0an7JhsvgcV5ctSqM5IwMWnWCykAtpuqduB8KpARqZ4QWy6itSNhJM0iTXAZ5VUj5ZeqMaV_H6f40t1GdJlXDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/68750" target="_blank">📅 00:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68749">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/68749" target="_blank">📅 00:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68748">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f962f6335.mp4?token=K-aZbR-aQ74zMYxXV_-q37zjnLHiDWsbNNL5lif56PHACMw9kb9S3EDR4uaUT5qNPBGIIUgAQ1xGYlegPcU2W2IeuoViSO2SYlst6Wf-y20V4Hiqqi5_lDyfwAE5XLaslROSboZRO3DQB6iqG765J5OA0AcRrKpySjuyRFiEAhGqGm2noSoftENfMNs2eFd3_JeQt2i9vO_cGy-qlm9AT3iDYF-XY16YV4VRqfLc9GG6YwEr0Na9ulKNwey7wLAXt0aeiZqp6Q0Lig8owWgqU14QwDud-zFhqE7sSQwt6goV9ynpZVGPJmgnH6-AkTmHuDOFIkNcCvqX7-zrPJ4BoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f962f6335.mp4?token=K-aZbR-aQ74zMYxXV_-q37zjnLHiDWsbNNL5lif56PHACMw9kb9S3EDR4uaUT5qNPBGIIUgAQ1xGYlegPcU2W2IeuoViSO2SYlst6Wf-y20V4Hiqqi5_lDyfwAE5XLaslROSboZRO3DQB6iqG765J5OA0AcRrKpySjuyRFiEAhGqGm2noSoftENfMNs2eFd3_JeQt2i9vO_cGy-qlm9AT3iDYF-XY16YV4VRqfLc9GG6YwEr0Na9ulKNwey7wLAXt0aeiZqp6Q0Lig8owWgqU14QwDud-zFhqE7sSQwt6goV9ynpZVGPJmgnH6-AkTmHuDOFIkNcCvqX7-zrPJ4BoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست:
من در مقابل یک کمیته نشسته‌ام که می‌خواهد درباره پیروزی در جنگی صحبت کند که چهار سال است ادامه دارد، و درباره شکست استراتژیک درگیری‌ای صحبت می‌کند که چهار ماه است ادامه دارد، تا از دستیابی ایران به بمب هسته‌ای جلوگیری شود.
امیدوارم که در این شهر، دیدگاهی وجود داشته باشد نسبت به اهمیت تاریخی اقداماتی که رئیس‌جمهور ترامپ در حال انجام آن‌ها است.
آیا شما می‌خواهید که گروه‌های افراطی اسلامی به بمب هسته‌ای دست پیدا کنند...؟"
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/68748" target="_blank">📅 00:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68747">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/68747" target="_blank">📅 00:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68746">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f9adfe1f.mp4?token=nAp_-TdFKaAm0orm7ozjgGO-UmkDojDw_6HwnIANPrBpOf2MdZBAt7tUYVRtaVTN8ar2-Hs93hd1auEhkzo5GY5sYfx_D4OzG0HXG3N9xN_KJ03DTGlHQzFgIXu_ie5j04wMY1J_vx8Yt4R9kqZw9bB1Ve71_OZP0-06ygZMueyM6A3o59ZdkQqdRUlqVO_SFZmdUmXtkBX0Kzf2TFMusOlBI5hokRhB7f9q6s9te8ysYnNxABw1AyjGa3mngoVUiAVr_rMDQoWvRhCCvVIvICjf_5_AfCmfAQ7J2mbrdRKXEkN_IVw_9UHffAJU-pQ0eel4xAYYqUr84s5RkA2nzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f9adfe1f.mp4?token=nAp_-TdFKaAm0orm7ozjgGO-UmkDojDw_6HwnIANPrBpOf2MdZBAt7tUYVRtaVTN8ar2-Hs93hd1auEhkzo5GY5sYfx_D4OzG0HXG3N9xN_KJ03DTGlHQzFgIXu_ie5j04wMY1J_vx8Yt4R9kqZw9bB1Ve71_OZP0-06ygZMueyM6A3o59ZdkQqdRUlqVO_SFZmdUmXtkBX0Kzf2TFMusOlBI5hokRhB7f9q6s9te8ysYnNxABw1AyjGa3mngoVUiAVr_rMDQoWvRhCCvVIvICjf_5_AfCmfAQ7J2mbrdRKXEkN_IVw_9UHffAJU-pQ0eel4xAYYqUr84s5RkA2nzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت
هگست:
این درخواست تکمیلی دو هدف را دنبال می‌کند: حفظ آمادگی نظامی ما برای پاسخگویی به نیازهای جدید امسال؛ و تسریع قابلیت‌های حیاتی برای جایگزینی و تقویت قابلیت‌هایی که در شرایط اضطراری استفاده کرده‌ایم...
در حوزه آمادگی، ما ۲۱ میلیارد دلار درخواست کردیم. این مبلغ برای تأمین حقوق نظامیان، جایگزینی تجهیزات مورد استفاده در عملیات‌های اخیر، حفظ نیروهای مستقر در خط مقدم و افزایش قدرت نهایی پرسنل در عین تثبیت کمبود سوخت حیاتی ماموریت و پشتیبانی از گارد ملی هزینه خواهد شد.
در حوزه قابلیت‌ها، ما ۴۶ میلیارد دلار درخواست کردیم. این بودجه خطوط تولید را گسترش داده و تحویل مهمات مورد نیاز را تسریع می‌کند. ما در مورد موتورهای موشک سوخت جامد، JADM، موشک‌های مافوق صوت و قابلیت‌های ضد پهپاد صحبت می‌کنیم. علاوه بر این، ما از این سرمایه‌گذاری برای تضمین تسلط دیجیتال و فضایی، از جمله شبکه‌های ماهواره‌ای انعطاف‌پذیر، استفاده خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/68746" target="_blank">📅 00:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68745">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/68745" target="_blank">📅 00:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68744">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVfxZn7nMI13gY2NnOMQOELkusOnEWHjjyCIBkvaBnpfblVh-wIrIe5sSS72l-8ek90ilZpORgMmaIXXwsP3hM3O7TgEQcWTQB4kCIM6PNwgjvQwQ-wieVer-GHo85ZJJT7R7IRrgcsdVWvKMM-vb-H44J5aufKOdypri9z8ba7bB1L-pGKlrAcASORTuaYU7sYafLsdACXbFAzyVDdQZpB0Eq6aCAUoyYq0Hf_piCGZ6k0dCwNQbsnwB2jvmTJHqUsZ3wMM05_UQAt7AgXGNvRzQsfgRhTNprWqN6UGsX5y42PFDcC5KkLTGF_wwupnUnxagBjom5fPvremLmDp-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
چند سوخت‌رسان از فرودگاه بن‌گوریون اسرائیل بلند شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/68744" target="_blank">📅 23:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68743">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تاسیسات جدید هسته‌ای ج.ا: ۲۰۰ متر زیر کوه کلنگ
پرنفوذ ترین بمب غیرهسته‌ای آمریکا: GBU-57 با ۶۰ متر نفوذ
#hjAly‌</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/68743" target="_blank">📅 23:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68742">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/68742" target="_blank">📅 23:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68741">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab2e49c2e.mp4?token=l9xjaHpPPVTrluKEd7uNMZhl47m572h-vn7sRSfwEtHRns2CGVbyScEw9SGvV0sY57_seK3ubwshfsBVhKnS1NbLnTV2fkcP6fPBgRctaxthVZH_L4P-icOYjU-8k2yGcwKFFhxHIhXnCW1F5D2__AcYxezC-Gvi4eGeyley3IGpRGKa--UjWbfi8g44SEIwe1JERVTcpMKhjfzT6NqU5K6s7PFYcMlh41qYevEbr0XROorMjs2oPIZH20Ao6ON1a3S7MIw3e8f_WOGZ099cKD7u0Nu9HCsEnSr2FdXB0M4wbOGiCNsITWXuX46xbczSez7JJP0x4r0r7tvcAhPhbBow71zz_h2t0FTOCuSpzeB3-D9fUrAJxZ_1BJ3O7uv3viKNg1VzW_kl758Ye2b_wqqZi6bK3b4Ekd6vd3WWTDSaD1jUi2eUloc4l0XJ6sdkQ5hEYy0ZH7Fr_Lco3p2UtTXNqs3x1whj8QyzKngXiefH1oSeoO2-KIb_AUQBZbakXuHsIxKIP1ZjsWNVRCvMmAD1hHsL9bpLvPll2UqSWPn7y8BGwYtY6bS27p8G2ujyWhTjCAFvmJD9hwNhoHe7AU7zoOMzCncj2f620BREBXhbSgeODXeUJqy_HWq_JBsxzP5mob8cpnfU_P0gT-S5nJVNFcnvdOLS-XYrOb3PQ9s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab2e49c2e.mp4?token=l9xjaHpPPVTrluKEd7uNMZhl47m572h-vn7sRSfwEtHRns2CGVbyScEw9SGvV0sY57_seK3ubwshfsBVhKnS1NbLnTV2fkcP6fPBgRctaxthVZH_L4P-icOYjU-8k2yGcwKFFhxHIhXnCW1F5D2__AcYxezC-Gvi4eGeyley3IGpRGKa--UjWbfi8g44SEIwe1JERVTcpMKhjfzT6NqU5K6s7PFYcMlh41qYevEbr0XROorMjs2oPIZH20Ao6ON1a3S7MIw3e8f_WOGZ099cKD7u0Nu9HCsEnSr2FdXB0M4wbOGiCNsITWXuX46xbczSez7JJP0x4r0r7tvcAhPhbBow71zz_h2t0FTOCuSpzeB3-D9fUrAJxZ_1BJ3O7uv3viKNg1VzW_kl758Ye2b_wqqZi6bK3b4Ekd6vd3WWTDSaD1jUi2eUloc4l0XJ6sdkQ5hEYy0ZH7Fr_Lco3p2UtTXNqs3x1whj8QyzKngXiefH1oSeoO2-KIb_AUQBZbakXuHsIxKIP1ZjsWNVRCvMmAD1hHsL9bpLvPll2UqSWPn7y8BGwYtY6bS27p8G2ujyWhTjCAFvmJD9hwNhoHe7AU7zoOMzCncj2f620BREBXhbSgeODXeUJqy_HWq_JBsxzP5mob8cpnfU_P0gT-S5nJVNFcnvdOLS-XYrOb3PQ9s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
هرگونه موفقیت عملیاتی در خاورمیانه، از جمله در زمینه محاصره ایران توسط ایالات متحده، با عملکرد نیروهای نظامی متمرکز بر مأموریت‌هایشان آغاز و تکمیل می‌شود. تا تاریخ ۲۱ ژوئیه، نیروهای آمریکایی برای اجرای کامل این محاصره، مسیر ۸ کشتی تجاری را تغییر داده و یک کشتی را از کار انداخته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/68741" target="_blank">📅 23:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68740">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68740" target="_blank">📅 23:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68739">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🇮🇱
کانال 14 اسرائیل:
سپاه سفارت اسرائیل رو تو بحرین زده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68739" target="_blank">📅 22:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68738">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d3140239a.mp4?token=Xvqu1BBHwilx-W0mMSxxfrKtQQR8k7uvz9W9o_KL-kzh2iEWrGyrkfQujT_E0tCX7iSfdLi73dWJHz4DWjmcDFzlraS3IqvAv5HDy28nCKBIq3hLu2WkTg7B1IoBq2VyY7SUGg8r5XmO3U4eLLiVV_Pic5AsAMbW2w_CANkF8Ba5tl7fOXzAdPaOprHsmjnUNE89XhsXN8RUYGk_e01CtW6YSlhXBNhKRaqUxtBWd7hqZ9oulF7BzEgOR_cTepy83nxKZREqiO9CjszJKFV46N-8MNe7QrOFNbHQXptN-M2LahJtn4Z-87ifrLG5kG71Cw8DEWN7tv_7ud1sHLUXfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d3140239a.mp4?token=Xvqu1BBHwilx-W0mMSxxfrKtQQR8k7uvz9W9o_KL-kzh2iEWrGyrkfQujT_E0tCX7iSfdLi73dWJHz4DWjmcDFzlraS3IqvAv5HDy28nCKBIq3hLu2WkTg7B1IoBq2VyY7SUGg8r5XmO3U4eLLiVV_Pic5AsAMbW2w_CANkF8Ba5tl7fOXzAdPaOprHsmjnUNE89XhsXN8RUYGk_e01CtW6YSlhXBNhKRaqUxtBWd7hqZ9oulF7BzEgOR_cTepy83nxKZREqiO9CjszJKFV46N-8MNe7QrOFNbHQXptN-M2LahJtn4Z-87ifrLG5kG71Cw8DEWN7tv_7ud1sHLUXfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
انهدام پهپاد جمهوری اسلامی توسط سامانه آمریکایی برفراز اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68738" target="_blank">📅 22:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68737">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cacafc700.mp4?token=oUOVXw2KXn_yUzggNZYUM-CA8CITGoVSC7V5cQGcApCjPWz9vYwoDGnY4eK79m4obIp-PVC7r2j2qYK13oVpFQUC5NNwhgGdTAFO-GY7vIyiW2LjBZKjieoZhPMMOxGDAatlt4l85XHpKtrpAlBh9b7LNVuHx4Zxx_RdZA7kSuQbj0lhWwNsPC7oQwP3JJIatPco422AW3zY0F2lzwE4tkBjpS1HWV-GcaL3IWd7qwj9FUp8K3ShigF7vy0BSyLy0VKW7Nkt2X3sr5ihEAU9rgZG8NvpTe9wQaM3Dv4r2LVXlNUXgDYX6fne_1mQE-26OKrbFpWxqxrslMGNMsB6Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cacafc700.mp4?token=oUOVXw2KXn_yUzggNZYUM-CA8CITGoVSC7V5cQGcApCjPWz9vYwoDGnY4eK79m4obIp-PVC7r2j2qYK13oVpFQUC5NNwhgGdTAFO-GY7vIyiW2LjBZKjieoZhPMMOxGDAatlt4l85XHpKtrpAlBh9b7LNVuHx4Zxx_RdZA7kSuQbj0lhWwNsPC7oQwP3JJIatPco422AW3zY0F2lzwE4tkBjpS1HWV-GcaL3IWd7qwj9FUp8K3ShigF7vy0BSyLy0VKW7Nkt2X3sr5ihEAU9rgZG8NvpTe9wQaM3Dv4r2LVXlNUXgDYX6fne_1mQE-26OKrbFpWxqxrslMGNMsB6Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانش آموزی که ۱۹/۷۵ گرفته دانش آموزی که ۰/۷۵ گرفته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68737" target="_blank">📅 22:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68736">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbTohZW8wjm2EtGsK0flKrBe-WwZgSuqttwSNHzjK8iFqTcxtnOYJYct-Z7ZmaSCI11Q7JcQXIE8b1Q6EBJyRknqDAvfAPIOgh9EBfTZ5F83FkDitKDVPCk7wO7qblziZT4i51j9oyfT30BCMOUvb83ogob9D4RvAiRpfFJ2CVE-1zY1uniuNJW9UuWiC-tKJbosNwkXCH9B2MEaHc5MlGxHqu8AcXNdFpcF4EPnBDm6oKqI-kVq-CoemDrRSRqbnAwyU98mkj7rruhjeCYuji-XKi8FTYgvCLrJNePnJI4-BWEeUxyV4mQVSAeBT-HI-KftOirAUUHcLdfY-p-8lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به گفته بعضی از کاربران شیرازی، این اولین بار نیست که چنین اتفاقی می‌افته. ظاهراً چند بار هم دیده شده یه نفر میاد اینجا آتیش روشن می‌کنه و بعد میره؛ اما هنوز معلوم نیست هدفش از این کار چیه...
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68736" target="_blank">📅 21:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68734">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lk2NXXCdLEEQCxkWqy3RMY2orepOBskemT1xWvGoO8StHTNNppONe18A8by2hcM9QQvl-oUEC1jwbcs3XPgQOM5a0lDxIeg0BmzlrOK_8d7IKz6t2yHfZUdMAsBegQCTd5yDu2lqzR0DbjS8vGAlHyYciMetELzTX9Nx8TP1TlFUHz_h4LFFU2nnlDnWU-99vENVkPpLTXKj0t9jNQBudA5vaH1gNDV5V6xk1qOsFaddKPetD7uWWQVIbFMTiYUxoR8dE1nPyR3d74iCbyG6y9nv6y55wDa47dOaEO_xJQyHwxCCQx2R8U_YhlgCyHnCLP0Wz516295FO0Xd1sDyaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cq_OqoopYPj8H8xYW6nqRttfG73Wr2W7oM758EkYYu_fFDhSdg3WoVtbX3JZdeyZMZZJY2jpojCroNY_QJzGiX7aFIoPhWEBEIAWvr0GAAja_sxIwIaHnNC75W30nDZY2M8_mWLrXXU5-x34XaD_mlnp9-Im8iOCrAJKotgyGrihgLkmnUTFeO_AUo0_L08Vq2vQXOJKlLD0bKdIj7Ii7-oNu2qXBMQBTOPeiDZfAsiPO-5jZbLMXxi8dt7MLNGZnoTxlHwgc2u1v7OPcqe2UGB6-DPLEdDskWJjZnegB2NytdVYxGvCKScRiK6KHAEzK6mEYCVr2hSmsMa3qfLaoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کوه دراک شیراز در حال آتش‌سوزی به دلایل نامعلوم
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68734" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68733">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AD9yVaPI6UnIBgEgc1CH4WTut6R9vJdMCs-HCFhlr26b9oNATC4acEdLsNKNbfd4tiyjLOAOOy1s6XGQa0cv5Pl_BSvDuCYGflZm2vu8PNMTMoxOZMAOPL9U1kFnXKnposf3dh_hGtNYX-Tr3xw02ENjzgqyM5jLxypPwaKzjoZOKe-cCFv1DD9TljWemOlQUfyLYz4v6XtN2nW8kIQ8gDO9ey69I0OZ4QocMIqua6-P-ehLvNa2OZkDLdBEcaV2wOYlq8T1t8DnjIQUDk3Ae-LmPSDUGMMKfoqMI_JKN2nS1698Da4UhC1L4ZMw56zaaJqVFPjSZoTLzy6Cr9-dyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
گزارش های تایید نشده از آتش‌سوزی در کوه دراک شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68733" target="_blank">📅 20:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68732">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68732" target="_blank">📅 20:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68731">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdd4a3d5a.mp4?token=eIDw-rQ7aytgqUCUNj-HTt0e1stvdsgAC_p8SyDXT7Xnr_1drnv37HNizmFVz50nUBZaifW2yuk0m3cELHxJhmCwCSDNV0kOrawCEuq42TsZ5XBo2JxBV2-_Pdsu1Wdgs91325UQrnFBqxJNznvDw_oLTVLEyvE-kMm0LI42zHNEE9BNLdHO3hbsmDmy-q7cCsnKbV5fXKyUkLajvIS8zq-hSqeXyS1n7yvSMrGz1z-pj1GIfMzON4pTTx_gRVhTLhnZHe2APbCb1Tr5d3M0NGA7wreD4CTTlkMzS_FHHcuLpC-gTVENidLjAfIvwRrJJK4wNOGN9epmDqCyHYCnmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdd4a3d5a.mp4?token=eIDw-rQ7aytgqUCUNj-HTt0e1stvdsgAC_p8SyDXT7Xnr_1drnv37HNizmFVz50nUBZaifW2yuk0m3cELHxJhmCwCSDNV0kOrawCEuq42TsZ5XBo2JxBV2-_Pdsu1Wdgs91325UQrnFBqxJNznvDw_oLTVLEyvE-kMm0LI42zHNEE9BNLdHO3hbsmDmy-q7cCsnKbV5fXKyUkLajvIS8zq-hSqeXyS1n7yvSMrGz1z-pj1GIfMzON4pTTx_gRVhTLhnZHe2APbCb1Tr5d3M0NGA7wreD4CTTlkMzS_FHHcuLpC-gTVENidLjAfIvwRrJJK4wNOGN9epmDqCyHYCnmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست، وزیر جنگ:
به ایران فرصت‌های فراوانی داده شده است تا مذاکره کند و نشان دهد که در قبال تنگه هرمز رفتاری معقول دارد. اما اگر آن‌ها بخواهند به کشتی‌های تجاری شلیک کنند، آن‌گاه ما — همان‌طور که رئیس‌جمهور گفته است — ضربه‌ای ده برابر سنگین‌تر به آن‌ها وارد خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68731" target="_blank">📅 19:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68730">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46342c6e91.mp4?token=sjn9Fo86j0uJkgmJf93kCK5lps1mHkyh6OFWAqA5C2gNOglM3v1Rafasxg2kkRd_jpbIGYV6wJnBLx4bQ8TGRFHwqKCEJZpebiwl1r1xP2edroBl1AEQHPGuvhvr0fiu9uK0ROE_vdh0OUbOIYyeNOGjXmX5uSHMSR_P0WMC4NJibRlGrZey8-iyv3HsOEjTcCbdBZrBBlvPVolITg2uRsoAJpxaTnk8-kFBYSusRLAaLQeIQ2OtwV2v1btQkJeeCZyZ7kyoQAcXHglt-Qa4FDG_J1wOQDBBLoNE3F-ntjX7LIh1Lsqh0iTYqlskDDYmWf32drWKuKS3F1TvCqligg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46342c6e91.mp4?token=sjn9Fo86j0uJkgmJf93kCK5lps1mHkyh6OFWAqA5C2gNOglM3v1Rafasxg2kkRd_jpbIGYV6wJnBLx4bQ8TGRFHwqKCEJZpebiwl1r1xP2edroBl1AEQHPGuvhvr0fiu9uK0ROE_vdh0OUbOIYyeNOGjXmX5uSHMSR_P0WMC4NJibRlGrZey8-iyv3HsOEjTcCbdBZrBBlvPVolITg2uRsoAJpxaTnk8-kFBYSusRLAaLQeIQ2OtwV2v1btQkJeeCZyZ7kyoQAcXHglt-Qa4FDG_J1wOQDBBLoNE3F-ntjX7LIh1Lsqh0iTYqlskDDYmWf32drWKuKS3F1TvCqligg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره حمله سپاه که باعث کشته شدن دوتا امریکایی شد:
«داریم توانشون رو در حدی از بین می‌بریم که هیچ‌کس فکرش رو هم نمی‌کرد ممکن باشه. واقعاً ضربات سنگینی خوردن.
البته تونستن یک مورد رو از اردن رد کنن و اگر افراد دیگه‌ای مسئول عملیات بودن، چنین اتفاقی نمی‌افتاد؛ چون ما بهترین تجهیزات دنیا رو داریم.
ما تقریباً جلوی همه‌چیز رو گرفتیم. اما وقتی کار آمریکا رو می‌سپری به آدم‌های دیگه، بعضی وقت‌ها اون‌طور که باید پیش نمیره.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68730" target="_blank">📅 19:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68729">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68729" target="_blank">📅 19:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68728">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0f808d08.mp4?token=S6evfcmpEC0iIZy3jQ-L9G4laH_emPnht4rdDP4rDc8x6t4UOBETHXuvVOzPhRux_qHbY001hCgT6XqUBKOEMrs-K8KWX3ngZbFDZcAwBNNvQ46aIV1QA9KC2CxHmK4faVXtuah4llUBUl5BYP9Gtrwfoy37rklG01OEQTRSAhEA8maqIV5L16NVjfG-IM-XNq2MmAhfOkLZVr_mB4XyXgHG07EP-hfa8TxgO_ftkM_mEQsfTWRfLB7Wk6meDzNg_ypVsDvevgsmdT_EQOhk_YkV2Ai47pO4o1KkP7i5r3IpvSyLhw6iuG-oWFYKot3jLPbJTbJMNVAyEb77K-5RgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0f808d08.mp4?token=S6evfcmpEC0iIZy3jQ-L9G4laH_emPnht4rdDP4rDc8x6t4UOBETHXuvVOzPhRux_qHbY001hCgT6XqUBKOEMrs-K8KWX3ngZbFDZcAwBNNvQ46aIV1QA9KC2CxHmK4faVXtuah4llUBUl5BYP9Gtrwfoy37rklG01OEQTRSAhEA8maqIV5L16NVjfG-IM-XNq2MmAhfOkLZVr_mB4XyXgHG07EP-hfa8TxgO_ftkM_mEQsfTWRfLB7Wk6meDzNg_ypVsDvevgsmdT_EQOhk_YkV2Ai47pO4o1KkP7i5r3IpvSyLhw6iuG-oWFYKot3jLPbJTbJMNVAyEb77K-5RgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68728" target="_blank">📅 19:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68727">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18745bb1ea.mp4?token=l79q-NOcP-3EpeIn7KCYSE1ecPFBNSLhZLZ7Y0ygG1TtpVlOcR87GUejzN_RmvwPjU0Xxvk2hue2a_8xovEpujx1BHZ4lzcrmN7yFPS8p7II0-5rdZ-IK6g3oZcBVV2lY6yGRwTO04fq4IBXuGjdHboRgQOeDQQaT7qDZrQPg7rD5e75b347s2mJgAuMa_YvzTyEfGJJbcOoQ6zfZnxmy0_nonEy0N4SoVjKoSq9yrbvGXkcj8m7V7zYlJCe94FAICfVHu52FIlK_O9hKI5TolE9EfoW8BsThtqdH3oL_jwpUCDApjp8b7zzFcoy6H_oI6Gz9DcgYI5lbku9D2I24xY1cpDbYAogX6Pgw4VsMCo3Ju0IcIHSstJ2WTUC3UCvBlHl7JvGby_82E1RaxooDYHPpD0IR9m33l-_fIZqxTupYFlxHNWvsBqW1ODfxMOTNd_xfL-DthvkwD-9fdMdK2kOBwtyu0uHh0_O5-TykYQqGfKM19xaYhavOUs_-_ldF2fS8RyleUGDKaL6mVi6ITkxk7sq4K6qOFV_l4PTaYEWP50xFiefFropek5ZumHbdewrvXvMuTRfGYriBKTeN-4N9vqfemufvREueVSbRvQROoTAJFiBcTIFr8mDyWEWHNjMAuX-6GdfM2OeSEKRDWaTLrv9k-SxFytmzbjXrW0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18745bb1ea.mp4?token=l79q-NOcP-3EpeIn7KCYSE1ecPFBNSLhZLZ7Y0ygG1TtpVlOcR87GUejzN_RmvwPjU0Xxvk2hue2a_8xovEpujx1BHZ4lzcrmN7yFPS8p7II0-5rdZ-IK6g3oZcBVV2lY6yGRwTO04fq4IBXuGjdHboRgQOeDQQaT7qDZrQPg7rD5e75b347s2mJgAuMa_YvzTyEfGJJbcOoQ6zfZnxmy0_nonEy0N4SoVjKoSq9yrbvGXkcj8m7V7zYlJCe94FAICfVHu52FIlK_O9hKI5TolE9EfoW8BsThtqdH3oL_jwpUCDApjp8b7zzFcoy6H_oI6Gz9DcgYI5lbku9D2I24xY1cpDbYAogX6Pgw4VsMCo3Ju0IcIHSstJ2WTUC3UCvBlHl7JvGby_82E1RaxooDYHPpD0IR9m33l-_fIZqxTupYFlxHNWvsBqW1ODfxMOTNd_xfL-DthvkwD-9fdMdK2kOBwtyu0uHh0_O5-TykYQqGfKM19xaYhavOUs_-_ldF2fS8RyleUGDKaL6mVi6ITkxk7sq4K6qOFV_l4PTaYEWP50xFiefFropek5ZumHbdewrvXvMuTRfGYriBKTeN-4N9vqfemufvREueVSbRvQROoTAJFiBcTIFr8mDyWEWHNjMAuX-6GdfM2OeSEKRDWaTLrv9k-SxFytmzbjXrW0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/68727" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68726">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/68726" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68725">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/68725" target="_blank">📅 19:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68724">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/68724" target="_blank">📅 19:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68723">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68723" target="_blank">📅 18:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68722">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhIgjPCOgOFXzyjqOn5j1g6T3CNbmz0iv_DiJ2UpBpp1BL-H4J-eV1SfjHOTx0WZyhPdiWAGxtIcyRJFiErdPXCJEhkha43sGX6nlTjpyP8saRbQc7cL5-ZDF5A0aH9C1TeWSAnK51E93UbM5F57a8nW8fder6C4g7f3XNakKRbOPE2BCak_-RU4qiv00R48LdLt-O9AMzX-zZvkXpFmteoqjQ0Mh4_zAiu4IWAC2p09x_0yS0SRSCEO9ANV1emRyp3MTSU-XmTZlT4pEWS8PAb3a05iU8DWZX1qm9Nd59TirhT3ljdMIqkJJQJnvPtuduEmtV4qauFA__yuLLTAAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پست جدید ترامپ در تروث:  این آخرین نفر از بین بیش از 52 هزار معترض بی‌گناهه. وحشی‌ان!!! دموکرات‌ها کی می‌خوان بالاخره بیدار بشن؟؟؟ این گل‌محمد محمدی، 23 ساله هس. امروز صبح توسط حکومت جمهوری اسلامی اعدام شد. تنها. بی‌گناه.  @News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68722" target="_blank">📅 17:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68720">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/oonY74fb4v37uZ8aJCkkcOvV6yWKBw3FLakOhd8cFRZWPqC9qW-Jw3_pgEcWoEFkNnGXQkZ-Mn8CWqQ6vY-fpB2mMBQhzb_smIZug-TyhY7QPGnNTi4_Vis8xC8xJbSuO9HsY6dpcRWWrcO5_gve13rITZYcoaLOyceywX6laI8iVKPMX6UnqyTXGUlFxeSPcnqGA3ChfutpQPxiepGdek2KRGVagUGAnLzZCAtpPMjJIc_1-JVCVjFYybyam0YZsx1D8J3xEFp9fzDoUydsJoidxGWJoq6QrtzCiWqUiRM51LY_Qx04cpMS6EanF_Vc6KyOWfXmaWolAmEh83UalQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/gi16A7KTyD0zlSuACMJfO-So02L9OXi22SpprLK5SW6XPnJOEfaq8UKnVuyE7zoYxuSjJkTxOi2PnRLPD59TIttL03NTucHS3mAijXx76hJLa2nYGCwl6apRsT-b3RXqv17GpqhHH9heGNHMyQRGhH9NeNRaXFvyO5ha3OpsMRYMOSfYKwDk8Xe6-3h6bYFSsA5ax3_eSGTM7PAXCJOgH7KDvmC2QdzbpSieMPJVT86HunKo5aj6mtVaH_AHBWGXrRWm6ppP96dyvQqg_Xu9-d7ra4bGLXCRIZ4mcn6jqIZhSqsPHDvy6i4nc-br6TiKQj1U2yr6P2juy2c1sfzBpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68720" target="_blank">📅 17:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68719">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c7e1427c7.mp4?token=kaHCV7HUBGC0d2T100ll_koUNCEkQZt_IebyzDbcBVfdKlNCECC-oq6Hs-oQu6698-0oFxiPsDXmNQ6-KgNe3CLcFWioKLTTjCSLJnQCpuZvMc-r0Mycicvdc_opV3WCvR1B1f3PorEJpgbDdqlA9P1xvdNXuytHNVzxK6iTqPa48Z-fhPo537T4R1yZOzzFTFs3i9NcTdJyt3JQcVnsu3w1gmjf2kKkn-HS6QfZ1ljHIeyxCykD8abZLOovykh_TSjEdQ5K1U_-scLFmFHBxUN-LVxVooVi7gpqCZ4NBYoGWfi0H-4NF5GXnA2N2OnYekBIdXtfarFGb-ic0QxGEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c7e1427c7.mp4?token=kaHCV7HUBGC0d2T100ll_koUNCEkQZt_IebyzDbcBVfdKlNCECC-oq6Hs-oQu6698-0oFxiPsDXmNQ6-KgNe3CLcFWioKLTTjCSLJnQCpuZvMc-r0Mycicvdc_opV3WCvR1B1f3PorEJpgbDdqlA9P1xvdNXuytHNVzxK6iTqPa48Z-fhPo537T4R1yZOzzFTFs3i9NcTdJyt3JQcVnsu3w1gmjf2kKkn-HS6QfZ1ljHIeyxCykD8abZLOovykh_TSjEdQ5K1U_-scLFmFHBxUN-LVxVooVi7gpqCZ4NBYoGWfi0H-4NF5GXnA2N2OnYekBIdXtfarFGb-ic0QxGEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمعات شبانه
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68719" target="_blank">📅 17:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68718">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iogRZfjWmYDZUGto1xriwA322blkFLAgv5QrmkAds27vkVtLtwfdzg0C7juoSqzamsmiBrTK9hFrhpiuQTX4jrWGlYH766PwjBQpFZgButHuzquiuYTCHcMsCU3u57d8-ZwB2HxnmSBqGC0G6wm--xuPW89IOc2BDVwRk5c5w9Mvfz7VtUrD2BNVKcFRN3PCg5a7_Quj7-gI6tZvGsVa72i9kGc1Q3VuBAu-Xct-r7Z8wy7zpsxFuv7WCCl3cTRTL5eanld4RnAy86SH55od99qpe48FvmLJZpHCPY968CNvrpUzX05nCzweFrbw8c48JKtwch4E0RAz6G5N6GsYxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
هویت نظامی آمریکایی که در جریان انهدام کنترل‌شدۀ یک پهپاد تهاجمی ایرانی در پایگاه هوایی اربیل در تاریخ ۱۹ ژوئیه کشته شد، گروهبان «مایکل سوینتون»، ۳۰ ساله و اهل فایت‌ویل در ایالت کارولینای شمالی، اعلام شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68718" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68717">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da37587eed.mp4?token=LHLUKfO2q0ts_1OlsVYxKtL_xhSaryf_nzgsS6IRORD-f_XDQ6DLLjCihnGA7NvJxbRsum9Zx_xfHXvj8sIrOI6JCgPZv_QUlEIffAfLJIKDrh8Z_R-LeUc1UhMHIN6UVaKWry7Jh5rABIZQiSKk6x5v3U6RHMN9EP1U6Z83Ypvcg1e9_6I3UaMJVVsP2aN0HaFYQ7Kr43cMPlclQ48OJJSxQF6Cz-ZVFwBJwTsMavw4KMSeBIXN92SC4PpPTGts7X9I2EYtuyzBujCSjxM30uWbrCwWvlCd5RaOFSBDjXlwBW928kgbOmMAXD6MCVkfuIgEJjATQV7bnUy5Aj00pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da37587eed.mp4?token=LHLUKfO2q0ts_1OlsVYxKtL_xhSaryf_nzgsS6IRORD-f_XDQ6DLLjCihnGA7NvJxbRsum9Zx_xfHXvj8sIrOI6JCgPZv_QUlEIffAfLJIKDrh8Z_R-LeUc1UhMHIN6UVaKWry7Jh5rABIZQiSKk6x5v3U6RHMN9EP1U6Z83Ypvcg1e9_6I3UaMJVVsP2aN0HaFYQ7Kr43cMPlclQ48OJJSxQF6Cz-ZVFwBJwTsMavw4KMSeBIXN92SC4PpPTGts7X9I2EYtuyzBujCSjxM30uWbrCwWvlCd5RaOFSBDjXlwBW928kgbOmMAXD6MCVkfuIgEJjATQV7bnUy5Aj00pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شاهزاده رضا پهلوی در گفتگو با رویترز:
«دخالت خارجی در ایران لازمه. این مداخله در واقع می‌تونه باعث بشه جان آدم‌های بیشتری نجات پیدا کنه؛ آدم‌هایی که در غیر این صورت ممکنه کشته بشن.
جایگاه من به‌عنوان رهبر دوره انتقال اینه که مقصد نهایی نیستم؛ من فقط پلی هستم برای رسیدن به اون مقصد.
برای اینکه بتونم نقش یه داور بی‌طرف رو داشته باشم، خودم رو وارد هیچ جناحی نمی‌کنم. نه طرفدار پادشاهی هستم، نه جمهوری.
وظیفه من اینه که مطمئن بشم یه بحث سالم شکل می‌گیره و در نهایت، این مردم هستن که تصمیم می‌گیرن چه نوع حکومتی رو برای آینده‌شون می‌خوان.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68717" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68716">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68716" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68715">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKb6GgaJ3Vm4kTs1ZAerjiDoj6Am1I-H7JIg7BdlKlP1CVB9GI_8j0FfdEaK3yTP8JLdQW1uNzE7Vw3uX8vK3PgQIADMPk1qR2hM2epw9xklrDvnVSs9ZArFgScjB0hP96SGWQ5F6Vf2NLgloQdD7eZQC7AE3kxQUw4DB7GPU7ZkvhD8qlka-bvaYa_J2K8pDthLPRR5BOzWpgbGO6VAjw35s3y-Lbelv4dLwUXMC_q8DqU4Rmlqm8X1m5P_V3CWeofns8rXUlHa_LJO9ILn7WrmMwIu5uSsWzWYrD19ZM5I0QO3mTbblCDXDhiUnLzbwDnZSvO_WmGcYeq5W1udRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68715" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68714">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFFMxQ0My9aF91jQnC8hIFmOZQx5EkbAOsv53b3ugm3dj18KLoAVVMKIBQB5wz1EVLDCQndQCL4C1EG4CKvNU7XY46Mv83StYtet0_UcTjRk8DB6TN24b-SYNcEnJe_LBhWFeII0e1QGtenD-WRQQax-aIaMIk3vJdoJm23yyesLLRQa_00IJ4ipsDNhDmeGRSeHAHDHvYC4ihbOd5zTSXXkiEev2b_ASOR-0BFoeQLl8CMgD9eU317zjy_ji_hhU4Nx3eRKcfzVvifqCw8lzLV4F5wnLFMbeVGt9EtZasP_mkeY3P0mPqepL4Z4bhICL1ZPQE67MFXMxl_kE4c-kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مراد ویسی، عباس عراقچی رو فالو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68714" target="_blank">📅 15:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68713">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‼️
🤩
عکس یامال و تیم ملی اسپانیا روی پهباد شاهد چسبوندن که بفرستنش سمت مواضع آمریکا تو منطقه  @News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68713" target="_blank">📅 15:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68712">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6161f8d4.mp4?token=bXYs0fNl7-RKSqzZulKEPV8HKiRacn8yk6ehgzxwy6vot1apoGTPWBRsJ3W8t3Pm9xa2h4o3lQYv8nyqV-gEWQP-9XydPyuk3DIkK8zQPyXdSac8V_exqZbH4JBb1H4yperrYHcnHkQk-_PSyEYAQcFOw6M7uSk0rMub6FQLFKoqYhDN21LuZ5tscjcTFWLO7GiJzVhP8-7A4Ii-BoPWos9OfZfXIBHqp-5wefEVvK4EpO2WO-709BvTbeDHC0rV5PXeSnBWqRq8FXGn8sjsHi8mYoC2U0Vx-0xGRdsH3yfCP0otOjjTb80WTws-OpP4TC8CyoGu7N6l_d2kIGXCSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6161f8d4.mp4?token=bXYs0fNl7-RKSqzZulKEPV8HKiRacn8yk6ehgzxwy6vot1apoGTPWBRsJ3W8t3Pm9xa2h4o3lQYv8nyqV-gEWQP-9XydPyuk3DIkK8zQPyXdSac8V_exqZbH4JBb1H4yperrYHcnHkQk-_PSyEYAQcFOw6M7uSk0rMub6FQLFKoqYhDN21LuZ5tscjcTFWLO7GiJzVhP8-7A4Ii-BoPWos9OfZfXIBHqp-5wefEVvK4EpO2WO-709BvTbeDHC0rV5PXeSnBWqRq8FXGn8sjsHi8mYoC2U0Vx-0xGRdsH3yfCP0otOjjTb80WTws-OpP4TC8CyoGu7N6l_d2kIGXCSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤩
عکس یامال و تیم ملی اسپانیا روی پهباد شاهد چسبوندن که بفرستنش سمت مواضع آمریکا تو منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68712" target="_blank">📅 15:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68711">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iI6jAQhynbVrmREu_WGajUInoeUUyhb-N7qJ5mlkVxMq2MMVmjEwuxtrVKZ9oAFkqcOZtSB4adTIpq30ap4ybxTYyjiPGx_RzCaMLta_fbE8C0YCcvFY3nVT4Dag4s6c4z54pf45klgHi4wqSM57x38EcBIIWYsRBzWVlBP7jDqtDrBnr8aHFm7JE1OqU5IsgayCw_hPcBzA9zJmMmJxXLgskBK4zwDj_zKWes21tygjsJ8_ZeKIqW91_S18g9QxMxWDiiahB45bU0DpEzXeYeCoZhiIJfE_2mlsgtPQ1HXKRqRGsvRlvuLwyUJ020xRFvaQSTWI2oQxrwVFziKRng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
با اعلام مقام‌های کویتی ،  چندین نیروگاه برق و تأسیسات آب‌شیرین‌کن این کشور در جریان حملات روز دوشنبه جمهوری اسلامی هدف قرار گرفته‌اند و دچار خسارات عمده‌ایی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68711" target="_blank">📅 15:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68710">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd31fc49e.mp4?token=VgSlx54rb4UykJRFbu9DYRY4G5L36IHvCo3IgoW3iqPrbmJRnISkmbAyD7BMLz9NE8hXPb5yC5ddLmdhF6QFDYypcxbcawSDI9GV0wjB5VCIMkg7Eg3kRF81Urw3d0k6wczQapmKJgIS4Ems8FnFQaM40YculGE8MBl_B7kEGbrywMRLHmQdLDgrBGzjjCWifEyy8TG99GCNpHox7z3qoiaO-W6MZ1qBQlIirc0qg2Xx1kq40XHaf0cDmukgR6sHbYzN0zyDaiQYpufh8ALPMcqTCDzpm0fRlUOuvD508oYnXbxdzjrK-LBCNtEoQzcRM3DX2R-yMxW5bB_snMrTTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd31fc49e.mp4?token=VgSlx54rb4UykJRFbu9DYRY4G5L36IHvCo3IgoW3iqPrbmJRnISkmbAyD7BMLz9NE8hXPb5yC5ddLmdhF6QFDYypcxbcawSDI9GV0wjB5VCIMkg7Eg3kRF81Urw3d0k6wczQapmKJgIS4Ems8FnFQaM40YculGE8MBl_B7kEGbrywMRLHmQdLDgrBGzjjCWifEyy8TG99GCNpHox7z3qoiaO-W6MZ1qBQlIirc0qg2Xx1kq40XHaf0cDmukgR6sHbYzN0zyDaiQYpufh8ALPMcqTCDzpm0fRlUOuvD508oYnXbxdzjrK-LBCNtEoQzcRM3DX2R-yMxW5bB_snMrTTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ها؟
درست شنیدم؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68710" target="_blank">📅 14:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68709">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
صداوسیما:
دقایقی قبل نقطه‌ای در ارتفاعات خرم‌آباد هدف حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68709" target="_blank">📅 14:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68708">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🇮🇱
وای‌نت:
مقامات ارشد اسرائیلی مدعی‌اند که تیم «جی‌دی ونس» مانع از برگزاری دیدار میان نتانیاهو و ترامپ می‌شود تا از اتخاذ مواضع تند و جنگ‌طلبانه علیه ایران توسط ترامپ جلوگیری کند.
نخست‌وزیر اسرائیل قصد دارد این سفر را با مراسم خاکسپاری سناتور گراهام در ۲۷ ژوئیه هماهنگ کند، اما تا زمانی که از قطعی شدن دیدار با ترامپ اطمینان حاصل نکند، به این سفر نخواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68708" target="_blank">📅 13:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68707">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f5cc929c.mp4?token=A8PdrtatV4YyNg7qf7s3p14VXLkVDpRcOxasmtU6Omte_gDs6OZqsxAabRoW7hjBIzgnmxz6LVyarwesujcGtOgkhkmikgIPsTvekbvWr9AU6QKqyof-D2_piXvTPYDV-_xmd4Is4TIOjSdwTfRADdCKS1Fltudn4hTm_ieoffdiUe8sD_IDKvETwjIJJpfT6eyA3_XzEu1zOfQudXTYMmctTPv-U0AMLIvMDYglPtXL6xqEOHYEKXWTjGRn8ZC7Rbu9Ua-iFqHPC3xRJqp2YxtM6ccgiUk9xKK01myWgQkZmVtXIaeuz37NN3868xdjhnbBi972E6cc0mnL9l103w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f5cc929c.mp4?token=A8PdrtatV4YyNg7qf7s3p14VXLkVDpRcOxasmtU6Omte_gDs6OZqsxAabRoW7hjBIzgnmxz6LVyarwesujcGtOgkhkmikgIPsTvekbvWr9AU6QKqyof-D2_piXvTPYDV-_xmd4Is4TIOjSdwTfRADdCKS1Fltudn4hTm_ieoffdiUe8sD_IDKvETwjIJJpfT6eyA3_XzEu1zOfQudXTYMmctTPv-U0AMLIvMDYglPtXL6xqEOHYEKXWTjGRn8ZC7Rbu9Ua-iFqHPC3xRJqp2YxtM6ccgiUk9xKK01myWgQkZmVtXIaeuz37NN3868xdjhnbBi972E6cc0mnL9l103w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پاسخ دفتر شاهزاده رضا پهلوی به صحبت‌های عباس عراقچی درمورد توافق پهلوی با اسرائیل برای تجزیه ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68707" target="_blank">📅 13:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68706">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427c084f6e.mp4?token=OOHFg6TrwEAJ7i-gZJ9ripI5SATBcVJU8kXsktwf2yawu0hTElQvsJaTQNVEvQrlGReWVtBa5wWV-px7T8aUlBtTPYHsgJCMAOxzgBDaVe9nQMhxWrkWw7Voo2cKKbeJmxUL9c549cs5mrBlSryd-am4TOS5UR0wv05h5b-ClDX4SgL5nsEeZYr66BQ0ikIe3UhJKMK1AotLOoos0p0ewDn0JDfE2UpIr00uRQ_l-u7D_1bU9XyP_yZXLihhw3TW11qCSVej9mEUrbavleH5jMNPqfH4IEgObMRV6CGlO3sVOwA4Tyywg_8_DIno0NHRF_h6xL8aKDL6LrLhEuigqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427c084f6e.mp4?token=OOHFg6TrwEAJ7i-gZJ9ripI5SATBcVJU8kXsktwf2yawu0hTElQvsJaTQNVEvQrlGReWVtBa5wWV-px7T8aUlBtTPYHsgJCMAOxzgBDaVe9nQMhxWrkWw7Voo2cKKbeJmxUL9c549cs5mrBlSryd-am4TOS5UR0wv05h5b-ClDX4SgL5nsEeZYr66BQ0ikIe3UhJKMK1AotLOoos0p0ewDn0JDfE2UpIr00uRQ_l-u7D_1bU9XyP_yZXLihhw3TW11qCSVej9mEUrbavleH5jMNPqfH4IEgObMRV6CGlO3sVOwA4Tyywg_8_DIno0NHRF_h6xL8aKDL6LrLhEuigqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حملات دیشب سنتکام به مراکز فرماندهی نظامی، توانایی‌های دریایی، سایت‌های پرتاب موشک و پهپاد و سیستم‌های دفاع هوایی جمهوری اسلامی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68706" target="_blank">📅 12:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68704">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BS94Kt81_dHHYVFpQ2ZkHmg9MANP9rHS7-cDShYG7AMqvbFXHsltxQAns14q1zyWcp84X-xYDucGBijXk16dYUCU2GewmqDxO9ZmrydHKcS5yTwbUg5O1fwGH7ZC3-FYLTUakUU4_W5nLRH18JQUx1FTTfK3SZV-H949R3IQ4RBFHyFj0KydKrB4Hqfwa4hG2iC0e790gCEZ6j37zthld93COez-v_LCYxXm-Xk3sGr_q2Rp5yU8RNQTYBEm-w-rnDSbX7QkuREbvQrEU_H9-viBNyloOF9M-gSiswMaTr-ILKmRWTS22Eg8GvUAs7T5ueFh9-pF9i8cQSwV0GXcvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jntmb8-p3GqNC3oFkUh_mwZQD9o_yrOatv-umow7UecWMLVeHRl3TLeVdXh4dVu7OXzMNYYnauByMDXdowdk9PMxniOHk9yQvs7d107j-KUPBT2_6AxchinU4oFRY4nl0KYkLzV1ox_lYuaXAEEYzChjUqP_XnpEkDmUH6i58sJL9YX3yFnxe0-HHxPNuagaQvnYAOMg6OAj0ernzqHgD1iBdLkd1uU-1DTCwKtTkhgNc8_BmkzFUQkheIUAt3SGcFhT8Vwlsmx7d9Q4f1kGtVQZxCndlzYdNsiG8SEC5rHpKb9cAcO6GyeaOXRBMiq5577aJ9rT_tLkKUN8Py44Jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
دقایقی قبل سپاه از زنجان و همدان به سمت پایگاه آمریکا در اردن موشک شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68704" target="_blank">📅 12:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68703">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0d3ZDJhQ4ir9RdbNQ2Cc0TuK27XHMVtZi3qhpNCSAVFV6nuXIo9pwvaeHCNJj3g80QZSHkspIcMI_ruBPt33EtjTYBMPjn_DD37LQeZqcYPYeGVdGUVaxnB3pPxpnQpYp3sTn1deksKI-Yimz2JuHG9BI7kO43P88kE6513R8974ME8l12JeiRdMESdf2FV0E_V9oOlcjvaXXw926CN1BP2j3DsV1Tw9YEQNNQfCzb_8eGUqcvddks4aUoiOsERPurQVF_S62ICRIJuItk5HsFD6xqCk8I8FWPBCx2YGIE1yQ0JcbuqAlYgdYebW5zVm4hASB76TYH5gBnTmU6wQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
در خصوص مناقشه با ایران، مقامات ارشد آمریکایی و اسرائیلی استدلال می‌کنند که تنها دو گزینه واقع‌بینانه پیش روی ترامپ وجود دارد:
پیگیری یک آتش‌بس ۱۰ روزه جدید با هدف بازگشایی تنگه هرمز
آغاز یک عملیات نظامی گسترده و جدید به همراه اسرائیل برای وادار کردن تهران به تسلیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68703" target="_blank">📅 11:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68702">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⁉️
مقایسه ایران و نروژ:
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68702" target="_blank">📅 11:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68701">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b4d07166.mp4?token=G7ud0LNfvo6vioAjXF8RkXlRDrYa1IN9BeBC5hq39TfrfMn7b9OLsA8VzoR1yn51cKs1oPDD8e4rf7c8DdNqWuOQEEy_aMrhbXLbCkIAOmCAwek3mvf5fT7snq6JQPzu9R4W07sr2g_1d0EwFV66Xb4dLd6MfqNRAtLDFapKpp302wgB8TXEj1g2R2s5KnVS1yk5XOk0hKxfGL1e_aX-nZ7KqeD7y7WqhL3-p-LPBj2Y7iXO4zPX2t6B_ATJw_1R-ggXq6DnWkub9pcmFH2Yr-0y2Jr2W9NXA0Y-lV2KYmnqCIyRaRyS0OCmdb_avQMuqQYMynLrblQpub4_OsjJrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b4d07166.mp4?token=G7ud0LNfvo6vioAjXF8RkXlRDrYa1IN9BeBC5hq39TfrfMn7b9OLsA8VzoR1yn51cKs1oPDD8e4rf7c8DdNqWuOQEEy_aMrhbXLbCkIAOmCAwek3mvf5fT7snq6JQPzu9R4W07sr2g_1d0EwFV66Xb4dLd6MfqNRAtLDFapKpp302wgB8TXEj1g2R2s5KnVS1yk5XOk0hKxfGL1e_aX-nZ7KqeD7y7WqhL3-p-LPBj2Y7iXO4zPX2t6B_ATJw_1R-ggXq6DnWkub9pcmFH2Yr-0y2Jr2W9NXA0Y-lV2KYmnqCIyRaRyS0OCmdb_avQMuqQYMynLrblQpub4_OsjJrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
اکرمی‌نیا، سخنگوی ارتش:
اگه پای آمریکا به بخشی از خاک کشور برسه، منطقِ جنگ اینه‌ که اون منطقه رو هم بزنیم و هدف قرار بدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68701" target="_blank">📅 10:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68700">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c2573b8c6.mp4?token=OwtlBp4E_yczm_UMYl-brwzNRe3zD4mB0Ej0dNwiUvjKenbgCMuIyr8P5YymOVT--hKbxxNdetcVbwFCr1BoGdb-5X2xi2N_6jR0NUrgzu748mo21Cr1ED27JHRzge7hImMfbo6NN9ZQgCfj9QqSXsjJ-tf3M-U9_6bWW1Yhg1vnRHqodJUvzWJGPfKKPeV8yRze0zSTXPGWx3r_l7rzAKmHgS5vn1yvDB50u64hbMPaqjA00yUMoAEH9iZk1RqwlT1kv1FPl2pk9a-TZcH6iF0BuKygw_AcSoMsBlGz8LNB4X33xLzRTh_kC4cd43f5l4f-EJUPZdv7d_IQv5JL2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c2573b8c6.mp4?token=OwtlBp4E_yczm_UMYl-brwzNRe3zD4mB0Ej0dNwiUvjKenbgCMuIyr8P5YymOVT--hKbxxNdetcVbwFCr1BoGdb-5X2xi2N_6jR0NUrgzu748mo21Cr1ED27JHRzge7hImMfbo6NN9ZQgCfj9QqSXsjJ-tf3M-U9_6bWW1Yhg1vnRHqodJUvzWJGPfKKPeV8yRze0zSTXPGWx3r_l7rzAKmHgS5vn1yvDB50u64hbMPaqjA00yUMoAEH9iZk1RqwlT1kv1FPl2pk9a-TZcH6iF0BuKygw_AcSoMsBlGz8LNB4X33xLzRTh_kC4cd43f5l4f-EJUPZdv7d_IQv5JL2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در سال ۲۰۰۵، نیروی دریایی آمریکا ناو هواپیمابر USS America را هفته‌ها زیر شدیدترین آزمایش‌های انفجاری قرار داد؛ انفجارهایی که حملات اژدر، مین دریایی و آسیب‌های واقعی میدان نبرد را شبیه‌سازی می‌کردند.
هدف یک چیز بود:
فهمیدن اینکه یک ناو هواپیمابر تا کجا مقاومت می‌کند، چگونه آسیب می‌بیند و در نهایت چگونه غرق می‌شود.
این ناو بعد از حدود 4هفته آزمایش با انفجار های کنترل‌شده و بررسی مقاومت سازه در14مه2005 عمدا در اقیانوس اطلس غرق شد.
نتایج این آزمایش بعدها در طراحی و افزایش مقاومت نسل جدید ناوهای هواپیمابر آمریکا به کار گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68700" target="_blank">📅 10:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68699">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9ecf589fd.mp4?token=Z0P9G1JedT72EHCslKptFzkx3uRs9KncYGyCd_BrcD5rzfxaRFm9XftzgcI29Rv9GqM1bnm1bprNE8BNWV9hEjvLgecKQgtPnR-BaE6EAD_ZVM6T5hqq0X1jRXBVsPAXYabnnv8_T9pBnk1D4048meZAnwf8FfrNGww7JGTJkNa11Fj8mJ9a7_WEGcC2Ql9rrci9jusXzt0_0ly5zd-1zue-0IZm5xUMXE6FrvcxrkoKajXFviHcZUxYOEHWimt6VYZTz2Hl2G-PEzcMYjS2lDJKZxQRbVth2Ynxs9vx-Bu9Kkb1ewA3dxmu3OD2d65Afrxl51T-vlq4hJyFkHg5rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9ecf589fd.mp4?token=Z0P9G1JedT72EHCslKptFzkx3uRs9KncYGyCd_BrcD5rzfxaRFm9XftzgcI29Rv9GqM1bnm1bprNE8BNWV9hEjvLgecKQgtPnR-BaE6EAD_ZVM6T5hqq0X1jRXBVsPAXYabnnv8_T9pBnk1D4048meZAnwf8FfrNGww7JGTJkNa11Fj8mJ9a7_WEGcC2Ql9rrci9jusXzt0_0ly5zd-1zue-0IZm5xUMXE6FrvcxrkoKajXFviHcZUxYOEHWimt6VYZTz2Hl2G-PEzcMYjS2lDJKZxQRbVth2Ynxs9vx-Bu9Kkb1ewA3dxmu3OD2d65Afrxl51T-vlq4hJyFkHg5rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68699" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68698">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68698" target="_blank">📅 04:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68697">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q04-QQJmdIR_MIzXg5_s9VOHG7VhAk3gxsA2JTwyIGQIfoyDz7UaXdCklcV-ofy_fKgTZZnSkq5HeVUQAilS4KvyJgrO8W3f1bNcNidWFTS5V97hBrbYIrfFZOiO1OCBEsy2rpy07KUJcp63sX5-H1882v-1GW5DjoLyxhOIkWLXkW-fcQWdCo2OA85jvZgPVuPyDx5yuqd14mVotesfrixOdmC2HmuKcHSPvQxNp1DnnjGmvBlQaxmd-0doN60R6TwkmYvVaf4qMkYQqCWFsoY_A_OKiDRdcc1aG8XWa9YqBl200FE0u_r-0NKxyYRAvS3h37Ch4L_4B9g5aQg2rA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68697" target="_blank">📅 04:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68696">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIumOLNsI547iMSxq0xeAfwhZnzE07XcH6FmKrVREHvdaKc-1HTBjpANafu60tilr3hR-9dSMJRKrlK3w9LYTI4mW6U4PsT9BfxxwWYLjbVCmLzSl5CQlHceeocQZGTqxpcfKwzrjGJadEwMIGjTulqB8VwjHZSiA4RyrkmQL1pVm0JUW8m2A8kiCr2i24MHTw7tTAIEQ9w1HWkES-RqtsIYz2Hfd8XUiXl9FkwfRgshh3_I86fk82zLfhKKyoDb28g5wcyH2M73y3R8tDe65c3VfcxkkGN1mEHhbkDMlh2fS-U4rD2hTyM41JyLbtvTmCW9XHpBZZXRbl3VNxGgtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68696" target="_blank">📅 02:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68694">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7xySdGDj643q2bGlQzF_8hj2tYV08CYKuKk8wehCXHkmOv0m1xSvCZwFv0zD9ZrHNS1HIf5iBsmAxflJio7HDL6L0aQ2NsKLvSekJVqMeat77gdougW789OMOQiGNaDQ954evBD-xgrd7n1_AOQvZXodADXj_ZfyfMG--3VRcmSSW8vQKpZXgIGZTkS-7nrFpFu16R2jRR9LhFgdrKuMoND1dTJGzmND5SwVwuAzI6k8OrNfA5XW58-_RirtLNhom0xKYO_K2jC7nA0rB3VESQieXCEI_D-_JPIQTWPnqhGLsmhjsUFT9JJX2cxsnWIKG__ZZTJqHp2bf3FoN81uA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68694" target="_blank">📅 01:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68693">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
پایگاه هوایی بندرعباس رو زدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68693" target="_blank">📅 01:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68692">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
دو انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68692" target="_blank">📅 01:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68691">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZczuLuGwqqUsialgX_331dLOPqyHRoY9XyFqphox3o6C7_8_WfakoxfOdS63Xu35Vrjy2LiszXVwh9TaYhKqMxRnUcGEQgjlx-YSrArCVo2mJkVkrBMujqoVndbdG45skIJ_BLB7_jfSpHPQfGoNLDuQ4Rz23BoA8Ys-0jI0wi7th1auZzOIGkUPouCdlUQgfPpir_JZ9su0-LTdKbFqvAnn2VpWMbClowyFXveBfxChDBodZ5H1mUswDaq1leVD0enSxfJQoVQEdjqq59T7BckoIfGcZ5QdZ1ZySsNLFiCmVY6uHq40VYuVVJepLUpOwQCmF0ZgwbEsr9AQJ6bwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سازمان تجارت دریایی بریتانیا (UKMTO):
یک حادثه در ۸ مایل دریایی شمال شرق LIMAH، عمان گزارش شده است. UKMTO گزارش‌های متعددی دریافت کرده است مبنی بر اینکه یک نفتکش از طریق کانال ۱۶ رادیویی VHF اعلام کرده که مورد اصابت یک شیء ناشناس قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68691" target="_blank">📅 01:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68690">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
مجدد انفجار در بندرلنگه
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68690" target="_blank">📅 01:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68686">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RnZmPBOUFVTWNxtT7mQpd7mhGlZCvBdy7JO3xMlt0BobjmGyQtctW4jR5UsCsLSEWDzrd6l9sDPgey-2S8TuljTkAW2lo0rq8gSNkkRIM7JPq0RqSqsMXdT7cN8WQJgxfP4qDTr5wfXJKwnpaP39mCzk_PffdAvocR2lyKYCXBbgZsSr_jCWfAvk4onLfx2zVCQS1OL561MguQyhpxFSv2-bpTq5cfP7oAiCQeaPzeJxgHG5zYC0Ryb_zDG3TsCyHorMEHGlPEAyy6azhl-e7USOR5TL8iLldN1hpvPBEqr6XMZef3KWPx-FciukbjwCnZEX_c6lp2-__XVb4hS2sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bxZq0UQ_YLckf34w8n5gxHgW8HT51NjOoYkLM6dbQ3KoZCl8BS5jFsCUQ8CFXx64UJ8taxRaZyTImGTBVMOo765OjnpjVyWEcYUFpT1nqRAPR0j6bHgyYWW5-84rxLnwdBBrv1n_P-17Odyml5eJ7PyDr2O8LWOYLVgHEd4SEKMnNa2NuYzJY8guPrq--DP8Tw2hOJNtj6KQjEaaWaahhacskIvImHq5PRjvROENqIqoSeQAIZcWb5VYeWAjphq3gzjm6kEa5ihmsJ1SKh302qakV7N0J34358UJ_yXge3IP1ZS6h3CiPCeqSkJDTCeTfkQ9z_kGcpvnaG4yq1Bbbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZnZXJkA45md75HhB1Y47hyWhWka1-tvVJuhn4pjKR7rGlb405IDqoBBSUfZfJfboAoB78bF7_qloBO3Ft4T95e_JENo03IbaBNDn3cNUaRcHyofa_7UYOjOhfgblDT4-nP1avARGNGyGIDEez2pzEu8bcaAJMYnMlJTJqvPi1v5ejGzKwPoWGzRcakTsz61MqGjoUwZlO8GKrN5sHWuMRQXE3uO_69bLyQ7EcXCrtLp2f5vE5azO4LmJNgIOYta4lbBVAjb-F1R9LJbzh9SR68CUi_cVprOq44SusPu9rb6jRoPRLwlqe0uJRIsp14vHYWHx8nzsWLyJzQ0niRf9Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dHPyNhLD9aJThQ2IsLqxI42YNMsu5kfCnmVGnUPKa1Em6v10ig8icTovmT7LHtV7gwjf_VUj-5Er28FhL-6ayd5ct9bbzdcwg8vYoBhrYawHnbNg_sIEQiela7gFazQ4m2Mzz7YlENlIws7Ee8uI6KA2BNBRHuh_QLOHKklnRsUVdgh0GDOuv7mjlpPpjdEp3pFpO4My2VgvvruO9EkmeYGd-vpKMdq3xDHJ5SpIQTqJKrbUbTermO6l8K6mg4ZDE-yXZtahOqnarP5heEFL2oVhGHRFeOHIFCHe_VJl5lYRvecbFO3w7W5D5qYtcKpHIXSRBldmSIXkjB_6klepQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کوه دراک شیراز زدن
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68686" target="_blank">📅 01:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68685">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6bdf4b6292.mp4?token=M1-QPwhZjGCgiJCindXFUDMhPq2OzW97SlCHoZxxkKs9SZyQhT3aG1isq-spjqo-DSiGW673Y5HojM4ebkWk6zYpZ3mnPGXHz06LPnlxGw97sI-QyXMiKjc5vf5HS9oLrONRy49_gRwdeoITKAOfoi_9XgzBisgwj05OIC8PcXhCspD4B5le9fV21fBNPR_6BCfZ3ct0PX8bxIdOevqg4t-QONyJmrHcoCveo4B6W09IOMt2r906R1VG16f8XAIiw_SlRzmLszE0oQTQORLMButG6_FVUg6j3r_AsG2JCXmKgQiZduDTHZ9ThvMX40nrzZPh6o1pnat0X2-EpzHJ-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6bdf4b6292.mp4?token=M1-QPwhZjGCgiJCindXFUDMhPq2OzW97SlCHoZxxkKs9SZyQhT3aG1isq-spjqo-DSiGW673Y5HojM4ebkWk6zYpZ3mnPGXHz06LPnlxGw97sI-QyXMiKjc5vf5HS9oLrONRy49_gRwdeoITKAOfoi_9XgzBisgwj05OIC8PcXhCspD4B5le9fV21fBNPR_6BCfZ3ct0PX8bxIdOevqg4t-QONyJmrHcoCveo4B6W09IOMt2r906R1VG16f8XAIiw_SlRzmLszE0oQTQORLMButG6_FVUg6j3r_AsG2JCXmKgQiZduDTHZ9ThvMX40nrzZPh6o1pnat0X2-EpzHJ-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فعالیت پدافند در کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68685" target="_blank">📅 00:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68684">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0oWZVlMey3DkFtqMEzKdhaf5zKWKRrONsrbj7rHIZQfGmwdfJtwA6ucz6LRKpEhF6_VGnEPq3upWrd0iqj1MX4USGqaBNJQty_zaFk_dW4odr2oS91jLS-KfBzmCycDtcmfAzg6x-16mgZ2RBktlV31oE73kLJojZuD-sDtaJqMwokGPebXhp0_VOkwv59ABxlenNtewErs_ULEhCS98lhasFbYvgnoPM7-UUUTjm_x9hSI9reLQe74n2mR3Me0vcAvyYiV1s5MRokOAJFrP3DKg8JMBMi-gdOXKIHlOnVZOyNymm1boPx8F87Y3nTuJVFosoz6QZ5Uqx0JszGfhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژیر ها در کویت به صدا درآمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68684" target="_blank">📅 00:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68683">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6040eb52.mp4?token=uR3xcKT4K9Mi3GZLmNYGl51PSt54M27uzYDfIfHqPHsvnjAuTZLSqsYHZ5Q40UkpgboH3c3nCjmSx3WLjdVDgcTxpyKOxxfKbIYXJoTwh5VRMD3L66xf49SleSQkE9pE1fkYVBB5dTY51qaKeGOKh7Stmco1DQGO-d5M9XlbZK9FH3QJBNtFqMlbk0N47y5l38UocVuZJZOR3dIPEq2eriPA-VdSMIuUstsv8pRvVCAuBJ2s9JYti7qwjq03eGFdQIiEC84b6DN-YyYm2mAVRf05aDgq1mNzK-6cjBISX2BQRbbonWHAo19kGGoPXPVWbH0V4svzGmmaTOG9OUUGPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6040eb52.mp4?token=uR3xcKT4K9Mi3GZLmNYGl51PSt54M27uzYDfIfHqPHsvnjAuTZLSqsYHZ5Q40UkpgboH3c3nCjmSx3WLjdVDgcTxpyKOxxfKbIYXJoTwh5VRMD3L66xf49SleSQkE9pE1fkYVBB5dTY51qaKeGOKh7Stmco1DQGO-d5M9XlbZK9FH3QJBNtFqMlbk0N47y5l38UocVuZJZOR3dIPEq2eriPA-VdSMIuUstsv8pRvVCAuBJ2s9JYti7qwjq03eGFdQIiEC84b6DN-YyYm2mAVRf05aDgq1mNzK-6cjBISX2BQRbbonWHAo19kGGoPXPVWbH0V4svzGmmaTOG9OUUGPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68683" target="_blank">📅 00:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68682">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
مجدد بندرعباس و بندرلنگه انفجار رخ داد
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68682" target="_blank">📅 00:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68681">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
انفجار در اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68681" target="_blank">📅 00:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68680">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
انفجار شدید در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68680" target="_blank">📅 00:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68678">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d45723674d.mp4?token=G92fK1IaxdfLguhqCMgjY7e4vhDU3GGuhpCxt4Ir4-ZX7mW8psMCEsh0McYkbLY7Bx6nsVjc28-Xeuy2tITefLq4c-H5PldvI9-HdUhmL7HZ1xUIXdBmzHQPa09Hnd8AhelrQJqKiQRgKAvbSKKSdmMYoKgq_RrMGjOYljUbsg5ngNG_2MbPQnlgKx4bv2HfeswlIas1Eh2gC1z9pYEbTBI1x0scNsq9hGzRM4lGxqK6AZx7Riw7CnUQfs2MHF0qnSne6hmfxUbZzppcOMinyf8XA--fAywicdMKp9gYMXLr2JZ-Cx76bD2ZwrySDsGHUed1QMtm12Tqhaz3BXwQ3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d45723674d.mp4?token=G92fK1IaxdfLguhqCMgjY7e4vhDU3GGuhpCxt4Ir4-ZX7mW8psMCEsh0McYkbLY7Bx6nsVjc28-Xeuy2tITefLq4c-H5PldvI9-HdUhmL7HZ1xUIXdBmzHQPa09Hnd8AhelrQJqKiQRgKAvbSKKSdmMYoKgq_RrMGjOYljUbsg5ngNG_2MbPQnlgKx4bv2HfeswlIas1Eh2gC1z9pYEbTBI1x0scNsq9hGzRM4lGxqK6AZx7Riw7CnUQfs2MHF0qnSne6hmfxUbZzppcOMinyf8XA--fAywicdMKp9gYMXLr2JZ-Cx76bD2ZwrySDsGHUed1QMtm12Tqhaz3BXwQ3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
منتسب به چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68678" target="_blank">📅 00:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68677">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
ایرنا:
در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68677" target="_blank">📅 00:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68676">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">امشب دهمین شب حملات به جنوبه، اگه این حملات یکسال طول بکشه، هیچ مسئولی حتی آخ هم نمی‌گه، چون اینا با حرومزاده هاشون راحت تو پنت‌هاوس‌شون دراز کشیدن و می‌دونن کشته نمی‌شن، پس تهش میان می‌گن چند تا #پرتابه بوده، دوای درد اینا همون مردیه که الان تو اورشلیم نشسته،…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68676" target="_blank">📅 00:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68675">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
انفجار در بخش بمانی سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68675" target="_blank">📅 00:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68674">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
سنت‌کام:  دور جدیدی از حملات به ایران آغاز شد.  @News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68674" target="_blank">📅 00:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68673">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
چندین انفجار سنگین در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68673" target="_blank">📅 00:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68672">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
شنیده شدن صدای چند انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68672" target="_blank">📅 00:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68671">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmgoJDAm0P9okmc1_4fV3N8-Xp-_pABMoEZKB8euUwQhxJ40ag56l_hJoSBSLeAXJemfN7sMd0P-vB3CRGBd_OWTdB84VyD1Vu2PoaSWT1EvYXoxuGYoaf7wgAaX0fgrj3GPsUa-t5-n9KGc7GZ6vMzHjWle1lhvmL5nC_9wsrcoUHl0NaySmK7y6zCrS0rLeG_wzFmRROGfyU9e4NH33E2m1oKR1mm_YJbKU4rjUQzT2tm61BseXK4k0GA5B9rAkUYUvFtVgYBaMhNOJQ9KTisSflLCWU99NWzXx-SOgIzYa47-nm9NtnHca0UmJPxFkdGVNziZqaRxPEuZE0dKpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنت‌کام:
دور جدیدی از حملات به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68671" target="_blank">📅 00:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68669">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
گزارش‌ها از آغاز حملات به چابهار، قشم و بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68669" target="_blank">📅 00:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68668">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWjrmt12JgBsNyvkiiVitSX8WR42n9RNJwQ7i90F-mPl66S5P_HYCKCZX0uUW5WtqIl5ihOvWAp8OnLrjEqU6xK9wdcn10Fh13zW12RiuycFBqqD-rv7A3OZwttoNkeyuA76_X-CgM2mLmljKmvPgSZDDbv2C48JG55_Y_UsW-R0MhWV4QCBbIMgTqG9fCT5mvvAWvZRZMT-gPjm1h4ZdDWN4j1a2G7CicpwM-XFsV1f5hBX4SJbw1Y2S1vAKF61NfjoH9orYOKos4TvBi-6GVR8F7Vi_uqU-nJ7OeQvJxYFsuv5kKxm3KjJGZYpFY2NMrNhFk9nI-yME0Jw1PZKrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
🤯
🤯
🤯
🤯
🤯
🤯
🤯
🤯
🤯
#hjAly‌</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68668" target="_blank">📅 23:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68667">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfs5aerDOlnIhgXQCMC9AIOyvqTaYRnaDKSsaUzon_rkPivmHt1615SM4wd9Opsgm4M2j7Uy5FrG0Bor33vWfSpM784eK-n9z9YxadBm_SMESIxNgVSAJ-kzb5c-EfvGrEyUo8gqcDgMpqs0I3U_bAXk5B43PsdJiBnHEuwqGddPPXDuMtqXMLsQkbgjA8QwOxhGPYZ78SwJdeL3jjCKr9b04iElRaui8xvPcViIQrWtkrgJjcSvlRkFlhjtzfDOf6CjTiV2VXOCvdQImrHtQ1u8PRRPWHfLeh63-N0h2YbEbzbj0Y0uEYNlPoYfgKZXyLrPIVJjfFNJz2povOOeEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک راوید:
«در حال حاضر، تمرکز رئیس‌جمهور ترامپ بر این است که ایران را بابت نقض تفاهم‌نامه (MOU) و اقدامات تروریستی مداومش در تنگه هرمز،پاسخگو کند.
به‌علاوه رئیس‌جمهور، ایران را بابت مرگ اخیر سربازان آمریکایی پاسخگو خواهد کرد و هزینه آن را از این کشور خواهد ستاند.
این ضربات سنگین تا زمانی که رئیس‌جمهور تصمیم دیگری بگیرد ادامه خواهد یافت، اما مذاکرات میان کشورهای ما همچنان در جریان است.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68667" target="_blank">📅 23:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68666">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
دو انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68666" target="_blank">📅 23:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68665">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeabf951b2.mp4?token=c88E1pfCaZ-tzKhZg_vRUkP52HtjIG6FHS6pSOJdimLX6TAQuCtawaynqlE1GuUUan92U7Dq1ABjHPKJV77Rk0L-fY6xVnMWxcyj41Jg7cN8WS1b5qekxbRl01uYKjpf6FzFUl7_8K2sVxLH4jupzxoHM2gXNd8KzF_aFiYvDrUZTqtKfexVWn-87d1UaZrF-oXL-G1hBrnrYq1AsH47mtEM_0-eGxoUp1V8WkgVaDv4hEBlylI9NXCMTJeXhz3Cjgw32SRNAJEG3CIE0BELCMLDAaIkLixVPUQabgeIzhHL1PM00fCz6huWarHBiMTVyKSJDoXmulm5btn4USSvTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeabf951b2.mp4?token=c88E1pfCaZ-tzKhZg_vRUkP52HtjIG6FHS6pSOJdimLX6TAQuCtawaynqlE1GuUUan92U7Dq1ABjHPKJV77Rk0L-fY6xVnMWxcyj41Jg7cN8WS1b5qekxbRl01uYKjpf6FzFUl7_8K2sVxLH4jupzxoHM2gXNd8KzF_aFiYvDrUZTqtKfexVWn-87d1UaZrF-oXL-G1hBrnrYq1AsH47mtEM_0-eGxoUp1V8WkgVaDv4hEBlylI9NXCMTJeXhz3Cjgw32SRNAJEG3CIE0BELCMLDAaIkLixVPUQabgeIzhHL1PM00fCz6huWarHBiMTVyKSJDoXmulm5btn4USSvTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو یه برنامه اینترنتی، به ایمان صفا (بازیگر) یه جایزه 12-13 سانتی دادن؛
مجریه میگه اینم یه هدیه کوچیک از طرف ما که به ایمان صفا برمی‌خوره و میگه بخدا این کوچیک نیست ، اعتماد به نفس ما رو خراب نکن...
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68665" target="_blank">📅 23:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68664">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0YZe8ciWE-gH6E-MIjysWG6Hs4eiDjvZodxvw01ShyatMomcSokWJICqvKH9Dp8vtNSYKrZgp8WqqQ2qjelUen3mVkq-jm9dL96VzbFgSB6NWgF-dGK9bVEiPX23Y1sVVftVrQx0ZhpHJmrDm0XPjUVPMeuVDoI7uvXIWAhf8cRBmom_69u7U4dubrb37cpeDNrQBTquiaK_96l4I_8BHpkp0idzbUJiThIFZXJSr2B4OyYJ1ddYPihB656yZBVHO2p20vofswT-nWo4F5QYdvW-UPaXVzjqyw7GaOOdOTK7EPE8cgafL1njrl3OhymjFqBHiH6eZrMhIaY9XWpyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
گزارش وقوع حادثه‌ای در فاصله ۱۷ مایل دریایی شرق دبا در امارات
.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68664" target="_blank">📅 22:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68663">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
رسانهi24:
آمریکا برای مرحله بعدی کارزار علیه جمهوری اسلامی در حال آماده شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68663" target="_blank">📅 22:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68662">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675435558d.mp4?token=UnLagutwnRTLA8URaGFjYyKmQa_PkxTmEGS0Cd4BdB3o_oo3kvWj2OW94CMli4LGCwbTHxOPV1rnQrmfMLPLZ41xnaTsuAkrLCnjGWL2TpzaiyaKahhWWHfUjvyaFckU6cTbhxYdK5PjR7J1_qdoDTfzqoriMN58z16mS0u1uCw4wAQLFOQRgXxVkfqUVIMZJBhHzBA4YEI-WZfDiKQwbLnlqhdvZJ3W7n436sHW29kkcUY8xgJeBnXljDSGZi3HrW4O5yJ-c3WXQs9JbnmIO-fM8mxXBkrgJ4wkpVWUXs6m95rsi1vo1o2oDOP9vVmVC4oTykzIF1HXe99AW8w8Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675435558d.mp4?token=UnLagutwnRTLA8URaGFjYyKmQa_PkxTmEGS0Cd4BdB3o_oo3kvWj2OW94CMli4LGCwbTHxOPV1rnQrmfMLPLZ41xnaTsuAkrLCnjGWL2TpzaiyaKahhWWHfUjvyaFckU6cTbhxYdK5PjR7J1_qdoDTfzqoriMN58z16mS0u1uCw4wAQLFOQRgXxVkfqUVIMZJBhHzBA4YEI-WZfDiKQwbLnlqhdvZJ3W7n436sHW29kkcUY8xgJeBnXljDSGZi3HrW4O5yJ-c3WXQs9JbnmIO-fM8mxXBkrgJ4wkpVWUXs6m95rsi1vo1o2oDOP9vVmVC4oTykzIF1HXe99AW8w8Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن سامانه‌های پدافندی در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68662" target="_blank">📅 21:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68661">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oz6zbIHT3ER3YNhU6zTD73pYJos1VFwXTMedlgr8JbsrocA1u_zgiRtkGICkloLF9M7Mnf-DpRYt91j9uyAwcbEzH0nBh7IqI1XAkVMlr7D5eTn_1OIO5kCDQrQVE5nubCroWxX_kzz691JyzqTfXgy8513PImmNBQEs590fJQk98hTQ3dUjFSNd16UezAt9v2vPklohRqYsZX2X07XlPTJP_g61y5D2upx0te21GpMFFRgqfUd5gg8QybNhom4ZhysmUw_SUfKZ9-py8DvZb4aKNmA8On0fojM4ZcsXIflMftZ3RaEBusyNAxvmZcF5e2r-jvQH4rHZ0P-QMUgFrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68661" target="_blank">📅 21:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68660">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در تبریز؛احتمالا موشک شلیک کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68660" target="_blank">📅 21:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68659">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
نایا رسانه عراقی وابسته به حکومت؛یک منبع در سپاه پاسداران انقلاب اسلامی، که نامش فاش نشد، اعلام کرد:
نیروهای زمینی ارتش ایران در نزدیکی مرز با کویت مستقر شده‌اند و به نظر می‌رسد که نیروهای مسلح ایران در ساعات آینده یک عملیات امنیتی زمینی به سمت کویت انجام خواهند داد.
تیپ ۶۶ ارتش ایران از دزفول به سمت آبادان منتقل شده است، و نیروهای ویژه "صابرین" نیز در آنجا حضور دارند. این عملیات ممکن است در جزیره بوبیان انجام شود، جایی که موشک‌های آمریکایی از نوع ATCAM به سمت جمهوری اسلامی شلیک شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68659" target="_blank">📅 21:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68658">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWyaGdc9hAAZ26jliuaAFG8CHVJdCrfTcV3RqQey0ZrYtshspUBWWDzl4Hy4LKvxAs2c5eTRgK-yvJRe-CPQS3Tp31gM5_Aq0o8rQLL6g2PaiGHaMoODLuEF5nXvk4K3y3cQEu4f1xhZg6dPH_bp4X5PexDBoVn-0aG3vweZI1xbpZJgzr4mSL9lPDfMYXs8B5RnXGACl8w62-KTYExHv1Z9McH_0qr4Hfdx49MwEpucSDSJHb2csT-yS9K-scsvgR3FKVVfoDG54LbQYVeGwiSJBYniaV736nfU-aUUl52vSIE4revWZi2frT9srqQ388qEL2QKUAV4dSPBgeSsQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، توسط شهردار نیویورک، ممدانی، بازداشت نخواهد شد و «اتهامات» مطرح‌شده از سوی دیوان کیفری بین‌المللی علیه او را در خاک ایالات متحده، «باطل و بی‌اثر» خواند.
«بنیامین نتانیاهو در دوران حضورش در ایالات متحده آمریکا، به هیچ وجه و تحت هیچ شرایطی بازداشت نخواهد شد. او در حال مبارزه با جمهوری اسلامی ایران است؛ حکومتی که اخیراً ۵۲ هزار معترض بی‌گناه را به قتل رسانده و طی ۴۷ سال گذشته، سربازان آمریکایی و دیگران را کشته است.»
«تنها کسانی که باید بازداشت شوند، افرادی هستند که ایران را به این چرخه بی‌سابقه مرگ و ویرانی کشانده‌اند؛ مسئله‌ای که رؤسای جمهور پیشین باید سال‌ها پیش به آن رسیدگی می‌کردند!»
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68658" target="_blank">📅 20:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68657">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jg5I8i4NNhPg4yHln247gH5xsICBRE6gXRCn3TFvk-zlCQcpFwQT7eTdlrcoSZeRtWpSUziGErK1a8j2M1b17q3ki95igQ4c7dTqyT9DgDvUGNGih6v4tj-bDJbIAODWTLh3ikoK6tzO1hWG2flby_slcv1mgZIm2pr-FFLzwyC85kOy4yOQoMpisyWo-6gsM9R4AztzZSUPsFCIsz0olD7R3fk4NAaJghaZhCL2QDNGoR7-XXRxeFtAON1WYLikK8nNlJqmGvJyp71dfabIaxn8WXjVjOY4eJhroK2FFhPOg-ZnR5WGPxHlocrgmAD9kYEUqqGyQpCR8Gk4vQ0U6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
هر بار که ایران یک سرباز آمریکایی را بکشد، بهای آن کشتار را چندین و چند برابر خواهد پرداخت! این دستور به وزیر دفاع، پیت هگسث، رئیس ستاد مشترک ارتش، دنیل کین، و تمامی فرماندهان نظامی ابلاغ شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68657" target="_blank">📅 20:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68655">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aOwSDJE1YEThgjgfI1DXH1p5DPd1RgEUK8b2gla786nAU0TtorEhsUuXRLBBLoBJN06U8SlJt33xFAqRNXVjHbxLnF_3F-6lC2dp22Z0tLoRnRcpAKFVRJXdEHzFP2CUl-MQLJzfb1yzJMJwRcvYK1hbc_AMLbTlJScZSKNNYwxJA2mIu5N7eNHkpmVCZpcw4Q4Mpx7HW76YSvRaF2-_bqmsV7wGETHmaeOgAOWxkYhVkQNDXDny5i6HKzWvPVorgFme2-ZCFh62C5hexerArhd8ZlVb-DIqYAkY93T7F9etnEZuvVXI0G1OMdHuBsvPOIB_7Ind_NntHYTXte73cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eHn-gV3oKA2q3jwZhHF2z8DMiNYQkVHdvP2KCk-2xmCsdSHpMsjK1UJwNOmuPCRH3oGZ0d72Z8UKoOh2Qxn-dPEme-cik9D2-xCRmFH0eKHSuUgnnoV31kC5YsOwFGaAhEmNjhZK44A_eoKarY-N90EeCBEd0nVcprQlj4v04Q8H1_BSGbirXXVK8_JLuJf1JwA9qA42fnDWyw6v3khSkDhaXab1bZbpFAYDXn-Xxe0CmG-0xrvB5FfA0uRtUU0CaStXsKfVhbagLX7lVWwwiPnKVmfpbE6ZGnk59FJbGfikStoez2GyCNYCGElHxrDegMFDryC0bUHPaFtsaG51ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
وزارت دفاع ایالات متحده هویت دو نظامی آمریکایی را که در حمله موشکی بالستیک ایران به پایگاه هوایی «موفق سلطی» در اردن کشته شدند، اعلام کرد.
تایلر جیمز فیهان، ۲۵ ساله، اهل هاوایی
ایزابلا گونزالس، ۱۹ ساله، اهل تگزاس
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68655" target="_blank">📅 20:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68654">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlXl66GnD1AmWL31zxWjAjSxUFTglNsVi-1jSMK2DEAtId4EnryKqiXS8HXnjNygHKKyWDYkLKTlhzdG3wgR_bVrTNcIwAFZhj2AGi76Ys-OkUxLO-B5-P0HQ8j9By7r14cc6HaSZEHvEiuhHZe_wm5AyymkR93h9A2Q1mKcGqWzmZ8rnTqY36wBwcOUew6w2MNwOznNEbkoCwz1NeL359eZiyDkTzR-l1XOF6XMuAAmDFpsydfU2Wqx5F1NcLw62NoFGhiRkUl4acj6LHZDd0SUZ_lPrsLyog7wnfBjrAhix3T29-puKXzkGe1mm8HRAdvekKE4-3pU-wJxnZoV9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امروز امتحان عربی یازدهم بوده، توی امتحان بخش ترجمه چی داده باشن خوبه؟
فَشِلَتْ خُطَّةُ الطُّلابِ لتأجيل الامتحان
ترجمه : نقشه دانش آموزان برای تعویق شکست خورد :))
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68654" target="_blank">📅 20:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68653">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
یک واحد صنعتی در حومه شهر خمین حوالی ساعت19 هدف حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68653" target="_blank">📅 19:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68651">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oyoj4QseY_LHiWpGD5DDEX6ZswxPL3_tqgY1s9LkT4SuPdFJR0sIU7GdmJy_YCAhhxEYHT7HRSypxWC0_FfEe6pIschVU7xdvEO0vmWlBU1MtOAnwPm_Mh5BjkQY2E8jOxPDJF_gmOlQS81m4yQuJoEEaExDbUL2q20JdG76Fmcdk3oWTptPmrTiqLGcRs1pdALqr5mDpU_Mkjq27XtvoY6aM9EyR2diyn4NlipGRGX5Y3wgyj1n-kEGEicd8hJ7bnjCpVV1PBZyKL67dFmhXPI9tSHEkmULrgtCWUKexWfjyXaHl8KNiZ3wG5a740WL7_yoREzz2CcKCrGLjyIL5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/246e0b466a.mp4?token=hSEeDsYtMawoAqikWCAbnlc6o9rWHBtAQOIUQIS_xO14QsyzqAv_FjnlyxPzzZNT6UmM1pzp8XFR11aRZbWCXosrymaRMGT1foP-bSQDCr2ImtOmYpY-GJ413pswBaWuw1kwu4lcpNrmfJnFbfBFai7ajYaEtAnt38fKmb2YRxKq02TCYBll-pLcsplqYJGpvTV7_NUvscK9EPbKV-XujS0cmDOTwl1Hsu4xdzlDVPoRf_FiQ6bWxQYYCbW1g8fK7K9mgkIEr6ub_aOrCM8mIaeQisPDvzcGDyC_m-ZtcZ5WpPDOmKns2zS38gyAmoVFldgNvVWh28lmA8Q6mJveEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/246e0b466a.mp4?token=hSEeDsYtMawoAqikWCAbnlc6o9rWHBtAQOIUQIS_xO14QsyzqAv_FjnlyxPzzZNT6UmM1pzp8XFR11aRZbWCXosrymaRMGT1foP-bSQDCr2ImtOmYpY-GJ413pswBaWuw1kwu4lcpNrmfJnFbfBFai7ajYaEtAnt38fKmb2YRxKq02TCYBll-pLcsplqYJGpvTV7_NUvscK9EPbKV-XujS0cmDOTwl1Hsu4xdzlDVPoRf_FiQ6bWxQYYCbW1g8fK7K9mgkIEr6ub_aOrCM8mIaeQisPDvzcGDyC_m-ZtcZ5WpPDOmKns2zS38gyAmoVFldgNvVWh28lmA8Q6mJveEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
دقایقی قبل شلیک موشک‌های بالستیک به سمت پایگاه های آمریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68651" target="_blank">📅 19:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68649">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toMc-BxPlg-OE14Q3iq7LNurZefevpqYc2wfjh-Y56j0aIvtdflrk3GsS0Ob57WqXeC1rmA2OKMt5UojCBzt8taROBVImWRIwN0v4znskFWH7fNTcTUKIGl10g-9ioIEC_DoFDUb0TQiSzXPzTf_BEzBHo5RGCA8wgghhwr-toDkxNUJnk_2o6G2COAMhiOKDML0kT4cImddVEnSo8enF9ynGG0-2a-hZ8Um6HdwEp8pc_t1U4mRYcRIo9ljOYa6_Py8gBGIoxtY_oA2pXMvYoMrJEEMNo0e2dK6D5pgXvuL5asKd-VZRn2DmjwuTBRi9j7rMrWGUabOT_6tDYEB9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e216a5ddb.mp4?token=AnZuu6kFMBjm8_IBishBqYy3nZdFd7fgpIbeFog5nEOxnU1OjnrT3DZIjfnywtlgl5MI73qRY31Mul3e32b5XyYjQK1GIaijiiogQHQ8OJxbWxtjS7H_hYFKPz6Jk4DPAEDlmA4UwXhBh_q_Q6H35jpfNpKkW6rzEOTcq5bJ18fUt2sBNJdVtImtg8mAGehaU8vMj6ZU5Ng7pPBP7sjDNF0NTbmN-QecFnOqPVomi2et7kYG4ZQqELJfFUzlvUrUHrRo-uZsXagnKFUuCI2IeO2sSji-63efVrRmNM5shfjBsPsJSmx86c9hk6gvq6T9t8FSMBXWDFIffoGx1EMd-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e216a5ddb.mp4?token=AnZuu6kFMBjm8_IBishBqYy3nZdFd7fgpIbeFog5nEOxnU1OjnrT3DZIjfnywtlgl5MI73qRY31Mul3e32b5XyYjQK1GIaijiiogQHQ8OJxbWxtjS7H_hYFKPz6Jk4DPAEDlmA4UwXhBh_q_Q6H35jpfNpKkW6rzEOTcq5bJ18fUt2sBNJdVtImtg8mAGehaU8vMj6ZU5Ng7pPBP7sjDNF0NTbmN-QecFnOqPVomi2et7kYG4ZQqELJfFUzlvUrUHrRo-uZsXagnKFUuCI2IeO2sSji-63efVrRmNM5shfjBsPsJSmx86c9hk6gvq6T9t8FSMBXWDFIffoGx1EMd-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آتش‌سوزی در یک تانکر نفتی در تنگه هرمز، پس از هدف قرار گرفتن آن توسط نیروی دریایی سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68649" target="_blank">📅 18:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68646">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bz0vYHbcSFIlfY7w2GqvC894o86zJjebt14pSA7di3mShziIugtF4zjpcbZ-5CQEqD1RqHUP1Z8FXVC5qB1-hoQU6GnkE34eZw0RKz1ZxBA_FXHQMFGXUK_VoXGDnKDDCTjf5OzqVpDrsY5ASupZwP2pQzzdbO1wQjcAbQwBMWVEuy7nytk-cAaydrjadjA7nTyO-KKsYa2kBAvBZbwJHreFBjUJkvpB01TX6ql5UEz0qxQh3Y57PZO0B2e-CI3sd0MIFbuHg4LiwBjyS5tRfwjuKIE31Fr3Q1RnpkEXeLnUpnjfz1daPvrFhfbmDzTu_DNKosHomva5Sf3Tv6Q6uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Aeo3Nk-8GNP3sw6vZ_SnxNPvv1hB7XjmcLAy-ZYoMrIdEaiZ8fQpuyvZhShZ6_leoABotXmbgvW8F-J-MKK7OTk2jB2Z0qH21mCnaJvx3i6jihh6C_bn5ITrMvM89Cg_8FNQHBinrPSKZ46DOGsVbtGImCJhnt7jAnBRK4GqjZt5JqxoLrpHov9IphuEboWC7KERiPT7hpE16pqXZjCyNqU2jrqgVyXCudjTvhT_7zEO_NtTl21AoKQrDlUn2iCR5VZQpkd4U9IGOIHo-w3v5wxihOH4AVE65QgPOaxauB1eMW9i0SdQVSmcAJRUYjb6Uye4LI4SKrW_v8ha6MG_PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jPRUJAdgtYqe4E57DpsoGSkOl6bi3K_tRqAk4HJAeLyqPc2GsL_qlxVes_YEdsUdRQjJ3qvavCSYCeWBru3NvtKe378WFuQreB_WuPcKRa3bc_gjZwNmkI_Ls8TBIKFc3-5-GDY4SAgXS3_Y8dNQH6QMwUEOqGTBWb2qnn0txy-1_E7Hkaf6tIZKCFTyNSeUAGy96ltj5nu3IMjh8vfIXY_kkZRADZ__vRbE7-9Ip1k1ILfv__f4x879lSHO1Z48od-JekoTkOpNJkfy8r7SkYFlBQvkqfzrfKOCaKoHBf9FZgvsi3H4iiX73v_nuHUTfPaP05J6Nf1aek30H-A7ZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
شلیک موشک از شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68646" target="_blank">📅 18:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68645">
<div class="tg-post-header">📌 پیام #1</div>
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
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68645" target="_blank">📅 18:50 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
