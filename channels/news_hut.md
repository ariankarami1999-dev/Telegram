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
<img src="https://cdn4.telesco.pe/file/FkoP_aIeIL4_-_inYPZro2KkX3opEAg21gfjMIaaHHMqWBonI0wH0NP7B1zMp9_tXARGNQLpQBLhpn8-vBOAwLZ1aGwwmFjStYdT7Ojt1pJias0tSQmw3qUZHuM6ax2iPaGj01C9cAX-3EdnCWYbkSH3AAoyKdgWRKdxJca61ijaFJtRyCvS83xET_e0hk0Jt_s4HmLIW99JH6RzpIrlJoF5KQM6TdfnzHjoUX5u7GqxpP8_E_ifu9k_w-Zv66zlX49xblAQJnVD_BxIABhHXMaUAvSxqSs77j0CHIjzii52kUIcOBZvE002_HJgdbEh8RIlT-NkM6M5WcmYOWfjEQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 216K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 12:04:43</div>
<hr>

<div class="tg-post" id="msg-67130">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lV7ONs_qKNoluYCc1YrJ3fN-7NvMxgM2cBTER6_shzy4WKvqFR60BOwAdvlTGSbHvxkm_5szMZ2dbEqXrPeeiviYWddrH3EfLPybmhRjQBe7NUF7MBcYI85IN-Y8vFrCO0vP-qXy-zybU4Iau-Db8dTkfqRgDYJADepp8f7_L6062wZPAkQB83S4ouGNF_ipAkTxpsBi1fF4JK8AxE0YVygEWWzzAVz4JvQikkgFwT3YVTICMePYIVLlL6PMkcszhPVhlZ5ROhaIknmHhUAXC8S0odnIoWU16kHH0ZOxTf39YehlevlXmz8LC2xQDZBWkh1rz9YTpJ3Xq4Ef46fW0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pe6NBDFT2yhxoGK7f83jXn8gI3ckx1I9MsZNrl6MKVVKkQBv4x8zOAtOYbAIQ-YApJgJMmBTz5EXWutPO2wtyx68t3Rrifgeh3apVQc7mu0OKuLl1_4j13D0EDClaXbiPazxRHIhLAej0ldivN9Qdy8KMIwsaSbgYeKYyUlOukAHs1yUAfJjcl1gtmcNseBppNNz3-8yFjxDcFZlCW4uh6ML8BKBXlDSasQeJrwo1UvJfPYbqvzjRjSnnbUW1gNizMifDJ0VxLl2YqAIHou5XLj4p6JHk7qY790etdwsAL53zAMdF1tEAEZNfRcmcIooKAkf1lK4FiUyyGWu60WY1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=AuyyZ6F8vL4fwJzqG5-a_VDEY1NOtGiiEa5gbOAlBUeSfJdEVjMwVLPy84UoTLD4qN97kwmLpHf_tgNPI9g7gJhvcZ2g9GUgInGeg_REiIDpvDPmEAN_TY5yJwjLh9OsarkitP_6Js5wJ6fW0--HwDcd8LtPeJ33GdswLeReNM9JPygcVPC3_TWBA42VbrU_50MJhox9rfiCLhvhJgXjVcRDXEs0jYVVTR1LyxVzcCRQrL7CucVZKqkcf0w87VZvJUpgO1G13csVxGt4jGup0ICvt3dCslFKtYSox9_XOkq4s6sxG6Ep47jcbU-HRyQ_AW9sDukqOMPM2TOtPg_aLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=AuyyZ6F8vL4fwJzqG5-a_VDEY1NOtGiiEa5gbOAlBUeSfJdEVjMwVLPy84UoTLD4qN97kwmLpHf_tgNPI9g7gJhvcZ2g9GUgInGeg_REiIDpvDPmEAN_TY5yJwjLh9OsarkitP_6Js5wJ6fW0--HwDcd8LtPeJ33GdswLeReNM9JPygcVPC3_TWBA42VbrU_50MJhox9rfiCLhvhJgXjVcRDXEs0jYVVTR1LyxVzcCRQrL7CucVZKqkcf0w87VZvJUpgO1G13csVxGt4jGup0ICvt3dCslFKtYSox9_XOkq4s6sxG6Ep47jcbU-HRyQ_AW9sDukqOMPM2TOtPg_aLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر منتشرشده از پایتخت ونزوئلا، آسمان کاراکاس را در زمان غروب با رنگ سرخ و نارنجی پررنگ نشان می‌دهد؛ بر اساس‌گزارش‌ها، گردوغبار برخاسته از زمین پس از زمین‌لرزه‌های اخیر با پراکنده‌کردن نور خورشید،این منظره غیرمعمول را بر فراز شهر ایجاد کرده است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/news_hut/67130" target="_blank">📅 11:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67129">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c160c90364.mp4?token=HrR_Th6BESep1Hn07yHjFKiQgqboRkjVs0-5mso5Yg15ilqk9ko5XNCkXJN5sVrUctmI3QayUXdK-Ylq5KaZIsSrYs87XbmjPLxETkxWvc9f-DLs06DyGseLWxti56cIa7ZxlXlzR4SsMinHMiXqB7YtsonXlqDZ0DXFotGEHgLMX8xDECezdGEIIDeRWLM2h0b_UVLNe0L9iYjdn6BQP-AKrF-fO2zYp03_Z_O_RvvagRO1T2KzOFhlO1DgYix5w8uieF77c2eG_sy6Av4yHzoU79X1f1Jkp84F4AsOpGA0SC1uKz0dnnmgZ0cHuFTr67MWcxoJw3f7PbrIdciV5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c160c90364.mp4?token=HrR_Th6BESep1Hn07yHjFKiQgqboRkjVs0-5mso5Yg15ilqk9ko5XNCkXJN5sVrUctmI3QayUXdK-Ylq5KaZIsSrYs87XbmjPLxETkxWvc9f-DLs06DyGseLWxti56cIa7ZxlXlzR4SsMinHMiXqB7YtsonXlqDZ0DXFotGEHgLMX8xDECezdGEIIDeRWLM2h0b_UVLNe0L9iYjdn6BQP-AKrF-fO2zYp03_Z_O_RvvagRO1T2KzOFhlO1DgYix5w8uieF77c2eG_sy6Av4yHzoU79X1f1Jkp84F4AsOpGA0SC1uKz0dnnmgZ0cHuFTr67MWcxoJw3f7PbrIdciV5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌نویی
:
خوشحالم که بزرگان دنیا یعنی آقای مورینیو و
تریلی هانری
از تیمی که من ساختم تعریف کردن.
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/news_hut/67129" target="_blank">📅 11:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67128">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=XPPz-XaFocdDCWZCoKI53mfbjs1UUm2pyzv4WLUdz8pceDsy6ibceWBkcRd_0yvo0LqbkzOCkBFQx5kKLRZKoDT8KnDCsA1N2nWWRSqIzEY93B-n2n7ENSMSKqYqTfSluD2NlhEwFvKRUxlo44ZtdpoZ-VHMfjzC_H-p4GlA1Bxku17a6gfJi5L50Dw0Gn_YDiIi_uK_0gOi2peXWu0mAUcf8WJCUWOnSgpyW8xbDeFeniYn4ufDDi7freiTuATU1rmQSENDnXQx2HlckNwEIZL4J2BGi4ZIsK7O8qWkNLIa2uUZgSxs8ErsS5Ff0jwES8UHpboC0zI_47N1NUBw8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=XPPz-XaFocdDCWZCoKI53mfbjs1UUm2pyzv4WLUdz8pceDsy6ibceWBkcRd_0yvo0LqbkzOCkBFQx5kKLRZKoDT8KnDCsA1N2nWWRSqIzEY93B-n2n7ENSMSKqYqTfSluD2NlhEwFvKRUxlo44ZtdpoZ-VHMfjzC_H-p4GlA1Bxku17a6gfJi5L50Dw0Gn_YDiIi_uK_0gOi2peXWu0mAUcf8WJCUWOnSgpyW8xbDeFeniYn4ufDDi7freiTuATU1rmQSENDnXQx2HlckNwEIZL4J2BGi4ZIsK7O8qWkNLIa2uUZgSxs8ErsS5Ff0jwES8UHpboC0zI_47N1NUBw8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
سازمان انتقال خون باید خون‌های زنانه و مردانه را از هم جدا کند زیرا قاطی شدن این خون‌های نامحرم با هم در رگ‌ها موجب ازدیاد گناه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/news_hut/67128" target="_blank">📅 11:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67127">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d22600661.mp4?token=Y9cuVlUYZ8k2gseV0n-cjZbHl4dLBFE_2B4ns5TWMkKfiigtMJN8Rvikw5nK906QiK2x5kcbhpRI_mLqlqK9iK3oBKRPMr4qfWquijG396DhskQ75aljSMU2IrPacrU5DuypR21WcwbCXPrxQRPd51TKV0EdesPO31m4UC9e-2n6xjkDeTwZepXajlDTK1vYCY4UP_nZscnslNL0xa6eOWPrGJnzN2kv8aj7tX1CdDRJhsLHYOQ-Q4KNe_8KtfOQ5FxdxNGwU8Cd89e-x1xYIkDBKpurI2erLSESjgMeLNZi5Ye6ytixZMeqIXtLNxbBBIu43ZgzC-g86NDd7krU2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d22600661.mp4?token=Y9cuVlUYZ8k2gseV0n-cjZbHl4dLBFE_2B4ns5TWMkKfiigtMJN8Rvikw5nK906QiK2x5kcbhpRI_mLqlqK9iK3oBKRPMr4qfWquijG396DhskQ75aljSMU2IrPacrU5DuypR21WcwbCXPrxQRPd51TKV0EdesPO31m4UC9e-2n6xjkDeTwZepXajlDTK1vYCY4UP_nZscnslNL0xa6eOWPrGJnzN2kv8aj7tX1CdDRJhsLHYOQ-Q4KNe_8KtfOQ5FxdxNGwU8Cd89e-x1xYIkDBKpurI2erLSESjgMeLNZi5Ye6ytixZMeqIXtLNxbBBIu43ZgzC-g86NDd7krU2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر ممدانی شهردار مسلمان نیویورک درباره مرگ خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/news_hut/67127" target="_blank">📅 10:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67126">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=S5FKpF2e0wZrCyoh2hk-nFidlGcWn9FDIUX4ARxifPP0pZdGY3EWWVl7hM4kXKCDoSfkeJpQoJiG7O1p-EZxn_mJp3xYLBJP_KOvSSzzZcXJFYVA4cW68GotIPdSZvxUl33pJuyu2DH5d3hNuUxAB31VEOsCqs7xwEe7DRdsqcqdN_pWX4DBY3-R-0uHuendPCOmnjuxTJUF7mCPUFiIkfNp1oOBru8_uG16dBrmZAVkucnmn0KhxCjtUNFqdcc9FSSkODnPoMKOjz497kJ_-MnzbnASY-qIje6Egsr_MfKwkWnrXTojvpvwf9DUiEq58n7nOARx_q8le4Wwc_IHNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=S5FKpF2e0wZrCyoh2hk-nFidlGcWn9FDIUX4ARxifPP0pZdGY3EWWVl7hM4kXKCDoSfkeJpQoJiG7O1p-EZxn_mJp3xYLBJP_KOvSSzzZcXJFYVA4cW68GotIPdSZvxUl33pJuyu2DH5d3hNuUxAB31VEOsCqs7xwEe7DRdsqcqdN_pWX4DBY3-R-0uHuendPCOmnjuxTJUF7mCPUFiIkfNp1oOBru8_uG16dBrmZAVkucnmn0KhxCjtUNFqdcc9FSSkODnPoMKOjz497kJ_-MnzbnASY-qIje6Egsr_MfKwkWnrXTojvpvwf9DUiEq58n7nOARx_q8le4Wwc_IHNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
نمایشی که قراره بزودی از عرازشه ببینیم:
@News_Hut</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/news_hut/67126" target="_blank">📅 10:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67125">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hK2aQlTYUkQ_jzp1RkSUQasDL6u4pDMvuvxakwE7cyqDwKYPAbIgR013NB1epKLAUC2IsaENi2wI8cfdKVojUTNn1c-4Jyif2_lrPVLS5ZDHS-naEDVPenNHTCondPFbR-Ej9EckYh0gZHMdBpZBnJctCP-PtmMtrmq3pT_IpngrhKF78nZbAuith9xt2uUm90s3xJZsQPG_g7hZNblqH1BnRGULl_-zciYr8fM9AJZdp0NnH3Q26Fodg8s68lB1vjcyEJXdOdXWYn3ASuRPulDQv4tpvKLRRNW1QPC100btOzkxS74oB9FZNQGvbveFZ5GI7Z2FyULTqJfO_-g3jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
به گفته مقامات آمریکایی آشنا با این بحث، رئیس جمهور ترامپ بازگشت به جنگ تمام عیار با ایران را بررسی کرده و در روزهای اخیر چندین گفتگو با وزیر دفاع پیت هگست و رئیس ستاد مشترک ارتش ژنرال دن کین در مورد حملات بیشتر داشته است، اما تصمیم گرفته است که فعلاً به مذاکرات دیپلماتیک ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/67125" target="_blank">📅 09:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67124">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOte9Oa4iMxQ79MGqGintt9rPnh6Q47wsLREXK_wXwT-LFHIhj9AOzDZiVIltphpRoFYY6Gnt1vwf9kBMetUKy2FYnu1thQOBuGQ6qSKMMX6jotRT5m8sXpCJxFE0_3vHC1of3agoTPrB56xkMp2UJxSq45vH0LayGmL7HQGSRbELIhO4dr3nKBdcoSr02kxj1Y0kwbKzBmxvQVIgDtrpjR9FH5Uvqw9LWkqC-5M6bh1odavmOYcyFGAMnJRVYxIfVJHasmG2Aqv07eHQxHFRhPCcs_8xJ3nHZlHSdM0e2XpyD-G3WolbAS9hVmW60YMn-1NqkPkUOr3lXZ2Ibz1KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
فرماندهی مرکزی ایالات متحده:ناو آبی خاکی USS Boxer آمریکا شامل ۲۲۰۰ تفنگدار دریایی وارد منطقه خاورمیانه شد.
گروه آماده به خدمت آبی-خاکی Boxer (ARG) و یازدهمین واحد اعزامی تفنگداران دریایی در حال حاضر به عنوان بخشی از یک استقرار برنامه‌ریزی شده در خاورمیانه فعالیت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/67124" target="_blank">📅 09:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67123">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/67123" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67122">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jIEHIdySgO72RJzFnrbD_UUe8aXo1UoTMTJ6Vnwnz_BZRdwQfWUWSpgg_1QL9stERD0MdRPPeYAx2JDg0kd4hRqKiGqhDB73ceZZDwPjZXHLIKW7Jo0ZERfwZfwMOWfVXe_9zcN-0TUCKWw_PZD5m5lVszS8AJZHiaQ3aVfM05OjATLIXYgu3OFVUpgkukdrJ2G3naC-wMFf-qKhPfUnR8LuQ0nwiTrU69TOBtwq_t5wfSh51E4QsF88cYxAU875n5kHVfIBWV7i2qdWdnFXVZzKp4LyRIuqa3zOZrHVytai18Vw8f8Jcbgc_JooIeBlgNB_LWIf7HiYvi58Oof8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/67122" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67121">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=NOqShHzu74iMPGBJ79thZcfbE1vB2X_ej3iYGMljksMV_IpZOHd4qht7A0-dnUbjFzOric9uWrcWRasd_FxFoGOYrfuPmOby4tv6uBIOXZlJq63azGBKfGMG4vb7DCr4IX9Cz827rnv4dbODlkRXAJ5IMPewfI3qg2lWy1BkyPkMx9nmREn__twy5TFR3Mgo40GCdJGVuTTQTw8Z7NXB-EknzbL4y5DMJyH8EwbsZSojvDlvWiF8nMrbbtJHCyyzgjL1nosWU1xnmkU1ROW8R_P9iTXtcYx-bOgWclyYai4AGXQ-86d9BhoiFYSrpjGrtnEgta-GAZueCgKjfnQ4ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=NOqShHzu74iMPGBJ79thZcfbE1vB2X_ej3iYGMljksMV_IpZOHd4qht7A0-dnUbjFzOric9uWrcWRasd_FxFoGOYrfuPmOby4tv6uBIOXZlJq63azGBKfGMG4vb7DCr4IX9Cz827rnv4dbODlkRXAJ5IMPewfI3qg2lWy1BkyPkMx9nmREn__twy5TFR3Mgo40GCdJGVuTTQTw8Z7NXB-EknzbL4y5DMJyH8EwbsZSojvDlvWiF8nMrbbtJHCyyzgjL1nosWU1xnmkU1ROW8R_P9iTXtcYx-bOgWclyYai4AGXQ-86d9BhoiFYSrpjGrtnEgta-GAZueCgKjfnQ4ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
کریس رایت، وزیر انرژی ایالات متحده:
ایران هنوز به هیچ وجه همکاری نکرده است.
جریان نفت از طریق تنگه هرمز به لطف ارتش ایالات متحده است. هنوز هیچ همکاری از سوی ایران صورت نگرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/67121" target="_blank">📅 02:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67120">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLPeW2ziJY8lR4naMS2QP14B8XHhya1B8hvm63qIDES12IZlR7OL_O_d9egn-QoHiINYaGf0kaFXc4uMCw8w_kMx-5732RX0WKheZYhD1-tyXbfiCoFqB2JbQjlQoVZi7JTBXgb4oypF4d3CZ2KD30-NKtIFACypdsNZenvBmHwlIhGGncTrpncqY_kVT7t3JB8zCQHvHFsqUISc-4kETXpSe66rPhXKA5nJBesKqOwaSpY_LMU6agSHNrwfuhqxWzqn9azin3hLIqF_1liAPFk3hOOhsSJMNoqHAAnZH4PUJXkvmhhNuDnbZ_sQWDrV2EOj5d5y4YuX-WnMnhcJMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر منسوب به تابوت علی‌ خامنه‌ای و خانوادش
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67120" target="_blank">📅 01:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67119">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=DLRFM1FHaro_di4LzcA65twXCeNbca5Px53QaJua5K6zWhS9rsMFRJ4sg6o6E_D-wMP2a3TL-skVUyciM-D1UIJH7nIHM1cL5eEXLVDUQztfshJLrhRJUFQWp5afPRBqPBJXI4MQeuc5lD5mAASK8keSWM-BMD8qkXqTpuqVMrtGP_8IjLwR-K-lC8GSjAtylyKguQEtMf8QyuWQ7-bdG64znrSOyanLZREulwzrScXP2AzYuFtlWgUsUeBwiPcb_UdCerwlQBY0vivhNXNkCxmmdRsSyk3wf4rJ_WhyK_FXLsMgIzFpuNLmmzyYr6GH_y9hUWa42BwIOXHZAJrOrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=DLRFM1FHaro_di4LzcA65twXCeNbca5Px53QaJua5K6zWhS9rsMFRJ4sg6o6E_D-wMP2a3TL-skVUyciM-D1UIJH7nIHM1cL5eEXLVDUQztfshJLrhRJUFQWp5afPRBqPBJXI4MQeuc5lD5mAASK8keSWM-BMD8qkXqTpuqVMrtGP_8IjLwR-K-lC8GSjAtylyKguQEtMf8QyuWQ7-bdG64znrSOyanLZREulwzrScXP2AzYuFtlWgUsUeBwiPcb_UdCerwlQBY0vivhNXNkCxmmdRsSyk3wf4rJ_WhyK_FXLsMgIzFpuNLmmzyYr6GH_y9hUWa42BwIOXHZAJrOrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
بخش سانسور شده صحبت‌های قالیباف در صداوسیما:
قالیباف در قسمت پخش نشده این سوال، می پرسد: خریدهای قبلی این اقلام که در طول ۱۵ سال گذشته انجام می‌شده، از کجا بوده؟ آیا ال‌سی اینها در لندن باز می شد یا نه؟ چرا الان مهم شد و این حرف‌ها را میزنند؟
🔴
چون نمی‌خواهند بپذیرند با مجوز اوفک صادرات نفت انجام می‌شود.
​
🔴
این قدرت جمهوری اسلامی است به آن افتخار کنید و پای آن بایستید. این سند شکست آمریکاست و ما با عزت آن را انجام دادیم.
​
🔴
گویا حداقل ۲۰دقیقه از این مصاحبه پخش نشده که نکات مهمی را در خود داشته است.
​
🔴
برخی قطع صحبت رییس مجلس را با بازگشت روزی‌طلب به معاونت سیاسی مرتبط می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67119" target="_blank">📅 01:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67118">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=pCrQtz0z6bWFIViSiYCSRnasJoLw1bQYNiRjqujliyT6OUuVYi3Fatec6c6NW1pu9fvKiZHgxMT0ZAmW6Y11vE1HyjA4hR3hDOySIc8hfD_VABIR7x-CKZC_kwPzxovkQ6oIHYxXEGcnRTBfQEPSZrp6U74DBbCY_L0vm2DlU6Xm1Q3MMQK9oEyyy3kz2cG7wtwTnxAdqHeVKzKG4f-p4hA2S9SEsGSPOSoNHO1dblpBjc4X1DmRV0q0J0-S3pqzuBDGp-A597TiU5THn_lPNtgM5DfBqqYds_MN-SYCP5P3cQ8L2vrnetkCRrSiBM8LNYjhs40RhZP8jKhss2TA3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=pCrQtz0z6bWFIViSiYCSRnasJoLw1bQYNiRjqujliyT6OUuVYi3Fatec6c6NW1pu9fvKiZHgxMT0ZAmW6Y11vE1HyjA4hR3hDOySIc8hfD_VABIR7x-CKZC_kwPzxovkQ6oIHYxXEGcnRTBfQEPSZrp6U74DBbCY_L0vm2DlU6Xm1Q3MMQK9oEyyy3kz2cG7wtwTnxAdqHeVKzKG4f-p4hA2S9SEsGSPOSoNHO1dblpBjc4X1DmRV0q0J0-S3pqzuBDGp-A597TiU5THn_lPNtgM5DfBqqYds_MN-SYCP5P3cQ8L2vrnetkCRrSiBM8LNYjhs40RhZP8jKhss2TA3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
قالیباف وقتی گفت توافق خرید غلات و گندم در ازای پول های بلوکه شده برای دولت سیزدهم بوده است، مصاحبه اش در صداوسیما قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67118" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67117">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640225b559.mp4?token=TOLrQ2YekB22RjdW-S9xtnFDgL68vefPgcuXaSWVJ_Wy5JfCOU3g9iJQpya-pDb4sapcuoneTy2Di2aL_eYyE_DnxT38R_lHTQjOUF0Pi7yDPI7Swp4S_J4n2bUewjRCZ3VIVAUXgdKnLPT1TI46t_K7spv7Va8YhT8xnJUtI5jIoGMSxs2kwwnTkDS2gBJ0iVKMLigbHNq_Pb0pFTc7MRSrwvvAgfwrpm5v4169vcZAXdtICr8MZxeQ3jLFimTpSNZua8jHCctlhLvDbfYRSRMlR7Chn1F5MPikGcw75BtS-MYY9O97X4UVQGbkYNPr_42IGJJLUnmssYSmIz3efA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640225b559.mp4?token=TOLrQ2YekB22RjdW-S9xtnFDgL68vefPgcuXaSWVJ_Wy5JfCOU3g9iJQpya-pDb4sapcuoneTy2Di2aL_eYyE_DnxT38R_lHTQjOUF0Pi7yDPI7Swp4S_J4n2bUewjRCZ3VIVAUXgdKnLPT1TI46t_K7spv7Va8YhT8xnJUtI5jIoGMSxs2kwwnTkDS2gBJ0iVKMLigbHNq_Pb0pFTc7MRSrwvvAgfwrpm5v4169vcZAXdtICr8MZxeQ3jLFimTpSNZua8jHCctlhLvDbfYRSRMlR7Chn1F5MPikGcw75BtS-MYY9O97X4UVQGbkYNPr_42IGJJLUnmssYSmIz3efA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
لحظه قطع شدن گفتگوی محمد باقر قالیباف، توسط صدا و سیما
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67117" target="_blank">📅 00:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67116">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e29288f186.mp4?token=VD8ZFjzLIQJ1S_ZpgZOBZv6LypkIZjZ3o0l0tcb127_0EizW1ymmdpdYxHeMCDSiamuWg3IOz9UDq4FmECFSzN7BtH0w52L42JYUXhpXQ7F7BrNVMD2FWYHjzzWQ2nAd9WpWycMSQJmwtBQc1zLEEMHqiTZl47-3Vw2tz3NywHC75ZHp_Hx94qqkMO_ewM8sfE2zVX4rkx5JlL0NzYlQplNG7F0_yhltsCtGDvEXTaOTLkmXjjeIns13Ip5SI6TrRLZaj2aMOolXJJuBRk0ROnJFbaR4FXjg_0uipN4JsRTDESIOuYDWv_nQxSgJ5fOIzZIVTS2WYCckiukwpjNt6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e29288f186.mp4?token=VD8ZFjzLIQJ1S_ZpgZOBZv6LypkIZjZ3o0l0tcb127_0EizW1ymmdpdYxHeMCDSiamuWg3IOz9UDq4FmECFSzN7BtH0w52L42JYUXhpXQ7F7BrNVMD2FWYHjzzWQ2nAd9WpWycMSQJmwtBQc1zLEEMHqiTZl47-3Vw2tz3NywHC75ZHp_Hx94qqkMO_ewM8sfE2zVX4rkx5JlL0NzYlQplNG7F0_yhltsCtGDvEXTaOTLkmXjjeIns13Ip5SI6TrRLZaj2aMOolXJJuBRk0ROnJFbaR4FXjg_0uipN4JsRTDESIOuYDWv_nQxSgJ5fOIzZIVTS2WYCckiukwpjNt6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
این خانم، عالیه نصیف از چهره های وابسته به رژیم جمهوری اسلامی، شش دوره بدون وقفه نماینده پارلمان عراق است، او در رقابت‌های پارلمانی چند ماه پیش گفت: «کاری می‌کنیم فاسدان از پنجره فرار کنند». حالا خودش به دلیل فساد کلان دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67116" target="_blank">📅 00:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67115">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e563023c29.mp4?token=mxOvuqvvf8KnMeZ25tJuqRFq3SKLsofQX1ArogW3QTRvZ5dv4--hyLjHXFVe_uKjAOY1vlqkIhYncRlXlWW4UCn_MGj5vCnYufM4LFstqD6xu84jN4i994r_EmQWWHaWngWFBcJhJtcxlkVRydPp_mXP_rLVSxEiDdN1rRRuKGxUeIvFskv5vLZfxHU9Q1RPRa30T3Fn3uys65pfxuSQDfwHfpWnud70RmVN6nEkXPxC8kPBZsIbnbK5E6lxPlBqocwqWc-HR38cyGQY3l6bCQqgAo7zCdvyHSxiVkvJ79sHeRIbfkpMw_KfIcsYox0e-3Q3z8mWl4N4EElq3LN_0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e563023c29.mp4?token=mxOvuqvvf8KnMeZ25tJuqRFq3SKLsofQX1ArogW3QTRvZ5dv4--hyLjHXFVe_uKjAOY1vlqkIhYncRlXlWW4UCn_MGj5vCnYufM4LFstqD6xu84jN4i994r_EmQWWHaWngWFBcJhJtcxlkVRydPp_mXP_rLVSxEiDdN1rRRuKGxUeIvFskv5vLZfxHU9Q1RPRa30T3Fn3uys65pfxuSQDfwHfpWnud70RmVN6nEkXPxC8kPBZsIbnbK5E6lxPlBqocwqWc-HR38cyGQY3l6bCQqgAo7zCdvyHSxiVkvJ79sHeRIbfkpMw_KfIcsYox0e-3Q3z8mWl4N4EElq3LN_0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سعید آجرلو از اعضای تیم رسانه‌ای مذاکره‌کننده جمهوری اسلامی در اظهاراتی در پخش زنده شبکه خبر رویکرد علی خامنه‌ای رهبر کشته شده جمهوری اسلامی درباره مذاکرات را اشتباه خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67115" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67114">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDwv2KQSR3uhiq-Vw_62tKvPSeCjZVsof6DyT8chB0Zq_rIMCZ6FbJ7hiGe9xow5yCMA0joDka3b8RzNb8nv51fxAZkwnM7leFkEiMk1N1QmAkDARWDNCLBIPiQtk4cfJZsrnRjqtQUC05r-chQexczEPv0pGLBdBJ69TSqaI5my18XLMuQIVJ0dTDj-JFewB-6ZVi88PpidHDfAlLf6pvjgBMpEMXIqzJz8WMW9T5t1HvTZ-CkFS8yHoe_hMcwN-a1EljzWnJLf3pCklm4DdEhGt5l7TsZTQC05UR_wnqfuX5ICSLbHProdZmTp_qstSRsm9oreZpA9_8wMEWvFiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌿
جدیدترین روش ترک اعتیاد  گیاهی
بدون درد، بدون خماری، با انگیزه‌ای نو برای زندگی
🌟
✅
ترک فقط در ۵ روز
✅
درمان کاملاً طبیعی
✅
بدون داروهای شیمیایی
✅
بدون بازگشت
✅
همراه با پشتیبانی روانی و انگیزشی
💚
بازگشت به آرامش، بازگشت به خود واقعی‌ات
💪
تو می‌تونی! ما کنارت هستیم تا دوباره بدرخشی…
♦️
جهت مشاوررایگان فرم زیررا پر کنید
👇🏻
https://app.epoll.ir/74570725
عدد 6 را به شماره زیر ارسال کنید
👇🏻
🆔
@Sahar77631
☎️
09923413672</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67114" target="_blank">📅 23:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67113">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSY7hxqacCNitGEG3Yy-8R8Pe3o0aEkJgPCGLfuqn2hE6XPhtZhR4Zbphn2TBWe3O_1mS9MCiJ1zzE44dcJ8a2kUlNAkKikUUjzBTT2n924O0TcoYtIusMsLbGdOte2N389PZd1iCTk9tGZ9YE-8EoR2NSMoCY9sjBa_TH22SKq5qlHpgK-D4aojndzxWLmvn9WvCC8wEwNQq-SCryCkLXTDKz5VzMZ1oIK4RUeBCdw2TjGQXsc48gtuL5rwp1FVFiHHZcfxq74BCfsSnMnTw2DgczTgMN9bfpodCYN-ZMCNi-7R9D4q12Lpv0Pp_G7eUpID424iOXuQELLhO_egq5Yxk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSY7hxqacCNitGEG3Yy-8R8Pe3o0aEkJgPCGLfuqn2hE6XPhtZhR4Zbphn2TBWe3O_1mS9MCiJ1zzE44dcJ8a2kUlNAkKikUUjzBTT2n924O0TcoYtIusMsLbGdOte2N389PZd1iCTk9tGZ9YE-8EoR2NSMoCY9sjBa_TH22SKq5qlHpgK-D4aojndzxWLmvn9WvCC8wEwNQq-SCryCkLXTDKz5VzMZ1oIK4RUeBCdw2TjGQXsc48gtuL5rwp1FVFiHHZcfxq74BCfsSnMnTw2DgczTgMN9bfpodCYN-ZMCNi-7R9D4q12Lpv0Pp_G7eUpID424iOXuQELLhO_egq5Yxk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دو موشک فلامینگو اوکراینی به یک کارخانه تسلیحاتی روسیه در ولگوگراد اصابت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/67113" target="_blank">📅 23:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67112">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=gNtp01Fj5iZE8lHjmaFEHPdExbD0vLLY07j8HGUllyZSRrEdd3byCgPZAx_3HMgbUdrg0xXhciFaoIucxlBpDkoO3N5vOHuhnJMCWGbTMctUfaDYn1MRgE4MIbzddA8HU1amMAI9eqTVdDqjzy5i8gaLxOx-Z16hNk7WNSatEA6WiWCoFOAb5eWL4U6nY_TRcwN3TJnEzfkqzoeu2l-aNcjLId_iJ7gNz6wgDwi346yJcuVT7fm-1WLzBUnzBwkajks5nOqtyD9tlySqs9g_PP6xOnuzhPaMifKINcoPY4NOVyiSjHiuWkyzL2HhVTR2G2gGo6fRXc_rfw6IFlI8DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=gNtp01Fj5iZE8lHjmaFEHPdExbD0vLLY07j8HGUllyZSRrEdd3byCgPZAx_3HMgbUdrg0xXhciFaoIucxlBpDkoO3N5vOHuhnJMCWGbTMctUfaDYn1MRgE4MIbzddA8HU1amMAI9eqTVdDqjzy5i8gaLxOx-Z16hNk7WNSatEA6WiWCoFOAb5eWL4U6nY_TRcwN3TJnEzfkqzoeu2l-aNcjLId_iJ7gNz6wgDwi346yJcuVT7fm-1WLzBUnzBwkajks5nOqtyD9tlySqs9g_PP6xOnuzhPaMifKINcoPY4NOVyiSjHiuWkyzL2HhVTR2G2gGo6fRXc_rfw6IFlI8DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازدید بنیامین نتانیاهو از منطقه امنیتی در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67112" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67111">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=nr0KPM5n_1384L_7R6NunEg767wDRtL_pnKmjEwOCuTRcZbmBh_S_S5GEspYeCDZRluAeP9Bfcuc9H6klWxLedNamKkfE8jiffyEjTENkjOLXgQ0_gdi1EkekEuF0UKsE9k6VkzvPwa-Ayo0NF8WmUlCVJ-yC6Sf8Y0FVnkv2gcG60vDwzvkjxlxOx-kfKFcy52Frydr7jqK17BDvMbOANg7byQCxwEl4LUVUvs6c97i4IsJY-OpIQk2YRZwG535fzCyJvqzKMnw7fn4WdjteuIEbw72hvd-mSlR_S9xVcS1tFCqsP0Qex6PpPjp7zfdySPsXD561liZQQLIjnKhmY_bDois8e3FSFS9bHMe-6cEJhcWCUPOCqoMVf_dXXCzS0NygQizVhGOh53g9zCrma25qh0bIK6p9qMScI3z6koBqAxbxOwx4GE9_krimxtHgY5DS1N85eUgpsv3k1bahV11YT_8SknCj9vNT3KUPQ0dhVdgzm82gtrY6G9btRBpm5CVyrs6bG25kxxSbCsONI8yXNzvuSi3Juv0DhN6gkblD4wtemkBSZx9panEmxtY_1XJ65fWvJ_5QXnGXzQ0Hn46VPhsxW4Swj0QoeNugL-si43Wth9H-wTNloLyrcSbXbyhyygxit-4WRJ1NuipzdNwQM9OwGGS69RAA3fm_Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=nr0KPM5n_1384L_7R6NunEg767wDRtL_pnKmjEwOCuTRcZbmBh_S_S5GEspYeCDZRluAeP9Bfcuc9H6klWxLedNamKkfE8jiffyEjTENkjOLXgQ0_gdi1EkekEuF0UKsE9k6VkzvPwa-Ayo0NF8WmUlCVJ-yC6Sf8Y0FVnkv2gcG60vDwzvkjxlxOx-kfKFcy52Frydr7jqK17BDvMbOANg7byQCxwEl4LUVUvs6c97i4IsJY-OpIQk2YRZwG535fzCyJvqzKMnw7fn4WdjteuIEbw72hvd-mSlR_S9xVcS1tFCqsP0Qex6PpPjp7zfdySPsXD561liZQQLIjnKhmY_bDois8e3FSFS9bHMe-6cEJhcWCUPOCqoMVf_dXXCzS0NygQizVhGOh53g9zCrma25qh0bIK6p9qMScI3z6koBqAxbxOwx4GE9_krimxtHgY5DS1N85eUgpsv3k1bahV11YT_8SknCj9vNT3KUPQ0dhVdgzm82gtrY6G9btRBpm5CVyrs6bG25kxxSbCsONI8yXNzvuSi3Juv0DhN6gkblD4wtemkBSZx9panEmxtY_1XJ65fWvJ_5QXnGXzQ0Hn46VPhsxW4Swj0QoeNugL-si43Wth9H-wTNloLyrcSbXbyhyygxit-4WRJ1NuipzdNwQM9OwGGS69RAA3fm_Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف: اگر می‌توان گره ای را با دست باز کرد چرا با دندان باز کنیم؟
🔴
کسی می تواند خوب مذاکره کند که برای جنگ آماده باشد.
🔴
مذاکره با آمریکا مذاکره با یک دشمن بد عهد است که هر لحظه فرصت پیدا کند علیه ما اقدام خواهد کرد.
🔴
ما در شرایطی با جنگ و آتش اقدامات تلافی جویانه ای را علیه رژیم انجام داده ایم.
🔴
خوب است ببینیم شیخ نعیم قاسم  و مردم لبنان درباره این تفاهم چه می گویند و برخی دوستان ما در داخل چه می گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67111" target="_blank">📅 22:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67110">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c10065584.mp4?token=EDGiCdzsTTxZnC_cDWJLIazQDoAhewA8PSzrFze0vSrJxoUgh_p9a-6f8j5tz5o1EQXdtyP61G7GqHxEksMXSr6E0jKbI0OcJyqvBy0gKIYkW_i6HA0V3t8t_7b3-9A1KTiOn4sfEaDuMEGWUupmp42D_V33sWqlZKLouSKad_Fn83sruQURpHjfTVNX9BvuIbrvq-07oBpgcLx8Pay6pUn-6aYdv9o5Cb_k5YOStDxmzsDvwC0dWtbVsW-pHtNElCv-d42q-CknzekB_RDwavlideFdW9dAgk6HXUsW-vagMZQltBMh3xCOkCqGQ8E6iPxDDJMrfUldHnl5dM_lPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c10065584.mp4?token=EDGiCdzsTTxZnC_cDWJLIazQDoAhewA8PSzrFze0vSrJxoUgh_p9a-6f8j5tz5o1EQXdtyP61G7GqHxEksMXSr6E0jKbI0OcJyqvBy0gKIYkW_i6HA0V3t8t_7b3-9A1KTiOn4sfEaDuMEGWUupmp42D_V33sWqlZKLouSKad_Fn83sruQURpHjfTVNX9BvuIbrvq-07oBpgcLx8Pay6pUn-6aYdv9o5Cb_k5YOStDxmzsDvwC0dWtbVsW-pHtNElCv-d42q-CknzekB_RDwavlideFdW9dAgk6HXUsW-vagMZQltBMh3xCOkCqGQ8E6iPxDDJMrfUldHnl5dM_lPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
تعهد ما نسبت به باز کردن تنگه هرمز و ادامه مذاکرات منوط به پایان جنگ در لبنان است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67110" target="_blank">📅 22:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67109">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
قالیباف:
غنی‌سازی حق ماست و خط قرمز ما در این زمینه مشخصه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67109" target="_blank">📅 22:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67108">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=POOQ-JMitB0WQORcxnHRvJIoevGIC58A9lwpzjwBMkck2wfaHOdaJJKblThRT95XbzBnT3lOpGMmKyxVfW8aiVQrPsU-C3shkNrEtQENkGWS1q3VTKy9eEmh1H7tu9TLXtgdvpzvMrf7feE9JskuCSO8cuVczizkZ6xzH9gQ-OuJHQzHUJN0OJft2yqOWQPr17Ji-1CNfIaeJKbgMKTE-ZLHUg9huVSnhHxVV5Shg9SVaggVHVR4bsZ1-6mVUrcN3JDejhM4ownEITFTFDwJ4jn3Q-2AcImMAebonpNlk3wCFrqcVNcs5dWWi_r_j9bZPJxIBW_GL79HyGrOW43o1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=POOQ-JMitB0WQORcxnHRvJIoevGIC58A9lwpzjwBMkck2wfaHOdaJJKblThRT95XbzBnT3lOpGMmKyxVfW8aiVQrPsU-C3shkNrEtQENkGWS1q3VTKy9eEmh1H7tu9TLXtgdvpzvMrf7feE9JskuCSO8cuVczizkZ6xzH9gQ-OuJHQzHUJN0OJft2yqOWQPr17Ji-1CNfIaeJKbgMKTE-ZLHUg9huVSnhHxVV5Shg9SVaggVHVR4bsZ1-6mVUrcN3JDejhM4ownEITFTFDwJ4jn3Q-2AcImMAebonpNlk3wCFrqcVNcs5dWWi_r_j9bZPJxIBW_GL79HyGrOW43o1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
اگر نخواهند در گفت‌وگو به تعهدات خود عمل کنند، آماده جنگ هستیم.
🔴
اتفاقات شب‌های اخیر خلیج‌فارس را نقض آتش بس می‌دانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67108" target="_blank">📅 22:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67107">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745f2de194.mp4?token=I2lrf2HwvEO3LL3tH-nqYcVFkWA7maaw5dVxP_6vLeWeXz2rhtrY9IOQ9hYtQ7zGpfjf-7jH7gBL3abENelJrQAxDa3JbzN1axXtxKb2u0tLSigI2crmcQor5uMs4Jm8fQZoKWybUKdq3_CT9HgFmZUxA5N04pJOWkBkWBx1dI4ySt4wDNpeI2NmZ-70Aek7zCDos04lkT9UsgMJxsrvPVN4NjaFNfEsy9y9tu07cw59ghbKnupoJBezZKrPsaKYG_NeMWOFW36BQ_iQucqC7Kpn-kocBc4Ng1ld4xVD3-t2VbkNfPlg1wDZdbni8DlraAmY8frH2yWeM_fVU2HJNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745f2de194.mp4?token=I2lrf2HwvEO3LL3tH-nqYcVFkWA7maaw5dVxP_6vLeWeXz2rhtrY9IOQ9hYtQ7zGpfjf-7jH7gBL3abENelJrQAxDa3JbzN1axXtxKb2u0tLSigI2crmcQor5uMs4Jm8fQZoKWybUKdq3_CT9HgFmZUxA5N04pJOWkBkWBx1dI4ySt4wDNpeI2NmZ-70Aek7zCDos04lkT9UsgMJxsrvPVN4NjaFNfEsy9y9tu07cw59ghbKnupoJBezZKrPsaKYG_NeMWOFW36BQ_iQucqC7Kpn-kocBc4Ng1ld4xVD3-t2VbkNfPlg1wDZdbni8DlraAmY8frH2yWeM_fVU2HJNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
دو اقدامی که پس از امضای تفاهم‌نامه، در شامگاه ۲۴ خرداد رخ داد، اعلام پایان جنگ از سوی نخست‌وزیر پاکستان و توییت ترامپ درباره برداشته شدن محاصره دریایی بود که از اتفاقات مهم تفاهم‌نامه به شمار می‌رود.
ما در حال دنبال کردن دوران گفت‌وگو برای تحقق ماده ۱۳ تفاهم‌نامه هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67107" target="_blank">📅 22:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67105">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gw8No68lp9wWVHExlGYMWIzRJ7U-Pmp38-lKUJagida2Ot8jJwTKr8IuxewJ38ehjCASkJfo1-q0gyKAxZPyXxidUpi-NYUAl1WdT7481L5KW-TYNbEi38kYeSnfgIFu3Bmfa5z29njpCXFRuOMCowInGA5kciSmfZjjfXcGW_LTUIAMGxLy9DweQWwZi6G24eMIX1qPsdCtGTzi2vb6wb2GYCjSvQhmvFqAmMXl-oSJNMDDz1C5XTh6ZNS5-05fdgDsugi1LX843keu64Okc504aMMC7ezFjmkJjhZON0R8zEYmPB_GRzV-o08FzlzuPA0Wkl-XYRk35ZAtKesKzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D4_JVxkOlUfZEp32xhM3-wRs-fAtZ-cUabDYhytdUWY1zIlxzUQadG1CFrt5IzWOfiy9kRkiystB_tAp8mHvUDpP0wQt-DTDypXB7dc3Tc0X1Xl-kUb62Z8pYJHNgfJ6m8mQXT1UA5v-AtZJrqoGfxvhZvWPeEuGqs6BxrxdFv0oWlo5Z7zsQQbVf2X0_267dAKjdy8IicDGqKK4paclgxuT5YAoPhuVKYjNxbcWJ11zsFQYHvuvZhlYcAqtnLUzEf6kW-mjTB2U76ZGWMCd5Bo1H31h-SCDcUBBsyEqSkJNsjjFsF9r6eTdQpNazkjhOxDQXzn-OdgGD6DUTQt3Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صفحه اسرائیل به فارسی:
چرا هر کجا این تصاویر به دیوار است، دزدی و فساد هم هست؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67105" target="_blank">📅 22:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67104">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Td2hmiswvxJZ9VtGAGzOvcUOqiQWR94zY3p1Rjsikp9aJHzwwH_nVjE4KSGaRGR04siKZVe4Kx3U1GxzcnpHOpdcAUqc5XjXUiQjobgabcCr-ZZOhHTFJs9IwhlTWtLwRoEedP7paXmbRtgTLSebhoHT_ADjnW8FZLWSeDae7Nr2iH57vBx4lfJ3dS64WTI8AotMRGfPl21gUn_irtUvwzDmFpvbhAb7YdA5EG-fC1UPljvPaEUSQ2kWQmX6Enk17tks5T7mpcxEL-QgCUtCZ0R-W5XmfYihpjYKZL_wuXv7RAkpvCmEYl_2-dLIhRRkFSWMNM-IECNm5QyG9BJZ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وال استریت ژورنال:
اختلاف نظر میان میانه‌روها و تندروهای ایران بر سر اهدافشان در مذاکرات با آمریکا، پیشرفت آنها را کند کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67104" target="_blank">📅 21:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67101">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_4azdXVDr0pyGRJaAtyVOk4b8bx2fQjCbk2xCgc_zgOkkSvstzTi1eDVex1yN1Nocpbb9VCsaMp5CfXegTZbPcsmcr2-KHxhiGZLUGIMGr5nw_H2d9g8KpxM9wZx-4StE68tO6FqZqcj-zkoZMK-qg6cqrZSXjRqWWkurZ40gsiFj12cIm4W9yxmzvyteKxqHbasb3OdRx89NSWWZOcu8h6jEmtGp8y0_AkyJsFb095r5tK5SX5pFktSy45XvTmZnQrYcxNfy2FBHKAfcen5P1pBI5pbjOGLXfMjwU2BZcl-kvCDsaGaoLYfq2a8sQiBX3fXI2H0YUxpvMCTQd2yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tpzyGq2Jvrh3NdSIyLNZTOp1s_Jh9N8K-Avawav1XTDNNrla1lzNiD8Og3NwVlsMHfciKx3MJyuzBejtxnjewjshEAcmELBv4UIc34TBwygztYrVZU6pD7I7hPKP-9-Uun--GUhfQUv7cVUQY5Nwthqz5lFzf8MzAMWUXGVwkaMdikF2pq4lLUWeHRk-j3c5TkzIL9nG9OLZyR5LYbYboqIZ4rpnn2BaEqiGpDcVPLdJziD-W2gEXuEmLa2gKc_haHDjLs9VBeXCfSmW3DsMGcwrc7W31eA3pMS7i37yiPwKnZuy86XX138qOiCuWMMsSZ6efv2Bmb-x3BFv4gNYWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bzvNKrYOm9f3NbUw7shrZtFR34D5dkYKHM3Mg8gn2k-a2K0lNZLcrjZOx2yNiZXEZWytAsLCSMjZDSn3csK-03mGgvXvTznZyq_HqqC6N7U9FABKxM7slUif0BOJFjtULg73Ns5ODo84tuHOkOa9FZjuJcBYfWrK6jN6xTRxE9c2dnBSbmb_yClG7D-ep-zceVdAAnWx8pP_xKa38kDp61Po_303WLAN9iIiz9-OiUD_3uhqBl_zaasmbJULSOTaL6AKBW-yrn1JbM6n2UovnAKCLbRvhTrQLBSqXLB6bd2K7ukn57RJVAVhalGM-Sr-kymKiF48BmyRF4blLNryeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سنتکام تصاویری از آموزش شبانه تفنگداران دریایی ایالات متحده در جایی در خاورمیانه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67101" target="_blank">📅 21:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67100">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=Jf71KIbGugXtlVk2Y6YKtb5HiveMEM9H7lR_ADYwwW4TIRFbe0V6jZOmhWw4Hb5zbxJH3pXKk-M8TnQ0EZIwUauYka3EmYCJIUfFfZBDYmv_Tv3CJ6Oo35OdoaKOy7ZiYpGHOWJDcUXhJVh4nGR-S_l27QVRlv9fhscPd5K-5aqdzO5CqPVSf_pPqO7yZF-cEr0zqHC6o0WK_Yw9-YFYPOR4uTn31BlzBSVxPSwQaqxUgdnpwmninipI-9-ER26cR2NNOa4S3GtJRSSSZRgKe7X0-nTWWsFwr2hK-S1D0XWy6X1hpYaHomtfFJ12aq3KjZEJxiiYJwVzpT6ZeLlZOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=Jf71KIbGugXtlVk2Y6YKtb5HiveMEM9H7lR_ADYwwW4TIRFbe0V6jZOmhWw4Hb5zbxJH3pXKk-M8TnQ0EZIwUauYka3EmYCJIUfFfZBDYmv_Tv3CJ6Oo35OdoaKOy7ZiYpGHOWJDcUXhJVh4nGR-S_l27QVRlv9fhscPd5K-5aqdzO5CqPVSf_pPqO7yZF-cEr0zqHC6o0WK_Yw9-YFYPOR4uTn31BlzBSVxPSwQaqxUgdnpwmninipI-9-ER26cR2NNOa4S3GtJRSSSZRgKe7X0-nTWWsFwr2hK-S1D0XWy6X1hpYaHomtfFJ12aq3KjZEJxiiYJwVzpT6ZeLlZOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه با مدیر داخلی بهشت
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67100" target="_blank">📅 20:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67099">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=oDf0FrnMwKiMarXul8_0sDh3oE0Djz-At7nmPc3cdEiE8w-5s5Ps2BjGyS-c_I3SY9gStq84lCwVxD1oi8Y-GqbWJUemROLkUX4GB26Sa9B06Q8dS-4UXyIvOKlqaTFoDb_G-S3FTLiw9BaIZVYj--sTi2YE7ZEqUgTL_Fsbc1uHQ-rY6v-h-ViPLoam3gMTObR-d3-W_0GujR6vgzKKQ3tk0sBF9-wjyKxCkgCAVnA4oXUIsWCFrdGlqbNoOipgK96Jf0J4dJLKj4TX_0-qQTeBHnUcO82rd7gES6Es8sIJnKfUSdEsXSHWBgHxD3S1017WeH0W461dpyVz1OrfSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=oDf0FrnMwKiMarXul8_0sDh3oE0Djz-At7nmPc3cdEiE8w-5s5Ps2BjGyS-c_I3SY9gStq84lCwVxD1oi8Y-GqbWJUemROLkUX4GB26Sa9B06Q8dS-4UXyIvOKlqaTFoDb_G-S3FTLiw9BaIZVYj--sTi2YE7ZEqUgTL_Fsbc1uHQ-rY6v-h-ViPLoam3gMTObR-d3-W_0GujR6vgzKKQ3tk0sBF9-wjyKxCkgCAVnA4oXUIsWCFrdGlqbNoOipgK96Jf0J4dJLKj4TX_0-qQTeBHnUcO82rd7gES6Es8sIJnKfUSdEsXSHWBgHxD3S1017WeH0W461dpyVz1OrfSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏در فضای مجازی این ویدیو به عنوان لحظه‌ی ترور خالد خالدی نیروی جمهوری اسلامی در پاوه منتشر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67099" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67098">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaoHAWLGnm-SsJHyNFl1K0_Jqc1hb3oHqoJvYY8wF7SmxWVca1Oy9Rayl43kp8q90pJJ0vhJ5C0Uzub6b7-Vy-LlrSONLHf7qWjCWvDkkfwjNlrKdtofdVT9P7Cv2bDaC1F8qJbtt1-RQsk8kiLEYAO6s3C9CNN8AGbhVqA9koxnOFU0MpSAPnTLeMUm07v3kpq3VHTTVhw7se-AEDpc0QK8AqTR8Q1boD6TPbqlhIOzYOEaFB-iFWxrd-I4i-WRoWxt6k_i7CGnsxzisVppDYKcp-7b5klSKGqIfkOcvGPAoC5NJYeaHau3hQWumEpHT4t4zXTWV4dvNuz7i1XPPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
علی حسین قاضی زاده تحلیلگر اینترنشنال:
‏ایران اینترنشنال نسخه‌ای از دستورالعمل محرمانه شورای عالی امنیت ملی را مشاهده کرده است که از مدیران رسانه‌ها می‌خواهد طی ۴۸ ساعت منتهی به آغاز مراسم تشییع جنازه علی خامنه‌ای اخبار مرتبط با مذاکرات و توافق را از اولویت پوشش خارج کنند و بر پوشش مراسم متمرکز شوند.
ساده اینکه از بازماندگان نظام می‌خواهد که چند روز تکه‌تکه‌ کردن یکدیگر برای تصاحب حکومت را رها کنند و به چال کردن رهبر ملعون‌شان مشغول شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67098" target="_blank">📅 19:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67097">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYEWjt_qCqKQNND2O3z4kZkYRZJvLpDLg-IulKyOFlty48-0o0TPy8eYjDNdcXLNbKvBFGU68QrZ4v6atI0B2MesznG6UXKHoIb1iZcq-gRA3Z9TFt2F69ZqpEs5jjEOR3XPayXEzjWvIR9UnMu0nhdSvve04YXm2U99paXKO8BgIvgXvmVJVuDqldLkeaiWEBF_uTfNeiparYGfinocZo3hx53wav4WvjCybJTQGRo5dgiGmUuLivGjN_lDgv4YUhLZm-1AYOUGGvu8NG4MkcUbRO486WHkhu0Hm2nXEMyOw5pcjs6b00-xrL7a1pqL6rjymYmjAObrzOAjNRAeNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ناو آبی خاکی «یو‌اس‌اس باکسر» آمریکا در حال نزدیک شدن به منطقه
🔴
بر اساس گزارش‌های منتشرشده، ناو آبی خاکی «یو‌اس‌اس باکسر» نیروی دریایی آمریکا در حال نزدیک شدن به منطقه خلیج فارس و آب‌های پیرامون رژیم جمهوری اسلامی است. تاکنون مقام‌های آمریکایی جزئیات بیشتری درباره ماموریت یا مقصد نهایی این شناور نظامی منتشر نکرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67097" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67096">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=mMVbJz35GVTuJbx2T3Jj-dPsg3MEwz5fmBpX_Yfms5GoTOE-Z2oABNV2jrH98UiexHHrihBlnxp7TMKihniUOjg9CG3TMCmz5lpsB2deoHA0S2EOwpbh_Opv4l_z5vZ6gEHvi3v4oT2BTe7i9yACoOulaMKeJZoyxKsqJ0PmAF28NpT49xzdJKvO_Vc98ICCFGIKQPr9fMpuotFaVevKL8sgTU0P-AFUAdBtbdXm54Er1syOHXVKuKsdHuOVIEpDfcnZhmQk_HbV-HkPQy7D5BPXaqynsJS4oGt8LMKRnC8ZzcmI2TacOlxodekyiJJXy4E7myNQHRF84eLQdE7O3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=mMVbJz35GVTuJbx2T3Jj-dPsg3MEwz5fmBpX_Yfms5GoTOE-Z2oABNV2jrH98UiexHHrihBlnxp7TMKihniUOjg9CG3TMCmz5lpsB2deoHA0S2EOwpbh_Opv4l_z5vZ6gEHvi3v4oT2BTe7i9yACoOulaMKeJZoyxKsqJ0PmAF28NpT49xzdJKvO_Vc98ICCFGIKQPr9fMpuotFaVevKL8sgTU0P-AFUAdBtbdXm54Er1syOHXVKuKsdHuOVIEpDfcnZhmQk_HbV-HkPQy7D5BPXaqynsJS4oGt8LMKRnC8ZzcmI2TacOlxodekyiJJXy4E7myNQHRF84eLQdE7O3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
مارکو روبیو:
تفاوت اصلی این تفاهم‌نامه با برجام اینه که برجام یک توافق واقعی با تعهدات و چارچوب مشخص بود،
اما این یکی عملاً چیزی جز یک کاغذ امضاشده نیست؛
متنی که فقط می‌گه طرفین قرار است درباره ادامه گفت‌وگوها، باز هم گفت‌وگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67096" target="_blank">📅 18:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67095">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=vcvKLsRgQRbVNRw10GmR3rpKDmQr45VAQhEx0jX1oPZHnF6vDr-ckKBh59YqLJUBwI6c_KZFnEHrkMRDMYXpCYBSWlf4NzOMIVz3pet2Z56-gord9Xs9KD8GVXrim76s_nZwMo0p9wSXRj6jjh52zgb7tmt7N1b93CkLpKFfYHXbQYEgyOxKBLLZLuiX78mYT4VbhAnC40fAgxLHIFb5Kc5oa9uIEkdf7VsEDbGveKnwxxDpFcmOCpCYxpa3spBL-45iTtk0tbXU0rb5k02oH6iWiIXhv0mz1eVvaU8-3zYeXJ_-vGEbQoSnJolo4n7V-thrApb91Y_4I9PozXyGEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=vcvKLsRgQRbVNRw10GmR3rpKDmQr45VAQhEx0jX1oPZHnF6vDr-ckKBh59YqLJUBwI6c_KZFnEHrkMRDMYXpCYBSWlf4NzOMIVz3pet2Z56-gord9Xs9KD8GVXrim76s_nZwMo0p9wSXRj6jjh52zgb7tmt7N1b93CkLpKFfYHXbQYEgyOxKBLLZLuiX78mYT4VbhAnC40fAgxLHIFb5Kc5oa9uIEkdf7VsEDbGveKnwxxDpFcmOCpCYxpa3spBL-45iTtk0tbXU0rb5k02oH6iWiIXhv0mz1eVvaU8-3zYeXJ_-vGEbQoSnJolo4n7V-thrApb91Y_4I9PozXyGEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی روسیه در زاپوروژیه اوکراین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67095" target="_blank">📅 18:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67094">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=DCsL4zF8AqHtdW0qgbqmH7zo8rW77HU0SbdMQeBU2RAlvP2QqYJlbfwOlfruqjVOwYmtWRb8Ba5nw4R7v4HfyItQUp1Jl8dtGmxuFLYADFgmUF-R_np8BflkAErU6tUA1ovZGRQjTWTGcWlo4uTyELXDtRDmN47oEfBlD52Q4RXnzgXy89ZnKx6lbYh4FqI_VF892rhKL7mX1huKzNd_ryIvLIsS56Y84iw1wQBmHdQIZPnGe8LMTC6vG0zH8q-mJQ455PiWY-ZI4iJeZNO685lkwyY_ZE5Na-uovexQTZPTyGOHq_X38-MWLIsqIubfX6OtKPNE8Yqm0i51cu03_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=DCsL4zF8AqHtdW0qgbqmH7zo8rW77HU0SbdMQeBU2RAlvP2QqYJlbfwOlfruqjVOwYmtWRb8Ba5nw4R7v4HfyItQUp1Jl8dtGmxuFLYADFgmUF-R_np8BflkAErU6tUA1ovZGRQjTWTGcWlo4uTyELXDtRDmN47oEfBlD52Q4RXnzgXy89ZnKx6lbYh4FqI_VF892rhKL7mX1huKzNd_ryIvLIsS56Y84iw1wQBmHdQIZPnGe8LMTC6vG0zH8q-mJQ455PiWY-ZI4iJeZNO685lkwyY_ZE5Na-uovexQTZPTyGOHq_X38-MWLIsqIubfX6OtKPNE8Yqm0i51cu03_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
پلیسا شوهر طرفو دستگیر میکنن زنه یهو میرسه به پلیسا میگه وایستید لطفا میخوام باهاش حرف بزنم یهو بعدش...
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67094" target="_blank">📅 17:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67093">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⏸
🇺🇸
نوه‌ترامپ رفته کاخ‌سفید گردی و با این ویدیو مکان‌های مختلف استقرار بابا بزرگش رو نشون مردم داده
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67093" target="_blank">📅 17:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67092">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c791837da.mp4?token=NjHZfQ5zgYeEBDwcpMsQVhIBvFNrRpaRhdsvAeintEtV5M6G9k4QcBFQJ8xPFLN7Uy480sNCWip3j-vIQg7efXWBDA9fiQJbV2nzdPs3EXaESmqHNh9fP93KxSOfxZxwQI2N3PEOa50lBL-w8juBB_Qe0v06eJavk-qjb7W4SVAH-Ll6tKukwE2XV90TnMMgMEAjRBdnrPItOVJgr8Zf-ckvXYCr3yYtBg0srBH3kGqlIcCCPsrORmLCMPIfdFaxlZ_77zbNYpix8EWKl81HstvYh5KvmkwjU1Oh6Kx8BEzvRD8qBKy29YsO4ewtIvMIU9PTYSbMEcZJALsi51_GByHQiU_gIL4RvSsC5q3j2twyTFDcRTpvKsjh34c84JcwetlW-O2OP7Mc8EX5yGxDJYeVQkGx_Cm8MDfEcyw-9SzxgB3JmjgJwx0i9lZpG7u_YcyJWb6XQ_NsYhsz7lRHD1CfBJwQxWrSRn67V_MujA0Kjlk3kKl2XdJDO8VrejGkQTkDWoBBWOMSIh26aCfmYr6iu5OznFJx8SRM3tumfNnm6aJ4clrgeuofosJoVmcSoYlNqGjoolxvvOlwv01iPDRp3T6rkixuV4h_C_2NUr-oRlRSH8pfZalZRVUHUuglP7h9nYgTUGACfBX-I21zVEEhvQFVq0QaLp7it2bGrm4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c791837da.mp4?token=NjHZfQ5zgYeEBDwcpMsQVhIBvFNrRpaRhdsvAeintEtV5M6G9k4QcBFQJ8xPFLN7Uy480sNCWip3j-vIQg7efXWBDA9fiQJbV2nzdPs3EXaESmqHNh9fP93KxSOfxZxwQI2N3PEOa50lBL-w8juBB_Qe0v06eJavk-qjb7W4SVAH-Ll6tKukwE2XV90TnMMgMEAjRBdnrPItOVJgr8Zf-ckvXYCr3yYtBg0srBH3kGqlIcCCPsrORmLCMPIfdFaxlZ_77zbNYpix8EWKl81HstvYh5KvmkwjU1Oh6Kx8BEzvRD8qBKy29YsO4ewtIvMIU9PTYSbMEcZJALsi51_GByHQiU_gIL4RvSsC5q3j2twyTFDcRTpvKsjh34c84JcwetlW-O2OP7Mc8EX5yGxDJYeVQkGx_Cm8MDfEcyw-9SzxgB3JmjgJwx0i9lZpG7u_YcyJWb6XQ_NsYhsz7lRHD1CfBJwQxWrSRn67V_MujA0Kjlk3kKl2XdJDO8VrejGkQTkDWoBBWOMSIh26aCfmYr6iu5OznFJx8SRM3tumfNnm6aJ4clrgeuofosJoVmcSoYlNqGjoolxvvOlwv01iPDRp3T6rkixuV4h_C_2NUr-oRlRSH8pfZalZRVUHUuglP7h9nYgTUGACfBX-I21zVEEhvQFVq0QaLp7it2bGrm4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
قمه کشی ارازل اوباش میان مردم در شب عاشورا رودبند دزفول که با دخالت پلیس خاتمه یافت
😐
😂
تاریخ ویدیو 1405/3/4 امامزاده رودبند
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67092" target="_blank">📅 17:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67091">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=wCDcQ9eWl7SM4VqtOanhrY4jElMWMrj4p3g1sL1-R5Jr2xjVixb1eDxHeJlPlj7VtYbh-LpAQn0AsmeLLYXErJmA3g3-4M0fRta0ovz5gfAOuNCV_ZAVH-L5fREHsVjNBWFoHX7L_e6nt74rkBhoIewz7z5-VkCY9UUFY0avFYYlXrCRnsxZT5DdZHE7151C9hHI3qAimC2TYJZgYrOBxg2nG15h3pxKV4VvYS6_mwRHqtD6Ts_9sdS_yqma7TVZrB4iIMWvygAbSxs7hk6uYYtqaQbNO8PG1Scny1q_Zue2fC1MfTAHC5Yi5HQ1Ty6DnDDoV-JRVMiTLNIYMWv3yZWLv9APtW6BTgXkn6KdLNWLjvmU3qQR73SJHMV454Sgt3-mFixQmuw1dMjhqJsT9Fb4WIhqSM90c-_96U2vzNtbUCYxv24_eGk35jq7BMb_xHN-iFzy4ryJbdaeXqheeZrx81kn9sRV3bj1ZVWKUoFv4BlkTOs-LOldJdRqvJeM09-VYeP4TXPHpQM5A6ExlHaq3mJWYHNY8QlxXYJRoaVtwH4geKdxz8fFl38nBO7EJQ-o04rJkCL4N3bYRtU4XQrMClUW2L2TkDg0QQkvoAb90Hy7bXuoWXVHeS02708yYmco6tMlOOOw6IY9fxmiY5TSs5Cio2pN3ybZcfus4yU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=wCDcQ9eWl7SM4VqtOanhrY4jElMWMrj4p3g1sL1-R5Jr2xjVixb1eDxHeJlPlj7VtYbh-LpAQn0AsmeLLYXErJmA3g3-4M0fRta0ovz5gfAOuNCV_ZAVH-L5fREHsVjNBWFoHX7L_e6nt74rkBhoIewz7z5-VkCY9UUFY0avFYYlXrCRnsxZT5DdZHE7151C9hHI3qAimC2TYJZgYrOBxg2nG15h3pxKV4VvYS6_mwRHqtD6Ts_9sdS_yqma7TVZrB4iIMWvygAbSxs7hk6uYYtqaQbNO8PG1Scny1q_Zue2fC1MfTAHC5Yi5HQ1Ty6DnDDoV-JRVMiTLNIYMWv3yZWLv9APtW6BTgXkn6KdLNWLjvmU3qQR73SJHMV454Sgt3-mFixQmuw1dMjhqJsT9Fb4WIhqSM90c-_96U2vzNtbUCYxv24_eGk35jq7BMb_xHN-iFzy4ryJbdaeXqheeZrx81kn9sRV3bj1ZVWKUoFv4BlkTOs-LOldJdRqvJeM09-VYeP4TXPHpQM5A6ExlHaq3mJWYHNY8QlxXYJRoaVtwH4geKdxz8fFl38nBO7EJQ-o04rJkCL4N3bYRtU4XQrMClUW2L2TkDg0QQkvoAb90Hy7bXuoWXVHeS02708yYmco6tMlOOOw6IY9fxmiY5TSs5Cio2pN3ybZcfus4yU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
😳
عاشورا برا این اراذل هرچه نداشته باشه یه خوبی داره و اونم اینه که تا سال‌ها سوژه میتونن دست مردم برا خنده بدن
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67091" target="_blank">📅 16:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67090">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=fiPOTA8mox6vzm7Y2srfPQZIH56lwtfo-s_x4JJcOzPTb0e3nrT8f70k0rfamSuWVzG_P7l9efzpQDna4buGWfIaX8ugcmQiNaT0zeZD-jtWZgYFGho0IRt1POFS7pDs7BXWaWf3Tng64kMBYLViLaUe96BdYifKnM_KyGHZaWsU7U4nEfdkdrSorOx99csAcQL_zXjFr0dYWIpQQcTYKzBf7l7-HB4Drmynb4jeHKuDzeGkWJRQTyMiN7YfSybbQuY5U7rFCP3lHxrw_qJtkhihIhRPv8CP6KPt-yHgYUWpT4602XzZRCqeJ7d64yFxVQoi2O0iQQtII3XZi9AYbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=fiPOTA8mox6vzm7Y2srfPQZIH56lwtfo-s_x4JJcOzPTb0e3nrT8f70k0rfamSuWVzG_P7l9efzpQDna4buGWfIaX8ugcmQiNaT0zeZD-jtWZgYFGho0IRt1POFS7pDs7BXWaWf3Tng64kMBYLViLaUe96BdYifKnM_KyGHZaWsU7U4nEfdkdrSorOx99csAcQL_zXjFr0dYWIpQQcTYKzBf7l7-HB4Drmynb4jeHKuDzeGkWJRQTyMiN7YfSybbQuY5U7rFCP3lHxrw_qJtkhihIhRPv8CP6KPt-yHgYUWpT4602XzZRCqeJ7d64yFxVQoi2O0iQQtII3XZi9AYbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی وزارت خارجه: اساساً برنامه‌ای برای دیدار با آمریکایی‌ها در هیچ سطحی نداشته‌ایم که بخواهیم از آن منصرف بشویم
🔴
گفت‌وگوهای دوحه دربارهٔ اجرای بندهایی از یادداشت تفاهم است و با هیئت قطری انجام خواهد شد.
🔴
اجرای بند آزادسازی دارایی‌های ایران در حال انجام است و امیدواریم کار به نتیجهٔ مطلوب برسد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67090" target="_blank">📅 16:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67089">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNn97VAOyg7EprYEn4RAdvC1U55j5G3aqpOxax1Svr1lpKw9NycgoaNQq42thhDGqz1lls1pZEo4likZc5HfLFp2rIdSvt_L3eqWVk_e1-KAP4V2ldhkwI705SnmP1tO4sunVpzyadOpAOMdWcUgnkl3-B4HFAZlvxS4FLm9Kr2xuSVvchrMCKPbHZjIvrgYBu_V_Dgk1gU93M34zm-syTLdr4egQeFCxPT0gTtkCDHETyNAPX2rgcpy-K2MUU8XrE-eb4twQc5FrVxWprnrFp85XT3Ms4zuDQWabcz2Wy1c_dCWjXDMt9PsrIn7RpNAPvBPj77G4pbXt8iYdzv_8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
مذاکرات غیرمستقیم میان هیئت‌های آمریکا و ایران فردا با حضور میانجی‌ها در قطر برگزار می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67089" target="_blank">📅 15:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67088">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iu6upV1EtSJ5VV6cGip_5UiuDX6XTE0vnZPfLmqr2BbkZFG_c0bATWoTEZPu4JQSjFUZ2-y9fUc4gcsMVxYjYJ5G5-7DGgQ4Zmxv26IY5T3Kt4xEIN0StTKV5kkCi0CGHbP_qTrrACRQup_fIEoSBbVHLz2kqQ2483G6PQPmIbZwNGwRMhB5joLxrdH7aliDpWV0d4YMFSRzIg_CDg3VOphcHjl1BZUT18jBb0Q2PNF0nXxUT--d0XF62lTN5m6F8OGhorW2VPouZ8RvPWaK7F8ik4roV0NJGUW8txoopL86SL1tMLyyF32Fo7DDzsC1vcHS80pXB6epAqnrU4cnQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه همشهری با این تیتر ترامپ رو تهدید کرد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67088" target="_blank">📅 15:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67087">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=CczrAZdl_GC2aFApF-XtX_vxp-8tmVhpMlZs1RM4j9EqdPaiMVLrxjjIG_mbrtosyJVHJCJ4KDeyAZDm1ETRTAGl2-FEE_hRqjHGmCLh9BtLN18AJffGXP8Ywk6F9FO1cUrMAJb275mDBy1aLZwlOhH1foir0vqy91E_8CHhw9AFcaHdktzcUt_HlvD7yXJacw1rjef_8fAbRgQoC4G-821YTf1LefOvi9HbfiqRx9eyAcwulvR--kNOxDbpPj_naSafQUvKLucMwZilIP5tGca4ZUOp7C9d7xNiPQ8QR64JXsKBjXBxAt0osKKX-xlOPXPi5doLmPEkPYWllRqouA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=CczrAZdl_GC2aFApF-XtX_vxp-8tmVhpMlZs1RM4j9EqdPaiMVLrxjjIG_mbrtosyJVHJCJ4KDeyAZDm1ETRTAGl2-FEE_hRqjHGmCLh9BtLN18AJffGXP8Ywk6F9FO1cUrMAJb275mDBy1aLZwlOhH1foir0vqy91E_8CHhw9AFcaHdktzcUt_HlvD7yXJacw1rjef_8fAbRgQoC4G-821YTf1LefOvi9HbfiqRx9eyAcwulvR--kNOxDbpPj_naSafQUvKLucMwZilIP5tGca4ZUOp7C9d7xNiPQ8QR64JXsKBjXBxAt0osKKX-xlOPXPi5doLmPEkPYWllRqouA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
ویدیوهای جدید از زلزله ۷.۸ ریشتری که در ۸ ژوئن ونزوئلا را لرزاند، در ساعات اخیر به سرعت در فضای مجازی پخش شده‌اند و لحظات پرتنشی را که در طول این لرزش قدرتمند تجربه شده است، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67087" target="_blank">📅 14:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67083">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K_qKH_xiHrdrHRlfBrkTI3objswcpNS1kkCOZF1jUUArYCY5iVVZTJZBxvP3RU1Rp6LcbwyFAUHBmS-bt0BaaXxHi4EXI6hPHl081--muZviuRPlCx_917O2g8iZiT6M9iBFb2lSH7fTlSBMqxq4kgE0c4Hbey5qG7r8E3qNvdAKnwAkvi27l4w8bldYl__NmBdaYAvW26L-o6VAPRt9kuVOW4_mLNjSQAeoAHBMS9FwfZZqwEWmtyDJBImF_kjy7k1nKd4_lBu6x3w_lB3q-sf_85E9HvKxtRYkOFpXnW7PGCWsE2rQ_-nM_U_r1NSTZStMSg2iyPbcYj6pkHFY6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJMj3mAJE3Ir4G33bV6XA0GEyXH5EbnFMwAFXmw1hiPI8kLbfdOR_B4sMdzhoUrX2sOSBZkkUqBDJybXrKvsapuVc_nLgrTyI8rOTa_yqndUXxLhMfTXXFtCtq41KcCmKZLf8KGuF7AOeKPSkejvfkVHGChhPx8FvNf3G5lmQB-BLNFqQkSxI7PQ60QBYfRm4yCPyaELqw9W1ST_8FEh-PC6NRQTwgDu9wtFrYXr-WEtGRqBLEFGVTXZhuYRniLt2OM5lM7G2lLF_u7ca89VCVQHNewxMIwzQgdCqzMYLjpJSr9GXNR8XDHy87eOT3O39LCP6EHJohA7nU421xmp4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s8W7BnxqGbOLiZtnek5aICelEauX08rsAYtRpY0Pd9zTBe5wBVHUxRiNKjPUmnr-3_1eUr05I3a5YcUtvVgyPWrId7BpewexYiEqncfw4XVK2I5ChsdWx87TNljnsJigV4-yHlnh-3uY_AxM52-8PwUDgTTdqUQ2phueXoVTmz5jimmIyrMxHNK550xH085iIN89tGWcJ-d1Re8-BHHKl4v8PHK5vv2A4NKSj-KSrRD78EsPwxsVMrhSq4T6dgXcDp7CF_c8EMEMKuxVxKCqqbczxDSNQCdrDrd5OnPznJIQ1zM2quGXD1zlIzrEdlxnb4dbZUFArvCcgvaLtBOiCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YhxSDY6lvwUqla2AIN_I8FAIZU6XqhSlCVJDkKRw5grM9-BvAOKLIV3XguJkUBAzViVlmawFTthoG11xSX_TZCEuhP_EtZ_I9aluX06vOBJcIAZPgNbYsJoMTX9stUT2t6Hv48mj1AXK0PHh4l611TMLa20_nnF6W2UgbYjFnEg4B4crOOPhcXky0EoLRZMmCH3ibMhl51W0jQBbvacdVUGQ5OXafIdBFWVFjCggSONfksCENef4pKzfZvTva7hjBnRfelcZDE7kjrRMbKBsfeibQmWoamFvzq99_j9N2GtLrWWAfoTGu6wgWfSeRW6uhXEsw5_Vq3Z24rcyQJf0Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😂
یه پسر 19ساله به اسم آقا سامیار، اومده چندتا عکس از تولد خودش به همراه دوستاش تواینستاگرام پست کرده؛
حالا به دلایلی نامعلوم، این پست تولد آقا سامیار تو اینستاگرام فارسی به شدت وایرال شده و بیش از چندمیلیون بازدید گرفته:
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67083" target="_blank">📅 14:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67082">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
⚠️
قالیباف: سوپرانقلابی هایی که هیچ غلطی برای این انقلاب نکردند، ازهمه طلبکار هستند
این ویدیو از قالیباف مربوط به سال ۱۴۰۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67082" target="_blank">📅 14:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67081">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی وزارت خارجه قطر :
هیئت ایرانی از اومدن به دوحه منصرف شدن و مذاکرات لغو شد.
۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67081" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67080">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
جرد کوشنر و استیو ویتکاف، فرستادگان آمریکا، در دوحه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67080" target="_blank">📅 14:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67079">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
هیچ نشستی در سطح عالی میان آمریکا و ایران برنامه‌ریزی نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67079" target="_blank">📅 14:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67078">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gnUsqZQiryJmbJQfnjq0D8YIVe0dVnRhA4DR_gUMp-XX-ByyoWQ8dx7aVMbiXoRX7HZlk9JHb7PVRRqVVgxmcJopX7W55pvjlmhsP9iV5NW2ef3DJSfM8JSCV3P4pZpEW3OV2DGJneC-awiO1RqSJpJ8BFU4XnMJQGq1TFR-e8ftbSx375vNXuaweShfuxF3BIpL8Y9f6rGsEw-D5hxT6cSe7zldsfaVOtmI4sWR2Sq7DVXOemyVy_iLLB3JDuSfxjmJfh4T-tjXuiKnohQ9KwJoShzQMSLVh96GrjrLAkgK_JWXVVvQmwxYe8aljfoh7L3T434RQ3tuD_EAsAW5Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افت رتبه همه دانشگاه‌ های ایران در رتبه‌بندی کیواس ۲۰۲۶.
این فقط یک خبر آموزشی نیست؛ گزارشی از هزینه انزوای علمی کشور است.
رشد دانشگاه‌ها را با قطع اینترنت ، فیلترینگ، دیوارکشی دیجیتال و انزوای دانشجویان متوقف کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67078" target="_blank">📅 13:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67077">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJxOmO6RkAA47ahUQIwVCtfe-DY45yON6uBKfDQsEPz4LCxc4nNETcogCE-K8clew3_RNh6Lp6LrxoBWE97Q6s05-VlZAuSvi-Q4oucTscHetIuTwFC89r83PsJfu2JLaemrwVjIgOStVesFbpuy3qv18boe6nYllGNxLpvLL5WRIHa-6UK5mQgf-sJ5BqWfuQEliC1C6oFa2_-CkmIeCxYcV63agOBdvnauiyKCN_Z6LBi4FU44ZWYcVBswudTlBTYpRXChQ4T85m2ZZ6ShCmKEnBPA_tIz9fT47BoCxR-Y9WiisMLtGP3sSgy-b-9eSCkEEfNYhLLPZaOkpAPm2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
💢
فرماندهی حمله جهانی نیروی هوایی ایالات متحده برای اولین بار تایید کرد که یک بمب‌افکن پنهان‌کار B-2 یک موشک ضد کشتی برد بلند (LRASM) را بر فراز اقیانوس آرام شلیک کرده است. ادغام جدیدترین موشک ضد کشتی آمریکا در این بمب‌افکن تاکنون برای عموم ناشناخته بوده است.
💢
نیروی هوایی ایالات متحده اکنون توانایی انجام حملات اشباعی ضد کشتی را مستقیماً از قاره اصلی ایالات متحده دارد، در حالی که پروفایل پنهان‌کاری خود را حفظ می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67077" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67074">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X63CsrWFkhD7Z8L7w4MKwYSWyus8vz8SXI9FEHSAxqMutjTk_GEuWvTCjoCM_NurkSA25QT0_8hMbCWeyCp7B7ob_INGgUe0lerPyLpzVDfLpJL5F-2EreVgFbb1iQSrpuMD7DUocWUaxHnLzk9yBPidVNKPmr1Z-sbHDT8DN4mAM3JTCDYjRrX0wIORkgZPz24q7qcXpMbUzW3EMR-Tlf4sF_R7pc171CBsIycrnCYz7g7eNioePYl8sSHb8hBQAqq1lFcNIMAzFwA5S7vuXrSzOUptDZD-xhHoXPmtExyXK9puqzqDkk_WgNzQpuC7W2NGSbmX2pLqlk8y36G1sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚠️
🇺🇸
مولین، وزیر امنیت داخلی آمریکا: خیلی خوشحال شدم ایران از جام جهانی حذف شد. انقدر خوشحال شدم که رقصیدم. نصف اعضای تیمشون سپاهی بودن و هربار برای ورود و خروجشون کلی اذیت میشدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67074" target="_blank">📅 12:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67071">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qB7qS9eyTXQr2gzl6i49fjh3ZdAfzstOGsLP9I_ehvfbNQ1FD75Fyht3elo78HGAWy8ZSrmUdAEoD-S6Mqj0KYmeAlvL_k82xdktrxvz7RhTpn8NEjLp-Z-ZJ8RZo84yvNpBBA81Ktm6yL88I2LBYDLX_lP4IIH_iNVEn6A6nZY08RaVQGAoTEHDSh6lbnNwHBFZLV7Fi8PHkzsXPV6fP8iExhL1Vu1YwxmYgwJlXmGkeGYXwHPQIXa0Ob1_dFegKB8QRKtJRpx3XitOpEx0KVzJQOsy1HmhMsP-Pg21kbgMBFmjqZ_Txo1gMzVFgM2Z1SeOfJ6N8aCL57JOKCWp5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fSlayz9KR85GrayCzOjfbvU35l7PrZQB9J_czruO2CJ8GJMJWdX4wL-GkBIld30gLG09Mwj8OmLJqpnPlkTxkQmTbQaZr0GpnqZYnbZM-VZ3PHMLwEkB9TvKWukq4VqwxEfYV5alf8Y4wdy5hKA1Kjv7Whb1O_UgoZhkX2kqgGtGkhD0_PlG6d4O8gDVB2ssS6zX0uv0tEsJWw3h6GfNfb46MHdChGmtHz1gHnoHm-LmvUju1_4BhEFC-VUUzt-1Ny7-1D5gpk6xFeZasunsBF1Qij0aBhD1hEwKKnKrxVlG3LWxXifUQBvRQWSURCzXQorfwokOPKs-g3tasy4lXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SnWh4WmFn_9AIMuqEXJoEGABRQ3GEO4CrpdiJL115GRjdCPvyYPbCelV7Lzqq2wk03YfVdkTbhzx_WYsYbb6i0Vi3jBUI4FhdH93BHbcOZxuw2PcmPic6SrrZpd7hYTmeJX9omTj4rR1vk2AOpxaryl5w3JdqotgRgFHDPYefCr-HlrcnpkO51G2LK6Nn2z3iDVwnPEtVLmV2jfWG3v4LJwixUCl-lklNgptxNkXpnsUmEp_WMzhrT4XAUIrqwwlB2YLBWpyToTg73e9BSaXyeQS5zrqbcLANZUuP_SfIaTIcPrASRcLiM6WU0NehqU6IucmLB3cTribgLXQYzKUCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اشتباه نکنید، این زیرزمین خونه والتر وایت نیست، این بخشی از دلارها و طلاهای کشف‌شده در منزل یکی از نمایندگان پارلمان عراقه. حالا شما به این فکر کن توی جمهوری اسلامی از دون‌پایه‌ترین عضو  تا کله‌گنده‌ترین فرد چه اموال و میراثی از مملکت رو چپاول کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67071" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67070">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMu2h0OEBBrECArotT7CDy4dHR7KUNXqHAcb1QOQk351wBwZzR9fJIdVx0lXy3QNTgAmeS5dorl39LFQsaN4BornnZOzCY0R4Y4TAI05bv2yL9QT2axTkL7chFBfPkAqQsgfmMQLhnuRu1f5Ss_hZ6MqdMFtRU5R-Bbzcv0Rrp7ZpklSsTZ1WdGGQiAOZdB_0VhwrcckdQhUkUQSDEjqemweuaXYU9xgDh8JLUqlsBKqMWPAiC1Z_MyDvcWoUBzu0qUNAyn3Ito55--NoTqrX-tS0aZybMflqgScRdnfdbQ2UJonH_zMzTRZic1LRWQcWr-k9q9au-FQ4fbX9HU0EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
اموال کشف شده تو خونه یکی از نماینده های مجلس عراق
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67070" target="_blank">📅 10:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67069">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=JzN_GfJgSAf9-ZttFKtTYbivGFL0M-2A9HcksZXieb7i3IJGUw0LUVfXZylzkTp11efKYJ6i8mAJxCCNIi6wYDpKDpJ83NzK6dYh9BpF94QOgpyr6OVxKz9SRQeDim1YAJtgFJyq2rm9tDZ4QdXok7WqLCXCO_VLQJT-Ut_5pIUhXIxZCuQY1XiyXbBT4y18mpvMy98fHGiQjr2KM3X34iQgUt8VXtnuRyAydUlNSggC3D9cXhIJi88NcpOxgcUm7bAHGdJP7BjV5GiNjDvrKbgpy6L3qEOMCjyB_tGKKRLCpu7ZiyJDDZCzjC77GUMyPaWw3sWfuyvWFqWdiJeZHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=JzN_GfJgSAf9-ZttFKtTYbivGFL0M-2A9HcksZXieb7i3IJGUw0LUVfXZylzkTp11efKYJ6i8mAJxCCNIi6wYDpKDpJ83NzK6dYh9BpF94QOgpyr6OVxKz9SRQeDim1YAJtgFJyq2rm9tDZ4QdXok7WqLCXCO_VLQJT-Ut_5pIUhXIxZCuQY1XiyXbBT4y18mpvMy98fHGiQjr2KM3X34iQgUt8VXtnuRyAydUlNSggC3D9cXhIJi88NcpOxgcUm7bAHGdJP7BjV5GiNjDvrKbgpy6L3qEOMCjyB_tGKKRLCpu7ZiyJDDZCzjC77GUMyPaWw3sWfuyvWFqWdiJeZHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مداح:
رو هلیکوپترشون غیرت داشتن بهتون حمله کردن و علی خامنه‌ای رو هنوز دفن نکردید.
۱۰۰ میلیارد دلار پولتون دست اوناست، و میخوان ۶ میلیاردشو بهتون سویا و ذرت بدن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67069" target="_blank">📅 10:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67068">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=FNUiZKHTUaCEMyt2cnw8h8jPWSEMItXCBNw_sulbcLri1_h-rqe-Dfu9XwPsUNEilUAkzsAXy0QGNdt8OaZukGj2Q3GsLyikYc4uIzkavT77n7MQVOgPI58AmvQJ0yfuG9Io3xvlUbnhs-7NE9bZh_fWatIrw13t1Pkel0VRqjlX3ZYd-kJJg7PhPQG_ujGb_yt-cXJpZ1XDjd675SzFkUDejlSR-7o5p_NKPeBNTiIacJj35vXFr2lS7j0jgo6Q-f4A8IerP2RsBLjJzYgZtnxJdcRCgKBXFvEKL64wjqstkmTJ2irpsdl1uTlQ431HwMWk9QWL5wIZLEhIU2Agjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=FNUiZKHTUaCEMyt2cnw8h8jPWSEMItXCBNw_sulbcLri1_h-rqe-Dfu9XwPsUNEilUAkzsAXy0QGNdt8OaZukGj2Q3GsLyikYc4uIzkavT77n7MQVOgPI58AmvQJ0yfuG9Io3xvlUbnhs-7NE9bZh_fWatIrw13t1Pkel0VRqjlX3ZYd-kJJg7PhPQG_ujGb_yt-cXJpZ1XDjd675SzFkUDejlSR-7o5p_NKPeBNTiIacJj35vXFr2lS7j0jgo6Q-f4A8IerP2RsBLjJzYgZtnxJdcRCgKBXFvEKL64wjqstkmTJ2irpsdl1uTlQ431HwMWk9QWL5wIZLEhIU2Agjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از سخنگوی‌زن‌قرارگاه خاتم‌الانبیا هم‌رونمایی‌شد
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67068" target="_blank">📅 10:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67067">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=chlHFWxAY0dv51JvC17AhmcJW1ILAU4KBMpy-XDgrKWcstIrLyIA37us5WZzxkU-fzjdpt8p_ikz5hSLvMzH6sfTCIlYHg5v4s3EESVCV4CdzepD59h_JVtGw2CLvhyUTRnfrOQMvZjPVmd-vwq--41dt6ruWhFBQX6H6hhSyl32f1oNqroplTAEYIkg1IAGcGXItSjC0EJHX8S2enORzpdb5_jv8kzX1vhEJpwfS36Zk-_Vc-vWdOc0C-r8ajyKp75nCQqSmdf-wFzyw6GXGOLfliW_T2nG8h6EpRlaf3FoHJ1kCf3ziGKekyfpVfiEaY9U30ShT6HroZNy6g9NDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=chlHFWxAY0dv51JvC17AhmcJW1ILAU4KBMpy-XDgrKWcstIrLyIA37us5WZzxkU-fzjdpt8p_ikz5hSLvMzH6sfTCIlYHg5v4s3EESVCV4CdzepD59h_JVtGw2CLvhyUTRnfrOQMvZjPVmd-vwq--41dt6ruWhFBQX6H6hhSyl32f1oNqroplTAEYIkg1IAGcGXItSjC0EJHX8S2enORzpdb5_jv8kzX1vhEJpwfS36Zk-_Vc-vWdOc0C-r8ajyKp75nCQqSmdf-wFzyw6GXGOLfliW_T2nG8h6EpRlaf3FoHJ1kCf3ziGKekyfpVfiEaY9U30ShT6HroZNy6g9NDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس تلویزیون:
جنگ تمام نشده در وقت استراحت بین دو نیمه هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67067" target="_blank">📅 09:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67066">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=VL91KCTBsaDgV2ob7EUER7K7F23DZiAolAgyTf7qhskNciKs7WbAC_hlkcglKz7HYQuCQ-JjnNX74tAuPKXiqFQuz9rdwcxjK442NVGfCR3UKH9d1OEloJgasVDim6vbO9ldk5cBpvl0dkuquPgbCqgmhj9ohsMlWLc41Kda1K89MdQ0YZKkUUsYASh_4oYw1td8j7pS5tryEKiXxbqlZbroEwiH5hzFglurdrZSQAEi7RcRfNj8qDJukI0N3AXeHaIEfmU1Iu1uYjeG8CjrtH4owhTRGux7uJL2fnQSUlye2oJms-E4FoeJtlytm2p3ybIei9Wr2uoQimV-TIYsZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=VL91KCTBsaDgV2ob7EUER7K7F23DZiAolAgyTf7qhskNciKs7WbAC_hlkcglKz7HYQuCQ-JjnNX74tAuPKXiqFQuz9rdwcxjK442NVGfCR3UKH9d1OEloJgasVDim6vbO9ldk5cBpvl0dkuquPgbCqgmhj9ohsMlWLc41Kda1K89MdQ0YZKkUUsYASh_4oYw1td8j7pS5tryEKiXxbqlZbroEwiH5hzFglurdrZSQAEi7RcRfNj8qDJukI0N3AXeHaIEfmU1Iu1uYjeG8CjrtH4owhTRGux7uJL2fnQSUlye2oJms-E4FoeJtlytm2p3ybIei9Wr2uoQimV-TIYsZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسعود پزشکیان در جریان مناظره‌های انتخابات ریاست‌جمهوری ۱۴۰۳ با مقایسه وضعیت امروز و دوران قبل از انقلاب گفت:
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67066" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67065">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67065" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67064">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TvDMuO5x0-31R1QeZ_siX-EqBA_NNpqJFBMnWtmLrGkk5QEtVBxNl5zaqSnB-IY3k2kTnrUFIETt3Nu5ipd3cEI7ozSnSuBdDKh4BF3FyKR4E74lWjTxEZUGZM1IUJsZ8_frk0abO3eMd5qoTkOx0mPdOqohW4ykiI3IxgX0yYnsuazc2Mgw-M2e5mU3RYkFNSYKCBoVaCM5ZBpV_PO-r6773B6nOeoabo75NOyEsYMu4IaiRs_9UQ2kEKw2xJhc9sMCLTqMgX6nJIMzU2fM4WM_nInZYxDXUDwqSkS6HX2LMO3u-zRp8wcDqY1KTINdc0UwF8xInX8lSLbh0e3w8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67064" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67063">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر جنگ اسرائیل:
احتمال دارد جنگ مجدد با ایران طی دو روز رخ دهد.
وی اعلام کرد که نیروهای دفاعی اسرائیل آماده عملیات و هدف قراردادن ایران در صورت استفاده ایران از موشک‌های بالستیک خود در راستای دفاع از لبنان هستند.
او از آماده‌باش کامل نیروهای اسرائیل خبر داد  اما خاطرنشان کرد در مذاکره و اقدامات آمریکا در راستای ایرانی‌ها دخالت نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67063" target="_blank">📅 02:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67061">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeuiVQ88KvLC72Q8Ds9UbEarVlNS0RyQULDUCUHzcnJLU0I3-Cp4_l44hRkrvI0lZr_fPCf6fIPUZEigA4PqKppA8zIRPpDhx2mDlsNzfhr7TsQCRDEpqziiS9Hyw8tefuzF1ApcTfM5U7NU2QnihBz0CoNMN7mHtKIamz9yOpnHyBqpjbcghFgty8jSK0lxwQDiCK0LcQTj3lbGbroAZ8dSsRTebWkY8an4TO03m2mTNpSNK_olE8wA7-whI_IJ0VmcfNJCN1oaYfVAEYWhvc0T29ONOYEbtGfRePo8WRO7Mbew1Leyup6WDf18gzKXEJ35a-s7HMP9S7z0nsREqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویری از بیمارستان پاوه و هجوم خانواده های نیرو های امنیتی به این بیمارستان،به نظر تلفات و زخمی ها بالاست.
«کشته شدن سه پاسدار تا کنون تایید شده است.
سیروس درویشی،خالد خالدی،برهان کریسانی»
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67061" target="_blank">📅 01:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67060">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
گزارش‌ها از درگیری و حادثه امنیتی بین نیروهای کرد و نیروهای نظامی در شهر پاوه ارسال شده
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67060" target="_blank">📅 01:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67059">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUtunD4gZXWi-GTkTq2jCsh5OESVF4XO3NlmhcpYwRY1RirBPp7eGOX2mvoTr2UU_OiVS9Xv4m5oltM1kvRwPNzOSD1Uy7xDXbJDlCZ3FEzdxrBwdawmCqRj2bYtNvlkc8nEXQtqH6_uzkdEJHSComCJ6OvcPDjwA6UGxvH2x-Mn1lT_jNNImDJzrXdbuyezMkXMOjmkMCcGtag5Swu4DRSrD7pMcOOu6L9DyrGn5mM4oiLG8Fn8YAuqs3wqtYvIVi1tGFIYzVstIOITS2Y7fYRw_Oyw1DfPKsaNJsJny3BmYj2UeAyxXz1h1N5UbQMmmeMwzwIaoVmZwSEa82KlFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
تفاهم امری طرفینی است. اگر طرف آمریکایی به تفاهم نامه پایبند باشد ما هم به تعهداتمان عمل می‌کنیم.
رویکرد ما در مقابل رجزخوانی‌های نامعقول و تهدیدهای بی‌پشتوانه، تکیه بر عقلانیت و کرامت انسانی در تصمیم‌گیری‌ها و دفاع قاطع و بی‌پروا به هنگام عمل است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67059" target="_blank">📅 01:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67058">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
این نشست در دوحه شاید مهم باشد، شاید هم نه.
خواهیم دید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67058" target="_blank">📅 01:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67057">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15a452960e.mp4?token=PbcZCwGFBOp14c0gAaSg7Fiqiqm9Kj94Y23qEodlzBFpiTiAPNlnQh7DqjbGjUC6tTjyE1r1YyuB49TtFQHqvnyMWv7P52Vuoxx1zZ8RaTFi2iMEc4J-662dngZ0J2h6UxIxoNVG5Tlu5OuYSPc3oVe_R0gIEJbq-SD-RzOmDZ0ahqFRJPd0XOsM8fvhy46nKGOvnYdVHSwy-KsqAfIAOshWCzxUOwoIl1pm0QJI7chgFM27_9sUExWPiA0F4Ise6YqjvxBn9YiMhYTyhCm8bLjzTbLGhL5QaOfm56pvn1xZ1okFHQNQSOzg2-AdDIg902s2Q37fp1EmprYgPzyW9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15a452960e.mp4?token=PbcZCwGFBOp14c0gAaSg7Fiqiqm9Kj94Y23qEodlzBFpiTiAPNlnQh7DqjbGjUC6tTjyE1r1YyuB49TtFQHqvnyMWv7P52Vuoxx1zZ8RaTFi2iMEc4J-662dngZ0J2h6UxIxoNVG5Tlu5OuYSPc3oVe_R0gIEJbq-SD-RzOmDZ0ahqFRJPd0XOsM8fvhy46nKGOvnYdVHSwy-KsqAfIAOshWCzxUOwoIl1pm0QJI7chgFM27_9sUExWPiA0F4Ise6YqjvxBn9YiMhYTyhCm8bLjzTbLGhL5QaOfm56pvn1xZ1okFHQNQSOzg2-AdDIg902s2Q37fp1EmprYgPzyW9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ درباره کمونیسم:
این سوسیالیسم نیست؛ در واقع کمونیسم است. آن‌ها از واژه “سوسیال دموکرات” استفاده می‌کنند چون خیلی خوش‌آهنگ به نظر می‌رسد، اما در واقع درباره کمونیسم صحبت می‌کنید.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست، شاید از زمان تأسیس آن. این شامل جنگ جهانی اول، جنگ جهانی دوم، حملات ۱۱ سپتامبر و حمله پرل هاربر هم می‌شود.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست. بعضی‌ها وقتی این را می‌گویم می‌خندند، اما افراد آگاه خواهند گفت: “می‌دانید، احتمالاً حق با اوست.”
این در واقع وارد کردن کمونیسم به ایالات متحده آمریکا است. هیچ‌چیز تا این حد خطرناک نبوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67057" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67056">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oI0KzE6Y-e5P3TZ7ipG8yqEIub4AAg9iTeUH69eOJ7AC2EyNA7skU4Tn4dYoQTjdGKgoHp9QUBn22eQqFCL78QpJtj6ywJ71qGqSKaVdZ4h8RqYfs7KOrpUK4Du29yUfw3iH_sFembXRWK1yXV-7ILB8xuShKng11emeM_otJeN4cpietLtVEns8kfqzS2Pu8hg925tqaWVWWHJNKuFQuf0Y6YpRSgiLFUzqxZA_aWkJXs9OaQUTexNiBHNeQ7jZv6NrPS2w4cgdVvkJH9RVAavqmGFWCB9QFPPwiumyWi6tbT82LH8NFiLOyHBaBQYhq-3ssZ_-oJlk8zjfQ7b47Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67056" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67055">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=WhFfz5uAqvL4YuUijJQZ0Y03oUGmKEva340rp4wavRsYvn7du9cWC2Gx4Mw5X1lw2t35nH839ePYehAZt5ZrqqhlLhChDFgTb8DdPlIgn0MKWsXC-oN0AzYC21PblDBEcdUmHFgxFsb7WNTeNHuf8C-8XAot9iKWoAhRV2nRi-6Bjoy5s352yt5Al8zL3wIEuMYGr6VII55ONfAakl21W98Kkx_n6eeyurbrW3NmACIpCjxh7QTlKAopkHATbEiOtahLwqCX7bSH2l8hwxBh1AQ8nClaiQDEYVMDghD4B-rXEDtAzRTYF1CSeDmDtlo4YVue4n4FXxyCINfRZ2ThOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=WhFfz5uAqvL4YuUijJQZ0Y03oUGmKEva340rp4wavRsYvn7du9cWC2Gx4Mw5X1lw2t35nH839ePYehAZt5ZrqqhlLhChDFgTb8DdPlIgn0MKWsXC-oN0AzYC21PblDBEcdUmHFgxFsb7WNTeNHuf8C-8XAot9iKWoAhRV2nRi-6Bjoy5s352yt5Al8zL3wIEuMYGr6VII55ONfAakl21W98Kkx_n6eeyurbrW3NmACIpCjxh7QTlKAopkHATbEiOtahLwqCX7bSH2l8hwxBh1AQ8nClaiQDEYVMDghD4B-rXEDtAzRTYF1CSeDmDtlo4YVue4n4FXxyCINfRZ2ThOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67055" target="_blank">📅 00:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67054">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1336110317.mp4?token=MjPZiOst5ay4CtDj5rr2qDwkiyHF5xOYA4R_59f7QexwgPiMOTeduR541lVmbE8mgkpj1i9d41fqKINVtyssCj1j8EmHAfCy6F1Yudbgv9ZnniyTBeRJPRjM6ombobaM25Q9YRtZll-fYMtZ-oK_o20mwJpOHgCsb9lvtVkp_swqRDaDmLBfRh0MCExNKgKpbimEbX-6EoC7o6ek0sY1c96_6GPZw3ZI4_9Azl5o0KOU_LdWTwaFN9YlRogLc7-MS9gLqgW3ebOxcVf7ED3hrNKCp3z3qzBWRSJDdZ-NHp_S-q4aNYGSPV0ec2TLSkfvWfow0msZ6UhUQfE4U_JYkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1336110317.mp4?token=MjPZiOst5ay4CtDj5rr2qDwkiyHF5xOYA4R_59f7QexwgPiMOTeduR541lVmbE8mgkpj1i9d41fqKINVtyssCj1j8EmHAfCy6F1Yudbgv9ZnniyTBeRJPRjM6ombobaM25Q9YRtZll-fYMtZ-oK_o20mwJpOHgCsb9lvtVkp_swqRDaDmLBfRh0MCExNKgKpbimEbX-6EoC7o6ek0sY1c96_6GPZw3ZI4_9Azl5o0KOU_LdWTwaFN9YlRogLc7-MS9gLqgW3ebOxcVf7ED3hrNKCp3z3qzBWRSJDdZ-NHp_S-q4aNYGSPV0ec2TLSkfvWfow0msZ6UhUQfE4U_JYkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادگاه محاکمه ترامپ و نتانیاهو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67054" target="_blank">📅 23:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67053">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e959102c72.mp4?token=W-1aMnTHQ8STNM78cbPNO-wZkHutHgFSmRQ5WVx-87PXQuE-vG1QEJuSbARR8ASb-3D5QB9mdW8eJRhdfetZhJ3zHHCm9ym0zyfl4myQmI2utaTWS67qPK6aRouQL-3UAI585-e1uPtEQ68UqQatA8EQ3WnEffqoCCiNqutHejNFE1mc74gNcFh8_a7KasWIrtMfnysc4kmVz7qh5wb8Kv7Kuwdwb0IEnz5GhRg-i793oArp4kNyieUrdD7MgK4hMaYNxiNKabjwl0A10mAxqPa2yCZXAuAiCm9FYml094UjUyhWq7aG2THu-Ap-CBzBboS-0hXNpQOZ5kESAwpo4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e959102c72.mp4?token=W-1aMnTHQ8STNM78cbPNO-wZkHutHgFSmRQ5WVx-87PXQuE-vG1QEJuSbARR8ASb-3D5QB9mdW8eJRhdfetZhJ3zHHCm9ym0zyfl4myQmI2utaTWS67qPK6aRouQL-3UAI585-e1uPtEQ68UqQatA8EQ3WnEffqoCCiNqutHejNFE1mc74gNcFh8_a7KasWIrtMfnysc4kmVz7qh5wb8Kv7Kuwdwb0IEnz5GhRg-i793oArp4kNyieUrdD7MgK4hMaYNxiNKabjwl0A10mAxqPa2yCZXAuAiCm9FYml094UjUyhWq7aG2THu-Ap-CBzBboS-0hXNpQOZ5kESAwpo4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عزاداری پدر جاوید‌نام داوود عباسی بر سر مزار فرزندش.
جاوید‌نام داوود عباسی یکی دیگر از کشته شدگان اعتراضات ۱۸و۱۹ دی ماه ۱۴۰۴ ایران بود.
داوود عباسی روحت شاد
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67053" target="_blank">📅 23:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67052">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7iDHuqBqqL2CYe6oS90kGtqF9LQijEeJ3Pqi0gpq0pWbOFT9aGIfJVJPxCFTxTYk-TAd0J5iRc6KQL_dv4tAaX4hs2ryDYvflhuZSlWI0Fs94fpNZuX0F7OTvaWH-KNLIr9DEdwU6YHg2oTG1V8Q2ZOw_JWld5ncZ6-HoWInx2reEqh8KBhnvpBqBQBvNsJ9byphNDyTVS5phUJP8S8PwM1Knl-t8dpKc4j17CDKt1QMIsNdxDZQIAdmDWTTBlQck6vGZL2tH-BZONHiFmcr37WeVEq0_a1I-N78a0PVNWqHyKftK2eMkeNldU9CoDXs073eJ0_ShQlmbrBTd_QiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری فارس
:
معاون سیاسی نیروی دریایی سپاه طی سانحه کشته شد
.
دریادار دوم محمد اکبرزاده، معاون سیاسی دفتر نمایندگی ولی فقیه در نیروی دریایی سپاه، ساعاتی پیش در یک سانحۀ رانندگی بر اثر واژگونی خودرو در یکی از جاده‌های استان کرمان کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67052" target="_blank">📅 22:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67051">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‼️
اسماعیل بقائی: هیئت کارشناسی ایران برای پیگیری اجرای تفاهمات عازم دوحه می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به وضعیت اجرای بندهای مختلف یادداشت تفاهم از جمله در رابطه با موضوع فروش نفت و دسترسی آزاد به دارائی‌های مسدودشده ایران گفت: در رابطه با تعهد آمریکا طبق بند ۱۰ (فروش نفت) مجوزهای لازم از سوی آمریکا صادر شده و پیگیر روند اجرای آن هستیم. در رابطه با بند ۱۱ (آزادشدن دارایی‌های مسدودشده ایران) نیز فرآیند اجرایی شدن آن در حال پیگیری است. در این چارچوب، همین هفته هیاتی کارشناسی از جمهوری اسلامی ایران به دوحه اعزام می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به شروع مذاکرات برای توافق نهایی در چارچوب گروه‌های کاری تعیین شده، گفت: هنوز وارد مرحله مذاکره برای توافق نهایی نشده‌ایم؛ طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ و تداوم اجرای آنها است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67051" target="_blank">📅 21:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67050">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‼️
بقائی سخنگوی وزارت خارجه: هیچ‌گونه مذاکره‌ای با طرف آمریکایی طی روزهای آینده در دستور کار نیست
🔴
طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم و اینکه نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیات ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله بند ۱۱ انجام می‌شود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67050" target="_blank">📅 21:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67049">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=Td91oJBqDqRCDMrLV3p24PuyJ5lrFCtKgrIPy-qC3h1gtddc6-wHWcfiaxNYLeQd-RAO_Mb2_bwwpFeUTbCSxORV4LOvhIKQ50QCyUSVWkx2NiOD87_iVxAbB3l78ni3LtYUfrRKZeqAHy75PVZs9Uaxq_V4bnjsL_2DaXBva2kT9PYbgdQfg1lVKfGek27CdkAIZoPaAiiMuQGonFU5qS5f1nGM-10ND0-jafq8484NrVrlhdJr-u3THhsRUQVcW18F12qvHZglv0ZFzuKciIPYfy3FTYw0mY14FgK8ORgU_w8ycHAoNpsszyJyOOcIHwYcGpXbNbtCxK_JvAI2ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=Td91oJBqDqRCDMrLV3p24PuyJ5lrFCtKgrIPy-qC3h1gtddc6-wHWcfiaxNYLeQd-RAO_Mb2_bwwpFeUTbCSxORV4LOvhIKQ50QCyUSVWkx2NiOD87_iVxAbB3l78ni3LtYUfrRKZeqAHy75PVZs9Uaxq_V4bnjsL_2DaXBva2kT9PYbgdQfg1lVKfGek27CdkAIZoPaAiiMuQGonFU5qS5f1nGM-10ND0-jafq8484NrVrlhdJr-u3THhsRUQVcW18F12qvHZglv0ZFzuKciIPYfy3FTYw0mY14FgK8ORgU_w8ycHAoNpsszyJyOOcIHwYcGpXbNbtCxK_JvAI2ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناو آبراهام لینکن امریکا توسط سپاه غرق شد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67049" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67048">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=dLu2Nwnq9w8qZHtcrDfccQxzogXHiNCD5NDvSixZCGBOZQY5aaHSrfmUbUoP8sNIr-Xhby8sNWI1D_BPTFNsqZV_PAMAKavfwKIC4l2eeRIJ-QJI30Clih0nbSZhh8Odthyo7Wb5pDuwN9NmftS8sjo7PYU5nr9AhQQxns_8ViH1_xFC1Be-YgJGbT1id_Lg4X-nnILwokKRkHyEroIH-_uIaLlffjy8QCKX6ZCIkFUwjQfwOHqwxIGEo2W8TXi8exqnYRef-LTY4VcH8UiA4yqLRzVk3cZz1dKxM21CBxfdWqusyEPVtOTn_U31PrniD9vKRVTo6XN3V6cCO1o-kAVfCpwWSwbJ4iv-dw_G3gKe4Me477X3-LQF8iweFz0jbCW5bFzH19Qqj-c74EIL65L2qy0bANLQ2EPEw3__N8MHQE27gVMo0ZMqPndOZdL03AVslvb6R9W1f1avp8UBlQrlwr9aZIwW1OWEsAsvN0m5eF0JIrXOSR_j-gPJHM8-mq28sZv8eamjSyZtqfVH2JHJ2Kk8sd9huUpfZrDrgfvmGejRm61qL2p865KcWgycSfxs22RSH79-Go7XWj3HwuEQXvFh_uTSEQLts9AveyP7Urbha9v7TNH_07qnya5d9VcBz1sYWzw5dzrXxp6q6newbedQ7UY-saWQzZ_zyIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=dLu2Nwnq9w8qZHtcrDfccQxzogXHiNCD5NDvSixZCGBOZQY5aaHSrfmUbUoP8sNIr-Xhby8sNWI1D_BPTFNsqZV_PAMAKavfwKIC4l2eeRIJ-QJI30Clih0nbSZhh8Odthyo7Wb5pDuwN9NmftS8sjo7PYU5nr9AhQQxns_8ViH1_xFC1Be-YgJGbT1id_Lg4X-nnILwokKRkHyEroIH-_uIaLlffjy8QCKX6ZCIkFUwjQfwOHqwxIGEo2W8TXi8exqnYRef-LTY4VcH8UiA4yqLRzVk3cZz1dKxM21CBxfdWqusyEPVtOTn_U31PrniD9vKRVTo6XN3V6cCO1o-kAVfCpwWSwbJ4iv-dw_G3gKe4Me477X3-LQF8iweFz0jbCW5bFzH19Qqj-c74EIL65L2qy0bANLQ2EPEw3__N8MHQE27gVMo0ZMqPndOZdL03AVslvb6R9W1f1avp8UBlQrlwr9aZIwW1OWEsAsvN0m5eF0JIrXOSR_j-gPJHM8-mq28sZv8eamjSyZtqfVH2JHJ2Kk8sd9huUpfZrDrgfvmGejRm61qL2p865KcWgycSfxs22RSH79-Go7XWj3HwuEQXvFh_uTSEQLts9AveyP7Urbha9v7TNH_07qnya5d9VcBz1sYWzw5dzrXxp6q6newbedQ7UY-saWQzZ_zyIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی کارشناس برنامه خط انرژی به غیرقابل شکست بودن ناوهای آمریکایی اعتراف میکند:
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67048" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67047">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVABzn2kEKRfUGwEQ6u5uzirmVKmkD4ayLWlbgucLYFHgEthz9ScgEVEMrvXvw1rN7HY_aLJOH6nr3nSTQn9_qTK0IMqHO-67RW656Kbg35rwoWpN_xCYzT9LDrn2pd48tIm6l6ByYwI3cTWZCt1GlsEzaZlN5Xa3NvGMcl1Hhab-mBrIc6AjrQk3LUlCsH2LoHAW6_uEskXddTs4Sr3DpJWwaHtNMOO1a9MegHKLlIt_x2yDlQ2AFqH_9cXj_TqtmqWCvwO7dRyrlSrXGr5-Xj5UvopvWAd_fyLeXUAGc21KtrX2sMwCAGoR5A_MfTPnJGqhBe-FRHLcjHeyMnV4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67047" target="_blank">📅 20:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67046">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
نیویورک پست به نقل از یک مقام آمریکایی:
ما به ایران روشن کردیم که تا زمانی که پیشرفتی در پرونده هسته‌ای حاصل نشود، دارایی‌های مسدود شده این کشور را آزاد نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67046" target="_blank">📅 20:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67045">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=Fk8pS8ttHAWN-mIrPO5sFJLduiC-anFRV4VGrAdGVyyUNVEE6VAlHPxFRviHqQcGljily4LvFjS4P08pEH8etaLxh_EAslVj2rd5NIlBilkYBUqtJebbL8c_fhscQ2i21IRbmLuz_bixRkTVCpq6tZKS3N0gcjoHgfaBWy3t9kWb8pesd3mK-sKg4ki4hOlFGV2_m2Ryz0bxbvJE7R0uPGPtaUU_tCBRSNf1_wXvALTh9ObtNhilkxw0uddqf0baEd6snRWcQhzD4YhBpGqQ3aPFWw_ondMLjzGqCgi4aYD_K_OgY3LTRHqQDX6sk4TKtDJlUTiCLUjZpgGDX-pGIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=Fk8pS8ttHAWN-mIrPO5sFJLduiC-anFRV4VGrAdGVyyUNVEE6VAlHPxFRviHqQcGljily4LvFjS4P08pEH8etaLxh_EAslVj2rd5NIlBilkYBUqtJebbL8c_fhscQ2i21IRbmLuz_bixRkTVCpq6tZKS3N0gcjoHgfaBWy3t9kWb8pesd3mK-sKg4ki4hOlFGV2_m2Ryz0bxbvJE7R0uPGPtaUU_tCBRSNf1_wXvALTh9ObtNhilkxw0uddqf0baEd6snRWcQhzD4YhBpGqQ3aPFWw_ondMLjzGqCgi4aYD_K_OgY3LTRHqQDX6sk4TKtDJlUTiCLUjZpgGDX-pGIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان این تحلیل رو سال ۱۳۹۸ مطرح کرده بود؛ تحلیلی که از سال‌ها مطالعه و شناختش از روابط بین‌الملل میومد. حالا بعد از گذشت حدود ۷ سال،
با دیدن اتفاقات امروز حرف‌هایی که اون زمان میزد، داره عیناً جلوی چشممون اتفاق میفته.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67045" target="_blank">📅 20:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67044">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBiZQZTZqnybRtUd-4c3okjY0FaXAPunkUSDqSNOlvJf1JTJMnP6gpSDusalsd2p8x4ZN3lc4ugpDNiJpJ4U-KLwOXwZ8wD19RH3zpFf2_D2Z1rAofqFTiE2NfxDGX0KC02T8fdNhVarJyRZQHFMFRvr41IwF3MABp3vxBkPlEWlU0ApcmgB-znlt8Jw5WtX0DM2tCmfDjeF4FqPeCoOm4O7h4oB4fZTDKILuUW4GzKtkzB4PpExNmwuIEpzk1pZbHodkTGYbcf92BGrm3nOhvz80AaPJYKlDJljgv28tAB3I_B1dsYMw96Zkf4PQp7VnqMgMM9MC3wtsgdbr_W1Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حمله ارتش اسرائیل به دیر میماس در استان نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67044" target="_blank">📅 19:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67043">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز:
اگر ترامپ تصمیم بگیرد که مذاکرات به نتیجه نرسیده است یا اگر ایران به اسرائیل حمله کند، جنگ با ایران می‌تواند دوباره آغاز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67043" target="_blank">📅 19:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67042">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=hGJmQoqBodKrgzdJxtosEq6AT8SJCJjeBvMwRSM2CEVilcIF30NHnV2Shziv-gvlNMxFndM7F9u1obe2UjyDC-sr-5XVYopcUHKa10BURI-hCtCL94GJz0R29ppDI9_CQiXtGdV-2fG8OLMMCbtK3WY2HLYlKZpgV8I1-rsaFrG6LKhOleEzGcm0W2tzhv5RwtBCTt6v118AB2hW4tTg99W4lGH4EIDnhRt01LMsDG8Fji7PN6FNtap1VrCELMFZV2QtWt5_QoHrpCDUniWgbatqnPnXjcLz4PbgjH2CDyyZ4B-PUjKUwv0z16dzLZvMrXIXoih6nDFHDq9aRJq9xTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=hGJmQoqBodKrgzdJxtosEq6AT8SJCJjeBvMwRSM2CEVilcIF30NHnV2Shziv-gvlNMxFndM7F9u1obe2UjyDC-sr-5XVYopcUHKa10BURI-hCtCL94GJz0R29ppDI9_CQiXtGdV-2fG8OLMMCbtK3WY2HLYlKZpgV8I1-rsaFrG6LKhOleEzGcm0W2tzhv5RwtBCTt6v118AB2hW4tTg99W4lGH4EIDnhRt01LMsDG8Fji7PN6FNtap1VrCELMFZV2QtWt5_QoHrpCDUniWgbatqnPnXjcLz4PbgjH2CDyyZ4B-PUjKUwv0z16dzLZvMrXIXoih6nDFHDq9aRJq9xTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تردد در تنگه هرمز در دو روز اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67042" target="_blank">📅 19:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67041">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=TmmM9nQ4j0J9xC0TPXUq4jinl38Vq-1Bj-R32cBT5yDur1PzTkjFbHvq6P3e1FhF_jRVcit0VSJ9ReTiRbZ3m42hmyHBS83TkpZBMX6tOmkbTGnY_qIGeKzl3LGNAP6U6mkfhgh8YZd2ohneCyGQKX2T0IM5C6F-u96LZtRD8Yo3Z5Xw_ihkgjr9NstRGTuXuhKO5tbfWJjh32uxBfkEX7j_R5h4Wb8Qw8T-cQZ10paocYVLdS2rZgzYnuX1nmkNkm73UJRZv9fnt0Xbyjo8A3CgZPkcw_Boezt6780VXUSH_Cmt2SY8-NHvoPH9-sMXWRI1nfuDxeFEc5XAdRVL0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=TmmM9nQ4j0J9xC0TPXUq4jinl38Vq-1Bj-R32cBT5yDur1PzTkjFbHvq6P3e1FhF_jRVcit0VSJ9ReTiRbZ3m42hmyHBS83TkpZBMX6tOmkbTGnY_qIGeKzl3LGNAP6U6mkfhgh8YZd2ohneCyGQKX2T0IM5C6F-u96LZtRD8Yo3Z5Xw_ihkgjr9NstRGTuXuhKO5tbfWJjh32uxBfkEX7j_R5h4Wb8Qw8T-cQZ10paocYVLdS2rZgzYnuX1nmkNkm73UJRZv9fnt0Xbyjo8A3CgZPkcw_Boezt6780VXUSH_Cmt2SY8-NHvoPH9-sMXWRI1nfuDxeFEc5XAdRVL0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر امور خارجه قطر:
ایران یک کشور همسایه است. باید بین ما و آن تفاهم وجود داشته باشد.
آنچه اتفاق افتاد غیرقابل قبول است - هم علیه ما و هم علیه بقیه برادران ما در کشورهای خلیج فارس.
اما در نهایت، همه ما بخشی از یک منطقه هستیم و راه حل باید دیپلماتیک باشد.
ما می‌خواهیم یک منطقه مرفه ببینیم.
ما می‌خواهیم یک خلیج مرفه و یک ایران مرفه ببینیم که به طور سازنده با کشورهای خلیج فارس، با سطح بالایی از اعتماد و همکاری - به جای آنچه این جنگ‌ها به جا گذاشته‌اند - همکاری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67041" target="_blank">📅 18:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67040">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=lx_0x9Q1vbiSX7NDB43gueb8pBVWX15JAYYM84moO2PRGYq3pZw5lXj1fSOJ8WPb7cEL-0m3l0n5yDAyxCRvbgkDLq9UTAyE6QVNe1OKr_gY5SinAaEoyxYTMcU74HHE9GSif42lQdTfCErCeZUZbhibNA978DBD1gFyEiKafXbRcF38nv4hkpTRypOF8L7aLzFdLyFa2iQ3lW86391oAoOhK3pgS5rMiQr020ijLr8SMRDgjkufrIeMts-iJHr6tPO0IfjWVPHjvhNpo7Lexx9seggXzi0Dc0u_J9Zp07A6KnyYNTH2zQ6Qb_a2WABwZQJVtAWMgodbFNvMoSWpSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=lx_0x9Q1vbiSX7NDB43gueb8pBVWX15JAYYM84moO2PRGYq3pZw5lXj1fSOJ8WPb7cEL-0m3l0n5yDAyxCRvbgkDLq9UTAyE6QVNe1OKr_gY5SinAaEoyxYTMcU74HHE9GSif42lQdTfCErCeZUZbhibNA978DBD1gFyEiKafXbRcF38nv4hkpTRypOF8L7aLzFdLyFa2iQ3lW86391oAoOhK3pgS5rMiQr020ijLr8SMRDgjkufrIeMts-iJHr6tPO0IfjWVPHjvhNpo7Lexx9seggXzi0Dc0u_J9Zp07A6KnyYNTH2zQ6Qb_a2WABwZQJVtAWMgodbFNvMoSWpSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جزئیات اسکان و تغذیه در استان تهران در مراسم تشییع رهبر شهید
اطلاع‌رسانی رسمی جزئیات مراسم تشییع در کانال پرچمدار
👇🏼
t.me/Parchamdar_tv</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67040" target="_blank">📅 17:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67039">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=JgAkm-SS_nXGOTFd7QVYQ4yTL-4bCrBu7G7ZSvCWCk6JQBaF5CJgtFkF7XKuqIdR13O5iwOKnPT7q4BXbEyfouinIv4Nz6UoCdiAO3SjHCmgoadyEHV3ErS9qmU2jGi8m6ksAnWMhn_lIoBFyuHPlnV11V7mBwy4DEqFOmryKwl__KovGNuEnK4Cxtf6a7F8oMWSCPhBBAeE9WcCbwCflUqu9XgwD6B7wyNPhJK8f8LfZhN6qIjyijhmcha3VYesRpfbUvG4WeUKy0JGQDt7PdYvhMsXKFijowyA2tQUfFrg3mDBLpsf6nhbc6BdL2HTwzwppuPWg2QuqQItxRQuww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=JgAkm-SS_nXGOTFd7QVYQ4yTL-4bCrBu7G7ZSvCWCk6JQBaF5CJgtFkF7XKuqIdR13O5iwOKnPT7q4BXbEyfouinIv4Nz6UoCdiAO3SjHCmgoadyEHV3ErS9qmU2jGi8m6ksAnWMhn_lIoBFyuHPlnV11V7mBwy4DEqFOmryKwl__KovGNuEnK4Cxtf6a7F8oMWSCPhBBAeE9WcCbwCflUqu9XgwD6B7wyNPhJK8f8LfZhN6qIjyijhmcha3VYesRpfbUvG4WeUKy0JGQDt7PdYvhMsXKFijowyA2tQUfFrg3mDBLpsf6nhbc6BdL2HTwzwppuPWg2QuqQItxRQuww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه داماد، وسط مراسم عروسی تازه متوجه میشه عروس 11 نفر از دوستای پسرش رو هم به جشن عروسی دعوت کرده؛
گفته میشه داماد اول فکر می‌کرد اونایی که دور عروس حلقه زدن، فامیلش هستن؛ اما بعد از پرس‌وجو می‌فهمه همشون دوستای صمیمی عروسن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67039" target="_blank">📅 17:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67038">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=dIv7YDUigPwQkP9_Rfy5Bv4WK49vkhcSy6L6iU-INsZeHhHq-gMr1XVpiwyZCATBoLCv4v8KdzPEe6oE9g8ZgxC6P-L6_3f4tnn91uOxTrM6a_r56MYV4OfVtdNSBGYf-FmCRCjHh9yevrnz_O8x-EOoYauJWqBVVwEIdqyq3IUAjNLIF3X40e0rKH-a4f3ljBLoE5g143k0pmaO52orqygRgMsfHV7v1y2rXb-BQjV9u6U-of-ZyJ_JuVFHNMm9vKc1ixWSVhSwDIUnLmjlN8NmkIYe5iP8qC7Grq9VMSU_S1bQASA0ZCErgQH8V8Z7W8oYJPAR2kojVnA1D88CqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=dIv7YDUigPwQkP9_Rfy5Bv4WK49vkhcSy6L6iU-INsZeHhHq-gMr1XVpiwyZCATBoLCv4v8KdzPEe6oE9g8ZgxC6P-L6_3f4tnn91uOxTrM6a_r56MYV4OfVtdNSBGYf-FmCRCjHh9yevrnz_O8x-EOoYauJWqBVVwEIdqyq3IUAjNLIF3X40e0rKH-a4f3ljBLoE5g143k0pmaO52orqygRgMsfHV7v1y2rXb-BQjV9u6U-of-ZyJ_JuVFHNMm9vKc1ixWSVhSwDIUnLmjlN8NmkIYe5iP8qC7Grq9VMSU_S1bQASA0ZCErgQH8V8Z7W8oYJPAR2kojVnA1D88CqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جان کری، وزیر امور خارجه پیشین آمریکا، درباره ایران:
اوباما تحت فشار و اصرار نتانیاهو قرار گرفت تا در بمباران ایران مشارکت کند.
و از اوباما درخواست شد که اجازه (چراغ سبز) بدهد تا این اقدام انجام شود.
اما اوباما گفت نه و از مشارکت در آن خودداری کرد، و آن را یک اشتباه بسیار بزرگ می‌دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67038" target="_blank">📅 17:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67037">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=fAk4Q2kQ-hgT0nnI_Bc4g_Ttj97WZ5vQExXTVPYbKRAjC1TrMgMNAg61FdjY43omQoUA4mSTeMChVu0S6QLhXFNOfh7tNxe2ylUHgrNngKrwhPOCGzbpwkzXKmU775-5VmXjgqxLqTcCJMQksjzUPA_t97VDo8N2EYoPRQRDV3qqnS_-m8thyHFYT7fiun2OPk-xd8b7V0Ck0pbzJrNOjn5hhCV44sYA3iGp9nfkwNccbq7QMUdZ833GdSR8XwWKsVGGuAHIwtebeIt2kPHtZ0z2AJm24NilgIbXnNIfkm93x7WSQO03xKw2RbikvXb9a-O7c0oxNT5upXEv-0d_xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=fAk4Q2kQ-hgT0nnI_Bc4g_Ttj97WZ5vQExXTVPYbKRAjC1TrMgMNAg61FdjY43omQoUA4mSTeMChVu0S6QLhXFNOfh7tNxe2ylUHgrNngKrwhPOCGzbpwkzXKmU775-5VmXjgqxLqTcCJMQksjzUPA_t97VDo8N2EYoPRQRDV3qqnS_-m8thyHFYT7fiun2OPk-xd8b7V0Ck0pbzJrNOjn5hhCV44sYA3iGp9nfkwNccbq7QMUdZ833GdSR8XwWKsVGGuAHIwtebeIt2kPHtZ0z2AJm24NilgIbXnNIfkm93x7WSQO03xKw2RbikvXb9a-O7c0oxNT5upXEv-0d_xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو ای دردناک از لحظه وقوع زلزله در ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67037" target="_blank">📅 16:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67036">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=P9yRZWmQr8GPY_QYfBtrizVzOiMgXk1ytpXmz_Tua_pRBg43aa30Z5SWTC9046gknAickm2mTXWtcV8PXljpFxT6_e6lpiVK_MOrB7bGZnE6bBY9Tir8lwPb5QOUluwsTe3Hoj09zPO2kDCIZUmPmKZ06QlwfVkSq0wmSeAYPcSNe0aoc7rLSxAbhQ7633wVpRXlM6Bw0NPoutcGmbwS1RDo8drLZGmyo18JAJ9TrHfgU-TpVfXXnfUXj1wMocVg0S_wqeQiagCzkc50f4E_RQk1ikTX_30RWATl9ArVQ5R8xu7dThNPSXLhP4dIV996gNVL4nsTLiF7XDPvOGvMVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=P9yRZWmQr8GPY_QYfBtrizVzOiMgXk1ytpXmz_Tua_pRBg43aa30Z5SWTC9046gknAickm2mTXWtcV8PXljpFxT6_e6lpiVK_MOrB7bGZnE6bBY9Tir8lwPb5QOUluwsTe3Hoj09zPO2kDCIZUmPmKZ06QlwfVkSq0wmSeAYPcSNe0aoc7rLSxAbhQ7633wVpRXlM6Bw0NPoutcGmbwS1RDo8drLZGmyo18JAJ9TrHfgU-TpVfXXnfUXj1wMocVg0S_wqeQiagCzkc50f4E_RQk1ikTX_30RWATl9ArVQ5R8xu7dThNPSXLhP4dIV996gNVL4nsTLiF7XDPvOGvMVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حصیر آباد اهواز؛لحظه ساییدن سیم‌های برق شهری با «برج میلاد»:
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67036" target="_blank">📅 16:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67035">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
سخنگوی کاخ سفید:
استیو ویتکاف و جرد کوشنر، در نشست روز سه‌شنبه در دوحه با جمهوری اسلامی شرکت خواهند کرد.
همزمان با نشست‌های مقام‌های ارشد، گفت‌وگوهای فنی نیز برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67035" target="_blank">📅 15:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67034">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVfL_x8OTpIxvRYQ_oXC1sPSw-IXVoSgta2Wua_YhLlkAlkeIDudV8kIHIrnj1sS9Lb28f_izBq9UWDBvvE0S89WhPR27r42Nyz8BesPYK51IcV01kRBFAxD13wb8g87KRCK-X39Vyvx7jsEC05WaZGUI1kn-LQXVyOgEurSBwazhVgBNb-8KUPtqkWuhRZrA3wHgODu14Mb98vv7FMmzW_apV91Ut61k6dsynJrQCk41CPKPv1P8OiViLU4MHFBRVyjW_ndEAwl-4nJippBi1U2pmVzpm2FU8LQgixU9i2pYEavtJZu8LoEh10qvLBemglUEJ6rLK6KGBJWQwe1uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران درخواست ملاقات داده است. این دیدار فردا در دوحه برگزار خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67034" target="_blank">📅 15:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67032">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmrWm-aVT_qaMeC71I2tX1-e2bHt4SSMp9PVY2yBQqv0cJy_Qnrk7JawCu7xU-avPY6kH7a51-NAx-6oji9FnHU2fyQ6nOXIvkSoZsgo3jBVnu8McX9Rx6I-awQTkQLcIPz4tbvIU_JNrg_ZcfOoIeJHPt4OYxn--sxGtW6NsTWPd0Lg5q3i8LVCQEFGy4yeSX9tyqPBCxZfSnSafMSlsOgKv7HWPdy9ouv-eTQPmnr06GOMckm3VqKbb3LykOL6Es2ZnSR7BCb4RvMyRSKQvEyo7pLe8H6FiU968Dy1pr7nX7ZcLGWyIQ3Zflv3VAW794wY3BBdQkRfpXcfTE8qOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در تروث سوشال:
محبوبیتم تو نظرسنجی‌ها از همیشه بالاتره
حتی از روز انتخابات ۵ نوامبر هم بیشتره؛ با این حال ایران نباید سلاح هسته‌ای داشته باشه
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67032" target="_blank">📅 14:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67031">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8SZbFScgKoyt_5sdtz-FBeSg-7qqcq11auwzMA1mhT1opRHlyVr939qEL-AqYD0pLYN034PFR7rDwQTobjf-qCzIalJM6B3LCKk0kRb36z5Ex9xx8sFePjm0Y6IGWd-tN9jCFbH3e5P5rnacdJ4GRW01iUSqCJ8OSeqKS4UY7NBtLfLdKKY5VOiu1nQLbo_QtBjvs78zQF-9AMTIF-Gg-3cyJLJmSpcCnemj15qM58nMbCSybTziXyVfc4JkXV_y437VbkQA_l69R0CpzO8u8evv2k_fdyrSatUhqnKPhqGYHOpHFWzJEXHQ6FfexigiVHSeENogyv8uXGERYa_jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حسین شریعتمداری (کیهان) :
گام اول تحقق خواسته‌های رهبری در مذاکرات، تاکید بر تحویل ترامپ به جمهوری اسلامی برای محاکمه در مراجع قضایی ج ا است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67031" target="_blank">📅 14:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67030">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=cJ0Un35a-Sno8uRT9Fk3VDQ2LtpW19L0LGrttEEXT2LeUqe8DVajQoWKIapmuZBSLR-LZh2W2aAy36hVC1GXnzKAUON6ZqChV1EJoTk-70SFwgXTnFJ0O3W6g5DeSktrVuvKL_-svTr-V9LgItZLHiEs-qDv5FOQpIHfh3QS_lsu1Id8WKRjfYrmkguk730zdS05Tg0_zQsrQzBu2J4NCIN4h2Khypq_WYALZ1ejlH1CdoEOSwiOjAUZGHa3zY1Hvb5W6XFeBQ3nqQNzQI4FbTOGm1xlP_SqiS2w9dyLUOEbG5wwuDjL6MaUTYQtx7fmWLndn4KCH8vsNkQFsqKrQHkF1u732IyvgATdWjKavFHxD0Xa5yx9i0-S6niD7ldH1J67rjFmtebSZV2PlEuGF1pLm0zPJYolx2MhuwZV29-HNjA3JkFiLdadc6WRX0Wps7muxQq8sq5JyWp3OZWcliQi2Ba_VULYklM-X8N7ZlbSVBmHR1NpScHj_OHbw1E_ESok-BKpaIC4PjXoKRSNMfJUo8x0qOzs0nzhFuYQyB9r8hAeImbhieXR0HcjzKcWgiS40upWJPpfd28C3-5ikEB7QQWv9DtdHlKPYkyoVwJYW8xscDLdzz-R2vHzqOUt5jq861New5RaxXrG_w8BxWF0uUlY40T8ow-8ODfY4bE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=cJ0Un35a-Sno8uRT9Fk3VDQ2LtpW19L0LGrttEEXT2LeUqe8DVajQoWKIapmuZBSLR-LZh2W2aAy36hVC1GXnzKAUON6ZqChV1EJoTk-70SFwgXTnFJ0O3W6g5DeSktrVuvKL_-svTr-V9LgItZLHiEs-qDv5FOQpIHfh3QS_lsu1Id8WKRjfYrmkguk730zdS05Tg0_zQsrQzBu2J4NCIN4h2Khypq_WYALZ1ejlH1CdoEOSwiOjAUZGHa3zY1Hvb5W6XFeBQ3nqQNzQI4FbTOGm1xlP_SqiS2w9dyLUOEbG5wwuDjL6MaUTYQtx7fmWLndn4KCH8vsNkQFsqKrQHkF1u732IyvgATdWjKavFHxD0Xa5yx9i0-S6niD7ldH1J67rjFmtebSZV2PlEuGF1pLm0zPJYolx2MhuwZV29-HNjA3JkFiLdadc6WRX0Wps7muxQq8sq5JyWp3OZWcliQi2Ba_VULYklM-X8N7ZlbSVBmHR1NpScHj_OHbw1E_ESok-BKpaIC4PjXoKRSNMfJUo8x0qOzs0nzhFuYQyB9r8hAeImbhieXR0HcjzKcWgiS40upWJPpfd28C3-5ikEB7QQWv9DtdHlKPYkyoVwJYW8xscDLdzz-R2vHzqOUt5jq861New5RaxXrG_w8BxWF0uUlY40T8ow-8ODfY4bE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش چشم کارشناس صداوسیما:
آمریکا فقط به دنبال باز نگه داشتن تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67030" target="_blank">📅 13:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67029">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbJka_RmGloGMun31xpk2B-BaFurpE3fpMHL9cFjIKEFmN7dqP1eYyMOMm5lAEREtldMnCuc0yAkpltvAR0YI7unCFhAbfu00XDAkCL4HUSYLbDqtyKeoZPIUrK9tm0dnZk21u5sL6ponXKCZmMUXOrI1P2WJCfwJflctejS2pPbG7Qj6DAqYg8M1L49GSg2WSARV08MpxMzwPrF9Lll5QGp8JpCFIs6SkartVqhip3AgFm5ZsjYoYFdweYekxSdPf1pyAXDot3t6wDFhOeSeUaaCL-GxJtAlXtTgOaaAr_CZGD-93rTJmKcugIrj2_sEW_9jntB0p3dAmCCEI3cLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی : قالیباف ٬ عراقچی پس خون رهبرم چی؟!
واکنش صادقانه ممباقر و عباس اقا:
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67029" target="_blank">📅 12:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67028">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706d335e17.mp4?token=ixgkXZJlP-ZB0tZM40EdIV2PGTysDkBoK3zfcpsUvxxn-i4zyF2k4SmMbikFMbyxsrC9SdpOxj8Tnxbh5f8PB0TClvtqeQj1YhzWsnSWZxshYqN82JlxLNIaFIwyUOrbRM0e--qNu4Yvjr_GpjF1ObE2_wd31OEn9HsHUp8ALYkhxQye7c6sK3vuolqQZH6Eyz7xd0dvLGEYuuI7UtkNd1mM9cte304HWMwMbEmUzHAzGMKGyE2LbM2XJqG717gIpIkSTRMl-5XQDFAfCOxtUbTJ1jcC_iPPPcQXNbsychSMS8HrwlNR0PBykVEPwwVowj3KFYunZoaSGaw1SraDCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706d335e17.mp4?token=ixgkXZJlP-ZB0tZM40EdIV2PGTysDkBoK3zfcpsUvxxn-i4zyF2k4SmMbikFMbyxsrC9SdpOxj8Tnxbh5f8PB0TClvtqeQj1YhzWsnSWZxshYqN82JlxLNIaFIwyUOrbRM0e--qNu4Yvjr_GpjF1ObE2_wd31OEn9HsHUp8ALYkhxQye7c6sK3vuolqQZH6Eyz7xd0dvLGEYuuI7UtkNd1mM9cte304HWMwMbEmUzHAzGMKGyE2LbM2XJqG717gIpIkSTRMl-5XQDFAfCOxtUbTJ1jcC_iPPPcQXNbsychSMS8HrwlNR0PBykVEPwwVowj3KFYunZoaSGaw1SraDCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
آتش‌سوزی گسترده در پالایشگاه اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67028" target="_blank">📅 12:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67027">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
پزشکیان:
بر اساس برنامه‌ریزی‌های انجام‌شده، شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع در قطر، آزاد و به کشور بازگردانده خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67027" target="_blank">📅 11:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67026">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=djjRQ4xMIaAIljIeiauYaHdkjKVMOpV2C7KuBFaXzPXdyWNr3IIaMpIWztOVN4fNqxeBzDiqRPfYwyc7We9d7IppPRufnLMwXZCraJYL2TOBHOU7BOu75Rltft0sSPZ8Ww4w24TEniamjGa0Wjch6GIM-V8Qf9m_NOTxz5cADDSShY_OEDvkPmritykcaUPMPydFKz8GwnbkD0W8ZvlaEi8RkreAS-XlTNw_S4ZDFrPD-cT22nKQ_k-dDmkcYRNMGWl-rj8xXy-oHeO52tOssM5ZFRspcq_N6GdVM4XTf9_qmoHiTMSySWop-BirGmKGEYrsGRyEWpcuRDNiAJOAWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=djjRQ4xMIaAIljIeiauYaHdkjKVMOpV2C7KuBFaXzPXdyWNr3IIaMpIWztOVN4fNqxeBzDiqRPfYwyc7We9d7IppPRufnLMwXZCraJYL2TOBHOU7BOu75Rltft0sSPZ8Ww4w24TEniamjGa0Wjch6GIM-V8Qf9m_NOTxz5cADDSShY_OEDvkPmritykcaUPMPydFKz8GwnbkD0W8ZvlaEi8RkreAS-XlTNw_S4ZDFrPD-cT22nKQ_k-dDmkcYRNMGWl-rj8xXy-oHeO52tOssM5ZFRspcq_N6GdVM4XTf9_qmoHiTMSySWop-BirGmKGEYrsGRyEWpcuRDNiAJOAWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات سنگین به جنوب کشور در جنگ اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67026" target="_blank">📅 11:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67025">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این کلیپ داره مثل بمب وایرال میشه، الجزایر گل سوم رو زده اتریشیا دعوا کردن که چرا طبق توافق پیش نرفتین‌...اونوقت بازیکن الجزایر اینجور با دست نشون داده که مساوی میشه نگران نباشید و ارومشون کرده  @sammfoott | پروکسی متصل</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67025" target="_blank">📅 11:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67024">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=BRIpVGLNDKgveB5du61eMuxYZ1DXys4inSiQ8jsYV6yoCAmRrwyzRx6vcPWfjKbjUNtlbuBBvH32iNLaYi7nlmI3E5gL6_6OvHK8KIh_MNCAlmqAQ9pyM0FsvOATy4Gm69GE_tKbq8SVjMOp_2PfvZYfdMZfwZpqz1VzsF5chswBH6hKXRpjGCW_wJOGV7RgVts2cs5PuGr_zDT6v82wfYPJ9Zi66PUwPk1jgTdgSAq1Biyi4rQfWaVEIN-I9fQYqWky0SN4kqcu8-JtMTMeA5xYDtSEnOHbGWcPD5VNg_tENpreq0qMzNM_ETUbLzyN5GWvUg-N7cB00q0RqJUGXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=BRIpVGLNDKgveB5du61eMuxYZ1DXys4inSiQ8jsYV6yoCAmRrwyzRx6vcPWfjKbjUNtlbuBBvH32iNLaYi7nlmI3E5gL6_6OvHK8KIh_MNCAlmqAQ9pyM0FsvOATy4Gm69GE_tKbq8SVjMOp_2PfvZYfdMZfwZpqz1VzsF5chswBH6hKXRpjGCW_wJOGV7RgVts2cs5PuGr_zDT6v82wfYPJ9Zi66PUwPk1jgTdgSAq1Biyi4rQfWaVEIN-I9fQYqWky0SN4kqcu8-JtMTMeA5xYDtSEnOHbGWcPD5VNg_tENpreq0qMzNM_ETUbLzyN5GWvUg-N7cB00q0RqJUGXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67024" target="_blank">📅 10:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67023">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91138929a8.mp4?token=qCf1pR0Wgt-UIS3cCq6XIer6sUQ4tQdbITfBrfH3_G4j9IP_ETHOuKWq60oUfVGMqtQTghTRKWfrneAl23n8RZU_E9VbJaZSb8hVoTOlSKOXyYe8zKS5X6dHyCHkW8bBQwsdOLVd_ABszD2SVcQXov3pTPLbbZPA96gbwRggpUBXURpqnpa4OIlGFRlGqzPH2SsN98sois3zjX78ujFJMi4uMDDviAi75oVEWVhiq3PrxDRZpZpj9yxwSCLEp6s9aC_azOQJVORbY-CG8Nbsa2v_NBsyWJa9JNbICO7rBzQgxxlEujoWNlM-pGOClX76rOirSb-PyTl_nUHxaYgW44WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91138929a8.mp4?token=qCf1pR0Wgt-UIS3cCq6XIer6sUQ4tQdbITfBrfH3_G4j9IP_ETHOuKWq60oUfVGMqtQTghTRKWfrneAl23n8RZU_E9VbJaZSb8hVoTOlSKOXyYe8zKS5X6dHyCHkW8bBQwsdOLVd_ABszD2SVcQXov3pTPLbbZPA96gbwRggpUBXURpqnpa4OIlGFRlGqzPH2SsN98sois3zjX78ujFJMi4uMDDviAi75oVEWVhiq3PrxDRZpZpj9yxwSCLEp6s9aC_azOQJVORbY-CG8Nbsa2v_NBsyWJa9JNbICO7rBzQgxxlEujoWNlM-pGOClX76rOirSb-PyTl_nUHxaYgW44WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
🇮🇱
بنیامین نتانیاهو، و یسرائیل کاتس، وزیر دفاع اسرائیل با انتشار بیانیه‌ای مشترک از کشف و انهدام یک شبکه زیرزمینی در منطقه «مجدل زون» واقع در جنوب لبنان خبر دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67023" target="_blank">📅 10:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67022">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HK85oGWyzA2go0-NmIz9t6LjbVBDXLIaKMsZiup7TyWP3dY8T1CR8sUVIRqpTSEpPLBWZEMghFq9jbByPAvZrvfPxzbQxlWvDvTjNV5yp9No2N3pIefW3e1LCyNcLtlOTDkAlygnnqf5y6lbW1kpwjj3pw2N8RqpfpbCizmh1voMmCQfbIR_qx38ON3oXsY9LMc0I7dZvTnDZFzpoFGJOWqREgTek1Z0g8dv6jpl8M3MXV3KAXj2VOri0CFPwnzfmur4568xpV55_JLUyznSsfhxFyzqX8musq6CUUEoZJOZbgy6GEZXV7DYFaKOP9YVS52zHYtMerQhmqRsyL4rZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شاهزاده رضا پهلوی:
🔴
‏از ۴ تا ۹ ژوئیه (١٣ تا ١٨ تیر)، هم‌زمان با برنامه‌های تبلیغاتی و فریبکارانه رژیم برای دفن بقایای جنایاتکار اعظم، علی خامنه‌ای، و در ششمین ماه خیزش ملی شجاعانه ۱۸ و ۱۹ دی، ایرانیان مهین‌پرست و آزادیخواه در قالب هفته جهانی اقدام برای آزادی ایران، به خیابان‌های سراسر جهان می‌آیند، تا واقعیت ایران را به گوش جهانیان برسانند، و هم‌زمان یاد جاویدنامان انقلاب شیروخورشید ایران را در ششمین ماه کشتارشان گرامی بدارند.
🔴
این کارزار ملی با گردهمایی‌های روز ۴ ژوئیه (۱۳ تیر) در برابر سفارتخانه‌های ایالات متحده در پایتخت‌های جهان آغاز خواهد شد.
🔴
پیام ما به ملت و دولت آمریکا در سالروز استقلال این کشور مشخص است: با تروریست‌ها معامله نکنید! مردم ایران را انتخاب کنید.
🔴
۲۵۰ سال پیش، آمریکا آزادی را برگزید. امروز نیز مردم ایران برای آزادی مبارزه می‌کنند.
🔴
معامله با رژیم جنایتکار جمهوری اسلامی در تضاد با آرمان‌ها و ارزش‌های ایالات متحده و جهان آزاد است.
🔴
هم‌میهنان در داخل کشور نیز می‌توانند با حفظ امنیت و پنهان نگه داشتن هویت خود، از طریق ضبط ویدئو بر مزار جاویدنامان، دیوارنویسی و دیگر روش‌های خلاقانه، پیام‌های مشابهی را خطاب به ملت و دولت آمریکا منتشر کنند.
🔴
برنامه‌های دیگر هفته جهانی اقدام برای آزادی ایران به مرور به اطلاع خواهد رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67022" target="_blank">📅 09:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67021">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‼️
آتش زدن متن تفاهم‌نامه توسط یک مداح تندرو
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67021" target="_blank">📅 09:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67020">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67020" target="_blank">📅 04:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67018">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dqLB40QJ59ZSB2A4fkfFI6oOpwLnJluo4i545Eh3jk3ZEw5_TaVKOPtwHWUBWeWUTWmd7F0KmeBMSMDMbOzLKbX0Ew4YLayBuH5iDoKeFbmSyenUqi2e0kvBKDD-ZA71PeLv0HpAo0KS5Bz2t85hdwHwCoPIjfVMMwdoqpjyDQasdldI4f-pA-ub_MopyIWh-rRaENHew-VXNVttCWXFwHapnOjhDo5cp6_IROSAPplfgJMIwGeK1Mu4cZdS2QibOEaBqjT7QlOWII2xoNhL6oRAORX6l3HPX8x0tUm-Kw7YmADkMczugdmWam_UjOGFfBqZaEM2Vlx3k-DCFhMsPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67018" target="_blank">📅 02:16 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
