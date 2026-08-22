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
<img src="https://cdn4.telesco.pe/file/QNOjOX7QBytQ6vWu5Rzw5o-_PndxbAStToeN7ermZG4r5YuZTcs2mJRwDkYz2m30htpwX4f4NoTU7uLSbh_-vUFBHc9WsHZ_zhZh8cHwTmECSPbzoE3FyVmUFklxmCo3MzeJX7MmXHYtT-aHCKBHZ3JB3OtrGHJhJDlrEa5ukKmRBaqOBMOqaa9YrUrvuEeHX4Fzzcdj9rJVTrGXVUi59g3eRRQ8-UDEQreZ8VZQe2Ib4xjDCYmzYjpcpsVK2r-cm7hZzQ9GpzIVZfT4XI4qwFz2Apk9dcNIEJZvYgyVw_0Nq3gmFBqmChceX7Z1onFN4SLmKTXF_TIXqUutcEl7JA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.28M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 01:42:18</div>
<hr>

<div class="tg-post" id="msg-683549">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80a6f6a7d3.mp4?token=rF_rHGKaDgyLKAc-YWZBme_9qbPIxc_8_mC5QrnIIJReLyruwl4TeTv4SVclf4TSZtgjKhpj6ZCufOyO_GkUH75dMJNt1KhRupL2i1f4Wbvolfz6OhfCZKUYACR0unFX5cPQXS_fG5cpDUZ0Iu2xYSVkdbylDeZY43v-McLbc4roU2TxWaQ1tgdpGQXTFakFpU7EScmWUzELCKEvvs3qXdtbJkofRR0NgtyUiWD6MaD318FWGb54Q07LPonXJ7iajA4iC07nYkDfYJFywNN-wdpKf_IxfRvQbJVuyCyAk3gDoHbyqfvNhu7xbUumRHTVpgOF2domWkJ1J6wrbzFCVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80a6f6a7d3.mp4?token=rF_rHGKaDgyLKAc-YWZBme_9qbPIxc_8_mC5QrnIIJReLyruwl4TeTv4SVclf4TSZtgjKhpj6ZCufOyO_GkUH75dMJNt1KhRupL2i1f4Wbvolfz6OhfCZKUYACR0unFX5cPQXS_fG5cpDUZ0Iu2xYSVkdbylDeZY43v-McLbc4roU2TxWaQ1tgdpGQXTFakFpU7EScmWUzELCKEvvs3qXdtbJkofRR0NgtyUiWD6MaD318FWGb54Q07LPonXJ7iajA4iC07nYkDfYJFywNN-wdpKf_IxfRvQbJVuyCyAk3gDoHbyqfvNhu7xbUumRHTVpgOF2domWkJ1J6wrbzFCVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بحران آب در فلسطین؛ تمسخر مردم تشنه به نام «انسانیت»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/akhbarefori/683549" target="_blank">📅 01:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683548">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
لارنس نورمن خبرنگار وال استریت ژورنال: برداشت شخصی من این است که در نهایت، دوباره به همان تفاهم نامه برخواهیم گشت، اما بهای موافقت ایران با مفاد آن، از نظر امتیازاتی که ایران در همان ابتدا دریافت خواهد کرد، بیشتر خواهد بود و ترامپ حاضر خواهد شد این بها را بپردازد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/akhbarefori/683548" target="_blank">📅 01:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683547">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سهم شیرینی از سبد خرید مردم به کمتر از ۵ درصد رسید
علی بهره‌مند، رئیس اتحادیه قنادان تهران در
#گفتگو
با خبرفوری:
🔹
قیمت هر کیلوگرم مغز گردو بین ۲ تا ۳ میلیون تومان و مغز پسته حدود ۴.۵ میلیون تومان می‌باشد اما در روزهای اخیر افزایش قیمت جدیدی در شیرینی‌ها اعمال نشده است.
🔹
با توجه به کاهش قدرت خرید مردم، سهم خرید شیرینی به کمتر از ۵ درصد رسیده و قنادی‌ها عملا از سبد خرید مردم حذف شده‌اند.
🔹
حدود ۶۰ تا ۷۰ درصد از مواد اولیه قنادی وارداتی هستند و با توجه به محدودیت‌های واردات و افزایش نرخ ارز و دلار، شاهد افزایش قیمت‌ها هستیم.
🔹
سرانه مصرف شیرینی به ۵۰ درصد کاهش یافته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/akhbarefori/683547" target="_blank">📅 01:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683546">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
حمله توپخانه‌ای رژیم صهیونیستی به جنوب لبنان
🔹
اشغالگران صهیونیست، شهرک المنصوری در جنوب لبنان را هدف حملات توپخانه ای خود قرار دادند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/akhbarefori/683546" target="_blank">📅 01:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683545">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
رسانه انگلیسی: هکرهای مرتبط با ایران برای نخستین‌بار یک نیروگاه بریتانیا را چهار روز از مدار خارج کردند
روزنامه تلگراف اعلام کرد:
🔹
هکرهایی که به ایران مرتبط هستند، یک نیروگاه کوچک در بریتانیا را به مدت چهار روز از مدار خارج کردند. این اولین حمله از نوع خود در بریتانیا است که تاکنون گزارش شده است.
🔹
این قطعی برق، شبکه برق گسترده‌تر را تحت تأثیر قرار نداد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/akhbarefori/683545" target="_blank">📅 01:12 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683538">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ArWkFC0Bap3Bp8qnnQ0yacXjiQ9VIy9D-nkLIqz6Thi06GNAZYp9tXxzkYEMpcxWEeASnZwzOyOBzAVgHlYezufyiq_E7IzMDvbbAkJ3DatpBtnHFbKNX17-LruHOto6AjF2p39lcUYkBG5Xl117JxGUiuEW74fyfXL2agAPXFOQkLQDeXrXRDySLX8_sEpqx5iXgaHtl-npQic7dqIf-SqS6jlmcBDZPHflyLJ6awmiPapuJLn7fkCIpng8O7kbYIEfTVSP7pqtG1kUKUF9yy5eqDkgk4ZidQqpz2Jx4CWs7Gchgdz9aIDz6jAdT4PTDhMdDbyRLk2IE3bmYQOa7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OYcNJOD7XGw8kXJWPKruzOZSDkE3EhLHjyV6gwtAhakFBtvekyPN3y2Vn4AQ9XHdGBZC5vkW3xm_nTyL2uRGQpsyNnASjsS-JT6JA-Qnsl-GRU3ocGvabFltAnLKtwy15f_UlDIDdCcxAlbQh5wuS_fj253cJ8KM03d2Xmto4dmh5X-SASfyV1LqJ1xZ5bBV9XYDvMGiKi1-xKUCMWjupKJADTqs0V9lKPSYavkduPrGd89VH3tS5orIdXkZmxZjmQxpIG9L95Z0lFIOdz4plGGFnlPstTNEaxef_vT3oYIJD2r4OogqBUZqRpDdqSC36rWfbzwLeJPkD693InI9kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4xzimIJfNU_tIzKWTJrpCgcqVKThupJia2TGfGjBHVGayMmBF_WqN2MpfXiGqw7auUHiNvBQ_7Q1Lb4VTBEraso1p8-RtFVXtUqxyAX49nS2YYC_bChz-vfEkTbBGHz_WTUKu83wwOeIV4cUxY66dZdjbkwDxlOQj4XYsc3AUhQw81rC0NRjya82DyoRezxEysA1hNOr1iGpRlSFUvZx7n--qzA7HcYpbI1KjoWV55KIXy6umydUF8BJosOU1uSAHQx8ACUX3uGpQvSJsPAc76a22ymW_NzbW3-rDlCyLhE6tt4xM-Kll_-CwLUpU-dm3CA7JuS_cmkIaag_itqLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h_rBAwwpg4cH7dglgWpMdmcabI7bUq-bHtnQrpkNpidcsbYeMw6bfKjdLAF6UqvlrzTdLJ5ZKYTpNxBSi7QW7Sjg3cubqW_h2a0dthFtsp_dGEEF5uQOpGusyiodvpp2zM02_d6PIiupsaI2hoZOi_WAWS1Uwdn53CMzEYFwiAqBH-vqWTl7mLCF98buAmAuQkYcEFlQiCkiyuIA0SMGtrzHZDkO-Yk3uTCECNAJzLwBU-eC7HCWnf2lxA4rsVt4jDhH5B0fZFdQ9mN8pkK-hfzIolbRmDkC2UF8unAvi-HiEK9Sx3iZuY8zCMmOsEJ8ElRyYFhs9cyBo57eQ8AkpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/agxCgIH8T7yZvqa3eB8YO_16mRlXMqROFfZXo56L1g8fgdNGxrIC7WFbhi1Tz_9Doj-PFQkyRVCSZBEkGSVCf0V8Chwzlm4wvz300Xf6WcNdSomiWNGcv7nmjsORYBm9eKg-icAyxnBMKr6UhJVOwJSd3ghz2ONd-pQSioAYEqdu3NP4kYDmAIIRRV4wDk4s-RfZlwJ3DD1ZvIdm8TdyVvmHWwFqcOBWa7ot4aFIGx1VdVzEslqsAkDLo2_MI3a2GIqonmZl3yDErF_gnMh3_MIuQZa-VvkSxVnsfhsaiWVRMrelB1Z8cOxOIVeGz6abck3eQVT14z5B4kOh__NP7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NSEiUiPhGhBUBBMNebFfpYywV9QeLku7AQLmXr8hT674lPhnoPsXhWKG1lbHsJnyBH15a0ghemZhStLUN84t9jzrvmRYNEOdCFo7Mi522V78QoQj9ZlbQqr5Df7sa401m0UMfu8w5I2ekcoI5sDD5yFvWk749ZziLfoxwtkVsXXcBymPtPgmyvblJnn01ECV_yg1B5Bwjbjvi4dZoLbIQ7YtsBlERZnfZgJGldncBJfKBBw4OOoRYAW2xgNXe4h7TaA3V9_WWl4LQkyX3di7UX7eZjPjO332GshL30GXuQB85TwZFUXgHMc-5viMNtbJnxoOrRtlejlmJvyrZOwjuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uzsN0rdMb6xUlrwTPO8i1BqtA_8JtgdifL5oV-MBdcbv7wmUNar-95jtXHy3snJQfwNgbzaC_kv6-WQtuQUmLPSht4fgzqg56eKej2RfmUtBkk31mjHoG0CdSoQFIMKuHh-RTFwR8vTF1e2QXfGTJ5n-emj6Rmm4rqKXnEspNpG8_1PgaxoWh2yld4pghl-RM8QrYqj1B5pmI-EqHd5xdmLoEvxPtPKOuW3h5OYkGpzTQGA2zz5_JpKCcZpVh3C1ni2Sz0fWu_kMCsBGxMFHvDdcW2YEa2xsFYAwFJqbT1UXxorIzuJzB1mkyok2xUh0DQl7c3VPrsMRvSrXU5qdwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شغل‌های عجیب در زندگی ستاره‌ها؛ رونالدو متخصص خواب دارد!
🔹
فکر می‌کنید فوتبالیست‌های میلیونر فقط مربی و بدنساز دارند؟
🔹
از مراقبت ماهی‌ها تا تنظیم خواب و حتی «دوستی»؛ بعضی شغل‌های اطراف ستاره‌ها واقعاً باورنکردنی‌اند! در این اسلایدها ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/akhbarefori/683538" target="_blank">📅 01:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683537">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e48556a24b.mp4?token=ZPn-mM3YMbNkZFE_QAdthHlAgOaLVQ0Jn93diCpNsnRr6peQAJOoeoUbWVGmwheuM-1aJkFfME95Ka5zDX0GWMT2g-2hMW28tYw3eoiKVDpSt33eqNJHYQDJOm3zVe8qdS9cX1OjRTrfYw_WoCEgU9wiMfhpWTlgKBy0IoEJQH-SrM9Z4vSaupM_Ig4vrwJSWng_5O73v7qUQgRwb50K6zRRwWI1Wss2_yrbc2662R7a8B8jy01iR0I30Ghpo6Oa2ueDtXz_uPgtuOBC0sNrpgdS5S6WkkCdrz4ZpASDA6Q9-MFAC49TwsqJGjMxZ_lbPwcMyRoVHSLeCTb2JRGhJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e48556a24b.mp4?token=ZPn-mM3YMbNkZFE_QAdthHlAgOaLVQ0Jn93diCpNsnRr6peQAJOoeoUbWVGmwheuM-1aJkFfME95Ka5zDX0GWMT2g-2hMW28tYw3eoiKVDpSt33eqNJHYQDJOm3zVe8qdS9cX1OjRTrfYw_WoCEgU9wiMfhpWTlgKBy0IoEJQH-SrM9Z4vSaupM_Ig4vrwJSWng_5O73v7qUQgRwb50K6zRRwWI1Wss2_yrbc2662R7a8B8jy01iR0I30Ghpo6Oa2ueDtXz_uPgtuOBC0sNrpgdS5S6WkkCdrz4ZpASDA6Q9-MFAC49TwsqJGjMxZ_lbPwcMyRoVHSLeCTb2JRGhJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراضات مردم آلمان به صدراعظم این کشور در نخستین حضور وی به مناطقی که دچار آتش‌سوزی شده بود
🔹
فردریش مرتس، صدراعظم آلمان در نخستین حضور عمومی خود پس از تعطیلات، هنگام بازدید از منطقه هورتگن‌والد که به تازگی شاهد آتش‌سوزی‌های جنگلی بود، با اعتراض، سوت‌زنی و بنرهایی از شهروندان مواجه شد که او را به تاخیر در رسیدن به این منطقه متهم می‌کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/akhbarefori/683537" target="_blank">📅 00:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683536">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbZY9IwJ8LurOmz0l-zxsujbnnGQO3ux-ZMHzO8_azOPplYVpKlg3Hsb18jsI8s2A--cFb5Az5QKGcY9qfDum8zLTSB2cMKCuhl68nyw5AgDB0geKXp4Fx4G8KSRJAu4MywCHNsBZmY7JDY1AdkPy4MwKJ3wP6bKpRZYxC6ZUZUhG0_j4bxOV5LjPLy_a4pNFZFeRJmsYVmXW-Yie7ufv1ll-3Kbkz_p6GHwBxXVPbXlq-4XPAvdktCtgSkeXW6gGEaRJUtaO86sBDSVcKT5yd2ACM5W8QHBdX9ngcMo_KvaRT5P-D4fRaj__e-MGYX4_q0MapxHxPUEBA_AFYRdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ دست از خیال‌پردازی برای تنگه هرمز بر نمی‌دارد
🔹
رئیس‌جمهور آمریکا بار دیگر با انتشار تصویری از خلیج فارس «تنگه هرمز» را «قلمرو جدید آمریکا» نام نهاد.
🔹
این توصیف طی روزهای گذشته موجب تمسخر و انتقادات زیادی در محافل آمریکایی شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/akhbarefori/683536" target="_blank">📅 00:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683535">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7e4aa207a.mp4?token=RGKJaYqinJyxMcWgK0v096c_g6i42USCXiUHZek6z4BgF8QWy_rJXfccZPJHUT-UtyCytIcQcYbjw4Ih-cBr-iAlOxWJ8-Dtg-Wgyq4QDPVFTq-DbXi46q9cGpRsAZyb8d93nLLmUxgGMwd3LwRUItR1XBUkDDFM2UseiphDP3XhZyuuQNcDlCQjVDvD62ptM9MoOb839PzLe-FFt1SN3C_6DBHnjnv-78HabV0twBYQfdGaWHYRK7Lx-duM7m8tkJN9PyVvrSG2lUq0pvB0CJ-iJ9KW5cNz3xAbocra6ugxwzx2ddGRch-QTwkJpQ6Y29YWeBSMU4PqUR6-aiFPtwRzTstxQdia3fbILyVaL9rsc7QUAkh-M7xaQZ8yiQM8x9wr1FCxL7E9wCYIFwVn5oivUYGXLBXRjlF-bfxsjbLm1G4BY6r31Mm32_W92SWij_0VyqUkGs857Z_TbO2vJkwbI1Cj07fdA0GZU3ppm33c9xvwSjyHYjLclEPsoR4THKXI1eC5ps8DSERUnQWewzjylZE8PDOmaC3LRheOJSPJs1TD_PhShNaKnPBEzIXDD27m5joZMyfMmIv30FH4qDvojUiRKBQ7-TXftnOl71Wu_jlq0iDamVLAGMXuqZqf0CbXeZXUeEXCviqtlyQ6cOM7sX4umKROLbtg5wAS80Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7e4aa207a.mp4?token=RGKJaYqinJyxMcWgK0v096c_g6i42USCXiUHZek6z4BgF8QWy_rJXfccZPJHUT-UtyCytIcQcYbjw4Ih-cBr-iAlOxWJ8-Dtg-Wgyq4QDPVFTq-DbXi46q9cGpRsAZyb8d93nLLmUxgGMwd3LwRUItR1XBUkDDFM2UseiphDP3XhZyuuQNcDlCQjVDvD62ptM9MoOb839PzLe-FFt1SN3C_6DBHnjnv-78HabV0twBYQfdGaWHYRK7Lx-duM7m8tkJN9PyVvrSG2lUq0pvB0CJ-iJ9KW5cNz3xAbocra6ugxwzx2ddGRch-QTwkJpQ6Y29YWeBSMU4PqUR6-aiFPtwRzTstxQdia3fbILyVaL9rsc7QUAkh-M7xaQZ8yiQM8x9wr1FCxL7E9wCYIFwVn5oivUYGXLBXRjlF-bfxsjbLm1G4BY6r31Mm32_W92SWij_0VyqUkGs857Z_TbO2vJkwbI1Cj07fdA0GZU3ppm33c9xvwSjyHYjLclEPsoR4THKXI1eC5ps8DSERUnQWewzjylZE8PDOmaC3LRheOJSPJs1TD_PhShNaKnPBEzIXDD27m5joZMyfMmIv30FH4qDvojUiRKBQ7-TXftnOl71Wu_jlq0iDamVLAGMXuqZqf0CbXeZXUeEXCviqtlyQ6cOM7sX4umKROLbtg5wAS80Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیام‌های ترامپ علیه ایران را چه کسی می‌نویسد؟
🔹
این زن مرموز ول‌کن ترامپ نیست، هرکجا که می‌رود این زن‌ هم دنبال ترامپ است. او شده همه کار ترامپ، تا حدی که در کاخ سفید هم به او حسودی می‌کنند!
ناتالی هارپ کیست؟ در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/akhbarefori/683535" target="_blank">📅 00:37 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683534">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
علی هاشم خبرنگار الجزیره: فرمانده ارتش پاکستان به ایران می‌آید
🔹
منابع بسیار مطلع به من گفته‌اند که انتظار می‌رود فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان، طی یکی دو روز آینده بار دیگر به تهران سفر کند.
🔹
به گفته منابع من، هدف از این سفر فعال‌سازی مجدد میانجیگری میان آمریکا و ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/683534" target="_blank">📅 00:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683533">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
الجزیره: آمریکا مدعی شده که هکرهای ایرانی ۳۱ ترابایت داده سرقت کردند
الجزیره:
🔹
وزارت دادگستری ۱۷ ایرانی را به انجام یک کارزار گسترده سرقت اطلاعات از طریق حملات سایبری متهم کرده است. این کمپین ۱۴۴ دانشگاه آمریکایی و ۱۷۸ دانشگاه خارجی، به همراه حداقل ۴۲ شرکت آمریکایی و ۱۱ شرکت خارجی و همچنین کارمندان حداقل ۵ سازمان دولتی آمریکایی را هدف قرار داد.
🔹
در جریان عملیات هک، هکرها بیش از ۳۱ ترابایت اطلاعات دانشگاهی و مالکیت معنوی را به سرقت بردند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/683533" target="_blank">📅 00:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683531">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_A8fm2FZCHEADXHSYk9Hh-zDGsGh0mDfVyeo1hQrwSqIinr153EA5No34-PNea3mNFWQS7Kq6sHr7KlrZlO7QnqFVJj8DXnM-unqOgsZtpchZCMyaqFjWhIg6vWJtTE-ocq-Hq24IRHimw__hLzXB2GsIGjnrlbh4504HNHVG4umE0pBtI-j8aBA2VjH73T9iFn-pmg52Ar5J9nQ6iEUZ0yvcX-YzFRUc_3irUcr-h2qcPWu-88a1YPIntTJL1OYefPnuamkZZvhkixRgCibEXnT4o2vG3XwRgIrkSIkIR__sKUNbwlaUsbrLTT347mYvM6y1Rjy9bZNgI6WlFBLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده جنگ
سرلشگر محسن رضایی دبیر شورای عالی امنیت ملی، شنبه شب در گفت‌وگویی تلویزیونی اظهار کرد:
🔹
اگر ترامپ بخواهد اقدامی علیه ایران انجام دهد، زلزله‌وار مقابله‌به‌مثل می‌کنیم، کشورهای منطقه نیز در صورت همراهی با جنگ اقتصادی آمریکا، با هدف قرار گرفتن منافعشان و توقف صادرات نفت از خلیج فارس و تنگه هرمز مواجه خواهند شد.
🔹
هشتصدوچهلمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/683531" target="_blank">📅 00:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683530">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63bd759edf.mp4?token=iOLh_xGFfrPNIYFZ8YhhhnRTQ5AGpnvC3RlOyMcD56FJazdmuPcKZvoOFJjMOOKTB6FrQdCr_23OEIKt4ahaHuLhX-U1XKtMSiEb0R5kYZc05LUEzjoezrjT0ye3OfV5BUvPOhZHE8ikNBp_VwIJpzAOfAcZEb3JN1M5OqaLt9cfpUxs1rnAtq9nmNLp5rt_rNEyY85OeEjUtuPYsH403PVjnpnlwQjRpvPUnKyYpDDFCuaB5hWTlBLX5D0VTDJn9Bbm9Cat9MvAU35FUqK90LODD73hqOM24zCeSZx0B4exen9UF75dDZFo5kF0kuWAEHkX6HUDlpBOj0AMcaoBrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63bd759edf.mp4?token=iOLh_xGFfrPNIYFZ8YhhhnRTQ5AGpnvC3RlOyMcD56FJazdmuPcKZvoOFJjMOOKTB6FrQdCr_23OEIKt4ahaHuLhX-U1XKtMSiEb0R5kYZc05LUEzjoezrjT0ye3OfV5BUvPOhZHE8ikNBp_VwIJpzAOfAcZEb3JN1M5OqaLt9cfpUxs1rnAtq9nmNLp5rt_rNEyY85OeEjUtuPYsH403PVjnpnlwQjRpvPUnKyYpDDFCuaB5hWTlBLX5D0VTDJn9Bbm9Cat9MvAU35FUqK90LODD73hqOM24zCeSZx0B4exen9UF75dDZFo5kF0kuWAEHkX6HUDlpBOj0AMcaoBrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: من با کیم جونگ اون کنار می‌آیم و این واقعیت که من با او کنار می‌آییم، چیز خوبی است، نه چیز بدی چون او ۵۷ سلاح هسته‌ای بسیار قدرتمند دارد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/683530" target="_blank">📅 00:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683528">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پزشکان عمومی به کار تزریق ژل و بوتاکس روی آورده‌اند!
حسینعلی شهریاری، رئیس کمیسیون بهداشت و درمان مجلس در
#گفتگو
با خبرفوری:
🔹
وضعیت دستمزد و پرداخت حقوق پزشکان بسیار پایین است و به همین دلیل پس از پایان دوره تعهدات‌قانونی، انگیزه‌ای برای ماندن در سیستم بهداشت و درمان ندارند.
🔹
تعداد زیادی از پزشکان عمومی برای داشتن درآمد قابل قبول، به‌جای انجام کارهای پزشکی به فعالیت‌های زیبایی مانند تزریق ژل، بوتاکس، سرم‌درمانی و مراکز ترک اعتیاد روی آورده‌اند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/683528" target="_blank">📅 00:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683527">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7z1RjD6fazFpW75NdkfznFFZnHXBqqL2tNF6eywKwyI6Ku24RS3Qq6oIQ1ZyqRw3oSJrm7oTiC1QmQXko08uWePojf1ZsEh3iBPmHEL32RoPYbgup0iSOD2_aBiyBH1ShZ7a4Pwi9NJHgONatSfMeL87e5XbdsiZoEllfDgJ-Q9LYU2kTCA088o-U9rHyheL0OJbPdeeclwIiTHfa9kfQi1g69pvAOY7nzTcb-43opS-Zq_TJBex9TsQhqU25kamKlBr8uKRYiXYwu28ipvxGq2CUSYrULQCYka1XrcVtyxc9kAzXstc3omkflBXmv5bvkQh8zweTxVSivlKFYV4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب‌آبادی: بیش از صد دیپلمات باسابقه انگلیسی و فرانسوی به دولت‌های‌شان هشدار دادند که سیاست رژیم صهیونسیتی به سمت «پاکسازی قومی» و «محو فلسطین» پیش می رود
🔹
آنان خواستار اقدام عملی لندن و پاریس در توقف انتقال سلاح، ممنوعیت تجارت با شهرک‌ها و اجرای تصمیمات دیوان های لاهه شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/683527" target="_blank">📅 00:09 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683526">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ادعای المیادین به نقل از یک منبع ایرانی: ایران دعوتنامه‌ای برای پیوستن به «توافق مکه» دریافت کرده و این موضوع در حال بررسی است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/683526" target="_blank">📅 00:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683525">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bf737fe53.mp4?token=QK7Lv9DvCPhZrfMwuW3YrVr0ixmeTdL5UkOgFHVOE5VI_DVn6ekCK6s5-fqmxvK5oOW2oalG3pW9oFhi81Bx7jwcyOYZeDHdlIKXaECqJiwWk_CpsXpzNtkPdlnUzWCub1rH6Pi8sgu-HUWPj4DrACvt_8wdfKTQ_MGJI3IeUcPbqgM5XvSIBoCKrZv5wNkQVOycJzLSaVDAutjPqCOfRpUTmjZOGJfh8P_xDiqlbEIXP-bww6_3z3TglFGcrnH9AJuoqCYNyi5pJNH9ZUhLV0n5gbE8azUktSaMVJoLBGdO7QLFDPszCXIxY0iKK5-UGmcSnlji3DJuhRWWPbNFrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bf737fe53.mp4?token=QK7Lv9DvCPhZrfMwuW3YrVr0ixmeTdL5UkOgFHVOE5VI_DVn6ekCK6s5-fqmxvK5oOW2oalG3pW9oFhi81Bx7jwcyOYZeDHdlIKXaECqJiwWk_CpsXpzNtkPdlnUzWCub1rH6Pi8sgu-HUWPj4DrACvt_8wdfKTQ_MGJI3IeUcPbqgM5XvSIBoCKrZv5wNkQVOycJzLSaVDAutjPqCOfRpUTmjZOGJfh8P_xDiqlbEIXP-bww6_3z3TglFGcrnH9AJuoqCYNyi5pJNH9ZUhLV0n5gbE8azUktSaMVJoLBGdO7QLFDPszCXIxY0iKK5-UGmcSnlji3DJuhRWWPbNFrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاهدۀ سه قلاده پلنگ در جاجرم خراسان‌شمالی
#اخبار_خراسان_شمالی
در فضای مجازی
👇
@akhbarkhorasanshomali</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/683525" target="_blank">📅 00:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683524">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ag6GVL8hudYbdJj51fJX57G7Tl4raULfxEARM-KlnYKmakYp2G3MturxlwICrsI9IynGxI1UplVSAAjmom6apV6k1eIX5oMg_mpcVOsXCdL353RBfYDV1jsrDiorjerKfJRxmg0rpvrhBMS2AsH9FcOgSwDIeHGc3VZaDqrlG9t5gMELqSnF2JlmIeIyCKWK36SEXBqvreMk_rzVEpXdTkfNcg5feax-1ieLCYtBSG_uXtSx20jHGcNHLwZC_yc5hQEfnI8RjLTpVmlHTEuIj1AKTYqY3YK1UdwwEmq0Ze4VX2BGzOYuSR_Y6NtIFMTlYAHjBrU5V3bXs7dmRAVakw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/akhbarefori/683524" target="_blank">📅 00:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-683523">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce6fb907f2.mp4?token=XGJNd56xXFNNJwG4LeSPAw6-7U8XeZudtjsS4Lw6_G4J0oC2Wm1YvUHeNG2R15kKewJzrzlNSKaxHmT3GuCistup-5Yb__-ot0ApKNzLdEcB-mVopCa7iT5eAWeWWVLBTCeQWCvR5rU1gumOeQukhRKVurcRfqNbn3u6fOzlTCgrJtAIpyBwhosk7tQPctA8OmkeeKKwhP84OfcoNtPOgcpeeX-dzKaHp5JWuCXTu83XtEHTynK-T6aG8jwNVQoi9xJoWSdiFDvyV0a-Y2I-HSrV5RXFm8DVibKXHSx1WonwHte4BNgg-ITMHOvooqKEPl062knWhfTBVlfQAJkVrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce6fb907f2.mp4?token=XGJNd56xXFNNJwG4LeSPAw6-7U8XeZudtjsS4Lw6_G4J0oC2Wm1YvUHeNG2R15kKewJzrzlNSKaxHmT3GuCistup-5Yb__-ot0ApKNzLdEcB-mVopCa7iT5eAWeWWVLBTCeQWCvR5rU1gumOeQukhRKVurcRfqNbn3u6fOzlTCgrJtAIpyBwhosk7tQPctA8OmkeeKKwhP84OfcoNtPOgcpeeX-dzKaHp5JWuCXTu83XtEHTynK-T6aG8jwNVQoi9xJoWSdiFDvyV0a-Y2I-HSrV5RXFm8DVibKXHSx1WonwHte4BNgg-ITMHOvooqKEPl062knWhfTBVlfQAJkVrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاخص کل بورس سقف شکنی کرد!
شاخص بورس امروز با رشد ۱۰۸ هزار واحدی وارد کانال ۶ میلیون واحد شد.
۳۱ همت ارزش معاملات امروز بود و ورود پول حقیقی به بورس داشتیم.
به نظر شما این سقف شکنی شاخص ادامه دار خواهد بود یا مانند سال ۹۹ شاهد یک تله برای معامله گران خرد هستیم؟
@Titretejarat</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/683523" target="_blank">📅 23:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683522">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
رائفی‌پور در اجتماع بزرگ بیعت مردم مشهد با امام زمان (عج): محبت امام صادق(ع) به شیعیان، محبتی فراتر از تصور است؛ حضرت از شوق دیدار شیعیان سخن می‌گوید / تقوا و بندگی خدا، راه تقویت این محبت و رسیدن به محبت نجات‌بخش اهل‌بیت(ع) است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/683522" target="_blank">📅 23:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683521">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJYaTjw2UPb7P7kMha14VozbID93rp1ejTgryekwHqWunJjASf0gFr7IbaBSRG8-zVMtQkL25beMYw5-6Vg7IqsTammDL2kbomRk7rqVmicAMhY_bbvzXPFIryr6sQ6pUVcc0318vb-sQjv9oeK2sSd-9GROmGA9k7cKryv7h73EESWTuF9lFrtywFZVkzUGVnOz3U_6DU352RMd_aHZC_RrbzU__EsrODjlZmZPfCvhFJzMkoWBQmPCYEmtsKGRhDtd50V6Nt-GTnW3XHPNxQPVMqOIDePzhMXp1PEXMkqzdX9B2wlDn_CdgAbngtr8jbiXItkw5MHreOpCGSvAkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله پیش‌دستانه، بهترین راهبرد در برابر فشار اقتصادی / ترامپ از جنگ می‌ترسد / محاصره دریایی اگر با مذاکره نشکست، شاید با جنگ بشکند
🔹
رسانه‌های آمریکایی می‌گویند، آمریکا روز دوشنبه تحریم‌های اقتصادی شدیدی را علیه ایران و شرکای تجاری‌اش اعمال خواهد کرد. در برابر این اقدام چه باید کرد؟
گزارش تحلیلی خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3239679</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/683521" target="_blank">📅 23:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683520">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsDo_yxJ99tQN_apCoXqOUGOFibgmnw-Z-WmJt2Ss6MtlMf8r78GJmkZvMx8__WFoMiV6gqTlpN3ZjxVzkdKxkyrtLpKRNjXdbZECyAgRpDuSYaOcNgW8CSq0h2ZWdVcEjYEbWLt9hI-lz38Eb539bDzhbv6bTy88RE86vhkwy_lIBfr0X6H8sAeN6RHnzeDd2VM8MJezYTyksi_33rgKVwfggFvSeCNBywMrG_KNResp4TMVnpXS_eJEdMxWhgtSvqlfVnu_p0UHLhsbEWJCY8krBBHNmfSSwTPTgNJYntoMnJpWtIQvwvC_EPe_LIoLmsGgWxDGzrt8ywiKuo4TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گرمای هوا شکست
🔹
از ۱۰ روز دیگر هوا خنک‌تر می‌شه و دیگه گرمای خاصی نداریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/683520" target="_blank">📅 23:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683519">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfP68qSZqftme1PzRxKOTY14scC8TvR07IQlQbvgYN4QFAGtIW72Ruu8Ectwk-1GwRIWStUO03HxPuLZ3VTdZ6n-20dMGTCCrkiCvVdJZhDIv_IVVjuRGDZLJ-TPFon6PxsUB8MX8LkaD-HbVrt48DdvmY3xVIUtDZco_TLhAF7f37QK8bZrQXhvm5Ln7sjaTKfyBaGL4Jr9hIl8do_-7xjJHT5uHZ41Ns-30hxmXvlAUF6RUd_XD8-t7xvTCqNIPA7NvxfclqiROIa5PN4sgjAfvTL1o8W5GNYPpftXaGPxfactRDLkostBiR_MwT5SCSp9UU2T04kINMha3QsOwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز خشت‌گذاری ۱۰ اَبرمدرسه هوشمند در تهران
🔹
آیین خشت‌گذاری ساخت ۱۰ ابرمدرسه مدرن با معماری فاخر باحضور رئیس‌جمهور و شهردار تهران آغاز شد
🔹
این سوپرمدرسه‌ها در مناطق جنوبی پایتخت در زیربنای بیش از ۴۰۰ هزار مترمربع و با اعتباری بالغ بر ۱۵۰۰۰ میلیارد تومان ساخته می‌شود
🔹
معاون شهرسازی شهرداری تهران از تکمیل این مدارس در مناطق ۱۵، ۱۷، ۱۸، ۱۹، ۲۰، ۲۱ و ۲۲ پایتخت تا ۲ سال آینده خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/683519" target="_blank">📅 23:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683517">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
طوفان ادارات سیستان را تعطیل کرد
🔹
فردا ادارات و بانک‌های زابل، زهک، هامون، نیمروز و هیرمند به‌دلیل شدت طوفان و افزایش غلظت ریزگردها تعطیل می‌باشند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/683517" target="_blank">📅 23:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683516">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
رائفی‌پور در اجتماع بزرگ بیعت مردم مشهد با امام زمان (عج): برای حل مشکلات و طلب یاری، باید به امام زمان پناه برد و محبت به حضرت را در عمل نشان داد / اجتماع قلوب و وفاداری به عهد با امام زمان، شرط رسیدن به سعادت دیدار حضرت است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/683516" target="_blank">📅 23:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683515">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
قتل پدر، ترک مادر، مهاجرت و بی‌پناهی | اولین زن افغان که به کنگره آمریکا رسید | عایشه وهاب کیست؟
👇
khabarfoori.com/fa/tiny/news-3239557
🔹
منشا صدای شنیده شده در تهران مشخص شد
👇
khabarfoori.com/fa/tiny/news-3239423
🔹
برگزاری مجلل‌ترین عروسی در تهران | عروس و داماد چه کسانی‌اند؟ | عکس
👇
khabarfoori.com/fa/tiny/news-3239376
🔹
عکس جدید معشوقه کاخ سفید | ماجرای ناتالی هارپ عجیب‌تر شد
👇
khabarfoori.com/fa/tiny/news-3239596
🔹
قیمت خودروی محمدرضا گلزار چقدر است؟ | رژه میلیاردی از میان صفِ گوشت
👇
khabarfoori.com/fa/tiny/news-3239571
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/683515" target="_blank">📅 23:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683514">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
بلومبرگ: ایران راه‌های زیادی برای تلافیِ تحریم‌های آمریکا دارد
🔹
رسانه آمریکایی روز شنبه تأکید کرد که ایران در طول جنگ نشان داده که می‌تواند در برابر اقدامات نظامی و اقتصادی آمریکا مقاومت کند و به آن پاسخ دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/683514" target="_blank">📅 23:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683513">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
واشنگتن‌پست: ایران در پی یک غافلگیری اکتبری برای آمریکاست
ادعای واشنگتن‌پست:
🔹
تهران هنوز قدرت آتش‌بار و انگیزه کافی برای حمله پیش از انتخابات نوامبر را دارد.
ایران در حال برنامه‌ریزی برای یک غافلگیری اکتبری یا شگفتی‌سازی انتخاباتی‌ پیش از انتخابات میان‌دوره‌ای است.
🔹
یکی از دلایلی که ترامپ در ازسرگیری درگیری‌های بزرگ تردید داشته، نگرانی اعلامی او از این بوده که ایران ممکن است با پرتاب حملات به اهداف انرژی در عربستان، قطر و دیگر کشورهای حاشیه خلیج فارس تلافی کند.
🔹
این موضوع بخش زیادی از نفت آنها را از بازار جهانی خارج کرده و باعث یک رکود جهانی می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/683513" target="_blank">📅 23:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683512">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
رائفی‌پور در اجتماع بزرگ بیعت مردم مشهد با امام زمان (عج): هر روز زمانی را به گفت‌وگو با امام زمان اختصاص دهید و محبت خود را به حضرت آشکار کنید / اشتیاق به امام زمان، یعنی با او حرف بزنیم و رابطه‌ای از جنس محبت و دلبستگی داشته باشیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/683512" target="_blank">📅 23:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683511">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کلثوم اکبری هَستٍمه.....
بازخوانی پرونده ای که هنوز باز است
🔹
زنی که با ازدواج، سراغ مردان تنها و سالمند می‌رفت... و کمتر از چند ماه بعد، همسرش دیگر زنده نبود!
🔹
پرونده کلثوم اکبری، یکی از عجیب‌ترین پرونده‌های جنایی ایران، حالا وارد مرحله نهایی شده. حکم قصاص صادر شده، اما هنوز قطعی نیست./ خبرفوری
@Tv_Fori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/683511" target="_blank">📅 23:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683510">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb9b1dcca0.mp4?token=B-VCNWpHELTVLqNPJOEv4a1apRGB5dsjE3oiUQ2QIJSGMuuxvsdgehBnpnMMmfLJ0TMSS4wrGWwvAGiI-7H03pS53OSRj_5RWD9YuqIpCjz2c8o6vilm9J76GehDh6m6twFG1xXXsh0NsWC1inISiw2vp7CrHgRcsWqbFNCFtj4itH5yqZSrIiUBgJJO3Pp1WxH7TR7nyDBkdEFyOarFZ-8D2vyacZF0CoUmBQnepitl17j4SV-E9t8dYc5AcTHtZGcgyjEWfxA92xD-pBo3yr2pSAeP8-6CizDz7XBSeLdVFLxS3SliESLjig5PnMWRkLi9ImSD-RW7UOB_NXlL0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb9b1dcca0.mp4?token=B-VCNWpHELTVLqNPJOEv4a1apRGB5dsjE3oiUQ2QIJSGMuuxvsdgehBnpnMMmfLJ0TMSS4wrGWwvAGiI-7H03pS53OSRj_5RWD9YuqIpCjz2c8o6vilm9J76GehDh6m6twFG1xXXsh0NsWC1inISiw2vp7CrHgRcsWqbFNCFtj4itH5yqZSrIiUBgJJO3Pp1WxH7TR7nyDBkdEFyOarFZ-8D2vyacZF0CoUmBQnepitl17j4SV-E9t8dYc5AcTHtZGcgyjEWfxA92xD-pBo3yr2pSAeP8-6CizDz7XBSeLdVFLxS3SliESLjig5PnMWRkLi9ImSD-RW7UOB_NXlL0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: باید جهاد اقتصادی راه‌اندازی کنیم
🔹
دولت باید از اقتصاد دولتی بیرون بیاید و مردم را کمک کند که وارد جهاد اقتصادی شوند. هر محله‌ای می‌تواند تبدیل به پایگاه موشکی جنگ اقتصادی شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/683510" target="_blank">📅 23:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683509">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fbc4c891c.mp4?token=FhM-6vljI23LPecwedeIBHdlt5zNsHKmtrEEsxsaj1ajXvDHKac73yRe8Kmh9pZuJFN3Wy9_OKosdEHBAFAB6mgVfwSwk9Fyz3Y7cFs_VTDf65HHEWdj9f3TXRqHtavn4AsyoEREYwbpLbtw-t9MF02KRsvrmS9jzsywgPvBRNPFOeWN-Ewf_0-4Zl-3JcmBwoCmuDctVbdJnYv5ORsOjQ_Z-2NltLfBfFBLnpAkvrWtSkHyF6ZyqhrF6mkv7vLX60_YXLqEfLvIO7FLGyL6k81R70lyOBRu_wjT_IdnnnaMEINNheCnhOUNN9VEFdt2zRmvDNcry-9MqvJdABM0_4E2t5lZlBTCmaC7S3GEDJ1jlc3vtWLohvJdNbYXX9Qk1XNEmTbcFRjg4oFrWiwqYwcFjE1BP2eRKgd_jfw3MUYgL0Z5DiF0VBp9ZzK22d8P785C7UQLqSTzt-9FHMDjTaiOWb_UIW9PuC_5GtX-m9yt2vcR-4niuItPDb8khVQgG0fmyy1aXwNCXjq9ON6nzWV5X_-SbBpVyWybfBs6sWgPa9d9Tyu-McziTqiaj3pINpR2w9eZHTesVxkA9EjIf8VQ8a-sWnz2hNic0WudfVshLnjdYLAt5man98UsEHYpYZECfM57VDaf1AdJaZ1LcImDI90wZNeMw_NeAmseMdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fbc4c891c.mp4?token=FhM-6vljI23LPecwedeIBHdlt5zNsHKmtrEEsxsaj1ajXvDHKac73yRe8Kmh9pZuJFN3Wy9_OKosdEHBAFAB6mgVfwSwk9Fyz3Y7cFs_VTDf65HHEWdj9f3TXRqHtavn4AsyoEREYwbpLbtw-t9MF02KRsvrmS9jzsywgPvBRNPFOeWN-Ewf_0-4Zl-3JcmBwoCmuDctVbdJnYv5ORsOjQ_Z-2NltLfBfFBLnpAkvrWtSkHyF6ZyqhrF6mkv7vLX60_YXLqEfLvIO7FLGyL6k81R70lyOBRu_wjT_IdnnnaMEINNheCnhOUNN9VEFdt2zRmvDNcry-9MqvJdABM0_4E2t5lZlBTCmaC7S3GEDJ1jlc3vtWLohvJdNbYXX9Qk1XNEmTbcFRjg4oFrWiwqYwcFjE1BP2eRKgd_jfw3MUYgL0Z5DiF0VBp9ZzK22d8P785C7UQLqSTzt-9FHMDjTaiOWb_UIW9PuC_5GtX-m9yt2vcR-4niuItPDb8khVQgG0fmyy1aXwNCXjq9ON6nzWV5X_-SbBpVyWybfBs6sWgPa9d9Tyu-McziTqiaj3pINpR2w9eZHTesVxkA9EjIf8VQ8a-sWnz2hNic0WudfVshLnjdYLAt5man98UsEHYpYZECfM57VDaf1AdJaZ1LcImDI90wZNeMw_NeAmseMdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رکورد شکنی شهروند روس با پرش از لایه‌های بالایی جَو
🔹
سرگئی بویتسوف، شهروند روس پیش از پرش و رکوردشکنی‌اش از بالون هوای گرم، پرچم کشورش را با افتخار به اهتزاز درآورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/683509" target="_blank">📅 23:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683508">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: حملات ما الان هدفمند است و جنگ اقتصادی را هم می‌زنیم خنثی می‌کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/683508" target="_blank">📅 23:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683507">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8ecdab1b.mp4?token=Uw3_1VdKYiG55yWUXPhFlzoIVwKpkNcReRbXOkjWcPfHO0WAY9T3zmnxp1vMIHVsa94meQcZX3tgC3Utln2Hk5g_Hyaipzmb7DCLJqhdWoX2mrDCnlJGyp2dZLZDJwKzlkIbh8oEz68q4LLv8fCAXEGq4XXCvx_JoZB7gz1168Ks9QV3DahdgfqgidjeFgAcICdDXdSrzJyg2ShIBNnkiLMslLbJFX1oGg0Nu4UBN9TmpdNzWzfifSLffROCD4xqx1XUaFdZb2n_XZZzumjoWbBG7XYNkf0XYX68O1S1JjgZ8xer6y_kVr7FXABbDaVNFEoeia_6-N-aeHje9xauRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8ecdab1b.mp4?token=Uw3_1VdKYiG55yWUXPhFlzoIVwKpkNcReRbXOkjWcPfHO0WAY9T3zmnxp1vMIHVsa94meQcZX3tgC3Utln2Hk5g_Hyaipzmb7DCLJqhdWoX2mrDCnlJGyp2dZLZDJwKzlkIbh8oEz68q4LLv8fCAXEGq4XXCvx_JoZB7gz1168Ks9QV3DahdgfqgidjeFgAcICdDXdSrzJyg2ShIBNnkiLMslLbJFX1oGg0Nu4UBN9TmpdNzWzfifSLffROCD4xqx1XUaFdZb2n_XZZzumjoWbBG7XYNkf0XYX68O1S1JjgZ8xer6y_kVr7FXABbDaVNFEoeia_6-N-aeHje9xauRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار در تایوان
🔹
انفجار در منطقه تاینان درتایوان، ۱۳ نفر را مجروح و ۱۱ خانه را تخریب کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/683507" target="_blank">📅 23:22 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683506">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: به‌هیچ‌وجه تسلیم نخواهیم شد و جانانه تا آخرین قطرۀ خون از ایران دفاع می‌کنیم؛ اجازه نمی‌دهیم پای دشمن به خاک ایران باز شود
🔹
ما نیروهای مسلح تا آخرین قطرۀ خون‌مان را به ملت ایران هدیه می‌کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/683506" target="_blank">📅 23:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683505">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: ما تاکنون به هیچکدام از منافع اقتصادی آمریکا حمله نکرده‌ایم
🔹
تاکنون ما فقط پایگاه‌های نظامی را هدف قرار داده‌ایم اما اگر قرار باشد جنگ اقتصادی را جلو ببرند آمادۀ هدف‌قراردادن همۀ شرکت‌های نفتی و اقتصادی آمریکا در منطقه هستیم.…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/683505" target="_blank">📅 23:14 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683504">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35b1e3ebd8.mp4?token=ZUFd0GxPGXOMZYT-7LS0LNPXiqN6neJ-CTjLV451_waHjnQZGcoTqWKrUJkwaCU4QuIm-WpHPPnPvr0ARaqaGaOr25kAo8p9cjmP-ClAV5MV7Ynvf2jr5huQGv0JL6u0iYBFfmMPU8UYkamGFBnImvMtEfoLOtJNtVsc3d3LXR4WumljO8xN-8vXRIOe7xCLViGEfzzMlw1ivYL5-EcW5NBZg5EaYfFDkopq6uhFgkpkxrh8uisn5LDThzboo8l276Vfvm5YJIIrb906Xr4V-JZCbN7UHrIsO_LbCGe1NFWUBgRydCZ6J44_zd8pkvLuVfTCkc4OXAkKyV5uGob8sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35b1e3ebd8.mp4?token=ZUFd0GxPGXOMZYT-7LS0LNPXiqN6neJ-CTjLV451_waHjnQZGcoTqWKrUJkwaCU4QuIm-WpHPPnPvr0ARaqaGaOr25kAo8p9cjmP-ClAV5MV7Ynvf2jr5huQGv0JL6u0iYBFfmMPU8UYkamGFBnImvMtEfoLOtJNtVsc3d3LXR4WumljO8xN-8vXRIOe7xCLViGEfzzMlw1ivYL5-EcW5NBZg5EaYfFDkopq6uhFgkpkxrh8uisn5LDThzboo8l276Vfvm5YJIIrb906Xr4V-JZCbN7UHrIsO_LbCGe1NFWUBgRydCZ6J44_zd8pkvLuVfTCkc4OXAkKyV5uGob8sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مبارزه ابرهواپیمای روسی با آتش‌سوزی‌ها در صربستان
🔹
رئیس‌جمهور روسیه هواپیمای غول‌پیکر و معروف EMERCOM Il-76 را برای کمک به صربستان در مبارزه با آتش‌سوزی‌ها فرستاد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/683504" target="_blank">📅 23:11 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683503">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c69RIpa9Ziwgp6A5Fyzcecq6Tl2Dv3fAkme8LYMhffq9kLu0UpW3zQCQodKRsai_Z-Ly_OgENlS1F0t0_qDQm7NcQBah-_Jce1-Pen9RDtTj4CKbLkzRrzvT1ADo_1Z0EJ_wvUs2KLIQLjwY9fznbzUMgxQYlSa-fEH_SrQJ6vRMCbSIVW1SjTU88PCvpr_igOR1JiSY6ZB2OiV7Or7t19CI3_daOPSnrqH4yEV6UcXq7DvG6tVVcPN1G57NdNvq-KVyD0xnKzq3VFNZ2S-NryTmUEbN_4PMvyyUDvM1xvNvAthoznLxEvkbUKwVlo06woHNn1thp0hkaSqMZ2hXSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اندیشه و دانش؛ چراغ‌های راهِ جان
🔹
امام علی(ع) در حکمت ۵ نهج‌البلاغه، یادآوری می‌کند که «دانش»، میراثی ماندگار است، «آداب» نیکو، زیور همیشگی شخصیت انسان است و «تفکر»، آیینه‌ای شفاف که واقعیت‌ها را آن‌گونه که هستند به ما نشان می‌دهد.  #نهج_البلاغه_بخوانیم…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/683503" target="_blank">📅 23:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683502">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bf0c45907.mp4?token=HLAeKrmJKFR9Sd6hqKLcNXwdd_5tzYPHpIxLng-dxpFfmw5PR5Y7P3h-97VaykzVhY5zcjMg7inEkOqfsz6XGkmldR7foLNtlmEtbcq6psAvtZq003Qx6wTYn_NWmCyVKqjsJnqwV8q6gwXYMaFSwyG2t3YuiF48ZqOAm6cYIBSoLxlJ8HClk5VyNHjaNkr6O8UiRI-qcGXKdkLKlBJwwGTQasVVvHNXk2HK3sRV__9atWvZI8FLojVHk1Kn43wPtCG242KQoXbCvU7N1QSCW9cozhpwSfrYRTRFW4FA7rsSJsyGSP9QwOOcFjj6oPZJEP3GQZB3Eo9qvasAiIpbZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bf0c45907.mp4?token=HLAeKrmJKFR9Sd6hqKLcNXwdd_5tzYPHpIxLng-dxpFfmw5PR5Y7P3h-97VaykzVhY5zcjMg7inEkOqfsz6XGkmldR7foLNtlmEtbcq6psAvtZq003Qx6wTYn_NWmCyVKqjsJnqwV8q6gwXYMaFSwyG2t3YuiF48ZqOAm6cYIBSoLxlJ8HClk5VyNHjaNkr6O8UiRI-qcGXKdkLKlBJwwGTQasVVvHNXk2HK3sRV__9atWvZI8FLojVHk1Kn43wPtCG242KQoXbCvU7N1QSCW9cozhpwSfrYRTRFW4FA7rsSJsyGSP9QwOOcFjj6oPZJEP3GQZB3Eo9qvasAiIpbZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدیرعامل بزرگترین مجتمع پالایش بنزین کشور اعلام کرد:
در بنزین تولیدی این پالایشگاه از ترکیب ۳ درصد متانول و بنزین استفاده می شود!
@Titretejarat</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/683502" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683501">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a780ac014.mp4?token=tbJQZZG10mGT-dmn8OlKbV7ATXL-Ow6jWhzaLPynAzPepW_mvbjXd506s19ArjjdVE-aXHTBFW4vfy7eR-R0Nm8y03RGoPjfRhCBjmCyupi_YR1ZKzrhjlxEdxIiQdnXOuBUPGOzs4cpxnUKvdaTUufStCXVgr5PIg8Dhx_5WaAAl8BobOIWw3v55brbPAokFbL4UUlzx8JIT_KP7ksLItjig6GoR-uM1qkrpyU7RWZG9hz0lPW-0VekrbVrC_AZjrLWhJh3KjxpsVKoa9lkJfZCnwxpWWCXGI4qt8aVFO_WoTaZ72LuJjcO8mOvQBttJvlI8CUcZZNNKobrwHFj2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a780ac014.mp4?token=tbJQZZG10mGT-dmn8OlKbV7ATXL-Ow6jWhzaLPynAzPepW_mvbjXd506s19ArjjdVE-aXHTBFW4vfy7eR-R0Nm8y03RGoPjfRhCBjmCyupi_YR1ZKzrhjlxEdxIiQdnXOuBUPGOzs4cpxnUKvdaTUufStCXVgr5PIg8Dhx_5WaAAl8BobOIWw3v55brbPAokFbL4UUlzx8JIT_KP7ksLItjig6GoR-uM1qkrpyU7RWZG9hz0lPW-0VekrbVrC_AZjrLWhJh3KjxpsVKoa9lkJfZCnwxpWWCXGI4qt8aVFO_WoTaZ72LuJjcO8mOvQBttJvlI8CUcZZNNKobrwHFj2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: ما تاکنون به هیچکدام از منافع اقتصادی آمریکا حمله نکرده‌ایم
🔹
تاکنون ما فقط پایگاه‌های نظامی را هدف قرار داده‌ایم اما اگر قرار باشد جنگ اقتصادی را جلو ببرند آمادۀ هدف‌قراردادن همۀ شرکت‌های نفتی و اقتصادی آمریکا در منطقه هستیم.…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/683501" target="_blank">📅 22:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683500">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">✨
اشک های الهام چرخنده وقتی که از مردم مبعوث شده می‌گفت
@Heyate_gharar</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/683500" target="_blank">📅 22:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683499">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: در صورت ادامه محاصره اقتصادی شرکت های اقتصادی آمریکا را در منطقه خواهیم زد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/683499" target="_blank">📅 22:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683498">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
محسن رضایی: هر خانه میتواند یک لانچر جنگ اقتصادی باشد  دبیر شورای عالی امنیت ملی:
🔹
جوانان ایرانی وارد اقتصاد شوند. هر محله میتواند پایگاه موشکی جنگ اقتصادی باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/683498" target="_blank">📅 22:52 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683497">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: ما با عمان روی مسیر تنگۀ هرمز توافق کردیم که یک مسیر میانی است اما این موضوع روی کاغذ است و تنگۀ هرمز زمانی باز می‌شود که آمریکایی‌ها به تعهداتشان عمل کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/683497" target="_blank">📅 22:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683496">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38655f3126.mp4?token=cw8fSVo-HpVbc3NhZ3r50jhZ76IACFcnHwpogUJ7J-6RKoDR_x3OFb-Agxl56fksWf9iSA9HtVQMCKXtFhNEijrzdsF5VBYMq8sJbk4KBriiF3J0Kqk7wdLvEoyqBvzcs6InMHj6-obe42_0brQvX12a6FXTvPGHOH9iOPoRPxDOHhlrhwxbIR1kgICKiRrHg0LbO_tev5SuU7bGbR4KES_nMaudKfWWuC8rirGlsZK3IhRVEFab5dJzStBawRByx2fFlHsEiEL0DFblVkJH1zFNoWFewTHcXoR9LI5gxAnLfhMMfolLHU8UAONOvDSelP6_8vQY6LnZ7uchHzgL0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38655f3126.mp4?token=cw8fSVo-HpVbc3NhZ3r50jhZ76IACFcnHwpogUJ7J-6RKoDR_x3OFb-Agxl56fksWf9iSA9HtVQMCKXtFhNEijrzdsF5VBYMq8sJbk4KBriiF3J0Kqk7wdLvEoyqBvzcs6InMHj6-obe42_0brQvX12a6FXTvPGHOH9iOPoRPxDOHhlrhwxbIR1kgICKiRrHg0LbO_tev5SuU7bGbR4KES_nMaudKfWWuC8rirGlsZK3IhRVEFab5dJzStBawRByx2fFlHsEiEL0DFblVkJH1zFNoWFewTHcXoR9LI5gxAnLfhMMfolLHU8UAONOvDSelP6_8vQY6LnZ7uchHzgL0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: ما فعلا فقط جریان نفت در تنگه هرمز را محدود کرده‌ایم اما درصورت جنگ اقتصادی اجازه نمی‌دهیم نفتی از خلیج‌فارس حتی به روش‌های دیگر خارج شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/683496" target="_blank">📅 22:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683495">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80537027b.mp4?token=gZTZGv3giYIEMJKr2_tBeatFirSKuDaSfyobSJ2oPa2-HizmFU88Ls46-7Ogal5quq4AgXUlcYutlX9babzwjfhCudSgNGcsbQMl9FRStWK2Ch8WyMVhhcLwQTTaj8GmU4GMdEj_6AUQIk5LK66m8zFfDmcgtfNBU_F8qgMplXxLnc9UYSds6heFOoS-Z3L-_3R3HCWBjEsy0OReCNNsCI-k0WmTjMw08fJ9urRb9kh3ArxxZN-u3lvqxjbPYsgbgODZJ-cZ7TSA3ljn2UtnLxPAcT1zJJxUq7fQs4aGb4tT4OP7yG9MTr9n4yyt-jUOVIBpCMzPy8n_iVkvCxoJFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80537027b.mp4?token=gZTZGv3giYIEMJKr2_tBeatFirSKuDaSfyobSJ2oPa2-HizmFU88Ls46-7Ogal5quq4AgXUlcYutlX9babzwjfhCudSgNGcsbQMl9FRStWK2Ch8WyMVhhcLwQTTaj8GmU4GMdEj_6AUQIk5LK66m8zFfDmcgtfNBU_F8qgMplXxLnc9UYSds6heFOoS-Z3L-_3R3HCWBjEsy0OReCNNsCI-k0WmTjMw08fJ9urRb9kh3ArxxZN-u3lvqxjbPYsgbgODZJ-cZ7TSA3ljn2UtnLxPAcT1zJJxUq7fQs4aGb4tT4OP7yG9MTr9n4yyt-jUOVIBpCMzPy8n_iVkvCxoJFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: جانانه از ایران دفاع می‌کنیم و نمی‌گذاریم پای آمریکایی‌ها به ایران باز شود
🔹
به آمریکایی‌ها توصیه می‌کنم هیچ نیرویی اضافه نکنند چرا که آن‌ها را خواهیم زد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/683495" target="_blank">📅 22:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683494">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKMC</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmW73KrlCoVy7HQft4kY0RfALHCQpxVUOx0qcx5ZTGS2iDrdT7muee1uL03wd7DKb1o4lb3R7bwU-9i8o3UQxorV6BHW7pUq7-uadv-lyj_4O3CEqwelO_7pAc3OxjFEo-UEFcIUSTcezcKEWfL1cEdmaoNo9i8ITDVGhM2499_jMtmyxEpD7uQiudTFBblAyqd13IfHpxqaGqPGGzdIhLDFKSjTSL2iX9e8Ni2hxJwGtw99UZAt9lM1Fin3l9IbjxfmUi4BQxxR1SihdK8PpvigLkvW7tsSLGyB08RL7Lr3bJAymYYZK4FNwU0PcIwleLduhyHP__i_igNUAVxAjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
شرایط فروش کی ام سی  ایگل(KMC EAGLE )
▫️
قیمت: ۲،۴۸۲،۵۰۰،۰۰۰ تومان
▫️
پیش پرداخت: ۱،۵۰۰،۰۰۰،۰۰۰ تومان
مشاهده شرایط فروش
#کرمان_موتور</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/683494" target="_blank">📅 22:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683493">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
الهام چرخنده در اجتماع بزرگ بیعت مردم مشهد با امام زمان (عج): رهبر شهید ما، یک ایرانی به تمام معنا بود/ دشمن تصور می‌کرد با شهادت رهبری، چراغ خیمه‌گاه حسینی خاموش می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/683493" target="_blank">📅 22:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683492">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef25218d8a.mp4?token=Sm7A_fY_sLjA6935cxmz95Vl-DlohPcWqcz7RLg9xUx-9u8ksH8vZRTaeYT4zKc6wBuAn2jVyx-GCCs0iMoaNxNmG-1RkTIGb8J25JOxFXRAB_hWAm6-pyJmlAxCvXo3_I1cjT5uNAA5csL_l63-k8pxBwdjytnYmkVESWNss8-kowb-pzHNNmdjwL2-70urt2hacJzVyel8jq5-5Zd8IAPovfMdMz0-qInRPa8uN-saiZMl9m1W12Xnhmv1OoIEeL_VYCUiofinN9st884l8SHqmS-L5T1ndqpD3TmElJwxQlXqbd4PkPqb3G1Y_EuNA4p1HMH4cUw56QV1je3bYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef25218d8a.mp4?token=Sm7A_fY_sLjA6935cxmz95Vl-DlohPcWqcz7RLg9xUx-9u8ksH8vZRTaeYT4zKc6wBuAn2jVyx-GCCs0iMoaNxNmG-1RkTIGb8J25JOxFXRAB_hWAm6-pyJmlAxCvXo3_I1cjT5uNAA5csL_l63-k8pxBwdjytnYmkVESWNss8-kowb-pzHNNmdjwL2-70urt2hacJzVyel8jq5-5Zd8IAPovfMdMz0-qInRPa8uN-saiZMl9m1W12Xnhmv1OoIEeL_VYCUiofinN9st884l8SHqmS-L5T1ndqpD3TmElJwxQlXqbd4PkPqb3G1Y_EuNA4p1HMH4cUw56QV1je3bYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
مشهد، ستاره‌بارانِ حضور مردم در مراسم تجدید بیعت با امام زمان(عج)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/683492" target="_blank">📅 22:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683491">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
روایت دبیر شورای‌عالی امنیت ملی از پیشنهاد جدید نتانیاهو به ترامپ
🔹
نتانیاهو در واشنگتن به ترامپ گفته ایران را ۶ ماه محاصرۀ اقتصادی کن من به تو قول می‌دهم ایران تسلیم می‌شود. ترامپ گفته در این مورد اشتباه می‌کنی. نتانیاهو گفته ۲-۳ ماه این موضوع را امتحان…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/683491" target="_blank">📅 22:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683490">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5300c5e24.mp4?token=t_52v_X3ujBdF8Pjx0bjij065iwd17ACjF8AlLhvP_dUIZn2Tp4az6UoiiIkjIjSBnYDtpfuuTBA7g-btK6HjonZmuvpsVFsfs6BI2K-SlhndS5eh3CWlFcZ7hjDIcdb4p_s8MLumUtbCxfibUnkXH92hUffM-vRjrsc7kbLTnSlKFQBdCpRKi1h26jV0m_avieq1Za867poQXP4l0V60DQcUvcU3G45r6INR-vLlVcAazsRWbqAAZZUfg_xJdS6c3xCKM5OMkP8aym1fx4s_kbptuJtmVLX5KoGHw6p_sWiuZ5fhnHJTqMeIxh5_UdBOP3Dp4svt51m5wR9v4CAloi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5300c5e24.mp4?token=t_52v_X3ujBdF8Pjx0bjij065iwd17ACjF8AlLhvP_dUIZn2Tp4az6UoiiIkjIjSBnYDtpfuuTBA7g-btK6HjonZmuvpsVFsfs6BI2K-SlhndS5eh3CWlFcZ7hjDIcdb4p_s8MLumUtbCxfibUnkXH92hUffM-vRjrsc7kbLTnSlKFQBdCpRKi1h26jV0m_avieq1Za867poQXP4l0V60DQcUvcU3G45r6INR-vLlVcAazsRWbqAAZZUfg_xJdS6c3xCKM5OMkP8aym1fx4s_kbptuJtmVLX5KoGHw6p_sWiuZ5fhnHJTqMeIxh5_UdBOP3Dp4svt51m5wR9v4CAloi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت دبیر شورای‌عالی امنیت ملی از پیشنهاد جدید نتانیاهو به ترامپ
🔹
نتانیاهو در واشنگتن به ترامپ گفته ایران را ۶ ماه محاصرۀ اقتصادی کن من به تو قول می‌دهم ایران تسلیم می‌شود. ترامپ گفته در این مورد اشتباه می‌کنی. نتانیاهو گفته ۲-۳ ماه این موضوع را امتحان…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/683490" target="_blank">📅 22:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683489">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e563bffa09.mp4?token=TuU37SgvHcCMz8NacEH3IYCFXl4r-1D5KARTeiTS6qdmJcdvT9uSPipglyDYHPtFiSFeKQ7N-_2aV9qeZ-TOv2qNRRoaeXuYw54XWwEMVKVxzHDadRPZdNTJu5UU-lEcoYl1wuA-MpEOfCvHbT4iuHC4bhzCAcrylDZpSHcwzA5ysgqehWd7O5Z_kXXdEUnMailnnylIBlncxMtGyi3-nfJ0T7I9wgh-TeS6MLknBM16IiHv6XZ0JgKYojIlNM-RLGHl2_R7ZeHRZtwj6zqV_87Pdv73nuwvQxIXvXy9VuUWPuFRLURZdZIgLibnNclImLroe3mAjnScDVqM866IZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e563bffa09.mp4?token=TuU37SgvHcCMz8NacEH3IYCFXl4r-1D5KARTeiTS6qdmJcdvT9uSPipglyDYHPtFiSFeKQ7N-_2aV9qeZ-TOv2qNRRoaeXuYw54XWwEMVKVxzHDadRPZdNTJu5UU-lEcoYl1wuA-MpEOfCvHbT4iuHC4bhzCAcrylDZpSHcwzA5ysgqehWd7O5Z_kXXdEUnMailnnylIBlncxMtGyi3-nfJ0T7I9wgh-TeS6MLknBM16IiHv6XZ0JgKYojIlNM-RLGHl2_R7ZeHRZtwj6zqV_87Pdv73nuwvQxIXvXy9VuUWPuFRLURZdZIgLibnNclImLroe3mAjnScDVqM866IZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: برادران ما آماده عملیات هستند اما ما با یک شیب عاقلانه و منطقی حرکت می‌کنیم، امیدواریم آمریکایی‌ها شرارت را تمام کنند و ما به مرحله بعدی نرسیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/683489" target="_blank">📅 22:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683488">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
محسن رضایی: اگر ترامپ بخواهد کارهایی بکند زلزله‌وار مقابله به مثل می‌کنیم  دبیر شورای عالی امنیت ملی:
🔹
به همه کشورهای اطراف می‌گوییم در جنگ اقتصادی با آمریکا شریک نشود وگرنه او را دشمن تلقی می‌کنیم.
🔹
دنبال توسعه جنگ نیستیم اما اگر کشورهای اطراف ایران در…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/683488" target="_blank">📅 22:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683487">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
محسن رضایی: اگر ترامپ بخواهد کارهایی بکند زلزله‌وار مقابله به مثل می‌کنیم
دبیر شورای عالی امنیت ملی:
🔹
به همه کشورهای اطراف می‌گوییم در جنگ اقتصادی با آمریکا شریک نشود وگرنه او را دشمن تلقی می‌کنیم.
🔹
دنبال توسعه جنگ نیستیم اما اگر کشورهای اطراف ایران در جنگ اقتصادی با آمریکایی‌ها همراهی کنند منافعشان را می‌زنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/683487" target="_blank">📅 22:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683486">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e563bffa09.mp4?token=W4FrdItWR9pYxZnfoivH2JE-ehjYwFmH4bM3RjWbISWVpZx82pIBcV2yTJ8XkOKuMaIRQiN_QvnC9lNs9kS_7gL8zIu80IMf7Hve286zw7qqj0VbKapumet5kRwCVcSMeMBgUIyx5VTkB4eqZhpXsB22mvWBybGHKdU4OsBNxaCL3JhV9QBEXnvXeUS412kgxeOPRwgvs_aNTIkOlmDocerzP6mWzz4_EJN5CfkTnTYWfI68V9BEbxs9IX8lDuBGV77u8YOMoAvO9bDnX0TO-C4nH5kZ0WSR4KaYZ0b21Ifih9XWTUjxlzjlqvYK4m--PVrnQqG93NRuTyYxhs2sGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e563bffa09.mp4?token=W4FrdItWR9pYxZnfoivH2JE-ehjYwFmH4bM3RjWbISWVpZx82pIBcV2yTJ8XkOKuMaIRQiN_QvnC9lNs9kS_7gL8zIu80IMf7Hve286zw7qqj0VbKapumet5kRwCVcSMeMBgUIyx5VTkB4eqZhpXsB22mvWBybGHKdU4OsBNxaCL3JhV9QBEXnvXeUS412kgxeOPRwgvs_aNTIkOlmDocerzP6mWzz4_EJN5CfkTnTYWfI68V9BEbxs9IX8lDuBGV77u8YOMoAvO9bDnX0TO-C4nH5kZ0WSR4KaYZ0b21Ifih9XWTUjxlzjlqvYK4m--PVrnQqG93NRuTyYxhs2sGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: حماقت ترامپ دنیا را به سمت دستیابی به بمب اتم سوق داده
🔹
حماقت ترامپ با حمله به ایران اشتیاق مردم جهان به بمب اتم را بیشتر کرد زیرا همۀ دنیا دیدند عضویت در سازمان انرژی اتمی و NPT برای جلوگیری از حمله آمریکا اثری ندارد.
🔹
ترامپ…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/683486" target="_blank">📅 22:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683485">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: امروز ملت ۵ هزار سالۀ ایران با دولت ۲۵۰ سالۀ آمریکا در تقابل است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/683485" target="_blank">📅 22:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683483">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04bbe9cc53.mp4?token=s-094HXsxI3viB2cGPEMnw5BthzHtRhBPO9p_Ey4cP7FFsMgltGmZLc9wxCVsd7LX_4kP7a5TqxN_FOS9sEFuKStBxtmsCFntb5parnBTmZaVggzA07KDhIMl__YwsWB9JyFshu3s4Yeij3XVdMdITTnQWgQnU9QMSfLycqSo78VN7PzhGRKaeAFIH1H9wArRpWiz-eL36KRJxaCQ7kiYOZbtMTLKVQObZeLh0IT6RDFzN1Y6zUaq7QA4ezSuPRjBRzZ-reCqYpeo_SzswsM6mc7LpAd_WjRlyWfQmqfY0DIfVixgIkbUcKie5V3uO1NYgQvyVHbiDPb07jTEkquLmrV3jaA4HHIOxddQaMjTdxfxm7Cuw_YPYHtJV_fmZvfRbwcI72IpONJ0DvSI3QH5wFTDPwMmNqRTQS_S30g84Pth6tQ5x8OfhF6X27iYIwuBoUBrtZk6if3I7MXcypLHDli3_lcq0DB3prAbqXf8nGwWg6Bu4NC4CpoNTJpReTgG06tIsVLmWdXQw6d5FnZ6iu5LOyZJxtkSnZnYqOQHCwWeRXRUlomWlRJ85Mwi1EOm2rsnkHhtA7dKreFXGZz6KV0oowVrj5Zy1zLZoTxkHeE35nNnSyKKfEM1rD2DLtqYGORYhvOD8AdcNDjFk5bUlcjtFAYfYNWvCD-S4YKXwM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04bbe9cc53.mp4?token=s-094HXsxI3viB2cGPEMnw5BthzHtRhBPO9p_Ey4cP7FFsMgltGmZLc9wxCVsd7LX_4kP7a5TqxN_FOS9sEFuKStBxtmsCFntb5parnBTmZaVggzA07KDhIMl__YwsWB9JyFshu3s4Yeij3XVdMdITTnQWgQnU9QMSfLycqSo78VN7PzhGRKaeAFIH1H9wArRpWiz-eL36KRJxaCQ7kiYOZbtMTLKVQObZeLh0IT6RDFzN1Y6zUaq7QA4ezSuPRjBRzZ-reCqYpeo_SzswsM6mc7LpAd_WjRlyWfQmqfY0DIfVixgIkbUcKie5V3uO1NYgQvyVHbiDPb07jTEkquLmrV3jaA4HHIOxddQaMjTdxfxm7Cuw_YPYHtJV_fmZvfRbwcI72IpONJ0DvSI3QH5wFTDPwMmNqRTQS_S30g84Pth6tQ5x8OfhF6X27iYIwuBoUBrtZk6if3I7MXcypLHDli3_lcq0DB3prAbqXf8nGwWg6Bu4NC4CpoNTJpReTgG06tIsVLmWdXQw6d5FnZ6iu5LOyZJxtkSnZnYqOQHCwWeRXRUlomWlRJ85Mwi1EOm2rsnkHhtA7dKreFXGZz6KV0oowVrj5Zy1zLZoTxkHeE35nNnSyKKfEM1rD2DLtqYGORYhvOD8AdcNDjFk5bUlcjtFAYfYNWvCD-S4YKXwM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آثار و برکات دعا برای فرج امام زمان از زبان حجت‌الاسلام حیدری کاشانی در اجتماع بزرگ بیعت مردم مشهد با امام زمان (عج)
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/683483" target="_blank">📅 22:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683482">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d73a84331a.mp4?token=CdZZuHJ1B1H0l0e-1DCQPWbmTR3jpbZYuAuhjwGTQVKR_FXlCNjZmyEC6z4cXwVRSzxcEvAiXZ_RoUjHED_lhTrEb3KTyzqQNQsblIQj3hEn9efcaqVVYkdhWZsT6bW7ZxIu5ryishczg-j_WkXlNnS0cbv1rGwfISwridfeaDluLzyRnWZIkDaQmu1UpjpMmaj8wrdEhEfAED7ZbqtZ9cngudUDFj94_Ly6a-LI0bMPSnWTpCsQ6HIv7DQaf2bXIcd3im-feoohPcDxqe6UKc4VrmmqKEW01OerpvhzcL7df0B8HeMW4wHEBogt1fqJUFfniOze7_OGE3rXrgZjsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d73a84331a.mp4?token=CdZZuHJ1B1H0l0e-1DCQPWbmTR3jpbZYuAuhjwGTQVKR_FXlCNjZmyEC6z4cXwVRSzxcEvAiXZ_RoUjHED_lhTrEb3KTyzqQNQsblIQj3hEn9efcaqVVYkdhWZsT6bW7ZxIu5ryishczg-j_WkXlNnS0cbv1rGwfISwridfeaDluLzyRnWZIkDaQmu1UpjpMmaj8wrdEhEfAED7ZbqtZ9cngudUDFj94_Ly6a-LI0bMPSnWTpCsQ6HIv7DQaf2bXIcd3im-feoohPcDxqe6UKc4VrmmqKEW01OerpvhzcL7df0B8HeMW4wHEBogt1fqJUFfniOze7_OGE3rXrgZjsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: تصمیم رهبر انقلاب برای آمدن فرماندهان باتجربه معنایش این است که تجارب یک‌سال گذشته حتما در نبرد آینده استفاده می‌شود و جنگ آینده متفاوت‌تر از جنگ ۴۰ روزه خواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/683482" target="_blank">📅 22:22 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683481">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
نیوزویک: تهران در کوتاه مدت تسلیم فشار نمی‌شود
نیوزویک:
🔹
مهم‌ترین سناریوی فعلی این است که تهران در کوتاه‌مدت تسلیم فشار نمی‌شود. ایران با تکیه بر شبکه پیچیده‌ای از کانال‌های تجاری غیررسمی، فروش نفت به چین و اقتصاد داخلی نسبتاً متنوع، به نوعی «صبر راهبردی» روی آورده است.
🔹
در مقابل، واشنگتن با تشدید تحریم‌ها و تهدید به محاصره دریایی، به دنبال فروپاشی اقتصادی ایران است. بار بحران اما تنها بر دوش ایران نیست؛ استراتژی آمریکا با چالش‌های داخلی ملموسی روبرو است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/683481" target="_blank">📅 22:22 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683480">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46a51b803f.mp4?token=RknuDvCDACTZ4PiLhOqi_S0rJqo4dJxT76dr2eHLL1QPivSr7qTtpMp8g1tjl2w4azKPKtxpcPxTF_qdnjE2NJlaGTXNZfyxmh1fzALSuG0EgN4xOpva7EoS5j1wJfxRlx_tcAybeGsRPAKa5i9jgGMKUqyfm3nYALiZMW_SRBdPSMUbBytP9d07osJfPd2Ej7DcaGAjjE62KsQj5gAh2ywO3tBhtL_ocbNGhVt0WXJtm-bBUkA94kH-Jn82jxzn0HkF7LrMJfoUDUScZO9pwFhSewxa-e7InbdrxueCRxaaP4y7-O_Ey6Cft_oko9Wb8tmzkbtDJJ8jPrY-7iaGwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46a51b803f.mp4?token=RknuDvCDACTZ4PiLhOqi_S0rJqo4dJxT76dr2eHLL1QPivSr7qTtpMp8g1tjl2w4azKPKtxpcPxTF_qdnjE2NJlaGTXNZfyxmh1fzALSuG0EgN4xOpva7EoS5j1wJfxRlx_tcAybeGsRPAKa5i9jgGMKUqyfm3nYALiZMW_SRBdPSMUbBytP9d07osJfPd2Ej7DcaGAjjE62KsQj5gAh2ywO3tBhtL_ocbNGhVt0WXJtm-bBUkA94kH-Jn82jxzn0HkF7LrMJfoUDUScZO9pwFhSewxa-e7InbdrxueCRxaaP4y7-O_Ey6Cft_oko9Wb8tmzkbtDJJ8jPrY-7iaGwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر رضایی: دشمن روی تفرقه حساب کرده است؛ وحدت ما کمتر از قدرت نظامی نیست  دبیر شورای عالی امنیت ملی:
🔹
از ملت عزیز ایران می‌خواهیم در این رویارویی بزرگ، وحدت و انسجام خود را حفظ کنند و اجازه ایجاد تفرقه داده نشود.
🔹
امام خمینی(ره) و امام شهید ما، همواره…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/683480" target="_blank">📅 22:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683479">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a7026789.mp4?token=Wlo3eC9azqhXYAtOQKdJo8NpZflfQD8DkxN46bsVDsT5ptw061-_v23r5Rghf3sHtuCe-X_ivV3QAsXjJwmu05YXA0nZjlJJJUmz60e9jtQKKWFH_xpnvBI-lsozvVspVZ_soljZYOvvDT3RlH_3mMtXFeOyS2_qahi0mdMkaX0gGm2qmg0xFi_xttrG_6THO_Usgc50TV2SPTQyc3E84i6luKj-Ifc8YfypBt-rGkjo-PFn71bFN6ZKamY1DNfoLFkpFW8hYEh5cf_an_E8U7kgR-5k5AlUqrMUx_FvHE1m8iIKzP1tdWGHJ3oFAKQ-7_cgaWYLPaOfkv8lILJFm2qKjW-6En8lj4ofs4VfzvjYH-ihaLeqbphO7dlGnxUNJ-KbWHegZijIibo7rYg49TPGFGETzlZQ1C1zYb8FEUMNE4hweYIZEdPFNP_QaqavSFETuVWREyGh62tLhJLmvFQhMI-4nwBEzUpuxQhg7VagGAWledJtu7cy-KaHQGlEVKn2M8IMXpa9LzPZfE3Oy66EgDkCU-v56S739jlEZfXx37uaKK5YKSZbRuk4iC2xHzt0zeADGvCYDYT2EAVXmeX_82j0yWZseXOcFGJbN6dYihhQYReh7D6GVaMwD-IM1uEGtnidMiO76CXLYG7co-0NPyrxNKiTAx9b7NiWvjo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a7026789.mp4?token=Wlo3eC9azqhXYAtOQKdJo8NpZflfQD8DkxN46bsVDsT5ptw061-_v23r5Rghf3sHtuCe-X_ivV3QAsXjJwmu05YXA0nZjlJJJUmz60e9jtQKKWFH_xpnvBI-lsozvVspVZ_soljZYOvvDT3RlH_3mMtXFeOyS2_qahi0mdMkaX0gGm2qmg0xFi_xttrG_6THO_Usgc50TV2SPTQyc3E84i6luKj-Ifc8YfypBt-rGkjo-PFn71bFN6ZKamY1DNfoLFkpFW8hYEh5cf_an_E8U7kgR-5k5AlUqrMUx_FvHE1m8iIKzP1tdWGHJ3oFAKQ-7_cgaWYLPaOfkv8lILJFm2qKjW-6En8lj4ofs4VfzvjYH-ihaLeqbphO7dlGnxUNJ-KbWHegZijIibo7rYg49TPGFGETzlZQ1C1zYb8FEUMNE4hweYIZEdPFNP_QaqavSFETuVWREyGh62tLhJLmvFQhMI-4nwBEzUpuxQhg7VagGAWledJtu7cy-KaHQGlEVKn2M8IMXpa9LzPZfE3Oy66EgDkCU-v56S739jlEZfXx37uaKK5YKSZbRuk4iC2xHzt0zeADGvCYDYT2EAVXmeX_82j0yWZseXOcFGJbN6dYihhQYReh7D6GVaMwD-IM1uEGtnidMiO76CXLYG7co-0NPyrxNKiTAx9b7NiWvjo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام حیدری کاشانی در اجتماع بزرگ بیعت مردم مشهد با امام زمان (عج): اجرای قوانین اسلامی و زمینه‌سازی ظهور باید دغدغه اصلی مسئولان جمهوری اسلامی باشد؛ مسئولی که در این مسیر کوتاهی کند، به تعبیر امام، خائن و خطرساز است / حجاب به‌عنوان یک حکم قطعی اسلامی، باید در جمهوری اسلامی مطالبه عمومی باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/683479" target="_blank">📅 22:18 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683478">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnxL1y-KR7r17mnqYVcpVcsKQT-YANg8lEbU4kMSIdwQpRf3dy7k75VeTgbMtWXqViZIzQbarGJyI-5qU9ck2IcoLqbxEcQkA6PH1ApTFtQuRZJQpsGL4mfUK3k6mliG9vOLK2JYR0K2rbrinTfLBcSFjsFUIaDbUq7Vs5e-WIdI4tUtE8nbGSsGoYH87GArogczfOiqTrxPuftYEWMUQvtfSURysLX266MBqfd5mDA3Q_hrsfeylgXMg2mAa79WLuHmhXREkaLgYHBs7u6XHAapWji_RPvaXbrlOlewnCx9nShc5l7xMos6kIQkkux1-31Ysrb4rPGQ26pZkk8urA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در قعر خلیج فارس
فرمانده کل قوا:
🔹
بیگانگانی که از هزاران کیلومتر دورتر، طمع‌کارانه در خلیج فارس شرارت می‌کنند، جایی در آن ندارند مگر در قعرِ آب‌هایش.
🔹
بخشی از پیام رهبر معظّم انقلاب به مناسبت روز ملی خلیج فارس | ۱۰/اردیبهشت/۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/683478" target="_blank">📅 22:18 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683477">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
محسن رضایی: در شیوه جنگ و مسائل اجتماعی حتما تحول خواهیم داشت  دبیر شورای عالی امنیت ملی:
🔹
همه تجارب یکسال گذشته را حتما در نبرد آینده به کار خواهیم گرفت و حتما جنگ آینده متفاوت از جنگ تحمیلی سوم خواهد شد.
🔹
حتما در مسئله اداره شیوه جنگ تغییراتی خواهیم داد.…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/683477" target="_blank">📅 22:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683476">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c48885d423.mp4?token=WD6Ya2qNjmCjFUiW7WQoPPXpU34SwjIV71VWYZtm5_XDaKwBf2XT3PfoGWtE9jI1KmzJFF_eoVvenDnE16Qj9GlkkQIUI-NXyeOWepvcYSm7GOU9FSBCVPS6jiXMPZyxSLg7DWbgcxO-apF1H2rorZ9Weurpddy5WrrS1rg9ZZsMYQIcb1DiDAkYk9r71NvZCYBm-wMjbduKJZp4PxrQ2CZxuzeXBeLAFvch0Neph3olST7QYFm7fptPW6QOY75mQhvAoBAT0k4ICebbnKYx4EReod3Fne9KIsSS2f7d4gzuk7OnzrdBY5LJS8UN4rAeOMevGyU-TOMH-VnKL_KpCG1EbAcFi8oeuab4y1t4btU7YssBPD-b_LvZo8Plc3GuelyLwq_5Cm0H7pMdfH6azuPPhDB85m24xbDBjxu0DJMlgVTdZl6XOlsmXM4NYjU61DRMBEdvUXl0ebEPtbLRU7rFZ8OfAtrQvKIgV40YjKX8GkEEMwS_KNuMzSUJ_sgsojBRGZNhFoUPtuVAXVykNCXUUgJR6lLGy8lSz0sfI-Bsbjb6EFkakC6xO9CsNyEweeWJkxED3iYpxXUaeI472_YIqYy2HmjgzuWQJWrOwMpTu9RhHz1TTqwxgRPTaF2tLInzOnfHaRkUFOfZMLTvFP6-9VR1xUDQfeC6LImD1LI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c48885d423.mp4?token=WD6Ya2qNjmCjFUiW7WQoPPXpU34SwjIV71VWYZtm5_XDaKwBf2XT3PfoGWtE9jI1KmzJFF_eoVvenDnE16Qj9GlkkQIUI-NXyeOWepvcYSm7GOU9FSBCVPS6jiXMPZyxSLg7DWbgcxO-apF1H2rorZ9Weurpddy5WrrS1rg9ZZsMYQIcb1DiDAkYk9r71NvZCYBm-wMjbduKJZp4PxrQ2CZxuzeXBeLAFvch0Neph3olST7QYFm7fptPW6QOY75mQhvAoBAT0k4ICebbnKYx4EReod3Fne9KIsSS2f7d4gzuk7OnzrdBY5LJS8UN4rAeOMevGyU-TOMH-VnKL_KpCG1EbAcFi8oeuab4y1t4btU7YssBPD-b_LvZo8Plc3GuelyLwq_5Cm0H7pMdfH6azuPPhDB85m24xbDBjxu0DJMlgVTdZl6XOlsmXM4NYjU61DRMBEdvUXl0ebEPtbLRU7rFZ8OfAtrQvKIgV40YjKX8GkEEMwS_KNuMzSUJ_sgsojBRGZNhFoUPtuVAXVykNCXUUgJR6lLGy8lSz0sfI-Bsbjb6EFkakC6xO9CsNyEweeWJkxED3iYpxXUaeI472_YIqYy2HmjgzuWQJWrOwMpTu9RhHz1TTqwxgRPTaF2tLInzOnfHaRkUFOfZMLTvFP6-9VR1xUDQfeC6LImD1LI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
«قیام کن، دنیا احترام کن؛ به جمهوری اسلامی ایران سلام کن»
🇮🇷
▫️
حال‌وهوای بی‌نظیر مراسم «تجدید بیعت با امام زمان (عج)»
@Heyate_gharar</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/683476" target="_blank">📅 22:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683475">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2085dd4e0.mp4?token=XSF6PcEZ8d764vbwrn5GbU3sSDT4KqXMEhv6vwlTU5fqoM76fl4z1IuAoNr2mRMtZdhOemvarb5hFDSEOHV2t8IDR0SFgUXxufv79qK2vsbGxCsSO-QuYYucLeP0qwaKRGGoM0LRyPzu6_nWZ62-k0xdBMJb0EkLIIuJsSEW48MXPyd0XM8woC7hiLI8qHMW6Arhe5jhEHb9mwSIIi4AFIFThrSthDpMlXzHsWH9qW7-S5XPpiZlkTkGvPnttIiaTBB8XjRYjhvBJkDrb2by1Lo2XKNtxciRo3NI_8rz03tzxOIBsPNLX_lHBuNGC37l0KmDV8CG5hCy4YUSm5xx4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2085dd4e0.mp4?token=XSF6PcEZ8d764vbwrn5GbU3sSDT4KqXMEhv6vwlTU5fqoM76fl4z1IuAoNr2mRMtZdhOemvarb5hFDSEOHV2t8IDR0SFgUXxufv79qK2vsbGxCsSO-QuYYucLeP0qwaKRGGoM0LRyPzu6_nWZ62-k0xdBMJb0EkLIIuJsSEW48MXPyd0XM8woC7hiLI8qHMW6Arhe5jhEHb9mwSIIi4AFIFThrSthDpMlXzHsWH9qW7-S5XPpiZlkTkGvPnttIiaTBB8XjRYjhvBJkDrb2by1Lo2XKNtxciRo3NI_8rz03tzxOIBsPNLX_lHBuNGC37l0KmDV8CG5hCy4YUSm5xx4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: در شیوه جنگ و مسائل اجتماعی حتما تحول خواهیم داشت
دبیر شورای عالی امنیت ملی:
🔹
همه تجارب یکسال گذشته را حتما در نبرد آینده به کار خواهیم گرفت و حتما جنگ آینده متفاوت از جنگ تحمیلی سوم خواهد شد.
🔹
حتما در مسئله اداره شیوه جنگ تغییراتی خواهیم داد.
🔹
آمریکایی‌ها به مذاکرات، دیپلماسی و امضایشان خیانت کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/683475" target="_blank">📅 22:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683474">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d89fa5dda.mp4?token=vOV8s0Z3vYrdp-EYGvMsEETnG4MTrXUR_xJ8elX49vd1bbblKP4AFGJtchrih7Bm-sDPj1xzbQOCLa1mBNPbaVCuJzVzpggv39jcfuU9zG9KRhOw5KV5iBYw0YMBvogVoaJEH9Cl0ROEYEJGtdOG_YuL2zzFQltSlLtdiyCAdCQCM9NYvL68Vg6eOhv8Cag6kxC8h9Ub2UmJAqcugYAhp2-fH_99jvFem4xTca77fiYegF3LzJhdilYQwKNaDZRHkaJjmsIycesIxHYtE3pfo_0tjnhyiNAMRIXdwayp_ucKmBZdrfktJ4ADvi1PpLLcqHz_U6LWHMD7d8NHMwyPTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d89fa5dda.mp4?token=vOV8s0Z3vYrdp-EYGvMsEETnG4MTrXUR_xJ8elX49vd1bbblKP4AFGJtchrih7Bm-sDPj1xzbQOCLa1mBNPbaVCuJzVzpggv39jcfuU9zG9KRhOw5KV5iBYw0YMBvogVoaJEH9Cl0ROEYEJGtdOG_YuL2zzFQltSlLtdiyCAdCQCM9NYvL68Vg6eOhv8Cag6kxC8h9Ub2UmJAqcugYAhp2-fH_99jvFem4xTca77fiYegF3LzJhdilYQwKNaDZRHkaJjmsIycesIxHYtE3pfo_0tjnhyiNAMRIXdwayp_ucKmBZdrfktJ4ADvi1PpLLcqHz_U6LWHMD7d8NHMwyPTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: باید در رفتار دیپلماتیک ایران اصلاحاتی انجام شود
دبیر شورای عالی امنیت ملی:
🔹
در راهبردهای دفاعی ایران تکامل رخ داده و از جنگ تحمیلی دوم دائما درحال تکامل دفاعی - سیاسی است.
🔹
ایران امروز ایران قبل از جنگ نیست؛ این قضیه درباره آمریکای پرمدعا هم صدق می‌کند و تصویر آمریکای صلح خواه و بزک کرده، در ذهن جوانان ایرانی عوض شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/683474" target="_blank">📅 22:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683473">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/567f74a1d9.mp4?token=h8hAwwRmF6NtK4lQ3h9rGXIcskA5ir7zYfpohoNFqf0ObtM43RRPJNBmKCMGSqEK0Tr0Pl_AiW8Pan12_7OHJMnTbAS2zoYVoBRzceiMKiAAjs6j_Q6mP-UCj_n14eTGTsiwEz5Xznf8AJKmb-m0m40wLyt3it7IO84fkN42K90ZyhdoBVyRdDlEXk3musXjgXufKHKi_1LrsFe-SmuMFtPpiMLGRrF-5p0cjSbZYEyyYwMrEcCKHFgd15yvOORydPcwNHBBGZcEeEXM9qaNpf_1xS4yZb03FsZsaNLs7abhs-VpCopjgBnTR0dr_uXiZKxM4S_odNJWP5zrpg2uVUEhbTpASBKDxi6MHujQ9Wj5WPgTexKsWbV2aBYdfN-_5uv2upPaqhKmu-ZEZ_xTq9YjmHamTJJWms0b1yQppDHkJpSavqNycN9h20fMNy3hOiJzhiqGk65zeYV0bi1L1DrgUW8evc2LezcKx7XP_QoU3z41eCQCUhVai9vySab2V27yPXFB2EDvqrdfqK4pOVYo2h5r4YkDclLHU2ZnlIa0_0qwk_o9rO-XD5N7fAc6NI4nK-AWFWwkyV6McEPX-QID_7ITi5c70Hagz4cUwLvEj-37aBAkoyEIjaEhM-5-EG4OdO4xV7qC9QD5IwpoG-VJ5EJI-s1FkeJSJra0YBo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/567f74a1d9.mp4?token=h8hAwwRmF6NtK4lQ3h9rGXIcskA5ir7zYfpohoNFqf0ObtM43RRPJNBmKCMGSqEK0Tr0Pl_AiW8Pan12_7OHJMnTbAS2zoYVoBRzceiMKiAAjs6j_Q6mP-UCj_n14eTGTsiwEz5Xznf8AJKmb-m0m40wLyt3it7IO84fkN42K90ZyhdoBVyRdDlEXk3musXjgXufKHKi_1LrsFe-SmuMFtPpiMLGRrF-5p0cjSbZYEyyYwMrEcCKHFgd15yvOORydPcwNHBBGZcEeEXM9qaNpf_1xS4yZb03FsZsaNLs7abhs-VpCopjgBnTR0dr_uXiZKxM4S_odNJWP5zrpg2uVUEhbTpASBKDxi6MHujQ9Wj5WPgTexKsWbV2aBYdfN-_5uv2upPaqhKmu-ZEZ_xTq9YjmHamTJJWms0b1yQppDHkJpSavqNycN9h20fMNy3hOiJzhiqGk65zeYV0bi1L1DrgUW8evc2LezcKx7XP_QoU3z41eCQCUhVai9vySab2V27yPXFB2EDvqrdfqK4pOVYo2h5r4YkDclLHU2ZnlIa0_0qwk_o9rO-XD5N7fAc6NI4nK-AWFWwkyV6McEPX-QID_7ITi5c70Hagz4cUwLvEj-37aBAkoyEIjaEhM-5-EG4OdO4xV7qC9QD5IwpoG-VJ5EJI-s1FkeJSJra0YBo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام حیدری کاشانی در اجتماع بزرگ بیعت مردم مشهد با امام زمان (عج): دشمن پس از ناکامی در جنگ نظامی، جنگ اقتصادی و فرهنگی را در پیش گرفته و به‌دنبال ترویج بی‌حجابی و بی‌عفتی است / مطالبه از مسئولان، اجرای قانون اسلامی و مقابله با این روند است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/683473" target="_blank">📅 22:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683472">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی ایران: شکرگذاریم که خدا رهبری شبیه رهبر شهیدمان به ما دادند
محسن رضایی:
🔹
شکرگذاریم که خدا رهبری شبیه رهبر شهیدمان به ما دادند. با وجود اینکه خودشان دارای حزن بزرگی هستند و خانواده خودشان را از دست دادند ولی خیلی قدرتمند ایران را اداره کردند و در مقابل جنگ از ایران دفاع کردند. با شجاعت در صحنه دیپلماسی و جنگ حاضر شدند و سربلند بیرون آمدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/683472" target="_blank">📅 22:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683471">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgr_PTdFudVDyOVx9X5ecnQVUa1r6elIZDwkGXtgHN8RZfbagq0c0WMKqxaNXBGoEjlef9jYFgjqOgvd6QmGbBfGnhLFeI-A-zu7y29SJFAy0oowyIEEDTktQb6yemeUb99xlysXVuGN6JylPJ6G8PjVkmzuHOeolDUeoDyDPrPx97XSZuwrArV8Wa1tV1jPCEgTWJPDZP3b_MXfim3EOTF2lgaQmPAYqYhxikRyvwfyVGbyr-KqsSV3Ry7htKPSnwZWhLORqRC1i7Gzm1Pq8KmXvmmVKLEiE8KuKvpppf5nNanpD3oey1lDHtjaKZK0gWPTvBEKAXVnlyKVN1bGzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شما خنگ نیستید، شما فقط به اندازه کافی پول ندارید! | رتبه کنکور را حساب بانکی والدین تعیین می‌کند | پشت رتبه‌های برتر کنکور چه می‌گذرد؟
🔹
«آموزش رایگان» حداقل به صورت آنچه ما از آن به یاد داریم حالا به یک شوخی بدل شده، یک شوخی که راستش خیلی هم خنده‌دار نیست. وقتی هزینه‌های یک کنکور معمولی برای ورود به دانشگاه‌هایی که پر از صندلی‌های خالیست به رقم چهارصدمیلیون تومان رسیده شما نباید چندان نگران این باشید که عدم قبولی شما در دانشگاه‌های برتر به معنای این است که شما از بهره هوشی کمی برخوردارید، خیر! شما فقط به اندازه کافی پول ندارید!
گزارش میثم اسماعیلی را در وبسایت خبرفوری بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3239632</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/683471" target="_blank">📅 22:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683470">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
یک اشتباه رایج در بازار طلا؛ حباب منفی همیشه فرصت نیست
🔹
طلا هفته گذشته یک نشانه مهم به معامله‌گران داد و هر گرم طلا حدود ۶۵۰ هزار تومان زیر ارزش ذاتی معامله شد. در نگاه اول، این فاصله می‌تواند یک فرصت خرید به نظر برسد، اما رفتار یک سال اخیر بازار هشدار دیگری می‌دهد.
🔹
بررسی دو تجربه قبلی نشان می‌دهد حباب منفی الزاماً مقدمه رشد قیمت نبوده و حتی در کوتاه‌مدت با افت طلا همراه شده است. به نظر می‌رسد بازار گاهی کاهش احتمالی دلار یا اونس جهانی را پیش از وقوع، در قیمت طلا لحاظ می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/683470" target="_blank">📅 22:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683468">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ed41d78d.mp4?token=Che7KMlNYhtSdcZbRsksKNviDS8yh0lkgO373OjozgsYu-YFc_eYGvapSU_O7JgfMUg9OHB4PTAzZ08QYN4jc05jfrQ1_vXMmxkn9-oD7uji4xVvpPWFfZWWp3oFNYaJxW_LagT2flD_xCYBkUz1uWrA1wK7ddMoivVUmpHd-HUjzzHUZngoGEsb634Jq9hhWkLWjZPbxS-NDVX7Rfq9Ker03XAhpduytJLJTkp6bSj6SQNmwyc6vXyMFf_zUrQprQ_tZ-ky31u5CtPm5_c-de7ejVVWXM4_2PeK0PFA2-aZjJLqB5DL0vR69-pbYhzVgWk9yJ3sUPCNO0VQHYZ5iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ed41d78d.mp4?token=Che7KMlNYhtSdcZbRsksKNviDS8yh0lkgO373OjozgsYu-YFc_eYGvapSU_O7JgfMUg9OHB4PTAzZ08QYN4jc05jfrQ1_vXMmxkn9-oD7uji4xVvpPWFfZWWp3oFNYaJxW_LagT2flD_xCYBkUz1uWrA1wK7ddMoivVUmpHd-HUjzzHUZngoGEsb634Jq9hhWkLWjZPbxS-NDVX7Rfq9Ker03XAhpduytJLJTkp6bSj6SQNmwyc6vXyMFf_zUrQprQ_tZ-ky31u5CtPm5_c-de7ejVVWXM4_2PeK0PFA2-aZjJLqB5DL0vR69-pbYhzVgWk9yJ3sUPCNO0VQHYZ5iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
ای خسرو مه وش بیا
ای خوشتر از صد خوش بیا
ای آب و ای آتش بیا
ای در و ای دریا بیا
▫️
شعرخوانی حسین حقیقی در جشن «تجدید بیعت با امام زمان(عج)»
@Heyate_gharar</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/683468" target="_blank">📅 22:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683467">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
پزشکیان: آن هایی که دستی بر آتش داشتند، در شورای عالی امنیت ملی معتقد بودند این تفاهم‌نامه، بهترین تفاهم‌نامه است  رئیس جمهور:
🔹
در تمام تفاهم‌نامه یک بند پیدا نمی‌کنید که ما، وا داده باشیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/683467" target="_blank">📅 21:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683466">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEg17CHWCnWQ63r4W8R5pz9u0L0wV1ATCf8HZsR7RmAiNz1EPtwOk2vz39wSjoQ9mgxiVVKTi1qhf3jOlaFs6LoV8v2PC7B5zvTaAYugnyiUTdbSvf-ZV27gMsfl1tN-bMllEye3tuPjGBCByNwnJr0uZIcc1pXIodk3Lt6KNHxsHh1dE2vK9ptkRezVs0AHp4VZW5L-4Bp0EzJkZWWv9vWHc6TT43rqa4I4ZAe8kp_sFSPhfFev4EtcSXwPgIMvG_CgYvh6Kg2mb-iCcMzwMKB4QzlyiIb_5pLV_wJ7laMARJHkqHuSAIXTFtIvoWqeDNOO0DHZ_gKuJCCs3d7O0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمی از بزرگسالان ایرانی تحرک کافی ندارند!
🔹
در ایران، ۴۶.۳٪ از افراد بالای ۱۸ سال فعالیت بدنی ناکافی دارند؛ یعنی تقریباً نیمی از بزرگسالان ایرانی کمتر از میزان توصیه‌شده فعالیت فیزیکی انجام می‌دهند.
🔹
میانگین جهانی فعالیت بدنی ناکافی ۳۱.۳٪ بوده است؛ یعنی حدود یک‌سوم بزرگسالان جهان تحرک کافی ندارند.
🔹
گسترش سبک زندگی کم‌تحرک، افزایش شهرنشینی و کاهش فعالیت‌های روزمره باعث شده کمبود تحرک به یکی از چالش‌های مهم سلامت عمومی در جهان تبدیل شود.
@amarfact</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/683466" target="_blank">📅 21:57 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683465">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
۲ سوخت‌رسان نیروی هوایی آمریکا، بلغارستان را ترک کردند
🔹
رویترز به نقل از وزیر دفاع بلغارستان اعلام کرد؛ ۲ فروند سوخت‌رسان آمریکا پایگاه هوایی بزمر در این کشور را ترک کردند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/683465" target="_blank">📅 21:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683464">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
پزشکیان: مصمم هستیم بستر را برای آموزش همه آماده کنیم  رئیس جمهور:
🔹
با نگاه سلامت در تبلیغات شرکت کردیم. همه کسانی که سوادشان و علمشان کم است، از نظر سلامت در خطر هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/683464" target="_blank">📅 21:52 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683463">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1923648b7c.mp4?token=jGEGUeXF6dEoJUZwWNfQUkfymE0I2a4K9DoXFezNLVauL6Vf6W_Iby5HWT4ZEGxzcZMJ3qtKxXM1iVwQ-1_f6DhxO5uQ5OZJVQplUQjCfl0QxG0OoSZ9eZ329DFudiWtP5QgZ2LcNvzk68-hxl2UHMmRDx0oY6astl8qs54NvoC53xs3N5yJsL3GBD8atHg5asKyCWxIlP47PIs8Ek-9VuEnlQz7nlANT4E5yS2OxaMkvB_qEeVN4KDAeEOMebNKBlAz9a5za8PHfpHvMJbOgPmXlQraDcz-sqB60rpdktf5Q2B_KvVi0bGnbK5udxLG76vWCuTXnoUNhGUPrc_dHgHXFwruJ1Fr0qBKAF81PTEghK1kK3W8U7LsJpZJqMf5Qqo-A1boJWnLA2ums5Vos4TbfOIdaa6gtYSV2m9b2njNz3GtDSxZxJF34nRjCckOEtJrmrMbreSA8bWMxtTd0cL5MvnMgAGeEub_Fp8R9TgVNh8YW6Z9DMHinfjxfnfirMxtbgFHsralXFEhf7BnQe5Kwyu-z5p3lj3fY7z7uYS7GNMxUamPwV_8fM7OSVEnVSUHs1B0P_nziV22HM0_QJBgdqQ2oqOV5FYCTG4QQ8GkYyqwonCMNzwBqdFW3NeJ7o4BB-p4UuRh-EoZL9mELSHE1dxkZCCZSm1ns6ifW10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1923648b7c.mp4?token=jGEGUeXF6dEoJUZwWNfQUkfymE0I2a4K9DoXFezNLVauL6Vf6W_Iby5HWT4ZEGxzcZMJ3qtKxXM1iVwQ-1_f6DhxO5uQ5OZJVQplUQjCfl0QxG0OoSZ9eZ329DFudiWtP5QgZ2LcNvzk68-hxl2UHMmRDx0oY6astl8qs54NvoC53xs3N5yJsL3GBD8atHg5asKyCWxIlP47PIs8Ek-9VuEnlQz7nlANT4E5yS2OxaMkvB_qEeVN4KDAeEOMebNKBlAz9a5za8PHfpHvMJbOgPmXlQraDcz-sqB60rpdktf5Q2B_KvVi0bGnbK5udxLG76vWCuTXnoUNhGUPrc_dHgHXFwruJ1Fr0qBKAF81PTEghK1kK3W8U7LsJpZJqMf5Qqo-A1boJWnLA2ums5Vos4TbfOIdaa6gtYSV2m9b2njNz3GtDSxZxJF34nRjCckOEtJrmrMbreSA8bWMxtTd0cL5MvnMgAGeEub_Fp8R9TgVNh8YW6Z9DMHinfjxfnfirMxtbgFHsralXFEhf7BnQe5Kwyu-z5p3lj3fY7z7uYS7GNMxUamPwV_8fM7OSVEnVSUHs1B0P_nziV22HM0_QJBgdqQ2oqOV5FYCTG4QQ8GkYyqwonCMNzwBqdFW3NeJ7o4BB-p4UuRh-EoZL9mELSHE1dxkZCCZSm1ns6ifW10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
برای حضرت مهدی (عج) که دعا می‌کنیم، نوری از قلب او به قلب ما می‌تابد؛ شاید دعای ما، پیش از آنکه برای او باشد، مرهمی برای دل خودمان باشد…
▫️
بخشی از سخنان حجت‌الاسلام‌والمسلمین حیدری کاشانی
@Heyate_gharar</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/683463" target="_blank">📅 21:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683458">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s495bPe4mRMB6-C-sh8cN7lSuJUDDEamJsJrLhpFhqywJ6CBbxkq6ycOTfQkfE5suDyKNEHl_8XeDcs471SFT7ALiK2mbwjrt8vsHgWC1633P_gYqQRPkjnj-pdJxIa1Vfv-6PgWiA1UnvT3cdDn1Gx8hskXeWu641d9uub1i5qSLKUFES8QHCktUm7kJna5EH6w1nYTaTqgVePNSvCwiAQZADeE8t0NVZWQbRQT8l38Weqf-lOH70Y4msdQxtDS3cAWTv2bDNGkTIWdYrqWTEl4ctqiI7AOenXmlMoZS4yW-kttaYiXa1vcHdgjyqQVrCvfsPxAvHr3o8JU4yN0Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HRA3Gq3JcFTHU6uDet01vKj8d2-Wzya1yEODAlOWNHBpab2fsoL3JO7Z2nAEvHXmturNU7YyN30l3PdxXy1Fmho9NS-t-qlgO7tUW-YbE127tFlEYmBccxBe03wrBsleZzWF4tFAngFpOg5ddS2IjQeP_NsmOVSi5SgcgPw5_-c2v2xCY7DNMBhhrr6Ljhh8w6vbf6nOwRiNTSfB4IMs5mgWQfZKhV7Ki1NWEH3aE7z2YZlBveyilEWQ0TEdKXzP46aapHnJvIdZU2mnG6BV0klE5pboY-QSbmVeIqTDCP5m5TM_p8u5X_bbqbmYnfWrpw68__GKaUd7mQgehikwCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bck1LxMR_q54nqKNiUJk5srisNMImKOHycasS0mjSSzJuxB4OoWpGR7TdcQfnz3OkEC1cT1lFbizlhW874UK-IeAWED0QM5hf3K7hiZWZJJz7rkPGV_7d9DYNXwtwAZizdVhIiwC2g4EuWohgn_hXBlTniJHl9ap7l6KzwNOGlTYwTcq9jXkgcze5gIO2g7B8euQ47iX2FBMrhwHtENS5xeoFTqYxNW06kIinQ0dHxTxXLnL9RGfDAqiY8_PTzo__zs-H1CwmfCI5YCVX-f1kfEnsUNXg2jafP8zDjxkZshNGr32ulB_JXBmmkby__Fas7PtodrQCJj2h-0jLMI36g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IevKxaion_p4CHpD1Pl7tig0a5g9Vimsy9rFWQVa_HLOxEHg0pGcDvfvsQfw6pWe1DhgI4WqNLSPjsLYP7O3IMMa9A8Xt72TSO0Qhk8ENLixScfgq2DHW9pAvL-lzRF_6GiP_bdiridsym_CqVLykTfhsn2exlVNrmIguidNcFiLTJfOIpEb74sqWTe_Qvwq-gkA-L8AKHqjAerkIu9_4WsuDygIyaDwTAyXE2K8huxaTZtPGXn32inhljKO56ateLCYzcVDu3qRqCOWmqzvfiNzbazc2vBHJL8NUa4Ok7kBbOfdoGSNfgEEI8J-Ib2mYnkaDCg2Zf6xHMrNOGHywQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iigu49P2L1Ry4YnpFPdVwlkGAeMyClqKkEUMJjeDZycAUkgQyN0-I2TzRTe5R3LPuMJmvJ9WPLwvEli6jYcPsFx9CAk9nn_MIukzedNHHPVAXD09sgTIFnz02fLTlt4BNmb00b27aAmoqsO6SCVz9WsZuJtFpaemELdSU07mXggtSqYB4o-biKtfPvcpvj_EFOxi4b3XStLd_QMM9enjcwFWHwCDQB8eS8U1LsIapRJIzP_yo-FRNbgatukX5mnoy01pWClalJBYky4OtGSVriC9i4HkUrBpwRuIysV9DCtijKPkJhY70MjHhEWpXF6EejmK8l0A-YIc3HgqtN_8xQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کدهای مخفی که خروجی بهتر از چت جی‌پی‌تی بهت میده
#هوش_فوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/683458" target="_blank">📅 21:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683457">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
۸۸ درصد درخواست پول بانک‌ها رد شد
🔹
تازه‌ترین داده‌های عملیات بازار باز، شدت گرفتن کمبود نقدینگی در شبکه بانکی را نشان می‌دهد.
🔹
تقاضای بانک‌ها برای منابع در یک هفته از حدود ۳۴۸ هزار میلیارد تومان به ۴۸۳ هزار میلیارد تومان رسیده، افزایشی بیش از ۱۳۰ همت.
🔹
در مقابل، پاسخ بانک مرکزی همچنان حوالی ۶۰ همت باقی مانده است؛ یعنی تنها حدود ۱۲ درصد از تقاضا تأمین شده و نزدیک به ۸۸ درصد بی‌پاسخ مانده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/683457" target="_blank">📅 21:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683451">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P8dgmjpYj0WADlr47goQ12cb5W9_iVsOLw0-i-FLkCk-_c4KSWnWoUB5yOUvKYbQVRzfB1t9hkkUkCpzgnKGpcnVvkkbGHuw_HLKkAsvLzZ2Sq3Y4yjZrRafcIttxvYDu9n7DiSC2dmF8LlzpVScCxFbCc3SHg-kUne5-jHq6hjrOSgcKbhuQlDpLKcTZNq736aLZZnCdDPg3yHw1Eo0QXvDHnJ0GhrrGXGtL0mLxYWnCak2iqkmveqspFtguILqBz0mpFIfMAjOVlQfxyh3j0-C06OyOr5zR51A9xrrZalNXtbCn9yOU9V04pt79MGmjdbGzQSRUAoFcMA1XNf8-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fAsFCn_SAhgj_scOV9VDsvvYqAo5jyTQnLz4wThhjJr18tJU7jtLyhn_D3RMhCWewzEHVz7bnEOPmo0PCTJH8CkxMWdVS6pxLS22uT8pVLs4KidYqAiiMsbRs24_1LsMqZuEanBUHrujSr_ies8rjVCwG3kgBKD57GiYQApN0D3SmeXntA3qlB6n45Z7AS1ZXb63SKruWyTe7xKiov76IYARaXlxrQcK6SDgncOCNLm2xPVVeM4LAF0nBQnBoUE1b5UbfBR7cwrJtQBYM8SOAoJF0-cuRBoIlFUAZFv2xkED22lKu5sMcnxfWQDvOFnsDSos2IXW_bsu-ybtRqdMag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZP4LhmqDtPaS52716-4sN1szydrWAtOpvOOUw6QKGmc1FMoK8Ysyyj00UgVQzWF7jim_FlNW_QunmyTAg-t0tK2dNk3FFw8b6Pvvnjr-NmX527AU7afKoslUn8TqQuoM2vp8oulkVJAPCAPqBmd0qe3O8StNnrTbIFkGGXSUZLmQCMaWvpnvM6emZRaznBjgenV4kSOwJkfw3fnhELkScfi42tMon8FhXgEcoxJFy8sH_93X-UJU0J_Bx0ZS4h7qZXsWLtbeUr0fVn-SBEZGxrGk-sOnd1bLP_2Jhln5lGmmqbWbksTykDLmV2PTf-9prtUl4vU0rEUWwSXL316XgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y86J4glYhbAUQB8yBS2RsstAyUo1LGvuKM4-lYOf-JZ-P9rb_MBo8SrZ_Tuwz4qrySRgle1Tvwu7pfaljoGAaS6SAMkSBy-mpv3PZ2rOBezUuZ5t4P6vxUbL3rbjshshCt8BUKg-XLL5wi4hoWNp2grbSA5wvJ72kvMGM_lf-nAzw8BtJ3rdCZtQiPtFX8BpbLuzvmbdHuz5eBtfVOcLt0uGNvhavZU_4Yn9GLL2l4_2rXJQfgq6FZrOdtJUWkT4VtB6akDkng_J7PHKZ7Iap3M3aCRXugTJJDhe7bGI8mkpVRjjdfHaAR2eMGD8ycmnpIlwV7eiqLC73_sTAELLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mq8wn4EK-xEied_5f0NRHtgMC7hYVVAy2q8wqSzFe4WSnW9IA_tnZP58bNMcrYFlQPh-uw41OKYrnmMynsIHJD6ExM9sdNSRy4clbDPEc0wRtecCvZTzD-eCkPmvoWqnIVhUsJ0pG29OJ-5TIJKjHYqw3kpUg9a52a4wOGnvz4gLgmS7-lTbdRewQD4quSvNhbLwHWgACtIJbNzbv-QAR-qXS0vxHDX7BHdxBpYoX58os82gSEq2BY8nhH4kE0T1-fy1g-kl9sk1KmilI7LwM98swD1BYrCGuDcKb-A3QkwvzOfBLDvAp7qcDqdE4IHJHAA1rtinIQd-HowEY4nRmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
یا مهدی، نامت شده حرزِ وطنمان؛ به عهدت می‌مانیم، برای ایرانمان
🇮🇷
▫️
مراسم جشن تجدید بیعت با امام زمان(عج) با حضور عاشقان ولایت
@Heyate_gharar</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/683451" target="_blank">📅 21:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683450">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
یمن: تحریم‌های آمریکا علیه حزب‌الله مشارکت در جنایات اسرائیل است
🔹
وزارت خارجه یمن اظهار داشت آمریکا در تقسیم کاری آشکار علیه مهم‌ترین مؤلفه لبنانی یعنی حزب‌الله تحریم‌هایی اعمال کرد و این حمایت آشکار از دشمن اسرائیلی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/683450" target="_blank">📅 21:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683449">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
پزشکیان: اختلاف‌نظرها هست، اما پای وطن که می‌رسد همه کنار هم هستیم  رئیس جمهور در  مراسم گرامیداشت روز پزشک:
🔹
دشمنان تصور می‌کردند اگر حمله کنند و در یکی دو روز بزرگان ما را به شهادت برسانند، می‌توانند کشور را قطعه‌قطعه کرده و از هم بپاشند.
🔹
اما هرچه زمان…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/683449" target="_blank">📅 21:36 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683448">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d124afbd.mp4?token=dKqxk8ca9wDY_uoMpGALXWVS9vIt_JgNvKufRYnOB7x45JRa5oeQzrSAeGdbfc1aMY3nplcuepARucbiseri77ploKiLYTAHZJn_C_hR2aYPry3e6gjBSCCNVn_tLya3v-k1gI8DFPRP3hva0GJuhoYl6kA0d9QvIx6SrIb1SA7NVHQiACsnMDziIk5FwQKqdlPR-XUEMie8P9vA73xknTsunJzSqhc-W6qPy4ShAPn6GRgPLL8d5MwPqYwSlurS2vHwfAAF55OlYVDOhNoABur1cbwwYomp86w0zicuAEgmZ2UvNrOfaGof5iMkby6NKBFpFeA3fmLxnZ3DgmQ0oVeECQjEgyQUEkQQoIWqW8p_nxwnVdhE914F1r5kAMAbdJ0oxL7p66dCe3PzkZf8zuhqhlQH2oJ6rqsiEL8Hifnu6SHi9WJKCaiD8hY6f7MOCvporDV6jcp6fPXukrV3GcWTLf3Fil0RKFUEo5s6Nn24cbyVlXg0zAhOlsbudAcLlAvVPF56JUpJFbHHfgKV3TnNgenLbJt53hnaUqG_o9RB33JT7TZwrf7l5Y5p2EBpntKgvIO5VK7oeG2vturY3U2c1flijiL1YZzk-rF53O34vJ_Awr92pBTmiB_ibilNtPsoIqu0IZbWwN6GtUQzJj2XYkAcYQBdcSBguELly5c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d124afbd.mp4?token=dKqxk8ca9wDY_uoMpGALXWVS9vIt_JgNvKufRYnOB7x45JRa5oeQzrSAeGdbfc1aMY3nplcuepARucbiseri77ploKiLYTAHZJn_C_hR2aYPry3e6gjBSCCNVn_tLya3v-k1gI8DFPRP3hva0GJuhoYl6kA0d9QvIx6SrIb1SA7NVHQiACsnMDziIk5FwQKqdlPR-XUEMie8P9vA73xknTsunJzSqhc-W6qPy4ShAPn6GRgPLL8d5MwPqYwSlurS2vHwfAAF55OlYVDOhNoABur1cbwwYomp86w0zicuAEgmZ2UvNrOfaGof5iMkby6NKBFpFeA3fmLxnZ3DgmQ0oVeECQjEgyQUEkQQoIWqW8p_nxwnVdhE914F1r5kAMAbdJ0oxL7p66dCe3PzkZf8zuhqhlQH2oJ6rqsiEL8Hifnu6SHi9WJKCaiD8hY6f7MOCvporDV6jcp6fPXukrV3GcWTLf3Fil0RKFUEo5s6Nn24cbyVlXg0zAhOlsbudAcLlAvVPF56JUpJFbHHfgKV3TnNgenLbJt53hnaUqG_o9RB33JT7TZwrf7l5Y5p2EBpntKgvIO5VK7oeG2vturY3U2c1flijiL1YZzk-rF53O34vJ_Awr92pBTmiB_ibilNtPsoIqu0IZbWwN6GtUQzJj2XYkAcYQBdcSBguELly5c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
شعرخوانیِ احمد بابایی؛ در جشن تجدید بیعت با امام زمان (عج) از «قرار» برای صاحبِ قرار…
@Heyate_gharar</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/683448" target="_blank">📅 21:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683447">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تمدید مهلت ثبت‌نام دانشگاه امام صادق (ع) تا ۶ شهریور
برای نخستین‌بار، کدرشته‌های دانشگاه امام صادق (ع) در فرم انتخاب رشته آزمون سراسری قرار گرفته است؛ اما درج کدرشته به‌تنهایی کافی نیست و داوطلبان باید ثبت‌نام اختصاصی خود را نیز در سامانه جذب دانشگاه تکمیل کنند.
🔹
مهلت ثبت‌نام تا ۶ شهریور تمدید شده است.
🔹
حتی داوطلبانی که هنگام ثبت‌نام کنکور گزینه علاقه‌مندی به دانشگاه امام صادق (ع) را انتخاب نکرده‌اند، می‌توانند ثبت‌نام کنند.
🔹
پذیرش بر اساس رتبه کنکور، سوابق تحصیلی و مصاحبه انجام می‌شود.
🔹
داوطلبان گروه‌های انسانی، ریاضی و تجربی امکان ثبت‌نام دارند.
🔹
تحصیل، خوابگاه و امکانات رفاهی برای دانشجویان رایگان است.
ثبت‌نام و تکمیل اطلاعات:
https://gzn1.isu.ac.ir/landing/info
ارزیابی و دعوت به مصاحبه به‌ترتیب تکمیل پرونده‌ها انجام می‌شود — هرچه زودتر ثبت‌نام کنید، زودتر در نوبت قرار می‌گیرید.
#انتخاب_رشته
#کنکور_۱۴۰۵
#دانشگاه_امام_صادق
#ثبت_نام
#ارشد_پیوسته</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/683447" target="_blank">📅 21:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683446">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e705d04a6.mp4?token=ghMyLn8VaWFYCIk9QhM0kOFDIXHs_AZ-wxTpBGgtRo6KCg-FK0v3XrsGCQoCuQG_bVZz6W9VUaAq90CucBZGnUlMCG8UV2u7yS6KMi1O4a8z81Ureg4zJ4kpek7BVTI75aKOX8w7amU-mdXuC1KKsX6e37Q97u_0mqjBuo031nTT0q4C2zvQo1ca0s3_u0z1p-MbCoA48BZXZL4Lu4qKFSknKpi8M2936jX67NO7ULCJU1a2QJ5jSt_DT04u-dr8fQkomU4SIm5aDdONANgPu2j0keMSZ3-AVa4aFFwvUIZMsJzRsWRokShFyC9RHCmpGvASbR-HjyDfO4443VYEoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e705d04a6.mp4?token=ghMyLn8VaWFYCIk9QhM0kOFDIXHs_AZ-wxTpBGgtRo6KCg-FK0v3XrsGCQoCuQG_bVZz6W9VUaAq90CucBZGnUlMCG8UV2u7yS6KMi1O4a8z81Ureg4zJ4kpek7BVTI75aKOX8w7amU-mdXuC1KKsX6e37Q97u_0mqjBuo031nTT0q4C2zvQo1ca0s3_u0z1p-MbCoA48BZXZL4Lu4qKFSknKpi8M2936jX67NO7ULCJU1a2QJ5jSt_DT04u-dr8fQkomU4SIm5aDdONANgPu2j0keMSZ3-AVa4aFFwvUIZMsJzRsWRokShFyC9RHCmpGvASbR-HjyDfO4443VYEoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: اختلاف‌نظرها هست، اما پای وطن که می‌رسد همه کنار هم هستیم
رئیس جمهور در  مراسم گرامیداشت روز پزشک:
🔹
دشمنان تصور می‌کردند اگر حمله کنند و در یکی دو روز بزرگان ما را به شهادت برسانند، می‌توانند کشور را قطعه‌قطعه کرده و از هم بپاشند.
🔹
اما هرچه زمان گذشت، برایشان ثابت شد ملتی که به آب و خاک خود پایبند است، به این راحتی زمین‌گیر نمی‌شود و تسلیم نخواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/683446" target="_blank">📅 21:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683445">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Stak_Ju4503Yb7c5Q3AQ1e0MeMBkmWzdo6TNf7ym-kLaD4oGIwS2UBG5Os35MC7vRQmnRAeOYMfs4NSwAN1WpcLVTGR5YuHtXBjMUaQUabqDY4EMer5lyuOiQEW0VJlMvnCY-93xX4QLjKLUn0zf_r4dsnRsh2V6yJYSpskPCbVSQF0MMi4P2UakLVuC5Ee5lfaNE1qWI6Wb9ZzfyCq_Z22qf2qQ6LH728Wz8lScahvyyPgowv9Ye1BdrhvTvVJuavZn2NtEFpBUrx2ojnyDsetCIP1J1wpGaUPnM9hbP9oEC7Z72Uy54Gu5NWzc_hAQsJhB5ywC2hKyUNf6cgtZfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشست سران قوا با محوریت معیشت و تحولات منطقه برگزار شد
🔹
نشست سران سه قوه به میزبانی رئیس‌جمهور و با حضور رؤسای مجلس و قوه قضائیه برگزار شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/683445" target="_blank">📅 21:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683444">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
سیدعلی خامنه‌ای، پس از تو هر خبری جز قصاص بی معناست
به خصم، زندگی خوش حرام می‌خواهیم
علی‌اصول، فقط انتقام می‌خواهیم
🔹
شعرخوانی حماسی احمد بابایی، شاعر آیینی در اجتماع بزرگ بیعت مردم مشهد با امام زمان (عج)
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/683444" target="_blank">📅 21:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683443">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
الجزیره: در ایران بیش از ۹۰۰۰ شرکت در تولید سلاح نقش دارند
ادعای الجزیره:
🔹
ایران در حال بررسی چگونگی واکنش به اجرای برنامه‌های اقتصادی آمریکا است. مقامات نظامی گفته‌اند که بیش از ۹۳۰۰ شرکت در ایران در تولید سلاح نقش دارند که به این معنی است که حملات آمریکا و اسرائیل قادر به نابودی این بخش نخواهد بود.
🔹
تولید برخی از «محصولات راهبردی و اولویت‌دار» در ایران از زمان آغاز جنگ بیش از سه برابر شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/683443" target="_blank">📅 21:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683442">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
ابهام در پرونده کشف جمجمه ۴۱ آهو در چاهی در شاهین‌شهر
فرمانده یگان حفاظت محیط‌زیست استان اصفهان:
🔹
شواهد اولیۀ ماجرای کشف ۴۱ جمجمۀ آهو حاکی از شکار غیرمجاز است؛ با این حال، تعیین دقیق تعداد تلفات و بازۀ زمانی دقیق این شکارها، نیازمند بررسی‌های کارشناسی توسط متخصصین حیات‌وحش است.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/683442" target="_blank">📅 21:24 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683441">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ناشران و کتابفروشان، وام کم‌بهره می‌گیرند
شهاب دارابیان، مدیر روابط عمومی معاونت فرهنگی وزارت ارشاد در
#گفتگو
با خبرفوری:
🔹
ثبت‌نام تسهیلات کم‌بهره ناشران غیردولتی و کتابفروشان سراسر کشور از شنبه ۳۱ مردادماه آغاز می‌شود.
🔹
این تسهیلات پس از بررسی کارگروه تخصصی و در چهار سطح، از ۲۰۰ میلیون تا یک میلیارد و ۵۰۰ میلیون تومان، ارائه می‌شود.
🔹
ناشران متقاضی درصورت داشتن پروانه نشر معتبر و قانونی، فعالیت مستمر و اصولی در سه سال اخیر،تولید و انتشار کتاب حداقل ۱۰ عنوان کتاب بزرگسال یا ۲۰ عنوان کتاب کودک و نوجوان در هرسال، از جمله شرایط دریافت این وام می‌باشد.
🔹
همچنین کتابفروشان سراسر کشور در صورت داشتن سه سال سابقه فعالیت مستمر فروش کتاب در واحد دارای مجوز، فعال بودن کد بیمه و پرونده مالیاتی و همچنین تایید صنفی و اجرایی از سوی کارگروه ارزیابی می‌توانند برای دریافت وام اقدام کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/683441" target="_blank">📅 21:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683439">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
حرمتش واجب است در دو جهان
هر که در فکر احترام علیست
از یمن تا به شام معلوم است
هر چه دعواست پای نام علیست
🔹
شعرخوانی حماسی احمد بابایی در اجتماع بزرگ بیعت مردم مشهد با امام زمان (عج)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/683439" target="_blank">📅 21:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683429">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d9p-LFTdFnVsPDhIZt2KugjurSbOlOCsgTitvWm5ebx7bwewwIEWMxYY-9KIBtMZt-Kk43A_HUAO6JzmgRPoQsEjEz7e_4sDyDNbPm_vMPaf19Sb-anlLBQrrAwO94snOdatXwRsz8VAkQkAB52u8dYDhA2z0fUCwUrMVgra-JYhwT9-PnFykk158fv213fbufR8LN3OwhT1y_qbpcY_SoZDr5h9nrPF8y_bSg83ANk6_-XLGn8s-PMZ0r6VTX1D8lniG0duPSbN2bSay5YmnVWc_yWljQ-plng29fwl1XNzmGfj-FK0mEdz5mVrUYPXyPfs3aJqKdqKMcaHJzRc4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qd1Bf5nl0KhDZea7xyC2LIUfpeFFPwkzVLW8RFD77QUpK7aA_zvIj48_Mc3XbGmx_r1oTn4vKdqnbvS_SiyYGYUFlcS5Yv4BiDoJTh_RE1u2Otum88HViBj-Lrq89_-LeXPb0qAw2qq63W0iaPMjp2Ft9NZGxEP2puIHGniayG5yabEeo6wUTeBJpfEePTIKppAtCmS864AE91j9MHTx2ZosNi9lj2gG-8hxio21VbWKlbFRwbvLZzRtmn81ISF7VHiEuoq82QAXYoirjnK6fX7tS_tEz7VBa6tV8INOg-IeVUY-SvL968PxgfFEL_pJyTZG7Wzth43mCJXYfQ3P_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l1OQ3YVXTkeFi8HAcBKtioBh-BxuhlZiLTzOI-InryUdrRnI-ijH1KHeB0DZr9pz3TVXLWXsx9xVnATNh-cKWY95ee4aJtkNzCD-ALDU85BTeaAMBr1CHJ40oGvrqsLNdVKUp7_k62nekWoFXoQXRK27IQh8KcfGlQTLX2DWDCVo3Fn6roE2Wk1Gw_wF_fi-POiW0gO304njKjRYu5OuMHWDU6iQY9RbKepxYBY2UJjDGGZqFCBA9cqupqYElwGHk0Df1YbmAzY3OAqXQ-BnixZXdUglHnNfXzvCKyxD4VynOaVT4X96_pOpIEoI4XmwsHJrxiRrvclvYL9MdhwGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jh1ovXk8Y5zG20bPhxRjglg-G4-vQMpVdtcpqTpgyarKV2uOlDCZh8KYMvn12PH1U_F7uPLqlM8K1FmZVfHl_NOzey4ER95yCucvqrRWyd4UHXfmcdK0LixWwCoH7hheA_whAwqflPPbKZcg9oxKT6xFZWubUOUkyZNgkEAOGjOX8W2qyzK6yh6K8fQE0Pc7xLjgKktSuR_Ri2_nMJcu5X9D3cEiRDeMEuQ8YFO_UtnkNxiWP2VVfaKSI5CQuKclpWYYfi2yks7tTWRoMYLUD56LkD55w7BPgYi6sDI1_vwIxFsYsQ4xsow0ALhE4DGhvquPKH0MJjEj3VPwqpYqPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DW8uREUUrWs5drNyt_BQY0Wo76kVpNo6yURrSTmUgSeyIUosKphgTKeM92ojTbPxw8pb4sbLT4NIOrNAFuo2DRM5eOi1xaWtRN7-5kyURsIlOhK-Po0zc-gS7xwwEGCFFhxiYkMHs-YAedabQ8qTDKl3T15KpjOpamjCavRyz4xu1jmLcepTpQtq0lLXNmve2NYKmdEJBTDA1oREy4AO3MLzVgluaOB1HuLvqTJniokXuSHzFCQnqJTwgMBN6aZfAJ990mUmKN_xgD_m4s2p8L3s3yR4NGfDPXQyEtbm5ZpVZtybuBw39OElTZVNqIQwvlpxgzBS074MgF0dP6IIVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
گزارش تصویری از برگزاری باشکوه تجدید بیعت با امام زمان(هم) به میزبانی هیات قرار
@Heyate_gharar</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/683429" target="_blank">📅 21:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683428">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
مرداد، بازارها را بالا کشید
🔹
پنجمین ماه سال با رشد خیره‌کننده ۲۴ درصدی بورس، افزایش ۷ درصدی طلا و افت حدود ۳ درصدی دلار به پایان رسید. در آخرین روز مرداد همه این بازارها افزایشی بودند.
🔹
البته صعود شدید انس جهانی در افزایش قیمت طلای زرد در ایران بی‌تاثیر نبوده است. توجه به فشار تحریمی و محدودیت‌های هرمز، ریسک تداوم فشار بر بازار انرژی بالاست/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/683428" target="_blank">📅 21:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683426">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
نتانیاهو: تا زمانی که من نخست‌وزیر هستم اجازه نمی‌دهم هیچ کشور فلسطینی تحت کنترل ایران تشکیل شود
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/683426" target="_blank">📅 21:11 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683425">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94ec87207f.mp4?token=kz2CUmZVO2WXqOHbfb-BPH35naKvWcJOBosqxmpRObUvHuwqwwQPrHRN-d6xN58swkpW41Jw2-eGpDtoDtdUQZioInO2KvsOPSCYN5_7-cih8-PPJ1tLNdR2_KoYZMR9yolfUma4yghl_ezG2otwG3X7Rq89gNu-6wyiGqb6qfscZ75_o8-FOY4kXG5CTGyVM5SzcX2AIK8EU0shREEwAU8CVLW76S-ibVS0OSebjp5br15Vrn-PRJ9AsIN9FepwJ6KKrjiBtdNvhJ1aMfQkCJskRsIz80jDgAuRRUhDrubDpboKtqZOrHi3shfNsc-fCy5kofnzMm2LdqxxSzu6Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94ec87207f.mp4?token=kz2CUmZVO2WXqOHbfb-BPH35naKvWcJOBosqxmpRObUvHuwqwwQPrHRN-d6xN58swkpW41Jw2-eGpDtoDtdUQZioInO2KvsOPSCYN5_7-cih8-PPJ1tLNdR2_KoYZMR9yolfUma4yghl_ezG2otwG3X7Rq89gNu-6wyiGqb6qfscZ75_o8-FOY4kXG5CTGyVM5SzcX2AIK8EU0shREEwAU8CVLW76S-ibVS0OSebjp5br15Vrn-PRJ9AsIN9FepwJ6KKrjiBtdNvhJ1aMfQkCJskRsIz80jDgAuRRUhDrubDpboKtqZOrHi3shfNsc-fCy5kofnzMm2LdqxxSzu6Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه پخش سرود ملی در اجتماع بزرگ بیعت با امام زمان (عج) که هم‌اکنون در مشهد در حال برگزاری است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/683425" target="_blank">📅 21:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683423">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac30e14d45.mp4?token=Ki4u5nkZ8mH-La3G2ql6xAa79YGT_kVjjoNKNhg0MXSGglmvQNPIpOj4yjoLW9OApml_ObgD6CCZiGDv-fJ54n7kopnkhuuzufkv0WGDuhZPiJRXCU3fFuyNde-_xHp2cosMkesJlRe3zfxg8rrCPNl_ZouNHamrWsxJaWOZe7XHoG9hClvWtpbbEyESrYoXFwQD03hXhEScrON0K0ejLqhjxX3m75OH-vtvEfUtD_gYXwCzujA5fb4cJuQyo4mkSSM8vyqYrGV45zOv-qAUTh8DjVq7ACdsptFWI1wtSN6SiAA9IGrMscKluxVPoscuCRjYGJFECiK6kNKLMKi3yizN0vxaajQ_ZYDWbqadXcZdsTooqcUxW6pMpmcWLOQHD3lq8xlZQ2-lqZEfws1kyOChkfEze75VLm3L9qVWSEOX8G4D1gFAJsWbTDp5j0PS8CxDk96cwZnkivzPcX9WBZSFk-VS7aC8y-UQh1nb7bizK2aD01vOStnglotWwW2CWgWO4_c2I1RZttDFNL0lJotSwp5zNZpC-WwjuU1aLcMQjoQFAJkYWD5z8_CSbLL4o-D_6AYu65yTj_ngdeWQGSXYWzJhDZIvLcR6QdK3mX-Ig9QWhpa5-Ed7FpAOuT3o0JDCX_8VmJr4E-9xJT5M9qZoW37H8GO7Z5nwitYkTtI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac30e14d45.mp4?token=Ki4u5nkZ8mH-La3G2ql6xAa79YGT_kVjjoNKNhg0MXSGglmvQNPIpOj4yjoLW9OApml_ObgD6CCZiGDv-fJ54n7kopnkhuuzufkv0WGDuhZPiJRXCU3fFuyNde-_xHp2cosMkesJlRe3zfxg8rrCPNl_ZouNHamrWsxJaWOZe7XHoG9hClvWtpbbEyESrYoXFwQD03hXhEScrON0K0ejLqhjxX3m75OH-vtvEfUtD_gYXwCzujA5fb4cJuQyo4mkSSM8vyqYrGV45zOv-qAUTh8DjVq7ACdsptFWI1wtSN6SiAA9IGrMscKluxVPoscuCRjYGJFECiK6kNKLMKi3yizN0vxaajQ_ZYDWbqadXcZdsTooqcUxW6pMpmcWLOQHD3lq8xlZQ2-lqZEfws1kyOChkfEze75VLm3L9qVWSEOX8G4D1gFAJsWbTDp5j0PS8CxDk96cwZnkivzPcX9WBZSFk-VS7aC8y-UQh1nb7bizK2aD01vOStnglotWwW2CWgWO4_c2I1RZttDFNL0lJotSwp5zNZpC-WwjuU1aLcMQjoQFAJkYWD5z8_CSbLL4o-D_6AYu65yTj_ngdeWQGSXYWzJhDZIvLcR6QdK3mX-Ig9QWhpa5-Ed7FpAOuT3o0JDCX_8VmJr4E-9xJT5M9qZoW37H8GO7Z5nwitYkTtI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
اى وارث ذوالفقار مولا برگــــــــــــــرد!
◽️
اجرای ویژه موسیقی توسط گروه سرود دختران در مراسم تجدید بیعت با امام زمان(ع)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/683423" target="_blank">📅 21:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683421">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس مرکز امور زنان و خانواده وزارت کشور: قانون مهریه باعث شد زنان مهریه خود را به اجرا بگذارند
پروین داد اندیش، مشاور وزیر و رییس مرکز امور زنان و خانواده وزارت کشور در
#گفتگو
با خبرفوری:
🔹
یکی از بانوان نماینده می‌گفت موبایلم را که باز می‌کنم زنان زیادی هستند که مهریه خود را به اجرا گذاشته‌اند که تا این قانون نیامده است، مهریه خود را بگیرند.
🔹
بنابراین به آقایان گفته‌ام که ما یک جنگ داریم و شما هم دارید یک جنگ خانوادگی راه می‌اندازید.
🔹
در بسیاری از موارد این قوانین از محتوای واقعی شرعی خود که به نفع زنان بوده، خارج شده است.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/683421" target="_blank">📅 21:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683420">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb137f4e5.mp4?token=ii7IcTJ-bWzQzyNQfkvh8D5GVLho9nrX3J1kc0PoBo61oxJupg4s2zOemItzuWLy4Ji9aG_SQQdSjTqKnVafCGW1OCOC7SCMDfd6VWMG6MHp2ACqK8b2sh8WBQaWVS0hUrhoj61ubZQVJ7C1HfupdTG1yl00VimgKNCkkqwYcCUoKoTRNQbk2lUbdZNNy9mvhwlJBQP0ylZDePt0pojRC1OM3O9xEWLcxAkmh-jbQUTp7UdJRoP9heoTVfqD12SSuKsOFLSAz1XoMydorar6xN7c-gAnSGwPLIYAydmiLZpMBXLvKmDEUHYcrlQ8MfuoKucU8epU_yjMm4MLaYM19buShFUBXT8kEwOdfQn-JpIZ0BxEaDo8JI2pXXxHbyHKP6ZWrZbZLzppFtIqhUwZM3trgzncHt__EQTzwBIpIv3JRL-gKg5c9irDhDX7E7RPO9Faybpr8vspa03QOyGoeT9JOrrlWOKlFhwz3nOT_rsEiyYqS14EDlHo4tbrLPul5u_fBHh4A6fsaCORwiFAlaI8sj9sQtJDHWdnloWLS_8wWamyPUCO8fRCP996y5SO2fSdfMX7DxJRsX-Kz_KK5gzbkfnrmdBbrVSmxcDGRLGlS90ftVHLEBHOAZpPs1TpyXtstFRUlybFaaIdR5hJg6EMKqv95GD6BdYTyhsRUGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb137f4e5.mp4?token=ii7IcTJ-bWzQzyNQfkvh8D5GVLho9nrX3J1kc0PoBo61oxJupg4s2zOemItzuWLy4Ji9aG_SQQdSjTqKnVafCGW1OCOC7SCMDfd6VWMG6MHp2ACqK8b2sh8WBQaWVS0hUrhoj61ubZQVJ7C1HfupdTG1yl00VimgKNCkkqwYcCUoKoTRNQbk2lUbdZNNy9mvhwlJBQP0ylZDePt0pojRC1OM3O9xEWLcxAkmh-jbQUTp7UdJRoP9heoTVfqD12SSuKsOFLSAz1XoMydorar6xN7c-gAnSGwPLIYAydmiLZpMBXLvKmDEUHYcrlQ8MfuoKucU8epU_yjMm4MLaYM19buShFUBXT8kEwOdfQn-JpIZ0BxEaDo8JI2pXXxHbyHKP6ZWrZbZLzppFtIqhUwZM3trgzncHt__EQTzwBIpIv3JRL-gKg5c9irDhDX7E7RPO9Faybpr8vspa03QOyGoeT9JOrrlWOKlFhwz3nOT_rsEiyYqS14EDlHo4tbrLPul5u_fBHh4A6fsaCORwiFAlaI8sj9sQtJDHWdnloWLS_8wWamyPUCO8fRCP996y5SO2fSdfMX7DxJRsX-Kz_KK5gzbkfnrmdBbrVSmxcDGRLGlS90ftVHLEBHOAZpPs1TpyXtstFRUlybFaaIdR5hJg6EMKqv95GD6BdYTyhsRUGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
شروع رسمی «مراسم تجدید بیعت با امام زمان (عج) و رهبر معظم انقلاب اسلامی» با اجرای امیرمهدی باقری
@Heyate_gharar</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/683420" target="_blank">📅 21:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683419">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ادامه جنایات اسرائیل در منفجر کردن و تخریب زیرساخت‌های جنوب لبنان
🔹
صهیونیست ها، ساختمانهای دیگری را در اطراف شهرک میس الجبل و منطقه المشاع در اطراف شهرک المنصوری در جنوب لبنان منفجر و ویران کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/683419" target="_blank">📅 20:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683413">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qExBhYiNqHoXTipgCzDorf63pMELK3YGhOiWGjzy3cYS2KzaPS-5ZqDAZMc5X3Euaianmp8rVy74D2rPt8Ogy6wzjle9ktjnj3iU3kAG_dQmifPHzjtQQz7omdhL3g2-B5kYSpczeiGyTg6FNLy_68QVkNYEQM6qvVz_XabZTzZox-2JpDIgtnzx1vw0sH7WO4Q5sGLNjMQNMKCVlHFfyggeXBBhQdP_k618yLH6iJeuQsiDdtH6sGyGaq8cvn-3r788XY0fdguXd5vHLHSR71HWyGp6xvNOsvNCKud9GLzWwigR_HnPulnwqnWEHDK-wh5MkdZU86uB1NlGTShTsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pxevp3SJkt0Dzq7i5eBPYS9eHW003H2gEu7X1YQ6B-dz50Vp7ME6qTB2XGTonCkD7SEWz9itnGnBeVxH4KUSbgp157eFwZ-oIPz3RAvjK-ZGD7qVwlAdqtRw8G_2j4_igWJslEEgY8jCTCwppt_gWSHp1yFbussVH28kXTmbw1GjPGn2QFtHOvxXEAD7ZfrvXddWG70W35SHfAO3_9J-FeTwIekX09OhLIzocEgRpo9AsO5v3vO39ZzHaRvQRDbzSebjH3aSWII6136eDDmkSzO-xJbp6OKKs5Bn3AlLeaW8937T9VUgfAov-5YiFF5iWaCsfR--ZnGPLyCyM8fmfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SNvb8eG40uJc2hsQFiVHQAqE_kl0BOqxAOASaDIute5q0NdafJAgSgGi9KPSSzXOZfd9XVUGBSYFKtteOK_qSfGcp8kWT0atTs8gMBkZOuRkwoznGdxxnZ56tWqXXtRS5SWj9y6X7wW4zb8gQy4rd4u9xkEr63gIeSnJcdJ7rwZYvTsqMw3IMb-80g9Z3uvJ-E_r7gJIrg7bZA4-5Ur5TNLLA20gcTz7pJQY9sUzHxhRmCEQektTazun2l-RwjH8ovWSlsBLwheGma71Fwgy7yRwmX6H0ePUF9g0G4uB4Sb5SiICy0u2RnSWezUUI737FjQZ4ci7sloMkCsFUfdwUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I9tUTto42hmNWa1B4VqMMKPJFH7eafyUsumXzHO0pcvxF28MAo9CXLHsZZaYVDws-T-Zi5JxE3GRRQBT-2UiCiIZ8CSigbh17gkr6QYzBwlsVBPoARksFDdsLaYmlIcy_NTformv0DouJxZOxqbLAimIWIJQVjLFeORsHAvfFIdfqYGvh3DILt0ojRC1ABUfrt_eg1kz2I943ODeJAIgoPc0mU0rq0eeJrEpgr6sjbCfTjNKSY2CNgVqEZ0EYpqNIl8vIfp_W_BPa2JRJvQ0KSBK7lV5vHONboRZBRTV8aq9fzo2ubg7Ap473TCCZgqy1yPL2VE0VLLc7cG0NYp9tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/leq6LjhNpUhfRdmnH1VQXvfXCjj8HWLxuWHUCLDajXTkagoDEHrFENMJHKCGuzxz_GsQHsKO7rpXQkKHx_4v6aauM4Sq3bZGUcUU3M4dzykO7eoD8gh81MyxZDrBpb5TCdgDt0uTZzgHnLlHfMOsc0SZu-o2LeZgk_IjMbtxQRL4wn7IcBcrHyMLFpi0tAAfnX6sG9k4cxq8dosdx4WxDKshQDjQMco5urE0sLwhFnACzGyKSrTDk5jboD2YfqUWw9msbjcP1QUt7MlgyLtRwUpSHf41DN9AtJKmUDOU-ObtT7BadGlPtma_fJqNkTRMezT4McTA7Kaxvgs0rTDONw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BdnvXVo8NSnqZVPy8pFlm_WhKARv6CNoPrk7z6AZzgR5La_DYAII7Np9FgZXRMEQ6PBL9blOSSoEop30Lshi2qHzqTAsE8NwOd2StasnwKJo9dE3leZRwDzCeCh5GVSuSYyuXwZmsDF3tHZwfjwlnjxQMz9PeWCdkEgqGhBJdEvPdDBJDJhMXa5SwUMjW11L5ajFjUOF-47PR83_KuJSE30ln_AC_5iLR-2MfHWFsFDS-ZQovylKjtvHkencjcQrwQvYrIZpZ3GLorl_z0aQ3nlo1IIvVgHqeu3szw3pjJYCsU6b4AZE-YwHWcRXVG94Dfo7ui0KSqJsX5qbgxqPew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هم‌اکنون اجتماع بیعت با امام زمان(عج) در میدان شهدای مشهد
@Heyate_gharar</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/683413" target="_blank">📅 20:57 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683412">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f75df1eb4.mp4?token=rIcpJO_WvDvhVKvD6tiSychm0W8QtdY9P09CToR31_NGtiXikNHuBJNcbnU5eCpNul_KX1JONPheFBRgcMR_Diz_XAWQCpVlaaTUyqUbAEUeGkcBCgv5gj8xTmgkDrIaasDossSsRhQoi4Njrql8l7DLyszM1ASHgcdxFWA0EkrsuiRmEgwpgGQGyFzIl2XZH2qkkViaHVDuWayy0G5rGiJmoTmsx_UWs2jc8VDxZKfg4o6go3o9jpBXzSOP9MHHTl-D0H4zJ1eN3YIDtgY8oXQ_rqyMrKn4pECMwm1inr9AHe_M-oB18BkPEvhx8Zxc-S3_sfPC3KdN3b-3rE1G8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f75df1eb4.mp4?token=rIcpJO_WvDvhVKvD6tiSychm0W8QtdY9P09CToR31_NGtiXikNHuBJNcbnU5eCpNul_KX1JONPheFBRgcMR_Diz_XAWQCpVlaaTUyqUbAEUeGkcBCgv5gj8xTmgkDrIaasDossSsRhQoi4Njrql8l7DLyszM1ASHgcdxFWA0EkrsuiRmEgwpgGQGyFzIl2XZH2qkkViaHVDuWayy0G5rGiJmoTmsx_UWs2jc8VDxZKfg4o6go3o9jpBXzSOP9MHHTl-D0H4zJ1eN3YIDtgY8oXQ_rqyMrKn4pECMwm1inr9AHe_M-oB18BkPEvhx8Zxc-S3_sfPC3KdN3b-3rE1G8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیگر لازم نیست برای قطع برق وسایل، هر بار دوشاخه را از پریز بکشید
🔹
پریزها و چندراهی‌های هوشمند امکان قطع و وصل برق دستگاه‌ها را با یک دکمه یا به‌صورت خودکار فراهم می‌کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/683412" target="_blank">📅 20:52 · 31 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
