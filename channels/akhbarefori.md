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
<img src="https://cdn4.telesco.pe/file/ifTA3EiV27UZq8zQLvkvwN_B6JfnNmcpm9BqRhbCQk263Kg817kKbsaVE_zuGZxLTxPz5W9e9xQVG9xNn3_bYYk_kItSCjYsuYcMdEc0g2Q5n6jS78zjsLW0Fv7IXaaXCEXcrYre5qyWPrGcWxQkYJQ5Qjoi8xAJs_Ony4DE_CPiNtmq0pb6RR9j1ceQxG-5m5-CS1KHcUt-MDWIHQ7pOsfWgHyM7nEWl3UwmYV290nQuREmorGJTUxMT2sIGbDHIPzZKooqRvVw-s6XCOBnhUm5brmVZtc7ZoOXr7QSd3Wk8W4BOEJ8wQH6ZKPTjDj33hvEih3Q_DvRagMA_ll5fw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.07M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 21:59:47</div>
<hr>

<div class="tg-post" id="msg-683163">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EBA68UWtDho0wptMKglYEGNamGNu1700QRIwa29AcpqT1HqpCmNf1A9X-BGxJZXx3m8_8YLKbno6K59cwM8D-EtqsF2gjEKKZnI-WrkA-RoyHnV3EFUcBn9khLJkfKx6at6QvtxMjsMyBkXTH6al7gJTuvxeSeWFc0l_84Y3qcf3p5r9JnI9T_lBhjWi0Hf8VdeLJwEelVvtOdge53z-PUMjCQrsBmA6VK7jhG384CvQ6CREb5G8sly6EOtH7yL0JyTCOtSxwgfUb2MbsckCn8lJH9tPw68D3DnH6gj9wQGw9n2lQums6kuzIROrJm7zhrRyjDf5L6yfSTDB-0ZMrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IgpaUiDvfpqECTN74aQhPynoB3kAesPmOq7WWn7jP3V54oy5v9Y2pWXsKkK-kcCxKwEtVP9EDooKpOwiDL0WirSihRiykJPuCl1K_le_J4XlvkPKU1AK_8-_Z7C27WWMxa_eWhaczHZdQ9sHP6N4N6ZclODSQLIYiMdK_57rR6ITcEAVwyQ_0MzbqnUE_uNiWYAku4NgoKX2uLhSPQvy76pNPYggNHkhp4AmdO_XmmpLDug3lM7bq9Jj3ZiU2AJnFrW2EosP8WizdYlyOjINM8Pj2Yhz9HNEVOaBON7Xu0MuYVYRsD_50Tb4MrZR1tBRlp_pnM6sXtgUHxu4T3EGeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a5da8055a.mp4?token=ZmzuQeXjndOa-AEWOt1SF83UrlgW477iI0VEEwSHPZ2jqo7AvB2QIJPXSFpKCyY2TwNv0rSg1QveU2O787Aq2vhVS0MtCuRITVqEErOK5FdGWI4PAM3HZ0yk4iXI_QYlnrYRTt8ACv-Q1_B9ZgfOyC992Qu_grOrXujbhekw01FWuxBK-1vVHoD5tx8weHksq-t6nb-Tvds9RUBX8kg0ma38r-I8DNXOdaY4P1e0f77Z_zbIM_yUnKUUWiQllSZfup5nz49Hz6cPshImRN7if9rVLLGVXoNMBOjJVOxp60djvCfDlgrL_Wb8y8o328otRNhBNApndiv8GAWnGXVvOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a5da8055a.mp4?token=ZmzuQeXjndOa-AEWOt1SF83UrlgW477iI0VEEwSHPZ2jqo7AvB2QIJPXSFpKCyY2TwNv0rSg1QveU2O787Aq2vhVS0MtCuRITVqEErOK5FdGWI4PAM3HZ0yk4iXI_QYlnrYRTt8ACv-Q1_B9ZgfOyC992Qu_grOrXujbhekw01FWuxBK-1vVHoD5tx8weHksq-t6nb-Tvds9RUBX8kg0ma38r-I8DNXOdaY4P1e0f77Z_zbIM_yUnKUUWiQllSZfup5nz49Hz6cPshImRN7if9rVLLGVXoNMBOjJVOxp60djvCfDlgrL_Wb8y8o328otRNhBNApndiv8GAWnGXVvOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
#پک_استوری
امامت امام زمان عجل‌الله
آقا مبارک است ردای امامتت
ای غایب از نظر به فدای امامتت
#امام_زمان
(عج)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/683163" target="_blank">📅 22:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683156">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda5519a1b.mp4?token=hsgiWuGKI4ZHcZ53c5Ub7ZdA0YIUniI9tklnLbCWXugd0EwrMykDjOPI-B1FZufB3vaPhx3WbHO-mj7hd8mS88vSPLZ9d7bNX11xwdfq4apDNv9FWKrxzvHdJctsPghHRlx0_s1jisXxQdAdPfdFQ1J3Zo7MN64z7PN2ElCFuYpRQZel_u2XsIbT75mf7oJaXT0Vng0Hs_Wz4_8lXnfReL1i-e3E6CtobBcSHoa9pIHU0pKdTjRwthvJeuxsihzqNSJmer9mzD9io6nhnfkYLUxZ1JFE_U9mt0d3lpBJAij61zxvULEXhK3KNKWd0fhuFmmijL1hV2Td96SdCKkKSx2hQik_mSdrDW23WzOdgXzfUBgFx2GzwhJEVVwrKBPc6nLYy51nTCj42t9971UwnEMFJa4Dg_FwnOdUwfBjtKOv5dYjY96haRO83CAv7c0-KmAOdR3Yu4z1xqqY81mSv-EZrSsN8346VPsdotyZjsXlIiwFyBxzAP504d3txQS8pPYgyrHsMfSEkBetm7gOzB05Tgg4I-bmSQHxB3SW3BFnOTQwkvmu8vWE821Q4nj_knbrR0IeQNK_-AUMqsf75zFGa_J4kEG0A6PImroD9Q78lgHvLyUepmv97ZKMUAFrC8XcbHrphw8hsb0NJGG4yr9CC78_gjjJoJt0CB19KqI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda5519a1b.mp4?token=hsgiWuGKI4ZHcZ53c5Ub7ZdA0YIUniI9tklnLbCWXugd0EwrMykDjOPI-B1FZufB3vaPhx3WbHO-mj7hd8mS88vSPLZ9d7bNX11xwdfq4apDNv9FWKrxzvHdJctsPghHRlx0_s1jisXxQdAdPfdFQ1J3Zo7MN64z7PN2ElCFuYpRQZel_u2XsIbT75mf7oJaXT0Vng0Hs_Wz4_8lXnfReL1i-e3E6CtobBcSHoa9pIHU0pKdTjRwthvJeuxsihzqNSJmer9mzD9io6nhnfkYLUxZ1JFE_U9mt0d3lpBJAij61zxvULEXhK3KNKWd0fhuFmmijL1hV2Td96SdCKkKSx2hQik_mSdrDW23WzOdgXzfUBgFx2GzwhJEVVwrKBPc6nLYy51nTCj42t9971UwnEMFJa4Dg_FwnOdUwfBjtKOv5dYjY96haRO83CAv7c0-KmAOdR3Yu4z1xqqY81mSv-EZrSsN8346VPsdotyZjsXlIiwFyBxzAP504d3txQS8pPYgyrHsMfSEkBetm7gOzB05Tgg4I-bmSQHxB3SW3BFnOTQwkvmu8vWE821Q4nj_knbrR0IeQNK_-AUMqsf75zFGa_J4kEG0A6PImroD9Q78lgHvLyUepmv97ZKMUAFrC8XcbHrphw8hsb0NJGG4yr9CC78_gjjJoJt0CB19KqI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی پایان سربازی هم تبدیل به یک «مُد» اینستاگرامی می‌شود؛ از یک اتفاق شخصی تا نمایشی برای لایک و دیده‌شدن!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/akhbarefori/683156" target="_blank">📅 21:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683155">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45944f0cdf.mp4?token=HJMF7t4AMfbdIxdv4aQv3gh8LulSNPVHIIeRY8zyY6Y0SB4PLKr2iL0Gw80vR8DX5y3Tc2vuFNZNr6uJEGFkDcenkmO8sSsQ_VD37BWMlijPN_X-bxlus13i4pS1fFMCtqZzJw8ZqqMOJWQtPiFM3yX39NUuCdugDpNCAlaB7dBEJBLapbHkjvNdiX7MiKo8F5i4aCQfCJsal5BKTxMPTqngHtVniT-HVguhRT7uzpExeX5RaZDUxRT3AcD6IcFSB3iQYfkWl9wvn2eONK3hyqv125k3fIRdl7_IMZBwf7IuFQkp72lSApvKxsJeVLWTiHstVK21ih4vNsn3ak4Gfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45944f0cdf.mp4?token=HJMF7t4AMfbdIxdv4aQv3gh8LulSNPVHIIeRY8zyY6Y0SB4PLKr2iL0Gw80vR8DX5y3Tc2vuFNZNr6uJEGFkDcenkmO8sSsQ_VD37BWMlijPN_X-bxlus13i4pS1fFMCtqZzJw8ZqqMOJWQtPiFM3yX39NUuCdugDpNCAlaB7dBEJBLapbHkjvNdiX7MiKo8F5i4aCQfCJsal5BKTxMPTqngHtVniT-HVguhRT7uzpExeX5RaZDUxRT3AcD6IcFSB3iQYfkWl9wvn2eONK3hyqv125k3fIRdl7_IMZBwf7IuFQkp72lSApvKxsJeVLWTiHstVK21ih4vNsn3ak4Gfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایرانیان در تاریخ بارها ثابت کردند که خلیج فارس و جزایر آن، از جمله خارک، با هیچ سلاحی تسخیر شدنی نیست‌‌...
ادامه ویدئو
👇🏻
https://youtu.be/PkNQz2D9nTY?si=MZvjgT4CBM9FkUZQ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/akhbarefori/683155" target="_blank">📅 21:47 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683154">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
حکم نهایی نظام وظیفه؛ بیرانوند از مهرماه سرباز است
سردار زاهدی، معاون نظام وظیفه عمومی:
🔹
علیرضا بیرانوند از مهرماه ۱۴۰۵ سرباز خواهد شد و دیگر امکان بازی برای تراکتور را نخواهد داشت./فرارو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/akhbarefori/683154" target="_blank">📅 21:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683153">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-poll">
<h4>📊 به نیت سلامتی و فرج امام زمان (عج ) نابودی شر و کفر چند صلوات میفرستید ؟</h4>
<ul>
<li>✓ ۵ صلوات</li>
<li>✓ ۱۴ صلوات</li>
<li>✓ ۱۱۴ صلوات</li>
<li>✓ ۱۰۱۴ صلوات</li>
<li>✓ ۱۴ هزار صلوات</li>
</ul>
</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/akhbarefori/683153" target="_blank">📅 21:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683152">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ادامه گزافه گویی معاون ترامپ علیه ایران
شبکه اسکای  نیوز:
🔹
جی‌دی‌ ونس، معاون رئیس جمهور دولت تروریسنی آمریکا مدعی شد که واشنگتن ابزارهای فشار لازم برای مقابله با ایران را دارد
🔹
او از ادامه حضور آمریکا در منطقه با بهانه‌ موضوع هسته‌ای ایران اشاره کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/683152" target="_blank">📅 21:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683151">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
هند خواستار حل‌وفصل تنش‌های خاورمیانه از طریق دیپلماسی شد.
🔹
سی‌بی‌اس: تحلیل‌های اقتصادی نشان می‌دهد ۲۵ درصد از نیروی کارگر آمریکا «عملا بیکار» هستند.
🔹
رئیس مجلس و هیئت پارلمانی همراه وارد تهران شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/683151" target="_blank">📅 21:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683150">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkgHx1fgekMR8xnn4FVui2aGCDpxhRg-hrxmZBZDOE8fRUlJu5H9wWFmXz6YkKMq-wEqGOB33yfC0jACx7NGtv05TDBY-5DDUtHtpD6FWzP7vxQyxn5Zhi50QfzioiJ7YkvPyGMPNxRC_IDgBRYF90plHDvNf0-eiIxbNIz43nWXeD2say6oDTaUQAa3L9S7nJQSvIH7LbxDj0_Vvb2LVkYasgQUraLvDyNooT053yml8N2QrDS6VwWS45XcO7Dt7I2UyKOiwQdHcRnmmvwxeri4a5S_IFrYccTrWQKao3qMjy5FeMbDHCg13ujda27BdJgikfYcDPmTElFfuxgHhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت جهانی انس طلا بیش از  ۲۰۰ دلار گران شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/683150" target="_blank">📅 21:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683149">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/198312ec77.mp4?token=hugbt3TOSmbofsiwNFBZsVw73dJaXs76zFGZQmwEod7I-Z67atcBlfOfL9yG64BGn1xOUbMeUGWFFdXsq0Lusb1OUAh4dxnmDh6a2j4KuWn-KADysx-LXFexB7c1hU21C3qgIBrbOIa03JUAOVB9p4RJRn2hMe8nyqELqC8GQ4CMGHgFm4b3nlk6yS5WVRf_KN4X9I1qydB643lqxTkfWm3irH7xpQCfbbuLZqG2JY496pjLa4Fdyj8Bf2GnnqMpJXDCvNKdx-qddV4XZy14dMn0BtGSZgDb_jfMHibG1xePqkSoRvsywwDIhc82ojOmiUETE-EouSiu7CQlxGQPSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/198312ec77.mp4?token=hugbt3TOSmbofsiwNFBZsVw73dJaXs76zFGZQmwEod7I-Z67atcBlfOfL9yG64BGn1xOUbMeUGWFFdXsq0Lusb1OUAh4dxnmDh6a2j4KuWn-KADysx-LXFexB7c1hU21C3qgIBrbOIa03JUAOVB9p4RJRn2hMe8nyqELqC8GQ4CMGHgFm4b3nlk6yS5WVRf_KN4X9I1qydB643lqxTkfWm3irH7xpQCfbbuLZqG2JY496pjLa4Fdyj8Bf2GnnqMpJXDCvNKdx-qddV4XZy14dMn0BtGSZgDb_jfMHibG1xePqkSoRvsywwDIhc82ojOmiUETE-EouSiu7CQlxGQPSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شقایق جای خشخاش را می‌گیرد
دبیر ستاد مبارزه با مواد مخدر:
🔹
کشفیات مواد مخدر خلوص کافی ندارد، واردات مورفین هم گران در می‌آید برای همین مجوز کشت شقایق برای تولید دارو صادر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/683149" target="_blank">📅 21:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683148">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ایران قصد دارد بزرگترین نیروگاه خورشیدی جهان را با ظرفیت ۵ گیگاوات در اصفهان احداث کند
🔹
در حال حاضر، رکورد بزرگترین نیروگاه خورشیدی جهان در اختیار نیروگاه خورشیدی می دونگ در چین است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/683148" target="_blank">📅 21:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683147">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bp7yBP28-kZMPAnIy6rf0y3x6ZiC6_CpMBUXgXqr8CsnMyOnva4kgzpykD-WhXz2d1RZpsWlp1f6dp7QvvdmI2pJjqrwN9_LQBH0UzO1ZqU5kG83-LTVRUuW5csWzzAWOpnjWaqa9IUgW-RFYIlqj1LLqCWsmPX0Q5HNrcPKMYZ5YEV5PiTjhp3jsBaYYXvkEYVB_j-zR0Pz7qfAf23_Rsm_r92tglthEteaRuZtzrkPp9gyj81BktN9AVpXLTJkjw62i1Z8ISAzqAnSUP1U5PM4hTqqk748ASZyW-xJBCI5ha6jPMRUvpw6nqxLW383PnMpMC7EMB8BT4z62mj78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از جنجال کریدور مرموز در جنوب تنگه تا شایعه اختلاف لحظه آخری تهران و مسقط در مذاکرات/ عمان؛ کلید جنگ یا صلح ایران و آمریکا
🔹
همانطور که عمان می تواند حل‌کننده مشکل و درگیری ایران و آمریکا باشد، به همان شکل، قادر است این اختلاف و درگیری را تبدیل به گرهی کور کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3239391</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/683147" target="_blank">📅 21:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683146">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAxXokfVnw5tUTnnnPX6QAngT61RWXFjdEFmR_tGc8jQG1liZTNMC6O0vHT-hnpTAEIel2B6VjTh6Hko_fIaItKuRZf26_jEzdfo2xU5e1QSxABazLOnRRSy5g1nNYSXyzUyElYTAOn4-mXdwunyzKqMd-qrYUN5Hb8YuwRHwUnXCqqIZHdsI1CUEVjFPIBY_FNtuK-0X44e1jPJj9wqRXe8mH1hg4PXPXWOv5xQ84KVOo-VBB7ZbtKvmo7L_IfVBhgYPiFWxfDJSfcipFop0sBztZS4f8B7bPOAptgN26GKu1QJyNpF5fDUIpDCGTgtpd66C31OCItRIwFxIP1XSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌼
بیعتی دوباره با صاحبِ زمان ( عج)
💚
به مناسبت سالروز آغاز امامت حضرت ولی‌عصر (عج)، در اجتماع بزرگ «مراسم تجدید بیعت با امام زمان (عج) و رهبر معظم انقلاب اسلامی»
▫️
با کلام: حجت‌الاسلام و المسلمین حیدری کاشانی و علی‌اکبر رائفی‌پور
▫️
با شعر خوانی : احمد بابایی
▫️
با حضور:  سرکار خانم الهام چرخنده
و حسین حقیقی
▫️
با اجرای : امیر مهدی باقری
📍
وعده ما: شنبه ۳۱ مردادماه، ساعت ۲۰
میدان شهدا، مشهد مقدس
🤍
بیایید در این شب عهد و انتظار، دست در دست هم، بیعتی دوباره با امام زمان (عج) کنیم...
@Heyate_gharar</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/683146" target="_blank">📅 21:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683145">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
خیابان‌های نیویورک پس از طوفان شدید به رودخانه تبدیل شدند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/683145" target="_blank">📅 21:08 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683144">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4e4525ee9.mp4?token=JXwqExefPzGM9mSZ4zRux416d5ZLwuOx7ikd_l-cG3rNrRo73COpgX2CtPSIwuzGEgZU-uzTFQpE9HlPsLF5gOs2HeFqhlUAx7UCTxS1tvVHckoNCh9Icws_0vHDghsq5G1bsGrYtl6liRpj0KNRpnpj0LKcUlG174y43NDKaUWpJfDnWblDE50qyIYREKtDO4gCSPfwrt8Ui6-K6y4-uZz12TSEVpyVLeGRkYDflV2ULt1zRLVLrjIL3NuRC0N8WtqbxWdM_QSuJus2MEx1B5sa8mHdgLm9QRUDJytzY2Eh7iKJfyqnT2h8m8cX5H6vTpJGDWR_sjtnNNTu80bl3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4e4525ee9.mp4?token=JXwqExefPzGM9mSZ4zRux416d5ZLwuOx7ikd_l-cG3rNrRo73COpgX2CtPSIwuzGEgZU-uzTFQpE9HlPsLF5gOs2HeFqhlUAx7UCTxS1tvVHckoNCh9Icws_0vHDghsq5G1bsGrYtl6liRpj0KNRpnpj0LKcUlG174y43NDKaUWpJfDnWblDE50qyIYREKtDO4gCSPfwrt8Ui6-K6y4-uZz12TSEVpyVLeGRkYDflV2ULt1zRLVLrjIL3NuRC0N8WtqbxWdM_QSuJus2MEx1B5sa8mHdgLm9QRUDJytzY2Eh7iKJfyqnT2h8m8cX5H6vTpJGDWR_sjtnNNTu80bl3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطوری با حقوق ۳۰ میلیون پس‌انداز کنیم؟
#جیب_من
#چرخ_زندگی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/683144" target="_blank">📅 20:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683143">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afd4c75b53.mp4?token=aq607iI53-xxdbnHnRolyHV6Pznwwv2UwNogwPgORyAlVSsvYDi8ZfJXTuzskw-50pcJl_SYy0o0ZUOagZBMItjLDf0_Cv9is9eULUVkdbGLfv1IBuINOj77tG6wVdcOWbcb7wDbMl-Wd0zsn7MBMpL9LdwqA-ni103LdYaVpT6ZEk7UYzMiiUl_6MmfttdYWh4zIxS-MI9tgVfYVmtElcZaG7GLASXh9HGz3L4Ov9BDEBK0hCkSSm63GbRV3Dflo8UZeIiaJcAyLkzszgPFTRKv_LgrGAhtfhkzkOfNFTSfNcktk28A5t1wuAKQBgIZ-6olX2VpBeeZHrYZQHgxUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afd4c75b53.mp4?token=aq607iI53-xxdbnHnRolyHV6Pznwwv2UwNogwPgORyAlVSsvYDi8ZfJXTuzskw-50pcJl_SYy0o0ZUOagZBMItjLDf0_Cv9is9eULUVkdbGLfv1IBuINOj77tG6wVdcOWbcb7wDbMl-Wd0zsn7MBMpL9LdwqA-ni103LdYaVpT6ZEk7UYzMiiUl_6MmfttdYWh4zIxS-MI9tgVfYVmtElcZaG7GLASXh9HGz3L4Ov9BDEBK0hCkSSm63GbRV3Dflo8UZeIiaJcAyLkzszgPFTRKv_LgrGAhtfhkzkOfNFTSfNcktk28A5t1wuAKQBgIZ-6olX2VpBeeZHrYZQHgxUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ابلاغ پیام رهبر انقلاب به مردم عراق در سفر هیئت پارلمانی ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/683143" target="_blank">📅 20:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683142">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcf5d544c.mp4?token=ACA6OqMZxlLf5awfy7zPhUCSuZDxDa4fVkHQmvaMHvQj1Yj_moBK6Js9GqxKfTolVCsCvy7QF73liWGQMt-EMjrAb_kzArN6c3csPy-fGV-DS8k8-B6xcgLWsAhPJVgnQ-t5i1iZBQQNnThc7SMiv9Qds6RoWdSnjVuEZ-KNUaQJCvnjQbTbLFGch62DolNgZrVEVzp26fn4KooRbWmIsHa4RebPw8p4yxlgZ97mtpHZddagXCXVJPtRN1AqaRQoyLaWzYDMS0OL4I22v8bL83fyZe0CD1ouA8ihnpDMEPjTz3AYI9t7eFYqWPkl-0He-PKajZQbFDJdjhMYhDM3Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcf5d544c.mp4?token=ACA6OqMZxlLf5awfy7zPhUCSuZDxDa4fVkHQmvaMHvQj1Yj_moBK6Js9GqxKfTolVCsCvy7QF73liWGQMt-EMjrAb_kzArN6c3csPy-fGV-DS8k8-B6xcgLWsAhPJVgnQ-t5i1iZBQQNnThc7SMiv9Qds6RoWdSnjVuEZ-KNUaQJCvnjQbTbLFGch62DolNgZrVEVzp26fn4KooRbWmIsHa4RebPw8p4yxlgZ97mtpHZddagXCXVJPtRN1AqaRQoyLaWzYDMS0OL4I22v8bL83fyZe0CD1ouA8ihnpDMEPjTz3AYI9t7eFYqWPkl-0He-PKajZQbFDJdjhMYhDM3Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنباکسینگ ربات انسان نما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/683142" target="_blank">📅 20:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683141">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f649371350.mp4?token=Q1jkm2pUVAgAofr3vx7zGCddoTIxEm6Oag953RPIbdC52F9bHwBkIEZAOHhDj_f5sowmXvTGjVo5DMD3bxt8dgGsWpCASc1SEuR4nJFoyLCgI9Ci6uOOFimoe-f9uMk1VvQLGJR89qBYaxwcRfCFlo80Pf6V8ymzXeiShQtTjqtxaiORBeNA-KW90HBR3juwByID2GirCZCYU_U9EYiNmah5V__OL5GD4Ko8GKP20xvGGrquAsZws2HU36n0BbQbrIvDwv9dBfPO3UfupPb6WTkfbAYUAAfuYlzZvKRyLmCNOXsRzmRcdrZ_wiTmPyd3SG_DOkvchri1BzO_BRNymFLpl9-tp_gARPOm6v7iEizVnPEyT3_-NRD38IfjrF7WoSMpNN1eqrV4ypqghVqJrHAVcxrjORqwI0y90ThCs_P4Ay1S0FP18Fttz72k679_MctsqVtPnc6osc2l9aaP2TuklNW5vkRXUH9j0C6r23W1Vrksjckv3f_-IM2DElGcS4YZb1qW2ttCk2gXo6FEp6NxLiyoWYR2XOKPzqbTOmEIVSFCICcrjXtXoGNW--V0FMvCTOISow-Mql6tzxwnZWbUT-H7zTRIqHbaEww-qlzjEG7VJstrcDPL8baQuI-7qIaCKR3RZZvRT0VHBhWYgqM9wxf__eq8XTJgIz9MXeU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f649371350.mp4?token=Q1jkm2pUVAgAofr3vx7zGCddoTIxEm6Oag953RPIbdC52F9bHwBkIEZAOHhDj_f5sowmXvTGjVo5DMD3bxt8dgGsWpCASc1SEuR4nJFoyLCgI9Ci6uOOFimoe-f9uMk1VvQLGJR89qBYaxwcRfCFlo80Pf6V8ymzXeiShQtTjqtxaiORBeNA-KW90HBR3juwByID2GirCZCYU_U9EYiNmah5V__OL5GD4Ko8GKP20xvGGrquAsZws2HU36n0BbQbrIvDwv9dBfPO3UfupPb6WTkfbAYUAAfuYlzZvKRyLmCNOXsRzmRcdrZ_wiTmPyd3SG_DOkvchri1BzO_BRNymFLpl9-tp_gARPOm6v7iEizVnPEyT3_-NRD38IfjrF7WoSMpNN1eqrV4ypqghVqJrHAVcxrjORqwI0y90ThCs_P4Ay1S0FP18Fttz72k679_MctsqVtPnc6osc2l9aaP2TuklNW5vkRXUH9j0C6r23W1Vrksjckv3f_-IM2DElGcS4YZb1qW2ttCk2gXo6FEp6NxLiyoWYR2XOKPzqbTOmEIVSFCICcrjXtXoGNW--V0FMvCTOISow-Mql6tzxwnZWbUT-H7zTRIqHbaEww-qlzjEG7VJstrcDPL8baQuI-7qIaCKR3RZZvRT0VHBhWYgqM9wxf__eq8XTJgIz9MXeU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بانک ملی ایران: ۹۸ سال اعتماد، فراتر از اعداد و ارقام
🔹
بانک ملی ایران در پیامی خطاب به مشتریان خود، از رابطه‌ای سخن گفته که به گفته این بانک، طی ۹۸ سال گذشته بر پایه اعتماد و حفاظت از سرمایه مردم شکل گرفته است.
🔹
در این پیام آمده است که سرمایه سپرده‌ شده نزد بانک، صرفاً یک عدد نیست؛ بلکه حاصل سال‌ها تلاش، امید و زندگی مردم است و بانک ملی خود را امانتدار این سرمایه می‌داند.
🔹
بانک ملی ایران تأکید کرده است که این پیوند طی نزدیک به یک قرن، همچنان پابرجا مانده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/683141" target="_blank">📅 20:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683140">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VberFzRMDQSx-zOVu32wc46aDpdvTF3xAbOAtjw4tiGw_ZE2Yw4qpSOe65lf4UAeos-tZOgEzjnA423inos8VtHdmqI9Jt0t7hzZZCHTNLWc6OO8x2P8q-HxB8ZKzJrLma8Rl3TTcc_DYZYR22OhEvCm6ZrlzGylhik62nDsrvS0LPJYbghfk3mAERzQtTSmF5KwQqL2rlnPN9W0gpS2vE0IqeQ5Dh7YpfpgIG5ZiLA9a4o75Wjlrb1MNbjd8aQ7VltoyKHij8xrcHGJ1Uk2O28Xu7djlU9BRcVl8AMT-fADlyHxNs8PdQ2jrgIyfH_rXSFw02-Bb6FElloIot5abw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوراکی‌های ضد بوی بد دهان
🫢
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/683140" target="_blank">📅 20:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683139">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b9fc42fbc.mp4?token=cWECzKNIo8WAA3P7EzIihvGNaVS3q10uV5A73ZBkHoCcjfWNOv1mx_uxY9SKdDH9w8OTpUBInXUFwVygdMeE_5-NVQ8F0ujdjmR-AfjrOjQwpJtHlROwIwQEdFI2MOiMAdzZen7bDET0DTKOAkZFuJYj-NXIsiSnVA4kyfzyp2DknlitKX6z8ozOGzuT6_CmCijTdy2nzpj9_9KNjH360juI-QaevJW8GsczfiFy2IC5r52Vhed1joV85qZ1yCmxLUpgfbiVXb8NIo4VPJLnFHHEoqO6C4EFRCg3Z9xmjAuvFw6mRkaiTKo5r7cVdYCkiXIEpWdN9Snz5lm9P2awoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b9fc42fbc.mp4?token=cWECzKNIo8WAA3P7EzIihvGNaVS3q10uV5A73ZBkHoCcjfWNOv1mx_uxY9SKdDH9w8OTpUBInXUFwVygdMeE_5-NVQ8F0ujdjmR-AfjrOjQwpJtHlROwIwQEdFI2MOiMAdzZen7bDET0DTKOAkZFuJYj-NXIsiSnVA4kyfzyp2DknlitKX6z8ozOGzuT6_CmCijTdy2nzpj9_9KNjH360juI-QaevJW8GsczfiFy2IC5r52Vhed1joV85qZ1yCmxLUpgfbiVXb8NIo4VPJLnFHHEoqO6C4EFRCg3Z9xmjAuvFw6mRkaiTKo5r7cVdYCkiXIEpWdN9Snz5lm9P2awoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قصد فرار ترامپ جنایتکار به پنج طبقه زیر زمین به بهانه ساخت سالن رقص
ترامپ:
🔹
در این سالن رقص تا حد زیادی یک بخش نظامی هم محسوب می‌شود؛ با پهپادها، پناهگاه‌های بمب و همه چیز دیگری که در آنجا داریم.
🔹
این سازه تا پنج طبقه زیر زمین امتداد دارد. می‌دانید، تقریباً ۶۵ فوت، یعنی حدود ۲۰ متر، به عمق زمین می‌رود."
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/683139" target="_blank">📅 20:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683138">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/826d7da14f.mp4?token=hGDJ7RKHGjdq7RVBXNddnPb-0F-k0DayavDWruvQB75-7KwzKStouwOhL-Q-MCo8qhD-NuQG2hJI0xDizjgHE7SznK5DZSRT-DAMYhQD69sL3p2Hu7-z6snVydjpsYpTFF6mGDbSnXdlG8QC9pA86iykI8KjnZmcb3KjifZGBGW_BLQNDAxAjifZ8k28yYujAiZkyc731DU2Gaz6gtcDnpnUYbrtB6ib9VxXX6eb0QaakwCchWwNVY4NaXrgcS8i_7swH3__vO7N6LLmpG3jsJAiuua9xqrAFuASl6JrRe8fkq1oNZDniR7Ryx-fwAUyUeiAydhQlcX2nr9tj3kFbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/826d7da14f.mp4?token=hGDJ7RKHGjdq7RVBXNddnPb-0F-k0DayavDWruvQB75-7KwzKStouwOhL-Q-MCo8qhD-NuQG2hJI0xDizjgHE7SznK5DZSRT-DAMYhQD69sL3p2Hu7-z6snVydjpsYpTFF6mGDbSnXdlG8QC9pA86iykI8KjnZmcb3KjifZGBGW_BLQNDAxAjifZ8k28yYujAiZkyc731DU2Gaz6gtcDnpnUYbrtB6ib9VxXX6eb0QaakwCchWwNVY4NaXrgcS8i_7swH3__vO7N6LLmpG3jsJAiuua9xqrAFuASl6JrRe8fkq1oNZDniR7Ryx-fwAUyUeiAydhQlcX2nr9tj3kFbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زاینده‌رود؛ جایی که هیجان و آرامش کنار هم جریان دارند
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/683138" target="_blank">📅 20:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683137">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
آب سرد سازمان بین‌المللی دریانوردی بر پیکر ادعاهای ترامپ درباره تنگه هرمز
🔹
دبیرکل سازمان بین‌المللی دریانوردی، آرسنیو دومینگوئز در مصاحبه‌ای با شبکه خبری بلومبرگ ادعاهای دونالد ترامپ و مقام‌های دولت او درباره باز بودن تنگه هرمز را رد کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/683137" target="_blank">📅 20:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683136">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K42WGrWJfl-50KYay7ZVblYdjAv62ovzbZF47kRTS3YZy5affJByOq6L8aKdilzRm2TrR4Q324P7AzSomZ-CLYrWEvMJklSiHasDKFIsX7HDPgZFE24Mp95zZNx7Bhc8ycJ00v6jBaZA_QihBE5-cS_2u6I-BijDB7iQgDvui9lTQX_sYYfpAP5LXgKMlhJhY14GOT-JRvqkWVYbLFt-o5StIfUTF2ibg9LLDcZ06RZaPa9vSlJxboNNqE-6WFSx1B3wDIZjwGc_idovzB9pwALxkvox2nsKNq_fcspBwkzzMYjJ9iINM7U4ePy0g7AJ-rUupSjzMqVxd3YxO1uqLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر خزانه‌داری آمریکا اعلام کرد پرتره ترامپ روی سکه جدید یک دلاری چاپ خواهد شد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/683136" target="_blank">📅 20:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683135">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jcu_pVJRYPNDGe4AnE5Z8ZKBRH3T2MKXBLa1GG1389x74MW4IMO8KjpfWKbDd8-RuvZ2sbLRPzu9WBEsi_A4kJBRoIWsK0YnDCez55t-uf3p1WTZDknYvuU2ZWsoj3slmprAgrWghKNP-B9tX5-Zz0RwlfH-fzFB1QAy-wfY9JhIYNtYYz_4SckqnzNd5XQAgmWQv9DRhjZ-AWDQA-JOcCBqtDBPKAirxvr9cnDjzc5MaKpDUrh0o7eY47IwAM6MAHPMLM_6RITF_SVqEKG1BpVlAFqG8DIVcoQHA-jE13iZXw0n3disGRR_-Ns-csqMAL7gIMxDGQ3m7z8kRq_aIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: آمریکا با عذرخواهی از مردم ایران، منطقه را ترک خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/683135" target="_blank">📅 20:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683134">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EylqiMj-yS5E6wxCNZUe3Dj7wPKi4oZk4-q8yQfHjsWCtxLhqMqED4Fh8csdpyiUzcEYvY5U2KB2c0Ap8szDdkNC92G6z1T1QJhBYv64cAAfKYmRs6eHdKsFkOZ32TeVlD5gsqHgcyNhHOg7rLKclIMB134YwNQee09PZu7INkWcnYEZNAkguQ7pGaf4Xq1U-Gd1vIGQ-M-lOFAF5T4XNTUcJ58GBYc8N_PocOr0Lo28SZDE3LqLUAt-W275uzBxjFvPXxk9_7Hmi1wlxqIyU5ZTTx9BAVSk7cjLtNj6uDT95VpltSpLpvakxJe1SS8rYWU6AfLjqL11BxW_HdO18g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص‌های سنجش بیماری چاقی
🔹
چاقی از بیماری‌های مزمن و شایع است که علاوه بر تاثیرات فراوان بر زندگی روزمره افراد، باعث افزایش ریسک ابتلا به بیماری‌های قلبی-عروقی، دیابت، کلیوی، کبد چرب و آپنه انسدادی خواب می‌شود. تشخیص و بررسی علل بیماری‌ها، اولین مرحله رفع مشکلات مختلف هستند و بیماری چاقی نیز از این قاعده مستثنی نیست.
🔹
اکنون که با دردسترس قرارگرفتن درمان‌های نوین و موثر مدیریت کاهش وزن و بیماری‌های متابولیک مانند داروی تیرزپاتاید (Tirzepatide) داروسازی دکتر عبیدی با نام تجاری زیکورپا (
®
ZCorpa) و داروی سماگلوتاید (Semaglutide) کوبل دارو با نام تجاری ولوریتا(
®
Velorita) ، مسیر درمان چاقی در ایران هموار و آسان شده است.
برای مطالعه متن کامل این مطلب روی لینک زیر کلیک کنید:
https://abidipharma.com/health-items/obesity-assessment/?utm_source=telegram&utm_medium=post&utm_campaign=pr</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/683134" target="_blank">📅 20:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683133">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
تماس تلفنی وزیران خارجه ایران و عمان درباره اوضاع منطقه و هرمز
خبرگزاری رسمی عمان:
🔹
وزیر خارجه سلطان نشین عمان و همتای ایرانی وی در یک تماس تلفنی آخرین تحولات و شرایط ازسرگیری گفتگو و مذاکرات را بررسی کردند.
🔹
وزیران خارجه دو کشور، اوضاع تنگه هرمز را بررسی و بر ادامه بحث و بررسی‌ها برای رسیدن به تفاهم تاکید کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/683133" target="_blank">📅 20:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683132">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRzdhRhhfNIVYpAsExon_lJyOL7g_sew0z0RD5npoym1rfZJkzBddwzQPAa9i4s8Sr59g6Wr7Qt83vdo2cTirS3kguzhuJxXJu563DoHsAsCP19UYfRch2IGxFOEEp5FCGviBqm-MCEYDgfBLSFrB4YkJUhwSGC5MrznkrrHaP-3Q--fISHUwasI-90K1DJg_Gx4_ZOMMRg7mXNrUVSOP4RJuV_vkWkB_ZgWBgvE-AtO5O921WXaYBED_JmwwbzneiVINjfVZnIKlX5D95PlQTabwqA0XLfBycKTmGYOWCKnwedzDmxNkHL1zjot2_tGrdY043kPSw6OY3pPwruKqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیگه از شر لکه‌های کفش راحت شو
👌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/683132" target="_blank">📅 20:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683131">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpF6doZg2MHT8f3_lEMtehdPssJ6PoyQQg-vqpbMc8npVH5xxzbpNeCPe2V7opQ6lHYHG9gcYqlDxZb_ijWY5u5uBnbsS_d5D71Upwn5WNEtf0AqvKzIl1tbYwEu5hZkuOVFbh9LNrFF7vUwpFlDyPbLiTgspN-pxqz29Vg8kQLuHgAHNXE0Vd-rDqInURstM9tHw6_GQll3EOzwaEQ0qjq9E-ylD2gCw61-FfN7bqeBioeSxesKLbWZZi2jdPlypKeTIA3yD-AipeERnCw41sAx_LWyXSl_rJTfXj8pvijkLvLgVXWuuh04zwBfTtKf5YM4YNscL9j_a5BQEtPX3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا ترامپ واقعاً می‌تواند مانع تجارت کشورهای دیگر با ایران شود؟
الجزیره:
🔹
کارشناسان حقوق بین‌الملل معتقدند که هیچ کشوری نمی‌تواند بدون مجوز شورای امنیت سازمان ملل متحد، یک تحریم همه‌جانبه و کامل را علیه کشور دیگری اعمال و سایرین را به رعایت آن ملزم کند.
🔹
به علاوه تحریم‌های پیشین نتوانسته‌اند جریان تجارت ایران را به طور کامل متوقف کنند.
🔹
کشورهایی نظیر چین، ترکیه، پاکستان و عراق همچنان به مبادلات تجاری و انرژی خود با ایران ادامه می‌دهند و منافع ملی خود را به فشارهای واشنگتن ترجیح می‌دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/683131" target="_blank">📅 19:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683130">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f1a148fb2.mp4?token=BQS9Qd9bStbZ5JULO5dilvwkck7uOEzgV3SIP5JCwuAiyTGqxdHpKsoH3ylkdW8trT4DaIX36lz-JSoGIhE6o1kzBqgkaA-0PQIbJZ62xSyyiG6v1nQyXNA0U764jkLsaz__WWWxZ8B_ICuXl3qevew-xrIJ0GjuC9nV9yDxxsSz7MEax10VOD0Jjm3Mue84z2rlp4hD1qYD0jvUIe17rbOa0ZmG6F440XnU4FDXo_pwojrMpzNbvWuwt3c5UWyGYZi6Az7WDiNQJZDHs3Ki-Ltn70v-SgvQ-qKtiNh1AHAB6vsDfT4huY6NYcZfkf7jho8XwMyv4g3fxoGn_hQC3RkG_ZUutw4WdHUOK9YHT1MCn9Fzg0pN-mXgaEEau6yeucXcqC5mtlq9pr4kkZP_grn3CsSvCmn3OC39bAc_mGfeuQ2t01lVfgybBhhGDxB_aKsormj_8wM2K36oonjmZSfHm3Cx022w-0WaJKcPAJ5rvYgHG5b_hK_Rk72imug6Q5zhf8x4ZAu3qyXb-iHwZ6x6U9R03ATJJZt6fJHgWEl6MrNYmMw_Jhp_3Ieqx9lrHD4PS10AvG7tarUaDejmBnKhziTli6Km5-iIM7znEnTwSFbJc9R5Fhzw9SCD7GxSL8F1dDCjDFl2U06MeFUJZLMn2Mr6W90Q6m6xiUOS5m4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f1a148fb2.mp4?token=BQS9Qd9bStbZ5JULO5dilvwkck7uOEzgV3SIP5JCwuAiyTGqxdHpKsoH3ylkdW8trT4DaIX36lz-JSoGIhE6o1kzBqgkaA-0PQIbJZ62xSyyiG6v1nQyXNA0U764jkLsaz__WWWxZ8B_ICuXl3qevew-xrIJ0GjuC9nV9yDxxsSz7MEax10VOD0Jjm3Mue84z2rlp4hD1qYD0jvUIe17rbOa0ZmG6F440XnU4FDXo_pwojrMpzNbvWuwt3c5UWyGYZi6Az7WDiNQJZDHs3Ki-Ltn70v-SgvQ-qKtiNh1AHAB6vsDfT4huY6NYcZfkf7jho8XwMyv4g3fxoGn_hQC3RkG_ZUutw4WdHUOK9YHT1MCn9Fzg0pN-mXgaEEau6yeucXcqC5mtlq9pr4kkZP_grn3CsSvCmn3OC39bAc_mGfeuQ2t01lVfgybBhhGDxB_aKsormj_8wM2K36oonjmZSfHm3Cx022w-0WaJKcPAJ5rvYgHG5b_hK_Rk72imug6Q5zhf8x4ZAu3qyXb-iHwZ6x6U9R03ATJJZt6fJHgWEl6MrNYmMw_Jhp_3Ieqx9lrHD4PS10AvG7tarUaDejmBnKhziTli6Km5-iIM7znEnTwSFbJc9R5Fhzw9SCD7GxSL8F1dDCjDFl2U06MeFUJZLMn2Mr6W90Q6m6xiUOS5m4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ اگه توی رابطه‌ات با امام زمانت شکست بخوری، کل زندگی‌ات رو باختی!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/683130" target="_blank">📅 19:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683129">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab1e9a0c02.mp4?token=CUvaVl9tXo-fnYUEF7UYPHLMTPkEoYgQyJF90JEuCb9SAtmvPAAQnSvERUvyeL05btotRoY1mr8xbi3QpTWcf8IgSchsM16D27S7Syvp_3CV400cALAuJ0yKrwuIlwd9XTFUYSgM4sUe4GPBFfrunFvZhsYtUHbIyWKBmmh7BouXkNv4jwhedRjdgSD72jhDd5MEzyyQVFNzzkSgiMXH8tunxeLYEGHYHfttTrBS3H62RtikVyVrp71DQoH707dSeZjxRC1clDoSlh2Zs-pdTKIPoeHe9IxL7x7053vT8AZYrU30xBrDictkXrUJQPeK-SxdPEwBkAt8h-Ps1MTFRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab1e9a0c02.mp4?token=CUvaVl9tXo-fnYUEF7UYPHLMTPkEoYgQyJF90JEuCb9SAtmvPAAQnSvERUvyeL05btotRoY1mr8xbi3QpTWcf8IgSchsM16D27S7Syvp_3CV400cALAuJ0yKrwuIlwd9XTFUYSgM4sUe4GPBFfrunFvZhsYtUHbIyWKBmmh7BouXkNv4jwhedRjdgSD72jhDd5MEzyyQVFNzzkSgiMXH8tunxeLYEGHYHfttTrBS3H62RtikVyVrp71DQoH707dSeZjxRC1clDoSlh2Zs-pdTKIPoeHe9IxL7x7053vT8AZYrU30xBrDictkXrUJQPeK-SxdPEwBkAt8h-Ps1MTFRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت سد لتیان
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/683129" target="_blank">📅 19:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683128">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvgaeeiLY25YXrFEPuNKjmz6eiHSfqEOgRCgVJ7JVtJ6s9XHwtq9jv2ejFRrl3NaEndRdoAzFFL9FHNO0Ww7i65oI9yt-ZLKi_mf7ZRMKp5j3yxh3iNsDadRnhyx-Sc_a4jsPbzEqOhn_Fp8_kf2sRrROAwQBbqyYPStY0Jowf9pXn9R9013H1TzmYSfve7iTB4IlnSlYdhdbA4C27A-NNIQpXrqsngvOG44B6lM9LrzsNW8LmxQLoLQ01lOMhEbmej3WhItM4E6WgebqiIacDJqkPyCkLTmgEvBb3yStyCQ4nns_xge2L-sGkyrSNHvwCJesvzjcsNnyPDEtBNXxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسن‌ترین زن جهان ۱۱۷ ساله شد
🔹
اتل کاترهام، زن ۱۱۷ ساله بریتانیایی، بهعنوان مسن‌ترین فرد زنده جهان تولد خود را جشن گرفت. او متولد ۱۹۰۹ است و راز عمر طولانی خود را نگرش مثبت و میانه‌روی می‌داند.
🔹
رکورد مطلق طول عمر با ۱۲۲ سال در اختیار ژان کالمان فرانسوی است که در سال ۱۹۹۷ درگذشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/683128" target="_blank">📅 19:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683127">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qL51HCTBHiisEVn52W95syawoQCcX8D9DbO5F5TIzY2qBI5yhLTCUd1kErZOIfsv_cN8Ms_h6tF3qpD_5Gye3c0N1kZezbbq-VgpMsxo55Jtlua7iUCW4Bc0KimUfBQVTbFNg3IRfbn6HVHAk537HTKbCxFjCMwsCIxRTNfk1XJyv4CxU3uIu98YUyBJyPlWIkLh7ra2bzzs4Rv3no_1vbfJYk28NWFDGMt9DsSqCaYRUGsOpIAWkDDb05GSJ3abMH9M7QmpaB8g5m_-QVNu2rMWK1Wp7HRGpzZz_DrmGTxaJ4qBtgbARk8mCtqHs6F_hGfl8hix2b63PzB0TTeAXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/683127" target="_blank">📅 19:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683124">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bbc1c9f3b.mp4?token=EVA1mV0_Qhx0lIOGM043itdKMqMkPDuWHOwty5NSRvTp9uTD-Zc7LA_uZIJmCWrzvXeW2sg-z0_RC5_OwJ7pk1EK1jsbzF56pXgZBsddhbl1DYiR6KCHb7urlsUjoKn6SEqY9hnsNXiJdMaFbx_M3vR0ENqIZXJTRYyFM_by8WsrSti727mRXTloDmmQDaJVV3dfL-dlII8vFSZPMWTQtfbY1QOeaFFNB1R-o4d2nXwdOKX8wcxlISWYOwBN-ZoD-qxP8htcaR_S1k8Ka9xkr7ZHo6s4ZirDkLu5t4MNYiZSgbeE6onQZifHrULmmqmp4j4Gy5cORqMKNz_AbrQvQ2PaQ552kZ9GFsL4jOZmVuKkDaJK_pRIOr3DkFmcgD-6il-MU85VKSY9_8UxQCwMIKMsiOTgiPuLUL8FotwC0J3-BNBXT8q0oJ93SrIJwRwHpjyXg5KNxN3lJEKRxzJQgnKcxKUrk8O3I0v-FWjDjLCAaXrjXl_FW6x4DpvWBXM0yS07as-NWLN51DIDvLOVSY3g7eAos8okyrEm71bgWkuH_-wPO7D4ffOcWd5czE661m_RNS2dixS4pZFSnYznTX9Vr8-fag_5cQqs-05BIjN5n2vB5-7wRQGkiIjdSkD0n9c0MisTWbnn8Zi-rwUB7GVml3KQkQEYhNHAKB_zrIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bbc1c9f3b.mp4?token=EVA1mV0_Qhx0lIOGM043itdKMqMkPDuWHOwty5NSRvTp9uTD-Zc7LA_uZIJmCWrzvXeW2sg-z0_RC5_OwJ7pk1EK1jsbzF56pXgZBsddhbl1DYiR6KCHb7urlsUjoKn6SEqY9hnsNXiJdMaFbx_M3vR0ENqIZXJTRYyFM_by8WsrSti727mRXTloDmmQDaJVV3dfL-dlII8vFSZPMWTQtfbY1QOeaFFNB1R-o4d2nXwdOKX8wcxlISWYOwBN-ZoD-qxP8htcaR_S1k8Ka9xkr7ZHo6s4ZirDkLu5t4MNYiZSgbeE6onQZifHrULmmqmp4j4Gy5cORqMKNz_AbrQvQ2PaQ552kZ9GFsL4jOZmVuKkDaJK_pRIOr3DkFmcgD-6il-MU85VKSY9_8UxQCwMIKMsiOTgiPuLUL8FotwC0J3-BNBXT8q0oJ93SrIJwRwHpjyXg5KNxN3lJEKRxzJQgnKcxKUrk8O3I0v-FWjDjLCAaXrjXl_FW6x4DpvWBXM0yS07as-NWLN51DIDvLOVSY3g7eAos8okyrEm71bgWkuH_-wPO7D4ffOcWd5czE661m_RNS2dixS4pZFSnYznTX9Vr8-fag_5cQqs-05BIjN5n2vB5-7wRQGkiIjdSkD0n9c0MisTWbnn8Zi-rwUB7GVml3KQkQEYhNHAKB_zrIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از تصادف رانندگی سنگین در نیویورک
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/683124" target="_blank">📅 19:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683122">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
آکسیوس: بازار نفت دیگر مثل گذشته به اظهارات ترامپ درباره ایران واکنش نشان نمی‌دهد و معامله‌گران اکنون بیشتر از مواضع سیاسی، به واقعیت‌های میدانی در تنگه هرمز توجه دارند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/683122" target="_blank">📅 19:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683121">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDeu7S3vynwssCVieU3ledmOdYxbtN0ZCBXhoF6ObVExFml71OfAtoJgwOlFytNc0RFcXXToOBtMnTWm5iCWiGJYSNK1Fg9lcGcndFxQiOSEjf3fkT2qGpJF69_YI_fbaKMAhtX3zc1Varsv3yw4LQA0jft082rnaI8Z2VpRotB2A77dEXem4vXHHVy0TKMf3clh42EnRp08C6_z0kMqLoEa-b8VBHaX1gt4s07j0_Zau-EUPdxTwjjmPePmxVLctpjBGgd5LyyZO5VAA3nadMCmNYv27lcE6JI7ByNhcCtbN8LT4mD3WP5Cwn84H2Jn4j5l8CGxiwu3jEijOG5ojw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینترسپت: برکناری‌ها در موساد نشانه شکست از ایران است
🔹
این رسانه آمریکایی با اشاره به برکناری روسای اداره اطلاعات و بخشِ ایرانِ موساد آن را اقدامی بی‌سابقه خواند: آخرین مورد از این نوع برکناری‌ها به دلیل بی‌کفایتی، حدود ۳۰ سال پیش و پس از شکست طرح ترور خالد مشعل رخ داد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/683121" target="_blank">📅 19:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683120">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0140942b56.mp4?token=JBCk8ueXMrk5z8m_MwdaSIjCBZw4eVQfOmV9Gg4o5zzKq7oTLnaje8efjBPsa86HbMmZcbGiJB9hs_cv9om_pK640t4GGu7KCSowu30_ADvW-AbEYPYUozbTCwWIVl62GsUx7dwBOJdGCLjM9yMM2MJ5JHnn6PScN1snGTxYJVqPn6bP2TXKyLL5HQHIoNio7m1aooOZaJs-m6WP0PG-NhIxo-flyw2aJLN3R_jikfOrRD57Kp3XQLQ0BinfPHPky_i73N8H9HW7fVt1GL1fIt3qfJ911niAvZvP5oJA34T97U8vPYslgx2SnrpwWI29Z4R-Ty79qiG58Z4aT73B7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0140942b56.mp4?token=JBCk8ueXMrk5z8m_MwdaSIjCBZw4eVQfOmV9Gg4o5zzKq7oTLnaje8efjBPsa86HbMmZcbGiJB9hs_cv9om_pK640t4GGu7KCSowu30_ADvW-AbEYPYUozbTCwWIVl62GsUx7dwBOJdGCLjM9yMM2MJ5JHnn6PScN1snGTxYJVqPn6bP2TXKyLL5HQHIoNio7m1aooOZaJs-m6WP0PG-NhIxo-flyw2aJLN3R_jikfOrRD57Kp3XQLQ0BinfPHPky_i73N8H9HW7fVt1GL1fIt3qfJ911niAvZvP5oJA34T97U8vPYslgx2SnrpwWI29Z4R-Ty79qiG58Z4aT73B7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جاری شدن سیل در جادهٔ روستای گیفان خراسان‌شمالی
#اخبار_خراسان_شمالی
در فضای مجازی
👇
@akhbarkhorasanshomali</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/683120" target="_blank">📅 19:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683118">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRL4TmyXrKpMzqLcIHgNbzDX72AiWiPN2QCcDtrvt4cHIlC6YYrqAQbdQYD_X9zylmnFsGRfzCRooJI72LnsA4ejTH2bOYnu193etgXEc23ssrZnx1ppoMGVlPGnJN03ubTtt-MwaFepAlEGLWPlxs93aq21UVzMbga3NMoWZwy8WwRjVGP0dKDnnjs7r0mHz1VLwVfgxR72CKpxmxOY0RN5h2THyBS6Fjnz6x8L6bHN8za-XdkbIay6wfrMwD88YO96B_gSHeOZAxRkDiOZyy5EouH9BjyzLLmJpGFWD2069RjKFekKed2zj9yZDIBAdz4pDbm_lEMQAxEnmLaOlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتانیاهو کودک‌کش: اجازه نمی‌دهیم اردوغانِ دیکتاتور سوریه را اشغال کند
🔹
نتانیاهو با متهم کردن اردوغان به دیکتاتوری، یهودستیزی، کشتار کردها، پناه دادن به حماس، اشغال نیمی از قبرس و زندانی کردن مخالفان، تأکید کرد که اجازه نمی‌دهد او دامنهٔ تجاوزاتش را به سوریه گسترش دهد و اسرائیل چنین کاری را برنمی‌تابد.
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/683118" target="_blank">📅 19:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683117">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/466763a826.mp4?token=WlI8tisPOiEwy5k1xnKXvX_7x-UaflrzqRR0Ea5LHsSmzwSergH5A3LnToX-vrQnBzH9r6e7rq_NsbUxcnRgijYGUCctIITVb-QtErFuuDjWx_ej8iwts574AuS9F6pe57NjvFSfyCE0kyCn-A5FfEI80shrT4zHQ6oRDZ4qVtDoCpPXfycdook2xpayLG0-YgP0XW5RlumW_PCuo6mlymXPJyIB_E8dNHj3ZK0iiFPctOvY5YituXdD8fw5HXyTZ2yrvbae7_x2tEWZqppHvgYuyXMyMmLEURjyp5OfGde_xaXtjrVFZ6RcmanZMSgqh4aawVYPww9LmLVEL_ytuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/466763a826.mp4?token=WlI8tisPOiEwy5k1xnKXvX_7x-UaflrzqRR0Ea5LHsSmzwSergH5A3LnToX-vrQnBzH9r6e7rq_NsbUxcnRgijYGUCctIITVb-QtErFuuDjWx_ej8iwts574AuS9F6pe57NjvFSfyCE0kyCn-A5FfEI80shrT4zHQ6oRDZ4qVtDoCpPXfycdook2xpayLG0-YgP0XW5RlumW_PCuo6mlymXPJyIB_E8dNHj3ZK0iiFPctOvY5YituXdD8fw5HXyTZ2yrvbae7_x2tEWZqppHvgYuyXMyMmLEURjyp5OfGde_xaXtjrVFZ6RcmanZMSgqh4aawVYPww9LmLVEL_ytuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت‌های شما از دلایل تجرد | چرا ازدواج نمی‌کنیم؟
🔹
صداهایی از جنس حقیقت ؛ بازتاب پیام‌های صوتی شما پیرامون موانع اقتصادی، فرهنگی و اجتماعی تشکیل خانواده.
🔸
پیام های صوتی  خود را  به آیدی زیر ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/683117" target="_blank">📅 18:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683116">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/En8B6rwhXf8up_gsuVjomEE3DDLKAWPiO_61ZE1RtRLF04faMQh7hfsSvhJ0a5TIdIKlQOZSvn_SGgRuUDyxbUMbtruzT3qMI6NoApiw-uN_tKZY5PIETzFs2eVqTyjXNRSxnpMIeUjfduKG27igHPx8-FRRAm478b3ZqF4ujAs7sLmc_7XepCGxuTpiLsYtUG_iAM9HL7U0GJCQT2pBS8wa7Iy9AnpbHkKmQkAsTQtjpP9DkhYlmslNwFyFKhXklHgh6mLUhAQdHkd5nvR4PpdZjNmfAAWT3vpVy_ayd-TA-T1DEdCcserKQHix7d1ZT6sQ0zFbQl-dZXBCORFpLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش سید عباس عراقچی وزیر امور خارجه به ادعای کمرشکن‌ترین عملیات اقتصادی تاریخ ؛ این فیلم تکراری نیز محکوم به شکست است
🔹
۱۴سال پیش:
«فلج‌کننده‌ترین تحریم‌های تاریخ.» شکست خورد.
🔹
۸ سال پیش:
«فشار حداکثری.» شکست خورد.
🔹
۵ماه پیش: «تسلیم بی‌قیدوشرط.» شکست خورد.
🔹
امروز:
«کمرشکن‌ترین عملیات اقتصادی تاریخ.» این هم محکوم به شکست است.
🔹
این فیلم را قبلاً دیده‌ایم؛ همان داستان همیشگی، فقط با قلدرهای متفاوت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/683116" target="_blank">📅 18:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683115">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
فرمانده کل ارتش: صنعت دفاعی ایران با خودکفایی و تجهیزات پیشرفته، بازدارندگی را افزایش داد و دشمنان را به تغییر محاسبات و پذیرش تفاهم سیاسی وادار کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/683115" target="_blank">📅 18:49 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683114">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ce969d3d3.mp4?token=c2-ob2svoDN_NvMzoJAzdA7c3BchLYYIHC-srFJHkFO_9a7t16vq-sYqVWIx9m4bP88N5eZj5oyNzaIzaOBbIvitdxEfyovNpkOxPU9W6lzX0BygHA3t1LQmPeYl2-1gbWDppL7fNCN6RPo4EUJ4O7MSLXCuhhbDdi5MzU0PsPJZ7dgU7rHSripaF4Cal_xnq6SnkvWtejo9P9QzAV6f0jIRPZ7NLP80FgW9FshbLECD9eF2cH2J73HISjC-xDizycdH3qnycqvaVUHpqAGtFzDTNPHghds1Uz6FCrDRnnzXZR2HFHl2DAyNntAkuLpCIbMIi7Ce7B87e7dZ3aII3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ce969d3d3.mp4?token=c2-ob2svoDN_NvMzoJAzdA7c3BchLYYIHC-srFJHkFO_9a7t16vq-sYqVWIx9m4bP88N5eZj5oyNzaIzaOBbIvitdxEfyovNpkOxPU9W6lzX0BygHA3t1LQmPeYl2-1gbWDppL7fNCN6RPo4EUJ4O7MSLXCuhhbDdi5MzU0PsPJZ7dgU7rHSripaF4Cal_xnq6SnkvWtejo9P9QzAV6f0jIRPZ7NLP80FgW9FshbLECD9eF2cH2J73HISjC-xDizycdH3qnycqvaVUHpqAGtFzDTNPHghds1Uz6FCrDRnnzXZR2HFHl2DAyNntAkuLpCIbMIi7Ce7B87e7dZ3aII3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: تفاهم‌نامه مفصلی در حوزه امنیتی میان ایران و عراق امضا شد/  ایران هرگز در امور داخلی عراق دخالت نمی‌کند
رئیس مجلس شورای اسلامی:
♦️
عراق در آستانه خروج نهایی نیروهای خارجی و تثبیت حاکمیت مستقل خود است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/683114" target="_blank">📅 18:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683113">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKvTHhfq_hEZbSQXaypUOUGcIKjq7bhBnB_FaPIU0t3NxmS8Cv3Cd7SGyGxPPmgLBALTJZHPKYQAU4xmwHhLH-fnBnVF3Y5hyc2qgzCsdDHE1Gm_O5UO4HNtiu-dV7Mjfwj8I20qAblcna4JuE68l2GaGUJeHXozzU90NEoDv6G8ooqzzQ7DORv81DCmd3zYJ_s0TrvB37FsnNWcmaH9QYOmLlahGo8oyHaDoQAeTqPZaHnAl3LQqalXI9QpFR931qgSjwEQ8LJHywShJOtRMnRcgSFyuZ62sL75YR1IxHzFjroEgkFnMKMVmP6iDZig3InKV7woq0E1riFbfPSQUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده نیروی دریایی ارتش: به‌زودی در پهنه دریا درس تاریخی به دشمن می‌دهیم
دریادار ایرانی:
🔹
شرق تنگه هرمز و دریای عمان تحت کنترل کامل جمهوری اسلامی ایران است و تحرکات دشمنان فرامنطقه‌ای به‌صورت شبانه‌روزی رصد می‌شود.
🔹
نیروهای مسلح تحت فرماندهی کل قوا محکم ایستاده‌اند و به‌زودی درس بزرگ، تاریخی و فراموش‌نشدنی به دشمنان خواهند داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/683113" target="_blank">📅 18:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683112">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhndI4KNUig8X6QMbz2g_QJnv4MISNM4na92MFtKRomC_cRVF6W-jyjFgQA2OcohQtV0WkVX9VcpEQ7y1t9YmI65Sb5s2vakMt2QAOokxUs8yQN_-NTOgrQ5_qApOYbcWgjE2k08tK7ReGcGiTrhQBLDn9eVB4SMmFdqvdEbX8ysVUj9g0nZmnKFIPwvPRNxfB3spNe0Q6kn6T6Ve84M_rofpV6wUSDIxt3rKmlkjbiU7slw3XJz8d5BMfYL99Na8O1MOMkVVG3wa0_oAu3SFz725mipidHn0XujHcVl3EzlFOfYHNRn9rzYBCHyfz-qGgqAHk9hNWgg3TtyISNSEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار مبتلایان به اختلال نقص توجه (ADHD) در ایران و جهان
🔹
بررسی داده‌های سال‌های ۲۰۱۹ تا ۲۰۲۳ نشان می‌دهد شیوع ADHD در ایران از ۱.۸۵ به ۱.۸۸ مورد به ازای هر هزار نفر رسیده است.
🔹
در همین بازه زمانی، میانگین جهانی شیوع این اختلال از ۱.۸ به ۱.۰۹ مورد به ازای هر هزار نفر افزایش یافته است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/683112" target="_blank">📅 18:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683111">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed0ebad46.mp4?token=NmONXdOCFzO-40EBthbIiE5ydPWvihE_7wllDC03qTCQG3s8MfMlQH86qJtIbxfdnXQ_2NNHSEQMqKVXTavN0_v9AftkP7R7RFTcWYh9oK7WggOSnwihqEiI_2eq0cyKkApDYylzWcky-WGFzaQXCzitPMVe_LoyW3Ktpsts5QVJgdxeIIF3ePG0gUUcfV8MPY_KO09bADUjGahtK_hUW81mhJfv0-tCrEzT1_NMZiYEqYZICRZ3rGR24z5gUthD8eVqGQEZ8I9DYOle9qBCEwfB63XIkIxSXRoaoqM7fVF9u6p_lNrX2u3-cps0R3IkA4vkYTW_J7L4YYRHd6vMKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed0ebad46.mp4?token=NmONXdOCFzO-40EBthbIiE5ydPWvihE_7wllDC03qTCQG3s8MfMlQH86qJtIbxfdnXQ_2NNHSEQMqKVXTavN0_v9AftkP7R7RFTcWYh9oK7WggOSnwihqEiI_2eq0cyKkApDYylzWcky-WGFzaQXCzitPMVe_LoyW3Ktpsts5QVJgdxeIIF3ePG0gUUcfV8MPY_KO09bADUjGahtK_hUW81mhJfv0-tCrEzT1_NMZiYEqYZICRZ3rGR24z5gUthD8eVqGQEZ8I9DYOle9qBCEwfB63XIkIxSXRoaoqM7fVF9u6p_lNrX2u3-cps0R3IkA4vkYTW_J7L4YYRHd6vMKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حقشه!
🔹
جمله‌ای که ممکن است روزی علیه خودت شنیده شود؛ حرف تلخ عمو فیتیله‌ای درباره قضاوت آدم‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/683111" target="_blank">📅 18:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683110">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn9biPFFiz8taQHrTP8Cvr7eMEJxblxQwQzejJ1K1H9JQpjWDo5ochhibFFfgSoz_VLEenxlqddBDa-PVF2KJyfqi4EtivMUspvP30bPGIXN-upDHL9T1wtZaS-QAVO-oIJiZFl2kufu2U6vlr8SLm1y8fx5WJ80blMtwg8mdVlVEoCjDbo3chOz0fPGIJpg7jI3XAHaFxjHRiVfd_WGSr0OM4leKt39QiI5PtmlS2IuTra9imWFEbJ9rAvWI4mbBKanJLH22NMLMXI1Tu4s5ZFYG5WMIQxz_R9DFsT7YQbQ9culuFg-ZoQOMXyk3grNm0-qMwBE2UtsqQ3zO-G52g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قهوه‌ای؛ رایج‌ترین رنگ چشم در جهان
👀
🔹
حدود ۷۰ تا ۷۹ درصد مردم جهان چشم‌های قهوه‌ای دارند؛ در مقابل، چشم‌های سبز با حدود ۲ درصد از کمیاب‌ترین رنگ‌های طبیعی چشم محسوب می‌شوند.
🔹
آبی ۸ تا ۱۰٪، فندقی و کهربایی هرکدام حدود ۵٪ و خاکستری حدود ۳٪ از رنگ چشم‌ها را تشکیل می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/683110" target="_blank">📅 18:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683109">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ادعای سازمان تروریستی سنتکام: ۶۶۰ میلیون بشکه نفت با حمایت ما از تنگه هرمز عبور کرد
سخنگوی سنتکام در گفت‌وگو با سی‌ان‌بی‌سی:
🔹
از اوایل ماه می تاکنون، نیروهای نظامی ایالات متحده به عبور بیش از ۶۶۰ میلیون بشکه نفت خام از تنگه هرمز کمک کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/683109" target="_blank">📅 18:12 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683106">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RZhnIx9P2h_Glg7kQw-LYqnqKXCcVMN8HECxjhW0XL3Gf99GGHXPRq6vujMFja19Rk3vk5fh0bPqEGhNuhqoy7OLhdMOGykjV1BzuTfJG6ttOyTfnHWYeXmJmFNeOF55IQ22e44WxOcBDRTRKHjRXhvjaO_My9OYHJaqpng5uP5WCfazm7AMHFQqRSyI9cenErN2JG2A87xJPeeuHdUOLNnxaBUjBu7uAivDCr9GQuIKOAk01zaexIXSYxDvv3EBDlpO4k-zm8gI6BDXWQhFWd705zNCHd_M66B2GEw4rb0PI4AcM1lSdbX7zC7ehjV8s1HBQxhD-liP8usF6tP0VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KeqylryXKJX36Gw6KeE_SsI_DFR8XtuJvY8JDt3iQPKZ6nfzgfnAsnmkU5eoitEfAFdwXaM7LA2LMt1kmJ6CbeU4qCWppWBPgA2tFrPVJ7S4M7pcvvDdcK03tUUZXHfxxvSWv_Z67q4jns9ki0ezD9BBg5_DobGlBhDGdT5OUQS762SYWT3qhGWIKNZM5wicRCoOLFrqLKz2iSvJN9fTFtxuTSSgcKOJlWCROyvSDqGHwZIEoVlM_ZAiva9fHG4itydN0nm3-Dd9Hr4JuQXp7Jq1hRdUxYlUpNCPnrcXTZ_7bCEecztCjTgY271GRrfk0j_lNDGpZTkaXlpRCSo68w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YmcUviaeky9X9TmC8JMUxocewnayyLOVof9Vl2JDr7DTJJhOpyv8c8vs3PEBdRXJonT5WgWJTSCe-luVlSu1DP-_f7zjfp6z6XasefRiCrXzSYktX_2YiZU01CPzxDBcya4y7cOVCyKkU2swRF6RntUsFLNci9N9My2BKlMPgaPER4cPV6WAAkgkWbKGWFkvDMHz1Kt7wLd8GNVKvs3G7KWtJSucIQ9iFU-J4mmiXWE1-vFbaLRzW4dmfD71kXDDYcjzQi4UPtdQBNVCFD9Ov7JV0sd2h5Y3ZhhRfuyxmBTTOjLMNrjFHMkNJAwvDp0GLjW0DeIuP6AS1Giw-iJeLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بارسلونا؛ شهری رنگارنگ و تماشایی
🇪🇸
🔹
بارسلونا در اسپانیا با معماری و خیابان‌های رنگارنگش، آن‌قدر زیباست که انگار همیشه یک فیلتر رنگی روی شهر قرار دارد؛ اما این جلوه در واقعیت هم همین‌قدر چشم‌نواز است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/683106" target="_blank">📅 18:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683105">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fbe2dacb5.mp4?token=rXHHKQcUqT9pdx_F86OOzuhnfLWYJkFyyJD6E1ib4CaX_hBj1IRNVChkEeXLhs1DUx8C1Jc4HT7GMF5QVaGplitd9fbWYTuPXDoJ9oxs7JQbE5froBpY9SXhFptCxwxkjzPkfmQ0RrzDj6SHY0mo-U9dGCHLwj-8Y7nXsHNfDN-dN9_htTTGrhZgnOQSKoKPe9OiJFItM9IDidhhczpTgvT_fW0StF05AhYe28C_3fklPBvCgrdmU_LJy38tftQuNTFY2CwL8_ef7OiMalRIh7JNwSQbHJ8hU25FNYQlBxsuFBsbQCpg6jceTy-GkRrP0eRXZLCjXfO2MImmTjdX1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fbe2dacb5.mp4?token=rXHHKQcUqT9pdx_F86OOzuhnfLWYJkFyyJD6E1ib4CaX_hBj1IRNVChkEeXLhs1DUx8C1Jc4HT7GMF5QVaGplitd9fbWYTuPXDoJ9oxs7JQbE5froBpY9SXhFptCxwxkjzPkfmQ0RrzDj6SHY0mo-U9dGCHLwj-8Y7nXsHNfDN-dN9_htTTGrhZgnOQSKoKPe9OiJFItM9IDidhhczpTgvT_fW0StF05AhYe28C_3fklPBvCgrdmU_LJy38tftQuNTFY2CwL8_ef7OiMalRIh7JNwSQbHJ8hU25FNYQlBxsuFBsbQCpg6jceTy-GkRrP0eRXZLCjXfO2MImmTjdX1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله هوایی اوکراین به پالایشگاه نفت روسیه
🔹
پهپادهای اوکراینی به یکی از بزرگترین پالایشگاه‌های نفت روسیه در پرم حمله کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/683105" target="_blank">📅 17:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683104">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/683104" target="_blank">📅 17:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683103">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
مصوبه مجلس: کلیه فعالیت‌ها و ارتباطات افراد با اشخاص خارجی باید در چارچوب قانون جدید صورت پذیرد  مصوبات تازه مجلس:
🔹
هرگونه فعالیت یا ارتباط اشخاص ایرانی یا خارجی که منجر به نقض وحدت ملی و موازین اسلامی شود، ممنوع است.
🔹
هر تبعه ایرانی که اقدام به اخذ هر…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/683103" target="_blank">📅 17:47 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683102">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffhlS8jAzeiNDVdlXOy6ZSmAwZpyAHSrvRvzCz9YI0wL1tu-7VUMX4NEehmUkxfS8UZ2ypR9E_kpcgJAFJNiHAklYOpogi_OPby38677FsqPIkzkXcRr1mY7maeMxOaSyc7ZRApK9Ul9t_V9djAxTbTWdMcAREGU-EnJCq488uUtEF-8mgMIwgeqZ6pqfBMv930woDX_jWfHlQ9ek02n80gZtxcuSvsl0muzInTW7QiHWiyfwvBywTPG9bBKRjXHPgRwWg8R3qXY4GI-nujboIbY__GpzVA0g9ituyfsI8n6knD40IkDZ2i5FoakZp8koVI8lwU-fOglbnFktt3ZyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
آخرین جزئیات پرونده ۷.۵همتی بانک کشاورزی
⚖️
احقاق حقوق بیت‌المال پس از ۸ سال
🔻
در پی صدور رأی قطعی دادگاه تجدیدنظر استان تهران در پرونده مطالبه خسارت از سعید جابری و محکومیت وی به پرداخت بیش از ۷۵ هزار میلیارد ریال، حقوق شرکت کارگزاری بانک کشاورزی پس از حدود هشت سال رسیدگی قضایی احقاق شد؛ رأیی که بانک کشاورزی آن را جلوه‌ای ارزشمند از استقلال، سلامت و اقتدار دستگاه قضایی در صیانت از حقوق عمومی و بیت‌المال دانست.
🔻
ماجرای این پرونده به سال ۱۳۹۴ بازمی‌گردد...
🔗
مشروح خبر
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/683102" target="_blank">📅 17:47 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683101">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06dc26b5e1.mp4?token=dkPbt7iBsBaFKcTlP1UHXQPISkmxT7rTq-D4Tx1swDk72yYEaJvfWhfeDWwi8fkqSLl6rs168awvvnEax8WTVaFZJPjMf2RotH7n0666otoYFHlAG2epihuO70fJspQZtwFI25VAcBoQAVdV3tS9-FEVVFR3ERaMj61QHgjUdjybMLvXre5ff4GEPTct3GwHSw4GyjPEDyWQqiF4qZ1i-lMbifkb9CLL9qV7mOIqPNeMvnEHBWU63kR3T_HWDPufKb9NDdrXFqY5fsEfxMen99QOu0MO8GUY23IItRq_dxMd-lbIGlee0V927eZN7RGFHcL5QZvDTTv5RTEZ3WWQ9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06dc26b5e1.mp4?token=dkPbt7iBsBaFKcTlP1UHXQPISkmxT7rTq-D4Tx1swDk72yYEaJvfWhfeDWwi8fkqSLl6rs168awvvnEax8WTVaFZJPjMf2RotH7n0666otoYFHlAG2epihuO70fJspQZtwFI25VAcBoQAVdV3tS9-FEVVFR3ERaMj61QHgjUdjybMLvXre5ff4GEPTct3GwHSw4GyjPEDyWQqiF4qZ1i-lMbifkb9CLL9qV7mOIqPNeMvnEHBWU63kR3T_HWDPufKb9NDdrXFqY5fsEfxMen99QOu0MO8GUY23IItRq_dxMd-lbIGlee0V927eZN7RGFHcL5QZvDTTv5RTEZ3WWQ9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار بیانات رهبر شهید انقلاب در جلسات روضهٔ‌ خصوصی شهادت امام حسن عسکری(ع) در سال‌های ۹۶، ۹۷ و ۱۴۰۲ برای اولین‌بار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/683101" target="_blank">📅 17:44 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683099">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec0b3d8249.mp4?token=YOO-Qwl31_fNRjlwyRdG_i7CBn6pDm9r7dth4QbXYdIuuBUShsADal_ZDWTWOQ0WdaCI19AYeQJU-wHMseyO8MwA3Y2vX74W6-uaGtx16ie4UZyT0J9u_z5ozRaOkcletuzQF3XPJuvIC3QFZnh0RarHRQ9uhgRGTFY-SOgZF16Mm580wL_44tGXqKlVfK1oCR5hjSWKRs97uDG-mrG9o8fkAEYaPRS5PZouomFHIA15YLOLpGeLTCMKz7hfikySIsVxHbhytHzFOrzPczfcAo957Z4eJskIeHyYUVpMqdr_nDVKQJi05nZFmnf2dcmJVRcyS2QuOy9bNbr7WgUZbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec0b3d8249.mp4?token=YOO-Qwl31_fNRjlwyRdG_i7CBn6pDm9r7dth4QbXYdIuuBUShsADal_ZDWTWOQ0WdaCI19AYeQJU-wHMseyO8MwA3Y2vX74W6-uaGtx16ie4UZyT0J9u_z5ozRaOkcletuzQF3XPJuvIC3QFZnh0RarHRQ9uhgRGTFY-SOgZF16Mm580wL_44tGXqKlVfK1oCR5hjSWKRs97uDG-mrG9o8fkAEYaPRS5PZouomFHIA15YLOLpGeLTCMKz7hfikySIsVxHbhytHzFOrzPczfcAo957Z4eJskIeHyYUVpMqdr_nDVKQJi05nZFmnf2dcmJVRcyS2QuOy9bNbr7WgUZbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
الفت‌نسب رییس اتحادیه کسب و کارهای مجازی: خیال مردم از پلتفرم‌های بزرگ طلا آسوده باشد، نهادهای بزرگ نظارتی این پلتفرم‌ها را کنترل می‌کنند/ برخلاف بازار آفلاین و سنتی تاکنون یک شکایت برای تحویل طلای تقلبی در پلتفرم‌های طلا نداشتیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/683099" target="_blank">📅 17:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683097">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی بریتانیا: میزان عبور و مرور از تنگه هرمز حدود ۹۰ درصد کمتر از سطوح پیش از درگیری است
🔹
مسیر عمانی در تنگه هرمز پرخطرترین گذرگاه است و از ابتدای سال جاری تا ۶ اوت، ۷۴ حادثه گزارش شده.
🔹
کشتی‌ها به دلیل حملات و نگرانی‌های امنیتی مستمر، بیش از پیش به مسیر شمالی در تنگه هرمز روی می‌آورند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/683097" target="_blank">📅 17:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683096">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرمانده نیروی دریایی ارتش: دشمن اجازه نزدیک شدن به خاک ایران را ندارد
🔹
فعالیت فرودگاه بن‌گوریون برای روز دوم بدلیل اعتصاب کارکنان مختل شد.
🔹
قیمت هر هزار مترمکعب گاز در بازار اروپا برای نخستین بار از آغاز جنگ تاکنون، از مرز ۸۰۰ دلار عبور کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/683096" target="_blank">📅 17:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683095">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee96d3b3c.mp4?token=fowNsyg2gORorEoKhXrVXTGw0yKR6f9TyRyhGiPW2ZC1XR_ybkWdA4L677PZkMhvxgfeRxQfY3OPusRAxJxRYVjo_-GuIFx8AZhjpsx43PHtWNYj3pxoQHIq8OzeFZQDfLFTRdH5O8VeaE5jn_i1LHZPkNN9GiffY9Bcvb-Qr87d0odcEc6_u4cCm3Yga_lBpjBtmb7262ZzaaNrhTXF6vMMRfLTJGVBtHDsAoMKkO6M1GBNHvIOndCuPQDPcLY7Z1mCqbwNGP8WLO5fTRBFqC_6enoX9Vm9w5Dz8bzasjmkH1TZrP_AdMqTX61Nk2qtyRcHl_AKIsdjjHwPnDXINg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee96d3b3c.mp4?token=fowNsyg2gORorEoKhXrVXTGw0yKR6f9TyRyhGiPW2ZC1XR_ybkWdA4L677PZkMhvxgfeRxQfY3OPusRAxJxRYVjo_-GuIFx8AZhjpsx43PHtWNYj3pxoQHIq8OzeFZQDfLFTRdH5O8VeaE5jn_i1LHZPkNN9GiffY9Bcvb-Qr87d0odcEc6_u4cCm3Yga_lBpjBtmb7262ZzaaNrhTXF6vMMRfLTJGVBtHDsAoMKkO6M1GBNHvIOndCuPQDPcLY7Z1mCqbwNGP8WLO5fTRBFqC_6enoX9Vm9w5Dz8bzasjmkH1TZrP_AdMqTX61Nk2qtyRcHl_AKIsdjjHwPnDXINg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای که گفته می‌شود مرتبط با آسیب‌های وارده به پالایشگاه نفت جازان عربستان سعودی پس از حمله پهپادی یمن در ۱۸ اوت است
🔹
یک مخزن بزرگ ذخیره نفت هدف قرار گرفته و دچار آتش‌سوزی شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/683095" target="_blank">📅 17:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683094">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDd7ozM2DTBaRX2puQNoctWExhYoAmaI4qxuesof4lFC9d8_UW2Lpb8qkeO5VBIZ1rTZh1KRhRt-L-hzSh_7rzBori84PynSMcrXdJCtv2IGO5qwujFnAR6HufSi6lhlk6D3-Es901GHQP23GKDrqbyElUFcWRMwITPc3lU1mCtnlQMM8VnYMRvFw1cvYwNcNwR5E0Awu3A_79j1H_Cu45yy5jwW4F1bE_f_Qdq4UUBX4jeiqWIlHkDW5pq0kcqUgL2NEVYZmpgQ6P5526py33jrKJKz9WDUmVHQ0Z1ILEYbo1P_h2Ls0a7hi-TFjL-lnFdRwPb6k_ZHDlGzPgD4ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌼
بیعتی دوباره با صاحبِ زمان ( عج)
💚
به مناسبت سالروز آغاز امامت حضرت ولی‌عصر (عج)، در اجتماع بزرگ «مراسم تجدید بیعت با امام زمان (عج) و رهبر معظم انقلاب اسلامی»
▫️
با کلام
: حجت‌الاسلام و المسلمین حیدری کاشانی و علی‌اکبر رائفی‌پور
▫️
با شعر خوانی
: احمد بابایی
▫️
با حضور
:  سرکار خانم الهام چرخنده
و حسین حقیقی
▫️
با اجرای
: امیر مهدی باقری
📍
وعده ما: شنبه ۳۱ مردادماه، ساعت ۲۰
میدان شهدا، مشهد مقدس
🤍
بیایید در این شب عهد و انتظار، دست در دست هم، بیعتی دوباره با امام زمان (عج) کنیم...
@Heyate_gharar</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/683094" target="_blank">📅 17:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683093">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14bee6ddb.mp4?token=skfxXGyP5wBh-PNwCycsxKvjA6lZZs4zy26wuorodkgMBaoV_LjsVNuYuLPOtlmAGKY_drrSHFu_tuiNCjLg2VBRmEtVE8txkqAXtBVf5AVq7jdjd3MEXqEHO0t5PGbK4SzLuV3jJy8EK3WpnDMo7vdxuaB3Dhw7fDwPurMutzlJZWgq61nLqT9Qm6aZAPigZUcxpp5O18cWFcU5V0x2UgyD2E7u9w06E1DhmVuQSd_rPnZnkun5GJ4Ebkps4v5I-6OWW0MjidtnP_jZedb8TAaYvq23MdDL6Wp7AeCcRi010wBRdcEsidjT2TcU-zQwhaZ90sp_OmWXPgo4A7jWNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14bee6ddb.mp4?token=skfxXGyP5wBh-PNwCycsxKvjA6lZZs4zy26wuorodkgMBaoV_LjsVNuYuLPOtlmAGKY_drrSHFu_tuiNCjLg2VBRmEtVE8txkqAXtBVf5AVq7jdjd3MEXqEHO0t5PGbK4SzLuV3jJy8EK3WpnDMo7vdxuaB3Dhw7fDwPurMutzlJZWgq61nLqT9Qm6aZAPigZUcxpp5O18cWFcU5V0x2UgyD2E7u9w06E1DhmVuQSd_rPnZnkun5GJ4Ebkps4v5I-6OWW0MjidtnP_jZedb8TAaYvq23MdDL6Wp7AeCcRi010wBRdcEsidjT2TcU-zQwhaZ90sp_OmWXPgo4A7jWNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردبیر ساندی تایمز: ایران حتی راه فرار آبرومندانه هم به آمریکا نمی‌دهد و سطح مطالبات را بالاتر برده است
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/683093" target="_blank">📅 17:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683092">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Srgh3Q5HO444lZYvo7NJA5i0ax-m17yHN4vKomqxSAmHx2PeX74bJY8vCmYJCHPuE5YOIe6zZi_jZOmXsFOWpgx4GHm66FxIamcbyVPWdSXAN4P6DON4BGbSh6uLgzVOywJ-g29SnpQq1pAxtEsszEx1HzGe3nbqDHYXDOFJi0XrQx3ByXVyQc5FhFcItfSYx-Mtgo69oWAwE53sC5DHIdvwdsqmCFuWd7X4TWqgcAvAGo_UqopSecU-0JZAf3MbGvgmKQFAUpIQN5pbBcxRlALNMP3tzp7Zuk3nyLwBY9hQWnMUgLdY9ZA1y9kCgTSbtGgSA3lUQjbWDa-Tvlh75Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری بی‌نظیر از یوز ایرانی در خراسان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/683092" target="_blank">📅 17:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683088">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/169c3f70d5.mp4?token=STlXg9MRl8GY6F35kARJvYmVuiBv4LwZdL5nUcfZZqZ7xcWNuGD8E7Jq-ZV7ECIKP4riJAcV0PISM-Oa0u8fTFmPV-ylGG5W2XwVZpUPAiIZZQAUqN-jSRFWXaWsEltjVFeZ8D_nmYhkiueonnnpjZLP-CVQM8n8ocJXqIOjjQqL2QsCyg42PInBWUd_wqv1TIlUcOYzoyNTzqFRJrTFNRhPxywWaoXs27U2MJMXzKs9MAZPk2a3NqW2fUeUsApvS3DCi9WlhQnQyCidLcmxMaZbz59h8pj8QjoAYA8kVPANFCFJrLIKyRGLnEVLHVmogXa634ks5Jz1KJq3ZlpFYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/169c3f70d5.mp4?token=STlXg9MRl8GY6F35kARJvYmVuiBv4LwZdL5nUcfZZqZ7xcWNuGD8E7Jq-ZV7ECIKP4riJAcV0PISM-Oa0u8fTFmPV-ylGG5W2XwVZpUPAiIZZQAUqN-jSRFWXaWsEltjVFeZ8D_nmYhkiueonnnpjZLP-CVQM8n8ocJXqIOjjQqL2QsCyg42PInBWUd_wqv1TIlUcOYzoyNTzqFRJrTFNRhPxywWaoXs27U2MJMXzKs9MAZPk2a3NqW2fUeUsApvS3DCi9WlhQnQyCidLcmxMaZbz59h8pj8QjoAYA8kVPANFCFJrLIKyRGLnEVLHVmogXa634ks5Jz1KJq3ZlpFYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای خالی فروشی پلتفرم طلا چه بود؟
خالقی معاون پلیس فتا:
🔹
صحبت‌های من در مورد پلتفرم‌های طلا ناقص در رسانه‌ها منعکس شد. پلتفرمی که ۲۰۰ هزارکاربر داشت به مردم خالی فروشی نکرده بود و به میزان طلاهای فروخته شده نزد بانک کارگشایی طلای ذخیره شده داشت.
🔹
مشکل تعهد این پلتفرم به شبکه همکارانش در بازار سنتی بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/683088" target="_blank">📅 16:49 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683076">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AiYajdd_JNpPUJFnfkyBTXseKIqTbTRBDe65hrBAAsU-xzjSqq6402sTFt0vPXL5SXB35Pm5UjAPn37wFHMrsNQdvwD93ImqIb5eYx1XCwiQ406Ysujp2Hbl6ujv73BP3i4OVvCUIRPorOKTp5G4jO6JnnvyhUKIzQn2q99QaYlkq0BuEQJBD1D30l54aJ5Ouz6bTBF8ac5MZlFL3CKFxmtBI8E7PRrKQWavKhQqjV1syS9KyRO5R4IKRmeSeJ5p3CilHtIBbZ2g4sMSjBuP0xFOH7vqPvtxAR3is0hMqC8jyaYdtKnhdLjZbJCaNNu8rWfi0yPtICVxF9s2k_qqAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oC_DaWYIWEi6tj3xr_SREQAiTJAbpSVmJggeNHRHWtNOYW7MOLhE8X2yOcnzUIeEH2yb0SyrZ6DThlw4kL3-TG7uxf3LG5TRV_AG1qa2CajxKsVjtRG2hrITLcgTBP9tunpad4R38ez4LPTndxE3ZG8RIbZbvXUAdV9bYZJDC9d1HqIpw4yoDMwC0NxS9onlPy3I7zQquAXRYML_C5c3f8Q0qiiJ_u1RLLkC3BFH2La3Ino1LyEo6_yTTfdiWxfXsletCZfngBLwOSlz5AJYxnugVHxzPQ3FHDNvOMDgPTlBjWmt-rtlcHuUPdj_oR0GE1BrHTDm_3sY4owJK74IwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oBRK5Ow0VxuAowFE5HmSNpGQcUQVX04hfadeh039pPwqCR1yqpZuQDXUKMPJMA7P8RdI2OE3_BdGTXAn__QTM_FRuSyDGvlZEH_CI092AXVlOiE89FZEISulGK3EKjYa3t2ENLVUFwlerS8O86tf2tccocFQuWAeYuD3zDyZFzlNUgjadUXuhrh9ehQBD48AlkeqzLbI88n03jWPemkmmw45u8J6TTdsUGXYVcfTx-C_WOdX9I8LgqYSrKtzUxYjbT_08pIOrpYn3l61lqteNXKHuwre0pcsB3fdGSSESV5Y189WVbxQ3qwJuqtQbjGT2H4W-sKcPs7Spain8XF7Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nixVxYqkIL_07cXllQ-Y6pfePwWQAWHWSoJscu3DzE7ZZCrMbVdzphXWuj496rW2lVfvmQmCjYxjZLYeZYtUzdJJqDf40uBcIvjOOsrStOpoGrkmYtwINmmrRpEIkrHyeRj-8QgrgHOraKOHscRPymg7-T-1ul14-YirGXyB5Db9ycsGUrERkEwcoclnZT1XheDWD1se12K_mJDM5Z7uo6E6uQbmOF2ek0QXzQx3CjRAUh2jJTPi0T0YdTVEw3_5_pJoEn3u6acgd8KbdI9khLcPrrBHh5XEHLzo_M95MP-8VWKqkVcDnz1GgwI-yVKmo6UPN7PCEFfToBwlPiMnHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gV1rI3sgQ2eldB1XagNFdYLuWT1pusZwUoD3hbZgJbfnqDWjjiaUkTcQolIkRN34Ig0NmblTVHlgb-Jz_EpZHH9MWciV0-MowMdG1OmEpL-ic9Lcsi1fy24C1Gz-IfynjrK7S9EX_4vlcBftH2DkyMakQ6KUzY0aSnVyG-xmuvjCp-bVImFuILZuostJesecjiMSOvkNUZLKNS99kaWLx-1db3l7kvUQKmoooDa1lbzJUsyLTwNuYJJUnLWSieVe4gX_zhB1_GAO1HCdb0iZvCTzM4hhKLp7HtUSYD7tPfYEMIrIUiRxn051W4c7QdJeBt-FY9AqI5auFGQiUK0JvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bm6giIlIkXeVH2251isyrLJAAq4VrHnQozDx-NtGeQOXTAk2ET7z1YqaahhPT2gk6RXJN2f4aiCN3ItZFS8lfpv4BoQglGv7HRm03Phdie5BHHgjWGxaJnvmiC-paMa67kWSQLbA4P1SzLHkjHkFrSUHwL7oz8EWy1sbu8eSsShWYsNVgqoWHhLSTW0gkjU4tNjV1JirvET26Fo6RhHboPCralKFCTCZI2S5V2Owf5OPad6Mtrv_HIo5X9cCjkabEg8nK3EamkJiqRC5wRNVMIGQV1iUbn5wd0iMo9MKViyepzY7uI7TpF6JQDhIFl8N3aL76_vg08NIBPouCGwxzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/svSCqQp72NrKIi7j6ss8Ha9LzauLR2xe7aMM6O73bh_TalTzYgkcut28lmzppVUgBfuBjXq0WbJd8xreXhCKwcosU6C-y7Iz__fBLUrtSCAe3Y5DKRMd0SQ34KTBNsQq9Mo0-MLCy1c9STkeNcOmpzOb2g57xOxxiqVUQH8qeHZzLSuRxV1mT9gjmMisYTOF5ny0ZfmbONK75Oy59rxPyl5WENyIzZ7pMr5xhs7Slr0i7DD2Ciz1FytFNcWPcGixkYKm8QLRuI8dGh5_2zVcH2rnoaK0sfHZwjA_Y2clXnhpLDY32fsFEwSSHhdInC7Fu5nAVzHQ6S5XKk_JrqbS3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBLy1NPjtKM62NTmS-E_N5X3QTOClts6Lnxs-fMIZJV8Y6wuvZJUnKhQh7sS-Sid_x7OgPYpRsI-1jXNNS9dTNLk9t8njZNso4ILARehIYbAOYKnPzvTLP48eV_FwSB_0SZ4X_c6tg-X-6NyYQHeMLkAJamjgwdhPkADeWLxCvLEF_SJBfH9ZsQRMkHRKafy-h5FsnBdvJMLrOgx_2tjUbHlmiM4fScHphpsXYpVVC5iwi26wTQGA8CPEcSacwaCBtZ6Po7mzONKNVxzXdM4qOVTEQF0ziH2-CHbYDIzAHDl8CmXBhDNTEWjP-0NzVyqShliN0tQtATEi6O7XhmLYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0dLQd2tWdO9k4LNdugG5s2ANc7C7ZJ1_EQsjA-Rb3SM_JNrFpkbpM1M1TgoijI_95nnQPU2Y9hwqYuNzf56AYWdTBiQXzrteqe1pPtK7Sr2YzPeKeGFUAW2Ibi9kY7lnEnwMv23s8MPXwySCZH1qSRJy9Eju-3zlWWdT2s_MGtkOSKEZyVmijrA0kwbznXhsCujLUznm8snwYApG8oE1luWaWa44-SoifY0dUrBsPTZjbiRvftSTO2pWuY0YxMSsGujbIEFC7XfmrHJLVq5ZPdlm15AUt_y0GbWB68WLMPhAUW9tWBcjZxdBxiF2Prk7CER-7Cp8r9Vys5mxrjVoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Po_ZyPkytzQvC8qjn26BhuXDE-CwSLfh_LmGZHMPIz5BUYlzI8ZtxVrDnjcQLt-lKGPlxwdc6-We8vZbbX412LJY3xXeIxxuoIxn1tgvhfmQahNVEk5qxFqMYLTRWy7febmVdmzzyW7qi7lXZYevf3D-NjqyDCqaJ9xPHdGdjZ3b0DdbcATVpocj1ruKm2fXpbLoQ_cgMday6G18xR6Q2jhvWF9aL51Vffn2tiEGPozY2XdJ3OQRB9jXZvGyZWZybR3awqEr5Wdi1jmRJPR9x4yEju2gUpWKS3Agm_CHTz3RYhtKfKsNVRDkLNP2C3uK4BvLoupxGuj6znLgVqIyog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نیروهای مسلح یمن: حمله پهپادی به مواضع نیروهای سعودی
🔹
نیروهای مسلح یمن تصاویری از هدف قرار دادن تجمعات و تجهیزات متعلق به نیروهای سعودی با پهپاد «رجوم» در مأرب و ساحل غربی منتشر کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/683076" target="_blank">📅 16:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683071">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/axA04BHLYexMTejd4dTGrJn4sPWnssnSWv4AVkxHpWInf1ckC8aDPNsitpPuezKEwiTzf76ys_TAo_LOlBRW4RyS1e2ZsGrB_BI-xhohrEv1mfpLCk5VuOJl4G2ExL3lS_tOnS0w6lHS5_VLVybK7_2HEcOumhp3wX2XLyFRQ7KLPEeZPptfj5YIT-ePiRqXyBbR6K4gUVbv9gZAvcQrNfhx5KbhSEfC4DE74t-nTyY1ER82QKgGC1_Bjz1Dlp02iDFcX-oXhPABSMuK2yuXbcJIzg5bsqQ4punKRZIqncHdmM7wDE7QNU3zbyebk6oR1odqk8siEcyoV3ZGfpcODQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GuuO1ftqxVIdHuEvio-R8aQlAV4yXiiMe6KFDzU4izIT-zs2zfvumIAScwfW54zk3fHqgWf_wH50VlyoBIovWKKmmjJsaz2Xbo8wc0YUGiUXCdq-TKQ6JO1TqzEJ48zgD3tQ2C4oJ558Ih-d5IGBV2UJz15ENAgK7J5Kv2yf2GXmems2W8UfbLOdftSQVIH-0Zb0VbLC43t_kg4YYivtmidVzafJFuBNTrWyy6sjpIlrVeGu6kAW49U2qkb8EoW9g7MPImdjpI-_UEQmKAKzDUOHr7-YAHtxsPfTvD1FaeX9CZHaKY0r8A4BaiCbIy3QOHOhX1osnsDeFspisdaTOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dJ_xlJuDtmWfr2AavIBMFEEzRBilROU14V8aesozlLUZjJhxdIFJVwIOdtH3AkL-wMiBm9ms0rOVexnlpe_ZjrU1a8yjDEqId3CWNBkFVhSF6jmWtzwOOsXkXlfg7hDyoXlhUGfNB3cPR2zLfRPsgA72QY5HyzoEdYbY7Ti4pdVyGCW7vQ_09LiZjbqR6ed_OK9xKrAOVcLekmLP4PkY21ykof13sN9qzVZYbsOhVbD86OXTe1VVItEIJd45jx9J5CxM_vh75JHJCesTEO63aMHd-XtSoW3RIiAvcr63Py39ayLA10NGpkIXz6QV0s7C-VRaMoeCPRBestfqu1Xj1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BI4pAjkOb9SBNHmy1lsb_qAwx0s-WzN06JUUZTlHGQb_7TMBL7k8Yf3x-9vFgAFp3sMOFiTd9WpWW95mi3ve9N2rGdZ62rJB8NSbid6zP9Og1y9iE7UwyAtCmlLDzkW3Bn5MUNzWtQ8lzaDzoZP_dSUMujIsBlRTFGoHBpB3vr8F8G4pOubyu9VO3Sd47XOromoMANa3nTA3a_T5UxSkij3cbhkFsA6365B5vHJiWjSPXHJQGqSpdtndTliwJT183W1BilkC90Q1OSRNlvbRzaSFUXypDjCFCPeliFK2FU5YOgq7jTBRoSwWFiqMKFk4xwNCNIS0UNj0EZpZApYdXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
صندل عجیب شنل در فرش قرمز جنجال‌ساز شد
🔹
مارگارت کوالی در مراسم فیلم «The Dog Stars» در لندن، لباس مشکی ساده‌ای را با صندل‌های «Barefoot Sandals» از شنل ترکیب کرد؛ کفش‌هایی با طراحی متفاوت که ظاهر پا را شبیه حالت پابرهنه نشان می‌دهند.
🔹
انتخاب غیرمعمول کوالی توجه‌ها را به خود جلب کرد و بار دیگر بحث درباره مرز میان جسارت و انتخاب‌های عجیب در دنیای مد را داغ کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/683071" target="_blank">📅 16:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683070">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7e5c725d4.mp4?token=TD3vNKByoGNl92cgyUA09ES5b5eJzfFXAy10u-T_F92m7UzZW_KJZxrL6FOEwvQhChAP3jUl1ZmLlv8bwWyFMNShL3OxlZV_6AXI941exCfM7zn8GrIQfBdoHZNoXKFxccdfzRV4xky83a1tswJ9yihr6A45F1BkayQP75wfMip59QcR37wFIGz5sD_SIWEbmIuv1fG3Zh2lthmlxZREqtCKmNVkQaoUKQ1AWmkedUyT3AY-9zjZOZTE_8-etOF29hB-8_JhLPwTcm4nT1XmbZIzIVLVtOHQON6n-g1D3qPQN7RjowTnKmLenJV9Ft_1mfpdtXlZCe8TZtu8FKMIOiZAZSfcQ5sU369Nqnn9uI_ZyRY2X4eKc4fPu_Jvtc1xI88h98Wt1iZbBgdTuWWKqZ4dwxoRd1MfJE5F61JZUPzRUOQLC2i4O5LRX-50E-vA_1m9NUAh5qP76A5yDS4nJkBiyP26XeMtXf1edcBizAupyGd60J1BIc1ZH0YPd7-puomX_1SA68hw4t3aqu1upFJzE_0C-6BwDU8wx4LS-J3bpIXXTjePxtgmLu4p2aM4NTjb6JmPnAW_k9SfxZC0fU0foDmD3m5ZFqb_bDxcWg2wjqqd4e2eowQAdetruKTVsp4vZ0dcLKXemY3wTn5MNk6XRcPwkUJkaoNOFKGt4LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7e5c725d4.mp4?token=TD3vNKByoGNl92cgyUA09ES5b5eJzfFXAy10u-T_F92m7UzZW_KJZxrL6FOEwvQhChAP3jUl1ZmLlv8bwWyFMNShL3OxlZV_6AXI941exCfM7zn8GrIQfBdoHZNoXKFxccdfzRV4xky83a1tswJ9yihr6A45F1BkayQP75wfMip59QcR37wFIGz5sD_SIWEbmIuv1fG3Zh2lthmlxZREqtCKmNVkQaoUKQ1AWmkedUyT3AY-9zjZOZTE_8-etOF29hB-8_JhLPwTcm4nT1XmbZIzIVLVtOHQON6n-g1D3qPQN7RjowTnKmLenJV9Ft_1mfpdtXlZCe8TZtu8FKMIOiZAZSfcQ5sU369Nqnn9uI_ZyRY2X4eKc4fPu_Jvtc1xI88h98Wt1iZbBgdTuWWKqZ4dwxoRd1MfJE5F61JZUPzRUOQLC2i4O5LRX-50E-vA_1m9NUAh5qP76A5yDS4nJkBiyP26XeMtXf1edcBizAupyGd60J1BIc1ZH0YPd7-puomX_1SA68hw4t3aqu1upFJzE_0C-6BwDU8wx4LS-J3bpIXXTjePxtgmLu4p2aM4NTjb6JmPnAW_k9SfxZC0fU0foDmD3m5ZFqb_bDxcWg2wjqqd4e2eowQAdetruKTVsp4vZ0dcLKXemY3wTn5MNk6XRcPwkUJkaoNOFKGt4LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«موج‌سازی مجازی» یا عملیات فریب؟
🔹
در روزهای اخیر، برخی جریان‌های ضدانقلاب با فراخوان‌های به‌اصطلاح اجتماعی و خاکستری، تلاش کرده‌اند موج‌هایی را در فضای مجازی ایجاد کنند؛ فراخوان‌هایی که در میدان، مابه‌ازای قابل‌توجهی نداشته‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/683070" target="_blank">📅 16:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683066">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elyrk9VlE8HrSEbIDlUkMPw3pM3Y9FDzBNgBkCXzHe048i6W6m8wqTpYTrnXu2wX3VqnrkrYYL4LlUKxOc1WK5RF_MW5LVwkHCOkD0aEpw6_9wE_iPD3H8hZTQZSSE20ysDwGgUp8jDyZQNhmUwgdO2TM1o5cBmIQ3ypDbbaDyA6Epq4IcH_ayRz_i5TVmsx3uphhU9y1HDzzvzgXubgj_TQ2uXA-9j3OPtONTmNwR-ZvYkMPR4UTSdoPT_Ag2q_rafWYn1kS3GjLI6mBBrRkpG1l4LwGKqV22QI0azcCen27x0Py6DogbYA6uUDBPXuf3zp4B76-Yps9Q2eZZuhsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ممنوعیت واردات لوازم خانگی؛ ممنوعیت قانونی واردات، مسیر قاچاق کالا را هموار کرد
🔹
هاشمی نخل‌ابراهیمی، نماینده مردم هرمزگان: پیگیر رفع ممنوعیت واردات لوازم خانگی از مسیر ته‌لنجی و کولبری هستیم
🔹
سید عبدالکریم هاشمی نخل‌ابراهیمی، نماینده مردم هرمزگان و عضو هیئت‌رئیسه کمیسیون برنامه و بودجه مجلس، با انتقاد از تداوم ممنوعیت واردات چهار قلم لوازم خانگی، این سیاست را عامل افزایش قیمت‌ها، تقویت قاچاق، کاهش درآمدهای گمرکی و فشار بیشتر بر معیشت مردم دانست و گفت:
🔹
ممنوعیت قانونی واردات، مسیر قاچاق کالا را هموار کرد و سود آن به جیب قاچاقچیان رفت. تداوم ممنوعیت واردات نه‌تنها به هدف حمایت از تولید داخلی نرسیده، بلکه موجب افزایش قیمت‌ها، تقویت قاچاق و کاهش درآمدهای گمرکی دولت شده است.
🔹
اگر بخشی از واردات لوازم خانگی از مسیر قانونی مجاز شود، مبادلات رسمی مرزی می‌تواند جایگزین قاچاق شود و دولت نیز از محل تعرفه‌ها و حقوق گمرکی به درآمدهای پایدار دست پیدا کند.
🔹
پیگیر هستیم بخشی از نیاز جامعه از طریق ملوانی، ته‌لنجی، کولبری و مبادلات رسمی مرزی تأمین شود؛ اقدامی که هم به معیشت مردم و اشتغال مناطق جنوبی و مرزی کمک می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/683066" target="_blank">📅 15:49 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683063">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
استفاده از متانول در بنزین تولیدی ستاره خلیج فارس تایید شد؛ احتمال افزایش خوردگی در برخی قطعات خودروها
🔹
مدیرعامل شرکت نفت ستاره خلیج فارس استفاده از متانول در ترکیب بنزین این پالایشگاه را تایید کرد.
🔹
انجمن خودروسازان ایران پیش از این در نامه‌ای هشدار داده بود که استفاده از متانول در بنزین سیستم سوخت رسانی، باک، فیلتر و پمپ بنزین، لوله های فلزی، واشرها و قطعات پلاستیکی را دچار خوردگی شدید می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/683063" target="_blank">📅 15:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683062">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPM-nya2Bmw6ocNcRGMGW4JNvkLYw680OcN4_gpbNvMGSWl8O0t2is3K8uQYHIE40G0dGZEDv4WC7tbXi1KBTTJFjhVxfEYC29GYsQL-a_Wt3fFY8bXBJ7S1xL9iG3X5mgCDKbies3LR3cDtQOIp6wf6MMqzy1vuA6dxlG2mbewV_2ojpprq6boQnJsJCIP-dmvi5O1WEDqNlC65LuEOCWq4r-i06g4zxfKqqHuf3TrVjeQnPfgMH6cHlklPqXB_9kgSauUqWBy8HAT_HF8pSMja2ekmYU1jMfVblcRh26XpXrV8ucdgDJvsPkFX18R5DYc8OpS3PVcWJEHwx8UwHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشت ملانیا پس از غیبت مرموز یکماهه | مقامات امنیتی: او ترسیده بود
🔹
ملانیا ترامپ، روز پنجشنبه پس از بیش از یک ماه دوری از صحنه‌های عمومی، با جمله‌ای شوخ‌طبعانه در باغ رز کاخ سفید ظاهر شد و به گمانه‌زنی‌ها درباره غیبتش واکنش نشان داد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3239331</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/683062" target="_blank">📅 15:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683061">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae1568e3bc.mp4?token=hIYw1GpJrrQh6pzMSGiDzp44P9lusRkH36m1vgoH3naETQJmh2gAgUwmQmGBjnlU435pfxnm6yDIQ7E4t2SIL2OLAGLWn66JWFeWG8srDmyzKarIo-zx7OCLj0qjRSFBSRyWNN9SXFsYtOREuXutI16bH_OdD0v9Et6gEaqI9peN8aCcnE-DdWU0zsTZMn7fs5pBmYQ7rUqlifJXLG4uLl18SXFzKdp2W57m1LiJaaB0iWIrsfh9OX1Q4EpLr7k5EjOI6Q9gRr5VU_vB0C_B-3pDMW4cXD37bIqDvVRm1gLAGZQajkZIA46XA9oKntWymR7Wb6447Zv4NxK1OeeVUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae1568e3bc.mp4?token=hIYw1GpJrrQh6pzMSGiDzp44P9lusRkH36m1vgoH3naETQJmh2gAgUwmQmGBjnlU435pfxnm6yDIQ7E4t2SIL2OLAGLWn66JWFeWG8srDmyzKarIo-zx7OCLj0qjRSFBSRyWNN9SXFsYtOREuXutI16bH_OdD0v9Et6gEaqI9peN8aCcnE-DdWU0zsTZMn7fs5pBmYQ7rUqlifJXLG4uLl18SXFzKdp2W57m1LiJaaB0iWIrsfh9OX1Q4EpLr7k5EjOI6Q9gRr5VU_vB0C_B-3pDMW4cXD37bIqDvVRm1gLAGZQajkZIA46XA9oKntWymR7Wb6447Zv4NxK1OeeVUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ناکامی گروهک مسلح در ورود به مرزهای جنوب شرق کشور
سخنگوی پلیس:
♦️
مرزبانان هنگ مرزی سراوان مسیر نفوذ یک گروهک مسلح را مسدود کردند؛ در درگیری، یکی از عناصر گروهک به هلاکت رسید و سلاح و تجهیزات ارتباطی کشف شد.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/683061" target="_blank">📅 15:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683053">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/swPJ-UsQ-exS5vDlWhspWrF_G_-X0YVjT-Q0dBs0N_dDPlx0CBcLr_XXRYSU349BwXWPMc-jObdZAwWo--NUGTtUOKNnCYvNviGHK_t9_Eum0ZDRYi63SaG1exZS7pcrYFqJI1_IrHkjLaKfjqyhTgQ6mXBe_jBDd2Y4c1AHnhuhthPHy6NBr3JZir3Ar2TgqU23UzEnusgEyr0aplzkBssMYeQRE_0jBe66o4IN-1-05Dejvo0akn5A13uQR86nBFdt3jDoqtbcFt_Rk_YfiDfM08uGSp0r6oQjLmck7phDh8BuqoH3rzUpbNA2aSdSwLvWlzyt0vmSQbG80RZLpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FcjGbOqoZNOIkLMULcLeF6k9S6BwMLnuHyamjTHoLzqKnihqayQl0u-ho0btBQXKXADnV9iQOE5x0XLgjHSwF2L4h5l94cTyoSAk5mS6lODnEaefuqaiMipL9Y8u7-Bxd6MpWiw-wgH_hHBcd5P1BJabOYeILnnCDcACHMWmWqsOGt59WQGUTY8kKuelUvgmBMVS2mryeJyiIE6FEqHMU55piFX9OtUfwYV_LPTtLKTRqW-7FNAsP4fVEXUz4-FpI0sg1aLYPm-of9meQikPEi0qO0ozhzvDDhiElyeAKswuBk_Tv1EOKGM1K0Zx-ZQYlGbeFnCZsrIz5dL6rcxkLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R79bOFI_3xbcVnWb9Ng4xZNkvi4U_EMogskvME-xnmybwX4GYr89bjnwYzW70ijnms8mcBzTfZiJfcIc1LJlP_JF_b6inqCHxQr03x3Ntda21vi_-4dZ-B3bUbHsTDllABwt4YY2K_rQ9dfO6_-n5bgNl6Lf3NFjJngf1TvIoKtYTJJGeaa_ACUERE_pkwSCUdCjzXn-4euLgOQgRj3_bZM-V7Ll85C67K1ara4tl8gbak6DNZAU5LwASTzRTlFxE93sTqgyRoZFZE5jsMyKXhKdxUxqZ2tViWTMnwhY2SO09YCe47Ur7JSdAwVj9zNf-10t-nEy2tnZ_Ms4rrVpJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s7Z6Mp86ROT4UW80LF7lJRN6ChwwUweKodI3NuT3q2bYSCcE9wOWyQKk-N2vKZnL8pj_C5q9PNjsIYIl7kQa1eFjye7YRkwrlSe3rJYv8myf5il3mlGNEydf-BfvplMd0wWVjEk35w-eyrY8OWAKNYeJ3hfwEBnqKlP9rBFOE4jLvskNr4z03-pPaEnlebQSBKvCLncwpO_ME5P4T6ORL3DixNxDmth7TqnnVww0oTsXqrW4U5_5IPwoQaQ4n_aJHSEHSINF6OzZg_IS0PXKxZjApr8UEXEn6kI02N-2cVYIfTDJ-ErYo95sciGmA7Qdd8kLAzA50oFtGQWh709t8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qrr6sHqN2ORjlcLg6Uy91HH5kItBqfAmMXl7Cl09MQKtxx5H87Rvcq0oGZXWD7xutYlitEsOBDXedfs1vQfnGdWeHthOxWbb347ecL0oLrZxEK4RWkAaEiaPS44VLDRkfYtEPbF9CVBwzsa27udK59_1auumG98zywLCfMKxyDVr5D2qtcGCgBEdXfTAeE-AXIhRRuCVFkD9YvibYDYXidz0DiWAlUg6yQT910470wh7DnkJPpq5eyYLWowyCX-n7XEGbURRrx56uQ-bX6jyjT4GMiQX3kV2_h1H7txMJNz98wJbm0Bevu-oHiWIVYs4mbsZ_h1nIUJecy9JXLD6Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F1yFEZjryosuZTUwEm34rp1RmD4hLjI5ELGz4P6dxdc6QqYXCSUalsSojkD2e4Nqa_Aq6NMMKWULx1fNPV6EaJlsQ6OL-hqJWZJLtDikRoM1Ox3Dvh0IYHpp0PokjxdOyGLsJAHhOFVqnwkd9RjUEz_sQbWfuQRqlpp0kwihwWWuQmAc-6h76Pf59jguvR-t28rCIfLlHA5wb0cPNYH-bOVehmCnurC8mHDXBJoYYhDcykdmlr_sEBy9calUMPawBENLT1loYQ0r3PYqwK7NIfagLNLOonyz4U4vZ2Qx8l88e_vpyhNa2-FGoDk0JkCp1dnLyVVfYi6kuf3ro719xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XAwByUXtduete0IvWnPyh285zdsJodayYZZKqf030Isd5hDzkhUidVdBX6NFG1LCPTNyyTDoC58Q_EktNkSYqTC9oiKMzsMs1tu4dwhM_cDjwUtuQL52w8Lj917G2k0g5jDLcLi5ECUrukk-TsNfs3MmYxiyzFyLPD8a3YTH09OrUel71etOsAsL21QBkLrGq4Q7QKHvcKkHw2AO2HWGxeMlhxObUEjIK06RWcJ0wnff7zFO7owBSdcHwv_DTXN2-Y_IQ0M4Uj2dmxh55y_6xHRN1oy4tzaUSlbUxZypSEPTZMAlRFgsilrQdDNHG4UiS-DdW31GGEN6ooiQakySLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۷ مدل بستنی خانگی چوبی خوش‌رنگ و خوشمزه
😍
🍦
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/683053" target="_blank">📅 15:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683050">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMkPhBO3Cv0nLrFsmndrqdyjhqUkxxGc33DkloiHlRwO0JK6fxJQzb9wIWyhXeQi1tx-Yi4vTZMAkSAeDsYPe4WCLCmDw6s_PUcqgP4o0zIcR7WTfFSn1ft24poCy5JNSCR46lDhj6mGIfPccnWhCGRu9po1m1DTBUuiKYdi-3_SzC9M7NHauzwgotGAWkaipF8JLdplms10W2DHlyB5Uj8YsbhSeoU0zYblG5vsIiUNgvytgg6SW0SUVo4li7GHpQMeeby8NcIh4Ey9O9pd53gP3yTV4FPNgpRMYhHVbq8JKwZipY9erLFUcQCtRutN4yDQmOKsLX_jM0fitzBpvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QL3BQz30qojh1Jb_W_FQVNKVQ_R_oF-z1DuglR_9LPyPI29tGtZVRmScE-2C4Kywz-lw9_kHlRvbFa9r0AnBROdbsMywSctAWdEfaamxpx_6HVEPj1wUNBOSRG15ai5ZTu3RS-vX1CEB5g6bOemXsjCmoT-FjJwT_gKGGrIMgsGSTNF90WUQCpOc-WY8zmkABkBofcRnLBFLhWEvmKca6anXPN33sP7K4cP0uSahcAj18sS_DG2V1aqA3wvU4u9txHlfEb3ui2jf9REmVXPuA_A1x0iBemhq-JNV5wIMFf7sGP48O_nL726STXc1TA8lr1tLaKn0PcPN4rCfSfeF0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dVbS5vKnpXn6XXVsapZID8_W8bNWYhZpg7BajvAJpNOxcYzt2sp5XHptrifVYw6xAqYvij_12LDElHBTypmY-sLfFX5fFAv1eeXrFLLJ-B2sPyk9TLzxoBYjSjb16nPmtWYbv-gdVTywLTJp9Z4bB6ey_dskEQ07lfIhHtaq2yX9D0ykAMKluZ2HHIB9ORPYt6rYOhknssIWqAU-L-aCX16nmfb-0MMjmtbtgFtHhN5Ic64-u63AI8CXtn2xhUzTLt7v-Dy7-so4DyV4_HuCC5vHFFiDQa31RdZVlawOr0vaYAUaBbU_AoEjvfHDsYPARpY9lvBQ-fAooQjD3UanNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
بستن شیر آب در زمان‌های غیرضروری، گامی ساده اما مؤثر در حفظ منابع ملی و مسئولیت‌پذیری همگانی است.
🔸
الوفوری را دنبال کنید
👇
#همه_باهم_برای_ایران
@Alo_fori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/683050" target="_blank">📅 15:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683047">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
نرخ غذای دانشجویی در دانشگاه علوم پزشکی ایران اعلام شد
🔹
طبق اعلام امور دانشجویی، قیمت وعده‌های غذایی افزایش یافت؛ صبحانه ۶۰ هزار ریال، ناهار ۱۳۰ هزار ریال و شام ۹۰ هزار ریال شد.
🔹
برای دانشجویان بین‌الملل نیز هزینه وعده‌ها به‌مراتب بیشتر تعیین شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/683047" target="_blank">📅 14:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683043">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fb760beea.mp4?token=QBe9i63-Ag2L9p8rmnQ5GNRKZxGM96pWHxbYFxdUvfFN2iRIblIeDhCQkjih0BX8CWDhmTccRTaVAuK6C1-FMpTg9Bi4V8ji0SjHkYq0249y27FZyTP3nUz_WRN8KP-VinUZs-__ztMPav0lUx_OY0g3edPZyu0BDte75Eje5_IKRwTId_PDKErt8UPW_ZmmmznKpg6KVcMEPrzfjc2Y_NN3kQ_UqzPIGN6AFKCR4a9sEJHOTWqNqvSpnVsr9Cd3YNM4IuQUBqT0zeLmoMwlTsYlLge5ECL96V4FZtZWsIfZhhnTlYXrLSic2dxg2YsXCSRSQJBJ7Ef5QR4briTOqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fb760beea.mp4?token=QBe9i63-Ag2L9p8rmnQ5GNRKZxGM96pWHxbYFxdUvfFN2iRIblIeDhCQkjih0BX8CWDhmTccRTaVAuK6C1-FMpTg9Bi4V8ji0SjHkYq0249y27FZyTP3nUz_WRN8KP-VinUZs-__ztMPav0lUx_OY0g3edPZyu0BDte75Eje5_IKRwTId_PDKErt8UPW_ZmmmznKpg6KVcMEPrzfjc2Y_NN3kQ_UqzPIGN6AFKCR4a9sEJHOTWqNqvSpnVsr9Cd3YNM4IuQUBqT0zeLmoMwlTsYlLge5ECL96V4FZtZWsIfZhhnTlYXrLSic2dxg2YsXCSRSQJBJ7Ef5QR4briTOqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شغل عجیب و ترسناک یک زن در فارس؛ کمک‌رسان چوپان‌ها در دل طبیعت
🔹
یکی از عجیب‌ترین، ترسناک‌ترین و هیجان انگیزترین مشاغل در ایران مربوط به این خانم است که در استان فارس زندگی می‌کند و به چوپان‌ها کمک می‌کند.
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/683043" target="_blank">📅 14:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683042">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_q-eZ3nepb8_Jx2azDasQAmupz8oLO0prDyUYbqPeO8t5C31OxhpH6_bUC4QE6xkENCENHKiUPJ34w-eZqwyfSQ4Bhifl8Fz0zl24TinotfLLodIYoZ5uHzI_7ufaoN4Y0Klb7MRu_mlUHpu2XLDQ0Ux05eiSs-JLzeoHJ7FznX9j1fGN_mSNTnSpN2X0BmKORokKbvRif8lbQxEztFS9t88bbE5JoMqn3goh5y4nC9lZA9_91INhxEyYZTJu-ZFafnBLuXk_9Ty6l2yz_hl6UegmGvPzKZscFaCEyEGAfrVovRc6hh8TpATjiCsjM0m0HFkBJLHfaYx2Xa_RYsow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقدیر معاون اول رئیس‌جمهور از خدمات سازمان راهداری و حمل‌ونقل جاده‌ای در اربعین حسینی
🔹
معاون اول رئیس‌جمهور با انتشار پیامی، از تلاش‌های بی‌وقفه و مدیریت موفق سازمان راهداری و حمل‌ونقل جاده‌ای در ساماندهی مراسم اربعین حسینی سال جاری قدردانی کرد.
🔹
محمدرضا عارف از حماسه اربعین به عنوان عظیم‌ترین همایش وحدت‌آفرین امت اسلامی در پهنه گیتی یاد کرد و گفت: این راهپیمایی عظیم مقارن با رشادت‌های ملت ایران شد که در جنگ نابرابر ۴۰ روزه با الهام از حماسه عاشورا، حماسه دیگری را آفریدند.
🔹
وی یاد رهبر شهید انقلاب اسلامی که عمر بابرکت خویش را در مسیر عزت اسلام و مسلمین سپری کرده و همواره بر پاس‌داشت شعائر حسینی و عظمت‌بخشی به حماسه اربعین تاکید می‌ورزید را گرامی داشت.
🔹
عارف از تلاش‌های بی‌وقفه و رویکرد مسئولانه سازمان راهداری و حمل‌ونقل جاده‌ای در ساماندهی باشکوه‌تر مراسم اربعین حسینی سال جاری، مدیریت مدبرانه در مواجهه با چالش‌های اجرایی و ارائه راهکارهای اثربخش و ایفای نقش محوری و ماندگار در اعتلای سطح کیفی و کمی این رویداد عظیم قدردانی کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/683042" target="_blank">📅 14:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683041">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81ce609344.mp4?token=TdnYT7JBRr-pa4SShg_m69UvK9oEdGcCYnbaX5YtsjoCItwPvMfO7ggFxLYYo7gkOlDJybs33KwRHLzQqTCUBZ_9h_yDTO7nMMiaGbaP8UG13Q3Yf6diWAFsooxX6WVWydEVyIJwm9Qc1k6ka16EoiIQebvzVJVEZlqGLWyEK4hRmoom5OE7P6JM28uSecwEmQsBuB7vTW76zDARUU6DzX1yOqdWxn5EDmoPkzh0_kwcDtJr5aLvYtusff8AVu71CNQEWEMRrnfzevHMtQQVK2brMZSIDFaJg5nMpH0nMearHFez46oBaPVKlP6dRxJ5Q5VDbKjomnlOZOTCyG4j0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81ce609344.mp4?token=TdnYT7JBRr-pa4SShg_m69UvK9oEdGcCYnbaX5YtsjoCItwPvMfO7ggFxLYYo7gkOlDJybs33KwRHLzQqTCUBZ_9h_yDTO7nMMiaGbaP8UG13Q3Yf6diWAFsooxX6WVWydEVyIJwm9Qc1k6ka16EoiIQebvzVJVEZlqGLWyEK4hRmoom5OE7P6JM28uSecwEmQsBuB7vTW76zDARUU6DzX1yOqdWxn5EDmoPkzh0_kwcDtJr5aLvYtusff8AVu71CNQEWEMRrnfzevHMtQQVK2brMZSIDFaJg5nMpH0nMearHFez46oBaPVKlP6dRxJ5Q5VDbKjomnlOZOTCyG4j0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بحران سوئز؛ کانالی که آغاز پایان امپراتوری بریتانیا را رقم زد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/683041" target="_blank">📅 14:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683040">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeMM0AB2UJxvGnLOyukSgZ6XvAiYcEMeUXzL3w1xMtuYhS68wh6AYyZ6u28GrEqaN4aClI-DHSQHd1QuRA4XXeBs8S-iVj0eGAjs0I9jEFqtfYyLfHkn0p-HuGCuBaFvRTuamnZuqgkxglBD5rN95f0mzP_Po4ynmsS3FlQZQGBQWM06rD4WWyKi597F9G5WVu6bomkmaIFGw-JRQOLKI5pdDm_3WWR7PvWfQaq6IBEWJPivwKhqjPD_ioxCxj_XrkKphZ9bgPZx22062_xI4MtaPJ7CggEBujfloHXA5riWwfdOuPcIJH9X48F7EGSqFLOH1zTNaoDVBjfs0ONxwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توصیه تاجگردون به پزشکیان درباره «بنزین»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/683040" target="_blank">📅 14:12 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683038">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30d8e0ebb3.mp4?token=jw4If06s9O_s5dfNVF575sa0tBUUA2iLLJasNxpMRNemvuzHS45oB-Gxt4fjigoqLod6c5nfo8ky-0iU_WhbTeb_3OJJ0HBZGDqkQmX7-TVn3xWu7ZYkwcMbFlc3-I2WJZx3hRf0EZefhqDnpidNhQ3O4P_Nnw6ElzwCdaYHzYE3eL9g5U0o5ifu85tjUoMrKAEjewJRBUKDUwB3oj-lTmb11Ock0Jm7nVwot_rFXr5nBcRZalmtlT8EebHhdu-wsD5FkN3YL2cHM5RPbuOmiqrFbABzBvydpW_CWgB3eWwtSrPHb-RMi2vqfXMXXRIZUbuH3I-DteUQH4GXpKlxNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30d8e0ebb3.mp4?token=jw4If06s9O_s5dfNVF575sa0tBUUA2iLLJasNxpMRNemvuzHS45oB-Gxt4fjigoqLod6c5nfo8ky-0iU_WhbTeb_3OJJ0HBZGDqkQmX7-TVn3xWu7ZYkwcMbFlc3-I2WJZx3hRf0EZefhqDnpidNhQ3O4P_Nnw6ElzwCdaYHzYE3eL9g5U0o5ifu85tjUoMrKAEjewJRBUKDUwB3oj-lTmb11Ock0Jm7nVwot_rFXr5nBcRZalmtlT8EebHhdu-wsD5FkN3YL2cHM5RPbuOmiqrFbABzBvydpW_CWgB3eWwtSrPHb-RMi2vqfXMXXRIZUbuH3I-DteUQH4GXpKlxNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهاجران در دبی به خیابان آمدند؛ اعتراض به پایان اقامت‌ها و اخراج‌ها
🔹
نیروهای مهاجر در دبی در اعتراض به اخراج و عدم تمدید اقامت به خیابان‌ها آمدند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/683038" target="_blank">📅 14:08 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683037">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxXu4Zi6HgEwkltFg8kaEIUatgV5cRVtfDttX0m8YyxnvDNxSbPVfMaQgIYXoQTBehJAMqvdtLMRMgp44sCBjw7zPNEFr6KfyaOCecUWf2vCulomiu8NXlxPlPBGa8StpNZ7p7KUboAHtT6-HTXlDip935yv2aOSofoAWiamjlIbVrdgWweDugFVJCiNbFjFzM3gA9TrTDXnXDt1YhW4BKrkWpZ6wznkE1VYTB0dmjoucQyvgV9zbQjJCKWXt_Ozf30hBD9jV2SXlQltkmX0qeA7Lz6yE7KG7mkbQnJibtktm5XsrL4uc3RAyKxIydQ6UdhWgljWztiZJ_zhTv3Gog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: جنگ باید در یک مقطع به پایان برسد، بهتر است امروز که در قدرت و عزت هستیم و تمام دنیا به پیروزی ما اذعان دارند جنگ را پایان دهیم
🔹
عده‌ای خارج از گود نشسته‌اند چون نمی‌دانند دولت در چه شرایطی است، بی‌محابا اظهارنظر و تحلیل می‌کنند، هیچ رنج و سختی هم به آنها نرسیده و بعد هم دم از گرانی می‌زنند
🔹
انتقاد از مشکلات تورم و مسائل ناشی از جنگ با شعار‌های برخی همخوانی ندارد./ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/683037" target="_blank">📅 13:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683036">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835c394f11.mp4?token=lFSzgESBeACOfRd_79GlNupxnk2wQDTywmsSYzKoLXpnAJqlTlSnKBqZ9uXSkNlC2FNUmjam8uXkeOLwl7givhCxHqtvb2PN_sGhRRLXuQ7o8_YqQ1s7M1TenhTZDlc6Miarolc0NpjyKInOnrjMIsx6nuRXFOoX_EHNHJ2j9kPh8CyjqUPm0SW5N_vZPXhcB5ghTT4zFENli85bOGZoCGxd6MYqNuaWA629t5IBJcbDrdQ-s02-YbCYc3U-4Wqf7ywF6fSqgICPfuawSvCCQxkVhQPq9HJiKt6-z84Wb7EJs4W0GjUPorwvgAGtivF6DmTN60Ur10Jeg9INnBKXEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835c394f11.mp4?token=lFSzgESBeACOfRd_79GlNupxnk2wQDTywmsSYzKoLXpnAJqlTlSnKBqZ9uXSkNlC2FNUmjam8uXkeOLwl7givhCxHqtvb2PN_sGhRRLXuQ7o8_YqQ1s7M1TenhTZDlc6Miarolc0NpjyKInOnrjMIsx6nuRXFOoX_EHNHJ2j9kPh8CyjqUPm0SW5N_vZPXhcB5ghTT4zFENli85bOGZoCGxd6MYqNuaWA629t5IBJcbDrdQ-s02-YbCYc3U-4Wqf7ywF6fSqgICPfuawSvCCQxkVhQPq9HJiKt6-z84Wb7EJs4W0GjUPorwvgAGtivF6DmTN60Ur10Jeg9INnBKXEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ابرهای خونی شهر گالراس کلمبیا را چند روز پس از زلزله مرگبار ۷.۴ ریشتری، به وحشت انداخت
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/683036" target="_blank">📅 13:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683033">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53e1bd7446.mp4?token=oJPd26dJRRZPMDg0xcQ6GFgrtp3zJ6hq0m6ZaKYnSx54PKgvxK8WE0HWjw0QajF8L0J_H5M4HDWJYjh-mxmDbFBPxdbFfqgS4lL_uOPxn-2fKe9GOLbn-dTkAXsE5lJRWZ_BS2_mC-G7nHtmmrXnWl1eaGidSL5ea4dD_iFHIgdhxqrwn5GQaq6Lncl7aEqJzgJFp-nywrN03vtN2LTrVxBs1JBji1SJDHqmMT5H4LUa7x9xqAYigVph6qGpemZQT20VolDUr_1eZR5ONUXFvlozugLSlWqmfYN4HcWYbmBf6Vl_NGu-DT2ZRDwDEVBmUu2E74zfxh2p8Iohfs8buQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53e1bd7446.mp4?token=oJPd26dJRRZPMDg0xcQ6GFgrtp3zJ6hq0m6ZaKYnSx54PKgvxK8WE0HWjw0QajF8L0J_H5M4HDWJYjh-mxmDbFBPxdbFfqgS4lL_uOPxn-2fKe9GOLbn-dTkAXsE5lJRWZ_BS2_mC-G7nHtmmrXnWl1eaGidSL5ea4dD_iFHIgdhxqrwn5GQaq6Lncl7aEqJzgJFp-nywrN03vtN2LTrVxBs1JBji1SJDHqmMT5H4LUa7x9xqAYigVph6qGpemZQT20VolDUr_1eZR5ONUXFvlozugLSlWqmfYN4HcWYbmBf6Vl_NGu-DT2ZRDwDEVBmUu2E74zfxh2p8Iohfs8buQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات «سوپرمن» رکورد سریع‌ترین انسان جهان را هم شکست!
🔹
شرکت رباتیک Unitree از یک ربات انسان‌نما به نام سوپرمن رونمایی کرده که موفق شد رکورد سرعت دونده سرشناس اوسین بولت را بشکند. این ربات فقط یک مشکل کوچک دارد، اینکه هنوز نمیداند چگونه ترمز کنه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/683033" target="_blank">📅 13:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683032">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71b778864c.mp4?token=pnsuQd43HFOjqsrCXbQfbG3SoRIQckopNLVsaDYpfxXxfcnfayWpynsPlU2gmfxbpbluZoLN-hXV1KjZzshrUXi9UmWig8mHXNz3oU0LSvJTkK1kHUt-w80oKhl2cnMazjYaickc0Y3vGbpb4eb2V6cbqMDp4OTrzlawnFSXDmV2UkHacUg_lTeMXIXFWB_341BdGdxKNs2-2gQPJQaZEKoVILSrtBCYCeYbSCn6AVTvVG7oFk3FGvHYA2nEu6phgIdDftGKy3mlDnEutB68qIddqu2b2x4TZHExwtQMwWm_dZGH1ItKZwrdY2IItjyUneui9gljGq7oWrVPh1jGag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71b778864c.mp4?token=pnsuQd43HFOjqsrCXbQfbG3SoRIQckopNLVsaDYpfxXxfcnfayWpynsPlU2gmfxbpbluZoLN-hXV1KjZzshrUXi9UmWig8mHXNz3oU0LSvJTkK1kHUt-w80oKhl2cnMazjYaickc0Y3vGbpb4eb2V6cbqMDp4OTrzlawnFSXDmV2UkHacUg_lTeMXIXFWB_341BdGdxKNs2-2gQPJQaZEKoVILSrtBCYCeYbSCn6AVTvVG7oFk3FGvHYA2nEu6phgIdDftGKy3mlDnEutB68qIddqu2b2x4TZHExwtQMwWm_dZGH1ItKZwrdY2IItjyUneui9gljGq7oWrVPh1jGag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ما ریشه در این خاکیم...
🇮🇷
❤️
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/683032" target="_blank">📅 13:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683030">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRsI9dmsMQDIxd5oJm4ZOfWfHszSK3VdB5XB-eQTDXcJKERVyBHEoNNJ4L0MrhUfxIoHrVXrhKiC1mKpG7gbrbS1kaKVcFHRjJuZIOiLA1stJCeYuJrU9wedEfyDOyIJ363_ZOCiDV8ZkF40Ol5QvppR2Xn8-kP5vgAaA28zjmI7Uh9owt29CfwHGKMvjox7UuRLsy_6fLuLcxUHOPSv1OwbpoXsiYtn41rx1cWt5eRsbOq1K-qhfHPU9bEcESi4SVdZPGTUN0jHffdHEe5_63Q2qcabQJFnkSpPgyqlleCtw1AoebWStHxSKgA_w0GomfvtC9WCNnnPnvQtL6UIzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اقدام گزینشی شهرداری اسلامشهر در تخریب باغات تهران!
🔹
در اقدامی عجیب و در سایه عدم وجود نظارت، شهرداری اسلامشهر اقدام به تخریب گزینشی برخی باغات جنوب غرب تهران کرده است.
🔹
این اقدام به تخریب، در پی ممانعت از پرداخت رشوه درخواستی از سوی برخی اکیپ‌های شهرداری اسلامشهر صورت گرفته و همین امر موجب شده تا به صورت شبانه، باغات برخی شهروندان تهرانی مورد تخریب قرار گیرد!
🔹
این در حالی است که شهرداری اسلامشهر   با ورود غیرمجاز، این اقدام را در حریم شهری شهرداری تهران در منطقه ۱۸ انجام داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/683030" target="_blank">📅 13:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683028">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OexPqmF3F1gyLiCySNifENxRLGYv1je0hVK2ZyzFaPbtktM7vTgcRo4mHdy_aOlvGTnAMDRRGGVT11h3SzFds6k1pIlycNRE38eDSja1i5uTQHt9kL18jo34LKvluhrNUZNP3jCmFySCEvNCVudLs7FNk3iW_suSrFlqt76evt-si3Hv_FrFnxjNQ2PCA_1qK9R2w5rmKQ_XAPEJzbTe53R36idwmVLX5DjWzjDv4TgsHh-ZEJgCAP0Mg755bHREsnvwgwfAm-ImXZ0-V2kyEjkgIUOZaUS1m9tPpf6mvK8pyrWV1zZoUgYrKCozECk8k9ogwM6OXhRrWLHOEGunlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ فرضی ترکیه و اسرائیل چگونه خواهد بود/ مهم‌ترین سلاح‌های آنکارا و تل‌آویو/ خطرناک‌ترین سلاح هر کدام چیست؟
🔹
اگرچه جنگ ترکیه و اسرائیل هنوز به واقعیت بدل نشده و بعید هم است که به این زودی ها به واقعیت بدل شود، اما بد نیست به مقایسه قدرت نظامی این دو بپردازیم.
گزارش خبرفوری دراین‌باره را بخوانید
👇
khabarfoori.com/fa/tiny/news-3238628</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/683028" target="_blank">📅 13:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683027">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83339bd471.mp4?token=lZWE_Ic-lvDQppPy2ROf0pN04kK_4ZfciNzamqooOMn5zto6dWh3X_1ZooD9u3FgFh_2LXVqCrZuRDC-jtxdIWMUun6EvYY6KPa8n12OtXZUi5ff3bC5LG39EYrYTGKbhzrJgy7qO_moA56JPRRhH7RNDwQ0eOo4naQAcjiOzbpDp1sd9gK06Wk_Kr5KlFEzljm44eVkI9ZV9QsewBvLzgQ_HDFyLstMgGgGIJxLATueikVGlZIpR8v3snF_Hn1BFCqyY_3vlQoygYu-9ITs0EVRYhAQTaCbo4My4eRM2kzzeg1MmrWNbEaoSkbHNpkL5oowlCQnftKK3yDZL5mbGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83339bd471.mp4?token=lZWE_Ic-lvDQppPy2ROf0pN04kK_4ZfciNzamqooOMn5zto6dWh3X_1ZooD9u3FgFh_2LXVqCrZuRDC-jtxdIWMUun6EvYY6KPa8n12OtXZUi5ff3bC5LG39EYrYTGKbhzrJgy7qO_moA56JPRRhH7RNDwQ0eOo4naQAcjiOzbpDp1sd9gK06Wk_Kr5KlFEzljm44eVkI9ZV9QsewBvLzgQ_HDFyLstMgGgGIJxLATueikVGlZIpR8v3snF_Hn1BFCqyY_3vlQoygYu-9ITs0EVRYhAQTaCbo4My4eRM2kzzeg1MmrWNbEaoSkbHNpkL5oowlCQnftKK3yDZL5mbGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس حضرت کی قراره بیان؟</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/683027" target="_blank">📅 13:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683026">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/309bcedc5b.mp4?token=T-cGWtG7Q_rIlBr910P2W2kYQC25RvjiccJ3tPxs7p1DsbtHQtvKyf252MRATqWqX18gR9IW4WQS__x2HCVSMD9t3bpiFNAjrgzsCr_iAB4e_gbIa0j37EXkquEv_5zVK15NaOSzUoH-L5-iiyUAoBlzAXN7kTRXNG3LzjS9MdP3DT0BR6V8ayDbMHdv8jAneXWPHLZoPgbiT06I_v8B1IoOik9cXjQmIwv72pZMpqC9SqD4_qRE83JhYgrZrOBoY0wEW4rfXSKw74-l1U-K8xVPkf-kfKhkRcSgXzQrOzlZQ_bvJj5YbkVU4WOJ6nR8s8duCv8HSuHpy6IdmfOanENkECtVcvq_aEYW9pZ7bvxs4FfQFuZ7REIPmnEwCvtnDmNgObdRRZoZFb10LWJ_XUI1yj07hzcVi8Fj5--t0HgN7HRQrGPRajE3geCQZfiC2rzHGu2cWnR4YvAZQl5GfWxs4u3jbqWfxBCnCThLvsxMPchR7s6JrELYTn7oHpf7Z9rc2GViaiQx1m0UemnJMEVnWWnp5aqk9xKdkghce-YRksRl5RPHCzdp7Mq4_kzkp2y_gIJNMOLnwiHXGUPTCfDxSmTXQ5APkCvIMdFLleMQHeCPrVWdZH7Yh6ZsmpVu6zIjooRF1zQAegYj4dumHrghoRKrrVBC6RvSID0I6Xc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/309bcedc5b.mp4?token=T-cGWtG7Q_rIlBr910P2W2kYQC25RvjiccJ3tPxs7p1DsbtHQtvKyf252MRATqWqX18gR9IW4WQS__x2HCVSMD9t3bpiFNAjrgzsCr_iAB4e_gbIa0j37EXkquEv_5zVK15NaOSzUoH-L5-iiyUAoBlzAXN7kTRXNG3LzjS9MdP3DT0BR6V8ayDbMHdv8jAneXWPHLZoPgbiT06I_v8B1IoOik9cXjQmIwv72pZMpqC9SqD4_qRE83JhYgrZrOBoY0wEW4rfXSKw74-l1U-K8xVPkf-kfKhkRcSgXzQrOzlZQ_bvJj5YbkVU4WOJ6nR8s8duCv8HSuHpy6IdmfOanENkECtVcvq_aEYW9pZ7bvxs4FfQFuZ7REIPmnEwCvtnDmNgObdRRZoZFb10LWJ_XUI1yj07hzcVi8Fj5--t0HgN7HRQrGPRajE3geCQZfiC2rzHGu2cWnR4YvAZQl5GfWxs4u3jbqWfxBCnCThLvsxMPchR7s6JrELYTn7oHpf7Z9rc2GViaiQx1m0UemnJMEVnWWnp5aqk9xKdkghce-YRksRl5RPHCzdp7Mq4_kzkp2y_gIJNMOLnwiHXGUPTCfDxSmTXQ5APkCvIMdFLleMQHeCPrVWdZH7Yh6ZsmpVu6zIjooRF1zQAegYj4dumHrghoRKrrVBC6RvSID0I6Xc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳۰ لغت کاربردی زبان انگلیسی در آشپزخانه
✨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/683026" target="_blank">📅 12:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683025">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYCUCWKzZmBw7Fd-55ZMot1-IRSP37_LOb9yb6f3TsyVW8ZGlWK-L1pdA4ibG_S--f4jh59Wc59Krrt6HIQ6O0c7DkrjHFya8qnBwKgq0zJ5d481_3EZ4_muZwj_ht8oCj-kAUzvUVmF_2gFU10YRDKWloYAZeuranUMWjI7VG1FOVBwnuK4TDTGqhoqa839Ft9utJtDvdHfmgiS8R4flIEWUG8FcPsMjGPcSQAxogePQpadrmbn-Jp9MHdwCaYc2EB673jgkEA4GfTVaIRi2mu8uMTaC9vsXy7sn0-LENOLSw4virHqBCA4CZke6AWhJ7T6lJl71bwYlf_aOVxurw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسارت به ۱۰۰ هواپیمای غیرنظامی در جریان جنگ
🔹
حدود ۱۰۰ فروند هواپیمای غیرنظامی در جریان جنگ آسیب دیدند که تنها ۸ فروند از هواپیماهای عملیاتی به‌طور کامل منهدم شدند.
🔹
حدود ۱۴۰ فروند شناور خصوصی غیرنظامی شامل شناورهای باری و مسافری محلی نیز در جریان جنگ آسیب دیدند.
@amarfact</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/683025" target="_blank">📅 12:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683020">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SlEmdc_Kk2n8fmp7uLOfo-CPrbmQhkuo1x7X7HLWhWGlSNotS2cbSF6ZG5i0XXeQoyOjPN1Tw6ev66uHN3OWq8gPOnazjC7cOhzfc6zd24Y5JQU2wVNF6SVJWnEa6inLkdnM97WejvMjfr4m0cpn-AqEfzhpj8sVDXHS-_wrN4HJ4SIbTpdLSUAJskPD4Jl_-uoxqKaNy2CVCsuelozWbSu45Mp7SzY88ZksCccGLQedOBvYjcmqeRvk_aMJIRkPKTTWZY6jr9h5ZkMcXZOluYlXsvBMBQbvbQYHLPMRiTAFkKih9kpY7ICEvYhxUrhL7UX389cOlW2inA4JiY64gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K--CQOQX3yA3seY2YDe9FqvR9pTM9XDtNNVngW1ZLc7FEnZ2QccKdit4Ro5dFUAH7cZe2Ei65abtPK65Qfm3qc5NSAT-nj-oyt8FGYrbNYJO7MV_feSnRdaQfbX6zXujtfKVvczxB5MaghlxPKgWAwYOW_13wYNTsIcOXTHG1J4a6hONs1Dhx0x2UeG6gMpbiwJDQ4lUXV-BxyadUj8TFKe5kYiBy3QZtMQnwuIT-Zq6Qk5tgbegj8ByPCeV_3iv54fGQ7jjnmQ4nRRf6fG506yJ7LNVDcI7lzwNlXzCewJAdfcWL9YRc7Ob_N3Z9d0wB1D1gnpFTT_oeQ7aJr7BUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZfiJCSAPMolXsR4Dys-PIx474BMG6_rRwde6C8hnOIxhDI4OzQrXOD2yNjetAcZPbmsIxkEx_o3NogpWOs7pqi8PtTcit33QxbGcG_-rn_SN0r6LODyn6xlDH0K_POkd3-E0IyUtWPn8GawqTcFmy5cdjtkUTZ_bZlV-7vgGyedJ8I_pAOH6QvKCW70F_tPCTFsd_PYpxXCpzcMcvKvuy8oWyz7sp65BzXEAUcJ9ZCzlyf_VQq4Vj_vUqDdMQ2xh13urucQrWQZCXb2CTywGCSgxz-s1NQa2TxVbwiyWlERjCZenHvUlKzFnUnFvjcVwr8tfHcXel4VOyS0aPa-_1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CekE95DMKd2F-ua4QquQCtGQ4O2e8JGstQZhmHuF5kd21WFFIgvn1cj9Ki5Cz6WYIzUMVauFxrRamlBtDeKDV8DygJ92_0iQynfAUX5ypvVrLOKIL1SkOKrkGC1l_LUHpyc2Rn-Ih-Q9ybKWdCZUpu152sKqoj225cjaiLf6LYajyFsTSFidpo29K6Lv5CIznZI5Q7U-41eJ0Dn-k87fPuVVnt6B28n5JVsUprNdRCthOvyHgnx2A5MiadcM7onwhLJKc8o5r8wafhE3TSJZqSoVmylruWOx3G1Ni9Oa0hv2_LBt_YA7rmHTcIUNTvuMycBR0Qo9QMVe6aQAKNTgNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KfPWN544NpW0fD-NDcRKfrdPVa9Wpp5be38DQA-8qVHQ_eqv-s4fLKcGPdgkMd_6HUyrU5keRhHERVP7yLyUleaf7vHtrAILCbUx5FOZsKM7QA0DfXtcn2DSGcBF-rhlQ6FP6ODhzYMe7HGOiOZ53VrOpDRSHB3QutLKhRMy3saF6II2EaEYv4vh7NCmGqS1joVyHWN1QUHX7d_BMjvJR_3g4o-FwQfwAUjsPsJL2Sk0PgoLYTzE7O0jThkP7PaSvUjws6WryPpF99s3lLi4q9kGtmX2FUnPTrSogd2YlZ2od7zVfCVmRpLy732PbbwmXenfUU-PRp_lF08o5mttUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قالی بافته شده در عراق - ۱۹۷۰ که نام خلیج فارس در آن حک شده است
🔹
۱۲ سال بعد از دوخت این قالی، رئیس مجلس عراق به دنیا آمد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/683020" target="_blank">📅 12:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683018">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b492a859.mp4?token=SgxGgP3KZBUhI_XmbrB6LIqmY_Bii8c3NR8-3hkN46sXFVX1MKw1Wih7qu49ShJ19VnC37gD7_z53JmT78AhGwRD3GTb-n5dnRUEWhzmJPBw3iI79x8W5-xt0N9A0lG28eYGIfobMrSvB2mYhrD26zkpBUA1OvYiaPwRrY3drYyDblKG5Ss6tCwYZk4d6CkpvY-UIE07Ups-WToQeEz3OUPivf9NXNo4Z3--CdgfKoCSIzMjLbA_KB3_ID1Hajh6R6BSkt7X51jLy65b8IGT2eebM-S3ZAxi-163ZHi1LJNJAkXCu4xlbTcZMj3sG9lbalH0A4q4XoIAzdhDelf5yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b492a859.mp4?token=SgxGgP3KZBUhI_XmbrB6LIqmY_Bii8c3NR8-3hkN46sXFVX1MKw1Wih7qu49ShJ19VnC37gD7_z53JmT78AhGwRD3GTb-n5dnRUEWhzmJPBw3iI79x8W5-xt0N9A0lG28eYGIfobMrSvB2mYhrD26zkpBUA1OvYiaPwRrY3drYyDblKG5Ss6tCwYZk4d6CkpvY-UIE07Ups-WToQeEz3OUPivf9NXNo4Z3--CdgfKoCSIzMjLbA_KB3_ID1Hajh6R6BSkt7X51jLy65b8IGT2eebM-S3ZAxi-163ZHi1LJNJAkXCu4xlbTcZMj3sG9lbalH0A4q4XoIAzdhDelf5yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عبور خطرناک جنگنده از فراز جمعیت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/683018" target="_blank">📅 12:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683017">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuHpfpuQso4eU3jvf2ptoLw6ELcT-lZHcg9skV7NyW8pt6GLf9oNQX6gzn2CB-N0HPOZfS8ITqeSLgkaJak8Inx7CxmrwED-cNGCnUoWzIlhhOerHGdmPNVseDNAZRn_e0mwuGHBj97ckMsWiPluxC8Roy-aX-gTXTmyrWDd9uCnCK2pld1aeoGXB3ArLMP-acEhxoO14yjx5Elgo1PMD7yYcWvKg-Y0WzIHqZp1vSiS6wFGtDFi5AUiAa7icgaEU8WW1HNqNdaVIT-vfz667lFWlwB5FcVOcmCCidujOoV83CCh_KZxEsDaGpn46SzmBQSAk6Fdyq7qsbmwGL5ksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ای‌بی‌سی‌نیوز: FBI از احتمال حمله پهپادی ایران به کالیفرنیا خبر داد
ادعای ای‌بی‌سی‌نیوز:
🔹
پلیس فدرال آمریکا (FBI) در روزهای اخیر به ادارات پلیس کالیفرنیا هشدار داده که ایران ممکن است در واکنش به حملات آمریکا، با پرتاب پهپاد از سواحل غربی آمریکا دست به اقدام تلافی‌جویانه بزند.
🔹
ایران ظاهراً در پی آن بوده است که در صورت انجام حملات آمریکا علیه ایران، یک حمله غافلگیرکننده با استفاده از وسایل نقلیه هوایی بدون سرنشین (UAV) را از یک شناور نامشخص در سواحل سرزمین اصلی آمریکا، به‌طور مشخص علیه اهداف نامشخصی در کالیفرنیا، انجام دهد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/683017" target="_blank">📅 12:12 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683015">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f30a0037e1.mp4?token=Lz5sVQf8hZUGhDVTpthU611Kr9vw4Xt-N_u7YNiLprl6Kg9MR52IubnSBuYgUvh-HxUTtDIxeXvX7iby_Rs5IpWow0OZQagGIaS09167kUoO3Whfl6a9Dy2WuBWuvvXJ6htYcBsTn-Ih1Ygkm4x3CV6d-Lc1Of5wcL-g_Fz8-3DwgXbQGL2CiscURsir0X2ZezrSpLDAiY6jCxdZwo7Lm3ULv1kJ8ZGcQgPxsbi0PegC6C76vr6tj9ApzatRUVNQzS92s7rDAPoR-Z-C41l2-OVM0FJ9DfFeNqxkcIfOS-6NcFlfaqteR_D3RH6mhFkk5tXEa6slsdrfQ6Eh44MkoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f30a0037e1.mp4?token=Lz5sVQf8hZUGhDVTpthU611Kr9vw4Xt-N_u7YNiLprl6Kg9MR52IubnSBuYgUvh-HxUTtDIxeXvX7iby_Rs5IpWow0OZQagGIaS09167kUoO3Whfl6a9Dy2WuBWuvvXJ6htYcBsTn-Ih1Ygkm4x3CV6d-Lc1Of5wcL-g_Fz8-3DwgXbQGL2CiscURsir0X2ZezrSpLDAiY6jCxdZwo7Lm3ULv1kJ8ZGcQgPxsbi0PegC6C76vr6tj9ApzatRUVNQzS92s7rDAPoR-Z-C41l2-OVM0FJ9DfFeNqxkcIfOS-6NcFlfaqteR_D3RH6mhFkk5tXEa6slsdrfQ6Eh44MkoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز «فرمول یک آسمان» در ایتالیا
🔹
مسابقات جهانی پاراگلایدر در ایتالیا با حضور ۱۵۰ خلبان از ۳۳ کشور آغاز شد؛ شرکت‌کنندگان باید مسیری حدود ۱۰۰ کیلومتری را بر اساس نقاط GPS طی کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/683015" target="_blank">📅 12:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683014">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hw33k0QmzKbLbYa5u_f4cWZ3-fI-5YyN0QcR8QpHbqmWAVQFGXHC_CwLnqOEyiqW5Ftz7aWAIm4Iw9ohfQhg9yCsAZ_lzbH97jRYnc9BiAXP5TqZajkihI2SKOwOndXMK6EKdGh2DAT6_AOVPqkGpnmVcgYmAwM4t5h_R_xQVMPTbGIj_lV8BcZ8F8VyvfiCnL6zb4y-fuc7Co-MBCXzHuaoiM6eGSR6iI1JCYazIKZOzYWYd_llqDQmOlSO8lpVJNZcT3JABWoL_nT9QbcZ_u1LN_quM6D42gvlu_DebMbs60voQ2YSW2xv8rqVQv7ekiwI7b2YDbC9l_ZTInTdsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد ۴ برابری قیمت موبایل در یک سال
🔹
افزایش قیمت تلفن همراه در یک سال گذشته، بازار موبایل را تحت تأثیر نوسانات نرخ ارز، افزایش هزینه‌های واردات و محدودیت‌های عرضه قرار داده است.
🔹
به‌طوری که قیمت برخی مدل‌های پرمخاطب طی یک سال دو تا چهار برابر شده و دسترسی مصرف‌کنندگان به گوشی‌های اقتصادی و میان‌رده را با مشکلاتی همراه کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/683014" target="_blank">📅 12:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683013">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea40a0464.mp4?token=HF1dPgH_ztXqUjPO23DFmA19DML_ytkvGxgtT5JaP7NIvQ5p0VgsGaS6XLjHa55vDorca9hiSytX1IX0CgxK1uDPkoH_6b_kGdr8mDE07hIq9JMpc_7j40qFtwp6Yhf-Rj-4b6E2VaxyKZ49xoijFUlSRXYNpCAPdsI-eWc-rXs3JwdN75X9yzfZqNtJ-5FBntPBPSQy4Kc5bnHe68JlfKzqYb1YNLxCX6n1HG5BSEKzcW-SN46JVooVQk07dk5xeEStKCYgcO9no5CgalYKVBUFMxRO6iSPlmOTGDFHM3DrQHBms7UREPTpbprWK7smEGDK4TeUkFnJqaL91DRU9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea40a0464.mp4?token=HF1dPgH_ztXqUjPO23DFmA19DML_ytkvGxgtT5JaP7NIvQ5p0VgsGaS6XLjHa55vDorca9hiSytX1IX0CgxK1uDPkoH_6b_kGdr8mDE07hIq9JMpc_7j40qFtwp6Yhf-Rj-4b6E2VaxyKZ49xoijFUlSRXYNpCAPdsI-eWc-rXs3JwdN75X9yzfZqNtJ-5FBntPBPSQy4Kc5bnHe68JlfKzqYb1YNLxCX6n1HG5BSEKzcW-SN46JVooVQk07dk5xeEStKCYgcO9no5CgalYKVBUFMxRO6iSPlmOTGDFHM3DrQHBms7UREPTpbprWK7smEGDK4TeUkFnJqaL91DRU9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ساعات پایانی...
جشنواره ۱۰ سالگی "چرم مَنطِـ"
✨
تا %𝟴𝟬 تخفیف
✨
«تمامی محصولات»
➕
𝟮,𝟬𝟬𝟬,𝟬𝟬𝟬 تومان هدیه اسنپ‌پی
با کد: PAYZ63R
حضوری و آنلاین
👇
🌐
manteofficial.com</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/683013" target="_blank">📅 12:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683012">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouT7AelUuh1jkEG4t9qZxWyv7NHEPJ6E4Ei_qqliaQTkFVKBWG5KDK9v4POV4ESyBqlBU5J3PkSd9tQMIHPTmV_jF_idLp0djz6vlXnJOmnB8ZAQ-EXyKI_uhKxQzcks2NXBsrOvzlP0SFV8zIarvwq6rBfWh4vzsHELCTfLDJYzfbt_SYQsnxj44m4bqmdKsx1WJASPPtdzV_AnpwtUtzi8nkIpCUoNDmh0JMSLPa7yq4JtvVgoBQQwQGk381IsugTlcQLgYUZINrkHf2GnBNDBn9xICiUe-uhOA7IRTYviFee2M0SD6grgU_yGkoq6fFiFHg1G2fA9GNdhuEtklw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلتفرم چینی Bilibili برای رقابت با یوتیوب وارد بازارهای جهانی می‌شود
🔹
سرویس Bilibili که رقیب چینی یوتیوب است با راه‌اندازی نسخه بین‌المللی اپلیکیشن خود در اندروید و iOS، به دنبال جذب کاربران و تولیدکنندگان محتوای غربی است.
🔹
این شرکت قصد دارد محتوای چینی و جهانی را در یک پلتفرم ترکیب کرده و با استخدام نیرو در چند شهر جهان، فعالیت‌های بین‌المللی خود را گسترش دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/683012" target="_blank">📅 11:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683010">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQe3W5oIxbV7MYp2XNlEIeWHSCCNk6fT1aB_ngGRJnd6ps_cMxwKR-PgO8uWeU6zmwwWplGBivypDfxrectd4x6hQwD_yKV0IuSM06BeZ_P2JzNXAPgRC5Yut-WB44c6ztFjhqClfDG9uBK5v4EcA2vmSRfm0ya6CCZZRVZbtrbhuxaUJ-r4NGvqHqU7XqkhH5O4Vbi2S8w7UFOG0iOBwja0Tp6e9_l8ZM4hS-DxYdxQ3i50V0eGCMTBPHYspDb_Ps_hnyP5j3B50Uh8zRs7i7h2gccV96-QqJorwolSk006t2t1xl0bciD6vTA_RslbwT6TALzfuor1HRsHavCtrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلتفرم توئیتر در واکنش به توئیت رئیس‌ پارلمان عراق که در آن از عبارت جعلی خلیج عربی استفاده کرده بود، طی یادآوری‌ای تأکید کرد که نام تاریخی و صحیح آن، خلیج فارس است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/683010" target="_blank">📅 11:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683009">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/in_zX0PcppV-lQTjHV1GhfwvbKMHdie6GJME4T5uWLFjevj4IHPMg1gFy2zzX3rCRpglhXmdORXjEQ3ZsZJJGEUArSTf20bNb3QZdl9XUNAD4Fa29kwgcjmM_24cPxEGLKUu_FyomJbQiq2hn5_jCZODOBE8o1suzr6HFdUu4oqMA3YZaLLoCesx-Ko-fpksZ9HdLJmNaydHio-Xk_Zyp__uT-Jjzt2MZjpXFub1yVkNecIfjCAMjbr4h7DsHhPWZQatESbc5BB2KC29mjKCuUmq-aKjAPDW8OGpDK0-OEGkKzx4O1Yyvg2jBfCDkHDFJ-yG38ndtB82F_kyxi6pkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌼
بیعتی دوباره با صاحبِ زمان ( عج)
💚
به مناسبت سالروز آغاز امامت حضرت ولی‌عصر (عج)، در اجتماع بزرگ
«مراسم تجدید بیعت با امام زمان (عج) و رهبر معظم انقلاب اسلامی»
▫️
با کلام:
حجت‌الاسلام و المسلمین سید مجتبی کاشانی و علی‌اکبر رائفی‌پور
▫️
با شعر خوانی
: محمد رسولی
▫️
با حضور
:  سرکار خانم الهام چرخنده
و حسین حقیقی
▫️
با اجرای
: امیر مهدی باقری
📍
وعده ما:
شنبه ۳۱ مردادماه، ساعت ۲۰
میدان شهدا، مشهد مقدس
🤍
بیایید در این شب عهد و انتظار، دست در دست هم، بیعتی دوباره با امام زمان (عج) کنیم...
@Heyate_gharar</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/683009" target="_blank">📅 11:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683007">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
خودرو جدید محمدرضا گلزار در خیابان‌های تهران؛ رولز رویس!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/683007" target="_blank">📅 11:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683005">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNJWrtBPT00UQr-Z3oO7VWvNTUoVbHfntap9lSRk9-xeRB9EQrhFm9tlwjteaqagCY6sXGF8upBUgamvFOBcGzn2ugNwEhHko4r1fiE6M39_KI0-MEWLdX5omTeSk7c_vAFcCOLZExH-1Vqg-OWxtolIxSPgk7I3nBRHfA1Mj5VaivXOLRDwW4G38FXvji0XCBjKl4ftUy635QkNqdAg5vsIzrSocjaPbLqOv4FtHyZAQnwKhava7oNOWM-rsQ-HIfwaN08OXHtzC6rw6xI08HM5oeE-opZN2NMXysrrL-JgL1gCrinnWgNbH6d7buOnjdJUg9hffAfA5Htc-ZRnFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجید شاکری: پاسخ نظامی ایران به حمله اقتصادی آمریکا ضروری است
🔹
هم معقول است؛ هم به موقع.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/683005" target="_blank">📅 11:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683000">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d3fbbb826.mp4?token=C8xHwdMWcNQFMQAx5ML36h-HVN6b2i6JSb5AASZWXtQ5hK6hKrIE154_rdk5wrIhWdAtqkBsUIz98dqjeRC3YStFenykyB_-Eqlzn3epik49TdVfkWRgHFSzPiWQBI0FPWNFkaCPx6OhlpGaJThrauU266JyoYijI55SEWsV3mtEaQkWn3lI4WuKp0QeFeAJFgXKBIhfMgYwMWlfGcl1rKysiYjznHvhmRWWoE80t08YQw_zbW9Kdztz6bzSZGaJ2AXy69h-6JQYNGMdjsRlNkk9-VzNNE3GGeRgoBdd265hIFuV4Yq3KgoJGq9_uRx7STEpvT4V1d_qwRZgQfqzKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d3fbbb826.mp4?token=C8xHwdMWcNQFMQAx5ML36h-HVN6b2i6JSb5AASZWXtQ5hK6hKrIE154_rdk5wrIhWdAtqkBsUIz98dqjeRC3YStFenykyB_-Eqlzn3epik49TdVfkWRgHFSzPiWQBI0FPWNFkaCPx6OhlpGaJThrauU266JyoYijI55SEWsV3mtEaQkWn3lI4WuKp0QeFeAJFgXKBIhfMgYwMWlfGcl1rKysiYjznHvhmRWWoE80t08YQw_zbW9Kdztz6bzSZGaJ2AXy69h-6JQYNGMdjsRlNkk9-VzNNE3GGeRgoBdd265hIFuV4Yq3KgoJGq9_uRx7STEpvT4V1d_qwRZgQfqzKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایمان محمدی، کارشناس مسائل یمن: یحیی سریع از تثبیت ۳ معادله در برابر عربستان خبر داده است/ یکی از معادلات این است که نقض حریم هوایی یمن با پاسخ در عمق عربستان همراه خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/683000" target="_blank">📅 11:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682999">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkyDTly7gfYqE_YmLXrKZo6jdoHC1w7rN_1cUkeuFSJLCbZXtBiPffkqnZ3rPGR43gENRZHj71msEZOABIv2Tl2_CMNpVJ8OcNcrVh9sBKkfylbf6rlT3W7Zo8Haaz58-fS8w5VrGk6aDl32ZikJA5XpW5VF4ugRbxVu1x2ewgCg_HJ0BgRtBBD-Qfsz_iFt7n7X3zQahVURaQlx3-kN9W8ma4Mzg-YiCN-W-6B878kEXgZaKtpN0lFvDziZWi7J2Zn6a6oCZApB_vZHt1DTxX_bq9XMtokDmsZSN1v84D1LfCL5G5kla62MTu_cHrSZist9-toDq_vljz2d1rXb6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌼
بیعتی دوباره با صاحبِ زمان ( عج)
💚
به مناسبت سالروز آغاز امامت حضرت ولی‌عصر (عج)، در اجتماع بزرگ
«مراسم تجدید بیعت با امام زمان (عج) و رهبر معظم انقلاب اسلامی»
▫️
با کلام:
حجت‌الاسلام و المسلمین سید مجتبی کاشانی و علی‌اکبر رائفی‌پور
▫️
با شعر خوانی
: محمد رسولی
▫️
با حضور
:  سرکار خانم الهام چرخنده
و حسین حقیقی
▫️
با اجرای
: امیر مهدی باقری
📍
وعده ما:
شنبه ۳۱ مردادماه، ساعت ۲۰
میدان شهدا، مشهد مقدس
🤍
بیایید در این شب عهد و انتظار، دست در دست هم، بیعتی دوباره با امام زمان (عج) کنیم...
@Heyate_gharar</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/682999" target="_blank">📅 10:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682996">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c13095e93.mp4?token=JB5wyj-wIsRCPrXZtD0ffE6sgQ9WkUILVwG-BEsjekBpitn0HB1gCt58xi5yp1K4t2Sx6--QXi3J04whOJaE2zVn8A_jDZj7duUh6LDRkRvcmZOs22VONtVt4M6nVmtMxdy2BDFpBROjlrLQrhqdA7QG0barHrNicP6JQNl-dS7QRoPnI0KM6YjU-6WatczT5irMk0wtV51xUOtskaTtrlckU_Lp3SCcehIUJ8-y-VN4NnPAWWBdgiPRtQohRoeYgVdAhy88FjquZlmGC8_6rtDhTEhPhfrrbYAmBl_Dnr5Rm2X21DMNTlG3ERK08lM9UqUHeJHZmH46eoiEa5oWkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c13095e93.mp4?token=JB5wyj-wIsRCPrXZtD0ffE6sgQ9WkUILVwG-BEsjekBpitn0HB1gCt58xi5yp1K4t2Sx6--QXi3J04whOJaE2zVn8A_jDZj7duUh6LDRkRvcmZOs22VONtVt4M6nVmtMxdy2BDFpBROjlrLQrhqdA7QG0barHrNicP6JQNl-dS7QRoPnI0KM6YjU-6WatczT5irMk0wtV51xUOtskaTtrlckU_Lp3SCcehIUJ8-y-VN4NnPAWWBdgiPRtQohRoeYgVdAhy88FjquZlmGC8_6rtDhTEhPhfrrbYAmBl_Dnr5Rm2X21DMNTlG3ERK08lM9UqUHeJHZmH46eoiEa5oWkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دوش رایگان برای پارک جلوی پارکینگ!
🔹
یک مرد استرالیایی برای جلوگیری از پارک خودروها مقابل پارکینگ خانه‌اش، آب‌پاش مجهز به سنسور حرکتی نصب کرد تا مزاحم‌ها را خیس کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/682996" target="_blank">📅 10:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682993">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66d822e31e.mp4?token=n9CAOLeI66I4MULNdQ-NyMj3Bhg5cptxHSS7R6zuVXHntgVN63rWseeoqTwu6N_t2LerHNcLxnOiFBfTJEhIlhrfzCAE9xHFc6sTur5Hk6zkGP0l0xz8RtPAvgXg_-omH9l0fyhNA1tn534pRNOGU4BidWx7enMwR-KifPrX-r--oyOjQou_m3VVrr6MjE-4bw7bLmRGWLV9So2KmIAE5FdQ1ZH-i4xygXpD2LUS2m131kEDDM8al_2RrcBhSkCMg0tAhchVBsVMolCKLDznDWC6TfTVKD3SWS42Ufoo58dWh7s0K_Jz8Zaagx2Cu8C_Ot4MauzMj05gOiHsVVdtow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66d822e31e.mp4?token=n9CAOLeI66I4MULNdQ-NyMj3Bhg5cptxHSS7R6zuVXHntgVN63rWseeoqTwu6N_t2LerHNcLxnOiFBfTJEhIlhrfzCAE9xHFc6sTur5Hk6zkGP0l0xz8RtPAvgXg_-omH9l0fyhNA1tn534pRNOGU4BidWx7enMwR-KifPrX-r--oyOjQou_m3VVrr6MjE-4bw7bLmRGWLV9So2KmIAE5FdQ1ZH-i4xygXpD2LUS2m131kEDDM8al_2RrcBhSkCMg0tAhchVBsVMolCKLDznDWC6TfTVKD3SWS42Ufoo58dWh7s0K_Jz8Zaagx2Cu8C_Ot4MauzMj05gOiHsVVdtow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روش خنک کردن کارگران در دمای ۶٠ درجه عسلویه
#اخبار_بوشهر
در فضای مجازی
👇
@Akhbarboushehr</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/682993" target="_blank">📅 10:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682992">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZC2rk10yGOr2PBg2I-P0sKpTodqfXbArphJB3m9JqyAJDFwb0NyNoqkiGYNo40yLyy-xl9gz6RdLMlgP_QVPzCjVh-1xajhghFC9kc56ZBd7dZywlIdJqb_V6DnUy4KBQDN0-uGgB-I2VlP1_1mSt06KQbyw6GjXqUwnHmQCEEcJlxMLtWCymxLHpducV1exaB4x0g1VuhG7IVZhOPm2RsfYHdpMK7XasyeC_pt9jpEvWgxwZFZRUdw5-1LQHd9aNfZTLGdh3xdRKYeKvUCMju1o4QdTQHLfo3Mx-j2HcmhFviMYnj9eX7rUtN1nX0zEpbkkkNzFCPbUo9ZkMgiEDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تکذیب شایعه بنزین ۸۰ هزار تومانی از سوی دفتر معاون اول رئیس‌جمهور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/682992" target="_blank">📅 10:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682991">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JS3jVbc592u52QDi8071FdEqKTmpcDcNYLjSwcG1oYhnFEJaCOCTS7uo6w0vf9iYVdj3hPCnzfG0EvJYm8kzc5SsLY2UMpxTcyFtUd08-rMgIfPoxNypMXufdgs8tiaur4egpKOIKHaYajiK6UM7N4KTdmGCfmOxPh3Atb4qOtl7-F9HjOxJkhDzX5DMif_v3obzckNRmu2hSqnoYR_CrPhBo6UdpK5CRv_EIQ0XOIzn-fMkjNM4mM7cHTaVAdTtXuD4UJMu9mERcWib7TfDCyZqtZXnmBS1ZeeWyrY2cYZzduw_QbP2edYZowpz6VnTsuj0uoFlUKiFlMna0BIDLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکس جدید رونالدو در ۴۱ سالگی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/682991" target="_blank">📅 10:11 · 30 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
