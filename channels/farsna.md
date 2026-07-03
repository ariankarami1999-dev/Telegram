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
<img src="https://cdn4.telesco.pe/file/RphuTCfrxuxxe6lK-0EJ-_tqfcS_xT4QZ6cnUajj8RB4WSj2cLqX2mlmeFTMYkzS2Qisd8bmt1_IeHlbcGrLxjigrfNEvuaYQpdGvP3TNpwK7Gpbit6vnQjQNmMqNOwmblgTt3e7RqnTtgBovIbDkjXjdnSVaZ3G1-ND6_d5_jz-bIwtEOwwgVKjFPsXQLRrM-D5M-S6kLOInxOhWSXRblQEHu8ipkd_xzLRv0p-Vg5wv3cbHD2Ar6yJ60yjKUqLKAmkoF-G8exAyIZdl1UqZr-VEJzq6K9zk3npqgsY-zuXhlFMZ03ud4ywOwXnvUzpbYvrUPe0nWmMgqXpXqCaLw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 09:52:45</div>
<hr>

<div class="tg-post" id="msg-446163">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc1efa7b7.mp4?token=p-cDbPXUa7TPFFKlLwU0cnqzY4NVLB39cEGfgun7hwJIWaJzyRkrgPNz_rbCWJ9jCazzwZkzRZgbQtVXmk9CxZf3zK3hJOLftoqoUVa6ZkIai0FkX_GgeJH9Uf_vzwWm2a9sXIBYZTE5AxL6IzlEf_6yN0oilByd03yUJn6RyXnhmTfi1GEcFa0FUYMvG9J0wYgSv-edqU86bxxaDGJjO0m1HEV2ia6GSV11LGFtiACzau8XFxyaVSlpu_TuZrDbHhx6WdqyLBPmFnhDUxNP_1CMEC_4qh4hRykV-ugFSyeB4cgOmjxtRtsS6unOavwNBFUMVU7Vc97zx3YnoLTDWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc1efa7b7.mp4?token=p-cDbPXUa7TPFFKlLwU0cnqzY4NVLB39cEGfgun7hwJIWaJzyRkrgPNz_rbCWJ9jCazzwZkzRZgbQtVXmk9CxZf3zK3hJOLftoqoUVa6ZkIai0FkX_GgeJH9Uf_vzwWm2a9sXIBYZTE5AxL6IzlEf_6yN0oilByd03yUJn6RyXnhmTfi1GEcFa0FUYMvG9J0wYgSv-edqU86bxxaDGJjO0m1HEV2ia6GSV11LGFtiACzau8XFxyaVSlpu_TuZrDbHhx6WdqyLBPmFnhDUxNP_1CMEC_4qh4hRykV-ugFSyeB4cgOmjxtRtsS6unOavwNBFUMVU7Vc97zx3YnoLTDWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور هیئتی از افغانستان برای ادای احترام به قائد شهید امت
@Farsna</div>
<div class="tg-footer">👁️ 394 · <a href="https://t.me/farsna/446163" target="_blank">📅 09:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446162">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ae670d40b.mp4?token=ZYG83jtyXg6LmrOkjohqvE4rHmSpSsTUxILDYLtHz0nA5SXTROB_vDIoWerQPey600537O9rdPGfrFjrTU74cQVfyZeGIZiduIBr8XvVD4ab1Xr637nRUSmpcm-NT73bGmGQ9Gf0472iUvKRiVrmhadu0Fiq5_I71np_3S7MZ07THlX2wl6sPfxu0npZOrTwuO47QKsC-qZ3pBEsoJgmQYK2hmIef_Rro9SQnfbQUsmwlqg5Of_w59ka72DjL7F1GFNBokVg-UUxJMGSL7A9CTbba7pm2bgbQ3hgEvnPJyNKuQhFFSaA-fUFTz02vQ4pwrB3PbzbCoS2D1gIlAIemw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ae670d40b.mp4?token=ZYG83jtyXg6LmrOkjohqvE4rHmSpSsTUxILDYLtHz0nA5SXTROB_vDIoWerQPey600537O9rdPGfrFjrTU74cQVfyZeGIZiduIBr8XvVD4ab1Xr637nRUSmpcm-NT73bGmGQ9Gf0472iUvKRiVrmhadu0Fiq5_I71np_3S7MZ07THlX2wl6sPfxu0npZOrTwuO47QKsC-qZ3pBEsoJgmQYK2hmIef_Rro9SQnfbQUsmwlqg5Of_w59ka72DjL7F1GFNBokVg-UUxJMGSL7A9CTbba7pm2bgbQ3hgEvnPJyNKuQhFFSaA-fUFTz02vQ4pwrB3PbzbCoS2D1gIlAIemw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود رئیس مجلس ازبکستان به تهران برای ادای احترام به رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/farsna/446162" target="_blank">📅 09:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446161">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3CA1cmgyUhlFNxcbjAZBCoSmH_UTXck2AxgQ3CeCugJurijH-gR58PEvZ0tMlTmt_KkziUj-aVN8fCVLmyloWquok1KNo2WwYcXYaAb0wUuR4xO9gsU0Izr-U-rgwB1hOB8p0ON2UEqO3FEi-s_Y-8Y93KzHNfXKD-yd9Zke7o7pogQy3660-yKCYai-EM8dnYWkT1yusjJ7G3DUXkOv25bTmCLJDWp6dS0F4Exj_s2m-BUToSEarxMAtyRoW8eNr2RKEES9jZ7D7cJXvtmF3dUyYeBdRxqLVjZeJJL_6-I4h5SttQdKDo030SKGygGojf8wIcYoRLj_omb8zEblw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رئیس جمهور عراق عازم تهران شد
🔹
شبکه خبری العهد گزارش داد «نزار امیدی» رئیس جمهور عراق برای شرکت در مراسم تشییع رهبر شهید، عازم تهران شده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/farsna/446161" target="_blank">📅 09:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446160">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a23fccfdd1.mp4?token=NP-mq0uCj8ABqZ6YeN7tke26D5DQiIp8rjN_4EZiqQS2IequqvPDWCXTOFTphLSZHbFnW-C4paFQYAeJWUESPdJq64HpV0TU6bG-leY6Rn-AWIho40he7UbizE2zHNeG0J5yJ61dwkp6oESVknaQ2xVrqEEhsTqrNOPnH5gltYyigM_U8peQpPppxiRv82IAAC7uFuCwi20kTs3JFTT8jqlD_XYp59ALMW1OlMXstNLwsjmmopG353njGqYEC01SZZ-xQOzD7BqbqmhJV-uZNVZbkSe_3sAfCd4MzorE9ntL0n6gLbCZnqq2X-Lp6z22mKuCXv26IOZZ_oRYbva5ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a23fccfdd1.mp4?token=NP-mq0uCj8ABqZ6YeN7tke26D5DQiIp8rjN_4EZiqQS2IequqvPDWCXTOFTphLSZHbFnW-C4paFQYAeJWUESPdJq64HpV0TU6bG-leY6Rn-AWIho40he7UbizE2zHNeG0J5yJ61dwkp6oESVknaQ2xVrqEEhsTqrNOPnH5gltYyigM_U8peQpPppxiRv82IAAC7uFuCwi20kTs3JFTT8jqlD_XYp59ALMW1OlMXstNLwsjmmopG353njGqYEC01SZZ-xQOzD7BqbqmhJV-uZNVZbkSe_3sAfCd4MzorE9ntL0n6gLbCZnqq2X-Lp6z22mKuCXv26IOZZ_oRYbva5ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام جمعی از اعضای جنبش اَمل لبنان به پیکر قائد امت
@Farsna</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/farsna/446160" target="_blank">📅 09:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446159">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bbc863f81.mp4?token=UWDuIHf0jCKHUkKY0NUdE8_z7rktosC7sD97e4rcHHHycisCT9OzngLRJPH66fDaKdN-QyLABo0mGVq-0jwONSIe7LdVG0-0AP0_M-uNVcY1fBoBKDLONU9WCcY7-JBNQGRM2Tb-cxniB0lMHTvpE-VPYicwJKb7ugeZc3ykI5WCDi6pa4B0Yo7ocncWCzqDSxJx9DOU13su7S9pJtATqo5m1_YfD-HYmaWE1CvgEqGdafOc38VjwdMA-F1T0j_pZ7TI0jw6ka4PIWedXjErd4cxcQOtVQ5zWMbg-dfa8AIK1Z9I2qwSTf9HXR4L3erHZFTSE25M-z8GorxeVhGEZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bbc863f81.mp4?token=UWDuIHf0jCKHUkKY0NUdE8_z7rktosC7sD97e4rcHHHycisCT9OzngLRJPH66fDaKdN-QyLABo0mGVq-0jwONSIe7LdVG0-0AP0_M-uNVcY1fBoBKDLONU9WCcY7-JBNQGRM2Tb-cxniB0lMHTvpE-VPYicwJKb7ugeZc3ykI5WCDi6pa4B0Yo7ocncWCzqDSxJx9DOU13su7S9pJtATqo5m1_YfD-HYmaWE1CvgEqGdafOc38VjwdMA-F1T0j_pZ7TI0jw6ka4PIWedXjErd4cxcQOtVQ5zWMbg-dfa8AIK1Z9I2qwSTf9HXR4L3erHZFTSE25M-z8GorxeVhGEZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور استانداران نجف و کربلا و شخصیت‌های مجاهد عراق در مراسم وداع با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/farsna/446159" target="_blank">📅 09:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446158">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb955c9ba1.mp4?token=nKy0LpSMy3Wok20HoEXeyFp_4nHujuZyBejHEF0zcEV0EE2O0YhBf0BMbfagGE85tUU-tKYvk0dXUhJHPIr2Yp315Iou8AVrB_WqA7xkc6DZtjF1D9F5DTPFoG3sZE2hroT-5mYPdZYuAdXO0d7_8elxWLYa1IgcaPEvSK4TJ-QVbyBZXtoxviCyUQxoXs8RqBaNFPUT9Vr6KbPUHoHKQOIDAHY2CWwzIsS5NizY9gNFc-YErOB21LBvfSvSMgLBm0-z0qf8KGd4oUaSDE0dsXihhoPgChpSOeDQvOfbXjKzoojG3RQLaE-dCJ8RvH_3tE2cvfZ8jb8MG_vzsXBS4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb955c9ba1.mp4?token=nKy0LpSMy3Wok20HoEXeyFp_4nHujuZyBejHEF0zcEV0EE2O0YhBf0BMbfagGE85tUU-tKYvk0dXUhJHPIr2Yp315Iou8AVrB_WqA7xkc6DZtjF1D9F5DTPFoG3sZE2hroT-5mYPdZYuAdXO0d7_8elxWLYa1IgcaPEvSK4TJ-QVbyBZXtoxviCyUQxoXs8RqBaNFPUT9Vr6KbPUHoHKQOIDAHY2CWwzIsS5NizY9gNFc-YErOB21LBvfSvSMgLBm0-z0qf8KGd4oUaSDE0dsXihhoPgChpSOeDQvOfbXjKzoojG3RQLaE-dCJ8RvH_3tE2cvfZ8jb8MG_vzsXBS4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام جمعی از شخصیت‌های حشدالشعبی عراق به پیکر مطهر رهبر شهید  @Farsna</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/farsna/446158" target="_blank">📅 09:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446157">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f418014f0.mp4?token=A10pbiKD-RWh4XxXdsPZ5CXbfRTnRZSj0-qPzRZ7eO4J9MvmexUkuJjo_A5KBcpHQbyxCBBBPgvzV6c3NW-zacLNZu2iYj3l1I0i9RnuYGtiUIEd-WQx6tfzQL00RGl6EQYy0gDGBenu6lpPcqPElhH6j-6xTnE-Ghhy8g6R-GEdeKsQa5WIPHF0fXgZqKo9ag-oCMuirg8WnfPeVZqqd-50m2I-nfFSm1o-cofCZvTZRZPPizDJFPAd4ybry3iuY-SeEFMB13g7YtQB8YD_RB1EKNUpZ9_qFfQHJAtbZjmsFQCD5f26a83WUoCrZoU6TDO5ffUN-fn6y8n6p5PTbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f418014f0.mp4?token=A10pbiKD-RWh4XxXdsPZ5CXbfRTnRZSj0-qPzRZ7eO4J9MvmexUkuJjo_A5KBcpHQbyxCBBBPgvzV6c3NW-zacLNZu2iYj3l1I0i9RnuYGtiUIEd-WQx6tfzQL00RGl6EQYy0gDGBenu6lpPcqPElhH6j-6xTnE-Ghhy8g6R-GEdeKsQa5WIPHF0fXgZqKo9ag-oCMuirg8WnfPeVZqqd-50m2I-nfFSm1o-cofCZvTZRZPPizDJFPAd4ybry3iuY-SeEFMB13g7YtQB8YD_RB1EKNUpZ9_qFfQHJAtbZjmsFQCD5f26a83WUoCrZoU6TDO5ffUN-fn6y8n6p5PTbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام جمعی از شخصیت‌های حشدالشعبی عراق به پیکر مطهر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/farsna/446157" target="_blank">📅 09:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446156">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ba0a3539.mp4?token=Q95d3qOKbGZQLMYAGqzlZW5OqBVKjKhO9ub5hCalkYFDq8GyWWneZh61AqVZ6PfqJuWrFOWDdpY1ow6f_UjN9r5qldsyH5SV3eofuhpTjZml_KAHK3zV4fmxtP7x0-TI3LvtJy5mpKNT0zpDNq4J8kh9seI1o6QCSEQZ8MC6KLreBHmwXwlfn38lWgRnZZgFHNJEtM3G2wKAHwk-WrbGYzwQgXApPQUu_8nLic2VBrwywM7Rga6j75y488uDyQU2bhxsR_TvLFvxvrIUhTXLGEkMuTpxpGxnb0-MpH35K4DjUBYz1IomYYAVZCf5iqAvJO_WLYZqcRybKWyylvdNTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ba0a3539.mp4?token=Q95d3qOKbGZQLMYAGqzlZW5OqBVKjKhO9ub5hCalkYFDq8GyWWneZh61AqVZ6PfqJuWrFOWDdpY1ow6f_UjN9r5qldsyH5SV3eofuhpTjZml_KAHK3zV4fmxtP7x0-TI3LvtJy5mpKNT0zpDNq4J8kh9seI1o6QCSEQZ8MC6KLreBHmwXwlfn38lWgRnZZgFHNJEtM3G2wKAHwk-WrbGYzwQgXApPQUu_8nLic2VBrwywM7Rga6j75y488uDyQU2bhxsR_TvLFvxvrIUhTXLGEkMuTpxpGxnb0-MpH35K4DjUBYz1IomYYAVZCf5iqAvJO_WLYZqcRybKWyylvdNTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع جمعی از شخصیت‌های جبههٔ مقاومت عراق با قائد امت
@Farsna</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/farsna/446156" target="_blank">📅 09:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446155">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1fc62f1ca.mp4?token=NdV0C8kXdugNuxUdTr1iZY0NuDEnq7Tg7AzFpR0ABY3a9BBXuh5ZmJECRBAFBkcpGfPfRqJRLVilWC9Cs766pOBbmAzusukzepvebVVIvweZvvSuL-JeY2YqAPkrRTavm9N-sKp2PoDe1Eo8nv3sP88cxdtLXptca6FfIQxnzs8AKJdimBdij9VIakvTNYbrYrAEG-FevREt5feYh2EdnGKDCK49TG6iESkm0To4I-xrpnXk_eXHtrKsI7e94BWnj4YUgwa7snHBqkIfeIFh7J_YsT2HHdtCJGXC4HOqNBXrq61PeafcP0uuEtHBfITzOBZ606E-U68VPn5OnEE2xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1fc62f1ca.mp4?token=NdV0C8kXdugNuxUdTr1iZY0NuDEnq7Tg7AzFpR0ABY3a9BBXuh5ZmJECRBAFBkcpGfPfRqJRLVilWC9Cs766pOBbmAzusukzepvebVVIvweZvvSuL-JeY2YqAPkrRTavm9N-sKp2PoDe1Eo8nv3sP88cxdtLXptca6FfIQxnzs8AKJdimBdij9VIakvTNYbrYrAEG-FevREt5feYh2EdnGKDCK49TG6iESkm0To4I-xrpnXk_eXHtrKsI7e94BWnj4YUgwa7snHBqkIfeIFh7J_YsT2HHdtCJGXC4HOqNBXrq61PeafcP0uuEtHBfITzOBZ606E-U68VPn5OnEE2xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سال‌ها آرزوی شهادت؛ سرانجام اجابت شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farsna/446155" target="_blank">📅 09:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446154">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54672fa8d3.mp4?token=CNgkCG63wz1igVkl0SWQP5lr1noVkvyOPuOfmEn7btrNcUOsLss4GI4JwyNQb_Wlc0VuMJi7Y1ljAMh_yXwsbhUhtCRrOT58eHN3YZAVFb8HV1eiK62IGjk6Ce0BLY4Tp2PkGcw5r9qXuvh-mgjeqT1pnXChJPor_BiqL9b2cB9QS-ai0WxSYy1ZAXHZXCzKDE5PZ3ZM-kdlEWXhO1P2nLmB5VbAKxYi6KJLNLkAA4PVvA4k55rIX01oq8mfgnB3Ac5RFQ1nq4IQXqhvZSe07IQwzKSvo8aM8T9WG3VHN553roal_S4N1NkOPoCujr7BhvXEdEZLLe2NIocXKcMrqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54672fa8d3.mp4?token=CNgkCG63wz1igVkl0SWQP5lr1noVkvyOPuOfmEn7btrNcUOsLss4GI4JwyNQb_Wlc0VuMJi7Y1ljAMh_yXwsbhUhtCRrOT58eHN3YZAVFb8HV1eiK62IGjk6Ce0BLY4Tp2PkGcw5r9qXuvh-mgjeqT1pnXChJPor_BiqL9b2cB9QS-ai0WxSYy1ZAXHZXCzKDE5PZ3ZM-kdlEWXhO1P2nLmB5VbAKxYi6KJLNLkAA4PVvA4k55rIX01oq8mfgnB3Ac5RFQ1nq4IQXqhvZSe07IQwzKSvo8aM8T9WG3VHN553roal_S4N1NkOPoCujr7BhvXEdEZLLe2NIocXKcMrqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود رئیس اقلیم کردستان عراق به ایران برای شرکت در مراسم تشییع و وداع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/446154" target="_blank">📅 08:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446153">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61ef459c66.mp4?token=PwXsXCuyx3XsgekkIhIXjCIl8muCQ8pvygMp6pnsymeOK94FnshJb5EzcgmXsf6IXhAEFqtSjLKyv079sO67SzLFIQxH2hZX6tfgEs5-4zEy0hF5W4KWCK___5kPi-OnIWlKx8UFvbJqWTbWGhiaysJ3aEsHT1ZYUrR6fHW__8gIbB7NVijJTbwhC9WclaCQ85dgQew8J973yZw-77YMPuZVOvuuymYOjlIgtfYy7KafKPI52AJl-r2W8tIIhXtS7CvwjjWtIUmUcjW-yBuXBvitVBtDiFHEtv-XuNJEeifnCuI3BV7wYugOSji9jihud5163YA1GQN6EdiyrpMdjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61ef459c66.mp4?token=PwXsXCuyx3XsgekkIhIXjCIl8muCQ8pvygMp6pnsymeOK94FnshJb5EzcgmXsf6IXhAEFqtSjLKyv079sO67SzLFIQxH2hZX6tfgEs5-4zEy0hF5W4KWCK___5kPi-OnIWlKx8UFvbJqWTbWGhiaysJ3aEsHT1ZYUrR6fHW__8gIbB7NVijJTbwhC9WclaCQ85dgQew8J973yZw-77YMPuZVOvuuymYOjlIgtfYy7KafKPI52AJl-r2W8tIIhXtS7CvwjjWtIUmUcjW-yBuXBvitVBtDiFHEtv-XuNJEeifnCuI3BV7wYugOSji9jihud5163YA1GQN6EdiyrpMdjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود نخست‌وزیر ارمنستان به تهران برای شرکت در مراسم وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/446153" target="_blank">📅 08:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446152">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/821f8a1804.mp4?token=ZsJ_azUBCG_FW2kNgooWCClUeTskn6CKPu7J-mq4and2r55UnV9LHaTEGan01ADkK0s2rczTCg7DExTIs-sPlJ2Ah0sakrM72wlNllT85M0sdZTNcjqeBNgGlkgX4nG88NdajuY66_v_ReF6zqEgO2OI_hyLVsarJKr_KQiCIgSkf_zW2e5ien1lNdNuC4z8MJG-F-MHW2NICyxhNEBs_jQ_wIXGVwKT8jdLBXv2oLOrpkwPJe5gG9ug-aBFu6HvTNHgg8S9pZwYZ2xQDyF9W23VKUPJyPhfDoaOPJWNFd2Q0XopnmmalpqUFwoJOJjCyfabt5s1D2cr_mnonM2Enw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/821f8a1804.mp4?token=ZsJ_azUBCG_FW2kNgooWCClUeTskn6CKPu7J-mq4and2r55UnV9LHaTEGan01ADkK0s2rczTCg7DExTIs-sPlJ2Ah0sakrM72wlNllT85M0sdZTNcjqeBNgGlkgX4nG88NdajuY66_v_ReF6zqEgO2OI_hyLVsarJKr_KQiCIgSkf_zW2e5ien1lNdNuC4z8MJG-F-MHW2NICyxhNEBs_jQ_wIXGVwKT8jdLBXv2oLOrpkwPJe5gG9ug-aBFu6HvTNHgg8S9pZwYZ2xQDyF9W23VKUPJyPhfDoaOPJWNFd2Q0XopnmmalpqUFwoJOJjCyfabt5s1D2cr_mnonM2Enw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام گروهی از مجاهدان و شخصیت‌های کتائب حزب‌الله عراق به پیکر رهبر شهید
‌
@Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/446152" target="_blank">📅 08:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446151">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fa1aa9d3c.mp4?token=i7ds1Th2C0dP0LNgyxProzjLOMcHbj3Uaor7pR8o4VMYSaOHPSf80lAhmfTLOCoUS6BDbJOWW6gMGaTB3dD9y6aC-E3kSXAzD3yl-qdrXgQeAf_BD4IQ9Jwjm4PxwX-5jvf3_jdQ9U3ZaLMRGgL6MisLtgtE7X4hbs3W8Uo1rjH5g8uEh_bOtYkdZd76A3FUGAj0PjGH-rHjK5QrPMFx6Z18MVavI0SEkvcQkHIhyE3mAURPRBixMOybU5MzK7c7_Y2jisBsn_xbeSB1R2H6B1X-tg1tErCtMqHaT_z_zYew_mFjyhqNtEUO-eRx0v3EjEACEIVIAnvgYZnoTaUCBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fa1aa9d3c.mp4?token=i7ds1Th2C0dP0LNgyxProzjLOMcHbj3Uaor7pR8o4VMYSaOHPSf80lAhmfTLOCoUS6BDbJOWW6gMGaTB3dD9y6aC-E3kSXAzD3yl-qdrXgQeAf_BD4IQ9Jwjm4PxwX-5jvf3_jdQ9U3ZaLMRGgL6MisLtgtE7X4hbs3W8Uo1rjH5g8uEh_bOtYkdZd76A3FUGAj0PjGH-rHjK5QrPMFx6Z18MVavI0SEkvcQkHIhyE3mAURPRBixMOybU5MzK7c7_Y2jisBsn_xbeSB1R2H6B1X-tg1tErCtMqHaT_z_zYew_mFjyhqNtEUO-eRx0v3EjEACEIVIAnvgYZnoTaUCBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام هیئت‌های خارجی به قائد شهید امت
@Farsna</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/446151" target="_blank">📅 08:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446144">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7_hyo-1FHyOhwZDdH3l3g0mCtrU0wlBJaNDyQJQZNKAa097B6_a3WwBRsF2nGkNY-HgFJBbvCaaJE4_a__6qD01swQrtH_NCeU7JGMfkHmtlo95iYbVa_d0Qjqad7hGHNhihkNM-vZgSyad8Wp16MfmK42hTdLP0DlQsrnlkdIchGEdYnRFbx-7zKlmHGHPlAdm_TIR9omHGCpbGEE8GHvd1MZXsbkbDUCCnPhPZlgNAZNafAsTpBiM6AlFXYXV0Ztwh86KHg0t3pRS6oMbc2tnQ60SP2nPyrY7EVZWV4QhQHWpX4ZpJvFvZFsRuD5_wwmp3nqfTq3elQlOWWFIsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c7L5rymx1j8iIJ5OxLpxu-Or1VpJjpMrJfHhTAd5J62lPJlrIBL5WKfkPAYYdxhP3dfk84jSnCFBYQhuxUaVf803fJK24tqbdb1XadvFRh3Kq6vK5jfuWR1SccfPJxq2BvfmLrMX7aNXXXV6LDDS1-k0ba4BvaCe5TnRrsIU4d7VnhwC3csIA93cZB2XC1OpCGsCRqeEF40bkQ6fwPk-QhWunENpwQ5sXz-P49KU3x065A5TZa883dUj2HyX06LnrPX3V3D_GwCYhu69AQKgkWcxwdSZfWyDTGv0zpfzTdCTR98OmQa06vi3HtEdCG9JdSm5g7lPGx6bYVRQ1iZE0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cS3OQf3O6mfXSymY0guYOhnaJ-QW7droAxL_Yo6oQEYIpEZXbZbMrV8ZkbkIFcqwmf12HMUwyL8TVS8JSCCo6hYrfukC4HSo_AVoTYqPENg6vYFu42A0BxilCUqXbn2R3NBS83NoQt8y5GLSsV3ETKW3v0erVeenmeB0MTT4-ASnn1851d8T_bZK2N5KprkaQ5R82dzeLzuMfX-FvyK9MoLK3SGWgxFd_sW_IItWioo6MQJ-6jHORpM4qfLNaUjtQa0yorEKgaqnhkywROGIcSICn174oYdHvREVEr6PP4xO9ar_KtITwKJYCYpCs9vfjgwaB-4WYCJZNKeL1O6XEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/syO6rqxJywXng2gENn4B1C09dEpNJCqHXp0ijUzrsABvjZkLIXaNRpgjdVlLiQQhJS8xnG01Srq0Hqu4Nlfzq4BYlOjJ-H-EuJChTMhiydPnAN3y5B7hldiNQzwFXkPMo6J8jMehstk2NURdTXlgGBBkeFD64F4UFTm0oleQfInWQWkIYBva2mGzeBgA11HVSeavQJLzplPndDNJA4XMqRTBjl8t8V6gENPPc_4bMFAL8gXQoJnIpUn0vdEZrcbUyjZXVFTnwjhAckCzC4b5qgSTvCwC99XYy6s9O_lYTsGpimk37QJogv0jZZLmhGrhcfU5AQTkDBwumS_Fsn5MvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l6LSXLYlCcpehggQ_4T5YVa9SYQqeW4ZXxouxg15TCgCUsuXr1ip7vDBNxKovNEvfXlRTbxe0ayyAKKOMj27TfHg4SlvUceFJlco0UUVVt51ERI8HwyJlR1JFAZe7DVz4fb58jAQyRYIXe3qEcDfW8OmkJuCBnblMI8151l_-IjKMkDzF5dRtKSa9Zlc2b1DFKVG_n3CQ8_N34__CCoJ2YnXloAt8T3yvzkKV9KrUVJStrrfkLDRK3FSpuLLrmdetrUB8GxcijwtZ0y-FlhLKIQSc20NuQx61hjs8h_00nijd5aXeAP5RH7QkbQrlEPpHZHdH58QZrqGNM417HFOXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ax7P7r7hqyPi9o_I3fy23C8LQPDruXKDFrVrw5vPnOsRGvca4ERkmlUW8469pYd4MAjEJ0VicfIY03Ibku0uRg-UBSJFW9Dzy3moHVnGn7q6g6unpcXT3wzuGPMJf1T-XAyO09cTk3JFDIu8pDEGi0BEh_PYwuN624ljGq6fuaake2RCscbvPRt6iv5VcqpOu11yVkPjhp-bCqeuimUXbeYuZyYTl0FeDATQskrgs3aDzE3HHyUMZNmCNF1gUJwcFDIiJ9OU2FRtQ5YiSVnu9KTto8I8yit18Z0Bv-aZqPfk0RBEj8U1nUbwbUEpxfzbKzKdTt2xO2nK3r7yr-DEEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MzjCh5dxhGpmAhHTdTCEAONt4bg9DacBo_YLiITYLejPTUqRnJjrieT2gWCBBlqS8aQqeyUxY0M72az37_Y3YAgrmMU9hdMHwYboTFWKAfhO15DUJAnWfRr4-mCFN6K80XjBi2sXQG_3gQ1ZajplEYYy8Jmxa12TyL2tWAZc6mfB5xubD39DUYR4EWqrcqBENiniVUaLNoHVdzAI7S_Z9Eq7IJHOcWsDCHqMk5JEsiMDqOH3kMNk-Jh3bcZJ6zi8o8N7xuFQW_T8ar1s3BN_XQzWharY5knl24sk-diYWa0kL4sq73LxNbKN-0XYj5zMVOSm-0ZsernVcYTscoiG3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ادای احترام علما و فرهیختگان جهان به پیکر رهبر شهید
عکس:
زینب حمزه لویی
@Farsna</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/446144" target="_blank">📅 08:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446143">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gadBHjqfQi74ZkLje6xiXPEw7mDWHIL4u0RoLvJp1XdMfs94IVxvYXnHqCVO1zZ9ftNmFsjt-Yr8QSkOuVU77D6K-KPzkiPZWClKoIVNhgltjItXnW1l-4AvVxqP6l2So7DPNhFnq8y-aDzCKzehx7fNsdxyO4gq9ijEloqFN7TBu_lKqOxST4JO-LqfT0Bgu70a57QWtsaGpCdAHho0CsRAKwns9JPkTN9Mo4gOE8pLkAX8igr1D8wIKqt9NYOfNAb_bMdr3OMVw1RikCDsYdAZqo7Ef0UefZRzy2aebzJe6rMhvId_c7_0X6meUjh0c0GkZqt1xXgTgyvPVoGBjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: شهادت رهبر عظیم‌الشأن ایران، اندوهی عمیق بر دل آحاد ملت ما، امت اسلامی و همه آزادگان جهان نشاند.
‌
@Farsna</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/446143" target="_blank">📅 08:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446142">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b5c42b261.mp4?token=N9xsKGnOuLVheLMSNSCxEglETIHQ9zEXcxtecoa72MdEv6okpHIwWqwD9fVe1KKyVrZhonihY4WGPrlWCs4p98SY9c6CWVQQCc9IHTV4hpiYmWF0wp7wEumQwEbExjZQpjyZFoMGbFw9f0aRBEeVzqplHPQKuhisb5VBySRxqGTbeJiZx8SBDpdOyz0HnBecEZxFt-uefR8j6qznAeXVGysnpj5pjtVxsx9tPNaQeBeG3ISs5LggbH2ohQZPFpLUhqQc5yypwDZthO8FjiuY9ZJvUrX5bPX1O7PLN--bRaOenIrMwnrsajWKC7b2rpRBpW7cOpF7NuAqsHOedzWHmEx_531jnJerjQaiJDBeEZG32YsToY9Xu9xz2PRf3eDh2BCNsDbsr6X7JCdti9sqFp5ijLpydg0e9qvmswGMG7XJgMCZgg92S1VSG1gSw7jgEoeZjCz_JxIuyMRgYdOm9vr1AN4D0QmcgDQWK52Ar9PlE-F3TfJFz3eOfyAyuJEgkU7nVehhHOpk1rWzBduTorZAoLxaxegeospwvH0Cm89IQhe0SG-ViLmdDrlbFogqgPn4CicY4gKVFsIFtNZqFYr-krDzhvJq5VV_Yi0CfkF2K3P9nbElIS20MQfhQIL2somYxkb5O-Og87phx_A9WDZzl-PIKg6r-DaBzEjaY6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b5c42b261.mp4?token=N9xsKGnOuLVheLMSNSCxEglETIHQ9zEXcxtecoa72MdEv6okpHIwWqwD9fVe1KKyVrZhonihY4WGPrlWCs4p98SY9c6CWVQQCc9IHTV4hpiYmWF0wp7wEumQwEbExjZQpjyZFoMGbFw9f0aRBEeVzqplHPQKuhisb5VBySRxqGTbeJiZx8SBDpdOyz0HnBecEZxFt-uefR8j6qznAeXVGysnpj5pjtVxsx9tPNaQeBeG3ISs5LggbH2ohQZPFpLUhqQc5yypwDZthO8FjiuY9ZJvUrX5bPX1O7PLN--bRaOenIrMwnrsajWKC7b2rpRBpW7cOpF7NuAqsHOedzWHmEx_531jnJerjQaiJDBeEZG32YsToY9Xu9xz2PRf3eDh2BCNsDbsr6X7JCdti9sqFp5ijLpydg0e9qvmswGMG7XJgMCZgg92S1VSG1gSw7jgEoeZjCz_JxIuyMRgYdOm9vr1AN4D0QmcgDQWK52Ar9PlE-F3TfJFz3eOfyAyuJEgkU7nVehhHOpk1rWzBduTorZAoLxaxegeospwvH0Cm89IQhe0SG-ViLmdDrlbFogqgPn4CicY4gKVFsIFtNZqFYr-krDzhvJq5VV_Yi0CfkF2K3P9nbElIS20MQfhQIL2somYxkb5O-Og87phx_A9WDZzl-PIKg6r-DaBzEjaY6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام گروهی از فضلا، اندیشمندان و چهره‌های اثرگذار جهان اسلام از کشورهای مالزی، لبنان، افغانستان، نروژ، پاکستان، روسیه، تونس سنگال، هند و مکزیک پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/446142" target="_blank">📅 08:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446141">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2fcb14972.mp4?token=K9v66Rw9vVsskh0eAl2OX4Xvjsq-Tvyr0SnbnpQ7p9iRc9hHt076koMGtcsl8xF1nziG7rwi4z6cZ2eGMqjbLqpDIyDIchWefFs99yghm87K4aHbED-Dxy-iFPT7dX6EQQy_lEdWSd8hm1gaRvpoTq0iAiPT4G2mXJTXRJJ414eRC2lJDQqy72ufiC2hgLrrl9hshTaRtt3jdTWeUhruVLPuI8ynsY_E1LhA_icft-p_mBOdOpbFFU2WhKgQx46q9aywZWE2PfIgyGT35xcKO_FJND-OwZb6G2qTc5psqJ8DRs9XxVSAdDwj52Go2tAIyQONlzP9-Im9WkxidzUhUTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2fcb14972.mp4?token=K9v66Rw9vVsskh0eAl2OX4Xvjsq-Tvyr0SnbnpQ7p9iRc9hHt076koMGtcsl8xF1nziG7rwi4z6cZ2eGMqjbLqpDIyDIchWefFs99yghm87K4aHbED-Dxy-iFPT7dX6EQQy_lEdWSd8hm1gaRvpoTq0iAiPT4G2mXJTXRJJ414eRC2lJDQqy72ufiC2hgLrrl9hshTaRtt3jdTWeUhruVLPuI8ynsY_E1LhA_icft-p_mBOdOpbFFU2WhKgQx46q9aywZWE2PfIgyGT35xcKO_FJND-OwZb6G2qTc5psqJ8DRs9XxVSAdDwj52Go2tAIyQONlzP9-Im9WkxidzUhUTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود رئیس مجلس عراق به تهران برای وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/farsna/446141" target="_blank">📅 08:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446140">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">زخمی شدن ۳ نظامی صهیونیست در جنوب لبنان
🔹
رادیو ارتش اسرائیل خبر داد سه نظامی صهیونیست در جریان درگیری با حزب‌الله در «بنت جبیل» زخمی شدند.
🔸
این درگیری‌ها در حالی ادامه دارد که دولت غربگرای لبنان به بهانۀ توقف جنگ، با اسرائیل به توافق اولیه دست یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farsna/446140" target="_blank">📅 07:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446139">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/404b549e82.mp4?token=rWMUu_kZ39k7o2O45ODf1xeH7tNqL8qE32EDLlIATybUEU2DVQ64L56j-O48HwuDBoXGFDweAyb5gUdiyLnkM_Kcfr4aj3IlgDxGZB1hevd-oKe4HC2GTbub7McVxt-sXNqXNI4QJPh5uOyiYcjCB-WdKOITDdiEh0xHjcGVM9k-xfxITXGco1-00uoRr0Ar6C2WbqBJShremYUcTR1nZQRAYMJN_0rORBQWHphpSRHuvdcSg8pZX6hcAUb4Z6tw-i_WGWJEhHvt7RGpHXfoQWHlEOEucU6UrmMNNZh_Abgm7zyUkbOmFc4ylCcPY1wYpC21Uj6wpdl4Voqb1793O0Hkanuuh1yI_BpHqmREsrD9bSKXUr17uNSo4EQr2-eQt40fsR-fcpnE_D1Ev6Rg0fZEwvgox--ZyH8-Fqr27dy4Je25J5hhUbtye961HbJdQs5Bnw9r6FzkYGDj7z8wYpjvxeKQykZE3V9fZPZXEH0O5SCAY-o7lQPRmq7HfQTPUB3DwStyKB6-1o6siVCv7EP094GTU39dijTPtUZ4uuaT7eteUQBGMd-bfotmNhTb4JTOJgvK5qxJG9kmvI26IrZZTQONcQhdS9QT6A9P_9KM4zEp4Tgmr5NXpZisD-_K1cH2kEwLc0d7-fz2pSbaVjDMR2bZa42vLfnjBBQODkM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/404b549e82.mp4?token=rWMUu_kZ39k7o2O45ODf1xeH7tNqL8qE32EDLlIATybUEU2DVQ64L56j-O48HwuDBoXGFDweAyb5gUdiyLnkM_Kcfr4aj3IlgDxGZB1hevd-oKe4HC2GTbub7McVxt-sXNqXNI4QJPh5uOyiYcjCB-WdKOITDdiEh0xHjcGVM9k-xfxITXGco1-00uoRr0Ar6C2WbqBJShremYUcTR1nZQRAYMJN_0rORBQWHphpSRHuvdcSg8pZX6hcAUb4Z6tw-i_WGWJEhHvt7RGpHXfoQWHlEOEucU6UrmMNNZh_Abgm7zyUkbOmFc4ylCcPY1wYpC21Uj6wpdl4Voqb1793O0Hkanuuh1yI_BpHqmREsrD9bSKXUr17uNSo4EQr2-eQt40fsR-fcpnE_D1Ev6Rg0fZEwvgox--ZyH8-Fqr27dy4Je25J5hhUbtye961HbJdQs5Bnw9r6FzkYGDj7z8wYpjvxeKQykZE3V9fZPZXEH0O5SCAY-o7lQPRmq7HfQTPUB3DwStyKB6-1o6siVCv7EP094GTU39dijTPtUZ4uuaT7eteUQBGMd-bfotmNhTb4JTOJgvK5qxJG9kmvI26IrZZTQONcQhdS9QT6A9P_9KM4zEp4Tgmr5NXpZisD-_K1cH2kEwLc0d7-fz2pSbaVjDMR2bZa42vLfnjBBQODkM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود مقامات ترکمنستانی به تهران برای وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/446139" target="_blank">📅 07:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446135">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gqnu5AfhfcHVViOldBfpwvISyTz4QoIH0dURhqtIXuay_nVI6Fd5sdDbSVIWbrc0LDHfhS0WEHE__OuP-gdDbYCXVNvweL1T1NaykrqHUCpzWnSe3L7k4MRSN4vkNS5gsCoYleouCldwvJUUUiGrB3-XKaOS1LO1XpHzjj_PVJY-vc8PxFvChSw-8dq_VkxNMKL5X5tJdg9LxrgxF7w-uvq4ihKXwCqz2BXKpKgUWhghGFZFw0IpnJVNOYa5lWUCGNxYF90D_JH3EKqePxUBdrsuEDG4ZkdJkO0e6ML-ewK5ApqXtb6WY0ib90OFSRxRqRXSuhE_CLfzVG_KDXLOkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzPCWk42OqPt07MmI28sjhit6XWqR4UmDtChooU4RUPegaMREKQl8FdB9FKAQYfI8sEubEWjQZe5P0x9Pd55LsfiS1H9QAzi55d-8-Ldq1N-dLG7Fh_rp6K26bzszSfNJ0KlUtdH3IVKD20Itg6RpJdeLW_OBNgaEQNu0S262UP5N3ISlgquJlrh4OXGSjS3Ds6cdS_ahXGrhuVXjDQcF12S4ctZu0vC6FiQrWANC-xDkOyjx6dTja6LOH1qYXk_w-BD7qIFV3ZQexrgag9a4IJk-BnKxMkIYzrXSHf4HyG-fIQ6qPkQvTlt-MTNNSDQZ2fiyQxTIcf7JYKHHt15cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O-97FuZ6YYW7nn7xFE9-CfiVxKVUyG0zollVGn7k9sbyQlOsSUSjBn_-rNavfc-0wRRogSI86DQKSPukZ7Vn_pu1jrgveE1KK2rU1e6_0-JPhGg__Fj_to2EW-t0tB50jDvzrvaawtJbKuEc2TG9OtbryWNuqx4F1WTBAlEV63g6AqP4YQUqwzAaxvsvFjzp94wzNCX2i8LQJSxly0kOYqKoG0Tcu8oPHTCAZMaIK6DozAb0p7Qnb2XyqFhj11tEb1hwwbYlCtj2EvhBUwtGAMTY7NaIIRbyBkwRDHzyioI1BNX0WCxnWEXtvpYXUYyMgi_0XC7iWiZWH8-ITU2OAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pKu6aaeru52WkakikwGwSNXWf8Wn3ZLkQ_xRIhEoQaNKAT-DVzsoGzbhiBxTtJqtm-xqJIrNROHDb8Nx5HYja5pI62vupi9edJVu6suqAu2Bq-AyGL0UGMi3hW3uZXDiq4QE1DTMZtNspWBCLAODBeKIGyajRl9M1NaNbHJZpbHEApjU2tbooB9ZPDLiQoqb6ydpIIJ4id-SCnizDGEK87ZqjYU51i-7AFgoGSp-IxM2SXe2Kt-ryOsFkn3Prd0D9XWaUQOewjhME39fIx_xbxo8SEzPYrTLqOC_4LbO7M4zQxX_NcRMB0ABIIFQ6Mjw6_vuRgA7FCK4djHUenNw0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
برپایی زائرشهر بزرگ مقابل مصلی امام خمینی(ره) در تهران
عکس:
فاطمه‌زهرا اربابی
@Farsna</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/446135" target="_blank">📅 07:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446134">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQ6miQfieaUSKeIqvvMzPl7mcp2OfXx-KjQgZeQ2ePdpnY48yiMvBkuxs7yflToFhMQTqTAr0igoKCinMPUGOrErzosiiksvWN9qyv0SXd6hgDPZjhnaaN4NggCbiizVfzI-GLsK2EMSu_M_iH-ug_Jfli9_eMe-e8jXjZ25T0hF9qWM1V2OJETfnMzk2wf1uPPL8Ko8sH-OdpDpS-7k7buVcXyoS6JsuBfqlLncV11ZmjCyLFF9pMeN7k_R0IaQuRd2gSaVcFM_Js8Pu5oBOXgFWaz0miAcBQKekOaBL5Ty8SDK92V32OPd-zih8bVzKO3Bx90ZDzorEeSqu8y5Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروسی: بازرسان آژانس هنوز به ایران بازنگشته‌اند
🔹
«رافائل گروسی» مدیرکل آژانس بین‌المللی انرژی اتمی بامداد امروز گفت که بازرسان هنوز به تأسیسات هسته‌ای ایران بازنگشته‌اند.
🔹
گروسی در مصاحبه با شبکه «ریانووستی» توضیح داد: «درمورد دسترسی - دقیقاً همان چیزی است که شما پرسیدید. ما هنوز نتوانسته‌ایم به این تأسیسات برگردیم. ما چنین دسترسی‌ای را درخواست کردیم، اما هنوز نتوانسته‌ایم آن را به دست آوریم».
🔹
گروسی سپس اظهار داشت که اطلاعاتی که آژانس اتمی در اختیار دارد، مبتنی بر آخرین کار بازرسی معمول آژانس است که قبل از جنگ ۱۲ روزه در تابستان گذشته انجام شده بود.
🔹
وی همچنین افزود: «یعنی ما دقیقاً می‌دانیم که این مواد کجا بوده و می‌دانیم چه مقدار از آنها وجود داشته است. پس از آن، ما مانند هر کس دیگری، با استفاده از تصاویر ماهواره‌ای و سایر ابزارهای مشابه، اشیاء را زیر نظر گرفتیم. ما هیچ حرکت قابل توجهی را ثبت نکردیم، البته به جز اینکه این تأسیسات به شدت آسیب دیده بودند. دسترسی به برخی از آنها مسدود شده بود».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/446134" target="_blank">📅 07:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446133">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🎥
ادای احترام هیئت فرهیختگان و فعالان فرهنگی رسانه‌ای از کشورهای اسپانیا، برزیل، آرژانتین، کلمبیا، اکوادور، بولیوی و نیکاراگوئه به پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/446133" target="_blank">📅 07:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446132">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f5b54f04.mp4?token=D6m-cEQrobJa0UTjNd0YktLBasddlGRAvOAsUfbg27BVde3f5g0TrZHpDEvpG7-HjFh9CBZI5TSNMa4L_uaaJXq1TyvZ0KlZJbZY0yRnm9sd1qpd9D2tRx1lsqcDABjAblVwX4f0vgJ8AXMsNpbovV4deN4qVtmHfk1dUFvew7pcYdGVWzHYVpZFWY66NvUQTfW4TJq067K9c1cVEdsP-hYtheLS3pOTZHlATVM7RPvAE-xzxiNRy9QyA_NBbPg6D7oa7yTBBR1y-SkGmG9RaS0JgKK1yakTCLU-kcmRYUS-Kl04hMfnHA1jrEi7YOToRP-eH5zUaoJi52A0Sol56A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f5b54f04.mp4?token=D6m-cEQrobJa0UTjNd0YktLBasddlGRAvOAsUfbg27BVde3f5g0TrZHpDEvpG7-HjFh9CBZI5TSNMa4L_uaaJXq1TyvZ0KlZJbZY0yRnm9sd1qpd9D2tRx1lsqcDABjAblVwX4f0vgJ8AXMsNpbovV4deN4qVtmHfk1dUFvew7pcYdGVWzHYVpZFWY66NvUQTfW4TJq067K9c1cVEdsP-hYtheLS3pOTZHlATVM7RPvAE-xzxiNRy9QyA_NBbPg6D7oa7yTBBR1y-SkGmG9RaS0JgKK1yakTCLU-kcmRYUS-Kl04hMfnHA1jrEi7YOToRP-eH5zUaoJi52A0Sol56A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود پیکر مطهر آیت‌الله العظمی خامنه‌ای رهبر شهید انقلاب به مصلی تهران  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/446132" target="_blank">📅 07:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446129">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pH92BRFAj9s-Tcg38Op7BYN6tY1Qmtqb2xON_hpH44Whc989rS58Nw4-eJEasY5AHE8wktt_dfYP06XJcoZc7KrYyUPGtGpWo1z3kqKT-9a3f8Zzb95PyvrS43dx0xk3Oy1eDISTSg4EpuREZZSLNcmPLv4_Zs0EFyPpHu8IiPZ10M3R6NeMpzlGmDYoqWFWvab2xJBF0naoBLgFt_tpgPNXY8JDvMGSRabei6pjd9Z5ov-_JNFBe5L1ruQkuh6TGnMt09GcrqDRB8Hw3o5mNaYI7vcDOH03sJauhJJ7B5Czfs0rQ0cqoJGzB5dW8s3wf-HmUsvaKH4lt8B-x9aNog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HhF90PC-0nFWH4WWTDIRv9vXtmZ87_Uzdi1mm5x6Ns552ayhgn2REZlyjTme6VunuYTZB3HoVgEAXwX0ycH4V8gI1tXUn1l1qwm9q2PmPVap1dB7JLgc4aJio9F4cVePtJ_jvbIdOhj7FstyTjrUBn5uKVPYBgv1-aIyv2nZspLceb49DNaX2VwsOL6RsH5RARFRrXvKbyOOgqP9XQK317tspGWjs6gOGgcnUz5qTMFol-Y_-Tfj1bbAyt8JeN_EC5ibK6L5r1uwrKbrhx-g3kwN8a1eSIn4Ly2Gh7-ZymfS7fRl5cp7h2HssXv30fjCEXSNkvXYF6ztuSdnhmdvMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOATBgF7sz9T5tzw7inwvHZWSX4B7NSN_QE_GzWCBUAosAYOHMT2MfsK0QTY_DK3dTBStUGV8vkLVwuIR-jg3WOtcupd3sTimZU_oGXiqaRjm9otTbVlogE-atJtJOjChhxTN5rnbsy7LYWkXnoBDV4ZbWHiOpVcwJNL0N7Ie4CEVrGy4sao1tQGGc2MQ7uUvPmMsrTqcQDodjhXjo-KFTlnsA_QcIlaBq3dvZMb_xeJNm8eYiuL7tQfU_E5Z2CMuTicg1__yrmjKa6V-IgZFJL4iCbbiNX3Cjp5mJEfEAstGEdOx2J3Pe1OolBeadMTMVULyO5RK1Lvj3aGm5Xjwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اولین تصاویر از محل استقرار پیکر مطهر رهبر شهید انقلاب و خانوادۀ شهیدشان در مصلی تهران
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/446129" target="_blank">📅 07:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446126">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kw89uKjsOoe_izqV0s6Y56Xqhl_pixvLr8vHlemTiiPf3RE9B6UD_C9i8VD2-xjPI59-O_Lq4RHJYNWV9_zJQhn1Ga4rcad_xwMZlSf6bEIA0Wo0Jj8p4-MrHn5DBPFUDka2YcH3GQ29rApM2jnhSZbvDLqmJ2VoeWsMN5sKiPezrI8tAHSPIkupofiLLs3oEYPQ_lI4UuwtOrA5i7gai50Shwzmw9Xap6cdlkNSgvHkgBqLDnBBgLoT3e42UaV-oLLgybg1jLV_eX6zW04zAspUj4lkRt4ygF8F1xPMfzCktaDRFpFgmF55BSJGJgb13jfp0aKhOyrKzH31BI5szg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tOnmfd-PDzhma1ThT2Q6mZgXXq-YAWo1ZWT2KNeybtQaTZdsEdGX5bJjMnD7IZmgP2heshWN6rFZGG9Ep0yubxotnljQXzVfk1LLGH93WpTo_mirLb4MObeHK4DWc6dHoVb8Gki99ZLSvGkYBNyPSXOmFth0G20BrHB8ODZHFIQSGxrW2Evdk8Fhvv51MYrp78erNvZycGhn9Li9ufCFQCYN6cWPjpCVuNQpP2Yd2CSbDGr8rABNc-3DR-F7OAxuhlspQTFa53dVpjEaVs22C523D43qrjDjjL3iUgUZ0u97X1uuoM3DtZw7xyQdvcipbt_DT362o3UfxyqoDDJM9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mOP-sA9zzlCr_IHdvX-qkYM9-OMhplTprHlGAx2hT-4TYUwfLVI6aaSp6fLHnJVaLQ_g9xDxXHRA2zKrb-xDQIzXZ97WVqNQ8OLE2vAFQ_2T3VNEUut2p2sPfq-c6-4XgLm60XqGmqmFzL-4AEgBJ8bvYrkV0Pye0RCjR_qQvvx2rVfkCn6qGiz_tdC7NjZkLhKhW0ypxllgsSIiCrHKtrF_9TeV4_4tsQklxYMSFAzNY9VkOZ_d6efcZDQujitRe-nSHpqUmio8FcAVpQsKhNXdm-DBDugmMB_01N7Mt-MRAune10QyxppG2EpfzrwUlFO-ZhFHGEVPY61cmM3HWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آخرین مراحل آماده‌سازی مصلی برای آخرین دیدار
عکس:
زینب خدابخشیان
@Farsna</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/446126" target="_blank">📅 07:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446119">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vD4Sb9zI5GuJxbLVFR_UKRcVqiFxRFn0_jZtgCVu1JRJ1U4vbAmTsS5XNgBCWdE6apbUV3SrZoe52j7hi1DUJ6nljU1csAe83qmose_GTgWwbvG5xi1_6SBHKR64rEe-PB61qwH0ODaD05ciK-OKAmoiOlGfl1_dkawdAHcBALbL6M3H1cbkF0g4X2xFtL7q07X_h_THpuW1LusSHN-EEClo7C5-i3_AujEfYItChrpB9yq4AtBNYjQpQ2RrMlit83oBpbcQEwxUSBLXAKUJ2uyP0EovKMEq8jgkkxz6Ya7zeqXaLhaHQsAkTIrNYIZwc12JiQGMoyR1LUWRJWHLYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XLWHRa7Sfvfqn-VEktulVWvX7qefo6sSDXRgteewew4UmE2FYTadN4Xo6vt4mW0qXiHrtwY6oJRs_VcRSxllZ9IOB4kJdnzmiqMcNzgowKIBUucPD9Kc4bFmm5sX2MdbJ5NnhN_J7mH3S-nLS2bHnKBFDtd4MounX6-mSll0kEgW85hUW2j1jF2PLimqOZMInma8IKTP6axG2lGxaBRf6DiKX4GLHwCxfO6I0ikvcEmeYSCN-RgL4etY05QxhN1WbIq1Beuv5iOEoInSeAFzGzeDM958-nrUNDV69S4ph8QNaYuVjkw0siujXpaeBM5WJs7G3NGpiBBGtZhc2K2apQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RpAZR2ApgOSXX71FlSjExy3gq5kBjK5uGLR0W-d_dsKKobmyB4lYeh6WN8zZVGKvXSEMq9NVy_H5-epdJub8SbzmPgNgs95VJHimzuYI-dtJ13BAFcoo20O3hkGfJkmptwxysK0WU6gvR9zbvVPn_uSnfWOTsj2HfzvYU0E5fjyAwwlD89jjaxcUbvzVfjwgnXLgCoZF7WHWkXhZ7G2NBu2gx90jW93h4ZV-IMxUBMHiUC4VVLNWAY7oe55BmLfHYnOMDKU11iAUOTGHjMGYSodSYWfzR9K3SwZI0HumRYt0euWDWKcJ807T53hV3X2bbg7j-AuBdJlHWnzBse6g8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZQg2h9Yt7PIozh5Jp-1hrNZ4DmayRvBeXWqShStpp0NRfmh2lTkw5oOXd8nCFuVtcJ6Yc_rMJxUsPdKw4jSSeZ_xke8xeB10kWCnR5jZrhaVWl5iHsBvtLzra2fJL3Ah-6BiedKfLLPDXAMh3V7iGNCsjp0hcr-tAHS1COKx-bFWMg73Z_ekNnfogdK3ni9NEUBacbtk2U-10J-vFjCIe0p5W80FMxQPmywe7KQxHlEk_ddYrVA1DMn-IRGO5ASiZA6PCDRfLyUu4s-0Hmsq_jtcMLQ85eVen7GkTyjH4aaan1u34pge-t3sMhf0movpqzsTgD9vhv1_4jdVdJOA_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L_4Guq1YahqSaCD1hE3wvdiVz32mfaONoUFUs--5QJh4qJoRagtuQXIL7FeKxpqNF0v6473Z2WeQ7IaNIUR5h_xdi4itZHJoZDrQ6KTxwsyCidxhW3TPYFaKQ2KAEh3KFZBXmrP2O141TWhUw1jcB0LiVNN1g817SWAaYLGqIpu1tgjl3Rc7HVOx66tcpXFe2jtZiFqNzW5niffUFgRfGYG5tuq9uB7KMpnht3xYtVPUA6CodH3yd7EL8s8kM5lfPSs07uVkW9K_X-QvqCJyVoHAF8KuAJPwz24S_ulViuIm4jyJ6YiufsWO21RcYpPqFd3cDEGGWTK_9Y5tFPydFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m2FzOLeq126r5WKA3BfIOO5VW3o0WPwUQH_fFnlwHtFFkHdxv4iJWphrSZizA1ISI_mCYdFy3KDh2kqZkqQ0OpGawUxamdxS233GP0eDJnE6sf0omtZ9DhFQs3suz_dXjzGxaU8RKaY9Voy5S2K8h11bxbzFqd7oNE2fZr3miVIiiDyYn7rw3ZdEyUp6RHMrDlj2ANTxHMYkqcpjSxmmHJKZbfh0e15eYbe1tya4-iluK7QJM77VsNykl9XlYoPoaf4UYzwyyLkJhJlbXDikKyu_NaAGe7aGFIibsSmugZQfzKK-K2lE5ccwLS-BCheYHPuHUFPL-tacHHD2zyxWdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OzHRXfAwbre1glwrodcpwZr79PxRAnlHXhi7dCPEYKqCOeV-IToANlVcyXvOo5rQF9ggasJSYMT8B8oSgd0nph23vx-zkqKF-w7Whg-yjUtp6mElEIuOMaquHtcQQb1OuYWHdtt7h4ZluuZ3gAo419DN6AXgpXGpg7bLYxfDuJTZVff7BUYlr5INg6p-DoeNA3iZlWlTrzBGZbtmTjuG_3fMMtWIjBiN_EjMDZaZU4dgnu3zTj59dq7jZQtcRP0N-NQNyyW0fVH3414BfeLId3qKQf5SqLi6Pmduve3YdvSRti3jxEM9zWk-cyX-7wlD9_u8BlpDgqMmQ5gWJQyyIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ادای احترام فرهیختگان و هیئت‌های دینی و شخصیت‌های سیاسی و فرهنگی کشورهای جهان
عکس:
زینب حمزه لویی
@farsimages</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farsna/446119" target="_blank">📅 07:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446111">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/174ae4008d.mp4?token=Hc9-jq_aMIB4kp7hp6OS_KgoplhSFMt8l0L5R7AS-IQIJWyDyZscahnGWvP3F9Qx13RF79cpiD6mijU-lwQlbSrnK3AyJg1T3YPMrNI3NvD6WfaAJzSk-uq33yPbis7PKfuaIkZXzvUis1MeWum1fQpn0TR6rZid41kdNItFTw-XYE1Y3Qq_PyelcQ9aECCEoSAtKzUTTnC07RR0iPrBmOMHKjU0GQA7xgfE_VS-gBYMwlMY4l-vNMnr9IVWA8jRfK2_DjJg0gVCgvxAZof2QQ2lbv7prT_MJI4OnnKPTckT5Nm93C3Psbnmq3pPpDQTkMQJ8TvqHST3nCPoJJDm9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/174ae4008d.mp4?token=Hc9-jq_aMIB4kp7hp6OS_KgoplhSFMt8l0L5R7AS-IQIJWyDyZscahnGWvP3F9Qx13RF79cpiD6mijU-lwQlbSrnK3AyJg1T3YPMrNI3NvD6WfaAJzSk-uq33yPbis7PKfuaIkZXzvUis1MeWum1fQpn0TR6rZid41kdNItFTw-XYE1Y3Qq_PyelcQ9aECCEoSAtKzUTTnC07RR0iPrBmOMHKjU0GQA7xgfE_VS-gBYMwlMY4l-vNMnr9IVWA8jRfK2_DjJg0gVCgvxAZof2QQ2lbv7prT_MJI4OnnKPTckT5Nm93C3Psbnmq3pPpDQTkMQJ8TvqHST3nCPoJJDm9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام ادیان مختلف بر پیکر رهبر مجاهد شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/446111" target="_blank">📅 07:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446110">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64cfa34cf1.mp4?token=jgmY_b_FgcsQjME-nXcrsyGMA1oGp9cquQnbNbfP82Z2IRKBC24ETjE8jdEFqiJkPUfpEhjSWRxMoP9UdAe2HnnlCVC-UbX5PJVTd1CfhLbEWXt4aXvLJ6OOY88SSE3S7ZQPVwUFe1x_9rNM9G2DfngOAiKUHmlZbFj5B7QHys7jpDAcSnOnS3eCJwdqqmpqZgZPF4YLzBtUtarZ9mhHMVh2g-yrxJwLO1DwtzqJ7YLKVyzDHtjGlkMJmeIqwL0E3LEsMzC9fKiXk4kHYRGxtUnrcRXfvShMD3KMkeHIXX7aP33BE-F_RToBykv_uYLZXQc2tR9T2s7ebQtR8sQT3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64cfa34cf1.mp4?token=jgmY_b_FgcsQjME-nXcrsyGMA1oGp9cquQnbNbfP82Z2IRKBC24ETjE8jdEFqiJkPUfpEhjSWRxMoP9UdAe2HnnlCVC-UbX5PJVTd1CfhLbEWXt4aXvLJ6OOY88SSE3S7ZQPVwUFe1x_9rNM9G2DfngOAiKUHmlZbFj5B7QHys7jpDAcSnOnS3eCJwdqqmpqZgZPF4YLzBtUtarZ9mhHMVh2g-yrxJwLO1DwtzqJ7YLKVyzDHtjGlkMJmeIqwL0E3LEsMzC9fKiXk4kHYRGxtUnrcRXfvShMD3KMkeHIXX7aP33BE-F_RToBykv_uYLZXQc2tR9T2s7ebQtR8sQT3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای احترام علما و فرهیختگان مذهبی از اندونزی و افغانستان به پیکر آقای شهید ایران  @Farsna</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/446110" target="_blank">📅 07:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446109">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_N2t_1L3IjsiU3P64NQfOWK7WUJ4HKbQlQYNuDutxcnNRaBWkq_rrOOgzvN4VFTYZSELYtzMS5f_eshNhL2AEb-do1yf35KdhEnn6Lv5DX5rDWabrx9OTlR6hnkU398o08Ye37oOKbRHc1LzQxUUWyd3qS7QdCJpqRXz-UMeSVgP9R2Z2f8JQuYLN-E7dRj9aCvPIGvHw-nVhO0GXQtWPGX3Uq5V6ng2MJbwP6z03NSnPjA07c21s79cv-nxbsS9GAs94OhvE_Gzj7GiB-QDKBMhEYvAVd91-Zvk0YVh05F_eOKM2or5gurezVOal8QFzt00rBV7jGycEp_yw_UDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محمدرضا» خانه را وقف امام حسین کرد؛ مادر، وقف آقای ایران
🔹
چندسال پیش آمد و یک‌راست نشست کنار مادر. سرش را پایین انداخت و گفت: «اگر می‌شود دیگر طبقه پایین را اجاره ندهیم؛ دلم می‌خواهد اینجا را حسینیه کنیم!»
🔹
طبقهٔ پایین خانه‌شان سال‌ها جز عاشقان سیدالشهدا مهمانی به خودش ندید تا امروز که قرار است میزبان دوستداران آقای دیگری باشد؛ یک میزبانی در غیاب صاحبخانه...
🔗
ماجرای این میزبانی عجیب را
اینجا
بخوانید
@farsna</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/446109" target="_blank">📅 07:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446108">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c98e3fc7.mp4?token=I6wuwPa1Bzn-kqvxoR2b9qLqwPP3poR0kYze7mP5buA7bp_BEa16sUrJ8kNO-iH6ueH4xkLMvZyFa13cpR-NQqsl_shpqcywJqVA9todC7asRjeeJqX5g-Cq45A4ODP7cX1NrJOxaf5LiyBGNxHhsy5N8LH_tOsgUZdZERdI0BTOefTz1fWWi1nbAgsgQmmBPz10LntGaph7NqGh7jVZdjpnFcfx5LlHVEep5foSuwyDn2qpVpSRB1RFOaELS7F_1o_sw3bwn5l4ajOwtwdsJLenpU_DMbuYGcN_0k6rGSStTiusQZr2VvrimRyxaqOAQ2QL3n93Wfki6we98C7tzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c98e3fc7.mp4?token=I6wuwPa1Bzn-kqvxoR2b9qLqwPP3poR0kYze7mP5buA7bp_BEa16sUrJ8kNO-iH6ueH4xkLMvZyFa13cpR-NQqsl_shpqcywJqVA9todC7asRjeeJqX5g-Cq45A4ODP7cX1NrJOxaf5LiyBGNxHhsy5N8LH_tOsgUZdZERdI0BTOefTz1fWWi1nbAgsgQmmBPz10LntGaph7NqGh7jVZdjpnFcfx5LlHVEep5foSuwyDn2qpVpSRB1RFOaELS7F_1o_sw3bwn5l4ajOwtwdsJLenpU_DMbuYGcN_0k6rGSStTiusQZr2VvrimRyxaqOAQ2QL3n93Wfki6we98C7tzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود پیکر مطهر آیت‌الله العظمی خامنه‌ای رهبر شهید انقلاب به مصلی تهران  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/446108" target="_blank">📅 06:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446107">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpkwODWFWwuYfir3RkN07uJt-cGcomtGqb60QHjOzU5C4r_PogHkjaJZiek9urP5H1Bkn7F0FAeoHj3Vah2N7GtxZtekg3Ml6lHW5aF_Cvs1KsTSiHCO4SCfausnCSon7GusMaMoD4zjbstOxmuPAw-MXrhF0SXtDRPfFJCZcg3YQXG4FXxCry9aktdzLR4gMqwcQEcfl38EqBRwWd2NVqxiAyZnD-cQdKVwEG59VcnFYARD01rwwfJ9VVD7qWA7LFFL3xjvvDJFysAEm7wEw8Y8GqldVTJT-fhokvFyns65JWeQLhja48fxaGfjNJ4KTMVxHJdtd5-_DDt9xH0IKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران آمادۀ پذیرش ۹۶۰ هزار خودرو شد
🔹
معاون شهردار تهران: با آماده‌سازی بیش از ۸۰ پارکینگ در ۱۴ نقطۀ ورودی پایتخت، تهران آمادۀ پذیرش بیش‌از ۹۶۰ هزار خودرو شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/446107" target="_blank">📅 06:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446105">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219897dc3a.mp4?token=CstJL0Gh5VC8xfp4upYrQJWh-nrRJD64OrPE7l5NY7wfqvAtUNw_BYX6gxbm6YdeKd3T_S8ysTRC6E_iubPMP9T0VkM1KvaV49Yi6RLQtvVV4jrPVEMGB4PpkmUGXQ7Y72Hw_e0iJosNxGgW8iXsNpsa6oJdlaTRY6Ec94NmvjlAYcfvZ7GQo6inT3CRjo81m6EdHmpY0KJdbcp2zg8dfab0bg-iTeuMMuj5Hv_bPnVpz0M35mXdGyBA-WIkRRp1lFIA8N3zPAmkAxN6I_woI7_-jTNHH41qbNAoxOoBjkf0ENCzNsO7FfAXunaLHnOLK5KPGMrlBBHUayE732FlhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219897dc3a.mp4?token=CstJL0Gh5VC8xfp4upYrQJWh-nrRJD64OrPE7l5NY7wfqvAtUNw_BYX6gxbm6YdeKd3T_S8ysTRC6E_iubPMP9T0VkM1KvaV49Yi6RLQtvVV4jrPVEMGB4PpkmUGXQ7Y72Hw_e0iJosNxGgW8iXsNpsa6oJdlaTRY6Ec94NmvjlAYcfvZ7GQo6inT3CRjo81m6EdHmpY0KJdbcp2zg8dfab0bg-iTeuMMuj5Hv_bPnVpz0M35mXdGyBA-WIkRRp1lFIA8N3zPAmkAxN6I_woI7_-jTNHH41qbNAoxOoBjkf0ENCzNsO7FfAXunaLHnOLK5KPGMrlBBHUayE732FlhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود پیکر مطهر
آیت‌الله العظمی خامنه‌ای رهبر شهید انقلاب به مصلی تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/446105" target="_blank">📅 06:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446101">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h8aZGOzLlxTc6wNjZLziHT_E__9fhI02J7ZCBfhG0OnIMvUpun5QUhUBnyUltCsZ2TWbtvoxEWWnQBnEWk5pyN6dcwGtBTIeUxGhHrXn6zOm7TMLRH6vSB17v8cPqsf8YbcIlR5MFAtYwat0dYWgwAG7tRWUjAot-ieM_FHJSLMN0KvVveUgZg2JU4nLgZdXe5iCjfz2nhZPBJ1fKGwBw0j4cKHmkGh5OVmUyyVBd5k7IHUKglMVSupY7SxTcvPXe_xjDbW8Tb2U_WwFzrVu9SOZRQsrAWzxHpSrav9wOiFGvpOKxH0HzjqF2XM04UuSFqdAh715WhomwS7PnD1FwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eru1vNG7MNopzZG44jghXYNN6TStoWxO2xLxo5R8qxrsYLBBBuLxvRBMGyMqKQ1o_MSkFPMKVxaY4gGQrhH80--Ja6n2V6HCStUNXMjGQgR1AglEfw9Uvu3W_-vqKE3HjoGCfin5rVM9X_sCDEZt6yB7xn01J8c97pL4xiaeGIQGaifDx7XdOZMdEMiHAwubcnviXYbfj4B61FXkgz9-IqlBTR03erk2yfwBgFHWedBf40-JGgNS0-4wBfNDJFJoaWhUcA8t_hh7KSNtWtr7fN6nMPqfjynnhq-rfMJAJsSSP4JcTvilR_c1a3qm6PYf5cCZu5gW3HVbVakIKH6b-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NjLMIHNdaLuxcyT_YXJ32f1XG0YxNOPzlWs5oFBScGOwe7D8XawxvH27Ox7kQREnYHNITxvBZdo2R0V8TDxDj9EqFsm0zJAmkbyr3A5gf1sjDsP8wTwY2PSlQ_ZtsKVOc8p1y65nJ2bYhgiLH_mx5YImoh4bvPS-yl7BR80vIZEbuzofm5DQh0VYeA-K9eDgU9H7BN37ZG7gQsgvVNDyYn92PP1unNU1qVw7m4yttCo5tirWWrhgU0TVbKs4VPQIYBT_cIaFv3sEtKYaE1sQLTM6kSSXOifu3v_EjUBa0Mea6VMwzBLaXCUAu83FTC_RYoUKAvHtTv2AM_WWgd086w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U3FYqkpzxaUb5iTVFQ4EQkSXY9BvzBy_Mnbui6WKWwk_ZCxJ3eWrOCUg3N0WuOapyRCRAnNAaPrOya0rmHfhIkhFi6-bWp8hCPwE-Aq101IDmymvXFOh0VRZwh1fErYBPZF6NSsWbknj2OiSwNQaOLb3GvjrEiPxa4NwYtPxJpwU59_m1GjJgmXCXhYXru4oaiZHPzDwsgFzhu13is7uZKlyR3TTMyPNgSQTrWxXWPzKfyZYFTGPhizPSaO-HqXSKfSAJfLlFLm_wXZncYTW67vJ8HYz3d2-KBmL0ypzyqRccowVeF_YuK4MavmJGj9XCLOoPbadHryGNPUmg217Rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تهران آمادۀ آخرین دیدار
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/446101" target="_blank">📅 05:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446100">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37ef94ed2.mp4?token=XyHx3JKoKCut9uUOzwI6JfXmLJUfM3yhGQzJBEuEg57ZZCnbPzpt5PozhImEo6M0YwwwZZABQWtUE1uxYfSXFLKubsJOH-_rkBOAvrtcH4TDUdmB65nbkXzwW3VxQ7apwExBOPINRgO69eCmUHZJMoT8OmZgBmDhPUytDDzfC0Jv8Gcq7bFdLZSc0cJLV92o2u65cdCk6kLQGqYidshU1RP4fZbckeQkb0muLLMWy2jhu7ahQ32RQjwRKhmb9ULYK3x6PIC_VpDXnDy9dt1izv5YgiE3un1WB9I5Ng2KJCtQMxja1o7USdgsx0fvkiKtiQjLv3LywMCp5h4KeYMCgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37ef94ed2.mp4?token=XyHx3JKoKCut9uUOzwI6JfXmLJUfM3yhGQzJBEuEg57ZZCnbPzpt5PozhImEo6M0YwwwZZABQWtUE1uxYfSXFLKubsJOH-_rkBOAvrtcH4TDUdmB65nbkXzwW3VxQ7apwExBOPINRgO69eCmUHZJMoT8OmZgBmDhPUytDDzfC0Jv8Gcq7bFdLZSc0cJLV92o2u65cdCk6kLQGqYidshU1RP4fZbckeQkb0muLLMWy2jhu7ahQ32RQjwRKhmb9ULYK3x6PIC_VpDXnDy9dt1izv5YgiE3un1WB9I5Ng2KJCtQMxja1o7USdgsx0fvkiKtiQjLv3LywMCp5h4KeYMCgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موشکی که با آن ماکان نصیری را هدف گرفتند
@Farsna</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/446100" target="_blank">📅 05:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446099">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یک معترض مقابل مقر سازمان ملل در نیویورک خود را به آتش کشید
🔹
مردی که پرچم تبت را به دور خود پیچیده بود عصر پنجشنبه به وقت واشنگتن در چند متری مقر سازمان ملل متحد در شهر نیویورک اقدام به خودسوزی کرد. این فرد پس از حادثه با وضعیت وخیم و بحرانی به بیمارستان منتقل شده است.
🎥
تصاویر دوربین‌های مداربسته ساختمان سازمان ملل نشان می‌دهد که این مرد حوالی ساعت ۷ عصر، ابتدا پرچم تبت (منطقۀ خودمختاردر غرب چین) را روی پیاده‌رو خیابان پهن کرده و سپس خود را به آتش می‌کشد.
🔹
ماموران امدادی بلافاصله این مرد را به بیمارستان منتقل کردند؛ گزارش‌های پزشکی حاکی از آن است که وی در شرایط وخیم و تحت مراقبت‌های ویژه قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/446099" target="_blank">📅 04:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446098">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIIFa0DIwyBkkk9aBYLZCwphbQre4P4Otuxt2eldA89a9y2FZwvTIjl8jqjIyFZe4-BjbVHr-aL2DTFuWhYJusdhkrfo87dlPSD5MeTVOLCc-uWizAPhHG2xRjdgfht3LJgEFoJfz7rf_xuWN2sUaNQfZR3L-eWf9BWBSnK1ZJIiUv0KeDjAd6kVa1DY3t9btH9FM2m9mDbzn8QvfunjC8QVk_Tj9kelr9zE74ZgPS790Dd5h1yienIgVHHvaXTtObK2IwJjuRUQwu7pfAhNBteYN0OTnnesKcvCy5jjsJUyoAsPEspDi68F1AQRW6cYZuVIxdFEIlu4Nismn3Ai_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان بحث‌برانگیز
خداحافظی تلخ لوکیتا با جام
جانشین رونالدو، او را نجات داد
اسپانیا پرتغال اولین فینال زودرس جام
پرتغال ۲ - ۱ کرواسی
@Sportfars</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/446098" target="_blank">📅 04:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446097">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4vtfePJLqrkNX9hIBv4jFO23ZHXKC52T4Uhsqxif4JeT59fHxgTdM8B0bi4FLMZ1ICUxVxGT_7TanT4kLYT8CNS9FE-lY7drS5AmtKfLI1BlE-AjoY1ui7nCeL2_I6mt7VXGNUpNPWK_SbZRz7-QUBMfJd-530kNJU4HDLbluiws9p8n2A_1cczbod3xq6VA6p6tmF6wx7IaRVlbaMjRoCxpTWg6d6bcjKyH465sSXjFHL8nD1WGEb0o_fzFX0PJRNZz9ADNaRy1QrLh9rnikU6YcuwL3Hsu8ehDpG0WmAO876F-WFiJvjaEix_0saXMJ3B8Zomf29uUL4YHs4pzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران آمادۀ پذیرش ۹۶۰ هزار خودرو شد
🔹
معاون شهردار تهران: با آماده‌سازی بیش از ۸۰ پارکینگ در ۱۴ نقطۀ ورودی پایتخت، تهران آمادۀ پذیرش بیش‌از ۹۶۰ هزار خودرو شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/446097" target="_blank">📅 04:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446096">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIxr4pVjKC4bElUviU8jc9OLWM56U2KDmegMWSzPt36hZ4XAF7F__bXRWVNwhbI5XbrvA27IhWHFWzagNdlDF9SWwe2SOBcAK3vbnFN3UDWulx8MeH4IaDBlmst-7KLe2E0clBfwXDqvM0qw-8N_Q-yKHVUS55HXoxzIh4dnMMMSuIrdL0abAwBI1H2VjFngVD-SMi8VRheTCW29v6BRoBr83-vinNy9evQnB9biEXp6UFzMjUQZCqrdaeZ44vvuF3v-ZWBVbYf_agkisP8IdFdK54pXmzkJJjnIqJyYIP9Rte-Iss1vNxJlpiE-Bf-XK4uAHSms77Axe1ihgn8TTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برج میلاد میزبان زائران می‌شود
🔹
هم‌زمان با برگزاری مراسم وداع و تشییع رهبر شهید و تعطیلی چهارروزۀ پایتخت، برج میلاد از امروز تعطیل خواهد بود.
🔹
براین اساس تا پایان روز پنج‌شنبه ۱۸ تیرماه امکان بازدید از سازۀ اصلی و طبقات گردشگری برج میلاد فراهم نیست و این مجموعه تنها به ارائۀ خدمات برای زائران اختصاص دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/446096" target="_blank">📅 03:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446095">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d01ae807a2.mp4?token=VcDzUN2q3eOjjqqfvtIywy55UhqQAqOTFwOt402zSPdYNHcIFM88AvgkRGG1LuzghXXmnu7G1z11GEohpr06gB1zTMOW48hVeXYRSc4tJmoAYF7Wpa5Y6TzSkzYiA8hRPkkuPx3DwbUofdKXtxXAF4rLAMUoImJVrtcgIBaRoY0LuS6nkfHHquS7cQcCXQ-HVjR8Az7AvebRNQk_WiuBHCviIm3_maYwbV07Wo0oFC1CeUrmlgJFqyIfb_pVpgZmvAYPiilEht8NGoOKfLn3Diprl7-Ft6Nu75kwWZr8srrDTCsOQdaGrbOahZvA1E_FZ18YBp_8TLIiPbkur6_GgxZq8A9Kc9IvckPEFveb1_3sDnApTTqddqyWrcYp-djFu_YZVLyh-nz5Jz4oXC3XkbdTMT-ymH99nrtGSfHIr_tJUInlqJa2eu1bL1LDzt9k9IR36WxMyHV2vlz-MtMBWp6wZMdZP-djpFgHknUzcsNkh4-P3CA_inJ5W2euy5lSAdAc-Rg1_Z8aZgFCKtFnFSgYBdl8uRJH7wmfRKSrMKYEc7aPCxcSv4DIxCHBaDHci3ac_knoVfGBmKuUrmzyrAzZmMa0w7EdIP2Dwi6Fvs71cwPRQhcLICLfYb7CLYzXcNTbe9sU2DWgFqBWZ45xMXeotEHEny2dzNjacAKo1pY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d01ae807a2.mp4?token=VcDzUN2q3eOjjqqfvtIywy55UhqQAqOTFwOt402zSPdYNHcIFM88AvgkRGG1LuzghXXmnu7G1z11GEohpr06gB1zTMOW48hVeXYRSc4tJmoAYF7Wpa5Y6TzSkzYiA8hRPkkuPx3DwbUofdKXtxXAF4rLAMUoImJVrtcgIBaRoY0LuS6nkfHHquS7cQcCXQ-HVjR8Az7AvebRNQk_WiuBHCviIm3_maYwbV07Wo0oFC1CeUrmlgJFqyIfb_pVpgZmvAYPiilEht8NGoOKfLn3Diprl7-Ft6Nu75kwWZr8srrDTCsOQdaGrbOahZvA1E_FZ18YBp_8TLIiPbkur6_GgxZq8A9Kc9IvckPEFveb1_3sDnApTTqddqyWrcYp-djFu_YZVLyh-nz5Jz4oXC3XkbdTMT-ymH99nrtGSfHIr_tJUInlqJa2eu1bL1LDzt9k9IR36WxMyHV2vlz-MtMBWp6wZMdZP-djpFgHknUzcsNkh4-P3CA_inJ5W2euy5lSAdAc-Rg1_Z8aZgFCKtFnFSgYBdl8uRJH7wmfRKSrMKYEc7aPCxcSv4DIxCHBaDHci3ac_knoVfGBmKuUrmzyrAzZmMa0w7EdIP2Dwi6Fvs71cwPRQhcLICLfYb7CLYzXcNTbe9sU2DWgFqBWZ45xMXeotEHEny2dzNjacAKo1pY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ای روضه‌دار قدیمی
دیدار ما به قیامت
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/446095" target="_blank">📅 03:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446094">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48e889c2ef.mp4?token=gOABR8GIBPkNeqfDK9sTJNZ4NFIvxHfcUEvGWgqMSS7CWI5hsWYLllsIGFcBzFob9mBGZ5nkwycOLFcEm96Fho1EglXfS6Mru-LhLX2u13etNPOUia0rhxlYjQ3BqF3xMTzgjgKYGZ-xgZwAcq2Sm_b2ZAtDennFy09iRM19Fr7-FoNFOsHhoj6S75HM1vzH2Fld_9V_XC7nuAwj0ohptu27BR4xZfpgEX76N6_MhjJ0AhlqEf6LA1Cp1T4Z4w_Edos6jGDpS0W6KUW-LLCSW2cf8KkTsh2-NAwVRUi5A_nBoUIVnN5SQWVW0-qjQj56zbh_Og0xM1uhRQ1iGCGlFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48e889c2ef.mp4?token=gOABR8GIBPkNeqfDK9sTJNZ4NFIvxHfcUEvGWgqMSS7CWI5hsWYLllsIGFcBzFob9mBGZ5nkwycOLFcEm96Fho1EglXfS6Mru-LhLX2u13etNPOUia0rhxlYjQ3BqF3xMTzgjgKYGZ-xgZwAcq2Sm_b2ZAtDennFy09iRM19Fr7-FoNFOsHhoj6S75HM1vzH2Fld_9V_XC7nuAwj0ohptu27BR4xZfpgEX76N6_MhjJ0AhlqEf6LA1Cp1T4Z4w_Edos6jGDpS0W6KUW-LLCSW2cf8KkTsh2-NAwVRUi5A_nBoUIVnN5SQWVW0-qjQj56zbh_Og0xM1uhRQ1iGCGlFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع خبری از حملات رژیم صهیونیستی به شهر صدیقین منطقۀ صور، در جنوب لبنان خبر دادند.   @Farsna</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/446094" target="_blank">📅 03:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446093">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIedkx84TxUxDjndiIIX-Sb1wiH88s0WvEpIr1kM092vhSke4MFg1umQVXAojYWNYo7Y77KbVjwSgCPoXfncgNN8m0RR0loKHpIpOW_PNhY1VDGMGtKsHrhFbUJmTLl1rN4PYq_J7emUh6fAw26SlKGTqfiYBcH5euQ3FMySbpEncrrQf835CrmRBEwUsLdgE-u2S1H2X2t00ifgPSrSczl7f-K9Ry4yw1vWGaOUNGuQA-rMqc_Iwz9gpY98Mjtzt61Y7_whTKsl3gaMgDIJmdp26BP8YESRKB6GsvTH0xNjU1N3Rx0n7poAJIRByo6FjHW8ZZBXbx1gnHW1JSIcgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پرچم مقدس حرم امام حسین(ع) بر روی پیکر مطهر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/446093" target="_blank">📅 02:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446092">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11549bf726.mp4?token=JAswVRaw6iwbJv43GXHuFoeiBuSu5IT3godSYHzsStBgovnVQGJB2xT4k4qBQLbL4d1b6_Ovhb7sJi-LTIKzteAigcQmvrnp09kecvPtfSC0ErmYmSmlLvQkbu4Ex7SXXvJhCKyNM9mGJgU8y3pHjdnib3UgQUFD9VIDqO_9bFOZj9WB8DHDQOqUFre8NPLZbaZUBybD6hkJr8Jg0rjmZeyI_mxDlezZzCSQv8Mjr4zCbJaUN6EObvjKcLXegp8zcBabaoWeAxqTj0yjiWwjRZXNxiYCYO18OJGbg1jbUde_thMTui3xeRfQLsPL3pgnQ1DUL_OhhfMKc9ETMzX_wmn7ca9MxVO3z93CHqUwVfhyNiJDrdvBcxYKZwQ2Akftsc9GFO31EtWmBaSg9wkrzXekfL9FVGGVpXqtG4dgVkcenD01D6_HYwmfAU123MkczmgWAzCUIEsXEYWx-yyvltmbXHLU_PjrBXGw73ceQ4NVgd2-VTxS8ZH8qd7B3SbetXyMaLk_uHFC-nGQ8mBeHFOzBq-Hq5x_y46GdnxeDOKM4VH6XgoTzDC-9oZZ9icbHOrUCu91XXjSZBDOIIDXr9D_Ii381OzH4oodq0fxdDXkp4IATKY99BFAswDCZXOVPZib4tYFHVrIszLOZqpHpFhalkMwGV9_SAjOYTTLsaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11549bf726.mp4?token=JAswVRaw6iwbJv43GXHuFoeiBuSu5IT3godSYHzsStBgovnVQGJB2xT4k4qBQLbL4d1b6_Ovhb7sJi-LTIKzteAigcQmvrnp09kecvPtfSC0ErmYmSmlLvQkbu4Ex7SXXvJhCKyNM9mGJgU8y3pHjdnib3UgQUFD9VIDqO_9bFOZj9WB8DHDQOqUFre8NPLZbaZUBybD6hkJr8Jg0rjmZeyI_mxDlezZzCSQv8Mjr4zCbJaUN6EObvjKcLXegp8zcBabaoWeAxqTj0yjiWwjRZXNxiYCYO18OJGbg1jbUde_thMTui3xeRfQLsPL3pgnQ1DUL_OhhfMKc9ETMzX_wmn7ca9MxVO3z93CHqUwVfhyNiJDrdvBcxYKZwQ2Akftsc9GFO31EtWmBaSg9wkrzXekfL9FVGGVpXqtG4dgVkcenD01D6_HYwmfAU123MkczmgWAzCUIEsXEYWx-yyvltmbXHLU_PjrBXGw73ceQ4NVgd2-VTxS8ZH8qd7B3SbetXyMaLk_uHFC-nGQ8mBeHFOzBq-Hq5x_y46GdnxeDOKM4VH6XgoTzDC-9oZZ9icbHOrUCu91XXjSZBDOIIDXr9D_Ii381OzH4oodq0fxdDXkp4IATKY99BFAswDCZXOVPZib4tYFHVrIszLOZqpHpFhalkMwGV9_SAjOYTTLsaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دعوتید به دیدار؛ این‌بار برای وداع...
◾️
نماهنگی از ادوار مختلف حضور رهبر شهید انقلاب در مصلی تهران، و اینک دعوت برای وداع با پیکر مطهر آقای ایران
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/446092" target="_blank">📅 02:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446091">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حمل‌ونقل عمومی قم در ایام بدرقۀ رهبر شهید رایگان شد
🔹
شهردار قم: همزمان با برگزاری آیین بدرقۀ رهبر شهید، استفاده از ناوگان اتوبوسرانی شهری در روزهای ۱۵، ۱۶ و ۱۷ تیرماه رایگان خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/446091" target="_blank">📅 02:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446090">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
منابع خبری از حملات رژیم صهیونیستی به شهر صدیقین منطقۀ صور، در جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/446090" target="_blank">📅 02:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446089">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05260e76fa.mp4?token=DIVMRYn3YsxHb-I0cgggKoy8b5Aai5jVPUMXM7jQJo17oPTkkHZmqnYfqcxCnkQgXmh7BnNitrvvvduOT3IWeVQ7y-ymyq0CNPJ_z2OnNQ9vq9OhCtj4GySZIxL3bGN4NwO4GIRgIjESWz9KSNhlVg9rYAZG2nTaaByMCCmOr9xlmjoOE8ZOFnx3DKnQWkzsF06G8QHGiU5-An41bsg49IS0xQd44bwi1DI5MP-wT2aP5caXe3EOps7iOufGIoAEZnim_qLx8Wjd_PxnsV5-VDwdzmvrEMWxpE1It5iaBQX3fhJESfZZhQ5oAKrCBCvhSPGxzlRGLLPzKjhezUdsVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05260e76fa.mp4?token=DIVMRYn3YsxHb-I0cgggKoy8b5Aai5jVPUMXM7jQJo17oPTkkHZmqnYfqcxCnkQgXmh7BnNitrvvvduOT3IWeVQ7y-ymyq0CNPJ_z2OnNQ9vq9OhCtj4GySZIxL3bGN4NwO4GIRgIjESWz9KSNhlVg9rYAZG2nTaaByMCCmOr9xlmjoOE8ZOFnx3DKnQWkzsF06G8QHGiU5-An41bsg49IS0xQd44bwi1DI5MP-wT2aP5caXe3EOps7iOufGIoAEZnim_qLx8Wjd_PxnsV5-VDwdzmvrEMWxpE1It5iaBQX3fhJESfZZhQ5oAKrCBCvhSPGxzlRGLLPzKjhezUdsVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید انقلاب: اِنّی سِلم لِمَن سالَمَکُم وَ حَرب لِمَن حارَبَکُم الی الیَومِ القیامَه، یعنی چه؟
🔹
یعنی کارزار میان جبهۀ حسینی و جبهۀ یزیدی تمام نشدنی است.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/446089" target="_blank">📅 02:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446088">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ادعاهای جعلی ترامپ دربارۀ ایران
🔸
ترامپ در مصاحبه با سی‌ان‌ان و شبکۀ ان‌بی‌سی به تکرار ادعاهای جعلی و گمراه‌کنندۀ خود دربارۀ ایران پرداخت.
🔹
او گفت تقابل با ایران جنگ نبوده بلکه عملیاتی برای خلع سلاح هسته‌ای بوده است.
🔹
ترامپ مدعی شد ایران با تمامی خواسته‌های ایالات متحده آمریکا موافقت کرده است
🔹
رئیس‌جمهور آمریکا تلاش برای ایجاد شکاف در داخل ایران و رهبران کنونی کشور را «عقلانی‌تر» توصیف کرد و گفت که آمریکا با آنها موافق است. ترامپ گفت این را می‌توان تغییر حکومت دانست.
🔹
او که به اذعان رسانه‌‌های آمریکایی در هدف خود برای تغییر حکومت ایران ناکام مانده گفت، به دنبال تغییر نظام حاکم نیست و تنها هدف او جلوگیری از دستیابی ایران به سلاح هسته‌ای است.
🔹
همچنین ترامپ مدعی شد که کشورش هفتۀ گذشته سیستم راداری جدید ایران را از کار انداخته و تهران در حال حاضر فاقد شبکۀ راداری است.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/446088" target="_blank">📅 01:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446087">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🎥
لحظه ورود پیکر رهبر شهید انقلاب به مراسم وداع در جوار حسینیه امام خمینی(ره)  @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/446087" target="_blank">📅 01:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446086">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔹
بارون اومده، حاج قاسم برات مهمون اومده، آقا از مقتل غرق خون اومده...
🎥
روضه‌خوانی مهدی رسولی در مراسم وداع با پیکر امام شهید انقلاب در جوار حسینیۀ امام خمینی(ره)  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/446086" target="_blank">📅 01:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446085">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4084445af.mp4?token=HVl2PmR182hvTbEZF6O65VvwJfj9HSDoOWBlh6uhotZ-5RP6DSIfJ_-oLg1LP0e6YjiP6FcGXLC73pjgXyGC4jt52-8j4NRqVi_Lin4SSDmuT3pK4Brrfbxiscr6Ggr3O5nlXuvSPHnGpEON3p7sLZcNLJKt4DMyiuAqI62wfxfuU473ym8FEhDwd0G7IGu95YEmwBQVuqofLWsJzeoWUNrLfcTdoVFyiZOUdorv5jAr20TQ7ubP9amRnwESG1dqgelvrITymGHt9hopgs96fR-EWTZdHG3RV7bKV-FqFQcO57He7E1GLdDZB1qKYqafMKCn6p2jug2CyHSjYhi5DTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4084445af.mp4?token=HVl2PmR182hvTbEZF6O65VvwJfj9HSDoOWBlh6uhotZ-5RP6DSIfJ_-oLg1LP0e6YjiP6FcGXLC73pjgXyGC4jt52-8j4NRqVi_Lin4SSDmuT3pK4Brrfbxiscr6Ggr3O5nlXuvSPHnGpEON3p7sLZcNLJKt4DMyiuAqI62wfxfuU473ym8FEhDwd0G7IGu95YEmwBQVuqofLWsJzeoWUNrLfcTdoVFyiZOUdorv5jAr20TQ7ubP9amRnwESG1dqgelvrITymGHt9hopgs96fR-EWTZdHG3RV7bKV-FqFQcO57He7E1GLdDZB1qKYqafMKCn6p2jug2CyHSjYhi5DTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
او به آرزوی خودش رسید
◾️
تعابیر رهبر شهید انقلاب در مورد شهید حاج قاسم سلیمانی که حالا در مورد شهید سیدعلی خامنه‌ای هم صدق می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/446085" target="_blank">📅 01:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446084">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔹
بارون اومده، حاج قاسم برات مهمون اومده، آقا از مقتل غرق خون اومده...
🎥
روضه‌خوانی مهدی رسولی در مراسم وداع با پیکر امام شهید انقلاب در جوار حسینیۀ امام خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/446084" target="_blank">📅 01:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446083">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">هتل‌های تهران هفته آینده نیم‌بها می‌شوند
🔹
جامعه هتل‌داران تهران: تمامی هتل‌ها و مراکز اقامتی استان از جمعه تا پایان سه‌شنبه با تخفیف ۵۰ درصدی، برای اسکان زائران و شرکت‌کنندگان در مراسم تشییع آماده خدمات‌رسانی هستند. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/446083" target="_blank">📅 00:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446082">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfcRMLfQQO2EG6Vl7cg8lLcVN_Np0QRQKiidhR6Ril2nGeW9W_n-ol9c56RZXtn-I_gYEmAcys8ixv3BsCoIGzaar_JMDlPjyvbf1D_RtaUeHkPxoZmGb_-wlEvQyjTT6TSrHFUccVoFcGBYN-hX60JPgnqQ_6Qrq2YFTBQizGPD0zEV7WFSw0ekLEImndC4zCRG3wOpkaFxzBa_8XCQFilE8AAxYgLslr4ySjARAKtRlvDKrIRJGLllxrteD06G1s5j61FJmSf2n0MGai9fu5bzjYaCoe2hlsQ6fny8MB9FWD4jy-c_xnWyiSEAsg8rx028cUMOOHGnadSAq2JoEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمازجمعۀ تهران، امروز به امامت آیت‌الله سید احمد خاتمی در دانشگاه تهران برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/446082" target="_blank">📅 00:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446081">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‌  خبرگزاری رسمی سوریه: شمار قربانیان انفجار دمشق به ۴ کشته و ۱۰ زخمی رسید
🔹
شبکه الاخباریه سوریه: انفجار در کافه‌ نزدیک کاخ دادگستری در دمشق، ناشی از یک وسیله انفجاری بوده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/446081" target="_blank">📅 00:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446080">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
حملۀ اسرائیل به چادرهای آوارگان در جنوب غزه
🔹
المیادین: در‌پی بمباران چادر آوارگان در شهر خان‌یونس در جنوب نوار غزه، حداقل ۳ نفر شهید و زخمی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/446080" target="_blank">📅 00:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446079">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Igr9HVqmsSRP6B2bZFN5a84FRvwsdQFUVn91YlMNwd5xZWQddkQBeuLq8N6nRPBmHLgYypDJtzP10pD3YS_P15KmCbif5kDwxd8-MoZM30uPIMggRDu_kYja8yz-pyF1N5HbhB6YaVtX6f-_V92iNTttvlf7U8RMXWYJ9t_PG4gzmK97MPi5cilUcg85UoU8WYWRfIqlJw2l_NMX3l0boGd1dYWk9mDHUExgfJlWB-gTEhfkj_XGxJq2Zho5lTGAhzJThN-2-7DPPr7S7G8exdWFY39rcOUcSUCDYK2z_o_2WvbSpUlcYqvM7cdSLGjZWk5k2BtaA8AC97Zb9vUJdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صعود بی‌دردسر یامال و رفقا
اتریش برای اسپانیا حریف راحتی بود
بار کج شاگردان رانگنیک به منزل نرسید
اسپانیا ۳ - ۰ اتریش
@Sportfars</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/446079" target="_blank">📅 00:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446078">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e55c2f97.mp4?token=WSXogf41kaYmjKC6g978e3HeX2rj4Jk6Z6MTANl754Nlm3mJRuJyC6GZw9kcAH4PKGGfhqToy7fuQRSjvZPvkVdOCaH8jGVLXbNdAictfhJ9J_a7AbhozbjKQsTIW3Bi3t42TuUma21BY4tJT-Fdpy6bONyYBTiI6vZ7qisNfkTF9MueqRhvkta2L3b6Ye-7Yx44fisoEIj7bjV3_HO99bO1FLP6Wo6GpqrieNz2H8aqYAzUXvaBsLlQjJOYS1tfAv2qy2ky2fJiTk7FNK470X2gpvZzXi6Ne0KxUOGNSZ2BevBfxhOEoEQdrad4ukFs9gzqTMUmL9_Zobhb4AhVCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e55c2f97.mp4?token=WSXogf41kaYmjKC6g978e3HeX2rj4Jk6Z6MTANl754Nlm3mJRuJyC6GZw9kcAH4PKGGfhqToy7fuQRSjvZPvkVdOCaH8jGVLXbNdAictfhJ9J_a7AbhozbjKQsTIW3Bi3t42TuUma21BY4tJT-Fdpy6bONyYBTiI6vZ7qisNfkTF9MueqRhvkta2L3b6Ye-7Yx44fisoEIj7bjV3_HO99bO1FLP6Wo6GpqrieNz2H8aqYAzUXvaBsLlQjJOYS1tfAv2qy2ky2fJiTk7FNK470X2gpvZzXi6Ne0KxUOGNSZ2BevBfxhOEoEQdrad4ukFs9gzqTMUmL9_Zobhb4AhVCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم اسپانیا توسط پدرو پورو در دقیقۀ ۶۶
⚽️
اسپانیا ۲ - ۰ اتریش @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/446078" target="_blank">📅 00:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446076">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZ9bSQeyqikSU3m-NUyhloBAB8MgG97uFHc59cNuCHytbL1-UAw61ApmI7An7wxLKnxodc-Bk-lRPZXBGlQGvsqiei35OPCarqdTK8R-F_ZqQgMOg5oA1tKKANpQB0Bzyysivf4CW_qhmqAAr3ue8Jw1J-cT8dJNkTPMhC1SpyQEe2grpXKxhLIng2uFbjQZ7guBsmWblqPigrHHcUqdu1l55Nf5z0wsZ1-LkrtARyY7OFmtr1rCswk6KTNjFCkUoeFFXMmLWhvF6o9vfh9XTqXMU2Ya44nfoQsvJH8MiqRqmvZtRWirEIJw4RZj0_miH8g13RtucgI0wKvCeYxd-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFaMH7x9DGVRHmclA7umcvXUDieAbF_GR_WBnnH4Qs_L0s1Q3KSPe8cRaPQX5hqbzRjaAMJXQM5gWZs40iq7IKeb55ErGOedHIRzDNTv3013a2ZUTiWgieOuWMM1sbHAOWa-ah2adQ5pxyC9b8zwVD6DpodELWYJ2yUeKZF3qGJGJZGm9w0cM-SpukhgExlXl9SJ9V6Re5qe5Jqwf2jWt0AAEvWl8Xkf7Gpos4QzW2uaiPxpgacKzKwIu_FBF_zmZXvK6p98qUVj90qXlgTq8e3pymTe6UWkSFZL0ISGkKpoFyB1LjygEB4wWj6zdLkI7icj5nb8atvy20t2kQvYHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور سردار وحیدی در مراسم وداع با پیکر مطهر قائد شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/446076" target="_blank">📅 00:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446075">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t500-C9L7a0UtEaLMC8Os-rbF7Ambz5JAABDMEEHEAw4vWm0oHz5DKxCf1yLrLlufHF-sBJ9D8REwJSUJQThQxMLb56kNB69S7cJctRf2yd1iZcAAjdC__zp2fVwT6aQzTHxmOjlK-cAkuYyLu68dTWRV4zebl0fateVbPVm10q74KVuXxjvxMljvVRrY2T8Th5NkufbSDHjZNjA3xNy1pNAmK__NvOevSAhWvwNhYhzYQdvQB2NXZsqbwdLUh0_ZsCMSOW2LWgRFB63lTDS-9yrJ7AtVQPjUemwLgn7PkF_T7Yh7ErBPkAWihnu7afMVx7zzGgCC18HfstRItE5Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نان و نمکِ علی(ع)
🔹
عقیل، برادر بزرگ‌تر امام علی(ع)، به‌دلیل بدهکاری سنگین به همراه فرزندانش به کوفه نزد امام آمد.
🔹
شب‌هنگام، وقتِ شام فرا رسید. عقیل که گمان می‌کرد به‌عنوان برادر خلیفه، سر سفره‌ای رنگین و شاهانه خواهد نشست، با یک شام بسیار ساده (نان و نمک) مواجه شد.
🔹
عقیل با تعجب گفت: «علی جان! تمام پذیرایی تو همین است؟! من فکر می‌کردم در خانه خلیفهٔ اسلامی غذاهای متنوعی پیدا می‌شود.» امام فرمودند: «مگر این نعمت خدا نیست؟ پس باید شکرگزار باشیم.»
🔹
سپس عقیل به امام گفت: «من ۱۰۰ هزار درهم قرض دارم و برای ادای آن به کمک تو نیاز دارم.»
🔹
امام فرمودند: «من چنین پولی ندارم؛ صبر کن سهم شخصی‌ام از بیت‌المال را به تو بدهم.» عقیل گفت: «بیت‌المال دست توست و مرا به سهم خودت حواله می‌دهی؟» امام فرمودند: «از بیت‌المال چیزی بیشتر به تو نمی‌دهم.»
🔹
وقتی عقیل اصرار کرد، امام علی(ع) پیشنهاد عجیبی دادند: «اگر عجله داری، بیا شبانه به بازار کوفه دستبرد بزنیم و قفل صندوق‌ تجار را بشکنیم!» عقیل با تعجب گفت: «علی! به من پیشنهاد دزدی از مال مردم بی‌گناه را می‌کنی؟!»
🔹
امام لبخندی زدند و فرمودند: «چطور ربودن مال یک نفر دزدی است، اما ربودن اموال بیت‌المال که متعلق به همهٔ مسلمانان است، دزدی نیست؟!»
🔹
سپس امام پیشنهاد دیگری دادند و گفتند: «اصلاً بیا ۲ نفری به بیابان برویم و راهزنی کنیم!» عقیل گفت: «من اهل راهزنی‌ام؟» امام فرمودند: «گناه راهزنی در بیابان بسیار کمتر است از اینکه منِ خلیفه، دست در بیت‌المال مسلمین ببرم و مال مردم را به برادرم ببخشم.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/446075" target="_blank">📅 00:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446074">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94fc02174c.mp4?token=pzkN0l8uzJekLIdRW7035bZc_lDOvyO6ZYKYxqUpt0ccGqGfhfnHxTDIgL9EqPKJ2Pfc0r2n7TDHcFRimDAYsM3hDQaDAbBzj50rCIQQRJ_UbhDTNcbpEfeZnD-3GBbMzFbK9B6o1Hxr-d4TYxJHyQxKH-S-zvM7T1Ot6Q28ZKKSzq8LQDqCh2sC3Jai6LC9nbto6jOHpZrIhjHQ5fLRYY306MZMAluZEcZ7Nb8JWU1KXbDKd_SVjN25cqpiRfd0euMjcSoGi_gFEliQOnqjMY_a0N-HBJgqUw3XyA9stQWFtXkMiKX6Xuq2SFC77MpHzHR6vVLAmjsS-TzAygdKPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94fc02174c.mp4?token=pzkN0l8uzJekLIdRW7035bZc_lDOvyO6ZYKYxqUpt0ccGqGfhfnHxTDIgL9EqPKJ2Pfc0r2n7TDHcFRimDAYsM3hDQaDAbBzj50rCIQQRJ_UbhDTNcbpEfeZnD-3GBbMzFbK9B6o1Hxr-d4TYxJHyQxKH-S-zvM7T1Ot6Q28ZKKSzq8LQDqCh2sC3Jai6LC9nbto6jOHpZrIhjHQ5fLRYY306MZMAluZEcZ7Nb8JWU1KXbDKd_SVjN25cqpiRfd0euMjcSoGi_gFEliQOnqjMY_a0N-HBJgqUw3XyA9stQWFtXkMiKX6Xuq2SFC77MpHzHR6vVLAmjsS-TzAygdKPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول اسپانیا به اتریش توسط اویارزابال در دقیقۀ ۳۶
⚽️
اسپانیا ۱ - ۰ اتریش  @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/446074" target="_blank">📅 00:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446073">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxNU7ho8epNolUcwOt7j4IWW1D9OgZC-zfqa13RkTPCaKzlYjSQedjtm3hCvAHWQBLkbmYHe2gOsKNFxQNNAFHKm4cmD7p6_kh8e5wTdyp8vY3L9EtUPvcZdvIvXmfv2QNcYJORkUw7GldUJpNA6ZSDeFSvxpgzBAoIhREIQOb7Qn1pf5jYOX0Ff7xZehjhCzH9YfMtY2bYaMedmzFlxVPH6_i1EhLGJGEYwwuCI9QUffr6vCAKR-qQ4rlZxrPpmseeVFDLxEs2mPFoQHTqhiaoOuvU9yVHlsVeQFGUyqRxT7rVrhPosT2b-zFmLwKetriLuAjt6m6UYohth6Tti0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
| جمعه ۱۲ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/446073" target="_blank">📅 00:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446068">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oANhnbPeIEOlQSbCyakJoLdubMfq1ktXJU0n5dClyCYUab6_B3cR1ApDRV2UH58BPv_-GelSAI8nVX2bSIoTx08Lrg3Sgx98Krm9uF_U7RJReUDN52Y8BOvPB0U5kPvP6VH_16Zx0rgn3ES-VIRv9yemOfjUDW34-nTHSS18nOnTw0idpq0NDAtiRIOLZUm3sKhVIoZYrXNUTS1mS-8qi_zmLcDYRW1TlJA-F9m322aDwA2TdIQVEnWvetvh7qXEm5V7qIx00HsN_K9f6e-F--iciSwf8mqsbRXDOFrTgt_KXvZybGEmvkU2UmXdGU91_cXMi6aBKISqFe1O0AVIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HpRTH21_7nIfjUraT77PyGF6u8Go-SfpKalFMzYgY-Kj01XIeW1Rsgkx6573FuRHNNX8OSMIIuWuy8fEPeXG9yztvF4NSJOpB6nsqc818-OU9UUUwKo-_8xZaoSZtsljsTWKAvFfKva62DV8S7VOGs4uPx7kmdnsbIulTqerFqu3xVv7bEgqZfgM6zEqVrnTE_RaXIzAC2qup0t2n3NClwBSrf0E7NGT0CGCFBVR77UaH8zlg1it7etXOgfNBKKmCnjjXne4vFAkmg_8kriRb5PGuWCycO1gr0RFD4l26YeX4PQw7_TeR9b5dH6UdUV3D7IsN7OIcehyCffJiZMP_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pqqMkfVzYbHO9fzhKLjvJKEVdMi2Ph9ItnoYt6yHM9RM8FMP60vA_QrV-wyZPG7y-BGGLBIRJMrVAJ6Ubx9eXEsv36nd_8oOxEtwd3IbzngLDe1xZUHL3cXZvuwRSlMVMlNVWZO0mqfCaqkxizjh9NN_IsEqtxxBZyXzEtARYUDWhC1u85rUQcPG4T0tgV-z1TxZEoJAcr4FGJ5pTBaEKl4t2JL-QTeZKqpYaTWt4qFaBRCKzazXB86zOpdwMHB_pVAhaRRGZ223U_qc5pyGnAcFIqHB6H78-6lYTuagl4nujVWJrxAdMomfcdfgZm3k0I20_Dg0x8y21-dhitGnHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TFvdGQuE29Zm-Bzz3mdQx2stdU5SGzL6cCw9zY7wBGdlKTeEV6f7ViDMEM0xNrthvDoQAaNOk_JoaMTL9c5jKWoQbqxnDkPDAGzbIEHp4Nbg8xM8U8aN5OQLuUphmnBJj5Fwzakfwxnhf8ohdoHKjGM26ArX6b1PrXwOPfNgvih7WubHHOzDVCYxwenJ5uWyBYvS0G-S93PHK1VIuu3Fl6vIu6f3R8df-3bsnVPoznOOgr3XomSCbowFZKYuF8DxU-IQg_7PmEUcK0b2FOlgfxJAEysw1G-7r6ndk3FwgCoEg_ySg9dCxZ4232yqrRtsJIwFdxhX3e3J3AxxSkymUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UmRQ3RDvA2JuuYoDaSSJdY6XK5g0FrFtaZKSoV07NbHW_0ns2FKuk9k4g4nFXA6E3oyJkYjOnpjlvnkTd3Rv4scoQDdswZJ05sDUSPAIGLHXwHkhB-M2QFUwfhcGOJDMT6OeKXvRt54OjN45lOhZ8wYKQbfhgLR7VppPdKvIRYx8zUo1AB9O16AFXB8OdOMPEbXmDELjp0gRRKZAiPVUyh7MMcUVZXjcK2dWHdEnfOdN5hutpk-x02mTiaXfVubdaG14edRDBd6Xj_k-AW4q_n2Hs9mHuD7_r571lbGk26wiQT7oML-63284SlYvtdHHRb2PQkEPlVKjh1EP1WvVZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
لحظه ورود پیکر رهبر شهید انقلاب به مراسم وداع در جوار حسینیه امام خمینی(ره)  @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/446068" target="_blank">📅 23:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446067">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etA4MnQ86o2LhZVvOs0rL_uxQ9-RIqvxK7yVvX2V4ZSsXtvrfUPYSYY2lOkEHPQC9qX9_qJvFmKFKjpQD4v4Lohrub_HvEVJSfB3anavD58BJ3gjqooElZnNb_y-jINHb58MAv9IMRxXMsenBehfpdyWzvxQCepDslz1twblIxWcjyCGj9C8lkdJg0BCgXamVn1oaysPL7-DDIdAWn26lF1NrLZj7kTZ3I2_nKrDe_y7Z7jNNjVmMVtVXT3wA-034UtzTW_JNBnsmUHR7UOBNBh41kovz2Ae6-jhJ_OdGho7pNjvUoKNZs2ywHvsdgv0BDCFNDsiGfdqce43fgC4-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسلیت مجدد گوترش به ایران در تماس با عراقچی
🔹
دبیرکل سازمان ملل در تماس تلفنی با وزیر خارجۀ ایران ضمن ابراز مجدد تسلیت در پی شهادت رهبر شهید انقلاب، با ملت و دولت ایران ابراز همدردی کرد.
🔹
طرفین همچنین آخرین تحولات منطقه‌ای و بین‌المللی، وضعیت تنگۀ هرمز، روند اجرای توافق خاتمۀ تجاوز نظامی رژیم صهیونیستی علیه لبنان، تحولات پس‌از امضای یادداشت تفاهم ایران و آمریکا و آخرین روند مرتبط با مذاکرات جاری را بررسی کردند.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/446067" target="_blank">📅 23:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446066">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b661961b4.mp4?token=g_pjnRP4evUIyj4eyJKtK0itobNVgDLPicZpoHcSTZU-G_RFCMnY9KU4DuiUbufqcQsAMNyNilVJOiqSWnmspjbKgL_eP76mbRpOqdwuPBGrWbIJnTqiC7iBReN93gWiW7V9q77HQvWagwFg72K5C0QdgW1gVaQkakCMSSeYOHEHK5poaDTZFkFq4pd8vacGorPg20v4fRyz_bBVtY3Ar5jtgsWSztmQFBQObBfTvYo8xwinBy2EJRxPURonIR1inW-SQ2DjFzZpotgyG5UVBcD2sLGsjRi4DHbvxq1fnyMnsGB5AQ-lYqutMki0jx_vYURLRlDuaJsLymSeBBDRZFzam-IipFEcg30nvTrJUDbDWoYYw5rXCgN-lHS7bBNWH94UXsJYTDzg3qijLorH3Xl7FAp4ajF_PtTMzqmsM09sj6y0_qNbCMgxI1Q2Z5T6Ev3Z1wozqEGkjVetdb8-pPsLn_GT9eweiP5wTmeB5tG1HfDK2yGnb_ErvTyTRB5gR3PwjQgFqRt3tJigLyU7WxNNNC9b4UAPACNa82LR4Ep0BzvQlTlunk9siVKwciTRgyWkNIWGVZiAaYseI6qkFqxEExKq3gztv1kq48uX9t87-8CjFWO0m7aGD5vaIsK3yJaVvwYV5SgbqgPUjj_jN1oz0kY7vSfCfxJ_BWdleps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b661961b4.mp4?token=g_pjnRP4evUIyj4eyJKtK0itobNVgDLPicZpoHcSTZU-G_RFCMnY9KU4DuiUbufqcQsAMNyNilVJOiqSWnmspjbKgL_eP76mbRpOqdwuPBGrWbIJnTqiC7iBReN93gWiW7V9q77HQvWagwFg72K5C0QdgW1gVaQkakCMSSeYOHEHK5poaDTZFkFq4pd8vacGorPg20v4fRyz_bBVtY3Ar5jtgsWSztmQFBQObBfTvYo8xwinBy2EJRxPURonIR1inW-SQ2DjFzZpotgyG5UVBcD2sLGsjRi4DHbvxq1fnyMnsGB5AQ-lYqutMki0jx_vYURLRlDuaJsLymSeBBDRZFzam-IipFEcg30nvTrJUDbDWoYYw5rXCgN-lHS7bBNWH94UXsJYTDzg3qijLorH3Xl7FAp4ajF_PtTMzqmsM09sj6y0_qNbCMgxI1Q2Z5T6Ev3Z1wozqEGkjVetdb8-pPsLn_GT9eweiP5wTmeB5tG1HfDK2yGnb_ErvTyTRB5gR3PwjQgFqRt3tJigLyU7WxNNNC9b4UAPACNa82LR4Ep0BzvQlTlunk9siVKwciTRgyWkNIWGVZiAaYseI6qkFqxEExKq3gztv1kq48uX9t87-8CjFWO0m7aGD5vaIsK3yJaVvwYV5SgbqgPUjj_jN1oz0kY7vSfCfxJ_BWdleps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظه ورود پیکر رهبر شهید انقلاب به مراسم وداع در جوار حسینیه امام خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/446066" target="_blank">📅 23:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446065">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13db40e712.mp4?token=H5HdFv7bxkyn0GAtUKz4oWfnmQVV__cTv0cK8q3tt57EKJLup8lTTk0_y5Hhfd45unFMvbO57RS68cwU0Jj9AjKq9APFIwHUbK-s34S4km9RlXDvuVGbFNHGBe1NAhhNtlQN5QtnpiIYcch6epG6y6q3Zrgi3WQOEdtxQWGgxQOEKO26bje-sWH5dst4E9DiddcZlNjmz4PISCEA7fF3sMyI_XIvkaE53EUPCYpFYvDc6h1WhmvYTXJYKsNG53OURx25Tnh4PA_Fcmp-kRQaoYb2UaM67cj0i7BOWaaJE10-PXv-K2kh--jHlkXPZBMPA-Xat4cE_iYtq4MvUi_jeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13db40e712.mp4?token=H5HdFv7bxkyn0GAtUKz4oWfnmQVV__cTv0cK8q3tt57EKJLup8lTTk0_y5Hhfd45unFMvbO57RS68cwU0Jj9AjKq9APFIwHUbK-s34S4km9RlXDvuVGbFNHGBe1NAhhNtlQN5QtnpiIYcch6epG6y6q3Zrgi3WQOEdtxQWGgxQOEKO26bje-sWH5dst4E9DiddcZlNjmz4PISCEA7fF3sMyI_XIvkaE53EUPCYpFYvDc6h1WhmvYTXJYKsNG53OURx25Tnh4PA_Fcmp-kRQaoYb2UaM67cj0i7BOWaaJE10-PXv-K2kh--jHlkXPZBMPA-Xat4cE_iYtq4MvUi_jeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصلی امام‌خمینی آمادۀ مراسم وداع با پیکر آقای شهید شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/446065" target="_blank">📅 23:22 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446064">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f5a56810e.mp4?token=rT0xlZQjt_oeQTvZ8QPjHc-iGTTUy3-fU39qbM9Dxy5fNga3MNvrVMu4d7Cb1OSsCHhdchBwfxTR1GYLqGRzwLHU6kdRF_Wo85dhCqCCxkJWAaJ3AmKNFxjxkxdt5qpWclvI2eXg8tcIpn3EQz-U1LP3HqX5WsY-LmkRnIXyX_VgTcr-DIUZu0j6vIaQQspNkwzBLMCwjQnQDd6GNDUQp386yXDor8YkxlEnH41-BPkWgxLMWxiipc25s97a0_RbBb1gwv6gO77dwod-ZCOa7WP_PE13wVXppGkRWuQDd4usDsrE5LUSRCtjsdTRjuj8Mjdt2DAIpjnTlrXXtjQwMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f5a56810e.mp4?token=rT0xlZQjt_oeQTvZ8QPjHc-iGTTUy3-fU39qbM9Dxy5fNga3MNvrVMu4d7Cb1OSsCHhdchBwfxTR1GYLqGRzwLHU6kdRF_Wo85dhCqCCxkJWAaJ3AmKNFxjxkxdt5qpWclvI2eXg8tcIpn3EQz-U1LP3HqX5WsY-LmkRnIXyX_VgTcr-DIUZu0j6vIaQQspNkwzBLMCwjQnQDd6GNDUQp386yXDor8YkxlEnH41-BPkWgxLMWxiipc25s97a0_RbBb1gwv6gO77dwod-ZCOa7WP_PE13wVXppGkRWuQDd4usDsrE5LUSRCtjsdTRjuj8Mjdt2DAIpjnTlrXXtjQwMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول اسپانیا به اتریش توسط اویارزابال در دقیقۀ ۳۶
⚽️
اسپانیا ۱ - ۰ اتریش
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/446064" target="_blank">📅 23:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446063">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">شهادت مرزبان هنگ مرزی سراوان
🔹
مرکز اطلاع‌رسانی مرزبانی از شهادت سروان نبی‌علی اکبری پس‌از تحمل ۱۰ روز رنج جراحت که حین خدمات‌رسانی و پشتیبانی رزمی ایجاد شده بود، خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/446063" target="_blank">📅 22:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446062">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bW-uQ_C1D8hPOpbl-xcEYLAjHB7lYCZPEBwUGjvdTbLqc5sOWe78xNEF5Y1ZC4aeTq8VLoOW_tpOp0FIiS4YhmcejDU80XJ4UkrkTHpoxSp8osT5PveHaFrFi5SbtRIG8OvdF1ERa04SXZ0r9tNWN5A8Agnjdb4smKADyUfxXE3M_iXBNiAYYaokOTk2voWOOAp_RVvlbXgTRkDtAAZBzhrcsV1e1yU0yZQRq-dV1xdDKeA9SHeLuNpNP-ExvsN6wG7cJKBM1R7fNNT9KWzzYN54z9Z9anOhEHXOYdKTFMPCy5j7ylEn2fwKAXt0j5wTghKf9VK-YaUB0NUfj4-XtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏀
ایران انتقام بازی رفت را از اردن گرفت و صدرنشین شد
🔹
تیم ملی بسکتبال ایران در مسابقات انتخابی جام جهانی مقابل اردن پیروز و صدرنشین گروه شد.
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/446062" target="_blank">📅 22:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446061">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5tKBLeLjfSEmfQH8Z_s_6H6Ly42uXYSi4Eh186h7UFKb9cLqwAiNAlMiOXAGl7vie9SMZoWGp-WvX8u61ktr0l7hyBEtvlaRNkQgufIrsEaW_gv5mJbGmEiNx-ygC7VEw8pWsQ89NxuI-o474Mj3ZlTChPpNiiGXBpARKdiVrQi2onjW7mDnh3NA6hR9EaglR4WPvw2pcrYAMJ7oYj-2M0QiXLRebKfij8YrkzgnHesgYNBK4wluLXsIbNQHr0ghhjRMiyOl74cmzCd3if0KemRnAWJiX-2veT-65szd4iF4VG8l0vm9IudwHtISCEWL7E6zUeJOMCEpX_VHqbNDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور اسکوچیچ در پرسپولیس مصوب شد
🔹
در شرایطی که طی روزهای اخیر اخباری مبنی بر منتفی شدن حضور دراگان اسکوچیچ در پرسپولیس منتشر شده اما پیگیری‌های فارس از منابع آگاه حاکی از آن است که این موضوع صحت ندارد و روند مذاکرات با سرمربی کروات همچنان طبق برنامه در حال انجام است.
⏺
روز گذشته هیئت‌مدیره باشگاه پرسپولیس در جلسه خود حضور اسکوچیچ را به عنوان سرمربی جدید این تیم به تصویب رساند و اختیار کامل را به پیمان حدادی، مدیرعامل باشگاه، داد تا مراحل نهایی مذاکرات و عقد قرارداد با این مربی را دنبال کند.
⏺
همچنین طبق برنامه‌ریزی انجام‌شده، قرار است متن نهایی قرارداد طی امروز و فردا برای اسکوچیچ ارسال شود تا پس از بررسی و امضای آن، این مربی کروات به صورت رسمی هدایت سرخپوشان را بر عهده بگیرد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/446061" target="_blank">📅 22:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446060">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aY2c9tTZCXuSmarVt1jgQZYV7j2hB5RF9BLoK0HlZ-r-hL4k7wDVqFvMker6eoo-lrHaZG_Yh0qEMCGdnQdBu0_mpfuJJX2Txu6IKH4p9rJ-ieobh8vOrWonEKOMmVUw3RfIL_GE61haxTX7vtXa3f4MuoxZFtp-tOlnotCocZkKENUOwRfS6KbfIbg9yZJ2iWbD1H16EgqWLpn0ywftY5XiAIQVjLEc1nqCTwJWUj9-YclsEPULFkRxxGzzQTS6SGFUN9yXJC5AUAKS3A0Ut73ada2Fx4gzNRwzdcFU2WcJoqbzMOphrj46D39Evxhf9BEQMxlW9D5xmsmnCSaxgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پاسخ عراقچی به سنتکام: صلح در منطقه وقتی پایدار خواهد بود که بدون دخالت خارجی باشد
🔹
وزیر خارجهٔ ایران در پاسخ به ادعای سنتکام دربارهٔ رهبری گفت‌وگوهای صلح در منطقه توسط آمریکا نوشت: آیا فرماندهی مرکزی آمریکا برای منطقهٔ ما امنیت به ارمغان آورده یا ناامنی؟ پاسخ کاملاً روشن است.
🔹
نیروهای مسلح قدرتمند ما ثابت کرده‌اند که بیگانگان حتی قادر به حفاظت از خودشان هم نیستند.
🔹
صلح در منطقهٔ ما تنها زمانی پایدار خواهد بود که فراگیر، همه‌شمول و بدون هیچ‌گونه مداخلهٔ خارجی باشد.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/446060" target="_blank">📅 22:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446059">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🎥
بهت خبرنگاران خارجی پس‌از دیدن مردم در خیابان‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/446059" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446058">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e606ffbff1.mp4?token=GFZ4OTpXNnPORxznd2y0a8s3dGMRRK4wW4BA4c6FYiLVMh-ekpQWLKJlYCdN6P7rhwMoc-klUCO9lQiPrMTgVorK5P3PEUDD6Q6zLVA_6Q7WNdEjEm-a3PsWkfP0PaMkgSmLkje_13vxNIQJTfxnPtgcELZhPAR-5FWkSZSqC2EayPZRcVLBhXCJeB6skmhotXwf99MQprS_KcXBysW_vm5g4n2p9OU8H9osmsLumk3Xxlrujy4v1t7AA0fYs1eqT25_D9XdJKhydKGIrz6jxIqEXfp2SW7Gd_WIP-NBM1-qtHfcgxh0YsiJblv0MZW-epNWQjFX0-g54eEgvJvDSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e606ffbff1.mp4?token=GFZ4OTpXNnPORxznd2y0a8s3dGMRRK4wW4BA4c6FYiLVMh-ekpQWLKJlYCdN6P7rhwMoc-klUCO9lQiPrMTgVorK5P3PEUDD6Q6zLVA_6Q7WNdEjEm-a3PsWkfP0PaMkgSmLkje_13vxNIQJTfxnPtgcELZhPAR-5FWkSZSqC2EayPZRcVLBhXCJeB6skmhotXwf99MQprS_KcXBysW_vm5g4n2p9OU8H9osmsLumk3Xxlrujy4v1t7AA0fYs1eqT25_D9XdJKhydKGIrz6jxIqEXfp2SW7Gd_WIP-NBM1-qtHfcgxh0YsiJblv0MZW-epNWQjFX0-g54eEgvJvDSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیرکل سازمان همکاری‌های شانگهای در جریان سفر به تهران برای شرکت در تشییع رهبر شهید انقلاب با عراقچی دیدار کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/446058" target="_blank">📅 21:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446054">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NlNz8VFwcv8mOcB6arGdIpnnZz7WlJZl2etycbuHiPs-ZHKHftuodHS4a0qdilHQHzRXZReeT2qkvnkHf0paA3XQX_aAYP3IA4DmNF6d8zMHQ6CrD7TRp3DgGl3h-WNYwzsljrzp4h3hLPIgroemK6xqWtWjDaVoaw1CL7a6lkQCMHkQa1u1c1AMChcFMZcRmhuRaxgVIwpv1q63c06TZZloMrt1ag5fXIhaA4si-hwAfrRLniqZb_YvGHXVtaD8ns2dYTR_ih15GJb9mraqaZJyOiEqWezylrQ7qb-f9fr8Hs-e8GKPfShOPvbEw3iFO13B7IbYcehNVZKlWvGCPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZPnufhH9ix2WNf7VwNOkffPn_sI-IwL4_x8oMG_xk7uyyf8RxyJflXj9a6MtywZ5eSGXtBjA9osfqJ5OSL3XVWtUxUwLA46SQvNSrTC-lWWlM3J5dITX_K_3eQiXSw6cHIpNiIZ8Gj4YSn8ChB7jsrdZbMj4iByBj7l6iH_rzJbnhVD9sHKqkMPQpqCd-OfeWAYsePZQTzRYu32sGOVEpFni8txqUMB1pKko0XKQ7bNB8vuI1pXomxmXiQg9DKTDOXCqgPuKEQLC8wR28Yjllh7XNiCIeFWkFqqTTC71qdRsSW8tEtw0mU23xcM9P6mFPn66WFZhsbhywjbJl0dNVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LLWPqlmJFQ1ekcNnECJ9uvTZqVH-sQLdZxkujm-8xwPD9FZJ6cuFWMaRmqvvjyx8pDl8oJIONQeon-CoeKlZdPyV3Da9SDozwIR4gwc7jBGdkEAipdZWR4kU9pzVjNq8BNmlaA8-Nh2QOOoz2RvTQHi5GRCXbPFZ2ZKtgT2uhvyNFoUzZfNtuw3S85tUxkxIHMWYUnPvOi7fE-woZme0U6MekrgLYKg6Czs3YuI2Ks9XdYP0y-rblKY86Bwq4210pHBBKAXWK-0kRwQ4l1pZuvTphOVSQBSlOZkIy7m6Ekttm_GngqQSb_AWtksiVw86CwPo6EeodrAUEz6VwBezGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WbdeQf4NSh5nTOylCR6isJYQlwaW0Lx1cI_yfPfT9ZWgwTybrj0-kYBRT7xpmZP-qLDBELf_m_u-XV6D7MTIP0rKApBKsKPjjDlhZN7ETyOgaZW0fidygx17aFEA7eNMyOj8ChSomqz51poBEvMwkX22aQ1zypSyF5hA0vRvXMtqLhy7PaNr1C9gnXozBc6F_g4r7w_zf9ufQBRvkdVsdCrBWqUS0UH5kSIJdWVXct2XnXYMG6MfZ0uFJe4zPGTI05v3GRDiUi42DDL7gMZA_XUVGazXmYwv-xqOSuQNsgSos4VRD1C30-1psqCMMKOTn7sJXQSNqosrt_7RLnOUwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار عضو جنبش امل لبنان با قالیباف
🔹
خلیل حمدان، عضو ارشد جنبش امل لبنان که به‌همراه جمعی از نمایندگان این کشور برای شرکت در تشییع رهبر شهید انقلاب به تهران سفر کرده، با رئیس مجلس دیدار و گفت‌وگو کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/446054" target="_blank">📅 21:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446053">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7b21e0bb7.mp4?token=ncFp9c_hKSKBe_xSLtGE52FQl100cgA7SozDlzNjw97UMQVslJtmLOR1qKC0U3UDssiAb7p61hUtnsgu2jX5IOgIjxcY2bLcDZEsva1q4HoUEf9EtAJZbH7RzduPe1Qh5U_OOWwFTrzTtBgyQx81axspBbYmVVcFzu2TXIlZio5-RXgVgkSMAY5ucLCcLSFqLZfYlDfqGtixB-toLciFPWFeYWaFPwBTN07K9vKZlvkOn55y6dA5Y2M0_N76yQCF5ciz-pVpHgWpiXpENCFw3LxLJ66CUMeEGTe8dNSDW8EBkkcJwEv5JOlcwvugRTFnMvSZbhFPm5aGY6CWDSgcMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7b21e0bb7.mp4?token=ncFp9c_hKSKBe_xSLtGE52FQl100cgA7SozDlzNjw97UMQVslJtmLOR1qKC0U3UDssiAb7p61hUtnsgu2jX5IOgIjxcY2bLcDZEsva1q4HoUEf9EtAJZbH7RzduPe1Qh5U_OOWwFTrzTtBgyQx81axspBbYmVVcFzu2TXIlZio5-RXgVgkSMAY5ucLCcLSFqLZfYlDfqGtixB-toLciFPWFeYWaFPwBTN07K9vKZlvkOn55y6dA5Y2M0_N76yQCF5ciz-pVpHgWpiXpENCFw3LxLJ66CUMeEGTe8dNSDW8EBkkcJwEv5JOlcwvugRTFnMvSZbhFPm5aGY6CWDSgcMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون دولت شهید رئیسی: حضور حماسی در مراسم بدرقهٔ رهبر شهید، نماد پایداری ملت ایران خواهد بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/446053" target="_blank">📅 21:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446052">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🎥
تا ابد یادت هست؛ در کشورِ ایران...
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/446052" target="_blank">📅 21:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446051">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a48c46c71a.mp4?token=c5QnRYtxMU8x2t1OnrAYbXKrWyEBb4mUQKuwsIqVL3LAopc_swH1ACp8NIOmYLkjm6pdVmTcEQgYyXkSl2kJEMn0CQ3yK7c7hyQKNFM7XMN0DGMtB4KTwUiq7AeHxtV9JDyli5uJTzZ-VGwQLlY2hp1e80kZ8NJHf_boful9mIqQiUDB1Cx0C68sb14jJH1BAJ9UnCMcGnJb8cPAchhTFHpGkl5wgO-te0puMKEwuaZgfNjpQboVvpdUfZryKYRbsrgDhysQNQRASNX-HIaNll6pyAM_9lz39RW8NlC0V4vs3nNOtz7d2sszkIUaYyP2cbBufmve8wr51DCFIV65nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a48c46c71a.mp4?token=c5QnRYtxMU8x2t1OnrAYbXKrWyEBb4mUQKuwsIqVL3LAopc_swH1ACp8NIOmYLkjm6pdVmTcEQgYyXkSl2kJEMn0CQ3yK7c7hyQKNFM7XMN0DGMtB4KTwUiq7AeHxtV9JDyli5uJTzZ-VGwQLlY2hp1e80kZ8NJHf_boful9mIqQiUDB1Cx0C68sb14jJH1BAJ9UnCMcGnJb8cPAchhTFHpGkl5wgO-te0puMKEwuaZgfNjpQboVvpdUfZryKYRbsrgDhysQNQRASNX-HIaNll6pyAM_9lz39RW8NlC0V4vs3nNOtz7d2sszkIUaYyP2cbBufmve8wr51DCFIV65nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: دفاع از نیروهای مسلح وظیفهٔ من است و با تمام توان از آنان حمایت خواهم کرد
🔹
برخی مطرح کردند که چرا اعلام شده ۲۰ میلیون بشکه نفت در اختیار فلان مجموعه قرار گرفته و این موضوع را افشای اطلاعات داخلی دانستند.
🔹
بنده معتقدم اگر بار دیگر نیز چنین شرایطی…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/446051" target="_blank">📅 20:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446050">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daac390ee1.mp4?token=nu-bZkwffsvw8m3JfW-eVvGvU95HTQxDGO1UlI4VZFWcrCaaVG0dcqFQNkdKaGhAdJ0Z6X3UkmO_PvJ2XTle4l3oRZDAjyH1EzzYtRI2Ri82dCLIu84LY3vWTw4ze_7X8skD6qDMOUsdnRnDX6Msprs4U7I1iR_erEORMeXk9jjgKz1hk7XtzAKPF2IYbVwybWOcBaLrL3BWzWOaPbspuW1zti0yCFDJmertkQQdS5PMX7YoRV4RwvxaR80wsRH7PGdCZMbWPu9Ls0aABkA_8yCmEYqkOrBRCKviq0oUUiWls8NL6sj-B7KkvhqmWjC9IzRst-9ER5h6Oly1uuKM_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daac390ee1.mp4?token=nu-bZkwffsvw8m3JfW-eVvGvU95HTQxDGO1UlI4VZFWcrCaaVG0dcqFQNkdKaGhAdJ0Z6X3UkmO_PvJ2XTle4l3oRZDAjyH1EzzYtRI2Ri82dCLIu84LY3vWTw4ze_7X8skD6qDMOUsdnRnDX6Msprs4U7I1iR_erEORMeXk9jjgKz1hk7XtzAKPF2IYbVwybWOcBaLrL3BWzWOaPbspuW1zti0yCFDJmertkQQdS5PMX7YoRV4RwvxaR80wsRH7PGdCZMbWPu9Ls0aABkA_8yCmEYqkOrBRCKviq0oUUiWls8NL6sj-B7KkvhqmWjC9IzRst-9ER5h6Oly1uuKM_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
در شورای‌عالی امنیت ملی تقریباً همۀ اعضا متفق بودند که این اتفاق باید رخ دهد و تنها یک نفر نظر متفاوت داشت که وجود یک نظر مخالف در یک مجموعه نیز ایرادی ندارد.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/446050" target="_blank">📅 20:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446048">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/116b02a266.mp4?token=CrEdMFEn5k0cTSsToa3opbgX9CV8gZsk1DiYg1ZH4mWzORZysdfs3k3FpQNKgMfi65rLHQzjEUOuKe5SQ0Mu5OvNYLOTlglquUvr67pOY3qvoJCg_JeTaQum1b__Q9o3tdf7lQvEqvKrii6-PkD-b7ny-p1WGDhrQ38KbPv2fDrReASShQqbB5H-Nkcesqajs-j-mdGM9XKw3YhwG8QRo6c4GyTNaEiPnKpbv5U3uSrSrXgeoDL_6h5TCJvGJCSYECmq1RpnMrudvj2gXwwsEnlUQ0C1eWKvmpEtbIqWm5_SVi7oxNRLit7qTjqLwiyC8ct5A5ye_8524i1t2XX0RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/116b02a266.mp4?token=CrEdMFEn5k0cTSsToa3opbgX9CV8gZsk1DiYg1ZH4mWzORZysdfs3k3FpQNKgMfi65rLHQzjEUOuKe5SQ0Mu5OvNYLOTlglquUvr67pOY3qvoJCg_JeTaQum1b__Q9o3tdf7lQvEqvKrii6-PkD-b7ny-p1WGDhrQ38KbPv2fDrReASShQqbB5H-Nkcesqajs-j-mdGM9XKw3YhwG8QRo6c4GyTNaEiPnKpbv5U3uSrSrXgeoDL_6h5TCJvGJCSYECmq1RpnMrudvj2gXwwsEnlUQ0C1eWKvmpEtbIqWm5_SVi7oxNRLit7qTjqLwiyC8ct5A5ye_8524i1t2XX0RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جانشین معاون سیاسی سپاه: سردار شهید اکبرزاده از برجسته‌ترین راویان رشادت‌ها و اقتدار نیروی دریایی سپاه بود
🔹
عزیز غضنفری: این شهید والامقام خدمت در نیروی دریایی را آگاهانه انتخاب کرد و با اخلاص، روحیه جهادی و مجاهدت مستمر، عمر خود را در مسیر دفاع از انقلاب…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/446048" target="_blank">📅 20:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446047">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDlS_rsyyGHyvVlGqv9vfGYuXBgjIcHuEp-CFTb4AwXjHngKkYq5-imb6FlX4-WybQM86wior7QM7RndoBbp9McYSILQ1lFRIq-X40s_uTYdv6P1vVNOU2hbx_WaK0S801tc6bjBkiKd_V2-oSnlRMk7EF2vDhAVRvQP08amXHHWLvT6OB9GiWdfEX9Hvt5YUHrbWJkCw108WLX33bTGOvqsyH6WFIfOz9gr_NSv8ioUGh0OmYGpxtjqTmZjuzWlXAC5n08TfCdTzpuhKrhzOrpAdocc8Wg_tyTQUbYvX5cDtIyEpNdailtleEHdQhoBpzlstn0xLIgXPjmd6rQ86Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
آتش زدن مزارع و خانه‌های مردم لبنان در دو شهرک بیت‌یاحون و حدّاثا به دست صهیونیست‌ها  @FarsNewsInt</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/446047" target="_blank">📅 20:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446037">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r5pPRIxzeKDw8S1zhATAiHZ1zic_xMuiktUxtG3VpexR4zo_rzyBbVvbXonhan2aBqmVkYL5o01gzqHjtBZEiJ_1aWfw0rG4c8ke3_FhquopHqzMl3y0TVfsBHSZLYSOqYgxRNE57iXxEGJW2os_EV_TkjBfb-AOBME6v46TnJdWJsk9eNnARrBM0RQMl8TfmpHcT9XYAUZgKEOR1veoVNPXY4s2191aDZsbj4w_TPxUapRwzK9iRt6cCUj_JIa8-BjJk_mxWtDHhDil9LSNZL8D8H7xShZfSImXExtk3qe7ebNjPkScJbvXbthi8BYaBACw-3S0_H9PTmAkfda9Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sPcNRme1QIYvo4W50wnjqjPhME67pCDMLkG2dHIRz7LM0xP1FelxqC47jjfGK1Y7sc6CTx0vUAgTkOzrn1zHMjMZOHZYIu5XSBAeZZAmHRrqe49l32mocnsA5k_hHm3Wr7bZUFT49zwnQ1_kL9SiJ5NIAkpkdQy2tnIddU6_E14PSezVfxm5YUy_86LUZdRpFT0s6ApKyzpDVQceKSiqCUUSv7TrVUYQnIsIrtUs1VTNTkDSFMIlgHjySS4PwIyIVU8FKbq4M1GNL-ILqqp9J7fyDWC_c5ftvUnxFq4Ica7ZQWHSobn9NcA1DKxi5Ya3mqsUz0M5CIpynCl0LONAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pSBlNAtJtfFiYCSce3buWExowrDyhTegSFnmHCZ-KIkvP3rg7OiGRcsHAObcWhwIKf5yXjHrG42omkkYfr3epYduCNv1fWJfb2Djr0mgRdcC8eQV_NZb5buK-ltei191ign00J3iT998UwqsU1i56CYQk9l0Fs3cIZqNCjXLpG94al1n83NzcWxw74IJaic8SqDL55fZWMtKLGKu8hNKaxE2lHWZuuTgI389VFYCO1Xu9_jXjqFqu4tne6nrGmjqORU-yjvVeMrGDIMxlWZXwC6rs9aP7XZ58jM_Fz17nl8XteXLTVNjk0TIJyCYbiLGlFXWSkt406YOv7i9mrx6KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bpFLfyhReK_q2sGDTQ-rtmXfel7m1NWT9a4TFx0LKRaveWKxNE7BmlFFAShVEjiMrWP3nZopaNMcCU7V1Fgr6MuMohB8BoZDqmPRoP4-gpCdOYaIPrSHMKd_uGys5yRUTZM_u-neyf1isRp2I7T3WTjDBx1h97a2JxkHhT7FI89kOjYEGsvsuZ0m9m460wrq0uX1gC8-8aXHj6NlMr0bh0TfjeDLgjYbFhE6iQf34Tr3W0yiBYrTfPMcP4ft2HgaE6RXp_hIz_rU3HTqdj8AsAuqBuAVGGmwtU4WShQmYCQk7ad2B9PjzTsVcyatTm4disA2g8BNGAIocxqKv7LnWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q-uG214fOnyTuTjfOj6638iqZRwMQJu19YLOGBdpdUNxO4BHbKMx9ufww4oVVmUokdDGRqw-Kd9_pinqM7RRPtPB1Y3z9IsVGCfvovueLRvqLhrXA0cjQ3xWo5X-tUthXHqUOg8EeodbOdwIRog6IY2zorVHg0e_G3Gjdy-rpWo4r1C-Cq_GdEY8ZTVraaRkcOwD0dQgU5SErLkJMJ3lZUoGI5OFTA8gYXpPFItcSaR0DNFDeijWozvmUW79CMT-5PnUuKKDivZ-HUikO6k3BkAiFkhTe7PSJewEsIZSm7XWCeC3cS1tULo-anF_fRppc2DljIuUMirxAl2j2iGu2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FrZhZIUVUpaduGk2sNqzdPL05CDRne9OZ41kEEkbS_t2c6lMV_QIS3PusXORRRNMNRqBRbp8-SRmZNzyCLTq3Uompb77E-ps5u-UHrWZ3la2__4TNviQbZxGzyKyVi-uUF3ajtHLpn1elK4wrTNg6MDhk-DZQKVXnGdvKqcq3ZgkuA5uk-8Dpw5NJ9IHi4PJlBJxR-sCsk2ymXFuRXSUn7gcfcpWGeJnLIQaFAYBA69l7PnR1FQ6VDvJR71XpFz94WNKs1yeY0-QDjq-5TFjCslDADlZfhWJPRe3_SktGxvkejyXoYqEHFLtCme1UH5O_h3grdYbqT_Ixa9JXyWk2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qeiqb_ZvtXcscdYjb15b3FdfM1-_VYY6vcaY1vw6Km5LDKDdYmj67Mdn9XGf9PRl-kpnIKJFSc8ViYu99B2xY0oHhDorJnWfTiyOzCEX2zt8lmGPnOpGdpnM-EbQMpkMUXypw2_zgENpeGLKnahL5hcetfg6bklu64UxpSp_jgQBk7-lGL61r6Gvkjqpx3Vwe1rs3SsFGcgrSd_EnViy0zJ7toVQlHJVe8UoMveD_-ISmt3PEUAPZYXBIU8sPkc6yqGXOQJnqaRSVTa5871YQqsn6Jj0muE3-633ve3GEoPxW_iaeD4ICrw7noBVAUNDELrjOdGRj3y2vXNLg2VfFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQ3417wpnVCNYzEC8rTmT2y6qKZu1q35q3F2GQ5g1mnzCKv8rkb3wBJj2CTMRiucDPaQEdLUevIrlU_0vw2Yok18dgjqizvG8XX8BF47Xsi0NjdKWSIxLr6Axr3_6KbjuhHH73V1KtV_DhejEv40-WrtHaHftTYzXjgkLO2mgK2hGOFPGP1MTtwP8fGTZ8CT_xqt6lNcfHH02WV1DVveotplpm_R0NLeKr4e6_86-BY_PgxwzFPbRB5bkMoQxTAyeVE6hygzUusDfjnHv4qNQUGOhI-FOYuFrWAf2hK3ySaheQ_L6qG49asB7R-WoQuSeT5-hiHCqNWsBvAMKANqDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YJ2XZI8tneQAqT3CJaAgW-p5juEFBfg2_XiwephdNP6Xut5sJyjzdDx8xw6le2jTaBgtyc4l31ZVyWZXocZnphKccacrcBK8xDxOV_MvnWt0tDzKaVUAOpAzcq6c8oc0m3vgPaD6J7HIZIfnB9xrG_bfNmhsm0XpzklpLQTqD8a-yLeYtSH28-WRLniM21KBAmXRarkns6IVOyJX5_5IMD3efpG0YLdOIQYI_wU4V8n-q31HTe_nLGH3RAZb7Sq42fB44b_RJBlO3DUuGyftdH1RH2xUpcrFMmhqnYqcD_eH1JA42opgDG2HlYSZh6ItK-FFcuVuJZk2IJ6TEnDDJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V2l-OdNNsmkm-6eErW-Bo3Jzbn_u7T7EG1Ev6z9Qo0t2EyTmt7YQvw4ZPfM2LUr2Y8fmyxn3y9l6xfpVFg2lc7rHx-CBxPWzMOc1FIBa2HylYvXC70q0_4jepYtZ8YJsLI4qEAnTF3IpdQJMHSXVLUts0HdSzzv3Pj0xYGDgU5i6Q6MBkLXJlENLtKVeSYbe1K4brzzMTlBPMzspiMfePdvGGZW9MBVhLtCpA9WBtwfnZs2QYbVDO2_vrlj4ypkWTVEt1BB2S_DAkgWxWiefyVQ5TjP3Rz-yNnSCfgTXwml4pb336U6yyBtzHgzPgm_hlBjp6gqSLwWGnuZIiRh8Sg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اینجا برای میزبانی ۱۰۰ هزار زائر آماده است
🔹
در آستانهٔ برگزاری مراسم وداع با رهبر شهید انقلاب، منطقهٔ گردشگری عباس‌آباد تهران برای میزبانی از ۱۰۰ هزار زائر آماده شده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/446037" target="_blank">📅 19:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446036">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بیانیه جمعی از اعضای مجلس خبرگان درباره تحولات اخیر و مذاکرات
🔹
جمعی از اعضای مجلس خبرگان رهبری در بیانیه‌ای با اشاره به پیام اخیر رهبر معظم انقلاب اسلامی و تحولات اخیر، بر لزوم رعایت خطوط قرمز نظام در مذاکرات و هوشیاری در برابر ترفندهای دشمن تأکید کردند.…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/446036" target="_blank">📅 19:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446035">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQlnxN5Izbdf-8pvFbqhof1XONlDkKaFfBVXp7cQx06tzJbIWWRPJYIHLknopLyYDkr187iWutDhRt1cg-X4saWGKh6IdH-EvcDR0sRcdnHovugOzPtgRup5nsaNaQKPT4VaIwidFY3vVycDzqZezgURL4OJWIF8F3MJDXdbdha9PzSC_H0j72FQoohe7z4ZxIxTGjKipQag2ZT95pdRZyOdwDV6MbrLaMVI0HU28G72bt6W2np32M4tkKaoi4qN0FcrWENcoYabwKwlM8QHMVmSlWbX1AAug2_zQMZtRSwlyOPJwmUHjPMss_6HmUURBi0w5tOX4XQFhMukDs5SkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
دختر سردار شهید اکبرزاده، معاون سیاسی نیروی دریایی سپاه: پدرم پیش‌از تشییع آقا لباس شهادت بر تن کرد  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/446035" target="_blank">📅 19:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446034">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار لرستان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f1e3a93a.mp4?token=d6rhbnTKwmgwPn6NoEaGEXfrLMIztCyAxPbTI8-4nSqLF8XfJgybgyVUby_hnIehaN-PQGsoe4snTNW0jS1HCx-rqb7E_IWbAyPrRzwbxA8ALu3jUHabLbUl-dILXjrEuMMlvuWU4YiFZks0bv1rFu3nhe8y4Sm6PH2-y6BvfUUm8DeCpHKi2qLD7qamokdnlyel1xvGIFYJLhONiLvtcq1Nx49RYo-ZNhgARmTFScdguaxuhQ_E0p1Ufr9Gyic0gjXlUZ12Ml9iEBI5ARLYC8r3fhb58BBIQNVYaCH5T5UWZYsitpOgzZuxCXPChfT_foOVbQviG0pJFX0OfRG0uUMFHXH746-HfKVO2EmWWCUWExgSOjL8rUVfJ3i1JHIL-dYVsikK_qo7Lpt30_4JU9DO0-gZfdocRrK49UnKwYtpKSCOde8nSLua46UQWgj5SWs2NH4p5GhHIlt_VQDFs0VSy55baRtURVEs0Zk5DpLUhwKhB3SRFEqLDi0jamP1AmSWNPf2zsr-vXMYr5l9-YF7xoxBB1AO-d_fxxumKEjLkfapdnBmJOr9m7blif-cmMBLbVZ63wQcnYt9lKq-m9BjZXtnrwq0wBSR33fWc0JMYV5ZxOmAZHVyTx7vhbtd2zSEA4gX4p56JZUJd9ZOfbFnNIz4zfa5Ccisz79b2IE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f1e3a93a.mp4?token=d6rhbnTKwmgwPn6NoEaGEXfrLMIztCyAxPbTI8-4nSqLF8XfJgybgyVUby_hnIehaN-PQGsoe4snTNW0jS1HCx-rqb7E_IWbAyPrRzwbxA8ALu3jUHabLbUl-dILXjrEuMMlvuWU4YiFZks0bv1rFu3nhe8y4Sm6PH2-y6BvfUUm8DeCpHKi2qLD7qamokdnlyel1xvGIFYJLhONiLvtcq1Nx49RYo-ZNhgARmTFScdguaxuhQ_E0p1Ufr9Gyic0gjXlUZ12Ml9iEBI5ARLYC8r3fhb58BBIQNVYaCH5T5UWZYsitpOgzZuxCXPChfT_foOVbQviG0pJFX0OfRG0uUMFHXH746-HfKVO2EmWWCUWExgSOjL8rUVfJ3i1JHIL-dYVsikK_qo7Lpt30_4JU9DO0-gZfdocRrK49UnKwYtpKSCOde8nSLua46UQWgj5SWs2NH4p5GhHIlt_VQDFs0VSy55baRtURVEs0Zk5DpLUhwKhB3SRFEqLDi0jamP1AmSWNPf2zsr-vXMYr5l9-YF7xoxBB1AO-d_fxxumKEjLkfapdnBmJOr9m7blif-cmMBLbVZ63wQcnYt9lKq-m9BjZXtnrwq0wBSR33fWc0JMYV5ZxOmAZHVyTx7vhbtd2zSEA4gX4p56JZUJd9ZOfbFnNIz4zfa5Ccisz79b2IE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پارک ارم در تب‌وتاب میزبانی از زائران بدرقه رهبر شهید
@LorestanFars
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/446034" target="_blank">📅 18:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446033">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c60ef9d66d.mp4?token=Z26CBEBoPFbXUeZskU76gzieps_8zEj2m3AuDK6ab3irPTSGleIU-KkcF7qX-SaVz0oE4QkQqjSL6IqRD1BxbAzUw-ZmMOJuzX78DkMLywGHPcZz2sKKgTv2_OmFeoJC3dQG2uN6muKaypVYPMdMjs5LyopZZR1_aVmnyTdd2yFOztBRcu_ev4PIaDRJhkb_fCdG3S85cRFmhr-AYRENr9mHH0FpoeN0jzRmL_47woTQgUZ3T-PSC6zWJb1gw6XdonzfF-9ctu4cxUOpuyD2O9AkUnSWCmlVONWDIp3SwDyH4qr6Yto8pd-oicH4hKMcNklez6OI-aI4zZNt9lerog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c60ef9d66d.mp4?token=Z26CBEBoPFbXUeZskU76gzieps_8zEj2m3AuDK6ab3irPTSGleIU-KkcF7qX-SaVz0oE4QkQqjSL6IqRD1BxbAzUw-ZmMOJuzX78DkMLywGHPcZz2sKKgTv2_OmFeoJC3dQG2uN6muKaypVYPMdMjs5LyopZZR1_aVmnyTdd2yFOztBRcu_ev4PIaDRJhkb_fCdG3S85cRFmhr-AYRENr9mHH0FpoeN0jzRmL_47woTQgUZ3T-PSC6zWJb1gw6XdonzfF-9ctu4cxUOpuyD2O9AkUnSWCmlVONWDIp3SwDyH4qr6Yto8pd-oicH4hKMcNklez6OI-aI4zZNt9lerog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از مصلی امام خمینی در آستانهٔ وداع با رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/446033" target="_blank">📅 18:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446030">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jt_b7CWpzIre9i_APyJlEDTJU34Ih9BAHFANvqzD7A5GEw0E1ZzuA_rAPc0XIgT1KxcAfQPOOUDZeUH0YiIGKNyhNNM22RZY8jq9S7H29AP3R-TDUToi2JMOQlvNF9JwJqhhSgY3v9aKi1dOP9pjQxztD_GovW0FHBGOtK2SNlVAQYafED8ZJqqv9xPaMze3FFgMt2XOJsnNjBfPQxFDcqT2ltrxFsp4bSpiqlLyuaEG2oAwh-C0Dt7dPvq4b6JtG3HTgCWiSFShewIYi3QJ7OGhSY2N4A7N2SZyKPC6wnfx8q1wyqCIrxp-xYEgVTBtKESwE7LL17vzjT2X6P7oFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ak-H4Tirb_GNvqKf_5v2-avRi_Wbq5L5rKmPSRpXYeYiFZtZ-p44DPNFCeLsxxcCZ8B5nbIckgVKreXpAVKNb_YbWRJViEi0TXUzP0P7DePT5xb5T6u2mtG1r-_1jWO4u23ACmF2fqDCwUI1jVWDGf322HpWSbzV2nrdKUfsnaCHdppPPKXPYLicpiAEKs5HGSTQyhwryZ7oG2GmWo94J9D1BSMxJuCSorGndaedlhrINT4gelgGVbp-Q0paUVfvUYyw5DIi6bsDyKETPdRvoQxEAdSbGBmmqPPmsgoj3ff7iwXevwHdeB__Dqq_jPPNCydsOtaLvibSs5bkff3Hdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WbXzWNi1bM-DQ8w8FMdrQJrdEoVA9SeHLaVsjmTl3ufKchUb-4QXGe8IvXSxtOuhSnMR5DmjgH3tXxnLufvWb6RQ7yrs9axgCEZoHcquPH2f8CZscANkFK0RYHFIqmgsk_yRSI6cPxo1PjZ2d3ax3c1umQiCBdc6NjVUW5o3e_28dYx8RLAB4W69O3nbrejDvtWihdTSpZWN3Hws1RXBsNtckeDY053Clhkhr34eXsHKM2l12Qqls7IMRfVbGQyknHSMjHip7pr2xNdiumC0lTWPxYlbkj4a33bVL_mRbipGmVL87cOXbcPJM555iFiev-wQiBaB1KyRP6qxm7oScg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وزیر خارجهٔ افغانستان که برای شرکت در تشییع رهبر شهید انقلاب به تهران سفر کرده، با عراقچی دیدار کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/446030" target="_blank">📅 18:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446029">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f52aaac282.mp4?token=ObwMeKAOW8tojbDHU2KIrqLDvRMTU79wck6bk51ebX52SHRaqguoxcmh80TtDhK75-lvpYxSAUeOqyqjTXvskj0d0uruAKvELbqnSUkEk9D2axmfvzhnhQrJX29xLCTHbaD1btq3zNnOvMNWe84g5PO45xI6qbHLKGODErHMCSl_ndrcc0Ni20jgDFsu_3k7iQoXXfJ5ziM9aIhfcNu4CP0Pxk3TsPrbr5RO3yXSF5_u8TwILmdWjQicLILJGHZ1AY3UjlrTiwtK1fQ4M0o-gqw7S26JmCyzpta-Rywmw8ngVrNpfTGp3C2Y_9ERUDm72qgvGkFfJ90EZu0MdSlc-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f52aaac282.mp4?token=ObwMeKAOW8tojbDHU2KIrqLDvRMTU79wck6bk51ebX52SHRaqguoxcmh80TtDhK75-lvpYxSAUeOqyqjTXvskj0d0uruAKvELbqnSUkEk9D2axmfvzhnhQrJX29xLCTHbaD1btq3zNnOvMNWe84g5PO45xI6qbHLKGODErHMCSl_ndrcc0Ni20jgDFsu_3k7iQoXXfJ5ziM9aIhfcNu4CP0Pxk3TsPrbr5RO3yXSF5_u8TwILmdWjQicLILJGHZ1AY3UjlrTiwtK1fQ4M0o-gqw7S26JmCyzpta-Rywmw8ngVrNpfTGp3C2Y_9ERUDm72qgvGkFfJ90EZu0MdSlc-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم ایران عزیزانشان را اینگونه بدرقه می‌کنند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/446029" target="_blank">📅 18:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446028">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fL1l_B0tH-r1x-SEB5aofBNfi82r_JFa-4a_UHhE0r6ylW7uTKmNOefb4UXPGcTq1TrEGZvj_9UPJISd30nAKUk2bBZ1dGHsuqBI_rkoS1f1XMqimFN_Fb5BFk5e14pYXn6hhlrpbQOS_HTgMtwthaY5g7OcC4xdY3z1_hXnb6Iv2QrOXsYZCkwLOHbnlSvd4j-1acqw7VQBBmgJeTEnS50gbEAp7QtaKqBEPmDZiagWe1A08jN0oOK2yvvSRQ5sh-aDf2V9LZ2e6k1Auv92gA8oBVxuSfpqquubgO0Y06Ea2OVn8sx_FyQhwBx72Tg8DGIXz-iwrQ9DZ582Av4McA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعدام جاسوس و عامل شهادت فرمانده کل قسام
🔹
دستگاه‌های امنیتی نوار غزه از اجرای حکم اعدام جاسوس وابسته به رژیم صهیونیستی خبر دادند که در شهادت چندین فلسطینی از جمله فرمانده کل گردان‌های قسام دست داشته است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/446028" target="_blank">📅 17:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446027">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🎥
جزئیات حضور مقامات عالی‌رتبۀ کشورها در مراسم ادای احترام و آیین وداع با پیکر رهبر شهید انقلاب
🔹
سخنگوی وزارت خارجه: از صبح جمعه ساعت ۸ صبح مراسم ادای احترام و آیین وداع با حضور تعداد زیادی از شخصیت‌ها و گروه‌های مردمی تا حدود ساعت ۱۲ ظهر برگزار خواهد شد.…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/446027" target="_blank">📅 17:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446026">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9a3266a08.mp4?token=qZp3p2_PAs7E6eAvsZcd13EwafJrxoUHpRVXDMweyLktQ-mHorvM60luNZgHqLanew3lC-YK9hVjywDpfQKxh0HZnsjEIcjjgQIkepkuHedoEG9Vt7UAcCyWa56UnpTzOI4b5Nqkl9SUIwc34J2J_01ruC5mXvpNFLfGJQzQ65vc3IWr8-WEZ4QSemMFEhtvH6JVTirb1R_ubhIZ9Tu-oysJ6HesCqoymHOMarqjguuS9GTOXdaTn3V-YDvAUsAapPgn0bSEBPbBB_q94Jb0OMlzQmst18SpUJCyc2bL3-RDRiz2JIen0M0uq4GQGmEAW9ZOmkPLy_q5DYEtS5rqmoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9a3266a08.mp4?token=qZp3p2_PAs7E6eAvsZcd13EwafJrxoUHpRVXDMweyLktQ-mHorvM60luNZgHqLanew3lC-YK9hVjywDpfQKxh0HZnsjEIcjjgQIkepkuHedoEG9Vt7UAcCyWa56UnpTzOI4b5Nqkl9SUIwc34J2J_01ruC5mXvpNFLfGJQzQ65vc3IWr8-WEZ4QSemMFEhtvH6JVTirb1R_ubhIZ9Tu-oysJ6HesCqoymHOMarqjguuS9GTOXdaTn3V-YDvAUsAapPgn0bSEBPbBB_q94Jb0OMlzQmst18SpUJCyc2bL3-RDRiz2JIen0M0uq4GQGmEAW9ZOmkPLy_q5DYEtS5rqmoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار جوانی: شهید اکبرزاده زبان گویای نیروی دریایی سپاه در جنگ رمضان بود
🔹
معاون سیاسی سپاه: شهید محمد اکبرزاده در طول جنگ رمضان در شهرهای مختلف حضور پیدا می‌کرد و به تشریح پیروزی‌های رزمندگان می‌پرداخت.
🔹
حضور ایشان در آن مقطع، به‌ویژه برای نیروی دریایی…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/446026" target="_blank">📅 17:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446020">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار استان فارس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7-IbwsVEKW7axjvRhgNw8BkdZEv9omb86PGrJPUrQnGKXaP9UqFUsVGzGDhswI8G0nSRGdpXkEt1xnHLAMUb6A2Y07aIR4Lufsb6agYFd3F1lIGDM4YH4TWvXFHgOwItNBvdQCy2QGMdugPXOu34lQGMF56Va_gJIx8M0PLo3BKzWUf9ysgWmoaiAi1bllnPiZZEk_OYCokMmHJzDsBcgdbOpkYoQIAW_E7_yVgTIySipSay9YQzCoEZMj0TBDD19YjKFzyU-6ajrX5zodWSgR2tko3lD67kG4PxmQ9A1zp38gdWmDOND2G7cURjL7r8yt1FwpOJEKq3waoVIQsMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fH3sEDaO5iqgLyFDhQk6EgdA2qHuPGDw-xEe43kfzUmkw4abyLSwje3IQNNXMU7VDZm-N-Rt9RR-GQh46bWbW37znZOAAfs_i9QviWeTEwmRlq-xO3dxsntCw7Vyjvpa3ZHoP-oD5IGSpCq5uX9wv64afo6MO31QSQxumoUfdpSZin9WeGcxmN1XUgwuZCh6jHAnXI1rfIZSku2qrW7foh5M08Yi8EtexEbv4TokUNhFSLItUbNHWdpfFLiog26tjeXhD2oG-9X-jASNEGdlrCkNNeAIalv0AvwA5qtKOfKN4_C7siJq5z-rce0rpI7jmIABJ5r0x5nXEgQ14r1X2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UkueUqTqk0fqQdYqyU7vrfNW_3yc_PqYCZ3UlpHop3Xwvfk7Ngco9A-FeIn7FGhm7rqMMyFZor93vUbSu98MLbhWliOb5YsWyO8ogxW7ddvhpFGJJP3MvjF9OIvQeFvz-WbYkzdKwL-gRS8ZLTNn6161qjqYWzRsa8Q0b98y4cYeqT4guBHJFuzrRT9wkmz-7K8cUbBLrI2Khp8mj0OjK_12Uw8C_kyc_cJHkMDirpz7ur-P2z4_Ao-to44byMDIeJTojIewvnTq87vkpwuMAcptLkej3PvbIZHq675Bc59kSB-Eoi5Hr2KQth0M6hX3fmQ77Q06MMMYiXQlj8YMIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EdX7HkGEMFpjzXd_raOIbS-5HvENliRrxhr4ijjahgdeirxkqWMcDojZcRZSPh00jmm0iq5pfmZREjih_yCaxsthlGBkMI3agOnK5I1N5jdxR3SVQC0T9Pw2_NczOsdkjnfiSl2yAQHq0vYYY_xepG7WvWeGEcWOyzU6SGrB_tvWcqAeqaXYVQo63NhW64jX_2AQ-bPAqChcpjeXET9xDAuQM9xyVmkl1FolADABa3913ej3QTwTGQX7OxZg1SytjG82erWLFDIMJj-jy3KRFGZoOqYEdH0trjhqDcvJoelrmv0MSLMyhnBiCuGx18tWIB_-oslt3WRZb7Yh69cOSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aifnQ8pnha6Nk52oUUzdiV0qPriTHlKjmYh-W73IS9sKJ54znsYijhO-Cyiq4oBUBNug1SCXZWaCW_k4Qb12VsKWeOZhk4vGo9gPwZaoQtR2TuhGPrgdCEcbeaRWoRNxYCGJfF_U3qJ9zK2vsK4d-lNiPjqwRckbcmcUXWs4UCqqK8aZ2bcWAo_CMNaWYSVcNYoCt_uzRFFrE_kF0lLUoe-rIP4usMFce0glSVzL3aZLZIZSnZFCdCd6kUgdKYhP-KnF4bB8GlIHgCBsWO-BQ_mGCVVlVV04Hu5knbDUrjhAxQ_teZAPJnja2El-pZIE5tkJkTIXjyFlcBJpwkmPpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/APh4rdg1VPXC25FUWqfRy8iPi8t37KZ54lYH1hsdcYb3_CNBmA-HxQ9moHDzJurZUIX_FXCGljYL2Q7Z2uwME6yAhKgrO8O1hXr67sEWjsnufAgduLBQB5sxE7V44LsRNLmTBlQdrnlOVJ23AWAPl5ul2d_92HqTw8jYvEN9sbH0bzcvlIC3o2DwusxSyuEjfvET48Zzjnu40XSe8plHFYqfC6_bwQkgGyYjEyVgpTcUb2mNfD3EcqC4GF85Ok8JgTF7x2zt-zl7slyrHx7DIxVofJ6MtSwNKteJx-Vaqeac_iY0ABDHAQUEZ9teaHfzA7RoD8HmepVDBiD7BIRSpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌ها هنوز آن سفر به شیراز را روایت می‌کنند
🔹
در آستانه وداع تاریخی ایران اسلامی با قائد شهید امت، هنوز قاب‌های ماندگار سفر شهید امت در اردیبهشت ۱۳٨۷ به شیراز در تاریخ این سرزمین به نقش بسته است.
عکس:
دریافتی
@farsnews_fars</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/446020" target="_blank">📅 17:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446019">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ed06b2f9d.mp4?token=J2NVrjnykMjGX7N4ej_F6-GpbHIqShc4bZ104nq4a3dZxZdZDy8gu9eSPrlE3E1Ir90ncSR2l3KD48BuLteAsBHnotwssCr5sGaRTuW_GhnHQOvEU3xYqszgkn2SD74Nit_82WjYKRZvWlgMnrBf8940jAGw38eR8gLmQpLoC7fOjlIQ3H4BGfCXqZdESQINrvHynrpgZuFpQjmxsmJvP_WLtjaW3TVUxYYWlKrJQEDKGAkhwwJq6Mva0nFJtZXYRjWT4Bv7RSFyczr6mhxObHTMQtpI1foskKWD5m5OPxAUOZ02nPGYD-kdRGOwbjUsoB4vWBNcUHmkApSZUyA7XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ed06b2f9d.mp4?token=J2NVrjnykMjGX7N4ej_F6-GpbHIqShc4bZ104nq4a3dZxZdZDy8gu9eSPrlE3E1Ir90ncSR2l3KD48BuLteAsBHnotwssCr5sGaRTuW_GhnHQOvEU3xYqszgkn2SD74Nit_82WjYKRZvWlgMnrBf8940jAGw38eR8gLmQpLoC7fOjlIQ3H4BGfCXqZdESQINrvHynrpgZuFpQjmxsmJvP_WLtjaW3TVUxYYWlKrJQEDKGAkhwwJq6Mva0nFJtZXYRjWT4Bv7RSFyczr6mhxObHTMQtpI1foskKWD5m5OPxAUOZ02nPGYD-kdRGOwbjUsoB4vWBNcUHmkApSZUyA7XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعر افشین علاء در وصف امام شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/446019" target="_blank">📅 17:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446018">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Apzle_vVDVZm0vs1YWksS1CULuAeVuiWaSeCBbbP4WAapre0BxlYTSLFRXHeq0vpCp2x6-vFRETcwXXI55b5xSAtPLnnY7P_6Z_JLiWT-RlpL6tK9WkRlFjacyvOZ1PlyXxT9qa4fn8WNpDd1s_8QsL-TYs0xUwbndes0__eOgeMoNpZyNyGHKAp3sBtpe6cmYrtEA6PCG1dvmyS20dALv-L0ia6E3UCGEtydiQxeyPJw5B57P5Jp6fAIp4GxbtxE2lF21a7Nclnaz1Dj23Axi0M8JVynF4yiCuKuTAIRL82TuX3DYDACRA6KQfeuuK0_AxrbqS1zVipKahWm2Ncmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت بدرقه با شما
🔹
کشور در آستانۀ یکی از متفاوت‌ترین و پرجمعیت‌ترین مراسم‌های تشییع قرار دارد. دل‌های بی‌قرار، شهرهایی که آرام‌آرام رنگ و بوی بدرقه گرفته‌اند و تهرانی که خود را برای میزبانی از خیل عزاداران آماده می‌کند.
🔹
این روزها در شهر شما چه حال‌وهوایی حاکم است؟ اگر میزبان هستید، برای پذیرایی از مهمانان چه تمهیداتی اندیشیده‌اید؟ و اگر راهی تهران هستید، از آمادگی برای این سفر، تصاویر کاروان‌ها و حال‌وهوای شهر خود برای ما بنویسید و عکس‌های خود را با دیگر مخاطبان فارس به اشتراک بگذارید.
🔹
شما می‌توانید روایت‌ها، تصاویر و ویدئوهای خود را با هشتگ
#روایت_بدرقه
در فارس تعاملی منتشر کنید، از طریق پیام‌رسان‌ها به نشانی‌های
@Interactive_Fars
و
@fars_ma
ارسال نمایید یا در پایگاه اینترنتی
https://revayat-badraghe.khamenei.ir
ثبت و بارگذاری کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/446018" target="_blank">📅 16:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446017">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">درگیری عوامل انتظامی با تیم سارق مسلح در زاهدان
🔹
فرماندهی انتظامی سیستان‌وبلوچستان: لحظاتی قبل، عوامل انتظامی با یک تیم سارق مسلح در خیابان بزرگمهر وجانبازان زاهدان درگیر شدند.
🔹
در این درگیری مسلحانه ۳ سارق مسلح به هلاکت رسیدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/446017" target="_blank">📅 16:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446016">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
انفجار در دمشق
🔹
رسانه‌های سوریه از زخمی شدن تعدادی در پی انفجار داخل یک کافه در پایتخت این کشور دمشق خبر داده‌اند.
🔹
خبرگزاری رسمی سانا گزارش داد که انفجار در منطقه حجاز دمشق رخ داده و ماهیت آن در دست بررسی است.
🔹
تلویزیون سوریه: این انفجار در منطقه حجاز…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/446016" target="_blank">📅 16:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446015">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRvEqwcNmHnCOyOC9A-t02-jSEkaieooYBZO96PCk_7jp6lHD_KcYUUHqzHeexbBVVqTFa2mXle8kX9md8alclQmvah3CufLLyhPmMyXhtD5JDFe0TKDXXfqkqbiuDv9xrTQcHjn191OsfJI7yC2V5VaiXBxasbBDWi7S-0RQ8Q2zoMmLg3mZh1_aGejH1H4ZrsnZdNjLhRDYhZ-i4TyGMNNnxdSOFYcpk-H-ktDjiM0lA2eCXheEtb7maQ8nv6fzqcLQUN_1mr842Q5teEBZGb9xQr1ncb8Jk1xJnvqptoN3JSBpvi5te-gDNSizpt6xL4S9MTITaARlWYI_bHyAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
جلسۀ ستاد برگزاری آیین تشییع رهبر شهید انقلاب به ریاست رئیس‌جمهور  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/446015" target="_blank">📅 16:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446014">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3e2e685bf.mp4?token=gEhs4Efj5bl-xiyZY3dL3pgmojxmKocG1rHgmolItnljxykcB_yG1vToRmUY-I-oBiGQT8cnJyXUxkh_IQ7IVDkCr1mQn15u8hNOTmAzJAzfjoXdG4gg3WwpYq3QTlxH87nLm7cqNUHRsnKkz1P-mQokuOpgY1p4qIm7ILBD1fz2ZRp7c8B5BvRI46fQJlIrFQ3XAsctqL1D0JmNLGCvdc-S6r2TrekgekSKOJtRKoBSMTBcXt1nPw36ygFFBZfS00Q8NexiZo9ecDn6vygRTmHBi0HTwbecHDg9J3ZpclC9Nhba4urDRCmgLr915Qqhz4XoO8_voc1CBnMn8d4pDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3e2e685bf.mp4?token=gEhs4Efj5bl-xiyZY3dL3pgmojxmKocG1rHgmolItnljxykcB_yG1vToRmUY-I-oBiGQT8cnJyXUxkh_IQ7IVDkCr1mQn15u8hNOTmAzJAzfjoXdG4gg3WwpYq3QTlxH87nLm7cqNUHRsnKkz1P-mQokuOpgY1p4qIm7ILBD1fz2ZRp7c8B5BvRI46fQJlIrFQ3XAsctqL1D0JmNLGCvdc-S6r2TrekgekSKOJtRKoBSMTBcXt1nPw36ygFFBZfS00Q8NexiZo9ecDn6vygRTmHBi0HTwbecHDg9J3ZpclC9Nhba4urDRCmgLr915Qqhz4XoO8_voc1CBnMn8d4pDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده سپاه تهران: آماده‌سازی خودروی حامل پیکر مطهر رهبر شهید به پایان رسید.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/446014" target="_blank">📅 16:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446013">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">استقرار ۴ بیمارستان سیار نیروی زمینی سپاه برای خدمت به زائران رهبر شهید
🔹
معاون بهداری رزمی نیروی زمینی سپاه پاسداران در گفت‌وگو با فارس: چهار بیمارستان صحرایی تخصصی در شهرهای تهران، قم و مشهد مستقر شده است.
🔹
دو بیمارستان صحرایی ۲۸ تختخوابی در تهران و قم و دو بیمارستان صحرایی ۶۴ تختخوابی در مشهد مستقر شده‌اند. همچنین ۲۵ پست امداد سیار و ۴۰ دستگاه آمبولانس نیز در کنار این بیمارستان‌ها برای ارائه خدمات درمانی و امدادی فعالیت می‌کنند.
🔹
بیمارستان‌های صحرایی مستقر، از تمامی بخش‌های تخصصی و فوق‌تخصصی شامل بخش‌های بستری، CCU، ICU، اتاق عمل، رادیولوژی و کادر درمانی مجرب برخوردار بوده و تمامی تجهیزات مورد نیاز را به همراه دارند.
جزئیات فعالیت‌ها و خدمات را
اینجا
بخوانید.
@Farspolitics</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/446013" target="_blank">📅 16:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446012">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5b5a61604.mp4?token=PgdX-KEKUK4kQGzkcG9tO0EvTjKB4iJWAQECfp-dmWh9eEylnUBIUPrVnKfB8D0DOWH4ItnHB1h03L7YCSSv2tn686DCDBHUonP2nuZDYurHWB1wsN0pO0FuaCCgFR05AaxllCJ7lQNONasxkoaZ0qvB-x939_0qZ5E4cKMjSwK_qWqoavAN2958Oo77fWb1nntVP92ZX5LqEwIPZiB6jDPaA_yOfJv_hQmsyPLil85l9j-JFiPtUAID1AozmeowG7cfYSVAjGoTypxkYcoFLIG8Ufywf8-weM6-yYVIvr30VjUB5Bk_ZnEt37zi2VWmOlDvB1XdhmcbOob1FkdRcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5b5a61604.mp4?token=PgdX-KEKUK4kQGzkcG9tO0EvTjKB4iJWAQECfp-dmWh9eEylnUBIUPrVnKfB8D0DOWH4ItnHB1h03L7YCSSv2tn686DCDBHUonP2nuZDYurHWB1wsN0pO0FuaCCgFR05AaxllCJ7lQNONasxkoaZ0qvB-x939_0qZ5E4cKMjSwK_qWqoavAN2958Oo77fWb1nntVP92ZX5LqEwIPZiB6jDPaA_yOfJv_hQmsyPLil85l9j-JFiPtUAID1AozmeowG7cfYSVAjGoTypxkYcoFLIG8Ufywf8-weM6-yYVIvr30VjUB5Bk_ZnEt37zi2VWmOlDvB1XdhmcbOob1FkdRcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آموزش‌وپرورش: امتحانات نهایی به‌هیچ‌وجه به تعویق نمی‌افتد
🔹
رئیس مرکز ارزشیابی آموزش کشور در برنامه پرچمدار: آزمون‌های نهایی طبق برنامه برگزار می‌شود.
🔹
امکان برگزاری آزمون‌های نهایی پس از کنکور وجود ندارد.
🔹
در نیمه اول شهریور نتیجه امتحانات نهایی به سازمان…</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/446012" target="_blank">📅 16:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446011">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea1c88eb50.mp4?token=DjaWSo3AyL7eRQltpAOS4ZEGZOivdwUIbh3uonBX4RCRcC4ZspWNi_gRj-2A4tyQNMTQnWnT1qVPvTQu2JMWF8j8lSI7QXeTY1Wu8bpiunWdaNiopWW7B49Pej6OITRvgfnRHaBiUkjACXqX03A6Z8V4jYwUvj1vxF9tdlr_3vdeqH8AdyyPt-_UOXnlUm_w1gQPlcKCL3OO1TonFjPOkZnqhrj34gd1lniBd-96OLZiLq2BwHkOR0931M-V9DUSO4qASoz9_B2kBsCjAxGsZoPmz0Ch2PCNnsTo8ULoLBs3XDtUY5LDpVSrwmYdaU-ih5_74wvOsOfQx19FkJY17Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea1c88eb50.mp4?token=DjaWSo3AyL7eRQltpAOS4ZEGZOivdwUIbh3uonBX4RCRcC4ZspWNi_gRj-2A4tyQNMTQnWnT1qVPvTQu2JMWF8j8lSI7QXeTY1Wu8bpiunWdaNiopWW7B49Pej6OITRvgfnRHaBiUkjACXqX03A6Z8V4jYwUvj1vxF9tdlr_3vdeqH8AdyyPt-_UOXnlUm_w1gQPlcKCL3OO1TonFjPOkZnqhrj34gd1lniBd-96OLZiLq2BwHkOR0931M-V9DUSO4qASoz9_B2kBsCjAxGsZoPmz0Ch2PCNnsTo8ULoLBs3XDtUY5LDpVSrwmYdaU-ih5_74wvOsOfQx19FkJY17Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اطلاعیهٔ جدید آموزش‌وپرورش: برنامهٔ برگزاری امتحانات نهایی بدون هیچ‌گونه تغییر اجرا می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/446011" target="_blank">📅 16:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446010">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دعوت فرمانده کل ارتش از عموم ملت ایران برای حضور در مراسم بدرقۀ پیکر مطهر فرمانده شهید کل قوا
🔹
ملت شریف، پرافتخار و داغ دیده ایران؛ شهادت قائد ملت، امام امت و فرمانده مجاهد و معظم  انقلاب اسلامی، حضرت آیت‌الله العظمی سیدعلی حسینی خامنه‌ای، (رضوان الله تعالی علیه)، آن بزرگمرد صبر و مقاومت، به دست دشمنان کینه‌توز، آمریکای جنایتکار و رژیم غاصب صهیونیستی، داغی عظیم بر قلب ملت ایران، مسلمانان جهان و آزادگان عالم گذاشت. دشمنان قسم خورده ملت ایران، در اوج خباثت، گمان می‌بردند با این جنایت می‌توانند اراده ملت بزرگ ایران را در هم بشکنند و روح مقاومت را از این سرزمین جدا کنند اما نه تنها به هیچ‌یک از اهداف شوم خود دست نیافتند، بلکه ملتی مصمم‌تر و متحدتر از گذشته را در برابر خویش یافتند.
🔹
رهبر شهید وفرمانده معظم کل قوا، در تمامی سال‌های پرافتخار حیات خویش، الگویی کامل از شجاعت، بصیرت و پایمردی در برابر زیاده‌خواهی استکبار جهانی را به کلیه آزادگان عالم ارائه داد. آن مجاهد بزرگ تا واپسین لحظات عمر پربرکت خود، خط مقاومت را با شجاعت و بصیرت پاسداری کرد و هرگز در برابر تهدیدها و فشارهای دشمنان، از راه حق کوتاه نیامد تا میراثی گران‌بها از ایستادگی و مقاومت، به جای بگذارد، میراثی برای همه ملل آزاده جهان که هرگز فراموش نخواهد شد.
🔹
اینک بر ماست که با حضوری باشکوه، متحد و آگاهانه در مراسم وداع و تشییع پیکر مطهر آن رهبر شهید، پیمان دیرینه خویش را با راه ایشان و آرمان‌های انقلاب شکوهمند اسلامی، تجدید کنیم. این حضور، پیامی روشن به دشمنان دارد و به استکبار جهانی، یادآوری می کند که راه آن رهبر و فرمانده شهید، با اراده فولادین ملت ایران و در سایه رهبری خردمندانه جانشین شایسته ایشان، حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای، با قدرت ادامه خواهد یافت.
🔹
اینجانب، به نمایندگی از کلیه همرزمان خویش در ارتش سرافراز و مقتدر جمهوری اسلامی ایران، از عموم مردم شریف، خانواده‌های معزز شهدا، رزمندگان و همه دلدادگان مکتب مقاومت دعوت می‌کنم، با حضوری حماسی و تاریخ‌ساز، قائد شهید ملت و همراهان شهیدش را بدرقه کنند و بار دیگر به جهانیان نشان دهند که ملت ایران، در برابر دشمنان تسلیم نخواهد شد و تا آخر ایستاده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/446010" target="_blank">📅 16:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446009">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzPwQUDxeW84w8hl_24U-V6rznYD98HSMgQFcrfPkr6JAdFu4sVoBpJt0XDNOq1hxK0HlV8KZb6OX4qMTgseEgHN5Enq5s1ZwCahfc3Bv71MW6xSp9uqAZZfyXCXiNV8-3tk9gVR67vo05uhX2RyDn1t557j0BQ4pj86BvHYeVWkuCRhRkumtI94C-fqhnriE1KrcXI4qtNVWnWs6LcWTUy7ylipgrUxsBnmXNz2SFjvB9d25rB4DZDxMJVL_Nhg6z4JEnnWnOafb5txINCgfOxcxexMw3fDMhTWK6sbfrzvBm-fJmi6QUcwYurvPbpByoOcJdIw5oS2LapBCKms9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرنگی‌کاران جوان ایران قهرمان آسیا شدند
🔹
تیم ملی کشتی فرنگی جوانان ایران عنوان قهرمانی زودهنگام رقابت های آسیایی تایلند را از آن خود کرد.
🔹
در جریان رقابت‌های ۵ وزن نخست کشتی فرنگی قهرمانی آسیا در تایلند، نمایندگان ایران صاحب ۳ مدال طلا و ۲ برنز شدند.
@Farsna</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/446009" target="_blank">📅 16:03 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
