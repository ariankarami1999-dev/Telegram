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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 17:07:57</div>
<hr>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqgPO4L5-cWo13NZXBiUQBBxyPePYMKPdxDLbbZToL7P4p9fdeeJQ0yqZ1OBoFguePcF-p2XAEs2wKFdIsl9blOkNYsougYUSTDgAsgsGFTONxPxJCY1krhACm3pE9DtQqTyuBwrL13miq3QMtb2UUVjLHYdaHuBohZZvRETUMvdjS9C6YLv3kOTT8d9XP5d3oj2cSXTonXn2mk7GFUjeiJWeopji4ZIzmPEUhexUiknAq_8qNCAYJjMR8ySeoRtKmhCsAWWb_ye9H04t3sOaGlna9ykZuXkGaifDDriiSgmae-Izv5rqExGkp8MfzAe4CLeTEHfQCGTsD_eOlTNwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XG3f9QOi3hKDDyJvO21Hx7hCCLAMCXCJRS72UU-RndNcIaVcYQgkChldHvKpo4c--VdJE76-vVQEQTlZbGzZA0JTKhU3MC-Pxw_yeQLEY9GUw1XZH96cqZkCi3zkKebnm7mwkTzvh6mIpGTROobJgeGrFkjFoG0ZfGjmRhsYd8k3p1YYf8541ak9Ui5Tf_ElRTyQ4Lq3e7k7m3egzW9iVqRJWie51Acjvjq9s1mFNxAM_kCayTubZzy63e730Bybvw1UbbPAZSAVRW0WnLYtj38vdla8_EqaOxFSDi2tgHOqCG6RVI5nvQk_p8v3RHp9T3ybwF7Zvveb0OqoxJ1TmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZEqPWWiNRlANetar915GXSvcA5DOr5NiSp_TTM851_KqsahyRTJIXvUEjoEUgyGPp8snDIUQg7w3gJ7P-j63LWL3ibcQtPY_EHeN07H-2A9pBXqj2gCKVWPwtHwdp0W-Yp6IjfYRzCIaljae8CLJobgnm3bNXvmQrPsOdlMkL2f8c778-MdE7zcsP6r_yXnrGG1wqbbc-Scn6q5HEbo30GHLO0A-dk_cQmGoKnb14NJTdZ8fVVx_sQo6Klpmdwal4eRPey7u9YhXHIxjdFDAtaZtl9RFtsmuqumFX_gjVB_i1o6peY6juGaL_Y7D-cbi_yHpWee9Eh0VrMHu_UqAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJb_xaXd_XA1jutx0oYBhNG44bUcWHBEx16DFyvdqiRY4Avwg9fqwnhP_c27i2nGS_oxQ_hSLHCkm67IZBrjSuYhaQM1TLqh8Mik0_c1DQJXqvu9BjCocfyXAABt8vkO2upODVa0WgdOZyUmKFRKOR6GygJWQzAVz7mwpjHcR72G0myZIvo2AY7kRgqm9xnJRWnd-bpxBYPzS5U93loF-7Kds_yNSFNqkTfSw6jhZrsfowOxnPLYB4loANz_PLN62s5K6l4qlm9Hne4kVSNfFMU_FNnjx6kl33xGaurLRUWvy-ZBj5l80IPu5pbaxwYA6QwJsAKyt9XPQ8-Dg1PmpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkkUbk8PJ24p4q8n67RQxhVsJwLZ-BQ2ZOIwDSxcxBZohJGJ9HmtBqPjxjPasUCJ6bx-KwvA7OdAoncaIAl3gX-5n6yXwZAtl56eZXQqDfSQmPFIzKIrsKct949u29WjHqIV5Zi9WhXK0iabhpv1iMMzrkLwUREv-UFP8n4mMQnYRHIcU8jzM_Lttc6J3qJf-SHCaZqYRrQHGPEUufaPz7-qaMWuAcXYpU2b6UGpkANSe1wnAL7LaiJeSpFCT85w9PpfLPkGauFyWNmM15EvKYLZQpQ5Jgne8tS1397C5Fnd6vmhJsAQJKqXLnkGCj7nazYWNPJ3YuxTOp5KHTjlQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5D2EX_RfuUvWJ1_ChccPPvOEmMYDhCT3sOXUi0Mz5dRdm89WHBYMFFD6Lh-15Hib6za6mDCWOAfcgbp0DkGoH1BnWBKs4UwO-pPc4ET8qH9fwRN3EcOeagiERjnjUct6nE5HDaWxfmmqX9yLQKCd-VIEd4KRFfuwYphDiyyhbYhBIsmOarGsyp4RiLi0Ayl0VvsCDSbyj0cLv17wrjtT5C-lz8YJjmTgHq4yEaovcgclAFaJ5JzfywgxUgDWGS_R7ck4Q4UQvqDSue8_T_h9dUpIkFTdHT9Gubn2HvxYpB9BfsWTKIDTYKUxL_V95GZAFYXqQPXNU8b7HRTFieTMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeemvMPMMWIWyDBUi7nAktagt5iCRKBqTPgsg0YyEWM7HbZWgZbGik9Kc3a9GIBmio_lHNICqCSjeGcNT1zb4seDlOFLgyjIvGFpDRlCwmwWGmyh4u-sa9xq9cEYwylSCJdi5xTAKZKQ18lRW73Apc0SbOnwLL8tDsWbEJgcHrBg4GM5GYUR36fXJny1i0teA2qA-U1HAtISxUZyfSFDD1mpxDlW_BfqZXwCTAA0LOmXIMwZfo8HQt0CSR1Ao9sxqPlh2K9ZJA5ZCzbE5hkvLHDBWeTtulGr5i_39u4CAlB_8o6qDex8I8yWKg71GWBqBZk4XWuydAPmcQ-cLTfpDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=dp3uuY_kAGFUhCu8nvSGpky9eHlfGeNU7z4TsHf3tPMNHWf5IujXZf869cDcCcA1I7feBEHcov4qMDdUeXv3WcB3rdCxMejfm5kOfGwhi3CZhuLjKFbsPZ_BA2pvswrnwLFhpjlZuJJ_v0WbJL0MdH55iQSgOp1Ul0iCavSNS-3hMXfQe6jfP-7hi-KHYzU6Bx-Zi2lT38avb_urrpoW1N2dxa1jHpAvpyiil_ua4KYZ-abPsqkrZBXu5ECwMD1Gh_qAWfJ4UFNOLzyhL0xAV1LJtf9Jvh54-X4iE1mwVctfSdeCi_zfwxDi9oM2eElqUNc5OFTCq8G7r-4mu0NXaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=dp3uuY_kAGFUhCu8nvSGpky9eHlfGeNU7z4TsHf3tPMNHWf5IujXZf869cDcCcA1I7feBEHcov4qMDdUeXv3WcB3rdCxMejfm5kOfGwhi3CZhuLjKFbsPZ_BA2pvswrnwLFhpjlZuJJ_v0WbJL0MdH55iQSgOp1Ul0iCavSNS-3hMXfQe6jfP-7hi-KHYzU6Bx-Zi2lT38avb_urrpoW1N2dxa1jHpAvpyiil_ua4KYZ-abPsqkrZBXu5ECwMD1Gh_qAWfJ4UFNOLzyhL0xAV1LJtf9Jvh54-X4iE1mwVctfSdeCi_zfwxDi9oM2eElqUNc5OFTCq8G7r-4mu0NXaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OREmQT-zq0JiUy7e2DZ4-ulO6alEsBl6wQAnRRKrqLhzG2D9LZx0zMLDWPIP1o8vWKMdpUCRlyF_KJQbVPG6R2YwkjiQNbtxAsid-t8w8VwYn6Ci33Xm7W0VMo3rLwy_hJlP8-3FDSDcG7cyTPLnUytpPFDmiDcFhmos4LHkaIjOVvctAy8NzfJJ0zmCnb7hw_ywBSqN6UHce3WAVgqwA2tripzQpYUY3g70Ll8ENWny4iD6FKzo3pp7KyXtMnHGvgZH7flrTEq-Efhu6HVFLOjbk130Q20KvXM2fenshx-FzacbpelLndZ30fNI63vUOj9iDr-PkTiUo8cbjlEE_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXCG2UH4ynmL0Ou_EkpAkp4Pq2uuXwKZZEFHoazJyWxG2JjNCs5QuIDSz4P2nqVkqowW8_-cdOcwMObDuqLiR-OslkJBuXi0IERy_X8rRNDj273-U7vRrT9fw8JHG73ryxBGeCn087Sk9kN-_s38aNCJa-mw7E0xsyzSPuTSBJXE9pdWrgErB3GBJaPu1tmQT79iUgpdDbAfLpPsOQape7EMpdJMG0j-LdV33dK8DwkbaGBn0-5L8m5clZGjNr_IC4UXM7tbmM1ZDJsBNNIJTPooWWb0agTs2aVG2kbjlHKPuHiZBEDxFv2_j2YaP9NL4BXTeWSGLvGXCKFLUPAbTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=Pcw4XsxDtbeMq7mkfTJ-mDb5LutQdspqkC483Z3j7-yrkhItoApqgD3QxDWhN8env-8P4y9ifvN5EyU_inoYxUAT6Sm6xcJribaSuIwNTenpui0E_7u8OVKUjSYdRwL4f832MBMTI1bdw5quT4FEnIOV3DQ2jFYBpfHfefnGx25mUzdHIhI2WkhgRdAScJFXhfL_dfG7l8OlCFEeBxgSxcWKTFdS0UiQiMZROgu6UcPOB3rXmVeYkLwXhVom5i7E8oejzLflsIisfDHygdi1i_nuEX1pAcTezMHnDXBIsxApxL3cW3fHrYK6PUsJrheiX0ytOWvQbZL_Jrs1aQDJbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=Pcw4XsxDtbeMq7mkfTJ-mDb5LutQdspqkC483Z3j7-yrkhItoApqgD3QxDWhN8env-8P4y9ifvN5EyU_inoYxUAT6Sm6xcJribaSuIwNTenpui0E_7u8OVKUjSYdRwL4f832MBMTI1bdw5quT4FEnIOV3DQ2jFYBpfHfefnGx25mUzdHIhI2WkhgRdAScJFXhfL_dfG7l8OlCFEeBxgSxcWKTFdS0UiQiMZROgu6UcPOB3rXmVeYkLwXhVom5i7E8oejzLflsIisfDHygdi1i_nuEX1pAcTezMHnDXBIsxApxL3cW3fHrYK6PUsJrheiX0ytOWvQbZL_Jrs1aQDJbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=iEcwncuFhzBDfxRLsQPmyV-BOV5UQ1MRg9LOjW438sSRlov4K8W3YV-CAHILh4V4m35ClYqfCQWVOtQL8I9Q77ZwLUp24OA2dOtNwjwEEM6s5L29shpu7wTwIMpXEJnHH-R1xQCs4dNrxHOKtxFXuYnKAmuHfjRGJQNvVgZLzkw80sG78vLp2Y2XSjj709JXeEoQjHuQH-Hm_Ikxb9_NvX6x--cU0s_7w9-bRJMvQaVu_xzUttezhmmajnMaWBAO_7Nl-nc_N-lcZe8kPRpiY1S_DiYDKwUT6duQNWFcjEgt8bYhCccaZjFho_HpH9SAPV9SIdYfRosBa-67I88DUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=iEcwncuFhzBDfxRLsQPmyV-BOV5UQ1MRg9LOjW438sSRlov4K8W3YV-CAHILh4V4m35ClYqfCQWVOtQL8I9Q77ZwLUp24OA2dOtNwjwEEM6s5L29shpu7wTwIMpXEJnHH-R1xQCs4dNrxHOKtxFXuYnKAmuHfjRGJQNvVgZLzkw80sG78vLp2Y2XSjj709JXeEoQjHuQH-Hm_Ikxb9_NvX6x--cU0s_7w9-bRJMvQaVu_xzUttezhmmajnMaWBAO_7Nl-nc_N-lcZe8kPRpiY1S_DiYDKwUT6duQNWFcjEgt8bYhCccaZjFho_HpH9SAPV9SIdYfRosBa-67I88DUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEFfCQ3J0RKUbEyR_ld9SjSa1kaYxrLFCIlmrrOZu5CEGzG1brPS58hnRtPUY0kyShI0qjVXEfl1i1rBsBWRu88hGjnn4YbLmtQAu382uEn_shC9THTKrzw4pe8uXxcTueSGRyB3jc9m4e2fZp4NZPUr6bP7ykHdvsjkcF5z6BrE8KXw-JmLDXgtS6hCiTSGNEvOMcCiEme7qSAm3i6JbOJwqZSVGMj7hU87lWTlJC6orODLUe4MAHUHPQLznKNdbu-ls-iJXcaCiJ7PBtmwHgB7mHyFq9Vr6CWXkTDTlRya7iCk5pgFSMI2sidYMILE85aBZ4Kpuoxx-4Stj5oC8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTrZFD2AD4jppYuSZ1EntodzDoghVJBo6eF0VKfoI52GhqXJAB8l6iXzbLvVRhMA1u9adK7pvaCN91Jf7AwLRhceWP7rliwfYQyVI9Rr6NF3mjGhQUtbDTzYXqbTqXtZ9nUBZ8ipIWENaeaMeCk5XGtVtOaVuSQvEOdZX5LCmm1zOdMloQWWJmKP-ODrAtjvWO256a5UT9pDGBSUvww9xd8D9aYz0Twsb-ah2cCZU9n7nkq34bjab32rCYA7U6z2DYdi7jddOKJnaDPNzskFI5106U3h4RLqBfI_NogEq3313yc-8t25hyI67Yt7poNeQ5CpKmAHsjNdWWPfKjWMUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VoEci90U1-W-l50WqGDG058a23jGRjO311slesIEIjFN9AmOYOVoRb3vm1dcwZXhIll49C1I4b43sPMHABdkJjHDjnc5nxi3QsCR5jNdyW_MmrDI2pX3Nk33TJ50CzzPIgfNPT7gkIx_gF7FoDlMahUHUXVOk2KvnfD6bIwISeKXdAaRYGYXc5TrcVYwjG2raxpCrg6-Bs7d99OBD8KkIEnQ2S7rjedMf06WMGEMAFyXuXrn8LG7R45pkSE1Dcap0BC7m5SIfjaVexCroRkmHrwKpaaeExdwZqugMJkWONGQnPcdTF4aFUwxPwmFjj4ClrJG0bnqWhblMyV3-rY7sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l25vMv-Xo7oXBeVduQ9W9as20xhtMsc32_ukTf6XC1qeMea3p8FiLBgq-XT5JkW5vCee7cjOtvJQbPKWW_DKXoCPd76YSulQq_-J-XIRDBrzKxgFKrMHEQoHELhcRsEp51P3Njocs0ETx1GTdXDsKbUasQPVR6aYJfq0MROOgX9EqOqVBMcNKfrqibeFffMbCFhomcjpZ3OjhaNYreSM3WiPaJK95j68KoGtZ16W_EocUL0GP77Dz8k2o9CnOljSr2ChVgA-hySfuQ3kGgVCs-qLsrarlrs3YNSb3FaHJxUBnzTguC4l0J3HXcaaqARDsN-R6xkmNu3G52incyiYHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CW8CcG2N0E2vszxzdx6Li7qWXQZ5jObxZD3mIZuoeDWBPh8q-eeO69o2GSzDftADlHHD-jSB2S_yk48gCggyP8V9WboirmQUq7aaDHSv_NArtIRiSWv9NZAgj4hR-sqUDq0KuvCeCOtQrBQ4hVfDCpKrwACSZu7yQXDmTTKOoEXpSpsCVdq59haH14XzJwS9ZfdIpP0HLeRW4sVXBL3vLhvqTASX7ZSN5A8frCvthvYrIg6PuTUx3A26bNVpT3gV3IUsN0iDwSmY_ZkLwTzo1J3WKE0pUZwWlaFmIQmGiGep8EFusC-pYS8sfO3AWG3ntqk6rL7slAXPS9RjQoZW9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOtkoHoOsnnOIDqnVkdM6x4o97SNRQdSSIu-iLd5C1JgVZBEAWNXf7Ptb2uQDr6LjtavCTIt61iIs9_nxIkTIsDqD9KaBfo_OnzEFLJ2wV5Z1VxbdHFkswDlBQd31JP8eJChZOnjBGjway44L7EOrG_t6zHObqYG4R8jv5PS8sR-8D0VWzhDdU8eTnJXMTPonGP18BCfAmik1Y6Muf5RI9zhGdQsqwiI5f6QWIwmdTHQ7ThmZ-AGOmTUnC7vEdO5kPW-Qon6s9LRd7uidVBDrrdS0EsyROGr-1KXwU690fCA7YLmi0agtnT4JSOFWH99Rh45oVu845NeP_t54K7UmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlgtyZxN6quJ-MPKjG5axwBwqgTbOhNhZ1eU8EE655eOxMFKFxMIP_7UTIb2_hW-d0ETLUfELsfw1yHo5sqEB5I1SyYfpM33K7FPY28sbWnHJDXKEd3i2vYKAJOFbbnv9DEPjbuVdQu9IOoWfManGBFNqJCA3gZCJLFHkXTR8t0rR2soRxRFYzsDgHhr5Qx7THDwrQmIfkbCjGdXPJDkvmNdBn1UU4oY2hucMEfwmmaIdd4ZXL1gZq4KSqDTyRoSBqoEL4aFz-4JZljdyp1ywH3UA3B2GnumqLwh7d2iZzUiOcDw3nFHXFLP5_2V0UGc435sHcBpev6MitY6AxyO2Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=IOoww6dXizBg0dFw3ksMeus8WZPMbYVyZ3gMPjYcGovkG3GpjR48_llwepeRzGIsC93frYzyFz5nRmEpqj771HsaiKI6eMUgZQPgY9Rgwnb4EwH9hbXcLA8FUT28Pgz9pWbjs5VO4imJK5DCGQGB2QjYAAbV-MNS7R7njqu6n8206IvqAgnzUlI_dlo8ZVD9QwlnrGp78VMirnm1NWnUyypWrU3hTbeFGQOEZlXtd-ZifmdLHgHkTDiLoqSNxOW1lo3zG_nzNuUQYlsTuFLX8ol-AHrNw8GHXypT1_d7yzes6aG7Crf8MG0ktTaomCgAfhoDB5cEjVWdl5aRJfgMUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=IOoww6dXizBg0dFw3ksMeus8WZPMbYVyZ3gMPjYcGovkG3GpjR48_llwepeRzGIsC93frYzyFz5nRmEpqj771HsaiKI6eMUgZQPgY9Rgwnb4EwH9hbXcLA8FUT28Pgz9pWbjs5VO4imJK5DCGQGB2QjYAAbV-MNS7R7njqu6n8206IvqAgnzUlI_dlo8ZVD9QwlnrGp78VMirnm1NWnUyypWrU3hTbeFGQOEZlXtd-ZifmdLHgHkTDiLoqSNxOW1lo3zG_nzNuUQYlsTuFLX8ol-AHrNw8GHXypT1_d7yzes6aG7Crf8MG0ktTaomCgAfhoDB5cEjVWdl5aRJfgMUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpCJPxO1wj849Gdqf5p_WG1Bebj6i7qKlk95gY44tnNDPEccOg6Iw5uzIURS_A8vVGkdtChpUy9g5Y_VCerperhAO3q7bEoSTlNIQ3yO3HBSaFFZkN1qQ0vokd3pGTXCCHO-4lFTTtkJ2tSJ7Udj-tEY5HIhtk6rdEcEpJhjRBvz-y4xD3oxa1K2MsaQtR0XKw0yKFJCHmlrTsgk1erSm6fSVgNiX17ZtIWmFUhE3j9_rA9QvDBiiKz4LxtCUMB5CJFJu2Y7QunhFLUNd6tg0t5BD_hKZ1h2cXAgpiL5_8OcwLkFvtc8x4gpxHuhqkcqvutJ2WGW003ttVlwW62xWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=soK3_Al6dAnSVMNi-ZO9zIwaAjzhzKrDjRC8-WBrXuYqb0kmI3M-lDzLX-RbObkeOxpf7JV_2TLxSrY3DobQb8BQiJYIH5QL8z4SVNWmGFgC9XsYWy08r-xmjQGBoBH69znNhUo_1_DZogGRJ-JIMbbX9NqxSMEf13CmiZi9fkgF4jZR6Se1MwZpWOKOCxpFGPBmZTyusQe569v43xcHdKu_xFV9SbcRRwiaH7c5TGBHQRQsB8Lz2IiEg6c_-zzQvphOPBsWHEDXDKZeRszkR1OYnaljtJEn2OTBIvDd7Q1ZMTkkkMCaV6ubBohBdObKKCqcd0TfMCYuYkovI1SrwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=soK3_Al6dAnSVMNi-ZO9zIwaAjzhzKrDjRC8-WBrXuYqb0kmI3M-lDzLX-RbObkeOxpf7JV_2TLxSrY3DobQb8BQiJYIH5QL8z4SVNWmGFgC9XsYWy08r-xmjQGBoBH69znNhUo_1_DZogGRJ-JIMbbX9NqxSMEf13CmiZi9fkgF4jZR6Se1MwZpWOKOCxpFGPBmZTyusQe569v43xcHdKu_xFV9SbcRRwiaH7c5TGBHQRQsB8Lz2IiEg6c_-zzQvphOPBsWHEDXDKZeRszkR1OYnaljtJEn2OTBIvDd7Q1ZMTkkkMCaV6ubBohBdObKKCqcd0TfMCYuYkovI1SrwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=CG4FTQFbPIJcluSa443_SewRWk4qPvFUF9IwwHbHdbnuQQC0N0j7Foln-NkdOM2_wIoyRFvGtMbinW3yVH3p3OZAilpWHViPRL6Q4Y2Lu83nMCITTnq87qgowMVXSQ_DhjgT2sEgPnvacXEhwPliO4lIFujstwTgI3jun2WN7o6a0_T8np5cyfSpJ8N6vTXKUmV5wwLRuRsL5j3wOSwGvB7nRve7rSnasQ34El7VSW3ilVerAxvZsuSRDcgDQ-5w_Bd2JWL2eVlKTQTv7wF7WRQio6u3rCJEdh2Fe2yeO21y_-R1d4DLr1M5CrJRYom2QrgRAFrTSZOWdtiyhzyD6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=CG4FTQFbPIJcluSa443_SewRWk4qPvFUF9IwwHbHdbnuQQC0N0j7Foln-NkdOM2_wIoyRFvGtMbinW3yVH3p3OZAilpWHViPRL6Q4Y2Lu83nMCITTnq87qgowMVXSQ_DhjgT2sEgPnvacXEhwPliO4lIFujstwTgI3jun2WN7o6a0_T8np5cyfSpJ8N6vTXKUmV5wwLRuRsL5j3wOSwGvB7nRve7rSnasQ34El7VSW3ilVerAxvZsuSRDcgDQ-5w_Bd2JWL2eVlKTQTv7wF7WRQio6u3rCJEdh2Fe2yeO21y_-R1d4DLr1M5CrJRYom2QrgRAFrTSZOWdtiyhzyD6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-38HGCjRLPEWDEZSz1sutRJ_nXKwIlB8CJYK0UYlo_0Wor8CLgyTmyHBvwWFVZtNz8ToFdJMFHXGDXO8mQjzEsJpeVD0kmUMbKJFKnztufznLcVhc2NTNahe8XK_JLDC2tjyze6_AeCfTZdx21d_zyrkoD1Yi0Mybw-gHJ7hR_Y3K_VQrUnFU8jbCo5Ux_CqkPx3E35QFqY3Zb6UBjdBbjEOWe7n8MAgrdY1MVtXBRo_M3CktYpGZi5DWTQw3I9TuiuyKO4xlfF0tWCNQVzp66m0jpatOGd-cWOplrLlh0PT6CgHfXxhhrQBbPkFAfV2yo492iV7_JWqDkgZScJ2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdKoeI3MDV5ssTww9vNYyr1Zu6_RwmaYhCmi0iKwN6MMO95v-a723W6BRDUsoDWE5WIp-NA9Qd3oH2lu6IkWum8So2mrb9Gf4F7km-eHe-fIye8uIUsjRMQa8tm94sHlnJA0nDq5pCRWK2rBvV5Akt0YBAdt8uGSOo8JBPvx7fzv99OpERhzCwIDacWiuCz5tOunvPuUFaRnazZvOJmWv2Okwd9Dapwo8djgzsm2kINEfiGbyNNrjA0oH4KCWeQMhst_iRYFjcNdlGhPQJ-T3tFgnCY4eSnfB3-PwvJUh9OzDBaeNOCAjzqhYJDTtEqBdhhmK1JtQmgcKdDakpy4Cg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=JRCPxkVtghQGYARpPzk_wwnG3UBbE40Pj87Sxfv884atvcu9WPcGtxNIRVTUTmmmmen8PGVhwSkKqlFRtpEGdS4KFiCt7szRI_fZn_axnZLpjDl3lv5pZ-e3BMi3rfc4cS2Ptog5r0r8Tq6WkPHjiwo1mkVjDZB_HyjeJmnpU9JpZUvgbLEJchBQL4Nmva2b7UttL1FOJnV0UKXWbT3nLRb0arzX8OXTovMkppOWMAinoR7DCcibb9PjUS60yeqiPcnw4XqjnbDg2jrrvNKmrBimNYfs7dshmpJVFCytcf-m7GRX5CQipazT9rAV2YaXbDm4VimWp-iOqhsZWmxN6FNssQe6AV4KZcRIexttamUv8ZeAlKcd7TwMi6ImcvUuylEHsNSlGm9jLKjVSEnGO0lZ0AkPT6JGskCuzkVtRARk-5XN6Ri1iMlMkjA5hGMKq1pZv5Dwz9DOzqWuk7QgnfCpvIF2xBTZDFN7Tj731nRVGUIrGtd4AN6Zil5vNV1sOhHgL57NN-LilPz8rSXXVHjJ3I89KoM-Up94or_qUeAqXa5l5Whvrpo7ZxQFJ4RfmT8fxyVyn3ETAPAz6t7u5yt7ypYGJ2hFh2p1muemA4VDZJRK_zL3_2E4IST2jfz-H8RcaHBiWpOUyNDWsR5Q2sR-Ce2Kl912MMlxzY5r_hY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=JRCPxkVtghQGYARpPzk_wwnG3UBbE40Pj87Sxfv884atvcu9WPcGtxNIRVTUTmmmmen8PGVhwSkKqlFRtpEGdS4KFiCt7szRI_fZn_axnZLpjDl3lv5pZ-e3BMi3rfc4cS2Ptog5r0r8Tq6WkPHjiwo1mkVjDZB_HyjeJmnpU9JpZUvgbLEJchBQL4Nmva2b7UttL1FOJnV0UKXWbT3nLRb0arzX8OXTovMkppOWMAinoR7DCcibb9PjUS60yeqiPcnw4XqjnbDg2jrrvNKmrBimNYfs7dshmpJVFCytcf-m7GRX5CQipazT9rAV2YaXbDm4VimWp-iOqhsZWmxN6FNssQe6AV4KZcRIexttamUv8ZeAlKcd7TwMi6ImcvUuylEHsNSlGm9jLKjVSEnGO0lZ0AkPT6JGskCuzkVtRARk-5XN6Ri1iMlMkjA5hGMKq1pZv5Dwz9DOzqWuk7QgnfCpvIF2xBTZDFN7Tj731nRVGUIrGtd4AN6Zil5vNV1sOhHgL57NN-LilPz8rSXXVHjJ3I89KoM-Up94or_qUeAqXa5l5Whvrpo7ZxQFJ4RfmT8fxyVyn3ETAPAz6t7u5yt7ypYGJ2hFh2p1muemA4VDZJRK_zL3_2E4IST2jfz-H8RcaHBiWpOUyNDWsR5Q2sR-Ce2Kl912MMlxzY5r_hY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ay2LX-znEjPVT5mFftKRuUeN1yYX4aegRdb6D7j7uuCwvDgh91a2RHdbrVrtQQFVdLVJynm0RxEie_MZcz_STNqONgQi1xF6gSimerDwpLrEmGqeGBCnVUXc3qpQN931EY5wJonFvKBYHbJ9CpMy70PDhxfSJF4ByMDq3tnCTtrnSLf0kS6Y9Syt6KNTGgkFDOvAnJ2lMwQTBLocoAuFK4dpZZjFunyNIj9L1r5uN64Fjb7105oEIj4W0DJJ3bcpR6XruzSaNUuITOUwK0ulEdpppfYjMSSQh8OBq_7ZaCkAe-OOQDMrj_bnsG-rm9to0czjuqQx6wLggmc7raNZ0w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=aQ26dU0a5zCJSeuk2n_oZCRDL18w_o0ySiUMYXL3nOHFqnuP2L5imu1bLAeEiJEH1R4itJPO-sSuG0mSUW5Gd5fIgQZNm01fFXhMMgT1N3RMvIODoh26AUZZuVx_F-tL3ke5kq5cUdvQ3mq37FkJZEUBRLoKsr0T5mmOQuQ3ejqDgUxlPOdyVb3irKPoAt7mDDij5KxETRqI1oBE1MJqIzpfskTTscAccs454XSRtjgPm6nwNOGdCaYvawcg7IUN-0lN_mvAL0TNWpLBveNq9He7zHq4zCZ5dS97BMjD4vIIQs_an-x2SFbtg1OF45Inqral3i5QHjmzxu2O4AQb_Iv4cFPfxMrk_QKYPoBawmX3Reg2u3LOXrH34x3cPt92c9BTesI4DEVsM6kvI3o9Z-z2v-soQwTD1n997aqLke9LBshpTuGCd2eLMfvuh6Nv7Dc3ITnFz68pzY1F4AlFtPrMSqC1HvjDTEAy3iual5UoAFJL-Fo_fEFmUAIvcYYVgzppmPXS9_fIuED_21Lyad7iC_tpDsR4AxultilJk7QPEO46MPSxuCXB3xiC7RzJRZ1F4oZbzcMpmLEKOFqmIRRonJZ-H8iBt-Kz9E9ca4wv9b5e6p-4PvI7s53mkvA0D11pZ1I2Mt3Xb9ZoK9PYcUrWSp-NewESwohAcBjtMfs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=aQ26dU0a5zCJSeuk2n_oZCRDL18w_o0ySiUMYXL3nOHFqnuP2L5imu1bLAeEiJEH1R4itJPO-sSuG0mSUW5Gd5fIgQZNm01fFXhMMgT1N3RMvIODoh26AUZZuVx_F-tL3ke5kq5cUdvQ3mq37FkJZEUBRLoKsr0T5mmOQuQ3ejqDgUxlPOdyVb3irKPoAt7mDDij5KxETRqI1oBE1MJqIzpfskTTscAccs454XSRtjgPm6nwNOGdCaYvawcg7IUN-0lN_mvAL0TNWpLBveNq9He7zHq4zCZ5dS97BMjD4vIIQs_an-x2SFbtg1OF45Inqral3i5QHjmzxu2O4AQb_Iv4cFPfxMrk_QKYPoBawmX3Reg2u3LOXrH34x3cPt92c9BTesI4DEVsM6kvI3o9Z-z2v-soQwTD1n997aqLke9LBshpTuGCd2eLMfvuh6Nv7Dc3ITnFz68pzY1F4AlFtPrMSqC1HvjDTEAy3iual5UoAFJL-Fo_fEFmUAIvcYYVgzppmPXS9_fIuED_21Lyad7iC_tpDsR4AxultilJk7QPEO46MPSxuCXB3xiC7RzJRZ1F4oZbzcMpmLEKOFqmIRRonJZ-H8iBt-Kz9E9ca4wv9b5e6p-4PvI7s53mkvA0D11pZ1I2Mt3Xb9ZoK9PYcUrWSp-NewESwohAcBjtMfs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpEIjDP1tUFC5LOXWUDhNUfSowjP2YAgkFO4RcDMUDsauzVsaK2CN9CaZq79fimQkYKDt2jxXmpF6rgrvwSCiHQYwQCuI2G-BG67Ac3cEL69NxbGqTAaYtJUb_veAKZcW0twOArd2t_TuLJool0hOmhgeimaaodX8teypyYCqPpmyLfLS2WSBg3k4ezb1Zi1HJXlq54HDxzcrOS0XWClEvmDQaWmOyRMAOZJqdY66uiIo_1W8qhqvtUqwgwZzkUDChlvJw5KHAUo54jJCD3aoriOwijLgkLsLSfY0m12JS9CcNMDZJYj3-wBik0w1KvRBdZaRN1H_NXvcXErYq5IZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I61hYbFYOcz-n8n8ybJnCW2XiC61vm1h48CH4EYGyhAvM9VzdmLI3JdLQ97R4sYQ0JQEkShfbsqyoKgQKVGKhWdBQPJHNo9dY39b-o8Ht8EGy4m-hYBcMtirhJHcQRtaKaYHQS78vMlUUw319LkR9llj-ocjDe1kt0tqSk7yydhnAEIL75Yq2TmdvrZB6SGqFEDaEUoBj5UZavX-SwaFmg9go8kDTxLbUJJh_z7EVNwNOcRa1VQRQG4bFeYtoODgCcA1-zRFT2Tl7gcNRC_NLoCllVPnADmPb09qGPwphVdG54VJTBn3OFCXsxdY9-E_7SiV-fMhnaMNhHpkGlS-QQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uou9weh3NGIMGhRZ2_--J7gj1kp8hGMs6oRIcamdam7xkcHQbOfpu_6s8BpYXqBh_yfJTWipJSG7xbK6Kh4-yU6jxOC9egIgHSw7GgVNwKrSsHnWbWMYk0NqmOMDa-7eIoqlxOgjwOA6JKIvC3Qn551qW5cgTHlTp_A_Vt1VuiAZr4neMC2a13fvYfWgdFAVvf6GTOj3MrFfIcbJSJAY0F7x3pmAgjb2-svOHEampn_LH93bxTykEC1ZHbzXN_4gVEhpUVt85cFsLQF_97ZMGCwQsZzKEbT841jIR_Ri3B8eTrN-7lF5GUJQ_X6Ci1YiuDju3AkjlEzcrN3GXUTTFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfKJlks39IDKpJDLas6XQBSycES5gONtfjkdW5AMt7A5PRHvOb-HT5l_2m98lbhI8-7tKh8U_IJOVF84nzeJhlo1Rd4CwfTHowpxWlXr9trR0wOHgwdK5NIy83-PBFBgrs0PyhY0m1xF_fvIq81ghD1_Rjm2Unvi2ZViY5FR47hObcB8BCj0z4U8dsK-B-iNuolt9KN7hU-QNsq8N7So1YTWZuO29JLUUFTS7HNrehRqRGdGw4ABpcMmRdr2av_mebg2oYp1Iv-baoiekmF3NIOp7mgasw2sUnP-FX9fekwB0G7hsmmBKiAi445yFblTmn9dDYOrb7qzc_G46DZw9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgMep65pt1lX9anxjcd8tMfZOIg-Fc5dPeW-coJSh_4rLEUPiVxM0uxVabs4odRxr-bbh6i5uZNRYOw6WRnj5B7h3Xg3TmM_aZDwYU-LfgVAiI2im3ZaqZvBt3tKDohKq3hlkzJzDPXVRobrovJkL4fWZ-gN-mifChiipC7ZgV-QRWA73SU-qDFfrETN9K-Kp7OS95QFhX6DmlCLMhZuzx1IjCAbvEChPRhGhOaRyHkYci-Ani4KWazX0_rxaM7pPE1mVKx-lDPLuwpNROR768hefpl5kyCAbIvyGAo-hdRGWBk5hc98aUPpdQFMkN5zl156GF7n7f0NPLFkOg4M-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ac78Y1vwGYYujV3rUfdtr0FJhr4D4KuD6aZ8YEqwP-7UEQVpXuA9ms_nDk9VVqVNJe_V-1gm09FOyQJxTV3j7YYGHtXKO1yTCoywD_ECyVi41TCn6XmlJk2Horz8fSWJ17TsQ2MIK8Nf8Jyl7Amu731t2PnObSNvdC9tYqJKwbbu-TSXkWyXLS38_yWVUNF2FdP8LDnAPYd5HbHngFIFIJctOrKkA5wrjttRayYQSdfIEWPC3GWhLULaMWw5_PB0stXwjVUNwOZIKgZV7CD1_qROuKD6e31Z9yVRuko6aObnh7Tka3f9OCQ9biObjdoyMxtXLvY_1zWkknI2MIa1_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cK6RgpPpD6-xVO6M5xVXOHXpoCwwkfXQMhAufZsHFu356qrEgutQpa9Xz58A-qsCd_fKLkzS2LLbBjJFIz-slPTLGZNnsOmVwvreUBvWnRy-OAc9RgH2GYGOjcln3Jx6I6eaM1V_kVUeVzGnZtt_IQhqvqPFY9wo-CBHvhjiHMEBX7TnVXlXlzpYtgj8bRsYSn1UKdU1RjDntSpAjRgutihWDV9AYE3KC3pnqaywFWfHW8ndzu3vpnKKSu6oecbueTJ8z-v2snXqFY6fMe1-cQMRpWIIxAbHjcwTYHyZo0trXj3Fvh0FwW5WYIQtrcgypsM1diycnm8IoaFAJ2jWRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpeSQuBlD1WpcIxBXzbw9M74YzGZqcQBIObk6RYvQa1-tzQN_eMX6BfnEzbSw7lGH6L7auqJo2euJWKUD8yQmPlvRU_7lT6X4l5sbJ4cmFhA8Hy9GJw4LJdD_ggX5rZHj4RKTNZ6-sParuVoc3TJwcPOCink1J1vGZvTczawo2DUJBGbDHJ0WM5nAKOcrw2nw_wVxGhEREcoWZOVUKekPcL3TIcOAL2TE-TOA4EDdSUg7ziRKLzepwZKhcl9d1ujGBypknN88oCPlDN2gTiflqwYUkDBxKtCaB6B4KDdtyMb3iwOptQqKVFnpcJtdVRcLR1KfVDRqyR2-hsHBhyqww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arVfud7jBIJr6Km0YaeAau7e-bQmyp7PqzM_mMyfZU16nqE4jcKvaHxpQo0BpIUsElqjAwcmMQNS7s4imk_C_Fofnf2xCrXu8J14ZYQaNWcBb6kMEdOMJIs5tyFzGyecDEW4yE_9kJd8B6eVd5AmxNYXVQUS4ggMJ1R6V91bKjmGJpzVLqGFKyVzQ_1RIhYgSQGtWLwC9e-DDxKfgpFIoB6EpQVYRMrPHpy8JjzWhb0V5iJibRUoUndI37FOegk5wMvmc9ABA2g56qg6aLYl3d5sVfI3cFOnks8WONYZMI3iyj4ZY1Zqt-09iQPET8AcW1vL8YlGOiIWD8l9Hpcl8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lv2JpAoD0bcaMBnRTP8wLxwqg4-CHRdLuQgyNRYt0Lo4dYcfFbveSwp9HaSqTD-bsn91dgg4VUfSYVCjsbWOYRZvVZvdw5UhhCPB6Enp9E14eEnCNCBAORuxPVvc-fJvt-8ee_ntSxf8fxHbDjwu6gPMLjpgzfjQQZl7ivNonbJyIvFrgUGGzuRkJQC8TmG_tDtZ4zhEmIimHukrsq5QZoY3OGcOct0_-cQ-epmhqYqbFoMkkTCtlBR0cplzUMvn6HtsLF1kYCPHh7OqMTjuPZV-oAfmhI7OwiBGxiFo9d0xhhmBKEJ4-3r0xoROY8alFB_deJvJqwKONLCEmedABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaeEU7qohi-JzDR466bEhlt5EO0aeLyDWuV0AVJJrDyEhgiZYp5c8jXw9-bYo3eIhMa1x_4tMS7yuDqzD8WYQaJIxuf0u9BgnXOphIdv6cN8KV1GsJiElL9q_VBFmx3ecwP0_Lx2Ouat276lzW5Z_l3_rtcKUyJ3d51Kk_tVL5Njw00_EMaqb-F6qfqQ6xney79rIQRhTIsuSb1_30RSg5lf-UB8BWwF4NmyWATFsIfVKUjB4PKa94ZIxmQCwregeYKG0jH34J4kpvDpjhtXrdbIo3_SLU-XhRQQNc5B7Dqo-HLZbBeqnxv0Ibkxy_plImw8Uz_Xy3OxYY1NV5Ua8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ckcd6EcGRrvzs9jI9wsepF1AZliLJvV8DYlT_dsTCxVk7XFJSlrHm07JmYjRfFtMC6BL1qfK3iXm_JirSUkjDPFlLaKFeJLOxMQSmMNmySbEEaTaFnrDFst-9k37pofDkbQomsjQncY1U98aP1L8XiKCEp9X_uxIKPde55sbO9TYF88fyO9FHa4QFqPtx5o-kB8sWYaDgQqGdY6IoLocgp6PHlmUXxf1-oLsT1mXlnzT8dR1W0tTU9JR3isCemVNfcEoe8Da4Wn9KxmxtKQkB3j6w1wI0o-wSLdb9AKq_bdfht2vzYXqTuBGAukbVmOMhJGG5qnebbUFyyDCRpUfSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9gmLyAVX6YA5W0EJPAlZ3KCyaDoo_h0N9AWFxp50FdfXZkE0_DhZ3jioWnzkCKrTYcBmu_ow84XVtdQEnyDrl_HigPza5sQ1UsALRywq3PVj-dA3bxoNYCFVvvDg2osbIbodE5aQQtVOQTmobJ4ChK7IxpUMu-zUNDRO0t-PJ0KemRLuAHVsuwD9y8T8Ctt9QoNTQmxoI9sAauCNrQgGcUNqXINgZzCF6Oe_dKPs2wPFJaFvYO2oNaRB5sY7PLVLD_ABIAHxX7KlcxJuMi5GUQRDs6t9OUqPQvD4Hu6t32ZeSRVWMdGmQ5mDVWZTZzsrYResMXutaOpYWHek_ASGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJikdPIC7aYHB2tunLdYBZu1Y80qx8wWuUsB3aaSod8IMOKi4QY4TGd3ieFr_mKXvBclpZCbk2VVJLmQ-NhpA0e8lwCZOQTbZtZmvIB5qsc-0SrjjXewr2W9ARMXQr_8ry4dmvA7UeIfmhFDRi1FW01Irx1HYbW94XuDIDN1o7wwj0WPeQbVJUU0-V9WQEYOUqWiiBhm0ptBhndKmKk-msLYKNYWcW95V1rEKziyJqv0RnMaMs18OJNViLZg278Z5UwnwPs15fpeoPylf5sI_3k5km5Ck1jWNK6G4_KZwPp-oMsPHddNKtwNBp6XMS1ggeMHARH2qLB7c3-4VgSa2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSdf5-lggIZlgVbRMJ5uc6SWIZUgpEZ9-etlZwCQPKTnrCP1MGUI9vz3cwAZ6JwNWwk1OFo_qGs9hA99Z4MCj6A49rpHCY4k4eaUx8jZ3246G-JhlZFMAx1h1YxcgObiv_FAeAiUOYWQZ3f7OpaMCdWZ6gcwOFJ1Q2BjY89RjEfWoqEE5Z32MxjYvrqb7Ibrc_O7ILiDBmxsYgVJmI5e7gxlmhEx-9IT-3n-yYlnlkq-N1XU7d8TAnzb3mFhDbOpe36vXxddTvsg1G8CWVnKiFP5Yo0YNZnm8y5mNbHhFc4ZWftAQo69h0JGPPioeKUFQjxI1gOhXwDNv6zGQSB8tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WX19a-mK3D6tk3IZpjYCwlv4Db4LjhpoLIWNJE7khn1By_4XnqgrPvQxl45En0dvU3gyxP-Zi_hbQdZeu3yy6-8r7iz4obHcPbG-4Aqk92CqhBFjQvi80Sg1-UxsOq576clZHbnjPXb4zXSJEVMeDdDjOYdsrJEoJRtOEXUkfxDRn5j6qEMCm3IW1rufr3IVDngJNCEXfXb8d948ftb8i91C_LWfP2bmZhP4nSEzEUpzZKzmnYJ1Evvb3aWt5IbluRGNpVe6NYU8sY2OZ-GWO9S_BeAprpkxm_43us5fwnRu93cwZLisirGaHZXqXhMlmT_1AxZfLAyTFYgxMT5N9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CPSl6rsEhbLQFkXwT4wpSGfKE1XkUJ4kvp-lEAcFaJBNcZN8D_F504824eJSOjNrGCtgVHzT-DkGFh49htQVwvmOQmhlZKWSHGOxfjw687hc6CIIckZM0AwOBhMaUXUplm0Yg4NL2mvsMgfpEu9bVIxgluP4svh9nhaZwRdaNWK1FwzZU0r-8PBAcIFM6ktmfRs_8RlAu1AyXRKLvx0KLD6hrJMWP1M_zd1Pgq4C-bPTlBI15zM-YF2dOFxsXk5KaH3lKmqOkNh-tKMHBPSCjNXGDawKhjwJDjs-GST_TTdKMJKOvJCHZLqa190jbmLfEclbRSaaUiYKyxwi0Tkvtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MSMmqV1fpXogDYvxvkFHvQngXgocOjnZoRDffEaxMgzw4xiZMhwSxKSLPBCOMNYqtIKH0lWb9FPAyQIveyB67Mp4zeDg-z_breftF7F3rmu4G0-ee3J-g1FaaURcmSlTD2wtbDYg_yahUjN__wsqx8TAb4ZxP_DvnSUYBgr5-1Pdbo8Z29KabrbUi4e8m1kRVMPfTS-kShFeUGlg-GidwwwqVZU3tvxzPNCluVUu8bs5yM8Ms2xJ3-1n9Pqvsdih30l3wPzKs4cczQvO9Oj0VbkYtc29FdPyWrH2spr9yty7_zG0r-wp8xRPtUiMdlmNOtWS14ndzk-YdgMcAiHFXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVvjGf9GcCEulLDfA7L_OMhe2OpORTs8KNxTHVdKtqFGiq8Djw2Gml3g3EXvUotADQTuJMtp-CvWlXBidAmfRFvgoBzpR0X4d2AIayV8qfrkoXjXbeRhfo8tbATpSNbuYEqe6FHaAgKT0c0cCxL3gzaNdxq2YDnb_QkGE4GEpZGo4Z1wQW50EKOODu7i5kraO5EiTvrn0LeDtPuDnp71itjpUunyW9wezurtTkLIyoDNGhohPdbj4qFbjI3POqLmyrZwQbcaL2M4uHXZIHyCoO2SlPtVpOi7cyoFnRE1ozpTXwVxegIXXqnUb0e0ZE4N2n5chJaCLpcuEpgZG_e06Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRHhQxkxGwh4Nx3QMRaWciJS7ILrDLFWZB69OpTYwRTt7gvOcnh01hi431XUF289cZNsthqLNsG4cwjisdxY3YnUAEhWCOkqquXBxHJm-TlwBpLV-L-rkL9hCw6MoTTnEa8kGGHKGNvbCRlene6ufXNvnO5o3vNDcNHJTT-LN2ArpX2Vltq5TcySdV2bdYV_RmXZDtsYWVtGTQGD6V7CGwI7A8shV5Y5PtCE2NW6Ws9e7c3trqgyuzJLUznuns6S7QxqRVIXdznH79c8GfzZe_97KMoYRVyjqVaQ6qEkIi6oXOUdBAgEeKd0yxVyXICO0LXv06GrkZrTYwYPuc1Nrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9M1IqeVyivUzZIyAFY0WPONCOqFmzyV2AL76N395DLaJvVr134l21kZYOaCR2C9E-o4LK02uwjTwEziwTQH6Gmt1zmXmDa-wGc2MKP3TLEeuF1riqOMGnrHHtn_NOxlzU7Y7mm3AfddAYoQdfzwuLc4mMyfu9qfYM2zsWgEMMMw_7_3S1fnyy33jHm0MmwutV0S7emwmi5oFEx3-0H07KEfMioz7IkigNRj_ExX3bXlIIzl6lQIvqGPZ3Lr60qdpf__xh-CyDqJX7icUm6Rt-XZebLHhYnzqfkpTMs1qI1-bK5AhCAC8sfdnLWK6DnXu_1pdNwLuNKvtpZOeXEd6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nz7oN2jduJPqOi5ZFQofIcdR9sr3mmyWNHwxLejZpvq5n6LypE4Sdk830rxKLm6rqR-70av5V3SLXSOrDxdntsfjLTi7I-t7mbRq4DFm_S7tK7cW9LQzfclPXae8eHNui7FwqzxwIF3PjBfh6wRZZPsfrEfkBzyEPMifngg_skxA16UYffAVq7XdT4ogDt_srwvSI0u879qniHxw2RqC-m4AoSe3asdiw_X15apScV0W2LCptRNu-asKDfryGqfjveWnuEo1d1cEew6brXONJEd89mO7-1-Wk8FES086W8mzUdZy92_RLSFP0P8boe6ZS8lG8WtV2XRdzCeJCNeBwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSwLj3IiPwRkCdeB7eOYqgdFmads7wXzkKXqoyms_fQ5mpaTv9AYI1yqRyb3pFf_EZ9O0W985OZNgkG-3dqtZCqCePWZL6Lur729u7_-Lhj7hRsgrYoi5ngB1k6RtdWygYe_ax-6KqNxKYOYhN3SYzmj3SDarujLGKEav0JrBO-EpAZrCynr0ivJ6EcmZeKkjqDOhnpwjxOIXfCyO5NqYs6EhmDpn1du5TsaKBLSrCAphFcvLX5FkuU3AF5eATRb5dFxX12DoNEdDkOfIVPm5T_YRmbKf4YiWVrnR_CmPbgCIiBA6xdgDZvfES0WbGCCqsP-idh_Myz_1hEUoLiL9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzpIhd-HHQ-xIYATSCi5JQ5NR6QRaoyw4ZxKAQyAHBzh5HARGQsT7zou7g2CNdL6xDxyq2m49uLEsqSdPwsyxW0LicdbCtgzY4hHvB8pe8sf8vcTMX_OcfhbKZcy62iQqmTK7biiI3pXG0y22MX_Qve3Nzc_mPMHApCEDImvRyZHYODxpBpahrb8GQjjUV4e_gHPmc-vXk2pn_NqrHGwviWCn1x6lz_c5ifBIlvtlIKfDOabQXQs3lZUU3YZh6SmLvC6vbqebMaPZTZ3uf0M9lGG4f0F_bBImKOFX4GlPnjS7OCBzKDH0CJNgx_qnkmFFfD_6atVpFt20XVDA0s4_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gepUwpfv7CV1TQ1KJQ2SImlhfo2v8CyxIJUWly0O4aPnpXwfp4QMOFD5unMtI-Pc8_-MaJkOn6UZTho4N22FIifEwPdWNqicm-An4sZleAvda56ZPojK-roj5pi6oEh-ih1hGlEu4xsSdfh5hmICXm71NKeF6lVK57vFFOiXTdKcbJf1B30oEWHVYm4K8gHSa8UQM1sotNq-x9xIuDIZps6OPr6yu6q__tP4GKMqXFIHhJuYqVXjD64URKrqyWm5aA9xJqEw9w44DW9lsnDAtRbhYjGo8qZlqIE3WYcSn-BQHr90t4eZRrh_aoBZZ47cKy3kKRPGTLHXt3ZmmH1ULw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ft1EJxQkaj5nVZuahCKuWu25O0roBCoo1dMYepo2KNytaSpzbWe6bMdBbE5ClD_2UfojOfvaSepXrgxhkrpWN9016TXhFGK23UH0l2mE0a-vP3WiP-onkzAaeNktLNU9RJj2H1HQx9dZEO94OPCojXK1LrTIg4DrVh1ZYvq67-rhBf4IEIF9sjC_7dULR_G3R8tSsuQBAlzEO6MB9FeG4G7YZONRVyNZW6x3gukslqMPP38mm0Aea6XO9NC8Kot5JtBktQVqBpvxbRLiwxhZN29FLvfgNmaPgtfPrhS6OkCtVjW5h6LNMIgxZsE7hlDGz-hSn1T2Ugwf3xbQ65W5oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyQdt1KnysOslwrHCL4wVh9Vm3SmUzEaONTLViljmiGr_g8rQ1Ah062zvyXjE-VSgvdOVKmmeq4Hj2_yMSjVAayU5wIRxgoZsoVpRK9AtMuvusuEQzFYOHxCwDMbCx4qNMb3qIInknWrf7S5-sK6r3NZr_CN1XZeNUZE2o3T1fkKhQy6L19rgDmej4DmNSHaWa0-voJsZWxvf00Y3EeJ_D_9Q4JmhGwHQ3l-AMFos28tmUk0l6jvVspXFI1QPHuoicwh5IeIRefBcd5LWavMNxkSBmZ0Jathkk-dA7QfuIq3Y4D3qIbL8-zC7zuLPQGSbc871sk9Oy6VTlrRCWILcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bG6SGC4NmDlri8wDVYjV60HBapa1npSYUil7W_R7mMpjnI4MRa8ZEZxuOx6GL9hUGHDVjsIGhpKaGtdzpXwQGMlpHSVnHQU8s6ZSGfEMujxJVVe2nrKEuopgm3cp-tV-uPG3vFdmMOoeriGFYwP2ZqBRitxVVaF-bfct-IfPGwzKB2tvzKEeXq3q2TD_ogU7wJ4pyOLmQ-_5OCN0Szj7tL7nGCY8wjwlYU8eEArPPZxydWxBCf2zh0iSAyLsXQhNeSb6BhHTT3BZmo4oOb0aY9qP5AtDN-17JNot9xW1rBjpacaSF9Z2GUnqb_kwukKeIprcdjVd2R0noegHaGLI1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQsGsrg1fnmJ-bgT4MLhjoLerOdWdIeCUUqsmoh3pvU3A0KjYYqIBo68DMneHgazy_RlaCXrnVF2ZwrKc6SqmopEhQkkJ8gXVMYouCPAxFazIfx-Kg_rcdTfN59eJdz8RJkInWgnDfZ9g3puV4-hUBm8C3ZF54jIQZsuXS2HLpfcZFMQPT3ad6C49MuXZpYIsSBBafGXEFLKMmQnSIWoI8yKvQ_bgq1vo2SeGuL4zgdoK0M6v_y1GR_oQtJ34QkyQjR3so9ez0Y4b5PLIuvuNgVgszPsu5HabtUcTK_KMFbFtSdK_yxcrBgBVAzmXSua9yrdMHMMjcLzDMVBGpuHLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0TDxm-Z6wuJrvHywb42JLPy-YSrVocbxFYsQ3PSnkSQ5qHmZgO4-pk9rg0oxdfFLDE19kq4jaQuatFWqLnLxxhMCCvEgB1FCL_W2pJkez9hQfSyPUvnzaZdJ00ifAk6j6uZWRLLix2w3q9riQdv525Ckx0iw3Oew1oKT1ZbfvTW9ghXIHIzBIHEgHfWFwPS1GhwzRHWwZwoQtE0ksTR0EDzegl57G9N7ydO7L1D4a8ckz4D7F73FJVtmkJrPT6Nc7HkCFtV_cL6lcGmgWdli-xQk2JSV6qFNpaOy1QSqzKXi9eKTQNWW9DbWIcKzwqztxwfF5iX2CeNMjokD7PoQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKEsaYn-yLqXAGMcKlX7u-Jw-YmKLjxW11YWlLk0kdZ3nX0bssY_i2-2IyRHRF0STxJckOc4iSUT-u7x2m47X8CSMt_QxgHM99J4L9Wq4I4XYtvu2Lp5lzV2U1zPjJrqWgww_819WqJsNQ36eyc5MfjKowLV5JUAhYVUsrXwhIvc7WRP8zxhWHDK39MyTCcXLXmpSETd7TeK6Omwbvbm9RikWW0539UxC55h8eHb_pKhniLq_wNZzHEwMakjPei3VYm8eggz3NWv-QueKI5ryLjYDYc77NJln9qMCDDs2tdMtWy1Jz2mq7UmktH9Mh2vYHVqVDQE_tDAJ6dKrTeUyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apnnt_a8IUYIRtK9ofO3NWg5Oxv8JFw8zEKbEJdDyF6vGaHCG5u9tSkh28rOOYd-OxqyK_HIe240nGzI5xYQDsaKONNDiJaiTQzRp-ZYIWb92e78swYyqL_SAIkBaWTggZ3ujmWQM98oXl1w_asWtchrkUShZmBucyX2EyXVMuduHXuzQwT26ODanBp0BKv_DyPNf5eufCK07edcGWbJP0Jt0U9s1dVd_burtkpw3FDoflGAzoy4Jj0w9yu6IWIMZ7i1xrY_6O3xmGsNlCjBBn_vlKCNUSkZ-JhtDywp4FeJC7fSgdvpktR7S1_TRNEHpdtSsLvy6UT0ZG5j0AtDuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HN8_ZmnoJnFNeUJ5JMPrXYt7-AC--QFfa2b8iQeS-mPBJ3D4grXc8xIBYxARdURsYhtX7XXnsMpo6uW9yExWUJ1bV_eTv1b2h0qYzTNMtqP24czRaaq4Xgr4DcFI83Uxh-hwPCGu8O1R-CnaDzl3N2c25YT1x4AGXKH4cnODjp-lzUn7l804a45dtT-FfbZek2pPMtzqwTereMmn-MdW2uu3z_6xYXHyh3TGfjT6pcAphdV4vXZMO90yV8tHLN0U62zUkVvrvHAFQTECTFf5FD5PPSZYO3TXCXzwiZLyKunC6kcodjDc62xoEg-Fr7P5m3Fyo9n0YPFIo7KjkRdpsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBGBNooY6wswL44a9YEvO2ltcSYJ6rCH8znyxPz_kaPq646VaLSNCGxggLAbvQLxVSBTflW7Wffb7CqltcDOj7PACrUp8bUOJtjA8oBbjcpJQb3xFxqR2l40SJGw_pzCCgucJylvBH9vZtZrxsXCDm2OKDnKg6XGNeeNkbEG6W5nq5lp4-vXkfYIuZJJh0F9R0M6AC3WvMB-tCz323IP-j4rN1-JLBCIE0PL_qrmz16501jWVM2koEUzhXZ3dNCy8gGXxKQj5nalLd1GpcrqypRtbz1IgdA7IFE6UrKpI7cFJFhb1KDqDy2-qCRKdiqOYE3rq6rI8vPvTCHu0W39ZQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=U7t-_y7KkBY3B5Yge7t96EnUfs-Ehk-WfJXZYNbPCbYg6TxXzoC7Sqa7XgmlwcVcytAI_xjFXowZVVEToPxgX2xuzqRTa-5OolclK7pzoNI7yAgcuATmdA7HIQxKq3nErT-_VzvZf0GTHH_C3mYu1no-Sm7TWUSwZ23XzX9KiP7gcZsRJg6Wi2gp4ENeluBtTtxx_Ff6gymBaugyz0TXTs3LlQyuuY_6UGdGx0rDWZyEc0YS8UWFtxQOfhwPMPJQc7MTItlgSuBG00QimKYOkKxxivq2nH0vj5YVy0I8CJuH_vmph61_fd4LMnJABTaOc4WxrMV2P2dzI3FE5L-FEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=U7t-_y7KkBY3B5Yge7t96EnUfs-Ehk-WfJXZYNbPCbYg6TxXzoC7Sqa7XgmlwcVcytAI_xjFXowZVVEToPxgX2xuzqRTa-5OolclK7pzoNI7yAgcuATmdA7HIQxKq3nErT-_VzvZf0GTHH_C3mYu1no-Sm7TWUSwZ23XzX9KiP7gcZsRJg6Wi2gp4ENeluBtTtxx_Ff6gymBaugyz0TXTs3LlQyuuY_6UGdGx0rDWZyEc0YS8UWFtxQOfhwPMPJQc7MTItlgSuBG00QimKYOkKxxivq2nH0vj5YVy0I8CJuH_vmph61_fd4LMnJABTaOc4WxrMV2P2dzI3FE5L-FEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7TGjsmErOY7URBqmdZZhy4puqo3lNmNqkHRAYoFKMgv-OQhOMypbpKm9OdcNhen6FnGpMrBV8hjCJFjScCKYl7hjRebaqmR7qXGUjwLUWu_EoXTqcMJO2WF2U0ZA0dH4FgopDjlf1ib67rsT_Nt-uTNa-QSH2rsuqJVNxHiWp85J2zA5b8MdU1ZYGFQCaPb5WTk915CQElhjgbHkpm83iDum_0eI0cbY2l_8e_bu_jJ2Lm1DHNI5MU34WonFRGW2DN6HvmBdwvvV2X2sX9_xHJ8YQHJZaTVXQCseLlEJRBw9zgfGtp9vnYGRRGL7DxbhbOWa0SSsAtOpCYdDYcHfw.jpg" alt="photo" loading="lazy"/></div>
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
