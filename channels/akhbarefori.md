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
<img src="https://cdn4.telesco.pe/file/eBh4UXPQ2xY0-9vmDHzCdL7TwRWkS5iQfxG5VoVWK3n2Y7ziC0gol_IP-PB9mXyZ6NbdUuwKVOuVhExU6PcnbkvKXSrnqrrUvWgAFE6LycpjUwSu3lc9JYKswvW4etKcH5my_meNJ6AynkIbJGK5EVxWYZYD0-A2Kz2FurihEgcAKNlbMu_5B-uBELPQshtKVXxdcMDAumEsM58_DZ2bnwxqBgxUfXYOFJr2R5W8QJ70TWKD9YU_p7-OO93x_ifiMa-JeJfTelwMAgX6KwgmJUn2m8ACT4YJMLtoU3pIrzA8de3ocm3BbMulq6BfU5Dk116plUpcit6ajCmCGZp8JA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.44M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 17:00:45</div>
<hr>

<div class="tg-post" id="msg-667932">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
آسیب به یک نفتکش در پی اصابت پرتابه ناشناس در تنگه هرمز
سازمان UKMTO:
🔹
یک نفتکش در پی اصابت پرتابه‌ای ناشناس دچار آسیب ساختاری شده است؛ این حادثه تلفات یا آلودگی زیست‌محیطی نداشته است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7 · <a href="https://t.me/akhbarefori/667932" target="_blank">📅 16:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667931">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLZ99yqcpSsQc7NdBFWJIc_TaPGTa1DIUPR00_TVCuxiTqsdxnCglNUekVW-mKK9RfP-Dc6AsrMWsC_AnvHfs7M9EAg2XjVyixsyGK4ZF8wawWKR1vgkYA6TCyZRfKLJyOjEtZko7h-B-6TpGCI41frreAXNpQTZ5a9MxorTdB98OqRQS-8eduzFfLAsTWLpGpV3mZgdODKnNoidNbkZC_XTaFo6imEp7TA1AaFUz6ReXf7thf0fsl4wEFzp4EPyGJEwvWym2wQbg9hFJSd_ar0_o8ttuLwrw1xNc7Qj3vRI6mtOvnsmYjaMN5yJKvqL3PBxbqfIq2FXNv0Kqw1U_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آسمان قم میزبان طواف پیکر پاک مرجع شهید شیعه، بر گرد مضجع شریف کریمه اهل بیت حضرت فاطمه معصومه سلام‌الله‌علیها
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/667931" target="_blank">📅 16:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667930">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQ4vdbaQrDrHx_PnFVBnVb84_IMaiIKoZNTt8PryaCGPrUmQroKQXdhzKBwVFn_m2V77-rJ5SAxaShJ2BpzB9CNDNYp6yOeMPHuzHxfRY-4_BJ3RjE7hjFrMSWfTGm-uLiBZRtBcIOT-BrwyJpeNIkbUZH3kAVAliXe3udOWH3EXHBlyMvwRLhE_6lC-tuD3CnQXOcgvWk_2gm_2nrt3wuea5yOLSvmt2BqLt305CiPGXlgQZkPPnHJA1UTV5wiS27aXoNUuF1TirzGl63S9j49JypuAKV7s3q-OxTHBIWuBYJUzygrKtOr3Ri4bSucCa2QOEDJOFZ2fRB_vcmmV8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقایی: اتحاد ملی و خوداتکایی، میراث ۳۷ ساله رهبر شهید
🔹
اسماعیل بقایی، سخنگوی وزارت امور خارجه، با رد روایت‌های غرب، ملت ایران را تمدن‌ساز و مقاوم خواند؛ وی تأکید کرد که ایرانیان تحت هدایت ۳۷ ساله رهبر شهید، به سطحی بی‌سابقه از اتحاد و اعتمادبه‌نفس در برابر فشارهای خارجی دست یافته‌اند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/akhbarefori/667930" target="_blank">📅 16:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667929">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb25b6c43c.mp4?token=rr7it7N-lNOhxkU1MqPUkZoatyJ_m3glSPMDxCLMxkoh5rKaabxVBtqQHbcz72teGiVpvN9yGfyEHkJd8TvSzUca6Q7FTZS6O4ToeptWpuGu-inryI_rJY2PsQ2lhcwKzdNXrb0MivOCJVH0f-HDrwQKIOocjkQdMOw54ZmHTAJoSsRA7cWPDfweQ6GAaaLmjodURItYABv_DVHxn_y7vDM_Jt0hJbKmgysPYsw1ivJ4UneRG0R9L9zpiOtlOCmpM0EZGzy6Ik-0TdyZNVf2Z0vW9C9GZl9vT1RCPKp4ZXkmBC0lFUaTZa27hZSzH03R6_3MFRvuHTtsx0BMB2lA_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb25b6c43c.mp4?token=rr7it7N-lNOhxkU1MqPUkZoatyJ_m3glSPMDxCLMxkoh5rKaabxVBtqQHbcz72teGiVpvN9yGfyEHkJd8TvSzUca6Q7FTZS6O4ToeptWpuGu-inryI_rJY2PsQ2lhcwKzdNXrb0MivOCJVH0f-HDrwQKIOocjkQdMOw54ZmHTAJoSsRA7cWPDfweQ6GAaaLmjodURItYABv_DVHxn_y7vDM_Jt0hJbKmgysPYsw1ivJ4UneRG0R9L9zpiOtlOCmpM0EZGzy6Ik-0TdyZNVf2Z0vW9C9GZl9vT1RCPKp4ZXkmBC0lFUaTZa27hZSzH03R6_3MFRvuHTtsx0BMB2lA_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: من از ناتو خیلی ناامید شده‌ام، ناتو [در رابطه با ایران] با ما رفتار خوبی نداشت
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/akhbarefori/667929" target="_blank">📅 16:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667928">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f088ce62d2.mp4?token=KLMcl0thgb8zVLUSJHEZQgvxE2_j5ThmUtWZx6WbImMAw6y-F4bFgOy-v9wWSVza020Mzpov5DEOADfVLoCzIXFaonv2rXnq1aTbCLF6lqKY2laJkyJMt-AeOY3uEv_CEjYcJgbBlblNC0afFA1hzRZgapjD4nW-SKvSwyc3WKgP7qzAqv_lxzJp9_sfLnpsdKvcNcIho79t4A3IW050vXwiW_VEwu5GPZk-j0qipgC6mQ8OIzkwCDOj1CAyR-G4eOHExDfhxJxhbxGhRs9I9lbOOzYNymKuXDjo5OIKO2ij4etBw_mHNIYULL6XiWOHNG8KLReAW79wblzD6XxwMaNmEiyAJRgzL4f-Fxhg7YWOtuj_g8P8Ro220wOfBzonFbdu6mRZa2oDukO3Iz0LdmC_2FMwSpeKVAdinNmaGfNuY_xDgy4sJpVvnNcMIhEHG1_m6DVNyw--ynG7PV4KuwtrQ-hqxt-3Fe-kJT2pUzJKDD2uJ6R06f4FKnRbuceff-dhoaViMeqe6ahGX1hwk2CB_v12SYDaXdU4Xjl_FkWD2YSAwQItJtyOR3CwsoyLgcOiAfmc2_5IEMUrwxSJ_FLfXzAAljM1pGIDGydInmggibIFNHmxEAIP6FQGzFBtitbwytQZ7rZmr3nJRLgAt7lKthG3csr8PI-xFavesaU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f088ce62d2.mp4?token=KLMcl0thgb8zVLUSJHEZQgvxE2_j5ThmUtWZx6WbImMAw6y-F4bFgOy-v9wWSVza020Mzpov5DEOADfVLoCzIXFaonv2rXnq1aTbCLF6lqKY2laJkyJMt-AeOY3uEv_CEjYcJgbBlblNC0afFA1hzRZgapjD4nW-SKvSwyc3WKgP7qzAqv_lxzJp9_sfLnpsdKvcNcIho79t4A3IW050vXwiW_VEwu5GPZk-j0qipgC6mQ8OIzkwCDOj1CAyR-G4eOHExDfhxJxhbxGhRs9I9lbOOzYNymKuXDjo5OIKO2ij4etBw_mHNIYULL6XiWOHNG8KLReAW79wblzD6XxwMaNmEiyAJRgzL4f-Fxhg7YWOtuj_g8P8Ro220wOfBzonFbdu6mRZa2oDukO3Iz0LdmC_2FMwSpeKVAdinNmaGfNuY_xDgy4sJpVvnNcMIhEHG1_m6DVNyw--ynG7PV4KuwtrQ-hqxt-3Fe-kJT2pUzJKDD2uJ6R06f4FKnRbuceff-dhoaViMeqe6ahGX1hwk2CB_v12SYDaXdU4Xjl_FkWD2YSAwQItJtyOR3CwsoyLgcOiAfmc2_5IEMUrwxSJ_FLfXzAAljM1pGIDGydInmggibIFNHmxEAIP6FQGzFBtitbwytQZ7rZmr3nJRLgAt7lKthG3csr8PI-xFavesaU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ خطاب به افسران تشریفات ارتش ترکیه: مرحبا عسگر (آفرین سرباز)
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/akhbarefori/667928" target="_blank">📅 16:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667927">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ادعاهای تکراری ترامپ: ما توانایی‌های نظامی ایران را از بین بردیم و این کشور هرگز به سلاح هسته‌ای دست نخواهد یافت
🔹
من ۸ جنگ را متوقف کردم و معتقدم نهمی را نیز تمام خواهم کرد و امیدوارم که به‌زودی به جنگ اوکراین پایان دهیم./ خبرفوری  #Devil
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/667927" target="_blank">📅 16:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667926">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ادعای ترامپ: ترکیه به لطف من در جنگ با ایران درگیر نشد و آن‌ها نمی‌خواهند ایران به سلاح هسته‌ای دست پیدا کند #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/667926" target="_blank">📅 16:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667925">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95776d88da.mp4?token=dA7bvVYUKP3psEHh6BlzYn7d_bBHfDvuI5ZIUmYf3009b0NK1_DQrr-jE2oqknHBNdK0_QOaXUUT4j8faB8v1Byzw_0eI0I-wIKvqTUpO42-w4PfyMSEhRapxwmnxhtRvdYDggVaLR5uFKqeV8I7RnYTy2xbgLnUtEUIGXIrxrvtzHtpLK1yNPVBPgdGdhO_47OaigGW0F0ecwyQoyYLg0feaoipV7dLuSpSVw2sHmgGiH1G-6aWY0uZ_NyQJ6_gOeCTgI7jJGpan_uMnjIfe9KHBjb9kjArEBUx5asTBftgaawA9WE8jvVSh7OnvHdwpDYiyuMsPXxe-Fjesr1Jag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95776d88da.mp4?token=dA7bvVYUKP3psEHh6BlzYn7d_bBHfDvuI5ZIUmYf3009b0NK1_DQrr-jE2oqknHBNdK0_QOaXUUT4j8faB8v1Byzw_0eI0I-wIKvqTUpO42-w4PfyMSEhRapxwmnxhtRvdYDggVaLR5uFKqeV8I7RnYTy2xbgLnUtEUIGXIrxrvtzHtpLK1yNPVBPgdGdhO_47OaigGW0F0ecwyQoyYLg0feaoipV7dLuSpSVw2sHmgGiH1G-6aWY0uZ_NyQJ6_gOeCTgI7jJGpan_uMnjIfe9KHBjb9kjArEBUx5asTBftgaawA9WE8jvVSh7OnvHdwpDYiyuMsPXxe-Fjesr1Jag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار خودرو در دمشق همزمان با سفر ماکرون
🔹
انفجار شدید یک خودرو در نزدیکی هتل «فورسیزن» دمشق و برخاستن ستون‌های دود از این محل، همزمان با سفر رئیس‌جمهور فرانسه به سوریه گزارش شده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/667925" target="_blank">📅 16:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667924">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ادعای اردوغان درباره تلاش ترکیه برای میانجی‌گری در روابط ایران و آمریکا  اردوغان:
🔹
ترکیه تمام تلاش خود را برای بهبود روابط ایران و آمریکا و پیشبرد صلح جهانی به کار خواهد گرفت.
🔹
وی همچنین از برنامه‌اش برای گفتگو با ترامپ درباره غزه و امیدواری به دریافت جنگنده‌های…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/667924" target="_blank">📅 16:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667923">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ترامپ: احتمالا با اردوغان درباره ایران هم صحبت می‌کنیم/ روابط ما با ترکیه در بهترین دوران خود است #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/667923" target="_blank">📅 16:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667922">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
ترامپ در پاسخ به فروش F-35 به ترکیه: فروش F-35 به ترکیه را بررسی می‌کنیم؛ ترکیه از بسیاری از متحدان وفادارتر است
🔹
اردوغان: رئیس‌جمهور ترامپ همیشه به قول‌های خود عمل می‌کند. من معتقدم که در مورد برنامه اف-35، یک تصمیم مثبت اتخاذ خواهد شد.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/667922" target="_blank">📅 16:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667921">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/50945cb8e8.mp4?token=U-B1-enqwS5huWVdiep7BirIpHMXcqv2y8uKutJyZkcROvDIpSppp40vrEXGSFL02JCcVLmkx_Qqrv0toSknZqDGtgMlZbLc6Syd7nBpmLWauc6XxE35DQZVY19xw9WLUWQBmi4ICMsb9Qhu6txbXI6JmsBc257kFiYVyMD8yIh6ZUPJIq3GQvRInPNrX2DXLfUImO61OIMh1V0rTvvdbiJQwXLw4rnx6haNdp0PMw4xAOZo8o6ELOA0eHClyv4YFewmmhHW-BrHNZLiTkj4DZV4-gUn4i6E_od35DVXVzQLoVLTClYGXhB35f4ALKULugMYJAknXGd_yVFpkSox4A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/50945cb8e8.mp4?token=U-B1-enqwS5huWVdiep7BirIpHMXcqv2y8uKutJyZkcROvDIpSppp40vrEXGSFL02JCcVLmkx_Qqrv0toSknZqDGtgMlZbLc6Syd7nBpmLWauc6XxE35DQZVY19xw9WLUWQBmi4ICMsb9Qhu6txbXI6JmsBc257kFiYVyMD8yIh6ZUPJIq3GQvRInPNrX2DXLfUImO61OIMh1V0rTvvdbiJQwXLw4rnx6haNdp0PMw4xAOZo8o6ELOA0eHClyv4YFewmmhHW-BrHNZLiTkj4DZV4-gUn4i6E_od35DVXVzQLoVLTClYGXhB35f4ALKULugMYJAknXGd_yVFpkSox4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت حمید گروگان، از کتابی که موجب شد اشک‌های رهبر شهید انقلاب جاری شود
🔹
در قاب《پشت جلد》از شبکه نسیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/667921" target="_blank">📅 16:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667920">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dd7f2f09b.mp4?token=WPBi_qK-DeOGGETGfzTwdxADXJyxgw0g2ouZtZ59pKFQubB0bIzIAukygzvMxFiO1qrzSh0JlmfcQsXktIoDiTZZwUOi6he9cib11jguOWJeT-LdEp49BU76AsRaGrKVXTqqc3V-O5iwkafvZawhW7-DNpj8DriE-0cF1chtxSjxqcEru9epqKWP4BqIQiyXx4A2g01L-n2Ibp981jlZjnbwY1Aa4ZntrE5daoKCFHsLf6Pnc6Mls68jDtWuzqKH1IQ_tLkzql0uAonK2mUXeuen3TgxEwk78jgZeLL9hUVRMLQpIeAoYltJTXQZNYsNJkZ_hIk_FoXyBrCR5VXG_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dd7f2f09b.mp4?token=WPBi_qK-DeOGGETGfzTwdxADXJyxgw0g2ouZtZ59pKFQubB0bIzIAukygzvMxFiO1qrzSh0JlmfcQsXktIoDiTZZwUOi6he9cib11jguOWJeT-LdEp49BU76AsRaGrKVXTqqc3V-O5iwkafvZawhW7-DNpj8DriE-0cF1chtxSjxqcEru9epqKWP4BqIQiyXx4A2g01L-n2Ibp981jlZjnbwY1Aa4ZntrE5daoKCFHsLf6Pnc6Mls68jDtWuzqKH1IQ_tLkzql0uAonK2mUXeuen3TgxEwk78jgZeLL9hUVRMLQpIeAoYltJTXQZNYsNJkZ_hIk_FoXyBrCR5VXG_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ در پاسخ به فروش F-35 به ترکیه: فروش F-35 به ترکیه را بررسی می‌کنیم؛ ترکیه از بسیاری از متحدان وفادارتر است
🔹
اردوغان: رئیس‌جمهور ترامپ همیشه به قول‌های خود عمل می‌کند. من معتقدم که در مورد برنامه اف-35، یک تصمیم مثبت اتخاذ خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/667920" target="_blank">📅 16:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667919">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
تعطیلی سراسری عراق همزمان با مراسم تشییع قائد شهید امت
🔹
علی فالح الزیدی، نخست‌وزیر عراق، دستور تعطیلی رسمی ادارات و مراکز دولتی این کشور را برای فردا چهارشنبه صادر کرد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/667919" target="_blank">📅 16:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667917">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ادارات کدام استان‌ها سه‌شنبه و چهارشنبه؛ ۱۶ و ۱۷ تیرماه تعطیل است
🔹
مشهد: چهارشنبه (فقط مراکز آموزشی)
🔹
سیستان‌وبلوچستان: چهارشنبه
🔹
گلستان: چهارشنبه
🔹
لرستان: سه‌شنبه
🔹
یزد: سه‌شنبه
🔹
تهران: سه‌شنبه
🔹
قم: سه‌شنبه و چهارشنبه
🔹
سمنان: سه‌شنبه و چهارشنبه
🔹
مازندران:…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/667917" target="_blank">📅 16:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667916">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b889e7ffa5.mp4?token=g4CY5eDmSPOKFJixuTiJ0xL6hEIjtqsvvVb0tXpowChBu_E2w07SXI2ob83Ye03JivUAU-tmM-fMNiql3rypGsjjeUdBfWrko0ggVD8kVpo3JlsQJL-QYQfXJnlLSqbG8YT2D_YlSC3hXrrYvGKsvjqlgrf5abLteqVuY6pHcNkVj0222m7jCoYyrk487OdoeBp4pEscAu7hBZbN5Hw_z0xjqUStOa8lui6nBZsedxEHszumOrmpXArbJed_A4YXPlUw9OAxe-HpfYxCZ1wSaOGG7uXxrcCC7_RelC1u02Js_uJBZ0GJqLc5-S7Khp7f0zQZbwk9_rkZUipjS-NCCEQ_QLKDNAzBtKXv5R_hy-xzw9ycnKW9ecy1Qg58Xk_1ESUo3_hp-N-tDFT0H3fu2C9j_NisdX4XGZjyrnH9IJs-7shhxKfKOdTFeccI8Qh2kFSyNHNyc70zikCdWuwHxl-_wZjXCGMBYhexYY8dGJihk6K-jkhIIWoMZynuRzj6kffg_dch-GjlZUvAxwXrTY-FgkjPZdiHUIcjCc0roGatw8UkcqfU8wfW3-OFO9_KBQvs3rjnnVvDLVTfgA62r8fMEvxgVdci3Qwk-qD0RP4P99mUL8felA5Ks08g-BxKLBhBCL3EsSHWE3RM1XXZKcM-yCGwQi01mtvpDtUA7C0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b889e7ffa5.mp4?token=g4CY5eDmSPOKFJixuTiJ0xL6hEIjtqsvvVb0tXpowChBu_E2w07SXI2ob83Ye03JivUAU-tmM-fMNiql3rypGsjjeUdBfWrko0ggVD8kVpo3JlsQJL-QYQfXJnlLSqbG8YT2D_YlSC3hXrrYvGKsvjqlgrf5abLteqVuY6pHcNkVj0222m7jCoYyrk487OdoeBp4pEscAu7hBZbN5Hw_z0xjqUStOa8lui6nBZsedxEHszumOrmpXArbJed_A4YXPlUw9OAxe-HpfYxCZ1wSaOGG7uXxrcCC7_RelC1u02Js_uJBZ0GJqLc5-S7Khp7f0zQZbwk9_rkZUipjS-NCCEQ_QLKDNAzBtKXv5R_hy-xzw9ycnKW9ecy1Qg58Xk_1ESUo3_hp-N-tDFT0H3fu2C9j_NisdX4XGZjyrnH9IJs-7shhxKfKOdTFeccI8Qh2kFSyNHNyc70zikCdWuwHxl-_wZjXCGMBYhexYY8dGJihk6K-jkhIIWoMZynuRzj6kffg_dch-GjlZUvAxwXrTY-FgkjPZdiHUIcjCc0roGatw8UkcqfU8wfW3-OFO9_KBQvs3rjnnVvDLVTfgA62r8fMEvxgVdci3Qwk-qD0RP4P99mUL8felA5Ks08g-BxKLBhBCL3EsSHWE3RM1XXZKcM-yCGwQi01mtvpDtUA7C0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایش قدرت هوایی ترکیه در آسمان آنکارا؛ جنگنده‌ها بر فراز ترامپ و اردوغان پرواز کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/667916" target="_blank">📅 16:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667915">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c99b8b38d.mp4?token=o7T929SgThYuYVv7lvFUyXG-ECTc_79OpYmRaZDKkv-bz5nnov7ZOs_N7ZaXsRHThKKO3arpu12_d34nQ8aNW5QiWTO3Xd2abMHeJbT3BtF2WTbDDsxdOu2x94p_svVVq879KB7V7eup2Gi3lFO0dECfKZd0PzNAZ8M_WI2ITesnzaAWL-4zwG5ywl92W_uS5XP0cwLV01XaLElTkxeAw69d4nPgfg3N24uH6rljXsNsYsgD_TkabJU0fPCEQg0OurfcIAAcmJvYZsD57xYN3Cn20LT9mLdeUwIjoW6OZNr1016mwRi_Y6xpycNyXDJ4QouZQdsgoesl1HqOakmPCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c99b8b38d.mp4?token=o7T929SgThYuYVv7lvFUyXG-ECTc_79OpYmRaZDKkv-bz5nnov7ZOs_N7ZaXsRHThKKO3arpu12_d34nQ8aNW5QiWTO3Xd2abMHeJbT3BtF2WTbDDsxdOu2x94p_svVVq879KB7V7eup2Gi3lFO0dECfKZd0PzNAZ8M_WI2ITesnzaAWL-4zwG5ywl92W_uS5XP0cwLV01XaLElTkxeAw69d4nPgfg3N24uH6rljXsNsYsgD_TkabJU0fPCEQg0OurfcIAAcmJvYZsD57xYN3Cn20LT9mLdeUwIjoW6OZNr1016mwRi_Y6xpycNyXDJ4QouZQdsgoesl1HqOakmPCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: ترکیه به کشوری بسیار قدرتمند از نظر نظامی تبدیل شده است /مردم نمی‌دانند که این کشور در واقع چقدر قدرتمند است. آن‌ها سربازان بسیار خوبی دارند
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/667915" target="_blank">📅 16:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667914">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
تلویزیون العربی به نقل از منابع: لبنان با انتقال مذاکرات با اسرائیل به رم مخالفت کرده است. هیأت لبنانی به طرف آمریکایی اطلاع داده که بر حفظ مذاکرات در واشنگتن پافشاری دارد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/667914" target="_blank">📅 16:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667913">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
درب‌های حرم رضوی بسته نخواهد شد
محل دقیق تدفین پس از تصمیم خانواده اعلام می‌شود
هوشمند، مسئول روابط عمومی ستاد بدرقه امام شهید در مشهد:
🔹
محل دقیق تدفین رهبر شهید، پس از تصمیم خانواده اعلام می‌شود؛ مکان انتخابی به‌گونه‌ای است که بانوان و آقایان به‌ترین شکل امکان زیارت همزمان داشته باشند.
🔹
هنوز درباره اقامه‌کننده نماز بر پیکر ایشان تصمیم نهایی گرفته نشده، ولی نماز در حرم رضوی برگزار می‌شود.
🔹
تدفین اعضای خانواده در کنار ایشان برنامه‌ریزی شده، اما تصمیم نهایی با خانواده است.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/667913" target="_blank">📅 16:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667912">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
رویترز به نقل از برخی منابع امنیتی دریایی خبر داد که یک نفتکش حامل نفت خام در نزدیکی عمان آسیب دیده است  رویترز همچنان مدعی شد:
🔹
نفتکش حامل گاز قطر که در تنگه هرمز هدف قرار گرفته، به دلیل آتش‌سوزی در اتاق موتور، در معرض انفجار است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/667912" target="_blank">📅 16:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667911">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8qk0n4ez5t4tOH3G-yA2h5haOm3FQUf5exfvH8_h_39OaUGits_OQq3uBkmMWF3AbV8n0EM5mCChOMHFk1cJJ2nbFp281LvKMbug9sP7UGJi_8VEL0t4LsTJZqOwNEFYgwg1iE_WosPqkPRnKDrS9o7ArDDObNwdvxB1kPQT-hI9eLjExzMUwpXbsFyaJYNUCYo3lfB8UUcW9r4_lPz_q-CXFyA1MFcRgy0ebGJVO6AQeNKfg2XOOuPqG8-jikDbxc1dUKYJydq7oi-xWVsf9UvR5slQchhguaFGQc4ISXEdt07g4PkpZoPYMx-vQQTQFOG51nBuYeI9Lxii24W9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طعنه فیلمساز ایرلندی به حماقت آمریکا و اسرائیل بابت جنگ با ایران
تایک هیکی، نویسنده فیلمساز و کنشگر ایرلندی:
🔹
«آن‌ها تلاش کردند ایران را دچار تفرقه کنند؛ اما بی‌رحمی و حماقتشان نه‌تنها ایران، بلکه تمامی آزادی‌خواهان جهان را با هم متحد کرد.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/667911" target="_blank">📅 15:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667910">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
جزئیات جدید از حادثه برای یک نفتکش در نزدیکی عمان   صداوسیما:
🔹
به گفته برخی منابع، نفتکش «الرقایات» متعلق به قطر، قصد داشت با حمایت نیروی دریایی آمریکا از مسیر عمانی در تنگۀ هرمز عبور کند، که پس از بی‌توجهی به هشدارهای مکرر، هدف حمله قرار گرفته است.
📲
🇮🇷
…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/667910" target="_blank">📅 15:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667909">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30bd08b26e.mp4?token=sQZtTVa5yYUXwScvsc5SRhSDNWpRWtUFHyrnddAttUxaqRY4xRU9OmkTXdG5hXDfOQeIo-Vn_aF3guzpCmX5-IS9dkgkDgUbEEIvOuBZI4KiMJx3rBrVwh7fRIYaYu5OWV6jJhtL3OfBYyd0CIiI2xJ4G6i12gBCnIjWztjNTBxHO8IhtL_Evd6cmdoPH8ppqfoKeRkM6cE113YU5YhL9MPkbMp9_I1Q4OIqioqd7kzQaEEdMjZcMfHulRBJaC8Pz2ezPT-wUzx4eqabFoXIvOdmPfUGsalhrFMJ3tiMlKdDO8b5dbxceehI934VNMFYWaKM7xhoW2e1RTFLOvCLXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30bd08b26e.mp4?token=sQZtTVa5yYUXwScvsc5SRhSDNWpRWtUFHyrnddAttUxaqRY4xRU9OmkTXdG5hXDfOQeIo-Vn_aF3guzpCmX5-IS9dkgkDgUbEEIvOuBZI4KiMJx3rBrVwh7fRIYaYu5OWV6jJhtL3OfBYyd0CIiI2xJ4G6i12gBCnIjWztjNTBxHO8IhtL_Evd6cmdoPH8ppqfoKeRkM6cE113YU5YhL9MPkbMp9_I1Q4OIqioqd7kzQaEEdMjZcMfHulRBJaC8Pz2ezPT-wUzx4eqabFoXIvOdmPfUGsalhrFMJ3tiMlKdDO8b5dbxceehI934VNMFYWaKM7xhoW2e1RTFLOvCLXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: مراسم تشییع رهبر شهید، نماد اقتدار و عزت ایران است
🔹
هم‌زمان که همهٔ ما سوگواریم، با تمام وجود به روش و منش رهبرمان افتخار می‌کنیم.
🔹
ایران امروز مقتدرتر و سربلندتر از هر زمان دیگری ایستاده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/667909" target="_blank">📅 15:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667908">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
| فصل ششم
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/667908" target="_blank">📅 15:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667907">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20c8990e1e.mp4?token=i9q510oqGqd1rMoJFgkYF2bK_FWN8jnTjucWrl_G1euYEZyU7lUKY4eIt2juE8wgNMlA7YGBACuPXj96MKqGQaq-TlWVCuRSnMP_9YqmhpcCOQz_nkIv9eihsT1dMiJJ1KnPNgZRrYPMAmViWc6jI8GojFj1G6fYUIgYbgVIdIlPqFi10eXqYWuRA_IIzT4Rx6dOgKKHl7ofwZtv_TJ1oUlq49ZTMPYJDb-fYcfyoRABGxsEDVzrQ0I02s8Vzn5PvWd7DCfHhvm919qolNORHarBa9ITmhTu5bhKedMuNafEOjoDfnGN_YK5Jtp3YXQl2m5TwFCPeJfgBdIuKlwj8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20c8990e1e.mp4?token=i9q510oqGqd1rMoJFgkYF2bK_FWN8jnTjucWrl_G1euYEZyU7lUKY4eIt2juE8wgNMlA7YGBACuPXj96MKqGQaq-TlWVCuRSnMP_9YqmhpcCOQz_nkIv9eihsT1dMiJJ1KnPNgZRrYPMAmViWc6jI8GojFj1G6fYUIgYbgVIdIlPqFi10eXqYWuRA_IIzT4Rx6dOgKKHl7ofwZtv_TJ1oUlq49ZTMPYJDb-fYcfyoRABGxsEDVzrQ0I02s8Vzn5PvWd7DCfHhvm919qolNORHarBa9ITmhTu5bhKedMuNafEOjoDfnGN_YK5Jtp3YXQl2m5TwFCPeJfgBdIuKlwj8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه باشکوه طلوع خورشید در پل خواجو‌ اصفهان
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/667907" target="_blank">📅 15:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667906">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJd8HLpNBaLpFqHdxvrHxXYfU_lD-VsaloaoWNAvENwbOHHsromDHZZqyIZrm8MbXqbWCnpxiBb37cpz2Ce75q0COmO7psS5y2QwmwY8SUc1E2bemDGXwk3KAgwtTvXR3838jUwuvUHyYgvw47vWlRnqCOsRDXAHaY4MX0eyrEtA8hWPD11gi8T0-MOGprog3aen4DlqXfAWE5T1Wy2HbJjwJ-lRlSrj9C5DD5IznuN_YGcqsYoYnK5mqPAovoJiXHSUXZSTAJnVt2r39dSLpfPqi-f9tbv8kwDqX4ELgfy1GH10YesOvmNadVc7Lb9qZsjzAjdd80erS5I0L5BylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/akhbarefori/667906" target="_blank">📅 15:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667904">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
تلویزیون العربی به نقل از منابع: لبنان با انتقال مذاکرات با اسرائیل به رم مخالفت کرده است. هیأت لبنانی به طرف آمریکایی اطلاع داده که بر حفظ مذاکرات در واشنگتن پافشاری دارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/667904" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667902">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e252bea2de.mp4?token=PArfuHYWVvJcLIO9gZnoQ6VBHOCqm17Irgrw8aNYs0Hsai9U-Sx6Ga30mpZEKl2C56zr7gp1SXXgLoT0QnMO2euQ8YLul8RaHDjEDt2Pi3UqrMOSif--_EiCV51cwh7RndUACQTBTq5vwvX6OhtjhSfXsxgMNjyc7VTPt8zTl-zIiRCbU0c97Swwwvuif8XMw51gWgKPLFdiPvGYyzdKjSqJ0ftruGFYn0pi6ACQKRLApmT97I5lhJ5O6qlHUMKyrxOb5eLWk_RDmkK9us17oQWGmqYbJ5BCoxGo8Pm6uD1g1JXiwYL4qXHhiOI1G4WQZNxZBdpvgo9FZ3SZhJDNLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e252bea2de.mp4?token=PArfuHYWVvJcLIO9gZnoQ6VBHOCqm17Irgrw8aNYs0Hsai9U-Sx6Ga30mpZEKl2C56zr7gp1SXXgLoT0QnMO2euQ8YLul8RaHDjEDt2Pi3UqrMOSif--_EiCV51cwh7RndUACQTBTq5vwvX6OhtjhSfXsxgMNjyc7VTPt8zTl-zIiRCbU0c97Swwwvuif8XMw51gWgKPLFdiPvGYyzdKjSqJ0ftruGFYn0pi6ACQKRLApmT97I5lhJ5O6qlHUMKyrxOb5eLWk_RDmkK9us17oQWGmqYbJ5BCoxGo8Pm6uD1g1JXiwYL4qXHhiOI1G4WQZNxZBdpvgo9FZ3SZhJDNLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
روزگار سیاه آمریکای حذف شده باوجود رانت «کاخ سفید»/ شیاطین سرخ مقتدرانه به یک‌چهارم رسیدند
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/667902" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667901">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2963d22c1b.mp4?token=Q-7VKz48ur4QTwLKbtwhR76W82zGUelPqfN29pzbxGHM4zRk6TnVmufk08pvnKRmP3_zjX5ni_TqTYnF0baDxa5SaVBUXQ-GWCUxI5dkXJNqAw_FM9jE8tgnoH30kTimCbz_c-hx0FOoEBp10fFmPtLuEyrqFTEW_CgUWYHBxTxpYSamUtNjFyx10GGzABrAvccUIFnUIew0OLry519DV5lBHKANSbv8OsVPx1r-xKWqVAnDlIrvu8-Zd0vZoS_u9T53NCmTTc13rtBn7fyWViRebo4Erpabg0R5MsAuoDkpDpO_V5y4mCAZiEMuYzNLrhqlNGqyYG06FryuSuB9Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2963d22c1b.mp4?token=Q-7VKz48ur4QTwLKbtwhR76W82zGUelPqfN29pzbxGHM4zRk6TnVmufk08pvnKRmP3_zjX5ni_TqTYnF0baDxa5SaVBUXQ-GWCUxI5dkXJNqAw_FM9jE8tgnoH30kTimCbz_c-hx0FOoEBp10fFmPtLuEyrqFTEW_CgUWYHBxTxpYSamUtNjFyx10GGzABrAvccUIFnUIew0OLry519DV5lBHKANSbv8OsVPx1r-xKWqVAnDlIrvu8-Zd0vZoS_u9T53NCmTTc13rtBn7fyWViRebo4Erpabg0R5MsAuoDkpDpO_V5y4mCAZiEMuYzNLrhqlNGqyYG06FryuSuB9Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قابی از پیکر مطهر رهبر شهید انقلاب در لحظات ابتدایی حرکت در مسیر تشییع قم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/667901" target="_blank">📅 15:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667900">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-text">♦️
ادارات کدام استان‌ها سه‌شنبه و چهارشنبه؛ ۱۶ و ۱۷ تیرماه تعطیل است
🔹
مشهد: چهارشنبه (فقط مراکز آموزشی)
🔹
سیستان‌وبلوچستان: چهارشنبه
🔹
گلستان: چهارشنبه
🔹
لرستان: سه‌شنبه
🔹
یزد: سه‌شنبه
🔹
تهران: سه‌شنبه
🔹
قم: سه‌شنبه
🔹
سمنان: سه‌شنبه و چهارشنبه
🔹
مازندران: سه‌شنبه و چهارشنبه
🔹
هرمزگان: سه‌شنبه
🔹
کاشان و آران و بیدگل: سه‌شنبه
🔹
مرکزی: سه‌شنبه
🔹
خراسان شمالی: چهارشنبه
🔹
بوشهر: سه‌شنبه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/akhbarefori/667900" target="_blank">📅 15:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667898">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZwgUJAmvOvSauVLeJOi-HXC71I5-Dr5xIfQzzJVPDYqdqOUDbnFprSdKLPHVuUyqVAdQs4DFrFZDtqEsbyggN2j6QpokqAcyCHLWZ9Ze88J2JwYVUIkZAqTlM9gckfBp_Ba59WHPb41zLxa-UCTTCTw86uccfVkzhq8JKCTmqk-KoGiZbMO7x5DtaCm0azK_QNaipEhzx3cWppRBJwoXGMfpyVhsY8AbMgxQBuvxh7J8p02WqqqaPTz_rTO9cGoel6YLScJgXGU0WqFvKdUGFcfGaN5Yyg054_eCJ5DaqSkWaQS8cflv_ae1cGFXiLMBSIHn0d4riwswn-bWVMP0Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QWdxaPrR9qxWy7uLAVQolYGXP5wLJkJdjpPieuT8Egw0F8LcABkyYG4grhO0fuynb15FMG4MY7VVOttgO4ss8UBFifcoYUTI2BqGK2ayvTgR5ADvMKvfkYBNIu_OXl5ta3bEq3GWwxBXTdSG2mXpDzY5nm4R6D_WvoMPFNouX7zBV9s7Suxqg-BU2Di3dgoGBHmCVzb1BadAsSGRH41VwX48GREri0M19goKcXuAJ3Ga3b2ojNDYCDNbqT0InuyGzW2rECjhRt0xeAciVak7rzOx5UXe5_jF3uxk0KPot2mN4seoTV91TsdI5uK2s0O3t8eaSDB4CBq_7a7ToeJ9OA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
رئیس‌جمهور آمریکا برای شرکت در اجلاس سران ناتو، وارد پایتخت ترکیه آنکارا شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/667898" target="_blank">📅 15:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667897">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مراسم تشییع پیکر شهید رهبر انقلاب فردا ساعت ۶.۳۰ صبح به وقت ایران در نجف آغاز میشود.
🔹
لاوروف: امیدواریم مذاکرات، تنگه هرمز را به شرایط قبل از جنگ برگرداند
🔹
راهداری: مردم بلیت اتوبوس بازگشت از قم و مشهد را از قبل تهیه کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/667897" target="_blank">📅 15:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667896">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0b38e9ed.mp4?token=kfxldECpB-Svzm6hURM_XavWdRXh7_NRJ7ad6gjvEq0fLm1Yc8mU_YxLQJ8mrHwYfAMgDaDYwKstm-sxlJTCHwrG7DaYS9VmHi27nHJGi7ccvCOB3Wl8P2eY_I6ybPyYUSYKmLGPE2TgqcN7PT5XiH88NG0LpowqxXF2IMoIGbMij3AgwAlmJiwzAdFLU4KJ6OHNsk_GxT93s6tX6a3oeqD54ZIlh9WXFGfRSszKp93E1scCk8Mvf9Qi0GBwvfHQvG9n6vAUeAoapW36tHS2Oe_hd4Ww9ezz-OMtgxwGrLgfZxVBEt5x_vxZAFRSLBhtLg1CyKvgkDKgrIYfE3C3mz_qFjldHNgt1SRGbPWnTDX45xGZvO7RnEw4RWhuohQ10QxrGu0XeGoGAF__K13p0jEfKEoMsCPCV6NAD8bFR7aTb9GKh8e8jIApJ5DSyaKY1Kq3hqzgTwb_QkOCZvpI2QIXi8w9DYRbm20VKufAo6sbHh_ZWvLxT_kM_Cy3cz5omTep3Yx23g1jCgR9nW8ZXVGtdyF8BPfo169nDBtdJ6HUTUe1dAH4VU8VDaSVW3WE1Zb6SwSreKrgm3ocotrRo6Dvnm9I1FuhI5munUNXc1-59guoMirUrBe1oX_QrinsVOpWnNBPyqGrWi4F_7YOHsLgo_dPj7SfO_gd7ZupZm4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0b38e9ed.mp4?token=kfxldECpB-Svzm6hURM_XavWdRXh7_NRJ7ad6gjvEq0fLm1Yc8mU_YxLQJ8mrHwYfAMgDaDYwKstm-sxlJTCHwrG7DaYS9VmHi27nHJGi7ccvCOB3Wl8P2eY_I6ybPyYUSYKmLGPE2TgqcN7PT5XiH88NG0LpowqxXF2IMoIGbMij3AgwAlmJiwzAdFLU4KJ6OHNsk_GxT93s6tX6a3oeqD54ZIlh9WXFGfRSszKp93E1scCk8Mvf9Qi0GBwvfHQvG9n6vAUeAoapW36tHS2Oe_hd4Ww9ezz-OMtgxwGrLgfZxVBEt5x_vxZAFRSLBhtLg1CyKvgkDKgrIYfE3C3mz_qFjldHNgt1SRGbPWnTDX45xGZvO7RnEw4RWhuohQ10QxrGu0XeGoGAF__K13p0jEfKEoMsCPCV6NAD8bFR7aTb9GKh8e8jIApJ5DSyaKY1Kq3hqzgTwb_QkOCZvpI2QIXi8w9DYRbm20VKufAo6sbHh_ZWvLxT_kM_Cy3cz5omTep3Yx23g1jCgR9nW8ZXVGtdyF8BPfo169nDBtdJ6HUTUe1dAH4VU8VDaSVW3WE1Zb6SwSreKrgm3ocotrRo6Dvnm9I1FuhI5munUNXc1-59guoMirUrBe1oX_QrinsVOpWnNBPyqGrWi4F_7YOHsLgo_dPj7SfO_gd7ZupZm4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهدی خلجی، روزنامه‌نگار و تحلیلگر سیاسی در بی‌بی‌سی: آقای خامنه‌ای قهرمان شبکه‌سازی هم در داخل و هم در خارج از کشور بود. ما قرار نیست اگر از واقعیت خوشمان نیامد چشمانمان را بر آن ببندیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/667896" target="_blank">📅 15:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667894">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwmkdKww2ZbahGkHJQFEw0pSNmUwPH5RfKtP0PHbcq5fiQLrOpr-cXxT1oC8EkoIh2lA9DghPxF9rU0wl6dzinSsHFDL7MoPaHkoydBxTkDaEUw8mO5XEJ53jAmHuH91s1YvIrcTkr3egrmo8FYRgM1I2fwO-OjbWRF7yZFdYqENVEnV2m7UvrIiJNUVN0jWqDadv86cx8yWRf0lebpAJwS_lwy5sogCOCcNdM0OEEis5tIvVo_pDAhyHWJjzQMwabkefnh4-KC9AluI80ar6tmjxg2shgCZYtYlcyJgESQfpYFB8OVANbUcFCmrpWiqvqwJynVocSTQD2io1AYJLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استوری پرچم سرخ مهران غفوریان برای خونخواهی آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/667894" target="_blank">📅 15:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667893">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fb8e46b00.mp4?token=fF1RdyfJwHJIRHC6-BliF4ruXBKnqooLAAdNURtRrPYESJhmyN5wsjlT5I5KjLkqUJ1bnt7DfYL-ZVDKg2lNyF5UuFjt6-339h-J0Ej7XatsMsRbEaFhhNKPN6yl5IKuszb_fDZ8hergxpA5RV1h5FVnvHSgN8HayKhqCReGo91O9UgunnrsdInqgTZuec9Gmtrcn4KcWw8LDDq1oUESvrhCwhW3fOFXdy0LT5lZG-SLaUqPgbbewb9zozhlF-HzPE9UBRKoZ03Dt-jiQyrhe1whkmf9gA9zPLNKzoiQ80IFRfcIavzXlhOiHwzagMzQ8AfSz1qK_qFvnknIHrwuRzJKhYVFgxyWPM6nbiBUlwoRUEQBcayaKtvKWtQmkRUrzD2AWsUZ52wu2X8Dg3SO2sUTi0mTSsvlfEfdCJQZ4lkrNw1xaquljaRYtdgR93k6_4C0y2NBXo4e0ud3BGdzszm2Xf8LhdBwO1sYiv0cKQ0KQizOQtBNGsppzSqx3k0H10r4b7zVKqPTIBceiXIvU8WbnXkEjE5H53AuH6YF-GBflfSU106wozrEGQ865kgiD9Gwx8cO1NdXgoRiKv56BBiSrp7-3JzXR1GcZFPuqTwn2-D8ZuHRal1O5xoM30ObVG82ckza3_BqPptGhPx0qjWCFJVx0u1r_qGHEwZtyPM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fb8e46b00.mp4?token=fF1RdyfJwHJIRHC6-BliF4ruXBKnqooLAAdNURtRrPYESJhmyN5wsjlT5I5KjLkqUJ1bnt7DfYL-ZVDKg2lNyF5UuFjt6-339h-J0Ej7XatsMsRbEaFhhNKPN6yl5IKuszb_fDZ8hergxpA5RV1h5FVnvHSgN8HayKhqCReGo91O9UgunnrsdInqgTZuec9Gmtrcn4KcWw8LDDq1oUESvrhCwhW3fOFXdy0LT5lZG-SLaUqPgbbewb9zozhlF-HzPE9UBRKoZ03Dt-jiQyrhe1whkmf9gA9zPLNKzoiQ80IFRfcIavzXlhOiHwzagMzQ8AfSz1qK_qFvnknIHrwuRzJKhYVFgxyWPM6nbiBUlwoRUEQBcayaKtvKWtQmkRUrzD2AWsUZ52wu2X8Dg3SO2sUTi0mTSsvlfEfdCJQZ4lkrNw1xaquljaRYtdgR93k6_4C0y2NBXo4e0ud3BGdzszm2Xf8LhdBwO1sYiv0cKQ0KQizOQtBNGsppzSqx3k0H10r4b7zVKqPTIBceiXIvU8WbnXkEjE5H53AuH6YF-GBflfSU106wozrEGQ865kgiD9Gwx8cO1NdXgoRiKv56BBiSrp7-3JzXR1GcZFPuqTwn2-D8ZuHRal1O5xoM30ObVG82ckza3_BqPptGhPx0qjWCFJVx0u1r_qGHEwZtyPM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار شیخ علی الخطیب، نایب رئیس مجلس اعلای اسلامی شیعیان لبنان با سید عباس عراقچی وزیر امور خارجه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/667893" target="_blank">📅 15:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667892">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceba014aff.mp4?token=oDqhGSJhc0RxXVbUPRn7OX-8NKZx7OJ3eLDloFBSORDSjzFLPQ93gAxhyJFN7fQ442j3Pjr21C4Tvtltm9aWZ5lAw3xItlSp2BTAuT6De7CvClZEDNac9_5AnrHGVWDZmYCgBmP6U-PV0dz3Y9MwWW-8_EDIgqdXn-P799HLzCginh-aXYFCiGs3Tq3zXv9q4jxzW6Z2khbnfdsJ-UlVAL4nl3dC74djmMCVqMDqMtHmUWgLcfNw1CgZI7Fp9_3Oy4BknGrNp06CMK-NxoDlsyLjc811-j3e-zBlpwELbiVE4dTgL4-wrCmKZNsa3fXblY-PnHMWXk056DhhWnnlyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceba014aff.mp4?token=oDqhGSJhc0RxXVbUPRn7OX-8NKZx7OJ3eLDloFBSORDSjzFLPQ93gAxhyJFN7fQ442j3Pjr21C4Tvtltm9aWZ5lAw3xItlSp2BTAuT6De7CvClZEDNac9_5AnrHGVWDZmYCgBmP6U-PV0dz3Y9MwWW-8_EDIgqdXn-P799HLzCginh-aXYFCiGs3Tq3zXv9q4jxzW6Z2khbnfdsJ-UlVAL4nl3dC74djmMCVqMDqMtHmUWgLcfNw1CgZI7Fp9_3Oy4BknGrNp06CMK-NxoDlsyLjc811-j3e-zBlpwELbiVE4dTgL4-wrCmKZNsa3fXblY-PnHMWXk056DhhWnnlyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رویترز: جمعیت کثیری در تشییع آیت‌الله خامنه‌ای در قم شرکت کردند
🔹
شبکه رویترز با انتشار تصاویری از حضور گسترده مردم ایران در خیابان‌های قم اعلام کرد «جمعیت کثیری در تشییع آیت‌الله خامنه‌ای، رهبر فقید ایران در شهر قم شرکت کردند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/667892" target="_blank">📅 15:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667891">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879aed6238.mp4?token=LmpCHyfFPhK3r1ykypRiRQ5O7Vd0hoFh3Vvq3AjHbEpF3EGUdUNXz1td83X3lk0VdFGBNGKa98ak59E7aB26fis8zX--coWOwqZscr_utQNWgJfvMDeAhQhmpZeG6CM1d42G1EwbSn0avqGn0no9L4El7PiFQW3R2XlcyGCOspWL1X61a9B-7NYOcoAtGZyqwOANymV569TNvQpq9Nm3OWvKvYdv7FjxDRV9QgQWYYAn_3P5rq7xDJhNK47lxJgDDC0HEBX9jGXeI2XFaJ7Cgv72_R5RZF7benQ-jFzgArAccZjekWqeZ6M0Yquaaxty-LzR9pfTCfSRKHbLKt624g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879aed6238.mp4?token=LmpCHyfFPhK3r1ykypRiRQ5O7Vd0hoFh3Vvq3AjHbEpF3EGUdUNXz1td83X3lk0VdFGBNGKa98ak59E7aB26fis8zX--coWOwqZscr_utQNWgJfvMDeAhQhmpZeG6CM1d42G1EwbSn0avqGn0no9L4El7PiFQW3R2XlcyGCOspWL1X61a9B-7NYOcoAtGZyqwOANymV569TNvQpq9Nm3OWvKvYdv7FjxDRV9QgQWYYAn_3P5rq7xDJhNK47lxJgDDC0HEBX9jGXeI2XFaJ7Cgv72_R5RZF7benQ-jFzgArAccZjekWqeZ6M0Yquaaxty-LzR9pfTCfSRKHbLKt624g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زلنسکی در اجلاس ناتو: ماهانه حدود ۳۰ هزار نیروی روسی را از بین می‌بریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/667891" target="_blank">📅 15:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667890">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
نجف مهیای میزبانی از قائد شهید امت می‌شود #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/667890" target="_blank">📅 14:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667889">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvRb1OaqAeoHi2jQiEZwYFjWkiGlvNn8jvRcUcw1sKZ2vDodoy6DxI8hzhjvtYPtbE3VxZ8lGncsOA8nmloVJ32wZdSFd_B1wxcCFyrRRLg8ubs21-j8je-v0Ul_QFU49zHhiN4iNUDOZgMTFLrf-JzwZ9gddohkAr90PTZKDDOtMhce9B2_-ENdPtjp8cV44VXBlFjqxGvA5nzLAkWcUjQ3oIEytpAwrKW5A1d__OUMz3D9f-6B0v2sP6DIUehG6qEuy-imPgvC9mo2rllUylTvakGrrB28GyQnbL7mapLaLvIRxY0nE_xlezX0M4kZEFpzoce7a-U6FB59KEfBVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عمامهٔ مشکی‌ات ماندگار شد ای آقای شهید ایران...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/667889" target="_blank">📅 14:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667888">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8a1fb142b.mp4?token=hYRetBUo6JJ0GkO_dm59RJ5zUjEJQHFRMO6mp_ermCHn20UR5lNYOneSVCp-7Co605ovQWWrIErh_iWrRmephTZDmvGbWql_LRE4KL2_4Qj9TBPZC_Z8CL27J_qlS0Al4NB9xYVlV7vDftu6AzE9cCA03aHbTf0gFAWSD9hb7iQmiyT2jVFXXW7hGbfQol0Li06Lh9ZYthLtds_nTWsOumwpVe8sjop-vhlQdTMnsu-UUUt0BwtqcBwVsp19jq8lu3M0HK1PD5Qr1HeuYbV2fxuTlwVNJM15S7GDZm9BqueiZhE7Q-EI0fCdnGZLUDZ5Z4pj7lBG49ASQSbI1woALKYizeJBMX8SLTxpwfdxOTEzBhMoHJShWOuZw1q5I5tjMiXzbFLzLVuoa999Fcojj0P1peIhQ7-YGiZK3yVLEYZWKNr7z37BUMOENKW91366qa5-2UAoXqzs4qAhEDA3buF0RYzYYjHWHoCRCfFU1EgotPGAiC5Fm_MWbw29F9nm-oL3RyyM0hNWegvuTP7aPopAOJQFbrDuGLyavskSYrvOW9QESIJprHGX_2SGmpdy5t2HJci_VKUZ_mHrXh3tbSobwR76_WSVZCnCLizYZDZYQi6A6R49lSNc4KjtdcKtSZ2FkTykGXobE2Wvt7U7JMKNJHJVKaZqBvOSrHVhwUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8a1fb142b.mp4?token=hYRetBUo6JJ0GkO_dm59RJ5zUjEJQHFRMO6mp_ermCHn20UR5lNYOneSVCp-7Co605ovQWWrIErh_iWrRmephTZDmvGbWql_LRE4KL2_4Qj9TBPZC_Z8CL27J_qlS0Al4NB9xYVlV7vDftu6AzE9cCA03aHbTf0gFAWSD9hb7iQmiyT2jVFXXW7hGbfQol0Li06Lh9ZYthLtds_nTWsOumwpVe8sjop-vhlQdTMnsu-UUUt0BwtqcBwVsp19jq8lu3M0HK1PD5Qr1HeuYbV2fxuTlwVNJM15S7GDZm9BqueiZhE7Q-EI0fCdnGZLUDZ5Z4pj7lBG49ASQSbI1woALKYizeJBMX8SLTxpwfdxOTEzBhMoHJShWOuZw1q5I5tjMiXzbFLzLVuoa999Fcojj0P1peIhQ7-YGiZK3yVLEYZWKNr7z37BUMOENKW91366qa5-2UAoXqzs4qAhEDA3buF0RYzYYjHWHoCRCfFU1EgotPGAiC5Fm_MWbw29F9nm-oL3RyyM0hNWegvuTP7aPopAOJQFbrDuGLyavskSYrvOW9QESIJprHGX_2SGmpdy5t2HJci_VKUZ_mHrXh3tbSobwR76_WSVZCnCLizYZDZYQi6A6R49lSNc4KjtdcKtSZ2FkTykGXobE2Wvt7U7JMKNJHJVKaZqBvOSrHVhwUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشک‌های رونالدو پس از حذف در جام جهانی   #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/667888" target="_blank">📅 14:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667884">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HdEW1muYEdQpqbGndjYXTFdbG9HAL6cv-OhWd40yWEOtQEgAHptTt7dwQuhujGuGzBXBGrzjnz-8nt1WEAipSVfmikFtlj3gBNDabgHFUCVY3XMrrTJpGXetYFIt_5QMjT4LKtkhlihl8boQYBMR20QHpDRgidxk5w38IeDUgYk3k66BD3AJFCpd9jGtqa4E3A02bDunlFjXxW8IyWPyzeU3CeCB--WbwEfD7GxZT9Z-PV8cSyylynnS48wCWi0O6O_TYAAej-o3FWDq96l3ikR5b1ELiNois4QohcaNC1Dz1Sz2NCcb7YhdrtF2ouNNJ_CDpZc7J6gs9laALGAegQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nzn7UJe2iT-VqyCBUwuNZWjRpRCjI03BL9FGNJGFVK2DdICw1E9smUQiow7K7rJlGEB2Z6AZSzort77rKG9MYK6BCXsrpCcjVaDgHUysSxCbNvGmZwC0gBdrXiHNHWAhUmztn5SxwupRWHbbU5Jt7cuRbNRGk55efO6sXbWc10FKFJb1O5v5jR5_2A28XtufPxk8jyUeHuFSKJehiWX-WRafVF2-O-RX2KnTR0jzd_fwCNYuB98RRsPMs9AQ0u1wm73cqwv7EnbAsraWcwluj9lSdDn1u8PxPGfEVWGTEf1DLekwS_iOrSvVTdvWGaLO6EznRncUdI8i60B1a1eWvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/353a17da48.mp4?token=JmmTja5muKgBn1xf6P9g4mxwrGUdpCf_Ob-B66t7orZw-VH_QcH-kCNRSwcyQ27N4b50PCgc0TEPbYEtqbRmZz6mW6u2Tv5MeYPTn40RF7ZcbyrG8TSSLWQFXH_noYpL3oK6GHbK_xgZ8ernSFEDjJYeDHCwaMvtBKsC9vJ_i4pKNBKgq9QEr6yOASX1fzEYFqfQyQ7WgUgkNXWGbZFqI9AS4Ch70JE3eBm2Lm8mjHFxXGNjtuLXAVd0MvV1jQAYidkDZJld151_1QxSl9NdA6TrnzOEWy8gyZRPP7jc_vfJvdCFcw7Gz-h7SGjjszK_HyRZaRWNHN3FebvGRUsZpg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/353a17da48.mp4?token=JmmTja5muKgBn1xf6P9g4mxwrGUdpCf_Ob-B66t7orZw-VH_QcH-kCNRSwcyQ27N4b50PCgc0TEPbYEtqbRmZz6mW6u2Tv5MeYPTn40RF7ZcbyrG8TSSLWQFXH_noYpL3oK6GHbK_xgZ8ernSFEDjJYeDHCwaMvtBKsC9vJ_i4pKNBKgq9QEr6yOASX1fzEYFqfQyQ7WgUgkNXWGbZFqI9AS4Ch70JE3eBm2Lm8mjHFxXGNjtuLXAVd0MvV1jQAYidkDZJld151_1QxSl9NdA6TrnzOEWy8gyZRPP7jc_vfJvdCFcw7Gz-h7SGjjszK_HyRZaRWNHN3FebvGRUsZpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز حرکت کاروان‌های پیاده‌روی اربعین از رأس‌البیشه؛ جنوبی‌ترین نقطه عراق به مقصد کربلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/667884" target="_blank">📅 14:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667883">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
کارشناس مسائل منطقه: در ترکیه خواستار تعقیب قاتلان رهبر شهید هستند
حامد خسروشاهی، کارشناس مسائل منطقه:
🔹
شهادت رهبر انقلاب، در ترکیه بازتاب وسیعی داشت و هیمنه ابرقدرتی آمریکا و اسرائیل در ذهن ترک‌ها فرو ریخت و ترک‌ها معتقدند امام شهیدمان با زیرکی توانست موضوع موشکی را به پیشران نظامی و سپاهیان تبدیل کند.
🔹
ترکیه یکی از شرکای راهبردی پروژه اف‌۳۵ بود اما پس از جنگ اخیر پایگاه مردمی خود را به سمت پروژه‌های موشکی و پهپادی بومی سوق داد و خود را مدیون رهبر شهیدمان می‌دانند.
🔹
در ترکیه احزاب اسلامی بیانیه داده‌اند که نباید اجازه داد قاتل رهبر شهیدمان با حاشیه امن به کشورهای اسلامی سفر کند و نباید این جنایت عادی‌سازی شود.
🔹
رهبری تأکید کردند که باید پرونده شهادت امام شهیدمان را در مجامع بین‌المللی و دادگاه‌ها پیگیری کرد و از اهمال در این زمینه در گذشته انتقاد کردند.
🔹
رأی دیوان بین‌المللی لاهه باعث شده نتانیاهو از سفر به کشورهای اروپایی حذر کند که این اتفاق باید برای سران آمریکا نیز بیفتد، هرچند امید کمی هست اما باید پیگیری حقوقی ادامه یابد.
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/667883" target="_blank">📅 14:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667878">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNDsn4NIhLZBr8GmEEKcXxnHqLQTyGfKlOQHMzs8KwQLgkP2b6jIKr7cOAA8tLO7VH6sCmcA10bCg5FdaokvzUOaqsR5Q8KPjhPTb_oamMH62GmsxNadfBKwDUAa3dQw7idE9v081uHQbgf_nC-MOc_VRdGiupRND_TE7mt_Q3GqeyLiS0PmR46Ed-6_1MZeWG7Nbzc535-hH25eI9gyqlY-hHWTmZGWvCD2QSv-YpUafk621Qn7jfA_Tt0cGpPaklkAfckAIsDOurPQEYkCMxPz9slcPEYrc4NJnHAvRiSn1bD0_sJhgbSx9T8QgSwFsenBDVIodGPsed3BBnIglA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/htkXCYWXljam3yc8iXH_zOx4FH-xYW1_q36-cYUcUSvn7arPXBqnj--r8jW-T5_89p9c5-S3HfIv9RUk9g0h8HWdijx6-y1qsUB9-QDCnP49PsxLbxoMvXRr8iDYlr6r0qVooRXlCZ1p3Nm1Y2oJYymLzLgknwF2xACteniTYpkNvH76SJdMy2zp3JZpfrpoaucwU1RZ6ckHFqAybfVlQd-_jEMJfbdgLSh8qMUlCZ29eq5zuxXO4dSgLmdU1UEUbYac7Hde8qECHU3-SnQCZPRnYaHDB8v9UXkY9rVnk_MwFTeYnxGXoPh5IGs3fZdBU6Z94Rr_eMzSv08P88InjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KYsOwX6yc7-9QWOKqKo8xTJf-_hmUNXBJ6GlfFMFZz0I3ZkjBGSVZNQ-UHWRixFGmui1ziOmyYfpZ7pu05mMM6O1AUCstPkOe3B4HNTmuzsaRYsIZosVmnkIuUCJH1oInslN2MRTdoWEm8scAfsxZfv0FNnt7gC5KK9td3BY1GvGMZntX2yMHFhJn0Gxk1f50bBCU83rSdGr_UWY7FEPdsU-DOFqukLt1O_Fqh6RrzugRRkQldWftqtWdSKA29UQT_0KQve8QcqmISMIf3l3iALw1ss3cz166df14yMB-jcHApORaUI0vRG38R90zcPVPfgzruIYcUVtTnBk2oQ7DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j37H85Fo-ZydDNeAl_Kgqn0Ci1eaCiRGGmdMKSzfyJnwqWXd-XPweoH5xyq9-y6_466uq58RSBSg2znp-oPildqrInV6Jc2NYTKuWm3nQ_icSTB00yk1dx9QU8DWZ4OiegIO8yEHPwJwvjZDUb1duv62yOWGC5KNn1t4oucP4NluZuOh0rynqCQumXvY3-n5PQCBN5VgPrr7QBX_ufz-5yQJ0l0YbxDp4maTViXimtpwQHcloDBjej-h9xcsLCuFChj62dQ3YiXEFuq3r5vwlDY2AjQEvph9zQutsCJ7wp_nPe6HP6HXtOR7ivpeYUn_HqnosK8ZgTgn82TS97M8zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sP_9gj3a5jYjXFxfWKvYTlu6uy33cYON95YlRZKO34iEKFVKSLplgWu4C63KWIqPIHadOvhVz_h5QM2vk7P8TcUWF--WSKlojILx4EpSpsg4IPtFS0GansqNljn9MX74LrzsYP-FvJ-_ERzjrh-3-Xq865oM4f0UFd4AtQEUodrdQOZHbyxWfZdCVwep1ZWn48wrMlVHBOuHoyZklLRlRQcZSmb1ZZ4UNvuNMnsuxENo5lW4ImvxB5nqKbNJeCJNnwSn3McvgwCUHu3EvZG7oSqAvdxJX4q_3e7sPC5btuYM3gE59VeUbi0jqMWqZ6EfplEOQcSKaDmRt4ZZSkEAuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تلسکوپ جیمز وب در چهار سالگی خود تصاویری حیرت‌انگیز از کهکشان قنطورس ای ثبت کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/667878" target="_blank">📅 14:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667877">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
رئیس‌جمهور آمریکا برای شرکت در اجلاس سران ناتو، وارد پایتخت ترکیه آنکارا شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/667877" target="_blank">📅 14:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667876">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e09e0c86e.mp4?token=YJ8b0lK0ZNHFZplDcWIghfEbHjbdFVnEkLmDHVDB6MdIVTAi3KF8rUFgsHtd7ELXlyKr4fwxqtqmMEiH-LSta4CE0de-8N7yaVEc0jgK7281ZR_MpBE5CjzXGovxjxEnYIAEGfGdpmnA8cJXq5i9Q8scS9RhTnwNYEB3fLhmcSqGrXd3YVVa2t7hFSjI-DLZWsvDK3dW2wVzoYOLDNKq07yCTeURsAGnRdpu_OTNu8ZvzzWXUEQz5qFUqy5xCYRn4oBGCSIGTkABJE583E1Fi5ccCKPSDMh4PI1KBeTiEkGyp588lE5JoxAM7cllCejZTGDgQGY2rymowlUhfvk3fWyR4IRyLiJQT80CTFtILD9a89rfY140G75LWNeA4d7VpW4PhN9uLeBII6vhsRV3DlNhw6dIgaWW2lyEuk7udQNvaU_j5ohCC4sSzQcQMlrdeSUznE-ZrMlIsABS3aEJUOd-KveK3vxkIynNUdObm1rvtlo8waIbJXumfzVUhzD3lohSOD3vUN1456orgfJmT2hP3XRcosyQ61jwIsIK-qYA3ZYvaMsJi6xLt6CcNe8Lg0GimdDMdBkJLqCHLVSXvpRmJZhAPYCIGtgUQ2SjTK8jHI3DkNP59JCB6FV0bZXJDz7HI7kn2jIrdmpluN1EIkiqO9mSlpZtm-hDWo1ids4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e09e0c86e.mp4?token=YJ8b0lK0ZNHFZplDcWIghfEbHjbdFVnEkLmDHVDB6MdIVTAi3KF8rUFgsHtd7ELXlyKr4fwxqtqmMEiH-LSta4CE0de-8N7yaVEc0jgK7281ZR_MpBE5CjzXGovxjxEnYIAEGfGdpmnA8cJXq5i9Q8scS9RhTnwNYEB3fLhmcSqGrXd3YVVa2t7hFSjI-DLZWsvDK3dW2wVzoYOLDNKq07yCTeURsAGnRdpu_OTNu8ZvzzWXUEQz5qFUqy5xCYRn4oBGCSIGTkABJE583E1Fi5ccCKPSDMh4PI1KBeTiEkGyp588lE5JoxAM7cllCejZTGDgQGY2rymowlUhfvk3fWyR4IRyLiJQT80CTFtILD9a89rfY140G75LWNeA4d7VpW4PhN9uLeBII6vhsRV3DlNhw6dIgaWW2lyEuk7udQNvaU_j5ohCC4sSzQcQMlrdeSUznE-ZrMlIsABS3aEJUOd-KveK3vxkIynNUdObm1rvtlo8waIbJXumfzVUhzD3lohSOD3vUN1456orgfJmT2hP3XRcosyQ61jwIsIK-qYA3ZYvaMsJi6xLt6CcNe8Lg0GimdDMdBkJLqCHLVSXvpRmJZhAPYCIGtgUQ2SjTK8jHI3DkNP59JCB6FV0bZXJDz7HI7kn2jIrdmpluN1EIkiqO9mSlpZtm-hDWo1ids4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار خبرفوری در بین‌الحرمین: حال‌وهوای شهر کربلا، آماده مراسم تشییع پیکر رهبر شهید است
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/667876" target="_blank">📅 14:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667875">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرودگاه بوشهر، فعالیت خود را از روز شنبه ۲۰ تیر از سر می‌گیرد.
🔹
فارن‌پالیسی: مهار ایران شکست خورد/ خلیج فارس به‌ سوی نظم امنیتی تازه می‌رود
🔹
امروز در حاشیه اجلاس سران ناتو در آنکارا، نشستی درباره تنگه هرمز برگزار شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/667875" target="_blank">📅 14:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667874">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌ونهم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ خانم نسرین جاپلقی که در سانحه بسیار سخت تصادف جاده‌ای، روح‌شان از جسم جدا شده و به خاطر رؤیت روح مادرشان و فضای بسیار زیبا و دلنشین برزخ با وجود درک سختی دنیای فرزندانشان بعد از مرگ ایشان، باز هم تمایلی به بازگشت نداشتند اما با نذر و نیاز بازماندگان به دنیا بازمی‌گردند اما همسر و برادرزاده ایشان در آن سانحه از دنیا می‌روند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: نسرین چاپلقی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/667874" target="_blank">📅 14:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667873">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nir2H0RTs8DL6gHgkYBX0pNLdvOPkde6tBjxdlBiX7rDVEuYc1CaiHrSg_SshXFrvwElDk7Hriahy5dSzBjcmXjLn0eTD7wuFPtAXvu8Q4QexqjztnqWZukMDEshpd3hrtPGqwMcxN0WFVsxx1SAGOsG4c46XcAtVa-1SPmD5-1WXgI4coeQ2nEpZQbwUlv-_o9uja-LlJDE6AYjv45GBo-SOT-jby55Tp4XOXDgkxl9KktQVvrfPyJKfR5AFPF7C4U0lCCWSI6KgaVMbXB1x-IfXE5nE7qgMIi4Zo7HF1HtWwvLukGxxwQYyT_-TA2Vump3AgVjBSDlc9jzoLHIJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت طلا و سکه
؛
امروز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/667873" target="_blank">📅 14:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667863">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U7UsLf3zWN76bkdsbihUbBcAZAON19JWSdU-KIUTM1kWvr7_uJY5PfUuYukbsH9VLalmmWXLsxdRrDBTD0lP82IRy--cqlO0RmhFvITPqTlMSKD3JbfNN8RBeks-9_Ex-MxZ257jugb1dC7NtYgkzus6iJtQLALRCPo5t84qsEdHGkQw9lo4Rr7MCa4QYZoqOJX8-UKuwH5rtfWDqq_X6uZV7B3Ez4Az2MLNTAYe0ZvSSH5-7RkYB0F36wDMEo3ckqZXPIguJPuMljqsko4ehV-ZI3TLsaM2x2JpgjaJfNHcw1tOp9SabrBB2_fS2oTsiOmfGjIQMz0a3Wu2H2UWgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sk-_lhli8FhaceI3tAp_N0l-4_WxHpH5LXpt-ng5JTNwwILlN18UXeH0UNz9Me60_X_Rynyz5Q9Z8-5BlLip1QwRqDV3P1Bux5cZKoOIgx5toVjwIs9EkKGsxUVoYEWZdz1WtZHbKBt_007-j2roDO3tdq9Qf8LOvAMYXkwNGEBemaxrz8OObUpezHukcs1YuIJGRTeRMvO8U3viPajmnA-Y4k6v7cYZaqTgBsvdLdMbEOb2ofKhPdQDtGyxvRTUhTEpbUcFoTD3Q1KBQxX_7DmGlY2aHaAmpOtWpM05ybymAlxInwuEkAZnCBT0KXZ6fV4073NHcgdQYWHjGMtZMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l68hoHEqcHRRyqa5WlH6289lbD3F8rvObLYnJCyh6HhwLFzqMZGmGv9juTRylxRSaqYsDwlk7lUQHIrPAU9Pi8TIXioUs80kEo_7-jttbphnKF4vRDJRr0Usw2we9f5ahzCJDlAqLwsGFHmiLoPfNusjNKJIkviKxPC8faya7EvVy0UrOZqW0fl8i_RwNd4a27eGT6jyuXGv7jChyh_XEHmuiRH6jg2vpz5vZyHzAsfhnsFCwbdoNsN11imXXg374V-Om5-tGXvqDkZ0spZSbThrsOJ19RLgY_dX4muGalEQLZf6SrPxrgxAMH5tdmwK2m9XqfiJ0iEUja9s_VNlJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERNDbZGpjoBssCQnUXdatEeVThELh_f9K6btmxVsGwa-ClB5EHXFuc6fRpk6PHeliRRJTx34MWdUMP2QT_4Zrz1f5823Guvu2M7lZkLp7F_1u-iOngfXN_8hUor14ZovetB-Jcq-uzyWuUU7EsyGKZUQcoBLSO3lW34FF14eg0kaxyD3RnMQ-R74RWasSP8YlXeeLutv495AGPXxSlV80i1IrswOlw001Y_3ebkPdq1mPD5PVVKEIXXQitRgA76fJzwUeFf5nPqTB0pMkkKtYRqi_A7ijJ6lLcUeWo6lXSHREV2EPjy7HrgOIPzivr01JsvuhCWoaKbwBszvsDEBPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q6kg2sts6EVINr1slCwqcOGGqsKpHQzLf2exvFLIUXANkdBNyroiepN6KDm5dOmHPC2OtbIyUMtdDW_YdFRSTr8xVIw4osdO_7ziodwbot1fu9ys77UxYIpjAFM8SrfCRXJlYY0pAswhg_Auf20HiAFxMYQbyvaCXyVg7Z1yPJuhtowLW_hGl15Yfo6z5glHJBaTvkIKpNwWd4X14AqVtAdfZ2Bt57IYtJCATMdp_vWruWd-5emKxkZ1CyDdskGleRIQa5h4Z3_IgT42jsQPvkw2OHdZoPG-gThv9qBEXTKNAcuVTaYNW0hPUvxCrXdLSUUqGvWN6TYzME7N2I59Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t4107eRJIfDPIALZs7ubGPnw4fBDFNvGuYBV4ddIVqXysz1Zu4mc7_cAasw_qDkrMbPNemfJi8MAxIvFb17PI1sqb1i56B8xk-4Nd5L3vLup-NTLYcrsxVrjUUNmijpkSMl2b2NLAYtZ9vkFZHonVfDl_IslmSQEeWviJmQX92Gvw-rHpnBBG3ZGZcAEySM6BldT61PmVs6Q-9wULaCWY2N2L0cZfQhv5apLgoylgcKE2bfcwnpNnK9H0m4ydI4gz1F6JeL2zNlHVcAUUTkvhb-27Pa0ntLjtTRckrsm4Lmtss0TYa9Pul75H55TIWyEXXAeaEkAtCURTqUnDsDl6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QY9JvQg4D1BiJXtjz3Xnm-sKU78UTDoXX0TVE5y2ejLGPS1PolrU2tkIgmE841iVxcW-lIi2oT7RXE4y9et9_sBEv0CcdU3ZQHlJ9dcpTeAm0GU-Sv1RFYcMymgXWwmCM56W0xdv0MWFFwtrSr451bRpa_gSKRkhls3VxjulJWSIaee9-HpKmLWAMyIpTtoaItuqmmF2PCBQv6jjgJPm_QApLrRyph-k-J_okot2M1W_C1Pymup5Ycvb7ez3NP4B7_UkjU0EooiI2gNpsbrTtRvMQejeffsWH2vaJHyGpWgBK2MWXb-n2o4i3TfAvcGIVbRhmCRak_NBWU2bJzaR0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EqVP9dGUhYQMIrDLaNqMy-FnojZLXb3BS6w5kw5LjhVqxM4n5HBkV-_cqp6GsvSYVvMH0UWNt4kkVOfiPHJWbYyO1IZ63G7zwxDkNimgT2_Xp2_HjG5jSKaNaEyyqP6LQHwc1fIUZ_EkSFrY8kQbN2R_yq8bfDi-vQwSt405-h-5meSrDwWsblhdHZmziGk95hfPrf6nLdb5CqkJcwcL15iONB4G9AlDhHbV8EK1HGvT9zyd8i169j2VsjYVmkYNBs441fBFwmc7FSaxwFIUr7cGSiX7Mnr--H4NDwR_I75gLJVUf66HHXTwTp1SyKILufXrfSd8EuPY47kPREpShQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V2iMQ2ngHmq2Xg3d5kdmh69tqMe8Zx7w2lfx8ffap9pN6m2yHl2if8GxlPDygaHjYjMprnlGJVmLcHHHwOerpO4eXPiiOjJxBPuf3rHHCsRTmiJqtzdxsHUTmsyntMJhIWjrIlBv3e-PFAAKqs18HIOV2RLV3Tfs0cAt0DWkwNe8H0WLXzH282Hpy9X9aWOPACIHJUx0kVELQwz4rrqlSRjR64_dVN2H_cKbRk35iSjD4_3ZETqabJcXwRl9lLYODEAojiLJY8vU0RtSsomR42SqeBT6wz7HajxvyGqPHYhKGaq6ey9O7z5w5xAvaGXouecu4xeoNyp8DnkrqCPWmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRqnWeHQEAjG1uHeg7Gn_oODSgkyWETqBflGFAgDXZmvFAdp3wCZvun6EpaJpZNS-mqpT9hzZ_GjFrvzSxUfHEoEMyEdoPwShRSOUFYrTJKRTf-4TwYg1-64jKp0aYxa_dBHzjb0n6uk_gt919qJLEibfBRwGQqvK90L7-vFRr8l8f07oWGtWy-Xtum_QAbY2UyGauiMdgtk1JhyqlCQNlA_NYDEe5_7qf28pmHHlwEv39aSm2T9vgpiRwVMSTVBQrwrZsnUhTFxEqe1voVaTi7jtf2PNhXwM7CUbmRHXuPuVxqALBg7qjDqfY-sJdBSFzLkwBZAFk37SEJ0eaGk1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">◾️
روایت تصویری مخاطبان خبرفوری از لحظات وداع با رهبر شهید
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/667863" target="_blank">📅 13:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667862">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/760f4aeabb.mp4?token=qWrgMo0mbnSAJyTAK1bwYVDq8j42fbCCdQU7mdGVxRxzTYnp_YXpRe7yKjhYsbwysZr70ze_Hp1VlQ7uQRrDjEfkPjdGc6Qp3VJ13zkHnNpHtnh5UOg3S0dmm1tsNccP-GVwNsoHYYjCQbx-X-Q4U9KP-Rbn3gQBiSYejY31IxzvB4j2qAPBVhh7p0QIelVfbbZ5TcUhTuhURtva1MnM_wD1cuP-MPwoxfMX61DIBiHrjuRvWP8YH6Hbvj5ePxM7bipPM1csf13_sBepykVhpcd4qrmAoHNc9XrBuMMf6ZX6UCqzThpQQ5_HkdpQwp8ZRI2sKWxF6S-c-nGOIWvC1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/760f4aeabb.mp4?token=qWrgMo0mbnSAJyTAK1bwYVDq8j42fbCCdQU7mdGVxRxzTYnp_YXpRe7yKjhYsbwysZr70ze_Hp1VlQ7uQRrDjEfkPjdGc6Qp3VJ13zkHnNpHtnh5UOg3S0dmm1tsNccP-GVwNsoHYYjCQbx-X-Q4U9KP-Rbn3gQBiSYejY31IxzvB4j2qAPBVhh7p0QIelVfbbZ5TcUhTuhURtva1MnM_wD1cuP-MPwoxfMX61DIBiHrjuRvWP8YH6Hbvj5ePxM7bipPM1csf13_sBepykVhpcd4qrmAoHNc9XrBuMMf6ZX6UCqzThpQQ5_HkdpQwp8ZRI2sKWxF6S-c-nGOIWvC1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زائر تشییع رهبر شهید: امیدواریم مسئولین کاری بکنند که حداقل در دنیا باب نشود که رهبر یک کشوری را از آن بگیری و هیچ هزینه‌ای بابتش پرداخت نکنی
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/667862" target="_blank">📅 13:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667861">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b63dc0c5e.mp4?token=GlXj_NrpjCBWa4Q0wAuUNyTEohmUsHd3w--QMQ2WVSXIYSL6knEU4CiudpeomceQTmXPXkTk-nhGH6iW3MzsDraVL2LJDHiYGwyhjNJJ9DkSiaiUtNCR1hyaC7MaQSIidwuomNEWlqfolnqb6Rcbxs4KFlqEPj6ikyx1bx5RqwUDqvluMwpHRrE5GUOl-x_Wwwd4V0fRwTbwSFxxFBADAlRpvyW7fovI1H4CX6Pakto-_QlLjlPsTkaAIgT8_6D-leOLcEr7TawCQPTDdytRd-5_fYUboEU3Y1DEaVZisidDiFZ9lSuNczOC0VxzWp3_7f4c6g5gS7VxaGKX8LLYsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b63dc0c5e.mp4?token=GlXj_NrpjCBWa4Q0wAuUNyTEohmUsHd3w--QMQ2WVSXIYSL6knEU4CiudpeomceQTmXPXkTk-nhGH6iW3MzsDraVL2LJDHiYGwyhjNJJ9DkSiaiUtNCR1hyaC7MaQSIidwuomNEWlqfolnqb6Rcbxs4KFlqEPj6ikyx1bx5RqwUDqvluMwpHRrE5GUOl-x_Wwwd4V0fRwTbwSFxxFBADAlRpvyW7fovI1H4CX6Pakto-_QlLjlPsTkaAIgT8_6D-leOLcEr7TawCQPTDdytRd-5_fYUboEU3Y1DEaVZisidDiFZ9lSuNczOC0VxzWp3_7f4c6g5gS7VxaGKX8LLYsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرگ بر آمریکای جکسون هینکل فعال رسانه‌ای آمریکایی در تجمعات شبانه تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/667861" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667860">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ناو «آبراهام لینکلن» از خلیج عمان خارج شد
🔹
تصاویر ماهواره‌ای تحلیل‌ شده توسط شبکه الجزیره نشان می‌دهد ناو هواپیمابر آمریکایی «یو‌اس‌اس آبراهام لینکلن» در دو هفته گذشته خلیج عمان را ترک کرده و حدود ۲۰۷ کیلومتر به سمت جنوب حرکت کرده است. بر اساس این داده‌ها، این ناو اکنون در موقعیت جدیدی در دریای عرب مستقر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/667860" target="_blank">📅 13:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667859">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
اطلاعیه شماره یک ستاد استقبال و تشییع آقای شهید ایران در مشهد
🔹
جریان زیارت و تردد زائران در صحن‌های پیرامونی حرم‌مطهر به‌ صورت مستمر و بدون وقفه برقرار خواهد بود و محدودیت‌های تشرف، صرفاً در صحن‌ها و رواق‌های مرکزی، از ظهر چهارشنبه ۱۷ تیر به‌صورت تدریجی تا پایان مراسم تدفین اعمال می‌شود.
🔹
تردد از تمامی مسیرهای منتهی به مشهد مقدس به‌صورت عادی و بدون هیچ‌گونه محدودیت برقرار خواهد بود.
🔹
مسیر قطعی استقبال و تشییع، خیابان امام رضا (علیه‌السلام) تا حرم مطهر رضوی خواهد بود و تمامی مسیرهای پیرامونی این خیابان برای حضور گسترده مردم آماده میزبانی است.
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/667859" target="_blank">📅 13:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667858">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c171544781.mp4?token=thtm6-S8m89WxMWd6XSyKV0ISQbip37Ba7os4HIEWnSUSFZG3GEmBLvdyJpyw9ddL-BOVME2zSGSxHyMRD73Y_b8nlUk9jCjXRzWKevDO6WUEyavA2zYCus-5_zsKeRKm2a21GEjCI__6NGGrxhx0cenevP50TJY_OG-jn2UtP5qiq5Jg47BOKI9CCT3lRB2qRkJP0h0Lz6b0rNYdaWe_Nflp5JECmhz9JiuqR2tdlNJ5tN7JlWTbXWrsVHcjVrALyXjoKIYa0m6dxUiNT-gLlKKEkPnJcVnf2V0V9Kq_ZVQOzw0ymMKYlzu6cWmMZuHaJjqBV4lGfnUOkQ4BVGP6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c171544781.mp4?token=thtm6-S8m89WxMWd6XSyKV0ISQbip37Ba7os4HIEWnSUSFZG3GEmBLvdyJpyw9ddL-BOVME2zSGSxHyMRD73Y_b8nlUk9jCjXRzWKevDO6WUEyavA2zYCus-5_zsKeRKm2a21GEjCI__6NGGrxhx0cenevP50TJY_OG-jn2UtP5qiq5Jg47BOKI9CCT3lRB2qRkJP0h0Lz6b0rNYdaWe_Nflp5JECmhz9JiuqR2tdlNJ5tN7JlWTbXWrsVHcjVrALyXjoKIYa0m6dxUiNT-gLlKKEkPnJcVnf2V0V9Kq_ZVQOzw0ymMKYlzu6cWmMZuHaJjqBV4lGfnUOkQ4BVGP6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راهپیمایی در آلمان در گرامیداشت یاد و خاطره‌ آقای شهید ایران برگزار شد
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/667858" target="_blank">📅 13:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667857">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
فرزند شهید نصرالله: شهادت رهبران، انگیزه انتقام را دوچندان کرد
سید جواد نصرالله در حاشیه مراسم وداع:
🔹
پیوند پدرم با رهبر شهید عمیق و معنوی بود؛ این شهادت‌ها، عزم مقاومت را راسخ‌تر و آتش انتقام از دشمن را شعله‌ورتر کرده است.
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/667857" target="_blank">📅 13:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667856">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
استاندار خراسان‌رضوی: مسیر نهایی تشییع رهبر شهید در مشهد از خیابان امام رضا به‌سمت حرم مطهر است
🔹
نماز در حرم مطهر برگزار می‌شود و خیابان های شمالی هم محدوده نماز هستند.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/667856" target="_blank">📅 13:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667855">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e97bca3cf.mp4?token=pj7UF6A1H5G_W6hI9u92LSBb37MjHB__FieeGLDS8AgLnPHYA4xos1ma3KYem27On4jqSQZ0AMxk_WZVc_W-4dJ01lGClWA4KeTNONjT1iL4sKV1AmegOfR7UNuh9NvFFRVPjIkmCn4A2IbO9ihYfkA6Pyz8E1q_HFGai9yvTSDWNXApoYtTPy9U4pT7GPT3_1aGZevW8TFzpz6Bobq7VXFKiyogUNoaVnPswnnCyz7sCVtk-GkfYD53emhn2-FLxFZ5-sI4CL1apcYbjfxnHjdMrl8LdN0EohBb9QGhOd_2SbX4WYYtVXM7wgGX1SQmdwOCuGho7tYSCskiF4Nsxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e97bca3cf.mp4?token=pj7UF6A1H5G_W6hI9u92LSBb37MjHB__FieeGLDS8AgLnPHYA4xos1ma3KYem27On4jqSQZ0AMxk_WZVc_W-4dJ01lGClWA4KeTNONjT1iL4sKV1AmegOfR7UNuh9NvFFRVPjIkmCn4A2IbO9ihYfkA6Pyz8E1q_HFGai9yvTSDWNXApoYtTPy9U4pT7GPT3_1aGZevW8TFzpz6Bobq7VXFKiyogUNoaVnPswnnCyz7sCVtk-GkfYD53emhn2-FLxFZ5-sI4CL1apcYbjfxnHjdMrl8LdN0EohBb9QGhOd_2SbX4WYYtVXM7wgGX1SQmdwOCuGho7tYSCskiF4Nsxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱۶ میانبر کاربردی برای افزایش سرعت نگارش با Word
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/667855" target="_blank">📅 13:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667854">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNMPjlMjHbhHy0yN9L8QecbnpdNOPW1SjOZb5BIVZpOigUbEIO2iw0ngGfw_qb3ExFeIDm7L06Qeqh9vV6ulOj9OIHn_xK1nVhvk89nDTLIKYOexA4UDc6MRYlv61ZHjJRCnZzsaEbTO4v3dG6XUcz-rrfGt-Z8JspC-HxAsPuC00zdlQdseqBWcDT_yEHyhA7pz2SGkEr0FeU8R4sDIgkC2H12ybMm_GoCgVwqb_IhDl5LdnRs5Tz5KZfla7iOH4BLSP_1uCLVundvNPeqx-s0tBxIC_8mbYe3hefEme-zTNGSfzlLDX2BvhoOtk8ASNXfA6b9lC0Bw5NOpJWVAxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسماعیل قاآنی: تشییع بی‌نظیر پیکر مطهر امام شهیدمان در عراق مشت های در هم گره شده دو ملت دربرابر فتنه های آمریکایی را محکم‌تر و خط سرخ خونخواهی را پررنگ‌تر خواهد ساخت
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/667854" target="_blank">📅 13:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667853">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDLb_koEzPME_pBseGf2NuT7f5S4Jj9_100d5oLEDfzVdCzv4ozp7c3vGhXHsro9LKsLBT8KyKEuGpI7wzfwGIbUbRV_q_qm5d0IoLxQF_XsvFDnaENp-5xArHKIZFMiCJW4usOivddqiTpXxbkDCQfzo5h4drd8XxlVscUZIQUghvQI7499bvpy6RkZ0x-MZrga8w_lkQ--ObUdx-AB5duXiJ2KUyRSQ7D3JgLL22G52J_isvF6qlaGAHc7vgJK1tXkwbTQwuj46_Q6QDnE2EzPOQa7Q-I7AtHawYcFIPwys-vjtbxUNCouWEzGAXt-XjQn_hgEioTzYtEspk-B7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص بورس تهران با رشد ۱۲۲ هزار واحدی، برای نخستین بار وارد کانال ۵.۳ میلیون واحد شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/667853" target="_blank">📅 13:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667851">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ادعای آکسیوس به نقل از یک مقام آمریکایی: دو کشتی تجاری توسط سپاه پاسداران مورد اصابت قرار گرفتند و خسارات قابل توجهی متحمل شدند، اما هیچ زخمی گزارش نشده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/667851" target="_blank">📅 13:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667850">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
وقوع حادثه برای یک نفتکش نزدیک عمان  سازمان عملیات دریایی انگلیس بامداد سه‌شنبه:
🔹
یک نفتکش در حدود ۱۵ کیلومتری شرق شهرک «لیمه» مورد اصابت یک پرتابه نامشخص قرار گرفته و دچار آتش‌سوزی شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/667850" target="_blank">📅 12:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667849">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6153eeeec3.mp4?token=XVx_cDElM0FaIdeKMMBi9KU92sZdIWFkmsPA_1_z9ZYWjlbrjSE5dRC7E2ECCqaHvXj-kRSnhnt-qMIUicpfMgiGkUj5IXsdebqzPZ2GevhUG281Jp6AQq4g8HhCsdrm_W_8G3dXpV8bCb6jw13_ztTOta4YRdYboA0bv2ssf912Xs6fetoyXU0ZbGk25sMyRQ0Pf14mRVQf8-sRehYkfMGNgbDnq6d0qWL_n7GFcY4Glz4GNe-U5KkzQShD5sQicHMJV1SJde9_po6Nf1PnX3km-B45IV6qLdMAmfhnvbUOlhyZu-VIRKh1pb0bjpk65MedGAjV8u2vcXKhrLJ8ADzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6153eeeec3.mp4?token=XVx_cDElM0FaIdeKMMBi9KU92sZdIWFkmsPA_1_z9ZYWjlbrjSE5dRC7E2ECCqaHvXj-kRSnhnt-qMIUicpfMgiGkUj5IXsdebqzPZ2GevhUG281Jp6AQq4g8HhCsdrm_W_8G3dXpV8bCb6jw13_ztTOta4YRdYboA0bv2ssf912Xs6fetoyXU0ZbGk25sMyRQ0Pf14mRVQf8-sRehYkfMGNgbDnq6d0qWL_n7GFcY4Glz4GNe-U5KkzQShD5sQicHMJV1SJde9_po6Nf1PnX3km-B45IV6qLdMAmfhnvbUOlhyZu-VIRKh1pb0bjpk65MedGAjV8u2vcXKhrLJ8ADzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راشاتودی: سیل میلیونی جمعیت در قم برای وداع با رهبر شهید
🔹
شبکه راشاتودی با انتشار تصاویر هوایی از مراسم قم، حضور بی‌سابقه و سیل‌آسای جمعیت برای وداع با آیت‌الله خامنه‌ای را بازتاب داد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/667849" target="_blank">📅 12:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667848">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d2128df50.mp4?token=A_T8LiLFIT808h-zeW5E5G21TQzIy9ETtB9MnZcFIBcKR8_XandF_HtIMElUsuXmt0OuSOGDS-O2aNFMgRpOqG6UZMzL7l0WLl2_Z4n0GfCIoiCVNq4J-lDUZ3rzQfWBlR4XoENe8tyq_bJ4Vun9eZ_Vg6WSTth0wlHv8Nn0VI5dVfMXCTEm0dzk_p4S2Tx12q3js_2HuOKNp7tdbbg-taN9ANHrC-Cj5n5AfN3v3joDFRcpekaGwSPCpicBjiOLawr9lkVdsMahqAsn54WUDDWXmz8p-1Rp3e0Gk6IyJuheOoiJGWBNuVTCLWwDysuVbeCqBUXxq-3QUieRmkrEJYxans1oMG2V6MlxGfH4KxV7xsDi4dbQPFxRjL6lLjNl6fEK7xBe9ysy4WO4bLyO-Z8J9AHbtLGW6z_SxXlU9MUpg41VyJ5o1I04doErmPZeMvEG_pd16Z83G-ImkqWCI8CfG-vImwLCE8OUkFXeQL7lKGrmpAxbwKHp4k8xRcNKItGzVHwTvZk0DZHiqzt8av8iFy6_93pnrtfWcENU0TPRy9PJw0031EklAQilVv6tDvqGrGtek1ZpK1ST7S839NgA4onSmt2fIR51LkQd3F7RUuNtUiOpd-507AuJGDCCp6Vp-qOwsOpvaOOk3nUNpcNblht9KXQ4MWImUfAndAo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d2128df50.mp4?token=A_T8LiLFIT808h-zeW5E5G21TQzIy9ETtB9MnZcFIBcKR8_XandF_HtIMElUsuXmt0OuSOGDS-O2aNFMgRpOqG6UZMzL7l0WLl2_Z4n0GfCIoiCVNq4J-lDUZ3rzQfWBlR4XoENe8tyq_bJ4Vun9eZ_Vg6WSTth0wlHv8Nn0VI5dVfMXCTEm0dzk_p4S2Tx12q3js_2HuOKNp7tdbbg-taN9ANHrC-Cj5n5AfN3v3joDFRcpekaGwSPCpicBjiOLawr9lkVdsMahqAsn54WUDDWXmz8p-1Rp3e0Gk6IyJuheOoiJGWBNuVTCLWwDysuVbeCqBUXxq-3QUieRmkrEJYxans1oMG2V6MlxGfH4KxV7xsDi4dbQPFxRjL6lLjNl6fEK7xBe9ysy4WO4bLyO-Z8J9AHbtLGW6z_SxXlU9MUpg41VyJ5o1I04doErmPZeMvEG_pd16Z83G-ImkqWCI8CfG-vImwLCE8OUkFXeQL7lKGrmpAxbwKHp4k8xRcNKItGzVHwTvZk0DZHiqzt8av8iFy6_93pnrtfWcENU0TPRy9PJw0031EklAQilVv6tDvqGrGtek1ZpK1ST7S839NgA4onSmt2fIR51LkQd3F7RUuNtUiOpd-507AuJGDCCp6Vp-qOwsOpvaOOk3nUNpcNblht9KXQ4MWImUfAndAo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
پخش مستند «بر آستان عهد» روایت دیدار تاریخی وزیر کشور و استانداران سراسر کشور با رهبر شهید انقلاب؛ امروز ساعت ۱۸ و فردا ساعت ۹:۴۵ از شبکه مستند
🔻
مستند«بر آستان عهد»بازخوانی روایت هایی از دیدار وزیر کشور به همراه معاونان این وزارتخانه و استانداران سراسر کشور با حضرت آیت‌الله سید علی خامنه‌ای،قائد شهید امت در هفتم خردادماه سال ۱۴۰۴ است که به مناسبت ایام وداع و تشییع رهبر شهید انقلاب توسط مرکز اطلاع رسانی وزارت کشور تولید شده و از طریق لینک زیر نیز قابل مشاهده است.
https://aparat.com/v/yzsg6d8</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/667848" target="_blank">📅 12:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667847">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
مراسم تشییع رهبر شهید در قم به پایان رسید
🔹
مراسم تشییع باشکوه و تاریخی رهبر شهید انقلاب آیت الله العظمی سید علی خامنه‌ای در شهر مقدس قم به پایان رسید.
🔹
قرار است پیکر مطهر رهبر شهید انقلاب و خانواده شهید ایشان فردا در کشور عراق تشییع شود. #بدرقه_یار
🇮🇷
…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/667847" target="_blank">📅 12:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667837">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAEByMtbzRvqx1EB0JJ4KKpetsHBXH7PVZAmmjYo6BFUxDCVoi8SJyG4JvifBlbPp5Rnw3rWa4JL7Bd_Pkn4Wtjl5DE5ewiahNzrHPDEgLWJuEbh20xjdfCpzVZ6dnHgEPF7HHDL1fK6VkOQEC63iOQv4QNL1wY305vsoXNy-0zagPhldc_G56DUMAq4Kn6R0jM5MH5YFY281G_l4fIEXJCgIjABb0mu0GrfcDyemc7FyyfXt_VlNCP6orZ1ZOY51rFDmyrcyeE_29oy3SsAhzEsQr6YMy3qN-uEwN48lr4dE79sJybFuLwsodFjmTuhnZ7Qg89ETbGyMvOFbOOD3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MOQX8EViBslIhGx-DR6JEuY5XXu6THRxRWf13ZzEmo4hBg4tKIYGx4AycknKZNAwyWMAz-LrwTBQEbOIB9eE3qwLR4zwpADXUnzWJyGqz4wqEcJwzq1NX6cv7I5ZwA2ql2QRgy9TDIb5tYhnXTXFnSS7dCYYI2_BPB2E6ZQ2QwHC8AimeEiJlKsIBBxoWL1_HelSnYuayto362O91XKEycqUtbygT2hlCFxhulnAs9-aBR044H6KSzKrsWUB_EBBy9Fqmcl42beB8xt7XYzZY2Yz3GlXfFM6zQe8R-K7jstPo2rkOPIQTcrog1uYzlNyjGCALwO9SyPfWiE0_fO_JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S6I0GmHRqRMwWk-yuiDODZmPRJxGaz11XKvwvVH6-yLq6KxxGgfIozHiw-9gVUL3pq4gBO1hA_Int1vL3q5XGXSb6NkiEPgBqdGtkbV0_GyRMIz2qEUSg97PqeK7QPAsEFms835qhaFkDL9qiXDUz9v59N1yJlpcWgce8l2gLUYdx_8g6Ln3UUc_3b7zSJmTBl2sV40dPki56A5QXXWfVjjawE2qRjIBDMldva7G2aybGkEdzdlj-AcLyAJaU4__nmWuzf4Z4s4IOBpaiCefYE9Imya1zIgCHIrM3GWMITDUAZS6w5WdCsijSMcjoSjb0cNqHgydCJTLz0lKH3--bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/flLUyid90G1xBXinhgjt8dWFksXfYujDbndMVClXXSIFM_nYyjKioJBrrxyDOg8wf1QD66QZiwdn9Gt9DltdFMYmLYbObmCR5b9vVv-HxKjUF09aVB2oQS89PQEwsNm-IgqWOTeiQVe1N9ZoZG1Dk8FYRdkO6YlEwme5nfleC7F-Bx96Xw61lGsn99DPSjw0NtwFms0X4mC9SVz13yc_ZvkNmA1tdeZ2n3zFX5GCfZpYafG834oA0dMqyjiB1paZ7FmxePfi_B2tDBrRIqtlF6reSg6-iXC_klQp-1--sDrMXDa_PTkN5cbufQyBtuYUzwsFGKpRaJVJgHaspD-0ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sxYkbdbCPCj1g7gEZ6IzA8UbLdd3p2EhooBpE4AyomTkWqndO361DL7ykmhd1jdftXBhxBrA5ZaQGOkVmCEa1DJHlPROFs3fpRgstCvVytTzMvft4g1b4vM0KuoNgPo7hkiotzfIXgS4CAdU8jCpy4MuMyZtN4Ews8Hbh9HoQxcg_nthx79dXxyfN8TTX1Sk5mQEG6KyqGIJgDKsq-X16EB1GIZChBUi09iZbsc4eyGhWSk8ytaN-zOuHkoBVFjHyGQilW_ic6Hf9Zo09mw5z_IwhfXuy88ngyDGVA27F7RWYcNmZZCvFKHZaoGPpXV0GZ52pOVG6_ZNqipvotwEdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJTrm4KRV53o887_cCeW6j5BS0mekp5EQhZyg8xSLlpvKBw6nVxrRzBz1wPbbKqujISu7xsWfWc_Z_DzjYulHpZSmRdq_vjr29y3T34mQVvZR0Cp8FlIxKi7tkLdC8uOwCMojl62_QuMFr8ZvvB5zMyCtLwqfROt-4tSN7Z5Ty8UoRtmntiC2BdLHDON6tQA5YlToF7Yz2zEbuCABL6FdCPN3K12bWUl_HlWV7Ra25DvqzeALv0LBl3EzPaF0wjyGyDPWzH4bGt7fpvpOMsEdn0Hn2QP1pi6_-qxH0BzZ4ioKg8bxB6Uud1n7rWHH67nK_h-Dp1YKycE6ek-usJXEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bcw8u2tL03KGeb9B2gLtZ_bmLSpbQCnLs6033U0toljK1ydI6kR3WX5ryQwRxhg5i3EJSng1nXbLENvw97tzt9VcRZR7u5veTfeXNsrLfDMyDQ9Sn1TR2EiCvYHXMRYgPPfssPgMtRX11q4B-O4cPUC2VH8pP9KvzyURiCDqJgPRvA8NwAK1EgPYag6_Z8QSl9Yt1gz1U950Bp7Z75CeZaAEunIlVEqa2LVD2gD08u9ISKu3ws_imHks-nGK5eZp6NIfVfupHJ5uxNHY0rliZng_xql43_aSaH9vs-BIijcREBg8w8-kXDdeyxY20HphpaITKfXzkPmzmM8_YwcNzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JrK-A4zbOc4hWEn2qBoqPbaTRtQqZz-o0Q0SmS5obulUT_e_dR1iHnX9ZtEbJMF6D5vIrPVSbgnDE9bpEPc8WA6t-WJc0TcouK2zbYmN8Xm_V7_VJbJJKHjPsJIqY2SWZwXhd5xuE6t15e77Q4qMO-bKH8Rk1ixib-JwTP2uEuHBpats5sJ9TH9RsOrfjKBoheWjapWJZsjm8jAKchsmpZF0O6IJbyKLaqsJRA29-CZolyxuWC8Qa-ImqvgQwHUONjXPQmB8_MX3Ef8w0TLPr7GoMe8u988mt-jDav_bdDR7ezgfjcygmbqXxBFSZGs3H-XISXIh9GOCSKXETHI1uA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مراسم تشییع پیکر رهبر شهید در شهر قم از دید لنز خبرفوری
🔹
عکاس: فهیمه فرخی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/667837" target="_blank">📅 12:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667836">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/209d04c63a.mp4?token=NC32yu42cCWSb5pjrKkNlBfXT302y8IZQltU5MLE96R7iIyoOI4FszSx2pood7VlzAZG9y1d5k-EMh5z1-ZjAL0yXegcRZDzxB0Dqf2k4bE4r4AXYyvaJsXSadkmILHhxcbzAyBtUMr_DrKlm--CtN8OFEoEc9a7Jne0dVYrMKgpXy2JUsKkEUvvIbdF9z5ORIA96bDVmhxjwoZ_1i31eec_TZx2G6apFU1pP0mWszPehREFnpQ1kgWmprWgEzuHHiFbPsPDXdRfocqVzZTZYLNmnQlUivXIqRa8U_ajzwkR2O4YcBCVAQqKH9dOfBWHiqKBNFiXRA3P4CAxPDFY8Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/209d04c63a.mp4?token=NC32yu42cCWSb5pjrKkNlBfXT302y8IZQltU5MLE96R7iIyoOI4FszSx2pood7VlzAZG9y1d5k-EMh5z1-ZjAL0yXegcRZDzxB0Dqf2k4bE4r4AXYyvaJsXSadkmILHhxcbzAyBtUMr_DrKlm--CtN8OFEoEc9a7Jne0dVYrMKgpXy2JUsKkEUvvIbdF9z5ORIA96bDVmhxjwoZ_1i31eec_TZx2G6apFU1pP0mWszPehREFnpQ1kgWmprWgEzuHHiFbPsPDXdRfocqVzZTZYLNmnQlUivXIqRa8U_ajzwkR2O4YcBCVAQqKH9dOfBWHiqKBNFiXRA3P4CAxPDFY8Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینجا ایران نیست، اسپانیا است
🔹
در جشن سنتی سن‌فرمین در پامپلونا، تصویری با شعار «اسرائیل را نابود کنید» مورد توجه رسانه‌ها قرار گرفته‌است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/667836" target="_blank">📅 12:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667835">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edVQxzv9X7cxTPr4ztYfhA_eAErHdk_edtP1QvlAcqRATT2a8oB7rK6g6nd43yP63RmZUFuzYKNfPiqBYKgZf6iw84DTV4_PTsWLrX3JW7sQt_UwDtvs-7LU6ca9ph9FaHntGlAJruubzfl1pkELv7LcYo5f77jEGN7aqGV6BkP_8_6AzH5uFaHO4Kx1UvQeuJi_ZSU48ugdd7dH7k4orGrbsEypWRdzVgpoEYo-slFjfh3g3Q0JxZCMDhnaaqxOqePEXuftyXnzPvDr4UoW0a7grTvPqkhKeyQDl67cQ5yhItQzkHXQZUPdx0fhcTxOruJc66nFhcmKmkADK_L4AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مراسم تشییع رهبر شهید در قم به پایان رسید
🔹
مراسم تشییع باشکوه و تاریخی رهبر شهید انقلاب آیت الله العظمی سید علی خامنه‌ای در شهر مقدس قم به پایان رسید.
🔹
قرار است پیکر مطهر رهبر شهید انقلاب و خانواده شهید ایشان فردا در کشور عراق تشییع شود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/667835" target="_blank">📅 12:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667834">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b13eef82e5.mp4?token=Wqh8Fb0YgBifVVaqpeIvaeoP7M-ffdC6C37C2Mil6KKxAy68dpDsnc5yKn0mSgZsa-b73_xhCThPp3Qz0PM1WuYp5O5TmZ760-CPxhXepe3qiCmb1Mw6cyKmXvW36tvnyoCn3wQLgZReuq_x-2XiR8z61Ny5jqupPluftD9Xqnz15KGBd5fkPEmYJ8pHTRgEVt9lvyYc4d5AjmdBwZZ_mu3A98f8ZQ1PXXILczhox2XeBCoocYL_h2HGelExxWfKeB60KQO9PWMa5ukMD60l1pTNOzY0Y0_icHFvXbixpBlefHxCD3b1KOatH4vaxELAiNcQUHUD9VwiZYJoCBFPwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b13eef82e5.mp4?token=Wqh8Fb0YgBifVVaqpeIvaeoP7M-ffdC6C37C2Mil6KKxAy68dpDsnc5yKn0mSgZsa-b73_xhCThPp3Qz0PM1WuYp5O5TmZ760-CPxhXepe3qiCmb1Mw6cyKmXvW36tvnyoCn3wQLgZReuq_x-2XiR8z61Ny5jqupPluftD9Xqnz15KGBd5fkPEmYJ8pHTRgEVt9lvyYc4d5AjmdBwZZ_mu3A98f8ZQ1PXXILczhox2XeBCoocYL_h2HGelExxWfKeB60KQO9PWMa5ukMD60l1pTNOzY0Y0_icHFvXbixpBlefHxCD3b1KOatH4vaxELAiNcQUHUD9VwiZYJoCBFPwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بدرقه باشکوه خیل عظیم عاشقان آقای شهید ایران در قم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/667834" target="_blank">📅 12:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667833">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
پمپئو: انتخاب چهارم جولای برای تشییع، عمدی بود
ادعای مایک پمپئو، وزیر اسبق امور خارجه آمریکا در گفتگو با فاکس‌نیوز:
🔹
حکومت ایران عمدا چهارم جولای، همزمان با روز استقلال آمریکا را برای برگزاری مراسم تشییع آیت‌الله خامنه‌ای انتخاب کرد تا نفرت خود را از هر آنچه آمریکا نماینده آن است، نشان دهد.
🔹
ایران قصد داشته پیام دشمنی خود با ایالات متحده و ارزش‌های مورد ادعای این کشور را به نمایش بگذارد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/667833" target="_blank">📅 12:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667832">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8d6fe01e.mp4?token=GKFQ52puWIDComYtklo3Rh1hdUflPg4v2xEgCWWk_pRJ6Ok1tzPeGRoanfgaBBwQwWB2RggZNzTqfNs9oVhquopGHI4EiJwuM9ouXmqdApja5e9_aQKxDGZVNtkMKYcOk4eyJs5wg-qa-aF3eS0gQpKEitb6QToD4D8agANgO_OIAWQvyGxyiwsGMcuHUeCikG6H5r-RQ0vMMlXpA5iB6P-DaT83dPIRDLloj5AGU7lf3ji1ANedtsuwPkJymexhWPrNtlvnpdwc1yFk2E7k-DQ_5lsdcGj6CLWnVnjVmymIjbo8ceP8JohEViIwiDWD7430XEX9Qk-EUvtrT7IpYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8d6fe01e.mp4?token=GKFQ52puWIDComYtklo3Rh1hdUflPg4v2xEgCWWk_pRJ6Ok1tzPeGRoanfgaBBwQwWB2RggZNzTqfNs9oVhquopGHI4EiJwuM9ouXmqdApja5e9_aQKxDGZVNtkMKYcOk4eyJs5wg-qa-aF3eS0gQpKEitb6QToD4D8agANgO_OIAWQvyGxyiwsGMcuHUeCikG6H5r-RQ0vMMlXpA5iB6P-DaT83dPIRDLloj5AGU7lf3ji1ANedtsuwPkJymexhWPrNtlvnpdwc1yFk2E7k-DQ_5lsdcGj6CLWnVnjVmymIjbo8ceP8JohEViIwiDWD7430XEX9Qk-EUvtrT7IpYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فضاسازی کربلا در آستانه تشییع رهبر شهید انقلاب
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/667832" target="_blank">📅 12:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667831">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5951235a1.mp4?token=pbVoWdqgcwSoKmr4A-sPx0v6ycCExx6WyNfC_G8_F72VmlGFjBK8TAfrVWeOooHXn42yUp-LIyDUuVKp_fxzylYua8Aiotosn_3-nT4DoEahFVkzX6PadlSHEVtZjqaUnITaEK0UyVh9BdTjGjduQgdXbzqZzVvO88KptpBGuc7euqKxuJfPGXpo1aGnrCTYsVyqcf5ZodBjXMXej9fzx6Pdu8jkthudaCL1XD3P5wLp_RSEfSIiAltvdT4GCRymSQGtKiEN2XsmIJSR2LYnMAT4swZNlrfRyfPZwE1a4J1XrnxNbZCyyt-2JWiG5bTkH_GTRqu8azKtKW2eMF1pzTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5951235a1.mp4?token=pbVoWdqgcwSoKmr4A-sPx0v6ycCExx6WyNfC_G8_F72VmlGFjBK8TAfrVWeOooHXn42yUp-LIyDUuVKp_fxzylYua8Aiotosn_3-nT4DoEahFVkzX6PadlSHEVtZjqaUnITaEK0UyVh9BdTjGjduQgdXbzqZzVvO88KptpBGuc7euqKxuJfPGXpo1aGnrCTYsVyqcf5ZodBjXMXej9fzx6Pdu8jkthudaCL1XD3P5wLp_RSEfSIiAltvdT4GCRymSQGtKiEN2XsmIJSR2LYnMAT4swZNlrfRyfPZwE1a4J1XrnxNbZCyyt-2JWiG5bTkH_GTRqu8azKtKW2eMF1pzTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خالی کردن دل مردم جرم است ...
@TV_Fori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/667831" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667830">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🏆
روزگار سیاه آمریکای حذف شده باوجود رانت «کاخ سفید»/ شیاطین سرخ مقتدرانه به یک‌چهارم رسیدند
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/667830" target="_blank">📅 12:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667827">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70352bb00.mp4?token=GjTQ8A7SjU3pI94gJ5TGo1nGx0BWExXua0qlp7h-z4hN0is5yEOQBYTxd98h_1j9Q86g6XRWutVmT6ClbAhRr8gPdP951YMYyEpXRPWmvNJZYg03DcIDQ0Nwq-JI6YKZEN-Lft3UCsbzhJbryIK4EysY0U4TdWb4Fk209vGQ0SFkEvKOeo7mtayFZ2dn7fi9GKHPxbhWYAfcuAoqrkIqRisK0iy57cishaxXu6wGZ11QGoAT8yq8tPR0imlFM5noU3ZKD36ez_Qxcy0kZon7cPopNr5T1-rnfHNHihtvZ8DAfaHr0c4w7Syyv4PzVYZv5jqY865pO0sXOOcMQxXCpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70352bb00.mp4?token=GjTQ8A7SjU3pI94gJ5TGo1nGx0BWExXua0qlp7h-z4hN0is5yEOQBYTxd98h_1j9Q86g6XRWutVmT6ClbAhRr8gPdP951YMYyEpXRPWmvNJZYg03DcIDQ0Nwq-JI6YKZEN-Lft3UCsbzhJbryIK4EysY0U4TdWb4Fk209vGQ0SFkEvKOeo7mtayFZ2dn7fi9GKHPxbhWYAfcuAoqrkIqRisK0iy57cishaxXu6wGZ11QGoAT8yq8tPR0imlFM5noU3ZKD36ez_Qxcy0kZon7cPopNr5T1-rnfHNHihtvZ8DAfaHr0c4w7Syyv4PzVYZv5jqY865pO0sXOOcMQxXCpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیت‌الله فاضل لنکرانی: خونخواهی امام شهید حق مردم است
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/667827" target="_blank">📅 12:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667826">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdZ2F-1HWMeeYgGu4V-YUkQn5v01c2BifZ5T9eMXPtm4UvL_3siCTo0__xXzKUXGdQ8JmXjuPQGy3p9WEeVpP0dvU34vFCYqpp8DXAwBiMpOQNBGVD39KjDoQ5-uxc0nY4kDd_TODOfaOVX_978Q2C84QusRYmAPWWCGundVq38fPrw75hXQZV8ElSIaQIU3Ny9y7tnFKZqATKjymnuU2_yqhPIThlrR-GuhERev5Uldjq07-8nc3lh4gTPie3eyGo6myzBXPWA0-LAdu767bYE0K9RPhag4THGPLC4Qc6owOGWjpUyNVGdUV6rIKl8TAV8nfD5K1exwfhBGHwA_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص بورس تهران با رشد ۱۲۲ هزار واحدی، برای نخستین بار وارد کانال ۵.۳ میلیون واحد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/667826" target="_blank">📅 11:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667825">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
خروج خودروی حامل پیکر رهبر شهید با بدرقه مردم از بلوار پیامبراعظم قم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/667825" target="_blank">📅 11:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667824">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rgpwtn-pmVt3pEaFtaIFDeavRGslRsqIet4bvwZcXKaHZLggiGbPJ6rjxYDEI1A_o269idtwHqVl8QKoZ1Al4LeNGgnwTZ0u9jS87n-kSEIRts02j1wfTTtmcA8Y4Fo1JHzxzxL3R4qbrQqrmROJDRf-LV3oJnP8DRlppMh-xSqP3IGGNXCoEJnO7xwCZfcYqdnPPgL-rNZ-xh0Ofn4qivhBk1UcPuqaw2MJTy9JOXxffsUZTEyZoJ6yoHJlkqUoEp0yv8OzGTMnUyFfZFiYGnlYHsf2L4xNzkNZi28nPzlUatENK7SrZkQp-xO9SZEJiCR24B1OOJhYMeFVWqTSqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قدردانی مشاور وزیر امور اقتصادی و دارایی ازخدمات رسانی موکب بانک توسعه صادرات ایران
🔹
حجت الاسلام و المسلمین ثقفی مشاور وزیر امور اقتصادی و دارایی در امور ایثارگران با حضور در موکب بانک توسعه صادرات ایران، از اقدامات و خدمات ارائه‌شده به زائران و شرکت‌کنندگان در مراسم قدردانی کرد و مراتب تقدیر و تشکر وزیر امور اقتصادی و دارایی را نیز به مدیران و کارکنان بانک ابلاغ کرد.
🔹
وی با ابلاغ پیام قدردانی وزیر امور اقتصادی و دارایی، خدمت‌رسانی صادقانه و حضور داوطلبانه کارکنان بانک در این اقدام فرهنگی و معنوی را ارزشمند توصیف کرد و از مشارکت موثر بانک توسعه صادرات ایران در اجرای این برنامه قدردانی نمود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/667824" target="_blank">📅 11:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667823">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LB21e9RmURxeRLL0RsqMIXEdzSybrRK7lL18PtcyA4MVTp-2kNjGBVYP_XTPNIN6lXOllejuG5Z5n04SDuE2R0LDzVt3m7zFwtchBsf1Awudoeq2q74UTBrO5js5svqWPw21qFDqU8QQaOJap8VYqTbinykxs5TaE2gXxyEozFXZan1g_2i6NAzjNjcZ6tTuH4ItCtd91UJU258TI1Zu5Bt3V9mIi3qhLU04pYMyFiqqjshbKaJrvcm9oPaBG8RqHoZ8E1YKzG8R8BzsBzRL-iKcNWrsjLAKyE59QfGdM8f4CXat0lKs-MX9-8q392fkumR_e5q3mPfKEymXTA_VHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/akhbarefori/667823" target="_blank">📅 11:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667818">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qZJbfGXY3zJqU6gMbkkrlByUJK6qcqjvlHaSA7pZ94t91uTJUAXcICGiY_Phd13PAJoJaW8y6jAoW7rGQLVy0ibb-C3xmPMJavcj5yVaz2rMFzG01aaErXNtTIBcoyhSzjs_hTQwuPi6lTlKyIg609Da4Rq98d1yVwZCpOEtjPbLs8frTt0718w8s9FVC2nTAiEuHNpJYSHfYKtCAmTO3456YYIrForCYv9svq89Kg_4AkPq8IK4QjLOnsz08T26_de1-k4W6mPVr2_f-b8Ue52ARfgGPeiZsktmRUbonqhtedk2ZAmuov6u6VtCnMxG4aH7SmY-hqwgE4Enx39_qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LoiVmYj1OWrueNogn_FSM1Kwyy4lzSS3bQbtYsFZGH6fRn6GAUUZ8J1xjBRRqcUfIpEF1s8IDN_YB3wpWQz5ivSssnwa0kjvs8IQaet5DVqJ88dKQgOjVnPfVcRyncCFoxXBQ7wkYJhwLBB8BadkGIsF9mzUCXpZvoHW6dt8jFI9AjKpL3UyjTsoMO1h7cJ3jvdTKX8Pa7wi4F7BWY-aCs5rbwC9vFkxf-AroZTdRkvbs6jJc-6kldkUWLj20s2eFddiEoHwGemnIEWsM_8_D27GptGICVdKJvhVrI8Q_XpjyhdgV6ixBeirD5N3RVwcVfLlYxt60CoIbHgrLa2Nfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CbxSKuT7nV5eUW821tWZPO4ePwEV9-VHsBZXZXufnVflKeUoiQFARWYSH-MU4IiuKJ81nWcAd5aQV281d9oeVtLiglHLiVjsPDQTJoc4ZPUm0xBA_FqPWMUCLTueJojWkWdNK07zElJXDp7mXQqeTj0Y2K26lB3Usq_0s-DYCOqRpIdbmrllHehR35R2czSeTOY-F5mf92plxTS3kCgq0s4u3rZ5ByrvEoUDeocP2Wwg_uy4YPMO5piU6bsomrjMKKEdyXHSm8yeN60XV4J1aCYg7rHxuYBP_3WKsugR3uFem-uZau2UTJYMpaXNbPlCBArv3F-PqiqIOkj4mvqoEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mMqHr_g3GAhfJqpaY8RX2OgZ--f1YlV8AbHcvTTE6yJuesruZP6bujPTYxVWzIphdo2vqQ6orh8Q_w9RXYva4csGw_lVQNAYrCi_IL2tOwnE6fJsETRNH2MFjEfFOAAtwuTTWpCG086L37AOUKOHjWe7Zzdm-H4XPXSIt8iGCOdbDCdIT69KU6nmP0OX8BeCca0W30iZe81zD2_mH9sz3sMsu3AxPHPqQNljWFdb5PFEcNBBBauplvQ6tsjYRqyAqwxcAzF7KJIRP_hiTf0Rj_ra6pu4EKQ9XPoPhYcpbS_q42fu63wdFp5zU550-4P1KiV7tobEM8QQNdCVvb85Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/co5BOhG5f3zNCv5eEZYCQXnkqtvNMrdTRoBL-J68LrfAjZIT_53NbeShY7GfgHaBWGK6wKird4V7Qs8CsPn0dcg6uqqInEHk9U7L0GQL9w3gCRH-gzGLvw_aPqjVwkHyXORBF-P0-SHp7uNOYLsZ1vuRiGEAF_yJ3XM-TdNuromCXv5kZt21r83_Mf9_bbAtA-m_s2xLH5fDyWvC7Bq7r0BhkKmGkJayt77y7LGCPOrbYtvOve9Rbak-p7vn8eJudfNXKF2f3CchvWvPyWlhossNfGowXZVcXFyY9vK2Y-fOLex-FpQVbu2PcIHkms8WvCtjPttQlMp3H4IKfw1deg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نجف مهیای میزبانی از قائد شهید امت می‌شود
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/667818" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667817">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دریافت کارت ورود به جلسه امتحانات نهایی ۱۴۰۵ از امروز آغاز شد.
🔹
۹ نیروی پلیس در حمله مسلحانه در بلوچستان پاکستان کشته شدند.
🔹
طوفان با سرعت ۱۰۸ کیلومتر بر ساعت زابل را درنوردید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/667817" target="_blank">📅 11:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667816">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسازمان راهداری و حمل و نقل جاده ای</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a8d0bb6a8.mp4?token=rvsqkQYLtIsA9Vi_ueMxr-QBdoc8EUyQz3xdNLSQy1z0hvPij_zMW9ukI-jRiyKnvEznW35_tVGg9W9b2YAah63SKn_l6ZyWn9ITyfkprjmR1VutoZFiP_99NLhjyu3d5x1am_I8rbeoFHIDG1TCx0QpR_Fp10zSEVPz_gf4BH0OEoNSXLkqe1iz0RgsNBPwTRmmmEGwSJ2sJzAWMXxO6AaTIZv-Sm3uyDUGaiEpiadK2vibRIFGUdbWMwiHdploA_8Uy-WOn--sgXvCB3k3PRh407kJx-xf3ko6hpZPvC3CTNLxT8H8Henf54C9JhFF7WNY2Q81F2xsyeevIbjML5Ahreegj__n907vUKxFpCMcRTIcMQqOaM6qjLCt1sXIqKiKJ1RsyPpj2yfuUMuC9r2Z1RzAOC6pLyQ9GDsmO8Cx9W28wJkHRrYc7ZSOSgRH6gZUmG5cUYHilRMCl3_w3rsF2dKueG7U5qGLP1fNdTypP7XBXLxWKa10P5NO56hqOB8ZcL8RfNY3BYQk_17Z3Lah4ay1dHssG_CL9YfMwue5S2pf-XLc2pi3A7AtWSx2jCl48LiRN0d1JqViDx_w4WJH2MwCc5cLGwwA_RmF6e9yVs2qn9KpZ68WCLQxE9CNxkB4_agyBesl1znLGm7jjLCZzwdk3SM3O434Zl4_wwI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a8d0bb6a8.mp4?token=rvsqkQYLtIsA9Vi_ueMxr-QBdoc8EUyQz3xdNLSQy1z0hvPij_zMW9ukI-jRiyKnvEznW35_tVGg9W9b2YAah63SKn_l6ZyWn9ITyfkprjmR1VutoZFiP_99NLhjyu3d5x1am_I8rbeoFHIDG1TCx0QpR_Fp10zSEVPz_gf4BH0OEoNSXLkqe1iz0RgsNBPwTRmmmEGwSJ2sJzAWMXxO6AaTIZv-Sm3uyDUGaiEpiadK2vibRIFGUdbWMwiHdploA_8Uy-WOn--sgXvCB3k3PRh407kJx-xf3ko6hpZPvC3CTNLxT8H8Henf54C9JhFF7WNY2Q81F2xsyeevIbjML5Ahreegj__n907vUKxFpCMcRTIcMQqOaM6qjLCt1sXIqKiKJ1RsyPpj2yfuUMuC9r2Z1RzAOC6pLyQ9GDsmO8Cx9W28wJkHRrYc7ZSOSgRH6gZUmG5cUYHilRMCl3_w3rsF2dKueG7U5qGLP1fNdTypP7XBXLxWKa10P5NO56hqOB8ZcL8RfNY3BYQk_17Z3Lah4ay1dHssG_CL9YfMwue5S2pf-XLc2pi3A7AtWSx2jCl48LiRN0d1JqViDx_w4WJH2MwCc5cLGwwA_RmF6e9yVs2qn9KpZ68WCLQxE9CNxkB4_agyBesl1znLGm7jjLCZzwdk3SM3O434Zl4_wwI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
پیش‌فروش بلیت و برنامه‌ریزی منظم سفرهای ناوگان حمل‌ونقل عمومی جابه‌جایی شرکت‌کنندگان در مراسم تشییع قائد شهید امت
‌
🔹
معاون وزیر راه و شهرسازی و رئیس سازمان راهداری و حمل‌ونقل جاده‌ای با قدردانی از حضور میلیونی هموطنان در مراسم وداع و تشییع قائد شهید امت در شهر تهران، گفت: با توجه به پیش‌فروش بلیت و برنامه‌ریزی سفرها از سوی عزاداران، آرامش در سفرهای بازگشت در پایانه‌های مسافربری تهران برقرار است.
‌
🔹
رضا اکبری افزود: پیش‌فروش بلیت در سفرهای رفت و برگشت و تامین ناوگان مورد نیاز از سوی شرکت‌های فعال در حوزه حمل‌ونقل عمومی مسافری، موجب شد سفرهای هموطنان در شهر تهران به صورت برنامه‌ریزی شده صورت گرفت.
‌
🔹
وی ابراز امیدواری کرد با تهیه بلیت سفرهای بازگشت شرکت‌کنندگان در مراسم تشییع رهبر شهید انقلاب اسلامی در شهرهای قم و مشهد، شاهد بازگشت مدیریت‌شده و همراه با آرامش هموطنان به مبادی اولیه سفرها باشیم.
‌
#چشم_به_راهیم
#باید_برخاست
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
@cheshm_be_rahim
🌐
rmto.ir
🌐
141.ir
🌐
https://ble.ir/141_bot</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/667816" target="_blank">📅 11:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667815">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🏆
تیر دقیقه نودی به قلب کریستیانو برای وداع جام با رونالدو؛ اسپانیا به یک چهارم صعود کرد
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/667815" target="_blank">📅 11:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667814">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
عناوین و ضرایب دروس سوابق تحصیلی در آزمون سراسری سال ۱۴۰۵
🔹
مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش عناوین و ضرایب دروس سوابق تحصیلی در آزمون سراسری سال ۱۴۰۵ را اعلام کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/667814" target="_blank">📅 11:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667813">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
برگزاری مراسم وداع با رهبر شهید ایران در تورنتو کانادا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/667813" target="_blank">📅 11:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667812">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ed2469d7.mp4?token=mZpDdRjSolkJMptlmHgFwEBaNnehKNd3sr3Yauzim28GnBKCaHoMoCbIR01UlzaEYimbi2h9o0dkMuqA1WSKhmTPd_loj1kd1gMx6uZI8XR-okGPSTgZ8am1pnmCzX-PHyyJjvM1CYYGwsyrXNLjUc201lNY7ZAv-5QXQrjihW9LIH8c_wLfHHpXDGwGeZcLsPTN_RSAjQGMsWHUddwXjMIRvQ2UCl2eexe87Of9R7hOmorPK0I5eSb_lXZDpzn77ea3maMGeyTpHzSYjprcarKvu9jfR5nrCSrodugIo4KB4tEybPm9gswvUOHU95Inm50aY7wIWBgwdr5eVOSFVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ed2469d7.mp4?token=mZpDdRjSolkJMptlmHgFwEBaNnehKNd3sr3Yauzim28GnBKCaHoMoCbIR01UlzaEYimbi2h9o0dkMuqA1WSKhmTPd_loj1kd1gMx6uZI8XR-okGPSTgZ8am1pnmCzX-PHyyJjvM1CYYGwsyrXNLjUc201lNY7ZAv-5QXQrjihW9LIH8c_wLfHHpXDGwGeZcLsPTN_RSAjQGMsWHUddwXjMIRvQ2UCl2eexe87Of9R7hOmorPK0I5eSb_lXZDpzn77ea3maMGeyTpHzSYjprcarKvu9jfR5nrCSrodugIo4KB4tEybPm9gswvUOHU95Inm50aY7wIWBgwdr5eVOSFVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلم کامل اقامه نماز بر پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان توسط حضرت آیت‌الله جوادی آملی در مسجد مقدس جمکران #بدرقه_یار  #اخبار_قم در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/667812" target="_blank">📅 11:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667811">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
رویترز: انفجار بمب در نزدیکی هتل محل اقامت ماکرون در دمشق  رویترز به نقل از یک منبع امنیتی:
🔹
چندین بمب دست‌ساز در نزدیکی هتلی که امانوئل ماکرون در دمشق در آن اقامت دارد، منفجر شده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/667811" target="_blank">📅 11:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667801">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJOqrRAfx_jmIEnbZaI1Nfmrto8y_R5KcJmBU9aZ2EkO_7zTUtEpI0d8wOEc-0VNIVTJ5y8NsUB0K5MkXjzuZz7wj4UKYEM9usUoRxE6kM9NGQhxgaujCBuEqZRHsJK_R7RyFMp7BU1PAq_ZdKYMSVMVv1yRmoJ_roEWv_0s7v4ss370AtWwA2tBowme-6BtobvVlyuL7U8IBv2z_S_86fJMyPVyjSdWQ8KaJ-e-6IOHYrXfr7xAfVop84ga2Esdelc63ULUeDWeqcKpAhZRdkyWE0oGPpTHSFPg7EaX2Vgx-io1zZWYPAWW1VclEADEY_S5tIvTbLXdDHzW-_zeGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VADYvbrqUI2fx8iIH__juc9jeI4168EJxSWTiX4nHRxWIgy-m1qV9U1oMe1EuDbeg9rdC-Rgsnq96lBWzOdFZGkCAml0mp-j5LYVESqLbO8ce9JJFKpibAFoe4L-dyF5nDQ_62PBYNPWiMP-igQdFRpWqDDUiXuLrnAL6x1THfda_JMAbtf8NpUuv6ynovSeWLsEliG5ry_6CCOfMS5Jw18ca5y08Ws7hedVrdBJDTR_YUE3OdIf8MaP2anOWml3U-yMFavKu0-ZWt8qHLVB0rX7niUmPfxWNE2lW6iWHVF9s-AatCtJHQTST9chLSV2Y4fGTfgaVbor01sQEIhJ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mrkwe6HL3kYGB_lObYiKry4MsL37xU3Nc4DpK0sBMmZAQigOc-a9SoUuQFPaBArbuek8uN6dJEeCPofc02G2lxktAVGKBxmMrye8tOHqHIPQjP_Ogf21inkQeRSluySIugct6kM_nMqjizeecxEVLsGPRO7BSYV2Fr0px3vYFf5zHdXSWKA3IYR4yXua4xkjrHJ6439vSItqAsV_rdHiOXs6Emayn0IoCoBeqWs2-0ZdeOA-uUxXsQlctrRIoRd65mwnOXyuDlktIop-NeFyCG9SsUYa9GX5WlbaqlAjnN2IvPe5nu1ic7IKaOMFAAWzWzFsN6tDYVFgUNSRHsB8Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BIjrvx6FidZDdldrMG_Rq43EBfOpExXWB3kI5OUmOHbewH250Qna5hMk4uE-lyeOuFD1GTXHYp9wVEsH36RzK-lyiTayHmHhqz9cygHbecUSiZJjVL-1bdnWT8NlN7thpisSA8fSLiKscpJ8ikHrc2wuSKIZHV5_V-goegFWU-913718_Jz5e6nLlQgQXMZ-Dt_-HmCWJ4j12mYnTF3JxeIrj2_RKOtARImwxV6W0FK1fu2ftRutitypryC-Aa881hTFGwllZHnoEVqJ88VscjhFBmpUclRfUpyz6vWTz4VdIPy-eucRECwChz-A3kgXzgad2IxMkfUBscFNNIf3TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dsBsGszyRNRW2evQ-UQZ07dXpTkxqJUoRi4sAvquKfkg248ZP-wYs4c3e5dKFR9Ios3vB9Nkb4rHW8CTzjfBfN3DXsKsvXma-CPdICmEYjc1ZwoPayWpFGBcuv3tFR059-Yw3gxATJ0Xxwb64E4Rb5VdjGXLeE4B9l3IZYHxT_96x114HIR3H8SlgVtFwE5SNRS-fhW928PweoJntSkLsL7X7zK33hZUNRjdeZtf-61A-G1P_18khz4Tpk67uMEdJ7KF0bI4SCZuCQon0fPX7wMsaigxm4BOfaV2zVy_16FmiZPNmw72SITV0v6xyS4SnZl2NhhKLPO-P9o4uIGr_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DT9rTgH3Nj8XI1UZoxqRR7AWQ0pWEDfOkX_qzSemnumFV59GcGhMnj4Vgr6NdSP__IE4hkDJM5lRc1SvSsRA8QO5a4MwFm2LFXKyDzzxzrYue5D9FHGqQqV8waiMIGOZ6RlA1T-Pea2wt_72Zp0utnFbPqC4zvUsoXhBxmKImNNgVo5_6bb09NbFjMvL9fHaYqInIEbWZNDg2w7oleCFlmvU63U0qbH3GbMNAjyJAnCVg76cDsVl1TZV2RnHGCA4ez1RXLb89Ap-Jt-U72LS-no1sUOvz1xMWJ1sMyOvLhbgtp-FDZxZdBYT_HOwR_PvD64V3DbmnoUalatT_XBQfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmJKDFYoZi5pUOi-yZEAOokfL7ur-32gh_Bm6B0VQM-J6K5v7oIu0_RJAF2FfXEPZFEFGnNsqJLgu0R61fXpkTHI8aNnY5RUQJXJ8CtFYBXT1rbRcr5dyGwCeuATPbvoIOrgqKFSaNcYaoy0EzH5Fn8GsHQqAW9eEIjrKZwR5dYiQTlcZz_b9If6eSTMl-5llrccBgSfRbw_gHqAtV-MFFwStk5ZXEkmpqvIQ6UJR9i6Hdp59J7hLBq0ksfrtyIk_O6V9HEmk3-UqYX6spYH6a-i1y1s1DwzcTHPfunftFu_BcIcJVLEoFet5MzR83VSUlpjuDZ5Uz36sg7ZeQoucA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZoVVhSjA3JW10z4tLHpxk5bvwDW7odxrNNPfc-8yzhbguvWz6oPZpW3QuZgzwBPmMBFczp5xWOi3DPJNddkUtyBq7UgY5_bG3HFoa0ZgXeMar1rzMzCfKRM7cbfhixqEfLnvPZJB4SvWUSnjCCIkKY_SsxKE31o7gaffITwV4eytn3ubwdQ2mQpAg_tF86wdCso46JC1VmJsHAvqtirbbIdeuJQ2hg49Lqk9_a8ih18IzzZCvP5rDnGhtTTPDE4Rdjyql0UN3QTHtAiwTblCsMVy2hXLOMVBC6Z85jarr9L1lAdaYPaFzFIs_x5mRsBaoOdcJH0-0iP55Af7rTTYRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v-0Rl_6dbCHDfyl_mmWwPK1MRJEnlDY_Bg1gT5oNHhTxTBKJRX1mkCEKT3DWZK_MxsnU9Ty_IkZR-giwcsFOcgZANJKHMF49b-DO1x7vYiKKtBBMaMt8oKJEr_RCFxg0kbrNgT96xg-6c35_cNG_fz_wOi5n8aJIX4DdrHKN7xlEur5eZ9cwWNAKYa5nu-3-zAxBZgaS5fnXISwyalzTuwqB37fc1aNNr1Zsesg0zl1S6wzczNX39_acTbyb6j4hKn78diSIh9sRb6HWKYrK6UquHyRPjBqTFtcpT_nwbqKohIKKgwjKsnjxcTCq2Tw8SI1ZdTgWtNnjy2X4KQ4mMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xi9qm2DXSjd17SHEpe7OgMQN-3Puphxxg4dPwpR8SJClZbqyRuoCIDCD8D1ydaiDW8O0sMX8r8lwZK498k4xSGe-gqczCw0cjd4c4C3Uby5IfKg2tUM862opNIwNGO11H6EqugdvikO4olLOPgj3l6_OThQtWtDPuwiO0O_ZGecTrCvKQSCk5yyt_DNh8SUs0aI2jimq0jD1droShPprpafSqxYdwUzIQty3-apFD06yFjyKi78664TfwD1T8y2RGArYcbh_BHf7HwoznyPRE5x6ZPnjFweVfS94PSz7b3Gi-JGKS1AQYlPP6KXdGTiLK3bViWTcUIPRBAGh4P6spA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از اقامه نماز بر پیکر رهبر شهید انقلاب در مسجد مقدس جمکران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/667801" target="_blank">📅 11:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667798">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bae6665157.mp4?token=muqbMAB5Be0BKC51EZYqhzEl0nopzgHwzHoMl6epwgNQYkOtCKOQEHSm11EX-87MjiFh_wOIF5rI9bX_ztma3a2-Gtb67Qdz3zEfVQRU4-bqZRXjwim-GdH34RloXQUTRIjLBNi28Tbq98LDzekKfu5Gx6cNsM36PuspRMvVPfTWwzhdpgjZ1o-zRtJVXIEgpUUtDbBLvhezxobL_Kz20pIDS-mmVhVipa0E3GZN0FN5wx_jEzAJpGec9-FtQ3FFtLDOoGkbtkF1zNigeKeekcp3tMo2G4HoazBCmKb5M3ZXRXODrz4I0rPK-vO0ZeyR7Dv2H-a5FeMOzASHEINttg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bae6665157.mp4?token=muqbMAB5Be0BKC51EZYqhzEl0nopzgHwzHoMl6epwgNQYkOtCKOQEHSm11EX-87MjiFh_wOIF5rI9bX_ztma3a2-Gtb67Qdz3zEfVQRU4-bqZRXjwim-GdH34RloXQUTRIjLBNi28Tbq98LDzekKfu5Gx6cNsM36PuspRMvVPfTWwzhdpgjZ1o-zRtJVXIEgpUUtDbBLvhezxobL_Kz20pIDS-mmVhVipa0E3GZN0FN5wx_jEzAJpGec9-FtQ3FFtLDOoGkbtkF1zNigeKeekcp3tMo2G4HoazBCmKb5M3ZXRXODrz4I0rPK-vO0ZeyR7Dv2H-a5FeMOzASHEINttg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای غمناک قم در آخرین ساعات تشییع پیکر رهبر شهید انقلاب به روایت دوربین خبرفوری
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/667798" target="_blank">📅 11:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667797">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20d538d846.mp4?token=GVpqHk7Nu2UXOChmq6jsX_YRmR8XXw6phcd4Y8oeh1JJBX7bPJj8LIrT69ItZfufZA4thEw9TW-l13MwNlSMcElDQoVNCbGHyZVOmc-lmZILS0VpQFYES50mApW-KXCF4ArWLDwiiV-v-D2JDZhgaauPLZvDJf0zcdbLzhfzWN7qNONufTiSrl8M_7TrZJD61Nk5a5HR-MxHyI7tG_2wOTh2HphVhZqr5bh1PVVx1LUlbyxFKP6_J7IK7WvU09cPbzdD854-z_CW9BvO7vj9w9-eu-n8I8996xUYN9i3FIgqfiB7WbomTznsPBrpYsmZ1WqMIP0Ga27Fd6_3tu50UXwvX9vL_p8-hRNGn1zaJHIq5d8cZ_hbhjNZYC1DHAnqhHwdy-4gpxH4Orm7VhL0ipw_nm27MFyRKtJy8MOMNo1S4nlT8Y5QDgD_y-vlJA8rCj-z09urK6jlcLxQCqoNCaCZH9lqo5Ccw4RMWwsvZYvLuHJofF1-McE4FMIFKBce065LaRRnWF3DuZgIldH6dbMiekEhr8N52m5oIjLXdmN6vyRlKbcaq219dyiPcUjDirxHmfox1pxZKPtlKOlWAYmjfOBqCk9i2PIYacwzidnlbxnYI0BKn977KRnnb9XbDguotj-EQDNSXDwjUPq30YexogbX2lIeerLjsF-ygS4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20d538d846.mp4?token=GVpqHk7Nu2UXOChmq6jsX_YRmR8XXw6phcd4Y8oeh1JJBX7bPJj8LIrT69ItZfufZA4thEw9TW-l13MwNlSMcElDQoVNCbGHyZVOmc-lmZILS0VpQFYES50mApW-KXCF4ArWLDwiiV-v-D2JDZhgaauPLZvDJf0zcdbLzhfzWN7qNONufTiSrl8M_7TrZJD61Nk5a5HR-MxHyI7tG_2wOTh2HphVhZqr5bh1PVVx1LUlbyxFKP6_J7IK7WvU09cPbzdD854-z_CW9BvO7vj9w9-eu-n8I8996xUYN9i3FIgqfiB7WbomTznsPBrpYsmZ1WqMIP0Ga27Fd6_3tu50UXwvX9vL_p8-hRNGn1zaJHIq5d8cZ_hbhjNZYC1DHAnqhHwdy-4gpxH4Orm7VhL0ipw_nm27MFyRKtJy8MOMNo1S4nlT8Y5QDgD_y-vlJA8rCj-z09urK6jlcLxQCqoNCaCZH9lqo5Ccw4RMWwsvZYvLuHJofF1-McE4FMIFKBce065LaRRnWF3DuZgIldH6dbMiekEhr8N52m5oIjLXdmN6vyRlKbcaq219dyiPcUjDirxHmfox1pxZKPtlKOlWAYmjfOBqCk9i2PIYacwzidnlbxnYI0BKn977KRnnb9XbDguotj-EQDNSXDwjUPq30YexogbX2lIeerLjsF-ygS4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر کوهرنگی رهبر شهید انقلاب خطاب به رهبر انقلاب: تا آخرین قطره خون بر عهدی که بستیم هستیم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/667797" target="_blank">📅 11:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667796">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
انفجار خودرو در دمشق همزمان با سفر ماکرون
🔹
انفجار شدید یک خودرو در نزدیکی هتل «فورسیزن» دمشق و برخاستن ستون‌های دود از این محل، همزمان با سفر رئیس‌جمهور فرانسه به سوریه گزارش شده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/667796" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667795">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34ef7a3d27.mp4?token=USNiHrHDceL3VieJgHZgmaSTaeXN0dOxkVsAHto4swPjkNFs0GgyCYwugjTzkLyJ9naWFiFNYT8ka4dopTkv9bOrUed_R_4dEnc8YDy0ciq9Rm0DzEYUMSsqOQMIo4wmwHv-WWg2ZpieaQHBGNB4bTdDKm3nhfo8lZLZ8KGtyGzQHT9WPTJGNSud42s50MXyua63tl1ql7n5bcx8XCHLUR8JSeVC55Y4XxzVz6bAc1YI6qiCzn8OmDLn88xfv8yzzuoA7q4FtIyLBhA0ygzBzGGyxO_QM6a0mxgx4Y8Ksrnkn8bPPUPJgmDcgA-VVItH_sovJZHgIK0YHNeNQJjq6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34ef7a3d27.mp4?token=USNiHrHDceL3VieJgHZgmaSTaeXN0dOxkVsAHto4swPjkNFs0GgyCYwugjTzkLyJ9naWFiFNYT8ka4dopTkv9bOrUed_R_4dEnc8YDy0ciq9Rm0DzEYUMSsqOQMIo4wmwHv-WWg2ZpieaQHBGNB4bTdDKm3nhfo8lZLZ8KGtyGzQHT9WPTJGNSud42s50MXyua63tl1ql7n5bcx8XCHLUR8JSeVC55Y4XxzVz6bAc1YI6qiCzn8OmDLn88xfv8yzzuoA7q4FtIyLBhA0ygzBzGGyxO_QM6a0mxgx4Y8Ksrnkn8bPPUPJgmDcgA-VVItH_sovJZHgIK0YHNeNQJjq6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دومینو حذف میزبان‌ها تکمیل شد؛ گل چهارم بلژیک به آمریکا توسط لوکاکو
🇺🇸
1️⃣
🏆
4️⃣
🇧🇪
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/667795" target="_blank">📅 11:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667794">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9JQwnNZasI5X8FBi5xACQ9HdgsB8d-nVhVbstdIa6nAUAICsV6XBHq3LSDQA4Y18uPsI4F9_3VdzAbjiGyBhfDi3Jzp0eWfPt-e0dNV_aVtxjjoxTFRO4QoIrP0WhI90QLoPCOHJ9GHiuvhe8_Q5GPqnQXeqviQPzTO7c_d0l7fL2JXBMJf4h7GAbiof74ccXdunszfu9S3tfdrBmuNzXbsJzxPo_yrva7Xovn95rLWBHuC053xu8bUNdvEfWzQIaKtqE3gpqoIjlpSddVYSBykR44nwbn7mSB5LYRbxZ1T3B81N3-wpy2MeGaND8q8pCcagrOUXOsqt75DKsbvSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماکرون و ابومحمد الجولانی (احمد الشرع) در دمشق دیدار کردند
🔹
این اولین دیدار مقامات فرانسوی با رئسای جمهور سوریه است پس از ۱۸ سال.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/667794" target="_blank">📅 10:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667793">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9cqffsPNLomArlPwcKtF5F5wTqCQek_-vyMIYNUQPZL0ZogA-gJs-XDs1e2egOqGAS-tfaa81TJ5B9TgqtsuLLfF43No4Pcqhr5wEKkdTBStFifW_2feQuklyPxxq6uK34X_toBgR0RTANt7CUs3LHaz9O8fSHFgoTsdq6klX-xl18WMcnm9pKcGvWqhsvaZcs0DVeJliDVsRtVp0_ce1zAAZnm-KZfDD-7F33t2lzK7TZiTWo7czkOH9bkJan5eRHJ1C2ra11G_QfMaA-uhYpZZQHOp9_N8-_xdDEUh5Vq-55DMM244yDF9Jh19oBvZLz6yUUSGHkpPITvS2Rulg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وعده پاداش بزرگ برای اجرای حکم قصاص الهی
محسنی ثانی نماینده مجلس:
🔹
کمیسیون امنیت و سیاست خارجی مجلس طرحی را به تصویب رسانده و آماده ارائه به صحن مجلس کرده است که در آن، برای هر کسی که در اجرای حکم قصاص الهی نقش داشته باشد، پاداش نقدی بزرگ و قابل ملاحظه‌ای در نظر گرفته شده است/خبرفوری
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/667793" target="_blank">📅 10:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667792">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1B8lvmnFC5_hgOKgvkYT8GFuNcY8Fiq2r1j9mePzlt817DCWi75SUYb0cPaI-HDgZBKNj71MgMgMptChODE983pbex4eKcPzMHBpPMAc3UQPydIMIozvvb-wAo0706dCtdESIuKMFU4Xl4QyCsVDnNfuSLBU7yqo956AfNifto5rEfAfBb_Z8tsfU06Mw3jZ3zthRKPWr8leqYqqIoK6oCiyk7OMzt-RjfeVEeYZSUv1eooLSCfNmDnTZv6vHeDXIeoVhxpbyeEkWJZw_vzR-j956BCH5HxTPIq3_aJL4mt-pwvmJF55XDEnyuBxvkQkjnwLFMnKuEWRWfiGg8ITA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرچم فلسطین در دستان خاویر باردم(بازیگر اسپانیایی) در جام جهانی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/667792" target="_blank">📅 10:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667791">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21385ee290.mp4?token=TsWoXEJnE7tHuD0MC2USKSe95kKBA1knO8mZjDYDu4KfWY2QVUF5wEvLbvnRsOQzgK3h9L7E_pslDYgBQmKe3Q7uJqQIAkOzdEYSoJadj5TJf_N8WmeQfgGdDzzzJJIUVhCHhRimB0uqTbFK_r56q2PpJWjtN35IPYBhFYflZ9o92wLZp9ow8y1RmNWqXrhQ_fN5_PeA8Gi23HHJcIbYgt_fa2E19hdrFJvZxx5FFAxjwEeydTw34rLfFyKI06HQQRxr6bvvcs_NScLgxwHugB0M0KrNd7kkLkXAifQpS5LULyAkckR6CapXMAOTcSQhkWP9cllE-fjVBDn8ysMipQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21385ee290.mp4?token=TsWoXEJnE7tHuD0MC2USKSe95kKBA1knO8mZjDYDu4KfWY2QVUF5wEvLbvnRsOQzgK3h9L7E_pslDYgBQmKe3Q7uJqQIAkOzdEYSoJadj5TJf_N8WmeQfgGdDzzzJJIUVhCHhRimB0uqTbFK_r56q2PpJWjtN35IPYBhFYflZ9o92wLZp9ow8y1RmNWqXrhQ_fN5_PeA8Gi23HHJcIbYgt_fa2E19hdrFJvZxx5FFAxjwEeydTw34rLfFyKI06HQQRxr6bvvcs_NScLgxwHugB0M0KrNd7kkLkXAifQpS5LULyAkckR6CapXMAOTcSQhkWP9cllE-fjVBDn8ysMipQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم بلژیک به آمریکا توسط واناکن
🇺🇸
1️⃣
🏆
3️⃣
🇧🇪
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/667791" target="_blank">📅 10:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667790">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19e2400d94.mp4?token=acrTdYwzVP4a7ZAQHFkSt2kA-MTirxW27KQ_dqrGgVixikSSPTj4ro_tSKXgS69f_HjXdl7mjmzZTnDGWIPL_efcylDcgmbjhByGxgQUZ63Nqb8_F68KDE0l4xhNnnGT5c7ono4XPYAZnH5RDgmRWQ94HoQeBkiHUfT-FS-1FuSVDqrJtEjwZN18u_fU1s50oeCyrIcr87RNRLweXiPjJ_QA0zKhP7v2VpR-C99rdJnI4HFmTM0AyN_CPHrqEemq2mpCuJw1IZ6BPiuREJ87mCa4fgGKiq47z6eIEvQPMsdknym5DtnqOhdPQFEk3DBgS-ZEjfOZTR6vs0iQjQrY6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19e2400d94.mp4?token=acrTdYwzVP4a7ZAQHFkSt2kA-MTirxW27KQ_dqrGgVixikSSPTj4ro_tSKXgS69f_HjXdl7mjmzZTnDGWIPL_efcylDcgmbjhByGxgQUZ63Nqb8_F68KDE0l4xhNnnGT5c7ono4XPYAZnH5RDgmRWQ94HoQeBkiHUfT-FS-1FuSVDqrJtEjwZN18u_fU1s50oeCyrIcr87RNRLweXiPjJ_QA0zKhP7v2VpR-C99rdJnI4HFmTM0AyN_CPHrqEemq2mpCuJw1IZ6BPiuREJ87mCa4fgGKiq47z6eIEvQPMsdknym5DtnqOhdPQFEk3DBgS-ZEjfOZTR6vs0iQjQrY6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">.
قم تا مرز انفجار شلوغ شده است</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/667790" target="_blank">📅 10:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667789">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cbc73046.mp4?token=lKi-Z0x-zM4_mFHR5iugXlaV6rT84dHkmZGCn426kjAuxbwzRriN148Rd28P1j_Ub0NTRKGXddKA4hIxprPoqSTRJK1XPcZBkIxN5vV5m0OnZXshPJVx48s96jOvA4GdpgIhFI88oTlZ2DXzYum_tsGVxGdYAtZ8I9eDUAmxOvF5Iqq4M24EVH4EhPHTKjtRQkO6tcfsvLlrRurov8OFQPk9FF3tiBJZaC5KnrIAomxpFj3k83GAw5ST5V0EFcipV3WZwuMf33bG502M0m7moIfHjo5AE1Mcg7-gWYY0asTAoiyA6D7bHROccyz_njfEL4x2TTy0Hh--sjWUqSTeqr6__5XW09BN-dsRJWldxGdKtUbJs6u9VVh-jCF3mKPNl6XVYRchPsZuj2NUejFgj1q5HXXPhq6Y8E8o-qscBlnVjtyuvvdB7HlK9J50GNSps_vsJYvCIEMiEEJSLvb-x6Js2c5uJnvcTj7YCiROP8WbLQEmhbNVqE0VcSyNDthSpKBfvCNCB4RyU_gi_pxLXLwwl-XFtXqnqDtm1c5jXpOHnKxP35TtgjBhQ8NCspPFp9HAf8CsKYWOfTDlnmwoNyxWXJKBHymtops1ytJ77vNhNxreGMjKd71qAfjL1oF1gZYOjtGSQfMZJIHiazoL3l2laiOj5Ngp088vwxAWU1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cbc73046.mp4?token=lKi-Z0x-zM4_mFHR5iugXlaV6rT84dHkmZGCn426kjAuxbwzRriN148Rd28P1j_Ub0NTRKGXddKA4hIxprPoqSTRJK1XPcZBkIxN5vV5m0OnZXshPJVx48s96jOvA4GdpgIhFI88oTlZ2DXzYum_tsGVxGdYAtZ8I9eDUAmxOvF5Iqq4M24EVH4EhPHTKjtRQkO6tcfsvLlrRurov8OFQPk9FF3tiBJZaC5KnrIAomxpFj3k83GAw5ST5V0EFcipV3WZwuMf33bG502M0m7moIfHjo5AE1Mcg7-gWYY0asTAoiyA6D7bHROccyz_njfEL4x2TTy0Hh--sjWUqSTeqr6__5XW09BN-dsRJWldxGdKtUbJs6u9VVh-jCF3mKPNl6XVYRchPsZuj2NUejFgj1q5HXXPhq6Y8E8o-qscBlnVjtyuvvdB7HlK9J50GNSps_vsJYvCIEMiEEJSLvb-x6Js2c5uJnvcTj7YCiROP8WbLQEmhbNVqE0VcSyNDthSpKBfvCNCB4RyU_gi_pxLXLwwl-XFtXqnqDtm1c5jXpOHnKxP35TtgjBhQ8NCspPFp9HAf8CsKYWOfTDlnmwoNyxWXJKBHymtops1ytJ77vNhNxreGMjKd71qAfjL1oF1gZYOjtGSQfMZJIHiazoL3l2laiOj5Ngp088vwxAWU1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروش وصف‌ناپذیر مردم قم در آخرین وداع با امام شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/667789" target="_blank">📅 10:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667788">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89066c841a.mp4?token=GHOgBLZUpMlLWejhOn0dkeISTI_yTAE6bd4ANcu9GCr7JNq8i5fj0kfLQ33hg6CcME-sIs_QdAfR7_NVmWqq8Aa2jhqSUCiiGn4iskwYZ8xqUzlLTM3uC9-m0MSy0BPuGDGHDZsF3C6dtfelUZUdSrBYgxK15NKxFRAY-Jq3qifEUF4n8a_flG2n-KYjhsjnxp_LW7RXR6rpwONNnF_r_GvmgH8i7hJm_DyqcIi_tTuLU01WmchX08vZdmXDSRVQ7u47Mhzy0H9aM6jv79U8O8XkXJOA_Px602IHnh_Maiwhz8eQCIutTyoLYuNjf4K1e5bhFuoQwdz_qtrBuKCutw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89066c841a.mp4?token=GHOgBLZUpMlLWejhOn0dkeISTI_yTAE6bd4ANcu9GCr7JNq8i5fj0kfLQ33hg6CcME-sIs_QdAfR7_NVmWqq8Aa2jhqSUCiiGn4iskwYZ8xqUzlLTM3uC9-m0MSy0BPuGDGHDZsF3C6dtfelUZUdSrBYgxK15NKxFRAY-Jq3qifEUF4n8a_flG2n-KYjhsjnxp_LW7RXR6rpwONNnF_r_GvmgH8i7hJm_DyqcIi_tTuLU01WmchX08vZdmXDSRVQ7u47Mhzy0H9aM6jv79U8O8XkXJOA_Px602IHnh_Maiwhz8eQCIutTyoLYuNjf4K1e5bhFuoQwdz_qtrBuKCutw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم بلژیک به آمریکا توسط دکتلار
🇺🇸
1️⃣
🏆
2️⃣
🇧🇪
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/667788" target="_blank">📅 10:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667787">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqgyLipZ014ZEyl66-83-bQ3QtaaTawXi1VvdVSljYPHbuIblDJhIfAuFUHmUbWsxgKMmhaILwvxmLgOUlEMwf6ZMCXyeOHv35aZStDn1wce3oAz7IAN-NpXx5vPk49TQRgKCyChA9pTXGdLNSzNJXGnXFwyFg3sJzeKwvD4WBACSDgqNKVsITOJTNCPSop9YAa1DbI3kHUzvKOr8CrcdLfEwIsx7RNf0HKlIxN8_aK3i7mqiuX0Xo-QLYvLEIIgybZqNBL2cKsAQ_uP9KOVKPYC1lJqkoQ1XFBcvMkXPaCVtgXEL4X79roL_lD9blI2v2jt-BaGGCp8sBg1DMFgIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماکرون و ابومحمد الجولانی (احمد الشرع) در دمشق دیدار کردند
🔹
این اولین دیدار مقامات فرانسوی با رئسای جمهور سوریه است پس از ۱۸ سال.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/667787" target="_blank">📅 10:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667786">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a3897255d.mp4?token=F7ykz3pw0s-joCcBaVXwHnKfQ1B-jWPiVC-Scp4Rr2S_m-OBdeZufta5jfhIBT78xmi2MhV6TMOT2p0fD5NPiLcVaDZJMAYx9mTIN0t8UDVLN-G3GM62p_Jd9-eNdXHw8sbstEBwfL5Vskk6PyqXUEPx2p8zSJuLAAzzbNEUJzhmXMq8vu9pPutynB4a7G6bW4KEPpwD7r1-owcfoX6jlqHWBrBE6NLagD-kDUqKTWPPnLD6_pzbeaEnvlPJAShX7B7LMGvc3QRjSh6W9GID1aPbRLpCCZaodiTaB4Bjr5r3h2yLws_4VE-HxGxOzcFAXNqEtgm4R4HubqbW3AoEjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a3897255d.mp4?token=F7ykz3pw0s-joCcBaVXwHnKfQ1B-jWPiVC-Scp4Rr2S_m-OBdeZufta5jfhIBT78xmi2MhV6TMOT2p0fD5NPiLcVaDZJMAYx9mTIN0t8UDVLN-G3GM62p_Jd9-eNdXHw8sbstEBwfL5Vskk6PyqXUEPx2p8zSJuLAAzzbNEUJzhmXMq8vu9pPutynB4a7G6bW4KEPpwD7r1-owcfoX6jlqHWBrBE6NLagD-kDUqKTWPPnLD6_pzbeaEnvlPJAShX7B7LMGvc3QRjSh6W9GID1aPbRLpCCZaodiTaB4Bjr5r3h2yLws_4VE-HxGxOzcFAXNqEtgm4R4HubqbW3AoEjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول آمریکا به بلژیک توسط تیلمن
🇺🇸
1️⃣
🏆
1️⃣
🇧🇪
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/667786" target="_blank">📅 10:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667785">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d339b23a.mp4?token=aNsRyM5iP2Krzv0RYpL-ADaPhASwph_md6jY0UdeBY0z30sPK8H-WakxsXj52l8DhyUqP8UCkKwmxJAw5vHs2OhogWEu3gGh1e2VF1brJDYp7HnMco5rtl_2PX3LY8hkQClvb01Eu8VfCdqiWvjz-NETsqBLjrccf86Aj9e9IUL9Dcy9R-v13a_b4nq1em2s4iq86R80fRtCT0keWEAdWp8gCgr8U9CxWEMBi_FUNi3WDiIDCmn_3kGQVmWuiU2ny0JxcHAfU5ZzyIjUvABdzuaFgsAWcGWt0a2daMW96_GfimfkAeCW2-B-s-051p4Y-Q_EyOXLGVoXAaKMQ1zBzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d339b23a.mp4?token=aNsRyM5iP2Krzv0RYpL-ADaPhASwph_md6jY0UdeBY0z30sPK8H-WakxsXj52l8DhyUqP8UCkKwmxJAw5vHs2OhogWEu3gGh1e2VF1brJDYp7HnMco5rtl_2PX3LY8hkQClvb01Eu8VfCdqiWvjz-NETsqBLjrccf86Aj9e9IUL9Dcy9R-v13a_b4nq1em2s4iq86R80fRtCT0keWEAdWp8gCgr8U9CxWEMBi_FUNi3WDiIDCmn_3kGQVmWuiU2ny0JxcHAfU5ZzyIjUvABdzuaFgsAWcGWt0a2daMW96_GfimfkAeCW2-B-s-051p4Y-Q_EyOXLGVoXAaKMQ1zBzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار خبرفوری به نقل از فرمانده سپاه قم: ماشین حمل پیکر رهبر شهید انقلاب و خانواده‌اش تا زیرگذر حکیم خواهند رفت و از آنجا به حرم حضرت معصومه(س) منتقل خواهند شد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/667785" target="_blank">📅 10:33 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
