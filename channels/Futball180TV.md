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
<img src="https://cdn5.telesco.pe/file/oCRfMHctDv52afti7MeH-h-_cA5m1j7NwspSUXMNMLQHQNSGkUCnqtozIL96feFaNMHLkUjV3vtRkwoiG_8aVaO3nWjHSxeGYPQEfjXaNu6wyK5FgncfrifKt_lWrIAeKyJufjuGv13meGpcxED2491AgyrReStQjt9OZuP1CwJN7XKEUSHe9HTaKnv-zMzkf07atj89DgXUoOn627D7vDAle6Jme-wGCe2XOxi2Iq2rXY8EInYSyOan2lZ54Ex9XfC7Wy8EQMBv9zfNdO28hpNz4wxk9azZa_59zuiCFud_zkzEWDt0oxQgGe9Npxj6PSt73zQ7WYzDMH_2wBGAzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 533K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 02:24:00</div>
<hr>

<div class="tg-post" id="msg-101852">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7211acfa.mp4?token=gha5Gup9AWk28a96mlAumZ2LinbP02xa_qVmhvlteLn14RoL9o2Lbb-w1CbNHB1k6O5-9CbjSWnZhXZ2ZGFAeJFSthNrSfZYHAkFek6xHySfjoganF4K7j2uDR4GxxvElvWEECYXxc8S2wXw8k6tYYnQJf7eT9CKXpE1EA65jcF0v6tcT-QawyxAte_zpVYV46IEMZcbXSetp8g6eFpOo79Nt8-1XaN13Rc9PVaCMKvmV1iOgm0eD5fvh4gjaXuWfT-Z-9egOxV256vuI-O_om4acX9sSbt92KCDgymAnWnNSzRxCTXTgGTFNSn576x9E5910p2i83b9h8oRRUca5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7211acfa.mp4?token=gha5Gup9AWk28a96mlAumZ2LinbP02xa_qVmhvlteLn14RoL9o2Lbb-w1CbNHB1k6O5-9CbjSWnZhXZ2ZGFAeJFSthNrSfZYHAkFek6xHySfjoganF4K7j2uDR4GxxvElvWEECYXxc8S2wXw8k6tYYnQJf7eT9CKXpE1EA65jcF0v6tcT-QawyxAte_zpVYV46IEMZcbXSetp8g6eFpOo79Nt8-1XaN13Rc9PVaCMKvmV1iOgm0eD5fvh4gjaXuWfT-Z-9egOxV256vuI-O_om4acX9sSbt92KCDgymAnWnNSzRxCTXTgGTFNSn576x9E5910p2i83b9h8oRRUca5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
‼️
🇪🇸
شروع‌قدرتمند آردا گولر در ترکیب رئال‌مادرید برای فصل‌جدید با خراب کردن‌پنالتی امروزش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/Futball180TV/101852" target="_blank">📅 02:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101851">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqBfL5eXffk83RIOptdjjsekAKpKqqa_WKRHvwWvf21h_CHcAU6DFE8-IwT5_8QHh-H2rdRrbu8SIAKmMM21aRwRVm9Dk3XGKPyGlXbfJdOH3e8hMdIhtcmjjJ5whEE4i2bwiYTZGif5ZDIsJut2vbhKTM1HIVwOLOEW48_iFeRHOWfSNfGNTLtvOd2nPeU36w3KAqP0ma89nAGs7D9Ll_wiJx4qoU6H3E4B8qgj2jz3Cyp7xRe6p0XPUgidcFdxZ5C0psFTu416pMftcnmI2C_oO2eXe0CQ-VSvUEqYC4YSavV3AEG_I7eugiaea4gLPIPAL78FzzRlbzgl3lf4YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇻
بر اساس شایعات منتشر شده از منابع خبری آمریکای جنوبی، ووزینیا گلر شگفتی‌ساز کیپ‌ورد فصل‌آینده به لیگ‌شیلی خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/101851" target="_blank">📅 02:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101850">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c-dxPaReRuS_mY1ZdYhm7r1tGjq6MWqQcB7KFQY49ipWzZ35Bvw89p1JgxaN4oyCR2sJqcsE9yUhclbHfL0-4mtwfXntsCJDYGPwsFiH0b4L0Z8XswqlsYxqsZcxM1hgxr3TELR9IlnHZAtUwhHbnUVEKK-baVhIUXNJ1ZGAn3DZdkKHOixN7yJZFpBuIsE6deUiYsVgVmZ-9n-9nORboljarC3jbv3vBFbURaqWNW5XZheKDnXu0XPBnv-gVvGaxQX9bao6EUmV7kBiNxnsp9f5AJ9V0tFpRBSUWUZHyFirtZbJklowJWh0zrliGICWh98OgPTa_dZ5V9n1IYC1jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/Futball180TV/101850" target="_blank">📅 01:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101849">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pO_irJUtT2rhxfqpKf7PyD-gSlt8-7YlalRilBltYgkKs-leVbRM6aHH2lj9GZxO9mnE-wkgw81NDwORIXC6U_V5pZbDpe9-tI-deedBf3dXzjy5A4XjxWeh5aCKQ-gKg2nFDHwxihohDNE6KlLikVXgEirRKakIWUmyQxeVpC9uJOLtTOp2SG7qnhQrDnFYZImr-lEXd22iy1xLQjY4wzC5pIEyP7osclBnKCqXQMRDyqrBJS3xjLKbbNksV_ayhaArZEXhDI61CAgLMRkjdE7Ofts70NtIzEZE2mjfHHT_athypEJ9DCXeB-64Pcy_nEmYQ6GZVSjFrRZ-Fi_zWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
🔥
🔥
🔥
مارکا: دیومانده تایید نهایی برای حضور در مادرید رو داده. این بازیکن به پیشنهاد نجومی پاری‌سن‌ژرمن دست رد زده و گفته که فقط به مادرید میره. مذاکرات فشرده برای توافق نهایی با لایپزیگ درحال انجامه و بزودی خبر رسمی میاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/Futball180TV/101849" target="_blank">📅 01:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101848">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eiy0tLkafz6e5NlgE8OZSAEMIPYxqD3yByegkuWZSDo8mrUrf8iDW4CGXfHaBbj-cauNwaN9W-zLc0OSHIXtnQMp3rWYH6J0fmiNKXZF1YV4PyA5F3yuQP4O-XAWDFfU8nyHW7TQu-ncso0vkTT2avCyTdygfRuLxA7e8GU1m9G4oyInNQJYgcjbEnH6TFijjtw4-SArep7PATKU7ys8_NYS-34GI8mEge94dy3bnVS6mmcdRUb4k-UON7AGJMvDygYK-07hML9nT78MErKUswbpDrfXzI8dK8EadpM4hmXONJTNezO12LUf3FOv7DPKu_fzOfffJhZfuLFvA7bepA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
په‌په‌آلوارز: رئال‌مادرید و ژوزه‌مورینیو دیوانه‌وار عاشق دیوماند شده‌اند. این تلاش پس از ناامیدی از جذب اولیسه صورت گرفته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/Futball180TV/101848" target="_blank">📅 01:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101845">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EAI7ucwi1x_gDmhKAbBnyUzCpOS5JSH7SoJ-79ghUx2VQ8idGPdg1r_erIIsXszmr9JMPRTHXdJbpb0H9k9EMPiNCucEvuCo3ZJAxDCJiw9HIKqnqEsTcNIDBFnKULWDCP1Zg0NumoVt2ZpFEywflFpw6EqCZMDtCve0rrSdxRjKokg8ZWbUn-PXCkDqlgUhDis10n91XTbKjiMQJ6ftbwacTgZot9teSupp6IDb4luOe-3maPdqJMBHavVqrNoUg2XKYSznaNZ1nWjEfiCgIv5J9RfGlDs0Deuue_Yjk-prr0gWSlyWhpKhTxQDanTD1quWmJczWytCzpb2IBzDNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oCTN1H3XHJjlyofiJBerARkC7Nb5pr1xfINQZaiqLJRMGFghJhSs3TE59yYVyHUhoJZFo9YdcKhKZnLJFQw30wbLplUyHDgsqyCCrwVz6t_HM6PD46JbczzaaRbjKZx9e1KC2VKNadM-tuos0kSHYZhJAL6y_jNg2XJ0RafKY5YUGoSZkJV6wm2IlTx7DdQdgG3FY06xOvZpzd3smo3-cFhbqwT3g4hcVZR1RrY8-rSO7WHKdJBrxurxY6c8qeJ69vexJcYTzJaJoCyeya3zab1dPLOB_S70smHkWld3YJ0zpltLyQyETmwLtEsEXSrDryn6Iw4yqq-U9IdDxWdC0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
په‌په‌آلوارز: رئال‌مادرید و ژوزه‌مورینیو دیوانه‌وار عاشق دیوماند شده‌اند. این تلاش پس از ناامیدی از جذب اولیسه صورت گرفته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/Futball180TV/101845" target="_blank">📅 01:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101844">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkGT1Uf4vJHT7WW5fKhCHEH1noxAngcVWG8bIm1J3ZJR1xR2gs3orFjdEG_jKvTQFo-GV9lLQe3eZkKX6WQ79lj8Egesr7UwlyUhiqvM8OkZFvb_5Ik3pBp-Rx4s48eEoSCBDsxTBXtDYv5DZMT-_aKkvgu1L8bCIPerLUrkNstqASx_pI1F2oeH_P7OP7mEp6oZ5j7oJHkCkyKMQn4WevVArDMPF8mSMn1v8osVXiDo2F2iIH7uK6MXzdEq7g--4ezuWA0L_GI2gRx47XjLZwBY3deRhKqITb0CmGkebIFt7q56CTsEkzrm_9mGmtCc3QSKRU5CYVSKcD31MgjCXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
په‌په‌آلوارز خبرنگار مطرح مادریدی: در رئال‌مادرید برای یک‌فروش دردناک و غیرمنتظره آماده میشن. بزودی نام این بازیکن فاش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/Futball180TV/101844" target="_blank">📅 01:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101843">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ko-UK5yeLKP53oFX3c0Ll5uE0HHhFXCW0p2xQsCyDS7J98ckUzTa0wz8l_X3hFuoxpsFvyKvGHKQI4QZWGUUcGjqB4muYwKDeKkK1gt2cT1tnvLudSOcipwBs-WCMEc15GPIlp1iNTV_gA7JMpLCYJRkhe3VF1eW_hCjzqEW9sgHXBE3J_JWFLXh6vsCb2ZSR_pX217eET_p6NzAx3KbHvBa6C7fsr-b9LgnH7SQQUmlASZ2wwoHmGOErO-oZM_UJAM4AKtRN9SkMKVtvQZie-xwghEx5H5BFozmy4t2ESgTnzgiOtvwipGpWLmS-QpzvHE_yDigwOnEzMmWOhvr4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
په‌په‌آلوارز خبرنگار مطرح مادریدی: در رئال‌مادرید برای یک‌فروش دردناک و غیرمنتظره آماده میشن. بزودی نام این بازیکن فاش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/Futball180TV/101843" target="_blank">📅 01:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101842">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
⚪️
رومانو: رئال مادرید پیشنهاد اولیه ای را برای جذب دیوماند به لایپزیگ ارسال کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/Futball180TV/101842" target="_blank">📅 01:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101841">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dkl-bjDqFmLy0NWGgzqKJ8KSOr5KrpZUENoUv7uG4BgPHz47CIdCSeFDJ49Axlfguvg0dxUUUfcN23RQ3G_OuNubAaBBchgut_48afv6iKwfBq-ITQ5QW9eT65RtyrLTF0auxu4vrHkFu8cGrOoE03bodAcSynig0QBXOpQEk9wYxaEBWr2GyXNJ-riQB8OJQ3rOGS2GHzinSPpsDP5-zs2EBQ1Xb4VL04mNaIhBcyhDtTFqsKSDzMeRN50xVe2ANP2r4cvDRwB3z_E_3Fk2PeClSfzs8qB45QGHFOyN6m1tzUmSsOmg6jrtW_wnYDzKZgCt2Fsk4Axmzm-U8is5qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیژن مرتضوی و بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/Futball180TV/101841" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101840">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOgmW3Zndc8PHocJU0jk_b1guPew-Wwz8_LlI1CnLdVAWqIa124lLWQjsm-aS9_pVAz46D9I77DDhpHLLp5PeMzt4w5G46p9pAtF3Xq6YDGwJKwXLjKHWwHjJQ-sp0Kn78kdeAbnZLEw3yhA38bu7lHyIjgpof94M9ACV86pg2PTOWbNcDtv37Wr33zbqmRiJPt3PWSqgGrxz_EBkP0dPY7kq7-cQ-fxilb3gLOj3uwpJHcUSrOAqbYdxEwXQVLheg1yogr7LusfKwSEhDRucI-J-vsyn2A-s99Ahu5E2TidbcKfUymxBNHTVWtqhkQXiXxsXYtEVuy5ObG2lRWxxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🤯
رقابت دو اسطوره برای رسیدن به ۱۰۰۰ گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/Futball180TV/101840" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101839">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8hS5nyq9ZDtekpSKWSLar57xy8jXakgHmZVnxvPscClK-T_aAEP1qQuCn9gMM1NHn-s3T9q0IYgy9Mx5i4meZBuAyggVbBD0gpzJ0vAs62eTSpxUnyF7wSytTAicgQ7hXIByx44okJRDiqk6ZiqTm-gGIEIw4iwa1sslgKla2uv2tvBaxYgKr8sn1S5xHTj3rtMJrmo4C2FS6Z6O42mLGBmmPGPlxJfxI2NPiTSiT1S1825OJ_YvR76BFy4UqaQNYsOagBshacayxw77MR4z9OorZkrMVngQBpF3FN5ID2-3Ar6pp9o5cRAp6EqKHaekr9DEuPODbsy8XR8Dl5uhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رومانو:
رئال مادرید پیشنهاد اولیه ای را برای جذب دیوماند به لایپزیگ ارسال کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/101839" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101838">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxzpsXHbwHHrLVWtztRRB6Abzj5eJ7VrWEq2tkvGTJAvpe2q7awCsudnWNv1ceSkcntfsOcDCdZs-Oez5F8w_-248UwRWkTiV-TWGgg2X8yZIbNqIM8S_bL9O-r7JAo3xGg6WrvjW-RWAJCebuiftIEnwHZ7zknOFpvgr5ONG0bZfpohpOB1TSFb-qrku2TZDcSLgwmBzXaPC1mHCvLxNA4zcry86xpNfHiGZW366lD2zHSjoRZfVLW_MwSIqZxDRXSqBuMy5yTHFAvCNNfToSrBsl8YkBtjnpfipdWP7jegLsEl_ORYwekJIn7oJSun9WDQ8KFkuN4cnjHP472mgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
بهترین بازیکن جام جهانی ۲۰۲۶ از نگاه فیفا و برخی رسانه های فوتبالی جهان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/101838" target="_blank">📅 00:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101836">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCa8kN7cB-y_X-JVn6Y0j5VLR5Oqp5JYMRhwAM9-x_54nhgvaBRFfxpt_bcLGifmsMffBaLBDbiRp2PtMXkaicgaBkuH1gYlcv1-6xw7ZWDc1ZBeLM4fpERnIO2WVWJWQO--__BbXWtSVxxkUYuXV6G3-qB4Svm6CwwrMRsDI8D1KJohjuE3G0c63NRr3GlP5ohLNiaHrO95MHHzt9Cl120gGLdEe7kyUwvJhxxC4RhuR60CHY-iPyaXwxvVO5r0TqbwOQFfCBWWXtFEdF7uK6OkZ0Od7X5xVAe6fhJaCn1BddHygnqPRJWOXohhIez4r46iCLXY4myzGFrLglSrvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تیم ملی آرژانتین اعلام کرد که لیونل اسکالونی به عنوان سرمربی این تیم به کار خود ادامه خواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/101836" target="_blank">📅 23:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101835">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQssKl4K0sbjOY-93pUKzjemIUDfr7dn-UnhSh1sl8PWoy-2OiS_yQBf3DNpiE-7IJ6q-Aut227cidbgGswHI2s_hw3YPrpk9eH8aEeVkIzaV4eznWE9wdOsCGz6DYlqH69oBY-bG61CmYBA5swII8Zs27mQm4jOlFKgm-yWf2AtMGglfyu1aAOm8yU0RWsTolta3mZ8O_MrVzXbQAXHXvYkQi2mmwHodmx-rr8fvUFYl62Mdkm8JsXRyzG7hoNiSVkRvJKUU_I861VswUOb6-g7QApIk1qFDdYmzDBH9Vrxow_UKjnDRFAvkb7FTjg5lg6gcC-YPzpcbMc-Ju4bwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
فهرست بازیکنان سانتوس برای بازی بعدیشون مشخص شد و نیمار به لیست برگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/101835" target="_blank">📅 23:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101834">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-CEXRC4nNi_EY7zJWzkogVfcK6QZHqZZCxpE0fkwU805e26DOxvZajlGWoMBkOenZQcPJk4-Jom-7E0Tu84RY13yPzKbA8KYlVXlCfN6CNZKFF94uVS3QCA5LylEu8rZFwnKHBJRhmCW67y2c2DtSzKixRgMRRKZHg_3ugwqzBmL-QQKo5WBlxz6a7CzIpOoNFV33YpVhHJH-hA8XvNV-MtoBvhRlydZVZ80MBPJmWlPaa4W-vzt73BkotjSUZ3iJQQQ43kOAAbDQixT47d7gB0ypWOU4DYiosn073lLg86ujESHPeen1IWmhTGHz0LC81LTZ5UMBndc3NvO_HyAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لبرون جیمز ۴۱ ساله با فیلادلفیا سونی‌سیکسرز، یکی از مدعیان قهرمانی NBA در فصل آینده، قرارداد امضا کرده. این انتقال مثل این میمونه که لیونل مسی ۳۹ ساله برای فصل آینده با آرسنال قرارداد امضا کنه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/101834" target="_blank">📅 23:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101833">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
🇺🇸
دونالد ترامپ: با وجود اینکه درحال گفتگو با ایران هستیم اما باید بگویم که مهمات ما برای یک حمله وحشتناک به ایران تکمیل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/101833" target="_blank">📅 23:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101831">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFxco8IjE66VR-rE4X6E0ZSGhrxZmFXWUvSqtrKdBkPf_wukH8hQQy2JsBZ9Av6OzhmSEMa-_aczT6M0oqAa4f52fG1Aeac-c7aMObLxTchl3PG0_BRBhii1iCnaqDy3iYaFUhF5y1elG4Z90Epd_aUICkGGsvWvJl3sThoP1SopLXylt6h45NsPtcIqJPvyYFRAFxIsgMJqpaydFeJEwaSfSthlRFiY7iwHctYhjnOMc2wRFngWFuC34cF6mQdRcNHZfCLdd4fAmihe-_tJsNh6Pxwy8ZlBteiPopK1Vp-7hsGEQz008swN_g_vcUW3VKM8L3mSdkkeKBlPQrmdAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V3oSbscJ_ZCHVjkr8oXJZR-fsZG54ZMpEQ59P_uFw98XjA7-jYU5T_N5zW18mgcEJUaKbItVe_yX5wjBzVgOkxOLOgnVM5lLsRc2Hec56Dxx5r-7Ye7FXxdMxBJ2hq1fgiXntPosv57rQliYucMjQ6PSqEIAG0wzZUCKkqL065V5XxeOlUKxRlKwcnbHxjVZhwn17JbXor6F9K_zCvFtTiuPEWXHS67pWH3giNctz4l3uDqN505woaz9RHZLJQtxmnZKxtT6nZcGERDI5jx8NK5cxNGEHvubB0tyHuLZw8ejd1Wz2uf96j0aef92Srt0m-y41DDsyRWoxPZVF0wkDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
نیکی نیکول گفته دلیل جداییش از لامین یامال، دخالت‌های زیاد مادر یامال بوده؛ از تماس‌های روزانه گرفته تا کنجکاوی درباره جزئیات رابطه و کلا مادر یامال علاقه خاصی داشته بدونه یامال تو رابطه با دوست دخترش چیکار میکنه! او مدعی شده این دخالت‌ها باعث خراب شدن رابطه شده و همین رفتارو در رابطه فعلی یامال با اینس گارسیا هم میبینه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101831" target="_blank">📅 23:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101829">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAt5iPLj__t7lMIrQ6cs4d0XSal9EUzZ0hnGzxpWBseSUwKIiDfDk0j3Rsg1KbtzGJxGWjUuTruvkQzjYs0q5XQVoUgzaAkez3N1z0P_zxnnLsMlJqQrKov1aFuyvtoHXfcnJOgF_7XprNMfHZwKJTgMyLZ2nHqy6gHv2H2KC1SRCjvANsktpXdD-5MyB3vN2R4aYlJzoPZt16IkmduFmwDhd8Cm420ue9jWpfHTrxkoSYmq95U6GAOyNx307tPenF_OTGXiFz7ePxSjS1faK5CBBp6roM4u3gUCb3oidcIQlsrV4NL_3OzI--XXC1EEnqsapjZzka4wcGnY_cLH9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dg9ko3xT0_2JsoswkBJovv0oDTGFU5sVU6aOqsY7PyNlm1bqlJs4YSfzjq9hMAJuWGHPrMKIgzD6TJYGYvpuGus1XIsfB3FS0JJfKqe_Uo7kKUPzbpspdtr-ONQntNB4XbSQQYZVHhCOj43BGRIToUXW0ZGZ_FynQbo2QK9n0NBSScRwljIAPRkmfvDQVt-EnVnfR0OGVITNswD6HKJ404KD-iqhQoo_zewAwp8oij00xtuOAz6jstun_ZP2VJ1fKx0z7tEI0-K0YPqt3j3y_Yo2p2rYMB0StRH36J-GdxaF5Q-1NonmuGyhKFuZjLz9_ubGumaS3B3ZWulDsjI1EA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔴
زمانی که رافائل لیائو تو میلان بود دوست‌دختر سابقش با استفاده از مدارک جعلی تلاش کرد ۲ میلیون دلار از حساب‌هاش منتقل کنه، اما ایجنت لیائو این اقدام رو کشف کرد. تحقیقات پلیس میلان جعل اسناد رو تأیید کرد و در نهایت دادگاه این دختره تیغ زن رو به پرداخت ۵ میلیون دلار غرامت محکوم کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101829" target="_blank">📅 22:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101828">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBELRp1JN_dytesghmoDqUaUmUXf-itP2FefrljwWo9ooqAfKaZ36Xo33M8q0QeKrAbfhC0q66RcYmrdL1fdLbiAiHcvkc-XGg_Ni5kzAGFP2KsHcLhU8it_VHLz9RdZd27Hm7fHK60acL3Rtbwxe4X6IDNiSbCItc21D2Ad0HYfTeBy3Sr5jGMx7Vel7vh4eYFOEyc-lSaVVPe-s8I2p-bXN-QOVJlHZsWC04_tQi1SgacyQpF64Okhoc4OGtiFc04iphOdBP4B5FWuGeJYgUl3TC6CpIL_ZrOqnHqFIoRu72Sy38h0gNlxDXS2TdodrURzbaI4w7lHf9aX07n2ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
توماس مولر در مورد ادعاهایی مبنی بر اینکه داوران به لیونل مسی در زمین امتیاز می‌دهند:
🔺
"در مرحله یک‌چهارم نهایی جام جهانی 2010، ما مقابل آرژانتین پیش بودیم و مسی دقیقاً کنار من ایستاده بود.
🔺
توپ به سمت بالا پرتاب شد و به دست من برخورد کرد. داور بلافاصله…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101828" target="_blank">📅 22:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101827">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpNkFkSeBqTrI0wpaRgGOMgIPQB1_VqmgWmf9TtgTcIfCgCu-OUtv473buM0XzzHa43N96xNr0Wm40qHvminLO8OtCgrZHREvR7gnA5F7xQkDR-fx9vbo8Qv1XrbGo2-pVhFw1Wa3g3YF0MD316A0-bziH_47N2tSa78TbIMMbyLDgjOQG5u0Sax4yHRJKKVILXsVw-pinV9eYlvZpRLr1WgObl26FWiAi9AqdDF61BSLAQ1Jfzu0F0ooFB1Trrk1p-n5O1aRdCIYdkp3qV9tYKEbUh9yBCkprBs_6pbFvtFiFoCgfLpH2ymGn7bXhsDkeJQUQmU2G7VP5Dc5YwvhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇸🇦
•
الهلال رسماً سامرویل رو با مبلغ 70 میلیون یورو از وستهام جذب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/101827" target="_blank">📅 22:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101826">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDtiSQ3T5kayivVpv2UbUwAsQGriPWhUh6QCJIKDLYQcBPWRdWLKVFlUtQxTQVwyoksuRk4Q_0E5GBcDdWBM1MjLcGwmw4uF-j52YiSzPuoQN1AVhWEhD3HbU6OqSJdV1mcwIs8yPGiAyIU8M7Y_aF5qEqXpr-uptHRTgVLuyihg3uxU2LoUh-OZz-uLql0ii1D6Xg6U5tnAzbJQX95SZcCQuCJjzaqL4kF3syAEwvGj4kPxDyQFwuJ3qI-jHEpKwBDi2oMlXUyw9REYgLakS5vl5XHKXrfiZNf_JrmhTv-RyPUW0B-DDA3cvVEg0A6u2h023xuJYfaZEzZH8L5ZNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
دیوید اورنشتین: رئال مادرید قصد داره که رودری رو حتما این تابستون به خدمت بگیره.عملکرد رودری در جام جهانی یکی از عواملی بود که باعث شد باشگاه رئال مادرید تصمیم به تلاش برای جذب او بگیرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/101826" target="_blank">📅 22:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101823">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k50o01M4o1plzV76Y0Ixp5_QzbF4BP9nI49McDk4l3jgJe8GprtqBhy8YuTx34omZKhVjmssYJfWdrPjn80g-gCjFLEA33ivEjWO9w1xnxsqf3Su5YJqBEgAYthkyXlY8OXH1Z0JZMcxLESH0HIgnSOeim_L6OI3P1ODUKY_kz51Bo6LZINXtgpV0QGh4j7U6pkUAMLsyY_kqpH_e18i9ZIDuQ2rFYTEtYbGsu3XB12G0ZkNnSpit6Lpsawf2WGr0Cz70eAibiGfhb_cmUViNTPqIqaPqWUKDElTzQURvYwOtOWULRQS6twV_nJPkq55s-aIHcuSRBQnN2Mi9NGhDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
🎙
ووزينيا درباره شایعات پیوستن به اینتر میامی و بازی کنار لیونل مسی:
من عاشق فوتبال هستم. اینکه در ۴۰ سالگی هنوز اینجا هستم، به خاطر علاقه واقعی‌ام به این ورزش است. میخواهم حداقل یک یا دو سال دیگر بازی کنم. امیدوارم باشگاهی را پیدا کنم که واقعا من را به‌عنوان یک فوتبالیست بخواهد، نه فقط برای اهداف تبلیغاتی.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/101823" target="_blank">📅 22:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101822">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XB9HU5ZK1y_pES4u6u2TlDRba_hyod27-NgTMHFx0oP92ZfocS-qG5dAHlXUgIPM69ryZlPIOqiSyv78xWbpokeNHP-7cb9bQYxlYR_HzfzGiM1cnqO9Z-EGEWR7q00njUyZ-Z_onyqOF9aopNSbSdMd8P8PnWkYFQ2Qv_Xyofll_FsrISJwJCvgdpjPAN2B8vZ7IW1lJFMcCw77ggL-q3jbXXW5lG3GiQRutVGs2Ngp2D1R7FnDbdiSXZLUlyoj7ogZ5clDiBCEb_YZsclE9Yk_HLhdQJnpojYw3uf0X1nemvqlSRklaxOPEY4qrDYjZDGAa0eUW9i19LtlAv0g_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
دیوید اورنشتین:
رئال مادرید قصد داره که رودری رو حتما این تابستون به خدمت بگیره.عملکرد رودری در جام جهانی یکی از عواملی بود که باعث شد باشگاه رئال مادرید تصمیم به تلاش برای جذب او بگیرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/101822" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101821">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLOjewV3Gr_9ahfS_suOPBg73gCyBlbRqhpgwy22yZlTAnAxkEVzYzwIyOzLBkueCqqrEbHSIXy1394fSim0lDSXmZ3uuuN5uVubSAkCoud2hnoAjIcCV1RszoYxkAq-i2AgO6vllxDSk0KA4QzYnRq8fztI51RUphqkOtEX_YRaLFnUHOxQm8wOO6Ok5Gwh6z00RnptiMsqkCEmstx5oBZlAdt4ID3vg7IaGtfzNvnRQHnIC686JY999cxVORwF9lDqBdXHzoWlACm4Rc_hzviGvdIoMAMk4AFrxDp3i0_mx0HtrQ6kwTCabKj8q6pOhIsJpjWK7Or3BuMa7RycoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
رده بندی ۱۰ بازیکن برتر جام جهانی از نگاه اسکای اسپورت:
🥇
🇦🇷
لیونل مسی
🥈
🇫🇷
کیلیان امباپه
🥉
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگام
4️⃣
🇫🇷
عثمان دمبله
5️⃣
🇪🇸
اونای سیمون
6️⃣
🇳🇴
ارلینگ هالند
7️⃣
🇪🇸
پدرو پورو
8️⃣
🇪🇸
میکل اویارزابال
9️⃣
🇪🇸
آیمریک لاپورته
🔟
🇪🇸
پائو کوبارسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/101821" target="_blank">📅 22:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101816">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i7xcj1BPSTC4zKjjtvBWx3p2iZVUdapcmZ_QCKhh2nEmdvFYbAGPsRuZE3RDecyFs08SCBotb0_TxWeSfj4zc4dk7YgYwViQZvaPu8GgYax7Jz-fFIzIhnUwOJbLH45S5tHbJO1IQ_g7ZcSJ4u0oMW7wzh2t4f3gpkretcU93n4DCYrbq_gpKb-uosH65kphijOZ0Jbhjyhw8egUPstGJT9nz2JjeL7MiiUTleFW3n8ed3Q6xuNOxPR76k-lU1OZpcec-ZNRq7euSIWQKMDEdmnszL6G9_hxBEgj5ZMm6P4nUuzzUCAwgBG1adFr8qYhKd4157ivekb-ElDtZbb_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxCLummXBRR0V8rQFq203bbTBfwxvOHnxGvh6IncwbAn2T3RF6RFaT5hNi8_Nlu1Q7yFA4wCQ3Ql-t6yX1cJOGHFrF6tQsSKz1amWbo0KAf6N3feXmVzwUCJVsMKXiE_zZODB-6dfL0L5_StTMd7VP0I0p5N1aHZEzhkOZ4EkvsGK5dlsK8JQHKiHsSn6QEmA56TKrDFp65ya1wdD2Jz9JxvZTgRFkcLzD8iiIhD38HG4pvRemf6JpZKOaQtbJQjELiFzccaoKuMQ3ReulN6GDjzWC-g-_o5iMVqLYbqRffT3OD1W4lok8lBscrvNOSPdGvMlQKui0f9r3fPpRWMVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/goKFsU_9TRN-ta3XCsY2vO_nFKzN-I6ZYRMLXxBB1CBMq5u_HTrwqK-cf_guu5WJ2EqVSUqktWAaz6sYxJm5EKqay97V3fQ3OH2mLTxwLZK5YMh1j9LyVKrs0S9RbMiTtcH070chnmr5Mxk8rjcOu7CJeldOMZqeRnwuUx0maJinlKGoaDDWZvrrebQh0cgn1oxMiDao9rqs4Kd84JxmIwJPvwTUKQ3Gh6bS1xFF-wL2LFG9MolQ2QhRhP0i4HSxZtKuJNEJOV_e3PVIVAGxvkzHe9JyjsfrjBMup3btJbxqW8UxFQYz8J8Nz0fJUCItJGg9lIMbCNdhhqyMn-4poQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vKXB16wxGTL80Qr6VJzPhHpJ7A67Vhrkfsq7M7fwegkz6EXxQgbWMWkWxF-0ESVBCsjXk7oixamS3qI0iiZpzYdv01G08aurwuzQ_FbfQKBeVT1qqh6jg57zUdlk1e9Jw-KtPJRpRNoxCCg5Q-9dfrXShYw7Z_jnlFgOc0Q2SPy9kfXHC61Rw9DILrNnjgtma4U6b5RplIBaHIfwQ8DxsVJO1nQQBvtnRo3It0w4Zt5FWqeY6GQ19liYxXyUaRcdSh1IYO5AsSSS2Pfv8WIjceHapWQvpdfnu1T3CmHV3HMFrwWXN8GR6KYKmrmU3wA39-O8FwQXMoJzLpv304IEMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GJsqek0flmiukt4Z9w86SwvdsQoPf0wHxDBrmZSuiBGGk2uKbia1uH0R2WlgdyaBgOlsW2UQz8b68KyKDpnIczQ_Q0xMW18-2-sbAPM92FSdPXR1UZiqKgWnFb1Q2dQ9S9uanwwozZBoIwUk3TASLxKyYHP3V-6L10HE2PzuRDW8COAcX5IhQXPNMmhTShEvCJ8Lau1NGAjvi-XTYi5bkaxR2uO-Wc9SPQ9hzuxgL-cSKZaQPmWWdq4-osRT69uk2e1vCruZHoGajKh_FSFR_YKAe28JZvaE6d6Izzf8hxqvHlx6l2ZBj8TatxWQEwr-HBWZLY4E7QdTQP0CsHBDzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌈
🏳️‍🌈
فران تورس با مارکوس یورنته رفته تعطیلات
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101816" target="_blank">📅 21:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101815">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEux3hSr_EyLFEDL3A8Z_Cekj9EORJmiIH7nUkmpeh84ChE7GYx8Vt0UbIrnkP7UETzBg36TKT49RxW9Dj2aGwi0CDgvphIL-1diMlwNWMkvn2WLdB6jDRCqgdLErTFFBF5Ya6ph_DMNA37m5olyy9BdLu71LiW8Tl_OSZLLO4GONKPgcGMtCUc8JILJv6JtzJTljV1_7qYe_1Zi8RIXewbc53DyNIv1Fq7qMm8qEGZRq9QKIwJirpchaWIIi2TTOX8GieaE6JxFeqOC11yWxiPoGC4x3cv8jU9H0FCeTp9JejoDklzlbO9ajOTMjNYT1sqoukY96cHQAbDYAgJrvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
کریستیانو رونالدو برای چهارمین سال متوالی پردرآمدترین ورزشکار سال ۲۰۲۶ معرفی شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101815" target="_blank">📅 21:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101814">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbhFBmq260arm3fEGDVcE0ASX5xKIVgqwTh9b4zcI2WjZAr8YKYqlD0ce_cF9Q9SpmLO8Nka7tPhWBlrN0Myn49mK-OS9cMRjXqHxxtqboll8ttCSX9BdhXfUY33H1QDvFdpD1uaYa41PsJiuBU8ES_AvKviigh9h0wVs-RLX8Pc_w1CsYnNrNNotLC0YiCtgFJpIUuvp08iKUXm0TFRlJuqVGmaKffoN2wgJdTmfgQQn0GGb5t5zl511JpxYsayWX3mlaCiHm35p-VSl5VyQgvGP-fc_F21XpM9yT8dWxZlIb1DMneABWmDKPx0rOU_PZsJN6GrZG_KHJW9THxa1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب امشب بارسلونا در بازی دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101814" target="_blank">📅 21:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101813">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3wsmScmC8GSoOd1umJuMyXs_IAoFkgVN2a8KvxZbPpjtwbaHM-_9Xa4ImnKUqRSEfFQoUfgRHBbTcImQG-7FZMqMJKZ7hXMPXG4dzEzpSVrUWwgSfth7ZPeqPmr0G9EHWxlWR8zNSkY_Vvrh7sQ1-DIwnNa3RiTEQsWtD3DEoLEBJS2xDgO9W-7NfIskcXe8wiYND7RyvO2b2pk7JLJGOoVUXh_yuvuoGL_MlNlAL4wiNO8CPNgmkDwPK1rexZnCsN7eCLM7d087a2M79Lc4KzWyngJu1VKJPNi-4x8Epi5JW2KiLUqW1q3xLTGwDnZY4QFXAJrN9lbxHYP3dZtQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
کریستین فالک:
‼️
بایرن مونیخ تابستون امسال مایکل اولیسه رو نمی‌فروشه و بررسی احتمال جدایی او به تابستون سال آینده موکول شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101813" target="_blank">📅 21:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101811">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qWN96zd9e-f4EDj-eq2KcxFj3S8VRosoActk10afebmAJHJi4dboBDktd7Yd89dFZPcHX3w0daS9q7KwmjyewzULnDug4HSm-0ueJG1bl2meA1aPZ-GT-BKZhEpAQjdvGIPEpf1UdLrGHoROmiP_wFmZQ7CteZ71cenomBp18pJQmF4rhpPmXhVWfL5xe03q-ScPK_iVrWPg46_bGox-T6idbauZYJcp3fpY7z4diUnWGIJO77JKC_u2dsLBuO-AOAMhSw5ylSX15tln1gJ26dytJ2H05j-2sm0o2ZjOKvpQq5C_dB9W8oXctajtz8_Z5bUxsOD3qQrBJG5IvyyDLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X4jUlj0SQCda3FQNcScC1W-xtJxYpNv3Rss0Lz3Wyw_Y2DXX7qMEVkUjCMYHYRo3q_SY0f0zaiZY4Oy19ognjlwVzYkam2QSODUR2dp4gaPjFZ_RKB-q4RneVnGnk7wFBhNQkbhkH44Oa3WXU-lzRumc9KpvMkhro2kHahmxycwPAXdWXjqYiRLynB-K1X1bjoZW3OHdIbGeyU8QxiZro6SC9YzhdVXEgB1n73EsSvAXa2hW_WSjRQtbXaLdBGuPKYFXhcJpXL2H4u6-2N-65L3ahsWR5KXzN7NmEZ1kfN6r7mqo5itubLLVAKLBxzC6J1ZchncTI6te-fO6aldR2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
💎
۹۱۵ روز پیش، پائو کوبارسی اولین بازی خود را برای بارسلونا انجام داد؛ در حالی که تنها ۱۶ سال داشت. حالا او قهرمان جهان است و ۵ جام با بارسلونا کسب کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101811" target="_blank">📅 21:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101810">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a142d4e6b9.mp4?token=H3CthBqaGswDpp9FkooNarwxMHd1P_iOVzwo7odUKn0I5TMQenNtkq52IVlw3zrHnKok6spXh6zavF0mW-L__TVWegJgtDfBbqgSGqFIM42eK5Z46nyq9N7V13ALyGyMusE--F_WfckgTddFjewj65Y_BNFS2vAvk5L9j59360Hv35nGlwpfhoXaqLG60wN2etOBqog18pWrDLBKTuV8NE6USO8PuW28X3H-bx3EZQxsHDO6SQ7ZheeCaawfGSYq41uNwqBPCrX57zoexxYUSbXs9H5u5wexbzmGF3yFx38Y6r0C_QcHLHJgBaF8Jta-AnHAFK9NDjhxM_qDwim1_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a142d4e6b9.mp4?token=H3CthBqaGswDpp9FkooNarwxMHd1P_iOVzwo7odUKn0I5TMQenNtkq52IVlw3zrHnKok6spXh6zavF0mW-L__TVWegJgtDfBbqgSGqFIM42eK5Z46nyq9N7V13ALyGyMusE--F_WfckgTddFjewj65Y_BNFS2vAvk5L9j59360Hv35nGlwpfhoXaqLG60wN2etOBqog18pWrDLBKTuV8NE6USO8PuW28X3H-bx3EZQxsHDO6SQ7ZheeCaawfGSYq41uNwqBPCrX57zoexxYUSbXs9H5u5wexbzmGF3yFx38Y6r0C_QcHLHJgBaF8Jta-AnHAFK9NDjhxM_qDwim1_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیرس مورگان:
چرا نمیخوای ازدواج کنی؟
❌
🔻
زلاتان ابراهیموویچ:
چون دوست ندارم 50 درصد از ثروتم رو از دست بدم.
💀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101810" target="_blank">📅 21:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101809">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euCNY-lNNS7xn0eljc7imZXE-w2NH26cWJbGEi-QnDjRvuhImtBp-AVtPVTJVhdE4kfntyYmXxkUmc-1CkaVc5eEoB9inw02dD6ZhPi2pj-2B4QbesUaZP8Z1K0t1CW-NPseaYEq3cepU1elpjXcV-T7k0Kix5aEvbrkwJJNTpF6J3fyXZPHalV_cfDpJwRMs-oXiZSea8stsUN1xGt9YW_hcNNthLVxMQ_sfZZ8er5XVO_FthTjZVfSNXvmfTA4sSs2utOC2zro0kRCi-7h2rhjytXyrviF218afFX8osAQyB5jjcgGi7OescU3oYGjxg6dkbJkvs--1X2d_jgmjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
🚨
فوووووری اکبر عبدی بازیگر سال‌های متمادی ایران به دلیل بیماری قلبی در سال ۶۶ سالگی درگذشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101809" target="_blank">📅 21:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101808">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwxgWjgkgr9xuw87OzQxUMfadcga7UksRFgaXu60ZW-_-YWDngYr2ze3g_dBhR4aDUR1RhXyAlrz38m7wM4QjvF7cH49Jb25g-gOtjhFTUaCLXBqwSWjUDB3EvYYAVaehi9cqD77wAM1gc3RW-bBd5tplfQL8pDNpnRyt_-ZsOw1gjJegf5L6yvNhwAh04WaQuf0lmzN2dhb3ynj40Lgy4w6cgGSsv5nn6-YI2GuYYPToQllAgqhF67TBFfGlq_GAsgzKvQSmnKnXwf4d3YCOA0lRBIOucmo0Kgw2jbX68DkEQzNhErwpCYRBrWGpnQatTycZcxGIR4UkuMyAbGvug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
کریستیانو رونالدو تنها بازیکن تاریخ فوتبال است که در ۴ سال تقویمی مختلف، میانگین بیش از ۱ گل در هر بازی را ثبت کرده است.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101808" target="_blank">📅 21:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101806">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZXiJ7ZJiS2KhB3shdLUZ3FxeTbHfU61clTwrxOgzXYggTCCdSuwiVnuF05cuNfp9M1Tb89FJ6qfbyZhLg4VIbchUgZyx4Hfs51E71p6vddVD5RMKzH18szM5vSxhkE52FeHzUDnwr5qTWUd4BLTYmWzsS8aWDmG2PPdCn4ouiX5bgEZlTyE_wQp7ednZHNv4ZcA1rnhcyxxODeTvYqfaDID2j_0WbjSkrMYC2KkK0ROYbCoZdMPlzyFOe1MPPFdbOu7_oiLBawCJin2bXCCsy84I1Xm189JzaYHwx1CdZ9T2H0EkOnTkCChadBY_wTF8fYhFoREY5sHkjkcCnbuww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a81621b4.mp4?token=Bkoi2REqCarFi0ztyHccuCTC4ENq3dmW-1hA0VGUY11JQF50muD3koDnDeOZRy2O1TNbl-BVFJk2mF5tqeFK6eMK6lRtYLux8a1JJlYzlraKlpuDJb2Z1WDc8faD-LEdG6D91kfUjOOA8_JyjYxKecFAkKe5EWoY7FjW-sATH3sc3eUljN-dDMtvRgRQxK2BeZHvXP0NQCVJDoGxO2OffeQ4QsghWybZ_LzhEBIR6_UQ98MfxzqX3PhIuLNMFkYSaR3BiaHrCILr7bYt-0amlL-C8Dc2xOXDklS39CQSndYDgqpsKAC4wy2S-5XzxZe5kvLGUasBb_dr4-iQVCXqHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a81621b4.mp4?token=Bkoi2REqCarFi0ztyHccuCTC4ENq3dmW-1hA0VGUY11JQF50muD3koDnDeOZRy2O1TNbl-BVFJk2mF5tqeFK6eMK6lRtYLux8a1JJlYzlraKlpuDJb2Z1WDc8faD-LEdG6D91kfUjOOA8_JyjYxKecFAkKe5EWoY7FjW-sATH3sc3eUljN-dDMtvRgRQxK2BeZHvXP0NQCVJDoGxO2OffeQ4QsghWybZ_LzhEBIR6_UQ98MfxzqX3PhIuLNMFkYSaR3BiaHrCILr7bYt-0amlL-C8Dc2xOXDklS39CQSndYDgqpsKAC4wy2S-5XzxZe5kvLGUasBb_dr4-iQVCXqHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تونی کروس، هافبک سابق رئال مادرید، بالاخره درباره توییت «فوتبال برنده شد» که پس از قهرمانی اسپانیا مقابل آرژانتین در فینال جام جهانی منتشر کرده بود، توضیح داد
.
🔺
دیدم که خیلی‌ها از آن توییت خوششان نیامد، اما همچنان پای حرفم هستم. به نظر من، یک تیم واقعی فوتبال روز یکشنبه برنده شد. همچنین معتقدم هر کسی جام جهانی را تماشا کرده باشد، دیده که اسپانیا بهترین تیم تورنمنت بود و آرژانتین نه‌تنها شایسته قهرمانی، بلکه حتی شایسته رسیدن به فینال هم نبود.
🔺
به‌خصوص مقابل انگلیس، بازی خوبی ارائه ندادند. آن‌ها بیشتر مسابقاتشان را به‌خاطر قضاوت‌های جانبدارانه داوران و فوتبالی که مدام با خطا روی حریف همراه بود، بردند. به همین دلیل از قهرمانی اسپانیا در فینال خوشحال شدم و همان باعث شد آن توییت را منتشر کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101806" target="_blank">📅 20:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101805">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdetRpkX-IaULYBaMFuhqaCQrzGyOgx71P8vAF564fuB2P9kHWikff9Sg9L0TKiSQHHnrsFgAqjoPFRT8oGo2qoubM8qIFXhQnSOUFrkJs-iKvrfwSmbvYOWz6OSequ19uwYdzkWUBG6dYRuZZIwa3Qs_tSLbKzKOMXap3NDFEDrRApzapZ5r7H1rM8ZZt-M1lSc08axc_gC7pDJ_1Xd-DYw8jILdR_kwYNp7cdD4UpPZ4KLUgrvQknfjE8-4c0RU7rKFI-gbbWSInSmO3iac4e7jEwkr20AUI3b6lKd6dwYn-gNn0CVyl29zT2--K7K0whweV-fpjaKgz-IG9Z0jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لیساندرو مارتینز درباره کسایی که از شکست آرژانتین خوشحال شدن:
سقوط بزرگان همیشه باعث خوشحالی افراد معمولی بوده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101805" target="_blank">📅 20:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101804">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpImD531ym9jpkB9QMNCA9CfFX3SUQS1ZvvvzQPPNragmer-tZbz4OstlRfP__thLUc6qr7OpcKTLMEvWkHzQ_fJJ47VzbW-LuoM2Ih6GELHn9gGOe6dJxcZCv2voW7eRvjOA_A39vry8ZrEvPCtz9lRrDttFO5RkB_ptQskb_4lEziyPjZMTf-HUIlcvvle7C1S9PtuI_5SrzVaLpICb6SfgHvG0_AVPFT9d1zt6BUbFVx1eAcv6fYrf8BiHI1wsXh_KQnrIQjwcUjnpTbudAt4Y_XZXXpCsOxlT4viu_onxYb6OGsNonUTKSVUUxcWW9nuFJ97dt-q8ncYKK2A8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
اسپورت:
فِران تورس از شرایطش در بارسلونا ناراضی است و تردیدها درباره آینده‌اش، احتمال جدایی او را بیشتر کرده. او احساس میکند هیچ‌وقت گزینه اول تیم نبوده و باشگاه ارزش واقعی‌اش را ندانسته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101804" target="_blank">📅 20:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101802">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RkcUSJPywdAajBVBt0LBGKpnOslQw3d2gWhJm3y92NN-9-PTTkeknTkfoVfWgLKU1SquYO6OsiL8LxzU5T4xxBx3I5CMVixtAr8it2UDFP5KWoXEJ7XIbv4kpIYp72JgIMr3MzhJF63SyeCeOJlVdpyibrzXN_upGHIAgSDrDvXyneHnd97owWuVIaZ5epd01EBWUP3cMpzhqUIcF59fj2DRg1CaTnnRewWk2lfJkl21-ZqZ07r_4uLCr3u8TdzgZTTJ79NB5ZcvaAKN5O5AjxiT0YCOItkk5YFdCxLvoZf1qRgdGeL0v3IKKN4T6cwl9OyDrRGdN34Ymsm-_tmFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X9SLn0myP8JiKbG_qF6fA2GYEhc8tbKS6tsQUyjwYIR5cyc-haf34YY2vJ4UqetMP--abVcZenk9WKMKVVLPsuREAGoR59WCpWpsGFsf23ZJpkBxcZgX1c-5qL6_gzqiC-s6WL5AM4-wfD09mJSjnjNZUOsbZ_bsYfrFIJe3brTe7r-tCcfND0Fp6qeNPitR9zEXQkUjE1lejdRMNvWJ3NTagb0qXNLwBxH508Ilt9dDqAJbTD0hWwoIqygFXb2giPWc5e2W9OD1Jrm6KD7NCWuhgNRcTAAYwoMhER7VfUxZUDaCz9MVQNa1n-lsURc8E_D3WbNav39ROEm_MrJnfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بدن سکسی‌ای که فرناندو تورس ساخته.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101802" target="_blank">📅 20:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101801">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FajfY-5QDaz6m6yY6s06MIWWPtxh5fFdI_FC0dnRIDusHz8tvIx-N3DEdi4bU6kqhqkGd8i07j9bLFjVkvrHa0QvUJgfE-sS6dzqOSIA0-GbE48EvZwPWWErd-dj8XseV5Y7dy1hnGFEq45m0R5cEaat1_9AjPFZWJLoIXSvpfoDbVijCXt9dB0rXajzQ901hapfpwfRCXlB5cb4hK-w91Zss0sMjUkvvq9698ZyLMSJjF-Sgouu41l2JStXBY7dGK7UcCTeLc2j8jrhemTDRXseJY6c0us99sHeSteQqHQJUUEipBPFXo7vnRTfMvMbpOHVE_HonfjD-zjMS8M06Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
لیونل مسی در چندین بخش آماری بهترین بازیکن جام جهانی بود:
⚔️
بیشترین دوئل موفق: 60
🎯
بیشترین دریبل موفق: 28
🅰️
بیشترین موقعیت‌سازی: 25
🎯
بیشترین سانتر دقیق: 20
🥵
بیشترین خطای گرفته‌شده: 20
🚀
بیشترین شوت از خارج محوطه: 18
همه این آمارها در ۳۹ سالگی!
🐐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101801" target="_blank">📅 20:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101800">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYoeN-9h9KLX8z72DC9XwKCPZUd5dgRgLvpO-nyXSUvpUd8ynbutZiEBIukOPdb_F1bsGG7KZEw0aJaTbgf8V1gba6HehzbawAa36zCMDqjLEjOOOHwZJ0F_RlLUayYAQnloAQk9VoRG_iqI-PRegvmCj2fg_aCIIBaLUH1eXog_h39DmcvJ9P5cwbiDv_LHX5v9DA0XWPIg0DL-_mvBWdiKwZudLrxiTXt766zuQBs6ANykRQU7l1yM6aZJ5WSPlCjsHHKcp9eV6NBmdx8vw9rLeo_RvksEYOf_rmvvmEm8jtFv3DMxzaT_o4iP9NcOsJlNiSKArhJkdneBT20ftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
✅
الاهلی مصر اعلام کرد که روز ۱۹ آگوست در جام خوان‌گمپر به مصاف بارسلونا میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101800" target="_blank">📅 19:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101799">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inyytEv8kLZ4_jCfvkSSPN9hXbyply1iosY8nC6KLdibkD8Ufe61im-DR0MInCKEQCjCZ3evd4bUkeqmwuTBqhxydjXsI1yeYLvN4e7Onmz6q1b_jsv2XfGG1Q76s9Tw2etMwXQAvjoFTmuasDJd9LE8T3cb9cbRDobFW81AjUe5L8UsfqOwa-hWQnGjFv8HS4t3IF2dWaGs9hPxqgRiaw4_H6fBimUihTvDjGCgGK1DMobOKngh3gB9Hs8EUHym-gxl_u9HD-e--sXWJMNaGUzMQdfObjyLXIi1tk8goKnB049dkEfaPWnSIIqhI5EAzegfywfGcu1cGSNjnJMWeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
لئاندرو پاردس فقط ۵ روز بعد از بازی در فینال جام جهانی، با بازوبند کاپیتانی بوکا جونیورز در کوپا سودآمریکانا به میدان رفت! هافبک آرژانتینی از ابتدا بازی کرد، ۹۰ دقیقه کامل در زمین بود و حتی پاس گل پیروزی‌بخش تیمش را هم ثبت کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/101799" target="_blank">📅 19:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101798">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PC_J6gGFX9scfc6dFd0AW5e1Q7gg4tL34dY8Kcn58gPrVZAmmuwnd1hftbMADkPRy5Vd7NzAKxIpRBi6YB-O8ikEdiEOkdZ-W_GRjyUF47W4BLnjQpW6KGzG6plg-eLFAhBxX2JF0KzI-cZHAhOSGW03tIPbs9FYOmbGoarxa9uu_T5AeVBK2ahAhI8Ztu058yirLfptMVgtpYs1iTYrT1KcYL7sxvvZXEiJ90D2WZ5RBYegkhievykP7ygTTibn2LT5g9Eku97wp9vZBq-IypU_jJq4nEqJtBVqeMLF9JDLBwZhdJRZmen2Lu8txclLmmF_B5fyxcnEP2s5xueQTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
فابريزيو رومانو: پیرلو به تیم ملی ایتالیا 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101798" target="_blank">📅 19:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101797">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGotLQSyOfkqnNoUMEvUoM_raBjMJapylDhu-CLfLFV4aq54TzIK7DzoyFA_frkveJ8ny0_7Ni4ux7UcoNpLHJ9zEU2P-udpDM8W-xGcbH0-4AUR8C-saIsP5JII8MRBsH6ATA88CHWJstLZHZ9SMIbZIcMABRtgdYiYhhE2_kTFr6Efl5M8WoF129jXjcdkCMd7QPdxMQrabjoVkRM3J2mSGNeKnqYqO9jJTOmVaWWrNt-TZrp_GzZpd4j6vwT3sfIqVSOzrVe9XNvO-frarI0NPmMMmDpW3jLRQn7VvKbrl4MJkNzYCivMHyFmKolB_9ft0l-AmOq_Cj5fu5GcOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بالاترین امتیاز ثبت‌شده توسط بازیکنان لالیگا در هر فصل از ۲۰۰۹/۱۰ تا امروز (با حداقل ۳۰ بازی):
2025/26
🇪🇸
لامین یامال — 8.23
2024/25
🇪🇸
لامین یامال — 8.01
2023/24
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگام — 7.81
2022/23
🇫🇷
آنتوان گریزمان — 7.69
2021/22
🇫🇷
کریم بنزما — 7.69
2020/21
🇦🇷
لیونل مسی — 8.52
2019/20
🇦🇷
لیونل مسی — 8.71
2018/19
🇦🇷
لیونل مسی — 8.48
2017/18
🇦🇷
لیونل مسی — 8.68
2016/17
🇧🇷
نیمار — 8.52
2015/16
🇦🇷
لیونل مسی — 8.46
2014/15
🇦🇷
لیونل مسی — 8.84
2013/14
🇦🇷
لیونل مسی — 8.34
2012/13
🇦🇷
لیونل مسی — 8.83
2011/12
🇦🇷
لیونل مسی — 8.88
2010/11
🇦🇷
لیونل مسی — 8.76
2009/10
🇦🇷
لیونل مسی — 8.65
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/101797" target="_blank">📅 19:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101796">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVQHCcx78PpN6lotQPJM11Hp_aPNe9kJGsi1yxqwGUsEYiSgqUWCwyQkrH7XOLLmasmgRYI2aOi1igpygeBG8LQX5S7x8cMoSuGeAGBHh0Ac_3jiWfom7Ffx_JOk1LT5d2YER9kJl8wrjPnczIUz6o8lu3l1UwoNd9N3zNmQrmrSRDzH0bxPSpsGJyII4qZ0RWGDgvX9ix_mF--TLalgotRmPhBqGl0PNnO6GoIrnBquxAqTXZGc5PnFs4O6pm3SWjc-7qVbDOGJ-5FiiL7vNzmuyKUlLM1NkaqbkYasf69UMINz0xaEc-_rQ0RB6d1QZzsD7BKyBEDCZwNx_be5eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💀
مثلث‌خط حمله فصل بعد بارسلونا: GAY
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101796" target="_blank">📅 19:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101795">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrDyMCxWa_MXZ32hykJ3kGDrLWXHGOUeIZlhXbQki0rrBXTixQbgq9IEtlr_lfUN9iYg3KAJaXnmnMh-fpvjISR2QUSULRv6f0dSbcHF33gUgZgIbz-iDhcFLR6DH7i1aMm5P_jWEXNNIIOBa454Z2Tq7fHqPaJl11ULO-V6vGRaakt7KeTSMTHuo6kTC1jHc3Oihibw58WHcKtOHEYlejBnFewcTwpCSo77tEL9wMRJG0YsKTu1Sdhystl1r1vtCnv6ZzBFnoCUxFnz91A5SIXh-Xo50itJY9Rql88SmtC9xu6lncI4-Uf8tfhSkFuUc5v9imiiOF_gLdnIzqT0jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
⚽️
بیشترین دستمزد هفتگی در سیتیزن‌ها.
💰
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101795" target="_blank">📅 18:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101794">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1da4d2bb8.mp4?token=pOq796Rh80xnJeArCobaPZhNobOP7uZpOKANCReScw2_J47PqoeDPjen8TPPT_DnbB2H-1KO5P1epbbNuk5f9WUTsZV7vneapyiuIAVIIsUTGuPDuMrNYLH5oj1R3DMF1vsPXgo9fDLnrmXJNxWOpA8AkXyEoqjk7CJK-V_XaGxNTxWy1hc-Ot6KeBvrCR_cZxeOIoKl8Hy4kw8jIP9oqMo9-a1m2W06XJo7SLeVwUVClcCaLM0daeLLRF6n2u2O0mqZ3LV9ORNIb0gu-L5-j9RPzGj7qmgQPTXX2g9BRKCZ3H3_RmQRMTbk9P8pP338dvS2P9iJ4u4lm-FafLeyc2g5ULSZ_xvSJ3WGvJThB4eUPchVlR8LK9PEakV74iaHRntQVFB6AM6A3pjDXbuOQ66ONMtb5hfRN6oJSPOlXrXIITaS2iEKLAN2o5aDrtyTBvjetghk6FL44q45U0otP4bvoaqPHlutrUgPv-UnlLJFBaBQr_QiGbgZksAlj9kqVCAsSSovN7cDR4aKqZeVHnDNULq5SY8XD6yoRs9cgsfTHL96toe_022CRN7F1SJUjSbTI2rXkZ6BJ-ho1Ip1-rVX0fTXcRG2u-byoBQMm1VYfdMNK5yFKWMAbvwjDzulFh7NAnIHu_hNndcQ_SAqRYrEV0kTk0QFnKjjETQbtNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1da4d2bb8.mp4?token=pOq796Rh80xnJeArCobaPZhNobOP7uZpOKANCReScw2_J47PqoeDPjen8TPPT_DnbB2H-1KO5P1epbbNuk5f9WUTsZV7vneapyiuIAVIIsUTGuPDuMrNYLH5oj1R3DMF1vsPXgo9fDLnrmXJNxWOpA8AkXyEoqjk7CJK-V_XaGxNTxWy1hc-Ot6KeBvrCR_cZxeOIoKl8Hy4kw8jIP9oqMo9-a1m2W06XJo7SLeVwUVClcCaLM0daeLLRF6n2u2O0mqZ3LV9ORNIb0gu-L5-j9RPzGj7qmgQPTXX2g9BRKCZ3H3_RmQRMTbk9P8pP338dvS2P9iJ4u4lm-FafLeyc2g5ULSZ_xvSJ3WGvJThB4eUPchVlR8LK9PEakV74iaHRntQVFB6AM6A3pjDXbuOQ66ONMtb5hfRN6oJSPOlXrXIITaS2iEKLAN2o5aDrtyTBvjetghk6FL44q45U0otP4bvoaqPHlutrUgPv-UnlLJFBaBQr_QiGbgZksAlj9kqVCAsSSovN7cDR4aKqZeVHnDNULq5SY8XD6yoRs9cgsfTHL96toe_022CRN7F1SJUjSbTI2rXkZ6BJ-ho1Ip1-rVX0fTXcRG2u-byoBQMm1VYfdMNK5yFKWMAbvwjDzulFh7NAnIHu_hNndcQ_SAqRYrEV0kTk0QFnKjjETQbtNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
▶️
اشرف‌حکیمی و امباپه در کنسرت بد‌بانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101794" target="_blank">📅 18:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101793">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b632e2b27.mp4?token=l4vh2cTPdYkcSNqoRql7WBLFiJ9PVr4UA7CnglN5IxzxRxvAkEGwSQ_Fooq7fbWvoJxoLUwcC4OCrgUdgTMqgEXxrxWJ9ES-9AV4tOuOvZoIgGrSOnPw3HvMCcjHz78Uykc3GJryM3IRCyt6YTGAuyisNwkTauaZG_Gv-hvM2u3UpqtgbSBmy_bnz0p3s88AJnoh7bxleBB2iDOplOSgyH-G59PUlU-fjZ1I9ER2pYEgP6cON3MPCa4u3oCtMaKKPYpKEjhHlWdq3uCq_plMNUoZPMG5Mk97XknHkgn9VQPA-0ApO2wi19kBZOULnLmnZervfrWSt0HGawHEvbOJyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b632e2b27.mp4?token=l4vh2cTPdYkcSNqoRql7WBLFiJ9PVr4UA7CnglN5IxzxRxvAkEGwSQ_Fooq7fbWvoJxoLUwcC4OCrgUdgTMqgEXxrxWJ9ES-9AV4tOuOvZoIgGrSOnPw3HvMCcjHz78Uykc3GJryM3IRCyt6YTGAuyisNwkTauaZG_Gv-hvM2u3UpqtgbSBmy_bnz0p3s88AJnoh7bxleBB2iDOplOSgyH-G59PUlU-fjZ1I9ER2pYEgP6cON3MPCa4u3oCtMaKKPYpKEjhHlWdq3uCq_plMNUoZPMG5Mk97XknHkgn9VQPA-0ApO2wi19kBZOULnLmnZervfrWSt0HGawHEvbOJyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسی همه چیش بهترینه، حتی میم‌ شدنش.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101793" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101792">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e74ccace70.mp4?token=d4EVW9-I23FNzzx5qKU2lA7-gBnvkbKtArYroSytc5ouHntWB7EA6wvf6BeYnGzrPoRSU6YRtppAHXX0ROEiR5VhE07pA626Y35rEMuY0PPb8cDoY7RzxqCVLpPVpiLTVukf6zkq6qGy1OtkQ9tANoz3Qtg_vPFpXKaSTpwCpicA_xHCtF9K0LrkCdAsM7B11Ei8j4D-QzHUAJAVHrgXq25t-_5jqAL9UXaFb69Xue85yOmg33Bt_rUHzGVmzPzzgyWjYq7K20IACkNSP0NTJ6fg6rt1qV3BroRPCSPYXIXKarkSe39ILnvUjlA1LZosAIayY2dY9pNhkJCfOEB1JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e74ccace70.mp4?token=d4EVW9-I23FNzzx5qKU2lA7-gBnvkbKtArYroSytc5ouHntWB7EA6wvf6BeYnGzrPoRSU6YRtppAHXX0ROEiR5VhE07pA626Y35rEMuY0PPb8cDoY7RzxqCVLpPVpiLTVukf6zkq6qGy1OtkQ9tANoz3Qtg_vPFpXKaSTpwCpicA_xHCtF9K0LrkCdAsM7B11Ei8j4D-QzHUAJAVHrgXq25t-_5jqAL9UXaFb69Xue85yOmg33Bt_rUHzGVmzPzzgyWjYq7K20IACkNSP0NTJ6fg6rt1qV3BroRPCSPYXIXKarkSe39ILnvUjlA1LZosAIayY2dY9pNhkJCfOEB1JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🇮🇷
عباس‌عراقچی وزیر خارجه پزشکیان: توافق با آمریکا بهترین توافق ممکن بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101792" target="_blank">📅 18:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101791">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYT-e6E-u-MQjy5jlesN6aYjZUy7UV7dLQpMyZfNtlAiikbDHp1BDBrnt4WT8pD2SjnCK3Ezxtg3T0iB2S48B6gZ8PjuSV2Z9yRz7curEit_doV1m_FWcUZoAorl_B6A86fjyO6VzcuYshyVj1tuy2-XST8_xPwDjU1qFG3U6KEdakusTuD24iFwRJ5sCR0gth06buRh3WOkxjA1aiboyWbDebDijPWp5dcbru8lHjtqlas87rOldCwYxBPwhcAAIvr5k3AytPy8U_L4h8uXE7-9u2nHMupPXJS-EhsOtwppPJK69OmalaQHp3d6u4l1O8dQCeBrIVQ2fEGhbZkKFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
💣
💣
💣
💣
💣
🇪🇸
خبر فوری: فلوریان پلتنبرگ: رودری اکنون به طور رسمی یکی از مهم‌ترین اهداف فلورنتینو پِرز در بازار نقل و انتقالات است. مذاکرات با نمایندگان این بازیکن آغاز شده و پِرز با این انتقال موافقت کرده است.
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101791" target="_blank">📅 17:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101790">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👀
یک استعداد دیگه در کارخانه لاماسیا درحال ساخته شدنه؛ سال‌ها بعد اسمشو قراره زیاد بشنوید..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101790" target="_blank">📅 17:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101789">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeTRckbG8rf501Apoe_jADIbMkPG5k6Jua-PY-EnkCDOs6HHk6CY3qoCpZ6zYHWE7IJldiBkxwDrOBqKEBPVE9ir_22wb7uAsYlivdRCyv7Ihfz5Sx3gkHavJFG9K7yvH10AzPG3IBO-cerMq2qk6XjtFiEd6U0A7Il1TM5au_ehYPJzeWyYrYuCcbA_wyt5CuLYkyskDcrhieguou3z9mWveARJwh7NtqjHNMKAyye2zDYYa02617uDVw9Chqp7vPovzDkvp30PgPoNKoE41i6ToDuvIW3TMfVIGGw_6_RriLu9y1BmOY5Yacux49jszUU-BDREAPFQ3JYA90PDeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
✅
رئال‌مادرید به رودری اعلام کرده که مشکلی با عمل جراحی مربوط به مصدومیت غضروفی این بازیکن و غیبت برای چند هفته ندارد و تصمیم نهایی برای عقد قرارداد به این بازیکن واگذار شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101789" target="_blank">📅 17:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101787">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vFu2W1LxLl_tyNaYbEjhCnmc_PvM5h1NNvzARypqy6mlPA8uBJ-8Ea1eZ6Sa5WJUVqxL8ofGUVAXgjE7CR2mZFlHo2UUweNy0gIB0UOYWR2B2QZTkN-8pd94OS5sRqcwrzlmclHfAFRQa7MmBbL9_10KVcn0_xCjgeDQRrFf7R0A70KpDd8i6-Pn9A41GWMWHsTFXf707klsOGlXD9i1c5BMKJFIfyNvkCZiTWRbpzxvz_9oH5mdiUgOf_zE6G3SPJ2Uzj_iCxI7VbmXzu3HWGSkr-ZU6HtiM2BjBMM1DzRkicZkDlEN2DVDJ4kUF4QRK-CbJVjQ6yRW3mQ1AluPIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CkoJAMfWh5xPhnb598VPbSoK83FjceEZ24DUhknybM2SbCKIy-I2QTzl-NiKiWXoyMrZ-031Iq7CxhI5Ob4Ca8hLtBUozG3AWQUzz53wNTfrMGXzKdTa1W68mfuMnEAz-KKlZKmODGkDNpSJKPNAlijw6QFKs1LFYsQA4KO3wmm8FRSzEpv1rn35BtvjukG7lu6zYchX3-u0bexxeyRP6fCH5dun7bLfPVApRw_35q7py0R4_1JT1u_x0HO_aJk3VWtiM1L2m61uded5wcxr57ykzObnZWLGnxoHgIGzQW4_l7H14inGwjw_84qn9gxT5iLCVvEHtUe5nctUZtw4zQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
مشکوک به نظر میرسی هالندعلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101787" target="_blank">📅 17:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101786">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzLDowtEaEwmYu3s6WFGqSZfioBM-EK6Cx7NMSri2YxyoBPqrWV6E9bXkM3oWdc7Ik2cGsWSUb1_bwFz3gLHLEqEXYPSjQtIF444adA_CgBBEtakfQWXiDSIvK6N8RprY2v6gSwKUb-pIS3hIyXqXv3OoJi2nxOOcitCz4DDnTsZNRQQMcacAEfKlCGV0vtZgEiL9cZX2y-q2Dcn6NhSBlyimeAzOBVJxb4mEgFxTNsG0--VHSj0hqjqh1QYNFPVC82c8NYJziPfd2ilLDlpzt-i6y35f8A0l1IqS7JBwXLDCXC4GZvI_8ItS9OIL3yhTRs24QfxSeZugBdJSzviag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اسپورت: منچسترسیتی با توجه به شایعات جدایی رودری، مارک‌برنال ستاره جوان بارسلونا رو زیر نظر گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101786" target="_blank">📅 17:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101785">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
⭕️
🔵
براساس شایعات منتشر شده، قرار است یاسر‌آسانی تا فردا به تهران برگردد و در تمرینات استقلال حاضر شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101785" target="_blank">📅 17:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101784">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnoKGlEEvvZ5NJFspNoAQjhWZrDLmQ0UtXD8-pauxgeiwt3bOBCyD-ju3orc08yW7d3AL5Z4ZUG7mCry7MK_7etdT9Z5raYcVxQGVM8ovKWp-VN2CaSVKbwwTQ-grSdo_OX2YImWoKwx3LquG2v_yyG-lQiqPhOljFqpuQPF1-lrOs9cZk-zvXGIVsYOXSnVL2e5Ov4uq7W5XYlUWO9AFzsCsjZsVmo9eHBOGM5zxqHEfm2-bCI0EK22v6rMX-H6tGxj7hQBoRzBeIsTGoy3JsaQ22wGIkBZlY-tzp2DGDYZpV91kJPX9YOM1RqYwFlL6N9tRMRSUKBHnLJTxvfx5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇹
✔️
به نقل از گاتزتا دلواسپورت، آندره‌آ پیرلو سرمربی جدید تیم ملی ایتالیا خواهد بود و این قرارداد به زودی نهایی می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101784" target="_blank">📅 17:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101783">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1ed1b860.mp4?token=J4QWih09MHfgPTyYr-n9u9BKOZMSTHSIYTeOrZ9HIc6CS6Kg6pJ5DmQp-rLjDKfNhlefaAXW4WwTLkn7-oE1nMySypOzKlLbJ3kIIXPhCTzrqDtkb2Od_sV9VQVPkwWF-wq4qK-DLU4id1FLsyhcPgpWRwoNEjtQk6UFWrWCMLDoi9hyIynjlA1i4oWlNM_7A0MpprLRG5jLBogHpBQKqro-GAm3rVqKbIbDh8PdiJv2dn9TKa2nGq7FlreaM_sm_x8B6ZObctOAZHUJGo3TVX7gWoASXR5wKlafqjTbuT7IN9s0hT6oaVPXJClWY5tB0J9faN4VebO5u5eDsQZ1aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1ed1b860.mp4?token=J4QWih09MHfgPTyYr-n9u9BKOZMSTHSIYTeOrZ9HIc6CS6Kg6pJ5DmQp-rLjDKfNhlefaAXW4WwTLkn7-oE1nMySypOzKlLbJ3kIIXPhCTzrqDtkb2Od_sV9VQVPkwWF-wq4qK-DLU4id1FLsyhcPgpWRwoNEjtQk6UFWrWCMLDoi9hyIynjlA1i4oWlNM_7A0MpprLRG5jLBogHpBQKqro-GAm3rVqKbIbDh8PdiJv2dn9TKa2nGq7FlreaM_sm_x8B6ZObctOAZHUJGo3TVX7gWoASXR5wKlafqjTbuT7IN9s0hT6oaVPXJClWY5tB0J9faN4VebO5u5eDsQZ1aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مهدی‌قایدی ستاره تیم‌ملی ایران: اگر میخواید عاقبت بخیر بشید، بچه‌دار بشید
😔
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101783" target="_blank">📅 16:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101781">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTBsOkQ3od8OpQnPP1ReSA57N_P4zA3cvX6E4_47rWgDICUfeLa7aJrbZNsGNP7IhEFkjc2m8YI0jyblU7GZ5ZEPEYJNP67esFSiLH80IQQoxE8xh_Lu62c7a758Bchakh0hSIhSjnsHWm9nlPtfhXKhn07a7U5gPF8p-dkmHqbMgzJP1MxvIhzXl3H6-XpB6D_qyLdKjwvKBhG9MjOILTj9d76UC9INFTLOLEXx_G9Z-xp7uXZQOVx039tgOrkVF1wx7ykvg1fu0v-T672sw-ebn9nPQZ9toxoRE87TdmSDX3YXe8s93BW-SSExcOmEJetoy7j2XXHRt4I-6C37WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avuIHVUerGqT3mSBMqqFQ2qNcGXUK0jQ9y8RZ-cE2Ml-6M3feHXBNZoN6SRInCGz8gouE5OFDMdbXrG9w-wWwx39akZszjcEWwcmkW5wC7AcwNEwsR8tDIj2G71UDUnFbPWO2wsSWnU1H-9SXlENDSFZHtHwOiJnVxAYtz7JjljRF_wpuJ1LNu4wN2S4OHP7ZKGB_Nl9-K0ifnC5fPgxg7TMiqheqrFqgEKX7TAEmeK9QcfMtbpq6RO3mujyzDWIg-BTgCm-6Jy_Ygyxohmt0hSV5wWQEovHjw-gAhrGSnY1a_tpJrCWB04ESEQ2ssMrFZtIddTqQbsWPiSImF9zow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
⚪️
امروز، ۲۶ سال از جنجالی‌ترین انتقال تاریخ فوتبال می‌گذرد؛ لوئیس فیگو، کاپیتان و ستاره بارسلونا، با فعال شدن بند فسخ ۶۲ میلیون یورویی‌اش توسط فلورنتینو پرز راهی رئال مادرید شد. این انتقال رکورد جهان را شکست و بازگشت او به نیوکمپ با استقبال شدید هواداران بارسا، از جمله پرتاب سرِ خوک به سمتش، همراه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101781" target="_blank">📅 16:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101780">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_znP4s3fCsr8s_6r2faaC_mmBR0FXME12_t241SZqZt_pu_sJsbjSnj9YDPpF5IkiyH2zcB9KKFQSNBJuml_3F1iS4TtA2zm8N9av1qIE2atdhMYdydyrSe4W8lZV3cYfTB7Yh6Vck8ymMX1rPutlc7r9ujZ_MSc9762d0mSV1FW4WoUlNXrGQaXeInAZ4yhYenVsfovWu_LH-D8OI8938Lw6GvDpzbr-T9WH622JCHFtWihCPwEXB6OgLTTbyQMASqHdHydJQlVzj_L5TIu48CX9YRGMFv7arAZcIUFRtmTBRZUlpDlLQj_S3RpXDmqkYaxXDcbhfqwb3FPMHkww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینتر دید کسی حواسش نیست رفت به یه تیم از دسته 5 آلمان 16 تا گل زد. دوستانه نیست این دشمنانه‌ست بیشتر.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101780" target="_blank">📅 16:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101779">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56f574b376.mp4?token=o-rlC9m92Eu-lGZojSuhfvq8j_HF4Xz_G54RTn47zoj7Y3Bu441j5oURZJcSsVKWqtSxqeU1f_EwxaTnRNVVhtNia_AluLA0Q8VcoaVHpy2-ywdxUSoWEZupF8G_kmk6eDAAqjEQNE1tu8m26o8_ZeUFJylkOAhqjnfEaHBehJglwt-wpX80T2aeXHTjcihBB2jxPKTRM0OrxyPS6R1P_G9FhRXuUF31ENiUR4VxclRGduv2VG9zpkohuPLaRSEVvxa0PvrVd2VBhmf0Lhgpk1me1Szr_5NSlylPGWurGgPlbSG4hEQeGIiQAlKUNVXGbcZr6XwlCphxvXokaL_sYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56f574b376.mp4?token=o-rlC9m92Eu-lGZojSuhfvq8j_HF4Xz_G54RTn47zoj7Y3Bu441j5oURZJcSsVKWqtSxqeU1f_EwxaTnRNVVhtNia_AluLA0Q8VcoaVHpy2-ywdxUSoWEZupF8G_kmk6eDAAqjEQNE1tu8m26o8_ZeUFJylkOAhqjnfEaHBehJglwt-wpX80T2aeXHTjcihBB2jxPKTRM0OrxyPS6R1P_G9FhRXuUF31ENiUR4VxclRGduv2VG9zpkohuPLaRSEVvxa0PvrVd2VBhmf0Lhgpk1me1Szr_5NSlylPGWurGgPlbSG4hEQeGIiQAlKUNVXGbcZr6XwlCphxvXokaL_sYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
برخی از سوپرگل‌های لوئیز سوارز در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101779" target="_blank">📅 16:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101778">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3068c762cc.mp4?token=k5lF4HY79xV683wkl7DThxzduQq54PV1fFiQMssivl5hCFfCwRPP_Cg8VuuPsU1bYDumfqPWSX6lmI4EzZd1Eu0uShEOaWhIAdqZ5JafY5KlBNCfYACE8BqeXXBMoHVnegCmY9koMS8lOSVnc8Hy9WjEJrzOaxygGVva8p3T9z0YW9B8xiwN6w5oR08P6SsPEyr-Oa3GsYYFFYRrrZFkpbltXurp79t956t17dqUSsffUsbGCd6xHNIvHjwjJm4HrPp22mgXObTknvEv92gTesH7PWVK6xYSiKQUn-1qE7vOgkRqN0dl09CGkoHYV09wsbW9-kKuEpNJDIkEF7AJOFieu7vUb995U0bt_unzExtEU1fSN9_huUdek8VdF_8rNBbzHxw6AmAzfxKeifiFfNa5moSFVXCCWrBvA7u3nSfIpAAqamAAFfSYc_dOqM8h0yVr9K4UpSicWzVXLFjDHC9VzTG56aRiCHMulziLKuWbwekRbR1sHnvyB9dLdTe2zrebhsVJ9I5-0YnljCnpy8WaH0ec4nd6_uKJ0u_D12jo2Sy1FkBghoPezPPPY-sPe-xigXgXAXlT2-kmHi96BF2x1P4WEbHQonyYXD4V-8laxhHGdNrNY-LWApUOor64P7mllCUt1Ynune26c2S5Z42Nw25I0zlRvBxAh1QDCQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3068c762cc.mp4?token=k5lF4HY79xV683wkl7DThxzduQq54PV1fFiQMssivl5hCFfCwRPP_Cg8VuuPsU1bYDumfqPWSX6lmI4EzZd1Eu0uShEOaWhIAdqZ5JafY5KlBNCfYACE8BqeXXBMoHVnegCmY9koMS8lOSVnc8Hy9WjEJrzOaxygGVva8p3T9z0YW9B8xiwN6w5oR08P6SsPEyr-Oa3GsYYFFYRrrZFkpbltXurp79t956t17dqUSsffUsbGCd6xHNIvHjwjJm4HrPp22mgXObTknvEv92gTesH7PWVK6xYSiKQUn-1qE7vOgkRqN0dl09CGkoHYV09wsbW9-kKuEpNJDIkEF7AJOFieu7vUb995U0bt_unzExtEU1fSN9_huUdek8VdF_8rNBbzHxw6AmAzfxKeifiFfNa5moSFVXCCWrBvA7u3nSfIpAAqamAAFfSYc_dOqM8h0yVr9K4UpSicWzVXLFjDHC9VzTG56aRiCHMulziLKuWbwekRbR1sHnvyB9dLdTe2zrebhsVJ9I5-0YnljCnpy8WaH0ec4nd6_uKJ0u_D12jo2Sy1FkBghoPezPPPY-sPe-xigXgXAXlT2-kmHi96BF2x1P4WEbHQonyYXD4V-8laxhHGdNrNY-LWApUOor64P7mllCUt1Ynune26c2S5Z42Nw25I0zlRvBxAh1QDCQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چطور در لاماسیا، مسی و اینیستا می‌سازند؟  اینیستا و تشریح سازوکار خاص‌ترین آکادمی فوتبال جهان؛ استعدادیابی در سرتاسر دنیا، مطابق با استانداردهای بارسا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101778" target="_blank">📅 15:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101777">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">▶️
👤
به بهانه تولد 49 سالگی مهدی مهدوی‌کیا ستاره سابق پرسپولیس؛ تمام گلهایی که در در تیم ملی به ثمر رسانده را در این ویدیو می‌توانید ببینید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101777" target="_blank">📅 15:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101776">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfurPxkr3b3GGrFzNcrw5UewEl_jYP9757ujNvUnLRV2hbQD6PnvKtS11LXsRaRyrI82sZYc-tLWOG6CrFXTdM3eSD9qfRmMD5p8Ka7OXDwbRa4vPlpYvtdRKHUTQg9TcH4krxXTEG2Nhdro54r2YL-jx3or2-hI_GzOXDArFsUXHm_ZDGP8bLZtNAxOyjBSCpgZ2uWZ8TS0hN2-i8IxpOoqKJVNuyUxrhSf3fwDGQ4I6MeMBqUDsoPyloh37i4YvknNagheTB9T1ndAk2fkEmEuJvbIpwPJxr5KLCsf0orN0Iu2VFR1ERMkCeVZ7IWqKUF2PFDVg2MFzszi2cqY5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇩🇪
یورگن کلوپ:
با چیزی که خیلی مخالفم فحش به خانوادست! اگر به خانواده‌ام توهین کنید، من می‌روم. اگر روزی فکر کردید من مربی بدی هستم، مستقیم به خودم بگویید؛ همان لحظه بدون اینکه حتی غرامتی بخواهم، کنار می‌روم. من این کار را برای خودم انجام نمی‌دهم، برای شما انجام می‌دهم. با وجود اینکه دیدم با ناگلزمان و توخل چه رفتاری شد، این مسئولیت را پذیرفتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101776" target="_blank">📅 15:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101775">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cz2sQB_9XbpS2IFCYHNB4glIn5QlaxpZCTvZd1hID2IVMohFsprEopYm8RhotiOvIYQeTe-9kDWqwtzpXRgx7cb2UwCif4imS8vSdLiKwXj3XX7I2PqYl5nnd2VNjoEzdDVh_yLD2o_LA0O0MddM45z-E9KsifxJFVvL732Z2ADvh0OEIH_AXk9UVDx_XGVP_zaT4na2FS4T4t32P3pHw-qULSlqlE9Hi5ePz7-JLwdz0Tw_XGutHeKAERDs1rjVLacWoIMRH1_uvzd7kzkqcvivj0mcI5BpIEJrBmPrUa15qqsoB6-OLx7xIHwl4oZ27AC-QjdMJc5lTUfcbmp5dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
دنیله دروسی:
عشق من فوتبال و رمه! اگه بازیکن رم نبودم، حاضر بودم همیشه 10 ساعت با ماشینم سفر کنم تا برم استادیوم و تشویقشون کنم. هیچکسی هیچوقت نمیتونه رم رو بیشتر از من دوست داشته باشه.
تولدت مبارک آخرین گلادیاتور رم
🎉
🎊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101775" target="_blank">📅 15:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101774">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_IUUcuH1z5ZPB4mSx3kBm6IuegeK9K2vhDamUULcD7PFD5gh0ILErMPcfJ1SQbZnfgwyjM-RCBaM_smMytLK5np6OcIO5tP-rVsul52xcNh_dfyOwe_Z-rI9UQpoP0LPKXc7MMPWtosU3BLlG3MkEe2hHPWTwsQV880gtzFgqiw9O3K9_WCbvIvcfop_K5jpW8ZJZRGRJW5BwNGzDsOT1p4Q1Q75VtpIEKXOm7K2nogo4MJRyifyFy7VOK338y2B8WL1wlX82rpTRAHU9BaqfTZ3UGRpRtCwevx3DFl-vAy1AO1pZi8VRiFo1vx3NoDWOtGN4tZ340CRkDgxLlYVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
قرعه کشی مرحله گروهی لیگ قهرمانان اروپا 27 مرداد ماه برگزار میشود.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101774" target="_blank">📅 15:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101773">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5pvFgnXrNSsFLz9uOHi9Q4m_HAGRvvKf-Q-hc-xorsfsz7E7BjAZCJBP74kcD1f1kP7Dihs0Ib2H6nKPkjRHcLO91XovtvG5u7FZ5H53f_c5vJWJmG7WfkWmMTRhada3MDKKyKOIErwj5LjRs1NwHDywASLKfJin5jUyS4OIRpSDvZNxTmWQ8Ls7BK876euRrk4-5gyrQOGzFhHRbJQMqMXxU02yGld2tE6fnGSLaoHE4N1xmRbwAvP7H4uZF4kMb2ryVTnuXrE96_B0ZNREiUun5BS5N-dX_J_EdXGHQ4L5foieCTtCkLuz6J8VDgp9Cv6oQNYz2B7osUBOeSNFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
📊
مقایسه عملکرد نیمار‌‌ و امباپه برای پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101773" target="_blank">📅 15:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101772">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUd2wuihrjUi-wEFEQI5KgRF85FRl4qhbl_I3noHpI6BxjiB4L00Reiz4zkF9kLpmnnrKxTYL5LGct3gBXztUaXSyGo6VgX4BULQ0VU4xOkfqGT4Z8Ef5DJkZMtZcBrMLGvqLIt6jEHYaEWyLmD_o3ZNQGOaCR1TFiqTi5Ub1XtKroSs3L4y-rs_dALUzKdgsfdW4BnemifHreMnnOjPIlmNADobJifuE-x2iWbYtrwiTQy0hTE-nKn_0mDUNHJKQdO3hWQfgtLY-yRvjyo08WCq955ji_tTLTa2wZ8s8TpngNLFvdn8NWekySW-FQSPSWGU8MSY3hdvIXsxRC1u6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوریییییی از فابريزيو رومانو
🚨
🚨
🇮🇹
🔺
پپ گواردیولا پیشنهاد سرمربیگری تیم‌ملی ایتالیا رو رد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101772" target="_blank">📅 15:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101771">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrIeqzAIVCCIt5EPsjEG3icLcS6HEzBqO5DAyfd22-6SJh0McE7kp7nSHnxUrp93g2wdiCnD7EZSYbPFwRJCK53JYpzgiyGiGYFNDz5MRYaC0F1k8kvMD3BG1W-2p4dllPMD7vqsG58O-LH9DEHxoFs9RGRfLIkSaYhSMHf9WAjgj6k-fRHPTMzUMjI7zM59wO8sWuhDr2bHEPov7NVmW0h6Xpj5UC4JA3aSZevGY45PHpQUJhiuI24lb1d2FPvkSWYptG6B3N4Gpoajjrh21Zt0KhvnCbmCx0fEObBOJOj1T12HPSbrEJreFZaukx8xed5jdCaslCJf7m3wmN71mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
اندریک و خانومش و بچه‌ای که خانومش بارداره به اسم کندریک!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101771" target="_blank">📅 14:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101770">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saD1P7GegXcxnBAYev8L-DgtzIM71OUiJcIY_TdKpMxrdEDdqROqTPUBhBwcUDmO63WflCjRabEvNYkRFcivSp6wmH3aYrWy3w4ya8pvTbsisHmNhAAYvwk9XzWO-W1rjkJ-7TSIYrVyzmfkaIvhzAq1tOoBEeVIyAO2h0X9lqPS-PZghovhjr-4hoqiardUEkLqkJZ5_r13wB_E1JUyub7h7-iT3Nm58wZQhiqMFKEMD_rmnSAprxrKThJPvXbkjzWLZnlYSEBM44ovyJxsTBArQfd__ijW2rxEV1ARCAbtGcSHk_0IoBoHDuPcOeiV2HUQGQueqgDM7iSFobhFDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚑
🔴
از زمان پیوستن به بارسلونا، فرنکی دی‌یونگ 416 روز رو به علت مصدومیت از دست داده که با این مصدومیت جدیدش احتمالا به 566 روز هم برسه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101770" target="_blank">📅 14:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101769">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/accd9e1667.mp4?token=RFsmCP2SwT8lF1giaNRU62B-VM6PdNLr5dH55JbfRxdL47zPeK6qhbDH_vyHzm2dpPKVbq_Qnb3mi6-ZtdH-B2jz3ECWcS27nRt2KUwpSJTQhUDkkceqmnfpnOK8M0nKGFKU9Q2B6S5Jwon3GxRvow8ChAivf76rdlyhSle7N01hAtUz2liXfLjZwtgTsbUrcZ-2EVYt2DruRR4j4bFV_fm0VjvgF_TXoHRbKkBn6UbzkUj7XXPtt7XREyKYsovaPMKPwvtSbWaS5dAG3w_djFaylCHQrOqiJ9tfr_BVdpbxxRavd8sUX9j87zDoXTWRa-59yVJIrXI2BUQfO4k0YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/accd9e1667.mp4?token=RFsmCP2SwT8lF1giaNRU62B-VM6PdNLr5dH55JbfRxdL47zPeK6qhbDH_vyHzm2dpPKVbq_Qnb3mi6-ZtdH-B2jz3ECWcS27nRt2KUwpSJTQhUDkkceqmnfpnOK8M0nKGFKU9Q2B6S5Jwon3GxRvow8ChAivf76rdlyhSle7N01hAtUz2liXfLjZwtgTsbUrcZ-2EVYt2DruRR4j4bFV_fm0VjvgF_TXoHRbKkBn6UbzkUj7XXPtt7XREyKYsovaPMKPwvtSbWaS5dAG3w_djFaylCHQrOqiJ9tfr_BVdpbxxRavd8sUX9j87zDoXTWRa-59yVJIrXI2BUQfO4k0YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
در چنین روزی، ۱۶ سال پیش، ماریو بالوتلی در جریان یکی از بازی‌های دوستانه پیش‌فصل منچسترسیتی این حرکت عجیب را انجام داد. روبرتو مانچینی آن‌قدر از این اتفاق عصبانی شد که بلافاصله بالوتلی را تعویض کرد..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101769" target="_blank">📅 14:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101768">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33b6580c49.mp4?token=hSmwjvorogRV9skl5GCiWOMsCroFKVbYLnQOriHuIs1AXL8_uN3Sselzkb_LAYg0jZ9bCD1jyQFRoIUt_5cvl35_zijGTANh0I3362d1efiiqfHkMekAdSOJpbIMsfhZK_P79acXn44vstVGWik2H_rKXXD3F9KVA23kCT-FO2KxpJNyqzI1PB6j_VgGpb7_GJLOL9FntYKux2moL3XoUyYgtblNogKn1xcnTx0bVsuiSkr6VqD1ycd8uaNdTIYyj5n3mOHlq0dnUPcCSBMjic5H69n0OF3mzO5bibIxtfETsuntdRJ3IURmHx5kDuUr3fW8tisfdLAfRSF0-vOrdTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33b6580c49.mp4?token=hSmwjvorogRV9skl5GCiWOMsCroFKVbYLnQOriHuIs1AXL8_uN3Sselzkb_LAYg0jZ9bCD1jyQFRoIUt_5cvl35_zijGTANh0I3362d1efiiqfHkMekAdSOJpbIMsfhZK_P79acXn44vstVGWik2H_rKXXD3F9KVA23kCT-FO2KxpJNyqzI1PB6j_VgGpb7_GJLOL9FntYKux2moL3XoUyYgtblNogKn1xcnTx0bVsuiSkr6VqD1ycd8uaNdTIYyj5n3mOHlq0dnUPcCSBMjic5H69n0OF3mzO5bibIxtfETsuntdRJ3IURmHx5kDuUr3fW8tisfdLAfRSF0-vOrdTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
کدگذاری به سبک قلعه‌نویی؛ واکنش قائدی به حرکات عجیب قلعه‌نویی کنار زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101768" target="_blank">📅 14:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101767">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUBk5UW53Bu85OZWIKURA7RGv6fnh7hm559uLKeg3zG5WYdv5JjFwPVagE1vw2NUAMIir-a1NsoXSRC3tmjbfgwboT7GTb76MGhzjDH1-KLEMNrcSD0m8FQftfiMedIka0GUnrxdUHO6IEDygGGApz3hd22hcsrSNO23EUs77j2WCz5KdJrhQ0GWaRPDZMUDiXwkSlwX6ITdZ104WoB5CdaCzl8PLQFsYz0iNfUl7HxvmrFLFv5lr9Dnovfrw-D_eY3RhzmKaL_uHQAnfJukLZsxrC9VZYNsooIe33OtLmDV0zfDWFNLqIKQPGrd6d9Ix9vxIcpXhRQkHHRPxj6vMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نفرات چلسی برای اردوی استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101767" target="_blank">📅 14:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101766">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f65adaacf.mp4?token=iEvym2wVQoTscqP-KlBs2oHNb6CuQjgaEclT3hCNowlwh8PyxEKhu-xdBCK_jBbIhpazLdI_8peU5m9H82vW7_1xsqAPmc3uBXvVKdvB_cgMxILdhYPwpLoT4ex8ks34E4vk8vZRhKxbKdEQoHdGt3hm_nLEE2RxeR9lhOuioSY1k7ASDLt0lgcruwLXyek61qropHKFTiK4n-lfu6NOrm-AzafeQ1qM3lkAsgJu2EpyfOSpUjR1fPTyMND4FvjrCMBMQgHN3BkTANVdPGTiT_jOaivzBUkMtX1BxvOOPp-bTj_f_kJgnY5ljowMPsF9u-LegDHdxtvMKnD4KbNTcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f65adaacf.mp4?token=iEvym2wVQoTscqP-KlBs2oHNb6CuQjgaEclT3hCNowlwh8PyxEKhu-xdBCK_jBbIhpazLdI_8peU5m9H82vW7_1xsqAPmc3uBXvVKdvB_cgMxILdhYPwpLoT4ex8ks34E4vk8vZRhKxbKdEQoHdGt3hm_nLEE2RxeR9lhOuioSY1k7ASDLt0lgcruwLXyek61qropHKFTiK4n-lfu6NOrm-AzafeQ1qM3lkAsgJu2EpyfOSpUjR1fPTyMND4FvjrCMBMQgHN3BkTANVdPGTiT_jOaivzBUkMtX1BxvOOPp-bTj_f_kJgnY5ljowMPsF9u-LegDHdxtvMKnD4KbNTcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❌
مصدومیت شدید یک ورزشکار در جریان مسابقات مردان‌آهنین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101766" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101765">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ea14c8f5.mp4?token=Mxqw0bgCYhE8Z53de7useu9RwDml3YQsvZ-4VRNd7_g842gvPa0WOmY0jV5KLDgG1QRvglcg7-p0RpvNkh2T5rTy-Kk8UL1My5UYotLedJgTZEM19TxlEdB1hL9S32SIV22LANWCk053PDO3ybkHtzO5luU1cFnSE1avQRmjUrSTFadZ2Xcy9xvNV_URL4W5XNdjgbesfTs14mf3JdCywPg27bR9O-8etCwYCw-n9bO12VXuGhB9Ss_GWRoqjX9y9rG3co0l5PWPpthy2d63IUyJZbhFHrVdhQ_4uhSGoe2z0NP2W6RlVHRhuz3_88PWqd_4QYm_S075WUCorswP1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ea14c8f5.mp4?token=Mxqw0bgCYhE8Z53de7useu9RwDml3YQsvZ-4VRNd7_g842gvPa0WOmY0jV5KLDgG1QRvglcg7-p0RpvNkh2T5rTy-Kk8UL1My5UYotLedJgTZEM19TxlEdB1hL9S32SIV22LANWCk053PDO3ybkHtzO5luU1cFnSE1avQRmjUrSTFadZ2Xcy9xvNV_URL4W5XNdjgbesfTs14mf3JdCywPg27bR9O-8etCwYCw-n9bO12VXuGhB9Ss_GWRoqjX9y9rG3co0l5PWPpthy2d63IUyJZbhFHrVdhQ_4uhSGoe2z0NP2W6RlVHRhuz3_88PWqd_4QYm_S075WUCorswP1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
😐
افشاگری پشم‌ریزون اوجی وزیرنفت‌ دولت ابراهیم رئیسی: موساد به من زنگ زد گفت ۳+۵ چند می شود و سپس خط لوله هشتم انتقال گاز به شمال کشور را منفجر کرد!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101765" target="_blank">📅 13:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101764">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a128d814cf.mp4?token=XKreureC30lDTHbNFVdxgS446vWZTqebdlE1Tf10KrwHDT5u57hrNoh1ZRgtwybDwnFPv7UwmuIKQb9nht_TvTJF1rtDuMfnvj0IXsSP43hngqFBAq0LPGLAaM_u-DQV-aJxgJJVUKlIp26lBVYlcr4LwGHp5wQ1zddIV7EYbvStC6GbC-MsOtClijqC2D5DDgYrBhvrytn-MjfVWtJIPVGyMfjJ2lRAzKKYkb2odLlMdc_lHjT_ekMwxYou1YxLnDH9dqgrZrvfXFCojzot79-ERnnACo2v4upuYFnsSQldkc7Ge3nk2j-b6qGm_sIXfVz7b-qliGeL-NtJCYUeBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a128d814cf.mp4?token=XKreureC30lDTHbNFVdxgS446vWZTqebdlE1Tf10KrwHDT5u57hrNoh1ZRgtwybDwnFPv7UwmuIKQb9nht_TvTJF1rtDuMfnvj0IXsSP43hngqFBAq0LPGLAaM_u-DQV-aJxgJJVUKlIp26lBVYlcr4LwGHp5wQ1zddIV7EYbvStC6GbC-MsOtClijqC2D5DDgYrBhvrytn-MjfVWtJIPVGyMfjJ2lRAzKKYkb2odLlMdc_lHjT_ekMwxYou1YxLnDH9dqgrZrvfXFCojzot79-ERnnACo2v4upuYFnsSQldkc7Ge3nk2j-b6qGm_sIXfVz7b-qliGeL-NtJCYUeBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🎙
پیرس مورگان، مجری معروف تلویزیونی انگلیس، بعد از باخت آرژانتین به اسپانیا تو فینال جام جهانی ۲۰۲۶، دوباره رفت سراغ انتقاد از لیونل مسی.
گفت: مسی فوراً دوید سمت داور، مثل یه بچه مدرسه‌ای که می‌خواد یکی رو لو بده، تا باعث اخراجش بشه. به نظرم این واقعاً چندش‌آور بود.
این‌همه از «سن‌لئو» حرف می‌زنن؛ همون کسی که می‌گن قراره بهترین بازیکن تاریخ فوتبال باشه. ولی توی فینال کاملاً محو شده بود؛ انقدر که اصلاً حس نکردم توی زمین حضور داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101764" target="_blank">📅 13:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101763">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eC4AsgZ2GrX23F7SmMCj2gRPMMk1QsOxuVbF4ggfJ1NN6AwrMRT8iqRggM7QNVbDilwEfK15tjnCM0ujBrspC13ew_p0KUqX4u3ZosYcAWsQU5osJpuCPTVrCUcdivjdbPQbNbV3J7LYxgQLD7YIvn-6sAXQ8SpAPqMeh-iiHWZi0U8iSvQ2W8zEovxxKCoeMOSDVcC8RhJ-yOqvLC3mHDnQVPM1Zu-NaEVwOrTAeL3kwMAWrv43APPCn-qgo0jJF_DMYMvVNhG_de9AKjq1MVMakI3_4eT5FOB67x8CaB5OJgHW8RqPdf8jLFu9XXKacoUCWCwx8WKlZs26EE01vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🔵
براساس شایعات منتشر شده، قرار است یاسر‌آسانی تا فردا به تهران برگردد و در تمرینات استقلال حاضر شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101763" target="_blank">📅 13:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101762">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632f699042.mp4?token=lrxbyJQ5xYzfZHSgex6yab3KJyv1iacTGtgqRnF1QwvwQzF5J9Dxg4crT9yuGp9ljUKJD_u_oTW7bUFN15woCwjkeBpklJzphwEF0HHhiQTB_mRd_Br0-e5d12S7PBc5-xIlayEWrGY5fZVYJlJPTG5lkeAlxIjWe6pW6I6gmre8b7stznwOCPAZr-h6FRZkF7jpriSwyksDcnga8N-1gGgRvIOaUVzcHh0ZRyw8d4AdnHH5m8J6LfYzvs6EqbDDnLTD5XcLS6tpHwWBzrky6plbB-U1rt8bxnOct-yQPP5wZOe6JSamdcnmQJWWuFlQdpg9WVuvw7oQWqMml8y96Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632f699042.mp4?token=lrxbyJQ5xYzfZHSgex6yab3KJyv1iacTGtgqRnF1QwvwQzF5J9Dxg4crT9yuGp9ljUKJD_u_oTW7bUFN15woCwjkeBpklJzphwEF0HHhiQTB_mRd_Br0-e5d12S7PBc5-xIlayEWrGY5fZVYJlJPTG5lkeAlxIjWe6pW6I6gmre8b7stznwOCPAZr-h6FRZkF7jpriSwyksDcnga8N-1gGgRvIOaUVzcHh0ZRyw8d4AdnHH5m8J6LfYzvs6EqbDDnLTD5XcLS6tpHwWBzrky6plbB-U1rt8bxnOct-yQPP5wZOe6JSamdcnmQJWWuFlQdpg9WVuvw7oQWqMml8y96Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
خبرنگار: ارزیابیت از عملکرد مسی در جام‌جهانی؟⁣
🎙
لوئیس سوارر: با سنی که اون داره، میتونست بشینه توی خونه، اما با انگیزه تمام رفت تا دومین جام‌جهانی رو برای کشورش کسب کنه و تیم ملیش رو هم تا بالاترین سطح بالا آورد اما نشد. فکر نکنم کسی گله و انتقادی ازش داشته باشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101762" target="_blank">📅 13:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101761">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a535e73d0.mp4?token=bFxBthm6eKQnUwU4PTkZl2oQveWrIsYwExylBsnthVz0kNaUDfI4F3ct9FTzX4WwKhtGLhBjTbLqG4dz1mTBszdnvdCJdC8Fr94VkUokb_5RqJlOMAooEiC5ahQAISxCB08PRbrQGmhb3YiHtwFPd1hv7UWvt5KtLam4X25dS_2H3j78ak7NU5UvC5RxN0rlJyO55QAgN5svmUdBNt8e95rlQek0I0_-020RoIDQYkoX5Fu-IrBRyS2Q1KY-2DvXbdzvQ-mtmFXEg45Bpmt_LSgRLI4eH2vuynaR6BdajHDBHVpFcZOhpN5suh3Y7drqgiZPMG03viLYU8NyhqEWlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a535e73d0.mp4?token=bFxBthm6eKQnUwU4PTkZl2oQveWrIsYwExylBsnthVz0kNaUDfI4F3ct9FTzX4WwKhtGLhBjTbLqG4dz1mTBszdnvdCJdC8Fr94VkUokb_5RqJlOMAooEiC5ahQAISxCB08PRbrQGmhb3YiHtwFPd1hv7UWvt5KtLam4X25dS_2H3j78ak7NU5UvC5RxN0rlJyO55QAgN5svmUdBNt8e95rlQek0I0_-020RoIDQYkoX5Fu-IrBRyS2Q1KY-2DvXbdzvQ-mtmFXEg45Bpmt_LSgRLI4eH2vuynaR6BdajHDBHVpFcZOhpN5suh3Y7drqgiZPMG03viLYU8NyhqEWlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇫🇷
هوگو لوریس درباره برنامه فرانسه برای مهار مسی: "یه دستور ویژه از طرف دشان به انگولو کانته داده شده بود. کانته همیشه باید سایه‌به‌سایه و تو شعاع حرکتیِ لئو مسی میموند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101761" target="_blank">📅 13:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101760">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adad22d87c.mp4?token=s9NUSf3w-MbYhp-EDj16wQDLSRSKt08nG4cFHrdKXxemtoEh0Xq8Sd4WTIkIALApzTGn0RIKg6xX35-nEaFiik4x07hBrWBsQEm5arXREAUpat2Uwf3venqV12-05WOUFQ6o7lt-otHMcv7HoRA87dxM1dPMjGKZxVbCuBrqOHr7xRMSJwpTRCj7SEKF8Tt2kRBGmTwXv7GnyRWaWPsjU3OIh4zc8ABn_AwxWfHQrDLIZqkyQA85tKOQH6Sxsj8fxfhfuhB_jnWRqVIv-3NPX_-RyyyDRvGyYFPRWR_T1TDF8Wh1g3adx3XHESHPAWoma4qur063PZR46c9hiEB7sIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adad22d87c.mp4?token=s9NUSf3w-MbYhp-EDj16wQDLSRSKt08nG4cFHrdKXxemtoEh0Xq8Sd4WTIkIALApzTGn0RIKg6xX35-nEaFiik4x07hBrWBsQEm5arXREAUpat2Uwf3venqV12-05WOUFQ6o7lt-otHMcv7HoRA87dxM1dPMjGKZxVbCuBrqOHr7xRMSJwpTRCj7SEKF8Tt2kRBGmTwXv7GnyRWaWPsjU3OIh4zc8ABn_AwxWfHQrDLIZqkyQA85tKOQH6Sxsj8fxfhfuhB_jnWRqVIv-3NPX_-RyyyDRvGyYFPRWR_T1TDF8Wh1g3adx3XHESHPAWoma4qur063PZR46c9hiEB7sIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
وضعیت استادیوم فینال جام‌جهانی که درحال کندن چمن و بازسازی برای مسابقات فوتبال آمریکایی هست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101760" target="_blank">📅 12:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101759">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQKU9lYqP-ipyWRnQs6KL9H1vgZdTi-1J5nsQ8W5JI6Ss1NC0n3OpKt-pbEdi2_VBtaafpppEaAVqJ1ulH2P6cwdMIcEkJeVk2xjLDZRzzHdYYEgJqBU9wCuZh70GcQOV66InXNGGmwViA8QB8Y9gLM6faGj9hfImKL5fRO79WhhCrCTZJVJUs27npPEF3HKYTMKcGo4hT9mHmLbmk1_bWYnTZJk-FJwUBDpQsD_fQvgc1n1rW8dYLKmlZ7ezWwK_CqfPh0dfyJ4DGY3mVjSSfgAU8zbQ1LwAv-ioc76XEubIKlvZNKaYNDJTxAlYMlTMp4ZhdBszGLf6HaF7C0RIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فدراسیون فوتبال آلمان از انتصاب یورگن کلوپ به عنوان سرمربی تیم ملی با قراردادی تا سال 2030 خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101759" target="_blank">📅 12:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101758">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IftOAMbyareRX2LpnuA-8Fih_IzfMuDbCwogb319hynRxJsx6dp-e-q5RrWs8LtWDuMZjTnCu9Fj189sKN4fnql-Esc96dx9AaUy22zguCnRsdoAsW-5K42t9CjY7Af2DCY5nYBa18NLX2LYiWgu_tE2wPDAwvaFWGwfutZtn3z5bxpkNzUFCO_hNiUm8eBFiMPJHaDr8ykOOPvC1sv4s3wCNBRj76ICL0K97nsvtIYZqDCITTy-LF6O1C-1pkE-dwAfcgDRpKdk2M_5E3kDUlmiw3AihG4IHsVxNxx0zn-wxwY6jo8RGNROZXvlTfc_aj1J3JVLhgS6kE7nb0BOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوریییییی از فابريزيو رومانو
🚨
🚨
🇮🇹
🔺
پپ گواردیولا پیشنهاد سرمربیگری تیم‌ملی ایتالیا رو رد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101758" target="_blank">📅 12:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101757">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d513714e20.mp4?token=ZLMH1T3vZowHi_Lmzl1oHDqlwu4wIdFLt4ZhDLFR53lxmqiwsnIgcdShLjx2vEEh4K20CDxgflXrhSpKiC14KWMk6QzZm2raizM9SXk7KcvMO8Qp3dMDFU2f9nBTCT7LUxFTlOKxxiVRbQiE6l3zfLNOB8vOttDiX25qseBaFcLnKYbN7VFAdGmQHTNTjaWPT6rel4zawAofuy0kPO6PoNFLE4bpQyFjy8p8hbKmkUKQl8t6Vo__seB4a5FK1eEiiUYs0vw7IblgFuH9LLU-nG-HAMI6Lx5ACBDCATFNqYzEdaJSV-eLVRrPdN3M9JtQX9TFPHpzjH6PKHtFdmclrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d513714e20.mp4?token=ZLMH1T3vZowHi_Lmzl1oHDqlwu4wIdFLt4ZhDLFR53lxmqiwsnIgcdShLjx2vEEh4K20CDxgflXrhSpKiC14KWMk6QzZm2raizM9SXk7KcvMO8Qp3dMDFU2f9nBTCT7LUxFTlOKxxiVRbQiE6l3zfLNOB8vOttDiX25qseBaFcLnKYbN7VFAdGmQHTNTjaWPT6rel4zawAofuy0kPO6PoNFLE4bpQyFjy8p8hbKmkUKQl8t6Vo__seB4a5FK1eEiiUYs0vw7IblgFuH9LLU-nG-HAMI6Lx5ACBDCATFNqYzEdaJSV-eLVRrPdN3M9JtQX9TFPHpzjH6PKHtFdmclrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇹
⭐
فوری از فابریزیو رومانو:
⚽️
ماکسین لاکرو از کریستال پالاس به چلسی پیوست. 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101757" target="_blank">📅 12:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101756">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47d5bde5ed.mp4?token=bpxsDclMZshllyxz12WviUJ9VX9zFOcDdAJqn8kY2h7yQ9lF1kkgKPelSoz4Ar4la0DLDsKxH95wzXcNKaqojv5k_fpMX0LwIKaxnwugejh8Ssqj9M2L4T6tvzwMSzOizJsAiW9XKtxARjS8ofPLqm8sQJyxOwxka68GgLZhGmT9iaVyLUMesiVlEQ309HR5WCwGDnlHxnSieDaOY-ee9UaXjE9nmT9j2JyJJfdGc-WFVvwEJhyN7pjlgflFvsX-wMXa2c_HlU67hXMHOARGEzO8gXyRATt4jcE_pvW28OvOzM5m5Q51CbXg9_CUgjDdcTzR7e0BFiXLh0siX1ITZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47d5bde5ed.mp4?token=bpxsDclMZshllyxz12WviUJ9VX9zFOcDdAJqn8kY2h7yQ9lF1kkgKPelSoz4Ar4la0DLDsKxH95wzXcNKaqojv5k_fpMX0LwIKaxnwugejh8Ssqj9M2L4T6tvzwMSzOizJsAiW9XKtxARjS8ofPLqm8sQJyxOwxka68GgLZhGmT9iaVyLUMesiVlEQ309HR5WCwGDnlHxnSieDaOY-ee9UaXjE9nmT9j2JyJJfdGc-WFVvwEJhyN7pjlgflFvsX-wMXa2c_HlU67hXMHOARGEzO8gXyRATt4jcE_pvW28OvOzM5m5Q51CbXg9_CUgjDdcTzR7e0BFiXLh0siX1ITZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
🤯
«لی میژن»، دونده ۲۵ ساله چینی، در حالی که تنها ۸ کیلومتر تا خط پایان ماراتن دریاچه هنگ‌شویی فاصله داشت، دچار قاعدگی شد. با وجود خونریزی و شرایط دشوار، از مسابقه انصراف نداد و با اراده‌ای مثال‌زدنی به دویدن ادامه داد. او سرانجام مسابقه را در زمان ۲ ساعت و ۳۵ دقیقه به پایان رساند و موفق شد حدنصاب لازم برای حضور در رقابت‌های قهرمانی را کسب کند؛ عملکردی که تحسین گسترده کاربران فضای مجازی را به دنبال داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101756" target="_blank">📅 12:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101754">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrxLbX-H7f686LyPGvDUP4ehDEgSHwgsz5d_IVIOYW1i4axA9Kvbv0ahUCsnR8c8t_-yjSAq8iBegkPL7osLjIuLeiGwKNQatEtXzJtdmh2vCFzQoO4lCsDotzvjYrbSQ80M-j_8Yq79IZHDhS0fl-pvRMJ9QBibCZie6HdaS7ft2_BgvmmAzDeVti1Gdpys6s7DVM5Dht3BRgPl3UJAnMzvq1k2AMZHemuExb25xLSNqnKn1y3TVYMG-CtfNic_44avWRjuu5_rnja93JkpU6eZ2wR2xP6rwo4hO_f5ghvSpTYcUsPxlxBWQ6idRE0Vruz-kNN7EN9efknutIdP7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بن جیکوبز:
🔺
چلسی به احتمال زیاد قرارداد با ماکسین لاکرو مدافع تیم کریستال پالاس را با مبلغی در حدود 52 میلیون دلار نهایی خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101754" target="_blank">📅 12:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101753">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60409e4f3e.mp4?token=QDz-apJ8qgQ-p3NdTtyQcab5HI2B-OiB0IBUyckfJT09tqsfO0AbQ6RTIvshxbzpTXaSap8xNFiRAy06rGAxc71iptSuRZOCwdqPsONt4ljWECP2aTdN0e6sfvUJtP2l7-c9Y3YS34XYeDGpuipyIS3KA1-X7LAgzGGL_HEExaU8xtCMepjVfer3S8TzDGIbXByBFhPLM6vXFBI17fA54OPzNv6mNtvy5qstxpZKdmmB66fh2jTTahOQitp86adl5VyShcsJlM6n-bhAA2GZHBa62CYmrgcfsfLgB2leHEs2xJ72MCEaueNQaW1Qw44bJkt5NOpGCTQychTI4gqRJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60409e4f3e.mp4?token=QDz-apJ8qgQ-p3NdTtyQcab5HI2B-OiB0IBUyckfJT09tqsfO0AbQ6RTIvshxbzpTXaSap8xNFiRAy06rGAxc71iptSuRZOCwdqPsONt4ljWECP2aTdN0e6sfvUJtP2l7-c9Y3YS34XYeDGpuipyIS3KA1-X7LAgzGGL_HEExaU8xtCMepjVfer3S8TzDGIbXByBFhPLM6vXFBI17fA54OPzNv6mNtvy5qstxpZKdmmB66fh2jTTahOQitp86adl5VyShcsJlM6n-bhAA2GZHBa62CYmrgcfsfLgB2leHEs2xJ72MCEaueNQaW1Qw44bJkt5NOpGCTQychTI4gqRJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
انتقاد شدید عباس عراقچی از صداوسیما: صداوسیما مصاحبه‌های بین‌المللی من و استقبال مردم عراق را پخش نمی‌کند، اما شعار «مرگ بر سازشگر» و روایت‌های منفی را برجسته می‌کند؛ گاهی با خود می‌گویم شاید اسرائیلی‌ها در این روند نفوذ کرده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101753" target="_blank">📅 12:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101752">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGJMsznCL54cPwDtrvn7bIUXNeEwVeA19AlnHcpOc_TXiBEaa0CbjhQamg8qywOdL9kuaPl002oEf_tTK6NpT_tAFbRP5L-pCgXNz9OfFWBDzpCsDVzWZXH9yBI7H2G9J6cdX1bwn72X_atO8o9_9uUiUJsZwjPPifXORmfeDnqr3gnE6ICvEP9kzil_D_KeROi0Bo39uMFmZFKvRhAllT8GUcqFZr3twUhQeuD6erkD-W-j_i6UG6PxhZWiHWrYtjffm6Xp0dQ_-O2o6GWTw609UN8hWd0V0K7f8lkGYSv1ZUvPuE77vAiC7jbs3UJ4i3_ximc4xmdH_k36DCpoPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
اینترمیلان تماس اولیه با نمایندگان کریستین رومرو برقرار کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101752" target="_blank">📅 12:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101749">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hjulrHYsZlXYhj6WSfnceD-Mg_JamFmTSitI0zDqe9rdio0arXh97GpM8X-bmMLQGXgdFKRFdL1l01pi6To-KEH8CmWUaNhZrhG0VF28IlNv5H2wlsxcECZ-8cRZ5YGnx-zZF3yeDUdKxhCDKSz8PLTxPA8QVaFhYWh1nQMdu4cyKCB4EAosCCpBSOA6Kdu8Wzpm2KfOcjbyd-U5n3NPPd6cxtLJ_wWxwxjF3oRwN9V8Xq4W0Eo68w-cNTMOWlm98mMIJA8VJQhDka6g7j3Ap5J61PWtqQUTcTF-bwnF5TUsULZVUEB386VEB-DxSmyxgBcmtcaiBiQ3mfr8DFsIOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DkecjFBRQUFcCygpkhmJA7jFIkRIjEt16W2WCaMu_wvwvDUQD8jGx75-jUYGEvzRDExv-bQaUHTi-ZK3P4rCYSdw4sLGxx5F_WiaD8hwkTafCtEGyJkdnWsHotB6_sVHpgUS4RjFCpWu_wrTB0QOV3y2TwRgfU2uhTQ4oSdkX50-hEUOiMfgrD_PBTtRTgykz2qWNqjFlgF4Sg5K-K1D2lD_P5Vln_h32VncswlkCXeW-Zit1g22mAvWiOHJqpIRxKayh5ScxGs93J_M9fDV_ZnLktyjq6TGD909ViXWEsQ_fgC0_U3ZTNp1hZH07klPTXGJnJdGUcIwmrSs7HscAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XVUuGSKFZrw4KHgyI1RN7gmb873eXLfcSsm7nNh-KwJxdJRQLWO5FBm9pE_moudPquAhNDP8yZvGLg5KAXwa0UoEQMz3bRfhTpPEA22Q6cemuvP93lVR73kDw_tDG1nJ_hdFa_2hca_Xt1F-fsEXymuieKThkCpcheCcIhRp9MCBD77O_eq58exxj4mSvS7kD8Tn6_s85xtUq9uoIbLkVaFkKEiZIahpfgaGM6SibUZIqvdfl-KLZ5__xiH_lTvwjza9HL3YUmx-EWG6QdQ1g1Wj3isc64-1CiUUwJbi5AAfx876pFn1Ij1mB5uTyvy1Qyng7roABwQxJRkH2wxIIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
⚫️
کیت‌دوم فصل‌آینده باشگاه نیوکاسل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101749" target="_blank">📅 12:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101748">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joLEAiJz5QsZtOxNU9p9U9ZJSIYEEa2DRA0ZYE7Mbx3y1kXZcAwmfIYva_gdM3DCLvJ28p1RbNRpcRlyaIxGmVsioEGknIwb_AJHUs1XKZgXyISF3PpNzWYsen1kw7nGWLHV6g10bPBeiWIpiS356ak7uLiULolhezrKhU0l5a5r8odpH-sQi_EsbTiOYMQxhsWMfKO6X-FuaaOCPqZupdMSV_xAcRVxjlheNDhRB2wbtJeqVqmYNMj7dgAtoe2QLGT40UvlHDmdS1n8CJgmlj6lYEUOPfKHrorNqn9077e6SNF75mxDcjjdjFVQKxmAVqwXjC3-JoBm08EFCTfwJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
لاگاتزتا: فنرباغچه ترکیه با ارائه پیشنهادی به ارزش ۴۰ میلیون یورو بدنبال جذب رافائل‌لیائو ستاره میلان است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101748" target="_blank">📅 11:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101744">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uqakz_D3lKa_I7YoZbG3GBxtKNflSoNpl8BTTC-Pgz6-0_dY003SXpStGesF7atXtI0dwOb73VLvh_Cj95e5OruFW1XOx_bsaEMiDNvmzleq4f3I-s21Hvcocif8sH_5-gxCyA5NUCPj_xYqibATUmGVElzCIwfJpoIKpVDT2U73Jej7qWcmFzsA09d8D_mfNHO3x9u-0Bzx5Si_1o71AHIHnZGBL6X4WYXXF4NlvkCB7hO0pQSjo7JutKNevLixSGLRC6elAsXpgrWGbQ1TJVFAt5NE_PuBSP_ES6dWg92L2S1IdA13cz53tEEw-zM2dRUNVTpwypAGbtCewUiTag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eVUct-mBOpmPwBMqmIWFiKaZ_waODnt3P7l4JIEesYJ15zJEJM5j3gRIU8Bm0PMyYQe730EyAJUYxbFK9Mgh83PMBGo7K4UlFEdchpykNSHS_Tbi01XEQNsvV1p8PGJyyqctU_G1VQZJSuDuRQIqkNxyZX419lHvOAWlRMWtfDPQz4H1kWdHzyF5U28denpjXtDmJB7FsvGESSW_w5wnJLFhs3yEI52qgThINPlNXzSBiRP5LAzMYaFmirKISUdDSR8-U3Lpv0rOs1ttSZLuJlTFD-1rkPvgt082RZDR1IqB3Vtr1HaZMTbnSxTdfaZEEsZXYPcjieDJZZdT-OZt_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vG2EOGD4RZmih0RTcpRrHnDqTDX9amtyPiJ_kNB04k35GWprt5d6e9EwIi1hkHq4TxIl0QX06iLtD8SMLLwx6I-9tClMIye5Go_o7R4PON7DYLd-e_BMG4gipyRZj1qbQ6X-hQzNEBGIvJeNmJltvW4YFbrfSR5m1__V7jOw8NSs-5l21QusHigiMTNNbTZ4Li_xI9WurfJyf-LPL0DpyWQ0LHjSu1IrM2-B4E4yBIS3Eb92xqxlVD08QDyWxDy8mnB6pZPaAqLB-SoMzq9JJm3rA8ddr3sFW8FgE8msCSS7zb3TrUmpfSE8cm6msnrtNDHkMNHFOl7GHT9PxHNWVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم فصل‌آینده باشگاه آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101744" target="_blank">📅 11:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101743">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0b08e15d.mp4?token=Fdz70HY6qNxtGHT7y6WscJ1V74CVl_9gs_wtoQpE6cDhWAioIQwbCidw05VCyy0M25paTUtKo-EcNBOymBB2ghzVTIWmSH69SkkZVykYWz154DQ9l8B03AJD3W95Bg5d_cL1wlT9ZE9jOQqqlQoSy-jMMYw9lzTFejFiG5QEnxHkgxT1LQwOrT22KufdhDRkXyN235Zddtfw7-4s0wK-AYh7jhUdiVB868luUwL4JJhqSG64n9YprzMMi5NMAIT1_hzR6BnVpF9zXVz3bPkEcGWl_-rP_en0IV-py_zRkVnsrj1qhLiVGW7wKDlNZqp0LdT4Qe25lVPDbe5hO7CCVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0b08e15d.mp4?token=Fdz70HY6qNxtGHT7y6WscJ1V74CVl_9gs_wtoQpE6cDhWAioIQwbCidw05VCyy0M25paTUtKo-EcNBOymBB2ghzVTIWmSH69SkkZVykYWz154DQ9l8B03AJD3W95Bg5d_cL1wlT9ZE9jOQqqlQoSy-jMMYw9lzTFejFiG5QEnxHkgxT1LQwOrT22KufdhDRkXyN235Zddtfw7-4s0wK-AYh7jhUdiVB868luUwL4JJhqSG64n9YprzMMi5NMAIT1_hzR6BnVpF9zXVz3bPkEcGWl_-rP_en0IV-py_zRkVnsrj1qhLiVGW7wKDlNZqp0LdT4Qe25lVPDbe5hO7CCVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
کاپیتانِ اسپانیا در رویای پیوستن به رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101743" target="_blank">📅 11:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101742">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc95b900a9.mp4?token=iPbDNO07mKJCzUbc3NSXoC-WIK24SIAhEx1vTtVpW5X-xlZzDayZAqKNkd_UnNKw9IaZU3jRflJBU_ruHMoctRSVGcLJOrWjJQkxlfcOsm6G0bJ_h4gCXZpPU_ahijfNE1HLNB7hyyIQQmWuG6-Sw5vuppw_TgM-Mr2aCqHXquOwigmnxP4S5bEcWMwyTiHe27oXF-Qs9u_RMGPhxCVlqD_eC-cc4Ksw0_HCqmtlE6SB7BPYrmSo4BXkS0gVmITLG8AJwDF0zdmpvxptotJb0XovUqP7rFwGNONF8pbDDjtcVolRYbADw-EoacBBcikFry-DHJLuROqg_gyJ1h8H4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc95b900a9.mp4?token=iPbDNO07mKJCzUbc3NSXoC-WIK24SIAhEx1vTtVpW5X-xlZzDayZAqKNkd_UnNKw9IaZU3jRflJBU_ruHMoctRSVGcLJOrWjJQkxlfcOsm6G0bJ_h4gCXZpPU_ahijfNE1HLNB7hyyIQQmWuG6-Sw5vuppw_TgM-Mr2aCqHXquOwigmnxP4S5bEcWMwyTiHe27oXF-Qs9u_RMGPhxCVlqD_eC-cc4Ksw0_HCqmtlE6SB7BPYrmSo4BXkS0gVmITLG8AJwDF0zdmpvxptotJb0XovUqP7rFwGNONF8pbDDjtcVolRYbADw-EoacBBcikFry-DHJLuROqg_gyJ1h8H4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⭐️
🇪🇸
زوج طلایی اینیستا و لیونل‌مسی که از بهترین ترکیب‌های تاریخ فوتبال یاد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101742" target="_blank">📅 11:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101734">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TMeOXUH9Mt301bKM9-1fgbyD_l2Rj95Ba4ETiPlIW3mRhaBg0JPwqSa9qqFixWAhbGmkbyXeHlJtmcjMoSgM4q59UDJT4GW7z3o2DquLSw33dnvopRvBsalKgtkcdKGXQgfZvnjVlPHMLfp56fIegIwW6Y3Ey5yh1FHy_7ykbQvjv2FnoZS_ZHhOscmO-l1j4paFqhvq7qS84T14b21M0nGYnhm9iuvBosjVRjaGkbqCYlUqX3_3RBStxSjb-7P7whz_XIuB-VIjL85HnWw_6wwkNcDIBN0-MWioTWkNjAjL1C4DHjdmtVQbew_j1do7GfUdC2KOZr29JbjUHN2wew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZtSEYxiyouiM4mi0EgL2MfYG7W9irqSN9_lPdVagXeJEvIAvxaXj5-2SNHZBHTfQcaSzEFrs3RYjeI2t-0qw90m-ZlocoDmFRykGPjkcMKBhzuq1nObPppgut0HWaTH2Z63DjZxo_9lzCTDGWeuEaGSsTPoeJTqqbCGXl4JBdmd0x5jJ8SWNgsciMTFM_qFhianQT36AHxEBy935G_4wBKRcRwHfYo8ui9_N8u0z70kORcFv8MP-5S300ZEaafiga3hQA8H4n1pwy3aUK1i-xh6O5s3oxhsl-DUB-_Tw29bqG30ICKJxCo8AwNQkhQMFz0-ULjC3ve0GJLE4cIbrYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mAGtr4lLJqhNiqLpaTnwY7-r1S7hfZfHQ7o1sJFeYkhQ8dnjMiX0Bk44mAKZgAEpxqzut68JYcYoAZcuCWtA3zY9xBBJeg3ACxWGTgGP48Kj459DVKLLZ1jcnTbp6Szb0Tx_l2jpnOuk7xbUwqXZ7b2aeJj9Jiy7iLi8sWDyLK83EGK8fxJqaVYFDkRWMyHxU0Bjnxa9k_g56NQicmMKc680hOefCB31cS0ku2M8nc0OczVNwwX7VrcA1u6Moteqkpz2IpqyRR4MBvMR0JxwQp8GeRLvMRyFWwvWh16euHH6TITUmnP5JKmVLogUaVgoqF7NB_dBGZOvdgOfXNlsRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nP5ghnSXexHDB4qeebdd0Lg7lHPLeI4FqYK-spprhFFfB48GP99hGlSeNuJVrRPJTNQloXgIRBHM4gB13RNjx2rrAgr6oCrEB932lWVma4gFKePKM1AzakkFey2KeN_v40BNo5U4PqddQrKeFKC9eFRV1qr0vodSOW5JSxcOUyfKzRal2LIBuor4l4nl2JSS4qpkLS0CVF1fn00r-iESF78IgYsCRBH-6TCqOci-4fQBjP0EsRBod8P2OWChOXGlWcK9cX2efeVWt9R9BL-Cj8IrYPz8e_VE1OvkPWaPCyuGeAKTrmnsaO1HADRGc-jtjgVl1Nqn-I5nbg5w83zu6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AzDb1ezjEtZ5NZEmlGNjLlhCsvBjDYEc014S6EXfnY6A1eDmumXbRdA2nSh0Lq-GX1oU9PHFhVXzMNWlG8T-cfT0hHa-sf5BpgaTIMlqhZr1wygDVh3opoYCVFUvRYdWZ1Ywes6OTBqyd4BsQPuHlG8L-z-w-p6GLjGArSd8N7F83YIqsU-Hx6c_r_KikdyLPeA_6MeQkcPbeHTh_XlaD3acJ9vrV6qxMBrX9cET7zuJ76J_hW3r3r550HWgvzfUtwRGrnbEHtGpwato2YOfQ_W2ow5pDmTduhjAdp5T4xvKEHjdab_nCv1KZqjr1sWn2csMPtGSasBfSAeFet-BPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DnOHHygwpC8Ud-niZ3qDgMe6Znt33vTFUwFJhZc91VkLnFuyoj7szv2itEcOidY5Xf0eb4mfVdA0ri9mf1iLv1jj_kd1_ck5zjcZ-ZoeEPnl_n7XV3CQQN-xIuUJURx3b8eqRdh-FPBO7f2aBP9ZmM7085DMi5GnFhfbsuXY8k9qbbOdxX0Y-e5Wu9NCaGjVF98OLR-J4k9vz0hC1QiCKqu0WeiAtn8ow5mU3aOijGCkpRdQ-3IfKQdxSc_wr8N2uSjcdEvxJyzYqiGgM5k-45J5kVE6I1mlosKu989XFrwukIW_S3fQbUfFkW-UtAmDT_bH3RvWpmOqVld6lQf8JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q0XxCyj9RgT0xfMRj4CLeY-xseWbo1T0y3ifvverYKVg6zBwCF1KY3tWqj2hZnSsqInTx62eyHQbJWG715cVABrH7To7NXyF-MrvqRvjB_8Ob-GLFEYt6ZmbXfoQKej2AsVU-V54h9TZxd1YzzxW0XtucIPUg_Bzsd9KXfP_J8j2cl_Tlz7tGP_ywmxa0cXXNzQawqqP6GNlZz8Di0nfiwnq0VrZccxoKmlE9-KMy7xwV1ExlH17sPTMCMRJJlCzKPG1kqt-KMVQgUSRklKroW-v1Tj7de-VEOrzPK-L_DunqLw8i-_DdjCjDmtVbQIfnV8m8MHw8kI6iHDA4BFU9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PRXg24x8LSWK_lc0au58xvoy1DWi_1WG1Of9es0kL4R9kEmFQ7u9lDxHnZ1CsLpnWz9_8dWwnFmlYfx5n9YhQRnV5KZJ0_8kUI5An1c2p6ADlWhBOS5ZTXJwgzgqnPjTaWuCshz9MM9mbJeF-rHBy8ppUbpfFmhFzNBeTBp-jTHZzp9lTAU7Lgs7MmDEbMxRzWTwK8F_SFbUjBO6_z9qAaAlzAEQbFikKnQdwLl_HsnyQBdu952fwLz2Rnw8geDHqUrVdWUJnyu2wisGdvx2uItBtq_FYO-WvSlsnwyf8spTBluUX590MgQz2EWuK3idXlHrFSrFPfRSIRYqfYP62w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔥
کیت دوم فصل ۲۰۲۶/۲۷ بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101734" target="_blank">📅 10:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101733">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae0f2a4c9d.mp4?token=BvXZbLz16EeU9K1zIZY1BTPBk9r8Gj2HxRMn-BA3ZSZ7GJZTv21IYXiW7ZqCU2N-MP__z2mEXOQGNvCofVzNpKciHnTHgaT7N7CeS6c-kB-aPkbflQdOWHli1_YyFMnEE1DyNiWx-oAgFwbKQJDPrKddlZJCZ0GPoezbmhXy5-UE3Mknz1Qd-H1-QtVLBXmMwMaglfUYm7F6duCWUvKMPnpc0QM7B4FUcfGiiI3nlXFsjKe8Ac091n2nry5FaHuABhhK7SxKqehRr1JwUEMpEl7PU5BjeYsOIbV2CFa97twpkNG8Iqm2T1DHZigGV4iY5V01RN7cFJPeTh9g9ZLWJISScR4I7WElCZjMasIIYk2iwg8QGK50jmVM9Rrpsty99XvSj9e5O4IkwyRzTMnG2a7cnXYg2zCD3bjSUCV8xF0yiR4hkMnm0ADASMOJXKTGcw545jKMW3AEJQocMW7vCWRgGGQ8xQh1oqtdJPNycbEsfszXOTlIn1dvEqkuopDMV4JZIUwhKfwn4-SACFJiwCUPuzbxJi9WgfR5Me4NrwW_T-S7p2waQrblRlbm5N1qi2N2ljyHbVy1CEJ8KvmLDm2HFtu3DkSuzxmALcTPKsMP2Lg2nH-VCGfZDFFqsaiQneyhXV5EWEGlWQG2-Mlxvm7yHj1bg0x3Xl0QtzDWRtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae0f2a4c9d.mp4?token=BvXZbLz16EeU9K1zIZY1BTPBk9r8Gj2HxRMn-BA3ZSZ7GJZTv21IYXiW7ZqCU2N-MP__z2mEXOQGNvCofVzNpKciHnTHgaT7N7CeS6c-kB-aPkbflQdOWHli1_YyFMnEE1DyNiWx-oAgFwbKQJDPrKddlZJCZ0GPoezbmhXy5-UE3Mknz1Qd-H1-QtVLBXmMwMaglfUYm7F6duCWUvKMPnpc0QM7B4FUcfGiiI3nlXFsjKe8Ac091n2nry5FaHuABhhK7SxKqehRr1JwUEMpEl7PU5BjeYsOIbV2CFa97twpkNG8Iqm2T1DHZigGV4iY5V01RN7cFJPeTh9g9ZLWJISScR4I7WElCZjMasIIYk2iwg8QGK50jmVM9Rrpsty99XvSj9e5O4IkwyRzTMnG2a7cnXYg2zCD3bjSUCV8xF0yiR4hkMnm0ADASMOJXKTGcw545jKMW3AEJQocMW7vCWRgGGQ8xQh1oqtdJPNycbEsfszXOTlIn1dvEqkuopDMV4JZIUwhKfwn4-SACFJiwCUPuzbxJi9WgfR5Me4NrwW_T-S7p2waQrblRlbm5N1qi2N2ljyHbVy1CEJ8KvmLDm2HFtu3DkSuzxmALcTPKsMP2Lg2nH-VCGfZDFFqsaiQneyhXV5EWEGlWQG2-Mlxvm7yHj1bg0x3Xl0QtzDWRtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏆
تمامی‌گل‌های کیلیان امباپه در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101733" target="_blank">📅 10:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101732">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eabdc39afc.mp4?token=RpmhVgoydP5OsE4GRTlgIWPd5kS0BmcU7pziNhLrzmycRVZW7WlqILJ9qWgPc62IbIvJT_8wuTRpM633PVulx3jH_XQ02LJjmbDNqWrNscr9p8YhyB7Cwmsah-dn3XXr-eXdZO7IcR8iDmWLH3JEHk4b2s_jHUnodgRzkyEZXWjVEViazjUUwwl2XsMHk8rMCI1vDMCjA2o6sdqrzdDoIPa3XAirzyC1c_HYooP2JwjtcSfJSV0IlO_VT_NCKE0O3q4xhkxUnEo5_MCowPNqQEs_zp-uJp8ziXqQETzDGAGDvC1jCRjI4zTsEMdHbQNS6tZG-LJM7u2nzCPviaEW2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eabdc39afc.mp4?token=RpmhVgoydP5OsE4GRTlgIWPd5kS0BmcU7pziNhLrzmycRVZW7WlqILJ9qWgPc62IbIvJT_8wuTRpM633PVulx3jH_XQ02LJjmbDNqWrNscr9p8YhyB7Cwmsah-dn3XXr-eXdZO7IcR8iDmWLH3JEHk4b2s_jHUnodgRzkyEZXWjVEViazjUUwwl2XsMHk8rMCI1vDMCjA2o6sdqrzdDoIPa3XAirzyC1c_HYooP2JwjtcSfJSV0IlO_VT_NCKE0O3q4xhkxUnEo5_MCowPNqQEs_zp-uJp8ziXqQETzDGAGDvC1jCRjI4zTsEMdHbQNS6tZG-LJM7u2nzCPviaEW2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
تفسیر نام اتحاد کلبا توسط مهدی‌قایدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101732" target="_blank">📅 10:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101731">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e10a696be7.mp4?token=aR5rAnnbg82NKCAqtbNE8IBiqUuxi1hbRCQTyCEPTMiEywx96__O16lvcMuchxZUERYO-G6V4OdizbFayR2vN0ODHFh9TCaal66fnXfBYo__mPYI90cKSqWTKlJrB3TPD4FPLCNIL7iNWR5idk9U8-c2kADExv8VhTrcg84W3kUCR_YEyzQkKjIZqdsiktfy-yVdfLWj15bPyXXqxg6JL2nPiQPSV5QkdnRYGbPaYKrKE9hR8DSyBASVFI0g-itCIVyBPhknn_4xFLtbcGaZcPCEyzjWj2Y8am-4_PCM8EBUlVemQ_NhYlrxuFdLg-aSrz1OcvjKqqoZZ38D3C7rxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e10a696be7.mp4?token=aR5rAnnbg82NKCAqtbNE8IBiqUuxi1hbRCQTyCEPTMiEywx96__O16lvcMuchxZUERYO-G6V4OdizbFayR2vN0ODHFh9TCaal66fnXfBYo__mPYI90cKSqWTKlJrB3TPD4FPLCNIL7iNWR5idk9U8-c2kADExv8VhTrcg84W3kUCR_YEyzQkKjIZqdsiktfy-yVdfLWj15bPyXXqxg6JL2nPiQPSV5QkdnRYGbPaYKrKE9hR8DSyBASVFI0g-itCIVyBPhknn_4xFLtbcGaZcPCEyzjWj2Y8am-4_PCM8EBUlVemQ_NhYlrxuFdLg-aSrz1OcvjKqqoZZ38D3C7rxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇦🇷
صحبت‌های یک‌آخوند حکومتی درباره عدم‌قهرمانی آرژانتین در جام‌جهانی!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101731" target="_blank">📅 10:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101729">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IhEp8Ki-CAcHt-pKNkMLJQzDNTlQ-qT2jcKY_JoRhk2LH1PSjRH4bTWj9c4A8iURDzF4qQzPZs6Fo7VHvhZ8GdR0T_xGxrQqxqi2inJugZ-5kCzBh3QeWlMzPmZiFoZIjsTSMhq5xrJtJnBC3dIOUTuPwtaQ83Gdo6la8s49bP1yarfimY2dbHBKGKIVEFjEvgI4BiaX12q0Nf91s7uhXWveygsCR6lV_YeitCGXUnBiEXqEDc71SwdkYsQyStMVZOfmKSkyzjUSlqTdlWSasCcAsPx5WxrVcIJkKI7BmyTAS5H_0HsRlvn1wBve5wFwzjcdD_vjdH7FLt1JzYE8bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SKrTbF5J0j-XGohOgaCFxb8_2lC0kDKEOOPpmVrllHcMCaxf2yA8tJvl9Rx68_WTujCnj3xTvO15UpJCLd59N2Ujc8hNkS9GJE98Ju-Tsqo2IH-6iKYHv8dpDm3QeSHViCVBEBLXvGFmo-7eC5sRPIWV9cavjk1QRenR6gO6lFLrd4b1f0qX9oPTf2ZbsmHsPYjbNcZIe83ttMuOmb0NUN7QLN0YjiJybvah59EEYz0Rc1sUFIkWvs2YGkghjMteKH6bLQVtkyy_DsNhkPrXyrhQpZyGyPYcCKY_P6XIa4wA6e3OM_lxPuiia_3D2DTPpl6Sw6pbBHq3Gluob5A9PA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفته میشه لامین یامال، دو هفته پیش به دوست دخترش یک خودروی مرسدس کابریو به ارزش ۹۰۰,۰۰۰ دلار هدیه داده
‼️
این دو نفر در حین خرید خودرو با هم دیده شدند و عجیبه که این هدیه در ابتدای رابطه اونا داده شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101729" target="_blank">📅 09:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101728">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLh0NUfxEVukx-L4gx-dofyt63sznxaqtYPvYKCcd84oRcAl6MsUbNmqYdP45ScFzzVa6GM0xt_1kh1jcu-XPdjV3nCpSO_e0ns2GrRwUOPIURLgL0k6Tok80kdtrtesXtknT_-pe11sLKvSUtoNEkidHYuQz_0GfzcHfzOOTzyCGb89g_LmqpDPrLmWZz2CWMNY65FM4AOZiO2kf-W7OMeQ9rKYCYs8wfklFYzz7Vwp-qeLU68uxav8sKK05swHz7g5XrGco6ditSTD_rrHIaoyrKAaI7TUeG10DQxwrDPly58axxfWZPcQ91LR6fHLZzo4eu8QWQxk0npcKUcMLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇦🇷
پاردس: آخرین بازی ملی لیونل‌مسی مقابل اسپانیا بود و این بازیکن قصدی برای ادامه دادن نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101728" target="_blank">📅 09:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101727">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnKGrJOsYKvzYudLtQW5aXsI0gPAcLn33CW1sYXcpJI4O2gmJD864QJr-Ob8hqcFGkexzru3dqO3zOE7kSzBl_HgRqTgbrCEdxnpwwH2IVvAWJvcgELTuthNY7lpcN2MCQEGSi5umerq-sfFfIMy73ZgQktxzeo0QnUgTYLlGtS_qroEV5wbQ4ysMFwXLi62jP9aPB1HdOIpYXEmZt7cBvqpbthVOo53n-b4ghiOsBKUFOaOJOy_BSyu7gwUiEo0qCeBAaj_-KpBYtIVbgmzpAwtjiJ3OnUsF5sNeoAAISnZHBUujSL2BSeLtWv72Jt2922I9q0U_9eELdDcDLq8EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔻
الکس فرگوسن: "آیا منچسترسیتی از منچستریونایتد پیشی خواهد گرفت؟ در طول عمر من، این اتفاق هرگز نخواهد افتاد."
🔵
🔺
منچسترسیتی از زمان بازنشستگی او در سال 2013، در هر فصل، جایگاه بهتری نسبت به منچستریونایتد کسب کرده است
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101727" target="_blank">📅 09:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101726">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4ISksCD0m1N_tBSaZxlnTg0hbFpnydbq77BwkeeSpKkMhKsTCs0K621t809eNp8r9cZHb96x9vuRf0D-CQdHbHzlJqMZ1GTTtHp_gw5cKBccU0C9VKYgf_A_Y2GdOy2YJeUWGdvTnxt9RWW3u4EIu2wbfvKlLdPUIaolbbbA8sa3k3-klk7X6jPglnQ7BVfNwkKlB1GOEmfOPtfeHSKiDKC3xpZUHnLGXAPrE4QywDHCx_md2sDBAJdKFFDRfEtliBYbeIdZMprQHPZh-FAXt7RULENaFCSLLUdOegB7P0FeJcvmTu3X9xyAQr55pc_mHfMnLyZ8SQwfEsc5hvvJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏟
✅
تمامی ورزشگاه‌های میزبان یورو ۲۰۲۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101726" target="_blank">📅 09:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101725">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6C2Gietxg-k6U_kTV4jSKYzXB1o6MsJKtqclQYOcw0whdbGRz4R_hn7lGnkjTVPIc9A785bwpPLNCt2bXEbcXf83-FiWgR7WyFCLyzXR4-edf0T4dmFWABdSxpY5q22KxTKJNKZxng5FvFfwBBsNuy890v6FhbwOdxIKkd2vc-US89SSVtXXwqS2ntzGz0KowW49seMVRzM0l9zrToDjihn0t8UQUatfs3ckSiolAztxrEcvt3GSPuaFmsuA2eP3Swuq4RJAP8vX9pUCHgQF94Pfkn1vXpvxVmSINMmEd-W5AVX9VQobxQOeB40TjFsxVzrGhv9NS0bSUJaawc6ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
👀
کیپ ورد در بازی مرحله گروهی خودش مقابل اسپانیا، 0.28 موقعیت گلزنی (xG) ثبت کرد.
‼️
جالبه بدونید، فرانسه و آرژانتین هم در مرحله نیمه‌نهایی و فینال مقابل اسپانیا به صورت میانگین (Xg) 0.28 رو ثبت کردند.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101725" target="_blank">📅 08:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101724">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bric13FugOls8tTAsiF6bUlbt04DCGAiLLF5Ht7lSqZRub7JrcNu_iwBGW4dVAKN5ud_7Y9Wre9PWUhH4DtYPNhuNT7xRaHa_Way_EoiQj_g9gBpxJEzsaPcYXvgp0vNxKqm6xTG87Nrl8OZfk0IpMRAaPR1J2MFPkNvO9Y7rJeNaYxkoBIF9hz2J_qD4E9wwdItzYcwV0e8YYfz4De8-TjSGL1ataWn511xO0c3fu45vUg71Z4VPasNuwfYa67puXasiAVPDYEgw7uJ4KHqjkB5wLEiwoUhgxw8jzqR-25httldwfrvi6Po6sg61siGmTMoykJzJ6dDKK-YIxTwvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🇫🇷
آلمان و فرانسه میخوان درخواست میزبانی مشترک جام جهانی ۲۰۳۸ رو ارائه کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101724" target="_blank">📅 08:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101723">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-lj2bAeBVcMIk0qvPUir0urIC7Ns3QttmB00yfPQ2mD3JEAF3qATpsg3OqK81WNw0RU0aUt6_sSkdTGEg7oqtDz2vOIxxtNufw3zFYqD-WBwZDU2gMf1fN_f41eDf00V795d6WUhrWUflY6X_cE_17sE9IonkeHudXToUaL4UdWNvGgRgdVL0MHWacKaVoPcHkchAxwn9OTlRLe-pOaz884CoqI1CTSaauubYNcNu4BV9I0d6k775y7pFz6aqTqIZdk8fPUOr_1gi_4uxhsSqBVonj56nw9IY2-xsb8sexC4qwhVf3WRg8pUNNV5C14URSEErwic0w7c_kEbuQBig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#
فکت
؛
پشماتون بریزه که بیشترین مبلغی که آرسنال از فروش یک بازیکن تو تاریخش درآمدزایی کرده 35 میلیون یورو بوده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/101723" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
