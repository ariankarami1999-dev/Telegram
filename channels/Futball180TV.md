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
<img src="https://cdn5.telesco.pe/file/DPP5HhYYUGYjyVXrL_7I4Z3Ky7Ov59Ar0OL3a2X0GauUquZ4Kxdq7L7tp3IK-wJfxR0g3ZiHw2OL8Lyb2j646j65fJLOiKpDEFH9bX7BhmWV6lU72bGp03gHg0RZA-oUsv8ZT338Sjj9dhq2tRATaaeG30ym7oVsqvrWiPNdSL5YKq1SHMwkc37Ew7lSVXTgVMYZEOPIDhuhT82pSyHehlsiiTXSxSAYRQlUTg1AVlnn8RJtUJVRcHWrQteDbVuWT4ivknpxD9nnxqDpgWp8BAySCGDojkCsxRzaTrT7WGewZ_xS-Mlise-UGV7HKPQTZvYFQVJyEXoe_rsC6NbsCw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 637K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 09:00:04</div>
<hr>

<div class="tg-post" id="msg-98275">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3b324ff50.mp4?token=kgPvcwMo5HkdoN4oj2pJOhZs89IWwxZjik_fCGdkzxckjWlh2RMF_O6o1aIBYR3HO70M8jmbsIJUkFRVQU5fYD7fzzZwAghc7WDga4FrJE54aja6kimljJ1WHZqD6D6AFGmYz43fU-Nd6KDP6IaZdmk71uiToKrTOs9ZVBMRQISlD1ycj1DznJN0M3jQkmOYF9btnHx31er4OdYSPeHKCzmdXhGmdMx8Cq1ys_2KbReA1YDZHnDu1XQLIufG-UeE2Y7J-uhXFbxqq6QlzjgO7fdKy80Z5Jm5SEerQ0xRZUJw-V4AFKdJ5BQcvVHvNklLM3IopIUFsOWaw0z1-NniBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3b324ff50.mp4?token=kgPvcwMo5HkdoN4oj2pJOhZs89IWwxZjik_fCGdkzxckjWlh2RMF_O6o1aIBYR3HO70M8jmbsIJUkFRVQU5fYD7fzzZwAghc7WDga4FrJE54aja6kimljJ1WHZqD6D6AFGmYz43fU-Nd6KDP6IaZdmk71uiToKrTOs9ZVBMRQISlD1ycj1DznJN0M3jQkmOYF9btnHx31er4OdYSPeHKCzmdXhGmdMx8Cq1ys_2KbReA1YDZHnDu1XQLIufG-UeE2Y7J-uhXFbxqq6QlzjgO7fdKy80Z5Jm5SEerQ0xRZUJw-V4AFKdJ5BQcvVHvNklLM3IopIUFsOWaw0z1-NniBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها استفاده من از خونه خالی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/Futball180TV/98275" target="_blank">📅 06:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98273">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aRCDxs5jjiXtko0q9SXbsdq31O6kOKQwgXq4DmtptIxh_5ZedbuARIhGJFWlRhV0haSo-ojQ5YcQe0CVqOVmSal-56nUdSEGCLJ_19za7S7U-ho5yW4wlAy_XYt8McGw1GyhWJRyPUN92X6lKr98sms8OEZ-kfusLxnMS6FFh5pYg83HCnlMF2TkKI7wSEZqsYhM5WmVxh9Di-y2xhvPZHudF9inNNiruksLWkZsoiOQ9Edkc4qoBprA_HWQkey04IreomPRm60moi0fDDVBvpFCBJzMkuo8Lv5lqivCu0ga_morlVSTVLsuZPL91IyYofgXYd4rCkbe8SjNyfiqCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JAFQPryxVkkaV9tTigZeBHDOfqUGuNqnZj0lHDdPGxN8USorCSgyyJCiQhz9YoksxmgRzdRcF6XqcF0mUQZpt7L7k9aTCoUYBtgKW2WtNOH8h6NgbwQyJW5iFXbHTNw94yetreKa_xtwG8eWvo3w-ePFnsV0p2gUNkaLa8QqBmivPeWtmP61WVjif2T7j5VoovF7W71v8HwR_TQpSEt9Oeky-cannno4q7F6KHeU9ZMsMLYFGlRZvdS-Pqi1gLiW59nQKYqh_TbG2VU2e7Z_kjEA5wrbRgKmUREudGw7moRKcs9fVQymvm7zgvK4Y-ATYApBQNw6ha2ws6tTVbi55g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
👀
پشماتون بریزه که مهرداد صدیقیان رو دختر مایکل اوون بازیکن سابق لیورپول کراش زده بوده و با مخ کردنش کیت امضا شده باباشو ازش گرفته:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/98273" target="_blank">📅 05:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98272">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb9f230059.mp4?token=LE-v4BxHSgZChjOsbKz-8rdU0X3ZX5tvH0lQFOEub51PEaNx1hw5rcilP1a0XVBMYFM3-wnXxVVGhSBkURHvhF6C7Nynt7LuPKs14n5BSjDHH6kh24XJaIfDiKfGT49yicnFgOlBVLlHLSOWqr6Oxa_Ebomf3GtOWrWE-vJEQDIHvd4S8DnEK5rdGI1XKVkdR9ZXrRPF1mWEGgkRW4iDZA2NgSd2BmGJdSfWY3aJy2r55nYp0X-D5Hn5sUgY42VcF92e5zl9C-nr4jfN6UYltCOytQt9XwS_AeJrf7Tv2RlEkz7BU13QSXcWHkTAnxwdWC41V1SXR384n7nWwlFtBE90w4mcrN_x4pzlTpG1RtewuQ20nvltLYYuUh7Af8oUlRh8Dh2hDHB7UpPTAT5XcIBr_4llIT2NNM50rJwYkxQYaN3-5MiX0XIicUqM_vifi-duhL_nrOHIGQ-vmMHH_gqUysF3mNWSTk6qjppeeLmEf4qUf1LTtUpzL-uGNplJaF6ccbAyO1YiDXd7naPkMdIavBR2Vx1rZihXUwO28P2Mkjxijbc-DRggsIGPlg1eza62ctD_SDWeTnOS_HDFkuR-YoMY-I8eT5-PWel9gAimbqI4F4nIsxeyJA8WoF8_8PlrgJRefZFYhvA_1jWr3exoRoOzfbD3n3Hye1Ux7Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb9f230059.mp4?token=LE-v4BxHSgZChjOsbKz-8rdU0X3ZX5tvH0lQFOEub51PEaNx1hw5rcilP1a0XVBMYFM3-wnXxVVGhSBkURHvhF6C7Nynt7LuPKs14n5BSjDHH6kh24XJaIfDiKfGT49yicnFgOlBVLlHLSOWqr6Oxa_Ebomf3GtOWrWE-vJEQDIHvd4S8DnEK5rdGI1XKVkdR9ZXrRPF1mWEGgkRW4iDZA2NgSd2BmGJdSfWY3aJy2r55nYp0X-D5Hn5sUgY42VcF92e5zl9C-nr4jfN6UYltCOytQt9XwS_AeJrf7Tv2RlEkz7BU13QSXcWHkTAnxwdWC41V1SXR384n7nWwlFtBE90w4mcrN_x4pzlTpG1RtewuQ20nvltLYYuUh7Af8oUlRh8Dh2hDHB7UpPTAT5XcIBr_4llIT2NNM50rJwYkxQYaN3-5MiX0XIicUqM_vifi-duhL_nrOHIGQ-vmMHH_gqUysF3mNWSTk6qjppeeLmEf4qUf1LTtUpzL-uGNplJaF6ccbAyO1YiDXd7naPkMdIavBR2Vx1rZihXUwO28P2Mkjxijbc-DRggsIGPlg1eza62ctD_SDWeTnOS_HDFkuR-YoMY-I8eT5-PWel9gAimbqI4F4nIsxeyJA8WoF8_8PlrgJRefZFYhvA_1jWr3exoRoOzfbD3n3Hye1Ux7Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
پشماتون بریزه که مهرداد صدیقیان رو دختر مایکل اوون بازیکن سابق لیورپول کراش زده بوده و با مخ کردنش کیت امضا شده باباشو ازش گرفته:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98272" target="_blank">📅 04:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98271">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efwdKA5DsSxMOFPuA3uA3_zyp_Hi9dRQpuXnVABTWZgRbQcK_nQr3lk4glQcRfAgYocrxQ1gtWQvMeC6MR5BZEuyqDsy0BDVkqm_GUnaRxe0gKt6L4jcCxlwsYx3zCJO-cHIcIUCqwQaVCoELnbMhfJHBgt_Q8va6wMRbUTkb-C8212KHwnRNk-ReqaeZuUKx8oeqSLDzJMAdwIzCPYSeXYTi9BidLosBY5Ur2BwdZeCqUL2WlOU-w8RSakJSXkt4L3r3d_h4K0KVjh5gDaB_i9udhH9iIX7jPazkYkzBs1X-dd_NOZP1ptw2XYHdGVspIUGcqfbuF-SO-4jimdteg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔺
از سال 2018، کیلیان امباپه با 11 گل بیشتر از تیم‌های زیر در مرحله حذفی جام‌جهانی گلزنی کرده است:
🇧🇷
برزیل (10 گل)
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس (10 گل)
🇵🇹
پرتغال (9 گل)
🇪🇸
اسپانیا (4 گل)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/98271" target="_blank">📅 04:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98270">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrP0KP8bI5XfS_CyCMe5nK-sq1yYZCdg34bSqlaJpKAuJzTfdbLGPmbyIoHDX4DVZ6Iy41G_Bh_dtKKXUa174wCJtGHXLxHqj6Abvx2FnAv5R-J5SDFqkBcrrUtOiy3T1a818fm5fLnNgbSG9sMGuklj-Hjc5vmJEeUGjXFsUa5e15J0G1zJhMRthCg7e87BgEWwsJh-Km6zhvVwQzmSGT61yiJkA4QXp4SOtnZQwk6KpnKjPZy1t1kWorzgPumRRmcA7kCO2VHZZgk_HdQu2XCYAPr9NRAX67x_k2afRgpXdFKwdciYc_R3xuYdcD3Df-gmhlsYjRsEQ0cfzRzKMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زلاتان: اگه من امشب بازی می‌کردم، ۴-۵ تا کارت قرمز می‌گرفتم. فرانسه خیلی خونسرد بود، آروم موندن و حتی بهشون لبخند زدن. بهترین واکنش همینه که وارد بازی روانی اونا نشی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/98270" target="_blank">📅 03:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98269">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b1ac9904.mp4?token=N7akzHYnQ8HpiGLI5gvkJrIB-ex8izeAgkxYJoEH-r0r0txAHSbuL8pDcujSwFfr6aOBTnd0kRHCdB5vTLbsYuNvRCJCB8AvTMCaf3WKmYcetB38sKAPSTG6sAc4BrhJc30Dw_iMqhmE4SMDKa2qN8ngnrPcTheRY6kblFtEadlafQzWs22ipsUOw_oGs1iO7hlR9jwvzgU3zWpZpteIwV5WMr4Y1R0fG80XTxOLRVFZst3eTXEwMlpZT0pAXxB7oR0xS46KlegDKusHJzPuOBNjn8HS1MlJ2y7YrMYPN6CzLuLdn01FAhqcwwpDzAwT0c65N45ovuXlpfVGMyjFfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b1ac9904.mp4?token=N7akzHYnQ8HpiGLI5gvkJrIB-ex8izeAgkxYJoEH-r0r0txAHSbuL8pDcujSwFfr6aOBTnd0kRHCdB5vTLbsYuNvRCJCB8AvTMCaf3WKmYcetB38sKAPSTG6sAc4BrhJc30Dw_iMqhmE4SMDKa2qN8ngnrPcTheRY6kblFtEadlafQzWs22ipsUOw_oGs1iO7hlR9jwvzgU3zWpZpteIwV5WMr4Y1R0fG80XTxOLRVFZst3eTXEwMlpZT0pAXxB7oR0xS46KlegDKusHJzPuOBNjn8HS1MlJ2y7YrMYPN6CzLuLdn01FAhqcwwpDzAwT0c65N45ovuXlpfVGMyjFfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قشنگ ترین صحنه بازی همینجا بود
😂
😂
بازیکنای پاراگوئه با تنه زدن و فحش دادن همه کاری کردن تا امباپه رو فشاری کنن ولی دیکتاتور با خنده‌هاش بازیکنای پاراگوئه‌ رو حسابی فشاری کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/98269" target="_blank">📅 03:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98268">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1wbEydqJJ3J3ChwWlMAA8o5H8lrwE5lCCwOAgWETRKmIr23tgmGReVaFltGDuDTZkZ-AOIXFtARAnhIJ6TJZuiUMIdAQW9pJoPprUnFzEXYNerx9SDiWRJBoUMeWjMu6wx6iYxhVpIwJshi-u4HbKhgTnhL_m6unMduFHQFTdSGhlqURUtHrup6LGWOsHctjFTC-lzLQmRTPoZT_MP_ALvc3wXI1598Qs2gC5xRQ8lIGMObUVqS7mb-9Ti5NJGpHiPC8KoBCmJ56obbuX21O-QZUIZw4FSj-Acl9rpMouL4v2LmrTHe1Bes4PpIqG8uDOgzaBN3C2MjyYhp5usgzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار :" کیلیان امباپه گفت اگه لازم باشه دستامونو کثیف میکنیم. نظر تو چیه؟"
رایان چرکی :" دستامونو کثیف میکنیم؟ ما لازم باشه تو خود گوه شیرجه میزنیم"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/98268" target="_blank">📅 03:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98267">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUQgbwUbB6_83TDEUElC3k450HHRppv56eWYxi6yWz0VaEu0pI0Hd8Smvh03jcGhMkNwgIipwlqUwGSKb97pQooakAn-tKFl_T-gAOwBco_IKhXCJTQe5oAylbnB3PlPTD1BQ4YruhfmIOo-hBt-syuTxXyKQruDaqYH9GkCN2OTXrCn-Vh0rRY9k5-0SQlBIJ2amk1RDJgVP4LFLZ4pABr__RLpyoI0Qnwgu-mKpPoya-VisFJrdwntxCHGRn3y5UjpT1OKxbiW_APMjfDsCENTpjBFOys0FxmaFJ7lqbI6Pcukw0CAd9FSJqNihPcsFldBwDxvfPPY26Pn6kaubA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلیان امباپه : ماهم بلدیم مث خودشون کثیف بازی کنیم. ما نشون دادیم تیمی نیستیم که فقط برای هجومی بازی کردن به زمین بیایم.
🔺
اونا فک کردن ما میایم با لباس مهمونی بازی کنیم اما ما هم بلدیم کثیف بازی کنیم. حتی تو کثیف بازی کردنم ما بهتریم. فک کردن میتونن مارو غافلگیر کنن ولی ما غافلگیرشون کردیم.
🔺
اگه اونا بهمون بگن برو به جهنم ماهم به اونا میگیم برو به جهنم. اونا نمیخواستن فوتبال بازی کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/98267" target="_blank">📅 03:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98266">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIA_X5Pb3Hll4BPS9yBquyeKixhZXZkgGjxJ7qd-HtwbPwqPpuhiocZX9xMsyQgPdJ83bPbBRJMonvFLpDxGzNCfarTPFKVJtaugdvQF_t-CfcNeef3d_cFvzn5UlDHJhUFJIvfPAymrhCELZiz-Q_qfSApF094CJu-mihG5LQzAS3GpgQxaHNzshTKcFPDITH_yvueHwn-rL9tAqwuoh1ZhkNFM0t1ZmlGp7jTgqFkniDRrTiOYPJJEM4XchSnic69st_1nolUynMvnC_UQfswnAuXDPswk1oNbHsSOkS2nSLBLUYHqSLX2z9k4RdbjG5Uf5TC6Bb3DtDasUYoiIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه تحقیقی هم در مورد این آقای تانتاشف باید بکنن تو این بازی. هیچکدوم از کرم‌ریختنای پاراگوئه‌ای‌ها رو ندید
😂
چندتا خطای خطرناک ازشون نگرفت و در عین ناباوری یه دونه کارت نداد بهشون و سه تا کارت داد به فرانسه. خیلی عجیب قضاوت کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/98266" target="_blank">📅 02:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98265">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2KLyuThRYnNqoUwjenJBOclYzA3NAlfkpyO0BemSegRDgNazJhEkhiVUjLjKsuhkUEG4I_rCbY7gwGO68jF5T7-0VHouelgjgEjP8NbEv_zw9wDXq76_bCNKbenYoC9OT8LylLNd2Tw6zwXadC1lFtD697WbplPg5wH6G4vUU7N1GHaSzYUhErb4krBGwyGcOpAS22kEoZWxZa2vXMyt39zKUqJ5T-Y1VfhWyxfIbdT1b4ekkjwLv2KT8iEcFYK2nMKxH0O3SfiyFONsmjpS9Yi9RR4N8gUOU7NJHlBLCKuMau6V-lGbG3ESBL8cHaPjvMBIp08c_9vMwaqOkj2Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه خطاب به یه بازیکن پاراگوئه تو بازی امشب: مادرت خرابه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/98265" target="_blank">📅 02:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98264">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBiKEu8PHllL7zOPfpRWVnzuhuhI-m5_0uTqNxckwfaiuICBjDxDE7c7A0SC0o22VtgV5HSL_QuMXtqlZtl5aGtp2UGWOF2aUr6vzR-M01Cvund3_0gUYw_by-FXh_6iozBjZfe6_IcxxUMOZcwX6OFAEpOFgeLNecFvxEooA4BfG-ZslqO1flGAt4GKKESVlKpcLRFTEjUOmM7PtmOG01q-_eMZVRCVAifhiv0eHEHiZCqV-i6RjYJjESkWVhry4fb_FLZeXkqRTfU2392mCfZSxfrHS4AsRwkYvXTgj71CEhkTqA_l8jJEczY2e82Iqham_shnundZKVmA6_E83w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
|| عملکرد پشم‌ریزون کیلیان امباپه در جام جهانی:
🏟️
19 بازی
⚽️
19 گل
🪄
4 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/98264" target="_blank">📅 02:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98263">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxTLRXRVArKWiN0mtN2XsDrRmqRvIadihgDyiumINFVQInUZwLlrDqouzUgMBkeODVx2PWeV75f1Nn8_0zaUvs4tEFh-tAu-Uuy8xaoQfShCQetM2K0c2Wy8ii5PVClnf4qpEK6AbP8Eo4GVSTh1JqOv9q_XfxBecJUXrcfDp77XiUQRFKtIzrjdetjAwJOsg4VwcnzwoDp0meX2maOJGigl-BSI734wcvNbNEcDWHSuFGEjQ3L2ya_330qTSnbKJXMuHaCJXVTsy0v-leqMqGSg5hc2K8Vs1qlnlu5D1q8JPxTVvRMRpJ2jwPkEEN5V3SnGE5C_VLs71gMa_mhTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏
🇫🇷
|
کیلیان امباپه به همراه مسی، رکورددار بیشترین مشارکت در گلزنی در مرحله حذفی جام جهانی شد.
🤩
لیونل مسی - 12 مشارکت در گلزنی
‏
🇫🇷
کیلیان امباپه - 12 مشارکت در کلزنی
🇧🇷
پله - 11 مشارکت در گلزنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/98263" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98262">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDATdFfoK4bUHhB1CMnwXK4NCmphtiP8VNZcnuLuMjcpuXs3eNi8PV4O3FwdcIrSbZe2VeE4RPRs42H0smVxYdGjKh3VBaMic-vhprGGxKfwlucVe-k0Iktj5hyN2akULUId8mUCgZfZHnKuRrbTyrH49EDlRnjyiPt3nYh70QuVsOMDZCTj5H0Z2Yi0x518MY8j7F6Lq-yfCNaolKMDYJuXxkq0kPqTCG6Cq2KPh_WiQcktvd11VOambA_kVQiBdYOzx2RQKwNMDsHWgp5pLqbSfe1QuLX1rgBCQbBgc4ds44I7asBbsdTtT3OcRH150ZOYOQhrG5U7V0PgEUmTLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورلاندو خیل، گلر پاراگوئه با ثبت 4 سیو مقابل فرانسه به عنوان بهترین بازیکن زمین انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/98262" target="_blank">📅 02:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98261">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP2PzxJE6NY42U1ocHU8T1bjS8eBc96OdyZgVwSVsM5_MjYcKlVl-gGFkdy-iZuYUciXtx6onojYcy7FR5BR_XTjN-6EkRcIkr2zPXSgZp2H1Jxm4xgQVNK79RKQTRLY-YSVxmdj-LPP1f6AICvhcGZDQaWO559-y6ZPYCDwQt86E4fyqLFopTqTCUmWdaz-ad8U1nlkptDLTs5XiS0e02kbvg7NqZURJPfE1C6Kf5wgpsUu95_tx39DWTYHmBQFc6m98G1xZirHXfUF8lIhl_eRh60XTAUuBxkXIc5BeRhOCIT4RvCYSxv-j2E_E9fCKhC6uTc61nNqtea8soGKuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلر پاراگوئه اومد به امباپه دست بده امباپه دست نداد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/98261" target="_blank">📅 02:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98260">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/98260" target="_blank">📅 02:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98259">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PX5D2eNDu3JUsshuhQ6qG2S0Hm0w4XXYICebi9CQLYgtCZBn32q-_try4yKloIhBg_hZzoFU6JD_dLips-UOXPIsLUUyLqNbliMW5-fKOnXpkLTz_Zj8kUso8NJ8dQPvkUC4zerGB7sIVR36syjegcDnzBPbHoMCmkNbFc7bdXH91FQPd-OWrrp8d--ZNMrcYtSVTCXWulbZt3WAURtHc5d_9cBNxrg3cmQ990h1drtTJQ_3hQH9ADP42bwSwznS-SYA4YFGCW8IJakqDJ5UE0Klm0Ej4ckVdeFrer30b8HB-VWKFOu9ehNwSLPjbhp4I8A4J_VHQfPjN9TRG72BeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/98259" target="_blank">📅 02:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98257">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qcQxZ0p4L3rW8nCSnRCwBoJ0gz-cuR3WnRhgTsOu3WdzqRGO0g2r8dERoBRBta_cZpA_4Tc-Y_rfI56lBDivj6J1UujnkndH7ZyUCimR9pg-abOidzhKwzYThRUHAbEDSnvnHoGofRtsnOkWTYObDD53XMBfeuSHITCsVVadRqfkGbsxeyFTKTZls2U2GIp3X_mcJojM354RZxsCELqCPL4Nzf58gWhg1TdHa6lGcx2VWHWQzb663_gR_KqomTVoJ_U_qvcIHjubhYKv5alKe-uh6C1ZI9ZkcRFifsxDvN_de3fYdbSgREeDYS4GEl--3TfgtiZWEnf4ADedxk0iSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UwnS_yr0tTWQwrZWn4F7ZpooAqZMgHjlf1HMULYoAAAlLPTYzHoNlN6kO4C6huaeKUYdnSzMndK_A8fewmv9YXz3ODr7u_GqaXDpd4POkQPzTAp6mt6Rp6eTqta-rO32H1YvFcrjCjaYl-bBxj76SUJIEm48csBQQwSSVaYZ0wXP7lnDnlsF7AbAMe5DvNSqzCL6OPoPF_cL1cXUnDYrQaeckWD60rqRqaClplvcFra8CkY3qwJilaJmCXctr1bxj-4qaZGlmqTBN6Xi0kjC9mO2uh9jBYTVf7tJGIqoIVcqJ4tw0Jbue6NowSUKw8T0KeCIig_JCPfyTAGsf7xv3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت رایان چرکی بعد بازی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/98257" target="_blank">📅 02:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98256">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKg6lEoMEXiXjd2rp_oliuFt8PyoMXCD6yA_Km3GExPnNU5HntOtbhNIIsFBeyPPLPhvadX5HAGRsEq1zTBVgodc_3kbTR346D5B5oadeDsS6In3cAoUtAfeF2DlmIUR2n_m-j9T1JDVedG1AG6Poso391yo_ieobtd3kA8vXdw4Z01fE0TcEit-mcqZeeaFuXdDjSq3NIXJWuYWboJtJsXCd2vCsWdvLLrYAREEHujOpIKbSbNPZAVNEcwk84A-_4z_yZbxbbgLXoRxqEfbmFsCe3u1SAb8GhIv5U2iKtEx_EbKbx-WyjdG6XUj3-VnToAbIoQKdRELOKnjItRTlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آپدیت نمودار مراحل حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/98256" target="_blank">📅 02:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98255">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFKfZmp3U50RXITh7KP46uourlmoe68kL9dspzgUswiJoy7FI1LiEwXk3kBHAqk116TWMkiCay0JOJWehuUdgc6aEi1sOtZzBSgBQnfrKGjIHelL8VN_yrAJNgqxJBp81L6Svma8aWsxWwasAm6xcY0DvzvMvr2Q4iQOC1LFrS3GmrbVGreUf2-VKdxdqQ3b8qAX1XlEU_2REsLl1CgDjgQgZj5W7sX07mM2RZ3PPH4eMr8PGEaGyyB17-ewe5IoZOgmag04oMY75FXlLcc8BYeO16FQnzfpKbJQgQMdZWPYqNNAPrRZhMMUURFOW91_w2KFOhBgEhJybJDrd0711w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مرحله یک چهارم نهایی جام جهانی
🇫🇷
فرانسه - مراکش
🇲🇦
📆
پنجشنبه 18 تیر ساعت 23:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/98255" target="_blank">📅 02:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98254">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_O9lBFcc-pUrH7035w92qiEZtKSl_MK10EgM1PccnFpbmzG08iQxlFY92YIG7c7fj9N9mU-AjzD8eSVuu1cTv_2Od4wXB9a8JJIUiPEUsmFQZ-jW0wAzgwm7Cs0FbTpd8YFt0bX5hdIe7lZnIPNNgtDNax8g-bpssyF7E9rJg20NQ5owcTStMZdyFIeqQtifoaRGwOYr7NPRY8zuJoJnRSKny4VY1UIKmasV1gf_O5heFK8qWlyRtLV5kpxiwZkDyH2RF4Q3qzuwa5J2vzhuwRBqp5d2dxjb4amiOssiQ_cK1wZpJKFi9HvX7lxO9nX4vmGF2QlJXhVbJKWEGF0qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود دشوار خروس‌ها با تک گل دیکتاتور
🇫🇷
فرانسه
1️⃣
-
0️⃣
پاراگوئه
🇵🇾
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/98254" target="_blank">📅 02:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98253">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFbDDx2vKT2NfF51Ddul0fCH7SPyia356kBP-t743TP4e8Lp04RzbphbXpGkE0v6jtg4jZmIpo7K2RvFm3pUNGcV2H5Su3WaB4SJCYmrgWYTW2pVygQ-LffHssN2SIyphKBSNB5mo4k8WaCLx69-H5SVu03toRnjXh7F561y2MfGrkBnK7F8i5zU5su9FhigCT7BkyTixAGUPkVn4ijj__6JavJ8u1nDFrFW7JpXoqTFB0Cy_5mOMzJmmD3hXsAWc5uWpMmPatPh2Bm-dZUKzilUO23H1PyLKgoKL8lF3HJCbzt0gD-AyWjO7uIqvnMLuiUHIgC8T5B2pitAsgn1Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه قشنگ با خنده‌هاش دفاع‌های پاراگوئه رو فشاری میکنه
😂
😂</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/98253" target="_blank">📅 02:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98252">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">امباپه قشنگ با خنده‌هاش دفاع‌های پاراگوئه رو فشاری میکنه
😂
😂</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/98252" target="_blank">📅 02:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98251">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26acefe7a4.mp4?token=IfFB-Ap0zlpUmTJKOg9cFP2oSM1xjz8zYRz3zNsMRm-RV7bF4kebPhkMxvWgTyGYHnBcR1cji3740XnpiXaNTGwymh20XaXpmvxvRVtGejdsyVTORm2KaTCDxn0vrZxecwKzgqoXcK2myiSil3cmvsHVgr-ujXsEcO3X1p89lPOMu0dY7bWZ_f_HZ0FYqZZ8QR9j-PBx1_ebfKLIbvxhvQw6ISuk9VkX9MnV5dSpuSTghPM3KvL_D-ke9hkriprFu3rfVEUnfOh5SeAJKvPoFM18Zv2wFXhPK1psde2G74-xwnTlpRHBc19y1vNlNFOYRSCT-_KfN6p7ZE2qXdfx4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26acefe7a4.mp4?token=IfFB-Ap0zlpUmTJKOg9cFP2oSM1xjz8zYRz3zNsMRm-RV7bF4kebPhkMxvWgTyGYHnBcR1cji3740XnpiXaNTGwymh20XaXpmvxvRVtGejdsyVTORm2KaTCDxn0vrZxecwKzgqoXcK2myiSil3cmvsHVgr-ujXsEcO3X1p89lPOMu0dY7bWZ_f_HZ0FYqZZ8QR9j-PBx1_ebfKLIbvxhvQw6ISuk9VkX9MnV5dSpuSTghPM3KvL_D-ke9hkriprFu3rfVEUnfOh5SeAJKvPoFM18Zv2wFXhPK1psde2G74-xwnTlpRHBc19y1vNlNFOYRSCT-_KfN6p7ZE2qXdfx4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇦🇷
تشکر خبرنگار آرژانتینی از لیونل مسی: "تو پناهگاه و دلیل شادی میلیون‌ها بچه بودی؛ از همون روزی که به دنیا اومدن، تا اون پیرمردی که داره از این دنیا میره.
🔺
بگذریم... این دستبند رو آوردم تا تو تمام کارها و مسیر زندگیت حافظ و نگهدارت باشه. برای خودت و خانواده‌ت آرزوی سلامتی فراوان دارم و از طرف همه مردم آرژانتین ازت ممنونم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/98251" target="_blank">📅 02:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98250">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اوه اوه ده دقیقه وقت اضافه گرفت‌</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/98250" target="_blank">📅 02:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98249">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJpANK-LJclw1xliaGxDotT1k6JJGChDBYSU_p5kDiRjCYK7UAbsQRFj3lEUMNVityZ8z5CLpecagfAl8nWbrs-jplF3icy82-LynLby9kPpGvgmC8hRQiC8s6XfwRIPCZI7WAMjzYJ3cwLsC-855hXEL7n_n8UJlkoAE02frSn9F1H25I9PUKL3gvSnv9SQY9uYh-VyqigsnvQZE3PKLp_WDm0EXAcobtvd1rScm44uYSIumedg6eBXBP9PJ1juJyzASc3MBKiKgWAIvXFNUyYqrPtxBpRf3IaKV5SPAsU35BMoCl7UIbBb2AgfdU7LrDTzJFAIm2VeXSn3hZ6BOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه به آمار 19 گل زده تو جام‌جهانی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/98249" target="_blank">📅 02:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98248">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8668e7ec94.mp4?token=fymwZ7AhfZnm8sAZMKxLSUbsmeloSk_ftqq2oHFNYqCaRUysc-uK93MNsB58_NdO4FnMZoHyJxr9AQszgY9CTTKm0EKqaHRt2nxTMjM7cK2jLFlWOGh_TNwbx2Pwp7BqapX-09a49KUJ7ke3AbTuPPqqCCSXT2ZJY0W5cacThYD9n2j23mNS92KrA4s_-6GT1crhaLdv9RGQTUV_lb85HM39MJdLYRgvPX7DISuZLeaIvJ8QjZhKDr9iIqRf-9cNKus0kVP1QWhze3Fs9BRqlVWiHS3EGCM2ic-anyHb5OZjdzaq2Z37ojlbg1bo4v8TXkvYfMc2E0XhprjW8KtprQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8668e7ec94.mp4?token=fymwZ7AhfZnm8sAZMKxLSUbsmeloSk_ftqq2oHFNYqCaRUysc-uK93MNsB58_NdO4FnMZoHyJxr9AQszgY9CTTKm0EKqaHRt2nxTMjM7cK2jLFlWOGh_TNwbx2Pwp7BqapX-09a49KUJ7ke3AbTuPPqqCCSXT2ZJY0W5cacThYD9n2j23mNS92KrA4s_-6GT1crhaLdv9RGQTUV_lb85HM39MJdLYRgvPX7DISuZLeaIvJ8QjZhKDr9iIqRf-9cNKus0kVP1QWhze3Fs9BRqlVWiHS3EGCM2ic-anyHb5OZjdzaq2Z37ojlbg1bo4v8TXkvYfMc2E0XhprjW8KtprQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول فرانسه به پاراگوئه توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/98248" target="_blank">📅 02:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98247">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پنالتی برای فرانسه</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/98247" target="_blank">📅 02:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98246">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پنالتی برای فرانسه</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/98246" target="_blank">📅 02:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98245">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">صحنه مشکوک به پنالتی برای فرانسه</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/98245" target="_blank">📅 02:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98244">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پشمام چی گرفت گلر پاراگوئه</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/98244" target="_blank">📅 01:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98243">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇫🇷
🏆
🇵🇾
بریم سراغ نیمه‌دوم بازی</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/98243" target="_blank">📅 01:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98241">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MkX1Ug81x9d7PciDJ6BTNu_PuSvUZ3cC_Tr7yS_1e73JVOW4Wl3a0WjyNiEGhQp_e513MowkN2LeuvuqZbPZh6zX5UuFSyeBfIKWSCal75PgOarRCX69XiUD12L2Lsj0HeEy3ymeUHgvLm0ER7a_06oTJXB5Oe4pKXyXM1etkNd5WCAIdDH6JeSeXrgJF4Ue1E7F4bnzcN4GOsVtY_nLUb7Llib4i3wNvyubeE7QUkAuvg28m6_dtc51IaW25ZtP8JljIT_oDh_KVzjl2P3I62xR9ZTeGHhpkUyKgeyWNsvM3QTFealLkwXaQ0Jx3B6vFA-QXNEYd55d3GJfNbcylw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YaE6mqdRcKdbre8wdidYib8SR_BrHIO492312UIp3TVU9Xb_C4_0vq_34JVUoNi6i0C3XiFuxwmuze_TZ-EEC5c89ZQS0GL9DP8lFFiqnBH3WiURKNFML0cWnjVOM7MpS22laGSmn-R6zZ1uCd-8REJqxTQGL-Cox8qNnS6XhzQR2bBeqcr2zItTEXg_ycdf36hYMQ-VO7jE6dpgGaKaLgi3LTa6zLpMIzXJ69kkV8TE_53zfOWrjAXegdKL9huHjfku899ze6r1D0XwJZ-VP468XGkj75cDn6kHJv_TPQjJlJuZc2kLN0OxkUtqRSS-pWIdp2pAsbVYYDRCTUOhsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
مراسم سالگرد استقلال کشور آمریکا که در بازی امشب پاراگوئه و فرانسه برگزار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/98241" target="_blank">📅 01:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98240">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auhXF4FkNPemVB10LZl3UH4rdsoZFFxX-cNtza2vq-VaHiC1lbS338qj5kHb_HOZctrXQDVAuQrPqA9xLkUBc-oBbTT9mcdkMIalZwVojYYerhokKSMAz5__YCJqgZ-jMBqkIWVu66OknI5Ke8Qro0e7N3ZhSZkQv9CmIFh_Nt-ZJRDwDLq_PX2UYoN4au2LAPb1tn2__Wslt5na2wf8u4REp88R4L0bvST5jEncqV3nj1PTqKM2MSp_B-cruAgKbOncnTFee8itquTfva4wvm95eFH2FODmChsCZOb4D1-OTONwLAzXVDqdVuXAWcKlyrzOv4-lzTlztCyqOZaiIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
حرام‌بال پاراگوئه از XG بازی مشخصه.
🇵🇾
: 0.05.
🇫🇷
: 0.15.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/98240" target="_blank">📅 01:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98239">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پایان نیمه‌اول؛
🇫🇷
فرانسه
😏
😏
پاراگوئه
🇵🇾</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/98239" target="_blank">📅 01:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98238">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پایان نیمه‌اول؛
🇫🇷
فرانسه
😏
😏
پاراگوئه
🇵🇾</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/98238" target="_blank">📅 01:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98237">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBxZSg1gsSe7A62v4__tpWjeaRWGoYMgTA13wcuRGd8H4MoZRIM9qkA0hfrIS_b5JTMD4jCG5VPzy2jDOurOV_76lb4keYmcYb5SfbAJdOmDihTv4pBEBcBF3FNlXJsovvk2bz-wAN0Pe5iKN13vvhFoSZlPdgKxvtLPolwL-vrZo7sPYfAM7z8FBgVScXPuAxySVogiZmj1ESH8U0Wv462Geu-s-TVci1d8l-wgaMJbMLgh1LBP4kg4SodM8X40jNkBCjG9GR8yrGD9gRrlG07ZZQr5QiFMUn7IGrOKdLO7YD5lAnK8ltChbw0lDuDKGf2x6wIymYirZmPI-Fw4FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درگیری دیکتاتور با بازیکنای پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/98237" target="_blank">📅 01:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98236">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tbfzw4yk-h9SVyLfaOX759i8Zg6SPz2-frZq3AkP7TJ_xxInDszHnT7PsvqY77xySZ0FXrCq0RmXi7sWu3AYL-5sxQTDACiotPYeaEg3PgE4GINJ9TFfwN8SdI55RMNd9nb0PHprSJvdI8ON6qf5buE1p1ZfYOC1O9mQYTlycnViIZO700VNucE1c-Y6OBDg43HEww6k8Njs4EltiHIF98POAGrNEFwKXeD3RDOh0gwKUwET4nHsCw0-Gag3Y681uzpsNPPGB8rkgi21kYC22VNHNEehB98mLvFDioTN9gQHvPKsyGAwHTEUICbF65_oGbH2BUB4uy7Q7XSONvaDoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرامبال واقعی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/98236" target="_blank">📅 01:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98235">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پاراگوئه اتوبوس پارک کرده</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/98235" target="_blank">📅 00:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98234">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bdh6Ly-BxH3Ggo6m21FR7C7LrN_ECNQsO1l_QkYrDNBi_3mrFOBiIRczP0-KTENUHaVGIa2qOqGrKXcpFzGpXyLc0W6uw0HSkS2KTg4I0-BcINtvie9x0EWbmp0c3vvG2nVdNEJx81ha1Xmn1wzc0S22Lc7qZZjCFpHfpuLiramaNuhaeCPAYoh3y0BgSyCkolcxtL06_e2fRggs1GB414N8gbQSjlK5qDiPvRxqghh6cxJVnhLFPBr1agMqO1dSlM38q0pH8HphVTg_XhO-L1a0H-dU-7yjasa2w9TNpA6h_w3gbumhncPCbsJjMDT6U2UnmcdgMvFUxxjYdkiVig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراکش شایسته صعود بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/98234" target="_blank">📅 00:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98233">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/98233" target="_blank">📅 00:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98232">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MoX9n6Umlzc5lgrh5cOc-cVAB6ZENU-YmgV5XXvrH4SMnpLykP6D0qzZcJ03EMqCOomkEnep1Y1-OIEqzhMQeM61veSdJdjtZlTcbnod-nUgYEck_vMFTySzVNGl_cFgVCnW2faxj71364c-3CmTpZV7JQOwNs3C4LTqMC1cpf1xIbvIDt-wSe_9y_dcyl45fgEvfNh_58C0UMI808QbWNntWzVJTPuVG12L3mCurQ56nnpMUIkEjhux6YleupyyCApfngECIgWXQGafAphUwso19wq33lNcBrjTOStEP0zFhGZ2cTknchRoE1MzJ91Haz0zf-9Q5kChB6-vVK6Wow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/98232" target="_blank">📅 00:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98231">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بریم سراغ فرانسه و پاراگوئه</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/98231" target="_blank">📅 00:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98229">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/px-sNnHYNQOe7IgeedHFfY9dVvR4WX55yyjb-UwvmdLAGxUykjHLPlZvT1xdmykmuYoDMGJi0VYULSwZBbL4hxeE7uG3rp0uGGhJL_dR1YYJzP2H5Kly2HDWqDmGJWlHIUH62ZTZufCe-va8Pr8WD89qbWd3uPb-DXEwndxjUNcmsuOqK3XMX35L-NTHuyLU6eoVFxBiaTURC88QYtFUqygftOlPBv4dQ0CZuH24G_J2IZvdsmt8-_nMXlyq1YSJ-RkhwBnkbG7bBHeSE3AyBFKpGiZ-B6PWHAkPm6up8yXobWjc8IUel48ilSZBNKCppSncpiaPBc4xHLr5V_NODA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0fENN8bzoFSkuUKRWMFYpjrokZDu_hKKsmyxzWTH2GlpUIoUDOSVFfj1eVy3r3DqDcr8f_-NDrQKfcEh6WX9tPWsspWJH10Dc2XtzfnMXDn1jFrOBj67rj4Pxp-kbKnRngo2xZgQC1uN8Ao_ED-S4Iarp4hHxtCrlndjqjnQptiQzoENYJOj9InUSnd3q-NMjVw5lVgK7VQjWCVZ3ovVl1OoLoCUpuuGLPCKX5B5O1SVhvQu-pgD22ENa77Fh9KLRSSa0hCSGd9SL1u9p_JW97DRAGD1coHHZMUq2Cxgi-Rjqwq7JSYebIM9EJcvkWvx4s7XJl5myalmTta8VzEdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مراسمی قبل از شروع مسابقه به مناسبت سالگرد استقلال آمریکا‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/98229" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98228">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QydzFA6HFTwJ5qjhHwEApYucKRpMCONDYlH_uV67i_-HOSvhOzUFGN2xzgpRVjrFbQKUG3yOvmba5qzso4zBrSLwY1MwYiXDxSVyFgdJTd1uDnFPAKE9e0D7tlceKmc6lSASwOKkcI7W36whPgIvfDdx954LHV8_Gp_H2hgrgNipq5zHb2dDlKDNaIalAjAuTo8yCR7ZzL0Hsxdfdg5fARaNnSQQOTi-4ww68ZtvhUeTePl0qiNrPqcKKITlthG_pqb3Rdrr9nm2zL_iWooAW8-CWW1g0Mu3w1z5ijSsJOzBXsyM68GNMzPDM-GYq-d5zf7-BwDgZY55j7USZV_y6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلاتان امشب با این استایل رفته برنامه فاکس اسپورت؛ کارگردان لاشیم یه دیس قوی بهش داده و تو زیر‌نویس برنامه نوشته: زلاتان ابراهیموویچ - 0 گل زده در جام جهانی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/98228" target="_blank">📅 00:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98227">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kszl6Umw6ria4_EyrRUcl1KmYPGQ2jVsCTwuwKTUDHBbvv4-J5z789MLtwFWgMexvQqQfd0Oo5u63UAqv4sh-81mE0r7KGCeJM0yXEwk6wYWIjDdYFLnb8zxatRkTnnnmS0-xjo4XvYx1TaZUxTui37kfhrIPKC2gRxH4otRbRh5g2jIUOcfZSuZC_Pjnl9cQyX6moERuFSfuUyiQJbpOGHibC6DAz8srHU7DXzXBd8kEI7qzuudlx0PKcJ8hueDVjbu1ngxhannQ4UBbKBGoikKFWZrCuJ3SaAdDnCL2JR_4mjSX9Kewwn0ZtGA33lreXDWKaSE_EcUc6Z7jc-m8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دماسنج‌های داخل استادیوم محل بازی فرانسه و پاراگوئه عدد 140 درجه فارنهایت رو نشون میدن که معادل 60 درجه سانتی‌گراده!
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/98227" target="_blank">📅 00:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98226">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qirishs0wukp0yWKz6G1opFDT79Ba1Mmp1ZOoRZB-NYjmFRMzFMeJ6Xk2GAj6gA_Damg8x1_oyaPmDm16siLBWU8ro3crS5GWzpLPZpLAOXHFl1vn0czDTTbnpKPW-eENhtNuja5yxRfbaHGxUWnSrCVvyafZQYSKkAAzoACklwT1gVfnqn7assBxk88YT4uljc9Y1C39fRz0MRAlXsgjYJojqdMkBF1tbALKQogg-to-2heh9yMr5xFewNO-o1ZfQoBJCPSUqVTR3bodjOxY4EYIZEtCiQ_mi2zPf1lkcCMVR8uNHFK7S3M6hzHFeUOT6W40jp9hKYPkUl3DtblwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دماسنج‌های داخل استادیوم محل بازی فرانسه و پاراگوئه عدد 140 درجه فارنهایت رو نشون میدن که معادل 60 درجه سانتی‌گراده!
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/98226" target="_blank">📅 23:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98224">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmJ4EyDQvT2NEsJ1c1Rq4L5C9c9HaQC8o0Q7l5ajjkjATe5afDcfcu8Oqo3Y_v_UODwBuT2wqLZdFn5e3-h6tXOdUoYCHKNfCGLva3xDpTOcDLFwnRoYy0Z771Fxy8-ILyudRMgMxLHyAqacMMnM42gfYL1SSlCQGTkDzQzRGErztJn1zX5A1ie_tskPKAtkkLxuSiCjOC-Jx9bfBYWS2NwYrAHfJzX1iSlfj4ceXAkWyK7qc7egI0tPwTWmzqP1cWvyURTwKp1WBKYV8qtlmijUI2cOGL3XQ05c1VBaKnDjPbiiHugmka8TFSGI2bv88H3qeJ_sPL0UxuG-FdioSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیسه به این شکل وارد استادیوم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/98224" target="_blank">📅 23:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98222">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hm91RdOavZgfctHFr7okTrjfkMe2IbK7CPinefCZc9lGhO7jFauth7nWvea0SRnmGPF9ihvcEhuxSAXwAxGBwBwxCUqK-tRZavyO7m70YKUYvz2iBsDg5Oc0Tq93dU6Fz6OyTiZSyMb4z6AitjDrfvBv3RhJ4mNM0xQmS76uhs4esMFt-JJA_WaXh9sCWYTsEaWF0PnVo-kFUyq5j_MKXWDGXbLWx0v2DT94M6_deqZ9TSBhKSyHzPfb6o8yD15iiI1Y2lLW43LtcriP0E6_jlT4yPQlZwTf3vTCNBsdBUcZPrZBZ5oUfynWPQbhi9ZWxweFeDk62l9gII_WMe5Ihg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBMmdq4V3ErREBZrYtleRzNFVKWGpz2e_10dgGeeLyGljVDfDJSOkbVys6qIfjhMQLkLtzqVDde2r5ES_JMNSDqY0akYfmGMa7lun04TzehbYqVjkErm-X398ZnPJeYExNlls5cWTCmqJAHm_HjvHgSfCuf1Bmi5wwIR4SSRDRLmCThCPnJmoNlRpffEgI6zKXhEIzFijFBKrnGPFKgJZvtHI0LpLYG1lXe_m-VKIuDabIy67lJE4nXK2mDabBuPlFTVnH2sLDiPwFRZ9m0jiDE3RfchUgLYo43QmR1FMr_yFA20nYO0C2-MB3QpfCTYCZ315zfTDR-i-OJbhNU40g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇵🇾
🇫🇷
ترکیب دو تیم فرانسه و پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/98222" target="_blank">📅 23:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98221">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ao0dSTE02chF1bV9rUcmfvaNADufxm5mg6zOSl4_XPivpcJYYrHgbmn9eNv_ENxQ0CiC1XR0glqZjxbdLWAL_6o_mZQOkXU1WUJvcqv1Kn9okRCrHhDzv1QAplx6PwuC7VIaEKFs9rcABmCcYRPlN_JjGz0T21ZVo-U8S5r9jE5fKjRTW90Mbp9eSZdDKPuqJO5BXXpadkWh4-sdkbVRS_eadE8jRC9vbo_JOHrrkfpl4ZLdKvAtUhp2Nd0lPJqnpJ1ppm5t7pHg7Pg7yJgK6R_9yMGNMrT6M0-XtK6j1o27ikAX3mCvOKYyA5PKEc3eGu12kKkBAsRZHjMFLBgChg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🏆
اشرف حکیمی با ۳ پاس گل و ایجاد ۱۵ موقعیت، بیشترین تعداد پاس گل و موقعیت ایجاد شده را در بین تمام مدافعان در جام جهانی تا به امروز داشته است.
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/98221" target="_blank">📅 23:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98220">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwVlw3nzi9040asIQeOOJqXBNATIXBndOCHAmBPgRZBNfk6AAPrWIiTCOJLNxECpPJj5SoK8ZGb6BqJhIslWqhPjxvbsxcterPGuN2TNbxgE0vFGuLzcxzNjPJnO_AICQ2RUS1i-GxvIdATo92JrxrXkxFsVuiP0xyZY-6eNvK_WziUe2hdjrv6YwMkSS0EAXULla0wCS8DNvGb_JuYFfgX4smjEulKzWXU5_lt29Qz3CQIPIbCW6Jp8lQCJ9SC7k3qFWcCRd4N555fR1BlQIlx89bU_XMV5uT7OzI_X8t-n9-6jFuqnNuwPZl5bzNDKhZgHmEbIMnqME-5EHQSBTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بردن مراکش کار هر تیمی نیست.
😏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/98220" target="_blank">📅 22:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98219">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iemn-uUkakVwkPhJ3PI5jTAg4QQ6tTk2RXYXl3zFxOE552r6dtYd26ffKzaDLXJXHBVbRg5e2pbt24ur1oPi0MbAstICBKABsrJ8bIPZOGAeOTZgs1oP4yTnwiGLg96Zst8kjQs1yRlUBXOPoG9W59r845g032nClF3RZWYPJPnCwBcuaTAy1yNpHmSAV-t9SlzQw1ygqeowbB707prUZ0o_Pbzavd-mpTm8dDw9GyOAxMuXr42HT-6MBumVOZyBRnraKDnEO6MYxRRbdYKXGeQX_Iqfs204SxW2ogRZgaJ66QyFFZnonP_-AWZFykkF8JwoSvQaHp4dEf7YAen0LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
یاسین بونو، نخستین دروازه‌بان عرب در تاریخ جام جهانی است که در 5 بازی متوالی دروازه‌اش را بسته نگه داشته است.
‏
🧤
بدون گل مقابل کرواسی
‏
🧤
بدون گل مقابل اسپانیا
‏
🧤
بدون گل مقابل پرتغال
‏
🧤
بدون گل مقابل اسکاتلند
‏
🧤
بدون گل مقابل کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/98219" target="_blank">📅 22:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98218">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
📊
|| بیشترین پاس‌گل در جام جهانی 2026:  ‏5 پاس گل -
🇫🇷
مایکل اولیسه ‏4 پاس گل -
🇧🇷
برونو گیمارش ‏4 پاس گل —
🇲🇦
براهیم دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/98218" target="_blank">📅 22:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98217">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTcZAw9fWkrjgdjsjBGf2MhjYXy4vwVBXdaxTuZrLVWizmSM-GpnkKmuHetHwAuKYssBU98X5XuKGHgl4AgG4cLxHgIvFFPI9U0qbD_OoGHnjZ0pMOGQy-VEasISIByLk63-gNJ0wWBwkeC-42PiSnuME2p85h4KH2SG8_p9LFbSffZc5v51UkYg_7QRvY6TnmUJzQYvhjAQbet71q-ZMRRX-4kfrD7TSQr4cDmp3mcQxEsvNVDGb3WrcaHl96oQpVtBkwwFUaW3n8iRrRDXbsUXvOCGMG_4dFTEArQWQh7jrRvUbjTkDR2BehAMW8JbMBBnRxdILf6M7AIo6VEUeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
عزالدین اوناحی:
ما تمام تلاش خود را برای رسیدن به مرحله یک‌چهارم نهایی انجام دادیم. هواداران مراکشی در اینجا اقلیت بودند، اما به ما قدرت دادند. این پیروزی را به کشورم تقدیم میکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/98217" target="_blank">📅 22:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98216">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVs5bR-uSZr8stoyTf2z5SSXqeOGvSn6kezZeRcOWcDfh2FR6kDBguBUZyerG1trWnuNQgHms0JB7wa6HzbvUdfGrO4OshuAYyPVw3mPuka_xxCqV-MntT9sVl0WzEuAZBMkl0XVfgfMu1sIVe_1l54j9m4Sw3CJkWGWEreOpfPx5T0lW8PcJwQcom4_JrAsEAhQ7_r0_onPJCNP6EEOntuDE7iiHGMtHvYJYHJlQV1KIQHulq6FtAYIvYBo7fCNp1uVI24QU_qoQ35hYAimHqd-SZhf3Nj7Jt8e2aOGF8Cs8sU94lTxMF5QIk6IDUtOdm4FwvwDenD1I_6WriOhoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
|
| بیشترین پاس‌گل در جام جهانی 2026:
‏5 پاس گل -
🇫🇷
مایکل اولیسه
‏4 پاس گل -
🇧🇷
برونو گیمارش
‏4 پاس گل —
🇲🇦
براهیم دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/98216" target="_blank">📅 22:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98215">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoHK9w7eZZsScoPAjGPq_R6Jy8PinxR7KTP8hSPk6hg0dolkHJw0GJ77e0wJzqBtlmQH8ZjQUgO5lV-2eorjaMfp3E13I5k8gH-efKG9Q4Ptwa0rSB5r1p6bTqVAqlKZpnkcW6AVEJW6W7kwsFU5S6kaulzsGx_LU0tH-HcAdVGlvuzfz-bVEFVFUtEw-Tg3JCytOw_dEbY5_tuN3ZDFwsgutDZoGY5fKMPZMfJYHXES-LlPOz2q_xUZcWOjLSin3NnE8IV2ycR63nuRI4zOY1nXjF-_0hbYI-5efRBz0YJyebebVfCikTCp9AEkJkmbvqKjGNTG3YkE0-SfFSq9zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بیشترین تعداد گل‌های زده توسط تیم‌های عربی در جام جهانی:
30 گل —
🇲🇦
مراکش
💎
18 گل —
🇩🇿
الجزایر
16 گل —
🇹🇳
تونس
16 گل —
🇸🇦
عربستان سعودی
11 گل —
🇪🇬
مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/98215" target="_blank">📅 22:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98214">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AC3CNN6L84WL_pCQfafEGsr5sT6CHOUf6NcYJAUIDOaHn2QGPpTWCA9LOgU28g_zwcCoNa_M2oO6jod72YDZJMAKA9ADleg8zUvmZRxDTeEydPV_XEBIKQpWXwrhwrYBYZ2Q63ddPFGzKLMS5-HklTi0WiUgLdrwrlPqSsz_uNqETgHTWKdNMORRH-6IOQbyovSOyoPTZLQFr5d-WAdPiojyXneb-dolupwBf6USfcYVXtEM5yXKEHFpaYDUUUJ80ktsr_hqmcmG0kg0ht6HqErDIu-qByLxPc5pOJe8D2cAhyRJ7FgZW66PYwvp2nmOWEslA3e6Q1FszZ0ejEcCng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
تیم ملی مراکش، نخستین تیم آفریقایی و عربی در تاریخ است که در دو دوره مختلف از جام جهانی، به مرحله یک‌چهارم نهایی صعود کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/98214" target="_blank">📅 22:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98213">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8-3fiFzpmLzecII-HVikQmTYY7VY_wNn1Cjoh5xraLT0M9yD0tLpuddlIQ7xMc0xAU4zykxEEsf1m03cf1BRku5lOH5oFbE42DdqAlhSMC5ksr7ButtMvauYcMxlwoYiPi66gdg7047ltiQtyc2ST5ntBRMXyzmYC0pU9cE8horRvUyV6B-daqU7PEeKMhqKihpXFwSY0YkRdSnyEGEI3P-qHJtWdIuRYYxPU52zub6gxzQHqPTnMDq8PfCCd9HcqvmFqf7_NAg7UUHA9_QyggHw_5xw8jWe1wqgzXVQoVR-knyXMAzwrNw5cKEZ5pNBJ1cj58NPKRdB2BaPw_R6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
عزالدین اوناهی مقابل کانادا:
۲ گل
۱ موقعیت عالی ایجاد شده
۱ پاس کلیدی
۲ شوت
۲/۳ دریبل موفق
۳ مشارکت دفاعی
۳ دفع توپ
۶/۱۰ دوئل زمینی برنده شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/98213" target="_blank">📅 22:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98212">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود مقتدرانه مراکش؛ شیرهای اطلس همچنان در مسیر تاریخ‌سازی!
🇲🇦
مراکش
😆
-
😏
کانادا
🇨🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/98212" target="_blank">📅 22:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98211">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_DwEeeno0WdNBBVrQ9u4qF8pd8WIsZ66LQwijmYv63_X6yLdbutor8iWGm5RBnaGHQ6Z1P2o0Fr3wdW7VgZNaHt3h_wEUM4gze4aCUiYLTHf-5XXOXRH8F_3tn-_EhledPYC1hnaNtpUV0wRrNY4lD3ixmtSVJnDtZc5amoE9YBp5Q4eb9T8U-6Qhd7ohmQF0PQYZ323te9z28hHYmyGwCHynIeKPPtGj_-D8YINcbmEMSbO7I676ltjS-H5VKN1sXzhPcR92whyxtv_BdO2xkc4FkO4FQmPmoFWq07U9Cjb4oi5ZEenrB7jpnnYtUCQsKRd0kBH65IyEnzZY3oug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود مقتدرانه مراکش؛ شیرهای اطلس همچنان در مسیر تاریخ‌سازی!
🇲🇦
مراکش
😆
-
😏
کانادا
🇨🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/98211" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98210">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d14181bcb.mp4?token=gITCgoT939VopVPoLsOrymBV5dJ6yecPBh0clC4Z8sJszQlPDESrEhEnaxvlAvyUzySNKZzKJNCcGoNm6omqw9WKJg4ouw7d2Pv_Uxjo2SOz6LFYg42jYmCttvRuYHVUQjgN9V0l1DzN8KUjb4_Tu5J2yrj15ODQ4MRZ0uBrh4XP0K3gFP8S476Kp2dBZJ8Ureg-dRFecRG4eleoxJbx0gCTYJ2FPTCSl_5diaiy5vn05HjpToO0vlCInrtt6-K7EImelSQOhxGp4lsm4eidq0ScAwpmT0hwN_innbUrIJZNo1jQO9tlWTfoRW9tQ5Iw6FCtPuMvDs3Xg8syED_yDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d14181bcb.mp4?token=gITCgoT939VopVPoLsOrymBV5dJ6yecPBh0clC4Z8sJszQlPDESrEhEnaxvlAvyUzySNKZzKJNCcGoNm6omqw9WKJg4ouw7d2Pv_Uxjo2SOz6LFYg42jYmCttvRuYHVUQjgN9V0l1DzN8KUjb4_Tu5J2yrj15ODQ4MRZ0uBrh4XP0K3gFP8S476Kp2dBZJ8Ureg-dRFecRG4eleoxJbx0gCTYJ2FPTCSl_5diaiy5vn05HjpToO0vlCInrtt6-K7EImelSQOhxGp4lsm4eidq0ScAwpmT0hwN_innbUrIJZNo1jQO9tlWTfoRW9tQ5Iw6FCtPuMvDs3Xg8syED_yDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
گل سوم مراکش توسط صوفیان رحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/98210" target="_blank">📅 22:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98209">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گلللللللللللل سوم مراکشش صوفیان رحیمیی</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/98209" target="_blank">📅 22:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98208">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2CFsFniMc5zP0CX7VGhRLCsifdBSIlIkbKuPqPZ_53ozKZ54ZyZxu3gxtRqIE02Qc_g7nYB4pVJGlAKchjkWozZD7gP5c-FqD9xXwbIribuBzPFlZMklrMEJMTFAf5PPjT1-I1fiZ0e9SuXHOXVYoMkxocPxaj7BEuSnufKebKmILdR0lwrbauKUqwTdjfe86zXLwQjtEBFFCQjPaB-b5tec8GaWCQJpVbo1I7jxbfbiGqIKIouoPIPuiAgRDFC9LhZTNu3nkeVP5nuTosyhkvhvsgIOBPiJ9bsZuNeM6rngbsaoHpUbPymtQeTImOze1AQ-WvSXqYfkKpJFb6Gtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانوان عزیز مراکشی خوشحالن منم خوشحالم
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98208" target="_blank">📅 22:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98207">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9a15c420ea.mp4?token=uronvJJcfT2g18xxv2kfufovC0XYycSc4AdybwvyZ5sBHMN8TJo89-6wIEZsDUrcYkncycz8bczt3qF9Int9lrVCeskjJ0tGVm_GaAC-aQiWhWOy0y6VTfHTzo3zLULGVImzlvGA-55Dm2amWAFTqPEpGMc0kv4KFzDzJhmRK602QL_XBzIXxJbG_MvtqMnpyrETjwSeq5F8Rysa1MHnOFQOo_d5CqwGkZAqLvbGxfBmlcEZmwUGiF99mjK5GOC2jNck9AIo169H40JvPhQEqfSphxnZwmi_N4lAPz2m1-RHWBkjtc9aUwMINqwo6ko-j-eA5U-7LxF9WZT2n6T58g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9a15c420ea.mp4?token=uronvJJcfT2g18xxv2kfufovC0XYycSc4AdybwvyZ5sBHMN8TJo89-6wIEZsDUrcYkncycz8bczt3qF9Int9lrVCeskjJ0tGVm_GaAC-aQiWhWOy0y6VTfHTzo3zLULGVImzlvGA-55Dm2amWAFTqPEpGMc0kv4KFzDzJhmRK602QL_XBzIXxJbG_MvtqMnpyrETjwSeq5F8Rysa1MHnOFQOo_d5CqwGkZAqLvbGxfBmlcEZmwUGiF99mjK5GOC2jNck9AIo169H40JvPhQEqfSphxnZwmi_N4lAPz2m1-RHWBkjtc9aUwMINqwo6ko-j-eA5U-7LxF9WZT2n6T58g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
گل دوم مراکش دبل اوناحی با پاس دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/98207" target="_blank">📅 22:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98206">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گلللللللللللل دوم مراکش اوناحیییی</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/98206" target="_blank">📅 22:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98205">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBN-GYr8akBNkRtj0TcvDuLQg84uHlQ2fjuMABu_GDa4qcMsEIE_ft4AfegEuZqSJCqDRLwdjfPRVajiCrTiHAwVyTmTLlN77u9LTAJlU-e02rkZXphhkKRUyykHlR7kFNIhiocWZK0l-XhWMxdmcH1tAe3bvBkF8UNcOGUYW0Um51dRef2gdpTBpcPpoj7BDh7mNzuD4hSnrtfVoJijTTF2F4XcooOHIhTo5SCe2xU0VgQ5Jsz3TOtU9mIdwrs3XRTgIKEF1KpKNarailsJWguy7dlKA04YiIugkOhSffjPiYeH2P2GmjzN32fVAVWaJhXgLZeiMuk1Td56pKIHEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل موی جدید رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/98205" target="_blank">📅 22:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98204">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/98204" target="_blank">📅 22:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98203">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KFVEf2kTNHrxh3VXBhEircEamSnnIiiyHZ-PyvZRveA7l4qmdstqHWvoBJ3uHmSMl-NV-lv6k5Dvz-JJ-GtuwJINPBFN55I-LnjvO3EIICUtcuErta6KZ9YNKZeKT8qm0LMbVQblgxfxk9I9ZFIZDlX75T89UI-53sAtGV7hda_63YSZO0M0QMnPGjdUsmUhC9EtYzsM3Au4dyLyzZJyRSnIrbI02heNoiXegjgGzGsFxCyCOPxLzbcwUpheNKmxlFdsrd_DRDZz4MlN6ArdvOcvE99LxUwEeEsayehTLZbyJ_90SrX-aqaHC0xfhMYMFBayywbHLcmwaT8oPjJwjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/98203" target="_blank">📅 22:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98202">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79bed95c4a.mp4?token=olNqH0YX1J5bVdQ3nlE_Lm9tRgV-mS_ucYVITb0X8kXCvn8PkOcCBfu6d4mWkchQ2pmKLZq4nWNaIeRcWpjHyZZ3n1zplAzv4vLZ-9iY5MFSvSNXWlSbEDYkorPhtZy9K46hbe4Sa5ZLaiYaxTfjY3JtGC-1pYB1NsRT6HozdgE4oM-c5RYw4Ll5Kvc7OU69vJu5H7HucfPIxyPBSysBXUtZryApVWeE-nPvbZ4HWnl3PqEJzsTE4FIPwO2dudvs38POgEEJWuVp4soTMjnBRrD5w07Q7WPLLV6pj5eCNBF3l8R0zmR-mkCtohNKF8lAeoXBJd1blFr1wuv9YLklFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79bed95c4a.mp4?token=olNqH0YX1J5bVdQ3nlE_Lm9tRgV-mS_ucYVITb0X8kXCvn8PkOcCBfu6d4mWkchQ2pmKLZq4nWNaIeRcWpjHyZZ3n1zplAzv4vLZ-9iY5MFSvSNXWlSbEDYkorPhtZy9K46hbe4Sa5ZLaiYaxTfjY3JtGC-1pYB1NsRT6HozdgE4oM-c5RYw4Ll5Kvc7OU69vJu5H7HucfPIxyPBSysBXUtZryApVWeE-nPvbZ4HWnl3PqEJzsTE4FIPwO2dudvs38POgEEJWuVp4soTMjnBRrD5w07Q7WPLLV6pj5eCNBF3l8R0zmR-mkCtohNKF8lAeoXBJd1blFr1wuv9YLklFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول مراکش به کانادا توسط اوناحی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/98202" target="_blank">📅 21:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98200">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مراکش اولی رو زددد</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/98200" target="_blank">📅 21:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98199">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/98199" target="_blank">📅 21:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98198">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بریم سراغ نیمه دوم</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/98198" target="_blank">📅 21:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98197">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTnJxc8sK7ddImIaaXCdzcWN5rbknfeuYsEq-2fBeAeBvvA_d1BrpROSR36HabX7NrboC8Pf2B3nN3JyYOA7lX1A5Xs-s-Z1q-QaQ5ztwbHlABGJoSNKNOJuupjOi5sGqwxgLela_ULVgUmW2ZVvxhnX3DeY_G2fy2wobzDO7bLT5yzcYDq2mxr-ClyJqoboElFEQzD7D9FSuxzmO1oaW-TWluMT7xRJxzz2pOBIvK7Ky8XXM76Aja-nZSKFZcKwWQMPak2NO2LdZpjJCZk3_HKzvgAAsB-0A17bN7utmj2Y502y7g0Mt9DWhXbG0d9nCafVZUjAqaiWNgjBtSn2TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول بازی مراکش-کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/98197" target="_blank">📅 21:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98196">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMapAmeLdxRxktHcUHUpOxEHJuUo7xay0Pz-NnQ6Wc092cP1znxHBEQsGce6C9hyrDmgfuVaRNvobJ9aXtoSeFmi0PeD-2Se6Zpc7g6GgFVBnLcScexsEmDuycWJbZFawm4bC2wibtHtOK44FpMP5TlRQzsC95qVoYiqThAW6KU_DFtG9fQ4_7GQ23Nqw2t0A6KNadRjwQteieBBbjmZ91WN2j2uiLlQotmxwTXgNStS96_7Tc5VN3MpUoIkJdHo7FyhWSdVb4Usc1bQ60Yid7fhTTwMfKNjzaP_H25Eu8Y4eFc-KOeqwMpOL-grDF4706EfQbY3dNUtsihGuKkIiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی اینفانتینو هم دیگه خسته شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/98196" target="_blank">📅 21:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98195">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پایان نیمه اول؛ کانادا 0 مراکش 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/98195" target="_blank">📅 21:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98194">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZpcKQMjK36bxyrn-b8Hxb1gcmCd0axB5Y3jMKEZC3s8L09z-nXBu-SKIUcTc-MMRYUTx8J6Spj-FQPtvWjkBFLDw10umqQNf29JrZ_Wtkfcy754FEptKAWZuczOX4VSJVhPcL7iTOz8oefXQGnwtl8Tc91Yhoz6LTXETOEWIxXSwxxdxL6RpPwGDasgWnHFSdNWl_v2GaTKLk9FToZnrpKe2eBK99upYAKIKKdHvth0a5Xn5k3lZKTIJ-PLsacHsDWj-2V5tMbn0iCD3ywBZ1ls0GmXTcA3Y-9DLuRlW8fv3ywenzRemzuZlwhHwkuD8zycZev_B7NN7TkZ_Na8tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایباری مصدوم شد، صوفیان رحیمی جاش اومد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/98194" target="_blank">📅 20:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98193">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7vx0Zo-kb983UKpzgceOSo92DeGvkweHmorxfVcDIKoKZOOr785PicCJZe1MgE7x7-wdXwIQWL2cdZI-t_idSbBQKnXR4x_dzeRh-23i3WtTAyYONekQ_-aEMZmK01nwjpuYa0SWPuBcAANyup5JfY4gFtbuJkWCQ6_wnkTotBVRaZmPl0ICR0gny2uDRSGhysKvrE7f0Feg7oprL-lTvKSgNDBbWZwSxC9pj41nx0sMmtiAPF4oga11fXo2N7zWObnx8Uui0ZbuhrfeUOoxGn50OCNJeeHjsPAlXEcwommmm3tZrH--7eIeR_pspHFu3JgH3S0JHuLWIyz4q2wNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون همیشگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/98193" target="_blank">📅 20:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98192">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhQW48Npu-tnTMpHegHVkvtNqzKoUoogd03HCixFdFgN1Y3Lvt0axG0HOPqlbdOVhXSGds1Z5gP_9hIIByAScC0xWfA5QWiJYT9KMzzXFabJkZOutqyeHOUVyTGXydS29BOLAUqMK0Q23uTUBeBGSymkOd7G8hzCALBfvOB7tmmKhqXJBqMbO2z3xL8zNqhfo6CnmkUG5o9ZIfnmqOsw1NsfMxZ7fdnf-wufTl8sD0zbF89XB-D3K0fTpieUKx4JzVcwRy23-rNlA--wRMsdY-TP2zm6_h1mrYvlMwYI_L0nfhI9m0S8C1z-UH9REtjH3J6t1woDsng6Dx2Nh2LrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گلریه این یاسین بونو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98192" target="_blank">📅 20:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98191">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سوپپپر سیو‌ بونو</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/98191" target="_blank">📅 20:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98190">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">شروع بازی کانادا و مراکش</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/98190" target="_blank">📅 20:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98189">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🇹🇳
فدراسیون فوتبال تونس از انتصاب هروه رنار به عنوان سرمربی این کشور تا پایان جام جهانی خبر داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98189" target="_blank">📅 20:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98188">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqJcsLSA8GHyYgWvQ_omlOzhWzsrkY4Z1El4NEgTaboAVQPnvHwuMaoPQ8-qjbSBL9rbRlvkbV2MRE08BCA5VUrfHvdEhDOqvh-iFtoDjUCzaTZF-iEqk_3BZoR53G1blwLpBYyfb5jRvxcxaQrhCqBVYNF6WXgxNf5jU1cARWxXvQdWm-VU_A0fVd48bHo-A_8PiakRhSdL_LL92kjGhAcNAW-66tQc7amWpDhu5t1_Cn-kYnWW1oEyEMHsU-NioPiIxw00nB3ob5lxoB7fpplQv4PWN8xoFFQl1SqEX7x8PHOfrRwgjqmAPGibM59AJUHVnMzsa8Bn9v_qTflXCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
🇪🇸
آنتونی تیلور داور بازی اسپانیا و پرتغال شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/98188" target="_blank">📅 20:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98187">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InZlv1JfZpigCJwWSPSGvIGSJw5ZtNAahLOQBKRGzqpPCmsLYlGPwYjB0Hf-yTtHTanzx-HbJUV_DE8HKHSVHsl4P_1AU4Eg41eGjTGgiZHuCh6Cj6Ivq0sJbfLOo3Jvy-w6VlUZ7CvVKv6h1C7etN6qaIWA2ys5GJdLSIX1G-OZzdYIt14uQXmQ9NaLDHu4Q2DjDcSxbFVoEmztj2TReULfvwwPoYvY9M0GjUjF17rqXEj9FZruRpDmrMgwnnQpJCTBdc6Q9igHeRchMtYtqZNOWo_6mgxhkkRvnAQK7VzZ-7fW8WZRCq2ox_PoxelZYURowIUKt8u1rSgUUnB_eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
پدری، هافبک تیم ملی اسپانیا و زیدش، الکساندرا دورتا، عکس‌های جدیدی از کوه لی در لس‌آنجلس منتشر کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/98187" target="_blank">📅 20:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98186">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVFOOzTEsMzYSvWfy1SKkXbmLJNKuimxdBuDn7Jw8d5Ii7sIG2S3qm9Nf1Jd_z-4tdvLjZQC1iEEDFo_H6Gr3q7oLNuWc3DNVH1jOi7SAvFoKyrDJ-Ros3fNya9uEJXbc9Bx4dYPpsdwiq_d7p4MobVTUxyWlzHO5-eaAVQa4Zb2MbK8hLwOofKZ604wfBqJzi1qQorQFF0wc8YgBgh03rniPbZWWP7L1OM1kdCGkyfEBwe1bzvTZ1jkIELKOOzpRucN_Aw-C02M_5aQ7DR-PxAhZw4w5h_iYrWulujA5BdNnZgTvXrz2eGnYuOcBobix6RdYFlNBxq4jmMRVXb3ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
#فوووووری
: بشیکتاش ترکیه با آرسنال برای جذب تروسارد به مبلغ ۱۸ میلیون پوند به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98186" target="_blank">📅 19:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98185">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfViGi4WpwVaMR5b10tYduHz89HAwX0-vHQunFC2kBOT1FZjS0jnd9qf5q9B7KXByiuLRoAz05djbOQDZuv5YtwpbHEjz_aZcUWjQ8_4EW6AflxRxvzJ6bRI-9IFmEdwbCzakoyi6JtmWhpbT3hQijzLex0w-5UWTZrW-LE2CGj4EwViXRXlvJjO7OSako3jiT-zzFLoZQVMNTkvrPAtohYnt3fnZV560qIlIw6AW_0RNgoxxMj5rNHH1XjH3yRwsORgcAOXybsfSBT7VxxSyVAIX2pfklyQTYevUouN-QopEyRv9vnFfUzSMidLfyaMXWgGNEJob_50B2dnfzORMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
— RMC |
🇫🇷
🇵🇾
فدراسیون جهانی فوتبال (فیفا) اعلام کرد که به دلیل شرایط آب و هوایی، احتمال به تعویق افتادن مسابقه بین فرانسه و پاراگوئه وجود دارد.
‏"ما وضعیت آب و هوا را در فیلادلفیا به دقت زیر نظر داریم و در حال حاضر احتمال زیادی وجود دارد که به دلیل شرایط آب و هوایی، این مسابقه به تعویق بیفتد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98185" target="_blank">📅 19:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98184">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4be21116.mp4?token=M0No1A6EM4yTv7BPkTk-3T54T_y_0yvP5o1RNizklyGU1FnFcf-YT2ZiC6Lcs-fxvWJPnzT1--k0e7of90CB1DKUwfhBsvOmSYGAiK2gDF71_yMf6yzDwfByUcwKeLomtbG4pGL57w3JQuHCGIHHkcA4bdRFzAoyUiFudF40m-kiojgzD_5Iw_PTVKCLnweHtbM8DCnyb7E0Nf0HGerjmEqtRxZ4fmuznC43ewipkXBrBGsQS7TUMf0UKtO14r2ODI82v2mmJPFNu40XpRa2WpWAHG8ip-3igk-oohBO_zP2sDQEgJoQMW8y7Qaq4cBuVpFzwYHJEqzwfnTkDxJ1Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4be21116.mp4?token=M0No1A6EM4yTv7BPkTk-3T54T_y_0yvP5o1RNizklyGU1FnFcf-YT2ZiC6Lcs-fxvWJPnzT1--k0e7of90CB1DKUwfhBsvOmSYGAiK2gDF71_yMf6yzDwfByUcwKeLomtbG4pGL57w3JQuHCGIHHkcA4bdRFzAoyUiFudF40m-kiojgzD_5Iw_PTVKCLnweHtbM8DCnyb7E0Nf0HGerjmEqtRxZ4fmuznC43ewipkXBrBGsQS7TUMf0UKtO14r2ODI82v2mmJPFNu40XpRa2WpWAHG8ip-3igk-oohBO_zP2sDQEgJoQMW8y7Qaq4cBuVpFzwYHJEqzwfnTkDxJ1Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
در کمال ناباوری و سرعت، به یک هشتم نهایی جام جهانی رسیدیم!
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/98184" target="_blank">📅 19:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98183">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a342fb6d.mp4?token=rD8J4dGVyl6Prpj3sMoCzXRD6HtK6m1mKh-QQxCyferUNRcUvsgULO0SEeEcmFO6d-CaN59vr2cTZ4d3hjAsuprehxMi_xlXiRRv6xXtPujvoNFg-LkQNBsE-fruw1z1lxQxbZx7dTOP_bFdXjTuNby8O0zEylAk2EmAtxLSkIofLExH7UM60x6qohDL_UIzII35lIfOg2aLucBucXAmpUcI1Xp-LCoEsu7DOg49fdXEvUDHkjbeN165P5OW1D4c1A4-9M1mXUvL37mLeSGN7HBH7naJYlShoWtzo7BQKp_2lvqvfSNbl3QoOnEwnTwMO8Uivr0CznUITlz8l5powkLc8kAvTcObrw6IlTmbUI2IS4iG-RXbCt6XLq-1TqC0l2cb16-UsKUnMUIZSW6zoFhyT-RJd-OyWJA56lsRBzeaR8xz1oa45XWNFOeOuIb21H-vKDLJhF0qqgAusrv8qt9lCt70YA37QXJh8s4p8jjy2Tk-cOIWnp6Ic7XYLDOMlyNd0fmeSMNFIk1RTmFRjU7si_c0a9epnSctHQPFO3qANxKKA2WX0zxfkq3L0MKvqYFlJvyfLG1qUpaPvItsZNCHMpxdV11oUqglFq4HGk3h77-9mnVTaNsJCBqr8FL7m_bQfIqaiONBNnedIBGXX9KAZVCKuReouM34k7WOqxY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a342fb6d.mp4?token=rD8J4dGVyl6Prpj3sMoCzXRD6HtK6m1mKh-QQxCyferUNRcUvsgULO0SEeEcmFO6d-CaN59vr2cTZ4d3hjAsuprehxMi_xlXiRRv6xXtPujvoNFg-LkQNBsE-fruw1z1lxQxbZx7dTOP_bFdXjTuNby8O0zEylAk2EmAtxLSkIofLExH7UM60x6qohDL_UIzII35lIfOg2aLucBucXAmpUcI1Xp-LCoEsu7DOg49fdXEvUDHkjbeN165P5OW1D4c1A4-9M1mXUvL37mLeSGN7HBH7naJYlShoWtzo7BQKp_2lvqvfSNbl3QoOnEwnTwMO8Uivr0CznUITlz8l5powkLc8kAvTcObrw6IlTmbUI2IS4iG-RXbCt6XLq-1TqC0l2cb16-UsKUnMUIZSW6zoFhyT-RJd-OyWJA56lsRBzeaR8xz1oa45XWNFOeOuIb21H-vKDLJhF0qqgAusrv8qt9lCt70YA37QXJh8s4p8jjy2Tk-cOIWnp6Ic7XYLDOMlyNd0fmeSMNFIk1RTmFRjU7si_c0a9epnSctHQPFO3qANxKKA2WX0zxfkq3L0MKvqYFlJvyfLG1qUpaPvItsZNCHMpxdV11oUqglFq4HGk3h77-9mnVTaNsJCBqr8FL7m_bQfIqaiONBNnedIBGXX9KAZVCKuReouM34k7WOqxY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇲🇦
هواداران مراکش در آستانه بازی با کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/98183" target="_blank">📅 19:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98182">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLUqwsOEpMb4Myl_MJY2UxMcV_srEeQZhPr7DP7NkSCJiyosOZJMiNNCnJ0afldANgm3K1ZY6wgT1PLKzNHoyNrm2H94htgaVyWrQsDaoZZ-HHKv64zyV8cAkGcwT-P2UBDvlYkLdyXyyteKWgNUqTvPRGEs2P5a1CLq8b5QcKrsm3uvVQfG5jgjgp2g_lR50dGpRKCXvPd7_IUjJByETbbQt8hEw41TdHNdqEG-NLxXtteGockXqWGIky4N5UW-Ch4qu9bdvcoKJtKUzEtODhgdraLuD5YBTWNXLbS8rd8NvhXd5orY2RsJn4xi2JB4EEXYiM-BU85TjOD0V_VdXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
ترکیب مراکش مقابل کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/98182" target="_blank">📅 18:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98181">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pV4Spo1Ea4uo2Gs7Ahdla8ukGUf1AKCs2nLLNASR1T6RbzcoquxmVGU4SaCOlvkbPAOgdEbo3D8eeAiOLllLpCoBD39iiWocwYMq9PDdalJAGBTkvt_QvuJj6qK1TX1zA2Vbu-KpuPOer1xb9l1aa6b83pM9SawVPDk0qoY8beScgHEh26qeLT9zrMt97Rbl746N5zuLWYqOofh824_hwTP2uQkCX3pb84eVt1tCjNNF6tDYb8yYeJ53CZVc7iihbqWYOnkRsDhYM1V5u99MuVwvzrJ0RzCo_L53bx8e1JVvuEfI8dPG-_cBmBnAa9GSedt0tF2z8kJuQrnd8bcnKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
🇨🇦
ورزشگاه NRG برای دیدار مراکش و کانادا آماده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/98181" target="_blank">📅 18:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98179">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HUx7bNycPHQRcBIke8q_ITxnmY3QaGLBTBKbK92cnrKBqc83hO3Y_-0f8YCFwZ173k-T43Krd6s8izwYFHXY8pSIPSllAQGgJQBrfZ7Tah0pkSB4R-CvlU67_R8S1aAAvwsUBRi33kOQ7iauNi739yCDs8hrl_mofqdDMI6m1vPbUlr2eY_5M_q7Tk9yYdgp2FeXb6BWKcoig_bSJiTFlp_HjGfnYKD8of97s9a5xH7GTeZ4RDM-7wvP-uMimuS5o6aMZnePdHxhp8QJSQ094lotvJ3Z7r25399zv7-gYUMXs5w6q7xqlQolMp5Cr_vRLq2ZsExfd85EhukPoZ_yBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xm8LNpseY8Dl_XrAzWJPsH1VK2UgsxGepzXyaXMhA8NCBemEDPTbITCJOhCLQqRUvKen-TNZrLUPxFyq96nY9dUnbIYYDxdeLEyXPbbj8ociHl3SWSPKFQvSCDXmyF1Q2tgYSMhvIjL-fim99imaSeW0iFgy_YKNaXCV-y9FU8HcLaq_Bh1Xo3klhlbLFOpxYR46Mt959Cal4vCeZOtB3-HNvC2AFwdWOQtvZNQQEQTVK9KCxBDrEBJSluZ68cau7ecoagHFXWt4C2zgj4TuRWzuka-Le3TS_hF6rjkLuNDZmqAXcwemp8DWNcS_quDYLuETFEbjSUjU9XRb2hrxnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
📊
طبق گزارش سایت Score 90:
✅
احتمال پیروزی تیم‌های ملی در هشت بازی مرحله یک‌هشتم نهایی جام جهانی
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98179" target="_blank">📅 18:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98178">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af013992f8.mp4?token=h0sQRWNX17azBu7LRZX6wXDvn-JpXQQIx5EQrIcnrrqBEZ4rMnt0jSwlB-m96zU6RkFuf45Y44FHY7PNc3ty7SrYF46QVs_LNXkxaoyuXmjB3q-RCJL7VAE2wFSGHPbJjL6fk3jbV-2FrN7L4JDXpJYQa931PL55YSYBWh5f1RsHcH5ih9ktXtoWwDWJIZina9gWTyctnUXcUaat0q1cPmth3BaW0ER5OgryHU8RysEGmJtCRj9l4afkPDHCywoRxgkWsd_Td43k8cgOMP8E2qZSGKlAJcXD_zNF-8BVz9gAyVj7oxiXKPs3an1fdN0u9WrrUUVmFs8wM_ZKAD-hbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af013992f8.mp4?token=h0sQRWNX17azBu7LRZX6wXDvn-JpXQQIx5EQrIcnrrqBEZ4rMnt0jSwlB-m96zU6RkFuf45Y44FHY7PNc3ty7SrYF46QVs_LNXkxaoyuXmjB3q-RCJL7VAE2wFSGHPbJjL6fk3jbV-2FrN7L4JDXpJYQa931PL55YSYBWh5f1RsHcH5ih9ktXtoWwDWJIZina9gWTyctnUXcUaat0q1cPmth3BaW0ER5OgryHU8RysEGmJtCRj9l4afkPDHCywoRxgkWsd_Td43k8cgOMP8E2qZSGKlAJcXD_zNF-8BVz9gAyVj7oxiXKPs3an1fdN0u9WrrUUVmFs8wM_ZKAD-hbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهرداد صدیقیان: چون رو جورجینا کراش دارم دلم میخواد پرتغال قهرمان جهان بشه
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/98178" target="_blank">📅 18:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98177">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🙂
🏆
🇪🇬
شادی سم محمد صلاح بعد بازی دیشب و صعود به مرحله ⅛نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98177" target="_blank">📅 18:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98176">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNnTuQzQO1_tJDwj2tWHJ4FbafD3itc-djOub8N8xciBiJYrw3G3gLw0bAk80f4-Bu6koPgWk2t3Xof0s1NruHWplwIQ_SBAzndlUO-peTCdf3skBrggDJ8YC1o-5DSQia1lGnFni8oNQuOZVd5rS_0FVKCpkEyCLZ-AkRqrPqz9Zp5iSgdgI5EoQulQF7ldVCJgQpvxpM3BDRBwX-Dyss7UtBqoh1ZFsfiu829z2K-Rniv0oe9Oir5HYNqQUrp1c-SgcUb-6o2wl18lQg5pAeL3QEuDXBw-_V5AU5j0J-ZESk9ZiTASBaJ1MmMKdO_YJ-l2dt9Hb_lTwcUFr1kzFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
میگل سرانو:
باشگاه رئال مادرید اعلام کرده که منابع مالی نامحدودی نداره و انزو فرناندز، هدف مورد نظر رئیس باشگاه نیست. فلورنتینو پِرز، قصد داره یک معامله بزرگ و مهم در سطح جهانی انجام بده و معتقده که اولیسه نامیه که باید به این تیم اضافه بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98176" target="_blank">📅 18:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98175">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
😐
مهرداد صدیقیان بازیگر سینما میگه تونستم مخ دختر مایکل اوون ستاره سابق فوتبال و برنده توپ‌طلا رو بزنم و حتی برام هدیه آورده
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98175" target="_blank">📅 18:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98174">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccWk-9cZ7jPhKztv-hgnB_KKmubEPWaXIhDgX9cYV5vLvTdSZOmJ6KrM0TNyR4U9uC_YNIDTUfiiQRkPEs5BaRX90YsAIrJLXoIXZ-FJEhVY0aJ7N5OPdR5RHYJ8ROEE9ONqohhq7oD9P1kNi0bXSb8CHPutmftfgXev4mb5vOe_khjbRIkkPBbbiiJpapdfvSoV9z41cT3aaOQ_5SXS5IaSpbNjncN2yYHX0jl-s5TpoqYRF2f8aQp1gmeyy3NTy3ocBy7qWBNVo4Mi_GeKydRRPgjFwtQ8Ona5SJnDBOU3AuYx-xJ0iCFbGZBRSW6N8HBPP1I8aoq3oRHE3HAizQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇭🇷
اظهارات فوزینیا، دروازه‌بان تیم ملی کیپ‌ورد، درباره مسی:
‏" به او نزدیک شدم و حتی فرصت نکردم زیاد حرف بزنم، اما او بلافاصله به من دست داد و گفت:
‏' عالی بودی. تو یک دروازه‌بان فوق‌العاده هستی. حتماً مردم کشورت به داشتن تو خیلی افتخار می‌کنند.'
‏ شنیدن چنین حرف‌هایی از کسی مثل لئو برای من خیلی ارزشمند بود. از او تشکر کردم و گفتم: ' ممنونم، لئو، تو بهترین هستی.'
‏ سپس از او خواستم پیراهن بازی‌اش را به من بدهد، و او لبخند زد و گفت:
‏' حتماً، آن را به شما در راهرو اتاق‌های رخت می‌رسانم.'
‏ این لحظات را تا پایان عمرم به یاد خواهم داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/98174" target="_blank">📅 17:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98173">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👀
▶️
🇨🇻
کشور زیبای کیپ‌ورد که علاوه بر فوتبال جذابش، این جاذبه‌های دیدنی رو هم داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/98173" target="_blank">📅 17:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98172">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a6f3f631a.mp4?token=A_zaNpLPhb4JSevXLh10mr0ukqLv7a9hQfA0h-ZUm2e-gspKbRPrU1mL0s3YWpeij3EBm8l_0UNlXnd_9gKvoZcBO6gXIvxS63SYNGeSbajz4PPakdzQz8ytxM0TfrjOuthSuLwnDoVGhbxfZRp2pcn5drNjRUDJLCTwf9wIVD1_ygbPxFD-pT77oKn2gfBXDtLaNVFGiNKkXWWThvPGaPi_7_h5Kyq1kW-5XQcZVxna9asYgQLtmmQunrVITjmUUyIZF73mRDfDnQT3MkkFGx3Su2bf-Nf1rNDh64f06ztvGWH_6gq_O8ZOeESvMoHJjcAnz7lr9KnWFXQEOi2xoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a6f3f631a.mp4?token=A_zaNpLPhb4JSevXLh10mr0ukqLv7a9hQfA0h-ZUm2e-gspKbRPrU1mL0s3YWpeij3EBm8l_0UNlXnd_9gKvoZcBO6gXIvxS63SYNGeSbajz4PPakdzQz8ytxM0TfrjOuthSuLwnDoVGhbxfZRp2pcn5drNjRUDJLCTwf9wIVD1_ygbPxFD-pT77oKn2gfBXDtLaNVFGiNKkXWWThvPGaPi_7_h5Kyq1kW-5XQcZVxna9asYgQLtmmQunrVITjmUUyIZF73mRDfDnQT3MkkFGx3Su2bf-Nf1rNDh64f06ztvGWH_6gq_O8ZOeESvMoHJjcAnz7lr9KnWFXQEOi2xoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇲🇽
هوادارای خانم انگلیس در آستانه بازی با مکزیک که پسرای مکزیکی‌رو تو خماری گذاشتن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/98172" target="_blank">📅 17:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98171">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8zFYz5FZD98A7QOJx1cy-9hDJNvtkekRwMh6ofRmrQQCy53LLpWHqygQggLJodRFYtev3D_OzxRB5GwB9GgOKOXh9gDEMweid5bnNJfVtGGlqEA15JpGvQT1lr45AXq65QG95BE63_Ks3vmHyP3NXjMrXj4oQCjlIa0IKF0Nom4YIGUljYlMBMimSqNT7S8kx3qYdn2PVtzM_7yY4p4m1KttvDv9ZNtuVCvoFj-QHJ71U6Oa7ZgjrVCdlC82VaV1JyI-wG6qlXG1SVpFZKaWP4He2o2d_xIp20wYZ3Ok9oGr6yC1oANrb6rb-2dLUmwBl_3wyl1d_xt9o8nbDXELw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
⚪️
فوری از آاس:
باشگاه رئال مادرید در این تابستان با هیچ هافبک دیگری قرارداد نخواهد بست. این باشگاه با جذب برناردو سیلوا به عنوان تنها گزینه در این پست، رضایت خواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/98171" target="_blank">📅 17:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98170">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f0c663da9.mp4?token=GoHtZkIse4FSgRB_l6dPM82GYyuWHqGI2aW8yta0DNSMZV5OSe-yWsFmIAFIseQD3ZgLE2Z4ZR3OHz5xIGfAYCNQ2DkyOKb0P3J1HVEzrzIRB1pwsY-ovZKx3Q2gkIA_nNL6ELkfuEtWvyK2uqlLJIkyO-4dm6OsVnLsYvQE44LY3K0ddzpx6akRi9jy-jwRtJEfj0LnNcWkgsqYGmCMMtdS4Q_LikQ5Y_t26frQkHX6x6MrC-wYZ9Ncc1jk83uw5q_Fos5rxvu6m77bUbxEgW2JjiKfKRL1UkeyNjI8_QKRZAVhpK02eF-ephOKmAbSCBYHXAGzgszVkxQbF4PqQ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f0c663da9.mp4?token=GoHtZkIse4FSgRB_l6dPM82GYyuWHqGI2aW8yta0DNSMZV5OSe-yWsFmIAFIseQD3ZgLE2Z4ZR3OHz5xIGfAYCNQ2DkyOKb0P3J1HVEzrzIRB1pwsY-ovZKx3Q2gkIA_nNL6ELkfuEtWvyK2uqlLJIkyO-4dm6OsVnLsYvQE44LY3K0ddzpx6akRi9jy-jwRtJEfj0LnNcWkgsqYGmCMMtdS4Q_LikQ5Y_t26frQkHX6x6MrC-wYZ9Ncc1jk83uw5q_Fos5rxvu6m77bUbxEgW2JjiKfKRL1UkeyNjI8_QKRZAVhpK02eF-ephOKmAbSCBYHXAGzgszVkxQbF4PqQ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇦🇷
🇨🇻
امکانات سوئیت ۷۵ هزار دلاری ورزشگاه میامی در بازی دیشب آرژانتین و کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/98170" target="_blank">📅 17:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98169">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58ab6c152.mp4?token=ArkAG5ES2FFp3RECSyZcJY_KvpBJTF-Fd1B2REGCkDu1w6ibhxdwLK0eShAagTU8iD_op6FJS137UN2AogENNu03uEwkmaAdL4_Nmkbl8qm_16fXW5PPTl8HzXF0crd0EvacxJ9bjrSlXecTUaLwJCpF3eRJwCqy8DvkF6yTwEFZo-kHIf08zTBmkNjw0IQ4vjpy_caq23aUDwcv_k-774K5dUlaMkdvIkepoA1BhtIWwZRnzA3oBlo85RcvTSUQ9C7hl8mo0ziyxddqnUdoUNV_yjHGs5Bg1y8HpTp0CYLYqFTGXEsdnrYDeWRdBtpr3M1KKSVLqANOdBtW4Y51CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58ab6c152.mp4?token=ArkAG5ES2FFp3RECSyZcJY_KvpBJTF-Fd1B2REGCkDu1w6ibhxdwLK0eShAagTU8iD_op6FJS137UN2AogENNu03uEwkmaAdL4_Nmkbl8qm_16fXW5PPTl8HzXF0crd0EvacxJ9bjrSlXecTUaLwJCpF3eRJwCqy8DvkF6yTwEFZo-kHIf08zTBmkNjw0IQ4vjpy_caq23aUDwcv_k-774K5dUlaMkdvIkepoA1BhtIWwZRnzA3oBlo85RcvTSUQ9C7hl8mo0ziyxddqnUdoUNV_yjHGs5Bg1y8HpTp0CYLYqFTGXEsdnrYDeWRdBtpr3M1KKSVLqANOdBtW4Y51CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گریه های شدید یک خانم تو مراسم تشییع خامنه‌ای :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/98169" target="_blank">📅 16:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98168">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a2a62f27.mp4?token=IYxbPj7GO4L3gf9tru0a2wjeFTlgOOudMb-NcALIF1pmdLqaJyikNGg5MM42Fi8OoPoPtfDREzA8tMT-ghGX4HY8AZVJ4ILT7ms8qwLsQm-kSQMcSNxSzx1N8Nxzs6LfFR8LUyJao8DyQ5u3v3SCWA4H6OFhcxthqbB59oNnZlNkelvKUW3Yhhe79XWmSOXD80V19CXci1J66ubmRApv3UlTo2q2MSsHNO1rRWHwvVacgghHA3OIX6bwS-D0zIRmB3bmFDOdfj_TBMTGeDSRx-qJABnu6nssPegAurS1rh91xK3ovEfYzWw9XPlRzGrvhczgczZnTsGDk1cVYy9NXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a2a62f27.mp4?token=IYxbPj7GO4L3gf9tru0a2wjeFTlgOOudMb-NcALIF1pmdLqaJyikNGg5MM42Fi8OoPoPtfDREzA8tMT-ghGX4HY8AZVJ4ILT7ms8qwLsQm-kSQMcSNxSzx1N8Nxzs6LfFR8LUyJao8DyQ5u3v3SCWA4H6OFhcxthqbB59oNnZlNkelvKUW3Yhhe79XWmSOXD80V19CXci1J66ubmRApv3UlTo2q2MSsHNO1rRWHwvVacgghHA3OIX6bwS-D0zIRmB3bmFDOdfj_TBMTGeDSRx-qJABnu6nssPegAurS1rh91xK3ovEfYzWw9XPlRzGrvhczgczZnTsGDk1cVYy9NXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
برد دیشب آرژانتین احتمالا بخش مهمیش مدیون این سوپر سیو امی‌مارتینز هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/98168" target="_blank">📅 16:40 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
