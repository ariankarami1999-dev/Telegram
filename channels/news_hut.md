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
<img src="https://cdn4.telesco.pe/file/IdrBVNgS2lgGwepqQYJQzi1rm7ssfTVDJ4zabDbc5MdCo5GysBWeosTjxEROEW4hXG63qHr5dwoggbqyuueZjOdcinI_x0WCOzd0XSBMGAs8rAyoEqtWZHCm4L2Gq017_K3I2xb_muxw5td5A_wUJuah5mifVxFipx000qjL77h6BXyX52-DzhqyXhKcXNShaeEmeA5nt4jFB5kyi_EjjV7sOXiRiY-qrp-oNy1Khas7CeJIs1euZgXevgWVP7TvVdstNNHNo-4RThr1zkeI-8Gtui0S7yAd85-jd7bNr7H4iC2e8atGFe9Rhm0x6pVu38kg_71ckJnUdSC-ZLPBXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 104K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 08:11:45</div>
<hr>

<div class="tg-post" id="msg-73195">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/news_hut/73195" target="_blank">📅 01:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73194">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/news_hut/73194" target="_blank">📅 01:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73193">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ: انتخابات میان‌دوره‌ای آمریکا تأثیری بر سیاست من در قبال ایران نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/news_hut/73193" target="_blank">📅 01:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73192">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52adbd7bd6.mp4?token=YHKuJMQ71kT0zbY06i7EfbgOH5ntSuhLO51M3S6OEwUf0G2JKMdcq1LgKmp4kRHlW64YA63EvDhfTzBSiCapPn7bY0O8xWEZPQjPKVeiuoTvmjhTj-0BdS0_-BJ2ptFkB8krbbPuomUlzic3RhLZRHgDRPMveD66i2udevDe5xvs7ga_x7MzRAgkiGQlmQsMC224tIAgbyXpYnk5azpOCjXs77Zls5t2IkJUZLuxuirwTM86AQtqWAuzCpkx_OYseXnLSPqvb133lYtx5LLl3emgW-oYK_EGMKJJ37O6_2lNqCvqYEeNE97PT4KOJjW8JHsB5mdiucRmkCkUF8FQvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52adbd7bd6.mp4?token=YHKuJMQ71kT0zbY06i7EfbgOH5ntSuhLO51M3S6OEwUf0G2JKMdcq1LgKmp4kRHlW64YA63EvDhfTzBSiCapPn7bY0O8xWEZPQjPKVeiuoTvmjhTj-0BdS0_-BJ2ptFkB8krbbPuomUlzic3RhLZRHgDRPMveD66i2udevDe5xvs7ga_x7MzRAgkiGQlmQsMC224tIAgbyXpYnk5azpOCjXs77Zls5t2IkJUZLuxuirwTM86AQtqWAuzCpkx_OYseXnLSPqvb133lYtx5LLl3emgW-oYK_EGMKJJ37O6_2lNqCvqYEeNE97PT4KOJjW8JHsB5mdiucRmkCkUF8FQvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: بعد از اینکه متحدان ناتو ایران رو به طرح حمله تروریستی به پایگاه هوایی فرفورد بریتانیا مرتبط دونستن، آیا قراره اقدامی علیه ایران انجام بدید؟
ترامپ: «باید ببینیم چی می‌شه. اقدامات زیادی در جریانه. وقتی می‌گید اقدام علیه ایران، (باید در نظر داشت که)اونا دیگه نیروی دریایی و نیروی هوایی ندارن. تورمشون هم الان به ۳۰۱ درصد رسیده.»
@News_Hut</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/news_hut/73192" target="_blank">📅 01:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73186">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FG2OwW8UxsQ9qZjpg6IQ1dB3TYBJR7Pfbuo5mOBa49H29s-biADwLLO5tQUKTofJASUB-NjAf9kyR-j8PTZKmbE0QFwRUjqeC9ZDoMfCkomrznly0Yp9CFe3vatmdEVulePkTJTMkng68fbXYkLzImvIhqZH4EFsU91w7lCE5ZrBU_Q0VyWF5ZBgfZ_dmczsH4wTZbH2XoP-UdkAXoBNwn-wf_wBEdYd0mISPL9KOQK8ZXneUk0jcbX6UeX12kaJd4yre7RFPYLbO93x18IjUbg784d11gzcvQj56982kPH_Yiigez-GnAkF5C0WKvZrtsrFu4ydFmRbCic-ChRjgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cg2s2zNDisnMJt9liN9XYsvqkIpU6tCGx31wXPpo5aXvqUsEkuSo0yDaaR3okHpq3RYsNkNG45Q2DY-O71XJgox_Jvd1U4rNzT5vJRiEkofAsOLRdq1q7pwwe2F7vJuvpFRla9WuwUEZrl-3w_8lYGK-f-ohcXN1akDuuacYn5WTcVemDa7TM_MQkh-zwc9us4f1OSlExYlflu3xtxX1MFVUTlZUuLE1lHTcEggHwYXuzqtSQP5SiJDjQ2eb13LSFjVKe-g92MmHhhBF3C5tAkPzZktrGGYT9v9bBxaHArAvPi30KGB950vtxV7fIG5x87heo4s2-3G9R5hU7A-PIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sTuJE09N2A3Xl9XKIJz7ZP-4-cZ3_UXE20pUhVGQgtSSHR79Ff1fEvZaoJlJOaX-a9WVRgT8Q2gwlCmtJBj8c4VaDnST8h6NZ_sPMmH90Hboo9tkSATSDTtcTanZNrxSmEqfZvYK5UyNd0VSWgga0Jo4MH58A5jHrbsj_KHoh7JLx_Pq4oMf3OhRyQM-cRw19vVYQTBNV2IoI5DjxLmMa_U-dIlalb5DN4XyG9cXtF614ST35YpcZ-kVfLdCRDCnLwp-Xfq_b7YcrvTcACGVsfEBHplfa3BC0Oe0X21Db6gfVf1Nen-XLSutYJX4_K7eC6a8nqtl2jHt8awtllJYRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Wk_fmcZsLmkRxhUPIaTEUFgzTWptGggGOknOBncsQtDK2eswNnVR5BLf970bUYCBDaKl0ID-E6US1R5yzl-apGyQ2_hqKs9VJh-KY3PYlNzZgWC71ScWhQ5kATnHUFjmXdcpvyYp_fROqIXwn0HdD3SzqFALPw3af91woHrBBUXc60BKNPE5x4RmdoGJNiMvczYGbsWu88O_PJEuOF9o9zE-Hx3G14rHmISas4Jh-N6F1-com3MYp4UOPAZi1Ar3IV-9lp9xrHN3OeFFYjnMPGYEB2Ru8LD0tpJk-9UFeiZlzhbV9Hmg5Ya9hbWMbKtdhAmFzuBs8qHdE2dC6CV_Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PuR08bjhHRKfQ8Rkc5C495p2iYDG3iXMzTpQqbfk20RQYFGmeJ-KhI0FPLr_obkuDKqgYoHiyrl6fCCD7boJlgxe5Cg2znXLG0RTGn_dibIhbqpdS7jyA-6MaGFLXtMFFhLtZTlBgeG0ZmJXWZ-n99URn5KT0CHIMlmJHB5C5TZy6znTrjKBI323p5cWZ4hRFvoE6zUu9r9s44KT2wYnMZLNVhIV98aoNfL0Cni9mkM4L4a2wkd_SSdsU6uzoV1C1PVq67tH2-dMKpDO9IxBbuNLWzfuj0JjC8fcIR3rQ5uHuH_SPqA4wWD1Dedw2HmfDevgs3lDGtyMj4P0QDHqYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rh7wXwrDqQat5-myr4QtRyqVXvdjdNBp2RvprLop00amVWGjeHM8xNtH4t33gDLkKHOvZd2Y1pTIXUlDhoCY5_b-5mGbNzWoK5stTaLZSV53130r524JjT7az8sPXSw6SGXN0FLL5jyahEIoe0OUX6df0nD9dwoYoaWKZvT7ZngIMUoDlUUUYzNhJS1Q9UPbQlPiqY6Q5y2-IpGUKKrDug1O-nTTsJREUeNnBj8Rwah-5jpjS2wtgNCnbpI-svQKia7s8S6-leYR1Taw3DbVDfT1d1yRDmn-fUWRWsEq9sMd_5iAEkU5Umz2fZgyQ7wEKqGExdLo5FcCDOhhK05OwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در ۲۴ساعت گذشته سپاه پاسداران به پنج کشتی در تنگه هرمز و یک کشتی در ساحل عمان حمله کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/news_hut/73186" target="_blank">📅 01:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73185">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f60941af.mp4?token=LLDl1HvkgIfoDrEGtOKBh0_RiEgNddcvQIjTYw3S6TU2ucTmI4iAGmW51SAIOpEQgB3eOi0wEyazqHwm-4YL7Jp9gy9RjEuo8xSuXyTLsxLFoZQIKRxzlEyzacK1AcPnDoAte8qv4aFEM7pP6Hc2utKBpqv8FsMS0K49oMBIzuBhJFKwRl17gabopXvMAuEfP9xnermjcOmk3iL8aJ8Zbj1Lir72UQICLLvwI9tlW7i5Y6IZL5fvzXSwigrrW8LQ92W61bV0rlwXt02isMD6LRnHZqs8FUjrbFMAWCMI8hEjF6EL0czHMVTumkC_wiEO2dCYkBggh0jgAPN4wz3Mxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f60941af.mp4?token=LLDl1HvkgIfoDrEGtOKBh0_RiEgNddcvQIjTYw3S6TU2ucTmI4iAGmW51SAIOpEQgB3eOi0wEyazqHwm-4YL7Jp9gy9RjEuo8xSuXyTLsxLFoZQIKRxzlEyzacK1AcPnDoAte8qv4aFEM7pP6Hc2utKBpqv8FsMS0K49oMBIzuBhJFKwRl17gabopXvMAuEfP9xnermjcOmk3iL8aJ8Zbj1Lir72UQICLLvwI9tlW7i5Y6IZL5fvzXSwigrrW8LQ92W61bV0rlwXt02isMD6LRnHZqs8FUjrbFMAWCMI8hEjF6EL0czHMVTumkC_wiEO2dCYkBggh0jgAPN4wz3Mxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: انتظار دارید جمهوری‌خواه‌ها مجلس نمایندگان رو ببرن؟
ترامپ: «ما عملکرد خوبی خواهیم داشت.»
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/73185" target="_blank">📅 00:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73184">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20acd7602d.mp4?token=cUoLrAjOd5xMarx1y03zfX0JcQuo77IsX_NtH9nyAILRSHNdDU1obzb1Aa9pyUBr8IexBieyuoqgd8G8gOCvhlTsG-6wSNCHwilmUYMGJrd9alipYblx9K4Kj7mr9Intgd_C80fXp9QZBBslQz3QSyPTd4Yom5BaNlWaBwNp3NwrW2CzaZxWi2o-ZlfxhIUmZoxCmCzUSnPZY_d_Mpc_Kiys4qRkX5xR-l1ajOcumTIoD3P8HHnDPAWhiL6pyMIQT3Or3h1PmQY68mEQzXw6xmNcoDAFRVp5FpGjnOTC7q5UsYMPhmG007fikecFBj4gFfo6TTvdUZMJJk6pmXv1gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20acd7602d.mp4?token=cUoLrAjOd5xMarx1y03zfX0JcQuo77IsX_NtH9nyAILRSHNdDU1obzb1Aa9pyUBr8IexBieyuoqgd8G8gOCvhlTsG-6wSNCHwilmUYMGJrd9alipYblx9K4Kj7mr9Intgd_C80fXp9QZBBslQz3QSyPTd4Yom5BaNlWaBwNp3NwrW2CzaZxWi2o-ZlfxhIUmZoxCmCzUSnPZY_d_Mpc_Kiys4qRkX5xR-l1ajOcumTIoD3P8HHnDPAWhiL6pyMIQT3Or3h1PmQY68mEQzXw6xmNcoDAFRVp5FpGjnOTC7q5UsYMPhmG007fikecFBj4gFfo6TTvdUZMJJk6pmXv1gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: شما گفتید روسیه و اوکراین با آتش‌بس موافقت کردن، اما هر دو طرف می‌گن چنین توافقی نکردن.
ترامپ: «موافقت کردن. می‌دونید چرا؟ چون من گفتم: شما موافقت می‌کنید! دلیلش هم همینه.»
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/73184" target="_blank">📅 00:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73183">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b813e1384c.mp4?token=mRbtmEZ1-2r26cJTh0XfNRSjqM4Mk2uab0AwDCGHg6FJzuYT4N-S-zUmmSAabLj2dmJ88rHtxiK3pHbHOEjlwOhnftaXa6i8mbcCdBshzUUC-8cutNAosK1r28q76nk_DQaW68tM_iceMR8wCWpip_iWp-pF42urs9g2apT-F1BvzXs_Te6BHf2vnd9Kmg78M_GqZP7qDPEAzUKg9ygwYTkoR6IHgYc_6t_jnvqMNEK5xWwfSw1_gHB-8rO2nyCKVcch9Sf9lbFnlYcdMgaWs24jdI3nALZ4XhRq689UNQdvtpDM4AD9sMuQen5TKBfMF2hwmS_caMBt2zH1Dv0ejQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b813e1384c.mp4?token=mRbtmEZ1-2r26cJTh0XfNRSjqM4Mk2uab0AwDCGHg6FJzuYT4N-S-zUmmSAabLj2dmJ88rHtxiK3pHbHOEjlwOhnftaXa6i8mbcCdBshzUUC-8cutNAosK1r28q76nk_DQaW68tM_iceMR8wCWpip_iWp-pF42urs9g2apT-F1BvzXs_Te6BHf2vnd9Kmg78M_GqZP7qDPEAzUKg9ygwYTkoR6IHgYc_6t_jnvqMNEK5xWwfSw1_gHB-8rO2nyCKVcch9Sf9lbFnlYcdMgaWs24jdI3nALZ4XhRq689UNQdvtpDM4AD9sMuQen5TKBfMF2hwmS_caMBt2zH1Dv0ejQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: روسیه همین حالا آتش‌بس رو نقض کرده و دیشب به اوکراین حمله کرده.
ترامپ: «در این مورد مطمئن نیستم. بررسی می‌کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/73183" target="_blank">📅 00:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73182">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIquySJlIJhdVQbeofg0qP5FtkrjDnsgSDAcCj79ds-NIb5HVIXKNQKNb3GraUNAw5tDrvcOQF6IzOmBirzMds2V_hFeCUR93mmiJyOarS-OJ1QzR6LDOSdKzSu1D2yyAHFD3xx_0a27r0zYhjbWnzbsQYem7qCd_1cZv0r-QvwNs5685UCA_Eminf2BRlLlTYSc95jY6UGDGewgEVxs-LUFi3lpFEOQEUkvyTPxUi78djo9xh9ldrzLbzUXMc4z2zg4iBMwRqXnvVoMk8DfmdNYir3W_j1l3sN_soluoZ1uvaZ9udWQCND7MXG6g4ci4xV4B5LtUvgAvH6E9oC1dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آر. جی. میته، بازیگر آمریکایی که به خاطر ایفای نقش «والتر وایت جونیور» در سریال محبوب «بریکینگ بد» شناخته می‌شد، متأسفانه در سن ۳۴ سالگی بر اثر خودکشی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/73182" target="_blank">📅 00:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73181">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a66098169.mp4?token=P-lNErtyzt7rB2SglNkLv6nrbrOz75wZFy5JXk8hD0wYpGofG402mDNd2jhrgNuotmPxsRRVUUUVLmclBAMp5EBFzkV8QrxZfakti921CYdsIAND24OnWehtL3qf46sUwkAE9TXW2OtxiUBDqsfcioJ0zPJULXpCEwfGSRep0gPZzuchvrvvAb_HzSoOs7XxLaINFpYqTjauZ03JeVVhFPQ5kJqDvvyBUkSdbvLxO6Tu7Q1E1TKMYC2qAtiMFn_TNbNBO3Q2liDK-VIf7G5BRd3wmLO7uc-g23puipNhELyqiIta0Gwc_d05tukIsSRzn3XY_A0Sjt2jazTo59eE0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a66098169.mp4?token=P-lNErtyzt7rB2SglNkLv6nrbrOz75wZFy5JXk8hD0wYpGofG402mDNd2jhrgNuotmPxsRRVUUUVLmclBAMp5EBFzkV8QrxZfakti921CYdsIAND24OnWehtL3qf46sUwkAE9TXW2OtxiUBDqsfcioJ0zPJULXpCEwfGSRep0gPZzuchvrvvAb_HzSoOs7XxLaINFpYqTjauZ03JeVVhFPQ5kJqDvvyBUkSdbvLxO6Tu7Q1E1TKMYC2qAtiMFn_TNbNBO3Q2liDK-VIf7G5BRd3wmLO7uc-g23puipNhELyqiIta0Gwc_d05tukIsSRzn3XY_A0Sjt2jazTo59eE0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالملکی؛ وزیر کار دولت رئیسی و عضو هیئت علمی اقتصاد دانشگاه امام صادق:اگه گرانی رو در نظر نگیریم، هیچ مشکل اقتصادی توی کشور نداریم.
+اگه ۴۷ تیم دیگه رو درنظر نگیریم تیم جمهوری اسلامی تو جام جهانی قهرمان شده
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/73181" target="_blank">📅 00:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73180">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بریتانیا دو تبعه ایرانی به نام‌های «روح‌الله بازقندی» و «شهرام علی‌رضا تمرزاده جاکی» را به اتهام دست داشتن در فعالیت‌های اطلاعاتی ایران و توطئه‌هایی با هدف قرار دادن افراد یا دارایی‌ها در بریتانیا و سایر کشورها، تحریم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/73180" target="_blank">📅 23:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73179">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EYGqc0o5cYxMBTtI1Wmj5ciO5hhl38c4I2RuTTCJ7RJCMuchamHXfGHf6byTs89EzlDLA9Ra7IM9fW_8a9ARYmccwcraUe9s1NbClxs9IKdzaD561VHFjndhj_ktQscIHDIlMoAfJ3yWXc8fFv-hthFXoXb7jV8HV4Mt5IhS8ErgqIzDNC1VX9n0BE8H6rLAsUPN6eIBtjJ1ZbvQ6eJtxMy-44p3wcpnv_xkBhpBqKBSTuH5uvkK9Vuz9n6FgLR4niKFRoOKRKtXwStrNkOcPrfee-vua1hAdvXZuklroLn6D3fNVvt0qJ84tH2Z6Z8Q2DJ2DPPfaJioLHcUUp6Llw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو امروز لایو گذاشته بود و خیلی جدی داشت در مورد انتخابات اسرائیل حرف میزد که یه ایرانی این کامنت شاهکار رو گذاشت:
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/73179" target="_blank">📅 22:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73178">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21384b098a.mp4?token=N6uU6_sWNoEPs2ZCO1tTFIstpT4rO43gfGwGer8pfDJdiF397LbqDOLWbzrfNKOO5__dZ2zAbwZjrhMW1HCr_74DIz8vSrZ10221XT7MCLB7tziMeDfS3U_1e1o6qGG-cutCk079hk-44CWaFjfjSEXiv_He1xZy2_O4vDqXT_Qy6KUl7WY7ZmDRJAVN6ksQaqF9W8Wl2LtJ08r2EAbC2QUK9tthVIm6-NtneOJNBCj9umIbN194G4F5z6ZXpKBJOBRx-7xJg27q_f1xH4T7AltJ18d_WYVWCPtj3U7AIxgRSn4PKte6x6EYrLrTJb-N-QOnEKb2EWDD03AC-Pa-VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21384b098a.mp4?token=N6uU6_sWNoEPs2ZCO1tTFIstpT4rO43gfGwGer8pfDJdiF397LbqDOLWbzrfNKOO5__dZ2zAbwZjrhMW1HCr_74DIz8vSrZ10221XT7MCLB7tziMeDfS3U_1e1o6qGG-cutCk079hk-44CWaFjfjSEXiv_He1xZy2_O4vDqXT_Qy6KUl7WY7ZmDRJAVN6ksQaqF9W8Wl2LtJ08r2EAbC2QUK9tthVIm6-NtneOJNBCj9umIbN194G4F5z6ZXpKBJOBRx-7xJg27q_f1xH4T7AltJ18d_WYVWCPtj3U7AIxgRSn4PKte6x6EYrLrTJb-N-QOnEKb2EWDD03AC-Pa-VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی النصر عربستان و نفتچی ازبکستان به دلیل حمله حوثی ها به ریاض به تاخیر افتاد!
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/73178" target="_blank">📅 22:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73176">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzmwdPSfxS2R59pTnB5OB3NIerKOdOc8N1bXZSS4SSdWmZgYQnZRES1i5g17S0AIPRvIwjvF9hyXH2AIDfLnawSBf2hQDmD29PCWyxsaoV5sEcOTVJUn9JzuLfK5qDEf4zdtMvWoi5l5b_IlEILCPeqnpzP7Ubv65fV0LauwxoSs95X8fIaVfQDK2mat7dW22tsCxEWyI2UuKmc4vKFTojkfXY-UBpnlwK9WH3ofnIhfsJeyXcw8HGpnBLkg9MX_ZEcWpCqQEFQAGpJeg_gOSdzh9O2Y_hG7I1rVseMX4jGRMO3MzfyRluq3XOXUHo2HWZRaJO-Ht2P1Y934o4CQLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارش داد که یک نفت‌کشِ حمل فرآورده‌های نفتی، هنگام عبور به سمت خارج از تنگه هرمز، مورد اصابت یک پرتابه ناشناس قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/73176" target="_blank">📅 22:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73175">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f2fd3a4fd.mp4?token=R9MH3trdVbl3_EW7hQF68_Q3lDPwlrXy5Ll_oS8328QYICwx6Lw9C2w0HLTOm_5M922TPtUGcRhSxWZw18qlhLyNKAUs7MwmUVHONA5KZfcuQEBJpawkZxmjuPIa7hUchDSgwwerWJZ4ZFfeutIUVwishenLJQPmoB6rSqt9GdzcETcaFbRW3WCPMwXd-IudkP41EAZZ3-D9fhMDYGEneuNedhlHVnzUV9Dv5DeaHwRzqmSEL3siDEtvh5vYxomnLMFEq9BnaEmaW6s5ZCpM7zV7gFznJsuyxobBeRDcS1TlI_fVDhMfBwT8nyCnwg0oaDveaFozaXm8wSzlZDY6Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f2fd3a4fd.mp4?token=R9MH3trdVbl3_EW7hQF68_Q3lDPwlrXy5Ll_oS8328QYICwx6Lw9C2w0HLTOm_5M922TPtUGcRhSxWZw18qlhLyNKAUs7MwmUVHONA5KZfcuQEBJpawkZxmjuPIa7hUchDSgwwerWJZ4ZFfeutIUVwishenLJQPmoB6rSqt9GdzcETcaFbRW3WCPMwXd-IudkP41EAZZ3-D9fhMDYGEneuNedhlHVnzUV9Dv5DeaHwRzqmSEL3siDEtvh5vYxomnLMFEq9BnaEmaW6s5ZCpM7zV7gFznJsuyxobBeRDcS1TlI_fVDhMfBwT8nyCnwg0oaDveaFozaXm8wSzlZDY6Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی وایرال شده از یه مدرسه پسرونه!
معلم اون جلو وایساده داره درس میده، دانش آموزا دور هم جمع شدن و کله‌پاچه میزنن...
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/73175" target="_blank">📅 20:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73174">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtCELL68f85DlgQZErVtsop0pt3UeRsjovl9eqo-QN_OOWsMGWY83qWxa5LNklBQWGidGp4P446Cn55M9Ix_vTAh-AzTeQNMqxhORx5MxmtrkNUT_uxhRk_AQ4cz_jn25EuAgGUv_2TKsJvWIUq4P7OOqvQGnD1v8HJTjWz0h9qGLyQZB7kmle5m9AGR6rj4XuQ8D8yw5cd2r7c_nx4UaLxN0WB1TAYqgG9OG13B-ZI3hmb_02DtQ1-18uqaV-DRidaHjVipRJSpjhCFdPE_Cx-hpdsJd4P1JzGPjx63WtlHI9OdofaacXug_kHypcQp4l0g7wR4SmFz2QB-iyf6Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با انتشار تصویری، اعلام کرد ۱۵۹ کشتی ایرانی در دوران ریاست‌جمهوری او نابود شده‌اند؛ همچنین مقایسه کرد که در دوران رؤسای جمهور قبلی این کشتی ها روی آب بودن ولی الان کف دریان.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/73174" target="_blank">📅 20:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73173">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7da0f71e2.mp4?token=fyu6ydgb6NxSqvz3g3ddgbTI6VtR6ghBBo3hDcxATFzyn3V9HXaOhe3-2gTdBxRpT3UlbKI5LTFqYB-ZFAAL-lgmxv3L3IbnNZoIv3iD1Q6YpAE2Zr9PKoqhCeIQlvFv4Q4PG7-mtY94T4zTmUQkZSbQozwlzdsQ12wig-FOLHZ-1EmUJC1KarsHYqV4ad0giFuY6k5Zw6y9yw9ewCCOJyFEKMQWyTp7iibAvgxv_BZCRKg2TmLZ-NBOz6h5ugRFzcPTmV5JbO78bcNo3rU-w7IS1NUlmbSOdG7BIKbrGxX0PUh5-S7Nv2JcpSk_9hL-72mhBZw4-eFmWPDkY1M4cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7da0f71e2.mp4?token=fyu6ydgb6NxSqvz3g3ddgbTI6VtR6ghBBo3hDcxATFzyn3V9HXaOhe3-2gTdBxRpT3UlbKI5LTFqYB-ZFAAL-lgmxv3L3IbnNZoIv3iD1Q6YpAE2Zr9PKoqhCeIQlvFv4Q4PG7-mtY94T4zTmUQkZSbQozwlzdsQ12wig-FOLHZ-1EmUJC1KarsHYqV4ad0giFuY6k5Zw6y9yw9ewCCOJyFEKMQWyTp7iibAvgxv_BZCRKg2TmLZ-NBOz6h5ugRFzcPTmV5JbO78bcNo3rU-w7IS1NUlmbSOdG7BIKbrGxX0PUh5-S7Nv2JcpSk_9hL-72mhBZw4-eFmWPDkY1M4cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه سرباز روس تو خط مقدم، سربازای اوکراینی رو که از پله‌ها بالا می‌اومدن، با نیروهای خودی اشتباه گرفت!
وقتی اوکراینی‌ها به سمتش تیراندازی کردن، تازه متوجه اشتباهش شد و درگیری از فاصله نزدیک بینشون شروع شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/73173" target="_blank">📅 19:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73172">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8047543035.mp4?token=v987uI4gViEQwo4oC5hQ7Gw9pPn6wT_w34qyzZGFPFBfhENhf8OaZhonF611MgeCi83ZIcrla0RoxhXdibMXusbfQUKryq-l1oXpr36FMUhLQ2FcvFJ54UUDWtY1m_yr2o1MVA2PmlDQIWPtcmgYhRPqYLIdS4TKdXce61uUh7ocFflV9CuexrR3i69PJGiJqF1FVuwt_9VqNdykeh67CQVmhXLfE4D2qTM4EL4fB-iWlZbQRoMRdVz2_TEQrydQgOnqfRyZccVR_h_myFJzzfy5Lu4clKBeNK-MqX0Au3G4vh8rOZdBi30lSPQ7xBZQpUe3_wpn3azVRIJltEvstQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8047543035.mp4?token=v987uI4gViEQwo4oC5hQ7Gw9pPn6wT_w34qyzZGFPFBfhENhf8OaZhonF611MgeCi83ZIcrla0RoxhXdibMXusbfQUKryq-l1oXpr36FMUhLQ2FcvFJ54UUDWtY1m_yr2o1MVA2PmlDQIWPtcmgYhRPqYLIdS4TKdXce61uUh7ocFflV9CuexrR3i69PJGiJqF1FVuwt_9VqNdykeh67CQVmhXLfE4D2qTM4EL4fB-iWlZbQRoMRdVz2_TEQrydQgOnqfRyZccVR_h_myFJzzfy5Lu4clKBeNK-MqX0Au3G4vh8rOZdBi30lSPQ7xBZQpUe3_wpn3azVRIJltEvstQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش علیرضا خمسه به کلیپ معروفش توی فضای مجازی(خلوت کنید آقای خمسس...) :
منم مثل همه شما یه آدم معمولیم. صبحا میرم پارک پیاده‌روی، بعدش میرم نون میگیریم و ...
بخدا من بادیگارد ندارم چرا به من فحش میدین؟
چرا به اون جلوییم که اون جمله رو داشت میگفت فحش نمیدین؟
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/73172" target="_blank">📅 19:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73171">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73171" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/73171" target="_blank">📅 19:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73170">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9ABFIfj74x8n4d3WMIerwIRXIQ6zrgZB3gGBCzE04sG90rYhsgOO7SwKSl0nn8XelQWwLKjCJVXCt6lkGnI3qgmSuah-JVswj9zdnj88cM5BDqQm26p4S1rbskNVypTHCf6yQQ0MSZScTAqth7Z9JHWh6s5djOC3tBYJ2NcJPs54l58MS_0dzuqbcN6og_Pg5dKWpi55AqdljA8CT7to9ayQaz5QWB5-C71mN_qQ-TYJ1Ai4WXe_S5pXnzHfEoqibRsiGYkVrYrUa33A03qNtXg-koFEVT2Av8Y7Sgnk4l_7pdkOjE3GrraYSCfgvnD5pEZceNSsg5FJmlSFr47ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز استقلال
🆚
الغرافه رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم در ۵ رویارویی اخیر:
استقلال: ۲ برد، ۳ تساوی و ۶ گل زده
الغرافه: ۱ برد، ۱ تساوی، ۳ شکست و ۶ گل زده
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/73170" target="_blank">📅 19:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73169">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">#مهم
؛
اندی برنهام، نخست‌وزیر بریتانیا، می‌گوید می‌تواند تأیید کند که حادثه پایگاه «آر.ای.اف فیرفورد» (RAF Fairford) «تقریباً به‌طور قطع» توسط سپاه پاسداران انقلاب اسلامی ایران هدایت شده است.
من می‌توانم ارزیابی خود را مبنی بر اینکه این اقدام به احتمال بسیار زیاد در ایران هماهنگ شده و تقریباً به‌طور قطع توسط سپاه پاسداران انقلاب اسلامی ایران هدایت شده است، تأیید کنم.
ما این تهدیدات را در خاک خود تحمل نخواهیم کرد. ما با استفاده از تمام اختیارات قانونی خود برای هدف قرار دادن شبکه‌های جنایتکار مورد استفاده ایران و همچنین منابع مالی آن‌ها، با این اقدامات به‌شدت مقابله خواهیم کرد.
ما تحریم‌های بیشتری را برای محدود کردن توانایی ایران و سپاه پاسداران در آسیب رساندن به خودمان اعمال خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/73169" target="_blank">📅 18:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73168">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50742ac121.mp4?token=RGRYzidJxvV5LMpyQKaJJc6B3Zfe8m8z3s-K6a2gjEGABmAZtKVYEU8WIqNnKfCDwHmAxsVByGeO7Yqm_KHvR-AhsgUENK4vmUy7MPY6PMXO-a22dvuKg1MbsY6I-CvAUzeDLoOu3M_8791cmAYvWGT0C-6ICwsb9qgHPLJHa-X7_kYaKPjuQYnNEefJcPBaDdJrmqBCUbW6jExf4scoUVPiswV-h4mNJFZ4qY3ukrqzEIlNQexmHpHMO3zrXIZCYwM5TImxFnULzB72RNaMJTjrFWZNtywCFX4t8Qz9TfSUFmC5kW1SB_MboP0nQP6Uui9_sJrqa3KgEqIa25AYMr-18YFIpK_swYoGTmiYUE4Qh9k-Egb1RaMCmdnuk9MJ5XwlY85-hiMFIfp2A__8Expu6LUxQt5NAehmjBFx2yMQbFZKKREPJYnLZNJi_ns0fxfUgape8lv4GShF3tirubaiq9uTn5iVJAAV7xKF3Yn3virudJ2apZvFrpmktRtqk2aMjo3IxKsiXrVKAkhQtdMLtvmRbfKCe0hjiwMwvO1JmnD9nXSgHyxIIFLtjh9labvQ1WYGmCx82rDkr_oyexFbDx-W2NRz6EOs-z0dS7MEB_IEGDN3I3tPpewx_PIDA2cMTLQ_hcv9DYKW114YmNcND8u1D86dcE9lHroHyAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50742ac121.mp4?token=RGRYzidJxvV5LMpyQKaJJc6B3Zfe8m8z3s-K6a2gjEGABmAZtKVYEU8WIqNnKfCDwHmAxsVByGeO7Yqm_KHvR-AhsgUENK4vmUy7MPY6PMXO-a22dvuKg1MbsY6I-CvAUzeDLoOu3M_8791cmAYvWGT0C-6ICwsb9qgHPLJHa-X7_kYaKPjuQYnNEefJcPBaDdJrmqBCUbW6jExf4scoUVPiswV-h4mNJFZ4qY3ukrqzEIlNQexmHpHMO3zrXIZCYwM5TImxFnULzB72RNaMJTjrFWZNtywCFX4t8Qz9TfSUFmC5kW1SB_MboP0nQP6Uui9_sJrqa3KgEqIa25AYMr-18YFIpK_swYoGTmiYUE4Qh9k-Egb1RaMCmdnuk9MJ5XwlY85-hiMFIfp2A__8Expu6LUxQt5NAehmjBFx2yMQbFZKKREPJYnLZNJi_ns0fxfUgape8lv4GShF3tirubaiq9uTn5iVJAAV7xKF3Yn3virudJ2apZvFrpmktRtqk2aMjo3IxKsiXrVKAkhQtdMLtvmRbfKCe0hjiwMwvO1JmnD9nXSgHyxIIFLtjh9labvQ1WYGmCx82rDkr_oyexFbDx-W2NRz6EOs-z0dS7MEB_IEGDN3I3tPpewx_PIDA2cMTLQ_hcv9DYKW114YmNcND8u1D86dcE9lHroHyAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ اندی برنهام نخست‌وزیر بریتانیا می‌گوید می‌تواند تأیید کند که حادثه تروریستی در پایگاه نیروی هوایی سلطنتی «فیرفورد» «تقریباً به‌طور قطع» توسط سپاه پاسداران انقلاب اسلامی ایران هدایت شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/73168" target="_blank">📅 18:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73167">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/294900b4d0.mp4?token=CFNuD3IfpailPPtVx-uXKUHyenjZo7659jzC5Z4jODHB5PyB6Y8BBbw47ygQjNXCKZnhxRRGMZCuofOVS1UN0KJbQdwHrk7GuzIA7QcGSwyAwSRnp2ocrxxDM99qnzeppImnxL1uurX7jF00Krtf2O3K5W9H8GF5VqRHh1jcx61VJlEFvTA2WTZRTDpRq6fD32nWOqXf-bYaeorom9UQr88SvcTmnyu8jUsIpnmGFzlaF4jDuGUmYVml0sv4c0yigADxwZGPyw2W13wDacV0Pk_uY7cHyU0PrMYphzVPh_bUCtmf2G2iBQF7QTmsSHX3pL2Fr6z6jKW-iPP8bv69mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/294900b4d0.mp4?token=CFNuD3IfpailPPtVx-uXKUHyenjZo7659jzC5Z4jODHB5PyB6Y8BBbw47ygQjNXCKZnhxRRGMZCuofOVS1UN0KJbQdwHrk7GuzIA7QcGSwyAwSRnp2ocrxxDM99qnzeppImnxL1uurX7jF00Krtf2O3K5W9H8GF5VqRHh1jcx61VJlEFvTA2WTZRTDpRq6fD32nWOqXf-bYaeorom9UQr88SvcTmnyu8jUsIpnmGFzlaF4jDuGUmYVml0sv4c0yigADxwZGPyw2W13wDacV0Pk_uY7cHyU0PrMYphzVPh_bUCtmf2G2iBQF7QTmsSHX3pL2Fr6z6jKW-iPP8bv69mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد که طی دو روز گذشته به سومین سوپر نفتکش در تنگه هرمز حمله کرده و موجب آتش‌سوزی آن شده است.
سپاه پاسداران اعلام کرد که این نفتکش هنگام تلاش برای خروج غیرمجاز از تنگه، سامانه ناوبری خود را غیرفعال کرده و به هشدارهای مکرر بی‌توجهی کرده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/73167" target="_blank">📅 18:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73164">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d1oBPqj6SaIqbUsqLBUi-xK4Q3Q7F7h8_Ove1LUg9alkioOhCuAGQblHWTCS88bWrj5Z-qfJHZxO54j8W-I7ra2rYvpCp63ZY4VfhD_6OO17yZrlbN-lleEX-dL6xuJ1J8wUaX1jUUBf7k6f_4CwlA4-yaxFK-hSd_kUVaBcSNu-8BeBivh_TyzDoVJTCAD6fCSq75wW0NGp4hQPb0jtElUuE9425RRdhOVqdMiyxoNJpe5WnOFZjhcotnaT-CrlYSk6dY3xe2pYUjbCGJCgc3KCb0bZcezKQY1DVx70nkg9VrArREDKj50hOWRp8DRLZlEQ1zCn1kU81eti9slF4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LncsvKZMmfDgStvo650nOBe2JvX9OMn4b8IFa914aJO6YWc4T27Ryc3g-wPFa-BEAIuIP77CVNav21-c5-pl37_Uiiy5xv0UPsEEEull4gISwVbmqkBx3l9rQBHmEj2XSLFnULh1qS_HdEF2usxtT00gVFoh1iu_VWVOFVSTBNb7UHjEgL0L7RP3t8R2VRLOj_PAYe7D-xprvzbfeUMlyH6UBtkCZ4qBQNGBJMEtOAkflsMSJXbICliZ03hQ1CmKvqj8-9lwvLPIPZ1KWTCSEXRw0bB4n52tCFIoJPWXUlqr3l6O6PPdIJaRMFplUs6dFwjQ7F9nk1eY6KLC6IPBTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e4sNoK29wej7nln_KQZoKqsHfoRsErNqJdxvfJe05_EI6HF3rL_HDbRKv101bknLS6-DuImi7RPT2zmoQck1gs1bey0DtqHvekFjFT7lrXxrUT8Qe2xYyW6N8nqhFCUEGrqTSLPS5lc7ItuvSBLC-yAamo4YIAPJV1fEPRXDqMx1yHaGqOY7K1ETrCEXA1Uygny5yD6Rg42XukBc3SsGqvOUfwMm6_Wej7BL1ljHkrftKf2hRo32acVoK646qWmPnMplTeHGa4SxCUlYquqKX0tDppNoQK1doUS51QbYhAORtRF4plwoeeu6kCiTOFhHnPV60WhIdayydlCeIsh7uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آزمایش موشکی سپاه در یزد:
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/73164" target="_blank">📅 17:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73163">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b1f4cc034.mp4?token=k-igTRzNuMrHAwZE4-Vh2dUWCFHuhEPFG-Nce_KAtXBRBy8oL2KEKXweYMuMn5iUm94Epbf-YrAjyY2V6ygJ98HiIUHsEO_P5w33d5ffSa_9rD6XG3byj8W2QrwM3sXY50ohm8FrriTQn0NA5HoDQH-fqEW7oHvvQE_bU0ITi5lB3xZouO6q8ZH4vCpvnYNeZ9yo4CnikKKcplqbeWXoKa4NqkoXLWcDphO5EjiDbfIzWR6lY-Yueo14nCK3K7zo6knH2mYJamdB0GErtTZGYWgOkAAquIbjk0_9S2cx_TBNpNWqYYe2t7fJkmnTpfRzWe4brFwqlXTFVWBmC8PPEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b1f4cc034.mp4?token=k-igTRzNuMrHAwZE4-Vh2dUWCFHuhEPFG-Nce_KAtXBRBy8oL2KEKXweYMuMn5iUm94Epbf-YrAjyY2V6ygJ98HiIUHsEO_P5w33d5ffSa_9rD6XG3byj8W2QrwM3sXY50ohm8FrriTQn0NA5HoDQH-fqEW7oHvvQE_bU0ITi5lB3xZouO6q8ZH4vCpvnYNeZ9yo4CnikKKcplqbeWXoKa4NqkoXLWcDphO5EjiDbfIzWR6lY-Yueo14nCK3K7zo6knH2mYJamdB0GErtTZGYWgOkAAquIbjk0_9S2cx_TBNpNWqYYe2t7fJkmnTpfRzWe4brFwqlXTFVWBmC8PPEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از اولین اصابت و انفجار ها روز ۹ اسفند در پایگاه سوم نیروی دریایی ارتش، کنارک
؛
در این ویدیو ، یکی از پرسنل که به ناچار و طی غافلگیری به اطراف پایگاه همراه با هم رزمان خود پناه برده بود، می‌گوید ،"جایی نداریم ،فعلا همین جا بمانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/73163" target="_blank">📅 17:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73162">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/73162" target="_blank">📅 17:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73161">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GiKCPSbNbf2Oxz7_bdJ6hT-0TmqhUrcD61hzt-RsWwXhuJRWINE3mmd_4oXZqiZSkxIBfXF_V7TH3Rl7BVgsnVuDnmt5nKO1Lhj6G8EkMJxMPW2FhPJIbHN6ZBD1XQA1OS43jqvV4qySepk0Vnil3ab4xfCQMzv6eKdoRnf-BO0wS_uWB7q8y1_MImI7JHmqVHdTQFzhH7Z-Esc_800SX4-RFAHTrcZDCUm9oALWgE9xkgC6G3KytYwPgMQVc5wRiSmbCx8pKUTCLD47VriP3ViYp2LPJeqTm2qjbMayAQ_4LZS9rGQw-_cjAyYXA6viQ3qCxmemEAES9D7uuuoR9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/73161" target="_blank">📅 17:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73160">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ارتش اسرائیل در پی وقوع حادثه‌ای در شمال این کشور که منجر به مجروح شدن گروهی از کوه‌پیمایان (که گفته می‌شود معلم و دانش‌آموز هستند) شده، وضعیت «حادثه با شمار بالای تلفات» اعلام کرد.
این حادثه احتمالاً ناشی از برخورد با مهمات عمل‌نکرده بوده است.
گزارش‌ها حاکی از حدود ۲۰ مجروح است که وضعیت برخی از آن‌ها وخیم بوده و یک نفر نیز نیازمند عملیات احیاست.
ارتش در حال انتقال مجروحان با بالگرد است.
نتانیاهو حضور خود در برنامه تلویزیونی «The Patriots» را لغو کرده و در حال عزیمت به محل حادثه است.
فردی که در وضعیت وخیمی به سر می‌برد، اکنون جان باخته است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/73160" target="_blank">📅 16:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73159">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bba8b18ff.mp4?token=uxZ4LKo08VJKuVM6cDhbYwG7MpUj7xgAvKzsdZEJ381Tr4JwV32XAfrfIVJ8rXw9V-UvlmfMbk5fTexKpJsZqzEGnil0tqFkaSbm9IK9KaIUCmgfbDjUlEJ3jcBnWajvzewFC3McIVixto_vrf8l7U8l2ZASUPvY-YGodmlz0Ulme4Xnu8A6qD8ZCQSMLqFjcFBWiJisygZwUdJcSrMzE-BX8Xc1A-XL5N3MHoJRMZippLHHqGgL-hCe9tGd6jUfMNMvYumk_6cQBAmIPg0m-UK-OhxVf3vvRwA-YSMX2lqWMoJhFJrk4-fBYyNA6Qr-C8eX50RPRsDgtOx66cOQIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bba8b18ff.mp4?token=uxZ4LKo08VJKuVM6cDhbYwG7MpUj7xgAvKzsdZEJ381Tr4JwV32XAfrfIVJ8rXw9V-UvlmfMbk5fTexKpJsZqzEGnil0tqFkaSbm9IK9KaIUCmgfbDjUlEJ3jcBnWajvzewFC3McIVixto_vrf8l7U8l2ZASUPvY-YGodmlz0Ulme4Xnu8A6qD8ZCQSMLqFjcFBWiJisygZwUdJcSrMzE-BX8Xc1A-XL5N3MHoJRMZippLHHqGgL-hCe9tGd6jUfMNMvYumk_6cQBAmIPg0m-UK-OhxVf3vvRwA-YSMX2lqWMoJhFJrk4-fBYyNA6Qr-C8eX50RPRsDgtOx66cOQIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها دو ماه پس از سیل ویرانگر پیشین، نپال بار دیگر گرفتار سیلاب‌های شدید شده است. این حادثه خسارات سنگینی به مناطق سیل‌زده وارد کرده و بار دیگر زندگی ساکنان این کشور را تحت تأثیر قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/73159" target="_blank">📅 16:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73158">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d202e2650b.mp4?token=h0eGiiIUlUkTctDrBGsToZJF5WUuvWVjaji7uqRII8NK9SnItL0hSX4fwxlGsTFriCyLail-pw_4Ik6QpZogEz88wgRx0xd2lXN32FwJl4X-_iLy0Kau5b5LaA67wyP6mtPOfA0OcU_a5qtuhAeeM0fHRuRxAZflp7DVjjb1E4vuN0ookmM-oKAJA8p7p2Rtv1kAmwJsEtblt5RUz4AiGKDJI4AQiPfs2iN6-m5GFG1-4WG5tYEX5tDl47v10cLMeLClwpNcAdPqxJYM89IQTQoYxr3d490pvuz6MTTjDvFttTEEDAYzHq-2vGRiHBm06LGTcCk0ETjJxGgnyzp3qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d202e2650b.mp4?token=h0eGiiIUlUkTctDrBGsToZJF5WUuvWVjaji7uqRII8NK9SnItL0hSX4fwxlGsTFriCyLail-pw_4Ik6QpZogEz88wgRx0xd2lXN32FwJl4X-_iLy0Kau5b5LaA67wyP6mtPOfA0OcU_a5qtuhAeeM0fHRuRxAZflp7DVjjb1E4vuN0ookmM-oKAJA8p7p2Rtv1kAmwJsEtblt5RUz4AiGKDJI4AQiPfs2iN6-m5GFG1-4WG5tYEX5tDl47v10cLMeLClwpNcAdPqxJYM89IQTQoYxr3d490pvuz6MTTjDvFttTEEDAYzHq-2vGRiHBm06LGTcCk0ETjJxGgnyzp3qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی عجیب که از اعتراضات فرانسه وایرال شده؛
مردم تو یه میدونِ بزرگ با جمعیتی زیاد جمع شدن و درحال شعار دادن هستن که تاچشم کار میکنه پرچم فلسطین دست گرفتن و حتی یه پرچم فرانسه هم دیده نمیشه :
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/73158" target="_blank">📅 16:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73155">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c264e282e3.mp4?token=DSqcyaisbmeeHiwNxhyCE9sdlHXe2mFx3y7Rqt29CCKXKD-WafYquysjJLO64_O8_iiPRxFnj-nZHwf7WUWq27nhWP1JtwV_ABpAHcJ3Zqg_9IQs6XASfj9E7Lo-GTTaD7wcywaMTYfn0Vf9RFGI29XXbqLIpcZm_081jiR68_EIj2EUFrJbR0wX5cBtBBRvO2Gozsa0hJy9GoSfHlm_MDcb43UD4Mdpcym1L5VELblNKNKXaMVZuQFTT-Yd1e0HcN8EAZfGTAc0PwTyf1EXTP4SqpxcHTrMCuJrTZHexqpF2Izq3QUrDIGBFmjpFL1GJW4_FXjc0f7vdMWMRbpO3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c264e282e3.mp4?token=DSqcyaisbmeeHiwNxhyCE9sdlHXe2mFx3y7Rqt29CCKXKD-WafYquysjJLO64_O8_iiPRxFnj-nZHwf7WUWq27nhWP1JtwV_ABpAHcJ3Zqg_9IQs6XASfj9E7Lo-GTTaD7wcywaMTYfn0Vf9RFGI29XXbqLIpcZm_081jiR68_EIj2EUFrJbR0wX5cBtBBRvO2Gozsa0hJy9GoSfHlm_MDcb43UD4Mdpcym1L5VELblNKNKXaMVZuQFTT-Yd1e0HcN8EAZfGTAc0PwTyf1EXTP4SqpxcHTrMCuJrTZHexqpF2Izq3QUrDIGBFmjpFL1GJW4_FXjc0f7vdMWMRbpO3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو بریتانیا، یه مرد جوون وارد محوطه ببرها تو پارک حیات وحش یورک‌شایر میشه و اونجا یکی از ببرها به نام آلتای بهش حمله می‌کنه و نهایتا میکُشتش!
مسئولین حیات وحش اعلام کردن که خوشبختانه ببر سالمه و داریم بررسی می‌کنیم بفهمیم اون کسخل چرا رفته داخل...
یه ویدئو از قبل ورود این مرحوم اومده که داره به یه زوج بریتانیایی میگه "
من میرم بین ببرها، ازم عکس بگیرید!
"
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/73155" target="_blank">📅 15:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73154">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e5000591.mp4?token=TIgW3iWfp2zVqEPIEBli2QSPsGMQmCG_SKftOpjDAPm6MBTE8CNDGyjZijF5ag5d_xYvFNs9HNTmSkzCKrCKR4zkgT349EGldjDFYg1PibKzDJuj4ESWPuEZ0BJ_W9q5HQvfJZuVir5Xl9G3nam9XHDesFr9OOYIxC6gx7VTXr0o8Bt-T3BGMjFXs6vSfVhrukdCqPyAz9aVTj2qq_9SGp5-D4mZ2iqvOHr0w5aQstSy5g-AqXyPHEFJ_3QdfG3qpeu4CvPk9Tm0_XtfIPztl63OHrry1L4VcMMUFfChynyo_2cpNuyP1n-SQKJH65ldUXDKevdjcvFqWgwsmsNv0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e5000591.mp4?token=TIgW3iWfp2zVqEPIEBli2QSPsGMQmCG_SKftOpjDAPm6MBTE8CNDGyjZijF5ag5d_xYvFNs9HNTmSkzCKrCKR4zkgT349EGldjDFYg1PibKzDJuj4ESWPuEZ0BJ_W9q5HQvfJZuVir5Xl9G3nam9XHDesFr9OOYIxC6gx7VTXr0o8Bt-T3BGMjFXs6vSfVhrukdCqPyAz9aVTj2qq_9SGp5-D4mZ2iqvOHr0w5aQstSy5g-AqXyPHEFJ_3QdfG3qpeu4CvPk9Tm0_XtfIPztl63OHrry1L4VcMMUFfChynyo_2cpNuyP1n-SQKJH65ldUXDKevdjcvFqWgwsmsNv0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف با نیسان از اصفهان راه افتاده و رسیده به پلیس‌راه سیستان‌ و بلوچستان؛ اونجا مأمورا بهش می‌گن می‌خوای کجا بری؟ می‌گه ایرانشهر.
مأمورا بهش می‌گن مسیر خطرناکه و توی جاده احتمال کمین گروهک ها وجود داره؛ بهتره صبر کنی چند نفر دیگه بیان تا باهم حرکت کنید، یا بین دو تا کامیون راه بیفتی تا همراهی‌ات کنن و به ایرانشهر برسی!
+
گنده‌گوز منطقه حتی نمی‌تونه امنیت جاده‌های داخل کشور رو تأمین کنه
!
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/73154" target="_blank">📅 14:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73153">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kQaHSHN_ZhiBQINZUh7AOLVjUywEBMfb2Ri-L1QhGZqVT00do82P0iB82a7rSFLJZbAYE66bEHcQwj19JivHG0EK5ZRNEYwKA83nxmGMNAQNEnWw-jDQlB0_6wsdEKmmvmynBJhlx9kEhqj2QsmSgU2JSjF2oWOZfBShyjfBxsMpKlVqWU9N55-pP0Jo-oLq9jaZNemu9OiMEq-RwNuBhMYM9HKNW5gR9GajlLEIy0DTSq3gpZ67EB2LqQ8HeR5wArkBtyl___gM2Vw-35-GJ7otXbS_kT7Ccsf0ssU88O4sDWMVlUDLXCGTOVBY9CNkhKKvJWZCxEksxQAgbnQBWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نفر به هوش مصنوعی گفته هر چی میگم، در جوابش بگو جمهوری اسلامی.
بعد ازش پرسیده بهترین حکومت تاریخ ایران چیه؟ اونم همچین جواب شاهکاری داده:
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/73153" target="_blank">📅 14:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73152">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff8e97c86a.mp4?token=GPqxKTAf9J8OaW_4cGHXG-o5DBbWRb0WxbPobP8VipcAxDYwY7BMYL5E9wOmeY9_EmMjNUCf_XzsyQbtrk4l4Dm9hxHWvywNhroqkH8_RziDUomU_DbBQhGbO_1lXHSvz2XogBAV1-IKGh1PO-UesmfzNZJ2jtOKOgwuuJ_p4F8M0fPB32p5pHVJAoQmkfl3I20XpZxytR3PU7KjxgQ6BffiM6c6uEI0nKqhSuqVttJj7heQghHXLM3b6F2eZ1WdpuZOVmB6_bPN9wMio5JD7S0zN-qsvfH5zrvp3IMEDYCoZtONpZISMHYcbWz34reQHWDbCXv1bSOJxiAtCsZRYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff8e97c86a.mp4?token=GPqxKTAf9J8OaW_4cGHXG-o5DBbWRb0WxbPobP8VipcAxDYwY7BMYL5E9wOmeY9_EmMjNUCf_XzsyQbtrk4l4Dm9hxHWvywNhroqkH8_RziDUomU_DbBQhGbO_1lXHSvz2XogBAV1-IKGh1PO-UesmfzNZJ2jtOKOgwuuJ_p4F8M0fPB32p5pHVJAoQmkfl3I20XpZxytR3PU7KjxgQ6BffiM6c6uEI0nKqhSuqVttJj7heQghHXLM3b6F2eZ1WdpuZOVmB6_bPN9wMio5JD7S0zN-qsvfH5zrvp3IMEDYCoZtONpZISMHYcbWz34reQHWDbCXv1bSOJxiAtCsZRYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دوربین مدار بسته از لحظه وقوع سیل‌ ویران‌گر در شهرستان گرمی اردبیل:
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/73152" target="_blank">📅 14:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73151">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/350f6d8da8.mp4?token=S896mulOfJ3Q8KJWKWBrpAsNZ_lpFj8RSYrxyTxlUTotCFHvsSnioVwHZAkm_Nw86xXtJv0Qk-b58pL8sgxPKY7VXJNgUg495r1dhTbyvz9f6N5lAkgB4QjdohwaH4PF2n0ToanKxqQ7zLdjQgyE4Eqh-51IltqK5u_ZKEPgRCwOtfXT1-BNYL4jSHTzRoHsiA01i7rLSS-7e_BCAMt1BJ8fD92Djibd9fW8z2fv7WwfyvBBibGQBE9IVx90gi-aEmkb4_c7mGpnibiYEDGxCXclB1V4waE_5ORHBP8S7ozC0UsS7e2Sn52CpAGpRssFutaUtyY22k4CGTka3YmgYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/350f6d8da8.mp4?token=S896mulOfJ3Q8KJWKWBrpAsNZ_lpFj8RSYrxyTxlUTotCFHvsSnioVwHZAkm_Nw86xXtJv0Qk-b58pL8sgxPKY7VXJNgUg495r1dhTbyvz9f6N5lAkgB4QjdohwaH4PF2n0ToanKxqQ7zLdjQgyE4Eqh-51IltqK5u_ZKEPgRCwOtfXT1-BNYL4jSHTzRoHsiA01i7rLSS-7e_BCAMt1BJ8fD92Djibd9fW8z2fv7WwfyvBBibGQBE9IVx90gi-aEmkb4_c7mGpnibiYEDGxCXclB1V4waE_5ORHBP8S7ozC0UsS7e2Sn52CpAGpRssFutaUtyY22k4CGTka3YmgYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلاش یک روس، برای سرنگون کردن پهپاد انتحاری اوکراینی با استفاده از یک نصف آجر:
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/73151" target="_blank">📅 13:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73150">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f347ef349.mp4?token=BfgH6NCrmBKX4-eNoxxlLf1rDEzBwwbNXzI-8KW6750GY3XhRNkgVtOTlpq_QqAtemdxTwxXwPqh_lnak8WpRFhy0ONQFhcBY7rAfD9wAcBy2MTWC8Q7_UWOEf8sG2nlQOJGFKpYn8nm5SfHhQISIATbEF3N6uTw6NV0--3QCJgdaVa1WnuuPb8u_CdSxcMD_MaoGyiWlceljpNrH3l63TDefP_lBFcwjgk1PREhEVuUepuiU29bQrhKU5xlFnfC6qx1aW_wwZhKkeIoh0rmCy0yOBCLmiyXX4S4P9r-qglvsj8rGFnV2sVGVhdppU2uPNCHQ-j-0XvXFJx2G3KYpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f347ef349.mp4?token=BfgH6NCrmBKX4-eNoxxlLf1rDEzBwwbNXzI-8KW6750GY3XhRNkgVtOTlpq_QqAtemdxTwxXwPqh_lnak8WpRFhy0ONQFhcBY7rAfD9wAcBy2MTWC8Q7_UWOEf8sG2nlQOJGFKpYn8nm5SfHhQISIATbEF3N6uTw6NV0--3QCJgdaVa1WnuuPb8u_CdSxcMD_MaoGyiWlceljpNrH3l63TDefP_lBFcwjgk1PREhEVuUepuiU29bQrhKU5xlFnfC6qx1aW_wwZhKkeIoh0rmCy0yOBCLmiyXX4S4P9r-qglvsj8rGFnV2sVGVhdppU2uPNCHQ-j-0XvXFJx2G3KYpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلنسکی:
«بلافاصله بعد از پست ترامپ در تروث سوشال، روسیه حمله‌ای هدفمند به یک نیروگاه در خارکیف انجام داد.
معلومه که پوتین تروث سوشال نمی‌خونه!»
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/73150" target="_blank">📅 12:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73149">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f7cc0c459.mp4?token=KhYOMJdzJVccHchku5FxR2EWxA0o2QwQ9l2j8WReX69MF81SIUT_pQdqjY6KjkKum1hGp9U36tEj4f_MYm4Pc3Qrbeky6HO3syU5OgYSkjm7o7GBciRosnp4coxY7RKSrypaRnD9ZUGmV4gdonxoYBZ0NLMDyFgWRijJecnhv5Dw9PchwDrLwlfmh92AdpFIS0-mZq6UoSJJxHIdFxiqrUPVKiL3Vp_Ih085VPtPeo-kFRIMmaQOuqPrGlfSVShmZYGq0NIsAjo7b8Y402huaayfxEVSPt3LsEuZJMS-SdVdZudKcTKCeZ0a1xhIHtGcrFwKoFNvqa5BW_Tm0Yp8fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f7cc0c459.mp4?token=KhYOMJdzJVccHchku5FxR2EWxA0o2QwQ9l2j8WReX69MF81SIUT_pQdqjY6KjkKum1hGp9U36tEj4f_MYm4Pc3Qrbeky6HO3syU5OgYSkjm7o7GBciRosnp4coxY7RKSrypaRnD9ZUGmV4gdonxoYBZ0NLMDyFgWRijJecnhv5Dw9PchwDrLwlfmh92AdpFIS0-mZq6UoSJJxHIdFxiqrUPVKiL3Vp_Ih085VPtPeo-kFRIMmaQOuqPrGlfSVShmZYGq0NIsAjo7b8Y402huaayfxEVSPt3LsEuZJMS-SdVdZudKcTKCeZ0a1xhIHtGcrFwKoFNvqa5BW_Tm0Yp8fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه بیکارِ کنجکاو رفته بازی Resident Evil 4 رو روی نوکیا N95 دکمه‌ای پیاده کرده و همه رو به تعجب وا‌داشته :
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/73149" target="_blank">📅 12:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73148">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da351ee96c.mp4?token=MthMsGzEnQGXh2BLtPeFce6lrINjNzlHwx9T6wzRDliPbRrQ9XXmXQ8GLufjjr5zqMUGIZB_z-wLj0FFlCsuxBfNpRFbGJn3P3Fx0KN1ivdvieZ34jZYXEAwbP1Uo3JR2z1cXTmhTPuwqPUX26nQp9AUtrv6DbG7u5BEkKrbEmXhp0Lj_wc4QS0XC_LJMohn_JrxtTsk9UaMfCKjN65m8NMzvcPW-szBsgPpgMJzgxTqncLDX0Q4znIn0oFYHYmReoVUGEGvgBXOXsJYefHbhr-Gk3VlCURba38qffo2eEJjINnXSmOY711NPIny_mvAZP-jpgNb_X6xNAG73dYNaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da351ee96c.mp4?token=MthMsGzEnQGXh2BLtPeFce6lrINjNzlHwx9T6wzRDliPbRrQ9XXmXQ8GLufjjr5zqMUGIZB_z-wLj0FFlCsuxBfNpRFbGJn3P3Fx0KN1ivdvieZ34jZYXEAwbP1Uo3JR2z1cXTmhTPuwqPUX26nQp9AUtrv6DbG7u5BEkKrbEmXhp0Lj_wc4QS0XC_LJMohn_JrxtTsk9UaMfCKjN65m8NMzvcPW-szBsgPpgMJzgxTqncLDX0Q4znIn0oFYHYmReoVUGEGvgBXOXsJYefHbhr-Gk3VlCURba38qffo2eEJjINnXSmOY711NPIny_mvAZP-jpgNb_X6xNAG73dYNaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیسکو مذهبی هم آنلاک شد و توی تجمعات شبانه یه رپر آوردن و حامیان حکومت دورهم میخونن و میرقصن!
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/73148" target="_blank">📅 11:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73147">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73147" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/73147" target="_blank">📅 11:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73146">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W00-Ang5QQLViTHqxuOUaklajTLhE1vafyFNH0minSexh0yZ__1tjXTyg2NzOwS9hATe7xcfGChRzVbnUQu_tUWOL1WwUStLfA_MwMcwoPveAsY4lFfvhfYuCB7tmRyHm2ZndSVKzopPvW-CD7AyIjCbPEhabWTGtqVPIfrQWVFPzTeJ_INp7oFUzf-QDzge0V0L9de-XC1lU9dPhc74gm6HXDYEkKr3kV4I4BhpKUxFWs1EzovlKHsO0YVaHkPS9PpiwlsZ2_ZVUGvKke0VceKl1N-83LBJbQ6t58J2H5iRcbyyW4WMzU8WJ5C4b1irS6OYmvmkSrEnkXPsraaUmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
نیوکاسل
🆚
کاونتری
سویا
🆚
لوانته
ونزیا
🆚
آتالانتا
اودینزه
🆚
تورینو
نفتچی فرغانه
🆚
النصر
استقلال
🆚
الغرافه
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
http://T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/73146" target="_blank">📅 11:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73145">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291083b4aa.mp4?token=VMTtxxBbizIcatqkp4cUY_xJ9qrGlMD3gMT59e7iIQJcj0MsSRsRmL7sO2_Y5YPtd9el0HaBrAEb-r4wimwDgECVwOZOobLVrxhOlcZAuy35JTOmGlMVptPna4Ukcd12OkS2qtmydOji3bgLYc79xmzorj6eOKH-Wmhr2UaWHcQ0e_5z3oZ3Jkgvo0wdjIwK1HvFK_04QkKlGJHdCnAGDyTKbTVLqa__A-SfIJIZxuilouJDAEyqrvTqb9ZF6WG0h0puBX0xY_4FSNI8wgMA-uHEm0urQBd2TxbXaBJTKCKa1zjJqYPHoUSMUVhGmR_IFTuLwnvfh7ejJ4XS6ej7OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291083b4aa.mp4?token=VMTtxxBbizIcatqkp4cUY_xJ9qrGlMD3gMT59e7iIQJcj0MsSRsRmL7sO2_Y5YPtd9el0HaBrAEb-r4wimwDgECVwOZOobLVrxhOlcZAuy35JTOmGlMVptPna4Ukcd12OkS2qtmydOji3bgLYc79xmzorj6eOKH-Wmhr2UaWHcQ0e_5z3oZ3Jkgvo0wdjIwK1HvFK_04QkKlGJHdCnAGDyTKbTVLqa__A-SfIJIZxuilouJDAEyqrvTqb9ZF6WG0h0puBX0xY_4FSNI8wgMA-uHEm0urQBd2TxbXaBJTKCKa1zjJqYPHoUSMUVhGmR_IFTuLwnvfh7ejJ4XS6ej7OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف رائفی پور به باز بودن تنگه هرمز برای همه بجز جمهوری اسلامی!
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/73145" target="_blank">📅 11:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73143">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c29e4b6ff2.mp4?token=AMCbRRFjrLJhfyVpzVRA2_JnWuKfQvAK111MfahYIJkwWoM6uyUwJ727CLCQUOfdiNnXyoYXnoJKvXf6eh0ArvDp_aTrUnncJRqmZof9QDRI5DJks6BJOvrZp6-WcjOMqvy76flkz7RbQXn-NvysUBWDZFL2h4fcDi-8kF6lm0L7pmONfGk4oJxkq4lS9BY2ppgqvLiT1fHx-CrDfLs-boBptgmkipdD2jEyLxezP0i0n_CuKEqTNy68VRATu4IFBmwqbFOT_Upf4Jtvbn6J9a1bSZt-i3ua8knvcKfNrsGnIpmPjlqLPbOGLJFIh5DLVVBW_FD3swXXdO2aicyJjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c29e4b6ff2.mp4?token=AMCbRRFjrLJhfyVpzVRA2_JnWuKfQvAK111MfahYIJkwWoM6uyUwJ727CLCQUOfdiNnXyoYXnoJKvXf6eh0ArvDp_aTrUnncJRqmZof9QDRI5DJks6BJOvrZp6-WcjOMqvy76flkz7RbQXn-NvysUBWDZFL2h4fcDi-8kF6lm0L7pmONfGk4oJxkq4lS9BY2ppgqvLiT1fHx-CrDfLs-boBptgmkipdD2jEyLxezP0i0n_CuKEqTNy68VRATu4IFBmwqbFOT_Upf4Jtvbn6J9a1bSZt-i3ua8knvcKfNrsGnIpmPjlqLPbOGLJFIh5DLVVBW_FD3swXXdO2aicyJjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زینب ابوطالبی، مجری صداوسیما که سال ۹۸ گفته بود «مملکت مال حزب‌اللهی‌هاست، هرکی نمی‌خواد بذاره بره»، طبق گفته محمدرضا باهنر از ایران مهاجرت کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/73143" target="_blank">📅 10:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73142">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b195be8e00.mp4?token=FMsoq_wAO9V3PlFjFg0-lWSZQm8f285GE4YoPFHyiECNTmJh2zLnHGAnPtYbLLkKGYTRHgsd1LX658U6MLwAuAtSifsvIHGIkwXqnYBVP1v1IHH47EmeAEH1Uvi3cALPPZXByQzsCmJ7ybkJp503cuMLfQuGnAyg18ed-wnrgEA2egCMPjRB3g1W1zt3BDmOHoccn66hmcRs0e9V4Wbt_Kl-tkrZ7B7yKIi-fFs-DkFcIV-klzDXjeZGz2VGcB-aLEenfYvjAMB3QmaIHMsIhTsNeMXZsBS6N9R8Q-mhue7y-QtNOtgJjW77wvJPHlawJPnmV2kZO0IH_QHWV3K0cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b195be8e00.mp4?token=FMsoq_wAO9V3PlFjFg0-lWSZQm8f285GE4YoPFHyiECNTmJh2zLnHGAnPtYbLLkKGYTRHgsd1LX658U6MLwAuAtSifsvIHGIkwXqnYBVP1v1IHH47EmeAEH1Uvi3cALPPZXByQzsCmJ7ybkJp503cuMLfQuGnAyg18ed-wnrgEA2egCMPjRB3g1W1zt3BDmOHoccn66hmcRs0e9V4Wbt_Kl-tkrZ7B7yKIi-fFs-DkFcIV-klzDXjeZGz2VGcB-aLEenfYvjAMB3QmaIHMsIhTsNeMXZsBS6N9R8Q-mhue7y-QtNOtgJjW77wvJPHlawJPnmV2kZO0IH_QHWV3K0cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبتای این خانم در مورد کادوی روز دختر و گل‌های چند صد میلیونی که این روزا بلاگرا به پارتنرشون کادو میدن، حسابی وایرال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/73142" target="_blank">📅 10:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73141">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/479627e865.mp4?token=TtW6LuVq8dRXvf76g6zNd0P3ztYiiKQvRk2C02ZMT0J6geRGYgdFONn9Y5mZPDfKdKmZuvr93cM_0jYg8nLxBMJHUCYnTRfgitpR8BWREYlQ-mPoKWw0IEOTuRJj5MJJX0T6gYCysQvCbdTlQfMFNOfs09l8NCxGkdZBwAhSx-KxPmgh1LdRfFvmhWk5gRuEfMrWlaHv4ENr6C7vEY14bCmLU18EBIr5udoLCckKys1E09J3sHkXkycIRbdPmWsKThuqfYrEOCTwbi7FJSsJYp5o0UnE7djaBt2AEl2rz7ThHbTuCiAan9YTQE7SLXVFymZhpWVz4RhjUCWHZhi0xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/479627e865.mp4?token=TtW6LuVq8dRXvf76g6zNd0P3ztYiiKQvRk2C02ZMT0J6geRGYgdFONn9Y5mZPDfKdKmZuvr93cM_0jYg8nLxBMJHUCYnTRfgitpR8BWREYlQ-mPoKWw0IEOTuRJj5MJJX0T6gYCysQvCbdTlQfMFNOfs09l8NCxGkdZBwAhSx-KxPmgh1LdRfFvmhWk5gRuEfMrWlaHv4ENr6C7vEY14bCmLU18EBIr5udoLCckKys1E09J3sHkXkycIRbdPmWsKThuqfYrEOCTwbi7FJSsJYp5o0UnE7djaBt2AEl2rz7ThHbTuCiAan9YTQE7SLXVFymZhpWVz4RhjUCWHZhi0xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش شبکه یک صداوسیما:دانش آموزان معترض فرانسوی، می‌تونن بیان تو مدارس ایران که همگی فول امکانات هستن، تحصیل کنن.
شما هیچ معلمی ندارید، پلیس هم داره دستگیرتون می‌کنه.
ما اینجا کلی معلم اضافه و کلاس خالی داریم.
اینجا ما آرامش داریم و همه چیز عالیه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/73141" target="_blank">📅 09:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73140">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22084c4b3c.mp4?token=iHjajJSrhI4OJ2G3OelI51y_rDrYdw1riUxzO6T13Fh6oBb0fbtAFt7ehWU6EM_D6NvwZx9iSCDgyTXVkwyKsxhofbeJ0NcDcT0km4RtnVcFaN25Niz4Otmu0MoAmxhSFhHvWl6TF2jE0hbGyjWoApaHPkfCs5Sh0kiRaZh25eIUgwwQc8wsQazjI0wUXAprGOfNsCFrh29vfBVWXvwLQ9ayz3bAiaeBFbhoBMLa8Aa6MaPcB8CRdQbo6nkVvhe7LYcy9qo2mrGEPUd-rpuJPmaWUi2x0oIvb3pQfeTSXT8CZtUWUdVoipYfy7Eftuda8D83M0a5JdIJV1WX-dyhDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22084c4b3c.mp4?token=iHjajJSrhI4OJ2G3OelI51y_rDrYdw1riUxzO6T13Fh6oBb0fbtAFt7ehWU6EM_D6NvwZx9iSCDgyTXVkwyKsxhofbeJ0NcDcT0km4RtnVcFaN25Niz4Otmu0MoAmxhSFhHvWl6TF2jE0hbGyjWoApaHPkfCs5Sh0kiRaZh25eIUgwwQc8wsQazjI0wUXAprGOfNsCFrh29vfBVWXvwLQ9ayz3bAiaeBFbhoBMLa8Aa6MaPcB8CRdQbo6nkVvhe7LYcy9qo2mrGEPUd-rpuJPmaWUi2x0oIvb3pQfeTSXT8CZtUWUdVoipYfy7Eftuda8D83M0a5JdIJV1WX-dyhDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که روبیو درباره خشایارشا صحبت کرده و باعث شده عده زیادی از طرفدارای حکومت عصبی بشن، یادی کنیم از مصاحبه قدیمی خامنه‌ای درباره خشایار‌شا که دوباره وایرال شده؛ جایی که می‌گه خشایارشا با بیش از یک میلیون سرباز به یونان حمله کرد، شکست خورد و هیچ منفعت ملی‌ای برای ایران نداشت!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/73140" target="_blank">📅 09:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73139">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73139" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73139" target="_blank">📅 01:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73138">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCCEgHzViXj1Sio8idcTUJPQOL9X4LkZp5Z7bsRcOCpY2T-jRAQkhJ1KiyG-iNvU2hchjuqQ0wVPc4jzrY_r-a5xOesaAjzXAteIfUCcNociSM8T8qrl_xfr94E-yfwL0sSuDcTPXIWlkorUBHwHv2VAK6yO5MhJkmsOPB9iDhOgwz2qWL8oHRguOW9cjrqnyKmL8MRfdszfdV8pUtlwNtGJfKF7GFPCeoXYib6Kh0SCKqJ4Ny-9F5iNMTDkSLY6n1GAJpSeKGU6OarCxc0mMwnGDrzl4EMmF9RNaz35G8JC8wLKhv1ywCD-CMsietZwbByVX2Br0tYJSRmBZqapYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
[
قوانین رو در سایت مطالعه کنید
]
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/73138" target="_blank">📅 01:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73137">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoPUgbsSqSxeUfGaCWipZQnHEDp2AALA-fEwPGlZZ6VfTOpg-L6ckU6ApHUnRm6eGwhPrNvwgUZoYSwek8URv7jqEjjiTQKJCrAf2VqLu3qz1D-G0OtGA8qzdraeDUUYYhPWHUX79YkOc609IwFCv9rlCb6jDxhgSM6w2EsiSEpF_I2o3x7Zid2Je_tvW2A1dadxBuJ7Pl00pAEc75RMEbYAKzAOHvlU727QUITh5YLm936xM-D3wyjP86X95QloKGZTpktyqvcQTk7Rz9bxGy0Ykgn9mKDcIU7dyhkKEy6LlMsvsdv0FG9g9DZkmZCd36orONHnUpRAdrVJ2nXRSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:
«آمریکا با بعضی از شروط هفت‌گانه ایران موافقت کرده، اما از نظر ما پاسخ آمریکا کافی نیست.
دیپلماسی ایران تغییر کرده و دیگه اوضاع به شرایط قبل برنمی‌گرده.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/73137" target="_blank">📅 01:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73136">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ویدئوی لحظه اصابت موشک حوثی‌ها به فرودگاه ریاض
تصاویر دوربین‌های مداربسته، لحظه اصابت موشک بالستیک حوثی‌ها (انصارالله) به ترمینال ۳ فرودگاه بین‌المللی ملک خالد در ریاض، در روز گذشته رو نشون می‌ده.
بر اساس این گزارش، دست‌کم ۱۳ نفر کشته و بیش از ۳۰۰ نفر زخمی شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/73136" target="_blank">📅 00:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73135">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c13d27cb81.mp4?token=Xu86Ts54s60qtSGvX0eCi_8gjNCL5di74Qovuc_uip3e0u___6X1-rIl6iGJ78wEdl0fyiB_nVbdvhEbrTRKFgSTUTMV73yemJDbXRVWgPbWDiHNn78SdBsG7m6GHCH4RpbxXtgFy5BOgD98_TSKNPB5ABd5Ye_pOFsu4ofCRz_k2u5kDV7vCRp-YxQm_s5ZcvvlJhEEG2nq-zLjPNm3GaPwTalKvsJvgpjUJPs5zHSYb3r1NJV8JFn4mcQBhjylAS7W8bke29M5PXgMzI4dRsUVLKzf0MxBKhZs9f9iImbWHjndBm0CPYiZBvMRLNfjQasDj_NVbjqNOVCTESsmVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c13d27cb81.mp4?token=Xu86Ts54s60qtSGvX0eCi_8gjNCL5di74Qovuc_uip3e0u___6X1-rIl6iGJ78wEdl0fyiB_nVbdvhEbrTRKFgSTUTMV73yemJDbXRVWgPbWDiHNn78SdBsG7m6GHCH4RpbxXtgFy5BOgD98_TSKNPB5ABd5Ye_pOFsu4ofCRz_k2u5kDV7vCRp-YxQm_s5ZcvvlJhEEG2nq-zLjPNm3GaPwTalKvsJvgpjUJPs5zHSYb3r1NJV8JFn4mcQBhjylAS7W8bke29M5PXgMzI4dRsUVLKzf0MxBKhZs9f9iImbWHjndBm0CPYiZBvMRLNfjQasDj_NVbjqNOVCTESsmVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مدارس پسرونه، اسپایدرمن تبدیل به اسپایدرعن شد :
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/73135" target="_blank">📅 23:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73134">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad58aeb38.mp4?token=A4UvPRtoT-rScbunaNNFcFhvW_zw4oBzfH4-VARKaKckcKbp8QCttnkDsyyHvHDF8ZjBHT3Kz741fnFzdHVnGnL49ECREANx4_WCDOVc1uWJP7iwpF_ymSFBE8959DOdBLSxoC9F1Rrr-g0fgN_GegDmloJP5RUir9luOiK0mPXn3yN0A-ntcK23LbcqNx4co6r_RIJQEVhS02VlX3jsF_LeVRHRmYtOl1CgSnWlvCYgY4cMZZcVb0Tni8QVvN8mX5uxU28AN0XcBBuzjJPXmEVkxRcnxZwfuRrNyb9obG-fhpnQC7tRXmh0995A61_cAvNyLe5xRy_RgFW82JyKRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad58aeb38.mp4?token=A4UvPRtoT-rScbunaNNFcFhvW_zw4oBzfH4-VARKaKckcKbp8QCttnkDsyyHvHDF8ZjBHT3Kz741fnFzdHVnGnL49ECREANx4_WCDOVc1uWJP7iwpF_ymSFBE8959DOdBLSxoC9F1Rrr-g0fgN_GegDmloJP5RUir9luOiK0mPXn3yN0A-ntcK23LbcqNx4co6r_RIJQEVhS02VlX3jsF_LeVRHRmYtOl1CgSnWlvCYgY4cMZZcVb0Tni8QVvN8mX5uxU28AN0XcBBuzjJPXmEVkxRcnxZwfuRrNyb9obG-fhpnQC7tRXmh0995A61_cAvNyLe5xRy_RgFW82JyKRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: اگر لازم باشد برق اتاق‌های دولت را خاموش می‌کنیم اما نمی‌گذاریم چرخ کارخانه و تولید متوقف شود. مردم همکاری کنند فشار دشمنان شکست خواهد خورد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/73134" target="_blank">📅 23:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73133">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67b9ee6a71.mp4?token=FlZhEcJ_s-GAGDqoPMU4FKRZiZRNPWmPcDHYzTIl12hNeVf_4y7dCs6X6kGl0wzmxxpDT2dSZNa564gPXmNvrSlnfjXL0TDsLG6Ziq1-jD3ys-c_HPVu7kk_hXLoM_EbMcNx02McgOONUyUpZXdNtp8ODFViPZE4TyiyxgUXpysX20lZpj4fTWfJoyg2W04n8gf_stmWMy0a_Dtm5GoYMR4OnwqjF-Pw7gpx50BMRsv7QJdYIWn0pTTHbyv6V1t-chCR-sAqisOzdA_AMlmFXqtQ_OKM0vcrx1hXZdvJinaRi25FCdFQqj34s2E_KQje8bzrMbTdXOqafZNTmSR7LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67b9ee6a71.mp4?token=FlZhEcJ_s-GAGDqoPMU4FKRZiZRNPWmPcDHYzTIl12hNeVf_4y7dCs6X6kGl0wzmxxpDT2dSZNa564gPXmNvrSlnfjXL0TDsLG6Ziq1-jD3ys-c_HPVu7kk_hXLoM_EbMcNx02McgOONUyUpZXdNtp8ODFViPZE4TyiyxgUXpysX20lZpj4fTWfJoyg2W04n8gf_stmWMy0a_Dtm5GoYMR4OnwqjF-Pw7gpx50BMRsv7QJdYIWn0pTTHbyv6V1t-chCR-sAqisOzdA_AMlmFXqtQ_OKM0vcrx1hXZdvJinaRi25FCdFQqj34s2E_KQje8bzrMbTdXOqafZNTmSR7LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کلیپ مربوط به پشت‌صحنه یه تئاتره؛ جایی که همه با هم دست می‌دن و همدیگه رو بغل می‌کنن.
+ عرزشی‌ها هم از این صحنه به خشم اومدن و می‌گن باید این بساط جمع بشه؛ حالا هم افتادن به جون عوامل تئاتر!
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/73133" target="_blank">📅 22:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73132">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3915a2c4be.mp4?token=qFxQqLTw0spNNpRgRg3aMJQxbf0i6IOYgxJBdPrhK0xFQu75FjOj__9yqXl4SZb4TFBIiKhWNckqq_Oia8TTiyXr86VlnO978hdT0QwsOXP0nNk_UHeucgD6InBSfeAXMZGAsb9rzPdk8M1yq72jvnBgqqOXlKI3Hla9BsMb7_FrfX2IhJ6XN04L9J_dkedGy6Y1B7OyfyuKcKTFz0_ADx1HgOYax7BfaMIcdeVfqW8ehP4_BiSl2WISeuG0iC8yuX3TcPmPk6en21DPhoGyWnxvcC7teRUUqwGnw_hcyfTZzUmH68kr_RzB-BrTumT8R2vKx2VWQT1FWUmbAfUExw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3915a2c4be.mp4?token=qFxQqLTw0spNNpRgRg3aMJQxbf0i6IOYgxJBdPrhK0xFQu75FjOj__9yqXl4SZb4TFBIiKhWNckqq_Oia8TTiyXr86VlnO978hdT0QwsOXP0nNk_UHeucgD6InBSfeAXMZGAsb9rzPdk8M1yq72jvnBgqqOXlKI3Hla9BsMb7_FrfX2IhJ6XN04L9J_dkedGy6Y1B7OyfyuKcKTFz0_ADx1HgOYax7BfaMIcdeVfqW8ehP4_BiSl2WISeuG0iC8yuX3TcPmPk6en21DPhoGyWnxvcC7teRUUqwGnw_hcyfTZzUmH68kr_RzB-BrTumT8R2vKx2VWQT1FWUmbAfUExw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه مدعی شد سومین نفتکش از دیروز تاکنون در جنوب تنگه هرمز با مین دریایی برخورد کرده و دچار انفجار و آتش‌سوزی شده است.
سپاه هشدار داد با کشتی‌هایی که سامانه‌های ناوبری و شناسایی خود را خاموش کنند، به‌شدت برخورد خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/73132" target="_blank">📅 21:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73131">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11e4cb03a5.mp4?token=NrPQlUI10NuGhLJxsLE_8v4P0PTcV1vIJ3KDsZ8zZrWv_0zzboYKcO83VJxs1nAyRttCa60iYRNwOWa5zwIVZP0NvvmhUzHAxXfxzYBxtMB-PsgET8qICvhphclGUsoKqxKoxsZnAIZocLKdbtI4wq5h1VDpjozJ_EA0SVdl-1bdYEU2em9iGVZHrf8wtrlOsSy2EpiDGAZuG8eLkfNoZ6Qthqlj0hBh6kKSblRa-zaUn1d28EdWrtDjEJCNokbZ9hhKNdCd7NF4WXp175QuZcLv8dr3hEmuqDD0aQFqroNEkDcgULD-ZejDfrgnJwucMOiieglywgxqIfNEVR8_og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11e4cb03a5.mp4?token=NrPQlUI10NuGhLJxsLE_8v4P0PTcV1vIJ3KDsZ8zZrWv_0zzboYKcO83VJxs1nAyRttCa60iYRNwOWa5zwIVZP0NvvmhUzHAxXfxzYBxtMB-PsgET8qICvhphclGUsoKqxKoxsZnAIZocLKdbtI4wq5h1VDpjozJ_EA0SVdl-1bdYEU2em9iGVZHrf8wtrlOsSy2EpiDGAZuG8eLkfNoZ6Qthqlj0hBh6kKSblRa-zaUn1d28EdWrtDjEJCNokbZ9hhKNdCd7NF4WXp175QuZcLv8dr3hEmuqDD0aQFqroNEkDcgULD-ZejDfrgnJwucMOiieglywgxqIfNEVR8_og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم وایرال شده از جشنی که یه خونواده، برای اولین پریود دخترشون گرفتن:
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/73131" target="_blank">📅 21:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73130">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa77f7e16d.mp4?token=AoIJ3iV9MeMe-A7bya7T3daQDHWfdKKYPEyQGmM_yQAejuM77pzQVf1yYFs93FT01RCN7xxwP71TjiAsbTfFP-tt20Cr8g-8Go0Dg0FuJ_cPiI4hPgOmrXj6yGunEKjiqOLpKS8xvk5Y2r9y99Wri27ekYvjCXYj994F5tyBuNgMwMdXgHDRPmrFn3Mi4HtUxHNpeQ7JI9naGOpbllxrlzATJuJ7hSJuCHA8sZcgnrsBzw7IcV-p_cp8Rm_JkYYQD3t5KL-lqVpfu-jvJfAyO9LK2CI9FBjOgRPD_grwk0MX03BSd4vswioaIeAlkehB577LEAvxY5YP9X0oUjxrXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa77f7e16d.mp4?token=AoIJ3iV9MeMe-A7bya7T3daQDHWfdKKYPEyQGmM_yQAejuM77pzQVf1yYFs93FT01RCN7xxwP71TjiAsbTfFP-tt20Cr8g-8Go0Dg0FuJ_cPiI4hPgOmrXj6yGunEKjiqOLpKS8xvk5Y2r9y99Wri27ekYvjCXYj994F5tyBuNgMwMdXgHDRPmrFn3Mi4HtUxHNpeQ7JI9naGOpbllxrlzATJuJ7hSJuCHA8sZcgnrsBzw7IcV-p_cp8Rm_JkYYQD3t5KL-lqVpfu-jvJfAyO9LK2CI9FBjOgRPD_grwk0MX03BSd4vswioaIeAlkehB577LEAvxY5YP9X0oUjxrXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی سازمان انرژی اتمی: منافعمان را یا با دیپلماسی می‌گیریم یا با نبرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/73130" target="_blank">📅 21:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73126">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf520c338.mp4?token=T7jJzmq64H85Eu-8oNl2b-MAcGzoeWIUT3WtJj9oZNEFwWIrbbz6N5ola12JfldogxDfhqh4Vn6jRUD82qyTsiq9McSSOh0a9e0PdNYtAtuEzSgS5uBFqSePU-9EUflYWLBEiMrOkyqQ1oWdvZJgQNXSu-cmiepX9QZ9jxuXEE4py-0Hf_sSW3ofcGk-x46jm3uIy6XQO8_7MmPoIvcbEcrRUPhP3E849XwzkGWM5BLp5Y6cCS6ShLCg3e-hmuTMGqXvmYjcZgTq95fNu9Oa7pGixdX_kKel4MKWmLSOf1ir486zxLx8RTmB1Iz807Qqh1NpgqbHeYDbKY-QWz3xHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf520c338.mp4?token=T7jJzmq64H85Eu-8oNl2b-MAcGzoeWIUT3WtJj9oZNEFwWIrbbz6N5ola12JfldogxDfhqh4Vn6jRUD82qyTsiq9McSSOh0a9e0PdNYtAtuEzSgS5uBFqSePU-9EUflYWLBEiMrOkyqQ1oWdvZJgQNXSu-cmiepX9QZ9jxuXEE4py-0Hf_sSW3ofcGk-x46jm3uIy6XQO8_7MmPoIvcbEcrRUPhP3E849XwzkGWM5BLp5Y6cCS6ShLCg3e-hmuTMGqXvmYjcZgTq95fNu9Oa7pGixdX_kKel4MKWmLSOf1ir486zxLx8RTmB1Iz807Qqh1NpgqbHeYDbKY-QWz3xHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی امروز گسترده‌ترین رزمایش نظامی خود از ۲۸ فوریه تاکنون را با مشارکت سپاه و نیروی هوایی ارتش برگزار کرد. تصاویر منتشرشده، پرتاب پهپادهای انتحاری شاهد-۱۳۶ و موشک‌های بالستیک و پرواز جنگنده‌ها بر فراز تهران و شهرهای دیگر را نشان می‌دهد؛ تحرکاتی که می‌تواند نشانه آمادگی ایران برای دور تازه‌ای از درگیری باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/73126" target="_blank">📅 20:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73125">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">محسن رضایی:
«اگه جنگ دوباره شروع بشه، خیلی از کابل‌ها، دیتاسنترها، مراکز هوش مصنوعی و زیرساخت‌های دیگه تو منطقه نابود می‌شن.»
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/73125" target="_blank">📅 19:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73124">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naZQv5j6Ti-yZ-HkIddKn5D-l_gfuiUr3BcE4twJu5kJEPjkbbOak2FSbXlSJjuFb8N2yDAO-kgqsWc5aWYHQEiHzYYL1-1ayR6nknuKIWh3nlt3hKF2lVm8_lfmgCU8F0rZ7t08uk8CNX3YVIp1d4Gx1NIHctImt9qLF8iy7XaKd7a3XdbQaf7p4aq-ruerIdBcvBVQbfpzedLEv0MlFCgqlosi8LRTSCcmxxX6N3JvtQ-5DsKg36V5PbAggX9wcg_iJflfVLdEOXZLYstjDYAY5ka9v2MWSxjWke66VnojtgS73jUbXLSPJ3ODPYyIWM13l25TuOsiOKrvGl4voQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی:
«ترامپ به قاچاق روی آورده و با استخدام تعدادی مجرم که در آب‌های ساحلی عمان فعالیت می‌کنن، این کار رو پیش می‌بره.
اون هر روز ادعا می‌کنه تنگه هرمز بازه؛ اما من در پاسخ می‌گم شما مشغول قاچاق هستید، در حالی که تنگه هرمز تحت کنترل ایرانه و ما مدیریت اون رو در دست داریم.
طی چند ماه گذشته، هر شب پنج شناور مورد استفاده قاچاقچی‌ها رو در تنگه هرمز هدف قرار داده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/73124" target="_blank">📅 18:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73123">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee20290170.mp4?token=OO5CEL7fLEbx668hKw7CNs51qJT4fR6oInYfMghOHbqo55dXvhs3_IduvrQJsyE-V7yNbu2WrqCpfVWaWSuzvFw9XNy6QOXPSX_3PlkknXxYQeZYgKTtVF6bJAVy5DNp5nGNSjWiyVYsgffmxejL0UkGFg2xVQqMyW_iLTnxlafvYYq8JRkZ8fKxTvG8-qYsWU1zb0LxWxVUu3kz9yPz2wuUtfIxUUd0IkGsotcLuOKgMR6qtBjWUXksBj5NxBBdxJgoBF3v94lVnjBGDC6ABVQpv4lrY-lrgKdqj1jJFse4bOJ15zCPGsSkbgqkGR-nd_uLbFyJ7AcB6aFEIoCr8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee20290170.mp4?token=OO5CEL7fLEbx668hKw7CNs51qJT4fR6oInYfMghOHbqo55dXvhs3_IduvrQJsyE-V7yNbu2WrqCpfVWaWSuzvFw9XNy6QOXPSX_3PlkknXxYQeZYgKTtVF6bJAVy5DNp5nGNSjWiyVYsgffmxejL0UkGFg2xVQqMyW_iLTnxlafvYYq8JRkZ8fKxTvG8-qYsWU1zb0LxWxVUu3kz9yPz2wuUtfIxUUd0IkGsotcLuOKgMR6qtBjWUXksBj5NxBBdxJgoBF3v94lVnjBGDC6ABVQpv4lrY-lrgKdqj1jJFse4bOJ15zCPGsSkbgqkGR-nd_uLbFyJ7AcB6aFEIoCr8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گزارشات رسانه‌های عربی حوثی ها مجددا به فرودگاه ریاض حمله کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/73123" target="_blank">📅 18:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73122">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">زلنسکی در گفت‌وگو با باراک راوید:
«اعلام آتش‌بس برای من هم خبر جدیدی بود. اما اگر روس‌ها با آتش‌بس در حوزه انرژی موافقت کنن، اوکراین هم موافقت خواهد کرد.
اگر رئیس‌جمهور ترامپ این توافق رو با پوتین مذاکره کرده، لطفاً به ما بگید آتش‌بس از چه زمانی شروع می‌شه. ما آماده‌ایم و این توافق رو می‌پذیریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/73122" target="_blank">📅 18:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73121">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRPB4HnEa-cb8BGuYk8teATFP9TFI9boWOStdMt5rxjIege8ftcPCnB7N3QtvpTmdepBf3tt3ZG0r_Fk-D4igYMuo5PeGRAV2ShtkXAT2_FXvQwhF-63qzoqNiZGVLzyJgu0E3G1LQ7HCttS4NSAlPITpQu4ra2biUwEmlcVzmI7B1ZhM5kIQY4Pl1QXJra-qLMhvsOw9S0cs34T5vavLQ1pMvqanm3H8yNdmpfMJ16k8Iy6LDGozlSm1t4TPWlD3PMSyJSrXpQMjUwqhq_-0fCbF73O0t-zrPBm7GoXJkB4hLfk9Qvb-Aww18aUwKdqmplARdF38HLCbj8VcZrDGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ از آتش‌بس انرژی بین روسیه و اوکراین خبر داد
«از همین لحظه، آتش‌بس در حوزه انرژی در جنگ روسیه و اوکراین برقرار می‌شه.
هر دو طرف با این توافق موافقت کردن. این آتش‌بس رو نقض نکنید!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73121" target="_blank">📅 18:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73120">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73120" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/73120" target="_blank">📅 18:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73119">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qz98HPBrzfgd3F7FoV8AxLD6are9jMsLfMLs5wVfuvKIZooKeEux9FLeS4rowEIkPxdFP3149FkIKwjbBUYSsMbNCfXE3N8A1PXuom3AGFpVthZwjZR7gW0wK-dr3VGfMGd0SoOXTOAK_FqgW6rum5jEgOmNaCJJiGnAp38oKHZARh9LLKFVbQup0JoiJyMTw1AEAeQE4aLm6mUVUBDfWJCD6AjoCz-HNp2d5N_1MZVc_ln34FmbVsCw24FnfFgRGQ818K-Na8VAX6RHN-0WmzTQtVUKwj5Ul_2O3_SuPZUaylCpLJB9G1u72-sq9wCCm-8ePoWSpSJX3zotJsHavw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز منچستر سیتی
🆚
لیورپول
را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
منچستر سیتی: ۵ برد و ۱۴ گل زده
لیورپول: ۴ برد، ۱ تساوی و ۸ گل زده
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/73119" target="_blank">📅 18:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73118">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb6d17c940.mp4?token=MBV8vicQQuFwDTKyOB03jJoDfMXjBsVqog2JeuWdyT5Om1b_PLv1BbpdHkBaUn0Or7XpKTrMAAkgnq26RQBbsLonhkT0VGfrfQdTEvJLg-9liu8IVs_ZL7EDInNeVg1Vov1dx8k6sTPfooIddsUZTGIwWgWdgBkGxJvXbzvL_tx4Ouejl3VQTY1Ba6vpyS1AW7l16XHOGiiY8tA7TvF6GWSDUfKBgS0zS05PcsMcUYLyqhvD-JnDvALMyNlzlesYnh0Ybz2ejdwyRnjpTJ24R9erRsLIjIUid_e1lI2UTO8oe1xGAO0EnRV7Wj3CdBLWiNqQTB2taPD3lWrko2cwyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb6d17c940.mp4?token=MBV8vicQQuFwDTKyOB03jJoDfMXjBsVqog2JeuWdyT5Om1b_PLv1BbpdHkBaUn0Or7XpKTrMAAkgnq26RQBbsLonhkT0VGfrfQdTEvJLg-9liu8IVs_ZL7EDInNeVg1Vov1dx8k6sTPfooIddsUZTGIwWgWdgBkGxJvXbzvL_tx4Ouejl3VQTY1Ba6vpyS1AW7l16XHOGiiY8tA7TvF6GWSDUfKBgS0zS05PcsMcUYLyqhvD-JnDvALMyNlzlesYnh0Ybz2ejdwyRnjpTJ24R9erRsLIjIUid_e1lI2UTO8oe1xGAO0EnRV7Wj3CdBLWiNqQTB2taPD3lWrko2cwyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت درباره ایران:
«نمی‌دونم این ماجرا چطور تموم می‌شه؛ هیچ‌وقت نمی‌شه از قبل دونست پایانش چطوریه. دیوار برلین هم بالاخره یه روز، یهو فرو ریخت.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/73118" target="_blank">📅 17:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73117">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4be03fff7.mp4?token=Wb6u2xNB-yyKqGf2snbWgQK7aUo-L-tPff8F4p_b7MfJCL5tEySks01VLB--SuJne8GEGJmT7B3YLJ9J1O4-5pboZ15DqNUFqX7I16k0PJ7BkT7PHjJfb8RIRyi45wUqY38MeEfQ3rL5nI-ct8XpZS8_Gh8tUiPmbVGk3Z1Vwem_9XA6UIWblqfxM9MSDdT4DHf2XSjC5K_qOuiUj1pA57GI54iPYHa6eVbx6D-AQboB5VAgjrJy257XEV_201MJ-x6_HGJv0Te94Iu2YZNcJosH0SmRbelb-_jW5NGjYjw9nyN0j8-DZeo-hFIlTsPRhF2HFjPGJEgX8Vcci3RH4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4be03fff7.mp4?token=Wb6u2xNB-yyKqGf2snbWgQK7aUo-L-tPff8F4p_b7MfJCL5tEySks01VLB--SuJne8GEGJmT7B3YLJ9J1O4-5pboZ15DqNUFqX7I16k0PJ7BkT7PHjJfb8RIRyi45wUqY38MeEfQ3rL5nI-ct8XpZS8_Gh8tUiPmbVGk3Z1Vwem_9XA6UIWblqfxM9MSDdT4DHf2XSjC5K_qOuiUj1pA57GI54iPYHa6eVbx6D-AQboB5VAgjrJy257XEV_201MJ-x6_HGJv0Te94Iu2YZNcJosH0SmRbelb-_jW5NGjYjw9nyN0j8-DZeo-hFIlTsPRhF2HFjPGJEgX8Vcci3RH4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت درباره ایران:
«اگه این ایرانی‌ها کشورشون رو دوست دارن، خب تبریک می‌گم؛ می‌تونن همون‌جا بمونن!
این فشار مستقیماً به نخبگان و مقام‌های حکومتی ضربه می‌زنه؛ دیگه نمی‌تونن برن لندن و اقوامشون رو ببینن، تو پاریس به دیدن دوست‌دخترهاشون برن یا به پول‌هاشون در سوئیس دسترسی داشته باشن.
اونا از دنیا جدا شدن و ما به ادامه این فشارها ادامه می‌دیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/73117" target="_blank">📅 17:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73116">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cfeac3aa6.mp4?token=AVC-Pe2ZfDRT1WUrce0EPg33lW1dT9IIAZ96vZ_zJjUyI8YOvzRGkd-XXH1mmpih6wl2ZdMBaJ4vcZIw1ZkXOfeSv7m60k7y9XW1vTbai1rnkbdymL-hEV_3LLS2qKWBTNQ20dNpjQjt5R7J3cptazxwM0JW74yk8VQ2HDx3m1r5HJeyzWv-2k-R5g1aw2jt23iSgv4T2MIQJljge0msFFhetCF_DsR2otUqWdL_z1XzE3VUuYE8XWo2ZUYZKOHlTSwiZS2_LBkU5ipS5wpNc0Wri9dhv-UguXBGiVhHIh24uw5KyWcIXtBSvM8ihteqM6Z6ek4Q5Yg04HmUMSgrrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cfeac3aa6.mp4?token=AVC-Pe2ZfDRT1WUrce0EPg33lW1dT9IIAZ96vZ_zJjUyI8YOvzRGkd-XXH1mmpih6wl2ZdMBaJ4vcZIw1ZkXOfeSv7m60k7y9XW1vTbai1rnkbdymL-hEV_3LLS2qKWBTNQ20dNpjQjt5R7J3cptazxwM0JW74yk8VQ2HDx3m1r5HJeyzWv-2k-R5g1aw2jt23iSgv4T2MIQJljge0msFFhetCF_DsR2otUqWdL_z1XzE3VUuYE8XWo2ZUYZKOHlTSwiZS2_LBkU5ipS5wpNc0Wri9dhv-UguXBGiVhHIh24uw5KyWcIXtBSvM8ihteqM6Z6ek4Q5Yg04HmUMSgrrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت:
«بزرگ‌ترین بازنده در این ماجرا، حکومت ایرانه.
اونا سعی کردن با بستن تنگه هرمز، مسیر عبور و مرور رو تحت فشار قرار بدن؛ اما این کارشون جواب نداد.
بعد تلاش کردن با بالا بردن قیمت گازوئیل، فشار ایجاد کنن؛ اما این یکی هم دیگه جواب نمی‌ده.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/73116" target="_blank">📅 17:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73115">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d595a9a29.mp4?token=gqvQa90h0Lcba4ddh1D9r6fBtag3__yaD0Y9ZoDmA1E_tF4BaMZBdmPDfwr9K3n3V4VHN3dhXvGvhZmyoGdbgz__6XjkX7KrovTKK3S0bNoeK4EbCSY6CnbaX7pruTs4ymTo83uci_LN6NYeiykBtvJqK57rqoTGR0LWaP1QJHh5PvH38eG0AmkPHB3ZBtkoOHYL3LC6aGmRg44miJAvOO9IKuKttvj3S-2RORNdGeOjismTekGtocsfFMLPnJ2fPjafEC-e2-10CQavYcv4d7llhz2l0IOjbLSfh00WcfC-Hvp5haiwDhy5SnMotGNYCkYIFDVTs7o_f1zVNHiItw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d595a9a29.mp4?token=gqvQa90h0Lcba4ddh1D9r6fBtag3__yaD0Y9ZoDmA1E_tF4BaMZBdmPDfwr9K3n3V4VHN3dhXvGvhZmyoGdbgz__6XjkX7KrovTKK3S0bNoeK4EbCSY6CnbaX7pruTs4ymTo83uci_LN6NYeiykBtvJqK57rqoTGR0LWaP1QJHh5PvH38eG0AmkPHB3ZBtkoOHYL3LC6aGmRg44miJAvOO9IKuKttvj3S-2RORNdGeOjismTekGtocsfFMLPnJ2fPjafEC-e2-10CQavYcv4d7llhz2l0IOjbLSfh00WcfC-Hvp5haiwDhy5SnMotGNYCkYIFDVTs7o_f1zVNHiItw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت:
«کارگرها دیگه سر کار حاضر نمی‌شن.
ایران به بازار دلار دسترسی نداره، برای همین کاری که می‌کنه، چاپ کردن پول بیشتره.»
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/73115" target="_blank">📅 17:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73114">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cbe1e496c.mp4?token=EXSkshrXDegECmpBApbqS6cdzJUQ2Y63CgfZbIbaMkfX-ueL14Y_PdoNJ00f1YLxUGsOZE7XUP4Sew-sph1XXfFSFtP4QW3uYLIbPmm3yJAdScmvR4tGKcaowfd-xBtACAMcqbbABtAyUUeJs8Ewy6AEuhgTdeMnnXpg7yNZcC_0D0QdKezLoxQ30J3kYTQgipC5r7-Yevdou2BTSL2Szof3dMoo_Oz2maj_dt3AVoLGxajJqUvrvm6luWqYNe32YHqWPmTQMSSF3ChSbZm46kuJJISZ68AGMh4Hl0S9GB-hg5yNC0OpwfO0H-fip9WaCYCCYWVuip64iLcy-sqTsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cbe1e496c.mp4?token=EXSkshrXDegECmpBApbqS6cdzJUQ2Y63CgfZbIbaMkfX-ueL14Y_PdoNJ00f1YLxUGsOZE7XUP4Sew-sph1XXfFSFtP4QW3uYLIbPmm3yJAdScmvR4tGKcaowfd-xBtACAMcqbbABtAyUUeJs8Ewy6AEuhgTdeMnnXpg7yNZcC_0D0QdKezLoxQ30J3kYTQgipC5r7-Yevdou2BTSL2Szof3dMoo_Oz2maj_dt3AVoLGxajJqUvrvm6luWqYNe32YHqWPmTQMSSF3ChSbZm46kuJJISZ68AGMh4Hl0S9GB-hg5yNC0OpwfO0H-fip9WaCYCCYWVuip64iLcy-sqTsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت:
«ایران دیگه هیچ محموله نفتی‌ای در مسیر انتقال نداره. جریان نقدی‌شون منفی شده و ما راهشون رو بستیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/73114" target="_blank">📅 17:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73113">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aafe668bc.mp4?token=cnD9_sEfIp_6X3XDkf3QihHCvxqMt60hPwW6c3dNgv4yryc6XdEbczvKUvP9rJYn0qsFw6IlwkjcI1e9UTKuFCxsrXvxQZgB8HfK8-8aq07NQcD2s114mEOK_spqv_zBUby3yhOloec8cfV8PvMUbY-DfsSpcFCxFc_7Doz2OPoSyUknFEpLU7Dge6fOfOVoxyM5cTqheaDP1mBiE4cVBRjImbtba2ZZqqRTfsVr64LTnEkea7xqIA6ChQJHcFatuykGmsFcm57R2PtlaIBmH8V_aXkPC86DfmCBmAcurmDaf2xADDPHBfNx9mVyyjrm4O11VDvY-MxIc2AdARi-dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aafe668bc.mp4?token=cnD9_sEfIp_6X3XDkf3QihHCvxqMt60hPwW6c3dNgv4yryc6XdEbczvKUvP9rJYn0qsFw6IlwkjcI1e9UTKuFCxsrXvxQZgB8HfK8-8aq07NQcD2s114mEOK_spqv_zBUby3yhOloec8cfV8PvMUbY-DfsSpcFCxFc_7Doz2OPoSyUknFEpLU7Dge6fOfOVoxyM5cTqheaDP1mBiE4cVBRjImbtba2ZZqqRTfsVr64LTnEkea7xqIA6ChQJHcFatuykGmsFcm57R2PtlaIBmH8V_aXkPC86DfmCBmAcurmDaf2xADDPHBfNx9mVyyjrm4O11VDvY-MxIc2AdARi-dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛
اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
«همون‌طور که رئیس‌جمهور گفته، انتظار نداره درگیری نظامی تا قبل از انتخابات میان‌دوره‌ای اتفاق بیفته؛ دست‌کم نه تا بعد از اون.
نمی‌دونم معادل عبارت «تسلیم شدن و درخواست توقف» به فارسی چیه، اما ایرانی‌ها بالاخره به جایی می‌رسن که از آمریکا درخواست کنن دست از فشار برداره و تسلیم می‌شن.»
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/73113" target="_blank">📅 17:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73112">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1394e2d860.mp4?token=ml65Q98V-O3cxkhOaq0O3BpqsHf0DUhq_Q2fjhGcctBXixYbVOB9zzgPZgz-_1qZgkz4P7g-CLqjRnkQ-1a8pAak8-LhauGV105mKDJW7rHGC-nhfm3QmrFshHhswgDsLDzshJh8zHTdtEpOGJgk8sJK0u9fCuJb2xQ-Ak0cb6-NkB3ogfIU-Hw_wdg3Kii7wLvFEyflAfJe5IVMnd9m2hvHLPNvMm9NRBHObD33mdhV8qIw4hneR67YtiYGuWIc8E9pDcibnvqmsv3REZNg_x42zracDlYhiYG5NanSdvJe4KfFK2qVJnnZ_14wwBm9LZslnCKx_S6ZpRut11cMNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1394e2d860.mp4?token=ml65Q98V-O3cxkhOaq0O3BpqsHf0DUhq_Q2fjhGcctBXixYbVOB9zzgPZgz-_1qZgkz4P7g-CLqjRnkQ-1a8pAak8-LhauGV105mKDJW7rHGC-nhfm3QmrFshHhswgDsLDzshJh8zHTdtEpOGJgk8sJK0u9fCuJb2xQ-Ak0cb6-NkB3ogfIU-Hw_wdg3Kii7wLvFEyflAfJe5IVMnd9m2hvHLPNvMm9NRBHObD33mdhV8qIw4hneR67YtiYGuWIc8E9pDcibnvqmsv3REZNg_x42zracDlYhiYG5NanSdvJe4KfFK2qVJnnZ_14wwBm9LZslnCKx_S6ZpRut11cMNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی یک کشتی در مسیر جنوبی تنگهٔ هرمز بر اثر اصابت یک پرتابه:
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/73112" target="_blank">📅 16:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73111">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">صدای دو انفجار از طرف تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/73111" target="_blank">📅 16:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73110">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2a7fa633.mp4?token=tSSiCfVKYzufJpgdjJhT0KKNuBhD1rd7MWdPDarelOtuAauIYwwQME6R8k8Gwq2J2KXliZLpZGF8ZQok6YhCx8vn6jrca9LPG8vCUrBuCwjcvMu55NoHgqntSpy98I1MYD8denbcVRwztQaeWAxPetqy7Qtm1-wGGhyXIKEtnNuJ-c1uU5oXrQAoKTOssMRF_-K0xUzOlXwXC_WPD5ZjmjKoAzbkLCn93vC2kRDy55s5fGrInm6MRAoru2GVvUS_8mJZebstAoeYwgAdHCUBn9_Is67y_V4LYp46Gnqj3LSGKGlM2Aqtl4AczEMf0qpcbciTB-Jb2mtDSCRdM87QKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2a7fa633.mp4?token=tSSiCfVKYzufJpgdjJhT0KKNuBhD1rd7MWdPDarelOtuAauIYwwQME6R8k8Gwq2J2KXliZLpZGF8ZQok6YhCx8vn6jrca9LPG8vCUrBuCwjcvMu55NoHgqntSpy98I1MYD8denbcVRwztQaeWAxPetqy7Qtm1-wGGhyXIKEtnNuJ-c1uU5oXrQAoKTOssMRF_-K0xUzOlXwXC_WPD5ZjmjKoAzbkLCn93vC2kRDy55s5fGrInm6MRAoru2GVvUS_8mJZebstAoeYwgAdHCUBn9_Is67y_V4LYp46Gnqj3LSGKGlM2Aqtl4AczEMf0qpcbciTB-Jb2mtDSCRdM87QKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس سازمان مدیریت بحران کشور: احتمالاً در ۴ ماه پایانی سال کسری انرژی خواهیم داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/73110" target="_blank">📅 16:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73109">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4f3b1e9af.mp4?token=j0SqfO--YCWwApzwJxzgJv-RBFcPAH2rC-spRronLhQcFlIv0A1P7M8-osCml1vL_fVXx16bmK7WrH5hBvUxa8X7iRdD2hOFUR5OoAk9DCEL3ifaSSqPgFYxP6UdQQBbSbefvZuB0xlNYeg0_cQx2hlAP9T-axwZlFyGLxGqiA8qccL_WasNIRJ2dT9_YpmIWS8tRA9tz0qheHORLgDGhsH_tt1hCNYCreF_b3ecJ8pMxgvPU1hbSTTsnRnbPtKniSmWOHMj214ICssJ70uQRvoHvkb8Vce8qjnrOiKXuIGjpvPZDt_DArMx0fzQMeRqxXpYxPGieVHqzLT3UjWuCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4f3b1e9af.mp4?token=j0SqfO--YCWwApzwJxzgJv-RBFcPAH2rC-spRronLhQcFlIv0A1P7M8-osCml1vL_fVXx16bmK7WrH5hBvUxa8X7iRdD2hOFUR5OoAk9DCEL3ifaSSqPgFYxP6UdQQBbSbefvZuB0xlNYeg0_cQx2hlAP9T-axwZlFyGLxGqiA8qccL_WasNIRJ2dT9_YpmIWS8tRA9tz0qheHORLgDGhsH_tt1hCNYCreF_b3ecJ8pMxgvPU1hbSTTsnRnbPtKniSmWOHMj214ICssJ70uQRvoHvkb8Vce8qjnrOiKXuIGjpvPZDt_DArMx0fzQMeRqxXpYxPGieVHqzLT3UjWuCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا بچه مچه با خودتون نبرید طلافروشی، یا اگه میبرید با طناب ببندینش به خودتون که همچین منظره‌ای خلق نکنه :
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73109" target="_blank">📅 15:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73106">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18ce038cc.mp4?token=T3M6Z5DKg_FsjVPiDiiglL4BKWDS2sD_A9kpe94lgTbJWbOCDCFRK-_hzN7y-pRsOlEEsWphP_na_RNhR8CWXhR7wKYbDMox0ElHFPLMycuirmlnuiRqcW1mBELdUA5bWOS_Shvcvf1JgpfePkPVLi3Z_CIeqiCWOr9JspmAv7yXsAiN0fO1DsiIL8fpPumTp7_rkSa3TWeyq7gfr6JrdBFB1_CGRQDaJssJ0hM164xsGcKPMgFTPiJSpbVR_IOhdKoK70z971lnvY_LH-qd_ksT3j1uaZA1hf_brxBt_nHHa2-WJWNP2UiGvYNtplAyCbYKXGrk5J0k4OfAD5Ah-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18ce038cc.mp4?token=T3M6Z5DKg_FsjVPiDiiglL4BKWDS2sD_A9kpe94lgTbJWbOCDCFRK-_hzN7y-pRsOlEEsWphP_na_RNhR8CWXhR7wKYbDMox0ElHFPLMycuirmlnuiRqcW1mBELdUA5bWOS_Shvcvf1JgpfePkPVLi3Z_CIeqiCWOr9JspmAv7yXsAiN0fO1DsiIL8fpPumTp7_rkSa3TWeyq7gfr6JrdBFB1_CGRQDaJssJ0hM164xsGcKPMgFTPiJSpbVR_IOhdKoK70z971lnvY_LH-qd_ksT3j1uaZA1hf_brxBt_nHHa2-WJWNP2UiGvYNtplAyCbYKXGrk5J0k4OfAD5Ah-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت گرگان بعد از سیلاب ساعاتی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/73106" target="_blank">📅 15:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73105">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/35cfb05bea.mp4?token=Cp6580pxSoRcC33IZ87xJbUaMRAnR2h039Oh_q4VRNEkzRvpLAu4NQK1irjphrd68QBJGh59IJE6JBRS4ahUaWCUpXsxlgCZMvwLAgJTkvOuBYoGNjnvypV2LM-UbadGCbhK9rj4PDGOUV5gBBjGoXWHaX-fL6WqUkSur0x7gW-ZijFAwtkbE5M7eax5S77AQ3DR8Rlg29xkHKPtPWR492K5zWEdvQ1tJUk-2_O6xF-xcYyn57kH1pTBJkoPb3n3XTAvyIRJ9wpJeoBmI8OHVPmUWffGPDHSzcJc3Ih1pOYIXZMgRS5y4UminRr4lK1SBBbMYIE9ry6DGQ3_HL3mrA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/35cfb05bea.mp4?token=Cp6580pxSoRcC33IZ87xJbUaMRAnR2h039Oh_q4VRNEkzRvpLAu4NQK1irjphrd68QBJGh59IJE6JBRS4ahUaWCUpXsxlgCZMvwLAgJTkvOuBYoGNjnvypV2LM-UbadGCbhK9rj4PDGOUV5gBBjGoXWHaX-fL6WqUkSur0x7gW-ZijFAwtkbE5M7eax5S77AQ3DR8Rlg29xkHKPtPWR492K5zWEdvQ1tJUk-2_O6xF-xcYyn57kH1pTBJkoPb3n3XTAvyIRJ9wpJeoBmI8OHVPmUWffGPDHSzcJc3Ih1pOYIXZMgRS5y4UminRr4lK1SBBbMYIE9ry6DGQ3_HL3mrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف:
من به مسئولین گفتم، با برجامی که کونتون رو پاک میکنین، فردا باید دماغ‌تون پاک کنین!
ما کشورهای منطقه رو تهدید می‌بینیم، برای همین سفرای ما در منطقه جا بازرگان و دیپلمات، نماینده سپاه قدس هستن.
ما همه چیزو تهدید می بینیم، زن رو تهدید دیدیم، اینترنت رو تهدید دیدیم، کشورای منطقه رو تهدید دیدیم، ما حتی حجاب هم خاکریز می‌بینیم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/73105" target="_blank">📅 14:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73104">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ac45cb0ca.mp4?token=a4Gk-PappG6e6jcv-oSebwLUCnrJXHfHGcVuUjvYxZykCUOGZOhRQqNklsRggZwoy2QUwEjH_YcwdyvRq6cP9yn2usaohOyTL3E-kVeDwEx9xbyuVx56-UdwARElQUI2DyDGrtfsa1FYuZstf_10GgdpWhG7BV70gB_aws1t1VTIGWRffVrNpSH4yTmtiFNRzAG6rdhMRB70IpNhhYyVALYE-wlPGWtfk3Kkbe3D20Up_UAlluu6xM8jvSTb1jCf1LgMChUfGEc_m19DBv-2R-7Qxil6qUOePjlXFyAcjDc7ZWfYnyvwzdBpIAwe4hpX2sQMflmdfi9wru00YBmmeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ac45cb0ca.mp4?token=a4Gk-PappG6e6jcv-oSebwLUCnrJXHfHGcVuUjvYxZykCUOGZOhRQqNklsRggZwoy2QUwEjH_YcwdyvRq6cP9yn2usaohOyTL3E-kVeDwEx9xbyuVx56-UdwARElQUI2DyDGrtfsa1FYuZstf_10GgdpWhG7BV70gB_aws1t1VTIGWRffVrNpSH4yTmtiFNRzAG6rdhMRB70IpNhhYyVALYE-wlPGWtfk3Kkbe3D20Up_UAlluu6xM8jvSTb1jCf1LgMChUfGEc_m19DBv-2R-7Qxil6qUOePjlXFyAcjDc7ZWfYnyvwzdBpIAwe4hpX2sQMflmdfi9wru00YBmmeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری منتشر شده است که لحظه حمله حوثی‌ها به فرودگاه بین‌المللی ملک خالد در ریاض را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/73104" target="_blank">📅 13:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73103">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVicJEEOBfpYRLG1iERfjfQZJ9ZYvMcqEfeAB62aGR7oo0PQYtuf24HzHPuPjPHvtz7AhSo43jHsgHwxKSyEfz85qAbMxPGc8Zk7kzBAIkj7li4n6JucSXEUZhIVlLbBdXvMY_lIoB3mHNboB-3C10wHif0-YErBzFEpQEbYEExtizeIYVCSbz59335v_BTfqyBtLGM9_9cp4uChVB9uoSJmvZKrkHLrdHTv0eAmlym4fz-qiPrfijVicIraKBmONyLRXpu183l1EMWlHVBtzjPRaTLx4oRrpgdBRFYQuN2CMZUWw6tABXjuwdZqhcV3tvxu6U3U5iALXtAgMYyebQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز جهانی دختر، بر دختران سربلند و آزاده‌ی ایران‌زمین فرخنده باد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73103" target="_blank">📅 12:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73102">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VoxDQHjAlRlkEJDQRj90TWmDmSALjQHaXYx-KNBq-XqhK-VLLrWpUdRoAySu4EHNzcBQhXFxFBl5CLcW1C01T01kj8273yeYSuv5egb7pbSASVmEsfkSThrKMB0-HJj1nPJ92yphEfXrNO6W3J-V3LEK-1duZPIoCOp28CNsVuxN9m4B-FktqkuRXGaYOn-fFfhNyPwvi8pRXSLVp20gu9jfqeSB98v21TRxsIq6cwLEAfxy7Ih_AJTPjF9hDtup28J0gGyLSGcpCo4ik6deJNK33vSi1aajApQG3yk72pL1F2Q5W-qQR4KAPoH-AuGFNe1wdioNH87ySYnXtI0A0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست موشکی از جنوب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73102" target="_blank">📅 12:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73101">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47fbc83428.mp4?token=N2O2RONv_9ZhUSxUmTZOp4X8QVmQ2Qailo-8xYFQwcpXN0utaD9WBuakG3lx-e5nN-KU0isMiwnfiGLtB6C2HtsVqN74hD0YuHuLY_0OzL-uopiJ5iEUNuHzedKCpCtTETeLPcGTGsVLKTeA1BPoc3Vrj_CAusD61sgnHwhufXvLYXWnxds5Hfmi7mFkkDLVM0ffOfi9smVDlrVS3my_NIGqxK82M2GFyXNmnytBFrjZ2m8PPWsHJmmCe6A2n8tzVitd3tXQOMPG1TaWGHlPA7xypI_hjEMj1Irj4TbcJAyfj5UwWbsQaDc4lDI8GKoMpXawERD35JrL4hGQLtLjrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47fbc83428.mp4?token=N2O2RONv_9ZhUSxUmTZOp4X8QVmQ2Qailo-8xYFQwcpXN0utaD9WBuakG3lx-e5nN-KU0isMiwnfiGLtB6C2HtsVqN74hD0YuHuLY_0OzL-uopiJ5iEUNuHzedKCpCtTETeLPcGTGsVLKTeA1BPoc3Vrj_CAusD61sgnHwhufXvLYXWnxds5Hfmi7mFkkDLVM0ffOfi9smVDlrVS3my_NIGqxK82M2GFyXNmnytBFrjZ2m8PPWsHJmmCe6A2n8tzVitd3tXQOMPG1TaWGHlPA7xypI_hjEMj1Irj4TbcJAyfj5UwWbsQaDc4lDI8GKoMpXawERD35JrL4hGQLtLjrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: یک کشتی باری در دریای عمان هدف حمله آمریکا قرار گرفت
فرماندهی مرکزی آمریکا (سنتکام) اعلام کرد در ۱۰ اکتبر، یک کشتی باری با پرچم پاناما به نام Ocean Molica که پیش‌تر از یکی از بنادر ایران حرکت کرده بود، پس از بی‌توجهی به هشدارهای مکرر و تلاش برای عبور از محاصره دریایی، هدف مهمات دقیق یک جنگنده آمریکایی قرار گرفت.
به گفته سنتکام، این حمله پیشرانه کشتی را از کار انداخت و خدمه آسیبی ندیدند. همچنین، طی سه ماه اجرای محاصره دریایی، ۴ کشتی از کار انداخته و ۱۳۵ کشتی دیگر وادار به تغییر مسیر شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/73101" target="_blank">📅 12:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73099">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6da19cc3d2.mp4?token=YzOfkfzneTDCH9Wnk0xn7fYKCp5BL2aDbdmAVeHZ7K6PmPTbkTINVaJwDUNIPv0-4c90A6ehLIxvgIL-vHQNajmHo2kssNvs2H-nmiIyg3arPrad8Dof1O3AoGd2pStyL3z3oNpDLaFDD8DmnCnn1op5ZTDi6694JdAnIG36Zcl_KvPgTioTeMA6J-GpnooNY2axHPpaluq8wRJNSmtCNURLGFzOjr6TIe-LPrDdXHqlA_xgv5F5hVR2S-9FD2vkBhdgePF6LQPhJHE9akZXEyG256wnsQsw5XimdmsCaXveBmfxdLza_zbwOdwdWIc6HdAUvELeeo035KKCsi6zfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6da19cc3d2.mp4?token=YzOfkfzneTDCH9Wnk0xn7fYKCp5BL2aDbdmAVeHZ7K6PmPTbkTINVaJwDUNIPv0-4c90A6ehLIxvgIL-vHQNajmHo2kssNvs2H-nmiIyg3arPrad8Dof1O3AoGd2pStyL3z3oNpDLaFDD8DmnCnn1op5ZTDi6694JdAnIG36Zcl_KvPgTioTeMA6J-GpnooNY2axHPpaluq8wRJNSmtCNURLGFzOjr6TIe-LPrDdXHqlA_xgv5F5hVR2S-9FD2vkBhdgePF6LQPhJHE9akZXEyG256wnsQsw5XimdmsCaXveBmfxdLza_zbwOdwdWIc6HdAUvELeeo035KKCsi6zfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدی رفتن ویدیوی رپ هوش‌مصنوعیِ بی‌بی رو نشون خودش دادن، اونم به شوخی میگه از کجا میدونید شاید واقعی باشه:)
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/73099" target="_blank">📅 11:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73098">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مقام‌های سعودی اعلام کردند در حمله روز شنبه به فرودگاه ملک خالد ریاض، ۱۲ نفر کشته و ۳۰۹ نفر زخمی شدند.
ملیت کشته‌شدگان:
عربستان سعودی: ۴ نفر
بنگلادش: ۲ نفر
آمریکا: ۱ نفر
مصر: ۱ نفر
اردن: ۱ نفر
سوریه: ۱ نفر
فلسطین: ۱ نفر
سودان: ۱ نفر
برخی مجروحان در وضعیت وخیم قرار دارند و حمله خساراتی به تأسیسات فرودگاه وارد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/73098" target="_blank">📅 11:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73097">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f2ae9fdb8.mp4?token=HRdArVFFb-41DFo9hDwQNuC9LwqQ6v498jGxOF0tdPMOj1GudXpofjGUHQIr3R4fOikMbJp8zOJyvHG5rn4BmA2wFbyWDg1c_XAv9vLmGqS5Gxx11Fllpqw_VrfY_vDMTm-LSiV5tBCouPbG3y7PmyTt8Hn77xcA4SbYp870K0A0J2x3MOVC5eYtGk_0RAdB758B0p0A0lN8ap9OrHyD6TWirTlYiL1P4P3o-CSyaHbtriUxVVDIQFbmP7sXociUxImux3QcxE-72fChiwas_vg7LUWta8t2rB1kbeysoZ-Izk4N13lduB_dlxfap847VBzTyVZuFelRT9lwTqCwMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f2ae9fdb8.mp4?token=HRdArVFFb-41DFo9hDwQNuC9LwqQ6v498jGxOF0tdPMOj1GudXpofjGUHQIr3R4fOikMbJp8zOJyvHG5rn4BmA2wFbyWDg1c_XAv9vLmGqS5Gxx11Fllpqw_VrfY_vDMTm-LSiV5tBCouPbG3y7PmyTt8Hn77xcA4SbYp870K0A0J2x3MOVC5eYtGk_0RAdB758B0p0A0lN8ap9OrHyD6TWirTlYiL1P4P3o-CSyaHbtriUxVVDIQFbmP7sXociUxImux3QcxE-72fChiwas_vg7LUWta8t2rB1kbeysoZ-Izk4N13lduB_dlxfap847VBzTyVZuFelRT9lwTqCwMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: نظرتون درباره حمله حوثی‌ها به فرودگاه ریاض چیه؟
ترامپ: «به نظرم اتفاق وحشتناکیه.»
خبرنگار: آیا آمریکا هم وارد ماجرا می‌شه؟
ترامپ: «خب، خودتون متوجه خواهید شد. اما به نظرم اتفاق وحشتناکیه.»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/73097" target="_blank">📅 10:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73096">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ درباره یمن:
«ما با حوثی‌ها در ارتباط هستیم و باید ببینیم چه اتفاقی می‌افته.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/73096" target="_blank">📅 10:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73095">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/174ee9d3ac.mp4?token=G3FMyMQybt-DFwkzdE3hVs9hxvMHEryETIqNujex_C1Vq5VyM0-GqBIsv3bZEzOgLCuU1hL88c29XcGhenXZpF7nPCJaiB5sNngYLezo6pPXsjRuKZlC2H4VstkbdJfgUsszDGj5sV8B1JRPdKT7FfEFT8U9OgJ5MeWd5Mbvu22ulunbRLC5-82oCt04ZTUHvnshc5dsLE3B-fNSdXOsLWxn-BMK4bz4-fFvgCuTwv8Pr-YG-TOgrCrknDu-LDYZRsVMfPJKM5lJnRINafW5d_tF4BKalK0OFL4zNovxfG1gioPtRLe_zzoR_ANGioF7vqxjOr1hPnRyz71Rj47dBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/174ee9d3ac.mp4?token=G3FMyMQybt-DFwkzdE3hVs9hxvMHEryETIqNujex_C1Vq5VyM0-GqBIsv3bZEzOgLCuU1hL88c29XcGhenXZpF7nPCJaiB5sNngYLezo6pPXsjRuKZlC2H4VstkbdJfgUsszDGj5sV8B1JRPdKT7FfEFT8U9OgJ5MeWd5Mbvu22ulunbRLC5-82oCt04ZTUHvnshc5dsLE3B-fNSdXOsLWxn-BMK4bz4-fFvgCuTwv8Pr-YG-TOgrCrknDu-LDYZRsVMfPJKM5lJnRINafW5d_tF4BKalK0OFL4zNovxfG1gioPtRLe_zzoR_ANGioF7vqxjOr1hPnRyz71Rj47dBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا سعودی‌ها بدون حضور نیروهای آمریکایی هم می‌تونن از خودشون دفاع کنن؟
ترامپ: «بله، توانایی دفاع از خودشون رو دارن. سعودی‌ها جنگجوهای خوبی هستن، اما به نظرم اون حمله اتفاق وحشتناکی بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/73095" target="_blank">📅 10:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73094">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73094" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/73094" target="_blank">📅 10:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73093">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIFln2MlJnvDx5uo0AJTczVLRTqdHeAoezc1_GHrxxz-wh0AOVBDGO1-PK7OU2IerAUuJWwHQp_zBc6lIs61qyyVh8o12S7r-eQ5vHp7DQzgPUlsT1CfpbjfXPI1hmJtiiBg7bkELMHbkm_f6wZNW5akAif4Bg_JONBAYoMhLVUQS8fdQb3w5tUVkriwgHf4-OwIgLahicMLzTgcau2zpkD0PrNJZyHwvuJeGl69SYUflilxBX9Yv3ZSfFg-6G0LXHIqX3y4huoWYjYAZ_RMwXy6KNBRNT_xDia2ZZiQssIMSMbgDfaxUj4YtWMUWoqnIlbjxGIu9F1JjybrDMZHew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
ناتینگهام‌فارست
🆚
کریستال‌پالاس
اورتون
🆚
هال
منچسترسیتی
🆚
لیورپول
اوساسونا
🆚
راسینگ سانتاندر
رم
🆚
کومو
مونزا
🆚
لاتزیو
میلان
🆚
ساسولو
فروزینونه
🆚
ناپولی
یوونتوس
🆚
کالیاری
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
https://TrexBet.com</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/73093" target="_blank">📅 10:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73092">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e6800693.mp4?token=T-GQv5Mm0nssDudJFydZ-ceSwmbPsFZkHd0BIb_Xx603d_Otrb8LVMIZjwHms2tgsu0b8kE4NzTagwFOyaPXcd51nnJyT2ha65OcO9SId1G7xB1mfgixZbg2Tn7FKUPO52C-_ojqu_BSHyYZTVJJHa1KbBhEb2O-9PLGJnrKi-yiCQoZ_LSi6JRFnm_QN_3LjParTcj0imRn4CuBUnEhvS1HoW2QkwkvOx8a9l0lF5eNhXLStQK_atgYSu2qbjag5QM6pm-6-Gs3PuINPQTnjztNhXM2cnrv3FtQfWngXfFGk4CCOtsXPZyHuMQgHleF9u8eGGo80MpvjDfCHRtV2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e6800693.mp4?token=T-GQv5Mm0nssDudJFydZ-ceSwmbPsFZkHd0BIb_Xx603d_Otrb8LVMIZjwHms2tgsu0b8kE4NzTagwFOyaPXcd51nnJyT2ha65OcO9SId1G7xB1mfgixZbg2Tn7FKUPO52C-_ojqu_BSHyYZTVJJHa1KbBhEb2O-9PLGJnrKi-yiCQoZ_LSi6JRFnm_QN_3LjParTcj0imRn4CuBUnEhvS1HoW2QkwkvOx8a9l0lF5eNhXLStQK_atgYSu2qbjag5QM6pm-6-Gs3PuINPQTnjztNhXM2cnrv3FtQfWngXfFGk4CCOtsXPZyHuMQgHleF9u8eGGo80MpvjDfCHRtV2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امام جمعه تهران:
توقع مردم، تجدید نظر در دکترین هسته‌ای ایران است
از ان پی تی خارج شویم به غرب می‌گویم هسته‌ای ما به شما ربطی ندارد؛
غلط کردین؛ برید گم شید!
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/73092" target="_blank">📅 10:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73091">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce6a5528a8.mp4?token=jpOtj1gk-uiNuIyKiVJAsg0M6eF2iYjjr18GkJvvOmkIWnbplf_GabeKKTjWlDBL_huAqkpnxyb9dYeubDxni160Isrl7lzbCDys5jE-CFkmCavHFYl2JsSeGBLoawB6ODEW-3P8lZgOTkShPgWtVARiNYdSfAmhQ-ipMN8a_vN_CflHJHcMujIIlzxrkiaLh94CABYzCBQgByIcGE0XoZI7c6LdnA_bgDm6E-RMihj1yN5StKPkDZ2AkpSgFBWbwCgEmYuInHjX5OUw-TTbmDKkeYqlx7rNAtXEus_e9fwdro3CyT6vmKvOjIxMbajCIQmYpkYGZcldTcnWlzS3P0iFFVYNTFe_r7kJ4n3RnE450y7zKZajRZOkRoPHs1wm0DCIzY4xcrAI_B1n9nY_b7rafY0lZBjyQA0FiR3XeS78ViZzo6Dp0s1kGJD7PrzY_qPqV05uzJymqyeRwQGixrNTRFapQtcCrTNeQ2hCNT3_Yvp4bidmBBLjLN3P6jFjIsPvyyarFllQpWXula9LzDpSTpCPXBrpsp3xTIlRZbCmRxY3evGvA7Y-r9q1M4g0Mq7dcBQye3it-AhZSZRPrW_NDrwRT0EazkinhWSoQBM-28WaZ3b5_MNGbI7kHyMJlZAGM2RC-tlj7nx3Y-m5tSA4neoCcO0wqJBdOsIMUVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce6a5528a8.mp4?token=jpOtj1gk-uiNuIyKiVJAsg0M6eF2iYjjr18GkJvvOmkIWnbplf_GabeKKTjWlDBL_huAqkpnxyb9dYeubDxni160Isrl7lzbCDys5jE-CFkmCavHFYl2JsSeGBLoawB6ODEW-3P8lZgOTkShPgWtVARiNYdSfAmhQ-ipMN8a_vN_CflHJHcMujIIlzxrkiaLh94CABYzCBQgByIcGE0XoZI7c6LdnA_bgDm6E-RMihj1yN5StKPkDZ2AkpSgFBWbwCgEmYuInHjX5OUw-TTbmDKkeYqlx7rNAtXEus_e9fwdro3CyT6vmKvOjIxMbajCIQmYpkYGZcldTcnWlzS3P0iFFVYNTFe_r7kJ4n3RnE450y7zKZajRZOkRoPHs1wm0DCIzY4xcrAI_B1n9nY_b7rafY0lZBjyQA0FiR3XeS78ViZzo6Dp0s1kGJD7PrzY_qPqV05uzJymqyeRwQGixrNTRFapQtcCrTNeQ2hCNT3_Yvp4bidmBBLjLN3P6jFjIsPvyyarFllQpWXula9LzDpSTpCPXBrpsp3xTIlRZbCmRxY3evGvA7Y-r9q1M4g0Mq7dcBQye3it-AhZSZRPrW_NDrwRT0EazkinhWSoQBM-28WaZ3b5_MNGbI7kHyMJlZAGM2RC-tlj7nx3Y-m5tSA4neoCcO0wqJBdOsIMUVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه بریتانیایی ITN حدود ۴ ساعت از تصاویر وقایع سال ۱۹۸۹ میدان تیان‌آن‌من را منتشر کرده است؛ تصاویری که پیش‌تر محرمانه نگه داشته شده بودند و توسط تیمی ضبط شدند که موفق شد این نوارها را مخفیانه از چین خارج کند.
این مجموعه که حدود ۳۵ سال در آرشیو نگهداری می‌شد، شامل یک ویدئوی تدوین‌شده‌ی ۲ ساعته از سرکوب‌ها و همچنین ۹۰ دقیقه تصاویر خام و مخفیانه‌ای است که در روزهای پس از آن واقعه ضبط شده‌اند؛
تصاویری که کامیون‌های نظامی در خیابان‌های پکن، جمعیت مردم و پیامدهای آن رویداد را به نمایش می‌گذارند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/73091" target="_blank">📅 09:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73090">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e31f09431.mp4?token=oWsITZYl1ExrA-cUok6Fc1ewlHpqpf1nTOH-wGoNqjsmPyp3Cc9ZEvUr2iA2LMKkDxLbnaJkYlYY1pDGP-iuJvCv_2CIfx2tkHVqihksNhFxNpyrlbTXHZuHQw_rxsdI0yc5GGxGhhnbFaqn3PbmKNBMCgO7f_kPLc_PNH6INV5oKGyuKaYnfj5oCa_dmBuPWKr-jt3t51dbMXqesKdzfNqLhzcP6O83aT8iYa0itImnmGvP3CbHIl3mAj65DBsqXI95jJ4luj2A5n5ggmQwEz5c4ewSUPZwGyWtuoq6ORhh2m8m4ew5axxIiR11qByG8oIsKSmbibZvJjc41shRJjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e31f09431.mp4?token=oWsITZYl1ExrA-cUok6Fc1ewlHpqpf1nTOH-wGoNqjsmPyp3Cc9ZEvUr2iA2LMKkDxLbnaJkYlYY1pDGP-iuJvCv_2CIfx2tkHVqihksNhFxNpyrlbTXHZuHQw_rxsdI0yc5GGxGhhnbFaqn3PbmKNBMCgO7f_kPLc_PNH6INV5oKGyuKaYnfj5oCa_dmBuPWKr-jt3t51dbMXqesKdzfNqLhzcP6O83aT8iYa0itImnmGvP3CbHIl3mAj65DBsqXI95jJ4luj2A5n5ggmQwEz5c4ewSUPZwGyWtuoq6ORhh2m8m4ew5axxIiR11qByG8oIsKSmbibZvJjc41shRJjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میرسلیم:
فلسفه بازنشستگی در یک کشور اسلامی هیچ مفهومی ندارد و مسلمان واقعی باید تا آنجا که می‌تواند خدمت کند
حیف است که افراد ۸۰ و ۹۰ ساله را از خدمت کنار بگذاریم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/73090" target="_blank">📅 09:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73089">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73089" target="_blank">📅 01:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73088">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/73088" target="_blank">📅 01:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73087">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1848b3d2ec.mp4?token=BJ9ZM1_v0oOjzEwQzw9aIWGGTx-wI-ohqRhi59x5tOKmz-qlMxmaekKWAWcIe5DwPmQHaUruyo9Tm2QgUxMxQsYwiXKAbI09hADFBlckhffCzBea1NhD1mi1q3hqzLzAHwJe3g1ZNeGgECrpEOZlxRtP43fN0MjNXPk-PmKLOYjwKxllR6M8drijGJ9JBQrlDJEE0aNfwYHH8l2ZscxAAcy2mWs-3ZPwwloHj_l05hTNmkTSvHcLgPSUGOCIMWnENDDcKwiyYYd5FpdGj003gwi-DEWxDC17vwLeuC11PB_wGmbGcUOMHADve-Fk_1XaP9C5UfbEuYDR9t4V3I866w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1848b3d2ec.mp4?token=BJ9ZM1_v0oOjzEwQzw9aIWGGTx-wI-ohqRhi59x5tOKmz-qlMxmaekKWAWcIe5DwPmQHaUruyo9Tm2QgUxMxQsYwiXKAbI09hADFBlckhffCzBea1NhD1mi1q3hqzLzAHwJe3g1ZNeGgECrpEOZlxRtP43fN0MjNXPk-PmKLOYjwKxllR6M8drijGJ9JBQrlDJEE0aNfwYHH8l2ZscxAAcy2mWs-3ZPwwloHj_l05hTNmkTSvHcLgPSUGOCIMWnENDDcKwiyYYd5FpdGj003gwi-DEWxDC17vwLeuC11PB_wGmbGcUOMHADve-Fk_1XaP9C5UfbEuYDR9t4V3I866w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«ایران کشور بسیار شروریه؛ بزرگ‌ترین حامی تروریسم در جهانه.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/73087" target="_blank">📅 01:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73086">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6a4893ab6.mp4?token=K60wC-fQERwZ6Ihq_x4SlumtgUc53x7EHL5VucplQ3cN6EcVk41gCnRE7QANkUTbi7ZsNsO5TYte09CCdOvTvnoPOAbWZNl7n4jQaiysfZf7A1dkfNjNQUzH2GAH6HL10Bog_YkIrrLc4CCboWCKzmVq8LxlWiDFWEoW6inBKtFsHjjTzYhi4V0oTpF9O87deX5tMvolUINqZKIOiRcKgMYVzReJSXAQzvb39oJ1R7npvfDI_zn2HC-lNMd81bf9Kq3lDL0YjmP4DHcNqijsteuRYkKfdyFiR56_5AKcC1XEmMAczdiOY1dsOERGyP2FHOayLAVjYyQD2oLT8eWPb4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6a4893ab6.mp4?token=K60wC-fQERwZ6Ihq_x4SlumtgUc53x7EHL5VucplQ3cN6EcVk41gCnRE7QANkUTbi7ZsNsO5TYte09CCdOvTvnoPOAbWZNl7n4jQaiysfZf7A1dkfNjNQUzH2GAH6HL10Bog_YkIrrLc4CCboWCKzmVq8LxlWiDFWEoW6inBKtFsHjjTzYhi4V0oTpF9O87deX5tMvolUINqZKIOiRcKgMYVzReJSXAQzvb39oJ1R7npvfDI_zn2HC-lNMd81bf9Kq3lDL0YjmP4DHcNqijsteuRYkKfdyFiR56_5AKcC1XEmMAczdiOY1dsOERGyP2FHOayLAVjYyQD2oLT8eWPb4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«اون جوان‌هایی که در جنگ علیه ایران از دست دادیم، بیهوده جونشون رو از دست ندادن.
نمی‌شه اجازه داد یه آدم کاملاً دیوونه به سلاح هسته‌ای دست پیدا کنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/73086" target="_blank">📅 01:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73084">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/595730e6c3.mp4?token=V9kzkPaPNxTaaefZZhOA9nDXDdFM3PtPaOAg5ovl7BdHewXUbeEtIyjtHQqRiPSgk05vCZYz61EF8OSTEqOxaJrpKTxozCe1mPtnf3Js7t8YSsbyVY7ZOkQNtkB9OarXkJbyJLAJtbp0DZrztxpZiYyvFY1GbLYeztMUBHV11IN9vjPYeDYBqB4spk73W_nZ-m412yeutS6vv8_TXnlb1DHGmneyHQSFnNyrFnKpFm3YBQa8a8pUVlAL7uWr7CkfNMDAYm6bipyKy9V0y7TU6e64nZn0yytR-EIaGF-l9VfJ80Cg8nzFAZ9UKE8Zj96aA5PWI3fIzE7eO5gttd3IBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/595730e6c3.mp4?token=V9kzkPaPNxTaaefZZhOA9nDXDdFM3PtPaOAg5ovl7BdHewXUbeEtIyjtHQqRiPSgk05vCZYz61EF8OSTEqOxaJrpKTxozCe1mPtnf3Js7t8YSsbyVY7ZOkQNtkB9OarXkJbyJLAJtbp0DZrztxpZiYyvFY1GbLYeztMUBHV11IN9vjPYeDYBqB4spk73W_nZ-m412yeutS6vv8_TXnlb1DHGmneyHQSFnNyrFnKpFm3YBQa8a8pUVlAL7uWr7CkfNMDAYm6bipyKy9V0y7TU6e64nZn0yytR-EIaGF-l9VfJ80Cg8nzFAZ9UKE8Zj96aA5PWI3fIzE7eO5gttd3IBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلقک بازی املاکی
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/73084" target="_blank">📅 00:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73083">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b6424edb4.mp4?token=pIcar2hPDKjHCCDLNRFhUfRrcnWG3IY7GIkmI6dN1aPJunN-z2y-ajwdr0XrBG3GcnxoThMZfLLrveWLJG4f6VDF-CRc1dA0JlSCA-VMktvq-lWrO1UAwqXlinDcqFw4sceJOBM-Ftfb17qDSIgYvtfK_wdZ1LcvUKic9SKLzK8R4ykUuJRakc7fBlx2bnJmDqwLh75Sx8zPry3-yCWqnOf0ckfU48-7muppIAQPzYfCAHcmgque9tS8T5DDehrDxclqF2ej-PEMWv2lbWA0f_PJta7zHXaSJI78eRU_yuwUJMWqB-egS40OOztZCxfAHSkjloIqLtDPN2SgpZsc2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b6424edb4.mp4?token=pIcar2hPDKjHCCDLNRFhUfRrcnWG3IY7GIkmI6dN1aPJunN-z2y-ajwdr0XrBG3GcnxoThMZfLLrveWLJG4f6VDF-CRc1dA0JlSCA-VMktvq-lWrO1UAwqXlinDcqFw4sceJOBM-Ftfb17qDSIgYvtfK_wdZ1LcvUKic9SKLzK8R4ykUuJRakc7fBlx2bnJmDqwLh75Sx8zPry3-yCWqnOf0ckfU48-7muppIAQPzYfCAHcmgque9tS8T5DDehrDxclqF2ej-PEMWv2lbWA0f_PJta7zHXaSJI78eRU_yuwUJMWqB-egS40OOztZCxfAHSkjloIqLtDPN2SgpZsc2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارسالی یکی از اعضا از گرگان:
بارندگی شدید امشب در گرگان باعث وقوع سیل و وارد شدن خسارت به اموال مردم شده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/73083" target="_blank">📅 00:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73082">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c88cca8dd.mp4?token=r3D2cmgEJ4eiQls85kn9Zx9bt3kEAkN2562c26Q0SukH65aYieY5SWI8C9oMZlhszEadDIC9oHahMMTCPPBAYF2hSM9_jQz0eLgbmZAlvORNI_J8aWk9Of0ZKrAEsEg93w5VE_atbk4cy9dg6Cvivj8FBwtk55CfrxaIpcd2ZQ9KKy_xnOA2dD93bMkmpgA72KA7kWRKhwzTrJpTxfiuSoZYSQBI0k5XYaCwaqjDvF-pu9HdLgT0XX7fIlHb-NsdlULjvJ-XHI0tcREdRyfEh3adkXVFKg5tTewTmmJk9AQEIZdPAE-jyt-P_AVrl-1zfuoJQSywqco_tVEDYJbthg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c88cca8dd.mp4?token=r3D2cmgEJ4eiQls85kn9Zx9bt3kEAkN2562c26Q0SukH65aYieY5SWI8C9oMZlhszEadDIC9oHahMMTCPPBAYF2hSM9_jQz0eLgbmZAlvORNI_J8aWk9Of0ZKrAEsEg93w5VE_atbk4cy9dg6Cvivj8FBwtk55CfrxaIpcd2ZQ9KKy_xnOA2dD93bMkmpgA72KA7kWRKhwzTrJpTxfiuSoZYSQBI0k5XYaCwaqjDvF-pu9HdLgT0XX7fIlHb-NsdlULjvJ-XHI0tcREdRyfEh3adkXVFKg5tTewTmmJk9AQEIZdPAE-jyt-P_AVrl-1zfuoJQSywqco_tVEDYJbthg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">املاکی درباره تنگه هرمز:
«داریم به این فکر می‌کنیم که اسم تنگه هرمز رو به تنگه ترامپ تغییر بدیم!»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/73082" target="_blank">📅 00:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73081">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e93cc318ec.mp4?token=jaCYa2s1tZ0pNbqr5lBDcQ5LzOJFkgExOT98Zzz9UYz9dZrLZbmvpovofjKKTstsaP7M78HOzMKySQaOyLYUvZYWXkB0ipWIIrUcZaANXNKL3ZkEpaPHfXNBk-00gwL5I1bIYRbukV4kclHve1zWPcn5r4o3tTKZjK6yV1oEzs2O_7VCP3kfGex023YfuQC_j0UcOirw0SiGsMCMlqfS-hwpVcIeCoh9AnvIRqMu4vW3tkrTgxRURS8qQgd9df089zJrP8-pl4ViCdDrv4hX8e9FXWjTfuk9-dv3pVqXkx2HWXGX0ft0zpbfLu_LJcMTLgvfiuRYOhNFy_DSzI_pBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e93cc318ec.mp4?token=jaCYa2s1tZ0pNbqr5lBDcQ5LzOJFkgExOT98Zzz9UYz9dZrLZbmvpovofjKKTstsaP7M78HOzMKySQaOyLYUvZYWXkB0ipWIIrUcZaANXNKL3ZkEpaPHfXNBk-00gwL5I1bIYRbukV4kclHve1zWPcn5r4o3tTKZjK6yV1oEzs2O_7VCP3kfGex023YfuQC_j0UcOirw0SiGsMCMlqfS-hwpVcIeCoh9AnvIRqMu4vW3tkrTgxRURS8qQgd9df089zJrP8-pl4ViCdDrv4hX8e9FXWjTfuk9-dv3pVqXkx2HWXGX0ft0zpbfLu_LJcMTLgvfiuRYOhNFy_DSzI_pBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«می‌تونیم خیلی سریع به این ماجرا پایان بدیم. ایرانی‌ها نمی‌دونن که من تا حالا چقدر باهاشون مدارا کردم و چقدر باهاشون راه اومدم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/73081" target="_blank">📅 00:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73080">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/988c9468b6.mp4?token=ZmXCEjBHNzzV22fHM1VTzIG-uBWOFbibD1jSipIzB3v2C51Uo1SshqlJun8ECyi9WvvDOJtsk5kKm36ObUuudCWPaFjYAlnyLvZhkz9sLXB_9ebijTo1HXMOkrvSNvDLBHg3X8dBe8PdLdC6rJBH-sn7PkHTmV93_HjgtesaOik13H-7xJWQa_eiCbddCP4o2MaJfAhGhtK73PjJtfnxztTOIFD3CmeG4pqGTn3QtL-scwQyc50EMWB2whbNq0-bnqpf1vJhX012HUnCyl35wtRaZScU_kAiLONS-PpKwfZqCM7NmUz8nhFt1BHJX28Qe6mVCvz9xur9B768m6mu_6rsKUAUab2PUgPHXmGycQZxTEBfOI_FOJaMwCHnrU6ExkbNCN_Hl4guhNFvXid4K9rNveZs3FX6xqswvzXp3GZ0NZcQd0lnQDW7I1niqByKpKGsum7rCxKADrQe4v_cJTZbLdQPFJHaodJLjKwE_Z5hNnRmuXPyIMJSlDDKGoEo1N2pc4YRoz2ornkkOmfXjhTjkw3YFlczXUTNEa3A8WYxj7VPHoMC3aakk56SS9YXShbLgJXztQhI9ZCysdoQ-Z-rGgEkiRKC3mLoKbQI-xAJla1WJ6FCgUbKWueVwN_GFbhklc7IEj-Yi7M34ydLy3JG3QgPEGvmsx48lp6A3D4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/988c9468b6.mp4?token=ZmXCEjBHNzzV22fHM1VTzIG-uBWOFbibD1jSipIzB3v2C51Uo1SshqlJun8ECyi9WvvDOJtsk5kKm36ObUuudCWPaFjYAlnyLvZhkz9sLXB_9ebijTo1HXMOkrvSNvDLBHg3X8dBe8PdLdC6rJBH-sn7PkHTmV93_HjgtesaOik13H-7xJWQa_eiCbddCP4o2MaJfAhGhtK73PjJtfnxztTOIFD3CmeG4pqGTn3QtL-scwQyc50EMWB2whbNq0-bnqpf1vJhX012HUnCyl35wtRaZScU_kAiLONS-PpKwfZqCM7NmUz8nhFt1BHJX28Qe6mVCvz9xur9B768m6mu_6rsKUAUab2PUgPHXmGycQZxTEBfOI_FOJaMwCHnrU6ExkbNCN_Hl4guhNFvXid4K9rNveZs3FX6xqswvzXp3GZ0NZcQd0lnQDW7I1niqByKpKGsum7rCxKADrQe4v_cJTZbLdQPFJHaodJLjKwE_Z5hNnRmuXPyIMJSlDDKGoEo1N2pc4YRoz2ornkkOmfXjhTjkw3YFlczXUTNEa3A8WYxj7VPHoMC3aakk56SS9YXShbLgJXztQhI9ZCysdoQ-Z-rGgEkiRKC3mLoKbQI-xAJla1WJ6FCgUbKWueVwN_GFbhklc7IEj-Yi7M34ydLy3JG3QgPEGvmsx48lp6A3D4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«ایرانی‌ها می‌گن: همه رو می‌کشیمممم! همه روووو!
همچنین می‌گن: الحمدلله! الحمدلله! الحمدلله!
منم بهشون می‌گم: بابا، شماها واقعاً دیوونه‌اید!»
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/73080" target="_blank">📅 00:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73079">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8279d9c497.mp4?token=na0v_oEH1WsRKPF62a4klCECZLE-njxrC-NRKo7Opo3-MqZODLdEO_j-6C7nYHlSvMlcgofjFwWb7GKgPVRf7Ge1owXILNZMiw21VRnAjfkmXityQ9qfekH61fCUIsYMNlhQQk24nkScF2apcLWWqI3UVYOklc7TQ_LgSubaaYH8uF-NpUwUhAu1z3pq92ijVxuFCB_wUeIQbvVvA9D9AohHaCN9q9VhEALUyg1Fl3C2p2TX8MXswMh83CwwPSlrFrjOGom4U2jtMNErkq5eiKPA7jk7NxCxiWC1N42N_nri3WtjQR4643-nX7_NskyyVfVMWlBtAQbMkcqY0Rraww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8279d9c497.mp4?token=na0v_oEH1WsRKPF62a4klCECZLE-njxrC-NRKo7Opo3-MqZODLdEO_j-6C7nYHlSvMlcgofjFwWb7GKgPVRf7Ge1owXILNZMiw21VRnAjfkmXityQ9qfekH61fCUIsYMNlhQQk24nkScF2apcLWWqI3UVYOklc7TQ_LgSubaaYH8uF-NpUwUhAu1z3pq92ijVxuFCB_wUeIQbvVvA9D9AohHaCN9q9VhEALUyg1Fl3C2p2TX8MXswMh83CwwPSlrFrjOGom4U2jtMNErkq5eiKPA7jk7NxCxiWC1N42N_nri3WtjQR4643-nX7_NskyyVfVMWlBtAQbMkcqY0Rraww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور گلشیفته فراهانی در فیلم Matchbox: The Movie 2026 و صحنه لب گرفتن او با جان‌سینا!
+ نکته جالب اینکه همسر جان‌سینا هم ایرانیه!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/73079" target="_blank">📅 23:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73078">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be8b607f1d.mp4?token=spXjevbd-a0d8lnOuOvWqFHSRkhrZu15YcjR3MPi6rvOgDLtSFIcSGZ7jm4uKUwWiR2VlZTmfr7EfqZfVWlprrZ8I-6LPYhV8_xrssKxEhX4S2tEUUv_fb2WowPoNCaV7dt1RiHFlCTR4enIuoQIAPsP1XG-ETv05hQsQqazpKtuquV_hhvxAW-IzGvh8IytBvaKu4k-ZkcAOr3ekYjWeUf3gXQ-Bw77HA7YbvTxX7WkRUPJUbYNwo2mRMdJST55Z7dEzPDfeELl29ydej8BI85vivHR4N09rCgHH1QwZq9REP10CU6sozIQQc0uk8jamipVI5w9IMmmCb-RljqNQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be8b607f1d.mp4?token=spXjevbd-a0d8lnOuOvWqFHSRkhrZu15YcjR3MPi6rvOgDLtSFIcSGZ7jm4uKUwWiR2VlZTmfr7EfqZfVWlprrZ8I-6LPYhV8_xrssKxEhX4S2tEUUv_fb2WowPoNCaV7dt1RiHFlCTR4enIuoQIAPsP1XG-ETv05hQsQqazpKtuquV_hhvxAW-IzGvh8IytBvaKu4k-ZkcAOr3ekYjWeUf3gXQ-Bw77HA7YbvTxX7WkRUPJUbYNwo2mRMdJST55Z7dEzPDfeELl29ydej8BI85vivHR4N09rCgHH1QwZq9REP10CU6sozIQQc0uk8jamipVI5w9IMmmCb-RljqNQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پلنگ حکومتی :هر روز صبح و شب اینجام که بگم ما فقط جنگ میخوایم  و مذاکره نمی کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/73078" target="_blank">📅 23:15 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
