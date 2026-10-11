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
<img src="https://cdn4.telesco.pe/file/JMKqRfaKIVQ2fMHNKU7rXbjRySqRczST6_KjXemvx1qtqUFCF5i-VyjPVLK0pt5t_UgL8xdnDwb4juznMRn9vsi_Qs2qh3eWHbHn3pNF-sKAjXqIWM8Xt65FGLvkpSeKqj7zZhzst0b3koLW6vd0DQgEuCFB_7toCmIugp7RSo-R7l-j5B4XduiyBFsAc9gZAmvjXDjuguWL2F5IT7raYY27aLokpKAJ27rnOZQfWMT_g5em37UXmPYnGNQbsfxWegLj8PdCrT5MtmdQYrL1ByrUiCcY9S9X5I3SZi5L6JAohL0Eb901C-NJJWsA9Ux_A5B9Dm_h_AJAd8gd6krqFw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 03:30:25</div>
<hr>

<div class="tg-post" id="msg-467609">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UX3GlAv8f1RAvUVpl3W4f6LAPgGgCveCGYwcT1CNlvd-T53MddiYs0sZf_eW1fur6hnQsGIFuUEQ2ZrO0JPd-vqiGvhEsdCaEnBLxQZ5uT4ULq683FUFNOI8C7HAMYfFfgvLEhytE_I01z51P2rNwwfGU_NhWj9_F2M7uNV6uTY4JQWBSs_m68BY6K_7y1ZgXYBJPGrAwwAsKOTDDRQNiMOLWuQhPaICGUnMubsSAcJaWsjgWoyib3sfMRi3gMLT1_k9Yvrp_IF3mdxPWZdsnTlRLg0mUdLDyijfjAMzrcwW4mU-HcZnPH3nGrSYWmfzLiCK0XQAQckLCpjzyJe3Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه داشتن کلیهٔ سالم را بدانید
🔹
سال‌هاست که تصور می‌شود ورزش کردن تنها برای تقویت قلب و عضلات است اما اکنون متخصصان متوجه شده‌اند که میدان اصلی نبرد برای سلامت کلیه‌ها در باشگاه‌های ورزشی است.
🔹
یک متخصص پزشکی ورزشی می‌گوید، ورزش می‌تواند به طرز چشمگیری سلامت کلیه‌ها را بهبود ببخشد اما یک اشتباه کوچک می‌تواند فاجعه به بار آورد.
🔹
ورزش منظم باعث می‌شود خون با سرعت و قدرت بیشتری در رگ‌ها حرکت کند و این جریان خون پرقدرت باعث می‌شود کلیه‌ها بتوانند سموم بدن را با کارایی بسیار بالایی از خون جدا کنند.
🔹
اما بسیاری از ورزشکاران و حتی افراد عادی در حین فعالیت‌های سنگین فراموش می‌کنند که بدن خود را با آب تامین کنند. این بی‌توجهی باعث می‌شود که کلیه‌ها تحت فشار بسیار شدیدی قرار گرفته و در بدترین حالت دچار آسیب‌های جبران‌ناپذیر شوند.
🔹
بنابراین اگر می‌خواهید از کلیه‌های خود محافظت کنید باید یاد بگیرید که چگونه بین شدت فعالیت و میزان آب مصرفی تعادل برقرار کنید تا ورزش به جای نجات دادن کلیه‌ها باعث از کار افتادن آن‌ها نشود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/467609" target="_blank">📅 03:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467608">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d25c5e1505.mp4?token=dt2_OUj2Hqge7sqPRlKdcjzy26RZnfbvpAa1FlADT4VZmqCDiw-xt0tTvX2pnQsdQscoWK5V81ca9Pe1VcfXqqd51frrnkZ-5Ab33DLQ1Ozd3mo0z7FGkY-W2hi7ahWXv9OrMZmlVqRR7CsJbh-giB0FQeSp3-WozI3dOrH23FXrk35KFKy1SYiQ6AHm-SMkbxr6gEmFAsvwZMRPEjUKq4vvjRU87H4kybO96H1gp4G6r-1GLITSNcwIl51oBrSF0_NF72orKZAdUllcd_27JV3VFCm4qMhLluovNXpxh-fDEoD8Z_8QjsTspgzUrFrExa9ryyXpEeyihutVF3QEIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d25c5e1505.mp4?token=dt2_OUj2Hqge7sqPRlKdcjzy26RZnfbvpAa1FlADT4VZmqCDiw-xt0tTvX2pnQsdQscoWK5V81ca9Pe1VcfXqqd51frrnkZ-5Ab33DLQ1Ozd3mo0z7FGkY-W2hi7ahWXv9OrMZmlVqRR7CsJbh-giB0FQeSp3-WozI3dOrH23FXrk35KFKy1SYiQ6AHm-SMkbxr6gEmFAsvwZMRPEjUKq4vvjRU87H4kybO96H1gp4G6r-1GLITSNcwIl51oBrSF0_NF72orKZAdUllcd_27JV3VFCm4qMhLluovNXpxh-fDEoD8Z_8QjsTspgzUrFrExa9ryyXpEeyihutVF3QEIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امام حسین(ع) کشتهٔ آیندهٔ مردمه
🎙
حجت‌الاسلام رمضانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 967 · <a href="https://t.me/farsna/467608" target="_blank">📅 03:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467607">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiDWMtu6WFE5RQM9TH2nvuR1hI5wZerh29gLazRP1Tg6CutwqO40M9ocQQh6G70WyMVX3ALs016SR-0EoqWrBPKxlz85VzytwwUsacfg4FSrmgZUd_WhOXfF084V_aU33gpDlQgDVRGi0oMgem5tl9nifbZAT-Lc55hFKE80kQjauu4zPshNGgsAw5cZkuylKHsfjfEpVTEBJo9WpxeWgVbEJ-FvIx8nR617P_kvE9N_v_lAptejqYsgUw1mSRCkrDFpXMj9hkIPnOsFujTya69wbdqmY-krQ6zhIQbjqmXy79445Nu3b3uXR2eLVBgKirHn-Rb-MLea3qLIUMdZ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها ملاک بهره‌مندی از طرح تورم صفر، سکونت در تهران است
🔹
زاکانی، شهردار تهران ضمن تکذیب محرومیت شهرستانی‌های ساکن تهران از طرح تورم صفر گفت: هر خانواری که در تهران باشد و براساس اطلاعات دریافتی از مراجع قانونی کشور سکونت آن در تهران احراز شود، مشمول این طرح خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/farsna/467607" target="_blank">📅 02:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467606">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">عضو ارشد انصارالله: حملات به فرودگاه‌های عربستان، پاسخی به حملات علیه زیرساخت‌های غیرنظامی است
🔹
محمد البخیتی، عضو ارشد انصارالله یمن در گفت‌وگو با نیویورک تایمز درخصوص حملهٔ روز شنبه به فرودگاه ریاض گفت: این حمله در پاسخ به حملات عربستان، از جمله حمله به…</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/farsna/467606" target="_blank">📅 02:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467605">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1792cb9b11.mp4?token=RTT5w8GjE3x8eb3ZA3YkWSeqnKiWGnmVew217-QML-YJ6Jj33YqmqK9Z9LkxOswn2_a0U5lS0AGHKddY4qgG1szMBWdm2GLSZhzrxE6xESFvHXQmGLD5I9r_js1C3kmXUlQycd0hQy4YKyGksPzdGJMNH1RFIjf-rrqj_LspNUXvOujssHeaAFWv7kicRWX876-aX1W5Wzl5itP8g-PGBoY6i2sG2Ex2T4t5S75mtTz1hqngfMQ08KteMr1RPR6HjQuEbpHfOiunEfR34aarrxrJME50DWBcQ96jg7oJeBlBrQnPZoCtzk2ReFwzEw2o9DDBbTD2AWGsf0BfYu0iEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1792cb9b11.mp4?token=RTT5w8GjE3x8eb3ZA3YkWSeqnKiWGnmVew217-QML-YJ6Jj33YqmqK9Z9LkxOswn2_a0U5lS0AGHKddY4qgG1szMBWdm2GLSZhzrxE6xESFvHXQmGLD5I9r_js1C3kmXUlQycd0hQy4YKyGksPzdGJMNH1RFIjf-rrqj_LspNUXvOujssHeaAFWv7kicRWX876-aX1W5Wzl5itP8g-PGBoY6i2sG2Ex2T4t5S75mtTz1hqngfMQ08KteMr1RPR6HjQuEbpHfOiunEfR34aarrxrJME50DWBcQ96jg7oJeBlBrQnPZoCtzk2ReFwzEw2o9DDBbTD2AWGsf0BfYu0iEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای حرم مطهر رضوی و رواق دارالذکر، مزار رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/farsna/467605" target="_blank">📅 02:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467604">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🎥
ترامپ: ما به زلنسکی گفتیم هرکاری می‌خواهی با روسیه بکن، اما به پالایشگاه‌هایش ضربه نزن اما او دقیقا همین کار را کرد
🔹
ما یک مشکل جهانی داریم و این مشکل ناشی از کمبود پالایشگاه‌های سوخت دیزل است. پس او چه می‌کند؟ می‌رود و به پالایشگاه‌ها حمله می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/farsna/467604" target="_blank">📅 02:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467603">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی انگلیس:
یک فروند نفتکش در پی اصابت پرتابهٔ ناشناس در تنگهٔ هرمز دچار آتش‌سوزی شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/farsna/467603" target="_blank">📅 01:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467602">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfYWC8xUtdCs1QA9KTmWbqOb5K1goT_Q_0c89Uie9ow7cznvw4yC6d8LwTLlLzitvKivQ3gnwH4FS8EjglhwdpCCUSkAAs4IkflvaU1Y7QsLUzK3wtQiaSbhzjNuMIeJ2hTOlbB9EGuIsvmS8gc6ZrywjuuPv4pkNpdy4hGWUVyB5cgZCUsvPw7lzgQwpgTu1fLfrOOBySRC_-kTY-kWOpKI-x1kWnu3lG12atQ2NbJcFgn57Mxffaf-i2iOAjbT9FNRs3hGV7c_-MHEyCeKLxFOpGY4FVD-NWcVy-KjbIawQjp9PpbHdci21-29ZI8sviqfox3V2Uf62kQs7Vjq4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ۱۲ کشته و ۵۰ زخمی در حملهٔ موشکی یمن به فرودگاه ریاض
🔹
نیویورک تایمز به نقل از منابع آگاه اعلام کرد حملهٔ ارتش و انصارالله یمن به فرودگاه بین‌المللی پایتخت عربستان در روز شنبه، دست‌کم ۱۲ کشته و ۵۰ زخمی بر جای گذاشته است.
🔹
به گزارش نیویورک‌تایمز، این حمله…</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/farsna/467602" target="_blank">📅 01:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467601">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25361b78ac.mp4?token=Tn27L8-WtkkHPj_k5LF8naV7CVbFY_1UE7QbVx3fRWTT_dhg0TLOld5prNdFoIyW9W_4k-vVf2fVAZ_ulhv3NXC8OnrSatCEyUbtPQpkCaZx1wM2EOLttSQnpTkdi8hMIJo_HGcgsVawmbJpgHMDZ3xKl9oNiBuaxzxrwwc-usb275YOI6KhRSc9tctIJCr1emBJOuoouYSdpCevVe0jK-KYyzYs552pCUZWiPlpGcpPPjRN6-F2GOsWxnId110VAsP2yyUqpjBbgsSnsVg_iuj5QhdwxXlSrtHDcRgUtXOxAnEBL2S2m1AkmkNYGIRriV9XM1PAwktmibXSjZzHEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25361b78ac.mp4?token=Tn27L8-WtkkHPj_k5LF8naV7CVbFY_1UE7QbVx3fRWTT_dhg0TLOld5prNdFoIyW9W_4k-vVf2fVAZ_ulhv3NXC8OnrSatCEyUbtPQpkCaZx1wM2EOLttSQnpTkdi8hMIJo_HGcgsVawmbJpgHMDZ3xKl9oNiBuaxzxrwwc-usb275YOI6KhRSc9tctIJCr1emBJOuoouYSdpCevVe0jK-KYyzYs552pCUZWiPlpGcpPPjRN6-F2GOsWxnId110VAsP2yyUqpjBbgsSnsVg_iuj5QhdwxXlSrtHDcRgUtXOxAnEBL2S2m1AkmkNYGIRriV9XM1PAwktmibXSjZzHEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیپلمات آمریکایی: ایران ممکن است این‌بار حملۀ پیش‌دستانه کند
🔹
«آلن ایر» دیپلمات و عضو «مؤسسه خاورمیانه آمریکا: در جنگ میان ایران و آمریکا هر ۲ طرف امیدوارند با افزایش فشار، طرف مقابل را به عقب‌نشینی وادار کنند.
🔹
باتوجه به این‌که تهدیدی علیه موجودیت ایران وجود دارد، بعید است تهران از اهرم کنترل تنگه هرمز صرف‌نظر کند.
🔹
ایران هم ممکن است این‌بار دست به حمله پیش‌دستانه بزند، چون تاکنون ۲ بار غافلگیر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/farsna/467601" target="_blank">📅 01:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467600">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/467600" target="_blank">📅 01:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467594">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ImNA6Nzq-xGNr-tsJpWuxLe01nC8YBDmc0bFcwD_W2iYLI9zieB8P5sq0T9DwrACOPDc04W6wXLeZUljsOiQg2U1cxYO2d2ly-tGj9DEqAsHElGBcRx5163jUDxdc73SOp3gynE0aFcsExjquRO5RDgno4ZouD8cL7KQHLlwvbvFlX1tGazRnuLqbuS9qa91i4m-4ZNFQu9u0oskTHpgKVwkyMoCjtRfqha0Zxr3-GCEa7HgMDcGp3F-p8nVvJJhrdA4pOFxOAniTQrp8y0R8NU54bNVYDqBtda0qGwO36JM2o2qOWM0-9RQOr8GOTg3ZfSiTo5DaJWGOd9tEtO8rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gWz6PTcMV9Gh5kBp4TDFEclekuF0VWpgAgk8-Eni_Dsry78PXHQSOyyL_9q29Jj-igOPlZ9p6F-kdstcQY4K5bWSTGrlV65kCDWPZEwSgPb0SMHQP0vDwwQFkCNLME1cfC9J1ZDqwEds1_bYolB7bn4EaeDNj1ptcb46CipLTSa21KTEB_SUuTkAy4rrmNNZH1Yyym0Y6e4mLJXP8egQdCDPcB4X8l6_kmG7T2VSBJu3xrVU4zzRl-rDcNGCI3IBqjfuBjKxc3zs73Y9bDrYbWjhFTcIdZHC60pgtpjhraJN69xJypZPjMIl30bkp9-e0LgYoSS_YqHX2T5IYgDZTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tf0GIFwsDMxURZ1tCxUnWgoCBDwLgAZGUu3VrOzhOVxPWG0Qaf26-nHcn_UeEfW4uQ3ek7gXB6Dk9Wm7dYixHCrBvdr5s41L7uKjGVGI5mYb_-PEB59jE8UROryvWbcR_4MnqTmGDPzD0oTUxF5g4X0tB3ye_GVubeBv_L9zNRLKQ2rrG-o45dEq3I-bsiMltXD1T5mYx_eLlwbpn98fPAYmbd6fDmB9xohHB3ItUfqE6doBfMW5QmSdJ50rqVShgj3B_HFAxwcHzU4FW6Bl3lk9SHflU3eTtyJcTitjoL-K2gMqOGO6J563nfwD2OR0JRJGJqMk8LFAv3A3eKyE7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R2pQ0wPm1FJFk7gotmQg_gP4g5OxepZF0eGY18p-NqlXbk5pvuSTtSODGgdF-Ga7wi2X05XDJRgmkm9l4Lc43RNDdsFhsjH2DuvLCouG8OmRNoGSQkaDF_O_Mwq9dOkk1LhF6AmsR-TopIIZLbqNqLMfhYF4fq7Zsu2xID4iZA0MVar86M9amtoF-9UB6tybi4Bs_twsDC1vMiXByMAEa_J7uL-iWzx5n39ccJfU7H4nDPEdj5ALdQWHldm4KBMfUuyxRVFRX0LVpoq9z9JS0NN0acS7ApCFB33jIo3h1LxkNl4xj9WIZUFbrvYD1RVMIdqG1VhP4ZzT52JVADC6pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mpN9GXGb8TD3LimSSjYcQ71KIYmS4ul2fZDnVGdXnDm8cDHAtxgIVVCDc8VVY4-KFoHRiy7XSRszjaAw_WgJXzZ37bNgyw_4IoN5vySSV2rtIQX1MCJXFgVlxQvTvSFk2uBURlfLxSXhRYvrdTKqT4Ns3UQqHLnFDSwYb0gpf5rntg77mCgMi0ZUCeoYnNLrpAykK8maDqFOG9vHCNy20p_CCs4Ifjb7a8mFf5GUPiwepQsq6wnEYW4WmS8oVnq7sNhGCYZj-AWN13F_UnyTnmn3MM-Ug4xYHNo7G-jdJJHJXhtpofkx9QHmLIiqh_2-tfB3UJOLqNcEGBQMzqtncg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gjDiCcHKs3NhVyw7kphRwU7SOV9M35Rn6AWQCNi9apaFks0A7ZL0AxHkDAnI-itvdumvWB5kQRxrh-eX9_e9QaQi92V-OfacZRwn0yF8yRkCFteiYNskFoJ53v2qraq8dFUBaThExfERA4_y7CC4EZdTx_2FZ5J-P9dnN04i1w-XXpnVBaBiduKUuFWjfQ419n09cqeeCX-NA1aMlW-T_MQVHwhIpd-TIDKPjU6u6zAu5tPH3O4YozewwWos338zXR8oTwhf-qKH3RRctcEK98Clz7vUHl6uzp-eggdTnU8-XldREt12FqVPL1jgiGStdRNW9CxyPO2XsGNXZogFpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اجتماع شبانۀ مردم نازی‌آباد تهران
عکس:
دانیال همتی
@Farsna</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/farsna/467594" target="_blank">📅 01:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467593">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8ewKRl_Z5x7p3SGD8D6n6OE7ISXW3GKI1yPI3RyvOBIa_z7TPg28stXI-hkkXW5QpZewtayz-aO0Bg_h31kBYqIg8mlkL-id5kj6JHg3_sEKKwad65roj2w6poQvxHQoo5OXQtxYa_4STLpqDKnFDtDG9MtMA4mdwsfGd71Nr6SvXAEbR4GYTNCQViarf0OD_k1JtcUq14aIZobJb_02FpMpAniSNAtDl1XUldHTD2KZNNDIitIWu2n-_EsCRsswGNCm-ELMYYmFMJp0ZGUtLXc5W0bq78iBDmjYHlcF-m0a7LlKtu5_W_gaQOQTm-ljrED6IVSaLhpl0Zrht9zXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقایی: بی‌عملی اروپا در قبال تحریم دیوان بین‌المللی کیفری و تهدید به برچیدن «آجر به آجر» آن از سوی آمریکا، همدستی در حمله به قانون و عدالت خواهد بود
🔹
سخنگوی وزارت امور خارجه در واکنش به تحریم‌های جدید آمریکا علیه دیوان بین‌المللی کیفری و تهدید به برچیدن آن: مارکو روبیو تهدید کرده است که اگر متحدان آمریکا دیوان بین‌المللی کیفری را مهار نکنند، واشنگتن آن را «آجر به آجر» برخواهد چید.
🔹
لطفا دههٔ ۱۹۳۰ را به یاد آورید: نظم بین‌المللی نه‌فقط در نتیجهٔ تجاوز، بلکه زمانی فرو می‌پاشد که استفاده از زور عادی‌سازی شود و جهان در قبال آن سکوت کند.
🔹
باید از اروپا پرسید: آیا ایستادن در کنار یک متحد به‌معنای دفاع از حقوق بین‌الملل و نظام هنجاری-نهادی پس از جنگ جهانی دوم است، یا همراهی با او در برچیدن آن‌ها؟!
🔹
اگر قانون و عدالت برای خشنود ساختن متحدی متجاوز و زورگو قربانی شود، سخن گفتن از حقوق بشر و نظم بین‌المللی مبتنی بر قواعد، چیزی جز شعاری توخالی نخواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/farsna/467593" target="_blank">📅 01:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467592">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMl8noEMuFHBaQe82b7N4QEhitRc45Q1n98RkGEedS4-kq4Hd53J3UPgW92dXMfZ9Nz-Ff6CvjT0dXOHwqv3qegnVimSXo2SUmMrNK-4QxQjd5DVuOKR08H8iknZsv1AIax_8CaWRygES-YfeIbjunl2sUZJponyMaiTWPIt2W75j38rsA-x2siPpN4rn-GFZaRLcTF_zslH2plhimIJVC1rQ0Gjxp1Zdl5OsxpCza-Mu31DY0lSB4ALE1HbQbaunnzOEQpp1Q93C9j_WZSpxcMn03hvayXQNvHpaFfOMNszIDUiVW0LMqDl9qGFvmJMLZdATXqB2vD6bumDZm8qAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
بارش شدید باران و آب‌گرفتگی خیابان‌ها در گرگان   @Farsna</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/467592" target="_blank">📅 01:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467591">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d9fabbd35.mp4?token=VU0QD7fRcLTXuoj87PVVfGxyj2dHJGFPiOjzTC2WBoBUkLjvNSexz_Fw3TxFB3i5exprMXLk925OeDHz30ZKLV9AD-bMvcV5QxwRAEK2DS3GzqsHTXQHWkBVUmbl0xzp5A4f8pqVFfzBLT7xnX4sW_93OOoRHq52rD90me0hd5_eAXWDlNBtLhUiBvhqFBjpZGwSFWC73pTzjVymtuNiADgwwoXRs25qiYL42K7v_k09bqIqKcVifrfCig37e9E0hR_1YKAi7Nt6xaU6NiaHdE9ket_NeHVeFMWJXRRGGVtJ7UNYg2LeW4HKBshcEEUai32utF1vof0WIhFa9J9ICA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d9fabbd35.mp4?token=VU0QD7fRcLTXuoj87PVVfGxyj2dHJGFPiOjzTC2WBoBUkLjvNSexz_Fw3TxFB3i5exprMXLk925OeDHz30ZKLV9AD-bMvcV5QxwRAEK2DS3GzqsHTXQHWkBVUmbl0xzp5A4f8pqVFfzBLT7xnX4sW_93OOoRHq52rD90me0hd5_eAXWDlNBtLhUiBvhqFBjpZGwSFWC73pTzjVymtuNiADgwwoXRs25qiYL42K7v_k09bqIqKcVifrfCig37e9E0hR_1YKAi7Nt6xaU6NiaHdE9ket_NeHVeFMWJXRRGGVtJ7UNYg2LeW4HKBshcEEUai32utF1vof0WIhFa9J9ICA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش شدید باران و آب‌گرفتگی خیابان‌ها در گرگان
@Farsna</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/467591" target="_blank">📅 00:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467590">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‌  فراخوان پزشکان از سراسر ریاض برای مدیریت وضعیت اضطراری
🔹
در پی حمله موشکی به فرودگاه ریاض، پزشکان به بیمارستان‌های سراسر ریاض فراخوانده شده‌اند تا یک وضعیت اضطراری جدی را مدیریت کنند. @Farsna - Link</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/467590" target="_blank">📅 00:49 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467589">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8UDGgEEZ7j3fukMgYXqBO2Ll3ZMBiqLByAylsghQncOGEfWO5Gan4dNGnknFP0HsTuY4TkKkR-ItkC17hPjFGpSdmoMpht2ZMTdYAq_Rk9R8iIZumSJLjzStlrvsjdFeQkA1v_Ybe5xRJe3zfzSGwMNqZX20nFpo8gLhSt0bsQFBCFpEnXsCxDtIfGKHPVa7uIXVuNwshoCQuRTd7WB3QEnT_zVTNPER08MC0RhSbMD5MS8fyYBJWXkVjV7rON0fmqrQkgC1AC9wjwyHnAyrlm3x_-VGTuWjTiF7dAzH9iM7PPGB-gw4lqRVlHpWo0qKkdAuCr2HhkCYqCkS7nRIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ممکن است نام اقیانوس آرام یا اطلس، و تنگهٔ هرمز را به‌نام ترامپ تغییر بدهم
🔹
رئیس‌جمهور تروریست آمریکا درحالی‌که سخن جدیدی برای گفتن نداشت، با تکرار موهومات تکراری خود گفت که ممکن است نام اقیانوس آرام یا اقیانوس اطلس را به «اقیانوس ترامپ» و همچنین تنگهٔ هرمز را هم به «تنگهٔ ترامپ» تغییر دهد.
🔹
او سپس در ادامهٔ یاوه‌گویی‌های خود، ایران را «کشوری دیوانه» توصیف کرد و گفت خودشان هم این را می‌دانند. من همیشه این را به آن‌ها می‌گویم.
@Farsna</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/467589" target="_blank">📅 00:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467588">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">عربستان از هدف‌قرارگرفتن فرودگاه بین‌المللی ملک فهد در دمام خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/467588" target="_blank">📅 00:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467587">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmtXrqWJFQrFQ8-lRq4wQYeL1jJ38aOxgIuoZfektwLC_CH0Kt7MD36nq2Bp5_EHsGmyNlJ8s8YohDZzwgb211relQH-kekWTvstjGh1grjU58rPFTyiW6nA9pibPLAgAawuUF4guaDj5MsU90Hw7QSFyA7SLcIMZYgdksKs5-yrhbhScm51f7ArH2Cvvx2iPJsrbSgrI59TY7TKwnnMkTzrYwKMr48i5tI50h9ebEwBrSeIH17KQaGtJF5rl1ZdPvT71R6XqVReUVPPrcYaB3_ZyvWuzsIG-pwENJ3Res2UeFSLe1kc-TJzhFP6OMVUHOkXf84GyopoIUc7KgF32w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سوپرنفتکش متخلف در تنگۀ هرمز درحال سوختن است  @Farsna</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/467587" target="_blank">📅 00:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467586">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foUHJ1s-KQWhJ8S3rlC2H_Gyd3fdzELinD_w1ogK1UvwGevPyM_h3Sjr5PCVBArf_cPWQu0UJWsUmGxGaSc2sxbxLepEfeNru6sTkBYjR1ifAOmhGNGguhZ6nz2b59NBSLGDM3fuTysSZRdmeIcSufgUOPg2tqNjP-bPe86INwdUXRWkGC408KjYg9AcV9Uet8jcv5rCwvLHSr1ML0GtUkXYSLDRfR6DUm5_jAJPofYTyux-X0XiBljP7p-po54GQDDX-0qFFHnSvjUpY9STFygL7cdLF0LGdNz6uUg61QFqPD240GfpMJG1AegltJEvCl3UJQGdL6Hj5sX0fPV6OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشورت با شکارچی!
🔹
ماهی‌خواری پیر که دیگر توان شکار نداشت، برای سیرکردن شکمش نقشه‌ای کشید. با چهره‌ای غمگین کنار آب نشست و به خرچنگ و ماهیان گفت: «شنیده‌ام صیادان به‌زودی می‌آیند تا تمام ماهی‌های این برکه را صید کنند؛ دلم به حالتان می‌سوزد!»
🔹
ماهیان نگران شدند و از او کمک خواستند. ماهی‌خوار پیشنهاد داد هر روز چند تا از آن‌ها را با منقار به برکه‌ای امن در آن نزدیکی ببرد.
🔹
ماهیان ساده‌لوح پذیرفتند؛ اما ماهی‌خوار آن‌ها را به بالای تپه‌ای می‌برد، می‌خورد و استخوان‌هایشان را همان‌جا می‌ریخت.
🔹
چندی بعد، خرچنگ هم خواست تا او را به برکهٔ امن ببرد. ماهی‌خوار با خود گفت: «خرچنگ هم طعمهٔ لذیذی است!»
🔹
سپس خرچنگ را برداشت و پرواز کرد. نزدیک تپه، چشم خرچنگ به انبوه استخوان‌های ماهیان افتاد و به حیله پی برد.
🔹
پس بی‌درنگ چنگال‌هایش را دور گلوی ماهی‌خوار انداخت، آن‌قدر فشار داد تا پرنده خفه شد و خود با هوشیاری نجات یافت.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/467586" target="_blank">📅 00:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467585">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIwDr2jWh0vJYmX9vb1FPrXrMtRekNZwkLLQc-mqgpTLoNm5IbNFFDKL9doa4KC7wxbwNFlCZkZsWP8xk9Vytycp9dBWJ6f58FU0G-da2uTy_4VmkaWx11sThQRt0Fg-0TutCOmZrkNJFbIvj4s4p-S5tZDZ_JkK2kLN3TrYPvpCtFcVcwnjNN-U6Hgt-kQ7j9-KYeNHbjH9-HnIAj4hBANSG5eSuIpJIHE7ojIf-CC1dinWD5mgXTloVAvh3H88Sohg_DPXGtHtCLJ4G7MO2PA-OrEGlPYfI5E1VPBhUJX1K2ztYsihTXtK_dwzDoI7DoNPYx95jeaULlfeOBZFkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس را بدون اختلال دنبال کنید
🔸
به‌دلیل محدودیت‌های ناشی از تحریم‌های آمریکا و عدم ارائهٔ برخی خدمات زیرساختی به خبرگزاری فارس، دسترسی به وب‌سایت فارس برای برخی کاربران با اختلال مواجه شده است.
🔸
برای دسترسی پایدار به اخبار فارس، آخرین نسخهٔ اپلیکیشن فارس را
به‌صورت مستقیم
یا از
کافه‌بازار
و
مایکت
دانلود کنید.
@Farsna</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/467585" target="_blank">📅 00:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467584">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceaea963dc.mp4?token=ldyohFwg7dpXlwwCjqYY4e1BjoT0qi8Yvzlh2Dab4jcRW3rKPqoQ8AYfKPq3ZHD8ZARubMdJIwkgOwN43wXrRBR9Oo-Zebsgi7KeIYMdixqMxrH13jOHzm5AAlXnnQ4GQ0X-rqicYSvOLUNoeFOxHj6y-yiZ7iOIj1meT9kI52K0KgBpJoZpFtaQcK3lm9_3Wy0lmWaVv9_Oj3unwQ7Ril0FOxxUuPLNynlnXrsA1QOmsM39CAS2mf_y73w1ZcZHaZ2DrK7SdfxfZaX0-avAQtyaG4zs3nJuAOUpxTjjqwy43iRAm-E1vUFd9RvQ0vXxJkQaNSt_hf2xYjpTMQY2NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceaea963dc.mp4?token=ldyohFwg7dpXlwwCjqYY4e1BjoT0qi8Yvzlh2Dab4jcRW3rKPqoQ8AYfKPq3ZHD8ZARubMdJIwkgOwN43wXrRBR9Oo-Zebsgi7KeIYMdixqMxrH13jOHzm5AAlXnnQ4GQ0X-rqicYSvOLUNoeFOxHj6y-yiZ7iOIj1meT9kI52K0KgBpJoZpFtaQcK3lm9_3Wy0lmWaVv9_Oj3unwQ7Ril0FOxxUuPLNynlnXrsA1QOmsM39CAS2mf_y73w1ZcZHaZ2DrK7SdfxfZaX0-avAQtyaG4zs3nJuAOUpxTjjqwy43iRAm-E1vUFd9RvQ0vXxJkQaNSt_hf2xYjpTMQY2NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باید علی‌الاصول، دشمن دهد تقاص!
🔹
نوحۀ جدید مهدی رسولی که امشب در جمع دانشجویان دانشگاه شریف اجرا شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/467584" target="_blank">📅 23:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467581">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PMQB09HQfrryrMiKdJhsf-IteD-K0I1wcNZ2UbFksEKMFqKAFEMgUAlABOPv7lQF3O_rIQjqgKTBdpUIM0rkRyN49B9f9vNXRBslLUgwq-fWdpY-tyTEmfCHdWbAjrs3aTi42Y6xheGk0Og7WJvFlPcAjRUS0PjBU9PwZkHLW23O38ejgzZYGacojTTdEPUjdPptXnZt7uoXPFOqFfOSEBXU8Vgh4fPzqIXR6-tBz5SsGegnsEwUu3ui7K4GVKri2YMCRw1I_gT5C5M4dMV-MTwj9DoproQz8TzLAFHJrAZWSrEj6vm2coUZOP5vORCDyRExbshxZmKlQPfn_I6B2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y5zrLqD2NsW4FIN3ekJQzKbQBDAklxRK14BXl2iqNqLZBNu7BAHE1CeTSrRM8TBLq1myzHmxHfaOHlx8E_T_d4FlMylh8w30rOvGyAl9xhUkSY6K5dcS6fd9vjtQx6hPI17-SMLMLNCXuUtVImpcnRQGGuJ9V4Ue9be3qlP74e3jmC-9Mv9pwwMDwwmj4ew_KbVOw4mbp8Qsf1xD-AeQrnwiyVJuv-9c9mBpOYZe8DfhXfDhg3dMgbI7JwlJzXyyuVSBYRbJC_poVAvuk35k46qVNwzsGISXqcuWdibdKe46AFriqJHeR02v1lK56udmgd5R9j_32W1TyJj73uCJxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OD2Mu-V3J5qIcmkTZhPvdiku8YtJiWoAGFyKWK3jCevGbaKkyG4EJ6p35UaWOUsbhB7-2jisYJmZbuyJmjBvcnH_vXh-CQHnTWVOJCaqgxyr5SwARUOFbs0XnKx7X0JW0sFyy3bQvUdpFmdiQWoHxGKaw1C9WyNcoq0rexq672PoNhpfaLvHTIA1L0SaY6-y5tMYJqhuxizFQfHh5T8RFxedLWn38UckTvWz6krpHc_LIztqoDNB0oYUdDQEMuW0N5NpCOpfqM5MD7dK3-vy2HIjJKQG8AcG-NGdXblQy4BPbjAqHnaKcDBBHzZHWOZEbTFEfKK2UkxigzkqVAQgfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
امروز چه اخبار خوبی در کشور از راه رسیدند؟
@Farsna</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/467581" target="_blank">📅 23:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467580">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">منبع آگاه: ترامپ در آستانۀ انتخابات به‌دنبال مدیریت بازار با موجی از اخبار اقتصادی و سیاسی است
🔹
یک منبع آگاه در گفت‌وگو با خبرنگار سیاسی فارس اظهار کرد: فشار کاندیداهای جمهوری‌خواه، هزینه‌های جنگ، آثار اقتصادی آن در داخل آمریکا و پیامدهای تحولات مرتبط با تنگه، فشارهایی را بر دولت ترامپ وارد کرده و در چنین شرایطی، انتشار اخبار مرتبط با تحولات اقتصادی و دیپلماتیک می‌تواند بر انتظارات بازار اثر بگذارد.
🔹
این منبع تأکید کرده ترامپ از شکست همزمان در انتخابات مجلس نمایندگان و سنا و تبدیل شدن به اولین رئیس جمهوری که ۳ بار استیضاح توسط کنگره را در کارنامه خود ثبت‌کرده است، واهمه دارد.
🔹
وی با اشاره به برخی خبرهای مطرح‌شده در این زمینه، از موضوع
واردات طلا از ونزوئلا، پرداخت ۵ هزار دلار به هر شهروند آمریکایی، احتمال رفع تحریم‌های نفتی روسیه و عرضه ۳۰۰ هزار تن گازوئیل این کشور، توافق گروه هفت برای آزادسازی ذخایر و همچنین اعلام عدم تصمیم برای ورود به جنگ تا پایان انتخابات
نام برد.
🔹
این منبع تاکید کرده مجموعه این تحولات را می‌توان در چارچوب تلاش واشنگتن برای مدیریت فضای سیاسی و اقتصادی پیش از انتخابات بررسی کرد.
🔹
به گفته این منبع آگاه ایران بر حفظ تنگه استراتژیک هرمز و‌ کنترل قیمت نفت مصمم است.
@Farsna</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/467580" target="_blank">📅 23:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467575">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AaBc-kdINl7LiCAJb34323kdId2nET2aABs69Ca6qtH8QU8xVPL9Ebr16Q7H_3gopj_mWtbHUT4hgVUoNyWp66SfpPVCADDgfEZ_SSRrKTo40cr7nuFxv-XD_Y93CSigD7iYG4gY4P2_mQrAT4Gy3QcusTmhSapjmyHpK1b_WlXLCB3PYhCpAJWreeZgQ3ds6-1hhoRRXEdWvgelQcc9PwC03T1Y37DdVKgBYhUwOGmufrptRGZVlGXVitBO1IYYYOlE3RT8E6RZl1-78iiuRYezK1d8d7_gxlMqkxg-bRmuusvgpAaFZf_6t9B7bpOWVepokj1E4AnS36LgqVo2gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q-sI70noyKWhtD2YJT3yMGsrVba6A7StMbP_PeCjXgBtXDmFl6J9pfqwlCCwbBvQ0MLDEPtIhiGO3heF39F_ip0XsrELyVErpdg5mY3XAqwhZeC62S3R7eTgGEZH03ABQrvq5WQIqLGWWu_XyNzWDGVRTVhAW0-UOM-mF8MW-pnp5noaeQUwi0eZhnfIDRzmg0tdcjtSkHbsXilDYP5Ph8ebGeA9G-2EzhFzwn8NwW-96hq0-k4jVT3mK6HGlAzjJL_x3byEmnnRqi5y9u3LRPI7EAk7gp3RnqFuU7IxQUvZyGO5P9K47aKFeszs6v_fLoRpHwndOKfxtsugJmGoRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cepBaBwnOxe-MStNU3r5tjvZlNmkncPFHZSWt1GYJZESzErNEVEET1Y5xV97d1UBgkcnClgVGlsxf3Dr28ruXA8_YdtUGiLFq0U5d5W0dFxgo8CZE9Myme3kIVnUWkk0_lsz5HjbYu79PIF9fBOtN4YgZqXOs4F4l8CecvmVaQe0M3tUQnIWqEBnv-5Pawvof6LTPe8uk3A-Z3pqQxr1kAUjHt9eUSZL7LkGkqfZFTRsUJj1l-6BUeMtDeUUQPa8YDD_voIR8DmE7yDn7ofAadVXVmu3urukjrDcPVa9JZl8zj2KDaaIiH6Vm3lsbU--fNbP27LFanDWPCbILpL9qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KoQCl_SXRnQmPlOkRZsellF_SV2hxjyUFlmkP-tTtlEEeVILR1j9xbfKosjh7sbrBiap-fxThTcTq8OSv2-t7QZqarTQO1GPb9dlypQYAiUCVCkkUIXygb3wdszHD36ZWknqSWTYdNQs-4UBSBBv6ucjb2dZgvjrcx5aGnr_LXgu2Z0Cd1pTsdutjSnu4VZP-FpxmkJMR5w0tP-SngEFqmVOAVm99fhu8tf0Rkgw3t-4YLQ-6KwRJDqj2ukYJYZ96ipHCml0i_ElbatpkJX9k0V0jyXo0W7TNY5pRg7nv6LRJYT9YH9hwBqiEJbCAR_p95Ij5SDfQ-lqKc4TVfXzOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تجمع اعتراضی مقابل سفارت فرانسه در تهران  عکس: محمدمهدی دهقانی @Farsna</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/467575" target="_blank">📅 23:44 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467574">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">پیشروی ارتش یمن در دروازه غربی شهر «تعز»
🔹
منابع خبری گزارش دادند نیروهای مسلح یمن در حال پیشروی در ارتفاعات «صبر» هستند که مشرف بر شهر تعز است.
🔸
همزمان با این مسئله، ارتش یمن بخش‌های گسترده‌ای از ارتفاعات راهبردی «هان» را تحت تسلط خود در آورده است. این منطقه، دروازه غربی تعز به شمار می‌رود.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/467574" target="_blank">📅 23:35 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467573">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mS1Q3qN2ywuN8g6J3_vGQBt5FtN6sJ8eby_COvsZLRWwE7QG5Kp8atUXs5KU1BTwS13_4fkj6iiZwv23QmXm17bkCbnqdI2s2sJ_AH9te6fHETIX9HnO2mAeabJn6ye-macFfvH9vZZhm1638jdI8HhPcE2viMWo-jWZPbkXegnrWzrgNqObUFZpE226M37bt1ZcTxQABajX22wb3jlM0cW_vbIe0osnyOHjLyzqo6_dBdXXLhIeattQfQWUftMlW1jaa1E6r6SF78VdPU2sNJcLuYWJ460d41qiC-mceqEZmIp3bPDcAU4gDlQcSTf_pk0dz_FntO3KtuDYI4J75A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقائی: دشمن واقعی مردم آمریکا مسئولین جنگ‌طلب خودشان هستند
🔹
سخنگوی وزارت خارجه: مسئولین آمریکایی برای ترساندن مردمشان، دشمنی خیالی در آسمان می‌سازند تا تهدید واقعی روی زمین را تحت‌الشعاع قرار دهند.
🔹
خطر واقعی نه پشت مرزهاست و نه در آسمان لس‌آنجلس و سن‌دیگو؛ خطر، هیات حاکمه‌ای است که جنگی غیرقانونی با پیامدهای جهانی بر دنیا تحمیل کرده است.
🔹
رئیس‌جمهور آمریکا حتی نابودی لس‌آنجلس و سن‌دیگو را «بهایی بسیار ناچیز» شمرده است. این، مصداق روشن «سیاست ترس» است: مردم را از تهدیدی موهوم بترسانی، نابودی شهرهایشان را بهایی قابل‌قبول نشان بدهی و کاری کنی که از توجه به خطر واقعی غافل شوند!
@Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/467573" target="_blank">📅 23:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467572">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
سازمان عملیات تجاری دریایی بریتانیا: چندین کشتی در نزدیکی شهر رأس‌الخیمه امارات، از طریق پخش رادیویی VHF، اخطار گرفتند که باید منطقه را ترک کنند.
@Farsna</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/467572" target="_blank">📅 23:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467571">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0MlxBof4qzwv0X7R8Vao25lcwNlpjajEShFZiSyPrk6s4TObBXeL8FQuR7t1_lTjfxrm8Rcun01wwik_UU7OtllnOsuFYvCiSc1ZenUomV27cK30Z8bxdoS0ozVmNf0KY_hEyxYD83lCBR8wP4nyUl6qvBgMU6iZf8X-UqEM9Cy7BHhYZUgAEC0wdNm1T_9qVvUznWPJrzBM1UolUs-SF57oln5yPk3YH-eOYfCoJ9ZIhfMOsdwlYEwW_AsrXbTiW7Zxm5vd8OfzsVOot6BSaxKQWik1A1iwJO_gdPAUaA59mQGePXU2DJni76yhSuBUSRWygA9hYb3DXLQBGI9zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس و خاطراتی از راننده شهید رهبر شهید انقلاب
🔹
شهید حاج عبّاس سعدآبادی از رزمندگان دوران دفاع مقدّس بود که از سال ۱۳۶۳ به تیم حفاظت آیت‌الله خامنه‌ای در دوران ریاست جمهوری پیوست و پس از مدّتی راننده‌ی ایشان شد و مسئولیّت واحد نقلیّه را نیز بر عهده گرفت.
🔹
او پس از سال‌ها خدمت صادقانه، در جریان بمباران مجدّد محدوده‌ی بیت رهبری، در یازدهم اسفندماه ۱۴۰۴ به شهادت رسید.
🔹
به روایت خانواده شهید: رهبر شهید انقلاب همواره تأکید داشتند که تردّد خودروهای حفاظتی نباید موجب آزار مردم شود و به حاج عبّاس فرموده بودند اگر قرار است به‌موقع به مقصد برسند، باید از قبل هماهنگی لازم انجام شده باشد تا نیازی به ایجاد مزاحمت برای مردم نباشد. این حسّاسیّت، در سفرهای استانی نیز دیده می‌شد.
🔹
روزی به مناسبتی رهبر شهید به حاج عبّاس فرموده بودند: «نوه فقط نوه‌ی پسری نیست و باید نسبت به نوه‌ی دختری و تربیت او هم حسّاسیّت داشته باشیم.» همین نگاه باعث شده بود حاج عبّاس نیز نسبت به خانواده، فرزندان، نوه‌ها و خانواده‌های شهدا حسّاس و مسئول باشد.
🔹
پس از سال‌ها خدمت، زمانی که حاج عبّاس تصمیم گرفت بازنشسته شود، در آخرین روز خدمتش نزد رهبر شهید رفت و گفت اگر اجازه بدهید، می‌خواهم بروم. رهبر شهید با تعجّب پرسیدند: «چرا این‌قدر زود؟» سپس به سردار جبّاری، فرمانده وقت سپاه حفاظت ولیّ‌امر، فرموده بودند: «عبّاس‌آقا را نگه دارید.»</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/467571" target="_blank">📅 23:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467570">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‌  یمن: سعودی از حجم و دقت موشک‌های شلیک‌شده از یمن غافلگیر شده است
🔹
یک مقام مسئول یمن: ناتوانی سامانه‌های پدافند عربستان، آن‌ها را مجبور به اعمال فشار بر نیروهای خود برای دستیابی به هرگونه پیشروی با صرف‌نظر از میزان تلفات کرده است.
🔹
تیپ ویژۀ موسوم به عمالقه…</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/467570" target="_blank">📅 22:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467569">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‌  یمن: مسئولیت افزایش تنش‌ها در باب‌المندب با عربستان است
🔹
وزارت خارجۀ یمن: تبدیل باب‌المندب و مناطق اطراف آن به صحنه عملیات نظامی از سوی عربستان، امنیت و ثبات این منطقه مهم برای جهان را به خطر می‌اندازد.
🔹
ادامه عملیات نظامی در باب‌المندب به تجارت جهانی…</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/467569" target="_blank">📅 22:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467568">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14c8dc96d2.mp4?token=VS0_bRptPtKKshjRvSwZj9HnqoNat2-NH9CknVeAcFEVBq04jV1AfUf1EBJqUEqx8xX3EReHSM2BS3DL50D1jhJDKE1e7zYe_Dpk0dQQPz30bhs6d-m98fEWgpO9alqeVOojH75cwj59YOe3reL4mahwPAd7NPMBhwBbEhyRtsbi7-avCe4Q8XRQM098AQfgeT5-BCMo7eJagC2iQ3sBqF6IezEvrOh0zPitKu4fAVJPrkIKNqIY0vMEdNF3K35TLZCXRZHXhz4bjh9qWYYV5U6PE6bk7B-8NX9Dm3v00AP4DyVMG7ShvbI0jWE8VsYxzR8kKvKAJNVR782ULAAvYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14c8dc96d2.mp4?token=VS0_bRptPtKKshjRvSwZj9HnqoNat2-NH9CknVeAcFEVBq04jV1AfUf1EBJqUEqx8xX3EReHSM2BS3DL50D1jhJDKE1e7zYe_Dpk0dQQPz30bhs6d-m98fEWgpO9alqeVOojH75cwj59YOe3reL4mahwPAd7NPMBhwBbEhyRtsbi7-avCe4Q8XRQM098AQfgeT5-BCMo7eJagC2iQ3sBqF6IezEvrOh0zPitKu4fAVJPrkIKNqIY0vMEdNF3K35TLZCXRZHXhz4bjh9qWYYV5U6PE6bk7B-8NX9Dm3v00AP4DyVMG7ShvbI0jWE8VsYxzR8kKvKAJNVR782ULAAvYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای راهبردی روابط خارجی: آقای روبیو، اگر خیام و خوازمی و ابن‌سینا نبودند شما هیچ چیز نداشتید  @Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/467568" target="_blank">📅 22:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467567">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4f965e96.mp4?token=H-wD9GqHUBXDrG1cdAKpwJC2V9NijEOy5feRWSbmYwJ5SdanSLQ_drxfiHGn2-I0XCWAQZibTFdpqKPGfoytKkISutJ-NnwVQCa8rsAlmuGuLW1NtNmFPBRMPar8ABB-z06mAydyNAJc4a72Jr6BBvyHuzv13Hx4BVuArv_sJqcCDyidXPnunsuHM0aSkMSmTf_mqRx7dXN9C1lzQxPeOZJ-1ak3B340_BOdcZbsyuoDrqyQRd2rkE806xtSN9O-LfyLXfOsVhWqaqqa5gC5Q3pDtU6azmKg7IS9BZqDo013-WND892I2XXWgmkLewbVhOiG5cJq1jpHhB19zJYwTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4f965e96.mp4?token=H-wD9GqHUBXDrG1cdAKpwJC2V9NijEOy5feRWSbmYwJ5SdanSLQ_drxfiHGn2-I0XCWAQZibTFdpqKPGfoytKkISutJ-NnwVQCa8rsAlmuGuLW1NtNmFPBRMPar8ABB-z06mAydyNAJc4a72Jr6BBvyHuzv13Hx4BVuArv_sJqcCDyidXPnunsuHM0aSkMSmTf_mqRx7dXN9C1lzQxPeOZJ-1ak3B340_BOdcZbsyuoDrqyQRd2rkE806xtSN9O-LfyLXfOsVhWqaqqa5gC5Q3pDtU6azmKg7IS9BZqDo013-WND892I2XXWgmkLewbVhOiG5cJq1jpHhB19zJYwTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای راهبردی روابط خارجی: روبیو ماجرا را ناقص بازگو کرده
🔹
حملۀ خشایارشاه در پاسخ به حملۀ یونانی‌ها بود که در آن آتنی‌ها سارد را به آتش کشیدند. @Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/467567" target="_blank">📅 22:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467566">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59ea887f9.mp4?token=X0vCx1UCQCAIGYJvn_58BnYsehRbvktw0hRVXVEVlqtqtbs4KjGMeGpZXJavRHFWwe_gxivPOsyd_CsqGVHWf-2QaOdcXBhsdTwaMSeVAx8C7sJZjqzfEEqQBkE_715EVvvl9t9-Rw0z7SF6YKrsnJFdXxTUZSNgMU3OFyXIfsRWPyfr5oYuS-WZ9_L9nGtmqtN-J_yv6Y7ISJSp5ZgP7DJrHhMTAbbhX3Ib-I7Ys37J-U9wGgCu76o7kTrsgdClMsyDiOrtAkrfj1Nwbor0kGOMhbfXt_kvrJwNY3jcNr7_HMFdUZR0GqjH-NBF8q07yszCxBBCZw1wGtI9LblGzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59ea887f9.mp4?token=X0vCx1UCQCAIGYJvn_58BnYsehRbvktw0hRVXVEVlqtqtbs4KjGMeGpZXJavRHFWwe_gxivPOsyd_CsqGVHWf-2QaOdcXBhsdTwaMSeVAx8C7sJZjqzfEEqQBkE_715EVvvl9t9-Rw0z7SF6YKrsnJFdXxTUZSNgMU3OFyXIfsRWPyfr5oYuS-WZ9_L9nGtmqtN-J_yv6Y7ISJSp5ZgP7DJrHhMTAbbhX3Ib-I7Ys37J-U9wGgCu76o7kTrsgdClMsyDiOrtAkrfj1Nwbor0kGOMhbfXt_kvrJwNY3jcNr7_HMFdUZR0GqjH-NBF8q07yszCxBBCZw1wGtI9LblGzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۵۰ هزار نفر در خیابان‌های لندن جنایات اسرائیل را محکوم کردند
🔹
مردم انگلیس امروز در حمایت از فلسطین در قلب لندن، با دست‌نوشته‌هایی مانند «نسل‌کشی را متوقف کنید» و «فلسطین آزاد» و همراه داشتن چفیه و پرچم فلسطین، به‌سوی پارلمان انگلیس راهپیمایی کردند. آن‌ها…</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/467566" target="_blank">📅 22:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467565">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd5954fef.mp4?token=dHXhTjFZZ3F-arN3Ohn1IuKYRzmTEdtSWqh0GDcF2MebfhhvH1fi97hkEcfPIG7GFe4Ln0djW3BMgDG4GzG8wuKiNEl-xdJtqbmmNyHqOMunKnwCP-2hTv7EYtepD4KczGDmnUi5qqIr1xL9KqePgqIA5X_VT2nFdDTYhD-H2x6u5K9BkZGV9CwuM-7Jox7yUIrQ53KVaGJZXPQvW_RntJEu39f3h9FGSerZ5QAh0zkdeJFq1zUR_zRCg4cckbAFsNqCirC3ic5IXTBhs9zaZjkAabdMHeGjs4y3LVQobSUFWkbWH9eAPF5nWQlo_1MCkuAqfd7T3XyCGJkWPyE3yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd5954fef.mp4?token=dHXhTjFZZ3F-arN3Ohn1IuKYRzmTEdtSWqh0GDcF2MebfhhvH1fi97hkEcfPIG7GFe4Ln0djW3BMgDG4GzG8wuKiNEl-xdJtqbmmNyHqOMunKnwCP-2hTv7EYtepD4KczGDmnUi5qqIr1xL9KqePgqIA5X_VT2nFdDTYhD-H2x6u5K9BkZGV9CwuM-7Jox7yUIrQ53KVaGJZXPQvW_RntJEu39f3h9FGSerZ5QAh0zkdeJFq1zUR_zRCg4cckbAFsNqCirC3ic5IXTBhs9zaZjkAabdMHeGjs4y3LVQobSUFWkbWH9eAPF5nWQlo_1MCkuAqfd7T3XyCGJkWPyE3yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشق ایستادگی سنندجی‌ها به شب ۲۲۴ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/467565" target="_blank">📅 22:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467564">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1642c84bf3.mp4?token=sDY98iA2KID6S2jm-ncaFjDD1eTjujFwBrggMMgBu-gshT9HZc6C-r5vwCxQDp2pvD_kT76fWvDjNMqnZvXP8JyfIqtWMZkRDXgQR-aQmuSQCt0mpLHrv-ItV1gt7PHMQkuwYyQCR2NJGwWLJyHWrr0qfR6Pk929_LsIA2yZJxX5RKEBwhGNT7i3R2Pp0PGvMuqHtBkBqLalIRMJaGC_QNabc28h3alVNNQJ8ChJU8v_RmJnw2zizkaESp02hK4sITq-p_l2HYKSse44M3DPudUPB2kBTyMie2f6E_3x2Iek6ZjvNzvhqmFgVr-zEL9LPi6CUjahEhEcL6siCfzKIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1642c84bf3.mp4?token=sDY98iA2KID6S2jm-ncaFjDD1eTjujFwBrggMMgBu-gshT9HZc6C-r5vwCxQDp2pvD_kT76fWvDjNMqnZvXP8JyfIqtWMZkRDXgQR-aQmuSQCt0mpLHrv-ItV1gt7PHMQkuwYyQCR2NJGwWLJyHWrr0qfR6Pk929_LsIA2yZJxX5RKEBwhGNT7i3R2Pp0PGvMuqHtBkBqLalIRMJaGC_QNabc28h3alVNNQJ8ChJU8v_RmJnw2zizkaESp02hK4sITq-p_l2HYKSse44M3DPudUPB2kBTyMie2f6E_3x2Iek6ZjvNzvhqmFgVr-zEL9LPi6CUjahEhEcL6siCfzKIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ شهادت مامور فراجا در حملهٔ تروریستی به یک گشت انتظامی در زاهدان
🔹
پلیس سیستان‌وبلوچستان: درپی حملهٔ تروریستی به گشت یگان تکاوری نصرت‌آباد، ستوان‌سوم‌ وحید عنایت به‌شهادت رسید.
🔹
عوامل این حمله شناسایی شده و یگان‌های انتظامی در منطقه درحال انجام عملیات…</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/467564" target="_blank">📅 22:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467563">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خنثی‌سازی مهمات عمل‌نکرده در کنارک
به مدت یک ماه
🔹
فرمانداری کنارک: عملیات خنثی‌سازی مهمات و بمب‌های عمل‌نکرده در محدودۀ‌ نظامی این شهرستان از فردا به مدت یک ماه انجام می شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/467563" target="_blank">📅 22:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467562">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/626160e949.mp4?token=KZ89dZR4DR2iFz3mHhIqnltMfGFiKyBun6s9SPd0Qi84xEX0LXs_R6sm_KDe5D4ubSGcBQSAZzt-IeVVI3Uib_jSu_HP4oqSkE7FRJ_H-yRDULRE1UD0gQgtRNdpHrWmNi_5eS-GhZQElxQ9-7b4gkU_L1a_EwONFOvZqK_mRZhBhJKxIBHcp-F6k97xXeFKpThzxYi4VsO6KPSwOmWkZPDMuzJaVMm4AnEbJBuUcEbcGC0PbU_JTKtK-nj5-mC9RQCl6dMv3nva0YRj_WpaPZYYKzQm_uQ3-x9GWl7UvQHMMrMlBLxdUdjICmgOwrNcUiWDBxkS74jWJ2OqqIDexw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/626160e949.mp4?token=KZ89dZR4DR2iFz3mHhIqnltMfGFiKyBun6s9SPd0Qi84xEX0LXs_R6sm_KDe5D4ubSGcBQSAZzt-IeVVI3Uib_jSu_HP4oqSkE7FRJ_H-yRDULRE1UD0gQgtRNdpHrWmNi_5eS-GhZQElxQ9-7b4gkU_L1a_EwONFOvZqK_mRZhBhJKxIBHcp-F6k97xXeFKpThzxYi4VsO6KPSwOmWkZPDMuzJaVMm4AnEbJBuUcEbcGC0PbU_JTKtK-nj5-mC9RQCl6dMv3nva0YRj_WpaPZYYKzQm_uQ3-x9GWl7UvQHMMrMlBLxdUdjICmgOwrNcUiWDBxkS74jWJ2OqqIDexw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینجا شهرکرد؛ صدای اقتدار ایران هرشب به‌گوش می‌رسد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/467562" target="_blank">📅 22:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467561">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca2f25046.mp4?token=EHFYS_2cusrht19UMsORSADy5Yd8xO7G8zo57FRHFuNShKDQdtw7MmlfxgU2gJ6HtSAmPQdKblAewBN4DCcsIrH5QU_bHPesnJ8kTsw9ue05LAhAZGT0f-Chdm-KPr1KQmkA41N8Uv67rUUT5fLFqdPtc7Fc5xlfbj0QcaJQPr-Zinb6s30YzpQDDBZdnDqi5dxYqbnuCvbwmgV9kNOIhcDxRnBtzYkHiNaBld99104YeeRHx_VC5rGz3bUis6ZVT8Buied_BNpArgg6moO2rnL8_r8T1ow_Wh6K7y0hb5MENhGJGY6b7zqobo5XAPV7k74MvbgoTRt8wj0QKk493A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca2f25046.mp4?token=EHFYS_2cusrht19UMsORSADy5Yd8xO7G8zo57FRHFuNShKDQdtw7MmlfxgU2gJ6HtSAmPQdKblAewBN4DCcsIrH5QU_bHPesnJ8kTsw9ue05LAhAZGT0f-Chdm-KPr1KQmkA41N8Uv67rUUT5fLFqdPtc7Fc5xlfbj0QcaJQPr-Zinb6s30YzpQDDBZdnDqi5dxYqbnuCvbwmgV9kNOIhcDxRnBtzYkHiNaBld99104YeeRHx_VC5rGz3bUis6ZVT8Buied_BNpArgg6moO2rnL8_r8T1ow_Wh6K7y0hb5MENhGJGY6b7zqobo5XAPV7k74MvbgoTRt8wj0QKk493A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای راهبردی روابط خارجی: آمریکا با ما مشکل تمدنی دارد
🔹
روبیو یران امروز را با هخامنشیان مقایسه کرده و این بازسازی موضوع «جنگ تمدن‌ها» است.
🔹
آمریکا فارغ از هر نظام سیاسی، با ایران قدرتمند مشکل دارد؛ البته نظام سیاسی می‌تواند ابعاد این جنگ تمدنی را…</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/467561" target="_blank">📅 22:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467560">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2RCWYwdZhVGjQHRju700fHXzMpZpgviysbznyrvzsprIVh3lMIxdaX9-K0mMj6md-t65GpsBxgtGAjU1A7rJ-taHygJk34l1FuFWX0fDlOPwO_JJP4P2ew0-BkFco4zLXpUQortCV9cAbDU4wQ_f-1hjPCwnByD-6wL56DCV-CQtBtlSJRrraSZtT3HCJeW7Sop7uXp8Ok2iHEeHuWz_-zcpm-Tjy7za90pgIHTVX-yQrmo4lIVR-rl8mH-ZZHRZs1Zbqmb5RSqBFlhQG5sZ0t05UpP-Ruskvg8r62JFXQyJuoWuu3QZCmHjYNOt6evOeb6hpxEwxAxMXLRczrz4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۵۰ هزار نفر در خیابان‌های لندن جنایات اسرائیل را محکوم کردند
🔹
مردم انگلیس امروز در حمایت از فلسطین در قلب لندن، با دست‌نوشته‌هایی مانند «نسل‌کشی را متوقف کنید» و «فلسطین آزاد» و همراه داشتن چفیه و پرچم فلسطین، به‌سوی پارلمان انگلیس راهپیمایی کردند. آن‌ها در طول این تظاهرات، ۲ دقیقه به احترام شهدای غزه سکوت کردند.
🔹
برگزارکنندگان این اجتماع می‌گویند: تا بعدازظهر شنبه ۲۵۰ هزار نفر در این راهپیمایی حضور داشتند. معترضان خواستار توقف ارسال سلاح به اسرائیل توسط دولت انگلیس بودند.
🔹
پلیس لندن اعلام کرد که ۲۰ نفر را در این تجمعات بازداشت کرده است. پلیس لندن در این باره گفت: «تا کنون چندین بازداشت انجام شده است، از جمله یک زن و یک مرد با پلاکاردهایی که حمایت از سازمان ممنوعه اقدام فلسطین را نشان می‌دادند.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/467560" target="_blank">📅 22:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467559">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b8e420b71.mp4?token=PNfDrhqhFjGnRXcvIPcWzhcMvmEZf_31U1iWXSNSHJappF4zwFERSrJAP9NkC2ySgxIgWSUuDAqisI9-3oieXcLHCHP8QCdFJSjFNiUVX9dFP2yyoSu3-hVFd3n0SYKJ5xo_qFw8TUkWDQMjoEBaQXB02G12fTNPd6x2DUTx54ruoiarLb9IGXoTs1gzgXVxFt9VMDPiIDYjV-FhScbiHkCE5wGwY9z2k6kkKxkavMfh9pkWLRaP5onr8pNs7XinlLE0RG-awdyasikHLujMAKLGwXgcWkGQiTNiz0W5mZ3QSJhkflWjgSegC4l6R-CKg_jPStgJi3OJJS6xpb_6rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b8e420b71.mp4?token=PNfDrhqhFjGnRXcvIPcWzhcMvmEZf_31U1iWXSNSHJappF4zwFERSrJAP9NkC2ySgxIgWSUuDAqisI9-3oieXcLHCHP8QCdFJSjFNiUVX9dFP2yyoSu3-hVFd3n0SYKJ5xo_qFw8TUkWDQMjoEBaQXB02G12fTNPd6x2DUTx54ruoiarLb9IGXoTs1gzgXVxFt9VMDPiIDYjV-FhScbiHkCE5wGwY9z2k6kkKxkavMfh9pkWLRaP5onr8pNs7XinlLE0RG-awdyasikHLujMAKLGwXgcWkGQiTNiz0W5mZ3QSJhkflWjgSegC4l6R-CKg_jPStgJi3OJJS6xpb_6rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای راهبردی روابط خارجی: آمریکا با ما مشکل تمدنی دارد
🔹
روبیو یران امروز را با هخامنشیان مقایسه کرده و این بازسازی موضوع «جنگ تمدن‌ها» است.
🔹
آمریکا فارغ از هر نظام سیاسی، با ایران قدرتمند مشکل دارد؛ البته نظام سیاسی می‌تواند ابعاد این جنگ تمدنی را تقویت یا تضعیف کند.
@Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/467559" target="_blank">📅 22:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467552">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p72t-kwqOwqpeTND-zTbDzROe0Vy49tnegQYjhCEmP0ale75Y9UhEiTtklStUeH2VKxJNcjjmZMa_HK6BVAfQAH_n_ZVVoyj2ylwQTzgfR1SkET1uOjvQNwJ-Xp_cUeadPlPfTPVWf7KCo6Y0uxojgJNGVimPmdMAKnEQbEbGpBmppPduqZtQDetoH0hWsgH6WwinvKUGndpnfBF0lFHqDATKqYUAjeiZkj0xN_V-0zepacQwJ1Q9QTb9a5OVT71YoFD6Ms5FT1zhFo9kCZRUactIpTM1UulThO7PjrZsd56U_0199CDyGr0M5fQ4UjOwT5-ufxs0mQkj6CmpY9rCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aPqD-quer7SD_2RgEJEjceJCP7jFC6XUeyCAMyR3diPraKTMSOFND4LzDKlV6K0p2Jmofz8m-4A_m4dwYMViexRrI4BB6wEHRkVL1PCSTI54AOfNjRqtwb_m6DszavPkmzEzRP33Q9cJVB95kvXy_lTQrIZkFakDJz-m5Q9s4QbkImveHMnitfatafb6FZCifWHaCNlERxqZs0w9CrC1VkcpfSyVOjSm2_CIspxg84sTVJV87LZtH3uGzyV-bI7d6H2SJu6GqquUkPZ0tsVlkRge3PAaiPnDZv0kvrSRww8jD-PhCy3NpZN73DScgx4kGLasVCYpQcTCyQ2gXMobPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mirERfFxAXKA9Oeb7taANSO4zBxupuunqDbJ1Vj2uPBYZybB7BzCALLMF8XlNvsgMuihFiv51a3s5nkWpcpGvoMWELObLzUYA_HOazjfO4lkLZrOuimXM9DQIlix-9osqKr9_fLhwujTqjDanybDyNYl50lFecMsSCCFAKNjC0q3QWtSpu-6vwXfl4zdutBqXUbD2VEDEsfIHgTeAk3V2T9sPg5Y6uBTl0VI3L1-JYNqM7K_7AZE3BGS7DXQSOFtG_1qh2A33Gg83O82MJPY_0TiohvF4ZW9kowuFjBLsRcDr9DPaRx8Gru4KgjL6KGapnCoPFiKqmEkpwbOxEqbYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aEYIoIKR2nkrwjQwiDzyylVCEVYtjen4GNyr0k3CWD56CCwZz9gFEdn2nEJeDopH2sovHeX9MIhakxhRGS9P4NFkoI3V8lR3o54jnFUXBYkBShiKa5ZOCTzt6WV912eX8wQDFESxrGCdDXshf1yH1FlGkBeiCpsZHdCRj-SlRy496xgCeA94SMP_F6nrRSo-rQTlSieUMbSaqV1lgIk9jXzoRivQ8Ys4z8l-TCzU-IeTVFR5gUXrRffyaHZ6Ug6KKloTKkBoNLN0qO5ySr7tsNwaNLpdheUgcS5etl3cAxWb8Ealc9V5fAKDhYt4cJC_wO9rnP2kDxFogWedtU4TdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EmCQdif51RWDBiDCEta3FWmE2TTUXbDtWzqZd7HabxjtYTQNb25tq5z-8bH6c4NHYbckq3U9547lLwgUUKRhVDWgkf1pBqAyF2JlD0QgnMKMczSuBJSOlg3DsDjDDTjHXSRNQmlT7gtjoUg24nLl2VJ7hsDzsKmrr_dKPPm8tLJeqBAw2fY12NvOovQA_LjBylCJveAt21xfcQEZxPR00GTz6VSvmqFJvCgSUfiRBnpdO15NUelGr4vnMceQSw4Ea_XRflHj0Foqs--nnsBL7N-nhmX5aU-14gel4BvS_tNDqZQCfIcFokoYEG8LExN5_BcUiAfbmrpbXGXIw2DUlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b_5_XJ8RJNWGPsmhWqtFrPx73mVYiWAo7qmxsPMPt-3RCyNJ2fB3bSvsfkjNvkG0PyKSnGKNXDZUVhix9d0-tSe9kIklFnGwstVOExHAsPFBJIvQsp70NJM8qaT8fZiRDwfxReC8d7moayp4sMy1EU4pUfNyOp-dKnwDSok_DX2nfksNLMnIOVHXPwT78q7_AFMWcd6hX7FrOKFhw1Ob7TAPDRURu08kDsfg_hUT8KCXowN50RNjXloLq873XdCpvHWgDfgpGAhikkrh5-EOp2x0X4m8WPH5pWupn0w6ujCeiFSFiG-1Yr06Pva1r-IxQeMgIQK_4GmqGFl8XwM1lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uIyUI8Km1H7j695JY1h86aixks5bC3FKELySLWX7lOxOwBU57Y41TYy49pLvtuubu2ork1RKb5LxaiH40KxD8yseFq08Tjw6CPa7z1_LBsCwlscP_fMiGAqQNDrEn3--pOilIf9St1zeh-m1GASuK97oLhx9uWHzIYecDKoMx4IlanTAXuGigu7_ufgnivfRCflGFAKUu-0zPnnGVw1SNqLcN40Xau75C9-exal_B_6LpheC1Gx0SS7KAlXxhBWFe0f4NfLLJZUFckPfZWQ6fVWc_IJ3vq4gAhP6u56NAX0ok0g9BdeFwg8eSK-QiO32xpKtu9HU1caq35LSoaiz4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تجمع دانشجویان مقابل سفارت فرانسه در اعتراض به سرکوب دانش‌آموزان فرانسوی
🔹
دانشجویان در اقدامی نمادین برای اعتراض به برخورد پلیس فرانسه با دانش‌آموزان میز و نیمکت‌های مدرسه را در مقابل سفارت این کشور قرار دادند. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/467552" target="_blank">📅 22:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467551">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d89780a171.mp4?token=CoZF1LSZvt8tePEvUPVKp7-Iict4SyBd5UZCRUppbOUkJvnEwAfiaXC-zfD3_8WmyIeFSOs0OpSlDTxwJO1BffW8EnAkckpgy2e5jMQ8qx7KJ03YXjktJ7O9qOJ781AzsLnsW8YQ0z9nc9PbkwdG4GNnmATc_y2fVctwteclhlslMDBYdwVUN4RP-4s2sampFjyPI25z1IBmTYJb6Cmg4UtQr2zbTTyuUI2JRxlK6qLeqPGUO7lKtRD539LfXFHV5aDeYFeUNTCsAz0zmWpldVUTjAKl95SzEJesvvK8tblR3gwM2dX8Fja6oQHF0kNyRLhOQhRqjtYxonzrVzLyKHSbLMUsiXKb_73cQOn6_QOvxf_RCuZa1i-OGHeu3qJguFxaxNR6jhdOSFH599Qv-V2qOvtD3xvG6K9HBqFT7Aox7Fe_ApBxXICsgR1g-GPtfJT8ekQNWg8dR0FE04iMRVyF3U1GBz31xYu3yIziTNki3ArjW1-nTI94bx71hKyeLP_pY09NWSlFeNXeiShmTGWMBcb4REYsbnN1psphXaZKHEtm7NHm9obnkozSmYEQaH3J2yPf-0EcC7snu7AovkCYf-oGtjBXCn5YaL9nmXiWPHNgHbIwJdLz608UWphvNDt-9sCprp52a5wgwLMw0sYjiE_oRZmAmonpXTlmzjU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d89780a171.mp4?token=CoZF1LSZvt8tePEvUPVKp7-Iict4SyBd5UZCRUppbOUkJvnEwAfiaXC-zfD3_8WmyIeFSOs0OpSlDTxwJO1BffW8EnAkckpgy2e5jMQ8qx7KJ03YXjktJ7O9qOJ781AzsLnsW8YQ0z9nc9PbkwdG4GNnmATc_y2fVctwteclhlslMDBYdwVUN4RP-4s2sampFjyPI25z1IBmTYJb6Cmg4UtQr2zbTTyuUI2JRxlK6qLeqPGUO7lKtRD539LfXFHV5aDeYFeUNTCsAz0zmWpldVUTjAKl95SzEJesvvK8tblR3gwM2dX8Fja6oQHF0kNyRLhOQhRqjtYxonzrVzLyKHSbLMUsiXKb_73cQOn6_QOvxf_RCuZa1i-OGHeu3qJguFxaxNR6jhdOSFH599Qv-V2qOvtD3xvG6K9HBqFT7Aox7Fe_ApBxXICsgR1g-GPtfJT8ekQNWg8dR0FE04iMRVyF3U1GBz31xYu3yIziTNki3ArjW1-nTI94bx71hKyeLP_pY09NWSlFeNXeiShmTGWMBcb4REYsbnN1psphXaZKHEtm7NHm9obnkozSmYEQaH3J2yPf-0EcC7snu7AovkCYf-oGtjBXCn5YaL9nmXiWPHNgHbIwJdLz608UWphvNDt-9sCprp52a5wgwLMw0sYjiE_oRZmAmonpXTlmzjU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج خون‌خواهی در کرمان از خروش نمی‌افتد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/467551" target="_blank">📅 22:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467550">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i61H61YhdohbPNPAWHLg9oIAygVj14ECWJOdBHzWIACbg7wrh6G7MIU7UCYMnyTdWiYxzwvPOK61_luJCaIIaQbFn8nqDKaMiovto9Q_93XXWR9sbbsnnHONZAbzGIPd-E15nAuY6t-7_vFglQAWke6pCttkV8bJjLE3LWSJgxp9DVCSrN7Ow4xn6yzzQvxiMqJIapgRAX6ee_eTPw0jzcpOQlMXx3Jpt1s8YomCVzkNQbfTEyZoLuGnDZB6Z1HjFKQddI6H6EPR6kSEcwHYEhIvGzK3banViWBTAT24mPNGumyvMIDoPyIaMSBcmEJuiXAkffJD82bMOhoCb2cj9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فجر ۴۵ و آزمون دشوار سازمان سینمایی
🔹
درحالی‌که چهل‌وپنجمین جشنواره فیلم فجر به دورۀ جدید نزدیک می‌شود، ابهام در معرفی دبیر، نگرانی‌ها از تکرار تأخیرها و ضعف‌های مدیریتی دوره‌های گذشته را افزایش داده است. سکوت رائد فریدزاده، رئیس سازمان سینمایی، درباره انتخاب دبیر نیز بر این ابهام افزوده است.
گزینه‌های دبیری جشنواره چه کسانی هستند؟
منوچهر شاهسواری؛ بازگشت به تجربه‌های اخیر
🔸
عملکرد شاهسواری در دو دوره اخیر با انتقادهایی دربارۀ کیفیت آثار، حذف هیئت انتخاب در دورۀ گذشته، ضعف فضای رسانه‌ای و محقق‌نشدن وعدۀ راه‌اندازی دبیرخانه دائمی همراه بوده است.
سیدمهدی طباطبایی‌نژاد؛ تکرار حواشی گذشته
🔸
دبیری او در دوره سی‌ونهم، با حذف هیئت انتخاب و انتقادهایی درباره کاهش شور جشنواره همراه بود. عملکردش در معاونت نظارت و ارزشیابی نیز با انتقادهایی درباره بی‌ثباتی سیاست‌گذاری و افزایش حواشی روبه‌رو شده است.
بهروز شعیبی؛ گزینه‌ای درحال آزمون
🔸
شعیبی نیز از گزینه‌های احتمالی دبیری است؛ سابقه مدیریتی او در جشنواره فیلم کوتاه تهران می‌تواند معیاری برای ارزیابی توان اجرایی‌اش باشد.
🔹
فجر ۴۵ بیش از انتخاب یک نام، به برنامه‌ای روشن نیاز دارد. تصمیم‌گیری به‌موقع، پرهیز از تکرار اشتباهات گذشته و تقویت ساختار اجرایی جشنواره، مهم‌ترین آزمون پیش‌روی سازمان سینمایی است.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/467550" target="_blank">📅 22:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467549">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🎥
شب ۲۲۴؛ سنگر خیابان همچنان در مشت کاشمری‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/467549" target="_blank">📅 21:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467548">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سودهای جاماندۀ سهام عدالت واریز شد
🔹
مدیر نظارت سازمان بورس: چهارشنبۀ هفته گذشته سود سهام عدالت ۱.۵ میلیون نفر که به‌دلیل نقص مدارک و عدم ثبت شماره حساب از واریزی‌ها جا مانده بودند، واریز شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/467548" target="_blank">📅 21:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467547">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jlbe-_oBvpKm7obr_uH1qiqS8o7ESj0Uymnu9wnaamdUOvROURIZNibN9K7fayX9uAZMOblCHwBReF9lbyNb12Ox3UPjLaTAUQhg45nPx1OfKzsQeTlyk5x8fq5KrFSLD4eQ5kmdamgbn9JpRNWBbVB0TIt--_T9Gkf0IGR76WKHjMIyD0WDq_fXbevnk8SXJkIc1q1uqJVVLSg3zPzQlOOnSq8I9cip3qzymfxwQdDnuvu9avCsSCvrMliDPQVrqS01tOpVcfLUGgVfoIinJ_Vu4m8IbRFSCnJLDOu8Iw0ZNZPAz4hy6byCzebcGo6QDyPlXzIc70B79RHlDNzzkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزاشگر ویژۀ سازمان ملل: اسرائیل معادل ۶ بمب هسته‌ای علیه غزه استفاده کرده است
🔹
فرانچسکا آلبانیز گزارشگر ویژه سازمان ملل در امور وضعیت حقوق بشر در سرزمین‌های فلسطینی، شرایط انسانی در نوار غزه را «بسیار فاجعه‌بار» توصیف کرد.
🔹
آلبانیز تأکید کرد که فلسطینیان تحت محاصره‌ در بحبوبه تداوم بمباران‌ها و ویرانی‌ها، گسترش بیماری‌ها، سوءتغذیه و نبود سرپناه امن با مرگی تدریجی روبه‌رو هستند.
🔹
وی به مناسبت گذشت ۳ سال از جنگ نسل‌کشی علیه نوار غزه گفت که قدرت بمب‌هایی که در حمله به غزه استفاده شده‌اند، معادل ۶ بمب هسته‌ای است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/467547" target="_blank">📅 21:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467546">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEsi_Tq-sppXCDmROq18zmV9Qp6WHjqikMpTdfX_5TsYvOlaHwGyuh-0SNIH-qIWCAWgt2fOLhQz_owmORcfxNwh4m9GmbpX36vmKpxVKgxdFx-6qubPPaHVWr_utBmeYr9YRBJuzs9Dk2Dk3sMBFzH2vh97Uycmi-B_Ffs0bEA-FwCrTnwS-uZcuYNdWP80l5WRTpZR8-MXQnnIRiw8vUt2rylYt53UWiem5gzsXhl0cuTw1pXvpZzLewQXUKecaurqX2n0q5JEcF1tu04R0KdZ3rkKbXY4gzya8OomLcd05J_VBUTiPP0XazjYk_u69UKRMikOwDbX5XECvRG5Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسیج فرهنگیان در نامه به پزشکیان: بی‌توجهی به معیشت معلمان باید پایان یابد
🔹
سازمان بسیج فرهنگیان کشور: در سال‌های گذشته، نظام‌های متفاوت پرداخت در دستگاه‌های دولتی شکل‌گرفته و کارکنان از درآمدهای عادلانه‌ای برخوردار نیستند.
🔹
برخی از دستگاه‌ها از جمله آموزش‌وپرورش در چارچوب قانون مدیریت خدمات کشوری قرار دارند، درحالی‌که تعداد قابل‌توجهی از دستگاه‌ها از قوانین خاص برخوردارند و این باعث شکاف در میزان دریافتی کارکنان شده است.
🔹
آموزش‌وپرورش از معدود دستگاه‌های دولتی است که دریافتی کارکنان آن از میزان ثبت‌شده در حکم کارگزینی هم کمتر است.
🔹
بی‌توجهی به معیشت معلم، می‌تواند هزینه‌هایی برای نظام آموزشی و کشور ایجاد کند که بسیار فراتر از هزینه‌های اصلاح حقوق و رفاه معلمان باشد.
🔹
مناعت معلمان نباید بهانه‌ای برای بی‌توجهی به معیشت ایشان باشد؛ امیدواریم دولت برای تکریم و بهبود معیشت معلمان برنامه‌ای روشن، زمان‌بندی‌شده و قابل‌اجرا ارائه نماید.
عکس: محسن ونائی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/467546" target="_blank">📅 21:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467545">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6tiQktuGv_aeFnhYp-2Ef9jnX1eQIKyCgSCjKhpv6UgL0Ea6HsEl5gxDMXxATJIZTl5W_-ShGfIfm3Vbp3XsXMhuyQMiI4TKY6RV_LVW6yJpzDgrYcHBvll9-rOWk17vBD59D0JGoTbF3uTW_Mxt2bYaPZ62WJhiPyFU5P-bEHbmvZqCmSD8nMq1Lf653roMpD3mW9sr521DY7h_rQQAerBvrYf7l7VwQ3ZIRiTfNe6hIf9whSWIeuWs8UeetIQ8jnK8_ruGXmF1ZYgTK3dnw35eWkArj0eSHhznQba9M585ijN2kZM0IfXJqmocPvp89xjT_hNA_EsX4HALAXvag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توسعۀ میدان نفتی سهراب کنار سفرۀ پرندگان مهاجر در هورالعظیم
🔹
هم‌زمان با فصل آمدن پرندگان مهاجر به تالاب هورالعظیم، خشکسالی، تأمین‌نشدن کامل حقابه و صدور مجوز توسعه میدان نفتی سهراب، آینده این زیستگاه را با نگرانی‌های جدی روبه‌رو کرده است.
🔹
در سال‌های اخیر، آمارها حاکی از کاهش پرندگان مهاجر به هورالعظیم است. براساس سرشماری‌های زمستانه در سال ۱۴۰۴، ۷۱ هزار پرنده در این تالاب شمارش شده، در حالی که در سال ۱۴۰۳، آمار پرندگان مهاجر ۸۸ هزار عدد شمارش شده بود.
🔹
تازه‌ترین مناقشه دربارۀ آیندۀ هورالعظیم، طرح توسعه میدان نفتی سهراب است که سال ۱۴۰۲، طرح توسعۀ آن به دلیل خشک‌شدن بخش‌های قابل‌توجهی از تالاب، رد شده بود اما مرداد امسال، شرکت مهندسی و توسعه نفت اعلام کرد که مجوز این میدان با لحاظ ملاحظات هیدرولوژیک و اکولوژیک صادر شده است.
🔹
عضو هیات علمی دانشکدۀ محیط زیست دانشگاه شهید چمران اهواز اما می‌گوید: در وضعیت کنونی تالاب هورالعظیم، برداشت نفت مساوی با از دست دادن زندگی تالاب است؛ با این حال، از نگاه من این دو، جمع‌شدنی هستند اما بی‌مبالاتی ما نمی‌گذارد هر دو مسیر ادامه یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/467545" target="_blank">📅 21:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467544">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌  هشدار آمریکا به اتباعش: به فرودگاه ریاض نزدیک نشوید
🔹
نمایندگی آمریکا در عربستان به شهروندان این کشور هشدار داد از فرودگاه ملک خالد در ریاض دوری کنند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/467544" target="_blank">📅 21:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467543">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/349dca9d7a.mp4?token=F42wsbRiwinJ005SFpl8WYjHIvOEkmfFj1bVdrLTMrz4JeorKNoFd8pv4_ps_BeaEf0vUNhr9uy8XKueXlu60E-7G_R4RftYk-EG7rV_FM6JDNMB3ivDK3n0Xs7HeF4UL94Xxxi5nBlX5mZ83ssgwX-yFF-Ix6_jWNVVMbsG_wofIKPKxu4mtaaQOc2mT9lgiZCvGdGhWE7dodsEc1IJcHO2bzTuYnXXLK-PmuWbmPq27snkWChGH8Ckfr4pagjb2axvPd48GQT9B3ZdZbl9G3EMXrs-yHZNlSCdDtP7LhXdcXfb2MGlU5xEg0sA8KfR2cyMJwyHxh6O9v3qJwKopQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/349dca9d7a.mp4?token=F42wsbRiwinJ005SFpl8WYjHIvOEkmfFj1bVdrLTMrz4JeorKNoFd8pv4_ps_BeaEf0vUNhr9uy8XKueXlu60E-7G_R4RftYk-EG7rV_FM6JDNMB3ivDK3n0Xs7HeF4UL94Xxxi5nBlX5mZ83ssgwX-yFF-Ix6_jWNVVMbsG_wofIKPKxu4mtaaQOc2mT9lgiZCvGdGhWE7dodsEc1IJcHO2bzTuYnXXLK-PmuWbmPq27snkWChGH8Ckfr4pagjb2axvPd48GQT9B3ZdZbl9G3EMXrs-yHZNlSCdDtP7LhXdcXfb2MGlU5xEg0sA8KfR2cyMJwyHxh6O9v3qJwKopQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامد کاشانی و محمدحسین پویانفر هم به «گردان‌های جانفدا» پیوستند
🔹
هم‌زمان با آغاز ثبت‌نام گردان هیئت‌های «جانفدا»، حامد کاشانی و محمدحسین پویانفر در هیئت ریحانةالنبی(س) برای شرکت در دوره‌های آموزشی نام‌نویسی کردند.
🔗
برای ثبت‌نام
اینجا
را لمس کنید
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/467543" target="_blank">📅 21:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467542">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🎥
تسلیم دسته‌جمعی مزدوران سعودی مقابل نیروهای یمنی
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/467542" target="_blank">📅 21:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467540">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b78b355366.mp4?token=A3QUPSR0fZccB0JUp_92leuGqFGl3-bH9IIpYU6ypUBJuqpRW_CBWN4Nbh6DTmDhWDc4mAc8YI1e-U6PyPqg5FRKL5Vnj9EhkzMPktZ5I2HNFxCuBGx9hcMX94dGXPajftPqC5adPowCI9vMI-kiiiVsWJsUiIMwmRhmnOV9UIGAj5mrfFC3vx6wV2uaSqIGT2IcRt0hRVjM_QOTJXxTT_KC0Vy5zIU1TKxbucIfSLfWfEDxkFUz2vPZkVQNr1yC8frWkDYV0GBCZRV5zMfrBVtqab4ko4AsTmzmrGA7f1CGkaw3VFGsykaGyJ0JL3P65Hyk0IWzs8oL5iNtiidlSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b78b355366.mp4?token=A3QUPSR0fZccB0JUp_92leuGqFGl3-bH9IIpYU6ypUBJuqpRW_CBWN4Nbh6DTmDhWDc4mAc8YI1e-U6PyPqg5FRKL5Vnj9EhkzMPktZ5I2HNFxCuBGx9hcMX94dGXPajftPqC5adPowCI9vMI-kiiiVsWJsUiIMwmRhmnOV9UIGAj5mrfFC3vx6wV2uaSqIGT2IcRt0hRVjM_QOTJXxTT_KC0Vy5zIU1TKxbucIfSLfWfEDxkFUz2vPZkVQNr1yC8frWkDYV0GBCZRV5zMfrBVtqab4ko4AsTmzmrGA7f1CGkaw3VFGsykaGyJ0JL3P65Hyk0IWzs8oL5iNtiidlSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: فکر می‌کنم وقت آن رسیده که اوکراین یک رئیس‌جمهور جدید داشته باشد
🔹
پیشنهاد می‌کنم که آن‌ها یک رهبر جدید روی کار بیاورند که بتواند توافق کند. زلنسکی می‌توانست توافق‌های زیادی انجام دهد، اما به دلایلی هرگز این کار را نمی‌کند. @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/467540" target="_blank">📅 20:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467539">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d3d04c904.mp4?token=aUKuw_mPksaR2TnFCs1xBe-Sn5nzh3eFEzY158xDyBssa4-CMAd6mDqsWs-Wko2P28SGM98CXREbGZg0HlbhKoJwHamcVssU1_jMytW_gjp41vNEUWSWgotqZZl05pjLm1pPHk2mEyboqA1Q8u_XcrrKYnYijwNWVddCN5E0D2uCz3c-Jeq-X0tM3zQ0vQ4cM8fqBENZg5_XcKaVX_4cF7U21hve2o16ci01I0JKFj3gMFMyt36qL5j4j0Xu-hi5L2cAFBr9qO-Tu90aRM58-iRbHcZxVPEqvTswkUMmqkkrC7AcJ6TbEOFkyyBH0B9QwqkIvrmWEOedawMpHnBmig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d3d04c904.mp4?token=aUKuw_mPksaR2TnFCs1xBe-Sn5nzh3eFEzY158xDyBssa4-CMAd6mDqsWs-Wko2P28SGM98CXREbGZg0HlbhKoJwHamcVssU1_jMytW_gjp41vNEUWSWgotqZZl05pjLm1pPHk2mEyboqA1Q8u_XcrrKYnYijwNWVddCN5E0D2uCz3c-Jeq-X0tM3zQ0vQ4cM8fqBENZg5_XcKaVX_4cF7U21hve2o16ci01I0JKFj3gMFMyt36qL5j4j0Xu-hi5L2cAFBr9qO-Tu90aRM58-iRbHcZxVPEqvTswkUMmqkkrC7AcJ6TbEOFkyyBH0B9QwqkIvrmWEOedawMpHnBmig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ما به زلنسکی گفتیم هرکاری می‌خواهی با روسیه بکن، اما به پالایشگاه‌هایش ضربه نزن اما او دقیقا همین کار را کرد
🔹
ما یک مشکل جهانی داریم و این مشکل ناشی از کمبود پالایشگاه‌های سوخت دیزل است. پس او چه می‌کند؟ می‌رود و به پالایشگاه‌ها حمله می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/467539" target="_blank">📅 20:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467538">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afb0987db5.mp4?token=i1AKzhkx3eTejmmo1TNxamAV4moe0Il0VKQKeM5MeUeS9hWK-AtN1KCooJB_6ipJX94MiAjG0MU67dBbA2IWp5mlw8CPH8lheIOiTujY7NV2_2iTjHhX3p2zlL5u4QpR9HzOh_Cf6-O-uWZGzQmijVwDy-l3NW34qXUyOIXMo54496rvmxwJFJ8-IpqV66hoX0hSUvPaLv1FF8a1IBCdjtCWxyQv_m7eJyM4juMigHqUeoJloUyIq3RYsXL8LjYUvuy-Mf9D_MScGKuvrpQw3Qmx-wdaN7FfSoNaJ9E5Z_V86ntW3eVs1OuyBGemfgd09NkVDTsMZ_0eYtBU8kIOGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afb0987db5.mp4?token=i1AKzhkx3eTejmmo1TNxamAV4moe0Il0VKQKeM5MeUeS9hWK-AtN1KCooJB_6ipJX94MiAjG0MU67dBbA2IWp5mlw8CPH8lheIOiTujY7NV2_2iTjHhX3p2zlL5u4QpR9HzOh_Cf6-O-uWZGzQmijVwDy-l3NW34qXUyOIXMo54496rvmxwJFJ8-IpqV66hoX0hSUvPaLv1FF8a1IBCdjtCWxyQv_m7eJyM4juMigHqUeoJloUyIq3RYsXL8LjYUvuy-Mf9D_MScGKuvrpQw3Qmx-wdaN7FfSoNaJ9E5Z_V86ntW3eVs1OuyBGemfgd09NkVDTsMZ_0eYtBU8kIOGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه: سوپرنفتکش متخلف در یک آتش عظیم درحال سوختن است
🔹
یک سوپرنفتکش حامل نفت خام که قصد داشت از مسیر غیرمجاز از تنگه هرمز خارج شود، پس از ورود به مسیر پرخطر اعلام‌شده و برخورد با «مین دریایی»، دچار انفجار شدید شده است.
🔹
این نفتکش با خاموش‌کردن…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/467538" target="_blank">📅 20:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467537">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUI-uuW9z0yEdaclzqZiQCGejW9wI1kkpNyF3RxIBVehPWYL3cx4ixmyCELCpPbp_usWEZ0stWn0uZPwk3Znldwj08hr6rKSlWT03xleqE0YtxV450DFNzop9il8KIwDDKAT0nLk1SWd2u7IkExn9O0YUxATc9C5yfQVm_Iaaw2ma65rJOE6e9WmsfwbetSZo4Auj9ki8-PGPCyk8Bn18aryta49lMH4ryudYFQVPQ6vDl7RHNTOIypKdQF8yRL6DbWW8tqtP7799JJ1WvNa1h4uuzwFnhmJVdjVghRtMgTMWQ3QHJXd3IbC-wQqWvQF40aa_usFB0bCTFuJbIBbOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه: سوپرنفتکش متخلف در یک آتش عظیم درحال سوختن است
🔹
یک سوپرنفتکش حامل نفت خام که قصد داشت از مسیر غیرمجاز از تنگه هرمز خارج شود، پس از ورود به مسیر پرخطر اعلام‌شده و برخورد با «مین دریایی»، دچار انفجار شدید شده است.
🔹
این نفتکش با خاموش‌کردن سامانه‌های ناوبری و موقعیت‌یاب خود حرکت می‌کرده و اکنون در آتش می‌سوزد. آتش از ساحل نیز قابل مشاهده است.
🔸
نیروی دریایی سپاه اعلام می کند: آتش‌سوزی مهیب، عاقبت نفتکش‌هایی است که امنیت و قوانین تنگه هرمز را نادیده بگیرند.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/467537" target="_blank">📅 20:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467536">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a87d623f5.mp4?token=i3RO46hgmnz507hvdrnQcHFriP6ucGuuktBEFVjWxuQ1YUvFkwjPjJYW7tRm6YIrCxbDjt6KIgTHfUAArrxwn-LHq96fdT4obwffjMXL73I-RVlEZGMQcwcFpioC5wSGSv7V7lvMmKaHplyqoU7Dl8ZWVUEdEUb4QNOeIvTVIgedHzWuobgDQGxRCGDRAgVMGgkcX678XuTGoL1IyFV2oRzMl0OqH6AAUv27Msr01SRqp94NFLOUZdvBxDL9_isk4QrwauQcM-unWXYJsTdc4AM1PLmjooTdeGAWZUrzJflsA6jqewD4rZjEVFCkGr6uIFqrWw8XBEzG0XhgGIO6aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a87d623f5.mp4?token=i3RO46hgmnz507hvdrnQcHFriP6ucGuuktBEFVjWxuQ1YUvFkwjPjJYW7tRm6YIrCxbDjt6KIgTHfUAArrxwn-LHq96fdT4obwffjMXL73I-RVlEZGMQcwcFpioC5wSGSv7V7lvMmKaHplyqoU7Dl8ZWVUEdEUb4QNOeIvTVIgedHzWuobgDQGxRCGDRAgVMGgkcX678XuTGoL1IyFV2oRzMl0OqH6AAUv27Msr01SRqp94NFLOUZdvBxDL9_isk4QrwauQcM-unWXYJsTdc4AM1PLmjooTdeGAWZUrzJflsA6jqewD4rZjEVFCkGr6uIFqrWw8XBEzG0XhgGIO6aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمریکا اوکراین را به قطع دسترسی اطلاعاتی تهدید کرد
🔹
فاییننشال‌تایمز: فرستادگان ترامپ به مقام‌های اوکراینی هشدار دادند که ادامه حملات کی‌یف به پالایشگاه‌های نفت روسیه ممکن است به قطع همکاری اطلاعاتی واشنگتن با اوکراین منجر شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/467536" target="_blank">📅 20:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467535">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3DCcXX2rlKnWclfMk_lVpUPBb5Umzbs5sd8drTLaKg3fj0GrMWROmPzdGj1X67Ze9SRgf1dIdoIpFt8RNy6oT4U13UR_YkVu09cX9zE39xjVSzCh4PjAB6hsjUqNj15qs_MKubJn8fbTt2OV_sIaoXeaRBZZQeJ6plmZvovY7d-s-sm_hqzxZrj2EAGqUc99Og5Q_ULCyPyZ3Bg6wcdMnS7maTeYCT3Xq-fmNxjiuHC2rP-yeEQxHI6CDdh9Gq0SFpyvYbXpmTmiswYKXmACimkK4yDF0Zg188L5qb4DNcHsWwMhYaPLY1iCdxnfnvqOJ-nc5Czg1_bI370KMQeWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رهبر انصارالله: قطری‌ها نباید تصور کنند که سعودی به آن‌ها وفادار خواهد بود
🔹
قطر باید به یاد داشته باشد که رژیم سعودی چگونه بدون دلیل به این کشور خیانت کرد و آن را محاصره کرد.  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/467535" target="_blank">📅 20:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467533">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_MJZ_JPA13PtS0G9UVyvb8wZGF028upJ-9-eeFBYCwiKnakUDOilC4HiY7WlDiT0MmFqgRKx4Q3lLdGe0B5M6tQwxrL9G7drS1sbK6x3R7kHMpXJeNfd_eVIRCxV5hl1arTErpURAFEruyFxQIOkSOAoyNvQtxelVqALfwJ-nO_b7abAu0qWana2o_e35RmvQFReejm-diD2OjEqsz01v75IQa_W0xA1Ua4oaIH03Bn6tqt_UpP-Lk6mTA1CwtA_O19RAEPVPhzWKPP-96vO7zdY-dib-cC0x8REBcVI1K8mLtpF7QGso0DYPJ7n22WloG5du9Cy_hH9nlPUU_law.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریدور عمانی تنگۀ هرمز تخلیه شد
🔹
تصاویر ماهواره‌ای از تخلیۀ کامل بخش عمانی تنگۀ هرمز خبر می‌دهد.
🔹
ایران در ۲ هفته اخیر، بیش از ۲۰ نفتکش متخلف را هدف قرار داده یا با هشدار از عبور منصرف کرده است.
🔹
هم‌زمان با بسته‌شدن تنگه هرمز قیمت نفت آتی برنت از ۱۰۴ دلار فراتر رفته و نرخ نفت واقعی بین ۱۳۰ تا ۱۵۰ دلار به‌ازای هر بشکه معامله می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/467533" target="_blank">📅 20:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467526">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N2D3EV5Z1S3Koilax6aj99i7xfOvNCzIOg9Xnpc8gBSdnKxSQ4qKx4mwO1G4xlV-WB_C4XCKCkXjmms-v5ToTKa7vYxDJiosTxdIV1NgU2pvzxS8i7gFy-Roup3Ql7k-PVPzhwCNLBX7_QwMtSiNdVcSzVKDzHowA25K8MtFpzk89rAuRqBAGr6D5QjyyeQoBFCa82kf2P1Lj4MnKayDwJkt3uKIupnExNg_7fP4nV-spkGKJsRQ3KXXnhEN81s5O1K9sbhCUz0g2auzaifIR5X2P9_676OTVxDTsyIM4dCa5gz-ITVWk0_yg4hg8LDQ8u5vQi_y7eu4DxtNmwQGNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JtUVMD77kEUpehu1jtFuogzKvp8LbObYVJtszqnLifrqYsDinjiuuREk60PubTilAPuFmRMttROZnGJpkgPS2JCr9sTWo9PCCD0I83DOzyRoVQ6mtgWvCaIIBb7V9iojNjuM6Q69ThZx0EY7_LN_Ymgur5Mu7zBpymY6Crp0lO3QOl3meJVMurRRBYxRfBhgFzK2p660bQ2vr7YJxuWN8EmcHSWyP3f3MmSkUxiI4gmjEXuy-urn48OUwykXkX3NEMflav9DaJog432mQZFQc0_9LUqSYfrIXCbRXuTb1witB-xqbz0Tuu9t3kb_iJI_I-nKQrYuo8zZnFLyXsPLCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HOfnJDmRhAiAvZdnU12UXNYJ1i7qcxxeGeQwmQo2FQgWIB-HL5RjImSiGHUkT6U2OdSW2mbS4s7uVQQp_jILpiR8v2YSL8QtA39R6k7UwmImojAQVYQ4fEOEv1mpPbItzMwdDOtHTldms3KdI7r3A5WCoxFwG3d3T75F9uaTXVIHgsuZ9N5f41QJHT2TpVuRuQeSC4rCm0Ui8sDWXEMKfR-b16KO2A6uTxBr1SS3JfZEu2ru67f6iCkAwo7ytaetKjrwyi6oY0bgBPb_o1dGFfkudXy34j1LRIs5w7WTndB_OngA3w0ALjTkWfxYDEajNDW6Rya398S9h29sUCpKUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GFtgH0rVdFtJyouJWcvcN1yB8xMFhY6a2mNCtH7BBt4NTnH1MxaEdQZ8TnhtNG7vF_gu6YSBYGo7j_KzXAjZxM7UWUyKdZu8OBcvqhEOvgOyoNLERHs1zmtr-W-FRYenLIrjGTS3UHWkOvNpVbrwSV0mecibMOCupHATLfAbxp-AB-W8b4EBDADpFK1wYwKwkO5Aceq7EHp8VpSR1qkBgRPUfQg79AuvKw2cUy2eJcUd-mKkwNtlhsFrEjIfLht6xhhp_yR9CZhq-2NWtTN2-9QdFftxnVuW8xkQkBM9TjC9V9jbLnGpZPh_PHOlmoEHe9Y8SKXxNR9CopwJg5iEKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o-RSm7QYdY6jClrJmf1NmvW-75R4EqSp39J2TSisEWTNls41lmo3yWqZEO45sRomC7Rtoa1mfUnTjGJG3FJehMFjxXaSgy9XiMTyCuV69l5L9udEjWReQcULAZ1e9dVHSG1cRp_eVRsqqDAnzlrdouNJWoILuB1byWr5r9skR-oy9EVsnmhMY8QMiS24_2_CcCl3KwELh814p2O_Ej7eC7EoPSaafk2YYjJMESis2g2jXEC9355skWAbUZXPW3jeKdqx_uG3FL6uvnWsiwzXrIh6wVzEt4H9lOEddNsf5w0CQTwvuqcDCXDz2tHkeESMtUo5D7O09yukq1LN-wPVRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PQmMcow6vasvJkWDMRA1oyQ4nLTc9mo95W_wfbnJCuDlstN-CTMPvVbM8iv6Un_hNJ7Rzs4MxMhQXGA5A5ItNO5ukNVpg2KvH3v2CUKdOHl9bjf2mlhZiSJkgAxEUISZKytfqDKH6kMirYNS9lPB0Wyk-mLEEyuir6qy_k2atBZ4V95B1B3z_9HFH5QjSuw4_y0AngEWUWTHZ_UZZ7xOY0TsLiIMche7MX24Mb15ASd1OV8WNWj98LZxMWQmgOnIQlFG0PMF-Ax6QfA3rRYl13O3hTy1TXdcggGdt7Q8u_ADlUnifU1fu0qdeKt5XWra-NNSNE7gLmI8Qk_ZOyBW1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cFMNkbTR-PPDXA5YBPYsmgVpFhCMpf9LQNbWQVlnENcP0l_lNQVGxlZhQvTWmYl6aC28AdgiWrikfJRBATVIHwwng4JHxpReTCneJj2RLMYMY7tJZKA0QzVCqC3TQDFeKvy_NDwWPhTUoOQ8dPKi9D7t2cJ91NF5V-Z-AUnkLfKQ8lgLjdf0FWYBatcNfpeP_9h_Td8m-ByGwaiINJnibdFQ2FsNwRmhAbY17EH1S2M3ibs_qcnH8R1HOgvXQ2jJo1-xOyUdELHBhFBKlU-lf9pbAL-xbfK-vtV7qvMiKk4ne-8tPVmsr2f5TAWjkdgmSNRM2TNRHtPtcuTzID_RwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
خیابان ستارخان تهران به بزرگراه شهید چمران متصل شد
🔹
پل دسترسی خیابان ستارخان به بزرگراه شهید چمران با حضور شهردار تهران و رئیس شورای شهر افتتاح شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/467526" target="_blank">📅 20:04 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467525">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‌  ‌
🔴
آلمان، کانادا و اسپانیا از شهروندان خود خواستند از حضور در فرودگاه بین‌المللی ملک خالد ریاض خودداری کنند. @Farsna</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/467525" target="_blank">📅 20:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467524">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90ff823252.mp4?token=Q9bYdJA1vvtH2rFA3I4E6FPC0uw8r2Rc3bq4pvaubQNnXigaciyWOCMVYCLcGQIYQHDw-7hHnvCXMPgBSbMTdtBG3FifWTWdnF48VtTQZRfy20KILK0a9_ZGxUXxuyaU1jgPRnix6EA6klFGoDF86nyD7vw89PcwGbluyjgT4u81W2quKdUCM6hC-DMC7XSXj2pR_fAT3zmVWSNjG6WUVZ87j5teO2yAbjgVJF1Z7Yn6bapBy7zxbkiO224o20bCvsCdxj3hH7T_crx6fs9Hl1qfc2_g0LM5v1XrE8kbpqYGEGeVo-H_iJBbyR1nA_pYOH_ez6dA2S-kLiWpt31bCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90ff823252.mp4?token=Q9bYdJA1vvtH2rFA3I4E6FPC0uw8r2Rc3bq4pvaubQNnXigaciyWOCMVYCLcGQIYQHDw-7hHnvCXMPgBSbMTdtBG3FifWTWdnF48VtTQZRfy20KILK0a9_ZGxUXxuyaU1jgPRnix6EA6klFGoDF86nyD7vw89PcwGbluyjgT4u81W2quKdUCM6hC-DMC7XSXj2pR_fAT3zmVWSNjG6WUVZ87j5teO2yAbjgVJF1Z7Yn6bapBy7zxbkiO224o20bCvsCdxj3hH7T_crx6fs9Hl1qfc2_g0LM5v1XrE8kbpqYGEGeVo-H_iJBbyR1nA_pYOH_ez6dA2S-kLiWpt31bCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نظر متفاوت پهلوی پدر و پسر دربارۀ هسته‌ای
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/467524" target="_blank">📅 19:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467523">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDt2OH1_qS43pbf-C5uwmmxr6yVKcrT83TPT_dLBJxe3Ak6FLjK9FLdqXDfbtmaNOtNmSIZYy8hjG96kyzQ3mUARHa95fwhqo32jGHo36uyv8laTFbBbub8QRqvfrnyjEGYKMgV339wwSI_kHawLFzV8st1JwnSdSFXZVrptwH0M151hWgXsAPX1g_YTI19tfpaRBc2aRxdNj87j6ohY68vhWLUDLHYH7etTwoTeIZ6TXJ1c_hreH0IeSB6w5jYPh85CO1pxw0mUbBDUIXHnRMGkC9fRp_82j2AEAb2lKvO58EseTFT9hlydTF8T6niwFdhri80N0JRFzyiqB4qM7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طوفان، صدها هزار آمریکایی را در تاریکی فرو برد
🔹
با ورود طوفان «ایسایاس» به سواحل آمریکا، برق بیش از ۸۷۴ هزار مشترک در سه ایالت جنوب‌ شرق این کشور قطع شده است.
🔸
باران سیل‌آسا، گردبادهای پراکنده و بادهای شدید چند ایالت آمریکا را دربرگرفته و ۲ کشته برجای گذاشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/467523" target="_blank">📅 19:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467521">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‌
🔴
شرکت هواپیمایی کویت از لغو پرواز کویت-ریاض و بالعکس به‌دلیل بسته‌شدن فرودگاه ریاض خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/467521" target="_blank">📅 19:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467520">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‌
🔴
وزارت خارجۀ یمن: هرکس به عربستان برای ادامۀ حملات به استان‌های یمن مشروعیت بدهد، در جنایت‌های سعودی‌ها شریک است. @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/467520" target="_blank">📅 19:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467519">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌  یمن: مسئولیت افزایش تنش‌ها در باب‌المندب با عربستان است
🔹
وزارت خارجۀ یمن: تبدیل باب‌المندب و مناطق اطراف آن به صحنه عملیات نظامی از سوی عربستان، امنیت و ثبات این منطقه مهم برای جهان را به خطر می‌اندازد.
🔹
ادامه عملیات نظامی در باب‌المندب به تجارت جهانی…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/467519" target="_blank">📅 19:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467518">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سعودی دوباره در باب‌المندب شکست خورد
🔹
سخنگوی نیروهای مسلح یمن: برای دومین بار ظرف چند ساعت گذشته، نیروهای مسلح یمن توانسته‌اند حملات مزدوران سعودی را دفع کنند.
🔹
عناصر مذکور تلاش داشتند از «لحج» به سمت باب المندب پیشروی کنند، گفت که با ایستادگی ارتش یمن،…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/467518" target="_blank">📅 19:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467517">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/593bce2b54.mp4?token=VqtT98aiSprN9CyMVI-lKWMeGRd-LJ5vDOGC2DqA5FLHSe7c934h35xV8ngfXuN7OKhYCOPPkGlv26DIBdMn2M9owC8sVr7lEmC3E4LrXKdMWNPF6k0ivLqeXU9vCZtoe4KHh5Cf28Dj1WTavXLnZYNj5oCLkqdK6peUz9kzCzqqCb0JHW_HwzUlnMvXZ4aJ9ekGUxo_uDZEt6hnmNV_J8vBrcsMbR2UONgpxtb2uaqHaPCtM_jvjYKYPpMTm3axclGwmjYuwmifrv4LgCzYyBOSq5tZCNQYrtQXFAxF15bW-Toj_qISbsCoio_-SBUT-NhVncKGeVBRzjFoeTNSMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/593bce2b54.mp4?token=VqtT98aiSprN9CyMVI-lKWMeGRd-LJ5vDOGC2DqA5FLHSe7c934h35xV8ngfXuN7OKhYCOPPkGlv26DIBdMn2M9owC8sVr7lEmC3E4LrXKdMWNPF6k0ivLqeXU9vCZtoe4KHh5Cf28Dj1WTavXLnZYNj5oCLkqdK6peUz9kzCzqqCb0JHW_HwzUlnMvXZ4aJ9ekGUxo_uDZEt6hnmNV_J8vBrcsMbR2UONgpxtb2uaqHaPCtM_jvjYKYPpMTm3axclGwmjYuwmifrv4LgCzYyBOSq5tZCNQYrtQXFAxF15bW-Toj_qISbsCoio_-SBUT-NhVncKGeVBRzjFoeTNSMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بایرن سریع‌ترین گل تاریخ بوندسلیگا را خورد
⚽️
اشتباه نویر در ثانیۀ ۴ بازی مقابل آکسبورگ، باعث شد زودهنگام‌ترین گل تاریخ بوندسلیگا وارد دروازۀ بایرن‌مونیخ شود.
⚽️
این دیدار با نتیجۀ ۲-۲ به پایان رسید و با این تساوی بایرن شانس صدرنشینی را ازدست داد.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/467517" target="_blank">📅 19:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467516">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6qbOQae-OoVB9AlHXn_cr4MxMdasroZiJsI3j3MSJ6gddI9enkXh5o8iQmohgjW2CDuDvlzl2UsTBlavPC3xPZssu_K5HdjL0F4tvAfXrJSOj4MS0jUIJVgToAG_oLCpU1jpKByom2Y6CAn33yueV0yu1cAAcqPzA6cE_Lg_28uauMo5-NjmrxDe7D1XSkSEJ8pYf8ZMold0v--M8EU3rSKm594XZDg2RNJM1qpDeuNV_l69FN_zsYvp1sWEKFTY_4zGRHwZIdQhpPXlY5Ympu2YOwv4m-d3hOs67tzfXIMXNUTJthDnWKsN2PoRKPCBlacji307S0cHqUDui1Qtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار غول‌های انرژی دربارۀ نفت ۲۰۰ دلاری
🔹
مدیران شرکت‌های بزرگ انرژی هشدار دادند در صورت تداوم جنگ و توقف جریان نفت از تنگۀ هرمز، قیمت هر بشکه نفت خام ممکن است به ۲۰۰ دلار برسد.
🔹
مدیرعامل شورون می‌گوید قیمت واقعی نفت هنگام رسیدن به آسیا به حدود ۱۵۰ دلار در هر بشکه رسیده؛ درحالی‌که نفت برنت در بازار آتی حدود ۱۰۰ دلار معامله می‌شود.
🔹
مدیرعامل ویتول نیز هشدار داد اختلال در عرضه نفت خاورمیانه می‌تواند بحران بازار را تشدید کند و کمبود فرآورده‌های نفتی تا زمستان ادامه یابد و سناریوی ۲۰۰ دلاری رقم بخورد.
🔹
مدیرعامل آرامکو هم از کاهش شدید ذخایر جهانی نفت خبر داد و گفت بازسازی این ذخایر ممکن است تا ۲ سال طول بکشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/467516" target="_blank">📅 19:08 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467515">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
برخی منابع از وقوع چند انفجار در فرودگاه ریاض خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/467515" target="_blank">📅 18:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467514">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUpVUccEQI5B8rtvVVs9-Y8sExsstUl5Ki30HBY5VhYE9IeC_de8CmjlLXtlWheA1kMohCiw1eUDJKyX9c-sRC7frMrMXB6DCSY94EDM-fT7O1k4jz7CkoPnit5q56fqlOhQsRZt2ws-6_wY9Vw-Gj8KqMGriXQK8uO_BHwtMgQQoFdP6uYMbwGXdb0R5E9y-h2cN2_jlWo59MTi9iN6HEyvHnJWpuhYD5xTxSfd4W4zeV1XdDkm-YezcskLo1OObXUShUL1QX5PHladaA5qvVRbcsWurWsvjJUInM68Pz1Q3RrMyJo6QEpOAbT75m0sRfcp_WJyUmWOuYTYbG7ZnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود عباس انتخابات فلسطین را به سپتامبر ۲۰۲۷ موکول کرد
🔹
رئیس تشکیلات خودگردان فلسطین اظهار داشت که به دلیل موانع سیاسی و امنیتی در قدس، کرانۀ باختری و نوار غزه، برگزاری انتخابات ریاستی و پارلمانی به تعویق افتاده و زمان جدید این انتخابات سپتامبر ۲۰۲۷ تعیین شده است.
🔹
خبرگزاری رسمی فلسطین وفا گزارش داد هدف از این تصمیم، فراهم کردن زمینه برای گفت‌وگوی ملی فراگیر، تقویت وحدت ملی و یکپارچگی سرزمینی و نظام سیاسی فلسطین و رسیدگی به موانع پیش‌روی روند انتخابات عنوان شده است؛ که مشارکت شهروندان در مناطق مختلف را با دشواری مواجه کرده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/467514" target="_blank">📅 18:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467513">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‌ ازکارافتادن کامل فرودگاه ریاض؛ ۲۲۱ پرواز لغو شد
🔹
به دنبال شنیده شدن صدای انفجار از فرودگاه ریاض، منابع هوانوردی از توقف کامل پروازها در فرودگاه بین‌المللی ملک خالد خبر دادند و شمار پروازهای لغوشده از بامداد امروز به ۲۲۱ پرواز رسید.
🔹
درحال‌حاضر تنها یک…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/467513" target="_blank">📅 18:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467512">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‌  بازداشت ۷ مظنون در پرونده شهادت مأمور انتظامی فاریاب
🔹
رئیس حوزه قضایی فاریاب: ۳ نفر از مظنونان کمتر از ۲ ساعت پس از حادثه به مراجع قضایی مراجعه و خود را تسلیم قانون کردند؛ با ادامه اقدامات انجام‌شده، شمار بازداشت‌شدگان این پرونده به ۷ نفر رسیده است.
🔹
مظنونان…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/467512" target="_blank">📅 18:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467511">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ex952vynlaxUIzMx0zV1yqfWBX5GLT8PoOcMWlBHNmjv0fPiBLaRpm87ba-5wDnMARa3sqB11R8Pt1-FgDQhRuDihBzLGhGobG8rx8RX1D4l8THi6Q7wVfrtXLzY8tVhP0hmMWm6MfkAHIk85nmo9EqtpCMcmu_0Ube2UiKaduWWBjFc_9kzdCmQx_Uj5U8dVd7SlWtf2UDgCNDXDdlwQ98aLVfZyJPeSiwppGYmWjtH-3FaW-ry9O6JVdcWLtRCp7_NCmsj2_Eu8DKxXq1PXTB-XAaOLe-Z_wYpD3hX9Xa2CmA8NRkiKp6CF2jpItMegaYO7qpQwRB6Q7F19CkVGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی توافق ترامپ و پوتین را به تمسخر گرفت
🔹
زلنسکی در واکنش به توافق صادرات گازوئیل روسیه به آمریکا، حمله روسیه به زاپوریژیا را «تشکر» مسکو از لغو تحریم‌ها توصیف کرد.
🔹
او با کنایه به ترامپ نوشت: «امروز روسیه با پرتاب ۵ بمب هدایت‌شونده روی ساختمان‌های مسکونی…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/467511" target="_blank">📅 18:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467510">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72c7e7aea.mp4?token=kJ78kMyGVeJTLzWAtPr0w2XQS2BkZBLQthYKMbDDyA3xCIBEupWI9W9urkXNFFZTc56bzjbO99ukzLg56seFYXlovkxUWSEC579qHxV3jGBSqDMdKmM1K3CE2PGbz1lKIBOkYzLxFrJ-flUsHULGIIKNJQS4bDMHgFCKiblHjytdlFtHFQ-R09zruoPTDnikyOBcahbRALzZ_NdiVHGXcJxsIOcQ2c73VZ9B6vpXyqj9uYu9zxHNwS2UYbEpCKzO_mfJfuY2R7nt6Ye--jLLCJ2ndTPesINvRW6_gtZ5lfIcilpxKB6IMM8v8QQXtQvLj87Sa2doqzBj_DgEUnNaqK88obdH_nI0HoN-DCdM8Qk3TsGwFAdN-e8Rzo3G-___OwPvB5YL0Vqq_Nc22t77afPSwZngzfvswDLbo4EmbNPG6LHAd6Am5H45rWtiji8I1wkcu5mrXW_n01qFbXdZVKXXbCikejSsj73c3udr1Q7y9iTupNfDch7z9-38DZnupBRMeebyRM9pZKZQrmG7zSFw5k6mmy2yPwPB6uCVGcEB0tjN9gjU2kJOf0WPIGiZVW9UBdrG7AO3gVwa6MY2DGClnsivkdUdbwY8U8-3IHNdbpCbaEINBiaqVKU816iYW7AzbDqakgJAEhEGxZF3Q0-Fq7VbY34LI81uj3C51dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72c7e7aea.mp4?token=kJ78kMyGVeJTLzWAtPr0w2XQS2BkZBLQthYKMbDDyA3xCIBEupWI9W9urkXNFFZTc56bzjbO99ukzLg56seFYXlovkxUWSEC579qHxV3jGBSqDMdKmM1K3CE2PGbz1lKIBOkYzLxFrJ-flUsHULGIIKNJQS4bDMHgFCKiblHjytdlFtHFQ-R09zruoPTDnikyOBcahbRALzZ_NdiVHGXcJxsIOcQ2c73VZ9B6vpXyqj9uYu9zxHNwS2UYbEpCKzO_mfJfuY2R7nt6Ye--jLLCJ2ndTPesINvRW6_gtZ5lfIcilpxKB6IMM8v8QQXtQvLj87Sa2doqzBj_DgEUnNaqK88obdH_nI0HoN-DCdM8Qk3TsGwFAdN-e8Rzo3G-___OwPvB5YL0Vqq_Nc22t77afPSwZngzfvswDLbo4EmbNPG6LHAd6Am5H45rWtiji8I1wkcu5mrXW_n01qFbXdZVKXXbCikejSsj73c3udr1Q7y9iTupNfDch7z9-38DZnupBRMeebyRM9pZKZQrmG7zSFw5k6mmy2yPwPB6uCVGcEB0tjN9gjU2kJOf0WPIGiZVW9UBdrG7AO3gVwa6MY2DGClnsivkdUdbwY8U8-3IHNdbpCbaEINBiaqVKU816iYW7AzbDqakgJAEhEGxZF3Q0-Fq7VbY34LI81uj3C51dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رکورد فروش محصول در هلدینگ خلیج‌فارس شکست/ ۲ جنگ تحمیلی هم مانع افزایش تولید نشد
🔹
در شرایطی که سال گذشته کشور درگیر دو جنگ تحمیلی بود و صنعت پتروشیمی از این جنگ آسیب دید، بر اساس صورت مالی منتشر شده «فارس» در کدال، گروه صنایع پتروشیمی خلیج‌فارس توانست برای اولین‌بار میزان فروش محصول خود را به رقم بی‌سابقه ۹۳۱ هزار  و ۴۶۳ میلیارد تومان برساند.
🔹
این میزان فروش، حاکی از افزایش ۵۶.۴ درصد میزان فروش در سالی است که حدود دو ماه از آن صنعت پتروشیمی کاملاً متاثر از شرایط جنگی بود.
🔹
نکته قابل توجه این است که این افزایش فقط شامل رشد ریالی و دلاری فروش نبوده و تولید نیز علی‌رغم تمام مشکلات ناشی از جنگ در این گروه در سال ۱۴۰۴ نسبت به سال ۱۴۰۳، رشد داشت.
🔹
همچنین آمارها نشان می‌دهد که با وجود توقف ۲ ماهه تولید؛ میزان محصولات تولید شده در گروه صنایع پتروشیمی خلیج فارس از ۲۷ میلیون تن در سال ۱۴۰۳ به ۲۷ میلیون و ۳۰۰ هزار تن در سال ۱۴۰۴ رسیده است.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/467510" target="_blank">📅 18:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467509">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUFFqwQ8njlYi1AB3ZnJOtEMUS3-1H1S0c3paYfVHRE2R6ZBw-ZtBg5L9_rA2OaQzEoL4zA8AFwbshU7zPlzAniP0PPiakJRrDj3ScEEPOhr1mas9wmiFAC4TrujusZMZD3QUfUU0hzUKZQGSUIkATEhE5uQ8nO-mbUGGrGy1hXrc5FdCKOl8kKnEIVwiquO_nLROYH_7WuwCNNzw__BCm9QE49GDVh5Hp-BiTmy8QUyUZ14wfDaFnTjLrFT6lrfWGg83DywdzUZYNpBk4qNuWp8h03gWHgM2LjXsw03CSnuMjI9fYBc9Or6SMUIuabhiI990s-rL5ZPvkhPM4StnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
متقی‌نیا در حاشیه آیین ملی آغاز سال زراعی ۱۴۰۶-۱۴۰۵ خبر داد:
تقویت حمایت از کشاورزان با  توسعه ابزارهای نوین تأمین مالی بانک کشاورزی
🔻
مدیرعامل بانک کشاورزی در حاشیه آیین ملی آغاز سال زراعی ۱۴۰۶-۱۴۰۵، با تاکید بر اهمیت تأمین مالی هدفمند و به‌موقع تولیدکنندگان توسط نظام بانکی، گفت: توسعه ابزارهای نوین تأمین مالی و تقویت حمایت‌های اعتباری از کشاورزان، با هدف پشتیبانی از تولید پایدار و تقویت امنیت غذایی کشور، در دستور کار بانک کشاورزی قرار دارد.
🔻
آیین ملی آغاز سال زراعی ۱۴۰۶-۱۴۰۵ امروز، شنبه ۱۸ مهرماه، با حضور رئیس‌جمهور، وزیر جهاد کشاورزی، مدیرعامل بانک کشاورزی و جمعی از کشاورزان، تولیدکنندگان، تشکل‌های تخصصی، پژوهشگران، کارشناسان و مدیران بخش کشاورزی در سالن اجتماعات مؤسسه تحقیقات اصلاح و تهیه نهال و بذر برگزار شد.
🔗
مشروح خبر
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/467509" target="_blank">📅 18:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467508">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/467508" target="_blank">📅 18:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467507">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/662419a612.mp4?token=b7RYp2i9L0yt8CzQAGC_jzEHcIQ5Rem6oMjWOYpACwWuOrI-McTy3a7h6q_YWWyDhm__GH1S_6MTyc2OUqCeTEAPPrVRePmwp9nK7YFcKRx1M5kXUi5l5H9eIQCLneWoJMW9bpNwJwfT7_JU7rdWWhWvsrJ6TLpMINAaGnVaZFb4gUTyVnqJO_SvNIyTGRnFfbw2GgA1tQhPbkbShhvhJktOnB0nVFe6-AL5n_ZtUZ8kKNN0E-Te5m2VQvZtC9b8fJOGY3DsnOEgB7Kud0jBLg92XIAcTkpkFpF2oR0FEFz3jkfBlLBBd17XtYd8CQrTUvnKGWVK29Nl6sj8IJaW9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/662419a612.mp4?token=b7RYp2i9L0yt8CzQAGC_jzEHcIQ5Rem6oMjWOYpACwWuOrI-McTy3a7h6q_YWWyDhm__GH1S_6MTyc2OUqCeTEAPPrVRePmwp9nK7YFcKRx1M5kXUi5l5H9eIQCLneWoJMW9bpNwJwfT7_JU7rdWWhWvsrJ6TLpMINAaGnVaZFb4gUTyVnqJO_SvNIyTGRnFfbw2GgA1tQhPbkbShhvhJktOnB0nVFe6-AL5n_ZtUZ8kKNN0E-Te5m2VQvZtC9b8fJOGY3DsnOEgB7Kud0jBLg92XIAcTkpkFpF2oR0FEFz3jkfBlLBBd17XtYd8CQrTUvnKGWVK29Nl6sj8IJaW9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تکرار سکوت «عبدالحمید» مقابل عملیات تروریستی
🔹
درحالی‌که گروهک تروریستی جیش‌الظلم مسئولیت ترور معاون اجتماعی انتظامی سیستان‌وبلوچستان خانم افتخاری را بر عهده گرفت، امام‌جمعه اهل‌سنت مسجد مکی زاهدان مولوی عبدالحمید تاکنون واکنشی به این عملیات تروریستی نشان…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/467507" target="_blank">📅 17:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467506">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuBRs1gjd4x9ZBnglL9xpSWHMRh8T32gG3m3Y7OGRW8TeCa6qAvw3Q6hz82CRo1b9MaNzEbCQsUuM6VP4hkGy_irhVOGIUefpti60NH7k5H4h8Mhel5goliweOEC2vjwCruaFMZYDu-cQrBTbKgNHc9lZkzAEZbvdQvk8VYsKui6yIc5Xnwkt9kHLFoC8RoDZKA-4WPihv1fv95JBzbeTGQy5FvGzhGlUsFk1bIgwZh1G_UBCkKRI6SIxpqGSrM7GXbJdmq6F9iLjohOt3_4_QUZT9SJEIc_nZDfxbube_6a8zL5RhB6oLHKy84xPvVTm9wnewfWc98nAZjj6X7Fbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
برخی منابع از وقوع چند انفجار در فرودگاه ریاض خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/467506" target="_blank">📅 17:41 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467505">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWAYKiNkhDSugQBmVLhMR0cT3DOp3qrthlDZ5F48NXMQMJXNL5XtLGLPQQfiIW1Pf0sTuGWFfG1wAGBf8GOW9bH3NUTLC-zhtOMijKp8g5sfs0B3pFocUIcpv6yAyLcp8TnDgiNyUv1kb9gzrmHS9K3mwue1Ai9NWz4JnQ_o-ggjEnCJcyi3i-IN6yP9dzIYwoegzqwvo5QCzqzvcknfK-XbYX-vYcLb-09OUjmwOZa9Oc5xlwRRI2GOYQikI1PnDmJ8uU_O3j96r6Yo77aKqB33EJMXBtlDxQUJD4z-hT4yz8XhGTnAztlfOGTtLfO_U81s4WnaKwh-Xfoa28i6bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک مرکزی: بانک‌ها دیگر اجازۀ فروش طلا ندارند
🔹
بانک مرکزی با صدور بخشنامه‌ای ورود شبکه بانکی به خرید و فروش آنلاین طلا و نقره را ممنوع کرد.
🔹
مسئول گروه فین‌تک بانک مرکزی گفته این تصمیم باتوجه به «بروز ریسک‌های جدی در یکی از پلتفرم‌های فروش آنلاین طلا» و احتمال سرایت آثار آن به شبکه بانکی اتخاذ شده است.
🔸
بانک مرکزی این تصمیم را از ۱۳ مهر گرفته و کاربران بلوبانک سامان نیز از هفته گذشته اعلام کرده بودند که امکان خرید طلا در این اپلیکیشن غیرفعال شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/467505" target="_blank">📅 17:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467504">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تکرار سکوت «عبدالحمید» مقابل عملیات تروریستی
🔹
درحالی‌که گروهک تروریستی جیش‌الظلم مسئولیت ترور معاون اجتماعی انتظامی سیستان‌وبلوچستان خانم افتخاری را بر عهده گرفت، امام‌جمعه اهل‌سنت مسجد مکی زاهدان مولوی عبدالحمید تاکنون واکنشی به این عملیات تروریستی نشان…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/467504" target="_blank">📅 17:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467498">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cjgwy-M5t2J4RhvK8ZuLXg8C-GnpGLjmqUqyHtJsqrGqGmSFBTLGS6a_v7m13n2zcwmVl4FK9a7kEs0CV9tuJORh4d_99TFZpCarCDpcVx1NpyO2Nu6HrXGIMZM1_wgICGj6CrokCQkJlaNTyXJk31ESZKniZw184eLVLS7GatKq2dai-vAAEwS4zw0QHrALwtdK5UmbL5sP69epi-L_LKC0souG5kSv4mJcP6mheJngqvlQsPZLihnWPGEAJwEWo6L8vJ1glCHIW0npC7BzQ15FmfrCd0ikHiIA8UZtWfdoYuL4hzR_tFILoSJDE-k7pdIc7Kwlbmdu93a9-7zTOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MBvS1QFaBX6vl00io-7D9jMlqZ5RbqqNjE8aB9csiORoM3ymMvptJhmihNINqDtNRiZNSKYmRphT9XlhYp20XazEKKuam50SZT5rflqN0UugsxxJgYMqBio4b-QM1DE83Z00-oFYN9lrLZtxBB2ypurtw4JP0A_Kg16qA1cTkVaa_FvWliv3ESvUme9pfVKvlX2ORB1XEudC61JB2JC2syql96vz50M74ejPugG_hScSxMS2SAEvatPRdKycWHUUhNc4VQwTi8VvOuTLKrtwO_IA8YDsCQgx2aTtZCok4-vsaqNscXdCf-6pAqS3ZOIYq4WU4Z4o_AN7pSixfBaI_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aXXOokA0Fe-tBYhLPTlK3XyFczpP8D1VCJPl_ZZjfrvQHTRhbgjEgUXpr4rObsiffq-GPJtGIrzaSsy_BFJ59fm4c_8tlIH41BLnMe_hZAD-pWNWUohOO7wj5ccu1IGSw59g6IwIYDjd5V9hV2T_3TtMKUhF6ZcbImuAaYEfuVPDGmC6u32e0rwd07Lgz5VP6kv8xka2PV6bCliItLQFCKl5U11NnGybyMP3mmt8yhINkNh1VtJ6-NxxQuEgpdca-zHXOVnWVmigFPZcqfyMJEjnQ3kvl7uOviZ7S-cnU3nvRN1pKjUxf0t9khM_RSs_3lqhKMckiM_ZowPz36qUtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jFJR4wnHSF1L7jqJ3kt-n7jHbqbWZ7Jjx0RXmj1CRV_qS9HczyCOPhSx3UNRpvGkA47fX0uIa2QSW9CJD2mhiWPKLuMBKmw-8PTz5tt4GJk6tIF-Giz15XTbLpK5FAgtSRF2Phozn2MSPC_frFJIqPCaTqBkNh8xx2otSsDhYANPESTzlZP5WmoAfTLw7ZMj1N9gDyx3vdVsOv-sNS3yer8uWuuEOgYDk2rYsFx0urfS16IXWp34B70wSVBvP8KxgqAWklXaU5XSmwEQfeSng995ajxc8yUFc6LtNvKr9MqmvMFg3V02WNC8mgnWQXW4QfbGPVD6OfDstfgN64Lnpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rUeI1MCGqU0eXkxf4ma5gJQpG7mC0Zb2MyeTVZi1LGH3f3xdA2_b0zkvLbG4I7HG_rQvlYApQapoYOnllxY1TH4wKcvuRV2GYfBwNk6s5pfpq2d8-GrOvaetJdqXhYFAZbNdwUdT3CanMVqQ4OkNtCievZXft2y58DAmeGLlHOhn4mkvuBACnHBAOjc3OnabZuBVoy64oF02I0vhvOTNlTM8dqVwhhO8nqVz8ZWPljkjqK-xqaLvlp4c44RSnORVkLLEBQMmXS_4rerT8IcB4dMZLqXHTARnFYeN8q4-n-IFwAvFPiWyE7mNCPvbr2aMoV69XorrYdrLVtSxXXd-YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d9uLzPIppXBLpa17ty-5oW3K0u4dNTAuXNbiJhaEcupkS-K0xTasaxTF1Nx6dAwIxOb_liZU9_dDqRpFrfhpsP0YCrnO8L-hry1jlnG4-T_2S6t6tdxLP4ujmEaQ-61v2IkYhTDvrLJbY-Bc4x3fQds12VC1s0mzFZysA2EQirDzbcnwG-1-s-rlhycUwWxUIMF_OHwVUOZ59owGeZ-LQbGt6_DEL_N4-h2f006C8ZQb1X6F8wXpsLT7EguoVNxyXA0Bo98r9MqXbbbeFxPPN91SEhH1JNwx_iwZ68WJ1qAeuJKKpSS2xW4WAFVav15vNZ4w6z4AqgJZOPZhFOoEWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تجمع دانشجویان مقابل سفارت فرانسه در اعتراض به سرکوب دانش‌آموزان فرانسوی
🔹
دانشجویان در اقدامی نمادین برای اعتراض به برخورد پلیس فرانسه با دانش‌آموزان میز و نیمکت‌های مدرسه را در مقابل سفارت این کشور قرار دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/467498" target="_blank">📅 17:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467497">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حکم قصاص قاتل یک مامور پلیس اجرا شد
🔹
رئیس‌ دادگستری استان سمنان از اجرای حکم قصاص قاتل شهید محمدجواد رحیمی، مأمور انتظامی دامغان، خبر داد.
🔹
شهید محمدجواد رحیمی ۱۱ شهریور ۱۴۰۱ هنگام انجام وظیفه در بیمارستان ولایت دامغان، با شلیک ۲ گلوله به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/467497" target="_blank">📅 17:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467496">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsTb00sgX7kRUN0oPG8IGdFJXhlUDYA9t9u2Rc4ibl9henS9j_QqViQLs3EWdOjNDZByLgkzHqCUnjl1dlHlq-ae64EoZgBX6539FkC-GXMToGtN0J33UPfbzxoY1HHoOiqq1JAFrzB3ZtNaNw0ve58YdlERAntnwAerzH9nt8mYx6WkVPipWcNBesLLhuCRfqQWFEfjXiwQGNH4BzC89JTtLL0kCz-jmI6ZsgLaDV_rVQ1bWUuFF1fhdAYLrnpKiUn6R10I_klQ6E9hZHveMpLwknGOAmo9X3eFaXzGn0FQZnbp5TvGlYIOnOpByKu86FlAJssyeJfm74KIqACVZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه هم سراغ محدودکردن دسترس نوجوانان به شبکه‌های اجتماعی رفت
🔹
رویترز: ترکیه درحال آماده‌سازی قانونی است که دسترسی افراد زیر ۱۶ سال به شبکه‌های اجتماعی را محدود می‌کند.
🔹
این قانون خواستار اقداماتی از جمله احراز هویت سنی، فیلترکردن محتوا و محدودیت در استفاده…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/467496" target="_blank">📅 17:08 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467495">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd46f834e3.mp4?token=V7mcmH1eFf38SF-klZJfx2mUXWRrhlEV2CEaCe-GDh_521hGACTCiFwwRkRoCxPgz7s1ZiyqLoyEBcCSNrrmdGeNekTQzJTeWe9V7hZURFdWxcX43Us45aYSi22uuoEJ2C_XFwTFYrAiqt8xfLTg4Ti5szR2ozSEvWlRtK7vsplLlPmVmpWbL_5mdFAJ_2uthSPFnqna6OWD50lAkqwSVn21m6i6DhAsE1-ZFcX_ZbYuzgYAul0PRFY6UMpyUdBpeEyIKLnBrRT8U181FMoIRwPiy27_DFUfVnxAcIfy2iPUzOj_nP9SdQNz59q47_FBXhSXZn3Pbs8QkO6Uyezv_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd46f834e3.mp4?token=V7mcmH1eFf38SF-klZJfx2mUXWRrhlEV2CEaCe-GDh_521hGACTCiFwwRkRoCxPgz7s1ZiyqLoyEBcCSNrrmdGeNekTQzJTeWe9V7hZURFdWxcX43Us45aYSi22uuoEJ2C_XFwTFYrAiqt8xfLTg4Ti5szR2ozSEvWlRtK7vsplLlPmVmpWbL_5mdFAJ_2uthSPFnqna6OWD50lAkqwSVn21m6i6DhAsE1-ZFcX_ZbYuzgYAul0PRFY6UMpyUdBpeEyIKLnBrRT8U181FMoIRwPiy27_DFUfVnxAcIfy2iPUzOj_nP9SdQNz59q47_FBXhSXZn3Pbs8QkO6Uyezv_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیلاب در شهرستان‌های گرمی و انگوت اردبیل
🔸
صبح امروز بارش شدید باران در شهرستان‌های گرمی و انگوت موجب جاری شدن سیلاب شد؛ آب‌گرفتگی منازل روستایی، تلف شدن احشام و آسیب به پل قدیمی زیوه از جمله خسارات وارده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/467495" target="_blank">📅 16:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467494">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
برخی منابع از وقوع چند انفجار در فرودگاه ریاض خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/467494" target="_blank">📅 16:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467492">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">در الوازعیه نیز پیش‌روی دشمن ناکام ماند و تلفات چشمگیری به تجهیزات زرهی و نیروهای مزدور سعودی تحمیل شد.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/467492" target="_blank">📅 16:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467491">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6dd6590e0.mp4?token=ti-8cgwJzRDfEDQ8Dc10GBNaEf7NnX5xOdP3TyTrIuzB5zOfCD6uGakKgV9Rgmi1PvpAq3yjKy5ahJyrNTeJ4yjlveEI4fKXSJTNVW8ztN0o_N1Vz5iFincYmLT5arpVJdzGSBUudop_nz9gWuwolqhp_zOhPF7VAjCyEMQgkQ8XvMPPEiGWzao-k8pAH6A7Dt4diDhmHvNyowfS3ZBWaAM_-vrRsw2eM0V-Ug0Tfr9XrZeuLqpY2yYVXoJfrz_NEJaFzFOdrPtdpsD-6sWyVdfmwVMe6Cdk0BoHAmEJmIipHN7sIBa41yCUsDWbuuPAlgCuoK2wZFjVZHLjMTYrQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6dd6590e0.mp4?token=ti-8cgwJzRDfEDQ8Dc10GBNaEf7NnX5xOdP3TyTrIuzB5zOfCD6uGakKgV9Rgmi1PvpAq3yjKy5ahJyrNTeJ4yjlveEI4fKXSJTNVW8ztN0o_N1Vz5iFincYmLT5arpVJdzGSBUudop_nz9gWuwolqhp_zOhPF7VAjCyEMQgkQ8XvMPPEiGWzao-k8pAH6A7Dt4diDhmHvNyowfS3ZBWaAM_-vrRsw2eM0V-Ug0Tfr9XrZeuLqpY2yYVXoJfrz_NEJaFzFOdrPtdpsD-6sWyVdfmwVMe6Cdk0BoHAmEJmIipHN7sIBa41yCUsDWbuuPAlgCuoK2wZFjVZHLjMTYrQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا قیمت لبنیات داخلی با دلار بالا می‌رود؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/467491" target="_blank">📅 16:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467490">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مهدکودک مروج عرفان حلقه در شهرری پلمب شد
🔹
دادستان شهرستان ری: یک مهدکودک در شهرری که اقدام به ترویج عرفان حلقه می‌کرد، شناسایی و پلمب شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/467490" target="_blank">📅 16:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467489">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c725BbEjjdKLusMruFc7RliZxCU55blUrjV9ksk-9fX555cNuvW6wrT_LivdKIGMcCkdRu-wIRw81egbNPBYCoNhBGtOLWA9eShOJegKsVDG73atx3_Q7B7B0QWaI53wvSUrbadZGfdJsPyCgy8sCWMGeWKTNHtS1ONtTpztBfKmXVZ26eCDN9It18dff5tj_KlyodaOiJrZKnrCvfWJaqpoYpCdG1UWQ5y3SPqiPEZP0CYTKGXNfB691I60VbMy7iIziupYjCM5Ny_uOFpGCaQyAhp-PfN-vEC9XORu-t2Qdqga85Wj0PPNbFWKTJukKK0FIjt5TUJiUnaEeIOYdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جیش‌الظلم مسئولیت حادثۀ تروریستی سیستان‌وبلوچستان را بر عهده گرفت
🔹
گروه تروریستی جیش الظلم مسئولیت حادثه تروریستی شهادت معاون اجتماعی انتظامی سیستان و بلوچستان را بر عهده گرفت.
🔸
عصر امروز در پیِ اقدام تروریستی و ناجوانمردانه در محور چشمه زیارت شهرستان زاهدان،…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/467489" target="_blank">📅 16:23 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467488">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🎥
چه کسی پشت بازگشت گلشیفته و خواننده‌هاست
‌
🔹
در قسمت پنجم «پشت صحنه» گپ‌وگفتی داشتیم درباره خبر بازگشت گلشیفته فراهانی به ایران، کناررفتن وزیر نفت، روایت هالیوودی از تنگه هرمز، فروش ۱۰ هزار دلار به مردم، شکایت پرسپولیس از آسانی و موضع ایرانی اصغر فرهادی.
🔗
نسخۀ باکیفیت را در
سایت فارس
و
یوتیوب
ببینید
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/467488" target="_blank">📅 16:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467487">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نیمۀ دوم مهر آغاز</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/467487" target="_blank">📅 15:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467480">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eoXr1Y-IUMNB_A8KxUEXrrK8ZmGqz1-83p9GDHKglcAxJ8egi3fA2noVGvNGEKEOnkWc2hs1crnOH-OTHccqrAjzgyrxjUMTcVoayTMPdJhOe95c7P-hDgy_53-RmiHZg3ZiyFBTUGwrlRjW3SsrqqFYt7fzoF5MGDMZ55jFwFRfZmy3MEzVDW5rqQmRV8GLKQZkzqwRmdOQTcWrMSbcrH1S4yYoK-1Sw4hFNZBDTpUq0dSfBOdq0L4GN7v-D5miQlWlneXqVHDACNe8cTbz-dmVWSdQI3oVut-ifWPZbfj4wZF6tEtLwwlgn_mAnqsfAv59gzsSaEWzFWMAPlSVqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tV846eNSt-f7NX5TBzSYTIMz6A9N6ys7FC6ABOq6WR5eL9wkDlICofkLZwfYp0KhrOF0E1Nmn84cl_A4-VRVC8Mezr5573wstsueyR7et0rnQCPRxnRE8flvhmnUIHf77_yRnwealeMYp6c9slQSl5JB36-zhG6WDeyhGC44dQABMtz2PAWnPMTT7O6Bdbj8mzSnJIxOYCOco2Un3kn-37A4WBitcoAfttUJF1yg1yy7DzCQz0t4PTQfP013Cq1hhVmT5qN-zpbJWp0Q9Au5T3-WmRPPWWBP9QDS0BuB78BvmsLiKAUp4KUrINXGrbrTDlcqqggg3JFLkVW-DBYv-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/onpB3j5XnuL5fs1HPGsDGjmSE8oT_eSWyevGHMg8bOV_izQRgVZQgIVoWmi35g4bDY4z-C1MXE28DETIjM_xgZ2PrBvcK2pFMxk-X3nrpizzUmhjT88hIAXnykSfF6PIgL1_Oz3YDcKtOfmYkE8aRIffHgFczbTJ7A7aYqVnN1BJl2okjxGatrv6l9PBMkmPRBEIwe7SqzYl6SSJrx4r7365PQAfOcRf-W6tIvgGfzC5gvBtOVdsrra2emKjstEuk2AErfQJ5PEIln2hM0KH2coPb14Jb6_P817L7KGwU5Laz1_cASn0Sx6Aym-R0ulP2YMRSGALMk4QoHLbQNt00Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TTxi6ZOvJIcA5kYaCw34bdIV2MPAoy1NwNEqUH9r8sPvNpLqoi033PlDf1c4FstsLDF3hXPME_CZVSq5hQyog1gHjlsGwBR6jUG5aHUYGJaUaJXn1i6UgeQUoYVZWhahrSsJMW0M53IT8fgtgUe9DGtij7YRm4f6ChUOOW-ZQPDiCaPZ8Iv23_OtG7wVZnhQAEm88QOZfiQOYVTOcnF_YfcvRuLyOqZC1OYfkFIOdYFuIpT-pYzmhnzs648woeSusnm-pMsaGsa-0APArRXhTT4m8x_zvBleIxBn4-2gpsoUOJ4iHWQZmOSjYleMdCzaRzeMLzRFLO4v7aYSZpNAtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FrG4PlDcWP4fvDCJAqN-GRBNtRXYuJbXFWUbHg9Gkdz76cntmaNclurkUaftfbQt9eeM434uJK7h1PjvqIk9IyhclyX6fAij7bdxthoO03oMq2FNd9HVq5oVfyVC7ctsilHeamDEWgW4JLyXycbZn8JkFiWufyAEfoGnytC9_j1yxC-69-cNIl4NKguONfWdd8nX9fLD-OHvhd8CuYRv36kEQq55WHwUgILrJM99E0_1MChiNZGUxqH9anfnQ4d8nO8ugIjcd4_orKP3fyPvQhqUTR4n0bqs_8zHzlxOsSenUoo3qCHISZaKQfX700r2LpPIsb2BfAzSkugbBeFfQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qmf2lfaTVE6MqNAMeuFaI1-qbXnALUsZHlCCKPOiTnO0YDboJxE2N4F_R1Ti62HEAzkQ2Kn4sjIcI7koj9vAqVDTpI4fIIRbd1xgJbYsNDA8WxRG89Fsf1QNlU_2Da89eTKgRflx6gwX3BiTwKuuq2RhryOYOsoYcmTW2xmcQXofrzy72JsLmeanhpob17KKes6jS5gBDg3tcUoc5phak5-KgnMNJ8VHenRagm1lfJKr9baA6q0PrWrFZJnFSwdiU8alWbuRbuRjtiGWsVM76lM_4xQlesEGamRGASXiRhJSAkkyj8so8JWrOdPFzxoYPnw66ZTpJP72JUzTzmjhvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hmv_HfSDSGcrzqeXtgJW9fj7X2tNvB3UXmVvQb9vkJZZvo7z5dVWW9YyiuJ9S8Vm0FEMdhBWDaJmpVM6doIgch4dbgZnma_HWr4u7APtTeTi8rX2HgWgUX9Lzyb5wFJ0t-xTCAY4ltuHd-ZOFwO1xpJRoP7LUTnUDkegv8MtHzW8BB5VYaqB0tg4kTwcxL6IGHw37csongK4sxPL1IEiBWHdsaB_i9yGJIQk9y9LyqLoUqsxUhbh600Jmq840WGZSdGNlbKVWIucjgIQyQoiLWhQb_-ALoy4OUh8ol8PT3OL_k4xTgQuq15IB9NDxqpkDrDCezmy6QfMjZUy1b4OMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور رئیس امداد و نجات هلال احمر در خبرگزاری فارس
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/467480" target="_blank">📅 15:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467479">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PySuQ7M8XJEFUIvN5aF5HieEWK5w98lwAi1Y7-WfYlFrfEsMSsRNiMRQsozORuWhggiZVC8OYD6JSrFA8JFVZBusG54hrbWSS12gHxNsbE0Ognru2eA2kaip8A7Epco8etEqqHs4rtgBIVyLNqruUYzME7AJcdJe5KrDqf06aj6XVgiyror-pWlZ-sXsfp5OGR5fU-P8InzL9K926eYNfjsjoqy56cC_tZUBQrwg88NeA-FwFF1rkamp20eLZBqcPsz6EeYX1YGRXOFN0LZGY1kWL_hFQabq2UA6p_ARvcxqCokA3TsM_GPmESe6C_98XltYFj-Mzlnl7VgAhE-egg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکش دعوای بیرو و تراکتور به یک نفر دیگر خورد
🔹
ماجرای اختلافات بیرانوند و مسئولان تراکتور ظاهراً به مسائل داخل باشگاه محدود نمانده است.
🔹
شنیده‌های خبرنگار فارس حاکی از آن است که فردی که با معرفی بیرانوند در یکی از شرکت‌های تحت مالکیت محمدرضا زنوزی مشغول…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/467479" target="_blank">📅 15:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467478">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3a66UUTswg73qyFCmOf7kzOi1WHm02LTskgiaVwfZPX6CgAyVBeRG5tzI_r9g0Eh5u7eVBndQgZaGtfqEPJl8hXvrxcriHILQ7ADzdFyxys9c-JuzSYm2NNq6wXh9W6AeBG906RG5VWF1xRgWXa23CuSM_Ri5H3iiWUQgymgonBvYsufTjk586Aqd9J351wkBidSjM3PZtTYrBqQ544LbUNkmSwAWSZCV-cThkylOJHO701UPfoD9V6G5vxiNRIjFPkxn1a90KGC5Fm--wFBY4CmwVqytFVQ1gKqHzvUkkCTL3pzHNoNfLyQxnhWWLejiTgx6porSpXE9KqH8UH5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ قالیباف: شهیده نصرت افتخاری در دورافتاده‌ترین نقاط سیستان‌وبلوچستان، پیگیر مشکلات و گره‌گشایی از زندگی مردم بود
🔹
شهادت مظلومانه و ناجوانمردانۀ معاون فرهنگی و اجتماعی فرماندهی انتظامی سیستان‌وبلوچستان، در مسیر خدمت به مردم، ضایعه‌ای تلخ و تأثرانگیز است.…</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/467478" target="_blank">📅 15:42 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467477">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812e55ee69.mp4?token=Zo1Rk1_08S8bwxKd9M35B5bgaCBRHoH_33c09YUJx-dMjLd02k1ngARrBnvBwHY3rhHnPIXtXbyp4QQqcYwVbg2NgvCzUY1Emnu8p09zglTsdHMN_mgj4EXpYgyOtPAHbPawx5Al4bag7mMypu6W1FIbq7lxmVUv6xnpiiQylT3fCR2z2buG_tPCYHVeZQjGUjXnhHhu4EFqsDOosc1jjgWrPSHac97QsoMQ5R-l-lonqjLYIOadzUuWOn_mOiUHpUl4cy5WjOniVvoZ2DufGjoT5dTL0FCwz0N9Vhjk46UL48-AeibH_xK5mkdcmCCvvwE9yayqRVHLl8t73y2m_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812e55ee69.mp4?token=Zo1Rk1_08S8bwxKd9M35B5bgaCBRHoH_33c09YUJx-dMjLd02k1ngARrBnvBwHY3rhHnPIXtXbyp4QQqcYwVbg2NgvCzUY1Emnu8p09zglTsdHMN_mgj4EXpYgyOtPAHbPawx5Al4bag7mMypu6W1FIbq7lxmVUv6xnpiiQylT3fCR2z2buG_tPCYHVeZQjGUjXnhHhu4EFqsDOosc1jjgWrPSHac97QsoMQ5R-l-lonqjLYIOadzUuWOn_mOiUHpUl4cy5WjOniVvoZ2DufGjoT5dTL0FCwz0N9Vhjk46UL48-AeibH_xK5mkdcmCCvvwE9yayqRVHLl8t73y2m_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان ستارخان تهران به بزرگراه شهید چمران متصل شد
🔹
پل دسترسی خیابان ستارخان به بزرگراه شهید چمران با حضور شهردار تهران و رئیس شورای شهر افتتاح شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/467477" target="_blank">📅 15:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467476">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORqkvGdtSp55qOV_QCjAYPYk6vx7lVo-quesY8RbbmW744t60jNvtOYa0hdjeXA8_vYRNq4HD5WEuvxuHOir18qzP4x0R7Zgydc5HSmwftxw-a0GgkcNvjk8EfQlPh2SUzTzhpalS289xRRotFwXcP4_xronvOzkY718LZqsaCMl7dGjxVRrsQCX71rYRTa2gFQ9P0OIVELmbGcLhStAYWudM3Ljj3FrjpCPCc0-ITmdKOhnJD1gtrLyAC8ESr4cA9ueyLAQXw8Pwgnx2MRVOFhKTDiV4n9LAHDcIadbikucU-UlNSMAaT8c7LJTvVEFGXaiPF_yx7HHt7PIM3FRfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ واردات ۳۰۰ هزار تن گازوئیل از روسیه، مصرف نیم‌روز آمریکا را کفاف می‌دهد
🔹
برآوردها نشان می‌دهد ۳۰۰ هزار تن گازوئیل معادل حدود ۲.۱۷ میلیون بشکه است.
🔹
با در نظر گرفتن مصرف روزانه حدود ۳.۹ میلیون بشکه فرآورده‌های میان‌تقطیر در آمریکا، این حجم معادل تقریباً…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/467476" target="_blank">📅 15:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467475">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iT4IrNErztWn9DTbiDmz0ZxC3qLcGUKdJ1LhcG3oA-KUcttPLZdkR7Q3MKmNSQ_oxTfpoLcpXL7fE2N4hcyTRqd4rmcJiBjOt-mMLUfeJ88wj5XvpiUfHUJLRFWMVrmhwnur4QP-GvRIKH9D14LUDYkEBkfpVNOgHYdKuxAu-raEd68Cs4gpUdWxlroGbEPVhmPODUhx55OZ_wNYqeS5hgioxpRco1XX24yF8m1EM4x46xrc5l5rp99oOm2xj2J3vGNSvHOraw9o89u8-Y2OOdhRM16tqA-M9WgUw5o_pQ61QQ0JiOUYXujeVwRIGtIa_5byY_pz1S2_e7PcOlZmHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاهان خطیبی را به خط پایان رساند
⚽️
با اعلام باشگاه فجرسپاسی، در پی کسب نتایج ضعیف و شکست ۶ بر ۱ برابر سپاهان، رسول خطیبی از هدایت این تیم کنار گذاشته شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/467475" target="_blank">📅 15:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467474">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLl4HvOFlOxzXGmdFhdik9jP-w3bpD1trLEmXWG5jxYJ22BFB88RClIN8K5o1Yy1nf0Khwq0k5G4VDQgA6dx9hymMD_Ud6172TUAu3DXvGfbMR6Ut6AUmhhSAe7HxncjcmI29knARt1fFORPkawS85P6LCQDEpVZhie-elkfIwk7G3s_EI8SNyUmiVBAuMxRWXbiDs1-0jO2LfeHhKWFl_IcK6rej3SSkrf8pPSqKW7u0TVqkQ2rIttf4HbhPlc2XdNFHwJQ_28n3F6JBisFncgQcNNiCIHwMBRlOSS_mST64gq8PUCzjPkmg133sKNHDfyEc-oXLJO-OVMLSh9aeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویای نفت ۵۰ دلاری بر باد رفت
🔹
رئیس اتاق مشترک ایران و چین: سال گذشته، کارشناسان قیمت نفت در سال ۲۰۲۶ را کمتر از ۵۰ دلار پیش‌بینی می‌کردند؛ اما حالا هزینۀ حمل هر بشکه نفت از خلیج فارس به ۴۱ دلار رسیده است.
🔹
گلدمن ساکس، سومین بانک بزرگ آمریکا، نیز پیش‌بینی کرده بود در صورت نبود اختلال جدی در عرضه، قیمت نفت برنت در سال ۲۰۲۶ به محدودۀ ۵۰ دلار کاهش یابد.
🔹
با این حال قیمت نفت برنت در پایان معاملات جمعه به ۱۰۴ دلار رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/467474" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467472">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKf9NM99PkVk-1PGo9NYjFhFwtnGDKVHqSLdsJP0aeBZfQglcSXWmQwBRphzK-zclQI0q5689azANYCVl0nrToR8ZNxBrWLcNoOLIEMid2-EqFEqKE9tnDAnxuWZVkEslUA0UGeS0F6KnRXtt5uD80fHhcCE3P47MCTF-KcE8alAQzE81wbVtd5d-39isF0Xb6EHsyH4hQ9KAP3cxhnmPBfsQM6KvcD3OLv4HXot0L-gcwcPOvqV_QNYEWi4buOy_K7mBV3MI00KGvfwQQlaajL8oPDaeO8ImkLwuMho_4A4vMTy_zvfZ8netf81GxAyaqVNO1-aQKSmGClr9QIwwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایتی از «آن روزها» که سفیران دولت‌های مستکبر برای ایران نسخه می‌نوشتند
🔹
مقایسه امروز و پیش از انقلاب در پیام رهبر انقلاب در حالی است که اسناد آمریکایی از کودتای ۲۸ مرداد تا روزهای پایانی حکومت پهلوی، از نفوذ آمریکا در تحولات سیاسی، نظامی و امنیتی ایران حکایت دارد.
🔹
این روایت فقط در اسناد خارجی نیست. حسین فردوست، از نزدیک‌ترین چهره‌ها به شاه، در خاطراتش از نفوذ آمریکایی‌ها در ارتش و همکاری برخی افسران با مستشاران نظامی آمریکا گفته است.
🔹
اسدالله علم نیز در خاطرات خود از گفت‌وگوهای مستقیم با سفیر انگلیس درباره واگذاری بحرین می‌گوید؛ روایتی که نشانگر نقش لندن در مسائل مهم منطقه‌ای ایران است.
🔹
خسرو معتضد هم درباره کاپیتولاسیون، دخالت آمریکا و ضرورت بررسی اسناد انگلیس درباره ۲۸ مرداد می‌گوید.
🔗
متن این گزارش را
اینجا
بخوانید
@Farspolitics</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/467472" target="_blank">📅 14:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467471">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6642900d47.mp4?token=ozbtmHQ0dWiZloKcTg6p03aDNLHrJV-vKVH8Pu7-aKTx5T3PAwUG-tggU9XFotBx0jFNpnO6-pjKb-mkdFevU4QkF49JaHXSnEZRqSx_miY51dYNIYVzRW-1XMniQcrGoyQVUfvbUSknsv-QrsfvQjqyGTO9UpT1AGWVYtQP2z8R1F6_Wg6dkmyGMnk4YOvo_cO_mjmKdhiOZ0Yda263LD1flOefy0trv7BhcIS8J77pznUpEoHdN-nbzP5jWR6BUttcri32z9ZQmYoGzLQx2mBtycsZIdLWgQsI4OJgXnshmbcCHj48hPj-e7AWXFex4O767q5Sgjnx-L6dsZrFbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6642900d47.mp4?token=ozbtmHQ0dWiZloKcTg6p03aDNLHrJV-vKVH8Pu7-aKTx5T3PAwUG-tggU9XFotBx0jFNpnO6-pjKb-mkdFevU4QkF49JaHXSnEZRqSx_miY51dYNIYVzRW-1XMniQcrGoyQVUfvbUSknsv-QrsfvQjqyGTO9UpT1AGWVYtQP2z8R1F6_Wg6dkmyGMnk4YOvo_cO_mjmKdhiOZ0Yda263LD1flOefy0trv7BhcIS8J77pznUpEoHdN-nbzP5jWR6BUttcri32z9ZQmYoGzLQx2mBtycsZIdLWgQsI4OJgXnshmbcCHj48hPj-e7AWXFex4O767q5Sgjnx-L6dsZrFbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲ هزار عنوان کتاب برای فهم رسانه و جهان پیچیده امروز
🔹
مرکز جامع کتب رسانه انتشارات فارس با گردآوری نزدیک به ۲ هزار عنوان کتاب از حدود ۷۰ ناشر، مجموعه‌ای تخصصی برای علاقه‌مندان به رسانه و تحولات فکری و فناوری فراهم کرده است.
موضوعات این مجموعه:
🔹
آموزش رسانه و جریان‌شناسی
🔹
علوم شناختی و هوش مصنوعی
🔹
حکمرانی نوین و آینده‌پژوهی
🔹
علاقه‌مندان می‌توانند برای بازدید و خرید کتاب به فروشگاه این مرکز در خیابان انقلاب مراجعه کنند.
🖼
برای آشنایی با تازه‌های نشر و معرفی کتاب‌ها، ما را دنبال کنید:
بله
|
ایتا
|
تلگرام
|
اینستاگرام
سفارش کتاب:
عنوان کتاب موردنظر را به شماره ۵۰۰۰۱۶۷۶ پیامک کنید یا با شماره‌های زیر تماس بگیرید:
۰۲۱۶۶۹۷۳۹۹۶
۰۲۱۶۶۹۷۳۹۷۴
🔗
مشاهده کتاب‌ها در مرکز جامع کتب رسانه
@Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/467471" target="_blank">📅 14:56 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
