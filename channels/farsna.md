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
<img src="https://cdn4.telesco.pe/file/neqDXHuiCjcoNMmLf5_NQEMaF7HxQaXM24gNGzFxWwM04TAual-jt8djZn1gR8_hGoi1v9-AbMSuA7N8W1LXQDKZww6AJgJR3xg0BKnRl4uO7v8VFi8MvPe3ED64Gxr-9sE8bRrM1hQznjzqQfTspbcIUytlY9jDrJ60IAoZn2gyApeklGhTivmSnHSrInkFDcaC7DSOCFWyNiHqOx9NP5mCOsg31ome_ALDB8Qzi-nHB04vcyEnUKXHoNBnhW7S9Ag4-9dlsC7Dhteeob-GwhLi8bbZvOCttVWT_OSqppa0PC0VvkOsbInZ_hZkoV5_LeOQ_DkzVRKy9xWdEEOLdQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.79M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 16:01:22</div>
<hr>

<div class="tg-post" id="msg-462819">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/332d0ce5e2.mp4?token=ZvFSHu12kULve77Xn7LHsZ42hQPywjlnQNiYIK4xf_cqK3xNpL-OgNC9a3kpSXDOKUagD3f02CqtZrFwJw9PeswfsEgLco4hXNk0r2ddh3wVkA9JKlkUCWSrzFRsTXzlO-AvKtol2teYKch6wUMo5rEOfHFGCfU-v9xIaSNy8DdjqUBuJjoiypY66nk8q3-bJWLoMsCifNhoR5kCiEEpF3CbN63DvXHYQgY2D-s4hvVmAsXr_EFMsS_iCtfSfIwj-vIrYgoUdRFcjltnIlUrExsMDFO828FAzLg_rtYMLBykS97Jgz5LN_jrdDxUxayEiwm-e9lGaob4vDjX_WJNtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/332d0ce5e2.mp4?token=ZvFSHu12kULve77Xn7LHsZ42hQPywjlnQNiYIK4xf_cqK3xNpL-OgNC9a3kpSXDOKUagD3f02CqtZrFwJw9PeswfsEgLco4hXNk0r2ddh3wVkA9JKlkUCWSrzFRsTXzlO-AvKtol2teYKch6wUMo5rEOfHFGCfU-v9xIaSNy8DdjqUBuJjoiypY66nk8q3-bJWLoMsCifNhoR5kCiEEpF3CbN63DvXHYQgY2D-s4hvVmAsXr_EFMsS_iCtfSfIwj-vIrYgoUdRFcjltnIlUrExsMDFO828FAzLg_rtYMLBykS97Jgz5LN_jrdDxUxayEiwm-e9lGaob4vDjX_WJNtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعری از شهریار با صدای رهبر شهید انقلاب
🗓
۲۷ شهریور، روز بزرگداشت شهریار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/farsna/462819" target="_blank">📅 15:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462818">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwKiZwJFrejyW89qLEkXE8QkiULgCNm-G1oRve0758Da5V3iSFdT_70mCnllTxF9ssonAY-TNpMovxtdgeGwgmp7tl9D6F0eRUcfk0MpSpirCPD5eiplORF25XsiDXQ-Gj3s35fkF0icJEULHbeViQdVGd70hfva6j7HMCfpjVy-nAjr4hvW4ecOvqDfuwigYsiMoxWCzNalmWvCcteFXgshRYHLzWx6gmeKMVkgBurM7n-T6fvM2vQrppGU-4diq0MGWJkfnVqdbVl5uCJM0QgXQWEMbpy_QUBuCQ_4vX0eYMJjnO5PdtcBy0PmxosVHDKcU8pFupdz0-Bh_GFi9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندۀ قرارگاه ثارالله: امنیت کشور مدیون مردم جانفداست
🔹
سردار نجات: ما خادم این مردم هستیم و ما باید بتوانیم قدردان ملت ایران باشیم.
🔹
مردم ما از ابتدای انقلاب مقابل دشمن ایستاده‌اند و درنهایت بعثت مردم با شهادت امام شهید اتفاق افتاد.
@Farsna</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/farsna/462818" target="_blank">📅 15:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462817">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLsas7jO4ujsD8Y9RZEmclQYnJN6DVzmnAevBCI4xqqMjA6BXeYcLTF8PkEg7bFLCBQJSPFAA-BMPGFyW9mm28l-aGNjnJ3DJMr4ZAOT8xXSjndRxiQXWlTD839eKc51hUq1WSxfEK8Dc30-JqpC7vXfkL62qdspIwoj3ZUGMTp6b0Y0LvS4l9KQoTv5qoje85DWSvBpM0IlIuPIb8IxviDVlT9wO-L8774iAffEYOHMQJUHncFUmmNhzTl6ya8erTFQhzsJ17EbxsBOnxFuEk3T1MfTmS56Sr0Ua8SSsdxip9jN3d_UI_ht8MyNEonPrL_dW3V4VW-nnOqB1sEGGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقلال-بیرانوند؛ شایعه یا واقعیت؟
🔹
شایعه پیوستن احتمالی علیرضا بیرانوند به استقلال بعد از پایان دوران خدمت سربازی جنجال‌برانگیز شده است.
⏺
دروازه‌بان شماره یک تیم ملی معتقد است شایعه انتخاب استقلال به عنوان مقصد آینده‌اش حاصل برخی‌ها شیطنت بوده و چنین چیزی حداقل در برهه فعلی واقعیت ندارد.
⏺
از طرفی پیگیری‌ها از باشگاه استقلال نیز نشان می‌دهد این باشگاه در حال حاضر هیچ برنامه‌ای برای جذب علیرضا بیرانوند ندارد و با خرید محمد خلیفه روی این گلر این جوان سرمایه‌گذاری کرده است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/farsna/462817" target="_blank">📅 15:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462816">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f77002ffb.mp4?token=S2Iud_KS_Bdy2Hi9LF2_F3zbXJN8_rwkwCRRXPMXzcy0bqEKZeq1LaXpW8YygCKPa9u5HAcoDO6CphqLrVD_LdCzwfkG3lUgIlYdrnNB9sCaHILYKCXSftENEhuH7LqtnIQbVjXQxpVpOfTTenIliTIzhSOA7MoYK-Szve7zpCTUuWeOSqv5YLHF5ztWn0CX7Q2eJXGrynlourYEZuH9x1wvns_sTnk5_kO8c-tnSTGzawq5nFJaHyH6A3A7yEOVto2pLdfFs-sN3w-j-8XRyMGZyNZEU_sL9X6cMEIBeqguHsTX6RlvP8bdyhwB8WtYS4zNSEub1ECrU4s-ORGOdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f77002ffb.mp4?token=S2Iud_KS_Bdy2Hi9LF2_F3zbXJN8_rwkwCRRXPMXzcy0bqEKZeq1LaXpW8YygCKPa9u5HAcoDO6CphqLrVD_LdCzwfkG3lUgIlYdrnNB9sCaHILYKCXSftENEhuH7LqtnIQbVjXQxpVpOfTTenIliTIzhSOA7MoYK-Szve7zpCTUuWeOSqv5YLHF5ztWn0CX7Q2eJXGrynlourYEZuH9x1wvns_sTnk5_kO8c-tnSTGzawq5nFJaHyH6A3A7yEOVto2pLdfFs-sN3w-j-8XRyMGZyNZEU_sL9X6cMEIBeqguHsTX6RlvP8bdyhwB8WtYS4zNSEub1ECrU4s-ORGOdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار اعضای دفتر امام شهید با خانواده هنرمند شهید پوریا شهبازی
🔹
شهید پوریا شهبازی از هنرمندان تئاتر و آهنگسازی بود که ۱۰ فروردین در مأموریت داوطلبانه در ایست و بازرسی کرج، با حملۀ دشمن صهیونیستی-آمریکایی به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/farsna/462816" target="_blank">📅 15:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462812">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H88ohkww2Dnm5vE30yUlY3QgCshET8KmaLxxzc_Ybgg7yIz2Di4uiaMcsnefGWVEJ8rSe3VBFhsGBko9-HVklz7m8fgIpC5EDHwR0HNcWuHpfPO8CWoj7lNwRxi24HrLJVz6gIa2jAOHog-17u2hW_JEgAlxuzX8Cq4g4dn-HNzW14_DWc7I2fTfTlOPS7xSLC5m9ZJYxyG65xRKmgbjvnKuJ8xvwNTBgxtlOYsCzuRnjrLs1yHAS6FIQEwy6mzwOSt4Kqk_GFcDMOHHoJDzUYeBp0XpikeU_wK7qYY5WvrUeo7iD5Y2tt-1w31vTrbXVjBB5xNTs5RhQPvIizdxgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NkLV5tyeu7LyHuk3nDfGcTv1fFpxpnVgxbmNnanqPwthd0qnrwgDPvIDMGKTAoOfGvgP_Y4TZo01rW2pyRKw9HoMiKZ3OXOYgV8fxs3girjPET4IAjZJKKtWAgz0QspfKxvPix4jjQWRTpTVIiSnCtKv3kXZfMvRnHogf_6kfHuKS9eshVzz8swOUxoGXugzdsxTJZ5HSaO_Sr_JYoWauE_WDVhTvhd0C5f56beK4vIs7QyTslDaGpEAP7_qBJgEfNI0KSQZsmjwglA1OKkf_rSkdjM3pHRaVlimvLpzliMGWs8V9TIRCRL9AhXWPMUn_he2Bol9LKfFDT0jUir7Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u8NPGWD4kgESoVl_07xUHUUCzImc7yaU8fnkMwjHc5Hg3YT8S0ImIgsSP0pkTZaIvBTVm1rNTLS6CHKr825EAsrF0HbzYpHyLtKZmVjScRPRQ8kbcQCZcd1EyVxX91TAeenKyZng1uAchwtLFTPLBB-3p5vuC86SLpSpTeInOkczQ7G5nlii5__KHIq5UIlPD3j8fLK4LVUy0Lpn2240WFhaUfm_82pOwV1bm_CFeeoB5ktwf-NnaP5zAFh8FlecYNq3krYOOHYKfvb4k6Vh-krvR6tAxWIxEb79k4iYq-euJiWF9oTFtFR7sYHcFEW_1PjZOXxL-Ea35jrckXrS0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NkLV5tyeu7LyHuk3nDfGcTv1fFpxpnVgxbmNnanqPwthd0qnrwgDPvIDMGKTAoOfGvgP_Y4TZo01rW2pyRKw9HoMiKZ3OXOYgV8fxs3girjPET4IAjZJKKtWAgz0QspfKxvPix4jjQWRTpTVIiSnCtKv3kXZfMvRnHogf_6kfHuKS9eshVzz8swOUxoGXugzdsxTJZ5HSaO_Sr_JYoWauE_WDVhTvhd0C5f56beK4vIs7QyTslDaGpEAP7_qBJgEfNI0KSQZsmjwglA1OKkf_rSkdjM3pHRaVlimvLpzliMGWs8V9TIRCRL9AhXWPMUn_he2Bol9LKfFDT0jUir7Qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از آثار حملات شب گذشتۀ ارتش روسیه به مرکزی در جنوب‌شرق اوکراین
@Farsna</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/462812" target="_blank">📅 14:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462811">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d01da4d854.mp4?token=cmwQx8rPu2_WEkdvTnEU24bFYhyhoosOKy_eMzMR9_lVm46BkC2eWAI7LVnfg9lrfnnBTT5Dg2WhXvDaqUM801dhZPWGs485sCBRLj6iAdfLQXaKXcBRmU9Teyr96tkBJXcuLAy_DRJsYYupKY7uH_U7oXNzhIsOEgyNoVnbK2KNEAdVpO5hBx8p9UwMXyw7uYb5nCLGcpxLhwLRK0LB6BNjLRu-pSWattmteR9u6OVjJ7X8Gc_Kn0j8UQmklbubI404nhGIxYEfw-QXRNwoot068GWMNP5xE9qOYdpNCCN9-eNT063cQupt9oGnp9zRpUv3VwSe5PhKkJlSbtYwCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d01da4d854.mp4?token=cmwQx8rPu2_WEkdvTnEU24bFYhyhoosOKy_eMzMR9_lVm46BkC2eWAI7LVnfg9lrfnnBTT5Dg2WhXvDaqUM801dhZPWGs485sCBRLj6iAdfLQXaKXcBRmU9Teyr96tkBJXcuLAy_DRJsYYupKY7uH_U7oXNzhIsOEgyNoVnbK2KNEAdVpO5hBx8p9UwMXyw7uYb5nCLGcpxLhwLRK0LB6BNjLRu-pSWattmteR9u6OVjJ7X8Gc_Kn0j8UQmklbubI404nhGIxYEfw-QXRNwoot068GWMNP5xE9qOYdpNCCN9-eNT063cQupt9oGnp9zRpUv3VwSe5PhKkJlSbtYwCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور مردم صعدۀ یمن در حمایت از پیروزی‌های نیروهای یمنی
@Farsna</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/farsna/462811" target="_blank">📅 14:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462810">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9384af4849.mp4?token=CUw9iHo0YudU1aiLQcdTIX8uZCaLIWjfQJ9a-fkcQtmJm0TpdITuEcrshFPGCHjrkZzgYBv3ty7g-R_EzwUtKxnP_gCzjF5qPD3IQLKDJCeiEqrbOCQBZZ_-lSCyK8ZWNTG8IiCZsE9hZ0vNmn9IK-LBz1tNwUa1U_3dzjcPn29WfmYbXLiDL1mOLTP5zniFDEO4nEALW51H8f1haE53b7xwLHFrQx6BlI1LXJtbnnG9MoZwOQZ5zUSNYdrbVMPo2mT9hNoSAxOPnSFe9lmojcN3LHhzhwIV5o_yzV4B1Q3oA4kGMEibPm7jL-TdKR7BXshtd_q4hst_35x1bAPXZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9384af4849.mp4?token=CUw9iHo0YudU1aiLQcdTIX8uZCaLIWjfQJ9a-fkcQtmJm0TpdITuEcrshFPGCHjrkZzgYBv3ty7g-R_EzwUtKxnP_gCzjF5qPD3IQLKDJCeiEqrbOCQBZZ_-lSCyK8ZWNTG8IiCZsE9hZ0vNmn9IK-LBz1tNwUa1U_3dzjcPn29WfmYbXLiDL1mOLTP5zniFDEO4nEALW51H8f1haE53b7xwLHFrQx6BlI1LXJtbnnG9MoZwOQZ5zUSNYdrbVMPo2mT9hNoSAxOPnSFe9lmojcN3LHhzhwIV5o_yzV4B1Q3oA4kGMEibPm7jL-TdKR7BXshtd_q4hst_35x1bAPXZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صف‌آرایی یگان‌های مردمی جان‌فدا در رزمایش امروز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/462810" target="_blank">📅 14:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462803">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ThDJY8FuMQjffmB554sFas3B3V3YvYuss1D7hQkWMFOpbvcvT7lA4dFyjQ-Fxist8ZjgNeVt3nDjYTOuarRmHKfH1LzPsIdlcryWDxHyvCNrNATd1cRjHq8bkQ3zHBr6QGe7b4xrWXBwdIswkEMZPsic1KSjjZTL1Soy1yZTSfi1PFLKJ98hUM-qaIBr8GRIezj6TZiUERlWzcTlYGv3G4Nt55mOfIrOV4PnkA5u2NzxsC5EkuMPH10MTIeYM0TGJlbfP1N5bTs-QYlWEU_bCKFdEkma3w2EplVkDP0Ay1elkp0LzmWKLGYOcfPGnMnx5XyoRfg7dBO9N6A9lCplMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cjD-L42hWT8gekqHJCmKwTRC-JNcxWEp8mJjOp-O6QmbeG49Sa0vp2fz1HtRi28pgjSwGME_Fi2S9NAKASxJdCVsOc3RhEQw4cgs1nX6k2sRn5B2wiFOPWelgAn8rHFMng-h7PMF67a-n9ovETuZDIr0xb6NPk_9g9r3CcJzEc8mDw8uC3kMAe-WSivQUh_Hp58-92qr-auJjq9mdI_BFzOdtm9uMh5QgvpL5lGUvwIM36cBr8Co9b1GzKr1tWTyBfGSgybAEEgBWgBoUGSrheiUxls8d_SmfgZ3wR-FpkXZQ1N0f3It8VTpJDFuZ455vmR6E8lbNmSe_cjzmr3XSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kRHdXnsSTEeYqjLG6hMJRLMspFKx5LiEEKWycpgc3nmlJKc3vmeSuwbRfOYmA-oblIMJJ5HoJpas-YwcME0CYa1INyVooEYXs7ME6fJojIvsmGUlQ_VXs0hkzYT9bRChnZ5CIC7QO02I5WCizYxnTcu9LrNAneYivo3bA_GNfgY8VGSg8zOPI0YJySJDvc4k81IKlc6SLKuHY0r1OXRmLgRN0elbZyPVD-iNgU6PiaAS9mhU8U829B69mbeTpivUkdvbuzYD9tIVjwXL5t1aKgC7z7s5Wj93tQSzOKrz2-xvWLR2jUFf_O8x8nTCmye6glxTUaqX3cxWGGhcUPlcnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bp2GXaFKW8EwuhJmZdmTYtoP_VTiYmJhex3sZBpCBOLh0HXKWk21Y7Lbqqg-Uj9I93P8qN8ZiQIdpTE5IHuI9yDvvxkckSc07yygIQQbsnhupm3c0AbvwPMilST1u04yhK8oX1V-y9gIcBtot1l04CDbTq8hiT7C3ERkpNhgo1l_y2EN4G8pE1tO_k1vzKH1EC9Ph32o0KyklJVZu_uwEzNi-dLZPtM3oYUdfP6K_ckdEzZVQ36Bab0JfJBifsFE52H6MVIvkiRAhTB-GYwbrhNdXBc4zUUnYHW2gnVGQEJvkFaM1lmPUj1HdF9VOFMmaspMITSLrxjk0HZXfqCJNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfyUHs1NJ4n_FUNTeQgSRTMWC_IbcehmS1VuLhGWiOT2QYB5B6fNvdfzcbEILaYkR-rJ4p5XnXJjLFBn1uqcUHCmuSDTQisTtN_iqSAiyj8IMA78b4GPcTG_YThJ_uC3p0QjXtrC3F0LHrEPb_mFIakEXMgJUTyvtQIVKYtixbujGZB5vSR2mYOG9_Mc-vjO0irWQHQ3KE-ObCdN0h5qFHMg45XTe-eVMsERREUsZNCujzbz9RCGObRDXs4vH6Y8pmLIhhn-DK76YOVlBMc-yF0uWSABuMYVwTcP_Qji-I8dU_iHghW5IWozPd2XDYdGN48WV7yFogz8s9SNR7xAfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LQqT4A7apZT9RFVUFYaRup-KMVKiQ19TycBIWi6IGt7bo4jADDUpY_Mssx5QDCWPweOps0HSe_uHxQKfVIGtTjSfkR_X3U5ftURcz-BsEe_0REjxOkGPUT6Z5wfu8ZjTWC_WTqwwAuw-C_U8_A3c8R5oqNV0QkUK5NV4Zu0_R3BCr4FKdODGVnz2-ZOANc1LwCuFLipFy04Pggn82uu_HUu3I4lmp0u-J3Y7XYxNCOc0P5v5iyyIGksJq_3pkEgAn2qkkhx85yDdR21Z_rltHE5J0iMuEbwMXynGY-suzmeOgPDbzKhrxwpeGq9zx2sFRr2uoFq3gEi1_GDjsrTIcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pyhaw1MnPxN2X48hz4PfeAkmooXaS_UA-yt2wPPJsR1B8qZi1AsgI6-WjX-gAWu4KEpqtT9Z6Tlvu5eoR2mz2YVVqb0kpDV2hUDuATR-0xr4Ey99fUYRE-k__SQn9AIRA1EhXVyZLx69Mc0gWGF1JTiXQXFWk6X7H3cAtHOFbQd1-pgXGe4jyON1v6wkhwRmrftWi5kvjtUmC8DVhA976h2HCS2iI8Rk6-ZSGvo1r8m6166_ZGtGfhO6IQ2SGJqSM0ixVrjMCR746HHbYjZu12QqlJmi8OT2MO2uBjQeJ2Hpal67JrBygFsOA57WGNBafyY3W2oiM-Xd3G1VGQ9t0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ماکان کجایی؟
🔹
جشن پرواز بادبادک‌ها در همدان به‌یاد دانش‌آموزان شهید میناب.
عکس:
امیرحسین ترکمن
@Farsna</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/462803" target="_blank">📅 14:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462802">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-9eVJe0WpeJ8sqxGCubzp7ZAj9X_Zjt_ei95Y10vU_jSJmLePd_cCUuFXODDKbTzlrYZzlPYrqciXcHDrs_sl2O0mtHB9I5JeUALzEhkPiAQbgJL09IwV6MvF_ecN2zemc00Y40Fk3XY5FOUJgeLZAtwtzipNAhNJwywYeTO3XJa3zrFwwXmKhHun8SvKaTy4fGIk-6LK548olkOyjpE1ku-DoFDyqf8o8gAIodz5Tbh65PpW7q0CWpCpF8vWUJQQwmzsoaFsHJzrA7G0bckPnz2W930mGPz9DEPbS7xpKsU74K3lby102XQcbwypPT7pb6Assbm_shY_ojTCjZKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
زخم کاری چین به آمریکا در میانۀ جنگ با ایران
🔹
گزارش فایننشال تایمز نشان می‌دهد چین حجم دارایی‌های خود در اوراق قرضۀ آمریکا را به پایین‌ترین سطح خود از سال ۲۰۰۸ تاکنون رسانده است.
🔹
پکن با کاهش ذخایر دلاری خود، به دنبال کاهش ریسک‌های ژئوپلیتیکی و مصون‌ماندن از تحریم‌های احتمالی مالی است.
🔹
این اقدام چین در میانۀ جنگ آمریکا با ایران، می‌توتند فشار اقتصادی بر واشنگتن را مضاعف کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/462802" target="_blank">📅 14:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462801">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ded40dc29.mp4?token=TfYNUpOcMunI_3vLjsaIj2jpbunnQyyBm2QVeXGpHjc8bwwj77TTp7pApXMRhut_ViCWEzPNvYSljoduZjzv8zFL7pA6hGzCkpYQksrj2TCi_p5aI_GzzMkXIpWSGp4HKYrM6BwNNejdFVr-yh-WDYiCLl2-kpaW3QIfoZ5VyCTiN_5IOnps3a7-6iaGYCpS7T-uIOLotm1N_bQ5WHFfRR8csxKh7VwO-kPzSwi97nPVLDvT4bjeXW-cx74C7Zi33RHDXn3H9lDPnAonVGsykoQNC-dhbdEOp3R9OcE60MIyqb5qciDWtaRBPDpx7w8pYjH0F7_qvDASt58QNr8Tug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ded40dc29.mp4?token=TfYNUpOcMunI_3vLjsaIj2jpbunnQyyBm2QVeXGpHjc8bwwj77TTp7pApXMRhut_ViCWEzPNvYSljoduZjzv8zFL7pA6hGzCkpYQksrj2TCi_p5aI_GzzMkXIpWSGp4HKYrM6BwNNejdFVr-yh-WDYiCLl2-kpaW3QIfoZ5VyCTiN_5IOnps3a7-6iaGYCpS7T-uIOLotm1N_bQ5WHFfRR8csxKh7VwO-kPzSwi97nPVLDvT4bjeXW-cx74C7Zi33RHDXn3H9lDPnAonVGsykoQNC-dhbdEOp3R9OcE60MIyqb5qciDWtaRBPDpx7w8pYjH0F7_qvDASt58QNr8Tug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از رزمایش جان‌فدایان ایران‌زمین
@Farsna</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/462801" target="_blank">📅 14:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462800">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3c5fae1e.mp4?token=PCUie-AdxUJu67BoKjUUHQjD772DkWWWRWiW6injQfHzNQYolSBIYqbPguWh9Vp8UmNF2__SPGMtsMIxYrWtL0kYNUJdWqjFoDYE5WvEVEXg1DvFYeiNnaK4ge1_ypIJkkhs4449UeB6ObMqfo91OeuwTlWbCuLrIOSZdPgH3VapbbKNACpZVKI5XWTBzoQcBpMgPFdQ1nufpkKb1DWNl8tFFShK9L7vDZ6G4sHNxlCAPPvjAuqov9l4NR-XrHz-zF1HRaQDSBmqXPeFcyRAM8FwUkKMbTqLY0bEr8SbFb0oaBuQtTmnBBADJ-r_MhaxWYGkdBNM_pMT3jjvKAWUNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3c5fae1e.mp4?token=PCUie-AdxUJu67BoKjUUHQjD772DkWWWRWiW6injQfHzNQYolSBIYqbPguWh9Vp8UmNF2__SPGMtsMIxYrWtL0kYNUJdWqjFoDYE5WvEVEXg1DvFYeiNnaK4ge1_ypIJkkhs4449UeB6ObMqfo91OeuwTlWbCuLrIOSZdPgH3VapbbKNACpZVKI5XWTBzoQcBpMgPFdQ1nufpkKb1DWNl8tFFShK9L7vDZ6G4sHNxlCAPPvjAuqov9l4NR-XrHz-zF1HRaQDSBmqXPeFcyRAM8FwUkKMbTqLY0bEr8SbFb0oaBuQtTmnBBADJ-r_MhaxWYGkdBNM_pMT3jjvKAWUNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش «جان‌فدایان» تهران؛ ۶ ساعت پس از آغاز، خیابان انقلاب همچنان در تسخیر جمعیت
🔹
رزمایش ۳۱۳ هزار نفری «جان‌فدای ایران» که از ساعت ۸ صبح امروز در تهران آغاز شده، با گذشت حدود ۶ ساعت همچنان ادامه دارد.
🔹
برخلاف اعلام اولیه، جمعیت حاضر در خیابان انقلاب اسلامی -حدفاصل میدان امام حسین (ع) تا میدان انقلاب- چندین برابر تعداد اعلام‌شده است.
🔹
خیابان انقلاب و اطراف آن هنوز شاهد حضور گسترده مردم و جان‌فدایان کشور است و رژه همچنان در جریان است.
@Farsna</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/462800" target="_blank">📅 14:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462792">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5683a85a1c.mp4?token=cxtnP4MKEhTR-43I0_yeqNQA5o2px32MSANprWPvP9AHNGlaNiEGjEbOGasQS1OtIC2ueITHGa6AQw32QemuDwhcCPLDB8eDOhRFuBJcq-FajJh9gFxMoEZXPLgF1AldRqpOvo2oO9U9SilmJZTSQR3KBg14n1-3fMKC0TB2f11Gtg-8dc4cWdjEmWRu6e8oRakOoruPlTTear6acQgxXiOn2aU7TzdT1IeZyVQjgYhDKuo72iRmCFE4PT9_cme88QKYbp2k_XgF0UDKpjvzqHUK2n-S36uk6b_YRQ1UnawuG7Z9e7bPwbtlKkxSG1DfVG9M9GnG7-M_NUI8ZAnkzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5683a85a1c.mp4?token=cxtnP4MKEhTR-43I0_yeqNQA5o2px32MSANprWPvP9AHNGlaNiEGjEbOGasQS1OtIC2ueITHGa6AQw32QemuDwhcCPLDB8eDOhRFuBJcq-FajJh9gFxMoEZXPLgF1AldRqpOvo2oO9U9SilmJZTSQR3KBg14n1-3fMKC0TB2f11Gtg-8dc4cWdjEmWRu6e8oRakOoruPlTTear6acQgxXiOn2aU7TzdT1IeZyVQjgYhDKuo72iRmCFE4PT9_cme88QKYbp2k_XgF0UDKpjvzqHUK2n-S36uk6b_YRQ1UnawuG7Z9e7bPwbtlKkxSG1DfVG9M9GnG7-M_NUI8ZAnkzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سال به بار نشستن طرح‌های برزمین مانده هلدینگ خلیج‌فارس
🔹
هلدینگ خلیج فارس طی دو سال اخیر با تمرکز بر رفع گره پروژه‌های نیمه‌تمام، مسیر بلاتکلیفی را به بهره‌برداری و تولید تبدیل کرده است.
🔹
در این مسیر واحد اوره پتروشیمی هنگام، طرح تولید پروپیلن ارغوان گستر ایلام، طرح تولید گازوییل یورو۶ نوری، صدف خلیج فارس هایکو کارون یا تکمیل شده‌اند یا به بهره‌برداری رسیده‌اند.</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/462792" target="_blank">📅 14:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462791">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDSqnKL37OaBsDNkZtQAVKesbrzd4FcXmKObiOe7xwHtjoZ-OroaHzWUKOWzunKXFBpHZb5pkPWH7WZsVNWmn6LRIS6knUk0rQvXTB44tfu_j61PboZrWKPZeG2oaaH9Oq34sh9e52QrQwaDM-_V1M-alqScDkf6qmh0R76em-HZnrDgzwSLUvEh3mm4WLpJgmNfKUX_QrnfGs1uHlMkGlqsqkuJdPSKoAZbJNCPDpVDw9KHeuLUfP78kADxS74UHx3PyrsairJkI9Dx58bRHyg5n1Bcy8iC97tijo270xcqkU6uFU383g-6kSkzqj6YnWLpw12TzqxsMGqv0Q2t_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
یکشنبه‌ها در پارک آبی اُپارک، بازی‌های گروهی منتظر شماست!
در سانس بانوان، در کنار آب‌بازی و تفریحات اُپارک، در بازی‌های گروهی شرکت کنید، با دوستانتان رقابت کنید و شانس برنده شدن هدیه‌های ویژه را داشته باشید.
🎁
🏆
🎟
برای خرید بلیت به سایت اُپارک مراجعه کنید</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/462791" target="_blank">📅 14:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462790">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/462790" target="_blank">📅 14:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462785">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3763fb0f9b.mp4?token=hdNvWnVX52jWKnRZVjg6uL4bpimJ06U48nIqLArwMdqwVu0Gcqv-D_eOqPXf6W1A_Fr_zyCcDAJvWjuNyBaGcL4XfjL4dvpn1PKkaTH19E8ECXefdhMwRr3-SFT-TFfiGJYTjWa75XsZdXPZjMuWFt5sT64skEmQiYB_DtN6q8bhYH2li4qYnsEWF8QROM15l43gTBT1a8FcbKnQ6bp9qEoDCg7jY4aJ5WOYHlag1mhhIEnoI0K56WinQVQJYRhVQn6KjQTdZ5bUobRJxSW71m8RxxcQ9WX_PRiXPJ64GwLWNRhznXnwroNP74LYJ45IGLSu_MW1UZrzQsPskVDqwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3763fb0f9b.mp4?token=hdNvWnVX52jWKnRZVjg6uL4bpimJ06U48nIqLArwMdqwVu0Gcqv-D_eOqPXf6W1A_Fr_zyCcDAJvWjuNyBaGcL4XfjL4dvpn1PKkaTH19E8ECXefdhMwRr3-SFT-TFfiGJYTjWa75XsZdXPZjMuWFt5sT64skEmQiYB_DtN6q8bhYH2li4qYnsEWF8QROM15l43gTBT1a8FcbKnQ6bp9qEoDCg7jY4aJ5WOYHlag1mhhIEnoI0K56WinQVQJYRhVQn6KjQTdZ5bUobRJxSW71m8RxxcQ9WX_PRiXPJ64GwLWNRhznXnwroNP74LYJ45IGLSu_MW1UZrzQsPskVDqwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عروس و دامادهای جانفدا در میدان انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/462785" target="_blank">📅 13:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462783">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926a0e6955.mp4?token=CLdBlmi-YeY882TaNUwXrI9CS3LKX_-k0abWFwU5-rxAgtNpURzPeNTCXJjjzAc_uCmKSo3YLPcwEBIAZjKcU1qyhE0EtUTN21NKJD62XYAnmX6Go_9B1GZ63LFcc5g66jlkU8qRuJryIcMuE6deUHjfFTPSp3Y7lA5wuSi9E7KsJB7VNsQO5mjAKkOU5yfQE_bq86RMep4s4rfKNw_Jj4uRXAEIUGEFggRCGoRxWT7zT9nJ0onQiQ6lVG5XxZSQcpmf57Y9xDpz89CrG4-O3FL9IW3fBa_c5s6Iy6fSMqS1ffN0Gtr0gR2ss0Q2tZPAvncSDf3IkzWJ4ccDt4-Z4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926a0e6955.mp4?token=CLdBlmi-YeY882TaNUwXrI9CS3LKX_-k0abWFwU5-rxAgtNpURzPeNTCXJjjzAc_uCmKSo3YLPcwEBIAZjKcU1qyhE0EtUTN21NKJD62XYAnmX6Go_9B1GZ63LFcc5g66jlkU8qRuJryIcMuE6deUHjfFTPSp3Y7lA5wuSi9E7KsJB7VNsQO5mjAKkOU5yfQE_bq86RMep4s4rfKNw_Jj4uRXAEIUGEFggRCGoRxWT7zT9nJ0onQiQ6lVG5XxZSQcpmf57Y9xDpz89CrG4-O3FL9IW3fBa_c5s6Iy6fSMqS1ffN0Gtr0gR2ss0Q2tZPAvncSDf3IkzWJ4ccDt4-Z4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انفجار در مسجدی در پاکستان با حداقل ۱۷ کشته
🔹
وزارت کشور پاکستان از کشته‌شدن حداقل ۱۷ نفر و زخمی‌شدن ده‌ها نفر درپی وقوع انفجار در مسجد مقر فرماندهی پلیس در شهر کوهات در ایالت خیبر پختونخوا خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/462783" target="_blank">📅 13:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462782">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fB_WQyf1j6lX8Iy-XVAyxdv1rxWZplVOmuQAyDtGcPLw3pWWcQr5lwhm0hZ3f2UGsefW-37LL7NKKhz4zyBRYc8xWr0-eJoNRwwfQHiInvzgIO_Bl9inouN6Mc1ff5i0jZ8qs1eBzcEB1hcVpSv0DEGyFxcX_BhkiHPXTi-b7m4w9alcfrMVIrA2-0eBbFu42V7JKpAXOLP9XnzNGsvAn2Kb-OwRaIIpWQyffiibM8xlQcHP0i9X7k5Vxx92x1d3Xlc4YvCO-rDnf1LVFNnex40miWDsi30f8BKFafjVrF6bHlhSQkmCgNMoJNEggLi5adE57W_0faqWTbo5FlwdUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطیب جمعۀ تهران: تا تحقق همۀ شروط رهبر انقلاب، مذاکره‌ای در کار نیست
🔹
حاج‌علی‌اکبری: دشمن به استیصال افتاده و برای مذاکره التماس می‌کند و میانجی می‌فرستد اما تا زمانی که همه شروط رهبر انقلاب محقق نشود، هیچ مذاکره‌ای در کار نخواهد بود.
🔹
اجتماعات مردمی تا هر زمان که خدا بخواهد و لازم باشد و رهبر انقلاب صلاح بدانند، ان‌شاءالله با قوت، طراوت و ابتکارهای تازه ادامه خواهد داشت.
🔹
به حمدالله وضعیت میدان خوب است و رزمندگان ما اشراف کامل بر صحنه نبرد دارند. مدیریت کامل ایرانی تنگه هرمز نیز یکی از موضوعات مهم این روزهاست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/462782" target="_blank">📅 13:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462781">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bb35813c4.mp4?token=NhMQjS3nQWhHQ0TscMz2sy24DT9og-QeFxBy5zJwV6_bH7snUS0BUomYshPG9ghTm3Q70CPxE8wx6J-hYhQt58NqyA7DtLuT913y1CtvGRbg6fWNVdxUK1kH-7J0aEH8ABI1DuR3BlaC2gUwlPw0ueCnPyYJwjc-PG5Cq9kfVHkbS7ekan0htc-6r1AQxIQ1l0cnw-k4YLKFX5Ytyip2Gm1ve55pZL5WTraBJJbt-XcUUE9LSWkiicTDF7gQiO4F4RmB6cQXTZKfkb86I-qrBwVga78RV6HEVMngFN0fBcEBu7FMJi5pmauXMi8lLgkhVqXpOsEeBM7VlU5V-amDtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bb35813c4.mp4?token=NhMQjS3nQWhHQ0TscMz2sy24DT9og-QeFxBy5zJwV6_bH7snUS0BUomYshPG9ghTm3Q70CPxE8wx6J-hYhQt58NqyA7DtLuT913y1CtvGRbg6fWNVdxUK1kH-7J0aEH8ABI1DuR3BlaC2gUwlPw0ueCnPyYJwjc-PG5Cq9kfVHkbS7ekan0htc-6r1AQxIQ1l0cnw-k4YLKFX5Ytyip2Gm1ve55pZL5WTraBJJbt-XcUUE9LSWkiicTDF7gQiO4F4RmB6cQXTZKfkb86I-qrBwVga78RV6HEVMngFN0fBcEBu7FMJi5pmauXMi8lLgkhVqXpOsEeBM7VlU5V-amDtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لغو اجباری جانفدا در خیابان انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/462781" target="_blank">📅 13:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462780">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKfwF3DSMs8YmQ8Y3JIHps1O3rFmKDAtGrBZjbF0IJhFVeOUaQWaqbV1nWF2TCUVb60YxdSKD-_wcNQHDuaB723aUVymo-TevzreGFjt_FfBcCJkmdz6R7qgel5jxMQVY7UNp_tcsEmFA_S92lQmrhQTHfGiykISXjjzTkwTeugLgygv5gdstGa0MD-miibNARlh9hbAQA1OWZrgKHGA-RA20O_Phc3leAaNEFZORPd-SZXtf16g4QdTHTDV6hUJey64Kv8oi4xoMaSd3_E4MQRR-iPjdGNR25QO6UhOzFNHWtan-ipK-iOS0NpDFdjMzzhRJI2-qRV8sxXgtDphug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
معاون حقوقی وزارت خارجه: آمریکا نمی‌تواند با خروج از شورای حقوق بشر از جنایت خود در میناب و لامرد فرار کند.
@Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/462780" target="_blank">📅 13:21 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462779">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94906501b5.mp4?token=J7A5YGDAUACVmYKtWKUtfghLaoCbBNG5LoNO0q_iBU62X4xC1VKj-MRvBY1NVWQxmhcsd-z4HnELmWjO8fujAPOti3nTSgnIQMd4hpHX7d7fMDujF92o2_eLUofhCJg3r8XYv3WLTIACboli0d98LBjUwxU3tix7kmHcJhzkeT6IQX2tyxP5mL7dL0WHvrH3JiZqsYa8qFNjXCk-i2ramqGa4aztqC33oGlg_vlFMaHqEwDzGzctit3VO7tdEAZwxUgIXpDRzfMDFJs5Lid8K3TELT_XlAoa_JeECRc50INPk9oeh2MXprDQXLz8lGbZFgsnEtH7YQYDheLIagavww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94906501b5.mp4?token=J7A5YGDAUACVmYKtWKUtfghLaoCbBNG5LoNO0q_iBU62X4xC1VKj-MRvBY1NVWQxmhcsd-z4HnELmWjO8fujAPOti3nTSgnIQMd4hpHX7d7fMDujF92o2_eLUofhCJg3r8XYv3WLTIACboli0d98LBjUwxU3tix7kmHcJhzkeT6IQX2tyxP5mL7dL0WHvrH3JiZqsYa8qFNjXCk-i2ramqGa4aztqC33oGlg_vlFMaHqEwDzGzctit3VO7tdEAZwxUgIXpDRzfMDFJs5Lid8K3TELT_XlAoa_JeECRc50INPk9oeh2MXprDQXLz8lGbZFgsnEtH7YQYDheLIagavww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کلبه چوبی، پوشش قاچاق ۸۳ کیلویی مواد مخدر شد
🔹
ماموران گمرک مرزی پس‌از مشکوک‌شدن به یک محمولۀ کلبۀ چوبی که درحال عبور از مرز ایران به‌سمت ترکیه بود، آن را توقیف کردند.
ماموران با بازرسی این کلبۀ چوبی موفق به ضبط ۸۳ کیلوگرم مواد مخدر شامل تعداد ۱۶۴ بسته انواع ماده مخدر گل و حشیش شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/462779" target="_blank">📅 13:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462778">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bttvwbcaE6kwPLbcD7fZyD-5uIKMEmL4-BLnEvYGdq90X7BgCmAcs6EeyyrahY6AyeqdQ2aewQmmIl_8uyG5DIfqFJWY3vO7Sktu6QeIVwMq5mCVRNEO1qe9oGj813nQieYp2Ov9ZxTvm3PJxonqiuBKhPKxAqlG8pG3yEWG5eKdYnakH5kC8M7baU7pBuYKsLn1BZjJgMTs-lNDxYrnhvkzEEwqPfEOqLtnFN_5QfpPPBoGDrsZICmhvnAJDYyuxSMZtDKOr61qTO8_FFODeR3OrmqayUkSWB9io0zqspiIPTRksHDYxvE3OSzxYxvXauXyu2QgAW4DYzkG7Ec6Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان از ترس یمن دست به دامن چین و ایران شد
🔹
مطابق گزارش رویترز، عربستانی‌ها پس‌از ناامیدی از  کمک آمریکا برای مقابله با پیشروی نیروهای انصارالله در یمن، حالا دست به دامن چین و ایران شده‌اند.
🔹
رویترز نوشته عربستان سعودی از چین خواسته از مقامات ایرانی بخواهد که تهران از نفوذ خود برای کاستن از شدت حملات و پیشروی نیروهای یمنی استفاده کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/462778" target="_blank">📅 12:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462777">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fsw34JQx5NDHLc1326m8kkaAK7XnOLPLBmxTlJdtaRlh3xSWO078Knzzxpdj45a5NEV8ZglH67VK-jyrUGy0gOzY6WgddXukmwEwWfh9YDdFmw961k2AejcncQDRfpqovVhJe9dSktUaz38DBIUzL2POMx38-acZz2b_q8fDduDXIZnGwtqdxMTQfp56Ka1dUY-qgqO7KygDr5TCFFtFvjHjsy8QLosMdE5cvlAM02IfMUbAPpaY93VgK_Q80EmF8k1qGdLD9NzFgIpnv7FpfjffukSd8QQK8gRlNi_cFjOfRDo6PSazCvFmXVUYVkp5b0d1YZ3sIDbR06Po9lW3-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسکتبال ایران با پیروزی مقابل بحرین به نیمه‌نهایی بازی‌های آسیایی ناگویا صعود کرد
🏀
ایران ۷۹ - ۷۴ بحرین @Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/462777" target="_blank">📅 12:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462776">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd3063f18.mp4?token=JMnE6HW-qEs1L-JmVj2rG2Zq_zGpIHuPrKXE9JpFGEvdUbiIW9SJFEN-E2kvg-uJDyeHHGK-phHX1dWBfPcSWZwQh7RIa35fSvt71zOLbtm2-38eEdrUcj7H7NrFRr0-0-oItsHHDoINjlO-W1hQxMUprkb_Gal90PRvpdQfsfqVVQAtaKz6UCgINYmk1Hytf09wvzL1qHoPcCIfqw-IVGf0TEjGE818GsgVI8WzT54QaSStBDOXNOPDBZyv5EzNeFGt3MpXblDAPRSDXZgtyIYR5WeXGMMCXTPM1Xr7E4F_QvaiTim3A5JM67aOnYZ4AoF-N3hiN_DG7k_GAc8Yig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd3063f18.mp4?token=JMnE6HW-qEs1L-JmVj2rG2Zq_zGpIHuPrKXE9JpFGEvdUbiIW9SJFEN-E2kvg-uJDyeHHGK-phHX1dWBfPcSWZwQh7RIa35fSvt71zOLbtm2-38eEdrUcj7H7NrFRr0-0-oItsHHDoINjlO-W1hQxMUprkb_Gal90PRvpdQfsfqVVQAtaKz6UCgINYmk1Hytf09wvzL1qHoPcCIfqw-IVGf0TEjGE818GsgVI8WzT54QaSStBDOXNOPDBZyv5EzNeFGt3MpXblDAPRSDXZgtyIYR5WeXGMMCXTPM1Xr7E4F_QvaiTim3A5JM67aOnYZ4AoF-N3hiN_DG7k_GAc8Yig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رژه داش‌مشتی‌های جان‌فدای ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/462776" target="_blank">📅 12:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462775">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c114b1bd47.mp4?token=Gs4K7LNvr4S4n3eniriwXOQd7TY88Gp6mgZAGSw_bxsgizE3DByppLZU3ZWW7Be6Ds6WBza6KKpHCLlt-DTSfKiuePuIq9_smTU_tSL__QzHsZDNBPdNFH8WhY-nYW8CfDEHGuqd8YH0d_7zhzowD4hvwLvaBHFeln7ZZjraanzduDto_Fz7BMbgU2wEXcNlnKnBDq6C9UEIFT_lEb5EbsmVawTH0Ee_7iYRDSEMGsQumqwJOPNrZ-2KL49yHXUuLuccjSGBaqb78WyBY9UDU5pKx4cqjWwHQXFoz4NLEc4mC47ySVJ8maNfHThoQB6Y3TFRJhvP77944zZB4cTq0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c114b1bd47.mp4?token=Gs4K7LNvr4S4n3eniriwXOQd7TY88Gp6mgZAGSw_bxsgizE3DByppLZU3ZWW7Be6Ds6WBza6KKpHCLlt-DTSfKiuePuIq9_smTU_tSL__QzHsZDNBPdNFH8WhY-nYW8CfDEHGuqd8YH0d_7zhzowD4hvwLvaBHFeln7ZZjraanzduDto_Fz7BMbgU2wEXcNlnKnBDq6C9UEIFT_lEb5EbsmVawTH0Ee_7iYRDSEMGsQumqwJOPNrZ-2KL49yHXUuLuccjSGBaqb78WyBY9UDU5pKx4cqjWwHQXFoz4NLEc4mC47ySVJ8maNfHThoQB6Y3TFRJhvP77944zZB4cTq0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش تماشایی جان‌فدایان ایران در پایتخت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/462775" target="_blank">📅 11:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462774">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d73d5f49b2.mp4?token=XbRAd17o08JlXaDWv5KuBGRWlcoiir3ufbEGsrbsEgSzRCN9bOcuJI6LE4hfpfPUS8LC8mAPmmEAUvXTiQRUx_ghnOmcLsGKJbd1FX6_v1rVkwDpwVIcrF78yDrhAyKCbhsD_cKcJ0J0RgEb8IfuTA9NlvT4e8dxLi0WsFxPEe9nd2dDAY4AyKMJVfa-9YEDD9UtysD9FDHQvHoTnO2PRoIXeqUYFd_bMRKylVurSS8lxA-WQZ5ctnjPEsawui-nXqb_P16rn5M1cdNXE4wYC9w67M6p1hALX0BXXQLaRwCc1ndymKAPnljQLJZaa8dk2Nfl9fMwtz7HTfLjkiX1iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d73d5f49b2.mp4?token=XbRAd17o08JlXaDWv5KuBGRWlcoiir3ufbEGsrbsEgSzRCN9bOcuJI6LE4hfpfPUS8LC8mAPmmEAUvXTiQRUx_ghnOmcLsGKJbd1FX6_v1rVkwDpwVIcrF78yDrhAyKCbhsD_cKcJ0J0RgEb8IfuTA9NlvT4e8dxLi0WsFxPEe9nd2dDAY4AyKMJVfa-9YEDD9UtysD9FDHQvHoTnO2PRoIXeqUYFd_bMRKylVurSS8lxA-WQZ5ctnjPEsawui-nXqb_P16rn5M1cdNXE4wYC9w67M6p1hALX0BXXQLaRwCc1ndymKAPnljQLJZaa8dk2Nfl9fMwtz7HTfLjkiX1iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداداد عزیزی ۴ ماه و عالیشاه ۴ جلسه محروم شد
⚽️
کمیتۀ انضباطی فدراسیون آرای مربوط به حواشی دیدار تراکتور-گل‌کهر را به شرح زیر اعلام کرد:
🔹
خداداد عزیزی ۴ ماه محرومیت از ورود به ورزشگاه‌ها و ۲ میلیارد تومان جریمه
🔹
امید عالیشاه ۴ جلسه محرومیت از مسابقات و ۵۰۰…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/462774" target="_blank">📅 11:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462766">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDb_ilFJ_UJFfpOnVB7hkbBCC-VWrrnma3ejQELEDBSTgWHSRaW5lv0UKjbIOldjpNbi7CynLwwjqDClySvu8HVsP55OhJqy-nfrfvKvXJIPiOkCSDOMf_V4T3TpNNEmLU--TJ1rKyewvpORFLKrPSXF3Rw7W6S9j8B77egGAw24glJ9zIde4-nT9aszbUIBuPDaEw53bwaJV0TFO4hp-L6dK3Krm73Yg0yhKjLkc6BMu2_bh_vMQwfLAl9oCBtlQc7WZEroBBd_5WEWb6GLulPfQE1Jn85PVTxBtN8JVhcZKFBuQbfzFW0cQ0dD8yVT0cBDtVsKXXMqJTYda0j2sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hg-Oc0T0_MVX0qz6FccpYMbzovEhr4XD5kuQLbpIsvFrmD0V2KM8jVkxhp2MoG7Nfc_6DC5mV42aOD20XmBt4uR1ohJGg4H2ccQjMGAr0OOzsxb66sVg142d6uGr67FbHGNhn1Wv8f8tby6jhwMKbq3fafM_7spg3v6CO1QOg1UgINioyM97evkEQXw3GHLinv44JM5xDQlMS2rs1PjRJwLTUtOzBxvUq-f03sN7Wum5FpT7E7ua824iL2VyRCi1ExyOR6gOs0lYsi_Wl7MahMxTxgGxkTVqJK1QoyCjHJrEP-G1DqAr_ELUsgBmkKvkmpxNAEBl1P-ceVNamufYxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lFOCLJWvBlkldq-iyNCgHPQenB0y8Cpr31ToAi9AVYfLHGi01XB41TdAiQRrRwaKA44PsEBTw_HRU_6xTpUMXtt1OKNpFWq0c90Zw2eeR-7d-F6ROCCi3d737iFlMRUoJ8KFNWm-LSi9-0rDcfU3p_k4_wtHjgp_UKOZrALyqVs1MjhSLMmuMPotKY_dEnhPgFTya4kBo4gqe2izln7m5rl-xf5A2qZCOigKPoDTz6yGJr_v3ce4wtvpbMXtS5iQ5nZcvm8H_XQ2Sj1-KEG3NvRW1n-OsIJj4LS_H0TegXhgY6GAuf4qjLVEH1wRA-rJPbLN3YUgK252FFIceUzaow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4n5FL4R456jXlUXHVtMgCsEtVi6kDaoKYp-Mi-zVys0hjgEjtpZabiMBgSO3Gh359o2vsyQjZUmCaIHKAEgG8QibObI_cLDrJgDObBG9kf3cnONRc0ItNEe92Z0dqWVYWP7yCVq8Wtj1xArnZmf-cRhlRSeohogcV1Qd_ILpcXS2cWbSdiRLnLamYWgEah_mgNeJsXr03ZWrX6_pkhNW2XCYLq9J-dizs8d7M97jOwzDDaqh2dlf8OokATZcqLOE3mWhSV1c4PJaMs-sMxqhpg35dbZK8uAP-okO4BU_6fVzfp3v7hvJafk1AzRsp70vt2bMNdOdyTFnOaa_2Jvuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rNh7z3-bj9MNyXwbUmFLwMsxypBo9OrXsJDzHsAbjj2SKORf5c9dnWDQmo70I6uP2QQ0sVnyxw7ESvoVlU9wqMQsl5k20f4gI-WEwydEfWMhugEnYVhAxmwAZ6ungYIhy-FgNIhzEd2SPl7WJRsUp1cutkXsbrdEOcfGXXOD2-wR6RRZx29GBTV7orNiciO1oXRgpGy5Y3ShHlZmKwB6RHHebHv0ifZuLHs5_agRGVqTF4hONR7w03yCWrSQy36X0Dic5EFVQ6D42yerUwnjGxrUKYr0gX7OkBNF-V1UTjBkktAdjya3B6LK4p0PMxeqikxvv0c4vu_ODWMBf7KuJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2bMtsGQ_qYS3_z1LJu4unnTz7CSp7cK8_qj_eBg3oOSMpHYb6i0ek-kPI_UYUmk8WtBVt2IyWLkRBHZQNXcaKFkhX_zwijdod02-PiJfGudLRf5wC6Ri6K_4E8-aIuNzojmmv6sWdzI2Xqnfny9ogi6_ZjoYEtLOnfOs7IQmNb5i3R2ByY1lm4wG8Qgeay2M_pSOBOH6v9OZ_fPaEeZF6ROVSF9OdqixiqdGw76H1k4Tlk9Wc2BjolUI3iM1RFIp9Mu18m_qVSyIZ6Jw_GA7IfLUEr4_c9q21DZr1JWRPx6CXRXBHPXifANhyndMP0qA0LkguzsN_IY6mrS9e8mVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAVedQrs1YlafVkumVVYpMVqO5HTwYlzxdYODIvwKtdD01bl-PkQGSBdiUSnvii7mJvnbuEqQBscVGraf5YKz0wZWPNPM_BBRqJXbGcg_3FcF6dThfrUN81ezUqTEQ2G-4E2BgKMDKhH7qwDzjEaAaoZBL0EFVdtxXRLn_KF_0kKjHPvfxswi2hd9skCiXgpHGtuagPto4o8HsqkOJOmy20sPYkZyar1jFVSEhWHdZuWxBf-sP3fx7yisyFwv6FPR2bk3odGfzoKB5hL0bk4dRzGZVV9JiDyspf5wjruyntw_YUgJszGNYExVHBHwpbWXdPsyHYZrln_JJZfCMr91w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bDlAtD7RWbQZzdW_h1fZU_E7vsDyJVFnyn0RS12oB-aQSkAd5bvkns08UP0b8M9SsBiogxooyxj2zOErQTinKgk9qEuXhG-2jhLGT0uUwHSU0r-2UnftuU2vh9vKE_nKvg8ja9TGipCeoea3e0XmUCJg4BPR3SBM1El98RcfxU1s95PWVw27AJZ32V86K-peIfEhhpc5PiOYo3yAyHfbGJ9eThHK_sAAHP_Y2sjIk45ObiydJihpvwtD3qy0dgQWAcni9x2MWoddbKjBcGFedIGeEwJEkjYWit2nOUCp_2teJCpQFu2VQzZ7PZpgKc8pvbidT-Chc1IBSj6kVL8yVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
۳۱۳ هزار جان‌فدا در قلب تهران
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/462766" target="_blank">📅 11:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462765">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbjR5I7rw35SEeQ7bVpkZhmCLunjC-x2nmZLIHrcuzVFAHjSPlWljmbTrqOjmY85onVjyA819pZXVrm1e534EkdXG6uzCU78tBwgCOgM4xvbMROIx2MEkWW8oU2aQz5UBeABXYqZcSB43IZbO0S5sAhR55xYYojXz5n81zMP3jIQpAwJ4Mnff-rFzlbcD94g6-oBsYEFM4tAV4zY4JV6un7Ka8Jh97Qugsi-f3oX5FFpKsdFEofmVoytvLFvDV9D94y_ysuqdPcWf1ulUHddw20mgrMO7biNaS-45iI4xfCItWF23MLG0oXdcWBlvixUW1QnmPhbtdlANBBkONo2gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اصابت پرتابه به یک نفتکش در تنگه هرمز
🔹
سازمان عملیات دریایی انگلیس: امروز یک شناور دیگر در آب‌های تنگه هرمز، مورد اصابت یک پرتابه نامشخص قرار گرفته و در آتش می‌سوزد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/462765" target="_blank">📅 11:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462764">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d896b9322e.mp4?token=n4GWvEN4Go6lp1W_3KJoY4X5CSpaYeHEGc_DF0bcJ5uP8IJFgwzvygKuB0cbLS3StORB5MHaA0VDsCTh6xIsjvgTSP33q_QHpyqMoAFgH6qwMwQ1lEFwNxznNdFJH7N3EWF9pplGTjiPzD2EH6zaKPj50HfEefNOZf3QfQxCvkkD5iI9qC2go0Ota50qTFbZ5oSIAV5vzkFn2JKe2HAdJUpEXQW77mAshWqObsweRmU_6X87GjuQJH8AbARhs0Q3NuzK0gsUWlEclJl-JCpKt6PT09bjstT7fI45_IPEzP6-MX5T85CD8IFwk8ZMbAQrMKiUOUdzZnrgBCpq_44eGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d896b9322e.mp4?token=n4GWvEN4Go6lp1W_3KJoY4X5CSpaYeHEGc_DF0bcJ5uP8IJFgwzvygKuB0cbLS3StORB5MHaA0VDsCTh6xIsjvgTSP33q_QHpyqMoAFgH6qwMwQ1lEFwNxznNdFJH7N3EWF9pplGTjiPzD2EH6zaKPj50HfEefNOZf3QfQxCvkkD5iI9qC2go0Ota50qTFbZ5oSIAV5vzkFn2JKe2HAdJUpEXQW77mAshWqObsweRmU_6X87GjuQJH8AbARhs0Q3NuzK0gsUWlEclJl-JCpKt6PT09bjstT7fI45_IPEzP6-MX5T85CD8IFwk8ZMbAQrMKiUOUdzZnrgBCpq_44eGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دانشجویان علوم‌پزشکی با عکس‌های هم‌کلاسی‌های شهیدشان در رزمایش جان‌فدا حاضر شدند
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/462764" target="_blank">📅 10:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462763">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKNFRHZfuhIHwgSnEhHdpjnBuqN7YkXLI7y0dbcbPM8aCm_RFCRKUkVo6GZEsD7nzZvDnTzSZo6Q_woKxqjc1h2KSDvIr0ExAV4y5BPf1JtDlDz2TzKPZgDTBm2SOR2h0-023qjAnsb1dcCHVEsVeBaWzqEMoviRmOWvarr3CnPg86YhFCfpPbibq2Dawur15Sb4cVrS1V0aKgNx-dXw6DXOV93Vbf6Jf1TLrV2-SDU1nxeQZL2aAH2udbUF2bM_tP-l0m66Pbbx_P4YAKYYyEW_GaDLqMylGa4g0bPiw8RjLW_sh2r31AQpq2278WZrQlxZLJj0ff_D4lU0KI6EAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
هلاکت ۲ تروریست در درگیری مسلحانه در زاهدان
🔹
بامداد امروز نیرو‌های قرارگاه قدس نیروی زمینی سپاه حین گشت‌زنی در محدوده خیابان دانشگاه زاهدان، به یک دستگاه خودروی سواری مشکوک و با آنها درگیر شدند.
🔹
در جریان این درگیری ۲ نفر از تروریست‌های مسلح کشته شدند و یک نفر از آن‌ها دستگیر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/462763" target="_blank">📅 10:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462762">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df7c004397.mp4?token=VDvB2aZXRokrUDqS0yGaPCnVFNpX25FW8iBbwxqlO0OrHd9zoAdseo-JjD6shm4p__qg_acrr9fk9r0NraUz919xAvJZpuXeYE9JOyCYzNAqkpqFBnVrHXcbos0IGFksd5yBzWYshXgf-f5lHMKbjbvWMrwzox_vyaadlXUjEsI_yJZ7BiC1eCCMaXpoW2gqGr7-DZFQra-yKKTNTTUfuqejMc56Rk2upOfqP3369K3GrGbCbX_PTe7ECKsW0NZBS67uZQNKF_C244yIcwP7uyI1K_HbcsAXpuAZggLIDc1ON2LJ1nTkUHijKJR01AePLvt5vMXQ1LiYmBNKG873UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df7c004397.mp4?token=VDvB2aZXRokrUDqS0yGaPCnVFNpX25FW8iBbwxqlO0OrHd9zoAdseo-JjD6shm4p__qg_acrr9fk9r0NraUz919xAvJZpuXeYE9JOyCYzNAqkpqFBnVrHXcbos0IGFksd5yBzWYshXgf-f5lHMKbjbvWMrwzox_vyaadlXUjEsI_yJZ7BiC1eCCMaXpoW2gqGr7-DZFQra-yKKTNTTUfuqejMc56Rk2upOfqP3369K3GrGbCbX_PTe7ECKsW0NZBS67uZQNKF_C244yIcwP7uyI1K_HbcsAXpuAZggLIDc1ON2LJ1nTkUHijKJR01AePLvt5vMXQ1LiYmBNKG873UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انبوه حضور مردم در رزمایش جان‌فدایان میهن
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/462762" target="_blank">📅 10:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462760">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad65eba82.mov?token=dgiJHZxp78G-JbeqpodNI2PcVO-SafCp8cFYbavvxEJsy7nF9MVNWeNjFRRXyU3WYtFXopCXhnDosYuqyqHEg-ZdpTtU04g33nDFVLmZvTKWbVdvGWCfKkyZJVG80kHtiigSYHvs8IOMe_nvoczWEipBSogdPuenWqiXyMO_JMEdhsFg1rKm7t_knv2UynhJIsZyBZqAbwkADMDAd_1SPJiFE0Zh3WgteuMVLdC7ZkuaoX0OQHIdC37_UCEmDD1T9bCgdUh2Y4OgQ-A3pztT3oYh1AmKgjUP0Iy_Katb1gnecZRf_fgN4UbIGtsaCKtm8qYia85OPLlvw9LX9S1EiDE2jAT1AmaXiwtaGtWKaJdMPrvTXXirA2dMreF4YYZb-ng6RPaNY7RWZICoRvhsfcEfJgVCloSFpkZBSE14wERc9zHOvYfOOsZpo-kEE_NWk6DcpqMEac_z01AIETb8f8O3mIKd9dZVXkMuDRTnYU_zhtBoaOXRXbvq-TFeXipIm6YwBZPs2mLaHfeWbSeU0mDFPZ9Ols0XTTwwdYxop1bRi-anJF02M2hOfcBInIwZrsd01IoqlUHC1Oc5J0x1qnYR0yId9IK7OdOrJtg1dIjDtOEQDh2T5H2_KQKZvCbt6ejIuvSrAhqiZbn-Y0cpbGBcOxYhrLF028HkidHAp08" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad65eba82.mov?token=dgiJHZxp78G-JbeqpodNI2PcVO-SafCp8cFYbavvxEJsy7nF9MVNWeNjFRRXyU3WYtFXopCXhnDosYuqyqHEg-ZdpTtU04g33nDFVLmZvTKWbVdvGWCfKkyZJVG80kHtiigSYHvs8IOMe_nvoczWEipBSogdPuenWqiXyMO_JMEdhsFg1rKm7t_knv2UynhJIsZyBZqAbwkADMDAd_1SPJiFE0Zh3WgteuMVLdC7ZkuaoX0OQHIdC37_UCEmDD1T9bCgdUh2Y4OgQ-A3pztT3oYh1AmKgjUP0Iy_Katb1gnecZRf_fgN4UbIGtsaCKtm8qYia85OPLlvw9LX9S1EiDE2jAT1AmaXiwtaGtWKaJdMPrvTXXirA2dMreF4YYZb-ng6RPaNY7RWZICoRvhsfcEfJgVCloSFpkZBSE14wERc9zHOvYfOOsZpo-kEE_NWk6DcpqMEac_z01AIETb8f8O3mIKd9dZVXkMuDRTnYU_zhtBoaOXRXbvq-TFeXipIm6YwBZPs2mLaHfeWbSeU0mDFPZ9Ols0XTTwwdYxop1bRi-anJF02M2hOfcBInIwZrsd01IoqlUHC1Oc5J0x1qnYR0yId9IK7OdOrJtg1dIjDtOEQDh2T5H2_KQKZvCbt6ejIuvSrAhqiZbn-Y0cpbGBcOxYhrLF028HkidHAp08" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور رئیس‌جمهور در رژۀ جان‌فدایان ایران
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/462760" target="_blank">📅 10:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462759">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af0b0c9915.mp4?token=rGYvBCEx3NGFfoODpOBKNAbzsHV-ZOHhH8Iz0-DrGsFi069DnFUncJ1NR4G1IM-8VQRQbR8mIXpQGCqOc9hN4vtxugXjmXZkv851DU43U6DZy7dfKqH5wZnOnYARFPpB2ymN5KpDlCymljsUZc_vjGMTfw9a2xZboCq4VQ7308ZRZ9X9Y82EnQMvmv-TMWPs4B-hodHTn8b-Taf3qnWGG0vEIJxazLhnX1ShdFe7JfkLaq7HdWiIW-xJjz1BayvYayPVxwhIkfEST6Jh1dJKvL_N_X20Qo_2kJ3_yw5Yo26X6F47AvLU2dfnfIOMzjHjWk6Eh0Z0CHA7ykwoi58s0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af0b0c9915.mp4?token=rGYvBCEx3NGFfoODpOBKNAbzsHV-ZOHhH8Iz0-DrGsFi069DnFUncJ1NR4G1IM-8VQRQbR8mIXpQGCqOc9hN4vtxugXjmXZkv851DU43U6DZy7dfKqH5wZnOnYARFPpB2ymN5KpDlCymljsUZc_vjGMTfw9a2xZboCq4VQ7308ZRZ9X9Y82EnQMvmv-TMWPs4B-hodHTn8b-Taf3qnWGG0vEIJxazLhnX1ShdFe7JfkLaq7HdWiIW-xJjz1BayvYayPVxwhIkfEST6Jh1dJKvL_N_X20Qo_2kJ3_yw5Yo26X6F47AvLU2dfnfIOMzjHjWk6Eh0Z0CHA7ykwoi58s0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ای لشکر صاحب‌زمان(عج) آماده‌ باش
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/462759" target="_blank">📅 09:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462752">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/adwx7rfTpIpzAL6jj91sU9a0CxcdflX4IBpnh3V2ayX87412_kQ7xzB4F3Kwh5qfEei8-UdnGh4UhAUqpI3I12gkCi4MmPl4omL7_9fs7utz7r9GnwUEYKOc6UIvaKz30PV2ABTi27vSTe_-mBUyJb2a4S97tlUe1Fcd4_I_EutwBLO28ayPZT6zlTRVcmpyLejPg1P5YJDXEc2Gz_2xc3AtVvkIizyVpVA12uFeQO--Z9fKguhi3LT2mfm-ZbTP_40z2jbdh5k1931i1A97KwBThVBSMtG5_Sxlpg-7ppQAzLpQegJRcXis5ukPJjS0Y7yTKnE2-Ih0padBrs9Acw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/chGjv6YWFaHXS_zhXC8xom9jCy7hTAqLoR3J9ejqPklzR1YA1BmAAl8DfWBS9OnV5UmsdQ9KhxAQ1chvbZdqoyEzJMiZRLE-IEyeYNGivZhSxiUCQgZKAxT4M1RhEhCymaLroXB8xZVWb2xryrjzOaBA95dISgqoymk-tHtoHJDTcrc2MSPqPAOAy1wXyptecVj9yP6kcc8nRH7DGtwExMqxgEUYH0ua1UkFZfrvJJJpEixCbWc6pWNlfdpPGz_xdQXEvC-xqu-Y3LsAq1FsvRrC9e6Ufxh-6LJlIVNjBKRasrj75LyL4sJdgQZAzuqDLLmlAqVwUSLptRVliORHEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SaqAHNwlHt4o1nGUR3kQYsYKhuJRM-TiC_OkZvi08w4C3YSeB4JQMMYzSVwOdNAf_tzK4AZnkkbPc_x85dOmMtuqTtM1rMbjTXei5d2rr0byQi2LMl9kXAwk6NkL91mTlycMsFV8GR6bUP5rynnjfECPNo9Yil3p6kAHntjuWCMxcNiJo4QroDTFkhsMA6gFUO5_e0WiYC3oGZGuhba9Lw0Y_99L7foy27W5xXWLlESmYI8lA4MX0VgZRxbmxdd90_cujrI86a-I6S_ImQF2IciLgdxF3sOXkzX96MjNuk5Mc1g1KCjzMw7zPbaNlgGJKdDCg3r0N7BVjl-ifaEk-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fDF5lBYm1yYbOiDOefOFgNwJPFeGruUwV4-gFGn8SvraMegQNFLqPY_KWBdPMc9gUEm4hrAf6ECJDjsu_bNOuxoGFUTowCP0buR0zNp2pAaz3Uz8b3nnqr_Wi8ddRQmhSmoElQuzu-WB7jELJfSHdNdOKvZFvckPSH5oHWm7Qq7R0zRX9aKzdO6fttKP6QzngvQh7HUqR6ZbWD-07XsIkB1jJXvtNz9gEPOY3xrm0kFmSob55zpvtBbU3wSlQ8BnVDknQzS7t6J67FmKkilGFkPeZMYoSrUXulsn8VHNcmIZw_nB4CvW7oQrkx4etQnDXhu6TcDnssUFTlOcUDp_sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZ71W60lEVylzBGeJ3zZg_LWvSsUcfhax-5CPJbRUmzngjDQsxUgAEVNFOqKLBNRUwYbORG-xnszuaYCaMpDomLW84Ga_XmA20ceT_Mnllmi6CVIn0GmkdI-_2O2HMRQJCBef0USD9PB2BeQxGNzvWjIL-BSmc3L7uZOfCMT5P3gJG46g7dyjcAmD2sNmUfVa10ApTR_oLg7Ig1US3hKi5HlRe0ho4Ea7WsEzMhbaANq5KY0I7AyYkC-xsYCqO_sfu2-_APk6PCL_-sbhtiGX8lBM-a8fPyZ5FN7AGN3hAajV3TbPkbwrNLShLpogbHCeyLrx484_bV4OdDOSl6o5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PXVKlgVgqxvQ0WY8u5-N_1EKaOlQRPZNiAulpkF0l8OdFHFiH_tlETBcyqmWKgLFb_m_xY1TVXkVGN7S_oWxprkRhkTBq0cfJfeM-h1VMFMn3mWt8a6HpZ6dSygW0Hanls1tabDVZBDs-Go-oEHSJYglJE-dwjlK7iIvmvwwb4Zx3yrpI5exILUaJ-5VxAQi9W_uAzLlV_w9L06WF6YS1W4jZiZHUHFnvH4YuS6g8pD-I779ajv-fpNtxVhYH2qqutqxXJ7PJ2YkqDVn5YM07_Ck4TvRnNvevM7QgPF-fQIFQEz2-2-Mp9dlOVy2EyusS2H4CK535ez9Q_VxnwNKZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCCMZW616vhmx94574kEQALYFrLXyNiRnOeCLCIZxvhocxleLlBcKhGL51vqG4Qtg-A2EQAfnrZvkjgKSPJzIhVQuToUIh243QeTkszNsQ8qdMMeMF5WMdTZ2M37gWVYITngccXMu5NdtT3oZOlj7rLft_TmuFNU5VCiNw28Fp-u4O7D-qDWzyqmuIkw8a1Ddp2iCQQyBV416mkyE8ZCLzGWemqNwvww2diHuuFYc9C8_54x_nyfutolG6bZm3GK1QJfhOmc8Y0KBPKfyDO002iiMvDRkZHp_e8RrNdAYL6aFBfHLbGvsDt5XQal6b6QmFnCjenLAKWjsz1g_3uwlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جان‌فدایان بی‌شمار ایران امروز لرزه بر تن دشمن انداختند
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/462752" target="_blank">📅 09:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462751">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJpO6ev-iWI3mzkobXexB8mDUgkgnB5UrA_arDvLfq6-frr_bxY1SWFwPa2DpXWnJ7IwAGZpLhyABN8z0kqcICC1kpH-tZuLJaZvqDAO3WDb78hIou8qNn0BWLxEcoj3YTJEft_sGvr7g8Z9b1nyO_Vhjzg3mQTKQ13tEjseXsHJW5fHFuV_oVDf9c_N4WyWXnDaZTIr4V6LBmoKCK9CYB7vDjvDW-DhamhGp9USdekmI-9f0X2u6gjyORte_OdKPJZ3QQpkrCy1Nq3SiOAFUMSaT4dNTDn1Bh-wovA1iY60jok8VCNMnQ2YxzWaPCkMVpbF02f_lzPN9SHOW9UNVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/462751" target="_blank">📅 09:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462744">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pXTquW4UX5j3G7YOat8VcR-bTgRiOlhrUbHlmFf64-_x4fyW_omYVgD-Vio3A-c3Ysk-EYvBibqERD9r95792_Ac6W79cHB0nCN7Nfv-fKdt-l9WEV4QZXm6p79TBEOEzjhJ8CBaYIecVAaVVmtqoLD-iW_fJScZWaVtfTI9LoeH_lH6fMuLcgvKMWW8p_HCNNteSxGGZcEyhnaYrFKHETS4OoP_WMDFOuc_eXrXLuxev-wJrD_Rf4-yCvnh0s-yi7kzozUIwkBPl52f9SjJC-0YCogFjDhECr_fqayX8lw3nn-dg4tygocdq76-zUWRrUH7lLjnLQpqhYjUzYjYEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZjOM3bpGnPkgIQi8RspIZbWHHPUJwC2E594J31WyEzV3j2EjuEN0wnzInQyI5uouvL3Dfgch1Ebm7wEfyP2mLIF6kIVY_qfQ6azKAltX3oiEqMV4joK-e_CanGDZuI6g6tCbH3da0C9hS1DYq8jF_s5EdJwbDQ8G9Uvfeqb1Ua2mIrl_wj8qCIP3Z63qNN58nrKROXqN3jbggnw0Vw_rerV3Oli1XS_J7Dz0y_tbC3yof-xGsL5qvjTu1Sc-FRcO1YiaUo0yBipLTnUuy16RK64h0mkPB-VPkGhZx15pAs1MIuZ81lc2oe_JAXUwxxo3Td_N7JzREigC_Ny7ggNddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kAJOdqME4wTaYl4q30WKiJz6OcLF5KDPUYsNVd_D6qGnBWuF2btgBj8P6BrYwOOW02W7Vq4bI8rw7MeVQlQtTsHfabSKpte99uRWaV_TXX30U5B_PXXFyUZ2J2LULCZG78o3O5A8FBP5HtGEFi9IiBC2Ubyho8r0gvzCqNh-1ZwiSRz0D8YvldqJdnm73izJTpRy_NF8f5lqLYuj2hNqYha5POxwyg31xRbeuDK7qbjXHnzAHDUI6xmIM9VroBxa2z3jbx9rSPZ-Kaxw1O8xblAl-SPX0j3oBEyaj1FQn8uC7xcnx_XSlvXFdDRgtz1RURYAdjNObub7imc735wpLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hnDgYnMAchdmsEIRwwXV0LiAEWpuNbpxABSE0m2sh6BBD0A-bzReCPdTF-ZOqLwo57gWg2CEOKp_rNNzW7ugfFRSp4M4_JdSWkWJfkeG6ejweyEbDh8OPtTqFUYwdyPCkEXhUH7wLqAinfylhfcEP6GuBLkSYSJ3XPSywV_u0qOD6UYX4_50qB43mO776ZLn8wpEzyabhSrfxPs19HuX7b8kUU-7zDib3gFQSUPflHp_VWUuU0ruocbrs4zV7oQxKtWvdJRJJtCnrtV_K6Wff4w6I9B76gUEg5yuFbYv-UY5YD3RrECQr22OYwQCv9QlbXZ8jy2XiYjCy4mMIdyrMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Af0MNDgYJSS4KxcaOPFGkyp0KBvOLZWdYb_UjQFFXvqsx3VKpFtr8U8pX0QLQhf6IuN1JEcFECw30nnqXErj8fZyRnGilqR27mNDK3VeozJAyE87fpNuaEbCrJu9jw5ifBEuR7F8T5ZJllmlF9sy8xMPq_KupsUx5T1VSIg7j9SG8Oe42dROBPBsutX2zVgUyAQVIBruAqSRP-pWjlMRufm1oJM6I-JLCV5rQMilMMeRktgmOLpNZ8kxF8Nk8oXxjTyKp4E0j1Q8U-zxvjUJXGcfr-01DBSiZPPAR5BkSAnQpZrByiv6IzM04BFr75WQ90doljLzBL3-1N-u1Bq_CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LXIayvGqTYRkXkMX-73WPKQxV5UIW28GgrIRdHF9qg9HErvwAtrbfXWBceyKKvE1PBYJORRjk7p52x2JNcMFfcmSVKrJaLB5hhIqiRZTW4oCAWBVLMPcLlki_j8Uen-Ph3tb7cSwAVvcX7vT8nzpCseZCfRUnAsa1OrJYKbDcOib_DnstnPKcAerJucZ3Wwtj1FF53_ERp1ZXKV-7Ro3RhlWvsn7NBo2pinod6Kd-0tGCbZxbKrxWdF_Rhl_updyQ0oVO9GEMhwvHfC3XARldgaWoI2On-TIpu3U4NZGFtwHWkE0G6bxjhPNy6_XXwpJTirnIbBEMhkw9SPJD4fkZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YlGdVzvdyVl8hmhJOKG1J5mLnf1HslTxK2X6G_EDiaObkuHHtnr8BFg3tsJZ_1zhw01gDO8u3V94nY_h0pgcWMIaqRjjz_pptM2dct8ucx9YsSnL3rqp7ssTELNKSuy9_SGJBEul5VSJaHEmyiuHhlMpu67goXQhnPNFjsldjYoc_9OjYxW_oOoNRjT-tjPQiqTcU6HVLOGhVOjlILz3d3JbqJXzhLFa-0vtsXk3hkMUFIDRMYPVoScLeIx_GbNs6RA7AXhZmJigyeMhgcZ8jAK6kxsIJXrPMGBqCJ9_a1ugZH8DCym0VOY8G2sWBYOo6-tSV6NDj2oFPv4K9CiO4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌هایی از ساعات اولیه رزمایش ۳۱۳ هزار نفری
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/462744" target="_blank">📅 09:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462741">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d907997fb6.mp4?token=TFwi9rTZRw1va2jUZyBCIGzJWvYAJl0He0QRyP2h95gYWHpCt8FCvv71KQMgnubqFqv0qPkA0Zus_pfG4rUg_KAtWlBGdBpwd6DnJYDbnnFpEi054mE95Us2eCFldvJmDAImnandNdLI6TCotDWkYyfBthjlfhPv7zMSOKx3kyLNfu8N_Q5DGj2YtzlYpuvWQ0aYnxW2EIuc-gJ5UAOHkT-zwuA2TZbXq7N78jLDjhAgKuM0EY1Jrui2gXaurJ5IfOzyt0d0CbRqh0n6qML6Etk4Rlr771wuzEbXW_Jdws9vmsnng-uAvpIlje_kQlvDKWfBM6OLIxvfER0a9JUnUYJ8cNBkvzE3G8Upr9N_G5btFPknVhhd0g03GaGOOkshFb5lhJlLvr6Jp4FRpQzgI6kLvgHo2FBZY3maXrfx0Zhi553qZ9aXRjg2WiJweKyp_luxhZOZA_-cd7ZbmKkGAW3QsyxbH2XDKPasJ1_ta36fnCGOLn4t9XvjgJKktGmcJoviQhaZK8lHOpBeOy8jHuOK4q2KSoQ9jqtZrejpAEh-PBTgfZiPgGMF_So8Qr7rSK07rOz9M-kNhEohfZypls2lbFl5Co3OlvmyaSp30GEYHVwgVs0wLiiDnwBhqNom2MDhgAv9sEOELs7NaNCWDkPUmSdy84KqqqynQ2MGZOs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d907997fb6.mp4?token=TFwi9rTZRw1va2jUZyBCIGzJWvYAJl0He0QRyP2h95gYWHpCt8FCvv71KQMgnubqFqv0qPkA0Zus_pfG4rUg_KAtWlBGdBpwd6DnJYDbnnFpEi054mE95Us2eCFldvJmDAImnandNdLI6TCotDWkYyfBthjlfhPv7zMSOKx3kyLNfu8N_Q5DGj2YtzlYpuvWQ0aYnxW2EIuc-gJ5UAOHkT-zwuA2TZbXq7N78jLDjhAgKuM0EY1Jrui2gXaurJ5IfOzyt0d0CbRqh0n6qML6Etk4Rlr771wuzEbXW_Jdws9vmsnng-uAvpIlje_kQlvDKWfBM6OLIxvfER0a9JUnUYJ8cNBkvzE3G8Upr9N_G5btFPknVhhd0g03GaGOOkshFb5lhJlLvr6Jp4FRpQzgI6kLvgHo2FBZY3maXrfx0Zhi553qZ9aXRjg2WiJweKyp_luxhZOZA_-cd7ZbmKkGAW3QsyxbH2XDKPasJ1_ta36fnCGOLn4t9XvjgJKktGmcJoviQhaZK8lHOpBeOy8jHuOK4q2KSoQ9jqtZrejpAEh-PBTgfZiPgGMF_So8Qr7rSK07rOz9M-kNhEohfZypls2lbFl5Co3OlvmyaSp30GEYHVwgVs0wLiiDnwBhqNom2MDhgAv9sEOELs7NaNCWDkPUmSdy84KqqqynQ2MGZOs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رژه یگان‌های جان‌فدا در طول خیابان‌های تهران
@Farsna</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/462741" target="_blank">📅 09:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462740">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f58446e2.mp4?token=YrPk3uEJvLLLIxrkAaM6uYrd4AGWEWPc25wjciQCVN0oV2joGZydzd6ovXaa7Trxdo53refX7gqu2e8eRroxMOX-aSf9ZNzkIzDQEL8y3IjL0ZnJfC0oehd326xKStZNL9fVEYtXbBw_6yLI2tFFOPL0Bvgof8aB2ven5zdwh6FP3m3Ze86R8qCc20hhSsZp2noNLN0RRaFu9p5xSMuKA2dOfkFFPBb0CNQMNjm84kE3zuVs1KaPNB96kPLTNFv6wTSL9cRwPhi3p_B3LwuqXkG0UgAO0rV6MDmGF17CQ2ZZQMWJ8k1w-Nj6t6RmcsD6HFFANxnbecGbcYEoWZepjLZK4g0KvuIapXYmvUIKhmuyTbydBBZthbGqq4jV4WUlpqZ8gdViz22utIKqxCgi5IakcFtZ4bmHD1L8KOSDxC0a9XZ4x5f4DdOO-jDhFxI0Aog3K_6pYrsrCibPz8ULhcloXckXFX1571jCldIcLUVqBpEVyvUQM6HMqXXW9Vo_soRr8Huz89Ead2-enKyMZrJs_V1wzveynEtgjPLpaB4rtj-PR7xNCQ91ELrkHEKPPfWeTtAAnXLXFnHc13uVicPmF2WpcdJXvrCXiAr7n277RLKDExB6SeF9Ph7k42rFfJk0Am0UjiSC7IKCdPZCsCwe5XiYAip-eGfu5jVZkrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f58446e2.mp4?token=YrPk3uEJvLLLIxrkAaM6uYrd4AGWEWPc25wjciQCVN0oV2joGZydzd6ovXaa7Trxdo53refX7gqu2e8eRroxMOX-aSf9ZNzkIzDQEL8y3IjL0ZnJfC0oehd326xKStZNL9fVEYtXbBw_6yLI2tFFOPL0Bvgof8aB2ven5zdwh6FP3m3Ze86R8qCc20hhSsZp2noNLN0RRaFu9p5xSMuKA2dOfkFFPBb0CNQMNjm84kE3zuVs1KaPNB96kPLTNFv6wTSL9cRwPhi3p_B3LwuqXkG0UgAO0rV6MDmGF17CQ2ZZQMWJ8k1w-Nj6t6RmcsD6HFFANxnbecGbcYEoWZepjLZK4g0KvuIapXYmvUIKhmuyTbydBBZthbGqq4jV4WUlpqZ8gdViz22utIKqxCgi5IakcFtZ4bmHD1L8KOSDxC0a9XZ4x5f4DdOO-jDhFxI0Aog3K_6pYrsrCibPz8ULhcloXckXFX1571jCldIcLUVqBpEVyvUQM6HMqXXW9Vo_soRr8Huz89Ead2-enKyMZrJs_V1wzveynEtgjPLpaB4rtj-PR7xNCQ91ELrkHEKPPfWeTtAAnXLXFnHc13uVicPmF2WpcdJXvrCXiAr7n277RLKDExB6SeF9Ph7k42rFfJk0Am0UjiSC7IKCdPZCsCwe5XiYAip-eGfu5jVZkrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز رزمایش ۳۱۳ هزار نفری جان‌فدایان ایران با رمز «لبیک یا خامنه‌ای»  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/462740" target="_blank">📅 08:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462739">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c44e5b9d94.mp4?token=KNBBIOK8TVOnym6Bc50xm8HMZWbpbCOoj6I2I_sZvseFo06mMozXgLTKDCp7I3Bj5HRIEeNi2Lv3szYUHNwRzfrqWRXJcLLIXJKGWf0xx8PRRcBGmzhHEo5WH6J00BNrR0hvf-GBseDnuPL4-In3t1fipZ67m_O9L6PXPjXzEIbdAH92N5g7pvukK_47e3q1l2nK-_7sBz_LLDnuNjcsU9PblJSMF93NLnAZtCHs5lFFGJLsn9fYlwrtmuCAsl7OdhurD9aczXfPA6OBk_lLr9wW1r4qRtIkmh8HPJmXokZlPgJsQZd83TuERk5qjynZRmsBiY3As4Zg75lXzvJ7ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c44e5b9d94.mp4?token=KNBBIOK8TVOnym6Bc50xm8HMZWbpbCOoj6I2I_sZvseFo06mMozXgLTKDCp7I3Bj5HRIEeNi2Lv3szYUHNwRzfrqWRXJcLLIXJKGWf0xx8PRRcBGmzhHEo5WH6J00BNrR0hvf-GBseDnuPL4-In3t1fipZ67m_O9L6PXPjXzEIbdAH92N5g7pvukK_47e3q1l2nK-_7sBz_LLDnuNjcsU9PblJSMF93NLnAZtCHs5lFFGJLsn9fYlwrtmuCAsl7OdhurD9aczXfPA6OBk_lLr9wW1r4qRtIkmh8HPJmXokZlPgJsQZd83TuERk5qjynZRmsBiY3As4Zg75lXzvJ7ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز رزمایش ۳۱۳ هزار نفری جان‌فدایان ایران با رمز «لبیک یا خامنه‌ای»
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/462739" target="_blank">📅 08:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462738">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgIKRvxoSAfNy44D46kff7pdad6laetndHmb4fbz63Wnji2p0VIc0r5iqredWc7hJ6gK_NcCiuSNR3odAjLwlMdfoUVnXSC2UwAgXlunsODC3cNckxqUfYqS_JRDsdCm4WZ02VxFXykVJe21eVsfJWgdai7hoqlRqEKtcFZtM77bphjcvZce68ZPddqhojL4rTPTuuJ6VgWvSmbuRplV-62piZ2drmjjoyB8UEDgdc13elCJsx7lqTSInestD_bO3xcaCDzjAeLHIns4gEyhcctBkmXMnEQOlgs18mtnfdSFKhHZi8RrN9JMgbGeErwRmKTKhNCgeTtD2KJhKdetPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیدیان: ماموریتم‌ در تراکتور به پایان رسید
🔹
جلال امیدیان مربی تیم تراکتور با انتشار پیامی خبر از جدایی از کادر فنی این تیم را داد.
🔹
وی در زمان حضور ربیعی به تیم تراکتور پیوسته بود و در کادر فنی نکونام هم حضور داشت.
🔹
امیدیان دلیل کناره‌گیری‌اش را تفاوت شرایط فعلی با مسیر حرفه‌ای و اهداف خود اعلام کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/462738" target="_blank">📅 08:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462731">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rs6YcWybIQ9gAqo73Q-fraZescQUIvwSKN6TJvc-fSTc-pKGDGQoDRN5EeVGjlrBWtC8GxQHBkSaHvmpHR4rhUWp3tuQzhlFa_P9mDXcjCSE3ESdjVvfEzczzs8xHO4wXoS2SefgSIHvA-wWn8tkpiC4ZFhe0En2XcjTBC-TUKbgpus6XziY1oa6FuGfgAJsm1jAlE4DZ6q3oLDS7QWf8hDvmrtcgvZ22gsjjrwdsKJTsTBD4F956DKFlsf8O2yIB03E0LDCS5vRixtCzAYR4UNugR2tCXG-rqfoblqtsLY7quqOdnOEp02vnw8_gM-C4Qru0Uk3PFXTpsWkl-CZ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f-Cg91O3vxQeU3T624BXBRdLOE6Nur5e7PerPgeDR2sQ0i--FP04yZzj12VwDlvH3RjwaIUoaKS5f_L6PlcTP7F8ARUnvJlVb9YDhyA91Q5DmJ9XXopZYIk53etwYcoRd4ENe6949stnVx3NWvN15x9TNtY1aG0hOtRzYmDj3dbd-s6Se7c1lsfhhprCPDYf23BybEH10Sr8kTG8TDuOSwN_e8p4i0uMLXD54K61s6Yd1qUw7W6k3oJOe3ssRyawrka2Fnlc55BGesJwtYUHMMBk6zxOhED35_PVqwhEdyJ3eSWcV7n5Vsw69M46BPG1MarIosluJIDy0W6XjQCvsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BU_7cfgs3yT6s_ZeZkDhoVyb6xHndDmlODMNdl_hsUPQ8IhsvLhj3354Sh_atsmb-Cj6IdXqlj-QYYi5pmRx2n_enk-lsLrfwDwLqy8XV11oCBJHI5HvcI5wkBY3XP10VrDv_HJgiaW8Ej6eOZTJzi1-70cSj1DZOGhN21G0ivRduEBInI-v_HMwMgcQtAR8Ba54u-Ag0gK-cNOiU5jBkU8kbMus1mDzG4lLekK8X2NJbvYqbNLqftHdaKkU8rbSNcJJKicHjiKyn4FNuGPxH4jb75ox4KqKnChftX2tNsxR7mnYvDN1n5ziB-LjbZBVa_B-tNGIjlwEfuCOh96hqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kn2JhWqjIZu0sZbrz_U8cTckjFMPE-Ga7SqcL0jNCaYzlg_cgoDend49RVJpEnHchONJW9Z54L-M8aVlqGbPT9gkTkP3fbnQQBjevrUS0qVyxOFO_s4xvJSK_c9mdt8bvCVSLEeSBlsRBGELBjtGmYpRMvBQLqnYBjy8fcamSLErkE7T2GHg8BYnmM_LH1mjQI3DqX2NLC87Ar_W18_1RY0NkuZuQbF5ufFNPWWQgzb9J0Ozo3LD35k_cUIIQAtPNoqtDyepyLUJKT9YPCE1P5ZhnU8n9dQm5zJZdlpuFPp6YBKHm1qqhL0uOvcDdij96lDAXPCU8VUGSgQR-uo0tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q-rYw5KL19S3nDkjG5WWsYHAJDpfAmqu82XRx07WObsmou2GSR_Mgi_3XNDFsIODjgCmaUVqu0yp9hDqxc6B7lJYM5bUoZDMWq_tM12m94xaYjFzbEb1I8FdEac8uk0xS7hvfIbLhVpC7AyXN7wiZP9ywt6Xn8W6T125ix8vdsQciWlLd0upb23jw7djueyIwpJ7woBT2lSqeKxWljhtVyfi5LJDLmlvzJ1cfMy1g2igaxVe1lhKhRte6V5sj5o6wvaCkhYmGZPtIDOxdnSOzzeyYVvbkMOlm29CZowavX8h4KyTn8uTEqVPurmv1M5CEYo5sumU3xCD_GsoAF9hXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NZW_97pwFEmaG5r4KV1HsndDi0M3JZhRRuAVo20Ft0MBQo2pM-MJrgdK1h9SXsnoD1I5-xF9BBFjzk4gieAfgUQkZmU-u83F-MUzvg2I5giql1sI6qrSE26CK6-i0-vqu9GW3Qp4HHkqqgFaUnVaCk7grkvVM263mX0sA7Ljfpu9gz2YGrj6hDLPMOt_fWV3ftyYIWJ2t7LWvmA9ze5fR9nM7aL_BYewegWXV8JV5832rzKcpl7proVu_7EqDT-Mj3VQ6_-qhywP28Hetmqg-qQsQ3fYSUJMi4MOWTYihlO42KxgDRFX7V1PLSyTweegixct4cwYXsnfR9KN1a9Yrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r8CP8JDYwrmpqBVp9WmRqm611jKisIxCktH3f633r1WZ-awWYh910_AB9RkJbi8RAGzo0vzIAlr10gN3ZLMyIDWR6WwpGCTwaMt8XTE-pETRPD_HeBPULwZugs589ywvfxxqdy6w6_vlYqwNahJLqxaxDwYODl6Gsth9g6TvwfwbJ2hf5ZplYvI6a2we_DJ6h9_4gnh4cIjnLhrj5dGf8FKGewXrNgSjs8m_Ymb_OQBGDhN5cOe308D_B1n26HJF3Z4v0uSGoOcHEAp9d-jzcaOSW_1kBzYV0rG7W4w9NGkau-w2S-f6MMWzDF4Fcz7V0Wy38t12DGS4MpnPORW4jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آبادانی‌ها در تکاپوی مهر و مدرسه
عکس:
فرید حمودی
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/462731" target="_blank">📅 07:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462730">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlubIR4iCPc2AXCAWoPPkWrkET6z5EQzSGYFh8WYhE4J6KUPhI5Ml7ciIL_pKO8vEF2D-agQzrEHhcsMP7gTMB8BbZkpPZA4KQFmNo75cNKFAi6M4t95W_uWvEIm-XfCmNnaMnQywGVetMogwTCkVJVsSc33qXUbMalkJgSiMxI-0x3tij84ML7zt5cYh7XxRZz0MrMa-PF86YrF-1_efLHDvwKyUliIoKmDjEYssk_p8SgOaJlXqHBTL6utOrhesLZwt1CF5fvZCQMDipUCdrFpBdo8UvfKw7QXrIB2Q2PYC-0qtTlk_KCsX5SJiS_3G_4zGmK4PIE2hi_xekkOnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان‌باختن روزانه ۵۰ نفر در تصادفات جاده‌ای، در شهریورماه
🔹
جانشین پلیس راهور فراجا: در ماه جاری بیش از یک‌هزار و ۶۰۹ نفر از هموطنانمان در پی تصادفات جاده‌ای برون‌شهری جان خود را از دست داده‌اند، که به‌طور میانگین روزانه بیش از ۵۰ نفر می‌شود.
🔸
شهریورماه از جمله ماه‌هایی است که ریسک وقوع تصادفات و حوادث جاده‌ای در آن بالاست و لازم است مسافران، به‌ویژه در روزهای پایانی این ماه، برنامه‌ریزی مناسبی برای سفر خود داشته باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/462730" target="_blank">📅 07:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462729">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eU2IAqNbdk2pkkrTEea4QQSql4NgZx89S5DcO81OxXvcWU-QaRQbN9ununJ_D_uO4ETVu6fvKfuEwMcIvCzF9urTkrE1M0046zvVpjGTxyTtYijEapHYNl3__pQRqo4gDyNaVZ6m5glLBojSfYGazG-5bFBmFdeMT455oM5G7FXnoVs56W6p9S4Jljv93pFqXmWPerH_JLCnK_D2-bZ_SbYeSwYX-JzY7Qc-0mzTDb3oKPiviljjCo4V7dNwMaRYDMtH-ieccRndRuEL23N6qJcX8uSaHE4vjMBGA6glipAtFLEx4XDpWTFng0QuhO710EZaNWtgxB1h0RYZz8V22g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سامانۀ بارشی جدید از بعدازظهر شنبه وارد مازندران می‌شود
🔹
براساس هشدار سطح زرد هواشناسی، فعالیت سامانۀ بارشی از بعدازظهر شنبه ۲۸ تا اواخر وقت یک‌شنبه ۲۹ شهریورماه تمامی مناطق استان را فراخواهد گرفت.
🔹
طی این مدت، رگبار باران همراه با رعدوبرق، وزش‌باد شدید موقتی، مه و در نقاط مستعد بارش تگرگ پیش‌بینی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/462729" target="_blank">📅 06:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462728">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7z0Wwy9JbuxZicuryyJNlXeI3PDEz7C1qLeNSJ5WAneRL0dXLXNd16yzwhBZnQFIXlu0zgX51DCxFZclsatwLlmolRX6bOttCAs-oLmd4wkG4STWMVnU8JpnTUOTnebpQdz69GERkfYGX-TB9DnvX2Oiu8BJ-llWiPpRql-QrwXOdyGxd34gRbRjrfRQj0VS9-3kKRdHnsTAhh1gwFopywJgjzIX42OQ4a3hzkr5JEmNTYvuObWygPTZol7Vg9nMHgvcFJiEKPZDtehbdsPTpdDFFmgX9xdq06NjC0yfyCPQ6ct5lu5z04k0K9f4pGphmMPidcVxG3aBSNYXFHJjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان: ترکیه و پاکستان مارا در برابر یمن تنها گذاشتند
🔹
یک مقام سعودی در گفت‌وگو با شبکۀ ۱۲ تلویزیون اسرائیل از عملکرد پاکستان و ترکیه در قبال تحولات یمن انتقاد کرد و گفت این دو کشور به‌رغم اظهارات حمایتی، همکاری عملی قابل توجهی با عربستان انجام نداده‌اند.…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/462728" target="_blank">📅 05:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462727">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uH1GTkT1ctobwoi_1ZRO8_Fb_ejSK8dMF0uCEeG7iv7TKbfz76xKfMtv5Fq4cdDDVSjOXVCjp9DjHpS-gBLMhuukRli-XlEqFeIXXOW9mmtELFmi9z-qWOs696rAVSn6r0cDajtvFqDpR08U0-8FIehtDIN9zgerUJ_vTf3d3spIb9s8XAcqrJ6Sbg-XM3QOWsnrI8p25sv2ely4sdDlYla96EPNus8FGp_YoDobAgeaxIKuytDWJhstpBzmC41d1MSDPxRA11VZSzjQ348eP2ZZwghpqrxzxhu__NED5_LIMF1aG9xYR1jQmrkw-WWVyYJSszsoTd_aCMNNKPMjhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات جعلی برای اینستاگرام دردسرساز شد
🔹
دادگاه آلمان متا را در قبال تبلیغات جعلی منتشرشده در اینستاگرام و فیسبوک مسئول دانست.
🔹
این پرونده پس از استفاده از نام، لوگو و تصویر مدیر یک پورتال مالی آلمانی در تبلیغات سرمایه‌گذاری جعلی شکل گرفت.
🔹
طبق گزارش رویترز، حدود ۲۶۰ مورد تخلف مشابه در یک ماه گزارش شده بود و حذف برخی آگهی‌ها تا ۶۲ روز طول کشیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/462727" target="_blank">📅 04:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462726">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b10fcfcb13.mp4?token=hRqnOCF2IWrzuBH0cGIjeWJOK81j2QNb8AeWywkXV-T3p_cFo8I3kQQEGVRVYND8nnwQ-RI70qE4ne56bOBOh23WRIbFmGaVTRDy8-pkAEH5LDLkmmOib7IeInZGHZvaL7jlys2fe79KL5MzglE9wnnw0eYq4puqrzUrfViRomkXdUpu8WggVNjzfy_8rGiySSXhqNbWYcaqmhE7h9e9Kp1bDbPK0nzptM5La2DNWaSsNjzp0eSwvwMzahim9feNjDq0MKZgykcSyc-YX1oKx-3_I252ZiOZVq4Lt-QF9c29abf9CigjR_b4Xl-s34isPKtsb_NbG4VzFxbqQv_RWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b10fcfcb13.mp4?token=hRqnOCF2IWrzuBH0cGIjeWJOK81j2QNb8AeWywkXV-T3p_cFo8I3kQQEGVRVYND8nnwQ-RI70qE4ne56bOBOh23WRIbFmGaVTRDy8-pkAEH5LDLkmmOib7IeInZGHZvaL7jlys2fe79KL5MzglE9wnnw0eYq4puqrzUrfViRomkXdUpu8WggVNjzfy_8rGiySSXhqNbWYcaqmhE7h9e9Kp1bDbPK0nzptM5La2DNWaSsNjzp0eSwvwMzahim9feNjDq0MKZgykcSyc-YX1oKx-3_I252ZiOZVq4Lt-QF9c29abf9CigjR_b4Xl-s34isPKtsb_NbG4VzFxbqQv_RWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا دعا کردن مثل خرید اینترنتی نیست؟!
🎙
حجت‌الاسلام رمضانی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/462726" target="_blank">📅 04:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462725">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">عربستان: ترکیه و پاکستان مارا در برابر یمن تنها گذاشتند
🔹
یک مقام سعودی در گفت‌وگو با شبکۀ ۱۲ تلویزیون اسرائیل از عملکرد پاکستان و ترکیه در قبال تحولات یمن انتقاد کرد و گفت این دو کشور به‌رغم اظهارات حمایتی، همکاری عملی قابل توجهی با عربستان انجام نداده‌اند.
🔹
این مقام سعودی گفت که از سوی پاکستان یا ترکیه چیزی جز اظهارات نرسیده و هیچ همکاری‌ای صورت نگرفته است. آنها فقط می‌خواهند سلاح بفروشند.
🔹
وی با اشاره به شرایط دشوار عربستان در مواجهه با نیروهای دولت صنعاء گفت که ریاض در شرایط کنونی به حمایت عملی متحدان خود نیاز دارد، اما تاکنون آنچه از برخی کشورهای منطقه دریافت کرده، بیشتر در حد اظهارات و مواضع سیاسی بوده است.
🔹
این شبکه در گزارش خود نوشت، نارضایتی مقام سعودی از پاکستان و ترکیه در شرایطی مطرح شده است که عربستان برای مقابله با نیروهای دولت صنعاء با فشارهای فزاینده‌ای روبه‌رو است و آمریکا نیز حاضر به کمک به ریاض برای مقابله با یمنی‌ها نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/462725" target="_blank">📅 03:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462724">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c730A4k6oKmxCGQdbyesiQTQndTZLRoRtfSUilr_jlujQ5lAMgWtDiXiP82wqgUD5AAJrL7qMsHdbJKXkfx5M7jlrPndD2s8tVWP4t8dv9wE7Wy99CJc-hkh3f1kOxs-p48BQv5eQkYI5LLXYXtCvCcZT0ZZgREncZucojcucX6mwBCcIbo_eCVedARTbNBUqrlU1Dq_bAxVl1kueNwPuqxOoaIhGwX1P_9zP46ouGypHdtpX6uNUGcRgKIQNnSTr9Kyasxf6mmwaKOv0a_2voiP3lPM80r_5rHzEOm9kDfHJT1IoVymZ7doNZAOl3huEHi428eHy7EmRT0Gkx2sAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریل‌گذاری تونل آهوران پروژۀ راه‌آهن چابهار-زاهدان، در کمتر از ۳ روز
🔹
عملیات ریل‌گذاری در تونل آهوران پروژۀ راه‌آهن چابهار-زاهدان با فعالیت سه‌شیفته و در مدت کمتر از ۳ روز توسط قرارگاه سازندگی خاتم‌الانبیاء(ص) به پایان رسید.
🔹
تکمیل ریل‌گذاری این تونل، گامی مؤثر در مسیر پیشرفت و تکمیل پروژۀ راه‌آهن راهبردی چابهار-زاهدان و توسعۀ زیرساخت‌های حمل‌ونقل ریلی کشور محسوب می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/462724" target="_blank">📅 03:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462721">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ACD9qnj7k-gI8NGmK1cUmnC7RoSs4j338ibCDLDWS9_a9aRAMNfuko2eJ7bgguQ6LFrCiXGNgOPilM7k-9bH9Yrs92DL5WZyuVp8Qyuys1beWefN3kdDh_DKEwX5-jI6fxkyEiY3sLsWr5hijfm-46Xg5Yw-f6EWOzNV-xRjAFHPgVQnTTXm3ab39LDqMbgQoXQzMJZxQLH8ikekItktwELCB0NXVOehUglFUDNL0cLk_CyzzBswLfJKQbbl9Vir-5wavoezPYAeEvjjASPlgrkN3ZVfkgm_XVOCCsbsg7HmAV-QzGAmrASQktyGBupZmG1W50DLVOmU9DZl6OuquQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-ZTe550vBTxuIKgy_1KgdJDCCjFBKgdERur_MTHuriIhph_fq9LyJ3kHsAL1yFFYyBdkWJ2GgSmLZ28LKEc59vDCgHIddFiNqr8EI_3SrkxfRVtFj6olf8iXp8Y1aggyFIS39YiFwxonFIigD9EUc4X5FP-QrfowgSBJrnsLHfVxePYetPKTgtZr4d0TG8aQCL1JImI_-3ejiqZXQEL4zIxWD1kGHV-gogTVDH-pYzt-2d8MBCGtYB6waW_afF2h9kxxNdrfjFqX3UyxTGxYIDOEg_CPARJ35cgxdWnYEZ5g0C9rHJCrw90XJveOE_ZfByzmuU_VI5Kw8P-rI1F9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HkP48WZSGLc8dy19Yi9-fNwm52Sf5hbL9dM9SxLauCG2qj3gin5-QiEKjtfKubvb4Hvucv-_gFuFjeGXtGGuiD4vxYobHDouLvuqNQAA8PnlQKseAWqh-urp93puvFhxqurq5_DzqYlH3sD09TzE-Xq_oftT8BbA3TbaIg3K-N5nPpC7tpDc4nek4LNHUcgJ7rAcg2PdnhqwA91RV24PGab35PM60cjYL1QMFGTxw-lDo1zjZA44WkKSO-ecbxpcKrS3Ub1Zs8mcWR2d1Ee2cTuh8p8vYfYl7Ar5b_WbfrqbZfsANwBYWeSiYX1rSBCVRvVzLEECE1lqIKheyn4RvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ادامۀ خروج تجهیزات ارتش آمریکا از عراق
🔹
کاربران عراقی تصاویری از کاروان نظامی ارتش آمریکا ثبت کرده‌اند که در حال حرکت به سمت اردن مشاهده شده است.
🔹
این کاروان نظامی از کردستان عراق به راه افتاده است.
🔹
ارتش تروریستی آمریکا قرار است تا ۳۰ سپتامبر به حضور ۲۳ساله خود در عراق پایان بدهد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/462721" target="_blank">📅 02:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462720">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انفجار در اطراف اربیل و سلیمانیۀ عراق
🔹
شبکۀ المیادین از شنیده‌شدن صدای یک انفجار در منطقۀ «مصیف» در حومۀ شهر اربیل خبر داد.
🔹
همزمان برخی منابع عراقی هم از حملۀ پهپادی به استان سلیمانیۀ عراق خبر داده‌اند.
🔹
به گفتۀ منابع عراقی، پس از شنیده‌شدن صدای انفجار در اربیل، هواپیماهای نظامی آمریکایی برای گشت‌زنی به پرواز در آمده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/462720" target="_blank">📅 02:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462719">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWZ9SNWexUBJtnCfYFAoKK-l-So-FKs8go5Lz4eHjvAH8iCM9AzP2IITjbd8l8mRm0DANPGRZl_BJyD7XMXHJKgNuBMErPk4aM-x6StiSMFy3GGNdKlpVMzgxT4ll9vkS3FDvkHUA_Iy28Ij9hGUpTvtbucB3UCExYAjZW9HKPA_GuXHadwzy5T_si-ut1WCSJSv98eMkQ90zPFHq1jEjEmWxaPcC8H0secOhl5vll8rMqKBnjlO5WXJD06x9Bt4L0Ic9-3mtBkGcLubKulxOLqBHG9WHz1A-QT2yXzsnM1q1GDj-TIQaX32fbZY5HhaBzqTkCz-s6f7tQkWkbuxzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متکی: دیپلماسی هم‌تراز میدان حرکت کند، دشمن شکست می‌خورد
🔹
در شرایط فعلی، جنگ‌های محدود، ادامۀ محاصره دریایی، آتش‌بس و مذاکره، چهار مؤلفه‌ای هستند که آمریکا در قبال ایران دنبال می‌کند.
🔹
در این شرایط، عرصۀ دیپلماسی نیازمند دقت و هوشیاری است و مذاکره یا عدم مذاکره باید متناسب با شرایط و منافع کشور تعیین شود.
🔹
اگر قدرت دیپلماسی ما پابه‌پای میدان و در تراز شرایط حرکت کند، می‌توانیم در برابر دشمن موفق شویم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/462719" target="_blank">📅 02:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462718">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فعال شدن پدافند هوایی در جدۀ عربستان؛ پروازهای فرودگاه جده تعلیق شدند
🔹
منابع غیررسمی از به صدا درآمدن آژیرهای هشدار در فرودگاه شهر جدۀ عربستان سعودی و تعلیق پروازها در این فرودگاه خبر دادند.
🔹
همزمان برخی منابع از فعال شدن سامانه‌های پدافند هوایی در این شهر خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/462718" target="_blank">📅 01:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462717">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25685c3991.mp4?token=T4UFVehvMcYGTBeMDex79msszQeHRM4bbVvamOHwgznVjnlqCJnXRmIN4HneCLVHI13KWp0RIOeMSKIrtyqusdOmL7H5uRqnsuN99Em_McyPjFGjLZ6ZVntxjKay3zdZaT1rN0oamgb9OJtq9-LW_xilZwDeuZRwv_H60rXEvvKNzvsofC1kTGR6Ry2VkyXv13zpVn1T_gbqsmI-B3GQ43f23E5U6RqqgOrGZIhfT3rQy-GsJ7pEsUUNtBot6MfjRbsLrY35AR7j2lJtpE1M1eZ9Xbx43W6K7zxf7PPzdOBT2cuTLR44Aor2J86khargchlI_G9EQo3WFTUI9YF_TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25685c3991.mp4?token=T4UFVehvMcYGTBeMDex79msszQeHRM4bbVvamOHwgznVjnlqCJnXRmIN4HneCLVHI13KWp0RIOeMSKIrtyqusdOmL7H5uRqnsuN99Em_McyPjFGjLZ6ZVntxjKay3zdZaT1rN0oamgb9OJtq9-LW_xilZwDeuZRwv_H60rXEvvKNzvsofC1kTGR6Ry2VkyXv13zpVn1T_gbqsmI-B3GQ43f23E5U6RqqgOrGZIhfT3rQy-GsJ7pEsUUNtBot6MfjRbsLrY35AR7j2lJtpE1M1eZ9Xbx43W6K7zxf7PPzdOBT2cuTLR44Aor2J86khargchlI_G9EQo3WFTUI9YF_TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رهبر شهید انقلاب از حضور شجاعانۀ حاج قاسم سلیمانی در منطقه‌ای که ۳۶۰درجه در محاصرۀ دشمن بود
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/462717" target="_blank">📅 01:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462716">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4ucy-7gqTmxsKU8NyQoUwXZD7fz0i4JEiJF_humDB6xQg0xNEbdtCqbCSEFFx1SRIHRB5p-Wgdol1P5d1L99kiKSOpj_bA3W5tgBaZNCJ4RSiBD6gG3UaP7Pg9lGdFStp9PqULzbhzbt-RHwnLKT1PL6x28PJoW0WhV9Uo83kj5w1ksPkLVdfcTq5yxdGJK9tOijtzhSUfZfBIoIYQil20_GIqkX5ij0EL3EiPad3zqG4_71auBb_qgWkQu5ZZkmVm1iDG0A4oOs0GDiaCDbRHqsLG_2nOPhuglqaFY7_xodjb91u3wEItFzcQJxMZomaP9l-jf_AIolIy8W1eMCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نصب دو راکتور سنگین در پتروشیمی لاوان توسط قرارگاه سازندگی خاتم‌‌الانبیاء(ص)
🔹
عملیات نصب دو راکتور سنگین در پتروشیمی لاوان با موفقیت انجام شد.
🔹
پتروشیمی لاوان به عنوان یکی از واحدهای مهم زنجیرۀ تولید محصولات پتروشیمی و مواد اولیۀ مورد نیاز صنایع پایین‌دستی، از ظرفیت قابل توجهی در تأمین نیاز صنایع داخلی و توسعۀ تولید محصولات پلیمری برخوردار است.
🔹
توسعۀ این‌گونه واحدهای صنعتی، علاوه بر تقویت زنجیرۀ تامین مواد اولیه، می‌تواند در افزایش ظرفیت تولید داخلی و توسعۀ بازارهای صادراتی نیز مؤثر باشد.
🔹
اجرای عملیات نصب تجهیزات سنگین در این مقیاس، مستلزم برخورداری از دانش فنی، تجهیزات تخصصی، برنامه‌ریزی دقیق و توانمندی در مدیریت عملیات‌های پیچیده مهندسی است.
🔸
این عملیات بیانگر ظرفیت مجموعه‌های تخصصی قرارگاه سازندگی خاتم‌الانبیاء(ص) در اجرای پروژه‌های سنگین صنعتی و نفت‌وگاز، و استفاده از توان و دانش فنی بومی در پیشبرد طرح‌های زیرساختی کشور است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/462716" target="_blank">📅 01:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462715">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4kYKTgHReCnd0WY8kkj_Za5R_f0xqo6ZrNvGEhpw1u7IXwXhyRHeyz-C3qaHwZo_BnaLHD8goLCorHUpsZ3Imdg4tSLjvxT3YlJiPuJ8c9L-yhk-eyzoDa1yTESJ8bft1-9hP_wIaEowOROfGFLZoKRq8XG6ZJb3vNZmWog4HIgJCCm91VkvWUz6YxCeKF7qIcTrIxZiJlf7jX0yEHR7zLqTOqZLiszbfEIQp5V2JTcuhnAKpMl8zPcLpmPnHb2nnkc26nbmBkTQTqFOdCwLkkcCxelRwwevSe2hqiVi-we2o5RclXWLhgVetGQRCn9en7X6GqSfYx8LWagUZcXqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزمایش نمایشی اسرائیل و یونان در مدیترانه
🔹
رسانه‌های عبری از برگزاری یک رزمایش دریایی مشترک توسط اسرائیل و یونان خبر دادند، در حالی که این رزمایش تنها شامل چهار شناور بود.
🔹
با این‌حال رسانه‌های عبری با بزرگنمایی این مانور،‌ آن را «پیامی به اردوغان» خواندند. ترکیه در سال‌های اخیر تنش‌هایی با یونان داشته و در ماه‌های اخیر، مقامات ترکیه‌ و اسرائیل بارها علیه یکدیگر موضع گرفته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/462715" target="_blank">📅 00:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462714">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
سپاه: نفتکش متخلف با پرچم کشور توگو مورد اصابت قرار گرفت و پس از آتش‌سوزی متوقف شد
🔹
نیروی دریایی سپاه: شب گذشته نفتکش متخلف ترند با پرچم کشور توگو، با تحریک و فریب ارتش کودک‌کش آمریکا قصد عبور غیرقانونی از تنگۀ هرمز را داشت که مورد اصابت قرار گرفت و پس از آتش‌سوزی متوقف شد.
🔸
نیروی دریایی سپاه بار دیگر اخطار می‌دهد که عبور غیرقانونی از تنگۀ هرمز جز نابودی شناور متخلف نتیجه‌ای نخواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/462714" target="_blank">📅 00:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462710">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gz3AcR341pvocVZJw4ZpwmIH9-eJaPAJ3UNEmLZMMDsUmA3F49pYHAuVegSG5GyoOAtHSf00vsO4XpmTSOKG3yc1qO7DuCGylLbowfuFARPjTiHjdfPzZ7W0wkkRPEZ36vQx796RMSj8Dxdnm4qMkhKPtW6Ww7U03SUMer1U1OFifVIOxxxEOoM_TYwLUCTL904Hdt4iyf7XMlcAtET_xJN9d4JDKxUJDZ_qYfpjEuvANMz87fcJuaKy1VChVPFlbClJBcoMuVuAOwR-BgnQ-YMSGURoVP9186QXm_PHz5f7M3cV8Ih8lE3PIuOTmpET5nAsr8UpccTOwL3SIrogwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Viw0_Nyv8nxG-3Sj0PJXcyYQBgN2JD_NHkvDoG2LEwsd7LC8PAXIgmDvJ2YbpIzvg2kwzNVl9MCxBH1Ezu0oXOkTbxUPuP08AV5CR4rIQvnhBhnZX6stVzaA362iFxAg6kRo4WjDhiJWp-oSK3I0CxqIbVr_t0uJJBP7Uonso6QH0mxTkf4g5JtGGbPZIP3YTVfc69YirfmYjraV_PfOrgdKMlj8vXK4tpSwlNMomESs3As7yKiPHyuRqnZUaaOJLE2nup8qoC_UHRT1AYO4LMSltKuoSpzpN0yXeMajxqP5nXoFRm3DLf3gQGx8BftdQhMMmk5aFgG1m0IIyT5X6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qm420GUA3jmpN9KLfxweBCkp2q_x1glOfM91dZPfzupgQ9-ewH3_2LdLNZB6nEC8QE1jORz0lBBUmFaZtY_sAUJKXtJZQ51LcsNN0LXcxKMkdVxZ7ovDvzhSqJl-OmCznIxc6q-LS5lZ4l20emEhUssgHg5q7tfGfM741OyzLB0xQ--aSK55bFAA35aFjb6_OOJ0o6m054d0uxF3_h5h5v04bmeMZXD6Fvfj2V2RcPcd1bwR8hfoUUtGBzt_nsGSv3lcqb8x_EMGxh_siTb2BzDJ3LPwmfigMAy2O7Pq8YOUabNlMqUEJXJOoH-jxAWh-LCcVsJjD4ATz11Fe8FGuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MMbCa_LCzOtMPoaboOo0vaieHl-rkg2gBIvNjRLZA4-sSoW-Q6d8GsBNmMcWW3om6bsSS3ocTvaQFXGMKlo8xlqOSoIbv4JxHgSvQmxxRmrgpA7W6QLrYBaV0r0NEChTBLOQI-tDWJVKdtAwXCH8sQTt_zp1D0fG6L3GlGo-9plQ-2kgYaXg68PVgQo1Q9PhCCyWLUc0vthLsTPaKrYdENXsiuYSm5x6ZioVemQO8936V1VvvPfmtdfRuTdjKmYIC-vKWg8Ysq37jjr6E_BkuiawZ2jo6c7nJJnGGnNPmykksU5BgqQFb286UAs0Rt23kIkq8ZkRoh7Q_2ThqSd_nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور حجت‌الاسلام محمدی گلپایگانی داماد رهبر شهید انقلاب، و پدر زهرای شهید ۱۴ ماهه در رواق دارالذکر
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/462710" target="_blank">📅 00:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462709">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ادامۀ تجاوز رژیم صهیونیستی به جنوب لبنان
🔹
ارتش اشغالگر رژیم صهیونیستی حومۀ شهرک‌های بنی‌حیان و طلوسه در جنوب لبنان را هدف حملۀ هوایی قرار داد. @Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/462709" target="_blank">📅 00:21 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462708">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foGnK4TaklpiOvfu9L--xP5tPdPFvxU21AllVDsqLgZfnrqE1QTBHuN6MN68Towe1_4k4Bgum0TvmV97FQ2db-t3oQY4mL4tCQzMeIDMTJcXf5_fxzt25pC9pZ9zGp9Az2kclxU9I9ODgmGFRWs7NE_490u9_soppsm3K06oHoEafRJcpf6FYy5bQ4RTcRVjHQv8FprBUOPzfDrvACYbkQEZzazKfbXOST4pWKeIRzUTtCYPw8ZbPyvmSdigMTqFIEXnO_dSFWTLONrR03gxj8GafVQhAOfgOGh9FqBtJmJ8Q7KIaz0TG4HWu1Tjrxp41FhTZ9kdcCoivcjXwAGlEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ما خیلی مراقب کشورهای حاشیهٔ خلیج فارس بوده‌ایم
🔹
ترامپ در مصاحبه با اکسیوس گفت که می‌خواهد از نشست سازمان ملل برای شنیدن مستقیم نظر متحدان منطقه‌ای استفاده کند.
🔹
او گفت: می‌خواهم بدانم کشورهای حاشیه خلیج فارس در چه وضعیتی هستند و اوضاع‌شان چگونه است. ما بسیار مراقب آن‌ها بوده‌ایم.
🔸
کشورهای شرکت‌کننده شامل عربستان سعودی، امارات، قطر، بحرین، کویت و عمان می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/462708" target="_blank">📅 00:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462707">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ادامۀ تجاوز رژیم صهیونیستی به جنوب لبنان
🔹
ارتش اشغالگر رژیم صهیونیستی حومۀ شهرک‌های بنی‌حیان و طلوسه در جنوب لبنان را هدف حملۀ هوایی قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/462707" target="_blank">📅 00:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462700">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxYJsGZw4GBAAVLoLrW42KB0RbiWviZ06Ia2wjb4ImWc_4DXNnJJafdZX-duGiYCx6d7YRpbuiH1oco2FA9kXDyGTFuQw9MecomRac8FpQQW0Umq-2NQ86gs3bvYYuh5D0cte4OlnUr2parvOhxmByLWDeu5Rr-FqHFphcFFDKgz0Uhs1nMpbQ4hL1ExH6S5f4vjp3rLPghY5-jjD45hUFYKn9aCnGXJ8t804DIQSUnNk58BuR3Y7r_p17DR40hgHCT61L31ruU6C5He8EEcet42OJ44fDo3bWg9bKcPGKi0fa9Uto5jjuuw5W7ocUMlBL6R8Pq3ySxXcX3QxI5Oig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UxTM6QuSZp4JIbiEPP7dxTMrUCp_2_NZv312lmZK3i4u_aXj0-6fvREqvegvhUnA9dZW2gE3vWDUiDF-OHYft1tfZsgxVLy_MBc9FGFEdDEL1EhgLjQsTH53K6ryKs9D_0eMag3GyzjS4Cw-V6aeXc_DJF6Aw-6rRy5Hub1G5TCWGRiHLNL9KeAmhVHgvIgt1d2lpDtSV2dSTjHgK-EVWl4f_pXqtxxGgEDwzgpOUEhqm7Ax65LoY8kaHEGWQtp0SxDAEjL5s9toXRLUnS7JR29vmUmX8ufvE35dMxUYjnOorxm5ch0iR5OmFxkMg20hBn8gi6-Rja46l7FUPwwc7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/elCCIChbcfAprzOUfmwzL-I-E16C1MzPHHvLyOVDpsjCj-YQwuQWOmYGiYEdHWVHPnagipmEm_xsHr2ghp3W9rebI5ZLLHV7Ta_48z8EmS_QfnkmdCqgMbp5l5xF1pmIggdEYAttYAn25mG2MswZO-TXAI9dhDZjDv1oDsusFZJXGKcq5e9zTD808Ifjunm1YuJ6yuYJjlawLjmDAKKD1OUs6M1aicibasG_0n28Pm8wH1B0E9_xMu6oNsC4h7v1bFUM7tNHv2WxKCmYXxyIVBqGZJEjeK1yBYZNu9dspVOF0IspASDguxwKR1vUHHMKwWd4PUc2yxxEn0_I-GFhrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JVH20lGP-IcjMiIQjUtxTs4fWe2zJ5SZ2VnHCVQASyllfYx8BfAvX4vL0zx3RENobpOF-sOJXv389OwSSFddO0NB4nEOU_D2lIzPfjv-LuH46voTwvxOpjgdKFR1FG2jCi7dx9CL_B3e_6cbdnYUnxyWOwTSol26OHBFOA3BJK28SYj5cCOCU7FQZXZeizRR6JzXHrg4vHrmxPouOvRKmXa89Hc3i8PaOuDtHEQFsgeomOpYziOA3RjbeTb9Ihw8t27p5eWJeaQYFiPzfAzh6Dy8KsE5jP224PJRaCohwmQ_yCVumUVCxPo5_2rek9jUQOSHTpDFKW757WOk2T6uGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iiZN1Yp0U6HSlh18ZK_B81Dc3edogeJ3SIC6_Mu96N9Tu_fUek4jP8zlgw7G3XC2YYQPCG_u03wf0WYQSbFYA2IUlpaQQa8sKP_Yv5xOk_sM4DDZakL5Axk81CpNxRk6DudbAbhTXhyhQe_8-397rtV_EI1RN3uPzsk03BBZssw2CKfIamIUjYxYVUO1wqE2M9AvafFFqx_VpO1XfyQ8qSBkK1wjnL5tV6juFMoCa3GYEe6y_05BkDiwPleuZ48xQ6BofbQSw69CLnD0Um7WQSVq9W_nBFwUwkKj5WOcTYdPOUKGiuU-ZDbVZawBoIkUghucJlKyV34xowfBSfDUcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZmRCtE9SbWKK1iNpeXsEZLalCqr0prWU4dAjbJul3zEPTTZkFpkWn4I6IrsX3udUwNEGxxL_WI_66gJPTZZw2LvvuwsRbkRwrQzJCLbt4S5vWH1sg4ZZjZ1cdX_QKQYdB3Ddw7_sIfWqyjf1WEAiyRw8J9yOLkN4TksgmfsvhQzjXKZMEru3sZSVAx4Ri0tFxuljI2-Htunr5YP0qbeKYGJxMbrj87lf7PzsppV0BiFtg9ZVu0_3D7gPqug82Jlijn16kMNmbxyo4E5x-Smune3OHEXR15VEIzoacdSyXN9WkYEshiUKo_mIQ_FiJk-Zl4yIoJdGsmOrzJ70t8vIRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PwforE1gBvNl9E2zVHZhf7ove5yWBlVLWN14kSQ4S3gNFP9mLrVQEzCLCcnsLRlVsWnnZYyJ5lKpJ8cV6PP6bc5f6JwWLNcLXGhb0CmxOPokM26o611qI51bZ-J8Zgw39CrAQN5BWakVpT8Hq-ZyTj9bYn-eWz4s1t8BIwZW3yUpZdNg3OJULDeTyFTVHta12nsb7IOHCUB1x_t8JQRB5NznmREckLFt0ryWk1_U4YytSTMq7Rr6a8fgkzRujENjVt7IGIdHAlWxs5JBGDtCCxIPTSC4jG0ddQS_Avf6FCVx3ALpei4x4l5itCSSEydT-M1ys1paQj01_nD1IO892A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خشکناب به یاد شهریار
🔹
روستای خشکناب، زادگاه و خانه اجدادی استاد شهریار، امروز میزبان رویداد فرهنگی و ادبی «یک روز با حیدربابا» بود.
عکس:
عطا داداشی
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/462700" target="_blank">📅 23:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462699">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqFpY8ZyADvQQ8eN-h3yOEoISX4pKhz5YqP29vwZTprThd6s3DVB-_eTRcXS1O6kVQSVFsAUJpDrIfAmhKvVWxnJH8n9OBXMiq4BviGlQYTf1xPh9_rArd47gPbYN2DJ6RiAE8mr1I-FFes2Dt9nlOj5pjwshS781b2rZkU_juvwq_r-m4szj_BqtqyeJkK88cAq41DZIpCrsO_4TwDesT-6YXCX6cAYdi-jqDS-QFAA5g_og9fdeRkt9mMd03PnfCYvQVCnZbY2dPd4W3bUgsAE_ZjJlEb65Kbo9jxm7WX2O1UbUKHziKYN4iZCzD8BO2LG9G6wNcMY9Hwr-74eFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرلشکر صفوی: هیچ جنگ تحمیلی نوین صهیونیستی یا آمریکایی، نمی‌تواند بر سپری که از بصیرت مردمی و اقتدارِ ولایی ساخته شده، برتری یابد
🔹
اتحاد مقتدرانه ۲۰۰شب حضور، میان اراده‌ٔ ملت در میادین و فرمان راهبردی رهبری، نه تنها یک پدیده بی‌نظیر تاریخی در سپهر بین‌الملل، بلکه یک واقعیت تغییردهنده در معادلات قدرت جهانی است؛ هیچ جنگ تحمیلی نوین صهیونیستی یا آمریکایی، نمی‌تواند بر سپری که از بصیرت مردمی و اقتدارِ ولایی ساخته شده، برتری یابد.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/462699" target="_blank">📅 23:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462692">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WhtxGzIdymEZLcds48OojfbrCFr39994WdVGG1WpO221kZQESwAbwgeo8NQpCHuygbwXaKL9t2FDq7KT_3ULXayvaA0XC9D5HotOxkg1BlNra-sBjgDFq2ZKoQq2ApSIdHRII4vg6j4TlTm7v96LkEi90NxY0PKY-ypyNUqFeFcwkY9VbyfoqNZPXPkoT7UyDgn7BWpa7ES9ASolyDOlT5VNbjsesEVvNzStN79lMsjKc0gvR3n45mVIpS5u_-IWBvUoU3mqKXDSBxLFMWTn-k5tN3MKVKoHyxnAs5UlJcBIedpBZChQ6r8ULCfFVkdkg5DtG8GZ7ZFycPat9-WdSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cFxcHQqdfIlnDG4XPOPCTOnl_q6RDcWcMynefVUlaU8jJUOWlY9a6f6zTysaU7CDj1s5B1VBZ0iMckrKGKeJSqD0yOJijpJUzvmwSoWI0518Wsnc93An3k72PrFMJc_UmCDTQaGEC2O723zVQVysUnlQax8BMjX0uggbnNrvwMOKAYv5u8YGpW_1VBeEM5r0ncMSsaUYdg8Me635CYiURH9zxBHfTdRLPhg5tH1UlO7IB4ue2Yeky26OXbcYxHO5Gt9u7OFE9cesD33-GEeLc4qWuoUk-0VT4NspUulyFSDMvUXQHarEnCDYeZDp87bzV-2PQw0rC3omI578FLH59w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I0Yy2yMSbJcaWB1_BhTcxctWRv7qE314Ear_LtYoJobD_cgyEScu4T5YSgL9XWiYHbWnEPn2QT4fCIydmzYqSVM72wb8JNY5-X8gtHzXPxBFC_Y-BaahtoK3JCu0iUC3wvE4kq8LtjqDXiPO7eL3S0JOShf5GpySinObO-X6iDja7rrbDqDb-BHZwMCOXkAJw6bh2kJ8oMz6_eS8qUu5PHNqPytTKMEOly1zxuoLTP9abR5Poy1neM1GUOIGhL-FOjiQb5kks9ZKVRwGLj6JsSR5XeWMJChqZ8F2HgeFEzObcZQi2rgETa-M4yYMGwaeEfImPBtLLM2eUNSsR7b2EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ku1gWjlcKVaYhJFg0LqBID9kLaH-QuzaUX5QKzFX7UTgcEKwJILIOPqpts2lJoVoOMexhW26LUsFnAqGlD_9xHVwAHkc0rp3wSUVfsCpbKok0qZIPiYnd9KentVYrW1_pmtOkQ4RnuOlhqdmOvvjIRO3Nu_VXiAmlFQcaXGw0nELlfBEioyp4bcUYJ0kR9dJgNi_IdKrQtRlKz_jq-iJ-reYm2eoZOo1NoOXn4KzPqXgm39bazaQdkmAcKsh_oo1smUK1Hgk9V9Krvoalbisu8En0W0juS9jPgKXvEfwiE-pM3Y99ZAJTKAwf7p000wYzQjFaE6wVGo6SUNJ-D_WNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B3rVSLwMLKRVIOBxwhSMLDBB8AgKwZ0vS9Aa308LQPqrOxCDpc8vDganSEGOqRBGTXXzQbpQ_VPozt8MORM-ZHdKab8RRD7tlV1B2f7UQX4SkvLiZe4fGFsN3rTNiH_OcKBNRqXF6u7M9JIBwCjt7Sh_VRIO_kGx6qskvhfSMX-IaGAOlLEVbCYO-MEWdZPNGdXaG0ABdcwrUcDvARlJWb7rrn-u-DO92UW8S8GrGsG_6YxfmbrCU3khnyeGHu3XPlIAqqCkxH0Q5ttNb6oIxkVWIWyew9tC8qA18nLikTqy_M0ZpRu59eA8b08WmZVG58TIlEgDzCK1YejHYyDa0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M2Q9dObhrBNUWYQiAlA8Q7P_9FdthmxzobYX2z-QnWg4XznJJSvzGAGJPagqYFe3B4BoBfLVXa9kFJMDcn_fmaAllw5KHcG__yjSi36yma-a7rYPccsn-HKurrwcLe9CyTywkM2Co8I5kzV4o9AoA3LG2lNhVLP39b63eyMi-RZdiWwKAxjdFoJsi6U514rY3lGYT_oJY1lo00pEpsSmg8tFyn8YC2w_sVm8H3o0UjVQPPJCvTR-xaFXV0NO1MTIR1bmunV6cl0O5lE1ILHTK_Jt2IP_FC_gi61kB_m-l5cdPVdb3POhHSQXUSQVFIrbBUE-bzb9zcpsoz-39p4_Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tLCN5O7j0TVNzvVB7dFAQSslZGr2ym-cajEZFN_EAD9tRQSTO2vs-6_JUJNfGNya8ki_r_ZuR2hZYJq7TuzUqP846m6Jui-Ob_z2ZPegAt_D5teHN2kePoOp7Hmw_Cpv97G8Gy9trtAzQMRaFUaMulhhRtTkLSyqKtWegP3knEYN9Pem9zCm2oHWgdlJ6SXbPA0LOWIFOhvsJljAcbDT8Y58yUtsbFExnagHgn-ug5Ty95gMf_FCExCKH9mFWf3EJQ-B1wp3qsJmo4mbUJ1zSSYbIMY6PcSJ6e-hccsiZYWXIxkvAfxaNVZm6-4HS2RHKSnnTlebpnWVDZUlvZ3XTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
روز بختیاری‌های کوهرنگ در دومین کنگرهٔ ملی شهدای چهارمحال‌وبختیاری
عکس‌:
رضا کمالی دهکردی
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/462692" target="_blank">📅 23:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462691">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-QBFjVglaMmYMlK9TOjZKroNguw52ZlOvOfL0MkJ7Q0G24aN4w2JWk0PE4D-vkM4fI95UDl224fWqYCBH-Euepa2cAq5P6EbHzrpMEd7VR8195GaSxy-k0LtWa7NLENqCLNY6IDzwW1W2Bjaf3wdRfO0dcFTpOztzmBCEq2-2gzmdcHzPTiNc7p70eSX3XkrXRg0EQNUEniW6T4CVJqHGGH3BdL7q4xEG5fg5IFZTqoLsm9NX9PsSwaLbRqfTDglRXMs4F8fQQWNrkqt5Nl4HeaJ8gv50BoF9BNDgO7kOlmvTTwXke2cb44geUQm4DgpVGIRbNBEjoH-eGu4V9dBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثه امنیتی در تنگه هرمز
🔹
سازمان عملیات تجارت دریایی انگلیس (UKMTO) روز پنجشنبه از وقوع یک حادثه امنیتی در نزدیکی سواحل عمان خبر داد.
🔸
طبق این بیانیه، گزارشی از یک حادثه امنیتی در تنگه هرمز در ۱۶ مایل دریایی شمال شرق خصب، عمان دریافت شده است.
🔹
طبق گزارش‌های اولیه، خدمه در سلامت هستند و در زمان این گزارش، هیچ تأثیر زیست‌محیطی تأیید نشده است.
🔸
بررسی‌ها درباره جزئیات این حادثه همچنان ادامه دارد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/462691" target="_blank">📅 23:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462690">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94517e21c1.mp4?token=Z8m0dU0vrglBIZP9pWUQFo77X0JngzgnXtDWVlKQ3oxOOpkRIJ6SVHidaC9BsCScJzazEl-an0UbPeiYrlbKF_em6MkBY-zMleLITzyLZHXUiKtoUyyDDMhs647Exjdx7yqzmgYT1HaWJoB_t6Kw7wjdhxMWx0NqCua7er6QAFEhA3qBIwVftrauVVcIJbLfVF7wq1HChQfO0HVdbzNyfZMaruJIru-H5trNGSQRypI7bXro4RpQJsGHKi7L7j4qByc0PgdxW03FqWCgkF6bVPUJTVvvqTqTbUE6gcsU5Qt96Lrc2ch5w2iMMv8C98ZSTTC_Q_9VpVuUwucM9s8lRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94517e21c1.mp4?token=Z8m0dU0vrglBIZP9pWUQFo77X0JngzgnXtDWVlKQ3oxOOpkRIJ6SVHidaC9BsCScJzazEl-an0UbPeiYrlbKF_em6MkBY-zMleLITzyLZHXUiKtoUyyDDMhs647Exjdx7yqzmgYT1HaWJoB_t6Kw7wjdhxMWx0NqCua7er6QAFEhA3qBIwVftrauVVcIJbLfVF7wq1HChQfO0HVdbzNyfZMaruJIru-H5trNGSQRypI7bXro4RpQJsGHKi7L7j4qByc0PgdxW03FqWCgkF6bVPUJTVvvqTqTbUE6gcsU5Qt96Lrc2ch5w2iMMv8C98ZSTTC_Q_9VpVuUwucM9s8lRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تب و تاب «میدان‌یار» در تجمعات شبانهٔ مردم گرمسار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/462690" target="_blank">📅 23:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462689">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkM46UStfv0tZLlZHqA4w-Z5QONage21HPvbZtn1keso0ZVf2b5oqlr6JuzSBW1lDR7xSBQ7zYnfriQptyJzUiQ8-dO5pJsSompdk_GuYU0tLUxjYAQboRm3dEqbjL_uvUxceMQXnv5LiBK4MbXeJde21wn7r6MKKbOfzB1yGsM3ycNmyjD13ZlWRfdnoMCbn3BbnmP6_4kybCJCgNmPhB00HgVmCwaab-zte4-uxc4THJ7V6w0aE2r_VJ3DKn-AHptDimc8SuMWIzWLfNpz37aqwSp0vGRhL9fxKgg6fMDQQYc0TyDQVB4mRg-To0lCkQvtzClpnD4CQFaQ9YhuDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از لبخند ماندگار شهید مرتضی لاریجانی
🔹
جمعی از اهالی رسانه امروز با حضور در منزل شهید لاریجانی با خانوادهٔ این شهید دیدار کردند.
🔸
همسر شهید مرتضی لاریجانی در این دیدار با اشاره به خصوصیات این شهید بزرگوار گفت که نمی‌دانم آقا مرتضی هنگام شهادت چه چیزی دیده بود که اینطور لبخند به لب داشت.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/462689" target="_blank">📅 23:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462688">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e3b781074.mp4?token=rTBFTT-59NIt6dS21yVP9rRVOrXlBwt4NoRrHAFChkrO1qVAUo1_wlw8ZOfO6z9QzmIk5J0x1ugoUxfqMA2CI9CpNl8G9RjnPfxPbzmY9CXEIp9gTdexj9xMNm05KD9U0cxfNZoeUV58jAsXWUE1HRVmEwNyptwVjAWF599UQQlxocmKjd8sZ9U3FH8QSXvGqJJ0YHGQx7gISpPPyrLY8-MTYx0EfrWcT1X8-Uoko583TZV4hbznUBUSL4jE6uzpwhDtg85NcB8dyFnlClYAYjOCoOTpUXDXvDURi22LGz_N4PGLQixSvDNloTp-ufGeMnuYNxNzKL5nzkDIkx04TK99EyxHi2SZyfiph82w-4TMiwxAi3pw6GBcy15aCf7ycSGb1_BBLZgSq-ruydbOLcXobtQuUDlrCYh_XjFWKhJSD9KgXQ7lwiTdbihqABrLA3TrZX0xifVIJk2I6Nk8sBEkhPB4XwpXSp3JQmQYbe6WN4rNWxioW3ZtaJlELHMcIQIcJN-QtCfSZr2oKLsmJBCaX8qB7wK3sP7hWdEbGlXRpmp13twOaJlE0xF6GSCEX5D_46NCL0Ks0bjuxzRr0cZ41cMztdE3HjnmetA7-BSzoqmeLd4uUVP_e5Hhz9uVUd2a9JYnLp9NOX59c3lNaN9FFF5K3SWsQwdDCpMwBCc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e3b781074.mp4?token=rTBFTT-59NIt6dS21yVP9rRVOrXlBwt4NoRrHAFChkrO1qVAUo1_wlw8ZOfO6z9QzmIk5J0x1ugoUxfqMA2CI9CpNl8G9RjnPfxPbzmY9CXEIp9gTdexj9xMNm05KD9U0cxfNZoeUV58jAsXWUE1HRVmEwNyptwVjAWF599UQQlxocmKjd8sZ9U3FH8QSXvGqJJ0YHGQx7gISpPPyrLY8-MTYx0EfrWcT1X8-Uoko583TZV4hbznUBUSL4jE6uzpwhDtg85NcB8dyFnlClYAYjOCoOTpUXDXvDURi22LGz_N4PGLQixSvDNloTp-ufGeMnuYNxNzKL5nzkDIkx04TK99EyxHi2SZyfiph82w-4TMiwxAi3pw6GBcy15aCf7ycSGb1_BBLZgSq-ruydbOLcXobtQuUDlrCYh_XjFWKhJSD9KgXQ7lwiTdbihqABrLA3TrZX0xifVIJk2I6Nk8sBEkhPB4XwpXSp3JQmQYbe6WN4rNWxioW3ZtaJlELHMcIQIcJN-QtCfSZr2oKLsmJBCaX8qB7wK3sP7hWdEbGlXRpmp13twOaJlE0xF6GSCEX5D_46NCL0Ks0bjuxzRr0cZ41cMztdE3HjnmetA7-BSzoqmeLd4uUVP_e5Hhz9uVUd2a9JYnLp9NOX59c3lNaN9FFF5K3SWsQwdDCpMwBCc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج حضور کاشمری‌ها در ۲۰۱ شب حماسه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/462688" target="_blank">📅 23:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462687">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3NtaLgs4PASe0wZjye7Grjcvxjy4IsaZFuwAuoeHgLVEHr96t9c4l-Ta3PmtO1RLaJU0mWQ0EgM2JiIn9F84ngCqGYZxhEaDkuPB5Hcl7SxqhJ2bFh6fUJEYhkiT2C7u3a9px0OmPKHqSKm8SHJUHIX8XcrkTNgkrHkP-TQstaaiaa5E19HstgBGmYZ6Es5JxUpOAQHSidycyJfVi7Nawij6NiVQodlZLpTsZ73W3lKS5I-LA0G91wTi28qdKyvEJJ_ZhjV4TsJlkHW4AKnUlzA4w0f7JJRQSlMxMlHwTQ5roYuuMO3eQYIeR36eUixoX0HNeO3rg9kgJDPx3eBLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: وتوی پیشنویس قطعنامهٔ غیرقانونی آمریکا توسط چین و روسیه، مانع سوء استفاده سیاسی از شورای امنیت شد
🔹
نظم تک‌قطبی که در آن یک طرف با زور و اجبار امتیازگیری می‌کرد، به پایان رسیده است.
🔹
وتوی چین و روسیه سوءاستفاده سیاسی از شورای امنیت را رد کرد و حاکمیت قانون را مجدداً تثبیت نمود.
🔹
ما باید از چندجانبه‌گرایی دفاع کنیم؛ زیرا یک‌جانبه‌گرایی در خدمت منافع هیچ‌کس نیست.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/462687" target="_blank">📅 22:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462686">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
خبرهایی دربارهٔ حملات موشکی یمن به عربستان سعودی
🔹
منابع خبری گزارش دادند در این حملات، «خمیس مشیط» و «ابها» هدف قرار گرفتند.
🔹
سازمان دفاع مدنی سعودی ضمن تأیید این حملات، از فعال شدن آژیرهای خطر در ابها و خمیش مشیط خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/462686" target="_blank">📅 22:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462684">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t3QV8o5B3k-hu4Y3Rz5yZDv6jtZhvoykXAUCfvIHPa9dq3p56J_96GOU7CjWhG5HBEoT3dK4gPjM1h-VAO5juJYafNuyN_MEH5bzmw4QE69VeYsRretMGqC5XVa2GV9_OJFp3nG2OMLYS8YyCRfEEa0ypLK4J3WfdPmKyl-j0E1JdncyGxbJolQMHsWRppxYZnRRRCfFtRN-pqFrcH5Y0SKl-MdXp6GVhRu-DtcYmUBjvV5w_2hIK4HWGc08OWvsFdLzY2h0aaCUIOHL_0DXacC_zW6Aw6sXgK4WTs8P78scAx3BRzidQcigtw2zUjOSmnZXgePB97EVAKYiYjmkHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VrDleV5PqwprKcbkg4pKer-B-vGXFkabaRJY2fyl_brGUURwGY8zbGmanuxbLqpBwrucjxiCZ0omLCyfuIO2slDKnArlbH4PIlK4Ij_fW5wX27jBuxiYVvahXXQIAY1ib1BXbVNT-4rg9fJaIrn9uAbY8bHcGRJTrgKLIKft5k1cQU40CMOW5Ldqz4Y3wkW_GqUcgILkhMoaGRtEgxMU8HTB2MzGz3kwyGhfb_QHaohs_WAwGMntvT5FmD1F0xm085H8ql5sKw8b1jjkqBzpA6MvzkJE9aXYZuDcq-litrG0ZoriP7HJtPwkBP2EQa0UTZOxPTddeHoB0gU_3nu1Rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از حضرت آیت‌الله سیدمجتبی خامنه‌ای رهبر معظم انقلاب اسلامی در جریان عیادت ۲ سال پیش فرزندان رهبر شهید انقلاب از جانبازان پیجری حزب‌الله لبنان
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/462684" target="_blank">📅 22:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462681">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SqjKLIGfMkV5QJWniZrIktA6BBkMpT7iR9gIQ-30c8iaf6bmgz7uLqLP03R_ndqNuoe3hqBuJ1w1jp6f_N203FTheTuGyM0UdiA1uXKcQmqKCjJx-kKYmUgQQYqdjrCpPE6OXGNM8Jp1EoFcoDY2w-e9QYljDigRpipNccgHu6Js7bB2pC1TMzh0NxMavxRDqpPqzVIZOlOlis3_z0zKnTJk7HjM8sC-noe7-qsW2vs55T8v51n52T6y-5ac2aSySZjH8Z2sHW6ZrsP4Wg1NWXkwve-4PZy_NvsvaZ3KqyoxL12JUsY2BJ6j-pNMrKAFbixoDEc3_gSZO_y6wTWf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jPndTy7XTYAU4BQDKSJ8Yk3G0mOEv8l-4_dDIb7ap_jhrY4zkfzkrTVfWB7tMdpi32XX4XPmAfq-I2aduSHXREBygphF54qw7tJRZeYPWsboCAwTwPJ909cfrH87rdHnlRaBQGvWFLI2YxqNvAux-UomgEaa6IKMUaqpj8Tn6IpBmCR4fzjhpkrwydBXhTzjyh_FbmJ6vsHvWGyCJMQl2m8kaxLHIcHW8AleyLFRUku0ZtF3XvnB4mMtxo2fk7sF6QCcWb69-98qwFDght9ZRKf04JKhHHxMejjGdAJSSoUQQG--1Zu1N74eM4MbxbCQNqDMkndtyVT7hfMlpEXuhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fXFE_w-Hp8UJeiutBxr6U2e99o_VS0f2GfkzQnlRZlJKgZxEh0oLqpmXEuz2SVIY3WKVrOAQal0WcdRbd0TP2-iHTPyXjWMB9gZV2RyWUWFsj9apo6JFXsKHGbq9A6XCq1OTCKOrtlqNl-A40CiBboPcis-4zcKYFgm-9DhAl2Y5WpLq_wSQbTO1NTSym8oDnp4oisP3Oee3dQ60d10ojKqijpuSZlxKAsGJzjFogDV3dx2jj7GsUAUkJScvDPA5XkhE82zXla7yCORF6xRNe8P5DTsTM4Vhmn0LjG-txxiZratGViuIW6ceyC2r4_QioOIE1S0tSdY2vhLXtK2WXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گزارش‌ها از سقوط اف۱۶ در آمریکا
🔹
رسانه‌های غیررسمی از سقوط جنگنده اف۱۶ آمریکایی در شمال ایالت میشیگان خبر می‌دهند.
🔸
تصاویر منتسب به این حادثه در فضای مجازی منتشر شده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/462681" target="_blank">📅 22:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462680">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تحریم‌های جدید آمریکا علیه ایران
🔹
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (اوفک) اعلام کرد ۳ فرد و ۲ نهاد ایرانی، از جمله پلتفرم معاملاتی ارزهای دیجیتال بیت‌بانک بابک زنجانی را به فهرست تحریم‌های خود افزوده است.
🔸
وزارت خزانه‌داری همچنین افراد و نهادهایی از کوبا را نیز تحریم نمود.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/462680" target="_blank">📅 22:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462679">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyO9Dfr6zIkdt0qF0eFRFD4UX0hx1mx7DHVTCq1ExEPl2AeK23ZHP8htrsgc4K8vCkdR7yLuEBEVWZlPBTTNydbnSuyoh9-Pvlz8oaA1OD7r5JcwRFAGgirl6wf1xHoSkTUH9AxAl8KUWt80tAKjbbWB_sIbkAGeduDzY24j3Tog8eqQtsiqN3EgLKeQAJssruAy9RqryUe-6VsSA2JjzkvLOqsft14VQxGbxyCHp6HBj4klccdzka6te8kmJe5-BPh9IKBPm2s5KJd1k5_KlO21MAj6DNy-98cGpIcGQBsTn54-QI_tjZkaufAJrjSUgF0Fp-08GJMOup-E8QWgpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی نیروهای مسلح یمن: جنگنده‌های سعودی در ۲۴ ساعت گذشته، ۳۷ حملهٔ هوایی به استان‌های تعز و حجه انجام دادند که به کشته و زخمی‌شدن غیرنظامیان منجر شد
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/462679" target="_blank">📅 22:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462678">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee92e48af.mp4?token=FZGgN81CNdLo_eFY2qSvlNCYJ5Ci7hY4JTUw1GPSYlZLc3ou-aIy2dLVlHh9FrsKMG0Tsc2kSfj26EtVo7qymxXDLXNUZ-oynq2oAiGv-wDzlSg44et_y11gvgNmlXzpPzmW1XSgM_OvvP_BpzI4Gp_E34XrHjZQS7HraJdVdrwWPw3RzO6GAvgkS3EHjuMtw334Dz31gY41enQLDnBVGRK3PlXIwVEyKRUPF6ehFbwjHyd7xtKptQU-HZAX-djvQDYneWLKxh0FqbIopXryMXs-0RrU27rn4GTGh77MwUkxRT5fetl6Pxj84AkBgSmgN3yRaTO_kRXvVLNzEDq1lEBNCWuVRNVLFRcBCx_TNypNMUlmqR_kpMSXTq6Odl4nFmEjPPehhjDJqeaQghDYhOS-bGq_xfRT4-GX2qASXFIgazv_q6URyNK-gy2RWrsF54p4FLnod5164B_YEByOvUCj-kIEp3pUD1tfywpFtVbuWs1-OfRBfGlvT437_wfe1n21l5_j46pUYhkxIDxxU8SrYj2jarx99DbMplb69_vcdpwaCuaVW-NTXzn63zWECExsp0LNNYTZd4j7NS_Rtwrn2LC3fT7CWB1Cqxd55XoRuhOz7-dKn4NXwdAtdLh4S9gRazkyKIcOmIdFoGyafAEq5JqmiklGbFGD5ykdi_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee92e48af.mp4?token=FZGgN81CNdLo_eFY2qSvlNCYJ5Ci7hY4JTUw1GPSYlZLc3ou-aIy2dLVlHh9FrsKMG0Tsc2kSfj26EtVo7qymxXDLXNUZ-oynq2oAiGv-wDzlSg44et_y11gvgNmlXzpPzmW1XSgM_OvvP_BpzI4Gp_E34XrHjZQS7HraJdVdrwWPw3RzO6GAvgkS3EHjuMtw334Dz31gY41enQLDnBVGRK3PlXIwVEyKRUPF6ehFbwjHyd7xtKptQU-HZAX-djvQDYneWLKxh0FqbIopXryMXs-0RrU27rn4GTGh77MwUkxRT5fetl6Pxj84AkBgSmgN3yRaTO_kRXvVLNzEDq1lEBNCWuVRNVLFRcBCx_TNypNMUlmqR_kpMSXTq6Odl4nFmEjPPehhjDJqeaQghDYhOS-bGq_xfRT4-GX2qASXFIgazv_q6URyNK-gy2RWrsF54p4FLnod5164B_YEByOvUCj-kIEp3pUD1tfywpFtVbuWs1-OfRBfGlvT437_wfe1n21l5_j46pUYhkxIDxxU8SrYj2jarx99DbMplb69_vcdpwaCuaVW-NTXzn63zWECExsp0LNNYTZd4j7NS_Rtwrn2LC3fT7CWB1Cqxd55XoRuhOz7-dKn4NXwdAtdLh4S9gRazkyKIcOmIdFoGyafAEq5JqmiklGbFGD5ykdi_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۰۱ شب میدان داری مردم مراغه برای وطن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/462678" target="_blank">📅 22:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462677">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30af9bb34f.mp4?token=bzbOSkBVPogX9FeutpzdxMjj_KGy6StqQXbgxcHeAaJm8t23pyDHN3SE-lvJFkQ2t4NteosAwFtYLsIJhAzC7yQoOOhUHDZzNEhGfppZglaM81e7fWHEUgKTp6zfikF4vb2CsjPS9WVjdhjikR4Rk2yH-kqpvKmlNuT907k-9eG3MoHzsdGoyQivak4lpfbDqOjEIvnYdomIffcoH2NyNBP1Vkem9RdoGWIW0Z5OUEar2m5T6xRnFneNiDiOVRj6e6V5qdfXsqIQICjwjrS7EbmlhDbkz0dcx7ZOlBlTaJIvY2Hbuyc1NGGARkHO_cV4yylA59jxVsmd9hby_f4WpJI1g8Yf5lL-ZnPePRk0LbweBTZeGP63upwLtk3Y-Jpdbm_9NQO2jwrBU9oFcKyEsX0p5g3sRQL5OH9WsbBAEAWx2ATpWIrLYXS6pCju0zRv_ZGO71CgZxlCtD9dklUIss7V3dhGxyqeezeHgluEkdRAKc2i2v2Og_zdyw1kfvZsyrDabTjWQDLmXiTGxK4ZTXPToz1IVxduR2gL6cMeoK0t3xcmxrR7K9pM7XC_BoVXYZ1OJp4QR6hzlCqb931pRQGyHhIErzDXdN-KJ2jC3gLpDL2sSwjjePEKPVPCJznUYrgkYVNcCs0EYYaRxWHmktraKLfiPo1LfvBfrT49C4c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30af9bb34f.mp4?token=bzbOSkBVPogX9FeutpzdxMjj_KGy6StqQXbgxcHeAaJm8t23pyDHN3SE-lvJFkQ2t4NteosAwFtYLsIJhAzC7yQoOOhUHDZzNEhGfppZglaM81e7fWHEUgKTp6zfikF4vb2CsjPS9WVjdhjikR4Rk2yH-kqpvKmlNuT907k-9eG3MoHzsdGoyQivak4lpfbDqOjEIvnYdomIffcoH2NyNBP1Vkem9RdoGWIW0Z5OUEar2m5T6xRnFneNiDiOVRj6e6V5qdfXsqIQICjwjrS7EbmlhDbkz0dcx7ZOlBlTaJIvY2Hbuyc1NGGARkHO_cV4yylA59jxVsmd9hby_f4WpJI1g8Yf5lL-ZnPePRk0LbweBTZeGP63upwLtk3Y-Jpdbm_9NQO2jwrBU9oFcKyEsX0p5g3sRQL5OH9WsbBAEAWx2ATpWIrLYXS6pCju0zRv_ZGO71CgZxlCtD9dklUIss7V3dhGxyqeezeHgluEkdRAKc2i2v2Og_zdyw1kfvZsyrDabTjWQDLmXiTGxK4ZTXPToz1IVxduR2gL6cMeoK0t3xcmxrR7K9pM7XC_BoVXYZ1OJp4QR6hzlCqb931pRQGyHhIErzDXdN-KJ2jC3gLpDL2sSwjjePEKPVPCJznUYrgkYVNcCs0EYYaRxWHmktraKLfiPo1LfvBfrT49C4c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور مردم در میدان، نقشهٔ دشمن را ناکام گذاشت
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/462677" target="_blank">📅 22:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462676">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
چند روز پیش به درخواست دختر نوجوانم، برایش یک چادر نماز گل‌گلی و زیبا دوختم. اما به محض اینکه کار تمام شد، گفت: «نمی‌خواهم مثل زندانی‌ها باشم.» لطفاً
مجرمان را با لباس متناسب شأن خودشان به مردم نشان دهید
، نه با پوششی که نماد یکی از مقدس‌ترین اعمال دینی ماست.
🔹
بنده
متقاضی پروژه ۸۱۰۰ واحدی مسکن ملی اراک
هستم. از سال ۱۴۰۰ تاکنون برای تأمین آورده، حتی طلاهای خود را فروختم و حدود ۱۳۰ میلیون تومان واریز کردم. تا قبل از سال ۱۴۰۵ نیز برای تأمین مبالغی که راه و شهرسازی اعلام می‌کرد، ماشینم را فروختم. تمام واریزی‌های من به‌موقع و حتی زودتر از مهلت‌های اعلام‌شده انجام شده است. قرار بود این واحدها حداکثر طی دو سال و با حدود ۳۰۰ تا ۴۰۰ میلیون تومان آورده متقاضی، به‌علاوه ۳۵۰ میلیون تومان تسهیلات بانکی، تحویل داده شوند. اما
حالا صحبت از هزینه‌ای حدود ۴ میلیارد تومان است
. به خدا مستأجرم، یک فرزند دارم و دیگر توان تأمین این مبالغ را ندارم.
🔹
برای تمدید
بیمه بدنه
خودروی سمند سورن مدل ۱۴۰۱ به بیمه ایران مراجعه کردم. گفتند باید پوشش «جبران زیان وارده به خودروهای نامتعارف» را هم به بیمه‌نامه اضافه کنم. وقتی گفتم خودرو من سمند سورن است و خودروی لوکس یا نامتعارفی نیست، پاسخ دادند طبق قانون
چون ارزش خودرو بیش از یک میلیارد تومان شده، نامتعارف محسوب می‌شود
. سؤال ما این است که چرا باید خودرویی مانند سمند سورن به‌دلیل افزایش قیمت خودرو، نامتعارف محسوب شود؟ آیا این قانون با شرایط و قیمت‌های امروز خودرو تناسب دارد؟
🔹
قسمت میانی
جاده خوشنام ملارد به سمت شهرک ناز فردیس
، به طول حدود ۴۰۰ متر،
بین دو استان تهران و البرز بلاتکلیف مانده
است. با وجود اینکه روزانه هزاران خودرو از این مسیر عبور می‌کنند، آسفالت این بخش به‌شدت تخریب شده و باعث آسیب جدی به خودروها و بروز تصادفات زیادی شده است. متأسفانه مسئولان هر یک از دو استان رسیدگی به این مسیر را بر عهده استان دیگر می‌گذارند و در این میان، مردم متحمل خسارت و هزینه‌های سنگین تعمیر خودرو می‌شوند.
🔹
من از
زاهدان
هستم و مشکل ما در این شهر،
وضعیت نامناسب نظافت و بهداشت شهری
است. سال‌هاست با این مشکل مواجهیم؛ زباله‌ها به‌موقع و به‌خوبی جمع‌آوری نمی‌شوند و بوی تعفن آب‌های راکد و تجمع زباله در جوی‌ها، به‌ویژه در خیابان معلم، محدوده باغ خانواده، واقعاً آزاردهنده شده است. وضعیت سرویس اتوبوس شهری نیز نابسامان است و مردم با مشکلات زیادی در زمینه حمل‌ونقل عمومی مواجه هستند.
🔹
شرکت
مدیران خودرو
از پذیرش خودروهای دارای گارانتی، به بهانه نبود قطعات خودداری می‌کند و در این زمینه نیز پاسخ‌گوی مشتریان نیست. خودروها معمولاً هفته‌ها در بلاتکلیفی کامل باقی می‌مانند و مالکان نمی‌دانند چه زمانی مشکل خودروشان برطرف خواهد شد. لطفاً با ارتباط‌گیری با مسئولان ذی‌ربط، این موضوع را پیگیری و خودروساز را ملزم به انجام
تعهدات گارانتی و پاسخ‌گویی به مشتریان
کنید.
🔹
مدتی است در
تهران
قرار است برخی منازل به فیبر نوری مجهز شوند. سؤال ما این است که آیا توسعه و
واگذاری خطوط مخابراتی و فیبر نوری
وظیفه مخابرات نیست؟ پس چرا شرکت‌های خصوصی برای انجام این کار از مردم مبالغ بالایی دریافت می‌کنند؟
🔹
از استان قزوین، شهر
بویین‌زهرا
مزاحم شما شدم. متأسفانه در پروژه
مسکن ملی ۵۴۴ واحدی
که در انتهای بلوار آزادگان قرار دارد هنوز از کابل تلفن و کابل فیبر نوری خبری نیست و آنتن‌دهی اینترنت ایرانسل نیز بسیار نامناسب است. خواهشمندیم مسئولان برای
تأمین امکانات ارتباطی
این پروژه و رفع مشکل آنتن‌دهی اینترنت اقدام کنند.
🔹
در
پارک شاپوری خرم‌آباد
، درِ سرویس‌های بهداشتی شب‌ها و درست در ساعات اوج شلوغی پارک بسته است. بچه‌ای که چند ساعت در پارک مشغول بازی و تفریح است، طبیعتاً ممکن است نیاز به
سرویس بهداشتی
پیدا کند؛ در این شرایط باید کجا برود؟
🔹
ما
کارمندان
معمولاً سالی ۱۰ روز تا دو هفته مرخصی می‌گیریم تا به مسافرت برویم. با توجه به هزینه بالای بلیت هواپیما و قطار به‌خصوص برای خانواده‌ای ۶ نفره، عملاً امکان استفاده از این وسایل حمل‌ونقل را نداریم و مجبوریم با خودروی شخصی سفر کنیم. متأسفانه با سهمیه سوخت موجود در کارت‌های شخصی و محدودیت ا
ستفاده از کارت‌های سوخت جایگاه‌ها در سفرها
با مشکل جدی مواجه شده‌ایم و مجبوریم برای استفاده از کارت جایگاه، مدام از این و آن درخواست کنیم. دولت باید برای فصل سفر برنامه و تدبیر ویژه‌ای در نظر بگیرد.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/462676" target="_blank">📅 22:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462675">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GglIBzNETOLBUeEcgcQN0djB3uu7yCbhR_JJO7OPtg2itLyGmiCInsWYijPA_kfEZc2warC5H0S1R97TTEXQlNCfY2JB66XaTAiUZqUnxZrdBiAsInGyxo6vmvKAU8UVLeD3rI-BR6MJW5ZfrWkdc8hlxMpcpzV8Y1opSQu8RF_6zLZk1WjRdtXWV_LDztD57-wCWSNlpEm4vrnHsWN8P_NkQTnqPmNM1RMylUYOlE3avm0TZMUvJkm1WCQvpkOLDsj9zdS3b32Nc12ALjJ1isXvybDY9fAEYE1TQ0aR6Wln2Uez6c77othFvp4FLFBCWRblEo1CgHRj179K_2XLgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرلشکر صفوی: یمن افسانهٔ شکست‌ناپذیری آمریکا را برای همیشه دفن کرد
🔹
از صنعا تا باب‌المندب، یمن با ایمان و اراده، افسانه شکست‌ناپذیری آمریکا را برای همیشه دفن کرد. این فتح مبارک را به ملت قهرمان یمن و فرماندهان انصارالله تبریک می‌گویم.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/462675" target="_blank">📅 22:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462674">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/935eb96623.mp4?token=hitrO5vshBpIBOPwJkElb8U8BQfqJsaLMuQl0P7hkwIg1wkqwpSo7X8fZVURWUt4bEUPXtqDT-2WKbX0BPsnf7tC7OeTkrwZ6XtsUX5iuoB_ArtVyc95zitZnl_83neVGGonjgLtT21_TJpavzHuQ0CRgzGF0VCe-n9YCJP7tTlFCwiaySKZ8QTvzTkz_JWijcWmzjVtEZpx2acFr8zMyaWv-mOH_X65WEvCFsPY-gKAnjNnkg4Zj9yoREMd2Au82IEcz15eHeTevx-5FKfOgrEl185nAz_5yWhluezYbDwNz1xlZAwWDsN9erAGCUgCm4weys6-irHtkaxSnekVQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/935eb96623.mp4?token=hitrO5vshBpIBOPwJkElb8U8BQfqJsaLMuQl0P7hkwIg1wkqwpSo7X8fZVURWUt4bEUPXtqDT-2WKbX0BPsnf7tC7OeTkrwZ6XtsUX5iuoB_ArtVyc95zitZnl_83neVGGonjgLtT21_TJpavzHuQ0CRgzGF0VCe-n9YCJP7tTlFCwiaySKZ8QTvzTkz_JWijcWmzjVtEZpx2acFr8zMyaWv-mOH_X65WEvCFsPY-gKAnjNnkg4Zj9yoREMd2Au82IEcz15eHeTevx-5FKfOgrEl185nAz_5yWhluezYbDwNz1xlZAwWDsN9erAGCUgCm4weys6-irHtkaxSnekVQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۰۱ شب گذشت؛ اما صف مردم برای ایستادگی هنوز ادامه دارد
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/462674" target="_blank">📅 21:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462673">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3df65ffe6.mp4?token=k_8WpGGj2gn4LrlJaML_QoLDN7EMa40eYSeCA7hOxH-MRqsHVTRNGXbRN8jPQYUcBzWUYcGET8RwAVmTi5iEfGAB05Ov20svUXDt1WoqC2jvWLdwM79yg0l6O_GNcn1zAEB_8UvmmLSxO-7KYWwag3vgl0x9StOqf8KRqPJNVOj-MW2lTCeZFw0XCu0C_OZY43aNSwCNYOJ49D25nZu5sriDo64e6zQbiibqXQTR1KRryyKMb3zfH3A4tvx7sPyhvl4t5Z1cauDPP0muKW3-WBt0YTF3KbghRfA2gnTNDXxoa_5LkPgdEkfXkJsFESQnV10mpDwaIERsjxaOMurgt0VbbwXrQ9dApvNL-FucY4CT-qNcIoWX00-EazwzJNqhfTAMWESGerVIFplk_44ZcaLAwrTXsFnSFGqf1gw57Om7gZicp9pW4Atluzzow4PEp-qsnm0aoEsws-HYtyDVXf35oHWlQ_641Nfq6_7wcq3YJSaaJLBkqXuEcQ6cnXbtPFMpPBucFu3KxHfRsWMl6jUA0ajNWPPXnTNs4fWJxZhSjavSuZK5xRYlvXmVaE4DxeXm1S3utZ6GKY2rxqx-mjsLxpw1WxGGWaHkJK3YQOwsj-7bXc4BdABO_OgjlvVdpvr1PILKFY_wtnV1OgiQBfRnnwSxO7mLgnXWs40n8qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3df65ffe6.mp4?token=k_8WpGGj2gn4LrlJaML_QoLDN7EMa40eYSeCA7hOxH-MRqsHVTRNGXbRN8jPQYUcBzWUYcGET8RwAVmTi5iEfGAB05Ov20svUXDt1WoqC2jvWLdwM79yg0l6O_GNcn1zAEB_8UvmmLSxO-7KYWwag3vgl0x9StOqf8KRqPJNVOj-MW2lTCeZFw0XCu0C_OZY43aNSwCNYOJ49D25nZu5sriDo64e6zQbiibqXQTR1KRryyKMb3zfH3A4tvx7sPyhvl4t5Z1cauDPP0muKW3-WBt0YTF3KbghRfA2gnTNDXxoa_5LkPgdEkfXkJsFESQnV10mpDwaIERsjxaOMurgt0VbbwXrQ9dApvNL-FucY4CT-qNcIoWX00-EazwzJNqhfTAMWESGerVIFplk_44ZcaLAwrTXsFnSFGqf1gw57Om7gZicp9pW4Atluzzow4PEp-qsnm0aoEsws-HYtyDVXf35oHWlQ_641Nfq6_7wcq3YJSaaJLBkqXuEcQ6cnXbtPFMpPBucFu3KxHfRsWMl6jUA0ajNWPPXnTNs4fWJxZhSjavSuZK5xRYlvXmVaE4DxeXm1S3utZ6GKY2rxqx-mjsLxpw1WxGGWaHkJK3YQOwsj-7bXc4BdABO_OgjlvVdpvr1PILKFY_wtnV1OgiQBfRnnwSxO7mLgnXWs40n8qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از دیدارهای صمیمانهٔ خانواده‌های معظم شهدا با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/462673" target="_blank">📅 21:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462672">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آمریکا به عربستان اف-۳۵ می‌فروشد
🔹
آمریکا ۴۸ فروند جنگنده اف-۳۵ به عربستان سعودی می‌فروشد؛ معامله‌ای به ارزش حداکثر ۲۴.۳ میلیارد دلار که اولین خرید اف-۳۵ توسط عربستان در تاریخ است.
🔸
وزارت خارجهٔ آمریکا امروز کنگره را در جریان این معامله گذاشت و آن را برای «بهبود امنیت یک متحد اصلی غیرناتو» ضروری خواند.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/462672" target="_blank">📅 21:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462671">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a8043bfa4.mp4?token=buUpzfb2u_DJr6qnF1WI-rBguLGEZcEqJnHuUNmzpoblIpiotlAsvunkM3RdSzZ7bD3Dzeo3TeQlz-Cz-QPsg8lmwY7qDi6pX3KlsFc9Wlt6v2EvwFXKPo688RK9Df7KG-JqxU9SdyaD2Hae8LG0UE7JTfa4vVNQlocbRVvm9SWmLToLZEwRY_Hkzsnx8WIMKXlr_V0IIvf2-ygpcs2jBjibwkxjBAltZsYx5xjl6K04R3jx3UmsxjbMgcfajRjJ-DDO96xqdCO-5irA9nuE2nHGNSUJpt5fysfI-0xpDymHgNfyZ6Ze6cemUGk2OA7eHS27HBJcL6FgrFaMXRbpqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a8043bfa4.mp4?token=buUpzfb2u_DJr6qnF1WI-rBguLGEZcEqJnHuUNmzpoblIpiotlAsvunkM3RdSzZ7bD3Dzeo3TeQlz-Cz-QPsg8lmwY7qDi6pX3KlsFc9Wlt6v2EvwFXKPo688RK9Df7KG-JqxU9SdyaD2Hae8LG0UE7JTfa4vVNQlocbRVvm9SWmLToLZEwRY_Hkzsnx8WIMKXlr_V0IIvf2-ygpcs2jBjibwkxjBAltZsYx5xjl6K04R3jx3UmsxjbMgcfajRjJ-DDO96xqdCO-5irA9nuE2nHGNSUJpt5fysfI-0xpDymHgNfyZ6Ze6cemUGk2OA7eHS27HBJcL6FgrFaMXRbpqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم شهرکرد در شب ۲۰۱؛ هم‌صدا با یمن
شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/462671" target="_blank">📅 21:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462670">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbNlH4QBnYOtproC9RO6kjw_owqOl2DBNtqRs7A4Egvaw3zsBh7q968dCxtlBfHjm2JPbvF5WNsmgIk8VMYcjyjPREVTHdZS9GUVrrOFywmHy4xA-KIZ7jY1S-sQh78rYyvyOp5zW5qZmc7ISReGdPg8srMnhJCDjKOYdRtAv5jb1lM3Ua4HiDBrs58p902fzeETODa8ucWG6EQM9ArejLdSDl1hzr7xo7EVe0iT83E-qiVlB_gXfFQ9wBh5iKBAI5XGoPGm4_qy5_7xcDEYM5PmCmztMPTe8eCZ55zc5PkuNEcx6K0L5AZcXdLvrntYx_no__6KkT96iPad0He8-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جبلی: فرهنگ‌سازی و مطالبه‌گری اقتصادی در رسانه ملی تقویت می‌شود
🔹
رئیس صداوسیما: در سال‌های گذشته، رسانه ملی در موضوعاتی همچون اجرای قانون مجوزهای کسب‌وکار و پنجره واحد خدمات دولت الکترونیک نقش مطالبه‌گرانه داشته و در موضوع ناترازی انرژی نیز با تمرکز بر فرهنگ‌سازی مصرف بهینه توانسته است به کاهش مصرف کمک کند.
🔹
این تجربه‌ها مسئولیت رسانه ملی را سنگین‌تر می‌کند؛ اگر با پیگیری، تمرکز و استفاده از همه ظرفیت‌ها توانسته‌ایم در یک موضوع خاص به حل مشکل کمک کنیم، می‌توانیم در سایر مسائل نیز نقش مؤثرتری ایفا کنیم.
🔹
وظیفهٔ رسانه ملی فرهنگ‌سازی، مطالبه‌گری و معرفی ظرفیت‌ها و دستاوردهاست و در همین راستا پیشنهاد شده است در شبکه‌های اصلی، برنامه‌های تخصصی و ثابت برای پیگیری مسائل حوزه‌های مختلف از جمله اقتصاد، صنعت، کشاورزی، معدن و مسائل مرزی استان‌ها ایجاد شود.
🔹
در کنار برنامه‌های تبلیغاتی، باید برنامه‌های مطالبه‌گرانه اقتصادی، فرهنگ‌سازی، بازارسازی و معرفی دستاوردهای کشور نیز تقویت شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/462670" target="_blank">📅 21:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462669">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb326ea94.mp4?token=Y7iRc_a9h_WIELbaQpK_vxJtjVafXe5Ax_tKq2MPv2WYTyvH1HUIfh0QQQkOXD8oGQYOUX4doC6lKDilbWypX2XbrYfDjMsMP9YcXrNJOhWuQS4YocTUxMb7vvpjhBt-4I5NH8BgP2P12RwFwrLMgORZ4OFjdluYV3vJLNXKBrKHzBYb7kpyyxHcXXWCHPUnLjV_WgmiTHnJCs2207S18gxzyX1FMhgHGjIsGEqV5lBWDCmbEiqzLQUhgaDDCWwvRsekCYuIloVPlWp9rjV0b-QXjDh7QrH4qEI6CUnmUFXIoe4nCa0qGMlKxyTIo6LSTjP6FnBcWdeJmuDTzv2sfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb326ea94.mp4?token=Y7iRc_a9h_WIELbaQpK_vxJtjVafXe5Ax_tKq2MPv2WYTyvH1HUIfh0QQQkOXD8oGQYOUX4doC6lKDilbWypX2XbrYfDjMsMP9YcXrNJOhWuQS4YocTUxMb7vvpjhBt-4I5NH8BgP2P12RwFwrLMgORZ4OFjdluYV3vJLNXKBrKHzBYb7kpyyxHcXXWCHPUnLjV_WgmiTHnJCs2207S18gxzyX1FMhgHGjIsGEqV5lBWDCmbEiqzLQUhgaDDCWwvRsekCYuIloVPlWp9rjV0b-QXjDh7QrH4qEI6CUnmUFXIoe4nCa0qGMlKxyTIo6LSTjP6FnBcWdeJmuDTzv2sfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شام شب ۲۰۰ فرق داشت!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/462669" target="_blank">📅 21:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462668">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae1110a925.mp4?token=Hj4APfAy0vF7Pw8-qKWa-xH_Zf22yphcUIp28x3pE9hbsLzqENhk47UWzhWPaISFIoBomHSDiASA0fpOBOTC0MYTl05c_xkT9SKjJHzf10xSX4GAKvt7MD2Rc9wOSiUeCvXRKhTojAxkd1Y9rWEq6F5WfUkLc4Gv7nPaMfnJBAJfkghVRUEaymSEI9OTpwLFkSV7lq_uEg9vaT5YjT-iF47K5pjzPZBAb8G7KgqQapis2VwDbvkTP3J_foG203KLRu_m2fnZLgJGaix5SGFwSjf9NcNsjnDMJ99f68WYv79IsszVaLr6RI4jh5kiV39qvaInfKlFu2nAlRsf7-h8fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae1110a925.mp4?token=Hj4APfAy0vF7Pw8-qKWa-xH_Zf22yphcUIp28x3pE9hbsLzqENhk47UWzhWPaISFIoBomHSDiASA0fpOBOTC0MYTl05c_xkT9SKjJHzf10xSX4GAKvt7MD2Rc9wOSiUeCvXRKhTojAxkd1Y9rWEq6F5WfUkLc4Gv7nPaMfnJBAJfkghVRUEaymSEI9OTpwLFkSV7lq_uEg9vaT5YjT-iF47K5pjzPZBAb8G7KgqQapis2VwDbvkTP3J_foG203KLRu_m2fnZLgJGaix5SGFwSjf9NcNsjnDMJ99f68WYv79IsszVaLr6RI4jh5kiV39qvaInfKlFu2nAlRsf7-h8fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام میرهاشم حسینی: بدترین طلسم زندگی گاهی همین زبان آدم است؛ یک تهمت، غیبت یا بدگویی می‌تواند زندگی را به هم بریزد
🔹
زخم زبان دردناک‌تر و اثرگذارتر از زخم شمشیر است.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/462668" target="_blank">📅 21:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462667">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e436cc3d33.mp4?token=GxpmtVlcnysPB1wSeLVibp1MBiiEzZHdy8OWL1-1KKOPgzO7zJhSqzOc9_3w3WETxD7RJ2Z5CHx2wh1SIdXp9co-jZKcQb-5UHLme_y7gBQk92NBtBP4dyIeCCmk7EQsCUE9YoD94w4tmylRG3ZL9JqjUAk-bHbL7BthAdb8ewFUuLw9-uDzN7d-TPIzrvvFBPHajNiBmvRLQ8p7rPzI3Ju_OHx3DjlA5IbMQLsV-mxsAMnxqMuGw0HUSZeYwjLrG2Gm5z8vhj_iWmMHL43Y9IM8AoaG04evouxQH5sokUAyVaqbm0FMX_Tk_3C_YSA2OLe__6q8t2ebjKA5n2CDcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e436cc3d33.mp4?token=GxpmtVlcnysPB1wSeLVibp1MBiiEzZHdy8OWL1-1KKOPgzO7zJhSqzOc9_3w3WETxD7RJ2Z5CHx2wh1SIdXp9co-jZKcQb-5UHLme_y7gBQk92NBtBP4dyIeCCmk7EQsCUE9YoD94w4tmylRG3ZL9JqjUAk-bHbL7BthAdb8ewFUuLw9-uDzN7d-TPIzrvvFBPHajNiBmvRLQ8p7rPzI3Ju_OHx3DjlA5IbMQLsV-mxsAMnxqMuGw0HUSZeYwjLrG2Gm5z8vhj_iWmMHL43Y9IM8AoaG04evouxQH5sokUAyVaqbm0FMX_Tk_3C_YSA2OLe__6q8t2ebjKA5n2CDcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهریور با سفرهای آخرش می‌چسبه
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/462667" target="_blank">📅 21:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462666">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8246fc0ad6.mp4?token=tDwpmHVMKDaQwJpJAIqcVIQxiEEy9MyPAy3StnmF7mfilEu6WcZ6SW6w-2zoqL5Tl82ravQ2GIZH8o9tK0po9MSvluzGbDdUvQZaQPDBLXAFp4Vi8Y2jlwZIkDrh7GoLDUqujY4-9gfi5OtxN_CSLFvjowe_FJK_RhuSvwm8sWOy8qBgel5Tq5YckTwep1_O0NM9rc01NO9wwDTbmMpiJEFPsz6RvZtbhefLdpgmZWBpdjMHE5TVC37kFHqlBGp__Ts7Ft0yvf3zyrPXjoxkPS5EmApLyxzd7BUvIWjza6F8tdar16yIXXAT9mqA0YcrLnWkx29aA7m0rxMXe5mzfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8246fc0ad6.mp4?token=tDwpmHVMKDaQwJpJAIqcVIQxiEEy9MyPAy3StnmF7mfilEu6WcZ6SW6w-2zoqL5Tl82ravQ2GIZH8o9tK0po9MSvluzGbDdUvQZaQPDBLXAFp4Vi8Y2jlwZIkDrh7GoLDUqujY4-9gfi5OtxN_CSLFvjowe_FJK_RhuSvwm8sWOy8qBgel5Tq5YckTwep1_O0NM9rc01NO9wwDTbmMpiJEFPsz6RvZtbhefLdpgmZWBpdjMHE5TVC37kFHqlBGp__Ts7Ft0yvf3zyrPXjoxkPS5EmApLyxzd7BUvIWjza6F8tdar16yIXXAT9mqA0YcrLnWkx29aA7m0rxMXe5mzfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاظمی، سخنگوی قوه قضاییه: پروندهٔ ترور امام شهید به دادگاه می‌رود
🔹
برای ۱۵۹ تن از مقامات ارشد سیاسی و نظامی دولت آمریکا و رژیم صهیونیستی کیفرخواست صادر شده است.
🔹
۶۷ نفر از این مقامات اسرائیلی و ۹۲ نفر آمریکایی هستد.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/462666" target="_blank">📅 21:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462665">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2089efc431.mp4?token=glec24HgcdY3W5f89fmhcQdwA4lNM2fivmtutxh18o7iEZyyGuvKz0mu0SblAnKBEQt2lkc5YEy_MQTQ4M6BiO_rC0TpfehsCTo5eAo0BeFHwWISh4bJpgw4CrYDmLjRaZervV20xGoMaenCW5po7MTkMrOi0DHOtKP5_EUsvcDukktmBsdUE0lfDNnjWaiDbu1PbI4PI9E5dNrmKt5ZnJujQZQXbQr6Sal7dbadKhrHboAgX9hKVB2wpfKkIzGrPSiWaAsqB4iJF1am0SDWevu8QiRtGHrJHx8o99jaEal5Uo7yMQt-rpJ-IMGpn-p6MrGYSNqHhAFGYbHHrg8k0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2089efc431.mp4?token=glec24HgcdY3W5f89fmhcQdwA4lNM2fivmtutxh18o7iEZyyGuvKz0mu0SblAnKBEQt2lkc5YEy_MQTQ4M6BiO_rC0TpfehsCTo5eAo0BeFHwWISh4bJpgw4CrYDmLjRaZervV20xGoMaenCW5po7MTkMrOi0DHOtKP5_EUsvcDukktmBsdUE0lfDNnjWaiDbu1PbI4PI9E5dNrmKt5ZnJujQZQXbQr6Sal7dbadKhrHboAgX9hKVB2wpfKkIzGrPSiWaAsqB4iJF1am0SDWevu8QiRtGHrJHx8o99jaEal5Uo7yMQt-rpJ-IMGpn-p6MrGYSNqHhAFGYbHHrg8k0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی براندازها برای موج‌سواری سراغ بنزین می‌روند
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/462665" target="_blank">📅 20:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462664">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🎥
در ۲۰۰ شب حضور مردم، خیابان‌ها چه روایتی داشتند؟
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/462664" target="_blank">📅 20:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462663">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d30f65bde.mp4?token=i3m-xSh5dHd9omY2uDgQ2sCL57hH5ZlLkv7FNaN6xEXeW4_HA3ZH1tC-Wi8f1UsFTGw86PzWirDVx51O27x3PrqAYR4eQ64JjTWyIGBCWalLLUNWCMexPUCEuGdAZ2wlg1QhVSLpwbwfZxO_EdSRX1C6U5ur7brZhe5Pqmq4sVOJsxKtd4QyGzqJLYeBUQawSHou4bDxEs8-X2p2SlfuGYkA6T7BswZ0bWzJiH4x_SEW9MxYyCdzTQJR-2xQe9YepaMTYhOhmm_HHYiC5gt27Jb-WEdA9wy_vMG24-k3mklkTzwlGQUpMiNSJjY8PTlSMNN8eTs1XTeqkdAStoqBKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d30f65bde.mp4?token=i3m-xSh5dHd9omY2uDgQ2sCL57hH5ZlLkv7FNaN6xEXeW4_HA3ZH1tC-Wi8f1UsFTGw86PzWirDVx51O27x3PrqAYR4eQ64JjTWyIGBCWalLLUNWCMexPUCEuGdAZ2wlg1QhVSLpwbwfZxO_EdSRX1C6U5ur7brZhe5Pqmq4sVOJsxKtd4QyGzqJLYeBUQawSHou4bDxEs8-X2p2SlfuGYkA6T7BswZ0bWzJiH4x_SEW9MxYyCdzTQJR-2xQe9YepaMTYhOhmm_HHYiC5gt27Jb-WEdA9wy_vMG24-k3mklkTzwlGQUpMiNSJjY8PTlSMNN8eTs1XTeqkdAStoqBKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان اداری و استخدامی: همهٔ مدیران در تمام سطوح نیازمند آموزش هستند  @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/462663" target="_blank">📅 20:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462662">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/343ca3619f.mp4?token=a-eEY13ASMSuGt8_0eQgg09XU4q7ilg6q0SD9r-a6H0-WmiJbNgfnkgo00dSoVt3nabr5oJUabHT_m8_97leGu4M0pm89uZ10N-REWRzE3oTjcJU23aETUipRlilmr37WbObyBa_gFJ04MO4qY1rPec_vggCnGkJUBxutyoOQEOXw06U4MoTjnPXa_LRIoOqkG6YIOcjY6tm99c3Tlaqr1VT5SwYHdpG1WMlwioRr4ZQ36LZUGVc9AfRZBwk-eDEj6Jyr-axxKu1KeMID2awRB-3DHVO7du7RbV5GS0HLDC7VufpN449WNOTnPg-QvL-RPs6AVFXmOAeiMQ680IKhGWs2hoJQyIWjJjgecn_x17rZH094rIDBgtLKC7HiJmkmm9uTvgkC6IpPa9OR9VzMEDsyLMjFN1C56nusl4LuRYJoNVZqO49X_uZBxIsGl4XypabZt5vcwWTJ7fWWd7Y8FkUVuESqjGYN0fq-bTdf8FQ91TNrlJIHzjh249tJDTHJ8WfzKBJR3MGQMUwPf2zcdeHFXVdasio-flhozDFULTLeMzqXFjmwaQK1Zztmq5VrA5btwH1XfXjXZVhVIpL9Fzr2JuRaxrd3jAyNWdiGY20iVrkc_UVIqHHXZF6PUM53k9xhuBL9k7klZeMgdeBfHfmw4qSmzJUGuO6j-cAcEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/343ca3619f.mp4?token=a-eEY13ASMSuGt8_0eQgg09XU4q7ilg6q0SD9r-a6H0-WmiJbNgfnkgo00dSoVt3nabr5oJUabHT_m8_97leGu4M0pm89uZ10N-REWRzE3oTjcJU23aETUipRlilmr37WbObyBa_gFJ04MO4qY1rPec_vggCnGkJUBxutyoOQEOXw06U4MoTjnPXa_LRIoOqkG6YIOcjY6tm99c3Tlaqr1VT5SwYHdpG1WMlwioRr4ZQ36LZUGVc9AfRZBwk-eDEj6Jyr-axxKu1KeMID2awRB-3DHVO7du7RbV5GS0HLDC7VufpN449WNOTnPg-QvL-RPs6AVFXmOAeiMQ680IKhGWs2hoJQyIWjJjgecn_x17rZH094rIDBgtLKC7HiJmkmm9uTvgkC6IpPa9OR9VzMEDsyLMjFN1C56nusl4LuRYJoNVZqO49X_uZBxIsGl4XypabZt5vcwWTJ7fWWd7Y8FkUVuESqjGYN0fq-bTdf8FQ91TNrlJIHzjh249tJDTHJ8WfzKBJR3MGQMUwPf2zcdeHFXVdasio-flhozDFULTLeMzqXFjmwaQK1Zztmq5VrA5btwH1XfXjXZVhVIpL9Fzr2JuRaxrd3jAyNWdiGY20iVrkc_UVIqHHXZF6PUM53k9xhuBL9k7klZeMgdeBfHfmw4qSmzJUGuO6j-cAcEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیلی نوجوانان پیشوا به هذیان‌گویی «اینترنشنال»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/462662" target="_blank">📅 20:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462661">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2TqcvKQaZQLA-wCXVla9h-5RwkUHu6OstqR6QBn5p7ZphvW-ZpfE9ukkCtIEplI1hjWBy1kNPVwkhgKqjMgJYhpg3zy7kJ_0Yt60Yr9XHt2sZmjZxvwBjey9OUeIJdipSoA6GO8hcpx6fPHehorclPHt8cSVXG15qmzyZGIxyGqxtaQi292m3dFuO0AR_XwSK1qxVbCCuB70vfHXAsSvnRlhXzTpbpU9i-FqW6AgcufOo3HyFGtONHJRqe1NYyqYWlFwGGNTgHtcS5Odz_KnsYnjuNBiS0MG-z5-9tY-0U_FluBDwShvRbe72o3J5R768pDji6ZAMiTtD6wL1SNYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجارهای کنترل شده در ساوه
🔹
ناحیه مقاومت بسیج ساوه: هم‌زمان با برگزاری نمایش بزرگ محیطی و میدانی «معبر ۳»، صدای تیراندازی و انفجارهای محدود و کنترل‌شده از شنبه ۲۸ شهریورماه به مدت ۷ شب در این شهر شنیده خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/462661" target="_blank">📅 20:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462660">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
وقوع حادثه برای یک نفتکش در سواحل یمن
🔹
سازمان عملیات تجارت دریایی بریتانیا امروز پنجشنبه از یک حادثه برای یک کشتی در سواحل یمن خبر داد.
🔸
هنوز هویت نفتکش و عامل حمله مشخص نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/462660" target="_blank">📅 19:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462659">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b4e86e47d.mp4?token=T548hUzdF9jRW09ODJVR-dcPBYbDKgqeuRART6OZP4dyMDwetRXx5dDpND_kmGN3wXAlemmipt5sGw2F9jxbjJL82p9w9QpiCWSCdCkb_02EOJOPq6vOjhMYOugc8_VRbmwHS_1FU54w6Uufpk_TwkVjb8Cc6XUKNuyQXYqkAyDZnnVCsmk6auaO8adFpxu8qkZ4S5l7KntN8T5ImJ0UXxda5iA35-ctzv1OfOhIj5Gb8-oFbHC_EiZzMY063h0GDT52DzW1g-NuqP4buyrO_esiVWqW-Y2X6f-zvxyjvOrLyaBXNANTbqogG7mNa9CJgBgyc_tOkO-P8Q7_7v6XNJhF72nTi6wamKEwL8-1b4KU8syD-TIpCWr5ard9Kc-d2_6uuqFvNMw6Yv4OE-OtKVsCbTZGWfdLHOzt3_7NVQsQ9DAxQez4wAsJI20K7VivNVxBljdAmML_7earo2Sbb46Q9i0_M_ZO55exF9cX95Et9D3vnAeTEFEewhBhjRu2W8uJ-Ca-bLyutwQAG-5LUN8XLH8K6w20CgKCNeghZeSB9nkgg2I-iHcO1iRS4jUPn3nP-25EMGhvmJuwOET5FVgniJuxb9GY7_w6N0DCFyY7Id-JvQYCiaKCcE8oPGWfdreCgLgtpSJYbwOiP4V8ihXKd8xYieFHMfzfzxPc50M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b4e86e47d.mp4?token=T548hUzdF9jRW09ODJVR-dcPBYbDKgqeuRART6OZP4dyMDwetRXx5dDpND_kmGN3wXAlemmipt5sGw2F9jxbjJL82p9w9QpiCWSCdCkb_02EOJOPq6vOjhMYOugc8_VRbmwHS_1FU54w6Uufpk_TwkVjb8Cc6XUKNuyQXYqkAyDZnnVCsmk6auaO8adFpxu8qkZ4S5l7KntN8T5ImJ0UXxda5iA35-ctzv1OfOhIj5Gb8-oFbHC_EiZzMY063h0GDT52DzW1g-NuqP4buyrO_esiVWqW-Y2X6f-zvxyjvOrLyaBXNANTbqogG7mNa9CJgBgyc_tOkO-P8Q7_7v6XNJhF72nTi6wamKEwL8-1b4KU8syD-TIpCWr5ard9Kc-d2_6uuqFvNMw6Yv4OE-OtKVsCbTZGWfdLHOzt3_7NVQsQ9DAxQez4wAsJI20K7VivNVxBljdAmML_7earo2Sbb46Q9i0_M_ZO55exF9cX95Et9D3vnAeTEFEewhBhjRu2W8uJ-Ca-bLyutwQAG-5LUN8XLH8K6w20CgKCNeghZeSB9nkgg2I-iHcO1iRS4jUPn3nP-25EMGhvmJuwOET5FVgniJuxb9GY7_w6N0DCFyY7Id-JvQYCiaKCcE8oPGWfdreCgLgtpSJYbwOiP4V8ihXKd8xYieFHMfzfzxPc50M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردمِ متحد، شکست نخواهند خورد
🎙
نماهنگ «خدا با ماست» با صدای محمود کریمی به زبان انگلیسی
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/462659" target="_blank">📅 19:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462658">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0e003523.mp4?token=Jq2f2I_2DNfFPnxIrO2BnKqx2uv6_X-CBRw2Rvy3I6qzmNxdkl6R2kj3FrJH4blU546dqVA-PhISNqLPtIgs4o5vBiE-VaMLGaC85AOVBWjnKmFIOdRAqDFLtoWcfJH4liIXyCHCZBSAaELFEP3-PqafuRQ8gsABQ9vcOzKPQE96zzBez7yz-5FqY9VKyFlzs6qvPBXJgU5HCzr_pgeQE8T7bL-8aSzg3PfCX1EFMd2sumUECu-xbVBiAsyeEcEPMBoY0kBFky0btJxA0aTMJPAlJy6gJYs0ayxvWrniQaS61p7EIbVHF7onFwPd6ojsQzdEEFLqjjWknpc27OZgOAQw_vJSxYqdrqiL0N031vk8ly11L4eamIaOoVgrD7TBzhLDIBhIx3TnTl3FEr6mRqMT2xdkJnEBH0p9TuD5-h8EDS-CDBDZzFNVSPaoU47atVpei3vSmh1QtJjEPUBdUsPPqFFVgKWcSyjrPCw20tjM3YgKOJNqkQJ7JWun6B5QyMj6cn7CvyGsdsx5bbnHnuiv7Aa91ge_dUjlnUTjpmSM8ocOGHZXBt2r1PeriDRja2aU9KPeFBK9n4OHezAwNlxgFTRk4tEajyYbxbQeXqkwGsh74stkkEOcBqGUjZ4-EdxpWoax1t1CmsK-sJ1y719r18NEqHY-JkG3Bz1NXNI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0e003523.mp4?token=Jq2f2I_2DNfFPnxIrO2BnKqx2uv6_X-CBRw2Rvy3I6qzmNxdkl6R2kj3FrJH4blU546dqVA-PhISNqLPtIgs4o5vBiE-VaMLGaC85AOVBWjnKmFIOdRAqDFLtoWcfJH4liIXyCHCZBSAaELFEP3-PqafuRQ8gsABQ9vcOzKPQE96zzBez7yz-5FqY9VKyFlzs6qvPBXJgU5HCzr_pgeQE8T7bL-8aSzg3PfCX1EFMd2sumUECu-xbVBiAsyeEcEPMBoY0kBFky0btJxA0aTMJPAlJy6gJYs0ayxvWrniQaS61p7EIbVHF7onFwPd6ojsQzdEEFLqjjWknpc27OZgOAQw_vJSxYqdrqiL0N031vk8ly11L4eamIaOoVgrD7TBzhLDIBhIx3TnTl3FEr6mRqMT2xdkJnEBH0p9TuD5-h8EDS-CDBDZzFNVSPaoU47atVpei3vSmh1QtJjEPUBdUsPPqFFVgKWcSyjrPCw20tjM3YgKOJNqkQJ7JWun6B5QyMj6cn7CvyGsdsx5bbnHnuiv7Aa91ge_dUjlnUTjpmSM8ocOGHZXBt2r1PeriDRja2aU9KPeFBK9n4OHezAwNlxgFTRk4tEajyYbxbQeXqkwGsh74stkkEOcBqGUjZ4-EdxpWoax1t1CmsK-sJ1y719r18NEqHY-JkG3Bz1NXNI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکست فراخوان اعتصاب ۲۵ شهریور گروهک‌‌های تجزیه‌طلب
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/462658" target="_blank">📅 19:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462657">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712ade6ecc.mp4?token=hnzZudYjgmzOHwDWH1ctjfX_CMfW0pXtLeFow73rkbmG5Pabs06bAJYf0wilGbGtpLVdQlc4LvCvk-_qlCBF0ugx0nIdimtqWFENVJ7xME4b_aEG3WUH9UblMx6IHD2CLs08LwF2yNFqIgBQgCLgPKdoU-LlwnorGisqERXgucyDZQkm5GJAe463sBdb5R-Z3kHk6baJLRAwC0nVd6kyegvchtQVcACJwaMLo5QVouAszQqzv-HcusNoJF5z-6XGsMMjPxp70Z9356aZBucGd45eAV3CIGVqnPgb4m6YzrE5nzC-WE4H_aU7jUHPQg8N-EZmRoL1tFwYF5ToneEkkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712ade6ecc.mp4?token=hnzZudYjgmzOHwDWH1ctjfX_CMfW0pXtLeFow73rkbmG5Pabs06bAJYf0wilGbGtpLVdQlc4LvCvk-_qlCBF0ugx0nIdimtqWFENVJ7xME4b_aEG3WUH9UblMx6IHD2CLs08LwF2yNFqIgBQgCLgPKdoU-LlwnorGisqERXgucyDZQkm5GJAe463sBdb5R-Z3kHk6baJLRAwC0nVd6kyegvchtQVcACJwaMLo5QVouAszQqzv-HcusNoJF5z-6XGsMMjPxp70Z9356aZBucGd45eAV3CIGVqnPgb4m6YzrE5nzC-WE4H_aU7jUHPQg8N-EZmRoL1tFwYF5ToneEkkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان اداری و استخدامی: همهٔ مدیران در تمام سطوح نیازمند آموزش هستند
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/462657" target="_blank">📅 19:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462656">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec22c401e5.mp4?token=PyvytpfkydbLkkObhDcIC1DTWiPKEEIV_kclKjw6jYO3k9IwFPG9AbfCGIZ86TpWrPiqQWPCq45Ir2BxTfe0byQFQXR6YtfsZIlpUVp_S7p8VMUFuJkyaTIU0k7OWz7jrMMun-KPF3yIiQzJFATvD4nnnbXoy9ABWOJcZrnCT_8gX0_90b2l_aYTuqsiluYHbk4mNUJsbQX6qOCCYkFTOFDIEUzsldy5_1zP_96ZMEaDAvD_Lu4AviweXEN0au1d9i5JiFoWn8xLXcOjxIqOdf9CA7Cq2b3tE05tAv9_Y_3t7ZqfQG-wfGJl9EGjWnbORGZ77NOj9xHUngZrW2yR4IMpVtcyKvUsY-INwt-D_mk814_CAoYVlFvacUx2SNRECD89frp0x4mvC44m6zQkpkDDo0tLQh-F2NtLeb5zNi-QrTxA2wMvdeTkb_-Z4KGzW5c9CpQjCzOzag5h0OEhpOUuLSc6C85F0G1fEoGyK19YqUURpR2qT2KW-mRpo3fKy5cQvwmDqqc1XradAuO_tg4Kr_p0Z0tdqCWIHyH1Km8h6GoFSQ8VXYWpV_lbRyMX2GXvxV4NjuJ3tiBjKu0zg1IC5H3Lc1llCKaSqGSPIGnXZH-CeQz7HPS3I9pEFeuMX_wQYamb1Gom8KeZXJf6pIQisVRmOPa3gP3bLZd6jls" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec22c401e5.mp4?token=PyvytpfkydbLkkObhDcIC1DTWiPKEEIV_kclKjw6jYO3k9IwFPG9AbfCGIZ86TpWrPiqQWPCq45Ir2BxTfe0byQFQXR6YtfsZIlpUVp_S7p8VMUFuJkyaTIU0k7OWz7jrMMun-KPF3yIiQzJFATvD4nnnbXoy9ABWOJcZrnCT_8gX0_90b2l_aYTuqsiluYHbk4mNUJsbQX6qOCCYkFTOFDIEUzsldy5_1zP_96ZMEaDAvD_Lu4AviweXEN0au1d9i5JiFoWn8xLXcOjxIqOdf9CA7Cq2b3tE05tAv9_Y_3t7ZqfQG-wfGJl9EGjWnbORGZ77NOj9xHUngZrW2yR4IMpVtcyKvUsY-INwt-D_mk814_CAoYVlFvacUx2SNRECD89frp0x4mvC44m6zQkpkDDo0tLQh-F2NtLeb5zNi-QrTxA2wMvdeTkb_-Z4KGzW5c9CpQjCzOzag5h0OEhpOUuLSc6C85F0G1fEoGyK19YqUURpR2qT2KW-mRpo3fKy5cQvwmDqqc1XradAuO_tg4Kr_p0Z0tdqCWIHyH1Km8h6GoFSQ8VXYWpV_lbRyMX2GXvxV4NjuJ3tiBjKu0zg1IC5H3Lc1llCKaSqGSPIGnXZH-CeQz7HPS3I9pEFeuMX_wQYamb1Gom8KeZXJf6pIQisVRmOPa3gP3bLZd6jls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رژهٔ خودرویی رزمایش جان‌فدا در اسلامشهر تهران  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/462656" target="_blank">📅 19:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462655">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcabdbd1b2.mp4?token=ig7LGiRorypyT29ww4W6fXhOrzxAeGZnuhF6JfpKrG9mB8c0Lq-7HLpPmMT9Lg1ABy50TrkrlGrfiyYy62axBDVB__eKjk2VOBReoIC_7fNkhYtT6rjwaun4YNjH7KOCp_NDhZwFVx7ctYFL8eorF8ZSCqqPmdJgM-IaZXYoeFNZfcgiD2V9kYtjuIX89grHh7R9xAEcLkF8h39E6wx9Bxm2xMXvRbsY_IQi_xuOsS2QKojompLUCWzgdD5fdNtZz2VMfvmRMTIbSOmiY2kJPP0-7yswhHG7iEXtVTbTSlhY5pgZkuWASIWIEV22HhO09b3LrhYo68KPNJQMrNQDfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcabdbd1b2.mp4?token=ig7LGiRorypyT29ww4W6fXhOrzxAeGZnuhF6JfpKrG9mB8c0Lq-7HLpPmMT9Lg1ABy50TrkrlGrfiyYy62axBDVB__eKjk2VOBReoIC_7fNkhYtT6rjwaun4YNjH7KOCp_NDhZwFVx7ctYFL8eorF8ZSCqqPmdJgM-IaZXYoeFNZfcgiD2V9kYtjuIX89grHh7R9xAEcLkF8h39E6wx9Bxm2xMXvRbsY_IQi_xuOsS2QKojompLUCWzgdD5fdNtZz2VMfvmRMTIbSOmiY2kJPP0-7yswhHG7iEXtVTbTSlhY5pgZkuWASIWIEV22HhO09b3LrhYo68KPNJQMrNQDfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس ترافیک شهری راهور فراجا: نظارت کامل بر ایمنی سرویس مدارس با سامانهٔ سپند انجام می شود  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/462655" target="_blank">📅 19:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462654">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26a97aedf0.mp4?token=pZZoF4VGYQAMwM7iymqQPio3KKZcpklLPdMgsg2sJkKff9HuRwgvrnjHsSovT-8vH13fJX5Qw55NCRjUURs1-uGHhuNp_D7A_nxd6P_lTRfX-80ud8vrFyAei2Do6vhAHUjK_EAPPGdm5qJgLcATqGA1WFu8Oq59vpvl1EwRlFjZAudgJhVXMnqzHF4GOG1_aYdl1qaX5dNKu_YyaMmsNstlOtcOdFQXg1qt1BUopLwWfj-BkMgbYZYvk5SCvgStJIO-x9kLhNanOlKqLMgeARpZ_GNRQnLyXFuNYsPk1B1OU4GzGleIHyPZ2HAxxSJK5U7ZEDOy-CKdTtvh7OpQLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26a97aedf0.mp4?token=pZZoF4VGYQAMwM7iymqQPio3KKZcpklLPdMgsg2sJkKff9HuRwgvrnjHsSovT-8vH13fJX5Qw55NCRjUURs1-uGHhuNp_D7A_nxd6P_lTRfX-80ud8vrFyAei2Do6vhAHUjK_EAPPGdm5qJgLcATqGA1WFu8Oq59vpvl1EwRlFjZAudgJhVXMnqzHF4GOG1_aYdl1qaX5dNKu_YyaMmsNstlOtcOdFQXg1qt1BUopLwWfj-BkMgbYZYvk5SCvgStJIO-x9kLhNanOlKqLMgeARpZ_GNRQnLyXFuNYsPk1B1OU4GzGleIHyPZ2HAxxSJK5U7ZEDOy-CKdTtvh7OpQLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس
پلیس ترافیک شهری راهور فراجا: نظارت کامل بر ایمنی سرویس مدارس با سامانهٔ سپند انجام می شود
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/462654" target="_blank">📅 19:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462653">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1edf6697b5.mp4?token=NU1gfLYsdQYnbDWBrY2BxJe719Rqs3DPoTEJkgeD-G-9zeIkTPkmyYmvsspOS8SzYTgFgsmASv8R6NWdldF3fZOJpCCtuGbyZ4aKQ3ZVpG3uqstGxa7YzfMN2cXztlpsR8hyLF9y2qTK_BauvxD6e5Cq3_dRBI0pwQeEIdm8lN9CGpOfXfmhe8IE9vAuCR9z11d-yhvoTUfl3pwah0T5GXvhywoBnJUupOWxT-Fe97GT66GkU6UsigD941vG5BV0Tmt99JN3ch1Ja9_qoDpEfF4rtFwMcAm3VB79fSXN7I_dlPDJBNV-3a3W4NRcgwqGSCDwgp56KT8OTHFo3WQszDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1edf6697b5.mp4?token=NU1gfLYsdQYnbDWBrY2BxJe719Rqs3DPoTEJkgeD-G-9zeIkTPkmyYmvsspOS8SzYTgFgsmASv8R6NWdldF3fZOJpCCtuGbyZ4aKQ3ZVpG3uqstGxa7YzfMN2cXztlpsR8hyLF9y2qTK_BauvxD6e5Cq3_dRBI0pwQeEIdm8lN9CGpOfXfmhe8IE9vAuCR9z11d-yhvoTUfl3pwah0T5GXvhywoBnJUupOWxT-Fe97GT66GkU6UsigD941vG5BV0Tmt99JN3ch1Ja9_qoDpEfF4rtFwMcAm3VB79fSXN7I_dlPDJBNV-3a3W4NRcgwqGSCDwgp56KT8OTHFo3WQszDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ وزارت اطلاعات: خود را متعهد می‌دانیم تا برای شناسایی و برخورد قانونی با عوامل، آمران و پشتیبانان ترور مولوی «شهید گرگیچ» از پای ننشینیم.  @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/462653" target="_blank">📅 19:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462652">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb4729cd84.mp4?token=ApyAhU76o-46_oRuSDAgvOJt11eK9BHOteTwRPMzl9N9bQyfCOa5j_I-q_DI_YmJjQIpANHGLCfbHlrkHBBcyStnS0H1CwXLAU8aXiKUFQE_5OBPz-x_ApuBqTb8mgsAjlxkTJt0SDJ1vU4dkFWUeHtRGMN0ew9SB3nEC1KPGqhTFrJzkdbN-D86dLgZEtXULab2N4Yqy18GokK7w-Yov32ZoaRRRs2R0C7uWZqfQF2GuFHIXi6D_VVUakBgyWOzqBMQsgLQq1aNnPPx0HUIwzkLwvEm8BOV98m2jNATxZJOjzuKelwsZMbCEIyL6D0blHj8Lyg6g5mB4_qwGkmNhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb4729cd84.mp4?token=ApyAhU76o-46_oRuSDAgvOJt11eK9BHOteTwRPMzl9N9bQyfCOa5j_I-q_DI_YmJjQIpANHGLCfbHlrkHBBcyStnS0H1CwXLAU8aXiKUFQE_5OBPz-x_ApuBqTb8mgsAjlxkTJt0SDJ1vU4dkFWUeHtRGMN0ew9SB3nEC1KPGqhTFrJzkdbN-D86dLgZEtXULab2N4Yqy18GokK7w-Yov32ZoaRRRs2R0C7uWZqfQF2GuFHIXi6D_VVUakBgyWOzqBMQsgLQq1aNnPPx0HUIwzkLwvEm8BOV98m2jNATxZJOjzuKelwsZMbCEIyL6D0blHj8Lyg6g5mB4_qwGkmNhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ ماموران خاطی برخورد ناپسند با فرد تبریزی در بازداشت هستند
🔹
سازمان قضایی نیرو‌های مسلح اعلام کرد که ماموران خاطی برخورد ناپسند با فرد تبریزی در بازداشت هستند.
🔹
تحقیقات قضایی در مورد این موضوع ادامه دارد و دستگاه قضایی وفق قانون با خاطیان برخورد بدون مماشات…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/462652" target="_blank">📅 18:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462651">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سردار حسن‌زاده: ایران در آستانهٔ یکی از بزرگ‌ترین رزمایش‌های مردمی است
🔹
فرمانده سپاه محمد رسول‌الله(ص) تهران: اکنون نسبت به پیش از جنگ ۱۲روزه و جنگ رمضان آماده‌تر است و ارتقای توان موشکی، پهپادی و پدافندی همچنان ادامه دارد.
🔹
پس از ثبت‌نام داوطلبان پویش جان‌فدا،…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/462651" target="_blank">📅 18:48 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
