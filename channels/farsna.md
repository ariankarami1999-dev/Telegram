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
<img src="https://cdn4.telesco.pe/file/KSisxuQEB-UYgrSishDZdc30S7ysmSCzbss_C6hvjfeykzK2pJxtp5cScts1_z82RtaXAyeceNCD89Bg29rdjCh6fhb86Q8qZCIoGkKVOJVhfCg4DdQug0va-uw2hYi3P07AY6sGY6R-9y3O-hylduHPI9K5pRj0RFu10hmB9jKoAKDd2t310QrE0CLvE8WLBDm66-7bfTeM7ASYlAcL-OqNE4nwwiQYs1hY6y6bzxQs3bAgmK-XuashUbH6Bl55Jitv84yhHvdOdgE_Zh7HPu7dPkMkzKmUwDAO_W3eFmifuknKopYhNa7-Mlcnz-q6zNvxwado6TTuItgJMV4vKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 00:30:37</div>
<hr>

<div class="tg-post" id="msg-448852">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/361a464c64.mp4?token=EBhMHrZAQIKztoAh0VS5OmxSscDJoW7qAfMAXw6Da1KN5Vnl2WMwzq8OM7oonbJCMhKLsNko9on99Yk5BwHkaUhOmfySRXDCfwz5E8SUdkuOiuR4OkEvjox9yxI2AMW96_APhW0aSQoMawBQfQVYI4Q7cTEmf7rP8jgk46-lFVg3qwId9ZrHxKKdBEcpzNjyjDp-EGaY2PKLOh7WpDXU35afed1Wob7d-KVv7IfixJpY_L-NbRb1iLFK45Mu0_wKJC08Qb2vJvBf85IDWoC893brG5lvgmtv6LoKswsYcsGS_jr9PbGupupmaQ-RJNqC1Oi0Z34tc8PkEtNLR9DiclXEPx91vTyI-75z6GZTJcnW1Aq8KxkqB0xXjo0BR8WM-QOzGCzeFugZpf1ggCDRNrBRHlNKuWeuKAsGkSxoeK7WybhTVRcunZqbWt8-c94Ul8_YDhJRZmpWWNZ1NGEzmhivYpayl2FHK98S_WBzg7QIYUje5di7TUkNxrcvrIun1zBFX5suoJ3iBAlPS7PD7c9e1srP3MLKv8cVWP5AZxaRmO6kML4VOldSRhjJlI2CeEyGg0K4Mxn-3znci4RwS3XtAin5bKKLGrBzELjTgg9ElapZEh72fTmGTurq-7GtjX8r5p7zhzLoAowdWMUpLfZ3BjEDUtGzPhFfeOeuzfE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/361a464c64.mp4?token=EBhMHrZAQIKztoAh0VS5OmxSscDJoW7qAfMAXw6Da1KN5Vnl2WMwzq8OM7oonbJCMhKLsNko9on99Yk5BwHkaUhOmfySRXDCfwz5E8SUdkuOiuR4OkEvjox9yxI2AMW96_APhW0aSQoMawBQfQVYI4Q7cTEmf7rP8jgk46-lFVg3qwId9ZrHxKKdBEcpzNjyjDp-EGaY2PKLOh7WpDXU35afed1Wob7d-KVv7IfixJpY_L-NbRb1iLFK45Mu0_wKJC08Qb2vJvBf85IDWoC893brG5lvgmtv6LoKswsYcsGS_jr9PbGupupmaQ-RJNqC1Oi0Z34tc8PkEtNLR9DiclXEPx91vTyI-75z6GZTJcnW1Aq8KxkqB0xXjo0BR8WM-QOzGCzeFugZpf1ggCDRNrBRHlNKuWeuKAsGkSxoeK7WybhTVRcunZqbWt8-c94Ul8_YDhJRZmpWWNZ1NGEzmhivYpayl2FHK98S_WBzg7QIYUje5di7TUkNxrcvrIun1zBFX5suoJ3iBAlPS7PD7c9e1srP3MLKv8cVWP5AZxaRmO6kML4VOldSRhjJlI2CeEyGg0K4Mxn-3znci4RwS3XtAin5bKKLGrBzELjTgg9ElapZEh72fTmGTurq-7GtjX8r5p7zhzLoAowdWMUpLfZ3BjEDUtGzPhFfeOeuzfE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید، زائر امام رضا(ع) شد  @Farsna</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/farsna/448852" target="_blank">📅 00:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448845">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VHsiT_a-qqXUfD3230Bb6ggTj7BQh9xTB34RGqj_JJ8T1AnO3d1UZ71FAXtybjvtJBUiB2oV9XVAwBhSgd9AuBeiyX7MWNKsPTwtz4pk4_QibJvn5RB_bbvW0-VoUURilTVsTC5ap55MdZnq-4opCSNGNO05gyXNZsEGXaniLUrIzLgY1cbW4gg1W8PKHWvgG6ZxULtqoue2Gmr8yK2RvD7kmu-PaNf8xPy1jQsElUgxD78pqo6ZEjwKiLuxeu13F_lOZt-TttKB1W9i2T40fHmjoKOzN0VX0C6i22Wb4nKoH-S61yWDLdOxlSrKi2Je7VDdrC8c8gbWWDIPSR-cFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W2bK7zIY9vbqiuowGbG6KMNfOvnlI7mftuQVYL2LwPfMVMzYnBaSxOKvuPKIEkLgatu7pCuXuv_txcOaLMljQphcr9Go9FtZ8zM1Vsq-wZQi4fi7em30OyW0fhF-ROkQeraliLxu3BYpcVOToYTZxvztSzen2tuS5toAEab3CE8QhVZMRhHdSM95OpXb64ykB6qPzNbGkbFRrCWBYKNECl9SGzUGNCm2AxxUUvdRp0zCV7Ibo_dNEBTlsIH8gLdFFql27Gd2W-nMJBgE8BH7CdaEz16ocxZtbV4bnHaRYfFwzPW_NQc7_2_LyAU0tN8UVwfT43Ak0Q3GDo9IKTxsJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VM_8bO-3Pq6PNNJ725EjwXEdo36-i7WK8G_6lEp9KXSUHZG3WPSKGwAsAAHD3-cyKiIj_W70qQ2D1D_CA5LyLNT-g4go3INiUPre_GDZHrXEC5rSEDnkptK8BT8vyCIbrRkEDZyeHMjaDJbGGmaeo3dItjD6G2yxVOJ3PvAqV_xp8Wdt6llpcuMB1uXLvSfYHhnczxp5HLiFYPpxlLtmHzZWSgb9MR4DIu243oag8qD7gAumFO0U4E8rcX9SQCKuiH7gGmT99WM4pqJ16HDlthVcMm8X31ela5VaTAvCygu-SIF9z-qtXttzi0pi8ib34qql7l5MNeeftjakbbGacw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TRVEAKs_afx3PTibk9X-tDcl6en28_XJSzDkXI_bAPjCWYXYO4VCgPIPJAI4e48So4iYoSmwwHyODix7ik21nDGaGilfGkBRAepFQ97vQCciPjdbJwrDyQNt8DzSCE_TC2tllVg2BfMle2j6RgDQe2NPmFVVItCEZLs0SHm0lRt52cO4FrWuHCDJnG6RC3f1p_twvf8EGQFAdva3ZiqkFAjklQI-SbQENu1Y9SXhgB7QkKZhXAlWrrpkB4FexVISFhEvcPAb2THWAZGLKofbvHHwk95HRx5vhDlVMHwz6udimoMXUQrcwi-IzGf4Glkbi7EFVPswHT549yPPXL2eJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I2rOCr_wlcU9MUpihQD9YOUZFYSM-tIhBqgfRMFT-2FA_9e53fi91K0gqiN9w2rjrJBSUNNciK4X8MaGa3S6LuVfKPWBfT-UTKpmw0QrYZBNGyVGoeJcDSIYshxQQ2fMiWN--0Gax_H_8_-LQNniibcq6H7K_bB3X6OUuXqKv-KFeuTcPS3kWJ0OQbRtb2ELXxWZW4h59uwaELb7xCF2l737HWAG_15Bz-NoSMu46E6L_2i2bL2XqeXI7enb3Xw4pMWi4IjCGT45YRNa1FeAgjaZA7iO4zYQHGNAAMN0EKA_2QHlHRhgZwvzop-SacNA77h0icdUD_55ft1Y3Tle1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NC05k7rgWoNg5VE_xXsEuzKCE9GRpf1o-_EXmni-W17frcqOOUVxi-sBbL2yWz2W6sdsI1RUi4RyZG3OzgUPi8epifbTtRrvwd5Y6uuSLOv2ugSUiMdCj6YHImy1kxQx3qUusC2VD0idkA5Pbh2CuYQm-YIGj-L_wGCtfKf2QjaCU_kUGUjGk1-kwrweDc64VVsLNruqVRWEIk0O1YSYIk-tS9uYF6knk2gQIcxrM35aOwI9KyX6Jnmboeqcs56t-_QIuhUBnu2TbVL-MlhUc2LQcsrXebRZAF5GbuKJa9z8N2NDaKoAX66MyIbKDTfJelHeyUqAHgyVqI3vbxZK3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rOtqEaHUi9BIsobCw7G6VlQWF_43FKwn2IycRLS0DEvC-INZJYcyLVz0R2zrJBpAubnGatoVb2iFJFdztwgTE3J3BqONy5lmRgcTnNvUaZAC4d_2Q3vE6p5G0e2-LRWhJb-tRz8RTjBVB2tvixmgIIO2U8TczfYtgoSkgNjd2xswniP7b4Hgq3bjvBGFevah-1s1cMEndnDEjt6ZoTcVrBbN-yFqbXRJP8pM51St1wRAOPYgjHtScsJ-9H39OAidRUrHYvdySD22EP1XD3oPH3lsdLQ1-uAxxBf4ouuprYsFAqdqaVt5lCTwP7-ZHVhSnHvbON460kmACtfgINZnLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر یار بر دستان عاشقان
عکس:
زینب شعبانپور
@Farsna</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/448845" target="_blank">📅 00:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448844">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2684c94630.mp4?token=WFmv7Ii_WlCKoresWsq_gmZQjMBOmYoeas6PZJ8gubcoV8kr4c2sAw5G_GdDq5OsUNlHb5GwU075x6BNNlk34zB4iNlP9Mnk1gmJouP1rWLYErj28TZlPPWKaBwTT5LvmgyCjGYwpUnuj2lU198tRPgYjt3URxhdXBispYgBK7MO1GENtxsb79Moy4WwKMYAaUgW7Kxx09tGS1_b6jyACwHnQIjthbvFmg-qw0CH0AFLDhKRX60Z9SWW3JGAh32iuxmpBroNbNn5QjN3fmHbG8rfpqlPcyuM-Q9JGzIT3avbWCyfZCPMKg35dLHKHcFiE-Ae2REczhWI831i9AX2Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2684c94630.mp4?token=WFmv7Ii_WlCKoresWsq_gmZQjMBOmYoeas6PZJ8gubcoV8kr4c2sAw5G_GdDq5OsUNlHb5GwU075x6BNNlk34zB4iNlP9Mnk1gmJouP1rWLYErj28TZlPPWKaBwTT5LvmgyCjGYwpUnuj2lU198tRPgYjt3URxhdXBispYgBK7MO1GENtxsb79Moy4WwKMYAaUgW7Kxx09tGS1_b6jyACwHnQIjthbvFmg-qw0CH0AFLDhKRX60Z9SWW3JGAh32iuxmpBroNbNn5QjN3fmHbG8rfpqlPcyuM-Q9JGzIT3avbWCyfZCPMKg35dLHKHcFiE-Ae2REczhWI831i9AX2Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ صداوسیما: اقامۀ نماز لیلةالدفن پس از خاکسپاری پیکر شهدا انجام خواهد شد
🔸
به محض خاکسپاری پیکر مطهر رهبر شهید ایران و شهدای خانواده ایشان، اطلاع رسانی می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/448844" target="_blank">📅 00:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448843">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/farsna/448843" target="_blank">📅 00:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448842">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
منطقۀ نظامی نیروی دریایی کنارک در ۲ مرحله هدف حملۀ دشمن قرار گرفت
🔹
فرماندار کنارک در جنوب سیستان‌وبلوچستان از وقوع ۲ انفجار در منطقۀ نظامی نیروی دریایی این شهرستان خبر داد و گفت: این منطقه شامگاه پنجشنبه در ۲ مرحله هدف حملۀ جنگنده‌های دشمن قرار گرفت.
🔹
او افزود: دستگاه‌های مسئول، نیروهای امدادی و نیروهای امنیتی بلافاصله در محل حادثه حاضر شدند و بررسی ابعاد و جزئیات این حمله در دستورکار قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/farsna/448842" target="_blank">📅 00:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448841">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxzxTC6Cbw8LL1SWU40kVY8Co8Lqw7tHdGvFJvDUkgdECzq84CJeoPTIrl_NE4x5qR08LGP-nC0JqITcPfFwHUA9EYbui_dyJa_O0Z_9P4L6-gWGA7uSUeCNlbGewL_qIDJfbd2ny8SiQ-kv6JKf4xe1PVOOmkXQog60OjxT-iRshzTZvYQsPNy7rxPfiu_gSzYY5tcMXvdBhREU8NfCh3jpzCw52RmryMSbVR6qNinuE9UIMV8-sRO5WKxT6HSVyKnKgxu5MmO7qKkuezo3YD-2ZqreE_B5se3JHAjOkU7aLF6F0x59xNgsW3azWgn6NLsMB61Os4wE6RstWyCODw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سر انجام؛ ۶۹ سال دوری و چشم‌انتظاری، تمام شد...
@Farsna</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/448841" target="_blank">📅 00:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448840">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d641c1bb0.mp4?token=lX1sd16ofE_RIanCXGXoU5PMTvOvIzmP0u0BkdTno1ET_viO7AnzmtEwlxvhqSbaULlzXDNv_AYP15l8xdAOdjweh4aiJ-UeOtSIvKqFMa77jQrRYQGUxKi6V2BMqfS-z9WCF2KUpSqVozLG9fDos63PVqBa07oKp43RlrsyMCaEhtZQvydksgjuyO4_Yi3pD5CHvWVnrkfT2vrWkbg4rflxu5FqXGgi0n6vVcKRYZo3JsBqk1ZzTPTP74EeKydVpqUwTxEdTZFhEnzlWgPWY-OQskUMjZqmeagfuRTOhFOuXzCNK1Qu9WuT9vYkejnKsw0EbsMyU-uJegVc6dYruA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d641c1bb0.mp4?token=lX1sd16ofE_RIanCXGXoU5PMTvOvIzmP0u0BkdTno1ET_viO7AnzmtEwlxvhqSbaULlzXDNv_AYP15l8xdAOdjweh4aiJ-UeOtSIvKqFMa77jQrRYQGUxKi6V2BMqfS-z9WCF2KUpSqVozLG9fDos63PVqBa07oKp43RlrsyMCaEhtZQvydksgjuyO4_Yi3pD5CHvWVnrkfT2vrWkbg4rflxu5FqXGgi0n6vVcKRYZo3JsBqk1ZzTPTP74EeKydVpqUwTxEdTZFhEnzlWgPWY-OQskUMjZqmeagfuRTOhFOuXzCNK1Qu9WuT9vYkejnKsw0EbsMyU-uJegVc6dYruA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری بانوان ملایری در شام غریبان رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/448840" target="_blank">📅 00:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448838">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hin-d6j3GNt1StWJnFGDTIfG6ktux4nTky9ndeedlv7GpRnZCSuaaB0Hupv2k23KnZtFozXN5u6gE3ydmk3hUOU1xsyqF6eGfau4cjMPQnbdjeN9pnDvOl8PAq6GFIrw2qCYoOzjQK8Gi8co-YqXZLkyCZMBM5qlMQ0ZuiB7eqPoVWRpv0j63FAjp_HBi6A3d4Y2b5oIIU-E-uDOp842OtRyRWkHDPdTmKG7HZVQUJ2i_sl1sJP-FTaHlhigUu3F2wHSePAi-atpi050LcEe0ksb6hqyKn0QvMbI7heYLn65a-B-0TIQ8clGIoGb_tHx07pfA5VbykAT8XjMzI4U3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
| جمعه ۱۹ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/448838" target="_blank">📅 00:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448837">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1adb3da9e3.mp4?token=uiyAUFIpbzW5B8zUpp1pj2zAeg8M2NKFE9VJ9eQABBcJ74VAtD779HX8__ayRqUxjJZAQ0roSC8iNOZ-Ft10csrTVzRLMi9_gHBJTIpakAP-pEqALz2gFW4nNDNflXT0yz3OMNTymjQBv-qbQ4jXh5WZQhJvT6lTquqdvIX3pyqiZRssEG4RcjWW5A4f2niOj25vU2cdgIBSQdBlk9sTF1vMu96cIWHsqCf_FapHNskP9ieVCHftt07b4UyOx9oX_cVhfZCL4P2TjVIoZ_DdFga0eyHKHKLQc9rMU0FZ4xPaR-8qAoHHExkhE8hoRtu0Zze3TVajth6b-mb7V9dBGUx8Re7nZC6Y-OMS-FlNt_SR3fisTbhIh_qztrFfAA4ryF8DcvTmE04lmLO0rQuDAkzZigdLcJEdu-j0OJ-aGkZt9t5xbLEgupt9vE3Kfa7jR2at1euydSSIoZtoH7oxqdqrxVJSJzdQJuZU7tgd7wksJUcsQFjrPQcBM-2mrD20SK3bvxXfHpyo1nfwztNRPjsTruqDEMd7h2VUsVnoFEL-F8ablIERxXVnXNZM6d6_xMT3C-nkKpvaKRxZsuy6q90aVuySF8osk-nQtSIVwG3TGGKYzqJnFseyN9dthk_4FK0C3seAt_oDjktF35GL4wqINBNY4893NcSDpAFRJek" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1adb3da9e3.mp4?token=uiyAUFIpbzW5B8zUpp1pj2zAeg8M2NKFE9VJ9eQABBcJ74VAtD779HX8__ayRqUxjJZAQ0roSC8iNOZ-Ft10csrTVzRLMi9_gHBJTIpakAP-pEqALz2gFW4nNDNflXT0yz3OMNTymjQBv-qbQ4jXh5WZQhJvT6lTquqdvIX3pyqiZRssEG4RcjWW5A4f2niOj25vU2cdgIBSQdBlk9sTF1vMu96cIWHsqCf_FapHNskP9ieVCHftt07b4UyOx9oX_cVhfZCL4P2TjVIoZ_DdFga0eyHKHKLQc9rMU0FZ4xPaR-8qAoHHExkhE8hoRtu0Zze3TVajth6b-mb7V9dBGUx8Re7nZC6Y-OMS-FlNt_SR3fisTbhIh_qztrFfAA4ryF8DcvTmE04lmLO0rQuDAkzZigdLcJEdu-j0OJ-aGkZt9t5xbLEgupt9vE3Kfa7jR2at1euydSSIoZtoH7oxqdqrxVJSJzdQJuZU7tgd7wksJUcsQFjrPQcBM-2mrD20SK3bvxXfHpyo1nfwztNRPjsTruqDEMd7h2VUsVnoFEL-F8ablIERxXVnXNZM6d6_xMT3C-nkKpvaKRxZsuy6q90aVuySF8osk-nQtSIVwG3TGGKYzqJnFseyN9dthk_4FK0C3seAt_oDjktF35GL4wqINBNY4893NcSDpAFRJek" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیرزنی که خیابان را به شوق رهبر شهید به هم ریخت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/448837" target="_blank">📅 23:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448836">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3dee3d178.mp4?token=onOp5bCv3CEid5QVk42gH4ZzvvCe1JcqSjhilpyvzOf9ay0VEqNUtFRNE-cvFzaCnZpgHDkOLl_IBAbDW0cty-z7tkgFPkNKT79bP9Puo0TwqjOf445w0X-52MYLUznBz02g64Acvn30FTIFtAlKeNO8y75gj8DY9DvOyJe0fObukjUDcSxE-g6S0Fr7PtmviQZWxegqyBhmaPMnuv6J0zYeLiIVQYR87wee6MCa_HgysB-f-4smCU3G40DkMeFfp8kRGCV3WR16i5AlKe_IESLKo62KuME7yVatPlx9SlBnLEsZSgoSjesG738oymbnVK2GoCQlcpnZyHN4CWKyfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3dee3d178.mp4?token=onOp5bCv3CEid5QVk42gH4ZzvvCe1JcqSjhilpyvzOf9ay0VEqNUtFRNE-cvFzaCnZpgHDkOLl_IBAbDW0cty-z7tkgFPkNKT79bP9Puo0TwqjOf445w0X-52MYLUznBz02g64Acvn30FTIFtAlKeNO8y75gj8DY9DvOyJe0fObukjUDcSxE-g6S0Fr7PtmviQZWxegqyBhmaPMnuv6J0zYeLiIVQYR87wee6MCa_HgysB-f-4smCU3G40DkMeFfp8kRGCV3WR16i5AlKe_IESLKo62KuME7yVatPlx9SlBnLEsZSgoSjesG738oymbnVK2GoCQlcpnZyHN4CWKyfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تا دقایقی دیگر خانواده با آقای شهید ایران وداع می‌کنند
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/448836" target="_blank">📅 23:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448835">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‌ صداوسیما: اقامۀ نماز لیلةالدفن پس از خاکسپاری پیکر شهدا انجام خواهد شد
🔸
به محض خاکسپاری پیکر مطهر رهبر شهید ایران و شهدای خانواده ایشان، اطلاع رسانی می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/448835" target="_blank">📅 23:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448834">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f506e92eca.mp4?token=PBRFZfZbm4qp9HA5EXihbs-ag8n6JKJVX0hvvseqAZNBUqrnCMtE8Rr-WdypYeD_nyY_6E4ypnqjIGGNk7N-InkTmBKr4dTUmy0YJjy-cSktNiAPfhXLr-D0aQUU7x_tAB8sbVPt5tl3X4dz907rVXUq0THuaRVUT0yGl2_pk2smpp7RfZvz4WFh2bWg4Pi_Jer3vfVMCWj5pacaqH3Y0zL2ppxekifhgaRmxr0IwVgzbVY_R_zkxxKIEQKf4MXA2h24hWcfnBiHE7m9i8boa7gMyZ6VfxxubkWOcPruwV7HAHAGdaHdjNORBvBIxeITeg82W7mlOoPdIkYJQb0YQ6RmIZlu0CMcAne_lQlSv8q9tNzOPhGhHPrKtCz1q0ztfpqtqNKOhA-BBKiJ9_gqRren_FeYO6LDkPWg2UV4mLuuCjW4A1gRamEInnE-AAYIrYlVyjbGkk9_3OuzRI7_LOAFtNIqTuvr5ZsRZlelvuVbtyQ53KufjSRN9-ovZmwBY7fQ-DYof-G3GhKczh0T8U5kmaW76p2Dtw7r9e4cnOqy6Msdz7rDRs_BMK3w7oubKLse7bGsceAoPCy9YHGfS3_bUDYHDoiExA8fIiooEXKSkBcRnhrHBjrojLJbL_EU1L-_UPRwGlfgaFqJ6aDT8hBEMD5qUPHmiXvYRQwjHJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f506e92eca.mp4?token=PBRFZfZbm4qp9HA5EXihbs-ag8n6JKJVX0hvvseqAZNBUqrnCMtE8Rr-WdypYeD_nyY_6E4ypnqjIGGNk7N-InkTmBKr4dTUmy0YJjy-cSktNiAPfhXLr-D0aQUU7x_tAB8sbVPt5tl3X4dz907rVXUq0THuaRVUT0yGl2_pk2smpp7RfZvz4WFh2bWg4Pi_Jer3vfVMCWj5pacaqH3Y0zL2ppxekifhgaRmxr0IwVgzbVY_R_zkxxKIEQKf4MXA2h24hWcfnBiHE7m9i8boa7gMyZ6VfxxubkWOcPruwV7HAHAGdaHdjNORBvBIxeITeg82W7mlOoPdIkYJQb0YQ6RmIZlu0CMcAne_lQlSv8q9tNzOPhGhHPrKtCz1q0ztfpqtqNKOhA-BBKiJ9_gqRren_FeYO6LDkPWg2UV4mLuuCjW4A1gRamEInnE-AAYIrYlVyjbGkk9_3OuzRI7_LOAFtNIqTuvr5ZsRZlelvuVbtyQ53KufjSRN9-ovZmwBY7fQ-DYof-G3GhKczh0T8U5kmaW76p2Dtw7r9e4cnOqy6Msdz7rDRs_BMK3w7oubKLse7bGsceAoPCy9YHGfS3_bUDYHDoiExA8fIiooEXKSkBcRnhrHBjrojLJbL_EU1L-_UPRwGlfgaFqJ6aDT8hBEMD5qUPHmiXvYRQwjHJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ را بکشید، ۱۰۰ میلیون‌‌دلار جایزه بگیرید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/448834" target="_blank">📅 23:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448833">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ece8888e51.mp4?token=s1rh9khLJFu29-ebR68F-PPMKqSXN9Hv6BSNNhkHaXuiw_6C-T5TbTY0TkZcxM0kEdRuGBvgCE9EQSWNeL_j9BNPVhoV0zOhLntgxQx71UAi7bF64tPxLZmbiLHt4badl4Dvg4fxpJYjZ3yV-FvZ9zev4h6EMJu8h3m5U2trhyql8iJp1bL2S1XiMwlbomoD55YFywAZ6FEA4rVKl8mhThBvIurbep4TuAmlX_XtHJc3GtTPvVPsnrYu3Bs2KL0huiJbvoGEyo2WUnhgA5hLMWSwZAEJaJ2zRf7XjKFcjw2SDQtEksdG_6OU0wRvqIfu7zyV0WF3iZoimoURDG-sUT3BE5OlQ-Nu6wFxqZ8eX5_FP7rYrptKPNWaUGFbkv1Cz9wnbaWwGNV0zNfGw-KquDDGu7oR7O0eFrCmEacaR6r848rZrOTuHKpbzpAXTgDmTxAfTdXppO8nmuTcWHVJzYmAMwQCbtNDnBbJLmL7LzmEJ5QFbSbiXgYLCAbsrXHMD3Mc1Ocrl02ng0m5n9mV82jbDgbVnXpjl0qXMsCtP1d4pqRsWlmeKS4OW3cHJX2H1efTk3nxhPemg7ulRMrSxCEIpBt8kdmBt-ErXzkABWUOMHAHtoKuhCi82RcNUQk7Be5GKPaVVwpDG_ykkXx8lsL1B4dcrEOnMzw2NIt0R4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ece8888e51.mp4?token=s1rh9khLJFu29-ebR68F-PPMKqSXN9Hv6BSNNhkHaXuiw_6C-T5TbTY0TkZcxM0kEdRuGBvgCE9EQSWNeL_j9BNPVhoV0zOhLntgxQx71UAi7bF64tPxLZmbiLHt4badl4Dvg4fxpJYjZ3yV-FvZ9zev4h6EMJu8h3m5U2trhyql8iJp1bL2S1XiMwlbomoD55YFywAZ6FEA4rVKl8mhThBvIurbep4TuAmlX_XtHJc3GtTPvVPsnrYu3Bs2KL0huiJbvoGEyo2WUnhgA5hLMWSwZAEJaJ2zRf7XjKFcjw2SDQtEksdG_6OU0wRvqIfu7zyV0WF3iZoimoURDG-sUT3BE5OlQ-Nu6wFxqZ8eX5_FP7rYrptKPNWaUGFbkv1Cz9wnbaWwGNV0zNfGw-KquDDGu7oR7O0eFrCmEacaR6r848rZrOTuHKpbzpAXTgDmTxAfTdXppO8nmuTcWHVJzYmAMwQCbtNDnBbJLmL7LzmEJ5QFbSbiXgYLCAbsrXHMD3Mc1Ocrl02ng0m5n9mV82jbDgbVnXpjl0qXMsCtP1d4pqRsWlmeKS4OW3cHJX2H1efTk3nxhPemg7ulRMrSxCEIpBt8kdmBt-ErXzkABWUOMHAHtoKuhCi82RcNUQk7Be5GKPaVVwpDG_ykkXx8lsL1B4dcrEOnMzw2NIt0R4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراسم تشییع شهدای ارتش در بندرعباس
🔸
۳ شهید ارتش در حملهٔ ۲ شب پیش آمریکای کودک کش، بر روی دستان مردم بندرعباس تا گلزار شهدا تشییع شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/448833" target="_blank">📅 23:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448831">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">امشب برای آقای شهیدمان نماز لیلةالدفن بخوانیم
🔹
روش خواندن نماز لیلة‌الدفن به این صورت است که در رکعت اول سوره حمد و آية‌الکرسی و در رکعت دوم سوره حمد و ده مرتبه سوره قدر می‌خواند و بعد از نماز می‌گويد:
🔹
«اَللّهُمَّ صَلِّ عَلی مُحَمَّدٍ وَ آلِ مُحَمَّدٍ وَ…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/448831" target="_blank">📅 23:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448830">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45e7cdb87a.mp4?token=Lxwmd5VhAo2JYglQvUim2lUhC5ZSf3Brn52A1f7t1c83aOQjaRrZvyHeSbAdlgX14h8s48xR4HFjR1F8dNGPIdCJJ00m1MIXqImoueoLUyMDD9GpuOCg0x7ncceVGZ1GLYc0s16zue_dgKUEHQDKZCYqD889-86buzaxF91Vw91f3IRGjYfDlHxzthTNhgmptCFMs1NttWhqucLqn61Ie5x0YGT300uiWrfwl6hXps08SNPnoNd8ME85Lwie-isZNJ1EU8f5xAHMcF57cWvKNwb3E-kpLoeS-ObhkH2caQ7UAgVOzN7JU5vPdXHJwJagIir4NFC5Jy8_2HGUP-6eVDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45e7cdb87a.mp4?token=Lxwmd5VhAo2JYglQvUim2lUhC5ZSf3Brn52A1f7t1c83aOQjaRrZvyHeSbAdlgX14h8s48xR4HFjR1F8dNGPIdCJJ00m1MIXqImoueoLUyMDD9GpuOCg0x7ncceVGZ1GLYc0s16zue_dgKUEHQDKZCYqD889-86buzaxF91Vw91f3IRGjYfDlHxzthTNhgmptCFMs1NttWhqucLqn61Ie5x0YGT300uiWrfwl6hXps08SNPnoNd8ME85Lwie-isZNJ1EU8f5xAHMcF57cWvKNwb3E-kpLoeS-ObhkH2caQ7UAgVOzN7JU5vPdXHJwJagIir4NFC5Jy8_2HGUP-6eVDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از انتظار خراسان برای متفاوت‌ترین بدرقه‌ٔ تاریخ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/448830" target="_blank">📅 23:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448829">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdY5SkkVhgoL-j3MxAvyTIzcanRBm4dRtIGnx4iJLXgLhMv6F4lTLAdKp-BI3EdYOQN07uLrdRP-CFe3WZI6XQ9A3GnCF4x4oUUwTjxTBdNaTv3nTYTxu_L1IGtoqImpMSJ5uNgkT-8wRPN03wBDGhOvDNkJ9XNoKqqsCdqp8_rIWgpnRt4R1-bs2UhBOCgLmMdJqkpyvSPA7hW8wWXojV1Zu7Tdbs92BgczUALzvI3SezIN3ylEVhqWIO81KPELiu5d7E2dHMfOUKoDVjY9zoKVzkobGecZSDt6SAxwzXt6cr1mG_Ipjb2Ic2Nm_I6aJC5IsmmdKGSjxR5e81rLBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
شهید خامنه‌ای در آغوش امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/448829" target="_blank">📅 23:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448828">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-57WriDZim_mvr5T1RCQdmrv20-1DvdXL0_rec7-EZZO1sU8BXfy9hMJ97zRIKqUcsSiAYBgs0rc6SPK1_EaNSHhmMtCm-yPlNR2SbTHhdcz7_ktlvqleWEDKVA4z1o_Y-CP4p8IyH7G3P-OnpGKczndlCbaZzgp0BBuH7pV1VLjvhLQElSAwK5Hfdy7HEHBnxKS_yqr_gWGiJs7vKBD41RE_QnSdK9qBOPO471JMls7wZi5V2XoJDltGXvB8jo44JHcEmZeUY6iGCN0d-2S7J5fK3ni3uJR6J3zRQp_e916t27d_w_8xBMBCQcStPTmYbInh0Dw7uva68xDjb76Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین برآوردها از میزان شرکت کنندگان در بزرگترین تشییع تاریخ جهان
🔹
مراسم وداع و تشییع پیکر رهبر شهید انقلاب، در یک بازه ۶ ‌روزه و در ۵ شهر تهران، قم، نجف، کربلا و مشهد برگزار شد که با حضور حماسی و کم‌نظیر مردم، به بزرگترین رویداد تشییعی در تاریخ جهان تبدیل شد. این مراسم در تهران سه روز (دو روز وداع در مصلای بزرگ تهران و یک روز تشییع اصلی) و در قم، نجف_کربلا و مشهد هر کدام یک روز ادامه داشت که با احتساب تکرار حضور افراد در شهرهای مختلف، جمعیتی کم‌سابقه را گرد هم آورد.
🔹
منابع رسمی جمعیت حدود ۴۱ تا ۴۳ میلیون نفر را برای مجموع شرکت‌کنندگان تأیید می‌کنند. این عدد از تلفیق چند منبع میدانی و رسمی به دست آمده است: میزان آمار تردد با وسایل حمل و نقل عمومی به محل مراسم، تعداد گوشی‌های تلفن همراه فعال در مصلی و خیابان محل تشییع، میانگین حضور هر نفر به مدت دو ساعت و نیم در ساعات برگزاری مراسم، محاسبه حجم جمعیت در مسیر راهپیمایی تهران، مساحت فاصله مسجد جمکران تا حرم مطهر در قم و همچنین مسافت مسیر فرودگاه تا حرم رضوی در مشهد که همگی به عنوان پایه‌های پشتیبان آماری در محاسبه لحاظ شده است. علاوه بر این، آمار رسمی مقامات عراقی از طرف دفتر نخست‌وزیری نیز حضور حدود ۱۰ میلیون نفر را در مراسم تشییع در نجف و کربلا تأیید کرده که این داده نیز به عنوان یکی از ارکان مستقل محاسبه، محسوب شده است.
🔹
براساس این داده‌های ترکیبی و میدانی، مراجع ذیربط تأکید کرده اند که حتی با محافظه‌کارانه‌ترین تخمین، این مراسم از تمامی نمونه‌های مشابه در قرن اخیر پیشی گرفته و به‌طور قطع و یقین، بزرگترین مراسم تشییع در طول تاریخ محسوب می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/448828" target="_blank">📅 22:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448821">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jukcKazZ97XnBM6S7_U0XHf3LZ1gd6SPSysWNgjldfbXdLBP999z4k9UpyrXESqiC3wQzk0IDtp17VujXWEVRu8_g7Bp_LK8kvoQqHPGUQk-cKNeMofrBrfE2QzNaSxutiS9A2DNHQ8VN9VrjpB7mkD8JVFx4YcDzSpBO91Y72owmIZdyMmdNLWtwLGyFAFuJG4BKGSECTg-2WAavoCqrBwTMoNtct4fOAUguprvy-dy4a-cqpt57TcHJ2xj1KZtL7tgUpgVE6B3UgmAUn1jCH8zO1jsgGKFVBo1-_GlA93e6luyXVNBH0x21xPZTkQBYsemjWzMnBnJorA77ohKOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERWsSNtXUw9OT30K2mMSdAeWgOG9UKo0AQUHZ4FR8Yqc005VoeXgA4uREiIyHRJgIyJEjVtcblpoSMLrJGkOrdzf3Ms6Hhcdvn9Ee4OqXAT1JGs6631LLcSReCdnckPT15JCvqQv5S0gw4iGY6Ua5kcNrY1Cq8mcFdA7TeAU2LIhjCb525c4IWXrPcya3Wq7fw5y5ujc9pzYRJ4Pm3ZPUJ6VdjILc8vc24xdDtnarS18J2zogGk3T2CfCHohuqOX3baDx_1008NeEV8Sz4FkhZmRHNIen80FlzGs95NfenY-i3uW5rKeilSt5lsH89u7mCdceC_X1I8Sncr2QAeYbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SI8Vuf7yLXGY24m1zmOgQiecJRi4l_wRh_wmUTbkiWmqUKay04FdhE4TSSpkL08MoKt2T4_79lhzMXZoeeqGLNM_4CDfP-INEidlukQ8PTVCshQbXse3SVrUCi_0iPmXt1Oq2CP7pqqiG53RdvifAR_VMUqbmMLKGEACpagHJXeJQAqU9FsEUhwkjdqfdoffbWSCnfwX2hp9rYAc0fkeGOFyNDzKBgMa1EvD2a_z6CRjeYOOhp-QYkv7-rzP3sy3ct-am51hBRIHUd2jr9YNn-d3xBk8lZ009FSxpEdA6h9J3ctWGjbKbgEFnXPncSbL15EAF5j0aSEXi2FY7lJHlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QNZYVtSQXr3PbEASSZqmcwVVUNFFgb7ebJ6RUf5xMDvLEWTRvY-SkSMG1zZTisppFsxfvPjYWUP6VcgVqv7nmexrZfa9BtVEijEfHgyhJiJdMQRY7BSsJHJo2ylHgdE7NUq-BefGnSCrbNCLwlW9nAOCIXWDoNIQ5xCCq47VOMsfSk_iaAq4_btK9ilHDuVyQjSAHAqp32rTYfeog8p-nkzddc66UcEJ-0gxnwIWDS5vqCWR3wt-XyvK1l_ZPr1E43-wgqikAF1aaOnOYR_EwnT_M6NLzELsAdFKoCu9SatqlSFle140j9RpDfJqWDpf61kZCR3g6pzUrNuyTClcdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HY0pLh_sxAsWlZIIVqFqaHqZ997AlKrKsws3MaDrKanhnOPQYOUqzT_WHrIclZ3Y0CI4SD6GTIkuVkrcBjqUB0_ft-GH3VnBNCoS3xeV3Hnsd2cED54OC3_cOw8mhnWHCPXocBH7RFWVtqTiNalLZ_6dKiq8dyVSnVSGxc-aVbDlGWytGcW2HFxN2uCIxK-g2a6_APmz1aTFlfc1LhikqUD_tPrCkRH_bW2zqLjThiyfVSiMZZx1_MQ2uNEusrEb73MwP0AlS5OqQZzY1YnYRwXE9Pqr8sF_GNMPCMd5LFO52WY9R68KSbKpb1ZK8KoyKpAVHTFqs14xQxlk-ce9-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bWltZzSaSLI--8XEMWg1ujSi2I6T8eanmgutvJG7yETnuCQCmzuL8SHKx-VVmwjaUXVO_hdSU-8f4vQRHHFb__TonDapevQ4WHi3WG9WgX-sPPDFY9wSZx9Qv85Go2qdKc_L51-H7Dj2KJ04m8IJBvdl_GHEw6OIvdzJs72u7PFp-47XJZoGw0CAX0DZbOK57n7aGB58iOwLHT-YEode0mpgdIqBiYyZx_EryO5pViROnJhcY0cErhrm6vcRXs6RwdFro3xjnkre36EIqmsfjHANrDDI5hy9AD0CLD-TsDh0C6bRbztHwnW_UxfQqwT5qbhLl9Cyiujtb8Tia6QLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qEzOoHu_qvXFIZXNgzUOo-6KjPSfMM9ChmB52_MJg4mpFkbGe6R3QE1UsoR0DB72ZLEdmONm2GNgP3dCRCkOJoJQ0roDtpCL5ZFnt7FtI8NWtw2BLb1hajnFmc-VQipNly9WB89Lhg9c4BklO5hUlRAFTmLmeYnFVJc0BmbVB6Pecbdgh_Gi4t-daQuOjxSM4s9d-ZJ6XAchgQ38utJjOqt8xdkfExGHoQRhzjgqy70FfzsN8vzXpziMvqJ2AeIICzfNjx7a7lSgGrS9r5IqqXTabSozQTKOlQuuO1xSTgeAuLvH2Rqa66vfukq4LoPjNbXGXd5uAz_7hU3C_HmoSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌های وداع آخر
عکس:
مرتضی مطهری‌نژاد
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/448821" target="_blank">📅 22:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448820">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5371985f25.mp4?token=TvcwzsjMDc9bI9uPCqp8F6hpS9-1Z1KNwaEXgmcDBNge3WcnzBkCIQHFB_gfh6YHFIP7E4LbDkPi_o-KIp5hhQtcMZmFije6xWD8lamm-fsGLDjWhmtkXGMfHygRmRvQoWNqD23C9xv2VVDWZwM2Vx8gJZsfXdpqmz2sSLW7KjFLcbff1LtyPVEtp9HZ91ZBnN92yEBRhjyFJfpkd7atqtJR9EFV-7Z7xl5BWhCrtVnlhDj1C2IHzt6pYcd3gre3Rnp7fot43rWlm0Q1iMLMOXuqCPciNFP0OFycrfliZUlgHeklcIsD7a-oF1rMTi-YIiiMv1Gupj0BFq7T10vx-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5371985f25.mp4?token=TvcwzsjMDc9bI9uPCqp8F6hpS9-1Z1KNwaEXgmcDBNge3WcnzBkCIQHFB_gfh6YHFIP7E4LbDkPi_o-KIp5hhQtcMZmFije6xWD8lamm-fsGLDjWhmtkXGMfHygRmRvQoWNqD23C9xv2VVDWZwM2Vx8gJZsfXdpqmz2sSLW7KjFLcbff1LtyPVEtp9HZ91ZBnN92yEBRhjyFJfpkd7atqtJR9EFV-7Z7xl5BWhCrtVnlhDj1C2IHzt6pYcd3gre3Rnp7fot43rWlm0Q1iMLMOXuqCPciNFP0OFycrfliZUlgHeklcIsD7a-oF1rMTi-YIiiMv1Gupj0BFq7T10vx-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
الوعده وفا امام رضا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/448820" target="_blank">📅 22:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448819">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d23cdb6a64.mp4?token=ZDRDsJUSh_15sx1dJs7K3dMyGVDYRgl3GsYI9nv5BQgE7hk9QRKehn2Nc9xpnZCy6EWmPAaNp5mCiTt49DBaBxKOe8YqPgnysumOYb4waYFMeVyrLpBIsI1msz3FhOsX0cyO8MTQAgz6xIEE8y9-1y0QRj-KlRglSvM4UetIl5Ezsek2yE0koLU0f6lLUb82lI4KiBlTVY_k_jwiWSMBHQGob7W1kJJV7gBy_fdtBH3lD4SkIQ8ua-32m2-7q3uEgBb1t4oCXBBqYwieoJjVQ3Blp7uIsp118NhOWbBModmlmjVgvMzNH5xw-sC3ZKvL3oH0RpFhxRFqenMTa44u-m0L-bhz-vdJnw_R1aXnM9wjCodsoJxsQ6IiXxHYdgmIZFOoqys53QU_3mFRDoXIqj7ArqJsysJ3HGIHJJh0gHwih-YFdVoMJdvigcturCy1vwRUM8QvZ9AAeSPhUVxwafPMu_lYdINGkFU5VwA7w0XikDu9scHnHBboafI4pQEDZcDqo8xBOrF7qP59v1XosY7wKRUCNFgccH1qRR2yCG7yWjeZSv0i6rJq_ZJVOdeyaFFf9mhQJNzOvuPXK7acxpFOin4p7RXi5YfU21EjN4bZfLWFCqVquY26cry_-Rls06ryuZs_APo4R4-iWB3vOzqg68dkQsGgeGRq_7vw_ZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d23cdb6a64.mp4?token=ZDRDsJUSh_15sx1dJs7K3dMyGVDYRgl3GsYI9nv5BQgE7hk9QRKehn2Nc9xpnZCy6EWmPAaNp5mCiTt49DBaBxKOe8YqPgnysumOYb4waYFMeVyrLpBIsI1msz3FhOsX0cyO8MTQAgz6xIEE8y9-1y0QRj-KlRglSvM4UetIl5Ezsek2yE0koLU0f6lLUb82lI4KiBlTVY_k_jwiWSMBHQGob7W1kJJV7gBy_fdtBH3lD4SkIQ8ua-32m2-7q3uEgBb1t4oCXBBqYwieoJjVQ3Blp7uIsp118NhOWbBModmlmjVgvMzNH5xw-sC3ZKvL3oH0RpFhxRFqenMTa44u-m0L-bhz-vdJnw_R1aXnM9wjCodsoJxsQ6IiXxHYdgmIZFOoqys53QU_3mFRDoXIqj7ArqJsysJ3HGIHJJh0gHwih-YFdVoMJdvigcturCy1vwRUM8QvZ9AAeSPhUVxwafPMu_lYdINGkFU5VwA7w0XikDu9scHnHBboafI4pQEDZcDqo8xBOrF7qP59v1XosY7wKRUCNFgccH1qRR2yCG7yWjeZSv0i6rJq_ZJVOdeyaFFf9mhQJNzOvuPXK7acxpFOin4p7RXi5YfU21EjN4bZfLWFCqVquY26cry_-Rls06ryuZs_APo4R4-iWB3vOzqg68dkQsGgeGRq_7vw_ZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید انقلاب بعد از اقامۀ نماز به‌سوی حرم تشییع شد  @Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/448819" target="_blank">📅 22:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448818">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e3dd3673.mp4?token=kTsSzK0fi3Wi_MJmQIjdAiPsfKY8_7hoDW-B8PUMCEThiSTylGHJ5K5v1y7T5kc8qQaWqd1rF0v5sxemC8q4XEvZoz_mxc8VyV4U9HGcygmXC88sUmnOKl_loxVtPPId06C7SF0YMfIM0NwwTgB3wVAhrNgCTcXwAMbyd9oDb3yRd_XKIXqPTwNvrXpWEdNJo_8gebzshBIuj8j743p17HQqhdWnF3tHeNOkVZiSvrJz0xIcWTEIFjaY3PxqVWem0bXqD7QEyOd1My3Re6jcND9Prfm86LVr0CLWncRmCNMolG51gjPiAwchGHefYfoJ-0Wd7ihHl5Sxw4cczKr2wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e3dd3673.mp4?token=kTsSzK0fi3Wi_MJmQIjdAiPsfKY8_7hoDW-B8PUMCEThiSTylGHJ5K5v1y7T5kc8qQaWqd1rF0v5sxemC8q4XEvZoz_mxc8VyV4U9HGcygmXC88sUmnOKl_loxVtPPId06C7SF0YMfIM0NwwTgB3wVAhrNgCTcXwAMbyd9oDb3yRd_XKIXqPTwNvrXpWEdNJo_8gebzshBIuj8j743p17HQqhdWnF3tHeNOkVZiSvrJz0xIcWTEIFjaY3PxqVWem0bXqD7QEyOd1My3Re6jcND9Prfm86LVr0CLWncRmCNMolG51gjPiAwchGHefYfoJ-0Wd7ihHl5Sxw4cczKr2wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اللَّهُمَّ إِنَّا لَا نَعْلَمُ مِنْهُ إِلَّا خَیْرا  @Farsna</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/448818" target="_blank">📅 22:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448817">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc0ff55c55.mp4?token=rNp9h0Ko7ChyUmYeGidu_XylPGPIdQ5xew5RSH-ne5oOfyYSk5Cg6s_OwMZJuSCmxKj_h3xDZg5MosyWzG4Af_8MffwWy2dqoA-cibnTnwqaIcCFX9fQqJ8oLnzIxkFWJ8HnKi39MJWO6AjXlv0khzFupJaY3ITUH8I64L5VVOVBGnnwos60GMFsUy2jFfF_mSL56R-RhjqkrpOvdomiXALi3renmNwZauBSOa8jGnT1iuh_qyuLkKYJGkqRMk4eK1GGEw8WMPFx1q3fY_Edo5HOdn-dzEwiZvAZ8m6DIpAtT4lyJq_iC1fFJjj6YM6YKtBj5SBH2ix_o_vRKwmVGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc0ff55c55.mp4?token=rNp9h0Ko7ChyUmYeGidu_XylPGPIdQ5xew5RSH-ne5oOfyYSk5Cg6s_OwMZJuSCmxKj_h3xDZg5MosyWzG4Af_8MffwWy2dqoA-cibnTnwqaIcCFX9fQqJ8oLnzIxkFWJ8HnKi39MJWO6AjXlv0khzFupJaY3ITUH8I64L5VVOVBGnnwos60GMFsUy2jFfF_mSL56R-RhjqkrpOvdomiXALi3renmNwZauBSOa8jGnT1iuh_qyuLkKYJGkqRMk4eK1GGEw8WMPFx1q3fY_Edo5HOdn-dzEwiZvAZ8m6DIpAtT4lyJq_iC1fFJjj6YM6YKtBj5SBH2ix_o_vRKwmVGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز اقامۀ نماز بر پیکر رهبر شهید انقلاب توسط آیت‌الله سیدمصطفی خامنه‌ای  @Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/448817" target="_blank">📅 21:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448816">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f925c851.mp4?token=E8PcV8Ebo5wvmq7OnDIDxgaPtleaopNwSimzY-DDIESWKrX3af6WW16U6gDRKkpqxd_gYs4hoaxLXTzJlKNz0UltAWyVyA1EvSu28dx84DwD0kmtRTE-T1ftfUMMKTdlfUGPrOyQoXuqT7IUUl6xHi5pkv4BqHryM1I496pBk2WzMp0uyQscMWtg13FuH0Ffmprarbed8ipJKTRsxUVD_ONRGowMV_18TOqRXH_U5MmViN1-16huBmQUwhP_LnW4lkqt1RfHsxVbyv1QOMK1hB1RqzxjvkgUGiFL5v5Sdo5j8T8QpOKWHVUUqxJgKMwhYkDpl1T6PYIjwL5EZ9LgPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f925c851.mp4?token=E8PcV8Ebo5wvmq7OnDIDxgaPtleaopNwSimzY-DDIESWKrX3af6WW16U6gDRKkpqxd_gYs4hoaxLXTzJlKNz0UltAWyVyA1EvSu28dx84DwD0kmtRTE-T1ftfUMMKTdlfUGPrOyQoXuqT7IUUl6xHi5pkv4BqHryM1I496pBk2WzMp0uyQscMWtg13FuH0Ffmprarbed8ipJKTRsxUVD_ONRGowMV_18TOqRXH_U5MmViN1-16huBmQUwhP_LnW4lkqt1RfHsxVbyv1QOMK1hB1RqzxjvkgUGiFL5v5Sdo5j8T8QpOKWHVUUqxJgKMwhYkDpl1T6PYIjwL5EZ9LgPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور فرزند ارشد رهبر شهید در حرم امام‌رضا (ع)  @Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/448816" target="_blank">📅 21:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448815">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qS_TyBnPAu7AL-GkIIq6wI5nDjRPc3iymVWMuSha8ypOvGPm2RUDdjyySXIenwNW8C-yOBsBBXkCs5RoxOaitA6qTkqtZY5ba483_3qcU1HgdmpT2U5Vss9kHDSxPx2_YHgK_5XDpAMVmUs76Qrxw21NmvDedqbYYsJ9ruNIsawfDfU7KjbVBVS1LXohOvDfWMtUWPQ1pyAL-Q4Noycy7CLDTP2xI7S6Ew8z5G7nkNf3loy7tVySk9jzRO4X6uRXX86k26VxEe0o0SvwUDIlG90O2xdNWMU7_uwmlIevnj3eIayrqt8E-akdtvfAZpygGqP9zPckSLk5AKEvzZ9J-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
دیری است زآشیانه جدا مانده‌ای «امین»
◾️
غربت بس است رو سوی آن کوی و بام کن
@Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/448815" target="_blank">📅 21:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448814">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsA_fw6ZgcJgxA20GKsYseKgN23A7GcER9RbZJfSFxeyYN4XWAzdTeBY5SAqHEXiUG6b-BR50km1gPOuWFpx6EtiObwhqKxPo7VwCMEKKgA4CQBvd61tCGCS7g5XGA6i__rfiNNMfrJhaArXamdfu-jhqlmfSF0XP1eeT4446zh1lzgNrIWtNKjXdMsr0yBRksB0opXvVjSx1iD1n6YDFozRmdhJISTKV8GEAKjET1INJNF1Ox7fLw5C9ihl_A7Vlncxqi7mtSlTDdcMe9bbenaTmDyaQmaa5ZH9_W8ROVvl48IMjo3YdgQYIEevrVPFL-VUqkw9phcgTbJM8p6OMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راغب: هنرمندترین رهبر دنیا را از دست دادیم
🔹
مصطفی راغب، خواننده عرصه موسیقی با حضور در تشییع رهبر شهید انقلاب در مشهد، نوشت:
🔹
«جمعیت عجیبی رو امروز در مشهد دیدم؛ خدا به هر کسی همچین عزتی نمیده
🔸
پاک‌ترین و خالص‌ترین رهبر دنیا و از همه مهم‌تر هنرمندترین روشن‌فکرترین چهره‌ برجسته‌ دنیا رو از دست دادیم
🔹
من از کودکی ایشون رو دوست داشتم و این روزها به عمق دوست داشتنم اضافه خواهد شد
🔸
تاسف برای کسانی که هزینه کردند تا این بزرگوار رو در چشم جهان انسان بدی جلوه بدند. فارغ از اینکه عزت و ذلت دست خداست».
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/448814" target="_blank">📅 21:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448813">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29151e8f4e.mp4?token=aDZhWZkYXStN922JCXE4IqgP6nG50LgyhLDgYdIRGsevh7Jo8x2rs__ZWg9b6_m2aU3_zni1Vd4DhA7NAW1F0RfBBVZ9e1YMja494Ye5nA_4aRs6G5NVh5Bu953G1diBMOfradK0aEtCAiOAbfE4krxNeCJVXZcvdkidRcxMfyvKyoETAvI04WPvB0ZtmeJNyT1rhSsJ3ZwTW7yiWBGg6sZctaXQP8C1pf0vZBjEaChU-Baj8-pUWuqCdL7Mvs0mlafVQLKUi7j10jHZ8qDzUIj2j2DnlNgXK6wnsVIzqDOkPSDlm7ULEoOuJrW4leBRQfqaVERwS9WwEtl55QLRTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29151e8f4e.mp4?token=aDZhWZkYXStN922JCXE4IqgP6nG50LgyhLDgYdIRGsevh7Jo8x2rs__ZWg9b6_m2aU3_zni1Vd4DhA7NAW1F0RfBBVZ9e1YMja494Ye5nA_4aRs6G5NVh5Bu953G1diBMOfradK0aEtCAiOAbfE4krxNeCJVXZcvdkidRcxMfyvKyoETAvI04WPvB0ZtmeJNyT1rhSsJ3ZwTW7yiWBGg6sZctaXQP8C1pf0vZBjEaChU-Baj8-pUWuqCdL7Mvs0mlafVQLKUi7j10jHZ8qDzUIj2j2DnlNgXK6wnsVIzqDOkPSDlm7ULEoOuJrW4leBRQfqaVERwS9WwEtl55QLRTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور فرزند ارشد رهبر شهید در حرم امام‌رضا (ع)
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/448813" target="_blank">📅 21:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448812">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hldeHULfl18IA8Dzxa-L8ZuCrG920wFPCOMnbIqkGfquSnldbZLBtnwc4fdas-fFw6WZrZKavAIvMBXyH2uDCnGyMIFfGCZ8ole1W_lPUF66UQKfL98RCVGUfS8HK8bYqrRe0-DbHLzQMDACg1rg_EL986xLSyNF62yKWhGJJaPnIHHOXyJLNMfI24dFfAjE5UHb3ZEP9YEi9nDVlw8TsJI2NtV6OFMi4z25tNTmp2XDcmz3xYmo7ZKX7nzpF08ELTZspAP48R6WosRa1qmb-W4Q9JcAOtfrg5GelPQMHBkloYCn_m3tzoelN-rWID-PYGJm92iT8ZJ50sjX-ADWMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ با پایان رسمی مراسم تشییع، هم‌اینک عزاداران در حرم مطهر رضوی و خیابان‌های منتهی به آن در انتظار اقامه نماز بر پیکر رهبر شهید و خانواده ایشان هستند
🔹
پس از اقامۀ نماز، مراسم رسمی تدفین پیکر شهدا در رواق دارالذکر آغاز خواهد شد.
🔹
زمان خواندن نماز لیلة‌الدفن…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/448812" target="_blank">📅 21:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448811">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da8747021.mp4?token=uMVHPvXIU8j2VHH-rPcPkg7Kuj5HKD7IpGMo5oLjvmxn6CIRmf2lneRENsiY6bkd8NjhCYrMRvFm6ayDSMkePoISSXXKXmr4cGo4vNj7RfqE7cx27_YnxSwdWvM1vKMTvzpIKRnHPX0S1T-wX9p7hR5XKjuVaYRQE3J9QNmINGe4moX_mTY07KNkQf3APT8fh-dE4ComK4Dpea1moMLRkSSQPq_AQlJgI_y_yYNooBU2vJsJAie4lfK8Gn6AAB3D3i8sC2yO9pFpHfQRFZ55aPfqQdOQIiT60vnGDMmRrdDUWPwNK9JG-5d0VUBrFCWtUQhV0MJ25yJaiJ1qBuki9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da8747021.mp4?token=uMVHPvXIU8j2VHH-rPcPkg7Kuj5HKD7IpGMo5oLjvmxn6CIRmf2lneRENsiY6bkd8NjhCYrMRvFm6ayDSMkePoISSXXKXmr4cGo4vNj7RfqE7cx27_YnxSwdWvM1vKMTvzpIKRnHPX0S1T-wX9p7hR5XKjuVaYRQE3J9QNmINGe4moX_mTY07KNkQf3APT8fh-dE4ComK4Dpea1moMLRkSSQPq_AQlJgI_y_yYNooBU2vJsJAie4lfK8Gn6AAB3D3i8sC2yO9pFpHfQRFZ55aPfqQdOQIiT60vnGDMmRrdDUWPwNK9JG-5d0VUBrFCWtUQhV0MJ25yJaiJ1qBuki9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور قالیباف، اژه‌ای، مخبر، آیت‌الله علم‌الهدی و سیدحسن خمینی در حرم رضوی
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/448811" target="_blank">📅 21:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448807">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DfilJksrzhqD0fE8WVw0aUYSjhOQ5vFOGUvv4QrQyfZ6KewIfIad_BiwLSZtIoCGi4OayMCghlToeCWo3uWCjJdx7x8Mrp4MwsJBWfmKn-6qxR-VXxTjMcWU9Vw2perJYkROudT9x4FKDB0r94qCr7FQm1AWBPNeeJa8EnwRneY_pboiSTNIRnlBvN7SotHLavfpEcpi6yDvTpUh0tGedWwfPM70H9yNz1WKCDkGQj1HhQFAVCQMvtfB8ROxgo04NZWlGANXs2j2O-iJhO5f4jKWUpGtGUQig2srz4DH3OmAfZ7IJ_rWtnonC29-6rSOOR67BUPwbDad2l6Tdb653A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nd26rj6BX0mo33hyQ8KbwcS6xHwt3UaTZJuoLQbtjiVDZX51o5E98TgAQDPCR5m4D5FD7cIlNfOlbGGFvcv8OlhPVyPF2NCtnSdhGAuEdRXi8NPyBdvBieXBZQ5ipid07k1uI1tHh5bLIeuUn41Py2eTgC-hngRz0-rfQVxTQOV6O3VcONFfqq_OT5YeBxZsk0SBlkjCkABC1PTC49LmeRFrjqcQ1IDPALQuYMDpkVPVINKm3cfuNgJWQabjIPFEe5Op9PLmhR-hYlJWYgFSZFyHhhMeb0LInluGC3XAzg0SNw-bHOKNeARs2Ehp0nrGLcNSs0e8UVv1jxhJRS-4rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ivbC1adwX6uNcsP1jMhfYjPnmfgabJ2Bv-flQAC9qRPTKjELzeEASqjFoitHUJpD2rLlS6reWKd_sKls7b9Jfl3LzWAaqJ2O6KcCzKfsbfq0_eWcNDJDrnb1qOR47xyuQ8qdSik0A0xLlkH42SJ3tjAuuAxBnncNj5Yh-85cWDJ2eikLlt7VvH0Aumvn-FL2ta6FaWcdRFxFWDlhfOnWxOkA4leWpgIv0n0Z0X7LlrPf1FH0puVxYbRxc5wrDUQL3Wvm0DIAEvGOMhjFyWZpyOtzsU90FUR6JpOPnWIurd68qT1ISRZyBQoOa76_0iBQ806Px6qiR6eb6XdBQaYRxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eZWMc-2xmspzDWWpC1QofivVuwA66gspdlbrkufCJyugenPJj4N-_EWCugBVnq28pVqlrrjOsf96dvVZEf9uIGZj7LJGLxwD_5wmzzU0QoBUE17XN8nDVapK9wktFd23qruk-98K6KS1k_9qU11aRg8gRIVSWfJkXbY3nWePdkNuM_BNmvvMrW8vm_YKO76gRhzU1h2Z-aDD7dth-Gzzy-CsL4W46SWf0a8Tut-pbWLdZc80WTR3yHzpTtUlSny1xcCsSJrAsFqhojJJEWf5kx8Il-zDjW18WvscMlvVco43SJPxG61fPyLlYLdafRIEbkowL-d33VoI0z61XkEvlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
امروز پرچم خون‌خواهی بالا بود
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/448807" target="_blank">📅 21:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448806">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb9c4c462b.mp4?token=fF9BRnH3pZroHadr62JdiKEKrznRKxfuF6hBnmqLisHfrXCu8zkjpLpob5YmhGwvCW_8D0rRp2gAolNRFve7B6XttH9jYwNw7OnA9C4VGnpmR7lohzaYJih1qKNap9iWBfjXkcdFhOwjtX49AznEbkNt5cCOk0CrxDfn24cBVSjPNJ9lERNZpxtL6FS7ybU9NSsq255BB4pnIKD5UY8og-37AY-3fmspNTEC5jXKe3hzrANQH_chr3brVcFXrG5OrlQMlG2nPM0f5At8_PAj73SfOaFKD7VxB9-oevs8Cww-PcA7G9vO0jWnUIg-2KFyKq1D1O9kIpr8NYIu6vRI6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb9c4c462b.mp4?token=fF9BRnH3pZroHadr62JdiKEKrznRKxfuF6hBnmqLisHfrXCu8zkjpLpob5YmhGwvCW_8D0rRp2gAolNRFve7B6XttH9jYwNw7OnA9C4VGnpmR7lohzaYJih1qKNap9iWBfjXkcdFhOwjtX49AznEbkNt5cCOk0CrxDfn24cBVSjPNJ9lERNZpxtL6FS7ybU9NSsq255BB4pnIKD5UY8og-37AY-3fmspNTEC5jXKe3hzrANQH_chr3brVcFXrG5OrlQMlG2nPM0f5At8_PAj73SfOaFKD7VxB9-oevs8Cww-PcA7G9vO0jWnUIg-2KFyKq1D1O9kIpr8NYIu6vRI6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیدعلی صبور ما خدانگه‌دار
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/448806" target="_blank">📅 21:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448805">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcd42908d3.mp4?token=jL4Z5TI15LPRZbjSFV5wBCm8ERkPEY1vPj9QkNm80NQNgOQsVBNWtAc-BfACq2rE_BNo90IXNwajg8S2Epgk1Suf5O82lUBRnjBJsJ7OXMBQGv_oLOjwl_B46SenoJiVLIPdtfJKTMi1EP7hpy40hrHOBVfbgXRG8zVdVenOpiCgziDO9HcwrJ_TZuHDdX2vS4bQz8udNAxhw-_03RxTrhu1qdQtwYFNlI_kQlcZTq9F2BAZ0txAD7fPYYGzr2gv-quXNUZgeM-ehjFOXqUFdtaMdgu9RS1-VyR60QOudQ0sDn-Cl2izwyrN-Kc628wOKGPsz4fT3SfPVq2-srxQIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcd42908d3.mp4?token=jL4Z5TI15LPRZbjSFV5wBCm8ERkPEY1vPj9QkNm80NQNgOQsVBNWtAc-BfACq2rE_BNo90IXNwajg8S2Epgk1Suf5O82lUBRnjBJsJ7OXMBQGv_oLOjwl_B46SenoJiVLIPdtfJKTMi1EP7hpy40hrHOBVfbgXRG8zVdVenOpiCgziDO9HcwrJ_TZuHDdX2vS4bQz8udNAxhw-_03RxTrhu1qdQtwYFNlI_kQlcZTq9F2BAZ0txAD7fPYYGzr2gv-quXNUZgeM-ehjFOXqUFdtaMdgu9RS1-VyR60QOudQ0sDn-Cl2izwyrN-Kc628wOKGPsz4fT3SfPVq2-srxQIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم امام ‌رضا(ع) عاشورایی شد
🔸
مداحی مهدی رسولی در حرم امام رضا (ع)
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/448805" target="_blank">📅 21:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448804">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bee60265af.mp4?token=r1gOsln_ygxrzVGip3hTaYDlvb_vG24Q7Vc36xuaV6AUua-m-daamgqhlOi8_Kk553mLo26mhTlX6XzsBkGetcMHflY8EBvJjdsnIlqGi_5tiEe9uEARKsj4HD-bR1xPdMi02eJdrW3HcIACuD-L81gQ8gpdEURn69az7mXgsVoZiPAGIFECvWQs312HQGxylsmmQAXqwxv7hi-bicess4-BEN8HddzhPuRbyMgwVN9X5BGuxRrXj5LiEBMpQCUODhX_oQrBBGiphZwqdfkntZQhtstHavNdTszv5u157_1AwiNEe7UEiDbaWFwS4TE5xDKmhv-gUY3ns4QCBdIlK57E4vCnv5BVfKvfbOD0CPCI4-ECOuVK3aAwozzIBxyu79P4YkyQQJcAWOdqgT6kosY4DEFiZiYCZOKQXEJRpjLKTzPFnE8h8ftU8tNXzgfByknfDeXbv7QFHCV9wOvDZdklZUklQ5OTkem-WNAggDRakLH7Nxjkq-GNcYPb-AieVdTLr9miMxO8dpgJfUH4tQ9NeH20QOXqf0a01xlunygah8Dz7ohvK5NkDaDAf-xuZscroxOMyNDmFEn9CHjSjjgTJZsOhjjSdlLLmXBTBqhESdqkEC2AWxif7bmj2GNYoA9ChCN7i13kqlWs6-SQ_72utbBYJy2M3Sdu2avqpzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bee60265af.mp4?token=r1gOsln_ygxrzVGip3hTaYDlvb_vG24Q7Vc36xuaV6AUua-m-daamgqhlOi8_Kk553mLo26mhTlX6XzsBkGetcMHflY8EBvJjdsnIlqGi_5tiEe9uEARKsj4HD-bR1xPdMi02eJdrW3HcIACuD-L81gQ8gpdEURn69az7mXgsVoZiPAGIFECvWQs312HQGxylsmmQAXqwxv7hi-bicess4-BEN8HddzhPuRbyMgwVN9X5BGuxRrXj5LiEBMpQCUODhX_oQrBBGiphZwqdfkntZQhtstHavNdTszv5u157_1AwiNEe7UEiDbaWFwS4TE5xDKmhv-gUY3ns4QCBdIlK57E4vCnv5BVfKvfbOD0CPCI4-ECOuVK3aAwozzIBxyu79P4YkyQQJcAWOdqgT6kosY4DEFiZiYCZOKQXEJRpjLKTzPFnE8h8ftU8tNXzgfByknfDeXbv7QFHCV9wOvDZdklZUklQ5OTkem-WNAggDRakLH7Nxjkq-GNcYPb-AieVdTLr9miMxO8dpgJfUH4tQ9NeH20QOXqf0a01xlunygah8Dz7ohvK5NkDaDAf-xuZscroxOMyNDmFEn9CHjSjjgTJZsOhjjSdlLLmXBTBqhESdqkEC2AWxif7bmj2GNYoA9ChCN7i13kqlWs6-SQ_72utbBYJy2M3Sdu2avqpzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقا فدای ایران شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/448804" target="_blank">📅 21:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448803">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf5a63ae6f.mp4?token=IS4yHa2BixyPK5bnwCLAnEzSK9ronxTZ1Z9QgQkqS2dTqGvY4jmAOIyy-jsmreb414akYi6QurBpPlfNwGjr4OX_at4_c2w1Qtr0y8ReUzfZRS_CfreyW9DMv0CvR5Ug6FsAxGo5oKxFLjgxurcCZTlVnwVVrNetsgFXtj60kv67sxhDG6j-szsHzvU0gKzDibwClAnd68CvFN0JdJXXySS03AZk0mSbVnrAGvW1UpBfmrSoXtisTYFYtAHHqsTopW3kq69sH6pZF_puHoBpfAmETrNfr439dCHPeLCl8ZIZN_2iPloYr5dpUN2bKvqa4ViDEJrTLA9MqbjTWhkIcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf5a63ae6f.mp4?token=IS4yHa2BixyPK5bnwCLAnEzSK9ronxTZ1Z9QgQkqS2dTqGvY4jmAOIyy-jsmreb414akYi6QurBpPlfNwGjr4OX_at4_c2w1Qtr0y8ReUzfZRS_CfreyW9DMv0CvR5Ug6FsAxGo5oKxFLjgxurcCZTlVnwVVrNetsgFXtj60kv67sxhDG6j-szsHzvU0gKzDibwClAnd68CvFN0JdJXXySS03AZk0mSbVnrAGvW1UpBfmrSoXtisTYFYtAHHqsTopW3kq69sH6pZF_puHoBpfAmETrNfr439dCHPeLCl8ZIZN_2iPloYr5dpUN2bKvqa4ViDEJrTLA9MqbjTWhkIcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یکی بهم بگه دروغه...
🔸
نوحه‌خوانی مهدی رسولی در حرم امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/448803" target="_blank">📅 21:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448802">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6100f7673c.mp4?token=SvicBLLj30fS1T0mQQfiG957BUFCRlMVMsXdrD5DL10vYI_a_Yw9A3B-JQqj37WWtSGox7nySNaQToWDvysXcd7FmJ2YeldQeL3N8fJ873icEPHWlZdT4K3oEaDYrl6dBO8GDNjPfV66_wlk3TUVEr7OQNWY2mr8pgVT3knaV5yKLBgTteEE1fBoGxVxGf1fPjqg5Wwl2eiiK-k7vNvJRIDs-2zpXGN8ocKr2e0DgNUctBS74JreSyoYr0XV-YxKJciIPmdJS0kpv5z2T4H0hS1Fet2pXiTyVB5Mi-jNHLDu5TITY2PQZ4rEphgGN2UZKyRsVQcC4xDgF_5E-9tmCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6100f7673c.mp4?token=SvicBLLj30fS1T0mQQfiG957BUFCRlMVMsXdrD5DL10vYI_a_Yw9A3B-JQqj37WWtSGox7nySNaQToWDvysXcd7FmJ2YeldQeL3N8fJ873icEPHWlZdT4K3oEaDYrl6dBO8GDNjPfV66_wlk3TUVEr7OQNWY2mr8pgVT3knaV5yKLBgTteEE1fBoGxVxGf1fPjqg5Wwl2eiiK-k7vNvJRIDs-2zpXGN8ocKr2e0DgNUctBS74JreSyoYr0XV-YxKJciIPmdJS0kpv5z2T4H0hS1Fet2pXiTyVB5Mi-jNHLDu5TITY2PQZ4rEphgGN2UZKyRsVQcC4xDgF_5E-9tmCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا رسانه‌های معاند از وحدت ایران وعراق به وحشت افتادند
؟
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/448802" target="_blank">📅 21:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448801">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28ae2384a7.mp4?token=qVaM9G8AKbm50BSLOa8G_E4_bKYwFbGjriU1qgDf6FqldQIOAtzdeABP4mX4qIja9cSViYNo3ulf8iVMpdHEPewHL5KKBWE550Y-pc-BNr8RF5X2cc4M7ZkFS80DTnHHMZCPRKx4iVW_exXnL83thlbrS8SibtnU0yjUS4QIvq0IT5c6H5nIp-d2sa3OZN6aHe9R-RWE_pFVeD_XG4gtB-YQRYD-lOekIClt4plWfuJoTbdjMRbQ_diKbsKSxsjp6zvtfl_he4pbey0u1pGVL3Q-xwsJqHIWbO_61OjU35qhhZdxKlJnlqWmTxUKTdGxgV6C7i6invxpebLY_HecVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28ae2384a7.mp4?token=qVaM9G8AKbm50BSLOa8G_E4_bKYwFbGjriU1qgDf6FqldQIOAtzdeABP4mX4qIja9cSViYNo3ulf8iVMpdHEPewHL5KKBWE550Y-pc-BNr8RF5X2cc4M7ZkFS80DTnHHMZCPRKx4iVW_exXnL83thlbrS8SibtnU0yjUS4QIvq0IT5c6H5nIp-d2sa3OZN6aHe9R-RWE_pFVeD_XG4gtB-YQRYD-lOekIClt4plWfuJoTbdjMRbQ_diKbsKSxsjp6zvtfl_he4pbey0u1pGVL3Q-xwsJqHIWbO_61OjU35qhhZdxKlJnlqWmTxUKTdGxgV6C7i6invxpebLY_HecVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک فرمان، میلیون‌ها روایت
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/448801" target="_blank">📅 21:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448800">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2575953999.mp4?token=Z4zxCIKKWdbF__UGOgig_B3dxD1liwdnJ0Le1HlHwX16zf8p9qoYYRUISZinioVj9xEjEd3Cuo4ltTeBU0a1atkl-_E9wJCI9ftk9b2AsjEteDu9FHH5iaJCh4OLKT2vB2I-5c3lRKlx9DIw7soL1eI9oIxxTEhkgmFbNfXzyFFdohRbR16eH7BdSzNKkaegbshDsv14gpgxzz4eTx98RAoAo5q3ajBW9_C1v-HYXYtNbpsIY5lTFdrWLxKK-OIpoZps14LQTinsQfjiKAFKn6v5COj6_GxM2ZJByg4JdJO0TrdOfKGWrBLpy1fYLbTFNk3U76M5qJ6KKx5bcAS6GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2575953999.mp4?token=Z4zxCIKKWdbF__UGOgig_B3dxD1liwdnJ0Le1HlHwX16zf8p9qoYYRUISZinioVj9xEjEd3Cuo4ltTeBU0a1atkl-_E9wJCI9ftk9b2AsjEteDu9FHH5iaJCh4OLKT2vB2I-5c3lRKlx9DIw7soL1eI9oIxxTEhkgmFbNfXzyFFdohRbR16eH7BdSzNKkaegbshDsv14gpgxzz4eTx98RAoAo5q3ajBW9_C1v-HYXYtNbpsIY5lTFdrWLxKK-OIpoZps14LQTinsQfjiKAFKn6v5COj6_GxM2ZJByg4JdJO0TrdOfKGWrBLpy1fYLbTFNk3U76M5qJ6KKx5bcAS6GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایش تشییع تاریخی رهبر شهید از زبان رسانه‌های خارجی
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/448800" target="_blank">📅 21:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448799">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944512f8aa.mp4?token=E5hxNUV5767OICSB0WAAra5w4IBJFT7XNsjbRgQf6nB-FchoY7zQysJLrVokSbwTVUQ4VzScVB_VO16Stq5KXTVuDXLc5Dp7AP8-KSCixU9-MxjRDxB69e6iP7keRflPRhFJXWCgQC_BD7bdXOosFyaxQxJlHY0Dw69Idl2UfCPj56GyhqKjsP-b4r4cvo5TvR30TaN116dbai-lOHOg-vxNrbWoqD0PF7IvWRwl8nCX3flgRVPXpuwyUK6LjdNgHVoDxvq45F6CYe_3Q1pyJ7jR3YDMdZ02akVfgU5lBPaduC99BoeZ_UF_ERAklhS6ZzOmAdB5ljCWHf5WnRBRSBLFI8CIPfv9AEMsLqZjbAIHEKJB2_wAg1uhMUWalISSFxVA9pf7ClCZU9nlqkbPjfFlp13-BWJUZvwX5qB3_3grUVIaRLrvNNiAjMH-JiSfZt8cyT_e-s8YoGWy1wqf2cwf5tTTH7NoiHnMfwV2nWJ5XK_EHFf1mnccstGmCy9Ozh5z88zOu6B_WnVelmPZ639w6nOEI1H2N0nTbEhVZohtWQ2Nl8og0rmvi8ldD9Jbwn_0eV8EIPL0RltrJrpWaL3bDSUrRNgfidW6pAOfnr3cHFcT4rA2ymv7o9hodqK8ANOoI-ABu0S7onOP6HjkzJRwVPGirDpXkWYNrNS_6ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944512f8aa.mp4?token=E5hxNUV5767OICSB0WAAra5w4IBJFT7XNsjbRgQf6nB-FchoY7zQysJLrVokSbwTVUQ4VzScVB_VO16Stq5KXTVuDXLc5Dp7AP8-KSCixU9-MxjRDxB69e6iP7keRflPRhFJXWCgQC_BD7bdXOosFyaxQxJlHY0Dw69Idl2UfCPj56GyhqKjsP-b4r4cvo5TvR30TaN116dbai-lOHOg-vxNrbWoqD0PF7IvWRwl8nCX3flgRVPXpuwyUK6LjdNgHVoDxvq45F6CYe_3Q1pyJ7jR3YDMdZ02akVfgU5lBPaduC99BoeZ_UF_ERAklhS6ZzOmAdB5ljCWHf5WnRBRSBLFI8CIPfv9AEMsLqZjbAIHEKJB2_wAg1uhMUWalISSFxVA9pf7ClCZU9nlqkbPjfFlp13-BWJUZvwX5qB3_3grUVIaRLrvNNiAjMH-JiSfZt8cyT_e-s8YoGWy1wqf2cwf5tTTH7NoiHnMfwV2nWJ5XK_EHFf1mnccstGmCy9Ozh5z88zOu6B_WnVelmPZ639w6nOEI1H2N0nTbEhVZohtWQ2Nl8og0rmvi8ldD9Jbwn_0eV8EIPL0RltrJrpWaL3bDSUrRNgfidW6pAOfnr3cHFcT4rA2ymv7o9hodqK8ANOoI-ABu0S7onOP6HjkzJRwVPGirDpXkWYNrNS_6ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آسمان دشمن در میانِ شعله‌های موشک‌های بالستیک
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/448799" target="_blank">📅 21:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448798">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc7e483608.mp4?token=ae1Gcul_DEStwaeIfCWEw16dtEDzGuQxEdir2ioMj4DAFFdjaWLSCfo7PqnyFwxliIdCgO6STCfmSQGBOu0xmUdCg9wIVZdENACQOXet_SeVGs8aPsvRSv90S_slIkVM1UxPjNgMxkn4fWzlao6W1OvC7PMp4OBjmMnUj22YsM_-eRdHuEmw9BF9-v19iWULCRSpYdx1PM_NZOcyC0d2cdiUwxhE8gltOv9jtfu8MRoJ0w9jUo0sDJU2v2Dpdz2PHz4MfEx9RLuklouFukZ03_lbpOEw0MzkmYrRxbHE_5RIsyFFvT-0I7KbCxWI1LCYK1C7LHwTg7OhxDcfkk4t_4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc7e483608.mp4?token=ae1Gcul_DEStwaeIfCWEw16dtEDzGuQxEdir2ioMj4DAFFdjaWLSCfo7PqnyFwxliIdCgO6STCfmSQGBOu0xmUdCg9wIVZdENACQOXet_SeVGs8aPsvRSv90S_slIkVM1UxPjNgMxkn4fWzlao6W1OvC7PMp4OBjmMnUj22YsM_-eRdHuEmw9BF9-v19iWULCRSpYdx1PM_NZOcyC0d2cdiUwxhE8gltOv9jtfu8MRoJ0w9jUo0sDJU2v2Dpdz2PHz4MfEx9RLuklouFukZ03_lbpOEw0MzkmYrRxbHE_5RIsyFFvT-0I7KbCxWI1LCYK1C7LHwTg7OhxDcfkk4t_4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار «مرگ بر آمریکا» و «مرگ بر اسرائیل» در حرم رضوی طنین‌انداز شد
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/448798" target="_blank">📅 20:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448797">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🎥
خداحافظ مقتدایِ آسمانی
...
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/448797" target="_blank">📅 20:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448796">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8791f99083.mp4?token=gPPpS79PPLPLkzjiodT_UpxhNsTfDHUxvL0D83Fcr3k37Wy4p9Odzf3btJ0QzN-fK-dyTzuhz3cZzBzQwUSFC3FEvEC3b4t5HIposSm87KAo3ALVBLDKBZ-VB-O2eCAUNH7d_rDifSIMJhcMhldfPJGEKZXGquj_e9Ltw7g2NwKMvWgdrPo6qYVT5W8vhJDKVipggH_SPaudStq8I6AsWt3ShBb7CxEfjH2NzXDwMsg3ch8InjGcPEvwH6LAMbGYnWOyKPhSzM0G0EFWIgqWEm2fU8XkAfMBYdkyZd41sWpCLPLHD_8r_HV8XZ2iA6_x5OO5ewlNLO348n9WeI1fNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8791f99083.mp4?token=gPPpS79PPLPLkzjiodT_UpxhNsTfDHUxvL0D83Fcr3k37Wy4p9Odzf3btJ0QzN-fK-dyTzuhz3cZzBzQwUSFC3FEvEC3b4t5HIposSm87KAo3ALVBLDKBZ-VB-O2eCAUNH7d_rDifSIMJhcMhldfPJGEKZXGquj_e9Ltw7g2NwKMvWgdrPo6qYVT5W8vhJDKVipggH_SPaudStq8I6AsWt3ShBb7CxEfjH2NzXDwMsg3ch8InjGcPEvwH6LAMbGYnWOyKPhSzM0G0EFWIgqWEm2fU8XkAfMBYdkyZd41sWpCLPLHD_8r_HV8XZ2iA6_x5OO5ewlNLO348n9WeI1fNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار یک‌صدای مردم در حرم رضوی: حرف ما یک کلام، انتقام انتقام
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/448796" target="_blank">📅 20:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448795">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c208eda68.mp4?token=ecus5Wme0vSZReB7B2Xiq1NycFViFsEAQIITVPgzZDoF3oKfRZepREMaApwAhUt2DxjbNo8eSQ3xbBWfMHvzF8-KgDygKZ1Yspj-HABRPBE8NrBIgX1j2z--cRTYdx1Hs4Iozf3cu7MVS-v-hYDCD8r3j41pgT_d3zi0udW95bzChQzn8cjuocx2v1WElXAP9fNSR__bKnt7PEah2avGw9by6-4C5efNEJZCYfWZUvOaA9R_tMGoGzAtpzSQzRTCnWtS4HDb-hg82VSVkw7HQ6-xO4z-ObsZyhN6rOrS4WMcGcM_bltuQ5SfFDCioaWKUj_aDj6fBQ8RvSyLbXrTUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c208eda68.mp4?token=ecus5Wme0vSZReB7B2Xiq1NycFViFsEAQIITVPgzZDoF3oKfRZepREMaApwAhUt2DxjbNo8eSQ3xbBWfMHvzF8-KgDygKZ1Yspj-HABRPBE8NrBIgX1j2z--cRTYdx1Hs4Iozf3cu7MVS-v-hYDCD8r3j41pgT_d3zi0udW95bzChQzn8cjuocx2v1WElXAP9fNSR__bKnt7PEah2avGw9by6-4C5efNEJZCYfWZUvOaA9R_tMGoGzAtpzSQzRTCnWtS4HDb-hg82VSVkw7HQ6-xO4z-ObsZyhN6rOrS4WMcGcM_bltuQ5SfFDCioaWKUj_aDj6fBQ8RvSyLbXrTUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ای پسر فاطمه(س) منتقم تو هستیم
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/448795" target="_blank">📅 20:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448794">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec21531385.mp4?token=MfKasgyMGIwWs4_w6vZ5h12XLf0zSQafxK0QRxrtSwWESpTnO9jAhGoMkUpdcdFFsClJbdMK4une6xA2fYplGcb5ScLAIVB77XUu_nqps9N5kGbFLqNCzOKSDtrzSh4uFi0b9h5aej3iKRtvyEaBdjhJTB-ncTEieYifQJqT7A2ohF-Qu1075rNg2tDymqrN2auLj0DQx2Me1pikFtlS4SGzw-5aQaM1JdtKpZn1d_YP49yoP0xBP6RLHUeYztyO7ahuOp_v72vbbGDdyo4JbcrL-VZISZ9t-IlBPYpproBcEcHIVECM9B8VVSWle8zIZBm7ZWF6BYGFwDdjB0QOeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec21531385.mp4?token=MfKasgyMGIwWs4_w6vZ5h12XLf0zSQafxK0QRxrtSwWESpTnO9jAhGoMkUpdcdFFsClJbdMK4une6xA2fYplGcb5ScLAIVB77XUu_nqps9N5kGbFLqNCzOKSDtrzSh4uFi0b9h5aej3iKRtvyEaBdjhJTB-ncTEieYifQJqT7A2ohF-Qu1075rNg2tDymqrN2auLj0DQx2Me1pikFtlS4SGzw-5aQaM1JdtKpZn1d_YP49yoP0xBP6RLHUeYztyO7ahuOp_v72vbbGDdyo4JbcrL-VZISZ9t-IlBPYpproBcEcHIVECM9B8VVSWle8zIZBm7ZWF6BYGFwDdjB0QOeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید با خانواده خود به بهشت سلام کرد
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/448794" target="_blank">📅 20:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448793">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73925989f.mp4?token=ojmQthLZO8cUMruAUtTFkdSe5I2OZAhB-3cy_LtegAo8zbX9QLT00fhbiUcwdA-I1S3r4IbgyAvmahmzSL84wS9CDI8iZbldZyJPYk3u_HZVBmhz2qL58zPdGsrt4UKxzcnabRAvDy4Dxk7-QbXINBf8BHxt8gGQqhtowvC9j-AneHMsgQlPpjfveq349YWupPdFmnI0p3kbsvhNg2eiH0Wsqo1jvMFgj7wTjHnZtuT8JUsoOQAv6h9iyAPdwdY4rAAzBsEMppbjne2Qw5Pg3qQfIaXwriRQ-N-S_7CnmlO8XQbSqB0xyaRVxjocWHyOq6zZtq4tv4odKIqb5HQFUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73925989f.mp4?token=ojmQthLZO8cUMruAUtTFkdSe5I2OZAhB-3cy_LtegAo8zbX9QLT00fhbiUcwdA-I1S3r4IbgyAvmahmzSL84wS9CDI8iZbldZyJPYk3u_HZVBmhz2qL58zPdGsrt4UKxzcnabRAvDy4Dxk7-QbXINBf8BHxt8gGQqhtowvC9j-AneHMsgQlPpjfveq349YWupPdFmnI0p3kbsvhNg2eiH0Wsqo1jvMFgj7wTjHnZtuT8JUsoOQAv6h9iyAPdwdY4rAAzBsEMppbjne2Qw5Pg3qQfIaXwriRQ-N-S_7CnmlO8XQbSqB0xyaRVxjocWHyOq6zZtq4tv4odKIqb5HQFUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خداحافظ آقاجان
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/448793" target="_blank">📅 20:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448792">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHv7QRe971gWVcJaR6Y8rLKSK_USUVWbKfKB5BwTKSUEUgbe0OFiv_frOUw4KKXIugfU3h4NyOiyVldzcdB65A8kfazNczBahc4FN68wLULh3D-5Axxt_2TprS7j05RA0kNeydCRy3yfgfCAVYsk-hvMWd2mguJh5HV_Bs6Dq5EFHQpKm9WjZerCflwjyWCVDGHE4R7oiKUyHW47u9kf_5qt9H5GgSwCssP67iw7FMMsV6De9-oDyqGZy9Xu1cjKt6cB_hOUP2TEMVtTnIG8NxQw3KkUD_UtOF5XTrYvveT648EM4mHnbz-FtUW5fxm1Nncqh_UYS29ukPgrTIcM7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
خادم حضرت خورشید به آغوش حرم باز آمد…
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/448792" target="_blank">📅 20:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448791">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8329395b4.mp4?token=MowG9tV_FyOaca9h6T_nxIqf1N5QNwvIOz2VYFodkR5kHbBOuR54MheJI2DXqS9LtEKBHMpGuJXOAGcHO7k_25WTVW1ZOvcN_xkvKdP-Imx-0tPlBLRRSbdBO97dyqzML6P62eQ2XIfyb_kLcA-jNtIUwTb_R_D5obyBTBM-kB2clx86OpezYczTLJqhggJmMh4yIlAYf-JcvBH0aBgTq_i4516hZCiNg0Qf84AaBH1J05J_lOz2-RsOOEsfH23LsvgfAS6u7E_W4iDSq-gVaam3hkXhoRJs5fA51cLikdGkEGZVl-CgoiZmdZlSwPNhd3AzG8wZzs0PTHVb86q5Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8329395b4.mp4?token=MowG9tV_FyOaca9h6T_nxIqf1N5QNwvIOz2VYFodkR5kHbBOuR54MheJI2DXqS9LtEKBHMpGuJXOAGcHO7k_25WTVW1ZOvcN_xkvKdP-Imx-0tPlBLRRSbdBO97dyqzML6P62eQ2XIfyb_kLcA-jNtIUwTb_R_D5obyBTBM-kB2clx86OpezYczTLJqhggJmMh4yIlAYf-JcvBH0aBgTq_i4516hZCiNg0Qf84AaBH1J05J_lOz2-RsOOEsfH23LsvgfAS6u7E_W4iDSq-gVaam3hkXhoRJs5fA51cLikdGkEGZVl-CgoiZmdZlSwPNhd3AzG8wZzs0PTHVb86q5Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوای «یا حسین(ع)» در حرم امام رضا(ع) طنین‌انداز شد
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/448791" target="_blank">📅 20:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448785">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s-X8ylgJaaxfO2KWsAzW6dF1H8gm4WT7pd3YQlUEg6LIOWYFCIpUrGG94YKy3G-LkPxn0cwpH70_x5u7LUFz7F1LHw0z9uZXow2rKL4yCwUtMh47aWB1Pan6J-1TQ1YmupRmnB-kq8owyg-V72vv2ZA5QhLmXbH0X9oeljaIhCNFglIgxBobxJeMgm_3raHBg0u2X64WJyJ-K3xgd2UDDWYYXOIibIslMlDREkDFKNqA5JBQBfX2RK4taU3p1zN9NpId0XGgJKjX_glK7TpUxOc1OVPZ34IWwbnhITdVvwGrw2p1k8Kd9uQ51N8TXVY21S9mqDFuWoHOezv8aMvWMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hYaZ4TPzXcsUBVRmNfSuDB3sxnNHqK2h5-06vyPmsK8nLC8cTB-X5j4V0kzGizXx6E1y0LDcGdXlF81oRFkN0szboz4HdxgCz8aVzNXE4AYjtpaMF3W6AMeTxfIJVO6IEueVdH-pcZ-KTmwGb1lfG2cezm6G8GvRuu3pZvLUzjsHRxK1RkuLgpn2Tc6BeYvl8F-SxzbbMAt2xlK85fzFfbWjkz-BIIbo2MLFRMTa128KUxBrBgoqBHj4wsgnoV33AD6QSzh1LIwfbXRSD6aulgfuSgkx_GaH7LE2Rol0dclVlxzd_GFzeFY3fdMGP2rtG8Z6G1a45Nwf8GZLyg7svg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qf-YQ4V339KCyf9ji8FQmL--SAtQXlipwT5OmZVxUOhEN8joEHb64fdtAiNKPd0mZA2E0008OVJd9acoLmwySupF_edKhoeYxNyPMtPKP7dvVtC6Y9266h-v8Gymt_SYIqihOH295pmaDpC6HWVll6fnyrAgOu9fjn63Mj-q5elrfLLQRm6CL2ymgKwlqLjhSM6ScLeCOAiALiFvZHBB7-pJlF21MUw4LkfXwUI_SrSF83bTlhGUpa4ur8CGNzdPGTrWfraFeFnOv0EEG9l6c_d28PCyXcyVUsu5kOQXsgfLvF078t2AvLW5dczK5f2HVAoF50Onjz65L9-zm91G8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgEaHVvYOFbLb_uRxSi8ZHwW2ezDWMf8VAZhub92j9UxcmeVxrKIwiXX_r-equf-LRs4duU8U9ErmWGAkb-vef9BazggV3O7zaG6jCpqZER5uVMyKmZcFSegKJ9nPKTFcZF_wFQ_E_qhE23bqEnqFBs2472OOqpbHUlGVsQEzD4yLxL5-qSujmUuDsQj7bo3TMx-ySGe9iKpcjSRgMJqW5BYykIGWC-2uaeGkyyhV28nGDzD1lWwWSsqTIue1TNxDSzDTKvEg20aQ7F1lhSVCvOAksmqjwG9Y1iOaZYOS8bQSD4POa8WP55bSlG7HUxjUzTmrWu5S1EYReswmljWnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N_jnDpGqiZkUc9aFpVXlQkZ9tcO1w8Wqbg0Ecqw1eoHblGaneJRPu43Q5q8I9EeQkzcUocVSQdVJI-FCs447ks1zvJ7_l6zzaYYwUfhNACN7_njHVyP6jfdurp2RJXjIU7wTzK93zYJmTYZkxupfo4SkUzfFZYOYmn1YGdDsIJSC8OzTjv3QYrE8UHKNhJfK_NthY4Bd23WsMdoTEk6BcKL82tIaJW4Eh6im-IYLNedGv4OJn5diVbwG4QIElzPBNi2i29ZJ5icjepqYANIQIUxHYJXEnbdiot-_c8xJK-kmYJ0IQSNdixqvkmwdc1DzWhC-n08FEWWvWOqVOu7Gew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R8anTp9_IQQzXI-HgRCOH1M3M2ADcZvjXPT4GfN5VfGLX8qArfP7qc5b1fd45cUb9-bE9AzCK877ZKe7htHg997wPSh9AvWanSeMAewspoaTFj2y-8VPvTtAW3-Zhr7oi97ZvFq1mJ59oCQClw-gyFOx4AdOB0tCU9dSOTLq56_8KNPkVwHasDwmjOVsPk_PvXJFPgKYEdakuaHCLu9ZiiIKQen_OV2N9tr-5FXooJaFPcz37nN9RsaBr2k_unS87VTuvNftyMkZMk9aR0GELkhHUj4YlYjZuA3u1ciwaBoRhBWl_p6wH3eXmSO0yo_HPUSrX7aX5UfAbNHoPjK8Cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر هوایی حوزه هنری انقلاب اسلامی از تشییع باشکوه پیکر مطهر رهبر شهید در مشهد.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/448785" target="_blank">📅 20:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448784">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک ملی ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqjSFpMqyOBsAevkKyD2Zs9wRH_qSDwY4lb_OjYjN9dfvbiGQPBoLhLo9t1EvvVBXemGb33TLZrpWISShlY45S9C-h49HuVEk3IbOW4JiLEH4uLApFhWaGXRtNRbJ6dQgXO30agtrR0bIC-gq8sREP_6UCUmtuaERvfCuGNl58LumJNZ2jlQNzcUFEQIUfmOo4DZ0InJrC1bgd0rx8GjzXtwMkgPnfYadnvuB-W64o9A1Gro8hSMAuHVmQcjcQAaLuuQ765TZhRVrCQwYoxqAoV6l3yb_z8xHzBvakYNBILyEaScwwCFzs06rlh8iuzBP2d7GvQwn1f1fzec7cdJNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔖
واریز سود سپرده‌های بلندمدت، فعال‌سازی خدمات چک و امکان مشاهده مانده حساب در بام؛ تداوم بازگشت خدمات بانک ملی ایران
آخرین خدمات فعال‌شده را در ادامه مشاهده کنید
⬇️
✅
واریز سود سپرده‌های بلندمدت
✅
مشاهده مانده حساب در بام
✅
سامانه چکاوک
✅
رفع محدودیت مبلغ استفاده از رمز دوم ثابت
✅
صدور کارت جدید برای حساب‌های واجد شرایط
✅
انتقال وجه از حساب‌های فاقد کارت در بام
✅
مشاهده صورت‌حساب در بام و شعب
(از ۱۱ تیر)
✅
وصول چک‌های صادره بانک ملی ایران
(در صورت وجود موجودی کافی)
روند بازگشت خدمات بانک ملی ایران ادامه دارد
🔹
🔗
مشروح خبر...
@bankmelli_ir
| بانک‌ ملی ‌ایران
🌟</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/448784" target="_blank">📅 20:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448783">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/448783" target="_blank">📅 20:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448782">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ef055869d.mp4?token=NEruy2NVF3o-Ym9-nctzleapVbOMMAvKieDzAcoGZRVazuCifHg9TveuTZxxFdGv3jWt04aqetshKWbmYuajpEkZWJ73ASwIWDwQJBczN-d3MPbZzX0C1zhq8ju5-bEYr31YGVHHoCUFRh42Lk8EHjKi4UjAijpE-iVZBiD4O_oPxK9c9utLQ-K7BUeM77O_f0_N3_ZKH2JGOC1Ffd1we4MLawNw1mbzL09oShzUFw5BP5gDcBecdcZusVaJCvU-T5vm3ao9lU2RhMSXMR5mNws_x0NQ5GfmPnHFowflxD7SQ9HXxPSKFUm3dGxWUeaT6iEUOv6eiZ5TUhD52Hx9hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ef055869d.mp4?token=NEruy2NVF3o-Ym9-nctzleapVbOMMAvKieDzAcoGZRVazuCifHg9TveuTZxxFdGv3jWt04aqetshKWbmYuajpEkZWJ73ASwIWDwQJBczN-d3MPbZzX0C1zhq8ju5-bEYr31YGVHHoCUFRh42Lk8EHjKi4UjAijpE-iVZBiD4O_oPxK9c9utLQ-K7BUeM77O_f0_N3_ZKH2JGOC1Ffd1we4MLawNw1mbzL09oShzUFw5BP5gDcBecdcZusVaJCvU-T5vm3ao9lU2RhMSXMR5mNws_x0NQ5GfmPnHFowflxD7SQ9HXxPSKFUm3dGxWUeaT6iEUOv6eiZ5TUhD52Hx9hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مردم در حرم امام رضا(ع): این همه لشکر آمده به عشق رهبر آمده.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/448782" target="_blank">📅 20:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448781">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تردد قطارهای مسیر تهران-مشهد متوقف شد
🔹
راه‌آهن: به‌دنبال حملۀ جنایتکارانه دشمن صهیونیستی آمریکایی بامداد امروز به یکی از ‌نقاط مسیر ریلی تهران-مشهد، حرکت قطارهای مسافری در این مسیر با وقفه مواجه شده است.
🔹
تیم‌های فنی و عملیاتی راه‌آهن بلافاصله به محل اعزام…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/448781" target="_blank">📅 20:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448780">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">امشب برای آقای شهیدمان نماز لیلةالدفن بخوانیم
🔹
روش خواندن نماز لیلة‌الدفن به این صورت است که در رکعت اول سوره حمد و آية‌الکرسی و در رکعت دوم سوره حمد و ده مرتبه سوره قدر می‌خواند و بعد از نماز می‌گويد:
🔹
«اَللّهُمَّ صَلِّ عَلی مُحَمَّدٍ وَ آلِ مُحَمَّدٍ وَ…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/448780" target="_blank">📅 20:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448779">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3XvhU5LoPzHXsXmcyW4sZqf74a94RJC-Et7dh1eDhxJ2AwNoMj5wFzXkoeKpEYMKAF7Onoaxocp9gkN84o7BjAGz10CgWXqv5kDsKpuy0NuvXDcHJQBhYReDQNInj1J4PnOREuhaaeYZvw5cE8F7K8pY2q7okip7yLXxVoYhtvWs5r3OJRklKlsILcqt0bFByjSIp7TXNH7jMRnoJpWJs6tVRcCAeH2flz6AJE5SYjcXXikdpMgkz_z2RPlYBh5se3Msu5VncQNwgd_hmDabBD9pAUSbRW0Almkd02AERf0oCsm2atOfee0ywdgLSbq26B8AnfWUmBcAflYueaiww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
رهبر شهید انقلاب اینجا دفن می‌شوند؛ رواق دارالذکر حرم امام رضا(ع)  @Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/448779" target="_blank">📅 20:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448778">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d99ff886c9.mp4?token=r_H3Dpt0flV-MRTDLkQ3xiIvtkEotgOZeA0sz8YoPPChNnJ2y82whpZeEjxzdj_3Yo9u2-FUU2SGqtAB7ax61SdAJaPovRAEclYZP7AIxU9nFnMH-WycrV0l8KXNaG_UaQtRI54etjTbr0rmF-e4hOjj18WIQvOiGVcyjHlRpXUABWHhhGdwNOckZafjjcy2mGZVWU0FecqfNXi0O1W03vlinss_qpQk3LxGxwB42pLeueYpdqPueXxu8sPrOgxP70ZXARofHrgtsaivSori-VefxYCgHFfEnfuDXEMiAXw1seFe4DBrpLPR5oswj1SUfFqfF10wR047yMxiP5pHbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d99ff886c9.mp4?token=r_H3Dpt0flV-MRTDLkQ3xiIvtkEotgOZeA0sz8YoPPChNnJ2y82whpZeEjxzdj_3Yo9u2-FUU2SGqtAB7ax61SdAJaPovRAEclYZP7AIxU9nFnMH-WycrV0l8KXNaG_UaQtRI54etjTbr0rmF-e4hOjj18WIQvOiGVcyjHlRpXUABWHhhGdwNOckZafjjcy2mGZVWU0FecqfNXi0O1W03vlinss_qpQk3LxGxwB42pLeueYpdqPueXxu8sPrOgxP70ZXARofHrgtsaivSori-VefxYCgHFfEnfuDXEMiAXw1seFe4DBrpLPR5oswj1SUfFqfF10wR047yMxiP5pHbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زیارت امین‌الله توسط بنی‌فاطمه قبل از شروع نماز بر پیکر امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/448778" target="_blank">📅 20:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448777">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcc86d82c8.mp4?token=ZDr-CRa8LxVdqE8jUjNz1GUonIbKlBgfkw1weBdMajJPS5tCIUZ2j0mxebMK6VTgxu47TFZY50B_LxFyGMZj6389bvOKUQ10jewje2l6z4kvce1yHBDBrQZEBt8_iFgZ8xaVfeZByxFkx6C6mlyy_rKCjF2uh4NX-aie5jzIgNeut3BJyBlBFwmIWFRs8kt95MdT_I4-LFVH1p0e2WKGtVMkwVW-NQcNXZW0OqjC-CL36EcCewGq4XhaH9Em2N9l7wkhEdlVEOCJ6ClGed_EhTS1dgDJWb8Djzg6rPTV7I0PTR0ijYUOLxkbH-bYAxKNPdAUZJr9V8ZYgJCUqNNbUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcc86d82c8.mp4?token=ZDr-CRa8LxVdqE8jUjNz1GUonIbKlBgfkw1weBdMajJPS5tCIUZ2j0mxebMK6VTgxu47TFZY50B_LxFyGMZj6389bvOKUQ10jewje2l6z4kvce1yHBDBrQZEBt8_iFgZ8xaVfeZByxFkx6C6mlyy_rKCjF2uh4NX-aie5jzIgNeut3BJyBlBFwmIWFRs8kt95MdT_I4-LFVH1p0e2WKGtVMkwVW-NQcNXZW0OqjC-CL36EcCewGq4XhaH9Em2N9l7wkhEdlVEOCJ6ClGed_EhTS1dgDJWb8Djzg6rPTV7I0PTR0ijYUOLxkbH-bYAxKNPdAUZJr9V8ZYgJCUqNNbUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دختری که آقا را با بغض تعریف کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/448777" target="_blank">📅 20:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448776">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnLby3c_pG4ysfqZBxZqib__RGsMOC7-LNQijR2zaXrUFfLdg-U0rOJJHS_Cqg8P-GGWT_BqnBog_yWTrNL8JQTdy37jL--pFFbxNSWDwPA8z38mOKlaULYqg_EklRWtEpK-bfA5h1nl23MAUHFYlQfKvE7gnTs6Htp-oSjow1j6GTfEtAgEB9g3tA1NGQKhYt3w36QW6DpsLmtsFge20yDGSETTuMQSVKPp5th9NiR8R-4konVL4_xS0-myAAW5KPj5eEKhRhE56y7PnaZgk2aX6Exa-w_qMK7qSghcggpgoqkC_vpd38J0dJa-L3Oley90mni9c_DMWfI2kPL-wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ما همه خون‌خواه توییم خامنه‌ای...
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/448776" target="_blank">📅 19:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448775">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1280170218.mp4?token=r1QK8v2n1QJVNey6e67h9c_ux40Bd2iGdW41pAdEBe9_RhZepJznfVizV_CuPoPJghcfQP4BWuGokC98RfOJI94ZD_bIFaHIaYo1OxvCPHWVsMYeWENE60vuUnnEACaMI0CkyWgTqkS3_yKxryj0tMQXgx6-WkWQ85Tny-ufksfLnhqxUIzTalbOJ-m1vO-8TnnFHHfq8YsnaW1AFE9zSjceKTOiIzAVr5jnm_mT7RIifaIXTei5IO0PRmgOJOKCa0xJk1LgpiMZDYrLyLeUxabZBJo89bE5YAYgHSR2cONecPJJEUK2DBRG70cyFjnORuPek3ddnbesDXQZe7AwVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1280170218.mp4?token=r1QK8v2n1QJVNey6e67h9c_ux40Bd2iGdW41pAdEBe9_RhZepJznfVizV_CuPoPJghcfQP4BWuGokC98RfOJI94ZD_bIFaHIaYo1OxvCPHWVsMYeWENE60vuUnnEACaMI0CkyWgTqkS3_yKxryj0tMQXgx6-WkWQ85Tny-ufksfLnhqxUIzTalbOJ-m1vO-8TnnFHHfq8YsnaW1AFE9zSjceKTOiIzAVr5jnm_mT7RIifaIXTei5IO0PRmgOJOKCa0xJk1LgpiMZDYrLyLeUxabZBJo89bE5YAYgHSR2cONecPJJEUK2DBRG70cyFjnORuPek3ddnbesDXQZe7AwVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید انقلاب اینجا دفن می‌شوند؛ رواق دارالذکر حرم امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/448775" target="_blank">📅 19:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448774">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe69692a2.mp4?token=hGfpaVPssdSn4wq8cYyI_MDj8I4SiPnfNtiJkRHYr6njy3e5V9XA6bk3Ay3_7j1bb1IAwpB4nyOd_pNsbfDrYEvwEiW8pY4PosTt8lyTBESQq_HoKo1RmBnoIhCmjwia7HHGoR3ct0bY5hvtEJl4bL4w0LlBFrjKzwgoOfn6IzEaTrm9r-iPJsClyoX24NgqeDQ4RmD3D9k9dJYNy78eq0zXSyJvwNrQHkURP1II3Z_l4ocZssVZ-UkvFJ6viLwP0Is5VSK4n_jZoud6PByengBmFMEUoSqEIk91Yr9WJx1PpTiHSfOmjpqW6LL2yRaMJvUoQCYVyNMDVgdVv6qofZGh9YOx35HHLUYhbrJhIIfDAYgNs2aGZtQpVvj9R5xGwjJ_HCh_H9G72TleFU_Ne9L14XOnh09ZMeo81BOaBNq3D4TZY-6XziEbmzzrLx_KzMzjkRuDPU2kYSt7BpmVFtp802ANql0Ku-fPY4Jalj6QkttuAiBDmPMxvdkxaca2QWh-7w8-6t2FmuilDJGuLKfiESFkEFUA-UUYdsWt8pMRDSSjCXxhm1FWLKrUBDCWE-KBjgB27pJOA63LK4JtZ0wkAuTyypOVhKy6JauF2PCVxLNGaGH9w_j-wFh5YsI7enc--W9Jat69L7UNEnsH1OzQFASxyousLE_Bf8URSdY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe69692a2.mp4?token=hGfpaVPssdSn4wq8cYyI_MDj8I4SiPnfNtiJkRHYr6njy3e5V9XA6bk3Ay3_7j1bb1IAwpB4nyOd_pNsbfDrYEvwEiW8pY4PosTt8lyTBESQq_HoKo1RmBnoIhCmjwia7HHGoR3ct0bY5hvtEJl4bL4w0LlBFrjKzwgoOfn6IzEaTrm9r-iPJsClyoX24NgqeDQ4RmD3D9k9dJYNy78eq0zXSyJvwNrQHkURP1II3Z_l4ocZssVZ-UkvFJ6viLwP0Is5VSK4n_jZoud6PByengBmFMEUoSqEIk91Yr9WJx1PpTiHSfOmjpqW6LL2yRaMJvUoQCYVyNMDVgdVv6qofZGh9YOx35HHLUYhbrJhIIfDAYgNs2aGZtQpVvj9R5xGwjJ_HCh_H9G72TleFU_Ne9L14XOnh09ZMeo81BOaBNq3D4TZY-6XziEbmzzrLx_KzMzjkRuDPU2kYSt7BpmVFtp802ANql0Ku-fPY4Jalj6QkttuAiBDmPMxvdkxaca2QWh-7w8-6t2FmuilDJGuLKfiESFkEFUA-UUYdsWt8pMRDSSjCXxhm1FWLKrUBDCWE-KBjgB27pJOA63LK4JtZ0wkAuTyypOVhKy6JauF2PCVxLNGaGH9w_j-wFh5YsI7enc--W9Jat69L7UNEnsH1OzQFASxyousLE_Bf8URSdY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این پرچم‌ها نماد خون‌خواهی است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/448774" target="_blank">📅 19:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448772">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ردپای عربستان، امارات و قطر در حملات اخیر به زیرساخت‌های ایران
🔹
داده‌های وبسایت‌های اوسینت و مراکز هوانوردی از حمایت‌های متعدد جنگنده‌های آمریکایی توسط پایگاه‌هایی در کشورهای امارات، قطر و عربستان خبر می‌دهند.
🔹
برخی منابع خبری  مدعی شدند سوخت‌رسان‌های اماراتی در حملات بامداد چهارشنبه آمریکا به بنادر ایرانی کمک کرده‌اند؛ داده‌های رصد ناوبری هوایی حضور دو هواپیمای تانکر حمل‌ونقل چندمنظوره (MRTT) در عملیات هوایی علیه ایران را تأیید کردند.
🔹
این هواپیماها توسط امارات متحده عربی اداره می‌شوند اما تا این لحظه امارات این اقدام خصمانه را رد یا تأیید نکرده است.
🔹
ایران در جنگ رمضان چندین فروند سوخت‌رسان و یک فروند آواکس آمریکایی مستقر در پایگاه الخرج عربستان سعودی را منهدم کرد.
🔹
مرکز ناوبری فلایت‌رادار، فعالیت هواپیماهای سوخت‌رسان از مبدأ پایگاه العدید قطر در حمله بامداد پنجشنبه آمریکا به ایران را تأیید کرد.
🔹
پیگیری خبرنگار دفاعی و امنیتی فارس از منابع نظامی نیز حمایت لجستیکی قطر، امارات، اردن و عربستان از پروازهای متعدد جنگنده‌های آمریکایی را تأیید می‌کند.
🔹
پایگاه‌های آمریکا در این کشورها در حملات ۴۸ ساعت اخیر مورد استفاده قرار گرفتند.
🔹
آمریکا بامداد پنجشنبه حداقل سه زیرساخت مرتبط با راه‌آهن و صنایع نفت ایران در شمال شرق و جنوب کشور را مورد حمله قرار داد. حملات به زیرساخت‌های فرودگاهی در چابهار و قایق‌های صیادی در عسلویه از دیگر اقدامات تنش‌زای آمریکا در نقض فاحش تفاهمنامه اسلام‌آباد است.
🔹
عبدالرضا صدیق، کارشناس حوزه امنیتی می‌گوید آمریکا با هدف قرار دادن زیرساخت مهم تجاری با چین، خط قرمز بزرگی را رد کرده است.
🔹
قرارگاه مرکزی خاتم‌الانبیا چهارشنبه شب اعلام کرد مبدأ هرگونه پشتیبانی از ارتش متجاوز آمریکا برای تجاوز به حاکمیت و سرزمین ایران اسلامی، هدف مشروع نیروهای مسلح ایران خواهد بود.
🔹
ایران پیش از جنگ رمضان نیز به‌طور مکتوب به سران کشورهای حاشیه خلیج فارس اعلام کرد مبدأ حملات به کشور خود را هدف قرار خواهد داد و این وعده را عملی کرد.
🔹
رضایی، سخنگوی کمیسیون امنیت ملی مجلس معتقد است با توجه به اعلام قبلی ستاد کل نیروهای مسلح، زیرساخت‌های ترابری دریایی، ریلی، فرودگاهی و زیرساخت‌های حوزه نفت و گاز در کشورهای عربستان، کویت، امارات، قطر، اردن و بحرین به عنوان ایالت پنجاه‌ویکم ایالات‌متحده هدف مشروع ایران برای پاسخ به حملات ۴۸ ساعت گذشته آمریکا به زیرساخت‌های کشور خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/448772" target="_blank">📅 19:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448771">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E95pPLGVa5orc_UKIwwj_KUjHtxgcQ3g9UYGdAAtqJQkN768CdquIYY2a_oPK-u4UtY6Vevyo9Xa6JiP2mIwSl_8SLPq7QLNnGAv0iyAnxCJe8drnxHCFzxy7M3SbYQaS_z5vtPSPXWkhIOKgBo8aIq8brsy72oWmBV1Se3J4Y15xh4Wcm-OPzLFhfUL5_CzkKUGJ1WUVRjMCb3S2rbNfKrsWgU5fbhJjSAak6GZZounR_FrUBsq0bKGzfp7c2hkY7jpjO2tcNgT-1jWiIpBUwvxrWfIe-3zN2KpF4aOx-O3F-QDakoaspuVei8T0cN9UGNrofG_nLAdfpofP_RtfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
یاد آن مشت‌ گره کرده...
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/448771" target="_blank">📅 19:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448770">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01cfcf412d.mp4?token=Wm10ema39au6t8aSa5C7R49C38p_PE-nXZI-hGTx3NjsFHu0CElau_f_2gLnL7jdVBjRpXWLQJnrqoFdRvDGPm_KQvx4hXz9D-4oA9NRTNfqTmehqd3hV8p8Fm4zI1zrslOZbw4YUfGbFHTNXlbZ1mgOwmadrRjCP7iL-Z-ggS3RpRDnhFLk4wI0XDow4MVz7QND91QUThfFBlksaatTxmTnBnU6XrBRTkP0Ke1MCLm5gKVMD4dQn96hMr5q9hQeUvtH9ePO7URX7a-aLMqQDX6nfMUoMevU-1x-U-NIi_p8LWHHirnBzSsd5aEeShcwg41jvRBy6wJESAxbvJGaWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01cfcf412d.mp4?token=Wm10ema39au6t8aSa5C7R49C38p_PE-nXZI-hGTx3NjsFHu0CElau_f_2gLnL7jdVBjRpXWLQJnrqoFdRvDGPm_KQvx4hXz9D-4oA9NRTNfqTmehqd3hV8p8Fm4zI1zrslOZbw4YUfGbFHTNXlbZ1mgOwmadrRjCP7iL-Z-ggS3RpRDnhFLk4wI0XDow4MVz7QND91QUThfFBlksaatTxmTnBnU6XrBRTkP0Ke1MCLm5gKVMD4dQn96hMr5q9hQeUvtH9ePO7URX7a-aLMqQDX6nfMUoMevU-1x-U-NIi_p8LWHHirnBzSsd5aEeShcwg41jvRBy6wJESAxbvJGaWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ای جهان از دادِ «حیدر حیدر» شیعه بترس
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/448770" target="_blank">📅 19:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448769">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02f558405c.mp4?token=nUOd-rW9qfh7rfnhmMvKi4aNxRCo4-q5lhpK-s_WM2-N79Z6HkBPmC64xzS14eVuWuZ014RfKRzUkzvk_3xEl39nXBAz_kiS8DdFgOMPhHepGovVaEQE_rTBlWzVV4P4_qni7WI5E3qM_DFzsXFkRwQUTzZ017Qvj8xSNUEGl3Iblj_BLEdaAmdczvWMhitZVUErs7dmdFbjgdaYZfBq3Di_THcVpZefr0sRdeZ12ierW3h2rlS-prcK0Cfj6EtnQ_-wqZst45oJaX1cEbLvaHfh45n429PNksgfHo29wKXGtUChFC9kWaUB-hoGrlgJrFRCcQ7a-UrJt7rqn6Dw9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02f558405c.mp4?token=nUOd-rW9qfh7rfnhmMvKi4aNxRCo4-q5lhpK-s_WM2-N79Z6HkBPmC64xzS14eVuWuZ014RfKRzUkzvk_3xEl39nXBAz_kiS8DdFgOMPhHepGovVaEQE_rTBlWzVV4P4_qni7WI5E3qM_DFzsXFkRwQUTzZ017Qvj8xSNUEGl3Iblj_BLEdaAmdczvWMhitZVUErs7dmdFbjgdaYZfBq3Di_THcVpZefr0sRdeZ12ierW3h2rlS-prcK0Cfj6EtnQ_-wqZst45oJaX1cEbLvaHfh45n429PNksgfHo29wKXGtUChFC9kWaUB-hoGrlgJrFRCcQ7a-UrJt7rqn6Dw9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غم‌انگیزترین اذان مغرب در فضای حرم مطهر رضوی طنین‌انداز شد
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/448769" target="_blank">📅 19:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448768">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51aa105312.mp4?token=TDrzYROODFOQbD1JDHFoXFY9BQBVVhmCxsfo9ZWaUlqRjct7FsA9Ds9JSMwKsd-FLqziJYU1vQmkzg-CBU-zL5GTThUxD4IUXpIpbW0Hl1cm6iUyDQlPEHrqovN2NlLb-GikYb0WE1CFpuYoG9Twp467jJJMzCPlHkdBmF_TU_BOnVAMzDrrs6NVnO4nuTOjQZhuUhcLDluXktHM6x2_CNjXVSHOc8KeIsRg0Qdf9SikVNtdvVcqC7XADLJy5D0ZvGOGB7GYP2A4qUxLhurOq1ZXZCDpp-zukj8joCry4qdHJuhi1HaOh8nnW7k8xCsTx8TPS8-wb6Od-0oH_eG9XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51aa105312.mp4?token=TDrzYROODFOQbD1JDHFoXFY9BQBVVhmCxsfo9ZWaUlqRjct7FsA9Ds9JSMwKsd-FLqziJYU1vQmkzg-CBU-zL5GTThUxD4IUXpIpbW0Hl1cm6iUyDQlPEHrqovN2NlLb-GikYb0WE1CFpuYoG9Twp467jJJMzCPlHkdBmF_TU_BOnVAMzDrrs6NVnO4nuTOjQZhuUhcLDluXktHM6x2_CNjXVSHOc8KeIsRg0Qdf9SikVNtdvVcqC7XADLJy5D0ZvGOGB7GYP2A4qUxLhurOq1ZXZCDpp-zukj8joCry4qdHJuhi1HaOh8nnW7k8xCsTx8TPS8-wb6Od-0oH_eG9XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این غروب حرم امام رضا(ع) فرق می‌کند
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/448768" target="_blank">📅 19:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448767">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a61f3dd23.mp4?token=EmyIeTI_b8WhTeTO48iEGqT_PSvbyc9hdqzF_wkEkJ_F696UCN0hJrW0aLvRgTCiC6rAJCnu1l6QnNt6ni5houORhgrDjhtUViGoCdEbzSvv-heV1XtkUWgzF0jD_do7d0ijMb54wShoUUbc0FA7dgLXWRdSNW-S_ql_hOu6S-JNkXTl_nWZa2LDTnOUmjiC8oyD4Rr_egAjZRZIYchI808ZeeCxauO7nd3zLQskk9a-F_ApBbxKBo3XW3UJ7caFXgGBXnOEcZmTkCrncudW89VL8Nvu6-XPeSHyR0y9RdzpMXwj6u1S0ma206WXgsBdKJF_h1hXcLg5KX9zpEuKVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a61f3dd23.mp4?token=EmyIeTI_b8WhTeTO48iEGqT_PSvbyc9hdqzF_wkEkJ_F696UCN0hJrW0aLvRgTCiC6rAJCnu1l6QnNt6ni5houORhgrDjhtUViGoCdEbzSvv-heV1XtkUWgzF0jD_do7d0ijMb54wShoUUbc0FA7dgLXWRdSNW-S_ql_hOu6S-JNkXTl_nWZa2LDTnOUmjiC8oyD4Rr_egAjZRZIYchI808ZeeCxauO7nd3zLQskk9a-F_ApBbxKBo3XW3UJ7caFXgGBXnOEcZmTkCrncudW89VL8Nvu6-XPeSHyR0y9RdzpMXwj6u1S0ma206WXgsBdKJF_h1hXcLg5KX9zpEuKVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انبوه جمعیت در کوچه‌ای که به خیابان امام رضا(ع) می‌رسد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/448767" target="_blank">📅 19:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448766">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0388f0078.mp4?token=SxgZqEACS5pLwoMofOxuG14dsOgjl8ZeK2spdo0QDbJFxzcRPGMTKaX9-pb2po7FBGQLuBFP4hLUBEanjf5NepGs8QLpTj5L1b9vlgZCXg82hG_jx8rMFCYViEFFiG3g8LrrbFX331Q7KFk1LusN3LG3RdNHH93PbEABD-SR9wkqFzNhL7Xw3xAf9KBIBDuxaOLC74A2EB2wJh9rXmviNP3p3q3frXZsRdUn5cyxmQpEOioDwz4b7XGVlsMm6pUapLp_jiho_3F8dm_MycEfV2F2tWQF095i2VX-Ayp2e9M2SK-_-N0TIG2I12ZFfg0DM0iszgWh1_f_1SMYZWRg_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0388f0078.mp4?token=SxgZqEACS5pLwoMofOxuG14dsOgjl8ZeK2spdo0QDbJFxzcRPGMTKaX9-pb2po7FBGQLuBFP4hLUBEanjf5NepGs8QLpTj5L1b9vlgZCXg82hG_jx8rMFCYViEFFiG3g8LrrbFX331Q7KFk1LusN3LG3RdNHH93PbEABD-SR9wkqFzNhL7Xw3xAf9KBIBDuxaOLC74A2EB2wJh9rXmviNP3p3q3frXZsRdUn5cyxmQpEOioDwz4b7XGVlsMm6pUapLp_jiho_3F8dm_MycEfV2F2tWQF095i2VX-Ayp2e9M2SK-_-N0TIG2I12ZFfg0DM0iszgWh1_f_1SMYZWRg_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سلام ای زائر شهید، مشهد به این‌گونه آمدنت عادت ندارد
🔹
حال‌وهوای خاصِ کنترلر مراقبت پرواز فرودگاه مشهد هنگام ورود هواپیمای حامل پیکر مطهر آقای شهید ایران.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/448766" target="_blank">📅 19:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448765">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73a592d33.mp4?token=XtR1lJffqgdD-wTCWrgHD_SpXddKiQrAIbP1wuPxT-4kcCvzf2uk6pVb7-qZgo6wWXeDU0HwhXeSN2_QtfALfVgyIuHC7igSiwLXqueLiWwwuxDcwYgnKCBZmUAxkCl3VNfUl7TWuFtcROcggyFWn9jGrs3yCHSmzJIbK93g1lNi7ISa64XE4lZQXbQMlWyScs8pH-1NcdmBIXOYwxOCJ3Ox7-6CxZ4U7SdG5bTn4ZuuFWkyowpdgi306Y8MjMwTZQ08hIYq_KtZattCJVI4qUfHMkls-K0nQubML-diY6D1lz3ndvY9XdSv9AQjocuHqBeNrADOQ57R7Rm_XnQkeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73a592d33.mp4?token=XtR1lJffqgdD-wTCWrgHD_SpXddKiQrAIbP1wuPxT-4kcCvzf2uk6pVb7-qZgo6wWXeDU0HwhXeSN2_QtfALfVgyIuHC7igSiwLXqueLiWwwuxDcwYgnKCBZmUAxkCl3VNfUl7TWuFtcROcggyFWn9jGrs3yCHSmzJIbK93g1lNi7ISa64XE4lZQXbQMlWyScs8pH-1NcdmBIXOYwxOCJ3Ox7-6CxZ4U7SdG5bTn4ZuuFWkyowpdgi306Y8MjMwTZQ08hIYq_KtZattCJVI4qUfHMkls-K0nQubML-diY6D1lz3ndvY9XdSv9AQjocuHqBeNrADOQ57R7Rm_XnQkeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مردم در حرم امام رضا(ع): نه سازش، نه تسلیم، انتقام انتقام
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/448765" target="_blank">📅 19:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448764">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a14e34a0.mp4?token=u3BLRbykJwNTHPeegnS6YKSPFrqfQAp0eTQN043JQDY7gWXPuiCMgP4ZVeiIWdIkbJLlN0_ihKQn5VD3TOYnqtklTz0-1FY4T0aDBuIBU7O5ak5-X6dE_OtxnIAXjJm55csFAzieCzYBGpXWu-c-J8b23CsvQty82UHuA7agrVRg52pyWN1k2is_8rELNP0Zn-3qY1BuUe160BXWvUbm5a7uVfHyupspVdza47MiYftUy_hyOWUnqN6sTVFonrzd3xy2gx9ypUhD1TOmaNB9g6TvetVHaMmDqeDmx_WguAglusX06z7XJEer-RPq67iDTNvGaa3VrAZo31sEDCfbQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a14e34a0.mp4?token=u3BLRbykJwNTHPeegnS6YKSPFrqfQAp0eTQN043JQDY7gWXPuiCMgP4ZVeiIWdIkbJLlN0_ihKQn5VD3TOYnqtklTz0-1FY4T0aDBuIBU7O5ak5-X6dE_OtxnIAXjJm55csFAzieCzYBGpXWu-c-J8b23CsvQty82UHuA7agrVRg52pyWN1k2is_8rELNP0Zn-3qY1BuUe160BXWvUbm5a7uVfHyupspVdza47MiYftUy_hyOWUnqN6sTVFonrzd3xy2gx9ypUhD1TOmaNB9g6TvetVHaMmDqeDmx_WguAglusX06z7XJEer-RPq67iDTNvGaa3VrAZo31sEDCfbQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ای اهل حرم میر و علمدار نیامد
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/448764" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448763">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">چه زمانی امکان زیارت مزار رهبر شهید انقلاب فراهم می‌شود؟
🔹
استاندار خراسان‌رضوی: امیدواریم از فردا حوالی ساعت ۱۰ تا ۱۱ صبح محدودیت‌های حرم برداشته شود و زائران بتوانند به زیارت مشرف شوند.
🔹
به نظر می‌رسد از ظهر جمعه، مقدمات زیارت مردم از محل تدفین فراهم شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/448763" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448762">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvcaIJ4bsQuF_DVUmofOtOrXDTlGX9tnEoaDz815YbJmtSuQtUi-7e9ndUMILfC8l6RLzk-dCFYRSc3Jc3v4o1NzmLJmd09KriSvFLQ8qeWItJDaYjaH3tYZtLjjneGllKhbn4QTJPy1pwl5ossJavbNYs33ONdD-JxRZJp_287VNweoXccCV8XhNB2TPWlYfaMGajzXA9Dg-SM2wngVCquphmbBn9gibejjO0Xbfj9B5OwFKQp90V8-JWIiYOArl_ENgsQjb_J1boMAI0l8ifqnmlTc7O_xw2mv7sBtOGdB8Mo_Dyw0mwkyoUblqBeyGL6PPo8wNeXLEgocpxMUOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قابِ ماندگار در تشییع امروز
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/448762" target="_blank">📅 19:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448761">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3886daf0c.mp4?token=VGshjsRouk4bw0rGFlF9dkeUtZSWSBtQ-LbYKxKpoPa0whRLdBbXTUxLwBaVWr86_rg4EPRoLKwqpfej764ejripqr3Eean261xhzCd6VtlSkHSM9Yb5f1CRLudM8j4R_NzsRsJPyuoMvMaiAIDCMZdtSKB9O_1G12HbyArlcVeXrsXVXpHHzO2bhlEeWuKkX_xRppgzowUVytr1uOaaa_QRfprEIvfFTHEOyblNd26BjPqrifQsI9F3DEhRrGnZIP1ZaE-a_x4yIDE0WQPhjxHc8ZhdEiULA7Qey7n6F5JlgEap7H8U-YvuXEIeS4nshaEBsZv3qvwQ_-rzqG1Ahw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3886daf0c.mp4?token=VGshjsRouk4bw0rGFlF9dkeUtZSWSBtQ-LbYKxKpoPa0whRLdBbXTUxLwBaVWr86_rg4EPRoLKwqpfej764ejripqr3Eean261xhzCd6VtlSkHSM9Yb5f1CRLudM8j4R_NzsRsJPyuoMvMaiAIDCMZdtSKB9O_1G12HbyArlcVeXrsXVXpHHzO2bhlEeWuKkX_xRppgzowUVytr1uOaaa_QRfprEIvfFTHEOyblNd26BjPqrifQsI9F3DEhRrGnZIP1ZaE-a_x4yIDE0WQPhjxHc8ZhdEiULA7Qey7n6F5JlgEap7H8U-YvuXEIeS4nshaEBsZv3qvwQ_-rzqG1Ahw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ جان‌سوز وداع آمد ولی جدایی از تو ممکن نیست
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/448761" target="_blank">📅 19:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448760">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
با توجه به ازدحام جمعیت در حدفاصل چهارراه دانش تا حرم مطهر رضوی، ادامهٔ انتقال پیکر به صورت هوایی به حرم مطهر انجام خواهد شد و نماز در حرم مطهر و خیابان‌های طبرسی، شیرازی و نواب‌صفوی اقامه خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/448760" target="_blank">📅 18:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448759">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fR32wUw9rRnpklIk07aB9Ctovw_g8KX1VCfVUFxRrC0hAoQ1H1jQ6bTTYPdxuSXinX1VfRdA1rSaVwjH5zeyf5BZnD5yuYJw5ypH6KnwD4LMvxSxnuuRcgkGOLf32QcxRRWwFG6hkiwQ8uAfMdniEMizIuiCfgy5bwkqwnkHZgwVUlPuaZkY3uBlLvHH4hxq7hnlwpPQoaUBEZNj3RZya0GGwPot-AoAxQ1UQMwmTMxnTjV8N6R1A1B6qNkXqeILm1_URr8IwzNZzwr973hCITD6Am-wRJ5udmE6Xc0r0B8-zM9hwt0zHQi_2CBF6FHMSY804DH05SBi3mE9risuRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور وزیر اقتصاد در تشییع رهبر شهید در مشهد مقدس
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/448759" target="_blank">📅 18:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448758">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d68f0b36.mp4?token=e8PajLC2FrIKjFOiZMFuWmkwFIioPnS6iWy6zP_6dKFaBLRLloPjvYiduPedSt3_GvDJHEsiNlCffu-M-Bj1_-qXMQm0KuiRMjOogBROh2KTElr8jRYPOiDUsNVlTfAWFANcJLE21q3Lq7OIg21U2ozozbkzL7WMeoCGsuuRzlFwGQacNV_yndlV4611aHJ8bhtk0oSMzkgggL5kwuz_eSP36MaVcpmV8ByfHmZM10f_fB9zmW2DZltuvmI-OsNR0zNx3Zmnw-ojM-W_l70IyJ_U55q4ZznidaT1IKaTQ6YhitW9JdeDIdoX4_42-Twg8AVjC_qsOlAdRrzm1J6ikQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d68f0b36.mp4?token=e8PajLC2FrIKjFOiZMFuWmkwFIioPnS6iWy6zP_6dKFaBLRLloPjvYiduPedSt3_GvDJHEsiNlCffu-M-Bj1_-qXMQm0KuiRMjOogBROh2KTElr8jRYPOiDUsNVlTfAWFANcJLE21q3Lq7OIg21U2ozozbkzL7WMeoCGsuuRzlFwGQacNV_yndlV4611aHJ8bhtk0oSMzkgggL5kwuz_eSP36MaVcpmV8ByfHmZM10f_fB9zmW2DZltuvmI-OsNR0zNx3Zmnw-ojM-W_l70IyJ_U55q4ZznidaT1IKaTQ6YhitW9JdeDIdoX4_42-Twg8AVjC_qsOlAdRrzm1J6ikQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرواز تهران-قشم-تهران امروز انجام شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/448758" target="_blank">📅 18:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448757">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">عراقچی در گفت‌وگو با فرمانده ارتش پاکستان: لفاظی‌ها و اذعان مقامات آمریکایی به عدم پایبندی به یادداشت تفاهم نشانه‌ای آشکار از پیمان‌شکنی است
🔹
عراقچی همچنین با هشدار نسبت به هرگونه ماجراجویی ارتش آمریکا، بر عزم و اراده راسخ ملت ایران و نیروهای مسلح غیور جمهوری اسلامی ایران برای دفاع از حاکمیت، تمامیت سرزمینی و امنیت ملی کشور تأکید کرد.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/448757" target="_blank">📅 18:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448756">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSWtne6n7wh4QLuL8bthsLMTL5rWPZ4YJqPKaRQ97BOA5pvmbwd5_aLaRLSbfNrrIg1gbXwQJ5Osn4ceKxu10Pqcgplna97P2aS1r8x82ItpuEDzUOkYlNyy45cW4DhGh-TbJmWlS9xDewMeuWGA3QrD-92i7qMffYov005CmvNFO0JGnd7bS4oNoAW46dNkf1P5y2WYtBQV0lBJp4uXrtf6xCMcdJLp6iMNnhEWe8cpkk8yNNXpt8i0ZAu0F5kyfXkRf4hI6NSQYAXg7sGeVHfPFydJTcI279Mp98svzONqnF4xSjHVly_ySFRu-NGrFCcmNFQxXog3CxKr-e8txg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ باز هم بنزین را در آمریکا گران کرد
🔹
انجمن خودروسازان آمریکا می‌گوید که متوسط قیمت بنزین در این کشور به بالاترین رقم در ۲ ماه گذشته رسیده است.
🔹
تنش‌هایی که آمریکا در تنگهٔ هرمز ایجاد کرده، قیمت نفت را هم دیروز تا ۸۰ دلار در هر بشکه بالا برد و تردد کشتی‌ها در هرمز را باز هم متوقف کرد.
🔹
حالا درحالی‌که ذخایر راهبردی نفت آمریکا هم هر هفته رکورد کاهشی جدیدی می‌زند، قیمت هر گالن بنزین در آمریکا ۳.۸۵ دلار شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/448756" target="_blank">📅 18:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448755">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205fd5823d.mp4?token=FzWFsr7goQrBtKGvdDLhBPbCMDUKKNfaY_RgpkH36QvQnwPjQZvo4yEYdQrFBivHKLOVX8qvLuTFw82vpAtfgrI439Q8xZLeniGOTlr7EP1VC14aj6jQmwuu6t7w86bTJXzsIzBl2uQaur3St8SMxWHH0-1k44Du2IqPLqQn9BMtLo0N4A0F4bJ0tpFUhs2u-Bj_5Y7XF_8pUEGRnHBEXotJ7CPpRpzxqqbVt2hY2T74tFBxwwY_Pev-kQyp3m5YEXiHEn1aCEvZpKJO_ok31FVZEL6jmKqJ8AHM4LPIeAxUlQKuk1f3HVxrNYeem1ayi489aSxz5f7cV5JZoN_oNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205fd5823d.mp4?token=FzWFsr7goQrBtKGvdDLhBPbCMDUKKNfaY_RgpkH36QvQnwPjQZvo4yEYdQrFBivHKLOVX8qvLuTFw82vpAtfgrI439Q8xZLeniGOTlr7EP1VC14aj6jQmwuu6t7w86bTJXzsIzBl2uQaur3St8SMxWHH0-1k44Du2IqPLqQn9BMtLo0N4A0F4bJ0tpFUhs2u-Bj_5Y7XF_8pUEGRnHBEXotJ7CPpRpzxqqbVt2hY2T74tFBxwwY_Pev-kQyp3m5YEXiHEn1aCEvZpKJO_ok31FVZEL6jmKqJ8AHM4LPIeAxUlQKuk1f3HVxrNYeem1ayi489aSxz5f7cV5JZoN_oNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور جلیلی در مراسم تشییع رهبر شهید در مشهد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/448755" target="_blank">📅 18:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448754">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1322afad.mp4?token=D9b2rE0IWZHfD2K11hUPg9laXbiCiL7myZDs3MCoARwK8A5tMYcNpHmvj-ZoWMbvJnys3_msjWle2D3BobMUBM8hLHCqdWk6kJCg4RZxtGty17DEX3WKgvN8iondDP1NfFLWkNHv01vSrbped46q8fjdmrVcotf-ib8l4-Icx-EBdU99yxvOB7yBolNjsfthSUYJs8ehoV5qhGJdeLFCuXoDk7rLncZOLt-rFaokSne4AUSFo0CJWaDVO8Ebffkx1MegO1d_IYnybSt3J8vOKJI1n7lB59iHZ-3Om7Q2G6kaU8c5-W-qFeknpde76qYuTkAUFtZ7DgSD9T154FoIpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1322afad.mp4?token=D9b2rE0IWZHfD2K11hUPg9laXbiCiL7myZDs3MCoARwK8A5tMYcNpHmvj-ZoWMbvJnys3_msjWle2D3BobMUBM8hLHCqdWk6kJCg4RZxtGty17DEX3WKgvN8iondDP1NfFLWkNHv01vSrbped46q8fjdmrVcotf-ib8l4-Icx-EBdU99yxvOB7yBolNjsfthSUYJs8ehoV5qhGJdeLFCuXoDk7rLncZOLt-rFaokSne4AUSFo0CJWaDVO8Ebffkx1MegO1d_IYnybSt3J8vOKJI1n7lB59iHZ-3Om7Q2G6kaU8c5-W-qFeknpde76qYuTkAUFtZ7DgSD9T154FoIpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفت‌وگو با مردم عراق در تشییع پیکر رهبر شهید در شهر نجف
🔹
امروز قسمت کوچکی از جبران ما برای جمهوری اسلامی است.
🔹
مردم عراق، شیعیان عراق و شیعیان تمام دنیا از سید علی خامنه‌ای ممنون هستند.
@Farspolitics</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/448754" target="_blank">📅 18:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448752">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bm3T4Znmq9nszcXWT-vagjttB_pVzpAW_qOche-ghQopgvC73Yk3D0g5rlzyVpcZd1quM3FRA5QiAYPbU2sm26hYc9IpxyyZZ37YSXY03myJHjHmxuP62IkOeMcqROhvZcPFm9zk0A_V5lcr_wa8EqwcHqw63bJHjC3IAolLKyM0CAcf4tfqF2C0cQOcgYykEn2_lLNuNLexLy1VJ55P4FDU0JvtQF0i4699h3WHvlsuaPjyaZjvc2YrI7oM0L0YIxwHlgzLgwVYfqzD5GljqqDD8JH4xUYuGzKvAUnNZJeqVjpO4SY8vHtCNV9QwDta1l9zsoW671i0UZChjM0NmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب برای آقای شهیدمان نماز لیلةالدفن بخوانیم
🔹
روش خواندن نماز لیلة‌الدفن به این صورت است که در رکعت اول سوره حمد و آية‌الکرسی و در رکعت دوم سوره حمد و ده مرتبه سوره قدر می‌خواند و بعد از نماز می‌گويد:
🔹
«اَللّهُمَّ صَلِّ عَلی مُحَمَّدٍ وَ آلِ مُحَمَّدٍ وَ ابْعَثْ ثَوابَها إلی قَبرِ فُلانِ بنِ فُلانْ»
🔸
(به‌جای «فلان بن فلان» اسم هر شهید و پدر ایشان گفته شود)
اسامی شهدا به همراه نام پدر:
◾️
حضرت آیت‌الله العظمی شهید سید علی حسینی خامنه‌ای، نام پدر: سید جواد
◾️
شهید مصباح الهدی باقری کنی، نام پدر: محمدباقر
◾️
شهید زهرا حداد عادل، نام پدر: غلامعلی
◾️
شهید سیده بشری حسینی خامنه‌ای، نام پدر: سید علی
◾️
شهید زهرا محمدی گلپایگانی، نام پدر: محمدجواد
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/448752" target="_blank">📅 18:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448751">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95b70af5b3.mp4?token=cvE-Zbi2wdRcji22wiGmlEKEPXGW5cANYWECrFnIxOg7iQ7JQHdQ_zeBw1DB4Q0LyvDUwQjvzugztU14sHJyB__8FVRQiLaDqeuS-PYzORpAcMVe1u7EowpooPUOUyx9sFE1TCVAZa43xRD8wXAMitDaGS8M1tRSI7Vam2nezthapXTK8fpc-M1p_9tWmOBv9PDnSArY55yhqi1DmPFu7HGrqsk298gtD9hgK0fSwEtMAPzFBAR3BjSuhUxdxJ4ZesfIoD0h2923pgS3ssvufZ9cFukulEPADl81B5g-2BYwV36yHfU_F4CiixprPSddaFTxZjdBvI8vV9wL96_IdVo3eVjp6SCGfLb0jTRB_yqJ2aczZ6ksCv1zvHeG1tZL9amXELzCVZ_m8PW8V8tn5qNFv7EQ2f7hRguI_iSArIDQWQe6mm1Bn-vWMNYwMcaLPIqu5SZB1NzNEia8hCrLP44tXNVGNN4OHhnzGCkJw-HsMZ_y31zrlJ-tDXCctN9Ddi0z8lVeNogEX_emJ5M-SBhhHvy-sapIrvuZTweiC3EedPou4_uuX5OqdxtDze9SgAS-MGwO-NXHUOC6ZjYxxORZOnRpqACHpyKg5GiTZAyyLHUJTxIomYAwg9ypK5yCel-FIj8wSJO9gZsHpvY5xv9wPaaVm-cr2YKQCN_wEA4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95b70af5b3.mp4?token=cvE-Zbi2wdRcji22wiGmlEKEPXGW5cANYWECrFnIxOg7iQ7JQHdQ_zeBw1DB4Q0LyvDUwQjvzugztU14sHJyB__8FVRQiLaDqeuS-PYzORpAcMVe1u7EowpooPUOUyx9sFE1TCVAZa43xRD8wXAMitDaGS8M1tRSI7Vam2nezthapXTK8fpc-M1p_9tWmOBv9PDnSArY55yhqi1DmPFu7HGrqsk298gtD9hgK0fSwEtMAPzFBAR3BjSuhUxdxJ4ZesfIoD0h2923pgS3ssvufZ9cFukulEPADl81B5g-2BYwV36yHfU_F4CiixprPSddaFTxZjdBvI8vV9wL96_IdVo3eVjp6SCGfLb0jTRB_yqJ2aczZ6ksCv1zvHeG1tZL9amXELzCVZ_m8PW8V8tn5qNFv7EQ2f7hRguI_iSArIDQWQe6mm1Bn-vWMNYwMcaLPIqu5SZB1NzNEia8hCrLP44tXNVGNN4OHhnzGCkJw-HsMZ_y31zrlJ-tDXCctN9Ddi0z8lVeNogEX_emJ5M-SBhhHvy-sapIrvuZTweiC3EedPou4_uuX5OqdxtDze9SgAS-MGwO-NXHUOC6ZjYxxORZOnRpqACHpyKg5GiTZAyyLHUJTxIomYAwg9ypK5yCel-FIj8wSJO9gZsHpvY5xv9wPaaVm-cr2YKQCN_wEA4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاب متفاوت هوایی از تشییع پیکر مطهر رهبر شهید انقلاب در مشهد مقدس.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/448751" target="_blank">📅 18:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448750">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🎥
پیامی که از دل این جمعیت به کاخ سفید می‌رسد
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/448750" target="_blank">📅 18:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448749">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🎥
پیکر مطهر رهبر شهید انقلاب اسلامی در سیل جمعیت عزاداران درحال حرکت به سمت حرم مطهر رضوی است  @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/448749" target="_blank">📅 18:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448748">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9dc2333dd.mp4?token=OUG2g_Oar_iR89i38knXWr8g_osvAUhro6_QyFMgIeNDrvnp3eX0w9yKjfJjOutOi7jNO35u5bijh-0_3p6v-j1Vf97gYsNYdH841HJcaMxHjaMfIMp-TL3QLcvYFG-vAtaG7Ojy_OV4HmA9QbaGoCx9J6XN0Eq8BbSpZTDKst_3pM57CGeem-jtGJc6oX_ilrdekVBZwNuNkaGWHbdG_qo_XokfP29HY2IS8CJV4Ov46IZSlTVXLieOC20Z8gUQW0UDD2x5xBX89Z23DGlK2RJVFpZOZ3187WJMXipD33f5mOBAbsN-jZAgVyOXN9JkRlU_BBJJtpCBbUaiMS_FIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9dc2333dd.mp4?token=OUG2g_Oar_iR89i38knXWr8g_osvAUhro6_QyFMgIeNDrvnp3eX0w9yKjfJjOutOi7jNO35u5bijh-0_3p6v-j1Vf97gYsNYdH841HJcaMxHjaMfIMp-TL3QLcvYFG-vAtaG7Ojy_OV4HmA9QbaGoCx9J6XN0Eq8BbSpZTDKst_3pM57CGeem-jtGJc6oX_ilrdekVBZwNuNkaGWHbdG_qo_XokfP29HY2IS8CJV4Ov46IZSlTVXLieOC20Z8gUQW0UDD2x5xBX89Z23DGlK2RJVFpZOZ3187WJMXipD33f5mOBAbsN-jZAgVyOXN9JkRlU_BBJJtpCBbUaiMS_FIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این‌پرچم‌ زمین نمی‌مونه
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/448748" target="_blank">📅 18:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448747">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bccb2ff9c4.mp4?token=O5BPvxGb_WZMxK67oJHGa9-5EhTdy_x6FV6flpDkLJvSi0lE_tB7_1DbcShPXU9zqalJdgyYWdwqyFRXdsGTUIi-9HFnAgTgk1xiF0F-FU4apu0w_BMFhmFgyX_GXWsP01VXRLyA0RT_PFQlmRjNWhNAMjAw_5S5y-gXterySSqVlFibTFwKzgtrJUhm02iHJOIYAiGTRaBViG6ApihwnCN2okK73qFLNBbY0vNltOULVIspe7wkMljdS75_rox_egEL2vQDmbe2uPb66RxLJVxdKV84H7O_8WwFWZXIp4h3m6fsqpZDeQp4DH7phuKgGCy2KkHqrvul8eJlv9b8Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bccb2ff9c4.mp4?token=O5BPvxGb_WZMxK67oJHGa9-5EhTdy_x6FV6flpDkLJvSi0lE_tB7_1DbcShPXU9zqalJdgyYWdwqyFRXdsGTUIi-9HFnAgTgk1xiF0F-FU4apu0w_BMFhmFgyX_GXWsP01VXRLyA0RT_PFQlmRjNWhNAMjAw_5S5y-gXterySSqVlFibTFwKzgtrJUhm02iHJOIYAiGTRaBViG6ApihwnCN2okK73qFLNBbY0vNltOULVIspe7wkMljdS75_rox_egEL2vQDmbe2uPb66RxLJVxdKV84H7O_8WwFWZXIp4h3m6fsqpZDeQp4DH7phuKgGCy2KkHqrvul8eJlv9b8Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر مطهر رهبر شهید انقلاب اسلامی در سیل جمعیت عزاداران درحال حرکت به سمت حرم مطهر رضوی است
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/448747" target="_blank">📅 18:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448745">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f803a62c9c.mp4?token=GZct1cN1xUCZAMJWI948rH9B8q5BoAdJL-fUtFJNpR0CSjmiu_bjtHHfGYBhbnyqtBBCefENiNpCmr-bdkx-YwmGfBRjOQkVNqATf_8d_l4OruVT908R2GJoglk4-XOTMBh4wKtcvitQ4lHl8MX1yUgTSWxSTbqjiZq9Gcu0cyMi6iZjp-j1rTRtV9Ap9uPjeS6w-CA9xckCEcPZI-CHagg09ZvuzMCWXPlWlbhsEOv5j3V66zThrHk7XQq9AaeDBcTRoxzkDl2W5UrfE4Ebeug1y-MQR6iGZk1sUiaGyioERPImFiy39J005frjqGmgZ-1ooO3Z-kwY0O2_HkcP1ga8vqUQuDzcZnhyljYgb5F6Io_h_afAFK8uVpGo5ivcrLqUy6LmqhIET3tQwt4ezuBY0gNXDGCWmVeIhKVpdE1n2h0VldAloY_kbNDfU5i-Vsu2cH1Euc11SuG4Jvr7wR5t--V1adL7O7RhPw3MtQp_BUpn_2PxvRDqJi8v8_1FtCD9LPo2g04AN9z5YW63efFy-q75zV7ZGf6br9d3wtWoRq8XVXEWsvOnEC56cfQerjbe9_q31I6j6sC4P1tauFim8t5L-BwVJSqhhuj6Of8KGMHiB86ZQ30pcQiRex8V9vFFQxUmWML1qbrIGJBIVkIgHdZCYf788wsD0zCtkS8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f803a62c9c.mp4?token=GZct1cN1xUCZAMJWI948rH9B8q5BoAdJL-fUtFJNpR0CSjmiu_bjtHHfGYBhbnyqtBBCefENiNpCmr-bdkx-YwmGfBRjOQkVNqATf_8d_l4OruVT908R2GJoglk4-XOTMBh4wKtcvitQ4lHl8MX1yUgTSWxSTbqjiZq9Gcu0cyMi6iZjp-j1rTRtV9Ap9uPjeS6w-CA9xckCEcPZI-CHagg09ZvuzMCWXPlWlbhsEOv5j3V66zThrHk7XQq9AaeDBcTRoxzkDl2W5UrfE4Ebeug1y-MQR6iGZk1sUiaGyioERPImFiy39J005frjqGmgZ-1ooO3Z-kwY0O2_HkcP1ga8vqUQuDzcZnhyljYgb5F6Io_h_afAFK8uVpGo5ivcrLqUy6LmqhIET3tQwt4ezuBY0gNXDGCWmVeIhKVpdE1n2h0VldAloY_kbNDfU5i-Vsu2cH1Euc11SuG4Jvr7wR5t--V1adL7O7RhPw3MtQp_BUpn_2PxvRDqJi8v8_1FtCD9LPo2g04AN9z5YW63efFy-q75zV7ZGf6br9d3wtWoRq8XVXEWsvOnEC56cfQerjbe9_q31I6j6sC4P1tauFim8t5L-BwVJSqhhuj6Of8KGMHiB86ZQ30pcQiRex8V9vFFQxUmWML1qbrIGJBIVkIgHdZCYf788wsD0zCtkS8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حالا حال حلما را درک می‌کنیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/448745" target="_blank">📅 18:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448744">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af6c4a87bd.mp4?token=ndM9wC7SKgdthyOKupIVKyvzT9rF0LwGIOwUzG5SANU9UxWRMa0tigReqVmDR33sEib2eUAE94XukspCRZLmF3WtW2BX9r4QeuZDQnfZomzEMrYfFfGX2M7yRr5JTV2FyLVUyFxCJ3jtSKfexbQ-JmUQ4_N9umoANEfHTwDBId4bvcR1uVWebgu4va7PekfVxUzWC2yPH73yPhMV449--Y9x8XGjI5r8w-uEjM8r29q-dBvU7LupBi-cMEcoY-rPcDm78UfWxoUq16Ir9vfHeyLj_dWk_clG4RdEBWvSRdix3Eo8CtKO6cCudBXQwawpQ-DDXuMbSLD7Q_eOuZUFFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af6c4a87bd.mp4?token=ndM9wC7SKgdthyOKupIVKyvzT9rF0LwGIOwUzG5SANU9UxWRMa0tigReqVmDR33sEib2eUAE94XukspCRZLmF3WtW2BX9r4QeuZDQnfZomzEMrYfFfGX2M7yRr5JTV2FyLVUyFxCJ3jtSKfexbQ-JmUQ4_N9umoANEfHTwDBId4bvcR1uVWebgu4va7PekfVxUzWC2yPH73yPhMV449--Y9x8XGjI5r8w-uEjM8r29q-dBvU7LupBi-cMEcoY-rPcDm78UfWxoUq16Ir9vfHeyLj_dWk_clG4RdEBWvSRdix3Eo8CtKO6cCudBXQwawpQ-DDXuMbSLD7Q_eOuZUFFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خون‌خواهی رهبر باید این‌شکلی باشد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/448744" target="_blank">📅 18:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448743">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0756d602ce.mp4?token=XQ3M8Ms9vRX2ghMrtXnOFnJ_EguUTue7_4PuZQ6Q1kasjFYqyNPYbMCZwiOHciDLCzrqiFXqWKneMOwOSoz2EtFi4pl7arcz91-29yBKwdlnwRoJLhHRVS9nUS5iP8iAunywidJL_D_8vm1G_vAUr5jb7U5Q_xCAGWUbBIP6v9JjPWyRlUrSgk7b-pmQ4uWOC4RacVqwJdF5yrShI9mYTE15oHz8a1CzFVQL-3AuR-UXy3mFsEWAtTggZBFseA5_CQqDdjjAkFY6EtL8Kf4OLxnVqz-iinpm2NeUV_vfVYrHtaBMg1oW7XyT7SbcNY605W30z1LcgQwBxZEUarFAkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0756d602ce.mp4?token=XQ3M8Ms9vRX2ghMrtXnOFnJ_EguUTue7_4PuZQ6Q1kasjFYqyNPYbMCZwiOHciDLCzrqiFXqWKneMOwOSoz2EtFi4pl7arcz91-29yBKwdlnwRoJLhHRVS9nUS5iP8iAunywidJL_D_8vm1G_vAUr5jb7U5Q_xCAGWUbBIP6v9JjPWyRlUrSgk7b-pmQ4uWOC4RacVqwJdF5yrShI9mYTE15oHz8a1CzFVQL-3AuR-UXy3mFsEWAtTggZBFseA5_CQqDdjjAkFY6EtL8Kf4OLxnVqz-iinpm2NeUV_vfVYrHtaBMg1oW7XyT7SbcNY605W30z1LcgQwBxZEUarFAkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دریایی خروشان، به رنگ انتقام
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/448743" target="_blank">📅 17:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448742">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ab73420a.mp4?token=k4-plwqq2cWTePPCIYkmTwaJzdSccIiCBPrSMCEa6F1lmcElZYv9Y-FwCQzwrp0m5GZNteiil3O0ClZ2IcyKFpWbjivJqVtc8c49ONarVO9MblZaP_sJON6i3F2e2nNTV0JrdqWy5qrz_KcieSaN_2jPaUhzHSVWU9oWKpL1x4g62kl-p9Vi3Nv5iEbtrSLa_qK2FHjo-KKv6WZFMDa8lTYEoXh2NJGVxAzLe2YiDFihUvr3MsoJTVbyM7zHkYT9K_jwNyMavKk5g6n96keIzYZWakOHr_mragXkFL8lFBZaRpRmK3eAMZ3zTdEGHUlvJ9wqmWX2uAh0Q7A48gKM7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ab73420a.mp4?token=k4-plwqq2cWTePPCIYkmTwaJzdSccIiCBPrSMCEa6F1lmcElZYv9Y-FwCQzwrp0m5GZNteiil3O0ClZ2IcyKFpWbjivJqVtc8c49ONarVO9MblZaP_sJON6i3F2e2nNTV0JrdqWy5qrz_KcieSaN_2jPaUhzHSVWU9oWKpL1x4g62kl-p9Vi3Nv5iEbtrSLa_qK2FHjo-KKv6WZFMDa8lTYEoXh2NJGVxAzLe2YiDFihUvr3MsoJTVbyM7zHkYT9K_jwNyMavKk5g6n96keIzYZWakOHr_mragXkFL8lFBZaRpRmK3eAMZ3zTdEGHUlvJ9wqmWX2uAh0Q7A48gKM7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وعده دختر دهه هشتادی به «آقای شهید ایران»
#حاشیه‌های_بدرقه_در_تهران
@Farspolitics
_
link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/448742" target="_blank">📅 17:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448741">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c53b5ed1ea.mp4?token=V8H9eQ8zjZI87ivo6cN57813d8USoshAI3FKcX9c1ccrYLZaEv1TN_nKpMGaJ94fkdG2ZVs7cgpcvRGqOXifo5sfsdSQfsqS_qo3VrxrSCcIWJfsDnvEgcsR-t3X60C4JYW28G7SZJ3KffdLQDa3BaqapUADBcElubdI_wOWsnvDp1bV4v07Wd0Ui0gmlPZSbZS8uxJ2S-y8kaC6aPk024W_sj-ViCPSt-42Q9CbotZi4OoVikeDVc8JqwxUVeLPO8Bl9uAXyO7OyYh4J4EBMGBblFwosw23QLlTUE2cOuWGqYz_V47cuy08ctrsjWEl3htH1mS-llSPWUPAj8NmzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c53b5ed1ea.mp4?token=V8H9eQ8zjZI87ivo6cN57813d8USoshAI3FKcX9c1ccrYLZaEv1TN_nKpMGaJ94fkdG2ZVs7cgpcvRGqOXifo5sfsdSQfsqS_qo3VrxrSCcIWJfsDnvEgcsR-t3X60C4JYW28G7SZJ3KffdLQDa3BaqapUADBcElubdI_wOWsnvDp1bV4v07Wd0Ui0gmlPZSbZS8uxJ2S-y8kaC6aPk024W_sj-ViCPSt-42Q9CbotZi4OoVikeDVc8JqwxUVeLPO8Bl9uAXyO7OyYh4J4EBMGBblFwosw23QLlTUE2cOuWGqYz_V47cuy08ctrsjWEl3htH1mS-llSPWUPAj8NmzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماهنگ در آغوش ابدی خورشید
🔸
برخی تصاویر رهبر شهید در این نماهنگ برای اولین‌بار منتشر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/448741" target="_blank">📅 17:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448740">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/792f81a5b6.mp4?token=nN7bvW6WiD0zo_uNS2K_AgMkQWd22lWf-nkRaKorOy48aYhk8vHbszVp0o9tSpXZkF8N2Z76dYpaYt3Djh8cU6YlwdRFdfKCUFI7J85tYUGULAp_B534CZjrPXCczSIjHgp7b4Fiwwxw9s4JgWdFEzg7VbSDMfWj01__i4kjKCuetJEVMxLmOMXcT4MUwmnpfogrz2f214PpLBD3t1bBLNfhKhM4Y7D_RWFi8ywvd33p8BV2nKRMtERjr6D_ka6MhS4Iym7ilexLZ49CdDXyKRA_HJq3TYnzQShAOCt9LfKuKtMhg9ZJJC7d_6rvogd0ce0Ur_qlFYJw6Ou4ivpKRwII6HCWHvmhhR2dE95sDH2K3eHrKO2MQ8hvM6xNZdD1LQTb89z28q5AQ9p0uGkNdeW6zD4z82RIqnufXk6yDUTjsXpoZ9BpA7DtQF_gSwoXo6RH2_koFReJTIZl23Fg_GwlDnQhyS-0jMLVXB2-7N5TdfwPWnqqOYUHwE995LaCfNtwzaYO5GCPHBXlI_oVzhjoY-gz6wB3seeCcqQDUL53-E3ykZH0qlGu6PuTlL8LPsLdELrkPaNofu-wSnfVkfpNXJ5fiIbpUoob3BVPZ-DpjZLG91oEji3hfblIXJ9NgHtZVDqxPe8ypCHAW1ivjJgjJ6R4WtdsHMDGiFhKVso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/792f81a5b6.mp4?token=nN7bvW6WiD0zo_uNS2K_AgMkQWd22lWf-nkRaKorOy48aYhk8vHbszVp0o9tSpXZkF8N2Z76dYpaYt3Djh8cU6YlwdRFdfKCUFI7J85tYUGULAp_B534CZjrPXCczSIjHgp7b4Fiwwxw9s4JgWdFEzg7VbSDMfWj01__i4kjKCuetJEVMxLmOMXcT4MUwmnpfogrz2f214PpLBD3t1bBLNfhKhM4Y7D_RWFi8ywvd33p8BV2nKRMtERjr6D_ka6MhS4Iym7ilexLZ49CdDXyKRA_HJq3TYnzQShAOCt9LfKuKtMhg9ZJJC7d_6rvogd0ce0Ur_qlFYJw6Ou4ivpKRwII6HCWHvmhhR2dE95sDH2K3eHrKO2MQ8hvM6xNZdD1LQTb89z28q5AQ9p0uGkNdeW6zD4z82RIqnufXk6yDUTjsXpoZ9BpA7DtQF_gSwoXo6RH2_koFReJTIZl23Fg_GwlDnQhyS-0jMLVXB2-7N5TdfwPWnqqOYUHwE995LaCfNtwzaYO5GCPHBXlI_oVzhjoY-gz6wB3seeCcqQDUL53-E3ykZH0qlGu6PuTlL8LPsLdELrkPaNofu-wSnfVkfpNXJ5fiIbpUoob3BVPZ-DpjZLG91oEji3hfblIXJ9NgHtZVDqxPe8ypCHAW1ivjJgjJ6R4WtdsHMDGiFhKVso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک ملت، یک داغ و آخرین وداع
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/448740" target="_blank">📅 17:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448739">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dca6861c19.mp4?token=vLdpNd1SKqXnC7R0Mu_iakp6kmoM1i7NlyiIdVGB0746S0LYWVsA9MDvsIB969RaL02TkePw_okrR-pWM8hg1OUxAFpJ5RJ4ya2pfU5q43URauWu_cIQZ70Z3EOVCEQg_aG7FXzvkTZW-kIoRg2P4LOYcWawNsHbDRt-OnRavoyrSUgeTAfri_oumb5PeJFKMkdxfNpih66caRc7tI5jG8hgkHT3Th9Tutt5sIIUB3YGSpvSAIx8KMsnJjUhJcOSg8d5zJACexpWbHWqxDgNBsX_ZfEOZOKudPJYuvogpDAQkGWcAaukrYwnJD8BOG9UrFKTPqVjehbJCJEJSLxHBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dca6861c19.mp4?token=vLdpNd1SKqXnC7R0Mu_iakp6kmoM1i7NlyiIdVGB0746S0LYWVsA9MDvsIB969RaL02TkePw_okrR-pWM8hg1OUxAFpJ5RJ4ya2pfU5q43URauWu_cIQZ70Z3EOVCEQg_aG7FXzvkTZW-kIoRg2P4LOYcWawNsHbDRt-OnRavoyrSUgeTAfri_oumb5PeJFKMkdxfNpih66caRc7tI5jG8hgkHT3Th9Tutt5sIIUB3YGSpvSAIx8KMsnJjUhJcOSg8d5zJACexpWbHWqxDgNBsX_ZfEOZOKudPJYuvogpDAQkGWcAaukrYwnJD8BOG9UrFKTPqVjehbJCJEJSLxHBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برافراشته شدن پرچم‌های انتقام در تشییع امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/448739" target="_blank">📅 17:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448738">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61f80416c9.mp4?token=olrhyRu_jopi5-5-rTTSiNvtap8uQ4VqSPy4hEWLN99mqmeY6uSDPvQwvUD3n5BT4-88rOS6pHhwUvNTwcpXDTY7jLcmdBuLTqFKZR6lQYjaXQunvbo80I55WyHFQ4CeGujeUAXWzphPi7Qgja5a5Npe5RvyKkD45Z_nxSEDnRuvgMa6uo1Erdgej9S6GbhgtTLQVTO3v4uatczZELjoHY3WADS1bIdbT30UMGf3DjaroOjO595sSLLW_R1mo9ublTl_GsVSQngOHfmVM8xJiGxZBDAzYqlNlAW4fmamGi3QHflJhji7MzZ2xCDl6jZ2_gc5zOY-HkrO3RD3WZGDjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61f80416c9.mp4?token=olrhyRu_jopi5-5-rTTSiNvtap8uQ4VqSPy4hEWLN99mqmeY6uSDPvQwvUD3n5BT4-88rOS6pHhwUvNTwcpXDTY7jLcmdBuLTqFKZR6lQYjaXQunvbo80I55WyHFQ4CeGujeUAXWzphPi7Qgja5a5Npe5RvyKkD45Z_nxSEDnRuvgMa6uo1Erdgej9S6GbhgtTLQVTO3v4uatczZELjoHY3WADS1bIdbT30UMGf3DjaroOjO595sSLLW_R1mo9ublTl_GsVSQngOHfmVM8xJiGxZBDAzYqlNlAW4fmamGi3QHflJhji7MzZ2xCDl6jZ2_gc5zOY-HkrO3RD3WZGDjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از سیل جمعیت مردم مشهد در بدرقهٔ آقای شهید
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/448738" target="_blank">📅 17:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448731">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XALCM6-K8nVpjLlICQ0pMByq6YOM-C8dZxpDvUvdJSmGaqDUgew47ljkkn1bn1wTnBjzYBK-AnuhbX011kxDcTtGr_9APaW6qarlpIAAd6HOFeLH3ZJE1SPmumWk45B6S1KCSxBpnGlr-BHej33fKDQzPl7C-qQqJXgmJJmC2dKpcUHfuA9XZL147yyADGxQSWohbRBGQdsOaE6jLGkzC8a9RAZchFCt9p28w0erDTZ3EhXvEsmp4elY6zHNl-nLkaCzij-1bNrLUvLkf55orQju8y-8a88nC0UZyFvHqjs7jsSPm4jBi9l2EVKRWUUeHU2TDkx9LZpOIKSRCp3zDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZbnJ-8ICq9ami7vAndpDudAuk3sXaOaeD7qtB8lte38lgH8IqCVKmVLvuUVTOzZyg8n8hS-YvPo5QlW39uKhME0Q4d8RXElMBEQPnreJESQ-FYk2olIhDdppDQQexoZ9MPDdxmVAC5uJZhScdL2BoEWGRc_EaZGg3VLzpiVHWuPOuhM_5RN41EbsWOJq95RVspK4fdrjECYOdAwMRL6EiPX8jRm4to6t6Ji066OXYocaw6V5vFD4_82slPzvfyhNBifEPj9Y53ubtv2SbGEK_CqpK4R87_ojrrblNn0RfOlczS3y9y6uD-ipdGmODTiK24NxcpHrPIky4Px3MdTmYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TAPnRvinTI18_8DaWplvY2qnD5EBuBDPzYUpK4Pak9oHVOvoiSx-oGan14O_BK-OPFpeIELnQ9tIZl6okxjbhTqht28HyyLcoIKGTJ_SdAu01RZmEk2nXvcQLfDJEnqEwJ61YL2_sc9jnrOt2kXSD_IKNSfKc6bu-rsqyxHMZ4piyM3n9yt-QvNILy8YFQNRivh_TjXfYm-7oYT7SI84R1FOjklXTdscp6J2uQ-uHlp16GYDc2GFbElJACyLEKb6wOyp9C4EMD4mjiyhar7XKaPLFUL-tulcQ7s2611lmWD8NyB3_AlmQEHOM0p5PGe_EsdtGgLKAU5MVyvNm20vfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pM-yng1BHxw93VLtbGP0lZU9reqdJp_49bjl5gE8QnA5ncVJPAS3ptt8cfPMFcJLXj8AR_y9w4CWbFjzjT4nYeXHCWhSLii2KU0Ur6aQ0-wEn7Cxn5GDygtkavz2lPWhdrBp3myHgff6FfG26KY3MG5b5E7_4x6uMrzB3QJFpmAkXn6_-BTe-CP6JwqPJUR2gIc_vLILRHGokAhu4aBiRvnk6O2x07KLER_-ydio9do4H3XUYGs4JBQlVSMjMPz6BeDrzkDMUhsdbtBmeYtfpQq557K5m2wFqAPt1X4cbUxaKN9AnVlS1BJ7Ord9XXW_8lJI7ZH5kysp6ugdkz_jiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nbNs7NzSK2_1xO6b_Dd3f_tQi_aVRI5UB54ERBtKAVYZKaZ-CshaNaIKNi53dmaHF70g-UxxC--C8AeenPfa0bsFqZCyxzTyqv9tydPxNvAeTuX2XV14I8hRcEamEDvb6DORBACExcJg81nTReNFnYRkulEN3lqjW99UiOHdNVrCoFCMvNhinznfrScEN8J9XKabs7lGIU7g-ppXtdJFSXJ91WOrKsyyRqEgZDn57JXAshejpvlyC7-jKbCXNrGGT0_egz6x6domVxZ_baDrrkJ-XHgzuIV8vH-BfrjF6U1JwjBRD0aZXgxG0NzhR2_qNBJQ3yXvJLIgoZGzJkJPRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VB6GMfthSCWnYnYegJft1Nt1Ckv7rOfZtoD8a0OKAiN_Du6lWL8RUXGKbgpnFXfqsm51-QNwyXJBciZboswgJrF-VK2XX_8eM7_ZITsA7YCksWl8FAFnUPK_lojrRqJT710lsIpVHQyoVOZ76yZVdfUIEl9PLOlCPsqjVKNkQQVUU5bBZC61k6VOQOLIapPAUmYdi1LVId0JW5OAidgsvy_R1HgYnIEtnAeOKG6DcYw5NVvH5s9ubQORdMI6BNu4poK7je6eXIvxyO998AqwRnL5z9b_KIC40HDD0pQuh569mtizTueC-VMqCst7tz2NjXi2VG4ZTnyUWk0tb34YfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ej5nn33btIiaWw7pzfOjil1UwC8JYfjlPufyEd5JUlnMXymR6ZDAhJQLJpvP4JGiRS-s4gnMCySr9y6M83mCLr35vc7amVegBAax9taPVOSzxy06QUYDvPay3atA3Kx4YJdwB8IvHivBuBdfGPECzyErpFX9-JPg-sPhIX_3YdkZw32t099eBe0C0nwCi-o0fhQQE8wu4jL4ZR3RYGctzJln8rYtBRuhyiduVpBoDcp8CvWNVeW5QB_IjD7JpNJJ0oDtpt-C_rhjRkRXvc3QfU8MbkgQU0BM1CTMgsmqZ0DsuxION0K9EOMbc7WOzyuGAo2PDOAV-AqvkTER_j5SMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پرچم ما ترامپ را خواهیم کشت در دست مردم عزادار مشهد
عکس:
حسین توحیدی فرد
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/448731" target="_blank">📅 17:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448730">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ظرفیت حرم مطهر رضوی تکمیل شد
🔹
ستاد برگزاری تشییع رهبر شهید در مشهد: ظرفیت تمامی صحن‌ها و رواق‌های حرم رضوی تکمیل شده است. از  از زائران و عزاداران درخواست می‌شود از مراجعه به محدوده‌های پرتراکم و ورودی‌های باب‌الرضا(ع) و باب‌الجواد(ع) خودداری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/448730" target="_blank">📅 17:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448729">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79d29c8884.mp4?token=Xz3owxuc9WeMKptTCtcPrQmd8segbStUUMz7Wt_vxcb3EacTkmYeijdQRdxWIO1WTIwxN1jW70QqcKv0YBwvpjKY6QSUA0T5EkuyQScAyxnCMo7NGVTc5Azq4vLqdXIJ62UAMn8LlW2yWepJyzgS8BhhGD_fw0sYlOC1bcGrQhav-gsyLq-yin8jKBHmxB-rr7weswuYoGVdtk3g6O8fEdK9KK_pplXCXFXU_WTr8l0t2FF8N5b_A6X3GQgCZFvWeerBJ-75CbGlcdyDODGgd_2f43UF9mdp2uEh4dWqg6vea1Lq32zQtDIAIuMf30gslswbPiGsLw2xWH9px4Eo4GqL2vjHZdtzM8tUIN_xmVKTrdqRKyBNO9_NpYQDFhBFjSA-D1NoTmrVEY7uDBf82R24nJRMnGlH-Gu9mkdfDQW07G0tt5OGnRW7Cfrr0GlKQfQFezWXa7kCfGzV7wVmV47rXt2cyXoYW9r5dsysDzlmabAt6Pv3hoWP1ZpCr9BZUrV-VAIpTkw8r8x7CnxsljzqEgBqmLSLg-l11tMl1YYwpWCaiQ37_FxJprQKOkRayzpWcYcbMJzOhU68pIJnPF4xp-rJCCzETnW9xyjcCJqjXsgNZcMrEG1X7aUA_pNeconiyrvVOzD9yD5N_r5hsLp1koDPLeuakAy3s969Xas" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79d29c8884.mp4?token=Xz3owxuc9WeMKptTCtcPrQmd8segbStUUMz7Wt_vxcb3EacTkmYeijdQRdxWIO1WTIwxN1jW70QqcKv0YBwvpjKY6QSUA0T5EkuyQScAyxnCMo7NGVTc5Azq4vLqdXIJ62UAMn8LlW2yWepJyzgS8BhhGD_fw0sYlOC1bcGrQhav-gsyLq-yin8jKBHmxB-rr7weswuYoGVdtk3g6O8fEdK9KK_pplXCXFXU_WTr8l0t2FF8N5b_A6X3GQgCZFvWeerBJ-75CbGlcdyDODGgd_2f43UF9mdp2uEh4dWqg6vea1Lq32zQtDIAIuMf30gslswbPiGsLw2xWH9px4Eo4GqL2vjHZdtzM8tUIN_xmVKTrdqRKyBNO9_NpYQDFhBFjSA-D1NoTmrVEY7uDBf82R24nJRMnGlH-Gu9mkdfDQW07G0tt5OGnRW7Cfrr0GlKQfQFezWXa7kCfGzV7wVmV47rXt2cyXoYW9r5dsysDzlmabAt6Pv3hoWP1ZpCr9BZUrV-VAIpTkw8r8x7CnxsljzqEgBqmLSLg-l11tMl1YYwpWCaiQ37_FxJprQKOkRayzpWcYcbMJzOhU68pIJnPF4xp-rJCCzETnW9xyjcCJqjXsgNZcMrEG1X7aUA_pNeconiyrvVOzD9yD5N_r5hsLp1koDPLeuakAy3s969Xas" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت‌هایی از میزبانی مردم عزیز مشهد از مراسم بدرقهٔ آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/448729" target="_blank">📅 17:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448728">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c7a7390bb.mp4?token=UGcpyrPxMIBhDL1uqJpfORbQFUdIjD2VhvbsQVu7LW7uzBmonj0AQrCQnsrEgE0Hg_hAHoO8VqtOQQ6liomO_DE6h7g2F6EBC6Fcv0F5uW4aNQ42XbM45liUEGuqcKK87mqQ0b05Wf1CIQNhEa5lDUkUVSpwd8_67ncNqc1xf5krEYgpsuOc7vqSXCQ3UeqpK-eJQGsf9Ydn8tHRURq6X4JaBEf2bTvWBLwVbcfoMDt1IZTLm8_Vnt1lLcYUs0W-o4ZRUhApQ3TtmOrp_SUnxCuIgP0_Eq2kO8bIsIgng3fWJvDkM08wUpqFmkgKEzLlB7Tbynk7k1bkV6NWfAPBuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c7a7390bb.mp4?token=UGcpyrPxMIBhDL1uqJpfORbQFUdIjD2VhvbsQVu7LW7uzBmonj0AQrCQnsrEgE0Hg_hAHoO8VqtOQQ6liomO_DE6h7g2F6EBC6Fcv0F5uW4aNQ42XbM45liUEGuqcKK87mqQ0b05Wf1CIQNhEa5lDUkUVSpwd8_67ncNqc1xf5krEYgpsuOc7vqSXCQ3UeqpK-eJQGsf9Ydn8tHRURq6X4JaBEf2bTvWBLwVbcfoMDt1IZTLm8_Vnt1lLcYUs0W-o4ZRUhApQ3TtmOrp_SUnxCuIgP0_Eq2kO8bIsIgng3fWJvDkM08wUpqFmkgKEzLlB7Tbynk7k1bkV6NWfAPBuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحن پیامبر اعظم(ص) پیش‌از رسیدن پیکر رهبر شهید مملو از جمعیت شد
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/448728" target="_blank">📅 17:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448727">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/099b8d9b4a.mp4?token=eMj3wn_2ureTNBXVbx7lJKmdGsaysXPm7a1ZLBrZ4iFOWFsawnm803IJzDqxO-FACxpNVFOs3A_OFmyit33l-WlWv_zHYVIu31xpl36q_nL3R4Sfr7uNNA2T0e6ZzxvMiciydx1CQxhBfYo5sTUkAhccrSE1bzgk4X6qbScDLgk_9d5WYEdotUbeiGzuaOxChhGb_NYtxfVlqwl-8eD-77DISs4TgHZLbOrWOR7ze71k25vF_q14FHfwyg2AuHbjo2ah5c9AWQkinWZfqNL338q2bMGTstz8f5rJ7UfwglcovJDu3EcMbfD_elrMlWbN448UkdQmJNvfoKRJiMNBqjN1kV5EDs5_yCIyb9CF-bTDZn_i9iKtoGNrSdr8x9YlQQE5rndLtegNXcdMteKTGGiluyuYmwjRp3UnM-7cSxLEYBv0MnhIiRYUK_Ca6pWqfSnwpR5KL12Du7PzOfisjQrWaOsHnIzwJcnLv2-tFZtDYS_bzQ3umhaS53zhwtgj_U3ZBD1BkRsvkXgQNyiUFR5yZo7nyBSXWw42tBLOokHZOUhdeLSp8gxCiF68aXU2SMv_Rw4RHf2KKPvt6lxvCQDCXGfSVzKQYkt5cOAvIJ5z0XAfqDxwKVPyB1cKo_Bi3N3MQ4b4nzbt_DgQmi4Gp3fLKkoLsuL_2YLTiOdwmkE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/099b8d9b4a.mp4?token=eMj3wn_2ureTNBXVbx7lJKmdGsaysXPm7a1ZLBrZ4iFOWFsawnm803IJzDqxO-FACxpNVFOs3A_OFmyit33l-WlWv_zHYVIu31xpl36q_nL3R4Sfr7uNNA2T0e6ZzxvMiciydx1CQxhBfYo5sTUkAhccrSE1bzgk4X6qbScDLgk_9d5WYEdotUbeiGzuaOxChhGb_NYtxfVlqwl-8eD-77DISs4TgHZLbOrWOR7ze71k25vF_q14FHfwyg2AuHbjo2ah5c9AWQkinWZfqNL338q2bMGTstz8f5rJ7UfwglcovJDu3EcMbfD_elrMlWbN448UkdQmJNvfoKRJiMNBqjN1kV5EDs5_yCIyb9CF-bTDZn_i9iKtoGNrSdr8x9YlQQE5rndLtegNXcdMteKTGGiluyuYmwjRp3UnM-7cSxLEYBv0MnhIiRYUK_Ca6pWqfSnwpR5KL12Du7PzOfisjQrWaOsHnIzwJcnLv2-tFZtDYS_bzQ3umhaS53zhwtgj_U3ZBD1BkRsvkXgQNyiUFR5yZo7nyBSXWw42tBLOokHZOUhdeLSp8gxCiF68aXU2SMv_Rw4RHf2KKPvt6lxvCQDCXGfSVzKQYkt5cOAvIJ5z0XAfqDxwKVPyB1cKo_Bi3N3MQ4b4nzbt_DgQmi4Gp3fLKkoLsuL_2YLTiOdwmkE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هر پرچم سرخ؛ فریاد بلند خون‌خواهی
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/448727" target="_blank">📅 17:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448726">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/606cfad7a9.mp4?token=pm9b2XfTlpqsx8cIalgr_3TyFVni8bTLZRKU0-7_oejeeJnObLmcUZ0xeesAFe5vFKI_nOS-6CkgCEVZxLaaqqjZigDSuLvtU-rkFDwJ-ajPIxKsL61XmA9va6YdA2Jp-hzpOPt3SZRDK1VBEstQvch8t-JVj8LJ4TFWISVmpa27Sfp-G5lAv-TREyg5KJeZz2Yz7rH5JpMUjUA6Zi21lluH65A14JUv5VxRbBpqcmnIEjkep8BUOIjVAU1mue7zqQuMnGyCg5zTOFCZxVTPLdC5hy0GugEh_O00IRaK3Gpor4AittmmgXzAbh9Tl2UJh6Saf5utmB0dFQzoXCk9fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/606cfad7a9.mp4?token=pm9b2XfTlpqsx8cIalgr_3TyFVni8bTLZRKU0-7_oejeeJnObLmcUZ0xeesAFe5vFKI_nOS-6CkgCEVZxLaaqqjZigDSuLvtU-rkFDwJ-ajPIxKsL61XmA9va6YdA2Jp-hzpOPt3SZRDK1VBEstQvch8t-JVj8LJ4TFWISVmpa27Sfp-G5lAv-TREyg5KJeZz2Yz7rH5JpMUjUA6Zi21lluH65A14JUv5VxRbBpqcmnIEjkep8BUOIjVAU1mue7zqQuMnGyCg5zTOFCZxVTPLdC5hy0GugEh_O00IRaK3Gpor4AittmmgXzAbh9Tl2UJh6Saf5utmB0dFQzoXCk9fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بغل واکن در آغوشت بگیر این‌ میهمان، سلطان
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/448726" target="_blank">📅 17:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448725">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fed5a5f4c.mp4?token=V4N_H67DKo5Kao49p6M9YGtjMYe6GROrWdDpZTQ1VLA3JhMfx67AEkFh0btoCAbMclLoN7fZcspw1BL-MZbS9OkQre5_4xeiDxst5x93KCzpbheGG_jUTYCuhMOwFzz85Srj8quy7y6f9xi4NPBTROzanEY9Y7FRXGMJA_tCHHED8Y9fbaRNK_oL0gp1dzfG4hBM_i9vCqHdeTFQtf03xsuGOAaJ0_Ax5hixcU-NDkn2QCxd2zeK6e7vZOVyPYWKTKbve2kg_9aURY_KQ54KOASuifpEzMZYVCCp3n_jJnW2Al9FzZb8UmTG2W6ZbrFr-75R0qWxDvGg_P3K8JJ-3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fed5a5f4c.mp4?token=V4N_H67DKo5Kao49p6M9YGtjMYe6GROrWdDpZTQ1VLA3JhMfx67AEkFh0btoCAbMclLoN7fZcspw1BL-MZbS9OkQre5_4xeiDxst5x93KCzpbheGG_jUTYCuhMOwFzz85Srj8quy7y6f9xi4NPBTROzanEY9Y7FRXGMJA_tCHHED8Y9fbaRNK_oL0gp1dzfG4hBM_i9vCqHdeTFQtf03xsuGOAaJ0_Ax5hixcU-NDkn2QCxd2zeK6e7vZOVyPYWKTKbve2kg_9aURY_KQ54KOASuifpEzMZYVCCp3n_jJnW2Al9FzZb8UmTG2W6ZbrFr-75R0qWxDvGg_P3K8JJ-3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با پرچم یالثارات برخاستیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/448725" target="_blank">📅 17:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448724">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b681ec30f.mp4?token=joHhCpgoSZQWKxSXz6zQwt9t9aVOOTMSfpFH9IQHFScqrhKu10CUsoeUzE8aDsIPCiknnwsoWJ547mv9NnwsBLc5sOM32l5Xky7oM1TkpTzK5C3tm6EnnEmBFWJfPSTqaTXld6oAuig5G6ys8J51rONktp5M_ceupETBeCfmM4sGgpERwybK9LhleWHsPUW5p2HwvktMUpkVw_lH1OrZ2vcGrQfC-41rdSZZY8MD3Dr4uc-cQsCGEoz7KpsbZjuPdIFBG7BkkaKSAcZZCP2VtH9i1Bq795OadwTNHnUra9mu6I2fyKHu84wiMXJMEP2uGJuQqSrafOv8Xy9FplPs_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b681ec30f.mp4?token=joHhCpgoSZQWKxSXz6zQwt9t9aVOOTMSfpFH9IQHFScqrhKu10CUsoeUzE8aDsIPCiknnwsoWJ547mv9NnwsBLc5sOM32l5Xky7oM1TkpTzK5C3tm6EnnEmBFWJfPSTqaTXld6oAuig5G6ys8J51rONktp5M_ceupETBeCfmM4sGgpERwybK9LhleWHsPUW5p2HwvktMUpkVw_lH1OrZ2vcGrQfC-41rdSZZY8MD3Dr4uc-cQsCGEoz7KpsbZjuPdIFBG7BkkaKSAcZZCP2VtH9i1Bq795OadwTNHnUra9mu6I2fyKHu84wiMXJMEP2uGJuQqSrafOv8Xy9FplPs_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مردم مشهد: حرف ما یک کلام؛ «انتقام، انتقام»
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/448724" target="_blank">📅 17:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448723">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14efea4cb7.mp4?token=JBtJmqN_n9sPc0hOoY1kgiJKY7UY_mwKrK97xlsgESuFy2NTc-iY8vyGv4oYg5mBJivJtAZfvq89UK7uFwcFWT2hccCpj63qyMT1wVnPPYC5C5DF3jXH9rX2_RJxJavUdUWXrj6WP2EhIc7PFjF31SP90ZDf35kiwZ8v4Rjus2RusTKWcaQbvzVNVKWc7W1lIr5lK_SpEz1pACHr8Jgkxz5cM3aVT35WMSTwG2pYNBj_8_YyLOiSgwWlbhkcVTtBy0tnqujaTdHi-2vbUWbBNW5MYzgYFsOZWZZ0dpLtnuzQL-WaW-rOhaYLK_QC9JXnrJMLm-LcfEdop9R_E_GRyW61wyKJ7dGGdGjKFc38X4rMOSB1JW8A3NANrBXBNOf-s8Y8O98Eab3qThLQIXvo2fBRypixue0ywnisfnDg0XaVdwYxOoW7FypO-9Enfm1IP580DhDsrGHYTfu-_Ye7DGf0fphhiz5ZEDTqMtD7XKbo6M9TUpZBgZ2eliGM7qPHDE9Lx1IPqlqQI0a-OZn2zmlPZgnmUQ1Ryv7WbLsjy_M9ejxpZFz9W3M2RZaJi-IA-MEHWtxatvywV9coRk5C_F9D7ZhAqk_dktfWK5t-Eubbz9-Q8-KGusELUM5w-q0ArgT7VKRD_-OM5PS6ANiwolix4O-Nuu7RZdFc8Hfg8m8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14efea4cb7.mp4?token=JBtJmqN_n9sPc0hOoY1kgiJKY7UY_mwKrK97xlsgESuFy2NTc-iY8vyGv4oYg5mBJivJtAZfvq89UK7uFwcFWT2hccCpj63qyMT1wVnPPYC5C5DF3jXH9rX2_RJxJavUdUWXrj6WP2EhIc7PFjF31SP90ZDf35kiwZ8v4Rjus2RusTKWcaQbvzVNVKWc7W1lIr5lK_SpEz1pACHr8Jgkxz5cM3aVT35WMSTwG2pYNBj_8_YyLOiSgwWlbhkcVTtBy0tnqujaTdHi-2vbUWbBNW5MYzgYFsOZWZZ0dpLtnuzQL-WaW-rOhaYLK_QC9JXnrJMLm-LcfEdop9R_E_GRyW61wyKJ7dGGdGjKFc38X4rMOSB1JW8A3NANrBXBNOf-s8Y8O98Eab3qThLQIXvo2fBRypixue0ywnisfnDg0XaVdwYxOoW7FypO-9Enfm1IP580DhDsrGHYTfu-_Ye7DGf0fphhiz5ZEDTqMtD7XKbo6M9TUpZBgZ2eliGM7qPHDE9Lx1IPqlqQI0a-OZn2zmlPZgnmUQ1Ryv7WbLsjy_M9ejxpZFz9W3M2RZaJi-IA-MEHWtxatvywV9coRk5C_F9D7ZhAqk_dktfWK5t-Eubbz9-Q8-KGusELUM5w-q0ArgT7VKRD_-OM5PS6ANiwolix4O-Nuu7RZdFc8Hfg8m8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اثر فاخر پرواز همای در رثای قائد شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/448723" target="_blank">📅 16:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448722">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3134345d79.mp4?token=cNTJ2QwlDwhwAcDABLGXdA5KlRnvmU1Hx36ueVekGJe2mWRVyuX9ZoyOk0u3tsMFULwawcD4OeMwrsW9YUlZwuee-aWKKpePAU1yykJ1mEcH0Okh1JIDGbEB99FG3GiGaHwTRiTk2gIis2SJw5jYrgUJ6xlyaTKHAaYOMo8AhdAX9OC7evO3DNw8uBwM2ux9TIxB4v40HS-DF5e8cAVN5-5QCMNFxov2UtuMlvR16qKGty2kndFH2yGnxRQ79JFPRyt5d49UFrgX9jqxtw59NPWE2keRVKYDTRBfKXeIvsseHFFiZYu4IYYKI7T2-GuAOWVpVYTOZlpotVI7lH-cxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3134345d79.mp4?token=cNTJ2QwlDwhwAcDABLGXdA5KlRnvmU1Hx36ueVekGJe2mWRVyuX9ZoyOk0u3tsMFULwawcD4OeMwrsW9YUlZwuee-aWKKpePAU1yykJ1mEcH0Okh1JIDGbEB99FG3GiGaHwTRiTk2gIis2SJw5jYrgUJ6xlyaTKHAaYOMo8AhdAX9OC7evO3DNw8uBwM2ux9TIxB4v40HS-DF5e8cAVN5-5QCMNFxov2UtuMlvR16qKGty2kndFH2yGnxRQ79JFPRyt5d49UFrgX9jqxtw59NPWE2keRVKYDTRBfKXeIvsseHFFiZYu4IYYKI7T2-GuAOWVpVYTOZlpotVI7lH-cxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم متفاوت خون‌خواهی مردم: ترامپ را خواهیم کشت
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/448722" target="_blank">📅 16:58 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
