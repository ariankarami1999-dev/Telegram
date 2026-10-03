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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 17:51:23</div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ag1IpHgUQbCuvlKDh3wit_xSm5kxt-_bt41xzna8DfsLYs2iKX79o3dGsiSYBX2eXU5x8MzGHjImdtnsSIez-_fwTNwkKKtCXT8b5PAmdob-MriBoNikrysTQ0P0FpQgNehhKzP8v6IM7g30nPWXfIH-3kJm7xpn5v2pBBRg5meeIOBQ36_unB4VLXVh6Kri-MCTW9-eFi8Biq1MYH1j1r9Iv4ZFsubaiZzYC0rY3t5JYJ4FSbBbtMmSbUx3ZzI2D6_ywcJw5rZjQ6LB5edGBwjpFXGRdiYy2KFogcivwkF0JrC6g_72r9dOxeVv45k437HPrOTkVUVzlNmDJEruEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWKJTP9efvsBF5z-9E7QRAbgzpRP8Gs1g_eSDtZdKGisQVEpVSrfijDykQdA5qCxPEeybDKVeQHGv-PyOzSFdScN7BmOYMQAF9OuwzfpJtIKy2COJiwTTMxEvD-w5d3PvgetG8bH0BImUP-A_QXt3su_wQzWgsyI-CkyZPNAHFbdNVi9vN2JXHMqIA-xlQSbUE_A5CdzNZDX5-6fj5xE6GjsU3tc-VZ-WyBZCKdNfzxUq_b9tuJoRc26ci9sUsE0b8G-ml5-XwflotC00xVKgsr3y58DklywAR4A2nc8QSxhXjy42ha9cj1JKaPLSKbw6PObg39FgV7BPzM0A6h4WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoQTpAGTsk1aVZdKV134P4FrAT2JK-xdGol5qGhIfZunmQohz66Cdm1eTB39BzQkL4EOWnj7IoxpT96g2NUUxCt0VvyURAUX8GnbIrB004art3rI-ZMELq-WdsTdVzaLtTIphwtZcLlAkbbrisvcalD3kWZi5Dk7qAxBP1Mo3W-ZKkIiJsCzQlLCA29r7_yeoIFnzweqtjqbN4UHahD9EJUNyk8ePFTNRtp9B--o0jGyJ9KivK6KEjaVpeC_Cj2ZXFuJg7YHYjqGiBNItPHwFg3lBA9mYqZB4uaKi8phkPO1kwiVPZAOBphm7H6sz4AEQJcMzrmIRPHKqefZjalI4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fy9uMj2LptI-cZkeANaY92HWtH6v4b4STvdcNFB39VjJTbRMqN09k1ZaruWXnsqtOrb8aCKF2mnxEeVNBSE8-NyvOnzht8KxI3zePbT7Z0ah6vM_pzP3RsPomfWRKVoMeLYH3k8-e8EhHUHMpbJuvHBJ_RcgQEmd8KcYfjcjO71bWchvqI9jF4sGVV5f1VoVxycIKm4gmBN602z_2ididcIQZ_HTdivyjCT-4wA6ezJV9BwJs8XM8rqLM_il_jC3cztYTgGkqZvo0LysOLlqmHfiLegChYGFHXv62h1RJWKUMWM_HaZiKqFK353G8ccUtOEbbQ6Lfjcj-FoLnafGMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=LDj32tL3h8aKvVRrrTZs9uLiMbI2AH7p65exSJZiu-h77jKXHtxx5NoEwSuSDoTuK481SfhR-3HrkPnrCy7oXniOburPWh6tYUqRzjbqZuRHnlg_XzTlO3U97XjPYzJNX_mgznLnR2UuDYZzw6cWtrTjRDRNvRA5DnkorUUfKEUA1id0miAZLLLIdoElSUMAIjMii9QSo5ZcQOs70tCXK5stEBuG7TPbgMzqEpmSqiBTiCEvo5vUNVRm6CsCQYbSkGMZRFuVeOJSRk-0gQ4NOHdOSCkWzdxZK6zpWkCo2-AO0uP2YLdEScm0SuW3A1Dntr7FcpRHikEQOxh5ALQARQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=LDj32tL3h8aKvVRrrTZs9uLiMbI2AH7p65exSJZiu-h77jKXHtxx5NoEwSuSDoTuK481SfhR-3HrkPnrCy7oXniOburPWh6tYUqRzjbqZuRHnlg_XzTlO3U97XjPYzJNX_mgznLnR2UuDYZzw6cWtrTjRDRNvRA5DnkorUUfKEUA1id0miAZLLLIdoElSUMAIjMii9QSo5ZcQOs70tCXK5stEBuG7TPbgMzqEpmSqiBTiCEvo5vUNVRm6CsCQYbSkGMZRFuVeOJSRk-0gQ4NOHdOSCkWzdxZK6zpWkCo2-AO0uP2YLdEScm0SuW3A1Dntr7FcpRHikEQOxh5ALQARQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=ZwKwMR1P7FrLGU5ubnE-oUeugCn0GFWlhAvNlS2tXo0vA8A8CX4UAUPbn5JTMJJJ2U7fXRLmTc5dofTOH5wqsRMpuXTZkEqRzbTHUTgbk8gIX1WNkaLX8WnLI_qu3E0ANWhykqK534k8fvh68f0D1DzqzHG4DIvxlfFVjTO3Jj0yzONtJfUMY4PF7yGUpB2yiwmbxJ8vNjQL1tWRXvF6bs-O-NXSOMfoP-IF-khsOZwQW7hV3sb7m6d4-8MfI1cnftfmrQn2tln1Ll_bKRCcn-4fTmWop4dz57RrTb1YfEguA335pG2TDlMvPuAYbclJp6N5gGcvhzlPlEi4W99WPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=ZwKwMR1P7FrLGU5ubnE-oUeugCn0GFWlhAvNlS2tXo0vA8A8CX4UAUPbn5JTMJJJ2U7fXRLmTc5dofTOH5wqsRMpuXTZkEqRzbTHUTgbk8gIX1WNkaLX8WnLI_qu3E0ANWhykqK534k8fvh68f0D1DzqzHG4DIvxlfFVjTO3Jj0yzONtJfUMY4PF7yGUpB2yiwmbxJ8vNjQL1tWRXvF6bs-O-NXSOMfoP-IF-khsOZwQW7hV3sb7m6d4-8MfI1cnftfmrQn2tln1Ll_bKRCcn-4fTmWop4dz57RrTb1YfEguA335pG2TDlMvPuAYbclJp6N5gGcvhzlPlEi4W99WPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=ocar4dlEND8Z9WLDe_pWT5lWOjbr_QYWm2pne8Ey13fUVEo9oaNcjIltrq7V3QTbKpfhCfahvgzLLgpJsBcpSWQPCaVBH7WwPc1cVCm0FvGSrisi--goIcLeUtlpCKqYJpoSF2kdqPDKaYU4kRzyWmben-fPqMTUKioiOD8o8eE7vGSZHMzQlaVqyXsPMqiexCLAVVD8qaLH5VqApjXZiax4TyjoLoscpBL_1nY5jRqra-t4AV2tsXf6f698ixqC00B7RN_v0mrfy7yA0BIed2I5CJ-fIOMQ3JlaSDi7IFNlKBqdWfsg0eu63NUAvperWuOI00C3jkrMr3_yYcy7jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=ocar4dlEND8Z9WLDe_pWT5lWOjbr_QYWm2pne8Ey13fUVEo9oaNcjIltrq7V3QTbKpfhCfahvgzLLgpJsBcpSWQPCaVBH7WwPc1cVCm0FvGSrisi--goIcLeUtlpCKqYJpoSF2kdqPDKaYU4kRzyWmben-fPqMTUKioiOD8o8eE7vGSZHMzQlaVqyXsPMqiexCLAVVD8qaLH5VqApjXZiax4TyjoLoscpBL_1nY5jRqra-t4AV2tsXf6f698ixqC00B7RN_v0mrfy7yA0BIed2I5CJ-fIOMQ3JlaSDi7IFNlKBqdWfsg0eu63NUAvperWuOI00C3jkrMr3_yYcy7jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crViwX4I72V2N94lah6ay9FdDJifixR7K9PFRJyFeUA6ntX5Z5T0hX1mV3_9bMBcANTeZoej9BN_s2JEKe4GAv-pG-4Y_eqxqRV8Cp9KWG3Yp62SH5qr5o7QPgBwp4OmVAxHjPRNZlemCwkCaav5DbPXdmSitoD-wClbo8z13eCCh5K1OybiLQJ_maiINJBJuuMVsWd0Be33Ac-PIxbJkpwoZY0PC6zDHtspilMieQ19XKH5VVoAhxNYaeWUahhwtg68zprShuBBfWn12rUFSRvHK6uWMH_gZpFmXBaNhuXSFDuaYHYagHQaWkv5fW1mNj9oyOcikTf_1sZGbey2pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8IxS5crnfUBqoZEXEI7SXHpEbmaeEQ1vQbceJP3W1iMv4Jodcdzrkd5PEx2Mm4NaFuT-sOnASM_Kdtr3iIofEc8CkjDhDB77Q1M6lHr9Ys_0oGo6jwHyVh7haPeYINofmpPnDX8Aq8EQj_MJ0BwmOYsQe3N7g_8_ABOGom6XujN2lUDwgtEuj0DoSDoo90qwDzBChCD7iXq1-3ALy68ZLgedSMSsNVV4JLd5DPKI9riy3E08wVXH7T3A2KwzWJUjEtegFR8Rdqi3q1zqyppWwBpSNPn_P-GA9TKCBfka20jzoH-fzKoxaDIvhbsYeUYNfdNS_H-VTgm3w69RXmTVNH4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8IxS5crnfUBqoZEXEI7SXHpEbmaeEQ1vQbceJP3W1iMv4Jodcdzrkd5PEx2Mm4NaFuT-sOnASM_Kdtr3iIofEc8CkjDhDB77Q1M6lHr9Ys_0oGo6jwHyVh7haPeYINofmpPnDX8Aq8EQj_MJ0BwmOYsQe3N7g_8_ABOGom6XujN2lUDwgtEuj0DoSDoo90qwDzBChCD7iXq1-3ALy68ZLgedSMSsNVV4JLd5DPKI9riy3E08wVXH7T3A2KwzWJUjEtegFR8Rdqi3q1zqyppWwBpSNPn_P-GA9TKCBfka20jzoH-fzKoxaDIvhbsYeUYNfdNS_H-VTgm3w69RXmTVNH4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=qHyL9XxqnfqwSeMHktYOxkxlIUIHgOCz9KFp9pKV5rpNMAYvtLXA-suQxh9i-DZkGo63bbEigv1KnnZ-Nv37Hzuz8apYWd2Huqba-5ZAuKfQOusgOkAjIwj0yPQgd5FZNUU1r_ydnvbeRMSTIv83QJNF-E-C2TozQqq6xMrni46KSsg4n4G_RtjhFM35yjwlox_RwfAsR43APL4RntRMBqdxm3kHdiIefQ6Qn-XXMDynK1TjBPSevznWcvFiqu6vIVqyKz22IdTNOzDVcPW-JXch-7BAFMZ25C14ZBpbhJnACoR5-04wnCt-X9kVW0w1_RRx_WEjcyaTN9UEumoMYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=qHyL9XxqnfqwSeMHktYOxkxlIUIHgOCz9KFp9pKV5rpNMAYvtLXA-suQxh9i-DZkGo63bbEigv1KnnZ-Nv37Hzuz8apYWd2Huqba-5ZAuKfQOusgOkAjIwj0yPQgd5FZNUU1r_ydnvbeRMSTIv83QJNF-E-C2TozQqq6xMrni46KSsg4n4G_RtjhFM35yjwlox_RwfAsR43APL4RntRMBqdxm3kHdiIefQ6Qn-XXMDynK1TjBPSevznWcvFiqu6vIVqyKz22IdTNOzDVcPW-JXch-7BAFMZ25C14ZBpbhJnACoR5-04wnCt-X9kVW0w1_RRx_WEjcyaTN9UEumoMYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ek9mgCqhGs4dumAKv1cBzVCi6SQrxX-KaNNJCs59zWhnABSjIg6rluJcaBWy85FY4x87-9Kctp-9wSPJyvvEuSRqckTcjdvwEpuwmbMVci64hrcRfvn2neBxOrxTcOiru5tYum9mCnpbBypVrFArWXoxC6I5ypTpnQjxzv1-zY3__b6dh7_INOBA9xOw05sWj9o1z_UUwaeFhrj2Q-WfCivWVzX7wFX9QyISBb-5IC_uV5IlP9HeoJr1HVw6Q1vbpApuQY8Hy1PduGTYni6biUjtmC8rSG2ABX8QTn1VEoGOtpGbFjxBjYE5BsarJFuYoRUZJEi2BmI2ngKxbIImtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=CrmVdwjwN4m-z7obun-x1CyAj3NoHKMSp11aXYsjLIWz5zqG9fVpCWlPXY6Rql5K6c70olgMpUBHg6g1ivJguPflQpD_PayOtU3vMEhI_L21i7prcBW6QaAqJpYse0mmBcNzfZbavM6o1FE3nlFPcSaNU3XQ-dBURiFCPcZP-sekAR3uZCjHd76uBqPgOf6MkyAkFMFC2WaDlOjRgNkqu3X4xGD3c6XvjHziov4SpH6kxfQUNriNh6349O-AfqUVn5uj4cGV2uXjEjWjcBe1F6qJKUg6chqYQ7ewveD31bE0loA-EHlLxYWkxz10Zhl69eXHvBzkhge4U5xDGwVtwx1fuXQKC-cDpFvDzO9eKExqOndeCNr_pnhYciPyj_ZIad02U2xdCWbJwbgoBIyQeVZxcCa1zoPLHL4T9RBE_g8N-_OMdh9z0RXuXj4irIAU8GJvGOP-emv9kLEBF8PVIpVYscvOjrb8OFAvCal1c2vT9Z7564R3EksudhJuOe_pZRCbvDfK2yeYk78hJ0xFGwaSl37TTLr2NMoO8t21ZYLenX-oBVXUpdLwm1rzlW-xAdF4syPV-mU7EwoljZ1Lhbtn9mkbpshECdrOQK52cyKIyzfp3OUAsnmr3xrMUNdAQo7rysAkyafnUEqKHv7jK_8kzFQf9BhQ5HVSzOyQTqM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=CrmVdwjwN4m-z7obun-x1CyAj3NoHKMSp11aXYsjLIWz5zqG9fVpCWlPXY6Rql5K6c70olgMpUBHg6g1ivJguPflQpD_PayOtU3vMEhI_L21i7prcBW6QaAqJpYse0mmBcNzfZbavM6o1FE3nlFPcSaNU3XQ-dBURiFCPcZP-sekAR3uZCjHd76uBqPgOf6MkyAkFMFC2WaDlOjRgNkqu3X4xGD3c6XvjHziov4SpH6kxfQUNriNh6349O-AfqUVn5uj4cGV2uXjEjWjcBe1F6qJKUg6chqYQ7ewveD31bE0loA-EHlLxYWkxz10Zhl69eXHvBzkhge4U5xDGwVtwx1fuXQKC-cDpFvDzO9eKExqOndeCNr_pnhYciPyj_ZIad02U2xdCWbJwbgoBIyQeVZxcCa1zoPLHL4T9RBE_g8N-_OMdh9z0RXuXj4irIAU8GJvGOP-emv9kLEBF8PVIpVYscvOjrb8OFAvCal1c2vT9Z7564R3EksudhJuOe_pZRCbvDfK2yeYk78hJ0xFGwaSl37TTLr2NMoO8t21ZYLenX-oBVXUpdLwm1rzlW-xAdF4syPV-mU7EwoljZ1Lhbtn9mkbpshECdrOQK52cyKIyzfp3OUAsnmr3xrMUNdAQo7rysAkyafnUEqKHv7jK_8kzFQf9BhQ5HVSzOyQTqM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmmLIZJaFqFtqANpqU0cpWV6tUe8uHfToAn9pQkZ8cJUOXldwoC_9UEexbaKtEJ8oSf74GM-sS1VOSBOu_rvgOjfCArUNjnjBehShPMFKYMPy15t4azqDMkRaiEB6tbGN6bqZUy93TbbpMP5x7WsXUH_s2Qmcf-df7enPpFGClKYiNQmxcaltehBHyaX4gc_YGSCPTZOC_9TS8debYJSQjIRxlfl9ZaNUvKi_skDYvnHasTJ_r1zJmzJ3YZ46iBabIHFoC6FmlceYMVb3_3NJ8DbEDwQGrv88-J3xZFskRfyifie3AeLSzSpc5J7-UT00PVl8vnZA7F3bKajMhQO-Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=JITQVUYcmTcR4Xl8CpISdmx9W3PBsdi5o4dvCbS8oPYs4Gpgqnr62wmZRpUh7nTiAhneaOM0gERumebXjos1cckjr0162ymc-dd_D93usPQnrt2aWYRurLcvRHVDc6y8Os67qcVo6sroNUxaxieXV5Nad1zLzQDL6PnBuyQzUzgTrA7RahcNGN5CzDNHcGq2dhJEvS6Rnls_MxGlF7hVBmRiQAxhYq8TfEOurBSrb7_THIJTg8aj4og1gTILtSaaF9k-1Lu5WrJRdZY1iwhtKjfasJkt1rEF91-MfOGdHHW20LL_h3dIEX1NDIRLmtNM72qnYjK7KNqdmKynfP8Brg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=JITQVUYcmTcR4Xl8CpISdmx9W3PBsdi5o4dvCbS8oPYs4Gpgqnr62wmZRpUh7nTiAhneaOM0gERumebXjos1cckjr0162ymc-dd_D93usPQnrt2aWYRurLcvRHVDc6y8Os67qcVo6sroNUxaxieXV5Nad1zLzQDL6PnBuyQzUzgTrA7RahcNGN5CzDNHcGq2dhJEvS6Rnls_MxGlF7hVBmRiQAxhYq8TfEOurBSrb7_THIJTg8aj4og1gTILtSaaF9k-1Lu5WrJRdZY1iwhtKjfasJkt1rEF91-MfOGdHHW20LL_h3dIEX1NDIRLmtNM72qnYjK7KNqdmKynfP8Brg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjIUWXJQ_G-XEmCzNOIrU30ep1__vCrHrP_u13qrGrBqDyp_hhF9D68S7rSYzJIZQjb-9OLPfnXLsxl22dKjnQfQBQi6eJQV5TDAoYPm51Ygc_QUvS7YCFggdWsYzspYOUW_9Yysh5nZlujwQ9EnQTldjn8dwOIDQNbeBsULCAoqAxG46r2j3BFDvFgRlRDzPEml-gw_MofkO4MCIe1w51R7LQjTBDiFlOU1B_7bQz6rx-aOiDKcTzsrI6Mg5EYskgFsWP-Zl5YH-j23QiHBQ0hEB6JOPI7Tn9CglMDM_S3abZR2pdYTCfaEAo2fCJlElHK2I68nlty9gK8ilrd9_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwNYpfDT7bJZv9gckK8fo6fBqm1NcSG4k7CaeniYaBAF6UPx2LDcgHXpNQwoUXuI_wvq4fHCELCCRggQm1oZtl4MCN6TaVE1dmMiB6n8RGZ5IQVreZ97MWUrsCIEbiVn3Ny6fgaEFRoBj8KWz-OsTlvnws6cQ1GsbLCAJco32jxn7Q-LpNkwoZJ0XKp3usAzdl0WAQtxK4B5n3WWgOOGVmI0MSGi13a9q6P6e-BdcefIVI635lXb5uCiKbenOJ9ivrjl8Xr4WXC36pQxDHL5EsmXV5TJ8kQSLx6CXdsIm2qtaF33O2_8-Wrr4s-Y5uPVv4JAmmWslZ9jaxI6di9Hcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWHo3pA9I9MV9zUIPsDXXTEKcBpX0TMsBVOVS_AUbz4t89eSVc4k1BW80v7Xgx8cX6yTJ9PgiglB8iQD5jRLE_bJL8Y9_l-A_WDQgYe17Mn1D3icniq42Vyp2ILinrB1ZHPXQTEkf_8uzpKpC4RARPWzArzVO45iSMlpuAYADb5BTMhBXiY2vIC-x7ErMH7FhrbawYh4RBuUBsas_r1yWlzjdOdVa1jvhRvas7coimNuknQqiQLQ_Nj0QYZWrBaOkke8bllQImItAPzzhAFGmQNHBtckNPDrbOrIb3RNnf_hVlAEtcBs0HQBijeCD6pSRfK3YzQQffd9XaOsfjVybw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=YoH8nnmutbSX1GfSvZ4uKRW-oyzk1PSVMEbYQEdy4RaQpXSd44wkgwzCmPvsRuepNDdktp84O7g78DQMpGfo82nc_pK3_TlBijVLB8bXTqYoCSgyytnWCggAa-O8gOPqQUfeiw25712EM7EYt-8rfkZ0YYUF8OoIzSH1R0OCxoMH7vNZYfk7xIQo9cTmF-416WT6sf9x3nx0CVTSEACmcxjzqorykRoY2YlbMF2BaeATa86UEhijb84DC4DTUv_AZ18mgxzRF8ZECGdyV_FS86kb-IuZ9HVPOqzZ-tA7jUUU9tzCN_-3-RTgOaai-fz12WdFEevEHhn732mp0a5HUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=YoH8nnmutbSX1GfSvZ4uKRW-oyzk1PSVMEbYQEdy4RaQpXSd44wkgwzCmPvsRuepNDdktp84O7g78DQMpGfo82nc_pK3_TlBijVLB8bXTqYoCSgyytnWCggAa-O8gOPqQUfeiw25712EM7EYt-8rfkZ0YYUF8OoIzSH1R0OCxoMH7vNZYfk7xIQo9cTmF-416WT6sf9x3nx0CVTSEACmcxjzqorykRoY2YlbMF2BaeATa86UEhijb84DC4DTUv_AZ18mgxzRF8ZECGdyV_FS86kb-IuZ9HVPOqzZ-tA7jUUU9tzCN_-3-RTgOaai-fz12WdFEevEHhn732mp0a5HUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0zmFOvSEowma9bgfPImf9dMLHoynn-ItlR20rgYYmj7jtLTJ7xVF6CCz6YVHXpQ8c0q6tlji1qOg3ZvpbLH5gCZZq6d7Nt0yW__9YUzhltP5PNgwHJ79iQRqX-ujw7Ext7VAWhQON7ZTBTBJTZhJ9SHoo1rx7BTeOgAFfh-xxjJPSGUtGzitHOTsE6hqq2dRvV973vd4Xg1iy87pkSOJoJOWzPIAztYo9b4cFVOnNDyojMP68e2jqPHtz43f9C1ntTsnVj3wWTZSspBNlBHsbJcZy3LaL2JZTRYHu-DU8DSyCTANJM1JOQohFFbeHhfHwtE-CNC190HrkoeR-WISA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu1h1y8FMianzy7_uvJSt5LRXeegfASmzLKXQrCzroTtvbEVf7EbNvtpYd6tdaOEonMdmPE9ohDxo8eXxcL6eptNAcZPNq17P6C39P1q9-PBABbdCAyc8PYYzymGD_I3PZLw3nKrD5CSXhHsAtEhLttM4HTMBcT6u9cJmXcYO6m7znL263HNk7Zp339lwWzH01vW9RZT6sZPhIuI3K06JDKHvGsU6_mf1YdfZv_kE5N9602wLxWGpiogeF6bxFW-b0QjpXCj_7fEPUxKYBXrkvaCb2oPwLYeKvbZ5ZJbPG5B2FbckkY-DgdhLRsjsCl_RMZc1wyHQ5C0iIxbb8MZgDxI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu1h1y8FMianzy7_uvJSt5LRXeegfASmzLKXQrCzroTtvbEVf7EbNvtpYd6tdaOEonMdmPE9ohDxo8eXxcL6eptNAcZPNq17P6C39P1q9-PBABbdCAyc8PYYzymGD_I3PZLw3nKrD5CSXhHsAtEhLttM4HTMBcT6u9cJmXcYO6m7znL263HNk7Zp339lwWzH01vW9RZT6sZPhIuI3K06JDKHvGsU6_mf1YdfZv_kE5N9602wLxWGpiogeF6bxFW-b0QjpXCj_7fEPUxKYBXrkvaCb2oPwLYeKvbZ5ZJbPG5B2FbckkY-DgdhLRsjsCl_RMZc1wyHQ5C0iIxbb8MZgDxI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=L-dCzrXTspbUmg8_RluDGT7c5L6gTUo_JW6QutkooB_E_jCH19DTV6-5rz31nnaBTwvQClcQ3su9pL9vIngBHvjjnbdMdmNH4AXO8uzBw6yXA0MRrMXaANxQOMaeg0fQVER6BUdYDBGuo2n-eAq3cJi65raypz1ElRGJOXnfvE7isb6eKYR3uGUrulp64e1nUXXcahqU8w-MYarPEVpn8XCibL_Fd5FAgoPFP64Lcgv5lsxxZbPKIivzfg0ekZ7LfcxRr_OBXT0nm_vh1cfgVLQFujbcsH8aMAfbipLjWH7ZR34aK_iDb46Awr1bdm2ncDsSLCzkaaJ0U5wegNTPOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=L-dCzrXTspbUmg8_RluDGT7c5L6gTUo_JW6QutkooB_E_jCH19DTV6-5rz31nnaBTwvQClcQ3su9pL9vIngBHvjjnbdMdmNH4AXO8uzBw6yXA0MRrMXaANxQOMaeg0fQVER6BUdYDBGuo2n-eAq3cJi65raypz1ElRGJOXnfvE7isb6eKYR3uGUrulp64e1nUXXcahqU8w-MYarPEVpn8XCibL_Fd5FAgoPFP64Lcgv5lsxxZbPKIivzfg0ekZ7LfcxRr_OBXT0nm_vh1cfgVLQFujbcsH8aMAfbipLjWH7ZR34aK_iDb46Awr1bdm2ncDsSLCzkaaJ0U5wegNTPOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=hpacfJfnXjHHMJs87pawGZuFO5R_eue_q5nLNA_9I6t4WPFfWHBx8ekeQ024EeH1KVSMvwOSkNUdkLzLerCPpVyXNBDsXdA-SX3gXgF0o741qFlSziCRdsBVe5wWwGMXkUjATZYpGCqKqmjdMMrwXpGgj5SzcZBs5brobYBS-FJLBz7WjxttyTiUYURgiuqMbTqjhpwj7bt61eom9T-jA-plyJVFW3wLptb6KirVo-KjvSvSm_psd3_WdYoCHaYkWdiS12h0L_LhwmlAd7Nd6ylePQLszDJCeoqI1UoLWHTcSeKPJwUp2GNgKvU5RTGRJLkNFUhV4Tud6w_3IvQI-A-0MdMaiavftHtslh4dBWjpice0cGRL6wq4g6qK7O3LECkepAXmB8KcRyKqLII8J2s4vRnEdpQENUEr5jrDlo4V_35J8Ld8r0O3HvG2mKv9oORGboP3pBYyLlFJgNgQ5oVcbNchaB88eF-gsycOo3OfND6BIeqJNl84diAhrgv3grVgLOUBzYse0CylQ1dwfYyC2SK3SAymVlEX7nl3S77r3ttMVuBGUvrtNRaEm791SHuesRqO8qMw57T0yneDQvD3Vs-JXLr48dYH7edmq-73wDsMCSrPf2-joWcRIHXEcUlmN2K3dITT5ol7bMFkg2zMiL0js32b-lSrlpeYn68" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=hpacfJfnXjHHMJs87pawGZuFO5R_eue_q5nLNA_9I6t4WPFfWHBx8ekeQ024EeH1KVSMvwOSkNUdkLzLerCPpVyXNBDsXdA-SX3gXgF0o741qFlSziCRdsBVe5wWwGMXkUjATZYpGCqKqmjdMMrwXpGgj5SzcZBs5brobYBS-FJLBz7WjxttyTiUYURgiuqMbTqjhpwj7bt61eom9T-jA-plyJVFW3wLptb6KirVo-KjvSvSm_psd3_WdYoCHaYkWdiS12h0L_LhwmlAd7Nd6ylePQLszDJCeoqI1UoLWHTcSeKPJwUp2GNgKvU5RTGRJLkNFUhV4Tud6w_3IvQI-A-0MdMaiavftHtslh4dBWjpice0cGRL6wq4g6qK7O3LECkepAXmB8KcRyKqLII8J2s4vRnEdpQENUEr5jrDlo4V_35J8Ld8r0O3HvG2mKv9oORGboP3pBYyLlFJgNgQ5oVcbNchaB88eF-gsycOo3OfND6BIeqJNl84diAhrgv3grVgLOUBzYse0CylQ1dwfYyC2SK3SAymVlEX7nl3S77r3ttMVuBGUvrtNRaEm791SHuesRqO8qMw57T0yneDQvD3Vs-JXLr48dYH7edmq-73wDsMCSrPf2-joWcRIHXEcUlmN2K3dITT5ol7bMFkg2zMiL0js32b-lSrlpeYn68" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=qKNuuSaQSH54eb9ANIPFS_qc-5caf9L1x_Ntylu3r_BZu2ZF196OVYwFSaNXE7dVeHmFtTOkwNz9leMqqGa_E9qzsAeGRm8vYoetmK0VYP-SGYE9Cxf6jFMvyxPQfPkDxdewdVddlW66ABEMduJ0QOXI5eWIiDx5_G2OxEFuA-tFp14F67JSujyYdWdhryvO53YzOh_SqsP-evtqdSPFDjGCYrkGTQLegRlvS4spftcN1zAlGQ-Wi1dCIld1llhSbn_lfL9_Uovm4um_JzB-Y-msLQv6UOqx286eT6jPkffJ3caXmqMq2IhPkliDjFr4QVsGIg9LGJfeixHh1Kkr6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=qKNuuSaQSH54eb9ANIPFS_qc-5caf9L1x_Ntylu3r_BZu2ZF196OVYwFSaNXE7dVeHmFtTOkwNz9leMqqGa_E9qzsAeGRm8vYoetmK0VYP-SGYE9Cxf6jFMvyxPQfPkDxdewdVddlW66ABEMduJ0QOXI5eWIiDx5_G2OxEFuA-tFp14F67JSujyYdWdhryvO53YzOh_SqsP-evtqdSPFDjGCYrkGTQLegRlvS4spftcN1zAlGQ-Wi1dCIld1llhSbn_lfL9_Uovm4um_JzB-Y-msLQv6UOqx286eT6jPkffJ3caXmqMq2IhPkliDjFr4QVsGIg9LGJfeixHh1Kkr6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXypfAUsFt5oi8Si8qDEH7igR8B8zcBndOXhdhKd9amNhxvafYMkPn_jgl6EEW8_IZXcbqf5VgpBeFLGEZCGT--aOHusBZ7jPS6IU6BfuMWQZ9nnuq8kxbAhbbnG1p33nQ_1Jh1pHBGipOXAF_3vecpFy5uiLhjo0qcFSTrYpVv8Wp9sEeP73qJChwUTyQxZdCynGvATF5F41ciAfl6K-4ZmY-_e-S77dsCWgkogO6j7Gt_CgkhGeZottn51OBvGhtQdqN3In7gzPTgGE5dsWe39hx-ZNj8qMH82kW2awE16F_LiK5oIpy-L1VxtnnKu8J_emCJoRbu-oo04cLoETQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=bySFMFLoku0fddppgtt38056qm96ALLjMu6ismY011jsMSYvBBChsDkRstOwAZ_vGltU-eXaMJaUt16YbsMG6xD0vM8uuCt4gwInsWdWfo-ozQoYrMEBzRFvfJOuDuN2Wjsv5rV7SLr_ws0cAZRkHUglIfE5HfqEI9tAPU_FcP66v4KefRinQvLlg9x4dCqPZordimx2WAR6jjVx_MLWHWmftUWBFWpTbZkoxZUr8933u4yrn1fnKIef0V6s7LwxHb_2lZky83314O5OuiVacs3o9MvUZ0rJRzrn0t-AeLOuCq129uO8gDbNXm8Zn73X_b_7gwvfWYgCK5O0UQhKSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=bySFMFLoku0fddppgtt38056qm96ALLjMu6ismY011jsMSYvBBChsDkRstOwAZ_vGltU-eXaMJaUt16YbsMG6xD0vM8uuCt4gwInsWdWfo-ozQoYrMEBzRFvfJOuDuN2Wjsv5rV7SLr_ws0cAZRkHUglIfE5HfqEI9tAPU_FcP66v4KefRinQvLlg9x4dCqPZordimx2WAR6jjVx_MLWHWmftUWBFWpTbZkoxZUr8933u4yrn1fnKIef0V6s7LwxHb_2lZky83314O5OuiVacs3o9MvUZ0rJRzrn0t-AeLOuCq129uO8gDbNXm8Zn73X_b_7gwvfWYgCK5O0UQhKSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=s6rO7E9wcpSiWH53aXj0KeZ63xNhLchxgKRLUwE2VL8XY3-G1CWisEyF9_PYsetoK92NLFTIvtPoX7VttXCHH1oxZTnI1H-K0210Ue03LyCTnCri6_AF1WqLXA_YHC_zkNgUSqnhqSwllMqJwWZGvqallsleUiTdMz5O10qPozSw0J_qZcvErQwXiWT_wAUwCAYnSYlUgRtt_HLPA5DSf1neWDVjKdfH4_RuptmEoBecMyx_8Vm15rMMCH80Z-qnMGKjeNW_TKaO2oYjAy6dlU8BOJLZVNr0KkzIpRjDOldvZtnFna_m94kHBI4HMaqEA4UR0e_ZefK4-IOeCE8vkRUn3zu8g2_xoeIV6vepCGMfocKYIFcjkZNuv6hWJX2Ln3s-kpU30j9Q_OTW7SeGv4ndmO3QepLAw7-c4jjyBYTLWBlVq6inso5J_r-hOV1uQz5q5l8Nq3MuabVCybDpek8AkVwOn1rplPfNQsnaHg7bFHXO8yJjYoTeTFjmiB-v6H1Q19aqCJbziNqKSp_-r6GZngtg5IJj8D8H2PW5Fj6F1J0Ts24jqQGa7wDq0VAgLKgCpExtWrtQuwBnR9TlT1_vXccX4n-0gtKuFPQCCtHhzeOWm7Ov2nVRtFfHk8aXvY5GrBYXEnh723QG-rsbgPVmdm7JKK1AyVrefDWknyM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=s6rO7E9wcpSiWH53aXj0KeZ63xNhLchxgKRLUwE2VL8XY3-G1CWisEyF9_PYsetoK92NLFTIvtPoX7VttXCHH1oxZTnI1H-K0210Ue03LyCTnCri6_AF1WqLXA_YHC_zkNgUSqnhqSwllMqJwWZGvqallsleUiTdMz5O10qPozSw0J_qZcvErQwXiWT_wAUwCAYnSYlUgRtt_HLPA5DSf1neWDVjKdfH4_RuptmEoBecMyx_8Vm15rMMCH80Z-qnMGKjeNW_TKaO2oYjAy6dlU8BOJLZVNr0KkzIpRjDOldvZtnFna_m94kHBI4HMaqEA4UR0e_ZefK4-IOeCE8vkRUn3zu8g2_xoeIV6vepCGMfocKYIFcjkZNuv6hWJX2Ln3s-kpU30j9Q_OTW7SeGv4ndmO3QepLAw7-c4jjyBYTLWBlVq6inso5J_r-hOV1uQz5q5l8Nq3MuabVCybDpek8AkVwOn1rplPfNQsnaHg7bFHXO8yJjYoTeTFjmiB-v6H1Q19aqCJbziNqKSp_-r6GZngtg5IJj8D8H2PW5Fj6F1J0Ts24jqQGa7wDq0VAgLKgCpExtWrtQuwBnR9TlT1_vXccX4n-0gtKuFPQCCtHhzeOWm7Ov2nVRtFfHk8aXvY5GrBYXEnh723QG-rsbgPVmdm7JKK1AyVrefDWknyM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2ME5xOc2S1glxp2b04HHH-kjmUf0mB4fjPSmlNCJfObU7czJ68g-n07oLZAOprAYda5EAvcVjsPCn01kdHskwu-EDK16SuwYXsd756cUeu7nz82cSRq2-ueCVOv2LRZTOlLsZt64H8Bv0_u1TGeYke6qNBi2r9NXDKEdY9rg_Wk7xL01FppjDbheGud4hzdKeiY-xI5dxTNUumkNjaMkT8CRW05o5W8maG-SsFqXIPSEi_RgwRa25ERXSJKgFzULvMTxSy0MeYYHrzDBRQvur7GPIHmfELsjIcjkZggifHxveZ_CG-WVFpxU-pvIW4r9HfLgcHbWyAccpcU02z9Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=cfc9MkicwoKhX_4jZMgKeuTbF17L5CxL2g1zFlwKdQNmsvsMsvl8EuxfSD6j6AgrV5iYqOYzBWKA_dVRDBd7CXvPxTveKeAg9y5UV0FbSNCKRLTum3HSrHNrtG1N06mHy1TndDG8m-HZlhrgj5mMULnLuVFbnA-0qINflS6awVBkbB71ujI7p9_S7KWKOrXCYvor8SjTmN3mh-qzsdJtP5s6_9YnohXtStaPe13phyv1U1RAJRpacXjXCKaEVKGkp7O3YKl6sAzb5DYB1Ln9Is8-2RSJdoie0EN4TeRzwpxTlZvGE0Z2uDx4fn-9lD5pbLQKgVbqcYrTDegOB9XiHq03JhkzHzOM0IN7MjZfhkl8QSDbGVDChjnjRFJADUxMdTl9udL_2JJvr2SaWT1ip20kwdIYMV9xxXht3p8RHXL7lsWkzZvqKHhQ9FtHR1N1hIL6-8Atws-Ho2E10PtMJO3IKN8cNqlmm1QhMrR816Wvsxq7CS2c3SHHT6EeGWh0bJMo9AlmEEPWcVtefak1buPtXzR53Ev88f5GgtjyI4KgoJ2CblvS0xpYPLukdsH0ZsxJBmKmDpf-fyqUjj_U6URu7zMGZINsbDNetkxr593aVDTKBgynYgoKlshechbFYAnN81uPfu0V59XQvy-uZOkcHscJ26YyQAEI6Vf05yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=cfc9MkicwoKhX_4jZMgKeuTbF17L5CxL2g1zFlwKdQNmsvsMsvl8EuxfSD6j6AgrV5iYqOYzBWKA_dVRDBd7CXvPxTveKeAg9y5UV0FbSNCKRLTum3HSrHNrtG1N06mHy1TndDG8m-HZlhrgj5mMULnLuVFbnA-0qINflS6awVBkbB71ujI7p9_S7KWKOrXCYvor8SjTmN3mh-qzsdJtP5s6_9YnohXtStaPe13phyv1U1RAJRpacXjXCKaEVKGkp7O3YKl6sAzb5DYB1Ln9Is8-2RSJdoie0EN4TeRzwpxTlZvGE0Z2uDx4fn-9lD5pbLQKgVbqcYrTDegOB9XiHq03JhkzHzOM0IN7MjZfhkl8QSDbGVDChjnjRFJADUxMdTl9udL_2JJvr2SaWT1ip20kwdIYMV9xxXht3p8RHXL7lsWkzZvqKHhQ9FtHR1N1hIL6-8Atws-Ho2E10PtMJO3IKN8cNqlmm1QhMrR816Wvsxq7CS2c3SHHT6EeGWh0bJMo9AlmEEPWcVtefak1buPtXzR53Ev88f5GgtjyI4KgoJ2CblvS0xpYPLukdsH0ZsxJBmKmDpf-fyqUjj_U6URu7zMGZINsbDNetkxr593aVDTKBgynYgoKlshechbFYAnN81uPfu0V59XQvy-uZOkcHscJ26YyQAEI6Vf05yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=TLqwqPUDlGYG3zNv7jerQxA_b1HRqmrLlfMOemPgJXOV5JzxQcj58k3_vrWpQbkstEwNdqgGOlnkGsA26jFffcsHNYmaJZLsXhMrkH6pOx8dzVO7haruMiplDrQnUdOUNzyLsEH6NFATJI0Z48ROUop5eF4eyOEptQsTKym1iV9KjEg_4u_L8iXaGMhWKf47-zFWNZqMPJ8kW3wAFgqma1ljMg6l-8kjQR9waKBflrOyqmLqAZ6OGzy1b_g0zuZuXbAxY8o5TyfcWmBq4hNK2NbB1YdbPVNKPfTv2WfkAI-1voOtWne5fF3AMF1nOOdNAF38SoE2Uv_AZOKNYhgki7edJiPFmhSsbvCpyNAXeJ4mPgF2Gkt8VY9jCyRPo5xBpVzpFxYhHsio6W6OEYi3mt_koXDWQGMrkNqelb2dv0xFkxS5bMHsuf4kmIe7Q-fFQ7dqgGCCTpfeLMZsJanRrfB3tG8fYRTCWbrMjdm7npcLQLQMglEyI9jIQJuu-Qkqn5o6wLk5KflIYYfOPpUCjjcPhTux7k5_uQl2Qn-p1b32WPqr742dR1Qk4S6PNYWEtbuiY2NiO7B_p-QujBPpRsKzi21_KBItowznXaOmKVxPQ5u7ZmivCWFiibeOQo5zGcjbd3DHV4bC5dECY0n-vBYP4MU96wFrtbsqB59yA0I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=TLqwqPUDlGYG3zNv7jerQxA_b1HRqmrLlfMOemPgJXOV5JzxQcj58k3_vrWpQbkstEwNdqgGOlnkGsA26jFffcsHNYmaJZLsXhMrkH6pOx8dzVO7haruMiplDrQnUdOUNzyLsEH6NFATJI0Z48ROUop5eF4eyOEptQsTKym1iV9KjEg_4u_L8iXaGMhWKf47-zFWNZqMPJ8kW3wAFgqma1ljMg6l-8kjQR9waKBflrOyqmLqAZ6OGzy1b_g0zuZuXbAxY8o5TyfcWmBq4hNK2NbB1YdbPVNKPfTv2WfkAI-1voOtWne5fF3AMF1nOOdNAF38SoE2Uv_AZOKNYhgki7edJiPFmhSsbvCpyNAXeJ4mPgF2Gkt8VY9jCyRPo5xBpVzpFxYhHsio6W6OEYi3mt_koXDWQGMrkNqelb2dv0xFkxS5bMHsuf4kmIe7Q-fFQ7dqgGCCTpfeLMZsJanRrfB3tG8fYRTCWbrMjdm7npcLQLQMglEyI9jIQJuu-Qkqn5o6wLk5KflIYYfOPpUCjjcPhTux7k5_uQl2Qn-p1b32WPqr742dR1Qk4S6PNYWEtbuiY2NiO7B_p-QujBPpRsKzi21_KBItowznXaOmKVxPQ5u7ZmivCWFiibeOQo5zGcjbd3DHV4bC5dECY0n-vBYP4MU96wFrtbsqB59yA0I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=a1EgfAFXIRzVBo3TlB-Jexu-tjqPq00WBiHY8b9K2lY91eatbPBDxG6_13_6sK1iLa8F23L33CceDNn1yxhtQYCHwlXJuEgqEWdmzWHEVF4s7xSNBGcvn7dmp9eiUz15SV0jcX4rBs5a19bzScM8cC3E0pNKC914m1Ovrb50KqHnGezEzisHxxfoxrcE31zKD-xN6kwDaYY-XUoMeTpewawqkIJiHDIqWMOScp0rCmOXMBAEZEoLZHJmYBTD7toO2vIpUCRSS-MtCwl2-gdho18tAJtQEusxFiNzKy-lY_znRIpMleBZyEH6AQN91eDPbanHOa2co3ua6wNFCnurvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=a1EgfAFXIRzVBo3TlB-Jexu-tjqPq00WBiHY8b9K2lY91eatbPBDxG6_13_6sK1iLa8F23L33CceDNn1yxhtQYCHwlXJuEgqEWdmzWHEVF4s7xSNBGcvn7dmp9eiUz15SV0jcX4rBs5a19bzScM8cC3E0pNKC914m1Ovrb50KqHnGezEzisHxxfoxrcE31zKD-xN6kwDaYY-XUoMeTpewawqkIJiHDIqWMOScp0rCmOXMBAEZEoLZHJmYBTD7toO2vIpUCRSS-MtCwl2-gdho18tAJtQEusxFiNzKy-lY_znRIpMleBZyEH6AQN91eDPbanHOa2co3ua6wNFCnurvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=VFuGRfxNriREwM68Mvo4D5bIoJGcE7UhyFO-VsA417WZyG_H8-MSLIIdGww_6yhz-dHttqtkG_UJ925Yo01rZ2lboN-FpDok04PzO6QsLPxihlG7bLFN3yK4UMtuVNg0mz7c0qonSp6vAEqoGiuyvjgx7SXEnzecldHFRcEWpK-3HJicAb2pplvcO1-UoxX_LpLRc3o2xjy81GWdb0chn3EXrxFTWo3sQEw990CrXZ5KqPfqT6kHGQ1zWLlwRVz6-thmjwb2yVl43uj6gK_AgXe_nbwhklPbHG_NWkT9FYHWggG8sQwxWFq_cOEhZWyJmuzyOetIf0W9P3fbVjkTww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=VFuGRfxNriREwM68Mvo4D5bIoJGcE7UhyFO-VsA417WZyG_H8-MSLIIdGww_6yhz-dHttqtkG_UJ925Yo01rZ2lboN-FpDok04PzO6QsLPxihlG7bLFN3yK4UMtuVNg0mz7c0qonSp6vAEqoGiuyvjgx7SXEnzecldHFRcEWpK-3HJicAb2pplvcO1-UoxX_LpLRc3o2xjy81GWdb0chn3EXrxFTWo3sQEw990CrXZ5KqPfqT6kHGQ1zWLlwRVz6-thmjwb2yVl43uj6gK_AgXe_nbwhklPbHG_NWkT9FYHWggG8sQwxWFq_cOEhZWyJmuzyOetIf0W9P3fbVjkTww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=uvEB9p0eKaLab9UHEGd3TP_-li52Nh-jnbnfxEwMHWyQw8T_9wCOso2eyOjYL1WSRKS1q71ZRA6sAEBo34ptMvGxRP5PQV3W7H_77FKddVbj9S7uvFaQV6apu1DU0k35bBzM_-3Y5iryZn5U4u5GTsr6w6ADc5DTTU0uugtciLQlCUpU2MlXZzCVuXGMD5DJlW8hqlISIvZewyLB-XPYB9SXA4QF0qr5uM5NsBhMQPAAJEYtBs-VeiDHNO4qvSrtHbsepQffBb0puTocOkAjQ70aur-OrnajluEcTZ1pM2U-4Mmeq6isw-swzDifhoWYeCJhBbiaLmoUwNqJCfGxKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=uvEB9p0eKaLab9UHEGd3TP_-li52Nh-jnbnfxEwMHWyQw8T_9wCOso2eyOjYL1WSRKS1q71ZRA6sAEBo34ptMvGxRP5PQV3W7H_77FKddVbj9S7uvFaQV6apu1DU0k35bBzM_-3Y5iryZn5U4u5GTsr6w6ADc5DTTU0uugtciLQlCUpU2MlXZzCVuXGMD5DJlW8hqlISIvZewyLB-XPYB9SXA4QF0qr5uM5NsBhMQPAAJEYtBs-VeiDHNO4qvSrtHbsepQffBb0puTocOkAjQ70aur-OrnajluEcTZ1pM2U-4Mmeq6isw-swzDifhoWYeCJhBbiaLmoUwNqJCfGxKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=OLQ8T0azevFDzWrf-FJ62CAGiJHS8nSRdODmI5fT5F3Unb7OXUGa1PIf-5fUdqmU5OF7JaPqIsfgAzYsnzhaH3Eancjgw4MZO-IP4jaNbDV822SlZgNRw33jAKoJGkFn4rcZeUtY__WsUTRwP0UNRRJoCAJiyaVoBwSKhVHIpoNqZypi3zuNf2yneXyEFQ8jMMGRONgKr3pfwmlpVYi2HMwjJ8uNx-Cfpgb4K9OSZsvXlOfsEpq3tpypgRA-AhUoE3S4B8yklISS9xRhPpGEeyybNHbSL196Uagm80DEkSUxOG346dWgCwQ1xpcH6eTlBgw-MZQl9Q3LGREvPUo5jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=OLQ8T0azevFDzWrf-FJ62CAGiJHS8nSRdODmI5fT5F3Unb7OXUGa1PIf-5fUdqmU5OF7JaPqIsfgAzYsnzhaH3Eancjgw4MZO-IP4jaNbDV822SlZgNRw33jAKoJGkFn4rcZeUtY__WsUTRwP0UNRRJoCAJiyaVoBwSKhVHIpoNqZypi3zuNf2yneXyEFQ8jMMGRONgKr3pfwmlpVYi2HMwjJ8uNx-Cfpgb4K9OSZsvXlOfsEpq3tpypgRA-AhUoE3S4B8yklISS9xRhPpGEeyybNHbSL196Uagm80DEkSUxOG346dWgCwQ1xpcH6eTlBgw-MZQl9Q3LGREvPUo5jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=IYshQUfwpbiFUb56rXOEx4z4cAXJeFkIcztUJXsctVl2gO7FPp1EFAyaDbhB_A2nHR4ZYAUt0Uxu83gfY-elUmKZjhfZP2tG8-2gaxyzdb234V6owZd1bK5bQ0oD1YRpRj4LPd7nA5ltjcexVoaD6o6z3V7_Gra120ARSW8jhIDvZ_Ax05CBQNPoLcyPXA8nbE-Y4GaiGR9m8WhTlCGrb1HJkIrf-0OFIkFCToCoq2HJk7P_1fUp0VvsPrVo4TVU26eGTyro9bG-ZCpROBYhx3Szk77Lv3p4PCK5rcILUIA-Q6B-fRgaAvInfHBiQbRsdE4NIV0N7TR17wmaOrZwmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=IYshQUfwpbiFUb56rXOEx4z4cAXJeFkIcztUJXsctVl2gO7FPp1EFAyaDbhB_A2nHR4ZYAUt0Uxu83gfY-elUmKZjhfZP2tG8-2gaxyzdb234V6owZd1bK5bQ0oD1YRpRj4LPd7nA5ltjcexVoaD6o6z3V7_Gra120ARSW8jhIDvZ_Ax05CBQNPoLcyPXA8nbE-Y4GaiGR9m8WhTlCGrb1HJkIrf-0OFIkFCToCoq2HJk7P_1fUp0VvsPrVo4TVU26eGTyro9bG-ZCpROBYhx3Szk77Lv3p4PCK5rcILUIA-Q6B-fRgaAvInfHBiQbRsdE4NIV0N7TR17wmaOrZwmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=IPyslA1pWBXnx-EufgKk6JLJy_VWK2pCc_Z32ooDhgNLoIx1voy7SCMFdh9fGJtp7ZJ1CsWrxxRnbOSCDM7T5RZvdGkL1lOzRMM4vr7g9RxUMd1DWIB9s5-2lyvqfOnY2v8xV7RRFhHMVpj4W29T5sflhpUIpADjxOaNiolC-wTeIONcQne6VC-8gvA-LrTHcC9uSUNNPw2mI8WdeJt4sUpADh4CRXOwx1cyLVYTQViHMR9WEHytaPSdgtFm1uZTXrGTKNbVTrJG3QiK51m5Qc9iazfCjnkGMAaQdTQBBG37NjpXkKv19IJDPZKV4tKMrAhp8I0V9JziN4pUHOK1xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=IPyslA1pWBXnx-EufgKk6JLJy_VWK2pCc_Z32ooDhgNLoIx1voy7SCMFdh9fGJtp7ZJ1CsWrxxRnbOSCDM7T5RZvdGkL1lOzRMM4vr7g9RxUMd1DWIB9s5-2lyvqfOnY2v8xV7RRFhHMVpj4W29T5sflhpUIpADjxOaNiolC-wTeIONcQne6VC-8gvA-LrTHcC9uSUNNPw2mI8WdeJt4sUpADh4CRXOwx1cyLVYTQViHMR9WEHytaPSdgtFm1uZTXrGTKNbVTrJG3QiK51m5Qc9iazfCjnkGMAaQdTQBBG37NjpXkKv19IJDPZKV4tKMrAhp8I0V9JziN4pUHOK1xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=Nx49Dg0ZQVgAZIsozf4-RCj4IsN7xdBK5AWP-rj7emHHNm7EaRbWAkzPL2uC8NYzHOfem1uPG06Wc1XMUBOHpx6cjtRpk6p3U0OjSjwBhglx-oH0KuNJ-RhmZJsjdajpjEaFFEFH1cZblc5CFTAFzqj6O7vWOOyrviVpfxaKk6HEzhE51-LYTt8vcStoUmU6_zbU-eQWPGaIxKA2PkuJe5uVyPOCpZ5xzNQ7uuYJ4E65QT2rKjOBDb9VwyB-Xv1lQlpRMFrKgGTLqNR60rgvm8AA9o5HB-ZZcletYB-bJKhHcGnZ5ruZktALMhvr4wRKmqNn-LgT2muV2uO7VFTfww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=Nx49Dg0ZQVgAZIsozf4-RCj4IsN7xdBK5AWP-rj7emHHNm7EaRbWAkzPL2uC8NYzHOfem1uPG06Wc1XMUBOHpx6cjtRpk6p3U0OjSjwBhglx-oH0KuNJ-RhmZJsjdajpjEaFFEFH1cZblc5CFTAFzqj6O7vWOOyrviVpfxaKk6HEzhE51-LYTt8vcStoUmU6_zbU-eQWPGaIxKA2PkuJe5uVyPOCpZ5xzNQ7uuYJ4E65QT2rKjOBDb9VwyB-Xv1lQlpRMFrKgGTLqNR60rgvm8AA9o5HB-ZZcletYB-bJKhHcGnZ5ruZktALMhvr4wRKmqNn-LgT2muV2uO7VFTfww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKDVtGDtekjVLuCVpaExyTXBCjVytVWmRsMqvQ4Go6-LEIIn2Js5xozywQ3i1VzwyDJi7JbGnWyKEFpTYpu0uwNBQnmbzDD0nuu8qybr7bOdJTBvVy8D_l6mXfxtfV8NAql0w088YyCOe4R8rQf-EPoZv9srrvvNNT2uuTU9ODbgIpHrbm1i9lrIj9YJnUGaFk9uq9Zgjz8bOqqcfI4vPQC4rwf67KPdn1nnStLF9SNgfKB8fxD6GQEkoyPyWZvXCUdxmsAp9bTlvADuqJVn4FhgPYgaFJN4VvmfjLMAuRnkPreB-CQoA-zNceZj96PPeBD4Za0MP0Teyz5QBCTkJg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=PS5tOxhN7yG6vfwUaag5cJGoyvqH49smXGrfiXhfBgEe0aI9JD17Og2_ZEF35wnEG3MsKWCXfRjqP_AWi2AVpMQVk7y7kyT0SGT1SyAgummlP8V1Yg48t_Ecq9vysGo_5DlnKufmsFrIi4cT3xEVsgcCJqjEfXqmaWaOAg7HjCuk_bWjBaPBZa-9uoGjWx3x8p_eFbRaU6_D-KJDxC1R1I97np7MnxFi3Bti7R2uuy8co0eD0gVvHyhhLFrxVSS9snrtj2nuxETeXGK15BG0Kr3-kaPjJsxYetoIKpXFruBkAEERIgZ882g_Bbml3oAspdT3c0kKyOJt3_NCik8RWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=PS5tOxhN7yG6vfwUaag5cJGoyvqH49smXGrfiXhfBgEe0aI9JD17Og2_ZEF35wnEG3MsKWCXfRjqP_AWi2AVpMQVk7y7kyT0SGT1SyAgummlP8V1Yg48t_Ecq9vysGo_5DlnKufmsFrIi4cT3xEVsgcCJqjEfXqmaWaOAg7HjCuk_bWjBaPBZa-9uoGjWx3x8p_eFbRaU6_D-KJDxC1R1I97np7MnxFi3Bti7R2uuy8co0eD0gVvHyhhLFrxVSS9snrtj2nuxETeXGK15BG0Kr3-kaPjJsxYetoIKpXFruBkAEERIgZ882g_Bbml3oAspdT3c0kKyOJt3_NCik8RWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=TcVNkmzqWTfblePEQs-l1XSYqtQlgl_vnKnwW5pwcNX4VEjwwkZpAbJ8PhUBymFmFmcWg8JpYU6oobOJO7J-xEfCPsYJiXrY08prEqwhGQYyrGGiHMjzzZGeddskvnX4gsF6Cz4sALOR0oI9_xgFvSdqU18TrA110znY6sgoUWPpmQxgDgpqIG1n8w82SYqZu6uPkNuuQNp7HmxUGvRkAR58G5FdNso4dUJ56WLPam1ckoJ2nsPIyZm1ks6tOC9F5nCAfcB9FNt2hmSDYbijMJR5sbbcgF5RY8Een7_G90UZ9FRXu4l00JkeGzlBuMQIj96lJjvXizk2u-j9qCHUgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=TcVNkmzqWTfblePEQs-l1XSYqtQlgl_vnKnwW5pwcNX4VEjwwkZpAbJ8PhUBymFmFmcWg8JpYU6oobOJO7J-xEfCPsYJiXrY08prEqwhGQYyrGGiHMjzzZGeddskvnX4gsF6Cz4sALOR0oI9_xgFvSdqU18TrA110znY6sgoUWPpmQxgDgpqIG1n8w82SYqZu6uPkNuuQNp7HmxUGvRkAR58G5FdNso4dUJ56WLPam1ckoJ2nsPIyZm1ks6tOC9F5nCAfcB9FNt2hmSDYbijMJR5sbbcgF5RY8Een7_G90UZ9FRXu4l00JkeGzlBuMQIj96lJjvXizk2u-j9qCHUgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=ZicYhNbPW0BH4oWsDkqIqbYPYv5t96ZBQ4J1SO8Y-RBzEkEVeH4zA-Y2mb9uZC4px-3iE83pKEcY77Bx3MgkkR3wByer8nYnf_JkE0J2nAIz_9MPJZ0q1YNGCALoig5KCBNBtknnaUCColIIpnH62jmfP1YYSdwKs_mhwqRxapyqm67337jjzkqHcV7slj3Iyi_qn5DnLg6NK0dq3J49iSHXcgeESNaj3Yl2rCDHoLwaKIaH4uuY2A4w6LwnQkp5OnV3LqRgNL2oxlYWy95MfOT6hqUeYNJ1_doSHSC5A9t9ZwPQh1IKkfRLfWJEO743XLCn_ClVZLEmnRoX8shE-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=ZicYhNbPW0BH4oWsDkqIqbYPYv5t96ZBQ4J1SO8Y-RBzEkEVeH4zA-Y2mb9uZC4px-3iE83pKEcY77Bx3MgkkR3wByer8nYnf_JkE0J2nAIz_9MPJZ0q1YNGCALoig5KCBNBtknnaUCColIIpnH62jmfP1YYSdwKs_mhwqRxapyqm67337jjzkqHcV7slj3Iyi_qn5DnLg6NK0dq3J49iSHXcgeESNaj3Yl2rCDHoLwaKIaH4uuY2A4w6LwnQkp5OnV3LqRgNL2oxlYWy95MfOT6hqUeYNJ1_doSHSC5A9t9ZwPQh1IKkfRLfWJEO743XLCn_ClVZLEmnRoX8shE-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=HuxuzqDPbUkLbvHjggVGaSPAQJCYf8wdH7u0iemCiW8OwYfLQFdV4lhtYRqM9uBIR245808-Qx3zaIA4DBsrInaFi29ZvHSVSjuYqHTfGZanMRsbC7YNrZHwzJMXyvEnng5FpeT6cKl_Nt4X0FO22SvtpBjT9ZDcsQJF2oLJrd8BOpzkEDazzsEiFIzvc5tg6gLISFQGlqPcQKZFcwuJB-PMyICBwvLesdmoo6yr-ri8uvR8vgBBWoqHX8qVrXwgxNPlacAN35-2V0qN4_1yWG1VqCfvqB5seSEKpJVLhqI503xAWIP6M1_bI0gp0HXDCVqZHKwTkLZm3DSaV3Qchw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=HuxuzqDPbUkLbvHjggVGaSPAQJCYf8wdH7u0iemCiW8OwYfLQFdV4lhtYRqM9uBIR245808-Qx3zaIA4DBsrInaFi29ZvHSVSjuYqHTfGZanMRsbC7YNrZHwzJMXyvEnng5FpeT6cKl_Nt4X0FO22SvtpBjT9ZDcsQJF2oLJrd8BOpzkEDazzsEiFIzvc5tg6gLISFQGlqPcQKZFcwuJB-PMyICBwvLesdmoo6yr-ri8uvR8vgBBWoqHX8qVrXwgxNPlacAN35-2V0qN4_1yWG1VqCfvqB5seSEKpJVLhqI503xAWIP6M1_bI0gp0HXDCVqZHKwTkLZm3DSaV3Qchw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIR92WUFh0-XpeesGj4TEhFqjYYI6N66tz9XS9VGeIvkQr8reweAmQzvtTHfvMYNXU94bSwjHbLEvapiDctbjsh-sADN77Z0qgx36_TpsnzJAckhk7RLlq9wiVY8fmn_0aQqe6v8_9FcL_W6k91efp7LA2wg2ynXzu4xkz4nTtdsnZRi2CMlmVegeIoQXME_Ha5dHQvj___jriKzNmfbQmGbJtipbpOfqubAjEM8I97sVuMsgG21OQr7Eq0NF0xqJLd25r7uoZUlRUroUMU5z0domQ13gj-eBc7TE2jx3UV1E7sShKbR7NhvtPyFSC21lDNWHbd-FbRixQCcPVEf4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=MQ957ItPkfA0ams1HApXldx6rtWMLq-s89ms5U2dZnMAe6N5m0_74TzNePg7eTjG1dG2eVuI7dwdk0NXaSeeuCiD4UX6uIMvmgPILsgLDaZ2RDWc_dud-Zn8x_zMG4NDHoiOw2mWpo5huO6hkDL7owWCG_pUsI8lthcgVlr3WvAmhIRnTZJzGzMzF_w-cG6GK3aFIcaRFIGB0ZneS0LdaxVnDAj-p0vgU1k4IGP782YShntPf0kKP8QvgA7ty8zH6bw_Q8E2a3hjAhGRM_QJf7izfQ6F-AOwr2y0ZksZM92iO7n1Hx4gbS2HGG_puBdsKH-xGMbGyQBa1NHfcizxR4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=MQ957ItPkfA0ams1HApXldx6rtWMLq-s89ms5U2dZnMAe6N5m0_74TzNePg7eTjG1dG2eVuI7dwdk0NXaSeeuCiD4UX6uIMvmgPILsgLDaZ2RDWc_dud-Zn8x_zMG4NDHoiOw2mWpo5huO6hkDL7owWCG_pUsI8lthcgVlr3WvAmhIRnTZJzGzMzF_w-cG6GK3aFIcaRFIGB0ZneS0LdaxVnDAj-p0vgU1k4IGP782YShntPf0kKP8QvgA7ty8zH6bw_Q8E2a3hjAhGRM_QJf7izfQ6F-AOwr2y0ZksZM92iO7n1Hx4gbS2HGG_puBdsKH-xGMbGyQBa1NHfcizxR4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=eKXJd4QpnxsrgHPn6EbtAqiqjzldjMIrLXBw3PSkRYCAFTDKleslg_B0AXYNQVrmMVCRjvZFIVOzz78AmiS6_zPlanJtvZunrzc0Q1WiXvAS1sgbaWdtfqvIlfcmultDb-Rq63XZHmglH-QzbT5WtnjDPST5RBBVStT8xNiqe31c7ADXf58haUZBPWY1QhkVernGoXhKNVx7gCf1fOpJNUxLDAKQhuCDRFgQaIBfvTqtCix3YuhNYUW2Hn9un737Zt5uJTRQIUAEuFCXb2rXSUCZqBrBj3Egg-A4fw1OKKXsV3rw-zC1k_BcWrNEpXSw9jzJWDOmrvDiZWxprqQ1TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=eKXJd4QpnxsrgHPn6EbtAqiqjzldjMIrLXBw3PSkRYCAFTDKleslg_B0AXYNQVrmMVCRjvZFIVOzz78AmiS6_zPlanJtvZunrzc0Q1WiXvAS1sgbaWdtfqvIlfcmultDb-Rq63XZHmglH-QzbT5WtnjDPST5RBBVStT8xNiqe31c7ADXf58haUZBPWY1QhkVernGoXhKNVx7gCf1fOpJNUxLDAKQhuCDRFgQaIBfvTqtCix3YuhNYUW2Hn9un737Zt5uJTRQIUAEuFCXb2rXSUCZqBrBj3Egg-A4fw1OKKXsV3rw-zC1k_BcWrNEpXSw9jzJWDOmrvDiZWxprqQ1TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UO8uX9sdqR5_zfrWcoiFiR71k8SyHrPttXuoWYuEeimhJ4ndwtO1R4pIgPrVoWkVCti7AY7H6sTxyjWaP_2d_ekE0kqjCAj0qXoTnnkQEjJM-facKQ_czbmSLiVVSWwk8efXD0b0WlzP2f4fD8nlHiX_EXH4lDAuHoJegvLmUUYZtMuzdNDTHHara7AKSO_BoD7k5ZXQzEuwfmlHyI_OpKhCc17uTqhCCBv-eDerd_UxgtPIVxQm38VEiLGlV_Kw3rBXpNYNBXI5Ia9iRrUMu3vsEPzmne_WsaahwaXhWuSpPuR_NWiFJ4pZV6pwFBlxEEK5tMNEQDVtRupIS4gGZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RPTt-qzcwp5QMzQLhVWQf_SjKsjiALXcapyjHOoZ8wyWawlvfdcq4KezQgEFM1VCT0s7-vmnxKNMrjJveAOf8m8QBxQob1VD9k1cfaH2_igrBasSiNiAS4GVeFg9Q1c7_kLHPTvrvb6t8PVtpOAiem0IX366K5o_AjG1xGCT2O_fMptQBnL_THDiJb3gFzvwMvJOjTov5ePjPNCif8N1YeualmPvwiJD1QBBYIsrRf-nt9DJ7NYloY-SWzYuNTXl6ARKEPGfJS_II-3NujXh83k5lUbFZ3mRXVU2N_mIpdimPT2JrgVi_DUt8S2HYXPPbde78zP-isXAtOFOLZpmhw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Xwlgt9bP4yU09WRENunYJ0fvaLtJMjv6U0N4-23M0h_vdvtcPxAInvkNDnrC_hwMIcyyv6_rQPxOIMnTvmRTrGW0bpp3Bm8v5auxE4jheD_TrQhIVYKtBwrpgKeV3gBIq3XSRxL-bhuz05daWNUZhpIGTlDxrwPI9wfGF6gGKmu8JAKKUqDx27HOe69TKBSqctUPlbBikQdYkwfaKBURNEVfah-SdHkCAVnjEqzB1j0ahERnyDQNuzbN5D8iHubUixobKMYFM8jAo1Mk6Q7jDpRe5ko3nV1romyYn-JHzRqX8eE5IhNPxP9fJSILYMMgfZVBISYNp8voLD7TVTRAew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Xwlgt9bP4yU09WRENunYJ0fvaLtJMjv6U0N4-23M0h_vdvtcPxAInvkNDnrC_hwMIcyyv6_rQPxOIMnTvmRTrGW0bpp3Bm8v5auxE4jheD_TrQhIVYKtBwrpgKeV3gBIq3XSRxL-bhuz05daWNUZhpIGTlDxrwPI9wfGF6gGKmu8JAKKUqDx27HOe69TKBSqctUPlbBikQdYkwfaKBURNEVfah-SdHkCAVnjEqzB1j0ahERnyDQNuzbN5D8iHubUixobKMYFM8jAo1Mk6Q7jDpRe5ko3nV1romyYn-JHzRqX8eE5IhNPxP9fJSILYMMgfZVBISYNp8voLD7TVTRAew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xy9CeAqfyKhVTaBGpZJgm2klPZfpaAu2ppZxu46Mh_H2Ua2fTJpZffIIPAJOa7dax4sOE6Erui9rMaR5wazZ1stRxkSo27K6n286ebwGCvtxhxvhVD43D2sRc5g8GPeg3LMmM53Gb2G_XI5pqKMZTtJCGFQJd2h-e-wnVRU8eZNicPjf23QJfky4h0xv0OirtAHkVzlYfsDqMfMmZx4VDOT74KIUWeNIs98eBXS8pAiM-INiwNJXR8dk3aem36tCKFmu2FA4s1RbAQLMOPvbUKpvhKDRpHOlhpgitfaxea1AkamJ1siLaRVt8kPciKrDwJur3uqT7i4sDtsvNm_w1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vE7ZmbfdsldxkksvymryPRdwuDF9ra5vhny3KOlqlnLQulOHfef4juQt1kCWwtsYwUHkyovRuRgwzxHgmPT4GOtOwM5MGntZzION6z5uAdR794EwT2xRagZ8DqMN8RCMBWGPLllY_CKEeYGe2FDCSbhuB5bu7UZ-W8CgnxPZAND12x8ksZxKNfQKHovcU14w3IB-0KQgTYKiKVVEBa7IYHVuFScJ8WgZQ2UOnAzmRyJhDWl9WsyoTfLIq41_gstQFCELF1-Iv16cbw8YYkMHN_2ywbv_DMNjCXHpzWn5gqfJWpwaCaF56iEKcopQXVjNhpvX_p_pi6MHvttvNd7LWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdrs-TDQRI_n4lwqGFqN8Sbktiyo0oPQ0idVAxJMYDWC2J-Lrn_GJt2cF9RVFqX29eQFkESbqjHkNrFbjt_T4Hv-jOvSVEhlWTl02mz6CWEwW_lD2EODRYBVBcWmzJsKlnTUQ5nSXSMjHamG0jL3BGdH7X3X2BAYyzc2GU0E7BzdwQ_W0Mi4EJqwsQ_zIiNh47XaQtkrAfMQAxN0MGD4pFkJRhEOwgUqFwrhNX4A1jZNH3N3URDrcNiAmCRnnBULmlDpsHuJ1PVgQJ9zl_eb6qxkj8SJ1klpY4JOwRUo6mFoBL0nBIVvaJ6ZiSvkd8CPaENnIvyPxp4BqUJJcz8VDA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=Bt3QI2GptIsqPZ7kNnRippR2amLHvTqX72DP0kPTNkNHSez6oK2xam-XqMzeg46TyUjSGkcWO4ZD6s8SC4KPp4wVoxWBsHAfN0dI4JI3tpn0z4Ov12Im-o5C9-BMzQK-KRJJTY5WeZnnvyuAHml6tn9asAs9cAyyquNBIQuE7PsM6WC6ZZWlNLHJLW603FEsf0egIcQkFBOUk5gCSjrrzJZr83SOyBGcV4b06Rev7KchnXcH4PFmzhoiBO1eQjgySVFscYtBCkuev6zIrfchIs-98SdyT5bVnuDLqIhUOmI_TywUpdnZxtmsl43Bg-SNytBoc8zLkBcX1OZpD_23Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=Bt3QI2GptIsqPZ7kNnRippR2amLHvTqX72DP0kPTNkNHSez6oK2xam-XqMzeg46TyUjSGkcWO4ZD6s8SC4KPp4wVoxWBsHAfN0dI4JI3tpn0z4Ov12Im-o5C9-BMzQK-KRJJTY5WeZnnvyuAHml6tn9asAs9cAyyquNBIQuE7PsM6WC6ZZWlNLHJLW603FEsf0egIcQkFBOUk5gCSjrrzJZr83SOyBGcV4b06Rev7KchnXcH4PFmzhoiBO1eQjgySVFscYtBCkuev6zIrfchIs-98SdyT5bVnuDLqIhUOmI_TywUpdnZxtmsl43Bg-SNytBoc8zLkBcX1OZpD_23Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=VC13qbK-LLq57gW9Kf7sv9eF57uLHWSE9GQZkyZgTxXVFy2K5Mmh-9qw8ta-xwjlVKV4zHN47wt-6jX2prybdk59Vxt7jAVg8RLFdowPAp7-qRCQD8AcKJFwX2ZdX1Q356DfCi_rCpHA6_ZbwZuIUInw1CesTEqyM6jBI8FTCpdzDY2OdDXcF_1aF-eBAeXFlYE7Fx4n4ioVc8HTRW1BmAlfUi2Ha0XwKcxxeeNw3z06c8ngfd5Bc9a8YHYpo9edK1AmDaZ00Bcpt5O0pLuDTdacX00xTJ1v0agRid29Oyxm1WKGFK9rknpd1JvqzlZqNRwc7K-beFmSgOCXk8NPQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=VC13qbK-LLq57gW9Kf7sv9eF57uLHWSE9GQZkyZgTxXVFy2K5Mmh-9qw8ta-xwjlVKV4zHN47wt-6jX2prybdk59Vxt7jAVg8RLFdowPAp7-qRCQD8AcKJFwX2ZdX1Q356DfCi_rCpHA6_ZbwZuIUInw1CesTEqyM6jBI8FTCpdzDY2OdDXcF_1aF-eBAeXFlYE7Fx4n4ioVc8HTRW1BmAlfUi2Ha0XwKcxxeeNw3z06c8ngfd5Bc9a8YHYpo9edK1AmDaZ00Bcpt5O0pLuDTdacX00xTJ1v0agRid29Oyxm1WKGFK9rknpd1JvqzlZqNRwc7K-beFmSgOCXk8NPQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=L0qRSJi5IaPQChmJwhdcQ4FaeQ4moXHIlSSaDA3zhGvp8-9JM6KiOxi35ZOWGYZnDQVabeRvwSWGsmpxYRMIMonc9MyqjaJ7Ggxu4vCU7dd4l_PAHyGPGeIty6Sm2fqknPQ_XCzxc5BG8GMP8NNMiczrQJWmkPq6wjzWVYJ3ENRxc5Z_-rsK-l4dfoSz3wEFDahcTcPZYkuWeKaaZeCTQk9_yzeYvNUCFxJCBN7rTa_BLHTpQ9TVjHSjDkvTNfuWJMEPgW05Nna7c5Asj8oU4sr_qkYq6gy62BuTPCdw_QYVLaxxGsVmB7nMv0h3_Ww78s8qmzpR7oHgMikDfuzndy515ptmDRhhUgDW1x1pB3x4qWjZVEgG-PjLv65KfqLL5nqjLZTKhc7yyrEX65zwbgV05xoQUwazvgp3VNxgsOS06CM-MZkNwK2e5xi3Qkqn7LItAbBdws6e8HS2XpgcPCmEXjKZExk8Q1SqBJD1nqENNq2hoUUPAV-RMpL9OlKWe5jQ2AZtbY4vev_W1Su0hdykLcfZuTxDNFys6yc9G2-m6XG5kxyttd0TNmF5SdyWz_LdId1t4Xc8c4VRXTog3NjgX4jebxpWG-1tXl_PgramwnlL71uuzdE-yRpdIBbtv3Dgm97Nw3FkEGtUXPJYhoXjIC-IjiDDaBqNObkv2Ys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=L0qRSJi5IaPQChmJwhdcQ4FaeQ4moXHIlSSaDA3zhGvp8-9JM6KiOxi35ZOWGYZnDQVabeRvwSWGsmpxYRMIMonc9MyqjaJ7Ggxu4vCU7dd4l_PAHyGPGeIty6Sm2fqknPQ_XCzxc5BG8GMP8NNMiczrQJWmkPq6wjzWVYJ3ENRxc5Z_-rsK-l4dfoSz3wEFDahcTcPZYkuWeKaaZeCTQk9_yzeYvNUCFxJCBN7rTa_BLHTpQ9TVjHSjDkvTNfuWJMEPgW05Nna7c5Asj8oU4sr_qkYq6gy62BuTPCdw_QYVLaxxGsVmB7nMv0h3_Ww78s8qmzpR7oHgMikDfuzndy515ptmDRhhUgDW1x1pB3x4qWjZVEgG-PjLv65KfqLL5nqjLZTKhc7yyrEX65zwbgV05xoQUwazvgp3VNxgsOS06CM-MZkNwK2e5xi3Qkqn7LItAbBdws6e8HS2XpgcPCmEXjKZExk8Q1SqBJD1nqENNq2hoUUPAV-RMpL9OlKWe5jQ2AZtbY4vev_W1Su0hdykLcfZuTxDNFys6yc9G2-m6XG5kxyttd0TNmF5SdyWz_LdId1t4Xc8c4VRXTog3NjgX4jebxpWG-1tXl_PgramwnlL71uuzdE-yRpdIBbtv3Dgm97Nw3FkEGtUXPJYhoXjIC-IjiDDaBqNObkv2Ys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=ZilSLri6N86TkoP6INE5GJ-jQJvRnZduoMNpUS7lZkZ8o20YnHTZppmGHZfRmOEbFNmpRJ-Envse8Naxmg9BpKgnrWWdv3mgWLXszoUK5aPY3a2krGnpBQ3dIlzgXofzocfVjon9TuVCEnWl2ew4xf-UjwwYPk9mWzlE3Hrml8fldELCixZsneVjkBPyd7LFcbFYsyjtJt-TPyrBc2yXIQrHKKfEuDOYirfcSGnCT7s-qk3VOof1bt49hKYfns1XJWvPSrsqDLk7eOC8z3D33CtcDIUGx2UPq50KDTbTSyt807eZ0Jp_sMAEFitqMEcSMlvUZWs8tHe43WI6yj811ZHQ1A_aG6NPx10Ef0BVglih91RMoKwVkZHLOApJKhyc1368kIy5YuUnAmazfIhk5fYEWHylVeSNZsBKvGPLukU_QP1KDYWFjcuQHg9SBF1fNgTmInlJuJqXdfc00F9x03RLLfP8x9m_Fb-Xb_WS1kpV_qj_Lx2kETOD02qAdtEM7wMoDskBKPWV94so9Stswqo7scJ_cDPzckAdOI6XWb9WzB9jixLfLIioIwhkRVQNEpMsfPU6jO7obVEymqHTUbZsWn-qUc0T8QPbTdpSWGy-MNKe5TWcAX46m3cnzVwl1IVmbOi3sMbj9cTJ19RT8sDBrwBXl-rSNAwgAcSbXhM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=ZilSLri6N86TkoP6INE5GJ-jQJvRnZduoMNpUS7lZkZ8o20YnHTZppmGHZfRmOEbFNmpRJ-Envse8Naxmg9BpKgnrWWdv3mgWLXszoUK5aPY3a2krGnpBQ3dIlzgXofzocfVjon9TuVCEnWl2ew4xf-UjwwYPk9mWzlE3Hrml8fldELCixZsneVjkBPyd7LFcbFYsyjtJt-TPyrBc2yXIQrHKKfEuDOYirfcSGnCT7s-qk3VOof1bt49hKYfns1XJWvPSrsqDLk7eOC8z3D33CtcDIUGx2UPq50KDTbTSyt807eZ0Jp_sMAEFitqMEcSMlvUZWs8tHe43WI6yj811ZHQ1A_aG6NPx10Ef0BVglih91RMoKwVkZHLOApJKhyc1368kIy5YuUnAmazfIhk5fYEWHylVeSNZsBKvGPLukU_QP1KDYWFjcuQHg9SBF1fNgTmInlJuJqXdfc00F9x03RLLfP8x9m_Fb-Xb_WS1kpV_qj_Lx2kETOD02qAdtEM7wMoDskBKPWV94so9Stswqo7scJ_cDPzckAdOI6XWb9WzB9jixLfLIioIwhkRVQNEpMsfPU6jO7obVEymqHTUbZsWn-qUc0T8QPbTdpSWGy-MNKe5TWcAX46m3cnzVwl1IVmbOi3sMbj9cTJ19RT8sDBrwBXl-rSNAwgAcSbXhM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=VxPS93UgTfTK5GBOkIgjKIly-uCh7NKrA9lewQ0zvhzPNruFSvQY4xK_3AbkeNWRsrlZUs0AkNDZFhHtqsNMgfQGWCAouLY0XSg6Us6NY0rZvj4sFxZeq2JaLdKLJ8LNpeEcfiNRCAoJrLhC11tBRRMDx4VfLq5lPyQ9xhMHegtQE5vm6kRuQ5vXHuAie8e4G8tEqRNoIpPmWrkJV14kOIG_XMU2N-E8BmPweFqFDh6q6ZqaAYDjTlc-dhTqGit5S-QvekEmY8Yt0Vq5-TV5UUyZRUr2qp789buW0uAJvthXn5lDN1LYh4yvlObtdr75NRO4ujYD7p1p2BRovX1f5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=VxPS93UgTfTK5GBOkIgjKIly-uCh7NKrA9lewQ0zvhzPNruFSvQY4xK_3AbkeNWRsrlZUs0AkNDZFhHtqsNMgfQGWCAouLY0XSg6Us6NY0rZvj4sFxZeq2JaLdKLJ8LNpeEcfiNRCAoJrLhC11tBRRMDx4VfLq5lPyQ9xhMHegtQE5vm6kRuQ5vXHuAie8e4G8tEqRNoIpPmWrkJV14kOIG_XMU2N-E8BmPweFqFDh6q6ZqaAYDjTlc-dhTqGit5S-QvekEmY8Yt0Vq5-TV5UUyZRUr2qp789buW0uAJvthXn5lDN1LYh4yvlObtdr75NRO4ujYD7p1p2BRovX1f5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJOOD6cczKrnI8hIFnoZ3nyUzSAmMb7F1Pv5I28ZWMDz4IyfadmHkAm97cvmECjsi6oAprZP8Ng8-MAD0rzfQBkczRKLzFoI5bHSFnRfirnygiTqJ-itWR-Utz-FUk2x0nSVrj9gR9gXcIp2v8FhEbg70WdO7GNn3jomA-ZgpE2b29eCDcjD66cTZgi_blBY2vvzAJIgHB_k2QswhFHVIBP33J4fr1YyOyFWE7CINc6XBTOoeSnlo48zrflM04so01IEMqk1GuyhtwCkcMIZoEIBX0TJf5PFft6sRhx3Tu3ivwIeGZ9uQ-FLotgvoYs-O9JE3XSa2Qj6wfQUYlBDpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=VIUrWYkKVmr-6zOr-GGhJBRCpo8sqgV_m4QQTR1y1TAQvDkr6tjCNmxqr--r_qr3uFowe1PjDzxVU8APNZ_wI7MimCKiQGsER6h8A2GvyNe0dgBJWbb73_Jlu2JZI_g6WSksa6L2LvXMKGydx3pzbTug5DelnwvWhninaGsrkyDhtzc5VAC2mPK1xJ5LiRnrk1VJHTFBzXGZ_msMGoPR46xAqcRJaiS8dB1gJ-8oIGYIFOsuFhuzaxMbB72nyVfXGSUe4BFD0D3vbFdBDZ45czdH3N668OjebpUhARNu9IJW6z8dDf_kK2oNiUO6uvuwyyzAU2HuRgReq5onKDYNYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=VIUrWYkKVmr-6zOr-GGhJBRCpo8sqgV_m4QQTR1y1TAQvDkr6tjCNmxqr--r_qr3uFowe1PjDzxVU8APNZ_wI7MimCKiQGsER6h8A2GvyNe0dgBJWbb73_Jlu2JZI_g6WSksa6L2LvXMKGydx3pzbTug5DelnwvWhninaGsrkyDhtzc5VAC2mPK1xJ5LiRnrk1VJHTFBzXGZ_msMGoPR46xAqcRJaiS8dB1gJ-8oIGYIFOsuFhuzaxMbB72nyVfXGSUe4BFD0D3vbFdBDZ45czdH3N668OjebpUhARNu9IJW6z8dDf_kK2oNiUO6uvuwyyzAU2HuRgReq5onKDYNYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=IG5h0Efxk_XwMJJJQ5jEMvoHXIhr-jPRwv1g_NIiv_0MHqptq2UBFQ9aos-szA7Y2EzVEN1R5j92sCYQmeTPYZHk3BgAc3Kmp5oTcKTuYrpZmofHfrRN6ZrlNbKCUYYSK--HlQg-zfswQIiGpwdlB5V6arPOHFhxt2MHkCOOvg79eL-3rZ0d5QCHZQFzOmCBCpKxKkwzE_kCYdrAQXrsr68ZlB2iinBGD1CzpXgPi8usv4qiHkFdTxAL8h7sV2ZG8j_K364gmJ2wiP4h0dauAvi4qLpRRD99A7Uog-bk_e9PulUCJMF8_jJd9oAECeQfgHB4mUtbIrrDRuwT1ztpaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=IG5h0Efxk_XwMJJJQ5jEMvoHXIhr-jPRwv1g_NIiv_0MHqptq2UBFQ9aos-szA7Y2EzVEN1R5j92sCYQmeTPYZHk3BgAc3Kmp5oTcKTuYrpZmofHfrRN6ZrlNbKCUYYSK--HlQg-zfswQIiGpwdlB5V6arPOHFhxt2MHkCOOvg79eL-3rZ0d5QCHZQFzOmCBCpKxKkwzE_kCYdrAQXrsr68ZlB2iinBGD1CzpXgPi8usv4qiHkFdTxAL8h7sV2ZG8j_K364gmJ2wiP4h0dauAvi4qLpRRD99A7Uog-bk_e9PulUCJMF8_jJd9oAECeQfgHB4mUtbIrrDRuwT1ztpaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtjO7DCFPqtBMXoJnOaSVuDsf05dUhstm85xT6EDa1NU7mfQ2E8JncJX3NLpnC3G9ZbmkgMDh5o6G7OXRsAH9nE1prWQWzondBb87JtouWE_xGb45L2b-s_bslfaPWr4pZxcqE9BeeS6-j9EjSric3udajblr2fcs-0aBxCb66ALI6mYBtpsCg4n12_fVIvozlVveRrCFDzF04Ek7IZNk5wWa3dtxGWf3WbdRHwGufDvpHaRAzbwDqvUtaKjiDXvKT-Hq4YxxZyXcZzDbAoe1wEuvuEO4iVgp86bqdcEGSbYRnITGI2WNODUYPoYhT82vyXFjhVTsdk2A6t6pBnb9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyIj0fB55uELV9KZJAb26rK4vKqVfPyxrjMaFBz4Plk3DaXM4Kcx7M1RSY-SC2C46EEQzRq-8HvWOxo6G97TT8dAUGC7-2ck2lggeoDM08l_y8kpHMh75a0ehaYi2QX7xPW0g7jnZGCs5U4ZXKbDunA1kfrsoc2ze7du1ANDNqLHkZDRObxBlLe_GykkQpNrx3RMy26XxFkUbRsZzNJ15V9LwhNCllKtIeqCzZ1-loH78o5iqOeS37cPRgE6kumk_rjuhyBhhMSCOWxRg9BuYRzkpON6t-ffq0kBwZxyh0ZwwNnsgetkKm0lCSN5EZqRhTOO_zYKr9RaGmKlUARbzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ya7-n_bpNS6e6xcrb5hWsL3xxhBcfpNe47GPtgQMDQgOu7h8t9NqG5Itv95QHwUaToZHqj5f9GThN2LT9rRlK2fNu6v0SZdm4d9Ohgt7PsXxeok7p5saa1iYUG2BYPcLd1BZEPojkgo8SQOBbqHGpBygMBF0JTLxv6IwKuaLwKijVAYGEsarw-Qy6grt7-ZEyJr0Er6vYFtD22LXr3SwcHMsJraLJze6ge7Mt3kpkYw4_V3YrAaL2ID3uspVOwmxT3CV_OHw9QQPiXH86V3Wf_TpxND7KofqGomskk14lkQ52CvyY9JRxiR346gLq0AT7UiAvOHTTNO1gjiQx8Y2oQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzvGSiujc52zk3bKc_oisBJzjKIj2AVsAUbVKvSqnh_7VZ5eLNMoRtE2p_l_x3RalTg_YL_GeYAT9QfTDYnrNASNprfMr1UmagB-IizlGgaBpcioRNOyrFZcQ4a9eY_mu5QK8V9DyB0zSaBhxrJaQVYbUxv-He_xKwnLrfyVSqhf1ThcZqqhWLtQSXsYWsGbyPVQi5GfOxdpmtrDXUmp4zn1jDN_0nyxX-IMbTxdThUHoJioqmbQ3mhCznGwTeyFFsb5ldK6Ym4hA9K-QACUw-jtbnZO-Enr-k1nqZ9LWeQjNHTBxpbOq7Nimm5ZQqC5MEU1e39q6E_quq5OuroMrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmFcG-g-7htYTbglEkeJYFTnUcrMmC4jzrCEqzBeFLF_tCXwH-lVEizy2oK2auxIgu99mLl9tQ6nAAakdTQKza6MEzoP6uW83Ka747Vhpmflod5OAyau1MF2NPDGhRgnZ3YWqkst0Y-593skd2Ri9UUTFukGCTft7QyS2ItQAet_qIBvNg5VZqXdnNeRauI6bLs2R-c0x3FrFy9cSdYDBmqii4oJFzNtqJxde1a9kvBn24KC4mkXHFcTLzRkmMTUKVX7qA1QN8BuxLHLkl2Dikp20QbT5WsCzYA_bujjb_7aa0iVfcio1_IUKnYgnXXFmUNfQMqqpSCqkh8-YvIvyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGl2ysJ5fYRDUsO2pbAT-KVD1i-x1b5htoJ8BDPnYKb9yETRMxi3aCubBz9hFQKmonxHeQfOSXbQ1tftsPPYngkWCxOxqR5aneo4Vzvgx9Qr1lF-8vueReNNTHFsuV0MN85eUuR_HDaXJbEdJVmy0PQuIyepH2i9DlYZIJUdR-AxqSvk26q_6OsRPBi9-Cm0vwEAf7D3ucwgEdZrSQQ-FTGejlGF9XIiGd5g_TTmy2JxQcdvVgPhBqdGDHcQlnrLR6A-SBEpmV9MFPNF0c7cA7j0UHKNlxHVPzNFLHbRRuqloTRv-N7bpGF8P05ix4wNsLUhgT1okMVDoM6AhpRuGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
