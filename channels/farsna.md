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
<img src="https://cdn4.telesco.pe/file/pJwSRWTig1jkD3fhs25AyJkqQT5NSo0X86LUe_avbTqs2YZGEV8g4PApj-8rIj06_G960G0iScRxRrCoGfcA9wZ2xKVnfRySzCXAPQ9gVwSxbtlpmnCJUoENM6BkNvGCTNl4QQpX7Cy1WWcK8Iwhbfo5pQyFpc56KQLaXDpDgkLX-8FX2Cv8y30OWyECl-3v5LjvlLCyIcL782aZGZQlOpYpF6UP4qfTrSLcy3KSYMbSCdWGsRAQLkJgJjIgEy6kc2CEc3k-S_eK0qPdktAoQlOKIACafo7T02AvSUANWaS9y5OYcq6BZWSNvfRgibQShgSS3nQeR9F19fVJFQCQ_g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.79M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 11:06:32</div>
<hr>

<div class="tg-post" id="msg-454704">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تمدید فرصت ثبت درخواست معافیت سربازی برای مشمولان دارای ۳ فرزند و بیشتر
🔹
سازمان وظیفهٔ عمومی اعلام کرد مهلت استفاده از معافیت خدمت سربازی برای مشمولان دارای ۳ و ۴ فرزند تا پایان سال ۱۴۰۷ تمدید شده است.  شرط سنی استفاده از این معافیت چیست؟
🔸
مشمولان دارای ۳…</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/farsna/454704" target="_blank">📅 10:49 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454703">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48cd5ccefe.mp4?token=qKWzUNUoLYQO7TxYkQ2NMcQK-0lZkI1xxghS8gKKVXdhf7TDm301eHKmA2XRUYk1ESVIpFxLjoL8oIIIU8D-pbWMFFgpXlQUhZzVQ8Edqczci5-QcX3m6nD_-7v4DYiQ0kwZc2NZG5KFfe4aU69jw0InQpEWW49YUE7YuWwXArFqubu6JIk0Kk-dqLXjJzIK5go6rnR_YFbrESfUMl3g687ULeR_X1DVWvRJfXiZ519Mqk4muAdhqjxTh7t_DURabAtXnhtfJghwBw7E_rl9vys47C4QXZnXXiFhW6J4-B2kjrSP-WT54ttE3stl96IrfnmKAWb8q0P6W_61eeAlTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48cd5ccefe.mp4?token=qKWzUNUoLYQO7TxYkQ2NMcQK-0lZkI1xxghS8gKKVXdhf7TDm301eHKmA2XRUYk1ESVIpFxLjoL8oIIIU8D-pbWMFFgpXlQUhZzVQ8Edqczci5-QcX3m6nD_-7v4DYiQ0kwZc2NZG5KFfe4aU69jw0InQpEWW49YUE7YuWwXArFqubu6JIk0Kk-dqLXjJzIK5go6rnR_YFbrESfUMl3g687ULeR_X1DVWvRJfXiZ519Mqk4muAdhqjxTh7t_DURabAtXnhtfJghwBw7E_rl9vys47C4QXZnXXiFhW6J4-B2kjrSP-WT54ttE3stl96IrfnmKAWb8q0P6W_61eeAlTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۸۰۰ سازۀ آمریکایی خاکستر شد
🔹
آتش‌سوزی‌های مهیب هفتۀ گذشته در منطقۀ اسپوکن، واشنگتن، دست‌کم ۸۴۶ سازه را ویران کرده و بیش از ۶۰ هزار نفر را مجبور به ترک خانه‌هایشان کرده است.
🔹
مجموعۀ آتش‌سوزی اسپوکن از ۳ حریق جداگانه تشکیل شده که تا روز سه‌شنبه بیش از ۱۰ هزار هکتار را سوزانده است.
🔹
به گفتۀ مقامات، یکی از این آتش‌سوزی‌ها عمدی بوده و مظنونی در این رابطه دستگیر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/farsna/454703" target="_blank">📅 10:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454702">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128a1a4b69.mp4?token=poBhDMTBYI2bV5UjwX5PPzWkXtibl6gDegpXOrfwkUWe1t62KQA-RawtG8V-3vZg27plvLmLtKJb8Y22tco7oQMjkFyDDP3lQZsamhb8Tr0sP1odwwn2uuFqeu3IwQ8QyrNQMFeqEdLkRgzQ9mQDkX4KaEKWYrwlP4PVGvCyTbElV-rrw6eX0M_2_xNSrZi7DPmsM2xXX0gdof0MYIfR0q1rGUXAtIKGPCGaQt5jNlOdDPJNZpad0emllHr6LV1GvF6ju6EWzeBTaUyn59SUUOr3FElAsyxBr-ZG5UrE8y-6rlFVNS0nkEfPMkYbq9-SynFA7u1a8MuhB2sU6KROfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128a1a4b69.mp4?token=poBhDMTBYI2bV5UjwX5PPzWkXtibl6gDegpXOrfwkUWe1t62KQA-RawtG8V-3vZg27plvLmLtKJb8Y22tco7oQMjkFyDDP3lQZsamhb8Tr0sP1odwwn2uuFqeu3IwQ8QyrNQMFeqEdLkRgzQ9mQDkX4KaEKWYrwlP4PVGvCyTbElV-rrw6eX0M_2_xNSrZi7DPmsM2xXX0gdof0MYIfR0q1rGUXAtIKGPCGaQt5jNlOdDPJNZpad0emllHr6LV1GvF6ju6EWzeBTaUyn59SUUOr3FElAsyxBr-ZG5UrE8y-6rlFVNS0nkEfPMkYbq9-SynFA7u1a8MuhB2sU6KROfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ خلبانان ایرانی بدون GPS به پایگاه آمریکا
🔹
معاون هماهنگ‌کنندۀ نیروی هوایی ارتش: خلبانان ما آموزش‌دیده بودند که بدون استفاده از GPS و INS، تنها با نقشه و سامانه‌های ابتدایی، هدایت جنگنده‌ها را در ماموریت‌های مختلف تمرین کنند.
🔹
شاید برگ برندۀ ما این بود که هیچ‌گونه سیگنال خروجی، حتی سیگنال رادیویی، از هواپیماهایمان وجود نداشت و احتمالاً در روز نخست، دشمن تصور نمی‌کرد نیروی هوایی جسارت اجرای چنین ماموریتی را داشته باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/farsna/454702" target="_blank">📅 10:35 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454700">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u593cs0psuiaPSbMIP_Zdk8Vxnmjr2YRgwep1GS9sqlNZlMAFLNXJ4rV_57ljAg6JXpfOZ1Ai-O9y9paHFS65Mgzky7AHTyCtPXe0YZtYPzn_FLCeZZxnaoaycGNi08MRCIVJCNV3eG15XTX3svAqi7FtXv20jBHN_9C_OC5m_4ISBNrkzFm-VFKNxC4hJstoP1rBEzqFvsSJ_ZPM-qkwCC_RgysV9tJPod1YyKTFiVIHP_9OTd7N3fqEolqXiHGlE4BfTMpbXbSCp0pOecZHCVoy0SnCYu-YkOkwjlSs-L_U_jwCoX71rTTNiaUClcEcKITSUP3ThUFdIJ2D03avA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hnLjz5icCsrrryn1aNMioGFwcEeqO9mJgxAJm0SR4rRR7CiSTz_rKRB1KsGs-qKP3jFLgfb9XykrB4-HcRRXtaCoGbqjP8mGIeL4gUBjEmEyNhl6uhmrKEjBzwKFSkjpHZ46LZJJng-lBphdez7tbDoA4f9an7H-gT8f9eX0oQYpEusHcjW7P5vbcLDDR9FEJqkgach9hBiuIY6X9_ePWM_voNGjKDb_oqd7AHLrJP1YREiLvXD0_UXphEXp3m6qnFCSXpd8f_Buz5sMMywqFyKeKAqEARkanKGLEmgaleqfY3lCzTl6SI76UJ0zhIpYNyUQMSpAcktO-6P-XTA9bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌ تلهٔ حزب‌الله ۲ نظامی صهیونیست را به هلاکت رساند و ۷ نفر را مجروح کرد
🔹
رسانه‌های صهیونیستی گزارش کردند که در پی انفجار یک ساختمان تله‌گذاری‌شده در شهر مجدل‌زون در جنوب لبنان، ۲ نظامی اسرائیلی کشته و ۷ نفر دیگر زخمی شدند.
🔹
براساس این گزارش، نیروهای ارتش…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/farsna/454700" target="_blank">📅 10:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454699">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFYKjUueQ8M4BIsyi0rftHfdBhtPaBDGnwqeFlXgiq10W-FzrAT4oMejGelARGFdBxzLqQIIgMDEIQQWXeowTwk3WK1OizXLoUzwLEexrWtaJHdv2rT2ufJz5Qd0w0xWhGHExkluvIXpQ-Hmp1CZU-D-3bWGhzfxUGaom4APCc2ma-fz5nFTAsF4oM9oEmW6CLtYrIhNfucfvLhISLgsrnCMOx7jygd9kDF76tqEFqG0a8zovpNKfnL2HQzCMcl5P1io3yXAcwQ9ACkYFYpyRxp7OAwu65ZCk_9Cz042-WIUPzs6J19nYj__-ei59OC1tlP3wTQBu78f7WBfHquFPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آقا هر وقت دختر موطلایی می‌دید دست‌وپایش می‌لرزید
🔹
اسدالله علم، وزیر دربار می‌نویسد: «در سرخس خانمی را که نسبتاً خوشگل هم بود و از مشهد آمده بود به شاهنشاه معرفی کردند که ایشان نمایندۀ سرخس در انجمن هستند…» محمدرضا پهلوی از لفظی استفاده کرد که صراحتاً از نگاه سخیف و ابزاری او پرده برداشت.
🔹
علاوه‌بر این محمدرضا در مصاحبۀ رسمی‌اش با اوریانا فالاچی، خبرنگار ایتالیایی، در سال ۱۳۵۲، بدون ذره‌ای ابهام اندیشۀ واقعی خود را روی دایره ریخت و گفت: «در زندگی یک فرد، زن به حساب نمی‌آید مگر وقتی که زیبا و دلربا باشد…» این منطق، حقیقت ساختاری رژیمی بود که زن را تهی از عقلانیت، مسئولیت و نقش‌آفرینی تمدنی می‌خواست.
🔹
اردشیر زاهدی، داماد شاه و سفیر وقت ایران در آمریکا نیز در خاطراتش می‌نویسد: اعلی‌حضرت به‌نحوی افراطی و غیرقابل باور به زنان و دختران موطلایی علاقه‌مند بودند و هر وقت دختری موطلایی می‌دیدند به وضوح دست‌وپایشان می‌لرزید!
🔹
خروجی این رفتار، افشاگری‌های متعددی بود که حتی همسران شاه را به ستوه آورد؛ آن‌چنان‌که ماروین زونیس در کتاب «شکست شاهانه» می‌نویسد ملکه فوزیه و ملکه ثریا بارها شاه را تهدید کردند که اگر به زن‌بارگی خود در محافل خصوصی ادامه دهد، از او جدا خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/454699" target="_blank">📅 10:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454698">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ec7f26e41.mp4?token=up8uHhns8OxnkxqoZqmD4lD-802bUVs0RnNK-kWXy21kqf8RO-gfCM8xrwMQyGag70qv7uTPFLC3N5HWoGs_RpqUIMRJWfr2JhO2MDxS0-V7u5Ecbb6p6IUroMouaz7fNyZKgxRGRMfyIKCzK14Llp43HdpJchpah9fwOyvVlXYacvqqjmCi_k9QeEewl2MzgpNooTGLBNBECUHU5YH35xHLEflgOKEqP5EATNYrYE8IlrhMDd_umwQzFh8sOCj1LlTujAON23AiWMh7Rzx8_X_8uQfHcnMuUgKpTKz5EvXXq2pZ-1aniEXVVdLmRC0W951vWq98EV999pe_CouHGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ec7f26e41.mp4?token=up8uHhns8OxnkxqoZqmD4lD-802bUVs0RnNK-kWXy21kqf8RO-gfCM8xrwMQyGag70qv7uTPFLC3N5HWoGs_RpqUIMRJWfr2JhO2MDxS0-V7u5Ecbb6p6IUroMouaz7fNyZKgxRGRMfyIKCzK14Llp43HdpJchpah9fwOyvVlXYacvqqjmCi_k9QeEewl2MzgpNooTGLBNBECUHU5YH35xHLEflgOKEqP5EATNYrYE8IlrhMDd_umwQzFh8sOCj1LlTujAON23AiWMh7Rzx8_X_8uQfHcnMuUgKpTKz5EvXXq2pZ-1aniEXVVdLmRC0W951vWq98EV999pe_CouHGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشهدالرضا منتظر میزبانی از دل‌های بی‌قرار است.
@Farsna</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/454698" target="_blank">📅 09:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454697">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NM3d0m9SZj9Q-V3sEx9geLi4c29hEmtCVe68yymLijdzbvsGH2gqiiwAAEtcLKdlqI1ckoWS8tuAo6Bv5Vr81s6Jm2KtLscg7HYcSLQxUNc0zxrGVHq5YmJCGIjN9sdqkbgj0s2cWdVdsqkHMKSDwy1CJj1E678ErxFjErVNl98KQwVKhxj3D58Mseh_JcYHr1wm2-WM2aOcKxsxJ6n6K-d0Zk_YrX9NOjtQFqV5Uhil3n3Hr0c0rEvuEcOcSEw79wU4JEDXlw6dVWtEL6yYJOR_4Ts9J_cBlLa9nmHPYwiJW5-CzUqD2vtIqnRf-MyVgnhsyBb7d_usZKXZ9epJSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار ارز به کدام سو می‌رود؟
🔹
بازار ارز در هفته‌های گذشته بیش از آنکه تحت تأثیر عرضه و تقاضای واقعی باشد، از فضای روانی و انتظارات معامله‌گران تأثیر پذیرفت.
🔹
افزایش تنش‌های سیاسی، رشد انتظارات تورمی و تقویت تقاضای احتیاطی، دلار را وارد کانال ۱۹۰ هزار تومانی کرد.
🔹
اما اکنون شرایط تا حدی تغییر کرده. کاهش نگرانی‌های کوتاه‌مدت، افت حجم معاملات و عقب‌نشینی خریداران هیجانی موجب شده بازار وارد فاز استراحت شود. این موضوع باعث شده دامنۀ نوسانات نیز نسبت به هفته‌های قبل کاهش یابد.
🔹
البته کارشناسان تأکید می‌کنند آرام شدن بازار الزاماً به معنای تغییر روند نیست، بلکه می‌تواند نشانه‌ای از انتظار معامله‌گران برای دریافت سیگنال‌های جدید باشد.
🖼
اما کارشناسان تکنیکال چه می‌گوید؟
🔗
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/454697" target="_blank">📅 09:49 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454696">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">انهدام مهمات عمل‌نکرده در پاکدشت
🔹
روابط‌عمومی سپاه سیدالشهدا تهران: انهدام مهمات عمل‌نکردۀ تجاوز آمریکایی‌صهیونی در شهرستان پاکدشت از ساعت ۹ الی ۱۲ صورت می‌گیرد و جای نگرانی نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/454696" target="_blank">📅 09:35 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454695">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
دستگیری ۸ تروریست که مهندسین حوزۀ زیرساخت را گروگان‌ می‌گرفتند
🔹
روابط‌عمومی قرارگاه قدس نیروی زمینی سپاه: ۸ نفر از اشرار و مرتبطین گروهک‌های تروریستی منطقه که با تشکیل تیم‌های مسلح اقدام به ایجاد ناامنی و اجرای اقدامات مختلف ضدامنیتی، گروگان‌گیری نیروها و مهندسین فعال در حوزۀ زیر ساخت‌های سیستان‌وبلوچستان، حمله به گشت‌ها و مقرهای نظامی و انتظامی، سرقت‌های مسلحانه و ایجاد رعب و وحشت در مناطق مرکزی استان می‌نمودند، دستگیر شدند.
🔹
از این اشرار مقادیری مهمات و تعدادی سلاح کشف گردید. اهداف این اشرار شناسایی مقرها و اماکن نظامی و انتظامی و همچنین شرکت‌ها و نیروهای فعال در حوزه توسعه و آبادانی استان بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/454695" target="_blank">📅 09:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454694">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/759e96e986.mp4?token=knoB1WeLObCnzxFAAqv1SIJFIvSONaiircY8kpCpWlDRD8zIdxIXCCurut7qVM_w68zcOpycwdpCyvdpH2wpS96U2QQXWQBoobcVj11gtzbFiQ4yDXdn5J0jt4PJtmmkP6cM_yIohBtOKd4GawsgFfcQhhIXVFKHVqeQsfkV8DHotvh0S8lkWKp0RlvcC3gaRXEAPyA991KmsrN5vUCKS56Jd8oIiJ_1BtEZTXU74Az-U-AfpNFvDxEmJLDAGSbpy2XXNiJFzffQJSUFig4f0ICLg6gD2b2IZG85zHKFcE1TvPGh9hTFbSPIgg1L3MOZI7AReMUd3BZLI190DVIcUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/759e96e986.mp4?token=knoB1WeLObCnzxFAAqv1SIJFIvSONaiircY8kpCpWlDRD8zIdxIXCCurut7qVM_w68zcOpycwdpCyvdpH2wpS96U2QQXWQBoobcVj11gtzbFiQ4yDXdn5J0jt4PJtmmkP6cM_yIohBtOKd4GawsgFfcQhhIXVFKHVqeQsfkV8DHotvh0S8lkWKp0RlvcC3gaRXEAPyA991KmsrN5vUCKS56Jd8oIiJ_1BtEZTXU74Az-U-AfpNFvDxEmJLDAGSbpy2XXNiJFzffQJSUFig4f0ICLg6gD2b2IZG85zHKFcE1TvPGh9hTFbSPIgg1L3MOZI7AReMUd3BZLI190DVIcUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کمدی ترامپ در لاس‌وگاس: کودکی که طعمۀ سیاسی شد!
🔹
دونالد ترامپ این هفته در لاس‌وگاس یک نمایش انتخاباتی دیگر به راه انداخت؛ این‌بار با یک بازیگر خردسال که هنوز درست حرف زدن بلد نیست.
🔹
او هنگامی که کودک ظاهراً قصد خروج از صحنه را داشت، به‌سرعت دستش را دراز کرد و مانع شد و بعد با کنایه‌ای به رئیس‌جمهور سابق، گفت «نمی‌خواهم مثل بایدن از روی سن بیفتد» که با خنده و تشویق حامیانش همراه شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/454694" target="_blank">📅 09:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454693">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/116eee5985.mp4?token=NeP40nwa3TMmCVv53SVkql0BfmZ0e-tNe1KyA3Bg86LFp9900mCtMMwsBZzZ5rmL8y6gpr2X-H4RIDnXyQojxiwHgcmNuKEPvczu6Ivp4-6qaFD-bbkmrTo70HmqLs_1TN1P-83QRPvBzN2-ZoR0sL58B2jz7PQMzhvrDje-jGhyEQwe0I_7pdSe9dybQzoJHOFQsUZsEtZhN8AqT_i49ZGJaqAbrX3D5cY6pisbMShEhupaw3zTliNsD4Y2FD0nhzleDxEkZK4_QrNjyK7hpH6Jqrfzjs5P6jFRUjJI2D0LIOA1huF76AOtB_cAo667Kc_BGkPzOhYHfeRoUXwHnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/116eee5985.mp4?token=NeP40nwa3TMmCVv53SVkql0BfmZ0e-tNe1KyA3Bg86LFp9900mCtMMwsBZzZ5rmL8y6gpr2X-H4RIDnXyQojxiwHgcmNuKEPvczu6Ivp4-6qaFD-bbkmrTo70HmqLs_1TN1P-83QRPvBzN2-ZoR0sL58B2jz7PQMzhvrDje-jGhyEQwe0I_7pdSe9dybQzoJHOFQsUZsEtZhN8AqT_i49ZGJaqAbrX3D5cY6pisbMShEhupaw3zTliNsD4Y2FD0nhzleDxEkZK4_QrNjyK7hpH6Jqrfzjs5P6jFRUjJI2D0LIOA1huF76AOtB_cAo667Kc_BGkPzOhYHfeRoUXwHnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکم ۱۷ سال حبس برای عمران‌خان
🔹
الجزیره: عمران‌خان، نخست‌وزیر سابق پاکستان، به همراه همسرش پس از آن که دادگاهی در پاکستان آن‌ها را به نگهداری غیرقانونی و فروش هدایای دولتی ارزشمند متهم کرد، به ۱۷ سال زندان محکوم شدند. @Farsna - Link</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/454693" target="_blank">📅 09:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454692">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwCP0h1CwTYuCetLJ9TeiWANF873eoQHYpwWydByKkVp6FzPtO7Ki_YGxMnU1M4Qexz_w2ddlc35Yx8RRCiBWD3ADAWbGkn_EXmcNrT-g8F2jm47yRv-AYIHsF_8jvXmr4-0uNO6atX19V-YN8OOmjpMsMTfB6yj2SlGMjPVqWE6KQe1M0pXqQkkitkW1QVQdUYBWS_inaVSbcTvOuS90zB-UzxBcb05AVm0UTpD3o4qHpoCtUsiSHvpuT7FHj9Se7EVaIotDI_Z3-rvPFIvTO3MUyanpzfDNg3af_nP8j3udABKcc72B8f4QSDMhtfxifzhdntmxlMWbof7q5F3PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پهپاد بمب‌گذاری‌شده در قلب فرودگاه آلمان
🔹
مقام‌های آلمانی اعلام کردند یک پهپاد حامل مواد منفجره در فرودگاه لایپزیگ/هاله آلمان کشف و خنثی شد و آن را نمایانگر «سطح جدیدی از تهدید» توصیف کردند.
🔹
وزیر کشور ایالت زاکسن گفته مقامات در جست‌وجوی قطعات یک پهپاد احتمالی دوم هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/farsna/454692" target="_blank">📅 08:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454691">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a38ed22c5.mp4?token=i20XVJWGE-nKa1iiEnrqoxYt-OEkEzWlQKXHMS_1pEO0ZpvRpbLKvm6HiL6inID2s2apZFdJ0AhS8XOPuGNbhvX0ZEg-ZTr_QfKuwdZTE8kalkXi0-YBbHVGCY9eGgC6PnuYUaRS8UuJbAmQ3V_wzG_mioJdlDDI_itIXkWwzdU07ic85VC2TCdslinr8SDX4fBimlL1xvRjHfqyHJ6iDJ0PXZSrYoxpk2--BWSXam1-ednNNCfJfIl1lHqQZouMkYYN3GE1qU7HNGRvjNUEnkR-5ASKwutWsF3oi1UeAnIT1K4RHnu4BZs2v3wgKpPPprpGSG9Oh9SssKLpau98Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a38ed22c5.mp4?token=i20XVJWGE-nKa1iiEnrqoxYt-OEkEzWlQKXHMS_1pEO0ZpvRpbLKvm6HiL6inID2s2apZFdJ0AhS8XOPuGNbhvX0ZEg-ZTr_QfKuwdZTE8kalkXi0-YBbHVGCY9eGgC6PnuYUaRS8UuJbAmQ3V_wzG_mioJdlDDI_itIXkWwzdU07ic85VC2TCdslinr8SDX4fBimlL1xvRjHfqyHJ6iDJ0PXZSrYoxpk2--BWSXam1-ednNNCfJfIl1lHqQZouMkYYN3GE1qU7HNGRvjNUEnkR-5ASKwutWsF3oi1UeAnIT1K4RHnu4BZs2v3wgKpPPprpGSG9Oh9SssKLpau98Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: به نظر نمی‌رسد تهران دیگر رنگ دمای ۴۰ درجه را به خودش ببیند.
@Farsna</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/454691" target="_blank">📅 08:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454690">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bc792275.mp4?token=cMNg6ShKJQfi6uJX5Ud31TXUbcbW6lGSlctIkhB6ESRRHYKw4tNzyiwQaOk8917Fj5cCwEMvgYvXVOkJ1-cdNEzAtMQQDufrwGwHeo8lOxTu8HGg5zyEB4h819OK-1zF04A4_8wi7a5i2L_R1ZYBFsDa7s9tlUwYqp-ALRXiXP4Y1BHOqdKiag2EuuhvSqN27CA6Z440rmDL7-5sHJV4_bqoR2dVeTap_sdRBOAEPRlcT6K1dsaOB0dhLGcG5eo8tfFzj73rSCpPVyJ3rik1IFEPykEs0Lq9JEaQ1WlfMbhu_iCTnMAwO2RZVlqWV5RsPsr7wL1rwXhzKPlhmofnRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bc792275.mp4?token=cMNg6ShKJQfi6uJX5Ud31TXUbcbW6lGSlctIkhB6ESRRHYKw4tNzyiwQaOk8917Fj5cCwEMvgYvXVOkJ1-cdNEzAtMQQDufrwGwHeo8lOxTu8HGg5zyEB4h819OK-1zF04A4_8wi7a5i2L_R1ZYBFsDa7s9tlUwYqp-ALRXiXP4Y1BHOqdKiag2EuuhvSqN27CA6Z440rmDL7-5sHJV4_bqoR2dVeTap_sdRBOAEPRlcT6K1dsaOB0dhLGcG5eo8tfFzj73rSCpPVyJ3rik1IFEPykEs0Lq9JEaQ1WlfMbhu_iCTnMAwO2RZVlqWV5RsPsr7wL1rwXhzKPlhmofnRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عطر برنج تازه در شالیزارهای شمال پیچید
🔹
شالیکار گلستانی: امسال خوشحال‌تر از سال‌های گذشته هستم، چون به‌عنوان یک سرباز در جبهۀ جنگ، امنیت غذایی مردم را تامین می‌کنم.
@Farsna</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/454690" target="_blank">📅 08:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454689">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34a86cac7b.mp4?token=VWpMR9b40igNA4lvpN_kN-Unty9FDBIII5p-xi6VgMTSFdqqev0kgwxDWjGSZ3CIrfYNxGgBtQ4vlDKHLKxwfafguBjeMpoD2ONsmty538qnzCCu2s4rh9XfbYW6zqh_byc5ey4vixJH2ZzYCWYbHXZPA1ORbvhB5GgcGh9Ydw7AUMKB1w7LzqA8t9_bTSBRBVvz6V5R58DzeC4a6LAdU7fVQPAQad70afOVukqufLpWfyd5OpNE6o6tuCtkLDvrF1i2nyKHQJkL8D9sAOstwBuQT5d8v2YuCDqr38t_dXYtJwNXF4bXFFTAoBm0qWgV38-4vixhZ_9Ol6PhQALmpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34a86cac7b.mp4?token=VWpMR9b40igNA4lvpN_kN-Unty9FDBIII5p-xi6VgMTSFdqqev0kgwxDWjGSZ3CIrfYNxGgBtQ4vlDKHLKxwfafguBjeMpoD2ONsmty538qnzCCu2s4rh9XfbYW6zqh_byc5ey4vixJH2ZzYCWYbHXZPA1ORbvhB5GgcGh9Ydw7AUMKB1w7LzqA8t9_bTSBRBVvz6V5R58DzeC4a6LAdU7fVQPAQad70afOVukqufLpWfyd5OpNE6o6tuCtkLDvrF1i2nyKHQJkL8D9sAOstwBuQT5d8v2YuCDqr38t_dXYtJwNXF4bXFFTAoBm0qWgV38-4vixhZ_9Ol6PhQALmpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ونس: ایرانی‌ها مذاکره‌کنندگان سرسختی هستند
🔹
معاون رئیس‌جمهور آمریکا در مصاحبه با شبکۀ «فاکس‌نیوز» مدعی شد که از تمام ابزارها شامل نظامی، اقتصادی و دیپلماتیک برای رسیدن به راهکاری برای ایران استفاده می‌کنند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/454689" target="_blank">📅 08:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454688">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دریای مازندران فعلا مواج و تعطیل است
🔹
هواشناسی استان مازندران با پیش‌بینی وزش‌باد و مواج شدن دریا، تمامی فعالیت‌های تفریحی، صیادی و قایقرانی را تا اواخر وقت جمعه ۱۶ مردادماه ممنوع اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/454688" target="_blank">📅 07:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454687">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSzR45UDdl3fumD0hMUt1s5YhBx-zzq4zyMF7-WoZsIW-yoVo-pzXpgoaXrstoTwFUQuKqbthRtsn90ZWPZSX2ZYkpIVbEH7DyYQejMZnJhA3K839tMJ-E0W8htkw0bNpf-DMZ4N7xDJ6ltp1wXYIuNhO-BjexMVl2XynkFRtJfiQIMbKIXNhs6iMa9DOLRsSi9Eq1sN1LTFJ0hMz5s1IKNz28a1uztQ-gRmscHRhTKibvBT-E52FIfcNMVRPm_3IutKX_D8mD-jFUd7A7NnXn1P-pB6O1wpXVF1nCk8NTsasQQI8Htb1DXKDVVCbwOe2R0zN_IolCH2aznJFVuwAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ زمان شارژ اعتبار کالابرگ تغییر کرد
🔹
معاون رفاه وزارت کار: از این پس اعتبار کالابرگ در روزهای ۱۵، ۲۵ و پنجم ماه بعد به حساب سرپرستان خانوار واریز می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/454687" target="_blank">📅 06:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454686">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">آمادگی خراسان‌رضوی برای میزبانی روزانه تا ۲ میلیون زائر
🔹
مدیرکل هماهنگی امور رفاهی زائران استانداری خراسان رضوی: یک میلیون و ۲۰۰ هزار ظرفیت اسکان برای اقامت زائران پیش‌بینی شده و امکان افزایش تا ۲ میلیون ظرفیت اقامت روزانه وجود دارد.
🔹
ناوگان حمل‌ونقل جاده‌ای با بیش از ۱۸۰۰ دستگاه اتوبوس تقویت شده و پروازهای روزانه تا ظرفیت ۲۸۰ پرواز افزایش یافته است. حمل‌ونقل ریلی به مجموع ۱۳۶ رام رسیده و امکان جابه‌جایی مسافر تا ۶۴ هزار نفر در روز فراهم  است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/454686" target="_blank">📅 04:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454685">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4xHawK2Yv4rckR4voWb5XBuidcW9ZK04zAeuKGSFlEypsOIj1qpsR1-hgCZ5qU9M3h7eUhhtNCMxQZo-UnQj3DgUoANGeMUjHV8DnrQConE6bd1oyfRNkgLhlCvGMezl6BzlZA6nj0wMPbm18g3T9LhIVA-BSGGiKIh-p_o2dN5EtmnbXC6QXtQC8k2XZdiGUlMJlv1IPcejYbbgb71w5nLu9zbXMwIkIA_Td6mBAAwPM8tEA682VbeMONTryMy5aXS-sDeis1RJYcJFrims80O_bxrAKlovQhS1nw21REDItof9UeXEAKjgjip7Y5QBx9Z8ZaFXpmxGo_A3ntrgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حادثۀ دریایی در تنگۀ هرمز
🔹
سازمان عملیات دریایی انگلیس از دریافت گزارش‌هایی دربارۀ حادثۀ امنیتی برای یک نفتکش در نزدیکی سواحل عمان خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/454685" target="_blank">📅 04:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454684">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7Eh2eKfXHhjqoE-apXhVbBIoCLZJvTpztae9v8NyND9anxoendYSePPVnernh3bMVmUyOCcxjomT-QGAaRkGDpsDiTCp1E-aQU3Mo4cSpmYqzwFS9KdSvbodQVGMokQyNrpSXDiCtmekDRcYc7NwoV44pDNr95MKwewPRoEka7KsoIi6ma49PysuvvU_njekXFMmnt1HfaxYGkycMySXPAXEmFGGj6AcIuvilRQfiuWsaa-hTqj-RtL-Bxi5J5VdsfZCefL2XuJPTsa7J-qIp_olYj1Ly2T4dYIA3Pe7aSQColUMvkFTaCOIGgJEuCr4em3MjQ_MVYhHtKI8IFj1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا برخی اتوبوس‌های تهران کولر ندارند؟
🔹
«اتوبوس بدون کولر در گرمای تهران زجرآور است و اگر کولر اتوبوس‌ها خراب باشد باید به شرکت واحد اخطار داده شود تا نسبت به تعمیر آن اقدام کند» این را مهدی چمران رئیس شورای شهر تهران می‌گوید.
🔹
طبق اعلام شرکت واحد اتوبوسرانی، تمامی اتوبوس‌های ملکی این شرکت مجهز به سیستم سرمایشی هستند و رانندگان موظف‌اند در زمان فعالیت، کولر را روشن کنند.
🔹
همچنین در صورت بروز هرگونه نقص فنی در سیستم تهویۀ مطبوع، اتوبوس برای انجام تعمیرات تخصصی از چرخۀ خدمت خارج می‌شود تا پس از رفع نقص، در کوتاه‌ترین زمان ممکن به خطوط بازگردد.
🔸
با این حال، مسئلۀ سرمایش در تمام ناوگان اتوبوسرانی یکسان نیست و بخشی از اتوبوس‌های تک‌کابین واگذارشده به بخش خصوصی اساساً فاقد سیستم سرمایشی هستند.
🔸
بر این اساس، در کنار تعمیر سیستم‌های سرمایشی موجود، باید وضعیت اتوبوس‌های فرسوده فاقد کولر نیز تعیین تکلیف، و نوسازی این بخش از ناوگان با جدیت بیشتری دنبال شود تا در فصل گرما، کیفیت خدمات حمل‌ونقل عمومی تحت تأثیر فرسودگی ناوگان قرار نگیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/454684" target="_blank">📅 03:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454683">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91518e29da.mp4?token=LBY68m3kJd9OQDjqu4Gd9Pxm4Wz-Y1Bff0BXN5AZLfCu6H6OuA-pB5K-byxxBlYJ4oyfqT1LqyBtQ2shRzDA5M75NytICVWHR0KoowLLawPAeq-YdeQ5a88mnPcss5FH8fdp3Kq_1lInSbB5GavYxWdStv239_kgiEk-PLnGOvJyrGYxkjdjzDfU1-OQf0KbETUi90OQSiHa5LFYmr6MgggUzRCvTREQRi8Ki0C7t5zPotqXC_KgY77vldK9T8FltE9c9Ck_7o9wJYXz5IUXqWrrSY3vKIwNarQhVkMUXyyvQ5Gy46zsUajp8G5Kmp-3-dbIAqCHX48_MO1wlwEu_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91518e29da.mp4?token=LBY68m3kJd9OQDjqu4Gd9Pxm4Wz-Y1Bff0BXN5AZLfCu6H6OuA-pB5K-byxxBlYJ4oyfqT1LqyBtQ2shRzDA5M75NytICVWHR0KoowLLawPAeq-YdeQ5a88mnPcss5FH8fdp3Kq_1lInSbB5GavYxWdStv239_kgiEk-PLnGOvJyrGYxkjdjzDfU1-OQf0KbETUi90OQSiHa5LFYmr6MgggUzRCvTREQRi8Ki0C7t5zPotqXC_KgY77vldK9T8FltE9c9Ck_7o9wJYXz5IUXqWrrSY3vKIwNarQhVkMUXyyvQ5Gy46zsUajp8G5Kmp-3-dbIAqCHX48_MO1wlwEu_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات رژیم صهیونیستی به جنوب لبنان
🔹
شبکۀ المیادین گزارش داد که چند منطقه در جنوب لبنان هدف حملات نظامیان صهیونیست قرار گرفته و این حملات همچنان ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/454683" target="_blank">📅 02:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454682">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHF4YAsHxA4-7BerpQQLYQr-uu66Eu_wr-Xp1UYY2KUYIyG1UW9cr1xqmQ6IiJcptPBMJEW9LwQTZvHMrWaOHFzPjpqu3PpUQ3KJockMQ9jpbbdadH6Lf03vbvQwus6_w8gQQOqO4JuE4yeCfb2F5bCmTMztVBFwm8TmI8zKE4SYocnyMpnPSmE6n4Jynprnq-HXUMOtuHoEIdNFYD1prn9hQcoFBmtHmw0x6wiBvz7fcCLun3EPfecho45nwkI5qO8QYZS601zs8M__pMOjUO_vAh7qi8H6Htyt6PUGth--JOstDeYHefXVOR9SpOL1cauEt_IFb-j7PN5DUZeYZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مربی خارجی از پرسپولیس دور شد
🔹
پیگیری‌های فارس از مسئولان باشگاه پرسپولیس نشان می‌دهد که احتمال منتفی شدن جذب مربی خارجی بیش از هر زمان دیگری مطرح است؛ و در صورت رخ ندادن اتفاقی غیرمنتظره، کادرفنی پرسپولیس در ادامۀ فصل با همین نفرات فعلی به فعالیت خود ادامه خواهد داد.
🔹
به این ترتیب، به نظر می‌رسد درخواست ابتدایی تارتار برای اضافه شدن یک مربی خارجی به کادرفنی، حداقل در مقطع فعلی، عملی نخواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/454682" target="_blank">📅 01:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454681">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یورش شهرک‌نشینان صهیونیست به فلسطینی‌ها در کرانۀ باختری
🔹
منابع محلی از یورش وحشیانۀ شهرک‌نشینان صهیونیست به روستاهای فلسطینیان در کرانۀ باختری خبر دادند. در این حملات حداقل ۸ نفر زخمی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/454681" target="_blank">📅 01:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454680">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">رویترز: ایران به کشورهای عربی هشدار داد
🔹
خبرگزاری انگلیسی به نقل از منابع بی‌نام ادعا کرد که ایران به کشورهای حاشیۀ خلیج‌فارس هشدار داده، حملات احتمالی آمریکا را با حمله به زیرساخت‌های انرژی آن‌ها تلافی خواهد کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454680" target="_blank">📅 01:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454677">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uyF93s09EM0F7UGKlOe9BNcUtYpwCtCs0hjM9UKeolRcQKqbUiVi7QNyomRWN8n8IM_yJ_hZS9hFNsa_Gk-4_Y_S1pQvPKa6t9tBZw1j-mzUjxsEAT90kuFyU6Np02qER0wAnxfN9JQXbP8UkWuHfzJjFqFytgpAMc-pZhTMAfofUKrELpQMqoMO9LaAx_mAJklwvqawdSq5CI7KzFTRiGAjY1_iWOpHucNVQDK5XZr1pahT5fddTzxhEe_YVukneRPrbhOOOehLAcAAYCQ8qfT-3ssjV5FehVU65i-uoG0lpH9Sqtj7gFG3jcgRo9m9e0FyvPc_Q_bG_GFffQKWRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JXbll2jkcbCk73XHvSv9a45QhSaNhBdT5CndaeDhWGNdWm49xdnsyhNS2XPaP2ogXEBAC5tro98oUMeeTW67MDJ-csTWag1vdZfYu0BYIdLym5_SqwiDORAV94Vd5sydsmXVtrTxVgokA6EisIM9epPj0nxw1VvWud-4QuhWz4ZgBlJpsv29w1y6GmEm6BnxkwKiIjDkMRtOJTRSubf7JbiE4w6Gn5mRGRiWBF-ZfoeaLXPZYc2VkDRWSfz29seem0kN_KAPYzumvo5y7b53I9PA1K3qNC-bqjPuHld7oF08tSKtk9ay9mI-npv9zDQwNMyRux0tp7WmQnI-muphGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sJD7r8-tCN0_ahmPWVMO02EBnGE5mfYBdWK_Oy85hHPmRlvM-ec9xqCuXM3qhheadDya4CHuuoZGPegspNI4BczualZ310ekupABsRPD0JPkcoOtpkIzi3bwRcuLLoCh0bqxlTWfQcGjffj10_02NkZyvs1zWrVEb-qKvfzgxQSxaoRH0tTsG_n_ketdcK4cMOjh-xJ8led6ZomjB885xU_sQ5ZnV0JD0ANJPZ_qltZgzbHmbUsGVCrUXbk2A_P1C7ulEQnTmywDA_w0vcvmJgvCxoWYVRf42ct1R_b7sXNltUbu5pR5nHtnaE7vbEdLFoiCBQk-b3xa9y9pfN184w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۱۵ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454677" target="_blank">📅 01:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454667">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1areJrTpwE6is7MbrKoLXua43zCZiN1Bu1_gbznOfsPLmy1CPoIxY91NuFzkgtniJ7u7qfg61v71GkzQZgl70WE_hMSQ-gC2Yr2HX52DIzs1vigDJAUTir6DpOMhx8xlYBy9vmyrn5kUTmMtlULYaSrTz5t-v6h-j7ol693llX4dzYxd8D1O5hgFhUUCjeksXmu1FIPNoSk-6iD-d2PfXpvAgcfOcGiEIucImNzJLVRGahFnh4Q1UCuVBS3bBtzguo_cHkBFSTq5HGWJEA8GLfQT8HAdN4V0CEcTqMDvEARuzwe3Za7x_kJBgnjJmU5brTQcTIrM8a4eYtUzvKSkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VxTDIyFDQ2NNIKkUJx_jMCPugoxw-NLSxzR45T9yp7DHW_p5Ifq2-dLXNYm1E-b669XB-632YY5yDY0ZtTzpuDwfXKVVbSthwOOu8XVglqtiZ4Tp89ZYBQemtN-6AOVUBTvX8Ig06CATqDprPAdTwUA33dDUJyGlBKhqOkO3TW2Ngl5kNs3UFjznwRxALphXyV1cJvzfCz2pGTbbouI08XW66cbiKWcyIyZSDNCQ8Lelapyi5MIbYliPTWkeRK8pLrh16LXXAfSolZTAIe9sxCkUALCrANQFrnH8rA5DHFoWVhKyWdUltcaWD06UTgbos2LbUD2FPoOhAPZrT5mUTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ck2qBhgJbHH2oi0b4IBDVc0iKoCOaOZsnsdCZFM9OSJoe0BwOjAWWNCSlx60tt6vg9E70ZFClOCadnhjStaUH1tPpohyM2448xFmlUBHRLnwapgqodQ6gRk7wApiufVhcoMlDc9zMIVwwlTpRASAnLvXGNg5cfyRkrKMFoUMeqNWKw9RPaQDwB_T-V7Ze0tFzzQ0JEWXpgJQNT8_hOX8Y_NaKhAPno5xfNdYSetQfZlpzD1m4tahDVOuzQD0mlOpOIPZtPY5GqRYRkcmeyLFPTNOg5a955w_7Ks7sm4-FrEIdr0qel9kXkesE9f878vlviYVzss8V2HKeAc_BTWuQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t2ztaWL3wt_4WOeezLPVRgxSUfjvEDGgnmsUTcewdyrb_Nx_48NQqUFt-GUVoHHDM6vubzSMTIrCKC4DIeljvutNofzymrylezJiYPTYuLp1weSw8nY9LRE7RqBdfJR_tIr_j4eQZbPvzJPZt3dYyM-R-8oDQOMwwBVF6AsnohjT0-A6KtGX_LCLVzdYHiIDaeuQs924wLqEKo0njs2nYG5aSvA1X_VsjWD23abeawY2z3M2ta7VEYHFXNKsYY528Vkz29nnhm400THowulFnnHSGa7_DK1QYDJrTSjQMZAMxRxU1Mb52qPNPko4Fntcqsw5UNRzfOFNUGK2X4z0mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Al3rN4Ds-HTwDxnLQ6U6WPfkMUsQ3x9XhXOlvmJkZumt-t4Ol8gq-sVGOuWZIVwjudUiVQ5Q2uLWsya_pImI_WaPFFNtk9TKlQhRdwoHeYAMhxGoMXVGc31UCpqOSemPElUcJ6pVP5KrJVO5m3YSvb-_vUELpwJSufoZfcamTcpESomqvFmVG4yRvfczyDwXh1d9JJDGVGH8xOjuR5h8p5lSR40YSdVlfNix1TUjXVPuBXdTdSexZmK9cVnBWrg0mlBXtY_8BihBt9BSb5gQT4hh6onFJYuM9gJ35OyEOSVq6IS4mwsAnu-TGzGgPwTRvs460FgWTuEa8jWuWQ38Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2nVUdS6mnBsDCdV9Pr5AYzj72mhsaPHgJBPyEsyScdvMkOz3mPI4h1YJtmjgV1GN0KscSEIpj1P3moGhH3kClP1wJUOGXlBWtJslF3-plCEV8bDG3Gf29HJ-ouHBBG9-X-CkIJlnglm17V4U-e697tYGXFLWD7oCHSi8aAsDDxk2PbZYa9q5I2T9i5EBcCaoKPI0KU7R4H1HcsD3H_ZhBSIOlZT3ImYaHPhuNkeH42UdKB8LMcBT37_VMyFMfQ8m9UyUBtRxM1e7hux_vm592vb94N0VedmFwqy6Cj1yHdbZsHgnFrSmnDcrz4IWOJuMkCwaCTxIiOi_QWtY2Q37Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ReaHoHmYCtiwFA0h6jTvXLq0t9k9dhQASmVfPwFH-qtYaa-4SpRsIlkku6inStBxbvw6aAbATtoiQSavEjMj5lGWyGDLpYuzsZW1_cRk9jIsXcMgMgdOSfmqLSzicofS4xvg93zoPwLQ-thEufHOOwvo3m60NR9-Rg_SwM5HNzaL-HwR2iW3qYL4roDoN_QEukg7ZIgivdby9NU-PRCDCY4A6TXLqSk68ZHpSbrX9OsQZSb-xyiHHRkRjBHaUeJ2Mv5iTumpSTfM1RuD5WYCl1Gf7tqKSl1rM-LyXgJLnT5EFAwT9Wp8I7kZ4Xa_9xBR6FO7ipu5IRq7IOQg-oElQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CyV5q1ay3b0lh9kUtH9gs4H8-ygCBvrxTGL3C7VeOo3W81fXPy1QRuvTT9JFiTDmCXS_3mGC6aAGT6jknByeNy8DBNCxoCQRrSSkxXLWSNxiY4Te6FVb94yvIAKvzUVKlZ79IbHTvXZfGWpOxYdXMoOQH0-hml_kXdfLVyI6nS71o2NKxY0v6MC-r0O1nSy1iCKddGvlpluKtzDJxBtQHgsXO0eIVWpVs1TWlFtLb9cfYGvSbCIXC7wsj3VT3iD2NVp53VNRNukHH4QChF6cZC94sMRX8Mtnznwe_ALVEowL6ES_9KEOgn5JVMBvbihQ0nURPT0bHsOsi8ovSB6Rgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TZDe8EIOjiCOwRFKjrEbiofW_dmDahnBD6K5W7hXewru89gMyRio6j4QY16X499t3kwvs-fepU6Iwohwv9N-0Yu48QjyhNwZBaXFQ8Az_4QPRSdrfwTrhyDICoiq9VfpxKHDt_mh_3npcNhMvUQXw9zmtPGSDlvVIdVMwaSwWfOjpOni_BnCHsmhG-NVkwvH7PUtdWvo-23DLJ2RN2D8Fm2D709gRi1MGrtGmRygCIRsCZ90po9Fd2DrlAzG7vZh6as5YRT4-cQDk2P2JA2VEkwG_NZRiSIy4YTLAejWKjpag3vF-WZwyuH_LrKyrxv3EBgRxgaimvat74h0fO1Fwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PMi4jvtRocYQmro4CQR-TvNylTCqrNKPV2LVhjTCoLo2g3Y8GLmOB9if5g-ZP61GMaU3XFtXbl31rJUiD8MwO1lIwHw7Yv7bktIRfFyayHOv11aK6xtXE3jZDMZ6PkUcYBCLW7ILOfvfMpsdBp0XYmMSv7AzZ4Cj78nQXMZDiuGgEQQaQdMZlr6gyug2WHqBnHxDejkVNRnQ7PnNMBCFS4Y8bEZP9pGcPEev-qLbJMCYlBsSf1iwrgtSGpxVeBQEgoa4i5Uc8LnidEKRw5kMW8P59C6kG9yODuOvFps1eWnxdp6n5Y2lQL1UxTmqgc3X2O3jq1Ap1v4rxiI4ejtsDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/454667" target="_blank">📅 01:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454666">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">دادگاه سوئیسی استقلال را ناامید کرد
پنجره پلمب شد
🔹
باشگاه استقلال در بیانیه‌ای به‌صورت رسمی اعلام کرد که تلاش‌هایش برای بازکردن پنجرۀ نقل‌وانتقالاتی این تیم موفقیت‌آمیز نبوده. این یعنی استقلال در پنجرۀ تابستانی نمی‌تواند بازیکنی را به خدمت بگیرد و باید با داشته‌هایش از فصل پیش در لیگ برتر و لیگ نخبگان آسیا به میدان برود. آبی‌پوشان در این پنجره دست‌کم ۹ بازیکن از فصل پیش را از دست داده‌اند و نتوانسته‌اند کسی را هم به خدمت بگیرند.
🔹
فسخ یک‌طرفه قرارداد منتظر محمد توسط استقلال، بعداً به شکایت او در فیفا منجر شد و فیفا هم باتوجه‌به این فسخ و سابقه فسخ‌های مشابه، باشگاه را با محرومیت از دو پنجره نقل‌وانتقالاتی روبه‌رو کرد. مدیران باشگاه استقلال با استخدام یک وکیل ایتالیایی تلاش کردند تا پنجرۀ این تیم را از طریق شکایت به دادگاه حکمیت ورزش CAS باز کنند.
🔹
حالا مدیران باشگاه گفته‌اند که در این کار ناکام بوده‌اند. تاجرنیا، سرپرست مدیرعاملی در توییتی عصر چهارشنبه گفته به‌ دلیل «کوتاهی قبلی» چنین اتفاقی رخ‌داده و توپ را به زمین مدیران عامل پیشین انداخته. وی حالا وعده داده که از بازیکنان آکادمی در ترکیب تیم اصلی بیشتر استفاده خواهند کرد.
@Sportfars</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/454666" target="_blank">📅 00:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454665">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojoJOsqJo88HDEiLlITVDnT8cgYBNqqQQxoTurS1shLlSJeqILVRkN8Fbruy1gV1bRheVu34R0R7a_aoOI36K_PFP4twAKp2RmQHnlr-E3Ibwf5y0IJbvUe1zNKo1Hd3S04rO1sAXKwNkZB9hYSO3LlwRumXSiV9zqFfxTgtuNdG3ZY7p_pWENTowxDNU65NhAEz53OAq5_N1erfXl2YcuQ18VE_GbOuxhoX-F-4GNfPW14byqe8fy9F8DFA1uzn5m7GYP2pj081HRy8bI_KUNCusvjuDiGfeAA3Tjv5s9gjduKizOhuEXdI8AxLf9SCVy4HBQLt0a_-YYXRFdSffQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت تسلیحاتی اسرائیل از امارات، این بار با ارسال پهپاد
🔹
بر اساس اطلاعات افشا شده، در سال ۲۰۲۱ جلسه‌ای بین مدیرعامل شرکت «البیت سیستمز» بزرگترین تولیدکنندهٔ تسلیحات اسرائیل، و رئیس دفتر سیاسی-امنیتی وزارت جنگ اسرائیل برگزار شده و در آن فروش احتمالی سامانه‌های تسلیحاتی مختلف به چندین کشور از جمله قطر، عربستان سعودی، اتیوپی، رواندا و ترکیه مورد گفت‌وگو قرار گرفته است.
🔹
بر اساس این سند، به البیت مجوز فروش پهپاد هرمس ۹۰۰ و همچنین مهمات سرگردان «اسکای‌استرایکر» با بُرد محدود ۶۰ کیلومتری به امارات داده شده بود.
🔹
همچنین در این دیدار در مورد فروش احتمالی بمب‌ها و مهمات یک‌تنی طراحی‌شده برای نفوذ به پناهگاه‌ها و سازه‌های مستحکم  نیز بحث شده است.
🔹
بر اساس این گزارش، شرکت‌های تسلیحاتی صهیونیستی با افتتاح دفاتر محلی، سرمایه‌گذاری‌های مشترکی را با شرکت‌های دفاعی امارات شروع کرده و فروش تسلیحات اسرائیلی به امارات همچنان در حال افزایش است.
🔸
به گفتهٔ هاآرتص، برنامهٔ فروش پهپاد به امارات بخشی از معاملات بزرگ بین تولیدکنندگان تسلیحات اسرائیل و کشورهای امضاکنندهٔ توافقنامهٔ ابراهیم است که به‌ندرت به‌طور رسمی افشا می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454665" target="_blank">📅 00:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454664">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhrd1xm8EYTUIm-TvQyqW_uC31Jq4WEUF_HL3agBdgIkY0389Os7PVrNl_VES_BXunzcZ4hnmeX27c6O3GL-CVWq1D5gwn2_ovc-_3-uMlerX1UCUafxYblXA-5_doRTv4wzkgZun17JhS7tpTcJqbmgtkHDLGNy4dT7qOuE2khXo7v5mR031SRUyrixDGtQSagW-tUQo5QhHZarIIK2hHei7YEXkYsSf8QUaiNwQIBPwfGEWQeraT-FQB7dO7bBZIlfJyeqN7X5oaTz8UstpUViRSvzDrJdcVX6POuW1cNzpHhiD-09gfjXo13nBdBTlVAmpzsr7PpiXRmH9sdOMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه حمل‌ونقل اربعین: در این موج از بازگشت زائران اربعین، هر ۴۰ ثانیه یک اتوبوس از پایانۀ شهید رئیسی مرز مهران خارج می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/454664" target="_blank">📅 00:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454663">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e352bba80.mp4?token=G8QG-jCVs-KkmvZYsnph5pyCsU7BOtBBBO4x2I6Bp1-yGXzaBBFmmVEj1q1I-wl920sAFAt4HXmOIiFYOd4I9EVoLiY5uTjV-Anx2CpBBfHxgw0osVbZ5LJpnsDW6KJvbNUr3Iw2njn59C5vRU0C7gAc09kkv_zZPkBnQPj9OP53HO2cfF4Dj_ai_PwQwxzBpqQdNuY2fa98nkH545KBSb-HfbdIXCYDIUxVFqEDit3zemlKfkavYTsGn3KjFFr7BOdFayUiFKCIHN78agcRereNZoquuQiKWtXjFLb40lBm-00Ud-hdR2hHiL4MJ6BlikHEBRSlBpXAe14R22hVzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e352bba80.mp4?token=G8QG-jCVs-KkmvZYsnph5pyCsU7BOtBBBO4x2I6Bp1-yGXzaBBFmmVEj1q1I-wl920sAFAt4HXmOIiFYOd4I9EVoLiY5uTjV-Anx2CpBBfHxgw0osVbZ5LJpnsDW6KJvbNUr3Iw2njn59C5vRU0C7gAc09kkv_zZPkBnQPj9OP53HO2cfF4Dj_ai_PwQwxzBpqQdNuY2fa98nkH545KBSb-HfbdIXCYDIUxVFqEDit3zemlKfkavYTsGn3KjFFr7BOdFayUiFKCIHN78agcRereNZoquuQiKWtXjFLb40lBm-00Ud-hdR2hHiL4MJ6BlikHEBRSlBpXAe14R22hVzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوحه‌خوانی مهدی سلحشور در تجمع امشب مردم رودان هرمزگان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/454663" target="_blank">📅 23:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454662">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95ffb726b8.mp4?token=QFvYjDarGPtNqhgS0vHqbBIWumObXBE5-R_cYk_uDD-sKGTqxhOkQCLF02nMqUv8aAMGh6nJo_zUOIQWDJ3XMtPRl_UOyRo3ykL-Uc0Ql5PccJad7p0MQceoJD1iRmVD023qOQj0c0qFDH2E038Mh8GmcdKPjmtnW6YyQ0kJRK6L7ujaJmNMkz5xpOqwo-e_I6iqYMw2bQkghxvNb9xiFffTIP1_TZL8vS4ZdGz2Pc24RM_iaBdfmRTRY61CVmWuPM-n4YepUzgcNLbCRRHNHPsQ0-T6rZUOS4LqeEq-lYeYPyJujQtsrnEBU_dKfACHpjrtZRSpIpiBo9WFa-EEIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95ffb726b8.mp4?token=QFvYjDarGPtNqhgS0vHqbBIWumObXBE5-R_cYk_uDD-sKGTqxhOkQCLF02nMqUv8aAMGh6nJo_zUOIQWDJ3XMtPRl_UOyRo3ykL-Uc0Ql5PccJad7p0MQceoJD1iRmVD023qOQj0c0qFDH2E038Mh8GmcdKPjmtnW6YyQ0kJRK6L7ujaJmNMkz5xpOqwo-e_I6iqYMw2bQkghxvNb9xiFffTIP1_TZL8vS4ZdGz2Pc24RM_iaBdfmRTRY61CVmWuPM-n4YepUzgcNLbCRRHNHPsQ0-T6rZUOS4LqeEq-lYeYPyJujQtsrnEBU_dKfACHpjrtZRSpIpiBo9WFa-EEIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشاهدات بلاگر روس از مهمان‌نوازی و صحنه‌هایی متفاوت اربعین امسال
🔹
جمعیت کثیری امسال با پرچم قرمز آمده‌اند، برای آن‌که نشان بدهند مصمم هستند تا انتقام خون مرجع دینی و رهبر عالی‌قدرشان را بگیرند.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/454662" target="_blank">📅 23:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454661">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aG6L_qbn7lsoyjPuzAB8eu5UJV59G_nXpWmT6YLk3rFl3y1kVbprs4qNAWhnZb-UWZBFPJDs2nT9LTPETwVgwSEOnROrVkTJiwvZf9eyGcgdz-fLIvgc-_U8_AOfEftVxviLz74CQ4AWQpB4mio6TQ8KKchrhC0Vhxcq29TyJtn-C2tmrjPC52zqdXefJhZBVVp_6JiVXAgX9YMVDbrw8vmA1YokCW8kXgSnxTXB5X_NM0zaJYKuTsUAsA1TemynD6VrvyBlt7yQZNEvRI2zHRj1gmvn8dMOg_iF6d0CBV-ZqJKyz2PL563lOtbRPk26LtPq9ABZVPeySUbaa3ztuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رهبر معظم انقلاب: از اصولی‌ترین امور، اصرار بر اتحاد مقدّس در همه‌ی سطوح است؛ پرهیز از تفرقه و تنازع وظیفۀ همگانی است
🔹
لازم است به شما مردم باوفا و سرافراز ایران عرض شود که از جمله اصولی‌ترین امور در این برهه، اصرار بر وحدت کلمه و اتحاد مقدّس در همه‌ی…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/454661" target="_blank">📅 23:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454660">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqbkPxbiX5BD4SZwKVsn-qsS0r5-T9SOl9KarVk91lMXnLNUy5BGvUokQdtyAdxXRsCGzTVCHsDICsMlr3QoJGKK6_3_Co27IMqrDfgYjUkeTIzaH0c9dran40EQjzskyjSn3FEVh6uHHc9_5M4J8jLD2pTIezj0aTl0qfZe6-UbCK5Ng6p5mdEDAIz1HwisYlR5w8Y6Vg0vpjm057aEijSPtHrf4P6cx_qo_Pt_Nk9MTSHsA61ln0RGrMm7WX-mN6LVywHdYeW_yUhCVsLjUp83M-1v_qZowLeC15WCWZZFoBO1u5uK50w9eLPppk3zlP_6hpHHbjtIt32YgmsU5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
عضو هیئت‌رئیسه فدراسیون در پرسپولیس پست گرفت
🗣
با اعلام باشگاه پرسپولیس، محمدرحمان سالاری، عضو هیئت‌رئیسه فدراسیون به‌عنوان مشاور حدادی، مدیرعامل سرخپوشان منصوب شد.
@Sportfars</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/454660" target="_blank">📅 23:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454658">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egQCZz6VnEKbNknMV3FZW9dPc19wtMXTzf7OclDZqnFn9D1z-DovnY2fO62bFd9neIIsrFI7VpPfB6U5HEy6krujMHYbJPwJncO8XR7cn5zOI2C9eJDH4bdPvDLH4AjZC2ZXk-yC2tUI1Pu29np2vJt2ttfGjjOetVmap08BtQe1C2ETO7Ed3D2rrD4-vPM80_z9rPZQ7pVFjZpGitqrWsjBe_afXxrrXLmMePqKjWBNpY3Y7zUP-wIKUh56KQlJ3UUJTtuoOEedTlloBIvlYzL5tsKiYY7ntxzDIWDLHbtTo02iYSCLUJ2ZneYzPNUYHX9N9H5s11ToCidx6V-sFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام مستعفی دولت ترامپ: آمریکایی‌ها از هر ۲ حزب کشور خسته شده‌اند
🔹
جو کنت، دبیر سابق مرکز مبارزه با تروریسم آمریکا: اکثر آمریکایی‌ها چیزی دربارۀ غزه یا تنگۀ هرمز نمی‌دانند؛ آن‌ها فقط می‌دانند میلیاردها دلار از پول‌هایشان به خارج می‌رود و سربازهایمان کشته می‌شوند.
🔹
یک اجماع روبه‌رشد از افرادی وجود دارد که از هر ۲ حزب جمهوری‌خواه و دموکرات در حاکمیت آمریکا خسته شده‌اند؛ آن‌ها می‌خواهند ما از این جنگ‌های احمقانه‌ خارج شویم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/454658" target="_blank">📅 22:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454657">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUw6yCOWOFkvQncAI7mO_remjSsfPnCOnyxRWT41a1KmrWVclsn-pBV7qUD7TsIjADx3H0f2h0BepA3JS9TMHo0Wx1Z0EfIHp0YRNozzfDBATQNUbSSTsf-GwcJacoEGIXQN3Qwisx0HTJQKHwNd-6qEzhQsl9dPwxtis7OAWZURdlPaRWxeWynkVJgRyuqT-CDmfw50eDMDqfb2dGhG0Yev688hJRmQMynUIPlGuW-ZY9lePB9MD4j6otykd_4OOCRJiBB5C9BNhSQHTax1M-w9J0ZbZyKnh4jMm_hmSAsJe00SKr8pWubbDcIKFj9sTRP7HOIQUmFybQvCwuq6KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ایرانی‌ها چقدر از هوش مصنوعی استفاده می‌کنند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454657" target="_blank">📅 22:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454654">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b22d6fe91f.mp4?token=ixuf01VJY23syjIFg86Msh_OrPTzY3fOykqf7qda_lyJjwmJF_RXG00KTqW8tB1WVBINXpggA_PoYQ-SiaVpZEHFOAS-q76-xt5iFJ6EwsdMO3ATRiqO1wOWKJ-ntoWKh4dGvUNewIGU2Dd8a8ZamV5bBdNK5ix8YhYzVvNrLhf5GJjcsRTDlnSlmB_UYjeFArhxUFmf-lQ24ULx4dFRlDz1DmVq7z5CzogoZc6gI8jGXINzmsCGL4W12IpFdbTD97wmSqHnAwfiAMsBlWGGJNOjo7dPFoJ9VZ-_4rr869tnaZmZVwtOg5Kt6M8uyO3O79dqcL6lZ2SYafSbZAQLBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b22d6fe91f.mp4?token=ixuf01VJY23syjIFg86Msh_OrPTzY3fOykqf7qda_lyJjwmJF_RXG00KTqW8tB1WVBINXpggA_PoYQ-SiaVpZEHFOAS-q76-xt5iFJ6EwsdMO3ATRiqO1wOWKJ-ntoWKh4dGvUNewIGU2Dd8a8ZamV5bBdNK5ix8YhYzVvNrLhf5GJjcsRTDlnSlmB_UYjeFArhxUFmf-lQ24ULx4dFRlDz1DmVq7z5CzogoZc6gI8jGXINzmsCGL4W12IpFdbTD97wmSqHnAwfiAMsBlWGGJNOjo7dPFoJ9VZ-_4rr869tnaZmZVwtOg5Kt6M8uyO3O79dqcL6lZ2SYafSbZAQLBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور مردم بجنورد در موج ۱۵۸ اجتماعات شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/454654" target="_blank">📅 22:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454653">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">تیراندازی مرگبار در آمریکا
🔹
فاکس‌نیوز روز چهارشنبه از تیراندازی در کارولینای شمالی خبر داد.
🔹
چندین نفر در تیراندازی جمعی در پراسپکت هیل کارولینای شمالی کشته شده‌اند و دست‌کم یک نفر نیز مجروح و به بیمارستان منتقل شده است.
🔸
پلیس محلی اعلام کرد که این تیراندازی حوالی ساعت ۸ صبح به وقت محلی رخ داده و تحقیقات درباره آن آغاز شده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/454653" target="_blank">📅 22:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454652">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49c34903d7.mp4?token=Z3z6V5cUA1bKVnVOaQeiMh4T9PSPSg6KQlyZyUi1-J0eGSVs7-BQBnQPjV0y9M3GIfXLDBV1XYunWCdu4k6OobXSSpT73lwb2V14CbMW8WFfUQ0kJDxmjdoxjXwUoi8z0JDwiQYhWdjE3sRadoeT8lDZ5aHKtc9t-uUNZTI3qg0yLERbWUH_bMlPylPzwk4E8q4FdjtYrY2D1YtQPcMWRIHy95iPI6jEClz6Bij4eNR8ye9_kR0sYmjTj5EOe4LVQv3ILNxM6kTqW8MaUGC5kCKz8dPo_OcJi8gBiVkduD6XEg3j6JXqj7waaH9b0Zgl4PBiLa-YBKg_S8YBVf47bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49c34903d7.mp4?token=Z3z6V5cUA1bKVnVOaQeiMh4T9PSPSg6KQlyZyUi1-J0eGSVs7-BQBnQPjV0y9M3GIfXLDBV1XYunWCdu4k6OobXSSpT73lwb2V14CbMW8WFfUQ0kJDxmjdoxjXwUoi8z0JDwiQYhWdjE3sRadoeT8lDZ5aHKtc9t-uUNZTI3qg0yLERbWUH_bMlPylPzwk4E8q4FdjtYrY2D1YtQPcMWRIHy95iPI6jEClz6Bij4eNR8ye9_kR0sYmjTj5EOe4LVQv3ILNxM6kTqW8MaUGC5kCKz8dPo_OcJi8gBiVkduD6XEg3j6JXqj7waaH9b0Zgl4PBiLa-YBKg_S8YBVf47bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: حوادث دی‌ماه پارسال قابل فراموشی نیست؛ کسانی‌که کشته‌شدگان را ۳۰-۴۰ هزار نفر اعلام می‌کنند، نامرد و وطن‌فروش هستند.  @Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/454652" target="_blank">📅 22:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454651">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc659092fa.mp4?token=R_w9Bi0vilROgZK2LQVdUywmfN5ermQHx48uE8QK0IVzgKMjO1g0RkcMRBYZbOFOxD38ZA4u1N0_2pe-EXwY9-Rg0xApW8jEEp1Y45zgynQSr0CKC1NhINgLL6qRu1pWBDb9OvsN3N2lTjV7j-gNZ9lRvjZ7A0D01ljr6Q6UhBIeXxgrU-ruQmHhpbnZypZnaYjzeRPG4QOurJmo1DCRhPLhAn4cSOAYKj5BiOpUCfIFL63KIzjkFe5QcsTrkXKmfOFHH4tpndGjRtt2IkIUnONEFDEsnBlTg-YpCB-ncTP5Tba27HzYkpIW2H5_L1iJ1gWlTp74PIlLmnEH5wdh0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc659092fa.mp4?token=R_w9Bi0vilROgZK2LQVdUywmfN5ermQHx48uE8QK0IVzgKMjO1g0RkcMRBYZbOFOxD38ZA4u1N0_2pe-EXwY9-Rg0xApW8jEEp1Y45zgynQSr0CKC1NhINgLL6qRu1pWBDb9OvsN3N2lTjV7j-gNZ9lRvjZ7A0D01ljr6Q6UhBIeXxgrU-ruQmHhpbnZypZnaYjzeRPG4QOurJmo1DCRhPLhAn4cSOAYKj5BiOpUCfIFL63KIzjkFe5QcsTrkXKmfOFHH4tpndGjRtt2IkIUnONEFDEsnBlTg-YpCB-ncTP5Tba27HzYkpIW2H5_L1iJ1gWlTp74PIlLmnEH5wdh0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: بسیاری از فرماندهان و دانشمندان شهید ما هیچ دارایی و اموال خاصی نداشتند  @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/454651" target="_blank">📅 22:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454650">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa5a47592.mp4?token=uMqyhvypHC-9PQqmrpasF6uIQQ-_oXca-mQa7rOFIF6ZRsYTWtmCOauqsuye3UQ56QtpFxTq3g0Znb9bbfDJKCqKDQZ4ZG2DQGnKs18oRTTx-H1_Er4C_5wjKeslRm2i_yhHTb7LfTSUNLHafhLtLR88uMsRifQeXuhEINt_PBtcrntAzIoQ2Jx8COhqMzFmCi5KhDhSxezIkq0FzQufKSd1LbvLLS3ozoKo8vZbFjDxwpVQOU-WfYsqe0n-TDraWZSHPVaawWrGHYcXRa0YCrivWxqhOlQ-mlyMVKjt4Gl5rQAAl5SlxDzJBmeV74g1IkUaDdK3M5KJzZ6pqWxx8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa5a47592.mp4?token=uMqyhvypHC-9PQqmrpasF6uIQQ-_oXca-mQa7rOFIF6ZRsYTWtmCOauqsuye3UQ56QtpFxTq3g0Znb9bbfDJKCqKDQZ4ZG2DQGnKs18oRTTx-H1_Er4C_5wjKeslRm2i_yhHTb7LfTSUNLHafhLtLR88uMsRifQeXuhEINt_PBtcrntAzIoQ2Jx8COhqMzFmCi5KhDhSxezIkq0FzQufKSd1LbvLLS3ozoKo8vZbFjDxwpVQOU-WfYsqe0n-TDraWZSHPVaawWrGHYcXRa0YCrivWxqhOlQ-mlyMVKjt4Gl5rQAAl5SlxDzJBmeV74g1IkUaDdK3M5KJzZ6pqWxx8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: من در مورد بازگشت ایرانیان خارج از کشور با رهبر شهید صحبت کرده بودم که ایشان دستور بدهند که هر ایرانی خواست وارد کشور شود برای او مشکلی ایجاد نشود و اگر مشکلی وجود داشت از اول بگوییم نیا و اگر آمد به او بگوییم برگرد وگرنه بازداشت می‌شوی.  @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/454650" target="_blank">📅 22:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454649">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c6223c099.mp4?token=nCEDmXD878HlGEuht05nsuaFb-qqacrA_w7cMDFXyQmUWU2405DWlQpXV9nCNpTU-5Z-Obzavdvxj9vMHYu6LqACkW022ht1Kw7P4N_I3NJ3wNsQNC2vwb2WmaVMKLYfeKUmypzxrEVzOyeM8ALNLXKEnrlukO7nlLGlL92iWjUCBQvGxdWdjA8T7pLRmUd3GNCy9BUJF-kZr6zzC6YqcKkXb392pkg8IQL3Exz5zGKktBgFrPQVx4--fTxU-lxczTKWFGQcy2t5Vctz32EjV36aphMsNzzzhwZbqlQk03VvaHi85FyUbWX99kZRJXlxpmEJwPbaNLs94ydXHsBFXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c6223c099.mp4?token=nCEDmXD878HlGEuht05nsuaFb-qqacrA_w7cMDFXyQmUWU2405DWlQpXV9nCNpTU-5Z-Obzavdvxj9vMHYu6LqACkW022ht1Kw7P4N_I3NJ3wNsQNC2vwb2WmaVMKLYfeKUmypzxrEVzOyeM8ALNLXKEnrlukO7nlLGlL92iWjUCBQvGxdWdjA8T7pLRmUd3GNCy9BUJF-kZr6zzC6YqcKkXb392pkg8IQL3Exz5zGKktBgFrPQVx4--fTxU-lxczTKWFGQcy2t5Vctz32EjV36aphMsNzzzhwZbqlQk03VvaHi85FyUbWX99kZRJXlxpmEJwPbaNLs94ydXHsBFXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: من در مورد بازگشت ایرانیان خارج از کشور با رهبر شهید صحبت کرده بودم که ایشان دستور بدهند که هر ایرانی خواست وارد کشور شود برای او مشکلی ایجاد نشود و اگر مشکلی وجود داشت از اول بگوییم نیا و اگر آمد به او بگوییم برگرد وگرنه بازداشت می‌شوی.  @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454649" target="_blank">📅 22:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454648">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b08b848d71.mp4?token=EXe0LwFTSVpFbhV6e4IUSiamYTKVAfO_T28SwFz2gjkuFIVpBiqKzeOjX3UkMwa-rCed4DM5iSW2bwG2uYCb_O77n64DOQUnmW6ado9STzPyV8NlqtB5aKh_f42-mORV_k6-3s7CQ4VP-zrtEhpPAMpsavQDaui-epMTC8kcoT9D9pP2iMZsq973XeG4wbUe4Dw6GYmaXcMXLQUuwZkgQdMhygHKvGgqB3m90c4ZVAmr26OsDjKvOKrbXJzL9PzxVp9Fa8KMXUJVrCvSTAgk_eqGikQnvef7zWmg7FwmhX-MhB_HdEpG1Ss2qbVZZtK9SS5usnWlEEyCQUr6I7vBjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b08b848d71.mp4?token=EXe0LwFTSVpFbhV6e4IUSiamYTKVAfO_T28SwFz2gjkuFIVpBiqKzeOjX3UkMwa-rCed4DM5iSW2bwG2uYCb_O77n64DOQUnmW6ado9STzPyV8NlqtB5aKh_f42-mORV_k6-3s7CQ4VP-zrtEhpPAMpsavQDaui-epMTC8kcoT9D9pP2iMZsq973XeG4wbUe4Dw6GYmaXcMXLQUuwZkgQdMhygHKvGgqB3m90c4ZVAmr26OsDjKvOKrbXJzL9PzxVp9Fa8KMXUJVrCvSTAgk_eqGikQnvef7zWmg7FwmhX-MhB_HdEpG1Ss2qbVZZtK9SS5usnWlEEyCQUr6I7vBjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: همۀ ذهنیت من دربارۀ حقوق بشر و نهادهای بین‌المللی فروریخته است
🔹
به چه جرمی رهبر و فرماندهان و کودکان ما را شهید کردند؟
🔹
دشمن با هرچه باعث رشد ما شود مشکل دارد. @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/454648" target="_blank">📅 22:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454647">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11ec7e1eee.mp4?token=uGGvLMeBvaOopvn85eET2GFYY7sOtpv1LOIy-oUitcc8ZEqxZh0H6BnscRy4tjaZnz3KNcFrnplI3Ov3-FfCaX7DYU8JTorN3WtmOamYUo8Q-KIyCcb2ulACkwApzEF4ZHpzFPUDLFuv3KGd6p7yxLBfiRM5ZmJ8O5ybw0a0Xy6YGtoV4nnWqra0xT_DrbuXnkVdbPVB1JEIOWqr8Qa_cAw1UfebjuaYsdO0vDGgZoqae0_FeQRBzITfxcFN-0uTfEHiCCWMlQJ-vJEVY-5-FrVRg4hcM2U1m9UdMSIqo62XZR3IRPRD8nDcVeVLmMTDr5YYEFY9Xv1fYIbO-hxYtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11ec7e1eee.mp4?token=uGGvLMeBvaOopvn85eET2GFYY7sOtpv1LOIy-oUitcc8ZEqxZh0H6BnscRy4tjaZnz3KNcFrnplI3Ov3-FfCaX7DYU8JTorN3WtmOamYUo8Q-KIyCcb2ulACkwApzEF4ZHpzFPUDLFuv3KGd6p7yxLBfiRM5ZmJ8O5ybw0a0Xy6YGtoV4nnWqra0xT_DrbuXnkVdbPVB1JEIOWqr8Qa_cAw1UfebjuaYsdO0vDGgZoqae0_FeQRBzITfxcFN-0uTfEHiCCWMlQJ-vJEVY-5-FrVRg4hcM2U1m9UdMSIqo62XZR3IRPRD8nDcVeVLmMTDr5YYEFY9Xv1fYIbO-hxYtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: رهبر انقلاب در مورد تفاهم، نظر کارشناسی را پذیرفتند؛ ایشان گفته بودند که اگر سه‌چهارم رای بیاورد آن را می‌پذیرند
🔹
امکان ارتباط با ایشان سخت است ولی بودنشان نقطۀ قوت بالایی برای ماست. @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/454647" target="_blank">📅 22:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454646">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3ef09d2f1.mp4?token=aZvNDfnZKfn50qepSH8oktUOtXQGYvbWeWCKHpJ8IuT2L9aach6A7WfXSRDUVdW-X2Cg2uiQPLRHrk8GGZAcT8iPZu7oUvrVMjglkFwHucVek3f2GfAoohaaEhEQHF_-nh6FXc6g263McGWFueG4EJJXN4i0SydYyT_EiFcWPaGXz741CVUYRQ4SpCAWUCBCh2z0ipf6f-J7hcBBe0_av-2aeUMmMs7I-6ET_tYlHpK0F9uXEjl0WA01UhvmHq_wqnFVyW_x09sHv9-PvpxEvI4Mo6B9AtmSzrRR--Eeyxt_svGRF14kAg-mbsT-PhQiJBVvD-HcC6TmSCLZ2aZtHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3ef09d2f1.mp4?token=aZvNDfnZKfn50qepSH8oktUOtXQGYvbWeWCKHpJ8IuT2L9aach6A7WfXSRDUVdW-X2Cg2uiQPLRHrk8GGZAcT8iPZu7oUvrVMjglkFwHucVek3f2GfAoohaaEhEQHF_-nh6FXc6g263McGWFueG4EJJXN4i0SydYyT_EiFcWPaGXz741CVUYRQ4SpCAWUCBCh2z0ipf6f-J7hcBBe0_av-2aeUMmMs7I-6ET_tYlHpK0F9uXEjl0WA01UhvmHq_wqnFVyW_x09sHv9-PvpxEvI4Mo6B9AtmSzrRR--Eeyxt_svGRF14kAg-mbsT-PhQiJBVvD-HcC6TmSCLZ2aZtHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: نقشه کشیده بودند ایران را ۴۸ ساعته مثل سوریه بگیرند
🔹
شهادت بزرگان ما در جنگ رمضان دردناک بود؛ با همه سختی‌ها و مشکلات امروز از ایران به عنوان یک کشور قدرتمند و با عزت بالا نام برده می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/454646" target="_blank">📅 22:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454645">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cd906c65a.mp4?token=G_i8lzhYfY6FWHluB1XIulXQ23qema-b5zlRZF-UUT_8bMqb18qd3EJ9BKCqsL0yisdnFSd11WBig-pvHtgr4rZr4ktX5fTwT447VEY8cmYxunFtM6GczFKTTSaoL6UyLYzS8y84hCqJKH0ZzhytH4fZOsOiB6MZc203jsFzfrWM2LNoGK9WU7V_EhJrDQSxGuPwgI7LC9T9QUVxfjNJxCfQ5in11fj3_VVpr9oAiQ_L1XdOaEODye7t5HaNVIs95gGCRQlQXvZBhOXQjJ6-QjS3vld06bqUUDQwAYNeA7x2JzpnCASgFHBQccA_xPSK6s3MdUdqMq2gNZ6DwMmbdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cd906c65a.mp4?token=G_i8lzhYfY6FWHluB1XIulXQ23qema-b5zlRZF-UUT_8bMqb18qd3EJ9BKCqsL0yisdnFSd11WBig-pvHtgr4rZr4ktX5fTwT447VEY8cmYxunFtM6GczFKTTSaoL6UyLYzS8y84hCqJKH0ZzhytH4fZOsOiB6MZc203jsFzfrWM2LNoGK9WU7V_EhJrDQSxGuPwgI7LC9T9QUVxfjNJxCfQ5in11fj3_VVpr9oAiQ_L1XdOaEODye7t5HaNVIs95gGCRQlQXvZBhOXQjJ6-QjS3vld06bqUUDQwAYNeA7x2JzpnCASgFHBQccA_xPSK6s3MdUdqMq2gNZ6DwMmbdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: رهبر شهید مثل کوه پشت ما ایستاده بود و از دولت حمایت می‌کرد
🔹
اگر کمک ایشان نبود می‌توانست تنش‌های اجتماعی شکل بگیرد ولی پشتیبانی ایشان اجازه نداد. @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454645" target="_blank">📅 22:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454644">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e7bd0df98.mp4?token=UqYhaMsdwED8uJM-svYz9FQaKPLZOfKdElswAodAhYAtVOV43mEZQUuI06_8MH1cMBJqPqTJe8xCdwaF29tyM41zgfwbwlEJv5ko4lXhsReazh-gOYh6bdjz8L8c4xnjPQYTa0ElUtfcstPHONEHSYCi4o57FPqCCZIG0Q2yen31qjYFFpSxeLU9mZE6JWBqyOOukVZ9ak-HpBDarcfWab2MH82GWoLicuCgLze8aepu2zthWFQUc-6zwNZ3NOewbYsK3EWIzQBPn0559rp20pm18DnwJbv3hTB3mzvWcL9_5Iegw8FZ64S9PKJ0IYWTGCFO6Hz03gFuUS9DUbA4yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e7bd0df98.mp4?token=UqYhaMsdwED8uJM-svYz9FQaKPLZOfKdElswAodAhYAtVOV43mEZQUuI06_8MH1cMBJqPqTJe8xCdwaF29tyM41zgfwbwlEJv5ko4lXhsReazh-gOYh6bdjz8L8c4xnjPQYTa0ElUtfcstPHONEHSYCi4o57FPqCCZIG0Q2yen31qjYFFpSxeLU9mZE6JWBqyOOukVZ9ak-HpBDarcfWab2MH82GWoLicuCgLze8aepu2zthWFQUc-6zwNZ3NOewbYsK3EWIzQBPn0559rp20pm18DnwJbv3hTB3mzvWcL9_5Iegw8FZ64S9PKJ0IYWTGCFO6Hz03gFuUS9DUbA4yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: اگر تابه‌حال کشور سرپا مانده مدیون مردم است
🔹
اگر با مردم باشیم هیچ قدرتی نمی‌تواند ما را زمین‌گیر کند.
🔹
دشمن فشار می‌آورد تا مردم را به اعتراض وادار کند.
🔹
اگر به مردم خدمت‌گزاری نکنیم با خدا جنگ کرده‌ایم، از خدا می‌خواهیم کمک کند تا شرمندۀ مردم…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454644" target="_blank">📅 22:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454643">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0653169395.mp4?token=QyNmmDlx0GKSUg7ve7biZ4RwWuIyQAa90-7e4W8z1I1lp2ElpdXbJM2YTMk1L_f3bh_EuOUw1dHDvuNn8-ZMlcL1ngiCqHBNnBrevIs5Dwp71ZFqMVZmX986SD15wXR-bFYuBoysqev7pzMtghWJjS6RrQ_O-HFmRoFqQodGfXAjo00d5XqJ88sG4Qgf7UVINwaKQjmaXR8a1hAuu95NFDneHCY9Pyi554_VufdSHnRKsOCgIGOkXH2MkPPW7YGOgsqnliMUPB1rOZ1o7IduWV7vKesgvtGy4DzgwH2oTU8axi7QPisC5zTLTMKFPaLLomuVPfMx6oIC46llYjHDNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0653169395.mp4?token=QyNmmDlx0GKSUg7ve7biZ4RwWuIyQAa90-7e4W8z1I1lp2ElpdXbJM2YTMk1L_f3bh_EuOUw1dHDvuNn8-ZMlcL1ngiCqHBNnBrevIs5Dwp71ZFqMVZmX986SD15wXR-bFYuBoysqev7pzMtghWJjS6RrQ_O-HFmRoFqQodGfXAjo00d5XqJ88sG4Qgf7UVINwaKQjmaXR8a1hAuu95NFDneHCY9Pyi554_VufdSHnRKsOCgIGOkXH2MkPPW7YGOgsqnliMUPB1rOZ1o7IduWV7vKesgvtGy4DzgwH2oTU8axi7QPisC5zTLTMKFPaLLomuVPfMx6oIC46llYjHDNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: علی‌رغم مشکلات ۲ سال گذشته، امروز ایران را به عنوان یک کشور قدرتمند و با عزت می‌شناسند.  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/454643" target="_blank">📅 22:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454642">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c783b2a39.mp4?token=rHY1iF2SNXclDIuQQgVIvT8oiC7WsHI0O2ZVDwuR2au_45FXtJMHVphE37zOOlLNvzYUmiC_TMIA0EaFyjwet5Z9I0IzFuY9Owz0EeIYr-teoeREtunCLqyjTLD3B7GIf7MXwBUY3FrSv_YgHwxuCrvQOakAn1rS89tcM_WUADzOu1N-yW26bmU9bZedy6xu1Ogm85y4Kf49VFPqUJE-i-aqdN05LlIlVIkYclqjvUK6dylMipSbGultTz8p6gUHlaK14_dFMs-moW3-X5lJ0vJLk-9Xc4vhDkgUKg7EgqTW4DHc_KqKcs-Sl1AxAbwm-IyTjACcF2g8psti2PFdBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c783b2a39.mp4?token=rHY1iF2SNXclDIuQQgVIvT8oiC7WsHI0O2ZVDwuR2au_45FXtJMHVphE37zOOlLNvzYUmiC_TMIA0EaFyjwet5Z9I0IzFuY9Owz0EeIYr-teoeREtunCLqyjTLD3B7GIf7MXwBUY3FrSv_YgHwxuCrvQOakAn1rS89tcM_WUADzOu1N-yW26bmU9bZedy6xu1Ogm85y4Kf49VFPqUJE-i-aqdN05LlIlVIkYclqjvUK6dylMipSbGultTz8p6gUHlaK14_dFMs-moW3-X5lJ0vJLk-9Xc4vhDkgUKg7EgqTW4DHc_KqKcs-Sl1AxAbwm-IyTjACcF2g8psti2PFdBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: علی‌رغم مشکلات ۲ سال گذشته، امروز ایران را به عنوان یک کشور قدرتمند و با عزت می‌شناسند.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/454642" target="_blank">📅 22:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454641">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QX1UHeucfbS4XqZlIaS0y3vLWZOHyCjiLWu0t_dz1G5JYgdJvPodj3vqGJh-9kuOIIvBMh9eJ3cEul1y7GYWgJHWbJTXdg6yu03FWO2LmscKTSGgcUmGgKKJFSmydq5JALz5dnthFCkOIuy9Z2yN2fLyIVtY4gMABxS1UQcH0-pbiL6TuBlosUBKYVlzvtOdiRsvpdGAa3OH5HWMlKtlp2hBPu9Dyyilwn2jnIAHl1TrbMPqP0ZXSxILB0zb0EUzd7dtBviBkrGrnOobd-NBRLpwQ-PZGXiRDDn5H6hqEViAom0sUIZSUJkJLyKgW4xil6HupEGNPx8VboVAeCHY1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استاد بین‌الملل: کنوانسیون دریای خزر در خدمت منافع آمریکا، اروپا و اسرائیل است
🔹
احمد کاظمی استاد حقوق بین‌الملل، تصویب کنوانسیون رژیم حقوقی دریای کاسپین را یک امتیاز مستقیم راهبردی برای رژیم صهیونیستی دانست و گفت این کنوانسیون علاوه بر تأمین منافع راهبردی…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/454641" target="_blank">📅 21:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454640">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
سازمان تجارت دریایی انگلیس از وقوع حادثه برای یک نفتکش در فاصلۀ ۹۵ مایل از شهر عدن در غرب یمن خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/454640" target="_blank">📅 21:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454639">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انهدام باند قاچاق بیش از ۵ میلیون لیتر سوخت در بندرعباس
🔹
فرمانده مرزبانی فراجا: یک باند قاچاق سوخت که در یک سال گذشته در پوشش صیادی بیش از ۵ میلیون لیتر سوخت قاچاق کرده منهدم شد.
🔹
فرار مالیاتی، تقلب و قاچاق سوخت از جمله اتهامات اعضای این باند سازمان‌یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/454639" target="_blank">📅 21:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454638">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWo9lHGISoc7TFx-CP-eX9lGmwFXyb-RqdX8DfXyjr_LLt0UGS_lT04F6_oIC0B1bL0HLR3TCRKn-A-593kpOHD_dkNPZkQEfirm_EqXcifbU7_MHWDEwo1jM4cYMmhAEd4Eq7woOsTRsuUxLC8NL1pVAWC36WSx-XIkVD6Kgp5xek3tTxcOSOJ1Jo57BuTkka8Z_JOmInezgyEX1ILtqJ9S_XxPcBaBqO48gsabhgeJj8vmiH0P-s7oSJqLHhrWy1-1KA50NfV65p-4oxE7qma69wFXiagoEuiZG3M0BSQOgBC8i_fppbJ0LRS841jyVmQ4cOocu9kIO_xUa2CGjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سریال‌های تاریخی بزرگ تلویزیون در راه‌اند
🔹
تلویزیون این روزها تولید مجموعه‌های تاریخی را با جدیت دنبال می‌کند. از پروژه‌های عظیمی مانند «سلمان فارسی» و «موسی کلیم‌الله» گرفته تا سریال‌هایی مانند «رئیسعلی»، «حماسه زاگرس»، «دیوار دفاعی»، «کارآگاه علوی»، «شکیب عیار» و «نگین ارباب» که هرکدام به بخشی از تاریخ ایران و جهان اسلام می‌پردازند.
🔹
اگر این آثار بتوانند شخصیت‌های تاریخی را باورپذیر و جذاب روایت کنند، شاید بار دیگر شاهد تکرار موفقیت سریال‌های ماندگاری مانند «مختارنامه»، «امام علی(ع)» و «یوسف پیامبر(ع)» باشیم.
🔗
اگر دوست دارید در مورد این سریال‌ها بیشتر بدانید،
اینجا
را بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/454638" target="_blank">📅 21:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454637">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e6ae32867.mp4?token=CuVe3lc8eBL_2PDfqColy1nVW21wR8IcsboXtDV1obLlANs4yIYLFesq3zLxz6AWau4uj0IW408DBAgZVHbkIt9oWsDnZbGgpROB-4iePKdKpBGM62k--JX_DPNPbB_AQgdpaWqNSz3656Alccwl8Hc8CNn6uwJQUbC--7FHvy49i4FbHDN56C4z0ukRWJlRbdrZsXHKvFafk3mvg72kB06UTqE6WSXRWwGp-R9ds1c_lurJug0EuMFloYqsuyaHLNjYTzyFEGpcoH_etMxX-4UwF4jauT9glNUlZw2HO-y1JsamGs7Wc857mXVpvs0VJoviTD8d9djdkP3gR0iZww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e6ae32867.mp4?token=CuVe3lc8eBL_2PDfqColy1nVW21wR8IcsboXtDV1obLlANs4yIYLFesq3zLxz6AWau4uj0IW408DBAgZVHbkIt9oWsDnZbGgpROB-4iePKdKpBGM62k--JX_DPNPbB_AQgdpaWqNSz3656Alccwl8Hc8CNn6uwJQUbC--7FHvy49i4FbHDN56C4z0ukRWJlRbdrZsXHKvFafk3mvg72kB06UTqE6WSXRWwGp-R9ds1c_lurJug0EuMFloYqsuyaHLNjYTzyFEGpcoH_etMxX-4UwF4jauT9glNUlZw2HO-y1JsamGs7Wc857mXVpvs0VJoviTD8d9djdkP3gR0iZww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بی‌بی‌سی و اینترنشنال چگونه بین خود تقسیم نقش کرده‌اند؟
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/454637" target="_blank">📅 21:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454636">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3f36ea27e.mp4?token=CRLzcOGUDDFf3FVFdrgt6YT7JXYBg5GLhFlPpyKUaqjnfAqwvyOOE5q9kSF4ctAMO6RMq-0vW19E6ojDLCwY8vNhM5M8BzDSnutFkEtekSy5QgVfuY6Zb6zkyPoEIx8kwEOpGLI1_IfcqMtok1O6Naf3T__wi1gejOkUbE62zkaxvRhZKEqXWNuXlQs-tkM6UJGHOUCPmJupbfBP5Pu8oZHlbyrUDcbEoLdrhIpx9p9cEd3FY2tSvnpOnvL6rHww102XzQKzwvKUl82g1ugipzJtext5_V3Q1YJJdUlrH70PjbSfiWHugmb9FITfL1uZ9E0mkJeOI2eflmrw_XkHbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3f36ea27e.mp4?token=CRLzcOGUDDFf3FVFdrgt6YT7JXYBg5GLhFlPpyKUaqjnfAqwvyOOE5q9kSF4ctAMO6RMq-0vW19E6ojDLCwY8vNhM5M8BzDSnutFkEtekSy5QgVfuY6Zb6zkyPoEIx8kwEOpGLI1_IfcqMtok1O6Naf3T__wi1gejOkUbE62zkaxvRhZKEqXWNuXlQs-tkM6UJGHOUCPmJupbfBP5Pu8oZHlbyrUDcbEoLdrhIpx9p9cEd3FY2tSvnpOnvL6rHww102XzQKzwvKUl82g1ugipzJtext5_V3Q1YJJdUlrH70PjbSfiWHugmb9FITfL1uZ9E0mkJeOI2eflmrw_XkHbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشیمانی پویانفر از برخورد با شهید لاریجانی در اربعین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/454636" target="_blank">📅 21:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454635">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d32835d80d.mp4?token=n099wcwrqyrAfUbIYiGSGsVc7rZW-D5AH4bROA7hA7aFB_f34fsjnuDWiVnFhVm6TTWMtkSd176t2-AhLOPD1pUDjK4b1PrnUtiNMbMQQe5woPPN900enyeZZkEFVZpuO78hM49uwArELzL5_rYWnVqB_JDgHkx2p6Hv0Nwq_4fRrugyqqJzMRcgVGLz59hMsb0nWFFsp0JliBEQQ5cTE4JkDyCo4wD_xF7eJkGDB4XosU-G166h9_gtvgHiRxmfJh6vedQetCFq83jsl38qsjz6UO2KwUeIvxnlEFNCE3vo6o0opN-FHcC7T7Q89EiurWdPIryxWPRvhX4RiPqMIG7lLywTf3v_bLg28cBs0KsHAJ1j3rYiQd0cMnC-Ibu53B89vdcNydyVlZUffJSrE96UOZUbPYGEnL9zzACBP2oMFxN0KdBmGuuZ-UB50WTtwyaiRLwyo0q7fSYY3EzTDYq7NajVrOl7E5QrF88J8B6M89JpWfKUNoFWL4fiAaEkag7gvF5ZlKG1vDX3eM3yE8hkcyGPu3uie8l6vs3Ny6-yFS1MyeWQYpF1Dki7peAQi5qMBMhMdrdK-KyTlR92yugyFMuWqq_62WN9A9FVl2T8hfxGyE1PwrvLMDlL3oohSu8OchzJ09RMlqb4V2WkaBVbWNU25GXO4U2ha2_BhD0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d32835d80d.mp4?token=n099wcwrqyrAfUbIYiGSGsVc7rZW-D5AH4bROA7hA7aFB_f34fsjnuDWiVnFhVm6TTWMtkSd176t2-AhLOPD1pUDjK4b1PrnUtiNMbMQQe5woPPN900enyeZZkEFVZpuO78hM49uwArELzL5_rYWnVqB_JDgHkx2p6Hv0Nwq_4fRrugyqqJzMRcgVGLz59hMsb0nWFFsp0JliBEQQ5cTE4JkDyCo4wD_xF7eJkGDB4XosU-G166h9_gtvgHiRxmfJh6vedQetCFq83jsl38qsjz6UO2KwUeIvxnlEFNCE3vo6o0opN-FHcC7T7Q89EiurWdPIryxWPRvhX4RiPqMIG7lLywTf3v_bLg28cBs0KsHAJ1j3rYiQd0cMnC-Ibu53B89vdcNydyVlZUffJSrE96UOZUbPYGEnL9zzACBP2oMFxN0KdBmGuuZ-UB50WTtwyaiRLwyo0q7fSYY3EzTDYq7NajVrOl7E5QrF88J8B6M89JpWfKUNoFWL4fiAaEkag7gvF5ZlKG1vDX3eM3yE8hkcyGPu3uie8l6vs3Ny6-yFS1MyeWQYpF1Dki7peAQi5qMBMhMdrdK-KyTlR92yugyFMuWqq_62WN9A9FVl2T8hfxGyE1PwrvLMDlL3oohSu8OchzJ09RMlqb4V2WkaBVbWNU25GXO4U2ha2_BhD0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردمی که با تمام مشغله‌ها همچنان شب‌ها میدان‌داری می‌کنند
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/454635" target="_blank">📅 21:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454634">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بازداشت عامل ارسال تصاویر پرتاب موشک به رسانه‌های معاند در یزد
🔹
دادستان یزد: شخصی که با تصویربرداری از لحظات پرتاب موشک‌های ایرانی، این تصاویر را برای رسانه‌های معاند ازجمله ‌اینترنشنال و یک کانال معروف معاند ارسال کرده بود، در یزد بازداشت شد.
🔹
با توجه به ارتکاب این اقدام در شرایط جنگی، امکان تشدید مجازات تا ۳ درجه وجود دارد.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/454634" target="_blank">📅 20:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454633">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fi2xW7mK0Bf9HX6gi9zvVIC8cGHzOUlgEHKehM2_Tb7MLk7LOrscqJaRiScvnSAp68sUzLAbMQw-vtJUk6MtjCDXRLQqeMqZ-A2-U6AvpB91c4TUPtmeC5oz9ibW_VRGwZeksb7Nc9TbmFTyPTxGjPAIqtOWQcpB4ttCNjjIGMBuJc1b4floG4DaDuW8ZuwHPxGhIJIhOTRxBCgNAZ2RAZ92f1Wlq7BYqO296ZI4tznMhnutpV6NVH-UjLGBdFjozovadDrlvrG8uKtoJkXURugTd2F6snclcZi7-nU-VZU7M9w6sUN8zotK4RcOSkju-E_VJdu73VC5kGy7Cc0vxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رایزنی وزرای خارجۀ آمریکا و انگلیس درباره ایران
🔹
وزارت خارجۀ آمریکا اعلام کرد که روبیو امروز با میلیبند، وزیر خارجۀ جدید انگلیس درباره مسائل پیرامون ایران گفت‌وگو کرده است.
🔹
طبق گزارش وزارت خارجۀ آمریکا ۲ طرف در این گفتوگو بر تعهد مشترک به عبور ایمن از تنگۀ هرمز و تضمین دستیابی‌نیافتن ایران به سلاح هسته‌ای تاکید کرده‌اند.
@Farsna
-
LinK</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/454633" target="_blank">📅 20:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454632">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‌ غریب‌آبادی: موضوع دریافت هزینه توسط ایران در تنگه هرمز بستگی به تصمیم مقامات عالی نظام و رفتار آمریکا دارد. @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/454632" target="_blank">📅 20:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454631">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار در محدودۀ جنوب اصفهان
🔹
سپاه استان اصفهان: فردا از ساعت ۸ صبح تا ۱۴ احتمال شنیده‌شدن صدای انفجار کنترل شده در محدوده صفه، سپاهان شهر و اطراف آن وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/454631" target="_blank">📅 20:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454630">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‌ غریب‌آبادی: طرح جدید به‌گونه‌ای خواهد بود که هم در مسیر ورود و هم در بخش‌هایی از مسیر خروج، کشتی‌ها از آب‌های ایران عبور خواهند کرد. @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/454630" target="_blank">📅 20:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454629">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‌ غریب آبادی: با اجرای تفاهم جدید، مسیرهای موقت در  تنگه هرمز بسته خواهد شد
🔹
برابر این تفاهم، مسیر شمالی که در نزدیک جزیره لارک ایجاد شده بود و مسیر جنوب که در آب‌های داخلی عمان است، بسته خواهند شد. @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/454629" target="_blank">📅 20:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454628">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‌ غریب‌آبادی: مسیر جدید در تنگه هرمز موقت است اما می‌تواند ۲ تا ۴ ماه یا بیشتر معتبر باشد.  @Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/454628" target="_blank">📅 20:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454627">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">معاون حقوقی وزارت خارجه: دخالت خارجی در تنگۀ هرمز را به هیچ‌وجه نخواهیم پذیرفت
🔹
تفاهم دربارۀ تنگۀ هرمز باید صرفاً بین ایران و عمان انجام شود و ما برای هیچ کشور دیگری حقی قائل نیستیم. @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454627" target="_blank">📅 20:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454626">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">معاون حقوقی وزارت خارجه: دخالت خارجی در تنگۀ هرمز را به هیچ‌وجه نخواهیم پذیرفت
🔹
تفاهم دربارۀ تنگۀ هرمز باید صرفاً بین ایران و عمان انجام شود و ما برای هیچ کشور دیگری حقی قائل نیستیم.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/454626" target="_blank">📅 20:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454625">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/476b901163.mp4?token=JcaT26qGRv2V_ZJ5UwYu6g4NqgOt0clQOho3jFpTdBdc3bLewQNo2t8F661SSDNua3qpJeeMYjHGtosHURJmS7b_h2LCqkBCs_C7gNml7gu7MD4OwXwLmjGaZr9U106FF60JkZ5b0gdS3rz58VYRxnzuexKn9eImSFVL5ayK3qEPElTPMG_ZJiTs3C29frPpLlvaSg0jyAMJnwxB3uZL6xaCh_sXPXEcozXBD1WNpt92UIlegB4WeJtLM75D5YjfAwZaO-JBX2Tp26FrUMsCq8ZLsChjEjh3YCTbIFk-tRCXLh-e4PiYTvsLBIkscPpm2xQHw66p4ATb3q8I8QV9nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/476b901163.mp4?token=JcaT26qGRv2V_ZJ5UwYu6g4NqgOt0clQOho3jFpTdBdc3bLewQNo2t8F661SSDNua3qpJeeMYjHGtosHURJmS7b_h2LCqkBCs_C7gNml7gu7MD4OwXwLmjGaZr9U106FF60JkZ5b0gdS3rz58VYRxnzuexKn9eImSFVL5ayK3qEPElTPMG_ZJiTs3C29frPpLlvaSg0jyAMJnwxB3uZL6xaCh_sXPXEcozXBD1WNpt92UIlegB4WeJtLM75D5YjfAwZaO-JBX2Tp26FrUMsCq8ZLsChjEjh3YCTbIFk-tRCXLh-e4PiYTvsLBIkscPpm2xQHw66p4ATb3q8I8QV9nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده قرارگاه نجف اشرف سپاه: مرز سومار می‌تواند در سال‌های آینده پایانۀ اصلی تردد زائران شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/454625" target="_blank">📅 20:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454624">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-text">بحران عجیب کتاب‌های جعلی در آمازون
🔹
جین فریدمن، نویسنده و تحلیلگر صنعت نشر، به‌طور کاملاً اتفاقی متوجه شد چندین کتاب جدید به نام او در آمازون و گودریدز در حال فروش است؛ کتاب‌هایی که او هرگز ننوشته بود!
🔹
اما او تنها قربانی نبود؛ کشف کتاب‌های جعلی مشابه با نام «کارا سویشر»، خبرنگار سرشناس حوزه فناوری، نشان داد این کارخانه کتاب‌سازی دامنه قربانیان خود را گسترش داده است.
🔹
زمانی که فریدمن این کلاهبرداری را به آمازون گزارش داد، پاسخی دریافت کرد که مسیر این ماجرا را به یک بحران بزرگ‌تر تبدیل کرد.
اینجا
بخوانید
@FarsnaTech</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/454624" target="_blank">📅 20:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454623">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">لغو چند تحریم عراق ربطی به تفاهم ایران ندارد/ برخی شروط بازشدن تنگه هرمز
🔹
یک منبع نزدیک به تیم مذاکره‌کننده: برخلاف برخی گمانه‌زنی‌ها و تبلیغات رسانه‌ای، لغو تعداد معدودی تحریم از جانب خزانه‌داری آمریکا، مرتبط با تعاملات دولت عراق با واشنگتن است و ارتباطی به تفاهم‌نامۀ ایران-آمریکا ندارد.
🔹
آمریکا با نقض تفاهم‌نامۀ اسلام‌آباد، روال‌مندشدن ترافیک تنگه را بر هم زد و علاوه بر حملات نظامی و ایجاد حصر دریایی، با لغو معافیت‌های صادرات نفت و پتروشیمی، مانع از در دسترس قرار گرفتن پول‌های بلوکه‌شدۀ ایران شد و بازگشت شرایط، منوط به برپایی تدابیر ایرانی در تنگۀ هرمز و عمل واقعی و عینی آمریکا به تعهدات خود است.
🔹
این منبع آگاه تأکید کرد که درصورت نهایی‌شدن تفاهم ایران با عمان، بازگشایی تنگۀ هرمز مستلزم ترتیبات جداگانه‌ای است که شامل انجام تعهدات آمریکا هم می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/454623" target="_blank">📅 20:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454622">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKzwAnqZatM-X5bbYBpVE1oMLJWrsQEqRNoC0Q2r3Se91x2yV2O5xKH5ixVSlnHNnG_NmOtfRaweMMf1hEIN8ntG_onI4t23DZbMWBj_w0sAwRRKed1_05RDXkRxjyakh2ngFetFR4Gg3cCXb1x2er9b3bUN0SdXXk2yyqytjquAOkMzRUvPp52UXRzACR809hwRfnD-fw0aFp_Ivra9mYNhM9xLGMlqtUuATUWDXBzTaNH5Jy1gWR-OFmxkRfc28IR2J-sMzjEYLqOkbzwPHehp3rCwJzigpT3eTfhE1nRiLmteKB53p_U6URf8JQn84hYWTMAPy-43p8_uYYlK7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان تجارت دریایی انگلیس از وقوع حادثه برای یک نفتکش در فاصلۀ ۹۵ مایل از شهر عدن در غرب یمن خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/454622" target="_blank">📅 19:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454618">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hP5BA83PoEHB_ap_zzKXK2h6rPGOSCHipiEulBMdhjneirilahv1gBHbr6e3IoKHvdIgPbH2MVl5DQ9mob8O54gBIqUDOwndOp95vGvKgSFGGn3O_GJN9WOjTEMM3p4pCL_ERUBMriWW6_UX46JCCmoXV_rB1PsAdD7K6H0mPXA4vhIiGI9LrwzvgMM4WoK3UbhDXPAmf8hDvpkbGLjxTgNcXvH57R8tqWpwclk0Q2hob88b5iXraztY79cqXFaMD_RRywxW-iJ1FoD1vBZArbPGhCj7wCH6gT7zczEEodz5fk8lQ0fGd7EzmcIswwU6f9WF_ymWQEMSqXsOoCFuuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vSvGoHinRTB1_fJHCCQgCSXzcb7b2J7Fuy9UxLZLQfAwbacAYBNMlzqzgePDgcreHb1mT_C9kNzYl72k33ul0nlDhrofnjXGKQ9E1QdrPFZ29RShsE_HSexrJzfkp1gaqCAgfYOWg1LkTCt8-17qr8wh8u3U9XywJTV4Y-b6zB1-mj75xAI4JphoKf1MJqfODqIJjn2CYt3LcqIHITRx6JFb_0MG6s5GUGxDabZnOH5WapQRFrVDAyQk_2PvMoOInUfE8B25bZklAb65kY8soWRWNuhIVhuDGszwMJ__bnr4vUUfh0jV59GP_y2Ntya7C-IFvFWw5xwhYT9OFLWOtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcfSBhfkn6Hh1I3xnFTPWJzusrNSkLUU6jdMQg_YiiRDJzILNMQMa965wur8-c7cqcL1eM_0ozIYHrJDiPZhGMSOE9VtV6awFRSWwm2aPAEinbSUZciH-2q96pzWTgLuratnkdSG4Bmn6NmpsxYR86LEITClxN5DAjDweYXG0S34UF3gkxJHmOJk6XJXazV9jmTePQ8_Wd3C5uLmvGyYnstbiSOwIZBsxdRHldOnXjiXu3Kl_R2vCoWq5v-aIz5enpOBmozFn1FmAbMXKmAaE61Bvw5x6fZ6H-EVN0dX87AdNsrEcQBZCGXpCTsfAszzjKKtA3MMJ9n6jNAY6Ke9lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z4jX56c_sTUTXmHR-cqd9XAJfPCp0kZtIvTGva7XXGyliF6CptCE4MczwheU3X-KwiujnOmiHQ3e-nzMHkX6qGYgJ_JKLMzV-l6Oqrl2ynTgG5Lm18-vaw4sbCLDpc9HyAjttK70KYw2dGa68ULji7j0DpnDeNamiS8BBCKn9yCbXMY8cVUpJbbyK8CTc2GbEsn8NvgZ3PHDd0j2O0vqujtn8maMYhfZEF8XRSowTZrshDTvQ9oJmWz5Jrp-snbS5dLHbHnTlMfczJN3fv8eK2YGWP-FcZs7o3YBEvi1tICtDah10YT5UGiZe9hMTyVaZb4tjkcEvQkTM35XwYardg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازدید وزیر بهداشت از محل جنایت آمریکا در لامرد
🔹
ظفرقندی باحضور در شهرستان لامِرد فارس، از بیمارستان این شهرستان و محل اصابت موشک‌های امریکایی-صهیونی در مجموعه ورزشی مرد که منجر به شهادت ۲۱ نفر شد بازدید کرد.
عکس:
محسن نی‌دانی
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/454618" target="_blank">📅 19:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454616">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/to8QcT2skVWz037DMuC4OiBZAB1Bj99eYAfgwd30aUy__GrH7gZb0Zx1CVMchkAZCsPJwGzvQXR-oxmQ0ZKSwUo1hLpIl6n4b45bJMCtlTaNGGgcYydwckB5vfktNIwtO6Z2Ghp24HVkzMCtVAOmRpyIPpCm7t167thp3JDJT6ef-wIk1DKBXtVchNjEiNnTtcIbYrZrpqcCJZrK8r-6dxD8iMRkOfWaijzKpZoH0YKtY8FXtiHGpGUzottHXbrJ24Z5B5ydEGHSASkQvTsDKUWiZ5xsiYuFJJaa_DgQ3ebfPLHvcjIRnd91aqIcFhUY_ZgsXmrrV64SVX956woDNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه: برنامه‌ای برای سفر به پاکستان و قطر در پایان هفته نداریم  @Farsna - Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/454616" target="_blank">📅 18:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454615">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سخنگوی وزارت خارجه: برنامه‌ای برای سفر به پاکستان و قطر در پایان هفته نداریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/454615" target="_blank">📅 18:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454614">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1410fe62a.mp4?token=rYOUjHLVTpctQazveFFt1UlN5rBmkAp6BSHxz4AjNAW-GhEHndy3w8gxEzoq9e_3SAa1eLHjjviPZ8fP6BbYVBKzJ53KqJeACaOnuvy3mKdMGIFfdxGPCirseuNSV1dsKy8t3T9pU3TG33DmN39fNCLEXbv2UnkIn4VdzTv_IEYG38sa98FCsH0greSkWVVzXa5zZ0VRCzhbnSCldZuGeculnaNW26WnwtE4avRJOEkbXGM5wwMlVqt69J6kI4dFKnYLd5gok180DmZjYXQm-jwhq_HEKnemuUFMoV7FF_EyIhKhWLElq8_8ExhJEIlngpLZ-TbtNu_W1lecspKFZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1410fe62a.mp4?token=rYOUjHLVTpctQazveFFt1UlN5rBmkAp6BSHxz4AjNAW-GhEHndy3w8gxEzoq9e_3SAa1eLHjjviPZ8fP6BbYVBKzJ53KqJeACaOnuvy3mKdMGIFfdxGPCirseuNSV1dsKy8t3T9pU3TG33DmN39fNCLEXbv2UnkIn4VdzTv_IEYG38sa98FCsH0greSkWVVzXa5zZ0VRCzhbnSCldZuGeculnaNW26WnwtE4avRJOEkbXGM5wwMlVqt69J6kI4dFKnYLd5gok180DmZjYXQm-jwhq_HEKnemuUFMoV7FF_EyIhKhWLElq8_8ExhJEIlngpLZ-TbtNu_W1lecspKFZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیویورک‌تایمز از برنامۀ مخفیانۀ ایران برای فشار بر ترامپ می‌گوید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/454614" target="_blank">📅 18:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454613">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">قیمت جدید بنزین سوپر در بورس انرژی ۸۴,۶۰۰ تومان تعیین شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/454613" target="_blank">📅 18:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454612">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4np08KS3Z5eLW6NzCauyYjfphBCwNB0_R7BkIUGECa72i2f4arhQ7BDK1erznH7l9Y-3Crg6dtZjtccuCKX1XWFCGUEJ6mvnN8Cp7GkglIclHNjoZItt6QUQZ1RF1blZuEL0yV7V2pKGA8Gr4Bj5fzVrZ9kPi8Bzhhn0sjcGrH6aR-LLQN1Eu59_0gGa4I7G3wNv0Kvc_hKQIe_4JiP6P4bfbgVf4eX9U0vvAF3W1ASGPBIJbsUqW2pzFp6nVorbpEHRyQeE8C9xhyGgndilwBY5Fe2G5OFkv79sr7pTGGSVnOJUf7MwG20GscGCOe9Kfv7_sW4NhrigH2NNBsWqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالیشاه به سیرجان می‌رود
⚽️
کاپیتان سابق پرسپولیس که پس از ۱۳ سال حضور از این تیم جدا شد، فصل آینده فوتبال خود را در سیرجان دنبال خواهد کرد.
⚽️
مذاکرات میان عالیشاه و مسئولان گل‌گهر به نتیجه رسیده و طرفین بر سر جزئیات قرارداد به توافق رسیده‌اند.  @Farsna…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/454612" target="_blank">📅 18:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454611">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تحریم‌های ضدایرانی شرکت عراقی رفع شد
🔹
وزارت خزانه‌داری آمریکا تحریم شرکت هواپیمایی «فلای‌بغداد» و ۲ هواپیمای عراقی دیگر را لغو کرد.
🔸
براساس ادعای آمریکا این شرکت‌ها به‌دلیل ارتباط مدیران با ایران تحریم شده بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/454611" target="_blank">📅 18:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454610">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e740dea4f0.mp4?token=SRSJWIlrkbuyPsGhkMM1FRRuRt0Mh3t3LuvY5iadyRnedUaVE5mUJ0pgoee2UN0UENiJGvtapGype1rrTdlW1xOVSQ418bN5CL_jUgxOHQ0Z1ZwfHudLg0N80FDrMPsVglzzOmvPMYnL1lf8J3ILNUn0Y1_ZLcDhLFz1O4VP9_cQcrLoM-PiL0PtfWozO32g4N2sCrVhhhGQkjI85C7kE_VuMm2o4FGMXJsp1dMYcK4nuMhtEEoK28KiuHD635MFvwN3nnJXNgf0_SI8o5POLwDBinZYNITlHZe2gtSrD6VNkBrvVN2nwF34V17evcFZblELRLk-syADyUFxHubMGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e740dea4f0.mp4?token=SRSJWIlrkbuyPsGhkMM1FRRuRt0Mh3t3LuvY5iadyRnedUaVE5mUJ0pgoee2UN0UENiJGvtapGype1rrTdlW1xOVSQ418bN5CL_jUgxOHQ0Z1ZwfHudLg0N80FDrMPsVglzzOmvPMYnL1lf8J3ILNUn0Y1_ZLcDhLFz1O4VP9_cQcrLoM-PiL0PtfWozO32g4N2sCrVhhhGQkjI85C7kE_VuMm2o4FGMXJsp1dMYcK4nuMhtEEoK28KiuHD635MFvwN3nnJXNgf0_SI8o5POLwDBinZYNITlHZe2gtSrD6VNkBrvVN2nwF34V17evcFZblELRLk-syADyUFxHubMGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بالاخره نردبان هم تسلیم ربات‌های انسان‌نما شد
🔹
شرکت «فیگِر» ویدئویی از ربات انسان‌نمای «فیگِر ۰۳» منتشر کرده که نشان می‌دهد این ربات می‌تواند بدون دخالت انسانی و به‌صورت خودکار از نردبان بالا برود.
🔹
بالارفتن از نردبان یکی از چالش‌های پیچیده در رباتیک محسوب می‌شود، زیرا به هماهنگی دقیق دست و پا، حفظ تعادل و درک لحظه‌ای محیط نیاز دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/454610" target="_blank">📅 17:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454609">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4_6aZhJyvxinoRi278F-kH3wUjZZ1fChXXc4prw7HL9k-_GITyN2WtcxH4t8b_hfdK6y_u2NHaxj0tT_BGmwttIKx0_8NgRV8O74BjvzkNSmrS4kMGD9NdMOEDUNeIyQK8HD09i9uyXxjhbtxjdHbcUs8TgMiVmEpxfJVwtLrTt1v6iFaUtFfkWsj_FMUdXKt0t_ZE-5gFQHYK1eJXg8bI4EQIPKqSjgCjeQRDABZ7acmO6UybjUqmDsMUpy3-gOqWwT2U2ogJvp83gt5pX8wZ9aD_ZqTSQCKXy6Tj5fzfeHwFqxWS91a_cFLcZjGNjOT9Ac0In6Qfiy8V6516NXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاپیتان پرسپولیس از این تیم جدا شد
⚽️
با اعلام باشگاه پرسپولیس، امید عالیشاه کاپیتان چند فصل اخیر سرخ‌پوشان با توافقی دوجانبه از پرسپولیس جدا شد.
⚽️
همچنین میلاد سرلک هم به شکل توافقی از قرمزپوشان جدا شد و مجتبی فخریان هم به‌صورت قرضی به گل‌گهر پیوست. @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/454609" target="_blank">📅 17:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454608">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37f3cf356d.mp4?token=vgxYyypBH5-pGX1QFtbB7WGodOi2Pycbs4WSici8HfdFQC_2q3TvRQN8qN187ViVRIeNy_2a_PjtYk7PHMAyYk5g3PL0OQinhlLNnZaDSC_Gtoo6xW67VVFQHqWSKGNcVs0J0wrD4pukzxyVdO9obNqBfRpS2tKwalK62RJue6ZResbnIJwa449nsoVmR6xfkN0UgpM98Y4QqqGQRwn6sLkXq5PaywCmsKUIh1XJhRnNrBBtAzWwtJUv0T2qbj-79EYAXLLw1FhhKKfA2X7huGV2IoQXMrGtYLcDD0tHf8J_caSB9JiDB5cnmo3nMT_TtqWCsJpeSagkZ8tiiBeNxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37f3cf356d.mp4?token=vgxYyypBH5-pGX1QFtbB7WGodOi2Pycbs4WSici8HfdFQC_2q3TvRQN8qN187ViVRIeNy_2a_PjtYk7PHMAyYk5g3PL0OQinhlLNnZaDSC_Gtoo6xW67VVFQHqWSKGNcVs0J0wrD4pukzxyVdO9obNqBfRpS2tKwalK62RJue6ZResbnIJwa449nsoVmR6xfkN0UgpM98Y4QqqGQRwn6sLkXq5PaywCmsKUIh1XJhRnNrBBtAzWwtJUv0T2qbj-79EYAXLLw1FhhKKfA2X7huGV2IoQXMrGtYLcDD0tHf8J_caSB9JiDB5cnmo3nMT_TtqWCsJpeSagkZ8tiiBeNxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بزرگ‌ترین دردسر والدین برای ثبت‌نام در مدارس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454608" target="_blank">📅 17:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454607">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9Z_AYPcKIn4EAu3fwbX42SSAOyzYN4os-xSLyuaVCAMc2BH8aRw3z5-yxiLABiTtQMgZwPVVyqnxmo63fccB-9LFSqDEc5cle_N3NOKuIFEJtiCa36WhaxQkur6Nc9a4ZCnaKrHi82Ia5ppj2ErjNp5EkV5KHmhk5Pv7pKl-lMa6ww_BKCiTjvYEM9Zsr7wTXaJwk-jR4rcVauHENbmdFt4nOnh-YO6I8XvzXk4gi8WI_UmZptn8vtpf-uBwoyJ2LfV-nTFiuxtkEXbMcweDI5bGIe2hv5NV5s33NMFbPQ7JxfARade5zAZ6ZdTWf9be5L6TF7hhCYcQGMB1ZXjqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶۰ میلیون دلار پرید؛ نامزدهای ضداسرائیلی پیشتاز انتخابات آمریکا
🔹
با وجود هزینه‌های سنگین لابی اسرائیل در آمریکا موسوم به «ایپک»، این نامزدهای مسلمان با مواضع ضدصهیونیستی بودند که توانستند از رقبای خود در مرحلهٔ مقدماتی انتخابات کنگرهٔ آمریکا پیشی بگیرند و پیروز این رقابت شوند.
🔹
«کمیتهٔ روابط عمومی آمریکا-اسرائیل» که به‌اختصار با نام ایپک (AIPAC) از آن یاد می‌شود، میلیون‌ها دلار را برای شکست «عبدل السید»، نامزد مسلمان و ضداسرائیلی ایالت میشیگان، هزینه کرد، اما در نهایت  نتوانست مانع پیروزی این پزشک در مرحلهٔ مقدماتی انتخابات مجلس سنا شود.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/454607" target="_blank">📅 16:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454606">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qtkd7U_Cg_bbTXd5i9GUaAC7V4CVmPMHBVCeVTAHCu4bn4sD1qBhUNJmU7gUUpfoefmO1JOs7Cp4aem6uIwDPBLWA3FClm09GFh7LI49VlFaZvAXV48JmOQGSqVfFgYGpkErMONzfbr56wzZowP4hK_KnjNcZ6BtYSKQLhWEnCJcstZldeUzFVO1qKESyWGku1bw7eiFBzVfiW_B1W7XAtzW79CYlQ38S3EC_L6V4ANYMr-YW8CL9hJ6ybqVX9k7UdcLO4YZcl8aeRud6qJhg8jacRj8TUtCqVS9z5ZnSDRXBv8s8YNirkByybZOuJFNVVjwlfqS7GEUmnp0HZf9Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برق پرمصرف‌ها گران شد
🔹
درحالی‌که برخی مشترکان از افزایش محسوس هزینۀ برق در صورت حساب‌های تیرماه خبر می دهند، وزارت نیرو می‌گوید قیمت برق گران نشده و افزایش رقم قبوض ناشی از مصرف بالاتر از الگو است.
🔹
تعرفۀ برق فقط یک بار در سال و در اوایل اردیبهشت تغییر می‌کند و در روزهای اخیر هیچ تغییر قیمتی تازه‌ای در قبوض اعمال نشده است.
🔹
مقایسه صورت حساب‌های برق برخی مشترکان در تیر و خرداد امسال نشان می‌دهد هزینه مصرف برق سه تا چهار برابر گران‌شده یعنی اگر قبض برق مشترکی در خرداد ۱۰۰ هزار تومان بوده، در تیرماه به ۳۰۰ هزار تومان رسیده است.
🔹
معاون برق و انرژی وزارت نیرو می‌گوید اگر مصرف مشترک از الگوی تعیین شده بیشتر باشد، هزینۀ برق مشترک به صورت پلکانی و با ارقام بالاتر محاسبه می شود؛ اما مشترکانی که در محدوده الگوی مصرف قرار دارند، برق را با تعرفه یارانه‌ای دریافت می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454606" target="_blank">📅 16:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454605">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42a494b0e4.mp4?token=cfICsEhtx_AcXSXKjzFz-OLEwslmeCqOJxSskQFtijDQaHbFLTTLIB25d74AV7_VQy2UXYTlsscUgk_7Ia95_2uz-Xi2W3Yfgqlp0G5CvMfT9JLMM3HgOqZZyuQ3jV89TeW6SQu7hb67oY2tAQTLTip2dRwF3XFnbkID6cFu4b7SPGW9LWR-GirmJHfhwsnfnA_i93HqYOpHEAzsIIFdk0c-aBT_dg3LQfj8TS1oqGr4fQMu9zp6pZ6E22qXH8Ham5W2gYGaf7V12LTQyttBgFb_bO8eOjETNpn4Oi-fPsAnnblhBqDPLS7PbgKZg__Xg-xhHSCrxR07IUSOvJIymg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42a494b0e4.mp4?token=cfICsEhtx_AcXSXKjzFz-OLEwslmeCqOJxSskQFtijDQaHbFLTTLIB25d74AV7_VQy2UXYTlsscUgk_7Ia95_2uz-Xi2W3Yfgqlp0G5CvMfT9JLMM3HgOqZZyuQ3jV89TeW6SQu7hb67oY2tAQTLTip2dRwF3XFnbkID6cFu4b7SPGW9LWR-GirmJHfhwsnfnA_i93HqYOpHEAzsIIFdk0c-aBT_dg3LQfj8TS1oqGr4fQMu9zp6pZ6E22qXH8Ham5W2gYGaf7V12LTQyttBgFb_bO8eOjETNpn4Oi-fPsAnnblhBqDPLS7PbgKZg__Xg-xhHSCrxR07IUSOvJIymg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش حماس به زیاده‌خواهی نمایندۀ ترامپ در شورای صلح
🔸
ملادنوف رئیس شورای به اصطلاح صلح آمریکایی در دیدار با نتانیاهو مدعی شده بود که تا وقتی حماس به‌صورت کامل خلع سلاح نشود، نظامیان اشغالگر از نوار غزه خارج نمی‌شوند.
🔹
حماس نیز در واکنش به گزافه‌گویی وی اعلام…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/454605" target="_blank">📅 16:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454604">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">باد شدید و گردوخاک در راه تهران
🔹
هواشناسی استان تهران: از عصر پنجشنبه وزش باد نسبتاً شدید به‌ویژه در ارتفاعات و مناطق جنوبی و غربی استان، همراه با خیزش گردوخاک پیش‌بینی می‌شود.
🔹
همچنین دمای هوای تهران در روزهای پنجشنبه و جمعه بین ۳ تا ۴ درجه کاهش می‌یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/454604" target="_blank">📅 16:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454603">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2089c2005.mp4?token=O5E5GEIKHXqicguEIzYreP9XFqxuNPRKeLWLDgklmq7NGKLhbu7ekDnTmU3B1qVJrwh0aKYLsPS909Cz_q92Fxxbd0Qci_Gl43x7c4kztNEd8N7WqRb_JbmVR_Lzq1vMwUxMjuyjLJZmQy8BQP3ODlJij7taCs80l34Ju22Yhv46ZnAosEnEB6I72mV7ijISsYdfM7-W1BBnl-xiQ88fxLntpQjf2wSR--mj-Ghr09svcNvs5lcNT_iFtUrWdAvlquFISfYE-My2RkWXQrkn1QP6svOsqF8ZbLJ9tj0-9wR2UoNGp4n-sVM15JHg9FDXkY3iQsOXmH_KN8A82UIncw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2089c2005.mp4?token=O5E5GEIKHXqicguEIzYreP9XFqxuNPRKeLWLDgklmq7NGKLhbu7ekDnTmU3B1qVJrwh0aKYLsPS909Cz_q92Fxxbd0Qci_Gl43x7c4kztNEd8N7WqRb_JbmVR_Lzq1vMwUxMjuyjLJZmQy8BQP3ODlJij7taCs80l34Ju22Yhv46ZnAosEnEB6I72mV7ijISsYdfM7-W1BBnl-xiQ88fxLntpQjf2wSR--mj-Ghr09svcNvs5lcNT_iFtUrWdAvlquFISfYE-My2RkWXQrkn1QP6svOsqF8ZbLJ9tj0-9wR2UoNGp4n-sVM15JHg9FDXkY3iQsOXmH_KN8A82UIncw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سعدالله زارعی: خون‌خواهی، فلسفۀ اصلی اربعین است و ایستادگی و خون‌خواهی در برابر جنایت، بخشی از این تفکر است.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/454603" target="_blank">📅 15:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454602">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24adfd0c64.mp4?token=fum4PpW9dGC2yC6Ubqk0EfiO00R2ATfm1o_xqXMpkUyRgmrZlB07-htEac8hSBwTUiW2jmGDuU4f7aGUTmbMahsumT28motnxcOXPBh2PM8tqLy9pBFPZxw1N5oLBeaOgbO4jMpiaWvrukv_v6uqBEjQzzDkGmzaUY0R7RqwWwxuVpnDerq_4NSdvpn2VdZVHvjTUkzLyKdhiu8-KaXfwY55ZQdgKDvGT3q9BrvjBeRlC8_5DY7DW0yeGhdj-c7hEMF-aPOMEZN9C66BunApFA50Ruqh9Bxh04AxsdFS4DiG9Bn4meJpHccMTfp2vog4rUlNCBgG2s7dl3b-O_n5CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24adfd0c64.mp4?token=fum4PpW9dGC2yC6Ubqk0EfiO00R2ATfm1o_xqXMpkUyRgmrZlB07-htEac8hSBwTUiW2jmGDuU4f7aGUTmbMahsumT28motnxcOXPBh2PM8tqLy9pBFPZxw1N5oLBeaOgbO4jMpiaWvrukv_v6uqBEjQzzDkGmzaUY0R7RqwWwxuVpnDerq_4NSdvpn2VdZVHvjTUkzLyKdhiu8-KaXfwY55ZQdgKDvGT3q9BrvjBeRlC8_5DY7DW0yeGhdj-c7hEMF-aPOMEZN9C66BunApFA50Ruqh9Bxh04AxsdFS4DiG9Bn4meJpHccMTfp2vog4rUlNCBgG2s7dl3b-O_n5CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهمان ویژۀ پیاده‌روی امسال اربعین
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454602" target="_blank">📅 15:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454601">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777a24997c.mp4?token=gHtAVr9IsaTCHIl-UMfXJAhI17jiZtPICt4tkFMqvF1_b21oGuLb3Ubj68ARcGQu_098sfN4gQnajT2m0EpevXva6QRAn4FJjFlivJiKXG32I9LIfXt52_CKTjUvHDN0I7MnGRvGamZ2-7WmigyBf2OjcWvCvtK8WzTjxjcMkLoKaGMHNI8hGY57J7U_LP4CLTc2-fjE9BfsEX8TOV3T9vX_GYRPgqu1IjgyrIpAILJpLEe0QHb72QZZXLroIisSDKFT0tMEf5tTqUHR2B4VTLZ0DxgV1aQcjKKqCrRBzb-HIR-msiXFs-V-A9OWm6ArCyus4-Fz3LRp9GlKzoLqag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777a24997c.mp4?token=gHtAVr9IsaTCHIl-UMfXJAhI17jiZtPICt4tkFMqvF1_b21oGuLb3Ubj68ARcGQu_098sfN4gQnajT2m0EpevXva6QRAn4FJjFlivJiKXG32I9LIfXt52_CKTjUvHDN0I7MnGRvGamZ2-7WmigyBf2OjcWvCvtK8WzTjxjcMkLoKaGMHNI8hGY57J7U_LP4CLTc2-fjE9BfsEX8TOV3T9vX_GYRPgqu1IjgyrIpAILJpLEe0QHb72QZZXLroIisSDKFT0tMEf5tTqUHR2B4VTLZ0DxgV1aQcjKKqCrRBzb-HIR-msiXFs-V-A9OWm6ArCyus4-Fz3LRp9GlKzoLqag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صاعقه جان فوتبالیست تایلندی را گرفت
🔹
پلیس تایلند: سوفوان آوای دیروز پس از اصابت صاعقه به زمین ورزشگاه سانتی‌فاپ واقع در جنوب تایلند براثر شدت جراحات جان باخت.
🔹
۱۲ بازیکن دیگر نیز دچار مصدومیت و به بیمارستان منتقل شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/454601" target="_blank">📅 15:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454600">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
رژیم صهیونیستی در ادامهٔ تجاوزات خود منطقه مشاع المنصوری در جنوب لبنان را هدف حملات توپخانه‌ای قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454600" target="_blank">📅 15:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454599">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/viHcOBLQHUJlIvGxv04tF2o_w3oXPMEV6o6JR4GWDGQQlCrPS2Jk6b1HDa7s3MGjK-U8kHdc8gx1PC-aF39MGwVsd8HIEm3A9A1d_L3NZOeAhs7RMBYO3XDFcmhcLLb_txHNmVhjv9r3_M6gIqGnveBeqbzJw9aQkUqO6T9BJ5pliHeSYPp63uFtbhaoDg8J0HSDLdt8UAVYQsrzP9Oi82__Q6UHakR1U4VfBJejJtRFGJKsi1DvQEZPDxrUSDBqSygSMMny1g5lcRG95tmVyJaR4fjX_nEjIcK5RQjyXV8fyxeiOwO1ECSX6FYilIvwEWjJdczCFY_SjdOw5oQ-bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثه برای یک کشتی در نزدیکی یمن
🔹
سازمان تجارت دریایی انگلیس: یک کشتی در آب‌های نزدیک یمن مورد حمله یک شناور بدون سرنشین قرار گرفت.
🔹
خدمۀ کشتی نجات یافتند اما گزارش شده که کشتی غرق شده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/454599" target="_blank">📅 15:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454598">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/125d40ac9b.mp4?token=hKHddIAOxkY3XW1hJdPlYMDP28Onm8QM1Z4NIRHCZD-_KVfZGxI7uHhsMvDnvRjMbRhFQBwIueVNXQrVhIJYBSUmGFeK954OXT1KIY_IDz4KfcvV5OlJ_P0hMmY2bUrT2aqBXuiGUJm46Nyx8Jfd-4CryWi1wHzbQvf57QuTFQOm2QqI2g1xSgCTQ0qXhtxhcJk4g1v9cJxs3YeKHUaE3hHOAubN6dYhgTlJURIzuaAXspbTPD0B_XdGpCPdmAPHKJjtrakKOXX4ViLWpdbCLzW0HBMdYNNFWSL30DR4x6psmjQF7-fgdL2oZ_L03jbXR-MNMEx4-5-apLwmNORmqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/125d40ac9b.mp4?token=hKHddIAOxkY3XW1hJdPlYMDP28Onm8QM1Z4NIRHCZD-_KVfZGxI7uHhsMvDnvRjMbRhFQBwIueVNXQrVhIJYBSUmGFeK954OXT1KIY_IDz4KfcvV5OlJ_P0hMmY2bUrT2aqBXuiGUJm46Nyx8Jfd-4CryWi1wHzbQvf57QuTFQOm2QqI2g1xSgCTQ0qXhtxhcJk4g1v9cJxs3YeKHUaE3hHOAubN6dYhgTlJURIzuaAXspbTPD0B_XdGpCPdmAPHKJjtrakKOXX4ViLWpdbCLzW0HBMdYNNFWSL30DR4x6psmjQF7-fgdL2oZ_L03jbXR-MNMEx4-5-apLwmNORmqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلالی که ۲۰ بازیکن در تیم‌های فوتبال ایران دارد!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/454598" target="_blank">📅 15:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454597">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTcNdGUtCty_mkvRdy5e1ZaZlRQJU6fMcFEOKIF0qhVIfd02X5Q5XNcq9mlfeZ3oW9gOzg2AtF17u9jGoKoDi_ndcwacPMzmAtZCyD17FUqr0QcMWCCFmSTtlyFtcilOTJnzNKYe3Jtwww4WPAHhsM6YuXbbI3WDL6-DEEd58fAePeVfxJzSqeH7S3-bfkarNi6xNJhLgVf4N2sSI7HijUxJvDZlSMEfmJGAAlnWOnkfwoPVacTZEaVVZovdzymj0_cbw6RTOJkouGACto9-A3ZZLb4sQhmDFJNyccxeh3wITMp2UAaC8uxQc3mGj2eVirsaNfvsVf8Jz0a9NaX2GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«کچاد» با رشد ۲۶ درصدی درآمد، جایگاه خود را تثبیت کرد
🔹
شرکت معدنی و صنعتی چادرملو (کچاد) در گزارش فعالیت ماهانه منتهی به ۳۱ تیر ۱۴۰۵، تصویری از تداوم ثبات عملیاتی و رشد درآمدی خود ارائه کرده است، گزارشی که نشان می‌دهد این شرکت در چهار ماه نخست سال مالی، ضمن حفظ سطح تولید در بخش‌های مختلف زنجیره فولاد، توانسته از بهبود نرخ فروش محصولات نیز بهره‌مند شود.
@Farsna
_
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/454597" target="_blank">📅 15:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454596">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8GR2QS73xOfIkKczu3oQu9jKgrCmW7iE4fu8npbkPvxo2FHINwVLbtbGoV6RgxcMNMLZv9TUB_EH29FChDlX8iubUJWpyoe34SVcUF2jmrqh3mmqFdmW4cKo9Q3gCn8TAv7lFNG5t_6JzL1YkacssFB56BHbfxHW4KeTI7Av549XH8rlVoSYUIjcjqJ_7p4ixooyef-yylGGEn-TQ3f1Q2tbGlsM6j90a8vnIZLddm4tqgEQFb1B4LeLfCFlr4egt7ey--gGbHFZ9WZuyAZDFY6AuT8qGUBQyIyNmUpdC39_AX6PwwwP9InFU9BwDb2_PgNCHV2xZ9-mUAVqcHmuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
جهش بیش از ۳۳ برابری سود خالص بانک رفاه کارگران در بهار ۱۴۰۵
🔹️
بانک رفاه کارگران بر پایه جدیدترین اطلاعات و صورت‌های مالی منتشرشده در سامانه کدال، در بهار سال جاری با ثبت رشد خیره‌کننده ۳۳۷۱ درصدی سود خالص، عملکردی درخشان از خود به نمایش گذاشت.
🔹️
بر اساس صورت‌های مالی مذکور، سود خالص این بانک در سه ماهه نخست سال جاری به رقمی بالغ بر ۲۲ هزار میلیارد ریال رسیده است که در مقایسه با دوره مشابه سال گذشته (حدود ۶۵۱ میلیارد ریال)، جهشی ۳۳ برابری را نشان می‌دهد.
🔹️
براساس گزارش کدال، درآمدهای تسهیلات اعطایی بانک نیز در این دوره با رشد ۵۳ درصدی به بیش از ۱۷۵ هزار میلیارد ریال رسیده است که نشان‌دهنده ارتقای توان تخصیص منابع و حمایت از بخش‌های تولیدی و اقتصادی کشور است.
🔹️
این جهش عملیاتی در حوزه اعطای تسهیلات، بیش از هر چیز بیانگر تمرکز راهبردی بانک رفاه کارگران بر ایفای نقش اثربخش در اقتصاد کلان کشور است. هدایت منابع مالی به سمت پروژه‌های پیشران و واحدهای تولیدی، علاوه بر تزریق نقدینگی به رگ‌های صنعت، گامی عملی در جهت تثبیت و ایجاد فرصت‌های شغلی جدید محسوب می‌شود.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/454596" target="_blank">📅 15:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454595">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/454595" target="_blank">📅 15:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454594">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
زخمی‌شدن نظامیان صهیونیست در جنوب لبنان
🔹
رسانه‌های صهیونیستی از زخمی‌شدن چند نظامی صهیونیست در مجدل زون در جنوب لبنان پس‌از انفجار یک مین خبر دادند و اعلام کردند که نظامیان صهیونیست با بالگرد به بیمارستان‌ها انتقال یافتند. @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/454594" target="_blank">📅 15:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454593">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlvNaDqIHPVU4VMuTarQIao5P9ZmF2Fmp7HoNvsRnvaB9-Ytzu2VA5gBrtO0y-LwnSuYTjKSlgcSHLTHjTlBzxzxKkUNPRGNLXAZdu4EJPZn0sKBiyY4zKzUHmTnDlbfWDD3JKoKwl8XAlikkXzn3ET_X610-XLEBC6pOybpTS6RsOl1ZwvY2WFby9DKoVmXfkmeA97aCBdSUHrzBfFGBePfubG90Oan_pJizHxjXJ6hp-qrRa7UgslUrfAXD93jEguBhit-NUIhq_p1QccD5LyjRvKqxL7uMmiXr1L9W0YOeXKm1RqgL4gska_R392vhlLSDuUMlA46ZXrpnyfu1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامۀ امتحانات نهایی برگزارنشده پایۀ دوازدهم ۴ استان جنوبی
🔹
امتحانات نهایی برگزارنشده پایۀ دوازدهم استان‌های خوزستان، بوشهر، هرمزگان و سیستان‌وبلوچستان در روزهای ۱۵، ۱۷ و ۲۰ مردادماه برگزار می‌شود.
🔸
امتحانات نهایی پایه دوازدهم این استان‌ها که قرار بود از…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/454593" target="_blank">📅 15:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454592">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c214d9363c.mp4?token=A4s6NOB-JDFLqmgMWwj78yKP0FkqanatFta3V3-MvpOEAt8GGxgcBP-H9maNT9F-sKuabZ98nmEG5W2u2H6TPhc_MsccjNSYhpC43Fsp8D0KokEyPkSkjQYpH6diGY0hI8Ycq2PmRpKFrOkWV_LDM5-oi7QXB_hG1OmeKtBfGmR-e_ZeZUomtyI4piVsV7ohlx5g5V1L8SZ71Dye8wkhbTFoUBVPKANpskYF49NFDlX2GB6vKn3hSCqywvl8-umqyu_vgcWeqiV1sM9f8F4WB1uSDKbwQydl9-gyF_wiF0f45bRJhMyMzIYVNWlfoeso0dcP2McAOo6m9lluIvDuog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c214d9363c.mp4?token=A4s6NOB-JDFLqmgMWwj78yKP0FkqanatFta3V3-MvpOEAt8GGxgcBP-H9maNT9F-sKuabZ98nmEG5W2u2H6TPhc_MsccjNSYhpC43Fsp8D0KokEyPkSkjQYpH6diGY0hI8Ycq2PmRpKFrOkWV_LDM5-oi7QXB_hG1OmeKtBfGmR-e_ZeZUomtyI4piVsV7ohlx5g5V1L8SZ71Dye8wkhbTFoUBVPKANpskYF49NFDlX2GB6vKn3hSCqywvl8-umqyu_vgcWeqiV1sM9f8F4WB1uSDKbwQydl9-gyF_wiF0f45bRJhMyMzIYVNWlfoeso0dcP2McAOo6m9lluIvDuog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگۀ هرمز بنزین‌دزدی در انگلیس را باب کرد
🔹
بحران انرژی در اروپا ابعاد تازه‌ای پیدا کرده. داده‌های تازه منتشرشده در اسکای‌نیوز عربی نشان می‌دهد از روز آغاز تجاوز نظامی آمریکا و اسرائیل علیه ایران روزانه به‌طور میانگین نزدیک به ۲۰۰ هزار پوند بنزین و گازوئیل…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/454592" target="_blank">📅 14:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454591">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56430c1b36.mp4?token=ICMRaD9wnNCVtAVssHVbTHEz10ITi47FwIyGXWpVmgHIBLG_5dZK7iAZ2BuVGSBYb715y1do0BcRCaaFD0TE3Q8RrHk49Of8GebwYokTjHINBpEt17ZjzQjSob6E_ikewZnbO38lhCloZi0Ti0nOf4azgUpaFt8r1C-W8SSb8sUtS5S1kiN7_k9jyPynoHF5YZUniYBS3uX3gAjXald56a4QQvxjxCJQhlWU7IWg2mxiqvb2hsPty56ofbc-g5RNR5AZnGXqbLb8RSxtCx1ASZwQoV3ygZVUSkYl4Th-95BBqMbEOVfFM9lwCG6QvamF44tcxJxQ97YrUWCBsN7m1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56430c1b36.mp4?token=ICMRaD9wnNCVtAVssHVbTHEz10ITi47FwIyGXWpVmgHIBLG_5dZK7iAZ2BuVGSBYb715y1do0BcRCaaFD0TE3Q8RrHk49Of8GebwYokTjHINBpEt17ZjzQjSob6E_ikewZnbO38lhCloZi0Ti0nOf4azgUpaFt8r1C-W8SSb8sUtS5S1kiN7_k9jyPynoHF5YZUniYBS3uX3gAjXald56a4QQvxjxCJQhlWU7IWg2mxiqvb2hsPty56ofbc-g5RNR5AZnGXqbLb8RSxtCx1ASZwQoV3ygZVUSkYl4Th-95BBqMbEOVfFM9lwCG6QvamF44tcxJxQ97YrUWCBsN7m1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ستاد اربعین: از ۳ میلیون و ۳۵۰ هزار زائر، ۲ میلیون و ۸۰۰ هزار نفر به کشور بازگشته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/454591" target="_blank">📅 14:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454590">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5168ee4e.mp4?token=qlb1kRJBlWFUqqh66QufiWu5aoN8iJtHbX46KyFuoRuQk6KaAWxnTnzwFz2fudjzrmo31D1Syyw1GJVhMLxmhpePvQhi2_H3r0lRIWPQH6qMCzALv0St2YzNS_2LHjzY2ZFmLhUrz13icKRcrOHZJLFeEpz13UtDxrYea2-A5fsyjbZhohOYV1aKkQoOp2KslH_ehKRiCZg-24dyJd7isMJrmkWS7KWjFNoF01x76aOy5jgeFodlBp86m5F82di58zCc3CYmpGG_7-SWln2kK1vd1DFcfr2v7O5NKk6n-APXUMc1Kp2B7jbap1FthiyVa4Wz-Z3GIza3WpLRaM5Adg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5168ee4e.mp4?token=qlb1kRJBlWFUqqh66QufiWu5aoN8iJtHbX46KyFuoRuQk6KaAWxnTnzwFz2fudjzrmo31D1Syyw1GJVhMLxmhpePvQhi2_H3r0lRIWPQH6qMCzALv0St2YzNS_2LHjzY2ZFmLhUrz13icKRcrOHZJLFeEpz13UtDxrYea2-A5fsyjbZhohOYV1aKkQoOp2KslH_ehKRiCZg-24dyJd7isMJrmkWS7KWjFNoF01x76aOy5jgeFodlBp86m5F82di58zCc3CYmpGG_7-SWln2kK1vd1DFcfr2v7O5NKk6n-APXUMc1Kp2B7jbap1FthiyVa4Wz-Z3GIza3WpLRaM5Adg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصویری از پیکر شهید ۲ سالۀ جنایت آمریکا در قشم
🔹
سینا جعفری به‌همراه پدر و مادرش بامداد امروز در حملۀ آمریکای جنایتکار به قشم آسمانی شدند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454590" target="_blank">📅 14:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454589">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lj-PgG1sKLnOtokKiEGPVaqeOqQgnockz0hGQN3laA8dL728kfMoflXrDsA_4rk48vUfHtu6FLMh-9aalCoi36w4xleGCJvohAGQe_-hnqmH-wWdGSk-G2JRCyfddZTXKa1CJIWh4DXdimQFdKWsDpE2mxAybzeqhTQ5qAEgsbf6Qi_J88xosFvrQceyrGL_ggqwj9cBuwCxQis7GujKRvGNzIZvUrqiQnay2ykLgDwBiD-iCC-JcUqvpRDwxFlKhRwwmyIGeNzkJAyLb1CSY2TCKQOG7fvCbWk25F9y5I4fvmMRjBlSTjH0WxDc29BOZ7mvDdj61UQZi3FxcNuRRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کنترل هرمز و گسترش جنگ؛ اهرم‌هایی که ترامپ را به بن‌بست کشاند
🔹
«کنترل بر تنگه هرمز»، «گسترش جنگ به منطقه» و «تهدید علیه زیرساخت‌های انرژی منطقه» تنها چند نمونه از اهرم‌های فشاری است که ایران در اختیار دارد؛ اهرم‌هایی که به اذعان کارشناسان غربی، هزینه‌های جنگ را برای دونالد ترامپ به شدت بالا برده و او را در «یک بن‌بست» به دام انداخته است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/454589" target="_blank">📅 14:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454588">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
زخمی‌شدن نظامیان صهیونیست در جنوب لبنان
🔹
رسانه‌های صهیونیستی از زخمی‌شدن چند نظامی صهیونیست در مجدل زون در جنوب لبنان پس‌از انفجار یک مین خبر دادند و اعلام کردند که نظامیان صهیونیست با بالگرد به بیمارستان‌ها انتقال یافتند.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/454588" target="_blank">📅 13:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454587">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پزشکیان: از هر تصمیم رهبران فلسطینی در روند مذاکرات حمایت می‌کنیم
🔹
رئیس‌جمهور در گفت‌وگوی تلفنی با رئیس دفتر سیاسی جنبش حماس: ایران از هر تدبیر، ابتکار و تصمیمی که رهبران فلسطینی در روند مذاکرات اتخاذ کنند، حمایت خواهد کرد.
🔹
به‌رغم تجاوزات اخیر رژیم صهیونیستی و آمریکا علیه خاک ایران و شرایط منطقه، مسئلۀ فلسطین همچنان جایگاه محوری خود را در سیاست خارجی ایران حفظ کرده و از نگاه مسئولان، سیاستگذاران و رهبر ایران دور نمانده و همچنان مسئلۀ نخست جهان اسلام به‌شمار می‌رود.
🔹
خلیل الحیه: ایران توانسته معادلات جدیدی در منطقه ایجاد کند.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/454587" target="_blank">📅 13:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454586">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d70982dd.mp4?token=N40fnmFOIQCnx9xXVTsEiTXrWqu1G3rPMZA6cp34jWKh1B0vG4HgttLbJS6Bds-Id6k4LsMQcqP2SQ_LkrojLOVoypOiYgW3HE4uegXQ-9UlxMT0WwF45_kRdR3ru2mRBPzPdSWYqYncEKQYqN3wyK3qQh_H6vClYirU4RBBy7IvWbp0W2RQrS97_WdAJEHYI1XgT_P0gb97fRUTd81ycBdAtFOqkpENlAKvEXxlOfiC5GZk_G_k0akdN522Mcw4fUhG2V1i08b5hYFppDftCQGoeF09T4OrFnV5N_Bts3YxppTbvOOPnh--pJDXCOVWPMjaXrmnm6Q5hUf56YuE-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d70982dd.mp4?token=N40fnmFOIQCnx9xXVTsEiTXrWqu1G3rPMZA6cp34jWKh1B0vG4HgttLbJS6Bds-Id6k4LsMQcqP2SQ_LkrojLOVoypOiYgW3HE4uegXQ-9UlxMT0WwF45_kRdR3ru2mRBPzPdSWYqYncEKQYqN3wyK3qQh_H6vClYirU4RBBy7IvWbp0W2RQrS97_WdAJEHYI1XgT_P0gb97fRUTd81ycBdAtFOqkpENlAKvEXxlOfiC5GZk_G_k0akdN522Mcw4fUhG2V1i08b5hYFppDftCQGoeF09T4OrFnV5N_Bts3YxppTbvOOPnh--pJDXCOVWPMjaXrmnm6Q5hUf56YuE-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خادمان اربعین غمگین از اتمام فصل عاشقی
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/454586" target="_blank">📅 13:09 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
