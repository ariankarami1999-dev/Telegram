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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 15:17:58</div>
<hr>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeUDumnwf8CmBNYt_QZ99AD5HivQYym0R0jdz_f2k7V_ReYr6-7Q7KO4J5-qNaSXkh0rGqHLJjzMdsplwbeV1k3hdLIVIgucEEXGgVyuvJdtjrZybLLKiiEdza_fQJ4F59OgcqQHFu6ElTGhzLrq_qxVltYfrhe8sPm7ZIFeEOQlpSb90u6-PZpJbH1dt3UgRRfvVC5GNta9TbCemTVHIywVgfxCP6d134uMjx2brgEqQV9ZMf-6fAuChUz0bl0kf11s2dmNl0R6aKOu4UzR86BkQmABZzAZm8v0olC-Li7iQDBcd5-_K40tWTFjMzwM40_oxwNd4UgLRaTEiCH4ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=pfQd1RFoIb_pYjvjjK7tQybT7GR5mhCKDZAqEmvALlsUCatp6RFWaPFrwVlg4RHkgWr83PydnLpeuQkPrMO-BXSHqwcDOWHSDnIWf70aSkajIku7P3vnQ9GIRTC5k8M28LrBCaHB4rqch1LF4gUTwLgBR57WG1mpEzwxw0UrXgswUzg-7gRbRSy1gbDEh-BVHoQGI3yi70LaCfDY5_UJbvmhUoeSB37BH1q8IzTxJwcqNOQPOcRhiL89GL1aBS2ihzW5XA3yjvfQ2yCwzr_Wa7FA4vxwJuGI_GQo6mAJqPlOy2v7gXneXBHQlxSa2-Cm2BY3ZBMnkzEHFG-CKyDmVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=pfQd1RFoIb_pYjvjjK7tQybT7GR5mhCKDZAqEmvALlsUCatp6RFWaPFrwVlg4RHkgWr83PydnLpeuQkPrMO-BXSHqwcDOWHSDnIWf70aSkajIku7P3vnQ9GIRTC5k8M28LrBCaHB4rqch1LF4gUTwLgBR57WG1mpEzwxw0UrXgswUzg-7gRbRSy1gbDEh-BVHoQGI3yi70LaCfDY5_UJbvmhUoeSB37BH1q8IzTxJwcqNOQPOcRhiL89GL1aBS2ihzW5XA3yjvfQ2yCwzr_Wa7FA4vxwJuGI_GQo6mAJqPlOy2v7gXneXBHQlxSa2-Cm2BY3ZBMnkzEHFG-CKyDmVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdtiAywHrPuhShYKrOKfIHuE0igSLK7wLwdmbAypbtze_5bewZgNbi97KQUWb2ZJ9-1I35QmrvamUIDC5nd46kxjqsnlxPUBd8tlyds2D-kozE1_GrjYaLz3LNFUbbDX6Y7gnSN8jbZgiWzoby2ItcINLLCfSgSUZ7MGOxUEqZv3XPqzTw7sbKmK4U1x923y1YiJt6Izkt9G1XGwBBIe1DHS3NgxchrGhBeuzLxDu8g-LCP9j5XQ66pgVfZbUW2H6CHDt4ZZtppxUrakGJlyWRXd4xlwmCBM6CjZLowETLQw5Lv90A_LazAOw0AJ7mk41lBiLKa8gDv2BXux83rFBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pa5IHMpCp69k0FESTr_-Z9eLryJKasZm1fqAylq6ym8HsOvNCqe8uN8WsNxHY4Yxb02YeuYqzbRh1L9B6xyK6n4ssEL8u9fTp96pLA4BUOTbjRhsp9pliNoxFpixRlp2MB9O84hEdMbT50zbC2n6rUvETXKzOnUfxtEuEbbMI4Wgq73y3pDx_dYwGjXBjBWZjasYVHpl_OzBSPmzdQb32Seg-QY_0xqtqVM-Du3V3OWaK6BqDlWNKX8vSei6ON0VW_TFcSgwufwjcCGD1nXwSTthMN5U2vgigVOO4LDk7Kj6axclS_uY_xNVloJO_TEDyYWrnSH_oXXbzfwKyA1n9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBfZKEOIY3cK_10QKsHa0iHIBUBve31VMnxZOJdm1Tw1X2F0WEB8b7qHnUWHsaKYc5QzVjTmZxfgCH2wcybP4BzOsViWBwBpuOnnBxDRp5WBfg_n9jgeYsLtLo-6-RRb4AiTzCB6rpXE1xf6brB5VQhgwuqJ3Qqb5cK1vnsgwWhom27lTkMJd2MhMO2IVyAoNhR-OUT62bn2uIqW3yFquYTLsACuu45M_AFc9SZcu8JcN1nTxIM-MXpLXR-vJCV6kJWL2BvE58gun0mrMjLNWWjoPEf9-IuVZxsT67bQHllTU0SD8Qz7Ni8Ia7ynvu9zpb2IvGKYn6S-wyTlub1AFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYpPwbtJ5I_jNlwLPZojzQbFBv5NZFdp90bUMdbg3kQa4-f92UgJ-pNlfCfkd42YhQ7_z2jcoatvU8x1u_rDZSBG4w8l-n1v4_lFBRSNa0qdkmqMezrSKHHYT-fhACBFq6GBlvxAFf3ao0WOi-c02G02bi_gEdDcZS3kD-WbeGd3rE-NoscXct-y8Yf_yuzTiOA2gWytcQBRDgoSJxbjT_XloZaAtKK8bOjE7U7dXHO7w3bq5wJ-O510A2JNHNJPuMLMAxDyeIOI0CVwvztuwS8UmNhzA9fQYJyzJpV2n3Obxrcp5D0WMBT9jxrkOZfQzUTVzUGqSkypyEWXfSfM4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tk8Pye1R0txkFomPVhn_Zc8HW2Z4PqV1hd4Bm6nSo_IGCpNT7_feUGgPxKThbIXfuz0i7UHztgviuetkPttvP3fdL7BR79hBkFwT2xT_AH_oKxye70sxe6WVAnOFIrUTT2IpVIYD9h6MH47CwfTS6hLOWYCzt-QWl_kAEy7d3kDPnrc0tdjCZy-pm8dM5wvqx1DmkqXXXSIRFWuOGTmtk_URRtOT4s6Whrgz5YzBTYlVkd1e2_rm8fw_eAYvpm0MYptW9ac-cTbrrZZLRPY_4gPp3BSqOWdzHehy1MuyPHtiSW-hCXyzdaRNo2lfkbeFdRGvsX85qTXrI7zg7sJknA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MoJ_XkJXkJJPsqTMJRDle-ab8y-fyUMVK6hvNB0mTxtDiSLvtXlJvrAuj6a1byp0Jt_g2cpAWqEopSvb_nB7Grfl8XV4gBmijyDE_AOm3NQMveOTf059OKZ-eEgh6vlD7vZxbijzTR1IvodX-LtlUfIea3GHX7eHuo2X5MhJMAV_i8OxP7It4fFHAjyYhfExbjWrZPxZYn3qI1d5dAN5xFmMAjpZPMDnAhNuxTE1ZMItuZQTGGJQtAm1QlE78CyUG0XuMI9Z1o0jPP8_FH3tABBbwpotyIzpCSP9-jdGuT2kofqH42LyDbS6UkL21Ts2FMy82DCrkaCig4xokj7exw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E4kxz5a7tRWkfyErIOnmPIZwFlU5zOGqzkM6EtTOL6Q9tXaubmq4f25S5EEAhRpXpcqj7s-aw1KcBIG_n3hA73DydcmJ2liEQfzRhTOQhnufQ3nLA2DsvJwFwB05pejvgoJ_7Cw16x7PXQQ4mjkIu63sdgKWNYOsx-6Cy4T6tTuIvqtB1UQ_k0cty4nKbL0-heQpwP21IzttjnMEejaUhSePeMGXVaZDpPblA7DBaAnmg09FXOOQDVXPmWbjlZyzLsKvuyJW76FCo-T5BP1ylac08dant0Yh8pZBK_YeX_hi0Lt-QENkKyM3682w_C3z5JzXjFRcy_0f0loUhd3P0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hKjfx56_HPIS3rsMA92vylkB4EBfdGRq_UxenGhMJS0q4E1GT5IhbSLtPZJkk6ztA9R2_czOSaWuxbCHIY_8YSwu1Dh9LcMP-9Rjy--h7yA_pqt5m-g8oOmNm9zgkpwNDZ6wOPlF33nAOnq47w2D6k32dc0ZaujwRNxofONnM7mIbEkF76MPf3O9KVOzQHXvpFeAYuo4e4AFntwegCzwqofh6ajYfq3ik-uK86MM4OV0g72q00QtQ0utzYEfQ8cQNxgah8cJoxZMiuqHshYBtMoVx-XKm1GlIZOTrMzO-jcI7Iy-UYo8_lpCjSvLb9Gh0VBUPET9jpGwCKzvIyuxCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیرین مدرسه ساز در ایران،  ۶۲٪ از مسئولیت ساخت و ساز مدرسه  رو به عهده گرفتند. حدود هزار مدرسه.  فرض بگیریم همه اینها مدارس ۶ کلاسه هستند (برخی ها فقط ۲ کلاسه هستند)  اگه هر مدرسه ۶ کلاسه حدود ۱۲ میلیارد تومن هزینه داشته باشه، هزار تا از این مدرسه‌ها میشه…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6524" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flKUk0yET-K08bKuQSWw8stum3ChMiH7VSs-MPy1pyrZYUuKhTOOe2a6R5VFRPSbTmUGxSYPyGbPtZnptKlM2mrEJEamlLkoiVZci5GCCBnLUhbtfpiLNXKvMKk45KH-LUypqyFZzlEY2UAJCZ-zPA2XZJvu2qX6JJTY14fwhFVQUZT50JcZnI9HBYTj2_vaMNZnTicFZKXrTz0m4vyS1FmQq6C_vrrvjzRlTkz6DR2vHri6DtIe41xic9aORMcs7NcpkUdM2D6B6VH5FjQLExVaR774QWpBoZErME6cMufMx8A7dRTFGotC5NYysIBBPO5zF8Mv2EvRYrvRghy72A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا این متن با دقت بخونید و قضاوت کنید:    پدر یک خانواده،  نیمی از درآمدش رو صرف مواد مخدر میکنه،  موضوعی که باعث فشار  و فقر در داخل خونه شده.  مادر خانواده ، چون بعد از اجاره و….  پولی براش نمی‌مونه، معمولا از بقیه کمک میگیره که پول پیاز و سیب زمینی و…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6523" target="_blank">📅 14:26 · 16 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6522" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6521" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6520">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbfFSJiTnLRGR2RUsLQXnScXf9XKEUjNwYYdui1jNx1qsIzy0ilDtTtoCKBi2R2YkopRoITmAfuacKLcCxGAaEsER23owEfeFCMhsTlb8TmlWaX6lZgYEFKj80Dph0ztAJmXfuadTmsY2YcFALx61brVs9E-Vjt4yLe2rUpHK2sXVVOmJ923Cv7hUi5yUqzGvNSR4A04v5MVBaVAeGiVzhxfyFnhKiKTIJH1Rlqo97E4ZAFEjlQkbelW84BFDAfZ12ARTO_Xg8wt4d3B4-3gP69w0XW5pKZKWrIAksdhE0hdI3uwM76vJR_HAhxhHM0eEpwrCSvCWr9KRzRfGoD3vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی به عنوان رئیس شورای عالی امنیت منصوب شد.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6520" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6519" target="_blank">📅 22:30 · 15 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKrwgfarlnVHccmSJ0novB-DXNTP6chCxTWCb4-HwYuQOCyTDymXeR-zkFJYxrJpeMSIweYqp1YKkzknBgYa8WmQYIAShyTGetvXhLbEKozYsgwsY4toLgPzkuOeLtJAyETahys0GNnfELTBgRiVFTuH_XW9ZN10kiShHOhOjen77vVVLm5E3TlYy4dParh761-VwoAdgPLIh09Wx2bBfsNBh37J0P3Mw_xnR2bcfQAjpjEBvfcx-YJTDjcbOXePQgf-C69jIbRk1zgHtb5nDHOaxAGSVdq5sziX3vktXUJj2CxhxQHzdGHqD37c4Xy5iEBBoJ7GFKKC-gwI4Y7Y7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tw1kxXKcoUAGLYAXJcAWZ95m0WGPqGWLFim3JpyuriJawvzbjQW5lp_1uIKswJaNpTaoHPY4Aqrx7cxGG1ZTeKrd6WNS1OwTpNClltr5xCimQn_NbIo64WI8lMTzI1R2LJyAcbnKM1uI9e0CxVbS4k-wmYwK5O-oAoD0D9FBgBjsdCWGidDO3VwzbIRN7yzxMw6sB8HVh2is6kWv1fzb-kwIG3G2qHuCs_87E0nRyk7iDLuMp9SfsK9AmrqegFsXvWvqo3XOkcostRef9Y8Py8lQQfjXgtlOKX1synOV4QwDF1xKc9bUVCLwet8kSVos1nu9OlxunbFlnJaZ4Yv_dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BYfqgfZNhjdcl1rtkQ5Gz3EF1ISIlZegw4YCs7Rm48351IdY5t01VxNEl4My052-VcrITTM1TZ4mPkwYCy4uU1HsjjRm2ZB1JRlGqFjxgRHP_2dnizTs9pggfjMzjP0BcXfb5qMa25Gsk93bj3nmOzb49P5D4t6G8AHsEEr8PornTMgakZGfqUXWmjUzxEOSqBDPb_7G1NIVfYJvWxl2Xx-CzJgMpdAX7wVfwLoUHB69pnK4W6x6KIov3elVApFJLNN1fZPyJZJsmDnRuNsUbJkk3dYTM7NqA0VPd8qkCEphUpxP3fBn6eGdSQHrcfb4hpR2o20Zx2NBcGJfeAKaaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.  اینها دنبال «اتفاق مبارک» افزایش قیمت  نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.  اساسا با همین منظور شروع به حمله  به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6513" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=SkNUU8wOLtXQxIw9ZymcVdRoK_s5NrX0AS5VLpPlBZJ07iNpJkTAC-0fpzmG5NwdYjDDslxoKcIXTLBd7mNyfVJ8VayiwvX6MlUXFry_gf99resdXnDl9cewu33adHt_o1kZcafAMb6xxjZ91A8QWd9ZqL0sWDkVMNo6luWNPC0l14MWzGRJZ1evO5qe6-irug1j7zrczrSpDhp0IHewbtvG85ZDrVrd2ENGQb4z2abkY8lll7VryKe9ryvGRZf26MaXn9OE9jL-xfagcGFVvzKdZO7HhsOVl9SLp2D9aPykS3UHVMSkUonGZpT5sP9KJfYEajgqH9EA1dIejAB0_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=SkNUU8wOLtXQxIw9ZymcVdRoK_s5NrX0AS5VLpPlBZJ07iNpJkTAC-0fpzmG5NwdYjDDslxoKcIXTLBd7mNyfVJ8VayiwvX6MlUXFry_gf99resdXnDl9cewu33adHt_o1kZcafAMb6xxjZ91A8QWd9ZqL0sWDkVMNo6luWNPC0l14MWzGRJZ1evO5qe6-irug1j7zrczrSpDhp0IHewbtvG85ZDrVrd2ENGQb4z2abkY8lll7VryKe9ryvGRZf26MaXn9OE9jL-xfagcGFVvzKdZO7HhsOVl9SLp2D9aPykS3UHVMSkUonGZpT5sP9KJfYEajgqH9EA1dIejAB0_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6511" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=lRussC_4VjcqGd5vPqI_yE8Zea4Lz_WiGQIs6DEQM3M-WH1P653gTYJbkRiMd4vyvYNJRc64Z-e4iRPYJxmEuXXf_zxLd6IZ06FQgVI423cA0Ml3XhlxPOwlwJHNA6nklcV0lKV7MYhOtYONtD3JhGwlMIq6hyihwTysgypI6QX58WerzMQNYoNCuRnyiuluh93IVJTwSjU-45I5F87Seth3_Ao_fL8qtcf4FdFAPeNCflciuRhJv0jhS-ubN9dI8zbZzESfbjUhWuBpzrW3F5N05JkSnL9FIK5navAyRMw-fJQJ3-e_eWSix4iJo1g3Jui8tM7UJMRnPaFe1CbQPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=lRussC_4VjcqGd5vPqI_yE8Zea4Lz_WiGQIs6DEQM3M-WH1P653gTYJbkRiMd4vyvYNJRc64Z-e4iRPYJxmEuXXf_zxLd6IZ06FQgVI423cA0Ml3XhlxPOwlwJHNA6nklcV0lKV7MYhOtYONtD3JhGwlMIq6hyihwTysgypI6QX58WerzMQNYoNCuRnyiuluh93IVJTwSjU-45I5F87Seth3_Ao_fL8qtcf4FdFAPeNCflciuRhJv0jhS-ubN9dI8zbZzESfbjUhWuBpzrW3F5N05JkSnL9FIK5navAyRMw-fJQJ3-e_eWSix4iJo1g3Jui8tM7UJMRnPaFe1CbQPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.
خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.
او همچنین با اشاره به اعتراض‌ها و تجمع‌های خیابانی گفت دولت مسعود پزشکیان به پایان دوره خود نخواهد رسید.
@iranintltv</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6510" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7mV6azgv6kGlRWnL6QKQalHj68JiMgO1gNcGwRU1ZQGe1EVzY8IFxseMK4UkHeiTdxWTuAPAkeoJPq7jSTr0V5txwsByphqoz4e0cvw688X6n343_2c_q2fgWr9_EnRJh0yX_YljKF9IYh8kPYVWH2DhbppFxmoGXOM6Nx_TrhOR1gZq_GA9ulqAFU5M3wV2PhEbq9sS-cPYMYO_9VgBAX9M47XToo6Vt0oS4Cfgxd9D1a6ig3xD0MOjbRgHRsz-hVcjn2WI4bdVMmS11LUGqIV6gALl0gdyl7syK738g65j953aYdqiOy_fP_Rnp0vLN7lmu78CzUpNLY6eUlvoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sznu-DFyznZE9NK7iY_G3WHMRwBWJkIi-GlpRnd4Il1d27H1Vx4WE6UM0IyfWxBaNsuVrFrN-rzzi7Z9TIfE8xa8uI4s6GCT0WE1SYBxrclEsyiC4y5XgDm1nYP4D5kDrVqHNaHdacQHFylgbXj3KU9aiiVB3tekD1HiyrULZau_hPEE9Q8XG0eOSVoPiNBlitKfg7oktGefd5gSOGv1BpyAmqF1Aiv2l3jj5Y41pt0qopHB63V6IXZyxBDoDoPOGxshaSvlIydo9fCwxbH9E-wqZQrHyInnu78AUP7Te5vmXggdnYxrjmVcmbLdBtzrwJvLarMN2qK5RS79XRkP3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=AwpfyQ_k124NWWY962RN1l-GqfxjlSsiKGyZjOI8zKI9uXMp0_np1dqalQXWWG8-Xllhd3UghFGYZ0ps4PvHayKemnxCnYLHdPG7yQyLnxLbPCoAQx1N-RW3xhdeycSZHnQUqsOkoLr2OE7dvIhzWIyRkUhtohiipyPqGs1yn7e8ghg8YoM1I-gd5SQ5JGDczvMvsq7hDCtbUoKdUpAIxFNgry4Lgg8t0UjtwE5eiWuPkSlbboWGaEFW16jA-WZsZHagvSE_EFxrgWa1Ku603aU8_XukTaqJATrpWexOtgclv7AJA3DLDWAJAfyBLpRiWSKvGiwDKbLvWz37rR_FQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=AwpfyQ_k124NWWY962RN1l-GqfxjlSsiKGyZjOI8zKI9uXMp0_np1dqalQXWWG8-Xllhd3UghFGYZ0ps4PvHayKemnxCnYLHdPG7yQyLnxLbPCoAQx1N-RW3xhdeycSZHnQUqsOkoLr2OE7dvIhzWIyRkUhtohiipyPqGs1yn7e8ghg8YoM1I-gd5SQ5JGDczvMvsq7hDCtbUoKdUpAIxFNgry4Lgg8t0UjtwE5eiWuPkSlbboWGaEFW16jA-WZsZHagvSE_EFxrgWa1Ku603aU8_XukTaqJATrpWexOtgclv7AJA3DLDWAJAfyBLpRiWSKvGiwDKbLvWz37rR_FQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!
که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده
و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6507" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bot-NlGtbg-QQZOOXKcoXXdZgZ2xSojfeAC4yffkc2WwrQ2v2pHYjPjb4VQ2bVpDicaO8qTNSdYswiZRfnXZzEjLmqwR1x8DLz5-r_Ni6fZFIluA-y3HdMLRFJrt9MVqaQJrPjtS1twci9I6nhQ8u2ZXUFU3cxMRq8KG-HbiCi6Dupwxz-AiXxqBtthB3CaEZLplZwjFlnLAzUk3YoKugDCZzaodq8gVON1aqBW_I3xdvTnNQHEH9OEMK4-1yyRNC8GGx9MbevErYw9kV9DPArTPlrwBjNpGRaGo2bvl0Iz-1ZDn2qESQRp_daDE_tBBEH1CYpdG3jWnqkrL8Sxw8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHcthD65L4YgwadOtAYix56JYY6IOC93shXA5Y6krQDIS3kANhRsHVvRXJij65uMSIEy2E-3LEspbSvYVwI1FBIwDM6SseKtXMnX6QXpU_xts84FifQSCclC5pLXOTQ0ko0Lh3B8UeF_loyJGauG5LvhZla7cN2oitPGwCscJ0kt3xwz6UH95_KBQIQ823g1zwMILDiPFMUXtmwylNeJtQUQ1tvwALhdqSaXp_zXM0924ZMsO4vimepKUVX4oIal0X2LkdK3aLnhXaiC1QpY6yQ2W35Xo4O9pOIMzfWa86pJx3CfClhKH3qPp_oLDcL3XYLqRAb08IhoaZOhWRdP6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29785e012.mp4?token=L80KaQxKfRu6Y1XqAzFqasD3OMKUwgZTGq3E60RixVI0XARc1DdWpvzQyIroWtG0ORdpG9lD3fuJyO-WLl8pTJow8Fl1-x3JdgOdugf7GQJ-ZU6UEqoCUczqp3OzlaeXSvmcMKK5Dfs7PmWPth9Y5jbV6HOLfgJ0JIPOsWDwZ0BeM4it6P2DQ_3jr07Fg2AKanadFPLBUB-QDWvVpc6ij8FXaseyLgbijShJYz40fvS5yRRrjpG1K_o3T5o1rG5v7eJN7318U4pJ94-eQx4P-fBdiY6FnbPt8iEHTCNmuDOol1R3EfB8H-5C7WsnDFK22b7vYDh-cRftiDyyWUeaTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29785e012.mp4?token=L80KaQxKfRu6Y1XqAzFqasD3OMKUwgZTGq3E60RixVI0XARc1DdWpvzQyIroWtG0ORdpG9lD3fuJyO-WLl8pTJow8Fl1-x3JdgOdugf7GQJ-ZU6UEqoCUczqp3OzlaeXSvmcMKK5Dfs7PmWPth9Y5jbV6HOLfgJ0JIPOsWDwZ0BeM4it6P2DQ_3jr07Fg2AKanadFPLBUB-QDWvVpc6ij8FXaseyLgbijShJYz40fvS5yRRrjpG1K_o3T5o1rG5v7eJN7318U4pJ94-eQx4P-fBdiY6FnbPt8iEHTCNmuDOol1R3EfB8H-5C7WsnDFK22b7vYDh-cRftiDyyWUeaTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6500">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=c0Pizj8nJ2YuTg1JD667Od1ATki204uDfLl3UO9qMD7w3jQwVEFEF-sUEYa-N-26uymYd0FiWmOkls_B9Ax9kHlO9B67zKfPIQ6PhiIsP5LUkrVZqcKBcDwUdQl6lZ38r6lm1N6lY0ZNYmPnuG9T1SllBSquPQ7c-HSoQOj08Wk0YLJiqsfbQ2WC__w0DMvnwMp84ohn8g1Ayb60O3m6ayI6AxPiWdDnfreShKsqDty3hGCloKjEatLnavSVyr3Vt7l1uOYBg8c4ylUfVGApfM9-JpI-9etXONcXuESdtZ2PvnTqLpMb3onVnjdzHwm0qBb4CY9zN0HSJpXEE62sdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=c0Pizj8nJ2YuTg1JD667Od1ATki204uDfLl3UO9qMD7w3jQwVEFEF-sUEYa-N-26uymYd0FiWmOkls_B9Ax9kHlO9B67zKfPIQ6PhiIsP5LUkrVZqcKBcDwUdQl6lZ38r6lm1N6lY0ZNYmPnuG9T1SllBSquPQ7c-HSoQOj08Wk0YLJiqsfbQ2WC__w0DMvnwMp84ohn8g1Ayb60O3m6ayI6AxPiWdDnfreShKsqDty3hGCloKjEatLnavSVyr3Vt7l1uOYBg8c4ylUfVGApfM9-JpI-9etXONcXuESdtZ2PvnTqLpMb3onVnjdzHwm0qBb4CY9zN0HSJpXEE62sdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xt_ATbu3kcncYWcUdZnggXW_hbuVjq4GXABY0wyDHCg2Zg28qEC3pBgsHz-Fex1wKjmCLccg3X-0HeXfxykOQbyLzBVKbyIga2kOVR1nv5zfC6FUtcmMrJdbxiGDtyAqaZGgxVnKI5oUs03iux9MGP_JXwCf-5suK1yhN1Fa4fX13eZBNtjuKCkiFox04JsjvxGzlXPKP8qJsHbnUdGNmklAZeb3g5fXvhWcxtN_LTTLUyq3Nmzye81QNV8qxryMrZskpAnYImqg7jaHOjm1J8AjWUXW4_4MbC8yvEdeb8eEe2OhUQzS2jaWSfc6Ekq2mQAZd55vD9IK6LGdvroKvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrBx__Z4qmYiKXl-7kD1mRX1jaHL7o72pmJYBKDNV1LnPgpCY4S-_0GRxXAb69ptJLxqmjRgVs1p_q1NBmL55Z4ADJWRZuMvTPZYG0dqGEvVkkrGQGaezawP-23DQM5F24L_jHwihgnHVtMJBc3p5NbdMVzCgi-x4TIAYijv0x9ZKywohIb50aghIQnhEYq4ajzFJ4yY5IkUTCEz96egBy_OOGstmZw7uvkkNggeKphQVmj3KkrqS4-cExcUbY0JPKgOyPOwc83OvPpERltGvdKSVYY9abjqfUvKdJU8EPkCfnRY8F6wMub0_oahO8-rAMn24ZOt021nLcAiWGy5Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8xXpbq1RYIzEXfnwvzXof6xwSGYRcPs4HG4hndDK4tdrVS6C4HFc3iMTDZEeHKOrhD1vHshgBOGKnQI04IyP5uxxfnuf3G65UPE6C2GC68lAY96rFmNjRq2oQTwG3zbvaP3z1MoSBylaIt1ieUC6pPg1TXEs3_lSfHJVa8oACrk5yTCPkCRrHn1J9ommCBHZOxYgb1ZRDleO7yNFaRN1lvjaR_7mIesTwnMXKZ_JD7Il06XK2a6b6KFuX8dmgJ6L0WQ4zNHZM2km3XYMNKR78jskejE4QVaXdCxsSMg6tFNYxxEvyaOgr4VA6_z5WUs02jrXe4TopzQ1ibxa04qew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.
عراق : از طریق خط لوله انتقال نفت به ترکیه
کویت : خط لوله به عراق و ترکیه و همچنین به عربستان
بحرین : از طریق خاک عربستان و‌دریای سرخ
عربستان : صادرات از طریق سواحلش در دریای سرخ
(همین الان هم ۷۰٪ صادرات عربستان از دریای سرخه)
امارات : دور زدن تنگه و صادرات از  خلیج عمان)</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=sPgbdwHP_NuEDhqgOuFSU6OLcnuRPRMEH5q8MVlxJOCTHSAlJwgK0700ya--0L7uF2fC3OTopVvGEuvIzIFDtfnZq4x-OT7k6Qidh1n8ZwloHgje91r2KjxG0cGpTRrybVTVJnVpAE8RqfYUH9MA9RJ6grUqF_V0YGl04Vh8j-bORCK4Ek2jHlgmyfis457B4bPOj2oT_hFsUdL7rCGzo186VF1w3Q8eK8GGurqA_WctS-ZbUypGc2s6je728iIS7tigKipeUZqfRA0X1HuECvH1qIkofd8_XKofuqMqRfHnB3iP0XeXZIxje8sEwrs0t1iqS3mJL1-wJqp4bb1Vhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=sPgbdwHP_NuEDhqgOuFSU6OLcnuRPRMEH5q8MVlxJOCTHSAlJwgK0700ya--0L7uF2fC3OTopVvGEuvIzIFDtfnZq4x-OT7k6Qidh1n8ZwloHgje91r2KjxG0cGpTRrybVTVJnVpAE8RqfYUH9MA9RJ6grUqF_V0YGl04Vh8j-bORCK4Ek2jHlgmyfis457B4bPOj2oT_hFsUdL7rCGzo186VF1w3Q8eK8GGurqA_WctS-ZbUypGc2s6je728iIS7tigKipeUZqfRA0X1HuECvH1qIkofd8_XKofuqMqRfHnB3iP0XeXZIxje8sEwrs0t1iqS3mJL1-wJqp4bb1Vhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=r2Stol9tonDwJjpLHeD4SHidD54kHfWkV70tPqvoz2k84om9FQ3otRw9uqcsBTudM_0zUFdO8nWRrpnbIUOUUD-00Srxy4-nwN2bhlzZAfZA1mzDqd3e_tUm0F0rauUlUtaPpdwfzoZR52JyoHfR1mE0iNN-IRhP7fvZa_IgvZ6F8jEhMbDEs6xaEb8WQ9RiSVNlK8NOt1q62kKFva8RSbgIJQwz5IxbtMJtyz1BrgrGOeNGWkqc6Gb4Y9J2ceSSRiiFx5UdTK2jFJXPpb0mHX2HtmicjCZZg8UdJKKXGs8LSgXswOnTOHrjm0laW3BhjkEkEMFMxrm42oJ_YRYgdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=r2Stol9tonDwJjpLHeD4SHidD54kHfWkV70tPqvoz2k84om9FQ3otRw9uqcsBTudM_0zUFdO8nWRrpnbIUOUUD-00Srxy4-nwN2bhlzZAfZA1mzDqd3e_tUm0F0rauUlUtaPpdwfzoZR52JyoHfR1mE0iNN-IRhP7fvZa_IgvZ6F8jEhMbDEs6xaEb8WQ9RiSVNlK8NOt1q62kKFva8RSbgIJQwz5IxbtMJtyz1BrgrGOeNGWkqc6Gb4Y9J2ceSSRiiFx5UdTK2jFJXPpb0mHX2HtmicjCZZg8UdJKKXGs8LSgXswOnTOHrjm0laW3BhjkEkEMFMxrm42oJ_YRYgdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=lKlvkSSVM-1C6Svna6Okxt8vNNBB1nuDM6D4pITvMAq1OQD6GPx9lgs-rXRz46Sc67zMqAUJULyDLuEVQt73eSHxnI1lK3snc3vlxVduJ6hnNqoP8IOSThrdca_RNxG_FZNWFyxJsrpLMItmIaIrtSUpyao8UFTVSXgCjNFhtLgYKZ1CeUXLWfXQ6b-FQjJbkPgefrYpI8t6zlPj6XOEHDbg0uqJHTp-jWrXR3OskTJwKdKEzHmqKIupG4uiMNm4b0xwdqW7ywHEsEacLN6rogYoJi2DA42zCuF52dI_y3HKcGfAMg9y6HGIT8dW60x-kZ1qcD6wEt32asnLmDVorQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=lKlvkSSVM-1C6Svna6Okxt8vNNBB1nuDM6D4pITvMAq1OQD6GPx9lgs-rXRz46Sc67zMqAUJULyDLuEVQt73eSHxnI1lK3snc3vlxVduJ6hnNqoP8IOSThrdca_RNxG_FZNWFyxJsrpLMItmIaIrtSUpyao8UFTVSXgCjNFhtLgYKZ1CeUXLWfXQ6b-FQjJbkPgefrYpI8t6zlPj6XOEHDbg0uqJHTp-jWrXR3OskTJwKdKEzHmqKIupG4uiMNm4b0xwdqW7ywHEsEacLN6rogYoJi2DA42zCuF52dI_y3HKcGfAMg9y6HGIT8dW60x-kZ1qcD6wEt32asnLmDVorQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=I3FH13eOeNkh9VQhqKlM8dCETF5stwsVZT52ElSNnmGo9NFCfHCbV5dXfde0qTL8-zYj-o8NQJa19nulld3DLICw4Nlo_1tX8OP744-auHzad7CqDi5PK6f9ZdqolhkWuiG89ryYYKzoSwEzb7m3msk0TzXR7IVOBSt5Bnorc28tPlqQ-8vECedXRwhfqO8d9NYbhi9kGvSOMAEdGJ7ETvh24g-woXSAohrntANDnw-KKL5O0rNuQP9KeItkKKNewjJR02PKc9SOUfFg0THA-QPbxnRq0zGUDP1nYO-5EWBkZpGMOIyRye9oygY1RhsswcxDkqx3lr8XzD4DZ9He1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=I3FH13eOeNkh9VQhqKlM8dCETF5stwsVZT52ElSNnmGo9NFCfHCbV5dXfde0qTL8-zYj-o8NQJa19nulld3DLICw4Nlo_1tX8OP744-auHzad7CqDi5PK6f9ZdqolhkWuiG89ryYYKzoSwEzb7m3msk0TzXR7IVOBSt5Bnorc28tPlqQ-8vECedXRwhfqO8d9NYbhi9kGvSOMAEdGJ7ETvh24g-woXSAohrntANDnw-KKL5O0rNuQP9KeItkKKNewjJR02PKc9SOUfFg0THA-QPbxnRq0zGUDP1nYO-5EWBkZpGMOIyRye9oygY1RhsswcxDkqx3lr8XzD4DZ9He1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRPhPv1Btk8PE41g4K67otouueziJw2TcaejHpuVHx6t1fNqJvNh_lbhp5LeI639D06ZUixFqJS5ir408qJeVKS4iDsj5OJrboF0xGchRhPbfW9bGkxzMWVdnKtAfHk1cPb7rn6d_YWk9_XalqMnHfdjB_V_ja5g1PcC0E3xwuxdGr87453dqW-aA_RecqJtTVtCevFc7ev6r_BvSzeEJDPVePDOnD-BIPOWNImtQiiN4xt1vGbOOhviKIzRwmEKPCm7w9IKp_-nBrKvq0CTHWMpLaWWyTtiM4d9GihVMNaN0p1WPCEbI3qI5mSmtvIKt65UiVZLB_cD42AgVhDm2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_qfOJbr_oYSPQM7JdFngHAb6N9JnVSLgHo_K8fMFncoCFxFOhejfFrttODVnyilBsYXGgRjiRHTqSVD5OS8q9XO2okIRxucRBycLkeMa0kTUc6E-CUnVbs_2GeUabLIir1soQJeaBCvYBbbVegW8qbsGeNL0zp2kXiFsDNSAeyAtQYxFh-FxiENqBgousBfI0Oi2mDY2-_T0YSYvWWt5PJPl7irQvEydhnUPJqRP0ssHgy6nW31gxqLIk66_ylRMLWPsrx-ULWl51stR6OabtTt7_P_3A06DXEvoLWQJZvnIWw0G1eqvxjsYczN7VG0tDzZKsqYsApLTCduZQ_4EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gjIoZxAurZx3LiNRYrjLl03u8qqVrRl9-S0sGAI5jRssZxTzbwfN6TxZ4p85sZaC388S-fuGpXOxmX1o7LEHD3SQn6SwN14eonuksq1bicy713RCPiLgPaHe7yEm__NhcRSUtw3Pzt71Kgfyy54MoxrRLNXllwKB33x-Rdb4sfgsT6p2ifLpv1q1vEWtu-0cmtgdDPOt4TptIlZip3kk3IUWv_ZX02K8zi7gw1vyQv0Q-V4bZiQfhpp4U2TmvSwEiM9U7GoHP0WdMPMaL3SgbOb8KeHeQX47bmoQEqFUySMkt0PzoTZw9y-bzvucA4U0InzSYgNlfuma5SC221f3uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G65yCW4BPrba_4-2spfje9kMiaW4pGYDHMGVMj2yHkuv72LLKW7CxikxFT0nfhB7WTcXLDq_AM6Pk5t6y8Xf_EyePnqWOjlZv8lgBqq32iYEmu1iibIfV6F2waAaGQiXwKIrPyLczz69Fps0pSYx2Hr0ZTnFL0U1JmundWjjq_RonHmtF9q7CstdyOZBaoDmhEz0qODjEGFSbrFFeqIcI1jXLP74U5qWf-NhfgQWlESRx2ZiNHaQ_DHUsB9kU7R1QJpxqpxtOFGb2QSoqeWoVJX_YHU6flNa_tRWQiAEEhEfHoMV_d5fIpSXg4J61bvw9G1HEV5N-bpK2wk4tYQcVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7OWtx8w0J4gSdZdH5EirmMJ92EqNL35S1lriQs6DfSBQcvcBALk1it68hT7eqzO3NA8mo6HBWw9FS6I0WY-fez9eEmLp0vHS8f6Ddsf6-67fqfcFy0UQenGk9KgFyNlbXV0lReHw5oImLKk_psoXtg77KJqe5n9GcjgHBIWiXgTvrySvdrxnCQr9LVsYpSn9mju4cwyEK_3CaGZpIrWljC1Ba7yBZ7EoSm7FMD03zGQW0oVgncaKUX7T3zGhcbP62coQaq3LlfzX-Btu9j9BFhK85PhzX1GGVSTq8eC7VMIFEOcmzbcuPxOF66HVfg_eerkxVGMGsJZSSHAHCeK6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAk4KEZILqTsphgyNnL7ju4rqkXYQjjBDQHt5F-EaBBDbWJUatjn13hoGul6PY_d745ulv9Yf9qAy47HAxQUnhwbvJYMKF3eJIgiTfOudsfNmvsSP2zWUO8Uixa-Zg_24KVoP9hIK4Tku5atvBNb9KNVBwRSY8ggQLWa6ZbZHA6hiqnVqeU3QBRZfAZEmYs5zfo59PG-KR2LwXL-vpZWZTdIfueoRrTAPkD4vsYTkq6rIRCDfHuNtNGSIc4yIkuzVK2K7cVUDVRCKjfDtB_M0pD9zlIUBc-8WB__KOIxI6E3PA23lP8LcSlh653rbmwGYZgDFJXuG2ATPB8Qr3NzOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBA21NC_REbYRU3smT2aMqu7eeocI3svD4tCZ0zpSShdnBgh6cWMzAEp6BZuNUwr4KXL59v59zaRLn-AHokcCSoP72GFksIGi0RPUu2Ny7vGQmYm8LUwPIBPOpjTH0yUsktYO_Axz8ro4DIh6R6EDKRQ8jDFOHbep8e1ovGmiHHF9Cl7Oq26_WupmdXlN3qw0C9h4UJ9cKj0OZ2kWYLdzllqbIc7frTPmdxx5lTX1NARXGTEW8UeHVimLaY6-v4ZBvLszVBoMZQj6gnyYQdsYqGkPn_CRNDXSn6C59UqQPgafOgOOazn9Q_JXwS2xqjDujWlR3QzpqhuPrbTAWzg7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRWleD1wJCeNFTf_J917stSme-XDZJT7X9n_gtvtFTQQ6Qgu6WuM4ICKFrf6fAD2BsKIIB5bNGR2Su8pW0TNHsglFDarXzssRzCp7-p733cojoM1HqYmci6U-BkO-4QruEm7rNNTv1ozdMidA7Fr05dKxUj3nWnsvTN1OMn0XIO81Hud7AgiTLwwPcGOUPjKTLMTvXF63RgQpzMeLLnAi0_UNttXGlZnXHj7ZAhqCyjnd-9MHYPLMaHJrA8uyO13Xga5wHVKhicaByK8CmH3MdOckF0sCzcbdL88jhuq-ys2IfQ-JDHphQSWRU6iB-jo1DAVwXkLVhOG57cdFPkI0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKuR34aNFwUS9BQz-OLpspTVBHIF-mPlR0FJ_7wscGq2MJnlALmiyvnVAgYCKsScvdjOOIuJ7RQIuMinF5-5J6ygK7O3jh_eb5SUImjHFDyYj7hZQi6BfTERS5Th2I-sWHDnhlSv-_HTMtnQeHao6ieDNr_jF6wuFk0JaIc1eo1oQW8rVFGHDMAFLIsb-DYuOda98ReXmltIWhgBgtz5L1jIravkG-IryeabOJuQ0v-ZFLrKQ_d19_zTU2fKZ3RUNaFUpJoa0xX4re4LdjmZ97b2zKmmfCrUVTI1rWditEzDCvN414uZyQv8vmyLRkbbVR_ix4x6EvbMewsY5MPFvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4BMQUUbSsdsjcC57Eef_XVbeFSLK-JcIHE5fTr90UGEriSnzLU8FXZFon8evpYUX6fm3L0WzYs1Dq4km6dfSoH5Wub9-vX2wt0VuvXewSmRXTIPcA2lvLMbYkm9INqMwWPWw_vtczxNe9K2CjZprqsWPyCkN-NzdgHFckOYJ08qW8xnOsraiA6SYQ1Sk2byp0NyGfn7LLE4tYH8Dh2Cblu4zJpx_be_F7Qn5hQKHOcXo21xpgF68kfUeTzb7sXHxPkiBfX-ppXll5oBt2yPc_f8FDkcpge1OkS1DiKovPK07mEDaBq8Pkr00rFVNh8sAz3fW_9Q019IInEEjdSLsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeSxu0HikGEsjw0VY29AHoc4x4pe7pi6hbcQGwIMfs5QV1RnljXbb3-oBF-u6TJc934DswZiEsuVyWPqlRKZmhQ2dfvZYAdQhCTWiQq_t0PN6Y6gFl1Yqc8x2fst7E7DIGj0Qc8xdAnYg5aHE7ArfJwdxGzfUqBqQwnyM_YwL8NxZaeT0tC_eA5kGCFvQVfP7BsUoR-R-iR3tJjRztWi0E4LweZW3gPGV3rkDWYkLJdysNFzzArgW7jhSgvTUMqpYJ1jfX3VTl6J9DLxPj4ImB5bF2hHi6iX8EcoJY6Am3B7zRtnhiuZBAT1I99lJLPWr2UtmXnpLPngqfnkCiqzyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8Qpyy3yIQGSC1rrBJHaubjcp01PGFlU9cviN1BLEVx2oha4T2_n1qs5vIADxM-YREax4lgKDq6YMbqC_vOjp1Y-WmFye8uR8CotUnTcQF0cqzvVyAr5vXsiCnuyTLvYPiB9iYBwLfi2Q9EzOkMGD3I5ICSTVrBsCxnYi7WvR2KoImG42ET1hk6iSiMUWNz5HD-cXe_WhQr-lvF5qhZi9EnZHB0_DvppBAWbbkBV0JfRD2ukXDsHOTXOuA64m5g2pgB7J-3qkNpq1mTiTvZi44p9X9Ooef44DOP0BPPtlHy3rj3XojfL3HHR8EoJQeiBNX9ag4di-GjK8B5yYKIn5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ka1dxdgMofnCv1taiIYwWcAHwIxJzYzbV-4fjaPjSdxzfsJaa3hMSETFM6A3skjrBj0IZqvTBBavgF4ZacVt63IoLQOX8Ebvxq0Bl2XeOMx-1x_iYs8EpFTYl9VrRGqQ5Y7FSPkVDtakh_qDKqD9gLxlPoJoOA3tb0VZT13T8c2aolgrArGKB1GiZSCG5nkH3FNYbmjJMm9OJ8AGZcVBJjTM5Bm7PX5EAXs8mA0O-RgiyqbHfYwuz9RNkr32ewvMgHA5IN2nEUiWllWDeEi1IXAqEvrILWJ5BzGJ8iR2BfQoqsksHo4f5pi03MxcO2NJQEgY46ieW5hRVFjOVsWErQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCPLL78gZAyCGkhQRzc2jyK_8Qs5Ih2_pBDTWfsDCf3hobZKp6Hc9LcTzrPJEdTpQ3MQCgzAIC7cluzramO5wZ1utzxy7njENjFi3MqIKDp4b6qL0K2aDuInuxDhwGUgJEvqKhAg_cL9dBawznJg-XqrxYeW9C563XpsunCRad-uM4P-ny0woOqQAHR0SuB6c55qpziYj6qCPfPezqiyEBXeDq3AYpT1dNiifV4pP7srm1AY_mRK9wBpl8CkZ0jXpVEBReUVLk4dA-yO-g8lZdWpkFPUnjXyysOiIFwHrRIBUdbW5zzimtZFNL78WNvxuuDuYqz9kPf34N_QpE-SMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=ICSCWAARdnVPDM_s-i8w-Sz4snhczA2RSquQkFLdH8gvZyvNvseeVb_bR6AOtinfHuYlm2_T2i37zMB6v11-18c1j0q8LtN0-MzlKGVKRk0T59k8-MgAIBhw23uw8gzC1LPh2v7d8ItN9kGlFOd-QNDazqbLnq5tlde7vQ5efEOPpTnMafZykMU5KZpo_nk3bTixTQFwq9nM-oQei-p8O3r8xbGT9oTFa_fVZIKTquN2hn9vJo6_xBjc05ewxlBDeepYEsZo8Mc7qKQbNh-PZnwzVQPbxQxmy1JmeBC4oGifysCq0rAUAjjUYujRsz8xj_LggOwKPPbi6HBWAQQ2Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=ICSCWAARdnVPDM_s-i8w-Sz4snhczA2RSquQkFLdH8gvZyvNvseeVb_bR6AOtinfHuYlm2_T2i37zMB6v11-18c1j0q8LtN0-MzlKGVKRk0T59k8-MgAIBhw23uw8gzC1LPh2v7d8ItN9kGlFOd-QNDazqbLnq5tlde7vQ5efEOPpTnMafZykMU5KZpo_nk3bTixTQFwq9nM-oQei-p8O3r8xbGT9oTFa_fVZIKTquN2hn9vJo6_xBjc05ewxlBDeepYEsZo8Mc7qKQbNh-PZnwzVQPbxQxmy1JmeBC4oGifysCq0rAUAjjUYujRsz8xj_LggOwKPPbi6HBWAQQ2Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skSSQDgzDKWxYwUhSzBgqa8BTTTOVM7z0iJmQ2Ej_z8XUt66WFOyImQR-X1VeSeYVTQ3SMeed6sd6R8wEylxSz_XelJLiM31yPPfulOv2qtN0qM4lN_bEwyOGm-EYzKTjlENr-9YtzjoqKpbn9bgqqf7rM-g4ZRO9ZA8ZSgGnJodf-EousdsFMmCvffhw3F1761q9plbLwpKNzifIBivH4AV1W6_y_DPWazh2WbEsy9PLd5QRiGScfUo0UxsV0M2kDXBMoAkJ4zuDTC5AYDdgOkpbInDg5gGKWpuTQnSLYIkHBxWqun8E4fO4Jjw7XyPncSgLPX_KlVY8Kk2bdCdAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUKthHLjlHBjDsOwywLbi4RLwAm5FvXDuWtSBdT86wQSmGvY41i1WCPEeCoCv2PVOTZqBo8t0tiQT6PzoL6TGLPnwz2FZWvQn7sUYCEVGR-5Vp26a3A5TnXgXGjv8_RqIkTbA4s5i3vK5nJSV-grXjxVhiP6lFu6BYIC_tEcBFzj8nvggWxBOTACqjWcSu-QDsMVw0YInuGdbo_UUrYgijajzWLI1SoZJDB94fFTM3cT74ex_4CHUeOw0HTfAEJMKFSGqEYTjaqdpr9CHPTQJZ5SmJc18xBcOPw-8u628xGxTxEwS-3Fr-5Ol15UcbHkD6xNY1oEcWYH_P_tUYZOwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNpHdspz7q0laZgd4wLv8SD6XkBSUvKgwlYXVU1_UBLagZAdxcXM5Pk3bFQDbVcflo1DBObNkf2-Zp8-1bp5e2Dh_n6h4tGoIPp3akY4R8sa7p_ReMWkZB1xmgjZm0MJNJ21VhNB8jF4T30IlWeurc1UEQOuz6ua_C8M8rkBO0f1pBVzBoQhvlw22Tf2uprm_epgMg4mWIUI4KGxRSQcuHcw41HtP0ZDdexDbrr576aWHeaeg06pL9z2G1tKbnAassIDzis3-sqyM9XiMzg_ZTALp1E2I6BQKfyLTNf8LRIEKV0I5V7knd4t-wKQLGqQMzXVGUrM-Xy-mp4RSrZCGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-X-8dbA9_b3Z8NR0N9pnv-NYUoi5nHgrljfmFMg8n2Jp144C1l5dcMxIkuizc3_eihoT_OPl8duUoO-SdMLsu4LkbBrWBm4HzXIQblGvXDGAGfPgYkTOo4Qj961_nw_RkoMxx_oM8-bEu9LWZJheI1LoPI1VXzQ3oCw8a0BzcAZ3S8TFhoayw33ti1xxsy_l-VDDqd7ub3t1keNktoDQji8PFAYchKRdVHKzjH2FLYNVPQjpwZuK7tb9b8DY9gREzXwZ1rlH4USV8T5VBB7sq8E863M4GXrVzHm2YqpHbIRJ6SzOmP80mhkJ4QZ05tUdeEmtr3LvussDOzr_TZzWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ha43ZH6ay3TxXNwg0VN5-JK1Ex3Lq7_uKFwCRCWRgrWgby9ITT7NE4jPKxugjmvUEwE8JllJBWK3p9rRT7ngrcunePrJJ2V0Kf1kkwj2VWMHWZP9yLVj6pc5CN56A0_3dO0I22j8M_Gb_fvMmiklgHi3hPkdQgGeYl0n0OJCx1U1M75z1SrrE6TDX_4D1oqHhqAXZ-DmRYx182_8TEe7y6mbNqd1S6XI5LUvuF_G8ozdrPKl3IHnZOqlLKsHArii7wM14qrXcRIFaOHGYZWtxFi2ku-LpIU2WDhOQke9xnUyCu-ZE30ttTQPbWcvZk-jBy3aXo0sYOejkpUUkZXxvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJIz0ftnZYTkFg9Vox0rVfHeXlhfaC8AxU6zM2rpYLEPg9wyHK8b2URoOGOh3ptolauhWRhGTGR-uACaPfLStChhGiLrnEcbjY5mtFxrfzvnQO-txkJwEoyfb_iUK58-wBqrj3QlBNXoPchhMiXrsyBYfo9dQLWrYQThcv9EVFNrwQN_A_viutSupVYoVWuf5biHSbaonRbig0LRsKR-KOA-1hw58qFqB2obsYFTxR-CFj461kw0PjwLFaW6Jrd5Odtif9H_gepFBZHwmtG63DvW75Pw4TxaOI0Sh1I3sJqXZyBYdaGSCkYILnpdckhIVJhGENdfojksW-fvqQYFLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUMD06i7uRbGXxUo5UGP2Uez-1RSRJmIFMslwiZWCKoEX0eQ98k9O4frLIh8weLTWwa4bSMSNtb6_K5EkTCJCEwA96oHaNPTGq1rsehLnLODcdfKnMOH9iRQJBCfP13GPJ9xM3AGHcmwKhfqAC79sdI8-Lp__BMddPedoKr28VyQEkoJOe4vBbP8BsfNphWfkqxmS-osK9qU0CWAYP_pDGnJ91G_-ES8Hsco2FNh3IdA9djhYYp2xlRf9cDLJ1EJ4xU1tiU1PO--fZlrRTTEaVspllPWhAX-yGZLrK-Bo82UfkOq5Hyd36xzJRfqGsH6By5-yNRY9pvDHYfrQw35VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0ZkFyK-R5fAfhbKvm_JyiwvFmZy-2s14K1cuVNFV2XeDOEHvhDS_x82y6KwsYKoG56_tPFCsvCdxpTNtX9NW7KZQFWdKRSvw0Iw6qY9uafr-lGmjlDz0Rd-m_pJvUnU2DzvCBDVanOd7Gt5EvZQ1aZMNaRjVzBn9bApAAha3rEmDZKhjqWf8kWatNL35VYrfIcCxowbrxEthcvFRRopJaFiqLq46zVl14ztD32KuLE_y6MIdEhD8evwa3_VBPrX1DodsRRXk2VxL3dY7oyL4eJbmarYOV3EGOkf2vIMXlCn_-sK3xUbQ3Q8oCmDrZJv5i7YndsYsyKRzceJL3OC9Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=W49fbQ0cS77tzvnTB4raGXOJf_veSxNQWj4Vp_sfjt5wKdY37phxQ5N8cUjuckLr7SfzAUEKHTMTykOXV0C2-c8jEDpj9PvFHZPi5WxxTEVemZiSkF4jAdEVKkeioic1BFD0t81U8LvGL0bQUyNciAnDHXLAvI_RnBRcjbnJ_IbG-TMv54ZNr6rX3y48rplPyfrdqxUJUTcqukKLjfrbQLvzdVWa270XtdFtjR_b3vOOEMhiR2FjgqMGOxqzBheaem0qjYN7ppiDEjISmMgYGfsJK4-0T6V1qts06_H6RigPtBdCzkHkjCoRScxRKJD8jcXTyMkZnQm0Ejt7vNV_sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=W49fbQ0cS77tzvnTB4raGXOJf_veSxNQWj4Vp_sfjt5wKdY37phxQ5N8cUjuckLr7SfzAUEKHTMTykOXV0C2-c8jEDpj9PvFHZPi5WxxTEVemZiSkF4jAdEVKkeioic1BFD0t81U8LvGL0bQUyNciAnDHXLAvI_RnBRcjbnJ_IbG-TMv54ZNr6rX3y48rplPyfrdqxUJUTcqukKLjfrbQLvzdVWa270XtdFtjR_b3vOOEMhiR2FjgqMGOxqzBheaem0qjYN7ppiDEjISmMgYGfsJK4-0T6V1qts06_H6RigPtBdCzkHkjCoRScxRKJD8jcXTyMkZnQm0Ejt7vNV_sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEzS63kqHCBUE80Ff0vXc-v2BEsn0dh-xiQAVuGKXLBX3iQYs7xYC65_Hc_pYhaSLLTwBas8ct3DQOThvQlDKYVAKdJo0k2_D2xGRivuIOa5Jq0Wa7J3v2Hik6Cms8bAF3xLyZaEF0m-HMaXHAogBVy8GvRr9fINigFOUYZHznGzEDRy0UUfn7ZnLj4eK8zFCLFibxllF9YwXpWXAzoJjj5DNgia68r8pLSu96Z3YycpnmCh2HArfraEN-5AneiEkAAAmcSVYS_kZivWacDJxF0yOK2IdepFnohrj8Gt0lyzFfHL00xoNt7Tfi3QoOnjtQKgo1dk9c_F-0s0J5ehCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T93xgzzeZZpyau-icDx1H7qs5Dbm3XiFXQ4IbWTPd1fTDKMZvEpOLKZ9E5eBouXLgpz-wkqG5-T2LCSGgz0_jHbBW7NzL9easXM9TZH2MCedUgIjFOOtYSrFRuwQQwHJXFoGSTQBElf1B42qCedlsDCbh7_z-9c99TgqNaBBi7Vr_JFK3FjsWjoT6ngXPdZT9-VuW9zi4rT6mp5RWpkdLo7JNQPpTQodrIBJkKyRGbKVUS2k7klqrqsmi9a6S2zxxXknaidotc0AZT3Qg4kJDj6bsF3uQSddnvRfcZtPhpWQVpp72Z529_nQzFrkeujM0E1NzqNWi1WlH2kVqQ42Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWilrHYtfVoo9X4WjJ0vFqaHbu1LbfhUuQ8Prk-AHanxMfW9m3N65eyhMHs-O5dazpxej_fjaFRf7Zs0iBIiE51fzfd_7aQfCnKGWtevGp80vjX6gCpt2mbtvLJso3lPeal-VsEauaWY0lVN8HwSkFGV0yJfzZQI0ZBNSDtKuZyXK-GxnSSloJ_-D2EFzK7OYh524SDXOyP9gxMfQFFDQyb8lyxI_CHCWq-eB3BsjaFyq9ZNCOO2AtU2PDIgmIEN4oUPoc2tpqmVsoQToc2zDy3RRSLUyzScRO8MnEZG2Qo_wj2_B5CnL3RzkKqZ2chYS3gmynUePuGTTSki_waqFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQfrIpNvyGE92FBN9tJVnDloFWRwAB5yOh1AWRV2MkO1KDUQIVd09lgeHC73FnMBb_Sb0odgDJVJGrHPuOUcPk5kMOeJBalf8oZL8cbF9UO8qXRvFwhvq2wn1UQ9Nca28421fAUf2z-q_3QqRfPRcfCU_h6ZL0hMzwKeJy8tWV_Os2X6DctKvfst0bXazZv7WE35X1PbkMjKv_ZbpPL00mA76gDr7XKeJLz6oZ5gFIcrMx8x7LzduHk0-7xK-6x4YNSVKJPxd_chqvYjPgAa4OxcQlxoqeS9_8tl-PP8XtzR7GjkcbwPfoNcNb777jBknW-7ANMxqIoRH53fHoiUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bW5v-La9lJYHLL6v5MYzVSMRJXvXloMv3ccr9AfhnS60K9OC6ahYAREvuyP3nSZkjr9MoNvAQ8Sv0PaeXFffGeXxIEMfH16YHQo84UMo-_94Zrrw6WDbrb8hc5TIcEzdN9AwfMom-wUwwVXZqm_5gBQ4UV5-J5mGiXaa0oREIJXqct-szFRJYL4rQbQYsiaFHmIYBef9SbMW0qE9S5diwBt13mCSLgwCwbIslque3CoQkozphKDXbuNR5I0BZgO_H7ER3zesuViY-oNGAMdms7v-oCykGI3FpO1jZDI4o10PgFtzFg4R2a0xfy18II5FDyV2BRkq00CccDiiUBZMRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3_f7tiT54NlQmcKCd8gIhySF8dT8AnRLI5ZC_re3B8yz7ICtnt4mIB031JGo2TLrpYz76vdDvoO126TcrK-CRu4geff_UzNCBttRuVz407ZA5pxJTrA6INc11SLEffYcqRuFVW8z1bkq6miLS3y1wmaVHMmclUq9TUtRdY26kNMlJybrbCCPx3qgVbYeBps1vG4tvclRvcF8HZwew6UhqI_Nv2zUbJ_jm_1HasZc9GUp__Fpiky7S9-cXYZ0NKYQ_dUqvzKGuERlkhVock2LjSUMoATlH5Kcc2vDcodaEqjcYqbBwFpfDarixkH6jaGVJHeCCvCKCImvn7ZdoBRGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dp7kVEZIw2ne0xCgwmaO_gFHiTLpRYDXMNcVc-EM3A6NRp8flEBKSXjw_Ji7aKMUdlhL4SLfe5Jz-FPG5DWbYoYoCZznosaSXhvW_1ZSa7R4rNt9Zpot3mmAQz5y5hD9yKq1wvLibSjprbrkkww5SBhFjwTzkZAlGhJMvx83s25a8ScnbxjLeUN6R83q1Pj6KKWUOUw3MWUE0DR8I_o4FKHHnw_YzU8vB-K-Z5eGDb4GWaWTDoxl2lw41ZGoH3L-8dgBzXqpvALgxyI_k-WqLY2ltTc7KcmBdOsd2Y0jIY0-_p4_jleY4Zt85PkN2IC3nZTToY4zj9j422TDXRtV6Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=pxEWn8NFyLrxpCKrX0JrSDTM6-LZXrMKrj7fxsG89X3d7-SGZe-sS376JOZL5C6fRdkcL--B1byhXSN1eeo6E9rbFZ2jWbXTT6iaAaye0YyIRwLdUg2bPYBHUbmi24cqQ-GBCRTkZDS3l7uYNKMeOdKcl0VyX1_FDeuLFOSpTTU3U8yie9U9KXyznfyP2xVLBYLodHXTd69CAeWc5FaThOuBom9P2HaF243JNKR6y-ojfxtcOqbgrd8aAoa6KGtWjBK__NTYLO65Cts6lzMakeVwd_4IIO6Aja_XauHN3IFgT_tMofgLL-8uKKXGUZVkXuQKAlIRUwwHOp5s0GZavTsJ9N_ogfPoPsck5A46TsDc5jUiN9IuSzvGATEGxFgzsGYxF_eWDZq2srKgzlUyusZNDPfaT1yCLH_ku2fszQ4J5IicsnvbVK9O274F9B1zazyVA9iMY173NDRkmk7Zuwzf2NjSlIUMx1BAhTllsnQAibqK37QZyGzzYUaPuYImavSUXvrcIQDVkupo443NMJQmynvDiIRYyTMznu1fdelpEx-tqXPdS8OotlRa-EqXMsO7WiLPBUUzAR6fga7XxqT0o4x-JC5nsP1hhKI6W0aTSBcDTZATbaJCr62lwG0l2F76nopMbg-TF4GKdYAc7dWJzC6xlKOB8l8LRpO0QUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=pxEWn8NFyLrxpCKrX0JrSDTM6-LZXrMKrj7fxsG89X3d7-SGZe-sS376JOZL5C6fRdkcL--B1byhXSN1eeo6E9rbFZ2jWbXTT6iaAaye0YyIRwLdUg2bPYBHUbmi24cqQ-GBCRTkZDS3l7uYNKMeOdKcl0VyX1_FDeuLFOSpTTU3U8yie9U9KXyznfyP2xVLBYLodHXTd69CAeWc5FaThOuBom9P2HaF243JNKR6y-ojfxtcOqbgrd8aAoa6KGtWjBK__NTYLO65Cts6lzMakeVwd_4IIO6Aja_XauHN3IFgT_tMofgLL-8uKKXGUZVkXuQKAlIRUwwHOp5s0GZavTsJ9N_ogfPoPsck5A46TsDc5jUiN9IuSzvGATEGxFgzsGYxF_eWDZq2srKgzlUyusZNDPfaT1yCLH_ku2fszQ4J5IicsnvbVK9O274F9B1zazyVA9iMY173NDRkmk7Zuwzf2NjSlIUMx1BAhTllsnQAibqK37QZyGzzYUaPuYImavSUXvrcIQDVkupo443NMJQmynvDiIRYyTMznu1fdelpEx-tqXPdS8OotlRa-EqXMsO7WiLPBUUzAR6fga7XxqT0o4x-JC5nsP1hhKI6W0aTSBcDTZATbaJCr62lwG0l2F76nopMbg-TF4GKdYAc7dWJzC6xlKOB8l8LRpO0QUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=G468QeFaq-_gd-1yBvW0y4m2Cq6n0zX4PwzYkxt46CJTVstBL760kcCJ7TtPBHV1RDIQ30-9St6oCB4_mO___Ozl2qp_PEtDSXiuDKB2i92M3yEY0bFo2dc674rdyGXiYnXFQnKdpU27MbVrJXPm9iFjSYTeVHeNLvXbuWx3K82KepeK2YmH80GE-5MdDqsx0DCSPjlKEk79eo1FlcAMoSap0CzgoITFDA8PxAyDDTWu1S6jii8zttWvjNP_dAJh6cqnZtBeZMluTSMIEPvATJgTkn7edftcqvbmTveVHzBzfeHeZhwzUpCgkmuSwn2uYfCB4ZoNCAR8Qzz_KGUt4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=G468QeFaq-_gd-1yBvW0y4m2Cq6n0zX4PwzYkxt46CJTVstBL760kcCJ7TtPBHV1RDIQ30-9St6oCB4_mO___Ozl2qp_PEtDSXiuDKB2i92M3yEY0bFo2dc674rdyGXiYnXFQnKdpU27MbVrJXPm9iFjSYTeVHeNLvXbuWx3K82KepeK2YmH80GE-5MdDqsx0DCSPjlKEk79eo1FlcAMoSap0CzgoITFDA8PxAyDDTWu1S6jii8zttWvjNP_dAJh6cqnZtBeZMluTSMIEPvATJgTkn7edftcqvbmTveVHzBzfeHeZhwzUpCgkmuSwn2uYfCB4ZoNCAR8Qzz_KGUt4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tR2eOJrr6EWTHFPjBqPjkCGUpJoxR-Q97YVUuEhN85dvBOhfCzxpDCh9AoY6onH8kWTHD-vGePz6ckOuMEXaqtkmm1JXZxCesEw-33cTcFri3y6qhhhFgeEarpcimT3VW2wSZ2jQu0Gf4YaK2CsAuhPFhErA7gGv3gNhRPwwVUL62giRIhpsDBxHDEZ79xSXKOjgRb0WkAgtTbpI8_DWVbCal4Dy3ScLW_YoGBCIfB8AHDf-wjxkEGYh9nC16V8tEeT1jF5On8Nz843590J7o4sfai-drbB-O7bLsbSHhtE2zmpkqCCCiV1NORpWvOlZiBRdmw6oWI7ktFYWqbVXIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWK1VWTge3MYeZjGU8v7KjAONgibwRvIV1bji9Do-1j2uTt49X8ilkd2ZfQTXKkrv_2r7qC-3NTvOX0SRb7ilnoiUoRbGfIqEF4A8smqEBfGZOknDzz_4k0DoJw7wUlArgDr3ryFrLXSwBWlflVMw2kKqPkwF_31Ksvr-KnNBK4JWOb_LFND0RD561hGmnpYv0Vt31mfBHiXTNbQY6P1ItefbwdehKLsePEQf1s9et7MmtYnmA0acWcj1i1zwNJMZIOtir17VbGQrQ2_PsBEmTSVcEv-jztUrpLBUVbMoUn3OhGBM4U1i-0welm6ID8azE1bs_l8Yl1YnafxOeZcfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=vj5ZgJPymx1OjwX0Ia4vjG8BcgoGrhu53JugP2H87VrJB29rZ9-4dhuom2b0EKH-VH6Kibk_cFi7C8ieyZoNIdJAzd5506IeVoU0Me7ezU30_1g94CMXFLwqRuIaG_gu898uWwSRKOjb4XCvQfvlGcThSyDRsvub6gk_GflyWGokqvCO6glfxsK_k4KN4W5sQ3_vp10YRRouPqxZEtYyxmHvenGHcpDlVeJr-YL4hrGXEzSCrX3hVASEOFwXgTavleFuNT1vEZ7zprYqC77PXTI8htN0Y4LiKcyciqL00jUElNM6AvnWiNTLtC7lhKl0hdLbeik3945eju1gy9iapjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=vj5ZgJPymx1OjwX0Ia4vjG8BcgoGrhu53JugP2H87VrJB29rZ9-4dhuom2b0EKH-VH6Kibk_cFi7C8ieyZoNIdJAzd5506IeVoU0Me7ezU30_1g94CMXFLwqRuIaG_gu898uWwSRKOjb4XCvQfvlGcThSyDRsvub6gk_GflyWGokqvCO6glfxsK_k4KN4W5sQ3_vp10YRRouPqxZEtYyxmHvenGHcpDlVeJr-YL4hrGXEzSCrX3hVASEOFwXgTavleFuNT1vEZ7zprYqC77PXTI8htN0Y4LiKcyciqL00jUElNM6AvnWiNTLtC7lhKl0hdLbeik3945eju1gy9iapjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JocTCvzbQPIfuyHSuTBp7jm6iso9x4K9WIl9Og0n9piqoPpm_bZZy7TubCFYMgCr3JLQjqRDrAqArYpY_MdfyxQfNY3M0VoRnPInsIQ7DoJZWEOeA7iGQR7JXjdHVaseKWoMzwarrY4li7a-YpQ3hOc_rnK0XZMqURtRbi8i7IfkIvsRuxSTOqUpusPxKxb7IpGUZz_5eLIB0aENILcXliumw1nK27EREntUb86ViSVoYv0s3T1hlck3AXNwTDBvPOUrgiBp8_ZgiFxBW5_LoGIpqc-EualKUrBF0pknsZIb0OmpMS1EluqtcLLmyyhFcIi1Czsq3VaK20xbeygGbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaZu1uVG1RreinMqtgZGx8KEt7YJgkqyyZFCc2wHYc5Y87QlCFvzUHnsePDrvCUDwU95kzDrOiE5nxuTjkFQ3sx4P6vutRrWYB2qChqG9r8-nQAZN6qeRWcSeEbrCwvti_JCcM8l9oZsTu2KU1WOcDrk8lcxttY_wSZP8CncD_JaR8JSv8QImZcZOQCsrp52fgUySWVOhpP3r41oZGPEH-vVRvlcx1EuOXc5yujKjbrZFZOB2nttvqz_eYCXavYZRsnU-hHXSDLPy4dAnAalC0nJGcCjp2Sf0fHjquN_xs8wpwuCFzmxgiVBW8jge03poSKXPmBm-qtGpr9Gq2Ak6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsMkhUe__xt9BfjDn1YE59YOc1SyvkH_dB7e_lzXyDhn4nnV6eb8r2XN_zsHdoIQAH5E-Dri57vOso8BUBEhX0EB5DTt8N8NF5jK6d7-svqv4Dmeb3jFZoaqmzFb1P07TQu4_uRe72h4AZj230kaixM1LFjH_iD6LkfH1LXi98ULGjREtzyBD2pr4DJa_gKs1StebPow3g3DrWCJKrx8KlOid4hJgO1DuzQLbYwhfY9jNJlTfXjKu34aSryH_-WQNv5j4LNNmLIWnFptOlpDYFkdHnbwu5FzOJFXCSzO_zRGcqhHvGs7rglYod4QvrGKSRk1AwItX8tn5keNeyvr1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dA2AK1S75ChOLL6CPheDbFTJTX5YdQv9zaqJrIAsp79TVbTdE-jiTQ8VyM9kTK8pOfufCHmJSkvBjUbJb0r5h-8wrjH9xHcVgQlCjQJ7hSLRG03hzAwiS57wUkW1kl_JJXnNqAIJt82qWx7JsfKDcguyh3wSxuFyTrhQIJe7GAkuM32a5aa36Pp63KVTjkThL_AAzDyEdrDCiFaV07WXyxv7DH_Q9j0dKOJ6aZyULIyyFeeS_61p4yiV5rgtEsK_J-aAhk63MOlMB_2v8wxoNWhqyCzzVrNAGTt1x24gI6hS6hd_mNvQeTqSE0A98kpE0XjtJMIOfxqcFAM55GlqaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJ4ob3ff7jCWHXjlQlrDUW272yKSBHASNXV-rEdc9CVXkq6SDOJF5ngfnPNhd875RCBF1FspZPXdcIMM8RpcYL98LJu1wbC5C9swOoQdJ_xfkZ980Q8t1PfGeFhJjRDpCkYBl_8zZeNkYbbcruqJqC8MQzRz4AIQ-Q3MXWn0GauUm3P9MwVNIqwXCDq5sso5itJVJsK-OYYB8kIiFL-jkyPpGyZlpXmuSqbt63BCckSd3yP1iNFUrO8P0wW3_bilD9ADBowI9TWT7aX8Rn6mWmi14AKrX8HP78A5-yMMHuyN6W7Hd9bafZmzRddXXMohDC6WwAHXbfL_g8qj5akItw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5TuQJ-HSk1gZZCItB4No_0dYyYkwhAPC9WKdO11iCizowtzyVqxAR2px2qrf7o8mvkSGtWmxb6kNDLUOjkVmOka0GqlAn5ByfxaTSoH3EeGtInHMAZW6H93RCDZwEADp7aL1mKjbU4IvkOry-5b1PrPwLFsANgMtVr2QD8cW8M3xBbWytm3rttUQdCHf3iRwCp99PBpCC7JXQTDPZEuLtylQ64Y3r-d8eNXgx3ANXUsD-VNPj8wNkxAGnxkhJi1RuS-HLG6nx5TzyrzrPyIg8tiiZPFkwI9s9rI2HTCS_Hnp8bbUoFi6YehK_V375ekWT7FMAvocIhOPkT9-J2fJt1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5TuQJ-HSk1gZZCItB4No_0dYyYkwhAPC9WKdO11iCizowtzyVqxAR2px2qrf7o8mvkSGtWmxb6kNDLUOjkVmOka0GqlAn5ByfxaTSoH3EeGtInHMAZW6H93RCDZwEADp7aL1mKjbU4IvkOry-5b1PrPwLFsANgMtVr2QD8cW8M3xBbWytm3rttUQdCHf3iRwCp99PBpCC7JXQTDPZEuLtylQ64Y3r-d8eNXgx3ANXUsD-VNPj8wNkxAGnxkhJi1RuS-HLG6nx5TzyrzrPyIg8tiiZPFkwI9s9rI2HTCS_Hnp8bbUoFi6YehK_V375ekWT7FMAvocIhOPkT9-J2fJt1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnGG8WCvt3A0oUTn7FHm8C3vG65q4tLB_rsJThGjlC3L9FNawjruw5f1MZ0LUnLqIrwDeu5l_jEkA8JiJmlSSQAokd8sr3OaH5yDmRpX61HX3ii4HzOTncaz38DKX6KvCRrjKrggKRm5oT-tgbz3Y-A49csDZ5YqJGITcaE5Maf-u56TFcgsjtZG94Cym8lZCpkESAZ1u57FWhSf1bLxn9-wwY_vynRRMg68gaZWHtcMbqdJY8oP6TSQ9dW7ti8RAbF7LrXzgM_E4ekZbz6M5XPc4H1jGcio_lS3jG8ESW5-KREuRewz-mkN5pEKQg-NxhibPFTZlzLgiWE7JWgmoks8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnGG8WCvt3A0oUTn7FHm8C3vG65q4tLB_rsJThGjlC3L9FNawjruw5f1MZ0LUnLqIrwDeu5l_jEkA8JiJmlSSQAokd8sr3OaH5yDmRpX61HX3ii4HzOTncaz38DKX6KvCRrjKrggKRm5oT-tgbz3Y-A49csDZ5YqJGITcaE5Maf-u56TFcgsjtZG94Cym8lZCpkESAZ1u57FWhSf1bLxn9-wwY_vynRRMg68gaZWHtcMbqdJY8oP6TSQ9dW7ti8RAbF7LrXzgM_E4ekZbz6M5XPc4H1jGcio_lS3jG8ESW5-KREuRewz-mkN5pEKQg-NxhibPFTZlzLgiWE7JWgmoks8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=THvGyt3jc7I-0kTh1FLGCnb9qwqo9nWurhnH3nq7TBe2kbSJlorEVsJwpjt46MXntLaVwq-vibxPLQWgT-WqNXW45HX40Kr7lykxZxJ0Ul8wNZgp6CVfSq2Fp3T6RAM7tiII_15W40iAt_OWaWEo49zKR5t5FW2FR3lZPU86nkJFPFZgUN56DLiqey-m8GhmfWq-7MauPTu3gBUJMIQGZ8wAQSQi8ksi6z_M5OtCOMYjP4ba3vvQpXko0jONnpkm_r2lOTgpknMjEaiqvq0moRYikChgkJQe5bSEKTt1NKXZU-Ya34Yywa4b9K6K55WclRzMDWO64L00JEafs916FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=THvGyt3jc7I-0kTh1FLGCnb9qwqo9nWurhnH3nq7TBe2kbSJlorEVsJwpjt46MXntLaVwq-vibxPLQWgT-WqNXW45HX40Kr7lykxZxJ0Ul8wNZgp6CVfSq2Fp3T6RAM7tiII_15W40iAt_OWaWEo49zKR5t5FW2FR3lZPU86nkJFPFZgUN56DLiqey-m8GhmfWq-7MauPTu3gBUJMIQGZ8wAQSQi8ksi6z_M5OtCOMYjP4ba3vvQpXko0jONnpkm_r2lOTgpknMjEaiqvq0moRYikChgkJQe5bSEKTt1NKXZU-Ya34Yywa4b9K6K55WclRzMDWO64L00JEafs916FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAyE1xGMxdRDh2Hf_LZQ3H8YkBEyPVb-V8T8mUQClzmpkALm8-I5W-VVA98zkiYYYQrDF05HvXtwcqJoC0JNWJeHtK7lC_J3SnSP33IW34wCKH0p9zhSPChV6npX8coxMD_Le0IUdYNH7HlSJi1Jf30xn3_fYDDZ_7JHyD5pCGLanZnxKQR-SCXd9SmHkKwptqOvcIAz8WULwLNMqvZ31Ue7gIBk3afyy7TgyufMx2HL46MFLvEUiDdJw4KmkrZ3UKEeIiIOOrQafaJ6-7XK9t71p1q7nFm238skMp0LdcnGXvoYLaDqEj4RiCx7m8bymDmvSX0DZLJZGfPcxvrLHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pjg25o6w_2Dh4yK00afFUVgcLDybM62fsGAmi5fD0Wi4q0PS9U0CYx5SovjBSnq9Qkqvz4zFGtokWoMAeNc-HtJETl9zCWlVNdlawDcdpsxWsBTh-KurVtpxSncd5rBTyafK7TMT1iTlGlhyaJ9hovqXXG0zNCX-ARlJcEOs9I0qfPEWphuNxHuutqV_zPoYe7LL8td7QstlSYzJd5BuCQfjk1cAk1zmCBTw4oKu2iVDggXlkbarrBEwrSzIEU7m5OkeR9qKzqwTFyecPYY0o4esJjXMcEVz6mZNMdokNC8UgUbukq5Bs_b8MGKuzRiOaq2VRsw82EC9LmYiwVSyXw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=D7nU8Y-ro8h1zv7J6rVR3871Z6Ounnk5Jwi62o7-HtUT3j2vEaNPooKetRJWWK2gGYZdePyws6NepidttYpKJAkzeQSepN9doXVLoVW45AjXUpmFNXE56GkruYy55vBgb2MO2JEwtj1XJKQM9Z-f5VXK20CTjzXsEMWf8gvZdmDRIDoxhQY6Z91CxBjbeoklHAbDWxsGHhTrQzFs7c-jMTIQevrfJRXKbYjKd13gabERjcbv7WIDCMSmM4CSCDnAl9mQhF9aByZUi3WnK4Ij8WmdkQ3zGRmo2Yp96NYyP-YcbcNTuOWkHk-5iS3xztMtl13ZjiTJESby6RSc6Szb3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=D7nU8Y-ro8h1zv7J6rVR3871Z6Ounnk5Jwi62o7-HtUT3j2vEaNPooKetRJWWK2gGYZdePyws6NepidttYpKJAkzeQSepN9doXVLoVW45AjXUpmFNXE56GkruYy55vBgb2MO2JEwtj1XJKQM9Z-f5VXK20CTjzXsEMWf8gvZdmDRIDoxhQY6Z91CxBjbeoklHAbDWxsGHhTrQzFs7c-jMTIQevrfJRXKbYjKd13gabERjcbv7WIDCMSmM4CSCDnAl9mQhF9aByZUi3WnK4Ij8WmdkQ3zGRmo2Yp96NYyP-YcbcNTuOWkHk-5iS3xztMtl13ZjiTJESby6RSc6Szb3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVnURNnDND1KYciPHab6nEB3TshnH07VwFKv8d6VnsodnsHaQU3_f0rfw5zvPN_l8Vq5Q55xLccG8kBj37ie1qehyP8-2AnCdNYkfyLyNexiUje1UfJedLiq48j63bTnkIYs9P3mNfYKNx8utPq3ApNTCmTX10TRvbur0qQV09bibwMy6rp9_MNdtmUrjwNCkuj5aDHEX5zt-B1Ho2LrzYbFQhmWNnN1ZKMKvQlHGmjtlm1SJhoT_vwdtOU8Cy__XXip7WnV7yP5Umf4EjYZxbnue4l0xAl-WvUMFXgwvYSrbcVsaYLkPUipwD5b6VdUrSCvJa3i1r5dm8hFGUhIew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vkideNER7sEH6XLn-hpu7PZeAXtZgIRznne2oi9RzdNEnA_n0VGLjrcXgLJ_eDyoEng1Y123rM2EJ64e7JtB3QVJ5ZzxuxLF1jySJWJcjf29ZBOiOwWRog0BJQ4tNEzwQICp5GOuopg-Aahk70_EBH6XONMWh_F-BE3FNVGUvbHUaPCxaoJyO7DhSTGR3Jqsg8Or9JtRfZzKkfhl7BJuknPGVq07oHDmnjrkFJhR9y-lvtQM_5QGHPuwE7AineCLkAdBmFANdi6ui-UcNOTpBB6iAC8yycdn_rmbEImNaP8SVvCCP6M6FfdH_PBXLbMQNQPIgMk70F5p5pQ1YHtVzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gdTQUfeMNF727BgkApfDLribyI6q6AwmdjUHrTF4xom9-Zyj18qFWlcDDPZ7b4NrGIAOSIaY1VJYfvpYMlUbSIHY-hPkhjgeTOV5nHqojjMilnZfkF-HiUWR8lqZPtVWvSx20Z6GdqNSGZhdT8MXU1Py7BIps5Igg603O2EMtcmkj2QwlFD_nYTjM1O9CTk3xu1nZ4F_oWqm4oqwaqIOeDTm3uaeS_3ZQlPBJ3Bn-51QyzbBxUX9TtvE8Df8BFMoz5vezJV5pTN16epUSjlQT0ttUfPBy6aFLBTI02z8Y5grtKE7lU7u_tjVZwVsl1uYoS5YmfgDUyPeGhjBFFBRCg.jpg" alt="photo" loading="lazy"/></div>
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
