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
<img src="https://cdn4.telesco.pe/file/SCNDJvpLe9ryw6ZYHRC0G8-arji2s-I_48XobwpVxRZzDzjW8RmIIHtsYH1CozwxvER-GNVtP5C9uUO4JUBoomHneXtD7ilh-UTw0nxwpXnav-YBn7xTtwxzCrbLAF8n_8FfDMhjrz7XmGGosLG8Z41KV4iEwIEhOd7zpb7SVlUxYZyCKJmhq2AhzW2go2Wc0Bhr1RieNNz24xL60wrxl8tjiq9BITvcpyJQQAjBsou88LF0ktPzN9k15lBtOxfCYNW65W7KqNSfI2m9F4j307IsOuId6p7r7celpO3Q1NPzbqrp6816p3jzWKUcR6aRkoMF8Opk_q7hdEhIWxeoqg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 939K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 17:28:51</div>
<hr>

<div class="tg-post" id="msg-135686">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
فوری/رویترز: حملات حوثی‌ها و ایران به عربستان، پاکستان را به شدت از تهران خشمگین کرده و ممکن است پاکستان به درگیری عربستان و یمن کشیده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/alonews/135686" target="_blank">📅 17:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135685">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSFxKgdYZWuaIZUM-kR_7trYjVAbrZ45OF1Elx2G7FT0iDQ-VosqwVy0YMrR5g4FmFc4TKsEnapdVVi-ZQW50leiwO8eAFulIixs4sahcNqH_Q1rKQxHJE1ap3HlkpY_rRbn8kOLViWwJtJBdvsUCCgtz4pjChpFLiJQC1NzsfgaIXiv1IxcWHmHzY99SMwDS_bov3vo3nbsmBWnm0YDGe3QoNQI9FF9ushUwJdUEPnv5hWDUGi7R7QqL-UGTZre1d26vZuJ54fDTLkv1DwEIONAgH1Hxo9aRTYhcaDZBQRoxwVYsiL8WoJJ0rqTv9KSRgY3L21LVS6A1XOwhYeM-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر دفاع اسرائیل کاتز:
اگر جمهوری اسلامی به اسرائیل موشک شلیک کند، ما با قدرت و بدون هیچ وابستگی یا شرایطی به آن ضربه خواهیم زد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/alonews/135685" target="_blank">📅 17:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135684">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0fb2383c1.mp4?token=GwUSfEQvfZsvrW-F9dslcGxF5P-CLfQs819WYKH47J9CVmqt2rFhnB-rM4vh0wvs5T53PCEI7II6yXNPphYqfQ46warSWYP6oKJJeO0C5OhP18J99V5nZIHvskLmQxyYn0WrufRFa9QdMuXAkRpXDm4E0vMBfY2YISkXu4IJxB3aaWPyB3Sp0LRsOetMZjR3DplCeRH4QaZ3N3EseDEleM1odJGHkIiEJxxXG9ciPtiV_Tgfoq-qHjD0M9d7sNDaXGR-Cffi_my617nAfzm8FpXNfHMOyxZK-TR4xCjq1-dxzHHmWLCTUpVQ-ZgvHY9tVcHaVs79HlBrA6_eNgagWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0fb2383c1.mp4?token=GwUSfEQvfZsvrW-F9dslcGxF5P-CLfQs819WYKH47J9CVmqt2rFhnB-rM4vh0wvs5T53PCEI7II6yXNPphYqfQ46warSWYP6oKJJeO0C5OhP18J99V5nZIHvskLmQxyYn0WrufRFa9QdMuXAkRpXDm4E0vMBfY2YISkXu4IJxB3aaWPyB3Sp0LRsOetMZjR3DplCeRH4QaZ3N3EseDEleM1odJGHkIiEJxxXG9ciPtiV_Tgfoq-qHjD0M9d7sNDaXGR-Cffi_my617nAfzm8FpXNfHMOyxZK-TR4xCjq1-dxzHHmWLCTUpVQ-ZgvHY9tVcHaVs79HlBrA6_eNgagWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله قلعه نویی به علی دایی
‼️
🔴
قلعه‌نویی درباره ساعت معروفش :
وقتی میام ساعت میندازم و کت‌شلوار می‌پوشم، شما باید بگی به به چه مربی خوش‌تیپی ولی شروع کردید به مسخره کردن!
🔴
حتما باید یقه باز بذارم و زنجیر طلا بندازم؟ (کنایه به علی دایی)
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/135684" target="_blank">📅 17:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135683">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9286ee216.mp4?token=BL3X-8-us9uToD8pHQqSyHDuLHr4rQ9qwi0AjZq5xZL7pEnBlOmKFLgTL6NKRSEb8O5EPUxg9UCGpCJ0FJga_PSp5q92sywkvEg_TXbFt1GEGkM70WfeLkX4JgtOFWP3JC9P89jEHtqx-3ViMY11kZDAGtAPcZbjvjBrQf7EtimdwEf3H7WnuwUfYkGrdMvBQ-kmX4uYJCrrVfGtSkrvyYV92EmFznieVBDgtheOhQa3A6ZtucUctL5BKaOLBQpB2r1_ii2mDuDzM3oaYRxynPTlkn79J2yrcGZTAZ2ekQCP0pZrD0ppIw_jiXLvSkdRY0UNHkjbEEBAJ3LuqhuVEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9286ee216.mp4?token=BL3X-8-us9uToD8pHQqSyHDuLHr4rQ9qwi0AjZq5xZL7pEnBlOmKFLgTL6NKRSEb8O5EPUxg9UCGpCJ0FJga_PSp5q92sywkvEg_TXbFt1GEGkM70WfeLkX4JgtOFWP3JC9P89jEHtqx-3ViMY11kZDAGtAPcZbjvjBrQf7EtimdwEf3H7WnuwUfYkGrdMvBQ-kmX4uYJCrrVfGtSkrvyYV92EmFznieVBDgtheOhQa3A6ZtucUctL5BKaOLBQpB2r1_ii2mDuDzM3oaYRxynPTlkn79J2yrcGZTAZ2ekQCP0pZrD0ppIw_jiXLvSkdRY0UNHkjbEEBAJ3LuqhuVEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اعلام کرد که یک پهپاد انتحاری لاکاس متعلق به ایالات متحده را در جنوب ایران سرنگون کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/135683" target="_blank">📅 17:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135682">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f376bb044e.mp4?token=crJ9-NnHXmt4xcrBvxVX8IjYfGNXFCzwpKjpMNuCkLz1j_xs6gqoBvczz-EGWnz-9XyIOR7Q4wtcWOozOD_28cM270AHdY5MwbfG65aT4ewwLLCv52tFlhPHZxaMmpz3_gvywlE9CkfiAbJr9XUAZaIoL3nFx8JaleDYknPEA7sYYdU9uuqFOZO5AsYPXJuLbZl9w9vnf1Z0G2jhxR7_mZ-IJXG9VYEQWA2Tr7Mo6z2OQQqPSJS7Ywfwi7KbmEMZp1ISKrJp0lIcIG9a0au-PktShsZstA2zo50euhHfHYHpK6Q6fwaYPWdefKMrUkVB_3EUA2fAt8L779IXJCO9VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f376bb044e.mp4?token=crJ9-NnHXmt4xcrBvxVX8IjYfGNXFCzwpKjpMNuCkLz1j_xs6gqoBvczz-EGWnz-9XyIOR7Q4wtcWOozOD_28cM270AHdY5MwbfG65aT4ewwLLCv52tFlhPHZxaMmpz3_gvywlE9CkfiAbJr9XUAZaIoL3nFx8JaleDYknPEA7sYYdU9uuqFOZO5AsYPXJuLbZl9w9vnf1Z0G2jhxR7_mZ-IJXG9VYEQWA2Tr7Mo6z2OQQqPSJS7Ywfwi7KbmEMZp1ISKrJp0lIcIG9a0au-PktShsZstA2zo50euhHfHYHpK6Q6fwaYPWdefKMrUkVB_3EUA2fAt8L779IXJCO9VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روایت عراقچی از لحظه اصابت موشک به بیت رهبری در ۹ اسفند: به آقای حجازی گفتم آقا اینجان، گفت نمی‌دانم
🔴
با آقای حجازی در بیت جلسه داشتم که ۳موشک اصابت کرد و از زیر آوار خودمان را بیرون کشیدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/135682" target="_blank">📅 17:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135681">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">علی خامنه‌ای رهبر پیشین جمهوری اسلامی، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/135681" target="_blank">📅 17:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135680">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
پرس‌تی‌وی: گزارش‌های غیررسمی حاکی از آن است که صدای انفجارها مجدداً در کویت شنیده شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/135680" target="_blank">📅 17:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135679">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b003e9e7d1.mp4?token=YlyLANyIEitWjZJkrYirQZDDgHYnVrqL6bC-5uopK3gMrfRhnKHr26UI-jozpZ9ldT2DEFCLPaGDrok4YENmgnp1mZqrBZJ8rOL2pHFfveu3bikrsAysq-M5NAMrohRkGUVkwz57FOZkfQjm7qisnHFaJpVGNz0nIpPrA2_1g42UD3ocoFApNIVmLUtbwKweCB0xh9KlILWDt3uZnKBemrD9N7Sw-MQN1bZyewAvbPGSnL_qoDHk-IjlozcIEjo9tCIjsSDeqUDe67MHlrrBCUbfoaW1J_lBQDK_AP1Ho_16FBKNxB2yH0R88Qe6AP7jP0HpYYyN9DshA1_NsjsTcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b003e9e7d1.mp4?token=YlyLANyIEitWjZJkrYirQZDDgHYnVrqL6bC-5uopK3gMrfRhnKHr26UI-jozpZ9ldT2DEFCLPaGDrok4YENmgnp1mZqrBZJ8rOL2pHFfveu3bikrsAysq-M5NAMrohRkGUVkwz57FOZkfQjm7qisnHFaJpVGNz0nIpPrA2_1g42UD3ocoFApNIVmLUtbwKweCB0xh9KlILWDt3uZnKBemrD9N7Sw-MQN1bZyewAvbPGSnL_qoDHk-IjlozcIEjo9tCIjsSDeqUDe67MHlrrBCUbfoaW1J_lBQDK_AP1Ho_16FBKNxB2yH0R88Qe6AP7jP0HpYYyN9DshA1_NsjsTcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از ایلات خروج یک زیردریایی موشک‌انداز ارتش اسرائیل (IDF) را نشان می دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/135679" target="_blank">📅 16:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135678">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری / چندین انفجار در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/135678" target="_blank">📅 16:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135677">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
فوری / گزارش ها از شنیده شدن صدای انفجار در بندر عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/135677" target="_blank">📅 16:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135676">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
منابع خبری محلی در جنوب لبنان از حملات نظامی جدید اسرائیل در مناطق مرزی خبر دادند.
🔴
ارتش اسرائیل دقایقی پیش اقدام به یک انفجار مهیب در اطراف شهرک «کفرتبنیت» واقع در جنوب لبنان کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/135676" target="_blank">📅 16:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135675">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ارتش: فردا قراره تو شرق تهران بمب های عمل نکرده رو منهدم کنیم پس اگه صدا اومد نگران نباشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/135675" target="_blank">📅 16:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135674">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‌
👈
پلیس راهور فراجا: تمام مسیرهای آسیب‌دیدهٔ هرمزگان بازگشایی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/135674" target="_blank">📅 16:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135673">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری / چندین انفجار در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/135673" target="_blank">📅 16:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135672">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ارتش اردن: 3 فروند موشک بالستیک ایران که به سمت جنوب شهر عقبه شلیک شده بود، در حالی که موشک چهارم به منطقه باز اصابت کرد، رهگیری شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/135672" target="_blank">📅 16:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135671">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
منابع عبری
: اسرائیل ممکن است در 24 تا 48 ساعت آینده،ارتباطات رادیویی خود را به دلیل تنش قریب‌الوقوع با ایران قطع کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/135671" target="_blank">📅 16:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135670">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cV9aJdJtkCw97rb4xt2e1DuDT3betRQ-m-2nK-KhjZ4rlj2Jw7DwcQCdmtcYDnY3dwaJZV9QTNCP-BfP6az0jIWAvReZGBTlBZm4O3p1dNZgASlq826mpisAwYYaq9LRTq9ymk5jSkrh8pl0nW_iucLriZRhMVey5DKwW6j3nxEZDOkNLsaux5jJgpyl3akBU6yZE3RTAG6A81Ex8Y6jSyjJNH7ATO3odlY4RUzAZomSGF1zuk8ZQSLU3s71L0V1l495FDkzgAemHQWx_byn8S8flO31HkdPb5cSm_7t8sDkqTKOY0dhmhSpMGGbp-xUlJfOIn_MGYUc0RZXcHk7mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منتسب به کرمانشاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/135670" target="_blank">📅 16:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135669">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
گزارش‌هایی از شلیک جدید از ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/135669" target="_blank">📅 16:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135668">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
گزارش انفجار در کرمانشاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/135668" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135667">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
معاون سیاسی سپاه : حمله به پایگاه‌های آمریکا تو اردن، کویت و عمان ادامه داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/135667" target="_blank">📅 16:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135666">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
فکت تاریخی
🔴
در طول تاریخ هیچ نیروی نظامی خارجی‌ای با دسته گل وارد یک کشور نشده.......
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/135666" target="_blank">📅 16:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135665">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KWfydc_B6-Tv_mAuPS8zdtiVxucVlkky0aB6yukiqJiy5Qff6K7U53qZ8yKRWGHj_m9igTvN8aPEhV2gM2Qve798Hm37Et7VL6w8XgReQS8Mid_IR6fmq2GprZeE7ELnuZiORO3hVsMtm7c0su5ULU8et_2l0_KMnQ5cQxeyk6DngwrYwyMDaDZN4vzq3nIUkyzaOYkkGcYXyvuO8GSCgK88wQRhFZYYWxBHCoR0itNLn3o6qPsslXYH1YYeZW34yEpTVTTZ2Qn7MCCbqMSWpOLPAzUGc5NpYpYMI28cIn7yylmspY6QEJEw6Za0MITLjKYoPOc-D0ZSsgR-Y8-EKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت آمریکا در امان، پایتخت اردن، هشدار داد که به دلیل «تهدید امنیتی موثق»، فرودگاه بین‌المللی عقبه و بندر دریایی اردن تخلیه شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/135665" target="_blank">📅 16:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135663">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
بر اساس گزارش الجزیره، موج شدید گرما و حملات مجدد نظامی ایالات متحده به ایران، باعث شده است که قطعی‌های برق که قبلاً پراکنده بودند، به یک پدیده روزانه در سراسر کشور تبدیل شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/135663" target="_blank">📅 16:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135662">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری / هم اکنون 14 هواپیمای سوخت رسان آمریکایی از اروپا به سمت اسرائیل اعزام شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/135662" target="_blank">📅 16:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135661">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فوری / هم اکنون 14 هواپیمای سوخت رسان آمریکایی از اروپا به سمت اسرائیل اعزام شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/135661" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135660">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
شبکه الجزیره به نقل از رسانه‌های اردنی: صدای چندین پهپاد در آسمان عقبه شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/135660" target="_blank">📅 16:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135659">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: سیستم‌های دفاعی آمریکایی دو موشک ایرانی را در منطقه العقبه رهگیری کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/135659" target="_blank">📅 16:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135658">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
رسانه عبری والا: نیروهای اسرائیلی با همکاری اردن موشک های ایرانی را که به سمت عقبه، اردن در حرکت بودند، رهگیری کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/135658" target="_blank">📅 16:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135657">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سازمان هواپیمایی کشوری، سقف نرخ بلیت پروازهای نجف و بغداد را ۱۲ و ۱۴ میلیون تومان اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/135657" target="_blank">📅 16:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135656">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
رسانه عبری: نیروهای اسرائیلی و اردنی موشک های ایرانی را که به سمت عقبه، اردن در حرکت بودند، رهگیری کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/135656" target="_blank">📅 16:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135654">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tipben8_qncuEwC3Bh3upnVz-ZfZGVkYSk8cZwwv16o7TB4JLsIad4THtxQLjA-Z56N9ko1dirVETr0oq9meMy4OVjOKfiEinRCm5id-_30PPZA-bA8KDc6TtQf3sEY45IhGpfGGFBxBTLb0fVzU2EseDq3Ga3YVZmqJ_1wesb_revDhqXAniTys8whrd1IyBzKvohlyt7K70j9YEJUymkBnTz5QnNwHwzL70OG0spdV3hIi5wTG5pXU8UhW8ucpJEGDtAIKxuNb7e6Rl2W-fJoP8dhOqJqYgZzmCKw2f1pH26ImUUBwzzXemfCCzoDPIEl7conp0B8aRyeKbWgJ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af3ea64d0.mp4?token=Y6TfdPb4ObZUck7ZvXmhr0X8IlJyfH7oEYnmKPtjnmQFAg-j059R8fb_HYNiPINANhXS-UNGm6Rgb9JYgj8L1Sr5CtiWr_jN5FHoUfxp245y4hUKckLOia4T5IMKU8xLPstV_sqSGDoz6WXy0NOvNPpMntLeIcPjHx5hoB9g_Ww_OhEMp7NeEmCyPdWQUp4WS9Wx-0MikO8VHvHSr4664g8tQKET0oHTMDfBLEFFZnh5_s3so0ahTCUKzlvbs9jw-6Ivysj2zMFaLA1pFr5EmUas73QDFWRP5ZaCzocdGnNOOLascYdMp0-Wisug7N_p42M-bNCik907FTe1vS8MHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af3ea64d0.mp4?token=Y6TfdPb4ObZUck7ZvXmhr0X8IlJyfH7oEYnmKPtjnmQFAg-j059R8fb_HYNiPINANhXS-UNGm6Rgb9JYgj8L1Sr5CtiWr_jN5FHoUfxp245y4hUKckLOia4T5IMKU8xLPstV_sqSGDoz6WXy0NOvNPpMntLeIcPjHx5hoB9g_Ww_OhEMp7NeEmCyPdWQUp4WS9Wx-0MikO8VHvHSr4664g8tQKET0oHTMDfBLEFFZnh5_s3so0ahTCUKzlvbs9jw-6Ivysj2zMFaLA1pFr5EmUas73QDFWRP5ZaCzocdGnNOOLascYdMp0-Wisug7N_p42M-bNCik907FTe1vS8MHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یکی از قطعات موشک در نزدیکی فرودگاه پادشاه حسین در شهر العقبه سقوط کرده است
🔴
تمامی موشک ها رهگیری و هیچ خسارتی وارد نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/135654" target="_blank">📅 16:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135653">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b870f451.mp4?token=S4XFKlUQW3LRsCkA9qh7S_cqHLrLsuY9U6Ib4u2GN_qOf1p3G-gvXyHftb2kWE2koMIfSs67yuw3yoNWMTWprtDcsfNEMTbMGGrtURFymNOO0i27bwLFSCmYlvX1kQbNI_0SB6xSrPV__Zn2JauQPhTkXMWb-mhwaUTyn692MkjiNfoEEHMphId7SV0HOAxdTJG9le9TX4z8klpM7FNvtt8rfVbJH4VT_kiP8UCSQ491D-r_esZsnVZVsvqGQsUGeYGERL-fndvwXvww4faxnpuoqs5tP3eppBfACfNIGlPmCVNCKQWpDL4kGcxam9ZhW_K4M27wyxt8zWw4cuSGl2ODZfXHEiQ2eaOrCzh0OqsyK2gL1jLEMFp8SsCUZyKbE-taxal-BNDC2A-AwitLTu3yq6yqFQPbMyCBLGzLUed38a-POjf-imaf2d7BtpoHsdbNpqNNc0tZohLGSf_x-V_w1Es322-k532e2g-90o_67l4YnFZFCfWyO-q9JK4wTxJZTk08101dT6_1JBBy9nNfjvNBHPVhqHp69j8Tz0CP1dvbNlVseeXny3VSvrX0o66bD5C7YaqsrbAOybpl4Pu-QKIJPv6P6XtMGBirYscQvdkeicuD-DlCxKgLa5jg-5TOds01D6SOsdoRMJ6gDhJB7QiY5za6-azsMmOOEqE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b870f451.mp4?token=S4XFKlUQW3LRsCkA9qh7S_cqHLrLsuY9U6Ib4u2GN_qOf1p3G-gvXyHftb2kWE2koMIfSs67yuw3yoNWMTWprtDcsfNEMTbMGGrtURFymNOO0i27bwLFSCmYlvX1kQbNI_0SB6xSrPV__Zn2JauQPhTkXMWb-mhwaUTyn692MkjiNfoEEHMphId7SV0HOAxdTJG9le9TX4z8klpM7FNvtt8rfVbJH4VT_kiP8UCSQ491D-r_esZsnVZVsvqGQsUGeYGERL-fndvwXvww4faxnpuoqs5tP3eppBfACfNIGlPmCVNCKQWpDL4kGcxam9ZhW_K4M27wyxt8zWw4cuSGl2ODZfXHEiQ2eaOrCzh0OqsyK2gL1jLEMFp8SsCUZyKbE-taxal-BNDC2A-AwitLTu3yq6yqFQPbMyCBLGzLUed38a-POjf-imaf2d7BtpoHsdbNpqNNc0tZohLGSf_x-V_w1Es322-k532e2g-90o_67l4YnFZFCfWyO-q9JK4wTxJZTk08101dT6_1JBBy9nNfjvNBHPVhqHp69j8Tz0CP1dvbNlVseeXny3VSvrX0o66bD5C7YaqsrbAOybpl4Pu-QKIJPv6P6XtMGBirYscQvdkeicuD-DlCxKgLa5jg-5TOds01D6SOsdoRMJ6gDhJB7QiY5za6-azsMmOOEqE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بهترین راه برای پیدا کردن شغل، راه‌اندازی کسب‌وکار و گرفتن پست‌های مهم مخصوصاً در صداوسیما، مجلس و نهادهای مختلف این است که از دیوار سفارتخانه‌ها بالا بروید، آنجا را آتش بزنید و غارت کنید، بعد هم نماز جماعت بخوانید!
🔴
بعد از آن، خیلی شیک و مجلسی تبدیل می‌شوید به «کارشناس مسائل بین‌الملل، جنگ، اقتصاد، سیاست خارجی و...» و در همه‌چیز هم صاحب‌نظر خواهید بود!
🤔
همین حروم زاده میدونین چند نفر از هم وطن های مارو تو 18، 19 دی کشته؟!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/135653" target="_blank">📅 16:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135651">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbG89J9B67dJedx3tBNbyj32dmkGR2Obznaknc0ym9wgwladcWGm-EF-bZO6_ywuzmm-MGNrvf9iSQNqG3zn7B4KanWfNvnR_a1ZQDw6Q8urr5rmQe2f1oZghud0ZN395kOplpacBUmIUAgtiatK1MfYbh5HrcoaCLXLJzbA-Hp-tRDBaXjZI0c2SYm1ilhabsadjxEKfvjBcB_7jchQ5FSWv8GdosizpI4NLXzNqDLEtel7ZjV_RiaxcdgdfKYfUh4R7OVEWoysXxYlrCBgjsb-Yo4zJ-RpVWhKE9FqksAap5XB9jwLYryWANn7RoKCp1dsIuYG8_EUrOX9FhOgiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af3ea64d0.mp4?token=uOpkGiiB9eZJIpZ2okSqT-AfjxlQfEsuE6JneAQdo6E5PZMkuyugfQcYlMcj6wzgU0wllJhiYaM9dYpBQEckRIUaOCpWf3i1GD9R54M8WqGNavztLmLzDRCMHCiFUb2Dua9OWKxiNKIbyQRYCql9_NPDYNABbjfjrvgeNuGWj4KIOkEXeLZsESvPZM_iWD4s3afgw5V-kPuitTJYrVwTOw65whKfkE2-lGeGZFr6RmUk8TUY8FZhsuoh09qa7q7vigeEs_fVp2U533qguMnafjgSpYjsRVUMmOyapqJepRUsHDk7GIv3jrNgceAXCITEqGBGzKGJoAqByQECTFpLSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af3ea64d0.mp4?token=uOpkGiiB9eZJIpZ2okSqT-AfjxlQfEsuE6JneAQdo6E5PZMkuyugfQcYlMcj6wzgU0wllJhiYaM9dYpBQEckRIUaOCpWf3i1GD9R54M8WqGNavztLmLzDRCMHCiFUb2Dua9OWKxiNKIbyQRYCql9_NPDYNABbjfjrvgeNuGWj4KIOkEXeLZsESvPZM_iWD4s3afgw5V-kPuitTJYrVwTOw65whKfkE2-lGeGZFr6RmUk8TUY8FZhsuoh09qa7q7vigeEs_fVp2U533qguMnafjgSpYjsRVUMmOyapqJepRUsHDk7GIv3jrNgceAXCITEqGBGzKGJoAqByQECTFpLSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یکی از قطعات موشک در نزدیکی فرودگاه پادشاه حسین در شهر العقبه سقوط کرده است
🔴
تمامی موشک ها رهگیری و هیچ خسارتی وارد نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/135651" target="_blank">📅 16:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135650">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXdheagiSERloasmagT4Aupw2Wnd_77XkxnHgfdvSGCI1E2U1QP2ZoMis-MwnrdBTiJ-TD-ZVfVPStEUvIY5w_1kdNgLzlmsIbmKyhxLFVJ-Ce28d1APKDIrwzrzaT7e5A07ajVVc6grULi3OjNMvnW2BGirpYHfFsYPH9tMoAZHPZgiCFcJ0g4S0EhtbvvupxQ1aRzeGPsrbNpNHf9UmSWhF6J7zdj7LsC26rTtJ4ca57CmusjyMA7nR7ddBxd6GjcJTHRHmBbqq1SMias6JDF_y0V06kxdgobRoBH2JUeO_2eDqRriFSKYWJBm1j-U6EOeiuzf_ZUXQ6rwHTnv_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک پرواز از دبی به تل‌آویو به دلیل شلیک‌ها به سمت اردن، مدتی در هوا معلق ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/135650" target="_blank">📅 16:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135649">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
رسانه‌های عبری: حمله ایران به عقبه، به عنوان یک هشدار به اسرائیل طراحی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/135649" target="_blank">📅 16:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135648">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424131ea7c.mp4?token=YU64nrLOYJ_KFNEOXkzG-Ikwyyrh7URst1FF8kwk5UU_VajOmuJXSUhfHW_ZuM0TExAomtoCd2ax9Ov5pUjWfLSzYeKA6kK6r5Dqw6Ajrs-ah_ulkHNzAuWhGUg7GI-5zVchvxCkMUIOlvWMU3kz0h9nIvtGHKPioHrYlzD6-KEmqma1EJh2aX9tHZrKLD1ggaflvc0TQtvnn9DWF72YntbLpaaMljlUkOSBwWDuEyK_mO-LgWjdrp0ZRAV1oovFz8PdGWEkKQTFHCxb56vcnEluGDl7yS_LWmccDaWtryw7L-ZeL8UTAXBGnnlFDPhauIQqDiZRHSs-1tcoHkh4jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424131ea7c.mp4?token=YU64nrLOYJ_KFNEOXkzG-Ikwyyrh7URst1FF8kwk5UU_VajOmuJXSUhfHW_ZuM0TExAomtoCd2ax9Ov5pUjWfLSzYeKA6kK6r5Dqw6Ajrs-ah_ulkHNzAuWhGUg7GI-5zVchvxCkMUIOlvWMU3kz0h9nIvtGHKPioHrYlzD6-KEmqma1EJh2aX9tHZrKLD1ggaflvc0TQtvnn9DWF72YntbLpaaMljlUkOSBwWDuEyK_mO-LgWjdrp0ZRAV1oovFz8PdGWEkKQTFHCxb56vcnEluGDl7yS_LWmccDaWtryw7L-ZeL8UTAXBGnnlFDPhauIQqDiZRHSs-1tcoHkh4jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ستون‌های دود از فرودگاه ملک حسین در عقبه اردن به هوا برخاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/135648" target="_blank">📅 16:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135647">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ستون‌های دود از فرودگاه ملک حسین در عقبه اردن به هوا برخاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/135647" target="_blank">📅 16:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135646">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
آژیر ها در اردن دوباره فعال شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/135646" target="_blank">📅 15:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135645">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3252ff46ed.mp4?token=pQ2Npud-DGHx0VjtgAoq2eSrOE8YvxRiCB0Yyk8b4sscA99JWx6Fe7yPa08VTXJOyr4j0m6byvvGFTE7Bo-LHHr2gFlHZyGMZ49XJDTelFnQ3COVqrENRhJPQdb-FDs5FQ7jexXUCQR_Jw48gVlLLgnA9HHqXwp6vgVrv67Wg0ScdU1rKmJKNPEi6uwZRVboMjjifUvUNVnADS8izuyWC8cANVF4bDaLDM1-A4o6Jb6XsI3JxoM7bw32mknCwVPklV8dxTDE_gu58tWDy5JsWTYIMVf5qb5GPHZmosp0o8JTxei5jpsaYAeIAtxwGmKjnGtE1MR7EYf29H3ETfdQEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3252ff46ed.mp4?token=pQ2Npud-DGHx0VjtgAoq2eSrOE8YvxRiCB0Yyk8b4sscA99JWx6Fe7yPa08VTXJOyr4j0m6byvvGFTE7Bo-LHHr2gFlHZyGMZ49XJDTelFnQ3COVqrENRhJPQdb-FDs5FQ7jexXUCQR_Jw48gVlLLgnA9HHqXwp6vgVrv67Wg0ScdU1rKmJKNPEi6uwZRVboMjjifUvUNVnADS8izuyWC8cANVF4bDaLDM1-A4o6Jb6XsI3JxoM7bw32mknCwVPklV8dxTDE_gu58tWDy5JsWTYIMVf5qb5GPHZmosp0o8JTxei5jpsaYAeIAtxwGmKjnGtE1MR7EYf29H3ETfdQEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقوط بقایای موشک در اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/135645" target="_blank">📅 15:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135644">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
گزارش‌ها از اصابت موشک به فرودگاه عقبه در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/135644" target="_blank">📅 15:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135643">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07aff8569.mp4?token=RxZKhZ8EjTXHs-4KpZbIhk4X-aWSTDqHA07RWAzVfmb9MTfxftJwkKJoc1yvnOE8DyqC3-3ijnfpeJYBp8Q8Ii_ktZuk4qvu5NAYj38I8uogbSipUavs3Cl3UzzVu41SgQIFENWSrSF8O9_aU6FtYC3cD_kOrEmcoMFsnaTcKTqs3PK5kSrt8DdY1MyeJkcoC5p42SqpsBI55KtNHexyslWtk4N0BYnFpo5OdTi8fmSERHj9vsP7R5bZNvdzS94mgRXOanYjRvzfOKpCPLPcGDK27EUTa8odRbCDk7F72zTjAj51Vkr8MzoyOQIs_vrxc_nDrh3aErFECmq2rMglcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07aff8569.mp4?token=RxZKhZ8EjTXHs-4KpZbIhk4X-aWSTDqHA07RWAzVfmb9MTfxftJwkKJoc1yvnOE8DyqC3-3ijnfpeJYBp8Q8Ii_ktZuk4qvu5NAYj38I8uogbSipUavs3Cl3UzzVu41SgQIFENWSrSF8O9_aU6FtYC3cD_kOrEmcoMFsnaTcKTqs3PK5kSrt8DdY1MyeJkcoC5p42SqpsBI55KtNHexyslWtk4N0BYnFpo5OdTi8fmSERHj9vsP7R5bZNvdzS94mgRXOanYjRvzfOKpCPLPcGDK27EUTa8odRbCDk7F72zTjAj51Vkr8MzoyOQIs_vrxc_nDrh3aErFECmq2rMglcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجارها در آسمان ایلات و العقبه
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/135643" target="_blank">📅 15:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135642">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ارتش اسرائیل: پس از شلیک موشک از ایران به سمت عقبه در اردن، خشونت می‌تواند به اسرائیل سرایت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/135642" target="_blank">📅 15:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135641">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
پروازها و فرود هواپیماها در فرودگاه رامون، واقع در شمال ایلات، پس از حمله ایران متوقف شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/135641" target="_blank">📅 15:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135640">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANQbL3BGuz6nMwVttAZp_D7ul8JxQi4uJNBosDKXlGT1oG2CzhvgPta9A-EKSqBWGNt1-0mQ7zBDj8o4YmKA4T0hKhNTeZPdIEBGwBvDyX4JT_ASoQd5Pab7aEan9I8MfsvEAf6XYMd6R7-DHHOpAcpIEAIXgUkS7A7fFE8dRMXMzzzf3Hb9aRuplLLfvG1SRNtpmeC6XUK-rJGLcFlTSvxjNSujnHs2W8YLbfCrp7MMaVyzNuzdFDokZAtZd3yQ7-2DxRlprk2_gP_ojROnLtdZCxIEst5isA3jc_op5N8Tr-cjeCP2_mNLeR5uu7u1UMAs8U9CiFxyLdHwR2fSUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چندین انفجار در آسمان ایلات اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/135640" target="_blank">📅 15:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135639">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوری /  ارتش اسرائیل: چند لحظه پیش، ارتش اسرائیل پرتاب موشک‌هایی را از ایران به سمت شهر عقبه در اردن، که مجاور اسرائیل است، شناسایی کرد.
🔴
احتمال وجود دارد که در نتیجه این حملات، خساراتی به اراضی اسرائیل نیز وارد شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/135639" target="_blank">📅 15:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135638">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فوری /  ارتش اسرائیل: چند لحظه پیش، ارتش اسرائیل پرتاب موشک‌هایی را از ایران به سمت شهر عقبه در اردن، که مجاور اسرائیل است، شناسایی کرد.
🔴
احتمال وجود دارد که در نتیجه این حملات، خساراتی به اراضی اسرائیل نیز وارد شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/135638" target="_blank">📅 15:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135637">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbecfb6571.mp4?token=mo7tsqKIzqdw2q76qBXE3ZrEwAhl5SJTZPN1YnCZNlrajXq_DPvcyr8xW4xhCFqvxaz6ULoZxlG7QfkVsLBnP7kOEAoBUxGCVJ-LxVhsdKYIvIh4O7OuUkO5HBLYEgo5PUOXJx7nf4sa6oL2WfWHwgnYZS2FSgHe-tG6G5lVg1QyORwylpu7k6k2SieceOt4oiHW7W9O89W2D9XOcutykD31V4pXcAKrwXUDXuznXqYrm_VXShLHiYL3lQUXIM0lkQg92AjzuWYbRkvzzts7_EhY8i7P_BhLFfUjyjtx-_XaJfO794fBQ_-yBiMKfcaHT2mRKrVLREgiPeEF4n0xwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbecfb6571.mp4?token=mo7tsqKIzqdw2q76qBXE3ZrEwAhl5SJTZPN1YnCZNlrajXq_DPvcyr8xW4xhCFqvxaz6ULoZxlG7QfkVsLBnP7kOEAoBUxGCVJ-LxVhsdKYIvIh4O7OuUkO5HBLYEgo5PUOXJx7nf4sa6oL2WfWHwgnYZS2FSgHe-tG6G5lVg1QyORwylpu7k6k2SieceOt4oiHW7W9O89W2D9XOcutykD31V4pXcAKrwXUDXuznXqYrm_VXShLHiYL3lQUXIM0lkQg92AjzuWYbRkvzzts7_EhY8i7P_BhLFfUjyjtx-_XaJfO794fBQ_-yBiMKfcaHT2mRKrVLREgiPeEF4n0xwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدای آژیرها در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/135637" target="_blank">📅 15:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135636">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
منابع محلی از به صدا درآمدن آژیرهای هشدار در نقاط مختلف اردن خبر دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/135636" target="_blank">📅 15:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135635">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1c6f5985e.mp4?token=LvRRVZ-3XF4kRdz598SJXX_ndo04Pj-0a-2TniMpmfXwyetVZMaU5EiIj3aCO6-uRXLQqlDxlgbSGUSl5_Ax8EuKAv96eYF8pdIIfRbh20pMSR0oDPv869_iDQET14JQhFvmYG2Kkuo0gY16SWBPG6xBMECP4dM_U9INKDJlljmDjGnqNYIZdOfo8LcVTq61ogoU8UShTzHBnzQayBLG1jJUOI3uQ398ilMPp24jZMiWX4SUoKwsB2gfyE8MB2QMgEdmUuQaTIJvL8xBaGrWTGzXamEJT7uVYbGCY12k8aQfNtB-3G_i5oaYNHqZqfImb7c_QlM5mhLDwd_tBdkntA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1c6f5985e.mp4?token=LvRRVZ-3XF4kRdz598SJXX_ndo04Pj-0a-2TniMpmfXwyetVZMaU5EiIj3aCO6-uRXLQqlDxlgbSGUSl5_Ax8EuKAv96eYF8pdIIfRbh20pMSR0oDPv869_iDQET14JQhFvmYG2Kkuo0gY16SWBPG6xBMECP4dM_U9INKDJlljmDjGnqNYIZdOfo8LcVTq61ogoU8UShTzHBnzQayBLG1jJUOI3uQ398ilMPp24jZMiWX4SUoKwsB2gfyE8MB2QMgEdmUuQaTIJvL8xBaGrWTGzXamEJT7uVYbGCY12k8aQfNtB-3G_i5oaYNHqZqfImb7c_QlM5mhLDwd_tBdkntA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک میدان نفتی در کویت دچار آتش‌سوزی گسترده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/135635" target="_blank">📅 15:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135634">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
فوری / ترامپ : جمهوری‌خواهان باید ایران رو هم به لایحه تحریم روسیه اضافه کنن
🔴
این همون کاریه که لیندیسی می‌خواست انجام بده و قرار بود اتفاق بیفته، خیلی مهمه!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/135634" target="_blank">📅 15:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135633">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSbN_0aFBQgsVpxtBHE4_bQph5-S4J229oPPm6WVZNvGMJvssPpvNSi5meN6G_mz28NpY6tEq5oGRJTcpqFBUTqptog_-eq3C9QQ38Wbfc6hAaiR6iuLfJ3jV0avCtZPo8JhtcMjNE8miMKmMo1AKee1OpOnV0H7bfXReaZjys0AquIAoaxkTze45dn3CY4xTNUxJtLj6F9gF9iPNvaMRAYC6iVm6xVL05xfShucP4mdM-dF9IoDM77Unyr-DynuozUTYBEfgcSh7pRVCCP8no8LbnjOVPeyGbx7l3vWjfqBUk9MFL1UwEx4KbG0Pe0fASz5Gdjyye8clAHwV6xVrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مهاجری: آقای عراقچی، شجاعانه و بدون ترس مسئله تنگه را از طریق دیپلماسی دنبال کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/135633" target="_blank">📅 15:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135632">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
آکسیوس: آماده‌باش هوایی آمریکا برای تشدید جنگ با ایران آغاز شده است
🔴
آمریکا تعداد سوخت‌رسان‌های خود را به سطح مشابه آغاز جنگ خواهد رساند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/135632" target="_blank">📅 15:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135631">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
اسکندر مومنی، وزیر کشور ایران، فردا به پاکستان می‌ره
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/135631" target="_blank">📅 15:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135630">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
اکونومیست گزارش داد کشورهای اروپایی عضو ناتو همزمان با کاهش حمایت‌های آمریکا، برای تقویت توانمندی‌های دفاعی و نظامی خود به تکاپو افتاده‌اند تا وابستگی کمتری به واشنگتن داشته باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/135630" target="_blank">📅 15:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135629">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
وقتی کشور به مدت 47 سال با ایدولوژی پوسیده دینی پیش میره و کشته شدنش رو رحمت میدونه انتظار چیزی غیر از شرایط فعلی رو نمیشه داشت.
🔴
هیچ استبدادی پابرجا نمونده و مردم ایران هم به پیروزی که حقشونه میرسن و رنگ آرامش رو میبینن.
🤔
تاریخ نشون داده چه با نیروی خارجی چه بدون اون دیکتاتوری سقوط میکنه. مردم تصمیمشون رو گرفتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/135629" target="_blank">📅 15:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135628">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
کویت: دومین حمله در دو روز گذشته به نیروگاه تولید برق و نمکزدایی آب
🔴
وقوع آتش‌سوزی در تأسیسات نیروگاه برق بر اثر حمله و آسیب دیدن واحدهای تولید برق
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/135628" target="_blank">📅 15:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135627">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
عراقچی: به ویتکاف گفتم تا حالا شده در جلسه‌ای شرکت کنی که هر لحظه امکان بمبارانش وجود دارد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/135627" target="_blank">📅 15:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135626">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24603a935a.mp4?token=KmrOyY7o8kNagPB1SOLgwMLr5zuphdHU3gszOyfoonXjVsw99XQtBv-bqbV2YQ2qqbWf4tYVbgEHIn37W2pB5HLM9ZJFcvbgUUTVA2VIg_YoLCExrwHamGeDmGSb4IQzSpfXazECxCTmopkxPk1JY2MX7_rIka9xzlantxgHf-tDxxuA_8Ybp0RugtSTmOh4SWNRRdjQY5_wOCZ7RYg9-A2-JJyYWgAq1OaqwPXAW5IvVY2CU7uVXI1C3Y7ijIKUh9Y_TB2j11qDI88XPxuSD1EMlQh3juN00SHS1qEeOcxSeXnRvzf9GB85IogsZ5FOQpwIDx4WmTKOsXvdy0Pvw2hSQMKAIvm-4dJcT6XlcuxzsUImB5p_XDd9Rr-sRg3WmDKlBmIUNtl0BKl_3AG2Si0g6f1Bi_E8aV8ZhVnv7djX1jRubcIhP7wD7KT49HWLQbktJNZKYiHT0HWiGyv_AjC5JqgLQEB9CziBmlW66kJ3F69lcm3RNzmBWE7OySsTquFNWFU5VXlx6xilB3PoIYdgg3-cf74O1F5BfJ7_dX04KUxg8XsWxLAb9QnXjgm6-cufVytQ5-D_SMyuzwEi4hVEQzd5RAblzRWHhfCyWTRFKmv06tQ0beOWvEZTOPo-aBlv8CEcbF-sjrOvTqUKq3hQolNi4rNjBDQS_t6x6dU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24603a935a.mp4?token=KmrOyY7o8kNagPB1SOLgwMLr5zuphdHU3gszOyfoonXjVsw99XQtBv-bqbV2YQ2qqbWf4tYVbgEHIn37W2pB5HLM9ZJFcvbgUUTVA2VIg_YoLCExrwHamGeDmGSb4IQzSpfXazECxCTmopkxPk1JY2MX7_rIka9xzlantxgHf-tDxxuA_8Ybp0RugtSTmOh4SWNRRdjQY5_wOCZ7RYg9-A2-JJyYWgAq1OaqwPXAW5IvVY2CU7uVXI1C3Y7ijIKUh9Y_TB2j11qDI88XPxuSD1EMlQh3juN00SHS1qEeOcxSeXnRvzf9GB85IogsZ5FOQpwIDx4WmTKOsXvdy0Pvw2hSQMKAIvm-4dJcT6XlcuxzsUImB5p_XDd9Rr-sRg3WmDKlBmIUNtl0BKl_3AG2Si0g6f1Bi_E8aV8ZhVnv7djX1jRubcIhP7wD7KT49HWLQbktJNZKYiHT0HWiGyv_AjC5JqgLQEB9CziBmlW66kJ3F69lcm3RNzmBWE7OySsTquFNWFU5VXlx6xilB3PoIYdgg3-cf74O1F5BfJ7_dX04KUxg8XsWxLAb9QnXjgm6-cufVytQ5-D_SMyuzwEi4hVEQzd5RAblzRWHhfCyWTRFKmv06tQ0beOWvEZTOPo-aBlv8CEcbF-sjrOvTqUKq3hQolNi4rNjBDQS_t6x6dU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش امیر رولکس به تصویر ساعتش در جام جهانی
🔴
اگر یک سرمربی ساعت می بندد و لباس خوب می پوشد که اشکالی ندارد.
🔴
اگر من زنجیر طلا می انداختم و یقه پیراهنم را باز می گذاشتم آدم خوبی بودم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/135626" target="_blank">📅 15:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135625">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
دولت کویت : یک ایستگاه برق و تأسیسات آب‌شیرین‌کن، برای دومین بار در دو روز گذشته هدف حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/135625" target="_blank">📅 15:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135624">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90e70968e8.mp4?token=fVbc7HHtpWi89IbM0ogDJugaBJIZlDTUTyVEODKvB0skUvELeApokBUFjBVTYO7JDLi2xjrGAlkGZB5SBjBHoF0uu9I-SS2KeahCxphjA0iTKXP_Igs88uyVuxov_1ViTbivesGMgFDncqdc88W-Ujt4NdnhzenKHnjcrxIOivx5op89mMlEc4tt2aDYEyEalj8nReAJoeqmv3XJysCLicPSdXxj2a9PBb64AAA3XYvP7bd4hYF2dUTnU1M__dpcBaQUmn5COmJlpDvuC_rjW9aZt_CO16MzaP8XEWI7OTXADtMo0O8e-QCrUQGu0X2naW-jN5k-cQ7uS4wR8modtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90e70968e8.mp4?token=fVbc7HHtpWi89IbM0ogDJugaBJIZlDTUTyVEODKvB0skUvELeApokBUFjBVTYO7JDLi2xjrGAlkGZB5SBjBHoF0uu9I-SS2KeahCxphjA0iTKXP_Igs88uyVuxov_1ViTbivesGMgFDncqdc88W-Ujt4NdnhzenKHnjcrxIOivx5op89mMlEc4tt2aDYEyEalj8nReAJoeqmv3XJysCLicPSdXxj2a9PBb64AAA3XYvP7bd4hYF2dUTnU1M__dpcBaQUmn5COmJlpDvuC_rjW9aZt_CO16MzaP8XEWI7OTXADtMo0O8e-QCrUQGu0X2naW-jN5k-cQ7uS4wR8modtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سفیر ایران تو روسیه: درحال حاضر آمریکاییا هوایی به ما حمله میکنن و فرار میکنن، اگر اونا زمینی بیان این خوب و بجاست چون اون موقع جنگ ما زمینی و مردونه میشه.
🔴
ما تو جنگ زمینی غیور هستیم.
🔴
مجری: اینطور که من برداشت کردم شما از جنگ زمینی استقبال میکنید درسته؟
🔴
سفیر ایران: جواب ما به اونا اینه که اگه میخواید وارد بشید مشکلی نیست، ما قطعا مثل مرد با شما میجنگیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/135624" target="_blank">📅 14:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135623">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
دولت کویت : یک ایستگاه برق و تأسیسات آب‌شیرین‌کن، برای دومین بار در دو روز گذشته هدف حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/135623" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135622">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
المیادین : وزیر کشور ایران فردا برای سفری یک‌روزه به پاکستان سفر خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/135622" target="_blank">📅 14:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135621">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
عراقچی: آمریکا به رهبران منطقه گفته بود یک ماه تحمل کنید کار ایران تمام است
🔴
رهبران منطقه باور کرده بودند یک ماهه کار ایران تمام است!
🔴
یکی از رهبران منطقه تهدید به حمله نظامی به ایران کرد؛ من به او هشدار دادم که اگر بزنی مستقیماً با شما وارد جنگ خواهیم شد؛ و تا آخر جنگ آن کشور عربی را بمباران کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/135621" target="_blank">📅 14:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135620">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e9ca8564.mp4?token=Z4d6Nie9Xk4xIrghnP2t7YPvbhQoTgZDVYpHoM9_16Abkkn2e5tvTVKCh_37U8GnrdoeYonf8rSnKrVBG_SPRCSzrhPjVylw9SFzZw88ZKWDwZGMHCYQH3PW34AqQLUH3muA2Xc1X_dtBqjzAYKjfc-DOi_1X8nalfMzPzj05JQtSgZFB0EETIP0zSScgotZr6CkxFhXTxRQCeM4ng1Gb-W-L5lVDjepcwyfhZ1knTECNw01EGh6nb3zVnT1hRy93R7JUL6JEPsVlLk3n-E1eMT2UZbpIGO3_Yp96G7r6YA8KuNJL8SBB0SX2dIHZrZbAHLjB54HTb_Q9n8ZNG2MrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e9ca8564.mp4?token=Z4d6Nie9Xk4xIrghnP2t7YPvbhQoTgZDVYpHoM9_16Abkkn2e5tvTVKCh_37U8GnrdoeYonf8rSnKrVBG_SPRCSzrhPjVylw9SFzZw88ZKWDwZGMHCYQH3PW34AqQLUH3muA2Xc1X_dtBqjzAYKjfc-DOi_1X8nalfMzPzj05JQtSgZFB0EETIP0zSScgotZr6CkxFhXTxRQCeM4ng1Gb-W-L5lVDjepcwyfhZ1knTECNw01EGh6nb3zVnT1hRy93R7JUL6JEPsVlLk3n-E1eMT2UZbpIGO3_Yp96G7r6YA8KuNJL8SBB0SX2dIHZrZbAHLjB54HTb_Q9n8ZNG2MrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی: هیچ تغییری در آرمان‌های انقلاب ایجاد نشد و جهان هم داره ترامپ رو سر این موضوع مسخره میکنه و حتی بهش میگن جنگی که شروع کردی باعث شد تنگه هرمز هم بسته بشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/135620" target="_blank">📅 14:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135619">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
المیادین به نقل از منابع آگاه:
وزیر کشور ایران فردا برای سفری یک‌روزه به پاکستان سفر خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/135619" target="_blank">📅 14:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135618">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bC5aTyQ33YAARHVLdyk8Mzt-poPcjekw06agsBFNwyzB0AEHgMLji59uJSS4zylbecuahgx8pZ9gdIVjoDsLqmz5NLKHiUcK2YpP-cGs26QJ0fzI2WkGmfNwW5CHHyDGRbiQWsZbUltBWcucJAJbjw7L-ya1gpQuIjEFK-LKcbHjtyd_Swmlg8TxSXrQU5bCXqFQQd6ytw6Ky3LxOVsEk4sWDlxDBxnPrEOOJx-wG4xzgI-E5YMg3cbJRw1AySOND89EnImDbHbO9poi8PUOYL64WZf5q91jT_5BSYV9hnOd1MI7jV1RiL6dNu3mXAlVGFN12uyJUtEGf5n1dhgaVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
پیام لیونل مسی در اینستاگرام: زیباترین چیز در تمام این سال‌ها، صرفا عنوان‌ها نبود بلکه کل سفر، اشتراک گذاری جزئیات روزانه با این گروه، رقابت با هم، برخاستن در لحظات سخت و لذت بردن از هر گام بود.
🔺
از تمام هم‌تیمی‌ها، کادر فنی و تمام افرادی که روزانه برای حفظ این تیم ملی به عنوان یک خانواده تلاش می‌کنند، سپاسگزارم.
🔻
هر چه فردا اتفاق بیفتد، این گروه قبلاً تاریخی را نوشته است که هرگز فراموش نخواهیم کرد و هیچ‌کس نمی‌تواند آن را پاک کند. به پیش، آرژانتین!
@AloSport</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/135618" target="_blank">📅 14:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135617">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5555334dc4.mp4?token=nyzQ4FqGf853HpGPvqUOFYXPfDiMlbzaGK8D3tg5WbsmYy1r4sMEeeRR5bUMCUvRDKTLBpY_CHnbU6Wr9l60bar48uEnj2aJJs4J1PRD9dYnNYZq-FpIZKGLrmVCnElkbFxfcShlqO8Ude62RQCVHVp4wNE21Sj4nlUn8MGXjeqvkXTDfnfGZB6EFq2tAi3q-zH0KiA6tBd3nCevbRFg6DZ0ri_Q7p1p73H9MkbzBOcXkUiQN4DlcMV4uCmXkyqUqP1hJcZ1cI7ShmFC6VD387poCBKVrRphMhh4sZXiUqkd5q2CUhQM4y2p3AHYP1hb_pV8qvWEywzMKmLMfP4NDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5555334dc4.mp4?token=nyzQ4FqGf853HpGPvqUOFYXPfDiMlbzaGK8D3tg5WbsmYy1r4sMEeeRR5bUMCUvRDKTLBpY_CHnbU6Wr9l60bar48uEnj2aJJs4J1PRD9dYnNYZq-FpIZKGLrmVCnElkbFxfcShlqO8Ude62RQCVHVp4wNE21Sj4nlUn8MGXjeqvkXTDfnfGZB6EFq2tAi3q-zH0KiA6tBd3nCevbRFg6DZ0ri_Q7p1p73H9MkbzBOcXkUiQN4DlcMV4uCmXkyqUqP1hJcZ1cI7ShmFC6VD387poCBKVrRphMhh4sZXiUqkd5q2CUhQM4y2p3AHYP1hb_pV8qvWEywzMKmLMfP4NDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سرباز آمریکایی خطاب به مردم ایران
🔴
اگه حمله هوایی آمریکا تبدیل به حمله زمینی شد، خیلی مواظب باشید و از سربازان آمریکایی فاصله بگیرید.
🔴
چون سپاه قصد داره نیروهاش رو با لباس مبدل، شبیه مردم عادی، وارد شهرها کنه و از این طریق هم به ارتش آمریکا و هم به خود مردم حمله کنه.
🤔
چیزی که تو 18، 19 دی هم دیدیم. نیروهای حکومت در نقش معترض قاطی جمعیت بودن و مردم رو به گلوله بستن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/135617" target="_blank">📅 14:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135616">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
عراقچی: وظیفه تحلیل جنگ یا آتش بس بر عهده شورای عالی امنیت ملی است اما تصمیم گیری نهایی را سید مجتبی خامنه‌ای انجام می دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/135616" target="_blank">📅 14:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135615">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cac25a379.mp4?token=n3eEf5XrO9O3l5T7rc1C6-RctqirHcX_vxlkdpsL3wHJWKn6iPSyiq5HlD5gqSvxyLNQz7-5ILgYpU4fTdOm4xLCXBOKq5WKjF8XkHE6x-XFm-TnH-Fjtlse4a8X1GnONCMG8TrCY19h_rrEPFpNW44EeK64JG3jzo5SoykvJZglObROLbK3VAIpG9WnrkTK8_LmhSnjft2pwyPZw5clk8aIftQPnqKEHrB-rswpZYQR28HPSbw4HQDn9eOO1aiMvlTVDDtARg1SD8KLsr6cCHlF-d6NLWrDkFgXVeXGPiloGtoy2siuuztbNEZ3xli51cVBzp10hralQkDccEQ8Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cac25a379.mp4?token=n3eEf5XrO9O3l5T7rc1C6-RctqirHcX_vxlkdpsL3wHJWKn6iPSyiq5HlD5gqSvxyLNQz7-5ILgYpU4fTdOm4xLCXBOKq5WKjF8XkHE6x-XFm-TnH-Fjtlse4a8X1GnONCMG8TrCY19h_rrEPFpNW44EeK64JG3jzo5SoykvJZglObROLbK3VAIpG9WnrkTK8_LmhSnjft2pwyPZw5clk8aIftQPnqKEHrB-rswpZYQR28HPSbw4HQDn9eOO1aiMvlTVDDtARg1SD8KLsr6cCHlF-d6NLWrDkFgXVeXGPiloGtoy2siuuztbNEZ3xli51cVBzp10hralQkDccEQ8Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شاهکار رو از بیرانوند ببینین
بعد متن اون استوری که در مورد اسطوره فوتبال ایران علی آقا دایی ،گذاشته رو دوباره بخونین
خودتون حساب کار دستتون میاد که چه آدم دوزاری هستش.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/135615" target="_blank">📅 14:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135614">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
سفارت آمریکا در اردن: مقامات پادشاهی اردن، فرودگاه بین‌المللی و بندر دریایی عقبه را به دلیل یک تهدید مشخص و معتبر تخلیه کرده‌اند.
🔴
ما به شدت به همه شهروندان آمریکایی توصیه می‌کنیم که از سفر به فرودگاه یا بندر دریایی خودداری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/135614" target="_blank">📅 14:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135613">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVlIfWLDgg_ZfFim1h2qf3AjHhMYu7NrG-51r6J9RSwS7pkcVO9rehH4A9N8D1IcmVZXVC8njWZH1LzzfwCuptMZ3f3e-URGDZVbv-N8VXKZHieLOcRvIhPY0fjFW9P9YNl8zh1_-be77Z82DvRcm2A8NNME3EP6Dj2r-bH0PVPLuEXYH09hRkgbo2y1D4ja4xmZwrHxR7_Pe8VQa_lKBoBWpmm0tJPICbphO8hxieHWJRyuzx-rnUuT9dQCi03QXteakauItg0eZF19FqCTwYNKSlt20a5FkZmal2Fg4WawYuFd35jsmcOV-n8rYkx5BF9Fq4gPZZa793ecjtoUKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل، با توجه به برنامه‌ریزی برای یک راهپیمایی شهرک‌نشینان به سمت غزه، منطقه نظامی "نِقاب غربی" را به عنوان منطقه ممنوعه اعلام کرده است. این ممنوعیت از ساعت 8:00 امروز، 19 جولای، تا ساعت 8:00 فردا، 20 جولای، اعمال خواهد شد.
🔴
این محدودیت در حالی اعمال می‌شود که برگزارکنندگان "راهپیمایی به سمت غزه" اعلام کرده‌اند: "شهرک‌سازی، امنیت است؛ شهرک‌سازی، پیروزی است."
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/135613" target="_blank">📅 14:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135612">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TF9XjPrej1aeYxrgiBhf-_YohuBvjoG67d8G6_Itxk3vhnNaXPNThsLt1ZdYsgxO3N6OPSgdFvp2EFYLE2ZLHGblANMJWTBKEEfk4uMJ97jIqJ2hSiJ85FDwTTKOWPZeyh6RgApjE-HJP-2X1bRC2PST38WEQpdAWa2EmIztqxn38NELBksey6AzLpxNRyVioBFtYgqAYN4CLz1RF9cQeIkOzn4d4qGuKaUYKCCQOWnF4PkSzJz54qgqSbWLlejR6Ejj7F9cHnmsvyErobkzo86kqsoiFBvcAQ0DW3hjIMaEfZxRuTbzEXz0ujXNzwOPeDrFeuCWZ54S7devllr_jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر جدید ماهواره‌ای با وضوح بالا نشان می‌دهند که یک بمب‌افکن استراتژیک Tu-95MS متعلق به روسیه در پایگاه هوایی انگلس-2 در نتیجه حمله پهپادی اوکراین در تاریخ ۱۶ جولای، که پیش از این توسط رئیس‌جمهور زلنسکی اعلام شده بود، منهدم شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/135612" target="_blank">📅 14:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135611">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7Vy6KWPb5ps90qZZKwcUSXXKQf327jxFyCx3jlxMIpHyusb7lLEA2PVQ834zoGnNx8GVQYQ6oBYvAVPtvqeHgIo0bQHH4TAmyaoPDshC2u9dzlC8Dv9rZ_fR787VIanqlAqIy3CnzL3fm8U0_6mO-jSKGFIPm_4JLmvNdCJPdFk9p3JNsjrv40n7a71I-v4nHbumSe7Ddb7s0dFTTgnpWcO3jaSnzcSMTPz9gMLpT1S07Av3d300hVtQys1Wuck-Xy-DMV9J-Mg0dSjTNHC8yDVcqknVPggZkBelwlVy8rlLEMLoXZktd9h6M4EksV8aS5AjRl4BhO5daeotTSxzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش خبرگزاری رسمی سوریه (سانا)، نیروهای اسرائیلی با استفاده از پنج خودروی نظامی وارد روستای "ال-سمدانیه الشارقیه" در استان "قنیطره" واقع در جنوب سوریه شدند، یک ایستگاه بازرسی موقت ایجاد کردند و به بازرسی افراد غیرنظامی پرداختند.
🔴
به طور جداگانه، نیروهای اسرائیلی که در نزدیکی منطقه "الحمیدیه" مستقر هستند، یک گلوله خمپاره و یک نارنجک دودزا به سمت منطقه‌ای بین "الحمیدیه" و "السلام" شلیک کردند، اما این اقدام هیچ تلفاتی نداشت.
🔴
سوریه این عملیات‌ها را محکوم کرد و خواستار عقب‌نشینی کامل نیروهای اسرائیلی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/135611" target="_blank">📅 14:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135610">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
دلار هم اکنون 193,150 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/135610" target="_blank">📅 14:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135609">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
عراقچی: از روز اول تصمیم بر این بود که اگر رهبری مورد هدف قرار گرفت، تنگه هرمز بسته شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/135609" target="_blank">📅 14:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135608">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/951d681504.mp4?token=JxFg2-HRwecz8WmB-lVqyC_ykgp00M-vFGd-kaeIZ9sSsl7yeygwLr38IaYOtGDwMWgs_BaD7M8QJftFB_ez9O8Ckkep65hI8MN9-Wo2WUycsoVVo8dt3YMjcP5di0lwRT0SOcuzpVu3d1evPLtCky4up2JyNFlnDrDTwmEHsZM1GHg_K4svOCUtng0rSe4L4RqRbO9ZAhpDf9Y2xCpwYxEheVkNE-AzTB5TuaU0OV1hwuTS-_0lB2hzAvT_cPFamGW5LMKrdTJg46ZVAfifWuW2eWXNqbUHWtQtjZayYVqpRw63vQ7NWaj50xHkH9VCecA28pLfWGuLXNr40OM6aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/951d681504.mp4?token=JxFg2-HRwecz8WmB-lVqyC_ykgp00M-vFGd-kaeIZ9sSsl7yeygwLr38IaYOtGDwMWgs_BaD7M8QJftFB_ez9O8Ckkep65hI8MN9-Wo2WUycsoVVo8dt3YMjcP5di0lwRT0SOcuzpVu3d1evPLtCky4up2JyNFlnDrDTwmEHsZM1GHg_K4svOCUtng0rSe4L4RqRbO9ZAhpDf9Y2xCpwYxEheVkNE-AzTB5TuaU0OV1hwuTS-_0lB2hzAvT_cPFamGW5LMKrdTJg46ZVAfifWuW2eWXNqbUHWtQtjZayYVqpRw63vQ7NWaj50xHkH9VCecA28pLfWGuLXNr40OM6aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
همه اون مسؤلینی که میگفتن به ایران حمله نمیشه الان باید باشن و بیان جواب بدن که چی شد؟
🔴
چی شد که آینده یه ملت رو از بین بردین؟
🔴
حاجی زاده و سلامی مگه نبودن میگفتن اگه جنگنده ای بیاد به ایران حمله کنه موقع برگشت دیگه اسرائیلی وجود نداره که فرود بیاد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135608" target="_blank">📅 14:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135607">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سازمان انرژی اتمی حمله آمریکا به نیروگاه هسته‌ای دارخوین را محکوم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/135607" target="_blank">📅 14:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135606">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UX-y-eeC5wwCiyJ5DoesxPubseHGmJcgskfduU79cmTUmsPsL02JFNEvKJ_D3YKSv8WFdciiOdXxiof8W9TeborGeeKa82Gr_iJEBPxqf-qP7XqYdb3rjv3BPt0Lr3I7bI7OeQSyfvTMGbWz5yIlR-jCNfN08jFAef0qqqDJd-QIFplJ4hkFTv2wiY7pqsd1S7ZmPx_m4jgM5liQekHTVKyNVtnrlz6_HXv2U3NsSschOgoXdBwey0b-03KlSaeuUQ_suEWGH_LiHIPqn9fK99J2nX2DAit5UHVdAGZPV7t80_IWl1tuf0AN4h6YUT8-jBEnxX3G5pv32ubFMPn9mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دنا کراری، یک شهروند ایرانی-آمریکایی که نزدیک به دو سال به جرم جاسوسی در ایران زندانی بود، با انتشار تصویری در فرودگاه‌های آمریکا‌ خبر از آزادی خود داد.
🔴
پیشتر ترامپ مدعی شده بود که ایران قرار است یک زندانی ایرانی-آمریکایی را آزاد کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135606" target="_blank">📅 13:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135605">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
عراقچی: پس از پیشنهاد آمریکا برای مذاکره درباره به صفر رساندن غنی سازی و تهدید به حمله، تصمیم بر آغاز مذاکرات گرفته شد تا اتمام حجت شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/135605" target="_blank">📅 13:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135604">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cab27f5ed.mp4?token=mgR9iOG4_e-MYcApDNdh1FAQWWyjhPM8sMhI1Qqcm6DYjyWHapU7GC-SxcVrNpCsMOb08L-wrKHUcdDoDj3gLj3WpxDXeiulAgtKkZBQQlSRBguJzBWzGxATuV6P8u3s60in7BiNy4yc6Vh8DJerPgnTYCTap0CEqwOMQxFcs8w_UnD6rwYn5llCJBUWmm7OqB84dnR9BpOp2pP7RkXLgi9hSVZwH-EE12Hw5rapj4qtlKi3gEkhQUkOIrwr46d1jyJX_KFeUfgomXaP7wGdcAw0M4Z6ALISf489VdEqjjE3LfMG4e3uOy8w52IbTiK0xr4571tZuWKjcPg_r5zYfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cab27f5ed.mp4?token=mgR9iOG4_e-MYcApDNdh1FAQWWyjhPM8sMhI1Qqcm6DYjyWHapU7GC-SxcVrNpCsMOb08L-wrKHUcdDoDj3gLj3WpxDXeiulAgtKkZBQQlSRBguJzBWzGxATuV6P8u3s60in7BiNy4yc6Vh8DJerPgnTYCTap0CEqwOMQxFcs8w_UnD6rwYn5llCJBUWmm7OqB84dnR9BpOp2pP7RkXLgi9hSVZwH-EE12Hw5rapj4qtlKi3gEkhQUkOIrwr46d1jyJX_KFeUfgomXaP7wGdcAw0M4Z6ALISf489VdEqjjE3LfMG4e3uOy8w52IbTiK0xr4571tZuWKjcPg_r5zYfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پل در تگزاس آمریکا به دلیل وقوع سیل فرو ریخت
🔴
وزارت امنیت عمومی ایالت تگزاس (جنوب ایالات متحده آمریکا) از مردم خواست از تردد در یک منطقه از شهرستان اوالده خودداری کنند، زیرا یک پل به دلیل سیل که در رودخانه نوس رخ داده بود، فرو ریخته است.
🔴
این حادثه پس از چند روز بارندگی شدید و وقوع سیل در مرکز و جنوب ایالت تگزاس رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/135604" target="_blank">📅 13:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135603">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
تسنیم : انهدام پهپاد MQ9 در دهلران
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135603" target="_blank">📅 13:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135602">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سخنگوی هیأت رئیسه مجلس شورای اسلامی گفت: جلسه علنی مجلس سه شنبه هفته جاری در بستر فضای مجازی برگزار خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/135602" target="_blank">📅 13:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135601">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
روزنامه والا به نقل از یک مقام ارشد امنیتی تایید کرد: ارتش ایالات متحده به طور قابل توجهی نیروهای خود را در خاورمیانه تقویت می‌کند، این در حالی است که تنش‌ها با ایران رو به افزایش است، 10 ها فروند هواپیمای سوخت رسان آمریکایی روز گذشته به خاورمیانه اعزام شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/135601" target="_blank">📅 13:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135600">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
سفارت آمریکا در اردن: مقامات پادشاهی اردن، فرودگاه بین‌المللی و بندر دریایی عقبه را به دلیل یک تهدید مشخص و معتبر تخلیه کرده‌اند.
🔴
ما به شدت به همه شهروندان آمریکایی توصیه می‌کنیم که از سفر به فرودگاه یا بندر دریایی خودداری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/135600" target="_blank">📅 13:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135599">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
عراقچی: آتش‌بس اولیه با آمریکا در جلسات کوچک‌تر از شورای‌عالی امنیت ملی پذیرفته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/135599" target="_blank">📅 13:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135598">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
جزئیات گفتگوی عراقچی و ویتکاف
🔴
عراقچی : به ویتکاف گفتم تا حالا شده در جلسه‌ای شرکت کنی که هر لحظه امکان بمبارانش وجود داره؟!
🔴
با ما طور دیگر باید صحبت کنی؛ ایرانی‌ها را نه می‌توانی تهدید کنی؛ نه می‌توانی تطمیع کنی!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/135598" target="_blank">📅 13:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135597">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
عراقچی: بمباران بیت از طریق حفره امنیتی صورت گرفته و این حفره امنیتی همچنان وجود دارد
🔴
این حفره امنیتی در جهت‌گیری در تصمیم‌سازی‌ها هم اثرگذار است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/135597" target="_blank">📅 13:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135596">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
عراقچی: من هنوز آقا مجتبی رو در این دوره رهبری از نزدیک ندیدم
🔴
چند نفر معدود فقط با ایشان ملاقات کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/135596" target="_blank">📅 13:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135595">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
دقایقی قبل دو کشتی در مسیر ناایمن تنگه هرمز مورد اصابت حملات سپاه قرار گرفتند و دو کشتی دیگر از ادامه مسیر ناایمن منصرف شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/135595" target="_blank">📅 13:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135594">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/796f478a7d.mp4?token=RJWkJJgjiiTuWKTsuYh5LWMxeaBcAifiaYGDnOcH8laKOmDHxA0j3waMoEISenBPLzAPTp3HZE7-1UN8y4c0EoAbruYya09Q2HICA_XuVgloxlSusBApHEoP1pybS2L2UYry56khKsIHBbN65dHiPICZZX99OPjFQg2YdA-b-RjaQUzDSXPrjnHDmV3Bo6Nyo4KQ3jGFqVO2R1NNg0NplxyFdXnj1DKvBUz8bl4A3MFErBO5HV4sUS9qljOXYVqb7mZB4mAgVTpkE4iw9bqW_0ax3ZIZIdp256KFdhdintvXQbTabLqOU-1j_B5CR1KzeKxRwnJV9ytbSBl95GNCu52uV7C2mi8aNYFK6tbrCSF0gUQKY25uAT1qYpHzPgi_OOp_PTbTEzENLO87YluSNcFzPqAmfr65CHUwEarmLsMiT1THEpoTyMbpmeU-3GxAH4p4UAF3-M9k5ORXURvT78tZ_ey0INMBLGILggSO3Th57T5cPLsosU9UBm5EmnUSIQpfdnjmiZHxxcAm_dP-UaZHZi4iaohVVBIr06i2jdR6wQluXsgcDZ-ZB-0jO5P3pCJHwcBYCfa3VvTbwGyq40DFh_hRfFI70D_3u2eMyPMDuAiFeZqsF6TLa1x-YzpZo3IePjLLEIV8nt4kWN0gqbffCtB7HT-jY36UWuXljY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/796f478a7d.mp4?token=RJWkJJgjiiTuWKTsuYh5LWMxeaBcAifiaYGDnOcH8laKOmDHxA0j3waMoEISenBPLzAPTp3HZE7-1UN8y4c0EoAbruYya09Q2HICA_XuVgloxlSusBApHEoP1pybS2L2UYry56khKsIHBbN65dHiPICZZX99OPjFQg2YdA-b-RjaQUzDSXPrjnHDmV3Bo6Nyo4KQ3jGFqVO2R1NNg0NplxyFdXnj1DKvBUz8bl4A3MFErBO5HV4sUS9qljOXYVqb7mZB4mAgVTpkE4iw9bqW_0ax3ZIZIdp256KFdhdintvXQbTabLqOU-1j_B5CR1KzeKxRwnJV9ytbSBl95GNCu52uV7C2mi8aNYFK6tbrCSF0gUQKY25uAT1qYpHzPgi_OOp_PTbTEzENLO87YluSNcFzPqAmfr65CHUwEarmLsMiT1THEpoTyMbpmeU-3GxAH4p4UAF3-M9k5ORXURvT78tZ_ey0INMBLGILggSO3Th57T5cPLsosU9UBm5EmnUSIQpfdnjmiZHxxcAm_dP-UaZHZi4iaohVVBIr06i2jdR6wQluXsgcDZ-ZB-0jO5P3pCJHwcBYCfa3VvTbwGyq40DFh_hRfFI70D_3u2eMyPMDuAiFeZqsF6TLa1x-YzpZo3IePjLLEIV8nt4kWN0gqbffCtB7HT-jY36UWuXljY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی، رئیس‌جمهور اوکراین، اعلام کرد که نیروهای سازمان امنیت اوکراین (SBU) شب گذشته سه انبار نفت را در منطقه استاوروپول روسیه مورد حمله قرار دادند، در حالی که نیروهای مسلح اوکراین نیز یک تاسیسات مرتبط با سوخت را در همان منطقه هدف قرار دادند.
🔴
او همچنین گفت که نیروهای اوکراینی با موفقیت سه تانکر نفتی متعلق به ناوگان سایه روسیه را در دریای سیاه هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/135594" target="_blank">📅 13:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135593">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b37d820b19.mp4?token=db7B65f1e2SrvCiWeqUkqvM0xObAbPYCrsw9wj_gbu5uBnyKrNqkJ-KX-t8aCALxbtwGiHpSfqWG0CpwWOc6FtI4ndlSycIPLMUEJzNdF_jCGN6v1j0x5GaJR48jA_vWaWCRXrp63e_ZnmGlIWQ7uHrZfeNHHC2TfbRVa5tMYFLlI9--98iEZhCyHZPTn10ipHR-enOATKhVtc79_TdTyw2pOUoc8yFEcYYLKRD4ewAPkGAvo64rvmBS0-uXMdwtIcbFjWOkIqSFlmTKEuxl6bPElDE3jSRHBvXxdIDkS-2YauZB5QNFGxfaCWZ-CytL-PLD6Txxe2UN__xCpk7BWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b37d820b19.mp4?token=db7B65f1e2SrvCiWeqUkqvM0xObAbPYCrsw9wj_gbu5uBnyKrNqkJ-KX-t8aCALxbtwGiHpSfqWG0CpwWOc6FtI4ndlSycIPLMUEJzNdF_jCGN6v1j0x5GaJR48jA_vWaWCRXrp63e_ZnmGlIWQ7uHrZfeNHHC2TfbRVa5tMYFLlI9--98iEZhCyHZPTn10ipHR-enOATKhVtc79_TdTyw2pOUoc8yFEcYYLKRD4ewAPkGAvo64rvmBS0-uXMdwtIcbFjWOkIqSFlmTKEuxl6bPElDE3jSRHBvXxdIDkS-2YauZB5QNFGxfaCWZ-CytL-PLD6Txxe2UN__xCpk7BWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واژگونی عجیب کامیون با  ۲۰ تن بار در سه‌راهی کمربندی سمیرم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/135593" target="_blank">📅 13:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135592">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjMBV4QZrPd6mpIMpZNARCh7uOKh3w5ku450Y5DAsy4EgMEY_WXS4uFiD4EqMMYbh7bJgKpZhrlivp480bOUhUPmljSIF9dWLPOe817ZDxf5vMgvqYwxbmaBKTZVv5qgV3Ka6Gj6EgEFWlpzPBxzZWrtRDlvQC_ZGgjxgPS0NqEXeS_t0B4fvXZ3m4YsVr4K1Z1YiU3vgXKIIrah80vZksKv3gDhXQfTXATRtDWs8btevfvur-doUXJA37n5AZ8R5lt_--xiPVmvPLnt5jguocHWdGrI1Q0exaK3DN9EWsCDAvIQFc5sUAQif3vypNjBimqKP5LoMAWZvD3nHCgnnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: اطاعت از رهبر یعنی اتحاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/135592" target="_blank">📅 13:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135591">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
تلویزیون بحرین از دفع حملات هوایی ایران در آسمان این کشور خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135591" target="_blank">📅 12:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135590">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toRP_Zgd6QVrq9-Otc0TURf2JQsd1IsNC1c6HlwZM09tfpfOGi1zeDwX8zujbr5XhQQi20GypODfESZnS-uxSeIb6rcowalLGWKRkAaMPMAEw8FF4Y91GJGsW62_ONFKzViIe_fpgxdx09-sfLCU_-1vOEZRRt18QPLJNi-UyGPiy9SDZjQ5LlFRImmHI0tvPwb4YBGclWr0xOR98Rs5jGLdQfvmTglAPpaCFTLsi1lcRN5MJxfKR1yIe03rbQvTYMtVUH2C66kYdMr8UMfBB0z0O0QGLGTiDPqgg9KN477HQv0uNj9fOyfboVzZNGm1HN-PJs9V3I-OgraLgZ-NUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
براساس گزارش Downdetector، اینستاگرام و فیسبوک دچار اختلال شده‌اند و کاربران نمی‌توانند به‌درستی از آن‌ها استفاده کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135590" target="_blank">📅 12:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135589">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2f58528b3.mp4?token=RunPJcMlN0qUpmqllq6YoVVRqZMkDjgBlwGgpVUfS1xJ9_KPkpywtLncUTU01jDB__1T3U5EfYBmJ4Vj_19HPVe_EWY_Ks5qztBlvXlkJdq9fIb3rpMR6bt3YQ3u0I_qWFV-zPLCyFWqyt8H0CNFF70NoBgypmusXDrKyo3bel3-S-4-vVTrj2b07xxY_D4uxWkZl5HTGASghAiV1TfeEqKlUprMm6mRHRR-FnVUl3NrHFz3D6-BUNr2Kn1qLRcpUQs07nnIiQ7EhAXOxGX8U9WISfxVFio501zeKSm0gQGBOIe0-3sWS_15lol2pXEVK4yniXmiRX3RnlKrTO-YlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2f58528b3.mp4?token=RunPJcMlN0qUpmqllq6YoVVRqZMkDjgBlwGgpVUfS1xJ9_KPkpywtLncUTU01jDB__1T3U5EfYBmJ4Vj_19HPVe_EWY_Ks5qztBlvXlkJdq9fIb3rpMR6bt3YQ3u0I_qWFV-zPLCyFWqyt8H0CNFF70NoBgypmusXDrKyo3bel3-S-4-vVTrj2b07xxY_D4uxWkZl5HTGASghAiV1TfeEqKlUprMm6mRHRR-FnVUl3NrHFz3D6-BUNr2Kn1qLRcpUQs07nnIiQ7EhAXOxGX8U9WISfxVFio501zeKSm0gQGBOIe0-3sWS_15lol2pXEVK4yniXmiRX3RnlKrTO-YlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خضریان، عضو کمیسیون امنیت ملی: کویت بداند وضعیتش در پایان این جنگ عادی نخواهد بود
🔴
حملات از کویت را حملات مستقیم تلقی می‌کنیم و بدانند که به‌صورت ویژه ادبشان خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/135589" target="_blank">📅 12:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135588">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از داده‌ها و تحلیل‌گران: ایران از آتش‌بس برای تسریع در صادرات نفت خود به چین استفاده کرد
🔴
حدود ۲۰ نفتکش ایرانی که حامل نزدیک به ۷۰ میلیون بشکه نفت بودند، پس از لغو محاصره، به سمت مقصد خود حرکت کردند
🔴
تهران رویکرد همیشگی خود برای دور زدن تحریم‌ها را در پیش گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/135588" target="_blank">📅 12:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135587">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
گزارش از انفجارهایی در شهر حمد، بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/135587" target="_blank">📅 12:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135586">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وقوع چند انفجار در اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/135586" target="_blank">📅 12:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135585">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ترامپ به نیویورک پست: جنگ با ایران ضروری است، اگر ایران را متوقف نکنیم، کل منطقه را به درگیری گسترده تر می کشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135585" target="_blank">📅 12:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135584">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJZnzRsDv5nmXEtrVOOxV-SpZ-PV7P1QtBtYcEIikVma466rGO5caQufD8SWk66Oi8vfLkkIknMkagYgT5SU0HqbbXUFcjrLL2DhO96MzdjNC1SCTTP589l78c2WnZVn6kCopir1UtIcnX-N2z5A0X7EWmVZ220PZXk7Jmx4lRCrUse0_5GdaFS9K37vjefYYEuNGfBx7fLYj3FySD_gCBy41kCQ1ORuPDkopV1k36LEJuEAHvtgV7RQGPxIloVcHKiba-L4cLQ_CUf9X_t8hQbhyxHouR_QA0shwl20_GDTlXj4mUIoLtpNgvkQ86bJ7JEOjs4LSZVMRuz562IT4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: هروقت انتقام بگیریم و ترامپ رو بکشیم، وضع اقتصادیمون خوب میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135584" target="_blank">📅 12:20 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
