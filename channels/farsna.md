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
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 08:31:44</div>
<hr>

<div class="tg-post" id="msg-446591">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34ebe347e2.mp4?token=JMBvAzPBDUYSPqB1MCU05jB6wQNR9PhAUnJYM9fG2w0y0rCFcjJboXWTtgjGi3uY4utvnRq4oprhLDiqzr0NybpRZTU3KBXMeXfGoGIRyLf0aLKR246fX02jNY3vz_7QnIbWLWk85qhz4x9Ial1G-rXsa0_IYiIcPDvrjzeRfDG2HgaltybM0jYSA7R67xuwxdO6j1MKycONbXZIKk0kQptPWz5J5V4YWkp17drcmWQMK4ELNB9D2YA0SiEXMSmTDYvVYQTxpkGOWrgYSVck3yZCLTw2YDJcD6yp7HX8k00Z2sEXb-_zT53ozw3RMVrzPT7i0eSr3kk4ArU88zyD96Gdun1AeTIZE0vM5XwuPTo56Zt3uOVA472jRzXSbQCtAXgK2mf2A2lih51mqr4nLRaTGoa1fAu9KNcYd7D1YI8WxsX9OVHfo62y9vwtV2QKvFNQnown6Dn7x-lPBklgReczrq2LgJ9Pvo0dA6WdnbNqK5MxzUPeJ8w99WuNtAyj6sa_K0qRuww-7o33MV8IWmbejiv6Q1Nnn3o6n5kYbzCjp2PNnxVf-cwH1x8GRXYxI21apAc05oATRfvb1ouVL2SsRPulaNUl11uDMuBDhlk9y0jThInGPlIdnKGysn9vLHYtBrqtaUwH9R6nXn2y-LgfVWG1CJaCjDzkYe50pcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34ebe347e2.mp4?token=JMBvAzPBDUYSPqB1MCU05jB6wQNR9PhAUnJYM9fG2w0y0rCFcjJboXWTtgjGi3uY4utvnRq4oprhLDiqzr0NybpRZTU3KBXMeXfGoGIRyLf0aLKR246fX02jNY3vz_7QnIbWLWk85qhz4x9Ial1G-rXsa0_IYiIcPDvrjzeRfDG2HgaltybM0jYSA7R67xuwxdO6j1MKycONbXZIKk0kQptPWz5J5V4YWkp17drcmWQMK4ELNB9D2YA0SiEXMSmTDYvVYQTxpkGOWrgYSVck3yZCLTw2YDJcD6yp7HX8k00Z2sEXb-_zT53ozw3RMVrzPT7i0eSr3kk4ArU88zyD96Gdun1AeTIZE0vM5XwuPTo56Zt3uOVA472jRzXSbQCtAXgK2mf2A2lih51mqr4nLRaTGoa1fAu9KNcYd7D1YI8WxsX9OVHfo62y9vwtV2QKvFNQnown6Dn7x-lPBklgReczrq2LgJ9Pvo0dA6WdnbNqK5MxzUPeJ8w99WuNtAyj6sa_K0qRuww-7o33MV8IWmbejiv6Q1Nnn3o6n5kYbzCjp2PNnxVf-cwH1x8GRXYxI21apAc05oATRfvb1ouVL2SsRPulaNUl11uDMuBDhlk9y0jThInGPlIdnKGysn9vLHYtBrqtaUwH9R6nXn2y-LgfVWG1CJaCjDzkYe50pcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برای ایران قوی، ما همه ممنونیم ازت...  لحظاتی از شعرخوانی مهدی رسولی در مصلای امام خمینی(ره) تهران.  @Farsna</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/farsna/446591" target="_blank">📅 08:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446590">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🎥
اصلا نمیشه باورم...  لحظاتی از شعرخوانی مهدی رسولی در مصلای امام خمینی(ره) تهران.  @Farsna</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/farsna/446590" target="_blank">📅 08:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446589">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">متروی تهران از امروز ۲۴ ساعته شد
🔹
مدیرعامل متروی تهران: تا ساعت یک بامداد روز سه‌شنبه، ۱۶ تیر، خدمات مترو به‌صورت ۲۴ ساعته و رایگان ارائه می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/farsna/446589" target="_blank">📅 07:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446588">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589f19bd5f.mp4?token=mskCEnBOhqTqpvI2YdUZKcPTOiSmLuyIrFGaBGUm4Rd3tRqq566FSEJsT6gJviSnKDkFrOX945RRpUCkcs3w_CpJ31M6d0AOzsNNRUZF8lUOYXfLwxbluBaUdV-lW6HFZJK3Rnf7S_vgQo89wx06qFikzk5l1n7ktUG2vk7htATM5xR1K3z1jmR4yBWLub-GStfE0U8ME22wMxDAslRQcikchOsaCSZ5roRVLagx_yuZSCukEgVU7t4FgWSkVa-vJqJO-eZD1W858OE4S-b7VJUH9eALtv8OYTahf-5LgoemUsDYQKcA6jNt3HSq1x0571ZRvWtpGjxLpcuQwySbwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589f19bd5f.mp4?token=mskCEnBOhqTqpvI2YdUZKcPTOiSmLuyIrFGaBGUm4Rd3tRqq566FSEJsT6gJviSnKDkFrOX945RRpUCkcs3w_CpJ31M6d0AOzsNNRUZF8lUOYXfLwxbluBaUdV-lW6HFZJK3Rnf7S_vgQo89wx06qFikzk5l1n7ktUG2vk7htATM5xR1K3z1jmR4yBWLub-GStfE0U8ME22wMxDAslRQcikchOsaCSZ5roRVLagx_yuZSCukEgVU7t4FgWSkVa-vJqJO-eZD1W858OE4S-b7VJUH9eALtv8OYTahf-5LgoemUsDYQKcA6jNt3HSq1x0571ZRvWtpGjxLpcuQwySbwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار یک‌صدای مردم در مصلی: «انتقام، انتقام»
@Farsna</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/farsna/446588" target="_blank">📅 07:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446587">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d13d158d39.mp4?token=NH_A7Q0PM5o_EBFTnmRNHfatJ_Nk-bVcYv6VllVUTrAfRWAZV0fgiQY-Yl-oXFZlnkjy-gtAZ4sjqXIamy1BVjs4fXKvw2ukhO8jRgui2MioADd8vQzYk2VRB0gisDt4RoYnzdt3d-tLdF9AAnLvyz_FbeEKlzkEjBfY1fSdv-JoVsd2Aj-AzlVpnvb-QwfrqFbKcesKr4dBqqvmYwvqtVSK4U_HtCpr0BzmysLQKvFCMiCJr5Xm0rwIE2MD04g_FS6QQqZG6Mqm_e-fULxZfHAbn0enABlcgj7V7gKIt2gJOkZaawYoBQzZBherc-CIsM7hB2Qf-c9dcWPZIWk8t6Dqe55OocOL-zqAhfxvJaEIiWAQS1n-UM4zCq7Nh5ui4scSmNMT56_Q0waLh4XHLqcLil1RpT12xdzUdekGqjmC1NHGfYfSOiXLmMbdl1iRMGUQMgyeZT_Gale_6DXOJTya9WAnHI9WKn26VZuxlu1EF9qFOr1kSY65Gp_hn9pkkPbPq7g_YdFSbGC2VInRkTD6bGcuGkL9vArrGtWeSVEMsyj-3eJsv4A6UA2Lg3u_lu9qneR1QVAWXIwJYic2qf8COCL6UmtwqB4ODZ6aEIXsdt6eVJwITuBiQYTSL9NLyAWgq3eg-egiptDy6Mt6ePOTH92cq6SuhQkzfCRm6NI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d13d158d39.mp4?token=NH_A7Q0PM5o_EBFTnmRNHfatJ_Nk-bVcYv6VllVUTrAfRWAZV0fgiQY-Yl-oXFZlnkjy-gtAZ4sjqXIamy1BVjs4fXKvw2ukhO8jRgui2MioADd8vQzYk2VRB0gisDt4RoYnzdt3d-tLdF9AAnLvyz_FbeEKlzkEjBfY1fSdv-JoVsd2Aj-AzlVpnvb-QwfrqFbKcesKr4dBqqvmYwvqtVSK4U_HtCpr0BzmysLQKvFCMiCJr5Xm0rwIE2MD04g_FS6QQqZG6Mqm_e-fULxZfHAbn0enABlcgj7V7gKIt2gJOkZaawYoBQzZBherc-CIsM7hB2Qf-c9dcWPZIWk8t6Dqe55OocOL-zqAhfxvJaEIiWAQS1n-UM4zCq7Nh5ui4scSmNMT56_Q0waLh4XHLqcLil1RpT12xdzUdekGqjmC1NHGfYfSOiXLmMbdl1iRMGUQMgyeZT_Gale_6DXOJTya9WAnHI9WKn26VZuxlu1EF9qFOr1kSY65Gp_hn9pkkPbPq7g_YdFSbGC2VInRkTD6bGcuGkL9vArrGtWeSVEMsyj-3eJsv4A6UA2Lg3u_lu9qneR1QVAWXIwJYic2qf8COCL6UmtwqB4ODZ6aEIXsdt6eVJwITuBiQYTSL9NLyAWgq3eg-egiptDy6Mt6ePOTH92cq6SuhQkzfCRm6NI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اصلا نمیشه باورم...
لحظاتی از شعرخوانی مهدی رسولی در مصلای امام خمینی(ره) تهران.
@Farsna</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/farsna/446587" target="_blank">📅 07:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446586">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efeb113d0c.mp4?token=CIKd5d5HEokzljV9lzgQhuP7WQ_2mnBnh8rdKw5aVzMW4FePEedo927n-XrPgtanAsOcwL1F0on7AoQqVA9txgMmS7SK9zddo7lCI5lDCWRDncQ7Z_HMFgMXTwOYyWbCFftRvL79Kv6nEFHNCPnqxpygOFCdHDqUbwqdxyjwBQkdMSWj8ypgfK0zem9ibHYdH9pwm33Aw3b_tjDxr-unW2idP2bGl9xYTjiZsw-Nb0dipTj_K0Jwnb1x8lhjoiLbPlkC4y3cYaxP0m5WRsLvXivaeazAdb48YPiNjxVjoDKegVPitFa2ylV-cf35y1t3e3b8Yp8-iQc-Tend63KgZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efeb113d0c.mp4?token=CIKd5d5HEokzljV9lzgQhuP7WQ_2mnBnh8rdKw5aVzMW4FePEedo927n-XrPgtanAsOcwL1F0on7AoQqVA9txgMmS7SK9zddo7lCI5lDCWRDncQ7Z_HMFgMXTwOYyWbCFftRvL79Kv6nEFHNCPnqxpygOFCdHDqUbwqdxyjwBQkdMSWj8ypgfK0zem9ibHYdH9pwm33Aw3b_tjDxr-unW2idP2bGl9xYTjiZsw-Nb0dipTj_K0Jwnb1x8lhjoiLbPlkC4y3cYaxP0m5WRsLvXivaeazAdb48YPiNjxVjoDKegVPitFa2ylV-cf35y1t3e3b8Yp8-iQc-Tend63KgZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار خیل عشاق در خیابان منتهی به مصلای تهران: ابالفضل علمدار، خامنه‌ای نگهدار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/farsna/446586" target="_blank">📅 07:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446584">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8db21ec429.mp4?token=LFI5iXv0gxvDheIad-YgbIm8tnf1DAMHj_iKrZHwu4cOy0bLX7quLyniytjQ5LkebwF-TzyePzAuJbUvPsOBD_DLz7ju8XwLu-dLDIBxuYW9gVG6ilekdNDms9dhGT6OHTQTlx4vWxBSeartXUgoHyp5Gp0p_ZyxC5XJv0Jp8r8EQMVR5laQQJmZgGNi-pXGlhKIIPJLD5E8bHPvheOqDU3R1QzSkY-O6pK8Ntn9vVjMn2LZ-MoqnHyrLq5h8Wp8BotPkiQoCaeWjpdJN-oK6DK8_HwcA9j2HUN3F5plkoN4tcIi6bW5XJGhoIG0o863FLX8EwEMwCZe8ldkIvsvSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8db21ec429.mp4?token=LFI5iXv0gxvDheIad-YgbIm8tnf1DAMHj_iKrZHwu4cOy0bLX7quLyniytjQ5LkebwF-TzyePzAuJbUvPsOBD_DLz7ju8XwLu-dLDIBxuYW9gVG6ilekdNDms9dhGT6OHTQTlx4vWxBSeartXUgoHyp5Gp0p_ZyxC5XJv0Jp8r8EQMVR5laQQJmZgGNi-pXGlhKIIPJLD5E8bHPvheOqDU3R1QzSkY-O6pK8Ntn9vVjMn2LZ-MoqnHyrLq5h8Wp8BotPkiQoCaeWjpdJN-oK6DK8_HwcA9j2HUN3F5plkoN4tcIi6bW5XJGhoIG0o863FLX8EwEMwCZe8ldkIvsvSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◾️
ای ناگهان عزم سفر کرده، خداحافظ...
🎥
قابی از پیکر مطهر رهبر شهید انقلاب و خانوادۀ شهیدشان در مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/farsna/446584" target="_blank">📅 07:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446583">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdOuSx43CWN7lULFyV9MDJdqwUVHCoghybXzDZSZWMroHAaJZgQM11OImzovsyX2UfuJTj6zLWpgOg3j62CIQgCKhX1OT4rGtxWTmv_lgiHz-IQRbmfKncsvZBmUmglZcPTeI2UPponOg5ISBm4rswTrsETj9UuA7xwQu1TIbMaoBxA3EJ1tNej-HiyYXr4of8ecZlotSVgwe7QM60FyGKFXJhWIh1FdHxZ2kVNlR_ugOdEEwGIMA-b9sdmGDtn4_bg7LBhhAm74GR9Wm8Bw_rVk0sEoe8e0kEk9uLBRctG68uySmz2TSPfAJIV73ntxbQr3Kw5UE64rDXBm_HQQuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
پیکرهای مطهر رهبر شهید انقلاب و خانواده گرامی ایشان در جایگاه برای وداع مردم در مصلی تهران قرار گرفت
@rahbari_plus</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farsna/446583" target="_blank">📅 07:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446582">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/542913cea4.mp4?token=rhaIuSYQwkMgOVIlPMw7Z1M1rV3DwJnMbBMB7-2isQgwNTts7DXOGa8paYzZeIKYLe74Zra0IxuySC42SnVC2vb8dnqApz-ggbm6WFJXsoXBS-rCGfqJ0_6h_F1O5tWBG1xCQXsTlh45nshysA3HpRAwKG4zNT2kgPY_O59Dbo_g1KJ9xkgaWu4JwBCnCJPZTIasKsA6nImVCoNH3sWDvUENpFmjVC9mR2gG17zKwQzbYgLOU2foi4ktFdfLpSDf6P1ZQrLTO5cepys3zWhEUdMBf5-ZHf3JxDCvhbVqdInYbJGTGCFzyWLOLdYMv5XyvLrWLpqAyh67nWxE08zAqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/542913cea4.mp4?token=rhaIuSYQwkMgOVIlPMw7Z1M1rV3DwJnMbBMB7-2isQgwNTts7DXOGa8paYzZeIKYLe74Zra0IxuySC42SnVC2vb8dnqApz-ggbm6WFJXsoXBS-rCGfqJ0_6h_F1O5tWBG1xCQXsTlh45nshysA3HpRAwKG4zNT2kgPY_O59Dbo_g1KJ9xkgaWu4JwBCnCJPZTIasKsA6nImVCoNH3sWDvUENpFmjVC9mR2gG17zKwQzbYgLOU2foi4ktFdfLpSDf6P1ZQrLTO5cepys3zWhEUdMBf5-ZHf3JxDCvhbVqdInYbJGTGCFzyWLOLdYMv5XyvLrWLpqAyh67nWxE08zAqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزا عزاست امروز...
@Farsna</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/farsna/446582" target="_blank">📅 07:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446581">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ebf5d2e7c.mp4?token=u5O-kofjR-PvyYPjM-IpEF3ETSQ1Q9BojDPqjwUx0FXTBb4gKwzdyAAUUym1xHsUO5TNzw_IxdAKrk3xuiIxiJrEI3r-2jZiztnRzOWeNg2RMUvFgRCV87fbe9y-0tpSEMOdG8-6Dxt_am52Nas0cRHjH2Uf8vswC-8ZkokPICqXMu5FbiO9h2GJEv8SlsGcOfzFjsLO-Ghf6G9BK_lymjS1_wsPztEUprGY6Y9bOTzA0Zk9L3iRnqKvvPzQt7Lp1Q8qpfX-a6Sg7Jk5Ab6YVLIi66kYBGG-kzqGKlJ9i0hF2hwTNz1oGA74Y7bDeRn7xYkOncZ3MoUPzB_PoeROnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ebf5d2e7c.mp4?token=u5O-kofjR-PvyYPjM-IpEF3ETSQ1Q9BojDPqjwUx0FXTBb4gKwzdyAAUUym1xHsUO5TNzw_IxdAKrk3xuiIxiJrEI3r-2jZiztnRzOWeNg2RMUvFgRCV87fbe9y-0tpSEMOdG8-6Dxt_am52Nas0cRHjH2Uf8vswC-8ZkokPICqXMu5FbiO9h2GJEv8SlsGcOfzFjsLO-Ghf6G9BK_lymjS1_wsPztEUprGY6Y9bOTzA0Zk9L3iRnqKvvPzQt7Lp1Q8qpfX-a6Sg7Jk5Ab6YVLIi66kYBGG-kzqGKlJ9i0hF2hwTNz1oGA74Y7bDeRn7xYkOncZ3MoUPzB_PoeROnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم سرود ملی ایران را در مصلی زمزمه کردند
@Farsna</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/446581" target="_blank">📅 07:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446580">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f4f7f5387.mp4?token=gny2WN6Ydgzg4EQVunRLuMzCfgOQOyHYc090nux3-LAeeRcOn-DfgKUY0gAjqu9JgQhPILb9EM1-bE0-r_xfSCENF-7rPP2Yd3agUvuvx8wG1rixOIbT9uwvnmcXTGQQUETXVTFiRwi0maoIJP24FaCniJEWFdV_-krEwEYeFzUgifDh5Q0ztpDCMBy-MZ1g4dJETphSrhkXrkRhXFi9WsQRbBp5-4GCImgC7jsWe2aP2iUG1aPqZJ6sWVjDWubj_0kqDkMXLp2s1sxdvMKdnCxoGTpc9tZgPUw8Hp1KGug07TKRdb64QcksuPVXv9IPfMfcPYlYXKgLDXaBy8aPmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f4f7f5387.mp4?token=gny2WN6Ydgzg4EQVunRLuMzCfgOQOyHYc090nux3-LAeeRcOn-DfgKUY0gAjqu9JgQhPILb9EM1-bE0-r_xfSCENF-7rPP2Yd3agUvuvx8wG1rixOIbT9uwvnmcXTGQQUETXVTFiRwi0maoIJP24FaCniJEWFdV_-krEwEYeFzUgifDh5Q0ztpDCMBy-MZ1g4dJETphSrhkXrkRhXFi9WsQRbBp5-4GCImgC7jsWe2aP2iUG1aPqZJ6sWVjDWubj_0kqDkMXLp2s1sxdvMKdnCxoGTpc9tZgPUw8Hp1KGug07TKRdb64QcksuPVXv9IPfMfcPYlYXKgLDXaBy8aPmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل جمعیت در خیابان‌های منتهی به مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/446580" target="_blank">📅 07:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446579">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/124d25574b.mp4?token=Dq47UCEQbQ5JnqgVA6HNAUlKbz-IJWg6QbiDJ3QVRLY7zzBWqSoIImIuos5nmz8uW4-6sxtl57zpBfJfnueazewnfaknaAfMs2SFANAHm5zeO_OjEHGA9cAC4QRLFu_a5vyE1hyGTS7LD6C4Xs1s7rf2LvE5M9l3tVPpcDaFr0skV46Ne_XLVX6OpyLm5OxOxWUY1p5Gz3Mm7dvtgcsxzARUvR17LiDPJVsf40I4v8TTJtowFPmF5YPJBAHNqSGCJFvaA_t_8blyquEI9mX5YoxTyepryWzRY2H6rHAOLB5ORu0aZPnO-tRR384xlkjvjs1DlqKWLwQYFyMoDxGdBDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/124d25574b.mp4?token=Dq47UCEQbQ5JnqgVA6HNAUlKbz-IJWg6QbiDJ3QVRLY7zzBWqSoIImIuos5nmz8uW4-6sxtl57zpBfJfnueazewnfaknaAfMs2SFANAHm5zeO_OjEHGA9cAC4QRLFu_a5vyE1hyGTS7LD6C4Xs1s7rf2LvE5M9l3tVPpcDaFr0skV46Ne_XLVX6OpyLm5OxOxWUY1p5Gz3Mm7dvtgcsxzARUvR17LiDPJVsf40I4v8TTJtowFPmF5YPJBAHNqSGCJFvaA_t_8blyquEI9mX5YoxTyepryWzRY2H6rHAOLB5ORu0aZPnO-tRR384xlkjvjs1DlqKWLwQYFyMoDxGdBDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این تلاطم تمام‌شدنی نیست
@Farsna</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/446579" target="_blank">📅 07:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446578">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJOnp4QRcYq4-PYYsDSZkydQEj7NG2souH4silaDewiDWoBy4JzAhtfYH6-43vucOFjPbxU1CfSR9t8q4DINZ_u9xgr5i7b7z2jDOR4wGzJ3sarq2vJxfdgowbrzssKgs7Cp4sIp89etKHhF1lpNgWWXL4yUYuBq7VxfsIQwtZIIDK9bnNYD-VgEp6fpaOtVRkNSYeG32dpakUFC_2i91SAGrnWSRGl1cHbicQnzmrHEIfIPlBbDLN7HmqcXfKmnskWZ9pBpS4Ys3gVMVf4tMRaJgH1SabSt3mLHcxj63y2uRxNwvMIgfG_igFp1c0ujEkCFN4MIjkwZZjv_vvpaGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وداع شاگردان کی‌روش با جام
غنا حرفی برای گفتن نداشت
کلمبیا حریف سوئیس شد
@Sportfars</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/446578" target="_blank">📅 07:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446577">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-G3LDmEOc8cgF41WiN2uRUhGhrkLUulGrNb3T_Y0iYX9fYtsqbsa4qJfokaunQrPLIRdp-KbKz4ZQXihx9VKYIH71a42rkxxYvlWbZaH8p-e6w7rRzJBZ56ZyrDlYLpCUQCrXzyppW9gHWpXdeuuBivhHlFdZPbPL7rKLUkkNrFG2DH-6av_rakzNWffeARMCwGdEL8DE58GqtdKzXlZBsRDjl0D-CdJfRBNDZqt2yEElDc7rXBOjGG7FsMFf2GnVEN7OmRIImGLSHcIqlVLVGU5tfxmSKz4eyqA9Ub1pXzq-6d8hNkRWdTMDQgw4UgidVkFXOeDVlJ4LyscJz-qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
مهمان گرجستانی اولین روز وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farsna/446577" target="_blank">📅 07:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446576">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3438c87d.mp4?token=mgdYlkF2WcYAc1vxG88iA6dIFzZayusLmIGm9N2DLzbo54Ks7jM_UVxOvGEuOjYd2toun40mVPBzAqAyYtEop4G1FiJrDuOlupBrCmT0u6ApJbO-aD7e65NZ3urzulgGNsafiHgsGbcb4LeK-HMHWWoT2vePtV_yU6fYYeen4fb1b4f0xjI-Xcm5_tnvlF-avybj-99GXt_zwijnZw6IX-SX7kQfqv_mM1xo4Q7el6YJhvkEXw8p-Npyfk-w9HrpmSY6yFtAjIWbb4U9-5vQMhTpWbDkVL1x2CDNpw3eR-NRIPSHqFj6u1MUKVagXt7mGwUUEz4jmLVBLQ6MmVYuQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3438c87d.mp4?token=mgdYlkF2WcYAc1vxG88iA6dIFzZayusLmIGm9N2DLzbo54Ks7jM_UVxOvGEuOjYd2toun40mVPBzAqAyYtEop4G1FiJrDuOlupBrCmT0u6ApJbO-aD7e65NZ3urzulgGNsafiHgsGbcb4LeK-HMHWWoT2vePtV_yU6fYYeen4fb1b4f0xjI-Xcm5_tnvlF-avybj-99GXt_zwijnZw6IX-SX7kQfqv_mM1xo4Q7el6YJhvkEXw8p-Npyfk-w9HrpmSY6yFtAjIWbb4U9-5vQMhTpWbDkVL1x2CDNpw3eR-NRIPSHqFj6u1MUKVagXt7mGwUUEz4jmLVBLQ6MmVYuQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصلی مغناطیس امروز پایتخت شد
@Farsna</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/446576" target="_blank">📅 07:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446575">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f042e46d24.mp4?token=UX-i5lP0HcPED1XNEErI_wLDoOcGdyxCBurhAGzZo_svXnxClpx2YNQccmOMhMN2Wj01bGiuchGtPbA2-CH1yDnxCZdgZ-gDwgWgN-BmUJ9uIIiqcCw9x4E-5jkgL-WTwBzdFIMMxof_EYQ3wNWwkq2JZbyRvOdRO2qXbomtwELCjCJw3dExEGb9qOh-FhstDz-jqsoi_1EgE0T_RRqXlS2sqQFcUfpmet-N_Oitx5t1TIC5uGczK4T3ixsjmK6fzDBfOkD1XJn5iDpGMnGfBYSYd_LNZ00OxqjQ13eTSU--O0CT0YAGpPxMVhrhjdIM8U_k_HU5O1K_ODQp0cXhZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f042e46d24.mp4?token=UX-i5lP0HcPED1XNEErI_wLDoOcGdyxCBurhAGzZo_svXnxClpx2YNQccmOMhMN2Wj01bGiuchGtPbA2-CH1yDnxCZdgZ-gDwgWgN-BmUJ9uIIiqcCw9x4E-5jkgL-WTwBzdFIMMxof_EYQ3wNWwkq2JZbyRvOdRO2qXbomtwELCjCJw3dExEGb9qOh-FhstDz-jqsoi_1EgE0T_RRqXlS2sqQFcUfpmet-N_Oitx5t1TIC5uGczK4T3ixsjmK6fzDBfOkD1XJn5iDpGMnGfBYSYd_LNZ00OxqjQ13eTSU--O0CT0YAGpPxMVhrhjdIM8U_k_HU5O1K_ODQp0cXhZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی از سیل خروشان دلدادگی
@Farsna</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/446575" target="_blank">📅 06:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446574">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a947bd8001.mp4?token=pIRF04q8EXcFqBFa_KUAVeiDJIhpIqYImwPd4QuAogPR4i7PNBjLSDXrtwnzT6tYUApJvvoFS_3PGDPQr7EpU3aEsxyVLHKfv3b1fd3ici7e2tljk1KX7OJyPfu924pG4LKzryDPGK2_5OWMC1jTdYso3XkySOoM-7pxOAHe6m0KyuVlCSktFPC0rRSURDCmcYBfx5gC_C_3UJbVzHXmZW1WXw1o9GdzQsZV4tgjaizEQCcbMxpCbyq6rncomp03mFX5npVC2CiszLgdJdSyOPZ14xSp7qPXnLT6KH7NpRIZh9xh9Depo-_ilERsWtwJAR4AdWLhJPnvahZzlbpJ1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a947bd8001.mp4?token=pIRF04q8EXcFqBFa_KUAVeiDJIhpIqYImwPd4QuAogPR4i7PNBjLSDXrtwnzT6tYUApJvvoFS_3PGDPQr7EpU3aEsxyVLHKfv3b1fd3ici7e2tljk1KX7OJyPfu924pG4LKzryDPGK2_5OWMC1jTdYso3XkySOoM-7pxOAHe6m0KyuVlCSktFPC0rRSURDCmcYBfx5gC_C_3UJbVzHXmZW1WXw1o9GdzQsZV4tgjaizEQCcbMxpCbyq6rncomp03mFX5npVC2CiszLgdJdSyOPZ14xSp7qPXnLT6KH7NpRIZh9xh9Depo-_ilERsWtwJAR4AdWLhJPnvahZzlbpJ1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم یالثارات‌ الحسین بر فراز گنبد مصلی تهران
🔹
همزمان با برگزاری مراسم وداع با پیکر رهبر شهید، پرچم سرخ «یا لثارات الحسین (ع)» بر فراز گنبد مصلی امام خمینی (ره) به اهتزاز درآمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farsna/446574" target="_blank">📅 06:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446573">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/553be7ddd5.mp4?token=qdYPG_ln3WhGVerAbclSemkGrWG95GxY_l0wpc_ijsBQNsZ0A39UqPs3tj1xJjaUzSudHBZ1m4Htb07ww9vqfIGyCW9REyOMLzzKoUX6iIoEb-awppQ3LYT344mO7C2RnXyo434ADFDxNAr8KF5a6wDMAUzvZHKdyDZ2AydasqZzHIFrEfe3erqh9yJ6rwaYLDHcnRI3RhyDMpPoCP9XvmPEoqtHMBCZ4bRaZaAlhGu-80wUZp60shWMV8cylnTSQWCQIAd7o0rMVsS8mDVfXKx3VMSoekuyNConyDmmxE98Oihwd5Kch3MEsHoEgeBSakLR3Al6mWjgzJBHwK9fVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/553be7ddd5.mp4?token=qdYPG_ln3WhGVerAbclSemkGrWG95GxY_l0wpc_ijsBQNsZ0A39UqPs3tj1xJjaUzSudHBZ1m4Htb07ww9vqfIGyCW9REyOMLzzKoUX6iIoEb-awppQ3LYT344mO7C2RnXyo434ADFDxNAr8KF5a6wDMAUzvZHKdyDZ2AydasqZzHIFrEfe3erqh9yJ6rwaYLDHcnRI3RhyDMpPoCP9XvmPEoqtHMBCZ4bRaZaAlhGu-80wUZp60shWMV8cylnTSQWCQIAd7o0rMVsS8mDVfXKx3VMSoekuyNConyDmmxE98Oihwd5Kch3MEsHoEgeBSakLR3Al6mWjgzJBHwK9fVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هر لحظه بر سیل عاشقان رهبر شهید در مصلی افزوده می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/446573" target="_blank">📅 06:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446572">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a292515d66.mp4?token=RRuatViStVeKpzlrjr-qwfyWOBmCUiSseI--bLr20wN5N5d80aafJCbN_2XTQVq9cwuElWcWZ-eZSfejwlde7PgKcgHihYEcyUQt5pKD3do_v7NwZcVWShvkIL5lFoQFXOLyxkU03ATdclm7hxo-F-Wg3nUw_6W2aJN7bB4XoO-3LQgOlKOrrnv67kqWJ9j2PlY1xBgHlZTRDxrREGtvtNOqr7-k0OPVB2nUdUkfKBAtHrHsdpH4mrdQzC6-KbuBfYAkpXBHvviy7N5WW8E4I8Kh5FXYwxeZE2aHYealP8UqpGhlZh_w5i6IaFINVz3aUVWFzUbevn7Lm_4GPHWXmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a292515d66.mp4?token=RRuatViStVeKpzlrjr-qwfyWOBmCUiSseI--bLr20wN5N5d80aafJCbN_2XTQVq9cwuElWcWZ-eZSfejwlde7PgKcgHihYEcyUQt5pKD3do_v7NwZcVWShvkIL5lFoQFXOLyxkU03ATdclm7hxo-F-Wg3nUw_6W2aJN7bB4XoO-3LQgOlKOrrnv67kqWJ9j2PlY1xBgHlZTRDxrREGtvtNOqr7-k0OPVB2nUdUkfKBAtHrHsdpH4mrdQzC6-KbuBfYAkpXBHvviy7N5WW8E4I8Kh5FXYwxeZE2aHYealP8UqpGhlZh_w5i6IaFINVz3aUVWFzUbevn7Lm_4GPHWXmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیل مشتاقان درحال رفتن به‌سوی مصلی هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/446572" target="_blank">📅 06:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446571">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/401e987e60.mp4?token=mz3srbxE0IUSxeNZ8Tj0VPGwpv55X9RzbDQY96d7KXnw0IL-d-RAXAKjKZNtQFwySbfLmn-kHTPHtgt2wQpJSvi7hKDbd6jUBU91nKU_yFHbjnzwjj2Nm2CTMWw_gT8aadJLRTLZL4tQ9dzE5IenWWAuj-UbdaHtb15q58GULxlrIRpa-I9KaqVGPq2Hryjy2pDMKZKsauBIIfcY3oT1QCluEWSOLl8uHy8AYJaLPOEUHLKuZDT2qJuJ2ZhQz7Pew3JnO44KUYURP4kpaSt-L683IQV_FBb9m7753N15a8ExP3JNuHqT3B2wVu6RnrrIMatyqFmvqhoUf_JqwJ7sOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/401e987e60.mp4?token=mz3srbxE0IUSxeNZ8Tj0VPGwpv55X9RzbDQY96d7KXnw0IL-d-RAXAKjKZNtQFwySbfLmn-kHTPHtgt2wQpJSvi7hKDbd6jUBU91nKU_yFHbjnzwjj2Nm2CTMWw_gT8aadJLRTLZL4tQ9dzE5IenWWAuj-UbdaHtb15q58GULxlrIRpa-I9KaqVGPq2Hryjy2pDMKZKsauBIIfcY3oT1QCluEWSOLl8uHy8AYJaLPOEUHLKuZDT2qJuJ2ZhQz7Pew3JnO44KUYURP4kpaSt-L683IQV_FBb9m7753N15a8ExP3JNuHqT3B2wVu6RnrrIMatyqFmvqhoUf_JqwJ7sOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد مرگ بر آمریکای انبوه زائران در مترو
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/446571" target="_blank">📅 06:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446570">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36339aa371.mp4?token=mgiWanhiTkuWfe7v0o-8W_tthw13xgLNkLSnR07dnAiMI47WmYP74W_heyjyPlenYvi2bN1QyGi6Cs7naam6UpCfEjo51J4f0KETN1dm_rNawvsZWF34k5_PKIhP03PB-sWn3ehWRgTT0f_EViZ3KXe_L3qKOQyZWM7S0w4bPe2xck70HWO_04R7rv5BPzbfvxmU4pIES-Z9Im5fScxFvDje6ixT2-R2aUGS03kOnuwM2HnisLsc0xmM9Jn3uSQN1esDSWEdDWgBmK0yoG7xWispY7cFQqQegy7zM5ytoAOx9Je0_t1dSSH-xD5bh41tydVo66vFZq1fXxO6lquukmD1yXzdkGS_WRdp0QX2rbxzWvCD-Ndrf_WRGqvUNjL-kzBHf6qKPjvp7K5zJM3jA6BfQ2aIZ89IojtvA-5yix1cS8BfpwXWapK1IyhhgS3_w7Q_C-DH6KNnw53S5wQYHcoW8-e_8Xe-OkPFwrrlcgd50LMJQNruj44aIiYGTCUX6HTwwGPjQQUsIanSJC8CBtCvopKjuoSZig8tLi8oL2XPFUtBDpZnHsoOTJJsyr84X4TLpKe6SL4cDkxCOrBXbBmfnqtW-5XlpDkERqdegepqeYqRFSlEGZxXEiZkJ_5eTKk5Eo49hIVSWGv9WK7GmLH39OMpg_hvee9e-Lm7axg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36339aa371.mp4?token=mgiWanhiTkuWfe7v0o-8W_tthw13xgLNkLSnR07dnAiMI47WmYP74W_heyjyPlenYvi2bN1QyGi6Cs7naam6UpCfEjo51J4f0KETN1dm_rNawvsZWF34k5_PKIhP03PB-sWn3ehWRgTT0f_EViZ3KXe_L3qKOQyZWM7S0w4bPe2xck70HWO_04R7rv5BPzbfvxmU4pIES-Z9Im5fScxFvDje6ixT2-R2aUGS03kOnuwM2HnisLsc0xmM9Jn3uSQN1esDSWEdDWgBmK0yoG7xWispY7cFQqQegy7zM5ytoAOx9Je0_t1dSSH-xD5bh41tydVo66vFZq1fXxO6lquukmD1yXzdkGS_WRdp0QX2rbxzWvCD-Ndrf_WRGqvUNjL-kzBHf6qKPjvp7K5zJM3jA6BfQ2aIZ89IojtvA-5yix1cS8BfpwXWapK1IyhhgS3_w7Q_C-DH6KNnw53S5wQYHcoW8-e_8Xe-OkPFwrrlcgd50LMJQNruj44aIiYGTCUX6HTwwGPjQQUsIanSJC8CBtCvopKjuoSZig8tLi8oL2XPFUtBDpZnHsoOTJJsyr84X4TLpKe6SL4cDkxCOrBXbBmfnqtW-5XlpDkERqdegepqeYqRFSlEGZxXEiZkJ_5eTKk5Eo49hIVSWGv9WK7GmLH39OMpg_hvee9e-Lm7axg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمده‌ایم برای بدرقه پیکر مطهر امام شهیدمان
@Farsna</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/446570" target="_blank">📅 06:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446569">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a9d38515.mp4?token=Wvb8UpOiJWP24TgC6xrEC6s5zw5pnJVIdMobDC3k9qwadVZ20V6e_JNWTWyhPL8ClxOZ-DJH-FiX2zuaW9imP2kapBEwoU4hKNE7K7hXkmBzWNdLxeid3OxJPdYJccwu5PzNneGPnDCMb-hA4d3DUVwdin_6hqfrsof9KC0P9_2tlfgRvqt-EQAljaVyxqDbU4ocIZCatiixbFBIWlHAbzDY4PRcTXjIuBm8EAWsXO8ZA6KYt_6Z3TWrTl_czqJkpIV44XctMkqQTKwJU-O_0YYtLjcL-sB56FAkpfyO-Jb0n97h-ox8d36DdC4-oJyck4a96jZgcXf7LxJzWaZk6IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a9d38515.mp4?token=Wvb8UpOiJWP24TgC6xrEC6s5zw5pnJVIdMobDC3k9qwadVZ20V6e_JNWTWyhPL8ClxOZ-DJH-FiX2zuaW9imP2kapBEwoU4hKNE7K7hXkmBzWNdLxeid3OxJPdYJccwu5PzNneGPnDCMb-hA4d3DUVwdin_6hqfrsof9KC0P9_2tlfgRvqt-EQAljaVyxqDbU4ocIZCatiixbFBIWlHAbzDY4PRcTXjIuBm8EAWsXO8ZA6KYt_6Z3TWrTl_czqJkpIV44XctMkqQTKwJU-O_0YYtLjcL-sB56FAkpfyO-Jb0n97h-ox8d36DdC4-oJyck4a96jZgcXf7LxJzWaZk6IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
جایگاه پیکر مطهر رهبر شهید انقلاب در مصلی تهران  عکس: صادق نیک‌گستر  @Farsna</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/446569" target="_blank">📅 06:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446568">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uh6eyhRJ92FQSBeEy2a7FvmBID2J-cxf-0ujnB739bNzclOT0dl9wkiKIeI6Xa-jf4iAqssxd1SsgmPviad2D4qe833vm9sDzBJo6wpcgG84EFOiOOMzkzF2u9qqzvfA_r9bYSqnT4KEXacbpJD3WyGEdMIeWg9QV9AZjZflLMH-96AbQxjFokWw1tTMwFXxyiUotysffJ6C0AUVfWemnq07XWeL_qbkJAxWitjSuiBywtfZ0AK8RStXeFYuYS__CzSmLfudLptPbPV8W7Now4eYcZ9i1eDJdfhYmudaDnyr88omA27Q_CR0Fswbend3Sguh-0yqmGRQ2NY5EeQKhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
آماده‌سازی جایگاه استقرار پیکر مطهر رهبر شهید  عکس: صادق نیک‌گستر  @Farsna</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/446568" target="_blank">📅 06:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446567">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f1e09ff6.mp4?token=hoPys8_Xtz3eBaXv87OjZI_qoDKlNhUROB2jpEMkNLeOFG4RJDTXoF3zj8rlAUnr1GTlcdaap9rgbAzwoFX0N1Ov23aw92BrDYj-pZnHcXL3ax4hpVqH0wWCHr0wFTjIygRqLg-0RLHhi3ec5IBmQOgtXGHBtgMZSleq6Lm__GZPEtVL-DoUPpoNp5ztCpqYpvTEpL4k5GlyUBB-eDTkBX-Q_w0tfQdXfWA8-rPhAfaRga2B_2neF_UYn9XsCXjRr5zjXNYvcqhzApcn894q-Ek25CdUhUufml6QW7Oyc0_9HdgvIlmkmdKDNbBG09Eu_lWGkti6IFBDv6MRcHaHyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f1e09ff6.mp4?token=hoPys8_Xtz3eBaXv87OjZI_qoDKlNhUROB2jpEMkNLeOFG4RJDTXoF3zj8rlAUnr1GTlcdaap9rgbAzwoFX0N1Ov23aw92BrDYj-pZnHcXL3ax4hpVqH0wWCHr0wFTjIygRqLg-0RLHhi3ec5IBmQOgtXGHBtgMZSleq6Lm__GZPEtVL-DoUPpoNp5ztCpqYpvTEpL4k5GlyUBB-eDTkBX-Q_w0tfQdXfWA8-rPhAfaRga2B_2neF_UYn9XsCXjRr5zjXNYvcqhzApcn894q-Ek25CdUhUufml6QW7Oyc0_9HdgvIlmkmdKDNbBG09Eu_lWGkti6IFBDv6MRcHaHyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجدید بیعت لرهای بختیاری با امام شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/446567" target="_blank">📅 06:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446566">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e34406c17e.mp4?token=HSr2Yod9ShkTOhmoD_shhSg73BTbSST2izckSCCwhHwBYupILgX70nnpzSaobCQDxCDgfEU2Q7_-MVZ_Ns5Loumf38YfWeWwPOyTtgcFtOQjCMBU9868MF74H_dR5fP4uUTj_Xbpmv9YSXRmROl392MeynHTZb1rkyHM8HzMNialzazcR4ZFpdY__0aeA3wFr86O6xX8L5XVP3V2LeaQArJ7BYzV1SxmwSmciJrIKVYNa-wo_1ays4RdE4cF08dNo3QPBIWk5vChStrmM7UAXX5g5m8nlWfu3kKq3pl_6vcc-VqnueUr8zWvv1ykuOE8wdBn4iJaZVzuym-MAM8vjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e34406c17e.mp4?token=HSr2Yod9ShkTOhmoD_shhSg73BTbSST2izckSCCwhHwBYupILgX70nnpzSaobCQDxCDgfEU2Q7_-MVZ_Ns5Loumf38YfWeWwPOyTtgcFtOQjCMBU9868MF74H_dR5fP4uUTj_Xbpmv9YSXRmROl392MeynHTZb1rkyHM8HzMNialzazcR4ZFpdY__0aeA3wFr86O6xX8L5XVP3V2LeaQArJ7BYzV1SxmwSmciJrIKVYNa-wo_1ays4RdE4cF08dNo3QPBIWk5vChStrmM7UAXX5g5m8nlWfu3kKq3pl_6vcc-VqnueUr8zWvv1ykuOE8wdBn4iJaZVzuym-MAM8vjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری دستۀ لرها در مصلی تهران
@Farsna</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/446566" target="_blank">📅 06:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446565">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e02c94e76.mp4?token=QTEBrbZ0zmd0fiiEjf0QaejDX0k0KkDU99BkQri6ChR691NOQTKtt5pK3YXLq--mZIUGwXm43n94wZ-GPRB1d124OoSeuJbK1kg7xxTaO8I-28V8Fi31KbMuUJrfRtYQKuVmvTeRZ7BdVHjg91NG4JAKQtuOp9Us3UX8FX1ubB3YnN6I9yL9hgh4ulr3EBDHhvLX0IOCNew3TdD-IERSiQf4m6tEIWLdm1DAPQ0abLeySvNT2Mz9_5EFMhQgYEnK4Fs5fju7LYaL5N__Ua0Jebi1Hp0oWgQkv9EhbD5-18-JSGxYdOrDuXxt0EA199U_1S0MAKoLZ7sz1ZeR90FJ9kJdaOmVXT_g2ZP4Bhb9m8SCgeFA-oIh2xBcVAo_Wdt8ieWdtPJS_oikCGlWoRH8KjwT_99ajOumnn3BjftF-Hi98fXqpDyaH7rAjcJoosbBWvPQG5ZBEmoE2WVODR1bahDw5vCUjiFXcnzmJzz-1BmT3mi__6nq0PxT3hbqn6KCiijH2HHdaQ4liPSqJalOxP5BBXjio-EfqVZomUnhhgs4LAAtPBkyVDjfIBJciAME1Em5fy_Oo7YdXPCGn_O4HO0izP_cPKcz18kq03e4sTe0zQ20FyW5DyIRBZFBrVL036gHmFj_kKeIVBLwMo8o3YkblGpy1-s8_J3QnhTbPW4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e02c94e76.mp4?token=QTEBrbZ0zmd0fiiEjf0QaejDX0k0KkDU99BkQri6ChR691NOQTKtt5pK3YXLq--mZIUGwXm43n94wZ-GPRB1d124OoSeuJbK1kg7xxTaO8I-28V8Fi31KbMuUJrfRtYQKuVmvTeRZ7BdVHjg91NG4JAKQtuOp9Us3UX8FX1ubB3YnN6I9yL9hgh4ulr3EBDHhvLX0IOCNew3TdD-IERSiQf4m6tEIWLdm1DAPQ0abLeySvNT2Mz9_5EFMhQgYEnK4Fs5fju7LYaL5N__Ua0Jebi1Hp0oWgQkv9EhbD5-18-JSGxYdOrDuXxt0EA199U_1S0MAKoLZ7sz1ZeR90FJ9kJdaOmVXT_g2ZP4Bhb9m8SCgeFA-oIh2xBcVAo_Wdt8ieWdtPJS_oikCGlWoRH8KjwT_99ajOumnn3BjftF-Hi98fXqpDyaH7rAjcJoosbBWvPQG5ZBEmoE2WVODR1bahDw5vCUjiFXcnzmJzz-1BmT3mi__6nq0PxT3hbqn6KCiijH2HHdaQ4liPSqJalOxP5BBXjio-EfqVZomUnhhgs4LAAtPBkyVDjfIBJciAME1Em5fy_Oo7YdXPCGn_O4HO0izP_cPKcz18kq03e4sTe0zQ20FyW5DyIRBZFBrVL036gHmFj_kKeIVBLwMo8o3YkblGpy1-s8_J3QnhTbPW4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علمدار ولایت، لرستان به فدایت
شعار لرستانی‌ها هنگام ورود به مصلی
@Farsna</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/446565" target="_blank">📅 06:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446564">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94777c2b96.mp4?token=noG_KUAN-hX9CgYKx8quQJi7_qHshkw2-EyH2-X_k5Q1Oit8ZD9e0rW3VNrNQMXLdSNxkN41N9aZ3bVlsG7IkbGkiLGKYgcYxfNem1PB_pcxKnGZjShvtD9Lg6Fophc46JfrXOrqrXnCiH92QOYUiKsAJlJl3aQes25_LiR38N1SiokJiII83bBoAcBWUS6CyladpmfSht2U6ivDv_ksNQzFMD6sAhc0DLFzG7mu32XbfInwsQ1XXkULa8PS6Q4cI1Q4ZoqLAk8LNejafg9_PY3H4teykasiZKLnbBcabFf2F6bWeARyKpH94J5cremk6MjqyU_I7oJOyetErp-L6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94777c2b96.mp4?token=noG_KUAN-hX9CgYKx8quQJi7_qHshkw2-EyH2-X_k5Q1Oit8ZD9e0rW3VNrNQMXLdSNxkN41N9aZ3bVlsG7IkbGkiLGKYgcYxfNem1PB_pcxKnGZjShvtD9Lg6Fophc46JfrXOrqrXnCiH92QOYUiKsAJlJl3aQes25_LiR38N1SiokJiII83bBoAcBWUS6CyladpmfSht2U6ivDv_ksNQzFMD6sAhc0DLFzG7mu32XbfInwsQ1XXkULa8PS6Q4cI1Q4ZoqLAk8LNejafg9_PY3H4teykasiZKLnbBcabFf2F6bWeARyKpH94J5cremk6MjqyU_I7oJOyetErp-L6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصلای تهران و حضور مردم برای وداع با آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/446564" target="_blank">📅 06:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446558">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SCV1euX2ueAmkWHrBAcV_mVQVpZPbBIx-UsHLeAN6ut57qdHBch8ktJEE6e8ibeYWRFQ_baNdB9HLbJ4tB4B6j5YK9ZDcJjD6cacNUSzdcjUDlsUD_4fqng9W4vX8kcFV2J-YHC1mQpSOSI69adei2spvTQwpzD-0MJGJhseMeHgpxBWWH6bRK76Ix67jCRTDIAvu94ZJBBANzxfYqTkO7aRITo92OUTd46Twib7StrwMwTYtdAkvxXQS6S4FbBX4NEQrtQOTRmKkOOh_x3Q9El2RNobIuio3UHBgiRulIMmq-_OndsIjMhdS8fE7wW1YXn-xdZ5rlUcD96Afr1ENQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PCECuXdIar8lWzUvzUCTf_aGgbkaFHIeA7w-zXvkyQLQYYFxlL3kbeBByJ8niUKJZqWWGxzduAYSUskvpmG9w2b1r8MdTbTuZZLl49X_bj-eklv4ulJRSKJ4cbbTcncjc1yLAAxRL3VpwvtTtc1YWJszDqLsuEuMYpRKEmaBNyaPaNKVlgErB1szjZP6GFzzIANG0WRUyNW_MqjwPE82A49I3jB2Xj5MtcxSF965Enf6Afw7WUb39OlqPs3ZkDZnNKIg6tfXStQwZF78xSVYdkGL0JsUGEkZQaFUG5zKxpUjCIgQ9dvyiGw4KR6W2Z9UhwDGb4Q-R3XTMSwYzk7JTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oDjHJhEn_bFW8KOEMud9wgCtMGMJ6rGEuxcS-NaP3_QhSEJuDwCU3DSpoPAT3uxNZ56639tclDJrtdixN4KzFgCpmm9Aa5V1G0X2yvA7yf5FJ5IK-F7CscP430ZQWgfKhUZpTazuOLmMgscTsEbRAfTggA0fstedUx25Yn87gueDL2VnJUP-N_nS3EvfMzeXm5504v0QyGePWhakRRLhDFtBTYWQpzfzz_rw787nlRqtUOuoGifL-xgaKs5K3Htnb8tdjFWEDSh3RU7c49TswyErIgToTpvKsA_4SV17_Q9iTclcJbH6dJ-6XbSWUK1lOrW2d1p6_R9QO7HFvf04Vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آماده‌سازی جایگاه استقرار پیکر مطهر رهبر شهید
عکس: صادق نیک‌گستر
@Farsna</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/446558" target="_blank">📅 05:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446557">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🎥
لحظه‌شماری دوربین‌ها برای بدرقۀ آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/446557" target="_blank">📅 05:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446556">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7861e5f68c.mp4?token=viWiPzYFzliL95e04z_Gs2sVNUDQ4ZXTHWO9RCUEjr_jTwW-P9OARwrJlun0X295NqejMkj9ivBY-PsBZIT-UfEaZ8xAImuX15DoJhZ3zYAKFX6LNBQQQrLcljgXZCS1EFTWv78Q42lrn3d6BcJcBD5R1LixLvm5KiR2COGFS5PiMGB13V5yA0AU9neTfMghqR5RjqKby9R9jPROnsupJUdFWXDfF_VcyT2y_Boao2LS2WfwCkue5PipmvKQ0XhsrKesJmUy21sf1G3UVzR4A4-TnSKRSNHy8vrD3hXfK27xCpAW0w9RRNlgFPlK4koMODwiJDeX6UTCWJAfAUX9rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7861e5f68c.mp4?token=viWiPzYFzliL95e04z_Gs2sVNUDQ4ZXTHWO9RCUEjr_jTwW-P9OARwrJlun0X295NqejMkj9ivBY-PsBZIT-UfEaZ8xAImuX15DoJhZ3zYAKFX6LNBQQQrLcljgXZCS1EFTWv78Q42lrn3d6BcJcBD5R1LixLvm5KiR2COGFS5PiMGB13V5yA0AU9neTfMghqR5RjqKby9R9jPROnsupJUdFWXDfF_VcyT2y_Boao2LS2WfwCkue5PipmvKQ0XhsrKesJmUy21sf1G3UVzR4A4-TnSKRSNHy8vrD3hXfK27xCpAW0w9RRNlgFPlK4koMODwiJDeX6UTCWJAfAUX9rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری پاکستانی‌ها در مصلی امام خمینی(ره)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/farsna/446556" target="_blank">📅 05:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446555">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d096f553.mp4?token=ZL-nlG5N6hzkH3_S4346waOw56JDmUGTo5l72O4OVWNBbIUh_t54t53a10WApL0XQhYAfKatj2wKUtabMyV4wEuCFIcQQ9Y0MzDynvCRtXcaY42U2d7MJ_s_KdxJ7G_UvBQHbw3_GWgcClCW21ojRou6kNsg21I2zmpA1uqA9PFaKhGSeyzovm846-vE1KruOC-7htFRUVmPdvioLM3O0HiZLofwIUqMaKvDobnNZatcYlOFtmZwi7weRUrxpa-E8Zw7EgJRJGmGMqSclZSbDjbKuhYg04atSIhkNX6rKW8eytW1M6YUTeYoy1yiJVqpXs3MlgZGBeKpMq1tTb3eRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d096f553.mp4?token=ZL-nlG5N6hzkH3_S4346waOw56JDmUGTo5l72O4OVWNBbIUh_t54t53a10WApL0XQhYAfKatj2wKUtabMyV4wEuCFIcQQ9Y0MzDynvCRtXcaY42U2d7MJ_s_KdxJ7G_UvBQHbw3_GWgcClCW21ojRou6kNsg21I2zmpA1uqA9PFaKhGSeyzovm846-vE1KruOC-7htFRUVmPdvioLM3O0HiZLofwIUqMaKvDobnNZatcYlOFtmZwi7weRUrxpa-E8Zw7EgJRJGmGMqSclZSbDjbKuhYg04atSIhkNX6rKW8eytW1M6YUTeYoy1yiJVqpXs3MlgZGBeKpMq1tTb3eRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات مسیرهای ورود و خروج زائران در مصلی تهران
🔹
درهای شرقی و شمالی مصلی برای ورود هستند.
🔹
خروجی خانم‌ها از در خیابان شهید بهشتی، و آقایان از در خیابان پاکستان می‌باشد.
🔹
اگر خانوادگی به مراسم می‌آیید، بهتر است از ابتدا محل ملاقات با یکدیگر در پایان وداع را هماهنگ کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/446555" target="_blank">📅 05:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446554">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c92a96e1b7.mp4?token=TYhWjWx7-YiMEZgMAyiaSckxAFyBRle0q6on8SbWQANugHewYIL83_iB2KtSPmjQQiVtVI93OrV3ne72xAvfhmnlca1OEQ72ErRrquXm9Yq0LQiHlGDrAQSdHqFuXtTaHiC9vISTdc11B3hpLKVzODvB5_cY9vsNFVULp0jX5yNCZmMTZ_Nt5bYcyEzPYKwHfVmmwIVMUJ1QmvYpZr-CNKeb9Ty1-ei3cJJ58Y_HSldWXHj5SYVnWRXRzZJPJZUDI8LJNqd1chGotIJ844xhY_7X63h-FpIsiF4gecNqi8SafvC0CvmWDPhEI9vT-uAHUv6T6JLQgu6O5hVflUogWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c92a96e1b7.mp4?token=TYhWjWx7-YiMEZgMAyiaSckxAFyBRle0q6on8SbWQANugHewYIL83_iB2KtSPmjQQiVtVI93OrV3ne72xAvfhmnlca1OEQ72ErRrquXm9Yq0LQiHlGDrAQSdHqFuXtTaHiC9vISTdc11B3hpLKVzODvB5_cY9vsNFVULp0jX5yNCZmMTZ_Nt5bYcyEzPYKwHfVmmwIVMUJ1QmvYpZr-CNKeb9Ty1-ei3cJJ58Y_HSldWXHj5SYVnWRXRzZJPJZUDI8LJNqd1chGotIJ844xhY_7X63h-FpIsiF4gecNqi8SafvC0CvmWDPhEI9vT-uAHUv6T6JLQgu6O5hVflUogWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دودمه‌خوانی لرهای غیور قبل از آغاز مراسم وداع
@Farsna</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/446554" target="_blank">📅 05:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446553">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c7e2db8e.mp4?token=nDCVKqIeiJnCN5nMVUkA5Cg1uBjXxDMbdaBqLBXDLU37nd0jd7naWSeJapPBzlSeFogJ8CiWlB5s5tET4dWACADVjmLS4jpxbsvglAci-Qa4i71HNV0tNyRF6odqHAL2U_qnoc--4nVGXJQfDd2ah23tgb9ycz_0x9N4gwBaHWH3vAUIJ5Aq9cdifluMXKUAGWP5rm0sokCChEjLCnO_tnkqQAu_m8qZ5eS9T3msyN22foboo-YCM6Ki70bPAmzGM_9zqR6mIce0qBEJpyhJcHxduLH88S7kpALx9bCyVweomGxSmDryoXnkiCNrYrtZwxo4Ti_Gp_MpBOP3nbWxoyRt7Qq-mzufbixs3X5OkIKjyK00xsll_KCc9q8lOLUHY1DCFmooplKqdNn5Fcm5g7FN2ZQkotI_hPNYvdjUCXj3sUmoeTeU4al5MFWSA-1Ql7Dw-7qCfD0Gg1B8Ys-ohs2cIGfrZ7QLkBPGrqWP4R665dnWhn5cGZPUeeGxLhoEJziJuPq8YsEkY1IJBLunKy2QkafKU-1RIpBl6B8vi55tIblU1AvCFnZWUYcCzsAz4xOfgkPIR5awaNVAktoWz7YumZdyKBLBopv6y-0N3Md7boA3WitX79gYDdzBBwFrFpSYhJbfUQ3iTcvdfqnD3ZAs2W_WMdl5OPwtEniB2pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c7e2db8e.mp4?token=nDCVKqIeiJnCN5nMVUkA5Cg1uBjXxDMbdaBqLBXDLU37nd0jd7naWSeJapPBzlSeFogJ8CiWlB5s5tET4dWACADVjmLS4jpxbsvglAci-Qa4i71HNV0tNyRF6odqHAL2U_qnoc--4nVGXJQfDd2ah23tgb9ycz_0x9N4gwBaHWH3vAUIJ5Aq9cdifluMXKUAGWP5rm0sokCChEjLCnO_tnkqQAu_m8qZ5eS9T3msyN22foboo-YCM6Ki70bPAmzGM_9zqR6mIce0qBEJpyhJcHxduLH88S7kpALx9bCyVweomGxSmDryoXnkiCNrYrtZwxo4Ti_Gp_MpBOP3nbWxoyRt7Qq-mzufbixs3X5OkIKjyK00xsll_KCc9q8lOLUHY1DCFmooplKqdNn5Fcm5g7FN2ZQkotI_hPNYvdjUCXj3sUmoeTeU4al5MFWSA-1Ql7Dw-7qCfD0Gg1B8Ys-ohs2cIGfrZ7QLkBPGrqWP4R665dnWhn5cGZPUeeGxLhoEJziJuPq8YsEkY1IJBLunKy2QkafKU-1RIpBl6B8vi55tIblU1AvCFnZWUYcCzsAz4xOfgkPIR5awaNVAktoWz7YumZdyKBLBopv6y-0N3Md7boA3WitX79gYDdzBBwFrFpSYhJbfUQ3iTcvdfqnD3ZAs2W_WMdl5OPwtEniB2pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای موکب‌های آقای شهید ایران در ساعات اولیۀ صبح روز اول وداع
🔹
نزدیک به ۱۰۰ موکب، بی‌وقفه خود را آماده کرده‌اند تا با تمام توان، میزبان قدم‌های عاشقانه زائران رهبر شهید باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/446553" target="_blank">📅 05:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446552">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9ad1d11e0.mp4?token=Y_ASxYWbxpYxknFSgbZl1_KnEOhfJeEF9AaGgG9cSEwpjdTDVmC3r3W6JTbCFP-XGy3mM098PffJHmVTS5AZZezajNwfuVtVBWH-08dUg89uB7iCaa4DJJYVtpov3DB0NEnWAd6vg3QhP_C0-q6FnthZKI1kszBIQzCV5JSf1sSyz_wm0TJxQySROS5N9fSDVwtIwX_h4QzuDjfmlf3fmpmK3HAGMd_3M2qw3Kokz7KVyAXVRisCl6khU5Nh0XSnTxshHIB5EUa0IkGAzVmbySjwCJ6vuUFdJiVR5GzvGjeeDHCSPzHlmIHnyWbk09aAdc9LRP4KnTab5TuW3NdQ0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9ad1d11e0.mp4?token=Y_ASxYWbxpYxknFSgbZl1_KnEOhfJeEF9AaGgG9cSEwpjdTDVmC3r3W6JTbCFP-XGy3mM098PffJHmVTS5AZZezajNwfuVtVBWH-08dUg89uB7iCaa4DJJYVtpov3DB0NEnWAd6vg3QhP_C0-q6FnthZKI1kszBIQzCV5JSf1sSyz_wm0TJxQySROS5N9fSDVwtIwX_h4QzuDjfmlf3fmpmK3HAGMd_3M2qw3Kokz7KVyAXVRisCl6khU5Nh0XSnTxshHIB5EUa0IkGAzVmbySjwCJ6vuUFdJiVR5GzvGjeeDHCSPzHlmIHnyWbk09aAdc9LRP4KnTab5TuW3NdQ0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداران امام شهید، ساعتی پیش از آغاز رسمی مراسم، خود را به صحن مصلای تهران رساندند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/446552" target="_blank">📅 05:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446551">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g119zrocWqdO5EQkl8-BBA5qeWNW3nx8G2e2Z6Zqcr33ZNJKlXGCJZ0vxVOjzYJxW2QO2zlw7WzqlkqbVVacpuz3t2vPCcxRmNLxwfvE_pFvnETVQQWp4wpt1qG0WVTEDi3Sr7y9RXVMT6hHi5SYkP1Y5z5XU1AWKBA7soNezdXjGxwol-bthJoqxi-aDRMj7Y2lNO5-70xaVI2Bq6ge1vRj3cI-0HlUa6Hupdh-iXprKZS2QfIyFvykyvPlt-5DLfgo4jGgXmK3__wF5BR1V0-UCnqyY9piRk7DDiLXOoUf6kpIqTgRKc4XFlpp81GMay9Lyy-u9Q_wlY80F8Un1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
طلوع آفتاب به افق مصلای تهران
در روز وداع با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/446551" target="_blank">📅 05:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446542">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kcdb4cRxyACukdMQ6qSjIrjOnkVDIb8vyh_ZqpnhSd25iGvkjjzt7crQAfCMlV8Xy_M0jZgbMWL9iVXXdhThMw5buYg61r1JVSiDkeOR0kdPuNYq9YhiVC6AMEcv0pIw3Ou8LXROIjNQhN7TPde9RD5QA4CoYWrHUkB6JyPbOM0Qc3RWgnYFZW-0Du8hIqo20ist8KJQqoypxjVUEsl8cWSOD7Np0IYQoOJTtZER0kxknfXD1EQdao8N9UVe6_j_WmxFSBB2-sJHoCBrgb5YHN2sSCvJzTj3Y2hH2fGWlyFxATfVhKFO3L2yox9nhCBs3uFdrX-zoq5_edU8Z5Vy-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oPSykQP3fsMNVVoUh4zey6K0ma6t-ZClqDYzl3Q-hgmaK4MJNXnSpTTRu54c53JbvNF030ojnZvXZIg3zaZuYw47LtHqg2hZMX0ZPITQt2yTcFL6hP3tQ63GObX7-EeSLpTeyq54Q5Yldr-FoLG8R3A4sBJpqGQmZw-T1WX_PUIMSJIHDADn4Tum98_n3JSz6Y17CJYyc57sr3RpGo-z7HnSIzjinZozh4OKyJZc0LunyeMAnxST2XHJ8RZkR0x3GEEjNJwKA8KQDQdeBALjDaQsx0mmZ512PIYgO9Bg0LponlLIfIyEn358jbifWnLctP45YKSGcyKSS-oPlgWlMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N8d0zgs1GkMEJS3EbJqCSqnuTaYTD_a9Qio8AG78xnuHWRdXWg_4-dMf2ctYPoUOHhkMmLuhynZYI9TtiMhweF5dIsbY7MCnBrG5KXMDyafyv7UfrLApyEPdLCtjlgXoITWWez7okrB3s35mNvU6V4_wo6qUITYaO2IoafopBJw-JSIQNSHl28mPlvLK_zFHX4c99NGEnZ4kTXwbAU26IjARzKn_sJyGB5ecSMeZW9kKizJzmrqV-UfnaUycuCpFK7pcDmO6_menBI9j3-18VkIK-iI084n5uLrqcq6J41uy8ymROm3MLRSafn6-fYYPo73t8Qi6KAqVCn_Xk81L9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ikWVcmQOVJXyZhZY6w3pMcGa9mYTXC8G4zkJc160lfrJYi6NGPF6zFKKddmpUiXAGnYoOvlV-IizJ18-gIYhaBwIlbAPrB6OtaDyoZIyQo-xSgJ_UMr_P0xX0A-AWFBA3qFPbDv7onaj039VCjlIMV_AE0Xmlo57X01ur1Pfa6TYyU5U9bKxziBmb8-cMIk1k4r2oqaTd3ZrXIwCtmTstJGwtFZ5Do64BIVivHpqlwmVTdLKpUY1ZdQPAYuFlEHnGRZeaN6HoENEY-lIvq_RZeWvLKHFicPuNOC8cbr3VAPok9r4HoJCga0fRz3Zi_ski4Qn1L3qjoMwZI7KLKvu0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k9aRmTAQTIBkaJ-qBxh8er6s1IVCKfdTvBKNASsfdrCEuR7FaCvC72VfKnVXVtDvPQX_S7A8H4eKXEWQ_eTEctH1R1ivyqWU5TE23ORfTowxedBR3nWhWxwUckbGtvcku-mD6Vz3Fx0QTOqQfhvGEzafz9jA6-CDGyXGqB9gWNsGLdmtKan8-6Hww1nhtPijyb_OLYh6XiHTSz0mg9PBfKzrBT4TqFXP2JtU9v0RrQmvboZufm3Lu_w1jo2cmx-TN9XNmhBRwaKSjVEBd5xn0R1szBG6xrQ9500_k5Td0BF_-bK39qPsJHGtysEabNJIORupleuomEghw_HSAQVtTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LozmVqe93NCQCDfcABiE65PaHeeSFe7hIDmbGWooroG5QVC9leuTcfkFl7qdKjoV_j8SBVTx2Spwap00kHN2c9ExFKDJ1qR0p4bbz-8Lz77p8q3jRipk3Znai8qdXtx22-qTyjvj8tTN-gmMwUYORMxC8BYQqk7dR2vGPrLyq6BQ5LcHEvKOrL00ARLUNTe18xxgDFRjXMVfYUxBBUijM1i49zpWPLTcycMbvlbKHgKdlR4d3cNNe7ZaBelv0ODAIbuk8KQovHlp_U2IgtF2ed1JRE-rcw_hLVawv9uwhNJrN8eubh35smA61B-dVioq1fGJIvVzkAZEsDmP7WgAlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGf73aDiZm9JPYtaa6swNzzNjOdYG6GzG28yS3vqFie4APae2kbETX4Gk07Yj2WGv9hugT75gm71K2K0bbn9MmKLaadOiz-O934Qo23BdWdIk80K0x4iv5nB6BmrvIGRNiZRVROqKdxR-cW8iKiuTrbB7VzSrWrbwbJ6NtfD3JzOzLb9WVziI3DBoNIL8OjKpwe_PlHSoiwq5a4hq8szOWEvIqp33wxQsRnmn3nfsyJWJxzNNpzu1aQq0xFUAIZXh2v9g5TT1z5qUiWZdJdERsoCxj44YZ3m2DjF1gz-q6h7bpPSvOgvEBs30wqyQCSP6QOh4Kn6Kf1vpgWkOCouFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v1z7cJpD6ky7fPWWugsSX0TvCvrN_GqRfHPaoUa9eoXgem7vPIleFZoRE0p8mNppQ1LkGWrV6P5cZkIQTUlxhKOTzWD7o8FMXTIq2IBfb7VsUq8mlvTlWJU5DFqAr5tBQRsDegu7PkzUgcgDU4uXdC12Ir9-dbAViY72fBkc8c3uQJjdHN-YsZTSAQXoYP0Jo6xU7-2V924MJwwLlU0oMAomnovGu9g217RnR_TLxwEp3w5xlO2iHbTePJuGsRWvvPb0DHo7S5vRXEj_cUawNFyl82ClZ_JoWaq58Ij7Xjx3jRfSYGM0_-WVFr6O2JY0fzg25D9gv6Kub8XDdkJr9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SVp83NnyTC2mU8FAsANjkBUsoINd7FzjsmJMSx6UFripdaAYbL2HVWTQhmTYYNpDxAGPnu7EmDXAFPzABIXw29tpL3kI3n5-sOd-ttJXRevNJUSUrzclqF11tXeefu7QlJ0RcWbQiI0QOX_WlO3j0ufNQ_1jOp1oo0SCyXdkq5dd_XIC67SFxqcCNg3XrGIqAsiv_ZAyGFCQWYretbh2DPBbapouVy4znOHK6zLfwoxItizXfXOZhNSnjRyi4DQnNmfbInj00kSXUha6Ofete1rXZWlNvUnhwnIQG8giTwBOO8niHrtnE17gasNGXdekNPf1-5ecWg1oDwe5uGvCag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تهرانی‌ها آمادۀ پذیرایی از میهمانان رهبر شهید هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/446542" target="_blank">📅 05:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446541">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUJTSSxx_vLwZFZskCC8crzVrJY6wOtaI-kM9n9d4AtxHXNX2MuLe_lA6TgYLnzV7ffaJqk4R1i5ISD_MPJM5BDhU4o1qi3xSWTpK48xqreKKal_-E40HEszoiH1mvSPgYV_65kyjQ9hxM1gaTtTYUkBR0Fgb08gHc0_zWeLn-toZQnU2loATpcL5HQaylL8D9XPu5uQJ3u3n--mwm6v-jKsmJC69YWTqg5YQoYbCrgEMiBJ-DzhiKknnQXePAjwBmW7z0KW5_ROTqAGN3yKrndYK5TCqHZS9JmztPKOcKsbzC1ZU4Jl3QEFI9hEi7iTuzvtIQZYdSwzj967nghfig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پوستر جدید
KHAMENEI.IR
در آستانۀ مراسم وداع مردم ایران عزیز با پیکر مطهر رهبر شهید انقلاب اسلامی
@Farsna</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/446541" target="_blank">📅 05:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446539">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzCrDo-NB54Py8mR29BlABDUtNDTsZq6Lpy1hXQhOeqjEwCP79KpcKgI4_wwHAK-UfZ15Qo5y5qEZH0HEOtQEjIf6eRrmtK6WH6x-gsCG8DoGefS7PIXW6QCY6P83bV9mO35Ed8zh0Ku8EjV5LdqD_P1u23_e2Q7w2P2kkVrDXK7tZqhsnHU0XdAwjwrmA6-Z3fyMifndn9HC__5YTy2h3lm_aZzkR6U9pXgr6d8AJBI5EBf5GUcb_cBWKcXyMD6KeLCXqoxb3AjUufoLB7M3JJz2x8yYi9zr3MPmctQYYo4vJfxJmujk8CNRGuvYl4UsrUz30f5hgP-iVlIkr21Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط یک جای‌ خالی مانده
📊
نمودار حذفی جام جهانی
@Sportfars</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/farsna/446539" target="_blank">📅 04:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446538">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8fe59c080.mp4?token=vimZi26fSMby7b3giGjkRcrWJopEN-s0PNY3JiLyqVf3UdIERSs3_xf7ikTyNKfR0G_ndScgc0-ZoD42A31WW3LDlODYoyfa2P_VXwAEfSFOOF9AJokgZJnUP0pDYU0UADs3jizWcs5cFSlRwsz_927YWxLK_3QVkK1X734VSrwxlnuWfi-izWMagVjfzc582RDtGtg7ZBRJGbz5bLSzBeflMzOYK87nqLs_aIP39qMUrDl5S1duJOpHN0kZ8y_nvEKrVXUb0R8a7D4X4JmPT7onymm8Q_31nzImV2eb-2gFbG7814b7fumWMwSCubBTlCy0pbQ93Ez-rtXddlZ9GDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8fe59c080.mp4?token=vimZi26fSMby7b3giGjkRcrWJopEN-s0PNY3JiLyqVf3UdIERSs3_xf7ikTyNKfR0G_ndScgc0-ZoD42A31WW3LDlODYoyfa2P_VXwAEfSFOOF9AJokgZJnUP0pDYU0UADs3jizWcs5cFSlRwsz_927YWxLK_3QVkK1X734VSrwxlnuWfi-izWMagVjfzc582RDtGtg7ZBRJGbz5bLSzBeflMzOYK87nqLs_aIP39qMUrDl5S1duJOpHN0kZ8y_nvEKrVXUb0R8a7D4X4JmPT7onymm8Q_31nzImV2eb-2gFbG7814b7fumWMwSCubBTlCy0pbQ93Ez-rtXddlZ9GDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یا ایهالمجتبی، تسلیت
🔹
فریاد مرگ‌بر آمریکا و مرگ‌بر اسرائیل در مصلی تهران طنین‌انداز شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/446538" target="_blank">📅 04:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446537">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6d94ea47e.mp4?token=Cy3vGvFwOel71bs0Lu6yQSnGz-tErV1uej_GXqgA6RIUV6zjmGPl3grt9qCZcePDtYRF4LBxgJCW4eLCDXCbN3AjQ9ribtvCkC0o62tYEzQt2syjuYRVwTUX31x-Umw8-Ue261ALzNI7jNnUXp9kajesjQiOU5q--tot4YY8DjTiFV2ubjIWwXALgq_7AAWZkTD59XTQBC2hMIzy1-t6vK1i63goyX_2xmg6s2YEf5MTpkSSPH2S2LeH-7g8vltwAaSZYG6kR9v_zW2vQP7aGOqc68wkYH41EDPVJ1d_gXMSoUkakeNwWRZ9T9nIphNF3XmxZ74yOBEqN_tCtECa2zCy0e2MZMpaKIu9GbImsR78QUF5vJjQpyt-OTdNZ34l6U2cX84QyQoC7ddghiQOL4zqEu4IBpuk16dKwZhAPkOw-cM3l4IStXZ3mMVMc-x6bS5BMznM2E9Dt953rwQm1kW9ZpSCOAU7aO5ZUNzCbUJMVMj6wArTqqeRISESdbOLhKjNLinXY9qtLVq_wghm20bv06G-T2jiJnAprYsRbJMJmCA7zDqH2MmckPqz53tJD8XNBJo5MwfCnX1a7Q72r0IrymbEc7_kwnTHWoK6rQfdwYAKcVn8zmtN4Tat5-A3g8Gu38jrq5EwsxldaZL3IK4QqytJ4cZpMu7k7m263uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6d94ea47e.mp4?token=Cy3vGvFwOel71bs0Lu6yQSnGz-tErV1uej_GXqgA6RIUV6zjmGPl3grt9qCZcePDtYRF4LBxgJCW4eLCDXCbN3AjQ9ribtvCkC0o62tYEzQt2syjuYRVwTUX31x-Umw8-Ue261ALzNI7jNnUXp9kajesjQiOU5q--tot4YY8DjTiFV2ubjIWwXALgq_7AAWZkTD59XTQBC2hMIzy1-t6vK1i63goyX_2xmg6s2YEf5MTpkSSPH2S2LeH-7g8vltwAaSZYG6kR9v_zW2vQP7aGOqc68wkYH41EDPVJ1d_gXMSoUkakeNwWRZ9T9nIphNF3XmxZ74yOBEqN_tCtECa2zCy0e2MZMpaKIu9GbImsR78QUF5vJjQpyt-OTdNZ34l6U2cX84QyQoC7ddghiQOL4zqEu4IBpuk16dKwZhAPkOw-cM3l4IStXZ3mMVMc-x6bS5BMznM2E9Dt953rwQm1kW9ZpSCOAU7aO5ZUNzCbUJMVMj6wArTqqeRISESdbOLhKjNLinXY9qtLVq_wghm20bv06G-T2jiJnAprYsRbJMJmCA7zDqH2MmckPqz53tJD8XNBJo5MwfCnX1a7Q72r0IrymbEc7_kwnTHWoK6rQfdwYAKcVn8zmtN4Tat5-A3g8Gu38jrq5EwsxldaZL3IK4QqytJ4cZpMu7k7m263uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود زائران به مصلای تهران
🔹
دل‌ها‌ بی‌تاب و چشم‌ها گریان از فراق رهبر شهیدی که تا ساعاتی دیگر به جایگاه آخرین وداع در سحرگاه شنبه می‌آیند.
@Farsna</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/446537" target="_blank">📅 04:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446536">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f8c363281.mp4?token=HywHtQOBQdGFlS640Ve4LO7HnJBfnHSbaX10LmcT_ZT_4qNWX1U23laOxZ9upJqwa3NeR7UwPJQx9NeOc6vzmrsWmdb_pke7ogPhG54zkqOX3MYQaG90Te9TUvkZjRJJtNhxWbVi3s5ETu8b5wMDa-AASxscxK5kJa27BGvVu1GQnUg58qO1KKRgX4RhrGPm6Dc-csDtxcf2jMytYHADrDuaWx7EUO8bbxwosRnkzrCtIt77eW_a7LIbNTs2R5KzIAIpvKuU6gvSW4d39pZuDyvZkZPq3a3LwXfAB9tqZLe06jn0jeu7clVN0VrRMtr_40rDXwOrQ05GEkWPP0osBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f8c363281.mp4?token=HywHtQOBQdGFlS640Ve4LO7HnJBfnHSbaX10LmcT_ZT_4qNWX1U23laOxZ9upJqwa3NeR7UwPJQx9NeOc6vzmrsWmdb_pke7ogPhG54zkqOX3MYQaG90Te9TUvkZjRJJtNhxWbVi3s5ETu8b5wMDa-AASxscxK5kJa27BGvVu1GQnUg58qO1KKRgX4RhrGPm6Dc-csDtxcf2jMytYHADrDuaWx7EUO8bbxwosRnkzrCtIt77eW_a7LIbNTs2R5KzIAIpvKuU6gvSW4d39pZuDyvZkZPq3a3LwXfAB9tqZLe06jn0jeu7clVN0VrRMtr_40rDXwOrQ05GEkWPP0osBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سنج و دمام‌زنی زائران در مراسم وداع با پیکر رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farsna/446536" target="_blank">📅 04:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446535">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b870b3546.mp4?token=skprluC82P2OzfjYrwqEaJq12T9hiPCTmZKfByUga-kkVyKNwTj9nYUp2nvDcfDkSMK_vd7Bpf8G4aVqv4nGrvbQEfiVBTCZS2UzoQWtvdLzQcxIw9Q1DuqWnNhY3Sjbc30AytyBqbkHC98Wu6JHkZ38RGqhivr0w7_8UR3gcT5hTipjKZfJsmuokK1CC0iauxz4VvNsmpkkk2z8BF5QsCto4oO_F_WoI3fxUCZRgYAkv9jDMWieA1tKSupX2_PZ-Xcmx0fwLPufjqZAETLfU7qEfKGWhNk27dlJMVARjpoKaA-3ocSmGDVcLE3rLhBFUTZ2AmwU1mQQ8ekUFZ7Snw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b870b3546.mp4?token=skprluC82P2OzfjYrwqEaJq12T9hiPCTmZKfByUga-kkVyKNwTj9nYUp2nvDcfDkSMK_vd7Bpf8G4aVqv4nGrvbQEfiVBTCZS2UzoQWtvdLzQcxIw9Q1DuqWnNhY3Sjbc30AytyBqbkHC98Wu6JHkZ38RGqhivr0w7_8UR3gcT5hTipjKZfJsmuokK1CC0iauxz4VvNsmpkkk2z8BF5QsCto4oO_F_WoI3fxUCZRgYAkv9jDMWieA1tKSupX2_PZ-Xcmx0fwLPufjqZAETLfU7qEfKGWhNk27dlJMVARjpoKaA-3ocSmGDVcLE3rLhBFUTZ2AmwU1mQQ8ekUFZ7Snw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مصلی با ورود خیل عاشقان رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/446535" target="_blank">📅 04:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446534">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
ورودی‌های ۶ و ۸ مصلای تهران در سمت شرقی به‌روی زائران باز شد @Farsna</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/446534" target="_blank">📅 04:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446533">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7833e3d388.mp4?token=AZWDPkTGL3YxCxc6Ktf0a5qO6FivJO80SfaI76F_M_pspInsdSLuD0xLolxm197PHuk45v9-hgbqdD4wY6WGGnhe8i7cxKJPQTn8MnJmF8I3dqU3V3YW6oObIhP_LE8W4Wum8kaY8aRwEUNZ_BLZ5oOV3bmjPEMXKoY-mYtdNwX-lA-unJeXCI8p55WUohAdAYEoqv84tuixwY2VmfNKa3wgChDojTCazK1VCZcGHnjIlXPsoaN8uVafSP402xD5Xw620Gzxb8pLeBRFI5Eso_wzEnS8rGiFkegM98nKWghw0uJAxP-IjgmtEcz8nZg4IvLpvdX6_BiYkULvj-S2YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7833e3d388.mp4?token=AZWDPkTGL3YxCxc6Ktf0a5qO6FivJO80SfaI76F_M_pspInsdSLuD0xLolxm197PHuk45v9-hgbqdD4wY6WGGnhe8i7cxKJPQTn8MnJmF8I3dqU3V3YW6oObIhP_LE8W4Wum8kaY8aRwEUNZ_BLZ5oOV3bmjPEMXKoY-mYtdNwX-lA-unJeXCI8p55WUohAdAYEoqv84tuixwY2VmfNKa3wgChDojTCazK1VCZcGHnjIlXPsoaN8uVafSP402xD5Xw620Gzxb8pLeBRFI5Eso_wzEnS8rGiFkegM98nKWghw0uJAxP-IjgmtEcz8nZg4IvLpvdX6_BiYkULvj-S2YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوای دعای عهد در مصلی امام خمینی(ره) تهران
@Farsna</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/446533" target="_blank">📅 04:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446532">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c78bc76f0c.mp4?token=YKpOLWnLshjAroJikDGrHaOiVg876BG0Ztqfy84RfLN0jo69NisBeNsSQRRbqP39SCs4OcXROyc-BWnLSFmMwu5YPEOyoy4z0M2J5BNMwntvem0lGipJY7EmZzq8xWch3iCikWvvVH7teU__YzZ5I9wwNwFLqubk2cYej7xIPW1NlRPBie4VpcCMCqcvm6tqaHkID7Uskb6WG3mvIM4nC5ufwouwIXpX9vhCjqCCqzyKA_TKpkETfeG4oZvoEY82-OvaFjEEfRrcCtrBuryY8Rk0N2Albs2zE1GsEZH8oJZGuMpio5mbcqEhbB7TBFzb8Xse_NJo0Atst5rQCqVMDaXkgoRQbA9-aPBB-wPNmI5jtg6Fyq2KdXuAurwA_htw50GDlmzeBPObff0Fp8gFqWcB2qUMywFJQLpc9VXsQx3Cj1lwxrPxQ4ryPj3147ONpNxv4dFjF0XOh60RazUkzdfMMnoGHMb5yfGrY6G__dAMC6RVKWJRKlDyaZFniT4ZyDta1f4NAhXd7k9NLXh9vkbPzlmieVQ2wz1zq9-nbLYFqFV3TAc1lnI6d_HSJyhSkSROV1S38pG47hXEUSEaL0Mc_T6SI14EPB_TVQ6vLoWbZyD_mcayfm6JA4ON8_jvJoDt7qNBNSex5VY6CinobO2fWkj66CL2Qikf-jXqmqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c78bc76f0c.mp4?token=YKpOLWnLshjAroJikDGrHaOiVg876BG0Ztqfy84RfLN0jo69NisBeNsSQRRbqP39SCs4OcXROyc-BWnLSFmMwu5YPEOyoy4z0M2J5BNMwntvem0lGipJY7EmZzq8xWch3iCikWvvVH7teU__YzZ5I9wwNwFLqubk2cYej7xIPW1NlRPBie4VpcCMCqcvm6tqaHkID7Uskb6WG3mvIM4nC5ufwouwIXpX9vhCjqCCqzyKA_TKpkETfeG4oZvoEY82-OvaFjEEfRrcCtrBuryY8Rk0N2Albs2zE1GsEZH8oJZGuMpio5mbcqEhbB7TBFzb8Xse_NJo0Atst5rQCqVMDaXkgoRQbA9-aPBB-wPNmI5jtg6Fyq2KdXuAurwA_htw50GDlmzeBPObff0Fp8gFqWcB2qUMywFJQLpc9VXsQx3Cj1lwxrPxQ4ryPj3147ONpNxv4dFjF0XOh60RazUkzdfMMnoGHMb5yfGrY6G__dAMC6RVKWJRKlDyaZFniT4ZyDta1f4NAhXd7k9NLXh9vkbPzlmieVQ2wz1zq9-nbLYFqFV3TAc1lnI6d_HSJyhSkSROV1S38pG47hXEUSEaL0Mc_T6SI14EPB_TVQ6vLoWbZyD_mcayfm6JA4ON8_jvJoDt7qNBNSex5VY6CinobO2fWkj66CL2Qikf-jXqmqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ورودی‌های ۶ و ۸ مصلای تهران در سمت شرقی به‌روی زائران باز شد @Farsna</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/446532" target="_blank">📅 04:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446531">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93cc5c358c.mp4?token=vnmid6sS00lxB9yoP_iigdL35zlUBfTZFMgkplzBNc-4wGjzyyxcNsCzJH9huISRQC2nYNRmOgh_2moD6ATm-MwNQU5FNviDrSr1MNnN7XSZI66fYL68hSgj59qe-mYYCdN-h8yq5ctudXO9LyKp4tR6-fnfCGc-38aFoKF_NPhZf5uKpjBShYTEPJ2q5KD29b3816v4eoappDDSF66VLNaFzFaWpYxQiJ4d-0yzkGB_aw3vOmtGQEZupl_MGiYltPXkP18bXc6jo0RYE5gE0uZ-IC7If-OJ45rVGUP1B1GLXpOpWJmKoU_DyynFBflzrq8Yy1KxL_2HZVDCH9U-BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93cc5c358c.mp4?token=vnmid6sS00lxB9yoP_iigdL35zlUBfTZFMgkplzBNc-4wGjzyyxcNsCzJH9huISRQC2nYNRmOgh_2moD6ATm-MwNQU5FNviDrSr1MNnN7XSZI66fYL68hSgj59qe-mYYCdN-h8yq5ctudXO9LyKp4tR6-fnfCGc-38aFoKF_NPhZf5uKpjBShYTEPJ2q5KD29b3816v4eoappDDSF66VLNaFzFaWpYxQiJ4d-0yzkGB_aw3vOmtGQEZupl_MGiYltPXkP18bXc6jo0RYE5gE0uZ-IC7If-OJ45rVGUP1B1GLXpOpWJmKoU_DyynFBflzrq8Yy1KxL_2HZVDCH9U-BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برای اولین‌بار و آخرین‌بار آمدیم دیدار؛ آمدیم تا حسرت دیدار به دلمان نماند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/446531" target="_blank">📅 04:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446530">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91ed610c9b.mp4?token=FvFEssudv6eBv0Yopg61v1tntH_680FgO7T_lVU7HWB5Roy0rbPSkISsnCS6qfms_JMwwFKS_HlSXGTPjJ6pm6S2GwA5bvU8UQ2U2xeVuSyfpF_pcQd6rvfzr4YrQG0dPyA6D5V38thh5SjQplyGnIwHOnAhH7WSYze1wBSPYD9buVQ-P9OFi1O6f-dtgBV40riQkO1czCQwnMcbwbhC9PiZjcncYeLZYGhv8DB2opzhnNifVMXR_jP5lrGpTFC4q_lB2dBhSacEb6eyyXR6GbYBoxDAidMzr25Uuw-VtvgZgXfhE38JDbpx9UklYSaNVKAw24HNVQ2IPEKa72itvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91ed610c9b.mp4?token=FvFEssudv6eBv0Yopg61v1tntH_680FgO7T_lVU7HWB5Roy0rbPSkISsnCS6qfms_JMwwFKS_HlSXGTPjJ6pm6S2GwA5bvU8UQ2U2xeVuSyfpF_pcQd6rvfzr4YrQG0dPyA6D5V38thh5SjQplyGnIwHOnAhH7WSYze1wBSPYD9buVQ-P9OFi1O6f-dtgBV40riQkO1czCQwnMcbwbhC9PiZjcncYeLZYGhv8DB2opzhnNifVMXR_jP5lrGpTFC4q_lB2dBhSacEb6eyyXR6GbYBoxDAidMzr25Uuw-VtvgZgXfhE38JDbpx9UklYSaNVKAw24HNVQ2IPEKa72itvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زیارت عاشورای آخرین دیدار با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/446530" target="_blank">📅 03:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446529">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de68dbe7b.mp4?token=of5DiwHLY_ASqsPHMmV02KKEgxfzjAoL4sxavd2OPKgJqbn_hj9PDK9WmofaMOKXmp_4hS2gvUyzTytuzlM6BUzX5o5_JY_T3UBxoSBZl46to64XOKDe8jkKf-d6hwDd6WFu5WrPw862rxyiuhwjfL69pWbuOzDbjsN4Sma0OMK1mRBgbLlzbgRsdReWI_ryOncGUon1QBFKJdljJOeKw8oiGiF-Z31nAnBhwv98msNoUwVwKn9ihcVWRC3wbmT2EEBaZAcEL_62YCeBQ0mn9YB5FjKjMKrE6tndjqnvKE7D3hN49ojKv3VxvX6_2c8BmE8-Z5JCay1EOJU6nC4fng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de68dbe7b.mp4?token=of5DiwHLY_ASqsPHMmV02KKEgxfzjAoL4sxavd2OPKgJqbn_hj9PDK9WmofaMOKXmp_4hS2gvUyzTytuzlM6BUzX5o5_JY_T3UBxoSBZl46to64XOKDe8jkKf-d6hwDd6WFu5WrPw862rxyiuhwjfL69pWbuOzDbjsN4Sma0OMK1mRBgbLlzbgRsdReWI_ryOncGUon1QBFKJdljJOeKw8oiGiF-Z31nAnBhwv98msNoUwVwKn9ihcVWRC3wbmT2EEBaZAcEL_62YCeBQ0mn9YB5FjKjMKrE6tndjqnvKE7D3hN49ojKv3VxvX6_2c8BmE8-Z5JCay1EOJU6nC4fng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای سحرگاهی مصلی امام خمینی(ره) تهران
@Farsna</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/446529" target="_blank">📅 03:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446527">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f926fd7cb3.mp4?token=rmbOkNiHgwKi3vNHf7FgRXJTcGzXA4xMO7_sn9JI0FE-Bn8watkKc9kKrbCQb0BUCuwbECKqUsFUsCDmauIXOLIz-pb9MiOVReqhJuIoP4P4wCnxN6V2UzB1GZthvyXHY1pmo1XfUDFWmiq5_w_AulO20VxhRq0Q4q5gWic6-H1q6NJAYGoNI9kIOyZ-Jn7IdHiFsN7wrHhUirDO6qmdQBiFD1rv308wQqNUEvdogzLmiFdh9437cU9oVwXYySbrpFAwXmDfAvIfpmlYRtHPdwdWixAAWYMDxvK_hVwrqHMcXURoYpl29d4N981nI4kYqhYUhQPwo6dx0cXsrUqAmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f926fd7cb3.mp4?token=rmbOkNiHgwKi3vNHf7FgRXJTcGzXA4xMO7_sn9JI0FE-Bn8watkKc9kKrbCQb0BUCuwbECKqUsFUsCDmauIXOLIz-pb9MiOVReqhJuIoP4P4wCnxN6V2UzB1GZthvyXHY1pmo1XfUDFWmiq5_w_AulO20VxhRq0Q4q5gWic6-H1q6NJAYGoNI9kIOyZ-Jn7IdHiFsN7wrHhUirDO6qmdQBiFD1rv308wQqNUEvdogzLmiFdh9437cU9oVwXYySbrpFAwXmDfAvIfpmlYRtHPdwdWixAAWYMDxvK_hVwrqHMcXURoYpl29d4N981nI4kYqhYUhQPwo6dx0cXsrUqAmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ورودی‌های ۶ و ۸ مصلای تهران در سمت شرقی به‌روی زائران باز شد
@Farsna</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/446527" target="_blank">📅 03:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446526">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c86a42811f.mp4?token=vF8RN5Yg6aN58Rr8b2pbDwwpj0hzT7yFmhd-2Motp2dtsDBd67EekIHxalVWsS_E0DcKLwLYuRchYtFlpLAtkRtdNkn7yFps2ZR-9nxk5BLE9z-UJBe_fjiyYuZKnt1Iyk6h2I9B3K2-6gnI9XUBRU-fZnlamGRTBRi9SVaHyyFNKf0-pQjG1Vs96Um1CyjHX6A8zLtb1fhpILOEBYlW6TCG2axLZOXy7keYw7IL7QCOEmgx7jKF8lc7yPfG6SA4BDDoydb3ZBxg8r0IwDpW7oFtHq4bTSK2gJasoF4Ctu9-HWK-BLmWn_Stn2AG-4eaXcuSFFiRJtvE6y8nKmhgqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c86a42811f.mp4?token=vF8RN5Yg6aN58Rr8b2pbDwwpj0hzT7yFmhd-2Motp2dtsDBd67EekIHxalVWsS_E0DcKLwLYuRchYtFlpLAtkRtdNkn7yFps2ZR-9nxk5BLE9z-UJBe_fjiyYuZKnt1Iyk6h2I9B3K2-6gnI9XUBRU-fZnlamGRTBRi9SVaHyyFNKf0-pQjG1Vs96Um1CyjHX6A8zLtb1fhpILOEBYlW6TCG2axLZOXy7keYw7IL7QCOEmgx7jKF8lc7yPfG6SA4BDDoydb3ZBxg8r0IwDpW7oFtHq4bTSK2gJasoF4Ctu9-HWK-BLmWn_Stn2AG-4eaXcuSFFiRJtvE6y8nKmhgqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اذان صبح به افق مصلای امام خمینی(ره)  @Farsna</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/446526" target="_blank">📅 03:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446525">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1Pw5Ea_aAlu8pzJrLcqYWo4Tl9eiHIb2_HScoX2Zlkq_PiYg2hObktwWi_fSyrlmH_G0pQrui5HXoxXuXej1ABj7p_OF6tVJ7NejOGVichZe6mERRISi4SCk2wxc7UQx4-zpVpq-LuoPLD2YENXf1WCw80o5bJpYRbuZg-vkGxzVsBdqZT2MwyZdfkP7aucvgMFdiVJr4JpO-JcCc6Ee1arupepVDcmlPDDeFLr-QtN_b00fHLmktfaI-wVMbU1Iegd-HNJvOjvlYZtV-usFBWsaNX2lwjvTf9Ts9QaykRBJVqNwoSj4jpRXp9pAz3fofPLhVuSg4FOsXWXq1Rz-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
آماده‌سازی محل قرارگرفتن پیکر آقای شهید در مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/446525" target="_blank">📅 03:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446524">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2baa9424d9.mp4?token=WFYZBftXIe6K8W9-zQrp418MVdPVxNw0uUb1iuOpnbFHoko44iCxuBI5tassMXyPNMepUOCCnVq5EHTCI9brsfllw-CR08GcBVTLRnd62NkUumVMweolU8Lt31rOj6zRFXyQfoZvWeSMOSU1ugQ9YXDiF-jtr9A01CC7ee9wq8B-bx3d-uYddteentYN2lyZ-C0Kxyr4UijlgFRr2PKLgzbD3qvZ0TXRsFiWkGvbNRpOZF8wknEmD0n6jWk5WZMY21wgLm7FjlOI1FZWLFNyM4BLFUZP004eMMNHSzNyzBhePSjqE6HOxQwt6o0Iess2pHZ-Xsr_jZxjmHaGaAxYGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2baa9424d9.mp4?token=WFYZBftXIe6K8W9-zQrp418MVdPVxNw0uUb1iuOpnbFHoko44iCxuBI5tassMXyPNMepUOCCnVq5EHTCI9brsfllw-CR08GcBVTLRnd62NkUumVMweolU8Lt31rOj6zRFXyQfoZvWeSMOSU1ugQ9YXDiF-jtr9A01CC7ee9wq8B-bx3d-uYddteentYN2lyZ-C0Kxyr4UijlgFRr2PKLgzbD3qvZ0TXRsFiWkGvbNRpOZF8wknEmD0n6jWk5WZMY21wgLm7FjlOI1FZWLFNyM4BLFUZP004eMMNHSzNyzBhePSjqE6HOxQwt6o0Iess2pHZ-Xsr_jZxjmHaGaAxYGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روضه‌خوانی نریمان پناهی در حیاط مصلای تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/farsna/446524" target="_blank">📅 03:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446523">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/939fdd058e.mp4?token=POVcXhJZc18jBeIcpbx_g4M6PBIhcAXiuxuQ4CHDDG6wEO5S9BCatFlu-cYRcl_Plke8RuL8OQETblGKCVTgr7zShsrf6vt9HlYIvQecV9-opCUeyIi7y_x5K697dJ-Xs22qagd9HRbI-FRpW_DU9SUD7YPpTLJ2ZZo9vLaT_87p40MnI86qkuTK0Ed3zqR_Ghx0TiOnXflVGiZ5OqNPv1wRXAOHaSmy169UQGgOX1L0w7wI6kMyXWCo9j6yR12-o9w2TmwEPmOwKUKVBz0797jTvYF2EhW5CKbc1Adea1sd0IhuCTEEXgEMfN6RvEUVpXAS1B70FNBXv7KVU4WGrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/939fdd058e.mp4?token=POVcXhJZc18jBeIcpbx_g4M6PBIhcAXiuxuQ4CHDDG6wEO5S9BCatFlu-cYRcl_Plke8RuL8OQETblGKCVTgr7zShsrf6vt9HlYIvQecV9-opCUeyIi7y_x5K697dJ-Xs22qagd9HRbI-FRpW_DU9SUD7YPpTLJ2ZZo9vLaT_87p40MnI86qkuTK0Ed3zqR_Ghx0TiOnXflVGiZ5OqNPv1wRXAOHaSmy169UQGgOX1L0w7wI6kMyXWCo9j6yR12-o9w2TmwEPmOwKUKVBz0797jTvYF2EhW5CKbc1Adea1sd0IhuCTEEXgEMfN6RvEUVpXAS1B70FNBXv7KVU4WGrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جایگاهی که اشک همه را در میاورد...
@Farsna</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/446523" target="_blank">📅 03:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446522">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de0fa71ef6.mp4?token=OBfWNfUvt4Lk4cvEk_LvqSKcT9G_Pl-Ts42y_BY9oHY5IaQFFA6bVOq2qW4oEIFbmfY3vfQyMwJG2HrKWHJXSlGKc5cIzCCT18IkN8jPgMDvIZFrXTvKiefAr-pJ5UwSnNT5oVyHnpCMcxHP7xjx_sdrikaSYsoTX8DREAdehvYBoebk1vwGgJsyhPXQh2Z3ldDLuk5qZVqWcDDWA5_UxWqwNWhQjUqWhk7P-IUOL-Z5fdIKgIz47hNKeo4OTV4YaOEPRBOnjWM1-fRp5leTDVgyFTP2zSxfJePd_iHgsptjFCwsSOl0TMC-tLOnW1ErL_xIC6xjidMSEPd3_clPLJw89L6LhpjEW--Wwc2FwmAZHiSQH4qDf22ItQ6NX_H1DnxUVUbar1Oy7GsecYvTPpxqPSbq9ITTFNnAqVdbivM5p3jjMofFw7TLLYi6WqN5kSEVPcmQ4K7RcgtzjQVYXa2wKUTtezJrhHotJJqMNSYYd9Ox1ULmeSiF6xvkrxZzj0G2OCn4S7q9DcFA0T0slytH8Ly_S3ZmUeSrxvlKjruj-eALWe6u9COiwwZQ6mQzW0t4GDpix_iFDHCqX8pn8KTLu6oj8ZdfWNkAFxIWlOZK4geJXAWVfpLSzOCgZ7XlsYv0VK3l7yEY-K1nKYyJaIamNc2OrYi4kMpM-yQExHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de0fa71ef6.mp4?token=OBfWNfUvt4Lk4cvEk_LvqSKcT9G_Pl-Ts42y_BY9oHY5IaQFFA6bVOq2qW4oEIFbmfY3vfQyMwJG2HrKWHJXSlGKc5cIzCCT18IkN8jPgMDvIZFrXTvKiefAr-pJ5UwSnNT5oVyHnpCMcxHP7xjx_sdrikaSYsoTX8DREAdehvYBoebk1vwGgJsyhPXQh2Z3ldDLuk5qZVqWcDDWA5_UxWqwNWhQjUqWhk7P-IUOL-Z5fdIKgIz47hNKeo4OTV4YaOEPRBOnjWM1-fRp5leTDVgyFTP2zSxfJePd_iHgsptjFCwsSOl0TMC-tLOnW1ErL_xIC6xjidMSEPd3_clPLJw89L6LhpjEW--Wwc2FwmAZHiSQH4qDf22ItQ6NX_H1DnxUVUbar1Oy7GsecYvTPpxqPSbq9ITTFNnAqVdbivM5p3jjMofFw7TLLYi6WqN5kSEVPcmQ4K7RcgtzjQVYXa2wKUTtezJrhHotJJqMNSYYd9Ox1ULmeSiF6xvkrxZzj0G2OCn4S7q9DcFA0T0slytH8Ly_S3ZmUeSrxvlKjruj-eALWe6u9COiwwZQ6mQzW0t4GDpix_iFDHCqX8pn8KTLu6oj8ZdfWNkAFxIWlOZK4geJXAWVfpLSzOCgZ7XlsYv0VK3l7yEY-K1nKYyJaIamNc2OrYi4kMpM-yQExHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اذان صبح به افق مصلای امام خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/446522" target="_blank">📅 03:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446521">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb0e215210.mp4?token=V8jwnSU0sdIF1DjtBeT1a6D41yJYKZo1wqnNEM1ZjGZ9FqyZHy4QkQBO_R_b-t3ahyyLEisCq72OaWNEALOUQX9ctJ1H2bXTJSjK1Kx6sOk5JY-9xnqiGbeoFC3sc_KGTRTjahxCg-j4PfKlCXf4eD93vEYmo1aeo7DJ2OgM5ZaOx4_MZCyAJNktM0YGix1HtheBXCoag2ukQygR70kW_zLicnX8llT1Lp5eJATNlZulw3cgMRCLvtV20eeHP5uFfqGJpquW0bWSWa13Gx86OypYl0dmF7b2z4s9iKb8BM79YFzuLcShMDiXEvHDnMRV08goKHWDRZ8M91rneC0R6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb0e215210.mp4?token=V8jwnSU0sdIF1DjtBeT1a6D41yJYKZo1wqnNEM1ZjGZ9FqyZHy4QkQBO_R_b-t3ahyyLEisCq72OaWNEALOUQX9ctJ1H2bXTJSjK1Kx6sOk5JY-9xnqiGbeoFC3sc_KGTRTjahxCg-j4PfKlCXf4eD93vEYmo1aeo7DJ2OgM5ZaOx4_MZCyAJNktM0YGix1HtheBXCoag2ukQygR70kW_zLicnX8llT1Lp5eJATNlZulw3cgMRCLvtV20eeHP5uFfqGJpquW0bWSWa13Gx86OypYl0dmF7b2z4s9iKb8BM79YFzuLcShMDiXEvHDnMRV08goKHWDRZ8M91rneC0R6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین ساعات انتظار این شکلی است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/446521" target="_blank">📅 03:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446519">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🎥
«عشق دل‌افروز» پرواز همای، برای رهبر شهید
🔹
نماهنگ «عشق دل‌افروز» ساعاتی مانده به آغاز برگزاری مراسم وداع با رهبر شهید ایران، با صدای پرواز همای و شعری از قائد شهید امت منتشر شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/446519" target="_blank">📅 03:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446518">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75bd38c9b2.mp4?token=dTU3jO_38SZBY5TIgdI5hoUGAtxMkAAML0LxIC0BbTm4jkuzzcLns1tNbncfUsyA9XycW_clWMDjQpo-h-CplkzjhkHhjjh9eWx7NgXrpTIekj2BLga6BavIWMSuTLV-YlEWRH5zn7wC0fJkQ5-U63BOjsXRb2R-kEvIBfCrTKAArXO2YjYAA4psBf1ou-CtwSMungSVI7KQVTIsFsrhPYP6tVD99KJ7SGYgRAdhhZcRxjZJUJUzm-KTc67zAbo7NJmfKhDuwCZ9to4KaFOWP4glOmlOCWMf0M1-DzU7sZq5OTnYLgGn9lbf0iVk9lVWnOVneT2bLAfF_vPdlBz2kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75bd38c9b2.mp4?token=dTU3jO_38SZBY5TIgdI5hoUGAtxMkAAML0LxIC0BbTm4jkuzzcLns1tNbncfUsyA9XycW_clWMDjQpo-h-CplkzjhkHhjjh9eWx7NgXrpTIekj2BLga6BavIWMSuTLV-YlEWRH5zn7wC0fJkQ5-U63BOjsXRb2R-kEvIBfCrTKAArXO2YjYAA4psBf1ou-CtwSMungSVI7KQVTIsFsrhPYP6tVD99KJ7SGYgRAdhhZcRxjZJUJUzm-KTc67zAbo7NJmfKhDuwCZ9to4KaFOWP4glOmlOCWMf0M1-DzU7sZq5OTnYLgGn9lbf0iVk9lVWnOVneT2bLAfF_vPdlBz2kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اندک اندک جمع مستان می‌رسد...
@Farsna</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/446518" target="_blank">📅 02:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446517">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ecc44ada.mp4?token=In8bc5u96037rF-wC-In98OAYFUx8D_YfkCUVomP1d7zBdq_oScX6SVC25JyHqH9rD29140psJsCZQph_wfely3zoaXDIgXwmIEHOzbXGCzV9E-Mv1Rne933kNf59jeh7mjeU8z-leBvE6W-wke3bQfsj6wEhWbMGN_pnrWANwalBfdbWJsAVURUto6sJurzO5qqBZ2EZdkYQDwbszSr_Ouywtv68QPjF4j4srFPJwiIphJkf3NmxtJynLZR_bwMIRxgCGgFHBykzRoeIHIHPNacF5a678vMdTjmHADpmeKx3KBNpZaDNmHisFmrEObmrAJ46gfbFZb5BROqQiQeKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ecc44ada.mp4?token=In8bc5u96037rF-wC-In98OAYFUx8D_YfkCUVomP1d7zBdq_oScX6SVC25JyHqH9rD29140psJsCZQph_wfely3zoaXDIgXwmIEHOzbXGCzV9E-Mv1Rne933kNf59jeh7mjeU8z-leBvE6W-wke3bQfsj6wEhWbMGN_pnrWANwalBfdbWJsAVURUto6sJurzO5qqBZ2EZdkYQDwbszSr_Ouywtv68QPjF4j4srFPJwiIphJkf3NmxtJynLZR_bwMIRxgCGgFHBykzRoeIHIHPNacF5a678vMdTjmHADpmeKx3KBNpZaDNmHisFmrEObmrAJ46gfbFZb5BROqQiQeKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چشم‌انتظاری مردم پشت درهای مصلای تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/446517" target="_blank">📅 02:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446516">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae50a122db.mp4?token=VSbfuB_0Nwfl_4WT3LU-n96daIWxmQJ2numSpCPk5N4whd5o8GfAnVOmGT1cYkTRld_OuCXKQiltV2WnausLRRTGyY_EsnOIrRxawvIEI6uSafcqomn6zm1-4sASAQK95GUf58kMWvYNYv3ReAFGcNG8brzZXRPtNHbfAaDqMOl4xOKAS9fongEgVohESNESMrh786albUbTuXYX01-0e8v_wh6TyR4H5JcsdyvEzXVi3hM9SrqezDB7LZC8nWAvw8gdeC5bjgauoJAxGbnotSTx63JTLffCdOpn6mvYZjZedmD_W2w7LTOcEFJqwWKd04AitBSFyE71oneKhOGxQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae50a122db.mp4?token=VSbfuB_0Nwfl_4WT3LU-n96daIWxmQJ2numSpCPk5N4whd5o8GfAnVOmGT1cYkTRld_OuCXKQiltV2WnausLRRTGyY_EsnOIrRxawvIEI6uSafcqomn6zm1-4sASAQK95GUf58kMWvYNYv3ReAFGcNG8brzZXRPtNHbfAaDqMOl4xOKAS9fongEgVohESNESMrh786albUbTuXYX01-0e8v_wh6TyR4H5JcsdyvEzXVi3hM9SrqezDB7LZC8nWAvw8gdeC5bjgauoJAxGbnotSTx63JTLffCdOpn6mvYZjZedmD_W2w7LTOcEFJqwWKd04AitBSFyE71oneKhOGxQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روضه‌خوانی عبدالرضا هلالی درکنار پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/446516" target="_blank">📅 02:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446515">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ed90b67f.mp4?token=WH1q2woTP_ypdy2qz_8uQP_ALce8xqm9JHUdwIJZ5ndBRnhEldu8jMZDVyMzGVugjZx4gVjcSTvfKyznG472GeoOchz0OgCFZan0rCyXoAKbZt9VOC4Tp5wTc3aXXznEXwC4dxdW8aNWpFHkuM3G-Yqq95bA8Yu65qxviBS2zqlG0x-DVQ1pe7w2TmrAnrmUGgWW1y-20S7vnt-CSaDTNlPve5bosJ9tzBG7Y-abJBMfKErw9FHafVpf88ph-fBO8OsiNEJ-aSAA6NepVxdlfMQy_Ae-OmqCiHu8g3V7RDZHwuIbx9e0dLGcxOKx_Rrg4IwuB5wypc_XBfdtKWWmAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ed90b67f.mp4?token=WH1q2woTP_ypdy2qz_8uQP_ALce8xqm9JHUdwIJZ5ndBRnhEldu8jMZDVyMzGVugjZx4gVjcSTvfKyznG472GeoOchz0OgCFZan0rCyXoAKbZt9VOC4Tp5wTc3aXXznEXwC4dxdW8aNWpFHkuM3G-Yqq95bA8Yu65qxviBS2zqlG0x-DVQ1pe7w2TmrAnrmUGgWW1y-20S7vnt-CSaDTNlPve5bosJ9tzBG7Y-abJBMfKErw9FHafVpf88ph-fBO8OsiNEJ-aSAA6NepVxdlfMQy_Ae-OmqCiHu8g3V7RDZHwuIbx9e0dLGcxOKx_Rrg4IwuB5wypc_XBfdtKWWmAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بی‌تاب آخرین دیدار
◾️
بغض و حسرت مردم در مصلای تهران، ساعاتی پیش از آغاز آیین وداع با آقای شهید
@Farsna</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/446515" target="_blank">📅 02:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446514">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🎥
۱۴۰۰ خودرو‌ی آتش‌نشانی در خدمت زوار امام شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/446514" target="_blank">📅 02:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446513">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
ادامۀ حملات اسرائیل به غزه
🔹
منابع خبری از حملات هوایی و توپخانه‌ای ارتش رژیم صهیونیستی به مناطقی در شرق و جنوب غزه خبر می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/446513" target="_blank">📅 02:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446512">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f977b04afe.mp4?token=WyPppCtEhwANaV7rcCLs5WSdZ94wYrNvFz2aoBlojWkkhJGRu1ZsaGnVNSY_2aCzwyFl1UR4OuHSM9bKA3y1UAUh0kD5SwKmrlBK3oVIlwNjndmYF5vHoSt41BNxfOzLg34afwS1BqnjSnPTBAcIDPU6v8fpOWCzQZJMjwXwtIvmA28LohMku4xhEBtKOjXYEK-4LT93S2BwsbRZIw-iAHUbyXrLjPgPWnzu1lAbSN8floG6QdX4jzsJOH84Bi-kTzdgaYMr7X2QB5daRRTNgnIFSdJua73Hf_4PJ5y7bw-RBdKNkZWzweTYYLL5UwgV0qyFku2uceCHUrpl_Y5_hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f977b04afe.mp4?token=WyPppCtEhwANaV7rcCLs5WSdZ94wYrNvFz2aoBlojWkkhJGRu1ZsaGnVNSY_2aCzwyFl1UR4OuHSM9bKA3y1UAUh0kD5SwKmrlBK3oVIlwNjndmYF5vHoSt41BNxfOzLg34afwS1BqnjSnPTBAcIDPU6v8fpOWCzQZJMjwXwtIvmA28LohMku4xhEBtKOjXYEK-4LT93S2BwsbRZIw-iAHUbyXrLjPgPWnzu1lAbSN8floG6QdX4jzsJOH84Bi-kTzdgaYMr7X2QB5daRRTNgnIFSdJua73Hf_4PJ5y7bw-RBdKNkZWzweTYYLL5UwgV0qyFku2uceCHUrpl_Y5_hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◾️
الا ای بزرگان، بزرگ جهان رفت
◾️
سران را بگو، سرور سروران رفت
🎥
قابی از پیکر مطهر رهبر شهید انقلاب در مصلای تهران، در مراسم ادای احترام نمایندگان کشورهای خارجی
@Farsna</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/446512" target="_blank">📅 02:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446509">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gSQR7L7B5jjrHxYDdhxzqONWMZoVLBiCzO6wy0e5EZ3DyXGioFvCoNJRhAgLVi_TG_wRdsYH59bC1SJMqLIC5mjGcnDWE2c2t44BKBfGIda28Nb3WrWqU1DklUonr5POW8h5gwuA9YHkzhSneIsA_ON8K6LvitP0gzyC3SnIaljyhveg2uqIX21HcBLqTz_Wzz9u8JcOgob14x6L63U3NN58aSVVcQhhPGJIHxH8VPJdsBU_MHf2DVT_RgKbqRzmj9v5tfjNRNsQJbptio0DPauLPTq_FqYf-TU-TC4_NnYStkhcLjgqOPBGaYt2kcDmunWdwfBQ7RiYiKH6PSSgWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GB-EzK5qGSI4hRDCnu4XO8NuFd7tExuQ7sy7wbx489pOMGYWZGilHr6TAPSAxKtFn0Zn8Gw5osoE59JZMkMR779bwJEBkuaawOjrAn3NXVibggbyOx7-XXFDyS3lbCh3u-HUAwf_xl8FyHyuKJF7C-iZ055t-bsRTpgabLhn8QxB2khDWgORYm6veLue1Uk8GnBKyaWO4a_UqWpnbAqdY6OzSuwBHb1URC3hufxSpiC-OHCZ_hb1k5sDSuIfLY6Nr9MU21unwt4U3357M8xhL8FVD9hjkAZNF-QsTqQSJQ4HlU5VYRPWkXsAOpvjc1YguX-ralHnUedtCSWjdg3Q7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KuYzbTXNTxZulWSR7ElPpE_tA1bubyjDrn1a9CAFAhd_YD4uY9Q63FgiUV7AhH1rsPczx_22I76ODJSyyZ2XW6nkwU8w8bQV43LZdpEo8pktnBxwDcaSG70_IGYw829jAcnjWnY1p_Po_bFBlpGHFTG3N4dWCsy30ZFqHvYWgx0aI95d8lBj5N9co7oRJKaEiqFHmBDNeMIDrParuOKsoC5lNxQZTfZ0PO3ux_KEKL9m5ay4zpaoznXYSOkjlhSKC2bLxnF0m556-1UVDpxi-50SHlL_cdYobv5j60h12XK_hlOn7oBP_WpZndzC0v2ti05BufVDXykIyiX2njx0PA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زاگرس‌نشینان با سیاه‌چادر به بدرقۀ رهبر شهید آمدند
🔹
هنوز سیاه‌چادر برافراشته نشده، اما چکش‌ها بی‌وقفه بر میخ‌ها فرود می‌آیند و مردانی از دامنه‌های زاگرس، در گرمای تهران، مشغول ساختن سقفی هستند که قرار است مأمن عزاداران مراسم تشییع رهبر شهید باشد.
🔹
از بچه‌های مسجد و بسیج تا کسانی که روزگاری اینترنشنال‌بین بودند، امروز در یک صف ایستاده‌اند تا به گفته خودشان، وحدت و ولایت‌مداری مردم بختیاری و زاگرس‌نشین را به نمایش بگذارند.
🔗
روایت شنیدنی بختیاری‌ها و حضورشان در تهران برای بدرقۀ رهبر شهید را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/446509" target="_blank">📅 02:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446508">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🎥
سردار معروفی: دشمن نمی‌تواند محاسبه ملت ایران را تغییر دهد
🔹
معاون فرهنگی سپاه: ملت ایران با حضور در آیین‌های وداع، نماز و تشییع، هوشمندانه پای ولایت و ایران اسلامی خواهد ایستاد و به دنیا استمرار انقلاب اسلامی، استمرار ولایت، بیعت با ولایت و یکپارچگی ایران اسلامی را نشان خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/446508" target="_blank">📅 02:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446507">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b7271e4e.mp4?token=HMwdYsOwj_ZAfWAY8Rj535_w9ljHe5xWrGbuK4H9INm8FqmN_FHBirm_GYxQsalSxRyJydGbGqd8AbTEtS0m1UENfAraUrm7t4L9wTlmJMfgmACqrVmdCRAkEqY2-HTMNQDi1o-ij9sydLMhIdY0TAlvSM3h0QsvrRKZt1aaqxoJTHvW58uxGl3cNDgOzG84ao_lZyDSsK9v_fse5tO4wMEOPjMW8lE0NYcKrxg0uyFCJAQ0bh7SM23XG_1DyJlL-eidM3TGppbmZ5UTPb2RwkJvFOkkUmrx3YVYKqIKoBy2-2MRgCvWJ1aJrWuBV9RDbhrN4pQe0zvWSvbv2D1XhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b7271e4e.mp4?token=HMwdYsOwj_ZAfWAY8Rj535_w9ljHe5xWrGbuK4H9INm8FqmN_FHBirm_GYxQsalSxRyJydGbGqd8AbTEtS0m1UENfAraUrm7t4L9wTlmJMfgmACqrVmdCRAkEqY2-HTMNQDi1o-ij9sydLMhIdY0TAlvSM3h0QsvrRKZt1aaqxoJTHvW58uxGl3cNDgOzG84ao_lZyDSsK9v_fse5tO4wMEOPjMW8lE0NYcKrxg0uyFCJAQ0bh7SM23XG_1DyJlL-eidM3TGppbmZ5UTPb2RwkJvFOkkUmrx3YVYKqIKoBy2-2MRgCvWJ1aJrWuBV9RDbhrN4pQe0zvWSvbv2D1XhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مصلای تهران، ساعاتی پیش از آغاز آیین وداع با قائد امت  @Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/446507" target="_blank">📅 02:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446505">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700fb5cced.mp4?token=Ya4d8Z-etqU0_QqAlxsC0mh0gOeP2bwuTtXTKbbcaorClVVNHsbe8VwdG3lvHgjebggLOtxSgX3wh-HtZuJSDHgtUkMa63Tp2IGO3n9AsxwXLa7d2gxPZGt9CkDh5tJCJ0CZCm9P8D-t6_koC5XuLSCVfqwvbyRFBRCwGM5fKEYZ14uJyAEE90zluaZiRf4G3aRTaZuAtDPKDEtEGWG3LVOLtNYCvVPmzTwSLcvMj4DtCtMbBpwgCMpI2xk_3wCb8NWtKsdytUr8Y6-QbzSX5mF71rJyZ48RuptTcFxsEILjqIpzaA0Htv6U-6YKNf5zzJlnVtZG2GKVIlRMYcGe0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700fb5cced.mp4?token=Ya4d8Z-etqU0_QqAlxsC0mh0gOeP2bwuTtXTKbbcaorClVVNHsbe8VwdG3lvHgjebggLOtxSgX3wh-HtZuJSDHgtUkMa63Tp2IGO3n9AsxwXLa7d2gxPZGt9CkDh5tJCJ0CZCm9P8D-t6_koC5XuLSCVfqwvbyRFBRCwGM5fKEYZ14uJyAEE90zluaZiRf4G3aRTaZuAtDPKDEtEGWG3LVOLtNYCvVPmzTwSLcvMj4DtCtMbBpwgCMpI2xk_3wCb8NWtKsdytUr8Y6-QbzSX5mF71rJyZ48RuptTcFxsEILjqIpzaA0Htv6U-6YKNf5zzJlnVtZG2GKVIlRMYcGe0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسی در دقیقۀ ۲۹ دروازۀ حریف را باز کرد
⚽️
آرژانتین ۱ - ۰ کیپ‌ورد
@Farsna</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/446505" target="_blank">📅 02:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446504">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43fb37209.mp4?token=TzlRhDhYuCn26bRqmp0f_NKPicb3R_ifZSY8ySnFLmbuC9I0cNjx-JPwQ5g5crtBnEoQ5GGtEfUrbHD1xMPRk4IP-K8W3ykVTTYuqIty0LICh-A2ZAUcO1ovM9Mscz2i_6vGa-oMVk6FdLowR_oVOESwhGbY-Q86QrHUW9h1KjR14jgHA4fdPC3op4lAF9PkZSnmAHj0SwfTXR0ffDeNP2zD3UOalqSwdLlJqIfLZ3_PRFN_Z5UVOS1lvwgjbs8lZC8lKgg5B6D5Lfdi7VBSdx56gPE5jIJJpO8IwD4PNnTTeVwTpx3YovWWBPDVy7DSh_HdzaDSTkrAz2jYTHXcVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43fb37209.mp4?token=TzlRhDhYuCn26bRqmp0f_NKPicb3R_ifZSY8ySnFLmbuC9I0cNjx-JPwQ5g5crtBnEoQ5GGtEfUrbHD1xMPRk4IP-K8W3ykVTTYuqIty0LICh-A2ZAUcO1ovM9Mscz2i_6vGa-oMVk6FdLowR_oVOESwhGbY-Q86QrHUW9h1KjR14jgHA4fdPC3op4lAF9PkZSnmAHj0SwfTXR0ffDeNP2zD3UOalqSwdLlJqIfLZ3_PRFN_Z5UVOS1lvwgjbs8lZC8lKgg5B6D5Lfdi7VBSdx56gPE5jIJJpO8IwD4PNnTTeVwTpx3YovWWBPDVy7DSh_HdzaDSTkrAz2jYTHXcVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات محدودیت‌های ترافیکی در محدودۀ مصلای تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/446504" target="_blank">📅 01:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446503">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36cefab0f6.mp4?token=HOkCVuNY-f24ILz-V9p00mZhgHRpurWcSC4YJc7cHvu1Y9F2Xige6GCEViLBWtIrlHOsJysABLrjfrl4-GvvNVPWy9c3z92_dfWbTJ7S0-GQrE8kmQBA3Ct8EBdW4vRyeMfPtIhXL55tZzwU6T_RPuHrTq8-uqsuEcATcboRiMwHKxqImbaitHSrZUDfSyRWKMWbQxLufIGueXbGKkZO6NBhJCoRB-OGa_b-rExKZKICtR4T6jwSBFHzkCEctFIS-Lo890DjbxfInkExFFB2Vdj06MYzkn0cm5J9is4OOUInaHQHCaI301jOHNRquYDXMbBlxRzhKAsJT6xrAcA6cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36cefab0f6.mp4?token=HOkCVuNY-f24ILz-V9p00mZhgHRpurWcSC4YJc7cHvu1Y9F2Xige6GCEViLBWtIrlHOsJysABLrjfrl4-GvvNVPWy9c3z92_dfWbTJ7S0-GQrE8kmQBA3Ct8EBdW4vRyeMfPtIhXL55tZzwU6T_RPuHrTq8-uqsuEcATcboRiMwHKxqImbaitHSrZUDfSyRWKMWbQxLufIGueXbGKkZO6NBhJCoRB-OGa_b-rExKZKICtR4T6jwSBFHzkCEctFIS-Lo890DjbxfInkExFFB2Vdj06MYzkn0cm5J9is4OOUInaHQHCaI301jOHNRquYDXMbBlxRzhKAsJT6xrAcA6cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم منتظر در خیابان، از بدرقۀ آقا می‌گویند؛ نمی‌توانم با آقا خداحافظی کنم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/446503" target="_blank">📅 01:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446502">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde79d832b.mp4?token=tlEWgkmE8zDl8T50Vw0-YZ1T36fgPEBehsYXuSGm2s6FO9CQtZm2HhoBdVIpBnZ8dLFPuRt1Guy-vmUeZvaOnioV3qn6QTgYMm1tOY_up_5_rAPxiPqcBXzMgmmjGNRgW3mfCGDg-sdpRRrgElrQDIL64YDccd3Q5GbSjA-lCqo3Kvl2SroJpxeFK9p9yN7XWETh6KSh9U4hcIbizrT0CeDMh5rjQgh2FsgJZXOD1zenS3hxW1gauwDNHrd-Q1Y1OvCm0TsJKqjyDuI2mtJm3hCwTkyJwPfF0cuBG_cQijVfupiry_IS3T1nuSOWukpzMi77IM7Fy0JT0I76oO1zNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde79d832b.mp4?token=tlEWgkmE8zDl8T50Vw0-YZ1T36fgPEBehsYXuSGm2s6FO9CQtZm2HhoBdVIpBnZ8dLFPuRt1Guy-vmUeZvaOnioV3qn6QTgYMm1tOY_up_5_rAPxiPqcBXzMgmmjGNRgW3mfCGDg-sdpRRrgElrQDIL64YDccd3Q5GbSjA-lCqo3Kvl2SroJpxeFK9p9yN7XWETh6KSh9U4hcIbizrT0CeDMh5rjQgh2FsgJZXOD1zenS3hxW1gauwDNHrd-Q1Y1OvCm0TsJKqjyDuI2mtJm3hCwTkyJwPfF0cuBG_cQijVfupiry_IS3T1nuSOWukpzMi77IM7Fy0JT0I76oO1zNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمای نزدیک از جایگاه پیکر رهبر شهید در مصلی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/446502" target="_blank">📅 01:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446501">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6b30cc11.mp4?token=HddEpSYPrfOp8j54crFFpD_XVPQoEpj_m5Mtptz8E5VhY2IugoO4gQ8varFi53PFB_wZAn1Two2zLcCIMbbIzUkoiQ6-uJ_7O8WInYWhpDrgd73zcoNrSMjTD9auSHklQjBn41jW6-1ViTZ6_2X5kfBqDjHHLF8mE_ICDwCsxN0stC8LUEuifYZbfuDA_AB6kIZYngLJfB1ELbyZpTlVoknXGIUiCmaIxwd1ERGEH8wcf7DAoEsZIR_HlI7FugECK7EUVXKBCigiJzL7aQRt26-dpPa07KJc9qBGjmZE5woNcIzM7ovCkK5keuFEk512fcjaQAMhgzr9NPqZcJx4Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6b30cc11.mp4?token=HddEpSYPrfOp8j54crFFpD_XVPQoEpj_m5Mtptz8E5VhY2IugoO4gQ8varFi53PFB_wZAn1Two2zLcCIMbbIzUkoiQ6-uJ_7O8WInYWhpDrgd73zcoNrSMjTD9auSHklQjBn41jW6-1ViTZ6_2X5kfBqDjHHLF8mE_ICDwCsxN0stC8LUEuifYZbfuDA_AB6kIZYngLJfB1ELbyZpTlVoknXGIUiCmaIxwd1ERGEH8wcf7DAoEsZIR_HlI7FugECK7EUVXKBCigiJzL7aQRt26-dpPa07KJc9qBGjmZE5woNcIzM7ovCkK5keuFEk512fcjaQAMhgzr9NPqZcJx4Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میهمانان خارجی حاضر در مراسم وداع، از رهبر شهید می‌گویند
@Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/446501" target="_blank">📅 01:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446500">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bG4mAErDJNmpnPDtY_xOVIVVRjZk2HtgHuKucJoRnG1vafDmB61Wh1794iY9pgF12Pu60Cj2WQjoAuT4Z6z75F1QsCP39RDpCuM0-hwhw8Y8rHr_GDiJildPCBRUhcHQ-RjeDkaH-y0GoL28okqvtOnMllwNeXrwEMllN8XbAJJuVgts5vP5acXACsLtNCex9398P7HjaNVaUYJKCJP5h8aB2j41F-9Z3_KkdztYTBt0UvcYfeg_nOlqzklqRmQP3L5AkFG4nHMGWQP6r8PMj2jQgCu7o2An48_rDBP0JAHk1XsBAO9gmAiWlgtVDgIvv-TTLByetZo7A963TgTZbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخت‌ترین شب زندگی حسین طاهری
🔹
«سخت‌تر از امشب توی زندگیم ندیدم!» همین جمله‌اش کافی بود تا بغض‌ چنبره زده بیخ گلویِ بیشتر آدم‌هایی که ساعت‌ها روی پا ایستاده بودند، دیگر طاقت نیاورد و بشکند.
🔹
«امشب وقتی وارد بیت شدم یک پرچم بزرگ دیدم که نوشته بود اتحاد مقدس؛ کلمه‌ای که آقای ما برای آن خیلی زحمت کشیدند و بعد از شهادت آقا، ما باید حواسمان به این اتحاد مقدس باشد. آقای ما فرمودند به مسئولان جمهوری اسلامی اعتماد کنید. اما از آنها مطالبهٔ مؤدبانه کنید که خطای محاسباتی برای آنها اتفاق نیفتد.»
🔗
صحبت های حسین طاهری از حال‌وهوای اولین شب وداع با رهبر شهید را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/446500" target="_blank">📅 01:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446499">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36f486aa29.mp4?token=ESxqDpGPg2P52aSUPTbACmp40ER-m97ENYovKHlFm_TaM_f00gjmRBiPHttVQGdwh3mQkOQf-6iy4cIJn0to_xMiO_jJ8pyU0k-OL45emBDm7-2xyFQ3J0NWp1dS50z2qUcBVtXx5wAkxZfexCDwLAxp26R8_TgEZsAsB7Y46IC3q52W39y6IuHA0JRvYQ26Q5SrxZSp-4EeiltboqRm02shYL3lZVe5-YwLCWXU5hviGHDiTNDLpXN7DwAXRl2bYXu_AljkiO5Gu8SFHxkx8UPCZ2ozyKDO-gq_VTBYqjAEL4RrSO3V1qaMn_gPyXrqvwQz8oGPPy1uEN3TCwoeJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36f486aa29.mp4?token=ESxqDpGPg2P52aSUPTbACmp40ER-m97ENYovKHlFm_TaM_f00gjmRBiPHttVQGdwh3mQkOQf-6iy4cIJn0to_xMiO_jJ8pyU0k-OL45emBDm7-2xyFQ3J0NWp1dS50z2qUcBVtXx5wAkxZfexCDwLAxp26R8_TgEZsAsB7Y46IC3q52W39y6IuHA0JRvYQ26Q5SrxZSp-4EeiltboqRm02shYL3lZVe5-YwLCWXU5hviGHDiTNDLpXN7DwAXRl2bYXu_AljkiO5Gu8SFHxkx8UPCZ2ozyKDO-gq_VTBYqjAEL4RrSO3V1qaMn_gPyXrqvwQz8oGPPy1uEN3TCwoeJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مصلای تهران، ساعاتی پیش از آغاز آیین وداع با قائد امت
@Farsna</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/446499" target="_blank">📅 01:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446498">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55a87dc475.mp4?token=KdxPwsYOpBHzB92cL6kTpyAkMmx3hL7EqXIMKLZJCLPpD0AKe3at_RWno9MGI0ljfWyT1r7A97ZmMO_HC5QmfAchbaaW65c9Fdhn3qjSM3DJhT9eg3ZHVMHrM1-SBkU0phGprlgylapyiBFXV00MAWQ9qftCtRCgbqqpbpkgAXQDz_Szg6RLntGDcBApNOPLbQyzaWqWKZDX-QYs6oWEKw6RGfG9MwoUx0uavNl4WFFIYHfYQr5o6pwW-zsL2Ef4tG8ryyX-bFxjISIOADXwJAi-x4G09C62cqCu7-zZ3raG5hd937ERQHQAp6O98cJQaEtE61qhckF4LM8LKgfz9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55a87dc475.mp4?token=KdxPwsYOpBHzB92cL6kTpyAkMmx3hL7EqXIMKLZJCLPpD0AKe3at_RWno9MGI0ljfWyT1r7A97ZmMO_HC5QmfAchbaaW65c9Fdhn3qjSM3DJhT9eg3ZHVMHrM1-SBkU0phGprlgylapyiBFXV00MAWQ9qftCtRCgbqqpbpkgAXQDz_Szg6RLntGDcBApNOPLbQyzaWqWKZDX-QYs6oWEKw6RGfG9MwoUx0uavNl4WFFIYHfYQr5o6pwW-zsL2Ef4tG8ryyX-bFxjISIOADXwJAi-x4G09C62cqCu7-zZ3raG5hd937ERQHQAp6O98cJQaEtE61qhckF4LM8LKgfz9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همه‌چیز دربارۀ مراسم و محل وداع با رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/446498" target="_blank">📅 01:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446497">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/495961d30c.mp4?token=RC16BRedv1VBRU0LqJQ5fP7KWPNf6pFlisRi3sIUjUf3dn-nQVgb1AEWVjdAWZ5vqLpc5nq9pf8z4am4TvupeBKfyKEk-17lRjx-ZUap81c4Xm_E6GqGvBFIV8sTSu0fQJqir7YjJrKKEC_88feij551qWjOwOVTb7SxeWh5Jur_R9QKeNLjsIpieSAFhhpiaVZ72m3Dt6VpkXAM6iJ1sl3kESnTgcMHszLEKVqiHFL5xFDRyek00lBRrEtxXs5bfg6JlwkybunLk4ShTXDjUeLHjQFEstowDcFOrDA8FzTt--PcvhLpDDr3iX60XzYBG3I_4OhsDh5fyJjU2u6-AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/495961d30c.mp4?token=RC16BRedv1VBRU0LqJQ5fP7KWPNf6pFlisRi3sIUjUf3dn-nQVgb1AEWVjdAWZ5vqLpc5nq9pf8z4am4TvupeBKfyKEk-17lRjx-ZUap81c4Xm_E6GqGvBFIV8sTSu0fQJqir7YjJrKKEC_88feij551qWjOwOVTb7SxeWh5Jur_R9QKeNLjsIpieSAFhhpiaVZ72m3Dt6VpkXAM6iJ1sl3kESnTgcMHszLEKVqiHFL5xFDRyek00lBRrEtxXs5bfg6JlwkybunLk4ShTXDjUeLHjQFEstowDcFOrDA8FzTt--PcvhLpDDr3iX60XzYBG3I_4OhsDh5fyJjU2u6-AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سنج و دمام‌زنی زائران وداع با آقای شهید ایران، در خیابان‌های اطراف مصلای تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/446497" target="_blank">📅 01:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446496">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‌  یک استان دیگر عراق هم برای تشییع رهبر انقلاب تعطیل شد
🔹
استاندار استان واسط عراق نیز برای حضور عزادارن در تشییع رهبر شهید انقلاب، چهارشنبه آینده را تعطیل اعلام کرد.
🔸
کوت و العزیزیه مهم‌ترین شهرهای استان واسط در نزدیکی نجف اشرف قرار دارند. @Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/446496" target="_blank">📅 01:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446495">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiamunR03TZJ1Tb9L2dpYRccFhibuLrYHVFAfkM_8pkyeO7YCgJby2XPqZdikJmLKcBf77KKQ2vsm-oUXRi4sSdcSVo3PHTAucfzb_LRdc-jhsYOQuRof0GMUe887wpazJnl0tpPtyw0-mZWBTm4sN0M2FtzSZOhPe8WqvOGNJRFWFqFs5W_JlN1_584_BnOdIn1Spa1h4G6RMskOMmyjgLQ94Dl1zh_N710Xkb7WwfwEU8bxzEdi95njWM2Jy6QHoB4kfvUqH3onykGTaHxYcCSq1m8azegmq87r9VdMh5wFgWu2ptDtuTvuyFGrUtfuCo69p_w9of13Ys7oXbbkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نجباء عراق: ارزش شرکت در مراسم تشییع رهبر شهید، کمتر از مبارزه با صهیونیست‌ها نیست
🔹
دبیرکل نجباء: میلیون‌ها شرکت‌کننده، خاری در چشم دشمن ظالم خواهد بود و فریاد مرگ‌بر آمریکا و مرگ‌بر اسرائیل تیرهایی هستند که توطئه‌ها، دروغ‌ها و جنایات آن‌ها را نشانه می‌گیرند؛ پس کوتاهی نکنید.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/446495" target="_blank">📅 01:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446494">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMVavkjyoTSiEhNdudPPuU9JknkuX3i4tVX_jK4eTtKcZvZPGqBc6RQdt6rWmhY95FVIckVMWp82rPztjtgNhcaGF5p6wf54twidmbrAiv7ZGjfr3zv6XGZelPvAnNHb9l6akbWU9gSpNutR_bpNJo_NUFaRC1ROibrbOG0-QfLDUmq7mdRisRY-V9cLW-dGDcgLbZRqa8A8VXWi4CczebrNmzEDuNLRK8uoTT6fHBcZRx2tjam9eK2wVM4Ey9jOEXF6ahkTVcmNk73-cFKdnQrToa4eCgl3vLqAsfns13rRMOdqORFuVRlxPMMN6EOzzreag_zBGI9pHUeyug9MsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرمربی مصر: این برد را به مردم مصر و فلسطین تقدیم می‌کنم
.
@Sportfars</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/446494" target="_blank">📅 01:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446493">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lopExvGw7Wzii-Sk0ipaAeXh2ZzO1dnpXi33U7AKWMHk_2yIttBe42KgCNxYHd5F0pYvhxhSBzKa3HZzmAyaVSo7HrkhRvBI_6L9xGZ268auklPtYGhlM1AXx1YXW50GIGJy_A39lUEFFFuryZ8sumA8dsQVP7EFvNqvN4e-b4eAFrLb4zLygcDykztBXk04v-jp-3a70p3-HLW46708B1NA5eJ1OvLQKdolb_XV9xkcub3pJynVvKvF2ELDPc2MTsP-r0CPwYtNcfJqA-N3tM5sHylCpwTKof04y0yLFQITIpQu2nHOMz-nG--hDrfzAjHLckIVICLC0XV9abdUaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نقشۀ مسدودی خیابان‌های منتهی به مصلای تهران   @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/446493" target="_blank">📅 00:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446492">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cn7FOv1klRj7fSfBfC5ReYLQpQnlJab2MB5qOcfrVxNInXgLSKqJu-j7cwkWQRss7i7EQ5-pQhZisTMxvFp8dBcgd0tYRaRRmOrifGfCiG_9WWM45BsQjTzGh00XfqNg1NlpxBklKIdCQ_Pf7hnNqx1EVQWUrLkRQAsxOGcjj3G-MtQ8aX1AvpA5KlEvLXmVDyK-2Ai5WI7V45o3JmyG8u7M7VZHkV-6O6E6VRjkdC8OB0L1Rck6BY69tFFwJTgMEsMAOG4fc92E-D5lilq1SCP-8kO2PXP79KYH05ieBtwyACBmy_m910q7HjTxRcSPw2cyQeD-Yoa2imiLWhS_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
وداعی به وسعت کل عراق
🔹
طرح حشدالشعبی جهت فراخوان مردم عراق برای حضور در مراسم تشییع پیکر رهبر شهید انقلاب.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/446492" target="_blank">📅 00:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446491">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eU8uiE_qXWbW0f_FVoDP1gO8CBIy6z0KpPO40E63asbm0fjbf_ZqKzO-q9267eBs2I2VKMSkQrV7Jg3MMFX6K2CB52TMJizQIufx_0vaKzlQWu3pTS8tTBv5srO4KtLy03gSfD3gyQ36BmSnQUNNQv9BVdHL0CvX_riPG8VFYzJtyH55Z4NQjcnjHAtawL1MdWKFDEFDQc0OmJoc-lx3zObEG2WTxWAjOe0nd6De_unupZNV3_94PLlBYvEAT0T6B_YMskz8tSc5TOJh8KvtWLQu0RjqfUayIWSvJH3g6BG7_lFwfZ5CgZbs3YeyK0Of-EJI-G77EyxfhrrrfyGGhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نقشۀ مسدودی خیابان‌های منتهی به مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/446491" target="_blank">📅 00:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446490">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEvf_mpxujgYRVVmcYl1naamgSMK-fRdlTKQAakqpmnDFF1qABac37aISX3LxC7gTol6TEaTVKPcD9DVFLUNiqA1x4awTHfBVtbfAbTeBgocmr_JTGvqhX3vnjKXfjsy9vf0O-loSSOxThmoHEAXapfastEk0tuMh3_yR7pq3iYU6kiIEkwEdWu0FsE412ifBjqPxUBdlIPXL7IOzidWFJOR3aaa1Wqrg5qJ8ZUvSapeEXrw8DRi6rt7XHkxfZE5iSMAznGu0s3VD4CylEJqDX40MXjdxzSOguUh48fswJI91w2RbwfHQEsy4M9HMsjKcNyCx0W9M6WOlUwCU2ZEcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
بازدید سردار وحیدی از بیمارستان موقت مصلی تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/446490" target="_blank">📅 00:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446489">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d77ec6308.mp4?token=LyRA7qtOEwlKBGqHxgroxp_1Q5_ToOtaptGlbpw3ODovMm4cNK-_8RxnZSxy1164kM0x-IOX03f9n6CnF31jBQgBoLLc-otPjrS0MUrj96KDYkkIunG86vvCexr8q-fhc0VmKHtZVqRRRSyMG61D9smkx8rhHLKwajmBnJ9E9PKnpOOgxWv7IT77wfxNi6-EXrUECs0NaSrRdyjfLuyXJK2yyOlopIaJN22xY-Bm_o4IWcYATEfspnIr5Pi-ZKGtZ4f_sRdlUNTkHqRSbRmYdBPzPrrAnUDt7bpjEc2qfSCyaL--U2bbCJB4mX9xjvx8-2m8Yv7DdQQ5ofkhgqLsU2Uy5TNaxCtrZzEXuzj0XVfzMZ9kN9RRQwp8iPfYr8jSMFEPmkkFwVaK5RHrEsazwFLrevA31nLdM-71rocr5ovy0yGEEWC740s7MvtnOI9qvIoKgijt87wOzNMm4L-UpUcdVLvtyD7nlSFSj5IjlFWS53xihCE3iNgFxMVWk8WHxcyC5eHCeV2lbDc9JmuMvF7pWdgdoSr4BZOjucd6yp58QppHfQX6WG_rfVHjX-9yYco67sb-aXOVP04J0Bhty5TFkl_W9ybDhwGB_gApdmUP3_Op55P7onpyhZzImQxHvb2hYyvfQ6OcKuKGwWzo0q8uYK5s3MUB0QFUo5ms-Ac" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d77ec6308.mp4?token=LyRA7qtOEwlKBGqHxgroxp_1Q5_ToOtaptGlbpw3ODovMm4cNK-_8RxnZSxy1164kM0x-IOX03f9n6CnF31jBQgBoLLc-otPjrS0MUrj96KDYkkIunG86vvCexr8q-fhc0VmKHtZVqRRRSyMG61D9smkx8rhHLKwajmBnJ9E9PKnpOOgxWv7IT77wfxNi6-EXrUECs0NaSrRdyjfLuyXJK2yyOlopIaJN22xY-Bm_o4IWcYATEfspnIr5Pi-ZKGtZ4f_sRdlUNTkHqRSbRmYdBPzPrrAnUDt7bpjEc2qfSCyaL--U2bbCJB4mX9xjvx8-2m8Yv7DdQQ5ofkhgqLsU2Uy5TNaxCtrZzEXuzj0XVfzMZ9kN9RRQwp8iPfYr8jSMFEPmkkFwVaK5RHrEsazwFLrevA31nLdM-71rocr5ovy0yGEEWC740s7MvtnOI9qvIoKgijt87wOzNMm4L-UpUcdVLvtyD7nlSFSj5IjlFWS53xihCE3iNgFxMVWk8WHxcyC5eHCeV2lbDc9JmuMvF7pWdgdoSr4BZOjucd6yp58QppHfQX6WG_rfVHjX-9yYco67sb-aXOVP04J0Bhty5TFkl_W9ybDhwGB_gApdmUP3_Op55P7onpyhZzImQxHvb2hYyvfQ6OcKuKGwWzo0q8uYK5s3MUB0QFUo5ms-Ac" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خداحافظ آقای عزیز ایران
...
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/446489" target="_blank">📅 00:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446486">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pRl2vFZ0_E55tQjF7fRTRflKTuayOiRcHKygmXuyqJ2jdyhsHfFIy0EUaTJA58ZoA8QfXDtlD313Aj1bzHEZ1zzz3g646dhhdSzdd5Un5aaTRT23rro9qvUQqRcOVV3HTZSZguZ_ufmnA_yLDEeIPvTvCrwZYSwKOdGy_sN4jI0jIb0D67gYktT3DQfwv4UFC9qQWe1ZhjlMMpqPSQgGV1ZjVBbirEaFzM-9IGnVrVpAuE5Kn12TLL5KsQzchKyj3fAP_Y7-CtoNpnjDxx8e2h4nRfbgLqTUsta-Ovx9F1e2DYEg2u266KCrVSR108Gm350NAPbnfaU3Ny7v2I8Ufg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QIokOk5Z_t9ofjgrqqIJbOCiYvRrpIQewhAUJs7Mexx9owPbpVdn7AeaNrLXW6Dl9KTrtqviPcQtbowSSnCTbJjAMTR47sGqW7pRywIDLpe1tdZnrF23_KNcSirrkBuX-8wdFzBn6_lIlWxiocP1h0J633a0txLKFIIJu6_OYYXxGrZhic0i6nj8GdRtx3_7mPukB1EdU_SI6Vd7AXP8plXmnZ_AtklC0VGLwTC0cjKoh8-tfy5ZuyVb4JTj89h6R0naipmTTQG4xAeA7i3SnT7zgjQSlGySGJXi-fJ42eHhP3Xa76x_kEX5eixBALJBzyK-b-diczBwJcsTIE-G-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LuowRq080G-HkIGU-bu8O_Wkb6ec0Jx7t4mHwbIBIpJ4vcNu5t3VJZvyUTPK-3SAR8g04uCO16R1vcmVCiJaJNBn2Mw_eRA5IPLkN1am7iKYDf8dgIbeQAMLUZq67xELO1YPKKHmjfDhtSazdE1RE7q4R7OkOflgyRQzZBs8zUTmI4-qf7azRkWdpqvjEj-NZ-8b25AoVBH-SK2TX_-L6R-lClPNNaVhATwm64kJnYZMptWOQ7NLuGmNQstaufU3qqyIQgDpWxCIciJCN6uU_GSXUy3dP2P6p4aR3rgcBo_Sm72a1vraZmWT7y2JnHPPRh8wgIjl02lrYwGAKWiLFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۱۳ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/446486" target="_blank">📅 00:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446476">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzS7wLlq0KUQGjm90eDAVIlaxTlqj0PG571ObKHjf4bjZ4lVn8YkB2BRKFO86YatL85c-rxFMt3_FYQUM4DNvgEraVc-aIZmCXmdCPkErltrE4H8oE7lJ2sXtnniCoAzm0dshTOy7-bPFn1L9kiEsJkKSVsX79hvTtUlLZ-g5xbZM6I4HoioSQu-RXMvwAXFI0LiBYRxMYl4DtsNszNFi0nAGc5j_vyy2UhYYWaJ7GvbAOWWkJ_TgiL4ALuNf7JCeTiWyPpjRS4rpC8LrUQgkFpg1XwAISq1CItwJir5FHWnbBm7lJ_quC2S7djOJiW1s9yC2Pul9TOJtgb340UR8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aSUGxGhF4XPnPUtrJfn_magjruNPRmCECnOnlfML9gXGAYLRM7KikRhyNlx40KZWSTPKmSyuJK9d-64g_hh7m39MoPYsIZoYCG7Lxi_IWgRXhcxy8ieZqksFGVtMSUch1vAHEJUeiYhkG5ovvZ9IMSxetjGthKMBJ0mvuSTO2lScLo1d_fV8u8VNJlobnQ_dasdA7xbSzctYn_aGYmOaxR2hlD90voIftx89mcY8By3eMa3Gyj837pZmYKJ_aVtM99_ne3AS4qwvofKsOr4zQqESc5cXvzNiubUp4dKxY1ZgAt5-0dO7iqdlAIyruGWB4cv2_ACZPSx-vXzaWsGfFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MvAxuwmtGPs9XzCmxL05ur6AN3YiKfpBQiabzYyLMD-QPlLZ-BhMI2_esf9lJdsiowU2p_Gihd-fO5oTgB4JICQMAj5hPxc2Xtau1767ZpUEfOckPA8P_O1_l-4QWI0aqYbGE9ZoGhoxK6Ee13VPYWtc6cXEgjzv_cCwoGaP5plyFsa84KZoPVlKvrMbmTWzjR14_bvYQpJAaWviV_xeomKD80AHzK8GEivX0bicw-sN5WNdm_sx2kVAVMp-CVoYcyI6iUCfmiu9XL_kq8OPw2mOTsXXqbm-ITayWKpVGavGLJbyHENAaP7me_RjC1Xb2yQ1-JsEkYyWJZDwkEm5Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TTA4xGB8eA-5hHB0sm--x4SFjVNsbIC-TQnMuUDvuFnNecHUMJyDHPXSaG3XdEmEMZveuEsbzGUzhl_f3YfxkIhw0juJH68Xis1LJ_CKrjXLOQ__p6Pehkvtz8LUyxab971-BuxW3GC261Q5_LcXsl2Fnueat8WcGdZsQZ9ehvOXa1w7BHW4j0TXod33IGnVw9ye3lgjowsDKntCO93XjBHm8u91UAOKJyUH2KcRZSSUJeDnuuB8paaYZNqbNoPuFg-oHxXCF_qju6QALpqSEAq5zVoAnz6zp343dZM2IWWJp50oxdqWn8mlXX7a5zfcAUQQQq3yze9C5s3p6jiXFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_-LhLSRq0FSO-hBMtFH7BFPgw6dog-9ybR1yTUCLiQHv_OirlQtxhBgPLMD5b0tLbaOGvwhvOMWo3ZEOpXtLN2oDWPdk9gK3d3TAQrfjRlXkZnJBU9fGTFRg1eQNCj9x6D66yoD7CBhfsCZP5UaY-2FqbFB1IjPKb2KTy1iVw5q5kTnPU8nlY2kIYly57VyfuEO87LxAknFd6BSFFhPxdmojVGyPC72O0XkteIv8Se6hpAKV9HTONhjz7Xu2_DqkZplFYhRivjplHYjJ3dblcXmqCBsrjgSCTiqV_JIwxRxP4DV6LRIYIFpHys8CeCUcJEaRqOCNZ_cVhwl_NhgEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pWj34PPYITlMriNxIU-m1UoWs6_F21txdv13cr8j9abOAnaoDiG43YJI-KGAkowEwPB-4cURKfz6PINooRg84Bi1vmfXyrPpLO4c_X8NQO6EKQCWrN5wt-OEW3FWCM4BTyzcm0FqNrYESq_BcdPjudnaypQWLRcv-R46U_AFCsyuVPPdBtg3ItencHNLjGPzQlIRyfxqNir2jI5bj_6SK_cYVyUbH7E4favU3f1Sh0DMd3y9nZ9vscfgzBg0LY5LePrEkik4ejG-Y0dJThnJrIh5MLmghFjBnR4EGmC1xZU_EbOPIDIXOIDUDllvEEbDsA1702aZ8QK3jg4Uoy97pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ll48fmFfo6E11uFkB4Zng5gD6xOGPN_VCdWZML_lyOWdMMNDtXt7f8DSVtZQGY6CJw7w6xK6_ZyU5l9YymnweWzE3NZTuzmbfF5NLC4Y_-WQW_RkNocJ73YAA1KfkJkx3l-RvNQLAI1_heWMszx2P1w1sfMTemFgqVPC4F55wcRgajCT2YN5btxwAIr5RXpBlvNIyw4n8o-spbbr1lMA-PtQ3D2Vxz7dXG-mO98dMNTDhQoDinmqHgzHmrcRloZsOCp6gPVjQ4hegzMLx7pyiT2akHoDKTXX1tCFB2QyBz3oUgznlgP8WzdZxe8_uLrJrzrUhaySyWvNr4pMKeBNxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iapDBioGGr8uPn9UAQwfRKV2rEGbP8eB3Z25ID_aTWm7Az29xVLpW4topsteR1e7dSp7aoIQlXzrTzfYYSp_zWhIU2H9FxISemfbPtgOxI-xS9wkvmcQrrAO3j95CFp8la_Og6XKdJJcUgrJRcYrobwWjEeeAV-8x7PmLOiRbucdkIrFP0F82H69Xts7ypemJaUetk1XKcLyT0cfynKKpQVN2XoL_0U2Dlfe_z__QnN2CfJrN7q_0Zu80ZTtCuTdBhZLOU3l_uL3OFjeWV8O2rzkQoqNRMH-z_LHcloEL4KaBNpt_CHerJHkwpGT2mCiaOkIKg9JhFLcJcHqTXDsmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KqUQY2gPDtWulAhy4N2SAjHMXWTBkJjGvfw4AhKU3PLPN08G4Yis2NOdRiArEo45BPZvWpUuhruojNSIkTuQM9D6HAKgTiJoSRdTTLC5fPPX74TG5XgOEpjLTb1CSK6xyWfcJhMVzMkEUaeg4t4NoghtgGnYWNBAv17qawkZ_kl6feySd-r_13OScvW9NNCASICl6CqShDNWbm8U7RRXvPhRQtcAfyd6cvFLqMgJiBcm-SZBMdQwUZjgRQ1BxTybLw4ekAsXBztyJHjanrM3Vm9mbCdvOB2Ao4rlVfTOjyR2KRWCkqJ1eg0ElBpm0vhzJq8ggodwjHIDf4nOxy3R9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LF8x3pGrZrQbjnLBJTfkqjjNp2atJE1IFFYKuk7CjlDAmfbWTicXaiRE1Cv93s3qsIujR92PJs6VEKCzbGtD1Kf2hxJT-yiRtGrGKL6MaxlXatGWYukTkPD45yqqzdnCsogTIbgfDU-UhIM-dumfb1vazeelQnjSs5VjHOHaY6r2znNym3r--EpRHEznKBRtsO_fIgheLtvnrOWGZddQePEDZ0CtO1yM26WP_a_oNEAKYySdIPGzuS6C3jrBYYCKd3Q0fZySjMLa8fp5Hg8n6EHdbfj_-6W_Y8pl8DHlMtN4iTTs--tvFQCd_byX3jv4oykYRJhF_ru3TmJd1K35mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/446476" target="_blank">📅 00:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446475">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ogv6INb1M5LdPSsbS6iJXfZ7yry5JmWmI9ThDS-uMVyNSFHf3zjz7koCShSXf-GkHgvPdaKHa0WfCAUA7vuaiCz3KJqb6nxPbi2pjJRqTFUI7-dSWZPX3tK0F1OTbxVLW98oYpOdymEwNbVMnbCsynmnP8PzbIzl6CxHW1dcqVjJ6XDPMnnKZrZ8DU-2FKUCcRLLrv_UmxSHv-j_AJ4lT37QXMO97WEwUKxUZnMP_VnyoHKFW_jnS1eiyksH4YTQj7JM4YvZuHEDp54HDSmsocyQrUgPnhnaQim16_NZQ6dIsXeQj5VutPfycgkD5Se3xkjGSZysix0tMZSAVTnIEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صعود فراعنه به مرحله یک‌هشتم با حذف کانگوروها
⚽️
نتیجۀ ضربات پنالتی: مصر ۴ - ۲ استرالیا
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/446475" target="_blank">📅 00:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446474">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwikcbWnViwkJ6n2CJ9SoBqAsBxtXz1EN-byiohG8HKF6tPEo7MH44xCEMkv48jRVloVYERhB_n-FG3ZXi8Y3MNtitmrA1t5A91B6GJP2h7kMQRf51scrZHtS0DJwYZG6g9SiK-x_aCE_LlxNzN_O-DWqhkKuwTOY3unnYX7xbpXZtXh2sbaZqY5K7NQ_fMY36NIWW59N-3vUCes01gy-OPCaRaF1gf-af2tfzPyx-yt0EKPRA9V7tUVpiL040MfkjKudj0HS-qs-fMyMxVnlBM78PkkGi4vEmRR6FZkpRB2uHAOBlOZzW3DcSLK5L111MgQeQUSILDtchpob4GYDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تصویری از شهید مصباح‌الهدی باقری‌کنی داماد رهبر شهید انقلاب، به‌همراه همسر و فرزندانش در کنار آبمیوه فروشی خیابان کارگر
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/446474" target="_blank">📅 00:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446470">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZqBuQtuquAiTHm4qt6ws9QcMpikeAZfZzTTpcLrXoeG3tpH0uxJuVyN1oSBLLERTZy9gcm6mOfcuR1WkMGwy_-dYNcVaLHiGcWZIdfaSXEOD4qSwg0Yd31GOyWJZ1Z-K6AP38zx3UG0mE3OQy3lLT7wHXFDR9LMCWK68PABPTbJY4YNkZC3VR-cZm_vCjRIf1iDuAR7Vn1zVsHV6A410vpPQeMgSKESEeUGHCpBjaKUmQ9kkmfZi4CuK5xx80yUnQT0dm_9CX1tho6kW3oSneD0XSOaIUFxFxsJ3vNuQb1WoNpGtMEVZBYscajNe2FrO4pQqJzmC5LIgHkImIp6xhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JjHtTn38MU2Q9M77z1MOoRq-1Sa5O1t8Nk6Vbb4eT3tE67eMn6bhbT1xLYIWouoQKgUm6UAUoYH7ELXgBgEwRWCYmcZ9DPaD2JPPMHgW6Zx36qbkAvykKgZDtTqfIFN8qSAUhdql0x0Hi85NabHsGWg2yanYNyApur_slHKY8iTxlmcUR60OncbFVACzUunyopP_mU0BGEIuUksUfiO2RTGJIx9OJG6ldOl7AY7dWgrvPggOJoZ8XX_nGpY_B1remymFpT4m-2RiCgaWf9uQp6ie9iIpPNrWr9GNAtmf8FlBmNduIqyW1xsFrE8omY5vLf0cn2vMHUlX4Ny38WT0zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fHdf_czb6jqqBpZfHlGcCJCTm1bfh9c5_U1LGcsstdX-6-HEEecMoshRAw1gL8NzjPXxx22QphMujF6Lv7j2yjaqDV72iGyLHj0LuVbHYTIFRAbYWmZLc3JUCedYbHoi9gERUbGyu57g37UoPnQrYW_9l1piTagiHfY0LeyboYXqDgTr9PhLo1eY5N_xzUesP2VhlFfc4RZIi_JUPbCm9bZdKrjtjN145p8k3imzTd7fJ-k_AcXD9_ZciYL66JvI0Xrw8e9latUcspJAIliCXrh2DVkS-qt6JaIuZ0RFDL2pX0Njwt0yI7XsdOUaaszRWWPXSTFnFkI19l5yJHjg4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bR9gGxDtjZ23sYU_qy5QKpMJsIGW1eQpKusQil3l0wo6Y1sPBHbu__zLlvFcdSLjg3NlUzi6_0M7Uhui4G9ZUK5b5UzV7mGnulN6KZanhFrOcGo2YNDwyZyZyGkVsrnkFwCXtFQs2I9i0OnomDIXmrp3ae4qSr10mcFCZX9_QkrmRudjYp3KB-qP0GvutrKlybLF22F9TKPGlxelBW1K4GCvZLlFJGDknTmPVdkE9sNHG3b39oZbu8oLhdbvXuCFt_9yWsszib-mTYDhbKZm1QHp1PG7myqdzGK_VRbEZjTrsxhxWEBkuRttUDtRu1mLNJqeZp_U2aC4BluIjiqbMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
انتظار مردم برای ورود به مصلای تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/446470" target="_blank">📅 00:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446469">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuM2jXl1NB8e4emNYnbSdFHG00tmsFX3VKEShbWdpnPiAoRcxSdn7lVKIhf4quenhT3BwpAWXne-KkJpIhLR6LqEMcE9CudFXTEi4XIcfSdw3edfm9otYnZqPjcGzvX_lTsBLiJp0_ApT8Tq5-wVuQAjXTqRbIhFxYxW_DDEmkamnTv9bHdLPiTN5psbNJzdmkeYBTHB64CryAlczOS_ETgB6JV2pTo-2vaZIeC_nc1cdLUpTyxi79GjWWbvKBwX4UtRMWeR3VerrI2m_6k8Us7gBGpmLHTeNGXMdoZwSELhQftZx_3bEJLtrpqGDGikJIdOkdMge8FNlJdKPBruOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درخت خرما
🔹
روزی امام علی(ع) درحالی‌که باری از هسته‌های خرما همراه داشتند و در مسیر با یکی از مسلمانان مواجه شدند.
🔹
آن شخص از امام پرسید: «ای ابالحسن، این چیست که با خود می‌بری؟»
🔹
امام علی(ع) فرمودند: «ان‌شاءالله، درخت خرما!»
🔹
آن مرد در آن لحظه از این پاسخ تعجب کرد.
🔹
مدتی گذشت و زمانه سپری شد. روزی آن شخص از همان مسیر عبور کرد و چشمانش به نخلستانی بزرگ و پربار افتاد. در همان لحظه یاد آن گفت‌وگو و کلام امام علی(ع) افتاد و تازه فهمید که منظور امام چه بوده است.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/446469" target="_blank">📅 00:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446468">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ada85a1d3.mp4?token=bisy9gNpFAp7QHREpr4BigOwS4ikfcpSDQ1_csWftzWf1SC78Y1dm0_voN4yUCiGw0uBT4kQ9IWXmRXfVX3e7wJZ8ByHngAYIx_XerSEks5v_bbIs6_l8kuEenmwCIwbYZUif6Vv7M9vtw7Bf8xLEE-ouYCi1CXf3FUwMZ9Q9mSiWhllXAdGgwmTpYsynP_gwiP0nCaXj44h02S-R2tf9wVB_I3cS9x1GMKgBkMz37O_fGg8khbE-60uvNTSKByUbrwrl6NHMYeLuLSXEc0F59z8vyIOefTwv_N-SSmA0CvTCjU7ExYHkgKF16DVoYoZE4z4r0Kg1JtyZYuqB2vbtT1SRDW136WSfAO5VfYLV-bSfybPRhYXegafg5O3v17eFPngwbBhKtvMFcCu7qNGdJXoigALyKFIVC7GUwwuOkNKvpPg6yhBRW-MPFSyySQ_sUh3fXhgtTkQZaSjoTahyJ7J2rXkIS3rwSXZN_U07OAhBThsM1aaHb3ssEp53TqLvtslhJz116sGyV-DK3scTubu88EORGeWmgnYO4jg6K1nd4--RiJ5NK10pj03_6OVX6cUGFtehrCinWMMbdJHCLzLS90q2Qz5SXYXLOnoF0mCzOTGcwb1lP0RBnoGbsxqoWwN1wO-jS3VHetg3z0FT_jnBM2J_YlmVLVHviMr06o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ada85a1d3.mp4?token=bisy9gNpFAp7QHREpr4BigOwS4ikfcpSDQ1_csWftzWf1SC78Y1dm0_voN4yUCiGw0uBT4kQ9IWXmRXfVX3e7wJZ8ByHngAYIx_XerSEks5v_bbIs6_l8kuEenmwCIwbYZUif6Vv7M9vtw7Bf8xLEE-ouYCi1CXf3FUwMZ9Q9mSiWhllXAdGgwmTpYsynP_gwiP0nCaXj44h02S-R2tf9wVB_I3cS9x1GMKgBkMz37O_fGg8khbE-60uvNTSKByUbrwrl6NHMYeLuLSXEc0F59z8vyIOefTwv_N-SSmA0CvTCjU7ExYHkgKF16DVoYoZE4z4r0Kg1JtyZYuqB2vbtT1SRDW136WSfAO5VfYLV-bSfybPRhYXegafg5O3v17eFPngwbBhKtvMFcCu7qNGdJXoigALyKFIVC7GUwwuOkNKvpPg6yhBRW-MPFSyySQ_sUh3fXhgtTkQZaSjoTahyJ7J2rXkIS3rwSXZN_U07OAhBThsM1aaHb3ssEp53TqLvtslhJz116sGyV-DK3scTubu88EORGeWmgnYO4jg6K1nd4--RiJ5NK10pj03_6OVX6cUGFtehrCinWMMbdJHCLzLS90q2Qz5SXYXLOnoF0mCzOTGcwb1lP0RBnoGbsxqoWwN1wO-jS3VHetg3z0FT_jnBM2J_YlmVLVHviMr06o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل عاشقان آقای شهید ایران پشت درهای مصلای تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/446468" target="_blank">📅 00:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446467">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjwOIURE7aLdG0JiAWNtYFxC67XBPS6kKZ3APif7xmHZpcnendQGPXjz3F5z4q0q28psT-2Wsx5sbpUXSvUbIyk7apC3wycSaB639NZOeHVMsObKsONXW2rDBUQDaxcnSIlH11v0vCfaZLVvzXlkuaKDkh7Rm3ayoDdmCrbIXIOD1h7R3NU4Ji8PJjiGRPoxbkT0AxFd_ywq2lDPjiphW81XZU4Vg54GsOk_AvXskV6GWjHhhzZsSvLj2ltN1VB270ZY0ijX751P4Yp1MUiaKXulIZuUONdt__cPzITMRRLzwLgyNlhERNmMV-iBz4Kq7WjSIg6Hr18DzDnR6W0Wxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
| شنبه ۱۳ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/446467" target="_blank">📅 00:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446466">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jC4-eEELaJkN45kKOYOHF5Vn3KLPGpVOVooDStsTBOHWiHoAS8ji9ur1SPc5ZCwl5-zeDRcwhOsDkCzHQWwR2Of1dL94nfnY1n9p6Ss7N5qsYtt4kCVwoTeoWjZmfyxoP1yFU4lZUjHNSKOikH1qYQsSur3CYLOlHP8cpu6nypZsIyagQNE05MgyXluVGlmGZFEX6sFgX4okrYWmydmFSq0s_YaYxUbZXgio4vQYORzkHA0Wsb-lR-NdxEiKfadFnQ7DT78mgltPcDlu9bYhr8dtpQQVekQwSExYDQ60l3O_Sd57gRnVTxJQ9gJ2XXwjEwqWj8ycL1ErsKdFEHveNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگاه رسانه‌های جهان به حضور مردم در بدرقۀ آقای شهید ایران
🔹
تقریباً تمامی رسانه‌های معتبر و مکتوب بین‌المللی اخبار مراسم وداع با حضرت آیت‌الله خامنه‌ای رهبر شهید انقلاب اسلامی را پوشش داده‌اند.
شبکه سی‌ان‌ان
🔸
گزارشگر ما فردریک پلیتگن از مرکز تهران گزارش می‌دهد که انتظار می‌رود میلیون‌ها نفر در شهر پایتخت روانه خیابان‌ها شوند تا برای رهبر سابقشان سوگواری کنند.
شبکه الجزیره
🔹
مراسم تشییع آیت‌الله خامنه‌ای قرار است به نمایش وحدت ایرانی‌ها تبدیل شود. آنچه آمریکا و اسرائیل در جنگ علیه ایران انجام دادند نتیجه معکوس داد زیرا حکومت نه تنها سقوط نکرد بلکه قوی‌تر شد.
یورونیوز
🔸
در صورتی که برآوردها مبنی بر حضور بین ۱۵ تا ۲۰ میلیون نفر در مراسم تشییع رهبر عالی ایران محقق شود این بزرگترین مراسم تشییع در تاریخ ایران خواهد بود.
ایندیپندنت
🔹
مراسمی که قرار است برای تشییع و تدفین آیت‌الله خامنه‌ای برگزار شود از لحاظ میزان بزرگی و اهمیت آن در تاریخ نمونه‌های اندکی دارد.
آسوشیتدپرس
🔸
آیت‌الله خامنه‌ای به خاک سپرده می‌شود. او در بیش از سه دهه رهبری خود ایران را بازسازی کرد و این کشور را به یک قدرت منطقه‌ای تبدیل کرد.
الجزیره
🔹
پیکر آیت‌الله خامنه‌ای سرانجام در شهر مشهد که به دلیل میزبانی از حرم امام رضا مقدس‌ترین شهر ایران است به خاک سپرده خواهد شد.
🔹
خاکسپاری در نزدیکی یکی از مورد احترام‌ترین شخصیت‌های مذهب شیعه، افتخاری بزرگ محسوب شده و بازتاب‌دهنده نقش آیت‌الله خامنه‌ای به عنوان رهبر سیاسی عالی ایران و بالاترین مرجع مذهبی آن است.
خبرگزاری فرانسه
🔸
انتظار می‌رود این مراسم بین ۱۵ تا ۲۰ میلیون عزادار را به خود جذب کند که آن را به بزرگترین مراسم تشییع در تاریخ کشور تبدیل خواهد کرد؛ قالیباف این رویداد را «یکی از مهم‌ترین لحظات» در تاریخ ایران خواند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/446466" target="_blank">📅 23:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446465">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a79a851cf.mp4?token=HFkJmGvYyt-mIULvsolAu52RR9PfwUxJRMByfIYpa9uICLuQ-MD3ZTRgRl811ihqNvpI8upeWuuGZcbJcwhOLIxC2FAznTbWO3cB-YY-XWpRkOzEPv-Mh_vb4bN8dPvGEKG8Hkb7SCkTyHaCJWNNVYvp4ez4R516AFstV1JbJMy4x1sMQd3Yu_wB75Aq8Hb9vK-VP33MT9SAvjw7LZi22u74mcRHVZkxol0NdIeEmFh44zOozorJAz75w0vPJuS4KFr6KDxoEKrrsIVSRMcTBL7M8S9oSrbZbC_nYdk_x5rwcT3N5EZig_1OvNu1cJwBLkkN4MXxRBl8m66q7jvD71F2pBPiVOQPMqbZALC-yXgGgOnF5xzKSGGH_X5lC3hbJVtwT9e6RbWwAIYeCUDSuCizDvoRb6qqzncB-Oni37Ie8K7k1cCQNGpssGnOptDeEv3JybRICty3PWR_Y0TEzVV2oaycL_QcPAwPsQvBTYLXhaK_OOkMDupBq0zrGjohKx9OHD7ePVB-0-akdJe8TRFVBITtxFAGlhC5kaKhc9iX8RVwC3rC1cYJ64-cTJ4Y38F8O2y2EO9uNX3pKlnXL7CAHe2ocJ-4nwl7PRYAaIfE4KXu_uIYL6KqqqAlzao3_I83XdaED1gbTFWU5LMQSlqpwpA2dAM2_NZRvqXZxuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a79a851cf.mp4?token=HFkJmGvYyt-mIULvsolAu52RR9PfwUxJRMByfIYpa9uICLuQ-MD3ZTRgRl811ihqNvpI8upeWuuGZcbJcwhOLIxC2FAznTbWO3cB-YY-XWpRkOzEPv-Mh_vb4bN8dPvGEKG8Hkb7SCkTyHaCJWNNVYvp4ez4R516AFstV1JbJMy4x1sMQd3Yu_wB75Aq8Hb9vK-VP33MT9SAvjw7LZi22u74mcRHVZkxol0NdIeEmFh44zOozorJAz75w0vPJuS4KFr6KDxoEKrrsIVSRMcTBL7M8S9oSrbZbC_nYdk_x5rwcT3N5EZig_1OvNu1cJwBLkkN4MXxRBl8m66q7jvD71F2pBPiVOQPMqbZALC-yXgGgOnF5xzKSGGH_X5lC3hbJVtwT9e6RbWwAIYeCUDSuCizDvoRb6qqzncB-Oni37Ie8K7k1cCQNGpssGnOptDeEv3JybRICty3PWR_Y0TEzVV2oaycL_QcPAwPsQvBTYLXhaK_OOkMDupBq0zrGjohKx9OHD7ePVB-0-akdJe8TRFVBITtxFAGlhC5kaKhc9iX8RVwC3rC1cYJ64-cTJ4Y38F8O2y2EO9uNX3pKlnXL7CAHe2ocJ-4nwl7PRYAaIfE4KXu_uIYL6KqqqAlzao3_I83XdaED1gbTFWU5LMQSlqpwpA2dAM2_NZRvqXZxuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دعوتید برای «سلام آخر»
◾️
از ۶ صبح فردا تا اذان مغرب روز یک‌شنبه
◾️
مصلی امام خمینی(ره) تهران
@Farsna</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/446465" target="_blank">📅 23:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446464">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
آیت‌الله بوشهری: شخصیت علمی رهبر شهید، منتقدان را به مدافعان ایشان تبدیل کرد
@Farspolitics
ـ
link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/446464" target="_blank">📅 23:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446463">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‌ بغداد هم برای تشییع رهبر انقلاب تعطیل می‌شود
🔹
با اعلام استاندار بغداد، پایتخت عراق روز چهارشنبه برای تشییع رهبر شهید انقلاب اسلامی ایران تعطیل خواهد بود. @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/446463" target="_blank">📅 23:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446462">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAZ9MTChmuUmI6cXEEYd857dmts23c9fj-YkJl7XPYq23Uc1qg3dSn5wh5S0O5y_kiHlQhpu2qTstql0MfYaFHjAS8PG0BMQ1_woLbMuk-z8ZtPQvuOZecV0RzpMkmhQcC_dB9F836ohbG6xHLitpWgd7qWyXmrMbW_nRUrkmx5d1Q_8C8HDaBZu2ocwSz1BFprttDQWFBjzY3c8v38Vchy4vvOAWVuyFHmdyM--35x2fKkmZoSBEQWZlipNHtrovV1GdPM-gInT3N6dj0yIIj2BqqfdwvV9u5K3TnCBDqEl3TK-SX8mzXrvBSiHOMg_WJSV_Mx2kAXgt1BZ-Q1muA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از شعار نوشته‌شده روی موشک عماد با سرجنگی شدیدالانفجار
🔹
رزمندگان هوافضای سپاه در آماده‌باش کامل عملیاتی حس حضور در مراسم بدرقه رهبر شهید را به شهرهای موشکی آوردند و شعار
#باید_برخاست
را بر روی موشک‌های آماده روی لانچر نوشتند.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/446462" target="_blank">📅 23:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446461">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a350193e58.mp4?token=hJmTfo1I_WA_7PphnkaFtJ1daW8W3ijAgZ32KT8MnbFCUyvVPCN8JCA2vlPrSXVNcWtjgY4Lzx5CfvKxf0zG20BImkDkgf3YBYjPsF3ms-QSgYU5sKuQK3H7zDpeR8b2FHt8nTmHdgh95JB7Z_j3xNDRBIF_yKhi6YFeRCJDN9gpMWxjymSnkitg_6hOk-3q6lrhh5qjzaHBG4ckJBQGsbGL8rpDptx3VHzCtfjWIfq3Oo5nqt0mzoVIM4BPv8OnWymCg51gWiAn_EsThuD47HlSntEIvcN0P8G9JnZkzWNPyvmYKWtDgNmV6jLl_MyBkFkyfcu6QC3oYxWLY5GSLHUg59WSE2wi76NtG7tttZoEgPEhVhLZKXTcqmgP4hea3Fkt_0EdjJrWTqtvG9p-lKxqA1WbUCy9Cj1ljfs-LZC59GVVOzGGrMBdN4ixF07Pi8HYXBAHlt03ATEUW0cpF6F7fzj8GxwAb6gGe3H_FRTkB-ITCRYpMoOZl8hFjIOrcYCn1OWEmv2nfM06RvzWnZoVIMH6-Cl6oeIH0MhCJp0b0_v5YQr_rFkot9bO75h8HF1P1Jx34a2FRYqZF3B2D8FNx9pbIu_QYRUvXU0jas3DmZcNW7uvOCW_Fp-MxSDrQYA3LpcLkmCR5aQ_gcoFo-_YX4GLhM3YDbb9qwP1Rcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a350193e58.mp4?token=hJmTfo1I_WA_7PphnkaFtJ1daW8W3ijAgZ32KT8MnbFCUyvVPCN8JCA2vlPrSXVNcWtjgY4Lzx5CfvKxf0zG20BImkDkgf3YBYjPsF3ms-QSgYU5sKuQK3H7zDpeR8b2FHt8nTmHdgh95JB7Z_j3xNDRBIF_yKhi6YFeRCJDN9gpMWxjymSnkitg_6hOk-3q6lrhh5qjzaHBG4ckJBQGsbGL8rpDptx3VHzCtfjWIfq3Oo5nqt0mzoVIM4BPv8OnWymCg51gWiAn_EsThuD47HlSntEIvcN0P8G9JnZkzWNPyvmYKWtDgNmV6jLl_MyBkFkyfcu6QC3oYxWLY5GSLHUg59WSE2wi76NtG7tttZoEgPEhVhLZKXTcqmgP4hea3Fkt_0EdjJrWTqtvG9p-lKxqA1WbUCy9Cj1ljfs-LZC59GVVOzGGrMBdN4ixF07Pi8HYXBAHlt03ATEUW0cpF6F7fzj8GxwAb6gGe3H_FRTkB-ITCRYpMoOZl8hFjIOrcYCn1OWEmv2nfM06RvzWnZoVIMH6-Cl6oeIH0MhCJp0b0_v5YQr_rFkot9bO75h8HF1P1Jx34a2FRYqZF3B2D8FNx9pbIu_QYRUvXU0jas3DmZcNW7uvOCW_Fp-MxSDrQYA3LpcLkmCR5aQ_gcoFo-_YX4GLhM3YDbb9qwP1Rcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزا و ماتم مردم بروجرد برای آقای شهید ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/446461" target="_blank">📅 23:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446460">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e008d976a.mp4?token=UzyUrEfR3YK1AMPf5goJmYW8TLj4bZLyEspKnT6Fo7NywgbtTtB4q05A5V3ht6s3JkxVdfnDYYnpHiJaG4KKKDxGg6-YsSFqHUGGSnTP7v1FmGBS1IfyOgo6BoC3VV3v1R5K1LfwRINaohDpeG2WVvWkaGGNEdNhB_aP3MbNER4hNDmy1HNJZNM3WE2-ZTYQ2vxnYE3yvGp3dFEqPQeCIBzlV1zPh94JCCa3P3NOivjKwExOqr61yhcGD2fP_pF0HQ8zKuq3cGa5Kt-_VBMgxMl8BdZwszAPXdcmpOlUzdyUghLZje5vbla1qIwxo510ISWS9RSdBNJ0rnRx18J61g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e008d976a.mp4?token=UzyUrEfR3YK1AMPf5goJmYW8TLj4bZLyEspKnT6Fo7NywgbtTtB4q05A5V3ht6s3JkxVdfnDYYnpHiJaG4KKKDxGg6-YsSFqHUGGSnTP7v1FmGBS1IfyOgo6BoC3VV3v1R5K1LfwRINaohDpeG2WVvWkaGGNEdNhB_aP3MbNER4hNDmy1HNJZNM3WE2-ZTYQ2vxnYE3yvGp3dFEqPQeCIBzlV1zPh94JCCa3P3NOivjKwExOqr61yhcGD2fP_pF0HQ8zKuq3cGa5Kt-_VBMgxMl8BdZwszAPXdcmpOlUzdyUghLZje5vbla1qIwxo510ISWS9RSdBNJ0rnRx18J61g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ستاد بدرقه رهبر شهید انقلاب: اقشار مختلف عراق مدت‌ها پیگیری کردند تا بتوانند میزبان پیکر رهبر شهید ایران باشند
🔹
روز چهارشنبه بر پیکر مطهر رهبر شهید در حرم امیرالمومنین(ع) و احتمالا در حرم امام حسین(ع) نماز اقامه خواهد شد.
🔹
رهبر شهید پس‌از ۶۹ سال…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/446460" target="_blank">📅 23:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446459">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🎥
گفت‌وگو با مردمی که از همه‌جای ایران زودتر از موعد برای وداع آمده‌اند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/446459" target="_blank">📅 23:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446458">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8776d64d2c.mp4?token=B5Qs2XwSauX_4K9_BXb3u5cbBpl7v5bpUGp5BnR8ytyjeQuMDiL2qcQsM7S0-DENGHMeB4-B6noe0zdF9JdmUbhveaQR2nj3JRuMqYIsScHHfmevvDawUa1TcUiAatqX389Qcodv_uBj1BfjIBk99S8It-n9IB8hSrB5ZVlpDKrohx037jL0uEp_WkfF32-K_qGozKSLGYNSPm19DM4JpMfbluWxtfnxjn8on74HLHYKqchuOq3XggwACGmWvAd1AeHFQFMlXCK9wq4eYVUwSCa8l8yY6ndQAr89gZw5FwrZ-fY2phq1ejfcM0hAjSFWVq-t5Be7czuPOv504ZmvcIG2Ve9e84ho-gz5cfCX8S13kJL9LZd9-ptEPRjMY_KojHflX2bU2gEK5TN8j1ljrGmQR47X8VIzasIjFafvhBCct8kxHjPzCSfoUr8LptAlml-JpqxiEUcmi9F745s2cap7jZYdpH9nCkE8KzbsS5SuU1Ug4PJn-VETSPVr6jHok_7pR_q7nHXcwiXCCZVVaF915arktYt2L1RdHapbWpl6JhZju0iPAbqfrx_yU77YgRt1434kKpZ9bOjX3-jtHUQjUuq_AU8vdkJ7nkEjJqzsLy6K384vDA0i-NxqG5ZsqkOXgIv2pbrda5-b56iXoieOIgbyOCfjg4stQ7Jb_7c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8776d64d2c.mp4?token=B5Qs2XwSauX_4K9_BXb3u5cbBpl7v5bpUGp5BnR8ytyjeQuMDiL2qcQsM7S0-DENGHMeB4-B6noe0zdF9JdmUbhveaQR2nj3JRuMqYIsScHHfmevvDawUa1TcUiAatqX389Qcodv_uBj1BfjIBk99S8It-n9IB8hSrB5ZVlpDKrohx037jL0uEp_WkfF32-K_qGozKSLGYNSPm19DM4JpMfbluWxtfnxjn8on74HLHYKqchuOq3XggwACGmWvAd1AeHFQFMlXCK9wq4eYVUwSCa8l8yY6ndQAr89gZw5FwrZ-fY2phq1ejfcM0hAjSFWVq-t5Be7czuPOv504ZmvcIG2Ve9e84ho-gz5cfCX8S13kJL9LZd9-ptEPRjMY_KojHflX2bU2gEK5TN8j1ljrGmQR47X8VIzasIjFafvhBCct8kxHjPzCSfoUr8LptAlml-JpqxiEUcmi9F745s2cap7jZYdpH9nCkE8KzbsS5SuU1Ug4PJn-VETSPVr6jHok_7pR_q7nHXcwiXCCZVVaF915arktYt2L1RdHapbWpl6JhZju0iPAbqfrx_yU77YgRt1434kKpZ9bOjX3-jtHUQjUuq_AU8vdkJ7nkEjJqzsLy6K384vDA0i-NxqG5ZsqkOXgIv2pbrda5-b56iXoieOIgbyOCfjg4stQ7Jb_7c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ستاد بدرقه رهبر شهید انقلاب: اقشار مختلف عراق مدت‌ها پیگیری کردند تا بتوانند میزبان پیکر رهبر شهید ایران باشند
🔹
روز چهارشنبه بر پیکر مطهر رهبر شهید در حرم امیرالمومنین(ع) و احتمالا در حرم امام حسین(ع) نماز اقامه خواهد شد.
🔹
رهبر شهید پس‌از ۶۹ سال حالا با شهادت به عتبات نجف و کربلا مشرف می‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/446458" target="_blank">📅 23:09 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
