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
<img src="https://cdn4.telesco.pe/file/UvldS95xs_KNY65x8DS6ZQG9Bi8LEQJP6e-ja_8urMOHBaLfoUthZoIgGEqG5pQD6OhvlYUE39PqZJp1wv9zbUrjYV391W5U1ZAQBJX9REp2ksfv5Hv0-n_stbLUUUwGPNrPdPLA85TdnxMAQywluYOwL_NhZRmy693_rMrXO_Kt5ggtMSD8S11hZx6xp5e7Wt9EX73I85aGdaPSOXS_KR-5Tp7EnVuIqnUfJqQXHJa342w5WXgnmIZno5Qm7IluLyQTQZX8US-XZry0Ot09CI2uFa0FG1Haux3K3vLp5QXeJRcy2fUNW4Ncebeccd3SyAwOQfimSkOga0mvVBkbWA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 18:58:47</div>
<hr>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeUDumnwf8CmBNYt_QZ99AD5HivQYym0R0jdz_f2k7V_ReYr6-7Q7KO4J5-qNaSXkh0rGqHLJjzMdsplwbeV1k3hdLIVIgucEEXGgVyuvJdtjrZybLLKiiEdza_fQJ4F59OgcqQHFu6ElTGhzLrq_qxVltYfrhe8sPm7ZIFeEOQlpSb90u6-PZpJbH1dt3UgRRfvVC5GNta9TbCemTVHIywVgfxCP6d134uMjx2brgEqQV9ZMf-6fAuChUz0bl0kf11s2dmNl0R6aKOu4UzR86BkQmABZzAZm8v0olC-Li7iQDBcd5-_K40tWTFjMzwM40_oxwNd4UgLRaTEiCH4ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=XyG6rrtEHnpCqOW1dQFAwFLC9CsfLH98S6OoLmtQp-Sjz4OjbYce6Ytz12QA0_4qcyIVCi_FBSj3CzHfdcCWgt8q4RP88mWdlQqVps1eFo1ec5hYc8GtqbLOdAo9rT8Ij_QZtrNZwWGnrgrQWXc1L6ZvcGGzxWn2Tw-erwHbR5zhIUgtQhFVip2maGKvuDBQPAl6efoVPHkZj7a3XQSxqtwfGAxQHO8W8RPjQNpA8fALMupWxvLri1lxhOdVuUKfP-Dra9CICb3Zs-P2c_dox7W3Bh_W7CIzdhQLgUEnZIwTZCAKkuHCFTyurVzV3A01Baq95nYdg1D5Ifzz6_D0IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=XyG6rrtEHnpCqOW1dQFAwFLC9CsfLH98S6OoLmtQp-Sjz4OjbYce6Ytz12QA0_4qcyIVCi_FBSj3CzHfdcCWgt8q4RP88mWdlQqVps1eFo1ec5hYc8GtqbLOdAo9rT8Ij_QZtrNZwWGnrgrQWXc1L6ZvcGGzxWn2Tw-erwHbR5zhIUgtQhFVip2maGKvuDBQPAl6efoVPHkZj7a3XQSxqtwfGAxQHO8W8RPjQNpA8fALMupWxvLri1lxhOdVuUKfP-Dra9CICb3Zs-P2c_dox7W3Bh_W7CIzdhQLgUEnZIwTZCAKkuHCFTyurVzV3A01Baq95nYdg1D5Ifzz6_D0IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل کوثری :
‏سردار کوثری: شمخانی برای جلسه فرماندهان در بیت بسیار اصرار کرد
‏سردار رادان جلسه را نیامد و سردار پاکپور هم نمی‌خواست جلسه را بیاید اما دستور شمخانی برای حضور بود؛
‏وزیر دفاع با معاونینش در جلسه حاضر شد؛</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=uHoy069lVUoL95KntXuO4IkpMGlrW1RmiHaUKVmGyfDZNUVbBZi8e_f-ybcYKTRn5kAwQmi-yIWSKKa8mxIHEcFefekg85U0MfiAdDAwFA6_2lhxiCf5h3ML29cIJGd1jXr662xkwQw_QDjeuZyvE_RJlsYzZqcfMkoN8qHOywvT76MKMYhTwUs_dEafKjWlD5GtNGcS5050Fd4OG4_1UKKCIAFnSQz_JldsAgETYRUF8pgDfo3pDwY8malVkW_4cBBWtM6DJpblycyxp7n-RIh7ANCrwpiuxre-US_j9Ju99c90RJ7wDj_Wpa-N_mXurp9FXqUhuU2dec5qatfv3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=uHoy069lVUoL95KntXuO4IkpMGlrW1RmiHaUKVmGyfDZNUVbBZi8e_f-ybcYKTRn5kAwQmi-yIWSKKa8mxIHEcFefekg85U0MfiAdDAwFA6_2lhxiCf5h3ML29cIJGd1jXr662xkwQw_QDjeuZyvE_RJlsYzZqcfMkoN8qHOywvT76MKMYhTwUs_dEafKjWlD5GtNGcS5050Fd4OG4_1UKKCIAFnSQz_JldsAgETYRUF8pgDfo3pDwY8malVkW_4cBBWtM6DJpblycyxp7n-RIh7ANCrwpiuxre-US_j9Ju99c90RJ7wDj_Wpa-N_mXurp9FXqUhuU2dec5qatfv3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdtiAywHrPuhShYKrOKfIHuE0igSLK7wLwdmbAypbtze_5bewZgNbi97KQUWb2ZJ9-1I35QmrvamUIDC5nd46kxjqsnlxPUBd8tlyds2D-kozE1_GrjYaLz3LNFUbbDX6Y7gnSN8jbZgiWzoby2ItcINLLCfSgSUZ7MGOxUEqZv3XPqzTw7sbKmK4U1x923y1YiJt6Izkt9G1XGwBBIe1DHS3NgxchrGhBeuzLxDu8g-LCP9j5XQ66pgVfZbUW2H6CHDt4ZZtppxUrakGJlyWRXd4xlwmCBM6CjZLowETLQw5Lv90A_LazAOw0AJ7mk41lBiLKa8gDv2BXux83rFBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pa5IHMpCp69k0FESTr_-Z9eLryJKasZm1fqAylq6ym8HsOvNCqe8uN8WsNxHY4Yxb02YeuYqzbRh1L9B6xyK6n4ssEL8u9fTp96pLA4BUOTbjRhsp9pliNoxFpixRlp2MB9O84hEdMbT50zbC2n6rUvETXKzOnUfxtEuEbbMI4Wgq73y3pDx_dYwGjXBjBWZjasYVHpl_OzBSPmzdQb32Seg-QY_0xqtqVM-Du3V3OWaK6BqDlWNKX8vSei6ON0VW_TFcSgwufwjcCGD1nXwSTthMN5U2vgigVOO4LDk7Kj6axclS_uY_xNVloJO_TEDyYWrnSH_oXXbzfwKyA1n9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBfZKEOIY3cK_10QKsHa0iHIBUBve31VMnxZOJdm1Tw1X2F0WEB8b7qHnUWHsaKYc5QzVjTmZxfgCH2wcybP4BzOsViWBwBpuOnnBxDRp5WBfg_n9jgeYsLtLo-6-RRb4AiTzCB6rpXE1xf6brB5VQhgwuqJ3Qqb5cK1vnsgwWhom27lTkMJd2MhMO2IVyAoNhR-OUT62bn2uIqW3yFquYTLsACuu45M_AFc9SZcu8JcN1nTxIM-MXpLXR-vJCV6kJWL2BvE58gun0mrMjLNWWjoPEf9-IuVZxsT67bQHllTU0SD8Qz7Ni8Ia7ynvu9zpb2IvGKYn6S-wyTlub1AFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYpPwbtJ5I_jNlwLPZojzQbFBv5NZFdp90bUMdbg3kQa4-f92UgJ-pNlfCfkd42YhQ7_z2jcoatvU8x1u_rDZSBG4w8l-n1v4_lFBRSNa0qdkmqMezrSKHHYT-fhACBFq6GBlvxAFf3ao0WOi-c02G02bi_gEdDcZS3kD-WbeGd3rE-NoscXct-y8Yf_yuzTiOA2gWytcQBRDgoSJxbjT_XloZaAtKK8bOjE7U7dXHO7w3bq5wJ-O510A2JNHNJPuMLMAxDyeIOI0CVwvztuwS8UmNhzA9fQYJyzJpV2n3Obxrcp5D0WMBT9jxrkOZfQzUTVzUGqSkypyEWXfSfM4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tk8Pye1R0txkFomPVhn_Zc8HW2Z4PqV1hd4Bm6nSo_IGCpNT7_feUGgPxKThbIXfuz0i7UHztgviuetkPttvP3fdL7BR79hBkFwT2xT_AH_oKxye70sxe6WVAnOFIrUTT2IpVIYD9h6MH47CwfTS6hLOWYCzt-QWl_kAEy7d3kDPnrc0tdjCZy-pm8dM5wvqx1DmkqXXXSIRFWuOGTmtk_URRtOT4s6Whrgz5YzBTYlVkd1e2_rm8fw_eAYvpm0MYptW9ac-cTbrrZZLRPY_4gPp3BSqOWdzHehy1MuyPHtiSW-hCXyzdaRNo2lfkbeFdRGvsX85qTXrI7zg7sJknA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MoJ_XkJXkJJPsqTMJRDle-ab8y-fyUMVK6hvNB0mTxtDiSLvtXlJvrAuj6a1byp0Jt_g2cpAWqEopSvb_nB7Grfl8XV4gBmijyDE_AOm3NQMveOTf059OKZ-eEgh6vlD7vZxbijzTR1IvodX-LtlUfIea3GHX7eHuo2X5MhJMAV_i8OxP7It4fFHAjyYhfExbjWrZPxZYn3qI1d5dAN5xFmMAjpZPMDnAhNuxTE1ZMItuZQTGGJQtAm1QlE78CyUG0XuMI9Z1o0jPP8_FH3tABBbwpotyIzpCSP9-jdGuT2kofqH42LyDbS6UkL21Ts2FMy82DCrkaCig4xokj7exw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E4kxz5a7tRWkfyErIOnmPIZwFlU5zOGqzkM6EtTOL6Q9tXaubmq4f25S5EEAhRpXpcqj7s-aw1KcBIG_n3hA73DydcmJ2liEQfzRhTOQhnufQ3nLA2DsvJwFwB05pejvgoJ_7Cw16x7PXQQ4mjkIu63sdgKWNYOsx-6Cy4T6tTuIvqtB1UQ_k0cty4nKbL0-heQpwP21IzttjnMEejaUhSePeMGXVaZDpPblA7DBaAnmg09FXOOQDVXPmWbjlZyzLsKvuyJW76FCo-T5BP1ylac08dant0Yh8pZBK_YeX_hi0Lt-QENkKyM3682w_C3z5JzXjFRcy_0f0loUhd3P0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hKjfx56_HPIS3rsMA92vylkB4EBfdGRq_UxenGhMJS0q4E1GT5IhbSLtPZJkk6ztA9R2_czOSaWuxbCHIY_8YSwu1Dh9LcMP-9Rjy--h7yA_pqt5m-g8oOmNm9zgkpwNDZ6wOPlF33nAOnq47w2D6k32dc0ZaujwRNxofONnM7mIbEkF76MPf3O9KVOzQHXvpFeAYuo4e4AFntwegCzwqofh6ajYfq3ik-uK86MM4OV0g72q00QtQ0utzYEfQ8cQNxgah8cJoxZMiuqHshYBtMoVx-XKm1GlIZOTrMzO-jcI7Iy-UYo8_lpCjSvLb9Gh0VBUPET9jpGwCKzvIyuxCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیرین مدرسه ساز در ایران،  ۶۲٪ از مسئولیت ساخت و ساز مدرسه  رو به عهده گرفتند. حدود هزار مدرسه.  فرض بگیریم همه اینها مدارس ۶ کلاسه هستند (برخی ها فقط ۲ کلاسه هستند)  اگه هر مدرسه ۶ کلاسه حدود ۱۲ میلیارد تومن هزینه داشته باشه، هزار تا از این مدرسه‌ها میشه…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6524" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flKUk0yET-K08bKuQSWw8stum3ChMiH7VSs-MPy1pyrZYUuKhTOOe2a6R5VFRPSbTmUGxSYPyGbPtZnptKlM2mrEJEamlLkoiVZci5GCCBnLUhbtfpiLNXKvMKk45KH-LUypqyFZzlEY2UAJCZ-zPA2XZJvu2qX6JJTY14fwhFVQUZT50JcZnI9HBYTj2_vaMNZnTicFZKXrTz0m4vyS1FmQq6C_vrrvjzRlTkz6DR2vHri6DtIe41xic9aORMcs7NcpkUdM2D6B6VH5FjQLExVaR774QWpBoZErME6cMufMx8A7dRTFGotC5NYysIBBPO5zF8Mv2EvRYrvRghy72A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا این متن با دقت بخونید و قضاوت کنید:    پدر یک خانواده،  نیمی از درآمدش رو صرف مواد مخدر میکنه،  موضوعی که باعث فشار  و فقر در داخل خونه شده.  مادر خانواده ، چون بعد از اجاره و….  پولی براش نمی‌مونه، معمولا از بقیه کمک میگیره که پول پیاز و سیب زمینی و…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6523" target="_blank">📅 14:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">لطفا این متن با دقت بخونید
و قضاوت کنید:
پدر یک خانواده،
نیمی از درآمدش رو صرف مواد مخدر میکنه،
موضوعی که باعث فشار
و فقر در داخل خونه شده.
مادر خانواده ، چون بعد از اجاره و….
پولی براش نمی‌مونه،
معمولا از بقیه کمک میگیره
که پول پیاز و سیب زمینی و قبض آب و برق رو بده  برای سیر کردم شکم بچه‌ها و…..
هر روز هم دعواست که اگه پدر اعتیاد رو ترک کنه، هم پول بیشتری در خونه می‌مونه، هم کار آبرودارتری پیدا میکنه و پول بیشتری در میاره،
هم خانواده از این فشار و تلخی.
🔺
حالا سوال : به نظر شما افرادی
که به این خانم کمک می‌کنند، دارند کار خیر می‌کنند در سیر کردن شکم این بچه‌ها، یا دارند مسئولیت رو از دوش پدر بر میدارن،
و اون هم با فراغ بال بیشتر، با شنیدن غرهای کمتر، پول خرج اعتیادش میکنه
و در واقع کمک هست به پدر ناشایست؟</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6522" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=RAxwSUr3pluiaXWGXRKor5-uanIRFT0QpAkQq53P6cNviq545aHBAWSCjMvK97iDzSmTbeUcv4Sjwl6lyL0gDI2W7u_lLwAmviDqzj9Nyi9GIsrHWp4idnQ8s6wpr40UjLEag7rz8eMEtUv5jgGvBrE-fDUQV0kplkQddyyMPG3E5rbp0SCbyvoSp5u_KGOmilxd6WbQE5afWy8DTuOI-8q9r1FYThMN_2_omBW1gn2eEy7vXoZ6TQmsXQPJ_EIFv2tMeupHaYJ8i9vf_0-NzG01J0lG9uoemMmcICiKquf5XRZT-Bf5UtYDipSj0fINLTSa6jWObxpB06BmMeQSuIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=RAxwSUr3pluiaXWGXRKor5-uanIRFT0QpAkQq53P6cNviq545aHBAWSCjMvK97iDzSmTbeUcv4Sjwl6lyL0gDI2W7u_lLwAmviDqzj9Nyi9GIsrHWp4idnQ8s6wpr40UjLEag7rz8eMEtUv5jgGvBrE-fDUQV0kplkQddyyMPG3E5rbp0SCbyvoSp5u_KGOmilxd6WbQE5afWy8DTuOI-8q9r1FYThMN_2_omBW1gn2eEy7vXoZ6TQmsXQPJ_EIFv2tMeupHaYJ8i9vf_0-NzG01J0lG9uoemMmcICiKquf5XRZT-Bf5UtYDipSj0fINLTSa6jWObxpB06BmMeQSuIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رجب صفروف، عضو تیم روسیه در مذاکرات رژیم حقوقی دریای خزر، مرداد ۹۷:
‏همه ما انتظار داشتیم ایران درخواست ۵۰ درصد بکند. قانونی هم بود. اما جلسه اول یکباره جمهوری اسلامی گفت تقسیم برابر بین ۵ کشور، یعنی کمتر از ۲۰درصد
‏برای ما عجیب‌وغریب بود که چجور ایران دارد از حقوق خودش گذشت می‌کند
‏این برای بقیه کشورها مثل هدیه الهی بود. از خوشحالی نمی‌دانستند چکار کنند</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6521" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6520">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbfFSJiTnLRGR2RUsLQXnScXf9XKEUjNwYYdui1jNx1qsIzy0ilDtTtoCKBi2R2YkopRoITmAfuacKLcCxGAaEsER23owEfeFCMhsTlb8TmlWaX6lZgYEFKj80Dph0ztAJmXfuadTmsY2YcFALx61brVs9E-Vjt4yLe2rUpHK2sXVVOmJ923Cv7hUi5yUqzGvNSR4A04v5MVBaVAeGiVzhxfyFnhKiKTIJH1Rlqo97E4ZAFEjlQkbelW84BFDAfZ12ARTO_Xg8wt4d3B4-3gP69w0XW5pKZKWrIAksdhE0hdI3uwM76vJR_HAhxhHM0eEpwrCSvCWr9KRzRfGoD3vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی به عنوان رئیس شورای عالی امنیت منصوب شد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6520" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6519">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSD1qUH69vTcBd62Gvk06EaQ2uacnAehuG0sFRJKYSi9mk3iupk4LeanDHSuijZ-_3chBE7ER3mBuZ680qpaLLSTrVhqEBEGY211XTTzlRJdmnvSg8GqCC9XM9xnPTEAZQBZDVAP3kOp4Yxs7NDNqRFC2faaFI1sM5NosDxOi040oAcBjGyY0Xnzq8JoyQDR-IHJtQOMF5RdsvaHNHCMGdeydrx2M-uZjj_zL3joGOTo3t6cmWkEm1EA-2HA_CzXDSiNTpagFJqHncTe1G7CoKaxXY7Av-nHLe8SyjDtJn5rPVQ9sRnuWHhlCVbFGwYXLdJoKWJqczLEBM1mTt8OOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«حمله‌ای گسترده در راه است…
نه، صبر کنید، می‌خواهند مذاکره کنند.»
این یعنی «دیپلماسی نمایشی»
که مدام در حال تکرار است.
استفاده از زورگویی، وعده‌های شکسته
و اخبار جعلی به‌عنوان ابزار فشار،
راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید.  ما به نمایش‌های بیشتری نیاز نداریم.
- فهمیدن حمله به کشتی‌ها و زدن زیر تفاهم‌نامه نمی‌تونه براشون دستاوردی داشته باشه ، از ترامپ میخوان که مذاکره کنند.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6519" target="_blank">📅 22:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFH1ZtdZi3QsiGf68G2ti77RrWggN6nkPWzjP_3qpMtxxRuT-OPHR-kEMd-D8x7TkK5U3axrZEoUfJhn4THSXIpxN1LICcPu-5DxUy7eoPJziSE7qYdSTv3dQVQfve1VvCzvPPD2FYUasmZxtKHU5UM6OwVJ_erexl5D-KXFpo02ryhvyCKIhNK3dSl3hesOSRu5lFeQ9ee6rlVm1VqLIVFvGPyrmUpyGFbnOifS-s_Mg_OQJcOilZK6hE7_ycbsUqIYkBvBgg5cOvWAPmpd4nFdK30AYfKSMYHgOqRq8PHbwTiDLVscFQljYpjdWRr3ev5iHKzuMsDzstF9zSXMtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به امید بالا رفتن قیمت نفت و فشار به ترامپ، زد زیر تفاهم نامه  و حمله به کشتی‌ها،  که با اقدام به موقع دوستان خودشون  در حزب کمونیست چین،  نقشه‌هاشون نقش بر آب شد!  خدایا عظمتت رو شکر!  اما در عوض برنامه آمریکا در پاسخ  به اقدام جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njPCDPWoWm5xgeyt9d5resb9CTaTHi20x5PiGVeddSBtjM4tYPgKhziRav5-VE_hzcLpXUaC3Cgb9DcokolPTeXUtpyY8Tpe0W6AK6ND-ztwOhDD0J6v7tkKw8ppIqa0NQ9XK7A9hNh3_HWKVso4Cy3A6qv7vAl8-qvLamU7WQvhiHJxBHIRmN9zTOC8G6fD5c1uSXOQ1I3WWZEeOSQyCRTuvGtubsR-GuYplpxhpnLazRRcbV2P-zrjcOHlUdxlNQkv6WyNvFAaEf4Gw0QUnhfKRWhJdN9jzCbSFnOQrzNsAKkToIH9Xx5I6ZJpJCGAfaAs4xMZvc7aSrFUfUk6dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم : افزایش تولید نفت کشورهایی چون امریکا (که رکورد تا یخی زد)، کانادا،  برزیل، قزاقستان، ونزوئلا و….. است!  نکته سوم ترامپ!  و به نحوه مدیریت ترامپ برمیگرده!  بازار نفت به شدت حساسه به اخبار  و به انفجار و ناامنی و جنگ و…..!  خیلی وقت‌ها قیمتش «روانی»…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZGNGYDIcG0b5RgirS3VmfKgR1va7-ZsYSgtgITZ6k03rB4nvUYHsD6dtGMtnnXR8Bw3Zq3mz2MsqAy5PuydoX8-q3TQH-L4oEdBqRy5ezm5skStU4Wf0L29lN9U1nbb5ZUjS1NAj-09Egcbm_97uz9IU0ciKtN5Sp0IJSGBmnWAAZPyWIK3_Ufg5B2Qc7a1j75dDBQlXOShsa1jXFIxTLityM9RGDR7EKQHsStMRMxM6QRrHIiFFEDkvpAW1CFNoQbs6xj7QRBjmCBfLOBgAC0TjWmCtKOx31E0_Kh0pOgy0HMDKahVoqZoj2HmwNbvqWHU1hRZdV-pfwHNHFzBTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qyu8sdImcw2viNja7YG5TW9ImG1qGrbvoS_M6ihJSTXxCybl0C_gljfArj67sk-xiog2zdeJHvFzUKuiRLOHcqCYnT2KBAjYk1pOGDS6vqcnIH5aDE-qvCHv8e6RP0EAPmkfDGw12CsO1ImxS69leVsJ1M5IAptbRICVw_or9_rED7XqY7M84za1hiHgtib429G0oQhlp02aemOMj0LJAU1R4VVSrvic_AmUeDm17bs95eZ8gpCMf6nMReZiSNhj0Ktceu_oSyVRL3h66D9IWgMsyfrg3TE0bhdr4r0pSFM7G3XLesWG8kzFvoUP10fe3wARpCNlu_4YT7xV8dsZ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gTl8MpNjzaZnwgNYClGzfNb4AnkMptn29OUgHBoNYTDCg-6p67fObkhIisz5RyUcr5DObVHoHWnpi3TKcx2VutJNYCHgd7nmPPG3GmlnG3vKYQLI_AQ2c-Z-giZa1cRsuvI0FP-9ycQSq6RB22ZXZp2JkuaLXyWZKFL5oL3jos67MHzPbTEVgl1IFTL2U7DW4fTnOuQ_onpg-j15P2nDbcKhb2k5gfaTHaBQJq4mahKkug-d9SHTRZY1zm-HDUOgwuC-G6ExxtCa7Mx1t0IizxoOExHaksd_fC-LOcuACvX5eOcG7jHAMlpwfpF7-qajJajYQ3Y37THKXscn4hXSEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.  اینها دنبال «اتفاق مبارک» افزایش قیمت  نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.  اساسا با همین منظور شروع به حمله  به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6513" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=Cx-_TbtTcSDQVTpbOhFbH_jLAvRv7fXsEwjMEoXrXs3zLxqEEmFy_FRseOwro44Pe_T2NA8U0VIJYZq84BssFPBBmTmO9Mz6c37l1FzFlYicbMxYhL--WAwrl-H7JEDmrtoRFKtVQe30o3AIdRiYVPKsO0N618qWpd_NIiCIqqndlYMnxz5x-7_7QHjrg9PPwpHkIEnfzGRVgXLxIzhZ4HWs2jbJHWElgUSb9b-rp9xVfdpNFWOOBlXgReh6eL9Uim0dsnceehMvqZjf0-c2Jtdox5iI0Klb5Rjod43U5MRcZziXqqYqYkxZMJ7tFjozBdHHPMpqKwrulzIRzAamqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=Cx-_TbtTcSDQVTpbOhFbH_jLAvRv7fXsEwjMEoXrXs3zLxqEEmFy_FRseOwro44Pe_T2NA8U0VIJYZq84BssFPBBmTmO9Mz6c37l1FzFlYicbMxYhL--WAwrl-H7JEDmrtoRFKtVQe30o3AIdRiYVPKsO0N618qWpd_NIiCIqqndlYMnxz5x-7_7QHjrg9PPwpHkIEnfzGRVgXLxIzhZ4HWs2jbJHWElgUSb9b-rp9xVfdpNFWOOBlXgReh6eL9Uim0dsnceehMvqZjf0-c2Jtdox5iI0Klb5Rjod43U5MRcZziXqqYqYkxZMJ7tFjozBdHHPMpqKwrulzIRzAamqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.
اینها دنبال «اتفاق مبارک» افزایش قیمت
نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.
اساسا با همین منظور شروع به حمله
به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6512" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.   خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.   او همچنین با اشاره به اعتراض‌ها…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6511" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=YK7dlq-QRhMRQbBNrgjoPf6rviKpO86kqJj-GWKT9g-EHO5RH8hZgHqwblC4XlZrRp3Qcehvz8yD9kS_-vJECL09W29GwzOZlCJWc-Ql0qQ31og59NLdSNCpvNQbiG9uZIHN4BfwAzRFkfaiVR192MViEYvmxuCp7RocdKW4cnnY5KK8mFcZGQ2bNb8otUdS5PBNsxhJLCjPryYzYMqI7-2-0R7YeMalSsbmviZCBSxGqaAuLkZypOWGCuC4tnVr4wuhR9szSdaRFi7CQWsnROVFWGWJdTRmQ1QnxEKLnMGlxfSje-lFTsvUNILVNQA0bo5AJfuobMpQixkWZK2Wyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=YK7dlq-QRhMRQbBNrgjoPf6rviKpO86kqJj-GWKT9g-EHO5RH8hZgHqwblC4XlZrRp3Qcehvz8yD9kS_-vJECL09W29GwzOZlCJWc-Ql0qQ31og59NLdSNCpvNQbiG9uZIHN4BfwAzRFkfaiVR192MViEYvmxuCp7RocdKW4cnnY5KK8mFcZGQ2bNb8otUdS5PBNsxhJLCjPryYzYMqI7-2-0R7YeMalSsbmviZCBSxGqaAuLkZypOWGCuC4tnVr4wuhR9szSdaRFi7CQWsnROVFWGWJdTRmQ1QnxEKLnMGlxfSje-lFTsvUNILVNQA0bo5AJfuobMpQixkWZK2Wyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.
خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.
او همچنین با اشاره به اعتراض‌ها و تجمع‌های خیابانی گفت دولت مسعود پزشکیان به پایان دوره خود نخواهد رسید.
@iranintltv</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6510" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBclFUlUnPlh4yhkOUfjdFBTyYJ9FgWzotj8EjNujv17AmAlyfr2TBC9unRi1telYlXMjQiGnw1S8ZsvUok-KU2Wa1fqU1iV6_44qPt4CLVbQbyzPi3JrqhBYzWjw13PlcZKm4DmZW8PM2obrZ2WJZfJFXmPBxwrLDQwUD5iqi6Xwdu1xt-gpNTyuass3IddmMtTXQlhCQC4T3hEPCpliE9EwTW0htPNnmeD2-qM_LqvmgNNK7fO1CHdXpKvDBZopnFOxw2jSVRYxKaq6shZCO-AW-uKuDn6IZ6kBDozxoHlbXGNuCGvUI4pkyBkClG9QmW2H4J-DLttQ-VK5rzDhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4XNPCaOxYTmsGCChh6PsjPH_hgu_PKTNC-kxXo0fdqBLI3nq417bPRoaaWp_z8CVogfF15ARoGAaGAJ9QEWUf4y2g1QQQMydh6XL_qaQPBn87WTsKu-pgypKFuqK7ohcs389nug181GrG9HCELgOsUa8DsS7C4VQkBISS58_Kr3sdaG3izrvFSYkDa3J1xpyXLGzt1u8BugfbrslhZibzCWqzI1drK7fw0RWfAiVApDwufXzcNqwv4-4OqaMuBQfE2_fYriXMhw7-8BAHzSB12Ho_mCNfSnjM6otjnjq2ghukWbyldG_5jWMXJc31AWN7hJxpEaanHexMxANQIccQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=ARoICv2KDkoS9LU9B0FocgSQIl30aNQcGNVl2TycoIuXDMz6bNWO7v9wBNju3bIu856r8yyb2OFs5hw_p_0h_sINjR_jyF-xua9iwyuD0pI5KNuNlqdfhdJTRZUAc98WFuq1bKeHIyGDoQj_VPS9PObq2OPdaiw6x2Yl5NvJbXk4VqEvoLY-qot5B_E-miODKDVbWRbHaclEW6vL2kY8o2z2Z0VqKH-Fyebb5znuZNwGEArzUGapYDEc-rjl5PFgID45WTY5ebJsnD_28vZzO3iNCi3XuRWys26Me7n0pPztYDSfaIpv-QW5Q0RX002Bjw4snvVsUFkSU7ho6Kc7vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=ARoICv2KDkoS9LU9B0FocgSQIl30aNQcGNVl2TycoIuXDMz6bNWO7v9wBNju3bIu856r8yyb2OFs5hw_p_0h_sINjR_jyF-xua9iwyuD0pI5KNuNlqdfhdJTRZUAc98WFuq1bKeHIyGDoQj_VPS9PObq2OPdaiw6x2Yl5NvJbXk4VqEvoLY-qot5B_E-miODKDVbWRbHaclEW6vL2kY8o2z2Z0VqKH-Fyebb5znuZNwGEArzUGapYDEc-rjl5PFgID45WTY5ebJsnD_28vZzO3iNCi3XuRWys26Me7n0pPztYDSfaIpv-QW5Q0RX002Bjw4snvVsUFkSU7ho6Kc7vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!
که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده
و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6507" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/as9yKvhayvR3ynG6RG0GEC698DDpWr1D2hyXdiKmYSe_wT7JQ3TYRnySlpu8FwHfBT3lTLxrvOBfYkVBtVkpqg7PQJ7apcE8uivfW3LgnGf1GEEjB8hQnQ3XXk92GN8-TAkxXlfLcZCS3tMj8SjaqNuBwUfwgaeiW89XwqwXQ-F-mbv7V-KHT3-MR731WWPGSgbWnpKFMVnyPooVf48j1mHVrqhf1Eky3NFkuI7veJMhuSC82cbEpEDHa0ea76VBn687fNHHDHZYXW6lyhL6LIDwA5NT3pmeAEuiOiQKCwCMh4BaDfwr1ImWGWwCW9pXPuXXsCG_4IuWlDPU0LuRWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBBCPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLjFS9yZiD978vNq4QMEcuAUrRY4ZSZEV0T6P1GMUMTIPqfylZePjEJ286irhgsh5KjqCbw3t5Rs0w4KlYHmkALOTSSh8-dsOIYUNr9fA6V9Jji2ocB69C3Cthhyf-ckQKLyR0hBpQ48CWYJEuCiE6J4D_6yu7YSaiu-I8TcI4emGFRwoQi5l4j_O3F4jl_N0FQr6FL1wXoax1sRxVob5uEwq09hs9N6Yc7hJwsoHWbUyxjaJ9Ru1TJDpQmFXKqRFMRnQCwzuG650MDVJ6ESWpM3McrbV2ALr3eRi02MWAMjZfuXAIK0rAX4q4Hf8RVHA_1st-G1ZT1oZ4iFK1V1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔻
سازمان عملیات تجارت دریایی بریتانیا می‌گوید یک گزارش باتاخیر از یک کشتی در فاصله ۹ مایل دریایی (تقریبا ۱۶ کیلومتر) از بندر «مخا» در یمن دریافت کرده است.
بنابر این گزارش، یک شهپاد به این کشتی در دریای سرخ برخورد کرد و باعث آتش‌سوزی شد اما خدمه و کارکنان همگی سالم هستند و نجات یافته‌اند.
به گفته این سازمان این کشتی اکنون غرق شده است.
جزئیات بیشتری منتشر نشده است. ساعاتی پیش حوثی‌های یمن که همسو با ایران هستند، اعلام کردند که با موشک بالستیک به یک نفتکش سعودی در دریای سرخ حمله کرده‌اند.
این هشتمین شناوری بود که از زمان آغاز محاصره دریایی علیه عربستان سعودی هدف قرار گرفته است.
سخنگوی نظامی حوثی‌ها به زمان حمله اشاره نکرد.
📷
Getty
@BBCPersian</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29785e012.mp4?token=NDi85aYEOguwMmQgvbb_iFKyzRQX6Ni9-fauKh950G0_EkzwoKhjtTlV7w05Z-LwLl8ynp_HFkiOjGwe83cHh3EfyWZsspvJYKJOjxlt1i-Kf6Smm5rzxf_jyuvtDP9JzgQN5bfogjAoPZrlLiMP5N9gZxvrRiYxYIxSsPki2anIkB9AajSIly-H6dnhHyEILVTIepCpTJe7ocMfQELuR3xqMFpMUXtWLo7nrQXw-LOiWg-hl-5vGxEVQGA0u8ujZrofMn7H-QhvAOo1kZNg4zg6n38Ps7MWBuDoyrbFPpXgSHK3Xqqkr8nKvDl_DvtvU26MvU8HIUE9waylcXZhBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29785e012.mp4?token=NDi85aYEOguwMmQgvbb_iFKyzRQX6Ni9-fauKh950G0_EkzwoKhjtTlV7w05Z-LwLl8ynp_HFkiOjGwe83cHh3EfyWZsspvJYKJOjxlt1i-Kf6Smm5rzxf_jyuvtDP9JzgQN5bfogjAoPZrlLiMP5N9gZxvrRiYxYIxSsPki2anIkB9AajSIly-H6dnhHyEILVTIepCpTJe7ocMfQELuR3xqMFpMUXtWLo7nrQXw-LOiWg-hl-5vGxEVQGA0u8ujZrofMn7H-QhvAOo1kZNg4zg6n38Ps7MWBuDoyrbFPpXgSHK3Xqqkr8nKvDl_DvtvU26MvU8HIUE9waylcXZhBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اثر یک انفجار در جنوب لبنان ۲ سرباز ارتش اسرائیل کشته و ۷ تن زخمی شدند،
ارتش اسرائیل دست به حملات توپخانه‌ای زد
و سپس دستور تخلیه فوری روستای المنصورن را صادر کرد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6501">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=nioRTpzs3VDVQTqulsquoTf_0nNehr72DFZVXCri4ffPkijTtSin1swezpXDnTDybtg86Bhx180x-SRpzCjBPxcXVZF_8JAUdTjmiAU1me9SUUttDng3vUNyiwxrzsmrR6kRcXVBLSuh1ko19rL4fvdEF8_HlpWFX-Gs8MMAx2vOqT2tjNvpDQyvQi5UnCaAdHIwfAPDyu-5WiLM6-rgBR0SJIiC7ogtifp5k6fXLyIxvN3tnWzctqK2kLOwCdPjJ6FrPwit7kQUfX73cHs_9MWpUELt_Y7X4CqV5Cdl4QCq7_SihSemQr8ZxEYcEnvtul0xkRqNvTKIy8dVivYk4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=nioRTpzs3VDVQTqulsquoTf_0nNehr72DFZVXCri4ffPkijTtSin1swezpXDnTDybtg86Bhx180x-SRpzCjBPxcXVZF_8JAUdTjmiAU1me9SUUttDng3vUNyiwxrzsmrR6kRcXVBLSuh1ko19rL4fvdEF8_HlpWFX-Gs8MMAx2vOqT2tjNvpDQyvQi5UnCaAdHIwfAPDyu-5WiLM6-rgBR0SJIiC7ogtifp5k6fXLyIxvN3tnWzctqK2kLOwCdPjJ6FrPwit7kQUfX73cHs_9MWpUELt_Y7X4CqV5Cdl4QCq7_SihSemQr8ZxEYcEnvtul0xkRqNvTKIy8dVivYk4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی منطقی بود!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6500">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=RPfBZX42eILyQqSMlh9rlGfUd9zByQBtoAasIpGz_LWqjDkRwAFU_AjUenR8H-DOqxHrEaCpve6FERy-Sw5TwaJh2mN5CKpiYSMOZHj1GmVpZEryBtGgB4rCY2NHq0XGA7ad7oAaTsQp8PmgOt3Y1J3W9bZq3vGzJWbIMAKBsDeeaNpp4WiWABQ7f90_0feTjja6zWshlR3qiYrxYXGVDba2QXtO0GGAcDoyx0ew8SqoyGCd-WGduLb6kRcrCsFK7uFfiFpLYofJ9mgM9bdrQog6sUVCJuz0WAI3gSpfaKOU19tJOttADr3oVs8XkAmfnHG7U7zDzAJZHxbqMKVfEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=RPfBZX42eILyQqSMlh9rlGfUd9zByQBtoAasIpGz_LWqjDkRwAFU_AjUenR8H-DOqxHrEaCpve6FERy-Sw5TwaJh2mN5CKpiYSMOZHj1GmVpZEryBtGgB4rCY2NHq0XGA7ad7oAaTsQp8PmgOt3Y1J3W9bZq3vGzJWbIMAKBsDeeaNpp4WiWABQ7f90_0feTjja6zWshlR3qiYrxYXGVDba2QXtO0GGAcDoyx0ew8SqoyGCd-WGduLb6kRcrCsFK7uFfiFpLYofJ9mgM9bdrQog6sUVCJuz0WAI3gSpfaKOU19tJOttADr3oVs8XkAmfnHG7U7zDzAJZHxbqMKVfEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERhX5mrGxYm9eCrv6Tj4yz2Jl63QbaxdW6wklfICB9heDNWhe7Uu6ETsrYXnhIECrIAmkWQ09E7CLUke7YZGilFwhvJAMy7AIVZtJoKfz4nBuhIodbeYTmK6mpW1xJEVWsW5le9Enzm9Mz278wymr36KpRXfUEI7DqyBz_cqa-GTVaHy9E55fCrZunwyh6rbUywKLSWoe1t2j1PhFUSfNyJu2mDSTmz5F5OoR3WWsjMB4QBijZokNUiDo-v5DTUNldkj2zeupnWGArImm5UeWW5x3Txai42vLn481LQ-nP1pYxe_asyEC210axuOCPKmQhe9X15dAHs8FylAqNfrHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrY4fkPK4PyfziZMFWMj8bvqb5GmxY2weHg5U7P1Wn5ItQPziHjun_i-ocmGqSbUE0twwDzaYzWBM6QRi6PLrXI7lIicqb0gyWTbJv1klm4LAH4h6XJ4VN9vCVfsq82WUvwG7e8ZhYB6k6cps7hg0muxApeWIlktBz1626A7dPUt-IJ40pST-yO0bjWj_-QWyd8yfaC-sN90j_GIvDqTtd-VeCQ8Yk_CeTDfCqpdaFW90BefqDI6TEW5uhbiWkdzLlQ1faQ-csADC6tNP0ygX8Sa78M9G7mc3aGVKkbpQBLEAraLR6ZYEMF0HFMc4R-51Urj5Oe-FBLMR22RcNqjmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtPJHKtCjoa7PZck0cRzgiPnd-bQ5np71wOwytLPAwM2swj5kcP3COc0BmTyss8dvLSza6lx6ABx1av6lbUCHGuggDooM6jjhQnrNib61CRDADld0VA9lx8korC_ar2st3XrYCebLFPFLH4GpYlFMEBpK2WQkMZwnfS7qlLJwNN1k0gZOOeY22tBSrv3fkJoT4XS_U6teVuQ6r317aPZCob4-vnAyepsGy5ovyIXi4QZRygFaXBDKsigrRn0uMYBL0_jlrSdpi2NtuRWlIyH8OWhfJcO_6rjBvwfvD_-KmK49gPDd4HO9LV5_K6zdRnkUIYiMlzdLuG0aRPZQ5ooUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.
عراق : از طریق خط لوله انتقال نفت به ترکیه
کویت : خط لوله به عراق و ترکیه و همچنین به عربستان
بحرین : از طریق خاک عربستان و‌دریای سرخ
عربستان : صادرات از طریق سواحلش در دریای سرخ
(همین الان هم ۷۰٪ صادرات عربستان از دریای سرخه)
امارات : دور زدن تنگه و صادرات از  خلیج عمان)</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=J1LcJjy8PP05jkNsMrwu9Z1u6mMU1nfeUwjrH3Ibjq1df0lHARlDFzcjcr8S3625C_byP6tJptOH6mk6ZPqS3LwjFj_gvyVMHzYQzPwQF5PtUFHxQ8dL9Tf8OoyMQIwrdfLwwhElwi9Vl0ftOaEzxvLqMJa66HtDv27VpF_C-oBKYIhvOZiK1qgLcgUdKLLCxk8FLSUdQT7lVCDnJeTpw5kxZTaHqyR1vuvtbj2SQ17gWFJEaAhiUwDoOEkgvk4FP3W5_zY8nT9c4HN_XWLkBbR_EYs_-D4Hmte-G0ukubBw1OWD_AXAhdW59g2zoFpSlKJjgzyiCnRQgVLl1LBiwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=J1LcJjy8PP05jkNsMrwu9Z1u6mMU1nfeUwjrH3Ibjq1df0lHARlDFzcjcr8S3625C_byP6tJptOH6mk6ZPqS3LwjFj_gvyVMHzYQzPwQF5PtUFHxQ8dL9Tf8OoyMQIwrdfLwwhElwi9Vl0ftOaEzxvLqMJa66HtDv27VpF_C-oBKYIhvOZiK1qgLcgUdKLLCxk8FLSUdQT7lVCDnJeTpw5kxZTaHqyR1vuvtbj2SQ17gWFJEaAhiUwDoOEkgvk4FP3W5_zY8nT9c4HN_XWLkBbR_EYs_-D4Hmte-G0ukubBw1OWD_AXAhdW59g2zoFpSlKJjgzyiCnRQgVLl1LBiwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم. می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر
همه مردم برای ایران سختی‌ها را تحمل می‌کنند!
[تحمل نکنند هم یا زندان یا کشته میشن]
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.»
اونهایی که به قول خودش بین ۳ هزار نفر رو کشتن، نامرد و وطن فروش نیستن، کسانی که به کشتار و ظلم معترض هستند، نامردن!!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">جزئیات تازه از طرح تغییر رژیم ایران؛ قرار بود کردها «زیر پرچم شیروخورشید پیشروی کنند»
🔸
یک روزنامه‌نگار سرشناس اسرائیلی در گزارشی تازه نوشته که هدف حقیقی این کشور از جنگ ۴۰روزه با جمهوری اسلامی ایران، تغییر رژیم در تهران بود نه صرفاً نابودی برنامه هسته‌ای و موشکی‌اش.
🔸
نداو ایال مدعی است که ساقط کردن جمهوری اسلامی در حالی به‌عنوان هدف اصلی تعیین شده بود که نقشه راه حقیقی برای عملی کردن آن ترسیم نشده بود؛ تناسب این هدف با امکاناتی که اسرائیل در اختیار داشت به‌طور عمیق بررسی نشد، دولت بنیامین نتانیاهو هشدارهای ارتش این کشور در مورد مخاطرات این طرح را نادیده گرفت و به عواقب آن، مانند آسیب به جایگاه اسرائیل نزد آمریکا، فکر نکرده بود.
🔸
این روزنامه‌نگار در گزارشی که روز ۹ مرداد در مجلهٔ ضمیمه آخر هفتهٔ روزنامهٔ «یدیعوت آحرونوت» منتشر شد، جزئیاتی را از مباحثات کابینهٔ اسرائیل و اختلاف‌نظرها در میان مقامات ارشد سیاسی، اطلاعاتی و نظامی این کشور پیش و پس از جنگ‌های اخیر اسرائیل با ایران ارائه داده که خود آن را «اطلاعات تازه» خوانده است.
🔸
گزارش «رؤیاهای بزرگ؛ افشاگری‌های تازه دربارهٔ طرح تغییر رژیم ایران»، نتیجهٔ «یک تحقیق جامع» نداو ایال بر اساس گفت‌وگوهایش با ده منبع نظامی و سیاسی اسرائیل بوده است.
🔸
این روزنامه‌نگار مدعی است که تلاش او تصویری دقیق‌تر از پشت‌پرده‌ها در بالاترین سطوح امنیتی و سیاسی اسرائیل ترسیم می‌کند؛ فراتر از ادعاهای پیشین که دو روزنامهٔ «نیویورک‌تایمز» و «هاآرتص» در ماه‌های گذشته در خصوص تلاش دولت اسرائیل برای تغییر رژیم در ایران و جلب همکاری محمود احمدی‌نژاد، رئیس‌جمهور پیشین، به‌عنوان یک گزینهٔ رهبری منتشر کرده بودند و به‌شدت بحث‌برانگیز شد.
🔸
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از بین بردن برنامهٔ هسته‌ای و مهار توان موشکی ایران را هدف‌های اول و دوم جنگ ۴۰ روزه اعلام کرده بود.
🔸
نتانیاهو اما از آغاز کار پنهان نکرد که هدف سوم جنگ هم فراهم کردن شرایطی برای مردم ایران است که بتوانند کار حکومت جمهوری اسلامی را یکسره کرده و اسرائیل نیز از وجود چنین رژیمی که نابودی این کشور را عملاً دنبال کرده و با تشکیل گروه‌های نیابتی در محور موسوم به «مقاومت» در اطراف اسرائیل «حلقه آتش» به پا کرده، رهایی یابد.
🔸
نداو ایال گزارش خود را حول این ادعا نوشته که «تغییر رژیم ایران» هدف واقعی جنگ بود، نه یک خواسته فرعی یا شعاری تبلیغاتی.
🔸
به نوشتهٔ او، چنین هدفی قرار بود بر اختلاف‌نظرها دربارهٔ ماهیت نهایی جنگ با ایران در میان مقام‌های اسرائیلی نقطه پایان بگذارد، در حالی که برخی از مقامات و نهادها همچنان خواهان محدود کردن جنگ به اهداف مشخص و معین نظامی بودند.
🔸
نسخه کامل این گزارش را در
وب‌سایت رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=cEsUrecZrhkDsyLvYhvEwA6pdyWGsfPN3pJ6oUXWYaYnXG_ZlO3f-BuBviAxdSIC1szcm__E9_hjYCi5YQfbc2UkFgsGpyEV61mSsR1tjD4QPCd7to_XxVxJEdI04w22iPga07JaWU8nVwYxxdPaEJn--lH8JFHGgzY4fj2dGH_eJ6TuJjispECP9_U0ARPXxrgNQRCti_-vJJo0cRD47pet1Uc9zuMCN7qt46eFOdvdOdXN8t1lDqhNERdZrvQzGtwPr5znXx5rJyVjdzDUJGGResmBz2Ns8QzOV3S659IpPso5_EDzSl25adDW7dPBfiIOeYxfn6_3huzaU-ooSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=cEsUrecZrhkDsyLvYhvEwA6pdyWGsfPN3pJ6oUXWYaYnXG_ZlO3f-BuBviAxdSIC1szcm__E9_hjYCi5YQfbc2UkFgsGpyEV61mSsR1tjD4QPCd7to_XxVxJEdI04w22iPga07JaWU8nVwYxxdPaEJn--lH8JFHGgzY4fj2dGH_eJ6TuJjispECP9_U0ARPXxrgNQRCti_-vJJo0cRD47pet1Uc9zuMCN7qt46eFOdvdOdXN8t1lDqhNERdZrvQzGtwPr5znXx5rJyVjdzDUJGGResmBz2Ns8QzOV3S659IpPso5_EDzSl25adDW7dPBfiIOeYxfn6_3huzaU-ooSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=RlMe3SCZgySOFD-qZD57BzFVX0zuf7SM-9mT4PJnw_4E7FTGZaKwtuxG3BoI-Kku7blbp8iJR9PfkpB-g1V_e7H1dzJ4gK1g129ugQ6QLoLK9e9nXXSc3xTG6tbbBSej9pJX9FsrZBFfL8W482iRs9LqK55vwk_RuaesS4sN01lNm4VWksFMhhyL3x_z2VWG7XJCy_56vO8c8iTabrMkG9OPkS-ToYJSdCTd57IqqCBYI-PWtYsRQMyJMVrfE50Bza-qK-f2kLMRYxe3sJXRO-z3m7C6tul9dcfgqKn7-zg0tdDDqi437JXTsWftFpTeqFf_osewIGqDiZ12pN_J5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=RlMe3SCZgySOFD-qZD57BzFVX0zuf7SM-9mT4PJnw_4E7FTGZaKwtuxG3BoI-Kku7blbp8iJR9PfkpB-g1V_e7H1dzJ4gK1g129ugQ6QLoLK9e9nXXSc3xTG6tbbBSej9pJX9FsrZBFfL8W482iRs9LqK55vwk_RuaesS4sN01lNm4VWksFMhhyL3x_z2VWG7XJCy_56vO8c8iTabrMkG9OPkS-ToYJSdCTd57IqqCBYI-PWtYsRQMyJMVrfE50Bza-qK-f2kLMRYxe3sJXRO-z3m7C6tul9dcfgqKn7-zg0tdDDqi437JXTsWftFpTeqFf_osewIGqDiZ12pN_J5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تبعیت از ولی‌فقیه بر مسئولان واجب است»
می‌دو‌نید شمر تا آخر عمرش
از اینکه در کربلا شرکت کرده بود
هیچ گونه پشیمانی نداشت!
شمر خودش از فرماندهان ارشد امام علی بود!
توی روایات اسلامی هم هست که
هر بار بحثی پیش می‌اومد دفاع می‌کرد از کارش! میگفت  تبعیت از حاکم اسلامی بر من واجبه !</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=diuvaNph85_mnTqs1ZMrw9KF1r2NByruRkeJ_sql5c5ROBknHBYx3NhFOMHyi4qMpBR3qTtqjw5FKgAJLQiLwv3IksU_gW1ogh5qzzsojAhagUNR0RPX0ttSn195bFN1GML6AF1UbfY70jzxGYxraInxcLJi32iPTJcKtXzYnSsz9IZ7OVdlx_biaSNkIHKL4Un8ihrONPfJSpBI-LnALj129V4PSwgPS6bjqK9Js-fBsW8w-Ut_0cJE5pOfobXLrMSOHUYRtRRbHshCeJqryP2UU8ZAkw_hVKqomd65fe4cet6wqS0u6CVC3bPAdTUrHCwZaR6Uif5uY2EoFZQ3xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=diuvaNph85_mnTqs1ZMrw9KF1r2NByruRkeJ_sql5c5ROBknHBYx3NhFOMHyi4qMpBR3qTtqjw5FKgAJLQiLwv3IksU_gW1ogh5qzzsojAhagUNR0RPX0ttSn195bFN1GML6AF1UbfY70jzxGYxraInxcLJi32iPTJcKtXzYnSsz9IZ7OVdlx_biaSNkIHKL4Un8ihrONPfJSpBI-LnALj129V4PSwgPS6bjqK9Js-fBsW8w-Ut_0cJE5pOfobXLrMSOHUYRtRRbHshCeJqryP2UU8ZAkw_hVKqomd65fe4cet6wqS0u6CVC3bPAdTUrHCwZaR6Uif5uY2EoFZQ3xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n63EPtqIkClybEi1PZURK6n-xN8ZMmXt1ZxdpQQIshisMcsLnwxtGqDhkMX-7ndyTjoIbI1xm270B5_UCNrKE8xypM_3D-Gsy0ulANOvC8YYQ0AS6A_-6JNAQZzid89N0i52GWOIjnnCHGVlnJ_J51ma8qloZtRuivy4ox2GjHYXhuz8AxXVRLv2t1hdUorbkM_-0DcCVCZPC80pqdttAb-3eLrSm-qPjZBM9J7JoQSiS-7yPYM5z-UYOGrNIMi0S4jDjo3gFsYeMroVvqvKgZRvC0xdekpyyT6IoLp667lE0n7CQ5xJcyTNHkw1PtZNurAGo_UkdIJGxThVOnHNGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEurb9S4HJiRh9PJc1Bj_GyVifl43MacAKrYEf90cmIeU1G3pvCCq3SjqVlXDnGBOtx2dmYZv5gQYqCKHwaVdro3gGlxwd6VlMVuQpcRDl44akcZBYaWe6jo6j6gFZemNDg-6b-vRmUzenp6GKeA723J76DM5DGUN4BsBY6KEDI2UfT3H5HpqNqsOOfdLatpIVwYagUgGoJgkFJVJL4ixjKMV8ZWokOnt9B4BD7l3bHa-14Gu9-YU_Sva9yXS0EPz-Awzcs_k-AO7CGjA4_vQWG0nxT0sLVdeH5ct-5_dMATYb0NodRxInZMu9zt1pO_PrTsi9TyHRTa-c6H0adZfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z0ZGS5VUdHCXdXyx3bNK0SCkFfLkIpm0Q9atgi8npLVMPH8lNQe5GyZyuj6HDUaoPbmoVnDNoaLd5JYiKObabMSD5H1yUhtYjsN79jxRoU0BkW_AIJfVa7FmuzDjZZWQj5QWelP7vqnaVYp5Xz0hBq8u7tqA7G_7TbIYsk_gbRprPmj3fKCIPe0TvVlY2DJwBhLT1bgTRLrBltkSIhS6eEozDXbSmepmjpISJjN3n9ykFtsgdEuRXVj5ljPXjondrlSTyi8ywfjJ2mb-5teKp57XdVDmBtlrdXSVRU8Tli7uFy9taZCG0f4-j8wheN922ewg6yIV5LjQAmxE68Z2pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W1z61wHGW7pGNHkSjAXr9tnaIomcDLXm75jd_jpdE5vQlrHxF2YIXkNI0l18YzlHTiUJI2PKaDI5tD9ggFK2YQYcnDPNKeHvGYbByPpO3i4YyuAW0I5niaM3v9xOYOF9s1CSUVIMcVINBb8-Ka3fCt1-tvq8OehgdC77L9O3Wz836pWVE9xwVk2yvY1UqgI02CwNZTlqP3bifKVPg5IjJ0c-mMExqzJPX_28R2p8OoLaOn5IHIR3vwbn6EasrwycCIGHSy-aCsHN8DcmDNFfj3v8Rj07h6FWkEXMtqmEWFDxRYk7G_u5OkJ7AX9EnbXe0ByjUcqfe8mzOBOkgKyyCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sN7EEC-aVGz6IxJK7KAd-ehzrg567k9TgnRWFplOkRmS31gzwJwbR6xnCgrwokh4lxSLEmyayE3oS_LlwS_i-R2Fua6CKb0xhrDsYpkdmKmxKMtbMB65IZUVnsQlIbGGLH10HYUia56-gFq9TzBXEgldFUJS72QX0D8GzE-DaZXFdlB7XuEBZv7fTuE72GR9jmQdcbXJ6b9lzFyb9Uyt4K3rAbilhdb6A-P1euDCfAL8uDgm0UPOs1s-B-TCdi_6dgJO0ds_phOH37NBe0foNK7g_Ez4lor10K92SjuemRvwymoZdSbDqLQicP87bhS4_qVefRqBDqEedgxgAb2x4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQizy0I638ppAvdwIhFR3eYrMSn8-CJAhicS6PmwouqMfHuwrggagzbvCwKK_42mWjM1PRgkFbBV4OfE_ylBgRf0Z3SXehDHcyihALG7l4E_TPfANk2ucekjChU-o1x52MU57pnRnam6k9t4jl0TGSAMQ3aAit6EhMrBJAz6BqnhrXoZVDiT_RuO4BE01FIMJeIW6dpJ3Ny-HW7c_crv4jCcwovH1wP24iqT_Tq7SMERaRkW1bxtz4fA83EYpjlFch1ioz2QgNkYmFC8psbbMkdmwxX7c36ILYOFNybgAjzCLAKUa8L8jINxvfjufujoz1F_CtQ-5QxHZ9WILpS4mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKW9_BQBTbYQguIRI1zfcpcc8LYukqIEh40hvIgqX5LQ5fQIG9FZaFcqtVTak958zv9i0RCeNLRvUbWScQ7oPL95f-WqHACG8AWa1UBN5afYArLmgLolhQ3FhwjKpLJXa_3ATKY3-AWWhrdAjhW64okoH6DqBItzFuhG8-SVqDp20QP3N2wILPGWGxh3RPdusUJgH36jD-CIpDlbWhPUArdlk8YS7jjD4enmeL33-l6u4j_S_EdRVXNzqAMPjv6nfHZC-NtUDzziOeiRI_8eyW4JFjM6JXL39eQ9kejAlsG2hLkJkrvFJCgjbY0-FHf07z7G1E3oWjxF3fGZYf3X8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtD1lpurlw-pmOjJxW-Z_YyEtnvdVhJ6dmzSdBerHpyRMjZ1AKeeuzZK0Va471U_SlHmr_ccJFWk_D-vUsQG-JU031pUJmTWdKst2u1PbCD_FgDSamQx0ZuW3LsKiBXPSFrh2CxXQLZn4FopaxM55iTRE4nxai0lGawimP2884fs_v3GX-fUYrJTosdga5CLboss1SrGeosP67MjJGq48kaswhsCYmL2aHJDjM_l7LeqsxYmQrK7nIMUeAAfTzX3WfRz_Zo25EzWpxqtmmhJSTUCULrJT36GnKcB-x8y-fFDUokBefYEjuB0e8DcrpN-bmML1yOX5FZMQatS1zixMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rgub7rLauJiYPCKq-EKX74maCy5SH3Mdn0KSnk8K-lyj8XnFbdjrdQLRr9RHAVeuBHntG9gPBJj2uRIVo5KGht2uSeyLCJHbnHfraJcFejDGMucFVBME09En2__AbGzAs__u16yeGjPKSkThEep1k8ObN2wkTwBInqnGQL90ToFDnYIFWbh7tQkVYLZuR0A9an1YYnS-eLtEC3veI8eM6UQvjh_LKvmaYQld8_n79ZS22yw5mEnOTEMnv2Ut7o5xMai6lDAR79qp844PfiKE3Tp3UKtFfm3R8bCKVIEpxNO12tAo0-nAkI6UnjxhGx4zaR870AFrwN4nLycid6KzbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرعون، جسد نخست زاده خود
را در دست دارد، زن فرعون گریه می‌کند
و موسی و هارون،
در گوشه‌ای از تصویر دیده می‌شوند.
برای مجازات فرعون، پسر او،
و نخست زادگان «همه مصری‌ها»،
«حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس
که در زندان بود.» همگی کشته شدند!
حتی! حتی نخست زادگان گاو و گوسفندهای مردم مصر!
و این تصمیم و اراده خدا بود!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nG7xvnlBYTERksWZQ1RaEpHFDMNk1mKEDf4p1CS8_ZmlJRKrZpP-JiZ493cqwXNXybI_ixWw5-mj-9kWD_3NlMVxm-HSMsksocNhqecIq53Kx1-v00nospugJ2lYUzx2Vp0fT7irWcCVMrDhwdHoetNZVAaDsIaKQBEJg9bpgBaxg9LdDtfDY78rfQnSAf_USIwKXr8hYd1EIjCD-ETZVaacMXQK_ryXtpdLuUiiYF6FOnA_8S5J_LukQ99UaDXSocxTdvfYGjtp5W5kIWE4bZBQW95hZ669oBwVrXDodeB7-V1HpYKkKX7NS6Q2yGWBtCKiCRviRBEWxhgJ5vITVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLlVXy9oO3_wOWsAVltZBYyk7NMLHWC56sVOrDZwbwNlwfIs_yuqHJfFvtVjnHCxOX5MOmAbaQUG4Q85kzaX8KXbWfBavfJc4RyNZUV5qKlhGHjkEjYy3RBU9xQMBJjQ8E65qvDlIAfnjbNgosD6mPmleASz7wg9ybrjkPyDKbKnsTSLeU9QGxME8cB4MRCeUAfRNKrIvthHRg4wNJrhzIafQ3Uba1TFO9lPTd6Ujdj4ihgiyAhpjoeMDQucHIv99RoWJRpgCZ52xU1ggd29o0EDoMM89GkTLvnLCuvmq1caaD7xn_AXOfjvaXTbAiUYbrN2NeNxtBHliCPW4OlTAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbzEw3qK97SAYP7rnBenneB1IjeZZWQDZx7ihWj-LjoW3Z-Euc6aj04rAPuWC7Cx7-yIkzyxDWR3gsbw7KAVh6sUD0p7bV5kkArhgY1CdwnWrqaz4fTid1E4Vk0ehrYsmDHARMux_BaZHsNuoJNkRRFPXhuasKnc1lWy16FuYWu8kXkA5XUQV5YZ_5Pcl_ipiSNi2uvMz8hPZpCtao0DfyS56UB4dINfELaSfOcsoJWp33A_ttxeZlGjJzS0I_UBeKmu7u0EmVyhg98cQMF73tNxldr7HWUpNdo6k2BmAUbt13c8i0yn0a8KsutEJyAW-HzEEadzKwqtjjcjgIpY6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMOWPwZ4Xek96sJarPV3q1R34eQrcFr5Cg8jtWZEhClL_WalpVNjDAVXm3Uxs5Wc9WgaKqB5bfB6QVOQfSgWlYbxx7SJNNh5A38F_eJ58QSkkOb0qkd1aIcI8BLchHazih5XuoPYKnfwiasMRmAqzjTba7-BcZTT5T2oOSRxDjLFufucUI8ehGwxeAwfQITbifgOUXvGpR0v2tkdkk56MbAL2n6Hrx0SlvbM1vu4A12GISodB9N-bQtCyNf6RScTINN05n_osl_8Qjz45-hWUkjTgzUidnPCjJyBapbJwe4YgsyaVq7kqle5wfHvAO0O6PmiNDC_HgT4skp9axXQLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -
سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!
تباه در تباه!
خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».
احمد شاملو - غلامحسین ساعدی - اسماعیل خوئی - منوچهر هزارخانی - هوشنگ گلشیری - باقر پرهام - محمد علی سپانلو
اینها روشنفکران ما بودن،
جامعه آرمانی اینها، ترکیب کمونیسم و اسلامگرایی بود!
از مسببان انقلاب تباه ۵۷.
از مسببان گمراهی یک نسل از ایرانیان،
از‌مسببان  تنبیه نسل‌هایی از ایرانیان که هنوز  به دنیا نیامده بودند!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0wRxRmQTCWocnUNQFDtUVcN5a_alFa-FPHWLPSWK_Bhn2dwlINGvBWhheCCeJR0057c95Rjy8W6z8hwWTJehPmHe3FzhBsN-KOVYbx8y7wV7wgO0ffCY8siJ4_KAJJwtPi0-Q_L5ZEj8vcky57rCa5kiMtwFbwGwrzkxWuM2avSl9ja54Mf7JGsviz8n8cPxH3tAFcMKzTrGlPVlO7OpXrS07j_iusRyulw2D_EJuLmBppDi0e1haReKNm2t24fPzZuhYrGS3trGjO44aq6QqoMJ-nHEuM7ImjDN65YMrp-BkuQGtJMrm2FEwneEVpFQ0bTEVbI7pvojZwOWgcUHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=Tf04t2ZRessNpjc7WASm2fDmK19pGfjdlowYcTUL6leZWN5gQ-5O42Hk3FJLLyUcqw7W-AaQxDGu3gZ3Ra8aJNvhWKwpqwc_e1KHgPvxCeCF5r-GdhbgAocAPy_jhNhIDLwGvMltoHicghgRAJScAsUJhp9JH8Ji2iOor-7dbVQ-83TWE2Myy7Q9wR6BXqiwKnBeRhrDBSpAJQIXhyBztbQeO3ki75FqrOu6GVniJG8Evg7qWbJx--7jkkCOo4cJbcwD84Tlf_QWm7e_y1V5CLTHb-8zI36NPd0iwWx1TogMgsOQwMVdH9YQ4SpIrsSgTyyXEa7LvxN6Dj8bYqxiuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=Tf04t2ZRessNpjc7WASm2fDmK19pGfjdlowYcTUL6leZWN5gQ-5O42Hk3FJLLyUcqw7W-AaQxDGu3gZ3Ra8aJNvhWKwpqwc_e1KHgPvxCeCF5r-GdhbgAocAPy_jhNhIDLwGvMltoHicghgRAJScAsUJhp9JH8Ji2iOor-7dbVQ-83TWE2Myy7Q9wR6BXqiwKnBeRhrDBSpAJQIXhyBztbQeO3ki75FqrOu6GVniJG8Evg7qWbJx--7jkkCOo4cJbcwD84Tlf_QWm7e_y1V5CLTHb-8zI36NPd0iwWx1TogMgsOQwMVdH9YQ4SpIrsSgTyyXEa7LvxN6Dj8bYqxiuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGPOmt-LV3qwPoLdZotlMHFe2SWx9jluh0Z_pK7BMCz95tzFH8PoVR_HJ1yeWwAYPc2bH5LExvYLvbGIlY_XcXMiy01zT5UdTIuOnB-fPNteYSMt26e59y6is9SZLiqcfGKoMXT1ca-F86clesAUi6UyU9G8OEzFya01fm53fkG-vyOQ6GgSTZPgtRUrLg7fUHPEfWScNFDCZkbyWhb0phtidm1QiGtLm2N0dyEytbOmP0bLC4Ad_cQVL_-acToHZa5h_3bZIFifHkMFegTxqcmt_YjEvSKZvQ6hJSvwSrphBGBLGPATfob3Z_xXPyB1DgEcRRTwhvQZIJC-1kegsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHxfTGqFBwairAteUN3NgrOPmx5ojwvhxbaRRFP6pE2xB9RPogt-kuN3jRh2e7dyekQOmViC_yupU002nuV0pYUHLwqOcLoGOeR4LxZ8D0tuUF325lyFDdk70l0-Y2RvdFVjaenKICE1J3cedtZpv6v4bCfbb-JsVuveExkiec7b3m6jM7pelr1jFPijmG4WAuciKA1jsAq1gEgvMVF6WR3MfbfK1QzYiWaQWlS7JuHTrkH_pr6mt4iaxAVa4dEuPnhdONCL7Aj6W_4ovHfozd3GT4ohUCO0uyuqcbFrnzjUmhfi13J8sHK3u7k-qkUAOzYZDytjpGnwmoTcm5-G3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJxNq_hKbYxA1QRbskvU8DF_dkBgr17btEIqVVPNkTsLKAexD3kjm1UPLQ-PGyq-ksW-cGLJdcgXUWTaFNDFTYf2f4QFo13vtvbmX6XU8Qrc0KN1vOJxTIVOj6DDsPYzDaKZX8FJyME5mmqhEYpwfD9u3JB5OJlzI1W7g2YRi-tlz1V1IYoV8zXwoWqZR1EXLn2pqT63lMeqtkZ78c0yBv9EG16Ws38iIWZ7XCzIA0BBXEmAlkRIoqvqco3ZEoxcOuRvogMznpHWSgsWE8I1Bsr7d4YMUVOfur5lySLCG_oOuoJHFjL17EIqL8B6asBCdZvp0vh0Y0wV_5qJuAZDjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHlTobM9cuqIyLKy2QnZUNKiMN0ALUT14IUlgZrYBtt8uOSQ1qwEbehznRRj707semIcZmZkZBkrkxr0MrZBmq7ta6qZFHIrLwu5ShvZy9TFKG5POljiI95dqlFugGUZinoAD4jkBR6Yo6ei9RnqQLKeJSCeBh5scGNcwqeGVr-lEplN7EAoAO7p4h60HenmuqX1CyXcSAhbDEq5NnvjrAoV9_ElCMkh6BubvRx4N3aVQrCGGwp8xpjQToYHmSXucjw_nTAUh-L9luIkIRfCv463k7j-WWZrnj50Q2eSY91f_H07YXDIcdyJ-H-Eh-AgQsZZAODQMfNNhXI1vcxHrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNlmjjrPdxW-8tlM-PWkBt-kESCmEI-kNCnpe67pbDpjes3UeJ2nEgGaznJBwshFNn9TkyE7tN5Hpb-2kb4mGypw2XLmNam99hW_feZ_FFJ1KL1ID8t9yFv-DThCwca-5h18xFHECwBWU6B7GL5Lgt9utq8IjVT2X8rK_cEjCEHKhpMgv3yoSlyEDvxTjtcbInUjIGlElmTwyDnvsSzzJrAILXXaGp2r8CvE8FIYUGITKBzdDGttGfTqDlDjzIZw1A9MMNIzxhrGQCzCAZnG2YEDUvjeQ-ChjfYyOW0AyWJ4I9ZWFudo6NLB3S-dxONIFvaXwJx3hXYYlq1kMwqXkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k80aMW_vacuDBEOs216dE0ulawA85yw4qDqHBQoKkOQA0QDN-vInEBjQVMMnjXSxQJSWavjCGRIOU6-oA8PsMXL9Bogtb7gOAlrKtPXUKyPkMss6U2cc-_ik7XPOWoTfttOszlip4CBr_SVBD49C3tudRQQScsJ_MK14bcPYZWdN4BtkoDngIlf66es2pRjMaqdLUwEwYDRIEmpaC1NI_SFVmfbAgehWuN-bVVC7_FjGtU11uvu_wHbxDmO3BQaG14OjoomnXBdcZnmwiJOUhouPQzZ2i-cb8RDF8sB9brvEmH6R8GR4YdTtrTFZ2Tw8aQngLuxMDTXXu3sVhyat5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzyXKpUeepFd5SloO7rYnkz7hmsp5xCS4H8Ac8DppMTymW6uT6IbE8ii2u1f2ZVUAW3x8SMEgvQXl2E_nlUfLn0ZZpKBQzn8pg3c2dRVl0j5b3ZU7I_6JcL_9EmwM_n_gGwKJmkd8nAZSlDKGoXbeI4wHnKnyz5tU-LYuA7mOEeT1UIq0yKA2Nej-GIjcAe47-fAgtH60pDlk_SeP_1vjBWgY_o5-QJ2dCDm07LC7UcLUCuGd9oPwu5W9iQ1mw55jjJv5Ddjw9vLCF5rybSoujwt-rEOK5WkELLArf2OUP_A7EFVubbJ0ji30qhHfZATR59PuId5lG4DMeF8-5RorQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3lUJC5t6ulJkkNDXq2Qu8ERK03Wa0dhsDOqAnQqyXoXeVpx2d00_zE9DB91HeCR8y_kQnoZE1DzTUbA4rAvaBrCA6gpdz763UuSNaD0tMlbwMCrDpy2Y8i4YVE3T-CZ2MLaxmKsqTn6KB8Hl579DydpBm3L1KCypVuj0IeCOSvMOtItCJ-6PcX0QVDbRuucnmBbtXoVKYBKx2R6VNpBXTtm5MMgvgkwZHuyf4FgXGOWy8xm6bZa53BzOB6yEabaRBDjdRmi8rDfmPCOmZEeqjA1lwt17rtRSW3vu5aC-uTeUsscEq3WWuvSInk1nf4xF6ZbcDQIkbFhoSZjakSkMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دولت ایتالیا آزادی رفت و آمد هوایی و دریایی
بین ایتالیا و اسپانیا رو به طور موقت لغو کرد!
این بدین معناست که تا اطلاع ثانوی،
پروازهایی که از اسپانیا به مقصد ایتالیا است،
دولت ایتالیا مسافران آن را کنترل خواهد کرد.
اقدام دولت راستگرای خانم ملونی،
فشار بر دولت چپگرای اسپانیا را افزایش می‌دهد.
دولت پدرو سانچز هم اکنون نیز دارای کمترین حمایت شده و پیش‌بینی‌ها حکایت از آن دارند که در انتخابات سال آینده از قدرت کنار خواهد رفت
گرچه برخی از راستگرایان امیدوارند با انجام انتخابات زودهنگام، انتقال قدرت سریعتر انجام شود.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=oKn8Un6pfyeZfQfyyE49ugOTsnmCinYNsiSWre99sZxnEjetzVK2CalRPEd6pdE2LfydnE5JUNE6Mf0jmpp226wActNXKVdS8c1fMXLRw4ybnMxLu_bN7jJyqupe2oIa0S2unZtTiBp4PRLtYmtgozT77q-rFb4ypJnsqN59-Ylq33uPaJszadLHGaXtywlSZCYpR_sCKGn7hkV5-ks6lMPe2GuPssxNnVUzfHDCLvqQUWyKf1-8uyFEHxOEIKehJPpDkokn8c8z-jde3975r-3_gCbZkkEwvO6YkcvHwuLZHqXy5mO6tFj-9hvR4JKwOgOtrwxrpGBcx2yQjKv9aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=oKn8Un6pfyeZfQfyyE49ugOTsnmCinYNsiSWre99sZxnEjetzVK2CalRPEd6pdE2LfydnE5JUNE6Mf0jmpp226wActNXKVdS8c1fMXLRw4ybnMxLu_bN7jJyqupe2oIa0S2unZtTiBp4PRLtYmtgozT77q-rFb4ypJnsqN59-Ylq33uPaJszadLHGaXtywlSZCYpR_sCKGn7hkV5-ks6lMPe2GuPssxNnVUzfHDCLvqQUWyKf1-8uyFEHxOEIKehJPpDkokn8c8z-jde3975r-3_gCbZkkEwvO6YkcvHwuLZHqXy5mO6tFj-9hvR4JKwOgOtrwxrpGBcx2yQjKv9aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXD7f1ZNghbwk67gHDD1Rp0_0JWdJSLKVm4vPaIN7u0-dM_RDpIZTLqaJYBM6Bjx4adwy29cpi4aDqxI08FSdtDn7kwT13Pecm-rrLfQKHHQ8nBvXUA4ASEEy7b_1c4cotmM1SnC_JsKh2-QtlDyup4KixPNYqLF32V5DriKLHmk-QVmJzGkr4g8Qg0dVtw4nvQIU9ijxwItmV3TnbNQBFX7CO4gjNlQeKD5yRguIDrMt5Kk4slsCwB7tSYnXo8K8LsFCI9tCHqq2giesOBG3Ylp8oEH1yG4Mzus83G8eavVotL-1l1ZNzEj2DgFoL1EYKxb6KcMwhBeoPTqzGS-RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xf4Y5E81nhRLwBtj6-6VH6WEdN2fIqj1m6Z2GfikQmzLAEyh3s9ne13M9IwrtablrAPHxbW15WBEk-SrMJDg6mzFawCRjoyKHDN6vphQsSDjmlsA1qZ6NMXu8O2P8_taXJ4W9JiVPXLl3dVZg5KJcD5BwaQtZI6bAEmoz_A2-xjqQ_ksZu5gh3kjYQNP8WPvCTZn5SzBely9ax0EI_QpxOICB3HOihRD4n0n9AAOEfMDLTwk5OSQ5Ro8SltNfe2s3z-zUFS9JIWYxPGXLJegWUJEdxKqPEMhIlQgtnZNstdebPCetxNc4O1sCCL9sHic-r52i6M189LKFX-01Jzq1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEAAYeYj5E_UHcUwc-VWyJoJa7Y8RIUvrjT6U0fABt1glFPPXUFcFMdso_HzZvw9bHoJK5deRJOInvy6ErbgYMJSKtvOsezBYoFV7mZoXdDd92i27muKV5YEL8IrIUStodPIUOjtnFA3bR2cHB5OEImp6GMqKZywzYVarseU2a3I_oc3a4a9SSR9HHGGqC2PVjrOEnGQoHiFfDYL9E5IbgTQuzBQeIQAknj3B0KUkllxq1ShstsNzUC7lJPNLsy7OHHwBBGFenz8XXxgs6Z2H_FyootX-CZjR9vG9LpukeWhdQuvNi7lI8Arun8jhSNHDJdh-F77RI7TX7xJJQctOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-FmRDeupSqW3TJ4qK60zp-Vk-GeBdPN84VPMpr_UIxkX1keWiF4nWPX8291SvjEuW_ZWk598nVHzPyu3_LgVWOEJN3fZqf6rX93cPmUP7KLr5CVvQdOsvHVeQgUUS0kpoPi7AU-bj8UVap4CRCsKZn-2GkClXtBFzd-tS0z1_R3UtIc4fj7RhQegGxQHwhYFxRPWZbDg1hBp9LSxPeX5NMjZomMPLQ3XsfT16nyn4vUvE0gagbkeJrsGbN_yi61O-ezeM44RoQ0-M7LHln1URTxUsjsZPBdR0WClyXegdCYU4F7Gct1m3i5wjtPEElIeDnNw0KyS-JXtIjT4wI_oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzWrXH-fb40RXThl-IU4Zn2hU5LnVHpKRZ2D3YX8PcLeeptfTAsnx1FC_LuFtRt_Tx4ao6W4k_d1K5IgZi7PVWALbcw2u0QCEueaFecScyqtj_yCNRp-FZrKylZqLIVp_KTT8OUbYtHsozkXwbw5-4Dmjhwf74jNixb8BlSvM2M3DLVoPtvH2wvkcGafTFKcYmP14hU5z6QHx4NNPBH_6wCU7epO2svJQ49JuskR6Yd8VzbyVz557jHZydCzltaK0S3yzlEx6WYCvfRlrxts_nasM5gvYgsedOMRO9jratMx1LAzhLYnXSd0Rmkp12_zQKb2ecciukKYdg5RJreuuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shjZlmt3J7b7AZ_AG3WAZ99KiqT1xIUhzyggFGX2HBzZj7XfDlvB84Dr21021C8UvB5nGHpAk6sxIwmixZyb_ymWJmb1CozxX8WVR0pG4w3_mKhnL-imqeFnUu00hITsOfwDsEBuzkSvId865M_8uJ8Z4mLSsxX0z1BtGhL6zA3XDfh8TG83NuoZ5iUvWAnPR0DzdLJaxBRYHQQx34UTwdUiOtBmoiWy8jahRf_-6cfeNbBhu9ZAOh1vON6pYwPGVAiB87R08Uki07R2SBFizCEC31ppKSla9IgsJUvALes0btJdRCOvjoBi37rxy7s2Awi2948atDQoPq2Fpi03Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lK2kUOQnHXQe6CA2x4j4iuQUNxtTBT-t9Pz96-NnAwct6IX6eEkTuXD7XVu9aGlw5KF0IzKbjS6dDfVYTVvxF40XAgfKTSuV1yHkjVm_nVoMSk3GUqCORnpr8FZO7G8-tiOzbwPiC2DPm4e68sX2NTNbSIWZzElcgMHPQ8JMzaM5Ovs_7TeVJ98WJK0BbSyRATJzUnDlwKjvS3zuRObkdAR8NkBz0gMbkm7TeX57pPvUNR0y5qM321VJN1fXwy_PFjbscT6m-HL7wZ4tc07bUbDXAUZ-iKb5dcT9AY6qrAsXyhX8_EKNvgfHWMnValhcX8rax2uN7NLcmMngrPSPAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=UcUiWrBN-uxLKFtPVYYLzR0A-kJZjeNWj8IBOWGIlX4OM3dPjYST3MStBOwSWHJK5AMwUYenWyhAfaezdhqeNOSkc7YQP-0bWSLBOzyskT3r0YYzAIA4utroQvIDJY4p0Cjd3UgBNjafYLUxosUqPHugsShd1omOmw5UhZS9rioZp16wktoJubsjzqtlwYSM8haCsJCADby0jY1MKWpENx5BSY_GqXKkG3ECAHfbjB59OaP5u9LftucQiRYFu2puLJNMIkrRnPe9lb12mgfJnOTzySWqLuOk96azEREINpJKiLtT7J4ndVXH1nzlkeFkOQhc867TRC4MNNzDNfDChI5Ai2Gx4gM936aCJcf8yMpvStJIOfqJhzcgckDxZ17uKe5Q5Z0X91DppEjC6T8mNBjR-DYPaLGgbY2272Co_hbsDlrftcbaHwf514mTJqFUudyusxr-ZyQdB1WHU6K9Lfq9mqtxCadBshM4u9lGfnLoqIwhqBqHR6WZq-Wu6N5jM1cVLxD82lGCIHycf7KEtrKePlc4ThLWzYN6Kqq0FgX02f-FWJPkgcdPN-qBRcyF6a0Dfvg8zHFowZjG2ONPtlY6LmV_OqVf2z-xV7GN4DDvZOSZJM-mM4FC0DQ1qF9xdAO7l6SKHEJfazObiHnz2cPjuylKzx0JxZN_vIYHnV4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=UcUiWrBN-uxLKFtPVYYLzR0A-kJZjeNWj8IBOWGIlX4OM3dPjYST3MStBOwSWHJK5AMwUYenWyhAfaezdhqeNOSkc7YQP-0bWSLBOzyskT3r0YYzAIA4utroQvIDJY4p0Cjd3UgBNjafYLUxosUqPHugsShd1omOmw5UhZS9rioZp16wktoJubsjzqtlwYSM8haCsJCADby0jY1MKWpENx5BSY_GqXKkG3ECAHfbjB59OaP5u9LftucQiRYFu2puLJNMIkrRnPe9lb12mgfJnOTzySWqLuOk96azEREINpJKiLtT7J4ndVXH1nzlkeFkOQhc867TRC4MNNzDNfDChI5Ai2Gx4gM936aCJcf8yMpvStJIOfqJhzcgckDxZ17uKe5Q5Z0X91DppEjC6T8mNBjR-DYPaLGgbY2272Co_hbsDlrftcbaHwf514mTJqFUudyusxr-ZyQdB1WHU6K9Lfq9mqtxCadBshM4u9lGfnLoqIwhqBqHR6WZq-Wu6N5jM1cVLxD82lGCIHycf7KEtrKePlc4ThLWzYN6Kqq0FgX02f-FWJPkgcdPN-qBRcyF6a0Dfvg8zHFowZjG2ONPtlY6LmV_OqVf2z-xV7GN4DDvZOSZJM-mM4FC0DQ1qF9xdAO7l6SKHEJfazObiHnz2cPjuylKzx0JxZN_vIYHnV4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=rR78Pan_0rYFWVJTNc_EHLwOXBAfP-j5govLtIGEVMbfAwQW5mAsfQ0LKieBu6atOQ427myZY6AbpsmlCRQb8ysKuEGf7SP6LOlCxJS_MXyPll5JmnKG0VP_E4kqa7abN8KWkpxi2sptT6k8IGD2yCwBcfIAm3A5fPNAcKuaGR1emFs7Ltp-VzNquTofNNC58wA9F5FFOE2mrormVNVtupTInOUbOHWyxOd_oXENW1d0MtwUnstQae9JYqldgnJP9-V3oEnWuHCkhiIvpNoXjMl5_xlqBPQ8BOEnnEbCT2DOLVy8D5R4TbawRn7-gekqs6SkuihAVVOXUqgE7QxLDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=rR78Pan_0rYFWVJTNc_EHLwOXBAfP-j5govLtIGEVMbfAwQW5mAsfQ0LKieBu6atOQ427myZY6AbpsmlCRQb8ysKuEGf7SP6LOlCxJS_MXyPll5JmnKG0VP_E4kqa7abN8KWkpxi2sptT6k8IGD2yCwBcfIAm3A5fPNAcKuaGR1emFs7Ltp-VzNquTofNNC58wA9F5FFOE2mrormVNVtupTInOUbOHWyxOd_oXENW1d0MtwUnstQae9JYqldgnJP9-V3oEnWuHCkhiIvpNoXjMl5_xlqBPQ8BOEnnEbCT2DOLVy8D5R4TbawRn7-gekqs6SkuihAVVOXUqgE7QxLDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cs9pKvQrFmnryeCpd5anfQV-luY7fs-E35ZfLO-MvKmsv3bBrIw8VweG9T61uQ0pLeC3ywYEhTG31bEkNxaCZDlp7ibK7c-kmafkD9OaBGgYaHiuxJ-pfiJVfaZHemuJCLhVem15S34AliMiwHeR1jCjPZ2a4qqadRdtd-pISXUxOKafxvR-XUoUwjaQicHHMi5zDDGN22zljTQolgOY2di5fjSq_368LSgPPTfNLku04wVMHPJ0nUo4IFn_-VTrkZmnSgXsMdHvqCpUVlq1XQvesXeWCGQ-MVGzzT3zurlpXzauNO6_pb2Ruk6hGUdpr6bxWGzKie5EWW12VTFPSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7UKccy1neGBZK_11DZrkyeRnVQqzbKupI7Ft82kvSczU1SbTO3PTKgKzLs90APiNgCbUulMqb8-Mjt6KOb1-G9KuxnP2hDgBrW1w-zUnG0nPg3MrQhz_AbQwdpy1a6xctIbPrGcHF16Rjc5UrQ9yT_oPuXrExj2g7euW577mGXj2FzqyEzka7j1SdeXByPyjf2uX9TchbI5STZ7X8ZiVcwxhVzjcwBbqJSJgp3QsEXsP3HbeSke1cNAwDyfxy_dFehbuukzTiTLRD-jyNdrpGzOLt3TcEwyvFpiFUVgY_z9sfx9GBp-iH7Sl8qQe1bGv6KXeqprIQj_AjYjEu-Cfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=ABclATftOMyXudOSibtp6EEFSJWLxcYV014eOfqHnwghtg1Fmm6SCkYC4nMhL5YIqQUz22ev7D1oHo-P2khO6rRiuDTLDP6cNzBEoLAsar3jk2pX-Tfq6iIZ5wA9fxW4kWjThJmskAmSRDOfWiTMAaB-Sh78aFiRYY99kpTJVxtkdWmdLHbMBHOa8ysoYl5PA5sFnw6OrTsJlxNywTZS_X4yQJ9cbKvUND6t5WtpJ-NJn55QjlhPTjr471kb8KdtpzQ7yikPNTDMFLdQib9uZjgZ2TogjwjKTVTBpN7G48Uc2poooeJoxq9VI5j2YJJ-srCEzxi26U6Y8ojsjLVQBIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=ABclATftOMyXudOSibtp6EEFSJWLxcYV014eOfqHnwghtg1Fmm6SCkYC4nMhL5YIqQUz22ev7D1oHo-P2khO6rRiuDTLDP6cNzBEoLAsar3jk2pX-Tfq6iIZ5wA9fxW4kWjThJmskAmSRDOfWiTMAaB-Sh78aFiRYY99kpTJVxtkdWmdLHbMBHOa8ysoYl5PA5sFnw6OrTsJlxNywTZS_X4yQJ9cbKvUND6t5WtpJ-NJn55QjlhPTjr471kb8KdtpzQ7yikPNTDMFLdQib9uZjgZ2TogjwjKTVTBpN7G48Uc2poooeJoxq9VI5j2YJJ-srCEzxi26U6Y8ojsjLVQBIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyHI3H73I2dT-ACORZ0NslR5bCmMzrzd3RbTqW_KyA3RagyOe8EhFsuwqdmKj5fdhNV-koPSsb7iXCSP-7IrSh2Ume5xqx1AErUSiZvpFZlu2mi1tcRIlUXsDRe-DhTY6tyO1Y1E-Wffy8GUwA_DuQMRDkXbmAF3dRpKeA6tKVe8evqCF-__Ts65F97FpzKC1Bjodh8bF9NqXfv7c2_EDOfexsCxrqcckxam7q11OhdTjQVrbdQud3kkvKcZwF1VlPDG8dGSS8ODd8CA4W1v1KpfJNVD-oQ3_qCRoZDD10_gtzxZKV7iMK7AvVKamR6KVBQDltEVVw1DDdEaQ_FbEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی ۶-۷ جمله نوشته که خط به خطش دروغه!
نوشته که مصر یک شریک مهم منطقه‌ای برای ماست و نمی‌دونم امنیتش برای ما فوق‌العاده مهمه!
در حالی که مصر و جمهوری اسلامی ۴۷ ساله هیچ رابطه‌ای ندارن و مصر حتی ویزای توریستی هم به شهروندان ایرانی نمیده!
همون موقع که پروازهای جهانی در اوج بود، حتی یک پرواز بین دو کشور هم نبود!
نوشته که اسرائیل علیه اتحاد و همبستگی اسلامی است!!
مصر حتی برای کشته شدن خامنه‌ای، یک خط تسلیت هم نفرستاد! براش این اندازه هم اهمیتی نداشت! کدوم همبستگی؟؟!
🔺
دیروز به دو کشتی حامل گاز مایع در مصر حمله پهپادی شد، دو تن از مقامات ج‌ا به روباز گفتن این فقط یک هشدار بوده از سوی ما.
دمپایی پوشان یمنی هم گفتن کار ما نبوده!
حالا این اومده میگه ما روابط مهمی داریم و همبستگی اسلامی!!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4UrGr5a_z3Llsg-CZEhD5KYoSRp6ZaOihuZCQuVysWfaPZI59aNE7HS81sZ96s0vjRf8lUh-0xSBkpmBkvEq4NxVvilH5Z23T2p8GxV_-yHNQ-WmTJekTCXaoGliaHCtu-OMKto7lGi1rURy6hRYOOIh0OMjvO7M-Ow18VLq5yVppCwbdhv9AJdcmw2KovqWF7KfRQ4JmJNOxP3E-SEQ6fB2BhxrvdsFzUI-_-wzf8N8247sEtFshd5ll_LxzIp6H7OhMhuRdJvTlSBrz_T_ez9YDcVvZeYqo6uE5kVcDZP6t36Hru4qS1dmNBAJrfTt5JglW2WsEmKzCMLZXpXcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBNgpB5B07Rq5WWTO7Ms5yWIztzlXb2kL870gVeeiwiCUori0XWnvhnvgt7tecQ4zofzgS7h_Dw3dlOWSELZAL4c82qVrNqCq7Kpkd1NR5VqFwTwj2vvhN_NlQ0uwCRbBuX4vloeHqk73Qc9nVeuPRgbGea1H4JFSErhhsS-GdFl6ElWRtufuUFYRP_reMgH93LXgQiFVlL3ri-lcBNwUjSUP6j88XBBGax5xQj3hZxPkTbkRec99pA6cZYeK0qkpeYd58CDg4QbSATm9bTY-2BawxqUvTZg-VP0Y-P2zTfArkFzOqVBvck8JDz6MxS14BE6388r_fIJCPp4INaCnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIoIigCVxVZ1549zqKXqXxbwNSA0ufIW9zwoNRrShMW6na6k-vmySTUpu1V8s-0Wpvr4JjJh-b-5pN43EyByxylLQ0nKytKBKlphOiayuXCApfQ5kqsM6G12N3osf3CY2CWcfsBDoC3liYKSpCArdYbfN99JSETmsigPLq9rvqrcwGnl6L0NPlJ-vZGgLuN0YCszTIK_4iKo8irxATlpbRuLmWNjMSuxbcdM80eoaQOhjZVqFj-NkTKPsfqPj6d2guhwcfnX6SBrwPg2flk0Y4KgXjt4p7MItqG1UsBeUKvb7TjDHJL2xS3gN-UWX4z70avMYQ7lPTb90h7H5WgkjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه بار هم درباره حجاب نوشتم،
در حالی که اکثر زنان جهان اسلام
(نمیگم همه‌شون، ولی اکثریتشون)
دوست دارند مثل زن‌های غربی لباس بپوشن و…..
زنان غربی هیچ تمایل و انگیزه ای
به لباس‌های زنان کشورهای اسلامی و چادر و مقنعه
و عبا و نقاب و برقع و پوشیه و ……. ندارند!
نیاز نیست حاصل تمدنی که اسلام
و جامعه‌ای که ساخته رو در ده تا کتاب قطور جستجو کرد! همینکه جمهوری اسلامی با حکم
«۷۰ ضربه شلاق» و «گشت ارشاد» و بگیر و ببند و پلمب، ظاهر حکومت و فرهنگ اسلامی رو حفظ میکنه، نشون میده، این تمدنی که میگن،  یک آدم برفی و یک توهم بیش نیست!  که به سرعت آب میشه و میره!
فعلا پول نفت پشت سرشه و بگیر و ببند!
حاصل ۱۴۰۰ سال عمر و ریختن ثروت و اموال مردم ده‌ها
کشور برای صدها سال به پای این درخت، هیچی نبوده!
نه هنر، نه علوم انسانی، نه صنعت، هیچی!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBA6VOtsroUOefivRJEoeCKkG0vs8Pf3-O2Nm5tSBzgfpM2aXrq8oV3EBt5hUbfj0Kblq66aUKX_eC3RhusJgnC8wr8-bZKc29xy7J9PAlyR8ZoVA3VZbrBcGZsf0Fn_47HTEa42lVJfIgkdBWrzkOSvjAo3VwibQIk80SNS5DQoTUV_w3CLGcEMrlMvk3vO_q-GORWADxH83CO1XyknIOF9UHZxHEZyvpoaY1SDGkOQUYWjmY7Rwoc6NBAmgogRBVAlFi3IFm2d0kTgepkrvlblAliaevVfizgMPeIIde1AtvgMLHXxLStfcWYQpZYtyuG5SazpqjkedyBzZdXe9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5R-hbspFZA5aBGRv9x2KrWKGbt-jHOUfVPW_ojwbCAgoydAvdB9hEOPi7ubyOmxQCc6oi3i2ulj7SHPzgeotkpceJrqvhyNXJeGqIYTS5n85Yfc7Nv42NrA62Rfq7SOAWEDgNEYP7gwV4gQPT5Wfw4uSiqXNtSocRVC0pRFE1V1C3Z9mvbOFCHflhc_KauCSpUi8fXCZHuK2P0YW8-m1jPHZN_EUBechnPohvq1IHeQO8G848T7RMFexBQksoymenVGDgKupCcIXyfcP_oEFY3k9p7kwcrOysy4tFsrgzfIaPRYVQY30zZH0RP2zkWRUFPkSulkTMtdaQnOjTh8Nr_M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5R-hbspFZA5aBGRv9x2KrWKGbt-jHOUfVPW_ojwbCAgoydAvdB9hEOPi7ubyOmxQCc6oi3i2ulj7SHPzgeotkpceJrqvhyNXJeGqIYTS5n85Yfc7Nv42NrA62Rfq7SOAWEDgNEYP7gwV4gQPT5Wfw4uSiqXNtSocRVC0pRFE1V1C3Z9mvbOFCHflhc_KauCSpUi8fXCZHuK2P0YW8-m1jPHZN_EUBechnPohvq1IHeQO8G848T7RMFexBQksoymenVGDgKupCcIXyfcP_oEFY3k9p7kwcrOysy4tFsrgzfIaPRYVQY30zZH0RP2zkWRUFPkSulkTMtdaQnOjTh8Nr_M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRfzwT5yn3Mejzs3d6H1s9f9AqBQPGB7LC7-gj3YkElbW8dgasMRCubP2wQPxRNAfyVAVxR0lBvXvdk5avFySyGZNJo7884ESDnrY7klR76ZueCGq5Bq9VCzZYk2r-YoXpTrnmdi755mwss35GnZivNlnrDl0-5nBzKB5hvI3nYKrWdzkRoldHzGSFs2dL1EBqHHFUMLoLxaHmFuBVJ-gMn0j0UhjRd--RjcTzcak8LeC8D_QOXcUuhEebDYDXAkJpHv_32wPrCpLi49lQHKUVBtUlFegnYu2i2nXW4wJVw1b2rZkBxX3gLa4UoOwgGJwPqAHmwSxYMI_vwmmIK7Hqc_8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRfzwT5yn3Mejzs3d6H1s9f9AqBQPGB7LC7-gj3YkElbW8dgasMRCubP2wQPxRNAfyVAVxR0lBvXvdk5avFySyGZNJo7884ESDnrY7klR76ZueCGq5Bq9VCzZYk2r-YoXpTrnmdi755mwss35GnZivNlnrDl0-5nBzKB5hvI3nYKrWdzkRoldHzGSFs2dL1EBqHHFUMLoLxaHmFuBVJ-gMn0j0UhjRd--RjcTzcak8LeC8D_QOXcUuhEebDYDXAkJpHv_32wPrCpLi49lQHKUVBtUlFegnYu2i2nXW4wJVw1b2rZkBxX3gLa4UoOwgGJwPqAHmwSxYMI_vwmmIK7Hqc_8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=gWJDBSFKJ-XcQuwcuV1mPa4G6uDYNyX3gI4tVv8Y4crQSz2QcqxYqadu189TQB6EmcCK4kk_rbb2B0a6jnp1rC6eNI0RKMVUqScCmYKN1ksnYfRTj-sUeaxAgbGj_vCn6A26NopieLAe_8GAowIsNhj7ATPE9Ipezf-LudUGr6h6CfcvRqA28D-n-hzHcS56iSSm9C1IvK8FJpYeDi7q42xKVT2Pn1zg19yDG9y8DVkqcTX7pJKgLIUpqChJHirxpsmrIFokuEf2HFaVfGn2rr8PFCml958m6OhziXII_9EgafGVKThzwTaQod0pOZRfhkX32moA8Xs8ycFVhv3x0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=gWJDBSFKJ-XcQuwcuV1mPa4G6uDYNyX3gI4tVv8Y4crQSz2QcqxYqadu189TQB6EmcCK4kk_rbb2B0a6jnp1rC6eNI0RKMVUqScCmYKN1ksnYfRTj-sUeaxAgbGj_vCn6A26NopieLAe_8GAowIsNhj7ATPE9Ipezf-LudUGr6h6CfcvRqA28D-n-hzHcS56iSSm9C1IvK8FJpYeDi7q42xKVT2Pn1zg19yDG9y8DVkqcTX7pJKgLIUpqChJHirxpsmrIFokuEf2HFaVfGn2rr8PFCml958m6OhziXII_9EgafGVKThzwTaQod0pOZRfhkX32moA8Xs8ycFVhv3x0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktqNV7k5JMg9BSHfmE4o9F3InJ2EXNkdooNwvU3KNLDCZuDQgzRoVGofTKB0BMxZWxKyb8_RwQX4p2sNHwaRElfEOG2FI_VgWRUDKgTgXloH1QWKRmAb0XMQYfIe2gaEzgn4k0o2wz8Fy-zBvNURQIZLiGTuJ27FShd5abgUW7-8O5U1gudVujvYJDkoEkVBWJh5QYH0UcX-hmjPcfhgrbljwCb1-fpY0MmR65EaMf0ei_6vvoh2Ft_wi4M_LyufiHl0xCZxXAgDelSQ7yUQsaW-iXqIIfAzJilr08OQyfwOBygmkHkRBOl1OBsX0YLOG1VtQ0E5oEIvbZchtH41jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFRt1vUBAqJn0H1UeRjn6-oj6KI9yHdet_ZdTdpqgvMvMyw-1apQXdBi5zohLFvYpDN-Kg-1b1ZnNagy2v6HOVcD7fOz7tJ-pwiSK_9kOOARTQHKkn3drClkkXfLTmAU_kRxA8xXf7pXHvl9TYVj-4On4Dq0Dk6prWSaurhL6GkVPCBs3ILrovBBl9lkNVha00kL0BEJSJnvwZBCgMFO0-46IlAYicCtjDJZSFrrCkkVmkL7K0qvwgtfIe64QQ22kyfMseKN943y_-9Wo5pUvPsEiXa_aLz7BXzDmsgtly3vEurvsIpmJCPUM713Oln299dj8w9dJtuCAOj6fmlwFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=Cjrv3UDRcPUGmWF_oFu6-INgtGCfViuVFD6HF5vQjoZFHUEAVE8rtREhQIiKCIguWEogd384Nrew8LgIq2qVUWpD31W43njjfy8PBXrBBSQUthb_PmPkzfcdmxAu9lVqV9hDpkZkY2e8REpbQwAId69UvFp0xdxK0XUIQE_NR6xorm1LY3z_5uwWQiRY-zWfAQgYokBlQP08qM6K8v3UPQY1bqAysE8mCWNK9CepTci7Nhy74tajzpe2t7rUh7SBjqq0Nmp2l5OfnIE_0ibW25kIVJkzr2GMEhMAlD8tBzwof1CPC_TBoID_m4rAaJKT_kfrOHl_bO9fXA-IZUhO3BaqXrxsoI0LgaUDNTc19ZPZQcxIlQhf1--qQrochk72TzjG51aibJXQWvpMXSAJxzT6Ot8mdtNykOMmhmHYhuhMWpkqd0anemZ45uNVBY6qW8upmM9AJvlcV6Pdh1Dq4Wy8rsE5k2JOE_ii-slNOq2iQEzB6YXtugvQ2IwsxzoUkjwHXzvuCpoy5bpxhX7f0UV7HaGmgXvOJTD01RWtucioZ4EGRcdvdOfDf2v3bF0b5lM_K9n3F0tKQONqZCq3WHwDJp-Pc-0co70fn1HlryODvleEhSs6kGLbaxGyYOzaor2frBtgotWRCzMcpoXF8DVeOideYza2_JgKgbVhHGE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=Cjrv3UDRcPUGmWF_oFu6-INgtGCfViuVFD6HF5vQjoZFHUEAVE8rtREhQIiKCIguWEogd384Nrew8LgIq2qVUWpD31W43njjfy8PBXrBBSQUthb_PmPkzfcdmxAu9lVqV9hDpkZkY2e8REpbQwAId69UvFp0xdxK0XUIQE_NR6xorm1LY3z_5uwWQiRY-zWfAQgYokBlQP08qM6K8v3UPQY1bqAysE8mCWNK9CepTci7Nhy74tajzpe2t7rUh7SBjqq0Nmp2l5OfnIE_0ibW25kIVJkzr2GMEhMAlD8tBzwof1CPC_TBoID_m4rAaJKT_kfrOHl_bO9fXA-IZUhO3BaqXrxsoI0LgaUDNTc19ZPZQcxIlQhf1--qQrochk72TzjG51aibJXQWvpMXSAJxzT6Ot8mdtNykOMmhmHYhuhMWpkqd0anemZ45uNVBY6qW8upmM9AJvlcV6Pdh1Dq4Wy8rsE5k2JOE_ii-slNOq2iQEzB6YXtugvQ2IwsxzoUkjwHXzvuCpoy5bpxhX7f0UV7HaGmgXvOJTD01RWtucioZ4EGRcdvdOfDf2v3bF0b5lM_K9n3F0tKQONqZCq3WHwDJp-Pc-0co70fn1HlryODvleEhSs6kGLbaxGyYOzaor2frBtgotWRCzMcpoXF8DVeOideYza2_JgKgbVhHGE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=rLBFNfRLGoaqFtE9yZJse6z1X-x6-BXByZSp8qtMGawBqqOBVs3U2U8gBazUDzoU7J8vh4j3GyZ6QJgwDE4ck5NhNn_skLBHOSDCGaSrAZmzl0ZXZkyMnERQ1LgslK9iSu1pCCsKZChdXic8j0i9fv2HHZxmuTkzp0Z0w2qjbFvaxKUuyEI94zOwVsuy9PmGOVgLv9Ck3uoU15eEvdK0JtY95pbBhEs8M4_A-446x4ZigDjFO06s5npRxx4pPfbziVq84XiksafL06eRq5gQImE6Fme5jB1x99KEPBc4-W-9YgB5LCAJ9nvZ5WnnkyDJWLHXB4_E7XsW03RwrV1Arw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=rLBFNfRLGoaqFtE9yZJse6z1X-x6-BXByZSp8qtMGawBqqOBVs3U2U8gBazUDzoU7J8vh4j3GyZ6QJgwDE4ck5NhNn_skLBHOSDCGaSrAZmzl0ZXZkyMnERQ1LgslK9iSu1pCCsKZChdXic8j0i9fv2HHZxmuTkzp0Z0w2qjbFvaxKUuyEI94zOwVsuy9PmGOVgLv9Ck3uoU15eEvdK0JtY95pbBhEs8M4_A-446x4ZigDjFO06s5npRxx4pPfbziVq84XiksafL06eRq5gQImE6Fme5jB1x99KEPBc4-W-9YgB5LCAJ9nvZ5WnnkyDJWLHXB4_E7XsW03RwrV1Arw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mln3H5QggVSh5skaGq0ue9GLO1QlC2Ym8M2oDIOObEc6-VsXPHcgtrZzqxKeTHYCSKn5OIzDZz_LqzGB0DnGJczQenQNtfwdivt51JwIUN_5LpgLUF6XrcKNMii-FHi3zZvnkBrXh-HfKii-lVyb-3ROsCf_G8b0Mm9GooiwXzN1KXf16c_Cx34A5Fq8Xvca4epbP3M5URj-np6JJ_uyPKasMEROJvqW-psdsFukg912ehRUMXa2DEfjIMvVCcAO_X_tzqObU4rB6JL1SOKyp-cuqAW3ttRv5UWfnGflk5vO9WM-VA_E5Trp0zTAxPvdCKzZ7349CroAahggg50DFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/glVRZ6aet4QdHvCTMKNs7bMGpJfOoDq1U3Z1riwQ_tVF-UToaWeFreNvhdr5ZyRE-YMC8LONI6kTfklTOBu1fjomgeOHmcGyXW4LzKaXTdv6_4lEaBZ8RFOvXuwpZVmFYtvMPC5FtpK8yF3EZfxAMvmDwFd11iMp6f5MTPUcKFBkPw4BSFfGusVUXqk1x2GbAyc2ZVdJPXnhH3T-BopvghBGfoQp2VCGBPK8l4A0rlzIsoAtSPfs2c562f77pTOw_5XBH5OEbv1ZvXxM76zL4QbNjtRRtDDxXj4HHA_sOyzhoOn65JQjZD3aApwwRS4rZVg0E4MAOjp_Y7olnzWvbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t1Ap5V68GPeFf4Sq9tEvzGdrfo-uKRIEWIZ-belIp01mjxLT0y3yuKbuGlQgJoeRHRSrR23nN5Q8ZMmGU8PNXkiZJ6LCoYnP7-a3qelQhP-q5kq29h8ZTP7l_DmgkYwbgv6WwPyrm0mGfXzFuJQ8m72lK6m6ZKBT3m4BH5vwg-NQbnPCrEVF0nv9cd6tZzCe8IgCeJvm-516klzii8uxz46hEPMiLhZ8gXd2-0Sj5O5WetYVr6rV_BFs1HW30fs3py6uEI2YwF2sqAWevZ_sMClqOC9W8unE1XYBrfw7MO9P6ybw3f_C8R8oH97jh_LxEhLEzvgbfXPKTln4L3cyGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
