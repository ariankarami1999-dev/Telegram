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
<img src="https://cdn4.telesco.pe/file/W-GwR4AepoI8Gx9auHL2O1X5gcndJ8DnGa47vOLyHmIfm061-mSosy22_CxTXjtNpGzuaMTKIG4npt_N0M2-719YHdoBOwgNoY5Fcoql6sAmlJAatBL-GPfBN7P4sqFqnnD4QgIhbFopafN-zSRYIFjn6EBMNIxqdsHU0lzD_2Ul23BfM0KH48_G7m_9rDLPXUjsZK3KeS5Y341cSkSPEgSpTwo8LCHtwvyaqWCJ-BA3MC_x1jyNYcG8wRb6c82yJ0qoKDBn7gf_3yXFnahdPWqZl3Ft31gPMiWhBTF87Sp9T4bFLL7oLwdRWpoL0xaDI2MRTeWjwjInceSOPD2Q2g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 140K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 12:12:47</div>
<hr>

<div class="tg-post" id="msg-69292">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1l9Dk0teRffYIOrRzaJyBf6438qW_BiOznbkjB7lzPaWG3YHEVcTXVW3tTvzgO5VS0c470NKQoHW9mOCXVVbe5vlxI2JUydgl1Dx8TAA0wLtTkvSr8c_1y7F3OVIlIV03HZIyVOtHV46AMV2izfitqEGQaN3p1iLyaTZyNXAd_zGsVzFF50HTy53Hxl8sP-023u2TuRZ1HvAXE0eOv0dQ0K757FntZdiiu6bDhiYEX2kBpgYW8uuPQ3oAwUm9abjSpLYDBzhRFWtaQpRWWEaA30YdAn1r-0vBPEAm5Ovxi9dlHlov6pGYrIDJTANR_pgJvcdgxcWHgkSlB1A4DUmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
به گفته یک منبع آگاه، مقامات سپاه پاسداران از هیئت حماس که برای مراسم خاکسپاری علی خامنه‌ای، رهبر عالی پیشین، به ایران سفر کرده بود، خواستند که در امضای توافق‌نامه عجله نکنند و وقت بخرند.
یک مقام ارشد آمریکایی مدعی شد که ایران تلاش کرد حماس را متقاعد کند تا این توافق را امضا نکند، اما این گروه تصمیم گرفت به این توصیه عمل نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/news_hut/69292" target="_blank">📅 11:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69291">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=ZTA2Kl_PpAGlJt07e-k2ncDGaF4RTlqX-YsW5pAUuYP7o9acbJnRqKpsUykxbPBOwz23SmP-gbFs-Jg7fLVjd3Ug4wsR1uzUmcjVueV2UQ3VL6y0TYzxkF7LfW0hgBnN-mzIlgXVazV0ni6JA7eMVdbrCo9wkKS_DTJLrOmUpOZ6z-kh8wH5lAWVrmVRxQb6GmvFo2dtaJABA1ywmX1Do9-QtkXgQAyhmVbCV6-9Pl6OH09vu5wjBMdZ2Ha5uOXJuF_QthiuKrmql9JICP4YAO94oDJLBvLS0-qXkUtAPWTvHS0u0t_QZeRgzXK8XG091QMuSDjlQ8JMvD-Yqm4mzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=ZTA2Kl_PpAGlJt07e-k2ncDGaF4RTlqX-YsW5pAUuYP7o9acbJnRqKpsUykxbPBOwz23SmP-gbFs-Jg7fLVjd3Ug4wsR1uzUmcjVueV2UQ3VL6y0TYzxkF7LfW0hgBnN-mzIlgXVazV0ni6JA7eMVdbrCo9wkKS_DTJLrOmUpOZ6z-kh8wH5lAWVrmVRxQb6GmvFo2dtaJABA1ywmX1Do9-QtkXgQAyhmVbCV6-9Pl6OH09vu5wjBMdZ2Ha5uOXJuF_QthiuKrmql9JICP4YAO94oDJLBvLS0-qXkUtAPWTvHS0u0t_QZeRgzXK8XG091QMuSDjlQ8JMvD-Yqm4mzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدئو وایرال شده از یکی از مراسمات عجیب آفریقایی ها که با شمشیر همدیگه رو میزنن
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/news_hut/69291" target="_blank">📅 11:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69290">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBNu6-r1vNZT0xopJwSvuwU3GNhfoJslOgjozCwj-hMH06B3b0sAmdX4h4LRs4y0ppL0OXQ37cjN6FKea9Gv5lp-sBxr-qrCOYjsO8Mz80PeRoL4gRfSB1jMT2C3HmORTz0u0VlbYfkNPykIqqiUAQZPzCMHmSRrIXG5-pbj3lDViuSQsRWunoAe45_77GNwWxrBjsSqKuS32ZgvyPMbEz0B0TLJ1nty_4FmoDgS4h32DYM1irfAmdzwiAhFCUGJ-GKfFei4Axgbh7FkhT6F5ECOMgXJMz_evk2bsIxjMcwqHZlsj0r_MAaLfE1Mppc5BkL9crcizFLONKewo0XVVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇱
🇮🇷
تایمز:سازمان سیا و موساد اسرائیل در حال تشدید جستجوی خود برای یافتن آیت‌الله مجتبی خامنه‌ای، رهبر جدید ایران، هستند که از زمان جانشینی پدرش پس از حمله هوایی فوریه ۲۰۲۶، در ملاء عام دیده نشده است.
مقامات اطلاعاتی معتقدند که او در این حمله به شدت مجروح شده است، بیش از ۱۵۰ روز از استفاده از تلفن یا لپ‌تاپ خودداری کرده و در یک پناهگاه زیرزمینی به شدت محافظت‌شده، احتمالاً در تهران یا نزدیک قم، پنهان شده است.
با توجه به اینکه نظارت الکترونیکی سرنخ‌های کمی به دست می‌دهد، جستجو از اطلاعات سایبری به اطلاعات انسانی تغییر یافته است.
مقامات سابق موساد می‌گویند که اعتقاد بر این است که مجتبی از طریق چندین لایه پیک ناخواسته که پیام‌های دست‌نویس حمل می‌کنند، ارتباط برقرار می‌کند و نفوذ به حلقه داخلی او تنها راه واقع‌بینانه برای تأیید موقعیت مکانی او - یا حتی اینکه آیا هنوز زنده است یا خیر - است.
برخی از چهره‌های اطلاعاتی گمان می‌کنند که سپاه پاسداران ممکن است مرگ او را پنهان کند، در حالی که برخی دیگر هشدار می‌دهند که رژیم ممکن است از بدل‌ها برای پنهان کردن حرکات او استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/69290" target="_blank">📅 10:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69289">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=YyfY5dOrpDmFo6egl7iewx10BkggLcvTYaAJlcGDiZHFY_D05NX5YOJInpftv9nkRoE0XNKn9Y__DEm4mHu1T9Fc1PqNYvbkuOFtDNlefFkTdexUb0VH_Q-1EH415BiCfRaiBJmIvTa5X6jIEuca86Z-jTP0Ui1XrieSm0i0DK6PLvlA1m3davRmGM1OuK8QLJfW3lKtIUWpmHAgDvF44tXLblGmgMF8KdF8-ylwCbNnsItaecymZ_rXsnXpmLgOMDnWOVC9fNGMlc6hANeWdDvDVkvFsZhcYM9XPzFzV4t_UTblLMDxEa5Nk_6Y_jwzYlPKnjbsWhzs4JAK3qABXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=YyfY5dOrpDmFo6egl7iewx10BkggLcvTYaAJlcGDiZHFY_D05NX5YOJInpftv9nkRoE0XNKn9Y__DEm4mHu1T9Fc1PqNYvbkuOFtDNlefFkTdexUb0VH_Q-1EH415BiCfRaiBJmIvTa5X6jIEuca86Z-jTP0Ui1XrieSm0i0DK6PLvlA1m3davRmGM1OuK8QLJfW3lKtIUWpmHAgDvF44tXLblGmgMF8KdF8-ylwCbNnsItaecymZ_rXsnXpmLgOMDnWOVC9fNGMlc6hANeWdDvDVkvFsZhcYM9XPzFzV4t_UTblLMDxEa5Nk_6Y_jwzYlPKnjbsWhzs4JAK3qABXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از حمله عجیب طرفداران حکومت به بنر ترامپ و نتانیاهو
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/69289" target="_blank">📅 09:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69288">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‼️
دلایل سقوط شوروی که صداوسیما پخش کرد در مقایسه با وضعیت الان ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/69288" target="_blank">📅 09:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69287">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=UWcKrxjq0Fxa9ix5esJWejPd41HDDsXAM92TnJ36hyv_0F830ALPdOfRuw073KmzNPss8NoNkuwX71m3dDJbPZRCAEVA9FcX74kaSsOA0ZLLWSbt0vDGw934QTmVxWvUFdf2QqEEncPaGUQCoxAf72i0pxYY5A1JeURgpOAIRrXH8JtyHtstm6GclSB17lDtfv1kGGyet3lwojQtggFhlHxjSfD593BoQYyyeYyty2uKFGCXVTudbLnBmlMugsKKody4nulo14pjRKN3SBheEJzdfImJJLpKy5NS2mBdKXVC_MiFhF_oqRFF-QBY6HBEPL1X2yxF2dmi76Sk-PT1Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=UWcKrxjq0Fxa9ix5esJWejPd41HDDsXAM92TnJ36hyv_0F830ALPdOfRuw073KmzNPss8NoNkuwX71m3dDJbPZRCAEVA9FcX74kaSsOA0ZLLWSbt0vDGw934QTmVxWvUFdf2QqEEncPaGUQCoxAf72i0pxYY5A1JeURgpOAIRrXH8JtyHtstm6GclSB17lDtfv1kGGyet3lwojQtggFhlHxjSfD593BoQYyyeYyty2uKFGCXVTudbLnBmlMugsKKody4nulo14pjRKN3SBheEJzdfImJJLpKy5NS2mBdKXVC_MiFhF_oqRFF-QBY6HBEPL1X2yxF2dmi76Sk-PT1Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار :
کشور های منطقه که مورد حمله ایران گرفتن آیا باهاتون تماس گرفتن و ارتباط گرفتن ؟؟
🇮🇱
نتانیاهو:
بیشتر از چیزی که فکر میکنی و بیشتر از چیزی که میتونم بگم اتفاق افتاده
.
⏺
خبرنگار:
هدفتون درباره حکومت چیه
.
🇮🇱
نتانیاهو:
خب هدف مشترک من و پرزیدنت ترامپ مشخصه اگه بتونیم تهدید ایران به طور جدی کاهش دهیم توافق های صلح زیادی انجام میشه
!
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69287" target="_blank">📅 02:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69286">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-HhNPEsLi2snIEG15-fsTWV9QnRPc1jmJcSOgLMbko-hAgZdcxdAtVyjVJvPz9UABvFyWx9kZPd8zVU__GYg1f0kTqg114EHr6U6uJTife9T5m7VLrLV3OdB1IVuImxrbtDnHePsotsLJv30pexnSp2wXDk6udNOkjRmiNSSDE0jAnksJ4GjxdLjRIY8MMK19HzpsFpqOrgEs5Q6FWIX9w51CGQuctrHohEGkDe1qkLVGH9Tz_dqVQf_gBw9FRfPyGAmWDIW0gxexiesJiFJOFuzXyq2Y7q5H0TUCHjHey_ZaeNUxxbkdiOHbXvgnYq8DES6PL7-hzq4ZdEwewzZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
امروز، «شورای صلح» به توافقی تاریخی برای خلع سلاح کامل حماس و تمامی دیگر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.
این توافق گامی حیاتی است تا غزه سرانجام تحت اداره یک دولت جدید فلسطینی قرار گیرد؛ دولتی که برای یاری رساندن به مردم فلسطین، همکاری نزدیکی با «شورای صلح» خواهد داشت. هم‌زمان، اسرائیل از امنیتی که شایسته آن است برخوردار خواهد شد و غزه دیگر به پایگاهی برای حملات تروریستی بدل نخواهد گشت.
این رویداد، نقطه عطفی بزرگ در اجرای «طرح ۲۰ ماده‌ای ترامپ» محسوب می‌شود. این توافق طی مراحلی با برنامه‌ریزی دقیق اجرا خواهد شد. هم‌زمان با تکمیل روند خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و «نیروی بین‌المللی ثبات‌بخش» با همکاری نیروی پلیس جدید فلسطین، مسئولیت تأمین امنیت غزه را برای ساکنان آن و همسایگانش بر عهده خواهد گرفت.
یک سال پیش، شاهد جنگی شدید و خونین، بحرانی انسانی و نگهداری گروگان‌ها در شرایط اسارتی بی‌رحمانه بودیم. ما به پیشرفت‌های تاریخی دست یافته‌ایم، هرچند هنوز کارهای بسیاری در پیش است.
می‌خواهم از میانجی‌ها — مصر، قطر و ترکیه — به خاطر تلاش‌های مهمشان و به‌ویژه از تیم فوق‌العاده‌ام که با تلاش‌های خستگی‌ناپذیر خود دستیابی به این موفقیت تاریخی را ممکن ساختند، تشکر کنم.
اجازه داده نخواهد شد تهدیدی که در ۷ اکتبر از سوی غزه سر برآورد، دوباره بازسازی شود!
بر اساس این توافق، غزه سرانجام در اختیار دولت جدید فلسطینی قرار خواهد گرفت که در خدمت مردم خود است.
این دستاورد شگفت‌انگیز را — که همگان دستیابی به آن را غیرممکن می‌دانستند — به همه تبریک می‌گویم!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69286" target="_blank">📅 02:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69284">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYTlMFlEgL9Ie3lcl17RAvWPVX-EfepAljuvybhvIoAP1HFIaePKAbpWtexUMbiuespyKlJ3ME1a9vPAvueNhbCGoAx0kUzgfcllgGsO4KNHeRB3hsZQrGGWm5J-Cc8ZZ3T4YcsDx45Xo4zwQlMPsOmQOWlUhiGkNdHQz3rMB93H4qCoEVMLj2qZXWYjyyFqF7D-k_oU8nOUenbJi-eEk1rNZMbTroQnN5aliPf6RJFZlYB6jDFGaDcpoRTOklRwd1k_cizqZQ7fxJtfzeFS7wnR0x_9aujvuALwBo1xgduI2b4kWExvX6FG-Sl68HlxVNF-DE__M81kEIlMcpj15w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=NvWC5YefSTi20EDfrIADZ7ZCl7Pa0EobV_kGwInNB7_8zG3rOYM2FBgGuMA1Wre7Zy6UtwmC6Uc1SHaXpvGY67jiSpqJxvY_8lzQE84LQn2-L2SZmg_ZCwDy5PE9UA4yhqeIZ5WZJ0A3R3O_K9YgE2sk0doNIZR376yS2oPO4M_tnYhhb6srQE_U5aCdl_NG_FrX3d8AdpEOi-9jLUDRddnFCLEthoAfguhBvnRnuxSclYIqyDK53eWhzU6renGYoOS3J2DrvPV_1FkPheH1t1JnEyH5igZSVod33aq0uCxco3ef89wbGg3TS1k_o5PmqAZPiTKwpm9GfYuQOmCdog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=NvWC5YefSTi20EDfrIADZ7ZCl7Pa0EobV_kGwInNB7_8zG3rOYM2FBgGuMA1Wre7Zy6UtwmC6Uc1SHaXpvGY67jiSpqJxvY_8lzQE84LQn2-L2SZmg_ZCwDy5PE9UA4yhqeIZ5WZJ0A3R3O_K9YgE2sk0doNIZR376yS2oPO4M_tnYhhb6srQE_U5aCdl_NG_FrX3d8AdpEOi-9jLUDRddnFCLEthoAfguhBvnRnuxSclYIqyDK53eWhzU6renGYoOS3J2DrvPV_1FkPheH1t1JnEyH5igZSVod33aq0uCxco3ef89wbGg3TS1k_o5PmqAZPiTKwpm9GfYuQOmCdog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیدار عجیب نتانیاهو با یک سناتور!
امروز نتانیاهو با جان فترمن دیدار کرد و طرف با شرتک نشیته بود و سرش کلا تو گوشی بود
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69284" target="_blank">📅 01:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69283">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69283" target="_blank">📅 01:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69282">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromلیوه</strong></div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69282" target="_blank">📅 01:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69281">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69281" target="_blank">📅 01:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69280">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">▶️
تیزر جدیدی از سینمایی Spider-Man: Brand New Day منتشر شده که دیدنش خالی از لطف نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69280" target="_blank">📅 01:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69279">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-jgn4McnGbfkKBqgKnfRKvH0aLELVdkQLtZ-FX3x0IWzLhlqwFq6v_ue7JEEgEvyLaN8Hs3SnUkUqhcd58I1U89XebJtKgEThqXHdY41QyXh7x7dV_OkPvDEosuqA4T7uyHRVBtdpllzWn975-bTZx7DR29-iw_MSbYA_kbIT3qvX1q5ytWNoqAeW-bMXIppm7u_vn4zi4WPGEs1_D51T1h-cZ1toaGDXalYBk9S7HHPl4KX7lNSNIhIg0iW6c-M-6lkh7K96zJIre0pWyDySHC5nvTPdjku0TAOlY3vFGACLe_h8yDYBV8dFJb9-6pqZ9pVSSO7TVHXZ51U01kRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
«آمریکا هر روز یه جنایت جدید انجام میده. حمله به خونه‌های مردم عادی توی جزیره قشم، ادامه همون جنایت‌هاییه که قبلاً توی لبنان و غزه انجام داده.
آمریکایی‌ها عادت دارن هر وقت توی میدان نبرد کم میارن، با ریختن خون آدم‌های بی‌گناه جبرانش کنن.
ولی بابت این کارشون، تاوان پس میدن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69279" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69278">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba260d124.mp4?token=ZjXp0E8KdO1mmPySwHypSWf1r6RYcz2i7GfCf0uQgy4eYWMKzeq0UEhVcMHdgpj16KlX3t3MScoZB_3C1UECdWFpGR8et2AdsroxQNc0tvelP27-ATIucuxtY1P1-CBMndEaxevsuLy-2ZnemH2CDy2ztHEyoKRw6kcuLJjAhzapdndt-zp5L1pyys87q-yrb4OnsEG9-5Il7U5gRGyf1Xo3lnzc0ns-b0Lh-waJ6NFZOUm40ies__UxbYZCFY-DjgtV-iJzCNlxJUYU-rNUKfL7vSYQhJL-2-Cybl3ytAQxRrcJsk376UDxA14Xb4Jp_3-ULnFThgOeSo9UokOAFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba260d124.mp4?token=ZjXp0E8KdO1mmPySwHypSWf1r6RYcz2i7GfCf0uQgy4eYWMKzeq0UEhVcMHdgpj16KlX3t3MScoZB_3C1UECdWFpGR8et2AdsroxQNc0tvelP27-ATIucuxtY1P1-CBMndEaxevsuLy-2ZnemH2CDy2ztHEyoKRw6kcuLJjAhzapdndt-zp5L1pyys87q-yrb4OnsEG9-5Il7U5gRGyf1Xo3lnzc0ns-b0Lh-waJ6NFZOUm40ies__UxbYZCFY-DjgtV-iJzCNlxJUYU-rNUKfL7vSYQhJL-2-Cybl3ytAQxRrcJsk376UDxA14Xb4Jp_3-ULnFThgOeSo9UokOAFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سنتکام:
یک فروند هواپیمای P-8 Poseidon(هواپیمای شناسایی تخصصی) نیروی دریایی ایالات متحده در حین گشت‌زنی در خاورمیانه، برای سوخت‌گیری به یک فروند هواپیمای KC-135 Stratotanker نیروی هوایی ایالات متحده نزدیک می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69278" target="_blank">📅 00:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69277">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUEJnDH9HXr0cieQHnodAj_9-BeXy74jdBGw3-4N5KjIkYN_yhL1XjhLr-zQRuJi2iHnzki6q5CvdBIqnKDBnzhtTtRIR-6xxHqfQfLOBD207ftCAiM-NgcW2s2c-QwmHK0soYcJmap0A0kn1VyBa4yBqsI8Gemf0oqSF-q13VLie2PH-P3OA23S_4pObzx_4_1N8MdV9l2_cbi74bR9mdwEpO7u9ar5f6JGoZ06nWHX1tk3wZI9ZQur9_DRVvts_3LqIaeJRd7KQnnzP8heE0-dcvUIg3Cpn9unR3Z8JvgMlRrRUCD9j0H0lm4nX1G56-Dun-oCafeDNmh4LkYBJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آی‌24نیوز:
اسرائیل کاتس، وزیر دفاع اسرائیل، روز پنج‌شنبه به همراه ایال زامیر، رئیس ستاد کل ارتش، جلسه‌ای برای ارزیابی وضعیت امنیتی برگزار کرد.
در این جلسه، تصویری از وضعیت اطلاعاتی و عملیاتی، سطح آمادگی ارتش و طرح‌های عملیاتی برای سناریوهای گوناگون در عرصه‌های مختلف به کاتس ارائه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69277" target="_blank">📅 23:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69276">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89da715482.mp4?token=MizoIJkJDFPq5VVsjSDHPZTgzZUzNt_UeddQPb7MnKPWyFyc10-SJ0MxHCFHunORBi8oLjhYxAFXmz_FEpsExPNMgbbV-YA2bfGvJyXbh1f5NOss-joIbHcVaBxBeHLQ0eFLrtcIM5_b7Wrh1_lQp2rl3ATKEh2ZwSF92eQn_skgzr8xdqsT7gg86au29WzmpvD-bFigEslbYDC_wCBxOgOQV1yEuHnz8KUN9BllTqhjvR06CI8wOX3YcuAlLzj77keog4sSuvjSRH_D9eNoL4bXmYrndWSXB98mCIzBrfIJ_3xCsBJcauWwsQmtIvzB8Apl_L3zhyhLj9KzA_BauQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89da715482.mp4?token=MizoIJkJDFPq5VVsjSDHPZTgzZUzNt_UeddQPb7MnKPWyFyc10-SJ0MxHCFHunORBi8oLjhYxAFXmz_FEpsExPNMgbbV-YA2bfGvJyXbh1f5NOss-joIbHcVaBxBeHLQ0eFLrtcIM5_b7Wrh1_lQp2rl3ATKEh2ZwSF92eQn_skgzr8xdqsT7gg86au29WzmpvD-bFigEslbYDC_wCBxOgOQV1yEuHnz8KUN9BllTqhjvR06CI8wOX3YcuAlLzj77keog4sSuvjSRH_D9eNoL4bXmYrndWSXB98mCIzBrfIJ_3xCsBJcauWwsQmtIvzB8Apl_L3zhyhLj9KzA_BauQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند روز پیش یه پسر بچه به اسم امیرحسین رو آورده بودن صداوسیما که اینجوری جواب سوال مجریا رو داد
:
مجری:
منو عروسیت دعوت میکنی؟
امیرحسین:
معلومه که نه
مجری:
کارشناس برنامه، خانم دکتر رو چی؟
امیرحسین:
فرقی نداره، اونم نه.
مجری:
مامانت چی؟ اونو که دیگه دعوت میکنی؟
امیرحسین:
وقتی زن بگیرم مامانمو میخوام چیکار
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69276" target="_blank">📅 23:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69275">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=E4JVqhuAe32Exf_E2nbTTHpxaSbBr2p-ZneLycmxxXwYZfNPf-uNPR4Cd1C8fSfkN6VfzPe-OZTI6vcEqhEyYiek1wOi8IJdrKqlXht3cfu9Ioi0IBTsGn7u4jRCjOn2wSSTaRnGJBnezs1QOh_YOR6DDnbie4I61g_YgV00aholN1u--f-mAakEa-WfUsBut9NCNv7ACjNlwqHwbX4mLy1G1QedpxiIKGbJ3fYuQfRDYzp8pPp0nL3CeI7KMYCqAQxPJAqQLZGgMup8wkNQwsvNlkHbw3j__RdT9lJwHNGoHYUJCNUioIKw7IXr2V1JDWpZk8yHTW0_inpOZidHxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=E4JVqhuAe32Exf_E2nbTTHpxaSbBr2p-ZneLycmxxXwYZfNPf-uNPR4Cd1C8fSfkN6VfzPe-OZTI6vcEqhEyYiek1wOi8IJdrKqlXht3cfu9Ioi0IBTsGn7u4jRCjOn2wSSTaRnGJBnezs1QOh_YOR6DDnbie4I61g_YgV00aholN1u--f-mAakEa-WfUsBut9NCNv7ACjNlwqHwbX4mLy1G1QedpxiIKGbJ3fYuQfRDYzp8pPp0nL3CeI7KMYCqAQxPJAqQLZGgMup8wkNQwsvNlkHbw3j__RdT9lJwHNGoHYUJCNUioIKw7IXr2V1JDWpZk8yHTW0_inpOZidHxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نقدعلی، نماینده مجلس:
با وضعیت حجاب میخوایم چیکار کنیم؟ والله جوابی برای خدا نداریم.
یه نماینده مجلس به من گفت از درد بی‌حجابی هر شب تو خونه گریه میکنه و خواب و خوراک نداره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69275" target="_blank">📅 23:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69274">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbPsQsEVkNz9xGHFrVecsYFoobWugQwnqydtiVyE4i8wQy-nEtzORAikhRLOd-kqVBuGfvgIwzxo5PZxfZd8j0FHxOxDEBLLGoSEHxjj9BpGjLf6Kf-6bHJL5vd0Zx_SmvQeMhzWCj6tK_qOJF-EhBx-FssLtLqyRY5-1hA5CsyTjgbjGPWwwl7kMM8C8KCmTB5tYvnYakZFVdI_sPk43YvgjkCxNLEH9QOtE3RlHsmpAhON3URyV4aDFnIjNFLnmlugsF32Be67o7TCDcOVgCXGNQZ79SN2fNyZEsF7n8QXl5oj1QLpwRl_Yn2E6KQPgrqYInS1cYZvBInTTPk1-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعدام می‌کنید؟ به‌به چه کتلت های تر و تازه‌ای داریم امشب  #hjAly</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69274" target="_blank">📅 23:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69273">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=ESpWshazxF0XtRX3D4ET_Y-o6KnPRpcblGphqvzGUvhVN2e0a3hyw6txk6Yc4H-NoCM4R2K599BaWxao6rhwASaBN3xq9h_IgwQXVbUguG0DFSFUuHJreeBCQOFMy3arFEkSqqelQrVrVDpPq4hpchb8gYCqfjyhnb5rZqmq6nbv2H9RACbkxnRoAz59YMLc_HO1v4IwFyKM8Y_KKPenrgcfcMlcb0txcnM-5HZpoGu4BYUtF1RPbhq2R69azTShVEb3hKiIBx5uvP_AsvRXFUIB6Ozc6k5ouXNwSeYGSY8XZ-5WG36NSjYBSl8Fwp-wslz5waa4yEoY9BRSSR7ZhjyFT6gMZv7Z4-rRHzr9Oyel3rjCum-sVWMBAgobXboL3-kApL9ZmkR73-NPMF_3Mvp8LFLvvYh2nByIWOSiMAIsf_s9iCBQ-s1xIZ0lLOKaFhKqbk27VwONs1Hql7PpTs6lM4mPFU2BWEj36tosatrNUIbGzLxoZ69s7K3MFMckb-EfE96JpY3ypw_g6oa5T5q7n5CgzWh0cz_PQroNIu1sOBF3LD_xRtfhqkwNIb-xaENBzBRgyRfmBHl9AaUVTEdj_GAc3289Ef2lipikT-oq3tI70GD0yCPYG-0Lo6QBW3PaoPWBFg39MSB08kjOQJxIVcdGnP8q04pBtULCsOo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=ESpWshazxF0XtRX3D4ET_Y-o6KnPRpcblGphqvzGUvhVN2e0a3hyw6txk6Yc4H-NoCM4R2K599BaWxao6rhwASaBN3xq9h_IgwQXVbUguG0DFSFUuHJreeBCQOFMy3arFEkSqqelQrVrVDpPq4hpchb8gYCqfjyhnb5rZqmq6nbv2H9RACbkxnRoAz59YMLc_HO1v4IwFyKM8Y_KKPenrgcfcMlcb0txcnM-5HZpoGu4BYUtF1RPbhq2R69azTShVEb3hKiIBx5uvP_AsvRXFUIB6Ozc6k5ouXNwSeYGSY8XZ-5WG36NSjYBSl8Fwp-wslz5waa4yEoY9BRSSR7ZhjyFT6gMZv7Z4-rRHzr9Oyel3rjCum-sVWMBAgobXboL3-kApL9ZmkR73-NPMF_3Mvp8LFLvvYh2nByIWOSiMAIsf_s9iCBQ-s1xIZ0lLOKaFhKqbk27VwONs1Hql7PpTs6lM4mPFU2BWEj36tosatrNUIbGzLxoZ69s7K3MFMckb-EfE96JpY3ypw_g6oa5T5q7n5CgzWh0cz_PQroNIu1sOBF3LD_xRtfhqkwNIb-xaENBzBRgyRfmBHl9AaUVTEdj_GAc3289Ef2lipikT-oq3tI70GD0yCPYG-0Lo6QBW3PaoPWBFg39MSB08kjOQJxIVcdGnP8q04pBtULCsOo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کویتی‌پور، معروف‌ترین مداح دوران جنگ ایران و عراق، دیگه حتی مداحی گوش نمیده
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69273" target="_blank">📅 22:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69272">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcxD3gHylBdltS7-z2FzbdSblFwvrryUX0SCyMOV83nU76OXxeVh8xovRXchGcESvaF7ZXTELAZQ6Q76BZ0TIlgk_JQromIwQicBtSilP_9x3aqaCgRu6U4piVDCUlqmLDfIxFUwlkCzEHphmKlQjSJfSSXXq6LkqhfKYUXy4JaxoHRmF3k9lHFiQwQTmX9OZ02GK_6FQYf5cb3GI_KSiBw1rfWihv4sVHRYnQ2FQUgc023XU4FFUJMy5rm4BpTlv7O-xnR4P9UaQ-IOZguP3f9Nk64RNDuuUhJfVyMMkNtUzEVqmAEuiuylGkXYQRUKRtJNchFLdnKBhWAU2NCIEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :  روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است. طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.  ظاهراً مقام‌های روسیه هنوز…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69272" target="_blank">📅 21:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69271">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o3D_aSjMu6hcimYnpDq_vb_1zcNVKaFw4PBQJoK0dVtOcPd46rzHKTYnY8zXKwRnU_T8IB6kj7zyFzeBeYjpUkHvDRU32q3tRXPBJHKTD6WDp1AVYlyjx21TN2HQU0UgmYk7tXUbJGRXn05IEfyRuIQMRMMzpy7pTQsOx4agmjVX3h79ZDvjpr_qMrDHfEXAnY57gfvmx9qDfXeYJCx2BifI243rG4ek3lxQDXoyiFrtj3yWvHZVgM85pHgD9h37faQ2Bb75bCV_LyecJacFqMurF-Az-pAOgUmCorjCx_yO32uHEO4O_f05sFwjN69FOIZ8SQn5QjKGhY4XNydg6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :
روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است.
طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.
ظاهراً مقام‌های روسیه هنوز نمی‌دانند که چه کسی می‌تواند چه کسی را از اینترنت محروم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69271" target="_blank">📅 21:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69270">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=aKfwenQoRhZmgr63_e5QNrDWY-CKDiSg4bpq38szTfchGXsnc3JSpd8t6VOMfGpg0thrZ1cs3Kw_hSf7CNUvjSY7PukHmnCTgj-PBlXOR46DostSjhSEbDg2dmLPLsJ7iVCY_3lpyevBpyCf9O5T-yU56Vi8knIRlOIYWsdx89NW4ylQ36juITr37VphfVqZpx3mtU279PZf8VNF93l-QbWisfc_3abGDzUdiEw7Yr0rNT-Nmz_a80UAufuW2c65WGaa5jKkpsDM8Nagt2DBVlQFubAzay6Fz1GnHzdYRG6nEusdTZecUy6wkurWznxaEaEDNmAWGMygBw9rZgp4Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=aKfwenQoRhZmgr63_e5QNrDWY-CKDiSg4bpq38szTfchGXsnc3JSpd8t6VOMfGpg0thrZ1cs3Kw_hSf7CNUvjSY7PukHmnCTgj-PBlXOR46DostSjhSEbDg2dmLPLsJ7iVCY_3lpyevBpyCf9O5T-yU56Vi8knIRlOIYWsdx89NW4ylQ36juITr37VphfVqZpx3mtU279PZf8VNF93l-QbWisfc_3abGDzUdiEw7Yr0rNT-Nmz_a80UAufuW2c65WGaa5jKkpsDM8Nagt2DBVlQFubAzay6Fz1GnHzdYRG6nEusdTZecUy6wkurWznxaEaEDNmAWGMygBw9rZgp4Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔝
سنای آمریکا به طرح قطعنامه‌ای برای توقف عملیات نظامی علیه ایران، مگر با کسب مجوز از کنگره، رأی منفی داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69270" target="_blank">📅 21:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69269">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=MqcDt6-UdhoGF_TnqCIahQXMIk_7IRwOBhMH2cyF0CQyBP55auIpARcusjE7uTy3fduAr_E1nMVx9uYv6PMSosu500dKf5KnYpCNQumrbWcR8VNhazwZMeJ2gjy5Wwi7qE8-VKpj_ZZbL1ew1p9XX-qJecnETZAAZc4NryMufrgMDxoEGuFlvrGWOLvmfGTMq4RA-Ega6Dqc3BY92f0BxKIwoUYQnLD7svEdQ-D3CqPsMlAiu2Ik61mVxKZ_oz962w95a90NX1DGufWVYiZU8Qc25l1i3KM8R4wAMT-5jkZ5ArVlgD7Q756vQsbqyE3iaLfyz6dks0FgmXgJ2yYEag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=MqcDt6-UdhoGF_TnqCIahQXMIk_7IRwOBhMH2cyF0CQyBP55auIpARcusjE7uTy3fduAr_E1nMVx9uYv6PMSosu500dKf5KnYpCNQumrbWcR8VNhazwZMeJ2gjy5Wwi7qE8-VKpj_ZZbL1ew1p9XX-qJecnETZAAZc4NryMufrgMDxoEGuFlvrGWOLvmfGTMq4RA-Ega6Dqc3BY92f0BxKIwoUYQnLD7svEdQ-D3CqPsMlAiu2Ik61mVxKZ_oz962w95a90NX1DGufWVYiZU8Qc25l1i3KM8R4wAMT-5jkZ5ArVlgD7Q756vQsbqyE3iaLfyz6dks0FgmXgJ2yYEag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📚
عمران عباسی، عضو کمیسیون آموزش مجلس
:
قطعا تو مهرماه باز شدن مدارس رو نخواهیم داشت.
چون برگزاری آزمون‌ها تقریبا یک ماه تاخیر داشته.
حالا همه تلاش‌مون رو می‌کنیم که اول آبان یا تو خودِ آبان ماه مدارس رو باز کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69269" target="_blank">📅 20:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69268">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=IcADLEpyFDv0Zd1WCJlYSymZk-ST343KSgJOhcwp_SBsPz-NMNC32L1FJyU3kGHys-7hs2y-s5k_yPBpf4qPwGErZYQX7S7hKzFKXpFtFmhLhq-WR-KFlAinb5LEa6PNUrdKvIr1MWnDrBQ1L3t3yb3mCeNLdDaU6eHMZ5CTb7a6Pw8ODuBFqs7t-UtTI74HxtOwS_z9cjnM8uOx1JytI0zynSlHis6H82iVEAA2A67va40Hzfgz6z1uH3oKCyrssqR8F36ym-2BfHD68KxQ7mIz2n9Lgkd2GSTadbQFLmV2YqA6Pld1NfKBgZpmIgBDLuWILs1cUOKJYq9quz2sOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=IcADLEpyFDv0Zd1WCJlYSymZk-ST343KSgJOhcwp_SBsPz-NMNC32L1FJyU3kGHys-7hs2y-s5k_yPBpf4qPwGErZYQX7S7hKzFKXpFtFmhLhq-WR-KFlAinb5LEa6PNUrdKvIr1MWnDrBQ1L3t3yb3mCeNLdDaU6eHMZ5CTb7a6Pw8ODuBFqs7t-UtTI74HxtOwS_z9cjnM8uOx1JytI0zynSlHis6H82iVEAA2A67va40Hzfgz6z1uH3oKCyrssqR8F36ym-2BfHD68KxQ7mIz2n9Lgkd2GSTadbQFLmV2YqA6Pld1NfKBgZpmIgBDLuWILs1cUOKJYq9quz2sOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
حکومت از امروز یه طرحی رو شروع کرده که بتونه فضای مجازی رو به صورت کامل به دست بگیره؛
طبق این طرح؛ قراره بلاگرها، اینفلوئنسرها و بقیه فعالای فضای مجازی ثبت و ساماندهی بشن.
در عوض می‌تونن از مزایایی مثل بیمه استفاده کنن، اما از اون طرف هم قراره نظارت روی محتوایی که منتشر می‌کنن بیشتر بشه و هر کسی خارج از چارچوب قوانین جمهوری اسلامی فعالیت کنه، صفحش بسته و با برخورد قانونی روبه‌رو میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69268" target="_blank">📅 20:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69267">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=oXrHfeqV2s0UU-Irhs_RNosN-sV1ggQWDORH1ZZhCuiQ2w47Qsb04k__7mvZd1mx7CbrwfWzon9ELPymh9VZJgSNqrQm7avxM7Y2m58Slc37S44jLHUUlKLnEfo2E-fBNp62qQqKKuv6TD8uCzE8vcSutWxvxEO6UjnenWb1GTn1Yo5hLGTPbEDW-R9-rbuWLdQSQzaCtrAhBsY4HRhDmx6lfP0jZJe7kPSaWOWvdlvjj0fyqUGEm2Uu5WhHggI1NPP2HXxP3lW2V8wbyg3nU16SqLF045XmzQph2Hfe1TueT760ohKvd3r_twk8ENE-qwhtVoGaEWH4dZCPGrP4Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=oXrHfeqV2s0UU-Irhs_RNosN-sV1ggQWDORH1ZZhCuiQ2w47Qsb04k__7mvZd1mx7CbrwfWzon9ELPymh9VZJgSNqrQm7avxM7Y2m58Slc37S44jLHUUlKLnEfo2E-fBNp62qQqKKuv6TD8uCzE8vcSutWxvxEO6UjnenWb1GTn1Yo5hLGTPbEDW-R9-rbuWLdQSQzaCtrAhBsY4HRhDmx6lfP0jZJe7kPSaWOWvdlvjj0fyqUGEm2Uu5WhHggI1NPP2HXxP3lW2V8wbyg3nU16SqLF045XmzQph2Hfe1TueT760ohKvd3r_twk8ENE-qwhtVoGaEWH4dZCPGrP4Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آفرود سواری هم تو ایران ممنوع شد؛سازمان منابع طبیعی:
از این به بعد هر کسی بدون مجوز یا خارج از مسیرهای مشخص وارد مناطق طبیعی بشه، باهاش برخورد می‌کنیم. اگه هم آفرود به‌عنوان یه ورزش به رسمیت شناخته بشه، براش دستورالعمل و چارچوب مشخص تعیین می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69267" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69266">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=asUybxu1EgJrfN25tDdO_JMxCe7_TSsBpMGtHw8GsOmoeTcUmJx7L0P2VkWbOR0R-6NRdMvaie-Id8Aw4r2CRp4Ty7ImVL5F0kYb-oaeOTvAs5oaAkxycZYCApCZByT2BaUvapiVyCoKlWGSQ5ZTbc3GHdmOYyrD9smW7WT87JmWfbRYh-8Dq74RNnBfbNj8CH80T1uWgeNRuCpXkIfy89nUM97_Cc5LBMUtEQfSaTcM_wYi5WVGlWYjO45JBF6ZmXzlDWyKcbk1_hiP5DaGVFXG7iPMzCg-g-_xFgx94KFPgmuuPs6CaNcjgdm-HKAjLpzWDcabIddkDZ7nVpl_8Gtk89ORLtNLS9KOhO2fyhYYNPReqwGaInFqlxAsf-wf7FpxovBISjdZkqM-lvoMGCYJswhjzhaxaGG3Qwl0f4ZkbHVAhahZPs9oKIRSbikoulEU93ev3n1RCLPwYySdA1DaOvb_fArsBB91Oo30LrZ5yatsXkg6fpWA8fX_cSsU1FPR_LOBXKt0l2SwT_Ske9qWSq63mQ1tS3kxE2Mtwmk_icH5qict3ZpR6ngeSCejZPH7xp15fanjElTjXtWqWw18xYgl7rbSfJp92YsUxB5UrWcTJ8MRgyUZqMz00nWO2PzYv6YNn3O8qebdHQ6jWHV_oVao0ee9IuFOuXe2AG0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=asUybxu1EgJrfN25tDdO_JMxCe7_TSsBpMGtHw8GsOmoeTcUmJx7L0P2VkWbOR0R-6NRdMvaie-Id8Aw4r2CRp4Ty7ImVL5F0kYb-oaeOTvAs5oaAkxycZYCApCZByT2BaUvapiVyCoKlWGSQ5ZTbc3GHdmOYyrD9smW7WT87JmWfbRYh-8Dq74RNnBfbNj8CH80T1uWgeNRuCpXkIfy89nUM97_Cc5LBMUtEQfSaTcM_wYi5WVGlWYjO45JBF6ZmXzlDWyKcbk1_hiP5DaGVFXG7iPMzCg-g-_xFgx94KFPgmuuPs6CaNcjgdm-HKAjLpzWDcabIddkDZ7nVpl_8Gtk89ORLtNLS9KOhO2fyhYYNPReqwGaInFqlxAsf-wf7FpxovBISjdZkqM-lvoMGCYJswhjzhaxaGG3Qwl0f4ZkbHVAhahZPs9oKIRSbikoulEU93ev3n1RCLPwYySdA1DaOvb_fArsBB91Oo30LrZ5yatsXkg6fpWA8fX_cSsU1FPR_LOBXKt0l2SwT_Ske9qWSq63mQ1tS3kxE2Mtwmk_icH5qict3ZpR6ngeSCejZPH7xp15fanjElTjXtWqWw18xYgl7rbSfJp92YsUxB5UrWcTJ8MRgyUZqMz00nWO2PzYv6YNn3O8qebdHQ6jWHV_oVao0ee9IuFOuXe2AG0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده‌یاد مانوک خدابخشیان:
"اگر رژیم مذاکره کنه باخته و اگر مذاکره نکنه هم باخته"
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69266" target="_blank">📅 19:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69265">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=lVGrkgrwP8pW15USyxGS1c4CrWXTf48X4aWuOYZBd2Axl4po5jUEr_0ffvVzA49LoCmbG0X3Ppxr4b4WXwhntEEz0cfFVH4Y8WW65bcM13IvD1jceo1S0IHI1gZxeq7rxet37AcKSHD3apGr99GKaPBpr0Hh93_Wd3qjZOKjsJs2G8PmMDbrneIyiLoKAbCBmdyyWdN_TT8cbcPtUGb3nrY9wDZFsZSfSwJ99B1evL96K8HU43jSek4iJTuCUCV-jwuw9I0_CYKDiajjzPGuFs_7WbXu5CWHz5t6kYXiCLQsl1z1oJLEM52qiU0PqzFJYEaZrvidzMh8B77M0EedDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=lVGrkgrwP8pW15USyxGS1c4CrWXTf48X4aWuOYZBd2Axl4po5jUEr_0ffvVzA49LoCmbG0X3Ppxr4b4WXwhntEEz0cfFVH4Y8WW65bcM13IvD1jceo1S0IHI1gZxeq7rxet37AcKSHD3apGr99GKaPBpr0Hh93_Wd3qjZOKjsJs2G8PmMDbrneIyiLoKAbCBmdyyWdN_TT8cbcPtUGb3nrY9wDZFsZSfSwJ99B1evL96K8HU43jSek4iJTuCUCV-jwuw9I0_CYKDiajjzPGuFs_7WbXu5CWHz5t6kYXiCLQsl1z1oJLEM52qiU0PqzFJYEaZrvidzMh8B77M0EedDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
سنتکام:در ساعات گذشته، رسانه‌های دولتی ایران به انتشار ادعاهای نادرست سپاه پاسداران انقلاب اسلامی (IRGC) ادامه داده‌اند؛به‌ویژه سه مورد زیر:
❌
ادعای اول: سپاه پاسداران (بار دیگر) مدعی است که مسیرهای آزاد و باز در تنگه هرمز برای کشتی‌های تجاری خطرناک هستند.
✔️
واقعیت: خطرات فوری که کشتی‌های تجاری و خدمه غیرنظامی آن‌ها را تهدید می‌کند، ناشی از تهدیدهای لفظی و تلاش‌های سپاه برای انجام حمله است.
❌
ادعای دوم: سپاه پاسداران مدعی است که سه جنگنده رادارگریز اف-۳۵ (F-35) و سه فروند هواپیمای دیگرِ ایالات متحده در جریان حمله اخیر ایران به یک پایگاه هوایی آمریکا منهدم شده‌اند.
✔️
واقعیت: هیچ‌یک از هواپیماهای ایالات متحده در تلاش‌های اخیر ایران برای حمله، منهدم یا دچار آسیب نشده‌اند. تمامی موشک‌ها و پهپادها رهگیری شدند یا به مناطق هدف‌گذاری‌شده نرسیدند.
❌
ادعای سوم: رسانه‌های دولتی ایران گزارش می‌دهند که یک نفتکش تجاری به نام «ام‌تی نورا» (M/T Nora) موفق شده است محاصره ایالات متحده را بشکند.
✔️
واقعیت: این کشتی تجاری موفق به شکستن محاصره مستحکم (دیوار فولادی) ایالات متحده نشده است. بیش از ۲۰ ناو جنگی، صدها هواپیما و هزاران نیروی نظامی آمریکا همچنان هوشیارانه به اجرای کامل این محاصره ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69265" target="_blank">📅 19:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69264">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=SQWQxD80COsxZM7kzBEhb4e4VxuMG7T5zKUy4GuPTMiApFqwrZyGZdvt8q8EZSmBiInP1Er4DoyIip8T5GwAlOtqCb1dw13Esw_lf6rjGzGw-Y-WUoCaF46HAmXbq9bVcI1vPT3w6WpI4ZnzbCbIINP2WXd8Vw9AVdqmhCBRylOuuc7RXQPurbuMsLUX0dXSksMZwI30w-2PMwCoThqYRTtQEC48QH6IJjII0pi9MuJPeOiZ1ZQD00-Fd43yo_DAGHgVNSrm50Zagg-THyqJ-P3dGoJGjuk3iu5ZzkP1rgPYi-Wv0bX2fKisFEVBCcd0svou2ZVWiN-k9rr9FCO1ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=SQWQxD80COsxZM7kzBEhb4e4VxuMG7T5zKUy4GuPTMiApFqwrZyGZdvt8q8EZSmBiInP1Er4DoyIip8T5GwAlOtqCb1dw13Esw_lf6rjGzGw-Y-WUoCaF46HAmXbq9bVcI1vPT3w6WpI4ZnzbCbIINP2WXd8Vw9AVdqmhCBRylOuuc7RXQPurbuMsLUX0dXSksMZwI30w-2PMwCoThqYRTtQEC48QH6IJjII0pi9MuJPeOiZ1ZQD00-Fd43yo_DAGHgVNSrm50Zagg-THyqJ-P3dGoJGjuk3iu5ZzkP1rgPYi-Wv0bX2fKisFEVBCcd0svou2ZVWiN-k9rr9FCO1ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسر جوون ایرانی رفت پشت فرمون ماشینش ی خر گذاشته رانندگی کنه خودشم داره از رانندگی خره فیلم‌ میگیره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69264" target="_blank">📅 18:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69263">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
انفجارهایی در صنعا، پایتخت یمن رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69263" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69262">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-bylJvyGsbdiWQ85IhiwJm0OD9q3ERz6-uiis0JrKka9YhZL94xx5mJngNv5b1ChVKXLPRKU9kmPR0JyvJZoEwhLcw4qupC2UVIabKJVrSt11ALJ3N5qCrH-eDyH6JZ4CvpnjQOFFTug_euw9HISuKJRqNr7XFPvs_rSnS7FKds8UrKJO5gWwJBn9keLfrpu4DDSmOoIqyr0FC_zR3It_OcY3WToeHGEMgLYFyecWwQoofGuNeyrWuPZNyVU_3rcSjlAEUrqtvdnIsaRAT7S3bZv8JcQh_JJ-JAo92THdWEnYrlesmptAYdC4cUujfVrq7c0wfcmD5ogtocYYdQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه تا از تروریستای مفعول حشد‌الشعبی که در حمله مشترک آمریکا و عربستان به عراق کشته شدن!
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69262" target="_blank">📅 17:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69261">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYj2uDZdxuB9WUMjDEXDk0GODgOnFkyZlYdpKh_2mWAGpLRo4Mr_Y8gHIjk92Iu1o6UjVr6RrTFI0pNam4fd7JY03sHO_eOpPNfXE0AIswyZP3C57slxkqUU65gDGQW80IOQZ6GcpnVSUSMmuzxMvIiE3M_DOF-BKSOOfyLPh-rZKPjUomL9-exu4lqqELKv16WFAOLTSqbXNq-HLMcJbZbycgLEfpTQnZF4BzbMu8gpKRinZzj90hNHfbRq44UB26h0aMtf4BL1WvRpx6KmjJGWoYfpXsVpP2UXeq3oG9sf4JcbSvFTwRR9hpBmrXXqCQXo0kBgek4ooBSboozTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران؛اطلاعیه شماره ۵۶:
دو آشیانه پهپادی و یک مخزن سوخت هواپیما و بالگردهای نظامی در پایگاه علی السالم به آتش کشیده و منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69261" target="_blank">📅 17:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69260">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=hCOUfUQ_17Vzuw-8NWPN16Q3joZzNjjfpyESUG1BxPjOx5DieO4ul4hH8Z1nihXv0E2tr7ojNq_6FkCT7yvweZmd_1m0uXr8gem0UopsmOJQazjOFf3sRbtnFz-LWFV094gMHcJrdxrbcWgVhOB5P7w5wNMKMGUvx5QT1VuuHAKbuF_hNimU_SD_k97kTLCO9vkbzLU64_HDXJUJejHVVKTVaplPExFFK4Z-xY_TYbdeKlF7akarO4sGOeca75E9vmLjVKoEZP2xXJJijxpKn7gHt85Kuad6MJ4pHJ73vnWCiVVkix8hl7txZ9UgZKpMz163TZIiMuKOcLmQuTvcbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=hCOUfUQ_17Vzuw-8NWPN16Q3joZzNjjfpyESUG1BxPjOx5DieO4ul4hH8Z1nihXv0E2tr7ojNq_6FkCT7yvweZmd_1m0uXr8gem0UopsmOJQazjOFf3sRbtnFz-LWFV094gMHcJrdxrbcWgVhOB5P7w5wNMKMGUvx5QT1VuuHAKbuF_hNimU_SD_k97kTLCO9vkbzLU64_HDXJUJejHVVKTVaplPExFFK4Z-xY_TYbdeKlF7akarO4sGOeca75E9vmLjVKoEZP2xXJJijxpKn7gHt85Kuad6MJ4pHJ73vnWCiVVkix8hl7txZ9UgZKpMz163TZIiMuKOcLmQuTvcbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی وسط خیابون بعد از شلیک دو گلوله به پا؛ این همون شخصیه که تو لایو دخترارو کتک می‌زد و...
⚠️
‌ ‌ ‌
حاوی خون و خون‌ریزی
🔗
‌
مشاهده ویدیوی کامل بازداشت
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69260" target="_blank">📅 17:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69257">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=EiACp6k7Fvx5cPIpvmAzZho7T6ZnaRSQAfL2Naq8uPgFY-rgNJ5MGm_A4DH7F7w3EhaSQdMPBPy7VTE6wx07urPSQNJss62MNoPJ2W6j0PqHy1y-xLso44KE_0V3k0hJh9aWTSy_ddgBs-TUgsctDFrGfqnoEu8arBZpgXOR7z-LkzGZ6t1FLkSmuvh_GuBT5EwULfXdPQQhwF9xHjjgmzyso5_4lYFqgIKkzaOW5NmiFSN9rUQ2Bb7-XVlUXACao8sjMpJBHQQdeHOIhl_JCzd_EEZb9UEDEfdK9cfpOVsyIzhPMmmWFIJXDKMkvKDTTQBupVsh1BzMcTiaQPg9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=EiACp6k7Fvx5cPIpvmAzZho7T6ZnaRSQAfL2Naq8uPgFY-rgNJ5MGm_A4DH7F7w3EhaSQdMPBPy7VTE6wx07urPSQNJss62MNoPJ2W6j0PqHy1y-xLso44KE_0V3k0hJh9aWTSy_ddgBs-TUgsctDFrGfqnoEu8arBZpgXOR7z-LkzGZ6t1FLkSmuvh_GuBT5EwULfXdPQQhwF9xHjjgmzyso5_4lYFqgIKkzaOW5NmiFSN9rUQ2Bb7-XVlUXACao8sjMpJBHQQdeHOIhl_JCzd_EEZb9UEDEfdK9cfpOVsyIzhPMmmWFIJXDKMkvKDTTQBupVsh1BzMcTiaQPg9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
حملات شبانه سنگین روسیه به کی‌یف، پایتخت اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69257" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69256">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=H6Es2S7_TqoIAtsvO5obVB6grslvU_69dsQEVeLZGR7bQMvdUYfNDDqABCMXBCisPM9XhIFLCR9clcIwAtPdtWrFM3e3lsDroqfBfHQuLWvHWyTuq_0urphQIaPU9gDgt5hOfpSGwFOcSJvdZOl7fQflfX6SXGjoWSixv4ePqkw87kmSC2kG2onL2KHAEPkWlm_2oAW1tipbwHqGi_7Nm_oCrjnU9oIE6MzfLMvxwD7pJ8zvysQyw8VRhB27dUfYPFB-epaezJD-bR9hXFYmNu5h6HKFg8PSDoeD-4OLPoLp8ykdGEGyRMWGwhciAQWGyadIYO2PURaww_ca6Jj1JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=H6Es2S7_TqoIAtsvO5obVB6grslvU_69dsQEVeLZGR7bQMvdUYfNDDqABCMXBCisPM9XhIFLCR9clcIwAtPdtWrFM3e3lsDroqfBfHQuLWvHWyTuq_0urphQIaPU9gDgt5hOfpSGwFOcSJvdZOl7fQflfX6SXGjoWSixv4ePqkw87kmSC2kG2onL2KHAEPkWlm_2oAW1tipbwHqGi_7Nm_oCrjnU9oIE6MzfLMvxwD7pJ8zvysQyw8VRhB27dUfYPFB-epaezJD-bR9hXFYmNu5h6HKFg8PSDoeD-4OLPoLp8ykdGEGyRMWGwhciAQWGyadIYO2PURaww_ca6Jj1JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
صبح امروز ارتش آمریکا به یک پایگاه پدافند هوایی سپاه‌پاسداران در اهواز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69256" target="_blank">📅 16:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69255">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=TbRQO886i4V_LQVV2kdwevnoS_tC6KnMIGvM08SEdyBaujyDHBSEMUDtuLBuTbtQWBIRXXikAT98whSTx8OlYbZ1KAjZq1RqE7LGpTSi22EC0cItZ-4nkseSGk_v2ERJ4yKhyBCeA4VbPFEaDy3nJ20q2aNx1dOCkqdFQHvG7WyeX_gMjoQi1h--W-2OA6meu1IINN62It0IIrX2z7oZMj58titNXmpI8-hanikW_86UKt_BZ4ZAC-KZaqAZxjvWVmjEGn3fqRhkiMWXX2quA7Yp7vdhT8izgAXfOG3kNIhKETxEgF23X_V3RhU5KaKn_nL116GSbi4g0kA_Ys1LDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=TbRQO886i4V_LQVV2kdwevnoS_tC6KnMIGvM08SEdyBaujyDHBSEMUDtuLBuTbtQWBIRXXikAT98whSTx8OlYbZ1KAjZq1RqE7LGpTSi22EC0cItZ-4nkseSGk_v2ERJ4yKhyBCeA4VbPFEaDy3nJ20q2aNx1dOCkqdFQHvG7WyeX_gMjoQi1h--W-2OA6meu1IINN62It0IIrX2z7oZMj58titNXmpI8-hanikW_86UKt_BZ4ZAC-KZaqAZxjvWVmjEGn3fqRhkiMWXX2quA7Yp7vdhT8izgAXfOG3kNIhKETxEgF23X_V3RhU5KaKn_nL116GSbi4g0kA_Ys1LDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی حرومزاده چهل پدر وسط خیابون:
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69255" target="_blank">📅 15:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69254">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=goEVbw4PE5kL_4Dwed_ysLRCVTvbOoJ8xsI2RQUI02QDg5i3jGNLA5sVjBt-nxCJeTvOPnDxrY_4Fq_DiOANm9m_M03b1sgfL71ZZNGd_ryu3eoV07VMt3wDgCbmiMmAcJAQnOLyGMQja1Om5W5e7Vezk0IXRJ1EakQeYTOvuYqwQwtZCaf41zWS2TQNS3BQiN7c1X-LdLx91stAmr-6RvwmBPv6gE1OtiLbfK97srtMduEXJmmrsSMIPL5cCR3JI7rreLQaL1ryxdFJHsF5piZ69mvM9870JcknyTvWJDC-sKJJWLpEpbtviGhE4rffW1lvk1nmhfsFzD94D7qtqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=goEVbw4PE5kL_4Dwed_ysLRCVTvbOoJ8xsI2RQUI02QDg5i3jGNLA5sVjBt-nxCJeTvOPnDxrY_4Fq_DiOANm9m_M03b1sgfL71ZZNGd_ryu3eoV07VMt3wDgCbmiMmAcJAQnOLyGMQja1Om5W5e7Vezk0IXRJ1EakQeYTOvuYqwQwtZCaf41zWS2TQNS3BQiN7c1X-LdLx91stAmr-6RvwmBPv6gE1OtiLbfK97srtMduEXJmmrsSMIPL5cCR3JI7rreLQaL1ryxdFJHsF5piZ69mvM9870JcknyTvWJDC-sKJJWLpEpbtviGhE4rffW1lvk1nmhfsFzD94D7qtqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت صداوسیما بعد از هر حمله آمریکا
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69254" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69253">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.  ۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69253" target="_blank">📅 15:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69251">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C-KxsF8sYGnQRsUxDIBUz0Muuleo3CGCUUnX7NY91EnrxWjAWfGzFFSepYUk83AJ1OyPOn815_lzkoLByJMIemUubB0jX4B0GwrYgvVreYyhtrKl7wuVACHsNDH6e0lRszO77HHhstLxFYpi2Hy_zpKNkE5FcQaHbVc7JecZty2U0AnLVolwdanc4iI88jJYe9iQUSpxU44MTmIJ4_U2Df6-r6liReddCYNCpuUD2hF4bPQe9bNGHj_-7L-tydOwAwSP7it53K0mlPlwBynl6rTf7GlZwvjd24voB1rJc0Mp2OMx4HXkrDKAx6LF4KLhcclreDgC9EW5CNfPGJBAIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=o2G4gjLhXl9j7ctf6McAaGhxR5lulS1zSjI_HpEFJY6Gd0UTxDUsd9w7Z6YQjgi7IPhx2_i3laC_8eV4yPupMgQAoFI7LTyNulkNWMv-8XOeCW03w1oqc9f22wLrAglRmEN5TaktyWfYgHssAsiLV7B1Am4gExuVrCbIWpkyjYrBPsSNZnwtRAV1Ks_qnPScH64GFfjiJMMLT5V0lYrQuUUVW-aS3NxkcCn4wNHwPb_16gzDx8UjW1Z_G16oEfu4IkHUmyhiBR2K6AZZe4b6XjgpHQQeB22pvaaayrhVDxxwFFFE2wDcy814SaCcQkTFPBbW5fFXTjz1N6519VpHrw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=o2G4gjLhXl9j7ctf6McAaGhxR5lulS1zSjI_HpEFJY6Gd0UTxDUsd9w7Z6YQjgi7IPhx2_i3laC_8eV4yPupMgQAoFI7LTyNulkNWMv-8XOeCW03w1oqc9f22wLrAglRmEN5TaktyWfYgHssAsiLV7B1Am4gExuVrCbIWpkyjYrBPsSNZnwtRAV1Ks_qnPScH64GFfjiJMMLT5V0lYrQuUUVW-aS3NxkcCn4wNHwPb_16gzDx8UjW1Z_G16oEfu4IkHUmyhiBR2K6AZZe4b6XjgpHQQeB22pvaaayrhVDxxwFFFE2wDcy814SaCcQkTFPBbW5fFXTjz1N6519VpHrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مادر جاوید‌نام ابوالفضل سپاهی، که توی میدان علیخانی اصفهان اعدام شد:
خطاب به یه نفر به اسم هادی: بگم برات که تیر زده بودن تو پای ابوالفضل؟ بگم برات که زیر چشماشو با فندک اتمی سوزونده بودن؟
بگم برات که ۲۰ روز بهش آب ندادن؟ بگم برات که فکشو شکسته بودن؟ بگم برات که دماغشو له کرده بودن و آویزون شده بود؟
هنوزم تحمل شنیدنشو داری که بگم برات...؟
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69251" target="_blank">📅 14:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69250">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🇮🇷
سپاه‌پاسداران:
تخریب کامل سه فروند هواپیمای اف 35 و ورود خسارت سنگین به سه فروند دیگر در الازرق در پاسخ به جنایت دشمن آمریکایی در قشم.
همچنین چند افسر و کادر فنی و تعمیرات دشمن نیز در این حمله کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69250" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69249">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa6076311.mp4?token=hWVgGUmx9xuMHJr9UWVDgso0cJFZ6705vyWCXzWA1qxtSD-Hz-eWbm8PfSLUY_0-qb4xlWhZ0AElMH0LI7saqslKolekKZCEk49iH_Jj3F3stb0E-E62kO2yC1skkOSCFWsT7MYmUmU_8y_rD_MrPu48ldU2b1-RjjwHjdizlYOE2g3Akyut4-SLBD4_LKiy5CZi8LeIbAgZpym2Nqi1DetUcT4qnt6bNw0oHm9Nb1Np2i6648q3XTsdQDAqd5jo4LMQdyuEMQOenxbsDySceDoH9-DWpj36LYv4I5U_lVYlSRikGVpKmMARGO6rWLC7SozboLlK6_v4buCyCFJSRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa6076311.mp4?token=hWVgGUmx9xuMHJr9UWVDgso0cJFZ6705vyWCXzWA1qxtSD-Hz-eWbm8PfSLUY_0-qb4xlWhZ0AElMH0LI7saqslKolekKZCEk49iH_Jj3F3stb0E-E62kO2yC1skkOSCFWsT7MYmUmU_8y_rD_MrPu48ldU2b1-RjjwHjdizlYOE2g3Akyut4-SLBD4_LKiy5CZi8LeIbAgZpym2Nqi1DetUcT4qnt6bNw0oHm9Nb1Np2i6648q3XTsdQDAqd5jo4LMQdyuEMQOenxbsDySceDoH9-DWpj36LYv4I5U_lVYlSRikGVpKmMARGO6rWLC7SozboLlK6_v4buCyCFJSRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرود دیدنی یک F/A-18 Hornet بر روی ناو هواپیمابر.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69249" target="_blank">📅 14:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69248">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IC8qJJvkmBEfIH1jCyiz-xtf9Pw5oDcnNUX3xd-xcryOs-em4NHQdlLil-y5701g1Yemp25LUvIXXmsu4vyQMgd2olM01ibDFzhGXpYbD-efLc6JxC1xx4wV4_hLdOm8CqbvnKxhnPP9Cvsg8gmaT6oW_CigWHt6xo_v_mlaVlt1KOdRpL6veVOp6u26yGdgDGlwF1HzQ4FOYMIOVmvzpG2ynAIRFOm8ZLEFTxOVR0u3k0EGZuuUjEWIODvQtYRGnBK8wZNOAmwdlUMAlrsyy1Ck-ULC03TdoaDFn82A9a4Lg-guEFfi7UcOF1mDao1PoLkjgKMcMSHmILUN5Ps08w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⏺
ان‌بی‌سی‌ نیوز:
به گفته منابع آگاه، ترامپ در قبال مسئله ایران «به‌شدت کلافه» شده است، چرا که مقامات ارشد بر سر راهبرد واحدی توافق ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69248" target="_blank">📅 13:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69247">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a176457914.mp4?token=MrAasup0gpFxw74U5CvpE61w_Lh-E1NHe1N8tMYD6LDv3sBQYa0sxXF3FNwhLC2oYmct9xzRbf67FzxSUVNp6M5UXuqg8oo0mJT3q6tVYHhUs7GfGFYj3-mOyMc1-BS7n6JE3OEryb1gep_D47gPMk4yTgYt1sodSKiw-NKtBdLdaVTUI6EIYOUYtrWwtPJpJ2LPyyGe-Fe3virMzx_qBXNLNG6YWcqU30-eyClTgH9EoHDRrWWm_tZwmYXkafNY7Koc6tu5jelFMn_A3_2vGL__U3af5Hz4bYbjv9td3X3JljC6C0HvqFLTdXoQW_-jk7Cqk7gYFHAawbuh4qKRJhwy_KLqlqFsWeYcbmBM_bAI2ybGJV5pHrjApjA8dMQjPk4XCr8NexEgdoK4MAP2yjriEI64xG6D96oII_lbs-oT7CcNww6tivF2UCDLDCvEeULkoFbGVXBpwMbSxugi_es-2QPD7EJS-fs_RUpf7lYZQSiw8oKv7OrWw_ytYKLbpXhiKJBqLEfQ7WJygpJk41FGrkVV-jx-VwReGK-6JTExcfRhMBpqOgnz1VvvMJkBa7EQq2vNA6blcent9sQ1RQ9FcNKQ-4BBaoiipdmjHqPg-ashh1ySHcmRxRhWCWwTtUqjYkqM1VnKRNWXArVFiaAlFMYQgH4M06uqMiOyISY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a176457914.mp4?token=MrAasup0gpFxw74U5CvpE61w_Lh-E1NHe1N8tMYD6LDv3sBQYa0sxXF3FNwhLC2oYmct9xzRbf67FzxSUVNp6M5UXuqg8oo0mJT3q6tVYHhUs7GfGFYj3-mOyMc1-BS7n6JE3OEryb1gep_D47gPMk4yTgYt1sodSKiw-NKtBdLdaVTUI6EIYOUYtrWwtPJpJ2LPyyGe-Fe3virMzx_qBXNLNG6YWcqU30-eyClTgH9EoHDRrWWm_tZwmYXkafNY7Koc6tu5jelFMn_A3_2vGL__U3af5Hz4bYbjv9td3X3JljC6C0HvqFLTdXoQW_-jk7Cqk7gYFHAawbuh4qKRJhwy_KLqlqFsWeYcbmBM_bAI2ybGJV5pHrjApjA8dMQjPk4XCr8NexEgdoK4MAP2yjriEI64xG6D96oII_lbs-oT7CcNww6tivF2UCDLDCvEeULkoFbGVXBpwMbSxugi_es-2QPD7EJS-fs_RUpf7lYZQSiw8oKv7OrWw_ytYKLbpXhiKJBqLEfQ7WJygpJk41FGrkVV-jx-VwReGK-6JTExcfRhMBpqOgnz1VvvMJkBa7EQq2vNA6blcent9sQ1RQ9FcNKQ-4BBaoiipdmjHqPg-ashh1ySHcmRxRhWCWwTtUqjYkqM1VnKRNWXArVFiaAlFMYQgH4M06uqMiOyISY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیلم گوه خوردن نوید حرومزاده هزارپدر که دخترا رو کتک میزد اومد بیرو
ن؛
از همه عذرخواهی میکنم ، گوه خوردم غلط کردم!
بذارید برم توبه کنم ، درمان بشم و برگردم به زندگیم برسم.
اتفاقاتی که بین من و اون خانم‌ها میفتاد رو تو ذهنم الکی بزرگ می‌کردم و دیگه کنترلم رو از دست میدادم.
خانم‌هایی که کتک میزدم، من رو درک میکردن و هیچ شکایتی ازم نمی‌کردن.
اتفاقا مردم خوب کاری کردن که انقدر واکنش نشون دادن؛ باعث شد یک بار واسه همیشه به خودم بیام و خیلی مسائل رو کنار بذارم.
از تَه قلبم از همه مردم عذرخواهی میکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69247" target="_blank">📅 12:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69246">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=SEhtZdwXEHtJyLq9fvD0Lk_ZhMIFvvCUpNvSOigBnJRt46GV35hkhjacsslMjl0rqyTEzgk034qQ4PVW9G2g7dGzuoVhuZ8E5PVN30kuAjK5Qwb5NKBQt7bliySDeFk_uiGPTVNihtQbY9xeArCrpbalqd6xfBRFuXfsfbM5z6Q31LqjD-dN5mYLJgeGluG6UpYZLYOYlibI-Qjtuelbs026CpwOUId0FHsjqvj65aTIL-G_qgZrtNFQ7pd_BDRX52aipp28LfBUvzOQohaPnhAjFBqY8dC5mY9FWML2TjeRwLMaEIX7fMHgRDXILM50Xf0eIRleSOchCEJ3WPDCmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=SEhtZdwXEHtJyLq9fvD0Lk_ZhMIFvvCUpNvSOigBnJRt46GV35hkhjacsslMjl0rqyTEzgk034qQ4PVW9G2g7dGzuoVhuZ8E5PVN30kuAjK5Qwb5NKBQt7bliySDeFk_uiGPTVNihtQbY9xeArCrpbalqd6xfBRFuXfsfbM5z6Q31LqjD-dN5mYLJgeGluG6UpYZLYOYlibI-Qjtuelbs026CpwOUId0FHsjqvj65aTIL-G_qgZrtNFQ7pd_BDRX52aipp28LfBUvzOQohaPnhAjFBqY8dC5mY9FWML2TjeRwLMaEIX7fMHgRDXILM50Xf0eIRleSOchCEJ3WPDCmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خبرنگار صداوسیما حین گزارش پرید توی آب و فاز کوسه گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69246" target="_blank">📅 12:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69245">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oksWgglLlbr73bAMwguF2PeIxrDOIi1P8gPiOqDIiTIZGQJYOA5-UQa438l9KgGy_y7q7xU8dXPno61GGOB3G_1Serer8WJTcky2DaVVZc4aFHlMG3LxIIOYK4nWCh2ci7aIAoz-B4dTsUK9iFwWHmCbiSCqclRQ9rWLZp0ZNw4pZuPhH409vWNP1_pN_yJtZHUgwps0A6pRkfk6hqCLcow4rIEhNJ6Qxt3t8J76HAmf0CPVW_56kC_nyHjzo1aKyizVK_YpWYEwefY1e9AVewjks1Hs2z05CWMxs-WhMkCIJKZvEewUHhwtYfLgXpFkrw2eRpcRejJLIcXBr9JiZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
سپاه پاسداران:
متجاوز رو همین امروز تنبیه میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69245" target="_blank">📅 11:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69243">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2yywzId2RsicPsu5uxGpnCeqj2B7oVw-11z86sMvJPiH8D87X6V4qflDbq-GL05ikZZLFoWe62hqS0vvjvnx5lb-01EuOP8Sd6d5jFgNP_M4z9m1O2noE2-MOx5rCuOUHUUsgtpcVz6rpXE07mE9Ym4qkZ9uenbRkKZwAgILNJxi-4RKR6zYFFfeUh6DJfgQM3Bt19wol1gFxyFypRxZQy0ZKCBYRbBnUIFLS2__oRnD0cOM9wGflC_4FgtzVeL_xh4oHkXLrWJVOaSDqUv_9ERCgx1d2s5XA9ohErFyBSHMJLVAf8Z4H5Iv9mX5XuZC49k0UVEJxPD-8g32M0cMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/854dca423a.mp4?token=BZ7nFV9D078MgdaP3tQsh8h5Py3hXaJXqLeTcJgYADz40ySOV_sW52fOnydlXuOoEn7c-Pnyg3BdOF5wiNnfbmKQzM8CVgwiN1vHu8DjuDQdOxd7RaySUkeO9zt-N6gLMBmoSTiKC7z1ykems7B1RiONSonzB2xD8EznNoiLq-4ZPz-JRclNqiDT-fb-ph9-TsP6DARDy_w0cnKI3rR9ZVsE40BKScHJerHxPuVg0lCSkhmDF1KoWdCkeiQRbZlhkT_xlnmIoZMOBCt5DTHaBQLbv_gymyDaCfJQfLBRQeGsdAdSQ3Xs4NmG01G_yIUBRxIJ9xNwumwT0T6A8pfmFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/854dca423a.mp4?token=BZ7nFV9D078MgdaP3tQsh8h5Py3hXaJXqLeTcJgYADz40ySOV_sW52fOnydlXuOoEn7c-Pnyg3BdOF5wiNnfbmKQzM8CVgwiN1vHu8DjuDQdOxd7RaySUkeO9zt-N6gLMBmoSTiKC7z1ykems7B1RiONSonzB2xD8EznNoiLq-4ZPz-JRclNqiDT-fb-ph9-TsP6DARDy_w0cnKI3rR9ZVsE40BKScHJerHxPuVg0lCSkhmDF1KoWdCkeiQRbZlhkT_xlnmIoZMOBCt5DTHaBQLbv_gymyDaCfJQfLBRQeGsdAdSQ3Xs4NmG01G_yIUBRxIJ9xNwumwT0T6A8pfmFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.  هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69243" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69242">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=BcIXjWzXRhhyuxUBxecOcW85wdpEMUFwCdEcYHEJoUOqrUUteSa1mj-7fgdUJeAXmMwQkrdVt32csDhswsGpAwqt-XfgclO6l6NBl4EzEJgaLERFzpNuHCOJRiOf_A136lRcnpHTA7rTIB0pHXq7dtlutQaI0jnNp8232sJqpNFNV0pxaaReah7_zRuK4wqWIVOGWpPz1AbQ1zj2Uuy7AZpTH02DILdEWR-I-EUmn1NBkeJMFrqSH5VjdCHjXD16DtbAG05zsIeV5IUtqXps6PzxAwvNhayKL2wwUXzyOJnABN6OLRJYy3k_Drp1pFQZA3elTUqG2uXk0rDaK_2-DA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=BcIXjWzXRhhyuxUBxecOcW85wdpEMUFwCdEcYHEJoUOqrUUteSa1mj-7fgdUJeAXmMwQkrdVt32csDhswsGpAwqt-XfgclO6l6NBl4EzEJgaLERFzpNuHCOJRiOf_A136lRcnpHTA7rTIB0pHXq7dtlutQaI0jnNp8232sJqpNFNV0pxaaReah7_zRuK4wqWIVOGWpPz1AbQ1zj2Uuy7AZpTH02DILdEWR-I-EUmn1NBkeJMFrqSH5VjdCHjXD16DtbAG05zsIeV5IUtqXps6PzxAwvNhayKL2wwUXzyOJnABN6OLRJYy3k_Drp1pFQZA3elTUqG2uXk0rDaK_2-DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه این خانم در الجزایر و تبریکش به یکی از کاندیدای انتخابات بابت پیروزیش خیلی وایرال شده.
"
منم کلی سوال دارم
🙂
"
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69242" target="_blank">📅 11:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69241">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🎙
خبرنگار:
نیویورک‌تایمز گزارش داده قبل از شروع جنگ، شما به ترامپ گفته بودید برنامه موشک‌های بالستیک ایران ظرف چند هفته نابود می‌شه، بدون اینکه تنگه هرمز بسته بشه و حتی ممکنه به تغییر رژیم هم منجر بشه.
اما الان بیشتر از پنج ماه از شروع جنگ گذشته، ایران هنوز موشک‌هاش رو داره، رژیم همچنان سر کاره و عملاً تنگه هرمز هم بسته شده. چرا ارزیابی اولیه‌تون این‌قدر اشتباه از آب دراومد؟
🇮🇱
نتانیاهو:
این اصلاً ارزیابی من نبود و چیزی که نقل کردید، درست نیست.
فقط یه پیش‌بینی می‌کنم؛ بعد از این شکاف عمیقی که بین مردم و حکومت ایجاد شده و اتفاقاتی که رخ داده، فکر می‌کنم این رژیم در نهایت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69241" target="_blank">📅 10:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69240">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e988916503.mp4?token=vYfFyqN33P6M47ljWcVCdNck7yIzooUHZghEZv30JDeW2PtNnaSgv7QEMUI9UfaFxn1TnU5Zc76oenGgdRAMklv3uY0Z96ChP907Wz5YGNYXZKqpPQgpfO1Zi--W4h-qm8dlYHwdKorsHdpRvAxI42chEfUvlCxP_bczYsOdUNOGWJMF4YjnKAZs-P_foOhN_vBLBtlFUZCaebK0fJ9eBiQHZfXDU6MCKGpikfS42E4jJYkHIz-jsUMFTyBV1dVB8MWpYaEViKGH1p95YuEDdUdlItZQT4VMGYwXD8QYamIjgRLmCtV1cn5pnT30b2M29TdPR77cVGmJ23TfwR-3DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e988916503.mp4?token=vYfFyqN33P6M47ljWcVCdNck7yIzooUHZghEZv30JDeW2PtNnaSgv7QEMUI9UfaFxn1TnU5Zc76oenGgdRAMklv3uY0Z96ChP907Wz5YGNYXZKqpPQgpfO1Zi--W4h-qm8dlYHwdKorsHdpRvAxI42chEfUvlCxP_bczYsOdUNOGWJMF4YjnKAZs-P_foOhN_vBLBtlFUZCaebK0fJ9eBiQHZfXDU6MCKGpikfS42E4jJYkHIz-jsUMFTyBV1dVB8MWpYaEViKGH1p95YuEDdUdlItZQT4VMGYwXD8QYamIjgRLmCtV1cn5pnT30b2M29TdPR77cVGmJ23TfwR-3DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سؤال: آیا هدف شما همچنان تغییر رژیم است؟
🇮🇱
نتانیاهو:
هدف من این است که اطمینان حاصل کنم ایران، با وجود این رژیم، به سلاح هسته‌ای دست پیدا نمی‌کند.
این موضوعی است که من و ترامپ هر دو بر سر آن توافق داریم، چرا که در غیر این صورت، با دنیای متفاوتی روبرو خواهیم بود.
آن‌ها با سایر کشورها و جوامع دیگر متفاوت هستند.
🎙
سؤال:
همین دیروز گفتید که به نظر شما دستیابی به یک راه‌حل دیپلماتیک بعید است. چرا فکر می‌کنید ارزیابی‌های شما تا این حد با یکدیگر متفاوت است؟
🇮🇱
نتانیاهو:
خب، نمی‌دانم آیا واقعاً بعید است یا نه، اما می‌دانید، من نسبت به شیوه عملکرد ایران تردید دارم.
آن‌ها همیشه دروغ می‌گویند، همیشه تقلب می‌کنند و همیشه وقت‌کشی می‌کنند. آیا ممکن است این رویه با اعمال فشار کافی دیپلماتیک و اقتصادی تغییر کند؟ باید امتحان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69240" target="_blank">📅 10:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69239">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q22gKvo5m9zNhuTJyTO-C4OWYJrMBVHSTxWVLQ2U6rD4XbWjmwi5e_NN-VuTeCHlN3xvkkcjdzhdyjbCbsRwZ0TgqZGLPf9sMaPvR-cbQ-fu_De8DrIasQK8lUlbbwtOTjBEpbspd-eBd7SAz0RY07YGLoSQ0rVAtnxvHoXL1RWuNTBD6kE-8UjNM_0UmtD4DHQFsefpRKpYCQuhDGsbTox-NoejijYgSDEied4TdFZaOD-XGNrSza0vj9tvOkEIRFlMrrI1CdThMqYelEBnyaG0_Tys_ala4npNX13LhXixds-EhKwb0Su31cflxGNUydSqXiVPw9RLN8-UZoHVbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇺🇸
تحلیل مرکز مطالعات استراتژیک و بین‌المللی (CSIS):
ایالات متحده اکنون تقریباً ۸۲۷ موشک پاتریوت و ۲۷۸ موشک رهگیر دفاع هوایی ارتفاع بالای ترمینال (THAAD) باقی مانده دارد که نسبت به تخمین‌های قبلی به ترتیب ۲۳۳۰ و ۴۵۲ کاهش یافته است.
تحلیلگران هشدار می‌دهند که با وجود تلاش‌های گسترده برای تولید، تکمیل مجدد این موجودی موشک‌های پیشرفته می‌تواند سال‌ها طول بکشد و در صورت بالا ماندن تقاضا، ظرفیت محدودی برای سایر موارد احتمالی عمده باقی می‌گذارد.
سی‌ان‌ان گزارش می‌دهد که منابع پنتاگون می‌گویند این تخمین‌ها نزدیک به ارقام داخلی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69239" target="_blank">📅 10:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69237">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=jYiN2edCpSflOjjbT6Y_myG7aFCsPpl3wms5o7NK615uNeghaMwhBgaB5Hxq9fiOzZWpjY9uNv5ZrklOUqsoHJSNt64P7QkEMHaWVxdtzsT0un4qFFLGCpbrR1jjub5GqN9eZpD0uty2tJobBsN5Ll1aSQJ1K7qs2y96_U-2OdxwucTuSkfocpOPCbXtXVbaldtFSySQ5VhgEyEAnBHadsciNZo_WZxhHC7yiX6p2xdsQNqRcADeivMi28SeRjhLSdj448tXudFLTNjLGW7RVSz3dNlgBTrsvwI0arIOzXhn9NXHzMH1IyOivcziFPp3udy-Ki8tVGcMQdKuVNdktQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=jYiN2edCpSflOjjbT6Y_myG7aFCsPpl3wms5o7NK615uNeghaMwhBgaB5Hxq9fiOzZWpjY9uNv5ZrklOUqsoHJSNt64P7QkEMHaWVxdtzsT0un4qFFLGCpbrR1jjub5GqN9eZpD0uty2tJobBsN5Ll1aSQJ1K7qs2y96_U-2OdxwucTuSkfocpOPCbXtXVbaldtFSySQ5VhgEyEAnBHadsciNZo_WZxhHC7yiX6p2xdsQNqRcADeivMi28SeRjhLSdj448tXudFLTNjLGW7RVSz3dNlgBTrsvwI0arIOzXhn9NXHzMH1IyOivcziFPp3udy-Ki8tVGcMQdKuVNdktQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حملات دیشب آمریکا به نقاطی از کشور
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69237" target="_blank">📅 09:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69233">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=AqYWajlYcZEXqHzdTnfpYcZ2u497sKaG-BcW2NXDtSf6l9Uctl5FCOzOkMA4q8iqf5Lgju7l_m_LLSsfk0g_q-Pgda9yIfLPlUsCbTS6RceM_EIfGpNrcfxMz1rknywfdDGjeya-QH81YrmKlqQ2_k4ohzr9UpeSxW9GsNGZjbObWx3yDdN6eIAbP9RVCKd9RZ2zggMiS5CwX-iSzsWOEceGY6eFZCYjROkhcaIsVrP8ZY9cUYkwFT1dvK3O5r_r4a77_16mmuC8mBvkmOCrB-vjkG3mIP0-5N91rwmmyL49mTKykMVR0HreoIr_82pDAla7yxCORKjPKIi77hGHMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=AqYWajlYcZEXqHzdTnfpYcZ2u497sKaG-BcW2NXDtSf6l9Uctl5FCOzOkMA4q8iqf5Lgju7l_m_LLSsfk0g_q-Pgda9yIfLPlUsCbTS6RceM_EIfGpNrcfxMz1rknywfdDGjeya-QH81YrmKlqQ2_k4ohzr9UpeSxW9GsNGZjbObWx3yDdN6eIAbP9RVCKd9RZ2zggMiS5CwX-iSzsWOEceGY6eFZCYjROkhcaIsVrP8ZY9cUYkwFT1dvK3O5r_r4a77_16mmuC8mBvkmOCrB-vjkG3mIP0-5N91rwmmyL49mTKykMVR0HreoIr_82pDAla7yxCORKjPKIi77hGHMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هواپیمای باری C-2A Greyhound متعلق به نیروی دریایی ایالات متحده، دیروز آخرین پرواز خود را انجام داد و اکنون پس از حدود 60 سال خدمت، رسماً از خدمت نظامی خارج شده است.
🗣️
با از رده خارج شدن هواپیمای C-2A Greyhound، تمام هواپیماهای نظامی که توسط شرکت Grumman قبل از ادغام آن با شرکت Northrop Corporation ساخته شده بودند، اکنون از خدمت نظامی خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69233" target="_blank">📅 09:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69232">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69232" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69231">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=GBz6MyqTWEFyadtjlXqmC8ewrNq7gxt686_mwtUMHefa-LF-hS6wDjlVwSRf1nriYzLUnZ4P862TC19eSTFC1WH_PwMYyZUbl_CMZcGWfZuIxwXQe5Pj0HKtWWaIxG1oiAHJ4N-vfJwSz3jfOUm__gFavOpSLsOKeG2K51W1mFxE18pLryDV9lxIb6lCxsw9n7D7-me4hM8RLNBeL7GrmtQuKAqLqqgIH9TIZpzhBGLbc9SKn6nz7Q-FmQpYNtKFIbXAc7iQ6si_auAM5v0E8AFwFBw2mYaXwNcp14yenP1L0veSx8O0x7sXSsKtjqXrUCF_qWaFYs_iVFx9huMV9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=GBz6MyqTWEFyadtjlXqmC8ewrNq7gxt686_mwtUMHefa-LF-hS6wDjlVwSRf1nriYzLUnZ4P862TC19eSTFC1WH_PwMYyZUbl_CMZcGWfZuIxwXQe5Pj0HKtWWaIxG1oiAHJ4N-vfJwSz3jfOUm__gFavOpSLsOKeG2K51W1mFxE18pLryDV9lxIb6lCxsw9n7D7-me4hM8RLNBeL7GrmtQuKAqLqqgIH9TIZpzhBGLbc9SKn6nz7Q-FmQpYNtKFIbXAc7iQ6si_auAM5v0E8AFwFBw2mYaXwNcp14yenP1L0veSx8O0x7sXSsKtjqXrUCF_qWaFYs_iVFx9huMV9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69231" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69229">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hepuFPQaifJUv9g6ExQPbQngG_HvaO9UZnK0OZbh1Fv0NCzdb9fCKegtgybe6bpCzFD6y-4QFfVMFBDQLTSNSMsHA-y0dnvf_6MimJlPD71lhQYtetb7s-IqDfNY6E3CulvS7UfaNX6PAB-hXnJTHY46_3IF3Vq6_E3JmrWmCI3dDjdoCkFCjMp3-dOU-3smsYkOtKoko-zMUG_D8BrvdYnF6r5tuFK4F2TvPs-PfMhFvQl342JHW8fDCyA-QF2l9_IrILnt9VN7SvKUUkbNXkYU7luVXpL8XNfEvnmyULKFWH8fW5iB9dHN_TIaIQq7Po2AdV6P5dlfvITNfJGNaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GxHbvv_Q3_ZEq18e6r15B0EuwOz0cZr0aeOheJxKum8TixJWZ0YXITRGEmpAbxFm8AHiPqgTcAaVapPHBKLeArcQUU2yjvGC3XKf8wpvtgFYZ2m2aa1RA0nYcGCGs5blh8fw4IBoAbfnHQ22-w6bok-WAvZOmDs2J-PNdH0rdSkqOvYdhulfxnnCJrlByVhOI5OoUugViSm7DZawHB_dzaM-qb2IYSNS0vcGtZzf2DMkntpGNrJo5Snn9GCcspfxkEvdnXQtAyDuahHoaGQ44Qbvx7qfyAS6gbhezMGv0aGqnbUnccE5pKSwif1DqaOftQ-lOGQBEx5i6POFHDO2Dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
وال‌استریت ژورنال: دریاسالار برد کوپر گزینه‌ای را برای یک کارزار هوایی تنبیهی علیه ایران آماده کرده است که می‌تواند تا دو هفته به طول انجامد.
کوپر معتقد است اگر ایالات متحده خواهان اثربخشی اقدام نظامی است، باید برای شکستن بن‌بست موجود، حملات هوایی خود را تشدید کند تا بدین‌وسیله تهدید موشکی ایران را به‌طور قابل‌توجهی تضعیف نماید.
این رویکردِ «اقدام گسترده» — که یکی از چندین گزینه تدوین‌شده توسط اوست — نیاز آمریکا به استفاده از مهمات پدافندی را کاهش خواهد داد، زیرا توانایی ایران برای انجام حمله کمتر خواهد شد.
- مقامات گفته‌اند که در صورت تصمیم دولت ترامپ برای بازگشت به عملیات‌های رزمی عمده، نیروهای اسرائیلی نیز ممکن است در حمله بزرگ احتمالی آمریکا مشارکت داده شوند.
- کوپر در جریان تشریح گزینه‌های مربوط به یک کارزار هوایی شدید، از حمایت «هگ‌ست» برخوردار شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69229" target="_blank">📅 02:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69228">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LK1wQPZBFVwJ3O0F03_ZRvHV2xwWa1AE-w0doXrZvdt-wfD4fKtOgoHSW9JRi7AM0FlWNnpIRM6DmgJfuqS2z6_V2eSqVJnQXHw4UIJt4qaDAv5hX5CVp7HZcwGGTMY1umG4NaWufiJoOOlReYgf7GwkMH67LH0MYnkyDCbENYjMDRwfbgxm_WTTKB0pTy11KZ5--m6_6yWD7iduVy6DqPI2OF9RT5Ue5e_jE1U_SJ0khS_7CwApX84CQe2itKOIXpMQRHRSr-tgDOiX5pkiv5Xq-XwelxZkHsRctdR9CnpMW_pstt64jj5YiXUOQ5NRL9_n9kUjr-DsGkgdXxEULg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوووری
؛باراک‌راوید:
یک مقام آمریکایی به من گفت که ارتش ایالات متحده در حال انجام حملات هوایی در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69228" target="_blank">📅 02:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69227">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از انفجار در نورآباد ممسنی استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69227" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69225">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTKXkSRAZL-dVD316ro1ZLPYuYUKzuCXl-4XR9XJBA_HeUVRKvK4t64PlqF54GpHaegMfwFXWthxg6Ls9Mg2-8uiwmYF7wyKEef1xZtKWPEG1kdO1pE0IowXRip4xo1s3IsRKO_M2x1QfPYoN9LVCvvYcHTTuXeN9rh9-iGhvcivmo8FAldiim_6FUbH7YdtnDhX0sfnAYoLtwYaSBT6ETMvl51cCaXWMZQqHT34xTdJm1XTpD14fNnwwVdasDBzL4DDRriLH3TfjhT8tkFTnN3rkGLlaDTMWLmTu-m30CT97nGlx_v_52Y6qO6Amqfbx_klryvJS03XCSqE71VzOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بعد از توییت عراقچی درباره اوکراین، خبرگزاری رجانیوز، عراقچی رو ماله‌کش خطاب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69225" target="_blank">📅 01:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69224">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahuX-xT0t6UwiuARLlTvnU1cmaJIzTOti4BF36sm3590k7Um0BwNp3nmhL1HoKJsE0_d3-1Wg6JcikECLFVyCjhroTTH1wr2zJ0blYhqYA3THmUcKVzg7-b4GNm1OCZ9Bn0nOhpcOzcV2NxnfcJFy-_qyFlvN5by2JHxIwzjGKzKD4WaBrVrQOeAwUGQWmjSH9-S5CpJEDXEhMwD7HUVIWUerfWfNpogspOD0aaoAwz8rivEh-_aST6ayCYN0_zVaAIBQJFa2HpcxEu3FcDNfR0wWzsOE8xMmbKN_YRPCufXHk7CQ1hUBYBSrm-XSNOL-Va2fU1ZnOJN1i5qhM9Dbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حساب توییتر خبرگزاری تسنیم وابسته به سپاه بسته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69224" target="_blank">📅 01:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69223">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doRc4tgt1r6Ad8G5ROkkOm2B0gcrDy5_aKqT-R7WIrBElmgaomyEYAvQRJ5QJxxw2IUmNEhmY4mXS__qZnCeN7T7OuAVgo--uek8vE12NTYDJP98uzpvhn0K5F6VDAcchEMOlreAsOo8TOIG6Mefz2AOAGoN4bWrRILo8oAv0hftGzBL4LRqm38yFn0MVRNa68sBn5qKLdKC3cDcmwEDcMCq4TXrBq1drA2PJY-aSHTEqMRjsqglWdtwpbbqgcg4E8PismWOZZA5E_4FGmYXIXTavC9uhX0S7a_lrqhGvfsn9B_-WDqWCnCjvRSHHWr_NgzwjKokfX_uh7MgHpoFcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏9 فروند هواپیمای تانکردار آمریکایی و یک فروند هواپیمای هشدار اولیه مدل E-3B در حال پرواز بر فراز خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69223" target="_blank">📅 01:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69222">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZ5e-0FILk9ROybbU8WovBmMztl7CLf9s0qq3XPYD-EhZc4bn3VycHaPWbkuGrJLPz1SsYdcNmWLIRSo3Qi60fj4t_XVD5B3IlKf2ZCxp82dQQopnwNEO1oJTCKMa6Dg5BQbKYx9t0rNV0WD36uS9sdDaFa15tnXsuOIxXXTsSP8YNnhRsFANKf1Uefql36Z7tS-MPw7QirwBrbIxBGgotPar5fU58_bTxA_7dznh6mTvvXHK0ao0gVX65y2aRI-X3LiaT3A8TjAR5GPpNWu-KWrKhwcZjLtdI3jvRwM0y7tswgAQCq190pKPIsUa3Y9gz6TEdaXqJb_1Mzmtf8SiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شش سوخت‌رسان آمریکایی در آسمان منطقه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69222" target="_blank">📅 00:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69221">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد  @News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69221" target="_blank">📅 00:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69220">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piuCr-bKg8eYGxepZnjxhJdaUvIorrZ4OEFrzVivHWAZR0aBGqNjl1XAYy15XYgkUxpzo0R8R5tR0Su2pkXU7YhwNsE0a_byJB6wfi3w80spXgh58ktsVu0FHDvKxE2bFGEPovnT16F13bVctwcvOTdOgDnqFhcBs4pZTXSSRfmC9xTFCEylXp8_TIpuPDnEqxo_wjtSpofhsORtYS1eMYN1TVBJpmpR8UPu3nOYVQKUODDEVDWd7UTIt6rUpjpqjZ7UQL9IZnSWssQosF5k7159PSp_VUpjLCJ_YDuf9Z9msvcACAJ6aAtVLR62s1EzxZbd_eSrtKHjoKts0A8Akg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه تو تلگرام یک کانال و اکانت ساخته بود گفته بود هرکی تو اردن و کویت تحرکاتی از نظامی های امریکایی دید گزارش بده؛
لحظاتی پیش تلگرام سیک اکانتشو زد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/69220" target="_blank">📅 00:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69219">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69219" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69217">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=a-ynOvIEaK5iEjINcQTWwDMD12qpWjLVbebL_pP4ZPZ09crwcwLYIWFliei56_z7amwFFF0jFbyDnx1quy7Vd6hKQ4FxXeb4dDTb_Ot9B4oCuRaclNM7VoRLXK0bAiYMyJ_aC6AoCLlwmZgHypFfcbRtHQdm5gFDvl1VFrfnY72XCmp3QnShZAS8NR8Z2FR0qwZ3Q3kDQkkAV6LlgOSTYbrUqlIIf3wuzmPj45WmOgLgzoIb4jaLVyBOAEbtR8kcMrkse7AT0P_FSBV90HTfMuUd4ktKvYqrUpIoV-Bw3i-K23l_obnrruQMyRi5ko_5rVORdqu3OmnA6l8fyoTgfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=a-ynOvIEaK5iEjINcQTWwDMD12qpWjLVbebL_pP4ZPZ09crwcwLYIWFliei56_z7amwFFF0jFbyDnx1quy7Vd6hKQ4FxXeb4dDTb_Ot9B4oCuRaclNM7VoRLXK0bAiYMyJ_aC6AoCLlwmZgHypFfcbRtHQdm5gFDvl1VFrfnY72XCmp3QnShZAS8NR8Z2FR0qwZ3Q3kDQkkAV6LlgOSTYbrUqlIIf3wuzmPj45WmOgLgzoIb4jaLVyBOAEbtR8kcMrkse7AT0P_FSBV90HTfMuUd4ktKvYqrUpIoV-Bw3i-K23l_obnrruQMyRi5ko_5rVORdqu3OmnA6l8fyoTgfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلمی عجیب از تجمعات چند شب پیش خرم آباد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/69217" target="_blank">📅 23:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69216">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند،</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69216" target="_blank">📅 23:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69215">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6df873441.mp4?token=Oz51tW3U_trzRcYFV4DrwdQyCzjd09dwLKjuoUnQaA22RC2vp3W_9O0068o0ID04IW3CmdrGNEd-OeytFMIbh0AGBF8ov2XtCZ5JB_sNfbS70LNA5p4irnsVxObgSGztSBvXWjl-AoIOVzknj1XzOVMv2HuYmL6LPfq8AwPZSTBSggIfBp9n939GD9qrmXJCNaAjrqSW6HnqbQytQMDmEqzef5rJ4hX3A7p6KXzFd5DEgVTo71jNYsYaVDCjB82nPTVK3pFHiIgvCFXHAF0pdoERs-hOWhGmG_gwUr3lax5bjXZesyXa8DNtCb8tdbuHMgiQcLDgtCdS-rNx31LUzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6df873441.mp4?token=Oz51tW3U_trzRcYFV4DrwdQyCzjd09dwLKjuoUnQaA22RC2vp3W_9O0068o0ID04IW3CmdrGNEd-OeytFMIbh0AGBF8ov2XtCZ5JB_sNfbS70LNA5p4irnsVxObgSGztSBvXWjl-AoIOVzknj1XzOVMv2HuYmL6LPfq8AwPZSTBSggIfBp9n939GD9qrmXJCNaAjrqSW6HnqbQytQMDmEqzef5rJ4hX3A7p6KXzFd5DEgVTo71jNYsYaVDCjB82nPTVK3pFHiIgvCFXHAF0pdoERs-hOWhGmG_gwUr3lax5bjXZesyXa8DNtCb8tdbuHMgiQcLDgtCdS-rNx31LUzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ضربه بسیار سختی به آن‌ها خواهیم زد. این را می‌توانم بگویم، چرا که کار زیادی از دستشان برنمی‌آید.
این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند، اما، می‌دانید، باید کمی آنها را تنبیه کنیم.
شی به شما گفته بود که چین هیچ‌گونه سلاحی به ایران نمی‌دهد یا نمی‌فروشد. گزارش جدیدی حاکی از آن است که ایران ۴۰۰ پرتابگر راکت از چین دریافت خواهد کرد. ترامپ: این موضوع تعجب‌آور خواهد بود. او به من گفته بود که در این کار مشارکت نمی‌کند. او می‌داند که من بسیار ناامید خواهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69215" target="_blank">📅 23:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69214">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=kE1tiKvwX5ITr8Utz-QqXJG7HsUFS9u2LQV6rAAlSn4bU0IP9BICa612bkArw84n6fN2YGjvN4gckB-p87gdatu9kbFMhIEnATTu5_A8flCQfv25hzFPKi1HfiaGFUEnvOcz2i6mUl_W8RB3Mqb95isl-f19edrqKYuKxWYDuD0d6vn31SPW5nsFnwukG1BDpWNTJfhoAx4f1LWQkd2l4rTjZs2fCUTq9wnz41KKER7r9eD1pglBj3DaV8icL2l7QosqqbeR3CgBTtnyJwxI61sB3oDfeTjBczadSiYSOb5kthCovv6Gw7Ca7QzBu2C3MLsm_YJvXCe4FLJs72oNtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=kE1tiKvwX5ITr8Utz-QqXJG7HsUFS9u2LQV6rAAlSn4bU0IP9BICa612bkArw84n6fN2YGjvN4gckB-p87gdatu9kbFMhIEnATTu5_A8flCQfv25hzFPKi1HfiaGFUEnvOcz2i6mUl_W8RB3Mqb95isl-f19edrqKYuKxWYDuD0d6vn31SPW5nsFnwukG1BDpWNTJfhoAx4f1LWQkd2l4rTjZs2fCUTq9wnz41KKER7r9eD1pglBj3DaV8icL2l7QosqqbeR3CgBTtnyJwxI61sB3oDfeTjBczadSiYSOb5kthCovv6Gw7Ca7QzBu2C3MLsm_YJvXCe4FLJs72oNtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
این ویدیو رو بفرستید واسه اون تعداد از رفیق‌هاتون که عشق دعوان:
دیه‌ی شکستن کامل بینی : 2 میلیارد و 100 میلیون تومن
شکستن فک بالا : 160 میلیون تومن
شکستن فک پایین : 640 میلیون تومن
شکستن هر دندون : 105 میلیون تومن
شکستن دست : 160 تا 210 میلیون تومن
شکستن سر : 120 میلیون تومن
شکستن پا : 210 میلیون تومن
شکستن گوش : 350 میلیون تومن
کبودی صورت : 6 میلیون تومن
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69214" target="_blank">📅 23:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69213">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3687c44382.mp4?token=YHLbJp68-tBjeTAlot5HYC1qvMwhb7Jb8BEXFBYcaZT5dOIJtQyPGlBXNiie76NQNHRjYS-dXLtToyQ_gm3gdvzpgSEypSq4PyyHP2ynTWbegIITyuGOtGlpZiNUWV34VzaKbBaYDGEs9cEQwZC_03xDjSkXByScYaHSy2ZOqviQgDKIFUOtDk90O4MG_GeNM1wlQidWh0THjhquoxb-gL7dUjF7iV58276Lai3L8P4Nce9NYKOSlfqI34Tvz1vTEu_dplh986TEyEKtzvXHbCCBp4KDf-6nJB2Ff2ampBajfjyPK5qCCe0FonWYi5LeBe_qFNHtxkqxHB7XF7FqRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687c44382.mp4?token=YHLbJp68-tBjeTAlot5HYC1qvMwhb7Jb8BEXFBYcaZT5dOIJtQyPGlBXNiie76NQNHRjYS-dXLtToyQ_gm3gdvzpgSEypSq4PyyHP2ynTWbegIITyuGOtGlpZiNUWV34VzaKbBaYDGEs9cEQwZC_03xDjSkXByScYaHSy2ZOqviQgDKIFUOtDk90O4MG_GeNM1wlQidWh0THjhquoxb-gL7dUjF7iV58276Lai3L8P4Nce9NYKOSlfqI34Tvz1vTEu_dplh986TEyEKtzvXHbCCBp4KDf-6nJB2Ff2ampBajfjyPK5qCCe0FonWYi5LeBe_qFNHtxkqxHB7XF7FqRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ضربه بسیار سختی به آن‌ها خواهیم زد، چرا که نوبت ماست که به آن‌ها ضربه بزنیم.
آن‌ها می‌دانند که این اتفاق در راه است و از ما می‌خواهند که چنین کاری نکنیم.
آن‌ها دیشب تلاش کردند با ۵ راکت به ما شلیک کنند؛ ما همه آن‌ها را رهگیری کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69213" target="_blank">📅 23:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69212">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ویدیو وایرال شده از یک پژو405 که درحال فرار از دست مامور هاست اونم بدون لاستیک!
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69212" target="_blank">📅 22:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69211">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdNOHR79q1X6LyspTM3iYeLQEhN2f27orFWPxk1KKwiTKxyOWRAvFv0gYhZnbhMc1EyNi9VnzKyXIlFc1k_xhJHv7MCjNiMqKpNHwzXbYMjJVLznom5N0UjCwulwi0Jp8nLvUmB4OXpamDH5zcjXrgnr0Z7519NshbiHaQzCwtiyHL0Q9RnPMZQFfv6Z_aCekLcMN_tFO62vWSlzn6USBZs892IB7bad-6xwiauX8DApMWglgtLe0WwXFhBdVxlzlrtgsf7VnkKqwW1TqKm4__-VO2NfsWZfznXlk1P6Ei9qxMttGea07jC0AIE43v2eG5BnIJW4DXmpEzAw3_WfXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.  حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!  @News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69211" target="_blank">📅 21:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69210">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_mFXcOeOr7h6mfRD3wJy3DKP1IN2C2bFrhKnOFtwmRMJnAxMJZszsebaiTSyRA0oECnWaE1en2FuQE5PRn9_9rrdWivdGinEfzKHN0VaBB35QQx6sDILPCgdnnJ-Hhhr69KY0lyoC9JpyjP8AxzMSeqow6s1oA3iFUQ3GdRDi18il3vR4qevJYgrZbsz6wneDMaCgargemIJ3IilRmoPr4pTHhB334AEg5uMSliZfsEL5qEyJ4n-xDmYVC80c4exw8FI4Gr5KIX_iK2dyomurUD881dOaomQIYrdbFILROI8DdAIK_HJOQNy9hYc3qGVRu_u3emHvOsI48qU6LuPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
❌
🇸🇦
نیویورک‌تایمز:
حدود ۲۰ مستشار ایرانی در جریان حملات شبانه آمریکا و عربستان به شبه‌نظامیان مورد حمایت ایران در عراق، کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69210" target="_blank">📅 21:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69209">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TY0StRkaPqPsGTLmlIIStTFzv3IGE2azWtyM6h9bc1fXT-00Z9KM02bNYDHPYdZUkwJDp6DHYXl9FGRyKRcpdLGbgd1wW7Ja9Az2BiaJPb-iRQeO7nXTtYDGApkoqKFAt8QoZIPF9goA7JEJi1irydpSxijuSr_soy1wOpgjW7aPcqtvXahcbahEu7SmK0U6NzYGH-kyQ02CajLGO9KZMTkEQIU38hQp5Z8DffPTYgWsXli_UMEZgVYx-DsgdqSoPXjHH2gixJZIdY1l8f7n1c3mK-_sjGYspYIe3BrdwORTM4JyNgVzsGStsT-USoK2eE_pooUQzUjBg2N4ZR0zqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.
حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69209" target="_blank">📅 21:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69208">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=ChjlCASxwz0pENru-Wrdek-ZhkewWgVO1to2P_gKQ8pxu1Wt4ByJUA-pkhNiP2dd83Fk6HMzJtooRBZCiuOvwlan-ytKS4df71ZdlK1vRkFGm7mA5lfBvZhF13B_0FSa0MvmciKzKXkrBMjZ_NbBVm_P79JMUj1iBQ4GZ3vuFiKlze4irz5AFpwRnLlFX07acDQ3t7KtRZJHF2uoXWPYftvp9-LR2k62IIAJCpFTjSeBxIW-5NuPAo6--Oeyfyd2Yhug-zq6-qE7bI-21xBQ4Nnn0bP_29cqJFkzDcCXE_ud_R0IHV7u30UNk4bh_SzDISc6NYzj_c7dN-vSfc457og0G0qjK712EJgdY9JkaUOPX_hJrxoB1IJr7eAd5FDvRPGCOXWebDpnccVsLlnIfowxtWoik_DMtidbY4O67MzR4IH6isjnJl7KUyvIqMeTp6zmGvshMCCDsCWvyKEvpMNLJBXs6xZqO37hPbczkTJdDEaTU6WhfWFEeFBT-ArgbBwDm6O0JtTT-KeugXUtoPIAO9zohCsasBSbOjdfgYvTSArqsF3MpqxQFBb6wuAH-74wJ3wryq_PTiU8oX_S9DWaW5sIn2nqs9iXoSEWWOMVnnYrqwT1fmsYOaVGpbZh_tcAZ4J4EMWMs4x5-WxW_aooPWe2a7M3gNdJ91jS8do" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=ChjlCASxwz0pENru-Wrdek-ZhkewWgVO1to2P_gKQ8pxu1Wt4ByJUA-pkhNiP2dd83Fk6HMzJtooRBZCiuOvwlan-ytKS4df71ZdlK1vRkFGm7mA5lfBvZhF13B_0FSa0MvmciKzKXkrBMjZ_NbBVm_P79JMUj1iBQ4GZ3vuFiKlze4irz5AFpwRnLlFX07acDQ3t7KtRZJHF2uoXWPYftvp9-LR2k62IIAJCpFTjSeBxIW-5NuPAo6--Oeyfyd2Yhug-zq6-qE7bI-21xBQ4Nnn0bP_29cqJFkzDcCXE_ud_R0IHV7u30UNk4bh_SzDISc6NYzj_c7dN-vSfc457og0G0qjK712EJgdY9JkaUOPX_hJrxoB1IJr7eAd5FDvRPGCOXWebDpnccVsLlnIfowxtWoik_DMtidbY4O67MzR4IH6isjnJl7KUyvIqMeTp6zmGvshMCCDsCWvyKEvpMNLJBXs6xZqO37hPbczkTJdDEaTU6WhfWFEeFBT-ArgbBwDm6O0JtTT-KeugXUtoPIAO9zohCsasBSbOjdfgYvTSArqsF3MpqxQFBb6wuAH-74wJ3wryq_PTiU8oX_S9DWaW5sIn2nqs9iXoSEWWOMVnnYrqwT1fmsYOaVGpbZh_tcAZ4J4EMWMs4x5-WxW_aooPWe2a7M3gNdJ91jS8do" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کشتی ترابری گاز آمریکا نزدیک بندر دمیاط مصر با پهپاد هدف قرار گرفت
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69208" target="_blank">📅 20:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69207">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f541b0693c.mp4?token=r8j4jKwSPQHNjpxYEfdxGW6d-2DDEwptLSyMQfPsd7A7fK-QMxD9Stlf8wjioYXbyG5GBV16QJLO2JqW5KR2dyurzGUfmqDCvlgdYQcpU5uINxR1nDRmlh_l3Rw6fd8drH_gPzrf1AU6fHIFJ5UEXzTqMDRENmtgUZkOXZNQXXK7vDUZ3iZMoySoHHnu3VgvMbw0tQ4ipEwcdOC_l3LgcY7Y8QRFIXnJput1NtPFFbeNlpNfMs_fLKQsmEXcao6Jv633TMtmvtw-23HKT8ywFT_njx_Ckosl5OfaAC6R0XMgggPQNiW4Z_OzHUPU-qhLP3TBtiOPNeKbB4m0a7tt6oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f541b0693c.mp4?token=r8j4jKwSPQHNjpxYEfdxGW6d-2DDEwptLSyMQfPsd7A7fK-QMxD9Stlf8wjioYXbyG5GBV16QJLO2JqW5KR2dyurzGUfmqDCvlgdYQcpU5uINxR1nDRmlh_l3Rw6fd8drH_gPzrf1AU6fHIFJ5UEXzTqMDRENmtgUZkOXZNQXXK7vDUZ3iZMoySoHHnu3VgvMbw0tQ4ipEwcdOC_l3LgcY7Y8QRFIXnJput1NtPFFbeNlpNfMs_fLKQsmEXcao6Jv633TMtmvtw-23HKT8ywFT_njx_Ckosl5OfaAC6R0XMgggPQNiW4Z_OzHUPU-qhLP3TBtiOPNeKbB4m0a7tt6oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
نخست‌وزیر نتانیاهو:
«سفرم به آمریکا فوق‌العاده بود.
همیشه درباره موج نفرت از اسرائیل در آمریکا می‌شنوید، اما احتمالاً کسی از موج حمایت و علاقه‌ای که نسبت به اسرائیل وجود داره براتون نمیگه.
همین الان هم با وزیر دفاع آمریکا،
پیت هگست
، صحبت کردم.
اون یه حرف جالب بهم زد. گفت: "توی دنیا کشورهایی هستن که اراده دارن کنار آمریکا بجنگن، اما توانش رو ندارن.
از اون طرف، کشورهایی هم هستن که توانش رو دارن، ولی اراده‌ای برای این کار ندارن."
بعد گفت: "فقط در اسرائیل هر دو رو با هم می‌بینیم؛ هم اراده و هم توانایی."»
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69207" target="_blank">📅 20:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69203">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPyWcoNA2ZONfop0WL5qAluIN9nvwhA8uqY6fUeIGRvH3vJ9Azf42eitcTmwXu0gQkCGaCp8WeqTnKROOKiIPHvYX3M9HcU4mCoOJdLPAFaGBT6D2qiP4zHwvwFKGrZy5ie_1RDSbcGCyNXLakNQxrQNUh5wL-CsZTWGmyUDz8MFdppKUglzydetOf39MtUyZvXwvVB-u3ALbw3So-UzRyH5k8ETdIElUNL9hl4CiSQfk5CxvUbUwpHIcEuyl3wGwSf33XJsvSkTEHmMdNNGQeVut1qUJWTBq90Eu8DLGNk3_j58tMolL0IW8LFxmhCQDL3pCHuYOqQ0bbmUa_jLxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=X9odSvpn_Slaro52qrn8CglJf-hHrY5ZdnZYSrH3jqJxlZeT0mx6csCHHKYlpF_W32eIC0EJ7J523ZfsmHXig9CnEEL6XXsPyifIQMMjnOpbcDA1qt8mjQ5TldyN3yDoec1MtPlnY_VXYpikbdRr9rK7AWZwjhv95BeWO3qyZvFEzKhSqJosO39RG4LixWUkbZ6YPyjwu9w3GSJ6KGRmgQzhSAUzT37IYoHElmD_4yRCqYmn61rjFV_bqmTfKkchGDna3HYF-h1YRikDazUC8nWOS0qgFGFy9-2S9WO07DVXz6uym9CWRCNZi7nvOD29Er7UfWWhuY9PvGRLiaZpNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=X9odSvpn_Slaro52qrn8CglJf-hHrY5ZdnZYSrH3jqJxlZeT0mx6csCHHKYlpF_W32eIC0EJ7J523ZfsmHXig9CnEEL6XXsPyifIQMMjnOpbcDA1qt8mjQ5TldyN3yDoec1MtPlnY_VXYpikbdRr9rK7AWZwjhv95BeWO3qyZvFEzKhSqJosO39RG4LixWUkbZ6YPyjwu9w3GSJ6KGRmgQzhSAUzT37IYoHElmD_4yRCqYmn61rjFV_bqmTfKkchGDna3HYF-h1YRikDazUC8nWOS0qgFGFy9-2S9WO07DVXz6uym9CWRCNZi7nvOD29Er7UfWWhuY9PvGRLiaZpNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین با حمله‌ای گسترده و پهپادی، منطقه ریازان روسیه را هدف قرار داد؛ در این حمله، یک مرکز لجستیکی بزرگ متعلق به شرکت «وایلدبریز» (Wildberries) آسیب دید و بنا بر گزارش‌ها، پالایشگاه نفت ریازان که تحت مدیریت شرکت «روس‌نفت» (Rosneft) قرار دارد نیز هدف قرار گرفت.
آشکارترین خسارت در انبار حدوداً ۱۸۰ هزار مترمربعی «وایلدبریز» در نزدیکی شهر «ریبنویه» (Rybnoye) رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69203" target="_blank">📅 19:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69202">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
⁉️
آمبری:
یک تأسیسات شناور ذخیره‌سازی گاز طبیعی مایع (LNG) با مالکیت آمریکایی و پرچم جزایر مارشال، در دمیاط مصر هدف اصابت دست‌کم یک پهپاد قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69202" target="_blank">📅 19:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69201">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=FsdqgwGwrHiW3vq22nXi1Tq-IntKP9JR6T9JoZHG-7qXJaUa7T4s-fdbkvEXmXNEUF_p-hfvs-sXuQmo6lew7mMN1NM8TZ3PicDopym0moOcPuRLYiIzN0nlHd-KdosJE37kM-ujvShnpcvzUTJhhyV6FK_1V5I1v_bUXhN40B8OeSj1mUaH7sEFeQh3bgfxqQG1k5ZzNYLLEVTYMc4Wu3NAVvCNlCq4E_XkpKi8P0Wc943c1zUu2ooETJ_e67kPYqu0-yAMhqSipAQ95sPnTwWmzFmD767JmLCamRtHSl4bYYLcAyMCvHCtYn52kiT4iyJ1vH92401HAD7Z5Ccowg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=FsdqgwGwrHiW3vq22nXi1Tq-IntKP9JR6T9JoZHG-7qXJaUa7T4s-fdbkvEXmXNEUF_p-hfvs-sXuQmo6lew7mMN1NM8TZ3PicDopym0moOcPuRLYiIzN0nlHd-KdosJE37kM-ujvShnpcvzUTJhhyV6FK_1V5I1v_bUXhN40B8OeSj1mUaH7sEFeQh3bgfxqQG1k5ZzNYLLEVTYMc4Wu3NAVvCNlCq4E_XkpKi8P0Wc943c1zUu2ooETJ_e67kPYqu0-yAMhqSipAQ95sPnTwWmzFmD767JmLCamRtHSl4bYYLcAyMCvHCtYn52kiT4iyJ1vH92401HAD7Z5Ccowg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر اسرائیل، بنیامین نتانیاهو، با پیت هگست، وزیر جنگ آمریکا، در واشنگتن دیدار کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69201" target="_blank">📅 19:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69200">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xtdz4M3hhW5WS_3mml4A4-BUT5dsxPUzCh8BaiXfBYkFRtFfIHIhrLh-Y5o3CdRN928ls67s0YDsxUsdTf1E26WKDEbEvwc5Bf3wMehQwnZP8aPvRbGdyxQ7EbjgYluk5l9vzDpSiBbXmM-x-socjcWnhUrGHZ3Name0AhIwYcWOvaeO8hJ1kT9kusN4Mx73zF3eUYquZ6Jwv8dxMUFwyJnKKTuWjc_IkdcEGZ2i-y5a4RpcGpm1dXbRg4_ZQw7fi2GK74fxHNopP6eNBM11h-ly7-23J63DIPUe_mq136A4N4rQRI2xW2EzCIjJBzTuy61dmXMZsYApPHc34B-Bvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنت‌کام:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران (IRGC) پس از تهدید و تلاش اخیر برای حمله به کشتی‌های تجاری و دریانوردان بی‌گناهی که از تنگه هرمز عبور می‌کردند، همچنان مدعی است که دریانوردان بین‌المللی باید تنها از مسیرهای مورد نظر سپاه استفاده کنند.
✔️
واقعیت: تنگه هرمز یک آبراه بین‌المللی است. سپاه پاسداران هیچ‌گونه اختیاری برای تعیین مسیر جهت تردد آزاد و باز ندارد. کشتی‌های تجاری همچنان با حمایت نظامی ایالات متحده از این تنگه استفاده می‌کنند. از اوایل ماه مه، نیروهای «سنتکام» (CENTCOM) به عبور حدود ۱۰۰۰ فروند کشتی و ۵۰۰ میلیون بشکه نفت خام از این آبراه باریک کمک کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69200" target="_blank">📅 19:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69199">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🇮🇱
یک مقام ارشد اسرائیلی:
ایرانی‌ها سانتریفیوژها را به «پیک‌اکس» (Pickaxe) منتقل کرده‌اند، اما اسرائیل از انجام هرگونه غنی‌سازی اورانیوم در آنجا بی‌اطلاع است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69199" target="_blank">📅 19:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69198">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiStpwPhrweQ-0Y0GcqD5197nTw5V9SpqmoG3lVZP9nnPPe6BuZQvF-Difb__y_42G1qVrH3SWYkvZvgeOB9pohcONsPFGGVlVQtnmeayxK6JtXV7RfghD5W2SmqiU4oM8NEqfuCKwBTeUbLekbuBK98YEVVlgvB9PYw_fodcyzeYrttdM7Zghaf-OxXiaUDvYj82A68hxtsPS90hgQ1m-GzA1NioKtft3MVRH2Jmave8Qwb2-rNTg1AYOIexCoFW58WO19fK9_pf6OPuUEwoM-LFQohJDpK0jB_ZmzXtkXN8c_AmwoOdZfrfpXyoRcxnFl0HeE94u_7UxtZ6wxqVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک‌راوید:
معاون رئیس‌جمهور، ونس، روز سه‌شنبه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار کرد. یک مقام اسرائیلی اعلام کرد که هگست، وزیر دفاع، امروز با نتانیاهو دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69198" target="_blank">📅 18:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69197">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pi625q4AoVZMFzDFG7mrcxsKYKZakep6SgMOKnKPUzZNevk6KM0TiQPNQuvnH2JYKtF9b7DnQia6iGeme4PCLxsEa5okY8pO_48xTDLib0Azrrgmh3OsHP6CJTIvjJsBrJaB-SwWl9J-SHrcKPI2OjfwYhWKeU31eozIVOtQftm_OUULEr6w2aX_sZTVbdmfd-7l3_QeZsGjpqrpovqyVPISP6NSM7_4cmjikmLqu2pYjdROxY-g4N1mijTOGMW-UuSpwbHvr0kZpN1VoiG3wOYByGRqB2w90P5I2OyY6knnVklagS3Lb-nQ9dPYKUw3dpOj0tvI2SaV6KWGBq9Irg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تلفات حمله مشترک آمریکا و عربستان به حشدالشعبیِ عراق تا اینجای کار؛
- 20 کشته
- 32 زخمی
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69197" target="_blank">📅 18:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69196">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxyr0rNvM6w8oclWouRpr10OKrQmtY-FTgCdEd6oKYfqoHsXLdIw-xha2NVP3djYjA9a97zWY6NlN2aZ-oSt-1abOD40RUPU117HiAnW-9hhTNcjxNOayl1cybj_gVr18-wlkLTRnugKAUIVkMapbgFIVNl4S_X7oE3zPYOWb4h-Hm6rPEJ61d1I0JuVaIbyNTMzC8Ky44lYtXTLgC65CHoDSrPWy2VDdU-UstXk0LTmLWQh9yfFlDdDfusuFetCMBaQ2WKKY82MXwlgSaMvppmdBiTxLkI8L4wiHmRnRqX6cpyg4VyyocF6arHOfJZwoHl2gV8ktCpPwoy4FBXbCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇷🇺
پروفایل عجیب پاول دوروف مالک تلگرام در واکنش به تحت تعقیب قرار گرفتنش
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69196" target="_blank">📅 17:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69195">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=vl2ctnLNgxEZ7soVWWn_HEH8NNvralKYtneGyrDZP-jwUfqtP5KtOUZZNcJ-273ZAFDJEZbm-HX790a_hM42gl1YWVLN4fqohoSb6CmWujcGbgYa2pa5zHzQCpjXMswjG9Kva_K58_w_quV9d0t7uDiGXfrVX0GBhqqgPsRrY4QZLJ6C3tcFz9zVpg93smEEcUd2Bbg_uK-FIFDP3DLajJafOF-x0n9yT3J8lDfYluW8e-nGIQXo6vYud_DkUmVMDcZKbbmzkdOjmdCyciW85l2VT3hWWwmaOXaK1ecyhONmG8Vfhb8rImn8HpDnKZr14mOdgEp9pmlXHp93vCZvfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=vl2ctnLNgxEZ7soVWWn_HEH8NNvralKYtneGyrDZP-jwUfqtP5KtOUZZNcJ-273ZAFDJEZbm-HX790a_hM42gl1YWVLN4fqohoSb6CmWujcGbgYa2pa5zHzQCpjXMswjG9Kva_K58_w_quV9d0t7uDiGXfrVX0GBhqqgPsRrY4QZLJ6C3tcFz9zVpg93smEEcUd2Bbg_uK-FIFDP3DLajJafOF-x0n9yT3J8lDfYluW8e-nGIQXo6vYud_DkUmVMDcZKbbmzkdOjmdCyciW85l2VT3hWWwmaOXaK1ecyhONmG8Vfhb8rImn8HpDnKZr14mOdgEp9pmlXHp93vCZvfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.
هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا رو گول زده و برده خونه
⚠️
ویدویوی کاملش ده دقیقه‌ست اگه خواستین می‌زارم ربات ببنید
🔗
🔞
مشاهده ویدیوی کامل
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69195" target="_blank">📅 17:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69194">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_ye0NbFPY5m-vtIXSUEnl7c9GARr0-Uq6FHonzH-yyAPkpgwMqWi8vS6HjqvG5jlfAJkun_7cZf77H_5Ut2OYKqENrSPpQVKJZm_014kYhNC8vOPLGAwS6N-2bQEZoOT3rKYwcgcPV1YV8flYvdrzhcYWcDE250NeHSgY1izxqkeu_ALcwN82GxASD7J0ILNM5KF5QXOYBtkPT6rRpu563QYPmiQqMLGVYQdwSJU6brw9Ogk_LJbjoso-hkDM-gknGMQGRcAgMfJfsb1WPLcuxKfgbv0vhghHezo5IAJz30NYG1CtKKffuMaFvz0Yp_8qwfNQjcKDlXfDvwPIyubw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیروی هوایی ارتش جمهوری اسلامی   اعلام کرد بقایای پیکر امیر سرتیپ خلبان مجید کاظمی یکی  از  خلبانهای  2 جنگنده سرنگون شده Su-24MK که توسط F-15Q های قطری سرنگون شده بودند را در خلیج فارس پیدا کرده است و از سرنوشت ۳ خلبان دیگر اطلاعی در دست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69194" target="_blank">📅 16:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69193">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=SmoiT80Fk3sZP8ZwP83IBifAz2FkIjS8DvagP4uowa2WJFWDlp2aM159rf8r9BQijV5UkKC8inYhBDmV-RhiVvu-W0XGrKV-N0icqDBFcR_xMOHTV82Sz5FvpWVH-eV7IGW5F0Ws3bFuds0iA07rZuRp3PMGZ-p9Eso1e-mR9ef-XigoJL6miv5HpPXdpZ5tfdVWGMhJayQ74eP6-QQ35FZHg6owOYuFFRIr40dFpR722wLlliZyu0R_aS7k-4AJUQV1LNwBNTt6UDaGangvKPBooaAHiHDBhIrxoPn7RPkkT-TolOUxMQjsB_5Db2TR8Jn5fxrimk5b39RJmcbE4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=SmoiT80Fk3sZP8ZwP83IBifAz2FkIjS8DvagP4uowa2WJFWDlp2aM159rf8r9BQijV5UkKC8inYhBDmV-RhiVvu-W0XGrKV-N0icqDBFcR_xMOHTV82Sz5FvpWVH-eV7IGW5F0Ws3bFuds0iA07rZuRp3PMGZ-p9Eso1e-mR9ef-XigoJL6miv5HpPXdpZ5tfdVWGMhJayQ74eP6-QQ35FZHg6owOYuFFRIr40dFpR722wLlliZyu0R_aS7k-4AJUQV1LNwBNTt6UDaGangvKPBooaAHiHDBhIrxoPn7RPkkT-TolOUxMQjsB_5Db2TR8Jn5fxrimk5b39RJmcbE4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره حمله اخیر ایران به اردن:
این یک حمله غافلگیرانه بود. نیروهای آمریکایی تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69193" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69192">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=DrmvlzZpo951dCv9bz4lFDwpZCargUpLWdupZh3U9ZiFcoDkUGwmHdxrNppGwPlghjxB-JUF_FH2rOMJR5zjPSBNmxT1vBaDW002FQL7PPi0A1AHCXIyxZRxT6YR8ksJRGjG6_f8gVWlI15eSjuTUG45pGmcVsgBd6tMhY7kmcAJMhp6ozi_2PPuEhcn15xB6rv7KR40CnZYeOFDd-pX_W5B3X2j1qA9zv6NBAwKD6881RQXj_pn7gx2V_31nJ5eexl9sKQZo77MA9SjBJoM7W3OjSSa0ymEOoHvBgB0zZF09_0QKBeytphH7abn_YJdAj4PoEGNjMJRJMFyBF5QfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=DrmvlzZpo951dCv9bz4lFDwpZCargUpLWdupZh3U9ZiFcoDkUGwmHdxrNppGwPlghjxB-JUF_FH2rOMJR5zjPSBNmxT1vBaDW002FQL7PPi0A1AHCXIyxZRxT6YR8ksJRGjG6_f8gVWlI15eSjuTUG45pGmcVsgBd6tMhY7kmcAJMhp6ozi_2PPuEhcn15xB6rv7KR40CnZYeOFDd-pX_W5B3X2j1qA9zv6NBAwKD6881RQXj_pn7gx2V_31nJ5eexl9sKQZo77MA9SjBJoM7W3OjSSa0ymEOoHvBgB0zZF09_0QKBeytphH7abn_YJdAj4PoEGNjMJRJMFyBF5QfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ به شبکه فاکس نیوز:
گروه‌های شبه‌نظامی مورد حمایت ایران در عراق، یک آفت جهانی هستند.
من در حال بررسی صدور هشدارهای بیشتری علیه عوامل نیابتی ایران هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69192" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69191">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
در پاسخ به حملاتی که اهداف آمریکایی در اردن را مورد هدف قرار داد، حملاتی علیه ایران انجام خواهد شد.
ما ایران را به شدت مجازات خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69191" target="_blank">📅 16:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69190">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rovYV4awLy6ObPW1OEC3xgWK9miNaxb1mpLLCDgkRrBX7qQXKoAApWyOS8RlpqmPRP1CAtBBAtBKSJ5Yjb68_Chd1Jblh2Ew_59sJemhtWNIi04ryd5FixeO6rOwBmydYXXBqNhSrweGGuZQIpkgyoHLH3btGXvJdmmyvXFO41zhpxdsHf-vzPdDdu77NRVHNBQLueudK-FLT3eTJjCast1PDI1JXysRYWyAJkQBaZTqupuXxLzhvWgMYkKQhkI4fWsN5qZrfNKQsKd8MGKa4jNTInHqMGugNqYtNystZDQfWHtaS5uhW_tYXV-mfQzGX8ZiasxKdKSWUqNH8EnMDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس تنش های دیشب، قراردادهای آتی نفت خام آمریکا ۴.۴ درصد افزایش یافت
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69190" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69189">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=uFcwzgblfzNGhv9hNMA-u_cMRksDd9gkidh9K6LnjoPdPGfcL97mhH9bGN7Zox3y_9v7cf_hdFFJj6n-RJqssMfoc5bANt_628Q8HDa9aTPOg1OW4hTfJBOfBMnoQ74TRf2NucStb8un4onvYLKwgv4mYySu87ejoVTi_QidkBVh-zJVamN4NP2u6I08U8djSfbqIEaqMtLaJ6pEGzX2-lQLwd-Ayd_G7X0hXIcyAzNE1ldts1nVVJ6_-rc_m77kAuU63w91h48nn4g1_sipVteDdkycJ-MRwunDZuVJUbD58WFH3FSHXQgvPy8oCVjTQDJhq3oVP8M5r23AhQQM5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=uFcwzgblfzNGhv9hNMA-u_cMRksDd9gkidh9K6LnjoPdPGfcL97mhH9bGN7Zox3y_9v7cf_hdFFJj6n-RJqssMfoc5bANt_628Q8HDa9aTPOg1OW4hTfJBOfBMnoQ74TRf2NucStb8un4onvYLKwgv4mYySu87ejoVTi_QidkBVh-zJVamN4NP2u6I08U8djSfbqIEaqMtLaJ6pEGzX2-lQLwd-Ayd_G7X0hXIcyAzNE1ldts1nVVJ6_-rc_m77kAuU63w91h48nn4g1_sipVteDdkycJ-MRwunDZuVJUbD58WFH3FSHXQgvPy8oCVjTQDJhq3oVP8M5r23AhQQM5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم ختم اکبر عبدی، مهوش وقاری وقتی داشت درباره مرحوم عبدی مصاحبه می‌کرد، یه پیرمرده تصمیم گرفت وسط مصاحبه باهاش یه سلفی بندازه
🌟
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69189" target="_blank">📅 15:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69188">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3KZ6hKhEpTPcZ_1huTj2OMvKpeX4YedpCWXQJDWCXUwXDHZh4csDYfLeg3NYnNE2q-wROjDu6iivqsTFqTB9Gyy1IV7T5YEYx9ZXqukbxflYRNjyAUZIhlJdyXYx851YrtWXZ9uYVI2xZONNHvrgGg4zJUpFNSxkLT1d9mdOrns8odjttJlmQYjj2dhLGjGRcKIjHRILbaOF2yTww2FKXHaFXu4GLaWitLiZXtC7gzkwgjCSTcxeVoVGAd0RB88ZnwSCMupphjSWfK9D8dmzZ3G6r2Skqa3bs9yR4i4Q1SjnyOfaQU7Zs9DcIBF1wM6Miyb-mp9EYKOWVy-ODJKCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.
۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک پدافند هوایی دوش‌پرتاب ساخت چین را دریافت کند؛ اقدامی که در راستای بازسازی توان دفاعی این کشور در بحبوحه مناقشه با ایالات متحده صورت می‌گیرد.
این خرید که ارزشی بین ۶۰ تا ۷۰ میلیون دلار دارد، یکی از بزرگ‌ترین اقدامات شناخته‌شده تهران برای تقویت سامانه‌های پدافند هوایی کوتاه‌برد از زمان آغاز درگیری با ایالات متحده و اسرائیل محسوب می‌شود؛ درگیری‌هایی که کاستی‌های موجود در توانایی ایران برای حفاظت از تأسیسات نظامی و زیرساخت‌های راهبردی را آشکار ساخت.
به گفته این منابع، این قرارداد شامل خرید ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی قابل‌حمل توسط نفر (MANPADS)، از جمله موشک‌های چینی QW-12 و FN-16 است.
این قرارداد با شرکت «ژونگ‌چینگ بائوشانگ اینترنشنال اینوستمنت» (Zhongqing Baoshang International Investment) امضا شد؛ شرکتی مستقر در هنگ‌کنگ که به گفته منابع، به عنوان واسطه میان طرف ایرانی و تأمین‌کننده چینی عمل می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69188" target="_blank">📅 14:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69187">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFm8hOnfw4Vo1yMHT5RWK1gyG-sxFfpJVwcP-m-QTuSQnZddlsgxkYEwdL0DUsCbhXg9x-cjXq_itQJq2sLAYeCkdxNEkYA7Lk3vurr7GjiY5pEPuudGVG4B15UlXSWUFinIYlh3esuaolpHfoMdsvYvp0AyD2XCbggtgUp1i0lkfgXKNb6ditWbGoF9ZHePtMBGzXLzLvd4R1E3I_ExIjIT9X0HeTzUU2zLyDlKwCLZffDyDpZ5UWbJJd6m1ksh10uPDbmAricM_Zgc-dA9EPaj_4RZhYodOt9hTGmVsUQ3NYo7DNk8Nw0E2VRhFyTcQsEzjf8RkuSUXZ5ttmChMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عباس عراقچی:
وزیر خارجه اوکراین به من اطمینان داد که
حمله به کشتی ایرانی عمدی نبوده
و اوکراین هم
دنبال تشدید تنش نیست.
ایران هم قصد تشدید تنش نداره، اما
به‌صراحت اعلام کرد هرگونه حمله به شهروندان یا منافع ایران غیرقابل قبوله.
خسارت‌های واردشده هم باید جبران بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69187" target="_blank">📅 13:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69186">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78f023144.mp4?token=oEdgRJnx7eIXjiNwAmnnb90m6AX2qPvwWDnsNUJZjTrlFV-5EbU7AP3FCX22GWqZS9w9mFRPFPgixBTWuKqO_4JER5I_1vWistonUNGadPZX4NIjTqiGT6AeOBVa-GlWP_eSiBIwSkERu2XvRU8CQ0BvFKUWObjqbhyTEvWFy4Hmmej5Su32DiCR2ABrtWXe5Kh4JiULqYwVMdd_txJe8ez8U72iq63QcfZIJ5IfTcxnlZN7Ltpg-T7QTvkgdfFJQtuYl6SXgTtZGtId8fWDaxHZxrOns5EcNTZpYBr3-wIdk-RFBSerj-KPIyO5zKig9ppN1u0vmVIzSAQrb3HIzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78f023144.mp4?token=oEdgRJnx7eIXjiNwAmnnb90m6AX2qPvwWDnsNUJZjTrlFV-5EbU7AP3FCX22GWqZS9w9mFRPFPgixBTWuKqO_4JER5I_1vWistonUNGadPZX4NIjTqiGT6AeOBVa-GlWP_eSiBIwSkERu2XvRU8CQ0BvFKUWObjqbhyTEvWFy4Hmmej5Su32DiCR2ABrtWXe5Kh4JiULqYwVMdd_txJe8ez8U72iq63QcfZIJ5IfTcxnlZN7Ltpg-T7QTvkgdfFJQtuYl6SXgTtZGtId8fWDaxHZxrOns5EcNTZpYBr3-wIdk-RFBSerj-KPIyO5zKig9ppN1u0vmVIzSAQrb3HIzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسیار کسان به این سرزمین روی آوردند ولی‌ همه آنان رفتند و ایران ماند؛
جاوید و پاینده ایران
🫡
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69186" target="_blank">📅 13:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69185">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBjrcXPrmR3YOIBDl18SydY3Pcj_GffLREmOi1C0-vRU9LHsMUQzzq70vrhjBys_AFY7aXBBcGLhuYcG6fQol6q5YTYUV4pspjo79cBHO8gpoZn6hiia1AQB0Ggauau-E9Y8W8Kaz1lHB3A_oKCwUadxI0yz8QaA-9XIMDSvNufZafG9B_A1wUogowSL7UchTn-5m0u1H16TBl81oHCp17w99KWnR5kb_72YfoYI9bAD7oShUtOtfl0uVQDh81FOwb2Ghi1SKZ674lKCB6O3iURFHs2Dh6AWsIpD12Vo-NhntNy9Ag3bVEKHV1qE8ejj5Q1wuq4s2piAHDbH-heGNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ایران پیشنهاد عمان برای مدیریت مشترک تنگۀ هرمز را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69185" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69184">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADwu5AxMPKQ19JuyhtuLsc1I8G6gNaWFGhkEgrlqSigB8SSoC2UGAPEZJYHa0y1fV6vHtrAiF-KYrB_F20O4G4EzLrdMLmRQlZ1hjg7LzieoiBF13Hn_RzdtVRIcIVuym_c6Jd4l1XNYQY1o_mItP-aLeiiv2V8RuNkvi0zbB9JRFDz_rUrVSRb54QCK8R6OCZlyKfflCs0UmIhBAnc6m34vZIX5NhpfESSoKykkARyX82yRKTeHEP5LtDUy6TGolQLkKicCfr1q7bm56FFy2lUidoDOx3fncJ5uZd2-Jjn4xg3lLY-Ld9nv_3AvdioRL1vrb8IKHrtCd1PJF7yZqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
نایا
:
موشک‌های ایران، همسر دوم رو لو دادن!
یه زن اردنی میگه موقع حمله موشکی به پایگاه موفق السلطي، متوجه خیانت شوهرش شده
😳
ماجرا از این قرار بوده که هشدارهای یه
گوشی دوم
که شوهرش داخل کمد قایم کرده بوده، موقع حمله شروع به زنگ خوردن کرده و همین باعث شده بفهمه اون گوشی رو برای ارتباط با
همسر دومش
استفاده می‌کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69184" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69183">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=JOdM-XzZVep9zLDVe9RFaW7vGLborYzbRN7FC5ZHRHEWAfhAUD0tEuPOlUbOQqt1MWmztdQgU7Zy0cBpzXx8owokwKj_yuR03bdXB_Z2W09W79MlAv2xCfUFCtHIvf4pKa9L2mVb3QkJJbmAU0ZSvcMnx6FWOVGGRW5fLivtuNcqdbPxMig28pDkSMiRAb2tTW3ViNrH-ZlJ-RfcJlJ4c4VZNvWJsWgmJ5GuiS8YFZ7E_Q23z2FufWe-vmhDjGnVfPqTP_AC1NXyGircfsjIUwMW30BnZn2cF8Xgan4xfDoYJETvX8tuRuQI4uXzTmHrMJQYcYXbEFpuQQw1c09NXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=JOdM-XzZVep9zLDVe9RFaW7vGLborYzbRN7FC5ZHRHEWAfhAUD0tEuPOlUbOQqt1MWmztdQgU7Zy0cBpzXx8owokwKj_yuR03bdXB_Z2W09W79MlAv2xCfUFCtHIvf4pKa9L2mVb3QkJJbmAU0ZSvcMnx6FWOVGGRW5fLivtuNcqdbPxMig28pDkSMiRAb2tTW3ViNrH-ZlJ-RfcJlJ4c4VZNvWJsWgmJ5GuiS8YFZ7E_Q23z2FufWe-vmhDjGnVfPqTP_AC1NXyGircfsjIUwMW30BnZn2cF8Xgan4xfDoYJETvX8tuRuQI4uXzTmHrMJQYcYXbEFpuQQw1c09NXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، درباره ایران:
من نسبت به این توافق تردید دارم و این را آشکارا می‌گویم؛ اما تنها راه دستیابی به آن، درکِ درستِ ایران از این جناح‌های گوناگون است. به گمان من، تفاوت این جناح‌ها بیش از آنکه ایدئولوژیک باشد، ناشی از ارزیابی‌های متفاوت آن‌ها درباره میزان سرسختی ماست.
کسانی که رئیس‌جمهور ترامپ را بسیار سرسخت می‌دانند، معتقدند که «نباید با این فرد درگیر شد»؛ اما کسانی که تصور می‌کنند «نه، می‌توان آمریکا را بازی داد»، معمولاً خواسته‌های بیشتری دارند. با این حال، به باور من، در نهایت آنچه تعیین‌کننده است، عزم و اراده ماست.
عزم مشترک ما این است که اطمینان حاصل کنیم ایران به سلاح‌های هسته‌ای دست نمی‌یابد تا بتواند با آن، تک‌تک آمریکایی‌ها را تهدید کند.
به اعتقاد من، رئیس‌جمهور ترامپ در این زمینه کاملاً قاطع و صریح عمل می‌کند و من به همین دلیل، عمیقاً برای او احترام قائلم.
آنها باید بدانند که اگر به ما حمله شود، با نیرویی وحشتناک پاسخ خواهیم داد.
آنها به خاطر آنچه که من گفتم، در دورهای اخیر درگیری‌ها به ما حمله نکرده‌اند.
به عملکرد امروز این رژیم نگاه کنید. این رژیم به هر کسی که در دسترسش باشد حمله می‌کند؛ به عربستان سعودی، کویت، بحرین، امارات متحده عربی و دیگران حمله می‌کند.
این رژیم به هر چیزی که در برابرش باشد حمله می‌برد و ده‌ها هزار نفر از شهروندان خود را به قتل رسانده یا دچار نقص عضو کرده است. این کاری است که رژیم ایران امروز، بدون در اختیار داشتن سلاح هسته‌ای، انجام می‌دهد.
حال تصور کنید اگر آن‌ها سلاح هسته‌ای داشتند، با جهان چه می‌کردند. این همان چیزی است که باید اطمینان حاصل کنیم از وقوع آن جلوگیری می‌کنیم؛ و گمان می‌کنم ما در این باره کاملاً هم‌نظر و مصمم هستیم.
مایلم کسانی را که به دنبال ایجاد تفرقه میان ما هستند ناامید کنم، چرا که من و رئیس‌جمهور ترامپ در این مورد کاملاً با یکدیگر هم‌عقیده هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69183" target="_blank">📅 11:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69182">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=hHMvHJsT_Z5lAZ0qXzAVyqLS2tnTlnv08bYQf8ym1MX9hyfaz0rt6J_ADwnnl3ZxDJELTWnF7uOYOF_e4pdK-N82arLdv2B78AVjTQRmhv635FSDrisVg4LF5jjpq5P8MFRIqsRSXPNUagzz8YrlVWxk9TyiJer2RN0XfkC8nANLsGUuhBA0HlxwOYW8occOIoPVIiWnNfrhj_pkrnWBfJqm5TIwf8mufQGn3P2UQjbyQX8d-Zb7o1VBoZ_NPMiuDUOpl49eYQ8KP9aQ5V59eCoUR475pHcC9i8wisK8ygH2sMBuVViScyvQ4D4EftNFlkMCl2HTNB4NsB9oslH92g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=hHMvHJsT_Z5lAZ0qXzAVyqLS2tnTlnv08bYQf8ym1MX9hyfaz0rt6J_ADwnnl3ZxDJELTWnF7uOYOF_e4pdK-N82arLdv2B78AVjTQRmhv635FSDrisVg4LF5jjpq5P8MFRIqsRSXPNUagzz8YrlVWxk9TyiJer2RN0XfkC8nANLsGUuhBA0HlxwOYW8occOIoPVIiWnNfrhj_pkrnWBfJqm5TIwf8mufQGn3P2UQjbyQX8d-Zb7o1VBoZ_NPMiuDUOpl49eYQ8KP9aQ5V59eCoUR475pHcC9i8wisK8ygH2sMBuVViScyvQ4D4EftNFlkMCl2HTNB4NsB9oslH92g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانمِ باردار رفته بود سونوگرافی ولی به دکتر سپرده بود که جنسیت بچه رو لو ندن تا اینکه با این صحنه‌ مواجه شدن؛
شومبول آقا پسرشون انقد بزرگ بود که تا دوتا اتاق اون‌ طرف‌تر هم همه فهمیدن بچشون پسره.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69182" target="_blank">📅 10:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69181">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTD6LAvKry22tRA-v_0OvICwTSnPVibPMFGg60_qfoSOGJm82aNws-cbX2raaB85wsUzT-cso97GKgJNO_mv4ls0H5WVPVGXm3Yyc6ctWcYRsyigCknU516nmzYRe0pHFJQZR5hBKxxGSqLrpIU82dBUZbW7bLoG5nDLWsmlZifCZLXZ163lUhxYwnlSnIgn5aLP21m_dtXZQWJjsOyv-hlKvJ8-S6tV4DyF9DAJW1obi1bGkiqiLBorJxTrdrNXAwxUzRJsbhv6lJ9BnKMCwkbk2PexGcKkVvXZQAUrnOQtzlvQ_xoEQL99lKJO4uZKixaS9chzRhm8ez3ndIz9LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه:
سه کشتی متخلف میخواستن از تنگه عبور کنن که مورد هدف قرار گرفتن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69181" target="_blank">📅 10:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69179">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=bQuqIez26dVhkuXh6gZsucHKr_yfgoSKU__yTCHvK3I04zUaRUSRo8CpOfZbkhLuqH7BKVNuhViYTVtDf-xy0C9h30INbCTzHWkCQSlkehAcaC_N1njjYjobCDqooKQFlk6iiCY1n0RVK4BVq5eKn-vAo_8ONrJ2ODgKT883dIwqAWhmmBjQF5QHuA2MmAs4bvWy2mk5ijVeAD84OWroR9xq7IL6pnDT2slmG-_xCHbgDbvbiet6N8TaMqrrWL6_NSHjmg45WO7TP2XWadBnJeHbvZr5kJd937rKWq5jSgfC0Tl894pM5TaXgtdrxC-VUhh8nd2TtpKQtCr2FyPVPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=bQuqIez26dVhkuXh6gZsucHKr_yfgoSKU__yTCHvK3I04zUaRUSRo8CpOfZbkhLuqH7BKVNuhViYTVtDf-xy0C9h30INbCTzHWkCQSlkehAcaC_N1njjYjobCDqooKQFlk6iiCY1n0RVK4BVq5eKn-vAo_8ONrJ2ODgKT883dIwqAWhmmBjQF5QHuA2MmAs4bvWy2mk5ijVeAD84OWroR9xq7IL6pnDT2slmG-_xCHbgDbvbiet6N8TaMqrrWL6_NSHjmg45WO7TP2XWadBnJeHbvZr5kJd937rKWq5jSgfC0Tl894pM5TaXgtdrxC-VUhh8nd2TtpKQtCr2FyPVPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کاخ سفید پست جدیدی از ترامپ با متن «کار این جنگ رو یه‌سره کن» منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69179" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69178">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305091e76a.mp4?token=eMFVhadSMvhZYoLiRfFKBjXriKJxnaA2sLfhnEOFQulDWccCL0sKdvvCZcwJFPCNoE634TNEP2R36Tm9Rk_5afP4nRDBb0ecR-pBCw0x9euPFCoh_gMu4deuYGvF3IlU-GAmer5VMoXdPQdXR986EBupE74ZrqQoqygAXSSgk6hFKJ3E5wkmi-R5wSmivx4krJEeO1DPPlSeyID_tDBDcQY3UWje1-IA002d8y8NIh6j9o7vLESrqGMGi2tpbCTQy9u1mjV8x9_4vAHsYoAifYz-mpZxWfTzbnnwIsZ6LKAfDNyqgRYlsWikES9KX3oMdtWTFirre_pK5hsIN5eLLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305091e76a.mp4?token=eMFVhadSMvhZYoLiRfFKBjXriKJxnaA2sLfhnEOFQulDWccCL0sKdvvCZcwJFPCNoE634TNEP2R36Tm9Rk_5afP4nRDBb0ecR-pBCw0x9euPFCoh_gMu4deuYGvF3IlU-GAmer5VMoXdPQdXR986EBupE74ZrqQoqygAXSSgk6hFKJ3E5wkmi-R5wSmivx4krJEeO1DPPlSeyID_tDBDcQY3UWje1-IA002d8y8NIh6j9o7vLESrqGMGi2tpbCTQy9u1mjV8x9_4vAHsYoAifYz-mpZxWfTzbnnwIsZ6LKAfDNyqgRYlsWikES9KX3oMdtWTFirre_pK5hsIN5eLLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از لحظه‌ی حملات عربستان و آمریکا به مواضع حشدالشعبی عراق تو استان واسط، که توسط دوربین مداربسته گرفته شده.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69178" target="_blank">📅 09:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69177">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74196ace24.mp4?token=H_iWGzV4EmDdfbcNW8kqR6-EjuXGjOs7I60KIuN2kDPow2gu37Xr60gxgkGKfSszdJaOU3SABLshDB_wTBIlsAAw2XNYlJYkUK9Ws2BHv_mayrzq3E24hD4tAvCEjIhyjUGSS9AddHxySskPKkbjjrWhpuXyqLGzyKRUiZXcyQlvWfITdNp2mlbnTvR8Zr798eF0V_nRqaxG9t2drJ2Hh2VZ6FdL7WARRJBvEHguwOAyMdX4h40JQo2PIs186xywV5IV_xhNixA80QgQytX3EOEbBbUFOzJhnlgaHt4ZG1HDdeFnNWa0fgGz3GFBTrwvYj4G89QJg3ZsvZ1uV2HB7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74196ace24.mp4?token=H_iWGzV4EmDdfbcNW8kqR6-EjuXGjOs7I60KIuN2kDPow2gu37Xr60gxgkGKfSszdJaOU3SABLshDB_wTBIlsAAw2XNYlJYkUK9Ws2BHv_mayrzq3E24hD4tAvCEjIhyjUGSS9AddHxySskPKkbjjrWhpuXyqLGzyKRUiZXcyQlvWfITdNp2mlbnTvR8Zr798eF0V_nRqaxG9t2drJ2Hh2VZ6FdL7WARRJBvEHguwOAyMdX4h40JQo2PIs186xywV5IV_xhNixA80QgQytX3EOEbBbUFOzJhnlgaHt4ZG1HDdeFnNWa0fgGz3GFBTrwvYj4G89QJg3ZsvZ1uV2HB7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
خداییان، رئيس سازمان بازرسی : بعضی تراستی‌ها خیانت کردن و با پول رفتن!
یه تراستی (شخص یا شرکتی که حکومت بهش واسه نگهداری یا انتقال پول، اعتماد میکنه) فقط 200 میلیون دلار پول مملکت رو برداشته و از کشور خارج شده!
معادل38.1همت!
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69177" target="_blank">📅 09:15 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
