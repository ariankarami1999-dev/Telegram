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
<img src="https://cdn4.telesco.pe/file/IyB3zwg63yVXxj-TvHvl4uTXH648JNkwsWEjyWXL4h4iHNuhSh0qhnvbHwmcjly3aLcKHNp5dSm7s35HJ0W2HUnMz0Rn0l3oftAfWieCAPcZ_4az6EDHp5fJVTjEpAJiTZjR7lazRbuoHe9FvfQez7NbH8SzhhkLPYT6pWUKeHGZif7ZY141EQtjTkcB9F6JQFidq0AF7_ig5CPsExUp1i921XuthlOylNMlaNTTiTx2bbD_66qA0e8ZqzM_cKwa5M0HMHGpi8VDMNaijFLR4XN0uXOsaf3fPqnt9L6JND-mafSBJPZoFWKWReBQxXf_kYwpOcbaaTJ7ZRZs6_nxLA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 167K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 14:08:44</div>
<hr>

<div class="tg-post" id="msg-68340">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6f934d59.mp4?token=Z0fHbR2FE3p6pPLuOIpv1yAeMVQmg5-SzZwn4ALuD7Dke05gBXXeOLAovPkt9ld4n0bJxhEL_sj6kU7DKR9L7YH_SRpLr7ARDTa_50uNA-N8L2UqhjRLaWY5MOV8mSMFBjpuVVydr-wHGFocekhbYsVdQW6AL6aDgzBF2gY5S7kiKcSW9ibRORlbUf1KrXUZgOlTCsKRyK9P0KWsVvkjAvbByAKpEkY8IuvQR12MFNdQlxJcRg3N7bDnDpjDC-LrSHXNR8DYsh8DLPXbfVRm3rY0trJd5bP_DSJ9v8Eu6teQSVIZJCvJnQSpdbTDzB-5eBD0XbBKH_WQvt7_dNtHKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6f934d59.mp4?token=Z0fHbR2FE3p6pPLuOIpv1yAeMVQmg5-SzZwn4ALuD7Dke05gBXXeOLAovPkt9ld4n0bJxhEL_sj6kU7DKR9L7YH_SRpLr7ARDTa_50uNA-N8L2UqhjRLaWY5MOV8mSMFBjpuVVydr-wHGFocekhbYsVdQW6AL6aDgzBF2gY5S7kiKcSW9ibRORlbUf1KrXUZgOlTCsKRyK9P0KWsVvkjAvbByAKpEkY8IuvQR12MFNdQlxJcRg3N7bDnDpjDC-LrSHXNR8DYsh8DLPXbfVRm3rY0trJd5bP_DSJ9v8Eu6teQSVIZJCvJnQSpdbTDzB-5eBD0XbBKH_WQvt7_dNtHKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی مطهرنیا در برنامه «با ضیا» به بررسی برخی سناریوهای احتمالی در تنش میان ایران و آمریکا پرداخت و از احتمال حمله زمینی و نیز مطرح بودن سناریوهای دیگر سخن گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/news_hut/68340" target="_blank">📅 13:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68339">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e12e57fa87.mp4?token=USRXdMQg6tabDCGyPwnuc_YtlXvfioIxG23_OFZ0UncEcMO0XHr-WdpIOkD2i_u425Sr7iubbsLeFrn9wkRVfQSyU_UhydW_b4iLk2m3h4yHTkBtaCBuuDEE5J-8VgrgMrZ003qv99pfzIyzN3MqqJwqCu8ygVGa-MWwt0g7kXrK2BW9D0G8oQgO1APTEkCWA-QkwjkKkK9gE6GYF8R6jR6kojrhkLU8911PPheExvy9S6Akt_pyeeBhPdfkMriNykuZMiu7ANCOEi33_2pRslyVP2Hci3Y9OA19zJBCbekb9Bg-pEdeKNOVQJ4T750fF7NPs61MMF_F3NM-eSfdMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e12e57fa87.mp4?token=USRXdMQg6tabDCGyPwnuc_YtlXvfioIxG23_OFZ0UncEcMO0XHr-WdpIOkD2i_u425Sr7iubbsLeFrn9wkRVfQSyU_UhydW_b4iLk2m3h4yHTkBtaCBuuDEE5J-8VgrgMrZ003qv99pfzIyzN3MqqJwqCu8ygVGa-MWwt0g7kXrK2BW9D0G8oQgO1APTEkCWA-QkwjkKkK9gE6GYF8R6jR6kojrhkLU8911PPheExvy9S6Akt_pyeeBhPdfkMriNykuZMiu7ANCOEi33_2pRslyVP2Hci3Y9OA19zJBCbekb9Bg-pEdeKNOVQJ4T750fF7NPs61MMF_F3NM-eSfdMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تسلیت به بلاگر های چابهاری!
برج کنترل دریایی کاملاً فروریخت دیگه نمی‌تونید باهاش ویو جمع کنید
🙁
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/68339" target="_blank">📅 13:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68338">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kn5TQD-dCgfuSV2W5TNDbOMbV_ZL2oVcg5TLAL9GxBVNqKusEMM8tlv5ljEs270YSRmN8wFu8weocjHqQcd4vjAdlYbfUlrMUCtURXbpEYV-W_5_2noEdWlCKg_Ic8avQgtkpX1AcdjajTtDMz0VwNSEsOyKflIUlHg0h1akTd0c0FkG7_Z6k_EEBFWGZd5N12amNZ2URAj9Q7ds3WEQzeliHhqcZlb-ChHGk6T37gHYGTnnkxu_6Crbfdb7sHkDGnh62wbPa97O5PcB9QMPXkrc7FUUELicyPz9y4tY73MTfe0BFOD4BrJ_IghbYTsA0WYP_ecy2rT5drznNsxurQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دقایقی پیش یک فروند نفتکش که قصد عبور از آبهای عمان را داشته است مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/68338" target="_blank">📅 12:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68336">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MjBCDUoqa4p-VAonaxDpCcWNIhj6ZCBoSqi3dTcLotUhWONmE4uJorGwDCghwggRpPB1FP-GyIluJFsTbaeef-pHJYKgB1WZrSlKt5wpXoEfaMr9Mew8Bz7NGy-TUDa7O1awkgdO_e4P1rw1TWPPwErl7_Z3PkCfyR5srAxcIHfvFCVvlu0KSHVlwOW_w4Kp68oDmqHTDNIk4t-Szv5a0fy5vbfzlRZ6iO6nvKYKySagjN39XmBoh0-N6k7a1XPwUVMtXWniLsC3OA4TCE8hTGt9goFdOxpIVS2dqqyvkvIhoBh3kozFwyEwV372J5kvx1n8iViHxQkvyI7exP0l_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R41x1LdjwrSetQckUnmTPRnWBN7OTM3tpuAYG4OH7-qVVcclfilpUhKxeHRjweL6Taa_JlGJCT1-A7HUcKOffmAxa0cnnGA_1c01tMO100_X0A46sS7FtlFGV7BS9HER0BwxUU-5rkOYI-Jm1s8a84dp6uOz_x2r_XUPUstbjyRfqKMycJTkHVlAZS_1Le9r3JuOBSEuXKL5F3OWVAeOF1LNky-NR0a8vLWgt5mIGx9psbTvo3yrIaJ4AUBgApmE5Wc0EgjFuKSe3_WlDNZcyqynYgXhFcBedWhLe3umJ08NwHeophF3lYJv3jCLy7fsVdSnbtTm2XiUvq6Up-Vhsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
هگست وزیر جنگ آمریکا لحظه سقوط برج مراقبت دریایی چابهار را در صفحه توئیتر خود بازنشر کرد!
الان فقط یه خاطره از این برج مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/68336" target="_blank">📅 12:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68335">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
استانداری هرمزگان: در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.
کدام پل‌ها مورد حمله قرار گرفتند؟
⏺
پل گریوه؛ مسیر بندرعباس، خمیر، لار
⏺
پل بعد از روستای لاتیدان (کلمتلی)؛ مسیر برگشت بندرعباس، خمیر، لار
⏺
دو پل مسیر کهورستان، لار
⏺
پل نیمه‌کاره؛ محور بندر خمیر، کشار، بندرعباس
⏺
پل روستای مارو شهرستان خمیر
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/68335" target="_blank">📅 11:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68333">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPgzszBeCI3ocUP6ciKFrAVuB112sRQMNhaStdiG8shryZ_RW76qZt85u55sL_n9LHsb823HUipm0W8R4HxbE6rHLwPhlUSNL5zt5KSSQEM4n0q8zPTkM-YLFhjEBPbQKXhs3WmVRdbHppMKUZmgtbbKmzIvGJtyag6D5VUSeUpoP1G2SFr6kOqPCNxC8ItvahhoyslzXjogbrNMfPX5VB_3q7ZzW-QDs0zw59N1mVZpoq-T6S8ME_mW9hJ-rEvN5m6G8xfJ2bJSBD6JJvB0MMIeKJzBXNnKp8KbS6WDEM2F_ZLfv4kjOuv0pkwajtYpJQ63viHiwLIQ4cMYaE-3lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1vY3k_RcNAjZU2JN1sbRlbkLoJwLevqalReK9JQ5pMmSgj4-ITUes5PPgc4TFgQdPTL9KUSR5LCOJ3kZL0mTL_gmBjEwv8VPVakgEAwiXHhAc0w_b-Xnx5XxKSzdlx8RObxiwgx8MGNuvMx2MtbBWuDYeCEvF0MSA4fhP3XbP4qglYCiysTY508KcEEM_b3E4KRmmWLGy0TGvRM3sIv2V6TdToyLJIN2Jm2lgp7_FrxGCzKUl_CYHUcMgAKF9XXYXIL49oNMfDy_emyRlybtDJ1j3fLbx2YOECFOyVZ0xRKGYAXjhDyMXILFQwDjzJTPY7bAU4Q3e00q4Na1_FJ7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
ما برای آقای فغانی عزیز اين چهره محبوب ملت‌ ایران آرزوی سلامتی و موفقیت‌روزافزون داریم
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/68333" target="_blank">📅 11:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68332">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b51a5dfa4.mp4?token=OCQfHu6v1UjVsZlBGq9SAnDymjqLF9pnQEj_9sSnweUq0ODtNyGUW4fkGgHsREgy2wLrKiUUzBC1pWkN5EaV26Ame-9MCDyorSWbzu1dAnzgP96aLzRwXG7Iwp5adXJ028uc6I9zDHbCdO9zjhA_Hc44u0Y6azqVsR2aHNEmiobb8gZaE-Rq8bYumr0GvD1bRvPV39FAw6ASZJ4tFRVsWi89Du03_5zAPcofel64mIJ-xdg9NPcGYnmhcoSI7gvTJBQJeRMZ06xk_4lgTeF9a3VVacF0yFdB9aHWmDOHfcRbm9nJGB00DP_XNpkp2iB1TaG4Ya9DveEL64flYreWOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b51a5dfa4.mp4?token=OCQfHu6v1UjVsZlBGq9SAnDymjqLF9pnQEj_9sSnweUq0ODtNyGUW4fkGgHsREgy2wLrKiUUzBC1pWkN5EaV26Ame-9MCDyorSWbzu1dAnzgP96aLzRwXG7Iwp5adXJ028uc6I9zDHbCdO9zjhA_Hc44u0Y6azqVsR2aHNEmiobb8gZaE-Rq8bYumr0GvD1bRvPV39FAw6ASZJ4tFRVsWi89Du03_5zAPcofel64mIJ-xdg9NPcGYnmhcoSI7gvTJBQJeRMZ06xk_4lgTeF9a3VVacF0yFdB9aHWmDOHfcRbm9nJGB00DP_XNpkp2iB1TaG4Ya9DveEL64flYreWOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
وضعیت پل کهورستان در محور بندرعباس شیراز بعد از حمله دیشب.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/68332" target="_blank">📅 10:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68331">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuMyvMH0SSB_MAKNRGXMROldacrxD1MsTAbb77lw9-2UH-Jz9myIWDtaNBRmFvbTDs7poi5vhngeUlQ_yetQ6TiGhX5Hi-h191Sv5qVutEzJiusieqVlUQ1USizLXGfpekeC1XBNr4THYQhDRljRzoZCOtcIrKtT3r_B9OGkGEKirCPm6YNfE6qdiABBCoboshgfZK8O22RCIGzq32Up7kpvtkQFlmvU30JlSsQ5bY9FCttZOpI9e5ELMmXMfGCYTzLp5mzgSIhzZcufrfaQIFmUpQ2TVLQL9ShmfupaDRMWLq3d3oqdVOGguI-tPsRFgpkmsq29eu564dno1mHfbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وال استریت ژورنال:
به گفته یک مقام ارشد آمریکایی، ایالات متحده روز پنجشنبه چندین پل را در ایران هدف قرار داد؛ اقدامی که با هدف قطع مسیرهای تدارکاتی به یک شهر بندری و پایگاه دریایی در تنگه هرمز صورت گرفت—مراکزی که ایران از آن‌ها برای حمله به کشتی‌ها و اعمال قدرت استفاده می‌کند.
بر اساس گزارش سازمان صداوسیمای جمهوری اسلامی ایران (IRIB)، در طول شب پنجشنبه چندین حمله به پل‌ها در داخل و اطراف شهر بندری بندرعباس گزارش شد و بزرگراه‌های متصل‌کننده بندرعباس به استان‌های همجوار مسدود اعلام شدند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/68331" target="_blank">📅 10:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68330">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e60e986837.mp4?token=hwM-u1M_tgAx3N9kJfXmevyNUw-4eryXbdr3uBaUQRuA99w8jCuhD_dmo6Be7H37RBdBfv04WGXMRgARDgcCMsik70MRjJepbEskzS_okN_lcnj6UHQYHo7anAIZ7HDDVX4T6nN0cd_sIUEH5M4SxOqSgBDxeW6uL8dc5JNk8uMtN9Dqi2n2Ea7UJBs-gsWoByyarAreTL6WqYy2LmeqDAFtLhPQbNGhiHOZSCrc1F10s_OWOwMlTcHHetIYD2-WPj8tYjvUHEeoKTZprCW551Ht6PBVp7nHDbgZoVoYVMyAo9bmZFKWbdpFA8Js1ZRJRB0XJOVhDcgcuUbDrOqEyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e60e986837.mp4?token=hwM-u1M_tgAx3N9kJfXmevyNUw-4eryXbdr3uBaUQRuA99w8jCuhD_dmo6Be7H37RBdBfv04WGXMRgARDgcCMsik70MRjJepbEskzS_okN_lcnj6UHQYHo7anAIZ7HDDVX4T6nN0cd_sIUEH5M4SxOqSgBDxeW6uL8dc5JNk8uMtN9Dqi2n2Ea7UJBs-gsWoByyarAreTL6WqYy2LmeqDAFtLhPQbNGhiHOZSCrc1F10s_OWOwMlTcHHetIYD2-WPj8tYjvUHEeoKTZprCW551Ht6PBVp7nHDbgZoVoYVMyAo9bmZFKWbdpFA8Js1ZRJRB0XJOVhDcgcuUbDrOqEyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدباقر قالیباف، تیر 1403:
ما غنی‌سازی را بیست درصد کردیم جنگ شد؟ شصت درصد کردیم جنگ شد؟
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68330" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68329">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47f00f211.mp4?token=IhPoOaYUXpRgSRN8spWbhoWVHb0lLtcQixHeLGZwEld_9fFPa34dqc1f-2IJ4YowEBW_cOmFYPW2AZFRqAAmSnoKJ6Hphx4FXldKA3OEvRjeBznfWlsUf69wRf_6PjZSiKJqB2VznAoUAj1v9b6_NHab_JKPkwcWBRdLvuG7HNZVxcrJffjzdGFLzX_C1rW-1dM1gR6FPBOMImoBzvcL63Qt3nFF0onvDf7_mUpqDfHYEwceKwLqwbGT1u8bP8N-GVgQ5DIBBN0VcCf105tyRNslWzauayZIRGyPuFjpT1RdxuwUZv9zstuCFCtEe-PNhdyL_ZI7vLy6jlACcdji2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47f00f211.mp4?token=IhPoOaYUXpRgSRN8spWbhoWVHb0lLtcQixHeLGZwEld_9fFPa34dqc1f-2IJ4YowEBW_cOmFYPW2AZFRqAAmSnoKJ6Hphx4FXldKA3OEvRjeBznfWlsUf69wRf_6PjZSiKJqB2VznAoUAj1v9b6_NHab_JKPkwcWBRdLvuG7HNZVxcrJffjzdGFLzX_C1rW-1dM1gR6FPBOMImoBzvcL63Qt3nFF0onvDf7_mUpqDfHYEwceKwLqwbGT1u8bP8N-GVgQ5DIBBN0VcCf105tyRNslWzauayZIRGyPuFjpT1RdxuwUZv9zstuCFCtEe-PNhdyL_ZI7vLy6jlACcdji2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تصاویر ماهواره‌ای نشان می‌دهند که آثار سوختگی در محل حضور یک سامانه پدافندی پاتریوت آمریکایی در فرودگاه اربیل عراق وجود داشته و احتمالا این سامانه  بالاخره توسط پهپادهای شاهد منهدم شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68329" target="_blank">📅 09:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68328">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68328" target="_blank">📅 03:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68327">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SPm_UAYh2Gd1MRgikMhNpExMzyyghabpA8rKv8rKVj2M6BIAdiPeyb4AaPMwVhjBNVVFeiFmqEUMyHK3virBFfmNMFlknWGzmSu6Ufn7mRnX6HAV-m8d2kYUQuImEX0PDaWUs4HjEA3uFNuBei5Hq0eiDRBfBApxidBUpSHvKXpTB1-zLm-9k8APPb0pIpZMrIlZvdGE85bIGFmdG58bpa9kC025WrvIvJLuUqG70t2WdvlrGZCsZsEbw6W0jUWMapaBka3xQFyZsy7Da-dmJwP_jvKLxtCraVulb3WF7X8z4BgPYC7UjAv5bjA7D0EOgW1C5ZJG6i3qqaA_6zpiOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68327" target="_blank">📅 03:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68326">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
از سایت موشکی جم چندین موشک شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68326" target="_blank">📅 03:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68325">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bee400515.mp4?token=I-3_bA4tZw3LmCHDitAtBatEZrZxYYdMEsmMHfcobmWxuyFnuEu3nFZXRiZp6Pqs14uFZTT7rEcdJ5gYhvHYh9levga85I-B-dBVa4wPOMDOMTOlby1SmarY77DrkqsarOOPDvMT4eIsK9iELVsYM_Lo8hBuR9X9nwflmt8pBz0fjqLjNtIr6g6J2UBP9lv3w5ATXOjHX7EBVlBUxheu3jlnFmKYn748P-HW2fYU7CpC8ltYt0EXYgvKMsX-41ijEVP2j1cvfelHnqYNAFrvM_NEfreCKTPKuWA2Pc3geNTni3MtySI3_mLys3n3UQWw_tpeBIGPgMTcyZ0Wd-y-rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bee400515.mp4?token=I-3_bA4tZw3LmCHDitAtBatEZrZxYYdMEsmMHfcobmWxuyFnuEu3nFZXRiZp6Pqs14uFZTT7rEcdJ5gYhvHYh9levga85I-B-dBVa4wPOMDOMTOlby1SmarY77DrkqsarOOPDvMT4eIsK9iELVsYM_Lo8hBuR9X9nwflmt8pBz0fjqLjNtIr6g6J2UBP9lv3w5ATXOjHX7EBVlBUxheu3jlnFmKYn748P-HW2fYU7CpC8ltYt0EXYgvKMsX-41ijEVP2j1cvfelHnqYNAFrvM_NEfreCKTPKuWA2Pc3geNTni3MtySI3_mLys3n3UQWw_tpeBIGPgMTcyZ0Wd-y-rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68325" target="_blank">📅 03:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68324">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه پاسداران به بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68324" target="_blank">📅 03:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68323">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">روز‌ها و هفته‌ی آینده بشدت مهمه، مردم خیلی بیشتر از جنگ ۴۰ روزه ترسیدن، و مسئولین علاوه بر ترس، بشدت سردرگمن، امکان یه قمبل‌قهرمانانه‌ی دیگه وجود داره #hjAly‌</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68323" target="_blank">📅 02:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68322">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اگر بخوان به جرایز مهم جنوب یعی تنب‌ها، ابوموسی، فارو، سیری و حتی هنگام حمله کنند باید جاده های مواصلاتی بندر لنگه رو قطع کنند؛ امشب زدن پل بندر خمیر به بندرعباس، مهمترین جاده مواصلاتی بندر لنگه رو قطع کرد.  #hjAly‌  @News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68322" target="_blank">📅 02:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68321">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g53QVvz594KOjZjlDBgVrF5SvZDZpPCG-7XKGcwFq-UF14Y8UZG-Ly6sXguZF_QWGxha8_E4UonkIeyYpkmH26WnNAIcuVfH2E-uGGwTLgqgNl89510MF2bay9tavUbRgUNvV75s05HYuCmJ0OkVwxZipzoyRZ-69ZVfuKhLqcqj-DTc63TE-WhVCJUfvklxWngppK0DLMyh2noHezxhNmjD_RjThaVjrLBB8TvbbGnH3GQs7kcWuUKcr8oP8Xj-KeHFLpuFM673VQLhBJy1Ffbh2EgkfuZXY7Ak5BpaFw2mxJ1gfBhDrzHNkJxex2d9XMFne78JDxAZkdo0N6QhuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر بخوان به جرایز مهم جنوب یعی تنب‌ها، ابوموسی، فارو، سیری و حتی هنگام حمله کنند باید جاده های مواصلاتی بندر لنگه رو قطع کنند؛ امشب زدن پل بندر خمیر به بندرعباس، مهمترین جاده مواصلاتی بندر لنگه رو قطع کرد.
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68321" target="_blank">📅 02:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68320">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=Rp1DA2SUkQUihrkFHDbVqwmO_rtP0PbEuKKKRZYVs0HJIWWrCkNxIyN8Z_fdYoPHZb_OD4zL7Kk75xT8BQc12UqrUiH4Ny7lIBB5c7TQpQmLcu_qnI_Yul9BRIkBpvibhR7rU8r_F-qr2Q4eTKrcipXVa4Pfnj8jwcu4NUGJyPjzkrz9ByxhiDZlqyo4mQksgYVOjOGo45MQkvVr18874ncXpfI2D9qrVGv8n2PeiH86Ys3KIpVsoV4IntVwPSZcKwjwUthu8UrT3jzIJdRR71zGJm5gdxeMt0yPszJmVBTwTq0LD1eKkDV0ZVc3doYZSSGqlQK2cPP5H6xQ6fKU3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=Rp1DA2SUkQUihrkFHDbVqwmO_rtP0PbEuKKKRZYVs0HJIWWrCkNxIyN8Z_fdYoPHZb_OD4zL7Kk75xT8BQc12UqrUiH4Ny7lIBB5c7TQpQmLcu_qnI_Yul9BRIkBpvibhR7rU8r_F-qr2Q4eTKrcipXVa4Pfnj8jwcu4NUGJyPjzkrz9ByxhiDZlqyo4mQksgYVOjOGo45MQkvVr18874ncXpfI2D9qrVGv8n2PeiH86Ys3KIpVsoV4IntVwPSZcKwjwUthu8UrT3jzIJdRR71zGJm5gdxeMt0yPszJmVBTwTq0LD1eKkDV0ZVc3doYZSSGqlQK2cPP5H6xQ6fKU3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68320" target="_blank">📅 02:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68319">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a3e60cce.mp4?token=XW4OYRDWEIcvDgby5FG0PCYp22hGunylWu6C6JmcfnRZxboMG9jcLT4J23qluMbBi3rf9Cpw8eVzENMzMdbiUOpqgabXeJKKoLeKdTG_kBimy_HnxI9D46G4xxLZZbqRXmct5mkxZV_laz4g1OrfUxdXYWedna397Mi-zJwBb5UudaTldDb7A0C4VqV-1OTLRmt-apW8MfUCdpWQ3AKIMiKt4ezdB49iftIPyzXerxFDrjbXLR7ConQV432rUb9E0GgfW1Vv-km-bXpZvvZ_9wt2x3hatPMe4z8eQnkGE353CbUKxPDI4lUKfUIEr7ch-6Cvhw5UeSnwOlowDFpSmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a3e60cce.mp4?token=XW4OYRDWEIcvDgby5FG0PCYp22hGunylWu6C6JmcfnRZxboMG9jcLT4J23qluMbBi3rf9Cpw8eVzENMzMdbiUOpqgabXeJKKoLeKdTG_kBimy_HnxI9D46G4xxLZZbqRXmct5mkxZV_laz4g1OrfUxdXYWedna397Mi-zJwBb5UudaTldDb7A0C4VqV-1OTLRmt-apW8MfUCdpWQ3AKIMiKt4ezdB49iftIPyzXerxFDrjbXLR7ConQV432rUb9E0GgfW1Vv-km-bXpZvvZ_9wt2x3hatPMe4z8eQnkGE353CbUKxPDI4lUKfUIEr7ch-6Cvhw5UeSnwOlowDFpSmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
حملات موشکی و پهبادی سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68319" target="_blank">📅 01:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68318">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
در حملۀ دقایقی پیش به بوشهر چند فروند موشک آمریکایی به پایگاه هوایی و پایگاه دریایی بوشهر اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68318" target="_blank">📅 01:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68317">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
فارس:
دقایقی پیش دشمن آمریکایی یک نقطه از بخش ویسیان شهرستان چگنی در استان لرستان را مورد حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68317" target="_blank">📅 01:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68316">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed596f3009.mp4?token=IwVrbsOYV7AidQTZ_ovWmsou52Hfj0D2eAcW6f73M-kS6O0hKv879wV_Jcm8zQ9sj-qrs5nkNYb3ZAmYfLzrM0gjVQ39te5YS4Rkcz8D6iHLEsuCZ1CN1f402RtoCqxM4Ny3ShCEYfE7XoK9WgbXGyi2MAqjaKZAl4-85psx66-Ypo2MGCnnreqiGZm801KKWr9WvRV8MEH3OhOoxuawOhpp2glFvSTcbpR0cytt5yzEZHuRYY6Jojn4vU8FZ1MDFDvMBh0XWohSFUFIvJBRqPNqsMEXZHi5DNYWlkfqbzVcwWpNSTTdMYSDV25uZbhJa3Bw9Bw6Ov6Gdg0mpWCCjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed596f3009.mp4?token=IwVrbsOYV7AidQTZ_ovWmsou52Hfj0D2eAcW6f73M-kS6O0hKv879wV_Jcm8zQ9sj-qrs5nkNYb3ZAmYfLzrM0gjVQ39te5YS4Rkcz8D6iHLEsuCZ1CN1f402RtoCqxM4Ny3ShCEYfE7XoK9WgbXGyi2MAqjaKZAl4-85psx66-Ypo2MGCnnreqiGZm801KKWr9WvRV8MEH3OhOoxuawOhpp2glFvSTcbpR0cytt5yzEZHuRYY6Jojn4vU8FZ1MDFDvMBh0XWohSFUFIvJBRqPNqsMEXZHi5DNYWlkfqbzVcwWpNSTTdMYSDV25uZbhJa3Bw9Bw6Ov6Gdg0mpWCCjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68316" target="_blank">📅 01:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68315">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68315" target="_blank">📅 01:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68314">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68314" target="_blank">📅 01:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68313">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5f29b590.mp4?token=OePmuX4dWSXmS7BT8CaxiMy7QK5ILANFuk3ZhDu0VKFtH349m859jothFu7G7aRJrJ9m_VOJmraqhduMnhoFCPxdWIhtC0D_buFw5Da5_1WhfRObw_EfqGKVZWkBZUpk2XrgI3BwaHva49ElSjpjSon2c32YAJPeBbTl7Sa8BcdGCjgJS6G-gkkCYyntSaJ3Kx2Rykqr-7SXAFAz3Pk8g9oQnwitZHH0tTzsZep4vNZbvrSu2H0hY_jjQzP8Rafm_w1jp0-gs08aBg2ruYO7Rqlir2BcuutAz7jT58VP3miYfXUOHmV6ykY0y3siZJvdEGnAXe6w9lmYD7qs3QNGjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5f29b590.mp4?token=OePmuX4dWSXmS7BT8CaxiMy7QK5ILANFuk3ZhDu0VKFtH349m859jothFu7G7aRJrJ9m_VOJmraqhduMnhoFCPxdWIhtC0D_buFw5Da5_1WhfRObw_EfqGKVZWkBZUpk2XrgI3BwaHva49ElSjpjSon2c32YAJPeBbTl7Sa8BcdGCjgJS6G-gkkCYyntSaJ3Kx2Rykqr-7SXAFAz3Pk8g9oQnwitZHH0tTzsZep4vNZbvrSu2H0hY_jjQzP8Rafm_w1jp0-gs08aBg2ruYO7Rqlir2BcuutAz7jT58VP3miYfXUOHmV6ykY0y3siZJvdEGnAXe6w9lmYD7qs3QNGjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو وایرال شده از حمله وحشتناک آمریکا به بوشهر
شیشه های ماشین فیلمبردار درجا ترکید!
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68313" target="_blank">📅 01:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68312">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d811948267.mp4?token=psNCTgVd6LmQ2mVrbbsyEe8dKcKutWQrSJlz3S15hEZsotlJrBJoyb8DINqELnImz1GK-r4a77dz-oRseAxBliKwJbNs9BpCzx7SoNAwwFFr02GFd_n_L94a-gK0TxSmOJfc-N7abpOW4td_qp4iZY1D4GFbmVjEb_e4UpB82MkVRVdEKe7qxmLJhvxTeAyXxaYUZ3Se59_MKmgnY9xTMQcUIi58VGdhMHN7I8KYp4nSVINp39THDgAS7JNV2HzKOqW5NAuZmb9jfjrF6_x5xJJ6GGWemAhxFbRe0SiOLT7BxD6QM9TtqyZAoWPqTrBzr2RkxelRsLC8uPCgo-qGznq1IPOsVjEKtM_DZa7xP9J_EeFESAdVVi4dmKWO70LiucszqzqVR73GOaN7fKnHZh2kSdA7IaeYFl3Cb9E7OygrhNxonCZ31M3aKpnzAbCImNipL0V4U5pGb4OsFl5nd4sWVPHxO0szdTfcO-3MMJBYGgh1mcCIgqSGCITCa4emfZ8mqsQlw3wx8o_Dhw76KXVkH6qFox8OJYgFxkbvXUZCcPDZmJNi0mXzKulsQzQsH-lEy6pvAHEpy53XzH61fUEIvPilCjbCnfIfKEM477TCoh_ewCf8BPkV0LT4A8sxI0wkYJSWH3JfZ11FdRX0EJJ0hTTaoYlRq6ozmfZRrJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d811948267.mp4?token=psNCTgVd6LmQ2mVrbbsyEe8dKcKutWQrSJlz3S15hEZsotlJrBJoyb8DINqELnImz1GK-r4a77dz-oRseAxBliKwJbNs9BpCzx7SoNAwwFFr02GFd_n_L94a-gK0TxSmOJfc-N7abpOW4td_qp4iZY1D4GFbmVjEb_e4UpB82MkVRVdEKe7qxmLJhvxTeAyXxaYUZ3Se59_MKmgnY9xTMQcUIi58VGdhMHN7I8KYp4nSVINp39THDgAS7JNV2HzKOqW5NAuZmb9jfjrF6_x5xJJ6GGWemAhxFbRe0SiOLT7BxD6QM9TtqyZAoWPqTrBzr2RkxelRsLC8uPCgo-qGznq1IPOsVjEKtM_DZa7xP9J_EeFESAdVVi4dmKWO70LiucszqzqVR73GOaN7fKnHZh2kSdA7IaeYFl3Cb9E7OygrhNxonCZ31M3aKpnzAbCImNipL0V4U5pGb4OsFl5nd4sWVPHxO0szdTfcO-3MMJBYGgh1mcCIgqSGCITCa4emfZ8mqsQlw3wx8o_Dhw76KXVkH6qFox8OJYgFxkbvXUZCcPDZmJNi0mXzKulsQzQsH-lEy6pvAHEpy53XzH61fUEIvPilCjbCnfIfKEM477TCoh_ewCf8BPkV0LT4A8sxI0wkYJSWH3JfZ11FdRX0EJJ0hTTaoYlRq6ozmfZRrJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده آمریکا، دقایقی پیش تصاویری از عملیاتی که دیروز بر روی یک نفتکش ایرانی انجام شد، منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68312" target="_blank">📅 01:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68311">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دیشب که داشتم با دوستای جنوبیم حرف می‌زدم، می‌گفتن حملات بیشتر داره به سمت پادگان و و قرارگاه های نیروی زمینی کشیده می‌شه، حتی دیشب مثل اینکه به پایگاه لشکر ۹۲ زرهی هم حملاتی شده...
امشب هم که خودمون با چشم دیدیم ته حمله به پل‌ها آغاز شده...
حالا سوال همه الان اینه که آیا قراره بهمون حمله زمینی شه؟!
اولاً اینکه ما در جایگاه تحلیلگر نیستیم که به این سوال، جواب دقیقی بدیم، ولی شواهد اولیه داره اینو تایید می‌کنه، اما وقتی کمی عمیق به مسئله نگاه می‌کنیم خیلی موضوع فرا تر از چند تا کلمه‌ست و عملا داریم از یه لشکر حداقل ۱۵۰ هزار نفری حرف می‌زنیم، حمله زمینی به خاک ایران، برای آمریکا بشدت پرریسک و پر از تلفات انسانی خواهد بود، ولی اینکه دارند شرایط رو برای تصرف جزایری مثل خارک فراهم می‌کنند
اون هم به قصد فشار بر جمهوری اسلامی،
یک موضوع دیگه و موضوعی محتمله.
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68311" target="_blank">📅 01:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68310">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/861fef7828.mp4?token=bls9ncRUJZhEfgBYOdIsggx8twFExkpz2eXDRgYU4TzHxRt8LQEvYovqjhbX7cJIrR8cqDe2s4hwizlZBOOGffPwmSjbpjiuhxxlQQPxMqjr0Np5I36ZUHibTDMGfRJwb4CGbHx6CdHNWQDkMlHr81YKGu6ZFhLk-r5G4NpQrLA2af5iqRyBG1M8bKyQnX8OhYylylNiyuAR4ujXsw51vva0-GyMdMqqm-BTjUCsPQ3OMKfqYJdcfyHz7CVJrhWLJrXVMdIJs5xyMq3n_EjDDZ_VHskDVnYJk0ILQYaKFQmXNjw1g0alkpsZimUdhcTg8NCP4cgbMpX92zHzCDEO3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/861fef7828.mp4?token=bls9ncRUJZhEfgBYOdIsggx8twFExkpz2eXDRgYU4TzHxRt8LQEvYovqjhbX7cJIrR8cqDe2s4hwizlZBOOGffPwmSjbpjiuhxxlQQPxMqjr0Np5I36ZUHibTDMGfRJwb4CGbHx6CdHNWQDkMlHr81YKGu6ZFhLk-r5G4NpQrLA2af5iqRyBG1M8bKyQnX8OhYylylNiyuAR4ujXsw51vva0-GyMdMqqm-BTjUCsPQ3OMKfqYJdcfyHz7CVJrhWLJrXVMdIJs5xyMq3n_EjDDZ_VHskDVnYJk0ILQYaKFQmXNjw1g0alkpsZimUdhcTg8NCP4cgbMpX92zHzCDEO3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
تفنگداران دریایی ایالات متحده از «یگان یازدهم اعزامی تفنگداران دریایی» در تاریخ ۱۶ ژوئیه، عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «وِن یائو» (Wen Yao) در دریای عمان اجرا کردند.
تا به امروز، نیروهای آمریکایی مسیر سه کشتی تجاری را که قصد عبور از سد محاصره را داشتند تغییر داده، یک کشتی را که از دستورات پیروی نکرده بود از کار انداخته و برای اطمینان از رعایت کامل محاصره دریایی جاری ایالات متحده علیه ایران، وارد یک کشتی دیگر شده‌اند.
تنگه هرمز و آب‌های پیرامونی آن همچنان آزاد و باز هستند؛ مگر برای کشتی‌هایی که قصد نقض محاصره آهنین آمریکا را دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68310" target="_blank">📅 01:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68309">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
چندین انفجار سنگین در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68309" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68308">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVBqNEjct0iu3VwvMzsCtGFh2xg7PVaRwx8uPr6gaNa7_WESD2oxc5htInavXmBKPS1NIaaFhWFfzd0-DCA5hE8qf2Ke_BNaqoTMF1fb4IaXK4SATjNhf4I7_ohApw68UfvXq8bzELpBhm3NFtx_EuAqdiKp3DDEOu4P0VWUtdtpcd3ONhcxbajKqp9cvXRYa16LKXGFIfFD6iHhsCUOsXDv48_-Q1WGyvFfYQPnBxndHG4bQMrfmBaSLJUC5G-GVxc4jWa9yFYB6Dw5Yi9LtoTJkV8twdv1NzofRQrcdjGqoOSqe6ow1M-SdxxeN6vaNAzq-R6A_mxD2p3jqVdJtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تمامی پل هایی که بندر خمیر را به بندرعباس متصل می کرد توسط ارتش آمریکا مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68308" target="_blank">📅 00:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68307">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
دفتر فرماندار هرمزگان اعلام کرد که تا اطلاع بعدی، جاده‌های زیر مسدود خواهند بود:
جاده بندرعباس - خمير - لار به طور کامل مسدود است.
جاده کشار - کاهورستان نیز مسدود است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68307" target="_blank">📅 00:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68306">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYABo8Kl6_gfrKak7Ods_Lij3ygi3WkxRvMSaP-p3jWefwwZbb4D3XQL4mpnfuZ-ec65WcEAQqXXNUyEZCST6_-1UDjw5-8umKnHmZ7VZU3Gso98E26sctcM5c1XNeQctBrYWXM9Q6ZgKpqMEAXPujIdq6fmfZiqrsARobO9p_Bgor9czvqnpvVN5N-_DxszdsNKkA_kmSVejdlxSLi1k7CAOcSEgULTTjoExWfngPVg_FNcA4GxZXDr5TZvSTHEO-KNYlr440jRvotONJ1fAplxDJXHh2Mddi_m0Meg3yoLhZbF1RBHrdAAsU7KsfGfjUkxj_4YBRlfPnfRMf-eUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رشیدی کوچی :
⏺
«حمله زمینی به ایران از سمت جنوب رو قطعی میدونم و به نظرم تنها دلیل تأخیرش، گرمای شدید هواست.
به نظرم تمرکز حملات آمریکا روی مناطق جنوبی هم در همین راستاست و ایران هم تا الان با هدف قرار دادن عقبه دشمن در کویت و بحرین، اجازه ایجاد مراکز پشتیبانی رو نداده.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68306" target="_blank">📅 00:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68305">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLI7X-8wy0zlyu_pohhqfqugx_9Qd_QP-PvA6En1exGrN1AK6EXZyjTEYsK8jOuzMhgp3Jn2PsFa6hKjToeMpun7tlWzCuuoGMb2Q5HBCoCmDCEmvZlLBXCxLWAQj-bZ6FDztKK0ZkXRfoJlE2en09tvnev7p8oLD1-Xv_bC0mb0ttHR8j1gffNAQD8EsaIBNScWQoWNOJXOZnys-lEAoujCtaWYoyX57BOEBo6hqQ80R86xdxta6KxL8bUT1i35Yy0JahagKzPFAE0NVFhk3vxhnXaBXaBpkJ1HvpGi5oGmcuPD07y4ufg5V-rOqQ65ANC2LOPOlNn-umQQUfShIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وضعیت پل کهورستان، محور اتصال بندرعباس به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68305" target="_blank">📅 00:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68304">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dX9bB_aVybAN4sjv3AZoAUyMslne_opfgrWk73V0iKqLqD68mIv1IHwlphN8_HvZzpkl5goN_sEMcDB4kNHu79X-Ba1Fye_5rp4egyziTuTEn9oNiCfetmf87QZ1hmcUgKmoIxfsjjxoX_UZl1_ThlvbBmCEAb-QdAmFBY6ORlOt6KKRYG96bbPDEWvfh92j0tmH0DQ32Kx-GIfBYC6aanV5wquwAip5I0lDrafGkoWh3Ry4s1b3yBttE6H6kPU62hwVdgKoTyZNRic81Fn7KXD704DHaDsoMDz2LH3o8XHH7ewI5AkTrId0rfgZCabBV6OGBuz0XX-lyYWQpEnQCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
راه‌آهن بندرعباس مورد اصابت قرار گرفت   @News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68304" target="_blank">📅 00:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68303">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
راه‌آهن بندرعباس مورد اصابت قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68303" target="_blank">📅 00:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68302">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f357e145.mp4?token=RXLV5KSMaCceQzIfZoooNoeNPiwmh11sMH-0Y78UbixBacWER8Cq__DFA3h-bREYTovZwdfmKzhBVj0a0jPHx0cE-1mVbUN5cZbG5KbzCnQTN4jeH0HzioczfGc1T8HaFd6mQIndmgvVqnf87K9xPrgr2dXtKqssxFApsW4eBXA_nuhkzoOhpd45JkQLlrnjsjQTjV5T2j9V-hFsAE1mAEY_ntDSRcn2KJUXO-PUVbvS0b5BM5N-jBNXqrGuSo2ZPweOmGyrtGiF-llnybJM7JANgjhCiDnxLtEsFiumBSeP4zc6PrzKkdcjZp93BM5Uj4WfczEEN6rM-xnx50Nrog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f357e145.mp4?token=RXLV5KSMaCceQzIfZoooNoeNPiwmh11sMH-0Y78UbixBacWER8Cq__DFA3h-bREYTovZwdfmKzhBVj0a0jPHx0cE-1mVbUN5cZbG5KbzCnQTN4jeH0HzioczfGc1T8HaFd6mQIndmgvVqnf87K9xPrgr2dXtKqssxFApsW4eBXA_nuhkzoOhpd45JkQLlrnjsjQTjV5T2j9V-hFsAE1mAEY_ntDSRcn2KJUXO-PUVbvS0b5BM5N-jBNXqrGuSo2ZPweOmGyrtGiF-llnybJM7JANgjhCiDnxLtEsFiumBSeP4zc6PrzKkdcjZp93BM5Uj4WfczEEN6rM-xnx50Nrog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو دیگر از پل کهورستان
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68302" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68301">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
تسنیم:
آمریکا شروع به زدن زیرساخت ها و پل ها کرده.
اونا به شهرستان بندرخمیر و بخش کهورستان حمله کردن و پل ارتباطی بندرعباس به شیراز که معروف به پل بندرعباس - کهورستان - لار هست رو هدف قرار دادن.برق مناطقی از کهورستان هم قطع شده
.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68301" target="_blank">📅 23:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68300">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=Hfn8OINgK9Ax9fhgLRWefnnzsCtCfYBhPCm_MZ7Qg7w2WzcB2KMmB6ZgLy1lBBOe-5wVGFWOB9jEnnPhIt_KYkyyttvpskDj1brd6yEhH47bpUl7Qf7FtqyApZZZgNqpd_sLSo31SifZ229vDZXu02V-SF0OyIcGaChlA3sFn0Rr-rqHxNJ1CHoxys1hny_s0xsuxSdfM-Nln44yjRS2TBeDJQkRuzJf0S-G2kBDkJZcECgxxbYTE3Vdu6k23B8V9ZT2ULaekiAC7Bj7ei4DdD3ylTMAuqwpIBOgJsLs0sblYEMfiGmt53XDoCMuaHS8m_cB1THIZmJhFACwfM91Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=Hfn8OINgK9Ax9fhgLRWefnnzsCtCfYBhPCm_MZ7Qg7w2WzcB2KMmB6ZgLy1lBBOe-5wVGFWOB9jEnnPhIt_KYkyyttvpskDj1brd6yEhH47bpUl7Qf7FtqyApZZZgNqpd_sLSo31SifZ229vDZXu02V-SF0OyIcGaChlA3sFn0Rr-rqHxNJ1CHoxys1hny_s0xsuxSdfM-Nln44yjRS2TBeDJQkRuzJf0S-G2kBDkJZcECgxxbYTE3Vdu6k23B8V9ZT2ULaekiAC7Bj7ei4DdD3ylTMAuqwpIBOgJsLs0sblYEMfiGmt53XDoCMuaHS8m_cB1THIZmJhFACwfM91Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
در کهورستان بندرعباس یک پل هدف گرفته شده.
موشک خورد به وسط پل، تانکر سوخت نابود شد، راننده مرد، یک تیکه از پل نیست، کسی این طرفی نیاد...
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68300" target="_blank">📅 23:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68299">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
پل ارتباطی بندرعباس به شیراز و معروف به پل بندرعباس - کهورستان - لار مورد اصابت قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68299" target="_blank">📅 23:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68298">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a71beb824.mp4?token=hUQNmgKSWP4YI07ydQQlIrZZII3_HAvZhh7pcmMj1o04YR6MG6ubE8Mdjil4kFFmkHHLPH7UJvJLb07uWUIIpMi4nM16jorG00oHYc6UB1HQ1GhiBh6xTdJHf0-nGwXLtzOlOKJI1EIbzKlnSlpHpS01vgQgZeSK2sZsyxPwMnVjFNfZyZA7f4R4bJOtOe0jvBk6SR-sqh51D38GLPnTqIz2KpPfViQjj6XB4VXJi6OONsnqXH4drg887zBq3lpKd7tX1H3IKXFywjD-wwLNFaLZr0x-0_7aANG-kQDS2PinbMmVHWxO9_q211Ifl3poEtuYSGn-QnZ_Mzj7q063GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a71beb824.mp4?token=hUQNmgKSWP4YI07ydQQlIrZZII3_HAvZhh7pcmMj1o04YR6MG6ubE8Mdjil4kFFmkHHLPH7UJvJLb07uWUIIpMi4nM16jorG00oHYc6UB1HQ1GhiBh6xTdJHf0-nGwXLtzOlOKJI1EIbzKlnSlpHpS01vgQgZeSK2sZsyxPwMnVjFNfZyZA7f4R4bJOtOe0jvBk6SR-sqh51D38GLPnTqIz2KpPfViQjj6XB4VXJi6OONsnqXH4drg887zBq3lpKd7tX1H3IKXFywjD-wwLNFaLZr0x-0_7aANG-kQDS2PinbMmVHWxO9_q211Ifl3poEtuYSGn-QnZ_Mzj7q063GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملهٔ آمریکا به یک پل در بندرعباس.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68298" target="_blank">📅 23:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68297">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
طبق گزارشات اولیه، یک پل در بندرعباس هدف قرار گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68297" target="_blank">📅 23:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68296">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
به گزارش ممبرا ساختمان مخابرات بندرعباس هدف حمله قرار گرفته
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68296" target="_blank">📅 23:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68295">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
حمله به ایرانشهر سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68295" target="_blank">📅 23:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68294">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlmKQl0rPFR9GUQN2SjW7LupPlN5LlGQxQrCNjT8o2KlmC2B_8ZjW15UMdFs1Mq5ITXCftBdaesQIT3KwheqQ3We2HGN43pkC3TJgiGEQgqHQb5hqjRE5y5MNzV1fHgtCVjlWTfOATpEcnfjKPMs21ey2BEbz57ugxKAEHiaTJ_yrR-yHWxLtLIP3Ubms7cGFLZYAwOtmF-FlBRhuCZ6JJMLKN2iab25rGfYJ0gPz-hd1e6LAikORqRCrP18koBFudhW--u-HzdqRwh-Eg7SrghTtGdEh58-Gw4nS2pOhi5oFFuebPcCkKmQwJWPvr_CZWP7WPyFh9GVokHMdXl2IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ستون دود در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68294" target="_blank">📅 23:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68293">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3vv8hAGag9uZEfPf648_9EnMJVg2Yh7XllqhVfXh634SWD8GmblQq8D1fp94dZ9vliapjEzXoYah2ra0u5RYvDSg8KFhUJ8dygcvQYO9Hu-G49QigeNJjTvDhkvlpwwxm338VGD3-oekmSyUBRuUfDhIVDCqZpUcXGJpTSaIUPOzxDuwTsCkGQIQnCKzH0nLMGqH7l8PnJgNhSi2EcLob7s9uW_eO1DSDLm1RDwDOcYF34Q4yhBZeQWSZWwT75rq7OwgM6o_LJsY-z-vh5q3zn8NWV_RUOEs8X5P9zlsvP7MZsPHYP8CVK4UA8GHWl-80olOoD0_UiXkuEUf64WsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وزارت دفاع کویت:امروز جمهوری اسلامی چندین تاسیسات حیاتیمون رو هدف قرار داد.
از سپیده دم امروز، نیروهای مسلح 32 پهپاد متخاصم را در حریم هوایی کویت شناسایی کرده‌اند؛
این پهپادها رهگیری و با آنها مقابله شده است
این تجاوز شنیع ایران چندین تأسیسات حیاتی در کشور را هدف قرار داد.
علاوه بر این، رهگیری اهداف متخاصم منجر به سقوط آوار در مناطق مسکونی مختلف شد که خسارات مادی به بار آورد، اما خوشبختانه تلفات انسانی نداشت.
نیروهای مسلح بر تعهد مداوم خود به انجام وظایف و تکالیف خود با کارایی و شایستگی، حفظ آمادگی و آمادگی مداوم برای تقویت امنیت ملی و حفظ ایمنی شهروندان و ساکنان تأکید می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68293" target="_blank">📅 23:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68292">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
پنج انفجار مهیب در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68292" target="_blank">📅 23:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68291">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به قشم و بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68291" target="_blank">📅 23:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68290">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS-</strong></div>
<div class="tg-text">داداش ما الان تو کوچه ایم تو اهواز بچه کوچیکا ذوق صدا بمب رو دارن</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68290" target="_blank">📅 22:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68289">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
اهواز رو دارن شدید میزنن همچنان  @News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68289" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68288">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14dca3521c.mp4?token=GXd-8V4-vzLnMPPz69l2AdQVE4EEk0L_Sn_-E0SBBxqXp3tLVLFQfpKp7gNrltq6v1RD1lV5w8P3LzgHir6D8YzjItNFarGA8b1HI_dYzMsV1KxL_Llsfj3RRFb7DUnTiKF9E7uILAIBF1jyK9um5Lt9a9HeJMj-M6YkhnmozcKEbx7cuC39RRJttRdW28PrYZoxgjBOkW4lHvwim77z1FlXC9P5XRY-y1UxcVITreFGpaEDTsH-0NS68EP7hJXyoTi5uPUzGNktWJWDlnXfTPCeh3jkFwS1YFaIc9b2s8OH-B4shZEodwQVLOCEyjCXOQwv19Adnu8P5R251begIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14dca3521c.mp4?token=GXd-8V4-vzLnMPPz69l2AdQVE4EEk0L_Sn_-E0SBBxqXp3tLVLFQfpKp7gNrltq6v1RD1lV5w8P3LzgHir6D8YzjItNFarGA8b1HI_dYzMsV1KxL_Llsfj3RRFb7DUnTiKF9E7uILAIBF1jyK9um5Lt9a9HeJMj-M6YkhnmozcKEbx7cuC39RRJttRdW28PrYZoxgjBOkW4lHvwim77z1FlXC9P5XRY-y1UxcVITreFGpaEDTsH-0NS68EP7hJXyoTi5uPUzGNktWJWDlnXfTPCeh3jkFwS1YFaIc9b2s8OH-B4shZEodwQVLOCEyjCXOQwv19Adnu8P5R251begIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک از کویت به خاک ایران
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68288" target="_blank">📅 22:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68287">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
اهواز رو دارن شدید میزنن همچنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68287" target="_blank">📅 22:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68286">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
دو انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68286" target="_blank">📅 22:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68285">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=a-jbE6nmkJCiKXgURh_Zg0fzYKednzjaKbpOaPHU8C531WkdgVAOPrB9NkunebMZ7eiHBlRNC3Ap9bX6sBGxD8vRHpHcGX4PEZNIUG3lo85haoLzv3RAxcxL-SQHdGJCgd5q7l-h8r7NGdpLnPfVi4WgE0HSqnj746i1x7HQpLbGrOZ1MLrjgUG9s50oqU7WyIPOwKAFy-C20yAHCU-0nfVYZAp0Ky5zIhONNdq32TNtvla-qaJqMwAmOTr3cIKhzNXc9xuDpVXT0OjtJs7k4FIiSNsNK3CkDoMGgKKWW0QNIqvhf3fvHLHfJRYbDFhqTLrSCUgaHaSzk2dnBNBDLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=a-jbE6nmkJCiKXgURh_Zg0fzYKednzjaKbpOaPHU8C531WkdgVAOPrB9NkunebMZ7eiHBlRNC3Ap9bX6sBGxD8vRHpHcGX4PEZNIUG3lo85haoLzv3RAxcxL-SQHdGJCgd5q7l-h8r7NGdpLnPfVi4WgE0HSqnj746i1x7HQpLbGrOZ1MLrjgUG9s50oqU7WyIPOwKAFy-C20yAHCU-0nfVYZAp0Ky5zIhONNdq32TNtvla-qaJqMwAmOTr3cIKhzNXc9xuDpVXT0OjtJs7k4FIiSNsNK3CkDoMGgKKWW0QNIqvhf3fvHLHfJRYbDFhqTLrSCUgaHaSzk2dnBNBDLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68285" target="_blank">📅 22:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68284">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68284" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68283">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOUvHd9SqoLBQ4jnoUjJDXFNsy-Sj92DMhuOtZtQ4zlCNF4l3k9mLh6ejMXLEOw-my-tFZwJ-3VGlXZtR_HOE0FU4tVmj2SytsvGq4dDJgM7CZ2LO1AwhxpPsk2dFn7cfEjzTSV4xKzbazmAqhtgbIricy68agcaPa7WgAGcBBvTUsU3ofdqPK6hM5ujuASkGKrMldmq281TF-Yf6h3j5syIdliZWP12srI8Bb-9prOL2XERMjazwKdBlPEcyDqyeaWrU6xRQiMX83lHRMu7ImRbFosyRvuCKQASBjHAgKn2aiFUp3BRXR1JPyZ83BzXKxcmDbmeNp1dDF3kn2cSXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگه آنلاین‌شاپ‌ داری این خبر مخصوص خودته!
اگر فروشگاهت تو تلگرام، اینستاگرام یا بقیه‌ی شبکه‌های اجتماعی فعاله، حالا می‌تونی بدون نیاز به سایت درگاه پرداخت اسنپ‌پی را فعال کنی.
✨
امکان خرید ۴ قسطه برای مشتریات
✅
فعال‌سازی در کمتر از یک هفته
✅
افزایش اعتماد مشتری به پرداخت
✅
بدون نگرانی از فیش‌های واریزی نامعتبر
🔥
همین حالا ثبت‌نام کن ‌و درگاه پرداخت اسنپ‌پی رو به فروشگاهت اضافه کن:
👇🏻
https://l.snpy.ir/i1ekm</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68283" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68282">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c56cad1a2.mp4?token=ikhsy9vaAa_5nMkz0K2dIHVBJybTx3hCr3kf8fP6K5GPFPRmJsXwuvsSLs6Ay-Ptg9HVOtLKaN6C4ZFr6CaJve0S_fbw1r-xyiNMciPqvesezmaOzNQtZLZYrZIFOAAPyQ-G6En0WtDsK1A5gmLET0PGTg8IiZyTwyN-EqyoCzBylSn28p0UHRnrEhFgQ9X5cLFfk1aSaGL5NG-tXJhQCP23DtVbdWU7tvYag8cKMyM8s2h9SbxXbb-IV6_R0I7NSz1oYNjOnEjyrXtSWc7Zy_4Afvf3yXXWCKoFiM6g9SHPOwmfEF2GRDerVqSTpkokbeu0_1fFNqHnFJpeSBAlOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c56cad1a2.mp4?token=ikhsy9vaAa_5nMkz0K2dIHVBJybTx3hCr3kf8fP6K5GPFPRmJsXwuvsSLs6Ay-Ptg9HVOtLKaN6C4ZFr6CaJve0S_fbw1r-xyiNMciPqvesezmaOzNQtZLZYrZIFOAAPyQ-G6En0WtDsK1A5gmLET0PGTg8IiZyTwyN-EqyoCzBylSn28p0UHRnrEhFgQ9X5cLFfk1aSaGL5NG-tXJhQCP23DtVbdWU7tvYag8cKMyM8s2h9SbxXbb-IV6_R0I7NSz1oYNjOnEjyrXtSWc7Zy_4Afvf3yXXWCKoFiM6g9SHPOwmfEF2GRDerVqSTpkokbeu0_1fFNqHnFJpeSBAlOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ستون دود در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68282" target="_blank">📅 22:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68281">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTmQk7xc1hOHQ2iDVqpz09tzG_mC8N4upPGZN2rWuMUqdR2Q4KxVo78j_PskbP_C6qfALE1w_Ww9MJZVi4XJ673XUQpL_A9kW9d3MHB6BbVk-9ikS2k8SpMg64CIKcZvQlDYc9t7z-fI0VNd7jmnZkEfF_bu0rzTMxB7Av-aaeJDH0czQ-zrUZoUIU71TtcFeUGxieripPsBYCixMG9DfLNPu1N7nWfjsv1_6tB1j3kJM8qbC4kqcEDmXpHUcpIAe2eg-8mp94wZX5P99S71qdVle-HWnmsrDOcxr4mpQgyeb-zQwcKqM16RtkYSNbCmrHRoZfN9CuEtPb1oPREB-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۲ بعدازظهر به وقت شرقی، نیروهای آمریکایی برای پنجمین شب پیاپی موج جدیدی از حملات را علیه ایران آغاز کردند تا توانمندی‌های نظامی ایران را بیش از پیش تضعیف کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68281" target="_blank">📅 22:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68280">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🇺🇸
رسما دور جدیدی از حملات آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68280" target="_blank">📅 22:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68279">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68279" target="_blank">📅 22:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68278">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
پنج انفجار در بندرعباس گزارش شده
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68278" target="_blank">📅 21:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68277">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
گزارش های اولیه از انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68277" target="_blank">📅 21:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68276">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4cdbbb0c4.mp4?token=G0N5HLdXKlmJgLzxwoZWF3HyJSQjOVZ28CX48WmvXW_HTvaCB69CbZ3fk3MQErtANmpY752WR-dnmU7qByWSSkjyVRubClACU6blJV0vMgHNtWBGEeEkcrcdLTrfDETbeAVjESf6iio15-rfHfmIJ9V9qBod2_1uypIt4J-JPPDNrYeo1xCIXRWlcSnt3WNIWKOPJRoS3JTCFfiX6lrGF8SGpDA0i65fSUyCdVNzYjjSlO-VWnJoaD-meNffFHHRCx5OD4lziyznravftSP2eEzZb5Ga4-p2xlBPmqbI8tuPFzrYtSCUfzlwclebcboEtwFitVzm8CiBf06DAYLJow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4cdbbb0c4.mp4?token=G0N5HLdXKlmJgLzxwoZWF3HyJSQjOVZ28CX48WmvXW_HTvaCB69CbZ3fk3MQErtANmpY752WR-dnmU7qByWSSkjyVRubClACU6blJV0vMgHNtWBGEeEkcrcdLTrfDETbeAVjESf6iio15-rfHfmIJ9V9qBod2_1uypIt4J-JPPDNrYeo1xCIXRWlcSnt3WNIWKOPJRoS3JTCFfiX6lrGF8SGpDA0i65fSUyCdVNzYjjSlO-VWnJoaD-meNffFHHRCx5OD4lziyznravftSP2eEzZb5Ga4-p2xlBPmqbI8tuPFzrYtSCUfzlwclebcboEtwFitVzm8CiBf06DAYLJow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کارولین لیویت سخنگوی سفید کاخ سفید:
«ایران همچنان به شدت با ایالات متحده آمریکا در حال گفتگو است و ابراز می‌کند که خواهان توافق با ماست، زیرا آنها از سوی نیروی نظامی ایالات متحده ضربات ویرانگری را متحمل می‌شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68276" target="_blank">📅 21:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68275">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8bf2cd6a1.mp4?token=dh3cRCFuFr95jdpwlF5Uir4QBNyhqs4Hm9CnP0t4xYdXkxa9vi5XtDT5ABeIjAVbfm7zFTe6djcncigiPr5bA18UBbMvlX9upVBVDPcJruk5WbHR2ehcn3oxszRAQ6p3Uij_MFMgGSBDILUMti3Gft0GToyuKTpkE2rkQ4aF5r6XIdm4WLqiDa-H6s4qroM4hGM9FmNYTPiGrQDnB0sw9J3BxEtkYZR_Cq4uBkz9xTmCuVEqQaGXVIzSnfnZQy1jdVvscPjulrBgLqaeihKOzG45PP8-05vvZLqE7ncLofmVid8HX3zkL1fZkQlpml1QjO4Yyvzc3BWMVJq2wKkZ-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8bf2cd6a1.mp4?token=dh3cRCFuFr95jdpwlF5Uir4QBNyhqs4Hm9CnP0t4xYdXkxa9vi5XtDT5ABeIjAVbfm7zFTe6djcncigiPr5bA18UBbMvlX9upVBVDPcJruk5WbHR2ehcn3oxszRAQ6p3Uij_MFMgGSBDILUMti3Gft0GToyuKTpkE2rkQ4aF5r6XIdm4WLqiDa-H6s4qroM4hGM9FmNYTPiGrQDnB0sw9J3BxEtkYZR_Cq4uBkz9xTmCuVEqQaGXVIzSnfnZQy1jdVvscPjulrBgLqaeihKOzG45PP8-05vvZLqE7ncLofmVid8HX3zkL1fZkQlpml1QjO4Yyvzc3BWMVJq2wKkZ-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز ظهر تو خیابون ولیعصر تهران،یه اتوبوس تندرو بی‌آر‌تی بدون راننده و مسافر به دلایل نامعلومی شروع به حرکت میکنه!
این اتوبوس میوفته تو مسیر سرپایینی و با ۶ موتور سیکلت و ۲ ماشین سواری برخورد میکنه که نهایتا ۶ نفر مصدوم میشن!
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68275" target="_blank">📅 21:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68274">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7sUJCYrClXVFTN5SN4CBm22l1d-fo5j4w9Kg0a5ZKWfjLBll1rkn9t2AI8DGEc1JMYVH_J-OXRDuJNtb_W1GX8XdNewoS29HvCRvyD7jM3pTv1W6npdaN1d7drRUZi6cLKjU8i3gIZbR-snIGi_X0ho_qJ7MeG7HfQyHdtHv8-8XL1-XeMyiaA-axIzOGCLTqpSzL0lwZ2UmiNZvP80CkXxiwp24Lv_BBRCz8YFcFMZZcuDqWUJToP3Mm4I2WRnAs8-l0tkSI4GW4HwcDT6M6f3mDgR0CjgknS_utwyH1WlEVqhPX7_FpKAE1fRp0Mffo9QzYsY1kBAAuA-z7b8dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کپی ترید خودکار
— فارکس و کریپتو
⚡
اجرای آنی
— بدون تاخیر، بدون دردسر
💎
رفرال
— با دعوت دوستان درآمد جداگانه داری
💻
پشتیبانی ۲۴/۷
— همیشه در دسترس
🎞
آموزش شارژ حساب</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/68274" target="_blank">📅 21:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68273">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqYynIvHXPBvHeJPWrC7REXtSmISFsIypWMW3J_B5O084VxtOo6RsPWdsw15yzHDGF_HcdUcjXdFmXDC6gY9qP2DMhK_2tZMy4BtGbHfsZIc3CEkzrKo3em1SvR7D8uwnm9DjLKHldoz-UejyYTsvvErVMn5hGaOrgNZS4y48t16r837jPAuqlSeuwOMaZars6wjFNxcBBqJUpWzqxOY4RMHM2EH1PkpbKrQ-AhRDaHf19-pl9afivccRZ1C2v0kqev3nqJFs5_OJde0W4-1kVj8WkxnfuxFRJ6xclEjDRm9axzGhhxaGa_7KJCAi_Ay7Q55t7SFcf2x8uHwIW1cfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏شاهزاده رضا پهلوی:
در حالی که جنگ‌افروزان جمهوری اسلامی در تهران و پناهگاه‌های امن خود پنهان شده‌اند، سربازان وظیفه و نیروهای جوان را در پادگان‌هایی بی‌دفاع رها کرده‌اند، بی‌آنکه حتی توان حفاظت از این نیروها را داشته باشند. این رژیم بار دیگر نشان داده است که میان جان فرزندان ایران و بقای خود، همواره بقای خود را انتخاب می‌کند.
جمهوری اسلامی این جنگ را بر ملت ایران تحمیل کرده است و مسئولیت جان همه قربانیان آن، از جمله‌ سربازان در پادگان بمپور، بر عهده همین حکومت است. آرزوی همه ما، صلح، امنیت و آرامش برای تمامی ایرانیان است، اما تا زمانی که این رژیم بر سر کار باشد، نه امنیتی پایدار ممکن است و نه صلحی واقعی.
این رژیم تبهکار بیش از آنکه دل‌نگران امنیت مردم ایران باشد، نگران حفظ حزب‌الله لبنان و دیگر نیروهای نیابتی خود در منطقه است. برای این رژیم، بقای بازوهای تروریستی‌اش از امنیت و جان مردم اهواز، زاهدان، بندرعباس، بوشهر، چابهار و سراسر ایران مهم‌تر است.
خطاب من به سربازان، افسران و همه نیروهای میهن‌دوست است. جان خود را برای بقای جمهوری اسلامی به خطر نیندازید. سوگند شما به ایران است، نه به رژیمی که در لحظه خطر، سرکردگانش می‌گریزند و شما را بی‌پناه رها می‌کنند.
من با خانواده‌های داغدار سربازان وظیفه که در حملات اخیر به مراکز نظامی جمهوری اسلامی جان باختند، عمیقأ هم‌دردی می‌‌کنم، و از خانواده‌های همه سربازان وظیفه می‌خواهم تا آنجا که در توان دارند، اجازه ندهند فرزندانشان در این شرایط خطرناک به خدمت سربازی اعزام شوند. هیچ پدر و مادری نباید فرزند خود را به پادگان‌هایی بفرستد که امروز به جای محل خدمت، به میدان مرگ تبدیل شده‌اند.
این جوانان، فرزندان این سرزمین هستند، نه سپر انسانی جمهوری اسلامی. آنها نباید بهای بقای حکومتی درمانده را با جان خود بپردازند.
هم‌چنین از مردم شریف ایرانشهر و زاهدان که برای اهدای خون و یاری رساندن به سربازان مجروح پادگان بمپور شتافتند، صمیمانه سپاسگزارم. این همبستگی ملی یادآور این حقیقت است که مردم ایران، حتی در سخت‌ترین روزها، فرزندان خود را تنها نمی‌گذارند.
ایران به فرزندانش زنده نیاز دارد، برای ساختن آینده‌ای آزاد، آباد و سربلند
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68273" target="_blank">📅 20:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68272">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
فارس:
حوالی ساعت های ۱۹ و ۱۹:۲۰ نقاطی در  بندر عباس مورد اصابت پرتابه‌های دشمن قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68272" target="_blank">📅 20:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68270">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7ad056e14.mp4?token=u2VDZZCSwdqgKvLERmVSQgmv23nO2LFiokYVqeHVRYXoM2-osWmxz0hh5aEftQQG0EUjZIntO8wSTU4ecA9IUwTKiZF8t6uPriK5rz4UKrJZ7kKJN1efx_paZI7ovoh7iuvkpTK1h9ckKVUgKvle8djZecuFYO9gNdf8YLBF24y4oevb9cLb_Gb1iAkfXOvcYywLbX1w6ri3ClAI0Yqqj97_cR24nf8yvxdSMXfdqyP9TsY68QizNZrbsI5sY90wb76TcNH8C-_QkHbpLtvulYp-RyF5oz8KVmKF0blg_zsddlnQi8IWYaeUxfg1DQ_QoTf5EMTj3npodfDv_-CL6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7ad056e14.mp4?token=u2VDZZCSwdqgKvLERmVSQgmv23nO2LFiokYVqeHVRYXoM2-osWmxz0hh5aEftQQG0EUjZIntO8wSTU4ecA9IUwTKiZF8t6uPriK5rz4UKrJZ7kKJN1efx_paZI7ovoh7iuvkpTK1h9ckKVUgKvle8djZecuFYO9gNdf8YLBF24y4oevb9cLb_Gb1iAkfXOvcYywLbX1w6ri3ClAI0Yqqj97_cR24nf8yvxdSMXfdqyP9TsY68QizNZrbsI5sY90wb76TcNH8C-_QkHbpLtvulYp-RyF5oz8KVmKF0blg_zsddlnQi8IWYaeUxfg1DQ_QoTf5EMTj3npodfDv_-CL6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در بهبهان استان خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68270" target="_blank">📅 19:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68269">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ebc1ab26.mp4?token=T1UHaDs7kfZEKcxD-D8czHeAIfOimCCDMtmfmWdV6NVKkTIZkS7i4mTNELJLLsYs9FhTiPhxTecN-pmcEXmJl39zF-tIB_eVmONORZqaiZQB6ZVHceiN8ssq_jU41q1wDngZSWPm_4LU-pDQMA9_tk6upNF5KH0HSubCV9akNdybhQmS2MeqkXGQAmIQtNbgVgbrmzMonznWzwxZSXM6pH29o6wE44cjsmCvolskGjYfXz59Hyp9NoUaUYz7eM3P18pfIDAmz1166nEPDxgO5agRJzd0XkZCrWolCg4GqaqBsOQVm9tIT-6fgjXsWqRb8fB5QOekEOpwgxlWH5W1lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ebc1ab26.mp4?token=T1UHaDs7kfZEKcxD-D8czHeAIfOimCCDMtmfmWdV6NVKkTIZkS7i4mTNELJLLsYs9FhTiPhxTecN-pmcEXmJl39zF-tIB_eVmONORZqaiZQB6ZVHceiN8ssq_jU41q1wDngZSWPm_4LU-pDQMA9_tk6upNF5KH0HSubCV9akNdybhQmS2MeqkXGQAmIQtNbgVgbrmzMonznWzwxZSXM6pH29o6wE44cjsmCvolskGjYfXz59Hyp9NoUaUYz7eM3P18pfIDAmz1166nEPDxgO5agRJzd0XkZCrWolCg4GqaqBsOQVm9tIT-6fgjXsWqRb8fB5QOekEOpwgxlWH5W1lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محسن رضایی: مسیری که در ذهن آقامجتبی هست، بهتر از مسیری بود که شورای عالی امنیت‌ ملی رفت.
مجری: چه مسیری بود؟
محسن رضایی: نمی‌دونم، نمیتونم ذهن خونی کنم
😆
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68269" target="_blank">📅 19:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68268">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNqMQ-QVbFstwVC6eY4KCifdTodrSO45KAd7XecQXfGo-lK15cjkN-SrZoXYVeSA0901GPYdhUfYpuT1XxlMDEwCj_hxopfFhF2PjKhgtWs6LtBjOu3W528NwruX2T9Ah6swxgtpg12riTvQ8ICTQL3J9mOWmQPRhV-KR6OmtnVx7OhgA3aJmgpgI10a01CZSlbVGtEZaUEdmm8BQlSW08JMhKgJStV4Dc06v_XwHCTcCyg4Yk0RJxqzC5JLjb6jLE3o_ktT0rE-PndwcLd6a5VPwVXC8m0-ef3fdHvI15Iti6uNP59NdbHdrayBoSIQMOag-TASW1Yhat4fPpPb7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سازگار با تمام اپراتور‌ها
✅
لینک ساب اختصاصی
✅
مناسب برای گیم
💵
20 گیگ — 120 تومان
💵
30 گیگ — 150 تومان
💵
نامحدود — 200 تومان
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn
چنل رضایت مشتری‌ها
⬇️
@kavianivpn</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68268" target="_blank">📅 19:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68267">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcZe8nEGXgutGLMkcaT0szDZyqodMbGdQktvO-c9nZLqjRpc66gGRxuijVVn2YEtTMtWD1jcU2Imh-tsUg7R2KqLI7qpJnASeJjXYbV0ubs35-MPmXUvI4HFLbXXRv4ZSyuM8683WsCakEVlH68Li_59Tx3oC-ubFXznUBsxg3zI4RWKQuNy3qF1GadWFsO1R7Mu5YSXqMvRyuykmz9zTZLyuS-UeX1J1ywEvcljpr-pWHsvBL5PjXi52QbQBliGeI9R5aI9hYhdvX_cp9q_n5DKGh_CTH-Ed4SCARd2f4BtTC4YvxAto5m8-Qgb8yqoQ6Da01gQrKCkE36yYtSGPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی به آرایش ناوگان آمریکا در محاصره دریایی ایران؛ هر چهار ناو لینکلن، بوش، باکسر و تریپولی در منطقه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68267" target="_blank">📅 19:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68266">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06389032d8.mp4?token=t8h6uSWXH19mDWN2TH3NclU2ifPsIQJlOYLs5kV018mJcS4PWNxS0CsDA7MhgHGY08_bbMRlldMlEVQsQozDvVNjC6GmKx1bJDAXF4Bp9ur73VbdlMdjuzKr9goxHT9YST0C3D9HjSpTyiYNpOJHfX72eqA860OWrlmApfmqHarReYxKEzfyf02wCkqtly4xI0KpGnD_vXSx4ZX7m3W4v4m4azyWocrKt8gP2HlyBHVAwA_rJs2UynNXKWal51vooJgK022jDV6xKARwqgSzdmkUIXCssv8B33My4aIPYIpziXqC4gA34mtQ6A677qElV0TCni5zH4eL6Acphb5uow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06389032d8.mp4?token=t8h6uSWXH19mDWN2TH3NclU2ifPsIQJlOYLs5kV018mJcS4PWNxS0CsDA7MhgHGY08_bbMRlldMlEVQsQozDvVNjC6GmKx1bJDAXF4Bp9ur73VbdlMdjuzKr9goxHT9YST0C3D9HjSpTyiYNpOJHfX72eqA860OWrlmApfmqHarReYxKEzfyf02wCkqtly4xI0KpGnD_vXSx4ZX7m3W4v4m4azyWocrKt8gP2HlyBHVAwA_rJs2UynNXKWal51vooJgK022jDV6xKARwqgSzdmkUIXCssv8B33My4aIPYIpziXqC4gA34mtQ6A677qElV0TCni5zH4eL6Acphb5uow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جی‌دی ونس، درباره ایران:
اگر مردم ایران بخواهند قیام کنند و حکومتشان را تغییر دهند، این تصمیم با خودشان است.
اما ما قرار نیست ۱۵۰ هزار نیروی زمینی برای تغییر رژیم اعزام کنیم، مگر اینکه خودِ مردمِ حاضر در میدان بخواهند به چنین نتیجه‌ای برسند.
البته ما در هر صورت قصد اعزام نیرو نداریم، اما پیشنهادِ اعزام نیرو عملاً به این معناست که ارتش آمریکا باید این کار را برای مردم ایران انجام دهد.
ما دیگر دنبال چنین کارهایی نیستیم؛ واقعاً نیستیم
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68266" target="_blank">📅 18:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68265">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HooYaO6udVM7yPi3TCozJIDLFcS_TVW4PSDQXVWBXvhn4iZI-gc4rmDbarey3hVE2kFuarr3aTmlLZ__Z2SBoQeQigLYe_F8GrODNxUxMLsYd5NwLFf6QgKwviW95pgYqxHEFJjX5z0TflTkjw3o0RK5VKuK0CXlrv3i-87ve86Bq8byA9LnXDR36CywP7fbg5AViHO5S6RuNR-wEDAjdbrk__jAhH1Ti4hIQtV6y9NX7cYPx088D4MmQz0WjC9bOUpjJ0YxW754dtizld6UH8c0KRPMa85Bo6QKbCRkiIuQrSmQQab7fpqU3ckPB0fVDVOFLqm1dLOPVcCy330-rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
لاشه پهپاد انتحاری آمریکایی FLM-136 LUCAS در نزدیکی بندرعباس
پهپاد LUCAS در واقع همتای آمریکایی پهپاد ایرانی «شاهد-۱۳۶» و یک پهپاد تهاجمی یک‌طرفه (انتحاری) و کم‌هزینه است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68265" target="_blank">📅 17:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68263">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55dfc7018b.mp4?token=KQ7TvaIWmRMfNF7uIgMIimRbEojUb8jiOkq2qrxmwLDxzrfC0U2b773-IAT3TEwmWH8ReNtnrovFGT_hDWzgGqPf0uf08L_CRxvw95oVZsfpN6rZMoLUDqtOihJEDgybwxIr0sbe0o8vBhK50UH08B9ALS6sgds4yAALAYUbcKh_gek_FHoZ98g8murk2a5PxPau5dnIhN9oQXQpTkn6YzWZG8Lxxi1WLTMyYFSQ5VkdanurHnr_CzW_ndf-urYXBucIvIGCbqlQkErL4JvMqschtoZY7r6gj5yxSuXDDhr3TscT3ZcN4EJzInQO2YMboDaxHbqLYIZwhFwNv2LO4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55dfc7018b.mp4?token=KQ7TvaIWmRMfNF7uIgMIimRbEojUb8jiOkq2qrxmwLDxzrfC0U2b773-IAT3TEwmWH8ReNtnrovFGT_hDWzgGqPf0uf08L_CRxvw95oVZsfpN6rZMoLUDqtOihJEDgybwxIr0sbe0o8vBhK50UH08B9ALS6sgds4yAALAYUbcKh_gek_FHoZ98g8murk2a5PxPau5dnIhN9oQXQpTkn6YzWZG8Lxxi1WLTMyYFSQ5VkdanurHnr_CzW_ndf-urYXBucIvIGCbqlQkErL4JvMqschtoZY7r6gj5yxSuXDDhr3TscT3ZcN4EJzInQO2YMboDaxHbqLYIZwhFwNv2LO4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عموپورنگ هم اینطوری بصورت دردناک برای مادرش گریه کرد:
من دیگه مامان ندارم...
دیگه در باز کنم کی بگه چی اوردی برام؟
💔
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68263" target="_blank">📅 17:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68262">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c15a1c1db.mp4?token=AaffIKpZ0ObChN9PBSewfUAZXwR4BbogNiUI7X_By2LkA5RdDyG7vvNJ0UYidKl5-W2pCH7xwVSVL0moTtETUViww3j1dB5_OhNGz7pWM2PEENk42hSWPYdmu6l_JubfWA5KrqxzHFLj0espMqcRUdv6zTpvfnxX2BJHC3UUoL1GmpDAnDH4Iod-Acf89WtIZSlBAqNoStDmue_Q7FNy9mLXb-yVX9iVeSi8ehOIrb4M0skG2DcSsdS_TDXbphUeewnaLpIDfQ9o1BpKdR3fSZFESfXNhDHhzrCYx7uvtPbezkYJak4K05px38nFv7FGZGKOjMLdZfSpKSQ3a4tXsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c15a1c1db.mp4?token=AaffIKpZ0ObChN9PBSewfUAZXwR4BbogNiUI7X_By2LkA5RdDyG7vvNJ0UYidKl5-W2pCH7xwVSVL0moTtETUViww3j1dB5_OhNGz7pWM2PEENk42hSWPYdmu6l_JubfWA5KrqxzHFLj0espMqcRUdv6zTpvfnxX2BJHC3UUoL1GmpDAnDH4Iod-Acf89WtIZSlBAqNoStDmue_Q7FNy9mLXb-yVX9iVeSi8ehOIrb4M0skG2DcSsdS_TDXbphUeewnaLpIDfQ9o1BpKdR3fSZFESfXNhDHhzrCYx7uvtPbezkYJak4K05px38nFv7FGZGKOjMLdZfSpKSQ3a4tXsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنت‌کام:
هواپیماهای جنگنده F-35A متعلق به نیروی هوایی ایالات متحده در حال سوخت‌گیری توسط هواپیمای تانکر KC-135 هستند، در حالی که در حال انجام گشت‌های هوایی بر فراز خاورمیانه می‌باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68262" target="_blank">📅 16:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68261">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsKOZ75NVwA2b7_gBQARJbj9-9e-5GBoLl5gLg0eZZ3AvyPj1rE_jNlMIkdLj06Vpc4YKAHaL7Bh0lhdQZawhfHSgoNidjfXB43_poMWCdH4N92ZIOIHo-lEV4T5_ADTMzoEyIrChgxznFM9cbgFvl1tXRiREIEE7-jT8tqTXj_kGw5daLyuwDZSUNC_A-TG6LIp4BJxlCO3seOcL2dF6XdpcF7PJrNTMiXdyr4xpKCFAXj0keldRkLwbcZP-l0T2vttXsLlWnBinY8XFQSEzuqyj0a59VdMZOo4x8HYERKdyxNjDkvZLvNB0F68DQWgXRMV5grQAJ6BZ3UkuCW_yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو سال ۱۲۸۷، محمدعلی شاه قاجار مجلس رو بخاطر مخالفتش با ایدئولوژیِ مشروطیت با کمکِ روس‌های حرومی، به توپ بست، و بعد از اون
دوره‌ی دیکتاتوری و استبداد سنگینی
تو ایران شکل گرفت و
آزادی‌خواهان کشته می‌شدند
یک‌سال بعد با اینکه ستارخان تو محاصره شدید بود ولی جبهه هایی شکل گرفت و شمالی‌ها از گیلان و بختیاری‌ها از جنوب به سمت تهران لشکر کشی کردند، و بعد از به‌هم پیوستنشون، سه روز درگیری خیابونی شکل گرفت و در نهایت، روز ۲۵ تیر ۱۲۸۸ محمدعلی شاه به سفارت روسیه فرار کرد و تهران فتح شد
خلاصه که مردم حتی بعد از
یک سرکوب و کشتار سنگین
باز هم ناامید نشدند
و پس از اتحاد اقوام ایرانی
، در
نهایت به خواسته‌شون رسیدند
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68261" target="_blank">📅 16:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68260">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دیشب تو اوج حملات، ترامپ از جمهوری اسلامی بابت آزادکردن یک شهروند آمریکایی که تو سال ۲۰۲۴ بازداشت شده بود، تشکر کرد
خلاصه اگه امشب حمله‌ای نشد یا شدت حملات کم بود دلیلش رو بدونید
#hjAly‌</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68260" target="_blank">📅 16:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68259">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4MOYdnOyKuwKKTg7PQz0OUx5oSqa88CrVtmdpr-94QPMsQ1H3B3KUoMFu5FWit_2R9r3-aarY_4_eBDIemReuEP5vStCNu56xor9jWeQkluNvwDnEiVdEo6daclYJs2r07IsSNR7wr26nLFVmIz2IZ2jy3-CaYSGQeL5iiIrjn-1zqAXiORJFx46KLTr-Y-12OGpwlTUZhPwx9e6LSuFnt1IUc5ezopoOZAuGEqjMBQhjABn9Ofuwnt7qz04aVZGFTjTul6U8N8yvXtjVf6nBkFxFfK8WwPDYdCGEYHJzn_zlGTx3ixipGZlTGOpR2_7xzQ0dXUUvnRjbdbS9l-pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوارنگاره جدید میدان ولیعصر تهران که نوشته «who is D nexT one»و هشتگ لیندسی گراهام هم زیرش قرار داره.
همچنین ‌حروفDT- اول نام دونالد ترامپ رو برجسته نوشتن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68259" target="_blank">📅 15:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68258">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">💢
مرد پاکستانی ، عاشق محمدرضاشاه
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68258" target="_blank">📅 15:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68257">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EerpoTFf9Dw0hHDZWmQDgKosPyGRUdNOgI7Bl-RyDXXyLEBH_nQgY56Clb96mVCSZkVcPzMi7Zz9aoVdxysYyxO6SJtGKvNYyrB1Eh4d5bevj9JM_m7rg4Vz6ukcu_cnizNUXdyZA7A0qP0M3vjlkDzk-D4Hpqdw0OI2ZWdYz110iXzcF1J1FYtx_iPF3Dq5IDaUZuBAo-DFsvAsvhcihOS0Gi5nDuuSL6mNFo3U4tQF3GjzNTXlAZxx4luzaQAyhrltmUDzIcL666KVt6c7nesUAk6sguSYltDoRiu5lUpwsFhY2Zr-UvUysLq1zrt06agLx_XleePgXCftSxC1ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نتانیاهو سفر برنامه‌ریزی‌شده خود به ایالات متحده را به تعویق انداخت؛ این تصمیم پس از آن اتخاذ شد که مراسم خاکسپاری سناتور سابق، لیندزی گراهام، به زمانی دیگر در اواخر ماه جاری موکول گردید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68257" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68256">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b50f05a056.mp4?token=sUuAm80UfswKtKF0FwiLdOm7vLDb6BpitC1wImrB4auAppyR8lXA_cmuazb7ycEiNi4EwBAKVHnyky94FiwwnlILUAGIPcDXF0Ckexk6fvCE1Rme3BSoMHM3P-lCMgkAM9IhYkC8H1DarVHOdmmlrPbmULsctkVWLZqt3gjrEKNDgFDzsK9ttjkSBR3cPMUJuJp6OPAcZ_EM65qOQXabeKaU132gfcEfY3-DY5JR36WpfhBig0cbc2ucCDtts4u1_pytKlrSXSEYW-6bBhIeytojsz9BJmrAfz4G4sKUkA_MST3fazslkpMvQ3DhVygxcnSzeXVZrH4jgT2RAP3gdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b50f05a056.mp4?token=sUuAm80UfswKtKF0FwiLdOm7vLDb6BpitC1wImrB4auAppyR8lXA_cmuazb7ycEiNi4EwBAKVHnyky94FiwwnlILUAGIPcDXF0Ckexk6fvCE1Rme3BSoMHM3P-lCMgkAM9IhYkC8H1DarVHOdmmlrPbmULsctkVWLZqt3gjrEKNDgFDzsK9ttjkSBR3cPMUJuJp6OPAcZ_EM65qOQXabeKaU132gfcEfY3-DY5JR36WpfhBig0cbc2ucCDtts4u1_pytKlrSXSEYW-6bBhIeytojsz9BJmrAfz4G4sKUkA_MST3fazslkpMvQ3DhVygxcnSzeXVZrH4jgT2RAP3gdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش مجری‌ها وقتی یارو میگه تشییع خامنه‌ای ۴۰ میلیون نفر حضور داشتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68256" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68255">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaBunhvDGpnA3cMSaSf82OKmePMZLbJfbF1mE9ZTt0H7FgbpQOeaCdyGuR-5Zy22k2ovfq6mfBLhP_9hRL_zKhJdsfbwkgHJ04PyJw55QAjMFPW9KEvD045yZrkt1qKWVwppX97SZF_ViSK2k9qBIdE5t8hVRaAXOwx8F6DGMI34nKvufK5iUmWxqTfcoW4NZFBqiqj2adrF8Ld-gicKuJzoPwfcyHILe4cwfVqXWQWKdcYhthvoLvF0WyhJr4xqoZdUlyH_JosOOq8tBiGyaoHclVVl2Y9IoRM_Zz5gjaxc4tOC64YHkYjXiuvO7H2_0qoEI7Db7lgxyEUTcNfocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فینال جام جهانی 28 تیر (یکشنبه) ساعت ده و نیم شبه؛
- یازدهمی‌ها فرداش عربی نهایی دارن
- دوازدهمی‌ها هم دو روز بعدش عربی نهایی دارن
بهترین راه اینه که فینال رو با گزارش عربی نگاه کنید
دیگه عذاب وجدان نمی‌گیرید
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68255" target="_blank">📅 13:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68254">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfEWMpTJNCG-coO0y0j4liKnGqzBY1FZrc4KTekudK9VnfNrrD6FbCmR6g9bS_BL-ov4DlgX9NUjxIAH0MsUdUNwPqZKM6Hi6aOHKcVtcMG9Ie6dxl9IQTLHfkNe2RUnTthZ07BRcCkUvqo-UvTH_ga3REw_9hqoiGyFpItePQ4OxF5Rst9e2HSfd688QnNi-kcpqOaBBN5VsOZO7LzkIRu1GReIfAb6r5IojdJKF5pSHdQQWQvwjpr4OX1fLOfp-fvjfw1Td4BrwWarQec8twSYBFablTaIurkWk2de7mYyYV91_ZL5o8hljbtkLpivbyzF2MwyIkAa8I92xOV5QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تسنیم:  کارگاه قیرسازی حرم آتیش گرفته!  @News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68254" target="_blank">📅 13:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68253">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34bb460b32.mp4?token=PBFPA7mnmp7Fwo0-5CpyYUphaE4B2tGoRGpy-98pjUWsSckXrLSqcGvmYnSD_NEsOrdBABBxS9TyTTDQLYyhElfAOB3R2gHZAL2Q-QAt0yvJoSPDkAnTafsyTDcmuY17sr7wM1mEhYTqqfGsV0O3G-Kwv6y502ML-dHwhlTd5dRlZ1p1MraqBEORe87IeYwyPmdY8XyOnc_z666cy9llxi5YFRJKDQBt05Zt51u7ASrTbVCJ7F0q_R7N_3_Rt5RKVd-dz1eS7of2pVq2lM0WjkU0rYc3K0VaalgQCk_Kpg0HQlBYc1okW1mbyWEMrAX3I0tFQv6Kx3Cbz-Gv6JlXtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34bb460b32.mp4?token=PBFPA7mnmp7Fwo0-5CpyYUphaE4B2tGoRGpy-98pjUWsSckXrLSqcGvmYnSD_NEsOrdBABBxS9TyTTDQLYyhElfAOB3R2gHZAL2Q-QAt0yvJoSPDkAnTafsyTDcmuY17sr7wM1mEhYTqqfGsV0O3G-Kwv6y502ML-dHwhlTd5dRlZ1p1MraqBEORe87IeYwyPmdY8XyOnc_z666cy9llxi5YFRJKDQBt05Zt51u7ASrTbVCJ7F0q_R7N_3_Rt5RKVd-dz1eS7of2pVq2lM0WjkU0rYc3K0VaalgQCk_Kpg0HQlBYc1okW1mbyWEMrAX3I0tFQv6Kx3Cbz-Gv6JlXtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تسنیم:
کارگاه قیرسازی حرم آتیش گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68253" target="_blank">📅 12:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68252">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RE3oHyrR-HDs0abTxIHGAgcQgH1Md3QABNWDHpTBfVJ2wrgPmkkmi-pU08xYCftIKisFIDT4C-8vfljnRsI53LRmSut-7xrTYEdj3NIqFEpF1Oucw4G6-UmplNqGebswbVjJvwWrBngbm-EqhPz8L-nryX_bSTUIOFFswGNJ0-MI8LkfE_R8v1vF6ZmJe_x9TsY_bMIYWoZVK6MN5-75yx3e02QcSUc8T1ZrcHlqJQ3qQTK1KZTEDudYU0j4PH71fl51pFxN2bheNcMWHsqfHnXhjOmFiYHCorjW0sqDhwngvD2T8Ep3fCgYih-G69YYXZ96BpH1c3c4UYbQbD32CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتش‌سوزی در حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68252" target="_blank">📅 12:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68251">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/314324694e.mp4?token=uSsZINuL8Ido1HkkPbMdfuLONUgGIE6K_vIKGfycxDayg3UBARCMD-GN13Xo0Pv67JHov1rdgbWa6PTbOTKsBI5W6S_SxfxLJBwXAHiHnT9thIzZam31F0yRcNdpBDOEUSpnScrIJAoPEpsJW55A9cUspmZArZjlco2WN0T4N_PHGKfQbmYB4f14QiDBdNjSfAGsZSy7RX6XH1VbkIBhGYeWj4R4D7NxDdBP-2Jzqjv4FKDp_Isi8vLElNMzNATbd4lcIne1C-cYaT__VyxPFhd3ArLLc_iRPhDuJHWoBkVtKm8btW3fzB5y1pK7jpNryq3d1k5wUYiha8-E_N-iSYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/314324694e.mp4?token=uSsZINuL8Ido1HkkPbMdfuLONUgGIE6K_vIKGfycxDayg3UBARCMD-GN13Xo0Pv67JHov1rdgbWa6PTbOTKsBI5W6S_SxfxLJBwXAHiHnT9thIzZam31F0yRcNdpBDOEUSpnScrIJAoPEpsJW55A9cUspmZArZjlco2WN0T4N_PHGKfQbmYB4f14QiDBdNjSfAGsZSy7RX6XH1VbkIBhGYeWj4R4D7NxDdBP-2Jzqjv4FKDp_Isi8vLElNMzNATbd4lcIne1C-cYaT__VyxPFhd3ArLLc_iRPhDuJHWoBkVtKm8btW3fzB5y1pK7jpNryq3d1k5wUYiha8-E_N-iSYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام تصاویری از حملات به ایران منتشر کرده است.
این تصاویر شامل برخاستن جنگنده‌های «اف/ای-۱۸ئی سوپر هورنت» نیروی دریایی ایالات متحده از ناو هواپیمابر کلاس نیمیتز «یو‌اس‌اس آبراهام لینکلن» و شلیک موشک‌های کروز «بی‌جی‌ام-۱۰۹ تاماهاوک» از ناوشکن‌های موشک‌انداز کلاس «آرلی برک» است.
اهداف مورد حمله شامل پرتابگرهای متحرک موشک (TEL)، سایت‌های پرتاب پهپاد، هواپیماهایی که پیش‌تر قطعاتشان جدا و از رده خارج شده بودند، و یک دکل مخابراتی بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68251" target="_blank">📅 12:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68250">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e23gwNSq4-kNzjRJcVuc-Iffug9m1Rr3FvK6tPENu8yfXUZkweMGxNGqMnFvv8uTxZCGyjtZ2CMUJV4iwbNmK6IopSyzmJ9CCTQKxU6AMcrnE28_bFmHk3FYOZDnxLD_vMxP1JicMVJ_L0EbIpLSQWeC2AvNg-ye3CyzuOHROcSBP4dTHXzD3H9gyUc86iLaq651NzVby2MOe7isMZfAGxYPQvqkJxARFMxz9bIQ-RqPqbckAWTtHW7YGKLkVHlMV1JrgpGd0rMg7BiTGrf4o4GpwYFA4iHPtglAke2SBP_TeRYq1fVyawGZdGdCCZOmAzOz11ggj_VIkHSJd0AQeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ترامپ:
ایران اجازه داده یک شهروند آمریکایی که در دسامبر ۲۰۲۴ و در دوران ریاست‌جمهوری جو بایدن بازداشت شده بود، از کشور خارج شود.
این زن اکنون در سلامت کامل و شرایطی مناسب خارج از ایران قرار دارد. آمریکا از این اقدام مبتنی بر حسن نیت ایران قدردانی می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68250" target="_blank">📅 11:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68249">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bc13721f.mp4?token=mcqaz4GPPXIfW2t7VA3ItPfVwLrj3tLoMAoRf0LCRbwSpLkYu5kJyB57grV2R-JXjphMtS-5to-2LuFU118eZNFI-g4Ux0c5L-00GbupvFwPiGBI0bk2-KBFG5X2Y0fdQ26yyEHzTPNRaToxivcLsvsVbzEa0ARl8vz1_joGc0Sf2YkomjUDSh9yKjMjnfUbWL_w8WaTDmkY68jdCyAhi8j3xWxlOgfOkGtcC29bZ0I85_cX1pDggyy7Mv51XQBix-Aw1IDoVhNKCqpZ5YZjyscPJvMIE-ujvNrPSthbx8ZEDMeySJXGSWFzBw4ORGGSGkgjIkQmspowjUsKylccxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bc13721f.mp4?token=mcqaz4GPPXIfW2t7VA3ItPfVwLrj3tLoMAoRf0LCRbwSpLkYu5kJyB57grV2R-JXjphMtS-5to-2LuFU118eZNFI-g4Ux0c5L-00GbupvFwPiGBI0bk2-KBFG5X2Y0fdQ26yyEHzTPNRaToxivcLsvsVbzEa0ARl8vz1_joGc0Sf2YkomjUDSh9yKjMjnfUbWL_w8WaTDmkY68jdCyAhi8j3xWxlOgfOkGtcC29bZ0I85_cX1pDggyy7Mv51XQBix-Aw1IDoVhNKCqpZ5YZjyscPJvMIE-ujvNrPSthbx8ZEDMeySJXGSWFzBw4ORGGSGkgjIkQmspowjUsKylccxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پهباد شاهد در حال رفتن به سمت پایگاه های آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68249" target="_blank">📅 11:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68248">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b8221101a.mp4?token=KhZo0yPoMkhOG_Ho8mdM0d6iQJETmJwVTjKYq7FGF5u3pq4Yp6Pz7FhKrvR6NyK2tcepNWmkcSviW3vYHqB9zqAP6QaAhAzVx7k-JWVCN2wKE_8PDCfxFMwKFquwWEynRRz4-cLUzLUk2Cms9AcJ9Umsc-ox0OHjEeJmVGC1XY2wKVPImUhY7sGAQSuE7hz4u2ssBYHr2FDhifLmknuJeAGZXsBJoCxpSNB4xFz3e1QLmbP_7YSnHElb8ijy9DC0SEQuPSETOziImIaRhOP6TbmIe1X_qUHX23vCXOEfwr_sDka0htY3RlqSB7MZfu_B9e53_8weSekap2KmuUXDTrK4zQvVB7XPryc41kNA-lb479KxVyC9zI0wuZvQE9T7v9AkJo-VAer1dFAFoL5usXSXRl35uAOjG1rlRj4G6yMjJr85fM4PRtL7W8XWJCgokWpOic4csN3wkS3EfpGKjsW2xvbqxCFkCtz284ujaRHXQMG5JZDRfeok_KS4yBNFddRY5_iCmSxPEroabVBKw6YEDpiJgqvetHs7wRHPc77R5PODb4P8bNOOPgMAse16eeLhgCHO6K7xR3dfGD4tvJ1Z2qzEl5g9AfNt4Fjypj5pneL4bApFfw_84Hd4wFkw_oNQ9x-WAUXKz4n0Ebe3PciEjijYL7gAAyyv-p2eIEY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b8221101a.mp4?token=KhZo0yPoMkhOG_Ho8mdM0d6iQJETmJwVTjKYq7FGF5u3pq4Yp6Pz7FhKrvR6NyK2tcepNWmkcSviW3vYHqB9zqAP6QaAhAzVx7k-JWVCN2wKE_8PDCfxFMwKFquwWEynRRz4-cLUzLUk2Cms9AcJ9Umsc-ox0OHjEeJmVGC1XY2wKVPImUhY7sGAQSuE7hz4u2ssBYHr2FDhifLmknuJeAGZXsBJoCxpSNB4xFz3e1QLmbP_7YSnHElb8ijy9DC0SEQuPSETOziImIaRhOP6TbmIe1X_qUHX23vCXOEfwr_sDka0htY3RlqSB7MZfu_B9e53_8weSekap2KmuUXDTrK4zQvVB7XPryc41kNA-lb479KxVyC9zI0wuZvQE9T7v9AkJo-VAer1dFAFoL5usXSXRl35uAOjG1rlRj4G6yMjJr85fM4PRtL7W8XWJCgokWpOic4csN3wkS3EfpGKjsW2xvbqxCFkCtz284ujaRHXQMG5JZDRfeok_KS4yBNFddRY5_iCmSxPEroabVBKw6YEDpiJgqvetHs7wRHPc77R5PODb4P8bNOOPgMAse16eeLhgCHO6K7xR3dfGD4tvJ1Z2qzEl5g9AfNt4Fjypj5pneL4bApFfw_84Hd4wFkw_oNQ9x-WAUXKz4n0Ebe3PciEjijYL7gAAyyv-p2eIEY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو وایرال شده از یک جوون طرفدار حکومت:
من الان شرایط ازدواج ندارم چون نه خونه دارم نه ماشین
بدیهی ترین چیز برای ازدواج اینه حداقل ماشین و خونه داشته باشی اما خب من ندارم و پدرمم پول نداره که بخره
دلیل وضعیت الان بخوام کوتاه توضیح بدم ؛ سخنان حضرت اقا یک طرف ، وضعیتی که مسئولین درست کردن یک طرف
الان ما باید تا30 سالگی بدوویم تا بتونیم یک زندگی متوسط درست کنیم
الان یک میلیارد طوریه ک ما شما با هفت الی هشت سال کار هم نمیتونی بهش برسی و انقدر هم پول کمیه که شما باهاش نمیتونی یک واحد اپارتمان بخری
با این اوضاع 50 شبه کف خیابونم و هیچ ربطی بهم ندارن.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68248" target="_blank">📅 10:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68247">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⏺
صحبت های روح‌الله زم درباره حلقه نارمک و جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68247" target="_blank">📅 10:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68246">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuAYenWzQA6852TaH5RQ-3JVXvCpFGDagMi7ghGihQg3qf00zw42Se6-GSdCyNZrP7y8TuJCLDf1DvOtnXJJrOjpVTtZlCwGiqAU9-NK_cZDHoTNIEqdnGJOsTCqqQ2VetgMYOJmjpIO907oWiwsF_BMsXWsrqb8-sLDFIJ49E0VbLX25xg4ZryVuv5KOYcj8fWfkZ6ZFSXge-AnlbUdfGzodmnm1tyIMJoNC5wp-NgSDc32S1KzvcfoTRW_cmKVvqPPjm5K0R2yqp6zx0bgOSOred8R2h-D9XfCjUdEWBzn8-NSu0s4OrITWjxbKWzrerPiMRUeZdWERKI0zVhp6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سی‌ان‌ان به نقل از دو منبع آگاه:
دونالد ترامپ، رییس‌جمهوری آمریکا، در حال بررسی گزینه‌های گسترش عملیات نظامی علیه جمهوری اسلامی است. به گفته این منابع، در نشست سه‌شنبه اتاق وضعیت کاخ سفید، راه‌های تشدید فشار بر حکومت ایران برای کاهش کنترل آن بر تنگه هرمز بررسی شد.
بر اساس این گزارش، ترامپ احتمال عملیات برای تصرف جزیره خارک، مهم‌ترین پایانه صادرات نفت ایران، و حمله به تاسیسات زیرزمینی کوه «پیک‌اکس» که گفته می‌شود با برنامه هسته‌ای جمهوری اسلامی مرتبط است را بررسی می‌کند. با این حال، او گفته است ممکن است عملیات زمینی برای تصرف جزیره خارک را کشور دیگری انجام دهد.
سی‌ان‌ان همچنین گزارش داد جی‌دی ونس، معاون رییس‌جمهوری آمریکا، در گفت‌وگویی تاکید کرده است که جنگ تنها با ابزار نظامی به نتیجه نمی‌رسد و در کنار فشار نظامی، گفت‌وگو برای حل بحران نیز ضروری است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68246" target="_blank">📅 09:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68245">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68245" target="_blank">📅 03:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68244">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TgBFMhS2044yIR15VH0HHdz1iv-I4DnZo9AhALTHmShWa7cUa4WucbgNLrOgWCwhVAhcGymU_9ygLNBeLkhfGCYPaJHbw4OY20pE1Z2S0e-ylTJ1uGqWUT9Qxdz2WNKXf_9PnQ6JCjrGPlQXAHCq25QMn65qg5RiHUm9aMCMhGc6YrYpKX7EA3hrtKTgrrjObZpM5pjDw5g_v7BGd068mA5NSWXBPsicSq9GKygFUu6zG11kt5Nz-yXtgbAjrjT0PlihC3f0jBdScWQQXhsAHhEbDTWK3Szj3aodGOgmpxaw21xqKTfhx-uX4thXu0G_QOnjtjqd4tZCXdHx2eTjqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68244" target="_blank">📅 03:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68243">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4873db94b.mp4?token=o2M2InER9C9HwF2sH-2zuX6qAuFWMoZ4g9OXAToYABVUZgBcAqw5AzLMeHmgg7HcizYCeZRpMQWqc2cOTVsqH1dRMhJ-QN1R4rfiLyB0DV4MWSp2xX3_lrRRe1Ipii513Wi1DieRIE7k_VA1xK5RlBbqz_SwASvelAGN86hpT5nPAuZc3oWe2EwGy06X2BdaCyeXEMluhjmJJiVAvgXPDG-fuA9DHQlBEMU14nTy8HjX6ymcLVGQgqWPfoUJnJE4pqG_4jShWNzLLl3vXhMU0EfOUoYsg5SGsxGT9JKl32rje21Xl66Q6cp5VxMqUe8vh_1hlEipddnrJWgtI0UIDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4873db94b.mp4?token=o2M2InER9C9HwF2sH-2zuX6qAuFWMoZ4g9OXAToYABVUZgBcAqw5AzLMeHmgg7HcizYCeZRpMQWqc2cOTVsqH1dRMhJ-QN1R4rfiLyB0DV4MWSp2xX3_lrRRe1Ipii513Wi1DieRIE7k_VA1xK5RlBbqz_SwASvelAGN86hpT5nPAuZc3oWe2EwGy06X2BdaCyeXEMluhjmJJiVAvgXPDG-fuA9DHQlBEMU14nTy8HjX6ymcLVGQgqWPfoUJnJE4pqG_4jShWNzLLl3vXhMU0EfOUoYsg5SGsxGT9JKl32rje21Xl66Q6cp5VxMqUe8vh_1hlEipddnrJWgtI0UIDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پرتاب‌های متعدد موشک‌های پدافندی پاتریوت به سمت پهپادهای ایرانی:
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68243" target="_blank">📅 02:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68242">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1519c2ac09.mp4?token=HdpB69y1pJUYh8p63zAX5IEXVV3taNQ0WX0xG3bBcS2ATuRhYZ8-lkrRHvvXLEHAQJCcykW1ADNtOPaeB17pVcUFELTHKBo1iJ3I2G-7_Us1Q-d7VlW9dM_l0FsvZxrRfyiobHdxnirTd8ehPSyEUI21Ia8ZXbc2-_n1DwABkR3_1KbAbmLpmAxLQFArEklNDrtX0IQ1EZody9zbipGPbzhlQZKD-l0WL1s9_d_DKOQMQu_UtcWxSUFlZk-nUmCmFDMZzfxv3YEuq9zPoLcgfF15dywWlpvF6f5_9SNUI_rUT9zW8HO5W89uuswBT_k4hLvF1purVZiljpyGJY9Xsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1519c2ac09.mp4?token=HdpB69y1pJUYh8p63zAX5IEXVV3taNQ0WX0xG3bBcS2ATuRhYZ8-lkrRHvvXLEHAQJCcykW1ADNtOPaeB17pVcUFELTHKBo1iJ3I2G-7_Us1Q-d7VlW9dM_l0FsvZxrRfyiobHdxnirTd8ehPSyEUI21Ia8ZXbc2-_n1DwABkR3_1KbAbmLpmAxLQFArEklNDrtX0IQ1EZody9zbipGPbzhlQZKD-l0WL1s9_d_DKOQMQu_UtcWxSUFlZk-nUmCmFDMZzfxv3YEuq9zPoLcgfF15dywWlpvF6f5_9SNUI_rUT9zW8HO5W89uuswBT_k4hLvF1purVZiljpyGJY9Xsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68242" target="_blank">📅 02:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68241">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jw9CxsfgQAsSYieVk6UJqEu0iYcx-E0kyyBRYdmtFi4BaNnew2C6kRUVhEcKlek4di09pFFiPumnuYXkN6_7dGO0wu4upmyNGp2p1siB0st7xyaMESbN95AMWzb8ICIj51nzs5ZrxJfcswt5vcIh7vsfbPNoBesDSaNoAt_I9BUito4CpDtSBavsR43yU_qEAXjVLBK9Buy7Y0oa4YjZBoDvrz2ARaIIGkU33PY_3wsYb1-yzPh3bYD2Q7XoYZDxI6Q_X18ETijyC-eXXqS2cFJFvEDvNhP5imOXiZInc1NMV2StilbhUP15llw6Hwe8gwlr71f9R7_nzKJ6y5v-Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68241" target="_blank">📅 01:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68240">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68240" target="_blank">📅 01:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68239">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd7e59689.mp4?token=auQ9Q2XrWtJORexhA4dwT_gmA3zDS7tV9PNzKRznCrZgwadgOByXPL7xHUp6hinl4Oq3pjEhpLzcTue1c8w7uRr2PDJxO-bIR-AGONoXgCe5DF7bKptJWiNqoebKbpQaomt67GjLkcTV6bUi2TjxQ5YxGeGYXO_ayEl1-L7FI3Fpl78k48wexpf62eR4P701jTk0VjZd9sQQgoiOxrmLiZkbbTKHQNOr1BBcxbd5X74apV34Kcc4c6TQ38C1HVMOFDf8LNXTnTkUDTmNog4ltX4IcGH6CpeQlzAUUfV6GKcnKkoISWN8ztKGwnLwXB9BT_u6msfHAJYHF-gcaBj0UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd7e59689.mp4?token=auQ9Q2XrWtJORexhA4dwT_gmA3zDS7tV9PNzKRznCrZgwadgOByXPL7xHUp6hinl4Oq3pjEhpLzcTue1c8w7uRr2PDJxO-bIR-AGONoXgCe5DF7bKptJWiNqoebKbpQaomt67GjLkcTV6bUi2TjxQ5YxGeGYXO_ayEl1-L7FI3Fpl78k48wexpf62eR4P701jTk0VjZd9sQQgoiOxrmLiZkbbTKHQNOr1BBcxbd5X74apV34Kcc4c6TQ38C1HVMOFDf8LNXTnTkUDTmNog4ltX4IcGH6CpeQlzAUUfV6GKcnKkoISWN8ztKGwnLwXB9BT_u6msfHAJYHF-gcaBj0UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سنتکام تصاویری از اصابت چندین موشک هلفایر به موتورخانه نفتکش M/T Belma که در خلیج فارس در حال حرکت به سمت جزیره خارگ بود را منتشر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68239" target="_blank">📅 01:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68238">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
بندرعباس بوووم
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68238" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68237">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vL1IiKawB45ztTmOBjZo0QGdoSCVPa6KIfU7w73zXnmS0d3eY4hfjGQNY8M47u_K3Jhx_G0smuEkw_R6sVqUBkhjnufOcXozGKIKhrNMCh2YriYFJ1NO8nCOQh2XVm1dy0vTVnj5SBtIXFvjpo7Lq0i1CCNanuhFg7fjpQ4ylkhgUTp2zukFH0WnVxeDIuuJQEAwfRfz0Fdhwf_n2Xb6T5OLm9NSPuQRyycdqm3MTArp-Rw7I7ueAtlkr3urfPe57bnlri24KR-TsGRLDds5SrN9_WL-V0QcvnE7d9yxujJTAVupZmuYoCZctWtJXFiVpPsuQ9K2ZWeejszWH4N7Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی| امشب روح فوتبال ارضا شد
🇦🇷
آرژانتین
😀
😃
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#hjAly‌  @News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/68237" target="_blank">📅 01:00 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
