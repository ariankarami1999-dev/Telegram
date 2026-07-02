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
<img src="https://cdn4.telesco.pe/file/L6eANzg5E2ope30iE-H-ULCvd7G7wVWIzTloBYNqXcmq7zn-BobyVwCd0ZwAclmZtL_4gOq305cOK_MNfXllWc9Ghw-N5A-7QcSViJlWV32TqHyeaEgq8bzSO_VEmRmyYqaAbOdW_vCzZ-JcIb07rKRQLOFSjUuM5iS6zvwXmoMvJua5fn0wrpvSzoQ9IMvMi_pwZhmhqxKiIlhITFeABtp7aJT7qOuu73bYRJCtsrv958Q73_FuX_29Ohm1VrCwbsH7Y0Y0jWezT3ftlakOfIwZMVPTN-iDEDm_jFnCuG7Yl3sQV64eReV09A-6N68B1MZWsFNVBiZk5FFidrM78g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 09:53:06</div>
<hr>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFRJOLf7yUOZDG6O2-P9-XbuNcHV40g_NRT1u0ocoZ1qR3iadf3re8NBpxnniuPm4phQ2q2E4-AotiwJ73YEo0xq1eB8OTnIU12vsJAertDdXHmEBa5kBD6uIjzZ52yOwmXZ6Gm7Stv93GSIPa4GXuIYgKkeHW3-ag3M5B-9njyewMRFP7ghkqG0jSDyXnHQZaT-Z-v67o-ml3bN_KP0z7TSYklkT9lsocmKMMAIk8IH5BWaZcajNDWd1syMML4wC0hDIRsiEFUQmh9MCWlnJjQLz77eUId9r6B4YEAzHNcaR6-C6hFJmKtZR4ExHF4i8SdknRts-a7My4a-3MZuhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد
به نام «روضه الشهدا»
توسط «حسین واعظ کاشفی»
این کتاب عملا مبدا روضه خوانی
و ذکر مصیبت در ایران شد.
و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)
برگرفته از همین کتابه!
حکومت صفویه خوندن این کتاب در همه مساجد و تکایا و….. گسترش داد.
بحث حدود ۴۰۰ سال پیشه.
(کتاب دو سال قبل از به قدرت رسیدن
شاه اسماعیل صفوی نوشته شده بود،
صفویه اون رو گسترش داد)</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=EUkl6ZftdcjVAYUPk6zo5BlTUuUNZpkql8lv7lyL9vWuDHjgo36BUoBkJ8n0vF7G5iGemZO1xOfcUtFEKpE66PqNEgkAUjunbg27Uhpmitk-ExQKrRdqwkL4H6SNkiauzYUMcyAoZ5msdi7khcZFGagbww0PBPQQpmGwJbmZdOZcJ1A5DRBGzK9DeYKUbtQCxU4u2l5tSO-NBBqdYJFW6OhHUxrvyPKhrC-YNfSXTqO7ljHjRSgwjv3nEEaI4Nqoj_RYZbwfQOgMsMqk1k3Ik2elJliisby7wE6yXRsSORGgsptp6qow6MQ75h7smGXS4ZU66sdglxdNZ_A7VbIv5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=EUkl6ZftdcjVAYUPk6zo5BlTUuUNZpkql8lv7lyL9vWuDHjgo36BUoBkJ8n0vF7G5iGemZO1xOfcUtFEKpE66PqNEgkAUjunbg27Uhpmitk-ExQKrRdqwkL4H6SNkiauzYUMcyAoZ5msdi7khcZFGagbww0PBPQQpmGwJbmZdOZcJ1A5DRBGzK9DeYKUbtQCxU4u2l5tSO-NBBqdYJFW6OhHUxrvyPKhrC-YNfSXTqO7ljHjRSgwjv3nEEaI4Nqoj_RYZbwfQOgMsMqk1k3Ik2elJliisby7wE6yXRsSORGgsptp6qow6MQ75h7smGXS4ZU66sdglxdNZ_A7VbIv5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=nJIojmQXwvhDlyNAcV0qRwjUwwNjXVCQfVBg6AKqn1IQogoaHs5iIn5Z4Z5UoOo1nTfcW6R0ZPdu0BRGFcWyrwSuqzrKqc-8_bnWaFLbXtBADrW-26qv35K2X0eDkWQPTLAq_B_YRFXiBNYZefnXX6-K2uBY3hk9xqImUxULcDPOoCBv8yuzevVU95BHkPveR1EIjNk9sSizqBvcWnqtS9wb_3wPtLKYgpUU0tFd8YCXlqmMS2ETBjALrYzJKU2mQEV_GFDW-rocRAdmsFL139ruNi9T5RDphFA3SKFkczRCC0JaEmRXrB2txaNRZKAUpKxpINqvjvG2LqGjAO3Q-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=nJIojmQXwvhDlyNAcV0qRwjUwwNjXVCQfVBg6AKqn1IQogoaHs5iIn5Z4Z5UoOo1nTfcW6R0ZPdu0BRGFcWyrwSuqzrKqc-8_bnWaFLbXtBADrW-26qv35K2X0eDkWQPTLAq_B_YRFXiBNYZefnXX6-K2uBY3hk9xqImUxULcDPOoCBv8yuzevVU95BHkPveR1EIjNk9sSizqBvcWnqtS9wb_3wPtLKYgpUU0tFd8YCXlqmMS2ETBjALrYzJKU2mQEV_GFDW-rocRAdmsFL139ruNi9T5RDphFA3SKFkczRCC0JaEmRXrB2txaNRZKAUpKxpINqvjvG2LqGjAO3Q-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=CGJ2IYAY_HuuP9opo2RDZmPfUK9IrLdV6HJGrjMspqp_xVLj7ljyzwUtmifagjtJQJub3wJeo3p-MFm2C-RtYrESu8AHUOXZ9ObtxlwmmYIn6_vziXgCoSmCo5RH4VB8-J3a3IbRThW8KE-c4PK3IkBpHaqSowFE0tsfeLKTwL30doDT25wFFi1CJnbeoG6Ws1YF1YHXZMEHzRLWfLUFCQ-8ZxWjOAeeyVTPfupZBu8I9YLqMfcic2pSaQxsBQEk25g6nD6M1cqifVDlfYkOoVor4j2e1l6uS5O5s8QyY0Y3nE2737miUQnQMpTvTJm4wpKO6wiQAnpRunmLtKDHNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=CGJ2IYAY_HuuP9opo2RDZmPfUK9IrLdV6HJGrjMspqp_xVLj7ljyzwUtmifagjtJQJub3wJeo3p-MFm2C-RtYrESu8AHUOXZ9ObtxlwmmYIn6_vziXgCoSmCo5RH4VB8-J3a3IbRThW8KE-c4PK3IkBpHaqSowFE0tsfeLKTwL30doDT25wFFi1CJnbeoG6Ws1YF1YHXZMEHzRLWfLUFCQ-8ZxWjOAeeyVTPfupZBu8I9YLqMfcic2pSaQxsBQEk25g6nD6M1cqifVDlfYkOoVor4j2e1l6uS5O5s8QyY0Y3nE2737miUQnQMpTvTJm4wpKO6wiQAnpRunmLtKDHNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=fJmyzrsMTEmfYg_rMFPn0Ixn8MTnBtAu658X_H3B2GgjFg1-z26rZdrknyz52DkUrTn5TN-fK20rdloKGq4Ohh7UNt4StDLaeZ9_GU36Waig4_lBAvuS7I6GviSBcmb4KWJiQepjpV9dhLLIgkTulpugjVunI2_6SSFsH7fYaofSRIoszhxrTO-dfW4gXUSFU0PudgFxJokIqBp_Brof6wpOjFQ-rLMXOlo4OHAS8fwo53mACjK8ibfUz0PxxOe4h_mquukU8liulEiGtUEkxzU6uQQBP4z4SpYqDD_JqQXrUOmS7GGsVd_hUMZLFKG9W6wPAPUcvzFifND9Ot1fig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=fJmyzrsMTEmfYg_rMFPn0Ixn8MTnBtAu658X_H3B2GgjFg1-z26rZdrknyz52DkUrTn5TN-fK20rdloKGq4Ohh7UNt4StDLaeZ9_GU36Waig4_lBAvuS7I6GviSBcmb4KWJiQepjpV9dhLLIgkTulpugjVunI2_6SSFsH7fYaofSRIoszhxrTO-dfW4gXUSFU0PudgFxJokIqBp_Brof6wpOjFQ-rLMXOlo4OHAS8fwo53mACjK8ibfUz0PxxOe4h_mquukU8liulEiGtUEkxzU6uQQBP4z4SpYqDD_JqQXrUOmS7GGsVd_hUMZLFKG9W6wPAPUcvzFifND9Ot1fig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=FarxS6zgpjZbJtdjVKsI9PYgizVHgSdHTRQkkHiVO1uiiEyFskU0N-Rdx88iIw6GUtGQumGrL86zi7yK7WO4CaVsDDnRWOejKWDSfJOHFxXQy0Vpd895tyP7mTGh261_3VJqYcznM_vEvUM2O63enKKqRBAlMiw4E8IyPQaJFY_HAvTu6vwDCB2vtY71JarmLXp3l32UoGp--hQWkEugyvx8_-kt3OJCz66VJmyCy0KkKt9X_Temnh3m4uuG1ALOTT3xV4Xhek2MMrZQvTue_PR-Iu6Y6V13t_21kNlw2bJIDOZln7eTOaejovHSZ9dboFgBQ_Pi5ylN81kygCjqJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=FarxS6zgpjZbJtdjVKsI9PYgizVHgSdHTRQkkHiVO1uiiEyFskU0N-Rdx88iIw6GUtGQumGrL86zi7yK7WO4CaVsDDnRWOejKWDSfJOHFxXQy0Vpd895tyP7mTGh261_3VJqYcznM_vEvUM2O63enKKqRBAlMiw4E8IyPQaJFY_HAvTu6vwDCB2vtY71JarmLXp3l32UoGp--hQWkEugyvx8_-kt3OJCz66VJmyCy0KkKt9X_Temnh3m4uuG1ALOTT3xV4Xhek2MMrZQvTue_PR-Iu6Y6V13t_21kNlw2bJIDOZln7eTOaejovHSZ9dboFgBQ_Pi5ylN81kygCjqJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=HHocNLqPVi8CabV33iE6qhkEZcdwdKu8xOzgj0sVNWNYQkEMxHTzZOEPjFtB8R6zgrNwrwDlzKCG8731c9pDP63fwsZXXIp54ql2u3ZJbmL2uR9sPVmQZgWhmgsCpASl4OO-umJRWXN5X9rXHo8y4YvagG3EmuuDoXHBXCUpEbB2mPeiwqGAGggKEHMkiH_SXjx_66574fxQZu8-BW08s4GykFLy_cQR-ZZkAeA1aMkfDxU4ujz0fh804VtZkOEO7uJTa82bVKxlqh68X8VnBXnZWCPW4O9WBjmRUgs2R58W14qz3WiT3sHHJbfuSfNcKGSG4XpPMLizpi3_tNsZDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=HHocNLqPVi8CabV33iE6qhkEZcdwdKu8xOzgj0sVNWNYQkEMxHTzZOEPjFtB8R6zgrNwrwDlzKCG8731c9pDP63fwsZXXIp54ql2u3ZJbmL2uR9sPVmQZgWhmgsCpASl4OO-umJRWXN5X9rXHo8y4YvagG3EmuuDoXHBXCUpEbB2mPeiwqGAGggKEHMkiH_SXjx_66574fxQZu8-BW08s4GykFLy_cQR-ZZkAeA1aMkfDxU4ujz0fh804VtZkOEO7uJTa82bVKxlqh68X8VnBXnZWCPW4O9WBjmRUgs2R58W14qz3WiT3sHHJbfuSfNcKGSG4XpPMLizpi3_tNsZDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=Mq-bcTPjzoOviHrwKgqre8iZP98zVqAL62SUwcn-4ZgIjvIvNF_AqmNTnuGoWVoSBhzjB3ulInQekp4DaJ7hExKFGXCIie35TO9LNsm638VY1QKI8y0f88JnHCUoju-gegeoo6UYwd_BcW95gXmxFRwAwtpBTzTZEKlfMBSBipjBNMaOysJ5jGQnV7TbtnHNaJ_Y8wy0uQTK6RNKzruuyLI28bDqjMBr8mCHFVjBaWcdQMxnlJjXRxKhDyfCWd125FU19T32etbiKAldPXKFiY10OXNmAAMw9DYTHcBQMSrTF-l0V4rbsVw_yZeWGNCaJxX5OnVkZJzyRn6PgSJEWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=Mq-bcTPjzoOviHrwKgqre8iZP98zVqAL62SUwcn-4ZgIjvIvNF_AqmNTnuGoWVoSBhzjB3ulInQekp4DaJ7hExKFGXCIie35TO9LNsm638VY1QKI8y0f88JnHCUoju-gegeoo6UYwd_BcW95gXmxFRwAwtpBTzTZEKlfMBSBipjBNMaOysJ5jGQnV7TbtnHNaJ_Y8wy0uQTK6RNKzruuyLI28bDqjMBr8mCHFVjBaWcdQMxnlJjXRxKhDyfCWd125FU19T32etbiKAldPXKFiY10OXNmAAMw9DYTHcBQMSrTF-l0V4rbsVw_yZeWGNCaJxX5OnVkZJzyRn6PgSJEWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pialK1hk9HI2hstF9Bak8n6E24Whj9d9TY9oqsM3ZlOChJO8T5JClSiGEx8sM0ZbkgaSwZBljwne77_rkVaL6PG5maf9dsvVkCtEQFGzZxJRNExnNymIeaWCEGUxXjWjilHElaLgnKLYUeomOau7iUIkkYQG33exnYnW1j8rs0ps684fIcLFqje48DeOMgmFnN6HJtS-wXS2EjFto_rl5NEyOypP3nuWUE7GT9p_onMyz6SklOvuaBO1zmnlFqM6GJB5147mvItjtD2nJ367wB3yXDM9JirmJ-Zxo5B_IULXWHik0eA545yCEjx9aX-O4MD9uTuJBqDbjdBNzZVm3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=uM5ZU1dLXBaDc7vcDrW2e_wuanDsWlVoKBe4NahKBWDAejduDkwsTsIqihRAGfhp7WaFYEqiMkvP04ju6XneDjGPpNzcz_fI5rD9lCubl9d2Jdac-9JMH9-614SJM04aZVq2wXfbrj_zjddo9QUPV8HrkY4wOWyvUn73RDxumOtT_yXskLT71jPXx81Rey9KHAjYs8GVKmZ8nYp_AKYfrrSy7AN-MwrxWp7uskm_Gxot5nYh6upzSI95ymwGuFCi91ht0SHFRmX_6pX71qhV6mcC21iLGdV_hqnZ8QutXMESneokbpnsDAsxj4088tQkSNbeykR-rtn4Fhy-DSY0rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=uM5ZU1dLXBaDc7vcDrW2e_wuanDsWlVoKBe4NahKBWDAejduDkwsTsIqihRAGfhp7WaFYEqiMkvP04ju6XneDjGPpNzcz_fI5rD9lCubl9d2Jdac-9JMH9-614SJM04aZVq2wXfbrj_zjddo9QUPV8HrkY4wOWyvUn73RDxumOtT_yXskLT71jPXx81Rey9KHAjYs8GVKmZ8nYp_AKYfrrSy7AN-MwrxWp7uskm_Gxot5nYh6upzSI95ymwGuFCi91ht0SHFRmX_6pX71qhV6mcC21iLGdV_hqnZ8QutXMESneokbpnsDAsxj4088tQkSNbeykR-rtn4Fhy-DSY0rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=RUYbYCMtpUa38zQUnGs3Q7WxPe3AMuajBMmf4oWPMuWqD2TIH2jHX2oQguCExT3zcZbwLOEuJ_E_EUT3xV_dZBbhOSe9gBh7haS2C7heEJd11x3aJ3yVvxnLy64WKf-_oNgn-IoE2C3-Ka-ryvK7M_kPD5rQ2vc5AQhUoIOXFbDlhZy5CSzxXT9YHn5EKvqHdDckfmWo0FRV0PqpoBDtU70n6n03Frf7B9mZtszDiIMR8Zamsv4gT4DRrrzptfCazXiqncNjxK5PNTTn8ne3P0M-2oO9AgEvaPAJDrutbrNwbzCyG36ZDUixGu5FmidJBQxYAzxAs1KQuhI0oG1Xow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=RUYbYCMtpUa38zQUnGs3Q7WxPe3AMuajBMmf4oWPMuWqD2TIH2jHX2oQguCExT3zcZbwLOEuJ_E_EUT3xV_dZBbhOSe9gBh7haS2C7heEJd11x3aJ3yVvxnLy64WKf-_oNgn-IoE2C3-Ka-ryvK7M_kPD5rQ2vc5AQhUoIOXFbDlhZy5CSzxXT9YHn5EKvqHdDckfmWo0FRV0PqpoBDtU70n6n03Frf7B9mZtszDiIMR8Zamsv4gT4DRrrzptfCazXiqncNjxK5PNTTn8ne3P0M-2oO9AgEvaPAJDrutbrNwbzCyG36ZDUixGu5FmidJBQxYAzxAs1KQuhI0oG1Xow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=lwZdIZBcH58DkCMaATQw31Fv7hm2Y1uQBSkZNMu6b8U1l5_JTPdybrEepT8QJKal8owTD7Ka9aqqymBXxOFI1lyde07IwmtV1RhjNSCO09UyDx5prSaWM_lTL7OrBoSYvHCmTVV7jJSZysarJMkm7ZVI7-jPKRn7-kN0-lKZeszUcZF1xv2theYxUZSWyep_MFEoRE28S9At6e3iZywyMcIMlScJIOJ0BOAEPnq5y8f-EBB783puu1mjLNx50x-DwWTSKQdDLWSg7Z4JGMc3wzD0k97t7BvP0OQ4p67-dhpYv0WuUF10eGJGGrPEepoqMy9FNGry1hMaeEWZ8tU-5ERJrxOULTFtPP-_LkocEemiBdGDhwXglpGloFsyV644F_PRzIOmcDAnSdBU9FVQxHsOUvF9p51eoEPJVDGWM6ZYmLku4IgrzdpvBNRL_D9EByaTnwSROzqQTAAs7W9f-uoqxRUebrLkIkY6ZhG9NvduNExBwaorUhnCwyKCFFpCqq2N1YqQQgvyoRlShaHnvBb3XRDKW_GEHM69L-oF0OdtXAqYCcFW3vZSdVRHZP_lEOhvSYxLR1ezTBO8pbDWW3VxaotTsfCS06kmq1Tx5LbdfCWffDlmHUnBGXVeIpz1H5PGewDEQm95uCcbSKAJEK61sbmEKqLwqBlV3FonMcc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=lwZdIZBcH58DkCMaATQw31Fv7hm2Y1uQBSkZNMu6b8U1l5_JTPdybrEepT8QJKal8owTD7Ka9aqqymBXxOFI1lyde07IwmtV1RhjNSCO09UyDx5prSaWM_lTL7OrBoSYvHCmTVV7jJSZysarJMkm7ZVI7-jPKRn7-kN0-lKZeszUcZF1xv2theYxUZSWyep_MFEoRE28S9At6e3iZywyMcIMlScJIOJ0BOAEPnq5y8f-EBB783puu1mjLNx50x-DwWTSKQdDLWSg7Z4JGMc3wzD0k97t7BvP0OQ4p67-dhpYv0WuUF10eGJGGrPEepoqMy9FNGry1hMaeEWZ8tU-5ERJrxOULTFtPP-_LkocEemiBdGDhwXglpGloFsyV644F_PRzIOmcDAnSdBU9FVQxHsOUvF9p51eoEPJVDGWM6ZYmLku4IgrzdpvBNRL_D9EByaTnwSROzqQTAAs7W9f-uoqxRUebrLkIkY6ZhG9NvduNExBwaorUhnCwyKCFFpCqq2N1YqQQgvyoRlShaHnvBb3XRDKW_GEHM69L-oF0OdtXAqYCcFW3vZSdVRHZP_lEOhvSYxLR1ezTBO8pbDWW3VxaotTsfCS06kmq1Tx5LbdfCWffDlmHUnBGXVeIpz1H5PGewDEQm95uCcbSKAJEK61sbmEKqLwqBlV3FonMcc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=oE9Gz8HfKiK1GNeA4IQkn6E-S-GkCIKRQaXQSNUhy2rmw-Eec-glvVS1jAtMdwkAQ1QZG82-sjOLVZmdBCm9r7kDpTJ3plE1UfEq_SZTiEmZjJyvosEjY_xOtluTid3i6aupSLb2Oz3MunembQcOH2eMfoMev-Q1noTCXPob2oVfOFy_QoN4bD4OazGPlTmTEVTYYoYpiiema1zKd89n3OqUeTbQqBn_Ql8Bx4Ge7r5gZDZTI44D52b16Mg7wXUPaeIGNpya97hdhMKUDXHrYi6-ps3Mrd0uGaeWUBik6CcVuu5Ek1lk0X1bH-R-9xxTuoHtHBqV3i0UbrkgIQkwhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=oE9Gz8HfKiK1GNeA4IQkn6E-S-GkCIKRQaXQSNUhy2rmw-Eec-glvVS1jAtMdwkAQ1QZG82-sjOLVZmdBCm9r7kDpTJ3plE1UfEq_SZTiEmZjJyvosEjY_xOtluTid3i6aupSLb2Oz3MunembQcOH2eMfoMev-Q1noTCXPob2oVfOFy_QoN4bD4OazGPlTmTEVTYYoYpiiema1zKd89n3OqUeTbQqBn_Ql8Bx4Ge7r5gZDZTI44D52b16Mg7wXUPaeIGNpya97hdhMKUDXHrYi6-ps3Mrd0uGaeWUBik6CcVuu5Ek1lk0X1bH-R-9xxTuoHtHBqV3i0UbrkgIQkwhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه تروریستی حماس
در شهر رفح در نوار غزه یک تونل ساخته به طول ۱۶ کیلومتر!
تقریبا به طول خط دو متروی تهران!
که این تونل از طریق خونه‌ها و مدارس
به سطح زمین ارتباط دارند.
این یکی از تونل‌هاست!
خود گروه تروریستی حماس سال ۲۰۲۱ ادعا کرده بود که ۳۶۰ کیلومتر تونل ساخته!
این همه پول رو صرف ساخت تونل و موشک و
اسلحه و….. کردن که مثلا مبارزه کنن!
میارزه هم کردن و نابود شدن و ۷۰٪ خاکشون رو هم‌از دست دادن! می‌تونست صرف مدرسه و دانشگاه و بیمارستان و غذا بشه!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=K_hVU1REAgYCzV5qh5_zXIlC_NX8aVqpvDyJtRZUoF-DKmUheuQsj-nxqd5RD8PLyvv4LAXuy_THpOOWCegaaMRGu3IX3-TRd63UfRzFJsjb9GE3-MwMOLnfBtBLSHCdc637qkbGct8PdiQIj9BdfFqM1MXTQ3tkCUQgYLeynQF4g5KtZ5Dd1LzsKFUsRd7EGaKkhbEExvjNAzvz9NHdwiYA9z1YQVWVqnC3cba2zzHNFY-W6WqU1sYfra6_2i2jGjU4vB0VI0zAxOGIQ05QX0K7DzNSrnIRVysjM_DnzVAfR0JTWb9czCH26dxS8UdDpEMN_Psst_UmvG46SJBsCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=K_hVU1REAgYCzV5qh5_zXIlC_NX8aVqpvDyJtRZUoF-DKmUheuQsj-nxqd5RD8PLyvv4LAXuy_THpOOWCegaaMRGu3IX3-TRd63UfRzFJsjb9GE3-MwMOLnfBtBLSHCdc637qkbGct8PdiQIj9BdfFqM1MXTQ3tkCUQgYLeynQF4g5KtZ5Dd1LzsKFUsRd7EGaKkhbEExvjNAzvz9NHdwiYA9z1YQVWVqnC3cba2zzHNFY-W6WqU1sYfra6_2i2jGjU4vB0VI0zAxOGIQ05QX0K7DzNSrnIRVysjM_DnzVAfR0JTWb9czCH26dxS8UdDpEMN_Psst_UmvG46SJBsCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ePD7R4akJNHgtADoLLrEGmggcBlHSCWonPMhTvzps1rXUU5QHyOhW7AEJU-wsoCKCUkneA0rIVGxQdV09hWNvoY_TGlJ5JscAuvtZwx_FjQPBCNolGMx4uy_2miPHn3C0he8F-Gdy5AhkwXxOAByaQgsQ6GpjfFXJ4p_LDkiDMTeeIU7FewLD761zzIK_nzdyGFUILhJoniqmXXl9-JDzIa8tRb9z7d-WDIwbk4RDxJ302fMiZ5dqD3kwvZ6QpD9-bgN2Xcb8y5ApKiAcjQ1GStsDV-1ajjMCVLCx40W1Q92zkQk43Tf-lPU9Wl2idMzPSEFegspk8Z5VfDYGxnJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fahTgi4jsNM3S9IweY50s1VBGNfoHpiiZlJ1GG4UftA0KGr1gEJy8J-zr4MhwZ-xKyLYgzPjYRgkxJgtuXDJCLQYxnqjIsn6yowDqYlu7yIpsWs93Z5j-MppWVYNi8GMJOdoZUwlM-cSJHRx2JWfmljPzCP6Y7_8Mxf-yGHtVHEZWj0zfPgXUZc4Oe8QlqmovLr-ViaaCaqSe-U0ZoO4S2VTwtWyVXVxBnz3hdD7_r28_ydLtBIATwbt6qFTAlD_8jyV19w0aJzIN4o8ep0ZMIaiwXTfojX8gmDD66CPQP_35DRgUUfe0oDfTavWdnVLieTvkCe8yQYqlN3ctkyt4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=J12XfAPqKXlUM3VTbQnv_Pigmgu0Cht8-m5YH83LY3s7Dv7YY_aD2lus0Wy6Ab2TbczCRabL6jz24YD9rqjl_ePmHkEUvz_kdPSGudU_kFGOfEiO_86R3Q4_s9gHig_ycWkjn7Oe1ko-2U3ce5CN4PXQg1c2Hag2tprbmiuVlFaORd1pZ794YtLxwsvw_kjqrxl4BaUC0Axo1_sAbFdDv5qFt-UHD2F3-4mFJknlAap30fdecSK0U5-AP2bmgxPwKJ0IP1U60HTqjEdfFtuAfmYg0cZLgogazA136V_E4HalsR5GnraXRxJAzS7BOZGbHdIz0YlRWfMDLK1pn2Bl2IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=J12XfAPqKXlUM3VTbQnv_Pigmgu0Cht8-m5YH83LY3s7Dv7YY_aD2lus0Wy6Ab2TbczCRabL6jz24YD9rqjl_ePmHkEUvz_kdPSGudU_kFGOfEiO_86R3Q4_s9gHig_ycWkjn7Oe1ko-2U3ce5CN4PXQg1c2Hag2tprbmiuVlFaORd1pZ794YtLxwsvw_kjqrxl4BaUC0Axo1_sAbFdDv5qFt-UHD2F3-4mFJknlAap30fdecSK0U5-AP2bmgxPwKJ0IP1U60HTqjEdfFtuAfmYg0cZLgogazA136V_E4HalsR5GnraXRxJAzS7BOZGbHdIz0YlRWfMDLK1pn2Bl2IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4fKtz9aVfS6J92jL69gAiGDLK-hG0_m_Du9Y2aq_OjI1YQUEsBqRGdm1rNOwFBZFWpQY1Qyvm18NDHceTCKgn5vRB_LWiExThmh8TkQ6f7cGwXIc-aV7YhrQUYgHJT6rRXHehEP-aosnmcK9z2Bvv71pt_Xo4wx00bpAcrgZJtPo7wcpRaT8tHOmL_hxZpB0EDZQiw6kS8u-hyX6BX-wc7CEDlEXqBbjNbOh0PP3ONGn0L_dX2hQCxkjgB4lBpL_qw7WhyPdfJ4-hxX9AGeowUnGHk2_5FwgXo1P50MSQ-8AyaqOF8R8aKCDxqcaNOzABPwBgoofO7RS3isGG6oVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v4HqklxJfku_mrrXqYQ1CIzBAaSAdMXnTBy2XWgsIZ8NLZpYhdYtn_0Ffil2ADCLPv5yaEQLKbn-1vkJRDS4nQJNYSdsJlnh_ev36mChCgcKMggsMDhaNSi_KyKQA5p675Mf9Pd3eDlUTcCJJrjAuHhTqAeN2sodFUvihxE92uuUigBTsTgyrn7CVmuUPICvqDNITQBDMw6q1IbVqcI929Dg08qTsuwE_3iEWeC3HwJWisRYmWud7z_-PoUxJEERLLbI7p2ycV6DFRuL4e_u_n1Xqj6u52voOKN9gn3d6a6uSPSnCmJZRekX9_iU6-6Fx0FKaWuLy2XRmpe9_Gjn9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PSh8XnVVJtqMeqBeoxSdMkzBP_9sBj26r_9c7BS5O8G50pjkEuePFJQs5eo_jZGjkFvKIoU3A7UhkGeML7_jHBDPg7_jYGZ8Ufy7LCfo_XN9HuwXrMHjrtDPwGs9MXLshAfn4KYhEYO1kIxBEObAKUfhEELYFiUPtJNNpWvfY7gOV2twztQrUqAcD94kxPXcBt7xKe_WTsTodQSqcx_OCm-dqyBoLnjbODXdqhZ1NK9XYaf7iuuLbOcDMECGn7ObWNXsGTAjXWhYWia_4xk0U5IylXiR64mEu7ObKRNND4F2k1Nyn2c7_NBzdCsKHWDQdngLx7rizzeCc7pYRja47g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smUgyRuPHGfoBzNjz_qKV2ynpKmsOiKaDYcjLsTVVo8MQI0VqP0uRnyqfoDbmHADBRSVMQW4krTK4Avt-bHYhBn3rwQvEhCMMOtwm73H_EyzxX3MXo_oAPoAcWF9qC_BFuzFWVirrGe4HQo_6dMxdgLWM_a5IdPyFqbYBTYhaFko-G-mvJentcqXn3qnUR_ponLAuvlw2c95RnsorSuEJNWnNyy661Ev3OrnCSin44VR7goG6AYs5sI3PSZuTVo7Uk0Jmo0M7gcn95z0TJRJzJ-ZCqX3A68VmAQ_k1Updg-20aWhVXplP9t7TSeBQIPFMJWD_MzcE6B0-YLijBu3Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=p9cfUxdsT5kiqt9RnqXR2_DlfpyKzrdcapghQ_9W5lt5pQcbO68VygWZBmVWlmcG5__A1w_WGx7ea6ba7i1BLh4Ix0Vp-UeH_kKfr4h5YKX0TlOVAAssoObnZuJzXNhnVuQf9tfJ4ZNex_fHmMkkH7TkHHtgIjYsecS7KLrCW8-yi3DQlw-5kyJnrcx-U0U4Nap35HVgQHiB1YXsDN6lw2kBR0EV8rSxBFMECJbiO2C98aKoctUPRavoMCdDabpqVSED6bOjKfcwXO6dCo0hZsKM1wM12tMGcibdynFhF8Uk0FWWbhm16WgSQTAAhSgVQFCrkI_ZXVRcT8KEEHfgjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=p9cfUxdsT5kiqt9RnqXR2_DlfpyKzrdcapghQ_9W5lt5pQcbO68VygWZBmVWlmcG5__A1w_WGx7ea6ba7i1BLh4Ix0Vp-UeH_kKfr4h5YKX0TlOVAAssoObnZuJzXNhnVuQf9tfJ4ZNex_fHmMkkH7TkHHtgIjYsecS7KLrCW8-yi3DQlw-5kyJnrcx-U0U4Nap35HVgQHiB1YXsDN6lw2kBR0EV8rSxBFMECJbiO2C98aKoctUPRavoMCdDabpqVSED6bOjKfcwXO6dCo0hZsKM1wM12tMGcibdynFhF8Uk0FWWbhm16WgSQTAAhSgVQFCrkI_ZXVRcT8KEEHfgjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=kMiyVbMzkx4QDkZFgArq9UWQyI61aoE2W7T44LokPLv0aBqIJQKiPjxGQHnaDhBo-jkdLfgtTWEzaz1rig1A1IKiM_linPWmRjqD3TwHRBWBigAvL_L2N1arRWXkSnjehEb1qGxHWzpYwJLrwPYEs7h-sTZLgze-WjWruUkhyyChdm45c2xFRrOT0LPKd3hEecp72IrYIE5IGeF1sAlxsnYk6XyjLic9LOvXOt2BkCxzbTGNgXbVBhFV0HxU77gAZmTj06wwCjiwlj8u5oAjt9_dCAb77dSrtugayK-6omIFEKtflD9jCu_Rh1RlupYQhpVGKu3mRBT0apd1476KRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=kMiyVbMzkx4QDkZFgArq9UWQyI61aoE2W7T44LokPLv0aBqIJQKiPjxGQHnaDhBo-jkdLfgtTWEzaz1rig1A1IKiM_linPWmRjqD3TwHRBWBigAvL_L2N1arRWXkSnjehEb1qGxHWzpYwJLrwPYEs7h-sTZLgze-WjWruUkhyyChdm45c2xFRrOT0LPKd3hEecp72IrYIE5IGeF1sAlxsnYk6XyjLic9LOvXOt2BkCxzbTGNgXbVBhFV0HxU77gAZmTj06wwCjiwlj8u5oAjt9_dCAb77dSrtugayK-6omIFEKtflD9jCu_Rh1RlupYQhpVGKu3mRBT0apd1476KRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIU5sESiscubGZ9MGkVGOGb1W2O3V6d8jIESxM3uL7zkdSWiRX5hasaKJBq68Sca9HrZQL0i-VfKhXd7bFOe7d6LmZKJ1aYlMo_n3Nvvt7-YvkQUI-qMX6WIgIvzyARhLcQBE7Tl9grG_RgwxVtu02qiCngnFECw8aQ7H3EUvIUshsSP4aoL98veOzq501wrowo29SO6b0C_b5-urh2meAW23mZgfX0u1MXSBuUE6KNSMeXt8VNJPTcVgveF5Rv8okVcsVCbccCXIa9VZhfx3qtWEno_4f7fA4-l2KuJ-yAzvX3BNgFoY1UGoHew0ST4qJlrhpE-_woBphVr5NLjHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=TIx9GtMF0uM9wBYRfAePFQmWoeeCtNPSvVINpUpTG3mo5AHxBcGHrunZWDL1807IJ1L2Y2cnMsiHta7HP6eeMcV1cWuYt_JNYQ3xTT20JZRjgEo5Vwj5NnGSIjSJ7BI03IAAXDEHoWyn88OclvoI8oKNcXyiBg1xLC9h5qO4mO5LePiQe034pZIxd5t6GJ6F5CQOkz3LRyqhhy3QAINjkmMN2OwQQ0DxNFUh5rN_LswK35gksN0WlRPQrY88-meIuRfg7R1OoOpRmrDrLYE9vgZGNheXPxoKXrEYe5OXMKgNS-FWRHAXtwqGeQM_vPnD2eLN2cgVyx_hRWPLWokZoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=TIx9GtMF0uM9wBYRfAePFQmWoeeCtNPSvVINpUpTG3mo5AHxBcGHrunZWDL1807IJ1L2Y2cnMsiHta7HP6eeMcV1cWuYt_JNYQ3xTT20JZRjgEo5Vwj5NnGSIjSJ7BI03IAAXDEHoWyn88OclvoI8oKNcXyiBg1xLC9h5qO4mO5LePiQe034pZIxd5t6GJ6F5CQOkz3LRyqhhy3QAINjkmMN2OwQQ0DxNFUh5rN_LswK35gksN0WlRPQrY88-meIuRfg7R1OoOpRmrDrLYE9vgZGNheXPxoKXrEYe5OXMKgNS-FWRHAXtwqGeQM_vPnD2eLN2cgVyx_hRWPLWokZoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=PtBFIKXSfIGPCHurTTAX-w2-ZH0IFW8TVZU4xoD_7xLgbGDOBTs530-pGFpxUDOn7DqcQeDgvgv5VPk5Bk7-VXoroNpicKWY1W6FzlJjxlxJli0x8SAi1oCrPWbpqv2hyvGpzrRIE74RRShmCyu8jae_IMgkdvqzY6XiJbB_7nNf3zLPOEE_yCcNFOr3wdu26ExKFzpnCUB6WX9P0ZULmDR6v4Mz0munzI7GF2DrvCpZvjJ8h-99wWZ5f-cQ31OPMneOUc1RDr8EYPtaxrkwreOV5ZwR92_c0cLFc2XLLMPxr3u1qIEwvsq76hpQOtGVKm0h5ZeuawAd4rqu2orRYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=PtBFIKXSfIGPCHurTTAX-w2-ZH0IFW8TVZU4xoD_7xLgbGDOBTs530-pGFpxUDOn7DqcQeDgvgv5VPk5Bk7-VXoroNpicKWY1W6FzlJjxlxJli0x8SAi1oCrPWbpqv2hyvGpzrRIE74RRShmCyu8jae_IMgkdvqzY6XiJbB_7nNf3zLPOEE_yCcNFOr3wdu26ExKFzpnCUB6WX9P0ZULmDR6v4Mz0munzI7GF2DrvCpZvjJ8h-99wWZ5f-cQ31OPMneOUc1RDr8EYPtaxrkwreOV5ZwR92_c0cLFc2XLLMPxr3u1qIEwvsq76hpQOtGVKm0h5ZeuawAd4rqu2orRYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=VU0zoY7xqnrp8_u3KxOG7m7aNXEvbAz9-hN4Kl70J6qtEjG41IZaYSI8O3ch5lukM49Lx96os72CDJkaKhb2qrYJlT0z6w3enxAZQFfU0eB9-Yc3yfsQdRnutk4CsiLs9EZeI4OEZNAnpC2qbzNSFGzLrKw4zxueUOV8989ROU5huZm8QDEu5wKi2hMuYlCxvwhPwJ9yyjGc4_QJfVUA3Z9XuzsVMpHznMY18hDQbrqhhnE3no2pAo7bAeGWGCED8yAiPmapXKfmKsf1aQrAXCZWZZ_57lt55ctqieeMddxxrpVVAFiIQJqlxayjQU2u9w0YTZU21ErlMs5LXYH_kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=VU0zoY7xqnrp8_u3KxOG7m7aNXEvbAz9-hN4Kl70J6qtEjG41IZaYSI8O3ch5lukM49Lx96os72CDJkaKhb2qrYJlT0z6w3enxAZQFfU0eB9-Yc3yfsQdRnutk4CsiLs9EZeI4OEZNAnpC2qbzNSFGzLrKw4zxueUOV8989ROU5huZm8QDEu5wKi2hMuYlCxvwhPwJ9yyjGc4_QJfVUA3Z9XuzsVMpHznMY18hDQbrqhhnE3no2pAo7bAeGWGCED8yAiPmapXKfmKsf1aQrAXCZWZZ_57lt55ctqieeMddxxrpVVAFiIQJqlxayjQU2u9w0YTZU21ErlMs5LXYH_kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNsPYGZ0qvEJfuL9Z4J5N1VHys0RiZdUrqdWm8bGwSZNU03sND2ojuxXl1sHTTNoWRS6gRYB2ANuYFtB2R-dvRpUCBVr91dGBwZBfNQi-IN2lWDJ4rqXTvJugZR5WrD6g2vxT-cSUB733sBfEFwwBXBO5tDAzi8dmHa2cE244Igp-kcrbCg_X6ezBruOmcHKl1-6KoTf_vxNeMvs1sr7IilNPTp3wABVo1Yz-0kjo0nq35sU8fYP-JMdgR19hWSpQRGpH3E2GUWNm3LN94S3cHESndtySP7r3iccWFPkhRshLdwwHEU2JmsHBj8REOaYQ-m_1UJUAQ2dRnW6mvExeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=scsHI69FWTP38112lY-1vM4hFjB_eWdTGEJxkggkDptuytf09vYuhxtMo37XIYX6xnS5LPeKL2H1ZW0HOYBzy-29dPQCIv-A2hVNops2K0oWAQIscxQiS7c1Begw-KWk2ZnjH0lPhOvoNton93SEcOd7oNBZ6SUICfzgjM1GsbZz_VT73k4YhW0S-lkMQ9tNVQhL4SVsJmF8sQqky9VeVsZdeD3l3RIHtsNYwEKqgreILSml8gFUU50TccFyoVjMNnuBt-6SessAh0DVI39IQaQGgMGu9vXL2OJJNXG4fs_i2iCJkl74jDWWh3Z2z0YNudmd14Nx7BeqrfqMtbslZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=scsHI69FWTP38112lY-1vM4hFjB_eWdTGEJxkggkDptuytf09vYuhxtMo37XIYX6xnS5LPeKL2H1ZW0HOYBzy-29dPQCIv-A2hVNops2K0oWAQIscxQiS7c1Begw-KWk2ZnjH0lPhOvoNton93SEcOd7oNBZ6SUICfzgjM1GsbZz_VT73k4YhW0S-lkMQ9tNVQhL4SVsJmF8sQqky9VeVsZdeD3l3RIHtsNYwEKqgreILSml8gFUU50TccFyoVjMNnuBt-6SessAh0DVI39IQaQGgMGu9vXL2OJJNXG4fs_i2iCJkl74jDWWh3Z2z0YNudmd14Nx7BeqrfqMtbslZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFSD8hk0SPUT_sPXJxWN9Hu2kHPNekOcObfh292lGouXHQa8YXNNx0-yBeP4dIdwQ-Zhg0ZzdgNSc2qGdF9OLWEPpsbP2ntdid0CJyDbVf4tqyO9n_R1wnJIvGePHwYLcpvBgXT2lD520oZXbwRq83tsH-zXZObraNa3fV91Xf6ZN8U7nZPZ6YuR_DtzBABNLvOE5JmMe9ZcEp1VFpFKXL6GJ7IT2_amSjtTiAU5JcUI9TFXL2vWli0yqyHn-UWHvV1kXbLBkUTiSnB0EryQl88oGawBH61JaeFreiC4uUG6IMCKYVoIeMvEOa30X3FO9hxpjkyYEyCLv40m4yc4dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI93XwmUHQz8F0VwSVpQ_MYR2y1_0btBCdJurLf78NgSLp4Y8cmEyArf1c31PTExE8tP_MDDHI1-cZaQIVMgayOlMxd3a6Tya4pryFNqx2d4j6OxqWA6BVSxDVL6lTPo88-B78sXQ2sqW9UdysXPTZL58NkWT82ZygbR3ZIismIaXV_Um0Ff5tjyIdYm9Z867hXfBJKBe1rASdIOuxG3lBhp875jarU3WG5qGygYpsdsZVZ0fEaMB600qDWJm3fMrfuz2BILj3CSV9TgarNsRYWnMENetrMEPFKsPNx83pqjIqbFX2ondQznMxI0ye__dPYcBSbzQDh5cpmTgD078A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=lBQNOXrM-zz8LxfJwVvUb8-beXPIzD8tmUPMDY9ECuFlRv4N7y3cuSPnTwPH88HSk0OvfF2riK7zZf_fnzBnUtE-CBvRc2g2Yh70Im4_jDyWxgzW-26BIBHKjJwfgEeQd3eaVSaPcPBYbIsFxDEoUR1bQ-SJyHBByMQPWddjNm3c4X6O2SXKVPlkeaaBXLK6v9650lr04dAaHfNafN_6p_nu5QKjdlr8RRiFCcBontpe3tWuTgnYERqIiM4I06W_bJT2B1GJe_v8Av7VyYM9f0VlEekTUEj6AHbGjlCRVxxw2jbiF-qvARAFPN4Xi7t_I46dPsEpLa4avkXJ8bPG4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=lBQNOXrM-zz8LxfJwVvUb8-beXPIzD8tmUPMDY9ECuFlRv4N7y3cuSPnTwPH88HSk0OvfF2riK7zZf_fnzBnUtE-CBvRc2g2Yh70Im4_jDyWxgzW-26BIBHKjJwfgEeQd3eaVSaPcPBYbIsFxDEoUR1bQ-SJyHBByMQPWddjNm3c4X6O2SXKVPlkeaaBXLK6v9650lr04dAaHfNafN_6p_nu5QKjdlr8RRiFCcBontpe3tWuTgnYERqIiM4I06W_bJT2B1GJe_v8Av7VyYM9f0VlEekTUEj6AHbGjlCRVxxw2jbiF-qvARAFPN4Xi7t_I46dPsEpLa4avkXJ8bPG4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0hgVuu-JJM4UCIsY21Y4SEg1sUm4QYJAgWjVJaIBwS_Nvp_Z6iszEbEZ1XBNxxRzBSQjsRdW9w_Wc3r_xmW6I2IkIT6swSDVuuoPCmzsPt7b81sozDMn0m-xuytss_GyJM9zmYaO5go7NI4pmNzMUDJ3X06SsU7lg4OLvg08b8ZoSbaBCOIq7BoYRh8LU2RRfRnFiMaanjwXjJGYnuSTDePjXeHvt_kSFf38HHalgbAI6B_UL9b8FRKyHiTGPzV0nUgaeELnTUGoocKEL7UN6xf96J-Szx-6vpuks-net8OaZnf0Un5xbO8M9MzRArlykymbqPXu0cLg7VTx3F9ychg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0hgVuu-JJM4UCIsY21Y4SEg1sUm4QYJAgWjVJaIBwS_Nvp_Z6iszEbEZ1XBNxxRzBSQjsRdW9w_Wc3r_xmW6I2IkIT6swSDVuuoPCmzsPt7b81sozDMn0m-xuytss_GyJM9zmYaO5go7NI4pmNzMUDJ3X06SsU7lg4OLvg08b8ZoSbaBCOIq7BoYRh8LU2RRfRnFiMaanjwXjJGYnuSTDePjXeHvt_kSFf38HHalgbAI6B_UL9b8FRKyHiTGPzV0nUgaeELnTUGoocKEL7UN6xf96J-Szx-6vpuks-net8OaZnf0Un5xbO8M9MzRArlykymbqPXu0cLg7VTx3F9ychg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=QCRxX0UXC_TNrvSD0U8sBQM6ihna7W6IBji4BCaQia3APBtpG7J6NSzEw3kH4m8516O46sskJ9rYOgJKy0Oksb_LsHlJYUKHR0I1UO5fGHE3ZlfdXmhToHPlo4_dNdpp8VHcC6QyhihcFFhOC5Q80j2q_LSbUbDP_BalZmZ55dTSDYWKCLkS-60NK_4WQzKavHYuegm5kshyDqwu_HGI_SrIqA7ICxUzuGAgrIBjBGe74PjTkU4PLDCGBIeU8n13yRBAKD5RX5WDT_PoOP7_uY6O--HOTClMm9eKlVgua9-aIMcTzyho8PlyfPcH883QbouJBpHFqH640jnCC2mTQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=QCRxX0UXC_TNrvSD0U8sBQM6ihna7W6IBji4BCaQia3APBtpG7J6NSzEw3kH4m8516O46sskJ9rYOgJKy0Oksb_LsHlJYUKHR0I1UO5fGHE3ZlfdXmhToHPlo4_dNdpp8VHcC6QyhihcFFhOC5Q80j2q_LSbUbDP_BalZmZ55dTSDYWKCLkS-60NK_4WQzKavHYuegm5kshyDqwu_HGI_SrIqA7ICxUzuGAgrIBjBGe74PjTkU4PLDCGBIeU8n13yRBAKD5RX5WDT_PoOP7_uY6O--HOTClMm9eKlVgua9-aIMcTzyho8PlyfPcH883QbouJBpHFqH640jnCC2mTQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOUwgshc2GYwfYF_S55KMcJRl_prRBm5dkXKIEhb0OZ8qCsu4VhCYNsIswxKZTRRxj9Wlj8eEozPjE6zntPEaoIpB85kgcw7HTRL_q5OhS8ZONl4FkFhQ2i1f1gNHpt1N_VBAViqCt2XExpv5EdCXWGXXXjtZewU79AhZVaykXjZ4z7yLDogNtAn7xgKScO5nSbJCHwYGdWOMrpmeFiH6IhUl48noyy8J4aqUyPFM6KuUboWE3ly71qRp408lCv3HSZKkgfEarSVeFjJNy4Yxd8SSnw_MfTXic9bIKsljFY9d-N1xO1pweZUC9uSMG_b_212fwdGERUfr2KUdiwM6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=df4hajTp7g-CNDvOPPp3aZ9-gwQUsBinsreTEyShLHcDD-HMox2d5d7EBV3e-NTqOX9J7LQa0RPAJZyiH8vbD5P5bqvYIMdZ-OkO1tB5MAV65tn_6V3ZgyguLtmvJ3oQf3ik7Ob4Gj-imqaT--qauLDBqnRyWAgVn3AgNiDB4g2RYBGRGBTiybytpJvh_kTIp4RXHrfXWA0HOsDBt13gBDWoiht-_w_68CHkAIwAnH-eNvZbE89pJgQmvuLXfnixwvM_HAYz38kUeastKelf_ew86VX9BUvTSiVlsSi7cKI-ouAaKU5aQd-2FtkkbmZYFcJvF6pQTGMg6VORqQLn7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=df4hajTp7g-CNDvOPPp3aZ9-gwQUsBinsreTEyShLHcDD-HMox2d5d7EBV3e-NTqOX9J7LQa0RPAJZyiH8vbD5P5bqvYIMdZ-OkO1tB5MAV65tn_6V3ZgyguLtmvJ3oQf3ik7Ob4Gj-imqaT--qauLDBqnRyWAgVn3AgNiDB4g2RYBGRGBTiybytpJvh_kTIp4RXHrfXWA0HOsDBt13gBDWoiht-_w_68CHkAIwAnH-eNvZbE89pJgQmvuLXfnixwvM_HAYz38kUeastKelf_ew86VX9BUvTSiVlsSi7cKI-ouAaKU5aQd-2FtkkbmZYFcJvF6pQTGMg6VORqQLn7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=eGEHFC8J9Q7YyJe6mrxUEJ-sHtD1-mqsCgqQIunNuSsMvLpun0eLayZkyvIqnteyn6UBM0SDblyH4G7OPCLCk_yLtDz_Fz2Lt5cAzuAocx6bsmMU7j6BbMIIJTHLyRbS67xez88-6EgpHaNW9H2D4_XntW1nIl12eRnly7dAsMvlt43898lvglgg1k5ke_7fmXe79QwJF0OU07uzpIxwZ_BwHo3PI0_qogGc1s-4MDfZwP73BDAayuEDwl2lLEglJau8K3-N1N372t2K3RGUH9N3lykO4iBrRDXqwaLj14_uYjkZUv_amC4y7_n4E8hQXnpQiUyrOH05UNUqRqWXzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=eGEHFC8J9Q7YyJe6mrxUEJ-sHtD1-mqsCgqQIunNuSsMvLpun0eLayZkyvIqnteyn6UBM0SDblyH4G7OPCLCk_yLtDz_Fz2Lt5cAzuAocx6bsmMU7j6BbMIIJTHLyRbS67xez88-6EgpHaNW9H2D4_XntW1nIl12eRnly7dAsMvlt43898lvglgg1k5ke_7fmXe79QwJF0OU07uzpIxwZ_BwHo3PI0_qogGc1s-4MDfZwP73BDAayuEDwl2lLEglJau8K3-N1N372t2K3RGUH9N3lykO4iBrRDXqwaLj14_uYjkZUv_amC4y7_n4E8hQXnpQiUyrOH05UNUqRqWXzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=ReIdWn3vn1Uj4GmZ5T3XmZ2vvODXnjJ4fvg8EnV91AZCygvDa-3RZRqrrkd05NvMDcYXbiVYJhNI4FwbhpUzEqZ2gUmiZFfvlXPWIOm-E_yVL5D4EItxVIkUbzAWbaFyYLG1umUtsZfJqQBgcPO-kev8Dfods8jFPbZuxKK4XZpyf6nt-8W-_J84SP7tuz6f1hF2EpdAb8aS6VIh6eVp-Drltj2TDyio7mHGBhzK5JxYgRMtnIcnNorAZyjN7fKpj1VE1Vp2hMRCP_5WUavGJA2qOLvhMUGr8zzJOGah2gq9nzeuicC90H6MxBJGM_fHjhJW2PqPhVMoRlHjXJ7z3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=ReIdWn3vn1Uj4GmZ5T3XmZ2vvODXnjJ4fvg8EnV91AZCygvDa-3RZRqrrkd05NvMDcYXbiVYJhNI4FwbhpUzEqZ2gUmiZFfvlXPWIOm-E_yVL5D4EItxVIkUbzAWbaFyYLG1umUtsZfJqQBgcPO-kev8Dfods8jFPbZuxKK4XZpyf6nt-8W-_J84SP7tuz6f1hF2EpdAb8aS6VIh6eVp-Drltj2TDyio7mHGBhzK5JxYgRMtnIcnNorAZyjN7fKpj1VE1Vp2hMRCP_5WUavGJA2qOLvhMUGr8zzJOGah2gq9nzeuicC90H6MxBJGM_fHjhJW2PqPhVMoRlHjXJ7z3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=vVYoITGJm-1Yuaw3d39aNI9F77XwK3MYh-6Q5p1OMf6Q9K9UAB6ZzRIPWpX0H9NkwpJ7u3wz3jxmGi9FLhBVw-YFypGy7Hubzxcoai-9-YgfSg8y1-68nDN01FrLJTHnLrqcpbfzq_a6NXrXpJBjJtwRK66ZXlIi0GoMktM9SL0aZT7T-fJ08LVOh-I-SYvxO2SLIEeBdrdgoTI44t02H9kYRlaZcc2yOiXKDLF6uaQddXjHTxY0IWyICpNrnMmm9OhxBTY_IJK6mtn-eAr-x2lfrQb3cfxWA_orFyXs_t9phus1Lczyaq8khMpBjTjgQ15NLF4oZrdyYmBYaPJv5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=vVYoITGJm-1Yuaw3d39aNI9F77XwK3MYh-6Q5p1OMf6Q9K9UAB6ZzRIPWpX0H9NkwpJ7u3wz3jxmGi9FLhBVw-YFypGy7Hubzxcoai-9-YgfSg8y1-68nDN01FrLJTHnLrqcpbfzq_a6NXrXpJBjJtwRK66ZXlIi0GoMktM9SL0aZT7T-fJ08LVOh-I-SYvxO2SLIEeBdrdgoTI44t02H9kYRlaZcc2yOiXKDLF6uaQddXjHTxY0IWyICpNrnMmm9OhxBTY_IJK6mtn-eAr-x2lfrQb3cfxWA_orFyXs_t9phus1Lczyaq8khMpBjTjgQ15NLF4oZrdyYmBYaPJv5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duDDolTaVZxwXexLJurPUblwjZGqTX7w_7f_YWk9Dcxp7DdDaAML0iPNmaJqi0EQn6h9tH9wYG9h6xnY9XTRDFQzavV-V0l0a46p0zT72Bw2mmhlQ3AgSQljn0JJQoN9g2o6cKmbJ-g8QYhFWnKn8djMynVocYBprr1XRHM3KM706Aq4eO1do8ECW1pxCfCyfYkodlW-ghhYcc3bBqtK_yuDabaBaCYGBZnfOtESXNlg2Exq8M5iu3sv7qv0iALrMd7SL0lrU53qOEl_qijg_Oxsnzj4jx48pgc3aYnMD9ZYxgSrO1xkbUkZ0wqnn2h_Cr4spGWo9UX73DE8NNLo-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نبیه بری» دبیر کل حزب امله
همون حزبی است که «موسی صدر»
در لبنان راه اندازی کرده،
همون حزبی که جمهوری اسلامی رفت دو شقه‌‌‌اش کرد
و از دلش، گروه تروریستی حزب‌الله رو ایجاد کرد و باعث یک جنگ حدود دو ساله بین شیعیان لبنان شد.
یعنی روی هم اسلحه کشیدن!
سوریه در زمان حافظ اسد حامی شیعیان امل شد، و جمهوری اسلامی حامی حزب‌الله لبنان.
سایه یکدیگر رو هم با تیر میزدن! برای سال‌های طولانی!
حزب امل، از زمان سقوط رژیم اسد یتیم شده.
جمهوری اسلامی ماهانه حدود ۵۰۰ هزار دلار به نبیه بری پول میده. میشه سالی حدود ۶ میلیون دلار، مه در برابر حدود یک میلیارد دلاری که به حزب الله میده تقریبا هیچه! اما همین ۶ میلیون دلار امورات نبیه بری رو میگذرونه، که در چنین روزهایی دهان باز کنه و به سود جمهوری اسلامی حرف بزنه! بعد از ۳۰ سال دشمنی!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=dII4I906ujMlMxvzEC2PuUKFnZjiYyueCFV34ZVTByP30dJ_14HF_0n-1_YqpYO3-Odc4FzY97BS4IFvMjfbD96vH8dS2_ZHk1CMwyq9mGjERocjGNYX0M8IGLqDoKRABhPZEIvVwPSACps1JDq9LspfmyFKkgb7I5uoXIC0bGvTcMJ2Pes8CctV8fav1NCqIGqfU6VU5TpTAhgppeVk47KDuz6G3-xXJRCzN5s9eZkHayr20bzguUd5PriCjdZwQkqgrWiwSaHsnW-q1XPMfLd09VYW_Jeku-PFQueT9Oj892r5hOqQ2tdf_OIfwdD8bBBYRJuhls_mreHU2oPQWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=dII4I906ujMlMxvzEC2PuUKFnZjiYyueCFV34ZVTByP30dJ_14HF_0n-1_YqpYO3-Odc4FzY97BS4IFvMjfbD96vH8dS2_ZHk1CMwyq9mGjERocjGNYX0M8IGLqDoKRABhPZEIvVwPSACps1JDq9LspfmyFKkgb7I5uoXIC0bGvTcMJ2Pes8CctV8fav1NCqIGqfU6VU5TpTAhgppeVk47KDuz6G3-xXJRCzN5s9eZkHayr20bzguUd5PriCjdZwQkqgrWiwSaHsnW-q1XPMfLd09VYW_Jeku-PFQueT9Oj892r5hOqQ2tdf_OIfwdD8bBBYRJuhls_mreHU2oPQWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=NUi6OifItMhI4zlrMpm6OK-gogLBZvb0lN9mOoMKNUEUZuRDrMWOdI2XOQlDTqODZnQR8VXtvwPjJKRSCvj2T5pgyCbqwdAGfvyHvjoX4AgQgkwEzHnXb2trXlUd-9NduFG49Y-B7OPD9-jj2IgkSEQ-zABN_ogt9X3kDOBglJpSMPa-91ENuZhVd6dmyiAo9iqxJb1pVm1ET2Nubygkq2i-uJya9Hfnym3Up8SCdG61qxjhE-HTEsNbkB8-T_mM_9SQSrLIfnIK6hsXvEuO-derWSP1QLbp7_s8bYMN_d2pVVjau6anwm1cX_5hbjUTfICRVA-95mcC3hvsE1TiBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=NUi6OifItMhI4zlrMpm6OK-gogLBZvb0lN9mOoMKNUEUZuRDrMWOdI2XOQlDTqODZnQR8VXtvwPjJKRSCvj2T5pgyCbqwdAGfvyHvjoX4AgQgkwEzHnXb2trXlUd-9NduFG49Y-B7OPD9-jj2IgkSEQ-zABN_ogt9X3kDOBglJpSMPa-91ENuZhVd6dmyiAo9iqxJb1pVm1ET2Nubygkq2i-uJya9Hfnym3Up8SCdG61qxjhE-HTEsNbkB8-T_mM_9SQSrLIfnIK6hsXvEuO-derWSP1QLbp7_s8bYMN_d2pVVjau6anwm1cX_5hbjUTfICRVA-95mcC3hvsE1TiBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tri8orx9d8UJKFpADV5lT2OAPVO0kGpQGDSdwDCpK2W12OGzE3jGR2Z_-oBzCS6oSP98XmLkQYpcbXddNa_mwENrm4rBrfZX_aqzUat91CUcyPrv96_gmmXXb1oyTl0bQGYNZI8JnKKv6d7HyMj28w3DpwxHLsy2ooGCOX2qsIOLd01aJTSHvcK-in0NomaVQHqiZ1bYe6j0mnTSYCetrA43w-pOigeVuFOQ-hUSH4hcOAfR7kpqjnvbg5ywFGWwuQ8bm01Q9KCsy2yD25GSGsoI9V6EvOtdUtbvLueTvWolvkxlbGEUePA3UUDi0NeIB1jWo8ZISIs796V7pLaDLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=SDHoDoiA-oF8cQ5viKPGoLV-BL_EXGZbo2sUfQnDMxh3yj4q906vUOXYuDULD3uxXNDaz3Lxu38BorGx_9Xk0_8UKSdY6ATPfXUsHXzKxjdffNwHzdgmIMMj3mnMHlXz-cLJIKdyDahLTv4eKarx1N0e6lyig82BSCp5CGFjBxideynH5yaciWS-3kpiL8TYkvLY7J7tiNvo0xPOxlOGvipEafH7fTWErIgDST4-tJrdw3Q1T5vxO82q0D250v1l5JRP3GP4EHSUxZ-dyeV52VcKC7MIR5lVsDLI6tVHz63-OrtW6JCEE_2b0hRAEL9m8izkw_oPiCR2VHzrd1A6KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=SDHoDoiA-oF8cQ5viKPGoLV-BL_EXGZbo2sUfQnDMxh3yj4q906vUOXYuDULD3uxXNDaz3Lxu38BorGx_9Xk0_8UKSdY6ATPfXUsHXzKxjdffNwHzdgmIMMj3mnMHlXz-cLJIKdyDahLTv4eKarx1N0e6lyig82BSCp5CGFjBxideynH5yaciWS-3kpiL8TYkvLY7J7tiNvo0xPOxlOGvipEafH7fTWErIgDST4-tJrdw3Q1T5vxO82q0D250v1l5JRP3GP4EHSUxZ-dyeV52VcKC7MIR5lVsDLI6tVHz63-OrtW6JCEE_2b0hRAEL9m8izkw_oPiCR2VHzrd1A6KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=mNcrpnFDuTxOJMEla39CEwjBq7fb5GvBHyWq6UWAvBMjYedsdw106qR8XAxBEF1A56Q0HDL5ayV1IRHMI5lV2qJR8h4NsCIzmCIDKYpTlYbq_4pskl_qYgkOka_-ilN0fmpg-YO4Fv0-FE4Vyxjo8SD9R-rcDwhUPEmtGPuw6xGWOUCbBzGkPVHODx7WloArRBis2imD68m2Glo1WW8Z4xc4aEx5QgHamiG8M_UFru9kv-Ps_RcoBiS8FfTxp0z1iOHXrRpeJxUgFvNI_mGRbNsvSXKbDyYJ8BIVIq08sfrJM3hVo_2ps_eoRT659Y0RQwmvoih0N2BN8e2S1ijxqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=mNcrpnFDuTxOJMEla39CEwjBq7fb5GvBHyWq6UWAvBMjYedsdw106qR8XAxBEF1A56Q0HDL5ayV1IRHMI5lV2qJR8h4NsCIzmCIDKYpTlYbq_4pskl_qYgkOka_-ilN0fmpg-YO4Fv0-FE4Vyxjo8SD9R-rcDwhUPEmtGPuw6xGWOUCbBzGkPVHODx7WloArRBis2imD68m2Glo1WW8Z4xc4aEx5QgHamiG8M_UFru9kv-Ps_RcoBiS8FfTxp0z1iOHXrRpeJxUgFvNI_mGRbNsvSXKbDyYJ8BIVIq08sfrJM3hVo_2ps_eoRT659Y0RQwmvoih0N2BN8e2S1ijxqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=q-te0ne0kT2LLkX1bZwfY6u2BwTUrBTX2Dd9nlWog_4FLe9US8_cjFr8QWnCB-eSE7EQFFG4m-4TIka1-UqVPywbfYcL9D5Vruyx8_TQBTcwqLYPCJrSTmTyj3Oh1En6mnpnWsBopvHhLIOISgsMKOT2EmSbPj6FkAqz7xMLaxis8jxo-b6o7Eh2amofi4LJvrqCZ2a8BnBVIOv-6Gr6FQbn4M8QOalCK6sg-0FB_Yy7FNtZ5lKwPtIRu0Pr55tWkchpgDqTAFFX2rAZxqqas2MPSqb48zAKsaAIIpld7NUCr0g9kn5yFhR8DTrCpDlKtLI1nOOyYYvBe_7IawA2uTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=q-te0ne0kT2LLkX1bZwfY6u2BwTUrBTX2Dd9nlWog_4FLe9US8_cjFr8QWnCB-eSE7EQFFG4m-4TIka1-UqVPywbfYcL9D5Vruyx8_TQBTcwqLYPCJrSTmTyj3Oh1En6mnpnWsBopvHhLIOISgsMKOT2EmSbPj6FkAqz7xMLaxis8jxo-b6o7Eh2amofi4LJvrqCZ2a8BnBVIOv-6Gr6FQbn4M8QOalCK6sg-0FB_Yy7FNtZ5lKwPtIRu0Pr55tWkchpgDqTAFFX2rAZxqqas2MPSqb48zAKsaAIIpld7NUCr0g9kn5yFhR8DTrCpDlKtLI1nOOyYYvBe_7IawA2uTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sv1ea-aXEBaqFC3usdftjPmXmH3NczER3NdpQg9ieWiV-9k66niyBvd_91H8sfjZFsR5_YFzyMwLDTnlN7kETx4bj-TXYkPGl_dM1qucva0EfTfmeo4vxCLG-F3jt2T2cH5DfKMWTNYcga0Z3g_FVmPC2IzAfBH1MpuqBaT7vV0t09jQDnhWqF8a1me0VkPCDyOeEKspWpORZzL2WX1C7xuhsethsRXPEk5XrCM1NjBl-n97VTm7K3UZZ7fJa5MQGaMfcYdmjmvDlAtuvX5DXchuiTor_fnMcenMT-aiOQmHcwxVXpOqIiAW5PY2022ApaU8XdwHKTMDuZJi9beMBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K63HkEwIVGGV9EAeoprkimL0mujEayLHzsDKs_y8GEB9y-rnx63_OUYfHTYLDpdVA3dafxIC3FIHIh69qkqrjXMvK639RQon3yHSpnl5tVV2BR5vLzQMCevPQoCtR6M3pT80D9YeRlEARHAqT7F8Ud_kT-AX_XUL8dLuCmJLwj3JRXW8wmmjZBtjC_iEfl3KrOYZSTQQYJg72E2iYU7-QaaLKGtvUjVJvia0FxA8oa8WK_sMEzxzrT7VO-8rQqB0s5L-rWXYsEUk0PHpCfXJdSzkGJRvlDQEG7AgxIxWEguZNKTPhMytQ9V9qhPWGJ6riJRPDHqkkI0hS_G3SwAG0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IdYmieIOD1rXGmApls5CmAaIXOFm0YuWKgj5XAvVnDu4YYp8SP6DhV6sk9TmsFkLls6ksREVfD8xyzCANPXEjjbftBgSvuBMI3lBCZhoSmsrQViAJb0CkN7SsaL8wH7UfMaS_pWbVRHy12QB8rDy5v-TjKO2QSUUb4jQXTtpvORMlzLRW05zYCX0BRZ2NYBYE9NdOqXMNJOD4NFVYB4rnuOi-uAHUJMcYe8Ibl4RO7rM95TxmR6FlKvc8pQYm8XPIUqs2g8-oeq7mWMtnjbqVe_bUZcgSty8dY5_DMKP1wVLyqg2rMknF1U6LA9TKTJTGOQBnGQp2MVP7J4ESZ3LFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=u3fAMWQgu8rZRbSBIU4gc_l2jYZuSGW60De9T3i0Wd7cf4JHa-IZqg0p3LMscM739cbgAABghGl4qLhW9aMs6Fy3rB5WxFif4aLMtn8ukaDABtZbo7xeU72XtDWu65QzWUi6BsVFew3IA9qUoo_ko_cW-psYcv_Z6Z9XXX0mD0eqPaJNMJWcioCObu6IbizmdTwhs4vOhttFJnGjyhMsr3-1aw_0Wq9U1uHBp2Toi1wTMj5yP3Mpgd7rSrbB7QK2YPwGyaGJvbex_N9ToZi7paMYrCeRUk5tWJEJQIH54e1biS1yOPdV1m52gVaKeG5gI_-qS0mcmmIin4fbUbTIkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=u3fAMWQgu8rZRbSBIU4gc_l2jYZuSGW60De9T3i0Wd7cf4JHa-IZqg0p3LMscM739cbgAABghGl4qLhW9aMs6Fy3rB5WxFif4aLMtn8ukaDABtZbo7xeU72XtDWu65QzWUi6BsVFew3IA9qUoo_ko_cW-psYcv_Z6Z9XXX0mD0eqPaJNMJWcioCObu6IbizmdTwhs4vOhttFJnGjyhMsr3-1aw_0Wq9U1uHBp2Toi1wTMj5yP3Mpgd7rSrbB7QK2YPwGyaGJvbex_N9ToZi7paMYrCeRUk5tWJEJQIH54e1biS1yOPdV1m52gVaKeG5gI_-qS0mcmmIin4fbUbTIkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_53iG9AB4ig_EjnM7Ug_eXqbG3PGYQm6IvzTaFXAQtUEJADQuAspX3brec_UNfJ9hGkIXXdQyxnSRokUyG_xAbJ6cH5jcIOC_qEbYqLerA43wxf6y-EHjm4VvKNzRDineeBfcowbnsF9oonSckDB0vOdNAHqniCbb7HnPOP5cAIox3xoGLIXELcHM812ZEs4seHi8791rPCtQ1nVFIaTBQMpky-vvoIVfzWSIade_AxrhovYdw_WBcRYHj97-l1aDQUDjRFSih5im55-BGasDaTq_sptMv8f5TlhL3hUfS7cRXofqLlmxgXChaKS279qa37Y_tU4WKQGUzjVjDdJVSk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_53iG9AB4ig_EjnM7Ug_eXqbG3PGYQm6IvzTaFXAQtUEJADQuAspX3brec_UNfJ9hGkIXXdQyxnSRokUyG_xAbJ6cH5jcIOC_qEbYqLerA43wxf6y-EHjm4VvKNzRDineeBfcowbnsF9oonSckDB0vOdNAHqniCbb7HnPOP5cAIox3xoGLIXELcHM812ZEs4seHi8791rPCtQ1nVFIaTBQMpky-vvoIVfzWSIade_AxrhovYdw_WBcRYHj97-l1aDQUDjRFSih5im55-BGasDaTq_sptMv8f5TlhL3hUfS7cRXofqLlmxgXChaKS279qa37Y_tU4WKQGUzjVjDdJVSk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=XLlhZhSEhTbJakr5ruaBuE09hJqngKr5IY7F6NXA9MRyeNOQAvrAKVK3NbnOst7jqEZHoIThnYCRfFhoSe6l16zhrT3sHhJgYNxTtN0GYmc7I96deIOzFUgxMdXPrCHDzqm4zAM5anmEhZYe9r2j_-3UgjnSi620mhjVa6GQdLUHjbB0L_hmxnBOyZsV6aK_EmjYKZ1LLo27fPrKe07uZzDtdNXF5lj6Bg8vNILPOKX8JN_C0-UmhjhP5J6_x_aeAqW0nyb86LXugvKLdw6bn0G4xq7a5FXUX3hH6uLWVXNB1oymNEHy11Vv4IK-h0mNmc85QXtqdKlX4zjTCKQDKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=XLlhZhSEhTbJakr5ruaBuE09hJqngKr5IY7F6NXA9MRyeNOQAvrAKVK3NbnOst7jqEZHoIThnYCRfFhoSe6l16zhrT3sHhJgYNxTtN0GYmc7I96deIOzFUgxMdXPrCHDzqm4zAM5anmEhZYe9r2j_-3UgjnSi620mhjVa6GQdLUHjbB0L_hmxnBOyZsV6aK_EmjYKZ1LLo27fPrKe07uZzDtdNXF5lj6Bg8vNILPOKX8JN_C0-UmhjhP5J6_x_aeAqW0nyb86LXugvKLdw6bn0G4xq7a5FXUX3hH6uLWVXNB1oymNEHy11Vv4IK-h0mNmc85QXtqdKlX4zjTCKQDKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
حمله سپاه به بحرین و کویت
سپاه پاسداران اعلام کرده که در پی حملات شب گذشته ارتش آمریکا به تاسیسات نظامی جمهوری اسلامی در اطراف تنگه هرمز، به ۸ سایت نظامی آمریکا در بحرین و کویت حمله پهپادی و موشکی داشت.
🔺
سنتکام شب گذشته به ۱۰ هدف در اطراف تنگه هرمز حمله کرد.
فاکس نیوز این حملات را وسیع‌تر از حملات پریشب توصیف کرده.
🔺
سپاه گفته است که در روزهای آینده حملات بیشتری به پایگاه های آمریکا انجام خواهد داد و پایگاه‌های آمریکایی جهنم را تجربه خواهند کرد.
🔺
کویت و بحرین اعلام کردند که موشک‌‌ها و پهپادهای جمهوری اسلامی را رهگیری و منهدم کردند.
🔺
ترامپ در واکنشی به افزایش تنش‌ها گفت : شاید کار ایران را از طریق نظامی کامل کنیم و دیگر جمهوری اسلامی وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lr5mkmQBefp2MkCGYqnJ17w4g_x_GWBs7SQLTiYpkFb0fgR1itV3dXtOiibLLHQZxhXtmmIvSHrze-mflsIZcMC67BhF9FY4PMaQpeZH-a0qDSELCW-nOz8_mn2JdoEmyHUecT-vG4ZVzL9bzmvZU55IteMzIxNeiIN5y6jZmZJLwE8nRuP58ueMzKXc7EqqFZhkBhuBPcJfnvezFwWUPbee6dGbEwsv7gkyNTf2rSVPBxp1VjYuOVju-Gn8wRqKoCykt3HtY6kiKCuQGck3ct8IVYxzzkxq7mPx5bqCDTZrBy9eW8bU0ccQ-9MqtdDSr-qIT58GI5Bs2ULKOl6cAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTkcgrDzME67cW_XyVtLQGYaNhx46VeGMk9_GSOChrAY2puw_SsvyCgQeMkD4k9NaW3OvXZ4ZN_MoVghXpVOoNspP-M-d2hlmcZrLZ5Hf-pw9KNJdyqXgHliUf7WlzAeQMqHNvSwWFC34sUHyMYkzKmZRTSzwuKC7S7QfjUI1lg8SpDjsb_KUqZl2-tzZO2Ibdi2mlbLeEggSw9X7ouawizDI_5FkI2D9m3demnDGhG9mzw_XZA8Gev2vdvuxy0AqYuhSfR1oY1JtmUQO7qBuj-biBF__plIPSMMfZu50XgvtgoRFsG_-aezF1H1d2AgUF2Dm6d1TJ-Ybp9SABXP83cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTkcgrDzME67cW_XyVtLQGYaNhx46VeGMk9_GSOChrAY2puw_SsvyCgQeMkD4k9NaW3OvXZ4ZN_MoVghXpVOoNspP-M-d2hlmcZrLZ5Hf-pw9KNJdyqXgHliUf7WlzAeQMqHNvSwWFC34sUHyMYkzKmZRTSzwuKC7S7QfjUI1lg8SpDjsb_KUqZl2-tzZO2Ibdi2mlbLeEggSw9X7ouawizDI_5FkI2D9m3demnDGhG9mzw_XZA8Gev2vdvuxy0AqYuhSfR1oY1JtmUQO7qBuj-biBF__plIPSMMfZu50XgvtgoRFsG_-aezF1H1d2AgUF2Dm6d1TJ-Ybp9SABXP83cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGnNX_CzJokmx_HpvERwj3q5ixU3SNQIm5oy14ityvS33-JSIv92gZI9NjlZGczT9edCo9S6VipPWMJ_H7bXsf6FPkNb3FAjZMwjdVjTWqmKQY0alJbd2-_SbecdyzTXyr63ZQ6idDR1Fy2gvwiUhHemOZHMJeT0r_YUDpRmiZxRILemaEwdlPDX6oqZGzk215xL9IFaFFprTQnFt2xjeHGB5RTId10WVd-dePWVpKX_kyUJZBnlDv124KpfgdAxsHeRofaW5xAQGy9stI3Kzc9LoOZUL41dQ5XDRGuC1mvE7h344CL_u0uY5aSwYoa-1KGJtVrRHcJnR1QGfOsK4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">«ما و حزب‌الله لبنان تا ابد همسنگریم» !
خب ذوالفقارها!!
چرا آتش بس با اسرائیل رو گدایی میکنید؟
چرا «آتش‌بس» در لبنان رو به عنوان پیش شرط مذاکره با آمریکا اعلام می‌کنید! خب با اسرائیل مبارزه کنید! ببینیم این اسلحه‌ها رو کجاتون فرو میکنه!
در ایام جنگ قیافه مظلوم میگیرن  و کبوتران صلح میشن و دنبال آتش بس هستن! آی سازمان ملل کو! آی حقوق بشر کو!
و در ایام آتش بس یهو شروع میکنن به گنده گویی و شعار و تهدید!
همین جمع اسلحه به دست، همین‌ها! از جمله قاتلان فرزندان ایران در دیماه بودن، که حیدر حیدر کنان مردم ایران رو به خاک و خون کشیدن!
هم‌ایران و مردم ایران رو، هم‌ لبنان رو به گروگان گرفتن!
نتیجه سیاست‌هاشون در فلسطین و شعار اینکه مشت اونها رو موشک کردیم هم جز ویران کردن غزه و دادن ۷۰٪ خاک غزه به اسرائیل نبود! اصلا هم به روی خودشون نمیارن! کارکرد موشک‌هاشون در غزه چی بود؟ ثمره این سیاست‌ها چی بود؟ ثمره ۲۰ سال سیاست هسته‌ای در ایران چی بود؟؟
ثمره جنگ خونخواهی برای خامنه‌ای که در لبنان راه انداختن چی بود؟ جز کشته شدن ۴ هزار لبنانی و گدایی آتش بس؟؟</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=At5nw6g0u3_gvo22vaJ_n8PUKf50qhQ28hWU9ZGAN1nJ_P3XnOAEOt4czrLDFDMVCLNdOANt34e6wts_Ww37XXb6UtRWPGzLEgRES8oivI-M-uW_oU8NFpyrMyfnaMsOiCoC7z5hPF698AWddBmWLUTmhclLViF6xSt5pEcVSu69bMkfQ_B_jYGPJAHCn_hXHHh-1QR2QNbHpuehRsfrVoxlAqKvssYBhRX4DAYnPaLFzdVy8WQsA8nn9yPoLxRvPPZHfPkXjr6KIr0O4hAwxLxx9VCidY9_0U09rzxfuaH5bibZd4D-Sbj6b8yi2PsGbg9af6f1eiStaMsao8V7cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=At5nw6g0u3_gvo22vaJ_n8PUKf50qhQ28hWU9ZGAN1nJ_P3XnOAEOt4czrLDFDMVCLNdOANt34e6wts_Ww37XXb6UtRWPGzLEgRES8oivI-M-uW_oU8NFpyrMyfnaMsOiCoC7z5hPF698AWddBmWLUTmhclLViF6xSt5pEcVSu69bMkfQ_B_jYGPJAHCn_hXHHh-1QR2QNbHpuehRsfrVoxlAqKvssYBhRX4DAYnPaLFzdVy8WQsA8nn9yPoLxRvPPZHfPkXjr6KIr0O4hAwxLxx9VCidY9_0U09rzxfuaH5bibZd4D-Sbj6b8yi2PsGbg9af6f1eiStaMsao8V7cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=pTQqnBpGielrO_IsHI--nOpbt-riBsIWZpII9KWWEJmfmqsX9IXf3Qrl1OdTxYFOoqbK702d67L1XGnjzt1LKDRJbXayGofaTZyxTDgbdKN_41VidKacA-XiR-EtfntRyUtT5sA2hNxPm8FPwYEc4xoFoqBJ7OyyL-5XDYPTPKNRd2sJkMLhKLWMilwMbUQCP8f9Fg6FrI1O20c2tk22FdzESn1DNksVFpnNMGnkvGZPNBe7vyLP0JVxjYVNZOEtbxH8fcx0CXECGXJbbdXq4UKoKU3s6SuIQN3MTxzehFlhx6l1ICHFH34rHz5_svELDW9HqMRa3iH2QUd3V644FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=pTQqnBpGielrO_IsHI--nOpbt-riBsIWZpII9KWWEJmfmqsX9IXf3Qrl1OdTxYFOoqbK702d67L1XGnjzt1LKDRJbXayGofaTZyxTDgbdKN_41VidKacA-XiR-EtfntRyUtT5sA2hNxPm8FPwYEc4xoFoqBJ7OyyL-5XDYPTPKNRd2sJkMLhKLWMilwMbUQCP8f9Fg6FrI1O20c2tk22FdzESn1DNksVFpnNMGnkvGZPNBe7vyLP0JVxjYVNZOEtbxH8fcx0CXECGXJbbdXq4UKoKU3s6SuIQN3MTxzehFlhx6l1ICHFH34rHz5_svELDW9HqMRa3iH2QUd3V644FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=ovKxAKTG74M4MMP8OtWw-Z2VpzULGDB0aIkWBPdeSg7pb8WXr72sd5gn2ag2E2OZpdPz1Jwf-T07cqIw_Y3LnV2qzvYcnkaqFWxq7oMeYj2dQYV0gO2Rg36h0Xk1U1lc9X-Nm6rd24L_i9aLPKGA1pmmRFRwMy6OG0Rso2csLsaRsmk5Lm_e18FrjvTXNcAIYy17DWE_YvkYCArucT1zlaZz9Tzu4Y28-yOjHZPt35iyZ4Qapslj_PQiBLBwvw86Rsn4Ak3bm5YF2gG3F1mL-70_qMSHvFqzHFMLzt6J6-urUZdL5D1PiKlSQ72oUGcohzN6PhuMV2UbdnIUMbmGqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=ovKxAKTG74M4MMP8OtWw-Z2VpzULGDB0aIkWBPdeSg7pb8WXr72sd5gn2ag2E2OZpdPz1Jwf-T07cqIw_Y3LnV2qzvYcnkaqFWxq7oMeYj2dQYV0gO2Rg36h0Xk1U1lc9X-Nm6rd24L_i9aLPKGA1pmmRFRwMy6OG0Rso2csLsaRsmk5Lm_e18FrjvTXNcAIYy17DWE_YvkYCArucT1zlaZz9Tzu4Y28-yOjHZPt35iyZ4Qapslj_PQiBLBwvw86Rsn4Ak3bm5YF2gG3F1mL-70_qMSHvFqzHFMLzt6J6-urUZdL5D1PiKlSQ72oUGcohzN6PhuMV2UbdnIUMbmGqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7EA6t4j3d4OP14LF9qhP9YGc4lEECB9BTxlD2C0VlNirFPEWnAbUv8wxk8gkfr-OVBvdekQQwEyt1k-q9uVsNYLpQ_SG0laUywms9PduvrmwH4rpwzAf8Eu-pLEZWvhbeeQJjzd550esnR6Sq7mes4-248Fa_Wjxl_rsOYi76ja3QDvbBGr1Wz4dlPTUdpXjIdm_yYHAO-RxEORdYSzQjNXDuilr3I5rxpQAktC1snX11rlZLi4OWuvYjU5dz4MRZ9iaW25dacmxjHOfrSJyP3LH-dsmlwKBD-2Gh8tb9snM0ZYek5fVmw3WRXTXk4Bo4yHEtdCHi0_kBCE-n1kDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiXEJrIIHg0TeWlPmg1jlHQyGsVxH6WfRgwfBaoTPOeQTu8iuH2_LJg56jOWumCvlHbmYr5ELHMyG7oYRmHwOOaBO0K-zN98mJtMfi5klPjopWqCBDGC8u3tKhT2qGF8zAlG7Qrb6BnrfdqIj8Sp7NQIY2IW_aJd0h2Xg3Sc80E57GYJNsda4HzNrCkri0CTrkG1kcpT73J0OyATha2inQZjAkMQUKAcnSZoyQpg8cYeB9pUBYz4H8QDBUPktHPFepnwFImlWHol-8aCrrwaF2TKU1RbUDTd_ZDcyaE3AsHNiIvDUzQH0j2JHHanEVyfaSL9ja3BljiFOjdgr7l7Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=Y45n4P9fVb9Q30JWCGLnf0a0NaKLd4rReCdgWP-xcuspi_xQAGusurDB9_QEZDoY5SxqPCA886sdyUbadVQeNjjauRJ_fCFh7I8eC5iNG5HuQEvodZVvTl9e5hBLagvdrNF5q88CZIJMo2x1eQ40J1GgtiysDXqHOvcDGJLLPfvuo0t53YkO0_lJWGd6PRXtqTF5iBNweZyRfOx8camNahSgkvrUPNUTSOQqmzX2UXBdVwFo9FqMTwXaq7MkaFamYL84mcziQMDjgxPNxp0fREDCTO4qHs5zwnhuj3zEv5xsAWlG_ebs1bWfN9GYPuNCqjGtt73aXGIE_qFx83_RhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=Y45n4P9fVb9Q30JWCGLnf0a0NaKLd4rReCdgWP-xcuspi_xQAGusurDB9_QEZDoY5SxqPCA886sdyUbadVQeNjjauRJ_fCFh7I8eC5iNG5HuQEvodZVvTl9e5hBLagvdrNF5q88CZIJMo2x1eQ40J1GgtiysDXqHOvcDGJLLPfvuo0t53YkO0_lJWGd6PRXtqTF5iBNweZyRfOx8camNahSgkvrUPNUTSOQqmzX2UXBdVwFo9FqMTwXaq7MkaFamYL84mcziQMDjgxPNxp0fREDCTO4qHs5zwnhuj3zEv5xsAWlG_ebs1bWfN9GYPuNCqjGtt73aXGIE_qFx83_RhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYjvyAY0U80NjZHOleMv00VABTcM5-iK-OUFsoE49UZfLGWCkU7ovfyKHeDuA-C5x40ts1gV9SDPfSzfwBZyNHU8AkLzZF2g0bIzBGZCxgz6wz3ofcx8ujkrQN0bfBLgjpjwd96mQ7BMz0yxRJrsuI2nRQiFkLI3sYfRY0EawSfp5qV9bOzfvMhTGbyx8zaELD9iKKXe_35CwgwvtmUa74PsQIH6VqGTVrpwhowGedYB6sp6EIizm1my3YKNGkOQXzeQTeE5qCB3JsWAq0wULKN9ApIRIk7fdW092KmkNikBr10m_IWceNzEutM7ufw8Dt5ODhKlfXtzdGob25XD9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fR4CjXA3LHs4glBdgh3la5sKX-Oy4b8mfG7beXDX5PJIzdZGBnGJAFr4begepkVfnohIoQ1WyxyPz9uEmBuWTyz4rndztxZaRu14pHuiTDA5edDhvPa6_7ATIjkZBsh-qUH0NW-dV-9yVvEn0LuT0DksG7hJLfjY7d5ZpFSxYxmsE6f8wlog1jahE-J1tJcgIZEJC1nQ3C0TXkwYyQ8M1kzhOLVekGu6cNiQlDEwEbUYOE_KBYcmTf01lNVPPmW1kW_Udgu8LodZypIsFxb2qyry5SVZijzjo9DHzdybQ5X7nlLZdrC3ohSi_8IRlYznevuy651OL8HLW_stQSa86Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=NE7Mz93VfIYqrm36tqqn2hEmdiR8bQyb1JN6CIRRqExpnictf1WgIa4zjOzx9GFybpE77zdFUrWxZwNFXyHSoi9cBiKPikzRdY1G92BrbzE4s5LyHf2LDj7w7DQjYJVx3XjWTxbX_RlPFxbIx7zRU7GEuKgHLE4n5eo9nEW6IZkkSOBF67cfKPHqxC_tVLslX-tKRYfznV-W1Jxqwi1H7-x6efs1SsRchVnf9Ao8MyxVEmgE9ZvSibZxU4bemQIEq6F3_TS6A2qvp1mtVd4_ynpfNznzAm2FysmHqq1xdRs1vVGCsPYLyOUD9OObQeMNOVgufukE_H5P-ObeO3FWHS0Ed4JM8Kj70m6U2_BczvMMz7TzlbjBz8GK6yi9bumAzrsUsduxAEnA6r1MUibU9el7OkvU70pOaOc1SOc4GG_mzZP1n8mj43YnwApro-RFiGPhur1M6RTZMFetCU4I9U9dZowZ5yA-FsvQlRBFtHgrtafNmyiUpS9yegg1eQbiISsNfq-Mdjisv6ZPrCnAsIS4a_fz9Fj8UCPLAbgc-PRGMDP6R9ZjEVh04xayWpL0vY-0cEUZ9J-dLnmckRQDyFAivihtHxrYAFkEFO5kVZW6p7KBTmN9o7MyP8tL1fohlfgsQMagkB-Y9hPiLLyhCKBIEvq9LGpvLNdXs2BNTSM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=NE7Mz93VfIYqrm36tqqn2hEmdiR8bQyb1JN6CIRRqExpnictf1WgIa4zjOzx9GFybpE77zdFUrWxZwNFXyHSoi9cBiKPikzRdY1G92BrbzE4s5LyHf2LDj7w7DQjYJVx3XjWTxbX_RlPFxbIx7zRU7GEuKgHLE4n5eo9nEW6IZkkSOBF67cfKPHqxC_tVLslX-tKRYfznV-W1Jxqwi1H7-x6efs1SsRchVnf9Ao8MyxVEmgE9ZvSibZxU4bemQIEq6F3_TS6A2qvp1mtVd4_ynpfNznzAm2FysmHqq1xdRs1vVGCsPYLyOUD9OObQeMNOVgufukE_H5P-ObeO3FWHS0Ed4JM8Kj70m6U2_BczvMMz7TzlbjBz8GK6yi9bumAzrsUsduxAEnA6r1MUibU9el7OkvU70pOaOc1SOc4GG_mzZP1n8mj43YnwApro-RFiGPhur1M6RTZMFetCU4I9U9dZowZ5yA-FsvQlRBFtHgrtafNmyiUpS9yegg1eQbiISsNfq-Mdjisv6ZPrCnAsIS4a_fz9Fj8UCPLAbgc-PRGMDP6R9ZjEVh04xayWpL0vY-0cEUZ9J-dLnmckRQDyFAivihtHxrYAFkEFO5kVZW6p7KBTmN9o7MyP8tL1fohlfgsQMagkB-Y9hPiLLyhCKBIEvq9LGpvLNdXs2BNTSM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETj6RC27LvsXHkInU2iT0mFn2TPBtcNN-cAuxgwcgbVzHCy_1YtRbaVWQnez6jAD5Y9PmRmTN1BlcGVUGCbsWwXcaGTCZbYNZ34vp44lTTn0o7I5LQbv9aPTEUOseJD77nt3VXHv7joCiP3GsTAeZd64NXDjzEAJ4It0lMlDBbPGZQaJD_0aeKXbXNGVjjvSY_Zmnd5LA67Ql_FPGZzBZxgvmV1T92sI1yp6pY2XqqlHMTstSRBTsRsRf3NAoZ3aQ2mP_VaWM64twv0mh6TriNXvkxq9hJXrqQNa0dMwEOMMEG7UkgsgncRpUSoJjlZaaYa-Ym1M-UyJ2boQ6cAyGF9c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETj6RC27LvsXHkInU2iT0mFn2TPBtcNN-cAuxgwcgbVzHCy_1YtRbaVWQnez6jAD5Y9PmRmTN1BlcGVUGCbsWwXcaGTCZbYNZ34vp44lTTn0o7I5LQbv9aPTEUOseJD77nt3VXHv7joCiP3GsTAeZd64NXDjzEAJ4It0lMlDBbPGZQaJD_0aeKXbXNGVjjvSY_Zmnd5LA67Ql_FPGZzBZxgvmV1T92sI1yp6pY2XqqlHMTstSRBTsRsRf3NAoZ3aQ2mP_VaWM64twv0mh6TriNXvkxq9hJXrqQNa0dMwEOMMEG7UkgsgncRpUSoJjlZaaYa-Ym1M-UyJ2boQ6cAyGF9c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=Vbp0SNh7kQqblURsiZYRB-TV1SdAc8NsuYK0wx0gtl_alsNE7l79Wsk57gMbMdEzAMGv-KgFh0hBXT0PsJl5MDZC4C5kMA2uxZ9Kx5LCel308onb6VP7_dF8tZuSZ2FPNzfpb12RzUkdF8O-vxa3RvtMAkYDBPbhtkH-avxvPmTx4Lp-70icRUIrN62NEBatK8mxT7yRo6eMdkG4VQ_2c33c6gDpbn5tR_v8QfskO6Mbte6jqGgwniUe4WKndcpWtv2bkrE1lPiXN4C7qlt8ojsCqWJybRXqSZK6AGh-Xl6l-S-1NOdV3gllp2KHEQHKC-AMV9F2EgQeztu7b8yw4oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=Vbp0SNh7kQqblURsiZYRB-TV1SdAc8NsuYK0wx0gtl_alsNE7l79Wsk57gMbMdEzAMGv-KgFh0hBXT0PsJl5MDZC4C5kMA2uxZ9Kx5LCel308onb6VP7_dF8tZuSZ2FPNzfpb12RzUkdF8O-vxa3RvtMAkYDBPbhtkH-avxvPmTx4Lp-70icRUIrN62NEBatK8mxT7yRo6eMdkG4VQ_2c33c6gDpbn5tR_v8QfskO6Mbte6jqGgwniUe4WKndcpWtv2bkrE1lPiXN4C7qlt8ojsCqWJybRXqSZK6AGh-Xl6l-S-1NOdV3gllp2KHEQHKC-AMV9F2EgQeztu7b8yw4oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=sLjqwTFO9ygIJUHHGEoTLLZ4Trd6f_7F8U0o8aQ2GzvOnjSgk6zS8v0_cxuwmRx8wrOj0pMHljZ8ow73mv3hHQIFnfCo2d4PcXtwyZaMTRc78IGEWEJUqzfFBpFiYuKPyj1PV0hAq-sjWHL3LUW15P3digKBhxw9gqrJF7FC7u8DSAPCZGWP0TaTQbd7fCWNKq8fPzr6-F5jUFhowa5Z6pLIngNjZXo5tc5tg8Gq8F_6MUsYpGOrac9tA0AtzO5iVB01J_KC97nePVUcVwVkyPf_ussVWrdsVK9Hrk0c4g9FoggBldnnSRVcdX34I3QfO941dhGdeRfuNPUl8al1VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=sLjqwTFO9ygIJUHHGEoTLLZ4Trd6f_7F8U0o8aQ2GzvOnjSgk6zS8v0_cxuwmRx8wrOj0pMHljZ8ow73mv3hHQIFnfCo2d4PcXtwyZaMTRc78IGEWEJUqzfFBpFiYuKPyj1PV0hAq-sjWHL3LUW15P3digKBhxw9gqrJF7FC7u8DSAPCZGWP0TaTQbd7fCWNKq8fPzr6-F5jUFhowa5Z6pLIngNjZXo5tc5tg8Gq8F_6MUsYpGOrac9tA0AtzO5iVB01J_KC97nePVUcVwVkyPf_ussVWrdsVK9Hrk0c4g9FoggBldnnSRVcdX34I3QfO941dhGdeRfuNPUl8al1VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWpl6anwbpS1AUXtV7886epeKGV0BobG7orB1n-dF3ZzAfGu977_ySd279WOs2FhQqV26v630aD3J8BfaXtMfMvkUF1nsvU-QU-F6Qo6sUUUGRcN1bT8PD0MpYw3jDT6S9BuljtaHZPJHf18B3Ms1EQsOVpyN_5GGhrfrZbBePYNwT2YkbtnCIfRZpOvtUqR1zIB9-bPTxSGP-6gsMRDaoUYirerSDXk37Mjq-WoFa61BJsTic4QhBLYaLcCwVztdGS9XxaX4eX_iB0drmalICxRvF-ZwXmW2etcokRUp78A9H0eTG-N5nqjlqSi_6VLtMGQo6A9lLsSupEryN4hnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3dnXs-UlHZ9mAB-JlPq75ilUFTU77B7UPTpjTeCtyo2meB5uJqwyrKzvuSaephrmboxwsv0__E7GQflSQ9_t-2DQWrVwqqh_73SBKPo9F65DkPVKsrHMZzh2WlStBqQJYOfpOQ12SukIEIlJB-jE1-x_jacQOdjf1pBsn0oK0l9-AgXaO1b6zKPIw-2wDFw5EA4O910pc3ejmOyqyoGd0Ull5CdGkQFCLXc5Hs8dnofiy68mGvmuU6Dh8JA1aVpZxoqj9KwJDUPIT7PFrb6HzA-QZkLBpaE6JyK0Gwl585ZpH9f1of-ksffhNhCs6xiRtDRIEmlGzFX4m6H6Mp7BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌بسی که دولت لبنان و دولت آمریکا
به دست آورده بودند رو رد کردند،
اول ۳ پ در یک بیانیه و بعد حز‌بالله،
۳ هفته آتش‌بس رو انداختن عقب،
۵۰۹ نفر دیگه کشته شدن، از جمله ده‌ها کودک،
تا بگن «جمهوری اسلامی» این آتش‌بس
رو آورد! جمهوری اسلامی و زاده‌هاش،
اینطوری با خون مردم بازی میکنن!
اساسا چرا این جنگ رو شروع کردید که بعد رفتید دنبال آتش بس؟ برای خوانخواهی خامنه‌ای بود دیگه؟!
چرا بعدش افتادید به گدایی آتش‌بس؟؟
ادامه میدادید تا شکست و اخراج دشمن از خاک لبنان!
مگه الان ۲۰٪ خاک لبنان رو ندادید اسرائیل،
آتش بس چرا؟؟  آشغالا!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-1aEy7DuqeuvDZxMZKmNxBLdQHxWQYAZNFjBLj8MZlLsS-k2rYC1sVNBZa0zZrCXYwgWktikHYPVAoE1ESgPSMVcUkQM7EtSBuNYO6RHhTDrg5Ha3ujlp2VyQPWHXrJfleJDGLfYDZL-IRXT4nH96jVrORKNOG8ImoJywUcSEfnsqI3GfBgzZgjgIR7_ETKWrMJ9P5zLQ9Dqlmm9fNxpYE-Ke6-V5MhYBg4pxVHQAoGg-b_PU5B7-c2aqqVQs8HeKjCD4-6z9bnJVmrXsdIqbyXhY8mfOeSlkUy6LVnK-fdxfjcXQDqxVLhIyXK3TvCASHocbNoHgFRn13p5erHsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYzk2Afd44h8-FwcwfKmMMRVr00HDkW21gEwpVq-YXYZ4pXMKkDTNw8edI-cMqEjWN5p-6unF8OooGAdIk3Z5EnRt8c1ktPEnwA46du7S4xrkoVrQCrJ_ZfF1u7tlLc93bkYqaIpa4Vf9O2eqDtwWZNjfO9xjrMuZdderDdCbpaO5ND_YeaLAA9tJmVV6D9bIgf_KA04jmKLwyj43a-bJ2wrmiqFYwj1XE5MyRfADFJLd5NTBIpbx0stGgoJkfnoYH5Vn95iiFLWbJObcMKEqpzaMP9PdoJWVbdfj8KeduELcdFenJYD-Pz7Qn-tiWwuZbplN1j-T3nK-Ev3ZwSKgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyMm9kzp9LDWy50ah2uLHL5jlSOUdhTcfRCxfh-KZJQsScyzadm2R5VrmE2FYWWKPLfAWoSsS6Ue9uAPGuDfwMZQDJIfuQz5AeoEZfjh2qLZtFZwoA8XQfkRUdtYPY1EU-Wym82pXNlRC0A3_Ueu2ncIJHYwwXso_9vpGXX1xySLP49Ws6FapTtDeGhNeg1GiQaEJMlQiv2jCMxbR_6Uxn1WA3eK_GVHDpsJJ7Yq47z6nMztkzx8Q7MgqNxZDoBBCG425NYHUgfr1AUc1dyYlSH8PznboZ3S-J9GuFaqcq_VtFXXT5K_FCk7Kf2n949Pp2TgMQMcDBR3soqiJzMdYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=Mx2MvksXyZMUhtYODJiNmtD5MulENYSESGkbRO48QjOtYia6On9GH08Mb4uklNQD8A0GFTIkZ4RWgyOfmJg5Kg9yADmjWbVPjpg18nmrY0N_Vl8nkV2IpzZr9cxPUOJ_qA2Ok25MuOgHhmTs14BAg4QxrWlXIcRP9eLWtp0Ly77ZbfTAxNyp7pvu4qzoUI7TEk8GINEIxMbZRvijGpfe5VhYznoVpw3plWPwb4f44WilPgM-k5GxBXVUCLCI0SnjBzmKguNqXS-FaT4SdqDPQC4ID6ZSczLira74ZgTSMzZroyyzcF2Fzqi168ctGjzF5KHsFHTF-wQhdSmcnnxmMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=Mx2MvksXyZMUhtYODJiNmtD5MulENYSESGkbRO48QjOtYia6On9GH08Mb4uklNQD8A0GFTIkZ4RWgyOfmJg5Kg9yADmjWbVPjpg18nmrY0N_Vl8nkV2IpzZr9cxPUOJ_qA2Ok25MuOgHhmTs14BAg4QxrWlXIcRP9eLWtp0Ly77ZbfTAxNyp7pvu4qzoUI7TEk8GINEIxMbZRvijGpfe5VhYznoVpw3plWPwb4f44WilPgM-k5GxBXVUCLCI0SnjBzmKguNqXS-FaT4SdqDPQC4ID6ZSczLira74ZgTSMzZroyyzcF2Fzqi168ctGjzF5KHsFHTF-wQhdSmcnnxmMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=sW6Paue84zarWl14sqh3AHjRr9IWghofE2ypOZELYm-qXO2EZQDH9TlfLSXMGFjJSasllEMtumqu9oItUPlY0aLOTTuOR26MbpQYprQKQ7Iq0SSSwEqg0RpG4F2rWGr7pmErEITwdN-VV1Tg66ZNc7eHjw9Qgm438Q4clTw_BRHy_JFAj0shjshDV-owKypKUBE_8Y_XVokYiDLgbGbkpjmU6eUhR5ejpWvPMuKfGQ0-f70449NgaanUBGrCssfk_NqgaTWlw3dImcTKuuJ6yeevfTZKXMzJdSaTi1sklbHYy2l2ZAR5EenvGvIC-8yROdfbjjEteZunM91UkVaBvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=sW6Paue84zarWl14sqh3AHjRr9IWghofE2ypOZELYm-qXO2EZQDH9TlfLSXMGFjJSasllEMtumqu9oItUPlY0aLOTTuOR26MbpQYprQKQ7Iq0SSSwEqg0RpG4F2rWGr7pmErEITwdN-VV1Tg66ZNc7eHjw9Qgm438Q4clTw_BRHy_JFAj0shjshDV-owKypKUBE_8Y_XVokYiDLgbGbkpjmU6eUhR5ejpWvPMuKfGQ0-f70449NgaanUBGrCssfk_NqgaTWlw3dImcTKuuJ6yeevfTZKXMzJdSaTi1sklbHYy2l2ZAR5EenvGvIC-8yROdfbjjEteZunM91UkVaBvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2P3PVT42W5F0T2IPDBUTeedOk12OrDB-25BmzZS4ZHy40UIZwoS02f81CnzdepmjSIHg6_Mx2Wxl0tmJ0va7KGkx7IAIqthVHTPN25m27g5BShLVIrgSf3n4kFuRo6tEGoZ2jTK6E0garY-Snb5vXhOxO2qVphUHmHUMqWKPZ4zxz3Tv8M67-1XKrrzFBS6THmcwFmiHFAPMtKUHVubUe1liMIylvL5Ea6LfnQYC4l047hKTT2pjG6R3nWq5gINIHTpOWOQ0rphlTl5xpIouyHs4Tabwfqie9U9uTuv4oBoikq_w8L-ZvMODPmRvW4OgA8z1dltVz4k_5-POa33gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌
میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره!
پس اگه کشور ما رو کلا آشغال گرفته
و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!
مثل همین حمید معصومی نژاد
که دیروز براش نوشتم، میگه فلان مراسم
عزداری، توی چند روستا در جنوب ایتالیا انجام میشه! هر سال هم این موضوع رو یادآوری می‌کنه!  خب اهمیت این چند روستا چیه؟
پارلمان و حکومت و بودجه کشور و قوه قضاییه  نیروی انتظامی و قضات ایتالیا رو از این مجموعه و از این ‌افکار انتخاب میکنن؟
آموزش و دروس و دانشگاه و رسانه‌ها، دست اینهاست؟
از افکار این عده است که صنایع مد و فشن و خوردروی لوکس و ….. ایتالیا در اومده؟
یا از مناطق دیگه کشوره؟
توی اون مناطقی که موجب شدن ایتالیا قدرت‌ هفتم صنعتی جهان بشه و از مراکز مد و فشن،
اصلا این‌ افراد رو راه میدن؟ چی کاره‌ان؟
یه مشت عقب افتاده در حاشیه کشورن! هیچ کاره!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vy6t4HJ-JfPWmH24ODvLZ4xQdHmE1AoyhZUry9zAW1dv_tIcws6wnNUb9Dm9qDsmgeQVP_2BUkMz-V6V_pNXXKLFmb0p_9cOMfW-gXqbqbB_RSx3uUX5qwPvhE0v3JEEVI_eOqkt-Dej-ZiU7PjYifrcw0P2FyGFC6HKyIgTVu5YhTztOjrS4Tx90uOGRfGowz-ne1SysS2v0kjiOu0hUy3l4-M7Q_aROyN0G7yowDLW3xWG8MIDadk9nJviX0ApAo3qWRtu9jqTDgQedE6TY2SPjAl4rEgmkvaNOfCdeTSgTxO4MI7HWE67L2d8CS9b01P73fpdVd76xSb8AWNdRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=ivCkf3H7o-zxT4E0C_C3CEEZAvNvmOor68koD1Hy0Le7DqzWzUQuc6wa9Mc5qtZBWR_DI3YG_4O9NEJkJM_FChNpo2Zwy-Pc4g6D0t3uAzISpWQV5YXwu8s2mteoGiZwloVkpyffFpLsvx6SQaQUbcP9TdPSy0qmTefQW4g46YFTuL9JxHB7fVhxtQL-zLpZWRKKexaKwoQl_ahh7hMme1f8GgISjHdG3XokIphf9kPgP_sUbV9w1bwo4FAmOu8GUc3s6KU0-BlPXjWX3_SkouvQw2z4h1zf9w1i9JBbwYJDmwr1xrbl9Sbrfn4kLcln5hMN7c_Seg7TuisDy91dhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=ivCkf3H7o-zxT4E0C_C3CEEZAvNvmOor68koD1Hy0Le7DqzWzUQuc6wa9Mc5qtZBWR_DI3YG_4O9NEJkJM_FChNpo2Zwy-Pc4g6D0t3uAzISpWQV5YXwu8s2mteoGiZwloVkpyffFpLsvx6SQaQUbcP9TdPSy0qmTefQW4g46YFTuL9JxHB7fVhxtQL-zLpZWRKKexaKwoQl_ahh7hMme1f8GgISjHdG3XokIphf9kPgP_sUbV9w1bwo4FAmOu8GUc3s6KU0-BlPXjWX3_SkouvQw2z4h1zf9w1i9JBbwYJDmwr1xrbl9Sbrfn4kLcln5hMN7c_Seg7TuisDy91dhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=lrOg9yR1EC9Igx-pdFgmq-1cbFeNeCXPpuiJ4vaOL2n3BMJrJjrq8ltToK9XORzBCIIr-Y19vlMmAb2ThC17Y3bGwJ1P4fFKlDWdjtmsyYc8YITUvEAA__988eEF-yOwyToavN37hNUwyaeAl7dqukO6q3-05R6mua6H9n1YNg_bRe5Ffk4ig3AQU2Ba7f7eeRFWDj4nJqnOgVBWhnZ0y0hIkbhmFULluxKIEWhQC0Tp1jc1u4qiMK44Piub5MH4CVIOXTQwENA6Tn4wg6EqhE4sUuWgmLcohyILzvHj4IYw6LnjI1HBjOJ3s9ghzIRHV95H9MiOgxbGULU2UQwnSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=lrOg9yR1EC9Igx-pdFgmq-1cbFeNeCXPpuiJ4vaOL2n3BMJrJjrq8ltToK9XORzBCIIr-Y19vlMmAb2ThC17Y3bGwJ1P4fFKlDWdjtmsyYc8YITUvEAA__988eEF-yOwyToavN37hNUwyaeAl7dqukO6q3-05R6mua6H9n1YNg_bRe5Ffk4ig3AQU2Ba7f7eeRFWDj4nJqnOgVBWhnZ0y0hIkbhmFULluxKIEWhQC0Tp1jc1u4qiMK44Piub5MH4CVIOXTQwENA6Tn4wg6EqhE4sUuWgmLcohyILzvHj4IYw6LnjI1HBjOJ3s9ghzIRHV95H9MiOgxbGULU2UQwnSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqBPI1meFq3ZKQNEYfuyb7r-qcD6AGm3YidsKpCGnH3Tb3XiEfzI4EPw-vgKGMulJfeqBtAFQMiwV4brR-zUaXoTPxoazRTNkrkBFApY4i3SCTCYDASpDSBLy24bmQo0jyTb0MEfXKy2hnXUwsudOY4yK69IY3ubLi1OgD3Nenn_gZHdE9aj2mKQ2e_arV7ca9JiZ9FZQF_QJGF-FuVZC2AkM7U8VFkmwU4xyDnvr86FHtcf762u5_mGrmfPx7SefoQs0bovEIN_qgnrC9TylxtbgRnyHvDcSNx2ENFQ9qQSmbbj9VHAM2TvcF_C0JDT4paKcepPOm1yBCfy26YS7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکید مجدد ترامپ بر ذرت و سویای آمریکایی
و اینکه ج‌ا حق دریافت هیچ درآمدی از تنگه را ندارد.
ترامپ : ایران به ایالات متحده اطلاع داده است که برخلاف گزارش‌های دروغین و جنجال‌آفرین رسانه‌های جعلی، ایران نه از کشتی‌های عبوری از تنگه هرمز عوارضی مطالبه یا دریافت می‌کند،
نه هزینه بیمه‌ای و نه هیچ‌گونه مبلغ دیگری.
اگر این اطلاعات نادرست باشد،
مذاکرات فوراً متوقف خواهد شد!
🔺
همچنین، ایالات متحده هیچ پولی به ایران نداده و هیچ‌یک از دارایی‌های ایران را نیز برای در اختیار گذاشتن به آن‌ها آزاد نکرده است.
🔺
ما بخشی از پول‌های ایران را که کاملاً تحت کنترل ماست، در اختیار کشاورزان و دامداران آمریکایی قرار خواهیم داد تا با آن برای ایران ذرت، گندم،
سویا و محصولات دیگر خریداری شود.
🔺
ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد غذایی را برای آن‌ها،
منحصراً از ایالات متحده خریداری خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JBQjfVW7ZIFEKpXbrwXIz4IRVSyAjb9j3hAe4zOHIg_Fne43yHaG-om_QKLzp62Kp7Keyy1TKEzNpyPX3nVp9KFnfUWZAaE_RndmFf_rXaGgtMU-80B0GmA5GlDWX-gk1p0TNP0Zz1P6YScUXCvR8MY-RQyaQs7a5Tts21dxEpH7w5H7gZMJuBe0yLvu4n8f1uUJI-1gyG7XGQNKZNbfNpcxCHxrZ5t8ScmywamxUd4qtfOG7rrlLEh5r5l3NBypG3gfzd98H1P-C49XbZ1QrN1s2ZhkLci7QcMXX3dkazd_n7PKc-DGmTQD7xoUMyh5JVghEE4zaolYEJ6Rj05srw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RJzocMAvdGCRtUMfpY3yLmKqe9XUq_Ek6lTaqn5JTlO1rgQh84sDNd7rBt0l4mJcz4xqG7l27I7IIrpeZn1fwPCW93_ruXZt64gSVbbeC_2ZmLRdHfUBJQbwnYQIv2PueX_WtTn89LTXAw_oV9fsqh3_Il8xw54X4PEjnmVpcO4f8ovqCwsWuRlj5g8izZaOlNS163N2GjQ_7s6NuxXIjC5WimBawfwGF1Y2Odqpbr9WqF-ltSRxRRngSd_wO8pqdcFUbR1go14N3cbCsBRJGH8dtiQ5SViCuLqh0N-IthBFBPd3i3tQ8_ofuI_7Pyk6vFuJE0nAqLcs1Rpd8jViow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=GL7AzJs9DoqknLpxCfqucKk6et5zRbXHWbJm132G34g2Eb9lVSDfAuaJWi31Yoh1qp0MVlVU0j8e5vUPKd0iaZR4R5sfQH0MQLh3mOkaiYE1YI5Enlp-JXo-g55_R_RQtOrJyqTg2ztpt2r-Fj3bsG7BYPL-90Vw-iLoCrtVjltTQNH7KafFs_4i-pyDbeoG4a3wTxfoH4-k2uO9Ah1Vpgxb8BkRuqaqdsLDo8n1mCRCESeDhZQD0QqPveaPnaWdE5QQ3vNu44DcVkzXTmcnTDQ5tCBji0oTwRHFg5Wo9Vqyk1HZdOvcehmpcSP3XZhI48tmpOvRc8S286RgXVaQYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=GL7AzJs9DoqknLpxCfqucKk6et5zRbXHWbJm132G34g2Eb9lVSDfAuaJWi31Yoh1qp0MVlVU0j8e5vUPKd0iaZR4R5sfQH0MQLh3mOkaiYE1YI5Enlp-JXo-g55_R_RQtOrJyqTg2ztpt2r-Fj3bsG7BYPL-90Vw-iLoCrtVjltTQNH7KafFs_4i-pyDbeoG4a3wTxfoH4-k2uO9Ah1Vpgxb8BkRuqaqdsLDo8n1mCRCESeDhZQD0QqPveaPnaWdE5QQ3vNu44DcVkzXTmcnTDQ5tCBji0oTwRHFg5Wo9Vqyk1HZdOvcehmpcSP3XZhI48tmpOvRc8S286RgXVaQYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6nA3aFyWALtCHvtNeD47M-_NJpKd3Jg6hG6htvCvFl2l-tTwsd4sHzy30Dn7oDoPDW6dmUYAVomIxevw21AFB2-Jo5gJMTiaIsa6xjorQaSSOy_4NC25r70fp-r7W7i0pvfdoTJNbOLhva36_smSlDe3S9wYvT_EPMGLcrZJAktBzYVIwb5UvoSFafHTbWPDrf777rtXmYPOcLFKaqqM-GpiMJFB7pM7RWVHFJaabaGzYBc6VykYu3X-RKUkxl5_uKtQiAOk59Ay0uqiawPmTZOOgfyWejlm0zwG924OJtnAKZ_GGueKKuyOLqpNB9kq2ReQeDGXqd4YnCidc4ysw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cv28ijbanGRgEWyS5fJ-dD1uTPjgNG5tQEsBYiwSYXQLl32_6mjJCqb0gVi-devy1utr6lAy1BrcluAyJtDOfohbbyynQhsecLgLbN5_aAzCsoAPLmK7ntz2SS8Yiyzx9KVQApcNwg7fRKPZF_uGm8_QXyeNkpCWDFaG4kG2p4OGvEmTTpPPPAIqS3rg0snbS5J_zV9MJ5RXfsIczS1N_ZsUH3O_ABFKTjnIodWq5nDeLJwTVgoaLEl06J6qqpNCMlQzsIrY9kBwQ_UCWhGj2fznUeLzVOZM4we-otxReZK0QghwUrfOeoCF5caF9a_WsPjlsTNCNdzPe9cStBEIZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDPy5DcmCdLGrNxQ_Z1dhYNInugYCQ5z5OvV8juCfFOxQrsmTZMFDicFFYWp3Pm0DzXPx5ncklht8c2Sw0BHTMTUmMiXouipYp8DsCgykFV487kCsoaKU1-bHLuRfYYmu8ZgbHYS30DhodIWWyCIfJV0HVHfP6sX5bx4LI3eP0-js-1NsyfALfx_M17nnMLvZBSfc6LMb5EVRRA-SIBe3K1d44yoTnew7z-l6E1fUn-cTF2IgwzU2ThKV4bs-OcACKXHQ8EXVi-QiWp76f2lzy03iMQ8_ixYoPoxBzPEkp7TFZJPl4Yret0ZVqLD0LjLOf96vS26QH_lOPQymba0zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملل گزارش داده که در عملیات خون‌خواهی خامنه‌ای، توسط تروریست‌های حزب‌الله ،
۱۱ هزار ساختمان،  که میشه
۱۸ هزار واحد مسکونی کاملا ویران شده!
بیش از ۵ هزار واحد مسکونی
هم بالای ۵۰٪ آسیب دیدن!
هزینه‌ این عملیات قهرمانانه!  ۱.۳۸ میلیارد دلار بود
که قاعدتا باید از جیب مردم ایران
پرداخته بشه!
بیش از ۴ هزار نفر رو هم به کشتن دادن
از حمله حدود ۸۰۰ کودک! بیش از ۲۰٪ خاک لبنان رو هم دادند دست اسرائیل!
🔺
آمارهای این گزارش سازمان ملل، شامل ساختمان‌های ویران شده در یک ماه اخیر نمی‌شود!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
