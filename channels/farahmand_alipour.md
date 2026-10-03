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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 21:34:41</div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ag1IpHgUQbCuvlKDh3wit_xSm5kxt-_bt41xzna8DfsLYs2iKX79o3dGsiSYBX2eXU5x8MzGHjImdtnsSIez-_fwTNwkKKtCXT8b5PAmdob-MriBoNikrysTQ0P0FpQgNehhKzP8v6IM7g30nPWXfIH-3kJm7xpn5v2pBBRg5meeIOBQ36_unB4VLXVh6Kri-MCTW9-eFi8Biq1MYH1j1r9Iv4ZFsubaiZzYC0rY3t5JYJ4FSbBbtMmSbUx3ZzI2D6_ywcJw5rZjQ6LB5edGBwjpFXGRdiYy2KFogcivwkF0JrC6g_72r9dOxeVv45k437HPrOTkVUVzlNmDJEruEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBmBd8TDGH46yrTS6wojmTylMkFwYR8yZXnewOs0z-VH-d-AdcNn5DraR3WHLvxSsYQb4H4T6BbvNDVf59Tuai_KtGBFY4XjvdLrQ9zE6LhN6Tu1DsqEZSIfVXEA5Ff4j1inU_uddtb_9805Czilbn4S68fuCnHYEyTGv8jwOXezpXRQ2uugMIPuWKJKLB393R7IDWxNiUsyYgrBKLEICsM_y00KNBLW0ikK1Q6TYWY9hHN_YJNw7XGVtiKKjvEeXtolvY7EqXu-eyHBHo9WPohtNQVBMMqSbnSSocematsbz29r3onjGwZZk52rG12-pO3sukgPFrsVknvh8YdREQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoQTpAGTsk1aVZdKV134P4FrAT2JK-xdGol5qGhIfZunmQohz66Cdm1eTB39BzQkL4EOWnj7IoxpT96g2NUUxCt0VvyURAUX8GnbIrB004art3rI-ZMELq-WdsTdVzaLtTIphwtZcLlAkbbrisvcalD3kWZi5Dk7qAxBP1Mo3W-ZKkIiJsCzQlLCA29r7_yeoIFnzweqtjqbN4UHahD9EJUNyk8ePFTNRtp9B--o0jGyJ9KivK6KEjaVpeC_Cj2ZXFuJg7YHYjqGiBNItPHwFg3lBA9mYqZB4uaKi8phkPO1kwiVPZAOBphm7H6sz4AEQJcMzrmIRPHKqefZjalI4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAvGxLw5iFW3sg0st50XFLG_O0acYcxGZq9PAPeFCNymCuFFs6CCAbCL8y_a-HGSZJzR1lVLZ7IlnpYB3ZaMceN4KplhCTAKyfNw25_L-TicSr1Nm3eo2y3z32m4y-zlFdzcUhVH6khltRu2qHskD_Xo9HLhRX1qJljebb9muEA0gmr0RRyGN3koQTBzQs6v6bDroLGVfGbru3yi-vB8TkVNzE4u08etavM_w1KNpGB5PPkZ8b6ItIsAOd-mjxzZLVrmtm8vQlScfsfKpkBbUpbCZZoB1HWjcC96k7LV7YCt4zlEbF0ZyAVfDHujFvemcs3TROJLO7RaDdUInlaWzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=VFhZFRcA-uLaYRUQohnIT36Ggoicee_umWpRCQUzlYbJt-PJD5t5ReFGQ64bvUz7BO83GX0AOl7zFLgOEnIv2PL4FoDfrHvrIseeeSdopneJEAMboPr0x7Q-CGRUnhQtQCSyj_KQ6Q8IleVOjqXlkJ-y-kEJIVwQdJOq26vZE7OqXcXZTQ-I8NWzRQNK7DAiXNYBoOfhnjQnFw4E7I34zUEAQb1bZf3lWXzzR6wng3e1Xun-DVlmjDf95AJKrHYL0t8wnK7GrZzNFfD2icEl65JSVwsCI95uUYaZQsCBhVoBZsLCEHNsjdA-0OlBLYmZLe-4bnD2Viuafz8Z0B8RiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=VFhZFRcA-uLaYRUQohnIT36Ggoicee_umWpRCQUzlYbJt-PJD5t5ReFGQ64bvUz7BO83GX0AOl7zFLgOEnIv2PL4FoDfrHvrIseeeSdopneJEAMboPr0x7Q-CGRUnhQtQCSyj_KQ6Q8IleVOjqXlkJ-y-kEJIVwQdJOq26vZE7OqXcXZTQ-I8NWzRQNK7DAiXNYBoOfhnjQnFw4E7I34zUEAQb1bZf3lWXzzR6wng3e1Xun-DVlmjDf95AJKrHYL0t8wnK7GrZzNFfD2icEl65JSVwsCI95uUYaZQsCBhVoBZsLCEHNsjdA-0OlBLYmZLe-4bnD2Viuafz8Z0B8RiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=MkBS5noRF6YxvpWUnjp1ai4L6j5ZiAlqKgzCWukleHcFLu4vHAt0hkydQ7ZgX6-ROqH11GpPGxklHtSh75srerXxSc30yShrs0vZdhMvYQjnfhiYlEGD_nvwQQ8Pi7w8WSLVHT4PnC_BkTbCatB2FVbAO9N_AfoYYrk0XHuOSPuZOXx_QKW7DwbchhZ5XoCzt5H0AmjDEKSPlKynP-qt1ARgScEjkXQFQkAC3wkeGzZK2O7UQs7ZrK_0mD8A_SWPHfNE1pg-fD4NSv8baWAMjWc5Q6txHUjXozBBAQJ4kTvqO_TzCk_rtGD0S-RFXKGTKRJeSIlbIeAh5U3QQUsEuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=MkBS5noRF6YxvpWUnjp1ai4L6j5ZiAlqKgzCWukleHcFLu4vHAt0hkydQ7ZgX6-ROqH11GpPGxklHtSh75srerXxSc30yShrs0vZdhMvYQjnfhiYlEGD_nvwQQ8Pi7w8WSLVHT4PnC_BkTbCatB2FVbAO9N_AfoYYrk0XHuOSPuZOXx_QKW7DwbchhZ5XoCzt5H0AmjDEKSPlKynP-qt1ARgScEjkXQFQkAC3wkeGzZK2O7UQs7ZrK_0mD8A_SWPHfNE1pg-fD4NSv8baWAMjWc5Q6txHUjXozBBAQJ4kTvqO_TzCk_rtGD0S-RFXKGTKRJeSIlbIeAh5U3QQUsEuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=FvRwkqX6kJqTaDTo3azmvm53RszVgaEzxwF5pHY3VJy7ypjL7jBBg9KKo45Q2b6N6C3GHmeauy9neBwmGceym0dIV6MaZD8wNxbYrMtnpWHfZzqih2IviumIS45Zmfl8q66hpnmDwFEOnIWDr9fJA_sn79Yf2AohXL4XRkc03WIQ5zt2gTnU40FDXyUqMKwLNaJDMfW2kPOP3c1bRYM1SvKBl4vxPvkAMr_B_96MfkncY8H_vkb1q6mkxQ-4dF_51e3YrWZhvu9M9B4gnDS72Zfm4UVVH5IjeWQWVx8pgYE67n_WTQuD49e6qV5Y_F9Wy6DJ16WXZZiMGHnZKsnn9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=FvRwkqX6kJqTaDTo3azmvm53RszVgaEzxwF5pHY3VJy7ypjL7jBBg9KKo45Q2b6N6C3GHmeauy9neBwmGceym0dIV6MaZD8wNxbYrMtnpWHfZzqih2IviumIS45Zmfl8q66hpnmDwFEOnIWDr9fJA_sn79Yf2AohXL4XRkc03WIQ5zt2gTnU40FDXyUqMKwLNaJDMfW2kPOP3c1bRYM1SvKBl4vxPvkAMr_B_96MfkncY8H_vkb1q6mkxQ-4dF_51e3YrWZhvu9M9B4gnDS72Zfm4UVVH5IjeWQWVx8pgYE67n_WTQuD49e6qV5Y_F9Wy6DJ16WXZZiMGHnZKsnn9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8hp38MrQSgMwASlvMSEVujB99_8ZeHXWBYMZFjkxBI9WA_6taqhoycUqYRr935WVJT5mreeNPSDuxLKLjIdSGYPUS_idQv_F5F2jclvzsfhFSvSMkRPZlo87ule7xTqqmMs_OcOZnHEcQUjDjFNbDjmodxyoD8_LhsSex5D7a7Cl656lh5hlikNDG5Q87wPv4BxwuZWXY7UJt92d7lJ5KoCJXO8ExsY6jGb2Ybe3hhK10LELp9DDBw9xEdAR9VDTXzRdXsIM9yPBASQUK7RWxOw0ijIuWK4LOUJqCRbg4Ic_wFIGWdCiANHo-XrtxEyVuGcHdcRvr6UCJjZAiWXjA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8HlJnOcDJLHx84rT9hiCLGseNV74KMG7xxhMGmPca7ahlLEabxjNdq96ZcvXjWG_UHOOx7f1a5U3YL5c2-wWB4q197rYNgkwww9v1ix3neOg5kOnXNGdDSyp7lWToXTR1TA5GYqKI_hcMgVu3gHNC6_kk4_nDB0CUGL6JspKj40tCeytlzqKpr8tWUVwU-10vo0FmWBJSbTrB69W_wj7vh51h6EZjwhGELqz1TpUpHGjKC90_ox7Z-pIclm74LVW_k5RHZ0C5z4VlvFYpBpOu7Hr_Mr5IkkKlPc5daeyC8npYqM3sGwHe69lZV-_KE6kxrYHgy46S1BsRtOqwINwuhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8HlJnOcDJLHx84rT9hiCLGseNV74KMG7xxhMGmPca7ahlLEabxjNdq96ZcvXjWG_UHOOx7f1a5U3YL5c2-wWB4q197rYNgkwww9v1ix3neOg5kOnXNGdDSyp7lWToXTR1TA5GYqKI_hcMgVu3gHNC6_kk4_nDB0CUGL6JspKj40tCeytlzqKpr8tWUVwU-10vo0FmWBJSbTrB69W_wj7vh51h6EZjwhGELqz1TpUpHGjKC90_ox7Z-pIclm74LVW_k5RHZ0C5z4VlvFYpBpOu7Hr_Mr5IkkKlPc5daeyC8npYqM3sGwHe69lZV-_KE6kxrYHgy46S1BsRtOqwINwuhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=ZJH-qKLb07buXCCb_JadBiNT-xLbJH2bbN7iT7wQS1wARQbs2sbbM1bqM0Le_fIXyEftaT5dCvFcigSH7LeCvfx5f8xxeusCeR2Jho7yuak3gmFGhN0I65LzfTxWqfpVzz6GfHLYHcJt4kjimAm84sDdRhtbt0SN8h7PxWNZS1890J_kb2iU3e_FGoouzF0CpPi0MrMfghgnC1fCACGQpK-56cYLAJ6wsa9CNSG3aFuGzPWX9VCeKLiB1QOOiirKx5oq2LnuQo7X8XkfKxaLf9LA2gYOgFkR_EbJx4UwNhr3ixHSVXJL_af87wI8nkLhAJyX-oyjiaA9RKZHC2HLQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=ZJH-qKLb07buXCCb_JadBiNT-xLbJH2bbN7iT7wQS1wARQbs2sbbM1bqM0Le_fIXyEftaT5dCvFcigSH7LeCvfx5f8xxeusCeR2Jho7yuak3gmFGhN0I65LzfTxWqfpVzz6GfHLYHcJt4kjimAm84sDdRhtbt0SN8h7PxWNZS1890J_kb2iU3e_FGoouzF0CpPi0MrMfghgnC1fCACGQpK-56cYLAJ6wsa9CNSG3aFuGzPWX9VCeKLiB1QOOiirKx5oq2LnuQo7X8XkfKxaLf9LA2gYOgFkR_EbJx4UwNhr3ixHSVXJL_af87wI8nkLhAJyX-oyjiaA9RKZHC2HLQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddWKQbmwAJwHipUmPxPr5hTJ6ky3Xbt1Z6jFcG0Y3mxACFmBKiwCxwqNEBJLSRDyf2vJg7hnXTcXsZjvlfEmWSvohjcF35my8Hxjv0eSxWy9BbN5oFeA_sIjs80jiGcFhnM3JibI-CbBh8d3n0Qyof1sAX7I11f8cPAwLQ84YvXEE4ArF4I5u2EALgNa-JvJC2H_meUnFHI0Jbi4lu52qHvhPgIRko-0uJ8004oHUGVVOfadk1w6MFACUwnmHu3abodv9Ma8fVWzlhPpMTjXh0F2LpMS92SsN0cbviJU_WgOKrfNqw-b4ltPJSQXnAmY5eFcdDlLGNIgcy8G-hSgZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=GnmRLKcoxqSmKKwIGTT7qfYX8Yia9dgdhXInejohGFkOGBlM2wisggzeLEQqd_s6He1f_X2OOAavg6wYX8fof2l936kMMCRm5jne9uUqvjqqiDyqS__AQun06CBw3l6xhrmVGLusG42e4Ka3eWJxMbR6KvcNLXvDYrdHFHYTnS7_FeU579rX2Bf-Vgz7T4l9vXBQmWjSiiyM-980TxE7z65xwCBWEIXcT0DPMepjs46slOUxtrFdbLzC9picbQ_jsTlmBWfebx-EVzWEPT1nLgHLUvHl7U9iQ0jKE-Nc3CQA1H9HdAYk3EJx8Qk0MKfZCder5x8c1oTxz2-TTlzJlzT_xtgqqmYMTYfIyQQU_H6yrN8jrVM-Lbf5am9z-LhK-GK0xeCmTZR8y3pLXMR9IgwoBBnbMMDIDff0KHII7RV7LzMZmgFNVjsXv5GQG0N4LdhMcSli3i-rM6uv54KJxUux3ASBK6PZbUDAUYXQecW-myAAJ2EuK-BoRnt8243wunQPqufsFKEPs3fVEeqppha16TpcNz2EEr680I_eYiL_9_556BvO1-DbxuJF9aeI84-U2qWcMP7G4NtI0cQb877a5vABWrXDuZ7Lp6ZRB3RI7f9WCX9URgv62eo3ba455z9IQtZu6cqhR93EkBFihLF4Na60_aizg6UScd4VuiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=GnmRLKcoxqSmKKwIGTT7qfYX8Yia9dgdhXInejohGFkOGBlM2wisggzeLEQqd_s6He1f_X2OOAavg6wYX8fof2l936kMMCRm5jne9uUqvjqqiDyqS__AQun06CBw3l6xhrmVGLusG42e4Ka3eWJxMbR6KvcNLXvDYrdHFHYTnS7_FeU579rX2Bf-Vgz7T4l9vXBQmWjSiiyM-980TxE7z65xwCBWEIXcT0DPMepjs46slOUxtrFdbLzC9picbQ_jsTlmBWfebx-EVzWEPT1nLgHLUvHl7U9iQ0jKE-Nc3CQA1H9HdAYk3EJx8Qk0MKfZCder5x8c1oTxz2-TTlzJlzT_xtgqqmYMTYfIyQQU_H6yrN8jrVM-Lbf5am9z-LhK-GK0xeCmTZR8y3pLXMR9IgwoBBnbMMDIDff0KHII7RV7LzMZmgFNVjsXv5GQG0N4LdhMcSli3i-rM6uv54KJxUux3ASBK6PZbUDAUYXQecW-myAAJ2EuK-BoRnt8243wunQPqufsFKEPs3fVEeqppha16TpcNz2EEr680I_eYiL_9_556BvO1-DbxuJF9aeI84-U2qWcMP7G4NtI0cQb877a5vABWrXDuZ7Lp6ZRB3RI7f9WCX9URgv62eo3ba455z9IQtZu6cqhR93EkBFihLF4Na60_aizg6UScd4VuiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsRC-26UWcIiBPj-9lQirhrwkFpMmUZflsCABlNT1LJcB89gWcrdJ5ZdCxADpkF88-5njXTS3Tt3mXr_vgDOmya0pLhTZ-_MCPkiS0cVDb_SkD5FYFA7JJf7mXRjR_2RXIV8V30_R_qbrfKdn5TRNA9gPxprEFvLDQ8DCiyY7E3rW1PCm8xAx62L6FbVCMQobvmKMKbtZ9EYiGSA9gVFfad00qpErheHbxxT3XdluAhgiilK98Eaumg-7RMeyDnzwxA5gHT5_vQeEkoge0UB2JT_MEgxjyyypH0320kpB9JpMA36jJAMjdOPGop8rcEZRVCZcCEZaBUZZ4E1xPoBug.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=ne9xExlhoA2qpLwzA591X36a8Q5hcvS5K69rK5Iobuq0HRP01VmDsCBqhNP5vfc5-7PQX05G6RxUtidT_DCHjPM1bBcUv4SnYTZzkn8RY-7xYDbxulYDu_lGtC6jEBA6bJqvJRVH58-CiLX9qsZMpFmyul41Ngu9RsYUL2u6QFTbvYxMnr-N_ixnXlYzWSOrkDI_5qGCBtxyGvy9-bt1oWTxhmVwAbNAcfLC-9d8umgmLQVMMGFIZ7pJTf1hZHNNwaC3KR6xpeaMowb0hlV3Sxgd7mGU6d1rI-OWAgTmnAAgKW4iQS70xPfn0338MK1OP7C--Nerac6JcRyTmM7R1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=ne9xExlhoA2qpLwzA591X36a8Q5hcvS5K69rK5Iobuq0HRP01VmDsCBqhNP5vfc5-7PQX05G6RxUtidT_DCHjPM1bBcUv4SnYTZzkn8RY-7xYDbxulYDu_lGtC6jEBA6bJqvJRVH58-CiLX9qsZMpFmyul41Ngu9RsYUL2u6QFTbvYxMnr-N_ixnXlYzWSOrkDI_5qGCBtxyGvy9-bt1oWTxhmVwAbNAcfLC-9d8umgmLQVMMGFIZ7pJTf1hZHNNwaC3KR6xpeaMowb0hlV3Sxgd7mGU6d1rI-OWAgTmnAAgKW4iQS70xPfn0338MK1OP7C--Nerac6JcRyTmM7R1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUyut6AhNca-o0dmqykLiTN-WWCt_VxOydbaya1FqyZ7f7Jf1wWePJFIFNs4lRotLkoVRyoniezrYeKbGe2cNniIPjt4eU5ojp14GHzHmRkRD5YtQyE9blmqnL8-DMWXix_GBWIVY9ojQc59YePi-lP-5Her3MqnBTWmTwzi3uHTXY0VC3m4RYYObzDvi_WmFMbIZhrxe_AHpfy5VH3gU_dX5hqefgjyYpwroT3AEcvDBT9kShvGb3Y7aUpvKOV3WRAaUwxPk4Eenr1u9jINyvilQb6CJhtFlNqKL1-mUZ5abEDzrN3LzbqOyTi2gA2duvWs8_vsbU3bFbQjaqscMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSIX3wd0DC3zF6CwMxtytSNeOZHbJrkwdalDb_JRj3M5DzriXnpgl_VGxDcIK0DNki69FvpUGyiFbAEUPGSoIjli0n0UHMhPSs8-fDd21WmMXmEwtEg2Y0OBf31tZtLv9xV6tsreyYbj-eiQcK-62BNJtbH5HxYMmI-kNnXj6-kYXWu_gg84tdp0bQqL1oLWRIJq95fNrzC1BO85ZCTKKVZh9VL4F7Vs7_tqn2xh1uCAa8hLwU67Wz7ftn_UTHJWcw_zXhSlfPT28xFrmEJBK3_0gUVECzNcEzPiKFiZk0K2GBKwanzb5dFMLs25kaq2S6uSYJ3Yi6v4ituG2CMqNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbXrxxZe4z1lGIrOwa67wHxhsaaJt-Mre6XLswCyAC4UnvvIIUq0Mbng_W5exi15LwhDx4I9eQbBDij-qNFRH_ljFIvOoF8P3RtTwtqLGOKLinW3Ddu_x5yxRr9Ok2V2nTcVmwCUWxgXlXjDpDWlgCAaeVp_v-x6ptHzrE9-wY_vraWluQ_qRrrw2ge5v3i-CxYKP4Py7QOqj8ueIQEnTXMBCi0GGWbE21TGcWyJItLLhBSpdVwx41UDQoz5IbEBQxIlBGkwfnl-08zpuEmxUUY302NigMtBhij7YWghOahMQ5sALaRDCpi9KapMO1FmM9xP5WtrRHYic66LzKTvhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=WqO7LYiSymWTXbTWqDlUH0KcpKVZ5_Yfa8nf_1r94EL4sxLVxWjU7Et5j0oNYETCzvbB99br5EUs3LYKMdhz7Sl1URYNeaKOjLu2nUxPWsG9E8VaB-x0D2LkoooMFHtQIrtOTiWAEj7Dl8p-q__tSZ6s2uA0lqqNMFnCYcshoG2NXheSPoIiCVbThkcFYPl547vmHI4BmvsgS7wPP0a-oou6lihXyjAFRv1NlULe5WoMvPh94EHSZvG9sUhD6PKWdYKW6vrWALSMOM_iQF8flceZMBwDtcov2gRW4lleLX3bvEpCUk_B2hAY5B9laZ4NNH7lzdlh1lsqVSclQvnt_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=WqO7LYiSymWTXbTWqDlUH0KcpKVZ5_Yfa8nf_1r94EL4sxLVxWjU7Et5j0oNYETCzvbB99br5EUs3LYKMdhz7Sl1URYNeaKOjLu2nUxPWsG9E8VaB-x0D2LkoooMFHtQIrtOTiWAEj7Dl8p-q__tSZ6s2uA0lqqNMFnCYcshoG2NXheSPoIiCVbThkcFYPl547vmHI4BmvsgS7wPP0a-oou6lihXyjAFRv1NlULe5WoMvPh94EHSZvG9sUhD6PKWdYKW6vrWALSMOM_iQF8flceZMBwDtcov2gRW4lleLX3bvEpCUk_B2hAY5B9laZ4NNH7lzdlh1lsqVSclQvnt_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oj1M27XvSZOmD2v2Wfn-pFoIgs8QyJ31K2QjGilmz0Juf0Jd7xZj2ckhUSgAFU8oubeeCS7Fh2YUFrErDQV4DFgLzKEAgN8yndJWGYPgE7YnsWq10mz5heGNSLsQZ5NiaXINLoWpmsmafBjp2kFd2kxLwSQ9CH4E1BuRgZk7P7_3Vq0yxbxbqj0Eh5LzclOImyehQhlD0ymRKxXRkMWzZ5vKOm9WI_tqxXIqKFQMXgq_i45kn7lABlYEiZ7i-jqku3CBK92D1otGOVKzDDjVl-KGlxX2krElNZS4L1kf916BPhEUQnAPipX2krSotnzSOWyutM1YgwWoQnV4t8e_CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu7ZWD2sT5bTPESyqrkesvsso23ePhpDeEbPcz5WPe12gHkDPvVMQAuOYGRkEC1vP_2jC6yjOBPwzKSfr5sHtBeGy_iYug2SpfP60wxRefiY_rXEIsk3XeBOdO5R8g0veBy8HmUb1wIjqOHlN_Gsshcn6JXGuQu1V_1vJdq3407u73ue3_CMUWNgYbO9tZRKTvaUI-Ry-5-VHt0rK7iRaI-S8Z7F6nwxmlp2_N_G48AK_IsD70jYUL_QYU-ktPBI-tFwP0PU_dLmhIWogRCJVsIoWAE-l7VGAw8r1toAoJW2j_KRo0Syc_n6WdvYAj018Q52IMAZe8BIlP5etXGoBYcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu7ZWD2sT5bTPESyqrkesvsso23ePhpDeEbPcz5WPe12gHkDPvVMQAuOYGRkEC1vP_2jC6yjOBPwzKSfr5sHtBeGy_iYug2SpfP60wxRefiY_rXEIsk3XeBOdO5R8g0veBy8HmUb1wIjqOHlN_Gsshcn6JXGuQu1V_1vJdq3407u73ue3_CMUWNgYbO9tZRKTvaUI-Ry-5-VHt0rK7iRaI-S8Z7F6nwxmlp2_N_G48AK_IsD70jYUL_QYU-ktPBI-tFwP0PU_dLmhIWogRCJVsIoWAE-l7VGAw8r1toAoJW2j_KRo0Syc_n6WdvYAj018Q52IMAZe8BIlP5etXGoBYcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=uSFPX11PPSApT-Vk8pi2tU3ZIUcOyJ0uMSp_q_BJazB_70UF7xoXiShSK7rrx0i5bbC4IpIjXDuYLSHgQ8gKXF4PXxbDeu7l69n2fdygHiZA95HltH71gHNZhmoP43y0RSmQVlnK8fwIFIpMC8xEAAsTix0LRtsqf1S_I_6EPm8HPp3HUlirsnyu4kT5WuUW6DTF9rL-DWoM32kU3JRI_5HafjJwNtbfH11-rEssWrecdlMO9K9gV1g0-t1IjlxZwKXEI0e6Mu3AR32ptdn0wD-CCQRzoqYat-1YF6_QTx9zAF8ZIPkXNRL-B43A8IA4HKjx4uzm_1iBXld4VWS0Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=uSFPX11PPSApT-Vk8pi2tU3ZIUcOyJ0uMSp_q_BJazB_70UF7xoXiShSK7rrx0i5bbC4IpIjXDuYLSHgQ8gKXF4PXxbDeu7l69n2fdygHiZA95HltH71gHNZhmoP43y0RSmQVlnK8fwIFIpMC8xEAAsTix0LRtsqf1S_I_6EPm8HPp3HUlirsnyu4kT5WuUW6DTF9rL-DWoM32kU3JRI_5HafjJwNtbfH11-rEssWrecdlMO9K9gV1g0-t1IjlxZwKXEI0e6Mu3AR32ptdn0wD-CCQRzoqYat-1YF6_QTx9zAF8ZIPkXNRL-B43A8IA4HKjx4uzm_1iBXld4VWS0Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=tllrPNZ851c36dQpBAGOIV0pLKFHHGLaB2ceIlrnXmpcMDE9iD9_QT3aAMGfjhPr-Al2iVR17j79n0iI8IlskPHfff_ZfB1ZbGSTq2MkWSjCYPnq8BKP34riDxUnqlwK96_xts9YxsmIMJxxa5_NA1LS7JiPUpoD7i5FR3eZGaZpeGvarOkYJ-LDENqOPvtsnwgiwa0E2vmjTi73w4Qxj9Kr35RXM37oHGy1AFHd84IKYkO8W5nGTbtmlpQCjsydN57TQwk-jIUueAkqxi6USCP-ys6ijkzpbt2skf67wqEttQWvRFyUXVg1nTpmeCB2Gq3YikoPBUBcL4Rlh7u3301fhQCvlhYusCU4FH2azyf4edvWyHzLBh1rv9F2ugQ6du9ZpngA4tuojt6o8tA916Zaxkc1SkRfY_klJszrm7_yp-FhXmU00Z_ITX1ej763m82gi_05BEijk3v704NSgp7RlGRF11WmfQqp1BLliOOPhtAyy6PLsrWEojhK9DgyBdi5wFlBnHcdbvkJFAD7TtcosCbdxJa_IiuQiSf9JDmaL-6reNT-5BGDmcowDwVzqH1h-WN9Wic60AmedQvmAxgBVJFnSXTkDoVVbfWepwheLCJdhNIidnjpbz65QRtjoyyiIVrFVqjhqPdnGU2u3U0du0KJFAwZK4ioEqJVbtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=tllrPNZ851c36dQpBAGOIV0pLKFHHGLaB2ceIlrnXmpcMDE9iD9_QT3aAMGfjhPr-Al2iVR17j79n0iI8IlskPHfff_ZfB1ZbGSTq2MkWSjCYPnq8BKP34riDxUnqlwK96_xts9YxsmIMJxxa5_NA1LS7JiPUpoD7i5FR3eZGaZpeGvarOkYJ-LDENqOPvtsnwgiwa0E2vmjTi73w4Qxj9Kr35RXM37oHGy1AFHd84IKYkO8W5nGTbtmlpQCjsydN57TQwk-jIUueAkqxi6USCP-ys6ijkzpbt2skf67wqEttQWvRFyUXVg1nTpmeCB2Gq3YikoPBUBcL4Rlh7u3301fhQCvlhYusCU4FH2azyf4edvWyHzLBh1rv9F2ugQ6du9ZpngA4tuojt6o8tA916Zaxkc1SkRfY_klJszrm7_yp-FhXmU00Z_ITX1ej763m82gi_05BEijk3v704NSgp7RlGRF11WmfQqp1BLliOOPhtAyy6PLsrWEojhK9DgyBdi5wFlBnHcdbvkJFAD7TtcosCbdxJa_IiuQiSf9JDmaL-6reNT-5BGDmcowDwVzqH1h-WN9Wic60AmedQvmAxgBVJFnSXTkDoVVbfWepwheLCJdhNIidnjpbz65QRtjoyyiIVrFVqjhqPdnGU2u3U0du0KJFAwZK4ioEqJVbtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=lMGdPRSB4Dq-Qmgx7fZ_feLY2LjWrzcXLJPe_UX5AmCOtgSCf-KTg5lp3m8JhWLLOxpPAD57kWKqbTR7j6c2oo80mxAm_jZ4F6F4Rdy8q4_MPidpTL-XqBmSajvlE0F-yVJgSptJ2jT7W0fmUUDhLs9BtJKr9ZeXnFq4mFJCfX_SmG8kkZSabhV6SFaHXmOIBIk0-0-cUWrmMTFoyUVjHFthwQgwGxrQqVNF2DqurRaS5DYLRxpC_qPJhD1XSmKVC3QDOhF8PnE639VIEBPvJ_rEEFoyPR99uAkUz2VyS83EDdSjJ1e7iwLRqZmYERJrcvVPjT2KIDyLjZ_SK8eMFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=lMGdPRSB4Dq-Qmgx7fZ_feLY2LjWrzcXLJPe_UX5AmCOtgSCf-KTg5lp3m8JhWLLOxpPAD57kWKqbTR7j6c2oo80mxAm_jZ4F6F4Rdy8q4_MPidpTL-XqBmSajvlE0F-yVJgSptJ2jT7W0fmUUDhLs9BtJKr9ZeXnFq4mFJCfX_SmG8kkZSabhV6SFaHXmOIBIk0-0-cUWrmMTFoyUVjHFthwQgwGxrQqVNF2DqurRaS5DYLRxpC_qPJhD1XSmKVC3QDOhF8PnE639VIEBPvJ_rEEFoyPR99uAkUz2VyS83EDdSjJ1e7iwLRqZmYERJrcvVPjT2KIDyLjZ_SK8eMFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7rndVfdfig5BXB-a8PK6C8dGt6kEeQPo65lwu20uTiZpf7U9-gHgJFC-pzh5DUUW7BboGukDafyOdq5946s-cR3Km3ffrrwusGqJtKN2JfWuBgAvnWUU_H6CxIcPxC4Qt6MFUOgEe9pwrzkFEMtL1BPqL-rkmm3XQSeUHg7DK3fuTcjSQVKs0hIggbgfm44YoHHvC0ooVhC8KzTSlOMy4N6vgd2EKzpYWl0k2Ga8W4GLdr_95J4k8q8Vtdwkn-HOD9g2ihI-Ktv5sCSrU5yrdJWYActceUTYAuQPFmiE7BxPbEhLH_u4KXaiU4yDtEtqOpayiLsYDGuWfSIDSFfLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=tqFqWs9ztcNkev8U-VfoCobdzy4V7d14tHLCtMBVViHd7Wr7chPAUfLK27ODZ3BcOiGZBRcagCRfyI9q9GXVoKJWSUbEtYgDT-AL60AfIwPzfn_u2k4TUws4sMp9U97cwTiT9Zs8g9CkeYEs9Pcw8I-WpRF8RTcvSBtPnnxyomI95CIAvYRDd7TwsqbCOryre_QBwjEoXgg9wzJI7m1MfNvfhMjJa6DiGXa4CTD-q07OeuTNKHx89zx9ZYUcnPanSCRhnzDexmMuhmV3Y9Qtb6BKFYJ9-sFeU7CKTaFfOQFtd7DIQlqiYdRAYeL2pSRDy_jTeoalXn0XHhLAzzO-ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=tqFqWs9ztcNkev8U-VfoCobdzy4V7d14tHLCtMBVViHd7Wr7chPAUfLK27ODZ3BcOiGZBRcagCRfyI9q9GXVoKJWSUbEtYgDT-AL60AfIwPzfn_u2k4TUws4sMp9U97cwTiT9Zs8g9CkeYEs9Pcw8I-WpRF8RTcvSBtPnnxyomI95CIAvYRDd7TwsqbCOryre_QBwjEoXgg9wzJI7m1MfNvfhMjJa6DiGXa4CTD-q07OeuTNKHx89zx9ZYUcnPanSCRhnzDexmMuhmV3Y9Qtb6BKFYJ9-sFeU7CKTaFfOQFtd7DIQlqiYdRAYeL2pSRDy_jTeoalXn0XHhLAzzO-ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=J_WLx8daMzknhc8gykgn9nsl_jlp0s4kjvDlvTtzOZJsBOO6hx36aoX7kDsEH0YkVAKTSjP-xvPtZl7i3I2C_XKH0EcUQH-hvtAs-2MlhgdRNPjCvQHlz2yl-EbqVToEtHVN-PvAi3-B1A1GfRmxg3AD3UqrXCpD53tFUcI_tyMRA7IVn73W4rrrl0trxan_DsJJdnGn2HBKhq2wz14XTMvwDOb7TNHOOrFt3xD4vep6MPf_gYwLPL12YArbTiW1MfyyZsT9dx_KaYUfLxr_fwugFTfKQGSkMObwjQ1_tPQ32MinxyfBzjAVEcXsXby3LIqrcW0l1OiX1IIcwieUmzVq47OOF_cRmuuq72qbZWLII1qzmoBWhAOseNNNk4_qrFnw5BgRYG8oMaZmA8jxOGH7-i8dkVWIwTUnWRhmt0K1e-NJaEjlOwp-BS37pVjVNOOqI3knA-6s4jiC9T9MocK3z8NkSWZrlYzG0x5Ce_Iy22LSsRtdPkd6mXT9zOsRi90lVNeOb7Ks04pDVW7SC7I5xMvg6TX_1OLrQJ0_9FbQBI3Qg3SD1bGcfIDlMGr_C299BlWNTnC8ApRFCilcnklsVvdlUs1cFNVQ8X6oeosjcHexAaUwh2natVagQ7LvO3ReLhobyIENuy3yDm6e7MJUr1jl8VdcSZdnklZLUs0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=J_WLx8daMzknhc8gykgn9nsl_jlp0s4kjvDlvTtzOZJsBOO6hx36aoX7kDsEH0YkVAKTSjP-xvPtZl7i3I2C_XKH0EcUQH-hvtAs-2MlhgdRNPjCvQHlz2yl-EbqVToEtHVN-PvAi3-B1A1GfRmxg3AD3UqrXCpD53tFUcI_tyMRA7IVn73W4rrrl0trxan_DsJJdnGn2HBKhq2wz14XTMvwDOb7TNHOOrFt3xD4vep6MPf_gYwLPL12YArbTiW1MfyyZsT9dx_KaYUfLxr_fwugFTfKQGSkMObwjQ1_tPQ32MinxyfBzjAVEcXsXby3LIqrcW0l1OiX1IIcwieUmzVq47OOF_cRmuuq72qbZWLII1qzmoBWhAOseNNNk4_qrFnw5BgRYG8oMaZmA8jxOGH7-i8dkVWIwTUnWRhmt0K1e-NJaEjlOwp-BS37pVjVNOOqI3knA-6s4jiC9T9MocK3z8NkSWZrlYzG0x5Ce_Iy22LSsRtdPkd6mXT9zOsRi90lVNeOb7Ks04pDVW7SC7I5xMvg6TX_1OLrQJ0_9FbQBI3Qg3SD1bGcfIDlMGr_C299BlWNTnC8ApRFCilcnklsVvdlUs1cFNVQ8X6oeosjcHexAaUwh2natVagQ7LvO3ReLhobyIENuy3yDm6e7MJUr1jl8VdcSZdnklZLUs0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcXXNG2JvvzfNAL5M100APNXdlOAXOFmBy8kfh2O-NFcAHgKPPWrtBR5H4KAa9OGEw0zC3HqjSdeCEg_dvQHk1pIHZELpV60Cy3GhfzlqjWnFTVT106AQxZ-6iVlET_spe7kUrg9imwtpg8hyhzidF2Oa9viq1OKTrbQkSZYNfxE3w8lQOVmBYGinR_axyiotwVRd9Cv8casOWp4RahcwdWpAbEJGR8RQKOwQnCjjT5WjEOOTgsRdWfmRG02qysDSS2V0JUW2FKobrdatlYc9RrvaJ8iI1VVVpyzmbmjHOH5hnaH2j4z3SxnmOQE13L-SPxQ-DbjHDeHr9VWHG9zWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=aDfvOPV1WT-eoZtUsx-VKf9RcuVBB5DLaK9At6HBSBA8JyPkbXdqLc13F5Y-op106iqzKHMC_B5mMZ5p4mLwDWH25Vut3xJDl0CGMsUALCaUQngU4XGybdtBhQ4iJTM4s3E2CaT-JFgFZCwJD1CY8PWDRDJu3U9jA3-WpJqoIcHnjlcYVaqjMZLx53ZtFXglyN_CgoZCSm5V7R5SSQ0KPd-iTxQLQM_FHlPFcaLHWJWHcRh8UDFziFsvJLugEteBlffmNiaF4YyUU-Mj1MowgUjUObfZGV_-4-v5NgSqoRXD-3ZgKf6ZSyeO9nRtVdjF42N94TZIjxQt_HBLefgrdVOw5A0F773S75S--KfB3M514S-xtHIyxl0DNYY2-dxMf4E1Q9MjEGYkEQ0URnGdgrYuXHQa-caD0gnfYMr7E4bfcawlcFUFv6KcbXVXEtXPHXCEL9bC4Dp-jA2DuDKVQeVigTUZ4A2h5NCK0YkTuoOSwc6L5uP2fM6ds5I54N081CQibPv5Dx73PkC7reUD1823qckh9mHLSM0_W8zsCxosIJGwW_q-BjnUoL0mn_5xlMt5ksEgyxHkeMvOXPh1NhV1cy_IBYEXHmTxwoQKRunF0MxqTZNgM9e8jIrM2K6UsVMBU9EECpnJ3T2WL22bPb_iToBoJHQHO5uP08THT4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=aDfvOPV1WT-eoZtUsx-VKf9RcuVBB5DLaK9At6HBSBA8JyPkbXdqLc13F5Y-op106iqzKHMC_B5mMZ5p4mLwDWH25Vut3xJDl0CGMsUALCaUQngU4XGybdtBhQ4iJTM4s3E2CaT-JFgFZCwJD1CY8PWDRDJu3U9jA3-WpJqoIcHnjlcYVaqjMZLx53ZtFXglyN_CgoZCSm5V7R5SSQ0KPd-iTxQLQM_FHlPFcaLHWJWHcRh8UDFziFsvJLugEteBlffmNiaF4YyUU-Mj1MowgUjUObfZGV_-4-v5NgSqoRXD-3ZgKf6ZSyeO9nRtVdjF42N94TZIjxQt_HBLefgrdVOw5A0F773S75S--KfB3M514S-xtHIyxl0DNYY2-dxMf4E1Q9MjEGYkEQ0URnGdgrYuXHQa-caD0gnfYMr7E4bfcawlcFUFv6KcbXVXEtXPHXCEL9bC4Dp-jA2DuDKVQeVigTUZ4A2h5NCK0YkTuoOSwc6L5uP2fM6ds5I54N081CQibPv5Dx73PkC7reUD1823qckh9mHLSM0_W8zsCxosIJGwW_q-BjnUoL0mn_5xlMt5ksEgyxHkeMvOXPh1NhV1cy_IBYEXHmTxwoQKRunF0MxqTZNgM9e8jIrM2K6UsVMBU9EECpnJ3T2WL22bPb_iToBoJHQHO5uP08THT4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=nZM36_iCNwzz6C5d8bdKjhXEN-KVyIFLeszQXIBKbmgmd3Ry8cPMWcg39dRRtk81DjylOiGhLuGPvQNdoRmN2MZtnFGM1VVfR5lBxqocY7d2IE2MVytdNgCVNYfB0PhgZ4Vxt3C34dspNv0Pb4ZfIEjMq5eTOSd8rvqHg48qe31s7xGcq2vJ-qr0qMKDdR7615GUvEPKQVFCzE0CpAT4vsppA0usnTRFAZxvHz2gUrtKgaQkoyD8CAHfQBoBUpQB6-iuk1_QlmIH9EqlfPlk89ci1ViFYSBIA3Tdt4QVsVYK4vaVioh_TqYYORy5wGGZy40rnJIRwDMJL_Xe2Yuse6nT3MtNtvC8jZpOVaRV1HKWZjfhkMKWi8tBkhvHzjGPhwd4YRTKihKm9bZq1BCvSmaJ9X8Mznh_G3ptP99cCVitzfK4PR5MXY5UdBKapBXHgkcer6LnRvaWQwGXaqXaG3ZZ_-sBJjZMaDCx9axYPEedbt5Be1g0Gdx4pEwHKx4VAHnPI1IduLuhJQMLZhGTmL3lAL9fAdE76R46xukj6nAJwipayaz8ZOMJrLJDWH8azuAJDufcSMRvQvFP29BmAGNJThz-MPhTqbxQ_sktz-VbgSrIHk33f9XPS-OIYjnNlcj_-i6qvUj18gNUDBjCNf8LtI2LguSNd_KaVhMIKQk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=nZM36_iCNwzz6C5d8bdKjhXEN-KVyIFLeszQXIBKbmgmd3Ry8cPMWcg39dRRtk81DjylOiGhLuGPvQNdoRmN2MZtnFGM1VVfR5lBxqocY7d2IE2MVytdNgCVNYfB0PhgZ4Vxt3C34dspNv0Pb4ZfIEjMq5eTOSd8rvqHg48qe31s7xGcq2vJ-qr0qMKDdR7615GUvEPKQVFCzE0CpAT4vsppA0usnTRFAZxvHz2gUrtKgaQkoyD8CAHfQBoBUpQB6-iuk1_QlmIH9EqlfPlk89ci1ViFYSBIA3Tdt4QVsVYK4vaVioh_TqYYORy5wGGZy40rnJIRwDMJL_Xe2Yuse6nT3MtNtvC8jZpOVaRV1HKWZjfhkMKWi8tBkhvHzjGPhwd4YRTKihKm9bZq1BCvSmaJ9X8Mznh_G3ptP99cCVitzfK4PR5MXY5UdBKapBXHgkcer6LnRvaWQwGXaqXaG3ZZ_-sBJjZMaDCx9axYPEedbt5Be1g0Gdx4pEwHKx4VAHnPI1IduLuhJQMLZhGTmL3lAL9fAdE76R46xukj6nAJwipayaz8ZOMJrLJDWH8azuAJDufcSMRvQvFP29BmAGNJThz-MPhTqbxQ_sktz-VbgSrIHk33f9XPS-OIYjnNlcj_-i6qvUj18gNUDBjCNf8LtI2LguSNd_KaVhMIKQk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=WOlgj9cGir93JIA4O5ONLYoU5Twbyb32NFXKCzUF7DRpuPIt8KlRCupwPBxLxVKQ2WOUlSw6bbbtz8gl-zn2uL71F2HlnRNMlOtGm6mwrX8kHnVlcK8q4gTITFastDSzYv5edlsn7HNLt-q2EUbjGlpLt8om1ZAXVHL-mH0Kzk39WQ3Pa8vd58XYZdiJi6EgsyMU18IdSyYLLtD7g7SN7ol-wao8Ezw93GCcA1cJIyzuW9cRc3AV6uvLbaRRZFMFO018gqtRbPZxsQc1M9jC7Oh031EspGU1Cevj8bHbMDOpfvpKFYoMi3SU725-Kt1kOD7xGAs8yfp0dpHQue8xCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=WOlgj9cGir93JIA4O5ONLYoU5Twbyb32NFXKCzUF7DRpuPIt8KlRCupwPBxLxVKQ2WOUlSw6bbbtz8gl-zn2uL71F2HlnRNMlOtGm6mwrX8kHnVlcK8q4gTITFastDSzYv5edlsn7HNLt-q2EUbjGlpLt8om1ZAXVHL-mH0Kzk39WQ3Pa8vd58XYZdiJi6EgsyMU18IdSyYLLtD7g7SN7ol-wao8Ezw93GCcA1cJIyzuW9cRc3AV6uvLbaRRZFMFO018gqtRbPZxsQc1M9jC7Oh031EspGU1Cevj8bHbMDOpfvpKFYoMi3SU725-Kt1kOD7xGAs8yfp0dpHQue8xCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=WKsz5QzkkyJ0E0nX8asknXrxirxScwk2vwFseyx5T1EfjJk5rNPyIWuZyrT4xFmuq_ruNbV_SP_CTDrRvSSyoIFmxl1MH4vv4JvK2SptmcTtoE-Fsvq3sWbf0Jpkssu1FvyzeUGFn_q27qhwaIJ1F2qHC40zEdRYPT-bMgSDlw0CbF0Ks0Qh-iu0JY9TAFH3q8O_Ay2XQGNUXwiJowpWB1qdMRwIbECUZhUhv22Z00Uelrv4CoPXbPt3qkRRcUMCF4uIIhDrAUWioQjknV802fs5Rsp70tnY0eXFrJBAOZiwb0MdszfnyGp9TU0UOUOFlfWwxhVa_inC_QmHd6PjwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=WKsz5QzkkyJ0E0nX8asknXrxirxScwk2vwFseyx5T1EfjJk5rNPyIWuZyrT4xFmuq_ruNbV_SP_CTDrRvSSyoIFmxl1MH4vv4JvK2SptmcTtoE-Fsvq3sWbf0Jpkssu1FvyzeUGFn_q27qhwaIJ1F2qHC40zEdRYPT-bMgSDlw0CbF0Ks0Qh-iu0JY9TAFH3q8O_Ay2XQGNUXwiJowpWB1qdMRwIbECUZhUhv22Z00Uelrv4CoPXbPt3qkRRcUMCF4uIIhDrAUWioQjknV802fs5Rsp70tnY0eXFrJBAOZiwb0MdszfnyGp9TU0UOUOFlfWwxhVa_inC_QmHd6PjwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=GYV4-T6jQyEuuleLMmqVD5ubiuq1vs_ErVLv6m4x8Q8tm5tYHWr-ze3-kELeNxUVTFgmN2zECUPIeQxaLDpgdqT6vNtdUU1IZEK69E8osy9aQ88hw-aq-lUB5vkAsUTS0y1Hq6Z_sZZOymcDXflN-HomqAGNUqApxgdUoYo04QbjGtlmDEFx0igevTHPR03kGUtEXF4AU35vDhDCPdejoIoaG9q0rF-zqZYB9jnj4rCYLa6kGBitoOO87oufbtdtOmOEXSmlzwDtEVgKtqwIfOtHzfCG0YgrPLVJZuukIsQH2V8xsVb5c_xGFt9yKUWsRAW8lVkx_H84PLgef7p6xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=GYV4-T6jQyEuuleLMmqVD5ubiuq1vs_ErVLv6m4x8Q8tm5tYHWr-ze3-kELeNxUVTFgmN2zECUPIeQxaLDpgdqT6vNtdUU1IZEK69E8osy9aQ88hw-aq-lUB5vkAsUTS0y1Hq6Z_sZZOymcDXflN-HomqAGNUqApxgdUoYo04QbjGtlmDEFx0igevTHPR03kGUtEXF4AU35vDhDCPdejoIoaG9q0rF-zqZYB9jnj4rCYLa6kGBitoOO87oufbtdtOmOEXSmlzwDtEVgKtqwIfOtHzfCG0YgrPLVJZuukIsQH2V8xsVb5c_xGFt9yKUWsRAW8lVkx_H84PLgef7p6xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=tDNF-iFmSVfPTHOHYKTnSf2Jhd2xCJHquu2n8baAyB_ypCKm6EI3r888VPdURGkRTGtSQU_E_WqxAOTkeuQzQlk3dJavI_wnOaUb92Vc051g8FEZWr87cr2e1xxFyOyDZAYJGDgLirzl7vP4OwC5DZmQoAUNcK3klO4Bgu6X9XqNh9-EGNCatn9_Po4VCvHxQcHPNhHdzjZ1g7lzN6uvA-YJfldRZ69xkczDnkAj5jmsRM03PG47LbLfwxK1_1npDDr3xVv6neIbwfIYPtjE2m4uGu1f7e8zuUV4Q6ue7s4DwVH-MJml9o2xmZfPR9uLx22FNRymSs8ppP7Mqt2Gsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=tDNF-iFmSVfPTHOHYKTnSf2Jhd2xCJHquu2n8baAyB_ypCKm6EI3r888VPdURGkRTGtSQU_E_WqxAOTkeuQzQlk3dJavI_wnOaUb92Vc051g8FEZWr87cr2e1xxFyOyDZAYJGDgLirzl7vP4OwC5DZmQoAUNcK3klO4Bgu6X9XqNh9-EGNCatn9_Po4VCvHxQcHPNhHdzjZ1g7lzN6uvA-YJfldRZ69xkczDnkAj5jmsRM03PG47LbLfwxK1_1npDDr3xVv6neIbwfIYPtjE2m4uGu1f7e8zuUV4Q6ue7s4DwVH-MJml9o2xmZfPR9uLx22FNRymSs8ppP7Mqt2Gsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=rGYpmSWsNq2ksFw-cH09Oqt3BfW9hQmAz_f1ubH_MBHb2Rn6Me15_TMF3hNtEpDYk6hmg01I47PGnY_Ewz6KWj-eZQb1hXDvzL0XfYXt5naRV1xc0bRi-l7qUVD2KDewYQyyYR8GagH4RXX4RLxlNufXEaXLKgYPB3EVRz7zxpgnigNrDKPJcYJG_GCvL-Iwd3AlKRcNuPfYCF6RoQWvZRPhb6YNHzwOkZfw4URxiZEd-U2y9PFbHFIK60un3gXlfPDMkt-hbE38haalvEoyzL2QqyItVvNurEfMsWpeICx6pTMhQsnPNHD2RcG27S1XVSUY95i3OLU6ITDvvBoTsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=rGYpmSWsNq2ksFw-cH09Oqt3BfW9hQmAz_f1ubH_MBHb2Rn6Me15_TMF3hNtEpDYk6hmg01I47PGnY_Ewz6KWj-eZQb1hXDvzL0XfYXt5naRV1xc0bRi-l7qUVD2KDewYQyyYR8GagH4RXX4RLxlNufXEaXLKgYPB3EVRz7zxpgnigNrDKPJcYJG_GCvL-Iwd3AlKRcNuPfYCF6RoQWvZRPhb6YNHzwOkZfw4URxiZEd-U2y9PFbHFIK60un3gXlfPDMkt-hbE38haalvEoyzL2QqyItVvNurEfMsWpeICx6pTMhQsnPNHD2RcG27S1XVSUY95i3OLU6ITDvvBoTsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=NK5A3izzSH7SknUiLY9jnnUeqwnPXP-BPWOIinLDlAqezAYMroJTC8myl2kcrU2hgApiUyDf71BhM0MxhSeiJQKIW1ja99MOXWobbZ-dQGL9qxt0GCYZGY44xOIqdl_mr8cbu4_Bek0BOMK31BAJwjcIj-itZob3ewrH9-6MN5Xz46MjAUMEcsAWa4Jz7ObPtpzIufKvuTLgvx7EaQ-2JAka2DB2OXHTPW7dekyWgVwwvu_IP2E9qOoEFqg4jYvWO5w9jK9umSkKxgl4BpC2TDfraW9FBsdVWMgXflCIX0S0rWL9Glqr7AtZGCGICMum9YZD0-t8cIK-QMiZiXIwSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=NK5A3izzSH7SknUiLY9jnnUeqwnPXP-BPWOIinLDlAqezAYMroJTC8myl2kcrU2hgApiUyDf71BhM0MxhSeiJQKIW1ja99MOXWobbZ-dQGL9qxt0GCYZGY44xOIqdl_mr8cbu4_Bek0BOMK31BAJwjcIj-itZob3ewrH9-6MN5Xz46MjAUMEcsAWa4Jz7ObPtpzIufKvuTLgvx7EaQ-2JAka2DB2OXHTPW7dekyWgVwwvu_IP2E9qOoEFqg4jYvWO5w9jK9umSkKxgl4BpC2TDfraW9FBsdVWMgXflCIX0S0rWL9Glqr7AtZGCGICMum9YZD0-t8cIK-QMiZiXIwSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=ZtWYzJnmiIhy2Nd8QDnq3QEHPDhfo1AgUanTv7M9C7kU-zVqOJUOqQQgyYS6FdF3I6HCnDmQ_0CHjc4JaF_WSbjrzcTO8HsE9UzuJxrF6tgDukindgyWpE0BZfyow9PlINLTbw-gTp2LmZYA-gPVGO551mV2uLsxWnAuuVkjKsQPplGYfibB-KXELDeagDPncPNFdwpMxM6T-59oO4RUSak2clg01DoKYNJ3tj0-SxK2GMQtALlCM800tfNenbZGORFjFsFs674z_8lcGZY04wbgt_A9fTYoLYEo5jlyu_WXl-o1VpG1mimv6zsdSAyX0L8nFIOgz79QdWRNuSGurA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=ZtWYzJnmiIhy2Nd8QDnq3QEHPDhfo1AgUanTv7M9C7kU-zVqOJUOqQQgyYS6FdF3I6HCnDmQ_0CHjc4JaF_WSbjrzcTO8HsE9UzuJxrF6tgDukindgyWpE0BZfyow9PlINLTbw-gTp2LmZYA-gPVGO551mV2uLsxWnAuuVkjKsQPplGYfibB-KXELDeagDPncPNFdwpMxM6T-59oO4RUSak2clg01DoKYNJ3tj0-SxK2GMQtALlCM800tfNenbZGORFjFsFs674z_8lcGZY04wbgt_A9fTYoLYEo5jlyu_WXl-o1VpG1mimv6zsdSAyX0L8nFIOgz79QdWRNuSGurA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enr0ibYS8lZ8ElbfGbt6jA165R0V-mWB167w7i7oKOfsJ5UqyFPrPvxGVGfBTVdHN-_OE4HiONuyHCTFBjfdZoysmNgB6sp71ilyPQYkTYnJPQExtkcK8ggC51HM3HCN1Bpqs6nSGBw5iajYtojshjeddorwIaDhFDCBNGW1sT85IDBbIkb4RkV6PUqCXNVU8iko4K7Qtxeb9Z1qdJSIHK4EAFEQs78IXgeyqwKcH5r8s8EaEV47Jr7dyKJWWBlPgXQlJbfFwQ4avNbODd88TGFanwQsEndHRD1G-3X0hLdnpSNWFv1qGV-f-BEdhDj4VzJDk37TbKj-TNnVPZ7CEw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=nrlQp7XFDUmBLKFqtlfvhevXz0P3vOcOz53UVTFh05PqunFXQ3XOrIW144w0P2umKW_WIKCHoUY2k6br7yExfLxh_uoMl1Xz0hihZdkXEzqMCgVPyTbiiqlKSsKIlj3qnIclJTPzFsR15NeOlCQnfTKYTIhGwR9tMO7UUomHNwo9idZ4wWVkkaw21K76gJ_HetRee0hu7Oudczf7sDSP_jDPXhej5T_-0JXXH8a4bA_R7GuYzKC5FoKKF5A7pKc7KjD8WGsCkm52Lfwp0HiX06oeIvHn_1jEO_ENMDvW2OqDh8D0CjxgAGgJFUalee6Sbf00m00CGIfWKc1Ohq5K-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=nrlQp7XFDUmBLKFqtlfvhevXz0P3vOcOz53UVTFh05PqunFXQ3XOrIW144w0P2umKW_WIKCHoUY2k6br7yExfLxh_uoMl1Xz0hihZdkXEzqMCgVPyTbiiqlKSsKIlj3qnIclJTPzFsR15NeOlCQnfTKYTIhGwR9tMO7UUomHNwo9idZ4wWVkkaw21K76gJ_HetRee0hu7Oudczf7sDSP_jDPXhej5T_-0JXXH8a4bA_R7GuYzKC5FoKKF5A7pKc7KjD8WGsCkm52Lfwp0HiX06oeIvHn_1jEO_ENMDvW2OqDh8D0CjxgAGgJFUalee6Sbf00m00CGIfWKc1Ohq5K-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=XLzUE6-jDCjT4ltbgeb7ltYML562ar1oW6ChYygEJYnyvgGS7HEIAArPyzsNloqTjQUtfe0379R1f2M8JFe_2zI2gGpl3j7or2GwGjb61_a7WnHzGDeLl4lcAyjR0tkw6SlY8zcLT827gi0t3uNj-UHf-t5pv9-OAGVU4iMYELWrJ2vsA08dvzR4XAZLuzmNnDwWV9ctwb7LXWBcxhBI6FDj7K4Y8UcA5GwO14g75nF2lkOrCzudf51LfkexKq6P-_OOv185hrLdHDnCGcrmZwHEyTh-9fc9VOv5X1HloRzc_sYk85D-aoOoaAyr7lOVoOqh7-oaffmVMtnlpBUv_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=XLzUE6-jDCjT4ltbgeb7ltYML562ar1oW6ChYygEJYnyvgGS7HEIAArPyzsNloqTjQUtfe0379R1f2M8JFe_2zI2gGpl3j7or2GwGjb61_a7WnHzGDeLl4lcAyjR0tkw6SlY8zcLT827gi0t3uNj-UHf-t5pv9-OAGVU4iMYELWrJ2vsA08dvzR4XAZLuzmNnDwWV9ctwb7LXWBcxhBI6FDj7K4Y8UcA5GwO14g75nF2lkOrCzudf51LfkexKq6P-_OOv185hrLdHDnCGcrmZwHEyTh-9fc9VOv5X1HloRzc_sYk85D-aoOoaAyr7lOVoOqh7-oaffmVMtnlpBUv_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=epf0kJzNyXOS2bmM6UKGPFOY8Bzl-aHJ8iAjDr2xz8yNMWbabGcisPG-TCCOa-uAn5VirJCsKbP_ltrPHs51RBaob0wAf5Pv9n1WksTgqFmzdurFBSN7C09sFXGWGfDgSq3fJDRLRxEBjEGNt3Ge-zIu2d8lAXnGqCabWgp207vmo-lM_6xPqA0B-7hyzCPLwJXf7qZzIjHO7IDiFKebOSJ-8ab-tAJGXrRp7huRnuA2uJUsgiIiwCZrRL_Ij4c51_9kUpKNu5g1kGLLCnQEdZG0wmCWIaBPFHCAVtwB6D4XY0-INnJUsvZC1gfsXU3akUOi0rJ_akxXTMGEsJUgWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=epf0kJzNyXOS2bmM6UKGPFOY8Bzl-aHJ8iAjDr2xz8yNMWbabGcisPG-TCCOa-uAn5VirJCsKbP_ltrPHs51RBaob0wAf5Pv9n1WksTgqFmzdurFBSN7C09sFXGWGfDgSq3fJDRLRxEBjEGNt3Ge-zIu2d8lAXnGqCabWgp207vmo-lM_6xPqA0B-7hyzCPLwJXf7qZzIjHO7IDiFKebOSJ-8ab-tAJGXrRp7huRnuA2uJUsgiIiwCZrRL_Ij4c51_9kUpKNu5g1kGLLCnQEdZG0wmCWIaBPFHCAVtwB6D4XY0-INnJUsvZC1gfsXU3akUOi0rJ_akxXTMGEsJUgWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=vZHsm2VZKBHGwWSSCA-iLPSnpVr3-b-Ppm4GoqIaPcYMKExHvlln10OSkmMsgdrkW-jFgKa2aajOvP79Enx5273-loNvh2hXpdzWjUofkqY6Osdp4PvA9fg02ZaWhcL5qg9HYg0DIcYJKNFJVjxFzIvSdF4zicFrAH1gnGSOXYql5il8fV2OUYvhn2O52p--usZTs1o6pZZeyJZPyhGfNR5VevBRaze3SM91p4JAYlgyDKjDE9g6dUR3J1MXvjrxemXG5vBT_m36oeGtzkW83vK2nl2e9R8ca6xrgixKpmTEc2k8E5pw0dPgBODN1Kh1CByaPgX7eF5ahiIZrNCLxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=vZHsm2VZKBHGwWSSCA-iLPSnpVr3-b-Ppm4GoqIaPcYMKExHvlln10OSkmMsgdrkW-jFgKa2aajOvP79Enx5273-loNvh2hXpdzWjUofkqY6Osdp4PvA9fg02ZaWhcL5qg9HYg0DIcYJKNFJVjxFzIvSdF4zicFrAH1gnGSOXYql5il8fV2OUYvhn2O52p--usZTs1o6pZZeyJZPyhGfNR5VevBRaze3SM91p4JAYlgyDKjDE9g6dUR3J1MXvjrxemXG5vBT_m36oeGtzkW83vK2nl2e9R8ca6xrgixKpmTEc2k8E5pw0dPgBODN1Kh1CByaPgX7eF5ahiIZrNCLxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHaxK7pIWBrRJ5M6xv2yJG0z8r466wRHPB7Fvv9xNnIQiIf8dCe-zhiuYs9INsqgy3vKQui4Z5w9qXFw1-yBGrbQ9n-feT1FOOiRgSgF665v4-rfVhuY7QUE2cXiPW_SceHaEceZG2KaXGWOJFhplL1zDduK-UV9YS02q2Ddvhh8ivkeB-0-QlDGXsfeLP4HLUcoFu_PO8lADMlM8x7JapZ2gflt1yVW10q_MV6iMLVkMe7Z2GfiFBWDyq3usUQMaesbMP9KMlipJdQjijKkC1Pjg58f_bxjsvKSaW2XAQq6iRbZVyYUSklsoMWxCOzhf5NzQuiFKmUjmSEfDuvQTg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=FNgWmgspevoSwmqOG_7TYKjeveYsVUymC9cs04DFV8i3nkeRdvVbl-54387guMS0pWRAqX6Q6-7i8amApi_KFrBkUYTLIq7ZHle8EQNBbHrBgsBnYEpBedjy_e489R3LpGggTfDDeZB9OThzFYpNQHBOMQIkpmAKBnmVjihk6kRTs5I99j-H_3THn13DCbW6ZXYnzYjLdHw5m3aXpzRNKZ12aIpo9wrUsErugNmmDazMAwzy3gHPv7kMyEEdYaJIRHXr-Z5t1ND58r6th13vv16SQ6f5DcxIHj8IN9v9hAjuE10E5yQoUj7EW6MgKJWnmuRVUlIloGuZunQSpAQnjjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=FNgWmgspevoSwmqOG_7TYKjeveYsVUymC9cs04DFV8i3nkeRdvVbl-54387guMS0pWRAqX6Q6-7i8amApi_KFrBkUYTLIq7ZHle8EQNBbHrBgsBnYEpBedjy_e489R3LpGggTfDDeZB9OThzFYpNQHBOMQIkpmAKBnmVjihk6kRTs5I99j-H_3THn13DCbW6ZXYnzYjLdHw5m3aXpzRNKZ12aIpo9wrUsErugNmmDazMAwzy3gHPv7kMyEEdYaJIRHXr-Z5t1ND58r6th13vv16SQ6f5DcxIHj8IN9v9hAjuE10E5yQoUj7EW6MgKJWnmuRVUlIloGuZunQSpAQnjjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=N6A2no_1cgJWq9598BrVhHJ3GA3NABTGHxLaDmS85m-4auc6CboMpyZqWQhUWTIc_v33f6NdpTnoSZB7Gz9AnL6ZkBUgp6oqai0qN31NP1IIa_8I2cb543tJnU-yG3pbPsT_dXYkvihjf6qfpKWCPln2YedHAz7EzsboHk_VftVKw0RY2_pOwUw_2snFDgEQup9hLPKBCtLX0Y0_sfi0ASq-ivXr9O3-_b7g41n113EbbreiR6ARBryGO1qAA1oFDbW8EGa7mP7hUhanOugTfMo0G0mrG6vIMyZwsGQWU3zuJJtvnC-PDqnjbSqoU2rG_jx7oArDe4ygAlXZ14Uxww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=N6A2no_1cgJWq9598BrVhHJ3GA3NABTGHxLaDmS85m-4auc6CboMpyZqWQhUWTIc_v33f6NdpTnoSZB7Gz9AnL6ZkBUgp6oqai0qN31NP1IIa_8I2cb543tJnU-yG3pbPsT_dXYkvihjf6qfpKWCPln2YedHAz7EzsboHk_VftVKw0RY2_pOwUw_2snFDgEQup9hLPKBCtLX0Y0_sfi0ASq-ivXr9O3-_b7g41n113EbbreiR6ARBryGO1qAA1oFDbW8EGa7mP7hUhanOugTfMo0G0mrG6vIMyZwsGQWU3zuJJtvnC-PDqnjbSqoU2rG_jx7oArDe4ygAlXZ14Uxww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3ToqLjI9bAZtLy08h0lEMkNQQz-UNvyJ07ehUAUWwQgupeWYcjHJMbVFjWgC0RKL2CQR5vDsNqObQjoft94nt6CJBoxEDKWWogSBpdnkSTXYh_7xMZw1RGlb75hqICXsy_6NHdB65ShrT8ZQga51TLDT67aNyca7bYGH1hewsi1ey1jzJeZnO9PZfKMdXd9FoNGUdlo8jZQMpHYojOOv308gzAhM7Bv1n8-8WFVhDZx83iJiLBz43iEKHQOy54c-InqnzDIbXu6O_2WbazBAl5lxppulrbmucZnmCpjuCjKSQzXsHgq8BSxQJU4XwJ_b4iaLpN17eDFlvVKCxlVhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TcVZOFREBCsaVj_UYJNAu9fUDpqQr0T0rIMNMI_XWZ5bDJiunovHMkwrMnCDEYu-HdzC6jy637_b3FUFzl8WbHJ1mox-yJRuknyTGURov0DDsPMbAksLVXSUAo1YHsOHupThnMOVUQAzLk-i3HF0PXZsTb67BmFdFRklSiW1n5gu7OCGpIJnYDAipJTQ2j0gCi2m-ulHJGwy_Ph9uq6MWfKO1ncAtho6JTJs8zFpWcOUyb0ackQe6x2fXoCjDmYdfI0_ZWjHJO1FBXtlcXem5BCOpeJe5NzLxqRsFhboPOTxhrxM3zPTw75jgcx_cxRsTZM3B_BOfFGJXbvzfV0Uog.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=hLJcSwBU6kjjZgHXJQKR6AJoyHzcdj68oMukj9ohC9dOAf5BHMpBFO2NWVq6BnLHp6TmwiT8JQM6-f4zMWIz7Rns1l99sOegvvbvPSYNBlnvw1NIF2TQLxOl-DjQx_yDulxj8H-FEg4ZsxghapKcfSsMIE1tsMFp6lHfUa62x0mzLxOiE-uNsV5fqLwwK7tJv4GRFItYJ13Khwa7sNmkDf9LT5qtlU2td2cN2AQZbZnNle-m6L_7ZEFtdbx3mxTyYah5WxPjyv2ONWdlmtxOeHAlyfQMvHvNCBLezgbeVlAz9_egmkuwK0IN67cCBoKfcyOeDcYoTDgwTFkxwNnkMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=hLJcSwBU6kjjZgHXJQKR6AJoyHzcdj68oMukj9ohC9dOAf5BHMpBFO2NWVq6BnLHp6TmwiT8JQM6-f4zMWIz7Rns1l99sOegvvbvPSYNBlnvw1NIF2TQLxOl-DjQx_yDulxj8H-FEg4ZsxghapKcfSsMIE1tsMFp6lHfUa62x0mzLxOiE-uNsV5fqLwwK7tJv4GRFItYJ13Khwa7sNmkDf9LT5qtlU2td2cN2AQZbZnNle-m6L_7ZEFtdbx3mxTyYah5WxPjyv2ONWdlmtxOeHAlyfQMvHvNCBLezgbeVlAz9_egmkuwK0IN67cCBoKfcyOeDcYoTDgwTFkxwNnkMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qagt5lHPgvAdgi66GiLuISjehtPtdNw2hH3q_nTuAYIUkpSl9w8Qj4DYEsBiUKeN9ZUtb5gEnGCCBdCTZ1p0Cpj424Wlad1XwtYFQe2USiJgtiLNYDoOSB5TeUcb_5OV1eHe5GMdBZ_te3HJV0Z_rjznV1tE923YaQBdXV978IdgoFgR4-l3O4MFy5-JsTNNolEoWjHo1jotLCyDMfu9ciZHLOaF-5alSERmFvTBhN4CocyMNPfm0PQRak-hS-2ilCy1mSehpaKL1KCElT8F9zHxYzU68f9Ah6VtPf6X6UKUJuXv6aHjtNPhihhnPjA5YmjbBMVFMGLcacu9BtN76w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvqQN74ed27X_ZtW-nHPFHbOyenpfotwpXqbYUZhdH2NP0FEXBPLX4S-ps0JqMUo9-aA_sFP-xbl9_y8GyCeKxlpYf_ZpWjy7kp3MGTfTBduwq9Nxz0bYstQv85EIpbV-U0zojYn5BMFyCtg3KoKCDA0SWX1jyEd1BuP6mTCGCfSxFDVSCnH2QuFOuEXycOta3W8LMErqQo1U8QqqznCMFIC_ZDgvHV2xpyJTgdKI2RoaHvLzBgmX6533xX8xSwEw6FmQ30PpSbwHQlKe9rqW3pZ1M-3FOq5vsjvPafg_VjRC7EuITe3ueCQfZbOOkMp9ehIRfceo7IA9jl31spPkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPYxY8fKIuG9po39lshdqvbJWRTIG8U_RkXkRIMns7x-add9eId6q_lCbpzzD217pTDZ7HVZ_9bMbS3ojhHM8lcBFuNKlTEUdl_n3JcFNAzy0ng6IKFD5kRCcW6m5cxUYvKWEw2Q7G9CTgJQdIIXGio8FEI7NX2h69CbxxF5kneByVGLoYCSELC29eok4Lp6Hjes7ixcCIiNEf3jO6eUomLARdlSeCJJVtAFmyVqhM2RgOoXD_xHRyd3ga21IkBeZAvsia1IwkUZKorZjXC-VyNCzuNyDYZPlJZEzvuH7rcP4d7pXrvQXxQM84aMZexbBdXEpz64MacQRtPu5Nf0bw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=HvYaDwit1tbTdf0_MKkBFWUOBbuThVzdADvjRqZnu6UA1PZ-yv5S9QbY_WJYIG7rBS7FE_SRG6uSVZ8I71ajZys1LP3SOakpvqYpWl4cUoDP2xkpHCQWJfQSJuD8zHv-K4sAq5W_z1ISaD-Fg6HJGMe3kMm1OHVJLrsBcLFTH-2Z_I0AsE6QRGF-5dFWf4JQrIeAdDDTk8bhMI3p6isiR5iWcBTchpghFSmbgdC7eQXM3TL71UwuBXMC9agPK7am1vDPMXQZqweuXJn67CWTEpyLOgCQ7TJKZhbVjWDKc-DJt4x9ih0Emj5-eOF67gwV2Xju2rYfLNWJci_1bd4E2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=HvYaDwit1tbTdf0_MKkBFWUOBbuThVzdADvjRqZnu6UA1PZ-yv5S9QbY_WJYIG7rBS7FE_SRG6uSVZ8I71ajZys1LP3SOakpvqYpWl4cUoDP2xkpHCQWJfQSJuD8zHv-K4sAq5W_z1ISaD-Fg6HJGMe3kMm1OHVJLrsBcLFTH-2Z_I0AsE6QRGF-5dFWf4JQrIeAdDDTk8bhMI3p6isiR5iWcBTchpghFSmbgdC7eQXM3TL71UwuBXMC9agPK7am1vDPMXQZqweuXJn67CWTEpyLOgCQ7TJKZhbVjWDKc-DJt4x9ih0Emj5-eOF67gwV2Xju2rYfLNWJci_1bd4E2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=VT7eYfh9BoJqaRMjKRNLVQMobx2sVubsZqP9YP2jgScF0iLYhEyFEyfA1KRQ4TC2nU8ZCkRYyOXgjJhTYBpMMIkTnbXmZWXerk3nJAxuEkBN4sYjHgilop5J7EIWq8R0lA7vDSeNt_-XfkcBN5pqiz8my08YOgKGfJRYbtP6q71NTsCrlTUivV39bh4Xu41Nk5jL11Oaq8Vem0RBxXOvRVofUtVePjGi85rclJsgZlTJLeHYJHf8VQKngT1j_cSyBCm-Nz7p39lc_QFvd0atz9lbvHkGqPVAMqQ4IeZKN2HaA5wq6xi2i_lWwL4hshv0ntw4PWRpE6YDBNDyvqhDtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=VT7eYfh9BoJqaRMjKRNLVQMobx2sVubsZqP9YP2jgScF0iLYhEyFEyfA1KRQ4TC2nU8ZCkRYyOXgjJhTYBpMMIkTnbXmZWXerk3nJAxuEkBN4sYjHgilop5J7EIWq8R0lA7vDSeNt_-XfkcBN5pqiz8my08YOgKGfJRYbtP6q71NTsCrlTUivV39bh4Xu41Nk5jL11Oaq8Vem0RBxXOvRVofUtVePjGi85rclJsgZlTJLeHYJHf8VQKngT1j_cSyBCm-Nz7p39lc_QFvd0atz9lbvHkGqPVAMqQ4IeZKN2HaA5wq6xi2i_lWwL4hshv0ntw4PWRpE6YDBNDyvqhDtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=XW3l5qyMuAjwq75iwa90PMwYDYMpdONku3ShwRoFfIo_SUGs2zIRfYnrfl-SnSz6oxo9TU6PGLE3-IAslEEssVO6Xbeb56yN-jan8g0DVYjUr33YOONlZ91CN9iCvLEaUwDfdr_XoyN0P53HolUobYMR4MSzC9OZeha9iizIEvpJZUH915ssfcMPzMT-k0jTqtoNWYJB7YC_B1tAVFnhPlb_Q8CTLTJ8SmtzGa4F4y3jL9WhrgwOSuMjXoTjkYgg-TEpwbIiNBqI3BRJPS8zb0IOz4ODEpV1Wxj3BIHVuy8ciHR7Ye45htzx4003FE7lv7KoxlpgnichCyBpaIlY7AIV-IH0vkDHpuNA_CYZXYTQLUxivVs0ck87IDR1sxBLotBnieiwhRACfqR9zagQGgeWXv_zLhL41hUXu7ACF9z7DxXXqbW_7AI62ZnZVco5FzYx7cPDhO8nTOEiMGpTetyk726KtBJF3RfG6zc8eCZCLWd23KgZAsasHSBv8e7dTD2qtP4ZlpPa1MotxJ1xZlMTG1Y6wNYfMadbvIOD86EAPK1fAUXmLqsHxtH0QXdjL3v496QeuQ97P2XvPxz9XljFqNzTKiildSm0NvF9F6eNfhhtY445sHZt0oOZNgZStHh4tFvpMif7AYOjebWe88-xzKbWr07BS9Ellz2YW10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=XW3l5qyMuAjwq75iwa90PMwYDYMpdONku3ShwRoFfIo_SUGs2zIRfYnrfl-SnSz6oxo9TU6PGLE3-IAslEEssVO6Xbeb56yN-jan8g0DVYjUr33YOONlZ91CN9iCvLEaUwDfdr_XoyN0P53HolUobYMR4MSzC9OZeha9iizIEvpJZUH915ssfcMPzMT-k0jTqtoNWYJB7YC_B1tAVFnhPlb_Q8CTLTJ8SmtzGa4F4y3jL9WhrgwOSuMjXoTjkYgg-TEpwbIiNBqI3BRJPS8zb0IOz4ODEpV1Wxj3BIHVuy8ciHR7Ye45htzx4003FE7lv7KoxlpgnichCyBpaIlY7AIV-IH0vkDHpuNA_CYZXYTQLUxivVs0ck87IDR1sxBLotBnieiwhRACfqR9zagQGgeWXv_zLhL41hUXu7ACF9z7DxXXqbW_7AI62ZnZVco5FzYx7cPDhO8nTOEiMGpTetyk726KtBJF3RfG6zc8eCZCLWd23KgZAsasHSBv8e7dTD2qtP4ZlpPa1MotxJ1xZlMTG1Y6wNYfMadbvIOD86EAPK1fAUXmLqsHxtH0QXdjL3v496QeuQ97P2XvPxz9XljFqNzTKiildSm0NvF9F6eNfhhtY445sHZt0oOZNgZStHh4tFvpMif7AYOjebWe88-xzKbWr07BS9Ellz2YW10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=NtblCBjdzBAPAHOZ8dCl0pgnxcsIDlOMgDVhgNomIKciw55sQaWhBblbzdYZF9wt3hSmdUQZpP7N5-kNPgtwaScZZZ9m684Okmou6LnhYb0yJpec_QJ0-QD1eiEAkBrviTxls3fhPGxWStX4EFdBKnjN9g5I0rH9uoX8JJxMJKTS9D87Y0T8exU4beFEMBESA5qHSWeCEr0eMrPA7dXahKM62vUgIC3c7C0acc94lb_FaL0SvCI_SA-KKvA7tG9r7pst1gKXPZ5OiH5vsjqMHdHP7--YEcYe49to0IeHoKSheLCcUhJIATSxtSx7gwgTho7ORgBN2CDZwPXPcTnx1nGUoaY4omwNgHlxi4g5zgZvGU_XJRjjXrWrAVK5_x7QE6ngY3wLjMFFTdpGJUACAFj6YCBHdKRBoHuVA3VZ8Om2xiWZubzHA9hrz44E5CXGlBgSgxmvdvFreuq7u2BAPnDxd6xWFHgRrJfQlE5JQDCVvoOmXYcQ4l14Mc7L-MEvFHP-4sb2z286St-MHe6w0AhdCSxgwumOXjGqoyhQvLz45mqh1i88OGPSRCTg0tl87GiwAsvX-QuBmTvP8WeZMG4m_sg0fKnUS4n0q46WYRZ5_P615MhR8hRCEGX1dBImev7BAHh1wm1sopyZDYr1i45ggKjJ9a-Nr_HHztsQ5Ys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=NtblCBjdzBAPAHOZ8dCl0pgnxcsIDlOMgDVhgNomIKciw55sQaWhBblbzdYZF9wt3hSmdUQZpP7N5-kNPgtwaScZZZ9m684Okmou6LnhYb0yJpec_QJ0-QD1eiEAkBrviTxls3fhPGxWStX4EFdBKnjN9g5I0rH9uoX8JJxMJKTS9D87Y0T8exU4beFEMBESA5qHSWeCEr0eMrPA7dXahKM62vUgIC3c7C0acc94lb_FaL0SvCI_SA-KKvA7tG9r7pst1gKXPZ5OiH5vsjqMHdHP7--YEcYe49to0IeHoKSheLCcUhJIATSxtSx7gwgTho7ORgBN2CDZwPXPcTnx1nGUoaY4omwNgHlxi4g5zgZvGU_XJRjjXrWrAVK5_x7QE6ngY3wLjMFFTdpGJUACAFj6YCBHdKRBoHuVA3VZ8Om2xiWZubzHA9hrz44E5CXGlBgSgxmvdvFreuq7u2BAPnDxd6xWFHgRrJfQlE5JQDCVvoOmXYcQ4l14Mc7L-MEvFHP-4sb2z286St-MHe6w0AhdCSxgwumOXjGqoyhQvLz45mqh1i88OGPSRCTg0tl87GiwAsvX-QuBmTvP8WeZMG4m_sg0fKnUS4n0q46WYRZ5_P615MhR8hRCEGX1dBImev7BAHh1wm1sopyZDYr1i45ggKjJ9a-Nr_HHztsQ5Ys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=VzsF9-8zcw1y0ITrgKS_xinI78pkcGcLa60AAvdMMEFZJ2lS8K9DD7NotGnO68EAkcVorauu4VOQ8N97H6wMhVPWIdN76B7NjhemEfzbEKSNLtCcHDkeePvsSWwr7PUe5gM9GEbw3YM3FDLqHFYYXcWWwT2iMPpAhBq5SJcrL55NsXDCX6AIdqJ9Jp4AtsPqV3fa-OS1yr3mx05EUq0LCC7kotvz-V860US-XQSdQnX2zGwdOG69Hsa50g8wb3e0HVSzh2cEl99tR2UoAb8_Pj1AY3UGr4sa-tvDiJlFmPvXIkSqwq0HDJCR_a0mVPXRRsNHVxVqvZBdat1aydVtkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=VzsF9-8zcw1y0ITrgKS_xinI78pkcGcLa60AAvdMMEFZJ2lS8K9DD7NotGnO68EAkcVorauu4VOQ8N97H6wMhVPWIdN76B7NjhemEfzbEKSNLtCcHDkeePvsSWwr7PUe5gM9GEbw3YM3FDLqHFYYXcWWwT2iMPpAhBq5SJcrL55NsXDCX6AIdqJ9Jp4AtsPqV3fa-OS1yr3mx05EUq0LCC7kotvz-V860US-XQSdQnX2zGwdOG69Hsa50g8wb3e0HVSzh2cEl99tR2UoAb8_Pj1AY3UGr4sa-tvDiJlFmPvXIkSqwq0HDJCR_a0mVPXRRsNHVxVqvZBdat1aydVtkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuL729csr4YwVe4Q0g9mD6dwsBd77ItfCLhcAbhAm00GlDs2d0eKgwPvrD4GH19hB1MP2xe6e11nZ00c5Z1YNz0kCZw6gTJS8yIrYw7I0VLZ8I1emUp0NoX7o6U1E_-bLxt1YafnSVICuaFPIWWV3C80pEGX3IAxCoW5DtCwl_Q0Onlt0GIsMFgEWN5b4EdmYdI8dLKZZ0FK6J1Waan23bxvI2cUI1APZCy4KgEmZ6As3d5KBgNepY-RH4XNFNvT3oyEInBZBBazlj4lhGJYhdkuMM8qr-NR0IPLGZDWxpm6hkUWB_l0O2v6SstsVkQ0wwf-Z9QhQ8_LPTpB2HLtpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=bQo_tjGZgWU8y7GRO75ivLokHQgRsld6jDaUAiajcr-oV3WDZqbRdxNUl58wQqsSJ7AYOWaR1dM3TBFphe1V-s3UwlUi47A-v_KkOtJ3ywh04w-X4TEKTHg-QkQ7Sh1kFc22UhDFWAu-HORbakUeM-Rn86S8hHHAInfb1sqQAvN0nhcldV0mKIV6hQyNfmzSRbElffFoEOXP5PWdhoBY-S4bB6Ehl0nEw-1TyQoa3i6wUWtUOPh7677ihD4r7I-dRT5MjSPwnDxbKtAvZgOhx-Pthh0PWNIu8xQi4ot2Lzp4q_To7i5GFO1QWF8_XWQ5igcR3-Ry6Rse_WfpFwf_eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=bQo_tjGZgWU8y7GRO75ivLokHQgRsld6jDaUAiajcr-oV3WDZqbRdxNUl58wQqsSJ7AYOWaR1dM3TBFphe1V-s3UwlUi47A-v_KkOtJ3ywh04w-X4TEKTHg-QkQ7Sh1kFc22UhDFWAu-HORbakUeM-Rn86S8hHHAInfb1sqQAvN0nhcldV0mKIV6hQyNfmzSRbElffFoEOXP5PWdhoBY-S4bB6Ehl0nEw-1TyQoa3i6wUWtUOPh7677ihD4r7I-dRT5MjSPwnDxbKtAvZgOhx-Pthh0PWNIu8xQi4ot2Lzp4q_To7i5GFO1QWF8_XWQ5igcR3-Ry6Rse_WfpFwf_eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=sf4c8oVtdJ6fg-F6ug8O2iBT3LX3riT2FqPS_t5cyDtlFi_ld2I479VrVScKsikYa3gPbDqzmsbzT6KvGxi88Jqxr4qy_XH3l0kZAQDj7M6bDVhLs06V7ikoTWDypvARoQfHlcV8aD1VJbw1pWD0XUBolqEqEIZUHlUDfUCgcCBFjrPlxv1yO5uklw9JLz2ZFF3nFts-cafMhxWSFtqtFKAHk5JmghVwEvId_Jj9KrxkYtI6_QxWDTZUcdixOx6ChLKigHXtKWP1SYGPXJzaJxro_rKrVJDxmNKJwyacu4YmafhNLCtKXwictvN4rOxHF3HaKhhysZTOe_Ve4BIo4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=sf4c8oVtdJ6fg-F6ug8O2iBT3LX3riT2FqPS_t5cyDtlFi_ld2I479VrVScKsikYa3gPbDqzmsbzT6KvGxi88Jqxr4qy_XH3l0kZAQDj7M6bDVhLs06V7ikoTWDypvARoQfHlcV8aD1VJbw1pWD0XUBolqEqEIZUHlUDfUCgcCBFjrPlxv1yO5uklw9JLz2ZFF3nFts-cafMhxWSFtqtFKAHk5JmghVwEvId_Jj9KrxkYtI6_QxWDTZUcdixOx6ChLKigHXtKWP1SYGPXJzaJxro_rKrVJDxmNKJwyacu4YmafhNLCtKXwictvN4rOxHF3HaKhhysZTOe_Ve4BIo4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYc1KqI337phDUqdMV5Z67e8QPHtWoSDxhd22w2rDvvpry7DQOT98wRqwJX9fYQ_9F84KJ_07dP5zYscwFhrcqhyqytXu5s6-vplTcMAhHw9kkXfw-YDNRXJbrgV8zZ1OCEy98Was1sIGlzi0HhTTwGFKK4S23Giax99SvRI-2E2r0zamcxq306uNYFZiMQ4C-Wn_T-STc6Uym4U9tivZW-iO8tseoX_Jvdi3n9jsu73jzzIO-G-EGb_PbWnlwMWxxNllFKuDbkhrZ9Qz4tmHeCi97_rohdrcs55qutoxN3ELAyqBAJ3H-7Z2GAXDL2G-sVKBKNxTAJZWZKauYrLoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QS7T9k3f4EHd58IkW1t5F_8dd75O20xXlcylyyzFCjtgQATSiKCxjo0B0ao7tLtH3NRPjvNIX2LMYiz3XB96EtQGG81md4FhWHY6sLFh5iOhMg2Stwd0kzIuv2XN1QSi5yUgv_99uOMwoW2OPQVAIjbPO7xM5Bl3qmnzisRqnIen1G0Gi4_Gs1NiOulwrfIXZL64eOcyEUrar-PBvwo3NpW6LUOE7pNuBlUwaZ-02tsXQWuF-T1Vhu1yMNtBXUUgpF335WfXcFiZm88utJ4TvTqG2rVPHvP9qkpk5CJkDhAgXJyjrQdv4bFeSR_WoD1CitiqyASn8iAbkDftap2vBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcC6g1eJeWDauVTEHoFZQUY5YYUKNYrr4lhnq_jNfgVCPOm-VUsWgjO8dmHZsSYB-I9GH7nGx9A6Mxg1CoywvXccc0bKVxC1b4IKDP1-qVm6IFkIB88jZkuKtY7FKnL_6oPwYmHbyWZU0Rq0Fu-3tgVbH78hyjC6Obyt0V9z5D0gyFgPFM0iHJ6HeqQMyPfqIUnT7D0X2CCK0dexv-qxaqYECmn5kKFk4IRkBzg907C1BbG1weejyt9lHOfKeZL9JaBOEilyrjHwisi2ELIrajiOEVXwELXk0npDmtTa96ZRLCk6PgT1Jsz5IxKKb4n7KHdwvwGPh8tXa3bDNNItKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRv0JSm47QhMq_sQz6oQxSbgLPGOrnymxo4TRrlASppmIxDVL65UTIcpdg470DfctKlfZgjo5l_egswST6rOjRLK9NmH1wWvKu7d3P6heZxbLTUglhYBzLHAGNbiDaYzbcT-MACXeLUq7n9LMpzT5CRC_S-zyzGrrQtoEB75dNvCWPFqKGfB5T8y1uBTsDqJcjz8SzR670zr14cTbCdD8A0Xpb6qAIf4Xl6ICmDsVaw8IspNbpDRHgVUkVWnwxYVjB5rAh9yjZHsXinao11lboJvlAt6apcIbypyNlc35tsUSlrKo_jUMuS1ZAT9KH61vV5WNIhJppHDmJmjBsTv3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FN7ePDrG4Ctr8U1siPW2W6g4cowEnTjdDpaPrdgb0gmgkdkAXB2ZyZDig17RtnR-hB7WcUwMRlF_NreKhGxlQn4QAZSW1rtQEnhw2sJTAfJVidyx9Abw3-b5v07zq62VHw1M7tAfwpS4FmImIKHe9dpE7PWyfTqxunujTk4bx3NmrLBNYD-TZptGJaBQST6M2MQjvDmY75SK-_bVPFnGaZACQi0SnRDY828wUy4KPgjdETQZoADZsKdZtPDFys686VRYZq4Qyj3XOc4Rv6aWwwbx8Pz0PKI0DJzxgrhhtB17mQ8px1AJ2Xc1Qzap9MhIrMpUOuQCjTf5qJ_n6gXG2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gqv8poiqa_HlVawFJQDd30Q_LooLuKlSaHK_TJYUgNXjsQJrLqBSzXig03sA5NV7AsRQ7X7K1lvezLUH8qg2Z4qi1tlQi9nn-9gNbYK1zBppBXX1dUix5qsS1cF7D19VOX-YUjHolywPBINQJ8vA7tQ_PLU7R2B4JJam3IFkDjRqoG1jJZNQVV-81Ix1kUkjbGFRlBlQ5tOOckt42r7Zu7f98ZwdCZjwkWUEOzezhO-tEy8qsLOPlagw8ILGaRG6P0N9-O3U9DzizWRQJeE0yq6zZqMZ5BpHLW1bYpVwHyDUz5f7-oiWdwdJBqa4tzweP7Rxt87ocABl3BUl9Z1w5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
