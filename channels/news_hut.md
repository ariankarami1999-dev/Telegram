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
<img src="https://cdn4.telesco.pe/file/qv0zHbFY8WTyRl5HgTZnlUKwbG-AfVRELkqLCWAB3zXRVAUCgw81BUV1NhqjpcKdxfK7g3RFj3IGQm9CLEe4io5rvN9KI3kRF0IEonhUtDiN1V63P6PxnBCVvDoyvnWe_3Q8hKkdP06mTszOxfa84PBN5FgIk7B9cRq3JgCj3cLNI-cK0MKqQPoe-Qrd5capcZBMHutNnIgFK3Bop36PLZdls-Mte7CUhzuEbA0dU7qE5Y2hRXe5LhgR1kz6S3LFASkrpJAndUobZzZ6rKraxKKLrWjMeyxwpcGx2KG_XYyz_b9cQBfowkT50Umxp6kI-j5_ayVTAe4FqnokEWrEfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 112K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 19:31:23</div>
<hr>

<div class="tg-post" id="msg-71198">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بیناموسا مگه نگفتین از امروز برق نمی‌ره؟ رفت که
#hjAly‌</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/news_hut/71198" target="_blank">📅 19:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71197">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd3aa09393.mp4?token=R32tAAZRpyoBYDUbqMVi7gNTcD245QLMIo4edxsH48cNcWbAlKoDOg-6G69L_EQxbJ85PoHjut7YjdAbUtU6pWBqx8VBjj9XKyRQCTqnILXoH34a2G4mu9oq6BT9LwFHu9Xp5pz3b1T3MBBXBy_HX3sJJcfAL2ZooTKpH9COmF63yD1E8b4103mID3HfqcOiQQ7Nqlfp_0DyVdTI9aRB9PP8XzqNDK6RFnSdoiQRxS2KeQlePVX0QCPE2tYnCfX_GCqds0FUjrROZXsePlQer2WwxmIah6sXgq26jom4p6uOPzBsPHSQjwxF6IzdPo8OJtmfbDXQm1wjMgaZjBuk9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd3aa09393.mp4?token=R32tAAZRpyoBYDUbqMVi7gNTcD245QLMIo4edxsH48cNcWbAlKoDOg-6G69L_EQxbJ85PoHjut7YjdAbUtU6pWBqx8VBjj9XKyRQCTqnILXoH34a2G4mu9oq6BT9LwFHu9Xp5pz3b1T3MBBXBy_HX3sJJcfAL2ZooTKpH9COmF63yD1E8b4103mID3HfqcOiQQ7Nqlfp_0DyVdTI9aRB9PP8XzqNDK6RFnSdoiQRxS2KeQlePVX0QCPE2tYnCfX_GCqds0FUjrROZXsePlQer2WwxmIah6sXgq26jom4p6uOPzBsPHSQjwxF6IzdPo8OJtmfbDXQm1wjMgaZjBuk9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست‌وزیر نتانیاهو درباره ایران:
پایان این رژیم در ایران نزدیک است.
این رژیم ضعیف است، برای بقای خود می‌جنگد، متزلزل شده است و هنوز مأموریتی ناتمام باقی مانده که ما مصمم به انجام آن هستیم.
این امر در نهایت چهره خاورمیانه و مسیر تاریخ را تغییر خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/news_hut/71197" target="_blank">📅 19:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71196">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djTvA5MEvOW-qWoGwfTs9MZHjV4Fch2b9wnA1X3kRPUaxUvLkBiFqF-95hUpBrqsWPg_LO4onSbZ7RWi6xNLHvMNPJBE3ia63DzWYn7-xR-dxTolLRysrLFbaHmrv8b4d_4POlqtbLDURexDrxTa-HNMuwWh3zbnqJ5LIpjGFDZsMsvdWTCSL3Wfjm7xCnRzdh3FGpB2s4xpDRN5ZJydpHDYqABAyQTMCetWHhKhZ-VYpgqq9TRQGHqPkVs3RO2jAGZGt9CpRdMUGjEMwKUclL3FLX3egzo566mlQSgPJ1VJOcTkEmkJWXQPQY3ZxPYRGIX3PWCK9P1KV1FuiSE04Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیس قالیباف به بسنت:
چرخ‌ها آماده. گرم کردن قبل از پرتاب:
دیزل ATH: فروش فوری
بزرگترین طلبکار شما: موفق باشید با Yentervention++
80میلیارد دلار کاهش می‌دهد: نام نروژ را به Americaway تغییر دهید
استخدام کم: بدهی به خدمات با DO[Israel's]W، طبق گفته عروسک‌گردان‌های شما
اوه. طرح نقطه‌ای فدرال رزرو قرمز چشمک می‌زند
😁
@News_Hut</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/news_hut/71196" target="_blank">📅 18:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71195">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeAiQ91AkS-kG5UIlzucjcy-xadSCd4Bt97hods_8JivyUdsWx7t_okrKn_PFOiUMtxvU3OMBOr0xeoWE7KrkzT4ylH-paSvUwKiC9oeYblW-gSFyZgR1a8WFQoL6bT6jmkkshb4nis3tewriuLP3iFDPFs4PW4YMTZSc4LkOkcPuu5GTUoUupDMDkRlOo6_ISqolGTqUJBqTgZ2z2A2m-H7NJN1Wk6WA-h-dXIuBJj1ELqbDWKpnu35pvmpPPt7h7QgEwhiNUqkwjnV31NFzoh8G7KeOaSgp8hbLGMXLce4_iMcaEIN7In0KcScEw2wuvQkbgbMBqaLRr55WpAgNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
گویا املاکی موهاشو رنگ کرده
@News_Hut</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/news_hut/71195" target="_blank">📅 18:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71193">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbDx5bgKnUZ3ub3MqzE7Py9q2pRAKpkJu5usPjHdqz8jrcsylTfB_zMvuOnZ6pxeuExtz9ZyZ9CdNluW8Z4YeCZ_MlUXYXKET7vs_M-JJ_MGV8YHQXZ2TN2XjUKSpxdjbi_dVkPLbu7bB-LMlv5yHsGVZSCsNAzdHHlXnbrNRVIwH5tzCtdwwUs9pxcBIQKZvWGvuTGa0jtOp4oQJsM118cOlPI_UtKYwuf_6r81GCwzzi5L_1qSM7xgvSISERiOdoMwPgva4VnoD2zHutw-1f1THtNuc4Q7kuklh8Hn8bfih2sF_QNc9FgpQX6HbaAiCYvtrR_uWxlPRmK_PguG3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/385d0bbd1a.mp4?token=v-IyJHVCQD-XDOBcYutAPCC6m5R1CNeaQowWz8HnfbzDnJCFSU8ptHpaX9yAMhqf3VHJTSmITdH_sgCfybWI5m5B-WD0z6GITvHntXqwGO8dQ2VCen-7OkzAmxZD87zyt127p7NT56ygouEo2uCJbktrnsByu2AZKnNR2i4aoeR1KPZKqE9fvG2YH3Q_FobJejE4IsNBiDW0eQhgTeKXxbYnklKUBAbeGhSA9U31yYVihu3GI7TlQ9_d7wfuAdky5j6SYI8l0DuBGzu8_HSdVX87M8EpXa2p_0rLxB7cQL776cwxC5823sSv5KMW4_F0m7t18PRGPDjgQD9KfGJaKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/385d0bbd1a.mp4?token=v-IyJHVCQD-XDOBcYutAPCC6m5R1CNeaQowWz8HnfbzDnJCFSU8ptHpaX9yAMhqf3VHJTSmITdH_sgCfybWI5m5B-WD0z6GITvHntXqwGO8dQ2VCen-7OkzAmxZD87zyt127p7NT56ygouEo2uCJbktrnsByu2AZKnNR2i4aoeR1KPZKqE9fvG2YH3Q_FobJejE4IsNBiDW0eQhgTeKXxbYnklKUBAbeGhSA9U31yYVihu3GI7TlQ9_d7wfuAdky5j6SYI8l0DuBGzu8_HSdVX87M8EpXa2p_0rLxB7cQL776cwxC5823sSv5KMW4_F0m7t18PRGPDjgQD9KfGJaKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
تو همه جای جهان هوش مصنوعی داره جای آدما رو میگیره ولی تو ایران برعکسه
@News_Hut</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/news_hut/71193" target="_blank">📅 18:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71192">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa47cd6f21.mp4?token=Z2u-76JdrCUDSpBAXxFuU1f5DYpY47JxNNGcWWeuGaWGXNqP62rEA6jBBRx8V2U959pHYcyIzIFPk2Ea3etdaKe_3GtZXHSXzmcBSMc_WW6lGKWrVbDuHsibRtOgv2NWUXLYOEXebtLer7xLpnM241MonXnVP4KewdAPBbAgmzTqXlA0F-tJiktjVT4d6L0bMHZISlpX4n-a1fAtjrhbalq2ieOTWWYaVKL21TzXIZyUvxZVIqTxcEMKK_mpgBxKsKWxCoLZvm7T8eJYuRb5JKn8VgjsYuq8WWLyVcdwqyHjsVa24pVJzEscUtsUSStzZtQ1ZG5ABW9sy9fSfmOQkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa47cd6f21.mp4?token=Z2u-76JdrCUDSpBAXxFuU1f5DYpY47JxNNGcWWeuGaWGXNqP62rEA6jBBRx8V2U959pHYcyIzIFPk2Ea3etdaKe_3GtZXHSXzmcBSMc_WW6lGKWrVbDuHsibRtOgv2NWUXLYOEXebtLer7xLpnM241MonXnVP4KewdAPBbAgmzTqXlA0F-tJiktjVT4d6L0bMHZISlpX4n-a1fAtjrhbalq2ieOTWWYaVKL21TzXIZyUvxZVIqTxcEMKK_mpgBxKsKWxCoLZvm7T8eJYuRb5JKn8VgjsYuq8WWLyVcdwqyHjsVa24pVJzEscUtsUSStzZtQ1ZG5ABW9sy9fSfmOQkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوای دو تا ترنس تو پارک لاله تهران!
فقط آخرش
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/71192" target="_blank">📅 17:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71191">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=OyW40qeJseGlmc8KGz8kuwUjtrK9sMZ-H1vX9CcRTt_RKVMozqhlhnokdRG2vI_7skmVDLpHlgYEfcjIm_CjjC-2supoEQxJfu5-ejAgqVoEWFoEW0TgZEANs7niMRDi--MGQNWdSbQJ27_BDLeAw7OIYpZnZjnv40IDilb4OtSGfB7dGufcZXPiNQV8kXw42_O5oOILDsxHaOAgUOxWIuVMXsw0XXBLxWXAE_I-4mBdvyWRZU299G9o30u3eIIUxLLTKzVlXVt-hnzeLrHt0IzZBkwP4x8jmqUB9vIGaxAK0Cop9RWnX9wOK0Ta5YHRma2SKc1DLt5UUfQcA1glDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=OyW40qeJseGlmc8KGz8kuwUjtrK9sMZ-H1vX9CcRTt_RKVMozqhlhnokdRG2vI_7skmVDLpHlgYEfcjIm_CjjC-2supoEQxJfu5-ejAgqVoEWFoEW0TgZEANs7niMRDi--MGQNWdSbQJ27_BDLeAw7OIYpZnZjnv40IDilb4OtSGfB7dGufcZXPiNQV8kXw42_O5oOILDsxHaOAgUOxWIuVMXsw0XXBLxWXAE_I-4mBdvyWRZU299G9o30u3eIIUxLLTKzVlXVt-hnzeLrHt0IzZBkwP4x8jmqUB9vIGaxAK0Cop9RWnX9wOK0Ta5YHRma2SKc1DLt5UUfQcA1glDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
🇺🇸
وضعیت دخترای حشری تایلندی بعد دیدن پرسنل ناو هواپیمابر آبراهام لینکلن در پاتایا برای تعطیلات!
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/71191" target="_blank">📅 17:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71190">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/45226525f2.mp4?token=VbyOKZkCccXj8XbZfctwryXesKEecflc07isw7ggjd01BBmCw_rDL7STwu8Da1Bhip6xkDvDgxnp3mgqO3apNZeF9VVtNvARv0HcpndBJJsMWuDXAkwExQwoZN3n2j_wLljSDv30xXNecsqGq8X0_vU_QaWU32InynRH1uqbSOXCsVu4_Gay3AUMhK6B1nKlcjaubobLCZgmji6xqv3zKSeePoq8kc_hwU2D2B_0nIJM9r_GGB_HAaPP5XrYrtcZkwEotQvGbZ2ObrOh6AGuJJbjWU0CafNw-iB-1A3zbYcuGFZTZtflQstUgpZz0RoLqCdQ0k1Ih_EKugRlGETHsA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/45226525f2.mp4?token=VbyOKZkCccXj8XbZfctwryXesKEecflc07isw7ggjd01BBmCw_rDL7STwu8Da1Bhip6xkDvDgxnp3mgqO3apNZeF9VVtNvARv0HcpndBJJsMWuDXAkwExQwoZN3n2j_wLljSDv30xXNecsqGq8X0_vU_QaWU32InynRH1uqbSOXCsVu4_Gay3AUMhK6B1nKlcjaubobLCZgmji6xqv3zKSeePoq8kc_hwU2D2B_0nIJM9r_GGB_HAaPP5XrYrtcZkwEotQvGbZ2ObrOh6AGuJJbjWU0CafNw-iB-1A3zbYcuGFZTZtflQstUgpZz0RoLqCdQ0k1Ih_EKugRlGETHsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
راننده ای که چند شب پیش در مشهد طرفداران حکومت رو زیر گرفت:
عمدی نبود تعادل نداشتم به یکی برخورد کردم تشنج کردم جای ترمز گاز دادم و یهویی زیر گرفتم
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/71190" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71189">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71189" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/71189" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71188">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPpaHh-lGkKx_zEWCUxr_Ieyl5hdSICpZbmw0Ok5VGSClkGo5FZVfnV5wOWLot09gkn1cX2jkN2lgZcW7w59nx89DyYawunnrTvhx17mw1mHNQQRmj134Ngg2itG_TI6vqMfM6fwrz6PWFWWfn2tWyDv8NY2KDtATuPvqrwqTg-6ARccp32U7-XXcaWnkj-KhRI-06i1P7HA4_Tgz0Ec_FdoSkdnscOIUSOiiDBokSA-3Ogh0ueIy3pIP3zFeESKvZgwVzO8Gc9pYXcLZJylzUxCWkyCT3QZgvXR7Z0hlVW2R3dYmAEnPjC6kqDMTeIo2oJupQ0V0flzjuzSle-ivg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
چلسی
🆚
آرسنال
⚽️
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار ۲ تیم:
چلسی: ۲ بازی ۲ برد و ۷ گل زده
آرسنال: ۲ بازی ۲ برد و ۴ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/71188" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71187">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cU27KpZqhBXcA3sYj5wOJR7M2d39C5vA-lQfPmUc3zOiTuOC9huC9uLx5Pujnb68aTMiuyCDkMBbWbgigtm6j9KQ0S592UiY8gkf1M_3V8JQLGn21to4rSfTNneUovGz_8vs4D7hJgEFevAikO4aDDCVp0pBqSoX_g9YecqxRXhZOmeah4nYvpP1bQKbtyUax2jLRDdW9KapSTMGYS15PUhyGZjZUF_q4fiYUTIw1yHKwWzGUCeQWGCYfiEtWP60HbDDzLnVemxGjnTnN62PfQBkxQ_NT7sFhY9KBJdC9uEpG4uloCTlpMnIe7Azo2hJ71wWhKjhZiHG95PzkAcMmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇰
🇵🇰
پارلمان پاکستان برای نخستین بار در تاریخ این کشور، فرماندهی قانونی هر سه شاخه نیروهای مسلح — شامل نیروی زمینی، نیروی دریایی و نیروی هوایی — را به «عاصم منیر»، فرمانده ارتش، واگذار کرده است.
او می‌تواند بدون نیاز به تصویب کابینه، کارکنان این نیروها را بازنشسته یا اخراج کند و یا در خدمت نگه دارد.
دوره پنج‌ساله مسئولیت او دست‌کم تا سال ۲۰۳۰ ادامه خواهد داشت.
او با دریافت درجه «فیلد مارشال»، این درجه و مصونیت قانونی را مادام‌العمر حفظ خواهد کرد و برکناری‌اش مستلزم کسب رأی دو‌سوم نمایندگان پارلمان است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/71187" target="_blank">📅 16:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71186">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22246726de.mp4?token=pl96_1ClUtH0GVZDLdPNKbUfEhYFqhy1d5toMKMxlEhqMXZtibzMloN12qAgwp61tZyWjmbyTpH5ibzUOiTJkXSPqkHf25BZCU38izfmTGKFqHqNOMoI6gcF_K7FzQDD27f3QTdqrqcjT21rxnom0YXRhCI3REvG74HZbxwC4uf1G-Yj2LEvm366FwzGwRBjX0pImQlb34JNLHZdwAQvwrc1_IAQTl3-OU2xqgfdYKsVT3nld4PyIt9SVOEhk8dlnD3ppJQgBSmnyp0wUAHvUfMVmgUNNdADJMvLhy9lkoRyeWCNo-w-WAocyAVRxkj6-FkgHUq538RnQt8U2R1rBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22246726de.mp4?token=pl96_1ClUtH0GVZDLdPNKbUfEhYFqhy1d5toMKMxlEhqMXZtibzMloN12qAgwp61tZyWjmbyTpH5ibzUOiTJkXSPqkHf25BZCU38izfmTGKFqHqNOMoI6gcF_K7FzQDD27f3QTdqrqcjT21rxnom0YXRhCI3REvG74HZbxwC4uf1G-Yj2LEvm366FwzGwRBjX0pImQlb34JNLHZdwAQvwrc1_IAQTl3-OU2xqgfdYKsVT3nld4PyIt9SVOEhk8dlnD3ppJQgBSmnyp0wUAHvUfMVmgUNNdADJMvLhy9lkoRyeWCNo-w-WAocyAVRxkj6-FkgHUq538RnQt8U2R1rBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم وایرال شده از ی دختر ایرانی که با یه پسر مکزیکی با هم وارد رابطه میشن و بعد از ۴ سال بالاخره به هم میرسن و باهم ازدواج میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/71186" target="_blank">📅 16:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71185">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWt1__7W_WkU62DTYn28DTMFhp6qCrU4_HG_aS4YpI87FriX7_VQq3UAF4OtjsngdbuRcIYusvsSViPuQ-wPSjC43KBCbel2pqyyzUFpp61lruQ2MX1vlfikpONkvvF2K4rVI10ApXnXwcdZgrrUlthNCZCxD9sAW6WP790uDXcErUi-Djco6hDlywkMeuRk2WltyBqSawdc-sVGlDrerl2FHrVRyXqQ6JqBv21Q5p_PgnWBYGJsmxrZHj0Cbdj0mBauusxJxVULVIRTUoqD_Azh_I202Wrd4GkLhy-15dsVRbrJa1vo-NKHgmKW0WnvfnhiXQ7IfvNxuyxzRqisSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیده شده در تجمعات شبانه:
قالیباف
:
علی الاصول یادت رفت
علی الطاهر هوا رفت
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/71185" target="_blank">📅 15:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71184">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64baa312ad.mp4?token=tPG1rWT3OEY1Zq_kN7pIjt7FNY4w98i0Ih0UQPCDUhw7q1OrxUq3NyUjxyJPFAvCbvFKtMIal8TSfaFb_2vKGXHqM4tyzsAkOe8O4FEeUBIKaPGKfvOsMcdzuINyhcVOW_EvxpuiI71v7846ETuoc65vOQp27XOqz67iJ2x17qbHgDbAGxA7PJZ0HT3wHr4xlLFzFAlJC4nVgkcQaybiWjD80PqECxzm5OnJmpLejHC63R_lRVO-sE9NxFfjYrJ6HSni9YfUtXyc8EuFYOYmafaoLTlswf2l0i3k5cUgB4HJuRIjaiiNMYG0dnqGPdwWfdIUqqaXnh8qWjDV8Ex4bA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64baa312ad.mp4?token=tPG1rWT3OEY1Zq_kN7pIjt7FNY4w98i0Ih0UQPCDUhw7q1OrxUq3NyUjxyJPFAvCbvFKtMIal8TSfaFb_2vKGXHqM4tyzsAkOe8O4FEeUBIKaPGKfvOsMcdzuINyhcVOW_EvxpuiI71v7846ETuoc65vOQp27XOqz67iJ2x17qbHgDbAGxA7PJZ0HT3wHr4xlLFzFAlJC4nVgkcQaybiWjD80PqECxzm5OnJmpLejHC63R_lRVO-sE9NxFfjYrJ6HSni9YfUtXyc8EuFYOYmafaoLTlswf2l0i3k5cUgB4HJuRIjaiiNMYG0dnqGPdwWfdIUqqaXnh8qWjDV8Ex4bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو درباره یکی از جنبه‌های سختی مرد بودن در حال وایرال شدنه:
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/71184" target="_blank">📅 15:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71183">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c325a7591.mp4?token=rBa6RFTmZ7g-6k3yAY-pgURNReHR3_VxDVg8QCpR_2fGPxlKq5UX81Ko4oDDinxupZUC8VK30ul_NbI5ecDhKkrnHGbCHwp1Lur-_KWjrTzlYfaB-85p0sndhUn-MeSBDdW_ZhwADf57LyGal2ppXpy-h2a7dYNM2b5D0j2WeVn_wJpx4jCd1m8Xn4UoE2HNG1YknmXBKLiwdRCz480kRB6EzrLFHBj12-MQ3ZC5RExXq2ZE1TUAG9WM5P7DU1yTTVHKwzV53a2T-IbyoHdIQ72DZxFvMlRqo-jocjNwurUkPaa-9dqKMBczBtDwdszDNgSvV8xlgx3uCHc0g5oznoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c325a7591.mp4?token=rBa6RFTmZ7g-6k3yAY-pgURNReHR3_VxDVg8QCpR_2fGPxlKq5UX81Ko4oDDinxupZUC8VK30ul_NbI5ecDhKkrnHGbCHwp1Lur-_KWjrTzlYfaB-85p0sndhUn-MeSBDdW_ZhwADf57LyGal2ppXpy-h2a7dYNM2b5D0j2WeVn_wJpx4jCd1m8Xn4UoE2HNG1YknmXBKLiwdRCz480kRB6EzrLFHBj12-MQ3ZC5RExXq2ZE1TUAG9WM5P7DU1yTTVHKwzV53a2T-IbyoHdIQ72DZxFvMlRqo-jocjNwurUkPaa-9dqKMBczBtDwdszDNgSvV8xlgx3uCHc0g5oznoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مراد ویسی درباره مسعود پزشکیان:
حساب اینو نکنید این متخصص قلبه. از نظر سواد اجتماعی یه آدم به شدت پرتیه پزشکیان.
گفته کارمند‌های دولتو داریم صحبت می‌کنیم در سراسر شهرها، نیان تو شهرها. مثلاً اگر کارمند بانک‌اند اولین بانکی که اونجا هستن برن تو بانک بشینن کار کنن. اگر کارمند تامین اجتماعی‌اند اولین شعبه تامین اجتماعی که هست برن اونجا کار کنن
😟
گفته دو میلیون خودرو میاد کارمند ما اگر یه میلیون از این کارمندها رو بگیم روزانه نیان سر کار تعطیل کنیم اداره رو یا بگیم اولین اداره‌ای که می‌بینن برن اونجا بشینن کار کنن.
گفته یه میلیون خودرو هرکدوم روزی بیست لیتر مصرف می‌کنن یه میلیون ضربدر بیست لیتر می‌شه بیست میلیون لیتر مسئله بنزین حل می‌شه
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71183" target="_blank">📅 14:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71181">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c318eb355.mp4?token=syVL68JNC_ZP5TAsB1MUGepEiYmgLKMm6NTC9gZ5yb2QOmjI_Yt9I4JmzEygSRKO3uiDcfcRK_QhaAfMKcCszMo4L_36i-wa7c3dMHEzJTyFK4vMTQjS1kzYAysJWWB45hTFPp2T184-n0izOChpjVRY3fH7aKhrQSbv6SCyI0-tjZjGO2C7K8S8mLfmIRshMkS31Jr-YqEOMJ05eBggwxRw5TH0KwZpwoAMb9cFWcvKUdGjgWqfN9N9_jV9b9nvFBaTTGo0r-QvCUKEx6AB-zYG-YUJrC44rx642MPPBjKZzJOXP1oHjOL6dJys_Sx1EEvjm0p3XvDYiWdNTHjqng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c318eb355.mp4?token=syVL68JNC_ZP5TAsB1MUGepEiYmgLKMm6NTC9gZ5yb2QOmjI_Yt9I4JmzEygSRKO3uiDcfcRK_QhaAfMKcCszMo4L_36i-wa7c3dMHEzJTyFK4vMTQjS1kzYAysJWWB45hTFPp2T184-n0izOChpjVRY3fH7aKhrQSbv6SCyI0-tjZjGO2C7K8S8mLfmIRshMkS31Jr-YqEOMJ05eBggwxRw5TH0KwZpwoAMb9cFWcvKUdGjgWqfN9N9_jV9b9nvFBaTTGo0r-QvCUKEx6AB-zYG-YUJrC44rx642MPPBjKZzJOXP1oHjOL6dJys_Sx1EEvjm0p3XvDYiWdNTHjqng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
〰️
ناو هواپیمابر «یو‌اس‌اس آبراهام لینکلن» (CVN-72) اسکله C-0 در بندر «لائم چابانگ» واقع در استان چونبوری تایلند را ترک کرد و مسیر خود را در عرض اقیانوس آرام به سوی پایگاه اصلی‌اش در سن‌دیگو در پیش گرفت.
خروج این ناو در صبح روز ۶ سپتامبر، به توقفِ حدوداً چهارروزه‌ای که از ۲ سپتامبر آغاز شده بود پایان داد و مرحله بعدیِ مسیر بازگشت آن به ایالات متحده را رقم زد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71181" target="_blank">📅 13:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71180">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/003437fd92.mp4?token=UDHpKZ6wUlhBD7tD_maHAlXPASJg9r4qrKJCB5DNvD6tf0HXXG5AHLxXZ4dcxHKFH8RuYTwSOuxmVF90tbO_gU9Jh0q1sWebDfZ_EQ2w4F9X-Z_wOWNMr6pZcH-wFGm_qfIfInn7C5kRCfDnf8gNFy34kvLyhVk5FtW7l-Ls7rbyckvtGkLf39nmqJJaoAUCwmhMGwlDcTYTMz22ukTyp7S0HkJ9VJdjLXWbxmSAs8Osu0cBkuhQhOJjW5yjdGojtb1xna3trJJ2jb5oIzUnl9gQ7bSBztfyHs3fYdaao9xZFGEc-MAd_L6kFKBKH7xF11Xp_NDZZan7VQjnDM3rFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/003437fd92.mp4?token=UDHpKZ6wUlhBD7tD_maHAlXPASJg9r4qrKJCB5DNvD6tf0HXXG5AHLxXZ4dcxHKFH8RuYTwSOuxmVF90tbO_gU9Jh0q1sWebDfZ_EQ2w4F9X-Z_wOWNMr6pZcH-wFGm_qfIfInn7C5kRCfDnf8gNFy34kvLyhVk5FtW7l-Ls7rbyckvtGkLf39nmqJJaoAUCwmhMGwlDcTYTMz22ukTyp7S0HkJ9VJdjLXWbxmSAs8Osu0cBkuhQhOJjW5yjdGojtb1xna3trJJ2jb5oIzUnl9gQ7bSBztfyHs3fYdaao9xZFGEc-MAd_L6kFKBKH7xF11Xp_NDZZan7VQjnDM3rFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی ایتا و روبیکا، ناو جرالد فورد رو بمبارون و غرق کردن
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/71180" target="_blank">📅 13:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71179">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71179" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/71179" target="_blank">📅 13:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71178">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLa0BzHCsWqzoE6Gn_zylpf7gzWlm-DekfxB34mEqIgP5AkEQiUZOiIhSb14XC8KzMmhqPAYgP1NCqLJvK4m-WnUdW_b_l-Jw8gGQ4Sl_glY0viZb6ljgk2nA8K5WrNu9f3UsME5FybQsMgNMDg40DicctNrI-w336fj5rD_2P-msAJe-rJN8fNPIO0IdYt3GRo9QLvVJ1Y9Hbm0Rd5guY7x7xEvDJm-A7L08BeHc5KJH1qxoXQRofFzYXVB-rPEO97-VqgJFrYu-ELhhHpqgDbI69pIMMyztbZ1we_N6kliVynm2QlINZdnviaEVb7cF2LVEu3DICi8syQ9tmNjSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید
.
اورتون
🆚
منچستریونایتد
آرسنال
🆚
چلسی
آلومینیوم
🆚
استقلال
والنسیا
🆚
بارسلونا
یوونتوس
🆚
میلان
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز و برداشت آسان و امن
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/71178" target="_blank">📅 13:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71177">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3c6743716.mp4?token=shWpq0Fh8vbfMc6EF2zUmmSV2Dd5iDHwPsDg89bu6SfSkFddaMgmx4FgUaM8wTnH5Ruyk7RxOAuPLjW3fknFuHiFH6_Tg320jds5gy1lU4_0X3iM4WRFQMz_7sUTyoUj45RzdyA8lekm4o-4ya4h23GZlb0iVpIKVIsw7A9ee5JOo_hKZHGngc5gSRnlwNzp2fDbj_J2Yf6gS_E1-P0MuDmQbadCcW4GD8hbQW5gsY44x5kwwLg1xy4uennQut9OSrl5nWeK6Ijk1DmVUG0C1uR760lTPNmE6tDnX6Tv2ZN2Se5JOEYSzQKSrRkqdXQZQXwTP491OSFInvqnoBtdjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3c6743716.mp4?token=shWpq0Fh8vbfMc6EF2zUmmSV2Dd5iDHwPsDg89bu6SfSkFddaMgmx4FgUaM8wTnH5Ruyk7RxOAuPLjW3fknFuHiFH6_Tg320jds5gy1lU4_0X3iM4WRFQMz_7sUTyoUj45RzdyA8lekm4o-4ya4h23GZlb0iVpIKVIsw7A9ee5JOo_hKZHGngc5gSRnlwNzp2fDbj_J2Yf6gS_E1-P0MuDmQbadCcW4GD8hbQW5gsY44x5kwwLg1xy4uennQut9OSrl5nWeK6Ijk1DmVUG0C1uR760lTPNmE6tDnX6Tv2ZN2Se5JOEYSzQKSrRkqdXQZQXwTP491OSFInvqnoBtdjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
سنتکام ویدئو غرق شدن نفتکش ایرانی در دریای عمان را منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71177" target="_blank">📅 13:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71176">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⏺
🇮🇷
قالیباف:
آمریکایی‌ها باید دریافته باشند که دوران «پاسخ‌های متناسب» به سر آمده است.
حملات ما به پایگاه‌های متجاوزان تنها یک آغاز بود.
قواعد بازی تغییر کرده است.
از این پس، هرگونه تجاوز به منافع ایران، پاسخی سریع‌تر، سنگین‌تر و دردناک‌تر در پی خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71176" target="_blank">📅 12:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71175">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20d5a31326.mp4?token=WCIXwXYIV44dZKFF2JrKc9M2-RlRHijOUKcYtSUo_WnpHuSGopy4ippSXLhaoCUn4NiPQxSflbWU_GygXJFXjpxCUjsGcy4SMu3RC1ghyX8q6sX6OI0NG8chXcq0VtKR942bmly4Rn6nZ7Atb4bmREHy3DrAw-utVMdvnbo9tKchjyHrjykkCVgFiB5zdDG390Te_vUlUjvPAHYsiH8G5DjWHTEtVQENy_XZopuDOTNK9R5yWQNbkXmtVmCgcdD6ehYK5_JIWtEHj_197cHufcdogWGQfO7mUAKcTOyk6kJeDpCOL45sKomCvUNf0ly3JtSLUuxjo6hGkiSMFMDRvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20d5a31326.mp4?token=WCIXwXYIV44dZKFF2JrKc9M2-RlRHijOUKcYtSUo_WnpHuSGopy4ippSXLhaoCUn4NiPQxSflbWU_GygXJFXjpxCUjsGcy4SMu3RC1ghyX8q6sX6OI0NG8chXcq0VtKR942bmly4Rn6nZ7Atb4bmREHy3DrAw-utVMdvnbo9tKchjyHrjykkCVgFiB5zdDG390Te_vUlUjvPAHYsiH8G5DjWHTEtVQENy_XZopuDOTNK9R5yWQNbkXmtVmCgcdD6ehYK5_JIWtEHj_197cHufcdogWGQfO7mUAKcTOyk6kJeDpCOL45sKomCvUNf0ly3JtSLUuxjo6hGkiSMFMDRvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف:بستن تنگه هرمز به ضرر ایران شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71175" target="_blank">📅 12:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71174">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8313313bb.mp4?token=ZUzxWwEX2OLx-zL_HXxLo_ha3OPUDSeaLhkLrxTv2x3CRHkZojQmwtqTQZH_saVVcpt5BnCTEylAlPgkzIEFfF-Litp_aNo3lHv6PLejoQUQg1yrjRgsWnu3GGZdEhRR19Pz0wEriFRVug5XG3z-L0dlpWJq9HiBFUjJ0gNdsf0Y4TvY4sAmNEOVkXxgWLPvCG0xHuBlLWj1ieEvisUuJCp3RqryCWZX3dhST4j--oxUKhNMc0FxIo2xw8hge6ML_knC-CBUDqu_tn4-L4UVu3EEizgS_o9bZgMs5a-4qvOvmbItPjOPinyXI1RAZVGJdMAgG4cYXTKhxMXejeqWPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8313313bb.mp4?token=ZUzxWwEX2OLx-zL_HXxLo_ha3OPUDSeaLhkLrxTv2x3CRHkZojQmwtqTQZH_saVVcpt5BnCTEylAlPgkzIEFfF-Litp_aNo3lHv6PLejoQUQg1yrjRgsWnu3GGZdEhRR19Pz0wEriFRVug5XG3z-L0dlpWJq9HiBFUjJ0gNdsf0Y4TvY4sAmNEOVkXxgWLPvCG0xHuBlLWj1ieEvisUuJCp3RqryCWZX3dhST4j--oxUKhNMc0FxIo2xw8hge6ML_knC-CBUDqu_tn4-L4UVu3EEizgS_o9bZgMs5a-4qvOvmbItPjOPinyXI1RAZVGJdMAgG4cYXTKhxMXejeqWPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
ویدیویی که در توییتر فارسی به شدت در حال وایرال شدنه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71174" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71173">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f8295abc0.mp4?token=gQ9Ch83aKMeFIeq0KSbrrYARWxMRdcfkiGc-eShUCxqcEx3wRHky-EzlA-nO4Ff-8QwClcsoBrNETN4sxjgkjtH6eJX8L_HwOquvIQN9AYjnTtc0KMhB-l3vkUbVjiQ-UkK9_4f1HvdYKXWQiWrica3ShbJUfwOoqFE_prwbq2J5WDU0jzKuw8b4y0d894QXYb-UdHFIJXE4_q3hjjBpo8sKoiDUY79SpfOuSpWpbBFLIAmuUhYqb3PuYX1VdTcAPsjqlBWCXECjE0n_-zFD_J2fiU23rASQ24Zil6aNrcnXLlcj3nDwZNKxaHGohGXYDpMFsBzvC3PPT7aO52m7bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f8295abc0.mp4?token=gQ9Ch83aKMeFIeq0KSbrrYARWxMRdcfkiGc-eShUCxqcEx3wRHky-EzlA-nO4Ff-8QwClcsoBrNETN4sxjgkjtH6eJX8L_HwOquvIQN9AYjnTtc0KMhB-l3vkUbVjiQ-UkK9_4f1HvdYKXWQiWrica3ShbJUfwOoqFE_prwbq2J5WDU0jzKuw8b4y0d894QXYb-UdHFIJXE4_q3hjjBpo8sKoiDUY79SpfOuSpWpbBFLIAmuUhYqb3PuYX1VdTcAPsjqlBWCXECjE0n_-zFD_J2fiU23rASQ24Zil6aNrcnXLlcj3nDwZNKxaHGohGXYDpMFsBzvC3PPT7aO52m7bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به گفته آقای دکتر اگه می‌خوای سرطان پروستات نگیری، باید ماهی ۲۱ بار سکس کنی...!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71173" target="_blank">📅 11:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71172">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b321711db4.mp4?token=t7IN4Ae5hSlzneuLiJPVjiyNhoSN0UYCvRy459E9f3vn5lmn4ibmkODbiGuvtgKEv7yzVZPYgrrzLRJuF63oMDBnLuh_tX2KLw7AMzhWQqcV8PBifhhclOPO2O57cZ1AYgeuNGIn6jpObWD3ucBDnvq6lHBHaJqxkmWRtmBPjO7BFrXHyRJ8NdHNLnWQc-FzRXJ_2andnd8R4SddLkudCA-2Q6g_HTgdo6sSKocI4lLLpwBP5dWCLXu_5jq41M44Gm3T5KNVE_DLYYqP81eeNTqXJ2eAJLHtKtofQtEUIUHfsReq2fSpuE7-kAIbZEvaNO4pxEMplyzBOEdjb8ERWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b321711db4.mp4?token=t7IN4Ae5hSlzneuLiJPVjiyNhoSN0UYCvRy459E9f3vn5lmn4ibmkODbiGuvtgKEv7yzVZPYgrrzLRJuF63oMDBnLuh_tX2KLw7AMzhWQqcV8PBifhhclOPO2O57cZ1AYgeuNGIn6jpObWD3ucBDnvq6lHBHaJqxkmWRtmBPjO7BFrXHyRJ8NdHNLnWQc-FzRXJ_2andnd8R4SddLkudCA-2Q6g_HTgdo6sSKocI4lLLpwBP5dWCLXu_5jq41M44Gm3T5KNVE_DLYYqP81eeNTqXJ2eAJLHtKtofQtEUIUHfsReq2fSpuE7-kAIbZEvaNO4pxEMplyzBOEdjb8ERWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇹🇷
این پسر بچه ارومیه ای که چند وقت پیش با ویدیوش که در حال آهنگ خوندن بود توی اینستاگرام به شدت وایرال شد حالا یه کمپانی بزرگ از ترکیه اومده و باهاش قرارداد همکاری بسته؛
فعلا این قرارداد واسه اجرای کنسرت های مختلف تو ترکیه‌ست
رئیس کمپانی میگه که این تازه اول راهه و قراره بزودی تو سراسر جهان کنسرت برگزار کنیم...
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71172" target="_blank">📅 10:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71171">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99e529d142.mp4?token=FUSmnnKaODjdZG6SGjp8GiHyCYHxPq9nuGNFC9j8PtnFKa-OEamnJPimog4yQo0kxxdP8RI0sbr71YX--rKXwPTCtq7USq6sPlivqpdp-hqPtNwmMNaVBDTlXpv7EczHCkEjMIrum0k7NcTI-Ajwsx1gzhYNxuoAEA9WedEtIVfHmxxCKswBMTQQFuedoUO3Ds800IYSTqYa4jtQ1m4i9V3hYdzO-zrhzk_vMZYotQmmJKMG85jCVb5InHe0DVcMITWb0BhilkvMiP7bu_hxvosu01ZKlwaj4LdajDmSI9W-1fty3eZUeFz0zRgZsal9Dr6eP71-SV1lBTJ7sjR4sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99e529d142.mp4?token=FUSmnnKaODjdZG6SGjp8GiHyCYHxPq9nuGNFC9j8PtnFKa-OEamnJPimog4yQo0kxxdP8RI0sbr71YX--rKXwPTCtq7USq6sPlivqpdp-hqPtNwmMNaVBDTlXpv7EczHCkEjMIrum0k7NcTI-Ajwsx1gzhYNxuoAEA9WedEtIVfHmxxCKswBMTQQFuedoUO3Ds800IYSTqYa4jtQ1m4i9V3hYdzO-zrhzk_vMZYotQmmJKMG85jCVb5InHe0DVcMITWb0BhilkvMiP7bu_hxvosu01ZKlwaj4LdajDmSI9W-1fty3eZUeFz0zRgZsal9Dr6eP71-SV1lBTJ7sjR4sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇱🇧
خبرنگار جمهوری اسلامی در لبنان:
اعضای سپاه پاسداران در تپه‌های علی‌الطاهر، به دلیل محاصره اسرائیل، در شرایط عاشورایی قرار دارن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71171" target="_blank">📅 10:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71170">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a662811c73.mp4?token=DknzSltuync5bBFkTl5BxKGUpDnZ1cO9e3yiH-hWc_00NrQJRqY7YQo3B8Wv3OwiFs9Z4HmfDoecbS5kQRDHhQpG5zslbj7Zgr3-bBdte0bIZVUiqwV-Pwtn2hAiD8hGgxTB46i0ldpUWV9zVION219411ucyTHbbSfApghn4MNCoxEzJRtEbLof5alZAKNN2GY9QeQHPjWImvohYvkK1Ck83QCDT1kKvV2XA3ny-iNqJDvq3rEsHeC-IjMpiky2gC8zvQPcDjtNxAvi0u5tQWy2N52F-kU9J3mnpIgV2ISxlDIiBbvgeHJi2qUof_s45-knmdFNmpIlLElI86Ah1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a662811c73.mp4?token=DknzSltuync5bBFkTl5BxKGUpDnZ1cO9e3yiH-hWc_00NrQJRqY7YQo3B8Wv3OwiFs9Z4HmfDoecbS5kQRDHhQpG5zslbj7Zgr3-bBdte0bIZVUiqwV-Pwtn2hAiD8hGgxTB46i0ldpUWV9zVION219411ucyTHbbSfApghn4MNCoxEzJRtEbLof5alZAKNN2GY9QeQHPjWImvohYvkK1Ck83QCDT1kKvV2XA3ny-iNqJDvq3rEsHeC-IjMpiky2gC8zvQPcDjtNxAvi0u5tQWy2N52F-kU9J3mnpIgV2ISxlDIiBbvgeHJi2qUof_s45-knmdFNmpIlLElI86Ah1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شاهین نجفی:
هرکسی رضا پهلوی رو مورد انتقادهای عجیب غریب قرار میده و میزنتش یه سرش وصل میشه به جمهوری اسلامی
اینا جوگیر شدن چهارتا شعار دادن و حرف زدن بعد دیدن اینجا خبری از سهم دهی به کسی نیست مسیرشون رو عوض کردن
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71170" target="_blank">📅 09:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71169">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d150aea8.mp4?token=GN-74MSeoqDpq0cAtAkdEtuOWsMiS1M_Umxju9KkZaywSPpdCv30QciYT1zXbxd-K5sVPad6CjbQyJgU6q08NeT62admDTovs1rViVQ1hopw1sWLL1E6X3T-XMuFmZSTFdM-ZrJqRDgkjHl30bvtulOaT6gSVC3Gk7SZB0hyt2WZe3ZvrY5LLWKVIa4OS-U01j1lIH7oLR3bWtNTY6qMOKk58wCxQipiwEU3jFJUu5O4uLV8ugHovlK7KuiX_f6w7HOSzW80NsQH8RD_yW7pOJ8FqC4lwuYhrTqzocXJS1foEQSQWjVuF2h9dDmDiEKI59SVgY1xR9f8khupZTLzGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d150aea8.mp4?token=GN-74MSeoqDpq0cAtAkdEtuOWsMiS1M_Umxju9KkZaywSPpdCv30QciYT1zXbxd-K5sVPad6CjbQyJgU6q08NeT62admDTovs1rViVQ1hopw1sWLL1E6X3T-XMuFmZSTFdM-ZrJqRDgkjHl30bvtulOaT6gSVC3Gk7SZB0hyt2WZe3ZvrY5LLWKVIa4OS-U01j1lIH7oLR3bWtNTY6qMOKk58wCxQipiwEU3jFJUu5O4uLV8ugHovlK7KuiX_f6w7HOSzW80NsQH8RD_yW7pOJ8FqC4lwuYhrTqzocXJS1foEQSQWjVuF2h9dDmDiEKI59SVgY1xR9f8khupZTLzGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صداوسیما آمار رسمی کشته شدگان اسرائیل تو سه روز اول جنگ رو منتشر کرد:
۶عدد ژنرال ارشد اسرائیلی
۳۲ نفر مامور موساد و ۷۸ نفر مامور شین بت
یازده دانشمند هسته‌ای
۱۹۸ نفر افسر نیروی هوایی
۴۶۲ سرباز و ۴۲۳ نیروی ذخیره ارتش اسرائیل کشته شدند
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71169" target="_blank">📅 09:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71168">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
سپاه پاسداران انقلاب اسلامی ساعاتی قبل در بیانیه ای مدعی حمله به یک ناو هواپیمابر و یک ناوشکن آمریکایی شد و اعلام کرد که پس از این حمله اونا خسارت دیدن، ترسیدن و از منطقه فرار کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71168" target="_blank">📅 08:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71167">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71167" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71167" target="_blank">📅 01:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71166">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjIEiUMi_KBmioT68QbN53CbczX2ygQJcZK0IYg6jwA-OE3IwmjFqC7D9ozQMqxjR5YVrY9hqAHYJhDluZUEx8N4W-oJ45JWsIaxW1HtTzp6QVTXWI70UIiaKGx2PuVSnxhNzONBfm8i0bT6j4j38YHCOsBvn5qCVS9mM6q4Dfd-JWkiELsWe2U2DnVR-89bCnQ1SbZHY_faSLQcLu5Be_RYunfiw0t-5l1e0GuungRjaKPULQfSz-LrVjCQFFtbZdIVxJcIKAQF58Ms3rTRAP67CgDYh3klVWyKUOZ8InscC6UWMeXUp6lzAfM8wdDS4Z1tfkfC8UMwovnFTqg-yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
تنیس US Open داغ‌تر از همیشه دنبال میشه!
🦖
مسابقات جذاب
US Open
رو در
TrexBet
پیش‌بینی کنید، هیجان رقابت‌ها رو بیشتر کنید و برای جوایز جذاب وارد رقابت بشید!
🦖
فرصت هیجان
US Open
رو از دست ندید!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71166" target="_blank">📅 01:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71165">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ویس فحاشی خداداد</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/news_hut/71165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
🚫
فوتبال مملکت هم اوضاع جالبی داره.  خداداد عزیزی امشب کلش فوق‌العاده کیری شده و اینجوری خواهر و مادر امید عالیشاه رو به فوش کشیده
😳
😳
😳
😳
😳
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71165" target="_blank">📅 01:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71163">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c0f365bbb.mp4?token=HFSs3dGd6bngEWuIT2bNXKegGQaheh-VsdXVedqBNconeR_KtKOasDRyQAlory9z4j3Knh4JpHhKR1p5LX0M7xAFMJnqvdtfimTLsdSNhpWwyQ2NHG_vv5vieR5lK_I4uVaBP_HivEyCJc9knEZJyWXFJbOOn_3CSX36qYCEE7rbISu8ummj0tyDeh7LB1httAuxECQ6zNVkbLNs27ZPc7deYH87ysYdsFBUgrOQfMvmAZEdCFDniAfmeTJdNvtsi0JrWQCkFdxAoLVHdVqVtlXm1XnHCEJfWl29ydv8xw3mIRNCW4HLtvIopErVA9iFSDMCpSjV2raQ4IKij9LArw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c0f365bbb.mp4?token=HFSs3dGd6bngEWuIT2bNXKegGQaheh-VsdXVedqBNconeR_KtKOasDRyQAlory9z4j3Knh4JpHhKR1p5LX0M7xAFMJnqvdtfimTLsdSNhpWwyQ2NHG_vv5vieR5lK_I4uVaBP_HivEyCJc9knEZJyWXFJbOOn_3CSX36qYCEE7rbISu8ummj0tyDeh7LB1httAuxECQ6zNVkbLNs27ZPc7deYH87ysYdsFBUgrOQfMvmAZEdCFDniAfmeTJdNvtsi0JrWQCkFdxAoLVHdVqVtlXm1XnHCEJfWl29ydv8xw3mIRNCW4HLtvIopErVA9iFSDMCpSjV2raQ4IKij9LArw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سپاه پاسداران تصاویری از «رصد و رهگیری شناورهای متخلف» در تنگه هرمز منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/71163" target="_blank">📅 00:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71162">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e9440ae83.mp4?token=Zt0ZlwM-HnP-jrZE2H_kLkUw3351WDrqVoIOVD1tbeUDclGejT7FucNGzqQvmmyQlrS6xZUi1lQgrgFQ7u1PVZSANTKllxPpDP34UCot20rapqxooxyBQW8hLg52pGPyEeggHfbV0-AnXtPLqseQgvXxjVUGpg-tFjXur5R1Wj0cSLJ3KEBQozUzBI99K4rQp7cXSC_gKN8R1n4feBvZCquqLfs708gZqXGmNVxWLca3h2jEl1yIVzaWvP42M_riUz-HTsSuER1avcbG0IBmYkNTbcgNtbbDMp06q2kQwoDG0KsGlgdoh8zm7J35pLxodl75Q8tFXColvAD5WUimzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e9440ae83.mp4?token=Zt0ZlwM-HnP-jrZE2H_kLkUw3351WDrqVoIOVD1tbeUDclGejT7FucNGzqQvmmyQlrS6xZUi1lQgrgFQ7u1PVZSANTKllxPpDP34UCot20rapqxooxyBQW8hLg52pGPyEeggHfbV0-AnXtPLqseQgvXxjVUGpg-tFjXur5R1Wj0cSLJ3KEBQozUzBI99K4rQp7cXSC_gKN8R1n4feBvZCquqLfs708gZqXGmNVxWLca3h2jEl1yIVzaWvP42M_riUz-HTsSuER1avcbG0IBmYkNTbcgNtbbDMp06q2kQwoDG0KsGlgdoh8zm7J35pLxodl75Q8tFXColvAD5WUimzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇬🇷
یک فروند جنگنده F-4 فانتوم نیروی هوایی یونان در جریان رویداد «هفته پرواز آتن» در پایگاه هوایی تاناگرا سقوط کرد و دو خلبان این جنگنده کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/71162" target="_blank">📅 00:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71161">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a02f1d06a.mp4?token=Iq7Fq64UmkQ0kMHXXmByWltp5XaNcbfx7ZG9uSliOkmTwR_ijztkXQkE24oVOREZQkAGkeCfVmcC0fStT0C3f6I6N8CvZwScJ5FbyF3mjQB-ANpffvcbzIoWbfmNzv083tUq8MxF0oriy3fd7e4qQxtaNEps4YvkhCsMEojmIj8xYv6Q_4Jy-uXZfCF--9I6PGpO7VnPB1Dou0FsG70iEtIGUTbyxozdejfzSbD6Nt0YbPkh-DmFwA9QJw0948MhWgS5w3-LHv0i8A-O_qKma4Ov9YhVQ91SWPC4sBwm-igkoBtlABVKDiqLBsE0OZUzyDYAXjOK13fRSMTY2wGghg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a02f1d06a.mp4?token=Iq7Fq64UmkQ0kMHXXmByWltp5XaNcbfx7ZG9uSliOkmTwR_ijztkXQkE24oVOREZQkAGkeCfVmcC0fStT0C3f6I6N8CvZwScJ5FbyF3mjQB-ANpffvcbzIoWbfmNzv083tUq8MxF0oriy3fd7e4qQxtaNEps4YvkhCsMEojmIj8xYv6Q_4Jy-uXZfCF--9I6PGpO7VnPB1Dou0FsG70iEtIGUTbyxozdejfzSbD6Nt0YbPkh-DmFwA9QJw0948MhWgS5w3-LHv0i8A-O_qKma4Ov9YhVQ91SWPC4sBwm-igkoBtlABVKDiqLBsE0OZUzyDYAXjOK13fRSMTY2wGghg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه خانم درباره اقتصاد:
چرا مردم هر چی گرون میشه از زاویه ی آدمای متوسط بهش نگاه می‌کنن؟
خونه از ۵ میلیارد شده ۵۰ میلیارد.
گوشت از ۵۰۰ تومن شده ۴ میلیون.
سود شما چند برابر شده.
مردم از گرونیا دارن سود میکنن، مردم باید دیدگاهشون از آدمای متوسط جامعه تغییر بدن و بگن هر چی گرون میشه خب ما هم سودمونو داریم میبریم
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/71161" target="_blank">📅 23:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71160">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d7d2ec60.mp4?token=TPYLHapmj58bopj7U7dqfn3r_jLTq2QLGL1RGd2EASGp1vnxtQGVo8EWW2VLyuXExUTAx8wgU2IRL7EG_N4-xXljKPg4dl0Ly_2_fXOSFNyZCQiSy-08aZYQrofNVIxRzG4IdGeZD8P8ENjP7AjSAk_5Gqy73fF7_9aom3-k9uxD1fPkL-MCkcR7v-OZyxLNGSgQHnnM78h8znk5hn4CjEnkTCu8YSqxryMX0o-IbIAk8LTYPh34LA-NtYEFnvnZYWyI3x7P_5HtaGZxvCB9Lh-rKZ_votWRUUZ4zhPHQ83g5D5-qKIBWRFNVAIomH1_6dQHBtPpvH9KkVbtM21rlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d7d2ec60.mp4?token=TPYLHapmj58bopj7U7dqfn3r_jLTq2QLGL1RGd2EASGp1vnxtQGVo8EWW2VLyuXExUTAx8wgU2IRL7EG_N4-xXljKPg4dl0Ly_2_fXOSFNyZCQiSy-08aZYQrofNVIxRzG4IdGeZD8P8ENjP7AjSAk_5Gqy73fF7_9aom3-k9uxD1fPkL-MCkcR7v-OZyxLNGSgQHnnM78h8znk5hn4CjEnkTCu8YSqxryMX0o-IbIAk8LTYPh34LA-NtYEFnvnZYWyI3x7P_5HtaGZxvCB9Lh-rKZ_votWRUUZ4zhPHQ83g5D5-qKIBWRFNVAIomH1_6dQHBtPpvH9KkVbtM21rlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه جانفدای رندوم و حرکات جالبش
😃
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/71160" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71159">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66b1ca1096.mp4?token=eTYnj8ftxMMuIvUTAxXLcVFTP6jgu7I66VhEjnOKLbPy6DmS-YMO4pex24Bf_tjZC259F8f9iOHcHzyE49NTlBmrDYetQ00Qausw2ZgGaXZkGOyRduxXvOcmp5emYBHjAkMczvoIWe2N5NVnDtFNmR5WV4xgNhyTFONdKLECwcMpNx1hojQvVmqHO1Kn1eNr68nc6H5RQGphDTmJbCb65NYHItmLvcPM5P-gFlLBnxphKGv2Jf22LIxjZS9RfXbiCTvHVMmuODiWzIpY7je-Ix4Dw1amg-szsOqP3gDWoXPIi3PCnAJZQOcpaThJBNKQwA1eLVTCyivysiDW2lPVaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66b1ca1096.mp4?token=eTYnj8ftxMMuIvUTAxXLcVFTP6jgu7I66VhEjnOKLbPy6DmS-YMO4pex24Bf_tjZC259F8f9iOHcHzyE49NTlBmrDYetQ00Qausw2ZgGaXZkGOyRduxXvOcmp5emYBHjAkMczvoIWe2N5NVnDtFNmR5WV4xgNhyTFONdKLECwcMpNx1hojQvVmqHO1Kn1eNr68nc6H5RQGphDTmJbCb65NYHItmLvcPM5P-gFlLBnxphKGv2Jf22LIxjZS9RfXbiCTvHVMmuODiWzIpY7je-Ix4Dw1amg-szsOqP3gDWoXPIi3PCnAJZQOcpaThJBNKQwA1eLVTCyivysiDW2lPVaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش تو مسیر پلیس‌راه همدان ـ سنندج، یه ماشین سنگین گویا ترمز می‌بره و مستقیم با یه دستگاه تانکر حامل سوخت برخورد می‌کنه و یه انفجار وحشتناک رخ میده!
متاسفانه تا الان 7  جونشون رو از دست دادن...
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/71159" target="_blank">📅 22:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71158">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aea156fe3.mp4?token=lk5E_IDwb9GAwUbVVtUaSzd45E8t7xReF-39ErZiezV9jS1rK8lu-cPApxS4aedU2UlXYzMGiP_9e0yiYCHW5_fyd4Kpg3oc6N_-SSr8TGe9HGUA_c40P3Mcvu5H75BcebMtWzHPJoaHxFDPHp6jQ3lAWMk3UZD0qBEtDgce2EGcRJmQP4bzta0DgsZ0sVPdpuHfwgc0LJ4KUgLOb9t5PnUmMp8PxPs4zgfQh_nXnY6FtW_P3mkYbG7M28f8TjCEPCFPwD9B3BV7oFQo5FQmcGAWlPSniDFpypuWOkQCjmwWknIl7e9Up4X6745fRdNV3sCSnBGIrqhtVzCSOLYrJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aea156fe3.mp4?token=lk5E_IDwb9GAwUbVVtUaSzd45E8t7xReF-39ErZiezV9jS1rK8lu-cPApxS4aedU2UlXYzMGiP_9e0yiYCHW5_fyd4Kpg3oc6N_-SSr8TGe9HGUA_c40P3Mcvu5H75BcebMtWzHPJoaHxFDPHp6jQ3lAWMk3UZD0qBEtDgce2EGcRJmQP4bzta0DgsZ0sVPdpuHfwgc0LJ4KUgLOb9t5PnUmMp8PxPs4zgfQh_nXnY6FtW_P3mkYbG7M28f8TjCEPCFPwD9B3BV7oFQo5FQmcGAWlPSniDFpypuWOkQCjmwWknIl7e9Up4X6745fRdNV3sCSnBGIrqhtVzCSOLYrJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وزیر نیرو:
دیگر قطعی برق برنامه‌ریزی‌شده نداریم
اگر مردم جایی دیدند به سامانهٔ ۱۲۱ اطلاع دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/71158" target="_blank">📅 21:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71157">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31160c5df1.mp4?token=tWPfe6rbBjGHosUP_fK94Sf0cMj6mOhmzVGjRqNKIenGiHx8Jcfo_R1Pm21p9HGdFnnvvEL7SwNSOerexpKPlt7-YaF8y7MgWgroeNNWVNwzh6w1u1ccFHYCp_V-Nqs8O1Lz0pa6qmwW39BSv1qfiYxSzUI0RCx5h_WWGOltHXZYRlXsqHniXdRfREfDFd7kLpySxczF0tkIHHGatr3POAY_NqS6xKhm8sqxCZrz-4ufrh9BAdL3IR5YJ0foWaKOVgXEEaQifIR0tR0HNGUGDeJnKV6j9gaBn8_6siSdpLqQqvHVY2I9Ywc1pzS8FLa_m74tWxcY6lnUhOj4-oluh4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31160c5df1.mp4?token=tWPfe6rbBjGHosUP_fK94Sf0cMj6mOhmzVGjRqNKIenGiHx8Jcfo_R1Pm21p9HGdFnnvvEL7SwNSOerexpKPlt7-YaF8y7MgWgroeNNWVNwzh6w1u1ccFHYCp_V-Nqs8O1Lz0pa6qmwW39BSv1qfiYxSzUI0RCx5h_WWGOltHXZYRlXsqHniXdRfREfDFd7kLpySxczF0tkIHHGatr3POAY_NqS6xKhm8sqxCZrz-4ufrh9BAdL3IR5YJ0foWaKOVgXEEaQifIR0tR0HNGUGDeJnKV6j9gaBn8_6siSdpLqQqvHVY2I9Ywc1pzS8FLa_m74tWxcY6lnUhOj4-oluh4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
جان بولتون دیپلمات آمریکایی درباره ایران:
من معتقدم — و دهه‌هاست که چنین نظری دارم — که تنها راه دستیابی به صلح و امنیت واقعی و پایدار در خاورمیانه، خلاص شدن از شر رژیم تهران است.
به گمانم حملات آمریکا و اسرائیل آسیب قابل‌توجهی به این رژیم وارد کرد.
بی‌شک ما اشتباهات زیادی مرتکب شدیم.
اما اگر اراده کنیم که درباره چگونگی انجام آن به‌درستی بیندیشیم، این هدف همچنان قابل‌تحقق است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71157" target="_blank">📅 21:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71156">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
صداوسیما:
صدای انفجار هایی که در جزیره قشم شنیده شده مربوط به شلیک موشک ها به سمت شناور های متخلف در تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71156" target="_blank">📅 21:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71155">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed43299c5.mp4?token=cWehphfEqa7gDizU8XtIinTRsDjlrP_wlX8I54wE0xbRvCesOxJSerMhBw_5L16sk2_ZUNyuRNavwQcJqbzDGZr_QsZcY8sPCk3lFMVFEQ-SjbeesnYx2CjKm9nXDWDAXLumnOYzfiBd0r0Rfsas83caJKS-mMngPKmHx-QTquTRrAhKctGdPqK1DJkFt-Qc8Q4JkwMPnvhqx9QoKj5eIuiTZYrO2cFE5r36vs0aO7GSAeYPaFIlvNXPb95lbptVKkh4Gt2r-sczG3c6B6uLpze3wldxd8TxRcoLD3k-LJo4uSkuD-amGwmTvGcQJzxX3a1mCpGygfQ1UcFlywfbJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed43299c5.mp4?token=cWehphfEqa7gDizU8XtIinTRsDjlrP_wlX8I54wE0xbRvCesOxJSerMhBw_5L16sk2_ZUNyuRNavwQcJqbzDGZr_QsZcY8sPCk3lFMVFEQ-SjbeesnYx2CjKm9nXDWDAXLumnOYzfiBd0r0Rfsas83caJKS-mMngPKmHx-QTquTRrAhKctGdPqK1DJkFt-Qc8Q4JkwMPnvhqx9QoKj5eIuiTZYrO2cFE5r36vs0aO7GSAeYPaFIlvNXPb95lbptVKkh4Gt2r-sczG3c6B6uLpze3wldxd8TxRcoLD3k-LJo4uSkuD-amGwmTvGcQJzxX3a1mCpGygfQ1UcFlywfbJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تصاویر منتشرشده نشان می‌دهد یک کشتی کانتینربر در اسکله بوشهر تقریبا به‌طور کامل نابود شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/71155" target="_blank">📅 20:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71154">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا UKMTO:
گزارش‌ هایی مبنی بر وقوع حوادث برای چندین کشتی تجاری در شمال خلیج فارس و دریای عمان دریافت کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71154" target="_blank">📅 19:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71153">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5717843ac.mp4?token=B4Y1M4VeoGXSYpl7kXiB6elmMFKZS6vfEt92H9IaDiQ9PSeV3sutUpzgkxI8a4_z82wYkFHh-0xPIyDfcGOFVgfwCATspJoZG3pYOzg8wnbTPU5pmLgDyBfTtsjePpYSd3NUtYLNGa30oVcP43m6vAsP7IDYepSfDeJwl4S1Fc9lIP5PSBOy9ft95nZcvorfS64REU0sUMsMsSanLlXy2iVdjjlvIdV0ERndBIlE-jLpL9ATMegRDEjaypEsFN03K2u_pzgnZRLqUkuCcFdP7FsPIRKFDRAEAvCr0OfXxngZttnuvmI15Cv0zqkXt1_cpIG40WsLYENe8FZJ991-xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5717843ac.mp4?token=B4Y1M4VeoGXSYpl7kXiB6elmMFKZS6vfEt92H9IaDiQ9PSeV3sutUpzgkxI8a4_z82wYkFHh-0xPIyDfcGOFVgfwCATspJoZG3pYOzg8wnbTPU5pmLgDyBfTtsjePpYSd3NUtYLNGa30oVcP43m6vAsP7IDYepSfDeJwl4S1Fc9lIP5PSBOy9ft95nZcvorfS64REU0sUMsMsSanLlXy2iVdjjlvIdV0ERndBIlE-jLpL9ATMegRDEjaypEsFN03K2u_pzgnZRLqUkuCcFdP7FsPIRKFDRAEAvCr0OfXxngZttnuvmI15Cv0zqkXt1_cpIG40WsLYENe8FZJ991-xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
✈️
ویدیویی تایید نشده از پرواز تانکر سوخت‌رسان آمریکایی به همراه دو جنگنده در آسمان جزیره کیش استان هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71153" target="_blank">📅 19:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71152">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71152" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71152" target="_blank">📅 19:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71151">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1-WnqBlSqGXarUbkvSOxX8GnqIumwVRTAOUuy9408m8ZKJSWNH7y_QosjMb1JP22PwFdJUHA9zn9dtrRH8H8VrvL6plxgD0M8ZME5r9uFUFFq5R3zU9sMu2s2DsEGYPOyFFpi937LETG5Pub-_o6-A414W0yEh3UI5qAa7eVeFgjSQ0cU073XGW7UrTb7unb7Ja2sroTm8uZeYBathn8j-4iIYpNbyTQcV2yn87pPW0j8UolvQsCWKtqYgYLsy4W-2rVgPiUmpyF8Buv6fK2VqJcyrIRw7igFLDE0lpyLKcIOE1i0N9HPHWnTDt6emPGvNr-KbGcOzxVDK3-ub14Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب اینتر
🆚
ناپولی را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار دو تیم:
اینتر: ۲ بازی ۲ برد و کسب و ۵ گل زده
ناپولی: ۲ بازی ۱ برد و ۱ شکست و ۳ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71151" target="_blank">📅 19:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71150">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf5e996b2c.mp4?token=QR5YUV4GBIG4iaA-8yvp9sfc285qR6cQFy9C3feDfIN-B3RhgZy3E5BQJ4kORQtHQBsRl--wb-xiyCK1NlYk61CUDCbN735Ugt2SczIu2XwNw2qqKl4E_QBd9I9L0sbhdsn5exwHQbOGgJkE1bXr5tXOrWAI_QdpyMB3u1NJUWZ_wpeWwg5Qc-yqI0kZKMvKfJJhRE0GvVc3FTPblbxepLgvOVgzdKMZ-91dNII5w1a80w8riAMi-dBImuxOxcsBpjipMNrMlEzpPCMxp98LMAr81zLmj97xZQuNegFYvyhM9Zi4LcBA2gSTWHrIjnOpTLBN2uyPhnuxNBKEOAHWHE24lNI9uEPgJ19_3oM2unIR-yNrCIIaKJy_jCw001yQo4QxZaA4b1UlIoP9C3lNw_58wxLKYp6xhtuvB0VVHMrNSAuDRhcnWJt6nAnSvzzkHJ8qYkPNlBx25fntbnqE64kwkZqO5hZxdpYYvWaZ_SFDaGKQoG6UsxrNoYtDIB_A558w5YbeUmZ50ZSAd3aDioTqugmGF2kl6IDepwXigNv0A_YFwn2iPf4K-oOa4ili4r9RybvhZ8D_Y2M0ehLUrx7wXOfZSc1wDz6tutMDYGEDa3fT77jBZmaEnzuLK0-aRE2188FtZZ47_vbmNmnFwyOrjsLkykCt_vuMVb5O9Xo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf5e996b2c.mp4?token=QR5YUV4GBIG4iaA-8yvp9sfc285qR6cQFy9C3feDfIN-B3RhgZy3E5BQJ4kORQtHQBsRl--wb-xiyCK1NlYk61CUDCbN735Ugt2SczIu2XwNw2qqKl4E_QBd9I9L0sbhdsn5exwHQbOGgJkE1bXr5tXOrWAI_QdpyMB3u1NJUWZ_wpeWwg5Qc-yqI0kZKMvKfJJhRE0GvVc3FTPblbxepLgvOVgzdKMZ-91dNII5w1a80w8riAMi-dBImuxOxcsBpjipMNrMlEzpPCMxp98LMAr81zLmj97xZQuNegFYvyhM9Zi4LcBA2gSTWHrIjnOpTLBN2uyPhnuxNBKEOAHWHE24lNI9uEPgJ19_3oM2unIR-yNrCIIaKJy_jCw001yQo4QxZaA4b1UlIoP9C3lNw_58wxLKYp6xhtuvB0VVHMrNSAuDRhcnWJt6nAnSvzzkHJ8qYkPNlBx25fntbnqE64kwkZqO5hZxdpYYvWaZ_SFDaGKQoG6UsxrNoYtDIB_A558w5YbeUmZ50ZSAd3aDioTqugmGF2kl6IDepwXigNv0A_YFwn2iPf4K-oOa4ili4r9RybvhZ8D_Y2M0ehLUrx7wXOfZSc1wDz6tutMDYGEDa3fT77jBZmaEnzuLK0-aRE2188FtZZ47_vbmNmnFwyOrjsLkykCt_vuMVb5O9Xo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
لحظه تهدید تخلیه خدمه نفتکش های جمهوری اسلامی توسط خلبان جنگنده ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71150" target="_blank">📅 18:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71149">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
〰️
⭕️
سنتکام مسئولیت حمله به نفتکش های ایرانی را گردن گرفت؛  پس از شلیک موشک‌های بالستیک سپاه به سمت دو ناو جنگی آمریکا، نیروهای آمریکایی ۳ نفتکش حامل نفت خام ایران را هدف قرار داده و از کار انداختند. دو نفتکش نزدیک خارک و جاسک هدف قرار گرفتند و یک نفتکش دیگر…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71149" target="_blank">📅 18:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71148">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tqweh4jnb9CAIrY7uUo-F9Uehozos0Kjt-8sB_GtugdjZQzo7mkMsVsZ8bkGmli9OUCZRSdmrPL-lFdrMptcDI3sGsP7YWanxUDu96PZBqeU3i2vLzBOCqdTNiF2FdCkjdYjAzuW3xmNy_VRGcH1i5L6v6R1TUQ9YnPUJMFNcMFFtwcrD-I5t6oIuIYuzK9uapCdl5gf2t4et4kk4K_TJOdKUN-I5VDBduXCl6TWZy8vSNjgF9vAsiH9ll0MIajDP3NPew0Qbnh8hJth7ADxqLsXFsvLSh4SphGgw3QbrkRVfdXGxpngssDzs2k4NZ5MfwHRiBhSy03TMM47gNkS4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
🇧🇭
سفارت ایالات متحده در بحرین:
با توجه به تنش‌ها در خاورمیانه، وضعیت امنیتی همچنان پیچیده است و احتمال تشدید غیرمنتظره اوضاع وجود دارد.
سفارت ایالات متحده به شهروندان آمریکایی یادآوری می‌کند که ایران پیش‌تر زیرساخت‌های غیرنظامی در بحرین، از جمله هتل‌های منامه، را هدف قرار داده است.
آمریکایی‌هایی که در حال حاضر در خاورمیانه حضور دارند، باید هوشیاری خود را افزایش دهند و نسبت به احتمال لغو پروازها، بسته شدن حریم هوایی و اختلال در سفرها آگاه باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71148" target="_blank">📅 18:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71147">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=b061eMlnXeQLvnzi-t5ElIZcxxGqk3Kf5PBrC-1OBMiMZCGMGlhreIss44a82CeSt37J-vTG4rL5Zy0-YX8oA_iT8BaiSa14qUtwgIXfMyZPGQcUGl_5y0x7sUH5kOF_zSXIyzqpr28MqoDsyyz-yuaSTxOBnC-2qukqDoZpN2LI4RDx7x6EbCbhn-vVozKBbXWgqGtfYr1K32KMrIz_w9G_Kcay_otYETdq95ttfcriTWQcqibvJehuXO-HISzQ4MvTxQHLBDA95XHScsnYrGeFW4WAZrLiT93IhxLcqeFYd7GOu6wPpSUITZ1thAyThh1qYPzeUEc4-V-G0S3Vrw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=b061eMlnXeQLvnzi-t5ElIZcxxGqk3Kf5PBrC-1OBMiMZCGMGlhreIss44a82CeSt37J-vTG4rL5Zy0-YX8oA_iT8BaiSa14qUtwgIXfMyZPGQcUGl_5y0x7sUH5kOF_zSXIyzqpr28MqoDsyyz-yuaSTxOBnC-2qukqDoZpN2LI4RDx7x6EbCbhn-vVozKBbXWgqGtfYr1K32KMrIz_w9G_Kcay_otYETdq95ttfcriTWQcqibvJehuXO-HISzQ4MvTxQHLBDA95XHScsnYrGeFW4WAZrLiT93IhxLcqeFYd7GOu6wPpSUITZ1thAyThh1qYPzeUEc4-V-G0S3Vrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
〰️
⭕️
سنتکام مسئولیت حمله به نفتکش های ایرانی را گردن گرفت؛
پس از شلیک موشک‌های بالستیک سپاه به سمت دو ناو جنگی آمریکا، نیروهای آمریکایی ۳ نفتکش حامل نفت خام ایران را هدف قرار داده و از کار انداختند.
دو نفتکش نزدیک خارک و جاسک هدف قرار گرفتند و یک نفتکش دیگر در دریای عمان منهدم شد.
سنتکام اعلام کرد این نفتکش‌ها بخشی از شبکه تأمین مالی سپاه و نیروهای نیابتی آن بوده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71147" target="_blank">📅 17:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71146">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c865776e9.mp4?token=hCt9NEU0mkC6fpZXuokxnX0ENVuo5Q5MRiCWkw2CqWY-HUSD3w4lH27hvPptsZZDzGNt-k0ghpWt79EJAg0TZD1L20B_U9HA6CfiKvKoHD0adhXT2E9RMvsUZ0EQLS-s0WZpk0KN6nJUT4fd9rE_yi3UyBE1bdBDonp5eC60zlP3Z0jK9JbZv_oma3DpFqT-5fGNbBVmTCGtr5mxFR-OwRRJ4tKeGMLVjxAqog1Xd-8LnyXUZIh4eF1lgMMhwGF1Qh2ltFbO8CRlFvj_3CKQ0IbNwuBlgWTbayBrs3jcYJHob3gOONERjkU9l5pF0iTSv2mc6wNFNBteRtAF0FHcwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c865776e9.mp4?token=hCt9NEU0mkC6fpZXuokxnX0ENVuo5Q5MRiCWkw2CqWY-HUSD3w4lH27hvPptsZZDzGNt-k0ghpWt79EJAg0TZD1L20B_U9HA6CfiKvKoHD0adhXT2E9RMvsUZ0EQLS-s0WZpk0KN6nJUT4fd9rE_yi3UyBE1bdBDonp5eC60zlP3Z0jK9JbZv_oma3DpFqT-5fGNbBVmTCGtr5mxFR-OwRRJ4tKeGMLVjxAqog1Xd-8LnyXUZIh4eF1lgMMhwGF1Qh2ltFbO8CRlFvj_3CKQ0IbNwuBlgWTbayBrs3jcYJHob3gOONERjkU9l5pF0iTSv2mc6wNFNBteRtAF0FHcwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حسن روحانی:
به مردم بگیم قرار ما اینه که با قدرت‌های بزرگ تا بیست سال دیگه بجنگیم.
اگه مردم قبول کردن عالیه بریم ادامه بدیم.
ولی اگه مردم نپذیرفتن و راه دیگه‌ای نشون دادن حق نداریم نادیده‌شون بگیریم.
حتی پیغمبر هم با مردم خودش مشورت می‌کرد.
تو این کشور هیچکی از جانب خدا حاکم نیست‌؛ همه به لطف رای مردم اومدن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71146" target="_blank">📅 17:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71145">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/100451e13a.mp4?token=VDku_7vF48VSf8GThTuK5uiF-fZ3uL-jOppBl5tpqDjbCaMn4FIfXgIIBz9Tr1IKpKKM37eaQYWRnG4mIqBToAAgQ0Ukmg0ZyylU5Eey5W-lXuOv-lfg477OkxaWHVa51Ln2Kw5usA9srpuXOJhrThM2xgwHwNLCSZjFoJrtpWExTZb_TWz45OfrL_sm1GplzBeFYEW-GcVkJ-HGLVr1lo8-77dfQgTLcx4vLf1orBEO7IGFZL_dg8iCzozqoBm4D-G8tOn_xngcNsmHEEzLcfPp5aqfQncIWqOhwkEIhZFug_ehniGVYern-6WxhLZA6ufiXX7jn-h5VBniW60gCjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/100451e13a.mp4?token=VDku_7vF48VSf8GThTuK5uiF-fZ3uL-jOppBl5tpqDjbCaMn4FIfXgIIBz9Tr1IKpKKM37eaQYWRnG4mIqBToAAgQ0Ukmg0ZyylU5Eey5W-lXuOv-lfg477OkxaWHVa51Ln2Kw5usA9srpuXOJhrThM2xgwHwNLCSZjFoJrtpWExTZb_TWz45OfrL_sm1GplzBeFYEW-GcVkJ-HGLVr1lo8-77dfQgTLcx4vLf1orBEO7IGFZL_dg8iCzozqoBm4D-G8tOn_xngcNsmHEEzLcfPp5aqfQncIWqOhwkEIhZFug_ehniGVYern-6WxhLZA6ufiXX7jn-h5VBniW60gCjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بابک زنجانی: سایپا را ۱ میلیارد دلار می‌فروختند، ۲ میلیارد پیشنهاد دادم، نفروختند
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71145" target="_blank">📅 17:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71144">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b09e3df411.mp4?token=vf1lralgmi1-0y0BIgGiwLom2qjENInM7gz6oHzQV3kZ74YQY805yGFyQOB9SdjR8do_1EHvpCjYsQ-eUXk_BE_Wo1QssH-LWwsV3wY4WkPRb6xGhg38G54qlvjces3jL3it2xsDgP4-7NzDjZudo5OMgboDGVcn9MjuUgfXOHkdSj5uJscmbYVvZDUywsHl8qIxWx7rzg5oeXG-JqBpfqrF7djh5f_jONfUPWqZ1O8sw163g_2gA6sHtLRIt3StRkUG2gGJnhrPWH_bjgUnV-yK0CbePj0tBXeUvWJtLji5zPdz4xpJ1pYJb9Ry3L5b6wANDaMmaHOsTHnKw5uckQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b09e3df411.mp4?token=vf1lralgmi1-0y0BIgGiwLom2qjENInM7gz6oHzQV3kZ74YQY805yGFyQOB9SdjR8do_1EHvpCjYsQ-eUXk_BE_Wo1QssH-LWwsV3wY4WkPRb6xGhg38G54qlvjces3jL3it2xsDgP4-7NzDjZudo5OMgboDGVcn9MjuUgfXOHkdSj5uJscmbYVvZDUywsHl8qIxWx7rzg5oeXG-JqBpfqrF7djh5f_jONfUPWqZ1O8sw163g_2gA6sHtLRIt3StRkUG2gGJnhrPWH_bjgUnV-yK0CbePj0tBXeUvWJtLji5zPdz4xpJ1pYJb9Ry3L5b6wANDaMmaHOsTHnKw5uckQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه سری ایرانیا هم انگار توی یه ایران دیگن و رفتن توی جنگلای شمال پستونک پارتی گرفتن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71144" target="_blank">📅 16:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71143">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc463ce6f9.mp4?token=Z9wNClRgjI8jL-nBbaCLvyrRgmOziYwKf8T3UPz0kI568GfRy0T0k-76_lUjhLumqAounZbhIYKe22HwKSS0ZqVlfiAQN_Dj2vLqExhBPN73ozyXZedjtzrzctTPTvqBYkODmJRajFNQb5er24DXMnmwxfn02urMrEph5_ceBEcdnhNOwFATyGEKwgV7tbr7CkZhcFakP8JUI6ntJCZRkLTeZuiOW2tmK4bzIuSrBgRzp5nNG3nH_uumYxDgsZ3rgWWb-TcToX6YoNZLLmcVCN3fGrBKpZiHqUKA3_qzlGVA-oBi0J8Z0wQSJ1JdL0ll5TVp_hz8VTiCv5LT8ljqag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc463ce6f9.mp4?token=Z9wNClRgjI8jL-nBbaCLvyrRgmOziYwKf8T3UPz0kI568GfRy0T0k-76_lUjhLumqAounZbhIYKe22HwKSS0ZqVlfiAQN_Dj2vLqExhBPN73ozyXZedjtzrzctTPTvqBYkODmJRajFNQb5er24DXMnmwxfn02urMrEph5_ceBEcdnhNOwFATyGEKwgV7tbr7CkZhcFakP8JUI6ntJCZRkLTeZuiOW2tmK4bzIuSrBgRzp5nNG3nH_uumYxDgsZ3rgWWb-TcToX6YoNZLLmcVCN3fGrBKpZiHqUKA3_qzlGVA-oBi0J8Z0wQSJ1JdL0ll5TVp_hz8VTiCv5LT8ljqag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
تو چین یه نفر بعد ورود به مغازه‌ش که به علت نشتی پر از گاز بوده، کلید برق رو میزنه و کل مغازه میترکه ولی خوشبختانه زنده میمونه و بعد از اینکه به بیرون پرت میشه کون لختی فرار میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71143" target="_blank">📅 16:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71142">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9c6b59588.mp4?token=FLdOCdWuOUQ-TVuIoIiUOuWGQPV0xzxKBod7DfS9mIjmhJXx3SBEhoNLNVobFWihgL5rvk8Sf1HtwB5_NMlgDUS1HtFM5XZRpT2cZFLG4D_73Ccy8M4qgVggKeS_XinfuF2qzboykz_sjTPk5xFSYBG_TUsdRARfD3mfOhCQ3WgH6-8kzXP8jtO3oU4zPqaOoqgPJyH0MqLjonlGd2dq8tk63fUoonGKRsOk2H-67yajx-Zjv4_n67lKIadQKlMfNLZ2C8raZxr6pBbW-ar_DIWTRWKxXGMvIXVyACKAFieMkN4NpUsNgUpKO41feo2bUPOyg3Nm7lBkPETRUUSNWzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9c6b59588.mp4?token=FLdOCdWuOUQ-TVuIoIiUOuWGQPV0xzxKBod7DfS9mIjmhJXx3SBEhoNLNVobFWihgL5rvk8Sf1HtwB5_NMlgDUS1HtFM5XZRpT2cZFLG4D_73Ccy8M4qgVggKeS_XinfuF2qzboykz_sjTPk5xFSYBG_TUsdRARfD3mfOhCQ3WgH6-8kzXP8jtO3oU4zPqaOoqgPJyH0MqLjonlGd2dq8tk63fUoonGKRsOk2H-67yajx-Zjv4_n67lKIadQKlMfNLZ2C8raZxr6pBbW-ar_DIWTRWKxXGMvIXVyACKAFieMkN4NpUsNgUpKO41feo2bUPOyg3Nm7lBkPETRUUSNWzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇺🇦
🇷🇺
یک مزدور برزیلی که در درگیری‌های روسیه و اوکراین می‌جنگید، لحظه حیرت‌انگیز عبور یک تانک از روی خود را — در حالی که میان علف‌ها پنهان شده بود — ضبط و در حساب اینستاگرامش منتشر کرد
😟
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71142" target="_blank">📅 15:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71141">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07a24e005.mp4?token=frmCpO14c4l6wodlqH-v8QOh3WyM01d1_-mIxtaMJ2L1jUmkOwJfu-kXSLsm13T0ACAT31Cz6kNu-UNo7cIqKWIYTZ7uCOfcsVx8IivoCOmvcIReQynDTE3Sv0n6zaN0Gass0b8iYUgP5JQpt_UDpdk5l4lcOt3Bg2SlZXYs6OhPoYMvKDPN_6h9RRB297wX0MZRWIZCip7GRlEXq4p1JItV9t_iRZT169gSCoEiRfZ_KTxdXUp-fpQ8D2gUkPuk7uG1D47qiKzEOe734rLcDZlUhZVbwVQv-BR7CmR0cEv07LrheYdimu9kt-W_9T5SfUC8YTvLsVbcy47pYNNUAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07a24e005.mp4?token=frmCpO14c4l6wodlqH-v8QOh3WyM01d1_-mIxtaMJ2L1jUmkOwJfu-kXSLsm13T0ACAT31Cz6kNu-UNo7cIqKWIYTZ7uCOfcsVx8IivoCOmvcIReQynDTE3Sv0n6zaN0Gass0b8iYUgP5JQpt_UDpdk5l4lcOt3Bg2SlZXYs6OhPoYMvKDPN_6h9RRB297wX0MZRWIZCip7GRlEXq4p1JItV9t_iRZT169gSCoEiRfZ_KTxdXUp-fpQ8D2gUkPuk7uG1D47qiKzEOe734rLcDZlUhZVbwVQv-BR7CmR0cEv07LrheYdimu9kt-W_9T5SfUC8YTvLsVbcy47pYNNUAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه آخوند درباره شعار«تا آخوند کفن نشود این وطن وطن نشود»
؛
همونطور که رهبرمون رو شهید کردن یه آخوند دیگه جاشو گرفت
به ترامپ و نتانیاهو و منافقین داخلی میگم این حرفمو
تا آخوند شماهارو کفن نکنه ول نخواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71141" target="_blank">📅 15:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71140">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⛔️
این قبیله ای که میبینید اسمشون موکو موکو هست
؛
این قبلیه در افریقا که مثل سرخپوست ها هستن برای اینکه زنان قبیله خودشون دعوت کنن به سبک رقص های به خصوص خودشون انجام میدن
هر زنی در قبیله شون مجذوب رقص مردی بشه میره بهش میده و اصلا اینطوری نیست که کسی حتما باید زن شخص خاصی بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71140" target="_blank">📅 14:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71137">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca83f4e683.mp4?token=kI5HNjbGtUeF_vRazf5AAoWJzMbNiZ2GYvKmD5MjBl3nMnNx-izIZ8AP-dEUUsUim-fvdC1THyH-eFzQNFzvQaVK5QMi38ZVxqQ500QBgbigTIicWHZxscX2Zf0-fS2y86oEmLZftljE6wwQ9GpRsbuPoLGI03Djn7VmwetT1Zh6158FdBvwhx9CO3H2gd2wE2AOuvWGHPKGQBOZXCIcMZW2kPOaoBI7c86NjSP1LcwUNRlHVu2cZ4AEprhtq1me6UiMu7SusfjAdlXkNkDbCyvIMM_WpLOGaaREQSq8qI7-Ml9huy0fUA7ilZp-o33ijHzWYHGkUEvMGI9bOI40ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca83f4e683.mp4?token=kI5HNjbGtUeF_vRazf5AAoWJzMbNiZ2GYvKmD5MjBl3nMnNx-izIZ8AP-dEUUsUim-fvdC1THyH-eFzQNFzvQaVK5QMi38ZVxqQ500QBgbigTIicWHZxscX2Zf0-fS2y86oEmLZftljE6wwQ9GpRsbuPoLGI03Djn7VmwetT1Zh6158FdBvwhx9CO3H2gd2wE2AOuvWGHPKGQBOZXCIcMZW2kPOaoBI7c86NjSP1LcwUNRlHVu2cZ4AEprhtq1me6UiMu7SusfjAdlXkNkDbCyvIMM_WpLOGaaREQSq8qI7-Ml9huy0fUA7ilZp-o33ijHzWYHGkUEvMGI9bOI40ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
تصاویری از تورنتو کانادا بعد از بارش باران و طوفان
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71137" target="_blank">📅 13:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71136">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fec01afbd.mp4?token=WXUYh4vDIo0n4yLLdKYEgD7isfUxgyoQAyiCnT3a7b0bmFhrYfbKKl5XCLKvuGbG1mkmUeQEkSrBns66cFmu5cZcH3XlXkK7NuDBk7TOebyMNMyJYxhlbinPyFk_muEXisfNyJmXSd8ZnLwFdga16ko73Kj1XOaT_Fpm1OUoIQi1HkzfwUmfs5bM2ctsO-2O2EdJmBLp3jctPrr1slvj70-aPOFhP92crUU2lLvxUjt02XqHmrYYj-LM4Y9GqQBVIKf0lilBirBTOjeQ4XMONvLVgTQGEOq1fVP2ukiyhmtLGfLHSA6K1UQ5hgxYRba3lfPhJuFY7Fc6hRu_ylVi-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fec01afbd.mp4?token=WXUYh4vDIo0n4yLLdKYEgD7isfUxgyoQAyiCnT3a7b0bmFhrYfbKKl5XCLKvuGbG1mkmUeQEkSrBns66cFmu5cZcH3XlXkK7NuDBk7TOebyMNMyJYxhlbinPyFk_muEXisfNyJmXSd8ZnLwFdga16ko73Kj1XOaT_Fpm1OUoIQi1HkzfwUmfs5bM2ctsO-2O2EdJmBLp3jctPrr1slvj70-aPOFhP92crUU2lLvxUjt02XqHmrYYj-LM4Y9GqQBVIKf0lilBirBTOjeQ4XMONvLVgTQGEOq1fVP2ukiyhmtLGfLHSA6K1UQ5hgxYRba3lfPhJuFY7Fc6hRu_ylVi-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پیرزن طرفدار حکومت که میگه:
نه پول میخایم نه چیزی دیگه گرونی هم تحمل میکنیم مسئله حجاب رو حل بکنید خیلی مسئله مهم تر و واجبی هستش
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71136" target="_blank">📅 13:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71135">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af49e9554.mp4?token=uFRcKeEUDbzXdLJ-_rrWY42jWz9qg-Q0xXy7SZnm9wOrldK38PP9i3JbImutCVhnCrWetTEA5Hv6TOM74HdxuJpf7vHZsKtma-CGtYj5-y9LZAqJp3IloEQraZQbyFhy0yS3t9izELLEqaUgtSSAjjzW6_RX6EzDPuJCm1-2_ME_T_g3h1ymaqkSlS6JbB_Y9F8kHQCVgON7hEbQ5iDMS7IQCdreilKfYH90i_GkOsPcAYTo3XIwaM1mPtaxSoedwzi7IIVBVgqhYxh8cNG0igfl8a_ISAYcApEp3pE338DX9pgLP587f0N24FegZ8_n3G_QT62YBKSPLt_tToPTwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af49e9554.mp4?token=uFRcKeEUDbzXdLJ-_rrWY42jWz9qg-Q0xXy7SZnm9wOrldK38PP9i3JbImutCVhnCrWetTEA5Hv6TOM74HdxuJpf7vHZsKtma-CGtYj5-y9LZAqJp3IloEQraZQbyFhy0yS3t9izELLEqaUgtSSAjjzW6_RX6EzDPuJCm1-2_ME_T_g3h1ymaqkSlS6JbB_Y9F8kHQCVgON7hEbQ5iDMS7IQCdreilKfYH90i_GkOsPcAYTo3XIwaM1mPtaxSoedwzi7IIVBVgqhYxh8cNG0igfl8a_ISAYcApEp3pE338DX9pgLP587f0N24FegZ8_n3G_QT62YBKSPLt_tToPTwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
تصاویری از نفتکش ایرانی که چند ساعت قبل هدف حمله آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71135" target="_blank">📅 12:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71131">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bb2e861ad.mp4?token=AxKgEbFAZeGzXsI_V_NRYs7V6EnkX1cnOFyZHughCIdff2O17NjkaRQhQjCy56gxtlg_CFIoYiyy2hIXdqGtCb7OG4FCOhtF2SEqoXTnUwYgGrUI3MV_TTMKmzvBaiYlmdWRWsr82_Jr3hFrqomvR-yymS0IN2n7e4V6j7NC_kLI7msuA8aSOajNXr_12IQHsUA9m9ZLq3QtrO40IsxJjum0MSwcRop8nREiAJUhDJhT06Fr9XQLGrPmn9pd1IT-slsqph1iOcYcr6XWFBym3Rocmyvj5__2THq6nQ5sj5F1cAfuoCQ2yU4C9D0JYyWxljyyzf_rGt3L65bZp9XBIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bb2e861ad.mp4?token=AxKgEbFAZeGzXsI_V_NRYs7V6EnkX1cnOFyZHughCIdff2O17NjkaRQhQjCy56gxtlg_CFIoYiyy2hIXdqGtCb7OG4FCOhtF2SEqoXTnUwYgGrUI3MV_TTMKmzvBaiYlmdWRWsr82_Jr3hFrqomvR-yymS0IN2n7e4V6j7NC_kLI7msuA8aSOajNXr_12IQHsUA9m9ZLq3QtrO40IsxJjum0MSwcRop8nREiAJUhDJhT06Fr9XQLGrPmn9pd1IT-slsqph1iOcYcr6XWFBym3Rocmyvj5__2THq6nQ5sj5F1cAfuoCQ2yU4C9D0JYyWxljyyzf_rGt3L65bZp9XBIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇱🇧
خبرنگار اعزامی صداوسیما به لبنان سقوط تپه علی الطاهر در جنوب لبنان رو تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71131" target="_blank">📅 12:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71130">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
خبرگزاری فارس:ساعتی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارگ شنیده شد  خبرنگار فارس در جزیره خارگ می‌گوید صدای انفجار از محدودهٔ خلیج فارس به گوش رسیده است اما نشانه‌ای از دود و آتش در خلیج فارس مشاهده نمی‌شود. تاکنون اطلاعات رسمی و دقیقی درباره…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71130" target="_blank">📅 11:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71128">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v5JYPre23_29dR3pC6gKAcXnFG9ReI7J9WBrbppnh8mQdLugoBEFEdgiTtg8nD-nnfS8gWK9e7a3aoUCVi5x0tQPpW4S3hxjdMbMNcRfu91QkJIkBGj_KzUGk-YgOx53b-YuinwvAlbmGaapw4Qu8jZuv9clLuY9ujCD2QuQ8uB9-IFCkZXLle9toqbluJN29I4ZZo_dSgkFVm0hAz-31omyGCEPCPdoOpcVfGGPB-Jppj296AJcb1VuBIYyS5s4wirJCXtskxAjRBofOlWcSAX3O0Mvs2qyk2wy857fdQJFfcUqV5UV6owPJ9G1mSsrzu-7O-x_sro7JR3oe4Jg_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/924e97ac3c.mp4?token=HT8QLhvnauF-Cs7st6MgqOwxiPdzTxykrSZQU0GDwBgC9oDzH7g10G06Rur3tOf17pMoyA5sgAZBBcAKo7r2WFcWxeiNq6Ze73ubDtk607YC4AAZU6kvGrMAhJhqGfa_nBjfUcsbO5m5QWVkJ4uw6w9fieKliDlqVE0FEOKZj6f9dvRidaT8Me2XH1-YHS5jfc5SMARV4WMluT9IQRcgKhLYJlo8UETcQOYvYxp5_20_rfiN6-whJVpX5DhQ9EPdr4_Yp1PyKFPD13_PuO_JfN9QyHD3GOC3VrZcAXif-ZzBiV6DgcuAOOGAe0lYLG38vsHfaxD8l7sn_M1WqzKVSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/924e97ac3c.mp4?token=HT8QLhvnauF-Cs7st6MgqOwxiPdzTxykrSZQU0GDwBgC9oDzH7g10G06Rur3tOf17pMoyA5sgAZBBcAKo7r2WFcWxeiNq6Ze73ubDtk607YC4AAZU6kvGrMAhJhqGfa_nBjfUcsbO5m5QWVkJ4uw6w9fieKliDlqVE0FEOKZj6f9dvRidaT8Me2XH1-YHS5jfc5SMARV4WMluT9IQRcgKhLYJlo8UETcQOYvYxp5_20_rfiN6-whJVpX5DhQ9EPdr4_Yp1PyKFPD13_PuO_JfN9QyHD3GOC3VrZcAXif-ZzBiV6DgcuAOOGAe0lYLG38vsHfaxD8l7sn_M1WqzKVSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه پسر بدبخت پست گذاشته که اگه این پست ۵ هزار تا لایک بخوره، صاحبکارم منو میکنه! تورو خدا لایکش نکنین.
و حالا واکنش مردم دلسوز ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71128" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71127">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
خبرگزاری فارس:ساعتی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارگ شنیده شد
خبرنگار فارس در جزیره خارگ می‌گوید صدای انفجار از محدودهٔ خلیج فارس به گوش رسیده است اما نشانه‌ای از دود و آتش در خلیج فارس مشاهده نمی‌شود.
تاکنون اطلاعات رسمی و دقیقی درباره علت و منشأ این صداها منتشر نشده و جزئیات تکمیلی متعاقباً اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71127" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71126">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71126" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71126" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71125">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDVQJvA5Nf-pweRFE8M7S8mfrILxQJYHW7zjotgUJHjkGafSy7tC-PyY3yQP5fUdHMKvuemZmCiCzexR-rPlyM1-6GRfjan8IJVwIKf6ZEaTnLAqLaXjcOrS6udm2XcZTZXyFTyq6TJ_j048hgkpivu3irWQLLqUOv-dNFQvIMkU0xa5JUUpCD6drzjTQE5b8Y0H--U2YGTz6BwBC2IW_zhpfNUM5zRPVKWsuZb_oAwn8URoG9IfB53RR1RUWMoKph-erH6OIlyny-L0QMrZuccIBGo-NKLZMwAoi75kTQufQKMA9V15M9MncbpZIKZ3n1Nj5ZURuQlUEMIR4e160w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
بورنموث
🆚
نیوکاسل
کاونتری
🆚
منچستر سیتی
تاتنهام
🆚
ناتینگهام فارست
اتلتیکو مادرید
🆚
اتلتیکو بیلبائو
ناپولی
🆚
اینتر
آتالانتا
🆚
رم
دورتموند
🆚
هوفنهایم
بایرن مونیخ
🆚
شالکه
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71125" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71124">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0380bdceab.mp4?token=NugANBYdRz-B-1pKzJwtLfW_kUYWMa_d8rUubwdPuK1BilcthrJrgA5laNMbaSZE7RtzzJTsabkLRDgAE8j14EtXKmg9drOFHBUiR63V9ht03S6c8wCd7nNEplY2uIptWQ4YF4SwRryeV4dNIl2pmH9lYZJcT_RvRLETiyGH3msxpxySbu1E3ndo_BL3thjYEBsb32m6YBdZ2m6wjaJ6L0hPHRjp_s_4kf3_k2lHeJUZ6liGXJFXScirRaG05mwDhJUW3tCV0VeEjx-3Gp2SbridX-7EadlmJ1knBoSaenUn9dHtHK44p3MCB4pds9b7Pr_7jsoLI0oDj0jOlfzYfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0380bdceab.mp4?token=NugANBYdRz-B-1pKzJwtLfW_kUYWMa_d8rUubwdPuK1BilcthrJrgA5laNMbaSZE7RtzzJTsabkLRDgAE8j14EtXKmg9drOFHBUiR63V9ht03S6c8wCd7nNEplY2uIptWQ4YF4SwRryeV4dNIl2pmH9lYZJcT_RvRLETiyGH3msxpxySbu1E3ndo_BL3thjYEBsb32m6YBdZ2m6wjaJ6L0hPHRjp_s_4kf3_k2lHeJUZ6liGXJFXScirRaG05mwDhJUW3tCV0VeEjx-3Gp2SbridX-7EadlmJ1knBoSaenUn9dHtHK44p3MCB4pds9b7Pr_7jsoLI0oDj0jOlfzYfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📚
معرفی لاکچری‌ترین مدارس ایران !
برای اینکه به علم برسی هم باید اول ثروت داشته باشی!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71124" target="_blank">📅 11:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71123">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a478b3c9a9.mp4?token=ClCInYjRbozfHaxabP2XXqhXiZzEN62EuJrCUcu6d-oIegnnB5tJ_lbBLTFLxCUrnRyx-fqg-N8i5xQOVpR2kUudVg1yBov59tfNbfeKEF1Eyeu4YQikMjZbhD0IGUhBbI-PyBSrChgRaDHG3H6lwLr1TRtI29sbmtdfbaZnbre6bZjaUAdL0zbAi-7jmZbblvVh0y3EePaGb2BaW0eTKAgFEsZrDwLidLcK445FVE5FfBmkTlfBI-cqIzYRYnQuHbuTQx3zLHz_D5_VvZb4po9Qy95YrYXOR4dhPozWoY7D7J7EuiEU_E_gX4Z3LEyzv5sgEhDRLnq6nNXYZ-3g_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a478b3c9a9.mp4?token=ClCInYjRbozfHaxabP2XXqhXiZzEN62EuJrCUcu6d-oIegnnB5tJ_lbBLTFLxCUrnRyx-fqg-N8i5xQOVpR2kUudVg1yBov59tfNbfeKEF1Eyeu4YQikMjZbhD0IGUhBbI-PyBSrChgRaDHG3H6lwLr1TRtI29sbmtdfbaZnbre6bZjaUAdL0zbAi-7jmZbblvVh0y3EePaGb2BaW0eTKAgFEsZrDwLidLcK445FVE5FfBmkTlfBI-cqIzYRYnQuHbuTQx3zLHz_D5_VvZb4po9Qy95YrYXOR4dhPozWoY7D7J7EuiEU_E_gX4Z3LEyzv5sgEhDRLnq6nNXYZ-3g_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تسلا، سفر با تاکسی‌های خودران Cybercab رو تو تگزاس آغاز کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71123" target="_blank">📅 10:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71122">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a09a3f19ee.mp4?token=Ad-CLFtqyg0KbDcdDxPfSWDm_w0StizzChFV3Z2Gm4zUs6_8IEMYr5-DL59eaxeBniSOez1hTOEzyyPzwcAs8FQdDq6HcADnhMSgXmFjm-l20rQsbaWGrgsJaBGwoB_kVV19F1n7ejETysn9GM-NFTxMiucH0pltIvGwipvgyvj-SHbTGXqr8pXRsw1Sjqmr4TLCgGtrL66t3BqKVMaFH35gsXMAjsIlSZX1Jr9HRnjTpbeO6bM3JatqJ8gdmhWQlXw-jHJrhafgEoyc6cI4Mypk4lKPqQ-jVrnUsPu8JvEspDTJN9jX2pAokP8jV8jwnytA8CQ8R1t5IVRI8BzmwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a09a3f19ee.mp4?token=Ad-CLFtqyg0KbDcdDxPfSWDm_w0StizzChFV3Z2Gm4zUs6_8IEMYr5-DL59eaxeBniSOez1hTOEzyyPzwcAs8FQdDq6HcADnhMSgXmFjm-l20rQsbaWGrgsJaBGwoB_kVV19F1n7ejETysn9GM-NFTxMiucH0pltIvGwipvgyvj-SHbTGXqr8pXRsw1Sjqmr4TLCgGtrL66t3BqKVMaFH35gsXMAjsIlSZX1Jr9HRnjTpbeO6bM3JatqJ8gdmhWQlXw-jHJrhafgEoyc6cI4Mypk4lKPqQ-jVrnUsPu8JvEspDTJN9jX2pAokP8jV8jwnytA8CQ8R1t5IVRI8BzmwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
〰️
🇹🇭
کامیون‌های سوخت‌رسان مشغول انتقال سوخت هواپیما به ناو هواپیمابری «یو‌اس‌اس آبراهام لینکلن» (CVN-72) در بندر «لائم چابانگ» تایلند هستند؛ به‌طوری که از زمان پهلو گرفتن این ناو، روزانه ورود و خروج ۲۰ تا ۳۰ دستگاه کامیون مشاهده شده است.
این سوخت برای تأمین نیازهای «بال هوایی نهم ناو» (CVW-9) در داخل ناو ذخیره می‌شود؛
یگانی شامل جنگنده‌های رادارگریز F-35C Lightning II، جنگنده‌های تهاجمی F/A-18E/F Super Hornet، جت‌های جنگ الکترونیک EA-18G Growler، هواپیماهای هشدار زودهنگام E-2D Advanced Hawkeye و بالگردهای MH-60 Seahawk.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71122" target="_blank">📅 10:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71121">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deba41468f.mp4?token=XS8a4viKXVBMLnovunVvadgwZc3eJRu4fNWvFT8udKXYpz0yetOy_vqjnQ5WinCne_Gft-rnlenihFZ-Je-V6B6gAOuPPFqE8E-3s2yDrs_8WxvJJ18uWrxTOKj6_X0MWExg3_veacURFzpUZ6dZueHnqk8QPDj1x0jSoeUXyM6JsUC_883hMhWypNbOVud7gbADjXVgQej0hBSl_prGwDjj9nYk7TVWdnR3byV3-L88xLbNqthIXfJv_MC4HaR2NXiZgrHGoH_4Mkshuku9O74iTiUy3iosyi9Efc-t4u-PWWL18gbg20JX7YjnDC3I5uk36FUBnrJWKwmhy3N58jVjcjADhF0xN6yyB-klF60SpG6CcN20s_FM12O_6oI04cznE71L777H2HIQTTPO5GaX6L1nFITlpTb_tu1noHS1nogah8V4Rek0aY-rCLSQgGsi2EYbP5R3AIJwynwlzM38_5fZP6qutP5C5pe71n1eGM5RaGy6Llke_P7pjzklkOvrEGEiA00WlosZJBcu4m_N1qlLVnjnYCUq49LWV0nuFczoGMhzE5Y0EIy1ysYzgdPLcjelrqxUs1dpf05OObVI3qnDMkzCObacEnwt_nrd28c1hBY2LaqiGXS1SasszrqWdKdVgvaQvRqT4HGbgeSwJr2H6N-aYXtgvHNo6E4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deba41468f.mp4?token=XS8a4viKXVBMLnovunVvadgwZc3eJRu4fNWvFT8udKXYpz0yetOy_vqjnQ5WinCne_Gft-rnlenihFZ-Je-V6B6gAOuPPFqE8E-3s2yDrs_8WxvJJ18uWrxTOKj6_X0MWExg3_veacURFzpUZ6dZueHnqk8QPDj1x0jSoeUXyM6JsUC_883hMhWypNbOVud7gbADjXVgQej0hBSl_prGwDjj9nYk7TVWdnR3byV3-L88xLbNqthIXfJv_MC4HaR2NXiZgrHGoH_4Mkshuku9O74iTiUy3iosyi9Efc-t4u-PWWL18gbg20JX7YjnDC3I5uk36FUBnrJWKwmhy3N58jVjcjADhF0xN6yyB-klF60SpG6CcN20s_FM12O_6oI04cznE71L777H2HIQTTPO5GaX6L1nFITlpTb_tu1noHS1nogah8V4Rek0aY-rCLSQgGsi2EYbP5R3AIJwynwlzM38_5fZP6qutP5C5pe71n1eGM5RaGy6Llke_P7pjzklkOvrEGEiA00WlosZJBcu4m_N1qlLVnjnYCUq49LWV0nuFczoGMhzE5Y0EIy1ysYzgdPLcjelrqxUs1dpf05OObVI3qnDMkzCObacEnwt_nrd28c1hBY2LaqiGXS1SasszrqWdKdVgvaQvRqT4HGbgeSwJr2H6N-aYXtgvHNo6E4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بابک زنجانی:
الان کافه‌های مردم را می‌بندید بعد شب آدم می‌فرستید که بیاید تعامل کند.
می‌خواهم فیلم و مستند درباره این موضوع تهیه کنم... آن شخص هم فکر می‌کند که با ۱۰، ۲۰ سکه زندگی‌اش را گذرانده
بیکار کردن ۸۰ نفر در منِ بابک زنجانی چه اثری دارد؟! اصلاً فردا بیایید آتشَش بزنید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71121" target="_blank">📅 09:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71120">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5G2qliGDLF4H9qIIqtCbNXt1uUQw64Hpf9s6-Z-bRTdLi5pQGuj_dKgYe37cJ9CjSo2AfAcvkvT-drNmuIwibfsInSHC0CDklaJoNNQGBBr42bRkQxrpwKJLy764F3UYphdYak0EXxxD21HhlFUeN8fPiHh4gdr1v8fGibeV_E1fDmNDybdt82ZF29RrzxAKIGiwEIkOLn493E_7ycmXAZJGEG17WITTwQl8j1n5iAiwNx5QxJYHyRA7XPdpFsbIPUhqNQ3qmfTVzV9FdwEJJsWXSL8S2aMeWOZioo3DYb2GoFl83cE82o1Y0549xgZc09-cGR5BObJAlcCmVMjYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
🇴🇲
نیویورک پست:عمان بی‌سروصدا پیشنهاد ایران برای دریافت مشترک عوارض از کشتی‌های عبوری از تنگه هرمز — حتی به‌صورت داوطلبانه — را رد کرده است.
این اقدام، ادعای هفته گذشته سپاه پاسداران مبنی بر توافق دو کشور بر سر تقسیم درآمدهای این آبراه را تضعیف می‌کند.
عمان معتقد است که دریافت عوارض از کشتی‌های عبوری ناقض قوانین بین‌المللی است و تحت فشار آمریکا و کشورهای حوزه خلیج فارس، از این طرح عقب‌نشینی کرده است.
ترامپ دو بار تهدید کرده است که در صورت موافقت عمان با دریافت عوارض، این کشور را بمباران خواهد کرد.
ایران در دوران جنگ، نهادی برای مدیریت تنگه ایجاد کرده بود و از هر نفتکش مبلغی بین ۱ تا ۲ میلیون دلار عوارض می‌گرفت؛ اما بدون همکاری عمان، هرگونه سازوکار دریافت عوارض در دوران پس از جنگ، فاقد وجاهت قانونی خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71120" target="_blank">📅 09:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71119">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71119" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71119" target="_blank">📅 01:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71118">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8dXXZ3iCStqjAlsc_i0MFNlZ_z6SgZm95I2tYIYwcKCwnFVTd2qgY3LyJ8R0gOumFvjH4Ttic0RBNskNQUBlUTc3ZIXEa6QzgDMln1zIa2llTEHgjsJ5MS4JcuLRAnc2ze1hEQxgNHIvtIVYMKGNYfWaqOHTJwz29735rT8ziPU2alQmbJwuhNEbtT-VlezOWx7KxPyRcNOkRcnGRbYy8M8iOSeFo7U3ot0NpJhHuLrTIhkd0onF5g3naku3RSZVfLuKWZvNd1-EahbWPBOm-7Iam3dyzstekWFKTX4xYcoQMIWjRnDJqDaC0KLhqO-634cZzROp7dq7Wf11fjoHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71118" target="_blank">📅 01:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71117">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59487b6d80.mp4?token=gpuSKlNv-RS3cFNYBfbHbGFP1yxzDAzwfFtM1yGREqcg4x--K3z6cASNZMWwlYPinOHgUdi45hGhae5Tk66cB4dp0kwN4EeUPLR7ILpuj8dmFqhUOdgXitBwm8CGI3r_8duQ4c6GTGVTEN7M0oSfsZitKd79JJ3E9gJ0xAtT3xqSFhy4LwOHp42JIQMHIPpSV50u131bHLENs-4ho1IeBVzOpuFSEGdHUU20TlNGdya5SxuL7nT-wFIqFyWjOwd0Tz-0gmMMfOrV055M7dF3mhmyRWjR2_CRg1qjv5leos_K5OPRC8jDbepV3o4Xeb1xUK9dZc6h7iiCLuf_aVJ-iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59487b6d80.mp4?token=gpuSKlNv-RS3cFNYBfbHbGFP1yxzDAzwfFtM1yGREqcg4x--K3z6cASNZMWwlYPinOHgUdi45hGhae5Tk66cB4dp0kwN4EeUPLR7ILpuj8dmFqhUOdgXitBwm8CGI3r_8duQ4c6GTGVTEN7M0oSfsZitKd79JJ3E9gJ0xAtT3xqSFhy4LwOHp42JIQMHIPpSV50u131bHLENs-4ho1IeBVzOpuFSEGdHUU20TlNGdya5SxuL7nT-wFIqFyWjOwd0Tz-0gmMMfOrV055M7dF3mhmyRWjR2_CRg1qjv5leos_K5OPRC8jDbepV3o4Xeb1xUK9dZc6h7iiCLuf_aVJ-iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
مردم آمریکا چه زمانی باید انتظار تعیین تکلیف (resolution) در مورد ایران را داشته باشند؟
🇺🇸
ترامپ:
انقلاب(Revolution)؟
🎙
خبرنگار:
تعیین تکلیف(Resolution).
🇺🇸
ترامپ:
تفاوت بزرگی است. فکر کردم انقلاب(Revolution) جالب‌تر بود.
⭕️
🗒️
به دلیل تلفظ نزدیک دو کلمه راه حل/تعیین‌وتکلیف(Resolution) و انقلاب(Revolution) ممکنه ترامپ اینجا به عمد کلمه انقلاب رو انتخاب کرده باشه!
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71117" target="_blank">📅 01:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71116">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ef0c44cf.mp4?token=OZ03SWc--xiGVhgEopuUEUXOUXfZko9fnAyDtBCOF1NnXqiJU1EEOSRskMrAq0GsFXoTsM_4goTnd4RsHpHpOYcy75XXX0wuiEdqaq2iWEE2Uq3veMSb8hHfNxyQeSx96Jqgbv6TfIGTXucyJWUTqkx1s6Lc68kwyF4Qj7Lbt90im7Ma9l_57MeZ4pV37-kzTvDgVflC1gRAmdbUIHR0ZcGE76Tyxl7U2IWEAbbuNRdtF1d5rwjKsj2OmI0HTnoap10LNGrJ6geYV0SFizMeuh_O12gF3YquKJtlmC_8n9sCm5CdrmfhYuxxpQTVnfJ_msMMqKajRSzzzvKSTrMZtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ef0c44cf.mp4?token=OZ03SWc--xiGVhgEopuUEUXOUXfZko9fnAyDtBCOF1NnXqiJU1EEOSRskMrAq0GsFXoTsM_4goTnd4RsHpHpOYcy75XXX0wuiEdqaq2iWEE2Uq3veMSb8hHfNxyQeSx96Jqgbv6TfIGTXucyJWUTqkx1s6Lc68kwyF4Qj7Lbt90im7Ma9l_57MeZ4pV37-kzTvDgVflC1gRAmdbUIHR0ZcGE76Tyxl7U2IWEAbbuNRdtF1d5rwjKsj2OmI0HTnoap10LNGrJ6geYV0SFizMeuh_O12gF3YquKJtlmC_8n9sCm5CdrmfhYuxxpQTVnfJ_msMMqKajRSzzzvKSTrMZtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو ایتا و روبیکا از یچیزی رونمایی کردن که حتی خودشون هم نمیدونن چیه
😳
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71116" target="_blank">📅 23:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71115">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1e4d7b78.mp4?token=fyTlaNtgX1uv8GLskIPa_h5OUASlW9rwifilogyEuaKLATsIsoL98Y1r8Z2nFP_IkeTWKUaXF9GFhiK6-nxXlD9Ux_79YFqnVU2vS90JZECl2riAs8fCKzu7T9kkS89y9l4WbcPt8l9EqBHZstBpBftFe6Wg2y93TeNaUIzq8EE-ZBbiskTRLhR-xNeDHJVt7z0u9FuyphGCbP5SAZJnrJWYFOA4vwX_HpksMfKwhfd1ewT5aa0VXZKrv5l1TevPvwpn3VNFgFwzpTtQn0ll_lbduS8T83BwxpLB4e2Fgo7UvmeBKxDpDTVDELMoRf9wlucvdF07Ozr9YKUTUfH3ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1e4d7b78.mp4?token=fyTlaNtgX1uv8GLskIPa_h5OUASlW9rwifilogyEuaKLATsIsoL98Y1r8Z2nFP_IkeTWKUaXF9GFhiK6-nxXlD9Ux_79YFqnVU2vS90JZECl2riAs8fCKzu7T9kkS89y9l4WbcPt8l9EqBHZstBpBftFe6Wg2y93TeNaUIzq8EE-ZBbiskTRLhR-xNeDHJVt7z0u9FuyphGCbP5SAZJnrJWYFOA4vwX_HpksMfKwhfd1ewT5aa0VXZKrv5l1TevPvwpn3VNFgFwzpTtQn0ll_lbduS8T83BwxpLB4e2Fgo7UvmeBKxDpDTVDELMoRf9wlucvdF07Ozr9YKUTUfH3ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
طرف اندازه یه گاری پول جمع کرده و الان آورده تبدیل به دلارش کنه، کل این همه پول نقد شد فقط ۳۰۰ دلار
!
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71115" target="_blank">📅 22:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71114">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/05f93dafa7.mp4?token=vUE19tw6g2qJINJ8sjphkb2lX6pQzpL1XhFPBTu0ljJvVHxtH4pwXHxJizE88oID8fPwuki-R_e_cIl75pHK_ttKJONf60cbFhes1tan5fmuiq1CsAyZtmgPmFI6_2BjAD0xF6DUSgKuNnV3UbO5p10za14yZiJ15pWUBS0eV-YcQbQXX5ZIqwK-JoDRZeytFO4sMIS863KEq9AjXsibT2Kt059lZUBQsy1wgltnsIBk8aSBnwondG-HXcMKx-u8gPy4BLyFDrzqzAZF8r4PN6Vy46mb1gymWSoYRY-gsjePU3UbkJBDpr1_Kr1_qInGtVYNJCSgkVt5zMEjwBWlDXgaZ14Ee4dxlAxjshhbzxNu79cVms1w9m3Cl72i5XgfBT5M-Nz_4KQKhzRhBukZiuPEtffUDcpl1iY6-UFLa-yEtoItwUJK-wxpW3DCVE-cQoATkUx-15tTo6ciHY80nbs2SogSMryoOBX5WOtBW0L3RAdoyzSYrO87xZNwy-NDGovpnS4TnuWrLsyV58HIPHiGFa0rHQ_rio-Axdo375avqrBaoxy2Oc_M87V0tIjpDx-ftcS9F1n82OVdlbHfsV2x_C4j9Jz71zK2k8dwVmKIAyZNJTxqU-Imo0bPOARu7OK2AuqdRLsV-J92EB8gtt9dGe8zBBL_MKsPxGEEzr0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/05f93dafa7.mp4?token=vUE19tw6g2qJINJ8sjphkb2lX6pQzpL1XhFPBTu0ljJvVHxtH4pwXHxJizE88oID8fPwuki-R_e_cIl75pHK_ttKJONf60cbFhes1tan5fmuiq1CsAyZtmgPmFI6_2BjAD0xF6DUSgKuNnV3UbO5p10za14yZiJ15pWUBS0eV-YcQbQXX5ZIqwK-JoDRZeytFO4sMIS863KEq9AjXsibT2Kt059lZUBQsy1wgltnsIBk8aSBnwondG-HXcMKx-u8gPy4BLyFDrzqzAZF8r4PN6Vy46mb1gymWSoYRY-gsjePU3UbkJBDpr1_Kr1_qInGtVYNJCSgkVt5zMEjwBWlDXgaZ14Ee4dxlAxjshhbzxNu79cVms1w9m3Cl72i5XgfBT5M-Nz_4KQKhzRhBukZiuPEtffUDcpl1iY6-UFLa-yEtoItwUJK-wxpW3DCVE-cQoATkUx-15tTo6ciHY80nbs2SogSMryoOBX5WOtBW0L3RAdoyzSYrO87xZNwy-NDGovpnS4TnuWrLsyV58HIPHiGFa0rHQ_rio-Axdo375avqrBaoxy2Oc_M87V0tIjpDx-ftcS9F1n82OVdlbHfsV2x_C4j9Jz71zK2k8dwVmKIAyZNJTxqU-Imo0bPOARu7OK2AuqdRLsV-J92EB8gtt9dGe8zBBL_MKsPxGEEzr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
یه بلاگر ایرانی رفته چین و ربات انسان نمای چینی رو به مبارزه طلبیده؛
حرکات ربات به قدری تمیزه که انسان واقعا از آینده جهان خایه میکنه!
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/71114" target="_blank">📅 22:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71113">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66a864cef.mp4?token=vWzePaOwVlX9H9_D7mbZEES60qdroC97oR7_wgqATHZ_re-EpwdAMco40K1L-tIi6X8tHAVJ1g4MB0MX8wtWbHy8lLKl8jM_L8z44OldtbgHKYCKqAdWJ0dvXTPnVoGtOVgiOGDMCS3OHlgioCW26ObDyD_hsFDN9c4ACK3YP2cXVTHHuU4vaQxKiHp7n-77VFgiQCmov_yX6OlnG11RJwxFY0ODY7ex6UhHVeyvoyFFbZgqXw25PdzuAy_oVIQaxXfANB2jbIPIDy0K2TFaNdOkyGbdDbdhZ0st6Cw_5GUZ5AYtoU7OnsIQo1B49075o-KTfZOSW9FisMXBUESkLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66a864cef.mp4?token=vWzePaOwVlX9H9_D7mbZEES60qdroC97oR7_wgqATHZ_re-EpwdAMco40K1L-tIi6X8tHAVJ1g4MB0MX8wtWbHy8lLKl8jM_L8z44OldtbgHKYCKqAdWJ0dvXTPnVoGtOVgiOGDMCS3OHlgioCW26ObDyD_hsFDN9c4ACK3YP2cXVTHHuU4vaQxKiHp7n-77VFgiQCmov_yX6OlnG11RJwxFY0ODY7ex6UhHVeyvoyFFbZgqXw25PdzuAy_oVIQaxXfANB2jbIPIDy0K2TFaNdOkyGbdDbdhZ0st6Cw_5GUZ5AYtoU7OnsIQo1B49075o-KTfZOSW9FisMXBUESkLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخیرا بعضی دخترا طی یه حرکت فوق‌العاده و زیبا، دارن هرچی ژل و بوتاکس تو صورتشون بوده رو خارج میکنن تا نچرال به نظر بیان
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71113" target="_blank">📅 21:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71112">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XixgZy09QVGHQHC8Un6g7MDHFKhr871xkah7ss13Zs2Jyi9af-6VDPwNNqNfgdQcvKCU_h8ZC-isHB1yf2TeL3wMMRlFyDj1TmmpElZapspgpheHgkkF6Cu_SIX319BW0Pnv3gFY6-XZsg4AnoXKtk3MGUUgzP4Bq-jE9yXbnovtYIa87rSnsFvGy5ZNDLh-cqWa6p1nzgjW9ophDRJJ0Z4fSj-D8HWasNUaWvW5Gaoplj8cBAZy_vZBjmzRkAp9_HoGTy7mJ7SmdK-DNWDS2UHOW3VtryuOGitNExzroqnhmhAeSCrjoAPaafxmgXjtV90_2Nu_1GaJORB4EokGQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👎
قرارگاه خاتم الانبیا: حملات پیش دستانه علیه پایگاه آمریکا در اردن که در حال آماده سازی برای حملاتی علیه کشور بودند را انجام دادیم!
❌
خبر بالا که بطور گسترده در حال انتشار در رسانه هاست فیک و نادرسته، همونطور که می‌بینید سپاه پاسداران و قرارگاه خاتم‌الانبیا هیچ اطلاعیه‌ای مبنی بر حملات پیش‌دستانه منتشر نکرده
@HutNewsPlus</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71112" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71111">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNB5jYWsRzTXb5CRBX96Su1vvlt1oCUGh9U3shEvextoDKPPdUbVV47RLeyApNPNk4cc-JHQVCnLTbl3kYbJtF248eEAYB17ZT-27PKQRR5PcmKZ6KJ7UuLvIU4Jep9dCd_6cHLlGUN792wFM0CO4LFtY5wfy5Qi0n58PoGrceW2S0S2VTnz1Ede9rOClIjXVnf9XbA_WjLNF3RB7PdSyZdb85hM3UTDRrttwyWJiZtPyAMsjju8VR0cZ4vjYAFa69Wdd4-99Hgmyw3R6gG2ZCQnGBnnu9khH5ySvnwPh0EFXLaOE6eYbKnj1t_uQzqAnPwfaThlQHtS9JtScRFoDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام ارشد آمریکایی به کانال 12: در حال حاضر هیچ اطلاعی از وقوع آتش‌سوزی در پایگاه‌های آمریکا در اردن وجود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71111" target="_blank">📅 21:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71110">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c74f1d2d4f.mp4?token=H_lLoWMaC3ZTN0ZCPNIUvgrpV-VPIpAcHmfUBJScfciBTg7UBDqi6pBWFCzbGzdQj8OLo6XCU1s6uZW8gP4uBLzvIL-KKp2yddmdXoPPlFG-1YdLDlIgVQ9VDFhx3mOUqV3npnECWyF3fVDsRZ3nexfU4CxDxoN5UXuwoCzR4RjSGclmIx9Ec4A2LBcZ4J9us-3VgxDQJbp7owwnKl_RZga4zvheVx7WYsIzI7Nfxwl8_VQqhab739-7BDVh3rmFkRFVeGMSxv-kpZTAfwQtVQ-1rm-Ja6REBEJmTbXbmnpDwgFUGY7pSdgoXwX3nmyrd0IMM0L83Ci5FQ1fmuaq3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c74f1d2d4f.mp4?token=H_lLoWMaC3ZTN0ZCPNIUvgrpV-VPIpAcHmfUBJScfciBTg7UBDqi6pBWFCzbGzdQj8OLo6XCU1s6uZW8gP4uBLzvIL-KKp2yddmdXoPPlFG-1YdLDlIgVQ9VDFhx3mOUqV3npnECWyF3fVDsRZ3nexfU4CxDxoN5UXuwoCzR4RjSGclmIx9Ec4A2LBcZ4J9us-3VgxDQJbp7owwnKl_RZga4zvheVx7WYsIzI7Nfxwl8_VQqhab739-7BDVh3rmFkRFVeGMSxv-kpZTAfwQtVQ-1rm-Ja6REBEJmTbXbmnpDwgFUGY7pSdgoXwX3nmyrd0IMM0L83Ci5FQ1fmuaq3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک ها از ایران به سمت اردن
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71110" target="_blank">📅 20:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71109">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
منابع عربی:چندین انفجار در اردن رخ داد
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71109" target="_blank">📅 20:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71108">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbf8f1e1a9.mp4?token=nGiVL6hAzqBL8EEaPni5hvg85hm7Ya3n8JTT3Ln0Zx7Xmwqf8O0SkgG1aoZNhsuxUEsOGwP6ixK0Y_b5Nl_vLS4DEU75QZQRW2PY2LbYjsoRUCYYZxPOcwwjf4uyYp6X53n_NQpDvplQn3h_93OLmKe08yj22l8NHk-7wYeUU_CTSzd7vGoMYZLNsDDCHGOm_ShZMQKzSuaR9W5LLCZCwvYoA5cCzXJ54R98HJ0ydmoPZBNW5BYDOdU1N94nD_wcCaz13PyC68d-zxG7GZD69_-UDvQyaXBZbr-GcXfPRI_gPprBCe5xId2FRljuS8mfyjYRuqBtsmIRpEWjNB1G4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbf8f1e1a9.mp4?token=nGiVL6hAzqBL8EEaPni5hvg85hm7Ya3n8JTT3Ln0Zx7Xmwqf8O0SkgG1aoZNhsuxUEsOGwP6ixK0Y_b5Nl_vLS4DEU75QZQRW2PY2LbYjsoRUCYYZxPOcwwjf4uyYp6X53n_NQpDvplQn3h_93OLmKe08yj22l8NHk-7wYeUU_CTSzd7vGoMYZLNsDDCHGOm_ShZMQKzSuaR9W5LLCZCwvYoA5cCzXJ54R98HJ0ydmoPZBNW5BYDOdU1N94nD_wcCaz13PyC68d-zxG7GZD69_-UDvQyaXBZbr-GcXfPRI_gPprBCe5xId2FRljuS8mfyjYRuqBtsmIRpEWjNB1G4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇨🇳
بِسِنت درباره ایران:
آن‌ها محموله‌های نفت را به سمت چین روانه کردند. منتظر اقدامات مربوط به این موضوع در روز سه‌شنبه باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71108" target="_blank">📅 20:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71105">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64aa07a7bb.mp4?token=hyG-BOZWeRWlWe-rZY58uJtRbSjRMxzBT8IcIwe4z8j266e9bRYLwZmGck2CIT0UvX4wm_XnzhOvyIW6D_5d0kaMFASQYaxPnbrZqOG39BfdPDP59IKm_DcdjKBY4W0PwbNBmynYXOve44-1ZGmpoL38-gVslJhMBpzUx0Y8vP0kb6xcbSRxN0GqHJn5Xdd93wQh02X2PWr0iItYAjgoKI5qeSe9VW3Hd_93GJ0f3MDVJDM4V7nA7zW2M4xT68lXhOjyqjpL6uOWCbuhBldGeiKlHZHLJWK3T7LQzRLIP5Nl3jjFDp0Slx-i6SnU-cJ6wjz35lUyGpHofgoU08THbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64aa07a7bb.mp4?token=hyG-BOZWeRWlWe-rZY58uJtRbSjRMxzBT8IcIwe4z8j266e9bRYLwZmGck2CIT0UvX4wm_XnzhOvyIW6D_5d0kaMFASQYaxPnbrZqOG39BfdPDP59IKm_DcdjKBY4W0PwbNBmynYXOve44-1ZGmpoL38-gVslJhMBpzUx0Y8vP0kb6xcbSRxN0GqHJn5Xdd93wQh02X2PWr0iItYAjgoKI5qeSe9VW3Hd_93GJ0f3MDVJDM4V7nA7zW2M4xT68lXhOjyqjpL6uOWCbuhBldGeiKlHZHLJWK3T7LQzRLIP5Nl3jjFDp0Slx-i6SnU-cJ6wjz35lUyGpHofgoU08THbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بابک زنجانی: دلار رو بدید دست من تا یک سال رو همین قیمت نگهش میدارم وگرنه با همین فرمون کشور تا یک سال دیگه نابود میشه.
من رو ۷ سال بدون بدهی انداختن زندان و همشم تو انفرادی بودم. همه اموالمم ازم گرفتن. وقتی آزاد شدم حتی ۱ دلار نداشتم.
با چند تا تلفن ۱ میلیارد دلار پول جور کردم و چندتا شرکت تاسیس کردم.
من میخواستم سایپا رو به قیمت ۲ میلیارد دلار بخرم که نشد ولی خودم میخوام کارخونه تولید خودرو تاسیس کنم
من توی خارج کشور بانک داشتم پولای وزارت نفت تو اون حساب بود. اونا تحریم شدن پولاشون اونجا گیر کرد گفتن تقصیر توعه و حکم اعـدام بهم دادن
تمام بانکای ایران بیان جلوی من بشینن ببینیم من بیشتر میتونم سرمایه جذب کنم یا اونا. فقط با چندتا تلفن. تا معلوم بشه کی اعتبار داره
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71105" target="_blank">📅 19:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71104">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf31ca2a30.mp4?token=rCVDjVGuOjqvDXvpvIE2PeNgMMMARD6howk4AuBbHqT3N_HOGQC4JmQ1y-yZAD-Ee9ru8RcXR_4pEl7eccOF3ffArrG2RhFJnZFluZmpSLYP4Jpk6voiXjZ95aUZEK9mMHgKnlQsUtTiU5Be-HYqtb5mUiWfzaFkH2415NC0ZuF9HlpXwWMw1FfWbQhDk9tsDrOEj1kqXmi040TJoulPjTBBK3e5pXMup9O7zyfJFftsyRDAu2lC4_NAReYshgXkKH6CX2_WqzQtvY18Jl-lgxQngoENep9KhLTfa6Puv0xSLKPQI9rxLGrhuIGdPvNPK81KiTSK0_FW2bMpCh1OXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf31ca2a30.mp4?token=rCVDjVGuOjqvDXvpvIE2PeNgMMMARD6howk4AuBbHqT3N_HOGQC4JmQ1y-yZAD-Ee9ru8RcXR_4pEl7eccOF3ffArrG2RhFJnZFluZmpSLYP4Jpk6voiXjZ95aUZEK9mMHgKnlQsUtTiU5Be-HYqtb5mUiWfzaFkH2415NC0ZuF9HlpXwWMw1FfWbQhDk9tsDrOEj1kqXmi040TJoulPjTBBK3e5pXMup9O7zyfJFftsyRDAu2lC4_NAReYshgXkKH6CX2_WqzQtvY18Jl-lgxQngoENep9KhLTfa6Puv0xSLKPQI9rxLGrhuIGdPvNPK81KiTSK0_FW2bMpCh1OXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
بسنت درباره ایران:
متحدان ما در امارات متحده عربی در خصوص این بانک مستقر در دبی همکاری بسیار مؤثری داشتند. اکنون ما برای متوقف کردن تمامی این جریان‌های مالی غیرقانونی، با آن‌ها وارد همکاری شده‌ایم.
ما برای رفع این مشکل با آن‌ها همکاری خواهیم کرد، چرا که بانک‌های متعددی در سیستم مالی آن‌ها فعالیت می‌کنند.
ما نمی‌خواهیم این بانک‌ها را نابود کنیم — هرچند اگر لازم باشد چنین خواهیم کرد — اما اکنون همه کشورها در این مسیر با ما همراه شده‌اند.
این پایان کار برای این رژیم است؛ آن‌ها یا باید [رفتار خود را] عادی‌سازی کنند و یا با عواقب آن روبرو شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71104" target="_blank">📅 18:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71103">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e7eb93ff.mp4?token=EYNkVcC_rOhfBibpVqOGGql92wJyWYOQbgaajHRaRzRib9e3jLDocODvp1jIQLcCaEJ8zbvLSc04tWikgMGtrRpTnfokPiKr8b_GvpI6S3N_VyXUTXbJgU8sqRJsFvo5-7YSCN_xcFm6Ma2MRvH8lU9TiCYs_Lk-X5zdQVNmCTLC5DC_lzlTyE5_98QPWZmYrMvTPR8zpbZmAS3wXk3B2eOUU0cMf7bTQAsMkNOBr1sj0k0D5bH975Hz3w4r0Ae6ujkuPoXz1wNSGgNQJjGWfpwT0VFs-KdMVZAQdTYB6f_ebkKmF6Lfas6YbwZFZqo2k6jgInUU7r-gCZ_3sY_BXz3zqTCABwVdhcMh-UowZUymlAIjjdUEo0EKFpSqQj8d_k3TxpkIsoiuEzZVqCt_Z2cX0M_YLqT3TSZVBSv8VbYt6n6joWrfiMAFyZ-ZQ0OP7q0vpfWSWEMGhupK8bUc58KeVMezFBEsRbG4eQS_6Jj0A7wIptqva6-WoD6Kwnl8dMxRVOm_hNDS0WXf1NALMYeyGZO93yOK-thXXT2d8wm2LEwRhXocaz8YNpF6vvEHeTdywl1MKJAqy0xYx-9Qt3zXCw65FlUAOJq7soBPImiwV2VTDIA4Rt_Jw6mQE3SxyFHxJ5qRvjP-ff6nhAxOkm981HdoRi-gfa6KsoWiM_I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e7eb93ff.mp4?token=EYNkVcC_rOhfBibpVqOGGql92wJyWYOQbgaajHRaRzRib9e3jLDocODvp1jIQLcCaEJ8zbvLSc04tWikgMGtrRpTnfokPiKr8b_GvpI6S3N_VyXUTXbJgU8sqRJsFvo5-7YSCN_xcFm6Ma2MRvH8lU9TiCYs_Lk-X5zdQVNmCTLC5DC_lzlTyE5_98QPWZmYrMvTPR8zpbZmAS3wXk3B2eOUU0cMf7bTQAsMkNOBr1sj0k0D5bH975Hz3w4r0Ae6ujkuPoXz1wNSGgNQJjGWfpwT0VFs-KdMVZAQdTYB6f_ebkKmF6Lfas6YbwZFZqo2k6jgInUU7r-gCZ_3sY_BXz3zqTCABwVdhcMh-UowZUymlAIjjdUEo0EKFpSqQj8d_k3TxpkIsoiuEzZVqCt_Z2cX0M_YLqT3TSZVBSv8VbYt6n6joWrfiMAFyZ-ZQ0OP7q0vpfWSWEMGhupK8bUc58KeVMezFBEsRbG4eQS_6Jj0A7wIptqva6-WoD6Kwnl8dMxRVOm_hNDS0WXf1NALMYeyGZO93yOK-thXXT2d8wm2LEwRhXocaz8YNpF6vvEHeTdywl1MKJAqy0xYx-9Qt3zXCw65FlUAOJq7soBPImiwV2VTDIA4Rt_Jw6mQE3SxyFHxJ5qRvjP-ff6nhAxOkm981HdoRi-gfa6KsoWiM_I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
همه خواهان پایان یافتن این وضعیت هستند. ۴۷ سال از عمر این رژیم شرور می‌گذرد و دنیا دیگر از دست آن‌ها به ستوه آمده است.
مردم ایران مردمی عالی هستند؛ اما رژیمی سرکوبگر بر آن‌ها حاکم است.
یا رژیم از درون تغییر خواهد کرد، یا مردم قیام خواهند کرد، و یا باید دید چه پیش می‌آید.
ما آن‌ها را از نظر اقتصادی خفه خواهیم کرد. آن‌ها در وضعیتی قرار دارند که من آن را «آرواره‌های مرگ اقتصادی» می‌نامم.
ارزش پول ملی‌شان در حال فروپاشی است و صادرات نفت آن‌ها به صفر رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71103" target="_blank">📅 18:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71102">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13cf8fb01d.mp4?token=kklM7ognDkSx1vDvmGrNgZQ7GX5BlTE30kgphwhurk8W6grE2t1NM4-bFCX5-IgdycnOwcRflAooKzhJl-Zej3lGOOmhVGzK_eEwdgd98PYsLF9LcCWR8K7r0ZcoXPRLZz-JnsuzrTSe7atF47vTWJxN0TpVOo8Kw-5naqWdVgUgmjFO7Vp-DkKXaThVTygHNMq4-iqwFZ7xIQzEISZRUYm6fSUKYqtz_kBHSQ1U08AxBuNOVHzpADih47-1qhC6Yz6oSoloQfNf2GNSl9_kFp-N9_qDzOfFwV6MpWult24hqjJ-jGidg5TAMcV4ZLXMqFQ-mYZAV2L4FZV1eEyQwzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13cf8fb01d.mp4?token=kklM7ognDkSx1vDvmGrNgZQ7GX5BlTE30kgphwhurk8W6grE2t1NM4-bFCX5-IgdycnOwcRflAooKzhJl-Zej3lGOOmhVGzK_eEwdgd98PYsLF9LcCWR8K7r0ZcoXPRLZz-JnsuzrTSe7atF47vTWJxN0TpVOo8Kw-5naqWdVgUgmjFO7Vp-DkKXaThVTygHNMq4-iqwFZ7xIQzEISZRUYm6fSUKYqtz_kBHSQ1U08AxBuNOVHzpADih47-1qhC6Yz6oSoloQfNf2GNSl9_kFp-N9_qDzOfFwV6MpWult24hqjJ-jGidg5TAMcV4ZLXMqFQ-mYZAV2L4FZV1eEyQwzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
ما بانک دیگری را که با ایران مرتبط است، تحریم کردیم. هفته گذشته، یک بانک مصری را که پنج شعبه در دبی داشت و ۱.۸ میلیارد دلار در اختیار این رژیم قرار داده بود، تحریم کردیم.
امروز بانک دیگری را تحریم خواهیم کرد و احتمالاً هفته آینده نیز بانک دیگری را تحریم می‌کنیم.
ما به سیستم مالی می‌گوییم:
ای عوامل مخرب، ما می‌دانیم شما چه کسانی هستید. خودتان هم می‌دانید چه کسانی هستید. کارتان تمام است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71102" target="_blank">📅 18:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71101">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
⭕️
🇹🇷
🇮🇷
وزارت خزانه‌داری آمریکا سه نهاد مستقر در ترکیه را به‌دلیل ارتباطات مالی و فعالیت‌های مرتبط با ایران تحریم کرده است:  Golden Global Portföy Yönetimi Golden Global Varlık Kiralama Golden Global Yatırım Bankası
⏺
هم‌زمان یک مجوز عمومی برای دوره جمع‌کردن…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71101" target="_blank">📅 18:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71100">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
⭕️
🇹🇷
🇮🇷
وزارت خزانه‌داری آمریکا سه نهاد مستقر در ترکیه را به‌دلیل ارتباطات مالی و فعالیت‌های مرتبط با ایران تحریم کرده است:
Golden Global Portföy Yönetimi
Golden Global Varlık Kiralama
Golden Global Yatırım Bankası
⏺
هم‌زمان یک مجوز عمومی برای دوره جمع‌کردن معاملات (wind-down) با این نهادها صادر شده است
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71100" target="_blank">📅 18:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71099">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372294672d.mp4?token=M0CqqYir2-yhzvYjWdnwRUsO5K2YYkMob0WduBsGnftrO4QQMlBlvjB6772wFednoxOYHRX0u32HqoOpsv3jB0V2H4IiRfzZgpG1Co5KGgp6wOYlsMuQyuil998a_YNrFk2pGleLyDoeFvCOkGF4yoy4YYL7lhJe7LpYYnJ5i47ZX-vgaYSF9L7M0C8ynblFpnxwOENnSUCZlTQ2EJaf72zWukQDwMxevdxrLUm_ezMeQ5ZV-aZtVomeyOe70r5swAurCV297WJFjloNjKYsj_0utsfPyts-HcFYMxQsR2LJrA_BIdpn6ncP2pyOJAbIYSzr9MBIyravB7HVLfEEYGgcYSihT-yW9dtG8PbM8epSNIPYaSX5m7P03JM16KzMqCxDX_oKyDn9FKWCLbvtNe_d6ajo219xGdBnUsFfGCh4Em5AaokrJXuF83-QwBYqXvF_utL5HL0Mv3qBa8RjuqJ4DBVDMcacZJ1xRCPznqgXHbYHWMUqxpossOKljwk3uZQCLruP51mqydK-_W_IS70SV47kR94nTE8cXppf29LfIMLxMWNlaSyCdLjTTatWMbkwDI40yb_d1gma-cDZW5aIVe7zvtu-a5b_KOnckKhAvlhxxJQW2UxtL_hzY7cAKD9gFgBeN1bJpJg99tbJbKg1-bV7W8ExbbuDLFX2YK0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372294672d.mp4?token=M0CqqYir2-yhzvYjWdnwRUsO5K2YYkMob0WduBsGnftrO4QQMlBlvjB6772wFednoxOYHRX0u32HqoOpsv3jB0V2H4IiRfzZgpG1Co5KGgp6wOYlsMuQyuil998a_YNrFk2pGleLyDoeFvCOkGF4yoy4YYL7lhJe7LpYYnJ5i47ZX-vgaYSF9L7M0C8ynblFpnxwOENnSUCZlTQ2EJaf72zWukQDwMxevdxrLUm_ezMeQ5ZV-aZtVomeyOe70r5swAurCV297WJFjloNjKYsj_0utsfPyts-HcFYMxQsR2LJrA_BIdpn6ncP2pyOJAbIYSzr9MBIyravB7HVLfEEYGgcYSihT-yW9dtG8PbM8epSNIPYaSX5m7P03JM16KzMqCxDX_oKyDn9FKWCLbvtNe_d6ajo219xGdBnUsFfGCh4Em5AaokrJXuF83-QwBYqXvF_utL5HL0Mv3qBa8RjuqJ4DBVDMcacZJ1xRCPznqgXHbYHWMUqxpossOKljwk3uZQCLruP51mqydK-_W_IS70SV47kR94nTE8cXppf29LfIMLxMWNlaSyCdLjTTatWMbkwDI40yb_d1gma-cDZW5aIVe7zvtu-a5b_KOnckKhAvlhxxJQW2UxtL_hzY7cAKD9gFgBeN1bJpJg99tbJbKg1-bV7W8ExbbuDLFX2YK0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تیزر دوم فصل اول سریال هری پاتر که از کریسمس 2027 قراره پخش بشه
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71099" target="_blank">📅 18:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71098">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71098" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71098" target="_blank">📅 18:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71097">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bnp9TY0pUoLwQUe7ATuY_ZluL2HAb_4P1Tp3fhEyzI5yQbWw7wZUksASiAvnL80qsFEQcPNwZz95gcHT_cZ4AJt0RMs_9usFyFGUIpJb5ptIrfMIjQR6JbeKfaDHKROmJxP3Jf32af6J41fr7v2TKsVA_qlJmSZJCVUCMjRDFhaL3m5bx82mxRYPIszOmlC1gMN2apPF4fRvkTylLTmiBSAcHF4mLSh5BZ9Zq2LcEbFtrobtZO-6aJMp3qQZ4YgFJ0Dounk-9nJFMl_z3cYzFatI9ga5HFuSevrxgPu7WwHr0tl7EuZWyehzIfamjl6V6BdXrKmuPrMPsXiHcGeK1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
پاری‌سن‌ژرمن
🆚
موناکو
⚽️
را در سایت بین‌المللی
TrexBet
پیش بینی کنید.
📊
مونامو ۲ برد | ۱ تساوی | ۲ شکست | ۹ گل زده
پاریس ۲ برد | ۱ تساوی | ۲ شکست | ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71097" target="_blank">📅 18:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71096">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">〰️
سنت‌کام:
بیش از ۲۶۰۰ تفنگدار دریایی و سرباز نیروی دریایی آمریکا، بر روی ناو جنگی USS Boxer (LHD 4) مستقر هستند و این ناو جنگی در حال حاضر در خاورمیانه در حال انجام ماموریت است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71096" target="_blank">📅 17:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71095">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcc841fe5.mp4?token=CSJ7a6NQ5jh3WkXy7N0-C7D138qiR5fFirAR-mY80x3ve0maRkrvDzXs63kqGNRgri_DOBLDSlFqKGoWYMpDD4jZY27feCTE4mLnzChHIQItShrk5ynbR0dz588DZcQh2hVHJ-5chMe-69HWguxN7nrt6wjZdWnrUwsfbv4tffYoLiZbs2ToR23tVDKrIjvJkCwm76IKg3b1egaGiztJ6odjiDffiinUieA4MA3UxlP7HA0yijkMROD3c7sBN4YinwTITRSK2JZcyQKKk9ysHWB-Wu1OxpnwZCLEroD4sIuwHY-l_fpSUE5eJXuNEmQTvD_oG_B-ucUR3GCJyhU0Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcc841fe5.mp4?token=CSJ7a6NQ5jh3WkXy7N0-C7D138qiR5fFirAR-mY80x3ve0maRkrvDzXs63kqGNRgri_DOBLDSlFqKGoWYMpDD4jZY27feCTE4mLnzChHIQItShrk5ynbR0dz588DZcQh2hVHJ-5chMe-69HWguxN7nrt6wjZdWnrUwsfbv4tffYoLiZbs2ToR23tVDKrIjvJkCwm76IKg3b1egaGiztJ6odjiDffiinUieA4MA3UxlP7HA0yijkMROD3c7sBN4YinwTITRSK2JZcyQKKk9ysHWB-Wu1OxpnwZCLEroD4sIuwHY-l_fpSUE5eJXuNEmQTvD_oG_B-ucUR3GCJyhU0Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ببینید از خانمی که داره از تجربیات رفتن خودش به تور کویر میگه...
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71095" target="_blank">📅 17:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71094">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf229661bf.mp4?token=aJ4kZuIjolgVxYUGCxTZ9SX3ZWYOi2S4AFGjV0BKi5xUtDs3VmJnKm9FxWSX0piLKQvEaNSUM4tZdX4eYwtbSE4r51IBhItQG5CwJYJREW4zZAG2C4d5mBWAj7aEHHA5XuZ5wybyYhZmDlwQeEAzvlMnmuEn-Th7CkaEJGHrSwX1ThDfZN_-U6uPBB8WbO-Yenwi5AHunhxbWZtG_44BbXsPb_Cw5G_rJtKOMglW5CDcWlgX-jG5xdmjHztIQMdFefBbBrAk6eUrDTz7HzkKLDqT_HplziFIIJPGd6CGkRrmlF5ksXWdSLBqA8hQTY3711rjA64T83XhO1YvQW77FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf229661bf.mp4?token=aJ4kZuIjolgVxYUGCxTZ9SX3ZWYOi2S4AFGjV0BKi5xUtDs3VmJnKm9FxWSX0piLKQvEaNSUM4tZdX4eYwtbSE4r51IBhItQG5CwJYJREW4zZAG2C4d5mBWAj7aEHHA5XuZ5wybyYhZmDlwQeEAzvlMnmuEn-Th7CkaEJGHrSwX1ThDfZN_-U6uPBB8WbO-Yenwi5AHunhxbWZtG_44BbXsPb_Cw5G_rJtKOMglW5CDcWlgX-jG5xdmjHztIQMdFefBbBrAk6eUrDTz7HzkKLDqT_HplziFIIJPGd6CGkRrmlF5ksXWdSLBqA8hQTY3711rjA64T83XhO1YvQW77FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
سامسونگ A17 که یکی از ضعیف‌ترین و تخمی‌ترین‌ گوشی‌های بازار به حساب میاد، قیمتش به 100 میلیون تومن رسیده.
البته این قیمت واسه دیروزه و امروز احتمالا گرونتر شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71094" target="_blank">📅 16:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71093">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc7b61838f.mp4?token=LFhmXaq3Q_fGbPx2xK9peJ3LVbGH-D-Qv9zJwL_iGKVJOOQrGX3eLvUHJHFybgN-CSsrQ93RhhqdnV9xpVLxsljNyUSgH3REInfPbiifU38-gGxDL9gxspfKhtw2vDNN7xAge5ZXxaCxtRgjN41YHXiacbunDeV8P_8HnlyNgF8KjAjn_Vq7Tob_fW-i7mvqUgI6wLHIAw7HLQqndIIHSlxToBkgFNlEfsz_uFQrzwGWuWqAaY-A5i73XkOjz6roaNv9dLTH4FnQOxJFGvAWEX9RVy2XTvqbiMBjuv5qjHX_HNbioztOJv7C75ROaxeUl9lBoWRXm0Typ39Z-9xXKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc7b61838f.mp4?token=LFhmXaq3Q_fGbPx2xK9peJ3LVbGH-D-Qv9zJwL_iGKVJOOQrGX3eLvUHJHFybgN-CSsrQ93RhhqdnV9xpVLxsljNyUSgH3REInfPbiifU38-gGxDL9gxspfKhtw2vDNN7xAge5ZXxaCxtRgjN41YHXiacbunDeV8P_8HnlyNgF8KjAjn_Vq7Tob_fW-i7mvqUgI6wLHIAw7HLQqndIIHSlxToBkgFNlEfsz_uFQrzwGWuWqAaY-A5i73XkOjz6roaNv9dLTH4FnQOxJFGvAWEX9RVy2XTvqbiMBjuv5qjHX_HNbioztOJv7C75ROaxeUl9lBoWRXm0Typ39Z-9xXKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یک راننده کامیون:
الان کنار مرز پاکستان هستیم میخوایم رد بشیم اجازه نمیدن.
رفتیم پیش رئیس گمرک میگه طرف پاکستانی اجازه ورود نمیده.
پاکستان گفته به ازای هر ماشین باید دو میلیارد تعرفه بدین.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71093" target="_blank">📅 16:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71092">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45bdb5a184.mp4?token=PP6gcOePyPYOamXvn4SN0W3K46fNFmRTf87DSeUSpaan-siJrDyVL_y2adhDNE1T35_AsMiUJYFTRE7Z6pxxzpMJBdvMHVm1fqFTjRiR6eDAMdqfe92IUVuSR2oAkzpr3jXuMgJhXE3OKnq5KwkR1syiV2VTNK-fjQwD7hHC8Ix15O3V3Jsd_kVD1LNMyMnH3N-bPPyl1ZBlt_Sw0Ksk-Up3Z8VQgDvsuqo7gtyxJW961OmbM6Be0EsL1LNFR-PqVEKhjfakINRZjfUtalqkDTzhVDhGsuXuoEPGBmNOkltiPLEib_2WDEDcn4oFvtQHqypB3DFohw5s8_xmovDsWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45bdb5a184.mp4?token=PP6gcOePyPYOamXvn4SN0W3K46fNFmRTf87DSeUSpaan-siJrDyVL_y2adhDNE1T35_AsMiUJYFTRE7Z6pxxzpMJBdvMHVm1fqFTjRiR6eDAMdqfe92IUVuSR2oAkzpr3jXuMgJhXE3OKnq5KwkR1syiV2VTNK-fjQwD7hHC8Ix15O3V3Jsd_kVD1LNMyMnH3N-bPPyl1ZBlt_Sw0Ksk-Up3Z8VQgDvsuqo7gtyxJW961OmbM6Be0EsL1LNFR-PqVEKhjfakINRZjfUtalqkDTzhVDhGsuXuoEPGBmNOkltiPLEib_2WDEDcn4oFvtQHqypB3DFohw5s8_xmovDsWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه دختر حامی حکومت:
فک کردین اومدم از قیمت دلار آه و ناله کنم؟ نه اومدم پاره‌اش کنم!
رزق و روزی دست خداست نه آمریکا، دلار قیمتش عوض شده، خدای ما که عوض نشده.
قیمت دلار هر چقدرم بشه، باز روزی مارو خدا می‌رسونه، منم اعتراض دارم ولی ناامیدی تزریق نمی کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71092" target="_blank">📅 15:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71091">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2be4c50b6.mp4?token=BA-S2DlDQOvf3_vphRjAL7PhFJlWyXduGJ6sQOuRVRb28ukk0ltHHrW5C5yUgrPzUAWRvqX34rAaNm-rTYkzsy_MNe1W7HdBAMMkl8J-e778kvP3B_UPn6TOiBX-PYLNlVWFhu9Xq8o38BDkOjZbVbL7icHHX2ZaSnJ62x0sxVQRP7J0DpsYlGVDy-WrKDaXbNSy83KKJFc6MrJXVMzXzw312bpwk36ZgxDuzdsBeycYsrz-8g94jrXRICBWc4HUG7vGzzc9fUQaa0FlKjAaIWmUDDVU0bCx_1QQcjSKty8wdK_wyYQb-77jd9vzzD5_f7lOWkoLO06YvU7biTJvfTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2be4c50b6.mp4?token=BA-S2DlDQOvf3_vphRjAL7PhFJlWyXduGJ6sQOuRVRb28ukk0ltHHrW5C5yUgrPzUAWRvqX34rAaNm-rTYkzsy_MNe1W7HdBAMMkl8J-e778kvP3B_UPn6TOiBX-PYLNlVWFhu9Xq8o38BDkOjZbVbL7icHHX2ZaSnJ62x0sxVQRP7J0DpsYlGVDy-WrKDaXbNSy83KKJFc6MrJXVMzXzw312bpwk36ZgxDuzdsBeycYsrz-8g94jrXRICBWc4HUG7vGzzc9fUQaa0FlKjAaIWmUDDVU0bCx_1QQcjSKty8wdK_wyYQb-77jd9vzzD5_f7lOWkoLO06YvU7biTJvfTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🚀
🇰🇼
روز گذشته، یک پهپاد انتحاری که توسط ارتش جمهوری اسلامی پرتاب شده بود، یکی از واحدهای برج مسکونی الدیره در شهر کویت را هدف قرار داد. این اصابت باعث آتش‌ سوزی و تخریب کامل آن واحد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71091" target="_blank">📅 14:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71090">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a0b6b730d.mp4?token=LAUVMmtPhfF8rG78u0w7X5rQwBKizjFawU-mIBc3lsWDlw5IL-XwAZtLonHpKzT1CYEk-wJ2ZD-5Pdn7sHBgAutItXkEw3HUs_IuUjX6SrJR0ENEkOUiIJvUHeo5T6QEpr544LhyiwangaBqvPdik0LqRzaGCzU4BuIGmTfU5BEFuksbR9I0SNtKQP3uCd7hT1klTuSxlzu5V-AtMxwRJwSfEnvgEypmj6T1HIwsfIwgiT6cJ0B4ZBjcb9QZ8ki8Zfp3uXvC9MTXpd2iKsVp75kFyf6vR95M-bHYIFBcOQxpQ7eT4FhF6yPTXx7UaVcBiJ6BwW-G2LSpA5pYBjNp_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a0b6b730d.mp4?token=LAUVMmtPhfF8rG78u0w7X5rQwBKizjFawU-mIBc3lsWDlw5IL-XwAZtLonHpKzT1CYEk-wJ2ZD-5Pdn7sHBgAutItXkEw3HUs_IuUjX6SrJR0ENEkOUiIJvUHeo5T6QEpr544LhyiwangaBqvPdik0LqRzaGCzU4BuIGmTfU5BEFuksbR9I0SNtKQP3uCd7hT1klTuSxlzu5V-AtMxwRJwSfEnvgEypmj6T1HIwsfIwgiT6cJ0B4ZBjcb9QZ8ki8Zfp3uXvC9MTXpd2iKsVp75kFyf6vR95M-bHYIFBcOQxpQ7eT4FhF6yPTXx7UaVcBiJ6BwW-G2LSpA5pYBjNp_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
❌
🇦🇪
با افزایش تحریم‌های آمریکا تجار و بازرگانان می‌گویند امارات از بارگیری لنج‌های ایرانی خودداری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71090" target="_blank">📅 14:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71089">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28ac9cc9fe.mp4?token=BV80ZvG8mXHpTQAJzwJUFfE09PBNG38-eEYTEpBtRIIvzEivbb2RF3kGq9PQejp_xUVSnBoJmbtwbX_CvShxR-FbLGC2NCpqx5UgCgiINwpsovpmGgjT0pRsuOC-L1Su1vQnwtOaRrgkzModHkXOIv3Wt-Al2yWhzPdX0Bj8UuiiTQigehWimFF8DbfyMFWl0fStCfisNON-ZsRM8UYBffyotGwq5aUa9RjrVmyiQLoPH__6Zf5g09eZD2zuDAdtFHdJVOqoLwsStUhQqqpn5f6HX-DYBEbtEG28oO2DZ8SEMBGcugCmG6K2nu7v2yPY1P5E9Nzon40zF-e0zXs5yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28ac9cc9fe.mp4?token=BV80ZvG8mXHpTQAJzwJUFfE09PBNG38-eEYTEpBtRIIvzEivbb2RF3kGq9PQejp_xUVSnBoJmbtwbX_CvShxR-FbLGC2NCpqx5UgCgiINwpsovpmGgjT0pRsuOC-L1Su1vQnwtOaRrgkzModHkXOIv3Wt-Al2yWhzPdX0Bj8UuiiTQigehWimFF8DbfyMFWl0fStCfisNON-ZsRM8UYBffyotGwq5aUa9RjrVmyiQLoPH__6Zf5g09eZD2zuDAdtFHdJVOqoLwsStUhQqqpn5f6HX-DYBEbtEG28oO2DZ8SEMBGcugCmG6K2nu7v2yPY1P5E9Nzon40zF-e0zXs5yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇱
🚂
برخورد قطار با یک کامیون در گذرگاه راه‌آهن در گدانسک لهستان.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71089" target="_blank">📅 13:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71088">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b60a6b68b8.mp4?token=cZwa5-XdGBZiwSI9gUPSRuQ4EnVSo_G8LkpRvUlmMqDQ8ct1fFWh6X97F80Vecf2yShwcp-lf1s34KoO1RXEYf_R9Ai2dGpyyVI6uBb7EwRDBhoQXohFK7CkDpyPvbAja2B_3cqTp_AIcurQgdUBz8pW1C0svjRl4LUf6mejvsIbs69X4sC9jd7GDHO8Y2vQKrGNwtVuEfzEdNbWnztkSFZCzwc8HC6XEV8dtnKXczcJfI9bcL0qgEb9d64XCG7csmEuxp3KMPuyvXex3wmChudZeEwkYfy_f6IO__r2XcM1aKkM9GbFX-YI58uiCotkkRn6ZYltJ4us-EMLFgmoOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b60a6b68b8.mp4?token=cZwa5-XdGBZiwSI9gUPSRuQ4EnVSo_G8LkpRvUlmMqDQ8ct1fFWh6X97F80Vecf2yShwcp-lf1s34KoO1RXEYf_R9Ai2dGpyyVI6uBb7EwRDBhoQXohFK7CkDpyPvbAja2B_3cqTp_AIcurQgdUBz8pW1C0svjRl4LUf6mejvsIbs69X4sC9jd7GDHO8Y2vQKrGNwtVuEfzEdNbWnztkSFZCzwc8HC6XEV8dtnKXczcJfI9bcL0qgEb9d64XCG7csmEuxp3KMPuyvXex3wmChudZeEwkYfy_f6IO__r2XcM1aKkM9GbFX-YI58uiCotkkRn6ZYltJ4us-EMLFgmoOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف با رفیقش رفته دور دور الهیه و به یه دختره شماره دادن،
و حالا اولین پیامی که دختره براشون فرستاده
😟
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71088" target="_blank">📅 13:49 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
