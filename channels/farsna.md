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
<img src="https://cdn4.telesco.pe/file/GmHYsPgcrWS5yFbcFptC0uJreU35ZemWTOx83Ixs-2O86jlg6fJ9RtFENtoXzcMRbrIvJwI1sAYBA4-BL8W0Nes7Ah_kFRBcg9rZglRv-EV15yx4eEEgTmAiYYlUXXPIXIlttWmJyUMrkazomgA_FnvBY2Enuozd0yhGmQihlyANZsZThCkL6d4nndzqTi3Cv3jyyiC_xTe8_VreNFaT6_y98bEmD_1CLvMiAN4_VsUVG5ZInqZAiPeYwx0ysGYmdPF29xBpQSnr3pKabr3WrEad5IYszNcI-joA6U8BqZTyyvMf0g44VkvGatMYg1UKlTp67tGL_8A-A7pSzl1FTg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 17:53:23</div>
<hr>

<div class="tg-post" id="msg-445160">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55484b4b76.mp4?token=HHKP2IGe9XzAN4qDSkskiiKe87QX5vKnhI87vfP5f5fkB1Jch3NBfYZbJahaiM2radFFQ7vlKtsi7Y9m5_WFXNAvT2CWkQq9S4N3pIgEjkJZZrHgV5989dgYzjZ26mXlxFgVvp7U28pRH6s_ENFXN0ZAvWFNfyT1IcLSpNna8S7MBjrX6VyU5eLSqVLbbTdPyKypiClbdQUb34XTAXbViq4770CJAHZHF6KNJgeLrboL3-DUR9A0csPaDFR-JMljz3UFZQb5bxMvrRCGhRYwnE-z4NIYfqegCAVdgYRjr643rl_l5-zjdvUjV9HMkfVftQzDFxZBnFoPmULjwzzLokCk2rvUkOaMgzpYpZ1Tzf3_py7Nv4XgsQmrRouoGtWe-8bBenp_p1H5QKHE6I0KA_hVhZ3myjr62yU5m634irh9odbS4NLOchnelxB2yJGhPYOi1iSp0BemhmRZvZn_SvpRDIqmg3yzMa_cs6ZcRz4o2qs9PGQsehG-lejZRPZ4_fiZxqmxR__wBXEYHnYBiqZuzIpuMSZDxv3RRIubrEkR1iliJrE7TSfjKmNlEeKEpdf8g6PksBhBd0pA3YVt7uMUQWU3UtIcChy-VmFvNY-IVUqHG5cgdciIzR0n0Pg2lssGt0uJMxQT2APdNPL6oddkdQppJKdPUc_9JAKmi4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55484b4b76.mp4?token=HHKP2IGe9XzAN4qDSkskiiKe87QX5vKnhI87vfP5f5fkB1Jch3NBfYZbJahaiM2radFFQ7vlKtsi7Y9m5_WFXNAvT2CWkQq9S4N3pIgEjkJZZrHgV5989dgYzjZ26mXlxFgVvp7U28pRH6s_ENFXN0ZAvWFNfyT1IcLSpNna8S7MBjrX6VyU5eLSqVLbbTdPyKypiClbdQUb34XTAXbViq4770CJAHZHF6KNJgeLrboL3-DUR9A0csPaDFR-JMljz3UFZQb5bxMvrRCGhRYwnE-z4NIYfqegCAVdgYRjr643rl_l5-zjdvUjV9HMkfVftQzDFxZBnFoPmULjwzzLokCk2rvUkOaMgzpYpZ1Tzf3_py7Nv4XgsQmrRouoGtWe-8bBenp_p1H5QKHE6I0KA_hVhZ3myjr62yU5m634irh9odbS4NLOchnelxB2yJGhPYOi1iSp0BemhmRZvZn_SvpRDIqmg3yzMa_cs6ZcRz4o2qs9PGQsehG-lejZRPZ4_fiZxqmxR__wBXEYHnYBiqZuzIpuMSZDxv3RRIubrEkR1iliJrE7TSfjKmNlEeKEpdf8g6PksBhBd0pA3YVt7uMUQWU3UtIcChy-VmFvNY-IVUqHG5cgdciIzR0n0Pg2lssGt0uJMxQT2APdNPL6oddkdQppJKdPUc_9JAKmi4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلایلی که نمی‌گذارد تهران صاحب یک ورزشگاه خوب شود!  @Farsna - Link</div>
<div class="tg-footer">👁️ 698 · <a href="https://t.me/farsna/445160" target="_blank">📅 17:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445159">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43e464dc72.mp4?token=Oaoq4cNOwly0M8iKr92xzhY6KkHt0xQEa-GWbOTYE5-KuJMn1pGosUS_NemUKp7p7m6MwDzGPEt1htP7-21vY93_TyLqCXrOfg0pUQVaNOxUo4o6fC5WjGYBMIHQYwIx7mZSjnNr9-VPujOP5_F5HkYOOvZSs0XGcVzNNC_uUjXvoTFURMSeGXUKyB5JVo7aRaG9JBwviaK8H0qSsN9wR3Vcn2xxgVjfpAAxo197PUf-eLn2kXcIdw3vrgykcL1jIfKwjGz0dCg57zQbDVvpDB1stC2Z-WhfIWP-ll3SLEGITC51J0lJ4B1NWvEIBP2FJ_hCl0577ZOlQ60G0vzSWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43e464dc72.mp4?token=Oaoq4cNOwly0M8iKr92xzhY6KkHt0xQEa-GWbOTYE5-KuJMn1pGosUS_NemUKp7p7m6MwDzGPEt1htP7-21vY93_TyLqCXrOfg0pUQVaNOxUo4o6fC5WjGYBMIHQYwIx7mZSjnNr9-VPujOP5_F5HkYOOvZSs0XGcVzNNC_uUjXvoTFURMSeGXUKyB5JVo7aRaG9JBwviaK8H0qSsN9wR3Vcn2xxgVjfpAAxo197PUf-eLn2kXcIdw3vrgykcL1jIfKwjGz0dCg57zQbDVvpDB1stC2Z-WhfIWP-ll3SLEGITC51J0lJ4B1NWvEIBP2FJ_hCl0577ZOlQ60G0vzSWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ثبت تصویر سیاه‌گوش در جنگل‌های ارسباران
🔹
سیاه‌گوش، گربه‌سانی وحشی و کمیاب با گوش‌های نوک‌تیز و دسته‌موهای سیاه است که از گونه‌های ارزشمند حیات‌وحش ایران محسوب می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/farsna/445159" target="_blank">📅 17:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445158">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akLwIz6S2DNJoGvLQu-6QehKt3cRlpareqtG2z7j31SIkX6334k4Gg0Ekk-MhN8WVUkzzMFed1mV21osC5j-6ARcHUmXuIpcF3XxQyPr_BYkv-7l-8woeQmFD4mC2w1d3Fg_W5phoOS1pfEQgeabja-q43Hq0Nh8Obddf01Zkb442-N2uCtQzamRr_3Y3hDVsfMD7TjlsoZoX3nFGIyMQOhpb7SUYXzB9FvzR7j91EcKZqWb8E5PR7lxhTSB0dYhdmK9x1pjznMG4uaI65X2Q91HmwYLOUi-0JfHLVri3iilUZoxoqKzARKBMqs1tl6LxaOJza-6kwqN6KJ1FIddLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
ایران با برآورده‌شدن یکی از این شروط بالا می‌رود:
🔸
بازی الجزایر-اتریش برنده داشته باشد.
🔹
غنا پیروز بازی با کرواسی باشد.
🔸
کنگو مقابل ازبکستان پیروز نشود.  @Sportfars</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/farsna/445158" target="_blank">📅 17:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445157">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vw1fWQHj3Bf1jA7bpG3Ynjrdy4ZqR43Xt1k1JY5RkmxTVB9kf7iUwE80n7knx3hI4Imz6d74bkzHi9FM0qVJbWOOr_BqoAKSq7lH8nz_oTYDPxXKrfx10YDzkaE3s6H7OYnOze5JSz6sQoJCdzmQqWFW9tfwuUnHLr9aGnYHWKeRH2VifeSUElPKn6lyp5xBRD-XbGJkuWeb0OYqdtAcZvzNjSa_rH5foHirHX1oPPpHwjycadkGo6qSSrKyQRMIAT7xMJDtXnED5HCsw9iws555kwUgBOUNNNWY7ft_HCxbh79kuHfnNqHS3EG3b9w7G8id8gNxhGgn59QhrYN-CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا دسترسی خارجی‌ها به ۲ مدل هوش مصنوعی را محدود می‌کند
🔹
رویترز: دولت آمریکا قصد دارد دسترسی کاربران غیرآمریکایی به دو مدل جدید «فیبل ۵» و «میتوس ۵» شرکت آنتروپیک را به دلایل امنیتی مسدود کند.
🔹
این مدل‌ها برای کارهای پیشرفتۀ تولید و تحلیل متن، برنامه‌نویسی…</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/farsna/445157" target="_blank">📅 17:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445156">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a4c78429d.mp4?token=V80ATrG-tYXEFsMzTmBrc95XlkmvKbWxgpDq7OiW_dtHsA-zVy6jA1tDSnIrljuI4jGRDxpru4to0KdjLGagg6k9m8DPPzDs95tQliY80I3Rq31s79AbrbeOtUy9GNq3YlHmCd7sLyASts2cLVBviU77DWsHrM_pCL8FtNFJ7y6-m-3caw3tc0wkNxpF_2harH4Qc5xwpnjC6w8hdw_rKDyIictqWO3yN_C6Cg_TljSit5NNlWnQyD7apnAmdCGScaNo8oRFyxFpBVaBoBD6Um5wCrYmmLu-VvEqBEKNAw8aYbm-opCYm4GdOEIvsOfShItNXCXdUMlHqKNS8O4O_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a4c78429d.mp4?token=V80ATrG-tYXEFsMzTmBrc95XlkmvKbWxgpDq7OiW_dtHsA-zVy6jA1tDSnIrljuI4jGRDxpru4to0KdjLGagg6k9m8DPPzDs95tQliY80I3Rq31s79AbrbeOtUy9GNq3YlHmCd7sLyASts2cLVBviU77DWsHrM_pCL8FtNFJ7y6-m-3caw3tc0wkNxpF_2harH4Qc5xwpnjC6w8hdw_rKDyIictqWO3yN_C6Cg_TljSit5NNlWnQyD7apnAmdCGScaNo8oRFyxFpBVaBoBD6Um5wCrYmmLu-VvEqBEKNAw8aYbm-opCYm4GdOEIvsOfShItNXCXdUMlHqKNS8O4O_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم امام حسین(ع) بر فراز دومین قلۀ بلند جهان
🔹
جمعی از کوهنوردان شیعه پاکستانی همزمان با ایام محرم، در بیس‌کمپ K2، دومین قله مرتفع جهان، مراسم عزاداری حضرت اباعبدالله الحسین(ع) را برگزار کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/farsna/445156" target="_blank">📅 17:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445155">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">جزئیات معافیت سربازی در قانون جوانی جمعیت اعلام شد
🔹
رئیس کمیسیون حمایت از خانواده و جوانی جمعیت: براساس اعلام نیروهای مسلح افراد اعم از اینکه غایب باشند یا غیرغایب،اگر دارای ۴ فرزند باشند معاف هستند و اگر ۳ فرزند داشته باشند و ۴۰ سال سن داشته باشند معاف هستند،…</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/farsna/445155" target="_blank">📅 17:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445151">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/riVuy-0zxU_W9i05U1HwCrZCjiT9utcM_pl55rHO7U3Rr9oWjPaWL4niLUJ7621DNYjJMOo262U1dQdtvSGSutV5pWWZaIQH8zpQoCHvzD0ZejpEKf0kIo_SI__yX1krbTKP1H2VdKYmLgQgx0WuM3kyIAaKR88W2_ECRXzro59YzW8_GkdsKK1kq_vBgzY3yTlX11rg-j-Ef16XXi4wCgOdWdqSRDMr7I5YZP3fnZFbbtK3oGadf65CkZ-08Ep_p4ZdlfnnqkLincAhS_Kj2GEBWd_L6_nkK5ukNURMwYNRIzKUsytCrOcnlM9lNmrH81UthBBh4fMzAjESZuAGMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WB-K-o6HfslpFG6790a6_H6FoYMJ0o29JGiyKsbwiiJ8F84rQzvWUYI2o5HdcmSphmAajUH9To27QiBa3HixgGK5xCQXYR90ZGxUQ4-Hc5tM77AS-VkOmhaj5l-qrWXiwz6HUzp-2QRxLxA4P7kMkFysy7u0osVzrk07mRi9VGP6aybCy4c4R2FiRuNjnNFEB4fzaxnv2Rvia1AmkGvwMNCwCzbchhEWPg6YVE4MuvpP_gQqwdDtrxO7NBPNPEct-AFk7zngmZjz3Yur3VRLyd651NO5-8oL44E8ihEyoOIucQatGUJm8sMMWMKnWNc6JLZGQAmoWBeNowrHE11JTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jDLqWsfW3vlFG_8SDqttdetlIC477OAX45WHYilNpiyi2CDARyw-Bw9qffZR-nw1zMCDqCQEcIRaYfkHCENzzFNUpsL2DOMivI3nV3QTNQpQyFi4Gi3L5n5utXl5trAqYAUW4FbjVjbbLuV5XMxfu4GCR65FQOC5ERuXCIukPMB_NNykJeWkjTf1enlw7daVICN0Lo19iGFpqtSjuRyFuvpQv3zUX_ZL1Wdeqr9SdUy4zdwO5gY8Dnh2cI7DGv3T5qsEZjFyEeeOq-4xVLZF_8l3_dQnLQL9CiQfk0cdB0oW9y8Th-L1puLl96y4Qpjux2ZIR-4Tn61WQnBmOxwYQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j_wG7gyGOS4i6RVjrNqKVJy2ZdKoKnDVUe4noSR4_eONAuyZnRrTuA-yh1KarDIm2bJJMQEyTRNw6hLdsexgpaZZWweJ8klq4LwSYKiJ-_A-evMk2vHyCMCTe5Q-_B5HEMBoodeqCWTK61iUcojBbOCcHh0kaAf7YhL7MNqqmikbybz8dB58oKcrCb-aar5IIvLMmSkettu5_QI2mjYKMuKLsl_Ys49rDEpnV7-wsHLjVsEY7A8HReljDS1L-IPEtDQurbx9SiNUGpGIFrxn1vafZO7zRpQfXregKUnhmVyyrAycIO3suIsswqwKiCTNRf1GZdld4OtDoS1b61JsAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست سران سه‌قوه به‌میزبانی پزشکیان برگزار شد
@Farsna</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/farsna/445151" target="_blank">📅 17:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445150">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: ما با تمام ابزارهای لازم و فشارهای بین‌المللی و عربی پیگیری خواهیم کرد تا دشمن اسرائیلی به بند اول تفاهم‌نامهٔ آمریکا و ایران و عقب‌نشینی از لبنان پایبند شود. @Farsna</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/445150" target="_blank">📅 16:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445149">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: دشمن باید از خاک لبنان عقب‌نشینی کند، زیرا متجاوز و اشغالگر است. @Farsna</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/farsna/445149" target="_blank">📅 16:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445148">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: توافق دولت لبنان و اسرائیل، محروم کردن لبنانی‌ها از بازگشت به سرزمینشان است
🔹
دشمن اسرائیلی چه ارتباطی به امور داخلی ما در لبنان دارد؟ هرگونه توافقی باید صرفاً محدود به جنوب رودخانه لیتانی باشد و هیچ ارتباطی به مسائل داخلی لبنان اعم از…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/farsna/445148" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445147">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: توافق دولت لبنان با اسرائیل، مایهٔ ذلت، ننگ و واگذاری حاکمیت لبنان است
🔸
این توافق از نظر ما باطل و بی‌اعتبار است و به‌جای آن باید مفاد تفاهم‌نامهٔ ایران و آمریکا اجرا شود.
🔸
تفاهم‌نامهٔ ایران و آمریکا «تمامیت ارضی و حاکمیت لبنان» را تضمین…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/farsna/445147" target="_blank">📅 16:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445146">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: سلاح مقاومت هرگز برچیده نخواهد شد و هیچ‌کس حق ندارد لبنانی‌ها را از حق دفاع از خود و سرزمینشان در برابر اشغالگران و قاتلان ملت محروم کند. @Farsna</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farsna/445146" target="_blank">📅 16:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445145">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: گره‌زدن عقب‌نشینی اسرائیل به خلع سلاح مقاومت در سراسر لبنان، طرحی بسیار خطرناک است که از تمامی خطوط قرمز عبور و لبنان را به بازیچه‌ای در دست دشمن اسرائیلی تبدیل می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/farsna/445145" target="_blank">📅 16:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445144">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مجلس اعلای شیعیان لبنان: توافق با اسرائیل اجرا نخواهد شد
🔹
نایب‌رئیس مجلس اعلای شیعیان لبنان: توافق مقدماتی میان دولت لبنان و رژیم صهیونیستی «تسلیم در برابر خواسته‌های اسرائیل» است و راه به جایی نخواهد برد.  مشروط‌کردن عقب‌نشینی کامل اسرائیل به خلع سلاح حزب‌الله…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/445144" target="_blank">📅 16:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445143">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvYHyCKekjhXRo46kvoLKFDyqpICxZbiWr3Y04uNKQJtD-3ze6WG4ft9j9OzNUYCLla3M4XLv0a9Xsh4TEhq0Sx0GRx8BY-pvg-1HlJGRx4cOYAhY30hz66M2I2gcv_KkBR_QoE5R68iMVKwb2S4po0oFLVvOt-49k4fY8oE7rWQCva35GQWorACoQFTHmw_FJZ8mYX-5sJ4HkKo4u57-78gn4iK6UTFas_tS1zsm37cQ2Vfgx8VQLw9_y05hcSVGLTa1gwhCF6RK9aKlZSrhI98vBJmPyPh1FAepTkE6ZVbA_MSYPM5UY44rwBt6Im8qIGHtIMWuWoF4cxO1kJCQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نصیحت جولانی به لبنان: اشتباه ما در مذاکره با اسرائیل را تکرار نکنید
🔹
روزنامۀ لبنانی الاخبار نوشت: جولانی رئیس‌جمهور خودخواندۀ سوریه، در دیدار اخیر خود با نخست‌وزیر لبنان به او هشدار داده در مذاکره با اسرائیل «اشتباه سوریه» در دادن امتیاز بدون دریافت تضمین…</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/445143" target="_blank">📅 16:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445142">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jg0hoCr-xN8xMRlBYdPuogMz8JpWHxAqkVd7S9S9Qcp0LOjrpnwjkZCa9xlaNi6qVW6953LIcwJrj3Cw7jVOpaHdHVMmSEdq_9hU4tOqhFbJ9oqj2k_sB7f1hHcaVvAkpqSUFRG0X3nvwWP9gjAaidTXTMkuJi9fNd47nNhLVQPb6o6lSHyGKuLb1mNTuGZBMzQ41NVnMjt1F7k47I4MZSfOyYNDBhtlPeJbPWYyrj-oKFZz5nTtvWgE6g4JeQPIqMMs7rAJDu76nxmBX5MT5mbi4-nLIATTHYBgW4mUgCVyNx0KTJVD_k6OJh_tHRwibJhf2E4DfTAXFSmUZsssVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان ثبت اسناد: اموال وطن‌فروشان با دستور قضایی فوراً توقیف می‌شود
🔹
دادستانی کل کشور دسترسی برخط به سامانه‌های ثبتی دارد و با دستور مقام قضایی، اموال این افراد شناسایی و بلافاصله توقیف می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/445142" target="_blank">📅 16:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445141">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/073ee0c888.mp4?token=E1KDgt42XcvccZUG6EiVQsxT48caiZOnh8hYfd7wT5hHZej31Ze2flnHLkgx-ibjJoByVC4benFugcHzQTRBIQJKr69Fe7Tczxtn31067d9HOO1OqGDulrQndV4NniPi7rG1yKK4dymfPq5-C9yVj5jiVmM5rYHEMSV0N95YP2EBA80krQdCIIJJw6HmhXw4gNVobohKUE_RQARzEUD2OOr6VNt6_MZ1mOIr7oKxYngrSrlj5yGPlJUp6Xsgvdz5JiJxi3GKuO17wCZia_w2xLko66KI2L51WL7kuAX591bh20PizRttZl1G-XQInxwwttSIYvoOpvglyVEKfeZeJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/073ee0c888.mp4?token=E1KDgt42XcvccZUG6EiVQsxT48caiZOnh8hYfd7wT5hHZej31Ze2flnHLkgx-ibjJoByVC4benFugcHzQTRBIQJKr69Fe7Tczxtn31067d9HOO1OqGDulrQndV4NniPi7rG1yKK4dymfPq5-C9yVj5jiVmM5rYHEMSV0N95YP2EBA80krQdCIIJJw6HmhXw4gNVobohKUE_RQARzEUD2OOr6VNt6_MZ1mOIr7oKxYngrSrlj5yGPlJUp6Xsgvdz5JiJxi3GKuO17wCZia_w2xLko66KI2L51WL7kuAX591bh20PizRttZl1G-XQInxwwttSIYvoOpvglyVEKfeZeJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میثاقی: مدیران پرسپولیس ابر و باد و ماه و فلک و خورشید را دیدند تا این تورنمنت برگزار شود که شاید سهمیه آسیا بگیرند و بعد به چادرملویی باختند که حتی تمرین هم نکرده بود.  @Farsna</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/445141" target="_blank">📅 16:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445140">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ok9qX523OrJb4f5plZ24_DVAYe2w4kuW49KopGPH7p0_AY5xIDF4WgQxqobzv4da_q5hYexIdChxks-QeU7M0lJNi9mbX2YqqGOLbsSRcxqIefxr2XllXvf39AhaNPzl9sSD_oXxsraUMXxxzjUZ9GuNeA06HO4pm4sONFw3kSr3FJUdxUW6tT7wCpm290cfhgQS9kptwKCFE8bUD_oYRfDKIE2QFoAUGAxGAiKOnxsWoQLTrxQxMB63zdlOzKnKk0B4LvDka3FYVYKdo-T0B0vw7potqTKWKU9ONPdeQlxtpivLiVAPJN0RmFURoPKzlmKMMBlBTLfMZXc2rS-pXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از توافق لبنان و رژیم صهیونیستی چه می‌دانیم؟
🔹
توافق اولیه میان لبنان و رژیم صهیونیستی را عملا باید طرحی برای خلع سلاح حزب‌الله و پایان حضور مقاومت در جنوب لبنان توصیف کرد؛ توافقی که حزب‌الله می‌گوید با آن مقابله خواهد کرد.
🔹
لبنان و اسرائیل شامگاه جمعه، پس…</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/445140" target="_blank">📅 16:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445139">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a45b79dc9.mp4?token=CUSipGrRJpYEAkuP7vL53Tur13auv9zOebUSWFCrk7BR5pFv6bu2gTZQug6BD-LeGZS8OEQ35RKSMRsdccRgAMFh2y0_TNEmzFNh1fMXYC1JCEu88Nhv8CC0AyldH-1W18bZZxlop2S4dwaSxinszHXuusnhFzOG65FD20eMzqCebEknTPmcsnf2MDAHwjCEWs0XE1rOr9BcNd70Ot4ZaJaFnUn8vTtqwjOwot5t9lxY1x_J5GjsUoPdVsiPai-aXLuEm1hgQb-9PtvDAnf-WEdwjdA6TzuQ5ZhLtgM813emkVnNWGzjng_BoLN7ytdKhaOTmJLUaUH_tPy3U6KfcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a45b79dc9.mp4?token=CUSipGrRJpYEAkuP7vL53Tur13auv9zOebUSWFCrk7BR5pFv6bu2gTZQug6BD-LeGZS8OEQ35RKSMRsdccRgAMFh2y0_TNEmzFNh1fMXYC1JCEu88Nhv8CC0AyldH-1W18bZZxlop2S4dwaSxinszHXuusnhFzOG65FD20eMzqCebEknTPmcsnf2MDAHwjCEWs0XE1rOr9BcNd70Ot4ZaJaFnUn8vTtqwjOwot5t9lxY1x_J5GjsUoPdVsiPai-aXLuEm1hgQb-9PtvDAnf-WEdwjdA6TzuQ5ZhLtgM813emkVnNWGzjng_BoLN7ytdKhaOTmJLUaUH_tPy3U6KfcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مستند ۵ قسمتی فیلسوف جنگ
🔸
درباره زندگی و زمانۀ شهید سپهبد غلامعلی رشید
🔹
از امروز ۶ تیر حدود ساعت ۱۷:۴۵ شبکه یک
@Farsna</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/445139" target="_blank">📅 15:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445138">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3yQN4c16KpX1GXEbDOcIHXhbEWQ8u6ogjsmZ_x8z2cgr2aD_94bP5bCJyK9xmbva0ttkoIbxh8JOreo5tTcKvnkjsgFyx08TTovdPVvJuUISaQt31vJ6HbplrdqFFYGpBbTRpJLmF019ke6RO3NxNbZi7TI4EHwL-Jb77sEIV_oc_nqr5NbOkF6sGo8qixuM5LArID1B8fPpLiklzLHObtCIiILq4oYVUh82w3ykd7HtE7Mn0HFi0_tJluNlhHNqohfqGi2jZb_ZHUmYFEJ7fxzcwnEN6KsV5UvpMzHeHDWO5C238V7FAZDaM_6xB-naU3mp71SKLKlLN1cHprGhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
سرمایه‌گذاری ویستا در مدریک
🔸
ویستا، هلدینگ سرمایه‌گذاری ایرانسل همسو با استراتژی‌های کلان خود برای ورود مؤثر به بازارهای نوین و با هدف توسعه صنعت بازی‌های دیجیتال ایران، به صورت مستقیم در استودیو بازی‌سازی «مدریک» سرمایه‌گذاری کرد.
🔸
هلدینگ ویستا با این سرمایه‌گذاری، مالک ۱۷ درصد از سهام شرکت مدریک شده است. منابع حاصل از تزریق این سرمایه، صرف توسعه زیرساخت‌های فنی، گسترش تیم‌های تولید، ارتقای پلتفرم‌های انتشار بازی و صادرات محصولات دانش بنیان در مدریک خواهد شد.
🔸
هلدینگ سرمایه‌گذاری ویستا، با تمرکز بر استارتاپ‌ها و شرکت‌های نوآور در حوزه‌های هوش مصنوعی و کلان داده، فین‌تک، سلامت دیجیتال، تجارت الکترونیک، رسانه و سرگرمی، شبکه و زیرساخت و نرم‌افزارهای سازمانی، مأموریت دارد تا زیست‌بوم نوآوری کشور را تقویت کرده و زنجیره ارزش دیجیتال را توسعه دهد.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/445138" target="_blank">📅 15:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445137">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarmaye Bank | بانک سرمایه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgdEcqtBPwLZqq58We7Sk4KQIy1X4Hfl_nGbIi8N9zWhUIqS8I5YB2PYvJfhLC1AzQSlFYdADXQxBjTXy3SdAPh5u1ohC2HAXtdKJi4dr8o8_kLyu4PuExo5oipJQHt-My7QS7VWOZPXktBenqnP-U601-KXcB9xuB2j8swb7xt4FcKIHOT0w5FFdHdCS1bPGtUlhGKiBYnTCljDVdxe4TXqIg9S2gLhpBb3lNk3Zb-rTAiRrFuUyDVubYnAu2oLEM6yngvWzAbVbbX7SASN4HB_OhLiSjRf6Zu6ENxMQc6ckeXOF8MjqLC6IvlNjERIk8nQVkUAyzGf6HkAhh46tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏢
آگهی مزایده املاک مازاد بانک سرمایه در تیر ماه ۱۴۰۵ با شرایط نقدی و اقساطی منتشر شد.
🌐
برای مشاهده جزئیات، لطفا کلیک فرمائید.
#بانک_خوب_سرمایه_است
‌
🔽
بانک سرمایه را در شبکه های اجتماعی دنبال کنید:
📲
اینستاگرام
📱
تلگرام
👨‍💻
وبسایت
📲
بله
📲
ایتا
📲
روبیکا
💖
آپارات
📲
سروش</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/445137" target="_blank">📅 15:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445136">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/445136" target="_blank">📅 15:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445135">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46a7cb7c8f.mov?token=OQeCg4uFsv0u1iq3epzBL0iI0JmrH-VomuMeMHkuYH2HDt4MhSODxCndpbRIIdVAv9V49LXxMg2rA61rM6folNQQFocgMVHhPys0rTSKUofoHmPb1QCGkheiq9J-KLDMp-08VsBI4dIYRzOmyM9z9Erc-JUK4ddZOAdepVWMcnSj8F3im2uQ3PsRYJwD-_esMiM46PNLM7_qKtjXHPZDJ39IMHypLg2_jVS0LjdApE98Bf9kig9oPyBkngCIEI5vfVG78FEosnDVo-4CoWDZ6y_TkOwSEjaEwTpPTmBw_uentuHWPyKwe1C_20pI42F4941UyL7GkB06qlkRD1qY0ZPdVOTW_6RamwLWBXj0D9lLOw8qiUxk_7V-TPChfMQ97Jb9GyTZFkKHBYIuXq3pV6-SO4WuC0TRFNpH0NjRwQEx-k4B1bAm1SzeJAIJKYQFvcK8pyU6GpVmu5w83kYg28oPnxXG67WX5z-4YikJv190ps947W0OX-BJTzYq8OQrXSmdrOCg8ad1yRsk5yqnNEe4wYoF-bYsJD7Bk4JLVgyrCJqmLE3Gs-JOBwJ_XBp1Q1Mfw2tfnFA2j2pOuyMFv1ueruUhz_qMkKfoUcnWIip3abfSmaC3BECHaf53z9sp0r9WAkTcq9hC2VEygKXn90JjrJm9IMe3MrjXndPMpzk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46a7cb7c8f.mov?token=OQeCg4uFsv0u1iq3epzBL0iI0JmrH-VomuMeMHkuYH2HDt4MhSODxCndpbRIIdVAv9V49LXxMg2rA61rM6folNQQFocgMVHhPys0rTSKUofoHmPb1QCGkheiq9J-KLDMp-08VsBI4dIYRzOmyM9z9Erc-JUK4ddZOAdepVWMcnSj8F3im2uQ3PsRYJwD-_esMiM46PNLM7_qKtjXHPZDJ39IMHypLg2_jVS0LjdApE98Bf9kig9oPyBkngCIEI5vfVG78FEosnDVo-4CoWDZ6y_TkOwSEjaEwTpPTmBw_uentuHWPyKwe1C_20pI42F4941UyL7GkB06qlkRD1qY0ZPdVOTW_6RamwLWBXj0D9lLOw8qiUxk_7V-TPChfMQ97Jb9GyTZFkKHBYIuXq3pV6-SO4WuC0TRFNpH0NjRwQEx-k4B1bAm1SzeJAIJKYQFvcK8pyU6GpVmu5w83kYg28oPnxXG67WX5z-4YikJv190ps947W0OX-BJTzYq8OQrXSmdrOCg8ad1yRsk5yqnNEe4wYoF-bYsJD7Bk4JLVgyrCJqmLE3Gs-JOBwJ_XBp1Q1Mfw2tfnFA2j2pOuyMFv1ueruUhz_qMkKfoUcnWIip3abfSmaC3BECHaf53z9sp0r9WAkTcq9hC2VEygKXn90JjrJm9IMe3MrjXndPMpzk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
اعضای تیم ملی پس از یک بازی سنگین و بدون انجام استراحت ساعت ۴ صبح روز شنبه به وقت محلی به تیخوانا رسیدند
@Sportfars</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/445135" target="_blank">📅 15:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445134">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c57c7e4f9.mp4?token=EfjLm2n1Tj9qyqiNRjoCzqNwcg4ngN8XeayrZxqcPVL09aRVFXw5lly54N0Xy6tJ77I0y_ckiAt_CMHgwXK4EMizhRgPtJgOZ6Qc28sBq6T4fPkKAHc-a85dDrTcb1xh4dHRm3NJIM6A3hCZgHBDWewTf0dj1_7wWQRmXOg5I5D5cWb602cM97bqWyMc3NG9l4P8XpYPNFcyZSJLwBAR4CI_zOwLE2HlJ4sBT_lA7io17JK0VHuo3XMTnzmp8BFfbAOUCYXkIz72o4rFhvt0-MAmqoWEVPrrGbIWfoF28ExuOWUe9JkJiw5pnF6CkXvdD8CHjpe031nJbTFS7HB8eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c57c7e4f9.mp4?token=EfjLm2n1Tj9qyqiNRjoCzqNwcg4ngN8XeayrZxqcPVL09aRVFXw5lly54N0Xy6tJ77I0y_ckiAt_CMHgwXK4EMizhRgPtJgOZ6Qc28sBq6T4fPkKAHc-a85dDrTcb1xh4dHRm3NJIM6A3hCZgHBDWewTf0dj1_7wWQRmXOg5I5D5cWb602cM97bqWyMc3NG9l4P8XpYPNFcyZSJLwBAR4CI_zOwLE2HlJ4sBT_lA7io17JK0VHuo3XMTnzmp8BFfbAOUCYXkIz72o4rFhvt0-MAmqoWEVPrrGbIWfoF28ExuOWUe9JkJiw5pnF6CkXvdD8CHjpe031nJbTFS7HB8eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میثاقی: اوسمار بعد از بازی دیشب اخراج شد و پرسپولیس با اسکوچیچ بسته است
🔹
مدیرعامل پرسپولیس وعده داده بود که اگر پرسپولیس قهرمان نشود کل حقوق و مزایای ۳ سال گذشته‌اش را پس بدهد. @Farsna</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/445134" target="_blank">📅 15:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445133">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrbXy9v5au67zTEAJ-OKTw_gk0Zg7f4m2nl23tQ4UMjQD3bIAmDAzWXXOXBjbBPYkj0bEplEKX8wgLVXohmHxtfWgcFBllhJfqCEeXTZRH6KU1n_A-uSXJx3Np24b_VnMQQWCkMlP_m9RwY2ptoBNuPCSbZe5D-xCCM-RvH-rC5FmUFoJEUtNWXW7_fc0UJbaMMj3EEzGc3_gMpB3MLzI8m7TU_n4sG0EuRUOWV57hPxxrtxp4t8mogz_84oqBkCvAfQW09bGaw4_BgOkXAJ6XMymxYqXtCMfy-zLpMEXgGWV5uRSaNoTlCDdGTrNkkAmM7c1GDHhAlfjv3sKPe3vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸ کشور بازی جی‌تی‌ای۶ را ممنوع کردند
🔹
هم‌زمان با آغاز پیش‌فروش بازی GTA ۶، در بخش پرسش‌های متداول صفحهٔ فروشگاه پلی‌استین، فهرست ۸ کشور ممنوعه برای عرضهٔ این بازی منتشر شد.
🔹
تاکنون کشورهای بحرین، چین، کویت، لبنان، عمان، قطر، روسیه و تایوان این بازی را ممنوع اعلام کرده‌اند.
🔸
نسخه‌های قبلی این بازی هم به دلایلی از جمله ترویج خشونت و رفتار مجرمانه، مصرف الکل و موادمخدر، قمار و محتوای جنسی، در تایلند، عربستان، امارات، تاجیکستان، چین، آلمان و استرالیا با محدودیت یا ممنوعیت مواجه شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/445133" target="_blank">📅 15:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445132">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7aff68a8c.mp4?token=GK9d6JAPoSGR1Jc51K46-1JRiLB8Tq8WUC8bNaea-xxSmCxdyCZRUfAW44HCEAbYxbwINpL9irspXoIdlPekjPGr5J0tDTJI4crOLFwyKOYroQMWmupHILzQgbdhNMQh9vR8xUhYqwlxGT0DyLAMh1cuM8FuChXmJqAMbD37Qz6xr5DAvg217Q9L-jrCtvUzXzsbswuVDrFPCw3YToMSXsINOtwVFTKMNvbNAelAQCNi6PtANSnwKdtudz9ZMOD8eCdRE9c-mEEkobOcHejn577OajDoRZjpc4WyzGZM7Ox9BjyRLreTJ1b8ns0AntpeGnrpP1JiDJ-0Fmn_tR1YFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7aff68a8c.mp4?token=GK9d6JAPoSGR1Jc51K46-1JRiLB8Tq8WUC8bNaea-xxSmCxdyCZRUfAW44HCEAbYxbwINpL9irspXoIdlPekjPGr5J0tDTJI4crOLFwyKOYroQMWmupHILzQgbdhNMQh9vR8xUhYqwlxGT0DyLAMh1cuM8FuChXmJqAMbD37Qz6xr5DAvg217Q9L-jrCtvUzXzsbswuVDrFPCw3YToMSXsINOtwVFTKMNvbNAelAQCNi6PtANSnwKdtudz9ZMOD8eCdRE9c-mEEkobOcHejn577OajDoRZjpc4WyzGZM7Ox9BjyRLreTJ1b8ns0AntpeGnrpP1JiDJ-0Fmn_tR1YFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: از بعدازظهر امروز در نوار شمالی کشور بارش رخ می‌دهد
🔹
در جنوب شرق کشور با افزایش ابرهای همرفتی، شاهد بارش‌های موسمی خواهیم بود.
@Farsna</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/445132" target="_blank">📅 15:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445131">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVnxoPiJlTJyiMnFNOGKEv0XOMkIDYTjGNGLSoERjALVMHC_H4cuG9CYj0BIHB5ZG6Pt1kwBY24OK8GVFYZxz5MEk-_FJyFOVGme7CE110qHfVUVxbEkmWsWZTy8n-UHRE29lbk_ymOK5UehgIy2bEhWGI4_7jUoB01k2rqOV9lM97DDmMxV5mim0b6jIQ4ya5BxMy64iKsdiJMjTheo-xnSy930d42LWONDMJu0NHudTvCmVv86Cn4w5y2il8VjxmIkZAp4ytQw41V5VgyEuRrzUwdjltWbMBFjoF8ktLZ9beqUe93e0sGdVba9D2WbQbW_GnscU-TxlZV5DQeVQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران نگران تکرار تاریخی تبانی در جام جهانی
🔹
۴۴ سال پس از یکی از جنجالی‌ترین اتفاقات تاریخ جام‌های جهانی، بار دیگر نام اتریش و الجزایر کنار هم قرار گرفته است.
🔹
رسوایی خیخون به جام جهانی ۱۹۸۲ اسپانیا بازمی‌گردد؛ جایی که آلمان غربی، اتریش، الجزایر و شیلی در گروه دوم این رقابت‌ها حضور داشتند. الجزایر در نخستین حضور خود در جام جهانی، ابتدا آلمان غربی را با نتیجه ۲ بر یک شکست داد، اما در دومین مسابقه با نتیجه ۲ بر صفر مغلوب اتریش شد. شاگردان محی‌الدین خالف در ادامه با برتری ۳ بر ۲ مقابل شیلی، چهار امتیازی شدند و امیدوار به صعود ماندند.
🔹
اتریش پیش از دیدار پایانی، شیلی را شکست داده بود و با چهار امتیاز مقابل آلمان غربی قرار گرفت. شرایط جدول به شکلی بود که پیروزی یک یا دو گله آلمان، هر دو تیم اروپایی را راهی دور بعد می‌کرد و الجزایر حذف می‌شد. آلمان در دقیقه ۱۰ به گل رسید و پس از آن، دو تیم بدون حملات جدی تنها به حفظ نتیجه پرداختند.
🔹
این نمایش با اعتراض شدید هواداران و رسانه‌ها روبه‌رو شد و آن مسابقه با عنوان «ننگ خیخون» در تاریخ فوتبال ماندگار شد. در پی این اتفاق، فیفا از جام جهانی ۱۹۸۶ به بعد تمامی دیدارهای هفته پایانی مرحله گروهی را به‌صورت همزمان برگزار کرد تا از تکرار چنین سناریوهایی جلوگیری شود.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/445131" target="_blank">📅 15:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445130">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b68a2145c.mp4?token=ZFFMOxiy0Y1LVbHTL0R1VQtvlATg7xoB5sp4d3diFupO5iHZsPT2SO6t2Yac-04-_pCm5iqk1zMP0FjvQLpLWnkTeQiyaKS0szmS4r0C4qarkOHpduNjuUl-Lp-6nE3YWcgkISTlBXFZg_NApcF8S-SDk5hi9PpTVh_5Py3iht5j-z7acV24yv8W2euZ4kA8lUKQUIuJ8ShqIfg6DJy7QlQL886z8LieIpJQzmGnGMaebkIO-0aFx7g7CnDRbUUdAk9tRwL8Zr95hlYsvhhqCpHbPXPZmZTpR4lRwjuiqpl3ir0Ga8Xr0xL5ah3BUsSOxPYMWd_emO65fsvmNE35yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b68a2145c.mp4?token=ZFFMOxiy0Y1LVbHTL0R1VQtvlATg7xoB5sp4d3diFupO5iHZsPT2SO6t2Yac-04-_pCm5iqk1zMP0FjvQLpLWnkTeQiyaKS0szmS4r0C4qarkOHpduNjuUl-Lp-6nE3YWcgkISTlBXFZg_NApcF8S-SDk5hi9PpTVh_5Py3iht5j-z7acV24yv8W2euZ4kA8lUKQUIuJ8ShqIfg6DJy7QlQL886z8LieIpJQzmGnGMaebkIO-0aFx7g7CnDRbUUdAk9tRwL8Zr95hlYsvhhqCpHbPXPZmZTpR4lRwjuiqpl3ir0Ga8Xr0xL5ah3BUsSOxPYMWd_emO65fsvmNE35yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل پرسپولیس: برخی بازیکنان پرسپولیس باید فردا خودشان قرارداد را فسخ کنند
🔹
کارتال، هاشمیان، گاریدو همه آمدند و رفتند، واقعا کادر فنی‌ها مشکل داشتند؟ نیمی از این تیم مدعی است باید در تیم ملی باشد ولی مدل بازی آن‌ها چه بود؟
🔹
بازیکنی که دنبال کسب‌وکار…</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/445130" target="_blank">📅 15:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445129">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10cf0269e.mp4?token=AYF6_NG5VxcWvlPLH-_jFFsjDkY4hSvX3sOsjGDh6BfXY4Uruy926ThRH28Z__a9C0yL2S9RgdkqqQj6uyVOsUTb0ev8_trdcAxa2nOiVTZJXwP_gN8n4ARGC4jGos28NQ8hixg5aUMfoNtHnRt6oCD54v0CcTM3oMFbMMaOQ7R2M1ByzGCge60dJ7FN1Dr6_BitQUF7joO7KoYUV0zUv9qC6Vy2O0u230BHcleNVgq7yxQdUatgV9ULD_h4cVfQdIGtvAlt9hLMGyECYnnYN2dEe5o_rDTGxquptrXPaWPHeZ3XxMUMGMEHWHhWF_RT_gg-UFmuRQxTe5wUgXArGAMgaQCUrvzHZNkhWm8_Xbdn1qLEHwTHFUjLZyAoDImja5ePd5MzVKl9au73ZM8aIaB2SFTxVgPc0lsH6QoxkdoY7stT2OVv_zJDL0DTKhquSoNcSMlR-S38cn6wVtBAp6Cg2-2kuOTR_6Fpra-M-ExM6gCifl5Vde7JQ8F0jEMNWbIj5yhyXGufjyhoXX1KD8djT2uPrR-dZzO_GXkwz_wp2ToGw9UfAxzhZiRNP4pdzvMwN4nFFO8mdUZH0a50QM18ic2Ioo7ViyWxs0j_72cFvJwm5OYjuLy3oCW-Nvd29k-8PnoIvMa1Y2X48NmDI1AVG1dlMWtFRV4aNEMy3yo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10cf0269e.mp4?token=AYF6_NG5VxcWvlPLH-_jFFsjDkY4hSvX3sOsjGDh6BfXY4Uruy926ThRH28Z__a9C0yL2S9RgdkqqQj6uyVOsUTb0ev8_trdcAxa2nOiVTZJXwP_gN8n4ARGC4jGos28NQ8hixg5aUMfoNtHnRt6oCD54v0CcTM3oMFbMMaOQ7R2M1ByzGCge60dJ7FN1Dr6_BitQUF7joO7KoYUV0zUv9qC6Vy2O0u230BHcleNVgq7yxQdUatgV9ULD_h4cVfQdIGtvAlt9hLMGyECYnnYN2dEe5o_rDTGxquptrXPaWPHeZ3XxMUMGMEHWHhWF_RT_gg-UFmuRQxTe5wUgXArGAMgaQCUrvzHZNkhWm8_Xbdn1qLEHwTHFUjLZyAoDImja5ePd5MzVKl9au73ZM8aIaB2SFTxVgPc0lsH6QoxkdoY7stT2OVv_zJDL0DTKhquSoNcSMlR-S38cn6wVtBAp6Cg2-2kuOTR_6Fpra-M-ExM6gCifl5Vde7JQ8F0jEMNWbIj5yhyXGufjyhoXX1KD8djT2uPrR-dZzO_GXkwz_wp2ToGw9UfAxzhZiRNP4pdzvMwN4nFFO8mdUZH0a50QM18ic2Ioo7ViyWxs0j_72cFvJwm5OYjuLy3oCW-Nvd29k-8PnoIvMa1Y2X48NmDI1AVG1dlMWtFRV4aNEMy3yo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تثبیت اشغال‌گری در پشت نقاب پایان جنگ
@Farsna</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/445129" target="_blank">📅 15:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445128">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🎥
خواسته‌های مردم در صدوهجدهمین شب اقتدار چه بود؟
@Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/445128" target="_blank">📅 15:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445127">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NO8bN0-fd0JH3bKmhYi8n4wYhpBgEhtWVoWKaqgNIBrnkR-rGlnA6LGCae8WxYVJLDnjPMsc8FfQH3zQuhLUKXaDkQqYDlFhmyT8-ev_4be96FGjBTAEaeAzjonvv_5KmcDqB9n6OuA-sU9yL-D9iWMPKqDcdWB49thL9WEP8bLkJG1fYWhlPmhYGdcySzHwDCWj_2FVB-I-siGmj3NX_Q96A2Y7kAf4DxFq2bpt0narOSyZeoR3mSfhLDUyhp8XxTvsmO04_ClNpnCNgFssC4JZB4Hfs3rxOVGJMWKFjq6AGM72whzROr6kQFV7o4zi1SHdX6N6pVott6MwKmVoDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار سازمان غذا و دارو دربارۀ مکمل ON
🔹
سازمان غذا و دارو اعلام کرد مکمل ورزشی ON هیچ‌گونه مجوزی از این سازمان ندارد.
🔹
این هشدار پس از ثبت شکایتی دربارۀ تقلبی‌بودن این محصول صادر شده و موضوع برای بررسی به مراجع ذی‌ربط ارجاع شده است.
🔸
سازمان غذا و دارو تأکید کرد مکمل‌های ورزشی را فقط از داروخانه‌ها و مراکز مجاز تهیه کنید و برای اطمینان از اصالت آن‌ها، کد رهگیری محصول را در سامانۀ تی‌تک استعلام بگیرید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/445127" target="_blank">📅 14:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445126">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db4936499a.mp4?token=fMQTbPklm7YG6pJ3pYObTrqznQ30Ddmk2EfPw6j6SkEAQcMhqcfDgNBYL-_KEvfUIFxNIXYtZXtwVkOVY7_AcSo3VI3l4C2b2hBcTmojd0V8mrEUkYmh1OElJY9OOzTojhZZMUVprPcqIqWMmvcswMkTxcqFwQsgesSyPy5iAr4Q-y6nscqivdTkavIrl9iGcMr6mgx12xRdcq1BJvv_Pb6B8BhmMz-HTe0JLT-2HogXcfRcFAb-xLN68wkOPWfgvPgvrWbtbxXaE_wIo-EntydgGifnIL9IqgOoVGlurJKGs1UHS1Ao-Rqpjly8OwcrAA7pBiSJpX0TccgMUL5Hp4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db4936499a.mp4?token=fMQTbPklm7YG6pJ3pYObTrqznQ30Ddmk2EfPw6j6SkEAQcMhqcfDgNBYL-_KEvfUIFxNIXYtZXtwVkOVY7_AcSo3VI3l4C2b2hBcTmojd0V8mrEUkYmh1OElJY9OOzTojhZZMUVprPcqIqWMmvcswMkTxcqFwQsgesSyPy5iAr4Q-y6nscqivdTkavIrl9iGcMr6mgx12xRdcq1BJvv_Pb6B8BhmMz-HTe0JLT-2HogXcfRcFAb-xLN68wkOPWfgvPgvrWbtbxXaE_wIo-EntydgGifnIL9IqgOoVGlurJKGs1UHS1Ao-Rqpjly8OwcrAA7pBiSJpX0TccgMUL5Hp4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با هشدار سپاه تقاضای کشتی‌ها برای تردد در تنگهٔ هرمز افزایش یافت
@Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/445126" target="_blank">📅 14:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445120">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LrmuteerMi7AdIojFUoTV1NKs_cbmXLcvJpCjssHOPJNaorMuY7KltFiVNVr33bzsp-byHmLBvw_LQA3sQM1jjq8AQbzpGr7TLBwoR5hNxf9ts-cMqqzN3rZnq_CKkLiTJ1oi3hnMwCCBTpyW7kprOLrMGgfWGSZw0ZLzVt9kEz462dWaJBnZCO2IY2ZCKlrMOJrtZPauaQXhPFsuiTIX_SJ_eXpTfjpwpNj04zw0m4tFYerkpXmY3C0JS0hrTk4I3jfM3DtA6mcqrGkm5QVqgziD9sndy7b5lFs0_2Awr1Qa3ZpUCQpsSCOzpuICMOO1Ojam3tuqI7vTB3fmtLjlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dCLXkv9YCz88GlAWHgd8Ttfr-GajtQjZ2i3L5Gju6dOrVTDIP6knixBTXeSJlIBJ9l3iFxPyWsgoVZrM_OoYHAIyFNMujcjda0XexQr8dC6wYP4ABTW-qoLYj10vOsaJgPSoD0GhYSRtFe09T1X6RqowASytLXyDc-60pV9oict1vV_MGTPuS6hfGXUiXWCN3B002aGX2q10UeDMpW1IwKvlNi596IhaB9f7W8eWGS2bKqeHpSUxpKQBkUM6wyoLj2kjlIw2OkPR5q-s6gP3DVjYNFTHUyFmcelb3_bacppqVPj6eeUgLO9L9DeOmmCyl3TL17ofsZYK6Zsnuo-cyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QwbQFCPvUoxAO2Rtevynv5i_4Hx-Yskf6VRYvKJ6gsCTaAHrDws72JxRdsfb86NWPBIa-ZP9gC-ONkwbH4TfvcEg9LrJ4fO4l6Gnx3KG9y8wrQRTEbeHC0gJUlLeUUYpx6-UmsMoveH7kwjG_DxfF6QHCssUqX8RM1U8Byn2KOYrQCB1c_ryMVQ9EULQqkcX_LwKC893McHkJPvbt6slTs6-heDeWod8-EUZxyCwmvVqpwI8H0SYCMH4A6XYGmbwg6_wlq0j8Oj3dCTz0m_kgWfiR8h3WILDka6NbC24XmQKo3Yu1nRPM8f0aPK9GFmfxKPptyKA6bud9Z_ArTaxBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P73o7ryUshff7G8WuNzsjHo6I8_CNJ85BrnMC9kluVt7jz7buDw3wB_NcHbftOZYErGUVJ6sk5HlJsa_9U6icnGDPYwR613kXnMhuXdh8r4gL99_pcNSyXfYTQE16t4MuCuJwr0KR4cm6Xan5iFlYeFE4s_R8Un_DQ55Et7k1DBZ6paDm7Sl5yQCgtqi-Lqsm6IjLJWwhsg3IEzrf_k2bSTq8hNaeGi_MEWVdLMTqwbz0Z2UEXx_XvtYo5VszRrTMnRBN-UKSk7qo3Doq7xryM5-vz5vAIFMTyBStkO7y8_lFgHoeRXDvsbHZzcyc0rC8yOEDX74uHbaQt5J9FfqHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hI7U-VYzof0JSfvy7q1FdqXYFmFgsGvDAHE8VplLQWxj5Fw3N3Pjsdr3K8mM7hvKuwXQ-9iLapMu94kFIaFca9GH_vs6aS_zi5RYDjZkj9TSckF8oPVKyhDvB3AOj77yYSWlTVT9ZbJm7FLiEhPJCe2IMmI8Vo2wqGyx7-zq1wrwqkPV5PDG1WvXQOWCyhArJ7mvtZdJLDHFIW2SmjrHFk3j8FFioCaDMug5q3dpy8T7Td3cbR1PsXQkW4pv0xWwx_3PO07znpblza5eMJ2m3oIq4l26C6YNsqYm6ZSRF5Cp7W-XbzSP8Fsiv8I_oqVoJcp7KMsyumIgX2LX6mVXXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZYUTB1vQ4YtP7x8UABY6ihy8Nlsvas4D2b4trYdVya9C5z9Go-d16xn55DFM0fcuB76W8a5bwPIEe7F0G5WxppI-tFw-HpJueXMUs1-8dhtfrvXXnTeK8DkdQsXTVaeMziOKROOK13kMPPRwkerVuithhE0-EquahzBVjKsVDm1p9FF2njRhNGvreT8TcP6U1sOGJHPhSrCDVzhXSFdPj6ppp1vgP5Ob9TMDai3UgSSxFrE3ZJmngbkyA1TakZ_05xzahJeXAKmL4NvKSgXr7UdAKhorkJy9mnDCPE10L6V2oiZ03xlNuRWlJ5aTFnt_lngA0aFBlx2M8rx_yEGtOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حرکت نمادین طایفهٔ بنی‌اسد در همدان
🔸
طایفهٔ بنی‌اسد یکی از قبایل اطراف کربلا بود که پس از واقعهٔ عاشورا و خروج سپاه عمر بن سعد، با راهنمایی و حضور امام سجاد(ع)، پیکرهای امام حسین(ع) و یارانش را شناسایی و به خاک سپردند.
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/445120" target="_blank">📅 14:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445119">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e4635e5.mp4?token=TMnUvsIA5Y4F4mKzgjMfOa_tkAYBIHXm-Rcc7m_mTWaz1cCYe3qz1qzZFuuVMIrJa_-Wmqq74HQiBwWZPAVoNO1RFh4v8C1qFHYyGyaNKhILd_k7RZScsOg4v6U8WRdHL2f8SP-cNHPlcAbt0IdSc2_MWlXG0R3vZR27pOyTO-IRkXkM1eYj1VI3ewCr36T6b_nDApQK9SnWDQLq64GHv8BcObsSjvfy3vP8dwgrwBEcQnvjUlEfpBU_ZhJN9H9Eio8JWBTdZ_AohYbc1h4oXbfegN82NVbPdn0XETHEXNWMY9OrIo-Vvg9YIDjYj3A1d3i_tSjIrHYN9YoiO0kQyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e4635e5.mp4?token=TMnUvsIA5Y4F4mKzgjMfOa_tkAYBIHXm-Rcc7m_mTWaz1cCYe3qz1qzZFuuVMIrJa_-Wmqq74HQiBwWZPAVoNO1RFh4v8C1qFHYyGyaNKhILd_k7RZScsOg4v6U8WRdHL2f8SP-cNHPlcAbt0IdSc2_MWlXG0R3vZR27pOyTO-IRkXkM1eYj1VI3ewCr36T6b_nDApQK9SnWDQLq64GHv8BcObsSjvfy3vP8dwgrwBEcQnvjUlEfpBU_ZhJN9H9Eio8JWBTdZ_AohYbc1h4oXbfegN82NVbPdn0XETHEXNWMY9OrIo-Vvg9YIDjYj3A1d3i_tSjIrHYN9YoiO0kQyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصری‌ها سلطنت‌طلب‌ها را از میان خود بیرون کردند
🔹
در حاشیۀ دیدار ایران و مصر، تعدادی از حامیان پهلوی با در دست داشتن پرچم‌های اسرائیل تلاش کردند وارد جمع هواداران مصر شدند اما مصری‌ها با سر دادن شعارهای «غزه آزاد» و «فلسطین آزاد» باعث شدند این افراد از میان جمعیت عقب‌نشینی کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/445119" target="_blank">📅 14:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445118">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7adc9a29.mp4?token=lRc94IV_cP_HRlIQndqmIDyUunMQ9TGGGKW8UrdWqqpf6v8QpkOosWljmuM6vF5J39Z34Yyyq96d6y_seTNP0as4m2UFjoOVhh9ycuKzGJqr2XKrQgjvZbOYugFn0cgn1ljZ5UZcs6bcU-Jm1zklyK-UVLZ1ABn8Xp4gA8HIJvKTBBiUHO1knH2_CxmSk5W18qvLOXddWoUVdS7cQIFjibAEOxNS9OLyBvQA-hWU_yEvzCDCcxmnxwYqh5v3okWK3K-IUWFq8Z0OJNeOf1fJB7G1Vm-PQ_dBC4Cu8g62_wQ9RRwHUE5-ZKaRKPMlfdOWb3iBWAOgtpBqQo5gFFDJyLbsZaUVn4FDg9YCDorgD019ZKr7H1q2PMYYiff7oUF__ChoDSo31fJnMm2yDf3mkQOUBegAQwErOhRFnNQlqK1okIx0YASBUHeO1eXxg4ovh1xeLb-E2lZPvW9j_DfRKdASWBOpY6GedupQt1kEEZoGbeI52Ekab6PAHhJQATpuI8wOe0pYKqJ3wQlma82OxMDFtU0YHYl3IE0ODD14K9Kx-beBBUJwJseJfNEBLsS30u5NV_WpuT1Bhv6HlOjzU3f4KEN0FiZ2_LVfa7VwCaZggHA6A6B0Vo73RIdLW5p6i91oZ8LWB2ghtO60KIV2w9AW3QnzMJ7PAMFoKoLkhi4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7adc9a29.mp4?token=lRc94IV_cP_HRlIQndqmIDyUunMQ9TGGGKW8UrdWqqpf6v8QpkOosWljmuM6vF5J39Z34Yyyq96d6y_seTNP0as4m2UFjoOVhh9ycuKzGJqr2XKrQgjvZbOYugFn0cgn1ljZ5UZcs6bcU-Jm1zklyK-UVLZ1ABn8Xp4gA8HIJvKTBBiUHO1knH2_CxmSk5W18qvLOXddWoUVdS7cQIFjibAEOxNS9OLyBvQA-hWU_yEvzCDCcxmnxwYqh5v3okWK3K-IUWFq8Z0OJNeOf1fJB7G1Vm-PQ_dBC4Cu8g62_wQ9RRwHUE5-ZKaRKPMlfdOWb3iBWAOgtpBqQo5gFFDJyLbsZaUVn4FDg9YCDorgD019ZKr7H1q2PMYYiff7oUF__ChoDSo31fJnMm2yDf3mkQOUBegAQwErOhRFnNQlqK1okIx0YASBUHeO1eXxg4ovh1xeLb-E2lZPvW9j_DfRKdASWBOpY6GedupQt1kEEZoGbeI52Ekab6PAHhJQATpuI8wOe0pYKqJ3wQlma82OxMDFtU0YHYl3IE0ODD14K9Kx-beBBUJwJseJfNEBLsS30u5NV_WpuT1Bhv6HlOjzU3f4KEN0FiZ2_LVfa7VwCaZggHA6A6B0Vo73RIdLW5p6i91oZ8LWB2ghtO60KIV2w9AW3QnzMJ7PAMFoKoLkhi4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امروز خوب بودیم اما روز «بردن» نبود!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/445118" target="_blank">📅 14:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445117">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🎥
آخرین وضعیت پروندۀ ابربدهکاران بانکی
🔹
سخنگوی قوه‌قضائیه: بر اساس گزارش دادگستری استان تهران دربارۀ ابربدهکاران بانکی، پرونده‌های متعددی در استان تهران در سال‌های اخیر از جمله پروندۀ گروه ایروانی، دبش، رستمی، مولی‌الموحدین، تعاونی وحدت و...  تشکیل و رسیدگی…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445117" target="_blank">📅 13:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445116">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Up9jbxRXzUEVgYe4DYB7pkNXyHmZ5r6ItBY_tQcarw4Hb5RWOm5D7pNTKoa2oOWkYvAN27jUFExr_DQwKx96702Csl6ZN3AD6FXWooivwODIfAzT6mgeoXv1ndZIJVTsdZJ8Wb03o9J5_eNSzZKSZNMxz9qWx__PWNxe7j2kV0oh5AswHz4Y23-zXoSxevuA6rZPrcrsNO4by86fCD6rR41yovgWAzLdvCH7FBI7TLK86dY3hQarZdGKh-0wb_FVU5PXfoxiEytBVPRBKJp4YsHaS33Ce1Ms_x7DVedrk284pWjAYF1hZY8CcK6wMEPoF1IMh6IpkgDtMYj5Zc6ebg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گل ایران به مصر  آفساید اعلام شد  @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/445116" target="_blank">📅 13:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445115">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">حملهٔ پهپادی به مواضع تروریست‌های ضد ایرانی در شمال عراق
🔹
رویترز به‌نقل از منابع امنیتی گزارش کرد که یک اردوگاه متعلق به کُردهای تجزیه‌طلب ضدایران در شمال اربیل هدف حمله پهپادی قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/445115" target="_blank">📅 13:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445114">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQoAoHjQuDjX1NsxyfMQCLfovPANXp0nNUZU-3nnh7Nqoe23PK183YFLWDmMEoaAOvYlUZaL4nnR1nhTH4O4KZunoOu4SWpYMXuWeOKCnQGHRAd8kIitDfDhVJkCCQ3Wg-Vbt8UDocuvoHdssqlNYI08tZuYNT32Ox2EtiR9-ZO3kgyK_KL9vtXSRKx4tvDJ0VhksRDRNnEyfvc9fgr3apz9j6Nb0x8zVUFEVD3uWd1sP7bS8npj5UaSgUSVXCgRYt7hsHgLf9LthJoNpX6LAsAOBXEg-pz-BFiOCRM8q9cd6GEL_axseojGie-4pHQRBdINpZ9ErbOZ3wzi39VfTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمان بازگشایی مصلای تهران برای وداع با رهبر شهید
🔹
ستاد برگزاری مراسم وداع با رهبر شهید: درهای مصلای تهران از ساعت ۶ روز شنبه برای حضور مردم در مراسم وداع با رهبر شهید بازگشایی خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/445114" target="_blank">📅 13:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445113">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی انگلیس: گزارشی دربارهٔ وقوع یک حادثه در تنگهٔ هرمز دریافت کرده‌ایم که براساس آن، یک نفت‌کش هدف حمله یک پرتابه قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/445113" target="_blank">📅 13:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445112">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی در پاسخ به این تجاوز نقاط استقرار ارتش تروریستی آمریکا در منطقه را مورد اصابت قرار داد.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/445112" target="_blank">📅 13:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445111">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آزمون‌های امروز و فردای دانشگاه علمی کاربردی لغو شد
🔹
رئیس دانشگاه علمی-کاربردی: در پی اختلال در سامانهٔ ویونا و برای اطمینان کامل از امنیت و سلامت بستر آزمون، برگزاری امتحاناتِ مبتنی بر این سامانه به‌مدت ۲ روز به‌تعویق افتاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/445111" target="_blank">📅 12:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445110">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc1418eeae.mp4?token=e9E_eR1FrHuxCStai6qBDpXbUXDxGu95PVzy6P8eiE5jUHmxv5PfxstRgZWWUZnZlFdyRpsG6y6D2lDb9Pfe5-1HLqeuRcWl-F2reEuYJPj5lPOd1ADV_uKGPTrEj-y04Dl7OqwKiTCeGdb1PRXaL7sHpShHfnZmuw58cJNFu-zbU5CN9YUmJ3mFeCAUcMkFr8kjYCBMnN0qqu2DSA8NElY9TryZ1avJUJtDkj_j51kPzDjHlaKLsIsvv6oVxtWz3tg-vNPSZBJQBCoNmEhI4FV6-gQOLdkjZ7twsMOpsSSEOb70-hpaEaFQ3OVqRJZNoO4dvkDO17ivDc7Zyu0Enw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc1418eeae.mp4?token=e9E_eR1FrHuxCStai6qBDpXbUXDxGu95PVzy6P8eiE5jUHmxv5PfxstRgZWWUZnZlFdyRpsG6y6D2lDb9Pfe5-1HLqeuRcWl-F2reEuYJPj5lPOd1ADV_uKGPTrEj-y04Dl7OqwKiTCeGdb1PRXaL7sHpShHfnZmuw58cJNFu-zbU5CN9YUmJ3mFeCAUcMkFr8kjYCBMnN0qqu2DSA8NElY9TryZ1avJUJtDkj_j51kPzDjHlaKLsIsvv6oVxtWz3tg-vNPSZBJQBCoNmEhI4FV6-gQOLdkjZ7twsMOpsSSEOb70-hpaEaFQ3OVqRJZNoO4dvkDO17ivDc7Zyu0Enw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احتمال وقوع سیلاب و بارش‌های شدید در ۹ استان کشور
🔹
سازمان مدیریت بحران: استان‌های آذربایجان‌غربی، آذربایجان‌شرقی، اردبیل، گیلان، مازندران، گلستان، سیستان‌وبلوچستان، کرمان و هرمزگان در معرض بارش‌های شدید و خطر سیلاب قرار دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/445110" target="_blank">📅 12:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445109">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i339ZDwxFi0geEgHNvgym9XNKC03_cDr-StVlrSfX2GRA94NUwEbXR_ZT8AgVDSgBX_q5CqKa-fqHuJNxaxiCM_HDCc2XhzRHMNH3UDiDf9sDYu64cRUFxC1w64VUXRzJ9fvfE5Cq-qAcDNxT5xPm9drlYNoQI1c7ypxHclErVKwOGunvOV9uJU1-rZx1Ttv9g8EkMM5Sh-fa0bp6zyVE6TRFpdRwPQKTDjVYMwJ_kU3nP51J7jGBpXD5nFkATVEuOvggxVsfcZ95ETWqI9mpeDwRxUtDjQZN79crxpzoGh8wU1irQFZv3x3mRKJJVpPoyJH2SrSHzXi354x4aWyIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با رشد ۱۵ هزار واحدی به ۵ میلیون و ۱۷۶ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/445109" target="_blank">📅 12:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445108">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37d94bea0d.mp4?token=Qt86pX_ThKlDUQTkOr5ac2_Sh317BFd-4AVpoyP87b3CE6L-OerZqya9D_2j5jxa4Mutv0KvT1s2S8_emMn2CbRyJl2DM9OWWmB-XXudVrGSywcYB-SnPIQfOjmsvoeEanoM0m3Gaclu8EaZUlW0KjEDhuKlIY0IY8b1vjKAkIgnv7NwC0E0JPxNW4IUQOZD5r95WQbu1EPPc7bo4SWb1jzo5jVtaZbdczQBzOY0b63xldwb3_RyaKmQF0ZlfPawTTgDEHOTVu9BnaKan3l3mkugsYR7kjO7IRoceUua4uPqUhOFnebXolf8Mk8DRq0H-0z8LRN3UICwFjrNerZ6IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37d94bea0d.mp4?token=Qt86pX_ThKlDUQTkOr5ac2_Sh317BFd-4AVpoyP87b3CE6L-OerZqya9D_2j5jxa4Mutv0KvT1s2S8_emMn2CbRyJl2DM9OWWmB-XXudVrGSywcYB-SnPIQfOjmsvoeEanoM0m3Gaclu8EaZUlW0KjEDhuKlIY0IY8b1vjKAkIgnv7NwC0E0JPxNW4IUQOZD5r95WQbu1EPPc7bo4SWb1jzo5jVtaZbdczQBzOY0b63xldwb3_RyaKmQF0ZlfPawTTgDEHOTVu9BnaKan3l3mkugsYR7kjO7IRoceUua4uPqUhOFnebXolf8Mk8DRq0H-0z8LRN3UICwFjrNerZ6IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا امروز همه سحرخیز بودند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445108" target="_blank">📅 12:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445107">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: به‌دلیل انجام انفجارهای کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴، احتمال شنیدن صدای ناشی از این انفجارها وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/445107" target="_blank">📅 12:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445106">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حکم بدوی اخراج دانشجوی دانشگاه امیرکبیر به‌دلیل اهانت به پرچم ایران صادر شد
🔹
در پی بررسی پرونده دانشجویان متخلف در تجمعات غیرقانونی دانشگاه امیرکبیر، کمیتهٔ انضباطی این دانشگاه در حکمی بدوی حکم اخراج یکی از دانشجویان را به‌دلیل اهانت به پرچم جمهوری اسلامی ایران از دانشگاه صادر کرد.
🔹
انجمن اسلامی دانشگاه امیرکبیر پیش‌تر در پیامی اعلام کرده بود که «دست‌کم ۶ نفر در ماجرای آتش‌زدن پرچم ایران در اسفند نقش داشته‌اند». براساس اطلاعات به‌دست‌آمده، بررسی پرونده سایر افراد در جلسات آتی کمیتهٔ انضباطی ادامه خواهد یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/445106" target="_blank">📅 11:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445105">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cviSMuJe2hJkpekq5wNscOD2UvJSw00NVQoEssXHXQ5IUiwEMCbI_q3gmV3-WXQzmA-6PmLjagXZhOvfkbwf5o_W67zmbjQSHatDg54Pu8lZuNkefb7iOuLIpKCATJVYMuzE1toFiT24MvkGfzjlpVBfmTdy4dZV7sK8pUt5AqrAfvwwKKWx8DnJtzqPkWVKTU7zL_-Yph4NFfj-WLeGo-_iO8hznVO1NBDj4a1pIrryRJ6J91fbaslJdVpabflrsHFeCFWuB18MkxIPm7z01NL-51XnR17RazHasipZrzRwQBvVlj0LSyX1GCPPazFe5V_-mZ1alTTRhI-Dw0FKEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رایگان بودن مترو و اتوبوس در تهران تا ۱۹ تیر تمدید شد
🔹
با تصویب اعضای شورای شهر تهران مترو و اتوبوس تا پایان مراسم تشییع رهبر شهید انقلاب ۱۹ تیر رایگان باقی ماند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/445105" target="_blank">📅 11:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445104">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsgIN_3Od6VdcH5ewgHgg9d5MycIDIBHvaEhDPtrUK9JrQ_oChQ4foVC-e_JZ_om3xkfJ--tJoh8a6yuW0BtiVdXQqOWM6TfXBn-MLDMcKSuSJLmUpvs0tee2-uw3_mpi_mbC2-Ltm7nGucDhVQEDyZgO9CM9s07Xw1eOQ3EQHsroUyiM6tKw77UQnLBaeBvW-6I0B17smabNy1wfYNohulpNbzW79w8do75yhhf35ctVu-CCIlEtngGAUpBdF6k4eSps9hTCUGskU0QfZKziNityYNnSUnxYWebREuO_doK8TBpX7hKWpnBaD0boUkGAti3wIvZLoGhJ4nkW793fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پاسخ نیروی دریایی سپاه به تجاوز و عهدشکنی آمریکا
🔹
سپاه پاسداران: به‌دنبال نقض آتش‌بس رژیم صهیونیستی در جنوب لبنان، ساعاتی پیش رژیم پیمان‌شکن آمریکا نیز مانند همیشه دست به نقض تعهدات خود زد و به بهانۀ ممانعت از تردد یک کشتی متخلف از مسیر غیرمجاز در تنگۀ…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/445104" target="_blank">📅 11:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445103">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ph_UZlVRcGCxa6U269kLe-LgUL8ugK5uKtquW6bn-pikFYKoEtCMSwKg2oH7JZ1GVcA8O5jWaEXonjntU1eqYJxnLDkfg3aW1WRmJdvM10wK5os0NCGIkCL6iHXody4ilBba3dLS_81ogGKKYSRpdE9yyac4_6PnhwyfEVFyzdSvQknF_xBDf1xBAwQb2aMqCxEmYov1A5DVj-EZTa4ayo4xYmKgb1lDfBGCjFtUoJAzcj6ovbWmmZHlhcXukbo5uXD5GRIRVFfo5ZiXgWsjqlJFB1i3v4OqwrN0pcV-p7phUYR57wCm0bV_9pduMUT3E4AQcRLQEw4HQ0zQ4gxmQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو هیئت‌رئیسۀ مجلس: صحن به زودی بازگشایی می‌شود
🔹
سلیمی، نمایندۀ تهران: با توجه به تغییر شرایط، آن دلیل ابتدایی که موجب می‌شد صحن تعطیل باشد، دیگر منتفی شده و ان‌شاءالله به زودی شاهد بازگشایی صحن خواهیم بود. @Farsna - Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445103" target="_blank">📅 11:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445102">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1wKbI_hT5l21WIb-0PbORVynqktrXmYv4BX6vZaS2yu3J9QRBT0gMhRT8i49s4Tqx45Vjq_mnSeqDFwo9xjLue1NTxtMQ_sNUi0z6F-aeiPTLfq6ZTKPNk_4ohW_mWkiUkj8gezgd8kFVoLbhElhfq4LJPNU09AE6dWNrjPQvBRl-YBuB1xXckOaKjuQirq7lhbfY6NPBm4PH8F_Ex-VwoSM_fi4zBePOBkOl2aUqr1rGtOxQC07_J-6KLHFlGouD_E14NUArWtyQLRcRLO8s0GeFo99atO6Rh36fLUXkMu7DxBxmcMZKY-dgFA4oRwwGdrgWj9V7hUF1jylQGfVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهداری کرمانشاه: از ابتدای ماه محرم ۲۱ هزار و ۶۷۱ زائر از پایانهٔ مرزی خسروی تردد داشته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/445102" target="_blank">📅 11:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445100">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fL4F4mwdq2gmiak-hmIO9R1uxww3pbqhhfRAUVPmIFb6ymfJKeaRESIPEpm2fW97APaUC5SLAmgxggJm6OiOsDAf7BWSdwyh2Otan66viwg2iDZ885LzcTNPk34sX_gLNmK_f-JzVZTQum8j1X2gs_Puk-wVMzjOB7iTD1StkZoUKlaOwAaquVd50sZmH6s_NgRyDsSD0jpq2qVy-66MXwY40aEFPMdzNblgf20JrSpfDbXxAgX4-mPgpYFV_oh0kPduViA8c7zlOqOVYR4bOjq_YO0xmcdY_n827TESqk7YUZW9xVvy6Mv-w4PWbgSs54Lr76N51WWWiXDvnynYkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lLOC_l0WkL1_5kn-yIFLg-IvKvynuzxSiSOjHSpl4yN1msv2mwm5rmE6IPBouXtAKdBhVwtMlBuILc--YTrlWrqhpbfdk9lNB910dCuRMg-84GyBiQyK_sNXNFtY265PamT8Gbpxh2oN77Sm0_l9X_tilWG5DDJNYhvCFDrsBxet1JBu8qYIbxYrB5m7azcoUnI1_XepTxUagOV7W2P_A5ebyrhwJmyXQuQtE3tJyG0bmHF3s3u-YrGb-Q-ZYN8bdOuFXhBXwG7JejxsMZDpiES-F7yfYSr_ulRHs_v64Pxar19BkDSUkAkhsH2EHFgBjZt-_JFBq_AzcQsQoTx6qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
پرچم یازینب(س) در ورزشگاه سیاتل  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/445100" target="_blank">📅 10:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445099">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZ1DyR2HgkfjEigw40xYwSdwpc_fRlP7Tcu4TEu5HlYMGMOZGUnta6xVWuC5L7j1z_cCLxIjBqLnaJEiz_VuZWG_mlfV9md3hR3SpPEzcmR-eWw3XWbLsf4ybVjXZ6p6pTQc8iWaB5s73fXXMk5zELknHWPZ86r02sHtr3WrB-z6j6QwYD8jrhswsUY-Dz5OIabSiLk0u8LuFbwkR1wZVJ44JpDrL1aW3VlXKRYuqVMz5ZSKQ-15BGPL18fsWaeVwN7Nz2i0q-fCqSAnvoAsw4EljBsjCcpq9YAZhn7RlsUGSfD7_YTu1qO86bSFFA2E3acw1ELtcIplZMc9Abd1SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز آمار: تورم نقطه‌به‌نقطهٔ خانوارهای کشور از خرداد پارسال تا خرداد امسال ۸۸.۶ درصد بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/445099" target="_blank">📅 10:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445098">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=AVX4CiyYjBaHIr9N8GGEoUmEDo1CBJxJxks7ThAJzaCZTWLSlXxuLaeE0J6i7BIl0LUkjqCmg-hVXAJ8iPskOjE87Zku2xtaE4IjkE4QprZ-6vE1zhAvbv8csGfFx1-x5tP1oECKskr73fM74raBhq0Nvqy9JnItA4HB2Pqec_RfuBkany3IVuXzF2NnfEbwLCocc-UjP85di_jL0TnyiX0YIXg5HzWyCx6aqksXGMMJOdz1ZjMf2jx8ZbpMQc3zbNe8bIkdQ4Nxzh6c26h45u39y3f4VEUp8wJpVGifLL47yeb7AEekhblcx0dZKaV9BSVl8jn5JSnxRNbkTImeTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=AVX4CiyYjBaHIr9N8GGEoUmEDo1CBJxJxks7ThAJzaCZTWLSlXxuLaeE0J6i7BIl0LUkjqCmg-hVXAJ8iPskOjE87Zku2xtaE4IjkE4QprZ-6vE1zhAvbv8csGfFx1-x5tP1oECKskr73fM74raBhq0Nvqy9JnItA4HB2Pqec_RfuBkany3IVuXzF2NnfEbwLCocc-UjP85di_jL0TnyiX0YIXg5HzWyCx6aqksXGMMJOdz1ZjMf2jx8ZbpMQc3zbNe8bIkdQ4Nxzh6c26h45u39y3f4VEUp8wJpVGifLL47yeb7AEekhblcx0dZKaV9BSVl8jn5JSnxRNbkTImeTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شمار کشته‌های زلزلهٔ ونزوئلا از ۹۰۰ نفر گذشت و ۵۰ هزار نفر همچنان مفقودند
🔹
عملیات جست‌وجو و امداد در ونزوئلا چند روز پس‌از وقوع ۲ زمین‌لرزهٔ ویرانگر همچنان ادامه دارد و کمبود امکانات و تجهیزات سنگین، جان صدها گرفتار زیر آوار و هزاران مفقودشده را تهدید می‌کند.…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/445098" target="_blank">📅 10:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445097">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a605d47d03.mp4?token=nyQN6aqIeJuBcT_8LBCjPl_Ku4uLh6HfMWwYHIDCTMEQWtKNofwp8oRBSaS6nxE4-ZpZf_WLVq6dj9viieYTFwNFQ00KvwQCk56vjlKoC83fLVpEKCrULFfka_HSI41I0FSrqNMtvV79h86p2Q0Zd6ww8uoS5ZvmftUykhp87uATkBpTm40epOIPKGDljBHK3cytZkx9IK2axvLeSLl6SsH_n7RgyDZL8f4Nc3CFEPIxiTfyOWrfINpigiMPvcTFQnYChzVMfwPadzXai1Vq-LrOKCZdC4jI0a5xO3qlcXCHV5RTGPrb-Iot5KdR50nKDtpb8gfXtosJuEdxZerQew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a605d47d03.mp4?token=nyQN6aqIeJuBcT_8LBCjPl_Ku4uLh6HfMWwYHIDCTMEQWtKNofwp8oRBSaS6nxE4-ZpZf_WLVq6dj9viieYTFwNFQ00KvwQCk56vjlKoC83fLVpEKCrULFfka_HSI41I0FSrqNMtvV79h86p2Q0Zd6ww8uoS5ZvmftUykhp87uATkBpTm40epOIPKGDljBHK3cytZkx9IK2axvLeSLl6SsH_n7RgyDZL8f4Nc3CFEPIxiTfyOWrfINpigiMPvcTFQnYChzVMfwPadzXai1Vq-LrOKCZdC4jI0a5xO3qlcXCHV5RTGPrb-Iot5KdR50nKDtpb8gfXtosJuEdxZerQew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای در منزل شهید لاریجانی: کسی غیر از خدا نمی‌توانست مزد تلاش‌ها و رنج‌های ایشان را بدهد؛ شهید لاریجانی سرمایه‌ای بود که یک ایران او را از دست داد.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/445097" target="_blank">📅 10:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445093">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzrJvw8M7rIFj0krRK59uHqrhtU8U0NWAqseAz8swfPW-AGoBCIpQHlayxuWgCgfcryNBqW-_2q89ply4ki97TUAo3ecHzE-gBbSFY8QitfpdQYFAj-P8V6QyQUWC8hXnQv7mkbHOxyWJsyXjq8JbYgtXlfg3r6kYkO8nIMvjS9gEwZqb7PvRDRwxJAMkT7gmqwhCrkpheJRxM-Ium_fRhUZSzlhXHGQ-PZuBrZGkMANPQxHjd-fd8PBEnwsDzyJsNvkMnhfi0r17CyqvXKt3p1Z1lu5XaQgcPAXwRM4ycucRz2LFoJ1ASnR830h0vkTdj8-H6ry7ln7IWXIQwtFpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cFJRR3SAkPREkGK2q1bg5GEZnBEFfBejpXhkg3oLw2b0bLbfxogn117b8x-jV94XXIRKtUJUxtRgK1_MPfZr4ZFka1RCUut678bJWxRpw2_qCj_2skHnhUJlPAZrXYUYvq6TFM9hv1J5j0JsRV65gVkEtuhqt_A6tqnNflnOITNoARrBQ-fcmBB6ufVBNNkeB8U8MgDxFQwhBhYVkRbPo6rLRT8MUObsZgGvnkYkhwbvPLvEch3_TtCxpmKDogTaBh8AG6V5FSteTRVtUsw2I7IXA5PqUfVKKJWnf0kautLV-NX8BptuGbC314fQSMPIxDMfoKRvMsD6x7HjaGJNDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jN2JFUhh2A9Cmyn-hkQF_Zx8rmz-9EbfuVmYOeSi9t4sRlsimH2MKh6-sr1RM_XUoEw5hv8opn-cSkou5CqN0uwgspL7nJxz6ct6prdg4Xj4DgRDTs7IAyjOTHhByZrbs6t3QcMfhJXCL2J7Gp8aZ0zJX7b6WHCM0ioJuDJ3SrGFHDzbaIsvZ6ibuOroyu1KugOOam3ZRUEaQ8vw9OKZ_dU9v5WEi_aPt1aBz-1MtcQMpyc79hhPXPljIInmvhGHdp7CqbDgW91xlTgy4HjxtOdRbvZHDwE5r45ZOfcrddPfc59vxNpZ9zTU1bLYQ-Bl4eBFySIVs89k1QnDhFKTYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V04nykkLsjvlQa6dV02NvfYEuQiHRxHSAAsnnFhu7UFkKsGgpB24RnWkOQqVTtJ6SdLk_wOXQOPdtD-1an7izn2eKqNvakdKs8STHJZDqqnCq7CExe6nGkf3O34hfz-xTj7YUa2chRXo5p_gcP44qCeJkLdRyJG-QMHqZ7a_rJNRRSQuB6rB96zD7GOKH5mKIhzkkCJZTEduYoD-uq2j48CTvSbyL_GaFKUp7N2ImTaaY-2nRchDT_AOTajBcJ4PXHVfQ_jcxqJoCSuo6BXhJTIKOKZ-I7O0UROHjF5mbRrv6u9GmPE6TpiWS1VdI0BMZOJ2Dl2S92ugfnjuQJbnKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌
🔴
تلفات زلزله‌های ونزوئلا به ۵۹۸ نفر رسید
🔹
دلسی رودریگز، رئیس‌جمهور موقت اعلام کرد که درپی وقوع ۲ زمین‌لرزه پیاپی در این کشور، دست‌کم ۵۸۹ نفر جان باخته و ۲ هزار و ۹۸۰ نفر دیگر زخمی شده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/445093" target="_blank">📅 10:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445086">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uo8flduF0ntuaXeiyP4LjbIzLMHl1McM-zfu3MqZsIzn54nm2cfmtei7_ONai5LBN1Cx6y7UBcIzL898oiM9u8lBSv0R_ceUj3_xD_k5Ait2mepEVCaKeSBqcQoVSGaFHwUyr5G81l8jbobdKR9jt7rAeVKj4uOVIeP1J0MyoHnJTQkY5_HPrV4P9HClryUvy-adI4EjiPPYVMzRDu_QwqIgd_CYFmQziypeFIQHKzJ4pVETGQnBPfv-raJMxDCT8zuti2S8ZmTP6j7SO34xreAv-yVj4gXlzhzreAA0VkCfW4qNU3qPSCusAsI_2eiRfPzAOSPyMMHGfqACsL9_QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMGugm50WshpBlH8aBdlHSDMsO6eFsR1buG43qGkwldO44wve78eIYGTbeokM8HpmtfIWDS-j-88h5foTTJvpRqzDVOY9UGQHULl6f9yID8Rgge8-vGvoMLODG8X0TuKAW8hNc3ejL7JstntFnF9v8Az5ptt5xqFbEI0dQ3sX9AIpKLTtRqvs5axLrPdNa2zzWteDsq3t9sUwDtOBKXVH3Z2q1hGy2vbF8WV0yJaIR7pzrCPb-LLJfUF49VEHPegFrF9qX4hxGKOjvcFRnFD9D9ch6_tjJ7aIwTw3yybyFjAC9AxtuLvWj6_1pXx9RQZdDZTfTxUZfeo9tgn_Z-n5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AalIDxm9iRjJKJflfzLSkIEk8j7aZjQulU8hP_8viLdSO5-T81KMJgDC_gFjMdMLHFBGW59LFFfTB77jyBt25jz1wkTT23sQMh-sHEMjQ-N3twodDhu0sdprGWSj3na9euI5o1sOeaFxdqXwkpxMpZ37LOkyX3ii96AGqpzQCYcYU4x0Sr2mA_ZZQvm0XF9SsLkQf_0Jt_8KY4K3spf32CKIiiAdwXo0LSG3p-svmLUYlQ-V9PgDEPJsQj_y2BBcUpT33DkpS2VtxsZTXjDi3Y8d80W3f4bXQs8Zji8O3cDqwueDeup4l-Qpecewt0Crbh23T5dZUmFW5ZaldhPVrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DQ-qV5-kMJIAkWTNmNKaKNmQvquBu4--4EUQUk_ldlEjncDfi76i-H9gPCXLdFY62fAl98uUlV4sa_erM57gUX6z7X_gjTQaajB0MoN0W4-ZA7Wr47RD_NanZdm7J6SgyBuOajwOKVl-KKQx27gy_Y_WiqRAxKafplhUndsNTVS-cIFXpCI_9p82a7x7jSW0xXqvNUYP_94EUw-MeLbIZAACsuX8KHDeHO881qFtG9kROynpQ2w7BVX3Zv26RRvSDGw6KvevFEN7Vn5kO7qwWYKwrvNbZ_ivApX1IA3mvPk3Ub5Dn1pVd5qC5bKRlyNLA_SGY97Ewnyg4kreM80T1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WOieb67SSDzT1i7ZeeUarnCwa4u_5uwWeqwDSaJAnrMlDgr69iOs9BwbPQW5-5QC5vsXs3xfsrTyR1ynACB00ZQ2Zhr_sy34K0IIcQFUcOamqUGH-Oj0KHEdx33ddIHrtpBDTID3iWM6qjHyBV3Xl077RrM60_3-hLt1C7iNhkf8ijMXeNR6mEAEOOer0S_5zLYBbBSqLAAOxCPVMV1Yk4hTdBvTI1gTQoFB2kwchaY59t03zDsUcZjJ_HkHlWvmBE6jpo-P8gYN0YyiSZGW0FC5_QZCJR5b1QBdFY1ZO3WDastagsaOQdHZyFRHbePugXipDWaBwAxHKSFZqbjYug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g7oEBCzpLgrkctbfel_-sp7q7_f7LDRi9i_wN7RlAW1srWM1DYyY3baYvmfazqYhNE1-o20zgXDAmF0zm1ItIMzvool1lG6kZ2GZ3aawyDr-EkLYDbClEM7lF6QZJun3EWFE1sTIZzijKxUzw4dhWCKEG19J8RRMNZHWjU6uQkjphBcd_BMbkNsfcN27NoCyMDcElxHxHad1u4XBUej1o6Tcny3OKeA70gJ-E3T-Ft3xtx0xg5rIT1601Xg5QWFyoZhgIiQH3v5GFuvZAMTuQxHAaKnCv0QhglDRwFVLliYs6zJNlLbj-_lts_K_sa9pKGy9m6EqfqbNojXaQB79SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nM7kqK3v0bxw1Q2jUDu_dZ61_laIkW6iihuyhEzV-CTXTODgQEhE3cT2UHgocggzoVKoWafGT3meKKBLCPhx3gKKp3dH-k0DG9mncnK200NIuiQemAmxMsyuNXc9dD0Rp8tbf4vBdcrSyHXXxEIxl_Jgng5bK8h_f1e59EzuJZodmQJqMKJPor0oZRGsFCBfQuPjSva6uGQ6q_wKilUcB8biCzkNe5IasipFzqxFIY7AtGs6FRsxa7ZJZjnlvmjIEloEAYovhUSA7RpmbdJGXpXDWrTI73vhB0Dbp6Lp_wFXrHEJE_1W-7gPJvSbKL8L15Kko5jVXuj98A1g4WV_zA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تماشای بازی ایران - مصر؛ از نانوایی تا کله‌پزی
🔸
همزمان با دیدار تیم‌های ملی فوتبال ایران و مصر، مردم در نقاط مختلف شهر از جمله نانوایی، کله‌پزی، املت‌فروشی، سوپرمارکت، ایستگاه راه‌آهن و ایستگاه‌های تاکسی، با تماشای این مسابقه از طریق تلویزیون و تلفن همراه، بازی تیم ملی را دنبال کردند.
عکس:
محمد‌مهدی دهقانی
@farsimages</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/445086" target="_blank">📅 10:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445085">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ugjd-Qs4t-m6LxOmSLC46RIyGgxXQlOt_C4u0SUA1Ej711sjPVsfzAX44LhXyoAWGLyJkawsFT9hOVeFMiIpw3GHvwn9JmNQKX0zsuJHO5zVXIqENTIPZKt5JOawwOLM-Al7dFNBijvNK9_pITtliQ_sylEw2OBvHnQIbKRrR_NTUwRQ4tQPuajNFWqml_GYlxeKdNTYdPNdNTy8rZu5T8NQhtEdtkwrcS6nU-VRg5qbXgY9gLXIMeoGriSKkcvqJ6zgYURKrILo1mkO0wI2-sOjO4HTfMs5JwE--VhBrTRXmcSOCztQu4qXUeOSBdqc2HsPkAJzYyCdP1JeakXcWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی ایران و بلژیک رکورد مصرف اینترنت کشور را شکست
🔹
براساس آمار شرکت ارتباطات زیرساخت، همزمان با برگزاری دیدار ایران و بلژیک در جام جهانی پیک مصرف اینترنت کشور به ۷.۵۶ ترابیت بر ثانیه رسید که نسبت به سقف ۵.۵ ترابیتی هفته‌های گذشته، افزایش ۳۷.۵ درصدی را نشان…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/445085" target="_blank">📅 10:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445080">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sgJxHI_3ptXXedCq9LE7FSdTOvSJ_ZOarasUJaX-QXIdE_qbzqkHVsjvzGQd6MvggdR3BBv4SpDlw_XBuVqdNszDrZQyaffW1oT4L0V8OO0lh95aIHCok7vYGQUmKekLiCHLkO1KIhsCCVATEudETiI9Qio_ut69TBefW2yrRI51RKPK1isUFQ6h0bMw2bxipgXSEm22u99BCDTnXgGo77z9zcWGsaJdboYpeFWvjQTQ36AraTC2chJYzgSbwi2wsBraYCQWCtI-GOE475qQ7NpdWtlzeaxX7RtR-JXYPSKbksP-SGOXyKiKD7an9J_im75AN8XLd8-ufGap937RiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dMhe6FYtidjIsb4F1XIXFW2f2D9SldLCiF0fdv-3kaTaerbTdv6VUNy7JHfVyGZZQremxh9qH2EBlvaElmp_I_4dj-9VKhWRoZwXwO1BFhb_S0NHXooCO8smrQBMxr54QF9hr_YrT_6gwop-OUH0J_dyhNxjEIsqWoxzXB0Vj9dnDSrgi7I25xyR4mJV66_ImCmgh3FcmUY2gbjk6yge84SIR_0AQKINbB5WuMBYSuwHOxly3VtOZyxX2lmNFyB1vE7HAbRnMonKXBPG506UIyaICKV3js8CouCJAWh4jyXDi3dlbItnF98Qxif2N2QP0KibBIE6ne4GfzAKy2mbDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jWtof20HhLYZ1A4GzYxUX9ZTvnKVYCHqvC8fQnRvTvA9d0hyM8eX_dE_EVlqeThgDU2suLuq4VXOd-R85UsMpSFTGE-n2XgVd-rOTjsmexsZKFN-40QeKKlGqfKrVR0j3_tx6IndocZj-V0-qdRGB7BdmDX6c1-bU02_1mFtpKeKkfI5NLACKkU2edmWZZLnrO0uxZpGfP-rOiMCzO0_JtjteHpexh9DRdYlqYlT52-r-F3FwjKXhfGMGMezjyVh0FTjg_xwJkyQZXcAz4zBBQhpteh1rxX1OU5eGgcbmOKkm44vxZEI4-jNrG7DV3GQuBwBU8PvGyOnOkc4ZI9A6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5e12dSTz7jkQQD2p9Q9BQIhcTToam_AtZTtpJAvVrttSR-WiZ10J0-Zj7cvzofaJIx2oCBcjM1s_1xdPyIpDuS1pdBNlvCs7ZHE3CQgTAjeKi02CeyB6v96n7QNcNkAaV9yL1ibOHcLyjKs2dzqRZNvaxTy6Dpn5ggyGXOA_Yb5gtCFQU7MN8t1fdJNTsyB78UD-uPe3olAkk6vfManufSoG1Xz2j3-N3jihDgSwv8343BHgJ52jhtJIdDh45EOruT7irXZZ52iaMW07IX0jTGrZNlAE7LTymR1YacGoaO5FthMX7rQ3AY-Z35O_wZ8yYJ_uwWZJNqVFiTYp-Lq3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OaQMzHi-CZnr2koGL1hXKu4_52u2pDU0f1fZ_R-0iyoUcSMYIigN6KGmg900NK-R0auNemx03u49lLQjn2RKPdFCRKZ3ztYdp1VLvDtySpRBXXN-oPy9PZWY8bN9XiZ8PueB-sHK02VhAL3iP3efiJctkOxipJ8gZ_V3INhFwc2Q8ZRBPdxbIlRDE1yP_e19ZGzOtKGRT6PnpJRE9GFlyMf_K0Z26ciVu-SpOk9iCGLtKqASgkf0vpXZWSgsCsR74HXduy3zWzvdHbqxxwi94U-b5IjCDItn-dr6Gk44I6ftxuV-BS-4n-wyJ-l8yGRvCb-iwQA3kMpGv4x3aA8QvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
همدانی‌ها در هر شرایطی پیگیر بازی تیم ملی بودند
عکس:
امیرحسین ترکمن
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/445080" target="_blank">📅 09:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445079">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLumd1sBDbmG_k4xaoPRRjmk0iFBaHvdwISd7RY1Y4CruQASN-ilvCz5aWog_ybn-NQ-Qtg3eaFdFvGNU7_VFnkriC-q2kW0z7finc_Zt8qA9Xg6tfvXq9-YAIfsGlipSziTECLq2vjH05E58gZ4cuWfPCHaHewwDWL6ja3UrPXYUZVyJTulsmnR1NOvz8JezlvyIWy_FQRjGwYA2l4U7j15Q-yaiD-7o4mAFv07rnDeOL3vgGSQNEhD0TuedzOwnXmuITv3q6fPe6VrwHTnON60-f2o4DQogmS_os2Yi_rR_J95eeosPPtg-1db7uRWPSf6ihu4fsYK_IEJEE4Gaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شانس ۹۲ درصدی ایران برای صعود
🕯
برآورد سایت اتلتیک از احتمال صعود ایران
@Sportfars</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/445079" target="_blank">📅 09:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445078">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c970fb9dfc.mp4?token=kkEnv1OA0QQftSxYdqkED2KQMWmsbanXR_wVHZUtSZOUW34rDcPy0Bg3yrfbLYiRiF8fOT0F5M1uFkv2Rag_x6SYjfXcOb6IWCMlR6UECaKNkZey60TIGzDY_iMcUPCfW3Os_6yLndtGcdfRAdXhF2VVKKKhapETO8KBBHdcUr7NqKwRClGbGlreylKmSS_Y2sYMjY49kD5qNLgkjYq1Qc2wmT1qkjYmEy07HiScl4e1fI39ds4vrhIk-aaQ3yoIZjgZ_NWkQhRN0obucwZIyIKDiinF7jEGJq__cIGwJe5SOu27Z-H5-x7SqFpSZJ97o366wT5CKYPdbOy_x3hu7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c970fb9dfc.mp4?token=kkEnv1OA0QQftSxYdqkED2KQMWmsbanXR_wVHZUtSZOUW34rDcPy0Bg3yrfbLYiRiF8fOT0F5M1uFkv2Rag_x6SYjfXcOb6IWCMlR6UECaKNkZey60TIGzDY_iMcUPCfW3Os_6yLndtGcdfRAdXhF2VVKKKhapETO8KBBHdcUr7NqKwRClGbGlreylKmSS_Y2sYMjY49kD5qNLgkjYq1Qc2wmT1qkjYmEy07HiScl4e1fI39ds4vrhIk-aaQ3yoIZjgZ_NWkQhRN0obucwZIyIKDiinF7jEGJq__cIGwJe5SOu27Z-H5-x7SqFpSZJ97o366wT5CKYPdbOy_x3hu7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رامین رضائیان: من نمی‌دانم چرا اینقدر بدشانیم؛ امیدوارم صعود کنیم تا حال مردم خوب شود‌
🔹
مردم ایران ما خیلی دوستتان داریم. ما را ببخشید. @Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/445078" target="_blank">📅 09:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445077">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c5a003f09.mp4?token=TjSPquCuHKIvyXZWi-QlJkZrwtjJy4oliEFtKGvHDYP6KGT1e_yi0bOHL-awS6W-4-VnG6V3XbpHT9VAs7wGVxHqa7vdJEonOKWREyGETuHRQR9RcyqBN2S6Gwlu9o-BTozQVLPtn1SkzIlASZPbREw4ekw2ucLVdAVJWTzrsE2KO7hWggvzEypO7Q0jFEHuudDfxgdqVM_p6o1NYW6a5TEGaWkgvIP92skvGq4HOOaHlmjtKgRrGUFcJOagbSJvejjMIwvonMlhsaNf13fGO_9Ip5d6OKI-r_FabDzGlOllnhhHjTqoknr_xA5x3tfJQ7UFem9xH79Q8V_N0LEPKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c5a003f09.mp4?token=TjSPquCuHKIvyXZWi-QlJkZrwtjJy4oliEFtKGvHDYP6KGT1e_yi0bOHL-awS6W-4-VnG6V3XbpHT9VAs7wGVxHqa7vdJEonOKWREyGETuHRQR9RcyqBN2S6Gwlu9o-BTozQVLPtn1SkzIlASZPbREw4ekw2ucLVdAVJWTzrsE2KO7hWggvzEypO7Q0jFEHuudDfxgdqVM_p6o1NYW6a5TEGaWkgvIP92skvGq4HOOaHlmjtKgRrGUFcJOagbSJvejjMIwvonMlhsaNf13fGO_9Ip5d6OKI-r_FabDzGlOllnhhHjTqoknr_xA5x3tfJQ7UFem9xH79Q8V_N0LEPKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رامین رضائیان: من نمی‌دانم چرا اینقدر بدشانیم؛ امیدوارم صعود کنیم تا حال مردم خوب شود‌
🔹
مردم ایران ما خیلی دوستتان داریم. ما را ببخشید.
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/445077" target="_blank">📅 08:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445076">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">📺
ایران با برآورده‌شدن یکی از این شروط بالا می‌رود:
🔸
بازی الجزایر-اتریش برنده داشته باشد.
🔹
غنا پیروز بازی با کرواسی باشد.
🔸
کنگو مقابل ازبکستان پیروز نشود.
@Sportfars</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/445076" target="_blank">📅 08:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445075">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef484074c4.mp4?token=QLnlxgycavV7-sNpT_QbLYwbY-3exDOtvmQXQR3vHdH5H0OoKvu57fnfyWNNAE4v_68WJfEGbZ3nRj4Blq2VYucnilewkVVaTCaYnReAPCyJ5wlgd5AvMzbOW1ZyGIu5l9m1h1iq2QTOmt8Vv6t2txGM7f6lnjuh3qW8EYAuZPqlPbu62vEnJRtqT_tIyeUFkTw5y6sqYIWDjWF5ytXcMM_9G4wZVuSGyIxyz5y2H7tWKlAakN1P2BfyhFIEDed3fILOyFJm1RJ6NS0m1UTQobFWJtg7ja_eUsKkizC5r5zNmZbalJJtICPv2KgcVNoXYjaBuaNPJW1BBad2Xd8ohA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef484074c4.mp4?token=QLnlxgycavV7-sNpT_QbLYwbY-3exDOtvmQXQR3vHdH5H0OoKvu57fnfyWNNAE4v_68WJfEGbZ3nRj4Blq2VYucnilewkVVaTCaYnReAPCyJ5wlgd5AvMzbOW1ZyGIu5l9m1h1iq2QTOmt8Vv6t2txGM7f6lnjuh3qW8EYAuZPqlPbu62vEnJRtqT_tIyeUFkTw5y6sqYIWDjWF5ytXcMM_9G4wZVuSGyIxyz5y2H7tWKlAakN1P2BfyhFIEDed3fILOyFJm1RJ6NS0m1UTQobFWJtg7ja_eUsKkizC5r5zNmZbalJJtICPv2KgcVNoXYjaBuaNPJW1BBad2Xd8ohA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افسوس قلعه‌نویی و بازیکنان تیم ملی بعد از پایان بازی  @Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/445075" target="_blank">📅 08:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445073">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMtQtS-sBAjsgT_Xhf-CfIT501mh3oWFrCASj_WD8X8FFRM-cQ1dqtBxrwwe8MrcVNbN-3z13NrGLyQQ-eKyxJrf8wg8gnWjFTQH0oBlNTZiopcICWsaAFAKno-etaUcyssEvS1cKnRPel8BwjrZLobOOaNYMKmaINdAUu-H_gnQAmLXqaukN9ZO2NfAz32wkWkjZP1HUlsLXhhKKeDfoY2s6gO8vX0Q98cZ9YXvrvVhZHgYL2qDExhm-tDjootZi1ihjILzJgOycJp88OFZ1JwuaH0r26SEXN1Q71zBb4lQ-N4zkMMoUtmm5oxx670JxVzsEZpO1H7qeDVKL_e23Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
جدول نهایی گروه G جام‌جهانی
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/445073" target="_blank">📅 08:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445072">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5eea9fb83.mp4?token=IZD3DMhV6fcRb9-SM7uS3HlQmatBAeZJ47GgWr0ieTV351TUiY15NxG41I-_W1fnOOHTchbrRc8FVEsxL4ow3bQk-GisJeybykrEv_tWDVJrY-0MNyGD-j8nzVq0259gzPukH5FK5HrX-PjzaKvBSyk4izVmNLmB2Xp1fqk1WWi6jnrvQ2EygPnPCVa4BZz4-tcz1Pj6_aIo56clFZVv4TdRw3wiu8Q-n7KZf1zuAUvmgvpidvo-OEl1BFn196OMPM-GWkpxLyYVCT-ycf3JBw04HYK167bvQonc2bthvqu8V5ArzRRo109KWGSe1noW2M0pO8tr0ll-6LVrGBNIyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5eea9fb83.mp4?token=IZD3DMhV6fcRb9-SM7uS3HlQmatBAeZJ47GgWr0ieTV351TUiY15NxG41I-_W1fnOOHTchbrRc8FVEsxL4ow3bQk-GisJeybykrEv_tWDVJrY-0MNyGD-j8nzVq0259gzPukH5FK5HrX-PjzaKvBSyk4izVmNLmB2Xp1fqk1WWi6jnrvQ2EygPnPCVa4BZz4-tcz1Pj6_aIo56clFZVv4TdRw3wiu8Q-n7KZf1zuAUvmgvpidvo-OEl1BFn196OMPM-GWkpxLyYVCT-ycf3JBw04HYK167bvQonc2bthvqu8V5ArzRRo109KWGSe1noW2M0pO8tr0ll-6LVrGBNIyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی مساوی تمام شد
⚽️
ایران ۱ - ۱ مصر @Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/445072" target="_blank">📅 08:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445071">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZKs347WWWHCFUfbQQwMV2sfqsiMVGMjwsrSyuSlY30RU2J_wak1SX5XwV4HRtrbMgS2bjFvinDK0ydNdSDkeku6cyczWxYXk5c5tbI4wWcSN2lW5-Z6DASyUm6UpHG5TBgadWwWYWSWVAaa3YaxSHRjkfm5nmQqySN5kwZRUWTpyR0MmHxHwCQcvAErLo_R5eynvZ-7QioPao-34RZUjb7t4siqq46PYhOt6FvCk90XcEwe1-5jaqLqJyXq3UmTsuKE6-r_8aqO66tj5I2jtbjn639sU5Ek09Ow0Tq_bgWSgN9GM--Le_ChwTqEeOmtpp_Ych1VwJVOMdh6Fpi5gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی مساوی تمام شد
⚽️
ایران ۱ - ۱ مصر
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/445071" target="_blank">📅 08:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445070">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4RZPxGrUUl-xSNqc5vXvxDYVTUhSRI6kYP6aw2NQ0WN-3f2hBMvhS-JKksR5TvMsLFywue-AZS-H5kkdqiZwxB78bLfU9oORATiSkObHeoy6l8APCEmDhPZKNuh7bNHv-PkV-mHgM-Nda1qH5DRZeEDN7muys2kpDb7UmyCU41vAAtbK-5X68kBcPFzepsTw_CYxR4jW0AXmw4KjO_5Nmpdg9wn6xZj1-NC8OHusHGRt0sO1FVTw4H1qoKb0XZaiqDSd_j7ea6IJ0PbJknlGRB_L9klSxtzKjnnEey4Aw0ur0fZjXCy3_z3F9ER_c2RCvC-Mq6lsuTbVIltLr2ANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امان از ۵ سانتی‌متر آفساید و تیرهای دروازه
@Sportfars</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/445070" target="_blank">📅 08:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445069">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1111467265.mp4?token=a8EnLXaJHVPWYjTn4GVkcpHzIghu-hx0nyrVE58d93SGnSUv3zohr4_pYYMCdB6BDj74tJxfNdiwDvB6D_Tpfn-drFg-vCp_Hwy7WSM636c5RHikwOVC9Jf2I74WlCMSvgMOaccealxudIOntjEMmu3oF1SEQMIoeQzCI_grLWZtt-GUf8CZ_YcHbsOxkm8zWTIndQWIqoc1xNhIn_yLkSwbSfneddCfppcWQGWUQWvbI8h2CgVb85TW6qveIbZsw0ZIv-fCQctVMYgkD7HDBCL72aMqadGWKwnBCWrsT27XN5qAxCn0PKIlRt5yonnC7zVssLbUJi2VL0X7Lwkjlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1111467265.mp4?token=a8EnLXaJHVPWYjTn4GVkcpHzIghu-hx0nyrVE58d93SGnSUv3zohr4_pYYMCdB6BDj74tJxfNdiwDvB6D_Tpfn-drFg-vCp_Hwy7WSM636c5RHikwOVC9Jf2I74WlCMSvgMOaccealxudIOntjEMmu3oF1SEQMIoeQzCI_grLWZtt-GUf8CZ_YcHbsOxkm8zWTIndQWIqoc1xNhIn_yLkSwbSfneddCfppcWQGWUQWvbI8h2CgVb85TW6qveIbZsw0ZIv-fCQctVMYgkD7HDBCL72aMqadGWKwnBCWrsT27XN5qAxCn0PKIlRt5yonnC7zVssLbUJi2VL0X7Lwkjlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل ایران به مصر  آفساید اعلام شد  @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/445069" target="_blank">📅 08:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445068">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a6be0c6ce.mp4?token=OYdCU5fS_rkTXjZVjrCpCk7OUNkxlTltiDg51Pwc74cuRLV2jp13mNzeP2ehh9cQOwhyOjSmyzX6XvTub0oOj8y5RJzQJqOD1BQX1x1Z3duYz1aSjRG4BclY1bV_8oKLXARrxLhOMOV30a-6DHrMW4QN-NaGwK2baNeHhz4GviSLNlO_6z3LaEaHmq6BI4xSU5xYIJNRsgKiRnuFcgiN7RsjJIcKt9sGPWofXKzLkXffNSqQBBw8dXKTjNkf82lfRHOMieo4KquN-_35kLglHqlXEl0hTboxKMtbuToXQ3Qh8vwAB7t1HmoZG7vqDyYko6Fmn3ng2_s-Dcrf9MdZmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a6be0c6ce.mp4?token=OYdCU5fS_rkTXjZVjrCpCk7OUNkxlTltiDg51Pwc74cuRLV2jp13mNzeP2ehh9cQOwhyOjSmyzX6XvTub0oOj8y5RJzQJqOD1BQX1x1Z3duYz1aSjRG4BclY1bV_8oKLXARrxLhOMOV30a-6DHrMW4QN-NaGwK2baNeHhz4GviSLNlO_6z3LaEaHmq6BI4xSU5xYIJNRsgKiRnuFcgiN7RsjJIcKt9sGPWofXKzLkXffNSqQBBw8dXKTjNkf82lfRHOMieo4KquN-_35kLglHqlXEl0hTboxKMtbuToXQ3Qh8vwAB7t1HmoZG7vqDyYko6Fmn3ng2_s-Dcrf9MdZmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربهٔ سر طارمی به تیر دروازهٔ مصر خورد  @Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/445068" target="_blank">📅 08:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445067">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/608fda927c.mp4?token=mTk9vtFnOTUCyH0of8-Lz4HVru7U6tef4GocmuE4PuSv2Itpm017y-OvwGCHqfwstjV_hrkZW4wB5fmrb72hTZZ9hdhaExUhBv1rxzeho_ZYCdzwVJShfA1_CMBoG-U-Y57GYgb55UX4G3DlEfd-PQUgooFL-lWLF9sbk1RBBGmh-EAVsS9u-WL0_Eyb4P_26ehsdhOo5CCm4QNdilhOdOkZEVLeCh7o2iILgKPqoi4g-LSrNm5WaT1BCDXHW9JK-JA0RR4fKMhb3ISrPy1jWietoUUzPG8NUF-O-Tr8v_Bb2WLhq3E_L8Q-m7YKKyYRnct80RDmrxlqHLFfJG2tjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/608fda927c.mp4?token=mTk9vtFnOTUCyH0of8-Lz4HVru7U6tef4GocmuE4PuSv2Itpm017y-OvwGCHqfwstjV_hrkZW4wB5fmrb72hTZZ9hdhaExUhBv1rxzeho_ZYCdzwVJShfA1_CMBoG-U-Y57GYgb55UX4G3DlEfd-PQUgooFL-lWLF9sbk1RBBGmh-EAVsS9u-WL0_Eyb4P_26ehsdhOo5CCm4QNdilhOdOkZEVLeCh7o2iILgKPqoi4g-LSrNm5WaT1BCDXHW9JK-JA0RR4fKMhb3ISrPy1jWietoUUzPG8NUF-O-Tr8v_Bb2WLhq3E_L8Q-m7YKKyYRnct80RDmrxlqHLFfJG2tjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شوت مصری‌ها به کرنر رفت  @Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/445067" target="_blank">📅 08:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445066">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/607ba533a6.mp4?token=YyObhuEjAPCh4GpVfLuCtJryM0XAA4VIStEGAfNzpGsVHEw3awHLjPY5W6vNjdgLoNF_bN2SIPlIn6WIr6nDfc7kACurwQj6hBsx6_l-MWCd6F7I-fuv4nE_idfgfUICM3YDNArY0h-Whz3zunbnO7dPx5TVPMKmemw9BBT4dPTSY9to1Q_L1NTSe8ZurihKsi_bv39r1EN2hMtdbi4-qr1TTItxFIFwx5fbvXZKJ1aQ9pdTCKE_IgFWjAR9Y9Se8BNz4qZqxyBO0cHUDwxgRmpxdLewuGuWsoKVLAG7yWtK0cdXW1aDk1RGrN5kO87Uk4-n3LAkTiMFU8NMwpixNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/607ba533a6.mp4?token=YyObhuEjAPCh4GpVfLuCtJryM0XAA4VIStEGAfNzpGsVHEw3awHLjPY5W6vNjdgLoNF_bN2SIPlIn6WIr6nDfc7kACurwQj6hBsx6_l-MWCd6F7I-fuv4nE_idfgfUICM3YDNArY0h-Whz3zunbnO7dPx5TVPMKmemw9BBT4dPTSY9to1Q_L1NTSe8ZurihKsi_bv39r1EN2hMtdbi4-qr1TTItxFIFwx5fbvXZKJ1aQ9pdTCKE_IgFWjAR9Y9Se8BNz4qZqxyBO0cHUDwxgRmpxdLewuGuWsoKVLAG7yWtK0cdXW1aDk1RGrN5kO87Uk4-n3LAkTiMFU8NMwpixNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تکل زیبای حردانی در دقیقۀ ۵۲ مانع از گلزنی ترزگه شد  @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/445066" target="_blank">📅 08:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445065">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
شهادت دو مأمور پلیس در حملۀ مسلحانه به ایست‌وبازرسی بانه
🔹
ساعتی پیش افرادی مسلح طی اقدامی تروریستی به ایست‌وبازرسی ورودی شهر بانه حملۀ مسلحانه کردند که منجر به درگیری با نیروهای امنیتی شد.
🔹
طبق گفتۀ منابع، در جریان این درگیری دو نفر از نیروهای پلیس به…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/445065" target="_blank">📅 07:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445064">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc26fd716.mp4?token=lQyuqfhb08YiFpFajtNg5U9Yvz6JU9RAvTtY-3581bTwBT3ofSrgxhYgrR6ICE0TT5ZslVHl32iClaW-HT5oQNhFSU7mHg_oxbAMQwI0y_0q0-cBvTxAPFd9M6N6xuTxSOJl3WBXvW-RuMNHsEgJf3Umug5rYSquUkauWREGASDclc5bO2kUd3Vo9gd_4EcoaWGLgv2KhWIoHEL8q2gD1BEXooTWoGEIMbCcEw4yEBoZMSUS2-bVFEWV474V9rBijwRPH2FJgASC59l-7dA15yD7Cv5DDjW7igbT6Wuy178GmSs8ah3JUSueRYLY4tpchbP1gu9AV9qiaiYcQx9MSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc26fd716.mp4?token=lQyuqfhb08YiFpFajtNg5U9Yvz6JU9RAvTtY-3581bTwBT3ofSrgxhYgrR6ICE0TT5ZslVHl32iClaW-HT5oQNhFSU7mHg_oxbAMQwI0y_0q0-cBvTxAPFd9M6N6xuTxSOJl3WBXvW-RuMNHsEgJf3Umug5rYSquUkauWREGASDclc5bO2kUd3Vo9gd_4EcoaWGLgv2KhWIoHEL8q2gD1BEXooTWoGEIMbCcEw4yEBoZMSUS2-bVFEWV474V9rBijwRPH2FJgASC59l-7dA15yD7Cv5DDjW7igbT6Wuy178GmSs8ah3JUSueRYLY4tpchbP1gu9AV9qiaiYcQx9MSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تکل زیبای حردانی در دقیقۀ ۵۲ مانع از گلزنی ترزگه شد
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/445064" target="_blank">📅 07:53 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445063">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e77ba796b.mp4?token=tVzlPxhPBv5FcP4bfgJb0TSwEF9uildiqkIVHt6Z2SeEWsmwQeFqPhYDr7RAVrRC8dimD_nh2wN1ZRc5McM7-nqh93CghPNxuZ7PjG_pgRi6s7UB9sGcTlfX4k3yDNc5Ug-HJObuHef32gnnQhZE7D1RZhwCGB-vgVdko6db7MvD2rb5J-t-95VYIiFpAcra3Y8BBlJWTotV4iCqq6G63j1d-f9db5ItQcR6lcpl9KrL4jvLo0TuI1gTZ1FVDa4vm3JDe21aS0xAvVojFQxEObGF9_AoT7y5xshXdQFuvJCUOIyzwbzVvZy0I-o5ykbw6tibWfo_OzPz3Rt0q5GEZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e77ba796b.mp4?token=tVzlPxhPBv5FcP4bfgJb0TSwEF9uildiqkIVHt6Z2SeEWsmwQeFqPhYDr7RAVrRC8dimD_nh2wN1ZRc5McM7-nqh93CghPNxuZ7PjG_pgRi6s7UB9sGcTlfX4k3yDNc5Ug-HJObuHef32gnnQhZE7D1RZhwCGB-vgVdko6db7MvD2rb5J-t-95VYIiFpAcra3Y8BBlJWTotV4iCqq6G63j1d-f9db5ItQcR6lcpl9KrL4jvLo0TuI1gTZ1FVDa4vm3JDe21aS0xAvVojFQxEObGF9_AoT7y5xshXdQFuvJCUOIyzwbzVvZy0I-o5ykbw6tibWfo_OzPz3Rt0q5GEZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شوت عزت‌اللهی از بالای دروازهٔ مصر بیرون رفت  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/445063" target="_blank">📅 07:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445062">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc44ca4f13.mp4?token=oki6A2UmTCqEsdNeMwA01AeDv9MYGE2Sgcidr352vR41cz69WZBcAYinnflbODrR6_83aPxhvGJrN2HbJv4poGV0seo1vW8bZVay1KjnpWiM8_p5Sg6O-48mbNUibzz7eH6LtdPHwnJtRJCU_87rCrWbvdDhzYrjUZ3-G-ogs6v8Ix6ecyybdzllmZR-i1LY7Y2ld_dr73UDHCfyFair0HeHLvN5TcZ94KCSAR05V4wXRJvcifhUg55jvFwqAVi96Q030oq7qwqFa4gtGFBhpiUFWmCIIVKiOiQ5o3tbcnOtzDL4mZZry_IDv0l1_eLVLroRxPB89UZXnEHOc35xpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc44ca4f13.mp4?token=oki6A2UmTCqEsdNeMwA01AeDv9MYGE2Sgcidr352vR41cz69WZBcAYinnflbODrR6_83aPxhvGJrN2HbJv4poGV0seo1vW8bZVay1KjnpWiM8_p5Sg6O-48mbNUibzz7eH6LtdPHwnJtRJCU_87rCrWbvdDhzYrjUZ3-G-ogs6v8Ix6ecyybdzllmZR-i1LY7Y2ld_dr73UDHCfyFair0HeHLvN5TcZ94KCSAR05V4wXRJvcifhUg55jvFwqAVi96Q030oq7qwqFa4gtGFBhpiUFWmCIIVKiOiQ5o3tbcnOtzDL4mZZry_IDv0l1_eLVLroRxPB89UZXnEHOc35xpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربهٔ سر خطرناک شجاع خلیل‌زاده از کنار دروازهٔ مصر بیرون رفت  @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445062" target="_blank">📅 07:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445061">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⚽️
در شروع نیمه دوم، دو تیم تعویض کردند
🔸
صالح حردانی به‌جای کنعانی‌زادگان
🔹
عمر مرموش به‌جای امام عاشور
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445061" target="_blank">📅 07:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445060">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYs7uUEZKdpXgQEYcYMfQ-MNTxe_45GufvPdGdHsRGf8HgqjuIPDG_cOwnVLqk7chYbG2DrGfqtcMSNzxZasVJvHnpayNAi2Yn6L86PvcQgYof1R-wwUdVnVmg3Y_IHzy09Nk8fHZbk0EvDdS0XamDAgFJnSaQneevJyvyygZcA0b5YNnWZ6t4j338X3poHW6BOgptjL5BQERIUyhSl6T2AjoFYRdH_ifCKWfpAvKYSA2X0H_vHcdSHZIcHm5yf-1Gf5G6aQ9Ii5G21XWA2fgfg4jxJ1NYj-2q22CNhEtccHRJ2dQp6RNDaLpD7ouWsxQRt-r9URsHpi0oQRpcF6vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نیمهٔ اول بازی با نتیجهٔ ۱-۱ تمام شد  @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445060" target="_blank">📅 07:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445059">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⚽️
نیمهٔ اول بازی با نتیجهٔ ۱-۱ تمام شد  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/445059" target="_blank">📅 07:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445058">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQhzZyfz0R9YgyKQU1ayxJ4FxCYrVPd5Ny9EDB-NWu2Ums-spvuWCjU56dQry8wTqBwhqTn_TgWIEjilcnuXqygsKHcIsZT4RlKptPrPDZrJ_FjjN0uh1Zv1SFRq4p0DbGxzRXQrujsV9kSWVT_-AZf1d_q8-IPElFN9GCjXRjlLSHn06BS7v35yK5lK-aPeEJ3MP5MXXVaPr-xotPws1e9jZCW8YBVG_v-T2bQED2HK1GHvPfG08xQEpmjn5dZvSkXO0Qx5-0-XQaT3HEvNhRMNtwQIx9IPKY-XkH2WRzyymInAgGnl4CTUyaOB3QV71Rl2_Fk6-FsQQnd4YalCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نیمهٔ اول بازی با نتیجهٔ ۱-۱ تمام شد
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/445058" target="_blank">📅 07:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445057">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f0751411.mp4?token=aBPu3dDxdxRC818nCLE0vbPhAGi7I-vNXqotLFR67a0Fgf3Ot7xthOsjhbC82GNcPFw2RRNyQlNnNPxonG8oF_WBbOG7g6uhGceJ7itglqXpq8lM_rX1VLhLdlOS7vlP2SnxVQ3lozM9Ohys_Fc02caSz8EBTeB3FfzV0MQLUiX6goHiOEy6Hd_og0w_DfkRVvyP4UgnNNkJ1C-N6TE89F5cC6UnpitOzNlLuHwKeRB76qm1sXZ-_mV8rGbt6vIyNhiL3q2mnwTcRO7So8fO93CCt5L36d-rMJHUhHXOQih5gvT64VArrGGGhjZLXac6ryWJ1Gmm7rb3AIeBiG9W-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f0751411.mp4?token=aBPu3dDxdxRC818nCLE0vbPhAGi7I-vNXqotLFR67a0Fgf3Ot7xthOsjhbC82GNcPFw2RRNyQlNnNPxonG8oF_WBbOG7g6uhGceJ7itglqXpq8lM_rX1VLhLdlOS7vlP2SnxVQ3lozM9Ohys_Fc02caSz8EBTeB3FfzV0MQLUiX6goHiOEy6Hd_og0w_DfkRVvyP4UgnNNkJ1C-N6TE89F5cC6UnpitOzNlLuHwKeRB76qm1sXZ-_mV8rGbt6vIyNhiL3q2mnwTcRO7So8fO93CCt5L36d-rMJHUhHXOQih5gvT64VArrGGGhjZLXac6ryWJ1Gmm7rb3AIeBiG9W-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رامین رضاییان توپ را مقابل دروازهٔ مصر بیرون زد  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445057" target="_blank">📅 07:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445056">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5644e6d580.mp4?token=tXSAEBWpFesUiC_Qy1sSs2Pk6SSTsI6zS1U6qy9xVy2yFdy5D8V4SM_4MyZZ0cnY9TONWpqyl4IMiwyHipr-wbO8ucXAAgf_1XXjV2lctaGEvgPcYicjaBnihkJe0vxFN9p4Lq5cQ1lmRsaGcp5bqgNO5o37JiE1vpl-lv_TYdVvYgVcurq-Rs3aADIoB8EGIQvND34uPDYXoRxAtnn46ggqKMBOVEfmGqFYY10ao77UPFLo_fvunuooV_v5Of2eX07DoGriVxncWPWUBbgXPM0RHg3fz4v1MMZyfTqUKja-vdDnoa6F3Vlar54KVBz0rTgBGvkaKTasLuPohA5fhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5644e6d580.mp4?token=tXSAEBWpFesUiC_Qy1sSs2Pk6SSTsI6zS1U6qy9xVy2yFdy5D8V4SM_4MyZZ0cnY9TONWpqyl4IMiwyHipr-wbO8ucXAAgf_1XXjV2lctaGEvgPcYicjaBnihkJe0vxFN9p4Lq5cQ1lmRsaGcp5bqgNO5o37JiE1vpl-lv_TYdVvYgVcurq-Rs3aADIoB8EGIQvND34uPDYXoRxAtnn46ggqKMBOVEfmGqFYY10ao77UPFLo_fvunuooV_v5Of2eX07DoGriVxncWPWUBbgXPM0RHg3fz4v1MMZyfTqUKja-vdDnoa6F3Vlar54KVBz0rTgBGvkaKTasLuPohA5fhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول ایران به مصر توسط رامین رضاییان در دقیقهٔ ۱۴
⚽️
مصر ۱ - ۱ ایران @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/445056" target="_blank">📅 07:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445055">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSeZaQDGJEJ6z2s7CnvYR25wqg6pA5FCTrgmRTNlNBS7lhO0Hl6CIdoAZPseYjt0O9XbBs6wtls2e71rsoRQQAthVaan1ZoS25krW2RmdNq5m3Q01C3A34wdGajzXnzrsSGJR7jTiyQBgUt71LnrhsGQ4Lmj3WPNiNEgWuS8exxxot3ffJiPGW9Apj4Ijq0kBLq4N_E7_u_-9PKZSFZi0gBg0rNU-dJiVyYLu2--YmwTkQviyLDJeHTK7Mdq06zjJxVccMwYBZ2mA2h0K-QDx1pKTsKaJhT9uDbYS5e1XFasWFwHperL8mhrd998PXLpNvZjMs1AOgxxH1XNtc9fpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پرچم یازینب(س) در ورزشگاه سیاتل
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/445055" target="_blank">📅 07:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445054">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtHsV1M8oeGqJwJDmrf_VA6PqwZkn0qe-20fpMagfwntJROAdnpZsUa2rYTTCBinPiURoV8OtBpJBWTtMl-_y5DDY7hlzVozHnO6dmuQDbq3am1jht77fJCD0S1WPJU1Hgsca0WsSlP44pt-GouA3bvg-51OZ_oTSsuNWLvQce8KzTDH8DfNlAsO1xExRuCPN_pG5HE1DlbjZGzZ5jkiOchBbtcv3KbbVZ-O4sEE6oK5lPPmn07N7tww2JdxyB87-6Am04Giairwb_5e-aN39NC_X7QwknstJbRkEPlk48_3kLBoEHzF8d9h--3xPf8uF13c2Pz7DDHVKkf3YFkmbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گل اول ایران به مصر توسط رامین رضاییان در دقیقهٔ ۱۴
⚽️
مصر ۱ - ۱ ایران @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/445054" target="_blank">📅 07:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445053">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">حیدر سلیمانی کارشناس داوری فارس:
💬
گل مصر صحیح بود و بازیکن مصر در فاز اول حمله با سینه‌اش به همدسته پاس داد و دریافت‌کننده هم در وضعیت آفساید نبود
💬
طارمی با زیرکی پنالتی گرفت و مدافع مصر بجای اینکه به توپ ضربه بزند، پای طارمی را مورد اصابت قرار داد و پنالتی صحیح بود.
@Sportfars</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/445053" target="_blank">📅 06:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445052">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87b88bf91.mp4?token=ByZBqUUGMvP5QyA0KrqYSsfSrH6jYzLGr241Q1qIFTcLtZN9N1iJFwVFG0u4IBFXzMHR7lslvRezOFCqCFKNIn-FmqyorWcRA29udgqOCzMu71xm2ixyuqT_rtQvHbV9sjReAz-oFazt5Kit6HGNta9BK_dKhrkuObZ3uMV-Mq_cogoXLbQlsTtCgvgNpoZWXUEqovz1xXFMDXzvbTLLyV1fUROjQnmrPDcHanoOIeybUDT2gdlwtnUSSKIubROHHQq7OCzaenbtavBX-grC_6mwyCnEF0OqBHI1oFWHD8cHSindkbCS-4RoCWKXVN1Zv8ISiBXx6As_vuM8UUf9OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87b88bf91.mp4?token=ByZBqUUGMvP5QyA0KrqYSsfSrH6jYzLGr241Q1qIFTcLtZN9N1iJFwVFG0u4IBFXzMHR7lslvRezOFCqCFKNIn-FmqyorWcRA29udgqOCzMu71xm2ixyuqT_rtQvHbV9sjReAz-oFazt5Kit6HGNta9BK_dKhrkuObZ3uMV-Mq_cogoXLbQlsTtCgvgNpoZWXUEqovz1xXFMDXzvbTLLyV1fUROjQnmrPDcHanoOIeybUDT2gdlwtnUSSKIubROHHQq7OCzaenbtavBX-grC_6mwyCnEF0OqBHI1oFWHD8cHSindkbCS-4RoCWKXVN1Zv8ISiBXx6As_vuM8UUf9OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طارمی پنالتی را نتوانست گل کند  @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/445052" target="_blank">📅 06:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445051">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e348ba189.mp4?token=gQ7QByGQEpHtGniB5jsoJZ_ZEZAC5kGUWIPxAsp705CVaBTc623_GOQkJwhQtGJDv9vL5KT2GmP-_RIHssfojpPVJl-KmW_VshRFhNCSwlRCqikWDMAmJ22YL1RpZeFh1r6vApF15rVLcjPH9FDU2kdeAtBg4gm7MEMb1ba9CFMYzSJEJctue6dyHacliQXmcUVBxfSunIJNI-aWEgG7zNmMvc7KuGCWHvuaJhPxZmzW5mg7w0afGhaGDUlzJCW_bxwmGX-OcZPlQpBkjgz5aWhoWY__TCQ_nvkSsfeaG0RaNn0nVviM9JNvBzOdqHxlS1SyJb_uv4DSt5OapOeJOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e348ba189.mp4?token=gQ7QByGQEpHtGniB5jsoJZ_ZEZAC5kGUWIPxAsp705CVaBTc623_GOQkJwhQtGJDv9vL5KT2GmP-_RIHssfojpPVJl-KmW_VshRFhNCSwlRCqikWDMAmJ22YL1RpZeFh1r6vApF15rVLcjPH9FDU2kdeAtBg4gm7MEMb1ba9CFMYzSJEJctue6dyHacliQXmcUVBxfSunIJNI-aWEgG7zNmMvc7KuGCWHvuaJhPxZmzW5mg7w0afGhaGDUlzJCW_bxwmGX-OcZPlQpBkjgz5aWhoWY__TCQ_nvkSsfeaG0RaNn0nVviM9JNvBzOdqHxlS1SyJb_uv4DSt5OapOeJOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
پنالتی برای ایران؛ خطای روی طارمی  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/445051" target="_blank">📅 06:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445050">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02fad4be22.mp4?token=Byp6uMiG5fq725CrV-4BPidTEJSUgGq7eMDHDj_5QCNJ3feJa4SAfAQDS5s6NDRtvLckfxNBr955zAER2dhBsOsikSfV6BN8R93bV6sOYlY8WJ7UHZ7mE_TYVcpbOZW5TIYlFjBJKsJ0JOMLSuDePk2DyCnPDUcIGRTE3EIIcqer_9TbdyBVtyXou5FYRUIXrN5mbpDQTZw-DkAOSH4RzTVbiA4It7qzbREg_RLu68M1EFN5r-d1UmwkGo3ru_t_8kw3kF-CXx9a104m15GvhKFK6DLWq85mE5KFf1qf6pvEw7Ff2hoc_G64SCPhGOo4_Ao2v0CpVgXePvmR6zuQ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02fad4be22.mp4?token=Byp6uMiG5fq725CrV-4BPidTEJSUgGq7eMDHDj_5QCNJ3feJa4SAfAQDS5s6NDRtvLckfxNBr955zAER2dhBsOsikSfV6BN8R93bV6sOYlY8WJ7UHZ7mE_TYVcpbOZW5TIYlFjBJKsJ0JOMLSuDePk2DyCnPDUcIGRTE3EIIcqer_9TbdyBVtyXou5FYRUIXrN5mbpDQTZw-DkAOSH4RzTVbiA4It7qzbREg_RLu68M1EFN5r-d1UmwkGo3ru_t_8kw3kF-CXx9a104m15GvhKFK6DLWq85mE5KFf1qf6pvEw7Ff2hoc_G64SCPhGOo4_Ao2v0CpVgXePvmR6zuQ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول مصر به ایران در دقیقهٔ ۴
⚽️
مصر ۱ - ۰ ایران @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/445050" target="_blank">📅 06:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445048">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea02389d00.mp4?token=Qp0FXMCW0-6I8NuOWXRzNvdI66brjg_Y1zuEPR8C0kQV6Mazz9zwJQSr80XJood3wYMCvwxFiYCz5nZW1tiZLxUnS6C2eMSG9Y4RvpyG11RU8sZy9JiOlV28-1KqxmGcDFKRDs4d7DUL4aXfGmHTJbJG9XlVBaMPMabWiUeExi8deHQRT-0ihDQtS8zHJSiA6XghngiuRCkY1DcFY2DPxrjB_3w4LYZKr-s5h4dVERuBr4EmDn3K8ACgQSeVXqRBP7agEnsP5xN1rL2eqcmKCYk22Pd8kiGf46oJK-0HPhvrthRofFMBN6j1JkxFd_QUUvls8NmRV1L7szAbbv83TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea02389d00.mp4?token=Qp0FXMCW0-6I8NuOWXRzNvdI66brjg_Y1zuEPR8C0kQV6Mazz9zwJQSr80XJood3wYMCvwxFiYCz5nZW1tiZLxUnS6C2eMSG9Y4RvpyG11RU8sZy9JiOlV28-1KqxmGcDFKRDs4d7DUL4aXfGmHTJbJG9XlVBaMPMabWiUeExi8deHQRT-0ihDQtS8zHJSiA6XghngiuRCkY1DcFY2DPxrjB_3w4LYZKr-s5h4dVERuBr4EmDn3K8ACgQSeVXqRBP7agEnsP5xN1rL2eqcmKCYk22Pd8kiGf46oJK-0HPhvrthRofFMBN6j1JkxFd_QUUvls8NmRV1L7szAbbv83TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پخش سرود جمهوری اسلامی ایران در سیاتل؛ بازیکنان ایران با مچ‌بند سیاه در این بازی وارد زمین شدند @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445048" target="_blank">📅 06:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445047">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1d6204e02.mp4?token=b86DWmqDu9yoevYsviwbD-g5tUNvl--OBt0zsKswmZJIZSAmVbuX5m5AU7Eypt2a6SVZUrfYZUQOgKH7mpfglHwuOD9-9V1O_n9JerQZxapvPihc1ntEEKFT1y8eXdLmjA37euIOj8-ItWsE4ydeNK6LJDTP7E4Yt3qJnuBYLG_JbwMy43HSajGVJ0RZJcHIPTEX2dGUlO1t5gjgzw9ZdjaqlORBhQ48MeCYjLcBHmf0I4BqwHxpjQgi9dp08kT64IQwHbw0Mj4zQT9JO-U1k_AgYuLu9gJkQ9Ih9ZOmDDfS0pQhkpIXtP0WX4fJYvnnwECG2ygH26iVphVjRUrhfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1d6204e02.mp4?token=b86DWmqDu9yoevYsviwbD-g5tUNvl--OBt0zsKswmZJIZSAmVbuX5m5AU7Eypt2a6SVZUrfYZUQOgKH7mpfglHwuOD9-9V1O_n9JerQZxapvPihc1ntEEKFT1y8eXdLmjA37euIOj8-ItWsE4ydeNK6LJDTP7E4Yt3qJnuBYLG_JbwMy43HSajGVJ0RZJcHIPTEX2dGUlO1t5gjgzw9ZdjaqlORBhQ48MeCYjLcBHmf0I4BqwHxpjQgi9dp08kT64IQwHbw0Mj4zQT9JO-U1k_AgYuLu9gJkQ9Ih9ZOmDDfS0pQhkpIXtP0WX4fJYvnnwECG2ygH26iVphVjRUrhfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پخش سرود جمهوری اسلامی ایران در سیاتل؛ بازیکنان ایران با مچ‌بند سیاه در این بازی وارد زمین شدند
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/445047" target="_blank">📅 06:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445046">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d193837db3.mp4?token=hy7E7N8lcu8Hfo7c2QHbq_F93XA89Y1zJETXzd9JFA48oUGJ4UkuvtYrmKiGjFXrmSYsjmEipdxZBx5S7QhYo5YSVyq5RQn624zTjgAGM2Dg2IfFZewKB2AsdoBaUgb4DP_1vSuk5JSNqSLCU0uckmbpCef3KfRmXTnqPFUswUp0_9sug3GBpc03OA8_YuEfKzVlL2SL7PdGtMTNbw7EC13TceHRcid9c3oQiSBxH2GBhQJ7bu5bfR4mW_X9bUAGkS8jd64yIkMzuw_xe-KU3ZqmuKz-cipEbddSnF07gh87HOR2Y76kSIDRALlXi9qu92h5CS9F1sk2B9MR-NHZ6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d193837db3.mp4?token=hy7E7N8lcu8Hfo7c2QHbq_F93XA89Y1zJETXzd9JFA48oUGJ4UkuvtYrmKiGjFXrmSYsjmEipdxZBx5S7QhYo5YSVyq5RQn624zTjgAGM2Dg2IfFZewKB2AsdoBaUgb4DP_1vSuk5JSNqSLCU0uckmbpCef3KfRmXTnqPFUswUp0_9sug3GBpc03OA8_YuEfKzVlL2SL7PdGtMTNbw7EC13TceHRcid9c3oQiSBxH2GBhQJ7bu5bfR4mW_X9bUAGkS8jd64yIkMzuw_xe-KU3ZqmuKz-cipEbddSnF07gh87HOR2Y76kSIDRALlXi9qu92h5CS9F1sk2B9MR-NHZ6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورزشگاه لومن از نمای بالا پیش از آغاز بازی
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445046" target="_blank">📅 06:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445042">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CHX_etAF4d91OVDBWKptKtjDgJKZ_L2ExwbcVK3y2RaPpq9wN3kdPRDUvsM5J3nzg528a8swQMkUh8_FAcpcW0i9gv66dNo8dK8ANIxNLUdkS4qaLgEeXDNAw4ZQo0xb96QeaTI27lXTG0XKvebkG56iNFxKmP-FsSYvd6MxBN539T6WEl4pMFozTghxV2JFLbdkrwNPW40j0YBr_rpEDWOHidM6yQo4mibAzRZFkpckxtnQLFu7l92liKdrJxhlKnjKSkoVzSMr6Bw_kBQnNCmhPmR9Z1JLEPInPoFLY1i1csjxI7aQzGv2dwSqWWh6CiUXvlempWVPN2F_Pzb5Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fz9G_4YnsWBbYXw5xWMYwqCO7BrpYIJDQ-QgpKxtDyD3YPs_Ql_djSoumSDZfFvPYxTt_HX4dpIq8WJYRvxJIMiSps_W11fAHnbumokoNkaeZXXs0S7fdbX8vveqGmt1ceJ0IQKtFIBN6W47QNX-J_Gg8GcEJird7hpMsePXRUscKY55HF9XANjLHdSo7Z7GyPGokMBf6IDZqEfG3qV2aEjtVpFiiBeGDcDpL7r6q5BwE3smpYMZXq7CjM6CncoEtvUOPGvjXPG0DV5E0rXH3N4nfvIUD47vcQ9EDyD3HePrRpZO3RRYJ_5YbrGV6yOkLPxVSZ4NuBn-g0rj-19wFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jy4jbg0ah-9fTbHBHaCD2ZygaScKovYGmbI08cO3Q8yxAh_6Pg6TvwmqLKVIcZjNwE8uWLesrW0hObRDq7ZL11cCUpzmgfNSCkPluDLeuMPckdJVfcW6U7I9rjgdPh5MjR6a2GxOMzb6DhWRe6iIpDOtxJc6tygAf7JyYPjf7ARao8zySNlb9Ly0JhejVLIrrA-JnC3V1x0hNGPeXB0c9xChv2giJJMUb0Ry9YQnUUhIkL8oMUJgT9PsUQyAk5-d9vo-oByP6QeKbxHZiRE6ev2aMdcA1t7MvGvXTCwlXgELRYY-ha-Utcxjs8GonCzHR6ntgaQBFBvkLo0KX-fBRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eLlKmRVhzYFNjiD9zqPO3WQ60nOWX31woejC39gKGGdP4B8Ikzg9QhVQD3PodrC-Pp3YEscMDPjmTii9A85dcBwbzLQi08ZJoCdC3mJOnAoKjKMtvX6_Ab0CqjTq7yOxyMdZCNzB02E0jP9B-7_G18l0lEsN_KzUBIXoLnsNmHnV2iPolg06bILyNgCpH0_cCk5B5MoTkACAuoTDtj0xcwX6Q_GeJJ78P1biAHnSuD4wKH-QnX6drpWW4EZdwKUzjr_IjkHxdgO2LQIcwyF7TBokFeI_-Urglzy9NTMX0Xhg1rWKwygNeEID-NiRFyMT5mUGHRDH6B9hywkgnEi-BQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بازیکنان ایران وارد زمین شدند
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/445042" target="_blank">📅 06:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445041">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rK0DB1DZBgNT10ic0Samcv3voCD-eUfzbUtp1W0e45jKnwcNWtO_puuWM7DwRrET_rVr85eFHmmwMka4aDj-0l-oJi5DQ34_MR31H4Ql_uR13nSvJMh2zFIEWQ_wJDKtN7918SU-IASW3KB2dyutDT5IYFDQIcT2fGdi2JiQPU7w2_ElknAeMbU2xGgECxsSHkkxVK4lskcCz_YXVQBhI3Go3R5OdQecSJs0a2OZeoIDTnI4AdwqIqdfLv7q0iTXFdwwwvUCivXZ-bWIjDJitCxJpdPIYjC7E_TR0zQPALBoCmNcftXVF3qcX5YxHH4Ratg90uBXVSNi64Sn50zq7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
بازی ایران ـ مصر فعالیت ادارات کدام استان‌ها را به تأخیر انداخت؟
🔹
با اعلام استانداری‌ها تاکنون، ادارات استان‌های
کردستان
،
قزوین
،
فارس
،
سمنان
،
گلستان
،
یزد
،
مرکزی
،
خوزستان
،
کرمان
،
مازندران
،
زنجان
،
آذربایجان‌شرقی
،
آذربایجان‌غربی
،
چهارمحال‌وبختیاری
،
کرمانشاه
،
اردبیل
،
ایلام
،
لرستان
،
هرمزگان
،
گیلان
،
خراسان‌جنوبی
،
خراسان‌شمالی
،
سیستان‌وبلوچستان
و
بوشهر
با حداقل ۲ ساعت تأخیر شروع به‌کار خواهند کرد.
🔗
جهت اطلاعات تکمیلی، نام استان خود را لمس کنید و شرح خبر را بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/445041" target="_blank">📅 06:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445040">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">ایران و مصر؛ نبرد صبر، انتقال و صلاح
🔹
بازی ایران و مصر در گروه G فقط یک مسابقه معمولی برای صعود نیست. هر دو تیم تا اینجا نشان داده‌اند که می‌توانند مقابل حریفان قدرتمند رقابت کنند، اما مسیرشان متفاوت بوده است.
🔹
ایران با دفاع فشرده و نمایش منظم برابر بلژیک یک امتیاز ارزشمند گرفت. مصر هم بعد از تساوی مقابل بلژیک، برابر نیوزلند به اولین برد تاریخ خود در جام جهانی رسید و با اعتمادبه‌نفس بیشتری وارد بازی آخر می‌شود.
🔹
سؤال اصلی برای ایران این است: مقابل تیمی که هم می‌تواند دفاع کند و هم در انتقال‌ها خطرناک باشد، چه باید کرد؟
ادامه دارد... | در
فارس ورزشی
بخوانید.
@Sportfars</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/445040" target="_blank">📅 06:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445038">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPWewV6stSKxb8FpTLsK27FtXzAcEGo59F-xzk3qMqCAHv5KrwHhjm4gNM3MylwG7cNufL2VKYvWCMchz2PYB3gI0MBodiZn5Ya6as8NCviVyRjGY3EdX90oAtp0xisyrQIwE95fy0Q8Z69NuMMZnOuh2VP-XdZHCU8gsbV75vZlYgnAVWAbnEIdpC-iabkx3DbUFJZ11NVc-5cQZzKvgXs49EGWDS1AvvbrqoA0PS3OmSVAOa08YkdTlmZdUhyd9qLIHH5cekvM3Qn0CkDpNiTZKMq8Gc865TO2tYhtx1alHddOBoXwFF-pxq9RbiUBipZrwCBnaMCCaJMWrCa8pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
جدول تیم‌های سوم تا این لحظه
📺
ایران در صورت کسب مساوی با برآورده‌شدن یکی از این شروط بالا می‌رود:
🔸
بازی الجزایر-اتریش برنده داشته باشد.
🔹
غنا پیروز بازی با کرواسی باشد.
🔸
کنگو مقابل ازبکستان پیروز نشود.
🔹
تساوی بلژیک و نیوزیلند، به‌طوری‌که گل زدۀ بلژیک بیشتر از ایران نشود.
@Sportfars</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/445038" target="_blank">📅 05:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445037">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ib5_RlURpg1_sQH5jZWXaggjQ2NRDtSZLG8VPKUjQ32twK36StGUt_QXslLZZhfCrGRAUUzuVEcMEOossG0Be6zJpIMvOmsbNd1H8bSHqxpvt_HIBOkKPUNmcODo1c3YLoEddsAZo6HbVNXtx_E4X4KLEKVNbELQwDq47oQ6qlI_KV8fJUQduLSOUjkCFEynMq2snvfmx0_J-9jN3gryGySjcWKuOT4IlrcK7CDk2GO1DltWSeboymH_nAHvK_h91emNHULBAorULK-VopVL3VfknUzggV0nw_-qzddipPTFuIZ2rcAZvAhBrGC3V12mQuWFDXiVqF64CRt1Iz4PbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
قلعه‌نویی: مصر تیم قدرتمندی است؛ اما ما هم ایرانیم و برنامه‌های خاص خود را داریم
🔹
حساس‌ترین بازی تاریخ ایران است. بچه‌ها فقط باید مسائل تاکتیکی را با آرامش باید پیاده کنند.
🔹
شاید بعد از مسائل ذهنی و فنی، تجربه می‌تواند عامل موفقیت باشد. نتیجه دست خداست.
@Farsna</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/445037" target="_blank">📅 05:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445036">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-xCTPzvKg1FwqZ6YVHmmGiOJDjkbBHZfBVmUsFALzHNJMJ8Hi_t4mZcJMExUCyAPfYooxo6cUtpjjFQZInpoI6qc2PHOyWO-sjX5mx1DgFHywAzz2X42bWLuylASnmNoi0uePVHHGY4yoXlyJEqQvA_OqBmUbuXbgmMPUQSBntU-KjbWh9Z9Gx8yexJF3FYvsByAwIPsWRejQ_gkERoA2sg5js3Uy7Z2TJBOdDoTruIavRoM3eJjibhIkmg9INJROecszCx5oR7jPZvjTt-qmfLZzzcZ7AW2O35cebPQZFLdm3ZAQvGKCjdmZefN2KLTcDlAhT6LLmf6Z3M0ZKuvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از توافق لبنان و رژیم صهیونیستی چه می‌دانیم؟
🔹
توافق اولیه میان لبنان و رژیم صهیونیستی را عملا باید طرحی برای خلع سلاح حزب‌الله و پایان حضور مقاومت در جنوب لبنان توصیف کرد؛ توافقی که حزب‌الله می‌گوید با آن مقابله خواهد کرد.
🔹
لبنان و اسرائیل شامگاه جمعه، پس از چهار روز مذاکرات در واشنگتن با میانجی‌گری آمریکا و در پی برگزاری دور پنجم گفت‌وگوها، توافقی کلی و مقدماتی را امضا کردند.
🔹
این توافق با حضور وزیر امور خارجه آمریکا، ندی حماده معوض، سفیر لبنان در آمریکا و یحیئیل لیتر، سفیر اسرائیل در واشنگتن، به امضا رسید.
🔹
بر اساس مفاد توافق و به گفتۀ یک مقام صهیونیستی، باید هرگونه تهدید از خاک لبنان علیه اسرائیل از میان برود تا ارتش این رژیم از خاک لبنان خارج شود.
🔗
اما این توافق چه مفادی دارد؟ جزئیات کامل را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/445036" target="_blank">📅 05:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445035">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8ePCwosmg_KR6taXlCnox1HvqFFjEojAY4XY4nu9gSfUmg9Kbid4eCNbtsShshZadlBgpEbLbdBXR3FAtSu7IGg5Y4fHOVHw9T3hzkFud2wj4gOIoAdZYJB8y1-vyf-bWXqJtBtW0hjKy9VksYMP0Y1Yhbz9HB86bMGgWwNp9bjtNdEIs6cOxxWA5rSERLn1UYBP22nK8DXH8FYIZUcBMsgOxsY4KgszNiLOTuHcgRI6Iinv0K4mjD9n2zH0zRsy9WkA1j2j3-Y_FLc4ySpfprN_Fz7JfFcuQUIPCe8KLcFEOqd7HD7hJLVZ_o8jY1_ldGz1rgfOCIr0MhA3w-ciQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا مقتدرانه در صدر؛ بالاخره یک بازی به نفع ایران شد
⚽️
اسپانیا ۱ - ۰ اروگوئه
@Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/445035" target="_blank">📅 05:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445034">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9MqQIlNZsdBg-Aux4GX7tiZ48D0DBE7EtQI3gtoagMBzmmV2__CTQKPf2AWpo8HNjk8v4XUNSxlXtXGdQ_ArQurgfTLM_hsQHdjoU2iUiNUBkhla_RvfRUUVE-aP3qL8XzY_6A7AFpwJqpJxv7c6y9ccNBeJkty2gMISpD9--RWPQjrulCQY4nMdVhWAnRcIaxIOe-HBZv6dN3COk7rvjsRASPhYBg2EaZfdNIkblj5JhjVOEYgJ7v0ZiESIuaclP86PJ1m-8kl7styh8DZy7HxfLy9J_KYtLrI9Ky-sWf2x1-FAIqW2dMIyKQ4qN0XXqLYAOqneHGK4Krzmk4h0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
دیدار عربستان و کیپ‌ورد با تساوی بدون گل به پایان رسید.
@Farsna</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/445034" target="_blank">📅 05:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445026">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mg9GcDzcZReHlxiaGuRW4vBe7Y0bQDiDiXCfavyS31RwFiRzN-e0iinl3JfpwjFKcpmZcg3FziFE1qD_gArLA7XBH7Xf6vYgVGtgliEzTpLhOF3GVc7h8ioAAsFcV4jvoQ4s38Np4IJyaWrpOz-3fV6SGqkpptMes-FEWkaD8Xxnv5uB_ZhJjLSgoKLZHeEZkYTQJANBt_doEfahDj3NNS10XoIqR7TNcolmNW3rcyIdqogpfJZ3136P_s80vFtzfD-S5K1Tra7JZO9HIl4bkiJp9f1ImkOkEzwLVQNhfJDhjYcwzyR31Zk8BuJILzf67JKnOpuuagD2lQEx3tTHcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D5yDNuEwq9ZUIg6sNJHzQX6Fiuz4CjxheIIrxWzrVJmXpyqxkk2SX75QBMz7BR1Kyx1gINLuRahxfuWRgj90L4qbYqXK32ZQysZxaeWu7Uao-UgXRdeYz_BkFPK11EObBXcyuFFHgXmxixDR-SDGA7ESrPqIZYE4Wht5qEKsP1riFgP_KpD5xG2CpXRHWOiUvyYCH1g6k1zuz3SORbkVYI5STngMy7y9m0oug1oEBjxOQyz1Cm2U-bah2EGkotk5bh-x_0_FkoHhM8lUrNJyQrEsbRpkuhkS7DDbkH-zR6nwJHg9W0sgC2qYrjixJt5KOa_9gWx-JMKXY4s2_WjYQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W0w-oJdfYrWBuRswwiAVdlelepQN5gYnJ8JCpiGv4JaoGrqdXcSWM53JARqrP0ZNVBe_tUaDEy4gQZFcw0pe3NibhahGtSeq_HXxz7YfL81yurg0HURfHtJKvYUv5thOHTjOClAAx4WgEdUCocvkmXstn1yKAo5SG5g70nQjGecfQ11KgxBmi24J8glZtFYj7mK3qRP5MQXKsc2A2QoPetB2-PqzmzqdtGQaoU3csV0icUBzeu1PWNn6954vJFC7YM064dnMEE-QL2wUyUs2Tu5Fv2BCilByiHvp9e6njWI5oaX1lPlVgYS7iRXnatl02ujlrHnCh5Y8W4OpIH7SwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SSyY7Inm7EUlM0Tgcx3jwj8EBKec54FefVA-u0_jwxUjBNhk4x4p3aXozdWhocASYq67n8npPoMhWJiu5Op-GwhD8LxlcPSYu-4JxkCEMmPlfZ4Vfy-RtGlqIuabIjZCVNSU85K8S8XGcRkke0Mdg7BTCIJZw0tqkcpcoVUNKhWFd2EojVJORM3nDdJjCZZR6kXUHDzr_9aqLo2V9alFGGmlovcoVqYVQcnb7dteK5Dua6_0C1UdeIZCbvrZ5T4sre2KnUSoGM4jQUl5kbTo7hzQqK-LKVNDP1OznIACCgJUx_Ry-PJ4GP-H9JhfNXCfvW4uN6Waw49RP3L9C0QshQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HIJgCcO2LuQePDG69GQXj9JdaxLVS0EShi4MuQIEKY4wBiy_-1su3sZdk7wNBF6w2B-dPyc-J3au5cjTh7PgAwASRwd9QYOhijO0Ds9e5SDFkjKZhamXHpOxEIT3kpDELbzxlWv7J86D3zpf6BJHlgn0I3OldSKeGgxgtCO0stjHctcv86ptisTjhiyuvIu2sGYw0MK-YftVhe4ZiQ9hKzJWJjHqYK4vytu36h_8WVutsHmphoZYCfVDlBSX-D2WUNOE8q5J3G3OjbvMVL_aRpwmju8lZ2SCjgmfX2wWRVdLkCJoCvkbfmMJrwo7bQFVpmShAJV9SDyeQ04EbXeyHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mm3z5-9Vp9eQGmBLzWHUaho32RPffFsdphGnoQClr1SjkU78Kn16xulDE3xALf7qY79nOCDLp9IrJFdk2-oQEZW4svz4lmg7WIQQ830LmrZDGhG2jmUkD-AH-wYYC-nfPO3AhoARlvNbgfV6u1iwXVICxJYatdlMlhR7gob7rOJDmC3y_chQ7qmEI8FQG-kuQevCnmHKAh5J-DxAypv2Svs04_3ZgoFFL754acC1Yz9bzyI19AuhQgK7FvVLHGiCRLoVx72yAMnUywUAqj0jTix5Hj5-fjk6zOwzL6u3P7Ja-92OrBWsjQYJ0rmNToMPdAvVgHtJuUhLrBRhKBKXmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EnIbeYge56e5_CKR8pWaN6rIwCbBaN6D16mfff8DtgXmQI8nIke8Uyqf5-Qpm825TbYneH8trxvU-UhQmgl8urUdZOJI590DQ8RO8w5pafh_WKEAZ97hFbwzo6BUj_FWSQvSw-PCjfu7ZbeNLuueYqiRlJvdWFSzxqkEMFctC0bAHs7NQ7CVEMpneBEgRB9VKwRYHTC1zXPpO5RZuuLZ-t-tGy2RcrOLo8sjrtmhf3rdx4J6YjYrlWPIpAyp0IFEVpyiXH811mKqq-8xX474-ryZCaZhRJ-kabNmRBIS5tm4O1S8XgXI_yztE2fTPkVunfP2xufrr3RuomPJVsnnuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dXH1FgQTUUGsfDwKGMG5Vq5g9Z1mvnHCq_R-QEbeYY-Z171BnnUgFskt4fRYZqH-gOIYxMpFMgQgXc966owW1d9Y3PAfCLrKav-Lm0LH9I74r_b7ilnARMNhrmJjnRm5kvn5gthiPl-X0b0C3ic0EAJqOOgqTiDL3x3zBdtW61WHfHYUwsUwI6nVh5GzmqNd-0bPg-LvSLD8AmDHE_EgLk7GeCkXT25KMezWeQknyFNA81Qi4jOj5XHC-uTpsZjU-zt-2K50kp09zTu6gMVHz-_OOaWz-IDXMPS439M9FoBzKrNhAwlozOXKcldDgNv1cSMlzVelC3PPmr1YCWlK8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از حضور بازیکنان ایران و مصر در ورزشگاه لومن فیلد
@Farsna</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/445026" target="_blank">📅 05:37 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
