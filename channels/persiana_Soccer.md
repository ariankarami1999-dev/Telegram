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
<img src="https://cdn4.telesco.pe/file/toKjM-XBPhDFdEauepOrDFZtFiRmSSKY1Ia73S-DVUMkT8h6XVwtNbqIREdD9ppRQZ3SPvv30rj0u5TK7xx13gX5Ew3ksiYYYoxUIS8FiPZK56nOLcSzDIxBQq1eYmZYPpGk0PrERePBGh2US24sunf28O4B_QfVoNmDLgEOnjFm9WDCwl8YACgjInKkX3GIOJGBs6vdHzl8gTtgZCjKuS-Y0lKPOrqT2BbGvNbT_0IZbe8fzmOsoSw08enfUGpE6GdNhr6Ju1DJibp286LdYws3igD4LfQq8B1pdm0flYe4C4lkp20SsT3fdRlFZLKFvU7jjUBjCS7NbV1mG37SZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 528K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 15:36:11</div>
<hr>

<div class="tg-post" id="msg-26215">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QPWeZRDFhpTAn0wQg_Yvczx7jbRDidUGdf9MRXdxfC8CN5O2WzOUic6mwAucG-S4nsNWdY_Qy3ktU8LWxk93JsgLIKZflayC3lmEIdVDTgRO_Ksz2uHAW2gKK3o5x0622HerlNJ0j_i_xGq1oBqrGrLrhEqoJhvIc_7yar7qeRwyxM7WbJ7zVopthvSDOu1EDM4ZzHWAKTqWWCmJBWeZXrt21BRnV9RYtzL58R1KlQp0NHKZfT71YKPlJEFTrCZlseidFow4jfPAKNl2q9-BT32XAzANzjlvxRvYzNXzODAA_AF6sMn8uDtFMHVbrysMYTytkSGOu4F1NYXi7nXvjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ssDnWcfvfEdCEn1UTrDX9vkWu32rAPfVg4tYajds21Uw7PeOlvz8RXBOuoEBZmYzB38U3E6Q9RU9zMkIZQfp3mliFuH0fvDNF-VHHLg8tSq8wwPqSqLteoBg6FrihOSMnAkSQ-frKC4lnElMHl-GoXJsvfyFe2pdt7ZQGLpfbJKbd4xPeoMM3nqWG2tdUbcSAN_0ZAhpGCFbQTp5tMGa5-AtcZPTxJr96AuJkXAk7dXPSSyZPLG8gtX_bdLUPLOoqWFNFQfr5QOnT0kLJQvYk_VhVN0uebMstu9rynII5zdTTXxb1I_I3KJbmHJTC07nWoQpjG4beyTVGPmGoixmEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
ارلینگ هالند ستاره نروژی تیم منچستر سیتی و دوس‌دخترش در تعطیلات پیش فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/persiana_Soccer/26215" target="_blank">📅 15:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26214">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klYgDuWf4OusW5KzWZ0QBFSwiIU9Rx6BL9x3gYiBReF9Xzb3s0Xy8ybQVOqPrCWXpO7ccvlKPwOlpSd5X4JTNis9vWYjQ_h9cPQdAL4Gg5ltkOI3yZEZXTcvwIS9kbPgT9aDKXpX_JQEatxSTLDs6jcF0jaLg-BkDxO_pvQVKMEGVxi3QvH-yY5FPRUlrWxQ5M1xjOsjmHTKsl_SUDCq8h36SLtQ2RwWQ9q7R-ou-qGJhXFPwqm8aXtXZy2_EmF3og-o6P5TIdQ4oK3UxJ_QLNcevLuUhNMe3DuL6o3IYf-JgU6MR7rdAAYLVWNdbOGOpZQqd6Z24r-muNxp1v0uZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/persiana_Soccer/26214" target="_blank">📅 15:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26213">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scgutJYuS7zOAPOeEnaQDKJWxac0iD_fEcsiLyODiIdMMzLAPy0mPzTiFk3cQb9MhsiXNEZOygk8Og8dys8U1masWNNnCuNulJZOwhsdlr17nnXJh2NJIHK6Aaz-KDlAcA7K1o7IghXsIPvZZiUvYQV_onQ72pd1FJcklBMvWpHYP8MQSx2xzxeKtiFMdI8_iecCcoA3ajQ4GIkSVC4gmS7KDajy51gkXsh8NQySwQy5EFV6VyNyCGfjko-KvV3O5aXnxsiL3_qr2cZzRV36GmNtxZ9Ny88sk6M8iuPCOrGppu_8YvKWVTn1N-uDgsMPa03IqTvFlCVXGnXxQkqD_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/persiana_Soccer/26213" target="_blank">📅 15:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26212">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbrkH1VgTZrO_Xa-cWJKXzkuMklCGp1LadUg0L90R7MeWZLx4B8OpkKTmU6jO7aJEVCTpdgp5o2BXwE5_XkHdiIwEkCa5_e2aNhV79KagmVwXXi-Mgqm0r2XzAFowjOLgqT0cvtYi68Mhr113jGU8S3THwmlSS7Tf2VzLKUdHZinuaAS2369Fx0MBWuEXDcqBOCX3KPLAb2F_KNdltt7umozBJURC76xxZVX7Q1xVJuR7V0EiYyn5RgC4-Sfswfrm8pingL2mVFMt80nrX44IlBVrPYWG33PLTBdjd4ZBlljEJ0hZiX3Wa72F0yo1UWAuTi-4AbtiVgnhw83mgoGhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/26212" target="_blank">📅 14:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26211">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxvKLDD9aAe2lB9Z7NwHpEO8jgHzd_OvJ03hPN1oSSlYF0buYCnxTwq7DffZjmb5iCEtibYKppnbGDEkqaWqDqhT_m5yKwh_UexqcjzmC5Wql7mxEOoeCKC0pS0tIXnOtQ74MfaEB02IWFUaQtaQ25DCH4W6MPj3Q148O6EHm5sCBU3c9Q_ApsUeAQlWOluRHGgk5kx-posu1R7fJr9QW-XA4vi4WX1bHUaSrewlIK_m_LdG1k1vCtnfrNAY64Va5KaEMAn6YUgzcY22M1_CYaC58ShEbkrQ3vYk7V7LBOGd9SwuHvnWZDWtANmP3Z-G9_6PFxD6Bi8Zt-j4YlD6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا؛ علیرضا کوشکی فصل آینده در استقلال خواهد بود. تمام‌توافقات برای تمدید قراردادش‌ انجام‌ شده و بزودی‌راهی ساختمان باشگاه خواهد شد تا قراردادش رو سه ساله تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/26211" target="_blank">📅 14:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26210">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKTHBmXZ1hPrFEOtzBQ-Qml9zRX_BMX_lic1uyvTfeLer8I7HsMlosXERJV1TMxlROypWVtKeEyN52y9UR0hEEtbVp7u2LeSoYxWjVkgZsqZQeI282Mr7L6UGOmQapMbtod6dnfsSE6sXQjek-hF-m_wzmqIBZS85c5U1Y-qeUF74sPPvodIKvvYHUtkX0EMkWgnWjxyEy7rKyq7HCR0Hvdz3uBwLJQJZIjH11wleqdF6qSg5S7ILs81dsqRsKDsjX2w-8ro-D5tOU4RvJwcAX4ijUFEZ6pt8EbYrJkzfipUJ208xbdau0VuexFxW4EWoNnLJnwfULolDEhPe-zrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
جسی بیسیوو وینگر 18 ساله کلوب‌بروژ با عقد قراردادی 5 ساله‌رسما بارسلونا پیوست. آبی اناری‌ها برای این انتقال 8.5 میلیون یورو هزینه کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/26210" target="_blank">📅 13:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26209">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jmr8SUKSZzD4C7jz96gTJH_SoQYp_umuCphZqfuaclyDfte6DAv9lnFE1pYJECsf7fU-Fh74jIS4EHegBEUgNaLO5m3bYHFY17jkxUjXwVCpMpFpr24Pzu8lQ6O7jK5Y9sBLxuBoz4y2AOx-PJUGvLTO2lv1RF1Eb8ygjIzEhHMFvInKHo4bmzaHJuBEvF-un9f9oe4HYCl4-og6Wp27tUVgofpZ1T11HUQINcP0H9u7CtZBPvuMSU1rg_QnOrtsubbJQgwjuxXBe4rRW4iD-nxODMlDgb43la_QQKM3iQJXBHmt-8wKx68uLwU5j8caN4QSQePDE5-LiQfS2Qt2Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری
؛
رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/26209" target="_blank">📅 13:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26208">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJCdgnAvmv71M89troUfZK8qfO9qcbrc-IutRU_lKDDF2iQ3T7yBfH_lk5KUzjRTonFnIU9zLDrGF-exX3s6nEcfQV_fsisZy_SFBym-6f2FNgLrT8D6IHzfIDASQdF987tTZHb7j9a0X9P55U1dGvTf-6e161OPSyYNQXxJWfc6hbi-oxD0rXIk4V7W-E_aK_sNAqNgXLK4-5QBgAAFQkefGD9WlKBbsTgZiWeYOWWYV3Z--jfGGpQJmQRJU8W5B19FZQH_bF0RLqeBm0UVu7gfKjaaxb1x_fGc5B-_fH2GqHZCPwD77S2EzXDkI56vTnlA--8dRW7pwd44OhEQsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 10 روز پیش پرشیانا
🔵
بهرام گودرزی مدافع‌چپ‌فصل‌قبل آلومینیوم اراک باعقد قراردادی پنج ساله رسما به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/26208" target="_blank">📅 13:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26207">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVfb-83ruLyvuJ-SVkGNsq5VIwkfaP9OwXkSmPeiDUm2xZNAbMQN819kP051juS8yUNwtIW7Ayy95tOf-YX4pQOg6ComrtPhtAaoIQrIYfih2W1lZPw79KFQnRPnY7RItY5k38n8qM-aZfR3GSzXWCUhE7SWHKcvdDg6nJr0UyQhvb3HEV_Jrp00PU8X74R938UVeaxvfOWVwwzAvw9eP8KeSy6iEJT_1mLG8gi4tp2N-fMdbUn1EXWKAuXAHTebO4Ouwjn_UXvZ3ffdYmSdqhpwyOOC-8BEyo2t8HZW67olxbCrVuUJrc9kUlrwuPt45ZORaCmlj9BKhWxifBLL6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیران هلدینگ خلیج فارس از عملکرد مدیریت‌فعلی باشگاه استقلال به هیچ‌عنوان رضایت ندارد و در هفته پیش تغییرات گسترده‌ای که مدیریت آبی پوشان رخ خواهد داد.
❌
علت نارضایتی هلدینگ بابت هزیته هنگفت برای جذب ستاره های خارجی استقلال در…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/26207" target="_blank">📅 13:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26206">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZzlTbMTZA2M10pK8f3BthNO1QnP07TaCK3qsgp0sVbKTbRqxL1odWvgPbWoL6t7qCj99grzgRvUWj4c45ipqsnpa29GVpTKq_rBHWmP0fmZjdwzBmFiHk1xZOT_JXGO_zBZV2Fypk1eMeHJcK3Aq_SIzvbZXdPCNGbOfaNiRcEgQxYGjSRWEtxul-MzYk2-gcObPmvRN1UWpTL7PxTjnrvk2SPT8Vx5fXq08B9Hrf8HsybAsOa7dITYzA8zHU3_zK3AlyQCB9AeaInWwtYlpxPYz2ghkSqjCutNiKcmv8LaHTqYjb8np-_ehMhFao7ZqdE-tRo1B43qkCO4ZO-itA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ حمید مطهری به مدیریت باشگاه فولاد خوزستان اعلام با هییچ رقمی ابوالفضل رزاق پور رو به پرسپولیس نخواهد داد. مدیریت فولاد به پرسپولیسی‌هااعلام‌کرده بود اگه‌مطهری اوکی بدهد این‌بازیکن رو با دریافت 80 میلیارد بهتون میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/26206" target="_blank">📅 12:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26205">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSl5fW67J3sgzFsIcZz7SqqNbBP2M7OvfQ-0iaODasNstv_wgc3Ia-DvxO98Sdm4ZbMizoZi2nzjV9fc41jFeNo1991OLa6LgOpSyK7miJLf0wQUJkYPmfAoIf-OM2y57kev4lleEc2lcjAXxCTwo8Bkm5CjwE67PCZlmsMjFQbOBquMyPCL3bhvf1qHpPi_26qJODvMuZC7LkUmM51I-NYRrpkQEcTwkd7iPGTZTC1WGAI14oi5tLn_kJzyAX9ux-9-E6F8PyRrIG9SjaqkSWV0eiesoEMwBSe1qkx4jcwkz3h-3CPF5-YqNRGY7QI1MKpBIzQ1OHfIGbqo8lWDMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/26205" target="_blank">📅 12:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26204">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">▶️
هایلایتی‌ازعملکرد بهرام‌گودرزی مدافع‌چپ جدید تیم استقلال در فصل گذشته رقابت‌ های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/26204" target="_blank">📅 11:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26203">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kq5NwEP_f4tg5TxCJFqBj_ddue0iQiEBKXigLaAzY5Sev9JKhfluUCYiYCbC905UCNBQn3IieSBFMx9emDePPqrg9IR1tWJv72b1tpHzm7C1kBERHiu6FYQZ2r5sBuaw98f0L-pB5dLxV6SxyqbMUCQjU7mOGHUQ1a_odZ46Dpa6u1dOAAsS5Sqy81CVI5LoCpuOHw7flFhjrXQfQvqf2yoA23QcCxdAaWfEDv9zgTPtyRT_AVfABhxcfo0251LAP8UGlhQS455_hMQWCJAjPt75CaBNVnZYhwwTfkdaj4QpL1TGZHzsw20QvRftr2fgGjSYVNolYKVPZLjU5G2T5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/26203" target="_blank">📅 11:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26202">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6cc5dfc32.mp4?token=hbdv1g6IiMdAVxu4_jO15AADFeIG2aXFD7HTse8k_u8qDn8ch7KqryNmf3--BsY1x1jgVPsyAwJkK7d6ACgOyrJUx8SvOtffg6NXMlE1hRZEoigeSt2RDu9Y8zJB81N6BfFetHXw76gBnLGcbvjCxoDDIgvkZGdUfQNHVo4Kw8nMWQv3UozW9yKZ0zVrEqVkml3iB3Qln_uKlYnHt9ZeeIhhX71mhhZGxkLhC8zW9N11fKnNkA1yS_m252Sz865Vkimu4W312TGlbpnt4MnTKxrVCuMWieFd909QiogFy62BVBOEAujhPir2esFpY5Oo9vUJTPUxxE6SRi4KTcGanA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6cc5dfc32.mp4?token=hbdv1g6IiMdAVxu4_jO15AADFeIG2aXFD7HTse8k_u8qDn8ch7KqryNmf3--BsY1x1jgVPsyAwJkK7d6ACgOyrJUx8SvOtffg6NXMlE1hRZEoigeSt2RDu9Y8zJB81N6BfFetHXw76gBnLGcbvjCxoDDIgvkZGdUfQNHVo4Kw8nMWQv3UozW9yKZ0zVrEqVkml3iB3Qln_uKlYnHt9ZeeIhhX71mhhZGxkLhC8zW9N11fKnNkA1yS_m252Sz865Vkimu4W312TGlbpnt4MnTKxrVCuMWieFd909QiogFy62BVBOEAujhPir2esFpY5Oo9vUJTPUxxE6SRi4KTcGanA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/26202" target="_blank">📅 11:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26201">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mar34L5ZORXaufR1tn8lIIPL0Mk5IfRHQdVPAXSggyGeFd-mVTuG68K2hkkS8iOfZeFlnkAJaHFtAQRDj9nnMCzENNifgwIu3saveGGjVZD1ZyLfD_dQ5L2sneOh52rbzzJhC--NDRtDH5HTVyUDshWTm-rrhXTUQtpis_kShVRDWuPwTE_a_-ODC_kwv0MzAxB2FCEFf_1UMsNsQpq1K-VNnD5j1YyfH-eLREKLGb7IooAHIAVSwnqe-M4_y2kL_-aDzOuNLPqbT1aPR3lEQmcilMBhQcxaviJrn575m2zKxbCKPOTEKKpaL5izPEBtloquw9JxwY0qVCLwx0Wf5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد محمدی مدافع‌چپ‌فصل‌گذشته پرسپولیس باعدم تمدیدقراردادش با سرخ‌ها با عقد قراردادی یک و نیم ساله به مکس لاین ویتبسک بلاروس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/26201" target="_blank">📅 11:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26200">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-Ov1K8U2sr_vkMmvgYCmWDt8QNS86cO17HmZwtozmbbS_zztZDBF7B0ZBpe9XOcEM_fJt2QlpAkRpBPc2lQ_gaaHlVeLhpVnZrP6-MValRrtM7RGNhcUtJfCDHAT6YXoUwta5YwA6eUHFihuqNe-Ga1oGJudo9acEa3lJ0cOziA1ENmKYf20BnSf1Vgm1sq1x9y4Zi5n-Gk8WoOr7wMW41lxUPw0n7zV9y-w0BrtjpWVI8N6pYljy33xQ5sDmfhteiBMOUFOInF2jiLS-wRLDJhiVOUJK-ibfR8GsNZUSZNpEsFX4gm15yL5Hrp6XKpm_hAsYWj3OuDuGlZhT3gQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
علی تاجرنیا باز هم تاکید کرد: انشالله تا آخر همین هفته پنجره باشگاه استقلال باز خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/26200" target="_blank">📅 10:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26199">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jht8nLq_RcXzCut9ZBoTnEPrK7l3K4HIcbHeNEbGgHqx59IVyiqK1YwqvM_3x0G6KeavW2rjPpCv-Ayk7S2UOL_bmuBoWUhFjTo5_1Ay0zTz0AO2C0u-j4KPaCUHX1q7Meb9kotsPtNALr9RIXlabIJjzppNazcOSTSWy4ThfQdlpN4Jc1xhgyXfhe1Gs_F_rKEGr2tCAFCHRYzjTJjJ_ueYuk2in7__aI62gYQNbsJRQKLmTs9NPzu9AKW-VQ71Bf7NqG5ft747eZysHfolBJf4pwtF4u_v0ViLvZkp5Fs5IxkWA-L30xNA6gU3OrhalLoFNaaZytzU1MWAzSnX8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛
لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/26199" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26198">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a3189b48.mp4?token=DEDJCwAPXMhAl_I9awy4orxoP0XwXMs-oABOVhi1cYap8nMjwWUZKAz-jLcSw5vUZWqMiVsBgbUq-NmT3Bd6OSeuMVQhwWoYlHUVAYxnq8CVOyjP_feDdS4GgxAWUQ5m8wPXNo0fGESvy3gZPt0bBClBHI0Y3lDy094vWp3HofPjq1WI1PI7zY3-s6xFUKheRqdvORnmO8ZF8xApYNHYHLzc3vEHha28H-8H6X7jx_zrFBsg0KRsmHmA_kfx2lA3Tu4KT9Ykm4j8dRp85qgcRuPSEuI9xHZyoz-KF03SdXtMjyTitj83w6NoqFvBi3tYoUqHgsJOKY8mLTam0QkYyUStuwE5CKfT0rUsAFn0azqTFmQ1aASVwambQFxQTuvdsQM37g9ClWQnATFEBkjegmqX3uwmHtZmDvf3Wgz_LJGG0sVUbh56bkQdoYwBpwkiJihGZkptjdp4X0O3X_gi_46swYytleR22D4ofkDypFdwcaCKLjmDGRRi98_UYPluX3FPlU93UXthfELt7dE9YBI_Fsf8pc4Xgjuh89-FqkmD2rVXz_8qdDgXyqPz2QEQLtywY802ewJTzR09olf2N2W2BkxtmrcTBbNn_1DJvc-ATDVjKIZPyuwiVcKz2LF4U4Xa3ILKBn3w4I0JTQM8RAbiyU2_XGNURPTG_H6n9s8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a3189b48.mp4?token=DEDJCwAPXMhAl_I9awy4orxoP0XwXMs-oABOVhi1cYap8nMjwWUZKAz-jLcSw5vUZWqMiVsBgbUq-NmT3Bd6OSeuMVQhwWoYlHUVAYxnq8CVOyjP_feDdS4GgxAWUQ5m8wPXNo0fGESvy3gZPt0bBClBHI0Y3lDy094vWp3HofPjq1WI1PI7zY3-s6xFUKheRqdvORnmO8ZF8xApYNHYHLzc3vEHha28H-8H6X7jx_zrFBsg0KRsmHmA_kfx2lA3Tu4KT9Ykm4j8dRp85qgcRuPSEuI9xHZyoz-KF03SdXtMjyTitj83w6NoqFvBi3tYoUqHgsJOKY8mLTam0QkYyUStuwE5CKfT0rUsAFn0azqTFmQ1aASVwambQFxQTuvdsQM37g9ClWQnATFEBkjegmqX3uwmHtZmDvf3Wgz_LJGG0sVUbh56bkQdoYwBpwkiJihGZkptjdp4X0O3X_gi_46swYytleR22D4ofkDypFdwcaCKLjmDGRRi98_UYPluX3FPlU93UXthfELt7dE9YBI_Fsf8pc4Xgjuh89-FqkmD2rVXz_8qdDgXyqPz2QEQLtywY802ewJTzR09olf2N2W2BkxtmrcTBbNn_1DJvc-ATDVjKIZPyuwiVcKz2LF4U4Xa3ILKBn3w4I0JTQM8RAbiyU2_XGNURPTG_H6n9s8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
این‌بخش‌از گفتگو عادل و علی آقا دایی و کریم خان باقری در هفته گذشته بیشترین بازخورد رو در فضای‌مجازی‌داشته‌وحدود 50 میلیون ویو خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/26198" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26197">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKU2tLFziWPQPDbyzWYfC1x_TVYCZ-SEq9LvGwjpyYficBpt8Zton6ns0UskOQc6uxHZIkEBj4w9oFRJfozJ5pOrkRnTaHRvwC1Irn0xIDCGPDJ1BmwatUixy8D94sV_9KnCGoIG7mHXYyHms2Kq4tQHAuW-_exoVfGHGJtVPBv88aiAlYyioIu1l7Xc5IMfZf_JJNWp23eGQsj-yVJwXgQ4XloX2IRdkddMlosrkEnYCtmqS89MSiNTovIZM77YTrPzIjfHQoR-MKnf5Q23fHT-lHv7O95AYz32qApPM59kDpzOKUcFwNB6WGU5evcG-9PqNzqRLDiMWSF4TYqcjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سوپر بونوس
0️⃣
0️⃣
2️⃣
درصدی وینرو
🎲
💰
1️⃣
میلیون تومان واریز كن
3️⃣
میلیون تومان تو وینرو شارژ شو
🔝
✅
مخصوص اولین واریز
✔️
🎲
برای اولین بار در ایران
🎰
متنوع ترین بونوس های را در وینرو تجربه کنید
🔊
با وینرو همیشه راهی برای برد پیدا میکنی
🎁
🚨
اطلاعات تکیملی بونوس
⚡️
✅
✍
️
ثبت نام آسان و سریع کلیک کنید
✅
🤩
🤩
🤩
کش‌بک هفتگی
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده
!
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
r30
📩
@winro_io</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/26197" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26196">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESLGO6g75P09C3Wl1XsX4fNGyMNqM0RfNEY3UPjWvVAs27bUpKB3AYZrHL-J1YeDZjLMQ8hdZ-oKT76u-ViHA7qKO3XH8ilyJn63pytOvsTi7PmHiaoyo7mg9HCzoQfc0AZgBPBgzOW9q9o4HNAZv1d0pru9hefMt3988BGn4r6ZAAFI_tm3pz6WMWSAR084i3-6k7hhLxHYLBbxYlgjtP5a2TvSjiPGthdAxNeDYm6JOJZCU5CNGYlIWAfK1Y5qvHOioogIVAHgchbWAMIdoUd6aZ0Fw7xDFIwqi7kwxyevthopeETQhmlB28hMOiUg2gJ7t6st2-xnIdj9Sy1Juw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برسه دست مجری صداوسیما؛ تیکه‌ سنگین رضا جاودانی به میثاقی در گفتگو شب گذشته با عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/26196" target="_blank">📅 10:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26195">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xnl9ymVkSXNfGTYR5mOVOLFT3oK4Iw7Pm8Pz_pa23Sh05bq7wNkne3VEcltpp4JakYGm-dsJDGeW5x-8CBHrLANEPpnvH7yL0FfEkoJsW8_tGe0MRBlpK7GOoL3nmXeRUrewWEhuY30bHk1hhVCN9vssc0oqJsxxTfi1koP601ccQYHeZWFLx6YSTneRW1YA_GumKT8kyZAXFPddePoo05BJeUtBgcASdyLVUUIHvhyDwZAOD0CQCMjrRnxSNRKGGMNaPwGjnCklAh0HVKoJazoK5fzvXcz54pG4EL6KFaUCBS6vEr_6smB64353qQN8kapjSvWyG9WLw7mQGGkuEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛پرسپولیسی‌ها برای‌جذب ابوالفضل رزاق پور مدافع چپ فولاد خوزستان با مدیریت این باشگاه تماس‌گرفته‌اند که گرشاسبی به حدادی اعلام کرده درصورت موافقت‌کادرفنی‌رضایت‌نامه رزاق‌پور روبا دریافت 80 میلیارد تومان براتون صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/26195" target="_blank">📅 09:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26193">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944a94e4e2.mp4?token=rsyWix2ieIMsaL2WqXZZLJEpjOJV3mS6562rn287yttUm2OpqVlNLV6sq1_btoID0KcMAP_GSGl66CriKHtx7Y690fjzUYGOLuBSYlru-1-Y8zhRQe3Gl5di9ccSmmS3BYTVgWLpTvTpYReCOXkTIq4hf8HbEmrAZVbZDQnRt99ETv6ekgZ0m_ivEmMLIxrcb_IHhqw731GLDCMGyB6g73IEpws0ysy-nCJPArH-_OL82_SQLEG5zu_-5Z1S43Ek5slm6ON8OnKhF7oHpDRVlLTXLx2aNlM2hAeG1EIEWN6V9SUa8n7NAtfOKp5o1pBwGA1HEQc_qk9RJrp-ZrZltw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944a94e4e2.mp4?token=rsyWix2ieIMsaL2WqXZZLJEpjOJV3mS6562rn287yttUm2OpqVlNLV6sq1_btoID0KcMAP_GSGl66CriKHtx7Y690fjzUYGOLuBSYlru-1-Y8zhRQe3Gl5di9ccSmmS3BYTVgWLpTvTpYReCOXkTIq4hf8HbEmrAZVbZDQnRt99ETv6ekgZ0m_ivEmMLIxrcb_IHhqw731GLDCMGyB6g73IEpws0ysy-nCJPArH-_OL82_SQLEG5zu_-5Z1S43Ek5slm6ON8OnKhF7oHpDRVlLTXLx2aNlM2hAeG1EIEWN6V9SUa8n7NAtfOKp5o1pBwGA1HEQc_qk9RJrp-ZrZltw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل: من هیییچوقت بلع قربان گو نبودم و نیستم و هیچوقت هم اینطوری نمیشم، اگه میبینید با من مشکلی دارید بیاید دستگیرم کنید و هر بلایی میخواین سرم بیارید ولی من بله قربان گو نیستم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/26193" target="_blank">📅 09:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26192">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a85e23671e.mp4?token=I5tLRp9pbDfdXMRUfNuOOkS69HCYNJuEu2pqB_o-to3_wNRiopccDpl9Bs9W4Tbwpe26j1EdT039a2j_sJfjw6DHIqaexEKO2O1WpSqy4g7ZYVpQx6DkWj37N8ZJfx61zC3WS72W_oe4JRpmp_mBJfVUtbKN5Xps5_iw8SoMlAu3zxLNPwsOveCsvsdYVDgq_ZT6E-1biGGAOWoUb10AugVoX6llBUr8qexjX8fDEOhyWdcsSTfcKr7wW1jl2dTvoarEGoXGX1Dc56kR1Hzu3brxheFAR-EriMOv5MCn_Qf_IhiYL-4JTDl_H0Yl2GmqTWX6sUENPOy-IYXIhJgDrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a85e23671e.mp4?token=I5tLRp9pbDfdXMRUfNuOOkS69HCYNJuEu2pqB_o-to3_wNRiopccDpl9Bs9W4Tbwpe26j1EdT039a2j_sJfjw6DHIqaexEKO2O1WpSqy4g7ZYVpQx6DkWj37N8ZJfx61zC3WS72W_oe4JRpmp_mBJfVUtbKN5Xps5_iw8SoMlAu3zxLNPwsOveCsvsdYVDgq_ZT6E-1biGGAOWoUb10AugVoX6llBUr8qexjX8fDEOhyWdcsSTfcKr7wW1jl2dTvoarEGoXGX1Dc56kR1Hzu3brxheFAR-EriMOv5MCn_Qf_IhiYL-4JTDl_H0Yl2GmqTWX6sUENPOy-IYXIhJgDrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/26192" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26191">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72d81bfda.mp4?token=VnmWCUl214MAttY9HYp9jIXoSrVl97NkSQ5sTFpm1oZbPzWWM7hbZyhSTHJMcKkXfN4xn8VSweDCVH8_0Z7see4g29IIHAvEst5wsytrpwmgPUOHLTgbuWTDWYXCmpfHaaFUQ2m4p7kCt91KoNQtDv-W8fOQDJiQxvdAPb7MGF_IpGl35U3wjmE-PBymKWE5gqlIBwQGEFRzbRlS9mswbOeYH4iM616NYSxbD1uPkjb2bDzVnxNY5yEIZb_uGwGFrvOR3i81Qmh4QG67_H77Gk83TCQvA4tMo4yonsTiI12XmINNrnXqGr3PneMujcd9PeFXFoG1f1ziNsi9K6NB9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72d81bfda.mp4?token=VnmWCUl214MAttY9HYp9jIXoSrVl97NkSQ5sTFpm1oZbPzWWM7hbZyhSTHJMcKkXfN4xn8VSweDCVH8_0Z7see4g29IIHAvEst5wsytrpwmgPUOHLTgbuWTDWYXCmpfHaaFUQ2m4p7kCt91KoNQtDv-W8fOQDJiQxvdAPb7MGF_IpGl35U3wjmE-PBymKWE5gqlIBwQGEFRzbRlS9mswbOeYH4iM616NYSxbD1uPkjb2bDzVnxNY5yEIZb_uGwGFrvOR3i81Qmh4QG67_H77Gk83TCQvA4tMo4yonsTiI12XmINNrnXqGr3PneMujcd9PeFXFoG1f1ziNsi9K6NB9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل: من هیییچوقت بلع قربان گو نبودم و نیستم و هیچوقت هم اینطوری نمیشم، اگه میبینید با من مشکلی دارید بیاید دستگیرم کنید و هر بلایی میخواین سرم بیارید ولی من بله قربان گو نیستم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/26191" target="_blank">📅 08:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26190">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ef7K0Ko8gxejDI7zc3RNt1d5vSoGhKANPz_zQITprB0avWWcM7KM4Omux3h1R19rwZoiMIVm68kBwrA0ogvgN4GnMeCaq_ohNRARZ2nfg6SEvHVJgvKEHFJWMKRWPuJ99C1hoYdxxYjJtn4963a2ip5aslEHooo0vBz5qE4VBa2qXsMTIa_8dY4iAet5jGGuEZHMIwKDPu__9wBwg6FffheSZ0OjLm5IDOiIxpTP37BQhToxYX5lutnJRGIvALTjpQlt0YtP3IHFHXtgyZie4Oiqo6bUVAa_6A96QGKXjFDzwFDHqFz5N7BS5WcGJYwB1GcRJQIMdOJYdsfggKM8tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26190" target="_blank">📅 08:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26189">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCxKNMFZfNaUyCk8Z5FItKLLb3Esn6SNHOzBhrzG2RdRf5Ed-6nHHdwsKsCjrrw-Fj_fOSGLSeC7bV18sEUsGMV9AeGkYDZ1j-e1yQ93kagXkMoeRuxHAf_bQoeUqJv9183JSefyMbPK3WH1cMspRt-ZPhGMlFG6t1K9G_g26Egz_vYJUX66RhA6h0UONCx6yIXyCYZY1C9VfBmB3NC6A3RrIj8T_qJHQxtg7p6S7VqEd-euVujVkR4Me6xCpfaJ6wq1S40h50X44Lxt6VwDHAXNXLqUPtMTGXzBMQLX2KBpJ9vLr7lSJ9oAI6b5o4hgBhsVOOBrkGyDQLd-pI1Z0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/26189" target="_blank">📅 08:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26188">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc5216b419.mp4?token=HIc13qcEskQsenRFHQg6g03WeOqBTMFmL9pSAt_0H1J7a_GmIn_vc2KVHLI8eKQVcspMTxWgtAwfvA_BjsiOl2W6tnQEQ1-UuB47pKx3OXaYBrSaVvb9k5fvcWQmEFO9tygCYTPSEL0Pv-42wkQpCBRurT-WSPzIa4Jo9ubeD_GTHowM8BoCsZnTbsaPW-i8gDtPuCdFikBk7ctPx-JaRFUCeERqwQDijymw2MDeNT4LCH6MQCpuzPvQoHmrFGAY9cp7wMxX2X0DGO0PXmjJLkFmsU3mVUppN_M0AzlTWZWzRTwgHf8LkjcbJLd-SAyTPDG0k0NohoAP3WCIvBdR0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc5216b419.mp4?token=HIc13qcEskQsenRFHQg6g03WeOqBTMFmL9pSAt_0H1J7a_GmIn_vc2KVHLI8eKQVcspMTxWgtAwfvA_BjsiOl2W6tnQEQ1-UuB47pKx3OXaYBrSaVvb9k5fvcWQmEFO9tygCYTPSEL0Pv-42wkQpCBRurT-WSPzIa4Jo9ubeD_GTHowM8BoCsZnTbsaPW-i8gDtPuCdFikBk7ctPx-JaRFUCeERqwQDijymw2MDeNT4LCH6MQCpuzPvQoHmrFGAY9cp7wMxX2X0DGO0PXmjJLkFmsU3mVUppN_M0AzlTWZWzRTwgHf8LkjcbJLd-SAyTPDG0k0NohoAP3WCIvBdR0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بغض‌عادل‌ازصحبت‌های حاج‌ رضایی بعداز توهین های بیشرمانه امیرقلعه‌نویی و فیلتر شدن پلتفرم ۳۶۰
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26188" target="_blank">📅 01:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26187">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e8c2669f2.mp4?token=aqqJa1KLgskPru3KDneBvf3NEZdjGCcFhKpCmWc65YGDcQ1Po_xPeRysFARU-lhWjmuSnj5FYVB6KWr9vdEpCw4ns3mu93Du-JVsNJKbUd1ElN68HmrIndZgXdsvSWDD9Bdsz8q8keQfBfvA06a6a7v7mk9rrP_MAeA4s07NOjvQY1X7fqFXx_73a14Bx6nAwOXjL6dV_F89Ni4emt0mOY3aYgxLULN6TdKyc_1la5fts1u_k87g_rXQQfLIrNP6meE-Yzs80YIDCbmUvLPHDce67RfeikIo8tx1_FTWRsjdHg6gUV2C5bjt4BbyI_1O4YKpyLBImlEHgozLG8YSxbv8mzXsM66rvpfe1OTJVzGWTuR1aOzSSnrgtbL8wkDjoqZubdRGoayX1zgFo5q-RvZ5cT9ApCoRwV-LBjSfIDq8xzIdOq6j9ZV1qwW-Yi4oRjHnleIVOOfRGWSGzPFf6SoHsMaA8bjDMNLONndDgHKjZ_7asX0oBtqb2ugYQ5yNvlqrJ4iMnCcWTB6w4DxOWDOMQblRXw7e3R66oWjxZiNgFm2G_-vzlvw952D6vync4NdVbtwo_hg5lbper2NOT-v9KqKCPigF1yY6yNDwDW4PsDba9PhbIiqkqUiDOu7IFmdmqiqK1I17VkfBdmejGCebFVyto_5EFp05gi8V6Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e8c2669f2.mp4?token=aqqJa1KLgskPru3KDneBvf3NEZdjGCcFhKpCmWc65YGDcQ1Po_xPeRysFARU-lhWjmuSnj5FYVB6KWr9vdEpCw4ns3mu93Du-JVsNJKbUd1ElN68HmrIndZgXdsvSWDD9Bdsz8q8keQfBfvA06a6a7v7mk9rrP_MAeA4s07NOjvQY1X7fqFXx_73a14Bx6nAwOXjL6dV_F89Ni4emt0mOY3aYgxLULN6TdKyc_1la5fts1u_k87g_rXQQfLIrNP6meE-Yzs80YIDCbmUvLPHDce67RfeikIo8tx1_FTWRsjdHg6gUV2C5bjt4BbyI_1O4YKpyLBImlEHgozLG8YSxbv8mzXsM66rvpfe1OTJVzGWTuR1aOzSSnrgtbL8wkDjoqZubdRGoayX1zgFo5q-RvZ5cT9ApCoRwV-LBjSfIDq8xzIdOq6j9ZV1qwW-Yi4oRjHnleIVOOfRGWSGzPFf6SoHsMaA8bjDMNLONndDgHKjZ_7asX0oBtqb2ugYQ5yNvlqrJ4iMnCcWTB6w4DxOWDOMQblRXw7e3R66oWjxZiNgFm2G_-vzlvw952D6vync4NdVbtwo_hg5lbper2NOT-v9KqKCPigF1yY6yNDwDW4PsDba9PhbIiqkqUiDOu7IFmdmqiqK1I17VkfBdmejGCebFVyto_5EFp05gi8V6Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
اشک‌های تلخ عادل خان درویژه برنامه امشب؛ مردی که پیشنهادهای وسوسه‌انگیز رسانه‌های ایرانی اون آب رو بدون فکر کردن رد میکنه حقش این نوع برخورد از سوی مسئولان دولت نیست واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26187" target="_blank">📅 01:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26186">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnwCNhAt0yZfXN-dhTkZd8gLMt8od0-xL6TT8Mcoe_WWv3RtDE7hS7tvmdPMwklRWkfR-F-2Tuambi8hqopK45yDO26vdpCStaiYD711UeioHqWrZ8BgRtEVkl4lsqBISobZU4uEzHVjHtnsjeJu0EaIkAIZy1VOvgjn5XOm9Hit3nD32jrHGN4PAFRGa2n2fNUI15n0eROBOP7IiBTa1kXUk1lO_8MUlbok35F5XRsSAPtFZ92rpUoj9svesQUW821UwO5pvS2Hf7zsTkucC2Gl2ccmTtk0MGgwE-k9T5mee0DOx4Fmo6af1Yk7CTxVgqi4JS149lKU4ZLc8FZjUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مزدک میرزایی:عوامل‌شبکه ایران اینترننشنال در سه مقطع پیشنهادمالی‌بسیار بالایی به عادل فردوسی پور داد که‌به‌این‌شبکه ملحق بشه اما او هر سه بار این پیشنهادات رو رد کرد و اعلام‌کرد هرگز خاک ایران رو به خاطر رفاه و منافع خودش ترک نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26186" target="_blank">📅 01:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26185">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6808ecf091.mp4?token=EVkUe_H8Lzy87CtufwSyD6DCOYv_GLJnVGSHJDbwkpA4xf1ZPlcrj00uGk-2tUq4_62Qkqcb57l44Wtu1QrWesxqiB5S99Ih5pqKaZcIAQB1Wnc4XN1PjTW0yka3PY-IRQEdkaSrwdJi2uiKWGW02AL87Y5ZcHzmLXecF1ddWjXOvNaJ2eMwERfFrlygiIXZBesValekETvyVojKYF3I6KMhh9UOfsmbZb7_n6VmmWTuNj6LfxHh1H61DF2J5MDMsJfm6GUYQX6tMjz5SlC1ugZmc-ICJP2vgG-6PRCWlzd9WLOojCUEqRfKs4YnJ-hvBaN1CSha9pVbD6gv1TPr7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6808ecf091.mp4?token=EVkUe_H8Lzy87CtufwSyD6DCOYv_GLJnVGSHJDbwkpA4xf1ZPlcrj00uGk-2tUq4_62Qkqcb57l44Wtu1QrWesxqiB5S99Ih5pqKaZcIAQB1Wnc4XN1PjTW0yka3PY-IRQEdkaSrwdJi2uiKWGW02AL87Y5ZcHzmLXecF1ddWjXOvNaJ2eMwERfFrlygiIXZBesValekETvyVojKYF3I6KMhh9UOfsmbZb7_n6VmmWTuNj6LfxHh1H61DF2J5MDMsJfm6GUYQX6tMjz5SlC1ugZmc-ICJP2vgG-6PRCWlzd9WLOojCUEqRfKs4YnJ-hvBaN1CSha9pVbD6gv1TPr7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت‌های‌جام‌جهانی2026
؛ جامی که اشک سه تااز بهترین و محبوب‌ترین‌بازیکنان تاریخ رو درآورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26185" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26184">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19f1d43ddb.mp4?token=p3CajOZcGLKRmq-qF2AyEwan4GjIa3tzORI6bjPN3bNfIciB-tYzU7Fq9Wou1FkSEIhn4kyjLm2X_CkdHhh0bqF1viGkSfJKuf3TnxbKJnEyqkxhiwjcKN2nlrWRRrDZirpf4F5L4aA9pj52by2iEx_rkCfBnypmP5bBu7OEmHJoiw_WxW4KPXc0_3v2PzzBzLydxo_zbOhbE6oOH-8eLeXNpq-Mf1Jt4qRbZ8BSPm5jprRo02D3aHUtgzaGc5oW_OD7SWJEVDqoUhuI5VXvhohdNmont03My-rXQUSmMmJswbAQNtorWC--vKAtId3XI9aFbHEDFoCM7VZkd4B3lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19f1d43ddb.mp4?token=p3CajOZcGLKRmq-qF2AyEwan4GjIa3tzORI6bjPN3bNfIciB-tYzU7Fq9Wou1FkSEIhn4kyjLm2X_CkdHhh0bqF1viGkSfJKuf3TnxbKJnEyqkxhiwjcKN2nlrWRRrDZirpf4F5L4aA9pj52by2iEx_rkCfBnypmP5bBu7OEmHJoiw_WxW4KPXc0_3v2PzzBzLydxo_zbOhbE6oOH-8eLeXNpq-Mf1Jt4qRbZ8BSPm5jprRo02D3aHUtgzaGc5oW_OD7SWJEVDqoUhuI5VXvhohdNmont03My-rXQUSmMmJswbAQNtorWC--vKAtId3XI9aFbHEDFoCM7VZkd4B3lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های تامل‌انگیزومعنادار ایمان صفا بازیگر سینما درباره‌شرافت‌دربرنامه‌شب گذشته‌ جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26184" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26182">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZA8xY30oEvYGfT-0Br3Rj4mC8PsnMPITHEBkAJ538et1fLUdAsqJzovpq3pZC7LS64eCHg8JIkyjACvNJHDRDl-t0FWSjiBpG5OnRQaabF3KZc6ZyX4Yo8SiEB1ntrTIhQE53kbTKZHj8KZsw5ZqcOobQoE4DyEaQszt9gUGUtfD70E-Fi1rvAste_aceVZZiFDBhffWs5aLPn4F6KFlsbmYE_RGJwOlGVNOvaeiSg2vyGV8hMzDqJOipWYO_3bgDGLA_IOP_IzYFEMUENGoZAs51aS7WZ4IhDY9qm0253BHI8qRzBxi75ZUNgLiUvmdsICd3xARlDFtD0pf-jFfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رفقای گل دیروزهم گفتیم باشگاه پرسپولیس هیچ مذاکره‌ای با علیرضا کوشکی ستاره تیم استقلال انجام نداده و هیچ‌برنامه‌ای هم برای.جذب این بازیکن 26 ساله نداره. بعنوان اولین‌رسانه گفتیم مهدی ترابی 32 ساله بمب اصلی مدیران باشگاه پرسپولیس است و امشب هم جلسه بسیار…</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26182" target="_blank">📅 00:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26181">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adwELFtPwIShmjOydYq2wIVPFSNKFLKlABR3WzCBHi0I-bp9zp6833Jl6SiFqEXRaho8Th6kcnXfqGsxHutqSpes2AUJYwmwywgLCqvpaU9MBGnGfoFvoPt6NUfC6qrEPOwGdK9QhsPCgxWf7KENkDCN9F7BPZNiKl3Px0am1jXq6nyuEvdIq8qeLyc62lfNRx0_5lFMNVoJR8gajT7V3ouDKAuzHb6Q6VLOkqndO3xPXyGbzMyv-rhA5hjJQ9lMlBYh66P79TpFWpyxrutF9INzCl4WlrUoRpNHVAZ-MtX0dlLzz1WORPrMTfD82xTZvWdWYAcqHh5chSge_n-ytw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوه اوه اینو داشت یادم میرفتم بگم؛ با پایان جام جهانی 202؛ تنها دوتیم‌دراین تورنمنت شکست نخوردند. یکیش‌اسپانیا بود که قهرمان شد یکی هم تیم امیر قلعه‌نویی که از گروهش بالا نیومده. قراره صداوسیما مخاطباش رو با این افتخار باردار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26181" target="_blank">📅 00:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26180">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7f2a6c71.mp4?token=uIUpHkSNNPjJ7OPchpk5j7QVDr8yOLW3-ixOB-Ve2Jh5FhY2HZwrPnIyJKfLuYKUoqCRTlYeS9Bc7-_rzpIiUmrByHe7AHTlWDt5GIlYFYZbjpwCoY7CSmncUULbuPE-lk62YPqyYM_KJGzx4veiBQojsPbgc8fNa1QdoHDhFYbjxNAMj_92EDMbowAHSzLxlfp6YWWArsHA-yTUw35-w0iTUrQnTzQEyyQUi9IVk8eY-PSxAoyhrZfZEKPVdNRGZTJhbrUbdz0y-SKP5wG9I_sClg6ozoXEhwM5Fk_5vYvDb6g9_6wpEpDYqBKCfs0iSS6ZC5qmVlto_AJt5kD4Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7f2a6c71.mp4?token=uIUpHkSNNPjJ7OPchpk5j7QVDr8yOLW3-ixOB-Ve2Jh5FhY2HZwrPnIyJKfLuYKUoqCRTlYeS9Bc7-_rzpIiUmrByHe7AHTlWDt5GIlYFYZbjpwCoY7CSmncUULbuPE-lk62YPqyYM_KJGzx4veiBQojsPbgc8fNa1QdoHDhFYbjxNAMj_92EDMbowAHSzLxlfp6YWWArsHA-yTUw35-w0iTUrQnTzQEyyQUi9IVk8eY-PSxAoyhrZfZEKPVdNRGZTJhbrUbdz0y-SKP5wG9I_sClg6ozoXEhwM5Fk_5vYvDb6g9_6wpEpDYqBKCfs0iSS6ZC5qmVlto_AJt5kD4Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برگام‌داره واقعی میشه که؛ رسانه‌های نزدیک به امیرقلعه‌نویی میگن سرمربی تیم ملی ایران میخواد بابت صحبت های شب گذشته از عادل شکایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26180" target="_blank">📅 00:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26179">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=pwueDMqTQpztVoTsOtpzMH6Qnu4PPwxWnE-rVMu74K1w_ns58T7DHzhiR7GTmATNNNUStWkvNmHGtakTZoWZJGi971Y147drX6DUp1zgO_DD12QcD_7VMSjSUzLSMpgQGInMrXrkwsJ91GPfz7ZqjcqY4W37RSXR9H6LIrNuRq9mf5opkcrWy5vZx2RNhQzzgm5ghP3De5A_f1TGDtmr8IAJJrFsruL-IKivl_ZKSfodZWwEsw0TIO5so_uJprPlvYsdymbD-2MyOMjYltw9FjU141oxMZFaJ_JIDqTbfhDHIA-K_Dy4qYEmRuzl2e0YmJ7AUrJy3Jv1c30gL8P9GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=pwueDMqTQpztVoTsOtpzMH6Qnu4PPwxWnE-rVMu74K1w_ns58T7DHzhiR7GTmATNNNUStWkvNmHGtakTZoWZJGi971Y147drX6DUp1zgO_DD12QcD_7VMSjSUzLSMpgQGInMrXrkwsJ91GPfz7ZqjcqY4W37RSXR9H6LIrNuRq9mf5opkcrWy5vZx2RNhQzzgm5ghP3De5A_f1TGDtmr8IAJJrFsruL-IKivl_ZKSfodZWwEsw0TIO5so_uJprPlvYsdymbD-2MyOMjYltw9FjU141oxMZFaJ_JIDqTbfhDHIA-K_Dy4qYEmRuzl2e0YmJ7AUrJy3Jv1c30gL8P9GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26179" target="_blank">📅 00:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26178">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nc3fTur2v9XL1cNaHTZYx9NsMA0RzXlFYdJaP91RuAqL43Q2cMCfKmfMHSlvmcnUTZscTmYUXYdnIEGL7RoBfmhATT8roTmZm7vGirjatCD16hddRYBllaIpRz0pYMZMpMfSfuciTYx9Na66xOq9us84ncm7rEa6Us4tGJgMxzoz6ejgZrXicbz2GbwFaQs7uBUWKkJlCCAUORF3cRnCncujVpj7apdeCa_gXwrin7i4wYsmzKr-jEZkRaYo-e6JcW4ox1CeHkoiMivY724LVGyBRd0Vj2qY1zeNEBuEeW-DTBpYLYR3yHHoh2qrNQFH1AUrP8JNFPuA4SWK5zxyTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/persiana_Soccer/26178" target="_blank">📅 23:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26177">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnVZ6GGkQV2jKCGNK7A7Yg2Pz7hSVpQonSCN0_7ReDaeeqxV0BjwrVP6G5SpH6SARRuCcvCnwRS3MTJf0AhC8_pOLkmdzzWxNNCw7CA82dn3rm7LCf-KXYRGb7iwJ6kH4OG25jdQhJKni0n8zBNNAi5L5-bHNvYbdpirW3wO3XA9xjU27ppBSm31sJp351zNgdpnt41LgT9r8Zmxw9e8SqNbRLUQV0of9Ee8qpK3spycGecjY3ENqdoUII2IM1CtCGcHqqXTT8aiE0Jg4d0z3vhmKnnA0zIV90H9HVSNXYXOmojj9TtZjukfr1p_4-WeP8834qY3xib80quLXfCtOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/persiana_Soccer/26177" target="_blank">📅 23:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26176">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/In66SqNe45SDJOOPh3vpyoVwavQbKel4pTNi96UzhxrBesVZLDLm2t3EgREsLmKP5Pfn8rWTYa7BJE322_1G1qA_iE-0inijwaUtjb1hR6OD3HTxdazkHXf0bfHmyhb84cdN4-08ME85CR4ydLQyJF0CRD_D20YGW8FSLFihenzGBEmLHAxFSOBtItd7vh2oAQC_G2whKboUqJQIvx1fIkvkCHkDedixvscC4N0og2kM4kAOTV5g3v1KLyIbecVSWX2kpJN7x9lan7O47lqFToeNah107m1uRfF5K3TQncANvU79D-C4oiA81xgu6B1UI8wE_yR5SyWFsv1vRuqxBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ راجب دانیال ایری به اندازه کافی تموم اخبارش رو ازروزهای‌گذشته تاظهرهمین امروز به‌عنوان اولین رسانه پوشش دادیم؛ حتی خبرگزاری آنا خبراز متتفی‌‌شدن این انتقال داد اما گفتیم منتفی‌ نشده و باشگاه نساجی72ساعت وقت داه. حالا طبق اخباریکه گرفتیم فرداصبح…</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/persiana_Soccer/26176" target="_blank">📅 23:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26175">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDmGYEDY8nT9h0oj86MvIPf3jDeti7R8AddArSDKlVn_r1tqCzuacWWkfxTeno-cEyYSxuE2tFg3uRiIlwSYc01sUwQdd9HKI8_L5lCH1-tepeTW2zdTl5BFOZ5o4D7E7mwggmF_7Y6NmMGRvv1htGL5Ifk_4hlVsuby_lw_C5FsP0TaeoqDmM3VThreBspdvMLAo9SegJQv63o22zEcAdz_wgv1XOPRUFqJqM9-REDgXyTI_w8Kuvj3yKqd_W51lMWiPOOdyDTii6XtmZvU-RPuyDnUlnEon-g6rw1Xt1MFd7IpO0mB1FsaqXvv-gnYYWGy5UWc7AWLu1ArKCiXKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه فجر سپاسی با مجتبی حسینی سرمربی سابق آلومینیوم مذاکرات مثبتی داشته و اگه اتفاق خاصی رخ ندهد بعنوان سرمربی جدید این تیم انتخاب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/persiana_Soccer/26175" target="_blank">📅 23:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26173">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ed7e49e2.mp4?token=uISzn7QnWUn3TmSRtyiMQewQUN6yeAr08ffVUIsR4XeLqI8oXHU1CJUuZ1biC9CVRa5ACwM-9CJv6Z9yTyrpxwdVVjHNK_dUcppKzsogSkT4Iwtbru5OqFNGCLr7heEbmwnZDWvv86MIdiAcjakdkm3_LALtMp_8LWl90k3U9UU_yGWpfDK_9abIZtZ7gR17auVXab9Heu_e4zc7MT6Vhx_FEGY6wZ4pAubGvH6-0LrBVA-WwHpclZgOwkjbxr-odZFl7qSZUVy0xXb-AHuoRceZEMtgdzVWSQGZsIi4QUm945xYH2MgX-ZiHr6XpFUNfMCdI5B9uobJaqMxEAAYiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ed7e49e2.mp4?token=uISzn7QnWUn3TmSRtyiMQewQUN6yeAr08ffVUIsR4XeLqI8oXHU1CJUuZ1biC9CVRa5ACwM-9CJv6Z9yTyrpxwdVVjHNK_dUcppKzsogSkT4Iwtbru5OqFNGCLr7heEbmwnZDWvv86MIdiAcjakdkm3_LALtMp_8LWl90k3U9UU_yGWpfDK_9abIZtZ7gR17auVXab9Heu_e4zc7MT6Vhx_FEGY6wZ4pAubGvH6-0LrBVA-WwHpclZgOwkjbxr-odZFl7qSZUVy0xXb-AHuoRceZEMtgdzVWSQGZsIi4QUm945xYH2MgX-ZiHr6XpFUNfMCdI5B9uobJaqMxEAAYiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
دیشب‌بعدبازی فینال؛
یه خلبان در حالی که کلی مسافر آرژانتینی داشته روآسمون گفته آرژانتین قهرمان شده درحالی که فینالو به اسپانیا باخته بودن و اینا از خدا بی خبر اینطوری خوشحالی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/26173" target="_blank">📅 23:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26172">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d51f33dc.mp4?token=j6mqtSXn_byEG02lilAeNTP35LELGLeBiXcHZbEx44g0xhAfFSJOIepL1rSUJdgaCKP1KEq3XJqlNMg5PvTKijMjJAW5HRFNlohQfrv-ubx6briAua_Kdb7ytrVQolE8mz6qGYenRQkLPNrnbEGJc2BcBXiAZh9Be1nS8MzbLE9gJ8nMMzc5C9n5UIFKip-4BB-Y6n1WPSHl1lT9f9baidFnIw7HKkCJ_YiXcqCR7567um8MvJwyg1_zDrXpqtmLUg8JSaEF6GJwrz3DfVbPS19g4ai0lc2jldwhmVBkuqvLA9LmpWNgQtqRkwELMA6D_y9_PuOAgaJAKxOCQ0TMHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d51f33dc.mp4?token=j6mqtSXn_byEG02lilAeNTP35LELGLeBiXcHZbEx44g0xhAfFSJOIepL1rSUJdgaCKP1KEq3XJqlNMg5PvTKijMjJAW5HRFNlohQfrv-ubx6briAua_Kdb7ytrVQolE8mz6qGYenRQkLPNrnbEGJc2BcBXiAZh9Be1nS8MzbLE9gJ8nMMzc5C9n5UIFKip-4BB-Y6n1WPSHl1lT9f9baidFnIw7HKkCJ_YiXcqCR7567um8MvJwyg1_zDrXpqtmLUg8JSaEF6GJwrz3DfVbPS19g4ai0lc2jldwhmVBkuqvLA9LmpWNgQtqRkwELMA6D_y9_PuOAgaJAKxOCQ0TMHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دیس‌فوق‌سنگین ابوطالب در برنامه ویژه امشب جام‌جهانی به‌قلعه‌نویی: ما تو غار کنار عادل هستیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26172" target="_blank">📅 22:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26171">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddacab4fa0.mp4?token=rHuUUfAmD2sZndMlUlbzgFrdZJFkCCiwaaMYAqEBUgrS7-KNWKShM3hftO53i0K3TZjHXdTFqT25h2QXUoRPkljVCSKHLQFnXscxldP8u0VsZ4BqeVegnPsyBtP1RgWpFaJrSwhcFFoyoP2xIz6nVcrIiSVc_XxFFZgaNLj6077UykbAULdYZ1P9f35Id6yjsHYPx9QigAnE3tHBmv5UiK-lWBmXesZ7p3I0mc4pAe4IjWZnhp6TBdISlyw-P9IF7A_J4QuMIAsOBcIGso-9qA4OG9tpiFBN44C6UZCdTaHigECgljb5FUsbiZfe-wQMxocdLKh_7Sk8wPk-KxejfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddacab4fa0.mp4?token=rHuUUfAmD2sZndMlUlbzgFrdZJFkCCiwaaMYAqEBUgrS7-KNWKShM3hftO53i0K3TZjHXdTFqT25h2QXUoRPkljVCSKHLQFnXscxldP8u0VsZ4BqeVegnPsyBtP1RgWpFaJrSwhcFFoyoP2xIz6nVcrIiSVc_XxFFZgaNLj6077UykbAULdYZ1P9f35Id6yjsHYPx9QigAnE3tHBmv5UiK-lWBmXesZ7p3I0mc4pAe4IjWZnhp6TBdISlyw-P9IF7A_J4QuMIAsOBcIGso-9qA4OG9tpiFBN44C6UZCdTaHigECgljb5FUsbiZfe-wQMxocdLKh_7Sk8wPk-KxejfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اینوقلعه‌نویی‌بشنوه‌دیگه فکر کنم شکایت کنه؛ تیکه فوق سنگین عادل فردوسی پور به قلعه نویی در بازی امشب: آرژانتین بارها تا آستانه حذف رفت. فاصله‌اش با حذف5سانت و 10سانت و 30 سانت بود اما خدا کمکش کرد و موند در این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26171" target="_blank">📅 22:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26170">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22beea35ed.mp4?token=ci6Nsvzmnm5o1tADv0O1TbR43I65u-nxjeQcZaNAAATxu9r4x7lMSM7QGMArwOLegT7Q3GMKzg6nQuOzFdY0MschsU6tKgm9_zk2ho61dh1Tdyf0PbEaSM_x2zgC7D6sKdCmsT2S6X8GoPl3ca3FHnMcOQxNWKRqsgKdmMdVchLXMAhE1wf8WyjG2yrwfOtCtvPtBhLOi51JNWOb5Vj3FE7dEuu_J_VlCSAgFfw9EhBU3eh4nC1z5_I7Y6Ht7EhyQKutXfWam4c40dLauaFAMenBHB2m9zPiGLCnlh6xXwjC5SjRzeyFKz0wmfbZMl3N-JvT5WUcjP6XGYgN4DR-xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22beea35ed.mp4?token=ci6Nsvzmnm5o1tADv0O1TbR43I65u-nxjeQcZaNAAATxu9r4x7lMSM7QGMArwOLegT7Q3GMKzg6nQuOzFdY0MschsU6tKgm9_zk2ho61dh1Tdyf0PbEaSM_x2zgC7D6sKdCmsT2S6X8GoPl3ca3FHnMcOQxNWKRqsgKdmMdVchLXMAhE1wf8WyjG2yrwfOtCtvPtBhLOi51JNWOb5Vj3FE7dEuu_J_VlCSAgFfw9EhBU3eh4nC1z5_I7Y6Ht7EhyQKutXfWam4c40dLauaFAMenBHB2m9zPiGLCnlh6xXwjC5SjRzeyFKz0wmfbZMl3N-JvT5WUcjP6XGYgN4DR-xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه سنگین و کاملا مستقیم علیرضا نیکبخت واحدی به میثاقی درگفتگوامشب خود با ابوطالب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26170" target="_blank">📅 22:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26169">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZsUP0bxygD3dj_DehUNgOkEf5gEbIuY8hGjm9KkENxjqrO1EJFIoghSd1VcVbWPALQx5baw4I7Na7nXUVyKuYi66pGf03B1rRSu-tUG3yLjnVBJ0DAD1QktbfIHkt8Jjsh3lz6WBcyOya10hR7rvYHafMAUBjPF_xgNwtdeqpH_ZaT24iFtCNEIcvckO7O0kBOj38GowTmxhmcBZZ9p7n6mxV89rNIRzL7panzUdqfVvYQMtvUOm7exJFdIyE54Wf6jRwcWQOt4ozO5lvT9aVkZqlsTwBZXamkZDv2HMNnd-xwJhi6kJa-bxCVyhjw5K0sfS2CtYPmIEyGf-Wn-uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
20 ابزارهوش‌مصنوعی درسال 2026؛
بهترین ابزار های هوش مصنوعی در دسته های مختلف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26169" target="_blank">📅 21:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26168">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed6167b3d.mp4?token=NZjPQBiTvXtuUthBky4qmnqFUfLziJVNxuhXYavRi08D8fCOCKz6mKPOcyZtM937e6prYfAdulpUxc2WgQEWpNZXFUeGRU2tmSae8OnOXJufqMqDJ4DIebgpx8zLoiiG5jJRmz4h6pQSUCT4y5O_Y9l9d3dVHO-3boFkFFCYUgpxh86JAf8-E6J-NvQSM0eobh6DgI4F1NH6LrOdsTu3w3V0YHL07AC9FObnHZI-kXZKom2DNAAc3t4TlzeoIuG0iZTciBYRpsUYmA2eQpmHLteCevPWUeLyg4nGy7519GBLe-YFEChVy7zJhZHNJE-uBq6vtv-EZ8EZ1UK7W-qI6IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed6167b3d.mp4?token=NZjPQBiTvXtuUthBky4qmnqFUfLziJVNxuhXYavRi08D8fCOCKz6mKPOcyZtM937e6prYfAdulpUxc2WgQEWpNZXFUeGRU2tmSae8OnOXJufqMqDJ4DIebgpx8zLoiiG5jJRmz4h6pQSUCT4y5O_Y9l9d3dVHO-3boFkFFCYUgpxh86JAf8-E6J-NvQSM0eobh6DgI4F1NH6LrOdsTu3w3V0YHL07AC9FObnHZI-kXZKom2DNAAc3t4TlzeoIuG0iZTciBYRpsUYmA2eQpmHLteCevPWUeLyg4nGy7519GBLe-YFEChVy7zJhZHNJE-uBq6vtv-EZ8EZ1UK7W-qI6IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌ های اسپانیایی: دوست‌ دختر یامال رابطه 5 ساله خودش رو با دوست‌ پسر سابقش به خاطر یه درخواست مسافرت از طرف یامال تموم کرد. گویا قرار بوده ازدواج هم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26168" target="_blank">📅 21:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26167">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9hU7UmvInAXR9KWssy1-8cIrZBc-sJjWwhm5aq6QBzoqawJQryINvBMtvsI-MgMT76kvw8vzl1kelRBycc9JBMbRs6bWCStiu6YDrLNpHbd7_C3u1ocMnChebLZwTnE2pSLr4_y1ZEUzzwuhyqzs4TTPGl-ELSHg44Vma1SaP14Ap7blJufE1DWg7RM_0egK4qOfSTDcyGEvjSPpOLvviTsuaUJbqkqgtcx_TYMGiKbsvgmwPbMpVLsSzi7jJCwVoI8v-AJyjl7QVtuociMXCvoI6l3DiiOaGWtwz0GXv8hCWE-hBbPZKH01-BqvktjGK8-jzQAH8JWTCOeV9zFYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام مدیربرنامه‌های داکنز نازون؛ این بازیکن قراردادش رو با باشگاه استقلال فسخ کرد و‌به‌شکل رسمی از جمع آبی پوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/persiana_Soccer/26167" target="_blank">📅 20:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26166">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vj-nrvwZhrh8LnfqVKIA6vJbZDI8uvxNm2ldHt-5B63VcUbLfEuT9rIQcEjelHMyfjg4y5TSgD_rkbN3hjtBPOI3infQZf5a4sKT4AdHh4AnPr73mzdIHbnGF2PkFw6ZC6HiB2ZTjq3o9VmKQ6E8deoUKFc5t-oR32ffkLO52lpLPaVwt1iM-e9yb5sE9WddKUEpegwVc4ZT7LfmuLgDQff0rH6Sa_eTNYvQr7UeK0rDi2I0K20WLkJE97kScBqGJ5aRoYRuh3wLaqZXBMB5Kgcqw0nz1bSrV_7uAVOXEK3r6hKBQ_5zRsMo79cuzwLgFcWBBizQMEVJpkUsOLMqLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ جدایی داکنز نازون مهاجم خارجی استقلال از جمع آبی‌ها قطعی شد. نازون به مدیریت آبی‌ها اعلام کرده دیگر به ایران باز نخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26166" target="_blank">📅 20:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26165">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhY61v19s8kTRPD10mjx14ZaQ-Kbp3vu1YwWdk5uTiPh3qm2q6BUo1sCMb1nu8T7_axIhFbzSKchJbzmBw4BWGP9KVVF_th51Sb4DO-i9xim1xy7YjrkTRFIc2nRvt5hIKXGtfHTAzK-r_N3u2UW2Rh1B8dhNWUQbqHfNV1YsbGykVcc-1fWhQhg1e9b27aXoLTz3LS13q-3q9DLSv_FpoxycVzBzSh093qvb9nwyKUVSQVCdt4SU5VF9VFs6iWqI5BVE5JjwpVWPyT9D7olaXzZJT4X-MQdB8-q7l9otxS_0kThPGPBzGEy4vENry3UZT-VkXgezZ-F-u2pU_FfNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌اخبار دریافتی رسانه پرشیانا؛ حسین ابرقویی دیگر بازیکنی‌ست‌که به احتمال خیلی زیاد از جمع سرخپوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26165" target="_blank">📅 19:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26164">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gfgdi1zL8BoFHPpDF9Xqdbw93Z4QJzezMLlYp16aeN3seRWj3FZDQz2k6Ve-5QzWDgBDVpU8h6WSVvRLoeZ2k1BgGmQfLmcMoNuvoMjgGgnYyjJFEKtggFH72IIn6DKWzDyPq9RSRwsHlzqZg2NwgFwIK1Z3g-hvjXVAvSbr3XN6ze3MnHX_Hb2OzQ_vwDFiC4dyaDRkxF5ojWuib8iSeQyVwUdktcKPq0n6XYWRQMsLDpiOBTLWl2cE7RyGTcimdC4V8GoFEjH1rcXRMIZD-pNNBZsEJjzuvQx0XYn7nA-Bth9cbxZu79ClLyioh8zQlX94D-jwbQAI9LBcPrqlbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مدیرعامل‌ تیم نساجی امروز صبح به مدیریت پرسپولیس اعلام کرده تا فردا فرصت دارند که 150 میلیاردتومان بابت رضایت نامه دانیال ایری پرداخت کنند تا بندفسخ‌او رو فعال کنند. در غیر این صورت اجازه جدایی به ایری رو نخواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26164" target="_blank">📅 19:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26163">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424844d43d.mp4?token=Qei9q6wcqubAID6oDYPIYofy4rQqIogqHNTZAZahKbgEQ7UQi6n0T09zIhtkbmf_RPLK_iwdVRIBQbjvsuUTsbJzRASw09srF5X3-uNoL2KYcD_D7QkJX-PdaoArlJyhCAQ77xwQ4TsiZvvrGkX481xHFZHL1Vu28lUnbHHe72kZvzQx8WCUxEvB0TX4BhV9-nYKiR_pK0jLvbH9uLSMTbh3ijlLOQPiAOkjXXXDamGUX-JgoxXbPxpfYKtNxz6XNf8FT2b-XrkIsMdqu1gAyxaUQJXl0SMMB6hFlG0iMoMVWcHljYqu8THjM9AulJoUzQjxJBD7mxjxj4MpMMHiFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424844d43d.mp4?token=Qei9q6wcqubAID6oDYPIYofy4rQqIogqHNTZAZahKbgEQ7UQi6n0T09zIhtkbmf_RPLK_iwdVRIBQbjvsuUTsbJzRASw09srF5X3-uNoL2KYcD_D7QkJX-PdaoArlJyhCAQ77xwQ4TsiZvvrGkX481xHFZHL1Vu28lUnbHHe72kZvzQx8WCUxEvB0TX4BhV9-nYKiR_pK0jLvbH9uLSMTbh3ijlLOQPiAOkjXXXDamGUX-JgoxXbPxpfYKtNxz6XNf8FT2b-XrkIsMdqu1gAyxaUQJXl0SMMB6hFlG0iMoMVWcHljYqu8THjM9AulJoUzQjxJBD7mxjxj4MpMMHiFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
خوان کاپدویا فولبک اسپانیا در تیم قهرمان ۲۰۱۰ توییت‌کرده‌که‌توفینال ۲۰۱۰ جلو هلند من یه سکه با خودم بردم گذاشتم یه جایی زیر چمنا برای خوش‌ شانسی و به کوکوریا هم‌گفتم‌همین کاروبکنه امسال.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26163" target="_blank">📅 19:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26162">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckkTmkgJR4V7wcRFKC0u4nh0JpFukV8bkpZDmK2NC0FMl09hLlFo0UjOpdKspoCcwKa3xL8SMBgeHah8u2djWD2sSDN4z6tHSBayx-rWN3RipQJw2-rR8kcjML2jeO3TkttDsnUqeJ8IijzNaLwAutbnnZQMIvXZps9Wuar21BWeqV73dHHjfD_FWCJgHogQsW5kD0XCLWJfpNGOludsF5yKFpUf0oYQ5ZVEIeFhTl6kbEpdW_Wb5ExXjn02cby9FIkI0lTNX6SbTeIPr81oK-Po9xFekSJPwrRH6-6PjVxGB47Lp4UEUXB4J2gENlLNNKkF_skLBaxfZHIYzcS8Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
معنای جامع و کامل کلمه آندرریتد؛ فابیان روییز ستاره‌پاریسن‌ژرمن50 بازی ملی داره و تا حالا شکست‌نخورده توبازیایی‌که‌برای اسپانیا انجام داده.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/26162" target="_blank">📅 19:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26161">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021b11787b.mp4?token=W2yXBcvXJCYHOwwrOmFvvAdTz8RbOyAF2siEuH4X5s7tLCRqcHD69X2Fp9Qwbj44rkEKXPHoqpijcRsCGryI_bD4JGlaxHyq39bW-crI0x61FpY5hUeUuUdSKau3fJbheF4F5wBJChks6IPYFTD6SRWnQRWpgX8cBrUfprObJlI0HOK7gOsS3NZaHD1_o6SfOOnqRkeZfCuGTCv21ksO4SDyRR_MkNWfk0u_0nqMtXi3C6U4mX2iQT2htZeetuJY_EFhXPbO8P5gKKobAhSXulSVVQtAZkh2CgUutkI3pIdTc87XlTIeIsjtnZ9zuGX1N0Tn__Js2ziKtsWid3AiPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021b11787b.mp4?token=W2yXBcvXJCYHOwwrOmFvvAdTz8RbOyAF2siEuH4X5s7tLCRqcHD69X2Fp9Qwbj44rkEKXPHoqpijcRsCGryI_bD4JGlaxHyq39bW-crI0x61FpY5hUeUuUdSKau3fJbheF4F5wBJChks6IPYFTD6SRWnQRWpgX8cBrUfprObJlI0HOK7gOsS3NZaHD1_o6SfOOnqRkeZfCuGTCv21ksO4SDyRR_MkNWfk0u_0nqMtXi3C6U4mX2iQT2htZeetuJY_EFhXPbO8P5gKKobAhSXulSVVQtAZkh2CgUutkI3pIdTc87XlTIeIsjtnZ9zuGX1N0Tn__Js2ziKtsWid3AiPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26161" target="_blank">📅 18:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26159">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522741a6f4.mp4?token=LxUrNnRVQO3uO1jrt8f4lGzWmpNy3Nrtg2-IAzfXQbv6XWiKn5gLfutAN34cUlUU4umNNCWPKz8ESGCcSZAmy5wBuxMqJuPsHzrKprM-2Wc8vxJH_3MuhdL9GwhFeAvvtQGc_vP2nEUuDfx1u1NfgE4zmcbHAy3doyVPKczNJViaAEywXeOMSN3txu9Y2a9Fxdk-iTmwEe5E-HOT7CZArzrVVF-jtfZMIw1IS7npv36riNMbzDs77o3wE7YSxAIlSYh59V2H69LfJqkwJmiixIbuStIVBsEKNTw1F7jdVj-Mw1c23vc3zlgy5fVdByT5-4lvfajPgTAQDJqLdvY6uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522741a6f4.mp4?token=LxUrNnRVQO3uO1jrt8f4lGzWmpNy3Nrtg2-IAzfXQbv6XWiKn5gLfutAN34cUlUU4umNNCWPKz8ESGCcSZAmy5wBuxMqJuPsHzrKprM-2Wc8vxJH_3MuhdL9GwhFeAvvtQGc_vP2nEUuDfx1u1NfgE4zmcbHAy3doyVPKczNJViaAEywXeOMSN3txu9Y2a9Fxdk-iTmwEe5E-HOT7CZArzrVVF-jtfZMIw1IS7npv36riNMbzDs77o3wE7YSxAIlSYh59V2H69LfJqkwJmiixIbuStIVBsEKNTw1F7jdVj-Mw1c23vc3zlgy5fVdByT5-4lvfajPgTAQDJqLdvY6uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی خفن سوسن پرور دربرنامه اخیر قیاسی؛
قیاسی از سوسن خانم پرور میپرسه که کدوم ورزش رو دوست داری؟ میگه ژیمناستیک قیاسی میگه خب چرا؟ سوسن میگه: چون میخوابی پاتو میدی بالا!!!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26159" target="_blank">📅 18:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26157">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219a5ecb02.mp4?token=dD7ZhHoAoYKrj8k8NzKovR2KYzRyTdD7L2kgrWmShRDW1swRKsU5bbxeqDwEBAqB7cBfMuk0FpGSaXkGQjVSYeLi04UBWK-TMKrHyw-MAzMeuxKzt756EaSoxwKt4sqYttZKOLtR0PtoPHAVep9-utrs9d2Sro7gmdm9eBfvO6mLqkMOB7xzwEUwP7z9xtR01IlXrkzbAb7zEVZQ-4gW8QV2dfXaGfoUa3qOqclv0SHS4CIuz2JBMFFhmAV0vXXHLOpXJzWrEMIR5aNYkRun1IqTzZ1ES-OwsIYNvcMSRxMm0vkxOsYGABFo5bmVqcbllAJVT9UbP-JmD_S0cdCV0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219a5ecb02.mp4?token=dD7ZhHoAoYKrj8k8NzKovR2KYzRyTdD7L2kgrWmShRDW1swRKsU5bbxeqDwEBAqB7cBfMuk0FpGSaXkGQjVSYeLi04UBWK-TMKrHyw-MAzMeuxKzt756EaSoxwKt4sqYttZKOLtR0PtoPHAVep9-utrs9d2Sro7gmdm9eBfvO6mLqkMOB7xzwEUwP7z9xtR01IlXrkzbAb7zEVZQ-4gW8QV2dfXaGfoUa3qOqclv0SHS4CIuz2JBMFFhmAV0vXXHLOpXJzWrEMIR5aNYkRun1IqTzZ1ES-OwsIYNvcMSRxMm0vkxOsYGABFo5bmVqcbllAJVT9UbP-JmD_S0cdCV0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترهاوقتی‌امتحان 19.75 میگیرند
🆚
پسرایی که امتحان 0.75 میگیرند و درباره‌اش حرف میزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26157" target="_blank">📅 18:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26156">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbS7BOpMa-tvcNYsWy5zhW9MzII3hxpwNv88JchNlcaUo-Vj0MwAtgwsV-yJfhUO2TxuHwx6TUBHW-kGYejI72gGiqjFoU2ZlzRZm5P0_M5TD6w1zWoN1bezdE1UrRKrTzg_T2YSXRYd5kzTMg1C0OdxKUxyMACwN7qsdeG8MZGXReIOx3uub3CQcAmWVak4yvBLaQS6nwJFsM5zX7LHn4NjJJ0j6CdbqP30VylkxnGKtzBf0y1KGpzJUdLqncRV8E7dIOuq5dKzrDu7aid1UQm6Ij5VSVPdsKa8HAD_UvlPWRqYLOGarGzfErKJPQGIeRCunS632O8pH4wlNzVt9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26156" target="_blank">📅 18:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26155">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlBK5AfnD1qUL7sJUALsb2BOs5WkCL0_n0HORLjThokQmSeo_X6BDvZIIdAHzZtkokzH5zYDEUiNcqeRxMLK6tQyQ2an8pE46OaA0lUzL6L7ewWRqGwpvyi0OvANMbcwX4hgbublLa_m9yicEQgfgfto4fpiSOQStI2Uj865ZRIe578iu61-gTFpLfsONEHcPV6RTL-tU2qEwAYoaH3pGkVjO2uyZ2BaSkNTLsmc_H6Woj1ku-Ulz9EtQfVitdL61yQhqrBQ28E2yV7GCaYeuRpEtWWouu74vvtOTbiZ3yzzwY1FbFQg_JRfK6ZpzfAXj1SThZzHpmD-5BA6E8WPCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پنج روز پیش پرشیانا
🔴
محمد عمری26ساله باحضور درساختمان باشگاه پرسپولیس قراردادش روبه‌مدت‌سه فصل تمدید کرد. حتی مدت‌دقیق‌قراردادش هم گفته بودیم. عمری آفر خوبی داشت ولی تارتار مخالفت کرد اینم موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26155" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26154">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b054f61942.mp4?token=BIjmhSRkblaLLdTITMpopXm-8BVYGmn3DFNc77cQvmFdtL8B2vV8Ts6NCT8X1dhGT0fP76t4uqUEfLB6HlEbc0D2D94ueJ41SgClBWWJL3uw2NzOci7wFSAYT0dUi2cuNPmkHXowOPJTHyFXny2MMmaj0uR4Eec_nixKmqJYurL7LoExU0dRjvqoij0i_zbTuMbN2-8EcBtYCx0FJJnU8hVx2KhMvhe4KMAptwjpfGktwInMXlsPx0493pAxYUUIwJ7yxxIXrRDl8vWPILKyvkEilEG54m48a4U_lhDqE-lfnaF8KHDgl5O1W-BnYDzydEOV9RyEsODDdqqi7XHPJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b054f61942.mp4?token=BIjmhSRkblaLLdTITMpopXm-8BVYGmn3DFNc77cQvmFdtL8B2vV8Ts6NCT8X1dhGT0fP76t4uqUEfLB6HlEbc0D2D94ueJ41SgClBWWJL3uw2NzOci7wFSAYT0dUi2cuNPmkHXowOPJTHyFXny2MMmaj0uR4Eec_nixKmqJYurL7LoExU0dRjvqoij0i_zbTuMbN2-8EcBtYCx0FJJnU8hVx2KhMvhe4KMAptwjpfGktwInMXlsPx0493pAxYUUIwJ7yxxIXrRDl8vWPILKyvkEilEG54m48a4U_lhDqE-lfnaF8KHDgl5O1W-BnYDzydEOV9RyEsODDdqqi7XHPJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
قالبی بسیار زیباوسنگین از فوق ستاره هایی که باعث‌شدند ماهاعاشق‌فوتبال بشیم. چه زود گذشت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26154" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26153">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1819c235ea.mp4?token=DXTT02_ROpNUrGRr-FW-c22yB04h81hE__xV6hc8wEX7C_qyEjFvZIhGUWMeRKUL4F-sbWzM8RhvSNf4vJ0lPVnCf80wQDKdcVfE97g6pOHzImOZrjYRgPYGNyLTvRJt_4h1-PQmDkHq1lyMJsc8ejCz-spOscrv7nuX69TkOoqVJ8hUX3r2ZISdE1-FDuitCcEP-9T6Ec7WvVfuGG2hHvUI4HTrgqO6MBnga5Rk4DLYqC-wOW9MIgNjcvis5i0Z_osNAsXIkDcTgbdhLFMi_lyJYgocPYT_iFf5LckaRP5kcoGONBWZpj3D3FrujlAFS3Vo96Z1QzHATeKEkHMxMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1819c235ea.mp4?token=DXTT02_ROpNUrGRr-FW-c22yB04h81hE__xV6hc8wEX7C_qyEjFvZIhGUWMeRKUL4F-sbWzM8RhvSNf4vJ0lPVnCf80wQDKdcVfE97g6pOHzImOZrjYRgPYGNyLTvRJt_4h1-PQmDkHq1lyMJsc8ejCz-spOscrv7nuX69TkOoqVJ8hUX3r2ZISdE1-FDuitCcEP-9T6Ec7WvVfuGG2hHvUI4HTrgqO6MBnga5Rk4DLYqC-wOW9MIgNjcvis5i0Z_osNAsXIkDcTgbdhLFMi_lyJYgocPYT_iFf5LckaRP5kcoGONBWZpj3D3FrujlAFS3Vo96Z1QzHATeKEkHMxMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
نیکو ویلیامز ستاره‌تیم‌اسپانیابلافاصله بعد از اینکه مدل‌روگرفت به این‌شکل به مادرش تقدیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26153" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26151">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoiArrFJkyv3Zu28Cth3FHUtkDXb_7eymeAVtq1N2XX-ZNRcjQNQFgl4z3CScYShObDAXQLwwiLtYEvA0MAx_TA4Cs0WOWbosoQ3I9g4E4KMyyduv5YXm2aXLqk2tOp08ce3VJY1iOR5Zd1UTLmswyq587FtXsucMn-E1BW-j2m7LK-PQQzFFdHozd8Uv3dVXrFGbWJzXDSQoFsXBUVp0J7ooHWyDIKNLv3LF0pEGL2cQ1VebZ9kFmtY8ar1QTGcI6fKoP8UJOTBqZbB1GuOcsYydYIALK9C_asaJ8QVjkGpTeYhtl5AR0TDwOJa5Ey1xebR-nkQ9idQ8FtJ_XfuNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین بازیکن 6 دوره اخیر جام جهانی؛ زیدان، فورلان، لئو مسی، لوکا مودریچ، لئو مسی و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26151" target="_blank">📅 17:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26150">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aY0sKn9Qqg5TKvzSZ2Yb8dYImHpu_CKSwtx6amtOHAuj0FttahXXlUSmNWperQfrxrSbxsw8L8AMNjf4o6opeCaXFl5NJ8NRraBZAbB1KTlN7Dd2tdJnyi-YysZBdCAoP8nrd4pyXkIsC77tALnLJVoa-tazBN-Sd6KEZdAjdmWiIeVT5ur5ChdRe5bb_FQtE4EtY54Eu8R8KDU3yUAvE5589BUDa-4kJUKtP6H0St1FAeQK00KOEDqK2JNkeZ8UaKicHfpo2r1NhP0_LjHK0wb1pECc_hBXyJWNOqvzHQDotlxrNTZ23yEpsgaFZMvqXaUHKPjePmL01u5h4Ml6Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درحالی که با قهرمانی اسپانیا هیچ گزینه قاطعی برای کسب توپ طلا دیده نمیشود ، فرانس فوتبال در آخرین‌آپدیت‌خود درماه آپریل "عملکرد فردی در تمام مسابقات بزرگ و مهم" را جزو ملاک‌های مهم انتخاب برنده توپ طلا در سال جاری اعلام کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26150" target="_blank">📅 17:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26149">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc40ade6c.mp4?token=m4C_Dm07E9RWFM36UL4bVEv5mS-j8uR6oHEScEpPSlZtXaH0la4UikhQea9IE6GOxNgBG9NqvsbSQh_SJ1_jMVYx--7sBHGTEtj1TbJh-aoP2eH2rGsUwnX_ZlMINu0XOQE5b9QzE3wqAHQSQAFG-oyxDhRh37aNYuxf0KaNLBcKxQMVlJWV-zOsBREG-J9X1_v3dmlA5pds9TdhHndYpkRvE53lVCn87O-IcTGvf3w_-KUt6puJ23gG3qdiCCqzYHdDw_S8fh9nri0BfSfYzeCbey7pP3UINmeYOVQhXYNhoJQeGab3gSqC27oVBOeMKUCjP64cAsbEZWnF-Fp2_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc40ade6c.mp4?token=m4C_Dm07E9RWFM36UL4bVEv5mS-j8uR6oHEScEpPSlZtXaH0la4UikhQea9IE6GOxNgBG9NqvsbSQh_SJ1_jMVYx--7sBHGTEtj1TbJh-aoP2eH2rGsUwnX_ZlMINu0XOQE5b9QzE3wqAHQSQAFG-oyxDhRh37aNYuxf0KaNLBcKxQMVlJWV-zOsBREG-J9X1_v3dmlA5pds9TdhHndYpkRvE53lVCn87O-IcTGvf3w_-KUt6puJ23gG3qdiCCqzYHdDw_S8fh9nri0BfSfYzeCbey7pP3UINmeYOVQhXYNhoJQeGab3gSqC27oVBOeMKUCjP64cAsbEZWnF-Fp2_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام امتحانات نهایی پایه‌های یازدهم و دوازدهم چهار استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، تاآروم‌شدن شرایط لغو و به تعویق افتاد. وضعیت دانش آموزای  بقیه استان های ایران:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26149" target="_blank">📅 17:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26148">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3qspwfxXoqZK4lJHs_K3lyYNXQVZKdKJyNj1eiKnv5TWV55usjEUKem_0NJfmiyP7RoahOF7EwJUVkkbuj5E76w2RyMr-L2gJCxYewg0jjD982fB9S5NFydQ73Lqm0hdSB-kRt3Vm-9HVormZojFzdobU3X8RiiMvEn1PBIquMgCTsiLeU5VLnnm71e4vtfI6TT8wAjEn4juKjfBN7lncn7w-pdG9ehNx2_Gw-MZ0fkyXPWJV3plLep4YqJL8mM6wYx50AJvT6-9htUoX5X6BlETmF3N_mJr4Ka2pRl0jhY5uQsCwwK_juB8CDznhjmOfa0Yip-PuAQKYFZFSMlZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تو نوزادی مسی با اون همه افتخار نشست کونش رو شست. تو دوره نوجوونی‌هم‌یه‌کلی جام با بارسلونا برد. تو 16 سالگی‌قهرمان‌یورو شد. تو 19 سالگی جام جهانی رو برد. این وسط هم بالای 10 تا دوست دختر داشت لاس خشکه میزد. این بشر دیگه از خدا چی میخواد؟ چی روش میشه اصلا…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26148" target="_blank">📅 16:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26147">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdnNYpi1hy6nx0hjqkGbb9CuFUD0x7zA0mSQOUF7dDSqL8jN9xCGschb4bWAdlwvR2_ZPipUjC2_nclvqQIOztBtcpgmZd5WzMR2UfvUcQ7sUp1HNFE5Hkvlo2Nox49zOZ8Mn3g-yfZYHyUpRnTBCrb1bo6yCQDP9P3FXlZkg4xv5aiEjffnPFMhiSJyT87elYr0gU4XGbjWiQDbARI6Qpm9agbCLR7SHkmzwrxB1QYZPN3ecgFV6MEA9z0mc11Da_y8kvLotWRMSwnfJ74xdKFHf-fUIAJFO33ImFL5MtuUzXZZ46O0tTtMQzGSFu211EMFmYGfArtIcOBuEnZf9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتزوری‌درحال‌شخصیت‌گرفتن؛بعدِانتخاب روبرتو مانچینی‌بعنوان‌سرمربی؛حالا پائولو مالدینی اسطوره میلانی‌ها بعنوان‌مدیرفنی تیم‌ملی‌ایتالیا انتخاب سد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26147" target="_blank">📅 16:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26146">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lx1k71FVOOJOp785BvzmHHt5dS9qtQMp0AlvbBPWk4hU85gfjoqB049h0qwwSVqKoPGFeMawfYa1AT_nV8E33oFrYpEhV2B916XgKrUhjdXRl-cKqeD1yLVxseXjFkxRr-xvOV_nsa8mLCadBp5uNhNWxH4xV7_9XH5Xpi7VP71ed1WitgfNJMFamQd7MxVJcQX5UBMG-QFAfcRdmR8zVOXUqiOSOylPtmMy9lwYU3xkzPiNQk7G0TFytOKaq4WC5km8IlGGwWtmgWe0oX3NyE9mvH-0-5NsC56WiWivAGnIu1jzKFpP-O24FwDbsk9_DvEbG63sSXns3znDjkL6ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛بامخالفت‌تارتارسرمربی پرسپولیس جدایی محمد عمری وینگر سرخ ها از این‌ تیم منتفی شد. ضمن‌اینکه محمد عمری برای تمدید قراردادش با باشگاه به مدت سه فصل دیگر به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26146" target="_blank">📅 16:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26144">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B3SUa4ZQkrDBtnmKmAKZ1ot7-OkcvAX7w_DfDZEJrif-URSt0gbfVna8vVVEUh0rcXx61ftKJJL8ICC4xha-gXWPOVGSjTx-razE-0pZ9phSh7gS4-xPuCgYJ3xseBV0EIMd6m8mNHnCr-toscZ4ceEGwoN7StVefZZ8ACcvXtGeXowAJdY1RK4Um4WcUifWa7e2t51UKl6w3VkdG7Jzbyl1WNbIs-IDW5c2oAJIAQFW5DfBR60hyPJMuBBdsQVxTCeotQMJYBbLXQ2at7r7f70_2DGIxNQAJk5hs2moz7Iv8OwmcHM88QkItKWN8IarV0E0siF2NeZpoePzl6hLBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v9gRrvGpH7yIa-GkMM44MFPhYR1iBhd2WUVn5iz5ilPkLbiTYATRB2hxsamvN2msmrfDSBT3YeBJaGxAZmG4Zk1eEdB-ZzndjlgT-yKEP1khtsfiUXvKh4NYOYP14HkWegmBTCR1Zly6SGQecsGG5FLbMDeOVFLvLpSVQWpDexR_Fe23Rx65uFX8a27tSvFKuwbdxN5ws_6Wp-wbNSGV7So60B3EAk7SFWnF1c4TQn4waShWoKTTWDzIx8oIh3I525a1hNxIEdKt3uh2L4mb7BT1JQ_cPbuja-7GWJEdPzzyGEjEEouJPZsPtZoHqJ_chqjpo4-qj7Qwd4CRVevC4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26144" target="_blank">📅 16:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26143">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5tbOEoAihK_oxWQIi7Jz60UGj1eB-gzwXIuZgVLNM6NWtvV36GuJw0X6SAeSWxe6gWtC3-JHkmRW40vYLkytG2ugMDvgB99Ncd7Fqe0E6veyJG3VrsO5eUboLgVNEZquc-mFi5GC4nnObbx0DPh_vSql_jPE0J-NosP15YSgNVzNrGzyM6WT5X94628CiGwkERzRDRtGgP8OjUcBx5PT-Z0RmR5xRMlUMpUFTTcjQzzLltcA4nOtuF1Pmmt5T_WsDoBUYWl0dgBv6aZ1SWQXUdT5xL7W3aul-zHrKVn93FvOR4VRNdh6iUJ_dVCiH9Ck5usOtE1nteaQb7i-frYJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لئونور ملکه‌آینده‌اسپانیا: بی‌محلی به گاوی؟ من اصلا همچین ادمی رو تومراسم‌دیشب ندیدم. بچه‌ها فوق‌العاده‌بودند و یک‌شب‌استثتایی برای تموم مردم اسپانیا ساختند. نمیخوام راجب گذشته حرف بزنم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26143" target="_blank">📅 16:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26142">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJawXuP6w-NnFLW9C932qPpgdwglls7D1qJBsyl3MeH8L6sy3t-mzbT5u6rFco_GbIZw8dr4lADIc1PWTdWvFBzZGtbtHnV4xE6jv9IjMawC9hJ2J6o3Vx5XTTBnP8NVXcRSvRwESRR26XjDvGxULOOHnhXWYn2cM8Ndt2orFmG4AAvl-ZCKRtiUEQx7QaB__uKici_ij49sA0blLw6ql4QsbtWbDwf17D5kSWux0b5h_Xh8oxcYS6KZr2utbemy4MlOupNnI5vN-RejL6DwFuXC4SDCh8C-tiXDwKVbqn70Rq3s76_HDPCLpOx1VFzybVCBYgGKn4UHcgRzH4AfnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال ستاره جوان اسپانیا و دوست دخترش همراه با کاپ قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26142" target="_blank">📅 15:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26141">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4sQ5-25FjHaX8LASVpnfxWK1BUfWS6bSqdJforMXBn3u5lZAm8uhfM1AeMagmVWZDl63FC6Wl9RgJ9jEwVTKsioZoDWXKbQwyJxmoBCUjlEGYpcdrizNbeIb-1sSRYp4fYA7FJJCrCWXS3T8IvTwmdQAscmSOLKBFK8b9CHVUAVvGqe1KpoBwvcBT2kCdXq09dlP-wZa6iiBhu1uA5iR4LcjW4GLxg2xl8UOBAVuFjWiax9-PIi2jBaSpQ5UBuuTxZgGpsigcq8sl_s66TO-xguPCpSsayCfADBjFpYu80vAohAsi-k5NqaZLhp2w-8YdRnVmSzHT_-G9jUYfRMng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26141" target="_blank">📅 15:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26140">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6473e7bf72.mp4?token=QvpOf28FmGUrXe-zemWrUUOsvwJtUzbs-M4iHOVj3jqaGdOKhJ62AqC2GFuQNz_6yRqXLgyGIxByuBHf4_qD_b__flIbQ9kDKswBTqgF-u80rikY35JUIx3uggjaTOlyhzOtw3GbPOpjPgGuMGCPenVDepEeM2M4aBKgI8rhYUz7w__bjVO4KFhaBFYjabXZGNjiPqxG9BHepYmMEPJDJv0PUoAydTCxO4YVLhzdUEkCK33a3Q7x8uG7VBNqIfYdxlfdTdDmDbfbc8KQzRftR4pfyRumiU3ro1k5MpubGUYz8-EYIKMxLyc3S8PDO7dnAk888kPnhmbVMX6Tq1vprQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6473e7bf72.mp4?token=QvpOf28FmGUrXe-zemWrUUOsvwJtUzbs-M4iHOVj3jqaGdOKhJ62AqC2GFuQNz_6yRqXLgyGIxByuBHf4_qD_b__flIbQ9kDKswBTqgF-u80rikY35JUIx3uggjaTOlyhzOtw3GbPOpjPgGuMGCPenVDepEeM2M4aBKgI8rhYUz7w__bjVO4KFhaBFYjabXZGNjiPqxG9BHepYmMEPJDJv0PUoAydTCxO4YVLhzdUEkCK33a3Q7x8uG7VBNqIfYdxlfdTdDmDbfbc8KQzRftR4pfyRumiU3ro1k5MpubGUYz8-EYIKMxLyc3S8PDO7dnAk888kPnhmbVMX6Tq1vprQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس فوق سنگین روزبه حصاری بازیگر مطرح سینما به علیرضا بیرانوند
: اینجا ایرانه چاله میدون نیست. با کشتی گرفتن با بزرگ‌تر از خودمون بزرگ نمیشیم با احترام کردن به بزرگ تر، بزرگ میشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26140" target="_blank">📅 15:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26139">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z72dix-M8utWsKFnNA8qc3fCHug2iS4V31tWdnQUASYzkWl8onwBpdXI-UtIb0GBvPGxRb-laXFrG3abclWvUfjWHztaYio-WEfwPPexeoMnZFoSo1Za3lWQLy3a-Vaw_M-g7Qxo9wdqvbTsSKDBH0dww5KrdIoyUUa2GhN6ut4BC-yqxNvcigK78An6sup5E6NrvdivXJZU0wtZ31f3TFNEB6kE7XsGah2dOHUaLnKzXPqtxCo7rqMgzn2znKl0aRPWO52-qOpSruxZlqAST0sFNVtwXTIHs8ztGI5mHJjG1L6-_oHv9HD10HY4ZMkpX8fU4EE2r3sTfBJfZSxQ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26139" target="_blank">📅 15:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26138">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xz63GH7CbEORf8aWBdqbnCO8To3G5dkrglL-Chq97dMSJeBtq9bBODOXXgbqyCYQFNKTahM1mGqPgIL7bG1jfa5XZ7KbbBTwDbj1Aif4PTrSt0dvXatBS33r7uMRmZaGkiNIN52X6_60BW1ONeYPC0ij0yO7z8fU5ptvLHsy9WY29mnc55MK-rH24KU3aPB58yteR4eQrgg8NbF4tPV64RKMjk0wTiXdefjYc3OoaZhsZdnGVtkYVgCskYKCcdfO2OUJ75sq8euyhdjm1NQIa3LeHTy8OU9WxYH4tX8OadUXIDJjp20_gTNRD-Bgj3UzTAFrHnhKSBKJD3eezfdKMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
آرمین سهرابیان مدافع میانی سابق تیم استقلال باعقدقراردادی دو ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26138" target="_blank">📅 14:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26137">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBeCayXOfZh_g-vZu019qrSZoIhkedYQBesVEvWxgnI6gdzFdQmN5QeVHskR_2Pghb5ZcsfBFsajvMBxdE0WsxIhC_RLrbe40v0KOmm7V1yD7wPtXzijPNKdqS0VYM0inwqqSeSNRipHE5k2x8JxahFfCdZLF-QsnuAaYW5Ik4J_QuTuFsD0oBWA7-fCYx2Btv7qNL0ZeEu-zn95JT2gifrV5qtLnd7NO1MD6fw1oMm8x-3ZPiHoPMA2MDFpTNovndNnJCkB3of6Pk1Mjo3O8pPOmrtP5W0rZHcU3RmV2rIhAGHwmTbSIsOgVmOBxbG7oIkxTMa5x9UJ7-bWgj4myQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام مدیربرنامه‌های عارف غلامی و آرمین سهرابیان در ترانسفر مارکت؛ این دو مدافع میانی از جمع آبی پوشان پایتخت رسما جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26137" target="_blank">📅 14:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26136">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه فینال جام جهانی 2026 شب گذشته عادل فردوسی پور؛ برنامه جذابی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26136" target="_blank">📅 14:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26135">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGoUL2Szeosx5PnT9sxmJLPwJX2tsEhED_MmqjFbqiN6N5Ieefb-HjhXDCeaBniK6FhDUmaafGsB9vM1ei0fpvOWqh1h7UUM1qacQiZSTFrCgYldGhM1-J2UxxodQw2mqUXoBBkrDgJm0zxKbotFMDy3hcPGvcUuuSOiMlkkG5eEnwdLxfs3YKV6lqw9w-zUdcst_4S2OJ30YOZZ8u4IDk-QAbTzfYkK_2o-GMXPGyWLNM6FoXdsoCNjjCoB-U5Em4h3XijvV44gkKcaUo2TFjO8dmOTzFxlSB5h6smfIqojWqJpG-i-snypBdW7hUQMyG56GDReV9Yq0aDvRRM2QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیران هلدینگ خلیج فارس از عملکرد مدیریت‌فعلی باشگاه استقلال به هیچ‌عنوان رضایت ندارد و در هفته پیش تغییرات گسترده‌ای که مدیریت آبی پوشان رخ خواهد داد.
❌
علت نارضایتی هلدینگ بابت هزیته هنگفت برای جذب ستاره های خارجی استقلال در…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26135" target="_blank">📅 13:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26134">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYAWMI77D9J5h5PS1wqbgnAP1dXBfAY0x04r0NVHjLQvAiwAaGOno4LqLlwPONnv643p4GDMpHTlh7hY-HfjQ6Oudz1BbgsGlzahSnRHWRTSK_19u7PSaipNkrgQxkc-0KqaD6actEvEGG4tFr25VhpOKaGdH9sQxmmdFcFXZEI4jXYNPlGssgm11LMRhXXeCPoGjX1CODk1yyd8z2k4jC-qqZj_d8L8Lu2fxGE9WiK4k0FY0hP4iQW5y6Sp7L2u4lU8Efs2mKxLeCfyxuY7UxqZmSF98Y2iCa6zcZbIfZ9C1gS-YMLidwxtjuu_IaWqiuc_SeDdRjPhSjl0r631dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26134" target="_blank">📅 13:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26132">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMSrUpv9M3kXvT1VTGiZqfsgDuVQu9g17BEDb-25x25uVdOqFwCW-jLhBihZ1wxGSlV2miPmEVz8tZFXua5BRTSyZWDQ6CRCjTtIzJpfp3aIetSdrEa-KeM5KPnpDI9j0JWCwH-nu6dWSJHcHrLXsL76aloIoax6x132lwmeTQ6fZlxJG8Yj64Ubk6CnTsYGIf5iMndWrvo-UFCGdQM_MNGZX04TDYL3mNYNknUoSdioSsuP5PK5KE94ojsXvYUOi76PMoY_Tt8GQ03_AkDslma1wk6j4NSCQtPMGYz6Sl51QJUU-TpYaw6vkjXLyrBh_ujHm3BtlhcfVhgQF8fxZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26132" target="_blank">📅 12:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26131">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkrS7eQRb6V88WI7iT9ThWhkOxxKVHuKomKcMpjFyD4_ahKZRI4DaelanMVdXODgE6nPRw7jnF7-DxIGk27aOGbjk0JWTR-4gp52fegNlbn8H1fN140ZlBOQHYbBUzalFPpHyubQoWmcIuChv01dpW20h2hxbTWCnsjd7uttgq6RFCD188h50Z6nnmjy8m8iCS3631VoxG63QmoTUJ0qVBrQcu4Ngn8ktWwftSuwi6GZdZM2djAi-taoZ4hO2pv8Zre-UdsOlmZRFIqs1LE4iDDHizBrYjtvUn-QxKsyoAO2cBRcpcQpEyEvI8bdNe_PyjiQtq9FZA_yEwdsPgb7xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26131" target="_blank">📅 11:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26130">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6HzlTJPIZn0-opg9-qTu900GCIr0-YSDKZpCGjhlZsBiQlMrLjP36gdDm0SNS8H-hnYkdvBsAYXD0g7vVlFxt-nxBukaWybIysqOC5S-Lh2bOTpl9J9iaLxr6hCPgfGvy73XTdMK8czlsfXXGX2Kr_-C_S_QpGVBa5dpFGhiONRh1qhq_tbbfPfv1KN3O-PV0XIsiG45qsnoJmwMAMTz0tX-SO3Pfc-zC01cJIXSCVnQ6MySGmHnVu-HQanbZzNxhcDGDpgGEV-amE_0KfIQxAyXg_mYM5gY-lfh1rECu8ONThkmwW5eDcxtfMaz5pt1c5A6v-pyEI-ckuRWs2VNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26130" target="_blank">📅 11:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26129">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uioaNPkG3CWbR8CUrHxk8W4I_-wEQzFlsxvZqYtX9eUdZeweiyPMhFQtdnQgrZENSwqY1lE-4js0rTS87Tc5tXExu0kP_o1GK7WJav3aARZ1Bgw2dtU3qC_ZrczI1-vFfmRchKqrRjpIwWMgTLw-4OUzNlj-xxclOyQ5CU1Rpc1mY7klNTSkgkg9Px_nLD0T2TLcqyxv2pCoWx6u0If0KQEfmBdMgruOq7kvMpzhNJHKVj6YNDuu_DVCckyBWe4QnvflehpHROwmNwIj7tl9oqWkjiwfyTKh_Wvsh7npTOs5Ao5Dn5n6HexMaXezwZL-57zXgWCbNMMyeOwJw5XBxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#فوری؛ باشگاه پاری‌ سن ژرمن بزودی قرار دادی چهار ساله به فران تورس اسپانیایی تا تابستان 2030امضاخواهد‌کرد. تورس به مدیران‌بارسا اعلام کرده که‌دیگر‌علاقه‌ای به موندن دراین باشگاه ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26129" target="_blank">📅 11:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26128">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202f77d369.mp4?token=EzVPGDyzWBj599KTeFBF9zrqZeX6oDBsgLCWVd4soqMjpqCOXuds7KMqzJo0Jryay_AUxW7-pcjQy-qYXDF1dVJUmf7-WhcrrnPZC5wAXqeYVjqz99Xu_q00_sTDklVEA79sF7PBmYXruzEUm5tdLpxDax-u62N5s66UWJTaf50xYSiLOyFg7WF4gSvdgelQH0qWcAzYya5a-iQg5ot6DiP2YC1MYt-dWqDJSwi5ov6BVtfud6AHYBgYDGgBHLueNV3IJtXqGV5fq11-maZNjTJvzX8cVGrurdd1yCexj5d7t-ZGwW_UIzwF-F_6Rukvtw9x42K1lYKuwGOS764Si0JjhZDAqEjIPX98XmdfJkR2OmD1kIV0VgFCDUgZ94oqBVgfU5JyKnX_OJrdwlLEfxbRxq1z9HYXYUe4KdNXUCu5aADn0V5pNxHKPZT9PtSNUGzRR_OE8Pc0MGoEnvHyfRu818bSx67spWRI7IVWc4AG5g9P4YzeB9UDL4uo-fGbU5X86kx8iU4LADW_XPqHFvEGkq6QhevvOxL9QayTKCcXDUoKkiCZiumQfYVhiD7HUpDaiCve47NUvf9lnNRz7xtmzbkncyNLJ9PuH30oFH57r27yijkYjJxpDJ9AdzJqNyZVylShn1hU7q7XEzm1ih4r9bxApFXAZUz7jT5Ds-8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202f77d369.mp4?token=EzVPGDyzWBj599KTeFBF9zrqZeX6oDBsgLCWVd4soqMjpqCOXuds7KMqzJo0Jryay_AUxW7-pcjQy-qYXDF1dVJUmf7-WhcrrnPZC5wAXqeYVjqz99Xu_q00_sTDklVEA79sF7PBmYXruzEUm5tdLpxDax-u62N5s66UWJTaf50xYSiLOyFg7WF4gSvdgelQH0qWcAzYya5a-iQg5ot6DiP2YC1MYt-dWqDJSwi5ov6BVtfud6AHYBgYDGgBHLueNV3IJtXqGV5fq11-maZNjTJvzX8cVGrurdd1yCexj5d7t-ZGwW_UIzwF-F_6Rukvtw9x42K1lYKuwGOS764Si0JjhZDAqEjIPX98XmdfJkR2OmD1kIV0VgFCDUgZ94oqBVgfU5JyKnX_OJrdwlLEfxbRxq1z9HYXYUe4KdNXUCu5aADn0V5pNxHKPZT9PtSNUGzRR_OE8Pc0MGoEnvHyfRu818bSx67spWRI7IVWc4AG5g9P4YzeB9UDL4uo-fGbU5X86kx8iU4LADW_XPqHFvEGkq6QhevvOxL9QayTKCcXDUoKkiCZiumQfYVhiD7HUpDaiCve47NUvf9lnNRz7xtmzbkncyNLJ9PuH30oFH57r27yijkYjJxpDJ9AdzJqNyZVylShn1hU7q7XEzm1ih4r9bxApFXAZUz7jT5Ds-8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26128" target="_blank">📅 11:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26127">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcAO1kQke0x04Uy6sJpN-VfE0qg0D0Bh68QPKw0Nu9lBIRplZAhKeXt_Tc1NHzYvlUeSY-Vh8WhHQb9UPZ1CEpkAvKRNrJ_ikpiFrGeYOO59JEVcJ8ZYWzDf0zIAj4STXkPVhwhadJ1LB8uhk5tTnLEFlg91hwzWytD3intB46Y1u8Rj1u5zQyUW7-8Mu4C7YD-NvApRHqk14X1puQxAV9tcJ5PAuqQ8O9Rmr48HJ4DFBptrBq546lbtz-1Mj4C_jRVsv78oeZ0zLGDUs7Tt-7jZGTmOqg6-cpcfXLxqUq4B5m91tQAuSeMWklsGXZLu_0liYh5EIy_getl-149FlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
طبق اخبار دریافتی پرشیانا
؛ رضا شکاری وینگر فصل گذشته پرسپولیس دو پیشنهاد از لیگ ستارگان قطر و سوپرلیگ‌بلژیک‌دریافت کرده و به احتمال زیاد درصورت‌توافق‌راهی یکی از این دو لیگ خواهد شد.
‼️
پیش‌تر در روزهای‌اخیررسانه‌ها مدعی شده بودند که شکاری قصد داره به باشگاه استقلال بپیونده اما پیگیری‌ها نشان داد هیچ مذاکره‌ای انجام نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26127" target="_blank">📅 10:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26126">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27dd0a5169.mp4?token=TtTe7SlS5545xBE609xTG_N-s51k1ERlOBrPX6oPPi5dG12HqDUOzvHABoasgNVZZMXQFnbjr6kHFfnAbfToN7F-AvXmgh63tKYGvEsljDiXAtGqmPafxVOIUV2X1PCx8WDOgx-Di2_C0rW5ZWrztfAQKiYcWl8OkdgqAQijwmaArDaecj_i150vyOrrQEceXHwVnm_fcLPmRJzCONVZQ1YYV0LRawf9bozFHJmK3QGiYwg6ZMnFLljtIupldUlyDkMTxKastOH4H9LSNayTabMHIuvt8WCKw-eHClgCF8dnqwbbqU3W0gs2WyeLWtZdwYEEoofJO7SH7SQF3ppHNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27dd0a5169.mp4?token=TtTe7SlS5545xBE609xTG_N-s51k1ERlOBrPX6oPPi5dG12HqDUOzvHABoasgNVZZMXQFnbjr6kHFfnAbfToN7F-AvXmgh63tKYGvEsljDiXAtGqmPafxVOIUV2X1PCx8WDOgx-Di2_C0rW5ZWrztfAQKiYcWl8OkdgqAQijwmaArDaecj_i150vyOrrQEceXHwVnm_fcLPmRJzCONVZQ1YYV0LRawf9bozFHJmK3QGiYwg6ZMnFLljtIupldUlyDkMTxKastOH4H9LSNayTabMHIuvt8WCKw-eHClgCF8dnqwbbqU3W0gs2WyeLWtZdwYEEoofJO7SH7SQF3ppHNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🩵
آپدیت جدید تلگرام دیشب اومد؛
چند تا قابلیت جدید بااستفاده‌از هوش‌مصنوعی اومده. چندتا عکس رو میتونید مثل اینستگرام پست کنید تو یک پست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26126" target="_blank">📅 10:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26125">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a101f8f4.mp4?token=gApBsfbbkadj-ZofDz7W6pOv5AXy4BWduZhkqnRsPaWoNAVdstwar8l9n1kVDUzkq_5ej52RPe73PgIBx5XLWObj58nDKm0HdqktotczzQnc8ZUXrGqixaJef8Cw8LZj6K4uJOgunbcwdJYm1-rVgd2XyPs6_WOhgka2LrBP3hw4xAj1pmcSk9gy7vfQRU1XX6bS-P36PopjQEGC6DfPPniy4BIAjDPb5A_B7leIEA2e-p2Rdu1oEmEd3FUdKbtGIXMqtP57vofqU44XxRX7ZeBTPnGJD8Lud9oMzsijq5uonab40keLV3_bxPKcxm--zXR9aAutX1VbxCwzqufdFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a101f8f4.mp4?token=gApBsfbbkadj-ZofDz7W6pOv5AXy4BWduZhkqnRsPaWoNAVdstwar8l9n1kVDUzkq_5ej52RPe73PgIBx5XLWObj58nDKm0HdqktotczzQnc8ZUXrGqixaJef8Cw8LZj6K4uJOgunbcwdJYm1-rVgd2XyPs6_WOhgka2LrBP3hw4xAj1pmcSk9gy7vfQRU1XX6bS-P36PopjQEGC6DfPPniy4BIAjDPb5A_B7leIEA2e-p2Rdu1oEmEd3FUdKbtGIXMqtP57vofqU44XxRX7ZeBTPnGJD8Lud9oMzsijq5uonab40keLV3_bxPKcxm--zXR9aAutX1VbxCwzqufdFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26125" target="_blank">📅 10:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26124">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1235d344e.mp4?token=FltbhmOck2WzOZZd3xwZnWCTg3UmqCfVAvUjF6EVNqxl7NDOPvXUvZbnburccia7DCeUor0cWbmm1PG2kuYCSR84PZBDKh1VlJKVxFihx7DCc8DrWyWUEihPpNUhpYc8t1nmnhye4vLTBDHV6_DTBiOTMDWTlEcmJAZx9cop9PmNp56JDH9aL9r5okocIjg7X-zpq625xRpgjMTKN6NYKbrQyEu7lLW6b5OFdqomxPo2x_XncpwSEOPVIyEb_lftApRcdljcvta-DFPfQskCiSRhhodbVJa-pwEV5Y8UnMyRecmt8HeM2jDFcDr-8nF8gJ50VTVMzzT0GZ-S1oDR6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1235d344e.mp4?token=FltbhmOck2WzOZZd3xwZnWCTg3UmqCfVAvUjF6EVNqxl7NDOPvXUvZbnburccia7DCeUor0cWbmm1PG2kuYCSR84PZBDKh1VlJKVxFihx7DCc8DrWyWUEihPpNUhpYc8t1nmnhye4vLTBDHV6_DTBiOTMDWTlEcmJAZx9cop9PmNp56JDH9aL9r5okocIjg7X-zpq625xRpgjMTKN6NYKbrQyEu7lLW6b5OFdqomxPo2x_XncpwSEOPVIyEb_lftApRcdljcvta-DFPfQskCiSRhhodbVJa-pwEV5Y8UnMyRecmt8HeM2jDFcDr-8nF8gJ50VTVMzzT0GZ-S1oDR6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد ترامپ‌موقعی‌که‌کاپ‌رومیخواستن ببرن بالا ازپیش بازیکن‌هانمیرفت‌ بره‌ کنار؛ رئیسفیفا اینفانتینو دست ترامپ رو گرفت جدا شه از بازیکن‌ها، جدا نشد وایستاد تاکاپ ببرن بالا؛ فِش فِشه ها اتیش بازی بالای استادیوم چرا آبی بود. قرمزنبود! ازقبل بازی چرا آبی تدارک دیدن!؟ فکر میکردن تیم ملی آرژانتین میبره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26124" target="_blank">📅 10:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26122">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ty6ztuHkjzWkgh6-S-s55hGJ6kgr7n8lEcgbJluYMnb1CqvJh9H_ncaXPKmHmFEJuR9VYtqET1ljOCeU_2QQlsntdTA6iSky5aGXsHUdAFlVna0o4jusEh-L4yCcdPoCKs4Pt8-DAd1xirNwihM1TPnAuT40KqBscuGz5LvERn-1_k4PPS7yljtoVsWtw38Zerh-pcX3RiJ0fwN04aA4m_Nf4NclbRqv7TLS9zAOERlaAmnbAZVueFjSJJt2aBGMIaLW2Y6AGNfSsicbjgV1JJp6mwZN9IL0Qt6t3oZxy3VwUil2A8sDaHVAz2CLhKDDdgcUB4UOqXVxQT7YHxwQcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ldq33wD5Xon6EoKZoIb07f_f2_eSYOQTXCtZo81dcHjIJCXtf1pnKFQbxsCkqGSKalfPP1L0UFe8wV7Y1ir3_zkVfLgCJUmciWQ5mm5ZQeL3c38YWlnAT_LEIgcqF4OTp7ZIghBjqsmnvyhNY-vDsoDaDBIG0dlG35Kqhks5xRP5EMulWUyb_YCaRrSE7qhVbit03AlV4O6AY647d_psroOla0NmtECcASbK9TcFN5lgGvInPUVYK9J8KF-OU5FBY28uzOPb-vzihO2w8P98OdmVscXkFpDwG7Fz-bLUTNB0vNOAqMekkVm40BhrDN2VioHg1PQR-NxdJiExrle7JA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26122" target="_blank">📅 10:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26121">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c071bd0be.mp4?token=evjJic7sOaTxu64GqpnczpZpBgN8amnOeoiZRJ2HZJ-8LK4VnxhI5igsD8Bz1ZJjwCbZsqF6L37m0rz3sLUynpEABdPR63ZbL94f3H7NwbPWPSom4nQtJgWXWUFg2nu0fGsnbHBg9X3vlYZEzy7UydzxhTg1DWMgGIQQOXAUJjlaPIj5LaeHEtON1hktJ4Ux1xsfpUqGPBPAt55RqamU5cq5VC4NA-c46DeuHbYTuUyaNnNblBqNC5WabGwjkO2Nz2_Vmoqcx7e5nig7yh-30FI_fjCB35cbxqeGW_FQ7ZqVsDEYjTMDtzaH8L8aqaCm9M06pnhIwLYWTIRXGHxfNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c071bd0be.mp4?token=evjJic7sOaTxu64GqpnczpZpBgN8amnOeoiZRJ2HZJ-8LK4VnxhI5igsD8Bz1ZJjwCbZsqF6L37m0rz3sLUynpEABdPR63ZbL94f3H7NwbPWPSom4nQtJgWXWUFg2nu0fGsnbHBg9X3vlYZEzy7UydzxhTg1DWMgGIQQOXAUJjlaPIj5LaeHEtON1hktJ4Ux1xsfpUqGPBPAt55RqamU5cq5VC4NA-c46DeuHbYTuUyaNnNblBqNC5WabGwjkO2Nz2_Vmoqcx7e5nig7yh-30FI_fjCB35cbxqeGW_FQ7ZqVsDEYjTMDtzaH8L8aqaCm9M06pnhIwLYWTIRXGHxfNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حماسه‌جدید خیابانی دربرنامه زنده؛ خداحافظی اوس جواد با مسی و میراث مارادونا با شعر مدونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26121" target="_blank">📅 10:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26120">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=Nkmy0d14fAtUdaKtSFRNCq-GxpiPAe0sSTPx9ZvWmj9o1entAmeYFCVqmMojXRovZl_Pl-xqkJVgnoQ2dhM9Py2t5tisDhfx7F2i6ndTUPUp6Nw8chQePRCWIc2UygrHXMXMC7OqIdBcMIq3kDPJ7pIxkdl5V1Fy6Wc4FY07YOLyGteoKhqikFOKa6Ta38ArrmNWJb3sqbByh7NKGDT_HnyjOdh1poGv6EejjjMOoCJL7G6TJ_wmqUuxfoLHTBoARcyDxG9Et55O6-HKr9jVkXBwcupzWlGCRYrnDI-29K6xNVJ9beARl1Vj9ohYngpvBrn-BKI-QLdDrVSuYJF2Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=Nkmy0d14fAtUdaKtSFRNCq-GxpiPAe0sSTPx9ZvWmj9o1entAmeYFCVqmMojXRovZl_Pl-xqkJVgnoQ2dhM9Py2t5tisDhfx7F2i6ndTUPUp6Nw8chQePRCWIc2UygrHXMXMC7OqIdBcMIq3kDPJ7pIxkdl5V1Fy6Wc4FY07YOLyGteoKhqikFOKa6Ta38ArrmNWJb3sqbByh7NKGDT_HnyjOdh1poGv6EejjjMOoCJL7G6TJ_wmqUuxfoLHTBoARcyDxG9Et55O6-HKr9jVkXBwcupzWlGCRYrnDI-29K6xNVJ9beARl1Vj9ohYngpvBrn-BKI-QLdDrVSuYJF2Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
#تکمیلی؛ اینجا دیگه عادل آن‌فایر میشه و خطاب به قلعه نویی میگه من تو جنگ‌های این یک سال اخیر ازتهران‌تکون‌نخوردم ولی‌تویی‌که خودت هرسری فرار میکردی تو ویلات‌نیا ازاین‌حرفای‌عجیب‌وغریب بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26120" target="_blank">📅 03:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26119">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=lxCz7L8fTEXu0rpvTedCdbDp4PAodNcoXO-m0aO3AOznGRwVfKF__YFuU8MPmkaKko2od1HC15sIN0hgqfHPJ9zqzEImZ1_B8nqdaQLdCbTgIB1-BOk5IjdSrTxlQW8QcmnGKZAMkPdzzEu6rqR_P2ht8gGJF3p9fzmMJDGBeCxCQNuD8-cFlIwQy94OPigOgXcl0hKOmujsb4dYrcj5Nt-3vf6CNzTCk-fCSbVRxvEgsppxw98bfWUVsY7_xZ1R5NsfcHcp1_sLDy6TJ0YyZGIZbgLhGvoWv0-mDTNPtMLfW8-z5xoUHukwvKKatPgkooKhDfTSQvu8D2EN0YI0cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=lxCz7L8fTEXu0rpvTedCdbDp4PAodNcoXO-m0aO3AOznGRwVfKF__YFuU8MPmkaKko2od1HC15sIN0hgqfHPJ9zqzEImZ1_B8nqdaQLdCbTgIB1-BOk5IjdSrTxlQW8QcmnGKZAMkPdzzEu6rqR_P2ht8gGJF3p9fzmMJDGBeCxCQNuD8-cFlIwQy94OPigOgXcl0hKOmujsb4dYrcj5Nt-3vf6CNzTCk-fCSbVRxvEgsppxw98bfWUVsY7_xZ1R5NsfcHcp1_sLDy6TJ0YyZGIZbgLhGvoWv0-mDTNPtMLfW8-z5xoUHukwvKKatPgkooKhDfTSQvu8D2EN0YI0cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26119" target="_blank">📅 03:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26118">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=EGepcRTO2EmrwHpyx502ioViWSupWT_QarVgmGqImKHSyu7c2YF_WId_wRQHfe99T6GwzU_sYYRwfKSytL9rBjbN9YzCXx6uwMaOr8uIRAZOqXTVTZW0cvUF3ynqPJkrOQao9DC-msCw-M0JBn0zX1NjtJAhTgSFUabq1xaBGx-IuIkvxsK5kbJ6cLmFqqW6WSh2OmSG5oBqYQiZN8FozWkCHhMcJUtA-91sXzxUnPndcJ4EmeCpC9eWISQWnXGAbfZEg9PwXS0wRXFuLfE0NEtaC9_91LcumtGBydv3b5CrZkqLAA8hiekMnUGUOULsl-3pNRm71oDYlynhP1K_Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=EGepcRTO2EmrwHpyx502ioViWSupWT_QarVgmGqImKHSyu7c2YF_WId_wRQHfe99T6GwzU_sYYRwfKSytL9rBjbN9YzCXx6uwMaOr8uIRAZOqXTVTZW0cvUF3ynqPJkrOQao9DC-msCw-M0JBn0zX1NjtJAhTgSFUabq1xaBGx-IuIkvxsK5kbJ6cLmFqqW6WSh2OmSG5oBqYQiZN8FozWkCHhMcJUtA-91sXzxUnPndcJ4EmeCpC9eWISQWnXGAbfZEg9PwXS0wRXFuLfE0NEtaC9_91LcumtGBydv3b5CrZkqLAA8hiekMnUGUOULsl-3pNRm71oDYlynhP1K_Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26118" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26117">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94e4b0c7b.mp4?token=NhmMrNqm5JIzXKpkCr2X4z5eI7JEqV2ejMzPFNoPI5tS0mhJpuICIuwTaES1KLMX8b9QuSqSU0vhW-EDVL-sMDd5lFMgQYAJ3mts3W1eslNFE50nLpA7PajAV9DqVHYIRQxxtk0nopxu9IP5vx_KblxMqOlBfokJ8sSqA1pmZ9RlrpLy3olLgbZfTkxxTyTR6KTKbb_J6zWlV1lQFc8o98e_ppNHQLWpQ5MXHv04_4c41c9gzB2OK1qWPYb_1JCCcnhECpyJay92i7WXbqUHAkYHwDp2U0YVUOFEBejJJs0VAehaota5fZ1YCUM7JAuXBcvTxA15MJMcqiGtkl_YsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94e4b0c7b.mp4?token=NhmMrNqm5JIzXKpkCr2X4z5eI7JEqV2ejMzPFNoPI5tS0mhJpuICIuwTaES1KLMX8b9QuSqSU0vhW-EDVL-sMDd5lFMgQYAJ3mts3W1eslNFE50nLpA7PajAV9DqVHYIRQxxtk0nopxu9IP5vx_KblxMqOlBfokJ8sSqA1pmZ9RlrpLy3olLgbZfTkxxTyTR6KTKbb_J6zWlV1lQFc8o98e_ppNHQLWpQ5MXHv04_4c41c9gzB2OK1qWPYb_1JCCcnhECpyJay92i7WXbqUHAkYHwDp2U0YVUOFEBejJJs0VAehaota5fZ1YCUM7JAuXBcvTxA15MJMcqiGtkl_YsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نسل‌جدیدعلاقمندان‌به‌فوتبال:اینادقیقاکی بودن که بازی اسپانیا
🆚
آرژانتین روداشتن نگاه میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26117" target="_blank">📅 02:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26116">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e72188ac69.mp4?token=l9ugM2HqYDvNX7GkdSqzx19b8r1b_pZT2MkT3T_H_Os1DYwiVuN00Y4zIBpS0rsEvpXmIdgiboocDhvaXibJq5MwJrVUDkm3uSEY97oHQU2MfpiOJSt-oRq_5iNab7rbJg5CCZxsvmsa9S-LAGkHeVtM0WHtQnTuhsQ_1y_AY_yhi7N9Yg47Rg5KqUCQRNN1Mkoe3bfdErgYBDn2jvtxzPbOJxYyoxKXbjBP-9Og6TiwDlWzRpjCQPdPJ-eylQofvkycLIaespq21LhcjortQZLnM2bzFA0nbooZnkm7yQpqCc9pdBEj5sNMLT-S4qux3rQBN0y0lWPFDa4BY4A2wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e72188ac69.mp4?token=l9ugM2HqYDvNX7GkdSqzx19b8r1b_pZT2MkT3T_H_Os1DYwiVuN00Y4zIBpS0rsEvpXmIdgiboocDhvaXibJq5MwJrVUDkm3uSEY97oHQU2MfpiOJSt-oRq_5iNab7rbJg5CCZxsvmsa9S-LAGkHeVtM0WHtQnTuhsQ_1y_AY_yhi7N9Yg47Rg5KqUCQRNN1Mkoe3bfdErgYBDn2jvtxzPbOJxYyoxKXbjBP-9Og6TiwDlWzRpjCQPdPJ-eylQofvkycLIaespq21LhcjortQZLnM2bzFA0nbooZnkm7yQpqCc9pdBEj5sNMLT-S4qux3rQBN0y0lWPFDa4BY4A2wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نسل‌جدیدعلاقمندان‌به‌فوتبال:
اینادقیقاکی بودن که بازی اسپانیا
🆚
آرژانتین روداشتن نگاه میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26116" target="_blank">📅 02:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26114">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWFPhA_KKvEvpXPusCs1Rz3extMT_qeZEsx42VJtrsPki1a9UEI3veqfoXN_oKgzl5wwYvjJGcpLbuXCPHP-zd97Watvqb17bER0jwko_BcjovX18CR9j4Xp6ZohDm9LqIWbHtuYI12iIrRpkcNgB5PjoBr3cbhNFA-fB4AVt101Qo6JzgwYmm_VE1WCmPy0Q5pQ0Ktvxgy6IRtULuUytQT6CkDZDyT6N8VkCZFjpoRGRq5ohjZmEHxQwFDQDGHVQRELlckvQlWF8BMnVQTjtMjFB5p8eQXMFMycJKskt2OrimMjkS5CSZpD6wp5GOb0Mtj7_YHvhbkh6JCkjKp2BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛ سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26114" target="_blank">📅 02:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26113">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-oAoJUgDsemnLS-rwdjWereyR-V3mXHiYfZrkC_lKfnk11JrzPF9r4-kAclGDlUjAhj0iQLrXsSnF91-a1FVptP8vaBV3uS6WoHIup2OGAemhlstZ0AWqkJv8FRmx5cGhFPV7N8zcAJmgxUQrim1XH8hJ0a9TFu6tmY2ZrwOMkYLqQBi3EBKdJHBlZtHQBsXGKIDSUy7TYAZpfGVgT_XCJtz5WZLuc6YDQL5hqsP6-O4SQw7RSr0Sr4GvDf-biwHAYQpW6Dlqq2_2msu8Jg1mt1zQqw7b3aPRQTevtKvyIwS9R1ZHSUtDGcrknhLHZ6yk3DGGZKCHQxCwwXtuMbMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26113" target="_blank">📅 02:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26112">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzFpOde2rpOAtfeGB1iM0iaEfsTfpNMyD9dSGOFc8Jq1q4xZl4U5rmUwgY4F03D8tObMNWRxHbKORyn_V4AtbLQm8fipup7l2-qy-mjN38iEuvz8SsPsy-mfQjcftGuAU5vSxLlZH-ahMqlW9phXrran76Gjj2zJ8FIu1rqNxZ4N96odKJVljYXvs4fzQ9TsBAw3_NWTOPdUemBRz43X0CK5UO3ZtVIuSs8SqPky6bMN4HN9WlkuF2OTS1e7Z88sZ7-f9T0SCPxJSMQn6WOSWrQoG7OVri3FtfF5fr-UsyGhl8Lgy45NTPgt0DUSeNpQB_tCsEJ9AHwyCTLBxskLvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فکت؛باحذف انگلیس،ایران، اسپانیا و آرژانتین تنها تیم‌های شکست‌ناپذیرجام‌جهانی هستند! اسپانیا و آرژانتین بدبخت باید تا آخرین نفس برای قهرمانی بجنگند، اما ایران؟! ایران یک مأموریت مهم‌تر دارد؛ حفظ رکورد شکست‌ ناپذیری! دو تیم برای بالا بردن جام‌جهانی میدوند…</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26112" target="_blank">📅 02:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26111">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_rDJMNIP_DoEECNHIrxxRkmydVt8WHCOa5_aBLgklMq8D0jA2p2WaJcu9FsdM8vEjtm7FU3n2_wpwTZo2fjeGbYDvzAvq1S524jkArNaJcU_mWlbmfzkZL05KYc0ZhmLXKbvBtmdCDIvBtfYzwJ5fL-V5_C8m5ney_j3YLafdE3xcej7sJl0a7VysBVKNw2v-JxXZUnrM7KH46JTMBIhg2zQt4rA6q6orlIa6Ei6b9tWEznBtpOrnfYxlBGf9wX6y79TjOxC0Ww-R8Xf4N4Ecq012Pdv1LSbF15SB9JbPqojMrlibGhp_W2oL_C6VpdymRYMCX90MVFQeg-S62i5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با عدم گلزنی لیونل مسی در فینال؛ کیلیان امباپه با 10 گل‌زده آقای گل‌ جام‌جهانی 2026 شد. همچنین امباپه با 22 گل‌زده‌لقب‌بهترین گلزن‌تاریخ رقابت های جام جهانی رو دوره بعدی مسابقات از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26111" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26110">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7TeD-57_XvAbIbPWRxVKUFbR-KEEXmQqeFaA99_e3LMtUt2NNDXiRNSaOd14HaMOyh8edl4NIWnqq4niuijfX8nd5QRNMyqaVHrUoCLL0WKsZQJszit3W8j2IneUQ2QwJmeV0EjnfODPFaM4denWnopQYRobqlQYWDOCFLm46ZX7c_pISrdLCaEkb5byMmfZqHBIONWLCiGST5yD-NK2v7mew0XdiQeFIfC0fy4TGHl44rfWia3kqn-tuQTS0HOrW5xwiQdxbcPdeb0yv1yisqJz7SNl7cK-AY48TVDBsOB0lehMmeVjCiaZuhlvz64cqrXW1GPCG4oUEUgZl-n-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
پایان جام‌جهانی 2026 باقهرمانی اسپانیایی‌ها و گل نجات‌بخش فران تورس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26110" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26109">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq7DsN07wAUhv0jKO7FyLQR8s4j6YKq_8IrN69mA4_LJKVcqG_QPp3c3D4lBVgiCur2S2pYqN7IXDiTGFTL1j7oa7eRxU_-Izxa6tHk91aoiH4avox84Ma4XLkZeFCXEGyKVkEY69b_P2igMNLSaqPumznKf1IzPbtwljyHiLCk7J2rpcqj51PYblpKmCxsxr-YMkuRYtt9xELLexqQcuL3LQ19AsAtrtzYLTTv_uak8dN_xjNgRaGJBwezWp64o5-7s0Ww8kg8rBfU2EVOuP8LGrdmTO4FYZ636o2xGJhMz_cMlDgpf1pTKTslF69Onm6-mtGiuo9HAF0Mdhagazg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرژانتین وقتی فینال رو به‌اسپانیایی‌ها باخت که دریک رپر کانادایی روبرد آرژانتین شرط بسته بود. او در این جام جهانی روی هم 10 میلیون دلار باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26109" target="_blank">📅 01:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26108">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJXOAB88JFxMicGCJP13nF_YzR1c9Tqbz1Tfej2HaMogx7r5_rePvnwLu1tAdnIug_vpiTnxFjv2ZG_J08vVxtFMhRyfKbZRSJCEyb8hnJ3MlbCswNJ0bn60zQTNpGjd58CkuU7H6ZyYqbRbgq-bV7NUQPvrL944yDI0ghX21PfVg5A5yEWNDhQAf2AsaqYAW-Lw9-RID_7PNdlxE_KMySrRmZRiUr17ZN5MGpQ0Bw65-die3SpUhWlJgcAWtunSBE19CJ8I7u2KXRpDP37DRHtd9CtePcV_Jga2ffXaiSXbbnhcq6NM-LZODJVTs7HdpUh6dAJKTRPJ_vaZes4a0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید بلینگهام هم اومد:) فینال هم یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26108" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26106">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d433l8xPAGWsM_TzQZiA5kU2Xc3_la7CVs6IXseN063ypxjyB8DUGIa5MluWXUJeKE7aIgB6TfsAiatnpVodThDy-juZXUsaMOC2uAYU-DyuigDp79gzbIsYQlxc4R_kRgup1BNOlqYtqMnIx5l6yxpFBPYwRU--lFku-qMU-qXoXmesMhv-xV0l90j18gJXZZ_5F4GtJUQ-N2B69n9qeiIJ3zvDvMzsrLHvmq_MHuhxj93eYQpibpphe8t7nQDXufV9LAObZLMGjErZSLLCJ47602PA0WSbVlmFeo92iGmyQxx9VApZkWbueq3EzSL7q5v5k5-A5Keks-MvdA6qmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26106" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26105">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRIEj1EgxvkmwdOsQG_ffCBVz31oyagGuBa4IPSU1coW8_Lb2_Ft09Pqba_EMtuhxN-d3N2yIIa5pHEGgHyh6J3XOkFiVUsJlfKbaZlasoqHW0mFGcmjuU_ws-qAsV0Q-7I5O5Q75ZJ9YLRD9uzu7i78aQFKxX93Ec3c0jpOkBWqcMWOWRBhNrgGMKHFnSb0rQabn4jGw24hGSRDLR3ZybPcnNcXsaFxbSJAhIIA3aK91p6c3YFi4j3P1FEjS8FT5Ctl8xaAYtFGeu0GUhF8qIs6MAplacwqpS6Rm0afpKSoyRJ9Al0HfZzEB_KR9OILZsCQjzhyd8IWL_Fzv4f7Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26105" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
