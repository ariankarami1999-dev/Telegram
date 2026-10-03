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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 01:05:37</div>
<hr>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6Y46fw-2QLfxnT_B44tyFoNR8gPkPSbbdB5D29s64bNZV_4-qkS3F7ykSpY3AAIZlszVKU3ClOUvAont20QnQJ8JyKQag5ZD9hZTgAT-1t-BSRzzdw-mEBLX-ORY1zZu-NhW1edTOp1qeRptA3HUGzc8p7_UpyACI_rbpDndUhkuSUWcKCBiKR1loseee97LXHWjtG3BLdm_N8N3Pf-2n2i_3wKAKM6Om5UfftyB4mHmoI6hlMsGuC-KvRx6jRAqp_DAlf1QBxnKwML1WoSAabb5OaNmTbE6lR8W8QJXUl6t9nPzbfL7UNtBVaPd05uCcFbnh_0ExEPSaYISxaavw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یورو شده ۳۰۰ هزار تومن!
و دلار تقریبا به ۲۷۰ هزار تومن رسیده.
ولی یادمون باشه که بزرگ‌ترین
فروشنده و عرضه کننده ارز در بازارهای ایران
خود حکومت و عوامل حکومت هستند!
ارز دست اونهاست!
صادرات دست اونهاست!
حکومت و عواملش خودشون دارند قیمت رو بالا
می‌برن، تا ارزهاشون رو به قیمتی بالاتر بفروشند
و سود بیشتری به جیب بزنند!
اساسا برخی از دامن زدن به جو جنگ و التهاب،
کار خود حکومته و مافیای حکومتیه، برای افزایش
قیمت‌ها و افزایش قیمت ارز
و افزایش درآمدهای خودش!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQRFPb_C-bV4hP4ARl0bjQA8YD4hvJt8770ZynlXhRrkEz0qU-Y0Czrfb3ioE_Qorfffe8ug-qU7fhU6jvLLfXnvRqLvv2J_xod63yV0ovQ0942Pmj_VcFB330v8MfIhDDy5nIIc9_d-hX7kPLGhwJ_pm9QX53fZ3Wt79qgSZXZWkAGgzjKw72vtuW_tSM0Z3w8Nqh0QdV4SG3kRy_3vsZ1mjbU_ap22_Br5Ly-NT3SCzqyH_7o_NaNqf4GeotBmtalElBLxVrWpu-7ruoZu4riiOD3xXN2AyP3axUXotRtFb7zdrYswLYoeiTDotLS8r8g_TVx_9rc9Z_csG1bTyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSIrOCdxRCBym-pYcJWJQvUt4Knff5D7Ck9U0ZsA7IV53cYECgwFSaAfXnXUtkHXtG9WiReBP4DtYLNTkh2-3O1BpA_cNKLueE1MKmIgERXBZZTFhJlyw_pA5AoajOBQ7xdbukVLPdVnyiT65Hm0Eumh7JmhHe4Ll1wUVdy-1NFktMesChFNMqaPCrWWmbqE0X8ImrjLd0EOIbT7mruCPKGBXB6l7Ajex7Hk6-KoY_kTR76wPbSBxFksTMDr0a_z3PGxj2ym8-onurJJ8j8KhCcUl49kvynXcnMObSdX3FOl_lqajHMrysolpxUSMQrcGi3MEW1GzVeWY9E5iWwASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBtnZtxfvmkZljS1X5mmsoi_3aQ2dE63LF_VSvZ8cHrMjAr4it62ivKnNgr7jnYcgNCwMKplZNtMWhxiJVIVSzPwyfPynGJGfLtPliG6xfHO8hSeBiHSOlQr0LRiLrzWDPh4Yhg8-miQoTL8M21SFw47R6AIApFyJenct6mBDibvvcEADDa7AMS5Z0HZyfgNbQ7IPWzWxyWLtXUiDY0BOehBGwlwOwcKv3AKOUTCKZN4tbHXHyIX_7e0Qno8X-kuw7gOUTRudhpn8FOpR_g8mDHmSBtI_EuCrEXiBYvrZAwv2_K3PtWhKb1woeE05zJPoEQP4F19UVbJSPyGLkcxDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=H89QaAcvfVzyWTVjmGzUJ5nMkw90cASi3K1Hb4ZKyOfsuEjT9zxcHBVeQkGq9XJVB8uXNG_CjyactTU4SAIVOfb4cQkJysHbSqrIFv9jMVnJRxZhdAyHHbdfbcBh3IFzyWbNsxunhePYaXXpo5kf5jy9QzzozQTVFVN0ZSlgpgOeaAstqiFNZDhf9VtdrX9NasZryq19LSjVKRE7UonUpoiqLpUVG3vYCy8SliWf4XqFPyaGPyRM7qzoBuPlntc4218kmePfC6qi0XpFmOo476ZaLPUuXp2kM7P7AQY4V0ZW8Fw5Z2G35Em7o-bdcTD9uneXv6Q8ORI7LxasJbkjWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=H89QaAcvfVzyWTVjmGzUJ5nMkw90cASi3K1Hb4ZKyOfsuEjT9zxcHBVeQkGq9XJVB8uXNG_CjyactTU4SAIVOfb4cQkJysHbSqrIFv9jMVnJRxZhdAyHHbdfbcBh3IFzyWbNsxunhePYaXXpo5kf5jy9QzzozQTVFVN0ZSlgpgOeaAstqiFNZDhf9VtdrX9NasZryq19LSjVKRE7UonUpoiqLpUVG3vYCy8SliWf4XqFPyaGPyRM7qzoBuPlntc4218kmePfC6qi0XpFmOo476ZaLPUuXp2kM7P7AQY4V0ZW8Fw5Z2G35Em7o-bdcTD9uneXv6Q8ORI7LxasJbkjWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2NRb6ogCHboWI7c7hI3L_XvkM1KY_8V37eZhIwxz3tVhjpIsghwjJp3NVUQAejQOQj_ZmqSEjkZHBvmbBh0SsLZN9TfSsUFPZDKAWdfjEABMnnnBl3Czq0mgmRLpipwkxQudS9QQi4xTAbdMrUXn9WGGZjhOrkMv4XeZuS5vd5x4aT_0IHXrhJppYj7jrBBNVM57nirxx-i7JkDOUx5-ElQ75VQD5GKrmY5J_jaoimVA7aoNKSNly_ViqUiyboqEVaNOvk3KMnAJdiWxSsWvy8G7pMwVuwnWWy7KnRX2lPfFJiLa6z1OC70rQoUAW_4N3dQAkZnoxOaqN4ukBXA9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=Ex3CPn_7X-zzI2jUV5mwKDU0akirtM7LpkbpYd2t9lQHfyZkjQRuZtsvIhAFoz92DVXn-wDot8f7MZH8Z1bdhtZo-muQVVGQQ6A2WYtKnUfJ-EU1v8V-EBs-XQbjNl7n6IRUXvAEzZ4mV_yDJLeviLbtiw-JeXixkF9MBOF8cT-d8Xq2CQotD8erVtHb9-_6vY2ASPc-i1Zgo6u8x8EkfP9xbqE81izmBZOZy7a2mr3KIicCVx7-xJEzadQ7P-kP6UlSWGQpiLebX8w2AV8JqMePpfDfkRVX5OTHje6KROvpkJUlsUSMxR3zGp1D2O5K0Q9tvtNuFCHqdWxCFk2G8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=Ex3CPn_7X-zzI2jUV5mwKDU0akirtM7LpkbpYd2t9lQHfyZkjQRuZtsvIhAFoz92DVXn-wDot8f7MZH8Z1bdhtZo-muQVVGQQ6A2WYtKnUfJ-EU1v8V-EBs-XQbjNl7n6IRUXvAEzZ4mV_yDJLeviLbtiw-JeXixkF9MBOF8cT-d8Xq2CQotD8erVtHb9-_6vY2ASPc-i1Zgo6u8x8EkfP9xbqE81izmBZOZy7a2mr3KIicCVx7-xJEzadQ7P-kP6UlSWGQpiLebX8w2AV8JqMePpfDfkRVX5OTHje6KROvpkJUlsUSMxR3zGp1D2O5K0Q9tvtNuFCHqdWxCFk2G8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBmBd8TDGH46yrTS6wojmTylMkFwYR8yZXnewOs0z-VH-d-AdcNn5DraR3WHLvxSsYQb4H4T6BbvNDVf59Tuai_KtGBFY4XjvdLrQ9zE6LhN6Tu1DsqEZSIfVXEA5Ff4j1inU_uddtb_9805Czilbn4S68fuCnHYEyTGv8jwOXezpXRQ2uugMIPuWKJKLB393R7IDWxNiUsyYgrBKLEICsM_y00KNBLW0ikK1Q6TYWY9hHN_YJNw7XGVtiKKjvEeXtolvY7EqXu-eyHBHo9WPohtNQVBMMqSbnSSocematsbz29r3onjGwZZk52rG12-pO3sukgPFrsVknvh8YdREQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=k_TfP1JoKzmys15l6P0Rp60H0zaQB1dgpVfSwKA25C_TP57i90QTGk8s-61-GLAfXmrD_byvqZxcM2Pdl7IFKw_q8ZhGn9Iw0FnAKxHofGNfIAgST2jDg556rAVDNodW6ZjgYSoDHd5StRnKy5FyU7uwumWl0ZZ3qOH2qJNBM6ubcvRPbTz26xWy3Qa_IWPE90Pdt9BzV-NdnHcDcBrRHt46e-nW2olwbGYteGYPbZY3kPQsF49bkCH1SAtXBAjlYPhzLDVFSM6QdrbTAsnokh_aV_Ww6aLZY7x2_dqOl4B7N8dLg7epvXekJsx6CN5-pBz-KBsxMah2OH95uplwcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=k_TfP1JoKzmys15l6P0Rp60H0zaQB1dgpVfSwKA25C_TP57i90QTGk8s-61-GLAfXmrD_byvqZxcM2Pdl7IFKw_q8ZhGn9Iw0FnAKxHofGNfIAgST2jDg556rAVDNodW6ZjgYSoDHd5StRnKy5FyU7uwumWl0ZZ3qOH2qJNBM6ubcvRPbTz26xWy3Qa_IWPE90Pdt9BzV-NdnHcDcBrRHt46e-nW2olwbGYteGYPbZY3kPQsF49bkCH1SAtXBAjlYPhzLDVFSM6QdrbTAsnokh_aV_Ww6aLZY7x2_dqOl4B7N8dLg7epvXekJsx6CN5-pBz-KBsxMah2OH95uplwcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWKJTP9efvsBF5z-9E7QRAbgzpRP8Gs1g_eSDtZdKGisQVEpVSrfijDykQdA5qCxPEeybDKVeQHGv-PyOzSFdScN7BmOYMQAF9OuwzfpJtIKy2COJiwTTMxEvD-w5d3PvgetG8bH0BImUP-A_QXt3su_wQzWgsyI-CkyZPNAHFbdNVi9vN2JXHMqIA-xlQSbUE_A5CdzNZDX5-6fj5xE6GjsU3tc-VZ-WyBZCKdNfzxUq_b9tuJoRc26ci9sUsE0b8G-ml5-XwflotC00xVKgsr3y58DklywAR4A2nc8QSxhXjy42ha9cj1JKaPLSKbw6PObg39FgV7BPzM0A6h4WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdVAZdansn3HGTPXqRpGaNwnZE0abz0HEfdQ1KqBnEguXFOKx9bWBlB9UC2SRgo_p4mtUOvKUfBb9Uc-WZko3e1_CSYzuKE4umXqHGndKsSOUt9PnksBGNAQg4xCFVYK4HJK5apLf9-fTlU3cCXj7ePH7zAqLhPuSIKItY2tkfN0CE3QBED9CbYpSq4VdNxXGx0Nu-vhtfpOEd1yOUa6696xnxpG1x8oy2iQGczr1bkfUrAPU2XFe9lrCjt6lZiyDkxZlJvSGoY5lmMkk7hk-_4nmNBU-SJ5GIzmx-4Mo1u_b6l0ZuFu4yYp5kTty-T6KfXTAkc0Hc4-hiZ1yhHj4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYVgtjOd0BwBMm5lBFr7__fEK9Oxm6sEDfrGnNO08nkkWiy-C1GMkZ43fYfukIzvThEfyo32MTimJajoSJHjTbRpMoLE5Vpb2VoPKQ9NKtNYl40KYqmWediWCibxIND7JSOtEC8I7Z_aHIA7KTbxiPrAaUDA9A6peIpcqwkJc_PPDSqS0n3dwgCx6AoIvP2ZM98Vj924Iqg0-KzwQWDpsDUMluSQfKWIkMS4EVY370zXY5rqq3r8Opi1_N1oi7zIdp3jT8QwbxkudgLgJh4j0noxHcdwxBjqeV3FQUTaxOz3ZppTPm62WFKGr54S-toiksA8uu3ivp28oqVwknR0bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=MvJphOcfaMF9qQTCcOJF0fpMGgQ84eSAN4WKV8d_fw3XBOyfGjexYc4UQFktQ20GDjaQeib9G5KxIhAOc6SRb_VzcRfN67X53G_pqeV3hHhRpznTkYqW-WObgQI1NY2guWAB5I0RDVJE6I2Jp1m3gqJsg39DRVP_k7TYPdalG6XcOv2CN9ku-RndpD3VgLxV9jd9yi0JdEFfJAwzYIDpiupRvUaRZdLqncOxxnM-mjSbnBGSk3ZtUYxryodfutes1O8wkY7vQvJIR0zBb-WpSysTx-6bnRA8wxMWDlGA39VjZadYYf9IP4owieKhI2JmCltArKm6euoNKA50ok2ygw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=MvJphOcfaMF9qQTCcOJF0fpMGgQ84eSAN4WKV8d_fw3XBOyfGjexYc4UQFktQ20GDjaQeib9G5KxIhAOc6SRb_VzcRfN67X53G_pqeV3hHhRpznTkYqW-WObgQI1NY2guWAB5I0RDVJE6I2Jp1m3gqJsg39DRVP_k7TYPdalG6XcOv2CN9ku-RndpD3VgLxV9jd9yi0JdEFfJAwzYIDpiupRvUaRZdLqncOxxnM-mjSbnBGSk3ZtUYxryodfutes1O8wkY7vQvJIR0zBb-WpSysTx-6bnRA8wxMWDlGA39VjZadYYf9IP4owieKhI2JmCltArKm6euoNKA50ok2ygw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=ur_poI4wDLc1nRc3DbSZ56_ltqECNfu2-w_NfBhFTbZLgPB484-qm9dIOtrTMZi0k8RL3jN9IlzvG1xz-fxlcLGMOfRUOpngXvR6hSlX0jFAxGEyI1tICbaZKjfMWCxwLoWzYj9K7qmAkqedNHyOW2jYkY_71Tt_cN04eFXbPxH7sXCeEXUPks7qTxxhwPzfSSE0puKdAnjMjZHrrmibxf8CagLHMKrIeHLoFvwdIqtV8P0CcZS_CyiayX8hoVQ8VExv68UySStveSlebY7VvcdU-2TpxmRHQfsLmE4SRBYTYKYmtYmORadYoDcJFQGONP5s_lNGqDiX3vWaOTHNAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=ur_poI4wDLc1nRc3DbSZ56_ltqECNfu2-w_NfBhFTbZLgPB484-qm9dIOtrTMZi0k8RL3jN9IlzvG1xz-fxlcLGMOfRUOpngXvR6hSlX0jFAxGEyI1tICbaZKjfMWCxwLoWzYj9K7qmAkqedNHyOW2jYkY_71Tt_cN04eFXbPxH7sXCeEXUPks7qTxxhwPzfSSE0puKdAnjMjZHrrmibxf8CagLHMKrIeHLoFvwdIqtV8P0CcZS_CyiayX8hoVQ8VExv68UySStveSlebY7VvcdU-2TpxmRHQfsLmE4SRBYTYKYmtYmORadYoDcJFQGONP5s_lNGqDiX3vWaOTHNAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=nJY_EoIuGZllCrG0wD3lUVFIIKkse7qSR3hfmw-MVEiLQgIK0aRm1BW0zOrPzRgaYuXUjYLnC5RXrxDBbasPWx3Zh54BaQqd4v5zCjU72JOJQNp2e8GHT7NSE6kY2IW9jvM5PGNbW-q8s0nEmaM5HouZwcQSEE9mCLO7F14ftpqyDa3LqyU8pNTeZJqctdRFZ8Uy2zXuArzDXu99Qv31KhAwRk374hamsDAzJ9A_aRqeUl20xXxp_4WtAS3JvMi2D0RzjEQeyg6oR8bOD-mWHtlLOI0vFug02V8mnLsWcom9pjDBi8J5n1AytXL6qJiVlgHbBSXuF0iIVwPhnKtj8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=nJY_EoIuGZllCrG0wD3lUVFIIKkse7qSR3hfmw-MVEiLQgIK0aRm1BW0zOrPzRgaYuXUjYLnC5RXrxDBbasPWx3Zh54BaQqd4v5zCjU72JOJQNp2e8GHT7NSE6kY2IW9jvM5PGNbW-q8s0nEmaM5HouZwcQSEE9mCLO7F14ftpqyDa3LqyU8pNTeZJqctdRFZ8Uy2zXuArzDXu99Qv31KhAwRk374hamsDAzJ9A_aRqeUl20xXxp_4WtAS3JvMi2D0RzjEQeyg6oR8bOD-mWHtlLOI0vFug02V8mnLsWcom9pjDBi8J5n1AytXL6qJiVlgHbBSXuF0iIVwPhnKtj8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3ebICSfEBpxDHaO46aNvhRhb7OGMnI_zEYSWFXm-K_RsuFoHf6IPxQfAurxErZItqSmYIhiknVwgaqgvYDE_EbjYNKEA2YltQim8FwySH1OfWm4FyAEUBhosBWumQg8LZ4CzGB1Wtn2A3u740NSeuSUOBWWvjJcgo5GBs9XXJfMbhxdK8GJzUfqRvQXL-2zD8Fq7fIgoFjLn8ikzvG8wypmIlAUAjGa-XSxqRr7BATG4WoGbFyt2ZqWOeMx3NlGlPfrEI91pd8i5qZNjt4_gcvpTrFeToMiEtOCPIr-uI0blfXZBu1PiHUIb-5cux-apViis8jBrcmqa8WroxcBRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8CSAUF-uRMfPy3WBFRXra_73hwcK01Y47scZwjhBD1vppeZHieP2ExJHHkH6pjLpDbPmO7nScT6bbMSZ1a80DvuF-K6z62LkE7uugv4L2N2vSbf9OhR4MrGoKkjm3HjE7mV8K8G0bioSZvC6y0TeAAUavmqYzA_KFHwq6BY8qJQ8Az7BWTp76FckvDDnUaA6vkRTuHX0j93uAiJRZqGbbW_sp2sVhtXAgalIKwkpovakhjTolWWCkDVCVihhUGOw9uCS9CXcAQb2t_luGprPtZqF0_fchlQ2EzkbnV9pQKL28xK946oPYgeVDx27kB-Q5XLuHcUYRvAy3CgvCxi7Zpc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8CSAUF-uRMfPy3WBFRXra_73hwcK01Y47scZwjhBD1vppeZHieP2ExJHHkH6pjLpDbPmO7nScT6bbMSZ1a80DvuF-K6z62LkE7uugv4L2N2vSbf9OhR4MrGoKkjm3HjE7mV8K8G0bioSZvC6y0TeAAUavmqYzA_KFHwq6BY8qJQ8Az7BWTp76FckvDDnUaA6vkRTuHX0j93uAiJRZqGbbW_sp2sVhtXAgalIKwkpovakhjTolWWCkDVCVihhUGOw9uCS9CXcAQb2t_luGprPtZqF0_fchlQ2EzkbnV9pQKL28xK946oPYgeVDx27kB-Q5XLuHcUYRvAy3CgvCxi7Zpc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=PffOSxaygbi-Ghlb7mtz5elUonl06ETNy_jNTemVKGO3lqomXbudIH_4mPwB_L1MZzBZsxo2ut2taGLMBz3WUjFL5iAx49YlrPhDYo2NXTZAFHnNFFMMxO3eiK2W2VR575dMjfAAUamjePMaDskV-q7uvMaeTc4ou9gHqyK3-LG69AaOVgy4kIrYXOZEv3XAY4HgQ9aIpLyDZt_BIczrXhUBAO3K9XajQbegEO0XDjqv1O4tqvcJ_JiFS1GeByH59F5l4n0_4qTweXHuYOrRMOyMn2SH2zbLS6e_t1OcOVVT18jjUFW4ndM6BM9233Zy2h6kkenslnQVdsbAiYG4sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=PffOSxaygbi-Ghlb7mtz5elUonl06ETNy_jNTemVKGO3lqomXbudIH_4mPwB_L1MZzBZsxo2ut2taGLMBz3WUjFL5iAx49YlrPhDYo2NXTZAFHnNFFMMxO3eiK2W2VR575dMjfAAUamjePMaDskV-q7uvMaeTc4ou9gHqyK3-LG69AaOVgy4kIrYXOZEv3XAY4HgQ9aIpLyDZt_BIczrXhUBAO3K9XajQbegEO0XDjqv1O4tqvcJ_JiFS1GeByH59F5l4n0_4qTweXHuYOrRMOyMn2SH2zbLS6e_t1OcOVVT18jjUFW4ndM6BM9233Zy2h6kkenslnQVdsbAiYG4sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-gd-t6lZn3xaSlNemjTV12VYDqJPfYoMLV-fzwKd8e3EEcd82sH6Gicbs3xWeBzramTHVadkZm_XQAkRLrppFqx4HqxS7rZYN-N019_vYI4-knkrW78ShsuLBZRhbbAjnkT5xhQVrW_fnlZnbv_TMGhJxrYTf7uT0tCwkFpJm8gqI6taiyDav6aXwjFZZ4TExsLsP5lVfywZnUcVrckzTDkA9FJ_9mMrPHlkZJ0VaHmfkF5c2PC6NFTuSsnUuSOw8-0xSw4VMyTZSraaR0TBpZEOpfKVk6YvGal_ocsxCt3MKzQGAXiHQJ52wW8dEv0H4gqi-WcUEC-2uEr15GclA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=I-Xq5EvdZDjvHk6FfjsySUN3BGakCmDOyFjB0wufdGheNvCMyOEhdmj_ItSUy7QEUYzvNxD7_IlsHapo34Ss2DYh-lgZDUZQBfLERRf3r85Lk12g4WQBupg5rogM_kNla5Dn9tlIKnyWD5mQG64-s_NbvkyAg9VHUa9xrnyLdcORwEE4RUTFXgDkIt-QexN6ogQAZZG28xxcrZty9g6h4NAJXDkKQ9UI09W2xsVwRCy5DJwqtDAlj4s2Y7mbxc_oeg3vGuPFmkjhIEQLLvUtg6hsUmU5Y0UhCgh2_PXRDrq7J-gU_MY6PDg1gmmbxmVwBJKjJv05AiDceXtLyW6GNCqyguZIttWQ-MaRdkFsVUNIcccANMAnogDXwZWRkJsPC7bbDZQJcNGCC3K2rEGtb4xK7HK4y7862ehXv7Eu_EpOv7jxxeRqdwdTkmEAQSwVdT7vTjRfiMrpx4udD-wiyZcMbYO6o1MkiRxR0De1RwiH3-sy1p3WWH5mlXo3USX6RwCy_rIhk2ZznkluOsYMthcxpjW_7_BH1w_8MEPoBbdBPO8xXFGVErKpKczjZmSYWPU4hIhWMon0GW-Kjxfh4bhOXlW2rRfsIJOuOdfIU0ezEpXoxNqdDXVaA4Qxa18gyA3zw56JHlQJm0ZJ8bfKNNk1iZat00GkYXN63GSTuoY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=I-Xq5EvdZDjvHk6FfjsySUN3BGakCmDOyFjB0wufdGheNvCMyOEhdmj_ItSUy7QEUYzvNxD7_IlsHapo34Ss2DYh-lgZDUZQBfLERRf3r85Lk12g4WQBupg5rogM_kNla5Dn9tlIKnyWD5mQG64-s_NbvkyAg9VHUa9xrnyLdcORwEE4RUTFXgDkIt-QexN6ogQAZZG28xxcrZty9g6h4NAJXDkKQ9UI09W2xsVwRCy5DJwqtDAlj4s2Y7mbxc_oeg3vGuPFmkjhIEQLLvUtg6hsUmU5Y0UhCgh2_PXRDrq7J-gU_MY6PDg1gmmbxmVwBJKjJv05AiDceXtLyW6GNCqyguZIttWQ-MaRdkFsVUNIcccANMAnogDXwZWRkJsPC7bbDZQJcNGCC3K2rEGtb4xK7HK4y7862ehXv7Eu_EpOv7jxxeRqdwdTkmEAQSwVdT7vTjRfiMrpx4udD-wiyZcMbYO6o1MkiRxR0De1RwiH3-sy1p3WWH5mlXo3USX6RwCy_rIhk2ZznkluOsYMthcxpjW_7_BH1w_8MEPoBbdBPO8xXFGVErKpKczjZmSYWPU4hIhWMon0GW-Kjxfh4bhOXlW2rRfsIJOuOdfIU0ezEpXoxNqdDXVaA4Qxa18gyA3zw56JHlQJm0ZJ8bfKNNk1iZat00GkYXN63GSTuoY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEeQr0dU1eh_HTrJ-KLygCbSqBdEFIDu0NThw3dbQ4jeKdsOqUIOlDNTGxAg2jr0DP2pZYdv1BHF7L-uzMGmKdieGLvXqHP6pxCQsyrHWWG2xFkfEnq4uABm_Gut_mD2_4cCpcUcJ3RmCwGRq1axqJIiGgKzvkF5ynOMAqAd0Tt2l-QivxdfptLFZ9mdgmutXCBAZGOowDOUNRKtZIPCFOlmgO22VWKGpoBHi14JioeS2YEDmDFch-R4TGyLHkVxDgo15Q9xutQrFOsNTx9Y99XxjvbRjsxY_0fToCXPXAW9qNfx8kc95KQ1KrkgaXIu7wNh6Q2P7pvD-u7I_uxh0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=oSfgrzgTypWmvv6nMG3VavqoR__hJsgJaxhhd-ekmtSuIMKlJG9_Ucm8fvV3ZQQlmvz7Ikp_1PwknYbjxbLMjqCNVF_vg2JviRPwVN6h5hFrF9vNC0GRN94tui0IBGTUmIcjoZc3RTctrHJi0FaU46MOYn7cnO-0s6TaCDVUBACfbZda42oKD7XHAg_G0-RVuEhDPl7AHubvskDDNEh7_jkN6qNgIN4wH8M0_Q09CPKxybILJNt9-mlCs3OJpTyiRoEeqB-5jXNixQ2c4oNx6W78hX30FLup5lOX9H5mi87XAu0MbGqvpxeKc1eqvpRg13PPN1vXMZdl7VoQ4GCnNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=oSfgrzgTypWmvv6nMG3VavqoR__hJsgJaxhhd-ekmtSuIMKlJG9_Ucm8fvV3ZQQlmvz7Ikp_1PwknYbjxbLMjqCNVF_vg2JviRPwVN6h5hFrF9vNC0GRN94tui0IBGTUmIcjoZc3RTctrHJi0FaU46MOYn7cnO-0s6TaCDVUBACfbZda42oKD7XHAg_G0-RVuEhDPl7AHubvskDDNEh7_jkN6qNgIN4wH8M0_Q09CPKxybILJNt9-mlCs3OJpTyiRoEeqB-5jXNixQ2c4oNx6W78hX30FLup5lOX9H5mi87XAu0MbGqvpxeKc1eqvpRg13PPN1vXMZdl7VoQ4GCnNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7l0fOygZIr0kUasdqGblJ74UErB6nxuuBk7FJ-tj_bAWZzrEwT2JKq9qWIcKeOnTgk9mwAtaIe6vaDFF9CT-UxRozQt7746aXgX8bmcADThiIDwL2kLlKVm0qqda02dA63tFzC03rx9BNHxhwCVd02NWmpdBuVq2DIiGLW16ZyU79ee6oNrFgs095Nz7mH0tM3bamFxuD9U66rBoR7DZsLwJ1OpiKRarWebfJykVDjDaVqkaY8Qon0Ww3-87gZwSMio2yuaXt01xHuJ039MAtnTgcX94xGzZibfhUY4bjlFdtRcBHPWRvKmGXZ77ijB_ZNfqQTAr4OQmPbrE4Cv5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hma76Ym1XufDMGFik4qvDZDHsr5P44KKvJubAYrSJbq-HbYn0r_KjytVAiwla0z_OuhbdqcqvMpf3Dh0Vlc3zR3AhRzod8jWJSd7H9xkAuNhZLqtI7VKS6gFPI1aMp5t2Qw46XdQZVdUtw-YXreJ4C0GBuO3iwOWk69VolK87Vo-ZFLe7ydSfO5n7yceSt6hba-iiZFPo3gdtl2shSkrR3pe07fJ0ItfYHU-47QHbnJaDDOHjMRMH7N71VAMGV8M2JOhFZMJ3WWfwtwtShgxBfMpqaUbAxgsxwGdL4CwLPoCAn-0NHT15ZAMT8Hijqzj5M2zLYTOPF4ufmVKGueS_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQwJaSACTQ10LZeHpRoEqUX6k55TLGDe17Lf92AkHXAUda1YzBL7FAFJNbgoIlZjL7z8kRC3u216MKC-BZUvbSh8HV13EnGELlQ8mBBvKSO-_t4s4y1Mlfd0xl7-VyzOPcjHCEaCMDRPDZzPDU0ZybE624iFNDlBw1omQVnbMZEEfdTyr2fKarhmrRDdguo1SGGahm6x7A7zg6i1TsEe6l9xiT7tm6sF1Wbg9duxsCQZRwXpP6fomNt1uLcqfM-9EXZXIvtUX9WytigQdF07D3CHirpxOcGis9VP9uZmdGax_BM29f2_nqc94BC0WTfLAAhxXZ15_BXMn7QfjDZukg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=W607cT4xRhWVoLrVc1LHqfIwdC7pP3VnSCNKR4H_jY94DXJX6rGZiMa4NjaD2UqEq5LADX_AMmavNhbZkwrJoyB_9phq0rpzIYPBnADEX_IW5y4E0mBeIEzbfLAMduuBqlAYrN84n7-Pv7pb5Rn2IEpUvXjsTTs3FZKAYUq4I1uXukkwGB4Wx_Iec__JVyvdV7oX8eLXf0usVy452R3PP3QGd8Kf03JBwpbzurkVWznf85Ckk2lSRzRxZypGGI7Ch2yAqGvYd13rBcnQlOD0vJu4e_HbB1G0AaeAckN9dedU7HJvAzqenD7Lwm6Ebl2apRhUy8hHDcgNzKEwuI8v2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=W607cT4xRhWVoLrVc1LHqfIwdC7pP3VnSCNKR4H_jY94DXJX6rGZiMa4NjaD2UqEq5LADX_AMmavNhbZkwrJoyB_9phq0rpzIYPBnADEX_IW5y4E0mBeIEzbfLAMduuBqlAYrN84n7-Pv7pb5Rn2IEpUvXjsTTs3FZKAYUq4I1uXukkwGB4Wx_Iec__JVyvdV7oX8eLXf0usVy452R3PP3QGd8Kf03JBwpbzurkVWznf85Ckk2lSRzRxZypGGI7Ch2yAqGvYd13rBcnQlOD0vJu4e_HbB1G0AaeAckN9dedU7HJvAzqenD7Lwm6Ebl2apRhUy8hHDcgNzKEwuI8v2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XM8A7hpn5NR6fx6utk7KiMA4rvyIvRFKGcBqtg-dnYDJSqjR5DxhBiePPqIxc0tLmxISfDZ6z1hk79usUT-UmsVYLX1gbXYezBSRobSe8c3KYvdWCgI9TTRM7hIAPm18jIwYEnBLnJAeIbvdWeTfn1y3aOASikjKg-VsH6chvY_Fw5TfgSI8aP6EOUqM-OjUJ3XDgA_NoAcTWCBMSBq0rF2abeT0SUvDb73aYF0mU1wP353kNIK96YXPMPg5I19cCkODEdpY4mVpO_QHfPgBbPG_YbgCwtMgrVq65_3BtZRVk3q2CkW3lyEHa9fBNUPr-9PmwZZC3DJM2NbPVLcitg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu1M5ewUdzCG-UcJ8ZeTEKB9eBdV7fz3R1qo7vWXvJqKXvvr2F8sPHX2pM2IuRv6To-0i4VlFI-QN0uh68kpv2YNWLCXUZ8uxlH6NuEmXUyIfoNLJfSwPtShdlCAFreToNczJpSnlLQnMYrWhSjKwcTaxoWSyN7xnaqdhHFY5r-ds3poWE8LyAk-_BLJGqn2fkZ3ga0Kg877wEEJT_1UPSaAu4d8jj48KENNX4LsWppWr9kaMLSwBRkRBa_WL3LrdamIVA_JCGriyYU3Mgbh4OF9H-5Jsy-DVJ_5BdT9_bbMg6gZnuvFfwSY8yfkENPaG-VBjl3Y4VLqh-saxZUEQ6mk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu1M5ewUdzCG-UcJ8ZeTEKB9eBdV7fz3R1qo7vWXvJqKXvvr2F8sPHX2pM2IuRv6To-0i4VlFI-QN0uh68kpv2YNWLCXUZ8uxlH6NuEmXUyIfoNLJfSwPtShdlCAFreToNczJpSnlLQnMYrWhSjKwcTaxoWSyN7xnaqdhHFY5r-ds3poWE8LyAk-_BLJGqn2fkZ3ga0Kg877wEEJT_1UPSaAu4d8jj48KENNX4LsWppWr9kaMLSwBRkRBa_WL3LrdamIVA_JCGriyYU3Mgbh4OF9H-5Jsy-DVJ_5BdT9_bbMg6gZnuvFfwSY8yfkENPaG-VBjl3Y4VLqh-saxZUEQ6mk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=fUbwSqNwV45XVbuIhCzCJmPoIu9lNb3RX0J4ruI5YqdP1Cm4-UcTa0pltUjcMD5F0QbTSWlBHEUgQsSOodeMGMN0ihCUxG-Y1qlEbTO4s9gZfeBg3CS9SxJEV4FFxXQWGNLfR6XBlFH90tVcPh6U93aZQ9nKHel-zwL7619wwXJ4QZVFQJkXE6UfPTPe3RKEkxNnkY4y3XHtwaOEIzsZuwMh3Lf1lr-cheY06KYhIUDYz-qcKeuSbGEMCbJsSzApsyCiBMfp4LnGYnpqtDtlJ7glmiHkyv3mHAN79uLbP74rWBQYNQ05BbQ4UKkv03c8iVf4RrYp_VMbT41sgqGdqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=fUbwSqNwV45XVbuIhCzCJmPoIu9lNb3RX0J4ruI5YqdP1Cm4-UcTa0pltUjcMD5F0QbTSWlBHEUgQsSOodeMGMN0ihCUxG-Y1qlEbTO4s9gZfeBg3CS9SxJEV4FFxXQWGNLfR6XBlFH90tVcPh6U93aZQ9nKHel-zwL7619wwXJ4QZVFQJkXE6UfPTPe3RKEkxNnkY4y3XHtwaOEIzsZuwMh3Lf1lr-cheY06KYhIUDYz-qcKeuSbGEMCbJsSzApsyCiBMfp4LnGYnpqtDtlJ7glmiHkyv3mHAN79uLbP74rWBQYNQ05BbQ4UKkv03c8iVf4RrYp_VMbT41sgqGdqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=qTuDIg94NWNi0R57wq_uzRPgDXhgFlW-UP19OHxTPQCwuM_D-sLVcxNr6umT2HwU5zcJEZi3onTUxWo92nGfaTaGuAMcpxJt2AmzKhaL_2bvyiXB1FHznykum_oUdkjiMMbjGrBojmm-m8Ky2DfwdbnrR5qSeXD3nHkvbRvsMYkGJ4uTUj28GyVaYFefv1WBzcAviP07XeoryY7dajLyKmeRRwLv5aDW9wl55SunCd93vP3ij8UvlEsD1mbwK3nt9-NAqaENNdREyEZLM7xI31HjOFqXaMBW7l7iYruyJ6tNsb_bXubHlL_A-v2TMlqmgIVJXEdRl-BXpKDVeBKVv4RVTi3NuvA0KCi6LTgOCQSbPrgZf7yxbMyhVo3gbFFisAj3PJDKA6YDjEKvY2VT3_75XmulSu-Vf2N3IVyyn1xepBrWGbbBjuFnlSUl1miJg2R_A_Vq5twk_c8668sxRUx8HCPZqFqdV4DFggn0GFuw6H9J9qFWJNfHUkIBelmUdGiWPCFktpn5tlkCNUs2_c-yKv5tDOK7jTd1W8wYoUwFX1S4vlHGA2U8A9i1IVtTK_QF7_iHvlNCeOf82bowOWT3O80I-BFMMoc_lcCMOdSquEdharMFJOJXQ1iOoZAbXNDdNu1Alm_gFIPO8AWSwg0mC15W-l3GdEtj9f9kW7s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=qTuDIg94NWNi0R57wq_uzRPgDXhgFlW-UP19OHxTPQCwuM_D-sLVcxNr6umT2HwU5zcJEZi3onTUxWo92nGfaTaGuAMcpxJt2AmzKhaL_2bvyiXB1FHznykum_oUdkjiMMbjGrBojmm-m8Ky2DfwdbnrR5qSeXD3nHkvbRvsMYkGJ4uTUj28GyVaYFefv1WBzcAviP07XeoryY7dajLyKmeRRwLv5aDW9wl55SunCd93vP3ij8UvlEsD1mbwK3nt9-NAqaENNdREyEZLM7xI31HjOFqXaMBW7l7iYruyJ6tNsb_bXubHlL_A-v2TMlqmgIVJXEdRl-BXpKDVeBKVv4RVTi3NuvA0KCi6LTgOCQSbPrgZf7yxbMyhVo3gbFFisAj3PJDKA6YDjEKvY2VT3_75XmulSu-Vf2N3IVyyn1xepBrWGbbBjuFnlSUl1miJg2R_A_Vq5twk_c8668sxRUx8HCPZqFqdV4DFggn0GFuw6H9J9qFWJNfHUkIBelmUdGiWPCFktpn5tlkCNUs2_c-yKv5tDOK7jTd1W8wYoUwFX1S4vlHGA2U8A9i1IVtTK_QF7_iHvlNCeOf82bowOWT3O80I-BFMMoc_lcCMOdSquEdharMFJOJXQ1iOoZAbXNDdNu1Alm_gFIPO8AWSwg0mC15W-l3GdEtj9f9kW7s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=HK_UBLKZbI29CUGlcBlDhlMsux0JpcPvaqu89gJrBbAL05HUNd6f4CrJ0tXytwhB4Q8SPDTykRWhGJVpGPHwCF4pQO8kyiUIbcc2zn2Mg3XBlOgqh_CPQ6Na3F3HeJPVaAh64TlrebG6xNkPXbfoh3ivYGIR119oh9x5FSu0iyaA9LDaRGjYWWKQkMuEwsMTEmN_M-McYSaKmMrkzGl1XV7ugdr6p1qnzi6kqrUQFxsAPmW9YJ8I-08Ko6BOwWG1L1HcEg5otiJCEEX96iTklecLCgK8ZYFCiilboZLCjt75Y2X9U7xRsWU6y5qRQEc-RNSY2DukPgX0VhkIMUv0lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=HK_UBLKZbI29CUGlcBlDhlMsux0JpcPvaqu89gJrBbAL05HUNd6f4CrJ0tXytwhB4Q8SPDTykRWhGJVpGPHwCF4pQO8kyiUIbcc2zn2Mg3XBlOgqh_CPQ6Na3F3HeJPVaAh64TlrebG6xNkPXbfoh3ivYGIR119oh9x5FSu0iyaA9LDaRGjYWWKQkMuEwsMTEmN_M-McYSaKmMrkzGl1XV7ugdr6p1qnzi6kqrUQFxsAPmW9YJ8I-08Ko6BOwWG1L1HcEg5otiJCEEX96iTklecLCgK8ZYFCiilboZLCjt75Y2X9U7xRsWU6y5qRQEc-RNSY2DukPgX0VhkIMUv0lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTbCqtj3_UAvgZFgJhpy7P_FWbf-fFd-OpC6poiDcKpowzjCU5N3SHqGLVpeEoL0zw5wC-34CFXI5tio16zH8C0ZvRa3cux_nHJbyapNdoA5ubqVoxvZhYTdZgza_d_5Btw0Mjj8hF665l3c6iaFipbxtvQQR39ybbcdVWiNykK5ZXhw-HhLM2K6CIqbxevJw2vBct534dnDyAg5hTGSeQtrXbCd4USid9Q3ZbiqZV3IIadPYlnlXwciBnaWpjmutCjjW88qYYPFUQ-HGAMXiU9uusAKVAsjI9mutJYsuF5UG04pHVKoRfxgnZnBknacqEDQ46PhVgcbJppVcrjCLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=bjTFkrU647h2TGLdIw6NPe_XumcVxgq5jGSftaXqwJZbvSRVR_jHNfz6yqcklHJMCdJ1GDPGisLR7Fvn83n_vbhwxYQ-9oX3Gow4KYoPLIzvYn2Gv5Za19X16mD3KrAxUWHdLn9_xdQPsqfo8TFt3bPaq1mpmTgfR08P35TZKQfY6GQrK-dimW8gLcEtFaYJZcI2huA8Ig1HJ6TSQBPaxzbRSZucnqX11TZstAzTwuOCrk-JfXYQQYzn_jm_uTfOFDhC3Xqjqm4VFBwFZxyniSEvDZKTRyfNsjQRhAAxqJPt50FDLZyrDM1420SmzMReT-LndlizuD9p_qPgcl_fsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=bjTFkrU647h2TGLdIw6NPe_XumcVxgq5jGSftaXqwJZbvSRVR_jHNfz6yqcklHJMCdJ1GDPGisLR7Fvn83n_vbhwxYQ-9oX3Gow4KYoPLIzvYn2Gv5Za19X16mD3KrAxUWHdLn9_xdQPsqfo8TFt3bPaq1mpmTgfR08P35TZKQfY6GQrK-dimW8gLcEtFaYJZcI2huA8Ig1HJ6TSQBPaxzbRSZucnqX11TZstAzTwuOCrk-JfXYQQYzn_jm_uTfOFDhC3Xqjqm4VFBwFZxyniSEvDZKTRyfNsjQRhAAxqJPt50FDLZyrDM1420SmzMReT-LndlizuD9p_qPgcl_fsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=kgMgbTZGQlXBRx6FY-rpZvz3QAu0eyAAc-4aJg445w22ZoQCM8Ihh8kr9sACd0dozd3bn68rt15e9VZOgn7QWQ7oDDf6rLjUf3qV3bxnXsGU6pvOlKEh7AjtxoemB6P_2o4ixQCVL3IpEpu-9GQF66d6MIcLWhhqSa_AJTtzqHp3SZXUp0C5JoH-oW_YXRfRz6LazHiUxEdPJbdmB3DF7nvwuBktyxPktwS0dcy81wuZI1vr_51sCvI3a-LN1FspAE3cpLw8j-c_8g9vQwxjFUpF3GJg9jE96mA9qi1zf4cF_327cfH7lpxz4av2ejMYfKkfT7LGRMo9c7HmUEmFkgBzF02Zm-BXaMmoJSWAUjLHvzBL-ljQ7uMnhq_qcFvR1AIbrPfLLJWSkvmo8wTsIln_3DjIYncIkrZ-D0AWKvkpzI8zQhuLU_vzfHNx6Uglwqr2ym-pjdqSFk3xvwm4apWAsdDY1IdxhUylEr3Z722MvbQ5wDGcoo4rbbP8cgo7KoOWszY4kP83mRk8mtgE1VIyHp2Y53Q6lt5eSYWlnRBMU8A0bEay99jv1QQF2NGV_kR7wW79qF7JO1Bf0A7bz5aQ7XyJEvj0dk5Imza9O_UrLoeu8zDLeRp8c2d5YcJWVOMCcVM2FDQGleXPnr4F0mYRDOYY_eXJi5Ndos3lK6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=kgMgbTZGQlXBRx6FY-rpZvz3QAu0eyAAc-4aJg445w22ZoQCM8Ihh8kr9sACd0dozd3bn68rt15e9VZOgn7QWQ7oDDf6rLjUf3qV3bxnXsGU6pvOlKEh7AjtxoemB6P_2o4ixQCVL3IpEpu-9GQF66d6MIcLWhhqSa_AJTtzqHp3SZXUp0C5JoH-oW_YXRfRz6LazHiUxEdPJbdmB3DF7nvwuBktyxPktwS0dcy81wuZI1vr_51sCvI3a-LN1FspAE3cpLw8j-c_8g9vQwxjFUpF3GJg9jE96mA9qi1zf4cF_327cfH7lpxz4av2ejMYfKkfT7LGRMo9c7HmUEmFkgBzF02Zm-BXaMmoJSWAUjLHvzBL-ljQ7uMnhq_qcFvR1AIbrPfLLJWSkvmo8wTsIln_3DjIYncIkrZ-D0AWKvkpzI8zQhuLU_vzfHNx6Uglwqr2ym-pjdqSFk3xvwm4apWAsdDY1IdxhUylEr3Z722MvbQ5wDGcoo4rbbP8cgo7KoOWszY4kP83mRk8mtgE1VIyHp2Y53Q6lt5eSYWlnRBMU8A0bEay99jv1QQF2NGV_kR7wW79qF7JO1Bf0A7bz5aQ7XyJEvj0dk5Imza9O_UrLoeu8zDLeRp8c2d5YcJWVOMCcVM2FDQGleXPnr4F0mYRDOYY_eXJi5Ndos3lK6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcbq1b3rfNAVoglMiz2nVgLJMclcknr48A8QaOMe9PBnL_mFArx9ZFzsMhUbCPmmKzWcq305cdBLTduhNYUfMXONEG7f3Gy_nJqVAD_l3tVrrLfFIGNlPJVxTbk7UkJ_jf_-HNwa8gqrTT72rpnrPso90O47Za7ZK9n2IqtEM2WtfQ_fGDgTAZ-XETZiOUDl6mZLKZcAp2RC8WFQiq9YreUzaMh6TgobN68_YnGK6Cw6kY2uwQuDPnZj8T7txIe3_gvdVOdAQPT3oA-TN_LcbocUB75qnVhtwPlMesM0mNL9Y_gxTiHpauTOZdg7nrk3SLy7SwNBKobILpP68YI78A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=ewJLvZCOhxq9E_5w5BU1AKGVDWAhfFTvKV1uTAbhFyQyz_TlNJCuKoXrD3OIyYNeHCtmb9KUxsq9ZKCDhhtnEdkLpXK9kEh0DsyfQkdf8DWexh7RJheGQF7Lv-Cd91KWi2cJGoE5Tz9nF_mj1Idi-eax-HIQ_oiBcy8ZF3cRAt4vQf9n-Ut3CyuBtam4akgOqnQjqZlqV9deU22H3ulIobjzXXB_31fsFV3ByauZ8-2aOEWk65S_ozuEKdgQ-t6UPUif3z6n81phE6fIPwvV8H43AobV3e0FJ6h2D1HXsLZacl1MnhnbMZcPVyunep5soWUkegASRDHEHyKB0ipBh7yCBd5b3d6ll4vGbuCycZ-il6vK5SUk212JWr8Eh6DQqXchFNGT8Q9q37BBijlfrvT0jGlecdq6D6P46noWKT5rxznp2JiNwl-75XvDHj42RnzwKeTtyvcpQtA_QZfGG_qgHM3_7MZ1odRXDSOVCSUFOVbHc1shuoh-OpgfdU2FCVcHtdPkKaQqgRs4_7xrCAJwvTwpzhvCiYul8gkncF6UFPucg2zowSd5tnUmopA2hUZQ6ZjTWhORa515RDzD8fqIz_CP4Bjp02QyVcUb4G8b_WpZTBEHcEWcdPXTfatiRkhQhZE9tbawv0rczLNx3SWgyGWpsfuN10KQ1oA7e4c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=ewJLvZCOhxq9E_5w5BU1AKGVDWAhfFTvKV1uTAbhFyQyz_TlNJCuKoXrD3OIyYNeHCtmb9KUxsq9ZKCDhhtnEdkLpXK9kEh0DsyfQkdf8DWexh7RJheGQF7Lv-Cd91KWi2cJGoE5Tz9nF_mj1Idi-eax-HIQ_oiBcy8ZF3cRAt4vQf9n-Ut3CyuBtam4akgOqnQjqZlqV9deU22H3ulIobjzXXB_31fsFV3ByauZ8-2aOEWk65S_ozuEKdgQ-t6UPUif3z6n81phE6fIPwvV8H43AobV3e0FJ6h2D1HXsLZacl1MnhnbMZcPVyunep5soWUkegASRDHEHyKB0ipBh7yCBd5b3d6ll4vGbuCycZ-il6vK5SUk212JWr8Eh6DQqXchFNGT8Q9q37BBijlfrvT0jGlecdq6D6P46noWKT5rxznp2JiNwl-75XvDHj42RnzwKeTtyvcpQtA_QZfGG_qgHM3_7MZ1odRXDSOVCSUFOVbHc1shuoh-OpgfdU2FCVcHtdPkKaQqgRs4_7xrCAJwvTwpzhvCiYul8gkncF6UFPucg2zowSd5tnUmopA2hUZQ6ZjTWhORa515RDzD8fqIz_CP4Bjp02QyVcUb4G8b_WpZTBEHcEWcdPXTfatiRkhQhZE9tbawv0rczLNx3SWgyGWpsfuN10KQ1oA7e4c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=aUkrErzblmG9XYKEWCzpWBmT9bZXfhr5QTwQFB86sr5T2eQPMzotehi7gxe2fH-anHr99TUZGxr9dq3ZpT2_aD0GzQYwTf-XOQsa3N9a9WX6ws4Km2kE40q26bRtiGz2Hvp9ZeQsXkj--pNDNCzIUSzSnrv2vOOqQxDLzkxMzlINYAqSeIKAyqDnLYqtBR0-TfM1NYdumSL61MvGtQNzcR1-HOpaFuj0h2QKxzfqEMj6_cLrGHXFaAIVl4HpHKoSu1YpaR8WMp2uUZqLbPfVxuCLO2AaxDsciJ98Kj_H_fbEgcH5legQ-soRksEqVXfQg674uP-eC6ebfwbPsgLlKiZObnDmvGglExGHPmJ2BmOs0K3tcNVPosfOBGSWf69Q1DHC74RXsiU3Y7b3pIb_5iU5GCieL86OJpMDbKhTqCBNYza4LY02JjgvnNOlektRL5DoNgwtzowoYGC922qtvZewXyS5_5w3oJgalfZjksvfRNJc_gh3QOUgO3CqM6CAhPN5mTHeyepOPScd8GpsVmo9GCfhs8V7CavpdIhu1sJEycC2JuJo1Kuruj5gNIB20Js-QSDerKFG_IeU8rlas1cTtbjDWbTnXpW8btR8zRfjd4SuN6_-wyykPJNubnrZNRA6-fMPra1Xnfkj7QFrs_TsIUndi2U4GaVrfAvkfdo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=aUkrErzblmG9XYKEWCzpWBmT9bZXfhr5QTwQFB86sr5T2eQPMzotehi7gxe2fH-anHr99TUZGxr9dq3ZpT2_aD0GzQYwTf-XOQsa3N9a9WX6ws4Km2kE40q26bRtiGz2Hvp9ZeQsXkj--pNDNCzIUSzSnrv2vOOqQxDLzkxMzlINYAqSeIKAyqDnLYqtBR0-TfM1NYdumSL61MvGtQNzcR1-HOpaFuj0h2QKxzfqEMj6_cLrGHXFaAIVl4HpHKoSu1YpaR8WMp2uUZqLbPfVxuCLO2AaxDsciJ98Kj_H_fbEgcH5legQ-soRksEqVXfQg674uP-eC6ebfwbPsgLlKiZObnDmvGglExGHPmJ2BmOs0K3tcNVPosfOBGSWf69Q1DHC74RXsiU3Y7b3pIb_5iU5GCieL86OJpMDbKhTqCBNYza4LY02JjgvnNOlektRL5DoNgwtzowoYGC922qtvZewXyS5_5w3oJgalfZjksvfRNJc_gh3QOUgO3CqM6CAhPN5mTHeyepOPScd8GpsVmo9GCfhs8V7CavpdIhu1sJEycC2JuJo1Kuruj5gNIB20Js-QSDerKFG_IeU8rlas1cTtbjDWbTnXpW8btR8zRfjd4SuN6_-wyykPJNubnrZNRA6-fMPra1Xnfkj7QFrs_TsIUndi2U4GaVrfAvkfdo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=fdrnV5PmDfzTDehGe4rouYd0tk2JcobXl9NOVew05wowoDU8oglS1wNP54oisycmq-1WDZyxfp4TUlTT9A5giQQZgwd0H0dKXRa22bTmqnITq4lVOUWRknhlDKugIvNGEYa5rsSJIqxqr2qh2TuScQeM4PBU0kMW55Tf29At6YVj2N4MC25ieRKGDWfDdtxQ1oENpr5m0Ae95mPtN_A-xuVpm-ZmTbSzSGGKAbnYTnSGTXwpC_LDWbqVxnPcze9LLQbHrnD9MhDyfji6lSd-jRNUMV8QTpf4CH1UZePviI-PfF9wI67ENHlu-asoTzTh-znfRhAI1x_b6eVHA1wdIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=fdrnV5PmDfzTDehGe4rouYd0tk2JcobXl9NOVew05wowoDU8oglS1wNP54oisycmq-1WDZyxfp4TUlTT9A5giQQZgwd0H0dKXRa22bTmqnITq4lVOUWRknhlDKugIvNGEYa5rsSJIqxqr2qh2TuScQeM4PBU0kMW55Tf29At6YVj2N4MC25ieRKGDWfDdtxQ1oENpr5m0Ae95mPtN_A-xuVpm-ZmTbSzSGGKAbnYTnSGTXwpC_LDWbqVxnPcze9LLQbHrnD9MhDyfji6lSd-jRNUMV8QTpf4CH1UZePviI-PfF9wI67ENHlu-asoTzTh-znfRhAI1x_b6eVHA1wdIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=NXb0cXDMclhTnZiXeIAcsHq2ot4iVe7sYe0LOs2WfoDOAuT7RQdm96F4LN4lNtRXkLaL5RlhCDeOZZb88DdhKgxolt0rClYCSjn4NT2mT1EwQMykjdtHB5-9lmzTXc5doYVwPUr4xqfiEANiPZ_9md7_LQPwRDy1TLXvUyR4N4L5LH1r0ntExUaOeOcNxbdMg7kH68pTh6lt-4FpbSilOPApfdYH4SD5xhe-gZSu4oRZo1Tu24JlO4FYlAPedb_8O82foNInN1qHKWQWFEQ8NqdKlh1ESEWuM-Lx8FdCmWqW53pfF4AAw6APDmHPb30oo0A0aTWFGSQq681tHDo3JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=NXb0cXDMclhTnZiXeIAcsHq2ot4iVe7sYe0LOs2WfoDOAuT7RQdm96F4LN4lNtRXkLaL5RlhCDeOZZb88DdhKgxolt0rClYCSjn4NT2mT1EwQMykjdtHB5-9lmzTXc5doYVwPUr4xqfiEANiPZ_9md7_LQPwRDy1TLXvUyR4N4L5LH1r0ntExUaOeOcNxbdMg7kH68pTh6lt-4FpbSilOPApfdYH4SD5xhe-gZSu4oRZo1Tu24JlO4FYlAPedb_8O82foNInN1qHKWQWFEQ8NqdKlh1ESEWuM-Lx8FdCmWqW53pfF4AAw6APDmHPb30oo0A0aTWFGSQq681tHDo3JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=ddc1DBL9N4G_CBJhccDt0wLmPrc1cmqA_BlfmCUNCcw-vSSPiSVJjv8t_vhJ5DyG1Jnb13TjQMXP6dkhrQfTXVsRNtUF4qlUU90a9hHOjMi4_-tFicLi68zWC7V-DSHa9QtBLHYzSGjmBWQQLVr1a0PwuyGFEnAfq0Mo6tCSIj9oPxL9n1abZK1cfhCPXFR6KsGnudfk1p3eE17sNoAd-YkDgPutPvABefEx4059KRE4IexDD4ruliTxmLk8vNpJS8BxrFDsLYxYfFbIUAamBWNqt_PL-x_xkp4CzfafE8fBiAz60hCjdYtOn7E0xdTsYBrWLGUC_JIJGoxMfki5lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=ddc1DBL9N4G_CBJhccDt0wLmPrc1cmqA_BlfmCUNCcw-vSSPiSVJjv8t_vhJ5DyG1Jnb13TjQMXP6dkhrQfTXVsRNtUF4qlUU90a9hHOjMi4_-tFicLi68zWC7V-DSHa9QtBLHYzSGjmBWQQLVr1a0PwuyGFEnAfq0Mo6tCSIj9oPxL9n1abZK1cfhCPXFR6KsGnudfk1p3eE17sNoAd-YkDgPutPvABefEx4059KRE4IexDD4ruliTxmLk8vNpJS8BxrFDsLYxYfFbIUAamBWNqt_PL-x_xkp4CzfafE8fBiAz60hCjdYtOn7E0xdTsYBrWLGUC_JIJGoxMfki5lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=g-6vlVsb8Y3ccRAU-Fr8_e4wLvx-ZPRikAZ6oosnV2Fr24wttEb51RH7STw5CyXLz6HTgQngcVqQYKAZFR9MpEQ8j2JnHcbzXXwnffHRE4Pvqqzvbha2sOjidFDMr6ohxC1fXxap4Fd1Dy9PLZ0JRnBF1j4GkETilNAmDXRIWU_JyDEQO0-vYPaLb76eAvmYk4-Fj2AuJAoTNWMXF433QtRxtO19d0VCssFACHYnlkq-eSDKs9mQhijajtnKRFTtYPKBf0Svnkfa5N8x9eVGnUVxvD2KkoCNfgA8QYmp5F9JmC4dS-B8VsNSRQmMoSj4UBYDATZBlH8TSy_2rUFpQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=g-6vlVsb8Y3ccRAU-Fr8_e4wLvx-ZPRikAZ6oosnV2Fr24wttEb51RH7STw5CyXLz6HTgQngcVqQYKAZFR9MpEQ8j2JnHcbzXXwnffHRE4Pvqqzvbha2sOjidFDMr6ohxC1fXxap4Fd1Dy9PLZ0JRnBF1j4GkETilNAmDXRIWU_JyDEQO0-vYPaLb76eAvmYk4-Fj2AuJAoTNWMXF433QtRxtO19d0VCssFACHYnlkq-eSDKs9mQhijajtnKRFTtYPKBf0Svnkfa5N8x9eVGnUVxvD2KkoCNfgA8QYmp5F9JmC4dS-B8VsNSRQmMoSj4UBYDATZBlH8TSy_2rUFpQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=B3woBjurMZtIWrDhwZ0q43mO3rfjvlbL5FKmFbycOZfBwT9ZQ6tuEKstEmLeTTQJ9Bo7bNaAXD1u2QvUl9Ignnd52wgRA1UA-gem29Z03NhAOrkIxMDQaKjw0yjLGpLjeB8UlZiieLg-qyvhdvOYPbt79syFONFi9FUHNDhaNoj-D9TJ0M1kOHjf5cpuBDWS-7NpU51Dh0-M_uZBBOKC8JdOY-HouXwwTKXkavAILQM73ugRuvWHoH5LwH2Sqy8axA-4piyois-LEHlkfGUujKTNn19YGw0VnyHXpm4VUF-k6whAcC4s0qUamuYdbNQ8tON5WTkkLtsInvD_SozV8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=B3woBjurMZtIWrDhwZ0q43mO3rfjvlbL5FKmFbycOZfBwT9ZQ6tuEKstEmLeTTQJ9Bo7bNaAXD1u2QvUl9Ignnd52wgRA1UA-gem29Z03NhAOrkIxMDQaKjw0yjLGpLjeB8UlZiieLg-qyvhdvOYPbt79syFONFi9FUHNDhaNoj-D9TJ0M1kOHjf5cpuBDWS-7NpU51Dh0-M_uZBBOKC8JdOY-HouXwwTKXkavAILQM73ugRuvWHoH5LwH2Sqy8axA-4piyois-LEHlkfGUujKTNn19YGw0VnyHXpm4VUF-k6whAcC4s0qUamuYdbNQ8tON5WTkkLtsInvD_SozV8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=LzduDg4Pgydo61foaYUVMOkIP8N-pnSenihwqsAaUjT0Th_lRoyJRbITk08D8oazQhOq0mzL1UISXx3pFdmhzyF7oSY_CKScYyrDcnH2JT5N5yw7MYiPn7GVZMoPKvr_C9BhnRcutkQByMb_aUXCN5U61vLcHsVGx73XaPxhuVRYi7iyMt0OVoVBDs7NjY9PEZgNtFj6QbQD9EIeg2R3y20FeX5JcnVbVX533Kqda0_iU7AIFx277DULid0RSMK_G6dZKCUXjZEakXrkqRCfsqqUC5A_SYzJz1T60a7qtmCRtHpz5NMxdfdTHsXMLvDDWc7g9JMOmhPMhmtNV4BDaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=LzduDg4Pgydo61foaYUVMOkIP8N-pnSenihwqsAaUjT0Th_lRoyJRbITk08D8oazQhOq0mzL1UISXx3pFdmhzyF7oSY_CKScYyrDcnH2JT5N5yw7MYiPn7GVZMoPKvr_C9BhnRcutkQByMb_aUXCN5U61vLcHsVGx73XaPxhuVRYi7iyMt0OVoVBDs7NjY9PEZgNtFj6QbQD9EIeg2R3y20FeX5JcnVbVX533Kqda0_iU7AIFx277DULid0RSMK_G6dZKCUXjZEakXrkqRCfsqqUC5A_SYzJz1T60a7qtmCRtHpz5NMxdfdTHsXMLvDDWc7g9JMOmhPMhmtNV4BDaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=K77Bm8HospiOdVIg3ndY6NnTijYiB7cGflawIjDm_LCc76NcPLl2mgT10GdY8LhyLUMVNcRlCTUekBdzuHJxVa3Z3_N5hUQqu9W15SmRPeORxrRNKfMTGaSeM0beFLaqxJseoJDqVF1SrUEDe_v1ILz90nmWr-O7z2R8u-TVSIIRdLmzc3Ew-ahpqHChwnP_s4pqPEkRmgbzIDRvTBp4Gpw8D3Vt54ZpWeOGDqK8Cq4JdrWcXsE8b5plKULf2euQVNbtfQxzn0NRMYc5Qcqk6HkI4KJj0XL2NjdRiDT0Niy9cIdo1B-u5dLd-nKAJP4NuaJnaxZul-eYrfO-5PDytw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=K77Bm8HospiOdVIg3ndY6NnTijYiB7cGflawIjDm_LCc76NcPLl2mgT10GdY8LhyLUMVNcRlCTUekBdzuHJxVa3Z3_N5hUQqu9W15SmRPeORxrRNKfMTGaSeM0beFLaqxJseoJDqVF1SrUEDe_v1ILz90nmWr-O7z2R8u-TVSIIRdLmzc3Ew-ahpqHChwnP_s4pqPEkRmgbzIDRvTBp4Gpw8D3Vt54ZpWeOGDqK8Cq4JdrWcXsE8b5plKULf2euQVNbtfQxzn0NRMYc5Qcqk6HkI4KJj0XL2NjdRiDT0Niy9cIdo1B-u5dLd-nKAJP4NuaJnaxZul-eYrfO-5PDytw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sn1n4IFpYzT9w-xqVGIeN1s1EbUjsw0c7iIJ6PfVNR_nLdLseWMbLELi-VXwtPY3yb_LFGiEJoSARnGiW6iz2hpR0ev_nHu1hUMPALgo8kcjX8piglBy7LMwEVleDeWz84dUbMS7AlDYCb6TiBci3aCEye6yPZfk8MaE_JOO1-sn7RTmlP-VqNMkwGeRWiIGf6_0DF_cNS3Scwe0gX8bqBpJQZRPFt18nam4XO1cA7KB5oEz-KkL4TJyiw12iNvAv9FpveW0uaOdSQfAf3Rwf89jMUOl7uuF0NS67Mcd0t33L3UgcidDm4YYwj6cFtVuKjEC51yDPnYMJCApw5MBdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=qsTWqJfue82gtzHdrmhpWF313ui606tFPzJq8VBtEx-k9y8trzQhHBCMy1sharGZytenh4sQamK8moa6M_sm2oJArUxfm9ic2CYzwqcKs8xF5tgPYm27HItUgM8t3dMkUQeEV-jwL9veK5r509ADV24DJ4QMrOUOAPglydGzYmO2jFRgqJBGtMAju9rZ8idxu_i-VBvUAls_Gm5Bt_f2qFZNI03IddDkQCkJiqXSUBCER81SRoWQq-su08g9eLDiQo5QsDDxIW_U4ELgDz0HYd9E1hkCI5WuH01dIoWnRD-bSjtl_YNJDNv4ZeFMkZudWHG0h0vPTYSzZzT6xjhPyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=qsTWqJfue82gtzHdrmhpWF313ui606tFPzJq8VBtEx-k9y8trzQhHBCMy1sharGZytenh4sQamK8moa6M_sm2oJArUxfm9ic2CYzwqcKs8xF5tgPYm27HItUgM8t3dMkUQeEV-jwL9veK5r509ADV24DJ4QMrOUOAPglydGzYmO2jFRgqJBGtMAju9rZ8idxu_i-VBvUAls_Gm5Bt_f2qFZNI03IddDkQCkJiqXSUBCER81SRoWQq-su08g9eLDiQo5QsDDxIW_U4ELgDz0HYd9E1hkCI5WuH01dIoWnRD-bSjtl_YNJDNv4ZeFMkZudWHG0h0vPTYSzZzT6xjhPyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=vh_wHOiTjrz3IjWso6IJDOdXyxFN6s0eRTielI-J4Jv0EaQxUyWoqxNrHlMomyNL1cSJrfqcXofNLhpbkCzXIGTRarkylPnBQGB1rr_UmBlq7fW85XKFMcT-nJeDWA68A7DBq1tNWSdBBvgOuD7dEhErEb8p31Zis8HNrNQPTu06WFfXEyP4XNQywZPoCDcZOnJSiXaMDXOqLDKxPH2tm2tRCC_4k8EsRGwPAioJeJ5TT-XnSPEzJ6CbPzJBzMAp3763XY7aLAwpiG23uIAeOHxphiwLJwBYEzXdYyRD2-OaKuP_xpP7ae72H-GJ8P-ic5ove0IXca9WdZB_-Als6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=vh_wHOiTjrz3IjWso6IJDOdXyxFN6s0eRTielI-J4Jv0EaQxUyWoqxNrHlMomyNL1cSJrfqcXofNLhpbkCzXIGTRarkylPnBQGB1rr_UmBlq7fW85XKFMcT-nJeDWA68A7DBq1tNWSdBBvgOuD7dEhErEb8p31Zis8HNrNQPTu06WFfXEyP4XNQywZPoCDcZOnJSiXaMDXOqLDKxPH2tm2tRCC_4k8EsRGwPAioJeJ5TT-XnSPEzJ6CbPzJBzMAp3763XY7aLAwpiG23uIAeOHxphiwLJwBYEzXdYyRD2-OaKuP_xpP7ae72H-GJ8P-ic5ove0IXca9WdZB_-Als6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=sng0nlh8CHUsNcoohq4_P28bda7Ow4e6rxsH1OQPGXMGzUiHOA6mdufGTEL3lz50KRLEcIi6hpIKX0k57wKfrnjZ9JqGlGd1yrxouNmYEFo7xrfgCKxegAjHdvhJ_yzjOwrcwcBJ4qzu6wWyDHvNj3-ldjWOjAAsvvKw94l7dpAw47_2IoRIJ2uNV12P3mIYzADgt7rjOeHle3agwFqfVfwMKQx4E8bhiqqjapb5-WtRmqZv_YUw_DTW2pCk9XEcJlx1r5tfehCSSitZ6LbUJfq_vobemVM8UFQ7wqBJmwbKohXM04bkIXwQ2-g0AGYLqQ1bpAQtrqL8uP-uNW87pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=sng0nlh8CHUsNcoohq4_P28bda7Ow4e6rxsH1OQPGXMGzUiHOA6mdufGTEL3lz50KRLEcIi6hpIKX0k57wKfrnjZ9JqGlGd1yrxouNmYEFo7xrfgCKxegAjHdvhJ_yzjOwrcwcBJ4qzu6wWyDHvNj3-ldjWOjAAsvvKw94l7dpAw47_2IoRIJ2uNV12P3mIYzADgt7rjOeHle3agwFqfVfwMKQx4E8bhiqqjapb5-WtRmqZv_YUw_DTW2pCk9XEcJlx1r5tfehCSSitZ6LbUJfq_vobemVM8UFQ7wqBJmwbKohXM04bkIXwQ2-g0AGYLqQ1bpAQtrqL8uP-uNW87pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=EMh9OAPoHp_gom-Mzd6dn2VRAPB6KI_XQhQSf4I98rIi1K7PCAoM2XyuPooiakboMx7lkJTizQU4ei69fduajNs-6Lsc5IJ1QhXfl809xXEj9K8QXLTCvJnfRj4fycM6IUdhKD37-K8uym0nX76Mvpy9CHC7ZdM3xa-X3Zppo8qQHo0vlP7zBmKFf8D9vWyLADrz0u4rMcYp2_bP7gHLwTVqhZWDJbtKOgqgdKEtYrZs5obmwNLU7zY9W0s-bgyy7r-J2Kr06CCxjoqljjUUv2Eyq9DUteB4G95E1OZWVXKdM-D5uiPhxyCOVYjs7umzCwCShT8WScwN8X0WQ36-rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=EMh9OAPoHp_gom-Mzd6dn2VRAPB6KI_XQhQSf4I98rIi1K7PCAoM2XyuPooiakboMx7lkJTizQU4ei69fduajNs-6Lsc5IJ1QhXfl809xXEj9K8QXLTCvJnfRj4fycM6IUdhKD37-K8uym0nX76Mvpy9CHC7ZdM3xa-X3Zppo8qQHo0vlP7zBmKFf8D9vWyLADrz0u4rMcYp2_bP7gHLwTVqhZWDJbtKOgqgdKEtYrZs5obmwNLU7zY9W0s-bgyy7r-J2Kr06CCxjoqljjUUv2Eyq9DUteB4G95E1OZWVXKdM-D5uiPhxyCOVYjs7umzCwCShT8WScwN8X0WQ36-rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dknPO81wuYAoSR-N_kq-2DbhUBKNnbkyN-1xsOnech_4XH0EtEeuXyINst8mtbmxk4vt-4w_1hXh8pTT6c03uroM91PtqiiNXho5-QZYzXqoHwkYOCUQrtYiLlF6RLZSvlVbtQ9T2hCV3yAdLfqRGxPDnUnsH4gr12d83GA2tC4IJ3NvNlog3SutnxHKhmONF8DVrx8ujsy0D74XOPSAC3Aj3RU7kPY0hUx2lBsJvKDXtA9AFSkz1CR3lgDIlOSS9apYN3qQbc6Xo1Ez19faPQj9iv8X1yk8hTiBkuj71h2gvhoEpAgDH__Qb2PK0ClL5ZlBdy1VtIjTNKyiFRNHxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=vQti3EHQMuMUaMrjTbUsUxF8MLxonfitK-Dc5fGUKSjCEYQuU4rdbRj1U5l5lF-i6V-BTV_PlJ-mBE0L_rhX5hWMz5_lbZaJNbLUNlpFngp3HDrusOrH79FD46o8btylbLdfH3EFAdB3A8AzZtng16a1408ZvPrBm09Uik7mikyMH3r6L6oV6uiwOJlWTmYeFBYRkzgir_tXsbhj41rG2XlOekQBPhOgV2WcdMZWSn49gAnjgwlwQ-I0hPDX2i1pgDtaxQ0y0pcvvIOJBi_vc8gmpO0SeLtPOysce-QpbeH_9GiRDwE1gdLdBGc1RI3fnKhO98vZGbYc0iAVvoMLtjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=vQti3EHQMuMUaMrjTbUsUxF8MLxonfitK-Dc5fGUKSjCEYQuU4rdbRj1U5l5lF-i6V-BTV_PlJ-mBE0L_rhX5hWMz5_lbZaJNbLUNlpFngp3HDrusOrH79FD46o8btylbLdfH3EFAdB3A8AzZtng16a1408ZvPrBm09Uik7mikyMH3r6L6oV6uiwOJlWTmYeFBYRkzgir_tXsbhj41rG2XlOekQBPhOgV2WcdMZWSn49gAnjgwlwQ-I0hPDX2i1pgDtaxQ0y0pcvvIOJBi_vc8gmpO0SeLtPOysce-QpbeH_9GiRDwE1gdLdBGc1RI3fnKhO98vZGbYc0iAVvoMLtjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=hfUKnCACpl7jX1igtcxTrRyuxB9hgmD3ogbEB7Eo77XVveUUxZSZHbgNE2gZj9XC4bEvAp96bqOfiDsbU9B3Rty9i8T8fHPntnVEeX3zXmI95D3eTtSB9egRUjdSoLpa2bJGBLJCDv_dRO57hoObkso31NcXqrYwuyxTx_Eg8ISTvVR8Se29WZ5zsFEw6_6IwJyLHl2vMCET_wahGXB1hMQ8KG1_Li0DZZYb5QutYFXtf9YiRP7kVJANp8roSwKLM2QP2LZ1SWLumnju6j_mBK2i0TzvJgCbSIHOVHLBKpSj1YTeDbtAKYRVChPYfauZC4e1zqlWo32VMTAZlOKSIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=hfUKnCACpl7jX1igtcxTrRyuxB9hgmD3ogbEB7Eo77XVveUUxZSZHbgNE2gZj9XC4bEvAp96bqOfiDsbU9B3Rty9i8T8fHPntnVEeX3zXmI95D3eTtSB9egRUjdSoLpa2bJGBLJCDv_dRO57hoObkso31NcXqrYwuyxTx_Eg8ISTvVR8Se29WZ5zsFEw6_6IwJyLHl2vMCET_wahGXB1hMQ8KG1_Li0DZZYb5QutYFXtf9YiRP7kVJANp8roSwKLM2QP2LZ1SWLumnju6j_mBK2i0TzvJgCbSIHOVHLBKpSj1YTeDbtAKYRVChPYfauZC4e1zqlWo32VMTAZlOKSIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EWmoY-xlAqM9tH0EF82qPAwAAumLJeZB710shATPsYsJal9Oya_j7BcRmwGkOQodDg_7y5s0a5pXay_-roAEWxsG8vK-k7R55YBL5f0EWHUJv7dXXUvtacRVBkg1W8op77Rpzq_0PSxLR07IeA6iPtpCSA-ZG8t4mCCpluV493E_11AgfafcPIz1NB5kSCIOIiF2qDue0kwNl1DJtX0mERiS-_1_qJb6Z4h12lrjTqbsx5WD_rP7AzgHiFUhFLvT4IuCaTO8Ijvu-2HropkIJgknX3MCff0LR6IYFZ2L466KsSgVALYyBf6cs7GwUNx2IAQ09JvSs9BdM7E6LqHGIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z3Ge7R-2qYe9k4Q4wFoZ_YFZy-59WGu6obrxru_0PAB106F-z-L0iF-ztWvOSeQL1cZOBzVFqCzHT3DECOeJvH3nB932p4Ts_KCsb2DAVMFax1en0WVMc8vWm_27gJDIl2OmIWhECI1WfBlex1Id4r-XNvQs9YYUjlzvciHId9fNKOUxkPL5eT1kVz2HXsFtzvltOByuNFPngAmEt2BgRLreGjyZ_WtmW684WG0KBPtVJEnSnIev1LBEdLQlkzwqgXEKd4yX7HLF6_KP_IKE203grJF2guOeLUXmG2FzzDnWWhS9Gc20cB6fwHA7UFJxoKgTMdQ3nRdxE1Jz9ihkjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=qpsQ_L_8sV3O7zr8ODThiajC1XYDaGzVFkf07SsvjOGLrQChRhRQktaAMW1ZcwOLv0uIi7bfmBFiwua7xSWlv2XpkSVXO484fbF5llbopMxC6HKvDNdMmh-OVHVz7srzb1V7B5HNeKH51m1nanuuk_6cfrIoDSOcipreuOyh6cCWwV4hs0cP-rLK5CzXM2SQloZbwDCZtFahqwyASlkiyfj9E4_-JGcgn1DkQFw6RQ7ly_nPiRxtqPzmNk4yqe5Bt605j_FfjPiHEVXWIY17vD45PIujAmaEMk2SVMEFC_8U9UmH-7W-FbdU5ZxWghdefiEyOnZMMRf0ZDTOudFrcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=qpsQ_L_8sV3O7zr8ODThiajC1XYDaGzVFkf07SsvjOGLrQChRhRQktaAMW1ZcwOLv0uIi7bfmBFiwua7xSWlv2XpkSVXO484fbF5llbopMxC6HKvDNdMmh-OVHVz7srzb1V7B5HNeKH51m1nanuuk_6cfrIoDSOcipreuOyh6cCWwV4hs0cP-rLK5CzXM2SQloZbwDCZtFahqwyASlkiyfj9E4_-JGcgn1DkQFw6RQ7ly_nPiRxtqPzmNk4yqe5Bt605j_FfjPiHEVXWIY17vD45PIujAmaEMk2SVMEFC_8U9UmH-7W-FbdU5ZxWghdefiEyOnZMMRf0ZDTOudFrcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2V_Hmz49W109Z1wXpXI0uvB9Pi4BDEjIURDTF3L2CVItKR0qJecAH_0BIWtobd4Cmh3npR0dhs3v2gEebtQaeUURkganMyKPDXSOxrwgO6CNrYRSNAbwziPgxI7Wi1w2Qv72u5brRh5HONIXN4juU-MitEVLQg7fLUnhyAP8uEQiviyeclaJ2BaCmwibFi7R6YMUIzQvDpgnIKQVTKn6O1X0k3NrSiYe_3qsVxFl6_ckuffg83Sro5VXStRoyPsoqKGSTgq2i6OrHnsxu_hYLjl6UU4zIe4BsFqPW0Tbp2ohOpbom04Pd5pUBADKTDXBT8byraR7dnCcQGC_R4aHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNMRAo-6zlIcWHwk54715SkOqj5ow6leYIgMs6hZDuqowGNvCfRp3hl4oPFjR6TG1LlAGMOAqE6BM_MriRpHq-5EB_2-Mm23R0wjO7KVECmyV_uVmzxUiHJq7_GsMSace934nAOC5uWG58_RWQfShCQ4jbTD_fWVlJEzmZfvGjxKWKQgt4s-lTdoAs8rrhfrco8VYOlHmDDsVODWt0TgrgAQoHAFvbGz1R8wBc2MWcIpq7DkjQhP1hnwmMiKCouLoWzAUBeU5Zesu7Y2v1z2XqPEYsAh_nvyUQ1X-2WD7mQJRXHVruQhw6UZWmMq7iTqiM8C8BRlsoX9BdJDMOGtXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQfhH-h5BR3IoCBZtjbWNG3T-oBEaVTwuWxGSmlEgshL-nBtpQkUW32xMrOvMzBYR0R8cJwVrC-IClt0BDP3QwSJ8bB6PTrjwZJY6Iql6wZ7aDfV-oUKwNQKOGl6AG1GHgPdAaF9ahvw2-Lb1rFnCJB5t-81rH3zXUnSwwV7obkP_vXUhLU7aYBzkqiPGx8CAO032XFmSHHsB0hJu3H8mKPrA1a3Kp7rNWtkGphDwoBefpKnby-FGwkMJdS4U-CKJCB9Xk2xzZCfF1IQmWIhtrnc9gqynU-3-a1bm3RDff8t5op8kgOtE1acI8RVbUufbO9L6do9rZRbKeUgBB9dlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=HN0EtE_pROtiOGjf3xop5xN9B_IYoshjR1ybuvtvksdakld3ri09GknheAOLEKqbBg28OU0PLTPob3gmopvHstCKrljOtPC02nGnp-N3Ksjln5dj69s06ePgjgI9oAJcjrxQX2IEvfoM8U5X4_XAsQqTkWrmyRD4jdRlxEQR08YahDxAeERs9oCXUMxj-wfYNnQoY2AxJOWaexB7ybzlPD0IwtvAaP1ovpEH40zYixJropZNfVVqhndQBomjoC4vwQlYsKqdafjh7m87iaMZ93BP3nPinygu8_1WrvJS4UeX_KswsQSiqK9yIeWEtZQQ6aJDrfgN6Rp8eJpHPyJ0tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=HN0EtE_pROtiOGjf3xop5xN9B_IYoshjR1ybuvtvksdakld3ri09GknheAOLEKqbBg28OU0PLTPob3gmopvHstCKrljOtPC02nGnp-N3Ksjln5dj69s06ePgjgI9oAJcjrxQX2IEvfoM8U5X4_XAsQqTkWrmyRD4jdRlxEQR08YahDxAeERs9oCXUMxj-wfYNnQoY2AxJOWaexB7ybzlPD0IwtvAaP1ovpEH40zYixJropZNfVVqhndQBomjoC4vwQlYsKqdafjh7m87iaMZ93BP3nPinygu8_1WrvJS4UeX_KswsQSiqK9yIeWEtZQQ6aJDrfgN6Rp8eJpHPyJ0tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=Y1gx4pq8DL7LGHBkARvlsfeHOPTBQ15ie3Jjr_PsbvjvZ2LUqefVtx7Wi3azHN4IsxAKBjzKwFRK0sxKkosBFuuYGbUMczXfwkq56nADqQamqmJRX7lIaBesS1Bw27zKplh48s9h-Fx1gU87BNegAzYCjeah7jQNvd58HNfg5jRMSqPAszzTRryvmZqaTjPawrY9XpTRQQ05ogf-G6ANvYKiH_XCu9lJ2GzYWwKG1TtmQWEsPxxjfqb0SrNUQPDhqOiqNxrR7ejCx6bVNUqSr6IKJdsJFlxUjW0iK4Z4R7pf0U2NhaWVNWHQk6nSox6ar00jpv3ssh2hMx4s4x7SGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=Y1gx4pq8DL7LGHBkARvlsfeHOPTBQ15ie3Jjr_PsbvjvZ2LUqefVtx7Wi3azHN4IsxAKBjzKwFRK0sxKkosBFuuYGbUMczXfwkq56nADqQamqmJRX7lIaBesS1Bw27zKplh48s9h-Fx1gU87BNegAzYCjeah7jQNvd58HNfg5jRMSqPAszzTRryvmZqaTjPawrY9XpTRQQ05ogf-G6ANvYKiH_XCu9lJ2GzYWwKG1TtmQWEsPxxjfqb0SrNUQPDhqOiqNxrR7ejCx6bVNUqSr6IKJdsJFlxUjW0iK4Z4R7pf0U2NhaWVNWHQk6nSox6ar00jpv3ssh2hMx4s4x7SGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Xhhrp_jESDM3aGKAbIcj7Eutu8cttptUuvTsu1sv4afVdIzqzPpe3_vvR-nloZC7EMS4cXJ79V7AdrkLvDwRwR9KYV_CkfwM0Nk3d-a_ArNBL5mCG4tUK2fTcv_KXrqNiGCWyLMxLWV8PJjipQ34tyb2yuPlK5bJQ8XSraztVXaYehl9aKElgcjXB-QIi8y8Zd0EltaPE9Ww5ci9UtYr_TytgY8TUckhKduGQZgmp3aD3MxbsBcw6S5Xw4DJAUn-K_TmPoiXDfwMAsXnOanOvoNlKyl_UeI0VOLzy33YRQcPevBxKTxgrozxhKD0rcp2T-vRly_irylictB6onA5rqlr5t7ii8X6POKKD1Gfzwzv-3RYwq2nR7ZzhTigcoh7gIniOAzc7FcfvsuoSDqBGvteLTrJPcEWUIIqm8Yj9P1-1vvIugXaFYkfTMHaA39neLXOwMJPP2HTk_w1XFG2uBa58z66B05kLLT5XLcA_VLk-oSAPFBQ0M7pH1tBAu-hVkie9nEcChIzV7sdME3F_U6Iqwswyqmzisa-SlJsXfXVEmPRpJTBQJDC4JzzhqF-gz5u-NfiySm2u_ACFQTpLKNOT2adsCSVY7EmX3awmlG5-yXof_5YgiJjkohq15lSoOqx1LZYdWy36NQqaLa3Ag7m6C7iCH1h6wMFOLth9yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Xhhrp_jESDM3aGKAbIcj7Eutu8cttptUuvTsu1sv4afVdIzqzPpe3_vvR-nloZC7EMS4cXJ79V7AdrkLvDwRwR9KYV_CkfwM0Nk3d-a_ArNBL5mCG4tUK2fTcv_KXrqNiGCWyLMxLWV8PJjipQ34tyb2yuPlK5bJQ8XSraztVXaYehl9aKElgcjXB-QIi8y8Zd0EltaPE9Ww5ci9UtYr_TytgY8TUckhKduGQZgmp3aD3MxbsBcw6S5Xw4DJAUn-K_TmPoiXDfwMAsXnOanOvoNlKyl_UeI0VOLzy33YRQcPevBxKTxgrozxhKD0rcp2T-vRly_irylictB6onA5rqlr5t7ii8X6POKKD1Gfzwzv-3RYwq2nR7ZzhTigcoh7gIniOAzc7FcfvsuoSDqBGvteLTrJPcEWUIIqm8Yj9P1-1vvIugXaFYkfTMHaA39neLXOwMJPP2HTk_w1XFG2uBa58z66B05kLLT5XLcA_VLk-oSAPFBQ0M7pH1tBAu-hVkie9nEcChIzV7sdME3F_U6Iqwswyqmzisa-SlJsXfXVEmPRpJTBQJDC4JzzhqF-gz5u-NfiySm2u_ACFQTpLKNOT2adsCSVY7EmX3awmlG5-yXof_5YgiJjkohq15lSoOqx1LZYdWy36NQqaLa3Ag7m6C7iCH1h6wMFOLth9yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=nemjogX1nfiOWKdeZqXOvGvOMZDhSZRC0EYJfgG0iWb6eGqO4wComHJA1qsVfPl04zulXmZCiZLv2ZR8m3Bg-_ZkIlb5Ty5aCfiYPjeOR-bTTuFwVQp6KfpopB1KiaNEeZkugy3SgzFEYyyYez-Haa6mRuXfqRO_N8LsaOKj4z2btR1tE_WotiB0Is5WRUst5Hcx8UQekYxa5Vt7YRNl93unyyVJ3d9cIkjT1uXYPDz74_29cAt-v0I6WpzaV1sMkJvvLxSuV6IJQLZZIlotOYVf1kVi1_CaKnsE4RuwBHU8j08OW85OXBB6gyTqKNhZOD4LFQyVytmF-i4bmy65elTedOJOGR1m60QeqcoeRl1BTkYj6JLTx4aNJMuhJf0TAOVhZGX-Ks5lpJn3VNV8-5tOJxkIRf5YUrOla8wC72_HFV1B19bB0b2-1Xjdd4zEm1e1QuGF4kpUnKUPUGqFFuUOzpN3aO1rofglFURo9x_P66VU084Deyg9tPt6xQwuAy5_LjZ2plrpWub0ITuOdhMgIssRJZFtaXlOyXkHYj1xaXJWFF_dg9-fVzSrTpt3ke164w_z_m1uOxb6K062dyMHjkJRJXKz33cYyHuvBG3xfrYs-OQ0MQXIJ2hsVd9gi0nm2aejZJlw5mO5rmsXP3_9MNlOulgPONznqgpBrgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=nemjogX1nfiOWKdeZqXOvGvOMZDhSZRC0EYJfgG0iWb6eGqO4wComHJA1qsVfPl04zulXmZCiZLv2ZR8m3Bg-_ZkIlb5Ty5aCfiYPjeOR-bTTuFwVQp6KfpopB1KiaNEeZkugy3SgzFEYyyYez-Haa6mRuXfqRO_N8LsaOKj4z2btR1tE_WotiB0Is5WRUst5Hcx8UQekYxa5Vt7YRNl93unyyVJ3d9cIkjT1uXYPDz74_29cAt-v0I6WpzaV1sMkJvvLxSuV6IJQLZZIlotOYVf1kVi1_CaKnsE4RuwBHU8j08OW85OXBB6gyTqKNhZOD4LFQyVytmF-i4bmy65elTedOJOGR1m60QeqcoeRl1BTkYj6JLTx4aNJMuhJf0TAOVhZGX-Ks5lpJn3VNV8-5tOJxkIRf5YUrOla8wC72_HFV1B19bB0b2-1Xjdd4zEm1e1QuGF4kpUnKUPUGqFFuUOzpN3aO1rofglFURo9x_P66VU084Deyg9tPt6xQwuAy5_LjZ2plrpWub0ITuOdhMgIssRJZFtaXlOyXkHYj1xaXJWFF_dg9-fVzSrTpt3ke164w_z_m1uOxb6K062dyMHjkJRJXKz33cYyHuvBG3xfrYs-OQ0MQXIJ2hsVd9gi0nm2aejZJlw5mO5rmsXP3_9MNlOulgPONznqgpBrgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=elQNss0Wdg7ZZ_9l9DA6T0X1nVkSuoINmueUzF0MKOXVMNut_G2L7ToMeX66kf1HB6KlNnMNjB9NhV-CNOzPE30v9ONZPG1OuzhzppRBFiqt6ZS--kXAPs-hZlvsc5WkZc14-AocodvovTrreIjESz9u5huqLPIPR_Fqe5TS9K-E13E30Nq8GFIVf8Cmf3VUgvdI6EkSEBKlE-laq-CHPGv4Vt4JdKf46CJqGIh71QRa7wDkEz1DVaWLLlMY-PXqe_IQzkBdycbEdBOlR6ZSX3RSk2r1UldsFSH9CE6HVwGtI43laflFfl3J_tvc3wkaq_drUrFyxsjHReBr_nEr2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=elQNss0Wdg7ZZ_9l9DA6T0X1nVkSuoINmueUzF0MKOXVMNut_G2L7ToMeX66kf1HB6KlNnMNjB9NhV-CNOzPE30v9ONZPG1OuzhzppRBFiqt6ZS--kXAPs-hZlvsc5WkZc14-AocodvovTrreIjESz9u5huqLPIPR_Fqe5TS9K-E13E30Nq8GFIVf8Cmf3VUgvdI6EkSEBKlE-laq-CHPGv4Vt4JdKf46CJqGIh71QRa7wDkEz1DVaWLLlMY-PXqe_IQzkBdycbEdBOlR6ZSX3RSk2r1UldsFSH9CE6HVwGtI43laflFfl3J_tvc3wkaq_drUrFyxsjHReBr_nEr2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpOEiCEX_K1FwMBbnaCoxIz6cWKDaeYE5G2nXDHIUaPN7hfKlH7H71ZTdMKPP6X62MdDctHF5i9QUYy0fYZvcdwH5KlTtPmRsg4qbhB3OygFcoV4Ra2hUCJ2Uq4u1Mx7RsWiQkeJTPEtdMegLgO72w5_qH-V7AamacduSQanM1Kwc_ca0A_qDgkU-4H-qgNw7nYgRpPkBWmXC60qjhPk3HZsQ_Bam1nBqhAoVlliZhLNbcDIVe11PnjrgATNrtti9zGZVPIOeJqTGTSOA22mk0Muf8VNJEF3LIl8okIK8beO5aI4DchXnsdn1V6KNb4ez_9x0-FvNnXgZBXC3K5Idg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=aOT3c1dYvK76PwXCuo4TVpwC44CxVfue4kYygV6Cl3zQzF7-w8CrzyQaReTreQbLKLhn7OXqHdG4-RX-8BYgjRZEWlTNimuq7cmiM8LG-IwARLglwjmnF3_4YHc61OXNjUYMA4XPgPPS8ftmeLSuM__MbMsbiFzlffSw0KT3KPQ4HlRNXVNa83WniEKDJltOQ48gqaE9KZ3t-BjVbdURAMN6iEJJRqKg28v6QS_tom_WsvPHTFa7HnkM0Eglso6aBKJ_qXINynp3na-7RgAlQ1Or0SEqd7PgkU4ojWpsvYWskwp5-MeeiDP5Z778AO8TRK_yVFyCUj37OTb82WZMYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=aOT3c1dYvK76PwXCuo4TVpwC44CxVfue4kYygV6Cl3zQzF7-w8CrzyQaReTreQbLKLhn7OXqHdG4-RX-8BYgjRZEWlTNimuq7cmiM8LG-IwARLglwjmnF3_4YHc61OXNjUYMA4XPgPPS8ftmeLSuM__MbMsbiFzlffSw0KT3KPQ4HlRNXVNa83WniEKDJltOQ48gqaE9KZ3t-BjVbdURAMN6iEJJRqKg28v6QS_tom_WsvPHTFa7HnkM0Eglso6aBKJ_qXINynp3na-7RgAlQ1Or0SEqd7PgkU4ojWpsvYWskwp5-MeeiDP5Z778AO8TRK_yVFyCUj37OTb82WZMYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=NR9-FPALG6ko5JEJ8ZfWmyjnkZGPh_neDHdDINFODfgYp0Suqc23Mt2R77HyAMPw2bdNWT1jC4clEAISf2-jfnZvORwx1haWuaXAvVwnR1MMe_ueyg2sZve9gpa8Mm3U2bB1EjEsnvdaliQxWKhtlVTNbXfnF9hoQULO94TR8xkXR13igBf1AgYwLwR6LMBpkY5yqj9H1zhBRE41fg5tjjcfBbDUokro8_BoQMGdMgGGzFKsIABvyuVim2klSAeTC05LyRw3HpLMn5tl7hfzt3vABaqVlblfpZq-7_uZmswKzEI5fxSIgenFEfDAHgupDfs7LztwU3G8Vuo02uNBlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=NR9-FPALG6ko5JEJ8ZfWmyjnkZGPh_neDHdDINFODfgYp0Suqc23Mt2R77HyAMPw2bdNWT1jC4clEAISf2-jfnZvORwx1haWuaXAvVwnR1MMe_ueyg2sZve9gpa8Mm3U2bB1EjEsnvdaliQxWKhtlVTNbXfnF9hoQULO94TR8xkXR13igBf1AgYwLwR6LMBpkY5yqj9H1zhBRE41fg5tjjcfBbDUokro8_BoQMGdMgGGzFKsIABvyuVim2klSAeTC05LyRw3HpLMn5tl7hfzt3vABaqVlblfpZq-7_uZmswKzEI5fxSIgenFEfDAHgupDfs7LztwU3G8Vuo02uNBlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZGMsgqz7YnEOW0yzmdpIXLMzNPqEQmxllgDJv9uQFg2LCmXgAXh4cGA-KGOjqDO_kkkxgcTqwe3bGhUNqYXhk3AL1RUQTIwmbJVdN26BljwZ4pJHC-SqvjRN96ObgwxKr4lidbn5UPNJ-ObTgQxkKDG7pfpQBccdf1lov0YogJskbjrzKqECIvdFzdDj_rJ5iMsDdSdiXKVGEYwuQzQra_wskbkOIwhwuARhYAE7lgpK_K1ajtaHG8j0KYdEhW6mgVYYlYFaAEPSRRDswoqPsaD2WnENzW-nuUZhA1F-21uPTuU0GKgD4aPhYnhdMVKOJuV97jVIIA-TALJxRVdyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1ZWzKXQ0_5da_7sDiOclqCeBuI-RSdaXDXK_0Yk-KAt4kfc8s9ttnIc46sGA4Vm5PvDmE9SGzrFw5JmZnkkUdWHIAjfc72dwsgI0UyGxHi67zyOhRKCCTISXXurxgPA5rZfz1T176x9cSVVRyA9JB1bupzGFt5xAe_bupKGxG_5WCEJu1Q7q1MkySvPsD7J6ml1tpdh4XXvJqnHfLj1A2Tpe6rqFNgxusK5Nh_-jiacuLOy8TNDtme4WXoYIqFsziTgpvRrRsCgLedrUhpxBn2fYVo1DzntLXlcZqktlNTbArk0mZk99KYpNk3oxANAwTyllyqIMFPdpiXeFuOQ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3e7A6BDcic6ALoxXXNm56f3KEsh7Wr8LL1uH9wZWEtSMrQELI8hCLGephGlTuO8I81SEqLr2PAOwAawzDF5X-2HJaeD2yLD0jBooWpjg2nU2Sv1U_ipJMsp4zDRRr1WNgs3l8YdMB0vSEjVa728iP2DKqaEE7b-z3gMIzRBVrv9aHfqwl5GZL8Yu7z0K7-4PTmid7mla4-4Wl51ICYjvjqJ_btuht3ksjwABhjA6nxIpP2MKdyzZmCNV9DO6bItwIcLEgKUMmHpgNJTLgvRfBDRPuUs3BPdyD7h7SepKnCizmuwYL5AXugDQa2krFIUQMbIbKfvrw8MjXYUbV3V3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPuT9egxMXoTKn8fUcjbEhDlvrJoFjZ1e9ieaUoV0ZDKE4qK6P9ftf7NLoQTrEMpcQM35AdhkujjbF893yNgXOMtyuNSbzYC_L_OS-J-IHnAysjUqL6OeWnv7tasa6Ddn8PhL_8pozUDizGLoP-1Kdg4uoEBFLhQ2QoIcfc4UWz7HNYAb4iFLmEpTOFWVZRWU7-rQ7xGT8wqQdNlocmRbBbpQchhK6FJgK0nHWb0dY5yRlzswBrlRiJq9HYqZpUR7nkQvDB8XTS984RETasPD1h-_seTbXvcjcqQ27McGYNIBJ3yOkJueF4pHR5LRF1pvqkhoSQ3CKtsJZm7BNZx3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKdW0hDR9uQIV_aoQFkWw9Uv3btUvouMXZ4oTV_7LJj3mViAOGt6kZlBkzY44KQuMxEVK40w8vy6Pcjd5xXa9xLtpOCivYD-T5V6LQdRjKwS-iKaKBtXfTLEo3R0LKu1UBqxqT9hxab003qmW70AlaRnjBcvH6WcAuyUJkj90ys1e9o5d_MsK-bU7qoG7t1V2R07mOBJG9uw9z9uZelOV6V9JR5xXXAwSeKMkSJVVhsZzXazp2a6Rc9VbTdRMJ3nIlM3SWOxZP6lf_B6AHRPG5r7E-8Yhkf68mEY9tYVJv23l26YBH9Qkej--G8MBcRilxCqf30d4mtGFz3vxRg4KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpzPgV1YP0hhUr0XhgVueiCz698yM2JeLcyQA2mHJoY9FVGrhF3fyNfMWvHdGhHknHpsilFoGFBh7OHwmJdhfk01suVSWL80nIolpBZreymi6lQdM6E9RUVXBKwaaTUxlJqkmrmb9jfQ9oz4__t688tjG2lsNzFQ7mZJ_7p2MOBnKBWPHQ2dso8c0PF7xspSKIBy_WvfMb6MNcJNtN7IAU2ADbD7eGcuFScyKf_Ie-zTF-kGYs9ItcbMgGS53jU6941m7YD4mlx9chk2Z-OulHLv2ZQ8-nU9ANqbB5jWDxxZ9Mg9HlmbyrNlvv9_za-CazdPfJ4oWrNB1NAXB2iUfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
