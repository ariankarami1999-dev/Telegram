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
<img src="https://cdn4.telesco.pe/file/vG14YVzSrhzBhgPD288OOqm_opVUcqTL3UapPqGaBgh5NwC6Syw3PCAH_-mk9QxfmVPuVSEDje8J6wp9S-FbBdTpE3RPRhQ7vHdrACELP5nEjc0R3Md0d8_9rx6CwLfXbFbIAU2t1gLa8NHveUZaIRgbgc6JiX5OfJv_P9eV1YkdQNavu_eFoiveEcAO9mQMWKfWgNMbEUt8-PGZEhDCnN9zuS8wY4lAVZrMPdGmg_07TpFsOCXlgrClSrJlkgnFSRADp4A8ZTT1LlVcfVY_5WrbeNV09nepB47-3_e6s7NFzSRbvBaFnAdyjsny6N0Pd_P24hH6-xKkprZzMbKswQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 12:42:35</div>
<hr>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqgPO4L5-cWo13NZXBiUQBBxyPePYMKPdxDLbbZToL7P4p9fdeeJQ0yqZ1OBoFguePcF-p2XAEs2wKFdIsl9blOkNYsougYUSTDgAsgsGFTONxPxJCY1krhACm3pE9DtQqTyuBwrL13miq3QMtb2UUVjLHYdaHuBohZZvRETUMvdjS9C6YLv3kOTT8d9XP5d3oj2cSXTonXn2mk7GFUjeiJWeopji4ZIzmPEUhexUiknAq_8qNCAYJjMR8ySeoRtKmhCsAWWb_ye9H04t3sOaGlna9ykZuXkGaifDDriiSgmae-Izv5rqExGkp8MfzAe4CLeTEHfQCGTsD_eOlTNwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=JS-5voReP6HIBhKhH1SSJIiDFVxv_MIJYc27-er5Blq6HSSkFp_ppaIOuPN04vBzw478Nf2DZY8i4tGLndOGK_RzVE5BuzXlBotRzFfuNK0sA8UNBvHTwZytdMo8Nd-YUXlzIdRd68x9IP3nm7jU-im8U-PC-cwAVg3yOG8raIAJAYe8VxtfxIQl1BJw7GAPjk13BAdlKns9s-QLEZn6P3NSxLJqFneLI2QVosQF3_Q2fVRCM7mz4ygMBQxfy7bA594gRs5vMiAoaV0ZGNOD1A6Nu_9tmW3OUO7hJor_M1pzJQzTQIhhj_7F43LgtRzyp2z8UA1gZCLg1jgJmkTodg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=JS-5voReP6HIBhKhH1SSJIiDFVxv_MIJYc27-er5Blq6HSSkFp_ppaIOuPN04vBzw478Nf2DZY8i4tGLndOGK_RzVE5BuzXlBotRzFfuNK0sA8UNBvHTwZytdMo8Nd-YUXlzIdRd68x9IP3nm7jU-im8U-PC-cwAVg3yOG8raIAJAYe8VxtfxIQl1BJw7GAPjk13BAdlKns9s-QLEZn6P3NSxLJqFneLI2QVosQF3_Q2fVRCM7mz4ygMBQxfy7bA594gRs5vMiAoaV0ZGNOD1A6Nu_9tmW3OUO7hJor_M1pzJQzTQIhhj_7F43LgtRzyp2z8UA1gZCLg1jgJmkTodg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=iKpEveoCZ-2CHdIhIurgC8wRV-jzus4yRW1woM993tQ2t2Iyylxb2S2wAyj3oxFPRsO6cLEPlBrtr3gLUTmNMkW35roWKe3oOT7ZEbqmb8lKKrrY2mgV_lWgMBr1xF4mM2QiE0ZRPzU7bBzI2qcQSVurOJ8XehH_6XXzL5Ks9Qxckbad7Z_YACv2n8uaRf-6JtCvuzxGsHgP5drgjJP6_GW0VYa4XJx362ECGzjGEFkT-jT6Go_CydmYBp0mKzHtdMnQdHueX3g8rtObAObPnU3lDSv-4NkRCDCTCBetuubzZjb-tHZABtbZd-50fodHlK03VrJQWLvpxZC1_2rR4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=iKpEveoCZ-2CHdIhIurgC8wRV-jzus4yRW1woM993tQ2t2Iyylxb2S2wAyj3oxFPRsO6cLEPlBrtr3gLUTmNMkW35roWKe3oOT7ZEbqmb8lKKrrY2mgV_lWgMBr1xF4mM2QiE0ZRPzU7bBzI2qcQSVurOJ8XehH_6XXzL5Ks9Qxckbad7Z_YACv2n8uaRf-6JtCvuzxGsHgP5drgjJP6_GW0VYa4XJx362ECGzjGEFkT-jT6Go_CydmYBp0mKzHtdMnQdHueX3g8rtObAObPnU3lDSv-4NkRCDCTCBetuubzZjb-tHZABtbZd-50fodHlK03VrJQWLvpxZC1_2rR4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQwgQB6MUx0AvbGDorc-79rjQrwJHYO5L2YVPTKQKvKGyayw4wlBIXlIanEw3WGHi4ZwVhE_thfstHPg6Olx5bICucdDUgxEhseKg06V3FnYtYj1O5l-GftaXl3CD2-UyG76i9XKt8Qmq0iazv0sGeE5WQelcbMM3GTDvry7BEwQFA5Yt_mS2LPyKezM0N4YZIAa_8SAjzIbLBl2EbaVHHt2srOuNsKyLF2tuHjFnJCh9zRNv4l8M-_MySV4DoRyqqMQVFlDFHtJf-BSsO2VfcJno2TeEEnJYYa5Qu2irTFqsuMtu2adqi7x1TTB-O1BROejfh6Frmgt-hISHXJ1lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTTn2Jj5KHYC8RLPb7aSDcF7aqG47R2kW2DF3V7v-9m7DaBht_hyBNl9WPUBJf7YyerXh4p2OOb1cN0EVIUoaET879xoy__e6LPKXUA0E25e0ANmOe9TnrDyvpIl9D3AhS2_VtxMmWf7sDb_M5sLOK0jw7NOB9WDd0RRSl9ODLNiFhREAf_CPypjoaPObs7MeN_btAZGc9KO3gn3GQgxNZhHTKVDObS4q9XAAnHMnzyhUdcVVfphlFPuWB8HAYrsZrsCNeGm52Ie-0keLZTspsXtnXK3KUAmMT3zuufxAk7xyrhsfCLd16_6id4FbnjqujrlyWD8wDL6S8lmA0nnfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G70VWaEQBxEcwvi6rMCkkJkWeBJEL-Sea-H_bxf_OaL6VbGpp4fQro_LKrkZa8YgoVrRFkGvP-8yOUQXNV16KJHxP_vt9lexm_oXzl7bHCqq8yBcpUP2DzgTKbSPYHXy0frysoE7i8ZD28QGx2r9uTM_Btq_YpsJjYxxxrq3POQIzPv_g3tBkg9TYFJy_QKztMLTE4ss50teG6qCRolBe8v3-qYpeHE5YU-oTwniFUdTpyzxpAIo5ISJjdoCo0wfXlFkfLtZ12EfFtk5aRrMV_1eDhJtctJEkE1SjQbtvJp3mIfD3WXV1txD-W82lHgK-qRzI1XYcDY9HIX4C1Uzew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5WgF6BaSGs_BCzcut4G7peSBQtKhy2T7mr2EIew1qHcr_ZUW9GxUjb146y2Zyh_6t8V9dBGenU_CePqRNwyZm-rvCaqYlEYHQpW6-pqBHkK5KfV5ETPs2Bjqr1VVsoQE0Bp0eQBL5Oh_zi_w2bUcANp9xAxWz9DzEjLQToJUyepLqKHkq4QnYU2CTUyY41LWJYPzdfsdOntIrJbAq3XO2NPluMfAYbWWaPKwBjlsQeiIksz6uryd6RD97aGU5C0TGxK73Qbw64BH9EYeTYpVtudPf7kiE8f7-lrvzvggaEfApr2_IZvEla2C3GdIeCvylcvzoyrxkr6AjYzDQ3HMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0h3gujJfP6Y1yvTQ9jplx8LCvqNyLo3cMaIzKL2accxpgIlYI2LgbwoBiq15taX-0w1jDeiRE50CSTvwyyI_7yv7CXL8HEDwQ37lBa4dwSWgmNHPyEtoz-U7OBQIbrrkYvZdmOG2reLJ2oLeGnQFoAclY7F6mFey79KrGpSVfCYqooILX3U45Tck6E-zDo3siaG7epYa6sG3hiJkpB3bA5-mcpniDWh5kFPeC6JX8RS3bLgJFTfgiGu2N5MDscx__ILu9NNezDt4qxALNuGedsw6idyvBBHUghi5PhUV3qiQGXoqKXBXGaSQlTaZFHNW3ml7G4IFWbN-ZFbxHQc_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5D2EX_RfuUvWJ1_ChccPPvOEmMYDhCT3sOXUi0Mz5dRdm89WHBYMFFD6Lh-15Hib6za6mDCWOAfcgbp0DkGoH1BnWBKs4UwO-pPc4ET8qH9fwRN3EcOeagiERjnjUct6nE5HDaWxfmmqX9yLQKCd-VIEd4KRFfuwYphDiyyhbYhBIsmOarGsyp4RiLi0Ayl0VvsCDSbyj0cLv17wrjtT5C-lz8YJjmTgHq4yEaovcgclAFaJ5JzfywgxUgDWGS_R7ck4Q4UQvqDSue8_T_h9dUpIkFTdHT9Gubn2HvxYpB9BfsWTKIDTYKUxL_V95GZAFYXqQPXNU8b7HRTFieTMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeemvMPMMWIWyDBUi7nAktagt5iCRKBqTPgsg0YyEWM7HbZWgZbGik9Kc3a9GIBmio_lHNICqCSjeGcNT1zb4seDlOFLgyjIvGFpDRlCwmwWGmyh4u-sa9xq9cEYwylSCJdi5xTAKZKQ18lRW73Apc0SbOnwLL8tDsWbEJgcHrBg4GM5GYUR36fXJny1i0teA2qA-U1HAtISxUZyfSFDD1mpxDlW_BfqZXwCTAA0LOmXIMwZfo8HQt0CSR1Ao9sxqPlh2K9ZJA5ZCzbE5hkvLHDBWeTtulGr5i_39u4CAlB_8o6qDex8I8yWKg71GWBqBZk4XWuydAPmcQ-cLTfpDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZdhZkCNBTA6k1oD5aYLwpDuRF2PWUob1R-m0XUM0V8DJvrWq-HeKi8k3FaufirQMvNqGzWzPmrnnnSZNLcQ7VHqSn9AeuiJYut9P4LJBrJ8o1NRMkIOD3g4NibvcGz-u5DbOBu5CZIk_iaGtxizBubRZ2ot3-0hs4I-180oGLG1bnY1VCCT-uG7OnJ31SmEE7NW12uTiQDzD2xFnR57NgqkE7f2eYtU2DqFCSX3DIRsckYmUnh2jnGH-1rYwya93TSUS0HsJCnno8CNwSM4f4l7-U17f490dwbm9MV-19JTPC27IBL5ev2S_0UMVKQ9kcuQ6WZcgUwJg6BndXGSFag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FuYrJ6cQZ3FM-Hdgrh6uLn8bHMzavtkrVB2JBViAn6A4Ei26PK-IILBdEOn2W88E2GyCb_9gZ-3L7BcOE5k2fY7Qi-1vZKU32a1H2FmiQ3QYtZX9eldBLjOZkHDulag5FauyBsKQ8P-C3onoOaiKaGMMrVBIkcbLgB2FPIVZqp2_48d2UoNC5YMLR0J5sys9fMxCotxnE0GFSKxpPCXgp9zCXoDy_zqK_cSTV2haZ-UzWLUqsbhafTIQfomA-Y4UzYDoYQI7-jVPhsGxQQXFPRf-by7ygsyeiEaKyuipX0-DG6UdJn4_cK8ePynOFJch1tTeZXOs9U1yW4Rs0ft6Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/awpJ5prG1Lgiks_aXG8OZJEpu6HUbPf9yLnQhrcxf5CvUoMj6rOLXm1A94h0WnyMvb5ps-uj8pN2tqNa9cQtdDTu4m6nhoWS713PiBmku5zALlIosa-RsPXAMmOwPqsuQiLE6OT0Y19M9ZZVSDf19oZyEMtM0C4DfhSH02k4vWEgonKsS9jwNlzG9Z7PaKHCtTIVWqrwOw8Zl3RnU91e014L-MGWr9HE9iEsK6KXFfWgNnwQxTaI_obL-_Xs-ny5yoC8sjzSrZn06jWKn_pHR1orv5XtrYe_cYqZnJihMdsSm0pKgo_DrHaQqva0cDqUgdXx_caRLr-3Ibk1JQkoTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=P0T88apSIOauOMXHrYRaIEoKTkHz5yZXoOC9VMxrDeJ90-pASoAgZgV7oJ0TAH8Z7OinXSTcfRpCeTriDKLadLJkpKe2yjfki6ETGaJQACz9CrFHZ4Xj4R6TQfYPOmWae18d0HlrArrkSnNFjNTF0r-5gBiEbm9zGMy9KKkH1xPWZ60_qK855hQu1sAD52WojzFBvpIwgLMI6SRkEh-XNfv7ufxnRIgzQd1QV3Jmox6bL5b3IUfKaKU0uU6B4qI3XH2T1JiTOVUD_guFjd8xgPDa9hRc_sBycaZP1xcEYldMTSrRKtL1KWgqaBPcZeMVFiP5b_lXhlz95aPGjRUIfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=P0T88apSIOauOMXHrYRaIEoKTkHz5yZXoOC9VMxrDeJ90-pASoAgZgV7oJ0TAH8Z7OinXSTcfRpCeTriDKLadLJkpKe2yjfki6ETGaJQACz9CrFHZ4Xj4R6TQfYPOmWae18d0HlrArrkSnNFjNTF0r-5gBiEbm9zGMy9KKkH1xPWZ60_qK855hQu1sAD52WojzFBvpIwgLMI6SRkEh-XNfv7ufxnRIgzQd1QV3Jmox6bL5b3IUfKaKU0uU6B4qI3XH2T1JiTOVUD_guFjd8xgPDa9hRc_sBycaZP1xcEYldMTSrRKtL1KWgqaBPcZeMVFiP5b_lXhlz95aPGjRUIfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7aNcnwlmrmmv1ksyP-SRUGVGcWk6rkz88ki7UJfetGZdOu9-p1Tmo_OSBelOczzxGZAod71T-ZMwftR6DTgEqy2CZ68Wom367LFIQZthVqxdY5trgNaIiE68gqr9qoRUT4MyWYbZPoym2pZxxbVsE-R5B0bnnLjHavgY2XYOTxCQ06VuHxQyEt41qNnc-Kt6a0WJiKdiXxQKScV0xqSI8NWhn8fP4Lh0RzlgzSQQ5QKdFdyspsuPy0U0jRO6QV1vTJORjHRzi2U8miYwZ8ZbkX604Ok4YWvQc5xIV8CzTV6UFkwlaL9DqSieB6G0xW6EpZFbftim96D27yTcxsiXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLks9I0bac_vANF147jwiF-bSoqep5fuW5Q8wpRM22j41yVNrmEAfOz-_f7d1pEKpBG4uWgbIRPRxjlWuXDMZkJ4qmGJLJaX0zMdQAURZNIJNPs9gJl4r-POaGTSZiWi53gv_iOS7ia5gfzD8octePMnqt5aRgBqrJc1EvRtnsq9NpCVXt46Kl7ApbQ2Q0utm0CsDuzDOBOW74_v2purTeu80adnBr6SiK0bnFIff-GhOXh9O8kwIVHY4ezAkn_kQQ0RQMNmn7T9O4eh4UuTEr0aHjxEVqM7QK5FGRN92a0vGJG0YinVmUICtelnsMDaQ8tujHgGhuKPtl0Eohg_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=nd5gpCoPp7oCHzHoxC6l8MkTqXSB7YmTVKS79zSkjBBm0LJ_qgKBbC4ILYH2LRe9DoT2mvkNhlw1fVTrPzyUxiVPru2iQjK14l3aNzAqBdGI4kfrJBHJqLqvvy_UIgwmfFOwlir18NFlxtKG1CmZwahWTs2PZT_pPMx-2IYtfwvUu9VJG7WLMkCR1nsqZYrlEO-SZFyXYNT2MRIATY5_RBPjDHTO54xZphe3YCRZJAdL6b8cPU98v-cuR2NS-SrwZSIeTZhZeWvRwhtEpHKJG_UnYtFxu47X79IYY8CqKN-_BNkim7Xw4cOxg2xPugeGdWCFJAzaF1BIO-0O_0IA1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=nd5gpCoPp7oCHzHoxC6l8MkTqXSB7YmTVKS79zSkjBBm0LJ_qgKBbC4ILYH2LRe9DoT2mvkNhlw1fVTrPzyUxiVPru2iQjK14l3aNzAqBdGI4kfrJBHJqLqvvy_UIgwmfFOwlir18NFlxtKG1CmZwahWTs2PZT_pPMx-2IYtfwvUu9VJG7WLMkCR1nsqZYrlEO-SZFyXYNT2MRIATY5_RBPjDHTO54xZphe3YCRZJAdL6b8cPU98v-cuR2NS-SrwZSIeTZhZeWvRwhtEpHKJG_UnYtFxu47X79IYY8CqKN-_BNkim7Xw4cOxg2xPugeGdWCFJAzaF1BIO-0O_0IA1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=oZqfPukOrzcfu4TPhZ2hgVOi24N2L21aCfOjzLchSamFJe9tgeokNYxfjOhg4yCA0jUQ09-9lqa-bZXEe8fE7XFS-fkrep6sADCy5NVA6uIP_W9nHrl6Q9fJPsoAZu7kDGSwiK_S_4S6qkOQfw6Ddp96UZ0zgNTtUN3Vm-4McUKy5Ozho4b73fpct5vylh7sbYLpXwgZrWL6ScSmzZuzksSkge2kRgS3umWwY5NawcnoXoAfN5nr9E7k1xeQLG0xRIQE2dLz8_bNvtM70fjY6I72bjoV8iO4U6bYrBiQRBjdHzEcfuk22oHkyLLYyIQreF7fm_NcTvSVpklGePYvzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=oZqfPukOrzcfu4TPhZ2hgVOi24N2L21aCfOjzLchSamFJe9tgeokNYxfjOhg4yCA0jUQ09-9lqa-bZXEe8fE7XFS-fkrep6sADCy5NVA6uIP_W9nHrl6Q9fJPsoAZu7kDGSwiK_S_4S6qkOQfw6Ddp96UZ0zgNTtUN3Vm-4McUKy5Ozho4b73fpct5vylh7sbYLpXwgZrWL6ScSmzZuzksSkge2kRgS3umWwY5NawcnoXoAfN5nr9E7k1xeQLG0xRIQE2dLz8_bNvtM70fjY6I72bjoV8iO4U6bYrBiQRBjdHzEcfuk22oHkyLLYyIQreF7fm_NcTvSVpklGePYvzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiljJk7qwxeaYDWBJhgOC-tVqWzo6IriRutKgrqh5GLP_SAo2nnbHGVca88msI-s9KEPuCstYh_XGdSWhCCj6rbzzMvw7SM0rczJfz9hmsd5tJrjQTebFfJXt1MORJ3dUTWmZuYHH6HJPU8Y-dT2bFLjgAV-yxOQIuycXm9W17TWTO1N-GcV6njMBbO_Ay9u_A23ZsSJ6MFJMidXl_uTCxahiRiterxt8RG9RddK5WSSzhYVXK9N58G0ACduZutyWi9vsBWqT4bAuZMEk_vsFJA0f43rEajyGD-AoOHYLMrbKR3aQJdY_4pV465yTaY4Deif4ufarOYsggUfMDr9_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUk92Bw8HBslQMj0X3Aci1oiM7yyCBhT_Ui_ly-8VHBd_67mWqhNSlfNG14gIZf75--WhEeUpdxHTpU7QbQqwztSaM8gbrDTcPimPFeh9sTgW031Di07GA55xosT3M9QWa51y-5w8VUDCqJ13doKchwKtl-SUc3BgQxgA8qc3XSPcM6TnQwgCmWoh09zUDjCq80c0pRzk_d-EDfSrFVsHSlB-Z13VMhU4W3SO59tt_ppEgUrAa5j8OKf6h959iVg_8F9TDoeMMrHTbF_fTCyLMXavvG94EBUiZTk2mya68PdCnHBOoFH7M2fuyoSeN5gavbcW30uEk9WhBDMsq9mpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHeZLSuaIWS33hXlZnG5uwuI0A853TMIaymvPfhQVSQTbK9BRoctmQmZ7YU5xaH1po2RyCNrhUtAHZ0kOGQ_PNbzfK7vkTQPsr3VHhblCAbXxYwWaj8wF42b0SAGiqjw6tromDhQjnf8u0K1zVatdUkB-jmNk7Y6D629B4CkiEtDO9peBe0Mlu0SYEHlfYuz_0zAbLh14pHUaae-9X2LC054aorgCbxnNMGlL8IOVJ67-347TqKcllcrRNRp7Dd3nV9o3VHvAHDNo4es3ii8kPNYf0RZuzl7MRF4yeev5OacHGEqAgAI7HmoK_9vcgybD5UN7edsTp2S_Hdxaw5kLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8RhuXPp3J2LZfCcNMfTW8KNm81RmnHlIDA5LMAJHkWrCwj3n4YWHdDzbR3miY3Hmidk84phcZTzl26_ptDk_J6psRMPoEZfTAskSymMmhdzRwXHliqGKA5nafvb_2SDjF8MBYwJFzdv8a-TY2X3XB9rYd2pHzEZvEWngkpvG3b9L3EYtEfWPU57jbz3v-HGl9kA9Osi6ca3smxmvXrSil0R2Pk6KilViYlzo5RIIQpvTo1sumQkANPuHmX7Q28sxR9Wh5DZm94yrozJDLeGJOc4cy3g9_BAcNXspVx-Uw43YM3D0O-FeTlc3xzJ4J1AQFWwWY_c0188aDxdhBeQBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pj_aAYkF_WMdiI9m23FjQV1ykLOurcxhDLYKIMMZpg6g1_L9ZVz6isOnNs84FVOOMCeY4B-XbkdyFIlrH-TM-pzd4eEN2kzK-ZqaN8l13Iq3Dgw1wBQlpc76qO8im-a3sk4aOvlNdDY_TvhUp9-Rbtryryon1N-gSQSg3E-OHH8sTpMO89hXs63ZQkGeURDEIIzOJVAx_Am-dMrmUAlLcIxgdXXmp2wbexw9HkCDU2aRaFY8_QDOSnE213m7p5Acp_jS_GoY4E5HTK_Q2h4sH5sJ0NYxq93n2oI-kpNjsf4khXweONGXbtPTgkocIVgtc4BXINTEGCtGsB7cyj-B1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgzpPinPXFzbuDpML1xwrOr1UOICxDqA9hdgb_82t4gSkm0UjSjhHea8PNoJMWTbaksdS1HggCFKFaObzlrCuBDS98p2VI-ku05pQlzgi8lDgMzKvJrpeb3INJ5vuoddzUczryl4rci4sKl7x2u7S5bCL9Y0SnthKJG5Zwkk4DWS4UnbQyu4XoWhYMQRg3O5WEXUWMHrqhGUzsrcK3XEt2aeL9xwroYCDE1uWNAZC1l5Q5LpwAD_jBiuBJE1LaDN6LLuMkjFYDGrKn7nEq8s7AHS339fF5J5RmYoQfJxL5llpFD9alOjW2rKGRqPh8NiwltrRP91Iyj8LmXwoc8zdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plcsUJ_ph4qzvc_dNIf8-EdBmAX3p6-8haIn3UDw8SZe2UwIGtKxaDJPyxHL2Xf-i4dRci5meJOCwPOoX6mjYsftkRNYyKP9EMX7FdiPp3qFPF0JGFMg5hEntAWCe-hxrk-xOA3Yr4SQah_3EIda_aR4cNMr1AhAHfRaMuJw5tjyuCOhuhWONgAM6lY9-cAwLYCBUbYFwTdpHvy6h_TQcC4yRaCwygW9l34xIXyGDvlNuVW2wVumNfHjag03BUt9GStCVUVZf9F637DOW3ZtRJFCtGBlZ-jKH68hkN8SOtMDMYrO3lmH4cbpBHt2jl3vPyspTV8sDYQshAGccoM0wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAoIq8kEJUhRJS3YNOxboZDpNTdt_SyomrKb91mN0eRN5eQrwP52PAvOvW33P9XD3L8HpChLP3MBKHbhfVb-MqER8dkAEwys0pnM-28vwVOL_BewMRyGeQWc8OqQNDLtsR_VRN1xtBPccTCr-VT1NEKGbOX3ZGNIXopsC4Y-l1XJZvFoZrwHepvkFVNj4vnOpGhzWZQoxvmw0whAncfDML7ygXvtuRVyqtquU9HHCTS8Tr-8_O0RSOoPgzw6rb5jJBjyqIfD_IJVuwVJ7V6zTR2YbNG2o0Cmo3goJIbFX0q3b6RWUTMpWlN8E8qHLI5omBrURt0Omb19YaBDMqfMvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=HZ3tWKCgrkbN5wHIKkCexK4H-7gkcMnPtjUTf2036qiZeUTiNGsJcbnyyj97UHCG5AGgqbSUOk-h-fLuz2CFwZhoGbFamCmi6NX3flotdTweb1C3z0XsMI9EUZpOTbwd1loQ961rARMLEiohkCDfB5HaSb6KjXSqksZH8g90lvOrBO1iGjP6r106hzXRs8FY1CFNq5E2x-8dCyk1P0t_8pkBoSaZb6os_7t78BgkIZzbZMzauB0EpD1Ds2HJU5JQ3gIxIepiPg2Av2JpoKmBNE7Lw80ZkPrJ_Qd68UUKJ4gg-8zodhtWFFrIFOgnk_6Oxpnw5CMijQaAA7gG0heAqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=HZ3tWKCgrkbN5wHIKkCexK4H-7gkcMnPtjUTf2036qiZeUTiNGsJcbnyyj97UHCG5AGgqbSUOk-h-fLuz2CFwZhoGbFamCmi6NX3flotdTweb1C3z0XsMI9EUZpOTbwd1loQ961rARMLEiohkCDfB5HaSb6KjXSqksZH8g90lvOrBO1iGjP6r106hzXRs8FY1CFNq5E2x-8dCyk1P0t_8pkBoSaZb6os_7t78BgkIZzbZMzauB0EpD1Ds2HJU5JQ3gIxIepiPg2Av2JpoKmBNE7Lw80ZkPrJ_Qd68UUKJ4gg-8zodhtWFFrIFOgnk_6Oxpnw5CMijQaAA7gG0heAqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aw_yucgrj6glIsiimDtqSsEtIy7K-trCLISXylZjIVwtSDoj2sW1kS10oD2NQyOcvcZnjIafot1QOXr85XwcyfYc0LmGrFtTwh57KlGGHzh3_uIlJxWcFRZTLG9PYs2dKuJCLy76nrpv8j1gewZzPLB13ZemfqvDzmU2nKMZomyVIuc6WHr-cLvICxQ9Pbj3xSx-nz-ykgbndLKQTa-huGkZZ-TrEGDDbSC_fkJ2WeyrlZJQQyw9bXHhlwO3fqDv8X-LIP_qfR0jBiUlzZmCPh02aSCiDt34VOPK_9uLXgCS9qwXAVYCuSd0CuuV7lo7rrWostsAF8PG2MkhPa6H0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=VkVcWPPvwbpEuS1Wmwf4qJ46Uo6rX9tvJfMbxVIXVUJZU6rrPmrDjliZIkH05g4l72VrPYk83VSTydvipC4D22vGUq6CLKwOc02YoR2EmtFAFmnq3jwYJTwMimqvswNnOyV_onLiKIlZrCt8IsA3HND-8Ye3BOv5NF1e8Az_JfO5RyDpKPfxhA_bzhu_lCtwnG2QwUPELwCJVgM5jEEcfLagGkVqRi9BG1-i-DYODl4QFXcFYmbPUp1GC5aKexi-l_b79cgQQlBTlN52fDgcVKbxraGmBaCWQoPEE1zm6CYsTKQBph_FI2ErRFJ-g49JsY08DC1ObSvwK8t3WLOOtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=VkVcWPPvwbpEuS1Wmwf4qJ46Uo6rX9tvJfMbxVIXVUJZU6rrPmrDjliZIkH05g4l72VrPYk83VSTydvipC4D22vGUq6CLKwOc02YoR2EmtFAFmnq3jwYJTwMimqvswNnOyV_onLiKIlZrCt8IsA3HND-8Ye3BOv5NF1e8Az_JfO5RyDpKPfxhA_bzhu_lCtwnG2QwUPELwCJVgM5jEEcfLagGkVqRi9BG1-i-DYODl4QFXcFYmbPUp1GC5aKexi-l_b79cgQQlBTlN52fDgcVKbxraGmBaCWQoPEE1zm6CYsTKQBph_FI2ErRFJ-g49JsY08DC1ObSvwK8t3WLOOtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=Z2vC8kFhMXqgYxXW8-ycw3qW8CPvUpohE4YILXK75wHiBYG0-nMFUpRozQpLtxR23V5ujVbYZeI7kpyh1q-m5goLTusKdstkXMw20Xj2HJcMjt7xGy2MIkIs-27P19IAjXfbA1wJK05rJCA0J-dQQkGuLq4QStQRP6nFPhrRJypetpAnlL4_lz4hPxBIqeN9yX-adzxXAdX9aFhaHtg2-uc-87j6IcY0vUYlwr6sL_7eYGN69j2q5US85tK20yOeuXxUIlxN4KEgDDvIzjXx1HgvOQEhvsXsE4gCGHQG7oQh8ZcDip2G1uNANRvch3Ccy0owCavzTI6kJ5IxVwoVuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=Z2vC8kFhMXqgYxXW8-ycw3qW8CPvUpohE4YILXK75wHiBYG0-nMFUpRozQpLtxR23V5ujVbYZeI7kpyh1q-m5goLTusKdstkXMw20Xj2HJcMjt7xGy2MIkIs-27P19IAjXfbA1wJK05rJCA0J-dQQkGuLq4QStQRP6nFPhrRJypetpAnlL4_lz4hPxBIqeN9yX-adzxXAdX9aFhaHtg2-uc-87j6IcY0vUYlwr6sL_7eYGN69j2q5US85tK20yOeuXxUIlxN4KEgDDvIzjXx1HgvOQEhvsXsE4gCGHQG7oQh8ZcDip2G1uNANRvch3Ccy0owCavzTI6kJ5IxVwoVuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFYGh1rFGCSCjQ_-H3y9CzzXpbn6744_WfVyyYfBEclJB88UMbLc02bOaEGleDD93wdCL1efyVTaq49m_vAzXe5M6q3Vk-5CFwPr982aJ-HOqYEjbgqnsq1_1dbu6xZ5XqfKLqswoTsRf-6bIUMAAuE8HFISNwSTH6gIDnSvHAOPxkciTAYKGyvEYwn_BG0Mk_9VVhrfhowObyNOoM70z7utntxM_mNHRNWWWsVyy_Vd6WPCibSeBBGW0wwUW02Hf3sxkmuV9plB8wkT12DkqELsVWKXG9NG8NBMc_GFJV5_vfGl0dPYlVAC5tAp8cmx4Fxd22Vl0IEec_VXaAc19Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBguVncr5utixX9P3rtK0cDdOSe-5LRqWUVDKZViHOXuyT9AcqDWuGwv5yIaT_L_Bnui4R6OR4TFJ7Pk6EE1F2OlNgoKowVTRehDgRFZXssAkPbQGqOdqy5UHCejGHwNu7e6pehEhUO-B6tsnET5BPHs8oDwB_p9ghhZYRJmDC_iObgQN64qD0VXlA08JLzW6Pu2kAVZuRkd2QwPmldYqZQTGjNhExQ_g183gGZ9njBzdZL3SorhJEc5O5P8lR2T4auDMW7M_79g-ME-5leIrpb4wQ7ymRVpAjlTGGyGkilTdJQI6h2uftRFS4UwV5iITu9xL2LSwtseJSvzU91f6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با افتخار می‌گفت ما مشت
و سنگ فلسطینی‌ها رو به موشک تبدیل کردیم!
همون موشک‌ها و ۷ اکتبر،
قدس رو که آزاد نکرد هیچ!
غزه رو که نابود کرد هیچ!
مخفیگاه حسن نصرالا رو که تبدیل به یک چاه
با عمق ۱۰۰ متری کرد هیچ!
بیت رهبری رو که شخم زد هیچ!
رهبر فعلی ج‌ا رو که از ترس جان
به غیبت کبری فرستاد هیچ!
حالا بادبادک هم نمی‌تونن دستشون بگیرن!
اینها همه پیروزی‌‌ان!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
اسکات بسنت، وزیر خزانه‌داری آمریکا :
‏
🔺
امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است.
کشورهایی که به ایران متصل بمانند، باید انتظار انزوای مشترک با این حکومت رو به زوال را داشته باشند.
‏
🔺
خطاب به رهبران جهان می‌گویم؛ امروز زمان انتخاب است، یا آمریکا و یا جمهوری اسلامی.
‏
🔺
هر کشوری که با ایران تجارت کند، خود نیز منزوی خواهد شد. هر کسی که تصمیم بگیرد با ما همکاری کند، سود خواهد برد.
‏
🔺
به عنوان مثال تمام شعب بانک «ملی» باید تعطیل شوند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=jX9cFRy2BeUE1uhPJugRGU4twlf6WWnVIYfJNlKflpqNMcY0BCyFZ3TvV6XvuFZbB8KjpV-Oku00d1YGp5AP5edVMQWlIMszqnpdUHpN7WK_gcuEDHgI61jn5GrIOCbcFdNBhGhTHgFmqukpBVDHPONxTVaT9EOT6i8DQt1EsFuNcrKBhnzZhQraSrku00PH1H-PKx730y9yrg5IExrT7omIs1-B0e5Y0RrzlSejwI3GfvWeJTv1Jly1e8q_dB3SqGCQpwJPmBM2AfGE31TyyHDgvbzDxbahWj_Tdy6w8ITUKVf91rp0R3IyYyCo9DEg7r1ZJ-y0fqLILOPhAKKPT3ulCy8rwymoG0J2tPZfJ22ux2Jq_nrZNs7Y9lbaLaE3KfXNc523Kw6C7DIw1dclBB_6zN-VnLaCHrxcJ_G1OlnvTCcPHBWaEe3ji0dRcPCbYlqVJ2PKPtjXC81HqcwThOte8V0wGUK3BviHpkS6xcghqhxsWog4DA9iFCu2K2tkEg6EoEqsnSsX-G5Dzq6eBXqWz7SpOjeERtjrrINDfpvXXHr40_GA2ZGw50NwswlIDPFRaWhzJdCxgkNKYS4YyS-ELxa0DFiHF7zY5vmpVpe4fqUPklq7jT6NPBwPKX_X7_J0GCdxS5ewD9B-dDPrvF7coOs-37g_yl9WHlnadcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=jX9cFRy2BeUE1uhPJugRGU4twlf6WWnVIYfJNlKflpqNMcY0BCyFZ3TvV6XvuFZbB8KjpV-Oku00d1YGp5AP5edVMQWlIMszqnpdUHpN7WK_gcuEDHgI61jn5GrIOCbcFdNBhGhTHgFmqukpBVDHPONxTVaT9EOT6i8DQt1EsFuNcrKBhnzZhQraSrku00PH1H-PKx730y9yrg5IExrT7omIs1-B0e5Y0RrzlSejwI3GfvWeJTv1Jly1e8q_dB3SqGCQpwJPmBM2AfGE31TyyHDgvbzDxbahWj_Tdy6w8ITUKVf91rp0R3IyYyCo9DEg7r1ZJ-y0fqLILOPhAKKPT3ulCy8rwymoG0J2tPZfJ22ux2Jq_nrZNs7Y9lbaLaE3KfXNc523Kw6C7DIw1dclBB_6zN-VnLaCHrxcJ_G1OlnvTCcPHBWaEe3ji0dRcPCbYlqVJ2PKPtjXC81HqcwThOte8V0wGUK3BviHpkS6xcghqhxsWog4DA9iFCu2K2tkEg6EoEqsnSsX-G5Dzq6eBXqWz7SpOjeERtjrrINDfpvXXHr40_GA2ZGw50NwswlIDPFRaWhzJdCxgkNKYS4YyS-ELxa0DFiHF7zY5vmpVpe4fqUPklq7jT6NPBwPKX_X7_J0GCdxS5ewD9B-dDPrvF7coOs-37g_yl9WHlnadcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRN1XF1AVocCA0IiIcHcWfWmJkUcg2wUKPl4D3YKbgJ2TwePCqQ-_NnwkYjY4LVxjDG-FaunyMn0zTifHPMvI1xapgnjDKdsEL3XdB3Xh1XMhxItZOLIxkHxHTNxy7mQ9ymrJFcfeo_eOmP5xSgFN9NJUD9FaH770GsQfvSIk1u76QgkDJSMpVk9uJWRK2F1Vy8u6hA2q8kVGctLAutkDbD20_rpxtrGvDdbyOjy040oORYm23nSP4zB8ImwZxTGrBaTwfTmiXBBioPB46cnuHmDOCdqyZu-wyMqo63KoOLSqwRptO-rpvVaj0rZxeBHpSzgJYAojOOf-rbOJbZVhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=oCxykbvJAMpVBnmbEo-KwG05tDRNcQXCCWUBNeYtvmSiHZ5RtFG7AtMG7dxUGm1IDJEAQpNi8YStXJ9fTw_zYSuN1Q1IkKUD1pproGsca_Mkq_ORXLMNta7qXgHr9MpanXetycc34Ig1qo-K1pOKTnoQQTtRdfmr0gMVp1gEdmchqymdaUC-qQOkmBdENjU3cg32FE0o6e4_MuiTsTGyJhXhdMX4-8b8iRFPChOA018a8AvqndOujrx1-VIMJh30wNImzu0ZrKKbXIX2hBbisD_vTzb6D-j_x0fLKTdgGHu0lMkjAn-BzPBajKqE4tN2gCA_MID6WE-f5xoRB7r_oqB3tUIGp8vqZoUM-bcJpsyJSNCeHXArjiOqL2GkUrmxE_mDf1wwfz0lkIBR-0XtnPvAUGnxcZVVvH254pqXDFuClnssNo4PNx-Igve_Jf8YZMTVK7OENsNzOyjPWrgujOrBmmlhXYNyCJvlaDrV0RX1IvewgZhHyxUShTWcLj4ZCmqrVNsuzor-U7mokVGd7iXZGO5asF2IWg6dRfzEXfCH4G7nGyTN6AsiJPbPLPo5ZGZLEvb9xoYf6P7q8ai9FFO_mK642aqY4MlLnqz7PDpsp5IQRMT9LbBmgIV0sRNGHfHGtIiJfeduduzckPJKjMgF39_CgF6RN_SX_fvOSBY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=oCxykbvJAMpVBnmbEo-KwG05tDRNcQXCCWUBNeYtvmSiHZ5RtFG7AtMG7dxUGm1IDJEAQpNi8YStXJ9fTw_zYSuN1Q1IkKUD1pproGsca_Mkq_ORXLMNta7qXgHr9MpanXetycc34Ig1qo-K1pOKTnoQQTtRdfmr0gMVp1gEdmchqymdaUC-qQOkmBdENjU3cg32FE0o6e4_MuiTsTGyJhXhdMX4-8b8iRFPChOA018a8AvqndOujrx1-VIMJh30wNImzu0ZrKKbXIX2hBbisD_vTzb6D-j_x0fLKTdgGHu0lMkjAn-BzPBajKqE4tN2gCA_MID6WE-f5xoRB7r_oqB3tUIGp8vqZoUM-bcJpsyJSNCeHXArjiOqL2GkUrmxE_mDf1wwfz0lkIBR-0XtnPvAUGnxcZVVvH254pqXDFuClnssNo4PNx-Igve_Jf8YZMTVK7OENsNzOyjPWrgujOrBmmlhXYNyCJvlaDrV0RX1IvewgZhHyxUShTWcLj4ZCmqrVNsuzor-U7mokVGd7iXZGO5asF2IWg6dRfzEXfCH4G7nGyTN6AsiJPbPLPo5ZGZLEvb9xoYf6P7q8ai9FFO_mK642aqY4MlLnqz7PDpsp5IQRMT9LbBmgIV0sRNGHfHGtIiJfeduduzckPJKjMgF39_CgF6RN_SX_fvOSBY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUHevFSUAjHF6ZtWgJ_IKwvJHm-z9M3aW6UmMCkBFENX9RILKMY_KvF7sJtXmpEBP71ZNudizg8OSKGoc0cm2XWqyzG9KmV41f2Yoqf-e1wgPqA7o76CqVCw1RemTgA-bpoZRVqYgRzF-Utkt8C11whsQLY6e5hgzgzCSUu90wsiSx0Nfd64ir9sdfJjD8CCpLOy18LvdblfF8LoO-7jow597DjDNA2dDWVIKc0bbsHEOR1JfuBSigx0BKbfkDIF2mMoVLS3ZnCJEmia1q9JxRQOY8zTJByNeqpkdpiUIU3yS-QN6-nD8lbMEJLKbprF_eNMwSp2aFs_1dg8pITMyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoBICl6jcyipKpCjRHj0VBLPmlM3lZsWqK_q0TY46y2kDHiNKy150J1XTKwev4qDcqEp8eSV1CHsa56zyvnnD0I3LUpHWBfAgQJnQum3ac8uWM05ng91Zh0vARNzMUY_ndTlxUHrqv3K_gfea5ziEr5sdSKaxWrSk9ygqDZW0OhzLud0rTAhFKmY4esVe_hNgnTx6oGtznhnj2Pp8JB2G6Enx7YK6NEu43bo07BkyfQidNTTu-oEF4eTsgYqJ3wOCUcteOZXSA6RTpC-tgFFabuEiUZDueTmhvCmRb7yPDLhQtmRxc207V9ur_yadFM6c1cRyzJjZcKqSKCexbceAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2Q4gzxYahoNP8CjNSr2vyCGsZ3tp4DLoJtlwY-0VsJ_6NjmFjKcKvQw8U6USB-jSI9icJ7uFUh4ieGuzyw5dHVJ29AiVp1kDzMeo_TeSev3CwDGeWB167Ihyy93jh-TGaSEDWu81EDu8-peo2CG_bHnzl8QdXzhCGI8uZtT1lR52tYx_DtuC3qHmnbOD3qfZGaY7HM3aP-j_yPhUbDIsjtQP1G8VEzcObyfk1q9tZ7FeioeI8VL_eo3OH_uYx93hkWw3wTWH89LsKAoiQ8tn_O78snoXymM2jzQOtXu3HwBFTaJ31KiyBrNT7-E-vMYmjEiFbSJQlhZyPmozIwArw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCPb1GQYNFTzQHlVr4isPFk5tvjfbNoWtmz_bk12XM-paYAxcLSiH7Xo_qc5fQbJb5fyxJ-KTacknxPFM_5xbWMJFhxN3SSI-TLI_of3LdnhZnO7_ZqhjPCGDgoQ71f51Avndz9auqu_iqqUn1Y36480BXGzfCkQzckP_xqI43tMiMfk3dSFN7MwL6BC2Ymhgpk5rAQ2GoC0oCCGti4W4Wih_8u8M_M7Tdbpg1W8tOWBJecaMzqW5rjqs2NvhdJcE4DAeYeG9cVptYVPuH-daVYKmzwOxkSGF05PHKODnoJ0Gl0HG_voQrMxYVJ3D9IOHTjKixZ3bA4wsQwfWQqdHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1kXjFp_HIL90COppNB8w2KhAEWrZar87ag6wdGqI22p-_pNAZzS_LLCfxJoYXaw39VN7TF3ywJX2TXEa-pCJyxGwSUq0Ij5gH4CNqFFX5L93gYTZwWRiOcSetG-u9VJMFWkIaXl7LqlcRGOFJ9Ujg0NQXWqDhraE3DSRihskbN_-L_OZkhVpyZPiNFTr6C8lyM9LyFtDdMo1ZIR8R9e9zuYmz_HsHVCjV5SdaZuuMpwM-lNmbd0h5TUwy744tqeJJD2A0ZTzBU0IpWqXREhmCfxg8B370IJ-V0-kHXO6cJQwBr6BqHVzAviB3tva8ISlR8pFqE2Xr9TclhdJcj-og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omloNAI4d6NQbKLM1UIeMuNaVSevzIKiqyXceUr1ckllWNO-5imgWuqYM8ixhyG9amDlZ1hGJqkrgwhuPRDfj5ZFZvpaAiMxbXk4BkbgXH9TBgQpywXjYfHonYKXUAduOFY7mkrbgS2zcKObH4lcssIU46DR2MP4hAoRya7z7rbJ33Y8Wwioyb9dhHqnDywVKFsoF1YOA4DGehb30UoB1cOyQiU_ewnaDvQ8TTV1x7VYIRUZsP38yuamVYC4Bx26JyPdXeXjQYPwXkhx1Sat0A9IE_y96W7ZU4bfSTq0QW1pYuZnGrgR8zcZDk8KN87Xzny3pEmdv3u9Y8RsRwVbUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1ATkWlbY802WSQuOYRmsopAZefDLIYF93p0qIye4Va1-wmh0LK4W8YJT7d0v75AG3fnf4a1f4ppND1rzuSLDSscxQoQcU3fkcYnvmRYzrISd0e9YRe4z0c5qc0S0kjTVX6CazG7Z1ctqyBXfoW7aQAPw46hLqSeFRd1jzF91utVuPox2qUVJlwxenuA-2nKdPGghZdaTIX-4L5n9c4yhmYj7_EyznwEkS1F6Xa8_AhFUglXsm-BYoed2CIIsSNglTh9CP1rp_oRUvQIXazLYtFMsPWd7llCicWggucxe1Ki2K5ogrQIYmHkCwuWClW_y4QsPtawzgbb73K7NHLoOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/in62U_ug2J5yxgoV4URtkRrwLdRLvmpOond6mZes-YTfjgjkfPhEF1w8DTfkKVbVXGl6Y7VMUGT46mlDoO7D39Ft9t_ocL97ICYljt9psawdLhXHnVeWq38xO7_nm2P43uf8dstHvI7peACuh4_H_DakcZaOEpgRHjDz5ROhz1X-JYYGP7P1FU7fkPyQaZ-WwxdN-7kunBK3l1Zow_XeR41XsatlOZqaOfF8N7H2QfAYZeUL7pD5mB0YvC5-_GQ10Z9uH8XOxp5xq9r_bhyfvWdkMmHlH34PmCrjU2cY6dlV2DeKrRmIrrPNYUD7AOGuHDia4Q_Opyzp4KPwNjZWDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aB0-dt4B01COmryZ_HDgAbD9xUAcDVijuznc5N2ML3uCOWSM5wAnSMtpjZKWUSSAZGO5jWubCisOMPdyxIg52wFFf6jlBpU2C0N9keEQCAiTcYz9Zv4ubn7LpuRqJwq0X5iEU-8HBsNT8L3gctc15eO7GdAcgDq684yLQskz-gVxNhvRsj753oAmtnEWx72V7j2032yvJWZqMDylUkmAWtz37JoTShpmUbYqm-Nxx79mNgfncTeXg8JEFZbTDlsw2jKwBGSsc8XRLdCffpnEXKTJXUqi57B3TCFZlrkx-4re7do4gnpl16KE7krvVd1NzOlzGoFcKqf9WKBLBWxqmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qF8s3U6QaihYI3gKOQBvknhpyz8hm_4k7zAy_N3ES6xGKSonfFXD1a6lFLuRLYNgWeVc9bctznxgNRBfpYtv0UByV0U_MIHcyGDMKU9RfTQX06Wp3InjAosRPSq49ITMS_koDF25wNDKc0o7tArftQEGqgcuiDyQcE-XYG842dTXvFIWXUq4NY33ySee1LusT0jdL0jJl48xqnsl0WgV3_vZHp1Ppi9A8KNyJb_n3exOVGIzRhotZwA-HkRFsg-blI0iUm8rYzwVuGBfji7YfTFHBeRdrX6DeeVFhIuGLxHpYoMLprpreA8JwAHHTEQ3VDpsBlp5RfVLnux8cf0KuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4ZdquMAk7Sw9qdJHuYoTHVAzBfzXvd347VKU8avlpquwK9AUrwJSIY1bF6ZOcmDHouOGrdSqqq2pmOiDHRfAm2yQLIH8Pd2pP7LYQpJlDydGEEu6_X5ZNDOgsw6iz-Ub4uFnXjlvnGXGGBA7OjZqNkLjUQAkRD9k1kOTH2pr4ap_U0bjUbB2ge_H9xDIY9ngDppTbhMbd7Nr9VljoINWrvlqAhQ7G0sLIiMdL5Ew9gbeRG90FOyejavoiJtpPHI1xa8DWf0Gys5Layq8XPqvkN1TGKFVMH2TtTb3agvFRcH9Y9eo3BuxOKrCpD67dLKsAQxDriWR9V0Kyy572CsJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ip4wVjHlC3ER7B9YyhuUReonvp78tJJZykTzUXBZMtRFu_JposnNw8Yst68tohxbPL_VudrZ35rD5A4RizjyhFl8P-j-Q3Pli0DPp0Fi_cK9m7U91Uxemqxcjf_ZmtOnQUlq5YkfjPnL_qTkDCDyzUkCBRff5yLOpZCM7uIcG5Rm-7CsaD7gpzErXHlaojpHyGWru1urqrjUDYKycQ0w99OGv16PluALkKQOQx1OXlapCHdeUA5-O5bHhIicf6wX9DmXsOiG0lbx1eEAfKmxqa1qX-vk7OaIV-EX9Pz2Zxox8wWc6n0z1xnLb7YecoN1S0n-qks3Vasx9p1RHDsehw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LukcyQ53lItAREs7qQNsf8BrPhhtGioS3GocbY2_XMgpm_t0eCHxGLCR-zPPVuEBkkOJ0XyHiJvTXhz0-TXQL13rtLAc7j_3HsT23az3kX8euO6O3PeClaMivxNlsYO8KVUE66oaO0Sy0O6p4XXg_jwQIR61o_6YGOG4EfaM76aDOHd-aK3R4gY_sHaXtD4Yt1DQYa9PCSxaQXzEhZ_q_aqwtBJV2dZMGIhIDbEYDTpXr1nMDKYeCfRAYNfVlmlp4SBFb9yYMteuxswO7806rnrOAKJswxTmjsiWA980roQWkeptceMYBUNLk9bgVu_zAZn7x5-JF-5FX37y-pcb9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iN8ibuOiyVYLKheBfeQbzsCF4PPQwXnDqGlcTVouSFnxnyKN-4CUfkHP5FgVsd0aOP-gHlveAE95Ih1FfxBd35UCkwWP_-mE8K7AfZQNoO8M9ffhHWd8xuR876i3ozWPDTooRvke6QUhEd62YCxQYrCmZ4hPgOeKp4iI6hwkJAOc3OK_F2zcNCR1BWbkm7rZgAainnKSswwQ9mYYO8mNDMdcvpThQIi5W2hxTk9_pr8Ik1U3ZZ_zI1HPiZ5w4W-bUhq5i3fteSrwrvEyYVsp2sSpdy-oBKgdcx_h1zJkocRRcjShCftrWRg6yRQrnK5fAQ4X6QaIjOdW__oxfVdt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند
«مصدق علیه دیکتاتوری شاه بود
و شاه علیه او کودتا کرد.»
ولی یه سوال! قبل از اینکه شاه حکم
عزل مصدق رو صادر کنه،
چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند
و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟
بله! یکی از آنها «حسین مکی» بود!
او نماینده ویژه مصدق در خلع ید انگلیس
در صنعت نفت ایران بود! به او «مرد پولادین» دولت مصدق می‌گفتند
به او «سردار ملی» می‌گفتند!
او دست راست مصدق بود! او مسئول اجرایی  ملی کردن صنعت نفت بود!
اما علیه مصدق شد! چرا؟؟ چه شد؟؟</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJmUu8z5FvH34xaMmKYTYVgcWpM7hWs_yK4CqbPo2prO1HCRKVbVjqN4-1ttf9iu4CIwgRRPssq8ukh8-pvf365xHOGxhkcvbRNVQLhyFvFvBdMcVItxEdXtOcRSBeWKUSZoQRtoNEVbeI3LBEZK2JiMXaNSEwGtU_ZBXiHr2qpKHuRoK3EmEcEod57TDkee4g8F0Evwb5RgSrxd8TTZ5-abdT1eD8mnUVQnQUmAJmj_EuaM9Xz7lHZF3_uj-tKs9f-gNiyWUBlk8lHVHDPHbOo9ZlXCZ88-lBDot0fM1J9zcg3EOmBY110HVPITP78TQneaKFBw_9yhUZQPdn-gqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVvWlFXYLrfn5a40EIIBIeanJ1Ty-rdqkUKEsZ0C_tHdEMUVdJPs667orFKSwhJGHuehjD0OopGVwbkQeVLhnK7xoaeuW7A4nD5EmuPiLhOcM2Owjo7hB0hVVJZ4U8dVnE9tD6hc_o65GyJcW4-XAazYFVlnNn-aX6U6gncvJwrOpOsPUJTSGT58X4VvckynY70cVbp9FNI4J-uTh6kJ5VThabNeyeVTg54ETU6hEznRXgJUgeWb6X3jKWHyVLyvU4xZwnYfPLiWalasXdo23nMFgw3Dz1F8uNJH4gVeOvu68uSL1tT76ZpxJaKCwZhepqjdf7726N6vn5SG4zdSlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3F8lZPGfsV9AefZyDvdT9a5LiOL7z1_acJt1MH6NpHWKRpkRYYsx9v4wRsUicFeiFDRSH9HwGDX-MLGyEMMbwEL8oPcobS1GFnBHhmRx1ZtzMxAEPgGS0Aecd_VrSv5zgmeocrprZV-GoprQnc0LYLZ-KImQY7d80ZyxnRYcMd7vXMK9jfgxjtIH6Dnbxxz_8ERB3BYY0UZ9L8D1ztneBB6ip_Qz9YmgKZKKonCIZ2Pn3tcalCQAlcacu0bpFqRmSiEtjRpl83nB_gtnlfOrlLh5HsnG5wMaVD7fnou146KcOkAvD18rRe34QjtJSVzdNyDm1socGITPT1LCYR9VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KJZ8RGRYipKRAd7DSa_x_lHvBlqsilMMdZKD6rOScsawB1EJBbYD3ATGAnLKRQNyg2Pl1IU9nlxZotdyx7AJC-sEf8zWkKvqf0dyjy9xCjy8ocl7I2VpIWdW1oCxwc59cHfH3xKmWCAF04J_hL3awWzqoJ1q4KheiwVcVHMRuz15aHKYcepn5yXZwoN1a0HKmRfMl_UM8cVeWKTbdMn5-USyKceLzao8mNRiAPi_h_EcIGMV0maaOLnDghL9dNmXOBXSuEdpNmTE4VwLbDt7PZAtGfCZpALnC7umtwMnwr2i2kns0vKsVltRjwymFBOjZ2b9slPOFnBvpf8dEq08ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFpMfpGBPfyjWT5hwndGZY7eRohYy_zhHflFimXL6-Hjw3lPwcgwWrsJIaIfKAptrY4gyaMpAYJqVBupBAjPq5OYy14KJauPyFNwcp1v6a8mD-QjxiTwofs-poeLJZpB7fC5zH9fLOAVzfXgd9rUH3jKeWlcmQjCooHsK9yMOv3OEBjTbO4JEpYdzZ8qK4V5Z8spU3hkah-orGOA1KyBnNVDPcOlhcyTKQT5bU022GqlJmPqTlPJODs5ZfJHRyWt06VryJhHqoJBCbt-18gs3nPQ5Xs_-YzLFFItt9nAubHgOfUmqXLYEMdoxGx46uJDLR7xEyQixD4Cw34yQrMPSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0Fr-5bfinZO_city7FoUat1AAJYwOCt5P1b5XjESmdFoSgwMFyGuKWVqbO84J6ePJg_UL6bsQstr0v9Sf-CSlifOCJ9ajtxNa22Hl6zubH6uXBB-y5LU0OGlac5D_F7zBu22F1loo86Box1OA9lBCIPi5i_tKy4XQoHWJVNpY_VnSqkHpFa9icFaE8uGX2sNn98-8zww0Gvknfqy11PEsEhaCZSBu5XWkNPmU9JzFoVNP0NwJ0FHCQIPfxy9S3ywpzPZydPZD-r3fPN06Lvg3XrF9sDl2iEu0UCZ7MJkmU8YHa_ltUPnxPAV0GdWbTBvgWBws1SixJn02DCeUxA0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSfSPYNmicbfldsOGDF4h9Vu8Aw8dP1vhh_TVqgE0_a4CUug19orcB0s9haXfl6c_pV30fC0xcTq1dRt_CLLKpIzKmG0k_VORQ1fCv2vnxcfvhzjHKSgHDmCN8CsZXUnYc7l5KgvJs5jCgVpYoKtiA8x_djArEuZ57SL50dWSIlpFqt_I2iXD6raw6TOmRaCFZYD28_mg4fFomL8vYvvIZt3uUsUsIXFw5IeukQqGEkT6N1RkAfv-v-ZaLBArHhUwHQEPx8B1NDReeetuORZ_me5yNWXZ5OZtXq3n9A2__cjDycpgUzCahZpiBSAkPa8mNg1Rp03Iccg09CRxFI6fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEJ7p12NZyT1DcfBuOdC_B5NiRFg_8JhVe_4ebZP7WyubCJFkJ2ABiVjJJccV6BBgg1vHsdcQcgk61-icmmx38h2hDswbr8OmT5VvDsS3_GjDBnDxkvrqzsqwcswc92dr12dcp6_uvRxmiJ0MdeLuqQwgwyzd4aIM7-2lZAIGiPtrvpWK4e446OSc1yy0uexUjZ1xa1J96WzFlMXYbW2joABbj6w-wrwlCyqGIVGbjvOa5pQcx_AQaiYm1WupgRBIaPXAH-DeASsr-ZAmr0SwWC8piwplZ6mk1cKVqGaEhj_VpDrP2p3LF5CZ6jdFudUYQPiwMXk0Fkd2XYaBfR8YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8Ehl2d1QJ_X_BlkFW2IacXoR_bcj5eeSYOg5AI140PTO_wlzinzxpkcHD0tNDK3MG5ve3-hY5w9U2CvuSFwvxHUnMUGNuU3diQbyTOSoqXutEAoOPBT_mqvXWe3p01YRCsLHY5u7xo6kohSDGDZTAjbThhyIv0MuWKwo31EAGfolKucW8CkQfkBn0B380muxgEto5pdVTqMaYXLEShBvdCACpDSv8d7lYM72MSLRjzWCnjQAq50jqWOJxg0Y48y95TrCRauUzTsWDSi7gU0fi_486T4V9HAgLSU2p0JbhIp9GPXy_H7MOfeUt3woalh9CKxY8QU7ZeAwgk343lVrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIlwyieUmG16rEV_oX3oSWamnXGB53OBRozy97t3ndMfChJbeXVp4XuwhE8TJ0onk_35_09suuxVJWv2atJDWgojOsqM86l9im2TWWBA3MHfqUWlagQsKMxxIlFXEctnkCXdiYo6NizdGYbURaSXrJk-P7TOltL5hh329hHSvt740d9RMfTjuj-ig1ZfHK9noSOH5RYbmdx0xMX-hQ5bO6UTrwezrr1oHN0cQUXBu6A6R3OxT3z9Bmg6qoRFDkEFhevsRY73HD7Qtv9LkZD-2ocX133BApJY0QC9wXL-qSWGn3TtKaIZDQ9Bekz08UP0Eq1xCQjb5Bavy3nu50Jv2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3YCjzWmgMx3O-W8kxtAnVty6WTkK59l2z7-BMuTG2l5Bbt5lEleoElvWTOWgtZAV_EXIGCKEC3mlAYMJI4wHqft9gk31SCCEgn6RA7LCyeKONXvxty8ucM8tY3sV4AQUv_MubMBNsn1VvGR8Up0CjIoUpvRW5sErK6QK9NHfmBeNoNhAwRz2sUol7vuDJWx1Qej2cdBxVaWARiUn5UI-QAlve9_m0VVlSJCUTulW1iiEpMJ6n3eIrmxbR7rabnF8cUq32HWMhtj_U4Hi07eLqAZ7gMzIUz9lFAusfpGe1LAiyNaCY3zHLAsoV-cBmJZabE84iIGyW5DH7j2NgU1kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O25cW28EdMLDEgGHqqCD5QUlTyGExg27BGZikrIDDVO1NfmYDe8T_XaXjzMZyF-VZG26cK6nFKhaRiWlLm22cROw7QW10cAPcmM06HnlyU2zhROp4wGBtRoOeyo_ylv0ZXqtKot_K143nWb3HUXmzDKFJIh4sn9d4YTbSNUpSubuoiyLF_7nKtxGm1Svmon43OYEkFtkpL0rJTAhnUqnc3fw3wwsEpSz4887NMNv19CEGi1NGSbS22FomLedJ51G3zJ0ttMJcg_XxJh4hCOuiDfkUF44NX-J1k1Am1ZVySVs-Ghdrs5TUJVzJke4YtIEw54eycSEn9trikOkq8b6Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4j5EujkXwL-Y-Wb_09duLZp3MI44Bsi0RASVHpg3aTRcnyJFGs-esA6EisMp1YYXdBdHR7EkW-xUuVR1JpjklECVc2XLXvRpAXauapiFKdcXuejb26WpxfpPdBMZ7NcMWc0_Nl05FB7wxwtW1eLUXB1m-sCde0Zf31sgsEl-w9wNJuMnPEimUVdS9DiAU71hj-diTvJgGO7oDYC5aFMd1WY9ivL7CmJqzAwhf5hw_t4heJseOTqq8tpLzwjBez71vQzBZ8JoQ1hNOzf5J_jJa7fXvHh7ggE1Kbj-5E40e9M23RnvNxquhZLkOO9JWNZvwZp-2c1CjAKWK7mrt3B1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HejinmdM5Nm6ot9oYM9QF8hofLAgv7d-Yad2f1T8XfWIX7SHO2IRhcBPreSWNuJZiDK0byqJcn1pmQTlt8xaygpp-UBhtmm8VKEXhTqoWCB7SsgPdEJx-eYCtD2ZOH-N8ISA6UlDAuSP8H03KBLsxiIrH2qapsdyHClFAWigCEyoKnSAtEuygXeUVgFKh3jnT7rjID63651OUdQ1F81XlcHNL8SCmSA3PfnphhyyqpV3YTZN_8rU59bt7Eq9KEFnFrrpEenfL1DiDi-ldD0KmkCbLmHBQJxgs7WPtQcGc_bd9I2sWbYVFLxpdShoJGROi92j0Na6rF4hxxl002obeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uN5bNrPPfSINPacW9NAHUfNqID6SoAGc6R39JLDqdL81FMvoPl1NLAbMiOw5hxdB64hzbmZNT3mPP85_Pm_6NNsgG6yYJtfF5gMNc1qh90kktQ_IBHwkw81Grp7Bo8xKxCtrbYOM9woC-xDD90uJg7KgnITi3YsgrCzY9vVCNa6-U3Hc3cfBWp8y77VOZ0KQJqIGHHRN0EeJ2Gafqqy0sFq4Es5kdbQQdPRr05qpclyfGy-0n5VNPf0tfBs1wBx38ZFmeOxzMJAc5tFpzDSDllbXvs1ZYbT2XaL3VDUKPrJhUNuUqX0TS5_ZOtH3c_3p-CN3YKiGWKBLYPwA35CX5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYYY5j2itpO62Ew0udUCfRV63dD1y0zgj7b_iROKk0buRU1eeqNov8HUaXCwnbF8uOmOfe2K02QhKP6cJvYTLtQ2AKla2CkOn4old-7metN3CIddrHX_67d9SDZKVLBxKxe57fHKxdkVKBmJDx0KLGOb-6AZNJJedTqBjAnc8qNJShE9CeVlPPmEfzIWwivAMgklmwyp2_oFQkThbgkaYV8jSfhclIcoSWGJbc2-A9HGJYJKog6Ws5-HNGWDz5VAjlEShyFw9J29h_ri2wwrjKmNb8sSukShgrLYzvXSuWGMEYNUDBrX9eZVktRHhPjdCUB0cunYkzbU-4FSBT_Ycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCMMWBbzKeNkvIp2RzFJ2E2IYhJO0Hi8RbAps9uwyNvTF861VUCXEX9oGzO61fonfEuRoEvWLVRdVrxf1KBmEym3Pr-3F3lVffY3Ghbz-D0MdkhIK5gD68_jVApEIOj2HyWBatETS4R4shP__-S3ZmEAvzF8I8lkgfBwQIHP-g0efqtBVO8Nne10HZbq-5OJHIa9G4jPwsdhvsMxL_be8113CUBzwmnfG9JiZspMWsYBm-d6k_ymFui2A8KVnMjTmyFF40Vsk0CtPCQHjJboMawKarZe3P9rpgV7h6goCAIQZeDDOB9DS4xNEQAJrNY7lkYDuP6Bz8WyCV_vipxRsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebXbt2gV4afpX8UghK1gP0cPzszOZ38t0sC9daunz1Ya1hlLMETAv0Yr5UMdbepDKZQ29vha1T_sqiF0103rpP4j0S_irsbg-3A2bbyHi_-tncjHYiclmwdKa5CEWcQhluB8pBHWAzEPu-yD7NFwLphQ67u3VeHJ4cs5xnIIXc02zvO8K3OkGtzA_sMQVM8L_t5yfLgBMAsm3L-SKbByrin9TwJ0k3qFz3nWymRbYImz6sHGbo5Z2Mj-XVFgM1mRT10Uv1q--F7v6TFPcycnwo0EaXjhX7UX37julnLn6yS3qLjHdCN1WHvvFQNmOJu-sO2lk7XQeti9TamIQX0ueQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQ9Yg1nOAICCAOMECJcz1W1lUxlDCYoaNyObeK9S-gj63tkn5grT9843q5-S3A-Ixs32XEJkkhGT3eXo4lKP7ESlM_-tKokmW81cuWk4ihNqGqR0HZgdAOuCchJ_3vkyXYk9HzuvnGnE4M81cUA_KVk2CFNfEdCdtz3OPPnL1Cog4s5fB0aMm3S1DYrgi4z9PJ8X8PaikTfQJczRja6cR6EqFPwSLGdTZjNiAscD3tFvIkDYvjE3oIJvSYnWooanzP-XHHZBjUfCp4iaiGTEHdkWwa_BNjflVIPEcE06rr2la8WYSgF_PQaBVFe2cK3lMaKBiokLlb7JUh81uYyo7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت.
ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى،
چه كسى میگفت؟
این حرف‌ها را مصدق میزد.
مصدق حتی اقدام رضاشاه در آسفالت
خیابان‌های تهران را به درخواست
انگلیسی‌ها می‌دانست!
او ۱۰ سال پیش از آنکه با محمدرضاشاه در بیفتد، یعنی در سال ۱۳۲۲ ، نطقی در مجلس داشت از آزادی حجاب در زمان رضاشاه و تغییر چهره شهرهای ایران و آبادی آنها انتقاد کرد  و از جمله گفت :« رفع حجاب از زنان پیر
و بی‌تدبیر چه نفعی برای ما داشت؟
اگر خیابان‌ها آسفالت نمی‌بود چه می‌شد؟  و اگر عمارت‌ها و مهمان‌خانه‌ها [هتل] ساخته نشده بود به کجا ضرر می‌رسید؟»</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6596" target="_blank">📅 11:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dapZGvWuDPY7jAkJPDvG1y_3R18n6OSoCkLB7ENi6CSocqufrC5oeVNk3GNNxxcd8-cBdHahQY2t2a7W40PMTFnbtypVIO9Ci-od1LGElH8qFa8VHtB4PukhJtbcxh61jIRNek4gPmi6ONK5wjpYrCZH-YnIoOd2a4rSF62TJTG6dy8828zuOfr2PUrax7Dl_u9UigDGfhldBMDUAKkRsJJxNwX8VNAQ44aDPkV86adm0LS6rZvuls8UTzUbMPTojbatlkyfn8fAByHl2qVWHXS7UlwT4g0KuDymajapOJv6gPpYwWxGPbgIX-ARaOSt-CFpb8VukQVEKSYOnOfDkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز نچیروان بارزانی
رئیس اقلیم کردستان عراق رسما درخواست داده بود که بین ج‌ا و آمریکا میانجی‌گری کنه.
خوشبختانه جمهوری اسلامی
همون دیشب با پهپاد به دفتر نخست وزیر
اقلیم حمله کرد، تا یادآوری بشه چه موجوداتی
در ایران حاکم هستند!
کار خوبی کردید، قطر و پاکستان رو هم بزنید!
قطر رو ولی حتی بیشتر!
که اون شبکه الجزیره‌اش
کپی صدا و سیمای خودتونه!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپایگاه خبری انتخاب</strong></div>
<div class="tg-text">🎥
تماشا کنید: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
🔹
این هم نتیجه باز‌شدن مجلس پایداری!
🔹
عقلای مجلس از تصویب جزئیات خطرناک طرح جلوگیری می‌کنند؟
🆔
@Entekhab_ir</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=Q0IB10QXasq23Nb7x7lgPc73UFKmnPcULzeUiuRVosqlYvqz977ifoThTBePrCfwe-buNIG2hWPOFiTlo_UAcMi8FvR6AUZOs5POeqJGPhpXFIrjmjihL7tY1u1NXE_pCVJBhGiSTj5NrjHRVcnzc3SRWjjKle2_YsGUGlUJJq__8lueMsNDyMBLwxXJYT-7TN1XUUjQboDL534bVKhIQu8dmPW4DW6HSaPXuXd_RMdB-Fv-wmW01fXwJIEvH0MvG1rDpETV6EXFKPsa7py2VDb2rFY6Q-qvlbksetD2gOTwa2jsb043O9sQP1sbpuLM6hZDkjvEHRnEntxDPzC8Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=Q0IB10QXasq23Nb7x7lgPc73UFKmnPcULzeUiuRVosqlYvqz977ifoThTBePrCfwe-buNIG2hWPOFiTlo_UAcMi8FvR6AUZOs5POeqJGPhpXFIrjmjihL7tY1u1NXE_pCVJBhGiSTj5NrjHRVcnzc3SRWjjKle2_YsGUGlUJJq__8lueMsNDyMBLwxXJYT-7TN1XUUjQboDL534bVKhIQu8dmPW4DW6HSaPXuXd_RMdB-Fv-wmW01fXwJIEvH0MvG1rDpETV6EXFKPsa7py2VDb2rFY6Q-qvlbksetD2gOTwa2jsb043O9sQP1sbpuLM6hZDkjvEHRnEntxDPzC8Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنبش شعوبیه یه چیزی توی این مایه‌ها بود
اعراب فاتح، ایرانیان رو تحقیر میکردن،
زنان و دخترهاشون رو توی بازارها می‌فروختن.
می‌زدن توی سرشون و ازشون جزیه می‌گرفتن.
ولی ایرانی‌ها گفتن اصلا ما خودمون از شما مسلمون‌تریم!  و در اسلامگرایی از عربها جلوتریم!
انقلاب اسلامی در هیچ کشوری عربی رخ نداد، در ایران رخ داد!
جمهوری اسلامی توی قانونش نوشته بی‌حجابی ۷۰ ضربه شلاق داره، نه فقط نوشته که اجرا هم میکنه.
هر روز پلمب کافه‌ها و... رو داریم.
هر صبح اعدام داریم، هنوز چند ماه از یک قتل عام نگذشته. اینها اما برای موشک‌های جمهوری اسلامی قر میدن و میرقصن.
البته که مردم ایران آگاه‌ترین مردم جهان نسبت به تاریخ و هویتشون هستن! خیلی!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVvCHGib5xvGXf2sUhazr1NyhUmnVPWQmGZP5yRxkgBimXDgubcaWlpSgkmUypynCpbqymDnY1oN-QnD_Fj5zTBNFdjXlXQmysWh1ooASKxhNG4y_lNnWOakT_Z2KAZ2jN3ojSCW52FpmBQdhJ6HumXip0ebFVLmaORHeavMGTUtM5EWTACqXAJ87S2a6hmdC8B9glOAkV7xv4nQ_KOXliAxefRkcZdNouRnrD0OJCdfRjt5yfr3RPhH7oE8_kLol8IiBDyeMERsFLSw4M0P0zI0bME7SSuDwoTz3-JjZBvlTEhduA70XDRPYghts92zjv-HXtAkfDeCSTxE6-yLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
