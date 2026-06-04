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
<img src="https://cdn5.telesco.pe/file/DXS4la6HD-4NjPxFR3uS_9x919RdS_T4AckDu0wBxXbpWodE89S1KxVBemTkNMEkXcea2iYxycwHiMQte_BKdUCzbae-qZnWvpF8aU_i2GMubgOudoorEX525is7kGc86tPJJC8jfO2VgY-hDA5Le2x5GYP8itWgQ24WNcjMFaQ_7fEe2U-sDNQZGEzP3po1m0cZQVDU1vRXFnv4fCdkvYhKyC_-VZ08eOZXbV7KLBBcYscDSctEgo-0UNpMkEN5slVt-v4YIM9Up7L6YtXkbCIWHaOU1xZkXIiItTZTXkKN6ZvIPp9bqY_hd9YEfu42-kRr7n3ttar3w5Yr1gqWNw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 178K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 22:44:21</div>
<hr>

<div class="tg-post" id="msg-90935">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
فوری و رسمی |گل‌گهر با رأی انضباطی مقابل چادرملو برنده شد
🔹
کمیته‌ انضباطی فدراسیون فوتبال رای خود را در خصوص شکایت گل‌گهر سیرجان از چادرملو اردکان در خصوص استفاده از مائورو آندرس کابایرو آگوییلرا، مهاجم پاراگوئه‌ای چادرملو، صادر کرد و براساس این رای گل گهر سیرجان در این مسابقه ۳ بر صفر برنده اعلام شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/Futball180TV/90935" target="_blank">📅 22:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90934">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تاجرنیا:
فصل پیش هرچی اتفاق افتاد مقصرش ساپینتو بود نه رامین رضاییان و غیره
من میخواستم ساپینتو رو قبل از بازی با الحسین اخراج کنم میدونستم اگه بمونه حذف میشیم ولی تو جلسه ۳_۲ به نفع ساپینتو شد و موندگار شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/Futball180TV/90934" target="_blank">📅 22:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90933">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqgMxz9sYUmxV5t2ZvnKLic_zHIKsm1M1nKVRVhBIJmS_hezcu1qBlDtHHImLiJn2X1Sj5nW7P5qGz1GuwSIYQyGVPRLQ5ITwjs4TNS_S9XJu2QzoR60Hbe3CUWsu16SLdKL1g3ahrWB6lAFvj4Cta4JJV9mbUd3FHvNRC8FEcCT14XjZietmxS-xHguvyhFS9VEbbTd2dwEn0LqY4THSafOrzuSzlm83rZBuiotIsyhEBSH2NO4A0qoG_QAv1btKXgrPq2PO9CLl2eSQKO6kcsxXI-vQjiVKDe8Ndh4SgIzbsP1PZeeyJ5UlGn3_VVzjayTvRZwWm9hLaoWF8zv0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فورییی و رسمییی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آندونی ایرائولا سرمربی فصل گذشته بورنموث به عنوان سرمربی لیورپول انتخاب شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/Futball180TV/90933" target="_blank">📅 22:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90932">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6uX65m47YqbhMHLwSBGV1BsqyHqTYO4tFdbNXVpQex-tA5CEAg_eo_imKWL3ysjm7Y7-mQIXAFBT8L8ZcJ1uVpcX7vkQE5Se28Sv-HkLXJ7kIVsoxrQ_vDilCKpo_cuD19YafwXrcDZB-NIeQb9HR0WajSquuogNH5O9XzH30_jJN_VCd376mp56Mh-Z60SHihNNMwG3e-px913XTLDiAy0APkY-1GS_M0A1eoefumeEo0Tc-WZbFWtAladYk1VmqIQgaBvR7i1magWJ-RIH-do6KWFXhJ20aItUUa9svmcydAKLWhlTfea6OWpMi7NdY5RcqDJF9rSjqpo4IIOQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران با پیروزی ۲ بر صفر مقابل مالی آماده جام جهانی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/Futball180TV/90932" target="_blank">📅 21:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90931">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iht7En_TdpEXTCw5Cdq73AYHehDtHc3JpEOGLsXlSqOs__mpbrQyKyxsrYszYT17dpq5TZS08af7LPBAfX1YIEr27p3eRIu-szBy6kGoPQQh9br3-gRQ9S682LWex2NqUm7VwmtmXaTszap19sxztJ6AYKz4rEIOut4Bl0p76q8Of9RJYY24w5W3Hj9glYyGz4tlXXaL07RXMf6aBiQlV64lNNnjo3dhG8eXRx3U5j3Ke1zl5xHPUsyBOWZN9RMltSKcnKwndc1WxEjGY0jxgHDylsH2H8Ne7m3Ee2QPH9OOwInk3vtdfguuJEgxAk_kVobobLSukxIFTDmOGijMYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب پرستاره فرانسه در بازی امشب
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/Futball180TV/90931" target="_blank">📅 21:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90930">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2312570c50.mp4?token=FCMdNC9UcCgjpv-NKj8sprn3djm_8548o8yHUzN8eI9xa77719PbiRy5t10QJa46uNPMxreNOM-JQ9L6jwipCNkOyDOFe1bxjQmWfUdvifzxBgC-ojzE36OsstIvPupKiw4yxWuLj_ABcAVDmMLM7BRWRDzT7QtCErndYVyciiL--eAqK_CWqw9zfl66__miTNe-ZrAfnrn9MqVp8NwTdMKALRXWoxmhE2515NnnAZi_YkbFGfPrSr2vAKvzTncApkx15USFrTidz7RD9tKEiDIcUdamwSmfngU4lxe7ubDeefdfpMN9-vfUtCpoyLW4kMa1rq98R6LJJfAm0cJGAnTyX7UQKgClcyXFZfzgNHkyDu8ZuTGvkY-jqJY1H7J64UDyF6-vwh7y0ExHEsP-6EvTxZrU9rt55H5H5jbhP6dpdbvZBR8H7I_sf3R2zflDtoZdT-Vw1EXuvD7mX3LzpyOkBToRAIChMhVrIe7dJHGxEPyk_nyQjbuOocMsrTiu0p8mboFRpltsjoLy1-A71AbjvTvv2WAY6VFl75lrSIdaLitQ4eZdyOFY34K1Q1WrvkaO8Kt91lHFvyFWovYSphWFUfAFEC2-j0u2bR5VmP1U67zob1DLrQMRdph-dxrUALOALjf-fseUe7OA0Lpg6H8sxHxB5W6uG6EGMndLddU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2312570c50.mp4?token=FCMdNC9UcCgjpv-NKj8sprn3djm_8548o8yHUzN8eI9xa77719PbiRy5t10QJa46uNPMxreNOM-JQ9L6jwipCNkOyDOFe1bxjQmWfUdvifzxBgC-ojzE36OsstIvPupKiw4yxWuLj_ABcAVDmMLM7BRWRDzT7QtCErndYVyciiL--eAqK_CWqw9zfl66__miTNe-ZrAfnrn9MqVp8NwTdMKALRXWoxmhE2515NnnAZi_YkbFGfPrSr2vAKvzTncApkx15USFrTidz7RD9tKEiDIcUdamwSmfngU4lxe7ubDeefdfpMN9-vfUtCpoyLW4kMa1rq98R6LJJfAm0cJGAnTyX7UQKgClcyXFZfzgNHkyDu8ZuTGvkY-jqJY1H7J64UDyF6-vwh7y0ExHEsP-6EvTxZrU9rt55H5H5jbhP6dpdbvZBR8H7I_sf3R2zflDtoZdT-Vw1EXuvD7mX3LzpyOkBToRAIChMhVrIe7dJHGxEPyk_nyQjbuOocMsrTiu0p8mboFRpltsjoLy1-A71AbjvTvv2WAY6VFl75lrSIdaLitQ4eZdyOFY34K1Q1WrvkaO8Kt91lHFvyFWovYSphWFUfAFEC2-j0u2bR5VmP1U67zob1DLrQMRdph-dxrUALOALjf-fseUe7OA0Lpg6H8sxHxB5W6uG6EGMndLddU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا حتی دهات رفتنشونم با ما فرق داره ناموسا
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/Futball180TV/90930" target="_blank">📅 21:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90929">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1wLPLrwgepWV1UaifFSCxu9jYzS4FgtMOTFbIKT2lOQ4TBmyGDDq7aE_PIpz6vfFEZAzmJ0PSUUAenFwMDMVNBe7BiYRWKQw9zValLrNOu0iBcuHn5cfQ_55fqYAYQXcv2xQ7j9VXp1n4S3PPR0saJNAhAvanttFtZaN1dLBgWpA2glk-vBEh2gOgC3Y-rifcHm9O5wl6h3_o4ZAJgcM_xrc5YStZEKFn5z0xcqMezZIJNHZfkTIQGE35fRDE6nq_d0rKROcEqGYAScfTjfaqcWkYLavDQmWZy3gqqXp0KKEMupDPUVZr4YzoWl6uK8XpyQtBvN3M2VjOQdREkb8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری از فابریتزیو رومانو | نیکولاس جکسون به رئال مادرید
✅
Here We Goooooo!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/90929" target="_blank">📅 21:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90928">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/707e563eeb.mp4?token=oVxbhll3HKFGmMtSMhY0_jXWQDZAwg0HVw3qojYpr0NDiMAYH6Jf3cXRiIbIPfAo-N3qc6m3EeyRbva0WV7wmilOvqgjv6ekmVe2I46QSvahHZ4aZhpw3snFKQUUtqvSki_jvlQW2NAReHXgs0hXdqW1PoJ3aPFDkMWRGaI-GMGBprjOwxZWiUB4n3ln8L4g_hrfIB9ndki7681cNve1NvL1jFEyweuyFOWrXuCMA48xzfP0sAAoiiOvPuuWy7n_FEzGOrhoXAZMayQ8h1S-MGc1sZS0geSxJH0W_11J-4i4nWg9_FsvkmwvxZW0k-yy9sUB3pi5-2U2ApMa6S80Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/707e563eeb.mp4?token=oVxbhll3HKFGmMtSMhY0_jXWQDZAwg0HVw3qojYpr0NDiMAYH6Jf3cXRiIbIPfAo-N3qc6m3EeyRbva0WV7wmilOvqgjv6ekmVe2I46QSvahHZ4aZhpw3snFKQUUtqvSki_jvlQW2NAReHXgs0hXdqW1PoJ3aPFDkMWRGaI-GMGBprjOwxZWiUB4n3ln8L4g_hrfIB9ndki7681cNve1NvL1jFEyweuyFOWrXuCMA48xzfP0sAAoiiOvPuuWy7n_FEzGOrhoXAZMayQ8h1S-MGc1sZS0geSxJH0W_11J-4i4nWg9_FsvkmwvxZW0k-yy9sUB3pi5-2U2ApMa6S80Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فووووووری
؛ علیرضا نورمحمدی دستیار مهدی تارتار اعلام کرد که سرمربی فعلی گل‌گهر به احتمال فراوان فصل‌آینده جانشین اوسمار در پرسپولیس میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90928" target="_blank">📅 21:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90927">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0759f4cb2e.mp4?token=RfOULAz18U0uLEvl-etXroLl-KnAiwagHwAMRJbVQLTiorS4pInGe-_VRhIHk9nnHARdp77D57weE95izoFO1fjeHL2Psi4vZoK6eiajBUXci71ppMm6I-FTJGXqteCP0ScG2TadcXHPpOw6pVirTEhgCSQrfVggLP87Gl0CfTd0ajz2RPLYLu_Vb2MopJcpNKsYmJBe-fhyQ04jf_FRnDxc8Fznyx3_BZWAn5LGUTqEJQfn29Eqz6StAwzVTmdBDklaW3_RPru8GPJlh_apFf0559r9ORbgHD0RZSjqPKK94VQHzs-4eGN34ErwwnVndvCYlSwg9vmJ3a_LhoQqVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0759f4cb2e.mp4?token=RfOULAz18U0uLEvl-etXroLl-KnAiwagHwAMRJbVQLTiorS4pInGe-_VRhIHk9nnHARdp77D57weE95izoFO1fjeHL2Psi4vZoK6eiajBUXci71ppMm6I-FTJGXqteCP0ScG2TadcXHPpOw6pVirTEhgCSQrfVggLP87Gl0CfTd0ajz2RPLYLu_Vb2MopJcpNKsYmJBe-fhyQ04jf_FRnDxc8Fznyx3_BZWAn5LGUTqEJQfn29Eqz6StAwzVTmdBDklaW3_RPru8GPJlh_apFf0559r9ORbgHD0RZSjqPKK94VQHzs-4eGN34ErwwnVndvCYlSwg9vmJ3a_LhoQqVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال چالش رفته بعد پشماش ریخته که اسم خودشو نمیتونه درست بگه
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90927" target="_blank">📅 21:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90926">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4R3HeLINXonNknCaNpH0HAlUIEXYp6n6vUVzqZO05Wln24xbXxutRxqCHNcyRnfhHLPJ1GtaKgpVZRqgcfx7iLOoaFdDQfCMrt8bc8Zk5XyYQ2kWndggqgl12h5FdP0LOPnT8TCajSGIFuuogVaU-ne8mGwxP43SnbiEE9Vs6vvD_L9WHYBsOpCIXPndtNKw7dOrLVemGx-6ZyK2IwDHXRK5nk2Am8TX_JvzUK-yhcLTgfEees_DsLe-u4yabmo5JMVioaNFANtIHhfB_AFklgl0MNOBNayVVXU8nITv3nQBJ_fVt66dXlOHv398oqZGyNyXtmKiQMtRBbLpHMWcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب اسپانیا در بازی امشب مقابل عراق
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/90926" target="_blank">📅 20:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90925">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVOY1Tt3TJdEfdYDuTpeIA3kaektSuc0lO93hDb4E882WojkuKEJFjUkfYIbpYJJH08yCAbzBEBctIKEVLao_QkFsDdGol5N2LU8q16tm6J8PrnNkiUrggt8vWOEHP-O7iumOVLqKg8JeeFmW6hpFHJDqixoIlbQvpwEsSXuRc49u9Y-qW_fBxdeXvWcwd27wEoKBRAA3PNEpFpCnuiBQNNetsD3nn8HkOA8v0YBf-1j_G9LNfZmtOJNsO2mWaxsFRmwZcqsrMNhpcgmKv0umU0nfQt71gBWU2IKJ5Ty4Lurc1wdGjo5Fxol9-fmHMqEG_hY-Z0Qrfp-3L7hBfVumQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرخه زندگی اوچوا؛ قشنگ هر جام جهانی میاد میترکونه و میره تا جام جهانی بعدی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/90925" target="_blank">📅 20:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90924">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ba0545774.mp4?token=J2YGyJ2cPsMqxBv5t5xiBIViBlDR2yMIpL1ttSy_UbepIs1l6JhFaPgKelofTfmL8jTF8yxiOiPUO2zyY4P3ALFmnd8K6g2dK932gzykQzBN872JNUTuCB-SvPCZ6g-PzcXTd173-Gki2KP_xsVhCIfaMZ06AoHn3yiXN7u7mNSZT7CsxZv8UyvTpEa5L1g7YIF_6zXcjdH9-xDs9eWQk9BErvZ37nPpiR68p6IfDkGA74BmyFEg47h1mHjMJSjI68PXZszXQfImHUyO_ySD9Hnwn-71-zYEU4AsMGcQGXg6-Nmu3EnIWWKPnDAvTCWp9rgiweU-4TDrfOs7C3t8Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ba0545774.mp4?token=J2YGyJ2cPsMqxBv5t5xiBIViBlDR2yMIpL1ttSy_UbepIs1l6JhFaPgKelofTfmL8jTF8yxiOiPUO2zyY4P3ALFmnd8K6g2dK932gzykQzBN872JNUTuCB-SvPCZ6g-PzcXTd173-Gki2KP_xsVhCIfaMZ06AoHn3yiXN7u7mNSZT7CsxZv8UyvTpEa5L1g7YIF_6zXcjdH9-xDs9eWQk9BErvZ37nPpiR68p6IfDkGA74BmyFEg47h1mHjMJSjI68PXZszXQfImHUyO_ySD9Hnwn-71-zYEU4AsMGcQGXg6-Nmu3EnIWWKPnDAvTCWp9rgiweU-4TDrfOs7C3t8Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چالش جام جهانی اینبار با دنیا جهانبخش
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/90924" target="_blank">📅 20:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90923">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-T70igYn5vwFNQ2PHfMGIdysXoP_ByQlyDnIJr4RaorWqAxysStKLYhZsUlSKuDccbnPdrgdYwt2vcpH-wFOrpI-wTCyrma8_BmavQcNdWHOR0eBCM791oSt0qFl9QG5td81kYQS-aI5Dfxpa_G7mgfJq04D48Lxz7d514RhgdcM9jVwSW9Vjp8qBP2rPD9u5HhyF8OpDr4IRGAWgP35hVUfIqrulspIVnLVWljiOfUr-DuH8PnQi-PO5J1knb2AwCGLSBVPg_nkPWYGyOcmiMpe1ja8wP09-BaXi6MdXK-MWC4Zx_p6_KWyu4hmIfO6bE7cMRMEl6baCysBhYwMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ارزش ترین بازیکن مالی:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/90923" target="_blank">📅 20:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90922">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2ecwLDiiVVXe4b3BnEKXn2R0zqk17c0XtikQK7BZqqnORor4QV0JPhoe1zMh3FRxKB-iw6nP7Oq1SGQYHDhLavWlw7l2OEZ_WQof70tn121lHzhK4X1IiNaaLYbI5PeyIq40OrmvzeIVcwu93GHacyTjfXngffYjSy7Sf7jorYLVFpi6ZouJOPA_3MkwL3YERf7VCX7B8jkEipA1ypxq03uo8NBdKARxNqa-IPY9z_tggVXO8lZTHEHHon7CikQpw3qpsc1sQ2LlYRXi7Qb13jtHRHb-dTW_rbtYemFvhb335BCemTj_vSh9gsKYZk5sJwKr3nuZUeWvpDxPjarpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔟
بازیکن برتر زیر 21 سال دنیا در 5 لیگ معتبر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/90922" target="_blank">📅 20:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90917">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9qIbISXkPJg03gu3aKR9pLEaDDx-1_WGfnopdO23ZooaIOA_WPB3pkW_ZCC_M5-_is_0u0JXvegjS5CytEh-hLP0BMDYD4O1VhFXQ20FJwRi6-K6_c03u16a-qKJnwvO0lfXSUpkXVJJwngP2nnDHZH_OuQySqJq3MiuJcUmWrmrk8bz_Gwd053-fHerH7RckX9DreSM3uMndYR3qD0ox4VY930CksZavULht_cfDDnB77nc2tE0Dew-n4iuhhocd3-rXeAUJMfLNu9ZnC_3qF4gm9yTd62H-52Id0YZPSjPM01x7hOoV0fyWZWftvMDzh19lnNo9EJrvZ43JnTAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب تیم فوتبال ایران مقابل مالی.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/90917" target="_blank">📅 19:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90916">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad596a5f1c.mp4?token=PjwnOlvtnVsR5y4lZmpfaUqu-T-I7CHyBOxPTp8K5m96wnNxf_e8AkepP2MYWobwqU3k5HFHbnuChGkw-L6VoKXuSNjOkHeocU_vixvl75LvhCVUuZdYO3mvJNsMeGFdjWyp3V3CbzMimZgPEYvAf9tOfelaHh-9tT_E6cVP7xqSQbpEM7s3jQVh5BwG4_fg4zBln5eOQU2pytS93clxKFQGrS_Rp3RQ1niM4f046aQ06WzXK4WFBhkOdCvUoDxSMLnc_OZEdpf-3TzHtj3H29uCzl4BBLdFOxEsKfzVT3oyU1uuamNNeaUkrwkldzKuggl1DrLaUSY0h321xdwP2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad596a5f1c.mp4?token=PjwnOlvtnVsR5y4lZmpfaUqu-T-I7CHyBOxPTp8K5m96wnNxf_e8AkepP2MYWobwqU3k5HFHbnuChGkw-L6VoKXuSNjOkHeocU_vixvl75LvhCVUuZdYO3mvJNsMeGFdjWyp3V3CbzMimZgPEYvAf9tOfelaHh-9tT_E6cVP7xqSQbpEM7s3jQVh5BwG4_fg4zBln5eOQU2pytS93clxKFQGrS_Rp3RQ1niM4f046aQ06WzXK4WFBhkOdCvUoDxSMLnc_OZEdpf-3TzHtj3H29uCzl4BBLdFOxEsKfzVT3oyU1uuamNNeaUkrwkldzKuggl1DrLaUSY0h321xdwP2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه های فرانسوی میگن دزیره دوئه و این خانومه که از قضا بازیکن تیم ملی بانوان فرانسه هست خیلی بهم میان
😍
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/90916" target="_blank">📅 19:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90915">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🔵
✅
تایید خبر 3روز پیش فوتبال180: تاجرنیا رسما اعلام کرد که با هیچ شخصی برای سرمربیگری استقلال مذاکره نکرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90915" target="_blank">📅 19:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90914">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAqmtTJA2_bfZdBEQSAoZAKWdrJs74Q545UPaR6C01U7n1lZydnD7TauIwg7I_EIRsINhfgsCjJlI4cVciYiv4Tjrc90zJI1lOmJD87guEyyUtPA_h6KnJxVGDXK6MVDGoGYsPUPXIf7SyeXCjmep14fd97VRgeYcmW11p0aNROGlqQYTR0XHfl7OEymDYvkhucvzd15e9dmxXP8t8u0pJEz9FR4IkUSyJPbLnkvqbARdj_CfXIslXa7WlXBq6yxyfJgy4L9wfEXyC1pwpyfcncZsFtVfAs--_NzNWJT6B4PUYO6Eu7cbjJusFzkdHLrS-XNY-nUR1mrBZJ4mFYmCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180؛ #فوری
🔵
با نظر کمیته فنی استقلال، سرمربی فصل بعدی آبی‌پوشان سهراب بختیاری‌زاده خواهد بود اما برای این مهم، یک پیش‌شرط مهم قرار گذاشته شده است. اعضای فنی استقلال به ریاست تاجرنیا از سهراب بختیاری‌زاده درخواست داشته‌اند که یک الی دو دستیار…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90914" target="_blank">📅 19:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90913">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH6aGj6ZomxR566cAMSnB8Zx5hcDU2EK9NarniXXjO-U4x31SZ_SXWQKWLI5uf9rOO21cuQKye87sE_cSCgzPz4nujatAZH0MYhiAKjsf3kHDJIaQ_JN6uU70FA1EdcTKWywExfvZxK7L4OZGG_cMj62N5SewmaZmNU9L22knTdHZ7T8CvNsrtaGlqQFnIwAXQAtSdyWzwbu58t4s6AqcNfy_JRTlVrWrPb36bEByvdsQnA1KwePlktaTEzeBgAYdhJwtNir1bIEghffzN0AHGroFpiaY6k4AqecSZqOZlpL7skU06A1ogqknizGmZQwtkW3Upt7Zuuc1bOTsR1LCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوری: بنفیکا رسما تایید کرد که رئال مادرید بند فسخ 15 میلیون یورویی ژوزه مورینیو را فعال کرده.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90913" target="_blank">📅 19:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90912">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZlcz2jkBIvym6eQsC1XcYb4pntS16nK5HMiRGrSkhbJo0woG3v0vvOfFkPKnLhZ_ndNL3_B82iKV3I6VEkpJIHWAUaU5u2REzw7hbB86H4kxNYEy28sWtNfQX4gME7Nn6uinELzotnRvO9bBGlcZMOCKFHkgLdXUwflqfiiX0STSRS6VszkW-zKnWxgC_IAvz-PwspETUmsyK3V-Ik2BEIz3KPayMbCGvsghRQ4KBqo3PcT3jsMaLe5Lx4GDXMOsg0dewy23gftRnzA4gOjebVCx2rtFGRzcKFcK5aX5sRyXv8TyOAazu2V6hTsxLJ6jpl8qVoz5Zs09i_i3gAvpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الکلاسیکویی که فصل بعد قراره ببینیم.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/90912" target="_blank">📅 18:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90911">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjBeXBETa0dLzQ6yKPBokqxBx_RaXlQ0apAVzj77n7g6HQoLKSFB-LKn7ecgdiSJP3q8UZANAXOElUk7PjHiNM9Ou8jLw2Y0RtsnOauqbvgzPXNk1Yb8aOWnaSZmk-gyPuhnM0KHP8wU8C1m3VfF8mHybGJs4X-GTM7lYsmt0uKIVWpMV5w1S_pgQQWVXVC5gk5PRlHGQaccdDV7_rbz85MJCC174Nz2r4in_pzR5z70Jb2bjE6hczUdB_F4aUHY0vb6XTtp2I0qKt-6WN8IDR4wbik1S4Gu8XXigi2-IeBLPdcVuGGY8H28XyLku-xQdU3e1HfFQXg02Cadu1pzjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇫🇷
🥶
وزن عکسو تریلی نمیتونه بکشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90911" target="_blank">📅 18:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90910">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJRzL2fkmSKP36Gc6O3SMnkxTr8FukusCdjg0GTgUuQLXBPjmJoi7JfcxKimAX9wJewDkxcJIVfAVWy2ZSVOuCCqRf3Ep2qhelqFJsOTPOH2apCceRdmJ1fR_BZ_73UGnvavvN0HqsCna1opDFcD9Ck6PlS-Ew14sgA8yAa2nFhvAvOyaiJsgNUhsE4y4lJt2x7VAOy5JNntavdTy9wznuK-srxtaC81OZy0tHAf_1CdZc43yysmtTnonMMpgSnk85B27v4TTRUNTzRpWJMX4gxR6OAN1ea4gB_NWXkJPs4tWKFN8uohf8ov-iM7R1UfB6gmIWL80mjAdadouIQ1nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
خوش چشم کارشناس اسطوره‌ای و حرفه‌ای صداوسیما: به نظرم جنگ تموم شده و دشمن دیگه تخم نميكنه به ما حمله كنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90910" target="_blank">📅 18:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90908">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfbdfd3dd3.mp4?token=MWr5kcgfPp2kMBMx3Sh__dPHNA4dmb8iF6IyQ3Y3vKq1HG0GK9Ul5V_dV9KGiMCBYq86MaXPGdvS4Y0hg62TCh9qXt14ZEMwcoNKeVNXPpyvPI0vra9M7VFxXhzJpgqf17xvubyypbqy3I92l-wALS6vRm9vML1MFTMHuGa26GG2iJQfAZbxC15KT6sKdwPCYxBphsPlmRnL5XwUyrqYdgeyQH1fADrJATURAe0FQOPqjaIn890veiqHZH-8WPGZw0qVjtNB_UZDoSFpbA6KmJfwJKtxHgGeUpbF6aKHzwlYd3K1lZXURQ82NLUFmzgT9787gJt36fV9jQ8aLqqqyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfbdfd3dd3.mp4?token=MWr5kcgfPp2kMBMx3Sh__dPHNA4dmb8iF6IyQ3Y3vKq1HG0GK9Ul5V_dV9KGiMCBYq86MaXPGdvS4Y0hg62TCh9qXt14ZEMwcoNKeVNXPpyvPI0vra9M7VFxXhzJpgqf17xvubyypbqy3I92l-wALS6vRm9vML1MFTMHuGa26GG2iJQfAZbxC15KT6sKdwPCYxBphsPlmRnL5XwUyrqYdgeyQH1fADrJATURAe0FQOPqjaIn890veiqHZH-8WPGZw0qVjtNB_UZDoSFpbA6KmJfwJKtxHgGeUpbF6aKHzwlYd3K1lZXURQ82NLUFmzgT9787gJt36fV9jQ8aLqqqyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو زیبای حمید سحری از اخرین جام جهانی دو گوت
💔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90908" target="_blank">📅 18:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90907">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laUEZQW0mFK7rmKL7X68rHk96rL79o0aTD1cJRG_kQB1bHD6QPOI5uw3sNMqULR6cXmKFLEKO_ySJpNINbBsh8dexZDcskgzJ2U0dLzhcu3JmeeHcyZThYTKrmOcVXZmFgHxTjAkZlWZ8NFhaG4vn9C4lMEDpHUczjB1Rs613gRELVGf_RxKs7b5XPKiasyhPL950C7GGGo6SKbHaImQPONI2N4rsqUz8cKRblZT8AzGoQyp9qu-GXus9vPyJWVJl28UwEti3jkhGOcIHMhizi3W9di1aWt9booBYYt4blXZk9eJKN8_qagss6vaZmSdk_zik_0W3xFQeUr-uy-Umw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایرائولا رسما قراردادش رو با لیورپول بست و بزودی توسط رسانه این باشگاه اعلام میشه.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90907" target="_blank">📅 18:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90906">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXQ20yjmACcSkZxmEGvAzxwDUAGQfD5s_YgY3MyDW7qqx0w-R9gVChPYPXVtC8Bu4nw_RdjmkicmPwbe-1q1MejFHdaLP2rYiYbvZaLPqnolcIHycH_sx7tTZPkJFiU3ecna0e6DFhRBH0EZBnk0J3Mlp9F_Q4Os1X_ZDZoBT7sJQgbGighry1IIFKQWO5nn0bXxvYA758kRU1mpTR7BMVsq2YvN8X9XHEU2ZE4hWU_Y5JnivYxsuoh5MWt0Z7hGQTjeXdQO8OiRB5X0MqqyOLIWFMBfuiJIg_dR7VGwyBlAte0Q654mqkvBQmdzcwVhtMM_6DV5tAZzUM1gkWLMlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕
️
🏆
لیست شبکه های پخش جام جهانی در ماهواره یاهست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/90906" target="_blank">📅 17:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90905">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQeoov3KZ6R2cHkNwkrseMUmHQZ5rBqwcnr56KKot-N92SnEZhal6to40JOdXSTZUoW1oubWIiqMs5IGzOdf8mQ7WoeU4Md6TBPNqznmAfqZlxiwBuK5d8c0dASYb7RcUgrkwO6LiOsIQQN8K-TPn0ZpBuWMKXa1WpIQ2DVOI5SFp9BqJBPWIu-MgFJbTtpiGYPt_4MY8Uj1XyJFEu8cLFZiCOFLDU773CcmjHselU0Hs7zAOkSefzTUYNBVBm4ZtFp2i0RFhgI-JQmqLOiIkqfkIOmmP5_hQw3rA3YTaDfbEnuGCfJU3t-1NB2WDd5_PFOhwvIacTTOIbGgdsktAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕
️
🏆
لیست شبکه های پخش جام جهانی در ماهواره یاهست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90905" target="_blank">📅 17:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90904">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4e1409299.mp4?token=U5dxOf8Y2quHfZrQkAa04I4saQ8T9_JTVrHjbG9T7k2imTestgj3e6NkVub7KP26oagrjHrPTCs4sPcbFoZyQQFfzm-4VgloivBsCVeyz7CWqynRRQ7DwYkB_WDxa_HsKaya7x3mzwZdycNcMHD2r1eIhkR3PaCYunX5hkuQ_atG0T4tdlfoBZ6ATDM8ZsCTsWOJxsDo659qzRQAKnnPbruEfdySon8Jv99771K9lmqylfbi_VzU1LbBTgTe8HFN7nxEkXoOB_lBK-mnyPcqK9fQ9EX-gncWH_ZzlJzm4tCio-5atrRPlQPZxwe-_5EA1ermZoG7SohSm5pv4DMGSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4e1409299.mp4?token=U5dxOf8Y2quHfZrQkAa04I4saQ8T9_JTVrHjbG9T7k2imTestgj3e6NkVub7KP26oagrjHrPTCs4sPcbFoZyQQFfzm-4VgloivBsCVeyz7CWqynRRQ7DwYkB_WDxa_HsKaya7x3mzwZdycNcMHD2r1eIhkR3PaCYunX5hkuQ_atG0T4tdlfoBZ6ATDM8ZsCTsWOJxsDo659qzRQAKnnPbruEfdySon8Jv99771K9lmqylfbi_VzU1LbBTgTe8HFN7nxEkXoOB_lBK-mnyPcqK9fQ9EX-gncWH_ZzlJzm4tCio-5atrRPlQPZxwe-_5EA1ermZoG7SohSm5pv4DMGSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازیکنای فرانسه وقتی تو جام جهانی به سنگال گل میزنن:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90904" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90903">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4ab6aa38c.mp4?token=UVNtp3FFuqn_U6PROxuPv-KQIkjB0A6ykNeKWB_O-fYViG-zdWdO5bqTP1pt7jFPZWlJRkbN1ZgeF27ZjW8exuPQjFa3tC3x062E5MoESuR9nXltnlrigWBFF6PO9rNnrFCP98LYiVw67fCpEWBCA-EkShlD2S2w-Pp9cuvT7XP47cXJED1pBK84x5aVyNqBQsZhwijdolTfCjgrYUyN1e9RMx3cPMOApFeElxMC5tCSkS8tpFaKQRxTPhlqUvBxuBMu23G5erZ6Ew_g7rtvTbR-g-zOgPrPzJHsbHXbK2i21_52BGjCpcW9X48rzOXewK5ejrsxaahxfdafV5q-9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4ab6aa38c.mp4?token=UVNtp3FFuqn_U6PROxuPv-KQIkjB0A6ykNeKWB_O-fYViG-zdWdO5bqTP1pt7jFPZWlJRkbN1ZgeF27ZjW8exuPQjFa3tC3x062E5MoESuR9nXltnlrigWBFF6PO9rNnrFCP98LYiVw67fCpEWBCA-EkShlD2S2w-Pp9cuvT7XP47cXJED1pBK84x5aVyNqBQsZhwijdolTfCjgrYUyN1e9RMx3cPMOApFeElxMC5tCSkS8tpFaKQRxTPhlqUvBxuBMu23G5erZ6Ew_g7rtvTbR-g-zOgPrPzJHsbHXbK2i21_52BGjCpcW9X48rzOXewK5ejrsxaahxfdafV5q-9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفاع های تیم حریف مقابل فرانسه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90903" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90902">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iaxgsg0BY5mlA38nEtMrXzJQIApCJVliwKZInjtKOaUTRLbMelMB4eFRY9md77BDBnPC75DA-8ghvt1IvQ4erflpqeyfIlVq6KzjdsawWgVl7-MMHmCog7s0GzAH4cbDW5oHSrE5cxF4EQ_uOtYp6MpUnQ1bo99ucUTXpykndw5H3bmQr4uKpYnrPjMmh8l8G1ehp4csgSBloFioRsJQe_bN_MaqVbI31r4rPyMQZH08NytUreIRWZ_BkC3jC2rj4Ac3bI6b3rMZZFT_WQ8KVmOuw-bQso4VPzIl6AJMRAIi2HINjQzIlhSnsI3iQ_Jiu4OvVDDjGompoTtc01tvpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/90902" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90901">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZnxL1njXk8RyJACnn8B-tG6Otcq0UWIa_Kp3zx6Gcr4y-ChJ7IRC05VibRE5Q2xbq9dPIAi90E_kAA4RshQe1xUr6R49CbLMb8axDzaKiQ5IQRBbSKQAEM4qntRBWZOY3ogwCwxpKt3FNGcLjt3pGIOOGzJqmWqL2ca8OG2aiO7WJqqGf1hIFr2x6UNXP0CTWUwM9oQTx6zJQVLvYCkSkZIU_MBNmbGMIQS65-MsN9GBQO6hfuHwrtZqtsIdT6kDlgl_9ojWmC9FezvhutC4vWskhUBRsMPkmKmCnmO0KHrqDig5h7oPukwc1K_j5ObS_GKO73aekAfHlN5r-4FMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Out Of Context Football:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90901" target="_blank">📅 16:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90900">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1ebbd4911.mp4?token=gi4iPh530Pxmlyc10JenB5Qm6I9_9ESsKXSIgIp3A_4io-xYQzjdL5BrTjKRQ37DS-FPdTLYV2rXbNMTepDnSKRM-T5YIyVw-2qAEDmSU_xu4LCzDAPT1kv72jmmXdmHi28sRg7cxx63AHn27fHqaGi0mnstmPBcJjfZxIR0LZ6NI42TT02RNMDHwFCJKWL8igNpky2DWM1iKXpI79M2tZJRA7FBdk7ufb0EbpOLZOXnCHY8fbKuEw2wLZkw6Qa0wQ-Ort9WRIcuXZm4yn2Cyf3lpOGQwgjOswYKwh1GozDTYRYoJSQCQ2ZSS_fvzIAZFRqWCoVbYuPKDu_5o0B410044lNVMJezSr1K4wIt4VJN2Rt6IQspqrEDNgDCiW0OC1xy0v4pECSJkeg7teFa9r7oqyJeSu6tgYwNoj08DKLghUh7DZ_nqW2gGggmFro4-ulDMYc4Y4tV4RNSh-zKCXMCQOIDcGrPvFsGU3PJxs4nI7rYJongFckX96UrVxz4tMUEWV7xPzkic_R_HNwtLsxPCkek4hqaR3g-KYKYL8AuLMH3MQrL_rSnEr7133oa_LhpF_Cm24RzaoVvyRE-2r9Wx4POqxt8gvCVUYgv6yusLEXtRedlWzT2isj2jwxMLsOQsJXQbkobQa_QLCt4Ye1h_WhaWR8V30lH9Xn4YDE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1ebbd4911.mp4?token=gi4iPh530Pxmlyc10JenB5Qm6I9_9ESsKXSIgIp3A_4io-xYQzjdL5BrTjKRQ37DS-FPdTLYV2rXbNMTepDnSKRM-T5YIyVw-2qAEDmSU_xu4LCzDAPT1kv72jmmXdmHi28sRg7cxx63AHn27fHqaGi0mnstmPBcJjfZxIR0LZ6NI42TT02RNMDHwFCJKWL8igNpky2DWM1iKXpI79M2tZJRA7FBdk7ufb0EbpOLZOXnCHY8fbKuEw2wLZkw6Qa0wQ-Ort9WRIcuXZm4yn2Cyf3lpOGQwgjOswYKwh1GozDTYRYoJSQCQ2ZSS_fvzIAZFRqWCoVbYuPKDu_5o0B410044lNVMJezSr1K4wIt4VJN2Rt6IQspqrEDNgDCiW0OC1xy0v4pECSJkeg7teFa9r7oqyJeSu6tgYwNoj08DKLghUh7DZ_nqW2gGggmFro4-ulDMYc4Y4tV4RNSh-zKCXMCQOIDcGrPvFsGU3PJxs4nI7rYJongFckX96UrVxz4tMUEWV7xPzkic_R_HNwtLsxPCkek4hqaR3g-KYKYL8AuLMH3MQrL_rSnEr7133oa_LhpF_Cm24RzaoVvyRE-2r9Wx4POqxt8gvCVUYgv6yusLEXtRedlWzT2isj2jwxMLsOQsJXQbkobQa_QLCt4Ye1h_WhaWR8V30lH9Xn4YDE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاراگوئه هم وارد چالش معروف شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90900" target="_blank">📅 16:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90899">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvulhqin7OwujodyuJcq9vNd9ZCLUzqTfwylYvSKY7NCGfqUqlsUTHPRPKb1b2H6aRfO30-pFjwy0NoOYbh91P_2EzPaRDaVhMYhTSpcw-Cei1L-xd3xgrQteL7E9wnN62A3wUdaabW_7Jynq3k5w6bePk1iu7Vj7wEZ7X4DESh9yWM-bBIJO6agCh3SJ6anABz7Wituo2xgZDq7khxk6I5m5lNyxEqYTOugKR5VQF6NOXNaY2Q60ysfaD2raj6HqrAX7ldq_Rlbex6OGGOFfrznE_wnNCIKp1-dJzoDr8pTHBBF4gy5qeNM-yXr-VJOzlqpBac9fI_f_OOf_iZ7Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
👀
#دانستنی‌های_جام‌جهانی
🇨🇻
فقط یک یادآوری که کیپ ورد برای اولین بار در تاریخ خود به جام جهانی فیفا راه یافته است و چیزی که این را حتی خاص‌تر می‌کند این است که آنها دومین کشور کوچک‌ترین در تاریخ هستند که به این دستاورد شگفت‌انگیز رسیده‌اند!
🤯
👏
🇨🇻
🌍
کیپ ورد کوچک‌ترین کشور از نظر مساحت زمین (۴۰۳۳ کیلومتر مربع) و دومین کوچک‌ترین از نظر جمعیت است، با تنها حدود ۵۲۵٬۰۰۰ نفر، پشت سر ایسلند، که به جام جهانی راه یافته‌اند!
👀
برای مقایسه، هر ایالت در چین، آمریکا، هند و اندونزی جمعیتی بزرگ‌تر از کل کشور آنها دارد… با این حال کوسه‌های آبی در راه بزرگ‌ترین جشن فوتبال هستند!
✔️
💥
و این اتفاق تصادفی نیست! کیپ ورد سال‌هاست که چیزی خاص ساخته است: دو بار به یک‌چهارم نهایی AFCON رسیده‌اند (۲۰۱۳ و ۲۰۲۴) پیروزی‌های معروفی برابر غنا، مصر و کامرون کسب کرده‌اند.  بازیکنان با استعدادی تولید کرده‌اند که در لیگ‌های برتر اروپا می‌درخشند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90899" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90898">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3257da74ef.mp4?token=i27EqXvqWBD55WV7s8WClOyyNhPRhK37lNl4TYcQq_XjV5UCZN5SlpP392GFTdtkeUz1gf5zbmcwY6EzOPj9ghej3ufKfBu9Wn8L0sUzxYMLjzynhqt8kWZ4912brTFH_Vpp_DeuvXqaknX1KjhB6TsIhEaJi0blS8jPptmVtCUDHclHn6mOo-Sck0agw1sLJhE7sx7j7m5Qa2f2QdnhcPlYqfJ26RsW7znSk9hE44lg5p_FUuA9waIWPiNdkIyg2E1J98rUbOzFs-1m7sU1TD5KLSj_XY5GdubfIuLFmg7eot6sCnDPl4thngJGQrgTeGJ8o5CrT9ZYB2krfz6gZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3257da74ef.mp4?token=i27EqXvqWBD55WV7s8WClOyyNhPRhK37lNl4TYcQq_XjV5UCZN5SlpP392GFTdtkeUz1gf5zbmcwY6EzOPj9ghej3ufKfBu9Wn8L0sUzxYMLjzynhqt8kWZ4912brTFH_Vpp_DeuvXqaknX1KjhB6TsIhEaJi0blS8jPptmVtCUDHclHn6mOo-Sck0agw1sLJhE7sx7j7m5Qa2f2QdnhcPlYqfJ26RsW7znSk9hE44lg5p_FUuA9waIWPiNdkIyg2E1J98rUbOzFs-1m7sU1TD5KLSj_XY5GdubfIuLFmg7eot6sCnDPl4thngJGQrgTeGJ8o5CrT9ZYB2krfz6gZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
‼️
رضا شاهرودی: علی‌دایی به مادرم فوش داد منم باهاش دعوا کردم
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/90898" target="_blank">📅 16:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90897">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cb836e7b3.mp4?token=Ah0qwRruhfidLnUh7kVM4u0UdzwT12JbKCBg1YGTizdGKGBweAf33Dp2FjCDYzHhxL0SqyW4zkbjh-pz5UojjuebOloB07-nF5pt0Rz4g9bpu5TXUEcj_fBIzhDcKZsizERr--CCsc5eI3FjgSAxweTEkq7eCWUin7UnpRqpaF2LtF87fhEYqfx6syyZDjUFG5AX1djHycrbDxx1HstkFfBXKu3xl1gKHxU4L15jdzSkZhA7B7W-xATde_3pfZWkvhACSaW2oPCTRe8n43WJKYol4MuCmgraEk6Q_3fA-2GoUcn-KSKFKOMB40lLSkHQru7lE52iJ8y2sv794e3VRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cb836e7b3.mp4?token=Ah0qwRruhfidLnUh7kVM4u0UdzwT12JbKCBg1YGTizdGKGBweAf33Dp2FjCDYzHhxL0SqyW4zkbjh-pz5UojjuebOloB07-nF5pt0Rz4g9bpu5TXUEcj_fBIzhDcKZsizERr--CCsc5eI3FjgSAxweTEkq7eCWUin7UnpRqpaF2LtF87fhEYqfx6syyZDjUFG5AX1djHycrbDxx1HstkFfBXKu3xl1gKHxU4L15jdzSkZhA7B7W-xATde_3pfZWkvhACSaW2oPCTRe8n43WJKYol4MuCmgraEk6Q_3fA-2GoUcn-KSKFKOMB40lLSkHQru7lE52iJ8y2sv794e3VRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇬🇭
حرکات موزون و عجیب کی‌روش سرمربی غنا در تمرینات بعد ریدمان‌های اخیرش
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/90897" target="_blank">📅 15:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90896">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkImg3gRLkAmazc5NLKNMSlnz7ycxj55E4b08yVpmGWx1TlrJ_ruHjl0KNtXTqUDhhGOPzbFz8wQCcdosH_rHt_NQ8IOFCY0ckYM73DHMsZDlV2mLfnMEULxspiW3EM5AgJ1-ykImskEwU2qelTQo5mZ7pTvlL6vp7_cdkMAveFOT-aJH_alwu2hAxLqO9ky4O8k0UpXjJNg9wTQowmJcspQ5xNTcqLuR9jYw6iJuwJ5pkGujF1Jip0wttLgq-JsH9wkk_VvZW1fK71lySrE5wdvR4zSTiZctq_crG-xaQ0xofM1jqmioqeiQZf0TNvwbQGgTqu8zxJJ22Sxfp00Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه ادوات بازیکنان نسل فعلی فوتبال و گذشته؛ واقعا نسل‌گذشته چه کله‌خرایی بودن
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/90896" target="_blank">📅 15:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90895">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d49121b221.mp4?token=kv7YA0_ioYwznGAGL8vZytJMOSHKqrIZbxDLqTIvApJ4fYcneaHal79TdwwwdSD7NyMm5kl_X5QLt1NswqfMIsdYTyG2d7V7Y9RTwlxQTCp4aQnr3hWyVe_y7MfztiuOxTl2HEOzUOEEYFjT-5SXOAphkOP1p-c_PhcIoYgvg809eUNsY3SPmwp_kdNTcXT9bHTarr2Mi2u10hjQ2exuW0Nlc3Nl5vJvpFDHG84BNdYbUbgx7FbhdCXAGBofv7GOao66J4G_6PMV1DwMAamb7LpWEqpGzJSBh1k7DG_Tx2KSRVLqpnj1QkJTQXVSP6aXp1LI9PApRgux8owSStO-8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d49121b221.mp4?token=kv7YA0_ioYwznGAGL8vZytJMOSHKqrIZbxDLqTIvApJ4fYcneaHal79TdwwwdSD7NyMm5kl_X5QLt1NswqfMIsdYTyG2d7V7Y9RTwlxQTCp4aQnr3hWyVe_y7MfztiuOxTl2HEOzUOEEYFjT-5SXOAphkOP1p-c_PhcIoYgvg809eUNsY3SPmwp_kdNTcXT9bHTarr2Mi2u10hjQ2exuW0Nlc3Nl5vJvpFDHG84BNdYbUbgx7FbhdCXAGBofv7GOao66J4G_6PMV1DwMAamb7LpWEqpGzJSBh1k7DG_Tx2KSRVLqpnj1QkJTQXVSP6aXp1LI9PApRgux8owSStO-8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🙂
شهروند لُنگ پوش اصفهانی امروز کف زاینده رود: بنده را به ریاست کل بانک مرکزی منصوب کنید تا مشکلات اقتصادی مملکت را در اسرع وقت حل کنم
😐
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/90895" target="_blank">📅 15:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90894">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👍
از معدود خبرهای خوب ممکلت اینکه پس از ۱۱ ماه آب در سی و سه پل جاری شده و مردم اصفهان بسیار از این موضوع خوشحالن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/90894" target="_blank">📅 14:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90892">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6039725c3.mp4?token=KQRncou7pudzOefVGTT7Hnfovt-iQrm6X4lgDTrgC4vFMFVhn4eVeQKgfVJxuLd3dGWx8lXiSe-NYD7XVwT7pvDbppBifXz9dgC2Bq_MIg-6RY75uGGhXdyhBIKXWC1gRUdU8Ps5GYS54Y6o_jI3MEWzwNlqvfUSrK_X_GNgO6gEDFvM5-eV6DWBE9zxX4FLcTVREr3cD47-df2wmsnzPWf51vvcYAj0OMREy2ONdZV9su4TL_-9GKoWX-vGIbGpCNU9QW7Mn7sdif4doiDOyRreHSVZwAv67EqQ3VaK2B4n_eAFNjV5lgX7cjsR0MorTMD_fiFnBEW1iwV3jc_VhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6039725c3.mp4?token=KQRncou7pudzOefVGTT7Hnfovt-iQrm6X4lgDTrgC4vFMFVhn4eVeQKgfVJxuLd3dGWx8lXiSe-NYD7XVwT7pvDbppBifXz9dgC2Bq_MIg-6RY75uGGhXdyhBIKXWC1gRUdU8Ps5GYS54Y6o_jI3MEWzwNlqvfUSrK_X_GNgO6gEDFvM5-eV6DWBE9zxX4FLcTVREr3cD47-df2wmsnzPWf51vvcYAj0OMREy2ONdZV9su4TL_-9GKoWX-vGIbGpCNU9QW7Mn7sdif4doiDOyRreHSVZwAv67EqQ3VaK2B4n_eAFNjV5lgX7cjsR0MorTMD_fiFnBEW1iwV3jc_VhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چالش بامزه بادیگارد مسی و روبرتو کارلوس
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/90892" target="_blank">📅 14:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90891">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuPQjtIsORYffOqFAHqYsQv8S8rf2YPPP6toAIswEwAYwxKRnxFBNOjuRPg55F-csAaf34mxsZlNmXe4QnunY0v99B8ZHmguLUrM4TSghqNAW0NoHpBbDhqWZfSsFpRbp5scw680mAGfRtfE121zF6wzOe0up1KGa1E7PF0QxHTnYa1PXHTbDjJ3jNO22ktbGH_4qRvul1S917ZDndMumix0-Q8y5RCxp1t_vENi3AnDSjiMb7mKkotYLh0zASZ1Kt_je17u0vrK1PmEgIEIoOo3suR4R45g50RlCTa5rgUQ5aNfHw5NSwcksKIDMIXej8qoQBC6Sytkk6mMppaMRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب در حالی ما با مالی بازی میکنیم دم گوشمون عراق با اسپانیا بازی دوستانه داره!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/90891" target="_blank">📅 14:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90890">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔥
🏆
فرآیند جالب ساخت کاپ‌قهرمانی جام‌جهانی در نسخه‌های کوچیکترش؛ خیلی دیدنیه از دست ندید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/90890" target="_blank">📅 14:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90889">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c49acd8fa4.mp4?token=MCB2NHjqCi3Hmhkvj5VFNBspjKVweCkjuVgbfKuvNkgFx7uiIJe3-xLwA-uZMe37OnAmGW1195VIVvHNep0w7IwsUTTWWDq9IJga7ffCO1otrWKQtfnnhCJRIs43H_K21w_BDzvEguHHw0rexZGk85g6YbsVTDBqDQfpKyV-PBn9Rpxic__O0cUhFts8OxJeZrcfpXBE3WSVOOGK51LYS2x6CD618t8w8ZZThcFslFtzXFr9a_-su7oPqtgP7Xl-yt-0oM_8_t8C-sezqQ0i4UXtEi0wRCmN8AFPNPd0AcJaNhg34To7cWcA70Gx0uCuQy29Kll15i8-nq5eE9FdsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c49acd8fa4.mp4?token=MCB2NHjqCi3Hmhkvj5VFNBspjKVweCkjuVgbfKuvNkgFx7uiIJe3-xLwA-uZMe37OnAmGW1195VIVvHNep0w7IwsUTTWWDq9IJga7ffCO1otrWKQtfnnhCJRIs43H_K21w_BDzvEguHHw0rexZGk85g6YbsVTDBqDQfpKyV-PBn9Rpxic__O0cUhFts8OxJeZrcfpXBE3WSVOOGK51LYS2x6CD618t8w8ZZThcFslFtzXFr9a_-su7oPqtgP7Xl-yt-0oM_8_t8C-sezqQ0i4UXtEi0wRCmN8AFPNPd0AcJaNhg34To7cWcA70Gx0uCuQy29Kll15i8-nq5eE9FdsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
چالش جدید هوادار رئال‌ با موزیک ترند شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/90889" target="_blank">📅 13:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90888">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C31pbG1yvUtARG6ADVJ23Fr6G5IWEMPrvmzS_dgNaNZM-fk4rpxPMmivhcMrYs2_1ItNsH_uFJLzUanaDb_Vzo_Dfa8rOy9tOeGz-TvXXI8_R8YAiIpeXe1AgCypypw72ZihIvA0Wo6XqZutywuqsnyM_Z1qlSSv7DamfGCbqUp8_WLYAYKUuiAHHl_z-HcGJ2UeOdJYVA_3pE51OEg75UQuKzKKz9vNH2PlTkvZAK13YIlodX1Xary1Qt-TbbGPvU23APJUACfYxrTY4zSTMnb5sQ_ZJsw09sK8DCk1SBfa2S-MsOnF55kIYxJKStvG6EI2GtP8MOjsUX7havEwtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
📰
#فووووووری
از اسکای اسپورت:
🇪🇸
بارسلونا نخستین تماس‌های خود را برای جذب آندره‌آ کامبیاسو آغاز کرده است.  این مدافع چپ ایتالیایی در فهرست گزینه‌های باشگاه قرار دارد و مذاکرات اولیه برای بررسی شرایط این انتقال انجام شده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/90888" target="_blank">📅 13:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90887">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری
؛ با اعلام نیکولا شیرا خبرنگار سرشناس ایتالیایی، قرارداد ژائو کانسلو با بارسا دائمی و تا 2028 تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/90887" target="_blank">📅 13:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90886">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvCJQV0Eu5jhrTINrGJ8jR6oYulJ1W5hLSUgZA8Uo8szKt1N7l8AAIrn0AJA6XffMZTWIYhdpAP4nnuXv2lzADbBeyfDWsOIllcOPwtxhqYqZg7eXxh_kEzsBY1UiLDJtqVhFewICysGTm0fMSQ2YX8hOI1PCiXGV_AcpQjGQwowF34iNuzDstuFcaki8tzYODAEuBldQddvBbMybbS0eCSu2V2DJQNB4iiyomx9as-fABy57LpXn_8IBqK9UttIMmNwPgmJoIcQSIr5IXg0N3hj6s56ZluuejdgsZZaFT43i1AInK2s5R-1rGcGZZJs26kf4qETjYUzof33LCm_Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
جوانترین مربیان فعلی جام‌جهانی، نکته پشم‌ریزون اینکه سن نویر از ناگلزمن بیشتره :|
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/90886" target="_blank">📅 13:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90885">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
اسپاتیفای رفع فیلتر شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/90885" target="_blank">📅 13:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90884">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOTn2tQg_whUJcSHLgjKZ0gloB5FRTWTwCgKXlihuJ4YRe-nFM-oK0z34nWZUGWEo6rQSHxMoR3KG1Zby_lteo12-1SwWoEuHsOJDmR5Fk5W7S6z0A9TxINi6NvO37IAcPDIkyCjWT_xSHdl_OQBVKoCgTEpjMIuWqvvSAJmHkDqwQtSZ5pyesB46VDXjkYENSDtLW6lnU63fnoG0-kYBaCfvBQrjYsGR8LWOF3EFCYO0EMio1e0DwYF8Zqsa8BwX5NCp9IawMun3rUz30aPCkbcWQCvEYvwmNGDhrRhzodEzG5T0h8Q7M-p-YaDNo6XW07RJLpjaELvyQqO_QHCgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|تاتنهام بدنبال جذب ساوینیو بازیکن منچسترسیتی رفته. گفته شده اولین پیشنهاد تاتنهام رقمی نزدیک به ۴۰ میلیون یورو هست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/90884" target="_blank">📅 13:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90883">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0d6510.mp4?token=KKP9SJILye4g6LGhuS4ppCLSM2xWte5CjGN_sx9mqSkjNb1tfI1vYh229SauyZpiDUhdSVIKZO5Ifx24c2RPWdkMJ86_Dsfup8nQpPJF3whLJy96omjZr7eXSalTXkJvE_v43uO_tkc7hcpRGGdtsmy7S1W7pPoqnPgZFot9kMNG8dvEc9-g4FKZkfqshD9zpso6ShnayJtrzNWaDejCELbmVeyd3_1G2G9GC2iCmAzR1FPUUGpwaP9kQwfPb6mtDKXgYGo8EtCJSLwxjtSCvjTG7N9rPQIRVGqzi9j1ZCyWjNjE4UUQcY-9zVzwvmSOb3iF68NGXdtdS4CrIKwL3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0d6510.mp4?token=KKP9SJILye4g6LGhuS4ppCLSM2xWte5CjGN_sx9mqSkjNb1tfI1vYh229SauyZpiDUhdSVIKZO5Ifx24c2RPWdkMJ86_Dsfup8nQpPJF3whLJy96omjZr7eXSalTXkJvE_v43uO_tkc7hcpRGGdtsmy7S1W7pPoqnPgZFot9kMNG8dvEc9-g4FKZkfqshD9zpso6ShnayJtrzNWaDejCELbmVeyd3_1G2G9GC2iCmAzR1FPUUGpwaP9kQwfPb6mtDKXgYGo8EtCJSLwxjtSCvjTG7N9rPQIRVGqzi9j1ZCyWjNjE4UUQcY-9zVzwvmSOb3iF68NGXdtdS4CrIKwL3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
چیچاریتو مکزیکی تولدش رو اینجوری به سبک چالش ترند شده فضای مجازی جشن گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/90883" target="_blank">📅 13:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90882">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6tl-Jp4OvMFvZ7fAQztMCY8UVuoSUPfgtg-eRIApQ-xBvfzA8zQbtTvQNlM6720vfVAh33k3Yi5tfHcjM9GPoEzydlr1Nn3ZtKxajp6VIYNYzNBW4F4vDXDUBDzKZFA7uBIC3FD7Q19iRGuF-hLvoUA-yFTO2i3eXasNxX4npMICqLG5tg8fZ0S32nowQ12GY9kA8WcgF77NF-Og59fPPD5HPYo1AeHvwmZL_ICObaZeRy1D4_Ef5yQi_BXFmTGulHXky5EoRvtgnAD18-2nrsucOLrX66hIt7cg85nNrrxwIfZVXFM4o_jsFVxAPlOgJRPp7uLxwdsPC_fuCn-Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رتبه اسپانیا تو ادوار مختلف جام جهانی‌
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/90882" target="_blank">📅 12:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90881">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/017a14deff.mp4?token=YJMQQSW4jvxVSk9p_z15-uyFk36kZcoR9JZsayRNhv7p377M9BVNyjsn6aGAhYcAWDm-031P3X_c9rnGImqFpgf8U2saLrfD1-gO_-05t7CubdSVPl52Rs1yE1pVlKxlgHAJVAumTIaVZ9s3lSUzo8La20rS2AqEIP_6-4QoJY-zSc_zrCgOXz3PWPp7RcadHCL3OS0n2i0NgKCQe4eIiL1dhcLm5YXjC0WD9mlNK9z_tbFmzXpMX1sx_fpzMCZfC7OhuBwfhS-QtN5ihq1XAcWVM2Oa4vD52VwoGBBfmkbbft8lUP_S5Cc9m_AkYtvjwsvmj_TkHkeAdmAv715t4iZDprrBdl_28q5Dp3W62Fq-YfKG26ZlEq4OgbI3LjzXq8JzfmoKZVq8_n0j4poAkgpDjYDl7xF8-no0uW2QXBwHyPZOfexENIXXzv0RJknK2LDI-L7xpHVYPHFDa2IB269UHIyZhNSWSclRTfAlk29_pqC5CJzU4mP2DrLW9_8NL55MEaXXX3Jit20JG2_7dbYASBcH86VY1IuSC3u8fvegmfhwve8BqN4T2zUGaDH8LbfMrD1xpax4Aabjasge8fqw6yjTvsqOWfQJmIT_HUidBp-VqM5kKMfUAa5EyWcK64YmLurSohriEoKjamNAg0tMppwOcDWhtTbLTVyq_JM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/017a14deff.mp4?token=YJMQQSW4jvxVSk9p_z15-uyFk36kZcoR9JZsayRNhv7p377M9BVNyjsn6aGAhYcAWDm-031P3X_c9rnGImqFpgf8U2saLrfD1-gO_-05t7CubdSVPl52Rs1yE1pVlKxlgHAJVAumTIaVZ9s3lSUzo8La20rS2AqEIP_6-4QoJY-zSc_zrCgOXz3PWPp7RcadHCL3OS0n2i0NgKCQe4eIiL1dhcLm5YXjC0WD9mlNK9z_tbFmzXpMX1sx_fpzMCZfC7OhuBwfhS-QtN5ihq1XAcWVM2Oa4vD52VwoGBBfmkbbft8lUP_S5Cc9m_AkYtvjwsvmj_TkHkeAdmAv715t4iZDprrBdl_28q5Dp3W62Fq-YfKG26ZlEq4OgbI3LjzXq8JzfmoKZVq8_n0j4poAkgpDjYDl7xF8-no0uW2QXBwHyPZOfexENIXXzv0RJknK2LDI-L7xpHVYPHFDa2IB269UHIyZhNSWSclRTfAlk29_pqC5CJzU4mP2DrLW9_8NL55MEaXXX3Jit20JG2_7dbYASBcH86VY1IuSC3u8fvegmfhwve8BqN4T2zUGaDH8LbfMrD1xpax4Aabjasge8fqw6yjTvsqOWfQJmIT_HUidBp-VqM5kKMfUAa5EyWcK64YmLurSohriEoKjamNAg0tMppwOcDWhtTbLTVyq_JM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
بی‌بی سریال متهم گریخت پس از ۲۱ سال
🥲
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/90881" target="_blank">📅 12:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90880">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/225f01016d.mp4?token=VUm-SgxMCTK7D5FJE4wvKL6Wvh-Kn6tcAjB3Und4kRcXJMpzWc5JvNFmy4boW3iUsUqc86GgPoztoNPI96FcmZJfDouLkCxuU_tENci9WRPGTjEe_bkJeAdAKQGbZjaZjcH_07xxYNTglz3aZaoa5hdReuqpIfoxVW2UcVlhYq4Kb5z8jncjDOiq0r_9knXQaZR4aASsXfAy9sq_wlf7RGrfMBrlh8eewNUktEXuxjKkNHtBA23cEFCshcRQx_hmdC3iybr89pMQb3lY5aghkA615P5MrpjF_NQLppHd0OmrqwhZ7Zurr4DynERCiEGL6IxCTAbQ5sVpHTtEnRH8zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/225f01016d.mp4?token=VUm-SgxMCTK7D5FJE4wvKL6Wvh-Kn6tcAjB3Und4kRcXJMpzWc5JvNFmy4boW3iUsUqc86GgPoztoNPI96FcmZJfDouLkCxuU_tENci9WRPGTjEe_bkJeAdAKQGbZjaZjcH_07xxYNTglz3aZaoa5hdReuqpIfoxVW2UcVlhYq4Kb5z8jncjDOiq0r_9knXQaZR4aASsXfAy9sq_wlf7RGrfMBrlh8eewNUktEXuxjKkNHtBA23cEFCshcRQx_hmdC3iybr89pMQb3lY5aghkA615P5MrpjF_NQLppHd0OmrqwhZ7Zurr4DynERCiEGL6IxCTAbQ5sVpHTtEnRH8zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دهن سرویسا چی میسازن
😂
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/90880" target="_blank">📅 12:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90879">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d81d6976b.mp4?token=bkCIwODZA8xSxDI9rATreXZMNKVVVlT8RLCVG2qtw-JVdfDR_c7Fv3Zg9Y2JDpJeAUgmo0k5ajcrf5wJNYkdJagoV7N2SPSBxc4GSZ1UM_Itss4a7KAwpFs1eFYNPnnalz2E6qNvtdrsmHw6Env3KTaKQVNDolF8RTFZXKQHj5Z-soviSXm0nD4F-FjT0C-hOa1Xzd_FEeDCbGUaw3LThp1IqUTqEn5Yl2_BrxS7F7ntZpWLUqyjz29RZF2O2m-gLek8x9S14nnn8Ysf7g-7o7MWix_Yg2d5QOhO7QBANk_7FLtYkk55Hhu5UrFzPfpYKTybv2X0KbBo7mdtaxWgVpZt3KiwxjGNDH4390jAjVrwRtqdmTl5-G6533Ps_z11xkAaDBE-1uODF5sJtt-cG356QhRpNX1i6AXB-3UKt9hSbU6c7Kp46XpsiULrMMTbsFHZ9I5aZg6pFfblXaPWVYsYO1wPuH1QxWhgdsdnz2ECKyjHGG2W01SJX2_L5oR8o0DhUnu_0wuVmFdzSCmaO82mf3N0t0aoJlv5QmOZin-XsjLDRYgI5BmIIMQhno-So4-jxbmaDVAQgNWLqtFWCfgJ3pfuZl-AOjX6CBxjzlmXw4HqCdN0BUfTQHSnszUCm2O2LsHGCSDUgbRJTlB2kSWwJxuA9p7_8B62rvTGMS8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d81d6976b.mp4?token=bkCIwODZA8xSxDI9rATreXZMNKVVVlT8RLCVG2qtw-JVdfDR_c7Fv3Zg9Y2JDpJeAUgmo0k5ajcrf5wJNYkdJagoV7N2SPSBxc4GSZ1UM_Itss4a7KAwpFs1eFYNPnnalz2E6qNvtdrsmHw6Env3KTaKQVNDolF8RTFZXKQHj5Z-soviSXm0nD4F-FjT0C-hOa1Xzd_FEeDCbGUaw3LThp1IqUTqEn5Yl2_BrxS7F7ntZpWLUqyjz29RZF2O2m-gLek8x9S14nnn8Ysf7g-7o7MWix_Yg2d5QOhO7QBANk_7FLtYkk55Hhu5UrFzPfpYKTybv2X0KbBo7mdtaxWgVpZt3KiwxjGNDH4390jAjVrwRtqdmTl5-G6533Ps_z11xkAaDBE-1uODF5sJtt-cG356QhRpNX1i6AXB-3UKt9hSbU6c7Kp46XpsiULrMMTbsFHZ9I5aZg6pFfblXaPWVYsYO1wPuH1QxWhgdsdnz2ECKyjHGG2W01SJX2_L5oR8o0DhUnu_0wuVmFdzSCmaO82mf3N0t0aoJlv5QmOZin-XsjLDRYgI5BmIIMQhno-So4-jxbmaDVAQgNWLqtFWCfgJ3pfuZl-AOjX6CBxjzlmXw4HqCdN0BUfTQHSnszUCm2O2LsHGCSDUgbRJTlB2kSWwJxuA9p7_8B62rvTGMS8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای دوستان گشادی که به هر دلیلی باشگاه نمیرن و ورزش و سیکس‌پک در خونه میخوان
👆🏻
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/90879" target="_blank">📅 11:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90878">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARoW9lAPbEdwnj79tDLFsouuX8u3t7Gyw5Wp2wJvv4H4bTiWEPCiRs09acXUnRDqVE-FPtP3fxXjvYJT4Kevdeo49arcBT0x0CTM0dxxpbPm3SSsiGSOLoLVFIMWt6i3cLQNkzvdyX62Tm_3usH3lmEb08ESgR_CBxokX3xml_I5-VwPuFgQ5i6qd9q_GegBf15FVOWC5Pg_KZu_ecLhqYxqGv80ESFl6_7Gjn55boqQUiylbW-V1PtKhrEVsQDzfS-VcnmLfY8lyAfSRvvnqXucfWMAiGS5IsRXEdn7dXYJXAMiKTDcIa_OOedo6XxRav5iQYkChVwWboc2Y6HqgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتلتیک : اگه تو جام جهانی در فاصله 13 کیلومتری ورزشگاه رعد و برقی ثبت بشه بازی به مدت 30 دقیقه متوقف میشه اگه تو این 30 دقیقه رعد و برق جدیدی ثبت نشه بازی دوباره به جریان می افته
در صورت ثبت رعد و برق جدید شمارش 30 دقیقه از اول انجام میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/90878" target="_blank">📅 11:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90877">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da40b1eeeb.mp4?token=v0Q5LKcNJ4vI-9z1uVEhghU7Skh4BhH5MeEomy9J3ihqjnJwkDjsjJ0OSvDPGYhcdboVV8uLLCVtlsC9XdI1MTyMEirqchg0bdjVjpnPI2hHeliiMaXWBcbHvqygd8xVD-IcGGP0Kbo1-68KN8yPhsIMokevm7g0pNHfkBbkDypLL2UrjkLZeiOVtCzKQY4xG5PxZ6Zl8BWhkps2AQxSDCGkHxWIo7wY7TkTyK0EgtKX6TyFiXpZEisfHBd50dUC5hyao7dF1rJA-ZXnzE1R3HdLxIDKgZQtNaxo3NDgsxPXy11KVKVZ-9IL8W7pPvXjB0Vhuzf7GsakVhwigGjKMYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da40b1eeeb.mp4?token=v0Q5LKcNJ4vI-9z1uVEhghU7Skh4BhH5MeEomy9J3ihqjnJwkDjsjJ0OSvDPGYhcdboVV8uLLCVtlsC9XdI1MTyMEirqchg0bdjVjpnPI2hHeliiMaXWBcbHvqygd8xVD-IcGGP0Kbo1-68KN8yPhsIMokevm7g0pNHfkBbkDypLL2UrjkLZeiOVtCzKQY4xG5PxZ6Zl8BWhkps2AQxSDCGkHxWIo7wY7TkTyK0EgtKX6TyFiXpZEisfHBd50dUC5hyao7dF1rJA-ZXnzE1R3HdLxIDKgZQtNaxo3NDgsxPXy11KVKVZ-9IL8W7pPvXjB0Vhuzf7GsakVhwigGjKMYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پشمامممممممممممممم؛ اشتراک تصاویر جوانانی که در کالیفرنیا زانو می‌زنند و ۱۰ تا ۲۰ دلار برای نوشیدن جرعه‌ای آب‌میوه از انگشتان یا پاشنه پای دختران جوان می‌پردازند، در فضای مجازی سر و صدای زیادی به پا کرده است.
😂
😂
😂
😐
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/90877" target="_blank">📅 11:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90876">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برای توضیحات بیشتر: قرارداد هالند با منچسترسیتی تا سال ۲۰۳۴ معتبره و بند فسخ ۱ میلیارد یورویی داره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/90876" target="_blank">📅 11:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90875">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ax9vu1EzfENjOMmRPaK95EJLr7r_2Fpo2H5p4uOY0veZW0A9UmvYzozP3ILm5FocbwWn1AzbJM1OZ2qUm_XvMFjvfz9HRgrtOFtOe7GuPZ2pXa1k6-E38WMTLfmP8aX4gL1-Ve-2BsoKcR78BEykD7w16adzkpzPjc1S3NZfsMG2DwQ5uW3YV-NlapdjKK9Mhf71c1Vg7UIaQabwrSV5io89aFmaEREegHUMemNuqIVHC3SjVJaVAAuoJ9Sl53Rtb-4vj5I-w9DO48EL5s-2T9oBIWTXcBMpxI7qbsg8lpPsqjgc6KzzcVLviovuKgk82Qx0XTC0WWDWWA8M1b_8wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری
؛ رئال‌مادرید درحال آماده‌سازی اولین پیشنهاد خود برای جذب ژائو نوس به مبلغ ۱۵۰ میلیون یورو است. پاری‌سن‌ژرمن برای فروش این بازیکن شرایط سختی تعیین کرده و به راحتی قصد فروش این بازیکن رو نداره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/90875" target="_blank">📅 11:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90874">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dad07bd808.mp4?token=SjZwS0w0pLBh_cY5pZ0YtIfUftoH7ddb560LJ6imWWU1n8u454j7ngRI47WAqV1gqi14XpB5YrLHmdNgy8NssXLD5BUUjcP0LhbKqmVbjmtrEZxvy1akGlvTfpQ4Pu_AJgLMd-j7-C08v1fugB7UvQhyMzRKVeGzqZAZvkfB4scS0neSVQpxFteitRo1OjrqKm9U8BqXJVAs8pUcirdGf1GKUTfE4KIqLWa1dN1Y9HJcAm95o4RYjLcRAu4RKrMF2vKOL-vTc57IsJf5Cxzb2kfiMJ9Rcv6yYdNt_Fg-rewUGgZzKy-SiBgjCuHYsU2iT-TO5s0aqeW9oiW8ElOCgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dad07bd808.mp4?token=SjZwS0w0pLBh_cY5pZ0YtIfUftoH7ddb560LJ6imWWU1n8u454j7ngRI47WAqV1gqi14XpB5YrLHmdNgy8NssXLD5BUUjcP0LhbKqmVbjmtrEZxvy1akGlvTfpQ4Pu_AJgLMd-j7-C08v1fugB7UvQhyMzRKVeGzqZAZvkfB4scS0neSVQpxFteitRo1OjrqKm9U8BqXJVAs8pUcirdGf1GKUTfE4KIqLWa1dN1Y9HJcAm95o4RYjLcRAu4RKrMF2vKOL-vTc57IsJf5Cxzb2kfiMJ9Rcv6yYdNt_Fg-rewUGgZzKy-SiBgjCuHYsU2iT-TO5s0aqeW9oiW8ElOCgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐸
مازیار لرستانی: از اینکه پسر شدم خیلی خوشحالم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/90874" target="_blank">📅 11:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90873">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XM7WIMrlwvVNx8CtILQZHJ9iidvJx1hDXP_8UBDUenXkyiL39TPGJM2OIsV7v7zDsxRbbVCqNs3nd-Sq_Mqsn4UocKIsAGRw_BOlnm5vM1uvr3IRa6UNlWU9K97Ee98CCVoBl4YZGdkjGQ4tILnCPqGqYIjC4h6qK4zFG6Ee73vczYcnKYxYx_oVBY7ck4EV8aCQJaTPRjybxSsKNO_5i-5-nYMtnw5Ml8x_of0ld5p2G_SQzmUp-0TXaOEr6Jg55wxYPJL_ZcQsF72G2jvFgmaFyfemTlu0FNpM9DRElOZWneYCjWOjzRREOmwwR8igKmbGiFuRM4pWM3w8CF5QIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنا د آرماس با کیت رئال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/90873" target="_blank">📅 10:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90872">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkHCdge2XeP1diTb8EnSoRb5YY72itzjkzeZaiY3ZfN2esC47Dfyqe8LxWLdW-PtMIGbjbfYu_pk5ZNx1CrKUYEGIrI1pPRuBzghpvZ4bWCoWoOFSYh3nanz3v7A5stMNMHqMxtEwlV7OPKP_GuVoEbCgIUeTFSpU7FNEF9UjMAXJzMzfr5H3JEpPUgS7pMrJJJ9SJZyCf2Giglm-djjv7NaDLbIXzBTfwrA3ZPRlZh-WJfYcvVkk2lTS6xGVJFhZmHT-Uz-ORJEuGAyIRs_J115LunR21Cw3w7pbrYw5hs8XvWIgImqPQy9oQy4WIn-ISuQ1zMyzWCJUvvxxLX6hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بی‌ارزش‌ترین تیم‌های جام‌جهانی؛ تیم قلعه‌نویی در رده ۴۴‌ام قراره داره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/90872" target="_blank">📅 10:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90871">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljKUcsUAeL_8oJvZcqWg7auIEgIaYmD5-prCQ_9RVkfDWcsgHy5w4izhJ6Z0OZ-S0bjcCDY6e0ZeYqL5fBKRHBumYG-FRZQBfSK7g3-gOeKVz9hoQXgLgh26NnFfPKFnzszAcgti9oY7WzzklGsGudv63iYbEkT708Cs3Kg_lS0Zl0qjlGVTuB86I326Yp-wVVDsPbpVbu7O-_o_o_Y5v33J8_5QIDr3MXK521eDuhH4Su9w-vEG71eASDmeCzt6ytif3wu4mVQOg4wwnyY4yT3ROOlQqH3QFR1XP_EpgrIOdIw2Win_LE2xlw8gzJi7yU_6ezKmQDzDMumYFzj99A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇲🇽
رائول آلونسو خیمنز، که قرار است شماره ۹ اصلی مکزیک در جام جهانی ۲۰۲۶ باشد، تنها ۱۱۶ دقیقه در جام‌های جهانی بازی کرده است. او هرگز در یک بازی به عنوان بازیکن اصلی حضور نداشته است. اگر بازی مقابل آفریقای جنوبی را کامل کند، زمان بازی‌اش در سه جام جهانی قبلی برابر خواهد شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/90871" target="_blank">📅 10:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90870">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qn449nsOAIevUxFpsNgKHoOkVTi55c7U7qT0dm_DATr4YMzxjZWTP44nn5OIoATLjqNR-d3_N5CWzmDsE8V5CtQRewV18BN16_Zvb_0Yc552xG4L2bwpqloKd0kdeDuKjym2MD-fY4LbgAVOXI2iZHvvMOS0Hvt1389pMdvjlbSZk8WxoefT-K6982xs2LABeZGmMyn4Kr7mHPUidLj3ZtmeZ5WQncMF5f0p4v6THFeMyu5FDwVNar45NAfZpigT_y6NFYV3lOwGx09zl3hJk22I7TwqiRHFQMe3Le9oni4YLBOTiOKWF0amz5U8JY5D5qtmnGADyKRFNBSIHXormg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکرد ریدمان کی‌روش با غنا در آستانه WC
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/90870" target="_blank">📅 10:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90869">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdfbdee815.mp4?token=Mkllnj5ii2mceeHoFf7rxcFNPbfUyKQYK2mR0unhN41hWvFdB9IPPv6x-aJ_NxCoSo10vw1TvTt4d0lIbMv3rBZa2G_loRzIoivZIPkyoIWb_fUf6cTmQpqfB-XrWQ_kORLEqkXJ5XDrBREWqkJz4uEVdaGrApWmsTTbY08DJwAacjVBMTIpKi2YVl47XUxF2XWapoN4V1GWeeR_qp38Pu4BJYl6QGAh00g5rNbU5kTlMaiE8eyibdNWKsTRV1HnDxdpdzSz5qQnQ9XB6kjLNjmooMIhLlPQidEl7S7XQo3Mq1mN0q0G2gOg7GNnZ3NYCcRyOe1MZBDHlx73dbow8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdfbdee815.mp4?token=Mkllnj5ii2mceeHoFf7rxcFNPbfUyKQYK2mR0unhN41hWvFdB9IPPv6x-aJ_NxCoSo10vw1TvTt4d0lIbMv3rBZa2G_loRzIoivZIPkyoIWb_fUf6cTmQpqfB-XrWQ_kORLEqkXJ5XDrBREWqkJz4uEVdaGrApWmsTTbY08DJwAacjVBMTIpKi2YVl47XUxF2XWapoN4V1GWeeR_qp38Pu4BJYl6QGAh00g5rNbU5kTlMaiE8eyibdNWKsTRV1HnDxdpdzSz5qQnQ9XB6kjLNjmooMIhLlPQidEl7S7XQo3Mq1mN0q0G2gOg7GNnZ3NYCcRyOe1MZBDHlx73dbow8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🏆
چالش بلاگر آرژانتینی با موزیک جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90869" target="_blank">📅 09:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90868">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇧🇷
مردم ریودوژانیرو این‌شکلی در آستانه جام‌جهانی؛ خداوکیلی خونه‌هارو میبینم حس خفگی میگیرم
🚬
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/90868" target="_blank">📅 09:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90867">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ce3254dd5.mp4?token=kTihEAnZ8lKfm2nO-eEmbX8Gib1TprvriEeRdhmWaOgoTqn_iFmoMnIz_Q2DXwaEtZwESnZwNQKJZ2tPaAgS2YCwhTGDDHMDSoCwz4Y0c2dDW08MgK0h_LKNmZzZgM9m5qDhXT-YDdXf9567OK1DvPWzIp-ca5HWRAnfuUqQYGTelo6WoFxa5wod_RFii8AQJv5izeB8HFoDKSC9HWxrZcY6RXX_AcFwOjqcjZHEZoDOc7RrP9ufOnj7lDWG5IPBvncKG5S4l67mTRnufOn0qrwj7HI0ORm8eK_XYngcXoehbOzNJXgc8U1KD1dqXjUGe52EL86Gir25TrzjwOOlpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ce3254dd5.mp4?token=kTihEAnZ8lKfm2nO-eEmbX8Gib1TprvriEeRdhmWaOgoTqn_iFmoMnIz_Q2DXwaEtZwESnZwNQKJZ2tPaAgS2YCwhTGDDHMDSoCwz4Y0c2dDW08MgK0h_LKNmZzZgM9m5qDhXT-YDdXf9567OK1DvPWzIp-ca5HWRAnfuUqQYGTelo6WoFxa5wod_RFii8AQJv5izeB8HFoDKSC9HWxrZcY6RXX_AcFwOjqcjZHEZoDOc7RrP9ufOnj7lDWG5IPBvncKG5S4l67mTRnufOn0qrwj7HI0ORm8eK_XYngcXoehbOzNJXgc8U1KD1dqXjUGe52EL86Gir25TrzjwOOlpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه بلاگر کانادایی تو استادیوم داشت ویدیو می‌گرفت که اینجوری مامور امنیتی کاسه کوزشو شکوند
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/90867" target="_blank">📅 09:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90866">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
رونمایی‌رسمی انریکه ریکلمه از پیراهن ارلینگ هالند با شماره 9
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/90866" target="_blank">📅 02:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90865">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EX9VYtxIm-DVqANp1E2qlORM5EyuVr1Tdd9vjNWZlfFk--P9V4_O8dq19PMuRm2bVNxOYdJLYykBf-b1XU_UPj4SI_TtMw5FVUkKq_r3tcKqjsoF9nJWhlaSY5IYuz_COPJeC_4PSFTQ2VDbq4GiE2vX1ZU-esw2h0bptjpKFvKOmq8vkATVMwjbmqEksxJnimj0v2jkuJNsfvm99I-SLQ-g5Gr0KjKlfM9J2aekUPbfh0E_4A2DgiI25skPPCMTf10V3rGiCpc8zvasINGqARNLRYJM4wz_pUegWJJZDUNL6srfEomKpYENqR9h6T_oADESo5ovW1Z4UXLBFMHKnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فووووووری
؛ با اعلام رومانو، کوناته با قراردادی چهار ساله به رئال‌مادرید پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/90865" target="_blank">📅 01:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90864">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
رونمایی‌رسمی انریکه ریکلمه از پیراهن ارلینگ هالند با شماره 9
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/90864" target="_blank">📅 00:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90863">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری؛ ریکلمه: ارلینگ هالند با من قرارداد رسمی امضا کرده. اسنادش موجوده و نمیتونه بزنه زیرش. فصل بعدی شماره ۹ رئال‌مادرید در اختیارشه.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/90863" target="_blank">📅 00:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90862">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
رونمایی‌رسمی انریکه ریکلمه از پیراهن ارلینگ هالند با شماره 9
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/90862" target="_blank">📅 00:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90861">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8OYho5UEK_mMKVAZVRqlP9yWa5vzaVPCcQrR5MwnpCaaNOjS5otk9g1UBNkyQG149_vsW1f00F_5GcGYwLMKV8_LBRjtwaXSQjmB3WjoGH19CsD4Mz28M_5xPa1QRe0C3YT4dJhGGzS-H-YL-3WHDlFeCwUnKbpDc_AgOCi0Vhh3j6qq1rJUjKwcteiPRhm3VL_9H9uRT5o3-4PAEpbkxBf0KD-fRZoSfihUjue3E25ho1Go0UdR8S75vTEaM-kCDG5JywmVBXgNNX9Pl8-JM7VpKwvA4IMjwhYVTrYS7pQVUN2ps0PaILqI6POaUmIeLsC-IHeJ84RlBUWK7DvQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
قرارداد بزرگ پرز: کوناته.
‼️
قرارداد بزرگ ریکلمه: هالند.
⁉️
با ریکشن بگید شما: پرز
🔥
یا ریکلمه
❤️
؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/90861" target="_blank">📅 00:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90860">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMwOAfxa7LZGTK1HNitttI0l01OCYTHx2KQXaeHASd7eyLh9PjmkqWgPcHipDQparhv8VqtEOI9hvS9wKaW5wiNMSAln7rDq3xrMyOL0CYbthRjXckk6iIluRjonIivHvvCD8uGDwWtwvMPpi4pDI5sTwBzyuUGP56QKb9Lt04oi_v8lvqeD62ivSQLTl06RJ9eZSz_Bylc5wEejMDOqYD-94qG7XLGj1z9ewxrr1PBENSU2XTpbEa5WHSXjdxhJljkBZ2ABa1XTHJN54Q16tfBZxh85cq98cYgpciPlEyyo8MzOxub4olUc2GQVjBhlHxWUMA5UJaHGc7VmyohsNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
رونمایی‌رسمی انریکه ریکلمه از پیراهن ارلینگ هالند با شماره 9
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/90860" target="_blank">📅 00:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90859">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">😂
خب دیگه کسشرای ریکمله ارزش پوشش دادن نداره. فقط اینکه ۴ روز دیگه انتخابات رئال برگزار میشه و احتمال ۹۹ درصد پرز با اختلاف این کودن رو شکست میده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/90859" target="_blank">📅 00:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90858">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i51eAEwNl9uz-jhCksHHvx4UGyXzBXdynPyNnGJRrAreTZaIe57nD6UJuPh7r8yXOogNmg5S1psooRvubAKc1uZYYwnwdNQQxgL78SbaWrJfmhFKgbpNp1G3REsfSG6yNk4NIGLjI0HzyL5qMVuc4-H0uEStze3s0b38DFpprehrJz3u-BjzlizRQFLsk49TIx_QExo6qloU3Wo8OM3t2jR66j4315z50D99qQSzF3OQC5KK-kGtKVNoBHcpArdLD4i2aLCVFas7pd86SgPzA-joE0r5E4Ecjo0Y7sJLjyClALgjUbMbG-r0SFR9PAbSoZ5NP17XXb4DR9B3m3J82g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤲
🚨
👤
استوری سردار آزمون برای مورینیو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/90858" target="_blank">📅 00:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90857">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">😂
خب دیگه کسشرای ریکمله ارزش پوشش دادن نداره. فقط اینکه ۴ روز دیگه انتخابات رئال برگزار میشه و احتمال ۹۹ درصد پرز با اختلاف این کودن رو شکست میده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/90857" target="_blank">📅 00:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90856">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f8fa88ed9.mp4?token=J__QOSbmdoOWJ4U5rVk-s1nomVM7m7NvHTF63J6kEye8dfm_u9HCoSluqwWuPwnKpQs6wUN4sUTgG0fgsJoDWvHYa7CWe29yo023-MmNcjJzvSio_xd94rZWCyZgHs0gHeQF8rpWkDkDI5C3gCNEfXWwU1G0yx2Rnh7FAdo96cgQCh89ShOFe6qZHy5nXTL2G1vMvCupaVYy5qIYv90QVKlD5xf2Vn1Y97qpK4R_Z-lht32xGoWVV9dxfLGxR9d1aNGZP-tF60EZ2SI1-yO8MakfGy3TYJGATmwFTCIZNDtzZMOc1rz3UPwxQX7Xgc96ZOEcH5EJ3Y64HmwSuPdjnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f8fa88ed9.mp4?token=J__QOSbmdoOWJ4U5rVk-s1nomVM7m7NvHTF63J6kEye8dfm_u9HCoSluqwWuPwnKpQs6wUN4sUTgG0fgsJoDWvHYa7CWe29yo023-MmNcjJzvSio_xd94rZWCyZgHs0gHeQF8rpWkDkDI5C3gCNEfXWwU1G0yx2Rnh7FAdo96cgQCh89ShOFe6qZHy5nXTL2G1vMvCupaVYy5qIYv90QVKlD5xf2Vn1Y97qpK4R_Z-lht32xGoWVV9dxfLGxR9d1aNGZP-tF60EZ2SI1-yO8MakfGy3TYJGATmwFTCIZNDtzZMOc1rz3UPwxQX7Xgc96ZOEcH5EJ3Y64HmwSuPdjnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
خنده‌های عجیب ریکمله به انتصاب مورینیو به عنوان سرمربی جدید پروژه فلورنتینو پرز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/90856" target="_blank">📅 00:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90855">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری؛ با اعلام ریکلمه، رودری ستاره سیتی در صورت برتری در انتخابات به رئال می‌پیوندد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/90855" target="_blank">📅 00:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90854">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkaPB_P34RoqZfIeJ6gUeoSR-tZOQN44kRHAjDuMsj0MJmHyHwg8nd-MXq_z6M8xYbLvxJqTCXVaT2B_aBL7ZkCrxO6FfCRZCGYVWAwAbQyAdLPMKg1505O1tf_GK1XkjSkB-OUIad8p_E_EbETurd_PBWhfmRmaSM2CvKj71-xFtE1v63IVOsK55F3BlApJ9eh4RalRc1RLV185n2p7RbzA6lZ5GQjxJTW0ZfYM3c-yv1QX8VysOhJf4Ut7RIwGKKosEjuL8n639q-7NFFJF_-gE_tyDL-Uwb9n2PiaxnQwYcKZLaKDMsF7gMUVWqrrjpszNXhQPXcuY2cqh2pshA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ته اجداد ریکلمه رو بگیری به خمینی برمیگرده
😂</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/90854" target="_blank">📅 00:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90853">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
انریکه ریکلمه: سرمربی تیم من بزرگترین و بهترین سرمربی فعلی جهانه!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/90853" target="_blank">📅 00:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90852">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
‼️
تیم رویاهای ریکلمه در یک‌نگاه:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/90852" target="_blank">📅 00:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90851">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuDh2UcvQDvHpsNbLYXk7aAOsmd2AbuPcZlPfzjZZQdboOlQtP8kG0BCEVK2rmoKTElV02shq2YzYaGRB-jGkHVcoczM4sRVpo0tuiCo-q3b4V1crcW2mizrOoexMuE6ZLfzunw6PXKBe0nM7mFr6XijyivJwLikId0jBgG59HFZ7F35M0fRJ_rVW-6UXNwlJxPa4Re5uf3z3oFCNx6rtZWaSOs9Z9mhhrJYYwSokE7hAEx3aaEH6xblk7W8vHJYpDU0-CgPQ-2PyibXohnTOU3oPJ_SQmYXXrngjqWZP2T_LsCDk94cuEnW0nX9EtVvhg1TvvFzyk1O6glXQ0hrDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
تیم رویاهای ریکلمه در یک‌نگاه
:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/90851" target="_blank">📅 00:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90850">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
‼️
انریکه ریکلمه کاندید ریاست رئال: در تاريخ ‌فوتبال تیمی به شرارت و کثیفی بارسلونا ندیدم!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90850" target="_blank">📅 00:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90849">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‼️
‼️
‼️
🚨
🇪🇸
🇪🇸
انریکه ریکلمه: بارسا تیمی با ۱۲ بازیکن است. یک یار آنها همیشه داور بوده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/90849" target="_blank">📅 00:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90848">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‼️
‼️
‼️
🚨
🇪🇸
🇪🇸
انریکه ریکلمه: بارسا تیمی با ۱۲ بازیکن است. یک یار آنها همیشه داور بوده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90848" target="_blank">📅 00:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90847">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری
؛ با اعلام ریکلمه، رودری ستاره سیتی در صورت برتری در انتخابات به رئال می‌پیوندد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/90847" target="_blank">📅 00:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90846">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووووری؛ انریکه ریکلمه کاندید ریاست رئال: سرمربی پروژه من شخصی بجز مورینیو است. ژوزه برای رئال‌مادرید کوچک است!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/90846" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90845">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووووری
؛ انریکه ریکلمه کاندید ریاست رئال: سرمربی پروژه من شخصی بجز مورینیو است. ژوزه برای رئال‌مادرید کوچک است!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90845" target="_blank">📅 00:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90844">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
حمایت مورینیو از پرز در انتخابات رئال‌مادرید با پوشیدن پیراهن کهکشانی‌ها
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90844" target="_blank">📅 23:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90843">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOVcwfV5ZHFfn_mq9M6CPqnLvHnrqpZ9EYZ2ymXlgjCG8MZg36nMwaNbdxBlt7PiLlJZQ-uGdE4U6RnD7_JlY0KRq6-cQJs5w84GH5OuLiEq4XdIAv_NWtEgk0yZp4cOUQLKlhFgTKQr1FQcs2qX0IdIBIlDCLXzcWh10kIZA7Z9aQwcEEEZVcWvY2YiBefDxQXGoSAJjlTPsYpPA3Q4KHQeTUVTbYLs_9yDrmjIGxTPP9JoDIv2a8Grf-0J9ujtIPGp6I8YnQ7YmMdlQEva9P755ZwssxO4MykYBQPMKCQ5gB2HfY3rMmxWEV6SCudgV_WhJKAQKhhtLn9XGcUE4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووووری
؛ پرز فردا از کوناته رونمایی میکنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90843" target="_blank">📅 23:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90842">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_Gx59gVna4EoKo1AIDUbzEny9l0fr3FIhHuBPJgHWi4iP_4rNs2C5Qdk4okllMWqNhe8FSKjiZBmUL0WMsNV6BdyXkVhmhYISDz6ZWJao41Q8cUIJ7WiXqiXpLhfD29Io0ZkcODw1m4LprGMWjN5eLjCtk6zL8Dkr-CiGd15n5E6Xy7ViPxi_OaZs1LW9SdA4h9-_zAKRZSFxJwltuybgT9qJ6H-mpOyad6lOlbPMMeI_xu4Q-ARuZPyPIdjR7ogxZQhsSnFpIbmRpawRRtLZVccOyBqQAwNaxvjmEAiRkP4ARr4C64MopV1StcNZZEU2tCWMvkAk3oCuUzBbYypQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمایت مورینیو از پرز در انتخابات رئال‌مادرید با پوشیدن پیراهن کهکشانی‌ها
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90842" target="_blank">📅 23:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90841">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkoZzOiMUfulPtJMsOaW_dh0jSbVRwPpOrd3EVAaGtl24iWRSLMJ4g-6efA_zH0-cvynwpB4yOpG_Jh8oTjnQyKKE0_d8FvJIlQPAVQM-3sEfWArRcGEQlEe5yDm2vHCN9RoBpQE2KyzyN5xjmyCJBOpTcRojN0CPS0-v8X4ueFvyYpAvhXOrZKmzTivdvTit48J0pizuNXSCIDt4IK0BQJtCmoLaYDIMabXbj3hC8ZoQql5CmlhErHHQzOvB8Edw-eM91LM2hcHfkFffk94mQWUl3s8sEORVStYLVHZcKp6lwMlhDYSe0RAcqvX-M1E3_1lbycFOrc9BBwEut-ITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
14 خیابان در پاریس به افتخار بازیکنان پاریسن ژرمن تغییر نام داده شد
عثمان دمبله تبدیل به بلوار شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90841" target="_blank">📅 23:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90834">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HKEf3t8e0TnYlSun35H7UD-m5DZraX9BrEzRXePO7-BsCX50nzsqMjmxCUtA6IE0oYiQGzbK1AkLekYGXYGk-uYpScV3NrAdUbtXTNB4DZQImrRF2A5Akzq7ubbOEDWqWlEX-d0pYZTcN3xyblYoM7fBnAK-8djCzVg3NwKE6hP9JPtAzzpsDUK8Dv4Ss4zR-5FKwTBnxoPBDHQjlwciORNT3mS6F_K6h7F36SDfWdfT0LA8p5hIQtH3eTsSHagvJ7A43CsgnsQ-Q9pT4zsE5Npta29mqPVwt3_onXPLIItG1gIz7k37M5PyDO8OKocmP99nM3xLLOsp5rxhhQhekg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dh5lhRGKwSD2wrhi7ka5RVZcs1YFsPVESM6oIXWFDT-y3dGwBhwxJpRlGjf5m16fSZHTxE2enuI407Xr6f45Ltd1TS0xk-Pcy9g8S62oyDJ2A7TivIAu-Z67HXabnX6CsQFNGPWM3N1kZ6lv2fmFSyAkaGEr7u-MgWIAvftRNq5qigWUU7FAlLkLvd5YAy30ZJ14CidnHm2jSNnofbQIpon0-6BTYS51-bqMiLmsfeL3VwZFfVAI7BP_eLSVmHe874ujPhiknt7VVjuAXSUlhGguofenW6FelMc3IdsN1fI3UvyvThETYfM8PizclzvD5JRUMVV2hUrTsMRpVC0nNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AuhLPIjZcFMIDCAfa8Zeej4-QqcLa0PkpfuhMDzjvg-Rny04stvno4uOJDmae9uE-63v4OSeEykNVLzebEOky1mEGqk5az7q0USlG88KTVG2DniPEXN1T3mYm_T1JD9MqO3cwhbkNov-Q8tllQysuxs9Uu65a8i-7OTgZ2JJ5EvSCbbARxTjTIjXtrVR2HOew3zOCAJmczTncl5VU8xIfRleWirfpaBLbSXfbcpZKXw08HnT0k9c3jJCA-mSLf8KNuAYoozTI5yYpFf4eMRNCa8JIoHM4XjoQrEmpFQUgL2gSuPeLqo9jz1UU7B1EIS4AMTs-c9qCa2ayyG4IlW2SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D_4PmBC9t0SSP8PCGmTzqJYVhc-e6seXqiDy4_5WLIUGxy9Dw_cfNoLEET0Y_cDD7N9qDrcofd5utfNxRMD-rFXr8Tm5gAkpWilmXcVfhV6hVmeHFAfxU7wztMI37kn0uq-kgifZFk67Zg6pveBLHB383LaYvx1764x0VbGPrnkWXzyuFbpd8Kwvt9UOX89CAnrJ_DwEW0r-pj1v1S_0b9UJs4I4dDUV1Vk-nk0OQ5oD1-LiIQ2hlM6hIlDUfkZgR-9Kscn98FHs1687N01bRxrLEt8N9RvS4NbmultFieTEnLlrpzNobeyZ8avyY5kAMwQjx80lR00M2870U3nvqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jKv2OxkjBgDQyGgldeZCoBlUUxtcoxZ4wzOOrCiMq23b7illZRiwilJSPcjWocPxS-8s6RZX350BaJkXzIxGiBvml-h5oMRb7viyEkFzHS388sp_Q1niBfVZKIMXN57QBMI5kmwkg1CoFJqMKPnBiktdaYYU6quD0V1J4_SxOf4xevpmuI-ajpFl0lrOd13WitTNtDDNb_S9lmB-8eaAqJg8TMMPeLRV9eS5ypQPkAZnf9ABL-1taObEgzOE0ZfYvrIGsqHU7GhdGksHbSaN_zc4OIxpJ7G2U4nNRrqbTGmFv4UrKuUtf93vu7RaPSJFMAqf8v2NZZxIpSI33OOALw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">8 روز مونده به شروع جام جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90834" target="_blank">📅 22:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90833">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJ6XJMSLPOkiyyHAAfjE_DzfvHiUizKASbdNHUjtrzXVxb8Z0LOoxMH2r3Ycr7L_Fya3Vh-rRkgwNj40oBnvPS_9YQaizOaFmp-sUwUWwh8WyVZDis5xFaWSGViI_rJF6VQ4iSyqLawFrZKOX2GjFrOvtp4EE_gGI2WYdle1Z0UL3y5BonKApU87oDYt57sXnHw26mz8eaKCCxgAyWlLwAEPhu2cEAjV8HKyI9AQWIqSCQbInMMUV4g5f-IHbwl2Yx2x2AGL2kd5tOUY7yCftnIw_64P0XLOygL6uK7BdWsxITwVfkKhdWAfOq9gBXe6DthsRGeCA8VRrg8a9WfGRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
شجاع خلیل‌زاده با ارزش‌ ۱۰۰ هزار دلاری، جز کم‌ارزش‌ترین بازیکنان جام جهانی لقب گرفت.
🔥
🔥
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90833" target="_blank">📅 22:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90832">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSPfyqwzDBVf7o52t3Nk4fyAJM7aHOS8ihvEBRyP9LMUrpZ_RLIqe8CvS5wfoPFESxe0vKDj_g8LGkAjshatlD71KIimI8bBcgCoN4JiXi3Xl1Ls_0SQyu6ujfJsVOZmwbx4EySaLvV82QAgXZwFdqeCRU9XG6p-EWK3r3tRKFHTXy3z87N3c-3KTzieMX4usFN7lTlTeEjjzl4Nq150TcQ-58H1mzgftNUsA_s7PEdD7P4G6BYNBiqQ019tsBUCkvZhENCSZq1kgJ4QRt2kBtLixxtNNxNFx61gUZFdruY9Y7Bajn925ovb0oGHYcDoS2ObBgKO3hoUZJsGg9K7Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری باشگاه استقلال برای تبریک تولد فرهاد مجیدی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90832" target="_blank">📅 22:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90831">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moRH6xWL0D5D0RkzzESsKOZdCwBmBi0vQ48wryHzqI2aZwZavU9PhbMPyXpZxXLEf17IORuWIsF_jg39i8lwOSbbtAFuVZx7YBaAfLZGiHIXl--fE-kAAjxTGSL7D3cyK0geoWrTgJa0KVnD7CopN5irJtfggw-Zj44vh0W5rSUOHz-K_o9IkcJf0DlTJ_0s5QLugjpIU1WRqt3wkS7lRY3M6KdGitnvmLwtYY9RulzV3EaTo-0BuLWXJY7veHdipPom5fwo0mDRaInn2hdMOBWiP-qiwLp80KGcoSyCWp4Oy48yM2QuI9nxYsT18M9063d5GttGhJtNexiQ_JwFcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپانیا
🇪🇸
-
🇮🇶
عراق
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
پنجشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ریازور
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اسپانیا در
۲۸
بازی اخیر خود در لیگ شکست نخورده است.
✅
عراق در
۷
بازی اخیر خود در لیگ مساوی نکرده است.
📈
میانگین گل در
۱۰
دیدار اخیر اسپانیا
۳.۴
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر عراق
۱.۸
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۲.۵
- ضریب :
۱.۲۹
🧠
پس از باخت، به خودتان زمان بدهید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90831" target="_blank">📅 22:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90830">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eay6dUmvctvppfGrI5h_Tpi8qerCemSJEphsDqkZmA1EFeXvcGZGdwztD8c26Ek58RzOK_zUbZ-p2uEZnlPz1Smfhk61ioB6gaBWLj8Fn6Jh100nQ9mrDRhOm2C1X9Dn4hA46C0I04mevTt7wcaveczcGPQ4WIZ_uy7FXkrIg78BQxzYflj0naGPOrSnbJ3cxVKfcNzUN03iDwBbeL4JdA7xUvcOCULh8AF2OI6MxpfbfjAMpDoefg0hEROyZBGyDFCnuJMEZ6Og5UfLioOj90VQm7Iu8DEouaivdsQDy724FO6JmqG-DNnxtelPpo71m4Yxak2aaPxdrbhoZlVhtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">TOO FUN🫪
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90830" target="_blank">📅 21:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90829">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gY53GIeMhcnleuFdGPHMgDy8d1NS0xXvEg9Dw4wjcxnxgaSOgZAE4MoD8SF6Mrwr7X_CpQlKR9F212p9IXMlHQtfKXdLDdCb-kJ89JScZr0G3SIir6iF1tUqP8cFf9EWAAeO8FeIyVH9GK6cLv2plz75D8kLhmT5JmNQJ-edvnw6YAE0r57EYMqC0Tf0mlHvdIgfwUAcGg0M6psZWnO377U1PrP4XPQ4zmFhW5wvI78C-HSCeiDdYtUyFm2azdN50X4ZeVdLpWNYafqC_WQT6uKycDAzRum8lZ-mRmCiiIPw3IWhB0d1c58OyRgEIlvxE1w3T8FUOwo3SYplJh-mHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو: برناردو سیلوا تصمیم‌گیری درباره آینده‌اش را به بعد از جام جهانی موکول کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90829" target="_blank">📅 21:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90826">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rw_hwVxmqTCA-nlWEtHFqbcQHOMkn3VACnVwAei-zjV9nqIozMXycRIuZ1reBS0QXMB6hyP_dubo_5Hp6G3tyTMXVV3wrUGFFsuctQiKJhBikn-c_CNcpgdg5tU6GszTekjbEdo0F2CJD22JtXRjTGSW5l09x9dTAXKDnKp4oE7a7Gz9wYKBn0nmssmRXXbtAjcTUowCfSqyDqd7bkgYl6VY7W8KV_yQwuU7N_GIVaUDM2RKspbF3HQPvnb5VFVBbl2NnRFfM819kY5m8z9PK0e8fK4FRpPug7h8iEfEPReeHOXVSlWbtG7cRH3ditmTjruOD2CP0jCYFvl984csEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/frFAsIyAwUWcZmsVvouYnKHQg-qax_rLSxcggelew3Z8ttc1X_sIUJDAgX0N2yadn_VyvLOMmwyrkK1kVexEleW4wa5taedmT1qzFD2wlBESxcmBPUeLXxracGZNcAMe5WBGCsr1Cr2hg366boKof4F0Vjm1FutsHzS7sLlej5rlJQOmuk6JnZ1_9SBRifXi_qFC-HxHpC0RAcocwoRQoSyLjjfM9j9xiud1MRoY2tLTsIkc6feGJJUzrRvXce5CIa3pghK6mPplDv_0pfTlOu6Rk4hKxpoWR1TS2GQucLkKYsOHxlLPSyGh7_FsWoIvWIYekH4wOg7wTsMY5A6AMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FG4r2E9bo0PiFxQcm_NHhsgavm8uLCSJbOeGbAkLrSgaoJsUE1rl7tMiBl771IzI5kZqdGQIM9nk3a8jyJcPj49YWs5tEzwfb6xEO1Hpcxj_Q_fpH_SaSQ6pBOWnEiS_gB8P_TUUj2h5ZqD-1hA0GnIWA7Juv6mx6QwGWCbOshL7brLRVGmirhxg8px5NsPbH9yKHp88UwSB_fgglwL6L_JV-Z9NM0Y7vPOhS0PTkvugN0isnOFdJOdz6RRL2jQVNEtNY0YwZtIwSXft52R6ZNVFAe99zhEdU_ntctCwdXXOIujHNyNAet4H4qjiikWAd4Q8ViKI_J25UUjG9xgImA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عشق و حال امباپه و بانو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90826" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90825">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
موناکو در آستانه خرید کاسادو از بارسلونا است، به محض قطعی شدن برناردو سیلوا هم به بارسلونا میپیونده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90825" target="_blank">📅 20:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90824">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csrOeAV98CnYJrXwX_hPI5w-ffQN_1NI1jgl53TMcKF-3iiOnymfwLgSj4EUzSNLrpxKXNImV6UqziKoEaXw9K872a0o7qHU08FglCPZRwSbbJCbggmWqESTdWBZRdbSEzxcHlu_J4E1gpALD_kgg3_nvGOa0yoWg4Skb85YmClqtHq6Tco_tw9x3CVjZOqMINLUf6UrOcYUmoS8b8oO-InuG85J3FWGMnyKzOE7mTVT-IOvYLUyjB8pg8NCjCiNDA0uZdt2wmR0fbLY1TF2NRH4hpMNI5VvZW1KHf1i9kzYG4NRDyzSp6RLl9ZKobPSeAqSsfvg0KdRV-4937DFiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
؛ در صورت منتفی شدن جذب گواردیول، رئال‌مادرید با درخواست مورینیو بدنبال جذب کالافیوری ستاره آرسنال است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90824" target="_blank">📅 20:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90823">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b12cb328d9.mp4?token=m78S0hz8FZ8cL90v12oVXeT0sBMLhWLZwPjP0SOtb7j0OjSKKcK54dRm4RkHMamrOpi_DhHSCtYcawS1XtEXokx_-bDoalWykfGBd0mr79Ec8Or7Sa5KNMjefb134Gd2PMQ7A7eOYr8NLBHvvYrGxTMJqXm5OQOFnlG6V5o-lssNWLh8xPOXf9ulA6dyV7hCv0eDImR6g4CZoPumS_zGrx7YKLUuG7MXVm2GlNP2WCILgYaC6oVaSbMHuFS_rwb0CN0QWAREtxDx9jzuaOX5I-1j4Ez7-hjF06bJy1aYHWeiIE8HLlvqaJEFCOvTVeMbKVPM0Edr1MvJVl5BNZRBMnQ24yfGA-3uIJDQUIGwtL6jqR275lLy8nOwF3bO9qeTP7G2R1PzY3kVl0WfZO0ErezECY0_DLWa8rHOZURT6gvgMvyMw5_iy2TcbNkLCPiTgubS7CMWMOlBrfHzCSPTF_YkiEkWKmBD5CrBT3rNPSoZ5P1j-6uQ-lysoD_kvQKlak0arOr1x5NzBd3koiPNRqioBZhc2Od5CbfQhuCyOU89O7v89JHCCiRL_jRqegyglbMa-TUY9T35QjShl1-fTILqaquEf-KKK6hZkhxOBsvNneb9lk21F9CxsL-x80OjJqGjpW0_83sYCZH2TPS5V6E7RyAbPvvrCgFIe-4NnP8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b12cb328d9.mp4?token=m78S0hz8FZ8cL90v12oVXeT0sBMLhWLZwPjP0SOtb7j0OjSKKcK54dRm4RkHMamrOpi_DhHSCtYcawS1XtEXokx_-bDoalWykfGBd0mr79Ec8Or7Sa5KNMjefb134Gd2PMQ7A7eOYr8NLBHvvYrGxTMJqXm5OQOFnlG6V5o-lssNWLh8xPOXf9ulA6dyV7hCv0eDImR6g4CZoPumS_zGrx7YKLUuG7MXVm2GlNP2WCILgYaC6oVaSbMHuFS_rwb0CN0QWAREtxDx9jzuaOX5I-1j4Ez7-hjF06bJy1aYHWeiIE8HLlvqaJEFCOvTVeMbKVPM0Edr1MvJVl5BNZRBMnQ24yfGA-3uIJDQUIGwtL6jqR275lLy8nOwF3bO9qeTP7G2R1PzY3kVl0WfZO0ErezECY0_DLWa8rHOZURT6gvgMvyMw5_iy2TcbNkLCPiTgubS7CMWMOlBrfHzCSPTF_YkiEkWKmBD5CrBT3rNPSoZ5P1j-6uQ-lysoD_kvQKlak0arOr1x5NzBd3koiPNRqioBZhc2Od5CbfQhuCyOU89O7v89JHCCiRL_jRqegyglbMa-TUY9T35QjShl1-fTILqaquEf-KKK6hZkhxOBsvNneb9lk21F9CxsL-x80OjJqGjpW0_83sYCZH2TPS5V6E7RyAbPvvrCgFIe-4NnP8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدمممم ینی؛
مصاحبه شاهکار این مرد وایرال شده؛ نزدیک خونش رو زدن و اومدن باهاش مصاحبه کنن
😂
😂
😂
+ خبرنگار: شما که خونه نبودین.
_ نه ولی کیرم دهن اسرائیل.
+ خبرنگار عع این حرفا چیه آقا
_ خب الان چی بگم؟ بگم ببخشین آقای نیتینیاهو کصکش؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90823" target="_blank">📅 20:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90822">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c5ec264c.mp4?token=MrBQ_5i_eKaAT4NT0MQ4mGN68MmVk6l-fACgRE3JHkndGLmpe9S7kQr8GUJngGZOH1QJsR_QFUvm3GKzaIbRLqpHLO8NZQlZl68iRdXCJXS48pRrt525PpF6bl187lZWTpg6uomK4LOn0bcbZEKhnAjNJhbwmslkiqtyoIIfX1y7tyFxaGAh7jnufc975Xq5q9rWww_fzbDeQA7l5cswIZBFILqyBYG2xulb56v0kE4LxV_49LBmhk1aPaSgMod0muQVVKA14d95KFt1eyNzlMA4U1NoymcCsv9-LHONlbNamhun43yOZLaQMv4I41in87J0HtohubcwNdE7LERjIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c5ec264c.mp4?token=MrBQ_5i_eKaAT4NT0MQ4mGN68MmVk6l-fACgRE3JHkndGLmpe9S7kQr8GUJngGZOH1QJsR_QFUvm3GKzaIbRLqpHLO8NZQlZl68iRdXCJXS48pRrt525PpF6bl187lZWTpg6uomK4LOn0bcbZEKhnAjNJhbwmslkiqtyoIIfX1y7tyFxaGAh7jnufc975Xq5q9rWww_fzbDeQA7l5cswIZBFILqyBYG2xulb56v0kE4LxV_49LBmhk1aPaSgMod0muQVVKA14d95KFt1eyNzlMA4U1NoymcCsv9-LHONlbNamhun43yOZLaQMv4I41in87J0HtohubcwNdE7LERjIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبلیغ گواردیولا برای پپسی
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90822" target="_blank">📅 20:04 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
