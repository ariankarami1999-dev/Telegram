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
<img src="https://cdn4.telesco.pe/file/MZjgOL25P0HOGAEBcLlVYWff9nmbgMEZOOpGAEYk9gKGt8L3dmezX8cBUK3TZ_bVOOUgFppyWrLMDxf_LmISi-ZsJfKhvjCemG9U0j105bCPkDjbmKrl1uZbkERGfy5L-SGYZOYzCD5NC6aDz9HvHZnx4eUqQhRkcLIQ_6r7QvOjiT_cEtNFhlv_NXRmFxPBbeMbYfVVKMK4VG9t8JrucgYc5AjmJiG1sqS31GMco86TVjX8qEcyC17H4huo0sbGZY7owxgqzQXnRW-qtBwHLCx8IQsg8YduFgAILwVUIv0jwbufW1RlOT-4nfKjw5MwYAdPlgMD058JZy1_8XPzhg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 12:49:04</div>
<hr>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQRFPb_C-bV4hP4ARl0bjQA8YD4hvJt8770ZynlXhRrkEz0qU-Y0Czrfb3ioE_Qorfffe8ug-qU7fhU6jvLLfXnvRqLvv2J_xod63yV0ovQ0942Pmj_VcFB330v8MfIhDDy5nIIc9_d-hX7kPLGhwJ_pm9QX53fZ3Wt79qgSZXZWkAGgzjKw72vtuW_tSM0Z3w8Nqh0QdV4SG3kRy_3vsZ1mjbU_ap22_Br5Ly-NT3SCzqyH_7o_NaNqf4GeotBmtalElBLxVrWpu-7ruoZu4riiOD3xXN2AyP3axUXotRtFb7zdrYswLYoeiTDotLS8r8g_TVx_9rc9Z_csG1bTyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSIrOCdxRCBym-pYcJWJQvUt4Knff5D7Ck9U0ZsA7IV53cYECgwFSaAfXnXUtkHXtG9WiReBP4DtYLNTkh2-3O1BpA_cNKLueE1MKmIgERXBZZTFhJlyw_pA5AoajOBQ7xdbukVLPdVnyiT65Hm0Eumh7JmhHe4Ll1wUVdy-1NFktMesChFNMqaPCrWWmbqE0X8ImrjLd0EOIbT7mruCPKGBXB6l7Ajex7Hk6-KoY_kTR76wPbSBxFksTMDr0a_z3PGxj2ym8-onurJJ8j8KhCcUl49kvynXcnMObSdX3FOl_lqajHMrysolpxUSMQrcGi3MEW1GzVeWY9E5iWwASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=Mci68Qgr3qdGm30KPsXVoPYYs3BhmizeX2qOzBMuyO9pcvBj_Wck_Q05I47yc6cEH7NfVOBjdw558PzR-6WAw5S-wwmqk6pD4SSMLkbsoOuu8DWDM8CshqjzDosKkQh6Jpzjy5eLUzaZZUzGH9zLRE1U40cpV_7VR0utfkYF8ooa_mrySS2-9aJvNqTY4A_qj6bV2NvDohwNXx3mJXd0G3AfnfWgY1pIuc2Gj6qevP8ilwr0JaiXQZfk8tIbd0CExA_jSlmlEQujc3RdvYBVTRjUyvmnTRPjNaQCutWnNW8zGrGIJCT1qppFkYbhXbQa_BjsN3x70EILMiZZjjDgtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=Mci68Qgr3qdGm30KPsXVoPYYs3BhmizeX2qOzBMuyO9pcvBj_Wck_Q05I47yc6cEH7NfVOBjdw558PzR-6WAw5S-wwmqk6pD4SSMLkbsoOuu8DWDM8CshqjzDosKkQh6Jpzjy5eLUzaZZUzGH9zLRE1U40cpV_7VR0utfkYF8ooa_mrySS2-9aJvNqTY4A_qj6bV2NvDohwNXx3mJXd0G3AfnfWgY1pIuc2Gj6qevP8ilwr0JaiXQZfk8tIbd0CExA_jSlmlEQujc3RdvYBVTRjUyvmnTRPjNaQCutWnNW8zGrGIJCT1qppFkYbhXbQa_BjsN3x70EILMiZZjjDgtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=g3zrDzz0iPNdBASr9BXFGEnFVOgVGLqA7ZuejpSxrm1rbgCtMp0kBqhQSJM2_yzT3N0RHELdRx2X9RdZFDFlKzqW4VGmGNBxAPb4sxKopQZ5pQakaBcQX2Vv2BBKUSRCkx5eFeuD8EMPyShMZkOQsKDpbXg6g4_j0Tf9_1VUpnocJjs-q08q96DbLLtFIfN2tzJs7BpWqgsNinWKJVswnRT94LdEDm0OtdmvRmawPFiT8y8_XBZRTHRTE9wlG4hI4Br-9-kKprOwBuUv-aiTbJL46TJyYuylehv3exlfzjg2-el9kvvksNBQu2_KEI--aecjofkuWmD92qSYm18-MFRD_cJBz6QZl80T6tfkGODWP7VkYAmoFKKsiJYK_yjESm6to2awdxZDgjw_1rpD9vIVLv_HVoCxn85V7KtorynrLDc7t5Yk2OOR-SE5JEX4jM_AYFsBymML3PgkKLpTCtZs8B6uYh8Bvu6aa2SEahsEUE_sLLU_RtkFwtrJ2wR7vYN6jOG9qLfkbVZ4iUaA_eItUmSG9MXAr49kyXjRyBLZcQH2cHdin9QkzLdoVTHYM5FVOHJRE7VqeXeXOj8hIfPNyc2uI9edD1o7QKh3Z8wvpZvYhSSA056K-nBnoV84rbyf5ha-ir6PPZTBSktxyzY0Tvm_EK4CqhICiMokrNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=g3zrDzz0iPNdBASr9BXFGEnFVOgVGLqA7ZuejpSxrm1rbgCtMp0kBqhQSJM2_yzT3N0RHELdRx2X9RdZFDFlKzqW4VGmGNBxAPb4sxKopQZ5pQakaBcQX2Vv2BBKUSRCkx5eFeuD8EMPyShMZkOQsKDpbXg6g4_j0Tf9_1VUpnocJjs-q08q96DbLLtFIfN2tzJs7BpWqgsNinWKJVswnRT94LdEDm0OtdmvRmawPFiT8y8_XBZRTHRTE9wlG4hI4Br-9-kKprOwBuUv-aiTbJL46TJyYuylehv3exlfzjg2-el9kvvksNBQu2_KEI--aecjofkuWmD92qSYm18-MFRD_cJBz6QZl80T6tfkGODWP7VkYAmoFKKsiJYK_yjESm6to2awdxZDgjw_1rpD9vIVLv_HVoCxn85V7KtorynrLDc7t5Yk2OOR-SE5JEX4jM_AYFsBymML3PgkKLpTCtZs8B6uYh8Bvu6aa2SEahsEUE_sLLU_RtkFwtrJ2wR7vYN6jOG9qLfkbVZ4iUaA_eItUmSG9MXAr49kyXjRyBLZcQH2cHdin9QkzLdoVTHYM5FVOHJRE7VqeXeXOj8hIfPNyc2uI9edD1o7QKh3Z8wvpZvYhSSA056K-nBnoV84rbyf5ha-ir6PPZTBSktxyzY0Tvm_EK4CqhICiMokrNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ag1IpHgUQbCuvlKDh3wit_xSm5kxt-_bt41xzna8DfsLYs2iKX79o3dGsiSYBX2eXU5x8MzGHjImdtnsSIez-_fwTNwkKKtCXT8b5PAmdob-MriBoNikrysTQ0P0FpQgNehhKzP8v6IM7g30nPWXfIH-3kJm7xpn5v2pBBRg5meeIOBQ36_unB4VLXVh6Kri-MCTW9-eFi8Biq1MYH1j1r9Iv4ZFsubaiZzYC0rY3t5JYJ4FSbBbtMmSbUx3ZzI2D6_ywcJw5rZjQ6LB5edGBwjpFXGRdiYy2KFogcivwkF0JrC6g_72r9dOxeVv45k437HPrOTkVUVzlNmDJEruEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F_KTgnzBWoEqerf_HbGFwTjv5TY1BjYosaYC1xwgOsDvYqlHydYca5pUQU4R6o7w-XZAAnkLxWrxdEN8nIYs_Xmp9cKnFMcr6GqubGZJ5OY11sDEa2wkMa4lXNOT2cZFXlm4xlVJZ42-9yja4r-509o9qMdLD2Gh5SeT0Mah85iwTkgyNZKYciIsxz2LxLP70P82epgWMJhXfdcQYerYwHk1ePDn_ic_GYm-PKEUyWxQoI_YzAzGg_MspYBM9Zc5hgTg5mSZ4ze8Dxr2b5Ie-1Ndz6abmfXG_rWydAEMrvQKUJ8kqFtI-NjsvkfqkbMTNfxJFE-BM50utpnbePyWIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vTbNLbxHArZAtwc1qWtlWnTXF9Za3a4LPQhcB52nbu91xsOEEOdhd7kIJtQHpteLzIR6kwGLZamW_6QC-MBdY_xTV-3ACc_k5k7i0Pp6-ECaQNh_wCu2jlhFMfqxeXVDHXkNCOEjKJf_adCYF9K0V6AI-njAQwa0PjxCRLEHpjuVfBA1T2gM0Fvng1KVCvJ1QTJV--tKlLGXSIPNo0ABCql5V_-BN_453-hQ4SpkSJshpoyFvsFRTteHOF_0DCdgO0TcNK1vOzlgrJ1PaABdMnS3Q3OYj2NcljkgwYVKc463SXc67oN_Fqg0tF0-BoSDvBp_Gp6rdWo6ZRUPulS2bA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=MrEvf8-rktPuDnI1ji7IR73UpOKUAgEpZQ2HKe6fy2VyR0-2E-PK-7HGLGFYxuIdoLfQMwUcPllokuxyKRR5cqOLvDg4p2MNkmJiwOYvO_oaSnI9otsn2fLMtZ9NdhYhABCf3PYGS1mYrR1on0Lk3JV7Df4tNLccIOJl3bqL8e0lPA4kx_rP57_xxHaReyzp_kMIhSKOUk-tBacB45ukRMH5w6qWVUaWXJn3oPJ2IyTmFuzeTWM9rSA2ZM4fyUkBfqbkp7eMb9IhKBAZ-wZC3kr38vGqxZ8zXw-FlDAyFocW2Xk9eKeWPUsTs0TJBUumAEQq1u02Td8RdCvk5dRLbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=MrEvf8-rktPuDnI1ji7IR73UpOKUAgEpZQ2HKe6fy2VyR0-2E-PK-7HGLGFYxuIdoLfQMwUcPllokuxyKRR5cqOLvDg4p2MNkmJiwOYvO_oaSnI9otsn2fLMtZ9NdhYhABCf3PYGS1mYrR1on0Lk3JV7Df4tNLccIOJl3bqL8e0lPA4kx_rP57_xxHaReyzp_kMIhSKOUk-tBacB45ukRMH5w6qWVUaWXJn3oPJ2IyTmFuzeTWM9rSA2ZM4fyUkBfqbkp7eMb9IhKBAZ-wZC3kr38vGqxZ8zXw-FlDAyFocW2Xk9eKeWPUsTs0TJBUumAEQq1u02Td8RdCvk5dRLbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال پیش
حسن نصرالله، رهبر گروه تروریستی
حزب الله لبنان، برای چند هفته،
ویدئوهای تهدید آمیز می‌ساخت!
کج نگاه میکنه! انگشت میزنه روی میز!
رد میشه و…!
رسانه‌های جمهوری اسلامی هم جشن گرفته بودن که آقا اسرائیل «با یک ویدئو!!» بهم ریخت!
تا اینکه در روزی چون امروز
(۲۷ سپتامبر)  ارتش اسرائیل با احداث یک گودال ۳۰ متری (به اندازه یک ساختمان ۹ طبقه) در بیروت، به تهدیدها و ویدئوها  و گنده گویی‌ها پایان داد!
به همین سادگی! فقط چند ثانیه زمان برد!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=H89QaAcvfVzyWTVjmGzUJ5nMkw90cASi3K1Hb4ZKyOfsuEjT9zxcHBVeQkGq9XJVB8uXNG_CjyactTU4SAIVOfb4cQkJysHbSqrIFv9jMVnJRxZhdAyHHbdfbcBh3IFzyWbNsxunhePYaXXpo5kf5jy9QzzozQTVFVN0ZSlgpgOeaAstqiFNZDhf9VtdrX9NasZryq19LSjVKRE7UonUpoiqLpUVG3vYCy8SliWf4XqFPyaGPyRM7qzoBuPlntc4218kmePfC6qi0XpFmOo476ZaLPUuXp2kM7P7AQY4V0ZW8Fw5Z2G35Em7o-bdcTD9uneXv6Q8ORI7LxasJbkjWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=H89QaAcvfVzyWTVjmGzUJ5nMkw90cASi3K1Hb4ZKyOfsuEjT9zxcHBVeQkGq9XJVB8uXNG_CjyactTU4SAIVOfb4cQkJysHbSqrIFv9jMVnJRxZhdAyHHbdfbcBh3IFzyWbNsxunhePYaXXpo5kf5jy9QzzozQTVFVN0ZSlgpgOeaAstqiFNZDhf9VtdrX9NasZryq19LSjVKRE7UonUpoiqLpUVG3vYCy8SliWf4XqFPyaGPyRM7qzoBuPlntc4218kmePfC6qi0XpFmOo476ZaLPUuXp2kM7P7AQY4V0ZW8Fw5Z2G35Em7o-bdcTD9uneXv6Q8ORI7LxasJbkjWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2NRb6ogCHboWI7c7hI3L_XvkM1KY_8V37eZhIwxz3tVhjpIsghwjJp3NVUQAejQOQj_ZmqSEjkZHBvmbBh0SsLZN9TfSsUFPZDKAWdfjEABMnnnBl3Czq0mgmRLpipwkxQudS9QQi4xTAbdMrUXn9WGGZjhOrkMv4XeZuS5vd5x4aT_0IHXrhJppYj7jrBBNVM57nirxx-i7JkDOUx5-ElQ75VQD5GKrmY5J_jaoimVA7aoNKSNly_ViqUiyboqEVaNOvk3KMnAJdiWxSsWvy8G7pMwVuwnWWy7KnRX2lPfFJiLa6z1OC70rQoUAW_4N3dQAkZnoxOaqN4ukBXA9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=LW2XcWznb_7AnCw610AeocHX23dxm_C-OYEcw4cv3rTUxluYaOTJGA1_stdLa1N25l8boq5cvvoPwUuLbe7Zmy9HaTdirJJOYLR45Cb5nyaXnbyyQDLlgpnff87BXnVdtv5pwJTxqUpdKmrfSDxBm5JTfefFniDtiTfogne0DX-cYiVRGOPjkGAGhtb1r9jW_Ji6eyV1fJFarGXa5s7kmbWvr_-dMkkQst8BLhK7wQ542p-PQooLvksVnrTnGrO-1o-8CGkfiebEs6pKZZ-qubgtNHlqwQ3jX_zvJxDcNIJSQhCDWFkpJxQeu4dUnfwM20WUXKpv6h_mFm2HcrQBNBWW-hwvUJYKtNuT4LxZCw1cZBM9YRHCkqFuieFJluFwSyXSDjjpedyF010IIDGeNOerbvr4-aLSugo2YisQrEny0Gwi-wHcRRU0BBdkaijnJOgwFpQJv9eLiu_goNPZTBrGjUg-psrTslWE7fCQOZYKyw23AoTFFXseFk5fAc5k9O_vJ_2CORPufEw8sExlOAvmxHawZM4P9lECUasAH2suM6LmvkzAX-XWVP2WPRDp-l2gy8vvbb5bGT6L7zmu7-4Yf8Ha3xYSAiHePHWm4qIZchc6Yf3hHoe13RDbPfpRf_aEwp1LkFiAoHg_S5PJBWH3jghqQITgsUpmj1xe0C0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=LW2XcWznb_7AnCw610AeocHX23dxm_C-OYEcw4cv3rTUxluYaOTJGA1_stdLa1N25l8boq5cvvoPwUuLbe7Zmy9HaTdirJJOYLR45Cb5nyaXnbyyQDLlgpnff87BXnVdtv5pwJTxqUpdKmrfSDxBm5JTfefFniDtiTfogne0DX-cYiVRGOPjkGAGhtb1r9jW_Ji6eyV1fJFarGXa5s7kmbWvr_-dMkkQst8BLhK7wQ542p-PQooLvksVnrTnGrO-1o-8CGkfiebEs6pKZZ-qubgtNHlqwQ3jX_zvJxDcNIJSQhCDWFkpJxQeu4dUnfwM20WUXKpv6h_mFm2HcrQBNBWW-hwvUJYKtNuT4LxZCw1cZBM9YRHCkqFuieFJluFwSyXSDjjpedyF010IIDGeNOerbvr4-aLSugo2YisQrEny0Gwi-wHcRRU0BBdkaijnJOgwFpQJv9eLiu_goNPZTBrGjUg-psrTslWE7fCQOZYKyw23AoTFFXseFk5fAc5k9O_vJ_2CORPufEw8sExlOAvmxHawZM4P9lECUasAH2suM6LmvkzAX-XWVP2WPRDp-l2gy8vvbb5bGT6L7zmu7-4Yf8Ha3xYSAiHePHWm4qIZchc6Yf3hHoe13RDbPfpRf_aEwp1LkFiAoHg_S5PJBWH3jghqQITgsUpmj1xe0C0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=XYspbYQYHNxf490r2da23G_JGAT-8gd16CppH6DIokF9WOSpOj-ZEIwfapnxBgNiL1imAbs_bVrZI2utobhjyEcby6Ib905ON0loeyhiT5_rKoXMICwiEx0i3SvAe-7f2YFb3gcqpzjz5-fPnLIeFiBXMgzIn-XCH4bDQaLf5ljpceJ_15EQ6gmXAr1ZVmqIElpvzoeI9gNQLiEBB5Fca2oZ7U19rvg1iHRAlY_LqIm0FWwbc9wS8NVJPYfAv_qQ2eYjB67YY2sCKgZj-nOIKgOprXikNTL26bw-MejW3Z1aAVc5IJB9wJW1VBkNavAjnXwHa1V2GRXI70mpFqdXPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=XYspbYQYHNxf490r2da23G_JGAT-8gd16CppH6DIokF9WOSpOj-ZEIwfapnxBgNiL1imAbs_bVrZI2utobhjyEcby6Ib905ON0loeyhiT5_rKoXMICwiEx0i3SvAe-7f2YFb3gcqpzjz5-fPnLIeFiBXMgzIn-XCH4bDQaLf5ljpceJ_15EQ6gmXAr1ZVmqIElpvzoeI9gNQLiEBB5Fca2oZ7U19rvg1iHRAlY_LqIm0FWwbc9wS8NVJPYfAv_qQ2eYjB67YY2sCKgZj-nOIKgOprXikNTL26bw-MejW3Z1aAVc5IJB9wJW1VBkNavAjnXwHa1V2GRXI70mpFqdXPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uP86bIVtPi9mAqOG0Xt1I131-Jv5xxUB3v3L1UZKSs7v-Q7q-o3rNe0DqxS-5h3Kn4T6M1H44wjXGh5BJdgUUzVe6c18GXm3_l1AQN4z9AVgH0iM0oR0QyMSHBP6-Cbu-663k7JhSy10CfyHh6rW4WxBLxK5EDW4tbkJpprVLuoVTz_dIcfMDcEB2dzBRewJ1lF5AnITdi_uQ49vjaMJiWWHefbCagbWxbX89P1wNaudNzfpVI2DELn54iC7GZtc6weIK0d3t9DYiKk3RIvVDrskjOUdtL6ZoFYXAJW32VACP0YRqk5r97NYnJK2DYH2o5KdtbWlWeYDiFUPNoWuDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=fKuDZeBS02Myl_Fk72a0kFfLa6npS1k3dabOR_js_6SyI-S9lu8Dl9IgC8B9pe70NtC5htD2bsFpnJGW8aSvuUTo0eknNbM5snzZkJQdBhTqee7yUddeCnehhlkWMdy2gMINveTbSraGfwXzzKI9DWRh4DKyRLalj3r0kcs7ZGcvQblnkPM3clgD_hpU8ykLwndj_JwWT2NsIkeCOhxx14qivElSwy3MrPCLewAywKdzrLEYOZI0f0dz3p3FIFsJ0vw0abP7EEQE7MEViegmyRP8jEMHLzNzkX56e0_rJ9aZlntvOUciTofqtzVcL2vPFdsLdorY9PQ3h9J2hcB8rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=fKuDZeBS02Myl_Fk72a0kFfLa6npS1k3dabOR_js_6SyI-S9lu8Dl9IgC8B9pe70NtC5htD2bsFpnJGW8aSvuUTo0eknNbM5snzZkJQdBhTqee7yUddeCnehhlkWMdy2gMINveTbSraGfwXzzKI9DWRh4DKyRLalj3r0kcs7ZGcvQblnkPM3clgD_hpU8ykLwndj_JwWT2NsIkeCOhxx14qivElSwy3MrPCLewAywKdzrLEYOZI0f0dz3p3FIFsJ0vw0abP7EEQE7MEViegmyRP8jEMHLzNzkX56e0_rJ9aZlntvOUciTofqtzVcL2vPFdsLdorY9PQ3h9J2hcB8rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو و این حرکت
یادآور داستان‌های عهد عتیق است!
شجاعت و جسارت فرزندان داوود!
که در عین جوانی و نحیف و خرد بودن،
مصمم و بی‌هراس،
مستقیم به چهره دشمنان خود می‌نگرند!
مثل داوود، نوجوانی ظریف و آواز خوان!
خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه زده بود، اما اسرائیلِ ۸۰ ساله، از این نهراسید!
یا از اینکه جمعیت ایران ۱۰ برابر اسرائیل است!
یا اینکه مساحت ایران ۷۵ برابر اسرائیل است!
در قطع سر حکومت جمهوری اسلامی تردید نکرد!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWKJTP9efvsBF5z-9E7QRAbgzpRP8Gs1g_eSDtZdKGisQVEpVSrfijDykQdA5qCxPEeybDKVeQHGv-PyOzSFdScN7BmOYMQAF9OuwzfpJtIKy2COJiwTTMxEvD-w5d3PvgetG8bH0BImUP-A_QXt3su_wQzWgsyI-CkyZPNAHFbdNVi9vN2JXHMqIA-xlQSbUE_A5CdzNZDX5-6fj5xE6GjsU3tc-VZ-WyBZCKdNfzxUq_b9tuJoRc26ci9sUsE0b8G-ml5-XwflotC00xVKgsr3y58DklywAR4A2nc8QSxhXjy42ha9cj1JKaPLSKbw6PObg39FgV7BPzM0A6h4WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9OLxNos75GTbMju-kxTJ2O3G5FKXO5u_cHnkhEGoE0sRVgQLelb-ij7XX-oUpII8okviRdHO_L3gS1ZIiINDV9U7F1zuDfGF2ehrF7CiTE5d4Yjtzd4b-yFDb_3Ys0ZZbIOf68qAt5Xg0cxZ4Z7AqpLaEqcnXpc253RaOXv2DRwcHzPBNu6IRj68TpU4D9QDEwB8lD3LAOHyp2rvpQzHQMbz-h0kcFq7Uw7FywvahqFhcKECiXJgXzEhW5Fy-0i9tKkc17fzmOcLKEM6cWEmNf1HRSVGrNUow4LeSCtDMh4-sBegE0-i8CWi1eocRUUv-Hc3N0KuvBHXM31nGB9lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود
که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.
.
این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،
و نقش میانجی‌گری این کشور.
(وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،
باز هم ترکیه این مسیر رو باز نگه داشت و گرچه  از انتقادها هم مصون نماند، اما کار خودش رو ادامه داد و سود بالایی هم برد)
🔴
با توجه به وضعیت افغانستان، پروازهای ایرانی به سمت شرق (چین و..) هم احتمالا ادامه داشته باشه
🔴
و از روی خزر پروازها به روسیه ادامه خواهد یافت.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=XyDHHQgsxQsL5W3UQ3HUxiIgvRr2n1FCRfwXhhb52D1MezL3Np8OkUn1Z4zSOgdkCsojiImObHdpna-PoWZDUU1M5R6TitAPs78TxfeXeCBCcojyeUhcp8BJvVIojOxVxeFlVpY2QslLAGjx5MHvFNAFQLmt7RzcOkQ0vCOxmB11UCTTsY_x6oEWMM_usEslxScvklvufWK71EZpd1GjY22ANjPN2v3FNGVvEgfl8i4GWC-CiSfxVzEJcOtnEQl-Brex68aNyOK0DWF86hst80oxjCFGgmLtNkOQGPhuL4NAikee-C1Zu-E0cE8cFdhoAoJc3JstJJYIV0FVQsovA3jJ9g9AXbULuu-ylulw2W6QwwrxzAhQjP4vqh3gMNQDKYIF8zb1qaKOiMVQzDGcfLSxn3KcR-KnRcYaUtFpRxyvQ2i4NCi39UYiB7km2e3KFDYLq8tYJxu-udhPLbDNHaMDhlpi9UDfs8NmH58w2KfLbrvfzxlColwHltWo0G-wroTtaf6sUQbb3GTAWRkWPAD11t6EIwxhc3a7I9wC06vyBdlsv1Ts2zHUmENASw76d6sRmdlkDHXrB8Hz8-DwWuUMD62DD_gD2kQgjbgOAyPbfipXmDvZnewa-nIkw4-JgQW7O6qhRTRPkmEE534WTmiBCITCUCBI2Wx3jLazDO8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=XyDHHQgsxQsL5W3UQ3HUxiIgvRr2n1FCRfwXhhb52D1MezL3Np8OkUn1Z4zSOgdkCsojiImObHdpna-PoWZDUU1M5R6TitAPs78TxfeXeCBCcojyeUhcp8BJvVIojOxVxeFlVpY2QslLAGjx5MHvFNAFQLmt7RzcOkQ0vCOxmB11UCTTsY_x6oEWMM_usEslxScvklvufWK71EZpd1GjY22ANjPN2v3FNGVvEgfl8i4GWC-CiSfxVzEJcOtnEQl-Brex68aNyOK0DWF86hst80oxjCFGgmLtNkOQGPhuL4NAikee-C1Zu-E0cE8cFdhoAoJc3JstJJYIV0FVQsovA3jJ9g9AXbULuu-ylulw2W6QwwrxzAhQjP4vqh3gMNQDKYIF8zb1qaKOiMVQzDGcfLSxn3KcR-KnRcYaUtFpRxyvQ2i4NCi39UYiB7km2e3KFDYLq8tYJxu-udhPLbDNHaMDhlpi9UDfs8NmH58w2KfLbrvfzxlColwHltWo0G-wroTtaf6sUQbb3GTAWRkWPAD11t6EIwxhc3a7I9wC06vyBdlsv1Ts2zHUmENASw76d6sRmdlkDHXrB8Hz8-DwWuUMD62DD_gD2kQgjbgOAyPbfipXmDvZnewa-nIkw4-JgQW7O6qhRTRPkmEE534WTmiBCITCUCBI2Wx3jLazDO8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoQTpAGTsk1aVZdKV134P4FrAT2JK-xdGol5qGhIfZunmQohz66Cdm1eTB39BzQkL4EOWnj7IoxpT96g2NUUxCt0VvyURAUX8GnbIrB004art3rI-ZMELq-WdsTdVzaLtTIphwtZcLlAkbbrisvcalD3kWZi5Dk7qAxBP1Mo3W-ZKkIiJsCzQlLCA29r7_yeoIFnzweqtjqbN4UHahD9EJUNyk8ePFTNRtp9B--o0jGyJ9KivK6KEjaVpeC_Cj2ZXFuJg7YHYjqGiBNItPHwFg3lBA9mYqZB4uaKi8phkPO1kwiVPZAOBphm7H6sz4AEQJcMzrmIRPHKqefZjalI4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ki0GN_IPEniI8qTP59m2fDP00HNnSlAkWbtbVsLdpkyrr4y_2ajb-g8aP5-ZM_oSeHlEmwH4OhXH52glTPMzXp4PGNH7uV1kj9kGpMIOTQxbQvL4v4YlIrIM5Vl_eeo5FZPJ-8bke_KUNXvr3AD-xClj0knv8KbwvCXhoSK47ZEak_r7U0z-CBqWu5yzHatIJXeVz0ww5t-HQvk0xAwVhfSq6gKkEdOM_fo6qv-ynSMzPPbvsh5PYG0jKNrh4x6-R93rNfAmYXomq21PJZfRIQF9nrhl87-XSvoU7JV1kTufGNWwttBepRyaR6tggktcsnXWUcTPPDh6-fwg4poS0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=FxTOVrxovZq_-_BJOwdIUAykozADSdy0LdSPDhpii2std89fJLQeoG3FNH3dStyWYorVfaGEnEvq_KYy6uls-Azauw89QdAihlMdANN3R0RdIjfM7N-uzfAVQCkDK1o34f0yN1O_gntPpbEwlKJ5qB06wMQASg--rPh6JKf9PMQu-tQHA9836r91gbfDQhamXIdiy_rHwVbH1vN9V4nrSocoYxTKe0GdUEcbY9GH8tB3ZkyQDPVxHqJk8b1v_tDWYqWMgw63vGhrwUyBIHsW78553hnWjU-YMlaKOH0UUJ_2mOYIwN9OfdodPUJ38MJi_Ku8rtw8hSw59rtLgTF2gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=FxTOVrxovZq_-_BJOwdIUAykozADSdy0LdSPDhpii2std89fJLQeoG3FNH3dStyWYorVfaGEnEvq_KYy6uls-Azauw89QdAihlMdANN3R0RdIjfM7N-uzfAVQCkDK1o34f0yN1O_gntPpbEwlKJ5qB06wMQASg--rPh6JKf9PMQu-tQHA9836r91gbfDQhamXIdiy_rHwVbH1vN9V4nrSocoYxTKe0GdUEcbY9GH8tB3ZkyQDPVxHqJk8b1v_tDWYqWMgw63vGhrwUyBIHsW78553hnWjU-YMlaKOH0UUJ_2mOYIwN9OfdodPUJ38MJi_Ku8rtw8hSw59rtLgTF2gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=gW0Ac4pDj1o5cC5msS5r7-ODOAV_filbO65jeqiNak04CJkGSRWufb1yyQDNtxya43CnNWMOC02I_9UglQtotRHkxDyiKLlQ0-D0X2dmgtNNXK660Lmj7p7JY9F3nHoxHyfQ-vtf26nL4u9AUx8p2U63eMq-4zCeLLajgyEotl6cHLoIK-gnaepKoOkKO_eeA4R5-RgjFRN76L506ImnAye_40QYN5BlN_spdL58EChXkR1lVLw8aGmAWxVV1SKWU6wyjGU-y2GFpTbRVaieJFSqrjbjm2Hl9MVc9iiFGPEfTRcuUCoE1PKkuq9OlvCK0KOTjJy5lZKIRy1Db6By4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=gW0Ac4pDj1o5cC5msS5r7-ODOAV_filbO65jeqiNak04CJkGSRWufb1yyQDNtxya43CnNWMOC02I_9UglQtotRHkxDyiKLlQ0-D0X2dmgtNNXK660Lmj7p7JY9F3nHoxHyfQ-vtf26nL4u9AUx8p2U63eMq-4zCeLLajgyEotl6cHLoIK-gnaepKoOkKO_eeA4R5-RgjFRN76L506ImnAye_40QYN5BlN_spdL58EChXkR1lVLw8aGmAWxVV1SKWU6wyjGU-y2GFpTbRVaieJFSqrjbjm2Hl9MVc9iiFGPEfTRcuUCoE1PKkuq9OlvCK0KOTjJy5lZKIRy1Db6By4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=GHVeVs6BU-aSn9H_PxFQicaCVVoz0SIMPnU5Hlw1ZohAL2rpEuGJgUhg7jw-GnFnwBUbVEiQr8jG1ZzCp-wUn-NUlyWSVDeNtA2Onf4SOIr1lhgFBronNvqbo340abM3pGCW9XZe7GWCFRfHLR5hlhzCZkEb6ici7xyDxn2I3Dh853elwQGofr_EUV1py3cfnxZur88vc-3Ltm0boF1AZfHlYPdT5cxxMrkzueVuUx7iAUNdhCWVvGuPgLqV6SpRJGIfccBg_gC7WI9fGdbNnXs-ZWGe30gomc9q8HUJXFWoM-ARWCnHV_YbhFfJvAoSsydZlPsd5fhwACBHKTsM-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=GHVeVs6BU-aSn9H_PxFQicaCVVoz0SIMPnU5Hlw1ZohAL2rpEuGJgUhg7jw-GnFnwBUbVEiQr8jG1ZzCp-wUn-NUlyWSVDeNtA2Onf4SOIr1lhgFBronNvqbo340abM3pGCW9XZe7GWCFRfHLR5hlhzCZkEb6ici7xyDxn2I3Dh853elwQGofr_EUV1py3cfnxZur88vc-3Ltm0boF1AZfHlYPdT5cxxMrkzueVuUx7iAUNdhCWVvGuPgLqV6SpRJGIfccBg_gC7WI9fGdbNnXs-ZWGe30gomc9q8HUJXFWoM-ARWCnHV_YbhFfJvAoSsydZlPsd5fhwACBHKTsM-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
«نصرالله، دو سال پیش هنوز در پناهگاهش نشسته بود. الان کجاست؟ با من تکرار کنید: پررررر!
و سنوار کجاست؟
پررررر!
و ضیف کجاست؟
پرررر!
و هنیه کجاست؟
پررررر!
و با خامنه‌ای چه کردیم؟
پرررر!
«سران ترور را یکی پس از دیگری هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2ZquEQeUqTyaHT9qJMBJG5Mmqio4Zj1C03jIJA-kCgHPRsYbAGfTse1HIDzhNyLajqIb--UL9sMszeS15zpt6sTLwA6vWMNge9uai5Gp3NhtBSpF7Fsn66Zrfsv-UQ8p2mJMiLMqwALg8OuhpD-Nb8pQ1X_g66mzmxCORvndmFj1XD3F7XxbGqyGoPNzQI061umXogEzWOHzlngrQ-4vTL72n3C_TRrAGbxgFmpPIXZAItQyNrret_Dl8LltV77h_BMhrN8wyWFuoJ0A31KbBlFcY-GtUkwtjOtNHmkYQDFOaMtdOLZCJV-3BdNGW0pH_5Gr-HhoHZFjrdDi5TX7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8HiLsxeTS_3dWm-sOVkQJ7Ohet5it8Rv6g22PsvpwvbarCwzyNUG8feK69gzNKgty6ooQYg0k57unoFqFUmejm5k3RF76bva9jubgrH_Yqql3ajun90xZE2P8itcxNV9O1w2u2kfMCHq7JMV2ixSzSxzdwBQuDbtQ7hcOJGHIqq52bF5tFsVFDDoVXnsfJlP7bEHbdbgkYnV_gtbRABGPjdfM4aNTs1RDR17LH_dLrG-YhCtIvLD5FJaoGEJ_cBkJEq3cnsLdHYeXSjiSWDMqAOweEynG_MZh6t5Tf2-mqkdq07HnAyuLVbsmJtQh2Il_a1bxZ9laDgeha2Gd1H2RGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8HiLsxeTS_3dWm-sOVkQJ7Ohet5it8Rv6g22PsvpwvbarCwzyNUG8feK69gzNKgty6ooQYg0k57unoFqFUmejm5k3RF76bva9jubgrH_Yqql3ajun90xZE2P8itcxNV9O1w2u2kfMCHq7JMV2ixSzSxzdwBQuDbtQ7hcOJGHIqq52bF5tFsVFDDoVXnsfJlP7bEHbdbgkYnV_gtbRABGPjdfM4aNTs1RDR17LH_dLrG-YhCtIvLD5FJaoGEJ_cBkJEq3cnsLdHYeXSjiSWDMqAOweEynG_MZh6t5Tf2-mqkdq07HnAyuLVbsmJtQh2Il_a1bxZ9laDgeha2Gd1H2RGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=gB17e3s1zuib7TlGjmbcRgYKzB8Ee4cycLpVrFMSowojSgsvNWwoDe3re7DvjWDYN4wFOTsq0ffRR7mm_DM9DMGWjW9-ozkbHjods5NFH6wxcMpzl2V9OxJEdM__ARzvsGGj6SA9teLlqovzh4TDrdD45e3AHo09J5SDJCbDKCvNssg7iy-OqtafjY4m8tKVROCdIydAnpOWtDBwNGh67X9uegg8dK9mxNbUvB3108TDQ5wcIZV8hmYUvvxvXLmyE35KaOpeGsT3IkoL6RWw6LWLLCngceAnANTOmLmrjy1wyETmV3xPBfux-jcW3mD1WvAOP9p1oZG3zl9ehxRBQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=gB17e3s1zuib7TlGjmbcRgYKzB8Ee4cycLpVrFMSowojSgsvNWwoDe3re7DvjWDYN4wFOTsq0ffRR7mm_DM9DMGWjW9-ozkbHjods5NFH6wxcMpzl2V9OxJEdM__ARzvsGGj6SA9teLlqovzh4TDrdD45e3AHo09J5SDJCbDKCvNssg7iy-OqtafjY4m8tKVROCdIydAnpOWtDBwNGh67X9uegg8dK9mxNbUvB3108TDQ5wcIZV8hmYUvvxvXLmyE35KaOpeGsT3IkoL6RWw6LWLLCngceAnANTOmLmrjy1wyETmV3xPBfux-jcW3mD1WvAOP9p1oZG3zl9ehxRBQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMnSiM-LmQD9JnWMkhuB6XzWUGmTjdtyYasy4LP6L3Hd8e92es62RJxpSlq7vB8xA5O4slF4B53Ea0knMy_avG6rkD6uEtVASJOyzemMb52xiMhrwWcEOi6S-T8jX-AkrEsKs41dBnxE9V1TgmJ_vvIuG-3W9YdXkoUh2ZnlbDkTZ6hjm7k_99T_TYkCMti9NTb1AUTjGKrvJGlJNML5pJkJyorINZ97k_t416HDm0X0dU1EnBp2xLw82tAmNpP01Tar56u7Tev7kj_2dqES5V42xOPU48eQY2WGtTwQNDxyVQvdAZUln0JiZRuuKIUK2Tc9_zaBVUdiLtF-B-65bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=SVsbQnkM90GVKL1uRGjiVW9TczwvWExo_Osd8eYBHXk8LmajYmwRoQnrPs0yGZ-heP_BJ1_Siaz9hlTu8aHjLPjJRHxlRfXHIayXCaNLS8K8sFlpr-OC_qzj9LzQa0cMhF6aoj6sPbQ1-PKKAnj9EXQNOyGzhm0FEImz3ul-bqMidXUbVjKY61xYy0qXR6r1upZnqEPVPTkT2O6uMNuUbfUScOjTDch4fsh6pDSeDkKE89GKWEuXH16_tNs0BYa8zYzFVEceaZIZg054cmsdoIxOaeQxWbn8ruUlIY1khelJkjh-ovRWq-rosDzfbfV6cFiaCaLUVxLC8o1xCRFV_W5txITa2puEQpKv9sq5U63JveuDmtz_badEHx2HNQdutGIVg1JJ0oUZnzNA7ZkqzpDOxoAgaKkYOrTn6gD3iNv1vgLTUzUDN40UD3T2pHehPXAb13bpGcFIqKdxnNXXNDw_oXOGJ-fQL299brlsz6WhhgfyUiLKR5Kays3PbEJXe6DBnLvbMg2G0TnY8rhoGkUD7jnn_g-RKsLjmjsffmqIAGGTQYTYueAs1vVKkmXaG9XqgbxGImxkPmjsnsd6_gT-Q5p6AkPyRci39FcVMrm_6_14Ux31cqA2KhD6LgIhuklz45qvPiN9EtTgvu4vVqfpC4qvGpInZFqPfP-NHUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=SVsbQnkM90GVKL1uRGjiVW9TczwvWExo_Osd8eYBHXk8LmajYmwRoQnrPs0yGZ-heP_BJ1_Siaz9hlTu8aHjLPjJRHxlRfXHIayXCaNLS8K8sFlpr-OC_qzj9LzQa0cMhF6aoj6sPbQ1-PKKAnj9EXQNOyGzhm0FEImz3ul-bqMidXUbVjKY61xYy0qXR6r1upZnqEPVPTkT2O6uMNuUbfUScOjTDch4fsh6pDSeDkKE89GKWEuXH16_tNs0BYa8zYzFVEceaZIZg054cmsdoIxOaeQxWbn8ruUlIY1khelJkjh-ovRWq-rosDzfbfV6cFiaCaLUVxLC8o1xCRFV_W5txITa2puEQpKv9sq5U63JveuDmtz_badEHx2HNQdutGIVg1JJ0oUZnzNA7ZkqzpDOxoAgaKkYOrTn6gD3iNv1vgLTUzUDN40UD3T2pHehPXAb13bpGcFIqKdxnNXXNDw_oXOGJ-fQL299brlsz6WhhgfyUiLKR5Kays3PbEJXe6DBnLvbMg2G0TnY8rhoGkUD7jnn_g-RKsLjmjsffmqIAGGTQYTYueAs1vVKkmXaG9XqgbxGImxkPmjsnsd6_gT-Q5p6AkPyRci39FcVMrm_6_14Ux31cqA2KhD6LgIhuklz45qvPiN9EtTgvu4vVqfpC4qvGpInZFqPfP-NHUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ING5PGpfJjehJXXDbiqgvrRI9xCLBq-qw2irdMSMkasDY99CMt-ReNkBwGD4XAv1VTBKKSOnTC-t_IhpITNlXOban948ZejGlQh3xSf5qCzAto3pkxaYuv4ChKt8htP1wHlPYArwzLY4gaDt0HvFPS3JcTUIHyN1B9jCrmbPWk4hvwnuNNX-Fyqhj7LdVz280AgshppU0P2hf427AA257sy323WTrqDVZ0R1jUmrLkdpZl9Fd928k91eaicmwR2knIFa4eB7iSQiDU327yijMk8Gl8utu0_tc_ufvsSdIgE2sO_tqhFHDsX4E63cimIgTVh5erjYhDYYJuTiHMiFPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=FY9sNshU7PY3GyZHaPWYknsG551eKLPPVCAqTHCnmPgkQDDtCjvCebmKpe0st7eIJc8NjaGt6cxmH6M0gtBzm4XDRKon-j9C0KILoVD6M_bPOpYSfwG3D-_r56ZceFHR24zNH1DxRZo3MhH7_3lA29D8x5xxWDarRRwNS3kQ2_Sy__eP-GhMHukhl5w-1Ej78aRxaMQS2gt63oWBtwSWAoRciZWswp63zoawuI-XKTyun3VICrUs-p16jeM1CuAZPcstE-v9K4DTSNxTcXzvjnk9F6MjyDugEoUvIkfA7TXke05qzfJr_xbXLIFEECSyQ7_QCx_D4F1Uyk7NWNt4Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=FY9sNshU7PY3GyZHaPWYknsG551eKLPPVCAqTHCnmPgkQDDtCjvCebmKpe0st7eIJc8NjaGt6cxmH6M0gtBzm4XDRKon-j9C0KILoVD6M_bPOpYSfwG3D-_r56ZceFHR24zNH1DxRZo3MhH7_3lA29D8x5xxWDarRRwNS3kQ2_Sy__eP-GhMHukhl5w-1Ej78aRxaMQS2gt63oWBtwSWAoRciZWswp63zoawuI-XKTyun3VICrUs-p16jeM1CuAZPcstE-v9K4DTSNxTcXzvjnk9F6MjyDugEoUvIkfA7TXke05qzfJr_xbXLIFEECSyQ7_QCx_D4F1Uyk7NWNt4Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zp6SUfPADa5EVA3xVGUC8a16ruEj_A5vyl7lmejHq4YOy3aOpdoc6IKtpwgwiHkKNeuTnGD_ywdoLN9sDcxazQo9QVKSANCRCcKJ0p9zcHrtpsznwsXmCSHbe_qDqbHvuI8eFa7B-xXEyqE5EnpKOLS59N5aCnrnYmonhfmnLZQOvFrS4ktMR93Q02Nuy4MgC18efveCFEmL_G-C2wLa1ulbp1HriyxlKBkmqy2wMYkvox0vWBwVAUmX32t9XhKm_jNeJhX6A5XDuZB6DOS3kY2u5SEAtGwpfdLeQcPgyUCLLX0SxmnzlcE0CFG-ilKH3xSmsZFgyWaCffXAnD176A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqDh7UxDAyFx0nH83BkCyxusKNiOiFfp_TDu5kP7m42fXaCKkkrq0JTy2to2RnAXyYQM9Srdz4aoDZF3-S5NHdr8Wy7uqv-Dayz3ksq4jFYPCUt5Qt_GXfy85qaD5HZhJxth8ZKaMe6Tq9CaE-k7wd-TjIR6aUnldYOxkdd6AXXDCVNhzPyz7-9e5NtWJqq3733sz5jaQnzmvSeMXG7NPKHB0872m2JmoCfJloandwxpvrq91nog1rqJZMNGo2NAGZ0hS3PA-jjKHpu4e5mjBEZU4zBQUfV6v_kWNQamUcmKFRoQa-iZQopGjxaNrxn7zZnWArdQuxyxFCmYE5AjjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TF7iDNEEVNWW8Hnco3tyqs9C9CTWFQiCh6hPhic8GP4232D2Uu5MnFPF3rk5kEmBMkif87btrfOLoGne0kwqXbMbBK6qRgDP12SqDKYH60EJAPMOaC5gaWqI-Q2oLWxaemyxZppF9FuRanzW7orNgnKPOiJ1z2AK-qIzcsB_2R18eEc3N6Cupcm4Hm-J5eTklD5KRSHVYC5YMMrG9DGmjK8vbEbL1Ni3CAFpU0zktNsMajCeF5BfN9EWeoiYJA3IMzn_YB0sAbxtSZisRdJ2jYwaDn4FbS2DdX8G_RfSrl613KKtWZwaVNxqN0QffHx32j3AlHJeyTlbmck4EEc_IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=iW1q4hdExShYUzIdh4VLFeBe77sT514nbsxltFh8X3jvinuK-CTdUcuqaeMhwH8hIJa4CGOG_viCESiFQnr_kKeZ4CTISWs8wkeNm9F7RBEAQhRYkdq2qAtvjsjkX1O7NW8HhTbAtlNJIxubwgi3PGTqIXXPjMh1V3Hyi7CB381i_VHmrevTcuz9iBMl2j79V_afEp9FjHHWwdfCWf6CviIeJCho0JVV2RCPIKsNWpj8bA3u7Fa-5f71DaZk0nwiZkmKmcJQRuU-MINBL3pyo0HR8fP7_mCFPO5gTBQOr8Pzq6d85hKAkaJvIlZFpqM0ScJCBoSvI9J7TfJruLa1lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=iW1q4hdExShYUzIdh4VLFeBe77sT514nbsxltFh8X3jvinuK-CTdUcuqaeMhwH8hIJa4CGOG_viCESiFQnr_kKeZ4CTISWs8wkeNm9F7RBEAQhRYkdq2qAtvjsjkX1O7NW8HhTbAtlNJIxubwgi3PGTqIXXPjMh1V3Hyi7CB381i_VHmrevTcuz9iBMl2j79V_afEp9FjHHWwdfCWf6CviIeJCho0JVV2RCPIKsNWpj8bA3u7Fa-5f71DaZk0nwiZkmKmcJQRuU-MINBL3pyo0HR8fP7_mCFPO5gTBQOr8Pzq6d85hKAkaJvIlZFpqM0ScJCBoSvI9J7TfJruLa1lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d92YUBcoqUqjs3BaCcSSvMNdGuOp1uBTKymhApGrVJA_CC8NDJLiU5LTO_ljA4gHIsL44Nw_sDXEtI2UO4zfzKAG5vU9eXMuEWsebLqw1ji_5Xx1S5kRpepx8rJGq0Z5s1ZITH3lQgWzVXzBOlo5IAL2qY4nXtYc4VeY-5D76Mp43hxQmr7tLHtKZHu_o7m0FG1ezzUFNY-61JI92y2XHwsb48Ix8fJCAzvDJGLIntR_yOz6TJUgbGHYsLr-pWWuUlztHw_P5OEkK3Q4OdUaoTju-v-TS-NcYvcQERzzsDnkRHAihjig1bdsnckvSC2doeIrj8K4OyBcy8qIAV59gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFG67OIFZM-Y0mRhLGtAyyuMdCu46RAerNcpBbjEzeDH63QeOPqXnCKm7zTML96HNo4oL7d924ioWGC0MdqvBbvFkXl66se_dbW7Q7bXJ34xCSyTWkr1HMKKzHC8YocsvOWFpi3JNjTxZaM_1rd1iHTJI_3qnVBq917V_0xldthxrOwBwmAknC3X09QBGQdWMpumUc0rnLIFme7_P-n0PJj7-HtLwclQgNTIgczFAWkWBU1gAewjCcbSF4MG2ROft1PyyhXRfflY12XJY4Pxo7Zzqs70lf2nVxb8fkaeF-0fgGV8CwI3qQav5dDT8HAUVGzTT3ooEehXRHqiBS6DGR-I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFG67OIFZM-Y0mRhLGtAyyuMdCu46RAerNcpBbjEzeDH63QeOPqXnCKm7zTML96HNo4oL7d924ioWGC0MdqvBbvFkXl66se_dbW7Q7bXJ34xCSyTWkr1HMKKzHC8YocsvOWFpi3JNjTxZaM_1rd1iHTJI_3qnVBq917V_0xldthxrOwBwmAknC3X09QBGQdWMpumUc0rnLIFme7_P-n0PJj7-HtLwclQgNTIgczFAWkWBU1gAewjCcbSF4MG2ROft1PyyhXRfflY12XJY4Pxo7Zzqs70lf2nVxb8fkaeF-0fgGV8CwI3qQav5dDT8HAUVGzTT3ooEehXRHqiBS6DGR-I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=F57epQP5Oj5_Vzvu0qqB-FJeQxT1jRvXD4MdyYqJs0TvB5gaBfwz7OZdS2FHlm283sJr8DsvQaxFsb5BkbLH_dbuMGGwdItXORbfPvMYxFWJCt9Qu5-rRQgMq449ulAUUH4r8Gdra7dLCJA3xRoJbXmz71i3jSTvFJj5KsZiqeZb96NpxyICaiXAsQgcux1fDiJIftp2M0QfScP03xcHFyyDk-nLYjHbPALXhq2GbxwBDjkZZPIHwO4k2W_to2jfrYdNxzqmykbuxRH_UdexWsiybnsfV4wf1yqoqkY_3PdSTEw9UOKDlPRMOtJ-JxUvvarJXKmb5dMzEVu8ugtlAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=F57epQP5Oj5_Vzvu0qqB-FJeQxT1jRvXD4MdyYqJs0TvB5gaBfwz7OZdS2FHlm283sJr8DsvQaxFsb5BkbLH_dbuMGGwdItXORbfPvMYxFWJCt9Qu5-rRQgMq449ulAUUH4r8Gdra7dLCJA3xRoJbXmz71i3jSTvFJj5KsZiqeZb96NpxyICaiXAsQgcux1fDiJIftp2M0QfScP03xcHFyyDk-nLYjHbPALXhq2GbxwBDjkZZPIHwO4k2W_to2jfrYdNxzqmykbuxRH_UdexWsiybnsfV4wf1yqoqkY_3PdSTEw9UOKDlPRMOtJ-JxUvvarJXKmb5dMzEVu8ugtlAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=bc8wdY3jLThSWPL8-CA4kKOkIoS6TrpgJtY0w5dzih3X5fy_Ob29EUJFOysBrFgt6w6qEEBIqF0M2IB_hHuVAxFcJFrYbqisCY9re3CYaKySii5rftliGcAyvf5XdOOj4DLBq_4dg5FqokDMZoLwm8dXAO1OEtYil0YINaKUptfb0J-rQ1tIisl8hdAqpJd-5IIS37inpuoOQPS03r89_K0O-3ehf11NzQKDOToLwDYmqCGE9SZhSh4yoVqtCPS8ffYhRQ2kezLdfJXtspwgI5X_EUP5MYFOzRwvdffRunuU1TsVfJucjV3i_wts_0klhCA7zy5LkORUMcvKFiCgvYizIRoNO8N7INhW59mMlzM24Jt5hXsUSsJ7_67qbtQHYCG8OYrFhAjIW6MMmrxn66UmElWGJ2NRSM3fXmyEx5ucDRcX5Vr_5r5BhgFPVl316QYNlAP6Pebd67p0z1NjpyHKca17QV5WM4AmBNqfzUoNo9p-HnnFhX-0AXlDZOoGEuXeAM0j26JiDuKxqqRAbKsOVRtGljb3p-o-MVhuHmvXu5fyA_FyQ5D6OjOzfyluvkj2crdSuWy8m6r_YTAPUkK3cXuP6E50qk9sH0fCFqLQwl3f5lxEeWap5wDIQJ_QnuS1RMxPUMc6A12hV-n-4ANl4jBaCP9tw5PmBgUJv4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=bc8wdY3jLThSWPL8-CA4kKOkIoS6TrpgJtY0w5dzih3X5fy_Ob29EUJFOysBrFgt6w6qEEBIqF0M2IB_hHuVAxFcJFrYbqisCY9re3CYaKySii5rftliGcAyvf5XdOOj4DLBq_4dg5FqokDMZoLwm8dXAO1OEtYil0YINaKUptfb0J-rQ1tIisl8hdAqpJd-5IIS37inpuoOQPS03r89_K0O-3ehf11NzQKDOToLwDYmqCGE9SZhSh4yoVqtCPS8ffYhRQ2kezLdfJXtspwgI5X_EUP5MYFOzRwvdffRunuU1TsVfJucjV3i_wts_0klhCA7zy5LkORUMcvKFiCgvYizIRoNO8N7INhW59mMlzM24Jt5hXsUSsJ7_67qbtQHYCG8OYrFhAjIW6MMmrxn66UmElWGJ2NRSM3fXmyEx5ucDRcX5Vr_5r5BhgFPVl316QYNlAP6Pebd67p0z1NjpyHKca17QV5WM4AmBNqfzUoNo9p-HnnFhX-0AXlDZOoGEuXeAM0j26JiDuKxqqRAbKsOVRtGljb3p-o-MVhuHmvXu5fyA_FyQ5D6OjOzfyluvkj2crdSuWy8m6r_YTAPUkK3cXuP6E50qk9sH0fCFqLQwl3f5lxEeWap5wDIQJ_QnuS1RMxPUMc6A12hV-n-4ANl4jBaCP9tw5PmBgUJv4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=WQA5f9d9QcngowuBk0kytbtZlPhrgVLObNs0j1O9S3tvsB5zgqTjJP6-uPQCisHhQx4wAxeM-y48oln0AOHMbSVKDF4PMRFmd4poR197b6u4Qc6XoxJ1WhqzIC3Ub1bcrDoWyaGQ4xmYIv5J-satFq8A-WZ1IurGJMPv9Dgb4061BT6FDFF-WIJC6m-55QjwOXaRj1SovtkPxMFcmqMGFy7XvtmxkJqZQFSi0r3ATDAtBITDdAhYpBWso3tdvc_nG7kw8F0NnIDBgrATx7Y6JJKlYMHpB5kMgGIkoJ9VlngdW4-sWOwRh1fBL3tTNpJldaB1rQ6b7LlpXTFKUPvTjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=WQA5f9d9QcngowuBk0kytbtZlPhrgVLObNs0j1O9S3tvsB5zgqTjJP6-uPQCisHhQx4wAxeM-y48oln0AOHMbSVKDF4PMRFmd4poR197b6u4Qc6XoxJ1WhqzIC3Ub1bcrDoWyaGQ4xmYIv5J-satFq8A-WZ1IurGJMPv9Dgb4061BT6FDFF-WIJC6m-55QjwOXaRj1SovtkPxMFcmqMGFy7XvtmxkJqZQFSi0r3ATDAtBITDdAhYpBWso3tdvc_nG7kw8F0NnIDBgrATx7Y6JJKlYMHpB5kMgGIkoJ9VlngdW4-sWOwRh1fBL3tTNpJldaB1rQ6b7LlpXTFKUPvTjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhl5f5UM6Q-spkCah9Ujm4av_hlUfFJ4_wbIxuq-GCBDgggkeZyLeJqB7BeI8qDmweO5hDBGJxEgqtblp-Y4wj8H4no5802t2QCJUPdA8Pg_LLJ-OlEUiRF2vA7Pi1MhYoFMxkHSxdC_lKPwoR_7TvyR4Jf_ws6X8DHTLv9sDtAszOhuBiby_iVUUdZ7BnllpxjLHVDaPQy0NFKZwT4B9yPRP922CoGfXetdjqRIZESfeusKWhVb5QqPk0U9x3R5BnHXlIQO0wifS7xvgmpjTBXBnd9Kk2i4mkgTjwqSQpRL4_N0Eg82N9HyELkxgBoO0FBu08-XsjF6fuKA1E3n2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=pF1BAf7YjiNbb6Hyq8HcEsccP3MRbMpLoHFIorWLtrEUfNI-aeWjOPMsVpjz2aG-_ZdCl0DUnlGFTG9QWZBIEV8E42jHgYFgc5OJqNj8PpfF08BEWSUfXk77WS39Yc2oZbwESxE0AnghUhgk7grVfM_krKconvHIM-hSczOFOz0BwDUUhhjzJ0MpI6ZpBl7TYmT5NUkhBPMob4LVJgZ_6_2NnKLhMJlas7TC2svhL5FPNcyez7KP3kW2eeAG3PUi23vvJjoKfSMHFn4dxKf9c6QY8xq2q-xi1uuPhGpdtkG1-Mg9ShjOFG_vZCt6DkTnd45MtqTM2t_OaPvpUT9i2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=pF1BAf7YjiNbb6Hyq8HcEsccP3MRbMpLoHFIorWLtrEUfNI-aeWjOPMsVpjz2aG-_ZdCl0DUnlGFTG9QWZBIEV8E42jHgYFgc5OJqNj8PpfF08BEWSUfXk77WS39Yc2oZbwESxE0AnghUhgk7grVfM_krKconvHIM-hSczOFOz0BwDUUhhjzJ0MpI6ZpBl7TYmT5NUkhBPMob4LVJgZ_6_2NnKLhMJlas7TC2svhL5FPNcyez7KP3kW2eeAG3PUi23vvJjoKfSMHFn4dxKf9c6QY8xq2q-xi1uuPhGpdtkG1-Mg9ShjOFG_vZCt6DkTnd45MtqTM2t_OaPvpUT9i2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=CAbQ5SpNPTcUAlkeydkUjVoZU_SZuJ086BXkr6teuiMkNEWj_fk6tt8baigL7eziR429-kDU83Yo2qodamwrDmRqPI6j3XEWF3txTVvnKHbjzPxffLcz8ULHsO0QmM6cR2zOtLDhNjB8v_i2GWZnWhQ1NzYGjgmMGFiwTCk3Alc1xYshCyC2Xgwa8EJBSRN8wejid3SC3ETx-bA6pI2hgawnrR0X1RBIjJggWfIuaLrEw-1Wi1KezyoP-ZmQEzQkcFmyWOR1H5Eoa3c4ojqWM69s6S724wkKfRwRoCAAnOwnA_U9RT_l762C7OEvsSjGLH5iBMuuTofhTni8BGLj95mOXkm3QLGNC--U02HD80yJZSa1B9JlHtAIQwAr2qUE26ZU4bsAhLbM1Tp2dZYzC71GIMei9_Qj6dKYleh5kjv04kQHacDjneS-9rkRwwMjnD52ZG8vuVJolg99vr0oC1fN4JCmoOPCAQnipCiYKLXhJ8j31LTMAgaM3mpgTePyP7Jlav1h1fiMCzP4u565BZo9d-8gozXgVKimlvD6_KZFu_eH0qDhIUMx4V8ro0vZbuhfX_r3t7dTexz18HfCP7GiGUufnzlATFEwHP0JwHGjXHhbX59poHY8i1CR4V-7WP_kxc2gg2ZveafST8fTA9Z_H49F93H0IWPhh1YZ3I4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=CAbQ5SpNPTcUAlkeydkUjVoZU_SZuJ086BXkr6teuiMkNEWj_fk6tt8baigL7eziR429-kDU83Yo2qodamwrDmRqPI6j3XEWF3txTVvnKHbjzPxffLcz8ULHsO0QmM6cR2zOtLDhNjB8v_i2GWZnWhQ1NzYGjgmMGFiwTCk3Alc1xYshCyC2Xgwa8EJBSRN8wejid3SC3ETx-bA6pI2hgawnrR0X1RBIjJggWfIuaLrEw-1Wi1KezyoP-ZmQEzQkcFmyWOR1H5Eoa3c4ojqWM69s6S724wkKfRwRoCAAnOwnA_U9RT_l762C7OEvsSjGLH5iBMuuTofhTni8BGLj95mOXkm3QLGNC--U02HD80yJZSa1B9JlHtAIQwAr2qUE26ZU4bsAhLbM1Tp2dZYzC71GIMei9_Qj6dKYleh5kjv04kQHacDjneS-9rkRwwMjnD52ZG8vuVJolg99vr0oC1fN4JCmoOPCAQnipCiYKLXhJ8j31LTMAgaM3mpgTePyP7Jlav1h1fiMCzP4u565BZo9d-8gozXgVKimlvD6_KZFu_eH0qDhIUMx4V8ro0vZbuhfX_r3t7dTexz18HfCP7GiGUufnzlATFEwHP0JwHGjXHhbX59poHY8i1CR4V-7WP_kxc2gg2ZveafST8fTA9Z_H49F93H0IWPhh1YZ3I4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJvg3Q91amcETTifvYNWOD0NMGVplyObNy2QdJ8nOIpl_SRwaK4YJmaSHc82x8VlZ_o37xnHFvgHOnFdoavPPPdcGLTjmFynLpZnC6g-peT30-MqXYi5Jr1XM0AhIvQjvhMXHCuzufZLWLO5QLzwz0W-kVueaA6AFc6TSAXgx6NrigNue9tcQOcWBgbuv3kwcKZIR-oVZxUt3I9XU2rM4xp_rdtO7fbjM_rbFwW-yWJe0f_bhl1pn3llDdGTpDQss-uA4AAUu87xzAOSjVtaDhNEMdGULJghScUwMfhQNAopj1jMh5TIWLDliPA0v5AjHnQI3-h8W7qY79_HGWkDag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=oiFEPso46JKtFgzByUiObP1wcztMQAylwmZ24Ny-2RY_gJ8e6rsprvmgeliBwW6kN2GtpMn0fAXm1wXyD1Xphl4E0H76ly7c_8KLBLQKejEhOhH1eU6R4HsKnIbkmPygG6K7IbW0gKH4RDoFCYHCwrefxvgG3Xx68_rui-MfL9y_u7QVuXeOu9NsDZYKsHaT-lJPIwfHhNiikCHvEK6cZXhHUBIJJNDI2ZM5KybWha2w-6ClnC_yhFdg4GqpSVoPeYG7I6Z6InqK7GTPUptqj2Rs4F4dwFNw008P37Pi_F-6kNHYdZRQZi1F28XLGK0SaXW0Wkxu7AIBHqat8Rha9jhhiA-vpt4MRz5EjGmgkkyGGc5sAOs-1xhcqaPQ-06YjHNyZuREpi6cLucTIPo9iHhMuVjxPQS0gmnx3My4pgYd0xTsmmFfEuxmt5_d-3fADYD2pCa3VCekq9P3vLm2vSg6EcAGNhpsWLn6NcZHMYS2XQoVpwk8h5tDTKQgC9R5MldsvYVoEk-QyfVsAlLwQeBR_9dvlNFYsYRwuafXJ9CsMF8jONusj6jYveNi5NV8LENfDvQxq6K4z25k0ag_3VgWqhLjkvfdUD9b_X9bjHpxDydcajWxKMSd4mWOintLX9nFAJvOoZTt3cBA0Ypgy-YxRfuKjN-XNl02nqkLX7o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=oiFEPso46JKtFgzByUiObP1wcztMQAylwmZ24Ny-2RY_gJ8e6rsprvmgeliBwW6kN2GtpMn0fAXm1wXyD1Xphl4E0H76ly7c_8KLBLQKejEhOhH1eU6R4HsKnIbkmPygG6K7IbW0gKH4RDoFCYHCwrefxvgG3Xx68_rui-MfL9y_u7QVuXeOu9NsDZYKsHaT-lJPIwfHhNiikCHvEK6cZXhHUBIJJNDI2ZM5KybWha2w-6ClnC_yhFdg4GqpSVoPeYG7I6Z6InqK7GTPUptqj2Rs4F4dwFNw008P37Pi_F-6kNHYdZRQZi1F28XLGK0SaXW0Wkxu7AIBHqat8Rha9jhhiA-vpt4MRz5EjGmgkkyGGc5sAOs-1xhcqaPQ-06YjHNyZuREpi6cLucTIPo9iHhMuVjxPQS0gmnx3My4pgYd0xTsmmFfEuxmt5_d-3fADYD2pCa3VCekq9P3vLm2vSg6EcAGNhpsWLn6NcZHMYS2XQoVpwk8h5tDTKQgC9R5MldsvYVoEk-QyfVsAlLwQeBR_9dvlNFYsYRwuafXJ9CsMF8jONusj6jYveNi5NV8LENfDvQxq6K4z25k0ag_3VgWqhLjkvfdUD9b_X9bjHpxDydcajWxKMSd4mWOintLX9nFAJvOoZTt3cBA0Ypgy-YxRfuKjN-XNl02nqkLX7o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=tojjaaKOTjQuchvi2vtTBEcIFVk41DrDfjnaa1b-v-ieLQ8k5hDz08ItfCV6r6EI_hsgufWXK45J7s_F91fwtjxeoEs9lmQwJAtxt11HwP-ZGrJhBA6OzbczTyAha59k6RmMP62Ypaygv1Gd6YqKwEQUbAy_Xn5rYKIAdDqNa-jb1dEc8bW2k52rwAsHnz1MBK1uqwGdNV0lD1MLuCYCseIQECVyPZ-23WCyzyqMSnQiWQito3JbJnphNs46GMpdbLG2TB2OEtuXx5jyCbT4_bWrKF4brH8WVO93Vp_a8Jd9ZydmLC-NstCHRUpM176jX8mSV64OyrveAQOSq3VLpkvNtaPrGMUxeZUNyZs-8z55Jcndb0Qclb3Syf-wvq8yezpF3JRDSm8aTwM-SS-wALhEMCD9_7QvR0ER5u6vcHU2iJHlEfTSl5UIqRenQQNdkQXn--3cC70HvGjASMan2y8Kb8YvGUtfHuxjZQ3Ojcjl0BJkG-wWHtSQMkmkHyNyDfhXEIfgt-8lUDvXST8VCmhGMuEjvorMwvG_Tw8pu-alJwtsShWz10uU5eVbayWhLIvBt_JhMG4ywi1B9jZnjQTyGVR4a7rs7I2S0XhqVM21CaAEL65UZtptPK3rlxVNXkcM7UT9xMI48ibBhkZF08Ju2l2iwYV6Gjj7fyCiIeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=tojjaaKOTjQuchvi2vtTBEcIFVk41DrDfjnaa1b-v-ieLQ8k5hDz08ItfCV6r6EI_hsgufWXK45J7s_F91fwtjxeoEs9lmQwJAtxt11HwP-ZGrJhBA6OzbczTyAha59k6RmMP62Ypaygv1Gd6YqKwEQUbAy_Xn5rYKIAdDqNa-jb1dEc8bW2k52rwAsHnz1MBK1uqwGdNV0lD1MLuCYCseIQECVyPZ-23WCyzyqMSnQiWQito3JbJnphNs46GMpdbLG2TB2OEtuXx5jyCbT4_bWrKF4brH8WVO93Vp_a8Jd9ZydmLC-NstCHRUpM176jX8mSV64OyrveAQOSq3VLpkvNtaPrGMUxeZUNyZs-8z55Jcndb0Qclb3Syf-wvq8yezpF3JRDSm8aTwM-SS-wALhEMCD9_7QvR0ER5u6vcHU2iJHlEfTSl5UIqRenQQNdkQXn--3cC70HvGjASMan2y8Kb8YvGUtfHuxjZQ3Ojcjl0BJkG-wWHtSQMkmkHyNyDfhXEIfgt-8lUDvXST8VCmhGMuEjvorMwvG_Tw8pu-alJwtsShWz10uU5eVbayWhLIvBt_JhMG4ywi1B9jZnjQTyGVR4a7rs7I2S0XhqVM21CaAEL65UZtptPK3rlxVNXkcM7UT9xMI48ibBhkZF08Ju2l2iwYV6Gjj7fyCiIeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=f2Ft1LWrJwzl6VwcGxKXNTDbvyhKsNjsBhGYY6Z2fdqdPExr1maLb75FhiB4l60YcIkAqzKceFz5vgDpgn6GsUGLdF8y8ds97pVMsxin_7NsKI_01n-MH2t0JnZYXFe0uVQ3VAu3ba7s0fk6HIClkkdo8rq84yVyuPchGnlhLMWpytU4Kp-kFZiWWPNAJj8cGMVoM4uKL4i3NeuSCUwQTrPcJbQ_q9Vc4yjbwP39txc2NXBUACKOxDu49Iy73_sE6mS-s_dwIBTW28ZIj63yWdqRqm9gNQWGmv7Brx0-Xbqbs6affE5dHGqVRIS7ex71ib6q28gwn7243Te8BzbCWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=f2Ft1LWrJwzl6VwcGxKXNTDbvyhKsNjsBhGYY6Z2fdqdPExr1maLb75FhiB4l60YcIkAqzKceFz5vgDpgn6GsUGLdF8y8ds97pVMsxin_7NsKI_01n-MH2t0JnZYXFe0uVQ3VAu3ba7s0fk6HIClkkdo8rq84yVyuPchGnlhLMWpytU4Kp-kFZiWWPNAJj8cGMVoM4uKL4i3NeuSCUwQTrPcJbQ_q9Vc4yjbwP39txc2NXBUACKOxDu49Iy73_sE6mS-s_dwIBTW28ZIj63yWdqRqm9gNQWGmv7Brx0-Xbqbs6affE5dHGqVRIS7ex71ib6q28gwn7243Te8BzbCWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=d4dItrn7BfsxT4hvux0Xj2xQ0LGGYLRn-KtbJkeD3btn-3kt6OEeMYZVSFJK0bb6-mVuEck06YgWpXu-81_IyeLozc2-L2Zax0LyroBeZ_HnJ30xtQfAS15m1eab20TRlY7XONEPWdAKL5tROfY1CjKrNp-Y-xSGpcQFq5SvyU_MQyn6pzx-fUMM0EFsktATq5zDTBgv6rwLPL6rp85VqB3oQd-SQQtasFlDR2LVaKedyRk080PfVzA2rtCPdeMKlV0YEjMaJn4F_V4Dkt9WIOml1I-EMZhejuX8ru6DlzU4EgwZlvY9j4A-M67KYLFnxcr2vK-JBTAqn0mCCy1mRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=d4dItrn7BfsxT4hvux0Xj2xQ0LGGYLRn-KtbJkeD3btn-3kt6OEeMYZVSFJK0bb6-mVuEck06YgWpXu-81_IyeLozc2-L2Zax0LyroBeZ_HnJ30xtQfAS15m1eab20TRlY7XONEPWdAKL5tROfY1CjKrNp-Y-xSGpcQFq5SvyU_MQyn6pzx-fUMM0EFsktATq5zDTBgv6rwLPL6rp85VqB3oQd-SQQtasFlDR2LVaKedyRk080PfVzA2rtCPdeMKlV0YEjMaJn4F_V4Dkt9WIOml1I-EMZhejuX8ru6DlzU4EgwZlvY9j4A-M67KYLFnxcr2vK-JBTAqn0mCCy1mRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=JHCZtqepE3B67cWJ3xMsR7kDf0sSLGCZcoMuvziwqtWeSgPMMVCwsubu5RUO1r9DDo4cP6VC18WJn_RdkktjT7lz3dN2aaGcgSNSpsZv8eguK81F47ypBbqU791bpDFe5AiUx6Q60y4wyVtdZn37H1yU2GiGIb39c8WDupOCr-pvUng1uVZ8PDli12TG1gwkMir8_fzs74EVFt9DaADpWEOBQDU1zrU2VG0KaTcFeabjUHX2dLwcCC3TGe7WMg-j_2MjigGWEpcfKOQWO0wd_X0JEfscEIQw4ifWmONfYIVIQz-3sZR4MpmYc-53NR5szJDKHf0h72T41gD16CMRGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=JHCZtqepE3B67cWJ3xMsR7kDf0sSLGCZcoMuvziwqtWeSgPMMVCwsubu5RUO1r9DDo4cP6VC18WJn_RdkktjT7lz3dN2aaGcgSNSpsZv8eguK81F47ypBbqU791bpDFe5AiUx6Q60y4wyVtdZn37H1yU2GiGIb39c8WDupOCr-pvUng1uVZ8PDli12TG1gwkMir8_fzs74EVFt9DaADpWEOBQDU1zrU2VG0KaTcFeabjUHX2dLwcCC3TGe7WMg-j_2MjigGWEpcfKOQWO0wd_X0JEfscEIQw4ifWmONfYIVIQz-3sZR4MpmYc-53NR5szJDKHf0h72T41gD16CMRGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=ma43_CvtCxwXLvvKvFuyIMb4M61inTHYz1rk0OAVnoNFVVwyGPXJlMTU1f07f61DiLaJ1O5zeEB9ecksim61G1z68H0WKT4710zgNBrmjAAgC4mDesexFvvI-AhmssW2XtRXrF59qcEbHMLr-kfDqpvtgBLKYBHbn3dx7eYY--OFtotzC4WSuSjMccRQuK7pITnb8EklC-QqOk26E5lpGW9Wngtsr6g15xtRc3RHCXn55TNuCmUJ-aUhvqP1nM-ZRYFpBFWkuNWfe44SRTXl1bxNfeMVwYrXJsiRG_bAfzWQxYJdRfX6oPpxFb2oszE-YSPmtBW8ZSxQCicwopRysg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=ma43_CvtCxwXLvvKvFuyIMb4M61inTHYz1rk0OAVnoNFVVwyGPXJlMTU1f07f61DiLaJ1O5zeEB9ecksim61G1z68H0WKT4710zgNBrmjAAgC4mDesexFvvI-AhmssW2XtRXrF59qcEbHMLr-kfDqpvtgBLKYBHbn3dx7eYY--OFtotzC4WSuSjMccRQuK7pITnb8EklC-QqOk26E5lpGW9Wngtsr6g15xtRc3RHCXn55TNuCmUJ-aUhvqP1nM-ZRYFpBFWkuNWfe44SRTXl1bxNfeMVwYrXJsiRG_bAfzWQxYJdRfX6oPpxFb2oszE-YSPmtBW8ZSxQCicwopRysg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=XreNOdLjnZz3XhKblKVD0kLN8v7KsTCSSOOeBRILdB9W8cISwRe8eVIiMMcpn3v5No9X1LUpVhGcU7Y0xXQdZ-4yXG9lHYjCwZt3AGo7y0iKVw0f0VZUIZaxRd3WGNqEYZj3wTWtl_VXvju-pCgx-g0TEU12JRCC-lWEbUgz0Vzy1KEUJHTBZwhnNCj8d80CA9DJJ-ueaEs6ffpzDBw_-IjoTh6bD0aVBdqjIul3q_su-qHX8lRr81yA8C091SAiAvlasse2b9530NXwCh4gJhtEyowQstbChy9NexldZ8ZMEU4ko_F_DSWMRLn5LIW7OdMEG_xxAU67fol8jiRmmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=XreNOdLjnZz3XhKblKVD0kLN8v7KsTCSSOOeBRILdB9W8cISwRe8eVIiMMcpn3v5No9X1LUpVhGcU7Y0xXQdZ-4yXG9lHYjCwZt3AGo7y0iKVw0f0VZUIZaxRd3WGNqEYZj3wTWtl_VXvju-pCgx-g0TEU12JRCC-lWEbUgz0Vzy1KEUJHTBZwhnNCj8d80CA9DJJ-ueaEs6ffpzDBw_-IjoTh6bD0aVBdqjIul3q_su-qHX8lRr81yA8C091SAiAvlasse2b9530NXwCh4gJhtEyowQstbChy9NexldZ8ZMEU4ko_F_DSWMRLn5LIW7OdMEG_xxAU67fol8jiRmmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=nfgttCFihu2L-Gyy1tBciPITz80G4amS-hcx54xGoIls1l9nB6nUqIVgoom9L074UYSsdR48f7FRr79etSVGw6d_c32sJL_NOlgVOdOClg1P16mMAEHjoepntDX5LvNMt0vTzn8elFtS_SRYNTypwoEP871IIxGx0b0JyxEsCq3eau2xLza4NPjuX3W9zMAV_8K_XArgJuNs_iiZ1Au6RNU-_42KgqCceNy7KShGbghC4Ai-vqGQLbpyUzJ2h7iWwk6_R6WmpLkpmSwhME7A568fL9r3YAUTCRp7rJMH7rzHKW5dV-sBMWwQPxuTQ7XeUU0KuB2RujbZcXBDfEp3fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=nfgttCFihu2L-Gyy1tBciPITz80G4amS-hcx54xGoIls1l9nB6nUqIVgoom9L074UYSsdR48f7FRr79etSVGw6d_c32sJL_NOlgVOdOClg1P16mMAEHjoepntDX5LvNMt0vTzn8elFtS_SRYNTypwoEP871IIxGx0b0JyxEsCq3eau2xLza4NPjuX3W9zMAV_8K_XArgJuNs_iiZ1Au6RNU-_42KgqCceNy7KShGbghC4Ai-vqGQLbpyUzJ2h7iWwk6_R6WmpLkpmSwhME7A568fL9r3YAUTCRp7rJMH7rzHKW5dV-sBMWwQPxuTQ7XeUU0KuB2RujbZcXBDfEp3fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=MZg8jY5k9TMhPzjYyHs5hvd1ByjHOFCiCUMme6foRMyTH7AE2lk2jc4bqYnO2g9E09ipQbYe13rftT9KWKUBlV6L4aG8t0xf8JPtxnma_-aRyFA6f7ImMV1WAhY1EBMAZnb5Sefvgise8mRgMDN630C5tiyKsRotSr9DDi5qhK4dGVBGeYWTQfQZ1MeezDNyZECMZBBG5Dy01JaM_gevw9qPf5g7VmCCCt5Bnlk5ej9I9DxbkvsDbe5hqor9fAjtc4j4eA8FSEPEDctL4tJ2GaFH4qSXC4iPlASUuFjlbydafHwOh1Wu3WHnYOInLYxzqNI5Nqoirh2OQU6Z2IT45A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=MZg8jY5k9TMhPzjYyHs5hvd1ByjHOFCiCUMme6foRMyTH7AE2lk2jc4bqYnO2g9E09ipQbYe13rftT9KWKUBlV6L4aG8t0xf8JPtxnma_-aRyFA6f7ImMV1WAhY1EBMAZnb5Sefvgise8mRgMDN630C5tiyKsRotSr9DDi5qhK4dGVBGeYWTQfQZ1MeezDNyZECMZBBG5Dy01JaM_gevw9qPf5g7VmCCCt5Bnlk5ej9I9DxbkvsDbe5hqor9fAjtc4j4eA8FSEPEDctL4tJ2GaFH4qSXC4iPlASUuFjlbydafHwOh1Wu3WHnYOInLYxzqNI5Nqoirh2OQU6Z2IT45A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOdTpO4kdjOAYTqph56i_6QWubOPupPgHDg-NO6FPEpsPPuN_UtFzPTPJEPZbeQEz3xaA5k8yPcgUTJK4ewlXd0kuP-8NEMAvPRn6BdVA9vLTtkub09t55-iLiSlXIHAa5h8ox-SJTo5wnnQbDmIQ5FkKDKGhsasGInJaVqqX032nlH6J5NFRRj3p1LQ4KsXIAZG4TJoTzaOn95J5SrhQVyYCgs_KrV7atkcm1PliE48SdH9ieXWC14TRAugLtrREJhtnFmKfiUP6LeupF96yF4ZQyjFXmymLprAlUQwEorc1WKyokOirX_haECMAwCRSm1iB30ziqXHozD05t2xLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Y6XCzez2ya8TunxAipTiY-mhl0Cn4qEXAGbPPKceworPAAIYCDNmfnO4roBvG6v2ZUs0CFsjGSmbkrO7Y6rFrY15q-GKW44BwRcp9BGqAg25RRWTTlvJcfvTKutH3bGdXcdmz3XGKZJIQdD-AX-MMeroW4-OmltmmpU3cMxlqHg8SCquMQSFm5nMT40-Or4S5zYXGZzfb1Ac0SIK-eoqeXv8eN9efvQGwf3J-9SaPCt1Tq2KIE_p8eCSXZ0BFZGEVszHgg4fJbXeNgeJdD7WvD9q8JL1CGEUobfa80qQLBJ33f8b7YsMz24QsgQ6cTroQUZo7fQ1UUdZ8t6gS7ir_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Y6XCzez2ya8TunxAipTiY-mhl0Cn4qEXAGbPPKceworPAAIYCDNmfnO4roBvG6v2ZUs0CFsjGSmbkrO7Y6rFrY15q-GKW44BwRcp9BGqAg25RRWTTlvJcfvTKutH3bGdXcdmz3XGKZJIQdD-AX-MMeroW4-OmltmmpU3cMxlqHg8SCquMQSFm5nMT40-Or4S5zYXGZzfb1Ac0SIK-eoqeXv8eN9efvQGwf3J-9SaPCt1Tq2KIE_p8eCSXZ0BFZGEVszHgg4fJbXeNgeJdD7WvD9q8JL1CGEUobfa80qQLBJ33f8b7YsMz24QsgQ6cTroQUZo7fQ1UUdZ8t6gS7ir_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=uQpyWzTijQJdqePkWyn-RyThaM0qS_wxoqzly1sWKJFTWFXwg8qJ7aTIw-yt5KV1xR_b7H2DZb-AQvVjRu18rLWvPFn3f0IhLG0lYCFmZACEwGK4OOt8_0A99nupX7dBu4D9shmMupsgjnpaaZAKCW1H4clluHnZaQ8PGdzhyhhyySlZikFOrfVvynR7c01wQZqs4A2TOvEgRoS1yE2vtzO2f3gBFrcDQx-1MtqCzpNKY60QSrYoJhJd6tyHsQCpR105gEIE2XoP_mcJDeSYupdpZbaoUKCim6pQJwDXBZ-GkAlpCrF57cK2o7uEg_tiRpaBedU598h2UlOmnngZhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=uQpyWzTijQJdqePkWyn-RyThaM0qS_wxoqzly1sWKJFTWFXwg8qJ7aTIw-yt5KV1xR_b7H2DZb-AQvVjRu18rLWvPFn3f0IhLG0lYCFmZACEwGK4OOt8_0A99nupX7dBu4D9shmMupsgjnpaaZAKCW1H4clluHnZaQ8PGdzhyhhyySlZikFOrfVvynR7c01wQZqs4A2TOvEgRoS1yE2vtzO2f3gBFrcDQx-1MtqCzpNKY60QSrYoJhJd6tyHsQCpR105gEIE2XoP_mcJDeSYupdpZbaoUKCim6pQJwDXBZ-GkAlpCrF57cK2o7uEg_tiRpaBedU598h2UlOmnngZhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=Pf0FYPpk1mwNAIg7_I6YdYI98uEdp-RISDnbfh0CtnlFlpPoLc_Omi9h_NjiAJYo2w53hHge-qVeY8WY1eLIXHC32-s0wH8pQfam4w1pQ8LQ4-sva1A0eUFBuewesG-hCeXIwlJVcgrRnaXai-iCipEwNnBBV9Q6CFAz55X6cPtcVV32zV-PapbexawGmrImfY_YtPrgH-ao9PJqEWHmIDZ-Gyf6FfO62t8MpvJWYASZLrtNkR8McoLGlt3MPWf11TTPvnfyGcNhLgUkSrSO7VhwOZV0E8UZmyPd30ASMzsd26Cy_Cuxrqieuq0309BNeaMgPxXgoWAU33IlrewfBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=Pf0FYPpk1mwNAIg7_I6YdYI98uEdp-RISDnbfh0CtnlFlpPoLc_Omi9h_NjiAJYo2w53hHge-qVeY8WY1eLIXHC32-s0wH8pQfam4w1pQ8LQ4-sva1A0eUFBuewesG-hCeXIwlJVcgrRnaXai-iCipEwNnBBV9Q6CFAz55X6cPtcVV32zV-PapbexawGmrImfY_YtPrgH-ao9PJqEWHmIDZ-Gyf6FfO62t8MpvJWYASZLrtNkR8McoLGlt3MPWf11TTPvnfyGcNhLgUkSrSO7VhwOZV0E8UZmyPd30ASMzsd26Cy_Cuxrqieuq0309BNeaMgPxXgoWAU33IlrewfBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Ms5zX4eMKd9SVNK42TZwy2k0frfjs1miZcolstKO38EXj8ay4j85JfEnvNtza8i6237qg_vwu3aTteXw0FqTNRCQU95xg7CL9tquc720aexqgXT3_xPgeC1KRhUiQZY-FTtj5lHQ64sMhVbDSwMBalCzmggZFLgPuJdfl-kVAu2_gLWrW873anjNGcy7kUtZVZThMwh-gKstSXhci2V-G96xi18GJE54-7s1KELX7VwEA3m1_Q1ZUlcSBNaqtkrdlbQkQZZ1Zbqxy2_Ot7omtkq5zINuLH9WIMxrsLU_6ClZmp2XrZ2WHAKctAhFJa4JOlxJHmYvh4_q-hMs1XEbPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Ms5zX4eMKd9SVNK42TZwy2k0frfjs1miZcolstKO38EXj8ay4j85JfEnvNtza8i6237qg_vwu3aTteXw0FqTNRCQU95xg7CL9tquc720aexqgXT3_xPgeC1KRhUiQZY-FTtj5lHQ64sMhVbDSwMBalCzmggZFLgPuJdfl-kVAu2_gLWrW873anjNGcy7kUtZVZThMwh-gKstSXhci2V-G96xi18GJE54-7s1KELX7VwEA3m1_Q1ZUlcSBNaqtkrdlbQkQZZ1Zbqxy2_Ot7omtkq5zINuLH9WIMxrsLU_6ClZmp2XrZ2WHAKctAhFJa4JOlxJHmYvh4_q-hMs1XEbPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/up41wg8-u6D3Qp4_TUcNzvmVrITW_DIeFGRRL4cwA8lbxXl--S8HuIdtB5Y1TlaZY9AoevoSl1yoViU5l7WCzEMlVrkvETfs7gXfQ1YsZSYCJvd-SNduCVstxoB8ReuupeGYiWKcXzBAKbOwjP4yWP_5IIyylPWPeUQqbeQSGFCW-acAJ-E52iocxbk-07QPEU8G6by6MAho1D5WwWdX6h3B40oDZBdDCKLNDMUDML6sAK1Y_0gwSF4e1FPWSd3BEs7j0EQFOZ16rNLNNYfDeLeuN7-Yt0IQh_Hu4-wpndW_MJQUJwfy6nTr62WVktZnKTMdRMc9STt_BqLn_X3Pyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=YAiukFcayatPyc1RDv_eZHdi1YLPbFHuZJA9TtiP10klGshDA4gZEcGLRE92p5_L3Gb5OyEFy6rtsrJvg3oKew6jC1Flxceesv2GgIcxvQi8BndKbHub-gIRJlFiFomeOg-Duz6m3cGokeHcRXmR5W954T1WF0li-n-7e0BIW5BiX2ErHjwYBH_WDbayQK4cd6_Xf6F39egDVwVSyeZXACBsxEm-VXaMeTvaalF06W4L9x0aLFwcW4y3JLL1RMpBhHMThD4dA1TNbIZShzlzWqng3XYU2N4WvalbxGlVMRVuClzeut-SmJcqOnw2_EcFi8hdLHym-4sGFCxLJpkOGoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=YAiukFcayatPyc1RDv_eZHdi1YLPbFHuZJA9TtiP10klGshDA4gZEcGLRE92p5_L3Gb5OyEFy6rtsrJvg3oKew6jC1Flxceesv2GgIcxvQi8BndKbHub-gIRJlFiFomeOg-Duz6m3cGokeHcRXmR5W954T1WF0li-n-7e0BIW5BiX2ErHjwYBH_WDbayQK4cd6_Xf6F39egDVwVSyeZXACBsxEm-VXaMeTvaalF06W4L9x0aLFwcW4y3JLL1RMpBhHMThD4dA1TNbIZShzlzWqng3XYU2N4WvalbxGlVMRVuClzeut-SmJcqOnw2_EcFi8hdLHym-4sGFCxLJpkOGoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=NPnjeQxEQW6U-EBE9qozGPVUBUud5-lONjbrapQZAJVES46BFn50EHLcwCsbGBmlL673fcoinqqK8OSBplwbJqvLlOIiWlklgEEaqjDrjxm1nIfanSXCRkodTL-ahe6O0aAqoFY3kld7L89pnFyIR9I2Zh8VaAikc7iU2CSi21aZS3_IVs2Xp8LDkSglyxMk4NoFQSqCdSQlsnJglg7-90nxNN_cHIKOUUC9cT2Ha3EKkX06r0RRrMdWucg7o-hnyLFzyvLSFdVOGJ7ZnnAWiZ2gPAuRF3d_Vu7w7pfLdPs2SlBfLGwovn9SOHCqeH9bqPU2UZbmL1-_GJI0qrU90w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=NPnjeQxEQW6U-EBE9qozGPVUBUud5-lONjbrapQZAJVES46BFn50EHLcwCsbGBmlL673fcoinqqK8OSBplwbJqvLlOIiWlklgEEaqjDrjxm1nIfanSXCRkodTL-ahe6O0aAqoFY3kld7L89pnFyIR9I2Zh8VaAikc7iU2CSi21aZS3_IVs2Xp8LDkSglyxMk4NoFQSqCdSQlsnJglg7-90nxNN_cHIKOUUC9cT2Ha3EKkX06r0RRrMdWucg7o-hnyLFzyvLSFdVOGJ7ZnnAWiZ2gPAuRF3d_Vu7w7pfLdPs2SlBfLGwovn9SOHCqeH9bqPU2UZbmL1-_GJI0qrU90w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e4NEavwCOregCHt0Dc-m5NzRYyGKjSWvjRu_VpbRadIIqiYLFa0XGbd9EXGmSq9mMPIgXgxhXpdiF87jiDLbyJK1ZJ2rSbfvbkDwAGYIuW7TxEUKBVKSWb_xUdkeKw4mihBPblzMJ9IM30NzrJks0HXs0MyCuDLnr-Yns0bINt3TkzXn-_cpB5wbtvC8bx8NhLpNs_OY2k76aKM4KFSKte1pzovdRMUI6D2LtEn01McMEPetx7sLFm6APY14t9hQtUoxrLrYQKJfZoyhPcRwM2-R5yJTKA7LTbqyjtVATdGZEY5aFekrs1a1lH6HoaVvTd8DtQYZDHUP_GkfzD31hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SWLFkX2Fwf8CB0zVXjyCP9MAhmxD3hvIN5gwtshxPknFLCcRetNzP0Y8q0lQSX-VugQzLqeC8LYUo3egxFXUSogFkEOnzmmvdDNWp465SbYmgAgbKh-PfKlznF5lLt0cBmvgHomeaMxLqhSQ-UeGLLLVhgi18CPu167sZtN24KGRkhgJQtVJVZIsIo9AeZZK4UmYI42MwXqgruRgI_WVc1KQgELZpWOt-QILE8Lbds0YfexQkX_ZS-qFCxDnh_mzmlAU2xsoGYSjMIqPFu3zr2nutn4JkbfEAKqb-byGAZ-tCJSf2WUXOOP0G5I2FY-AbcfrM4gpfUU6KRByPtCBZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=mN0gTuWFoyk9URO0-TyZXjtE7bff0-yHMIpf4pCioU5AVk4DTvKIqPz5t8uqWcs0VXDlFKj1K0C_Z4zDF6zewAc8R96v03rtsZW_bUiL5lRs1kPgoa0vVKvNDWVolXL_HVHfRf9Ie0zRTdXG8PPCmFU316-CKd3guhrUNDWA1qlSP4G4eXvNs1gBKfobMoYI553f4ckUOqRWMRk-WGmiSLPcdlFHjA_bEuekb-yG8wNWN0t2bQhTd-8jK7s6ceYU580cK0eIve9QSTge4UqkJZS3Tg3xCkHvnqH7VvOqavGuEVxWVClZg_noWwXUqjSpoDxoobs12u4F-reYyiYakw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=mN0gTuWFoyk9URO0-TyZXjtE7bff0-yHMIpf4pCioU5AVk4DTvKIqPz5t8uqWcs0VXDlFKj1K0C_Z4zDF6zewAc8R96v03rtsZW_bUiL5lRs1kPgoa0vVKvNDWVolXL_HVHfRf9Ie0zRTdXG8PPCmFU316-CKd3guhrUNDWA1qlSP4G4eXvNs1gBKfobMoYI553f4ckUOqRWMRk-WGmiSLPcdlFHjA_bEuekb-yG8wNWN0t2bQhTd-8jK7s6ceYU580cK0eIve9QSTge4UqkJZS3Tg3xCkHvnqH7VvOqavGuEVxWVClZg_noWwXUqjSpoDxoobs12u4F-reYyiYakw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPLqisey5u08dYSsyXiEKIhnO2OhYjDdFcYXB9TvCghZ6K4rxgwH39aXfs2tVqLASPh2yBseIOMn39XU8dUImX0y6wKlB-H1gC7v8tFQwCVv6CfIcYMOL6sDuwT4fwLpVZNyTWjysUkiSGi8_fPT4WThIElqFDhTzdokzhm8E-pifFBlX1YvYnjBquYcP4tMo4Gg1HSm_QSsIbLVeGG9rfAR2bjud9vvjyQH23X2s5tRs7ZyyIsSDde-AT6CaNuJdDscn0Tz72ke1ZlfgPdJ2KjKWt30tYrWVRfvLH57vJbYTEU9tkKkSKC4lNQlCn_AbW23oTBtpE3FMtewQntrOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdah8A8z-Q-HYtdf9Dq84c51ZDBKT5pd-NCIww28SDEZi_X6_dHLAfd2_N5axgCk4_tozzZm1u4bP-SLKtTUM1EFNtqArwITqc3LVUiv9TXtkqkdL0n7BbJ8qEx1dKo6wGumvfeEq2XaL6Kh8OI8xrJlrwMONVk6I_y87CnKn2XXm43-IcyzVRewKgZBeRIaSF1zjfEtY6wYdaAk5sn6w4M3_LIsCme_0v3Wbz-NKa1bB8BCU7RzWi__-RXq9YyL9Iy666nBIbN1RFhrharPiLt3qy9Hvf3MYzLztOYqpU5Qk7DQtwDG8bS-XVGR526tGZJy1UgFzgGl7EZKroVuxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNEhcBDP1tGqkIAv1ElaAlfs0C6zf6sLqyb5d5PV_3htUj5XtRBOFTOi-f7U4NBfYa0G2QY6PVfKTWEcSy1zwy8xoEHdUwyyMeXiZhKG0hIAFQJXmKZX6OMFXl9jwyuhD6CnEalCg0wyI7jo_9-j_LL_hs8u64U7eIdlyoDNbdjsUIutOyj-apG30Xv_yey1DVnmaBqS49eX8fzVhEBgPnyrsmJZs6VSCi0W80bIu4zXzZcJlm_BNuTtQp4IET0tLx80sSnh39CZaXGBx0-SY7hDWFX31Ok52JBRLYFfvaL6dlb8B3XzyzLZHQ3UbgyU9R9E7CpiSSvZUzpzH3JydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=CJ_vxXpWUaCZQMXPF4mEH7CHzoP2pfKZzdw4MjKxoBfzZrodTEUeNxPuAI8mdPs5uvrkvL1JxPLJnChC5tVhMoYBkWRfh5_b4ujDrp2bWsVAcy4MonOaZL7nYQRHCgL__-ej6IgEAIKmrrVSpUxw3ExWLN3pm2K1UTSg58G9pWIJe2CgAEkYaVYnFIaMCACvVaAMF4IySgF5a99IVaG7MUyiGCFzXzImE8DUfCFuS6l5DdC5z_oaJ6XvpI1Vj8XcmsXorzGalRoqeNTleQ30hMN6qjC8cATEFyZEFJGjdi47Ooc8CS2lPrui94RZAyaRzVJfnrpUuhZFnOEQhOBGcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=CJ_vxXpWUaCZQMXPF4mEH7CHzoP2pfKZzdw4MjKxoBfzZrodTEUeNxPuAI8mdPs5uvrkvL1JxPLJnChC5tVhMoYBkWRfh5_b4ujDrp2bWsVAcy4MonOaZL7nYQRHCgL__-ej6IgEAIKmrrVSpUxw3ExWLN3pm2K1UTSg58G9pWIJe2CgAEkYaVYnFIaMCACvVaAMF4IySgF5a99IVaG7MUyiGCFzXzImE8DUfCFuS6l5DdC5z_oaJ6XvpI1Vj8XcmsXorzGalRoqeNTleQ30hMN6qjC8cATEFyZEFJGjdi47Ooc8CS2lPrui94RZAyaRzVJfnrpUuhZFnOEQhOBGcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=ArrsKA5DDCF6Ak81F_WA_0wQ2izR4RXA2uyVYD6wtk5vDtusGFgI97X5yLONjC0klzf5jPwINKYNO_4NihchQR0pgC4p9Ug9IrhgVLgb8V7sjUGxOb7Z8RgKtkGKKGKeE-QwozUjC2v6xpzLghXgE_BfR_wshDL0eycac7TTL8YlLWVjW6QpAEYUExZagAZGfCYXoNTfcjp7btBAHwQCbHW4sOBDF_ddcVEtIZhEDxvlvRPeSYw5NshlQgCAms9seUeOOPj2y4L8xcKxVXI0ASukk51qJulSYCZhii_AFpLIryOKa76DHXlKPs5rY9gzNlIofxQ6a1iXm9fFNw44Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=ArrsKA5DDCF6Ak81F_WA_0wQ2izR4RXA2uyVYD6wtk5vDtusGFgI97X5yLONjC0klzf5jPwINKYNO_4NihchQR0pgC4p9Ug9IrhgVLgb8V7sjUGxOb7Z8RgKtkGKKGKeE-QwozUjC2v6xpzLghXgE_BfR_wshDL0eycac7TTL8YlLWVjW6QpAEYUExZagAZGfCYXoNTfcjp7btBAHwQCbHW4sOBDF_ddcVEtIZhEDxvlvRPeSYw5NshlQgCAms9seUeOOPj2y4L8xcKxVXI0ASukk51qJulSYCZhii_AFpLIryOKa76DHXlKPs5rY9gzNlIofxQ6a1iXm9fFNw44Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=VHf2CcBH-D2C_rGfdGLcNcklsWLBp3TvXbg9lW-Vuie4laPn5n38HW9wD3FbZJGWjGLevt1ujCQStM--sU9FJ9gQ-NmpSs2XcileY73KCB9veeIfVJF2otOCpoTJ9wfNYSjKHtGiIPJ7ULPMh8SG9Yw6R99H1X20PkyEEFZrPYrzE30RH3_m9ocNEFkEVB5nEYGyVStFV11o32Tchs7LvD11eUg1uHdtEhcGcZsqf2ubyID-U_6_0qoRLuU5sIqdnJs-XKZ2E1K3ML3fEAZp7mlshI2kvXaBjedK2j6VXGdF5LgPjgnntl-LCt38S-35CyOc7bYetchAlFv-hDF1TTin7ab1uqtRvoGsxWju1Xs8RHthmS809kX6XSXsw-QUjrafYdqOwMCyft9NJhYpL3PVJL6tABBbz6KRZeeB7riUUbIbIZfMHAkgt9OGVtWUasXOxYULz3NYpEGc8hDWBnB223xWkLTjMvrJGTdd-jEFPt68jeLBb0comcdNtyuZ79chSRu6PM1CSTgKJgJt5C3u_8zMr5XZLq3zsla5jboM7N9dkpPceCqo3Iyqixtz-oaluN_SKQrirMwLV8oRl8lY-XFIdzx0XiBgwVoMjWd_TXtwwQBwl8QOVK1IQP9G7ZOtH3iWv-poiBv-SzdOy9BuTXoSeeYA1QHjwSTSAdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=VHf2CcBH-D2C_rGfdGLcNcklsWLBp3TvXbg9lW-Vuie4laPn5n38HW9wD3FbZJGWjGLevt1ujCQStM--sU9FJ9gQ-NmpSs2XcileY73KCB9veeIfVJF2otOCpoTJ9wfNYSjKHtGiIPJ7ULPMh8SG9Yw6R99H1X20PkyEEFZrPYrzE30RH3_m9ocNEFkEVB5nEYGyVStFV11o32Tchs7LvD11eUg1uHdtEhcGcZsqf2ubyID-U_6_0qoRLuU5sIqdnJs-XKZ2E1K3ML3fEAZp7mlshI2kvXaBjedK2j6VXGdF5LgPjgnntl-LCt38S-35CyOc7bYetchAlFv-hDF1TTin7ab1uqtRvoGsxWju1Xs8RHthmS809kX6XSXsw-QUjrafYdqOwMCyft9NJhYpL3PVJL6tABBbz6KRZeeB7riUUbIbIZfMHAkgt9OGVtWUasXOxYULz3NYpEGc8hDWBnB223xWkLTjMvrJGTdd-jEFPt68jeLBb0comcdNtyuZ79chSRu6PM1CSTgKJgJt5C3u_8zMr5XZLq3zsla5jboM7N9dkpPceCqo3Iyqixtz-oaluN_SKQrirMwLV8oRl8lY-XFIdzx0XiBgwVoMjWd_TXtwwQBwl8QOVK1IQP9G7ZOtH3iWv-poiBv-SzdOy9BuTXoSeeYA1QHjwSTSAdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=UdeDx8pIZGJWsPlmFp_B0u5zpfpydKwjAzYLbjswcSSyiXeTBEb3fC3M2-fSFH4iENbYpSxf2NPT6rNVBMYx4WkC0WzZt0X_TMzruHueZzwlxnfXZgdHsO9mSra4P9_shMyLJUMY47Q_GearlitGD_O5QLePX-aKuwjAlX9OoJXTxW-kdic0ExfO5hUZoepdlaG6nW72GySavDhtl7Yb4yPllSgZDqB9tj6spEHQ0kH1FBPtt_jZaObqaT38IsONDy28lh80Xzk3t9lJLG1iyIeqcqzeaFeoml3m0BsnlDyhiW1sW576bF3dIRHUtJNWemeXC4F_Y39sr3hsLehTRkTqpclEP4dunlbzAzG3YjEsF4VN39QycQsnKslCXfMVre0yutx9IYg56QvbDuOA_jBHW2O-79jexB2XQr8CWN8g8eno9xbi30kiwlJajpQ5Sk_s8AP12aMN1G_eNGiB68BBEzaN7DmMIQqXjyMixyyJv_9vC0d9rA8duG5J2N-aARs_Afwx1R5-E1Ni3jK5hW7pW6Ldf4kN3A4EaaVIBDLbZuIegAEpd5j5cqwl5NfdNb72qdRnYefGJpfVYWs2YUbpZuC6UZKsNnu2t1FE60hFnmx0SH_fB3dWNUBpgQQTxkJ_br-kJjJa1owYkOLa2qLMTbrMwSoCsbywoA6iRUM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=UdeDx8pIZGJWsPlmFp_B0u5zpfpydKwjAzYLbjswcSSyiXeTBEb3fC3M2-fSFH4iENbYpSxf2NPT6rNVBMYx4WkC0WzZt0X_TMzruHueZzwlxnfXZgdHsO9mSra4P9_shMyLJUMY47Q_GearlitGD_O5QLePX-aKuwjAlX9OoJXTxW-kdic0ExfO5hUZoepdlaG6nW72GySavDhtl7Yb4yPllSgZDqB9tj6spEHQ0kH1FBPtt_jZaObqaT38IsONDy28lh80Xzk3t9lJLG1iyIeqcqzeaFeoml3m0BsnlDyhiW1sW576bF3dIRHUtJNWemeXC4F_Y39sr3hsLehTRkTqpclEP4dunlbzAzG3YjEsF4VN39QycQsnKslCXfMVre0yutx9IYg56QvbDuOA_jBHW2O-79jexB2XQr8CWN8g8eno9xbi30kiwlJajpQ5Sk_s8AP12aMN1G_eNGiB68BBEzaN7DmMIQqXjyMixyyJv_9vC0d9rA8duG5J2N-aARs_Afwx1R5-E1Ni3jK5hW7pW6Ldf4kN3A4EaaVIBDLbZuIegAEpd5j5cqwl5NfdNb72qdRnYefGJpfVYWs2YUbpZuC6UZKsNnu2t1FE60hFnmx0SH_fB3dWNUBpgQQTxkJ_br-kJjJa1owYkOLa2qLMTbrMwSoCsbywoA6iRUM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=hD6LgslPJLS3PMcFXiKzz0EOe7AwKRfsKMDHuo93Lselmv71trwnZm5z28nC0UXKsptlGxkdeK0IGcE704ij46CBo-6426R2L2zxzqrdI9q_YeEgQjwTVh82krUwZm9OgDx61AJj79srPCDwKOj60V2bzBkdQukzWm5eB3p6lTWz8ng5zsD7-LovPFz4u-ToX5zqsZILNc1hFmTr-LxFVjQMzM_bdRfQmot3R6ww1Nq_PYZFjMJHJx1XcZgFLdWlrtcMZpfT6uWg79xvPWS0ED1A0bPpvDovIQfFmh1XDvFY4nvyJWBjSBcFqhWfFlC_qlBj36jqzde5w3G36lH1qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=hD6LgslPJLS3PMcFXiKzz0EOe7AwKRfsKMDHuo93Lselmv71trwnZm5z28nC0UXKsptlGxkdeK0IGcE704ij46CBo-6426R2L2zxzqrdI9q_YeEgQjwTVh82krUwZm9OgDx61AJj79srPCDwKOj60V2bzBkdQukzWm5eB3p6lTWz8ng5zsD7-LovPFz4u-ToX5zqsZILNc1hFmTr-LxFVjQMzM_bdRfQmot3R6ww1Nq_PYZFjMJHJx1XcZgFLdWlrtcMZpfT6uWg79xvPWS0ED1A0bPpvDovIQfFmh1XDvFY4nvyJWBjSBcFqhWfFlC_qlBj36jqzde5w3G36lH1qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVxHxGahFK-yF47-MIhxGMzDNazQ88Dwpm3sSaDht9Ec1qFiUr8_30wDFikjWIg73oeOZpJq34-SJSrfcNc42r7JaWJME4qOf0apgEuai9BPBGnMwfIpuSNgomE7LKjEHdEuuEXpl1x38nU3nMXg5IU3P9pDe0V_JAGw5JAGOqT28oP2O0bC1pMM3APx0C5YFyplEqCEx6vFEXVKd5cWuvFU82jW-dN5lQ5Hnbmha0ZCuqPstb5mCx_EkKsUkbnUDToqZRFTu9XytGEuvFLBZguNqP37Lzox29AMy3v77vumOkZJEqp5GA3QZm8Ymu1jsjZfASa0oRrdHtph4e2FjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=Gho3w2nXIZ-nFyuc1X61Pnt2WBkGyPJGNLGK83Dwg5AUE7h0m-M5eu1CIxkp5wyiX9QLNX6XCxpk9_3xhfEHo5zy1akQIJ6WZo6Faq5zi_xyiDCM_aqhfxn6ZYPI4RaYZ5FkfZM0F__I8ftohU3nDeNqt6IaVGvr1sX4HJKhNQjw0mCfOlJNG4hSnZmNYVV9v8uyHJcDZs3KerCob2kKlzd5lalX9XMkajn4BxOA4QFqvrzrEFxB9M3zglqr6-XSMfOfuuTLNKG1Vlg4K25dIu1L5IOqrkJRSMp0XdM7KuY47P_1h8GUD5xnvApfH2J7EyaaRsUgpGHHg9fXndrOtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=Gho3w2nXIZ-nFyuc1X61Pnt2WBkGyPJGNLGK83Dwg5AUE7h0m-M5eu1CIxkp5wyiX9QLNX6XCxpk9_3xhfEHo5zy1akQIJ6WZo6Faq5zi_xyiDCM_aqhfxn6ZYPI4RaYZ5FkfZM0F__I8ftohU3nDeNqt6IaVGvr1sX4HJKhNQjw0mCfOlJNG4hSnZmNYVV9v8uyHJcDZs3KerCob2kKlzd5lalX9XMkajn4BxOA4QFqvrzrEFxB9M3zglqr6-XSMfOfuuTLNKG1Vlg4K25dIu1L5IOqrkJRSMp0XdM7KuY47P_1h8GUD5xnvApfH2J7EyaaRsUgpGHHg9fXndrOtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=ooyzVyKXe0AFAWN7jWUUxKd0s7VaFbyN1nVlZWIZz2MW8_zl8ycEEmUEfDc3KtIoLc3XIGVzDYYDfyv0WP1OmMmMQHmP4LH9JkVAzwcxkhF-LsizWN2aMh_2Kp7OwbUWfigkXgbqJvBeOJgxpFHhnxVP687XYoQLwLT1aPPo0pNezFHPLwBr7gDJKdzzgoNPB-rG2Jyj0BfMS3LHXlyacAGAnIh-TZaAVTRSx7of_HuIXQWE6HCDxYUzkIaBjvDaZIDwKqg2jd2MnxvMcCKY_dsAIY8wBhJ2moaDLe0UyzP4LC4TP3jpE-7F8XcthEwRvdf-UDsCyou93jfZxjEj9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=ooyzVyKXe0AFAWN7jWUUxKd0s7VaFbyN1nVlZWIZz2MW8_zl8ycEEmUEfDc3KtIoLc3XIGVzDYYDfyv0WP1OmMmMQHmP4LH9JkVAzwcxkhF-LsizWN2aMh_2Kp7OwbUWfigkXgbqJvBeOJgxpFHhnxVP687XYoQLwLT1aPPo0pNezFHPLwBr7gDJKdzzgoNPB-rG2Jyj0BfMS3LHXlyacAGAnIh-TZaAVTRSx7of_HuIXQWE6HCDxYUzkIaBjvDaZIDwKqg2jd2MnxvMcCKY_dsAIY8wBhJ2moaDLe0UyzP4LC4TP3jpE-7F8XcthEwRvdf-UDsCyou93jfZxjEj9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIJn0rljnl2QTZrt0yJXjFvmaGe8Lh8Z0izPMujnL2kaIu2LJW9Upp_ijRjyjd_RMVrnegnc1hCUaNUIO5m4KsjLqmg_M9_y5TjqO8TxBgwX52Xdgaglkl5WsibF9XG_brC665hw_7B_pJQ5qFf_W7UV_uiGG5GbUmQ198YgpWzcDb38IazM1fP3XFx1f4z3ZL-OsrWH2iqMcQjXj99kbDNkrPiBpy8k4zvDT0le-yZdBKexceQqJnqp8U3InKGYh7oKCrLLfTTRsKoHBwKU9zUVYSjInvRsz7QhXKrGSF2nb8b2sYyKYh3TVQULG4ZMRtA9mGUvadOFgNbzKgR85A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9BhjmAZHtx6-MKwzVAjtjtfKmXq791-kcqxgWXI9C5scyl4ezaCY_Emtz-IPHJIdWIEajAbF0D7QUPLN_SmiZjKR9fJSsU4Dtv_hpv5gWtlQVRPGd5ds1vsM5pvB5f2W7OnmXGyzjrWnd5UgkozLd82oJFu9u1jPWFS8783d8T_cTF605X_k8NV41HrqpbYQBW4vd_9yKLxZllcNVKtKO-tVIoh7YhO-ngWszhbf_jIyJILB2kWJwSY4HMVuuaWTh9ubDOaIKMNQmbCeoplKCUqX6wkWS1kyMGx7SOe3qcy__8dWKZraSljIzp_kyxwRRP0_aeSuXspQuRF5lWyGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoSrmgQTk-rM4hfW5lvw2LeCiiZYHZAC9lnFTITcLRmSalgHYUHKIYFBpLFf9fvu7tA1yxRZCCIE7srCneaOnlTzIpBfFHr0kKuFS1vZd9F1wkh3eEW13Qx_HzMlhJgzKu7nyFgmWpGoDO3W1dbg0GbrKIWp_CP0sThi0x69hX7igcslnXpVeN0IGfMnvu0kKUKdM6Lh99OeOJbCa1qNfBS-97sSIzjZlaopJ7x-rJVYBNawJHSlXW7ekaE2UDStWgj5qjaoZOsMsaQGAz7PINxzflO45dAlHQFZ8p7kluWLCsG5NqdD_ISF7tn9WVrz739hkHXJB3R33g-ms2y6cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH6GJ5Tbm6xW7oIQW3mwfCsBXGvqFijX-sL23dE_qDmj7Kul93UXiQV4RVJ8vBMu7yLiu32nZuAq-g3PiXdTqLDiA0WfKlu2Rr-0_x7xKPA6VsSL96OrbCLziOqecroLqs7jqARHgPTAjV5ABY4K6xZvDnejaMEFOilWfTAqrnQVtyAkHodPdMoM2miUW4_Q97JeNLs1Eg8lTdVKerBmK-k97g5AcDCmkOkfbffq_t_QsQxqytysq6glsdXEoDXPJAs9r5ZHz3e3oTfd0gRJnelGN8VcK6sikABhDTs5E52JrcWGsAg7c7hFRZJihKCvSQkcKokrdebGLTxzLreMMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjHJg2AVrevoggUHUqR8OP2HI1cvi2s3ixVgUkv8cZqYyeBKrmM-Kd-KXMoAnnu4N6lARLCSpfu84GNhWIyp6-nSOYVTeZ0OzF9duv33XKc7q3KwZWMvltkUjSVQfgVURlKKXnYM5c8SHs8c788mMMf7Q4UBzx2cHY7ZkuEX3lJFuoP4gY2TRqDf5rLzZML0yEq6qj_G0i1OvT2NSQUPKKNVhYaxwjOXZ3raZuEWjZPTZ6RtdF64lbvK4bcWLPdSINPs_m4Cix6O2THK4H1rnaisLUuEJ8vP0GFt0STPjm83nueWShb0eNjobm2XjmRofvKczTDvqI0GCILji-HuTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-FekU3JFpg4-M5jxKxu-DyWguozdZb6vN5_X03n7J7yOLoZdgEGS-dtNKGSjdudmAIBdJS1MSb77kEgSlMLBEeG77Tyed5CEoaT4ARKGZWxsa9Z0nM3tOxRhL7ibS8I-5TTrcX3MgwND0evQspCBJERE6Ob8B-aOHQ11TbdXnPwyDpfR8a3ib5TsbNbls2vWzOV1W2EUgHmJZrwudsGamdhux_k6iJuCTlNt-PQLKFYFSrtAvYD0DgqjdzHjd8ueo2uIkzCRz0JPAWpVzAv9NqJ3-EP1qfZ_Vv2x1YXb4NlKRa_PCu3AspniOMYKnUdTPG9PZIJ0LUTIRPnXhmk6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPi1TVt-H7gVsQK_9PsdKpR9dWZeecbNkmFDueyO7Mdoan0VZ5as0njoHvKyZVLIftYqtVQDVYVK4cWs3qflX1MEyNET9m6ZDonyvOpDOAk8INlYjgZGX3l1kxImwomFKfue0IMFogN3bAcDfUQSGHew4f5AewJLGRtXyVaIC5SuWlGpKoLwtHx_aRyowX4CEZhi4QO96nsdqDfRqFGDXduJXNgcAxpVC6ZuD1I9xYxd8v-MK-4Rmg5qskWob7Y4F266er9__B0II43mIIX3u3BYHVw_s_WbEGMHr-Pgilphbm4-1GShzzqNRYl7cjGvZo90oOWG95fTFi_p6_eCyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
