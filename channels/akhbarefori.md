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
<img src="https://cdn4.telesco.pe/file/Lym_dcOQXWsF_VmRN1_gihXvKoSBq_mwDQe0GkDvQevnF1oxcQurBQ6Wmu8wey00Ym0hH_6LlQT9d4LK_DewhnlPj_m85LgO_V7zcxj93fYEhR83A9YxvJmZJrsiXhnNQ1d56jASgwupaHCvKf6-F57xGRqC7X7OlnzFyDQn_9NL-Xx3l7hk7eI-ZGmkkMu4iyznv1h1RSGa8Asux5aP3v0e7NNp_s3ADvpu5l1Ud8UL_2u9pVMLK9mFJR4Tul8V-UVKRVYhRrv34oOYGH7cCmzQ5NA-4peqOo8-SyPrMno5PRKx32CvNXUZ91yBasYXVaDw0EddgHp0W19AIlIJfw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.39M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 19:12:14</div>
<hr>

<div class="tg-post" id="msg-685336">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ضربه مهلک مرزبانان هرمزگان به شبکه قاچاق سوخت/توقیف۲ میلیون لیتر گازوئیل در خلیج فارس
فرمانده مرزبانی فراجا:
🔹
مرزبانان استان هرمزگان در یک عملیات مقتدرانه، ضمن شناسایی و توقیف یک فروند بارج یدک‌کش، از خروج ۲ میلیون لیتر سوخت قاچاق از کشور جلوگیری کردند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 13 · <a href="https://t.me/akhbarefori/685336" target="_blank">📅 19:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685335">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgqYnK1GVANxhYqel_LAwKrGHts848lTHcvVTpxkZySEvh8D775wP5eMfxWWUW0hzuS2KzAwPMUT5eJhvxrVIDksCtZmi4E2dOSASschjnx_9B6v-ANBCVNM5_Z4Tf0UcZVYVh0KW5L_vOGgzCFmOqRyzdUIELKSRTkaMjGiKsk_y7ibaagG4e-q4PmA3zBwazk65K6QR11ylEBAr6t6OdM6hqNHsF5jdIKmpA1lcXL2HVTLQjiOvPpq-CtHQ4sxTefly_Jy0cdL1q1zSh2-I1U5HVyaMsz6A0Feh8NTRGvbyo25VpYWe2PSoVKZM2JB9qppTjUHbDtyiDo1fC-64A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میوه‌های خشک به جای دارو!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/akhbarefori/685335" target="_blank">📅 19:06 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685334">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rp9fGXaUiB1FlspbPspw4Ak0Y15eysIBYBpUV9u8PBvkhYM0eUAjP4FLVAzOBoAND7vZtw_96oLYQWZWOR5XbZLgvD5t3z7EsjVMRC_piI90ex17y4pgUMSc4SP057CqNrNQzO4gFz744aNk_OTwOVUj1pLKQYL37fkvUE4Z35wSnGGveK3QjjQtkIvtkVU_EFCbfNohpU_lZ8pYtR4WilnTB_bDqiON60fIIli4H1G-122oqJLoDO1wsKALs2NVbhNMmriipu7v0OZdkQxLPiIta_bQptj8zrRE0tm5YuLo99oGCB83oQ0Lo60bywilpn39zc8Wk6Rohuhf8q4Xhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏳
خوبا زود پر می‌شن
زودتر قسطی اجاره کن!
🔥
🏡
ویلای استخردار تا کلبه جنگلی
⭐️
اقامتگاه‌های کمیاب و پرتقاضا
⚡️
رزرو آنی و قطعی
مشاهده اقامتگاه‌ها
👇
https://www.jabama.com/landing/jabama-best?utm_source=telegram&utm_medium=social&utm_campaign=news_0607
@jabama_com</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/akhbarefori/685334" target="_blank">📅 19:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685333">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPeLI9OL8lk6ZZNCwWZHtVQSH3Cww3my8BAM5eIC-kz2mAmbEQFW3VzpSct_TRk0ucphyjuo5FZsru50lRI7bQJVBp3RZLsV1Zt1LFQ8NM0mL5gJPk8VFVpSaLHASz_lagO9_4myQ-F1Z3TbB0yyYIXf38OosE-wo0WQpfwLk62WXkGMPx7VnowxS_qblY0PGUXbsvh876vVIPyw0SVUL8_lfOawdbGLjJig1GnjBVOx8uxeZPFOs75dqtT5gzlSfYj2gGEFg3eU7VErdHD9KQDsqhE8JCpR1h9bA1145N6Xz2riKloCkL_wieIQoPa82nmM2Q8YGINAL7fkOt5XMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه کریس مورفی، سناتور آمریکایی به پدوفیل: تنها دلیلی که قیمت بنزین سر به فلک کشیده، این است که رئیس‌جمهورتان جنگی را با ایران آغاز کرد که هیچکس آن را نمی‌خواست و او به هیچ‌وجه نمی‌توانست در آن پیروز شود. انتخابات ماه نوامبر، همه‌پرسی درباره بی‌کفایتی او خواهد بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/akhbarefori/685333" target="_blank">📅 18:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685332">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ba8def8e7.mp4?token=YEJtP8ztjjQdX1VXHTbhkRwJ6inbpqAtnSViPZ6TH3mlI9Nqzg_T3ExHaDlYzLEpodPeVwiYTz1VSgneIR8H1fuQcYWn53GwRnnvhEnFrYdkMjsPxjFXhyR3cUc5F8WPQfU1f3ErsQMkge8DcJlF3gRlCI4ZiCaYAPSfGloE10dYvmmGEfu6zy8ZMAWPqf3vZV5ysaI6NY58p4AqbRNIo0vRvuD8UkCmqLs8Oo8y1YA0uNz2XDMy6N4sL0fRUMpD-jjHc2XGlMee_Et1JaWderGVVOQvyUixPylHRDRcFcmWVJukhXfSlaLqC4MnK0MOnVwvUjTwq84ZYCbHZWIjBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ba8def8e7.mp4?token=YEJtP8ztjjQdX1VXHTbhkRwJ6inbpqAtnSViPZ6TH3mlI9Nqzg_T3ExHaDlYzLEpodPeVwiYTz1VSgneIR8H1fuQcYWn53GwRnnvhEnFrYdkMjsPxjFXhyR3cUc5F8WPQfU1f3ErsQMkge8DcJlF3gRlCI4ZiCaYAPSfGloE10dYvmmGEfu6zy8ZMAWPqf3vZV5ysaI6NY58p4AqbRNIo0vRvuD8UkCmqLs8Oo8y1YA0uNz2XDMy6N4sL0fRUMpD-jjHc2XGlMee_Et1JaWderGVVOQvyUixPylHRDRcFcmWVJukhXfSlaLqC4MnK0MOnVwvUjTwq84ZYCbHZWIjBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راسته میگن پول رو بذاری رو جنازه بلند میشه؟!
@Tv_Fori</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/akhbarefori/685332" target="_blank">📅 18:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685331">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
نیویورک‌تایمز: جنگ ایران به «جنگ بی‌پایان» ترامپ تبدیل شده است
🔹
رسانه آمریکایی در تحلیلی نوشت جنگ ایران پس از ۶ ماه به بن‌بستی بدون هدف روشن، راهبرد مشخص یا چشم‌انداز بی‌پایان تبدیل شده و رئیس‌جمهور آمریکا که زمانی با انتقاد از «جنگ‌های بی‌پایان» به قدرت رسید، اکنون خود با نسخه‌ای از همان وضعیت روبه‌رو شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/akhbarefori/685331" target="_blank">📅 18:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685322">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MIfGPiSOUVhH9CYa8FkxXKuv_g4n6D_NBZE-qbqINnJZwq2HfsXNDUwVxQSsNoBktgAfFxasgfm6k3RfCJhgaWpPdpWSSWAg71YKTPevc-YypHdLsAFpUQqf0CDk0BXBHnXdkPEwrhN7HMLQ0IYxZpaR4UaClVF9CbLubR35F7jzfIPmmI3Ub35d6FdoP2_oDMDXW0Ulovg2TuRC4LuMmR7HGbpCJFDf3g8iTfZTrlgiGPZnAVNz31NRHk0LgWulooNNXlf4oaamYHsYyOAS3fxXYeanvRKeWSsSROzS2QHxInNILCpKbOVGp7ou77L1osyXr7ifOAiYYFPv2co2cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qMEVyb1lF6Am7fncZS3C83r66j2-AqWQ7hS6WSy8Q7RHQATdjYN7Avp_XD-rGRunt7MooCcMQsInCcg795dgazxlCSI16ENfIBzvRKUIhYcCjfdjDaAF-Bvrpt34wALH3DvIR_ePlUTQEIjWvvjwbUkdtNGP0MciRCYQ5zptqCKdvv0WYZCpmEv_OuCMKDMHS_YMcyEwdiC3F2_0ayCQEPZricYy1O7VyZK7yS3CBrU2hq5fM76veYwLEx2AmTvB2N_mCk6iMpFfP8RUu-poGauG7kcpfhqRvX_p02LMBQs83ELO6jEUVd9ZX4Yko6ElZqQST0AtJwko21vCp4ep9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Si-u7AW4x6BPW6GtUP0zfmkAjVfzblWTkZAh0HCJ416k5pzEhQSdrF2ZObuhYabuoYMZC53VCB5VsnO4D7IMLRxitMMgScpqksQfjpB_HxG1ePxyhHFWl3xHN4OAfucuU0u_8DlRhMvnT1SEQZyHybvedDNvfNyQPWZCL689K2ZdE7dol6Fgj8yEQ861wr3u02jxERU7CkCECQdAgKRgSa812tLB2VPja8F7CoatlUXpNP3IHQgSz73ujRTW7n70YQJTAWL1B_bfCeqCQxKvNdPtWJd18rKHrWB7c44VHjlshmm78HZcS1dqvRFCHlu-G9DJpKwhTdalRcN65GX61g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6Cxa4Z8AxHnDRgMF3-9F1HWlng7QTDd6P-KM4gG3fjySKtY13OQ1Rr0J80gQUX8BFWg-QBVuN8tDSwp1dGoZE86iHr64VEDByUb9lxE2jpbV1C78SuvwEbZEHVbZIoqa3vSB-Cbbe-TfI8ptNSJZ99Qjv_A_PDwuQM-mI2MEnEIXtw72TAG54tHnDwimNQ7BS567ILN3PtvfhET9f58tyuibhJp7Ofa0HjgnMsZiiWezqpAEqDYGN0uuZuQCki3NCg5bD1z5uZpoXkRO4-t9U9pZtkEEm9W7haaBy_7DmYC6fwQYALFrcnnciHX0Wcwx9yqTEqazy0GZlf84DaPAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i3JtvDocuM_68SaWCALc9GTHaK-a_DGEimGlMJhu6s0BnQ_ZqRwU30PZiLp5-BKBaFXjaSixXjefCiGLhA1RIedlXZPVfGzHZSNsp3CmxwWQfEjIr-m3uqnet3M1NJrkn5JijgeJ9kWv7ir_tn__g2P9-jKoNRjD6tpm1g5-WwKc5smSgedx9DaArDW08_nVc-fMeGpy-jtqgUcBqS82IHQjy5kLffn-dZZbstQFUecs2v-sWYPqCbJyUfIpR9kPmNgI14pIkSYiLW83uNObFsG4UmbXhzSkClqp2ysOLLfWkWF75IxHCcLBIeGhSV2kYMico5CqkrTeapn3BbV0BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FJZ8SA2GQBhjQlTZDP7Qh3DVxZHN2ivzg0YqD8ZOeFZ48P53QxH87pFRjqdtmQTUGRqrNrQpK3jj2blqjQE1gzr-Xn8EFXwSRvHQLXHHyhFxqV1RgH9DYvkUBRX7PsKNoOqbo3hNxP4MxG8mTr907V6u-u-HkFu7nD5qNP4vb-rB2rioEze2Vwi5olGOLuW4_Fk5XvbsAV0_LkOfjhS2pMbWoloq_QQ3p-BIWasRJMy0IJctYc-WMdzfieRxRaf0EW-N9fQCxw3fuFlr57yQkzGSTdDwJtKNbaS5VtMhviKaHc4a7y0WyiFhmYfB6CEshfXydYweuNy6RDTf6JIgOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M3Z47lEaSOvlkEJ6417awittXyh5tEsZYMeOktOBgA3-HNh5uYeKc6RjN2TwVjZ6eVkwVcHXh8dprOenohBrXO3ReJxpcUkjuUtbv-9nKSW-k2Bi6lKwlGU7dpSrRTMKzTIAPdhBUtW3nu-203Hyu3YeouHRYq8ZqliHoJahdW_0_jqNd3wi5mqXNHajPr2tZFNMqsfS9WVz4Q8imUCjxDDexUjEMxGX-Hw8Yi6yxNUCERNIM2VkTlcOouCHlm8Fxiwsm4t-Ri1CfipfsAlbPeVsiF1H7sPKwHaTfV_5StUwfuAIPUU9FWfjq5jQVSIrohh97tBuROoNmJNpWFLCTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AznZDHy1275cNVm7i7Tg3gEbhLOkiw6mAmjrIFLVAWuDLpf5m8-UosLcezbmONmyAnMTcyHvstcG7Cn1UCr6fAAcKCZHH5F1imHFOwX2mfi3MfOeInGbCnP1tfdCnqC1-U4dVkdVyWfwju5fS1xerbxjyw10MnHzmAYbSR3uGcoyVARVqYlT0h6neFGz3K1rD4VrrrI9zK1nzGGHYFMgtRw6N85m48JvZPxyExMqAk_b2aw7fAjew3rZ2ZqaifjpJprwOFSUuy2nbM8KHVF5nDVvazD2ojcisxmLIK-drTlIl8sVXJ7FS9FgpEBfrqbAvoM39YNSViaS4NSlPgiTzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HdUosus-67wcMffmKdorzJiNO-pWH0fx8mWzSrlkzD1GEbShIiny1jfTKMjXR7JN-orLSPsrCtE_g_kjaYTzfk57P0RWLlWh7SNHAeefcoy53QvYnAaSy0OyPuGNeQYpLTYM_weKspx3NS7rIY9ZRjBwjoF-AqzKtX2_JFgTZYymUVTcIZ9aAEiXIldTqMsGrVtxUPVOIg-M7EEa7coKi_gasQ9mpPmfeUGJ8gncRSVQDJcYIlj_WwyK0bnYGffP5pjz9tQYoORqwygqC3neluFHqqUA6OUMj5C2WbxEMpHxPkqLHcyVOVMNYozjQGj_ew762B8aQ_UVvZS3u-WA5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت دل‌های هم‌قدم
💫
✨
وقتی دل‌ها برای یک نیت خیر کنار هم قرار می‌گیرند، هر قدم می‌تواند بخشی از یک اتفاق بزرگ‌تر باشد.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با نذر و قربانی و توزیع گوشت قربانی، در مسیر حمایت از خانواده‌های حائز صلاحیت، این هم‌قدمی را ادامه می‌دهد.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/akhbarefori/685322" target="_blank">📅 18:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685321">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
آخرین وضعیت توزیع بنزین در جایگاه‌های سوخت
سخنگوی صنف جایگاه‌های سوخت کشور
:
🔹
تامین و توزیع بنزین کماکان بی وقفه ادامه دارد
🔹
امسال به دلیل شایعات فضای مجازی تقاضا برای مصرف افزایش پیدا کرده است.
🔹
احتمال می‌دهیم از مهرماه با کاهش سفرهای تابستانی، شاهد افت مصرف هم باشیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/akhbarefori/685321" target="_blank">📅 18:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685320">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مصطفی را وعده کرد الطاف حق
گر بمیری تو نمیرد این سبق
نام احمد نام جمله انبیاست
چون که صد آمد نود هم پیش ماست
میلاد حضرت رسول اكرم (ص) و امام جعفر صادق (ع) مبارك باد
🌸
✨
💚
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/akhbarefori/685320" target="_blank">📅 18:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685319">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
نتایج امتحانات نهایی اعلام شد؛ آغاز مهلت ۷۲ ساعته اعتراض
🔹
رئیس مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش از اعلام نتایج اولیه آزمون‌های نهایی و آغاز مهلت ۷۲ ساعته اعتراض خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/akhbarefori/685319" target="_blank">📅 18:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685318">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46f82268e2.mp4?token=q4knbE8LK_bh9nynUOdPTr_NBDq8K7FTRII-iIuFvEA0hUxFRhLdelsipYbR32KEuHmDxgtJsYSvXKqpa5Kay-uD_RWceFb9cQu4X-FPEAQ-rkvAnewtVveL3sj0RcFuP92tEiz6c-eGS3OoRBiWGSpLLSHZwo0eP7l2PQ9qFREvTBCbFKoGyWZYUamaSAshsqTRiDYC-1Er3CxqBvGSscexMHMCjHzC7MGCYDmRl8Gvix7GmX2exV7UDV4nGtGitXB_nO6w42EM6R3N1k2LhybCEv5QjSTvFBan8WwQ2ebuG69-O1Xhddv1_CfJ8jA1K_t9ICLgxoViMnSEX4aixA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46f82268e2.mp4?token=q4knbE8LK_bh9nynUOdPTr_NBDq8K7FTRII-iIuFvEA0hUxFRhLdelsipYbR32KEuHmDxgtJsYSvXKqpa5Kay-uD_RWceFb9cQu4X-FPEAQ-rkvAnewtVveL3sj0RcFuP92tEiz6c-eGS3OoRBiWGSpLLSHZwo0eP7l2PQ9qFREvTBCbFKoGyWZYUamaSAshsqTRiDYC-1Er3CxqBvGSscexMHMCjHzC7MGCYDmRl8Gvix7GmX2exV7UDV4nGtGitXB_nO6w42EM6R3N1k2LhybCEv5QjSTvFBan8WwQ2ebuG69-O1Xhddv1_CfJ8jA1K_t9ICLgxoViMnSEX4aixA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تگرگ‌های غول‌پیکر در ایتالیا خسارت به بار آوردند
🔹
یک ابرطوفان شدید در شهر برشا و مناطق اطراف آن در شمال ایتالیا، تگرگ‌هایی با قطر حدود ۱۰ سانتی‌متر بارید؛ اندازه‌ای نزدیک به یک کف دست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/akhbarefori/685318" target="_blank">📅 18:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685317">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAX3HsMZ6XHH9-EISRU4bacqSMQPeW4DTvDvWkHa6F4CfqXae-3vnvZ-z7e54i9IbXW4g0raHTB3DhB_vIlkKIBeGFbskVfgVBhNUpOa2MwicIsajgNu3rfiYkiicPAZcz7iAlE0GZtqqBWq17PUu2xYz5Zuf3Hpfk-o8D44_5VqERLSuOxnHWPKXrW1s2-OEHddMmnV19y8wQAXNGwNjyewaJGQQArzIGjHNNLOyTF8igdltrr4ZbI_RmDAn5vTpztqKq2vbOi24RRRUNactwy5_j6HEYxEFGXMBrtOgyKgOt8oFDv1NLpaWm70U3KnMGrCyg6Zv29xGzKK1Dn7Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شوق پرواز
🔹
تیم ملی والیبال زنان ایران برای نخستین‌بار در تاریخ، با صعود به جمع چهار تیم برتر آسیا و مرحله نیمه‌نهایی قهرمانی آسیا، دست به افتخاری تاریخی زد. ملی‌پوشان امروز هرچند برابر چین شکست خوردند، اما عملکرد درخشانشان در این رقابت‌ها باعث شد با کسب مجموع ۱۱۵.۷۲ امتیاز، سه پله در رده‌بندی جهانی صعود کرده و از جایگاه ۴۰ به رتبه ۳۷ برسند. در ادامه این افتخارآفرینی، تیم ملی زیر ۱۷ سال ایران نیز با پیروزی مقتدرانه ۳ بر صفر مقابل آرژانتین، راهی فینال قهرمانی جهان شد.
🔹
هشتصدوچهل‌وهفتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/685317" target="_blank">📅 18:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685316">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOiDUWyjiBsf6Hg_XFe3tOY9tt935C9YeO2R1fJbO9ohdJOhI1yaHZBVzpnR_C9KpYoaoUBI1APb9FX05zSxTZVzdKesEHvXsGEdtZ1WWyeccX7ayuYSSc2FsL4XpWVesjK_P71qRMb8asELEc45OJAarlF4pyrZwIbtNKeQmD_Vp2-ZELHgD3VKx26wYbFfuzM2EukNm7zKW8s2QPds2WdV1OKv-r8QtJ4iPSIs0Apjw4Pj8Bl1DZPMCU9tNoSw6mtzrFn_JahkLqcSMvQsFlfoadDOkDTtIfiRKHapDwsBAW5ls6-BUX9oVI4SUFNM_i31iPSD-SwdYF_9r-Sy7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/akhbarefori/685316" target="_blank">📅 18:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685315">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024d1c31f.mp4?token=AYSDcXVm2EWj721pG4wCEE_iZ691VC73tc7H2eiS4Xz4VBKuwk4DwHscbUQCHwyD-neqhNCTZ4D5XrQNOXfRQ6lxceqRZ41QMXZIc3r64ekFyxstgDCqkntdIAIpaqHs0_3pzdEndE8mZvmSgYld1WYG2_xvduXZMyoPQVjwv7G1xSkUocZAndGS4_s_lgwi9pQ3vSxovGp53u8STG3uWUKlAWsxF47OnqLn0CIwP1vYN9DmL1ACgxIV5wq6jLSnuQlLtO4YoxQ6OCAvMpYIc2gQZcV7ObewNB8Y6g5L4CS1jxNe31kCDZMvW-HKPipNRT9lVo-aBU4i0NXRuPd91Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024d1c31f.mp4?token=AYSDcXVm2EWj721pG4wCEE_iZ691VC73tc7H2eiS4Xz4VBKuwk4DwHscbUQCHwyD-neqhNCTZ4D5XrQNOXfRQ6lxceqRZ41QMXZIc3r64ekFyxstgDCqkntdIAIpaqHs0_3pzdEndE8mZvmSgYld1WYG2_xvduXZMyoPQVjwv7G1xSkUocZAndGS4_s_lgwi9pQ3vSxovGp53u8STG3uWUKlAWsxF47OnqLn0CIwP1vYN9DmL1ACgxIV5wq6jLSnuQlLtO4YoxQ6OCAvMpYIc2gQZcV7ObewNB8Y6g5L4CS1jxNe31kCDZMvW-HKPipNRT9lVo-aBU4i0NXRuPd91Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
#تیتر_مستند
| قسمت اول: اقتصاد خرج‌های بی‌صدا
🔹
بخش بزرگی از درآمدمان نه با خریدهای بزرگ، بلکه با هزینه‌های کوچک و پنهان از دست می‌رود.
🔹
در این مستند می‌بینیم که این هزینه‌ها چگونه شکل می‌گیرند و چرا به چشم نمی‌آیند./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/akhbarefori/685315" target="_blank">📅 18:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685310">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N1IzRkZkVrGcJuVFWqUiiY9T6FN_3ZzJMBpBNIH2yiCKrOJftHn-vSajehoPZ8wyaxoYA2KKoh7sZv-M9C1NvLfE4rwnVeDtA9yVUjYQ4YY6Yd4Wqp5O906fDfrfYUMAkFB4Up8uwbY-4BP92C9FSV7rOdmlTzQA3FDRih3UvuY8nhwbXbZg2YBYsSNzgaibIvyvaW0_kC48-t_rpACbbsiqS4d_yw27OipZ-0DI0AbW3PAO1UbRf0GRgg2rSq72oBPm8XNOs65DV6Gq1tHkllnFWtJPYI7o1Yy9jZgZBcVQGMRyxBr2BxYSyZMkamjAR93U13y5ayTK_7xif9ZFuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/igtwU94qBVTqdqqVW-WpD0XFd3TyjYObVfTdAghb1ENIP5da_wUrocidkRLUULbvEIifAvrVeJ5ciCihTrB7ur_-lP5sEavK5QaLoyj8TwbQIrhaI0ZZ2NoBL2z1LFQTTPuCaKWowcIMmuqGCSZNtTNa_NvmsGy4TPre8a8mnf90EZ9lJxkef3PmENeauQs2I_XTfE_JvRtcakWXYs-mCdJwzHV0fmYAREzdew1xYA6I--uMwibHPczKaqj1ieBLuEFyfXVJ3SwhRUudC0_OWWvJdAl6bFZWLZmnIGQu1hAWwTBW4CihrVP1T7qNBt9mrirRpYhnAmj-3Begg5Xulg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/axXAwg8-JYeB7qSuwRYv1ncVp81D2EUNWg4mN73FfPZ8FdXPaIesZkUYEVvPZTmNwUX9MlC3L0zOZvfF0W0B-YQvOsVGI8zabjLmuhEVghqjptrDUCyKmJw1thAV8QvZe-6CiHxOKmS6BdWhxPel2DOujcJ7Xzhq05UIXmJaSIdrSdrE21IJ95WLPRBqqABzrba2iRRjofge0QQ5A2zI4HcV9kOLLRdSpYA1UISnndfo8mntJHlSw2bsDI2bPfajMaaOoQtbpjI-DTnEbire8rwXrxJtC83zeNj0AdBgHqb3qxWIHpCBwFgV-zkwsVNG9ObYhk3CL-q9GyWYH88uXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Be1WnCwX5i4XKiIdM4IIiP9f1gQTelI-ZlLsGva0njWlyxuICKTGwLmDL8h9vxxYmHoDTQCnWCimcNdNQZ2MOKhTsKc53Zfr95QovzECkcgCR1KaoIpDDNdgEU-LD732bBlORbTSCs-GyWX3dLb3kDIc0u4CKzkf-BIy5ACnLmvdiWV3iakawLh9clv0pKfo4f4t0NCxrFavc6a3AFeQSezssEt6NOgQcM2u9Q7e4jdFJ9fiO4ne4TWtGUy4w_Qfg8OH7AMdcasJ71o4vp_iAsGUfr7s8DeJ92-2VYiwvOl8J6xEqCD8vRC1E1mjr6JCI2oX2KepCWGpevp2yDjnQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sEw-20bMjOf0a99HRmtWw237k5wTmfpqch5FKSOUIQhJ0y12S0xI47kfExEevl9LCkVe5-FH1NZnc8Daxaxa-FN4Dk7lH0kNYhVWsTd2JbJvcmhPv_8ldgryLTkrdvPq7qxlIbEvcgJkWO5P7X9o6Cz1YzruRIaoKYqfwPfIu1Ic9qi8pAW6hkUgbLHzr3J-a3XL9sDxWYXoHN6wYIsliegLZWDLqVgBg0RcVOmiAMuGc1cXZwUgH9T9yQp3RMkjAXHhfd2MZ93FfhoW9_8uSwBnjmqkLdY_TKBrzxCoBBk5I3gfmDQHI-Pf2pTkQCRP8vsVZBZY92KGkFDDIgVXQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر می‌خوای انگلیسی رو درست و اصولی یاد بگیری، باید تفاوت این سه مورد رو یاد بگیری #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/685310" target="_blank">📅 18:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685309">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e51a21852.mp4?token=jkZEvJOWZF_vns3msU56V86PDZmHtzI8OtR9JPa9DpMVNimDJo_NSQRB78MUpn9BiWoqkYWWBg6wMHQlYSgIALmjO0mZItNOdI_usEI4rp7uu9kNYqh91FtwBhufa4R0sQX4VjS3Y5qDUJKUo71i8f_rzEsAmVEkdGihjL83D1_iePzAABxFUGBR2weu7jZFse4AMCvZhDsZU6eip-xTdnb8v9ltKvw9Z838__7trSLEAjCyFKgurX7--7Naa0yj66J413-7aVoAbTXPshFKwL9veN3yEBtcJL-xpxyuPlqAey7bv90TpVZ0e2T9OUmW1rYvXPEZseEy7Xqc6eWNoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e51a21852.mp4?token=jkZEvJOWZF_vns3msU56V86PDZmHtzI8OtR9JPa9DpMVNimDJo_NSQRB78MUpn9BiWoqkYWWBg6wMHQlYSgIALmjO0mZItNOdI_usEI4rp7uu9kNYqh91FtwBhufa4R0sQX4VjS3Y5qDUJKUo71i8f_rzEsAmVEkdGihjL83D1_iePzAABxFUGBR2weu7jZFse4AMCvZhDsZU6eip-xTdnb8v9ltKvw9Z838__7trSLEAjCyFKgurX7--7Naa0yj66J413-7aVoAbTXPshFKwL9veN3yEBtcJL-xpxyuPlqAey7bv90TpVZ0e2T9OUmW1rYvXPEZseEy7Xqc6eWNoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی دست استاد خود را به نشانه ادب بوسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/685309" target="_blank">📅 17:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685308">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
تصاویر هولناک از سیل روز گذشته نپال
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/685308" target="_blank">📅 17:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685307">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77a4fd2672.mp4?token=G5NhE3tGSq1zFFIkspvklZQBEkxc_ys6YHUFiV3PbLPXDof7XIKt3QL9G_YI9_UYoaXRvuxSI92YOFygyA1s_S9fJPXBkDa6gQh9JMY2R7XOYluuYhEuKpoZQAGofzEubUhC7C3E5BVPPEyPotLzzDwTo31gVELkxuOVA60Lf6FgokiTLzEzZlHdd0xslfcy__hAh0sCfuMl4iEpVIPEHCLlz5YKpCdCrNPXhbf_Js-0gkfFCYqKx97wjxc7qBfLYHWpHDl79WnDDwOfy_iBs6Lkx2Kfm-eza_PnEko7rhzQolkSHeYomydYyIDECkkBW2g3LU3AUzMbeZl_XPfPrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77a4fd2672.mp4?token=G5NhE3tGSq1zFFIkspvklZQBEkxc_ys6YHUFiV3PbLPXDof7XIKt3QL9G_YI9_UYoaXRvuxSI92YOFygyA1s_S9fJPXBkDa6gQh9JMY2R7XOYluuYhEuKpoZQAGofzEubUhC7C3E5BVPPEyPotLzzDwTo31gVELkxuOVA60Lf6FgokiTLzEzZlHdd0xslfcy__hAh0sCfuMl4iEpVIPEHCLlz5YKpCdCrNPXhbf_Js-0gkfFCYqKx97wjxc7qBfLYHWpHDl79WnDDwOfy_iBs6Lkx2Kfm-eza_PnEko7rhzQolkSHeYomydYyIDECkkBW2g3LU3AUzMbeZl_XPfPrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روابط نزدیک ایران با چین و روسیه می‌تواند فشار آمریکا و تحریم‌ها را کاهش دهد/ آینده اقتصادی جهان در آسیاست و ایران، قطعه کلیدی آن است
دکتر بیکلینی روزنامه‌نگار برزیلی و استاد روابط بین‌الملل در
#گفتگو
با خبرفوری:
🔹
اگر ۱۰ تا ۱۲ سال گذشته را دنبال کنیم، روسیه و ایران بسیار بیشتر از دو دهه قبل به سیستم مالی چین متصل شده‌اند. امروز ارتباط اقتصادی در قاره آسیا بسیار بیشتر از حداقل ۱۰ سال پیش است. من معتقدم چین پروژه‌ای برای تبدیل‌ شدن به بزرگ‌ترین قدرت اقتصادی جهان دارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/685307" target="_blank">📅 17:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685306">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBxWpWavJtUr5IoFSu4EHGtZIcKekShavLsQtfpPH68CpQQQSCYkie7Xw4Nf-HygQNBN0uX2PKBumXphN-zYI3yU05FAVmMNs9cjdfIsLcHYeJRMMDpskPqClujWtxdcjQ-wtMFtjzswKkw2kDIGtxz6q13EWXuZgotvR_QUgM6hHFhOUdWPnPbWccY4u668nhvW6aCz2oh5fZ25KLplQPwu5EtjoDJIzWrqE9pi-kJzFFxJqyCapgWQ55u8X8YI3OG7Ywj5EPlRpeC7K_3dsJBSUIgqu89JF7JYBzSuRB07caZxGSxtaQ7Bl56CFhue8z1_T2vzQX0P-2I_8DVmAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نکات مهم انتخاب رشته کنکور ارشد ۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/685306" target="_blank">📅 17:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685305">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/817d078ff7.mp4?token=avmXYOQtD7S0GOJ2pS9e6I5QdlQiG7Sch68Btkic23SLyfvcGmRF3o-QNuu5VS8dQPCQePUI8t-LDryL00EnNpIsY1o5cgJ8_ab34WLqTn6sZnqvS0RTtmTRloY8NHf5F0QhtjxXXDhWbe9u7nzhFbbZPLXMz9N_3463Y4xErd2Ce9Uh3BR461bOHXp_r2qBPshei5HLwYDhDP3yuUnb3ZN7sEO6Xl0GJjXJmgQXQDWAlN2xPXzXAgKnAbYY9uxRyxSn1MzeBfOcB0uY31JwXUdaVVEXWOlcqunt_FYwUSgU-23s6q5eQvXKPEIAUWzDkQtAz_OxD72oDQB1R6HSuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/817d078ff7.mp4?token=avmXYOQtD7S0GOJ2pS9e6I5QdlQiG7Sch68Btkic23SLyfvcGmRF3o-QNuu5VS8dQPCQePUI8t-LDryL00EnNpIsY1o5cgJ8_ab34WLqTn6sZnqvS0RTtmTRloY8NHf5F0QhtjxXXDhWbe9u7nzhFbbZPLXMz9N_3463Y4xErd2Ce9Uh3BR461bOHXp_r2qBPshei5HLwYDhDP3yuUnb3ZN7sEO6Xl0GJjXJmgQXQDWAlN2xPXzXAgKnAbYY9uxRyxSn1MzeBfOcB0uY31JwXUdaVVEXWOlcqunt_FYwUSgU-23s6q5eQvXKPEIAUWzDkQtAz_OxD72oDQB1R6HSuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقاد علی ضیا به مدرسه‌های غیر انتفاعی: ۲۰ نفر از بچه‌‌های کلاس دوم ابتدایی را به خاطر نبردن برگه چک ثبت‌نام، به کلاس راه ندادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/685305" target="_blank">📅 17:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685304">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/710bec86ee.mp4?token=a-3jH_GXuwCX8F2ci09cxt1nXAWC5r4mrBSQDjmtTu_sGuRexp8jiuF1ACd6m6Cwh_2PGsLt1gaaAiqMDDlHRjeBCs40WYUcOM2yAib-hJ9nUEbCT9NdJyC1Bn43Q-TF5ecy1A7dxZJWS36eqNVxzOJzbeU0jYQmBoGVXQr0KeOQ4y3CkQbzismcf6dkkmC4yzN_BcD3fw-CBNCSk3A041LIZzA6A6LIP-7ruAOnYi65xM9IjkuZva-Tz26VvhGTEx09hzO9S0rBJzognb_GVv8UBYxwVl-nftJBKan3Sb1NeMp7aHdq1DQ02lZlbBMvpbFHvAHtBvP5CV84n7-LIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/710bec86ee.mp4?token=a-3jH_GXuwCX8F2ci09cxt1nXAWC5r4mrBSQDjmtTu_sGuRexp8jiuF1ACd6m6Cwh_2PGsLt1gaaAiqMDDlHRjeBCs40WYUcOM2yAib-hJ9nUEbCT9NdJyC1Bn43Q-TF5ecy1A7dxZJWS36eqNVxzOJzbeU0jYQmBoGVXQr0KeOQ4y3CkQbzismcf6dkkmC4yzN_BcD3fw-CBNCSk3A041LIZzA6A6LIP-7ruAOnYi65xM9IjkuZva-Tz26VvhGTEx09hzO9S0rBJzognb_GVv8UBYxwVl-nftJBKan3Sb1NeMp7aHdq1DQ02lZlbBMvpbFHvAHtBvP5CV84n7-LIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طرز تهیه کرپ چینی فوق‌نازک و ترد به سبک حرفه‌ای‌ها؛ یک صبحانه متفاوت
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/685304" target="_blank">📅 17:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685303">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkkjT9Pe5Iwsl7beYWA272vEyFmMkfkbHoN9RjjIyLe4cYpHz9X5DNOq3mEyM7713BagXCgAKvCl17nwxParkZmz0fF9SzT2lRwavnJCF56X4f9pnZBOw3j3Tg6NlQiOfahIA_tPjIik5EiNaJdGMuCmxNOBp_CRhUfa_vurAXNaXkgrTWcZmtFdOqdbRb_EIaJgPPs4oeXJl-5G3SdbbgJxqH6ZwVlMolnHUh5ZS-XaTWlf8dWfY1Ue3Y55Wd8fIogYLJJ4Z_5hBeErSc6igaFGcYZVBhRo_z02t6aj3xnFeX8UFnzNB7UrTXQfPN-8Sm8CbABWQT_GZUn5_ZKY6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلایی که ترامپ از آن می‌ترسید، سرش آمد
🔹
جیمی کارتر، رئیس‌جمهور ۴ دهه پیش آمریکا بود که ترامپ با تمسخر ضعف‌هایش، برای خود در انتخابات رای می‌خرید و می‌گفت که نمی‌خواهد شبیه او باشد.
🔹
دو ضعف بزرگ کارتر که در تاریخ آمریکا از آن یاد می‌شود، عبارت‌اند از: «شکست در جنگ با ایران و تورم برای مردم آمریکا.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/685303" target="_blank">📅 17:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685302">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/685302" target="_blank">📅 17:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685301">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8l2ADyhr-c_p8l7kOXHPYQ5SjwIoum3RUCcxbtv9agg6Ep60vFOg0-EG-54Ca23fofwm-TVUkzvfBiHTEYuU4XOp4CtxV-JNppVb5pAB3BLOCzAeMn6U4ciLHBRfbtcAGgO21BElaHykb2qpHtEEiOVpwImBxdzlBuZ-Xbu3Rl7TKf1OJw50zyYgbhTCgX9zP02x0Ym70F9dkTJSQoKHq5x_EFaO1qyAPYN4p-FecTwHkEZL-vKG0BfnNqFJlE_tv0yjpK1Ckh46HnmyHsaDsrpJ2SGe1XUZP8gR43sHnaayca53fXw2u39rf1Pqrcm_2oQA5xYcvsVYdkZj5mAlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستگیری یکی از سرکردگان شبکه تراستی با بدهی ۷۰ هزار میلیارد تومانی
مرکز اطلاع‌رسانی پلیس:
🔹
شخصی به هویت معلوم «الف .ل» از سرکردگان شبکه تراستی که طی سالیان گذشته مبادرت به دریافت ارز حاصل از صادرات نموده بود.
🔹
بدهی این شخص به شبکه بانکی بالغ بر  ۳۰۰ میلیون یورو یا به عبارتی بیش از ۷۰۰ هزار میلیارد ریال می‌باشد و تاکنون از اجرای تعهدات خود امتناع و متواری بود توسط کاراگاهان پلیس امنیت اقتصادی فراجا شناسایی و دستگیر شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/685301" target="_blank">📅 17:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685300">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
عراقچی: مردم صلح‌طلب ژاپن از دولتشان به سبب جنایت‌های آمریکا توضیح بخواهند
وزیر امور خارجه:
🔹
استفاده از جنگنده‌های اف-۱۶ آمریکا در پایگاه هوایی «میساوا» در شمال ژاپن برای حمله به ایران، نشان می‌دهد واشنگتن از این پایگاه‌ها نه برای دفاع از کشور میزبان، بلکه برای پیشبرد سیاست‌های تهاجمی خود بهره می‌برد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/685300" target="_blank">📅 17:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685299">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z32kOgwIgXIWJQkMRH0vQlirP3zb5ZJEsjv0IeEsaKlA8ySSgUANH_XUDmWtpy05pTnWNwBlVL31NeNxGDyBCnI4EBT8hZAwCLQAf8gnzuVQTEuuyC8fw60c6fdxXfl4ggUA-nh0051DHiJICshb1NgKePLZGd-hY_ecM4e5qWquisiQ0pUJGLJEY5cQkF2SZA3Us8xyflk4TXIJet2_jqXeQ4ilu_RWgQsHM-fBmXnNaeIMf8rD8jt5yH8DG4YPfjjkacxBUjH2Rn5XwLmszYISLo0rysgWExIP-mR0SpzJTHWaV9UV2ixXo8XEpqOjBfpewNdrbro2q09btjYmYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۷
سال پیش در چنین روزی، کریستیانو رونالدو اولین گل خود را در اولین بازی برای رئال‌مادرید به ثمر رساند
🔹
او در ادامه ۴۴۹ گل دیگر به ثمر رساند و بهترین گلزن تاریخ باشگاه شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/685299" target="_blank">📅 17:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685298">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ادعای ارتش رژیم صهیونیستی در هدف قرار دادن یکی از فرماندهان حماس
🔹
اوکراین: ارتش روسیه در تدارک حمله زمینی به کی‌یف است
🔹
حمله هوایی رژیم اسرائیل به چندین منطقه در جنوب لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/685298" target="_blank">📅 16:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685292">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoPydUnolIMCgQpH2HuHjIIHCiO2tyJf4nzfx0oc73inV8-dUgcVD6kxF-xsqtz5tCqQQCJY2g2HbKX6u4cSZB7_g5B3ArPA1_v9G37nZbeW29K6oRnNzPtT5HHUrcBkmJuJar62rvDIlc5Q_PJSjskRwOuc61bRQ5FhUq1JUYdxywWMjPlx2MJpyNbI7NJx-106q9I3hjEstsP3TusP_bwT3tEV0gXyFEvTONXNqTj5LClU4-ehReza6FnAhUoBXRh5xq3OPtuCrgCux6xtPdqP4vxpk4GgI-bWDdciGF2A56tlGY_cTlpwWYOvhyRCD3GC8p-ytH1p_34wekvhcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b36cc97a.mp4?token=GTFBalYgoJTBhQOROk-cfojQ1ftiyQhb4HN1YRxZjTER9KGwR9cwn9JC9BoBlFLbItltQ1ToNvjFiNwETZ5s44R4qyDiiqpZPgrYEFCLx4jRmlnQVYNPiXfuzOMgg97ykEHxKF7Anv9tS1381_Bvap5ZS39Z_cn_ZmcsHjUqck57nD_yCgPnc3Fz4AniXot-jqD_u88WQ1KqOHttP1E17ZOGoz3fAIZ5ycuu3QBmcCe6lUtYp1Jmx_jCZ60ursmINCB7jwPM6v56I50IiTJswlHu8bWKrdF9eGoXTYygSZH7Vv9G8zvozvXmbUE_T_Ki7_sM_NZhZVHQlGIToEKtbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b36cc97a.mp4?token=GTFBalYgoJTBhQOROk-cfojQ1ftiyQhb4HN1YRxZjTER9KGwR9cwn9JC9BoBlFLbItltQ1ToNvjFiNwETZ5s44R4qyDiiqpZPgrYEFCLx4jRmlnQVYNPiXfuzOMgg97ykEHxKF7Anv9tS1381_Bvap5ZS39Z_cn_ZmcsHjUqck57nD_yCgPnc3Fz4AniXot-jqD_u88WQ1KqOHttP1E17ZOGoz3fAIZ5ycuu3QBmcCe6lUtYp1Jmx_jCZ60ursmINCB7jwPM6v56I50IiTJswlHu8bWKrdF9eGoXTYygSZH7Vv9G8zvozvXmbUE_T_Ki7_sM_NZhZVHQlGIToEKtbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💚
#استوری
کلیپ های ولادت پیامبر اکرم (ص) و امام جعفر صادق (ع)
✨
از عرش پیام سرمدی آوردند
بـه بـه چـه مه زبانزدی آوردند
در روز ولادت امام صادق
یک دسته گل محمدی آوردند
@Heyate_gharar</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/685292" target="_blank">📅 16:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685291">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
قالیباف: ثمره وحدت چشاندن طعم شکست به دشمن بود
رئیس مجلس:
🔹
پیمان‌های منطقه‌ای نوید بخش مرحله‌ای است که همسایگان به جای بیگانگان بر ظرفیت‌های خود تکیه کنند.
🔹
ثمره وحدت چشاندن طعم شکست به دشمن بود. امنیتی که بر دخالت قدرت‌های فرامنطقه‌ای بنا شود، شکننده و وابسته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/685291" target="_blank">📅 16:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685290">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0IMff-RKMILoN8ript04lkBt7Mblm3CLQn8Uz6lKuIN1B72MWxL-2lWiHSwFSEqZeIMyNcgA2eBh0rASC6ZYTaxkJg16jYxMWugPou5YNMGup6_uqTQ83af_vbNTs7QKdioNff_jq5wG037ZPScuNfwKBG0MQ3hxkZvZdHmFhyr56Iu4jYC6IF6jh4RdA8oM2uPu7oaCN-BFjL102_qzLntTbMn069z8h3UWtbmq0lI5FxVKgC98-YlB9P8ppINNxuXTDTN3My8ZpSLv8xIDRy1v5OaJkGTOwXMtRK6dKC1VQs-d6dVj6RKMTnxigBI340cATo9QHqmYbZ1e_CLxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آب چغندر؛ نوشیدنی‌ای که از کلیه مادران باردار محافظت کند
🔹
پژوهشی روی ۱۰۸ زن باردار مبتلا به بیماری مزمن کلیه نشان داده آب چغندرِ حاوی نیترات ممکن است به بهبود جریان خون و کاهش برخی عوارض کمک کند؛ البته این نتایج هنوز اولیه‌اند و به تحقیقات بیشتری نیاز دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/685290" target="_blank">📅 16:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685289">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1e225587.mp4?token=sm6C4SaGtwwbIjrSPhKWvvrRjo828cm2hZFsmG37ajS-0OEi2kDdpnRUgRhDmlAFZLQ3nLxcHhgqMop6jfxlHc1CO88VBoGP4SXCQoo2fkuqgNYM1Jk6_tAqomf19ox9zghgPchQuGWmaZaevmh4jQEqbWdzY5NYpIkg37neBO1_3sB0VLQ2NlIQL_H87jpFB0On7EQ58DY4TzGjl6lzUJtgvpVqGozDJjJ8d_WGQNj7O1f-zwodW_YKnA9YeVPixGXUTwjB6CPgtXkcI3YEnn2QBrA5E_gguimXuO06zt-sbJLTx1rkwad83KXRx_iiO2VtfB81K47x3Syg2E_WCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1e225587.mp4?token=sm6C4SaGtwwbIjrSPhKWvvrRjo828cm2hZFsmG37ajS-0OEi2kDdpnRUgRhDmlAFZLQ3nLxcHhgqMop6jfxlHc1CO88VBoGP4SXCQoo2fkuqgNYM1Jk6_tAqomf19ox9zghgPchQuGWmaZaevmh4jQEqbWdzY5NYpIkg37neBO1_3sB0VLQ2NlIQL_H87jpFB0On7EQ58DY4TzGjl6lzUJtgvpVqGozDJjJ8d_WGQNj7O1f-zwodW_YKnA9YeVPixGXUTwjB6CPgtXkcI3YEnn2QBrA5E_gguimXuO06zt-sbJLTx1rkwad83KXRx_iiO2VtfB81K47x3Syg2E_WCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همه فکر می‌کردند ایران ضعیف شده؛ اما جنگ ۱۲ روزه و رمضان تصویر دیگری نشان داد/ ایران قدرتمندترین کشور اسلامی در جهان امروز است
دکتر بیکلینی روزنامه‌نگار برزیلی و استاد روابط بین‌الملل در
#گفتگو
با خبرفوری:
🔹
بعد از تحولات سوریه در اواخر ۲۰۲۴ و تضعیف حزب‌الله، بسیاری از تحلیلگران بین‌المللی تصور کردند نفوذ و قدرت ایران در منطقه کاهش یافته و تهران دیگر توان پاسخ مؤثر به اسرائیل را ندارد. اما جنگ ۱۲ روزه ژوئن، این برداشت را به چالش کشید و دوباره بحث درباره جایگاه واقعی ایران در معادلات خاورمیانه را مطرح کرد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/685289" target="_blank">📅 16:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685288">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e67f6fc6f8.mp4?token=JGmbAUCcXrnbtVGp1-TDGh8PFEYGAwaGJal66vGRK_TinyVFlFbVb5Tao23Dlyz_u-E8LdiW39Yej9Z_JHNanel4ipQFvDq-2KiXd7gSFlu2Y-oytMmlEtYJpugqUazTorCyFfS_3ctfKZOj7xsANsdV2WmRH1cm8P7vWfZ0s6CljSAXfRy6x8W8LBzz8R3nuhbI1RYu0lidE2fUBmbULN9ZAmB4do6pLbq5jKceVYCDyBU4nFDnArFDdUiVP1dzIDry4ngNokUs_l4T4mg-XG7FnmKc9Z1Gaf1z0UDFsTiK28CJsEe97TGgMIb1h6VRRjPQe_5xRqXwuMIq4hkYZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e67f6fc6f8.mp4?token=JGmbAUCcXrnbtVGp1-TDGh8PFEYGAwaGJal66vGRK_TinyVFlFbVb5Tao23Dlyz_u-E8LdiW39Yej9Z_JHNanel4ipQFvDq-2KiXd7gSFlu2Y-oytMmlEtYJpugqUazTorCyFfS_3ctfKZOj7xsANsdV2WmRH1cm8P7vWfZ0s6CljSAXfRy6x8W8LBzz8R3nuhbI1RYu0lidE2fUBmbULN9ZAmB4do6pLbq5jKceVYCDyBU4nFDnArFDdUiVP1dzIDry4ngNokUs_l4T4mg-XG7FnmKc9Z1Gaf1z0UDFsTiK28CJsEe97TGgMIb1h6VRRjPQe_5xRqXwuMIq4hkYZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای تکان‌دهنده درباره جنگ اوکراین؛ روایت‌هایی از سرقت اعضای پیکر سربازان کشته‌ شده
🔹
اخیرا مشخص شده که دپارتمان پاتوبیولوژی اوکراین تمام اعضا حتی استخوان‌های سربازان کشته شده در جنگ رو سرقت می‌کرده و به جای استخوان‌ها چوب داخل بدن می‌ذاشتن و باقی اعضا رو هم به همین شیوه سرقت می‌کردن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/685288" target="_blank">📅 16:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685287">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pk82BLmZpCIobIhmpl4J1WwzyahZ1vb5JXU2Qc7IE5rgoKjLy0Fe6URB6RZnAT99ECR1BFRcj7SRWe6A59jlLSpWqUePZBqUiA5wF75Uqfu3hra-I0KYwDDqRtOY7xNXMDiQy_ENcXboyLMTiYTKCyVRCVoTIzmrzeh5ZDgfWgytEjk2D0I15EI2fS8tPMTzxEuHPB-csMctVz9xlvUBxxc-AIfTslm-_snT7QN_WgcOTJ0lb9RVvsWWOr67U9CT-Ea5-g7GzxOUOueFkBJI2nALotYr5w0uQjfy2H-5Ct-K815FYx9t6G2KeTZfOJnjgELjB7k_60a1Vazfg4iY1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایرانی‌ها چقدر بازی دیجیتال انجام می‌دهند؟
🔹
صنعت گیم در ایران به یکی از فراگیرترین سرگرمی‌ها تبدیل شده و بیش از یک‌سوم جمعیت کشور را درگیر خود کرده است.
🔹
بر اساس آمار بنیاد ملی بازی‌های رایانه‌ای، ۲۹.۳ میلیون بازیکن در کشور روزانه به طور میانگین ۸۳ دقیقه بازی می‌کنند که ۳۸.۳ درصد آن‌ها را زنان تشکیل می‌دهند.
🔹
موبایل با ۹۴.۵ درصد پرکاربردترین پلتفرم بازی در ایران است و از کل گردش مالی ۷ همتی این صنعت، ۶.۹ همت آن صرف خرید کنسول و لوازم جانبی می‌شود.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/685287" target="_blank">📅 16:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685285">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df6939ca53.mp4?token=smeeKbG9HPS2keTIJUbMBhsN8lKO4-AtkRKhq5uMrVAckWnFheBuuRaxFK565QqnbdOLI4va2M3Xptjbf07TToer_UFK6cI9jj8IIjS6W6I188ICZfL6IqA-vVyie7V0auGRSMIgqxmxVkM9pe-F-ICUhYp3V525aeGX-Tyy-lLqsyf6xjxLxS_Qxd2TxFRrPILvTVyX8N4h9Oaas1OagS9lldyr_kBn1Ha7boedcEoOagM39LNrokKuhOf-9fsMBqiMruTYkjgo-bk4Sf6fR8Du3CqOZt-2WWmqOI-KPTwQis_fUIjXlRr0kwMoDqeMUU-qf7702_q0pv3ELoXpgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df6939ca53.mp4?token=smeeKbG9HPS2keTIJUbMBhsN8lKO4-AtkRKhq5uMrVAckWnFheBuuRaxFK565QqnbdOLI4va2M3Xptjbf07TToer_UFK6cI9jj8IIjS6W6I188ICZfL6IqA-vVyie7V0auGRSMIgqxmxVkM9pe-F-ICUhYp3V525aeGX-Tyy-lLqsyf6xjxLxS_Qxd2TxFRrPILvTVyX8N4h9Oaas1OagS9lldyr_kBn1Ha7boedcEoOagM39LNrokKuhOf-9fsMBqiMruTYkjgo-bk4Sf6fR8Du3CqOZt-2WWmqOI-KPTwQis_fUIjXlRr0kwMoDqeMUU-qf7702_q0pv3ELoXpgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی تماشایی از قدم زدن فلامینگوها بر روی دریاچه مهارلو
🦩
🔹
ویدئو از حسین پوراکبریان
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/685285" target="_blank">📅 16:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685284">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
گام بزرگ ارس در مسیر توسعه | مروری بر پروژه‌های افتتاح‌ شده
🔹
همزمان با هفته دولت پروژه های مهم زیرساختی، ورزشی، فرهنگی، عمرانی و صنعتی در منطقه آزاد ارس باحضور دبیر شورایعالی مناطق آزاد کشور و استاندار آذربایجان شرقی به بهره برداری رسید.
@arasfz
.ir</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/685284" target="_blank">📅 16:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685283">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead0270f87.mp4?token=Ygq17anvG0-_LWXWYDJEkqQrHqA4zEo5NoxL4vdt7RkrYFzhfMKldpQUNaDQNr8E92Y2isSndbLOHGd2cIMfs6QQt8mbZ-Z83h5_rXt5RfaBueCjbCaAbFovHUYsF_fcTDQm6ui_sm0IGzLvWTf4k86C6fjg2q-lrLgK-KvrOdBAe_b6NInTZDpHUpQcLbHog9S-NhNynuQC7e_e-X6SvWKe0ieY5yxyEoKoKpWz0qiOLih7tgubkcQY80dj92ERLIqPt6DNxQCxsdHVZdh4G1RXoHPFAZ9uqtDvedd6DRwtgVBajrALR6iyQqIOsIpa5n7leqDOeQWWPA_f17nlCHVZwV5kfFi8ryAX4iBqtrwKK7oku794s23_suz5OxCvbfET4UHNW2WWTdtzvG8q8KC-uXgZOi6Dg1Wn06KCX0OVU1K67yX-ntbmSyGX5tv62EYl668zaH9i2I9nkB1KSUbLHPg5jWeQN0I856a_4FsMwM95jhn8m_dTSg31sqCEa5kYLNYKJeDZJEDPoN4bVFrpjqInnk7tg_cAyD59kFx0s7y_U_pGbajzz7Dk6XmCxNAZCpfDP5q09fy4l5HWQB3rUanzT-2CpbLwk-wyhMRHj9vXGcNiOpyf4vIORsyXB0z8IpgsuE6gX8DCgeOp6sWbCNLeSZkJVl-FJxnf8bE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead0270f87.mp4?token=Ygq17anvG0-_LWXWYDJEkqQrHqA4zEo5NoxL4vdt7RkrYFzhfMKldpQUNaDQNr8E92Y2isSndbLOHGd2cIMfs6QQt8mbZ-Z83h5_rXt5RfaBueCjbCaAbFovHUYsF_fcTDQm6ui_sm0IGzLvWTf4k86C6fjg2q-lrLgK-KvrOdBAe_b6NInTZDpHUpQcLbHog9S-NhNynuQC7e_e-X6SvWKe0ieY5yxyEoKoKpWz0qiOLih7tgubkcQY80dj92ERLIqPt6DNxQCxsdHVZdh4G1RXoHPFAZ9uqtDvedd6DRwtgVBajrALR6iyQqIOsIpa5n7leqDOeQWWPA_f17nlCHVZwV5kfFi8ryAX4iBqtrwKK7oku794s23_suz5OxCvbfET4UHNW2WWTdtzvG8q8KC-uXgZOi6Dg1Wn06KCX0OVU1K67yX-ntbmSyGX5tv62EYl668zaH9i2I9nkB1KSUbLHPg5jWeQN0I856a_4FsMwM95jhn8m_dTSg31sqCEa5kYLNYKJeDZJEDPoN4bVFrpjqInnk7tg_cAyD59kFx0s7y_U_pGbajzz7Dk6XmCxNAZCpfDP5q09fy4l5HWQB3rUanzT-2CpbLwk-wyhMRHj9vXGcNiOpyf4vIORsyXB0z8IpgsuE6gX8DCgeOp6sWbCNLeSZkJVl-FJxnf8bE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای آذر منصوری: پزشکیان گفته نه تنها استعفا نمی‌دهم بلکه برای انتخابات ریاست‌جمهوری بعدی هم هستم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/685283" target="_blank">📅 16:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685282">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ceHRbWM8AQHajoXs2a6LQuGX05JkLzxR9G2414yyD2DSuxTT4j051Sws98Qxhyd7PyXFmHvUQYsv2ex-UdVhwPa2W5NiuYigkMgyJeLlplxlPaBKJCfIxkGQ_ywETXhbVoFtWZqRw84WycMhkUmiN6-Q4rSm6QN1SGciaR_rVAEVVZlxqiUR2JmgDtN6DEt382r7dmWvLbhrvRXDTHVuLKZ0r9K2jjUN09VzA_hRG30yssFXipinjzWtbGkCI554MRlGiTFUeIPXXeQ7aR-WmbVAyZKevL5_W9BPzyCq8K0QVPOv066xXkb3u8E5-a1CbIf7iSaR7WOnc-Hhnq6JzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اقدام عجیب دانشگاه اکستر انگستان: توافق با عربستان سعودی برای آموزش افسران نظامی!
گاردین:
🔹
در قراردادی، استادان دانشگاه اکستر دوره کارشناسی ارشد را در دانشگاه دفاع ملی ریاض ارائه خواهند کرد.
🔹
دانشگاه اکستر طرح ایجاد یک «مشارکت رسمی» با عربستان سعودی برای آموزش افسران ارشد نظامی و مقامات دولتی را تصویب کرده است؛ تصمیمی که به‌رغم نگرانی‌های دیرینه درباره کارنامه حقوق بشری دولت عربستان اتخاذ شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/685282" target="_blank">📅 16:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685281">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8e0dfd548.mp4?token=RrmjcCGAi2Bo9bxV1JEVCgQg5LtPE4VBvwBnJc--hx8x7vNSNe0H2hflTSvgJuZdpELfMVtomOQDoC03jDw-PtzawqLKjk0RKhS6bgEAhYl4OI1916hjso5YlZ8ykByfI46FF_3PjcT2fCU9KnbyGiPCaYGopCkmqh1qTR2IZzGskXNO67QTPEpY1SNKwRbDdpHQm8-Hz7EnKK2mq7o6g0YWWJQGBfyb0rcGFs6mSlmRMjCr1TMHoDjzjEuW0g_yAVliE7mBPgMrv-o6HuzRC9LePWUE6ZRRsB10YnSxQ-QtTm-l6v3d3ZWBw6lvZ706W2pMEFwY3tGUWHpx_okCeYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8e0dfd548.mp4?token=RrmjcCGAi2Bo9bxV1JEVCgQg5LtPE4VBvwBnJc--hx8x7vNSNe0H2hflTSvgJuZdpELfMVtomOQDoC03jDw-PtzawqLKjk0RKhS6bgEAhYl4OI1916hjso5YlZ8ykByfI46FF_3PjcT2fCU9KnbyGiPCaYGopCkmqh1qTR2IZzGskXNO67QTPEpY1SNKwRbDdpHQm8-Hz7EnKK2mq7o6g0YWWJQGBfyb0rcGFs6mSlmRMjCr1TMHoDjzjEuW0g_yAVliE7mBPgMrv-o6HuzRC9LePWUE6ZRRsB10YnSxQ-QtTm-l6v3d3ZWBw6lvZ706W2pMEFwY3tGUWHpx_okCeYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بخیه‌زدن بادکنک بدون ترکاندن
🎈
🔹
این تمرین یکی از دشوارترین روش‌های آموزش جراحی و تقویت مهارت‌های حرکتی ظریف در رزیدنتی و جراحی است. کوچک‌ترین فشار اضافی یا زاویه‌ نامناسب سوزن، باعث ترکیدن بادکنک می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/685281" target="_blank">📅 16:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685280">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4U-OWIQE-88VpwkwG4mOpcn9U-gKODMkAwZ7d2XOAtT1sBSxsSIvbp1HEYBP-kcVdWy_vM_4Qb5t1e9kMI63JTKtIUJ7ddvYdqmh_EkVQsLCqOmAo3MbzbIDsTdedL8Tp7lk1G18JRVUr87BCLLUkXbDhd6ffpo5IfsJL9OrRYStLjVATYvsopAMYndYm7aGziyGAApS833XdRrtkNttzzkvTd-WMl1csmSuIOeNKW613Jo_IU5NHFUYGJzyC9Re9EXxT5dxRRiwP-xOGth4P-X3gBggLjj005YSyPiOG3YdHOOeSlX-YMyuHwHGuH655VPasagIDx1ZNNNtmV-8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هزینه انتقال نفت از عربستان به چین به روزی ۶۴۷ هزار دلار افزایش پیدا کرده که تقریبا سه برابر خارج از تنگه هرمز و از عمان تا چین است که روزی ۲۰۰ هزار دلار خرج دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/685280" target="_blank">📅 16:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685276">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kdESKUkirgUT2MwTKH1s0Vjc7_xdOHchKpV19KVmD2sCBar2ixNau91wl8Uy4g6nwHwo8SabmbGfpeoakwMdIvr1f2-hLY1hDZ8_2an_oGzc0FxkSDEe9nxubNxXqBysEo7dqtJcMkPv0FhzEH00pQ9Vj0ECwP4xzMO8BLf5OzSUhlDDYWA2vZT_mqW0EFaDoodYnlSc-OPU3gLqFKWS1Wy1PNhazk66DtNGA3oIusWHQbZ5JBYeSldciAw7O1EkgkqQJxOoz9mpqaEvxDAZ1XFdn_BmBHbsiJu6W6ZpPDxXs7yK5w2ugMHn50QQCbLdoBWU9O3kblDNWso4mQecvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H8LZla2hMXPwmmjBTQhd_Y7WUKsyHYfRvXrZyi-uw6GT_f-8kl4Kvy3wpN5S3MIW0h6_h3C90wFTGybNmquvaA0EPB_FN0jZEyXEn6eSe1DeyNTwtTw1sZhYeYmpqdvniJ3drvMrUCK7UsA3W5HEXkecahlOrIbEDdTl_yRQ9-OJN7RXWvwb4NcdPGeEr0sMIvItcsAyzxqKDMwb4xcKVLdR3yoe7-aNqtOYpq5EDVcjMYV6a_BiCLNvKZsWBpU2fiz6_tWjV97hCEjyeAgfxPELjo_SeCxFFkDys6xYYwgElKVpQ6maFguUtzBBzwi8sdzrJ2wtWEadawwMoYeFIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CLeMByiloYpZx14DaYRVoD94-USIDYqS6s6v1abPxsoNxZfUqnPHWmw7QJKa-bzhf2qnNQbM2j30BxENEtvrnlRio9RDhASUkaTKLjd3AAB481svlejHOUg0GuLXW8HX_h32msI_e9fu3izSpS0IGf8XrSrb1D4NJgy9xaG6D5nnMEgfHr16uUAc5ex6TfEKtaxJlAkzG61f-irm29mmL34YrmdeITGKNXfk29CDOcvTv8An0R7G43lbBa12t36DqrtVnzMl5LdGBvwr6AKfVmuQgrW7bFu2Aw5gVS-1FkUo23RXRJOAKN4pG98WKUDWxbIzhQ6LvE-_dyqJv9YWww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p8JB6hdeo7FHozC3NIzZydwum7kDCng5cixibniXBbrhZSykdzUraMsrXvAAjdWH7CA7Kem0w6c6FGlJrBL1DIW7x-RpdJAt9Lv6gR7kRKB6VXWXJPp7Om_2a5CAiDyQ00q7wB_XfMUpsYoa4Mx8rsgZ8mWqO9QfufuCfovxlXapjuJUJdn9zP509FCGYuTmjhfIcpX261STNNuK_6gdPImXwbWCk9eXYTs-3-q5qoax88yFNUduMaNCNvuV9lsR95ca6CjgeAzH42c_rH2ijVCXuM4JwwBsdVJNhuldvPQIZjAtI0jXeQ_EpEKW0dXoZTf142oehxhG1KSAxB1t9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تفاوت فارکس و کریپتو دقیقا چیه؟ توی این ویدیو چندتا از تفاوت‌هاشون رو ببینید #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/685276" target="_blank">📅 16:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685275">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKMC</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqQDKqwKQMUKKRxzFRvlMVnRPZ5UE-obYk4OxG45GpZjSa1kkJbkuckEoU-3RBx-kl8vv0p6jL4xQBbpQVu7yyVa1JaNuCKsEjCybiOIm_H-HAFZqjjDzJEwDr-PCfkjC4RnxkBPniKmjzTOz4v-bh7iuE-NLhUybE0UFTX4HuSviY3oWUH44tZ7UBu_NhsrylIsLqu3YENsl5oVdP1_42FcjgEZzzx17wKjZGeK9BFnfn02RwPbdffFf8ERyF5NJZjVIXvsR1sbqpCHV5xkOYRBYv7qhXach--KBH7PsxnyN7lri80S1CoWomefgxR01zVPKzveq0CrJvVrxayC9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
پیش‌فروش  BAC X3 PRO
ثبت‌نام: ۷ تا ۲۱ شهریور ۱۴۰۵
پیش‌پرداخت: ۱/۵ میلیارد تومان
تحویل: اسفند ۱۴۰۵ و خرداد ۱۴۰۶
مشاهده شرایط فروش
#kermanmotor
#کرمان_موتور</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/685275" target="_blank">📅 16:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685274">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فیش معوقه فروردین بازنشستگان تامین اجتماعی در دسترس قرار گرفت
🔹
سردار ابن‌الرضا: از ساختن قدرت دفاعی ایران دست نخواهیم کشید
🔹
مخبر: ملت مومن و استوار ایران، محاصره را به شکست محاصره‌گر بدل می‌کند
🔹
شرکت ملی پالایش و پخش: کمبودی در تأمین بنزین وجود ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/685274" target="_blank">📅 15:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685273">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1e657f150.mp4?token=QVeKmYdFF_wtDSTtmMMMXWXSjODGxXMlSy1dTGxeEbrFZkIaziPD62ZHcCjeLxoAiUn7ib0BRQBBioLKSHnnmNVliXZ_FUr9OQaR39g4GAS7_V9JrOA8BtTuZ3KgFNA-WRSSNHLXtqD-wHFYgwFvBxe7jPdf7srkZqdxw7xY-5SCBMdLVtt-m_TL3Hnz4UcNB7DbCykNQT6aHTpcwbZDJyzCQktb_mroqKsN9lMbx1sLg0uL8f6HPzdSWufIKsHu4UrYX4fRPtCHMSFhRUoE1zYsQaGj1t5AFpjH7w7Kg1PlTE2gL8jybfGauBSOCH-MJ6Y0nMjiFhNksRO-Vra1xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1e657f150.mp4?token=QVeKmYdFF_wtDSTtmMMMXWXSjODGxXMlSy1dTGxeEbrFZkIaziPD62ZHcCjeLxoAiUn7ib0BRQBBioLKSHnnmNVliXZ_FUr9OQaR39g4GAS7_V9JrOA8BtTuZ3KgFNA-WRSSNHLXtqD-wHFYgwFvBxe7jPdf7srkZqdxw7xY-5SCBMdLVtt-m_TL3Hnz4UcNB7DbCykNQT6aHTpcwbZDJyzCQktb_mroqKsN9lMbx1sLg0uL8f6HPzdSWufIKsHu4UrYX4fRPtCHMSFhRUoE1zYsQaGj1t5AFpjH7w7Kg1PlTE2gL8jybfGauBSOCH-MJ6Y0nMjiFhNksRO-Vra1xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور کندی: من تسلیح کردها را در نظر می‌گیرم و به کردها می‌گفتم هر بخشی از خاک ایران را تحت کنترل یا اشغال خود درآورده‌اند، می‌توانند به‌عنوان سرزمین خودشان حفظ کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/685273" target="_blank">📅 15:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685272">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
حمله خمپاره‌ای مزدوران سعودی به تعز
🔹
رسانه‌های یمنی گزارش دادند در حمله خمپاره‌ای مزدوران سعودی به منطقه «العرف» در شهرستان «مقبنه» در تعز، دو کودک به شهادت رسیدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/685272" target="_blank">📅 15:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685271">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7847268ce8.mp4?token=f5TyAunnLzJuO7rAOKULJUZxuyiLViIZz5SjLPX3H_kPlOuDrdKkbBrFeDo5udG9vsW08Sy36yAklSIneqfTPkwzy-H-9OQ0LJVCZBVw0EnH84C1S9JHDpD0nW0peQy0w5U6oibjFjtL7x0GERyzNSBla1LBtRBglEiSmbJ5Ejhhkqb2tFnCy9wf0JfgejqRu3g1BbXGhxTJAFHdwK4auA_H7wgfg0-N2logjB8AXyqEReRUUJgE6KFQjNvkEIQ8TVdAl7Sbbo7N7EcmlKTHehvNCm09SB1GjKZsYErHnMr9zOal1OOpyZRATqtWGbmS9hY_QwQJYr1Tvmp9qJgM_FN2h_q28Uq71YScKAryd97qOE9n7aADw7HNY28fRYeMwjt8-gUqnhg6OOAvjrd-XDgl0HcV6VJ9dJcr78MGfmW6ouKd_T6eh_OHXbJrmp5xVHpiMGBZPjjalBnM2T0rDjVJtuugDnopzBH9nBWwKuzqUREFZBnzOGZselUVsVxnY8rnvXYKXDQixHIGUPf-Lo37ma235y_3gxfD_OWcq8NysurNL_lHVCBG75l200kQ34jS5tsVlH18MJR-Li4Suj_ZBFABLA-4ihhHLQNo-Vkpuw4RsXV2r-b55YCG91aFIN-TzwQba_vbbpHarwfC3pvogbKTjxmOe0ZIRUuSLyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7847268ce8.mp4?token=f5TyAunnLzJuO7rAOKULJUZxuyiLViIZz5SjLPX3H_kPlOuDrdKkbBrFeDo5udG9vsW08Sy36yAklSIneqfTPkwzy-H-9OQ0LJVCZBVw0EnH84C1S9JHDpD0nW0peQy0w5U6oibjFjtL7x0GERyzNSBla1LBtRBglEiSmbJ5Ejhhkqb2tFnCy9wf0JfgejqRu3g1BbXGhxTJAFHdwK4auA_H7wgfg0-N2logjB8AXyqEReRUUJgE6KFQjNvkEIQ8TVdAl7Sbbo7N7EcmlKTHehvNCm09SB1GjKZsYErHnMr9zOal1OOpyZRATqtWGbmS9hY_QwQJYr1Tvmp9qJgM_FN2h_q28Uq71YScKAryd97qOE9n7aADw7HNY28fRYeMwjt8-gUqnhg6OOAvjrd-XDgl0HcV6VJ9dJcr78MGfmW6ouKd_T6eh_OHXbJrmp5xVHpiMGBZPjjalBnM2T0rDjVJtuugDnopzBH9nBWwKuzqUREFZBnzOGZselUVsVxnY8rnvXYKXDQixHIGUPf-Lo37ma235y_3gxfD_OWcq8NysurNL_lHVCBG75l200kQ34jS5tsVlH18MJR-Li4Suj_ZBFABLA-4ihhHLQNo-Vkpuw4RsXV2r-b55YCG91aFIN-TzwQba_vbbpHarwfC3pvogbKTjxmOe0ZIRUuSLyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنها امکان برای یک غرب آسیای صلح‌آمیز، این است که ایران به بزرگ‌ترین قدرت منطقه تبدیل شود
دکتر بیکلینی روزنامه‌نگار برزیلی و استاد روابط بین‌الملل، در
#گفتگو
با خبرفوری:
🔹
اگر ایران حتی قدرتمندتر شود، منطقه به سمت صلح بیشتری می‌رود. من هنوز معتقدم نوعی توافق میان ایران، عربستان سعودی و ترکیه، با میانجی‌گری رهبران پاکستان، امکان‌پذیر است.
🔹
اما امروز می‌گویم تنها امکان برای یک غرب آسیای صلح‌آمیز، این است که ایران به بزرگ‌ترین قدرت منطقه تبدیل شود، اگر مقاومت کنید و حمایت داشته باشید، می‌توانید امپراتوری را به چالش بکشید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/685271" target="_blank">📅 15:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685270">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eaad60905.mp4?token=AqywPrzQtLBRn1PbyjHOQkb51LeRstqyzZVk-U8GQMFUvAnDnCTVO9D1xiVA0gwboyM13vpJZqIYcTfl0U413Wa9rh-0VfJEClzg_OXvfR_CYH9SUgm0iggu61SWmJfgFHq6GthzbWVIW98Xsu_6lH1FQthb3X8wjPpC0_PSA-kYeJQSw7ATRzrN1x8AKHJRwaW-5wjC7f4MDSpiygdFk7wBnrbbbwXBwjNjrRynWt0xCadBwRglAIIV1mC9QMCWCTq4TqEf9VxlJwoFHKHcjNZHK1nNRdrftQsT_wXy_IF6Lxr7Qpx3Sd9PMEjKErOc1IWWpmrLLIKvFxBE9L4sMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eaad60905.mp4?token=AqywPrzQtLBRn1PbyjHOQkb51LeRstqyzZVk-U8GQMFUvAnDnCTVO9D1xiVA0gwboyM13vpJZqIYcTfl0U413Wa9rh-0VfJEClzg_OXvfR_CYH9SUgm0iggu61SWmJfgFHq6GthzbWVIW98Xsu_6lH1FQthb3X8wjPpC0_PSA-kYeJQSw7ATRzrN1x8AKHJRwaW-5wjC7f4MDSpiygdFk7wBnrbbbwXBwjNjrRynWt0xCadBwRglAIIV1mC9QMCWCTq4TqEf9VxlJwoFHKHcjNZHK1nNRdrftQsT_wXy_IF6Lxr7Qpx3Sd9PMEjKErOc1IWWpmrLLIKvFxBE9L4sMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر کنجکاو هستید بدانید اتوی بخار چطور کار می‌کند، این ویدیو را ببینید
#موشکافی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/685270" target="_blank">📅 15:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685269">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOggXnkQ8oHmsO-mGFwgFfbD7w_8ROGTyYlk910QhPVDXoKhmxGMQxgcf1p3Ey6jNMAHfS-xJlpIEgN0z53cryIeFLEROl1kDQzsZJM-MqFyRa8JJAAuBisGx0rWHNNbNSss3kXDkbRhC_jkCFURBhnY_PilhKCHDY1ud774R20bP1WltMRL9dwSVa2wwPIG_R7dLglMz-kymv1gLCJ2PUtgMlHsSMQCnfza5of49hy_klOGeuMFDCqcqPQ_4ywzdTzBdpIvLLTCg4CIozGkg8TkHqX4UWW4dFqNP4nBKIEglgxITXsrpA-eYX_xp67Dbi59GLpt3D5Qk5y1H_OxRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جدید ترامپ جنایتکار با شخصیت فیلم ضدایرانی ۳۰۰
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/685269" target="_blank">📅 15:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685268">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
پزشکیان: اسرائیل کاری می‌کند که مسلمانان در منطقه مشکل داشته باشند و با هم، درگیر شوند/ با وحدت با کشورهای اسلامی نقشه‌های شوم آنها را نقش بر آب خواهیم کرد
🔹
پزشکیان: اگر تفاهم‌نامه با وحدت داخلی اجرا شود بر مشکلات غلبه می‌کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/685268" target="_blank">📅 15:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685267">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
پزشکیان: اسرائیل کاری می‌کند که مسلمانان در منطقه مشکل داشته باشند و با هم، درگیر شوند/ با وحدت با کشورهای اسلامی نقشه‌های شوم آنها را نقش بر آب خواهیم کرد
🔹
پزشکیان: اگر تفاهم‌نامه با وحدت داخلی اجرا شود بر مشکلات غلبه می‌کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/685267" target="_blank">📅 15:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685266">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
انهدام تیم تروریستی در سراوان
روابط عمومی قرارگاه قدس نیروی زمینی سپاه:
🔹
یک تیم تروریستی به محض ورود به منطقه، مورد ضربه قاطع قرار گرفته که منجر به هلاکت یک نفر و دستگیری تعداد ۶ نفر اعضا و پشتیبانان این تیم گردید.
🔹
از تیم یاد شده تعداد ۲۰ بسته مواد انفجاری به همراه متعلقات انفجاری؛ تعداد زیادی سلاح جنگی سبک و نیمه سنگین به همراه مهمات سبک و نیمه سنگین و وسایل ارتباطی استارلینک کشف گردید. این تیم قصد انجام اقدامات تروریستی بر روی اهداف از پیش تعیین شده در جنوب استان را داشت.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/685266" target="_blank">📅 15:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685265">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ff27ae35.mp4?token=tSLxUWw0xXzlZILyrVs8StUNyiyL3Xr1y0cuxfj3xJ2JCDrvugjybFHUc6B8MywCj9B39YYU4Stp5owEb9BVXXACmBZbmKraR8O0w96RIK71hiN2Jp94bT6ve5HuJVfcvfb8KYVLVs3oRCS-VwvJbU285v_edCjyusQJaTFf56fx6dqh4JTi7hw_A29a8qzZ8MA3QC2MHBBxb34SIMs_uz__26ZMV15Kb9Zd64WWMfKYBQo3NY6zkEhC5NcUDBx9REqTuy22ZVGMMmnqNx1RWw60thXVoR9b-1kwEs3MhW6fUiODq8rdzuREVAowO0FW8UQPn0-NXvV-R8g48wV9Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ff27ae35.mp4?token=tSLxUWw0xXzlZILyrVs8StUNyiyL3Xr1y0cuxfj3xJ2JCDrvugjybFHUc6B8MywCj9B39YYU4Stp5owEb9BVXXACmBZbmKraR8O0w96RIK71hiN2Jp94bT6ve5HuJVfcvfb8KYVLVs3oRCS-VwvJbU285v_edCjyusQJaTFf56fx6dqh4JTi7hw_A29a8qzZ8MA3QC2MHBBxb34SIMs_uz__26ZMV15Kb9Zd64WWMfKYBQo3NY6zkEhC5NcUDBx9REqTuy22ZVGMMmnqNx1RWw60thXVoR9b-1kwEs3MhW6fUiODq8rdzuREVAowO0FW8UQPn0-NXvV-R8g48wV9Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت‌پرده تهدیدات علیه خریداران نفت ایران؛ بلوف سیاسی یا چالش جدید؟
صدیقی؛ کارشناس مسائل آمریکای شمالی:
🔹
تهدیدات اخیر خزانه‌داری آمریکا برای حذف «کشور به کشور» نهادهای همکار با ایران از سیستم دلاری، فعلاً در حد بیانیه‌های کلی و اقدامات نامشخص باقی مانده است./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/685265" target="_blank">📅 15:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685264">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbdMTebjtUc_kqB48W3V0kAb7ohpBp_NJpbEP9D8j76L4guChYjF5qF-mHPkRpSeZwQybU6DGmUbJdQO76IIQ_-vptlt9XoQrjpGMgqORrw-fdmYVnDEj5RYUegNR0Bg_nO7N1cc5F0z30zTBCumDObSX_CwZj3v4w6Nsw6JjMwxt0cLWzj1HWR_KRMqoiBB6lPgE0sC6HipWa_bJ6CfFFVaayzjXJEmjdpjZhYEIfhVdm018t0etqt46ixX1jj_Joqap9tcGi7rtsOKfBsXHs9qW1ofDUpSwZCEJTNwU1pvUMZtzfwjJu3YQT2Rwt3zYE4jWDuBlCyQ6V1iCRjAfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تذکر دکتر یامین پور به وزیر ارشاد؛ مخاطب دو قطبی نکردن دولت و دولتیان هستند.
دوقطبی سازی ممنوع
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/685264" target="_blank">📅 15:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685263">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcaIdypi2H5_o_UzGN9p0yzk0hbCtzi_2Mj4I9fOQDglLnpmnhvkFvIz-Dapcxw5UWti1ull2NSQg6xyNtJOpKkF3CLzY44hL21lOlVK890FcaUnQo3eNi4aTtbPLvabM8w7jrfX4D5Bu07FD9uow_f1KjhLIq3kCASctpgm5SovT9DgvLiQ5NFCD6TiS5Ejk-pqpf9b09WE9sry6MiylIG48dVOMT_xnSYpitvGk_wsK_eRIW794_9IC8uu5z-oqK5R1vGaN9XEIego43jqimYFo5amA3ltC7nh-BVTFgcp9ojehFczEuA4_AqGxAXNHxrR8YpZjcoPsuvid0MESg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: بازیگران همسو با اسرائیل به دنبال ادامه جنگ هستند| مصرف‌کنندگان آمریکایی هزینه واقعی جنگ را می‌پردازند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/685263" target="_blank">📅 15:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685262">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXWpA6f1q30HqoylhyZ9zvFhBZtKsQ4tijeUJ8_Ut0oeyspS2QoOSvNR0U6b_RYr6G7ybzrMMP5Iv6wkc1Rchtgq0aPL3TJqSXyVUHa_ElWJV34YCeRiomT8MyNT_x4eTplI6D2ayy_CCLW-Bv8SOzlXFNkn4wtjSbg-u-VbZN50RkMhEMDv8pIMkiDf-hENZ-T9WQbKGjLMs6dgRroBa5xMru2z-3P5QdoBzpmbdLzw_-Hj6oHupPM9ywV6rxzzb-gXizNox8oi8Hz-8c6IRIC3VFjLpR4Wnr1IwSjiM49QAmwZ_39CYcGCKzEwdqHwxQ4-71qhGO8nz2hKNebMqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یوسف پزشکیان: ما باید هر کاری که برای تامین منافع‌مون لازمه انجام بدیم اگر منافع ما در غنی‌سازی است، دنبال کنیم. اگر نیست متوقف کنیم
🔹
اگر منافع ما در داشتن توان موشکی و پهپادی است دنبال کنیم اگر نیست دست برداریم.
🔹
حیات و ممات ما به غنی‌سازی وابسته نیست اما به توان نظامی ما وابسته است. این دو قابل قیاس نیستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/685262" target="_blank">📅 15:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685261">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RP258UcWq9euCdZgu0OpavYKXmre7E30Ml9B2KEFO5OlUsgM6N2Zvv1w66k2HATZ5zQJHehHVR1kBfHq0O9I2Kv8WlRvXARVJo8Fzem5zUcgxQhtAJxGyVOMV7PklUdWrSUKBdqICz1NMbxDq9yHsFzXghuUVDSdgk7tb4coJ-cKJLbSQAfT0jfaN7i42oAOcGoA_iwgseRXtanqTIxHtFeAmLSi1grIuiqHKp77qZhDtbCb9VtyunkI0sXGQxAI0F5tX9UpA-MRl_Q7n1Ny2YFlaiHzy7Fim0rjgug2EzzWeyc3ZBixAZw5SmzGZZwoRyvdxgtL9eH8ocLI8sc_hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نانسی پلوسی: عملیات شکست حماسی ترامپ هنوز به یک هدف استراتژیک واحد دست نیافته است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/685261" target="_blank">📅 15:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685260">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cac48f96e.mp4?token=CNiMjip-7EpFTPQz6VUDmeFrmBd4zi5rGHDqjSyAmFNTpvHBLniEGdnRwZ2DufsHGGZ-oqXIGcySiJ1U3r9GfRkEAK1t6vsTXjGvJ3uv_j1GF1b4Wo0aUq2YEOGor3uQqgaw80QRGYFLaED3Cbc9d4Wj8mUaOAdfWgzFywcfdK6HEe08ykOkYFSE67NEYxDRZKrQqUxWT2GHx3kZ8gSfwucyYCKuIlWb4d3ljC5rVQ-CaUYLTm6A0p10zqDki8E-Idoqt4prT16ZpMl8fBgKwMhh6vI6WYaEfft33o97bitGnxeW6Ck9jm73aNLBcVVEO3JgsdWLH7BWRjNmQuzMiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cac48f96e.mp4?token=CNiMjip-7EpFTPQz6VUDmeFrmBd4zi5rGHDqjSyAmFNTpvHBLniEGdnRwZ2DufsHGGZ-oqXIGcySiJ1U3r9GfRkEAK1t6vsTXjGvJ3uv_j1GF1b4Wo0aUq2YEOGor3uQqgaw80QRGYFLaED3Cbc9d4Wj8mUaOAdfWgzFywcfdK6HEe08ykOkYFSE67NEYxDRZKrQqUxWT2GHx3kZ8gSfwucyYCKuIlWb4d3ljC5rVQ-CaUYLTm6A0p10zqDki8E-Idoqt4prT16ZpMl8fBgKwMhh6vI6WYaEfft33o97bitGnxeW6Ck9jm73aNLBcVVEO3JgsdWLH7BWRjNmQuzMiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معماری ایرانی یکی از بهترین نمونه‌های معماری در جهان که از دل اقلیم، جغرافیا و نیازهای محیطی شکل گرفته  #حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/685260" target="_blank">📅 15:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685259">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/206964d4e3.mp4?token=fymEnnyve-wEC2aAY5gaFTGUuZb10DCrmSq4Zdk3YTTrb64-hvhtcYEeYgSU0Gy9Pj9xWM2mvaAj6As0Q8QndJmVnNXW2XjHw8hCUKjTeOmkE-QRZzo_8qsAlNvopXtzT_N5a75OTH4jfOSqt1cdnRU39FuthqUhDDZrF2fw-j5VXlzeYRjpc6i5aLBIqqAb_whJ6s8WNd7auiSGsxGyoNU1jsaUh7JNLeT3an_G3n2iX4P6wqtgcmlpZBTAjpbo-7uoGjvbx210Y9KCmX28l78ykp-tEws3ol7fhw1VD0sdjq4lyj7fdXnAMJgAcIfHv7gXL4zPWdbJ9TTcYbCFBw5Jw2YkbAUimJsxM0NNLNnal9Yr-59My-qrdrfF5fHZ9VkYy2R9mDWsfy8z_pFCurbCKBaf4NaCXfe3eUN6GQElScvBMYM1ZZk1lfHT7GcO4GNSOl1-uVy98nFenW1scJxkbizS-qnzROBXFuDxyhA8QRk-9fHZ-tQbMrBjaDGjEOEkB6W1SgZskBPZVzZY2RNTD9ccEx6x1ESrQhW5t4rEMEb37TnFbiEMkgsEfW_u5Btt6Ya7mMCWzX8O9nYzDmuNjww1EDC9cL3pC-FyClcV8O5hNECg46ipEKq2Krcmv6r_QqAqwitLkRlvG1jzzkHHcbvb1y5An9OPq51Hxy4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/206964d4e3.mp4?token=fymEnnyve-wEC2aAY5gaFTGUuZb10DCrmSq4Zdk3YTTrb64-hvhtcYEeYgSU0Gy9Pj9xWM2mvaAj6As0Q8QndJmVnNXW2XjHw8hCUKjTeOmkE-QRZzo_8qsAlNvopXtzT_N5a75OTH4jfOSqt1cdnRU39FuthqUhDDZrF2fw-j5VXlzeYRjpc6i5aLBIqqAb_whJ6s8WNd7auiSGsxGyoNU1jsaUh7JNLeT3an_G3n2iX4P6wqtgcmlpZBTAjpbo-7uoGjvbx210Y9KCmX28l78ykp-tEws3ol7fhw1VD0sdjq4lyj7fdXnAMJgAcIfHv7gXL4zPWdbJ9TTcYbCFBw5Jw2YkbAUimJsxM0NNLNnal9Yr-59My-qrdrfF5fHZ9VkYy2R9mDWsfy8z_pFCurbCKBaf4NaCXfe3eUN6GQElScvBMYM1ZZk1lfHT7GcO4GNSOl1-uVy98nFenW1scJxkbizS-qnzROBXFuDxyhA8QRk-9fHZ-tQbMrBjaDGjEOEkB6W1SgZskBPZVzZY2RNTD9ccEx6x1ESrQhW5t4rEMEb37TnFbiEMkgsEfW_u5Btt6Ya7mMCWzX8O9nYzDmuNjww1EDC9cL3pC-FyClcV8O5hNECg46ipEKq2Krcmv6r_QqAqwitLkRlvG1jzzkHHcbvb1y5An9OPq51Hxy4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از درگیری محیط‌بانان با شکارچیان مسلح در تنگ‌صیاد چهارمحال‌وبختیاری
#اخبار_چهارمحال_و_بختیاری
در فضای مجازی
👇
@akhbarchaharmahalvabakhtiari</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/685259" target="_blank">📅 14:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685254">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vAQ1NXjrbcKEF-mIlVN5p_LMfYDRCgjHamlzZRmauJTaSNhO0wP2fQ0oXOrSYyB7UiHLUzUIs-VGz0mTtt5GPlOlEOglSujZnsNgjVsdwYWK78dVmckuTLC09WDmDTuLKE3IYaZcJjTuMlvWhg9jb1YzIyqzvZCF1t93dxLT7PbHCydSHhgZruWkKLtJFmHqA31kQ7j4ZBFSbG8qik0SBzbc5nHJecFYggp_qyjfVJT4SqIb-6mzzEWS2Z3jf_nK3WFDjgXDvY4n4OJ9ikMtN5MrmoBEfzrdQ761IHe4o4n39-GdEi9_bbXWDOIgQ4RJcaSjmkePAVWjhFF8ybVimg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g-vJev6NtZ2PLcDG1T29Xfv7nGbr8ZvfZTSl345IZ752KUl1NfwFmUTNDMhFrlHtpAbgOH0QWxdvfMiEuYzlVTmym0Fy6niVGQQSym0Fr1xGDPORRnz8WyAbR9zDf_2SUJUR_u80_SBTPKSn2dFAmwaALDpHTALEp7bNI9ejZbpH9d_vjBsUqXQA3EUv7c4OsZeWN3rdRObkEIyxOCdtjs3ziIQS_cLlcgzoJ55rUrIRRS-ohz-PG7qdaj5EkHUtfbLViBo9ZYEjoDZBHG08psrTEJ4ZmY1tVui9rPvFbAyxq03_Xgdy2V1MeC83WZUNQxvb_Pm3WzqpsKc4YDzpCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B7wFsO8VkRoaqrZ8qLycMd6ixx_H4B9BU9OZSRhHUYW5IHmhiQQ2JELd1iPD_zt_UtNbf_P9-9vlA78HkmNzhkeOwjS_g176dpYXHn9XObobVL_kfeHjx_AZT8SMmPLT7GOTYTd34_MFzz1_BydOL-If9RmSNd3V-oyhTPih0mgQgQb27SKy6ZCRBxd2EQF_u0hFrqKv07S5dMm1y8RvS1di0hMaZtv0ZVJ3C0D-MlMbwDOe0BzyASuwnUa5ZqGsCxOmIaOArigkl7FloQOAihpDfZEaLQlT4BYXUjBpoj4MuV_q-HEkogDf8qIQ1q11TxoVWhhIRWgyuWkuSwlUrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پیست عجیب فرمول یک عربستان؛ پیچ ۷۰ متری در ارتفاع ۲۰ طبقه!
🔹
پیست فوق‌مدرن «اسپید پارک» در شهر القدیه عربستان، بخشی منحصربه‌فرد به نام «بلید» دارد؛ یک پیچ مرتفع که در ارتفاع حدود ۷۰ متری از زمین ساخته می‌شود و نخستین نمونه در جهان معرفی شده است.
🔹
این پیست ۲۱ پیچ، اختلاف ارتفاع بیش از ۱۰۸ متر، سرعتی بالای ۳۲۵ کیلومتر بر ساعت و ۸۰ گاراژ خواهد داشت و با مجموعه‌های تفریحی القدیه ترکیب می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/685254" target="_blank">📅 14:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685253">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da07fe860.mp4?token=YHudjgE6c6KyX7uyJBsdqcu9_nHaKX-FeAJ12xLS7-TrBa1Uq1cC-TmIKkxitdsy5d5CspA8FPyYlINNFnBAi2cHEzpliXEY6_cRN9_S_ap1gkq31m0egm0RCfSdoqt3K9N0iDE_ID9O1GL8DMqQsbemoQhcmYo4Jnkh9MK68eS51t-fquI2Bg5is4XpljjVqkD9LGlECcXnBJQpunzTTPiGhw-mO6M2reJtA-nLGCePqZtJTFaqUR1F6nZ1YnJ_R6N7UZMtiVvnuCnNGzR49daAh3fCGnYCSfmZKgdwK0APcxUikRHYzd3J4GKdSRjFN1BBjlpDM3vuqtzQKRS0nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da07fe860.mp4?token=YHudjgE6c6KyX7uyJBsdqcu9_nHaKX-FeAJ12xLS7-TrBa1Uq1cC-TmIKkxitdsy5d5CspA8FPyYlINNFnBAi2cHEzpliXEY6_cRN9_S_ap1gkq31m0egm0RCfSdoqt3K9N0iDE_ID9O1GL8DMqQsbemoQhcmYo4Jnkh9MK68eS51t-fquI2Bg5is4XpljjVqkD9LGlECcXnBJQpunzTTPiGhw-mO6M2reJtA-nLGCePqZtJTFaqUR1F6nZ1YnJ_R6N7UZMtiVvnuCnNGzR49daAh3fCGnYCSfmZKgdwK0APcxUikRHYzd3J4GKdSRjFN1BBjlpDM3vuqtzQKRS0nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ چرخ زندگی
🔹
مسیر ساختن یک کسب‌وکار از دل خانه؛ داستان‌های واقعی از کسانی که با اراده، ایده‌هایشان را به واقعیت تبدیل کردند.
🔸
در یک فایل صوتی کوتاه (حداکثر ۳۰ ثانیه) نام، شهر سکونت، چگونگی آغاز مسیر و دستاوردهای فعلی‌تان را بیان کرده و به همراه تصویری از کسب‌وکارتان ارسال نمایید. روایت‌های منتخب در مجموعه رسانه‌های خبرفوری بازنشر خواهند شد
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/685253" target="_blank">📅 14:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685252">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmPb68b8Le-RosUCzys0WLtxFR-gBo6zwIuNztVfB-9sw8D5qAqpf_M_hju6c1HTa0qc6m7yJ46TC8beE3narAg2DPOLakTCfPUpaaz6vaeR7BSF7PHUOnJ11NsJDynOABqXLVuK9sobIYaMkMVAM5fW9jH9lIu65erQyU8CYXpc-cHzFwcBiQ9VO6FmeSeRWall_GsNjoxyjSqdIWWpD_xfVRUeOKFm73FGeuXxIEVhWf1MFDKkbiH2K8-JewOtG6OpKiw4zYCbde7kwqnjfeab9VtdySCU_AlqywYQg3n6If202pZzpu_lki7qKAATevMhiNeBGlEi3xw-658zVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عذرخواهی طارمی از هواداران الوصل
🔹
مهدی طارمی پس از شکست الوصل در دیدار شب گذشته مقابل شباب الاهلی با انتشار پیامی از هواداران تیمش عذرخواهی کرد و نوشت: «این فوتبال است؛ ما یاد می‌گیریم، پیشرفت می‌کنیم و به حرکت رو به جلو ادامه می‌دهیم. ان‌شاءالله قوی‌تر برمی‌گردیم و به موفقیت‌های بزرگی دست پیدا می‌کنیم.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/685252" target="_blank">📅 14:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685251">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c45f93b367.mp4?token=CFFiLkFqmVnRBR-UAQVQThcwgVtn-cGdI6V9kZA-ud0hmho_kLOk-a2UnSa_NrZ-XZfQlmsc4MudvfvUguyKR8WqvTmt-icbgrpG8OQO4LlrF0xIz6jOi3J5EY3e0cJ41NgEQQZvObMBxLmldXV9NHWXfywe39DqCQfeKFsozWMgyNhl5_VursXzo2WflMjyk5X_EAfO7LU2k5Z-5IXqyECRTIFlFkpeH_WCjL4dJDp3imuqzarrEl76ASziQBFQ07_tJjff-ez-cxJkIoCTsbjqG3JFvYdnoif9fKuX5oKKh1CqXQGzSKss75mhibS8yVtV1lnHY2ah8IPjl__5rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c45f93b367.mp4?token=CFFiLkFqmVnRBR-UAQVQThcwgVtn-cGdI6V9kZA-ud0hmho_kLOk-a2UnSa_NrZ-XZfQlmsc4MudvfvUguyKR8WqvTmt-icbgrpG8OQO4LlrF0xIz6jOi3J5EY3e0cJ41NgEQQZvObMBxLmldXV9NHWXfywe39DqCQfeKFsozWMgyNhl5_VursXzo2WflMjyk5X_EAfO7LU2k5Z-5IXqyECRTIFlFkpeH_WCjL4dJDp3imuqzarrEl76ASziQBFQ07_tJjff-ez-cxJkIoCTsbjqG3JFvYdnoif9fKuX5oKKh1CqXQGzSKss75mhibS8yVtV1lnHY2ah8IPjl__5rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میز نسل بعدی: ژست‌های ساده، هولوگرام‌های تعاملی!
🔹
با یک میز هوشمند جدید، دیگر نیازی به ماوس و کیبورد نیست. فقط با حرکات ساده دست می‌توانید نمایشگرهای هولوگرافیک سه‌بعدی را در هوا کنترل، جابه‌جا و دستکاری کنید.تکنولوژی فضایی (Spatial Computing) که آینده میز کار، طراحی، آموزش و حتی بازی را متحول می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/685251" target="_blank">📅 14:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685247">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gd4W3zOXmL51WV4jLCuJpk5TNpGWoGmasnK_hpoJec88dr4sl_tP8_wKkYywaUD8q4C35dRz2U0X9_fG9O0651ptjNIxBX01ph_JJHHmTaf13RkOGjZ36EtBoJiAt0T0NQsM_HY3W2hixrsNpjCUMxx8Mjyq9CPgdL6ESzuwKYrUm3f0zuD_BNEiQf_8guCwk9XYl0ilMn6zSYiDBsbhtE32F86RExkWMVcH8F_DhvfjIWXWwP-0ay27uI9GPp3ibcZimOKv02aY3fY-fG6qr6qDx0XfobBu9_WTOGmYlCJ_vLoVIVvD0fVK6FWL3t_zDrqLo6dEtVCW19ua_Kr1cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eKtqRHvK9d5Zjb3TB4KLxx1kLKv6Qo2uas2KKWQlEgeioC-qylg-sa5NDR_OWBltKMfmAmZ9THb2I1FyKAXTm7yKYQyBRugHw59tvrml71Y-Uq15v61LqgDXQ8c_ZPNHULhjFKd4Gsg_jmfnDC8Hikb6sGttml721YxyTrFcAOaobljMnhSFH1Gc3evtObXlF7Cl6KJRgpbeaOmbMhEjUljqaqTdu5pJJMoBglYwehtwI5_gYm9qJzCXXqV3K4rgOgVKrMWc4b-q67vXqSYuETYTJ87Fadr5u45HB2_jl12MYHLmTh8otkqL4DLrnhxP-FZfOderllQGtHXGbeGYfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jW5bBMSjuo8QaytZVr4qau3RUST2TPiLQxZPUnmJ7_YpsqcYtm8jCGk1-IwqUsDrRRC_sI7GBzzkiKkpjVaMKd6tVFHSeHYGDq9RnpHArGUpquokQymNC04rKIZfbApY0XbRD3z8s4JZKmCPIuqKQk5BeS-0LWaWCGlNKnHu615KEvUCJx1KsuMahP8HvcJyiCv0OurrPVX4Z-DUVWKwc2XvyiclThylKIrmCPxCPUuNpCE0MEXQQQJUhH35Xp9VGFp_qexpVQ7Qx4r8x1LhxyokC3lIpeNVO4sbxt7w9bmPd4oQl_8xFNSu6yHdmKNlvAv_GncneNt3VTYR1lx0iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hlic7dhMvXWsx8ApNImc_DfGYmGzAhYT1uMKlmwzLp4oqWzL2Dyfg3B0Ujh-7-UVUkIUWDZw1V4kou4m0qmVLWXDnp7bk6Oy24UkpLTzslGpJw68sh8AHgjx3XcMZV5FAwGBbt6qBQT5ts7ZlBjApD1eF5xsikwEXGqVTFVLWowspvjJy7BBqfrSDmfA7gj9Uih8XM__oVPESIcxvhEhBFmRNmLr3BVVckSsIVkKUEv74wwu0h2TnW3e1h-gwxTbl_-B0NlB41UmoK36JzNRN8w_P-bsYYrEE4O68veIw4uKg2TPVs2yBHV3ZW20ZhnvS5i4GAMa-ZHDfs0jQWF4Cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جلوه‌هایی از طبیعت شگفت‌انگیز مازندران
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/685247" target="_blank">📅 14:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685246">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e66a21da29.mp4?token=V1esgCKzin2TJ8X5p3q2eQK35y2LxLFweVkTf0TSKeZiblVM0cSq3zfUTxGzVj5fH6Gj46seD12kDfdWIOs_OjuygAgudzTjDNzg9SD_sb8F9IOZ85Ky99Db3d00rM7x_Y0jZOjE23y5oXesWFopD369MU6n8i0U-onmnjO64QUTz3i0pFcuSBf5_foJ7n5V6zqlMR22VW-o9x9l1n6lRAMscpCsk4Wgg-zJRyZMiB-ahwqf4_6p93lwJAceTh8V0slFC8by74NCRzMjhdf4tmnPnTH92v1eEZ6xwZ1D3jxfOp-472jbkzVFI4yqn6UnbCDmMx7EBv-NGUN3_jIX0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e66a21da29.mp4?token=V1esgCKzin2TJ8X5p3q2eQK35y2LxLFweVkTf0TSKeZiblVM0cSq3zfUTxGzVj5fH6Gj46seD12kDfdWIOs_OjuygAgudzTjDNzg9SD_sb8F9IOZ85Ky99Db3d00rM7x_Y0jZOjE23y5oXesWFopD369MU6n8i0U-onmnjO64QUTz3i0pFcuSBf5_foJ7n5V6zqlMR22VW-o9x9l1n6lRAMscpCsk4Wgg-zJRyZMiB-ahwqf4_6p93lwJAceTh8V0slFC8by74NCRzMjhdf4tmnPnTH92v1eEZ6xwZ1D3jxfOp-472jbkzVFI4yqn6UnbCDmMx7EBv-NGUN3_jIX0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آب‌گرفتگی مسیر زائران مسجدالحرام را بست
🔹
بارش شدید باران در مکه، هم‌زمان با حضور زائران در مسجدالحرام به آب‌گرفتگی برخی مسیرها و اختلال در تردد زائران منجر شد تا جایی که نیروهای سعودی برای انتقال برخی بانوان به فضای مسقف وارد عمل شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/685246" target="_blank">📅 14:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685245">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9PfYto4G4et26bOMqB0ILavFV2yI428-MFiZBdbsryimb3IeDmQy4z49HOcT6o5Aw-hDZUUA1fm49ppOEjBMkLry8zQrdnxGuawM7tkGxsFIGIns9nFMZYXwUCpDz76JeUE6WBS3kjKAF9eKvHhqMyXsMhowTj9PXkAE1Ifo64sHHX74nAPnm1ra9EQcTFr48BSeTh3n8qZ3QJAdH9SH6270Wv5B-CpTd6LIdY3HLTU5mOKgUnCOAf0m4SWcnK2H4tphzBxDRAdE5LxC3MJuagJIDpZ9_ZnAcWM1jmnRLQTlp3YclAtW3UT1NV-PfY2H9Df4zR8H4MRBbSWuJHHXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
"راب گرینفیلد" فعال محیط زیست طی ابتکاری جالب از زباله‌های خود لباس ساخته است
🔹
هدف او نشان دادن اثرات مخرب زباله بر روی محیط زیست و ظاهر شهرها می‌باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/685245" target="_blank">📅 14:06 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685244">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c657448ab.mp4?token=pcEJJ5G-psw3U_0hwsEEcEt6LFbhoBtSVUwuPZUlVeJxHdidsVzq6H_FQSV7W3rS7x2F04g1XNiRC4Tm9qGUCMOAWOA5emCRMtudFOCJMdxfUnNTv2ofEzCWEgmNHEqpVHVJFwVuZLzJ8dbauass9NzXM6aYI7abFoOpBgzYLrnmmimp864-s_vlqxWD-rZNcUeSXWuoqr-FmlI-Ui7X3Aol0uS28Y03x5uLd7sg1HJkIYq2W-xbCrJSZweb5hksMFilC96qu2NJTZbqjx0BcmZmZgWHRRzVfTzyQDZftBBkVilgOfTtInRvWHDRBj4E9d7ff0tp-5gHSJDwaunUZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c657448ab.mp4?token=pcEJJ5G-psw3U_0hwsEEcEt6LFbhoBtSVUwuPZUlVeJxHdidsVzq6H_FQSV7W3rS7x2F04g1XNiRC4Tm9qGUCMOAWOA5emCRMtudFOCJMdxfUnNTv2ofEzCWEgmNHEqpVHVJFwVuZLzJ8dbauass9NzXM6aYI7abFoOpBgzYLrnmmimp864-s_vlqxWD-rZNcUeSXWuoqr-FmlI-Ui7X3Aol0uS28Y03x5uLd7sg1HJkIYq2W-xbCrJSZweb5hksMFilC96qu2NJTZbqjx0BcmZmZgWHRRzVfTzyQDZftBBkVilgOfTtInRvWHDRBj4E9d7ff0tp-5gHSJDwaunUZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
به هرنوع رنگ‌پوستی کدوم رنگ‌ها بیشتر میاد؟ #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/685244" target="_blank">📅 14:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685243">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThLmgH0DKUMDSy439zHcWfDsSd6BNLCUw89I9xkoo8b6AlAj0FA4OUfckM4kNmGvq4Lp7K1_49YE7_XqM1XgZQM7D30uO0mzIldYq5yUnDKywZuOtj1UN6GBfh0gFd-6yo75GBgPqt-_JHvWz10Vf5doHyeXTzEQ6xbnkGHakbvsH9pskaNazqcnuX_xGY3btPNbortgKFlykFwZXN-AqkU45G1zyKTOtiB09yWEptKh_61xtCqbpNlvpa16qdXwOkxzvNTp3ROQqjVNqmcVORNh5_42yQwcXX7Pf-eMNOMsf-sW8xWLYeRQxdSfnrjDYABIbYUGcJGEx7ulpEua5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمان تاسیس شرکت‌های مشهور
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/685243" target="_blank">📅 13:55 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685241">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTbKxALKU_nTnWiuvRJNJijcl_lwKgLbt8wmd5iSaYs58kVHoEX9qSR0sU_tJOS8ChvimeKVODdwptNrwLZc0iRtTV0WQNBCdr2icXX8AZ7uoMKaNWxBtcJRsAX0Up9qIMHoxz7hfOOM0vOfeHYu3GlDDnJjRWogbaMQvB4ZRRoJkfw5h0avCKLJQ6OHjaoaznTGWwuyOkOgyrPUVeLdqcqtaoaAo0uv5z8AooqB0NBeSwb6lIEJ4tHtLjWRmzPKPJeh_WIEtIS10dXYxgwriaS3EKUDOuX52Jt3OW1NRouptNRJlGSdWk2vzCoWgWfQ7Uk39bYWjXCObEMwx4zBFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۶ سالگی و عمل بینی!
🔹
وقتی یک نوجوان قبل از اینکه خودش رو بشناسه، دنبال تغییر قیافه‌اش می‌ره، باید پرسید مشکل واقعاً از بینیه یا از تصویری که فضای مجازی از «زیبا بودن» ساخته؟
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/685241" target="_blank">📅 13:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685240">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/466edb2c8f.mp4?token=YpF4N4OYYoT2A65vH173p-mYqGUm49F9KcXIbmj3LnGEiBfaE-RFOafqxvdA9WHn-oRk2OQNQrjGRxmcuXZi5BzS4kprg9RpOPe_lGDN-FcTXR-DSmVaGjFvGnJ0vFCX_ejVAWugacuzxggjvrLeKNvfKyL744g_FeSM39IOTWMj6o_U0g63RF8EGKL0Mf7uSeKmDDfvJ1DCCt5RX1og5Ny-4rJ4GsIDXFKMal5NjLi4A_bQfmJN-U697M5XfmvgaVHcQaN1zmZxgOom6TF3VBfOURHkt12DfbcRlqFgbNG74uqpaZbs2a1q_uv7ti0EZUbNEcgabg-7DptpXrcZIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/466edb2c8f.mp4?token=YpF4N4OYYoT2A65vH173p-mYqGUm49F9KcXIbmj3LnGEiBfaE-RFOafqxvdA9WHn-oRk2OQNQrjGRxmcuXZi5BzS4kprg9RpOPe_lGDN-FcTXR-DSmVaGjFvGnJ0vFCX_ejVAWugacuzxggjvrLeKNvfKyL744g_FeSM39IOTWMj6o_U0g63RF8EGKL0Mf7uSeKmDDfvJ1DCCt5RX1og5Ny-4rJ4GsIDXFKMal5NjLi4A_bQfmJN-U697M5XfmvgaVHcQaN1zmZxgOom6TF3VBfOURHkt12DfbcRlqFgbNG74uqpaZbs2a1q_uv7ti0EZUbNEcgabg-7DptpXrcZIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعضی مرزها روی نقشه نیستند؛ در دل مردم‌اند و آن‌ها را نمی‌توان با هیچ فشاری جابه‌جا کرد
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/685240" target="_blank">📅 13:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685239">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/103c5fbd41.mp4?token=AQY1Z9OYDdUMQXA-PqNRO6lvrmmuNfgB6g856Wtl6nABVDcHp9Uldjr-1YS7Ib4y7i3m3JbjC1489xAph2k9Aze-2uJ53iDIT6WbtYHU9LYc7PDKBYrYQRGOvWUNy2hcN4eh49QfOVfSoRgSq9gB1OEBkGW92i26fhcHne5Rh4hOaGu3Uw3ky2Oq79tYQojylgO0p99kf8QuEbmEcMDtMItGHdWfnL40TRC23cApQ6dYFgZsLwKOJYNWHfkId6PRoB8Z6OcfGyz0HvHxAX3VHXqkTsXpS9rU70QdQJfj2Aq6t_HIEwrMmb2I9SmLppBeJNFeMIOrany9_VA8Y7f2vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/103c5fbd41.mp4?token=AQY1Z9OYDdUMQXA-PqNRO6lvrmmuNfgB6g856Wtl6nABVDcHp9Uldjr-1YS7Ib4y7i3m3JbjC1489xAph2k9Aze-2uJ53iDIT6WbtYHU9LYc7PDKBYrYQRGOvWUNy2hcN4eh49QfOVfSoRgSq9gB1OEBkGW92i26fhcHne5Rh4hOaGu3Uw3ky2Oq79tYQojylgO0p99kf8QuEbmEcMDtMItGHdWfnL40TRC23cApQ6dYFgZsLwKOJYNWHfkId6PRoB8Z6OcfGyz0HvHxAX3VHXqkTsXpS9rU70QdQJfj2Aq6t_HIEwrMmb2I9SmLppBeJNFeMIOrany9_VA8Y7f2vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عجیب‌ترین ساختمان در هند
🔹
ساختمان کاغذی هند تو خیابان بنگلور که افرادی هم داخلش زندگی می‌کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/685239" target="_blank">📅 13:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685237">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0fEDEkIiHFcvEoSHmIa3W6rjoZU8VNhu_TAzeR9QjFGbmX18BH0RNJJgpCbBrAcEszA_EUEUJ8HoMCdbVlmB1vj5WGe74c7_euk9xwFLgKe_B39mlGnW4wdHuI28vPv41XcKn1VHFf7OpnkscWJ4kqfB5popEuIoR3ywzg5k9Xpxio7GmR3-UuSW9Bn-4AbHp2ZrxiNGVa86UkCdyASDHU2ZRJstkEVWAaP_c4oT6UafLi0jXvi8z2wCmonBxMa7GelKrD8jc36AjsDu_pT1ovJAL5FUFHKHP2rZMEmYdHSNay0hdN_PiPmUfnXDHAW6VhU9AjVg5CsVuGnJdbc8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
کشف سنگ ۱۷۰ میلیون ساله  بعد از سیل وحشتاک نپال؛ غول ۳۰ تنی شالیگرام!
🔹
یک سنگ شالیگرام عظیم با قدمتی بیش از ۱۷۰ میلیون سال در منطقه موکتینات نپال پیدا شده که وزن آن بیش از ۳۰ تن اعلام شده است؛ سنگی که گفته می‌شود یکی از بزرگ‌ترین نمونه‌های شالیگرام کشف‌شده در جهان است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/685237" target="_blank">📅 13:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685236">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
اعطای وام اشتغال به سرباز ماهرها
سازمان وظیفه عمومی فراجا:
🔹
سربازان ماهر منقضی خدمت نیروهای مسلح که از اول مهرماه سال ۱۴۰۰ تا پایان شهریور ماه ۱۴۰۴ خدمت خود را به اتمام رسانده و کارت پایان خدمت اخذ کرده‌اند، می‌توانند از روز دوشنبه مورخه ۱۴۰۵/۰۶/۰۹ نسبت به ثبت درخواست وام تسهیلات اشتغال‌زایی اقدام کنند.
🔹
اولویت واگذاری تسهیلات مذکور با افراد برتر مسابقات، سربازان متاهل و افرادی است که در بازه تعیین شده زودتر نسبت به ثبت‌نام و تکمیل مدارک اقدام کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/685236" target="_blank">📅 13:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685235">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/km4JmFQVNwCtA0IP3wzw-grWr_Iqr5agwh2dMN6Y16wA-dkGFpURZBWyemBNHjpKbuATjFeLglAVNE8Wz3M_jp7cHTD6ukWfDsO1nrbejtmPV4Zr1jQhh-4TcnA5Vx4Yfuo287lsLjpSL0Ae7BjIyfgiANWKR89O3qcIuJbf9Kq5J42LeAl77XHp3vFPiXmiil34KKF7d2A_MC4BB3V01FNOYUNl-hhKybhO4e09Yp9U1Uoynk0KtEQ7zxLOjw0xY5CAPCzfEf2fIccltd5KGh1h5OBoxjZCz4sq3kIZNvbF1Kwl66qKU-GyroJV2rYjYkOR_2vmqJeYD8jaWSs2oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تغییر سهم اپراتورها در بازار مشترکان تلفن همراه/ افزایش سهم همراه اول در بازار مشترکان
🔹
گزارش بهار ۱۴۰۵ سازمان تنظیم مقررات و ارتباطات رادیویی نشان می‌دهد سهم همراه اول از بازار مشترکان تلفن همراه، از ۵۴.۲۹ درصد در پایان ۱۴۰۴ به ۵۴.۳۷ درصد در پایان بهار امسال رسیده است.
🔹
این افزایش در حالی اتفاق افتاده که سهم ایرانسل در همین بازه از ۴۲.۲۰ درصد به ۴۲.۱۰ درصد کاهش یافته است.
🔹
همراه اول با این رشد، همچنان بیش از نیمی از بازار تلفن همراه کشور را در اختیار دارد و بزرگ‌ترین اپراتور موبایل ایران باقی مانده است./ فرهیختگان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/685235" target="_blank">📅 13:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685234">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9325e0586.mp4?token=iRcuJNqWbIctvOqvVYspsLrfJ5BYUlzeSGKFaI3La5vH8_NPeZBoeBYzjvXt2ar36sp_1-mTb24M2M4TZdbyh3hgeXETZF3RTR5LYI7Po3Fao5NNpFfWyb6cxMmIedxWM7V4XI7KCrpb2wzqU0khXilb6xqMxhkMQUuSW0jLb9NnrudRYDIxTmMdAmv3r-ffAMmkY9rqAt4CdFtPuZueumWCWgC_QaG2RV_fQF3Y9QAT6GuYmCAzw-99llaNKih84cozURrN6k86kp30DausjalVu0BB4CPujFatBzubUHO8EItr2QwLM-tVtB_wswIhMayOGA5QxppXR37WdEQYJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9325e0586.mp4?token=iRcuJNqWbIctvOqvVYspsLrfJ5BYUlzeSGKFaI3La5vH8_NPeZBoeBYzjvXt2ar36sp_1-mTb24M2M4TZdbyh3hgeXETZF3RTR5LYI7Po3Fao5NNpFfWyb6cxMmIedxWM7V4XI7KCrpb2wzqU0khXilb6xqMxhkMQUuSW0jLb9NnrudRYDIxTmMdAmv3r-ffAMmkY9rqAt4CdFtPuZueumWCWgC_QaG2RV_fQF3Y9QAT6GuYmCAzw-99llaNKih84cozURrN6k86kp30DausjalVu0BB4CPujFatBzubUHO8EItr2QwLM-tVtB_wswIhMayOGA5QxppXR37WdEQYJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک فرود انجام‌شده در شرایط دید صفر، از کابین خلبان بوئینگ ۷۳۷ فیلمبرداری شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/685234" target="_blank">📅 13:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685232">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
با رعایت این سه مرحله روانشناختی دیگه به راحتی از دست حرف هرکسی آشفته نمی‌شید #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/685232" target="_blank">📅 13:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685231">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc5db577a5.mp4?token=OcXqAh5U_Apq1B2ati1keEtv1-QDa7LISbDliiy3L7B8tbbk8G5uZtb0p-dC_mDohNQ-pLumL4VsKkC7ua8XGa5d0MF5g7drgBaXKttWrv4OSCFtN1XG-MmEHNNu1s4qqJJhK6-jmW0vbBrjf2nS_V6KvMyOa9Hsr0icvSEAz04UEseW8wqYk3b0ZVq0DzzBBai6lxIS8-cVqgwd_jYdM4HheOmjAC8lTMAsgnd2-lLkJdQFEjzI7rr2xxBRsBIsJE7DCDqMYAhrLvectIfd5bUouEDfhbD2-RQFQziSJnMHbgNalzkwnXr3HFgvoHhFrC6f3OSYSckiWTI8Z1VbqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc5db577a5.mp4?token=OcXqAh5U_Apq1B2ati1keEtv1-QDa7LISbDliiy3L7B8tbbk8G5uZtb0p-dC_mDohNQ-pLumL4VsKkC7ua8XGa5d0MF5g7drgBaXKttWrv4OSCFtN1XG-MmEHNNu1s4qqJJhK6-jmW0vbBrjf2nS_V6KvMyOa9Hsr0icvSEAz04UEseW8wqYk3b0ZVq0DzzBBai6lxIS8-cVqgwd_jYdM4HheOmjAC8lTMAsgnd2-lLkJdQFEjzI7rr2xxBRsBIsJE7DCDqMYAhrLvectIfd5bUouEDfhbD2-RQFQziSJnMHbgNalzkwnXr3HFgvoHhFrC6f3OSYSckiWTI8Z1VbqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزارت رفاه بنگاه‌دار است و بیش از ۳۷ درصد اقتصاد ملی ما در شرکت‌های زیرمجموعه وزارت رفاه رقم می‌خورد/ ۶ میلیون زن سرپرست خانوار در کشور داریم
مجید نصیرپور، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
۷ دستگاه حاکمیتی و دولتی مسئولیت سرپرستی افراد ضعیف به لحاظ مالی را دارند که یکی دولتی و مابقی حاکمیتی است.
🔹
بنیادها و ستادهای مختلفی داریم که از رییس تا نیروهای اداری‌اش هزینه مالی کشور را افزایش می‌دهند و همه آنها هم هدف‌شان رسیدگی به افراد نیازمند مالی کشور است. وزارت رفاه باید به وظیفه ذاتی‌اش رسیدگی کند، اما بنگاه دار شده است؛ وزیر رفاه نه توانایی این موضوع و نه توانایی ممانعت از مداخلات بیرونی را دارد.
🔹
فرض کنیم تمام زنان سرپرست خانوار، خانه، ماشین و حقوق خوب دارند، بقیه نیازهایشان را کجا و چگونه جبران می‌کنند؛ این یکی از مسایل حاد جامعه ایران است که هیچ کس درباره آن حرف نمی‌زند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/685231" target="_blank">📅 13:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685229">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/784e0ffb8e.mp4?token=VkO-c1TEghgd2IbEwq-u5jOAu0sx2QSA-ocfd0ObUFJCSjTQEYpdlmIDJ91IhlPST8MMUled9RyWoAuZuVjqXrYMS7PT52Vbik5YJpWbzped19-0oexg1nHCJbZgK4upZUHbop1SIF7OwI1JPmytDr05u_9VJAevxCF-4c3Sw2SvBvSge8h8vN38nl5_zLBPZNiai97-XI3LYVxKWZH8XzUBu2a6SjPhy8Ve9ev68SlkUmPbgPjqQmPGlcu5UxDpmyrI9b3M4IXRQsjKRC3c2iAZ-QgldIyZUz1pj7lEqdeoj1_LSYaGE44kRj9eg0aJUVJMgM3h0rESo4HxtQx1rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/784e0ffb8e.mp4?token=VkO-c1TEghgd2IbEwq-u5jOAu0sx2QSA-ocfd0ObUFJCSjTQEYpdlmIDJ91IhlPST8MMUled9RyWoAuZuVjqXrYMS7PT52Vbik5YJpWbzped19-0oexg1nHCJbZgK4upZUHbop1SIF7OwI1JPmytDr05u_9VJAevxCF-4c3Sw2SvBvSge8h8vN38nl5_zLBPZNiai97-XI3LYVxKWZH8XzUBu2a6SjPhy8Ve9ev68SlkUmPbgPjqQmPGlcu5UxDpmyrI9b3M4IXRQsjKRC3c2iAZ-QgldIyZUz1pj7lEqdeoj1_LSYaGE44kRj9eg0aJUVJMgM3h0rESo4HxtQx1rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت شکست سیاست فشار حداکثری آمریکا علیه ایران و بی‌نتیجه ماندن بیش از ۳ هزار تحریم برای وادار کردن ایران به تسلیم سیاسی از زبان پژوهشگر روابط بین‌الملل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/685229" target="_blank">📅 13:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685225">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5umLM7Jleac49NzSh_JY_k1GfLAfL92Hr4VWqBtxAyaNxXIbHXcnQJ_2C-OhH-ntqqtcULba1dFP_097kFdgsm7zlUpP9UvSpDKqBD4jkOl1MzPzlnyCJf96GKjkeQ-HFVJ-xlYlEBP8HgCl33dc2BStJDGejahDg7aU2AdRM258yNTexfcVe2DNLgDecc50eL3tRg8XusRLnQnkOuXf0581Qc3KdESP7JWR9hhM9K3JV7rT-5VO-5tfPxzOOQv6C72eLKqPsYE8eSmdM0iNJIlWb7k3bYYnpvJQ6bHoc-oSEPoAjSsU1Yd2cFhgoX46Ec94LyL7xT6XmCP_WBX2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشورهایی با بیشترین ذخایر نفت در جهان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/685225" target="_blank">📅 12:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685223">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9d0eca302.mp4?token=aZ7V8KX7ExKECJCWWiaoH2-lZS5chtUStERE7C-NLLE6f1gCFAjfZG47-iMLI76iBDeqd-5yorADbT37MQOPoh6oUhUhs3cc6lWb9AgKxEmM1Nmt5m1U3TEUJbyfSQWEFIoGcB23GkaENyiGRv9jJ2fSrmW3WADtGrbdeWhHSjlDa8Xh2XIe-9aj8FgxOv2FKgBW6EopD-KWHWoIeC27etJkFkzLOFvJr5OgV6bE2WJL4cNncyhgkYMPo3I3xEUX5z43-0wBZQ2UnDgHK4y17x7LLWdJdjiFhRjp6e3yQPqIxe6vME2bLRRMt6i0YPgRBA4GKf9ZyZgitmq3AqfefQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9d0eca302.mp4?token=aZ7V8KX7ExKECJCWWiaoH2-lZS5chtUStERE7C-NLLE6f1gCFAjfZG47-iMLI76iBDeqd-5yorADbT37MQOPoh6oUhUhs3cc6lWb9AgKxEmM1Nmt5m1U3TEUJbyfSQWEFIoGcB23GkaENyiGRv9jJ2fSrmW3WADtGrbdeWhHSjlDa8Xh2XIe-9aj8FgxOv2FKgBW6EopD-KWHWoIeC27etJkFkzLOFvJr5OgV6bE2WJL4cNncyhgkYMPo3I3xEUX5z43-0wBZQ2UnDgHK4y17x7LLWdJdjiFhRjp6e3yQPqIxe6vME2bLRRMt6i0YPgRBA4GKf9ZyZgitmq3AqfefQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دختر کوچولو وقتی فهمید پیک ناشنواست، عبارت متشکرم را به زبان اشاره یاد گرفت تا بتواند از او تشکر کند
🥹
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/685223" target="_blank">📅 12:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685222">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712ab5dcd9.mp4?token=Z8efdrgmJtzEj5UJpc3dZf9ojmJ3MkK9gO8NdZQT-wD_5bdtAiDwIk1j_d5Be2tR02_Atx5pOcBBpHyeoQRfbU8NKwPHbkpitxVFmpPP51NYcJTYFNDrce-nVP6f78FpLmvRKRNYb4VBbaGsqa6SOTU0axcwZGLid7qQcOz1ZVPxSJ8cDV9EHAykZp2H7SMzkyFBuJlKhnPdI5raUSDbIWZLX2KSz3H9BjdZLKxtXcyhHvD7meBC7DDdwKaxCMww3TVy0SMo9GXG3SDDWX2icGuOzPhNUJpZrC9ChcuDcUtT2MD5YuIHUidIgtTMNEA1O0Lc-sNv2YLLMEpIsVxDKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712ab5dcd9.mp4?token=Z8efdrgmJtzEj5UJpc3dZf9ojmJ3MkK9gO8NdZQT-wD_5bdtAiDwIk1j_d5Be2tR02_Atx5pOcBBpHyeoQRfbU8NKwPHbkpitxVFmpPP51NYcJTYFNDrce-nVP6f78FpLmvRKRNYb4VBbaGsqa6SOTU0axcwZGLid7qQcOz1ZVPxSJ8cDV9EHAykZp2H7SMzkyFBuJlKhnPdI5raUSDbIWZLX2KSz3H9BjdZLKxtXcyhHvD7meBC7DDdwKaxCMww3TVy0SMo9GXG3SDDWX2icGuOzPhNUJpZrC9ChcuDcUtT2MD5YuIHUidIgtTMNEA1O0Lc-sNv2YLLMEpIsVxDKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش جنجالی گاردین انگلیس از ورشکستگی نیروی دریایی آمریکا
مجری شبکه آمریکایی میداس تاچ:
🔹
جنگ فاجعه‌بار و ویرانگر دونالد ترامپ در ایران، نیروی دریایی آمریکا را ورشکسته کرده است!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/685222" target="_blank">📅 12:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685216">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a805ea2127.mp4?token=PWQJE6bguK2BLoFdJkpxwxNd0KKqCOoaCIsdNU_d35Yl7kWHgpocRX294F6zKmXhZF_EXuOk2YZyhjMv_ClFM0jXNP8kFJFazCedVGUT2aB98kUjJnh2lVe52fzgdUIvD76T5fUZq5Nsu9F7uUIiD6tFmOgSkZnhJt_Ue33JUqIyKuE86KhVz0iRJU-DNq3qkyKq1CYvk9SssTk8L2vsL-ycQ6EGHquscLKP4PE16SeRBuEDGPhLp_iPWu4V4QuTmTPjRfnOmL8begx9VNqR7JeAayI9AEAh4q36v5XvxtJtz2a_o3X5iBTiDnvJ8eWOrOGKkdZYdab6jCaw31EMXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a805ea2127.mp4?token=PWQJE6bguK2BLoFdJkpxwxNd0KKqCOoaCIsdNU_d35Yl7kWHgpocRX294F6zKmXhZF_EXuOk2YZyhjMv_ClFM0jXNP8kFJFazCedVGUT2aB98kUjJnh2lVe52fzgdUIvD76T5fUZq5Nsu9F7uUIiD6tFmOgSkZnhJt_Ue33JUqIyKuE86KhVz0iRJU-DNq3qkyKq1CYvk9SssTk8L2vsL-ycQ6EGHquscLKP4PE16SeRBuEDGPhLp_iPWu4V4QuTmTPjRfnOmL8begx9VNqR7JeAayI9AEAh4q36v5XvxtJtz2a_o3X5iBTiDnvJ8eWOrOGKkdZYdab6jCaw31EMXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جارکیک خانگی؛ ایده‌ای شیرین برای رسیدن به درآمد
🔹
در #چرخ_زندگی سراغ ایده‌هایی می‌رویم که با سرمایه اولیه قابل‌مدیریت می‌توانند به یک کسب‌وکار خانگی تبدیل شوند.
🔹
این بار نوبت به جارکیک‌های رنگارنگ و پرطرفدار رسیده؛ محصولی که با تهیه مواد اولیه، بسته‌بندی…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/685216" target="_blank">📅 12:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685215">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473021b96f.mp4?token=DfA2WvH_SJcuYewUFvunEOmlPv_1BzDraTMvnLAx9HXVqBlVmN2-d1eJbgmu65acCC0oVWMsHvLO4GWkPzlJK9BS8VRgcAxFiWlsqfXwHOaGpSWiBc1k05Mxpa0s2aUCDdPbaCOUJ3xteNoLQpAHUrKaphOdc8YQP0IL5icYdiMyxIYK9QSgVAkbDbMl5W-fdCD-ypqtMXFbiUvWuw4uYndM66YDr5_7guRDbAuTOAv_OxTlrcpHzBY56LrSGO-UmUs5-CxHKlxfm8RgwWqd8GhFoDRRC1QOK4thVrNK-MrgEx0YJM6TqJ8KJYGwvrpe_EFPrGC5jUBixV9ZDfQSvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473021b96f.mp4?token=DfA2WvH_SJcuYewUFvunEOmlPv_1BzDraTMvnLAx9HXVqBlVmN2-d1eJbgmu65acCC0oVWMsHvLO4GWkPzlJK9BS8VRgcAxFiWlsqfXwHOaGpSWiBc1k05Mxpa0s2aUCDdPbaCOUJ3xteNoLQpAHUrKaphOdc8YQP0IL5icYdiMyxIYK9QSgVAkbDbMl5W-fdCD-ypqtMXFbiUvWuw4uYndM66YDr5_7guRDbAuTOAv_OxTlrcpHzBY56LrSGO-UmUs5-CxHKlxfm8RgwWqd8GhFoDRRC1QOK4thVrNK-MrgEx0YJM6TqJ8KJYGwvrpe_EFPrGC5jUBixV9ZDfQSvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صف بنزین در روسیه به علت کمبود شدید سوخت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/685215" target="_blank">📅 12:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685214">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e30b6cbad4.mp4?token=oujqKYvVaJc6ZqQ2MOYqWSQwlaubhI4Rdd7i6sAx9dx5-eB3GXlF20oAMEfyCHES9L6z_yI79CiNutoL3gpDpIF23XQSoUfmGpxVvggY8XeSROxulbo5Dw41tb25e0TSQf8NQ0385I9UJxEC5R5ZM7s2p2eoiQ9t-9KVZpUyxcJtWglWyfu1nofLNqUGBrsLGbfb2pav9nOCjLCAz1zdQ6UYFp6e3TvyRKX6bGKA-dLbVvW0MUA2qHCCI66ZSaHNbd9JDbXzMs5J8pcHuKkIn92FgpwiUvfz_enhZlalhF_OysxjrOueBsI8rlzTJk913WrDq6vnzF9seaQrYDlGxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e30b6cbad4.mp4?token=oujqKYvVaJc6ZqQ2MOYqWSQwlaubhI4Rdd7i6sAx9dx5-eB3GXlF20oAMEfyCHES9L6z_yI79CiNutoL3gpDpIF23XQSoUfmGpxVvggY8XeSROxulbo5Dw41tb25e0TSQf8NQ0385I9UJxEC5R5ZM7s2p2eoiQ9t-9KVZpUyxcJtWglWyfu1nofLNqUGBrsLGbfb2pav9nOCjLCAz1zdQ6UYFp6e3TvyRKX6bGKA-dLbVvW0MUA2qHCCI66ZSaHNbd9JDbXzMs5J8pcHuKkIn92FgpwiUvfz_enhZlalhF_OysxjrOueBsI8rlzTJk913WrDq6vnzF9seaQrYDlGxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازگشت به آغوش وطن، بعد از ۶ ماه
🔹
سه جوان ارتشیِ ناو لاوان، پس از ۶ ماه دوری و اسارت، امروز به داراب بازگشتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/685214" target="_blank">📅 12:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685213">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fc5dc2c0f.mp4?token=vF8whK0N09sRJsOiaIqTwuT45aarszuOsRcF0eLuXEruOlecsXSWETAARpd6jneNAteekMWwfVXtKdS8bmsdWeR9A7zvXRN2YbPFxKmRJPWN4lDTi1orXGR9movgXtiA2iRYj3TeAMosYdzWoJoNILtMh8CFIWTdY87Py0QdYoJQeSUF8y0lz6lcicZheasvXkGuMxr-6jyQOAR91NrC3M-R7tuxqRHaXZfC9rkTh53geCnQ9cs9V8KC7iWOlrg3pbanGZbo0hqIeD6Rx3QINwW4aMk8eBbTLu2aDGAPxK6D_2Q16rYnSZPzNHmdlnHbezf1jkDHk8_6TQBV-0MsVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fc5dc2c0f.mp4?token=vF8whK0N09sRJsOiaIqTwuT45aarszuOsRcF0eLuXEruOlecsXSWETAARpd6jneNAteekMWwfVXtKdS8bmsdWeR9A7zvXRN2YbPFxKmRJPWN4lDTi1orXGR9movgXtiA2iRYj3TeAMosYdzWoJoNILtMh8CFIWTdY87Py0QdYoJQeSUF8y0lz6lcicZheasvXkGuMxr-6jyQOAR91NrC3M-R7tuxqRHaXZfC9rkTh53geCnQ9cs9V8KC7iWOlrg3pbanGZbo0hqIeD6Rx3QINwW4aMk8eBbTLu2aDGAPxK6D_2Q16rYnSZPzNHmdlnHbezf1jkDHk8_6TQBV-0MsVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی حتی SIUUU رونالدو هم منتظر VAR می‌ماند!
🔹
رونالدو در دیدار دیشب النصر مقابل التعاون، پس از گلزنی بلافاصله خوشحالی نکرد و منتظر ماند تا VAR گل را تأیید کند و بعد از قطعی شدن گل، ستاره پرتغالی برگشت و خوشحالی معروف SIUUU را انجام داد. این گل، گل پیروزی النصر بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/685213" target="_blank">📅 11:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685212">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2faa7b5d8.mp4?token=viL_69MVhrBKyUP0AMSoIq60Jyf_FqlZtlsPAgVVcsAVkuwc5oUiJtr8n8I10Ejbd21dvLJavr0Mv2Pig1t9EuscjB2tcA7xqkfNbGvyQ-X6WaHbETSB3gu3uMkxgiIEf60tLK4_Nfj48jvttoK--z1fVGPF_ak0tqIV3142SKpMxTiqfSAlWsNAz-wVSXZprDjfB47RDImnbT0QR-26o6x_RDzfukXS2wOUQlZypgpOVumNVuNAgozvihp5OSjMu6xJphRDEzaP-_aSqpNno4JO5mxpPYpOJz6Qvpv5bDTe2xaknxQ4RaVyPWP8-EIm6_34VVsM11nnaQW7LtapBWBJLsgPH5YRtMmAApyJXIXNJag91cPyTM7jso13AY_luNkZpTsMr23Lb-zCxqi-YozWP6v51FuPDmz1rLejCmn6gyRoLAitIxhxFbHIVx8FAoTAKtqDcCLHoS4cWxRBj-0Yos_nyqHA3k_n3fUt0RatU-YLA-gNsjYQCQ0xG1pLXtzOIcOriuxg_vykMzGti66hoaO5Ope8zRFDTN89ZQ_IzFUlxyH9pvN0bt1FxJYtSDIF-Ve-Cwyq2kr2udRI3g0jc3m_x_1WwBn1iDHrWMT__bXz5yC4a-yMBFQUAqF8Kpwsc7zmLmfFKZl9f8bDKcgCN9LcHPQ9lLpOvY5M7CE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2faa7b5d8.mp4?token=viL_69MVhrBKyUP0AMSoIq60Jyf_FqlZtlsPAgVVcsAVkuwc5oUiJtr8n8I10Ejbd21dvLJavr0Mv2Pig1t9EuscjB2tcA7xqkfNbGvyQ-X6WaHbETSB3gu3uMkxgiIEf60tLK4_Nfj48jvttoK--z1fVGPF_ak0tqIV3142SKpMxTiqfSAlWsNAz-wVSXZprDjfB47RDImnbT0QR-26o6x_RDzfukXS2wOUQlZypgpOVumNVuNAgozvihp5OSjMu6xJphRDEzaP-_aSqpNno4JO5mxpPYpOJz6Qvpv5bDTe2xaknxQ4RaVyPWP8-EIm6_34VVsM11nnaQW7LtapBWBJLsgPH5YRtMmAApyJXIXNJag91cPyTM7jso13AY_luNkZpTsMr23Lb-zCxqi-YozWP6v51FuPDmz1rLejCmn6gyRoLAitIxhxFbHIVx8FAoTAKtqDcCLHoS4cWxRBj-0Yos_nyqHA3k_n3fUt0RatU-YLA-gNsjYQCQ0xG1pLXtzOIcOriuxg_vykMzGti66hoaO5Ope8zRFDTN89ZQ_IzFUlxyH9pvN0bt1FxJYtSDIF-Ve-Cwyq2kr2udRI3g0jc3m_x_1WwBn1iDHrWMT__bXz5yC4a-yMBFQUAqF8Kpwsc7zmLmfFKZl9f8bDKcgCN9LcHPQ9lLpOvY5M7CE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاهده مجدد هلیا و توله‌هایش در زیستگاه یوزپلنگ‌های خراسان شمالی
#اخبار_خراسان_شمالی
در فضای مجازی
👇
@akhbarkhorasanshomali</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/685212" target="_blank">📅 11:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685210">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UA_DK3dRRJcQierigVMebLyGL1Zgf07G9i4btA3c-tcahtlnTDWVy_6MPCvl3mkZIMwyAo-6FDOhtSWDjXEc2yqlP_RtuZgTB67U_Jl5M-fMDmK78eNMoVhX2IrXDOHj_WX0UNch89tIZmNJblA7PV3pWA0rUVFknfnSUWK4H-UYaQ3RpDuq0d-DmD9v5mWs7qfL_1Za7TG45pZwoNaH6Cn71cAd6lzmR-mgOcuy0Z6Q7_FCokrDvs7kDQ47YjWZZnxLQaQU7spGrG8d_wulQAWYiOr1xRjzn9WQLvK_ePzyi3aiP6S7Iyp28J54Kmuul3VMDD-zRQjrPVzBZLhdNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تنها کوه خوراکی دنیا در جزیره رنگین کمان هرمز
🔹
این خوراکی نوعی خاک به نام گِلَک است که از دل کوه‌های سرخ استخراج و به عنوان ادویه در غذا بکار می‌رود.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/685210" target="_blank">📅 11:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685201">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Idb4jGIIQ4tIFk42b1IktkwStlXWMUpXE9hf8wp_Hk5_TAX3K_vcowvYXGEpxTh0qmHZe_cDKIjHM7CM3BB2FOqOEFxzVzIe9-a3NF1QbmYolfdBphlAJnTcKZ_W5Qm6CDmz6QxUYVj2-bElLyvv6wUlpZmpLUPSN4agZ9lqhvJrcd4usI6FSZeAKTZ2q3ViDwO0omLUCN8WPSMAHWiH5LRt296906TLMpKuM73T-D2QIwViiWC3EXCGD9agPDAKSMG3IdRcDqRMhf4pq4EYYfhx7RWKE3QPjaEVZQB8pDisJx2uwKv6_e2XV8PhKFTVDC7145LFMEMo9BklQKU8qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BlcJ8Rg9dL8go6jajUw3UszMK9_5vU41aaDKmzYFnWCr1wXqXfpmpn58DiOvsp3afACcznCjD8DYGr-Ieqz78C2Ov5aWRVdcHU-opuKjYuQJjGeKcwhO2ifUbuOEfnjKleFRKOKeAFWDmfBcL_bcgXmYAuQDJAvMguowITEKGtXTwA-m4gWnBCE8f0la4OnJaMh14pcORL7jyno1wdLr3E0H8DYeF81i7NxE_rsxPE9Ak97nnpQ8jpWEF1RRiHXQ-7XlBB-XPyQILRYgIzafbTliiLq9fkvzbq_1YygNl3vAWf-YLvuJLIBZxAr5_TObkOReWU5E_SQGbF4a15e0bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tixEOj-2giFTEfgkyB8F9b9P9BKEMVJ5hFGf9PVTe8LBUYsNK1-zH0XJbfcz_uCEaAkDWTUkipIRORu2RZrGx2jYPTJI836CoAIOaqsMGL-Yz1z5mp6jH1dLIt5rEaKE60dQeMGlQJJkciiITaIGy-J9ZxuRODTsRkwsvi4V0hZhtjvqOJ2cgCSTJN6vat6J9AWgOtK9XDxabXaDOHCRw72OvGpqgnu2361nDyZmzJKQi1-xKpDv-QDtnGr-uR8JapO-C6R1otTs92xpYu_UArLBPVWn-7jI2o-7Hw6hvEHzdC2hLsADI7_p1RJ6b12zCHmW0oMHMrq5ZsJmO-Uw1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b3-pnuQt13BUA8qlJuL-jCbsx2VyuOWN5VYY8OaFqueUkT-BaxBaAS-EMJ4CEl5QfbtxC6d8ZZNvn52CeiDVP-qPHsOD39igAZm_ypa_laPRaulIqVR9YSIS-QZdq7YU28Qx_ksCRF1ioXhYRYVRNABl-bgeOcfZaiBGHfEQDKhn3tJPOKtYYBhEYA4Xcd7glEWi6ZMmP2n_tnwr15_sFMozoSyzs5zZS2JG7lm3IAXKmfQktp-etiQehrlzyBHmLb9TuiYnKSiu9baWWCLUjlxGorBZ69tUA1Bpn8kZk7bk8gEncLCfaJCW1dgfVMFStRDozGleDEDkDDIOJUIKOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mldfZ7991HvZg5M8WjIYOHb2eE_cJX5XTENsNjACYBaXSGfyVh0Hx_9JwGzXeKYdvWhi-M86loVBav-ghEdo5nw8Cq2dch6LUnlPysEup6uOKnQsoBvlzLXbA6Geujii_BYQ-O-56AOKBq9joJfh6_PxADMlKutlqxYMtO53uFiLhP5SZFBx2xl3-TbipOIQptZ3pVXataW6SK9M1POW5UgVjPSGeIgs4rn3oTJof5TJcSAWRUQWdbyLDB9GxAX32WFHzmoVrh4u41hxIZbTgFzfsL6A0yht3HHOAMDgC4SYAx2LC7Z8QqhAzPaFn_Sw2CxcwlKZsW7GRoY4tzGaEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BbrceH8L4eKgmbxoQPGuMo-dIhu3C8EsxOgoh7wtL628ZXj6pGOaR9LPQrVZ1bsok_J0INwVzpbHquSi4h32vQCb4JhXDUKXJ058tpxzSHTY8UcuG4PLpFSJ8ki0qQ4_r15LN7eZkKwY4IkG2stL8s74wkLrfmUia9LtSqHjSD5YGA6mmhN08ZQGW_WuG6dsSP7TDDXzOd6IznEPkcT7kHBJGdY9TlGIAyzxfkuklIxbn1QBhpQoMGfAWCF81Gf9gwqZPyrk3xpCH0aSageV6YsoFwk17pcfXJ_KaP_mJdVLHKJIwVZU0Wzx8y8jj-wn39EHRw9OS5_gCa3424T1ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s5_iw0QIIZNo-PJjtbJ9fGh1ERVlecb3xbqGFEEh9wdQmWbtHayFkOU4f8uzD9oVMElk-uMFZ5G7EqS4rtweYPAAlDYiJSTp5qfGjBV0zK7n-Iy2ZmrH9tt4bq76653jFb-By_UJ2Pg6-PqDg2tpMsrU8iLuGKOV4zto8czM-xD4IEZ3xwySeCU_XN11Jzhfv3CLm98GbK3-wlsVMVY2iIxgXYi0Hb-a6YURWYto8I3Gyx6uQUOHNSiK_Ibh4K3XGxYXr6xG4U0yscbCe_-Nf7zzxW8PJ3fXg0S-oNQ9TCzQQDdBocjPoX4UtYK76DFqibS4xdQVpApHGM9NsAk4dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EQ8ricvzCkkdBrWdmcgwXvcbkL7p6Zz9j7FZdwQ-WmoM7jPHgFjzQE7egYkmkfAVEHsVO7qslRBEFh8jJXO69_27VRAj3sJ3cOG34le2PP9YL_czyqyPBySaAz-esR97MQ-fgf0phjDsYrsSpZZ26Gn3RzOqz1Y1EXfW8jF5LdcGC7yR9XkVB3DBfavVuoI-gFq5TA4IM4uvOLjUxzUok66Cg3s3Nb_dleoK9HgF_keSTJxOVaYR1QBWrPoNRGbD6VzwYiWF7nPPqVF0W0Abf8msGDTrVmelSx_UYgK_1kNgGKB_5S5yMHMKSRm84rtkH85K2dVXHBEidC2T4CAAKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CAxmha9Yxm9kUCcedzlgRS9J8zkc3-tDHmVkqbkVdoV53Jhj5nqMgUuh-M85_Ub6sYd5WtSeaaeywb2bcTiG_MJDr_qKhbjRrzqCF1Teov3TxjMBPQSKs6MJHuN8hZPa-DlSaUP4iveh14CD426Qbw1CJUCCFRNKqXbwtO_Q3Gqh4ia6V4HRJdM_arklTROuXFyABrTvjqQ8LQNfYZ-7zv3X7zMTT5_w3q9A9N-hnI7227ZDmxhV5IHdzi9S5n4MfitXOqfwvvllnt-3y4ezqgszZuvrWRD-wBChTmhTWAKa5J-92prsEfz5YQNRo9fmkS8xKKmvCyHIITPU1w4mVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری ؛ درد دارو
🔹
چالش‌های تأمین دارو؛ روایت شما از سختیِ دسترسی به داروهای ضروری.
🔸
پیام های صوتی خود را به آیدی زیر ارسال کنید
👇
#درد_دارو
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/685201" target="_blank">📅 11:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685199">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d282c9187.mp4?token=WrNEX-3KlDjacCtyMjsi6Z2batSrOq4RkPrveJywYlDxtzS8HTL_lOxRVYS-yZohSgZYraFSs0pZpvZEsUfQXoax78qFfNMGvEDwpSKAB4FbRHsaS_7VXd-UeKNV-f0pZV3pGLbYxsviPvxjI1j6Vc9WZWy2TY4KnP__l7k4I6J8Y8iSkrxgoNnzglTwWYOydA9ztgcou60uLHMtPFHoTAs0ZXS9y0nHqY9bLwzz0XnRPw_dOtyOXHlkuIem4kOufUP2_DyO3MHJq3txSZ_1KjBxLXQgTkeGizBrEdgnLAm5w3w8AS2EmUO8w-EavcuEQ9ivFdLMy6TYlCP5ed8Myw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d282c9187.mp4?token=WrNEX-3KlDjacCtyMjsi6Z2batSrOq4RkPrveJywYlDxtzS8HTL_lOxRVYS-yZohSgZYraFSs0pZpvZEsUfQXoax78qFfNMGvEDwpSKAB4FbRHsaS_7VXd-UeKNV-f0pZV3pGLbYxsviPvxjI1j6Vc9WZWy2TY4KnP__l7k4I6J8Y8iSkrxgoNnzglTwWYOydA9ztgcou60uLHMtPFHoTAs0ZXS9y0nHqY9bLwzz0XnRPw_dOtyOXHlkuIem4kOufUP2_DyO3MHJq3txSZ_1KjBxLXQgTkeGizBrEdgnLAm5w3w8AS2EmUO8w-EavcuEQ9ivFdLMy6TYlCP5ed8Myw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قدیمی‌ترین پرچم‌های ملی جهان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/685199" target="_blank">📅 11:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685195">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۸۳ درصد از اعتبارات فرهنگی کشور به  دستگاه‌هایی تعلق داشت که به هیچکس پاسخگو نبودند
مجید نصیرپور، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
واقعیتی که اتفاق افتاده این است که جوانان نخبه از کشور مهاجرت می‌کنند. دختر من که فارغ‌التحصیل دانشگاه شریف است، تقریبا تمام هم دوره‌ای‌هایش رفته‌اند.
🔹
شاید بیش از ۲۷ دستگاه فرهنگی داریم که چون تعدد دارد لذا موضوعات روی زمین می‌ماند و همه مبادرت به تولید آمارهای کاغذی می‌کنند.
🔹
نزدیک به ۱۷ درصد اعتبارات فرهنگی کشور مربوط به وزارت ارشاد بود و مابقی به دستگاه‌هایی تعلق داشت که به هیچکس پاسخگو نیستند.
🔹
از صدا و سیما و نهادهای فیلم‌سازی کشور بپرسیم در چهل سال گذشته چند فیلم در حوزه اسطوره‌های ملی و تاریخ ملی ما ساختید؟
🔹
اخباری شنیدم که رهبر خودشان ازقبل یک شبکه اجتماعی  داشتند و روی موضوعات فرهنگی قصد تمرکز گرایی دارند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/685195" target="_blank">📅 11:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685194">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65ad30894b.mp4?token=cec718tr6kic8mz5iYylJ_8y8tP5QiEiNjsZ5140ooukRZWNAkXAOvtmkXEqwftLP8Wy2ypQk8J0zLMQdXREtgiL7nLL9f8SVI5V9vZ48muqivIExqZE3fHDdoyoIOTvmL2D-UYUhirJcXJYxqxl5EoWERxqS3q_TtCgy5v4Fu6-alj-ecrcvKKmhr54pEB63ngxA9uwslOxbTV0pkgeI1TKYIqrdYz_O6vVxIHCdjd0J6-4xlZk8d31udM1S2O7DpnCT_MGIn8M08MM7KF8Vio5wVvBIqQTqRmcd4YoEIYiRvvddasH5KFeu4HEVOUhHH0YMXtDQahMYs20lPhsdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65ad30894b.mp4?token=cec718tr6kic8mz5iYylJ_8y8tP5QiEiNjsZ5140ooukRZWNAkXAOvtmkXEqwftLP8Wy2ypQk8J0zLMQdXREtgiL7nLL9f8SVI5V9vZ48muqivIExqZE3fHDdoyoIOTvmL2D-UYUhirJcXJYxqxl5EoWERxqS3q_TtCgy5v4Fu6-alj-ecrcvKKmhr54pEB63ngxA9uwslOxbTV0pkgeI1TKYIqrdYz_O6vVxIHCdjd0J6-4xlZk8d31udM1S2O7DpnCT_MGIn8M08MM7KF8Vio5wVvBIqQTqRmcd4YoEIYiRvvddasH5KFeu4HEVOUhHH0YMXtDQahMYs20lPhsdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفند بسیار راحت و کاربردی وقتی به شیر آب دسترسی ندارید!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/685194" target="_blank">📅 10:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685193">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرمانده کل ارتش: مقتدرانه در برابر دشمنان ایستاده‌ایم.
🔹
بانک مرکزی: ۲۰ میلیون دلار اسکناس از بستهٔ ۵۰۰ میلیون دلاری تزریق شده به شبکه بانکی، توسط متقاضیان خریداری شده است.
🔹
وزیر دارایی آلمان: به جنگ علیه ایران پایان دهید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/685193" target="_blank">📅 10:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685192">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
آیا رهبر شهید، خبرگان رهبری را از بررسی نام آیت‌الله مجتبی خامنه‌ای نهی کرده بود؟
سعید صلح میرزایی، عضو مجلس خبرگان:
🔹
دشمن زودتر از همه ما خطر ایشان را برای جبهه استکبار دیده  و حدودا از سال ۸۴ بود که تهمت‌هایشان به آیت‌الله حاج آقا مجتبی آغاز شد. خب رهبر انقلاب فرزندان دیگری هم داشتند و اتفاقاً ایشان فرزند دومِ امام شهید هستند و می‌شد این فضا برای بقیه فرزندان هم پدید آید.
🔹
این سخنی که تقریباً اواخر سال ۱۴۰۲ مطرح شد که امام شهید نهی کردند از این که فرزندانشان در کمیته تعیین مصداق رهبری در خبرگان مورد بررسی قرار بگیرند. در پی این حرف و حدیث ها از رهبر شهید در این زمینه سوال شد و ایشان آن جا انکار کردند که چنین نکته‌ای را گفته باشند. منطقی و عقلانی هم نیست؛ چون در یک برهه زمانی ممکن است جامعه به شخصیتی نیاز پیدا کند که اتفاقا آن شخصیت فرزند یک مسئول باشد لذا هیچ دلیل شرعی و عقلی وجود ندارد که فرزند یک مسئول نتواند مسئولیت بگیرد.
🔹
در واقع نام ایشان هم جزو کسانی بود که در کمیته مورد بررسی قرار گرفت و اتفاقاً جزو نفرات برتر آن مجموعه چند ده‌نفری شد./ باشگاه خبرنگاران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/685192" target="_blank">📅 10:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685190">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oW5LYp0N6YOCGfWFfDR_Io182yBcdKGFLBTKyPaaKxfMMwgmuv6lGMU0wYuokCxW0y0XdCwNCqxhTAVSwsltLTNjUCcpBaf_pQaAIV1wJEfKmxMWb81aTuUNeJODbgRoIPBGKiyowEKLHiQUSdUZ08sPapRKr-V95LjyXCyStkWZgS7D3wwKs-PXpZakSrJuJvr_FjFFNtCbL4OPWrg3lLoo-pjjr--7Up5EFfDEdAXoRUNxzUSnIZ6hbbsmolxUOXzfah8ckCZFrmEdedDr5rQ-2N1OMAIH_2Kt5rIwX9Tqfv73LO4gA2DUpnn83el2yoi_vO-dBx6-Axn2cQXJyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره
02191551808
در ارتباط باشید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/685190" target="_blank">📅 10:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685189">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKzPhhLytlgUWG-_nO4xafJ97DrVbbmkfub29UR4a7KgcQAhicx5WCX_6CVmLaX3sPbmOsJ_aOcxB-B2J3h-ON-lErzzsAyDy3wp7cQYQBCU869poKOXb5YMF4OBha55-TsB1os6g2phe7bVHT1uwvPMQCts19ifX04V9cFEeEOC3Y5RKtstq65r54QPjqiclRPWy8GKyR4kRRQgkk0jFaBudZZH9zXKPiIs78xqjQBDTaHAJ_nK0ftRrgXV7naBHg4I01JBEKhrGIbDuEmzigwhVI9sKJAq2gtEeNqSdSd1sEy0-jiWykpt5kkOW5XJiRLLTwducCNdfrg7Edbp0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمان‌بندی تکمیلی انتخاب واحد نیم‌سال اول دانشگاه آزاد اعلام شد
🔹
بر این اساس، انتخاب واحد دانشجویان دانشگاه آزاد اسلامی در نیمسال اول از ۱۰ شهریور آغاز شده و تا ۱۹ شهریور ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/685189" target="_blank">📅 10:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685188">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c85c696e93.mp4?token=YjiJHLgznGU4UiW39Do24ppmOFJp2bf7_iSqpJEi4OUNkxrDQcJXqcAFI_s_KNHAXV1ky2TzMYYsTi3uU2M6ZBa0QJBbhvXX3V1YQZipU9F7PawBBMYRmu_nmQMChGxiFAhaG2z68t0Wxjt9DwW79S4Ul-atAdx8f9OO1DBvP0aZZHzGrZQkU1JERT2CmQOjjzXySBqCET9xJzabDyKwB8-E37dIvpcr6hGMtQzqKLgpOiyvVhRkJxwecswX7hP7zVSdToOzZVDjqYAiDkzV3ixm_tm3GWMDWT8M17kcUOkqPqBkZGsm7LgZ4NTlu_MKzNmEdPz0YL-AzIMm-qQPzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c85c696e93.mp4?token=YjiJHLgznGU4UiW39Do24ppmOFJp2bf7_iSqpJEi4OUNkxrDQcJXqcAFI_s_KNHAXV1ky2TzMYYsTi3uU2M6ZBa0QJBbhvXX3V1YQZipU9F7PawBBMYRmu_nmQMChGxiFAhaG2z68t0Wxjt9DwW79S4Ul-atAdx8f9OO1DBvP0aZZHzGrZQkU1JERT2CmQOjjzXySBqCET9xJzabDyKwB8-E37dIvpcr6hGMtQzqKLgpOiyvVhRkJxwecswX7hP7zVSdToOzZVDjqYAiDkzV3ixm_tm3GWMDWT8M17kcUOkqPqBkZGsm7LgZ4NTlu_MKzNmEdPz0YL-AzIMm-qQPzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاهکارهای هنری جان گرفتند؛ هوش مصنوعی نقاشی‌های مشهور را واقعی کرد
🎨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/685188" target="_blank">📅 10:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685187">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bff5bbd5d.mp4?token=rpDSeg-FiO0aWM_n-Z959AsAgp7PXV2cDPR-24VO8CRoz1zMBazLCUcnCWhNECt63quiE__3Dz-kKetTYlO6qO8be-qqq84p0bMVjxmSzoGIah53a31DucVGwnvewVJEZUlRdV2Bdn-2FOLpk9CFmX1dVSJb_D7Wv75QPemALQW5rpmtaVDQKeUPwYU3GExL6Bqd_34iyTZBBhbDzMy9B2Zmf8rY9KAxS_w8kLD0ypzBcNVn1xIDKoNoNMfUbyR0aOr_28D-yr1cQHBZqwJPja0LnUhkFdNa83AtK_A2Ti9hTdn6cLclmEw5Q0NRYJt5eGn84gYcYsFg-cFDEIIMPzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bff5bbd5d.mp4?token=rpDSeg-FiO0aWM_n-Z959AsAgp7PXV2cDPR-24VO8CRoz1zMBazLCUcnCWhNECt63quiE__3Dz-kKetTYlO6qO8be-qqq84p0bMVjxmSzoGIah53a31DucVGwnvewVJEZUlRdV2Bdn-2FOLpk9CFmX1dVSJb_D7Wv75QPemALQW5rpmtaVDQKeUPwYU3GExL6Bqd_34iyTZBBhbDzMy9B2Zmf8rY9KAxS_w8kLD0ypzBcNVn1xIDKoNoNMfUbyR0aOr_28D-yr1cQHBZqwJPja0LnUhkFdNa83AtK_A2Ti9hTdn6cLclmEw5Q0NRYJt5eGn84gYcYsFg-cFDEIIMPzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیگه تن ماهی رو ساده نخور، با این دستور می‌تونی یه پلو تن خوشمزه و آسون درست کنی  مواد لازم:
🔹
تن ماهی
🔹
پیاز
🔹
سیر
🔹
زردچوبه و فلفل سیاه
🔹
فلفل دلمه ای
🔹
رب
🔹
شوید تازه
🔹
سیب زمینی  #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/685187" target="_blank">📅 10:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685186">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سپاه اصفهان: احتمال شنیدن صدای انفجار در جنوب اصفهان تا ساعت ۱۴ امروز
🔹
دانشگاه تهران: مهلت دفاع از پایان‌نامه یا رساله، بدون نیاز به دریافت مجوز جدید تا پایان مهرماه ۱۴۰۵ تمدید شد
🔹
جانشین فرمانده انتظامی قم: کشف ۵۰ تن تخم مرغ احتکار شده در قم
🔹
روزنامه معاریو: نتانیاهو در قبال لبنان با احتیاط رفتار می‌کند تا ترامپ را خشمگین نکند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/685186" target="_blank">📅 10:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685185">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b0344ce1.mp4?token=ol3w1v8JvZbjY0B3TcvJ3ULk7yecBkTH2xrSRS2FggM2GiWyIldfh7Nx9NJgi2gRXabocpghEkMsFlM9Bf9tD1sL0Y78iI9Wh-RskV0veZ_qwMmGAWy2DpdsVCnUpVLu2MpJe3-1Gqz6Wuuy5nTfqw-CzgiQ85DtYxbacrv2ifFsHWYd85sOwdTsKDXsOdv_cvokOyhEpBhDriEiDTXCql9BMAxJKujZ3MmxVfZOu5KN3OM6BY-8ViFlNKxztsDc00MVkUsxTs-Qb7wRkT9a2cJ41A4oYPdwaYSZ-W769UJp7uLKLxQF5jmqBEIktLokjOKcfEeeQ2LdqF_pdyzU0YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b0344ce1.mp4?token=ol3w1v8JvZbjY0B3TcvJ3ULk7yecBkTH2xrSRS2FggM2GiWyIldfh7Nx9NJgi2gRXabocpghEkMsFlM9Bf9tD1sL0Y78iI9Wh-RskV0veZ_qwMmGAWy2DpdsVCnUpVLu2MpJe3-1Gqz6Wuuy5nTfqw-CzgiQ85DtYxbacrv2ifFsHWYd85sOwdTsKDXsOdv_cvokOyhEpBhDriEiDTXCql9BMAxJKujZ3MmxVfZOu5KN3OM6BY-8ViFlNKxztsDc00MVkUsxTs-Qb7wRkT9a2cJ41A4oYPdwaYSZ-W769UJp7uLKLxQF5jmqBEIktLokjOKcfEeeQ2LdqF_pdyzU0YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
یک آگهی؛ یک فرصت چند میلیاردی!
با مزایده مناقصه آگهی‌های مرتبط با حوزه فعالیتت رو مستقیم دریافت کن و هیچ فرصتی رو از دست نده
🎯
https://B2n.ir/mozayedehh</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/685185" target="_blank">📅 10:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685183">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8096f43c1.mp4?token=DGWjdlYDtOMpOtR8LhUxCYQrtpPU53yhhhzb3PgK5ingZgeNNzpIEt440E_kt9X7rk65jA4C34M5JwMSJQqJu_guxHAY4xbH4InZGddXffxu9cWmbf23xzCDrBbm7uxr88nM1zLsOXkhZ_vuO7-v9p2C8pDU0VazEWPyEynTywGg_m_5ZLiZNJX6sc6SOCpRwf6HG_gpDGyWFByXWuKmjkA6PWOew5akMiOdfcw1Li7gStJN-VliX7vYf9PDBAI66pMQ8QoPaU4JTLsuGO-jLZzDmbVW30UNO4lunf28HngdUR3y92rRMPjhHpWVi7cRf8OrgtMjUtdYBEXZqOCaOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8096f43c1.mp4?token=DGWjdlYDtOMpOtR8LhUxCYQrtpPU53yhhhzb3PgK5ingZgeNNzpIEt440E_kt9X7rk65jA4C34M5JwMSJQqJu_guxHAY4xbH4InZGddXffxu9cWmbf23xzCDrBbm7uxr88nM1zLsOXkhZ_vuO7-v9p2C8pDU0VazEWPyEynTywGg_m_5ZLiZNJX6sc6SOCpRwf6HG_gpDGyWFByXWuKmjkA6PWOew5akMiOdfcw1Li7gStJN-VliX7vYf9PDBAI66pMQ8QoPaU4JTLsuGO-jLZzDmbVW30UNO4lunf28HngdUR3y92rRMPjhHpWVi7cRf8OrgtMjUtdYBEXZqOCaOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پنج تمرین در منزل برای عضلات پشت فقط با وزن بدن و یک حوله  #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/685183" target="_blank">📅 09:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685175">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NCzxMo7dgEg14uuum7fRQRsWrPQS2_hbGX2BR79eLXSIS2f2ouh_ueiuqlhRCOaie0LaO5dzQ8FwlZmh5ecGPdBNnjO2DWXGfTcyw3KxtSoz_Q4GP6ocrE1tgGVhYm23wv3-T53Ov92hOI5Q1WrvCsiE2OeXO0zz1hr0kyC1Q4LMa-j65KbSKwbDNbkIkTzTC0s0q0xVt4mYl9vK6LdZFC5pWfY0inhJzSuo6kG7YLLOd3uDd4AY7nPzBBRVToagZAAOionLjsUFut2RLiOFPRfTeY62KBmZVDtM35lFlHDHYkFYcPHgWHM271f3G8MrtcL9ULtOFrQYPkJoA9aW2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kykL-n0X0iAjbvN4S884dF8nwXXYSMfn0PjnmQRm7jBNstG8dwKCo_ax2zWNdznMFnTaaQ12u1T2rBFmv2VJM-XiAHCws168E2-s6Y9YBrNLWRWRaTR7YKeV0jfdiKfuRNEkHnPqpqeW8s3kGW0oFMl0UyQROOzBBStIGKSR8yh224bYExK8WsGzpscxmAOe4r7KezSUxNW52V83bHDhUL3pFxUQ07dexKnGQVjaGt9xNxcwsP3e7YbUTWdpZM_K6OFH0R4ipp4dfhw--VLbFIuk_oMVMQDBF4eECBeT6SoPbouxXs9xyQBNyWohSn0Ut6QJalf1Xpu_6ZIqUi7omg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gu7nrejrpjmP3nNIoIEVdOFI3Uv2UelNep7F88Lz4OhIdOE5ZuZpCbNeMKbLTuaeCiKlGlHayiztlDgZ-BqP_G0ZEInBtwupwvlsUKokwQ2w2enNXUCOqavgJ4DfhUNEjRjXA2TTYkJIYTUG4oH-V3D_dykxr3hc9AQN3Nuor8E3rk8rvAqa2QxFbzcp7mSWq34YHHS79pcic_TpkIlrsOTdPOYIgSWMjxrSD8znHaZOpp9Ngu6TxydcP5E9XwKCn-SKrDbhFEt4uTY_AwnnDYHY7X6FegorvMsccvZIng1ZIJCdtRn-zD4126fD2T-MK54nJQeilAr4STUUlSW2vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qepG72zdcRZjBuf_zIDRxoiDTs7cwxzOL4IGhrXyAFBiHwIELdTfjgUuqaoap1IUdits2GcTlSMOkgM430rsU0cRU-xyg2QGOh8FLXiGVokUq9LuCp8WEV58mFnEIACEuNwiYOPcd4R7f7MHD4r0I4qHHDEqfH5LXR1ejSY-eJThLkZucms1wTTAHKpU9_31n-AH1yXkZzwf-RusMEcB608PdZUgbiWNj6twFQUwvA4KMqV91S8yCQU3Oa0wbg8UvzSzAmK42mch2Zpt3YXUhsNubmafslDuQ0mQtevtsfpqwbwVhixDvA7UKBHGt5nIg6f5eh7VcgMB8lzFdotDeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/apJ9ZwB1IixxADw1NXv8P_uRwQm7AtyUS2FqBShxSR9bIsSKa__5dB7Ryfa90v6CQ1T1u_hmOXKfdEVZNR_kPVxLBWubfrkQBVacJsArlltdDy4RjaPARvJCo6BfbnBnEmKkPkp1GZax1mDF8s1XciGHxivPCnmW04kjDm9MjlhAcJNWX66MTBSrOl9ZHEXmwTGDaSJhA-1cyFPr1Nn4ERCmb6YRH4PgNOS6i91n6-nY9e1pvx4bEOSCMFj9C9WX5Sg1zblWWsIVlvBvYIbL0dLGua4l-ImDfShGT7mOjwu7HZ_DPJqUrV_rUXPnvPFRLXQFRY0KYhFDTLJcMj-pxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JfDt7Q6-Hzt_o8flXaSZihqVQI_wvQdOjSSW9kP0sf3Vff9_3Am_DN06_-PJaLRlcuFpWEUrpqq2H2FS20w7c2lKf3_QGwXZMAX3vRh-lxxqbopM8dMYor3x6lcXuUG_rfKTXdhoHzAA4gyzegkZH6Tyu4sfClRjiLobHqoeynNkpmlpICKkReM6okEaZdnF2ecUrQX-LG1AT_iJmuqDenMTXxwdSY3y1kgsYRou_1tnNwOFc5NJVGIAm0iApac4-TtuPBVQIUJ4tWzthp4EosXELh2CqgfDmPHMD-LF2spt_6Hqr6gQK9MLutESNU_udIDEj-JsxYO7vT9xJmBWoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قبل از خواب چی بنوشیم؟
۶ نوشیدنی ساده برای شبی آرام‌تر و صبحی سبک‌تر
🍵
✨
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/685175" target="_blank">📅 09:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685172">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d30464c760.mp4?token=c5EqV1M3QYWD8xFitb5or-fJQVz0Pck1kXBsPgLGwTODLEEN-u2mkps2AMmHEUfQon0h_WEHdzfkk5lJ5hO1Jot73NIfHSgoiM_Zxp40NTDjE0jqi6FNdpiKs7r65yVber1STo_emeaM-wwRHU9K3ml6VpsDM7st4RXP9rgbE3wHFwZyF3FDpziCdS1m6N2xAyggoaKGjvXd27YC-gSjbwiC-FdWprkfCIuOFqYwlGq3dummUneEBRs2IqGx77GDOuIbk3FVADS6wUMVfYSNqgvrM6v3u_dNLTLtDidU1sUZzCyU-Knx9COLgGtnLWd7_NCnlsqP224CdLeupY6Eww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d30464c760.mp4?token=c5EqV1M3QYWD8xFitb5or-fJQVz0Pck1kXBsPgLGwTODLEEN-u2mkps2AMmHEUfQon0h_WEHdzfkk5lJ5hO1Jot73NIfHSgoiM_Zxp40NTDjE0jqi6FNdpiKs7r65yVber1STo_emeaM-wwRHU9K3ml6VpsDM7st4RXP9rgbE3wHFwZyF3FDpziCdS1m6N2xAyggoaKGjvXd27YC-gSjbwiC-FdWprkfCIuOFqYwlGq3dummUneEBRs2IqGx77GDOuIbk3FVADS6wUMVfYSNqgvrM6v3u_dNLTLtDidU1sUZzCyU-Knx9COLgGtnLWd7_NCnlsqP224CdLeupY6Eww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نظام سیاسی ما مبتنی بر ایدئولوژی است/ صداوسیما در اختیار یک تفکر خاص است
مجید نصیرپور، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
امیدوارم با توجه به اتمام دوره رئیس صداوسیما به لحاظ زمانی، تغییر در صداوسیما اتفاق بیفتد.
🔹
به یکی از روسای یکی از مهمترین سازمان‌های فرهنگی گفتم، قبول دارید نظام سیاسی ما مبتنی بر ایدئولوژی اداره می‌شود؟
🔹
در موضوع دینداری به معنای عام آن، مسئولش در جمهوری اسلامی چه کسی است؟
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/685172" target="_blank">📅 09:00 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
