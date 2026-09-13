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
<img src="https://cdn4.telesco.pe/file/LienQdsnIEOBD34zlNN7AF5XR2I0bVQIfoTgnLx1Ve3Hl127ma6K9Xs9vCJNZEutkQuwzignQpdpMuqemmvud4IJdNmkyecKJ70fgV3vH3PZ008UOU5gGszotkFN--ZAZaR4twhvZTaXtkoZlddr8O3jmE5CKhWPOR79hUU_E6gWyHvExpSv7V3DuY6JzW0cldtS0HU4jcPaRciZ-Zkzll92Fl8-2Wf-lAn8NhFEh9x0mSXuBZnL3iT3KnT-NdC8tFUyl7GG7wk-Iu-iEoo_lgUOw5TlZBx7WHs48tvncXfrE5SfV7Sauo5jJGQXbgMvx5dEQhIhZRoAfum8zRkfNw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 109K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 03:18:25</div>
<hr>

<div class="tg-post" id="msg-71599">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71599" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/news_hut/71599" target="_blank">📅 01:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71598">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eX_l-ZFPkxBrv2OLqHAprvfHK9A785xpTTaLiGHVkjae6cWjelgE_NkYeuzGBKLE4R2zwc63293XfoLAlZrRfaW1YpaEBiFS6vEnKYtKpXEL8J7G75Q_7CvK0viMFoS2eeuU3ewPYGwgog4b0XOhBTMMfwfPfKE60xdRmAPR0F5tXnUOexSSIlgjCAMtRcbSyFoso4HY7eY_wLcH3Cii4pZxczPL0skIL5WCzkCKg7JIsMDhtvg_AtiXchyK-qWLkWYz4f1uagVZA93alxD75kLO4Oua9NSewjDO6yzrYUBzRUKfNFMDDTyHsT8di6GEdvgPtTGJvnNVqMAPOKpTUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/news_hut/71598" target="_blank">📅 01:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71597">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b94dc744f.mp4?token=kJpw0uwLlgTVoS9kTNrVRFQlLp_j5osdICSWtBFRdm5vLIF65Wr-p8Co64Q8tVpe41AsCzQrvV5lm06jJbeDlxWVN0S81_r1IUU-vE-qwMjXpCfILkfpTglprcQpmAWcHSb-F0UUN7hKLX6XQ_mrZ57TcUziM9HpkH9Oj1gomnVkXQSIk2LJSVjBTCInpKoT1Ex9MisBXAjxlhrXp29Q4mtvoKdnfGm2zuBogJ1Toprsw6KaJGl4DGSHJ0p4k3JMvxkXtT3DVcz1ynPM3KNXaNfFyL7AVL1rCts5xn2JA_x-a692V_fGraG3LPqGIYqGbID8PPGaA5lEfutr4OTlKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b94dc744f.mp4?token=kJpw0uwLlgTVoS9kTNrVRFQlLp_j5osdICSWtBFRdm5vLIF65Wr-p8Co64Q8tVpe41AsCzQrvV5lm06jJbeDlxWVN0S81_r1IUU-vE-qwMjXpCfILkfpTglprcQpmAWcHSb-F0UUN7hKLX6XQ_mrZ57TcUziM9HpkH9Oj1gomnVkXQSIk2LJSVjBTCInpKoT1Ex9MisBXAjxlhrXp29Q4mtvoKdnfGm2zuBogJ1Toprsw6KaJGl4DGSHJ0p4k3JMvxkXtT3DVcz1ynPM3KNXaNfFyL7AVL1rCts5xn2JA_x-a692V_fGraG3LPqGIYqGbID8PPGaA5lEfutr4OTlKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سپاه به طرف تنگه هرمز موشک شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/news_hut/71597" target="_blank">📅 01:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71596">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZisGzl6WolWFcsoCmKj-CkyjfABzleqXUFjmg6wXkIPxWAWkUcglpRLB8F3mU03YohXseR3GSZXOpLJnNiWoe0nVMhhqpCOxrLZzmDaOi2iLhvzpJ78ONRSymGttF-EOa0TyfQ8oHfLwio-zWcPJuSqMDmQ85onYwIlIaVQYsPH3XpfYh4MaG-TnK1f0ZoYbRVpIi3GfW0ZalQRVscZQgbDnQdC1Y5Rf2uyEev-A1AiAkxU5N1Hk7WqAhuE36PLFKOjC-m-RtUvdt9yxrHiwgQc_wc_DJIAxkiIirtMFyaztKpinS6EDBSPnuHhp82Peg4xCnsx6w2y0hyodKOOFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
❌
🇮🇷
🇴🇲
باراک راوید:
یک مقام حوزه خلیج فارس به من گفت که عربستان سعودی اصلاحاتی را در طرح پیشنهادی عمان و ایران در خصوص تنگه هرمز ارائه کرده است؛
زیرا نگران بود که عبارات پیشنهادی عملاً منجر به ایجاد وضعیت موجود جدیدی در این تنگه شود که برای این کشور یا سایر کشورهای عضو شورای همکاری خلیج فارس قابل قبول نباشد.
@News_Hut</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/news_hut/71596" target="_blank">📅 01:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71595">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c7311729.mp4?token=uO0fDWWirbbLOObcygoMgMmjiLIGM2UvfPIc6tQSBhu5rijtYzYGQbmwqY9qx8_b6HH69wAmpka1-0ub0tF9NSsR6UUBhxoxfHvGVSWqX0EHTld-r92EkkTxvrzP5DQwPhEtwMmaj2rRrM-DzzpQbWxxJ1EBW9GNZ9oJ2atFLrFOTk9SJEskjSFWRFCj7YCmYfRXZq0sTIc4WBU05gSEl6CsThx8D-mLkzB_0e-YyXdqfvcfWo4ug2hlO9vBhbuKWiuoqsX7FJeMdlv-qVCgxNmRppGGh4YjApqa4_Pc6KqQ7RVvQpUhYlJfbVWdCKOBBTakMqNcuIJtM_mX__P-9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c7311729.mp4?token=uO0fDWWirbbLOObcygoMgMmjiLIGM2UvfPIc6tQSBhu5rijtYzYGQbmwqY9qx8_b6HH69wAmpka1-0ub0tF9NSsR6UUBhxoxfHvGVSWqX0EHTld-r92EkkTxvrzP5DQwPhEtwMmaj2rRrM-DzzpQbWxxJ1EBW9GNZ9oJ2atFLrFOTk9SJEskjSFWRFCj7YCmYfRXZq0sTIc4WBU05gSEl6CsThx8D-mLkzB_0e-YyXdqfvcfWo4ug2hlO9vBhbuKWiuoqsX7FJeMdlv-qVCgxNmRppGGh4YjApqa4_Pc6KqQ7RVvQpUhYlJfbVWdCKOBBTakMqNcuIJtM_mX__P-9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
ایران می‌گوید دیشب به یکی از شناورهایش حمله شده است. آیا کار آمریکا بود؟
🇺🇸
ترامپ:
نمی‌خواهم بگویم.
@News_Hut</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/news_hut/71595" target="_blank">📅 00:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71594">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjXNAsNK9kIPlaPl3gUBcmD_mVLPQ7oM2Mf9TK_Yzf2kfLu18bIHZlOv4WEfq_ulZyTFzKmYvtsHcNMonpafmbowGfEkHIX85qmheh9LIhWqne0ndKI3EqTlxQl1ZtOtuEkjVXeVpZu5cGbNK5SMAWFzabaOjO4li_NBQ_jlJm5WhzD3c7iIi5tysF1Vi0IiddsDyR-vLE225njU1JE7fL_KuKjWiIjhtFythdlyC0iM-oSB66S-Q38ZOBHPYu0Yf7ArLXYJK6a0-H88O9VFkmrEbXYHi-fZcczxvGE3ToUXA_iWqtYUa4-7tbksiuFikGtKwomrHAg7rxJP9ZE-KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇴🇲
بدر‌البوسعیدی وزیر خارجه عمان:
در راستای دستیابی به اجماع، نشست منطقه‌ای که قرار بود فردا در صلاله برگزار شود، به تعویق افتاد.
ما همچنان به ترویج گفت‌وگویی که حامی ثبات و همکاری پایدار در منطقه ما باشد، متعهد هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/news_hut/71594" target="_blank">📅 00:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71593">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
⭕️
نشستی که قرار بود فردا در عمان میان ایران و کشورهای حوزه خلیج فارس درباره تنگه هرمز برگزار شود، به تعویق افتاده است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/news_hut/71593" target="_blank">📅 00:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71592">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNApwZOTfbbDc3PjGlVJjwwx0uZ0W02zSihDmF9muLlJLjTE5as5cmjF0PsSBljHF25fggq6k2VrdfqD8zKQ0_5N9OiqWtRH-5_Xi_9k9n6AL41ePm7i8ETKvVPEXHzVKvzezI8LKJxHAR7VgRW4A-kocdRKpmHx95KVmtZyPXIVsKby7nN5zuSJPFEWV0iHkeVKgmqgOizZ3yjT9wzxJcfiXWIk3CbiusZMwbFWHbG2EWJXO_FCQkGhtsjcFqnBO28sNVHrrJzvQYaaYg_kmh9QNSfzIYjgQywNv3vqh_wh7_UvsuT8MnK_yvkajkhoRDX9cDQi2N_aV4OwRDpR3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبت های عجیب پوریا بختیاری کارشناس اقتصادی در مصاحبه با علی ضیا درباره ابراهیم رئیسی:</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/71592" target="_blank">📅 00:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71591">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec76e7285d.mp4?token=cjiExMHjTu9v_Ow4uuD-wseKljyxaOc3-QQFpmxijo-XijzLnhJ8XZnwkCt6vwaF3a2012FledA1aCvUV4ebeedMx9s6pFe4rZTXA4eI_ujKEy_bLI6t6UE03o155Bd5xu2iAXtma7kyxtESjhKeP_LxjNGoOcJCTxvDAEJ6CWH3WRWg-w1VXXYA6P9Ndluh3fdxiRVMpoZ2213QJ91NPIeYVeIw3E5l-uVVD3g_aRUek2zHJGaxX7eLAnUe-cTGeXHRqOz4dNNVCpZzqxASJImT7jQZDXZeNBkzD6HCmbBEEL0H_CXc2-ZVg5QCspDOpRXr1G-A4WRIPVCiN6I7ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec76e7285d.mp4?token=cjiExMHjTu9v_Ow4uuD-wseKljyxaOc3-QQFpmxijo-XijzLnhJ8XZnwkCt6vwaF3a2012FledA1aCvUV4ebeedMx9s6pFe4rZTXA4eI_ujKEy_bLI6t6UE03o155Bd5xu2iAXtma7kyxtESjhKeP_LxjNGoOcJCTxvDAEJ6CWH3WRWg-w1VXXYA6P9Ndluh3fdxiRVMpoZ2213QJ91NPIeYVeIw3E5l-uVVD3g_aRUek2zHJGaxX7eLAnUe-cTGeXHRqOz4dNNVCpZzqxASJImT7jQZDXZeNBkzD6HCmbBEEL0H_CXc2-ZVg5QCspDOpRXr1G-A4WRIPVCiN6I7ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیو تبلیغاتی بانو سیدنی سویینی برای novig
😟
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/71591" target="_blank">📅 23:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71590">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1NIjOfYv9lsbi0I8685bK4-Mut3c9MtH5HiwSEpeD4WFHWzKujfHMuheYx7DLI_g_Q6_vcMoM_YgOSLG4vasFaJgRVazLezrtLdzB0A70pKJZIfG_ucI3Yb1ZDN-UCUwnfzcyi9NTodwnL9XPCo7B4LWRWDos1v0m_eqv7qcoDTHxD-9YUVP4M_T3r_MIfx8djRMmRM0yJvfMOBOwTuTxOkeodNNEodcY24CtWHbtocOa0YUFQnS-ibKsYrmZmMawDXUux1pLGnau-HlsyfSdVfalZI1r0qO0ZG8VA_4d4zDRm9dDU7IqHsvjZGOxKm5PxI3hYFgXgQGh_hmH64-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
🇺🇸
نیویورک‌تایمز:
مقامات ایرانی می‌گویند که رهبری این کشور طی هفته‌های اخیر بر سر دو راهبرد برای شکستن بن‌بست با ایالات متحده دچار اختلاف نظر بوده است: بازگشت به مذاکرات یا تشدید درگیری‌ها.
بر اساس طرح تشدید تنش، ایران حملات خود به اهداف آمریکایی - از جمله شناورهای نیروی دریایی و نیروهای نظامی ایالات متحده - را افزایش می‌دهد و هم‌زمان تلاش می‌کند با بالا بردن قیمت جهانی نفت، طرف مقابل را وادار به پایان دادن به محاصره دریایی کند؛ محاصره‌ای که تجارت ایران را فلج کرده و صادرات نفت این کشور را به صفر رسانده است.
ژنرال‌های تندرو، از جمله سرتیپ سید مجید موسوی (فرمانده نیروی هوافضای سپاه پاسداران)، طرح جنگی مفصلی را به شورای عالی امنیت ملی ارائه کردند. این طرح خواستار آن بود که ایران و گروه‌های هم‌پیمانش - به‌ویژه حوثی‌ها (انصارالله) در یمن و شبه‌نظامیان شیعه در عراق - دامنه حملات خود علیه نیروهای آمریکایی و زیرساخت‌های نفتی منطقه را گسترش دهند.
مسعود پزشکیان، رئیس‌جمهور، و محمدباقر قالیباف، رئیس مجلس، با این طرح مخالفت کردند و هشدار دادند که اجرای آن می‌تواند ایران را به جنگی بسیار گسترده‌تر بکشاند، موجب حملات هوایی سنگین‌تر آمریکا شود و بحران اقتصادی کشور را عمیق‌تر سازد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/71590" target="_blank">📅 23:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71589">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f02f69702f.mp4?token=jDfEKh9m9HTRYoF2BDxKJtMB54ibPocYUkmDlHr1NDTk3ZI4LFz7BR9TBMR-ytSREo8l1kLADsOwWO3X8R2cHEVo4hulKjlvhlBQmuLk3rRcNOtT-A12IfbgJfm5eM17HAF3KM8Yj5UeD2fcznqbOVN7qBhTHUfXa_XimdLrssN4bDDm5HxD83sCGb6jKXa94I_qt0D8rEQXMi_ireJdWQTTZParcVlmfSExhc8Xzxar_CCA8Qd81EeXzzqAr4zJdsdyyZtyVz0Qy87n_7LL5o3kisAIJuEbo6BR28Nlnt0QvK-lAPga1zbNDuxknBStDOZeteFCrng6DNXDXEJzTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f02f69702f.mp4?token=jDfEKh9m9HTRYoF2BDxKJtMB54ibPocYUkmDlHr1NDTk3ZI4LFz7BR9TBMR-ytSREo8l1kLADsOwWO3X8R2cHEVo4hulKjlvhlBQmuLk3rRcNOtT-A12IfbgJfm5eM17HAF3KM8Yj5UeD2fcznqbOVN7qBhTHUfXa_XimdLrssN4bDDm5HxD83sCGb6jKXa94I_qt0D8rEQXMi_ireJdWQTTZParcVlmfSExhc8Xzxar_CCA8Qd81EeXzzqAr4zJdsdyyZtyVz0Qy87n_7LL5o3kisAIJuEbo6BR28Nlnt0QvK-lAPga1zbNDuxknBStDOZeteFCrng6DNXDXEJzTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کشتی که امروز صبح در نزدیکی جزیره قشم در جنوب ایران مورد حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71589" target="_blank">📅 22:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71588">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18ae06116.mp4?token=ZJwog6IGxBtm_RmYqlyRAUQnPvOYb6VOSJ8VZAVFb8TC86wQ39esuVJehKspzki2q34ol5Txu93Do2ERa1lnp5cAGetKlz8wGW3P5Q_mYpw1fx-xQxIKCLNFs6DEzqfnL1uCgADFGtZnAdf3uw8QECVH9AKQ2zNb5BjeM7xz1GdZmQkT-ZEz8Plz2etyBuPTEQb5XGIACo7FUElu7-TtM5JXR-65smtQAmp0IOs0fud-SNZXrxa_dP15WxnmyACQ3yvDkT7Zb-kCCzZoxL0aUajF8wY7AaCnpLJLD1qn-eaivmS--A3KFq3Z0CGle9ddTN9EnN5gb-7NQgFJzIB4rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18ae06116.mp4?token=ZJwog6IGxBtm_RmYqlyRAUQnPvOYb6VOSJ8VZAVFb8TC86wQ39esuVJehKspzki2q34ol5Txu93Do2ERa1lnp5cAGetKlz8wGW3P5Q_mYpw1fx-xQxIKCLNFs6DEzqfnL1uCgADFGtZnAdf3uw8QECVH9AKQ2zNb5BjeM7xz1GdZmQkT-ZEz8Plz2etyBuPTEQb5XGIACo7FUElu7-TtM5JXR-65smtQAmp0IOs0fud-SNZXrxa_dP15WxnmyACQ3yvDkT7Zb-kCCzZoxL0aUajF8wY7AaCnpLJLD1qn-eaivmS--A3KFq3Z0CGle9ddTN9EnN5gb-7NQgFJzIB4rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
زهران ممدانی شهردار نیویورک :
قربانی اصلی حمله ۱۱ سپتامبر عمه‌ی من بود که بعد از اون اتفاق نمی‌تونست با امنیت از مترو استفاده کنه چون حجاب داشت
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71588" target="_blank">📅 21:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71587">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oU33dNlGbP51v2miujiTF48-CM1Jr9PCDavI1H-ol7rm-CGzQbzCLIncqrM1uCMyauEStvSv8d0hPfga_iA8306NxN8l3DGShGZvpDwWXWOsz-jlLHKG1Rh3MeGCYLO5u5ugiK2TgnesZc1V9V9uYg0s7vMTNEYPyQgdUziK5R8YphsNcxzCE-vuILKX4SwBlZ6eRJ8hALnQmHeTp0CF5Dly2GZOQC2dP35CtKDpwt-I2NwB3QKmGJzV01OFcW45CrFnIFBWxz5Ln7BYKZqOwZQmQrPfMBVquVaPfCiS3WoQ2Z7-xMJObo4WGAGVrnpiZp2J7TXQqvinhzkXfhMnlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧩
🎮
کنسول بازی ps5 pro به قیمت تقریبا ۳۰۰ میلیون تومان رسیده!
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71587" target="_blank">📅 21:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71586">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/643027f01a.mp4?token=PS5J1tYfKZFUDK6TOpPGi6ygaTvrbYDzWYDSwbdbidl2tZ3xJ0ZhsBRbFnvU6fvAihvtVhDO0XpMagclES3Q0_U_tHL_D-nt9xqNO6QehtkRQkFiEXN_j93LZVM28ZlHnScxecZSa8LGTAmxMfCRsBUq1ziaCNzHt1DERCIvSOc6K_hlejmQyi371GFAA_mQN7SHeeLdvoY40oZ1WsuX0tdf05EHy2G3uh8eQMN6P8HXXIuy38o-8W7aCfRJ1ZS75EmHNFzqGPxcxyve4vJpx4wRytxsAUsAbOA0RQNID0v8Jv-i4o1S4ZqZBauVAbHHi0tL0s02RKvxbWu4kGlGpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/643027f01a.mp4?token=PS5J1tYfKZFUDK6TOpPGi6ygaTvrbYDzWYDSwbdbidl2tZ3xJ0ZhsBRbFnvU6fvAihvtVhDO0XpMagclES3Q0_U_tHL_D-nt9xqNO6QehtkRQkFiEXN_j93LZVM28ZlHnScxecZSa8LGTAmxMfCRsBUq1ziaCNzHt1DERCIvSOc6K_hlejmQyi371GFAA_mQN7SHeeLdvoY40oZ1WsuX0tdf05EHy2G3uh8eQMN6P8HXXIuy38o-8W7aCfRJ1ZS75EmHNFzqGPxcxyve4vJpx4wRytxsAUsAbOA0RQNID0v8Jv-i4o1S4ZqZBauVAbHHi0tL0s02RKvxbWu4kGlGpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
مدیر سامانۀ هوشمند سوخت:
خودروهای نوشمارۀ بالای یک میلیارد تومان سهمیۀ ۱۵۰۰ و ۳۰۰۰ تومانی بنزین نمی‌گیرند!
این خودروها ماهانه ۱۱۰ لیتر بنزین ۱۰ هزار تومانی می‌گیرند
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71586" target="_blank">📅 20:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71585">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇷
اطلاعیه قرارگاه جانفدا:
از سه شنبه 24 شهریور ماه قراره هزار گردان مقاومت ملی تشکیل بدیم که شامل کسایی هست که جانفدا ثبت‌نام کردن.
قراره به این افراد آموزش نظامی و امدادی بدن تا اگه جنگ شد، فورا اعزام بشن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71585" target="_blank">📅 20:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71584">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c23e20e2.mp4?token=H2olKdCe_2KQ4-AZHoLMfQIXRfmbIM-7dU2tzN_8_kH_qWPcaqh_WTuCtKBu5diO2_wu1d_rZjHRriCh1pk2qtEHC1Bz-Uqss0SuZjuZRx3VIrXZe3-Wr-mB500qjMoCxJS_I3yPW3xksXy8Tf96zbR-C1SZBii1iucTvDfQIkSxe-TGkB6JaQU764ty5uxIol5SHhRCOBLhIWawDIw_9exruSUbKuLmc9eRVRdCPWYArKYjX5ZSIl6uhaqZWpQ_wYZBEwnwex8dhvtahQHA025QBg9nZKNug7nYwROl9-E7bRiAEDp_iNCrFDt0NWea-5zQcl2eVqmIpRLOWpkdJlmaJCtqTvC0Z_qxYfeLTt0kc8grmR_byiq-H568NrCBQcalyEwX1lI39j5EjcR5Qw1gcmfBGkOuDaO_gg2pJIVTol01wkSP2jLgbVv2a5YBUndbfUO3xsqsjpEBkHKMm2uC6V5a_gGljKiQkyb6AIX8yPA4pfbV4nui08x0gZz7fVXyzvGO0mXQeZ-VigAY8qS-rUgOJIgc_LQqVWmJzcdnP-mpYFV3--une1mSUxixscrAepXvzMOYY2JAXMF0S5kRK_Nll5dNK6FMCEtQ1KOQBE4HRDo5QOrZPcVQuPeKdewgn-ajhoWh-IrN9_4FCc-10C6XpZvh_yXWQLXWDWY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c23e20e2.mp4?token=H2olKdCe_2KQ4-AZHoLMfQIXRfmbIM-7dU2tzN_8_kH_qWPcaqh_WTuCtKBu5diO2_wu1d_rZjHRriCh1pk2qtEHC1Bz-Uqss0SuZjuZRx3VIrXZe3-Wr-mB500qjMoCxJS_I3yPW3xksXy8Tf96zbR-C1SZBii1iucTvDfQIkSxe-TGkB6JaQU764ty5uxIol5SHhRCOBLhIWawDIw_9exruSUbKuLmc9eRVRdCPWYArKYjX5ZSIl6uhaqZWpQ_wYZBEwnwex8dhvtahQHA025QBg9nZKNug7nYwROl9-E7bRiAEDp_iNCrFDt0NWea-5zQcl2eVqmIpRLOWpkdJlmaJCtqTvC0Z_qxYfeLTt0kc8grmR_byiq-H568NrCBQcalyEwX1lI39j5EjcR5Qw1gcmfBGkOuDaO_gg2pJIVTol01wkSP2jLgbVv2a5YBUndbfUO3xsqsjpEBkHKMm2uC6V5a_gGljKiQkyb6AIX8yPA4pfbV4nui08x0gZz7fVXyzvGO0mXQeZ-VigAY8qS-rUgOJIgc_LQqVWmJzcdnP-mpYFV3--une1mSUxixscrAepXvzMOYY2JAXMF0S5kRK_Nll5dNK6FMCEtQ1KOQBE4HRDo5QOrZPcVQuPeKdewgn-ajhoWh-IrN9_4FCc-10C6XpZvh_yXWQLXWDWY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی آموزشی برای دخترای موتور‌سوار چنل که قطعا بکارشون میاد
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71584" target="_blank">📅 19:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71582">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eC_YffYl7YpxqZumEU9JBiTNc0E6dAouzUDnHUC5zh4idOK7fpz8GgKRtoQJ0L1vzDD8BiziGOgm2T49YYwpTpENEZ_VowimJMawoE25nJYIn0exN1OG6eKML-vDIe1-7QYruM3IJWalHwDzGN5ioOfTJJubXUUPB6JKNbOjaCzg8LVBaaoIsRIWcsCpNNAiq5OWo1jL_RNVzJSMP4cWb-U_FcthYRBapUJrcKcZAwf1Pf37Haeop7lajdsobv5e1KwKV1Q7gqbnFCBL575DDz5oqDKeqsuULVTnzcMP7Y6LyY9EsuLuBz5vqCYp4svMDOZOkLh7M1yj40-QEcn_gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UElo5nWDxaMxr72-Ren3ZlHGIHJuxl6u8eQMhcNhT6mRFj1Flrw3f-tToZ4YGSL7Em8etwzD0fOue3bezXLte7Ayffx-T-YKhxKj7HpmNxLfjs5m9VlPoszJMBjTLh6viMkq16YhqhyJUkqNewnv6QfT_uiKwu4jd4ztsEebsFdBF6jwSyqtD-5mNruMOkKZcu9uqcR0OkK6eVuM9l7-rkRQ4_bX8YyAKQ9o16jCjAX7VnsD8JhRWTLRynhOyYgFGLCxPRgW-ITa7REl4QCiAbBSiJZ9IipAMZy-9F1KiO7VN_6howQHr6aw4k2vG3TdxiDYN1DOKwnov604TplAlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👑
دفتر شاهزاده رضا پهلوی:دستگاه کشتار و سرکوب جمهوری اسلامی بار دیگر قصد جان یک زن جوان را کرده است. سودا (مرضیه) ابراهیمی شمس‌آبادی، بلاگر ۳۳ ساله اهل بندرعباس، پس از ماه‌ها بازداشت و تحمل شکنجه، تنها به دلیل فعالیت رسانه‌ای، در بی‌دادگاه رژیم با مجازات اعدام روبه‌رو شده است.
صدای سودا باشیم و از همه ظرفیت‌ها برای فشار بین‌المللی جهت توقف ماشین کشتار رژیم استفاده کنیم.
سودا ۳۳سال دارد و ساکن بندرعباس است.
او در تاریخ ۹فروردین بازداشت و اکنون با اتهاماتی چون "عکسبرداری از فاصله دور محل اصابت یک موشک و ارسال این تصویر برای یک رسانه فارسی خارج از کشور" به اعدام محکوم شده است.
او حدود شش سال است که به بیماری ام‌اس مبتلاست و علاوه بر آن از بیماری‌های پسوریازیس، نارکولپسی و کولیک معده نیز رنج می‌برد و نمیتواند در زندان بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71582" target="_blank">📅 18:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71581">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBTcxO30-jySps5clEbAU_TuvgZk_PhtkNBRW1YBSRi8ZyCWAcmO87mAWSGyRIqR5WzATOsLwJ0Ux75RdXfqYKBNJoVXxY-o6HEjz_uUt4dJceB-3s_EsvabO7spgDqPeDsO-iRxBEHWJdcy4WR4ISwq0Z2ANJ6Ic36TMSw1DthnqbRI_PW4edlsGqjSTUn_wGNoHYjVJfk6iQ_4T9o0M5V-yslYhsc7mIpqDdx1ni06UBzvuQGyRiAa5pVykVzoi0J33S27q64hl3d7VVmESyLHQOft7yAsNoa6wa8VHYN8wzgp75ctohSNGK8Mqkdsllb-X9r8tK-CDM89GmnVFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇺🇸
نیویورک تایمز:به گفته مقامات ایرانی، تندروهای ایران با صدور دستور حمله به سه کشتی تجاری در تنگه هرمز در تاریخ ۷ ژوئیه، مخفیانه توافق صلح با ایالات متحده را که اوایل همان ماه حاصل شده بود، مختل کردند.
گزارش‌ها حاکی از آن است که مسعود پزشکیان، رئیس‌جمهور، احمد وحیدی و بخش عمده‌ای از رهبری ایران از این عملیات بی‌اطلاع بودند.
بازرسان رد این تصمیم را به جناحی مرتبط با حسین طائب — روحانی بانفوذ و رئیس پیشین اطلاعات سپاه که از همان ابتدا با این توافق مخالف بود — رساندند.
حملات ۷ ژوئیه منجر به حملات متقابل ایالات متحده در روز بعد و همچنین یک کشمکش قدرت بزرگ در داخل ایران شد.
تا ماه سپتامبر، ژنرال‌های تندرو دست بالا را پیدا کردند و به جای بازگشت به میز مذاکره، راهبرد تشدید حملات علیه نیروهای آمریکایی و زیرساخت‌های نفتی منطقه را پیش گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71581" target="_blank">📅 18:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71580">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71580" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/71580" target="_blank">📅 18:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71579">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpBsSZYGgB3XpIO_fvdHreTNYig7Y5MOBfmJ3mfKC55nyXDHDu9_pcWI0ht1B-1Q7aBjzUzhV3XAE_LBEUsHQIhnxfFEMVXepZ9xC180I8BI-iVosUc4nrqlclO_7eACFpamHDEx3VUFrmXm0G5OOgaVFsVJefMfmS9CFJoNSM54icmvseLCWaX8VtgY2HhwLhIlsM1Iil28h6gOAc4-lkYoYZq6EyEs3_mIs3HHa3aDrOH_UYeALtICHDNrPGkfH6TrGUr-fa_5C4JWO-Rx_u2o0rhO2nKdslg8rOvXJR3c45dHc9-qY79rnFWNPcw2GnVaxhgKtoWvoJttgjl95Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/71579" target="_blank">📅 18:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71578">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc5dc935e.mp4?token=pfXj8uA0IHH08RC-QaOj_EePZBAfz2rcAulnjhJc2KYJ6u-uMW3oiuBZCqZ39x02bhdQlYk6WWNDMEA3mJO08vZRpvmf9Sg00qePXkuWHTvsA-43WDTeoHX2Pgp2v24gvkeNcj3AhsepxZqClun0Vm_VHfmLb6XQMrUzXQfldIUWZtSkIYG-NTc6afIufXQgDDgy77Wf5IrKAU0bBochQaeo-D9nYHNNIm0CHIUPomLIAATD5WW3K7CzH0Nq563mxoNcjEWp5i7cRzxXHPh8BUrfc8yNnfLhgeuF2eYiwpCuUE-n8A2-WJqARx5SrHcVj9DvdEqr4yMI0jwcmZA1yUr6C4KCEBGpS3DnWUayAXQgjASD5TsDy5GuHPTjofeSprF570KTQXpjiiqNS3_9wqVJ0A18BqTel0IND5J-PkZnNzS_OhKd5MAtzqYJhTIyrNJY8Gw-5Ph86zEizuuZB8vJ8UTBZU-0P3zu0K4PlVSF4kF6ZkM78JTIpF2XGHg-_z7iCW_YokcinZdnDBBBkGQV1qbVVewIwKtWaT_tvnNkPsCaugxGH-ItcTojfQ4R_rTLyLzAK8Dxq70pTYgLnlER5WmcAh4Pzq_h-jJwevIbHNniYls4qG3TiIzKf4U9JohMWxrQOCiw5xTrv0fxXs4VbbqaGoGD6u4j15cbIpk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc5dc935e.mp4?token=pfXj8uA0IHH08RC-QaOj_EePZBAfz2rcAulnjhJc2KYJ6u-uMW3oiuBZCqZ39x02bhdQlYk6WWNDMEA3mJO08vZRpvmf9Sg00qePXkuWHTvsA-43WDTeoHX2Pgp2v24gvkeNcj3AhsepxZqClun0Vm_VHfmLb6XQMrUzXQfldIUWZtSkIYG-NTc6afIufXQgDDgy77Wf5IrKAU0bBochQaeo-D9nYHNNIm0CHIUPomLIAATD5WW3K7CzH0Nq563mxoNcjEWp5i7cRzxXHPh8BUrfc8yNnfLhgeuF2eYiwpCuUE-n8A2-WJqARx5SrHcVj9DvdEqr4yMI0jwcmZA1yUr6C4KCEBGpS3DnWUayAXQgjASD5TsDy5GuHPTjofeSprF570KTQXpjiiqNS3_9wqVJ0A18BqTel0IND5J-PkZnNzS_OhKd5MAtzqYJhTIyrNJY8Gw-5Ph86zEizuuZB8vJ8UTBZU-0P3zu0K4PlVSF4kF6ZkM78JTIpF2XGHg-_z7iCW_YokcinZdnDBBBkGQV1qbVVewIwKtWaT_tvnNkPsCaugxGH-ItcTojfQ4R_rTLyLzAK8Dxq70pTYgLnlER5WmcAh4Pzq_h-jJwevIbHNniYls4qG3TiIzKf4U9JohMWxrQOCiw5xTrv0fxXs4VbbqaGoGD6u4j15cbIpk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ایران به‌شدت خواهان توافق است.
آن‌ها مدام تماس می‌گیرند. می‌خواهند توافق کنند. اما باید توافق درستی باشد؛
من تن به توافقی که خوب نباشد، نخواهم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/71578" target="_blank">📅 17:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71577">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f46b70464e.mp4?token=SeALfdY0WLwvRu5QZsvo-nM_eqMLLCWPbBPVgSf8Fr5mZ2gICZBmx0LED-LBfw9CdETZth2lK2bINai04aQghd366G7dwL_e2-jYjztxXsM3UgO3suFO_C-Zyh_WfptOegYk_FGNZO131WnCyhyFgCpqnCVNNAy2gf8iAT2zeLNOjYcyIwCU_fCnqOoF6grRcR4MIwf0s4npFSTAeaped3Y3wKf1FfRxJO1g8LZH_aYnLs9dTy2tI_woW2y1BHnJxq3qX36cZFWpXLWJzKVO4LN-40UpoIiM5m1dClPg_VD9DKyKjE37_T9bEYHKcYI3Ey6yVvCXfsnNgqHhkdKIuFJLSqIAqR35p5OKOOiFNMvyzwmv2PepDAf1JXfmnaK_M2aMuHsF4wqu16AKzxaj8FXbGTj0WtbpqUCQEG9Xi7upUPbE5Fl9_vRLecyI6X2Zcp_OhkPCfWh6CKQSUquT9w82qK9cQQN3nWG1MVrnBn1Zn99xUNxQHFzKGfp65UJvSuUwteDrjQmho3T5bKzSnQrfqMHY_Skwk04q5Xua4kQay6v4W0H_HIhXDYASMHKeoz8Tnpy7nfLF4ABUfeQjLtEj6odPwrNL8tfrrk2cf_-2mlWXBrRb8cDwTjMveVAD84Cb050Us8r8Nr7ZNaVri9I3r96M7uBNgeHrtxAS83U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f46b70464e.mp4?token=SeALfdY0WLwvRu5QZsvo-nM_eqMLLCWPbBPVgSf8Fr5mZ2gICZBmx0LED-LBfw9CdETZth2lK2bINai04aQghd366G7dwL_e2-jYjztxXsM3UgO3suFO_C-Zyh_WfptOegYk_FGNZO131WnCyhyFgCpqnCVNNAy2gf8iAT2zeLNOjYcyIwCU_fCnqOoF6grRcR4MIwf0s4npFSTAeaped3Y3wKf1FfRxJO1g8LZH_aYnLs9dTy2tI_woW2y1BHnJxq3qX36cZFWpXLWJzKVO4LN-40UpoIiM5m1dClPg_VD9DKyKjE37_T9bEYHKcYI3Ey6yVvCXfsnNgqHhkdKIuFJLSqIAqR35p5OKOOiFNMvyzwmv2PepDAf1JXfmnaK_M2aMuHsF4wqu16AKzxaj8FXbGTj0WtbpqUCQEG9Xi7upUPbE5Fl9_vRLecyI6X2Zcp_OhkPCfWh6CKQSUquT9w82qK9cQQN3nWG1MVrnBn1Zn99xUNxQHFzKGfp65UJvSuUwteDrjQmho3T5bKzSnQrfqMHY_Skwk04q5Xua4kQay6v4W0H_HIhXDYASMHKeoz8Tnpy7nfLF4ABUfeQjLtEj6odPwrNL8tfrrk2cf_-2mlWXBrRb8cDwTjMveVAD84Cb050Us8r8Nr7ZNaVri9I3r96M7uBNgeHrtxAS83U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ماجرای ایران درست بعد از انتخابات میان‌دوره‌ای تمام می‌شود؛ شاید هم قبل از آن، اما قطعاً بلافاصله پس از انتخابات میان‌دوره‌ای پایان می‌یابد.
قیمت بنزین به‌شدت سقوط خواهد کرد،خب، من می‌دانستم چه کار می‌کنم و باید آن کار را انجام می‌دادم.
ایران نباید به سلاح هسته‌ای دست پیدا کند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/71577" target="_blank">📅 17:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71576">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a78bb4d113.mp4?token=pyt6aAvfXKlP9U2vTLnCPl5uvPKeSWGKgQAcO2sTAUSseQ3AMqIFii449FGIWcJj33w4_zns0nrDpo1gAyOWrDKmXpOswJeLvCufXAwkCPKpYiyxeWPYlm1HUI3s-T9CAK5uzZ2wX7n1gG1bf_Y7c2Amswg_YniTLvKaFoOARIFmHFM6DiT8Jdd_IsqESqCz8N0iAnmgtoSDSne-gMq5QUIL_EYEOmiNPlEFdBDZEQsQ9xMOnMH7h9z0oIjA07zJcReyZdLfCDppBAsvSlqraZvuVz266ymO_7fudEJlwksPW6N310V-jaMli69SCXSswRD-X36ixX80PHW-N-gBNDXPHnGZV4HldoQ42YL5qxv_9Etk23UTpaV-J_jzBH4uIgSYPf_GaFrA1SLdMHJ4rUjYsZny6yIHnB7Z4JWmfBU3zHR35vQNm5mJBO2YTFUAOtEE-rtEUfxDgrCt90o7ignmuQZj2ps4QewNQpTBYM0sVn81ifdcPn95FjxgZV7hbvumpv8vyDpQ0OewP3KDCQv9yvM8en7j3hlUY774axoC2fsa-C6w-zvgy2tbVccnR2Px9N0mecEwUopVqpUOT4DSPQM36nmr_P2bv_kcVaFJ5dBSt7LprHP0zLR3t9ClJel2C6WsUkKMirt-27LkBs37XD4uIDNTRIjzFaOIdjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a78bb4d113.mp4?token=pyt6aAvfXKlP9U2vTLnCPl5uvPKeSWGKgQAcO2sTAUSseQ3AMqIFii449FGIWcJj33w4_zns0nrDpo1gAyOWrDKmXpOswJeLvCufXAwkCPKpYiyxeWPYlm1HUI3s-T9CAK5uzZ2wX7n1gG1bf_Y7c2Amswg_YniTLvKaFoOARIFmHFM6DiT8Jdd_IsqESqCz8N0iAnmgtoSDSne-gMq5QUIL_EYEOmiNPlEFdBDZEQsQ9xMOnMH7h9z0oIjA07zJcReyZdLfCDppBAsvSlqraZvuVz266ymO_7fudEJlwksPW6N310V-jaMli69SCXSswRD-X36ixX80PHW-N-gBNDXPHnGZV4HldoQ42YL5qxv_9Etk23UTpaV-J_jzBH4uIgSYPf_GaFrA1SLdMHJ4rUjYsZny6yIHnB7Z4JWmfBU3zHR35vQNm5mJBO2YTFUAOtEE-rtEUfxDgrCt90o7ignmuQZj2ps4QewNQpTBYM0sVn81ifdcPn95FjxgZV7hbvumpv8vyDpQ0OewP3KDCQv9yvM8en7j3hlUY774axoC2fsa-C6w-zvgy2tbVccnR2Px9N0mecEwUopVqpUOT4DSPQM36nmr_P2bv_kcVaFJ5dBSt7LprHP0zLR3t9ClJel2C6WsUkKMirt-27LkBs37XD4uIDNTRIjzFaOIdjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آقای رئیس‌جمهور، آیا فکر می‌کنید کنگره باید آن ۵۰۰۰ دلار را تصویب کند؟
🇺🇸
ترامپ:
همان‌طور که گفتم، نمی‌دانم اگر جمهوری‌خواهان پیروز شوند، انجام این کار چقدر آسان خواهد بود.
صحبت از ۵۰۰۰ دلار برای تمام بزرگسالان کشور است و ما به‌راحتی از پسِ آن برمی‌آییم، چون درآمدهای کلانی داریم؛
وضعیت ما هرگز تا این حد عالی نبوده است. دموکرات‌ها نمی‌توانند چنین وعده‌ای بدهند، چون در آن صورت اوضاع بلافاصله به هم می‌ریزد و نابود می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/71576" target="_blank">📅 17:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71575">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2f2319501.mp4?token=b1WnO7FW_LxLArs-4VRZ0WoDXVj4QzOdQa4iJvFQBHEsgtAftkhuojjCV9Fc66bygnJW1juPHQMuPCfIo8QaRQJBpAtfTBOXzS5NQzOaA-jnlaHVIwwAmErZm7zixVTOBGJLmAY8fcgTWfwa_7GLN6IHV68J7iUSJlaukSabe6RLHIwbunMQQ25ZQ5P2iTJnNQvC9maRjU_83w1MaTMbAwoqHZIagqOlylUbCP2NOHfruKaWggq0RBwXJKLJ19n9RJ3kgFkV_iS7_7_EBWkOSeD_EzNij_1kv7EG2iSH_1WEopOQdmATl16igHca7aATlExXLbplBFvgUD4QQ1Na5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2f2319501.mp4?token=b1WnO7FW_LxLArs-4VRZ0WoDXVj4QzOdQa4iJvFQBHEsgtAftkhuojjCV9Fc66bygnJW1juPHQMuPCfIo8QaRQJBpAtfTBOXzS5NQzOaA-jnlaHVIwwAmErZm7zixVTOBGJLmAY8fcgTWfwa_7GLN6IHV68J7iUSJlaukSabe6RLHIwbunMQQ25ZQ5P2iTJnNQvC9maRjU_83w1MaTMbAwoqHZIagqOlylUbCP2NOHfruKaWggq0RBwXJKLJ19n9RJ3kgFkV_iS7_7_EBWkOSeD_EzNij_1kv7EG2iSH_1WEopOQdmATl16igHca7aATlExXLbplBFvgUD4QQ1Na5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
نظر شما درباره دیدار کشورهای حوزه خلیج فارس با ایران چیست؟
🇺🇸
ترامپ:
برایم اهمیتی ندارد. این به خودشان مربوط است. اشکالی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/71575" target="_blank">📅 17:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71574">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e5ba3545.mp4?token=kX-C7NkAMrocq_KexHQc9lLvPPGTwWneUxXs6AIGVxt1TDZkTNzLKt8jrS44bme6XDQPgIQ17xLl_izX8S3S2nI_WeMsmqddXor_VGx6yO9cELBuzR9EjOEf7IzG0IWxjJ_083hoRwdn2mdCSPOOvf1bST3bui-BNjdGSUBXvaGdNKI4Z0AbTHT90k_6gg0-wnfNOMO_F9-a4079qX4DZv9XyqOq_dt1NwLYiJRbE-cmeAlK9_-TZo_2B4RlvbENniX8HqPe3Q35A-0E-Iz8Qgvwq_-LL393BTsds2T12lkX_fg4pqp-iaadZg62GBg77lv-zc15MbJGBHdmkmkFWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e5ba3545.mp4?token=kX-C7NkAMrocq_KexHQc9lLvPPGTwWneUxXs6AIGVxt1TDZkTNzLKt8jrS44bme6XDQPgIQ17xLl_izX8S3S2nI_WeMsmqddXor_VGx6yO9cELBuzR9EjOEf7IzG0IWxjJ_083hoRwdn2mdCSPOOvf1bST3bui-BNjdGSUBXvaGdNKI4Z0AbTHT90k_6gg0-wnfNOMO_F9-a4079qX4DZv9XyqOq_dt1NwLYiJRbE-cmeAlK9_-TZo_2B4RlvbENniX8HqPe3Q35A-0E-Iz8Qgvwq_-LL393BTsds2T12lkX_fg4pqp-iaadZg62GBg77lv-zc15MbJGBHdmkmkFWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
در نهایت ما آنجا را ترک خواهیم کرد، مگر اینکه تصمیم بگیریم بمانیم و نفت را برای خود نگه داریم؛ درست مثل ونزوئلا.
دیگر درباره ونزوئلا حرفی نمی‌زنید، مگر نه؟ خوب به این موضوع فکر کنید: میلیاردها و میلیاردها و میلیاردها دلار.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71574" target="_blank">📅 17:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71573">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇾🇪
حوثی‌های یمن تصاویر مفصلی از عملیات نظامی جدید خود با عنوان «و خداوند از نظر قدرت و کیفر، سخت‌گیرتر است» منتشر کردند؛ ویدئویی که صحنه‌های نبرد در جریان تهاجم اخیر آن‌ها در ساحل غربی را به تصویر می‌کشد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/71573" target="_blank">📅 17:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71572">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9fa2fdcc9.mp4?token=Cb0SvG0p46YvokreNG8a57p6LnQDo7fMsHqOEH5k-85NLTb0sYn40_rIJxHRtaLsCIXpStBqpE447ouNKPEGGnSuSUGnwYZamFAV3YnR4DRGATDuXvMlGN5hkj4MMfXvjHMnr0fN6w5wACvRiZ_7HomfrvjdLrCLJZXXpBxzrgR0Yn0sZuAITXjoXNEOacYzKAUpqlVI5GsSfMr5Oyb6qxgZyVQR7AEdaUKmxl2ZFiKORJ5OJQrpxHqfsLiv9CfHhZQ9JyzWO6jc8PpB3d_iXjXAYFu7vQLAj817hb5IogL9aUTUxRtyT1EShaVrRMNkZK7LTeZ1Agsy7tMc92Wuww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9fa2fdcc9.mp4?token=Cb0SvG0p46YvokreNG8a57p6LnQDo7fMsHqOEH5k-85NLTb0sYn40_rIJxHRtaLsCIXpStBqpE447ouNKPEGGnSuSUGnwYZamFAV3YnR4DRGATDuXvMlGN5hkj4MMfXvjHMnr0fN6w5wACvRiZ_7HomfrvjdLrCLJZXXpBxzrgR0Yn0sZuAITXjoXNEOacYzKAUpqlVI5GsSfMr5Oyb6qxgZyVQR7AEdaUKmxl2ZFiKORJ5OJQrpxHqfsLiv9CfHhZQ9JyzWO6jc8PpB3d_iXjXAYFu7vQLAj817hb5IogL9aUTUxRtyT1EShaVrRMNkZK7LTeZ1Agsy7tMc92Wuww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی مملکت یه سری کارگاه آموزشی گذاشتن و به افراد بالای 60 سال آموزش میدن که چطوری اسنپ بگیرن.
هزینه شرکت تو این کارگاه بین ۱ـ۲ میلیونه.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71572" target="_blank">📅 16:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71571">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cc03db8a0.mp4?token=a8AB7E8K5HM-KZbCWlkiK-T-VEKFOhVjVnVfy-vyN3Z_5cdqw7PoUuzhgAL_jBul5iqbX6CgDn40m_P9_oIZVQ9kyN0uoCntPdJ0v3WQ7VQ8XzTHHtLXx3lP_jye1uWim5y7X5AMEEN4Go7mbuPuXu1kH3gOf5ng0A-CPGrU_ec-mueSvtKSjdTKMKyoKqioH2iTvG-dzBEkldx1PUp2G9zJ0mv6DAbxFBH5PjXQgEGmVX1iE7rvngkM8gq-UtXWK9942L8iOpOhqFmtyXGy8IT5hj3zfMhB-fUFpT7MdOwsEaNygQuaZ3ER_qwPiwAAjQuEkPmh8BMO36lydaA8QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cc03db8a0.mp4?token=a8AB7E8K5HM-KZbCWlkiK-T-VEKFOhVjVnVfy-vyN3Z_5cdqw7PoUuzhgAL_jBul5iqbX6CgDn40m_P9_oIZVQ9kyN0uoCntPdJ0v3WQ7VQ8XzTHHtLXx3lP_jye1uWim5y7X5AMEEN4Go7mbuPuXu1kH3gOf5ng0A-CPGrU_ec-mueSvtKSjdTKMKyoKqioH2iTvG-dzBEkldx1PUp2G9zJ0mv6DAbxFBH5PjXQgEGmVX1iE7rvngkM8gq-UtXWK9942L8iOpOhqFmtyXGy8IT5hj3zfMhB-fUFpT7MdOwsEaNygQuaZ3ER_qwPiwAAjQuEkPmh8BMO36lydaA8QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
ویدیویی جالب از یک پهپاد اوکراینی که به سمت یک کشتی روسی در حال حرکته و یه بالگرد روسی تلاش می‌کنه اونو بزنه ولی، این پهباد در نهایت خودشو به کشتی میرسونه و منفجرش میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71571" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71570">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31fa8bd2c9.mp4?token=dO6z-tE9xhCp5OGePrI0RLOFQgjCHUGRdmB6vUYlOohjdqDxbU88aBlru01toNithPLjFbgavXSL19hpSs28TYjFv_pGwHrcGD5GxVXV1yNSi3iV32Yc-EP2P67wUXvXIPjzd4JOTPZQZA_R9p-OL58-6RRL41NkNct_wTiyJR-1Zsj2UWWffzzCCqp8LEvTN-67fCRi4HoB8_PyhTOnx48k1G1NjsoF2rO5oI96t3DNwe-njOjZCBzNRBRC647u8_1Dp79ox40_zm2x5GiPaxQG1oXfvaPAb8Ph9EcrLQjWuJQS98Sa2SFTKKzlqSgAb8DNZpCsyJXeDX28upGpgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31fa8bd2c9.mp4?token=dO6z-tE9xhCp5OGePrI0RLOFQgjCHUGRdmB6vUYlOohjdqDxbU88aBlru01toNithPLjFbgavXSL19hpSs28TYjFv_pGwHrcGD5GxVXV1yNSi3iV32Yc-EP2P67wUXvXIPjzd4JOTPZQZA_R9p-OL58-6RRL41NkNct_wTiyJR-1Zsj2UWWffzzCCqp8LEvTN-67fCRi4HoB8_PyhTOnx48k1G1NjsoF2rO5oI96t3DNwe-njOjZCBzNRBRC647u8_1Dp79ox40_zm2x5GiPaxQG1oXfvaPAb8Ph9EcrLQjWuJQS98Sa2SFTKKzlqSgAb8DNZpCsyJXeDX28upGpgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری صداوسیما:
از جنگ تحمیلی دوم حدود ۱۵ ماه اینا هست میگذره دیگه
مقامات صهیونیستی و امریکایی پر تکرار گفته ان که با حمله به ایران ظهور مهدی موعود رو به عقب انداختیم
دلیل اصلی بمباران تاسیسات هسته‌ای ایران به عقب انداختن ظهور بود
اونا نگاهشون آخرالزمانی هستش
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71570" target="_blank">📅 15:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71569">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d522fc2430.mp4?token=cAAEdZTFPJ4vICtfg278BLKLUEiA2UKp8i6XH491KBwFqdz4ZYiTge7qcqHxqFKDMnDi3w96Mw_w1GN7n-I2FjDvzaQpZsz3Ur9gpM336yd-cNU8uwl1gLBWjqZBeBkaYCLtDZ7v7kv7Hj98bmMHznvyt4G6w20WjhDRmFzuSJe6dpjXicMq_0OA56-EgpSuEjAXvx0D2pHvHLn9hWoWnKeyFVFRs-DG7Slv0lsA08LnrrxiDAKgdhrj0qGXPVgHkAJQG-t2VLccUuD6HnNfQDMLnb33yYCXoszAnjeO0bZT8lrSS0fg4oX0vYLcDaXBscDls0oQeRHtK0Bmm0D4RzSDinXB2rXae08HrWUoHH4Un70GtuSWwd5rla5yd6O1sQ_Q2vBzzr-bour1jJ-yI8GSpLxQwByB9H0f4YiLVDW77SHYeUknAlS_8eHkqAA6IixrOJVMyPhRyI-AkXEksbY4_mxp-DRzSfEyYaFtYLCwZFDvojlmlMXUydijlwzV9O8JnvK650wtCpiR1_zBZB3-n-JGbqczhDp-ZKVCodqAJ9NiivironV9cIPtrjNTxY7JOM2-h8cHhUTP5dJL_iE_Q8O0EO7wGfT7m4Qg2bIFhxl-8Tu9HarM32-Nbh_6lXyw_GaJnViNA-pLDz-SDRAdT4Q2ZXkbiVxfbCDR1og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d522fc2430.mp4?token=cAAEdZTFPJ4vICtfg278BLKLUEiA2UKp8i6XH491KBwFqdz4ZYiTge7qcqHxqFKDMnDi3w96Mw_w1GN7n-I2FjDvzaQpZsz3Ur9gpM336yd-cNU8uwl1gLBWjqZBeBkaYCLtDZ7v7kv7Hj98bmMHznvyt4G6w20WjhDRmFzuSJe6dpjXicMq_0OA56-EgpSuEjAXvx0D2pHvHLn9hWoWnKeyFVFRs-DG7Slv0lsA08LnrrxiDAKgdhrj0qGXPVgHkAJQG-t2VLccUuD6HnNfQDMLnb33yYCXoszAnjeO0bZT8lrSS0fg4oX0vYLcDaXBscDls0oQeRHtK0Bmm0D4RzSDinXB2rXae08HrWUoHH4Un70GtuSWwd5rla5yd6O1sQ_Q2vBzzr-bour1jJ-yI8GSpLxQwByB9H0f4YiLVDW77SHYeUknAlS_8eHkqAA6IixrOJVMyPhRyI-AkXEksbY4_mxp-DRzSfEyYaFtYLCwZFDvojlmlMXUydijlwzV9O8JnvK650wtCpiR1_zBZB3-n-JGbqczhDp-ZKVCodqAJ9NiivironV9cIPtrjNTxY7JOM2-h8cHhUTP5dJL_iE_Q8O0EO7wGfT7m4Qg2bIFhxl-8Tu9HarM32-Nbh_6lXyw_GaJnViNA-pLDz-SDRAdT4Q2ZXkbiVxfbCDR1og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇾🇪
تصاویر بسیج قبایل حوثی، ستون‌های طویلی از خودروهای تویوتا (تکنیکال) مجهز به سلاح را در بیابان به نمایش می‌گذارد؛ تصویری که نماد کلاسیک جنگ یمن است.
قبایل «بنی‌حشیش» برای پیشروی به سوی «مأرب» — آخرین پایگاه عمده دولت در شمال — اعلام آمادگی کرده‌اند.
وانت‌های تویوتا مجهز به سلاح، همچنان ستون فقرات نیروی زمینی حوثی‌ها را تشکیل می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71569" target="_blank">📅 14:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71568">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRCZJIJuQWtzaUxPAoL_6TT8UqFzw9B-EEvM19uEXfeEDkWc6E2ty_joRTlcX2YYNYsVAoMfZuLedG3BIRLFKphQlfjx9NjmwgAGIgNT5jjesjmFBVZnQ4aCX79YODsjO2BJd0Yw1goqYiofoK_WwUmVSp-Bog_OEIMHe83XbiZSnmMKqcTHywa3SjF53gozJGVONOc4oV3yde9C7GnzDY77cSWCK-tz1jb0qgdid638H5xRTMRJDdDsoCJeXGkao-ds2Q_E4jp1twGEGzsB0lawMSjxMUd6cGEf-CguQ98yCHQWkKpcJoXPX_P1dSXu4OCQr-VoU4kGALpMHa1HrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
📰
اکسیوس: محمد بن سلمان، ولیعهد عربستان سعودی، روز پنج‌شنبه دو بار با دونالد ترامپ، رئیس‌جمهور آمریکا، تماس گرفت و از ایالات متحده خواست تا هم‌زمان با پیشروی حوثی‌ها به سوی یک نقطه راهبردی و حیاتی در دریای سرخ، به آن‌ها حمله کند.
ترامپ این درخواست را نپذیرفت و مقامات آمریکایی اعلام کردند که در حال حاضر هیچ برنامه‌ای برای مداخله مستقیم علیه حوثی‌ها وجود ندارد.
دریاسالار کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، نیز روز پنج‌شنبه برای هماهنگی‌های اضطراری به ریاض سفر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71568" target="_blank">📅 14:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71567">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363bcb9915.mp4?token=eHcCaHwzZNauaXrVghd8dA7RhBYdmqssfex8Z6vYxWQkwsw3B-yLcFNNYR6K4w5U2ImFxMir8I8VqrFdkvkD-p3sh7h1V2Pnhp1H0iFGvC50GRJY-mEEhbrib_e_VqSN3xyX6APmvpPNzhq7MFXPAqIrQ12oomnPTNgO3hgw1R974Z9Ap8XkJecp87hlEkjgdEXIY4MUkxGtMkVoEzcEaqB9N6YzCLIDUKLPr6pRAAZo1IDscceyBWFQ2tOnDazFtBDR1OJ0xztumBb2d9uIM5VTts_nF7tIpXPFAbJnjmoEVxQQv2Sm98__F-l8Rhxxd1c2yt7TWjNp_E4pz8mWoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363bcb9915.mp4?token=eHcCaHwzZNauaXrVghd8dA7RhBYdmqssfex8Z6vYxWQkwsw3B-yLcFNNYR6K4w5U2ImFxMir8I8VqrFdkvkD-p3sh7h1V2Pnhp1H0iFGvC50GRJY-mEEhbrib_e_VqSN3xyX6APmvpPNzhq7MFXPAqIrQ12oomnPTNgO3hgw1R974Z9Ap8XkJecp87hlEkjgdEXIY4MUkxGtMkVoEzcEaqB9N6YzCLIDUKLPr6pRAAZo1IDscceyBWFQ2tOnDazFtBDR1OJ0xztumBb2d9uIM5VTts_nF7tIpXPFAbJnjmoEVxQQv2Sm98__F-l8Rhxxd1c2yt7TWjNp_E4pz8mWoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کنعانی مقدم:
اگر رهبری اجازه دهند، ظرف ۲۴ ساعت از سلاح هسته‌ای استفاده خواهیم کرد
خرید فیوز هسته‌ای از کره شمالی، کار خیلی ساده‌ای است و ۵۰ تا فیوز می‌توانیم بخریم
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71567" target="_blank">📅 13:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71566">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f67e4c7321.mp4?token=FpEz2KlcDx4aOYNDPxxupO766khFO5uHKRD0wBPsFwOPkmfP0ZjMsavNHhut1E9yIRrHTHHUDV59oV6FixV3Ig_NmBl-dChUAcVgHU_mEL-XV9BxD2cp9YPdw4C-RE1fC2onGUQ2TZgJEZmmwD4kpfs1S_0xaOM8YxSEynB8dMQSe82z0AlPRyZ8vo25xpC83B5Kc9hLNONGR5Fs5bNvo4-2SSKchFG7JrjEYMRyTXaEQr7iScizIuivj3kfrz9kgdDzBB5B7DyHQiviMXPBZisWCZwkkl5EE09evw9HGStah9bYI0IcE90U3vGDWY98NY_8v1iz4gEzWYl4ST_dvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f67e4c7321.mp4?token=FpEz2KlcDx4aOYNDPxxupO766khFO5uHKRD0wBPsFwOPkmfP0ZjMsavNHhut1E9yIRrHTHHUDV59oV6FixV3Ig_NmBl-dChUAcVgHU_mEL-XV9BxD2cp9YPdw4C-RE1fC2onGUQ2TZgJEZmmwD4kpfs1S_0xaOM8YxSEynB8dMQSe82z0AlPRyZ8vo25xpC83B5Kc9hLNONGR5Fs5bNvo4-2SSKchFG7JrjEYMRyTXaEQr7iScizIuivj3kfrz9kgdDzBB5B7DyHQiviMXPBZisWCZwkkl5EE09evw9HGStah9bYI0IcE90U3vGDWY98NY_8v1iz4gEzWYl4ST_dvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎯
ویدیویی از هدف قرار گرفتن نیروهای انصارالله توسط نیروی اسنایپر مورد حمایت عربستان سعودی
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71566" target="_blank">📅 13:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71565">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0000373bd7.mp4?token=qO9w4Sx9jOS3RX0YUP5PHdwQdYD7jfrRLHhn5AQPz2gxh9SnDHDospYyIfxev_lX0CbbWOcKIdIlUKs-Avb13Qhj78Eo6oHWIr8SB6Z_Ap1N_bmtkjnT0T-ubMPjqhXmi3E_xv3AUAZ61OZBqmMK4yWbXP73dadRIdR_QsDqHqMWU71adJNU61FpbLPKpoD7lF4pk6LGBKDAtmMKpTM5Tf_TuGSJ1CE_BqKIfpofJ6gPDn3ImbCLogUYivdcXIdNicmudfwnQg9dKahxEt4ipfxqStoIlnBXIsT7ucZHxN6c4ofH7Y6t91mUw4GiNFYwHBoYX9efJbSgLuySqZ8KoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0000373bd7.mp4?token=qO9w4Sx9jOS3RX0YUP5PHdwQdYD7jfrRLHhn5AQPz2gxh9SnDHDospYyIfxev_lX0CbbWOcKIdIlUKs-Avb13Qhj78Eo6oHWIr8SB6Z_Ap1N_bmtkjnT0T-ubMPjqhXmi3E_xv3AUAZ61OZBqmMK4yWbXP73dadRIdR_QsDqHqMWU71adJNU61FpbLPKpoD7lF4pk6LGBKDAtmMKpTM5Tf_TuGSJ1CE_BqKIfpofJ6gPDn3ImbCLogUYivdcXIdNicmudfwnQg9dKahxEt4ipfxqStoIlnBXIsT7ucZHxN6c4ofH7Y6t91mUw4GiNFYwHBoYX9efJbSgLuySqZ8KoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
این رهبران جدید و رهبران واقعی که رئیس‌جمهور ترامپ از آن‌ها صحبت می‌کند، چه کسانی هستند؟
🇮🇷
پزشکیان:
به گمانم باید این را از خود او پرسید، چرا که هر روز حرف متفاوتی می‌زند.
یک روز می‌خواهد ایران را نابود کند و روز دیگر می‌گوید ما دوست ایران هستیم؛ یک روز می‌گوید ما را به رسمیت می‌شناسد و روز دیگر می‌گوید ما را قبول ندارد.
بنابراین، ما مطمئن نیستیم که باید کدام اظهارنظر را بپذیریم و بر اساس کدام‌یک عمل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71565" target="_blank">📅 12:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71564">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71564" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71564" target="_blank">📅 12:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71563">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnMot8NdiAdCilOG8rOFQnl3p1Awfk85gERXivwgtAtXtxBrHgCKHHGqlBEIzJdqRkTlrk5PjzjhbPyrWWFp6fyxaqUDL1DCxQN20LHir6ikQns1n_ifQDP08zp12f6yIcqo9CrmZ8giMILsxzDxbKSdYe1RUHE-qXp25fBCGakB5dbJpZ8qYUVIYc_ptNp01XR6UZlSx_JHN-ldzz31isCFGt8G6S8LizjkFe7E23A4yfSevu_trTHDd0C8yMwNbl4pVKvKB45ZSH69EYhlsQUSOopr0LMd6ujl9Kguh5DmmKkiNmgl3LQyAu3AUEAUoQCHruWP7LNfiKyTZ8zdmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد بزرگ منچستر در راه است!
نبرد هیجان انگیز
⚽️
منچستریونایتد
🆚
منچسترسیتی
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ دربی اخیر منچستر:
⚽️
منچستریونایتد: ۲ برد، ۲ تساوی، ۱ شکست و ۵ گل زده
⚽️
منچسترسیتی: ۱ برد، ۲ تساوی، ۲ شکست و ۵ گل زده
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71563" target="_blank">📅 12:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71562">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrI6KaGwqxLUg2k7xa50Hqg7V0c_1xLBA5u-h0tPMDcu6ErIz2bZQssCJaJatbpyNEIY3dy4eXkftsV4ytyOZT7gpn5qdByMjlxfr0nJyccNc0YKv-ORnwH1eVQDjJIBgZE9CzITXp2ucKY0ox8gS9XpqbjZlaSG70z_cHMApKrPVYwcjjwPafsg7CABRcTmfdD606mnGBGq-3Wi6ve86oKUeQiNBrVi1Xifj3ZpTKkQye0kKHukdlr7_Y10H48OBDMkv44rzDvH7iuws_WByuSQKy9cWB3-3P-uL1DsbE_yidsWyCkXgxsXJ9MlC5rC1-f1c0r8pEE0WXM_YiNe-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
روز یکشنبه در گزارشی اعلام کرد که بر اثر اصابت یک پرتابه ناشناس به شناوری در حال عبور از تنگه هرمز، در آن کشتی آتش‌سوزی رخ داده است.
این سازمان اعلام کرد که مقامات محلی در حال کمک به تخلیه خدمه کشتی هستند. در این گزارش، نام شناور یا اطلاعاتی درباره تلفات، خسارات و یا پیامدهای احتمالی زیست‌محیطی آن ذکر نشده است
.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71562" target="_blank">📅 11:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71561">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇷
🇯🇴
ویدئویی از پرتاب انبوه موشک‌های رهگیر «پاتریوت PAC-3» از پایگاه هوایی «موفق سلطی» در اردن در سه روز گذشته، برای مقابله با موشک‌های بالستیک ورودی ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71561" target="_blank">📅 11:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71560">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c7237eb3.mp4?token=afWTsrN2zp3tDCo5UDD0yekEWuglHiKcYYvpeIux3X4Opbb1s0XYwk8-wEGWjzgFDB5vFw6ErytcBNlctdtjvqmIQzQUeB7rKUYrLtb90rTIaKPrhVjkRmPpiiCnqz0gX9jYI4_V6ePQ-9wnKOW-PgickNEMxjt5Y_-QROPJPTquneFeT8FkTbkZGMna3oYkl_lNV2C7n4X2jM1cFkv3SCM3JT7yPH0I325c0WoYwSAiH64GmqcRk1mou3gcXm8s4bPSMe4H5bSzs2ydkCJfelWoicy3bZ3ajPqe2ek1R4Mg0GFxx53hxuP3gtBeg37ui6XETY3hOro_GFU9IsyXmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c7237eb3.mp4?token=afWTsrN2zp3tDCo5UDD0yekEWuglHiKcYYvpeIux3X4Opbb1s0XYwk8-wEGWjzgFDB5vFw6ErytcBNlctdtjvqmIQzQUeB7rKUYrLtb90rTIaKPrhVjkRmPpiiCnqz0gX9jYI4_V6ePQ-9wnKOW-PgickNEMxjt5Y_-QROPJPTquneFeT8FkTbkZGMna3oYkl_lNV2C7n4X2jM1cFkv3SCM3JT7yPH0I325c0WoYwSAiH64GmqcRk1mou3gcXm8s4bPSMe4H5bSzs2ydkCJfelWoicy3bZ3ajPqe2ek1R4Mg0GFxx53hxuP3gtBeg37ui6XETY3hOro_GFU9IsyXmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
نظرات متناقض هادی چوپان درباره هانی رامبد:
بعد از قهرمانی
بعد از جدایی
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71560" target="_blank">📅 11:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71559">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097559287c.mp4?token=ncmj1F_Z4NfHhCFvAXRZscapT9A5WWsgy15iufFwKpghNJ_rey18SSG9xX762PX5e59isIe2Qph6OdsvUcAWx2wlAoxfGDygO82TUFLrX7Fc4NJLH-gkgJliydEMMIynOOVXYzlBFURTWt39FmOavszr9v7olCP10CDfXs44M7ajgN7iaYG3Flbtutvk9v-LEoAc4MhipOKDijwGur72XYWyt33YnoWJrLc6ig_np7c_LkituH5hj1tQT4cXskn7sjqQECbToXzVQvT6QZRwambOMeUCr1ZaCflGUdkcHI6IhPnoPlCoZR20ijTEDonI_WWH50F5h4z2rtZ8GdSyxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097559287c.mp4?token=ncmj1F_Z4NfHhCFvAXRZscapT9A5WWsgy15iufFwKpghNJ_rey18SSG9xX762PX5e59isIe2Qph6OdsvUcAWx2wlAoxfGDygO82TUFLrX7Fc4NJLH-gkgJliydEMMIynOOVXYzlBFURTWt39FmOavszr9v7olCP10CDfXs44M7ajgN7iaYG3Flbtutvk9v-LEoAc4MhipOKDijwGur72XYWyt33YnoWJrLc6ig_np7c_LkituH5hj1tQT4cXskn7sjqQECbToXzVQvT6QZRwambOMeUCr1ZaCflGUdkcHI6IhPnoPlCoZR20ijTEDonI_WWH50F5h4z2rtZ8GdSyxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
تلاش ابی برای بوسیدن دست یکی از بازیگران برنامه عشق ابدی که ویدئوش به شدت در حال وایرال شدنه!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71559" target="_blank">📅 10:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71558">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427cd49fec.mp4?token=IozFKnLVQtjleAst_awlqq0ulzkUiZS3e8dKVkMf6ROZPGLk5URu00jO9vMvsmYODPU-wx3fzMLI0OMpAbnaG04HlYypntEZNMBp_P4AYz2W44ylzRI4HNB0i0MzMzXyV3GpdAQsiB2qZLft6PRnAPgnwDUbVBCpeYY79zMRD9u-ZWkCPYY6ZUIRdWncCKOdgzAxlkesW7SvuNbeutV_ezIQXrLyNmNhEv3ivSu3Nty13bg70Nbsb7PURdUNjFP6iKIUiSfGcwzkvxAbz_GHmrlJPvE1Mjjr0pjKnbgm447RnOZfvHBCngzFUEsjz2xK4i2qkwnkUwIFlpHmBOn5uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427cd49fec.mp4?token=IozFKnLVQtjleAst_awlqq0ulzkUiZS3e8dKVkMf6ROZPGLk5URu00jO9vMvsmYODPU-wx3fzMLI0OMpAbnaG04HlYypntEZNMBp_P4AYz2W44ylzRI4HNB0i0MzMzXyV3GpdAQsiB2qZLft6PRnAPgnwDUbVBCpeYY79zMRD9u-ZWkCPYY6ZUIRdWncCKOdgzAxlkesW7SvuNbeutV_ezIQXrLyNmNhEv3ivSu3Nty13bg70Nbsb7PURdUNjFP6iKIUiSfGcwzkvxAbz_GHmrlJPvE1Mjjr0pjKnbgm447RnOZfvHBCngzFUEsjz2xK4i2qkwnkUwIFlpHmBOn5uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئو وایرال شده از 9 اسفند - روز شروع جنگ و بمباران تهران و واکنش  دانش‌آموزانی که خرکیف شدن
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71558" target="_blank">📅 09:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71557">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🇮🇷
امیر تیموری فرماندار شهرستان قشم:
یک کشتی تجاری حدود ساعت ۵ صبح امروز در محدوده جزیره هنگام و ساحل شیب دراز جزیره قشم مورد اصابت قرار گرفته است.
در این حادثه  یک نفر شهید  و سه نفر مجروح شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71557" target="_blank">📅 09:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71556">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnbsaoC5dH4K4U6GAW4T0075448BrqQnw94JYAFvYBhA6YMf2yHswKUld0wgDONFENRWgnpbuZb11nIBL27T0CtQ04w9LUmzYHQmCaDEsllz3mAvk5NTNLzOAUMotLIiJwNG8c9elHFf7qZ35Sa47_jRYIL0wlYtwKu3s8dTRqryUM0Xtj-rSjcfcBnNyFsWYBlif65fh-5AFAaMmTfhr8QafpB2hD1cPjUBHbX_9b3JPNZwNBRsgicKBTjbSRFDbI_gif61Nk2oF3hqSJzidJYb8l_ATyH75Dhmp64TGyolgjoVguKSP-mr76qCt0qEbVzjX1LbXR2tbmjaJqkOoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇳
🇮🇷
📰
وال استریت ژورنال:
مقامات آمریکایی می‌گویند ایران پیش از حمله موشکی بالستیک ۱۷ ژوئیه به پایگاه هوایی «موفق سلطی» در اردن — که منجر به کشته شدن سه سرباز آمریکایی و زخمی شدن چهار تن دیگر شد — تصاویر ماهواره‌ای با وضوح بالا از نهادهای چینی دریافت کرده بود.
این مقامات معتقدند که تصاویر مذکور با این حمله مرتبط بوده و احتمالاً به ایران در شناسایی دقیق‌تر اهداف ارزشمند کمک کرده است.
آن‌ها دولت چین را به مشارکت مستقیم در این حمله متهم نکرده‌اند و هویت نهادهای چینیِ دخیل در این ماجرا نیز مشخص نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71556" target="_blank">📅 09:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71555">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🦖
2 چالش، 2 کد مخفی، 2 جایزه 1$ در سایت بین‌المللی TREXBET !   فردا در دو زمان مشخص، عکس‌های چالشی داخل استوری کانال منتشر میشه؛ اما کدها همین‌طوری به دستت نمی‌رسن…
👀
🔎
باید با دقت بگردی، Promo Code یک‌دلاری رو پیدا کنی و قبل از بقیه داخل سایت ثبتش کنی! …</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71555" target="_blank">📅 01:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71554">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yit5A9wxByZWQaXgoc3znB285_hNsbwmZHVhLYcSkN3YOfsazLSJ7XROKt0HEFcqJmFqH4LWMDOZgwwBkRw974z8el03TUaEqcGoC2LnU5ppgplgHoDYGBiwwGlAwalNy0BB51p4ymafZ7QT5xlZoLTY_xb-rYdL9o3vjK6ArGE9iPC7g1JlEtWX7NxAFF3E0HDqK67kPuJOGc5HplTwHfvtNpP2K2S97ukpvzcOHC9g0NF-CAhg4Qer5sdraqTwaTDACRAqtm3NrL5_DrvIEaweKGn28jMfr_QM_cTSFfjRw0J75rjNFURibmjr6CrgoEtA-xheZuk0PI1hcc24ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
2 چالش، 2 کد مخفی، 2 جایزه 1$ در سایت بین‌المللی
TREXBET
!
فردا در دو زمان مشخص، عکس‌های چالشی داخل استوری کانال منتشر میشه؛
اما کدها همین‌طوری به دستت نمی‌رسن…
👀
🔎
باید با دقت بگردی،
Promo Code یک‌دلاری
رو پیدا کنی و قبل از بقیه داخل سایت ثبتش کنی!
⏰
چالش اول → 18:30
⏰
چالش دوم → 20:00
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71554" target="_blank">📅 01:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71553">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad61e1e00.mp4?token=Xu9n_iZ9tTdQS_cF7wow_IDNhYfnhhRrJjcuoxsJEiF96YsQScO5cz4CjFMqslqBVrzaB2O8gz37qKUOt8bGW37TWFuXO3-V1FsiB1kcqbSh7QKW31ubIoF7VtwKs_KGtDecQ61ZUMewo1iOS-JSLQJa--ZUDwWUE-KlbNsoKYyuHky6OcgONFj9cEZ2wZGbJJjIvjFmyv_OBya3LLnAQS53dR1XtsbY15VVlZG7QoNAZp-_s62gASZxkg9hOBxaipvcPUHuTYi_vG8BojxA8ii4f7BOEiu0TQ8EfGeXLEnCdOkrcHTDin1AgcjQ9lSxzNpxWpg35LbVM8BvADlBEqrWaB2FA6kik6nDDTWIJkaYggST8SO9ZvBlrOHMjns0Z_T1TF0FqCem97723TW10cqtFh5PS6jVHLYHdtxgaEePIQs_1A3ZQhgmZ19efudTFioxxGGGatMRuWYsekVRxVWdvkNVvWRjl5i9a6vqRLb1cCndm9roOQOcFXUUcl0i1tfR9Yzz1yYyxTC8qAT4r60BPcTx-XeW7Nr3B1vaWX-doezXEANBi-ZQWFJsftB64SeXfIcAnyBK5FU5EN8zK07S3tcg0w3ETXQ5wVsAUpnVJED8enbTczmFyRqRGPrxlzdj95Dcx3-6hXnwg2reLkCdfgaz8DPOKFwyd8wULNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad61e1e00.mp4?token=Xu9n_iZ9tTdQS_cF7wow_IDNhYfnhhRrJjcuoxsJEiF96YsQScO5cz4CjFMqslqBVrzaB2O8gz37qKUOt8bGW37TWFuXO3-V1FsiB1kcqbSh7QKW31ubIoF7VtwKs_KGtDecQ61ZUMewo1iOS-JSLQJa--ZUDwWUE-KlbNsoKYyuHky6OcgONFj9cEZ2wZGbJJjIvjFmyv_OBya3LLnAQS53dR1XtsbY15VVlZG7QoNAZp-_s62gASZxkg9hOBxaipvcPUHuTYi_vG8BojxA8ii4f7BOEiu0TQ8EfGeXLEnCdOkrcHTDin1AgcjQ9lSxzNpxWpg35LbVM8BvADlBEqrWaB2FA6kik6nDDTWIJkaYggST8SO9ZvBlrOHMjns0Z_T1TF0FqCem97723TW10cqtFh5PS6jVHLYHdtxgaEePIQs_1A3ZQhgmZ19efudTFioxxGGGatMRuWYsekVRxVWdvkNVvWRjl5i9a6vqRLb1cCndm9roOQOcFXUUcl0i1tfR9Yzz1yYyxTC8qAT4r60BPcTx-XeW7Nr3B1vaWX-doezXEANBi-ZQWFJsftB64SeXfIcAnyBK5FU5EN8zK07S3tcg0w3ETXQ5wVsAUpnVJED8enbTczmFyRqRGPrxlzdj95Dcx3-6hXnwg2reLkCdfgaz8DPOKFwyd8wULNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🟥
گزارش فاکس‌نیوز:
جنگنده‌ها از ناو «یو‌اس‌اس جورج واشنگتن» (USS George Washington) در حال برخاستن هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71553" target="_blank">📅 01:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71552">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uk413CSOc2vo0lh_YQIDEJXh6M8OGLZQ2xreHjDmFkpz1kCQnx3r1KqXs3TRbYowfATWfoi8rXNr9E7lrSQbMi9i4T3JISdd_mkbJ5dajdGgPaKbukFWMAgtOJ9VOstZo5rTz-M7xFd4gOriN453NCf50HydtPoao255Wdyb-Agk1B8QpZec2RtA8e4IvhfhCBMvGbeAdnYrG-zTf8qyVEDpP2Eh0Hh7oq5ekPuAdNKaSdhscoEIulGIv60QHuo55pehFDliUlEwPqMgA21x8clWrZJ8bSAA1IflfxRx5MckTtWw5Rx4HnYBWEVKivh39XOx9zah2VnGKrzH9M_4Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوری
؛کانال۱۴ اسرائیل:ایران برای خروج از پیمان منع گسترش سلاح‌های هسته‌ای (NPT) و آزمایش بمب هسته‌ای آماده می‌شود.
حاجی‌دلیگانی، نماینده مجلس، از آماده بودن طرحی با قید سه فوریت خبر داد و افزود: «باید هرچه سریع‌تر آزمایش‌های لازم برای سلاح هسته‌ای را انجام دهیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/71552" target="_blank">📅 00:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71549">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGh1mDIqabvUSlYolq0r2nFCiQeR2OTtpMwWvuA4jcbCNKnlJiSfh5h2GE1AAdtudTuHvUMXpwE-_m563-B2_dMgv26DqYnbn28DI6LwI2UppjFZYVyfKjJKDEgsivqXLRYkNBYHkaFPhY-FJuylmUQR7AyPtKWwvmcRxR8lsiRp3fBk0MIwJByupNUQSAE62JHnpzFyMvJsGCEn-SEM_DlmxGPOmEGqa1QO8oHQ1Nq3uG-mxbka_9f1DmjJfoZIBfLJPOFSreJCclppl4_9WHe1I6bPkdmlYbztUZSqjJwNTHChIOVNlz4PxVsCivtFc3RAtFmbNHhbDQVvQlnzMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ddef7d0b.mp4?token=Io8f9I1t5Sy79YBkhOcseOrOg63cUQny0bPkR7HSADPfHTSfXFi42_8elvjiZBXdJcwrCC6djw6gY9HX97O-uUOQLt50fQRWr31nYFoZwQpxbu-ZlyABHs2p_dgXh7YlkMpXp1pzCm716Xq7Xz4SF6cPw4YzxTpFs_5mZWRgo1nerboKSn0chWFIrSKmIApTyoWF0uZrD-YDu3zCo1pnaie_csguhf_nSOz48OvRqmLgcwZE49UUOQuDhdiT4nXVzQW8vh1SUpXqycCEfczJXowKfyEJT4dqFjIogXYzKEVUNIZVgJwvyqqu1znldCnhrTkmTa-0JbeCwAugE6ksfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ddef7d0b.mp4?token=Io8f9I1t5Sy79YBkhOcseOrOg63cUQny0bPkR7HSADPfHTSfXFi42_8elvjiZBXdJcwrCC6djw6gY9HX97O-uUOQLt50fQRWr31nYFoZwQpxbu-ZlyABHs2p_dgXh7YlkMpXp1pzCm716Xq7Xz4SF6cPw4YzxTpFs_5mZWRgo1nerboKSn0chWFIrSKmIApTyoWF0uZrD-YDu3zCo1pnaie_csguhf_nSOz48OvRqmLgcwZE49UUOQuDhdiT4nXVzQW8vh1SUpXqycCEfczJXowKfyEJT4dqFjIogXYzKEVUNIZVgJwvyqqu1znldCnhrTkmTa-0JbeCwAugE6ksfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
درحالی‌که شرکت اپل ایران رو تحریم کرده، قمی‌ها طی یه حرکت عجیب، همزمان با مراسم معرفی محصولات جدید اپل، خودشون هم به‌صورت جداگانه یه ایونت برگزار کردن و از آیفون‌های جدید این شرکت رونمایی کردن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/71549" target="_blank">📅 23:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71548">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac8d39358d.mp4?token=rNHuA87U6nbSdHy9TXOP2wRQDM86mKrSq9XHR9pLpKlD4MtEJ8v0IC1BHEOOCrACirndJZfcq6Vs3gRJlQgSdZjdxFV6UaeXJo0B4pAvs19gmd_duEsChIEra8QYzjLXPo6I5hD2jza9whnJ5Rus6b0_TPRZ0kYqRC3wwJkUkSKF8TdPV-J_pZxzrS3uCaurmXwTzHEmsOO3MQBb5LdPwtAhVKyFwZA01y5leU_IrsXDvI54juySxEm0utB2vN3y0Kg5M9wlrdvJpI6ZEbWYy0V-96C7Hiw43WcpIYO69VyrMK_d9oj9AVufmWwI39yRPcchlEZWHWj8Z3o6TTlkWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac8d39358d.mp4?token=rNHuA87U6nbSdHy9TXOP2wRQDM86mKrSq9XHR9pLpKlD4MtEJ8v0IC1BHEOOCrACirndJZfcq6Vs3gRJlQgSdZjdxFV6UaeXJo0B4pAvs19gmd_duEsChIEra8QYzjLXPo6I5hD2jza9whnJ5Rus6b0_TPRZ0kYqRC3wwJkUkSKF8TdPV-J_pZxzrS3uCaurmXwTzHEmsOO3MQBb5LdPwtAhVKyFwZA01y5leU_IrsXDvI54juySxEm0utB2vN3y0Kg5M9wlrdvJpI6ZEbWYy0V-96C7Hiw43WcpIYO69VyrMK_d9oj9AVufmWwI39yRPcchlEZWHWj8Z3o6TTlkWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
لحظه‌ای که جورج دبلیو بوش خبر حمله به برج‌های دوقلو را دریافت می‌کند
جورج دبلیو بوش آن صبح در مدرسه ابتدایی Emma E. Booker در ساراسوتای فلوریدا بود و برای دانش‌آموزان کلاس دوم در یک برنامه کتاب‌خوانی حضور داشت.
نکته جالب این است که بلافاصله از جا بلند نشد و کلاس را ترک نکرد. چند لحظه در همان صندلی ماند و سعی کرد آرامش خود را حفظ کند تا دانش‌آموزان وحشت نکنند.
چهره‌اش به‌وضوح تغییر کرد و حالت شوک و نگرانی در آن دیده می‌شود. دانش‌آموزانی که آنجا بودند بعدها گفتند تغییر حالت چهره او را به‌خوبی به یاد دارند.
جالب‌تر اینکه او حدود هفت دقیقه دیگر در کلاس ماند و بعد از پایان بخش کوتاه کتاب‌خوانی، از کلاس خارج شد و در همان مدرسه برای خبرنگاران صحبت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/71548" target="_blank">📅 23:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71547">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e621bd826.mp4?token=gnZjI7cPaxqnv4Dm2rBRWxF4psgUPkBSFnUDiRl_JFzr8PSiBuVqXthAZD1rEmw3lH_drcieUEuyFvLmjdyQ5UArr_zc3uLdULgw6xoEC8ypWD4y6K7O0TE0x3Nj_Cy0klcux1BaVfI8CHVCCKNCF2iP060YvyaASiTua1L1Lj7UNSEk70gX6nVTD2KWC7N-rJUPkx84I_PBNH3flKpX7tComzlcAMPtkoSWvddp6sFocZX2dK6NQemWJClXer7WSM-B1EQv5kAuFQXUrbmIdVQ2yBzUnOJULox6S40_ubCGxQ1ceKXvogtFUMZ0Tg3MPxUzmytpDPE1NpVTxHgCEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e621bd826.mp4?token=gnZjI7cPaxqnv4Dm2rBRWxF4psgUPkBSFnUDiRl_JFzr8PSiBuVqXthAZD1rEmw3lH_drcieUEuyFvLmjdyQ5UArr_zc3uLdULgw6xoEC8ypWD4y6K7O0TE0x3Nj_Cy0klcux1BaVfI8CHVCCKNCF2iP060YvyaASiTua1L1Lj7UNSEk70gX6nVTD2KWC7N-rJUPkx84I_PBNH3flKpX7tComzlcAMPtkoSWvddp6sFocZX2dK6NQemWJClXer7WSM-B1EQv5kAuFQXUrbmIdVQ2yBzUnOJULox6S40_ubCGxQ1ceKXvogtFUMZ0Tg3MPxUzmytpDPE1NpVTxHgCEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو مشهد اردهالِ کاشان، از " نمادِ مشت گره کرده‌ی علی خامنه‌ای " رونمایی کردن ولی انقد بد ساخته بودنش که صدای طرفدارهای حکومت رو هم دراوردن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/71547" target="_blank">📅 22:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71544">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YpsyAjZPJzeyFWfPSRPcPlXwd9vOPOMQOGph5f-bnAhI6sjYJCHTY5vdrXaAcr_tJSzLb8LxGqzg8Fc9PYViLBqiMlan1NdHlnygN0e5J2XVU5srZsFMRh1TmhxkLxmznr_w1xVA1FHPIp7hlguCpCokAeRbyXLNM6uugHZxsiDU1a0hhHhzqSsqtvnnzzYf6lEZFwhuo71an6nzasomYLfUYuuUf7lqN6MluVPkH30vQrzrpMIxnuabd5NZN0QMN44M8ffWEPimYE6yHDd1kolSe5DAEadaaHVn8J-EFrTvwF_2cBQ30yGt9zBfs5FDgWK5xBV4bm1CvikspwJQ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q-aQdG31pG182K42-R6VX2WdjCLhF1_owOIxZ3WYXkolMLbTKNwziNelRiSD3oAnlrCypciwzgg2DXVw21-EBMIUeUKvkjW7th4JRDZKyuSUUkFYLDQ4tjJGJf2ESpaauy4tUKMv_8HRoxZJznRm-uWMyF2gynIeQILFYyy7SJlTB7Fkfdb5XmwK_AQAwGluZXgxyVSm31d-6jBQyOzbR_QTzgCGVieZtV7DsrSbBgCTTPecOG3ctw5tiaqyqgztsZ5fh9LOjWzFs5ms9uU8NuY3lRX0ibvV7dWo7Dt3eH2KYrkj08A48lirDbQcuWp-oULJGCQaITI2AGJnoIfV-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jdUQyYXfBarGNZlH1p01N6CT3_LCcN4_AoHMgNoa7v596YeZ9KBmaBww1aeQkyaVYgLmac1HzKS4Wfoy9hIIlRZ0wmNB9TF3SXgLp5MzCeXsOOn6A7KcWDlAOR4L78cb2AbTIvMoC6mRcdAABz3TSTN4AAWzlGvG64z3GiiAKkTQK6LuPMopc_rBpsj1E-BeOIIIqrfrLXukf3pDIRLnjSJSrPO-3DNtcgg8Bi8kdtdkMALcJcvtpKgf6Wm_iZ4JZp-i1ykJj6tiaramEKE9igWSnoTvfiQacaaS79lVrSVnPQeQNprD-US1aCQ479u7q1Xc7YvY-HDk0pxuKYs0LQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚠️
کشتی‌ها و نفتکش‌های آسیب‌دیده ایرانی در خلیج فارس.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71544" target="_blank">📅 21:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71543">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
شلیک یک موشک/پهباد به سمت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71543" target="_blank">📅 21:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71542">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQiVciFAWI1j4OWT-lQ3fRcaXz661EV4b2QWwQVawmoOzudH8AKocqFlaorK9ZI3e-bp0SE_PSn2LobZ7mTPl8PWnFHKtbwsovU8M0bqLcUzrUqMEKy6VPQP9sTBiYB2PyFnqjmGrWOy49xFV1A5orAishS7AENqGIl_qqPnlPAThQ-ab1lwhCdSH5FUR313nCvnfh4HIxjtkXSRFFj63ZtzPuBUdu-pBGdq6OBPLuarq6m-Pa-RfVGVQet6Z2MACjTfsw8x2rNnnK4-V9gMuBAjFMyDGMlp_vJQUUB0e6uN5E3XmdY84lp1Y4Qg7lxcXUXtdM4JJuXfvs6MUWVGdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
شعار جدید عرزشی‌ها برای حسن روحانی
😂
نهپاد: نفوذی هدایت پذیر از راه دور
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/71542" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71540">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a60a908ab2.mp4?token=PpHrXdQ0qLZ4uiFatjDqUOe4vfim2IyJhBJxl4vGInStRvnFJS8ADsrcrKzQxfZ7zPxKU-TrRs8pJypfpPSJI_3THPZT4vldVu-1iQxyfmi1oEy0FhMylWHAqmcqGgADuralyJ6ZztHSmz2pr-RmTxAPcTVV7IbkRwJRqVYDjxZG0GnlD-Y1AuVbLDH-OA3z6iE19WHAsqsc1kLPWyYvrBwW1FQFNBk1G8Jfoj1ION0DEiBq6T0mg7J4IIeW_y454BreDVCxVqpHjPJiONiYVL-vt_CRtvylImk8OtEbjkIRmy5bFCujW0L-tWSNriibo57bZPtNE_Vlc_Bz7WLUVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a60a908ab2.mp4?token=PpHrXdQ0qLZ4uiFatjDqUOe4vfim2IyJhBJxl4vGInStRvnFJS8ADsrcrKzQxfZ7zPxKU-TrRs8pJypfpPSJI_3THPZT4vldVu-1iQxyfmi1oEy0FhMylWHAqmcqGgADuralyJ6ZztHSmz2pr-RmTxAPcTVV7IbkRwJRqVYDjxZG0GnlD-Y1AuVbLDH-OA3z6iE19WHAsqsc1kLPWyYvrBwW1FQFNBk1G8Jfoj1ION0DEiBq6T0mg7J4IIeW_y454BreDVCxVqpHjPJiONiYVL-vt_CRtvylImk8OtEbjkIRmy5bFCujW0L-tWSNriibo57bZPtNE_Vlc_Bz7WLUVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
❌
🇾🇪
حملات هوایی جنگنده‌های عربستان سعودی به استان البیضاء یمن
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71540" target="_blank">📅 20:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71539">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvNzPdlG8pEO495pcukn1UEk2lYcB_MJPLk8_JXHwkQsjFcQRaggV38qTbIu7GWYQmcAIJmxxt0NZm65VjuOXd_M3RpFek6_up3YQxJt77qiYLMdrCCYisgC-tedC6paH0t_i0iQrCrqhVCcuTc4Mu3Y2d9zXd4p3mW9nm7WbBnjKJvFU4T8_ee_zZeOohnwcJbT9yvOL6maWoH6Nevp2bQaUNR4epmKeOsU174m_vR7lWP9M1a3nxG33mZHu-G4xVFJnuvXd1f55m3ZpaDdJZxIAVz6h27wKA0paOwbY-HjB_ChOvk8DroQUzyhDq_3ODS4-ePPGbVebJdsUAbUYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
علی قلهکی:
مذاکره متوقف شده است چیزی وجود ندارد که میانجیگر داشته باشد.
عاصم منیر هم جمع بندی ندارد که اگر وارد جنگ یمن شد، بتواند پیروز شود و پرتابه‌ای سمت تاسیسات حیاتی پاکستان نرود
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71539" target="_blank">📅 19:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71538">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvEC1uu0NpBxEnJB8jDQGE3H5w-uzwHtdRMojfoZZWQz4_PNgwh6-yyhLK7lTg0Ay0CVPA8GUuA56_-cxp7cUMh1xXL67DNZUHgFwZovVTaxnl-1pdA9TPmEnjdOCpxmS70zPi8lj0-NzEAynFZQ5kAil1QFyEJP08KnHElTAtxzXlaSc9wnyQ8FYyXLiVs-rpG_3TFmfxFiOCJJOl_3aqFxm1zqCiGiFdzgQLc6TMwk0CL5_nAfEczWMyZ8PpxCnANcYMOm4tZ4bQjSFa4KAIzb29ts9Wjt1Mh-nycXckbOdeeai2gTntJFiSQM2w50MsrL3LoQOrD0rrBzVoE56A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
فرماندهی مرکزی ایالات متحده:
از زمان ازسرگیری محاصره موسوم به «دیوار فولادی» علیه ایران توسط آمریکا در ۶۰ روز گذشته، نیروهای سنتکام مسیر ۱۰۰ کشتی تجاری را تغییر داده‌اند.
حتی یک کشتی هم بدون مجوز نیروهای آمریکایی از این محاصره عبور نکرده است و نظامیان آمریکایی همچنان با تمرکز کامل بر این مأموریت متمرکز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71538" target="_blank">📅 19:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71537">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇧🇭
❌
🇮🇷
بحرین اعلام کرد تا زمانی که روابط دیپلماتیک با ایران از سر گرفته نشود، در هیچ‌گونه نشستی با این کشور شرکت نخواهد کرد و بدین ترتیب پیشنهاد عمان برای برگزاری نشست وزرای کشورهای حوزه خلیج فارس و ایران پیرامون مسئله هرمز را رد کرد.
🗣️
بحرین چهار شرط تعیین کرد:
توقف حملات
پرداخت غرامت
احترام به حاکمیت
حل‌وفصل اختلافات از مجاری قانونی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71537" target="_blank">📅 19:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71533">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b779ef03e.mp4?token=AT5qb12Mvf02raUCpd5bMPxD-6QeJHPtR3KqGPuaTfxUafx6kydSSy4WtDzvvC-A01FbODbtpLyuTBQtl018XNk39IRJl40F_14waBktKErSY07Q36JyecV6rTzQ5FTt8sVwa7-K5uAE7FayTpO8C9v367lfVUJh81w-Xe0nzJmQdSDyvNZBPbe1bb-F2Bkv8OhkyuzsU7gqKnAPsSJzdAyVYNMNnlgQbMuyAdnyBGEnWYNDdCOnVNmBsTxK7Gzvz0kqlNLTuSdUHIFHEjp5ivVV7CWGld6K1QONAY7e7VPVahWW-5KRcMTLxzX-oLEEVlb9QK8BYG2gwryxqLS9Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b779ef03e.mp4?token=AT5qb12Mvf02raUCpd5bMPxD-6QeJHPtR3KqGPuaTfxUafx6kydSSy4WtDzvvC-A01FbODbtpLyuTBQtl018XNk39IRJl40F_14waBktKErSY07Q36JyecV6rTzQ5FTt8sVwa7-K5uAE7FayTpO8C9v367lfVUJh81w-Xe0nzJmQdSDyvNZBPbe1bb-F2Bkv8OhkyuzsU7gqKnAPsSJzdAyVYNMNnlgQbMuyAdnyBGEnWYNDdCOnVNmBsTxK7Gzvz0kqlNLTuSdUHIFHEjp5ivVV7CWGld6K1QONAY7e7VPVahWW-5KRcMTLxzX-oLEEVlb9QK8BYG2gwryxqLS9Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین  به اهدافی در چهار منطقه روسیه حمله کرد که حملات ساراتوف تایید شده‌ترین و چشمگیرترین آنها بود.
مرکز لجستیک عظیم اوزون در ساراتوف (با بیش از ۱۰۰۰۰۰ متر مربع مساحت، بیش از ۳۰ میلیون قلم کالا ذخیره شده، تا ۹۰۰ هزار سفارش در روز).
طبق گزارش‌ها، پالایشگاه نفت ساراتوف (روس‌نفت، که قبلاً بارها هدف قرار گرفته بود) نیز آتش گرفت.
در ولگوگراد، فرماندار تایید کرد که آوار به یک مرکز صنعتی و یک ساختمان آپارتمانی برخورد کرده است.
منابع اوکراینی می‌گویند که هدف صنعتی، پالایشگاه ولگوگراد لوک‌اویل بوده است.
برخی ادعا می‌کنند که از موشک‌های کروز در کنار پهپادها استفاده شده است.
انفجارهایی در انگلس (محل پایگاه بمب‌افکن‌های استراتژیک روسیه) گزارش شده است، اما هنوز هیچ اصابت تایید شده‌ای به فرودگاه وجود ندارد.
بنا به گزارش‌ها، منطقه بندری کاسپیسک/داغستان نیز هدف قرار گرفته است - پس از حمله تایید شده شب گذشته به بندر ماخاچکالا.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71533" target="_blank">📅 18:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71532">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71532" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71532" target="_blank">📅 18:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71531">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZus5qbaREFKNp7MQWLboNY2fyMdjB-PjgZmCPVQvkyn2o1CYE_X__2gDPBaKEBd_g_W0VwQeE6-Hn59gb3EmoXVW8Yu8WCB7Btuc9dKErv-rnzBcTMXOc94YEEsudum4D6hNpIt23UrYZyY6Y_76TC1sl5LxkMXRBYIzsmgt-Tzd-xUPGyite5HZuXMa694hGU3upnHIT4S8fPLlInQ0wtpxi4z5Fsk0La-qeaIMLQSsMfmh4OYUnkwCPo91gFqu7bwPYd5dMHUf--CUxJbgTebnlMIgSRgmVAioXbvCExlwvT6iOyU-5PA_PkwH23R5Q3XAaISExOpAfNU8_k6Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
میلان
🆚
لاتزیو
⚽️
را در
TrexBet
پیش‌بینی کنید.
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
میلان: ۳ برد، ۱ تساوی و ۱ شکست و ۹ گل زده
⚽️
لاتزیو: ۴ برد، ۱ شکست و ۶ گل زده
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71531" target="_blank">📅 18:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71530">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/554b629d89.mp4?token=ulgTuKrwOGfs3OE3grvdZmb6SngJCJkF3qbp7nJ0H-uCkOxWn3A4GF0Q0AHHyleZgz3B63RHWmtwgwDS9wtT5J5vf52cSw8se4QFSP_uv3rYn3oqKUfc1ha9GtWyDIK1hnIwmUQ4yMELiygbHISC0T8wjbWkc1zdthv8O7BcW1Xd2ykP9lYPEMfhKt-6l2s0Hf-G2-Nmrx7jIeDuV3BEiEe7pBNWgWHi81xq779kTTs0lNIU9tJj6EYqiPZiWeNw3WzmFFbKlx5KgM8cdS2NCFi8PPXZN6bYy1Pq0bG-Os_odDpBnuzqIMLf-CkVZC99rgRSjRV12kvFzlnR9eiLkA0eaHiZiogPkGW09gAILJynpa8MXhM619dDZ5q8VaOvK8W0xjZ5J1pPleReN3fmI01A5Mt-dq_phxNqB33xCkGAGuVgO47MJR_91_xNEg76YYYIbyWi3G9ViesleKSI9k04I3_NbMeRTkFDkN1OLxD_gfyS8qNmQ7pD4ejIFCKHZ5mc8J7BJhiF5D24t9EC3On7LgCtfHVnJIGahLRSQiS6TcEB3vILDEIfD70HwpcUI_Ojpk1uiEZPN5s-UQJLtf1msGBQBeLVI9Jspa6HNafowk03GGrmhSkF2DsUWYwD3vh_qzwvfuu-UfIGVu1HffCqxU8cZX3eeiVX8T2K4iY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/554b629d89.mp4?token=ulgTuKrwOGfs3OE3grvdZmb6SngJCJkF3qbp7nJ0H-uCkOxWn3A4GF0Q0AHHyleZgz3B63RHWmtwgwDS9wtT5J5vf52cSw8se4QFSP_uv3rYn3oqKUfc1ha9GtWyDIK1hnIwmUQ4yMELiygbHISC0T8wjbWkc1zdthv8O7BcW1Xd2ykP9lYPEMfhKt-6l2s0Hf-G2-Nmrx7jIeDuV3BEiEe7pBNWgWHi81xq779kTTs0lNIU9tJj6EYqiPZiWeNw3WzmFFbKlx5KgM8cdS2NCFi8PPXZN6bYy1Pq0bG-Os_odDpBnuzqIMLf-CkVZC99rgRSjRV12kvFzlnR9eiLkA0eaHiZiogPkGW09gAILJynpa8MXhM619dDZ5q8VaOvK8W0xjZ5J1pPleReN3fmI01A5Mt-dq_phxNqB33xCkGAGuVgO47MJR_91_xNEg76YYYIbyWi3G9ViesleKSI9k04I3_NbMeRTkFDkN1OLxD_gfyS8qNmQ7pD4ejIFCKHZ5mc8J7BJhiF5D24t9EC3On7LgCtfHVnJIGahLRSQiS6TcEB3vILDEIfD70HwpcUI_Ojpk1uiEZPN5s-UQJLtf1msGBQBeLVI9Jspa6HNafowk03GGrmhSkF2DsUWYwD3vh_qzwvfuu-UfIGVu1HffCqxU8cZX3eeiVX8T2K4iY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
پست جدید هیچکس (سروش لشگری ) توی اینستاگرام که وایرال شده؛
«هنو به یادتم»
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71530" target="_blank">📅 18:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71528">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4b43f033.mp4?token=PB2iq3doryRTTaiBiQwNcGF_MHYQWki_o8xXGAaRhVtZcYGAo78YgtphJEXZN__d_s2R_W1wDyFGiCfu4AQ3OxuoCAtHPfzIAeKiA3haa2BuXtTLaAX7KabVCckKXC4DG08WPlmqT1CjJWXJg16ADJYWI5Eu88lb5vfpTHvYgJu65Bb-VS_fQ7YyTi4lHTFNDxjAZGiZJV9KvfMnj-oqgQpb_-s7z3U1Xt9u_45hU9TlPtXPQ4yv_iauVSa-4diWwjb1M_rtJLqy4K8oIxDIuMyYZ-QBw05oKv4t0vzreDrwKY-0ASQ5nz79ICbSb-msuvh1n5-Yw_SmG8OuQQseBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4b43f033.mp4?token=PB2iq3doryRTTaiBiQwNcGF_MHYQWki_o8xXGAaRhVtZcYGAo78YgtphJEXZN__d_s2R_W1wDyFGiCfu4AQ3OxuoCAtHPfzIAeKiA3haa2BuXtTLaAX7KabVCckKXC4DG08WPlmqT1CjJWXJg16ADJYWI5Eu88lb5vfpTHvYgJu65Bb-VS_fQ7YyTi4lHTFNDxjAZGiZJV9KvfMnj-oqgQpb_-s7z3U1Xt9u_45hU9TlPtXPQ4yv_iauVSa-4diWwjb1M_rtJLqy4K8oIxDIuMyYZ-QBw05oKv4t0vzreDrwKY-0ASQ5nz79ICbSb-msuvh1n5-Yw_SmG8OuQQseBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
شعار «مرگ بر روحانی» در تجمع شبانه عرزشی‌ها
:
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71528" target="_blank">📅 17:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71527">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e506b56e1e.mp4?token=ko1ON5rhYHYzDyAkwYFOXDWC8U1WZ4qwzn9juYQMn7OBxOVvxKmz0ClwaZnnhm-JTe0NWrUTKj0aJj5MU5Fs3zRAoXLaFXWSUsNlR-YwbSwkzY6qqZCaeSjjNafxgyfhwA4oCI0rzKfTOI7On8KksYYzLvkUtejlGI6Vw7oB7oU0Q_Uv_AC9VULPazD0E0qDXKedkrAWt6sjVXfsaBCZ3j_yNhh5f1VpzBgUBUVftPuj1Iaq2V8vBH8Q9JdV2g8-C-DrwLLn94lv7U3j0Jp0ARglpivM7spAagAP6dJqa8P8YNspznmudU3XxZ9rb-bQ7v4gDRpOC44xJtvLUrvNVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e506b56e1e.mp4?token=ko1ON5rhYHYzDyAkwYFOXDWC8U1WZ4qwzn9juYQMn7OBxOVvxKmz0ClwaZnnhm-JTe0NWrUTKj0aJj5MU5Fs3zRAoXLaFXWSUsNlR-YwbSwkzY6qqZCaeSjjNafxgyfhwA4oCI0rzKfTOI7On8KksYYzLvkUtejlGI6Vw7oB7oU0Q_Uv_AC9VULPazD0E0qDXKedkrAWt6sjVXfsaBCZ3j_yNhh5f1VpzBgUBUVftPuj1Iaq2V8vBH8Q9JdV2g8-C-DrwLLn94lv7U3j0Jp0ARglpivM7spAagAP6dJqa8P8YNspznmudU3XxZ9rb-bQ7v4gDRpOC44xJtvLUrvNVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
یک شهروند ایرانی با انتشار ویدیویی اعلام کرد ترکیه مرزش رو به روی ایرانیا بسته و اجازه عبور و مرور رو نمیده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71527" target="_blank">📅 17:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71526">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89e47bf456.mp4?token=Z7dhWrIELO6hJidEJJmRzid0smKqgrP6FFT0hd-XX5woADsmz7UBUpPSfg7FmKw4RRbfIFYzqYo00mT42mhDfMyqeU6i_michxaFxsUqcw0ktz4YWX-gJ4jyzeY-55_7HHr0CpxNMPfqkDl1_KFO1bMABwaMnp1WDud3W0Xck1HRn0jXJyT_rbvXPsSS0RcIi8fxvzsORAiFN8peJiK6hn6DscNQNFY6mpLQjTRNLvhOQTSfrH4Jhhf3T6HaC_sByhj3zpjw5F9HktZrKGYHGgKeKMJQZj6WvAgWZy_Eskj-7fQ8WhRtrQssRRwLZ9SDIdu0NVcGB-e2wqduvqCTIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89e47bf456.mp4?token=Z7dhWrIELO6hJidEJJmRzid0smKqgrP6FFT0hd-XX5woADsmz7UBUpPSfg7FmKw4RRbfIFYzqYo00mT42mhDfMyqeU6i_michxaFxsUqcw0ktz4YWX-gJ4jyzeY-55_7HHr0CpxNMPfqkDl1_KFO1bMABwaMnp1WDud3W0Xck1HRn0jXJyT_rbvXPsSS0RcIi8fxvzsORAiFN8peJiK6hn6DscNQNFY6mpLQjTRNLvhOQTSfrH4Jhhf3T6HaC_sByhj3zpjw5F9HktZrKGYHGgKeKMJQZj6WvAgWZy_Eskj-7fQ8WhRtrQssRRwLZ9SDIdu0NVcGB-e2wqduvqCTIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو از عشق و ابراز علاقه زیبای یه پیرمرد و پیرزن ایرانی توی پارک خیلی وایرال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71526" target="_blank">📅 16:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71525">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/401752fb0e.mp4?token=FE03EGiYWFK4hMcfFFloFDWZxCDrUhohwfELn1XNFvjm_EIdy3oMUqIcnTCTVZPX8O_aQNKyMOrjQFMquK16NCwL0mn5nCcEgzbBFpxEg_a3N7Gjmq_HglOw-XCJhAEJVqlroVDiA3Y18PLKgPUIdZPpFweJMc1f8gev7NZBeoRzlI3k_SgMsPskVfi8TBDrye8iw2D376_fhZOAtSDV7prICVgZcKHxdoz0pexZFI3d1JM_cCvV_71fFj6kucAZqPiH_IcZ7emRAIHP3gj0bg_CrFdIPVyVY_VYpjKq1Kr-wNvf6nasTER15jY2i-uMN5hZCw6uDX_bEjP9pYJqaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/401752fb0e.mp4?token=FE03EGiYWFK4hMcfFFloFDWZxCDrUhohwfELn1XNFvjm_EIdy3oMUqIcnTCTVZPX8O_aQNKyMOrjQFMquK16NCwL0mn5nCcEgzbBFpxEg_a3N7Gjmq_HglOw-XCJhAEJVqlroVDiA3Y18PLKgPUIdZPpFweJMc1f8gev7NZBeoRzlI3k_SgMsPskVfi8TBDrye8iw2D376_fhZOAtSDV7prICVgZcKHxdoz0pexZFI3d1JM_cCvV_71fFj6kucAZqPiH_IcZ7emRAIHP3gj0bg_CrFdIPVyVY_VYpjKq1Kr-wNvf6nasTER15jY2i-uMN5hZCw6uDX_bEjP9pYJqaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه دختر حامی حکومت:
چرا پزشکیان ۱۷ شهریور که تولد مجتبی خامنه‌ای هست بنزین رو گرون کرد؟ چرا روز تولد خودش گرون نکرد؟
میخواین همه تقصیرات رو بندازین گردن امامِ ما یعنی مجتبی؟ کور خوندین!
ما دیگه فریب بازی‌هاتون رو نمی‌خوریم که میخواین علیه رهبرمون کودتا کنین.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71525" target="_blank">📅 16:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71523">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e93a51beb4.mp4?token=Sx7PcaJ33Nd365hrTDB7TJcUtI8BBCbKAXYw19j4Rh9U_utGYSS4aeK5vmZYzGlpDHFLJwQ2-CWsXaaspAoozKtmOGpueru9E5GIitPnHmAKyeAQU5-nwARI-oxeoQOukIzKkrg7cPwgo5lw98a65xCd_o-vW6TeXgS_mxmN8q4o8IOa6XNTf2cpuxgITSY2IfXMfq_tIqhnGJmXosUFLRpcmbEqGkV1HQpr6zbjBj6m7H0BKIfLcRB9MlcloL-8BUDFtvH80HrKHcmKAga9CysVEw9sh8X46pU5fI3mhmBxfM8etTa1W8Zl1nBc_9uekLVMUwxuH-8NJNYuMckiH6x6u6B-o7UHcqWCNC70zV2rfp7oVWGpdDFGoO9K1bD0JRSqB6Q3S4OPOY6b9qb4-HlQf0KUkDzJmQkU2EI8C2lLsyjpe7TqVCybMC6Yy5Jj5-ZXmPKWN3QuCy85rHnyTjGBB3M7gJDzz9jcWnPDUpA-Ml1lLIP1RtWvMVIYBkNoUVhU9DOrf706nYvl5BBFiXo0mjzDweL3clAxYfXHnoabKgcItYNBR_23Yh4TiJnH_iolO79N-aDk7ja2qfjcumbKB5cScGEzd-o-aZppdYtvtjXUpXZMfIWvHndOjELWxJiffMe9A-QzEwkB1J1TLvP-c07Vc2aaV0F7V5XQ2hc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e93a51beb4.mp4?token=Sx7PcaJ33Nd365hrTDB7TJcUtI8BBCbKAXYw19j4Rh9U_utGYSS4aeK5vmZYzGlpDHFLJwQ2-CWsXaaspAoozKtmOGpueru9E5GIitPnHmAKyeAQU5-nwARI-oxeoQOukIzKkrg7cPwgo5lw98a65xCd_o-vW6TeXgS_mxmN8q4o8IOa6XNTf2cpuxgITSY2IfXMfq_tIqhnGJmXosUFLRpcmbEqGkV1HQpr6zbjBj6m7H0BKIfLcRB9MlcloL-8BUDFtvH80HrKHcmKAga9CysVEw9sh8X46pU5fI3mhmBxfM8etTa1W8Zl1nBc_9uekLVMUwxuH-8NJNYuMckiH6x6u6B-o7UHcqWCNC70zV2rfp7oVWGpdDFGoO9K1bD0JRSqB6Q3S4OPOY6b9qb4-HlQf0KUkDzJmQkU2EI8C2lLsyjpe7TqVCybMC6Yy5Jj5-ZXmPKWN3QuCy85rHnyTjGBB3M7gJDzz9jcWnPDUpA-Ml1lLIP1RtWvMVIYBkNoUVhU9DOrf706nYvl5BBFiXo0mjzDweL3clAxYfXHnoabKgcItYNBR_23Yh4TiJnH_iolO79N-aDk7ja2qfjcumbKB5cScGEzd-o-aZppdYtvtjXUpXZMfIWvHndOjELWxJiffMe9A-QzEwkB1J1TLvP-c07Vc2aaV0F7V5XQ2hc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ درباره ایران:
«ما کنترل تنگه هرمز را به دست گرفتیم. تمام مین‌ها را پاکسازی کردیم.
من گفتم: «خب، پس چرا آنها مین‌روب‌های ما را هدف قرار نمی‌دهند؟»
گفتند: «قربان، این مین‌روب‌ها زیر آب هستند. آنها همیشه در زیر آب فعالیت می‌کنند.»
گفتم: «چرا این کار را می‌کنید؟»
گفتند: «خب، به‌طور کلی، وقتی مین وجود دارد، بیرون از آن منطقه هم خصومت و درگیری زیادی وجود دارد.»
یعنی اگر در یک آبراه مین وجود داشته باشد، معمولاً افرادی هم هستند که به سمت شما تیراندازی می‌کنند. بنابراین اگر زیر آب باشید، آنها نمی‌دانند شما آنجا هستید.
حالا دیگر هیچ مینی آنجا نیست، هیچ چیز دیگری هم نیست. و اگر ببینیم آنها [دوباره مین‌گذاری می‌کنند/اقدام به این کار می‌کنند]، آن‌وقت می‌بینید چه اتفاقی می‌افتد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71523" target="_blank">📅 15:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71522">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffb4e73a23.mp4?token=IRfefqIDOrcnujx9PaSlvcTD5a_0IfjEyjv3Iphy5fWqJlaEAjY0GBdfq4L492KCBXNh5e8RFcy1sIqoJfC1bIPewvp5qVhV6ClXgDM5avWxUi21E5viGVuEGEC0bP48mwNBdyN2BEl8Pz0UW8VUITr4fbm8UW4HCiNOknS0Tw9ZNS00CyA1W1bzhB57t67CQUq3YWKeEnRgGdinUc_A7VkkRaj8i_6A8sL8U-waJ1zrNwesXlbc5Hfqc7xtd3T_F09hHjufYrzN8BKUll9TIpfB3wYasyfA-h4U9WZPd-7FnndwRdcLMg-ba2rMY_Z6RYpZMVlVP3UB-n4oyyEgng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffb4e73a23.mp4?token=IRfefqIDOrcnujx9PaSlvcTD5a_0IfjEyjv3Iphy5fWqJlaEAjY0GBdfq4L492KCBXNh5e8RFcy1sIqoJfC1bIPewvp5qVhV6ClXgDM5avWxUi21E5viGVuEGEC0bP48mwNBdyN2BEl8Pz0UW8VUITr4fbm8UW4HCiNOknS0Tw9ZNS00CyA1W1bzhB57t67CQUq3YWKeEnRgGdinUc_A7VkkRaj8i_6A8sL8U-waJ1zrNwesXlbc5Hfqc7xtd3T_F09hHjufYrzN8BKUll9TIpfB3wYasyfA-h4U9WZPd-7FnndwRdcLMg-ba2rMY_Z6RYpZMVlVP3UB-n4oyyEgng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
هادی چوپان :
هانی رامبد از پشت بهم خنجر زد.
گفت پشت جمهوری اسلامی نباید باشی ولی من قبول نکردم و اونم همکاریشو کامل باهام قطع کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71522" target="_blank">📅 15:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71521">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdiU1iUjsdudHt2x8rMl8PluR7n--6eoUJu8JPWpWZ08vtl7h9Wtcw9gIzkTXq_HiR8GWpO1tEzTl0eBKHP1H-02syudCchOGdVMaCdzDegydEa_1qpCqPCCHR4FvE0uTEFSgKk52nL12Q12tLUU9LiHQcagRcwR_HPItHyfLFSAmd9P-C7g89_6oosjWyKvOEPbetZ09gx9dEexABqSfAIZZEuoCXE8na1F4-GeZAt-POgWK2vMEt38KrhZV0pHZorFCPddyUqjONms9bJayBkmO_-7UvqKVWPPy_zJkZOK2Obo_yTrTPyKeW271F_sXp2T8cP-bDaaDwsNUF0zww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇦🇪
پزشکیان در جریان حضور در اجلاس سران بریکس با محمد بن زاید آل نهیان رئیس امارات متحده عربی دیدار کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71521" target="_blank">📅 14:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71520">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=eE_XBkDqaeaHGwsPDdJCR1DfcQrPM9tVTRulddLzrEHn56LaQzkE9GqDeO6YUqxmauCnnrH4DqmO1Pq_b1DYwxZVq0q5LbvMzXqiI_aFiB26CAs-Pe66Sy84SlN9wDboyAwxiYCbz-NunjvOnmOvL2fi0wEa_bhH5BA74pzlN98qGlEhpPys8iqBZPugwhTHf4RLJtpf7d1_UsPVgSLq61BeKhYPEMjebsrhb5Zq_czXQ7r426JHj0duEtzHBAagl7toUvih22D_EoZPZ8TgJG_3j1myeo5ue00rrI_41xh4FTEFvAylsIuDFLu8WP8PT16ppccpik2bXhkjGLl_FCi-Nd_9ku6zGOi7putchyR2puiLaqfiQZnwUA7BgO9C8yoKl2XEoaXXLj_c__-F0ysO1Wo3MCSgA_-bMJ11eV9Iy0KpGJ92Lq5rXjK37nH79USOWpeKg0VtECloX9yGkqEBr03uBLALTbz8g20K14SHcL03uej1rWiykHjrpIk_pevrrlpW7TVPJXpce3df3vs41j5J4I75UbcSV_55RZ_AfHSiGdl7wMPL1HIAdzu2hx4OF_RCNQ4Era09aJZ3rqK7oY_UUESoFxz74q-20gdUh8Jcv-pi4vWEW8VWIjmwoD6cotLaG_y0mvvuLeoUVbby2NgZUe4xPQ7ALYq3xDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=eE_XBkDqaeaHGwsPDdJCR1DfcQrPM9tVTRulddLzrEHn56LaQzkE9GqDeO6YUqxmauCnnrH4DqmO1Pq_b1DYwxZVq0q5LbvMzXqiI_aFiB26CAs-Pe66Sy84SlN9wDboyAwxiYCbz-NunjvOnmOvL2fi0wEa_bhH5BA74pzlN98qGlEhpPys8iqBZPugwhTHf4RLJtpf7d1_UsPVgSLq61BeKhYPEMjebsrhb5Zq_czXQ7r426JHj0duEtzHBAagl7toUvih22D_EoZPZ8TgJG_3j1myeo5ue00rrI_41xh4FTEFvAylsIuDFLu8WP8PT16ppccpik2bXhkjGLl_FCi-Nd_9ku6zGOi7putchyR2puiLaqfiQZnwUA7BgO9C8yoKl2XEoaXXLj_c__-F0ysO1Wo3MCSgA_-bMJ11eV9Iy0KpGJ92Lq5rXjK37nH79USOWpeKg0VtECloX9yGkqEBr03uBLALTbz8g20K14SHcL03uej1rWiykHjrpIk_pevrrlpW7TVPJXpce3df3vs41j5J4I75UbcSV_55RZ_AfHSiGdl7wMPL1HIAdzu2hx4OF_RCNQ4Era09aJZ3rqK7oY_UUESoFxz74q-20gdUh8Jcv-pi4vWEW8VWIjmwoD6cotLaG_y0mvvuLeoUVbby2NgZUe4xPQ7ALYq3xDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ:
ببینید، ما کار فوق‌العاده‌ای انجام دادیم. می‌دانید، ما آنجا را تحت کنترل گرفتیم. ما واقعاً با اقتدار کامل بر «تنگه هرمز» مسلط شدیم و هیچ‌کس متوجه این ماجرا نشد.
ما کنترل بسیار قدرتمندی بر آن داشتیم.
ما یک محاصره دریایی اعمال کردیم که واقعاً بی‌نظیر بود.
ما تعداد زیادی از شناورها را بیرون می‌کشیم؛ به‌طور میانگین روزی ۲۵ شناور را خارج می‌کنیم که بیشترشان در شب انجام می‌شود.
اما به‌طور متوسط، هر روز حدود ۲۵ شناور را از کار می‌اندازیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71520" target="_blank">📅 13:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71519">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🎙
خبرنگار:
آقای رئیس‌جمهور، جنگ در ایران چه زمانی پایان می‌یابد؟
🇺🇸
ترامپ:
فکر می‌کنم خیلی زود. گمان می‌کنم احتمالاً درست پس از پایان دوره [فعلی انتخابات] باشد. آن‌ها سعی دارند تا جای ممکن مقاومت کنند تا وضعیت انتخابات را پیچیده سازند. اما فکر می‌کنم مردم متوجه ماجرا هستند، چرا که ایران نمی‌تواند سلاح هسته‌ای داشته باشد. موضوع بسیار ساده‌ای است؛ مسئله خیلی ساده‌ای است. ایران نباید چنین سلاحی داشته باشد. آن‌ها تنها دو هفته با دستیابی به سلاح هسته‌ای فاصله داشتند.
اگر این کار را نکرده بودند [و جلوی آن‌ها گرفته نمی‌شد]، اسرائیل را نابود می‌کردند، خاورمیانه را به آتش می‌کشیدند و به برخی شهرهای اروپا — و حتی فراتر از شهرها — حمله می‌کردند. و احتمالاً پیش از آنکه ما بتوانیم آتش را خاموش کنیم، به خود ما هم حمله می‌کردند. اما آن‌ها نباید سلاح هسته‌ای داشته باشند. با این حال، می‌گویم که [این اتفاق] به‌زودی رخ خواهد داد و قیمت نفت به‌شدت سقوط خواهد کرد. وقتی آن اتفاق بیفتد، قیمت نفت به‌شدت پایین خواهد آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71519" target="_blank">📅 13:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71518">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⏺
🇮🇷
قرارگاه قدس نیروی زمینی سپاه:
درپی انهدام یک تیم تروریستی حرفه‌ای که قصد اجرای عملیات ترور در سراوان را داشت، ۴ نفر از این تروریست‌ها به هلاکت رسیدند؛ همچنین تعدادی سلاح و مقادیری مهمات و مواد انفجاری از مخفیگاه این تیم کشف گردید.
در این عملیات که تا پیش از ظهر امروز ادامه داشت ۳ نفر از پاسداران گمنام امام زمان(عج) نیز به شهادت رسیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71518" target="_blank">📅 13:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71517">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8136d3aa.mp4?token=b0BhIF95GKpysHa-IMPtgKMiWxd7FKahJ-dCQchh57ieRy6dBpE92-3XFZEuTCE8oZtWFh8FF7n2hVmVusRgYhp-66mbZuOofeKLt2QmnDoL8kRFinF8TvYC_VHg_11_VGCc7ZGm68EKGtpSS_KcPj64ANrDV6IAmbbJkDzV7cKjxMihQ83ohcxPayUgMPd3nMLulEGyWMa2QyvZ5BZuZId8C7za9PVmOabPhlJ3jqBcz7fk76fbWNolGjoazfG5jMuXgKZVEwyEUqiJ3881cBMy2o-kdleeO1JFXjZL2Q2-TEpWayO2u-KX2bkANeJNv-EnAMcGnay0kZFpZ21n-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8136d3aa.mp4?token=b0BhIF95GKpysHa-IMPtgKMiWxd7FKahJ-dCQchh57ieRy6dBpE92-3XFZEuTCE8oZtWFh8FF7n2hVmVusRgYhp-66mbZuOofeKLt2QmnDoL8kRFinF8TvYC_VHg_11_VGCc7ZGm68EKGtpSS_KcPj64ANrDV6IAmbbJkDzV7cKjxMihQ83ohcxPayUgMPd3nMLulEGyWMa2QyvZ5BZuZId8C7za9PVmOabPhlJ3jqBcz7fk76fbWNolGjoazfG5jMuXgKZVEwyEUqiJ3881cBMy2o-kdleeO1JFXjZL2Q2-TEpWayO2u-KX2bkANeJNv-EnAMcGnay0kZFpZ21n-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا ایران مسئول حمله به خط لوله «شرق-غرب» است؟
و به نظر شما عربستان سعودی چه کاری می‌تواند انجام دهد؟
🇺🇸
ترامپ:
خب، فکر می‌کنم همین‌طور است. احتمالاً همین‌طور است.
آن‌ها در حال حاضر در وضعیت آماده‌باش و هوشیاری کامل هستند، اما فکر می‌کنم مسئول آن هستند.
آن‌ها مدتی است که کنترل آن را در دست دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71517" target="_blank">📅 13:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71516">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9946b1f32a.mp4?token=jyZyqI7qGyjJkAMTVWY6ghQWa7t7cnVmjeeX8PhS3AFLNgkO90fBN5EaEqvm2jJzFV610GdofcAzQqC1Mk85_bXAKriF89YHVi8fXVWiUKj4eihSZAch0KO3BnvrcgeCOb2CPPr-eWq2YNLLuIUAm9g-QnZ9Z6SsoAiiBj66uwj2rK5KtU9cNKG92Kv7cdMZ3sRuAQnh2cKAFc5h6_Ddy8ITievoQOePkLoc1mlXUl5hdAb0ThJXC4ZQnTxSC57TcZSHtvaPcwghtvRVolZdsmcLjnZcwGXF80m2NsCAljmKgU38l4C7If8XVjsOT9MnCTgElIqTCcot0Dd6fE93HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9946b1f32a.mp4?token=jyZyqI7qGyjJkAMTVWY6ghQWa7t7cnVmjeeX8PhS3AFLNgkO90fBN5EaEqvm2jJzFV610GdofcAzQqC1Mk85_bXAKriF89YHVi8fXVWiUKj4eihSZAch0KO3BnvrcgeCOb2CPPr-eWq2YNLLuIUAm9g-QnZ9Z6SsoAiiBj66uwj2rK5KtU9cNKG92Kv7cdMZ3sRuAQnh2cKAFc5h6_Ddy8ITievoQOePkLoc1mlXUl5hdAb0ThJXC4ZQnTxSC57TcZSHtvaPcwghtvRVolZdsmcLjnZcwGXF80m2NsCAljmKgU38l4C7If8XVjsOT9MnCTgElIqTCcot0Dd6fE93HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
این رستوران توی تهرانه
نوشته : هیچی کتلت بی بی نمیشه:)))
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71516" target="_blank">📅 13:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71515">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0f6d97e2.mp4?token=Mqbq7br6ypvE9gmvCNGQzPfZlsROdkbjQoN5-c0RsH2LM7PJ7gARcQd0Rm9ThJy6CWJ1CZFtiYoYiuFKaYQOO3v_7zrnUGdcaPohypOonyNoNog1Upn0Rak6IHd3zBhAW0dIBbOJwo2z40XUjffq80D905sG12xEDgD-hMTWgTn0cdGz9SqSEH_tgtuMm72X29x0G7Xpt3F-Itt6jZkNfLcTEvaGpI0rOjaOKAGsWCiR7cOwxFz-pntNpR6Grwwpat3Zc4wsNI27y6IdK5hT-5P0yofzcPN65nSUKdmeyKkHvGC0XKFZCE-XKChiRNprOrh9EgwuPC9FL3lffnZFwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0f6d97e2.mp4?token=Mqbq7br6ypvE9gmvCNGQzPfZlsROdkbjQoN5-c0RsH2LM7PJ7gARcQd0Rm9ThJy6CWJ1CZFtiYoYiuFKaYQOO3v_7zrnUGdcaPohypOonyNoNog1Upn0Rak6IHd3zBhAW0dIBbOJwo2z40XUjffq80D905sG12xEDgD-hMTWgTn0cdGz9SqSEH_tgtuMm72X29x0G7Xpt3F-Itt6jZkNfLcTEvaGpI0rOjaOKAGsWCiR7cOwxFz-pntNpR6Grwwpat3Zc4wsNI27y6IdK5hT-5P0yofzcPN65nSUKdmeyKkHvGC0XKFZCE-XKChiRNprOrh9EgwuPC9FL3lffnZFwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
🇺🇸
پست جدید دونالد ترامپ در تروث سوشال:
با این رئیس جمهور بازی نکنید، زیرا نتیجه خوبی نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71515" target="_blank">📅 12:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71514">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1pMwAJZQyuaikr-5JrxH6AVoZRnV762IeM8j6qQzYfKZemKPj5SGDD0BbqdDAVT-PJTKwRhvoDpa96Ukfj2IUOtHXxL51FYz9SVVr5wrzxS2Q3VD1VblUoiH9kEJ3SjQ_5gMnDMFZPuj0Xt0RsNB4hvcWn2SUkJ2gqFaJ8Pu_ubznptmbUAmPJpE2y9jchZdmV6IfPoj1xVa_SLxnMme1Ae98zwRkaeRuqy2GHzfqOgxDJpudEZQG_yAFxFrVNgxv0EJj8n5xgTvlHLrG3nzbxG8mugw1r6jwvq8YZggUE7rsGM3v5O5DPQLd_Q1PCmq0LqlpRItwkZHVbwAF2swA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
طبق پیش‌بینی‌ها، یکی از پربارش‌ترین پاییزها تو راهه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71514" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71513">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71513" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71513" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71512">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLbWzoiAL4w7S3bFJCJTdlMlcgHJwLjBjQDLpibGJnPjsO4H5wSKmHXWG4Fr01db4vGO4pLZoRFiMdt0Gwq-CW52SxWDRxXiYnggmGaY_tcMXnFW54NVDghTMP5IyqKl_qTO5Le4ZgqM-x4NcLoMI5JnBODNy8sj-DXCRAvRSFFECi7-OLs4OGBJK6swRUDc46faAXxRc1BhEZ7Si0X2z6tAlOG9WKOXger4A_tHxDpF-uNiGZjx7suIyF8a9LLmR_1SrqBOc_5Hv2WHVhd0lAyWKkK5u_CbKIAjqCszDpCfYyIS9ToJl9wW8LSZNCiIWa9A_KsIjLy5ywVQUuWanA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت‌بین‌المللی
TrexBet
پیش ‌بینی کنید.
چلسی
🆚
لیدز یونایتد
فولام
🆚
لیورپول
اورتون
🆚
تاتنهام
ساندرلند
🆚
آرسنال
رایو وایکانو
🆚
رئال مادرید
میلان
🆚
لاتزیو
کالیاری
🆚
آتالانتا
پادربورن
🆚
دورتموند
🦖
🦖
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب برای بازی‌های امروز
🦖
واریز آسان و امن از طریق کارت به کارت و ارز های دیجیتال
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71512" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71511">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🇮🇷
معاون امنیتی و انتظامی استاندار سیستان‌وبلوچستان: محل تجمع اعضای «گروهک‌های معاند و تروریستی» شناسایی شده و نیروهای امنیتی در یک عملیات غافلگیرانه به آن ضربه زده‌اند.
در گزارش‌های اولیه، نام جیش‌العدل/جیش‌الظلم به‌عنوان عامل درگیری امروز به کار برده شده که هنوز به صورت رسمی تایید نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71511" target="_blank">📅 12:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71504">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d436ab6a3.mp4?token=CJp1aXqozNK2DIfMR-RugZwVHBSq-qOToTB-OLfVz90op8pOEw7Lxx31YImc46RSX9TRnRrrJLXoCqtxtFh0QEjLzmv8NsA3LHTfVk6yh5PBAmftit5z22Qky6UZQXly0Y9UX0bG49jE_x2ZNAD7EIpzgBNSCuEx-YogmRqLCAdTLh5eUj5XzKPb3yvBkzEU4FNLtQkvyE0iBDuEp_FiC2nSMuaXlVsU8qwfRlDyWc57Y3hWs0VB8Tr1m3rjoOhNJME2WzccLp1tlq5r7DYkZtBGpFLYvEuz63mxMhdRqd8Ce2Sj5tWMDESECzGF4kGc80t5YUMvnrszV8ivT9Av9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d436ab6a3.mp4?token=CJp1aXqozNK2DIfMR-RugZwVHBSq-qOToTB-OLfVz90op8pOEw7Lxx31YImc46RSX9TRnRrrJLXoCqtxtFh0QEjLzmv8NsA3LHTfVk6yh5PBAmftit5z22Qky6UZQXly0Y9UX0bG49jE_x2ZNAD7EIpzgBNSCuEx-YogmRqLCAdTLh5eUj5XzKPb3yvBkzEU4FNLtQkvyE0iBDuEp_FiC2nSMuaXlVsU8qwfRlDyWc57Y3hWs0VB8Tr1m3rjoOhNJME2WzccLp1tlq5r7DYkZtBGpFLYvEuz63mxMhdRqd8Ce2Sj5tWMDESECzGF4kGc80t5YUMvnrszV8ivT9Av9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
درگیری های بی سابقه نیروهای جمهوری اسلامی و نیروهای مسلح در سراوان سیستان بلوچستان
ویدیو ها مربوط به چند ساعت پیش
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71504" target="_blank">📅 11:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71503">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🇮🇷
🇮🇶
رسانه عراقی نایا به نقل از یک منبع:  دستور فوری و جدیدی از سوی فرماندهی کل نیروهای مسلح به بصره ابلاغ شده است که بر اساس آن، گذرگاه مرزی شلمچه با ایران از همین لحظه و تا اطلاع ثانوی به‌طور کامل بسته می‌شود. این تصمیم شامل تردد مسافران و همچنین جابه‌جایی…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71503" target="_blank">📅 11:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71498">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba81cb21e1.mp4?token=qQMtfbLaYh33bVsPGlVCE_3IxVqdRGKGdakfa_7Tw4gtGLTqIHeXO4YmMAmYRo3Z2oYGXzJypJnU44RFyNGXhYsNfe_bZhY4xRurT9oi3E1YLK5vc2M6Kg9KZvaV1LtHr-Aot_vSCdT13j6m4tOdvKCrE1P8StAZq0PVRlgSOUOvyv5m9Qna9FmAnFrOfFZxlzELrf-ZsZTVCF-NKGb42isR9iTWmmb8qTHVT4mSO7QeiB9qOVIvC_BV1L_eIvKhdulYAMkaaCkzp_0GssLMt4_RYabbruWcSEWibwADoKW3mba2Cx7DmeckLch4H8cKbVTY0MyTOpGnvzydne-Rgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba81cb21e1.mp4?token=qQMtfbLaYh33bVsPGlVCE_3IxVqdRGKGdakfa_7Tw4gtGLTqIHeXO4YmMAmYRo3Z2oYGXzJypJnU44RFyNGXhYsNfe_bZhY4xRurT9oi3E1YLK5vc2M6Kg9KZvaV1LtHr-Aot_vSCdT13j6m4tOdvKCrE1P8StAZq0PVRlgSOUOvyv5m9Qna9FmAnFrOfFZxlzELrf-ZsZTVCF-NKGb42isR9iTWmmb8qTHVT4mSO7QeiB9qOVIvC_BV1L_eIvKhdulYAMkaaCkzp_0GssLMt4_RYabbruWcSEWibwADoKW3mba2Cx7DmeckLch4H8cKbVTY0MyTOpGnvzydne-Rgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پسر تهرانی بعد از اینکه با دوس دخترش کات کرد، رفته تمام اکسای دختره رو جمع کرده، واسش دسته جمعی آهنگ خوندن تا قشنگ دختره رو بسوزونه و عقده هاش رو خالی کنه...
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71498" target="_blank">📅 11:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71497">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa7081550.mp4?token=P_x0L9ZYAm9McmDso7pYhoqDKmhs88myAeQW51f9-GSdXwb4Rfd0y3q-vI5fWakpm6qB_rqyLJ3zIDtdgIFB97IqYsAzTEcnOmC40Qcu34Y-tID1Dv3woBja1CFsWH_ugLA_LmlS98RWVSjY-da6WKYeSSS6Te0pr3nEAoaMVgjOw7NSskVDzKsRpQYJHZJvkGDHTsqln8LACIGplS3L7L7iBL2Sxy4nDApy0vx5RcrEqJPQr2NRvWtreqn7kSbMsZtRwmFnnjNgjn3WzHtsFfLc4TOuUgK7JgLwp7fQtllclrsYsvHGxxGCw-EHawPa8s_-Hetqm6NYIPHMWOLO8Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa7081550.mp4?token=P_x0L9ZYAm9McmDso7pYhoqDKmhs88myAeQW51f9-GSdXwb4Rfd0y3q-vI5fWakpm6qB_rqyLJ3zIDtdgIFB97IqYsAzTEcnOmC40Qcu34Y-tID1Dv3woBja1CFsWH_ugLA_LmlS98RWVSjY-da6WKYeSSS6Te0pr3nEAoaMVgjOw7NSskVDzKsRpQYJHZJvkGDHTsqln8LACIGplS3L7L7iBL2Sxy4nDApy0vx5RcrEqJPQr2NRvWtreqn7kSbMsZtRwmFnnjNgjn3WzHtsFfLc4TOuUgK7JgLwp7fQtllclrsYsvHGxxGCw-EHawPa8s_-Hetqm6NYIPHMWOLO8Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇹🇷
یه گزارشگر تو شهر وان ترکیه طی یه گزارشِ خیابونی، نظر مردم این شهر رو درباره گردشگران ایرانی پرسیده که حسابی وایرال شده؛
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71497" target="_blank">📅 10:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71495">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faeed5163b.mp4?token=rm5nl1hHsAsJzrXaQ5NT6r90JKPzZJrbVGs3QIV-K9Oneybvhrl4wqpeXZQ-sLIMb5oDGqAnOijt2HF0uZbMl62xf2zwJlRq3j0JS639gMz-z2KDiAA_kZy-A5b8c0tF_2KbMPZIiz93W2bg_pgMPHV04irRj8vB9Vqe-Aw8JaSsPdaSxH8e6xd9FikQ5RPdxZaH68MFOR9XpyBfLiM_Gk3MHnWRPerzaI2KI3xXD1v3y26V9sN118ZZGm4fI7MLD2HsZ9UnxYN_3xyHRl6djmc-lEQSnNJkZzHJpbvNe2teS7BXzw5vv6Ba5MdhCiidv_YmeW3ECG9xRuy5HGv8gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faeed5163b.mp4?token=rm5nl1hHsAsJzrXaQ5NT6r90JKPzZJrbVGs3QIV-K9Oneybvhrl4wqpeXZQ-sLIMb5oDGqAnOijt2HF0uZbMl62xf2zwJlRq3j0JS639gMz-z2KDiAA_kZy-A5b8c0tF_2KbMPZIiz93W2bg_pgMPHV04irRj8vB9Vqe-Aw8JaSsPdaSxH8e6xd9FikQ5RPdxZaH68MFOR9XpyBfLiM_Gk3MHnWRPerzaI2KI3xXD1v3y26V9sN118ZZGm4fI7MLD2HsZ9UnxYN_3xyHRl6djmc-lEQSnNJkZzHJpbvNe2teS7BXzw5vv6Ba5MdhCiidv_YmeW3ECG9xRuy5HGv8gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئو وایرال شده و پشم ریزون از کنسرت تیلور سوییفت؛
خودتون ببینید به چه دلیل وایرال شده
😏
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71495" target="_blank">📅 10:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71494">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‼️
خورلسوخ، رئیس‌جمهور ۵۸ ساله مغولستان، هنگام بازدید از یک یگان نظامی، حرکت پرس سینه را با وزنه ۱۰۰ کیلوگرمی در ۲۰ تکرار انجام داد.
او که پیش‌تر افسر ارتش بوده، نامش در لغت به معنای «تبر برنزی» است، باشگاه هارلی-دیویدسون مغولستان را تأسیس کرده و در یک گروه موسیقی گیتار می‌نوازد؛ او همچنین جانشین «باتولگا» شده است که خود قهرمان جهان در رشته سامبو بود.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71494" target="_blank">📅 09:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71493">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a695c5e874.mp4?token=iByCXmJYnCteDdnqZ8NysZtu5rdtVos5I78d7JxtzDryk4DVpAjwTb_Ztb57AURT-hHsfPnYAP5FKchQrRzF-bogaKAMJO6CnkZlx0WB3j3r4OzXWidokQLtVL9gwARmf3lo6ExaS2rNL_ZvZ7Ij0VIfREXqCX62UoEq1iujYVTuysrXm737SkP1ALGUvs_hhKqeKSEgo_JF8069NbHgwE83uEN5Xl_n_r25U142IZWf1iPlcynvWRbkcGlHViTurgNXMXqw8BLC-JpwcuX6VRlinEsnL96F0VKruRwUWIsnEbJzkKh5ETSMAmBXt3nD-_m0FXz-KG8D7PRUctP8Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a695c5e874.mp4?token=iByCXmJYnCteDdnqZ8NysZtu5rdtVos5I78d7JxtzDryk4DVpAjwTb_Ztb57AURT-hHsfPnYAP5FKchQrRzF-bogaKAMJO6CnkZlx0WB3j3r4OzXWidokQLtVL9gwARmf3lo6ExaS2rNL_ZvZ7Ij0VIfREXqCX62UoEq1iujYVTuysrXm737SkP1ALGUvs_hhKqeKSEgo_JF8069NbHgwE83uEN5Xl_n_r25U142IZWf1iPlcynvWRbkcGlHViTurgNXMXqw8BLC-JpwcuX6VRlinEsnL96F0VKruRwUWIsnEbJzkKh5ETSMAmBXt3nD-_m0FXz-KG8D7PRUctP8Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حسن روحانی خطاب به ارزشی ها : انتقام خامنه‌ای رو امام زمان که ظهور کنه میگیره
وسط مذاکره برای اینکه راهی پیدا کنیم که جنگ زورتر تموم شه یه عده میگن باید انتقام بگیریم خب چجوری ؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71493" target="_blank">📅 09:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71492">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🇮🇷
🇮🇶
رسانه عراقی نایا به نقل از یک منبع:
دستور فوری و جدیدی از سوی فرماندهی کل نیروهای مسلح به بصره ابلاغ شده است که بر اساس آن، گذرگاه مرزی شلمچه با ایران از همین لحظه و تا اطلاع ثانوی به‌طور کامل بسته می‌شود.
این تصمیم شامل تردد مسافران و همچنین جابه‌جایی کالاها می‌گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71492" target="_blank">📅 07:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71491">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/71491" target="_blank">📅 01:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71490">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pdv0O1qmnvGwWNPGeQOR3QSxDFOmzlgnfRMmD9vI0787fJO8wrqBAuK8zUkBR35KUM5x-UuV8xkVi2MnZQIeeVKmxlqDsOwqCcMn22ueaHz0w6rCHNMXysU9WmlRUCUxnLxRDnaOOQKZ4NWduxo1ZxMYyWuThtZpDsQ2wRikp9puKjHAyAZ-sKaROFVoAk4AyMEElJfDp1fKcJSGG2iAn5CMT5kT7zGyr63VwKZrVUYh_5RaxW8Cyijt8v7_r1BmwPX3Jx4OlsnCDwp6atD5OrgzrqCt8sKZQKjNExbcOWEzaTDd5H-CHJd9Rid36gB7fgGeBcBkiaJ0c1Nse63glg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/71490" target="_blank">📅 01:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71489">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c20cfcda3a.mp4?token=rRpcMj_H6EsUBgNbq4e2amqFqEp7Hr-XnUbkqOv6PwZk49L2EypmzPUk2kd0bDVhbGsK4jUZr9A-KAnzokMATSxAe7wJVQYyhxi1VRH2W9zPEG6EJ0EKHcYD-nvGAgX7cOnlaeyVbx1pdRTO6plYpQ4L91rqNLfNfkad0QwQWLFhD6CY3YqyhsbnCoeLvKI_1W0WUvfNujDaXvOJU8wO7UND-MfA0z7WQ5_S5OtymhP2wr0RxvicF4ragKoJH6reIWUccJKF2ISgdsnJtvVejYJQDTjnCgI8mkKYisgHLtQb8MLHLXmq2pinuIalLwNU-xFs7kus8IEYghYo7Stu5g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c20cfcda3a.mp4?token=rRpcMj_H6EsUBgNbq4e2amqFqEp7Hr-XnUbkqOv6PwZk49L2EypmzPUk2kd0bDVhbGsK4jUZr9A-KAnzokMATSxAe7wJVQYyhxi1VRH2W9zPEG6EJ0EKHcYD-nvGAgX7cOnlaeyVbx1pdRTO6plYpQ4L91rqNLfNfkad0QwQWLFhD6CY3YqyhsbnCoeLvKI_1W0WUvfNujDaXvOJU8wO7UND-MfA0z7WQ5_S5OtymhP2wr0RxvicF4ragKoJH6reIWUccJKF2ISgdsnJtvVejYJQDTjnCgI8mkKYisgHLtQb8MLHLXmq2pinuIalLwNU-xFs7kus8IEYghYo7Stu5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
❌
🇾🇪
تصاویری از حملات هوایی نیروی هوایی سلطنتی عربستان سعودی به بندر «مخا» در جنوب غربی یمن که تحت کنترل انصارالله قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/71489" target="_blank">📅 00:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71488">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgS_QQmGGAPcVfDhRJKj1BfjgnrAvCJmZ25f1e6mAAYAWd3Vn7Z4c6Vra7Mu0qme9zS2xPD0PD3PdmjKXSQZU8retPk4pALVst6siMHJ-aOlcAvw_j9Z0ELsLtLQUyq9f5JmxKA3mlGu0Y3dh-VMGge5VWIqvAcBkOFBqmimdDplOz4m1llSyWYRIQoFns9iat6fivtzuy51PM58q0D749xZnHYeujOqmMTepiUHIyZdRhT39nXISRWG3_IzQWkkaxQmj6G4fpM1kBZZGH86w0ttd4wErXpxlI-rfXxiL1nrec9c-pW5z2sCBncQL161s8SUu-r63mGss6Bec18iOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با پول ۲۰۷ در ایران تو کشورهای مختلف چه ماشینی میشه خرید؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/71488" target="_blank">📅 23:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71487">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2da32c63e2.mp4?token=vgDaH3RyPImyEsZ8s8QHmgFsKgz-uN0_o0eAXeR6yVRelPKiAeyPfqXnnNzdrqAJfSSCbkdxFSBQvcIA21kGeskKDqUjEF6vPhPFB3A_0LAmml5_vrVttlr8AcJ0k3J_t_87mzmlcXAOtIdTeFplzLGkoyyNahtVXSy8dGUMB0OGTS-5nqYA8vDOjfenX25GW-q6NkD__TWXFcTlfBVk5bjecyCEfNWXYZkV8lGQdpM_AZGhXk7LXSMvPM-NjPZe3qmnwEzACF7c47FNgeRhUnVPZzTPZx1QdR4G0TLw_4_7UEzEXXiQYFbfjCbXZkXfDnDcVvNP4vMJp7E1bjc4Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2da32c63e2.mp4?token=vgDaH3RyPImyEsZ8s8QHmgFsKgz-uN0_o0eAXeR6yVRelPKiAeyPfqXnnNzdrqAJfSSCbkdxFSBQvcIA21kGeskKDqUjEF6vPhPFB3A_0LAmml5_vrVttlr8AcJ0k3J_t_87mzmlcXAOtIdTeFplzLGkoyyNahtVXSy8dGUMB0OGTS-5nqYA8vDOjfenX25GW-q6NkD__TWXFcTlfBVk5bjecyCEfNWXYZkV8lGQdpM_AZGhXk7LXSMvPM-NjPZe3qmnwEzACF7c47FNgeRhUnVPZzTPZx1QdR4G0TLw_4_7UEzEXXiQYFbfjCbXZkXfDnDcVvNP4vMJp7E1bjc4Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇱🇧
🇱🇧
رسانه های نزدیک به حزب‌الله لبنان وویس هایی رو از اعضای حزب‌الله منتشر کردن که در زیر ارتفاعات علی‌الطاهر در تونل ها گیر افتاده بودن و درخواست کمک میکردن.
همه این افراد بعد از حملات ارتش اسرائیل و نابودی تاسیسات زیرزمینی کوه علی‌الطاهر کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/71487" target="_blank">📅 23:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71486">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68083de4e6.mp4?token=MYqEV_P9w-nBrfzW81glVz50Rnv1Zh3TNb1t2aLNgjVm0ErHJsIX_sYdgZGunfT-a6-azumvw1UF-mWxVqMzr8Nn7WAFSf24nXzutwf8UHp6Li8SBHHnaa1iCSdYjhG2Tgqq9f5gx8zVSbvOIImwJKcVjC5RJvpXBp-gNnqZS3Fi8PoQ4NOV6eha0RZCW9rGqqcZpCHs8fn54dLzWu8QIIAPFmiFEsrsJcYClpoAL4fa1jSswNeBZU-vMvtFmkWUUzBEb7Gxcpm-cicwdElzoeUQV01L6kRV4N5bUTj-ec45cPO4RnQePlbJk5zrXYz7R5yZHWVtLcyfA9hLYf_kWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68083de4e6.mp4?token=MYqEV_P9w-nBrfzW81glVz50Rnv1Zh3TNb1t2aLNgjVm0ErHJsIX_sYdgZGunfT-a6-azumvw1UF-mWxVqMzr8Nn7WAFSf24nXzutwf8UHp6Li8SBHHnaa1iCSdYjhG2Tgqq9f5gx8zVSbvOIImwJKcVjC5RJvpXBp-gNnqZS3Fi8PoQ4NOV6eha0RZCW9rGqqcZpCHs8fn54dLzWu8QIIAPFmiFEsrsJcYClpoAL4fa1jSswNeBZU-vMvtFmkWUUzBEb7Gxcpm-cicwdElzoeUQV01L6kRV4N5bUTj-ec45cPO4RnQePlbJk5zrXYz7R5yZHWVtLcyfA9hLYf_kWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یه دختره که پارتنرش یه ترنسه
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/71486" target="_blank">📅 22:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71485">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c1f7e0a7d.mp4?token=mdLMPOKXtcSkVYWk43oBcbznPGuH3NejYyRqy_M9C-ugziWVl1iBYADfxeeprks0YaffggQ1jmyAfWdg_0LNDZKtVjlGVAJf4Kwf1UFeSRDxEzEyvizRvtxFZ1cPa9Uk8Adtzr_LLtdtTtL222k_KHtfLt0oMdUbWCm6YLMfV-qe3HdzxkOQLqhrmOQUtEvU30hBxB5WOyr7_71koaNr1eRF8VNLQl5QBONreh17gaVKcJiQcZ-jZhbJh3kXPw2fJ8db7F-XItB8IlhAoGvR4TGisZ_VWLB3Yf0dSJqsfC7f98pOH9xrT04L4UUgdjTkHbm3X2W64lqpR8iVZzPDKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c1f7e0a7d.mp4?token=mdLMPOKXtcSkVYWk43oBcbznPGuH3NejYyRqy_M9C-ugziWVl1iBYADfxeeprks0YaffggQ1jmyAfWdg_0LNDZKtVjlGVAJf4Kwf1UFeSRDxEzEyvizRvtxFZ1cPa9Uk8Adtzr_LLtdtTtL222k_KHtfLt0oMdUbWCm6YLMfV-qe3HdzxkOQLqhrmOQUtEvU30hBxB5WOyr7_71koaNr1eRF8VNLQl5QBONreh17gaVKcJiQcZ-jZhbJh3kXPw2fJ8db7F-XItB8IlhAoGvR4TGisZ_VWLB3Yf0dSJqsfC7f98pOH9xrT04L4UUgdjTkHbm3X2W64lqpR8iVZzPDKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای زن دعوت شده به صداوسیما درباره ترامپ و نتانیاهو:
ما میخایم با پول حلقه های ازدواجمون طناب داری بر گردن نتانیاهو و ترامپ بندازیم
درست ۷ کیلو و ۲۰۰ گرم طلا به قاتل ترامپ جایزه میدیم
ما میخایم خون بر شمشیر پیروز بشه
از مامان های محترم تعهد گرفتیم و به مقدار توانشون طلا کمک کردن که به قاتل ترامپ بدیم
از ارزشمند ترین دارایی هامون می‌گذریم تا ترامپ کشته بشه
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/71485" target="_blank">📅 21:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71484">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🇮🇷
۱۰ دقیقه پیش، نیروی دریایی سپاه پاسداران یک موشک کروز ضدکشتی را از سیریک به سمت تنگه هرمز شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/71484" target="_blank">📅 20:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71483">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dcbed492f8.mp4?token=eTLn6Hj7gOqY8zR8yjj8Td0dAQ0RQBLx5xrJynfl3lpVz7wAN__6CE59Z2-esQixir0Q2onEtFwKlaDe1zdIGOru4fXsixxVJ87Uc__LpO_Atpnn6c4hUxRzcp-S8Z04HoY9LiEq_zqSdUR_b1l40whAiLGZBw6B1oBc2MoiNYrtyDivtsqXWpAty9dtrZ_9HH0tz9EHFbZ4ztyZIm__nwfgjXl-Eh3ZX_3AXW4j1_Dn2z8GM1V_GHlJCu1ge7LALdCtpiCVQ50xiP2oGHKVc1X1TDkh1yqgm14LaO-RPntWJHHwimcaYrMO-tge0HnNqdWAwTeA7cKefSTA7z56Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dcbed492f8.mp4?token=eTLn6Hj7gOqY8zR8yjj8Td0dAQ0RQBLx5xrJynfl3lpVz7wAN__6CE59Z2-esQixir0Q2onEtFwKlaDe1zdIGOru4fXsixxVJ87Uc__LpO_Atpnn6c4hUxRzcp-S8Z04HoY9LiEq_zqSdUR_b1l40whAiLGZBw6B1oBc2MoiNYrtyDivtsqXWpAty9dtrZ_9HH0tz9EHFbZ4ztyZIm__nwfgjXl-Eh3ZX_3AXW4j1_Dn2z8GM1V_GHlJCu1ge7LALdCtpiCVQ50xiP2oGHKVc1X1TDkh1yqgm14LaO-RPntWJHHwimcaYrMO-tge0HnNqdWAwTeA7cKefSTA7z56Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
آتشفشان ساکوراجیما در جزیره کیوشو ژاپن فوران کرد و خاکستر و مواد آتشفشانی را تا ارتفاع چند هزار فوتی به هوا فرستاد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/71483" target="_blank">📅 20:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71482">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d66564850.mp4?token=DRd1yfApDCviEvb3XvYCi_p-bZ7O3UhTh6_7gKrGXp0juolXg8VCR5s-ucHx1qeomZAbQz3L9G6noZ3N_sPo3NL8gdTemN_-rwx_mj3azM0eFUmr2jC1aTJBYhe5-LXmXlhRWjCociZN2lFbSXHbyGH6F2CGQEtCHhYwXU4C1HNz0sO2FgZGYVr9H_8G7Ae2fYcwkzC6oljt9pZ4Clp7Im8RO8xuJJ-3lICa0IEN3CrnIoz4GGffUmxka_cnvDI1LoTjjRk6KGiMm0eFCeqjITNwdOslU9b5MZPXyXHmWeci90fyoYGT16Zie815_6UEIlNuyP8sQhNX1OTnwkX0dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d66564850.mp4?token=DRd1yfApDCviEvb3XvYCi_p-bZ7O3UhTh6_7gKrGXp0juolXg8VCR5s-ucHx1qeomZAbQz3L9G6noZ3N_sPo3NL8gdTemN_-rwx_mj3azM0eFUmr2jC1aTJBYhe5-LXmXlhRWjCociZN2lFbSXHbyGH6F2CGQEtCHhYwXU4C1HNz0sO2FgZGYVr9H_8G7Ae2fYcwkzC6oljt9pZ4Clp7Im8RO8xuJJ-3lICa0IEN3CrnIoz4GGffUmxka_cnvDI1LoTjjRk6KGiMm0eFCeqjITNwdOslU9b5MZPXyXHmWeci90fyoYGT16Zie815_6UEIlNuyP8sQhNX1OTnwkX0dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
صحبت های عجیب
پوریا بختیاری کارشناس اقتصادی در مصاحبه با علی ضیا درباره ابراهیم رئیسی:
نزدیکان رئیسی گفتند که حاج‌آقا خودش اقرار کرده که اقتصاد متوجه نمی‌شود.
بعد گفتیم خب، یعنی باید برای رئیس‌جمهور کلاس اقتصاد بگذاریم؟
گفتند نه، کلاس اقتصاد که نه؛ حاج‌آقا ذهنش می‌پرد و خسته می‌شود. بیاییم موشن‌گرافی بسازیم.
ما یک تیم انیمیشن آوردیم که برای رئیس‌جمهور مملکت کلیپ‌های اقتصادی درست کند. قانون هم گذاشته بودند که هر کدام از کلیپ‌ها بیشتر از سه دقیقه نشود، چون ذهن حاج‌آقا می‌پرد.
ببینید چقدر این موضوع تلخ و «دارک» است که برای رئیس‌جمهور مملکت و بالاترین قدرت اجرایی، بروی انیمیشن درست کنی تا بلکه اقتصاد را بفهمد!
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/71482" target="_blank">📅 19:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71481">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90c5de5a1.mp4?token=bSB7EfwPNLj5-TpCLOqO5lKNIh8PEkLefGONx51sdmFdkUBr_iEGP9omqZTG1l6qBrw7vVY2JruTW1mudHBKwKb-As9ly0BNIn_DcOeq62oyLqw_mxE13zyLTiW-IzkIZx672_NZnNnmtDMy5pTza83MjDjYaLMXhzLevFzcGAnDUiqsn0rVFoqYZkEcg0YvPrsiIWGhnw0sF6Z6jjFsibofJPOcLaI5yF-kUpPfqR6LYnG6TRYdNVDKAB67f_fOTHxqY8lklU2Qa5cEso0sZnitpzMLez9EXw2CBaXwVIBBwMop2G-D5j307vKYcX4i7C3WIVb1Dkte0W_MTGFnSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90c5de5a1.mp4?token=bSB7EfwPNLj5-TpCLOqO5lKNIh8PEkLefGONx51sdmFdkUBr_iEGP9omqZTG1l6qBrw7vVY2JruTW1mudHBKwKb-As9ly0BNIn_DcOeq62oyLqw_mxE13zyLTiW-IzkIZx672_NZnNnmtDMy5pTza83MjDjYaLMXhzLevFzcGAnDUiqsn0rVFoqYZkEcg0YvPrsiIWGhnw0sF6Z6jjFsibofJPOcLaI5yF-kUpPfqR6LYnG6TRYdNVDKAB67f_fOTHxqY8lklU2Qa5cEso0sZnitpzMLez9EXw2CBaXwVIBBwMop2G-D5j307vKYcX4i7C3WIVb1Dkte0W_MTGFnSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین پایگاه دریایی نووروسیسک روسیه - بندر اصلی باقی مانده ناوگان دریای سیاه - را با حمله ترکیبی پهپاد و موشک در طول شب هدف قرار داد.
لیست خسارات تایید شده قابل توجه است
؛
ستاد کل ارتش می‌گوید سه کشتی جنگی (مین‌روب ژلزنیاکوف، ناوچه حامل کالیبر، دریاسالار اسن، و کشتی پهلوگیری پیوتر مورگونوف) به علاوه انبار سوخت مورد اصابت قرار گرفته‌اند.
اطلاعات و OSINT اوکراین، ناوچه دریاسالار ماکاروف، یک کشتی موشک‌انداز بویان-ام (غیرعملیاتی ارزیابی شده)، کشتی گشت‌زنی واسیلی بیکوف، چندین قایق موشک‌انداز و دو رادار دفاع هوایی در نزدیکی گلندژیک را اضافه می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71481" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71480">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71480" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71480" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71479">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_e5uirCwqzEoGKWdtF6N2iP80_3F9-qMqQSAuudPoh_T00KLw8IZ9FQicRrCmBNtkznmJEedqDCQ4Q95PnpUYnyLMO6XDTf-7PLF3R_J-z0_c1qJZStKfkrk55XbVIksvyVVSlaZp_CRAEOGjVGS5DBmrgi20RMP9dEsLlbg6iZSOUhpW0HFwlUFwJmLkhJBwQTlA73hBGpuqs2q5GwbWaNHbsktdLAdcKMW_D3QIiQDNsg3GAJnZM2fYUlbneMFBBLRbat2xtcAEg7rtnt4DHKZT0CHHctoKF0nzyNOG9L9PIhNyWEqnr1ltidsPzR4X_nisi-Rud3SZJdtHG1JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71479" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71478">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0Ag_xqF57MU1i1GM8YrPT0oQen1HdOejawo2-6RwUZzI06dIlCiboCj1uzI89wdmjARV_d1B0PZy4II0gji66YjCVEknn6GWFDzWm34v6h8sNuZfIszLaW5v028J3DUCOhSaNvpHGVvPrL7NqW-IFoNt90HJxQJQFCSaTbddFjkBAeNHNoA-8uXvn4TNKAApDFCBwUEi-ya8376S8BAT1yG0c79wjyfQRDN-D81gm32R_lzWGrJiTu2ephZEj-KHh_scS8r8eL5Sk-d6t1sm6wAmynlgyURKfzJhJCszX8r5iRBJ4jvZxujM9-bfik_yEVE1bJjTgU1Mw143605WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
می‌خواهم برای رئیس‌جمهور دونالد جی. ترامپ، خانواده‌اش و مردم آمریکا آرزوی «شانا تووا» (Shana Tova) داشته باشم؛ سالی نو همراه با شادی و سلامتی.
در طول سال گذشته، ایالات متحده و اسرائیل با یکدیگر به پیشرفت‌های تاریخی دست یافته‌اند. ایران و محور شرارتِ آن، ضعیف‌تر از هر زمان دیگری شده‌اند، در حالی که اتحاد میان آمریکا و اسرائیل قوی‌تر از همیشه است.
من به رئیس‌جمهور ترامپ بابت اعمال محاصره علیه رژیم شرور ایران و فشار اقتصادی بر بزرگ‌ترین منبع بی‌ثباتی در جهان، تبریک می‌گویم.
مردم اسرائیل در مقابله با نیروهای ترور، در کنار مردم ایالات متحده و رئیس‌جمهور ترامپ ایستاده‌اند.
در سال پیشِ رو، ما همچنان به تلاش برای امن‌تر ساختن جهان برای همگان ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71478" target="_blank">📅 18:49 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
