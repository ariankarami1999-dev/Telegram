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
<img src="https://cdn4.telesco.pe/file/YY-4eU9szcio3jYsSIK7XMye_jOm4spUPlrh53aQYlFe7ejE6st-wmMG3t7zWAPtrD6i5JUQsT6RtKzCuNhTW363kHclFjTFCoW4I-91UWM-xGK3m0MpXAOXtjqpBTo_feooY1CC_yyLNhhThs6nujWoybJqdUClhDqk8B-ujRkXiGFTFAiLg7b6xHWIHy5R4z5HRuYgqNl39ptnGxBjWCeG-27lynKW2JWmYWUInte4CMsQTTrpAX2IswXKc-1qWoTBqtp50Ci3mgiL9uy_rXsovP4Mv_gqP6PYYZWlrdl8csm2bclFJv9boB6aAacz-bal6nPZtMEqx-MzM4_FeA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 136K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 17:48:11</div>
<hr>

<div class="tg-post" id="msg-69467">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04343db3da.mp4?token=fpd0YViaD0r26dMOaAuxTjyy9JxjWQpiMInIRAyE-DwDIde3loID_2NCrS12FdGldxD5SFQTdWnR0P6swY7xN1IqB_rXHzz9SyR2bHs_b2bAsoftsSPVjQvAFCwR_5sXStaqiULHqcR3CgdPgX_ovHd5iBxFJ9HSQCzc2qSkZcrIXDw8WEMMjlwwah8zAoFEFyQLfzagRKKj4ac3D6oMChXxkUz4-LCve0clW_Jh0ca-744qHNspAm6u1BiiyRgoIBbC9RD2o5QEY2rDiqjvuIoL43ZPx_sRroY5gUjcMrm7e_gn8BYuU3nk-nKPbXf-DhUJDY7simNi_2-g2s8XOkdp5WNtAmf29MRg8ZxeyEnX8g07iNH60U0_7tPMvO0FWyfPjrHOHIdsJVL3Ebgxn6gzuDysAAHlaFcLSwFqouyW2BMzwTzJNOoXcHYxvi-3VeOi1uHEjzmeLUqepB0XN1pEwFqIcFdxoiT3vaM1IbvcuOdQAXIfTOpEwgGooRM7Zbxbb3v3QKND1mE-20BDlYqy98lzhHWdzzwTpJfKaZM8m6As9JGmICMPtBj9t04H4PDrMy4RnMmoKn_liDkhq7OhgW8sSyWA2wFC2ahPF888kwluAljgXYT_dDvRO_SQ1ljrGbzgf0VovBHQJnrKGudGqDQDVG8bpKl2CL4eTQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04343db3da.mp4?token=fpd0YViaD0r26dMOaAuxTjyy9JxjWQpiMInIRAyE-DwDIde3loID_2NCrS12FdGldxD5SFQTdWnR0P6swY7xN1IqB_rXHzz9SyR2bHs_b2bAsoftsSPVjQvAFCwR_5sXStaqiULHqcR3CgdPgX_ovHd5iBxFJ9HSQCzc2qSkZcrIXDw8WEMMjlwwah8zAoFEFyQLfzagRKKj4ac3D6oMChXxkUz4-LCve0clW_Jh0ca-744qHNspAm6u1BiiyRgoIBbC9RD2o5QEY2rDiqjvuIoL43ZPx_sRroY5gUjcMrm7e_gn8BYuU3nk-nKPbXf-DhUJDY7simNi_2-g2s8XOkdp5WNtAmf29MRg8ZxeyEnX8g07iNH60U0_7tPMvO0FWyfPjrHOHIdsJVL3Ebgxn6gzuDysAAHlaFcLSwFqouyW2BMzwTzJNOoXcHYxvi-3VeOi1uHEjzmeLUqepB0XN1pEwFqIcFdxoiT3vaM1IbvcuOdQAXIfTOpEwgGooRM7Zbxbb3v3QKND1mE-20BDlYqy98lzhHWdzzwTpJfKaZM8m6As9JGmICMPtBj9t04H4PDrMy4RnMmoKn_liDkhq7OhgW8sSyWA2wFC2ahPF888kwluAljgXYT_dDvRO_SQ1ljrGbzgf0VovBHQJnrKGudGqDQDVG8bpKl2CL4eTQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو ای از یک طرفدار حکومت که میخاد ترامپ رو بکشه:
میرم خون رهبرمو از ترامپ بگیرم یه دهنی ازش سرویس بکنم از یادش نره
از لحاظ دفاعی یا هجومی همه جوره دهن ترامپ رو میارم پایین
حرکت های رزمی‌شو ببینید فقط
😳
@News_Hut</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/news_hut/69467" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69466">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEP1e1phef8bjK2_8JSbUrwIUou7ZRtCRZ7vhFzRGU1c0kzsJFeZVHcCq4xUCIhitUjOii-NbT7b_p64lDqNHgYZADWXUaIOaJyHChejy8mqS6a7Da01JP5V--KaAOga4MHnR84sqVbP5wvLbgJoeBD1NRowYqCocnW9DFW-O2bdzCVwN9bckoYzLms7OLzzaXXRE4Qr23qbTNnmA-hxlnnZq0i-R1lcv97t0LI2zT5u9t7TH_F5HT3YFS1JH-b2a_Sb4rzvCQMMIj-7bJk6zqfjWccz5zaxE9s788-V0ewcIDu3-XaS1GEl7Vu7xCVL9FX5auY8ASITWxKGg64_Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛المیادین به نقل از یک منبع ایرانی:
ایران در پاسخ به آخرین پیشنهاد آمریکا، با بازگشایی تنگه هرمز تا پیش از پایان کامل جنگ مخالفت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/news_hut/69466" target="_blank">📅 16:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69465">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwH2G1Ia-eVL17uC9sfnHZ-by5nX_-Np6adpyoIS7aKYDu0dqrLFZsSeSDiPRxM2T9ykhAeVYX-CWD2cNaVs8F8Ym3arh3TvTX6kLk4hcuLvVDWnZNaNxApHmEED5ipn9TqiIsI1IRzlthvytAvuDlG5lZxKpnk4uDCG7jz36e72CqI-YTV7iiVtnTDoCJgRbIeTO3cnNGXy9B2NVmUKS7ygR32GQZdiuFQfaWuBzsmI0lWwIbFXZM4vUWndIUY9Mor2mIdoGiyu0PQOpggIcB9K2iDEhE68ZFJm7umzyFax92kJobJbeY3n2hHU5LcSW3CVZp7JfBkvzfK2EAKrag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست میانگین IQ کشورهای مختلف تو سال 2026 هم منتشر شد
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/news_hut/69465" target="_blank">📅 16:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69464">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/863fff3357.mp4?token=a3G2Lyr9B3VSKVN1cId4oWiaeY3natpKsLRL3-3OsAP8xQ9mwYuC2Hnn2nmJbKOoeGPdqIrsP7DCrkghXpbVA5uIiE1VeooYze_hRsjMpvKz9OphDmiD5PnWZicPoViiqYCOVJJvHiUg_PNcA5Jipcgtgu2xLgfBzW1vQeYytEcPdZGKAGQBgRQxryoWRL_yAcFBl8htVYnbNzPk76KT3_CW9_ZJanXs4BSIrizWJAAL5C561mAY_VLOjOQFjPihIWhartw39jm3cT3C6rUchIBIPFOp3bTNP9R8nS7PLoqlGG3VvIvZAtSkkZs2AwDszoPajuYsDQA2MNr4UkzMuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/863fff3357.mp4?token=a3G2Lyr9B3VSKVN1cId4oWiaeY3natpKsLRL3-3OsAP8xQ9mwYuC2Hnn2nmJbKOoeGPdqIrsP7DCrkghXpbVA5uIiE1VeooYze_hRsjMpvKz9OphDmiD5PnWZicPoViiqYCOVJJvHiUg_PNcA5Jipcgtgu2xLgfBzW1vQeYytEcPdZGKAGQBgRQxryoWRL_yAcFBl8htVYnbNzPk76KT3_CW9_ZJanXs4BSIrizWJAAL5C561mAY_VLOjOQFjPihIWhartw39jm3cT3C6rUchIBIPFOp3bTNP9R8nS7PLoqlGG3VvIvZAtSkkZs2AwDszoPajuYsDQA2MNr4UkzMuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مشهد یه دوره‌ی آموزشی گذاشتن برای افراد بالای 60 سال که توش مبانی اولیه‌ی استفاده از موبایل رو یاد میدن؛
موضوعات آموزش:
آشنایی مقدماتی با برنامه‌ی بله
آشنایی مقدماتی با اینستاگرام
وصل کردن فیلترشکن
ارسال لوکیشن
تماس تصویری
ویرایش متن تو واتساپ و بله
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/69464" target="_blank">📅 15:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69463">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cda203069a.mp4?token=amAzFujkqtaFWjrQDf_-_yA-rkkT5FDudEo1oNATqkwNdjoW6vBZ4eUi31c_SqNVH1gQ7CdT5seusrix8FWYClusmre3SAEQsJOMNwEgfDTF1KdwPrLu84HwPt8OKBExdiUljvf5jO0Xe6MWs8AiypxkwoLYri7i8XsdDeXe4VYUiPsk3sxhPqDJVnkct1xqSsefSSiHXNhLqr7EmV8Tat6vJnKv3cjzx5AsJIH1_E3vCXmWBT7rjPfaG7TA1aPxJTljkei41RCVeX0KorJyy6Aeas13qBnglml7FmrN-yPPnW_5DTA_QtlhToL8q-eEcEYPAWKuR_YSx2i3vbFvzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cda203069a.mp4?token=amAzFujkqtaFWjrQDf_-_yA-rkkT5FDudEo1oNATqkwNdjoW6vBZ4eUi31c_SqNVH1gQ7CdT5seusrix8FWYClusmre3SAEQsJOMNwEgfDTF1KdwPrLu84HwPt8OKBExdiUljvf5jO0Xe6MWs8AiypxkwoLYri7i8XsdDeXe4VYUiPsk3sxhPqDJVnkct1xqSsefSSiHXNhLqr7EmV8Tat6vJnKv3cjzx5AsJIH1_E3vCXmWBT7rjPfaG7TA1aPxJTljkei41RCVeX0KorJyy6Aeas13qBnglml7FmrN-yPPnW_5DTA_QtlhToL8q-eEcEYPAWKuR_YSx2i3vbFvzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
میزان شانس بقای جمهوری اسلامی از زبان مراد ویسی:
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/69463" target="_blank">📅 15:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69462">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b293a286.mp4?token=jOp4EzRoxa_ToUclpUrGXmjmWYGmPoMCl2ExupTg61EbRw74hYqbD-ulFnc_p32hXQnTO9o9-s4Fa8Dr0Ua2FzGDsDX8AwGHZE5xb2x0ybUAL42vaIwz7lVauQ30E1lfafOsL2gCS8DD9UYWFz0cMQ5dODieMPLa6V2q8cX-gRbWGNQw6YgD7n8S6UYqjcvfYRmOjZiCsBRMxC6mbHM_nRgIMjjsU0Th4KSp7k1StD3kKfDFRWA9ZtR_Mg5G0LdUozoxEeJWcBbGzF3Ec5BzsFMzA12XaaggwwZ8hOyJ2Wn8Bsoi2XmwBioYEN1RcYyQiGvZ7pmFu_JwXilwEybddg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b293a286.mp4?token=jOp4EzRoxa_ToUclpUrGXmjmWYGmPoMCl2ExupTg61EbRw74hYqbD-ulFnc_p32hXQnTO9o9-s4Fa8Dr0Ua2FzGDsDX8AwGHZE5xb2x0ybUAL42vaIwz7lVauQ30E1lfafOsL2gCS8DD9UYWFz0cMQ5dODieMPLa6V2q8cX-gRbWGNQw6YgD7n8S6UYqjcvfYRmOjZiCsBRMxC6mbHM_nRgIMjjsU0Th4KSp7k1StD3kKfDFRWA9ZtR_Mg5G0LdUozoxEeJWcBbGzF3Ec5BzsFMzA12XaaggwwZ8hOyJ2Wn8Bsoi2XmwBioYEN1RcYyQiGvZ7pmFu_JwXilwEybddg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعترافات عبدالباری عطوان (تحلیلگر سرشناس جهان عرب) رو شنیدید؟ کسی که همیشه به مواضع خاصش معروف بوده، حالا لب به اعتراف باز کرده و از کابوس کشورهای عربی پرده برداشته!
عطوان در تحلیل اخیرش (مارس 2026 )به صراحت میگه:
اگر پسر شاه (شاهزاده رضا پهلوی) به ایران برگرده، با توجه به اتحاد استراتژیکی که با اسرائیل خواهد داشت ،ایران به چنان قدرتی تبدیل میشه که تمام کشورهای عربی منطقه باید جلوی عظمتش زانو بزنند و عملاً به نوکرهای ایران تبدیل میشن!
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/69462" target="_blank">📅 14:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69461">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0c3fd91e0.mp4?token=cA-Eag6gaUCeq76vInKMgi0Rw8z8rZ1NhSsanho9D66z-AM-ydujHkM-BuO9UNyF8bV8ZRW4DKxPz8ThW1-jAhwD1XvaBog2BLXG7Ps3DRKmzeALqmpfipoRFH-M4Ib0Meip2vBQoVrEnHoR-5lKm85b2xE2cjKoAC-f4rp4OBPQRwpQX7sd4VxbL00OPy_n0Bo30C51mzviCRD8oXLDcOPhdgly-BSk0vnxG9jLfm5gXFyxiThQaCF8zEY8H1Jpxjfv-7VYhGFAO8FTYO4WZMZEbtAx0MAt7y0Debzl_hr8qLS-6Zq7lUkIq53A2lJqYpC4Qi5TwavR35S2URvyew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0c3fd91e0.mp4?token=cA-Eag6gaUCeq76vInKMgi0Rw8z8rZ1NhSsanho9D66z-AM-ydujHkM-BuO9UNyF8bV8ZRW4DKxPz8ThW1-jAhwD1XvaBog2BLXG7Ps3DRKmzeALqmpfipoRFH-M4Ib0Meip2vBQoVrEnHoR-5lKm85b2xE2cjKoAC-f4rp4OBPQRwpQX7sd4VxbL00OPy_n0Bo30C51mzviCRD8oXLDcOPhdgly-BSk0vnxG9jLfm5gXFyxiThQaCF8zEY8H1Jpxjfv-7VYhGFAO8FTYO4WZMZEbtAx0MAt7y0Debzl_hr8qLS-6Zq7lUkIq53A2lJqYpC4Qi5TwavR35S2URvyew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
عراقچی داره میره اربعین و ماهم توی تهرانیم.
دوشنبه مذاکره ای نداریم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/69461" target="_blank">📅 13:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69460">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⏺
اکرمی‌نیا، سخنگوی ارتش:
از فرصت تفاهم‌نامه و لحظه‌به‌لحظه آتش‌بس نهایت بهره‌برداری انجام شد
در این مدت، واردات تجهیزات جدید، تعمیر و بازسازی سامانه‌های آسیب‌دیده و همچنین تولید سامانه‌های جدید در دستور کار قرار گرفت.
پهپاد‌های جدیدی که اخیراً از آنها استفاده کردیم نیز حاصل بهره‌گیری از فرصت ایجادشده در دوره آتش‌بس بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/69460" target="_blank">📅 13:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69459">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08375903ec.mp4?token=ctwo5ZKLKIevmxe_9jZ8wV2-2KMPwHcbcBTMI6Hf8ygHQajX_sHBkJBLc4vvaIVPl3ryBXIyoSgKkhS5A02MuDe6FcIRrJvK_A116Iz17EKQHlrZKdkdHz3rz1ZvtwHqc7rAEb3lGVmuYppMnhwU1IxFc39BfKm-SW4sHdZTlOKeaAgVzyNUlhDWOByoW5fQTfGMP7yHUUPENeVzyFuqj1rItmd87df5lhPEiVTMqgSzXELVCNC_GJl79rXWoG0kapltWiUmzvmTyTMa-hnJz-6bQgs1peg-Mtf10s1_Yk-VeQJwepRB-e9P6w7oHvWlTOCBZOaCOJ82dr1lGniHZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08375903ec.mp4?token=ctwo5ZKLKIevmxe_9jZ8wV2-2KMPwHcbcBTMI6Hf8ygHQajX_sHBkJBLc4vvaIVPl3ryBXIyoSgKkhS5A02MuDe6FcIRrJvK_A116Iz17EKQHlrZKdkdHz3rz1ZvtwHqc7rAEb3lGVmuYppMnhwU1IxFc39BfKm-SW4sHdZTlOKeaAgVzyNUlhDWOByoW5fQTfGMP7yHUUPENeVzyFuqj1rItmd87df5lhPEiVTMqgSzXELVCNC_GJl79rXWoG0kapltWiUmzvmTyTMa-hnJz-6bQgs1peg-Mtf10s1_Yk-VeQJwepRB-e9P6w7oHvWlTOCBZOaCOJ82dr1lGniHZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
نیروی تفنگداران دریایی آمریکا ویدیویی از تمرین‌های تیراندازی نیروهای خود منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/69459" target="_blank">📅 12:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69458">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyhlkY8AYq9funs8NOug4tksYtptTfekwBFpUOZwlUjaNEsaVdwRMkeffOk_UrREB1qm5_5dV06QtRpRbvhdmSsH2S2imrcWRFAeFKXN9Whm5hmVT86B7bdrn1IyqtpHpVyK8-m0Qh9fSaSaleSDkiaanCXaH9PB76GMs5N9VIbZ1W77mKkZ3HS2-Pb_HkfQIeTHST2hZ0kpDfyPDq9_UMC74SfwHBRJQdiGICF10Zhk5J-UYCJ1rIQKYo8idGJ5flwDikH3_Zl77hvJJ0yUiKVa71SS_Y4vWuFCrJ_m1SaKP9jGhQE8Xz5Lf9xGFwveBQlFYbyX0pxESdMXc32NVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی، سخنگوی وزارت خارجه:
ما در حال حاضر هیچ‌گونه مذاکره‌ای با ایالات متحده نداریم و مذاکرات با عمان بر دستیابی به توافقی پیرامون عبور ایمن کشتی‌ها از تنگه هرمز متمرکز است.
هدف، تعیین مسیری موقت است که ایمنی کشتیرانی در تنگه هرمز را تضمین کند.
تا زمانی که محاصره دریایی و اقدامات ایالات متحده ادامه داشته باشد، هیچ تحول قابل‌توجهی در وضعیت تنگه هرمز رخ نخواهد داد.
🇮🇷
اسماعیل بقایی، در واکنش به ادعای جلوگیری عربستان سعودی از حمله آمریکا به ایران:
اینکه همه کشورهای منطقه اذعان دارند که از تحولات و شرایط آتی منطقه متأثر  شد، امری مثبت است.
جنگ ایالات متحده علیه ایران، جنگی علیه کل منطقه است.
طی پنج ماه گذشته شاهد بوده‌ایم که حضور ایالات متحده در منطقه، موجب افزایش ناامنی و بی‌ثباتی شده است.
طبیعی است که کشورها برای جلوگیری از تشدید ناامنی تلاش کنند، اما تجربه نشان داده است که هیچ‌چیز جز قدرت و توان بازدارندگی ایران، مانع دشمن نمی‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/69458" target="_blank">📅 12:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69457">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5b3706c487.mp4?token=qg_5UzcXVRCXktS90XlIXy2NHWCEvKXEzlp1dBRMvjuQVJn-JvlZP1366oXK_cD-8gvc2EVLUIfKZVQGydIOIsSle0hXweQOHjDGIhgfddhdbevLL2ldiLE2syAlD07hxFCDjHsh7UWqnT4QPToe7ZDcesWvUBECw6QUXArHYG1VZ2dUKn0-MygOWsh4W-rS1OaXNrt8yP7rtVaQLcRRrFJpOtDZtrlizG5m9NzBDmiaG-kz6SazoMFbtqZ_uUknbBnX-jpziBfrSqfbS6zmvrgHXF6lteFGkKtdKjlsjOvdga-z4-or8RUM5dWoeS0YxS89RRn-De0Ek6Ee0Xx1Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5b3706c487.mp4?token=qg_5UzcXVRCXktS90XlIXy2NHWCEvKXEzlp1dBRMvjuQVJn-JvlZP1366oXK_cD-8gvc2EVLUIfKZVQGydIOIsSle0hXweQOHjDGIhgfddhdbevLL2ldiLE2syAlD07hxFCDjHsh7UWqnT4QPToe7ZDcesWvUBECw6QUXArHYG1VZ2dUKn0-MygOWsh4W-rS1OaXNrt8yP7rtVaQLcRRrFJpOtDZtrlizG5m9NzBDmiaG-kz6SazoMFbtqZ_uUknbBnX-jpziBfrSqfbS6zmvrgHXF6lteFGkKtdKjlsjOvdga-z4-or8RUM5dWoeS0YxS89RRn-De0Ek6Ee0Xx1Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
حمله پهپادی روز گذشته به مرکز لجستیکی عظیم شرکت وایلدبریز (Wildberries) در نزدیکی سامارا.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/69457" target="_blank">📅 11:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69455">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGUpokH7Ij-jtv-FwGsKpEjaEQ2VKd8pWFrmxDhSIODySUd-toCiPCEgxHhd-cSz7zbh5tK3dUbtUL1p6k2B5BOayKmoy8LLhgbqoqrdSGiSzVJ5i635w5K6a6kAGXa84sb2A3WzxMIxqHjK5LuLS21mlSA83aMsGn2YoySGkDuI1bY_xMvMkhnDgmBGVJIoYkllxzcuSCshH1Ct-zDeASshi9rpBVfMFBxIO8evp-m4aXGLvAtNrGBS0rVtzEJMIkYFFF71SVQYreJg9Lkv1a41kOkC-e4PH_VpbxlLQ2OFIChZAIIsHh-BxnNeKEv48XA0Dmv61AvR32PQ5ACUEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429ab83ad5.mp4?token=NfMJxKI86r_p96HQ7FEYIcVj8ecNwbrQWb63spYYUPHYdHxBdYkceppoPPuG7zxRdBR5u2S_OhEgejHu2RdgmQjbf3_3v31VIHd2jHXemwihnpE_onaQhAsiNOlRby5EGGwi0ufKu4MpGmVDu6CqagSMFwITAMyyaPPcuIWDmzwr8cgrfy81z6XF2A24rPvZghuJQABCnFWLL-eOk1oxHbWhMbZOCwxUbIKXkPgkJCBE5dq8SZWykatMCq2PsC8yhbntW08HzMYX5dY881-jLgbU29O3WbKbEgtdD7oZB1vA5LZn783JOKmcYvXvCFA5aM3QUDgv0Yeav-TSqW87GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429ab83ad5.mp4?token=NfMJxKI86r_p96HQ7FEYIcVj8ecNwbrQWb63spYYUPHYdHxBdYkceppoPPuG7zxRdBR5u2S_OhEgejHu2RdgmQjbf3_3v31VIHd2jHXemwihnpE_onaQhAsiNOlRby5EGGwi0ufKu4MpGmVDu6CqagSMFwITAMyyaPPcuIWDmzwr8cgrfy81z6XF2A24rPvZghuJQABCnFWLL-eOk1oxHbWhMbZOCwxUbIKXkPgkJCBE5dq8SZWykatMCq2PsC8yhbntW08HzMYX5dY881-jLgbU29O3WbKbEgtdD7oZB1vA5LZn783JOKmcYvXvCFA5aM3QUDgv0Yeav-TSqW87GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده مردم در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69455" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69454">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f06a84a2.mp4?token=XtJaBmYfF_6Xdio9FJjElrpA5kAAdQM0eeiQM_sLKmAblUKxajjbSpB59AsVJof2HGtrVT78XKn5VhOK-N4J0E8wc7RdTTzDXLNcEVswn_YviXNUD8UJkjaWoR4UFREI0-rIraIdAeGF-o1_Ya-dgNplP0QI4uWihuIdAvwRDqZuCTmHuOvvoRDBUEIcu7twrEo30KwATDVClG0adM0SXemcLMQ7DBecrlgJ2oJoM4jTnJKiW-GhUY0SiqniMnUAX0T9_Lxd-Yd03GmX0IhLoUf18uh5XPubaeTwHkvLJZcH1HLrmyoNPyDHYe0qAnLOUYMdhYiFo6yaUE8Pk6EnGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f06a84a2.mp4?token=XtJaBmYfF_6Xdio9FJjElrpA5kAAdQM0eeiQM_sLKmAblUKxajjbSpB59AsVJof2HGtrVT78XKn5VhOK-N4J0E8wc7RdTTzDXLNcEVswn_YviXNUD8UJkjaWoR4UFREI0-rIraIdAeGF-o1_Ya-dgNplP0QI4uWihuIdAvwRDqZuCTmHuOvvoRDBUEIcu7twrEo30KwATDVClG0adM0SXemcLMQ7DBecrlgJ2oJoM4jTnJKiW-GhUY0SiqniMnUAX0T9_Lxd-Yd03GmX0IhLoUf18uh5XPubaeTwHkvLJZcH1HLrmyoNPyDHYe0qAnLOUYMdhYiFo6yaUE8Pk6EnGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای ازجواد موگویی که توی برنامش داره خیلی شیک و مجلسی جای همه فرمانده‌ها و مسئولان رو لو میده:
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69454" target="_blank">📅 10:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69453">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b06d3aa4b2.mp4?token=gkL6GzPf-jqLQpCs7fKNRQCi06Rp2DdUhF-eAieN52a9Mrqor8I9XvQzMnoTUc_mhdHZiIFML6NCOXU4z80oFHK1C4z9VmPf_cQxnfbYNBQKN4np9HX4BLNVdGUhokSWj1WRJCG68Ys-42HDavLcvjQ4uqE6__9LLVqUblLjaC-U75g8AI8E9tr_Oz7ODNDP0w7algQnb31hKSkHO4_cXmIgpHO1Qavmlj-4URjA9ruED8LbRCMOtPUt1Z_LnxdEmccZkXe6O6z6K_7YlyhlCM7fQepiNPvkTpJxUxB2YrIDhNgYSjcIT_jc9tcVJ8zrQAMJPMuhRURThlnshLkYVFmW8vr1PjKY43PaiTvD3nQkELpD5Z5BD6gnXhLqBrtL1-uWe4quTmAeRKaoHcCgzUaMszioy-IFFvmUoBOJTvFo0mimR8hPwicoUHJ0rgqM12u_yMQzLkKt4ZLMsdVEs_OjoJknJ-KFukh_fWwxhRQ4xlUPKzTLpyQ_42q20Y0wB3NagJKOcATzwghn6IAORUXL4ZbNtW0MqzTTZC8KbqUP1T-CDhYFanq0TlIXQ71DxmLau5N7UWpAHstldpPJNAvO3ZPjKc-c4tkuALgsyobP-XkUfZ5c6b2J4OFARqSYGR_djsfR0kM1pbrUpvQCIpmFy7fKKAm5oMFuseUr8Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b06d3aa4b2.mp4?token=gkL6GzPf-jqLQpCs7fKNRQCi06Rp2DdUhF-eAieN52a9Mrqor8I9XvQzMnoTUc_mhdHZiIFML6NCOXU4z80oFHK1C4z9VmPf_cQxnfbYNBQKN4np9HX4BLNVdGUhokSWj1WRJCG68Ys-42HDavLcvjQ4uqE6__9LLVqUblLjaC-U75g8AI8E9tr_Oz7ODNDP0w7algQnb31hKSkHO4_cXmIgpHO1Qavmlj-4URjA9ruED8LbRCMOtPUt1Z_LnxdEmccZkXe6O6z6K_7YlyhlCM7fQepiNPvkTpJxUxB2YrIDhNgYSjcIT_jc9tcVJ8zrQAMJPMuhRURThlnshLkYVFmW8vr1PjKY43PaiTvD3nQkELpD5Z5BD6gnXhLqBrtL1-uWe4quTmAeRKaoHcCgzUaMszioy-IFFvmUoBOJTvFo0mimR8hPwicoUHJ0rgqM12u_yMQzLkKt4ZLMsdVEs_OjoJknJ-KFukh_fWwxhRQ4xlUPKzTLpyQ_42q20Y0wB3NagJKOcATzwghn6IAORUXL4ZbNtW0MqzTTZC8KbqUP1T-CDhYFanq0TlIXQ71DxmLau5N7UWpAHstldpPJNAvO3ZPjKc-c4tkuALgsyobP-XkUfZ5c6b2J4OFARqSYGR_djsfR0kM1pbrUpvQCIpmFy7fKKAm5oMFuseUr8Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مارک لوین:
تداوم توقیف دارایی‌های متعلق به ایران
ادامه محاصره دریایی برای قطع درآمدهای نفتی و گازی ایران
هدف‌گیری مستمر فرماندهان نظامی
حمله به کارخانه‌های تولید موشک‌های بالستیک و پهپادها در سراسر ایران
هدف قرار دادن ساختمان‌های دولتی و تأسیسات متعلق به سپاه و ارتش
حمله به بانک‌ها و مراکز مالی
دست‌کم تا ۳۰ روز و شاید بیشتر، هیچ آتش‌بسی در کار نباشد.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69453" target="_blank">📅 10:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69452">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/998caf4317.mp4?token=aIXm5xWibsa_RPwJlHvk1xWy0hmboMDss-87RH7Yexf4WcSulX7IAMh-KFPM0BrtSTvrglh86buNOy3T5nUKTQvPrrx0Kj66DNWWUUPIOeinKC9zIfeu_09E0eTL8WQkfBBQcBFcGsuX5XWIG-tQWd4Wl12_yX43twDZyR3fXmJZiuOTqv5T1hlcDEZ6GEbpShXLr7qp3cmU5JYCmLA7HxuQ9PzmJA8iSS7piLTvCjiordTWyLgHNZda4uQ79G56cXAAMVnJaVl8bU7TBbSKSDtkrzobwCP2NxYz5fdtb4RJLgU82LZuefrbPV9NIHz6-UsPTxUP_5Ig2cDqn2tskXqIS0_oVw7UWkDFIzKlmKkQoVh5VQuVYX3H5UcTRl_bltBA0xLgrZEkwBr84pNLkanCU6D8_9S-Ao3DuPb57x0BjniGFtvw0ULfyPVSQIFqy4TtPNaMMSCHni81RXkdveMO7Ixobs2lsx7vP7asib5WwZ8GycI-jtyJ0OKU08mHr2wt6R8tOLsG4Be0dClFWgjC1SDRAgOdVz2jz9bobKw3fYJBpSOvFXS8qHN_Vq-LYIgLdGgEQvf6vv6C1BGDbp784T3nwXMaCVq6jm1sNRga-gLEWeMjfH7ff3u775AG6U0WsS1i6t4rS1k_9IV5kaqZAWnAMKUFygk6PRYG3BE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/998caf4317.mp4?token=aIXm5xWibsa_RPwJlHvk1xWy0hmboMDss-87RH7Yexf4WcSulX7IAMh-KFPM0BrtSTvrglh86buNOy3T5nUKTQvPrrx0Kj66DNWWUUPIOeinKC9zIfeu_09E0eTL8WQkfBBQcBFcGsuX5XWIG-tQWd4Wl12_yX43twDZyR3fXmJZiuOTqv5T1hlcDEZ6GEbpShXLr7qp3cmU5JYCmLA7HxuQ9PzmJA8iSS7piLTvCjiordTWyLgHNZda4uQ79G56cXAAMVnJaVl8bU7TBbSKSDtkrzobwCP2NxYz5fdtb4RJLgU82LZuefrbPV9NIHz6-UsPTxUP_5Ig2cDqn2tskXqIS0_oVw7UWkDFIzKlmKkQoVh5VQuVYX3H5UcTRl_bltBA0xLgrZEkwBr84pNLkanCU6D8_9S-Ao3DuPb57x0BjniGFtvw0ULfyPVSQIFqy4TtPNaMMSCHni81RXkdveMO7Ixobs2lsx7vP7asib5WwZ8GycI-jtyJ0OKU08mHr2wt6R8tOLsG4Be0dClFWgjC1SDRAgOdVz2jz9bobKw3fYJBpSOvFXS8qHN_Vq-LYIgLdGgEQvf6vv6C1BGDbp784T3nwXMaCVq6jm1sNRga-gLEWeMjfH7ff3u775AG6U0WsS1i6t4rS1k_9IV5kaqZAWnAMKUFygk6PRYG3BE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🇮🇱
🇺🇸
ویدیویی جدید از لحظه بمباران خیابان فردوسی در زمان جنگ ۴۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69452" target="_blank">📅 09:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69451">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHXFvf14gxyCa4uwNuBQqigDbSZzwNcjl1mJFtV7IGcNhqxvC10N5K8IMeXM60ImltRYxepGipdvhht0CAvehqlBLEvZe3KDySK4EMpMxjZvzqYBgPHAi43gb82cV_mm7OzsUf87hX3knls0mVPWFJGXHkRZBjvYyft4vPvrxlcpqUMBG9rTtb-nUywdk81D2OZtBox8_GTnoc3fA2eKbIQ7we4WESep6zLwe_go5Rf2o0KOIiPo4rNe9Y77mVSr5tRu1NTzM7SC59lZrhgTLx2nasRDcqzsFU456llWY44auYqMy2Y8j3Q4t8JE80yRtzx8XdIdQ16B2STBdYelXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
هگست وزیر جنگ آمریکا:
واقعیت.
وزارت جنگ آماده‌ی حمله بود - و همچنان آماده است - در سطحی که از جنگ جهانی دوم دیده نشده است.
قفل و بارگذاری شده(آماده اقدام).
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69451" target="_blank">📅 03:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69450">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TCzMS5UUZ1BMM78etqNXzlE-bpbage7ASx2FXjT3jLDmTJmxAkw52oijgqgkKCAgrnMAv9Yd6-Gdz4Kael2sVxKK1C9LQeMkVMA3Lh9Pis2J_nCcLYl8pL_0Oj-iXHVxzEaKrqvoOAa9__c2KTcEwnDd3p_QbIOaXLqEeKRUDKRtiQ-ysXRFdCaIeaQeOAs359YaNGkJiVcu67e2z8KMtIXSu_KD52vTTMF2leN0_UpT_QfHepGBKUlO8Gb_ZQ7J42mUHyboIu5XqeIpa-u8XPcyMkoRA8U17FlPb6LcRENNrM4TmF-brNMQQy3tNPjsF9A97TfApSiRRBzZ0rd0tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پست جدید کاخ سفید:
به ترامپ اعتماد کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69450" target="_blank">📅 01:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69449">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQlVjXNY8AM4H02TICyOvXO1FH2DQwXnw5hL8qqGuG0KSTwclleQhVKJ15SYLTLz4ZKwI5ViwirfotJ6J-zhvfkVQvz1E1VwvdI-3eFpe9kAE3uC09FTRB7rMabVcA9zCherditXwJgkJvI031ipfPaINukqX9IESz9HO6PLDc9N1cRnedyVppG_kyzI-ZMvcQVoncgj6j3cGuRBFVNGKQH5_a8LjRYTxo4GPHtgq6xxHSF63pmnVy6imp1Nh19cy77E0VudCLx7ptSSFEEA5xSfr0zH68cqpFkSTO5uFd5GZDscBr9FQGAss0gyK5jX11s8zrYHbirolD2shN2nvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی مبنی بر وقوع یک حادثه در فاصله ۲۰ مایل دریایی شمال‌شرقی خصبِ عمان دریافت شده است. مقامات در حال بررسی موضوع هستند و به شناورهای حاضر در منطقه توصیه شده است که احتیاط کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69449" target="_blank">📅 01:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69448">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
وسط حرفای ترامپ یه کشتی تو تنگه هرمز هدف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69448" target="_blank">📅 01:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69447">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac4e8fdd53.mp4?token=AWTRENLFkXwEotFpTmvoNi7qoRMUM5PEUmHMUeH63hLgFxykxZmWMPoQJ0dH1zfLu9RMby-y3cDJKl6fgYy8TiivGaxIq8ODnFKUnB8dpiSF2CXZ2ADKL3jFDJpSJ7xQAEBzE-OHYfpegpEKT_-7ggcCxmSocj0hcXZeK2KPmgwiCobP5yDB9TfXzBOUmdHc74L5khuzfZ4IvYtF0oZZJC7rGdrMuQy549Ru4GZSESdhDzVN67MtR2jPel9TW_FYjO0uAedPm1sNwWSPm2zRoEewgmAfgvAkNJfoyL2bGkUF9qhNoVYYixQhndg8A8JrvlY3YZywK_eOOT98mGEDXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac4e8fdd53.mp4?token=AWTRENLFkXwEotFpTmvoNi7qoRMUM5PEUmHMUeH63hLgFxykxZmWMPoQJ0dH1zfLu9RMby-y3cDJKl6fgYy8TiivGaxIq8ODnFKUnB8dpiSF2CXZ2ADKL3jFDJpSJ7xQAEBzE-OHYfpegpEKT_-7ggcCxmSocj0hcXZeK2KPmgwiCobP5yDB9TfXzBOUmdHc74L5khuzfZ4IvYtF0oZZJC7rGdrMuQy549Ru4GZSESdhDzVN67MtR2jPel9TW_FYjO0uAedPm1sNwWSPm2zRoEewgmAfgvAkNJfoyL2bGkUF9qhNoVYYixQhndg8A8JrvlY3YZywK_eOOT98mGEDXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
نمی‌دانید این حملات به کجا ختم می‌شود.
منظورم این است که آیا همسایگان ایران با هجوم سیل‌وار جمعیت به کشورهایشان مواجه خواهند شد؟
یک فاجعه. اتفاقات بد بسیاری ممکن است رخ دهد.
ترجیح می‌دهم توافق کنم. به دنبال کشتن آدم‌ها نیستم.
آدم‌ها می‌میرند؛ خیلی‌ها می‌میرند. ما چنین چیزی نمی‌خواهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69447" target="_blank">📅 01:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69446">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/320bfbc7f8.mp4?token=CVp1UQY7NOZO-G5buANGUMaTS6H8ZdCjPQEaXS7JvGT_X7JdaG6J0bGPv3mwCl4y1XM_K-4vXSTaZt0wclSn_xHKegoEIt7vbc75uY59g6BVtPhd80bdTBZ-8hTf-Fiotr19x4prKo9HjrUxs0r4u4mlUl4pK2TkHRr93Ud_wQnnMoOv1vw8YHamsiNcNcmTg4FYoce4OkGUxfXnRxi6wtuapbIZPW_eUOeEoDyFCtiqHyFZ9KDO9q9s_w-JzLcERKLIHK8OA13HrhPJlYfiQW8RfVlCbyb6-9VnXhFit8fy5DPTqkg8hvTiirfHcRvy5Wf0juGU3lDRZnID2eZ6rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/320bfbc7f8.mp4?token=CVp1UQY7NOZO-G5buANGUMaTS6H8ZdCjPQEaXS7JvGT_X7JdaG6J0bGPv3mwCl4y1XM_K-4vXSTaZt0wclSn_xHKegoEIt7vbc75uY59g6BVtPhd80bdTBZ-8hTf-Fiotr19x4prKo9HjrUxs0r4u4mlUl4pK2TkHRr93Ud_wQnnMoOv1vw8YHamsiNcNcmTg4FYoce4OkGUxfXnRxi6wtuapbIZPW_eUOeEoDyFCtiqHyFZ9KDO9q9s_w-JzLcERKLIHK8OA13HrhPJlYfiQW8RfVlCbyb6-9VnXhFit8fy5DPTqkg8hvTiirfHcRvy5Wf0juGU3lDRZnID2eZ6rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد ایران:
ما حمله‌ای داشتیم که می‌توانست بزرگترین حمله از زمان جنگ جهانی دوم باشد.
این حمله برای آنها فاجعه‌بار می‌بود و آنها نمی‌خواستند ما این کار را انجام دهیم.
صادقانه بگویم، عربستان سعودی هم این را نمی‌خواست.
آنها فکر می‌کردند که توافق قریب‌الوقوع است.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69446" target="_blank">📅 01:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69445">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4635f3df1.mp4?token=qU-GdSz8BNNHbwIAeFDz8HzugE1SnQ0hAtURh7qg_bcfmycoLfSXchL9ej53DAa1mzjCGBJOpbmOtJcTCgLx1tQinitxUusez8ybN4GH3rY8g886sclcfbD78mPOFTdwXCJq3QRWJIXgRLolE6-2HTGwoZzfvn7rJCq1yaaDuTAW-7HbQ5bd78e9wW7VdY18YKYaWJ35CM5niyqVMsBIsD_hq18ZVcYm7zfFyuY4xWYQqF1HznYZ0D_rHheD_NR3D9Zhnx0l-Z5bEr4ePzZYHHHZMgDsZ66ThgXv3CGSxvXEtizNy0aT03_zoxFGSx4dxRG1ocdACeIjOjSi06sTDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4635f3df1.mp4?token=qU-GdSz8BNNHbwIAeFDz8HzugE1SnQ0hAtURh7qg_bcfmycoLfSXchL9ej53DAa1mzjCGBJOpbmOtJcTCgLx1tQinitxUusez8ybN4GH3rY8g886sclcfbD78mPOFTdwXCJq3QRWJIXgRLolE6-2HTGwoZzfvn7rJCq1yaaDuTAW-7HbQ5bd78e9wW7VdY18YKYaWJ35CM5niyqVMsBIsD_hq18ZVcYm7zfFyuY4xWYQqF1HznYZ0D_rHheD_NR3D9Zhnx0l-Z5bEr4ePzZYHHHZMgDsZ66ThgXv3CGSxvXEtizNy0aT03_zoxFGSx4dxRG1ocdACeIjOjSi06sTDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
قرار بود حمله‌ای گسترده باشد.
آنها از ما خواستند که این کار را نکنیم. گفتند: "لطفاً این کار را نکنید."
همسایه‌هایشان هم همین را گفتند.
ما فقط می‌خواهیم ببینیم که آیا می‌توانیم به توافق برسیم یا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69445" target="_blank">📅 01:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69444">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ad85e5d7.mp4?token=K8ARUyN_azeqFM_MKRHk1okislVINMm99jAacN9ebJ7R5Za3S8fm8rTky9b1JS_CtD0fWWuFD_yFN8loXREr2jfx6dgWM2uuHGdF7bBta4P_qZ0_qVPZun0tmVZiTCbkZeYkiHQCft2MHQjZBMa29aI9_QNwldb8fd7c1ztpzKH3Eks8RLkT92VJLczGZkVzqQWjGQNEwUBxuUVCvIWkeGlKbc-sh9vsIlUSEsPg_9OIQ15ZamM2okjSzBg_aMG4sRU6ZOIIc-vxLKKTOpl83n13NszXEq4_ZP6U0vW8ZsOOh1yIXUJbVbARjaW3U6adWetKk4sBeBBvurywTuiLcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ad85e5d7.mp4?token=K8ARUyN_azeqFM_MKRHk1okislVINMm99jAacN9ebJ7R5Za3S8fm8rTky9b1JS_CtD0fWWuFD_yFN8loXREr2jfx6dgWM2uuHGdF7bBta4P_qZ0_qVPZun0tmVZiTCbkZeYkiHQCft2MHQjZBMa29aI9_QNwldb8fd7c1ztpzKH3Eks8RLkT92VJLczGZkVzqQWjGQNEwUBxuUVCvIWkeGlKbc-sh9vsIlUSEsPg_9OIQ15ZamM2okjSzBg_aMG4sRU6ZOIIc-vxLKKTOpl83n13NszXEq4_ZP6U0vW8ZsOOh1yIXUJbVbARjaW3U6adWetKk4sBeBBvurywTuiLcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره بمباران ایران:
گروهی از افراد هستند که خیلی دوست دارند من این کار را انجام دهم—صرفاً انجامش دهم—و گروه دیگری هم هستند که نمی‌خواهند من این کار را بکنم.
🎙
خبرنگار: آیا ایران برای دستیابی به توافق ضرب‌الاجلی دارد؟
🇺🇸
ترامپ:
خواهیم دید. من به دنبال کشتن مردم نیستم.
از ولیعهد عربستان سعودی پرسیدم: «ترجیح می‌دهید ما چه کار کنیم؟»
او گفت: «ما توافق را به حمله ترجیح می‌دهیم.»
🎙
خبرنگار: گزارشی وجود دارد که می‌گوید شما در حال خارج کردن نیروهای آمریکایی از کویت و بحرین هستید.
⏺
🇺🇸
ترامپ:
نمیخواهم در این باره اظهار نظر کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69444" target="_blank">📅 01:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69443">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098cb6b6b9.mp4?token=NomW06NuG-SA8x2-gsb7FqI41deodzj4op0YriP3LENSrGSGUwJ-7wv16OfFkvxVHr5oHvxtWmYVwB9M2l5FyfJZurFOwL_FXeEnTOfOmntUpG1fn3la0Kfg5TkilITrHj7OLaDQyX1bCDW2O0cDzNJKtifcv1FNtiCImvEt_-AzgHVq8bKLcDrTnedSTde75npcSgBZCAUeWA5R0mU8AV0CJb208w2CIY2YMl3c9TpyVJun4j5TcDqW07y0jZGdgjEz4kMrHL_l5utYSm6VPfOcNGSWi2Yr8klKbZY0CL2GqJ9CjgKG4lLezpQLhkAz4GN-hhRFDeHPsIiagmo88Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098cb6b6b9.mp4?token=NomW06NuG-SA8x2-gsb7FqI41deodzj4op0YriP3LENSrGSGUwJ-7wv16OfFkvxVHr5oHvxtWmYVwB9M2l5FyfJZurFOwL_FXeEnTOfOmntUpG1fn3la0Kfg5TkilITrHj7OLaDQyX1bCDW2O0cDzNJKtifcv1FNtiCImvEt_-AzgHVq8bKLcDrTnedSTde75npcSgBZCAUeWA5R0mU8AV0CJb208w2CIY2YMl3c9TpyVJun4j5TcDqW07y0jZGdgjEz4kMrHL_l5utYSm6VPfOcNGSWi2Yr8klKbZY0CL2GqJ9CjgKG4lLezpQLhkAz4GN-hhRFDeHPsIiagmo88Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: در مورد ایران، حالا چه پیش می‌آید؟
🇺🇸
املاکی:
ما در حال گفتگو با آن‌ها هستیم. این گفتگوها از بعدازظهر فردا آغاز می‌شود. این کار جان‌های بسیاری را نجات خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69443" target="_blank">📅 01:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69442">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992fe6ee4d.mp4?token=PPcQndbI2jLrYmbbRkFn_Cv63l1zycGafZy1tGtN0bdvjjXEWwlQGY9e6q2slhE8X-aU2-YLdw8Vj4ioEnQ1ljwYFbdLcOT5kY1G4fLRA6mfR_k_BiOy1lRvpsTzsdPjFyYchUj-n9t4UohvvH60wk6Yo9nmUIS3mRqE2psryiPOWzAs9mGe1syNMQvB_Up49toWCVD1wwO86rrfrhsLHkeiS53pYERPmg1CGg3WS9rrTFv7NB-ShSJdZQc_ojRHDYKZMk9mcRgh9SeVKrDs0DJRL3VRJiqamUg1vPZmsH2y9BGI-BzwdWNl5NrLFXDP7bNVUO9z_B7iAsHjuK1OWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992fe6ee4d.mp4?token=PPcQndbI2jLrYmbbRkFn_Cv63l1zycGafZy1tGtN0bdvjjXEWwlQGY9e6q2slhE8X-aU2-YLdw8Vj4ioEnQ1ljwYFbdLcOT5kY1G4fLRA6mfR_k_BiOy1lRvpsTzsdPjFyYchUj-n9t4UohvvH60wk6Yo9nmUIS3mRqE2psryiPOWzAs9mGe1syNMQvB_Up49toWCVD1wwO86rrfrhsLHkeiS53pYERPmg1CGg3WS9rrTFv7NB-ShSJdZQc_ojRHDYKZMk9mcRgh9SeVKrDs0DJRL3VRJiqamUg1vPZmsH2y9BGI-BzwdWNl5NrLFXDP7bNVUO9z_B7iAsHjuK1OWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ در مورد ایران:
عربستان سعودی، امارات متحده عربی، قطر و ایران از من خواستند که حملات را متوقف کنم.
حمله بزرگی می‌شد.
وقتی متحدان خواستند که آن را لغو کنیم، باید گفت: "خب، ببینیم چه می‌شود."
متحدان فکر می‌کنند که توافقی حاصل شده است. توافقی در مورد هرمز وجود دارد و توافقی در مورد هسته‌ای خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69442" target="_blank">📅 01:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69441">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/661dbe4eff.mp4?token=gYm8Zwq2tlYclVz707nAiGsy8GhAs2CUEGHYFVi6iPtLynS1I3XR3crZI8ZKrjQ3aOQBPM3nXT8UcQ3PsNhc6r9aHnfHlwOiKozwgyLf7cm7sjETk4fxPK7elk4s3uYhfl62KiTln-2w-CGwfM2QaI1NlTc0XsElrtBEBPM_snWIpb7OMr2CYCk4ImbWiznVFbFT6cQh8wK6oQldzQuvYDqdjO4r0TuQyHXqRORAtbWNuju4tG0SfenWVaXsWyNr9ToSQCpc2diN00Nwnu_-OHcvNCBXA-UGtTqhGEwL-tbBzFSf1LNPQWmrFB6jLlscGHZjYPJ9-kP262CV645iPA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/661dbe4eff.mp4?token=gYm8Zwq2tlYclVz707nAiGsy8GhAs2CUEGHYFVi6iPtLynS1I3XR3crZI8ZKrjQ3aOQBPM3nXT8UcQ3PsNhc6r9aHnfHlwOiKozwgyLf7cm7sjETk4fxPK7elk4s3uYhfl62KiTln-2w-CGwfM2QaI1NlTc0XsElrtBEBPM_snWIpb7OMr2CYCk4ImbWiznVFbFT6cQh8wK6oQldzQuvYDqdjO4r0TuQyHXqRORAtbWNuju4tG0SfenWVaXsWyNr9ToSQCpc2diN00Nwnu_-OHcvNCBXA-UGtTqhGEwL-tbBzFSf1LNPQWmrFB6jLlscGHZjYPJ9-kP262CV645iPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی وقتی می بینه دلار شده 190 هزار تومن و آب و برقم هر روز قطع میشه:
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69441" target="_blank">📅 00:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69440">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93362f281c.mp4?token=Y5NJuv7jOcFx52BWy-W5lW9nBKeO_qRyQ2kjwHvGKfDwcu1KspCPXAnMuaVN926gxkY3ZrEaELfyfT11-ZO2mExiRp4ri_4q7tR4XtuPEGirsGU_air3aGDxeowLRi1rhPn56uVxyd55XjPeD-y9npyX57XKmeklCIT1mf181OqzEY0LXBafYiJvaqM8_HIo4y6ATB2cuSdCHwNPiultJxd94ZE-zxs0NnVn1645QIuC5V3j7ofpBRvH3_JrOjh7wIcyC_de2AYfJoNdAKN9oLHs1SAoVJ_Y5hkSuCsOevYbLpIZz6sG3cI13LiXVVyqx7FTh_53FwD5oX9hzgZ5hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93362f281c.mp4?token=Y5NJuv7jOcFx52BWy-W5lW9nBKeO_qRyQ2kjwHvGKfDwcu1KspCPXAnMuaVN926gxkY3ZrEaELfyfT11-ZO2mExiRp4ri_4q7tR4XtuPEGirsGU_air3aGDxeowLRi1rhPn56uVxyd55XjPeD-y9npyX57XKmeklCIT1mf181OqzEY0LXBafYiJvaqM8_HIo4y6ATB2cuSdCHwNPiultJxd94ZE-zxs0NnVn1645QIuC5V3j7ofpBRvH3_JrOjh7wIcyC_de2AYfJoNdAKN9oLHs1SAoVJ_Y5hkSuCsOevYbLpIZz6sG3cI13LiXVVyqx7FTh_53FwD5oX9hzgZ5hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث سوشال:
شوت برنده در مسابقات قهرمانی باشگاه بدمنستر! از تمام کسانی که شرکت کردند، بسیار سپاسگزارم.
من با امتیاز 70 برنده شدم و از این بابت بسیار مفتخرم، زیرا برخلاف سایر شرکت‌کنندگان، زمان بسیار کمی برای تمرین دارم، زیرا تمرکزم روی مسائل دیگری است.
این را "استعداد" می‌گویند و من آن را دارم، در حالی که آنها ندارند!
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69440" target="_blank">📅 23:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69439">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsLd-lYl8htLb5cAZrksQQrvay1Lv9EBY74jh9Db94QYFkh6XjqyKYn0_hdEfzaEwVK7D-lOiVhQTt2fnA_vCzrpA5bvl-gFQ23IWGxaFKKDHqNiIn2PvmfOlx5pfChD1FvtdvhKRAJd1C5VZnl1X-Ywyk0Y0Z-mkkjUNKZtP55aGd_4t46C50r1pY-JoFJ087J727rsB0uLXTlXVJq-4pHTxaS1f_pjps6_XZ99aVciXsHHYCJ_jpACbdtTC_5g3Wt7Qhm_stACSFgTVcML8PJ3K4o8839ZtwvY9uZyMoiHflQIn72mBuU7va0OAjksIc4KO-TXabpxxTEYOU7Q8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پزشکیان:
تفاهم نامه که امضا شد حاصل خرد جمعی اعضای شعام بود
این تفاهم نامه ثقل روابط خارجی ما توی آینده هستش و باید دشمن رو وادار کنیم بهش پایبند باشه
امنیت کشور و منطقه و هم‌پیمانان با این تفاهم نامه ارتقا پیدا میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69439" target="_blank">📅 23:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69438">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⏺
شکار و هدف قرار دادن ۶۷ سرباز روس توسط مولتی روتورهای اوکراینی در اطراف پوکروفسک
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69438" target="_blank">📅 23:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69437">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f93e085c7.mp4?token=rK8JWYgmHB_Bs9ViQ26L9b5GNCli_-ulgpQ0PUbNwJQNVT_lPtq6DEDl6VIIvw5lAAljIMx8LzsYOFevIgnBpyPwUJVMn_xDwnJWC-AU-6Jp0Eb-ZuSohxMKcBmxR9ak_5tRXuQ4kqYEna4UclJFOx-Obzp7du3IhhmablvgDJRfjxTrIvFQ2FsM6TrcIlqcuv76rzTFy9BdhfWlxOOjNH9H5uU9SNeBJoEVn1etdhJKArorV1jnWGLnKIFSag2k7mVfmJIOseePrbKjoegqncKAFNpoxM3013spqBr7PtV_zf82ftF6biI4R5BDFc7m-EFWIpO8ZhXokaiuk-HG5Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f93e085c7.mp4?token=rK8JWYgmHB_Bs9ViQ26L9b5GNCli_-ulgpQ0PUbNwJQNVT_lPtq6DEDl6VIIvw5lAAljIMx8LzsYOFevIgnBpyPwUJVMn_xDwnJWC-AU-6Jp0Eb-ZuSohxMKcBmxR9ak_5tRXuQ4kqYEna4UclJFOx-Obzp7du3IhhmablvgDJRfjxTrIvFQ2FsM6TrcIlqcuv76rzTFy9BdhfWlxOOjNH9H5uU9SNeBJoEVn1etdhJKArorV1jnWGLnKIFSag2k7mVfmJIOseePrbKjoegqncKAFNpoxM3013spqBr7PtV_zf82ftF6biI4R5BDFc7m-EFWIpO8ZhXokaiuk-HG5Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌‌
‼️
روح الله قرهی رئیس حوزه علمیه:
«وقتی ماهواره به فضا می‌فرستیم، می‌توانیم سرش را کج کنیم و خود آمریکا را بزنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69437" target="_blank">📅 22:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69436">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4MEqkCzjjRRxUQUKTk4F5FCbtDXfSFKRCnFGl4cC-sDvN8UXMCxUCGjUPxkepV3cq65zN8CAD2glBg-1-BQfm3w_UH2EcmZ_etJ4r11LNVlzhOH2c43RxzEZRACq8QTIV4IdjYoWEbzYmy_FpHFIr98Y7qhEQ0Kz3CKv9kqcjDBICrj1ugCPZnZDMR4gAQf7mP1aXsD3YmQfJGWv4PylycqG3IxrF4F6VIooIH9UEDcBgBgXZT8KuupQJI0zyJQ1cbXu-FIub4Qt8_v5HBMKjDZwFr0mXmksvWOsNTlg_Co2Svjh86Xqr7KXbr64ZHpHQFOhlKC29ezIVgmNUHQAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
کان‌نیوز به نقل از یک منبع امنیتی:
رفتار دونالد ترامپ — که منجر به لغو حمله گسترده به ایران شد — به توانمندی عملیاتی آسیب می‌زند و آن را تضعیف می‌کند.
این مقام امنیتی گفت: «این دومین بار در طول یک هفته است که ایالات متحده اسرائیل را در جریان حمله‌ای برنامه‌ریزی‌شده قرار می‌دهد که می‌توانست خاورمیانه را تکان دهد، اما آن حمله در آخرین لحظه و بدون هیچ توضیحی لغو شد.»
یک منبع اسرائیلی نیز افزود: «با وجود رفتار رئیس‌جمهور ترامپ، آماده‌سازی و تدوین جدی برنامه‌های آتی دشوار است.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69436" target="_blank">📅 21:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69433">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Dd87kvz72qdAtWSt8xWvTqEzo89w9nH7ZQDBJDlP32Aqe0m_G3dNvVZj2STggXDP_oeh_IEFhd89uXhd-piXa_atmFWrgaR8VNWhNKyFXgAyHsCZJ2COa05BszJ7zT4puq3nNtm573s3y7WhpM8uvJ14ZCt34TJzQAI0gYk3P8Dfdj4spXfg8_be8kZVT4pvEvFV2Res_rU98DCUczlZK6qPMJPGYcO39RbjhT10jT3izJVWtNipaRTFieYdqHYqC1uhwxBt4Lx4z_OeCHLT4pjjje-dPOOqBk2bpD6oVecKfKFINdaxAighfzkaM7zKbgyq8vaCbM7Ej3tdfZb5OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/98190fb3e2.mp4?token=XnEwoNsZ03YX0Z-sAg9F95uBj9FOLVnAPJm4gsKmypLsPulKdjs0NcWI-sTWvSHqHoUO0kVUBmADMofhjV3RmYB9ftRTly_LtwtCLRC3QSRFO-eh_0jDMbYO7kxkzORxBZze8Y6SrQl2Xgst2UMz_cuXWo-rkFX1cQAhvc7EJiP5MhsWhhLaU1xxO2RI66ssLZ93ERzWbrMSCE-aE9bu0uMMeBBpAu5x1T40frc8eH-CRIGhWeRXXWlVAOnepJvVoR15dJoj8ChpWy46bgqooHe7Q2YTeKK0AWVx_Hw-TmBQ4zyyOoi1FERNaHFOsEDAjmTVV2Z8hx4z6HeSPjXbgw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/98190fb3e2.mp4?token=XnEwoNsZ03YX0Z-sAg9F95uBj9FOLVnAPJm4gsKmypLsPulKdjs0NcWI-sTWvSHqHoUO0kVUBmADMofhjV3RmYB9ftRTly_LtwtCLRC3QSRFO-eh_0jDMbYO7kxkzORxBZze8Y6SrQl2Xgst2UMz_cuXWo-rkFX1cQAhvc7EJiP5MhsWhhLaU1xxO2RI66ssLZ93ERzWbrMSCE-aE9bu0uMMeBBpAu5x1T40frc8eH-CRIGhWeRXXWlVAOnepJvVoR15dJoj8ChpWy46bgqooHe7Q2YTeKK0AWVx_Hw-TmBQ4zyyOoi1FERNaHFOsEDAjmTVV2Z8hx4z6HeSPjXbgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
انبار شرکت Wildberries در منطقه سمارا دچار آتش‌سوزی شد، این اتفاق پس از حمله اوکراین رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69433" target="_blank">📅 21:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69432">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5208110eae.mp4?token=XbBcsf17yCuz1FT8w_LVkwbVvnseEdycyrDJv0fpQ8BrV_n46Znl5KCqsO9GRS7dNh5og60Fb89h2QzGTNIsdHa2jgkSbRQuvcxadW-DS-MZvyJw3Y89CNDPHc_pes6-TsDytw7qz63JIpybqXm9N49_qLeVK3lh-wYTjYZ9fbnBImK7SYi7bxB67JOGicrKW8sl3z86GGD4eLJbNwXqQ7ivODiokPa3bN8b9pI9U26qiLfkVXr7b2nRGgk3n3bPvD33xTn0rWOM_6qewFhhpyyZfzcaYBANnTe-L6DrdTFJb3f-4c2HI7EuK2lnxJ-l0mon7GilvHxi2BZxP0pdmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5208110eae.mp4?token=XbBcsf17yCuz1FT8w_LVkwbVvnseEdycyrDJv0fpQ8BrV_n46Znl5KCqsO9GRS7dNh5og60Fb89h2QzGTNIsdHa2jgkSbRQuvcxadW-DS-MZvyJw3Y89CNDPHc_pes6-TsDytw7qz63JIpybqXm9N49_qLeVK3lh-wYTjYZ9fbnBImK7SYi7bxB67JOGicrKW8sl3z86GGD4eLJbNwXqQ7ivODiokPa3bN8b9pI9U26qiLfkVXr7b2nRGgk3n3bPvD33xTn0rWOM_6qewFhhpyyZfzcaYBANnTe-L6DrdTFJb3f-4c2HI7EuK2lnxJ-l0mon7GilvHxi2BZxP0pdmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سخنگوی امور خارجه، اسماعیل بقایی:
مدیریت آینده تنگه هرمز توسط ایران و با مشورت عمان انجام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69432" target="_blank">📅 20:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69431">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04acf28261.mp4?token=XEcZSALoPXZIAs2oWloLRMOIXAZ1JFxhGQdbUBPLN8sL6hqNEWYMeKS-YFNAzh_N2WKHGZEq58LGH-whfMsF17GhQNDvUgDEvUrDc0TxCUliY-ptJT20WqwtYRR4tyjbov3WSd5XeO6oNwCZPKJDbZFCIQWbjtq8CFhCQRRo0lUjaO_TzfBVWZZ0keSPut9nVKg3-FyqhbT_4P_yxBhszGfOKS7JgksE0jKe_TJoXVydb0R44u84DNo3MLYewCk2QHRP9MhrjIy2jh1oZkUKCg7W-_X9XatKEf-gn0lWKWDC5a4TuQmkcdFbUpW_DGPqhdOVs3yQCGtvghy1YdqGnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04acf28261.mp4?token=XEcZSALoPXZIAs2oWloLRMOIXAZ1JFxhGQdbUBPLN8sL6hqNEWYMeKS-YFNAzh_N2WKHGZEq58LGH-whfMsF17GhQNDvUgDEvUrDc0TxCUliY-ptJT20WqwtYRR4tyjbov3WSd5XeO6oNwCZPKJDbZFCIQWbjtq8CFhCQRRo0lUjaO_TzfBVWZZ0keSPut9nVKg3-FyqhbT_4P_yxBhszGfOKS7JgksE0jKe_TJoXVydb0R44u84DNo3MLYewCk2QHRP9MhrjIy2jh1oZkUKCg7W-_X9XatKEf-gn0lWKWDC5a4TuQmkcdFbUpW_DGPqhdOVs3yQCGtvghy1YdqGnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سخنگوی وزارت خارجه اسماعیل بقایی:
توافق ایران و عمان بر سر مسیر جدید هیچ ارتباطی با بازگشایی تنگه هرمز یا حفظ بسته بودن آن ندارد.
مسیر جنوبی از طریق تنگه هرمز با ناامن کردن منطقه و آسیب رساندن به منافع ملی ایران همراه بوده است و تهران آن را نمی‌پذیرد.
مسیر مورد توافق نه مسیر شمالی و نه مسیر جنوبی فعلی خواهد بود. در عوض، مسیر جدیدی خواهد بود که هر دو طرف متقابلاً بر سر آن توافق دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69431" target="_blank">📅 20:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69430">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc8dec97ea.mp4?token=KOeMvZI2E5EWKnN4PlLEZnQlFm33F4zNVCuDhGfKb8KjiQt5n9xeRxal381oeCEoQ1V2zFDRHnw6WK2uxcl4OPSVzNolnf64QwLWtci7JYzd8WsBOkaPvuouAxAr1xbc5cVcMDlEdoLKK6C4iF37Gg_SbnMGu-NFZqbo0Xvq3JhuhmNKDaqmMXcv2HcpXryvoq9d0bjgE2MyWTDUJPv4vJ7ptitcZIVrR6ekByzvoNrVkWH39ACyYB7xLy-YNnfqZWdqpsuNwjMKxPnkw_CWbc9x6yR1ijPmV-MBcWWRe1_FzmFDnWbsf1gRvZqLwU6i6VSa_2ti1eicrWxK45Dj2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc8dec97ea.mp4?token=KOeMvZI2E5EWKnN4PlLEZnQlFm33F4zNVCuDhGfKb8KjiQt5n9xeRxal381oeCEoQ1V2zFDRHnw6WK2uxcl4OPSVzNolnf64QwLWtci7JYzd8WsBOkaPvuouAxAr1xbc5cVcMDlEdoLKK6C4iF37Gg_SbnMGu-NFZqbo0Xvq3JhuhmNKDaqmMXcv2HcpXryvoq9d0bjgE2MyWTDUJPv4vJ7ptitcZIVrR6ekByzvoNrVkWH39ACyYB7xLy-YNnfqZWdqpsuNwjMKxPnkw_CWbc9x6yR1ijPmV-MBcWWRe1_FzmFDnWbsf1gRvZqLwU6i6VSa_2ti1eicrWxK45Dj2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کارشناس صداسیما:
مسعود رجوی (رئیس سابق مجاهدین خلق) فرد باسواد و کتاب‌خونده‌ای بود و قطعا خیلی باهوش‌تر از رضا پهلوی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69430" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69429">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d5ffc4c3.mp4?token=TSC0r0MbQruwXFQj5KKRoyXSJHhBrkyY7JaiMjJfNGYnnEWCkTsCe7eZ1ceobWIk293JwDZMzxg8wkGUv8dncP0_L9gzvJ5KOA9nbdPijd__Xmw3oYh5KMDt61oWyc-DGyUfu4qlRqks13pIE-vkmGO_QkADzmGIHym8HHmlm8QbEvBUSyjOreGlh_C0mf4f7aOrq7h932QjnEdg6n-BsC5EnHZtm-W9grVGQTkUnz6omctCQscz-PV34P-le3GiZ40wEORUWnJR0SqdaEzWo-A8sRl8GsF0bKU96zpXDuWbXdTK_eHfe8hYH3pC3FhyoApZJn1N7e8eM0LTRhfZQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d5ffc4c3.mp4?token=TSC0r0MbQruwXFQj5KKRoyXSJHhBrkyY7JaiMjJfNGYnnEWCkTsCe7eZ1ceobWIk293JwDZMzxg8wkGUv8dncP0_L9gzvJ5KOA9nbdPijd__Xmw3oYh5KMDt61oWyc-DGyUfu4qlRqks13pIE-vkmGO_QkADzmGIHym8HHmlm8QbEvBUSyjOreGlh_C0mf4f7aOrq7h932QjnEdg6n-BsC5EnHZtm-W9grVGQTkUnz6omctCQscz-PV34P-le3GiZ40wEORUWnJR0SqdaEzWo-A8sRl8GsF0bKU96zpXDuWbXdTK_eHfe8hYH3pC3FhyoApZJn1N7e8eM0LTRhfZQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رادان:
من یه مشکلی برام پیش اومد که گفتم نمی‌تونم در جلسه شورای دفاع در نهم اسفندماه شرکت کنم و غلامرضا رضاییان، رییس سازمان اطلاعات فراجا به جای من در جلسه شرکت کرد و کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69429" target="_blank">📅 19:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69426">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=TyfR0YIo30LIG7zScGYGKMHnsvvRo9DkOr5QO18o_uueq3UO4W6lwLPMCRmPoUi0bxfIlPNCvZZmy5D8lK8VR9aD4L6IwJRIa85JpVtJXBBI0FOiwK6AIIdkpQ2JPVaS4c4ukWVjM8r2Vl89EioMShtBbjODR4oU-_3F6jAQlVfAaBOH39Yz6a-6CAl-Ohzxb86Lxe4ezkXNsgHX3Ne8Rx2ozSsLdxpkJVCMnFFlXFNrMaG3_-8-0oPGoA7Lk4NhDDgXiHO26g9JtWE6lzDruyoVkHEo4aQucOuqR4I8l3Ws8-OWmB2-6Sou02CD7t1xK_mMkiZauaMlNCjWl2rS2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=TyfR0YIo30LIG7zScGYGKMHnsvvRo9DkOr5QO18o_uueq3UO4W6lwLPMCRmPoUi0bxfIlPNCvZZmy5D8lK8VR9aD4L6IwJRIa85JpVtJXBBI0FOiwK6AIIdkpQ2JPVaS4c4ukWVjM8r2Vl89EioMShtBbjODR4oU-_3F6jAQlVfAaBOH39Yz6a-6CAl-Ohzxb86Lxe4ezkXNsgHX3Ne8Rx2ozSsLdxpkJVCMnFFlXFNrMaG3_-8-0oPGoA7Lk4NhDDgXiHO26g9JtWE6lzDruyoVkHEo4aQucOuqR4I8l3Ws8-OWmB2-6Sou02CD7t1xK_mMkiZauaMlNCjWl2rS2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💋
🇮🇷
این جنده‌اینستاگرامی که خیلی ماجراش وایرال شده، یک‌شبه تصمیم گرفت بره تو آغوش حکومت و تبلیغ اربعین بکنه، چند ساعت بعدشم ازش یه ویدیو های
🔞
عجیب منتشر شد
🔗
⚠️
مشاهده تصاویر و ویدیو ها
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69426" target="_blank">📅 18:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69425">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae764e4921.mp4?token=IxNiEH908tA2GH-GaBp6BUxWBNrhHYSFj2iRiXw0C92W7Cqk7OYRyomoKBCAOn25IXP7gOYyqJnatvZnsDyz6s-ovk6YHe6OBmONb-9CoAHyrV3eywc1cTt-uRUIXkPehGEVLtUISTatLWLOYsGJCecK1SRqcVt0FnhSqMHL7gBCyASxEMLaGW5Etj2D5IF4eDBNuRKnaJ4XGmWxLiO_fhOuZQ5LLK8MplTSI3NG-4qeLUHTaqOhpRGvZ5Ohy6OCimpqzm1TY9nnUznnZSVmVeX11aTJfuxBS3w4AziEANXZE6kcIWazz3X3gNzxhdH5Ynz_PZTI-RkEUTXAgmGKHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae764e4921.mp4?token=IxNiEH908tA2GH-GaBp6BUxWBNrhHYSFj2iRiXw0C92W7Cqk7OYRyomoKBCAOn25IXP7gOYyqJnatvZnsDyz6s-ovk6YHe6OBmONb-9CoAHyrV3eywc1cTt-uRUIXkPehGEVLtUISTatLWLOYsGJCecK1SRqcVt0FnhSqMHL7gBCyASxEMLaGW5Etj2D5IF4eDBNuRKnaJ4XGmWxLiO_fhOuZQ5LLK8MplTSI3NG-4qeLUHTaqOhpRGvZ5Ohy6OCimpqzm1TY9nnUznnZSVmVeX11aTJfuxBS3w4AziEANXZE6kcIWazz3X3gNzxhdH5Ynz_PZTI-RkEUTXAgmGKHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخوند پناهیان به پزشکیان و قالیباف:
همه پیامبران را مسخره کردند؛ از تمسخر نترسید و با عظمت صحبت کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69425" target="_blank">📅 18:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69424">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🇮🇷
بیانیه سپاه پاسداران :
انتقام خون رهبر شهید و اسماعیل هنیه اجتناب ناپذیره
پاسخ این جنایت بشدت سخت و قاطع و سخت گیرانه خواهد بود
توطئه خلع سلاح حماس به نتیجه نخواهد رسید و از همین الان شکست خورده بدانید
دنیا بداند اراده ضد صهیونیستی ادامه دار خواهد بود و پیروزی نهایی فلسطین خیلی نزدیک است
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69424" target="_blank">📅 18:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69423">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc039adc5b.mp4?token=JtWMFn9kq03vJXZ6Pp-HTGGqHyd8Y9YOmSbyv1EoRsvH2D5X0EJwycGnhtlwaHywJIguZsbYym5Oy9jhLKYKJt27aLSZgC7qlNTRTqIzjZM8zLihzFTOF2BpzSC-Y1W7AsXGJx2zo_IEug_tIaqhPyad9i6cTLcw9BqtyyQC6Bo3_UskoPIPvQsaXlwLoqmy2YI8VPs7BWx0m0vYYoZsVNfyesOPg_2E5BpaokN99yiDsi96dUD1dLClR4QvAlOXz5vztKUamr3kBUDeFJXOoFYUcAO0zhxzGW00baX5DhaKyM4_9Clp_0Coim9pbZzJFd5a2_KvsOLGffR0yRsK7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc039adc5b.mp4?token=JtWMFn9kq03vJXZ6Pp-HTGGqHyd8Y9YOmSbyv1EoRsvH2D5X0EJwycGnhtlwaHywJIguZsbYym5Oy9jhLKYKJt27aLSZgC7qlNTRTqIzjZM8zLihzFTOF2BpzSC-Y1W7AsXGJx2zo_IEug_tIaqhPyad9i6cTLcw9BqtyyQC6Bo3_UskoPIPvQsaXlwLoqmy2YI8VPs7BWx0m0vYYoZsVNfyesOPg_2E5BpaokN99yiDsi96dUD1dLClR4QvAlOXz5vztKUamr3kBUDeFJXOoFYUcAO0zhxzGW00baX5DhaKyM4_9Clp_0Coim9pbZzJFd5a2_KvsOLGffR0yRsK7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو هلیکوپتر آتش‌نشانی در حین مبارزه با آتش‌سوزی جنگلی در نزدیکی پساتا، یونان، در هوا با هم برخورد کرده و سقوط کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69423" target="_blank">📅 17:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69422">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bef1baf0f6.mp4?token=tWfX08wJSsk3e8dcVBev7hfX7YMGb2JcJblUnoaoWmRWE57qle0DqJ0L3m_IxgLqS7zLOdbEfD3oI94ZQ0NsSRc0qq1xI3cpaZaJQFaTzgpUob5vGYPBSm1FEueQ3roSLTq6ErGG5HtGWskjCdy5nrHwfhc7cU6XgWyEzXtn5FrN49bHB_Z4BqclhM2C0dWD69FpzwRL-DwykwzrJ9zgmaF8bwdaOdnV5f6semxrUd7-do2tKuJRPzfSqDXpzGpRaMCOKEa21El_rGa07YK3X23oOJRadjotsK9TjOenzpm97SVwEnVe2n7eopT9OKQty3rgJQBJORBefJWWtfMHcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bef1baf0f6.mp4?token=tWfX08wJSsk3e8dcVBev7hfX7YMGb2JcJblUnoaoWmRWE57qle0DqJ0L3m_IxgLqS7zLOdbEfD3oI94ZQ0NsSRc0qq1xI3cpaZaJQFaTzgpUob5vGYPBSm1FEueQ3roSLTq6ErGG5HtGWskjCdy5nrHwfhc7cU6XgWyEzXtn5FrN49bHB_Z4BqclhM2C0dWD69FpzwRL-DwykwzrJ9zgmaF8bwdaOdnV5f6semxrUd7-do2tKuJRPzfSqDXpzGpRaMCOKEa21El_rGa07YK3X23oOJRadjotsK9TjOenzpm97SVwEnVe2n7eopT9OKQty3rgJQBJORBefJWWtfMHcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلقک بازی اینو ببینید توی پخش‌زنده صداوسیما
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69422" target="_blank">📅 17:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69421">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVgyC6o9oQiSG8CVED3wBhCvZdS7-9GPjL5JC49EkwZoecStTq6-9V-_Z8zj71sbevXAFOjmE4_CDCu-xF6kDWUwZX25bot7j4TNt1vhAlDzASy9VFrZkg1J42pw6ASSFKlnPeNt_Xme2OPn7y9cqu6vlGEiNTaFDgFBeUbTREBckFdgvJDZnmg7ZGyrgw4GXZT1GW8iqPSJ2D-oBBSd2nmYy-obs6LoteMK65FQD-Cwm1zkB-1GwVcMdwfOW7pMXOUUK3KtjfTEyOq9jZgP6LCkPbipkFKqiLvQFAM8Fy7Tq9H2idA7xOHd2YZ7BM6MaQi7UbWgV9OZ9ITA0rQSIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
نیویورک پست:به گفته منابع آگاه، در حالی که رهبران اعتراضات در تلاش برای دستیابی به سلاح هستند، انقلاب ایران ممکن است «هر لحظه» رخ دهد.
چهره‌های مخالف حکومت در تهران به نشریه «پست» گفتند که خیابان‌های ایران به دلیل اعدام‌های در ملأعام، فروپاشی اقتصادی و جنگی که بیش از پنج ماه است ادامه دارد، به مرز انفجار رسیده‌اند.
یکی از رهبران اعتراضات با اشاره به سرکوب بی‌رحمانه ماه ژانویه توسط رژیم — که به گفته رئیس‌جمهور ترامپ منجر به کشته شدن ۵۲ هزار نفر شد — گفت: «انقلاب ممکن است هر لحظه رخ دهد؛ مردم خواهان انتقام هستند.»
یک روزنامه‌نگار مستقلِ فعال در جریان‌های زیرزمینی ایران گفت که تدارکات برای خیزش بعدی هم‌اکنون در حال انجام است و فعالانی از تمامی اقشار جامعه مصمم‌اند تا ضربه‌ای نهایی و تعیین‌کننده به رژیم وارد کنند.
این روزنامه‌نگار گفت: «ما در حال بررسی اعتراضات ماه ژانویه و تشخیص این نکته هستیم که چه تاکتیک‌هایی مؤثر بوده‌اند و کدام‌یک نه؛ همچنین نقشه‌ها را تحلیل می‌کنیم تا امن‌ترین و خطرناک‌ترین مناطق برای تجمع را شناسایی کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69421" target="_blank">📅 17:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69420">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTASaXybdBvb16fBbQ7Tox1AWtJdojnZ51kGm5v6I2yhEUUUTzcF1FkB5mwVmtHSkLg9IQ6yVeSMjwguxwOmpBOQVajVN8bVIsY-kwPDpNG-Ljt0Y1hDGwq2U02No98N6nC4MsW8nnaPCrYHjoRVjnLq5WqfZO69p_erZ-JPFrvrC_ohhNLStXsb428aGpasEVR7KLXkCtKQb7xs-vxneve0QRA2pjpdxcboSgS0atHLeWvlbLj25HQw-DVO3hwiZnMvH-NIF864Ac7sEWlSuTp_YUhXL1OTWqj6BUVjObAWxSGIwmGZvHYn3Gani7BV1WgO2mGYSY6IU2TXHccphw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
صفحه فارسی وزارت خارجه اسرائیل:
هفته خوبی از اسرائیل برای شما آرزومندیم!
💦
اسرائیل داغ‌تر از همیشه به نظر می‌رسد... و ما فقط در مورد آب و هوا صحبت نمی‌کنیم
😉
🇮🇱
☀️
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69420" target="_blank">📅 16:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69419">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6e5661f181.mp4?token=R4amuocKXsWNG6Un396w1ZGLgmZKAgEod4vv9QOdlPaJtueuibJbcFJzZ-rnOIs1pS1ftf6HrS1sX9Jr3LSv5uzwRP8pW2br6UvfWKA7E8jrkYZAi7wtBlq54bBtP_GgTsUjB9tM80TF8jpZf_V1ipHhKeUxTACVOVtCfiKWURrqa0lJRMyGuXqVgfix__boOgn5rAOX5hDYrG6-oi4xfMFBZNs_lDFbd0CPht_qRnvOH-ZMu5oize6jG-ioEuFCeHWczFm4rSNknEEpBbuiiTK54-9jbvkYin4D3leSMvZW5FJwtCFwc2gT-6yjr6wUqvrg_mKmmZaxMr5yEkn0zg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6e5661f181.mp4?token=R4amuocKXsWNG6Un396w1ZGLgmZKAgEod4vv9QOdlPaJtueuibJbcFJzZ-rnOIs1pS1ftf6HrS1sX9Jr3LSv5uzwRP8pW2br6UvfWKA7E8jrkYZAi7wtBlq54bBtP_GgTsUjB9tM80TF8jpZf_V1ipHhKeUxTACVOVtCfiKWURrqa0lJRMyGuXqVgfix__boOgn5rAOX5hDYrG6-oi4xfMFBZNs_lDFbd0CPht_qRnvOH-ZMu5oize6jG-ioEuFCeHWczFm4rSNknEEpBbuiiTK54-9jbvkYin4D3leSMvZW5FJwtCFwc2gT-6yjr6wUqvrg_mKmmZaxMr5yEkn0zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از نیروهای سرکوبگر: تا تهش پای حکومت وایسادیم، بازم بیاین بیرون بهتون رحم نمی کنیم!
چون داریم دستور خدا رو انجام میدیم، شما اصلا کسی نیستین جلوی جمهوری اسلامی وایسین.
کل دنیا هم جمع بشن نمیتونن کاری کنن، پاینده جمهوری اسلامی!
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69419" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69418">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f215b551.mp4?token=v96wy678nXHOLRRfBbTE0w_0r38y4dM1XW1FboBfdE7Jqrx5hoARWL94nAg6MbZWdkS03pQ2cgF4aGN2hkkoGK4f1jk7_9RZt1Si6eYQppKHiZLP9Ly6FPRbHDEU-HlWph7vjY0SYPRyMhuIozMGMoxnZcaeu3tF8l3DstjnmknUGysBZ1GsOCmxRullok3GfMLf-ZVE2RISR-aqdKQhKB9qccXuzVN-9fnKG9HlRMEGV8oe2jYAOffdYhjzct_HfLqhRpqTZCRckg4I7D94a4xTBf-fRPCKNxCMav0S8Tw3z7QeSW2oupoWQTuqbIGPdBVMBz2K06i3V8qI90YfTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f215b551.mp4?token=v96wy678nXHOLRRfBbTE0w_0r38y4dM1XW1FboBfdE7Jqrx5hoARWL94nAg6MbZWdkS03pQ2cgF4aGN2hkkoGK4f1jk7_9RZt1Si6eYQppKHiZLP9Ly6FPRbHDEU-HlWph7vjY0SYPRyMhuIozMGMoxnZcaeu3tF8l3DstjnmknUGysBZ1GsOCmxRullok3GfMLf-ZVE2RISR-aqdKQhKB9qccXuzVN-9fnKG9HlRMEGV8oe2jYAOffdYhjzct_HfLqhRpqTZCRckg4I7D94a4xTBf-fRPCKNxCMav0S8Tw3z7QeSW2oupoWQTuqbIGPdBVMBz2K06i3V8qI90YfTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدئو با اختلاف زیاد عجیب‌ترین و دارک ترین چیزیه که تا آخر هفته می‌تونید ببینید؛
هربار یکی از این خانواده رو دنبال کنید تا متوجه عمقِ نفهمیدن بشید...
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69418" target="_blank">📅 15:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69417">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90d8743494.mp4?token=UqDOy7iv_x8-AZr7UARrQQD6Qn8ougMDnOTOlqKlu5oUq3aJksY-Puh6JxGk2202h7TaaPw0k1ET96-pfJ6NlyWJyViSuamxK3IwCw0rBhzaB21Vr-5fC3WjjtccyBWRWtJz84tSNCGD4rEymS9H0uBJE2yHdGqHHSwD0JfUI8qsxF156NIX2drzxCGhX3DFiHjhtp0XdM5_kLAUNgMBIIwF1sqVm8EXXtOyYfTxHi4v-NhT9jAiHSgvI9Ogw_1SRH3xdJnWi3smoOpYBq-rIBccjxk3-Bn97SBYC1g4PtCCj-qYp69GSEWMnzBGUgLt2sHq8-SrME7zPyuXGINQbA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90d8743494.mp4?token=UqDOy7iv_x8-AZr7UARrQQD6Qn8ougMDnOTOlqKlu5oUq3aJksY-Puh6JxGk2202h7TaaPw0k1ET96-pfJ6NlyWJyViSuamxK3IwCw0rBhzaB21Vr-5fC3WjjtccyBWRWtJz84tSNCGD4rEymS9H0uBJE2yHdGqHHSwD0JfUI8qsxF156NIX2drzxCGhX3DFiHjhtp0XdM5_kLAUNgMBIIwF1sqVm8EXXtOyYfTxHi4v-NhT9jAiHSgvI9Ogw_1SRH3xdJnWi3smoOpYBq-rIBccjxk3-Bn97SBYC1g4PtCCj-qYp69GSEWMnzBGUgLt2sHq8-SrME7zPyuXGINQbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بر اساس تصاویر ماهواره‌ای، پایگاه هوایی شیخ عیسی در بحرین که مورد استفاده نیروهای آمریکایی است، اخیراً تخلیه شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69417" target="_blank">📅 15:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69416">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba4d1f7356.mp4?token=T0pmDkVSwb7ZjCaf5_MgrCgZJx6clBiHpKpP__GDzBFmcu5xtOZQ9stfZ4i8uC9lIjBYrMPwLiYws0QZM-1SpXC14fsDPTyKirfW-Y4oKPmbj9xgpKgmgEHUywjIGszAdiKdWt9m4UpbIVnqp6sTV3O42b5DgiF3ie69Keed7AVdEAiMub0TNQEaMmTurZbe1wzIRUgC3K8SIjc_BV42sMHzDiQ-cr1du8XijiwGeGMXVYBgmppJNd3KgtWle5GE2h78sEDQhl5cR9lRMciPHztL43YG_WOzloZUnvbJGnZrKdP9gCGJQtUSrlMSllYJJA3DuzCQldulgX_0UAVgUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba4d1f7356.mp4?token=T0pmDkVSwb7ZjCaf5_MgrCgZJx6clBiHpKpP__GDzBFmcu5xtOZQ9stfZ4i8uC9lIjBYrMPwLiYws0QZM-1SpXC14fsDPTyKirfW-Y4oKPmbj9xgpKgmgEHUywjIGszAdiKdWt9m4UpbIVnqp6sTV3O42b5DgiF3ie69Keed7AVdEAiMub0TNQEaMmTurZbe1wzIRUgC3K8SIjc_BV42sMHzDiQ-cr1du8XijiwGeGMXVYBgmppJNd3KgtWle5GE2h78sEDQhl5cR9lRMciPHztL43YG_WOzloZUnvbJGnZrKdP9gCGJQtUSrlMSllYJJA3DuzCQldulgX_0UAVgUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر مارو خندوندی حاج اقا دارم پاره میشم
👅
👅
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69416" target="_blank">📅 14:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69415">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇮🇱
بنسالل اسموتریچ، وزیر دارایی اسرائیل:
رژیم ایران در جریان جنگ سقوط نخواهد کرد.
مردم ایران در شرایطی که هواپیماهای اسرائیلی و آمریکایی بر فراز آسمانشان در پرواز بودند، به خیابان‌ها نمی‌آمدند؛ چرا که نمی‌خواستند در نظر دیگران، همدست دشمن به نظر برسند.
تأکید اصلی باید بر این موارد باشد: اقتصاد، اقتصاد، اقتصاد و باز هم اقتصاد. این همان عاملی است که در نهایت موجب سقوط رژیم خواهد شد.
به گمان من، رژیم ممکن است به نقطه‌ای برسد که شهروندان عادی احساس کنند دیگر چیزی برای از دست دادن ندارند.
وقتی چنین وضعیتی پیش بیاید، ترس دیگر مانعی نخواهد بود؛ آنگاه مردم به خیابان‌ها می‌آیند، قیام می‌کنند و رژیم را سرنگون می‌سازند.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69415" target="_blank">📅 13:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69414">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
خبرگزاری فارس، وابسته به سپاه:
گزارش‌های حاکی از موافقت ایران با بازگشایی تنگه هرمز نادرست است و هیچ تغییری در سیاست تهران ایجاد نشده.
منابع نظامی گفته‌اند این آبراه راهبردی همچنان بسته است و عبور از آن نیازمند مجوز صریح و هماهنگی با نیروی دریایی سپاه پاسداران است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69414" target="_blank">📅 12:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69413">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835653bd72.mp4?token=unXIY9U9RZjd_WHNI4oNcESMa36ye20BIbQ64MLeh6gLoYJ7ZtDIQMptgRCOFetdusTjz0fjLN3u5UE6VxQy8gVdGCwXdb6snwNd_2q1WPArc4ZmF8QT7NDpVATqhOgjTRn7YOdTeMe5qjqpNBzCCPMhhDQKeGUHbPFcxYwiO9yrG-xQ1Hy9cl5ptSWD9n6SeGu0-3HD8BLDe-SwMWDlq0j17nN7taphlznAKI2GaYxo2aVsMyLt-788G25AL6RahdDe7gAHMx2qc5wMBEPW4R2DhH3NGV5GUKZEzF1KlF1n9l3ZJ4MOh9HUGrfkKkYPvS_Vu8sEMHMNrymEdFyo-JP8V3OYQmVPDoz3TW8zKe_N2obNkneijx4S8D_jaETuKZqkpZOc93risDqfqcSA5cuOrsJMCTA1E18rfF57iN1ixZX-ydXxvD8AZRI2et8qCPwwP9U5YtpTtzJYxUULhxA93svI7fnl1dSmF7feg32pZLvaE5kiPgv8YTOEY6Es6rJKCJvBitHsUTd9Gs6uKd7EgKD2Myq_YtOk-vxQ5MYx5ZO1KddHR1NHNG2zHg2AZtZGyZz8ll_EGWUs-j_XAcoDNkksCvK4twsfUFjBnoXbEvNTMnq80_t1QzC4Nb81894-aqauZUSH4DcIFwwvZKR0b8djELDZ18ersyiRLyU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835653bd72.mp4?token=unXIY9U9RZjd_WHNI4oNcESMa36ye20BIbQ64MLeh6gLoYJ7ZtDIQMptgRCOFetdusTjz0fjLN3u5UE6VxQy8gVdGCwXdb6snwNd_2q1WPArc4ZmF8QT7NDpVATqhOgjTRn7YOdTeMe5qjqpNBzCCPMhhDQKeGUHbPFcxYwiO9yrG-xQ1Hy9cl5ptSWD9n6SeGu0-3HD8BLDe-SwMWDlq0j17nN7taphlznAKI2GaYxo2aVsMyLt-788G25AL6RahdDe7gAHMx2qc5wMBEPW4R2DhH3NGV5GUKZEzF1KlF1n9l3ZJ4MOh9HUGrfkKkYPvS_Vu8sEMHMNrymEdFyo-JP8V3OYQmVPDoz3TW8zKe_N2obNkneijx4S8D_jaETuKZqkpZOc93risDqfqcSA5cuOrsJMCTA1E18rfF57iN1ixZX-ydXxvD8AZRI2et8qCPwwP9U5YtpTtzJYxUULhxA93svI7fnl1dSmF7feg32pZLvaE5kiPgv8YTOEY6Es6rJKCJvBitHsUTd9Gs6uKd7EgKD2Myq_YtOk-vxQ5MYx5ZO1KddHR1NHNG2zHg2AZtZGyZz8ll_EGWUs-j_XAcoDNkksCvK4twsfUFjBnoXbEvNTMnq80_t1QzC4Nb81894-aqauZUSH4DcIFwwvZKR0b8djELDZ18ersyiRLyU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گزارش روزنامه همشهری از دلایل عدم انتشار صدای مجتبی خامنه‌ای :
از طریق صدا میتونن پیدا بکنن چون هر فضای بسته امضای صوتی منحصر به فردی داره و از بازتاب صدا از طریق فرش و دیوار میتونن مکان رو تشخیص بدن و ارتفاع اتاق و فاصله گوینده رو از محل بازتاب رو پیدا بکنن
همچنین از طریق تحلیل شبکه برق میتونن ردیابی بکنن چون همهمه ضعیف الکترومغناطیسی در پس زمینه صدا ضبط میشه و سرویس های اطلاعاتی میتونن از طریق شبکه های اتصال برقی مکان رو ردیابی بکنن
هر میکروفون و دستگاه ضبط اثر متفاوت داره و مختص خود دستگاهه مثل اثر انگشت خود شخص لذا از طریق ردیابی دستگاه میتونن مکان رو پیدا بکنن
صدای پس زمینه مثل خنک کننده ها یا ژنراتور ها و حتی توی مکان باز صدای ترافیک ها و صدای محیط و نوع حشرات و پرندگان میتونن محل جغرافیایی رو لو بدن
😳
😳
ویس ابعاد فیزیکی نای دهان و مجرای صوتی رو نشون میده و حتی فیلتر هم باشه با دستگاه هایی میشه ردیابی کرد و تشخیص داد طرف زنده باشه محل حضورش کجاست
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/69413" target="_blank">📅 12:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69412">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🇺🇸
ویدیو ای که صفحه رسمی وزارت جنگ آمریکا به تازگی منتشر کرده
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69412" target="_blank">📅 11:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69411">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb1d460275.mp4?token=GjmJK1ZsCvRmnCC7KiT7QrzN6soHWpA9Ij2n6iV2fKCEsZKmt9NaCeHj-8e5tyAvJp-_5JnHZ1bWx9M4tnAhlFaAx8LWASptuecdy1XYNllmoRk4cN1mEyiHyd4psrep0_th7-xGjB5n99HCwzKP3grQmRGTsUln4zTjKELxuDKf50XhRUnFlXE1ILiyG81JbmZIaCMpsfjspf-TQlWEnFMcFtoGjVahN84DCQE_bsS9rAB3aqSAtBCXMmA89gtRcTpQo7yjSAO6x2NkHUzAl1RW9qYDtKZNLgo3j0b07dVXzKLUhXAn_pXv-IYVMx4a-6xlf62qz5tKmNx7DWOCzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb1d460275.mp4?token=GjmJK1ZsCvRmnCC7KiT7QrzN6soHWpA9Ij2n6iV2fKCEsZKmt9NaCeHj-8e5tyAvJp-_5JnHZ1bWx9M4tnAhlFaAx8LWASptuecdy1XYNllmoRk4cN1mEyiHyd4psrep0_th7-xGjB5n99HCwzKP3grQmRGTsUln4zTjKELxuDKf50XhRUnFlXE1ILiyG81JbmZIaCMpsfjspf-TQlWEnFMcFtoGjVahN84DCQE_bsS9rAB3aqSAtBCXMmA89gtRcTpQo7yjSAO6x2NkHUzAl1RW9qYDtKZNLgo3j0b07dVXzKLUhXAn_pXv-IYVMx4a-6xlf62qz5tKmNx7DWOCzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
واکنش پزشکیان به تاخیر ۱۰ روزه در  پرداخت حقوق اعضای هیئت علمی دانشگاه‌ها:
این واقعاً قابل قبول نیست، کاری کنید که اساتید بیش از این ناراضی نشوند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69411" target="_blank">📅 11:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69410">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🇮🇱
کانال۱۲ اسرائیل:
عراقچی، وزیر امور خارجه ایران، شبانه با یک مصالحه میان قطر و آمریکا برای بازگشایی تنگه هرمز موافقت کرد؛ اقدامی که باعث شد دونالد ترامپ، رئیس‌جمهور آمریکا، حملات تلافی‌جویانه برنامه‌ریزی‌شده را لغو کند.
بر اساس این طرح، کشتی‌های عازم خلیج فارس از طریق آب‌های سرزمینی ایران وارد و از مسیر آب‌های عمان خارج خواهند شد؛ هرچند عمان خواستار تأیید رسمی این موضوع شده است که سپاه پاسداران از این توافق حمایت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69410" target="_blank">📅 11:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69409">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66dc919056.mp4?token=NO9eLytEUFuJWznaQ_-5xc3HrDUcrPG_h9KzRLAFGPoZHZSztQN7gaJJtGidNVefWnd4ngal2q_jFFbAwQe45dVSpptsXjZDD8GBa2OLrxwSlDCjzjqV1AuVVsStgRt8COWuZ6XAWXq5a1ftXbSg5Bm1Uo89-2fOzCLvfj-IG9Pfw-BnmJvko0K4p1k0EtVcat1_tcUMGgUen4WpfY80CW2ZqTKXfAmemYi3H7M3Fmk8sfJL9u_Wvdj9v3uctGUiy4JgPwBAm1EB2xtay70qcgiLD6GyRF3k62FUXHqb0l1ZqEHA7Inw83BVd_NvtgV4HnOk1M5yhNH8fP2DTcgZQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66dc919056.mp4?token=NO9eLytEUFuJWznaQ_-5xc3HrDUcrPG_h9KzRLAFGPoZHZSztQN7gaJJtGidNVefWnd4ngal2q_jFFbAwQe45dVSpptsXjZDD8GBa2OLrxwSlDCjzjqV1AuVVsStgRt8COWuZ6XAWXq5a1ftXbSg5Bm1Uo89-2fOzCLvfj-IG9Pfw-BnmJvko0K4p1k0EtVcat1_tcUMGgUen4WpfY80CW2ZqTKXfAmemYi3H7M3Fmk8sfJL9u_Wvdj9v3uctGUiy4JgPwBAm1EB2xtay70qcgiLD6GyRF3k62FUXHqb0l1ZqEHA7Inw83BVd_NvtgV4HnOk1M5yhNH8fP2DTcgZQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
با این حال، تغییر رژیم هرگز هدف اصلی نبوده است؛ هدف، خلع سلاح هسته‌ای بوده است. آیا می‌توان یکی را بدون دیگری داشت؟
🇺🇸
مارکو روبیو:
هرکاری که توی خاورمیانه و جهان انجام دادیم کسی مانع ما نشده و موفقیت بدست آوردیم
رژیم باید تغییر بکنه شما شاید تغییر رژیم نداشته باشید ولی باید اینا تغییر بکنه
اونا میخان
انقلابشون رو به کل دنیا صادر بکنن و باید این تغییر پیدا بکنه
ایران تابحال با رئیس جمهوری مثل ترامپ که مرد عمل هست رو به رو نشده
اونا هنوزم موشک و پهپاد دارن میتونن صدمه بزنن ولی خب سپری ندارن پشتش قایم بشن
از روی قدرت باهاشون مذاکره میکنیم نه ضعف
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69409" target="_blank">📅 10:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69408">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb72a3070d.mp4?token=ou1K40_9R-zEE8DwUjhrdsCNcp9HGjHObPL-Tti3maaYkK2vuNiHo5OXF6p0P7jq9pYjjxVYSXpXN3bItD12DAY1BXYA2H60Ac2X0heVvBfcJV2fC_3Kpn3nqKq8LpkaYbu18ctpscKKyMO86GnY3fFR90ajyIjypss6tZAZ-A7YaOLAMYMKlt6O4Ua9o9HMEx-AIr_YG4tyU8cw27rKrKEHsvqyW-cxwyHt6q9gL9XVyhQsLcto-9XVi-JxeW3dvJLi1eyCSkT6MOIvWOsFotqSLD_-JZaa_M8jpkmXvJeZhAzb5Ta5-8TLAi4OYLYs38ks6MVkVdusdAQGsJyVgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb72a3070d.mp4?token=ou1K40_9R-zEE8DwUjhrdsCNcp9HGjHObPL-Tti3maaYkK2vuNiHo5OXF6p0P7jq9pYjjxVYSXpXN3bItD12DAY1BXYA2H60Ac2X0heVvBfcJV2fC_3Kpn3nqKq8LpkaYbu18ctpscKKyMO86GnY3fFR90ajyIjypss6tZAZ-A7YaOLAMYMKlt6O4Ua9o9HMEx-AIr_YG4tyU8cw27rKrKEHsvqyW-cxwyHt6q9gL9XVyhQsLcto-9XVi-JxeW3dvJLi1eyCSkT6MOIvWOsFotqSLD_-JZaa_M8jpkmXvJeZhAzb5Ta5-8TLAi4OYLYs38ks6MVkVdusdAQGsJyVgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مرادویسی، تحلیلگر ارشد اینترنشنال:هدف‌های احتمالی آمریکا تو جنگ جدید میتونه شامل این موارد بشه:
1. مراکز نظامی سپاه تو جنوب کشور
2. شهرهای موشکی و پهپادی تو عمق خاک ایران
3. تاسیسات هسته‌ای "کوه کلنگ"
4. مراکز نظامی سراسر کشور
5. سامانه‌های پدافندی و راداری
6. پایگاه‌های هوایی ارتش
7. مراکز و نهادهای حکومتی
8. ساختارهای سرکوب (سپاه، بسیج و نیروی انتظامی)
9. مقامات و فرماندهان ارشد باقی‌مونده
10. مکان‌های نمادین مثل صداوسیما
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/69408" target="_blank">📅 09:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69407">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cbd0e326f.mp4?token=cTA1oxOahzFUaZG7BAZttVMQBmQCCMZY6jH2VHsstQd9HFEOM9zfWo-l2Z5Czf0zP34sbGkWSmyB8uuOXW5SMfbcTZw_j5cPaHORT-xgPbJyw14GQEFJ4Zh2DRhvtJCzAZvV8c86m1UkgNFRCaNcEZ1cBdLwa39zcUBCAL_DXN2rNIlc_WZHmmZzNOUzPwgvuPDj1j6yQKf-MuHaCiQMDY2qTlnPxpgZcEtRY2h20L6FYPLu6Z8Mj0wiwnuNTaAY2HARmt2Y2YipgQBE72rWqpbzGVuIcODaqllUSChfUb48SjBwhv4MJOvJadOYHk9YSgF-IM5Q0GrTIGCUuEY7QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cbd0e326f.mp4?token=cTA1oxOahzFUaZG7BAZttVMQBmQCCMZY6jH2VHsstQd9HFEOM9zfWo-l2Z5Czf0zP34sbGkWSmyB8uuOXW5SMfbcTZw_j5cPaHORT-xgPbJyw14GQEFJ4Zh2DRhvtJCzAZvV8c86m1UkgNFRCaNcEZ1cBdLwa39zcUBCAL_DXN2rNIlc_WZHmmZzNOUzPwgvuPDj1j6yQKf-MuHaCiQMDY2qTlnPxpgZcEtRY2h20L6FYPLu6Z8Mj0wiwnuNTaAY2HARmt2Y2YipgQBE72rWqpbzGVuIcODaqllUSChfUb48SjBwhv4MJOvJadOYHk9YSgF-IM5Q0GrTIGCUuEY7QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
حاکم بحرین:
حضرت محمد (ص) پس از قرن ها تاریکی در ایران به آن عمق روحی، انسانی و معرفتی بخشید، بخاطر تشکر از این کار حداقل دیگه به بحرین حمله نکنید.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/69407" target="_blank">📅 09:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69406">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaQMQQSvjZcrO_Y53Wtt8mT4mZSyEy1EAZzPjAt5wcsq7TmI0PYedD9c947_-eDHF2sDVxjvxD790PnmiL-myog1HtxdeEUaIymikkQd-uLiAJpSn1-ttK8OZxjBJxWPGlZuBuD0Wd_yY1WDjmdbBrPjwps2r5mwX5reif_CrK8UXwBp8v_NErgTbqeTbG-CtdwcgBdZ4sxvO_NC395rwNnX2DCyEcUf80AO3uxuntE-mOi5hV3ROSyrw6ZJDhrKqnFfEaK1KuwhViKLPFqZ0ntDgaoeeDTPD2BJ7TzXIqJ-9U-ZGVB6-bzbI7Vb9xDanU-jTNBva9DRQ0mgMStEXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: حمله رو کنسل کردم
!
ایالات متحده آمریکا آماده و مجهز به سلاح است تا علیه جمهوری اسلامی ایران، در سطوحی از ترور نظامی، قدرت و صلابت که از زمان جنگ جهانی دوم دیده نشده است، اقدام کند. با وجود این، ایران و سایر کشورهای خاورمیانه از ما خواسته‌اند که هرگونه حمله‌ای را در چارچوب توافق‌نامه‌ای که مورد توافق قرار گرفته است، متوقف کنیم. این شامل بازگشایی فوری، کامل و تمام‌عیار تنگه هرمز و پایان دادن به تهدید هسته‌ای ایران می‌شود. بر اساس این درخواست، من برای منافع آینده جهان و همچنین بقای یک ایران موفق و مرفه، موافقت کرده‌ام که حمله را لغو کنم، مشروط بر اینکه بتوانم به سرعت به توافق‌نامه‌ای دست یابم. کشور اسرائیل در این تعهد به من می‌پیوندد. همه دست به کار شوید و آن را انجام دهید. از توجه شما به این موضوع متشکرم! رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/news_hut/69406" target="_blank">📅 06:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69405">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeSbl-QwvXzteQ-uyTocK56xczBVn67p62BPn1M07roxMT4a4f8FVQPadZv3rzXx4rEfpXG14prCr7wcVEaYnTHFWEtrvm2WsMAQrWf4GS02vUtLeija5S4oTOngH9K-FIC8WSqtaNiEMizeexuIYQq_tdrA6mG9uCSXmDcoLJWM2DQjCtVY8vDqloIwRk0AuNhHVfniNnKxunV0o38hhfcB4SNq1wOtzr-2OAYg2lrL14bdfK6Fsgk4jBZh8T5UP0I_tOvD7BCQ7O3_P4mdWV7Cp9loMInTyg49umEo_kpkU1VtkVneqAT4NXZZb7jYzol7bUVNcst-oGvIa6utxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیکه و ترامپ چیزی نگفته.
#hjAly‌</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/69405" target="_blank">📅 02:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69404">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6db9d071b.mp4?token=upIlyHDC-3NtVtDbn9nxDEHB9juXOptKb3obaFAURBFQ5IUnUx9yTRj4wHgMARdskvsF-3ztq0rCG-QIhn-ZPjVKgD0-GEf0cQtcPbM3uGngmNCXkGKKYkgElW2RT7YjaOQEZMsTsE7xyAbig7nRQX4k1gmOKx3sfu0eWWf4fYDG99DyryFMC2mBAoiKqQ-MwCIV3HJPHdejhpwt6WK8-tNecUbW4K1Rn8m5YSSXcyk2wHJy8YH2oToyKddmBndNnIGHQq8EUTZBpvo_zRaFja7qd0AMl0O2O1xFH6cIB0l0k1yh3cCYyN516Quz0uB6zngnG2QUaD-skr66cBVNNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6db9d071b.mp4?token=upIlyHDC-3NtVtDbn9nxDEHB9juXOptKb3obaFAURBFQ5IUnUx9yTRj4wHgMARdskvsF-3ztq0rCG-QIhn-ZPjVKgD0-GEf0cQtcPbM3uGngmNCXkGKKYkgElW2RT7YjaOQEZMsTsE7xyAbig7nRQX4k1gmOKx3sfu0eWWf4fYDG99DyryFMC2mBAoiKqQ-MwCIV3HJPHdejhpwt6WK8-tNecUbW4K1Rn8m5YSSXcyk2wHJy8YH2oToyKddmBndNnIGHQq8EUTZBpvo_zRaFja7qd0AMl0O2O1xFH6cIB0l0k1yh3cCYyN516Quz0uB6zngnG2QUaD-skr66cBVNNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آسمان سلیمانیه
@News_Hut</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/news_hut/69404" target="_blank">📅 02:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69403">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5cdd81f13.mp4?token=MIeh-H0KklqueoSX12E_GkegGSyhqoUs1Gb6GuiRXIfv22DGTHsyLZcTHvvygw8EKyfRMHmjCzsO-4Q0nEQm3199ev4113AzMb8Rqi9xCqrMZ820lr_rjY2xK4qr9QvmN6sYRTdPIxEdF09bqTL-uc9akoxtRNffgOGGI5VoMxhkRvj6O3YhWba76h_kzWJ9TKtmJmq9WLfwR_iZ9rwyx6KvFdlFx90zaiAUzBVJhfq7I0HJr08Dkfb1jAMIQQ5AkGZjfdfPVkc2qEcgRvusTZkCFMepZ31-fsWTdJfzKo9fpvdkaT17QsPiTTzeWsPyPvfyAE1h8WNjaMiaqhbFbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5cdd81f13.mp4?token=MIeh-H0KklqueoSX12E_GkegGSyhqoUs1Gb6GuiRXIfv22DGTHsyLZcTHvvygw8EKyfRMHmjCzsO-4Q0nEQm3199ev4113AzMb8Rqi9xCqrMZ820lr_rjY2xK4qr9QvmN6sYRTdPIxEdF09bqTL-uc9akoxtRNffgOGGI5VoMxhkRvj6O3YhWba76h_kzWJ9TKtmJmq9WLfwR_iZ9rwyx6KvFdlFx90zaiAUzBVJhfq7I0HJr08Dkfb1jAMIQQ5AkGZjfdfPVkc2qEcgRvusTZkCFMepZ31-fsWTdJfzKo9fpvdkaT17QsPiTTzeWsPyPvfyAE1h8WNjaMiaqhbFbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
حملات سپاه به‌ سلیمانیه عراق
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/69403" target="_blank">📅 02:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69399">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UFG1x6sbSYKbHzDNVKNAWiDLBFgR61OujRLb-VeXuxkNW9ctW7RctXp2z767hbeaJrTWglQ5m0dD2-SSTje7c4qrxG3tWISrpnHEzJhjO_rEwJyWXbng-8KDsbOiYQdHcQjJwMlsI75m6FAdtIrqyQpdFUEyASboQpPA_9nQjTvxO5VZoqBQcxD9BiYYQdeMfPputY3yMWEDOQcHy6H1c_TXj_NCid1JiX6IsXSke4qwS8A1XHA9yxI61v3H5dqCKl329dknJouGncSpsYj9K3WMiF-YqP28Df76QCrn3d7cgCqU32oDqROXOAnfTiguoM3beiNk7jTbwmYrj-hFYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IHN2Squ_qDyul-vigEmV3PCwZuFN1GQc8_BeuX4JYjuAQmQtnj16KfkaicxzWL4Ll0AqAVU6Moz7ZWj4AyV38SJH2XFUGIKyboeuPgQIiIwoyAeXg0MvT64SPWOQxYjjTF2Pb2nLqze38WA6NwwEuw4HRpojxlcnrI1tScZlSO6q_qCJ5kW9JadC1_JP6nsenWCxkxIs2Th0s_ZKKGpkbI4dtABdFZJ1og5WKaGLG7QlHCAKeIebIwJWSMZ9-_lHPxUz9U4cNcsGFfYg70RPplnL9Cgao1cyiJ6jRj4lThfI__WfGTbwhfPf9G0zb_aRYGYEQOIQ2WBJl4IcZ0vC1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ea496ad43.mp4?token=rUQmVVS_52n05JGFGbFB4gRLKmQw75fbP2h-DN7K1JjQd-Lq5mpB6AVvXt8V5e0rg-XnGvADIb8shUSyaS7aN30GxsAtQYK-5d8bG3tfhAFQOOYi0ldgIWbi0ZM0BkyuVx2otiIt7DXNbZ_JgkB_aH45A1whL_-AM0uxtQ4DdPqMH0w-J7GFvxEtCImKp2VT1N_hI3xGvuI9kqU62uDhHr3GEQyIJHM4Kg_nRCS5dYY1RBVwM7s5l4TVoiqDRoKmyvJBUHOWB9Qip5NkrhLUdfA6Lnm8Wp-AZqA4g-MGfnxRNfmhEpR8rB2ZU5sWtKthiTPiZnpJ0W0tLt0OMFl6Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ea496ad43.mp4?token=rUQmVVS_52n05JGFGbFB4gRLKmQw75fbP2h-DN7K1JjQd-Lq5mpB6AVvXt8V5e0rg-XnGvADIb8shUSyaS7aN30GxsAtQYK-5d8bG3tfhAFQOOYi0ldgIWbi0ZM0BkyuVx2otiIt7DXNbZ_JgkB_aH45A1whL_-AM0uxtQ4DdPqMH0w-J7GFvxEtCImKp2VT1N_hI3xGvuI9kqU62uDhHr3GEQyIJHM4Kg_nRCS5dYY1RBVwM7s5l4TVoiqDRoKmyvJBUHOWB9Qip5NkrhLUdfA6Lnm8Wp-AZqA4g-MGfnxRNfmhEpR8rB2ZU5sWtKthiTPiZnpJ0W0tLt0OMFl6Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇷🇺
ساعاتی پیش یه انفجار تو یه رستوران تو مرکز مسکو رخ داد؛
جایی که به گفته منابع روسی، مراسم عروسی خصوصی با حضور چند نفر از فرماندهان ارشد نظامی در حال برگزاری بود.
کانال‌های تلگرامی روسیه می‌گن "الکساندر چایکو"، فرمانده نیروی هوافضای روسیه هم بین مهمون‌ها بوده.
گزارش‌های اولیه حاکی از کشته شدن دست‌کم 3 نفر و زخمی شدن بیش از 20 نفره!
@News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/69399" target="_blank">📅 01:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69398">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⏺
المیادین:
بر اساس اطلاعات بدست آمده، گروه‌های کرد حاضر در خاک عراق در حال آمادگی و برنامه‌ریزی برای اجرای عملیات علیه جمهوری اسلامی ایران هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/69398" target="_blank">📅 01:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69397">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پمپ بنزین‌های مملکت بخاطر حملات احتمالی، دوباره شلوغ شدن.  @News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/69397" target="_blank">📅 01:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69396">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff498baa1d.mp4?token=uU6mA4kw3Uev6Ud7FY-PrwJfxntjFj_w4UAt46EyAKawAHXaILixz6TIYG8IvPN4HDhLPY50V6W8ts2j3lz5ExKqOd8iq9Ld0cwx-_I3VyIDDB6opO1MIIpmgmKR2WfcQFuCqcEmxxRNGHT3BDhidFSuU_u7R_U1y7lw_6qVF1ohSK6efoK_wuJJrJSK9gb2El3hapsX1DRUFyC32C013SMKTAp9qVhAc5ncSr87GKiDWIoL2-dSPMaSYoU9e1HRNZ7XHWEESCdPZyvobGA-9Z3zDGapxbc5vELiLT7Sx80QlQE6520wIAMaLX6rRqmkpkRktaBkdCwdnc-G9QeeZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff498baa1d.mp4?token=uU6mA4kw3Uev6Ud7FY-PrwJfxntjFj_w4UAt46EyAKawAHXaILixz6TIYG8IvPN4HDhLPY50V6W8ts2j3lz5ExKqOd8iq9Ld0cwx-_I3VyIDDB6opO1MIIpmgmKR2WfcQFuCqcEmxxRNGHT3BDhidFSuU_u7R_U1y7lw_6qVF1ohSK6efoK_wuJJrJSK9gb2El3hapsX1DRUFyC32C013SMKTAp9qVhAc5ncSr87GKiDWIoL2-dSPMaSYoU9e1HRNZ7XHWEESCdPZyvobGA-9Z3zDGapxbc5vELiLT7Sx80QlQE6520wIAMaLX6rRqmkpkRktaBkdCwdnc-G9QeeZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پمپ بنزین‌های مملکت بخاطر حملات احتمالی، دوباره شلوغ شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/news_hut/69396" target="_blank">📅 01:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69395">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUr-UISTM0A4RmgTXCx5ZBJnUiDYIkwM-XdxuMTNOVR33O4cfsBPri_NG5F5i0uBgI4273MDalPw_yiXXGE-GCjhD_nCjXkGtvgeGBqda11S4LMDHkAjUlEo92T4niHkQ3l1FGEV30tcHTciBYQLTlnfuFgb2X2Mp-BJlT2SYh_hiX1OxzMDXXr0oXt22QDKjDMjkqHB1_12sCWxnEzHTXIg2JeU6Ln2YS55uQd_FVYe1WSs5VD0oQQMmHN7_AwUyE6HpugEyWXY6T_hPSRg0ng2H8pAJ5FLWWjAS_qw_oggrQAk7o0q0-l6EmHnIkBVBWXLkkivicddcAJGJMGgsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
توییت اتاق جنگ اسرائیل و اون ساعت شنی معروفش
@News_Hut</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/news_hut/69395" target="_blank">📅 00:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69394">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b418c0b947.mp4?token=YOvjTToNiMW19Bi_CrY943RdjeanFEkPU6Cg_VLRe2uDccDaX16DgnK9Vs5gOlXh2K3_Mx0GUeve_nHozWIBWU7BAqi-idjYNxnJbNyhFi14Sr0bUKK60feuSggVy5hVy95SYd7xin0SOjAtuMi2CL95SD0MIgvfXlHd9PivvnUhPjnoG9NSqG6Tqf7ZDUwxv6LEn40PXXTJldaYDuIqSOvqocMz4mL2DsPVPUNBy7RUbqCi22PasrdYQePiKw7U9NiosQUDrO9j432rrhZpDZGNDhqWG-FmkBu1B0ONaTX5jlaaCzWqe0ywGf9g8DtgHEjwKGPxKcle2D-x4FCJAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b418c0b947.mp4?token=YOvjTToNiMW19Bi_CrY943RdjeanFEkPU6Cg_VLRe2uDccDaX16DgnK9Vs5gOlXh2K3_Mx0GUeve_nHozWIBWU7BAqi-idjYNxnJbNyhFi14Sr0bUKK60feuSggVy5hVy95SYd7xin0SOjAtuMi2CL95SD0MIgvfXlHd9PivvnUhPjnoG9NSqG6Tqf7ZDUwxv6LEn40PXXTJldaYDuIqSOvqocMz4mL2DsPVPUNBy7RUbqCi22PasrdYQePiKw7U9NiosQUDrO9j432rrhZpDZGNDhqWG-FmkBu1B0ONaTX5jlaaCzWqe0ywGf9g8DtgHEjwKGPxKcle2D-x4FCJAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محمود احمدی‌نژاد درباره دستگاه سرکوب جمهوری اسلامی:
نیروهای امنیتی خود افرادی را به میان معترضان می‌فرستند تا با ایجاد تلفات و آسیب به اماکن عمومی، بهانه‌ای برای سرکوب خونین فراهم کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/news_hut/69394" target="_blank">📅 23:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69392">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B4Bk5fLVFhXVimsxfsKfVUob-gZtj2g9v0F7Rrufn_Yk7wbfWRYzAczFvRppO3FR_Uk5_o2tSjdmDP5fOPpX1yCTCRQ78EjGQOVcBOoDZESu9UwVvueHVZsakkC4CkFHku4FLLUQA7xPKIYBmuQEBc7Y44EWzGzzWKWrd6sSuCYcUsbjbaoYvJSRb3IhAHKTDfp40_PgE2JdgTXX0UFfkkj3I_orWgl7fa5mvsW5W-SdUJMaUjdF3U1CvoqgKlamwwHDRUL7KMRFslhQz1iZu2QJmhrSUbPk_QDsqG4fZWunSgXLsTsuYfyCia1_LFvwQssWz2-L7I8oVdkpJWmeMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82ccfb8ec6.mp4?token=c-m8m3u14Nner1Rm__0Gj4eAaAWInM1vA4D9A89pLBcSYrZZWTfbgSUObYFN7gSRa4ffb84JlJ1ECTGmuCfj_NFq-P2kppU6vrwOpXgVGTdhfFiKIH_i7_oe6zMvaTB7x8-81AMIlhWmDnmd1-v4DiSMGWoX2Yka_rUpiBbsg_ygMXgTvJ7ddFFYC0W9Rg6HZj97fbB1s6Eda8aF4xy5Qc56K7DY-fVTKHTxCOJXO80Sx8_GWDQteOuG_L96WCFP4aKJuAq6Jp2ObTko93WNY8gbGYU0EDVvi8zZsItYFtvNTahr6fNS3Dqy2AOtaW4m8z5xzT7pwzCM9SkR_3ydTw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82ccfb8ec6.mp4?token=c-m8m3u14Nner1Rm__0Gj4eAaAWInM1vA4D9A89pLBcSYrZZWTfbgSUObYFN7gSRa4ffb84JlJ1ECTGmuCfj_NFq-P2kppU6vrwOpXgVGTdhfFiKIH_i7_oe6zMvaTB7x8-81AMIlhWmDnmd1-v4DiSMGWoX2Yka_rUpiBbsg_ygMXgTvJ7ddFFYC0W9Rg6HZj97fbB1s6Eda8aF4xy5Qc56K7DY-fVTKHTxCOJXO80Sx8_GWDQteOuG_L96WCFP4aKJuAq6Jp2ObTko93WNY8gbGYU0EDVvi8zZsItYFtvNTahr6fNS3Dqy2AOtaW4m8z5xzT7pwzCM9SkR_3ydTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زهرا کاظمیان از حامیان جمهوری اسلامی در انگلیس که کارش زیرآب زنی مخالفین رژیم بود، دستگیر شد.
حالا فیلم لحظه بازداشتش رو ببینید که پلیس اومده بازداشتش کنه، میگه تروخدا بذارین زنگ بزنم پلیس
@News_Hut</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/news_hut/69392" target="_blank">📅 23:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69391">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28c29c1e71.mp4?token=u1Swp1C6esjIsEZ4K5JfDJeth9gOlo7Ok1TCBOHP-6qRYQrp6E6GaRSZkl9bV9af3uvDLgVz8tRlqMTOaXMyykVaQJV3Nasu1TYrg0vRsEwhUdNPeQwJB1HlDJ8VGLv2BbBIlW4IH3E0Da1eVeNx1wQxahwlp29ewWwjRkzJ7E5qUXmqlNLB_OKJOr5fV6JoA3H7h4y3DNy_KvHAyRpPO8HaWnsOc5g-Qwv7ImDtInB_BeE5KY-HzNMLjuMEmZcZcrTzXHPC_XuoZrvfD5QQOsOiOxuZVloRatqMJs3oYyqyWZn9Tl7gWoXWPw5PlzQTXusiyNZF3SauBIYx-928og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28c29c1e71.mp4?token=u1Swp1C6esjIsEZ4K5JfDJeth9gOlo7Ok1TCBOHP-6qRYQrp6E6GaRSZkl9bV9af3uvDLgVz8tRlqMTOaXMyykVaQJV3Nasu1TYrg0vRsEwhUdNPeQwJB1HlDJ8VGLv2BbBIlW4IH3E0Da1eVeNx1wQxahwlp29ewWwjRkzJ7E5qUXmqlNLB_OKJOr5fV6JoA3H7h4y3DNy_KvHAyRpPO8HaWnsOc5g-Qwv7ImDtInB_BeE5KY-HzNMLjuMEmZcZcrTzXHPC_XuoZrvfD5QQOsOiOxuZVloRatqMJs3oYyqyWZn9Tl7gWoXWPw5PlzQTXusiyNZF3SauBIYx-928og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
کانال 13 اسرائیل:ترامپ تصمیم خودشو برای حمله گرفته؛
میانجی‌ها که آدم‌های خیلی خوشبینی‌ان و همیشه میگن راه مذاکره بازه، حتی اونا هم میگن حمله‌ی آمریکا از هر وقت دیگه‌ای نزدیکتره.
آمریکا هم از طریق سفارت خونه‌هاش به مردمش تو خاورمیانه هشدارهایی داده که اینم یه نشونه بزرگه برای حمله مگه اینکه ایران همه رو سوپرایز کنه و برگرده به مذاکره.
@News_Hut</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/news_hut/69391" target="_blank">📅 22:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69390">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⏺
🇮🇷
نیروی هوایی جمهوری اسلامی هم از دیروز تا الان مشغول آماده‌سازی خودشه تا در صورت نیاز، بعضی از اهداف تو خاورمیانه رو هدف قرار بده:
@News_Hut</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/69390" target="_blank">📅 22:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69389">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSiAQ6CGDKeJ7sAbc7YH8RP0lZzkIqhj0w7mvKaodNx8bFibeymf15UErar9CzQ7BrnBjHKGhGe8qW4OK_1L3s6XxhhSOaPXV5FBT-ENs-8qCbpjm6P9Uzq_Rrsu3nzSmbwMvEXqWZ7yw41lpinHIfuQF59cxJnmNt0xQ2NCo8X9bCapcE8nz_QKxPMmIfE_ExfrYPjqS0JnjmhdIBMWXk5g30sRdGzunbIS_KZGcXqEn6ttpy_vbluF0ULvqvqVYpLBNEW8yrLyc42o5uO2ne34hIA5OV5dsmcxUakjL_NwphsvFRm-UTrmV9Ns0WIhC52JRPmBw4SiW3mIzYEbKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
ترامپ در حال نابود کردن ارزش پول ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/69389" target="_blank">📅 21:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69388">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/If_zITn_HFEFg7aQERH-IikQhWNUMShcuWN0Zwh6e46BC4ohMqIE5KIezuu6MwZ8AFTXk33L0WpfWPn6LC-zcp-BUtU74VshWiPtif-AVRPe6oqee1fX1Mudf83EojWmdBmXJUGxWE8Nd3H4K_zku23ltFs0qFRDLLcXKvoeRhFetJNjMq0IrH8ZU_8IwSFXD2-IF-2rs209IPzso9XN0ZiWfxoO3zoNHa-76H5x4Ix-RRZG4eJ0ZyZfHZcahR0F6C1AoNqGlLdoS0UkukimeZQfjN4oJQIMSsVEnZkrrdvi2XJ-VnyHQ3OKZhFR_kIacrIRWjmwyvPh9rf44JklaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/69388" target="_blank">📅 21:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69384">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nK1ZtrBKcepGlpb4k5AhuQGz__IARCx66Aw2Mis5cYPLP6dQ8vpnN8YD8VOAIwNA4McR2PutGK67WL2DuRapasB9-Moijbq757V7iIZfziZnLRyRFGDtKWtq30HUKL1TymLB_zK0LK4ZrfXTsb6T5QqDGbAxt8JVNT4KSIVrrbpFzKG_-Rh8iq1_T37FapmoZ7iTecyGEJapmHAv3iPCw7NlX5lKCcK6TDKfH26JFFW0qWU-nucSTBs6VQeq-xqlDLfdL7xztm8Nquh8TEthc2wf5bSYb975BgvHknS6NcwB12UfEgLpGhnOLbFcVrz5Wio2yqWuImdmO0gr8TjhIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZLowYS8Dy_lFVa7OJPnonCOdVscnE6GmdnqqSnu2z6zr9ab1YuGqkOQvlrlvrHK_0_B828Eix4yiy9SgOdN7thJeGufJRE4weGgYjxMz-yFlMJ4pQ3JbU6kjhkgMzIL9anOKr64pNbIqNXU6BZVOivPvbieUyAvWFTfhNfGbVxRqG-RfOSTYYOZWxwtthLYNnytWSbPwoV9MVRBxfYV4ctr4NaL4aSG6jfEauBh5OkBnEoHlRZNeZIdbqH5Mon-8ebCmE8Gq6-f4Q4WutYtjEkMkZK8jpPq5BhWoPaGJIFIHIjNUlOqGlt2Kph5Ioyjxh9zS-zDQYOM2bMWwf9nenQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eIsUxauwxjb5GRnKCi29oWqmFwPxvjFSJ04vrDQfW-vfuW-PefbJX6Sv7J1-rgW2Zy80ewi0qWeJc1IgdZ6AsaCCSxBJZzsCbcZERlQEU5oj0rPpLrzoJQFuPIy1_ZjFVxQzDhcFnUQXUlldjzaJcMzcWtLpVsPHSHY-DC7Qszsag8QpyT18ZHqp7izXZSWuNzWBREuEJV2SadLKvxWYuuwsMpS2OtXpg2b3xJeiZKjE0zIyCRjjQ6vxKSuKEWwOcSqixWuSKC2t_AZ7Zv1bSVBheKHOG8Kq7OA8GCJ74tP0tsI7bFxIDP0tiR-zbplTxTj5tYmhYNaH6AARFLhyWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/etSkw6rx7uoYLHmdlavot2LCuc5YVQ7R-csTrkPqjsz0UQLOXymyrjdC3UV0DHFSR9ZhbroddYfew8EEbi-OYqRql3mHvIRuoZXd1DggYghLu6dQLuJw1balmhFKbtXr41QL_9SquRJotC5m3FCgI8lb5IEH3XP-MqHMZxc6250G_pRTx-nqRsSp4pVlPlGSkHEPpXRsyLDhgAZy5gB_DJTOsTVYNhDHsxRR7KTNZxZkFktbxGHWyrN-aLudXazJL5omRZHzNAakOyPXOvImYrjoxu6PuZwCperzADitdKcP6EibgsjhCzoMq7abg7tiaDOlFxocpmkj_cUGT6FdqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
پست های جدید ترامپ
از تصاحب گرینلند تا جنگنده و انهدام ۱۵۹ شناور جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/69384" target="_blank">📅 21:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69383">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fy5upc1AsNRNZzS_9Y9JpkoHJeh2ICzIP7snxVpMr-AxW2xW4z_rhNJ50fMTqa9601_Dwy3GPkDnyn3B6KpKYeQOVQtg1tHLiCdvkeJW5pLtyTSL_0qKfy1AcSVwLVLXsByie0AbAsQooIXLCYfIXm8lxVDJST-To7A4OGCyKoxKXMeW42TzHjdwgerHXjIM-Y8bF9WY3uAT5akuxosAlLiGBk1ZBBqR_jLVHFlKucVGGbVcm1sJTIUlg6Bsqo_9QWxaBOq-xN3Sn9Jr56lkxLN7wHsKTjR0ro42TeR5BRMJurK65rM4bNYRKv1BVV65C_HtqlYb6t5D-6FN4CriNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/69383" target="_blank">📅 21:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69382">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY5GIDSZICP4fak8vzDO10wDCmF7yt_F79_MNbDJRAKG36I1W7d5aRAo5dLvoE7Kyht8wsorAqlExDp0WC3Wy6YGbMwyEujqx-eP-uaB_f0RA0SljrUkKv_MCbanvMZT51HEMQU16vVjKmGPAEJKmMsslKvO89P1KqUmohCZqz0sV-BB60UZJwNp4bvJ8_fiqAxnmwZj8fisbkzGJrDYTLhiju_m3JEskteMCBeRxV6UTSznZvbPqlPJmRz3oaRBKGTyO-iL5x_Om3AfsdGL6ha7pOma7UkuV4b8qZZg5FyO6NDSaPU1vgTYMxA5bJeAu3hV9dKFKAbI_7K6ePg5dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی:
بر اساس اظهارات رژیم ترامپ، کاملاً محتمل به نظر می‌رسد که پس از ماه‌ها تهدیدهای وحشیانه، امشب آخرین شبِ وضعیت عادی در قطر، عربستان سعودی، کویت، بحرین، امارات و احتمالاً عمان باشد.
اگر حملاتی علیه زیرساخت‌های غیرنظامی ایران صورت گیرد، زیرساخت‌های حیاتی این رژیم‌های همدست — به همراه زیرساخت‌های رژیم صهیونیستی و شاید اردن — ویران خواهد شد.
مردم ساکن در قلمرو این رژیم‌ها باید فوراً برای تخلیه آماده شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/69382" target="_blank">📅 21:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69381">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
کانال ۱۲ اسرائیل:
این کشور در بالاترین سطح آماده‌باش قرار گرفته و مقامات ارشد سیاسی و امنیتی در طول تعطیلات آخر هفته مشغول رایزنی بوده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69381" target="_blank">📅 20:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69380">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdzISgW_DQ3grHlSBblO5PllpUiBXDHTqoEjLmChUz-fROfsiImIChLqjsH_wkdyrcocTFG-atl5d9CTN01w669sz-g8PSggrddTUak-oWhUCos9G-dQtoWU_hDgzp8LtFsOxRI-O10RM4SEp8an6Xo_MdTBHTXOnps9My8Q1VnIxverBfc5sIu6y9F20yhBJa9RvgMf-uAW-YXfXHrcHDxkpnKG70lxfLrjX9PboPQLrv4lrOpRwkWH-3Px9MpXbGGnUg8y7QPjHL6Jb4j9rRFqWOT2fsmB3WmKDBg4EGBrp1d-wQTs9AUlbSNIPe0iOmekwE7k1yhA8KKqBD9o8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
🇮🇱
کانال 12 اسرائیل:یک مقام اسرائیلی؛
«تنش‌ها به بالاترین حد خود رسیده است؛ ترامپ بیش از هر زمان دیگری به انجام حمله‌ای بزرگ علیه ایران نزدیک است.»
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/69380" target="_blank">📅 20:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69378">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/799177ea92.mp4?token=j_xmXrkFi5GZEnlPwc5jbldY-jc2kR4ZqWLnWYFaFdUJUheK1wgkaLVXFX3zX5N3VW8YIho45bSu7IhXOmUhAq0yLsU86lGZUC19hdVtkNlZqAgzCNUZHWtx83zjfFNwFChsKVwhjVwpoWC_lv0722gE4k1b3a4wCkM_Llgug3kUfWxXuT7KtDKbcX-PELaxpk8TDov1jyuteE_BoOwhfgOj_T0BMYQUMm36vxXFvgzN194WCEyLEHdDhEJ3U7ortqgYVUI6noowb3alvm6FfjkcCoBMxL0S0cYC4pL724k16Jt31SGqoDnPiLWzppsqbKCQX0ogpvv46ZTZN7H1AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/799177ea92.mp4?token=j_xmXrkFi5GZEnlPwc5jbldY-jc2kR4ZqWLnWYFaFdUJUheK1wgkaLVXFX3zX5N3VW8YIho45bSu7IhXOmUhAq0yLsU86lGZUC19hdVtkNlZqAgzCNUZHWtx83zjfFNwFChsKVwhjVwpoWC_lv0722gE4k1b3a4wCkM_Llgug3kUfWxXuT7KtDKbcX-PELaxpk8TDov1jyuteE_BoOwhfgOj_T0BMYQUMm36vxXFvgzN194WCEyLEHdDhEJ3U7ortqgYVUI6noowb3alvm6FfjkcCoBMxL0S0cYC4pL724k16Jt31SGqoDnPiLWzppsqbKCQX0ogpvv46ZTZN7H1AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تخلیه پایگاه های هوایی آمریکا در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/69378" target="_blank">📅 20:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69377">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/483837b794.mp4?token=X67rlmMPli_ozQhPRgTAVC1iIzkctWg3SFVdFSOHF2YckrGksDG9cvqFL9OdvDO8nDWs3waZg6l4dLzZHhO44oLNyxumVa6abEvHQsBtF4nqtxqF4z2NsId2vgpvUqoGerg8PSJPfHe5fbQB2Go8On6408XGAe0klN7COklQd3J0btumVSstSfdwRl_OintWXNG2ID31fa71R1m2tlnGMKBCPG4zqqmt0bihNuvf6olNjmFtJHnIR3UW1ZEkWod7j0xIMZZQu3l85URcXAseExrPICaIXupXy1v8oAhZlnsL5FsgvouQzM3Jq2zb1lUIMJznr7c2sFkJ8iTvwkOXDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/483837b794.mp4?token=X67rlmMPli_ozQhPRgTAVC1iIzkctWg3SFVdFSOHF2YckrGksDG9cvqFL9OdvDO8nDWs3waZg6l4dLzZHhO44oLNyxumVa6abEvHQsBtF4nqtxqF4z2NsId2vgpvUqoGerg8PSJPfHe5fbQB2Go8On6408XGAe0klN7COklQd3J0btumVSstSfdwRl_OintWXNG2ID31fa71R1m2tlnGMKBCPG4zqqmt0bihNuvf6olNjmFtJHnIR3UW1ZEkWod7j0xIMZZQu3l85URcXAseExrPICaIXupXy1v8oAhZlnsL5FsgvouQzM3Jq2zb1lUIMJznr7c2sFkJ8iTvwkOXDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کاخ سفید:خداوند سربازان مارا حفظ کند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69377" target="_blank">📅 19:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69376">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c746862829.mp4?token=iTeCBWSQWuq5teiQ0c_d8f1M2k9KJN9WivW0d6YvkTy0nFZBvNneZJP4EbSMlG0X0VRDOwhHCJJhZi8Tv4iEqSq_l7kMSEaQm8AXh8w6BjvrPFwUsYpygIkVDi9V2UiqnyAoXpdbjH2_oxaSjPUNyPn6XToQXN35nlwSNz6mUxNBCnfvm_8S8H1hIpkbPVWLkCQ-E-QNS-re34cR4Y0-m227i7q43akUA80O2zKJftp_CyCIk2-5T9iMFqLpjSi1u-zee2hHr6iGaAR6f6-6RVb8YplMoHFyTTfGyTSA3NIqM5qqpqmW9EjkeiUmKh1KXdgufW5iCAxD6-J-8upErDJ5rUClbYP5XLMm78YqgVNgANZDfGhlChPCRauLbYDe-hBUA5uPd7PUHFnWAL2sMB3UIqbzZelvuYM5aoJBfKQP6jcwcPGouuPP-M_aZ8lSvnTSfQ-6Jn97oShG7cqWlvOGXGT6nJVCFhiXU51s48axYsvHv1zGt0jVdyEbahr5roFXwMAvcldXYSsyGOS7e19CsM-49czv0ZIYie2jJ8tKd82YWWTJI2q2tQTLYSbD9YI4QHLVSMCuP9-p835SW_bjCAKhiq8unMwAabC4TDtGeLJeKbRKbNxc0VHaAjBsu3ZNZQJd6pNrOSsYKoLBH5w-fM51Z8N4qTfMXSFe2TY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c746862829.mp4?token=iTeCBWSQWuq5teiQ0c_d8f1M2k9KJN9WivW0d6YvkTy0nFZBvNneZJP4EbSMlG0X0VRDOwhHCJJhZi8Tv4iEqSq_l7kMSEaQm8AXh8w6BjvrPFwUsYpygIkVDi9V2UiqnyAoXpdbjH2_oxaSjPUNyPn6XToQXN35nlwSNz6mUxNBCnfvm_8S8H1hIpkbPVWLkCQ-E-QNS-re34cR4Y0-m227i7q43akUA80O2zKJftp_CyCIk2-5T9iMFqLpjSi1u-zee2hHr6iGaAR6f6-6RVb8YplMoHFyTTfGyTSA3NIqM5qqpqmW9EjkeiUmKh1KXdgufW5iCAxD6-J-8upErDJ5rUClbYP5XLMm78YqgVNgANZDfGhlChPCRauLbYDe-hBUA5uPd7PUHFnWAL2sMB3UIqbzZelvuYM5aoJBfKQP6jcwcPGouuPP-M_aZ8lSvnTSfQ-6Jn97oShG7cqWlvOGXGT6nJVCFhiXU51s48axYsvHv1zGt0jVdyEbahr5roFXwMAvcldXYSsyGOS7e19CsM-49czv0ZIYie2jJ8tKd82YWWTJI2q2tQTLYSbD9YI4QHLVSMCuP9-p835SW_bjCAKhiq8unMwAabC4TDtGeLJeKbRKbNxc0VHaAjBsu3ZNZQJd6pNrOSsYKoLBH5w-fM51Z8N4qTfMXSFe2TY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیستون؛
جایی که سنگ،
به زبان تاریخ سخن می‌گوید.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/69376" target="_blank">📅 19:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69375">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b275487f.mp4?token=fIg0oGG8O1hmuEeVXv_Fk9WGGUw0VJ7_9UQWZQpNt6PwzcGj6jBGGlu7lwFvWc0iP43uaT3DUVxx3gPOvgD1rt_gbdWb_sKznB7apGvWkJPm4Kd1Uzdp4gq-b_1sAxLq-tMlLSwVZ069GVr3pAnxTO96A9gA3xw9RAR0BngYKdiDgXJ8ZJgOYoZQ6P2KXL7jWKiokePQqwnuKszmDjb376ktJkz8WT3ar9mpTqssu73ynPcJY-IEfHo4slR8IEQ1dXiCGV568b45jtAw7qLK29AxaD625D188f92-hotAlVhHocRtNPW1M_MrXjk4uroZvmFxcpVUxLrFi3cJTWArw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b275487f.mp4?token=fIg0oGG8O1hmuEeVXv_Fk9WGGUw0VJ7_9UQWZQpNt6PwzcGj6jBGGlu7lwFvWc0iP43uaT3DUVxx3gPOvgD1rt_gbdWb_sKznB7apGvWkJPm4Kd1Uzdp4gq-b_1sAxLq-tMlLSwVZ069GVr3pAnxTO96A9gA3xw9RAR0BngYKdiDgXJ8ZJgOYoZQ6P2KXL7jWKiokePQqwnuKszmDjb376ktJkz8WT3ar9mpTqssu73ynPcJY-IEfHo4slR8IEQ1dXiCGV568b45jtAw7qLK29AxaD625D188f92-hotAlVhHocRtNPW1M_MrXjk4uroZvmFxcpVUxLrFi3cJTWArw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇷🇺
دونالد ترامپ، رئیس‌جمهور آمریکا، و ولادیمیر پوتین، رئیس‌جمهور روسیه، در قالب «زوج در حال بوسه» در رژه کانال‌های آمستردام:
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/69375" target="_blank">📅 18:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69374">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4517b5c3.mp4?token=Dt9Xulmeax9sQphTYLS5QgQ55BACQ043-4WAlGtuHcNBLwlmJfHWE8VbpRgB9VN1zSOR8DT9QJRvLvngZcccZN0vtW37qTNhjZg3nZBn5wA7IAUpwdDds94eeEQcmNwPu7_eMTTA7dkVPaTsXm4yYAM6G0MofxkQXeF3LT6t3Lzrd13GNL44nLXsu_8uCr92sl6ObWr2BMk-iQ7NN1EvofVscI5lMwA7Lq3cvqB3ul2maX5EXgoHwQSxPBv9wfQCosN27ovyIz39i82GxvWe6xz4Z0DRoGL2baLg2IFKO3WV4mskBnhWWc2hEtnBu3zna3Ku9C3mDieCqBTLEY1clw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4517b5c3.mp4?token=Dt9Xulmeax9sQphTYLS5QgQ55BACQ043-4WAlGtuHcNBLwlmJfHWE8VbpRgB9VN1zSOR8DT9QJRvLvngZcccZN0vtW37qTNhjZg3nZBn5wA7IAUpwdDds94eeEQcmNwPu7_eMTTA7dkVPaTsXm4yYAM6G0MofxkQXeF3LT6t3Lzrd13GNL44nLXsu_8uCr92sl6ObWr2BMk-iQ7NN1EvofVscI5lMwA7Lq3cvqB3ul2maX5EXgoHwQSxPBv9wfQCosN27ovyIz39i82GxvWe6xz4Z0DRoGL2baLg2IFKO3WV4mskBnhWWc2hEtnBu3zna3Ku9C3mDieCqBTLEY1clw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
فاکس نیوز:
رئیس‌جمهور ترامپ در حال تشدید فشارها بر ایران است و می‌گوید در صورتی که مذاکرات دیپلماتیک به نتیجه نرسد، انجام حملات نظامی جدید همچنان یکی از گزینه‌های روی میز است.
ترامپ پس از دیدار با اعضای کابینه خود در «کمپ دیوید» اظهار داشت که توان نظامی ایران به‌طور قابل‌توجهی تضعیف شده، اما این کشور همچنان از برخی قابلیت‌های موشکی برخوردار است.
مقامات آمریکایی می‌گویند این حملات ممکن است حتی در همین آخر هفته انجام شود؛ در مقابل، ایران اعلام کرده است که در صورت هدف قرار گرفتن زیرساخت‌های حیاتی‌اش توسط آمریکا یا اسرائیل، آماده پاسخگویی است.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/69374" target="_blank">📅 18:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69373">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f0734246c.mp4?token=fzG-tjBAYBPTW0z6LjVc1nq9pZJNi4-R4cH6Fzb1qamiJC-tsbfiNCjLzs6pMpde7z_25Wnc6tFeMNKSfbso98vC--YcluXJ1rWTLHiutQEBbDGRQiy0_M7J7ckX0JQWibg43IpRDclAMb9TqRdGcw4Pebjd8Nw1rjCX_3uDG2cNCEqemp07oBpCWK5_owm7jKEYfOADZF4FSmOkeckGQSwaer6eFKREv2sOWWURnKbEfJoCw9foj1rrDO7_4WyQaSDJTiKOoAPp4JI9gzFv35sIUqRfE6x0q0vz3PYYEfun93BRc57lXLT1wMRV9rjKTdJpg-eFrhxLtd6S7n6XCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f0734246c.mp4?token=fzG-tjBAYBPTW0z6LjVc1nq9pZJNi4-R4cH6Fzb1qamiJC-tsbfiNCjLzs6pMpde7z_25Wnc6tFeMNKSfbso98vC--YcluXJ1rWTLHiutQEBbDGRQiy0_M7J7ckX0JQWibg43IpRDclAMb9TqRdGcw4Pebjd8Nw1rjCX_3uDG2cNCEqemp07oBpCWK5_owm7jKEYfOADZF4FSmOkeckGQSwaer6eFKREv2sOWWURnKbEfJoCw9foj1rrDO7_4WyQaSDJTiKOoAPp4JI9gzFv35sIUqRfE6x0q0vz3PYYEfun93BRc57lXLT1wMRV9rjKTdJpg-eFrhxLtd6S7n6XCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک هواپیمای سبک قاچاقچیان کلمبیایی در حال فرار از رهگیری توسط جت جنگنده ونزوئلایی.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/69373" target="_blank">📅 18:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69372">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f45020b76.mp4?token=kPe2cZM_XdDLR8rH_7ue_d1umWLDa4dFl6jyCVl63aTBfg4C5ub7uedRyIeSEjVSmVUir-4685yHzsALI4mblG0snAZz0b6cykIt6tualSQwsdCmn76hVc2nrPIBaZmXYYiz-xsIoxIscGLU61zPZbYIx6IkZmVlGdJo2EwQ5dF_qze4P8VfCyTytXQNYB-o5BjA-zCkWy1Wbw_dnkWQEpfHF7783NZhvLC0MaOEXKa4JgO9y6dFX3IcYFJF_jOYYBgU-2_Xy_53vrYOGrIEwQDREV6XdzKxC5S1y46I3yUvayOjyGov-_Xs8rZYhj9BFB8lFj4mhCSjzCTymp1v9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f45020b76.mp4?token=kPe2cZM_XdDLR8rH_7ue_d1umWLDa4dFl6jyCVl63aTBfg4C5ub7uedRyIeSEjVSmVUir-4685yHzsALI4mblG0snAZz0b6cykIt6tualSQwsdCmn76hVc2nrPIBaZmXYYiz-xsIoxIscGLU61zPZbYIx6IkZmVlGdJo2EwQ5dF_qze4P8VfCyTytXQNYB-o5BjA-zCkWy1Wbw_dnkWQEpfHF7783NZhvLC0MaOEXKa4JgO9y6dFX3IcYFJF_jOYYBgU-2_Xy_53vrYOGrIEwQDREV6XdzKxC5S1y46I3yUvayOjyGov-_Xs8rZYhj9BFB8lFj4mhCSjzCTymp1v9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز صبح تو یکی از حوزه‌های امتحانات نهاییِ اردبيل، 9 تا از بچه‌ها مونده بودن پشت در و داشتن گریه می‌کردن؛
طبق ادعای خودِ دانش‌آموزا، مسئول حوزه ساعت 07:03 در ورودی رو بسته!
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/69372" target="_blank">📅 17:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69371">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
ویدیو وایرال شده از این هموطنمون که در زمان شاه حضور داشته :
زمان شاه به دانشجو هایی که میومدن اینجا درس بخونن ماهی 400 دلار حقوق میداد
اون زمان صدتا نارنگی یک دلار بود
یه اپارتمان سه خوابه تو نیویورک میگرفتیم با سه تا توالت و حمام اجاره اش 210 دلار بود ما ماهی 400 دلار اونوقت حقوق میگرفتیم از شاه
شورلت کامارو یکی از ماشین های اسطوره ای امریکا بود سه هزار و صد دلار
با یک سال تونستم ماشینو بخورم
امریکایی ها میگفتن کجایی هستی میگفتم ایرانی همشون میگفتن شاه شاه شاه
کدوم شاه شما دیدید بیاد تو امریکا براش با کلی عزت مراسم بگیرن که برای شاه ما گرفتن
چه افتخار و عزتی و لوکی بود شاه واقعا نوع بیانش و لباس پوشیدنش هرچیزی نگاه میکردی لذت میبردی
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/69371" target="_blank">📅 16:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69370">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruZKIw2KgoVP5l-82Mp4lKiKU2w83o1DRQQsJoPjPmmyfueHoCNwQJ5vuRQOrUSER8IpLSlAhysYETiwm8XwfuNnKOo82GTB-IBgmlKUR7SSb51YomrXjjNyk4G9TkqdrR56ivD5lI3PrF6e64J5DEljwUuvMAKEEwAA4ELKuhp0sQ7OTMn9VWYqWxx18FDd4TOm0Lm1_CyaE_MLqmk5IoszVuFQ7xg9g96OLKc0AJtxrseCQugnYH58QXcQOkuX4DW_73pu3OCelx6RiWqs-wYi2n3m51Fl3Np5a1OW7UqOy_fFmruBI6T1rOD14lCgBXDVvBE8fzCnzmJZS7jo3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سفارت آمریکا در مصر هم برای شهروندان آمریکایی هشدار صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69370" target="_blank">📅 16:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69369">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46327b1ae3.mp4?token=cDvI1N7HT_WB_ecYSIuDBWJJfDcXUN2kWVE12jGZA7d5QzmGV8nCMYrUwWjm5jRCDYcaywRHg2dUEGcz5CLPRIab0bPyTZasYRnwCuL1n0fOVimh5ywPgAMgsaHetG5_iUG8R7xFdxRzUHNQOjQVH9UlKWBStL1SDOaXXS0_WLfe9jk2aSx1B3ZCM1Nh6-_Dnsqsn7hswT2uFvkDH2Hsn88bPTcWdz7NpOrqkf6eXesWrRWISfPd9qXKpWsM_RxdfEvFXFWfhLh1j8DRmRYGpSmmCHJFuxPax_LupAMIkPQTA5gVNIWliqnxJKKRd9bO5Edn3FH5KBBBkFsK1-OWLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46327b1ae3.mp4?token=cDvI1N7HT_WB_ecYSIuDBWJJfDcXUN2kWVE12jGZA7d5QzmGV8nCMYrUwWjm5jRCDYcaywRHg2dUEGcz5CLPRIab0bPyTZasYRnwCuL1n0fOVimh5ywPgAMgsaHetG5_iUG8R7xFdxRzUHNQOjQVH9UlKWBStL1SDOaXXS0_WLfe9jk2aSx1B3ZCM1Nh6-_Dnsqsn7hswT2uFvkDH2Hsn88bPTcWdz7NpOrqkf6eXesWrRWISfPd9qXKpWsM_RxdfEvFXFWfhLh1j8DRmRYGpSmmCHJFuxPax_LupAMIkPQTA5gVNIWliqnxJKKRd9bO5Edn3FH5KBBBkFsK1-OWLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پیرزن ایرانی توی مراسم اربعین، برای اینکه از یه زن عراقی صندلی‌شو بگیره، بهش حمله‌ور شد
😔
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69369" target="_blank">📅 16:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69368">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حالا ما کجا بریم
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69368" target="_blank">📅 15:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69363">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuO56KdtRZDvWXnyErftpW8w72QmffyT2lGjwxPkxEyITK_cF-sPV0aVKEeF5Nn3zMp8tMf6kyM1kpiVx-G6bO5vr3N_uGih74WFH0eqO2RXw2Pn_orjIoeraJtgborT74iXyrwfo6y5oEjjoSL8MEdy8ytUmvgn_9HBrBoXhdJtPO-0lMNw9-jtlqA1AbIOjjVGSsNRCMZltM9F9bQBhQgzRgtvrNX7s2abOR-3im007PBa0B9k5y9m3IUlXoJFxR6MQ-dXq9UGwUmui3z5INCmuaXZF-7QgkvrY9sngraz4qxpZFUmcsrLkrL2oCBy9UpjlftYIHzuPQ_fSWS4uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pHbEGmf0LgSsy4zNG95f9nO7S1-dwBIj5cGodZa4JxH5ksu0ILi-5HmK2bL8ULhyqAiEdc3-q_sPk-mb7yfr3isac3GD6tUE2cWjf9C8kITfoEHTpXMuNSKGXm9yT9YMquB8wALKcvqp2AcdQClYBBYh9C_Fz6bvEbN697G-NhXs0Ct0orS-NPCLqXlY7S6zNHd_9RtPdnoQshzhGr9Sqk1TlfZIbQJzXYdvTPA-A3zs7MI25BXxXQQ_iw276KtOeNKaVI6Xi4jdmz8m-TzSWjSsbVZw5XqYory61cpNTA7neH4QnEQJekSYirwVaDAGxzp9ql7lCqfSBHQ5d_jQnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PJ-rozrL8XxYcR9XxOmT8mbGrVLDtA4WlBNRkpT97dlzlbGyQbOBtNw5lQx5N4rjxkqkRZgW4a2-brO0G4Y897S9o66TEO4ThuSlXon7CMIs0apa4K1s-BDc6BygtIw49bvbsQafQmp4fJl7QmYTRJyx24ic93jz2_y-KiAKsqG63yR9xNvl8tIp1AVb3bGG7bs8ExrK7OfNOvB26UK4rg4Y9SmbORsLoIeJk9cCG0P_SfjhEQ8qAeZTcgCytePEv8HodBVqioQrFwImbV0py0XU1b4qywdZo0QEqZzZ5sTbL_FPYsovJwQdtItNZMY0ZM-SudSorwAGGnzC2cvkrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LwWzyxOxIqkPVJdICQFNL0uQfnA2j8dpIgKpeR6xBqyKWALWtdrRQKJT7jcMYQP0eWK510rir3Mo37xP2I4cTALqkjPx0AsoOqUasnGNm_lke1uDQ46J9zmk5ou_wTRo5iaW2pNdgh18DLi7SCL78Cx3lACt8ZbDHgCJV5y7_Pf079bWKEhSvxYD4fQ9CaAU3wc_2ocLNQDtKaAFW1Y4w8q7HlYA6RWAEc1ItHzEYEVMEvftJi8X_otYCySPIK7heC0TkhD9tvxmpjuErT0CM7bYc7WsG-6mKgkdYyyH60KV8rNRuVH2-Yk2rqDUROTN5U41pVoZO3phGhAXztoa1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gLPwhbQQy_7ImzVc-VJhI_HYqqQooWfCpO553s-tXpwrW0UhDeYvOB5dA93JRLvdXD8OgXZ68qSZcLf1qBAp5A-T5NOLuNAvjdHmQTpZUHJK8620KSW11YjgFHOJW2O64sMkeIhZNJg_Vf22k_BBhkMPy4cdVhNYQJc-GDx3J9UOIwCm7qEokBXYeRFbi2mc0PbQ_Af7goYmMWOW_sFxWpJysNvB0hwrc-GhJSAVUnpnOPLeYJZ9O9BUjrojCIo6rZOSVhJxA3QOWgJQoRw6fWH6PtwSl7C4bv1Owhp45FOkg0NBIYGVwBOAkwfy1TMi8I4v5IJTGrRxaTmSm1o0EA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
سفارتخانه‌های آمریکا در خاورمیانه یکی پس از دیگری درحال صدور هشدار به شهروندان خود هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69363" target="_blank">📅 15:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69362">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be758c5d3.mp4?token=FyEE7rF-LCjqXsAQVJ5_Ar9Gs80Gxnbj_e0haHbBXKIL0WOmngYtYzpS9spPK1NZKQRdswaDmsBvoEytvgvC4sGrHQYLt2r2pX7XRInwr8ZXsjTnQKKVdCncTWuKSRIPkTLmmb6SOtkEMpv9fbend6ioSsmhUZXLlEVVQ2t1K4yjMDrz-vXmMmoP47nE4-XBmnpTjaD2Js21X397Skc5FNGQymYFtFWJkqdf1CyxQ6RZxtWNLGm3kZyw6GFg4SzFzKn39E-d9ehAA8ecnQc3hxvoy-f6JO7J_c7OKsbazbFWI67rei_aXFcv3ZZ8KIcFxsJzNpa0cWrv0qV6UOlHzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be758c5d3.mp4?token=FyEE7rF-LCjqXsAQVJ5_Ar9Gs80Gxnbj_e0haHbBXKIL0WOmngYtYzpS9spPK1NZKQRdswaDmsBvoEytvgvC4sGrHQYLt2r2pX7XRInwr8ZXsjTnQKKVdCncTWuKSRIPkTLmmb6SOtkEMpv9fbend6ioSsmhUZXLlEVVQ2t1K4yjMDrz-vXmMmoP47nE4-XBmnpTjaD2Js21X397Skc5FNGQymYFtFWJkqdf1CyxQ6RZxtWNLGm3kZyw6GFg4SzFzKn39E-d9ehAA8ecnQc3hxvoy-f6JO7J_c7OKsbazbFWI67rei_aXFcv3ZZ8KIcFxsJzNpa0cWrv0qV6UOlHzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده‌یاد مانوک خدابخشیان: دو شعاری که کار این رژیم را تمام کرد؛
رضاشاه، روحت شاد.
اصلاح طلب اصولگرا دیگه تمومه ماجرا.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69362" target="_blank">📅 15:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69360">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e4EG7RPSJMNX_IFbktsk6sSUXyLHf_5ggoiA-_gMMlwwQ6i4ks5PlrO7EN2q8tJNttqdO-sF6Yxy08sIZC_nypYm95FdPcz6xkzf0LuG2caQsIVWebSD1aYuFCriZclBGTRQQM3ZbW9sB-kQm6wpRmQVjTXtBhXaLUZJD-IKTgbz5Orbrh_Pn-QSYkioZBOiiZKv6BHg-U2M_0VGYQ_P1f8ENJJNGACvb-GCcDQd6zE5kvppJGrAdaiqVUMoZYysfFiA0zvPqLKvIm-yKDRhAO5sZB5aT37DMHsVvPq-eDH1bZasKDCwKKCWX92vr0f31XXibc2e1BDK3NNa-KBTMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qnM03LUwRAY-BLPEJjJSKJMDEu9Jtc5VzrVWPqH18WkSKVicZAYYQz8eynNCumdi0NOCt0fJqPPYCyhNRPezSpxufYGK1t2yAGJ78PPhCzmbeGUI9lGk31YHox8uVMoD9M5tgZqHUeOZARiepCY8Q1dl7z_JygSPPqGT0SkBSFj7wp8Ox5ThltDaU4SYOaf6YGhqJtl53FOkfnAhy3o2kFmnT6dSOQZBfvmMLWfIJ6ZrHNV7Vmsn7whN_XoNf94zlbapdpgmE0tEb1GhLBoEeQHa-yosar-RdvL8AYTE92AdeTw7zITtSCP6xGuy6EIpvEHTPkJYguFaqKZql0mxAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
سفارت آمریکا در اسرائیل و عراق:
آمریکایی‌های حاضر در منطقه باید آماده باشند و در صورت تشدید تنش، خروج از منطقه را در نظر بگیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69360" target="_blank">📅 14:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69359">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyInBpdcKjCl9qVxlNssNuTFCb06Besjapo9uWDL_CS2V_0Dhgg3CVD_407rAhv3c4ZSjMmlwY4nFvyJuT5qYLO0uto2lwggVTK4T6izP9d_jXeAcTqhwex8lYp1TLDdYvhrEczKsSv_cabkKkaqZGXiIS_0RDrEZqhVJt0_fXciZB683OzvnRTwNGKGA6cp7wk-JkqZ38pp8FntH5kS1xyuZH-jM8_eT_L4RR51K5G4RVAdo7eY7WBvOaDLg7EY4QpPzwOZo_kEFKUc01Oab_cf7fWWLqMpkLaPXi3pQbIDwP4vEJY9wT4ZKxEO0Z4DBM21ksR8aA_Vubywspf3lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تسنیم:  بهمون حمله نشده، گلوله توپ زمان دفاع مقدس ۸ ساله منفجر شد.  @News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69359" target="_blank">📅 14:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69358">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
تسنیم:
بهمون حمله نشده، گلوله توپ زمان دفاع مقدس ۸ ساله منفجر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/69358" target="_blank">📅 14:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69357">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
دقایقی پیش از حوالی اسلام‌آباد غرب کرمانشاه، صدای چند انفجار شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69357" target="_blank">📅 14:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69356">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c794c22fb.mp4?token=tAs_50e8WDda7UyHm-q4cOP7qYNuUhxl1PvmbVa4tg5ue-AQ2yovabOxdmN_EQ9C1KW4Omy27FwNuE4SD413WDQDkiuiubazirYh4JQUgELb2Jox-xSggixq_ayoi5EWeR3fb6rHw_jzgMgUiAHbpEB32dATqBGFKFC6gGzbd5UI8USylZoK256-Ys98LNYyOY9XXU8DJg0ohHiPFvWQcQED9zPeVTqmhpglShA3MQBzmbhn_Mswx7qdZj6dpHiGoy4YiLmnfNmfmYNrBSW1i680qHDUh6sHRdpgmw5naOC00Xr38_I51fR2IyZrZTc-J_7oLHl9eCcLTv9PjkYBBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c794c22fb.mp4?token=tAs_50e8WDda7UyHm-q4cOP7qYNuUhxl1PvmbVa4tg5ue-AQ2yovabOxdmN_EQ9C1KW4Omy27FwNuE4SD413WDQDkiuiubazirYh4JQUgELb2Jox-xSggixq_ayoi5EWeR3fb6rHw_jzgMgUiAHbpEB32dATqBGFKFC6gGzbd5UI8USylZoK256-Ys98LNYyOY9XXU8DJg0ohHiPFvWQcQED9zPeVTqmhpglShA3MQBzmbhn_Mswx7qdZj6dpHiGoy4YiLmnfNmfmYNrBSW1i680qHDUh6sHRdpgmw5naOC00Xr38_I51fR2IyZrZTc-J_7oLHl9eCcLTv9PjkYBBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه جوون عرب داشت به زائرا میگفت بیاید آب انگور بخورید که یه ایرانی رسید و بهش گفت:
آب‌انگور نه، بگوآب‌شنگول
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/69356" target="_blank">📅 13:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69355">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/917485436c.mp4?token=Pm3IVdrnOyl4qUfRCLl0ND0W7W5AnEp1bxgE10nY4IZQ7WZTOBP9zQwyHSlg6TbhkykhqS6ATRKlgSXOYTCRUC-wkFs3EdMG1770vlTNOCPZo9TmWqxi5s9LVkrBLjqDrI4IJ2SV5hGxn9_M6UtXTo1Dwb2h4RJDBy-RBARhdfU1oKpGXasfitQGi5pQJ-D5kRvmDk_OTgDFg9hLo3mTwJi04_yX6KTGDYCelEjTmy7DJaGpE6-F2N8GRSm0BeqS44POsxiwl3AQLjhC9vaVfQxj3zeqwzukU9JUwcgPXeVXqCxJKbMnuOMQY6YRtU_750oa37AQ-j2OYRH9QEGsmRVSvQ4UTp0cr8cgEI-IqmgpOOCSfWUXnE9E4pJADwvNmyhk37gXd_YdfSOtt0Yaceqomq9cgf8GavWn6eCWd1kvMSXdfODPvFmIi0SKSswqBhsRXd-fWUm185h15FB3f9aR7kx1FsxfJ7W0w4DIuwOHpc4p3ItqsJ0MYZ9Jk4buHTYyCu3ox3mPKKJ9QZYbBHa34uvvRHRuHIrt5JzSQ0YcPFtxnwPt0Wn6Gd4Di2gKjvabRxD9U9zSisPm4j3zkKDTx8kio1RPLxo0XoOBqdJ3Zw5FyqdqXK2QE6T_N_lCZ3b5ApBAzUzMqmXWUayYGO5HbayXmOn6p2Dx7GAJzMU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/917485436c.mp4?token=Pm3IVdrnOyl4qUfRCLl0ND0W7W5AnEp1bxgE10nY4IZQ7WZTOBP9zQwyHSlg6TbhkykhqS6ATRKlgSXOYTCRUC-wkFs3EdMG1770vlTNOCPZo9TmWqxi5s9LVkrBLjqDrI4IJ2SV5hGxn9_M6UtXTo1Dwb2h4RJDBy-RBARhdfU1oKpGXasfitQGi5pQJ-D5kRvmDk_OTgDFg9hLo3mTwJi04_yX6KTGDYCelEjTmy7DJaGpE6-F2N8GRSm0BeqS44POsxiwl3AQLjhC9vaVfQxj3zeqwzukU9JUwcgPXeVXqCxJKbMnuOMQY6YRtU_750oa37AQ-j2OYRH9QEGsmRVSvQ4UTp0cr8cgEI-IqmgpOOCSfWUXnE9E4pJADwvNmyhk37gXd_YdfSOtt0Yaceqomq9cgf8GavWn6eCWd1kvMSXdfODPvFmIi0SKSswqBhsRXd-fWUm185h15FB3f9aR7kx1FsxfJ7W0w4DIuwOHpc4p3ItqsJ0MYZ9Jk4buHTYyCu3ox3mPKKJ9QZYbBHa34uvvRHRuHIrt5JzSQ0YcPFtxnwPt0Wn6Gd4Di2gKjvabRxD9U9zSisPm4j3zkKDTx8kio1RPLxo0XoOBqdJ3Zw5FyqdqXK2QE6T_N_lCZ3b5ApBAzUzMqmXWUayYGO5HbayXmOn6p2Dx7GAJzMU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
آتش‌سوزی در یکی از پالایشگاه‌های استان اربیل در اقلیم کردستان عراق
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69355" target="_blank">📅 13:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69354">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/532a951287.mp4?token=q6q3MsjZITEoVG-HaH5sNUTBQ_0-yWCPj2LzVfVNgh_jljCEbmA8WCl4Watw2QVS4I8bieVHtl87ZRrFTryiOG_CEFz5Qu2MoPiyb2xhmoElCkIbn7HtVsBueNxbZN9PcC7135t2Mnv6tD9DPgySIBFE3vDvlCJ6Le9SYdpV7YDNb1fgwUaCz2Sc0qD-IIaKKwDRZkTJPr_-I4fOHX-YLUW7nfG7IDkTDJPJunD4Ek0a6igsX9-h58Wx7NhQKkdm_HYoDES5ZFTwqZiwcX5CywYMW-d0M3GXoOxyk4qrTmKwL06Y-zklmaVowi61oOm8D3feQuCevKky7XxDNTsxFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/532a951287.mp4?token=q6q3MsjZITEoVG-HaH5sNUTBQ_0-yWCPj2LzVfVNgh_jljCEbmA8WCl4Watw2QVS4I8bieVHtl87ZRrFTryiOG_CEFz5Qu2MoPiyb2xhmoElCkIbn7HtVsBueNxbZN9PcC7135t2Mnv6tD9DPgySIBFE3vDvlCJ6Le9SYdpV7YDNb1fgwUaCz2Sc0qD-IIaKKwDRZkTJPr_-I4fOHX-YLUW7nfG7IDkTDJPJunD4Ek0a6igsX9-h58Wx7NhQKkdm_HYoDES5ZFTwqZiwcX5CywYMW-d0M3GXoOxyk4qrTmKwL06Y-zklmaVowi61oOm8D3feQuCevKky7XxDNTsxFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه لیلی فیلیپس پورن استار معروف که تو 24 ساعت با 2 هزار نفر سکس کرده بود!
دوس پسر لیلی: من اصلا از این موضوع ناراحت نیستم، چون اون واقعا زحمت می‌کشه.
مهم اینه که آخر شبا میاد پیش من، و اینکه من بوسیدن رو براش ممنوع کردم، اگه با بقیه سکس کنه مشکلی نداره، ولی فقط باید منو بوس کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/69354" target="_blank">📅 13:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69353">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d26851041.mp4?token=cW7fzptSbyzHnyI-A86G8kFccfp-D_eWWOhU5E2m7F2zoty2F3qJPQioo022QkopM8f4-p0noS9SIeGRgBnT5ooTapowVAlkBZzDWtgBcRhc5ZMBDX4sy28G290ok5LdtaCrAxKpe1FOSuUzfalju_5XjsNum0lSGb6zQTetE245AjYyrFSbPSGhpJ2m8MAKiQ3iEW5BWvdMU6fsbX_7wmUnQC_FMw6CeB-WE2FJvQExmvOngo0qb98Vq0rnM5lRb9-Gn05rJ20-2JsGhK4jVOYOWX6fwmoW296yX0MvdGPyBqgOJZWOoMJSL30GgoYlWuaXEQo7STxAJJSH8CIZ-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d26851041.mp4?token=cW7fzptSbyzHnyI-A86G8kFccfp-D_eWWOhU5E2m7F2zoty2F3qJPQioo022QkopM8f4-p0noS9SIeGRgBnT5ooTapowVAlkBZzDWtgBcRhc5ZMBDX4sy28G290ok5LdtaCrAxKpe1FOSuUzfalju_5XjsNum0lSGb6zQTetE245AjYyrFSbPSGhpJ2m8MAKiQ3iEW5BWvdMU6fsbX_7wmUnQC_FMw6CeB-WE2FJvQExmvOngo0qb98Vq0rnM5lRb9-Gn05rJ20-2JsGhK4jVOYOWX6fwmoW296yX0MvdGPyBqgOJZWOoMJSL30GgoYlWuaXEQo7STxAJJSH8CIZ-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از عوارض خوردن ساندیس زیاد
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69353" target="_blank">📅 12:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69352">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e653ac6e6.mp4?token=GH8SBcJPzLGGcvLiqQAOvEJzsKtowaw-zmywo4adEfDX_xDvisuB0cKMTUbMS8cmjJUh6w6y2kGzCh23S_xRs36UdHUxvMKvJG-DBYUIkw8lFH5cRdxkuz_BQXZwFOVHRhwPAouhSk1wunI20ZJ__wnl3GD5PhAFGUenaOOfANiNfwCDhC-sbeIgziMHZcYYMLaUoCQka1SYtREr4eF-HSlcwTz2qWYdqwfSXyeQXViT8hbj_k-MXaIqT3CKEVZ-HCiCkhPysFdDGNwYIr3NkOe2wkD5EqAn_XOb4PTUVpi1B7LNY4_OvIezMNmXruFR5x0XXAeM4jvTJfl41BVaqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e653ac6e6.mp4?token=GH8SBcJPzLGGcvLiqQAOvEJzsKtowaw-zmywo4adEfDX_xDvisuB0cKMTUbMS8cmjJUh6w6y2kGzCh23S_xRs36UdHUxvMKvJG-DBYUIkw8lFH5cRdxkuz_BQXZwFOVHRhwPAouhSk1wunI20ZJ__wnl3GD5PhAFGUenaOOfANiNfwCDhC-sbeIgziMHZcYYMLaUoCQka1SYtREr4eF-HSlcwTz2qWYdqwfSXyeQXViT8hbj_k-MXaIqT3CKEVZ-HCiCkhPysFdDGNwYIr3NkOe2wkD5EqAn_XOb4PTUVpi1B7LNY4_OvIezMNmXruFR5x0XXAeM4jvTJfl41BVaqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف: میخواستیم خبر شهادت رهبر را ساعت ۸ صبح اعلام کنیم اما تلویزیون‌های خارجی، زودتر اعلام کردند
.
در روز نخست جنگ و تنها یک ساعت پس از بمباران بیت، شهادت رهبر قطعی شده بود.
تا همدیگر را پیدا کنیم و هماهنگ شویم، ساعت ۸ شب شده بود.
قرار شد خبر را فردا ساعت ۸ صبح اعلام کنیم و از مردم بخواهیم به خیابان بیایند. اما تلویزیون‌های خارجی، [ منظور اعلام رسمی ترامپ]  خبر را ساعت ۹ و نیم شب اعلام کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69352" target="_blank">📅 12:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69351">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⏺
سفارت آمریکا در اردن:
از شهروندان آمریکایی مقیم در خاورمیانه درخواست می‌شود که برای ترک در صورت تشدید اوضاع آماده باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69351" target="_blank">📅 11:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69349">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14b8168f8.mp4?token=AtrMmnWHCZ6ctZVxDaYROuCJ_tk8vrm0p5mRg2adVuKKC93Kp8U5tVPkIjvC9e3G-49ePf2vlvfo0TjFNuIpuNgwYmKj7LCU76uMLA0vDPMOX0UQu0ObUoermSThg-GepNvwCm5LRHbs7-93H7Yygk8tEN7gaR9iqQaywfcHpXwRQJQwD-ReCHmNek0h45rFE83KFaT6B85Zy_BMT3lCnNQp6tflMkInyEhE6gmdz0iXrEFHChtDKzzI896DLTy3dFH-i2Hjo0PAphsinf81t1GGSQ7JILNGOm5flL9gbWxl0H_dnin6T2crenpglDq5KSYE1_e_IibajVsx_dFZkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14b8168f8.mp4?token=AtrMmnWHCZ6ctZVxDaYROuCJ_tk8vrm0p5mRg2adVuKKC93Kp8U5tVPkIjvC9e3G-49ePf2vlvfo0TjFNuIpuNgwYmKj7LCU76uMLA0vDPMOX0UQu0ObUoermSThg-GepNvwCm5LRHbs7-93H7Yygk8tEN7gaR9iqQaywfcHpXwRQJQwD-ReCHmNek0h45rFE83KFaT6B85Zy_BMT3lCnNQp6tflMkInyEhE6gmdz0iXrEFHChtDKzzI896DLTy3dFH-i2Hjo0PAphsinf81t1GGSQ7JILNGOm5flL9gbWxl0H_dnin6T2crenpglDq5KSYE1_e_IibajVsx_dFZkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
یک انفجار بسیار بزرگ در یک انبار مهمات در شهر خملنیتسکی، واقع در غرب اوکراین، رخ داده است که پس از آن، انفجارهای ثانویه گسترده‌ای نیز به وقوع پیوسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69349" target="_blank">📅 11:45 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
