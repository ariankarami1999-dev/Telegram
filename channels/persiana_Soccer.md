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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 13:46:06</div>
<hr>

<div class="tg-post" id="msg-26209">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jmr8SUKSZzD4C7jz96gTJH_SoQYp_umuCphZqfuaclyDfte6DAv9lnFE1pYJECsf7fU-Fh74jIS4EHegBEUgNaLO5m3bYHFY17jkxUjXwVCpMpFpr24Pzu8lQ6O7jK5Y9sBLxuBoz4y2AOx-PJUGvLTO2lv1RF1Eb8ygjIzEhHMFvInKHo4bmzaHJuBEvF-un9f9oe4HYCl4-og6Wp27tUVgofpZ1T11HUQINcP0H9u7CtZBPvuMSU1rg_QnOrtsubbJQgwjuxXBe4rRW4iD-nxODMlDgb43la_QQKM3iQJXBHmt-8wKx68uLwU5j8caN4QSQePDE5-LiQfS2Qt2Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری
؛
رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/persiana_Soccer/26209" target="_blank">📅 13:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26208">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJCdgnAvmv71M89troUfZK8qfO9qcbrc-IutRU_lKDDF2iQ3T7yBfH_lk5KUzjRTonFnIU9zLDrGF-exX3s6nEcfQV_fsisZy_SFBym-6f2FNgLrT8D6IHzfIDASQdF987tTZHb7j9a0X9P55U1dGvTf-6e161OPSyYNQXxJWfc6hbi-oxD0rXIk4V7W-E_aK_sNAqNgXLK4-5QBgAAFQkefGD9WlKBbsTgZiWeYOWWYV3Z--jfGGpQJmQRJU8W5B19FZQH_bF0RLqeBm0UVu7gfKjaaxb1x_fGc5B-_fH2GqHZCPwD77S2EzXDkI56vTnlA--8dRW7pwd44OhEQsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 10 روز پیش پرشیانا
🔵
بهرام گودرزی مدافع‌چپ‌فصل‌قبل آلومینیوم اراک باعقد قراردادی پنج ساله رسما به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/26208" target="_blank">📅 13:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26207">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVfb-83ruLyvuJ-SVkGNsq5VIwkfaP9OwXkSmPeiDUm2xZNAbMQN819kP051juS8yUNwtIW7Ayy95tOf-YX4pQOg6ComrtPhtAaoIQrIYfih2W1lZPw79KFQnRPnY7RItY5k38n8qM-aZfR3GSzXWCUhE7SWHKcvdDg6nJr0UyQhvb3HEV_Jrp00PU8X74R938UVeaxvfOWVwwzAvw9eP8KeSy6iEJT_1mLG8gi4tp2N-fMdbUn1EXWKAuXAHTebO4Ouwjn_UXvZ3ffdYmSdqhpwyOOC-8BEyo2t8HZW67olxbCrVuUJrc9kUlrwuPt45ZORaCmlj9BKhWxifBLL6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیران هلدینگ خلیج فارس از عملکرد مدیریت‌فعلی باشگاه استقلال به هیچ‌عنوان رضایت ندارد و در هفته پیش تغییرات گسترده‌ای که مدیریت آبی پوشان رخ خواهد داد.
❌
علت نارضایتی هلدینگ بابت هزیته هنگفت برای جذب ستاره های خارجی استقلال در…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/persiana_Soccer/26207" target="_blank">📅 13:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26206">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZzlTbMTZA2M10pK8f3BthNO1QnP07TaCK3qsgp0sVbKTbRqxL1odWvgPbWoL6t7qCj99grzgRvUWj4c45ipqsnpa29GVpTKq_rBHWmP0fmZjdwzBmFiHk1xZOT_JXGO_zBZV2Fypk1eMeHJcK3Aq_SIzvbZXdPCNGbOfaNiRcEgQxYGjSRWEtxul-MzYk2-gcObPmvRN1UWpTL7PxTjnrvk2SPT8Vx5fXq08B9Hrf8HsybAsOa7dITYzA8zHU3_zK3AlyQCB9AeaInWwtYlpxPYz2ghkSqjCutNiKcmv8LaHTqYjb8np-_ehMhFao7ZqdE-tRo1B43qkCO4ZO-itA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ حمید مطهری به مدیریت باشگاه فولاد خوزستان اعلام با هییچ رقمی ابوالفضل رزاق پور رو به پرسپولیس نخواهد داد. مدیریت فولاد به پرسپولیسی‌هااعلام‌کرده بود اگه‌مطهری اوکی بدهد این‌بازیکن رو با دریافت 80 میلیارد بهتون میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/26206" target="_blank">📅 12:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26205">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSl5fW67J3sgzFsIcZz7SqqNbBP2M7OvfQ-0iaODasNstv_wgc3Ia-DvxO98Sdm4ZbMizoZi2nzjV9fc41jFeNo1991OLa6LgOpSyK7miJLf0wQUJkYPmfAoIf-OM2y57kev4lleEc2lcjAXxCTwo8Bkm5CjwE67PCZlmsMjFQbOBquMyPCL3bhvf1qHpPi_26qJODvMuZC7LkUmM51I-NYRrpkQEcTwkd7iPGTZTC1WGAI14oi5tLn_kJzyAX9ux-9-E6F8PyRrIG9SjaqkSWV0eiesoEMwBSe1qkx4jcwkz3h-3CPF5-YqNRGY7QI1MKpBIzQ1OHfIGbqo8lWDMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/26205" target="_blank">📅 12:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26204">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">▶️
هایلایتی‌ازعملکرد بهرام‌گودرزی مدافع‌چپ جدید تیم استقلال در فصل گذشته رقابت‌ های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/26204" target="_blank">📅 11:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26203">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kq5NwEP_f4tg5TxCJFqBj_ddue0iQiEBKXigLaAzY5Sev9JKhfluUCYiYCbC905UCNBQn3IieSBFMx9emDePPqrg9IR1tWJv72b1tpHzm7C1kBERHiu6FYQZ2r5sBuaw98f0L-pB5dLxV6SxyqbMUCQjU7mOGHUQ1a_odZ46Dpa6u1dOAAsS5Sqy81CVI5LoCpuOHw7flFhjrXQfQvqf2yoA23QcCxdAaWfEDv9zgTPtyRT_AVfABhxcfo0251LAP8UGlhQS455_hMQWCJAjPt75CaBNVnZYhwwTfkdaj4QpL1TGZHzsw20QvRftr2fgGjSYVNolYKVPZLjU5G2T5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/26203" target="_blank">📅 11:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26202">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/26202" target="_blank">📅 11:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26201">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mar34L5ZORXaufR1tn8lIIPL0Mk5IfRHQdVPAXSggyGeFd-mVTuG68K2hkkS8iOfZeFlnkAJaHFtAQRDj9nnMCzENNifgwIu3saveGGjVZD1ZyLfD_dQ5L2sneOh52rbzzJhC--NDRtDH5HTVyUDshWTm-rrhXTUQtpis_kShVRDWuPwTE_a_-ODC_kwv0MzAxB2FCEFf_1UMsNsQpq1K-VNnD5j1YyfH-eLREKLGb7IooAHIAVSwnqe-M4_y2kL_-aDzOuNLPqbT1aPR3lEQmcilMBhQcxaviJrn575m2zKxbCKPOTEKKpaL5izPEBtloquw9JxwY0qVCLwx0Wf5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد محمدی مدافع‌چپ‌فصل‌گذشته پرسپولیس باعدم تمدیدقراردادش با سرخ‌ها با عقد قراردادی یک و نیم ساله به مکس لاین ویتبسک بلاروس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/26201" target="_blank">📅 11:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26200">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-Ov1K8U2sr_vkMmvgYCmWDt8QNS86cO17HmZwtozmbbS_zztZDBF7B0ZBpe9XOcEM_fJt2QlpAkRpBPc2lQ_gaaHlVeLhpVnZrP6-MValRrtM7RGNhcUtJfCDHAT6YXoUwta5YwA6eUHFihuqNe-Ga1oGJudo9acEa3lJ0cOziA1ENmKYf20BnSf1Vgm1sq1x9y4Zi5n-Gk8WoOr7wMW41lxUPw0n7zV9y-w0BrtjpWVI8N6pYljy33xQ5sDmfhteiBMOUFOInF2jiLS-wRLDJhiVOUJK-ibfR8GsNZUSZNpEsFX4gm15yL5Hrp6XKpm_hAsYWj3OuDuGlZhT3gQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
علی تاجرنیا باز هم تاکید کرد: انشالله تا آخر همین هفته پنجره باشگاه استقلال باز خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/26200" target="_blank">📅 10:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26199">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jht8nLq_RcXzCut9ZBoTnEPrK7l3K4HIcbHeNEbGgHqx59IVyiqK1YwqvM_3x0G6KeavW2rjPpCv-Ayk7S2UOL_bmuBoWUhFjTo5_1Ay0zTz0AO2C0u-j4KPaCUHX1q7Meb9kotsPtNALr9RIXlabIJjzppNazcOSTSWy4ThfQdlpN4Jc1xhgyXfhe1Gs_F_rKEGr2tCAFCHRYzjTJjJ_ueYuk2in7__aI62gYQNbsJRQKLmTs9NPzu9AKW-VQ71Bf7NqG5ft747eZysHfolBJf4pwtF4u_v0ViLvZkp5Fs5IxkWA-L30xNA6gU3OrhalLoFNaaZytzU1MWAzSnX8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛
لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/26199" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26198">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/26198" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26197">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/26197" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26196">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESLGO6g75P09C3Wl1XsX4fNGyMNqM0RfNEY3UPjWvVAs27bUpKB3AYZrHL-J1YeDZjLMQ8hdZ-oKT76u-ViHA7qKO3XH8ilyJn63pytOvsTi7PmHiaoyo7mg9HCzoQfc0AZgBPBgzOW9q9o4HNAZv1d0pru9hefMt3988BGn4r6ZAAFI_tm3pz6WMWSAR084i3-6k7hhLxHYLBbxYlgjtP5a2TvSjiPGthdAxNeDYm6JOJZCU5CNGYlIWAfK1Y5qvHOioogIVAHgchbWAMIdoUd6aZ0Fw7xDFIwqi7kwxyevthopeETQhmlB28hMOiUg2gJ7t6st2-xnIdj9Sy1Juw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برسه دست مجری صداوسیما؛ تیکه‌ سنگین رضا جاودانی به میثاقی در گفتگو شب گذشته با عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/26196" target="_blank">📅 10:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26195">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xnl9ymVkSXNfGTYR5mOVOLFT3oK4Iw7Pm8Pz_pa23Sh05bq7wNkne3VEcltpp4JakYGm-dsJDGeW5x-8CBHrLANEPpnvH7yL0FfEkoJsW8_tGe0MRBlpK7GOoL3nmXeRUrewWEhuY30bHk1hhVCN9vssc0oqJsxxTfi1koP601ccQYHeZWFLx6YSTneRW1YA_GumKT8kyZAXFPddePoo05BJeUtBgcASdyLVUUIHvhyDwZAOD0CQCMjrRnxSNRKGGMNaPwGjnCklAh0HVKoJazoK5fzvXcz54pG4EL6KFaUCBS6vEr_6smB64353qQN8kapjSvWyG9WLw7mQGGkuEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛پرسپولیسی‌ها برای‌جذب ابوالفضل رزاق پور مدافع چپ فولاد خوزستان با مدیریت این باشگاه تماس‌گرفته‌اند که گرشاسبی به حدادی اعلام کرده درصورت موافقت‌کادرفنی‌رضایت‌نامه رزاق‌پور روبا دریافت 80 میلیارد تومان براتون صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/26195" target="_blank">📅 09:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26193">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/26193" target="_blank">📅 09:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26192">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/26192" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26191">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/26191" target="_blank">📅 08:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26190">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgE1B2K4jRhI-I3Uazx8lqbYXR_oL_zmUfkQnTDLeSbkat2PohzUAZWfIKcNbwrfh7r9jMFJd2ZJsfbhNiQI5qlfM2Cx6BDcs3dMCu6hWzetONFjYlaM-Yk-C3xojAstQ0f_sRcoXgHjdfeIuQoCloHkKc9iVQMvFqJirnxpa3exFd1RiAGfo32pPS8t3ET-hW7GCucQ5CrbbgW9U8AoPGGk3L89O6VPRy7NtqBwB692nSQ3DGue8AONarV1Y5uGdbJcPjQdjiZBgWj3vMe-wbzNzD347A6lBM1QQR3HdXEPZ5gheFrs9BNqbdCZYf8eqSWu1FNrV_tW4FW2JUIetQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/26190" target="_blank">📅 08:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26189">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXvrIbvtEfR_MxshQhDWRAIsMcgAy3lzwZn9LGLpvVf9Vuqo2pZW55z3JvNedm4kykWW_NiTxQlL_W1IC67UxlXgRNKFtb2tm-2xzFP8MKuDS0v34vSaPcrGoYVrn9cVlsy_xrFo_ZUSBYMs9vCiErqiz-9mRvoPRF4MoTzJqplaUWCA-iEYjWfOFNF5KtXSDFlKW9r7Qn6z3wKjczuieuguslVEms09xTe-JL7DFTOh7Fma-5ja0KgaSIGY7TH2Eq_Dwn1Qsi6xPytzBBp86_-3R9ouZ1Aa1b2fSQfQlz5ioYRy7Au41lduAdD_xxknOY_OPicG6IZFf9-rWbZQWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/26189" target="_blank">📅 08:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26188">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26188" target="_blank">📅 01:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26187">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e8c2669f2.mp4?token=UlQrDwEj42bilEpGFmy52tjcLF98sPfPuXhnzlxwcYa2Dlmb_rUwQHMQrcM-a6PYAQW7zHJUL81ROsIvHrfPthb9r1NbalGqZ9GiOV1FJwUh5sEz3lNdQzkhk4fqcaglHPR62mqyZkf5f3e2-BqXz9UMExkSoTBmLF5riGztJhlZzRzWhWMpH57jVvZEOspYAWAIvY4S4jPQRGQyii7xAd5V5JvQ1YN9hZp9vY9pg5c6nupB2cGaV_EkUoei1SykvjNX5OPYJEztapmwLmjg3VPfoVsQnwmHb5xLrXK54ZfQCdo_oZluHn0o_xe3AM1oD3iDIcwUT7eRe2bAQE09vnD4gJEYvjY7xETJGo33ZbXHlqbaAYZb7npUla4_kpW-hOc1YPGeXAUjRiurNgPyusWhyfFg_KCwchGD6o_vXOr7nFPqWjDAyFbJBB0UauGIqZcv6weHHyGTnbQMQIBow0UY2b7EbK1b0uoUlFxtv4YXGOSLr6nWrEKUuDHWGZbuqosQLBDsEUAoiEPHyOtHW5fUeF5pzoYxLSSdakslyxgl89hIPwoWmezazrNECvNPdlEbPjI4bJqUlISh9r13VP8Ycc8hhggwF7SEOCraEeoDA2df3NxVo8YiNdGYGHnlSvDNlHuinTPtpXTpzlnNbBIJ0y56_P4YWwdYMHhc2GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e8c2669f2.mp4?token=UlQrDwEj42bilEpGFmy52tjcLF98sPfPuXhnzlxwcYa2Dlmb_rUwQHMQrcM-a6PYAQW7zHJUL81ROsIvHrfPthb9r1NbalGqZ9GiOV1FJwUh5sEz3lNdQzkhk4fqcaglHPR62mqyZkf5f3e2-BqXz9UMExkSoTBmLF5riGztJhlZzRzWhWMpH57jVvZEOspYAWAIvY4S4jPQRGQyii7xAd5V5JvQ1YN9hZp9vY9pg5c6nupB2cGaV_EkUoei1SykvjNX5OPYJEztapmwLmjg3VPfoVsQnwmHb5xLrXK54ZfQCdo_oZluHn0o_xe3AM1oD3iDIcwUT7eRe2bAQE09vnD4gJEYvjY7xETJGo33ZbXHlqbaAYZb7npUla4_kpW-hOc1YPGeXAUjRiurNgPyusWhyfFg_KCwchGD6o_vXOr7nFPqWjDAyFbJBB0UauGIqZcv6weHHyGTnbQMQIBow0UY2b7EbK1b0uoUlFxtv4YXGOSLr6nWrEKUuDHWGZbuqosQLBDsEUAoiEPHyOtHW5fUeF5pzoYxLSSdakslyxgl89hIPwoWmezazrNECvNPdlEbPjI4bJqUlISh9r13VP8Ycc8hhggwF7SEOCraEeoDA2df3NxVo8YiNdGYGHnlSvDNlHuinTPtpXTpzlnNbBIJ0y56_P4YWwdYMHhc2GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
اشک‌های تلخ عادل خان درویژه برنامه امشب؛ مردی که پیشنهادهای وسوسه‌انگیز رسانه‌های ایرانی اون آب رو بدون فکر کردن رد میکنه حقش این نوع برخورد از سوی مسئولان دولت نیست واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26187" target="_blank">📅 01:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26186">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZQbPzpjNjr1X-Gfi6Vlk3SnCAIKMPs_PYCjrBeWoluHCEGambZPA87tj_DSiZdgyLMSSCvw0gcKv_k-02lg98Ayb2D9JTYIkpztrzsr4q72U38CWweN-gMAAMfS91a4USabtXUkxJyRp-a1R41Yu1ViJYFhcssD74GGBIRV-5UXzFBkfTyfp-znG47-GsdTIqwEYwACCiB9D8WHco7GdINaiCevbheQZpBIPp8ov-MOxYWqCxsF98P2hnx3tou9XB1Lox6L8TjbQ01suUh2v23xUN88-70-CAisF3jmNdcdmTeq7Zt_T8SXKe7cfWi1YA4d9XbcyL6D7hQ-usr8WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مزدک میرزایی:عوامل‌شبکه ایران اینترننشنال در سه مقطع پیشنهادمالی‌بسیار بالایی به عادل فردوسی پور داد که‌به‌این‌شبکه ملحق بشه اما او هر سه بار این پیشنهادات رو رد کرد و اعلام‌کرد هرگز خاک ایران رو به خاطر رفاه و منافع خودش ترک نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26186" target="_blank">📅 01:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26185">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6808ecf091.mp4?token=ht0unGfp_005DcW0f3uHUsSeURLZJFdltxeAmnufmRkljIAAwT9OkTAOgrz-1E3ht6dRsQWQlBGxeZxXhpUMZ2ZytzWo7ttJ6eVrm2K2ik7H7orqHONMAlkvodiL0mOSiELT8mpo7pLGhCUB9As_4SFQRmRBI34f_TV5LKziOJw87WTRRB70cTmre3shjKc3jnyhkzizvDvAA-_c7ev4D6K0zNfdsX9OXx4CL4YKIIRnK7EJ9TpQHe-O6ZFQXxAIgOMov-aDWf4w6kaxqw2mBW5_I4pe7iCaZ9gFvo20Yl_suYt9arnm0zLO-jhVoCRvk8dsztvbjB5R8veVaJgtjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6808ecf091.mp4?token=ht0unGfp_005DcW0f3uHUsSeURLZJFdltxeAmnufmRkljIAAwT9OkTAOgrz-1E3ht6dRsQWQlBGxeZxXhpUMZ2ZytzWo7ttJ6eVrm2K2ik7H7orqHONMAlkvodiL0mOSiELT8mpo7pLGhCUB9As_4SFQRmRBI34f_TV5LKziOJw87WTRRB70cTmre3shjKc3jnyhkzizvDvAA-_c7ev4D6K0zNfdsX9OXx4CL4YKIIRnK7EJ9TpQHe-O6ZFQXxAIgOMov-aDWf4w6kaxqw2mBW5_I4pe7iCaZ9gFvo20Yl_suYt9arnm0zLO-jhVoCRvk8dsztvbjB5R8veVaJgtjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت‌های‌جام‌جهانی2026
؛ جامی که اشک سه تااز بهترین و محبوب‌ترین‌بازیکنان تاریخ رو درآورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26185" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26184">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19f1d43ddb.mp4?token=pBJXciARpTst9EnOpoXPanslHTCoIt-zWoKApF5hMvDwCT00UxrI2JCXbDNJMt7duFHsS8uXkoBUpcmAeCzycXTlaSq77ta5C8MJYyE0IAo1EmkQNFizs-AH5uDqGQvEfD5aKlrZ2pwjxQvYMcORgIUhzKSzHYB7J8gEzEZjERs4WIGvINMdsCzyRgp_rIiaGECTrYLb7gQbWfQ5uatUhwjF2YDToZ6Ae-HrhVvuyeFn6BlkWiRh2_dXRF7cNYevMGeGLcutt7DFG_YS-jYJl12UiduRjQlLTCu5mNyVnas3iaTTzJtToSKdVI7r1R3EcnxvU9-Ejp3_rug2MeHGOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19f1d43ddb.mp4?token=pBJXciARpTst9EnOpoXPanslHTCoIt-zWoKApF5hMvDwCT00UxrI2JCXbDNJMt7duFHsS8uXkoBUpcmAeCzycXTlaSq77ta5C8MJYyE0IAo1EmkQNFizs-AH5uDqGQvEfD5aKlrZ2pwjxQvYMcORgIUhzKSzHYB7J8gEzEZjERs4WIGvINMdsCzyRgp_rIiaGECTrYLb7gQbWfQ5uatUhwjF2YDToZ6Ae-HrhVvuyeFn6BlkWiRh2_dXRF7cNYevMGeGLcutt7DFG_YS-jYJl12UiduRjQlLTCu5mNyVnas3iaTTzJtToSKdVI7r1R3EcnxvU9-Ejp3_rug2MeHGOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های تامل‌انگیزومعنادار ایمان صفا بازیگر سینما درباره‌شرافت‌دربرنامه‌شب گذشته‌ جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26184" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26182">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZki_A4quz415cUoSZR_G433tQD8jAaByr5A0vK6qZPNTHmXcsGAbSraYjcgHZ7GbnRuWEN4FO9AbxXvZ1by3m1u0jk0x7jskwfMCS0-4jnStIDTygjix9L98NxFPnW1_lLKRDfAG8vFw9nOI319CYfx0XH_8rQYzt4Fh39KLgjvrrHhl9DKGGC3eI5A_aJqG-JpLvm11RowqV1HfC-phZCHVWLdTktX1g57MvCOL6_Y3vhmfOGCFuslnpP_GgBbg6vGq0sjmLTKqvCrxKwqRpcumu2nmsdP6T5y9PYVzscM84ClP6eW7Y_Iv1VMfAtsw8l3PcglRpukw72N2SL08g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رفقای گل دیروزهم گفتیم باشگاه پرسپولیس هیچ مذاکره‌ای با علیرضا کوشکی ستاره تیم استقلال انجام نداده و هیچ‌برنامه‌ای هم برای.جذب این بازیکن 26 ساله نداره. بعنوان اولین‌رسانه گفتیم مهدی ترابی 32 ساله بمب اصلی مدیران باشگاه پرسپولیس است و امشب هم جلسه بسیار…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26182" target="_blank">📅 00:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26181">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyct8yjdO8Bfz7F_UVBfA2T4eQE-pZGw6I4Ao5tKMGR2SkPLUekswvWPUj9o4lXFewMa4QQNFHk0p09Beyrhyl8mDgBGs0A8nEHsPsa3-wK0zGJUFmG9CC6RjNlQYSo9cwIcx23jxBmksdT7jTC9Vj8qZ6bOs2CLPeigwuudGpTaEfXHWFpAFDOtlYmBZMcrhS1TO-JJSSb6tOBGRLShVDwvoYB5euGci6cdCPwiRNFtZJJvW-kNeP2GbdZqn5yJh0tkzg6zbj4JDnIxAcKKgXnxlZ3yRLpiJXkMinaZt--3lle2lezd7cUno2m1Eoa3B98GTjJJjVBfVJwh7iosoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوه اوه اینو داشت یادم میرفتم بگم؛ با پایان جام جهانی 202؛ تنها دوتیم‌دراین تورنمنت شکست نخوردند. یکیش‌اسپانیا بود که قهرمان شد یکی هم تیم امیر قلعه‌نویی که از گروهش بالا نیومده. قراره صداوسیما مخاطباش رو با این افتخار باردار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26181" target="_blank">📅 00:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26180">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7f2a6c71.mp4?token=M2GXYz1aDxC1zTSjJbLRacIP06tf_kfsup1R251IPaCln4J4_JYpGAM4VjRxiTiEJy66QoLhEaHCAxVps0N9SXaEQ8gvXmkr7vq_l7HUo3aYOutTfxnNcldvwp4Ihu9KXCeckRKIQuRmGG2-rvXCgqDfog-M_7aTdilitLI4NU8w2aPO-MuBcL0oCcUWCykyRzHPb4Gx39QC1jg3pagRzD3AkR03viU81uf4EtRtF5KPLhLA9k3Mdg8hBQNMmd3uvJoyg2hqI6c9EsftmxFA6S0AEDsFfhiIQ2aza2oNP9umwf_kR3SuKPp1QTjP2cvw7YP5TMSW57zUa5Ek0VBmSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7f2a6c71.mp4?token=M2GXYz1aDxC1zTSjJbLRacIP06tf_kfsup1R251IPaCln4J4_JYpGAM4VjRxiTiEJy66QoLhEaHCAxVps0N9SXaEQ8gvXmkr7vq_l7HUo3aYOutTfxnNcldvwp4Ihu9KXCeckRKIQuRmGG2-rvXCgqDfog-M_7aTdilitLI4NU8w2aPO-MuBcL0oCcUWCykyRzHPb4Gx39QC1jg3pagRzD3AkR03viU81uf4EtRtF5KPLhLA9k3Mdg8hBQNMmd3uvJoyg2hqI6c9EsftmxFA6S0AEDsFfhiIQ2aza2oNP9umwf_kR3SuKPp1QTjP2cvw7YP5TMSW57zUa5Ek0VBmSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برگام‌داره واقعی میشه که؛ رسانه‌های نزدیک به امیرقلعه‌نویی میگن سرمربی تیم ملی ایران میخواد بابت صحبت های شب گذشته از عادل شکایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26180" target="_blank">📅 00:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26179">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=onegkcDU41dAgrVd5HTsAPIOj0aSKivwcr54WTsvr5JJSWyohoa6szyaEkO0y4G39LDb3X-k_mHW22I731Cuc4D37gh4xFn15GeWdCHNaJQwDoPDoGayYv5XXLhw19Z1BLDqFNDcIYArl0Mma9Xh38e8WU-Kyegzbpv9qmHfOG5M5LnBYuozcaLj69IgnHrvHIa1mJk5uNUVK1HxSWU-QOykBO-TB-lFpiuRPVvM034-Fdc88rUTAj-svrtvKEdYiKtN5BCDJgQZSnX9inY5kHLRVV20PcYiO8VgqYtFsb4ycuCKDlNZkfUwFTONmXmM0DNeeFGmQ8G4pvaADj8AeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=onegkcDU41dAgrVd5HTsAPIOj0aSKivwcr54WTsvr5JJSWyohoa6szyaEkO0y4G39LDb3X-k_mHW22I731Cuc4D37gh4xFn15GeWdCHNaJQwDoPDoGayYv5XXLhw19Z1BLDqFNDcIYArl0Mma9Xh38e8WU-Kyegzbpv9qmHfOG5M5LnBYuozcaLj69IgnHrvHIa1mJk5uNUVK1HxSWU-QOykBO-TB-lFpiuRPVvM034-Fdc88rUTAj-svrtvKEdYiKtN5BCDJgQZSnX9inY5kHLRVV20PcYiO8VgqYtFsb4ycuCKDlNZkfUwFTONmXmM0DNeeFGmQ8G4pvaADj8AeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26179" target="_blank">📅 00:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26178">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nc3fTur2v9XL1cNaHTZYx9NsMA0RzXlFYdJaP91RuAqL43Q2cMCfKmfMHSlvmcnUTZscTmYUXYdnIEGL7RoBfmhATT8roTmZm7vGirjatCD16hddRYBllaIpRz0pYMZMpMfSfuciTYx9Na66xOq9us84ncm7rEa6Us4tGJgMxzoz6ejgZrXicbz2GbwFaQs7uBUWKkJlCCAUORF3cRnCncujVpj7apdeCa_gXwrin7i4wYsmzKr-jEZkRaYo-e6JcW4ox1CeHkoiMivY724LVGyBRd0Vj2qY1zeNEBuEeW-DTBpYLYR3yHHoh2qrNQFH1AUrP8JNFPuA4SWK5zxyTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/persiana_Soccer/26178" target="_blank">📅 23:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26177">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twnIesZMrGRmp4t59XiQlXBK9ko2-N6E-GqMvjs9xDniPQxAM5KhttbszfBTaNhqNd1N3je2FtxhTYwfCFRNOQoCBcxCC-LBJZE_ZuVfvGlav7117PPKbZ_5nM3VrXpUoAlVMv-PpqDNpuief7sKw8vTgm9DIUbvqzGFSG0UbBfN-jPE5ucjFpwl9g6h5NxRZKiZejsSmUmdrzZQypK1RPF79mo_klU9d1YXXbzSvjvvf3eBk1Cco3RBSg_lBzIfCCQSfF45LAfNDoTT8hmdDVLPIEinW_TjEXnal9Zvlrk4EjtF7JsRihpRiyk98R5_jnCxpMHZWDh4jXVF8ZhVLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/persiana_Soccer/26177" target="_blank">📅 23:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26176">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nij57szZSS_wfrN3GmkLbdDEdcCxJNtBN3Qsa0Dis5mAufuaNk0btVC0zvc51JlW84r1XHvgg46iAJhsVVaao46jPXGWQf0RU81buuxbf7KYX4U2ULM29VbIPZoBNldBInBaq3VebPOalPqkihxI_G_pXNdd9IhHiaC-mAasIDrMdYpVoR2DIg9kijLdmavWLA_b595P6IROkLapmJ4C5OiNzBLOsimvSfNbpBQcsxSAE5JJK429rNFFnvkf01pAPPXBS2nfYG-EkuVcAd4EwRh9eJsHlGF6rBuhMGLOWfHkDMXGfzWJNUXUEZroN5bBVfJNXPhidxx5wO6tW_-2DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ راجب دانیال ایری به اندازه کافی تموم اخبارش رو ازروزهای‌گذشته تاظهرهمین امروز به‌عنوان اولین رسانه پوشش دادیم؛ حتی خبرگزاری آنا خبراز متتفی‌‌شدن این انتقال داد اما گفتیم منتفی‌ نشده و باشگاه نساجی72ساعت وقت داه. حالا طبق اخباریکه گرفتیم فرداصبح…</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/persiana_Soccer/26176" target="_blank">📅 23:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26175">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZujMd2fF7IMJI2P_Ftk77IqvFhaEoa_9CzCNAhxGvvV7XvNHlTKOc8mHv82cO3deQjdFkZduJn4kTCOXBRxfKfp4gcyGhVUA2go9lWAvVPssiVxBt0vYl9Z1D2oN90Qtv7l3GfRj8Mo1VQDXDGiZIfXt2wJhJkgg1SMvSPrfC7Fb86re0Jn9nI7t87hXT8ODUszQS7iasOF3rdRcLNMPLiGd6Yg1xvIjYrDU0K8fAlDfcYl6DHDFAkVsGrhYtBDgK9F95DflMw9n6BUJBB8J1hGkCL0RY9K97DIO_DJ5PLibto5WyMkd8jscJDF0XlL7IUUWwANhIOsoy0C7naGOBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه فجر سپاسی با مجتبی حسینی سرمربی سابق آلومینیوم مذاکرات مثبتی داشته و اگه اتفاق خاصی رخ ندهد بعنوان سرمربی جدید این تیم انتخاب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/persiana_Soccer/26175" target="_blank">📅 23:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26173">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ed7e49e2.mp4?token=Tr6u6XeaBcvoXUXt8NIcfqxzu-6y3hWUE6_R1c7xzhNoevSq_IBK9TuZ0DP1GypreW6qUs00a8eJdx7weMjeaOB9owSxJBB2d9hIXuW97CmoG56H0MK1ECRcdhTxrR3Zr7YKicJoLxe9oa1HtV1b6gqk8UIWN9r6wOagOxes_BUU3AmQHtFK5VcBLxFlzvuj7dGWBGutvaulonQJrMOinLRxO44DbqBKGG9_zFuIeCZlbLS15UbuVKmry3CinJnqEjx6G3wo0XV1OmcdHwSOOsIAXHTDrrM_p_UPAKajTxKb4Hca58i4OwpX6wRsJJHGzcG4NIw1ToDKvbIHiVm_7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ed7e49e2.mp4?token=Tr6u6XeaBcvoXUXt8NIcfqxzu-6y3hWUE6_R1c7xzhNoevSq_IBK9TuZ0DP1GypreW6qUs00a8eJdx7weMjeaOB9owSxJBB2d9hIXuW97CmoG56H0MK1ECRcdhTxrR3Zr7YKicJoLxe9oa1HtV1b6gqk8UIWN9r6wOagOxes_BUU3AmQHtFK5VcBLxFlzvuj7dGWBGutvaulonQJrMOinLRxO44DbqBKGG9_zFuIeCZlbLS15UbuVKmry3CinJnqEjx6G3wo0XV1OmcdHwSOOsIAXHTDrrM_p_UPAKajTxKb4Hca58i4OwpX6wRsJJHGzcG4NIw1ToDKvbIHiVm_7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
دیشب‌بعدبازی فینال؛
یه خلبان در حالی که کلی مسافر آرژانتینی داشته روآسمون گفته آرژانتین قهرمان شده درحالی که فینالو به اسپانیا باخته بودن و اینا از خدا بی خبر اینطوری خوشحالی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26173" target="_blank">📅 23:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26172">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d51f33dc.mp4?token=YvYe_HeIL6vCWKbdiSwTclJ7WJUUUNosrbPANDsLKXHeB1qA1x7i3f--NlqGarDghTr6Ia9QuO2V7aXVeqNSYTkTpPLWX3HADV-JfKiqZEeTJa9ZMrhMJairMgz2e1gqPET7bPA0173gobT2N9Ii7-fTbCD88V_66k4-hdnTD8-hR8IrPN77S6XtDTdNT4ccdIXEwmekLaOoCY_YWY6nr7JfiB5LiK6kpZuuihtFM9fyRF2WBt6s1UkOuqutT9pg1sb8-OZWFMWmqkqop3XVCk1N6x5HUFX_Z1o50zCZ04hFPxXl6QIF5In_hZUl3ny447j5sE0E4r4-F0dzHLerQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d51f33dc.mp4?token=YvYe_HeIL6vCWKbdiSwTclJ7WJUUUNosrbPANDsLKXHeB1qA1x7i3f--NlqGarDghTr6Ia9QuO2V7aXVeqNSYTkTpPLWX3HADV-JfKiqZEeTJa9ZMrhMJairMgz2e1gqPET7bPA0173gobT2N9Ii7-fTbCD88V_66k4-hdnTD8-hR8IrPN77S6XtDTdNT4ccdIXEwmekLaOoCY_YWY6nr7JfiB5LiK6kpZuuihtFM9fyRF2WBt6s1UkOuqutT9pg1sb8-OZWFMWmqkqop3XVCk1N6x5HUFX_Z1o50zCZ04hFPxXl6QIF5In_hZUl3ny447j5sE0E4r4-F0dzHLerQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دیس‌فوق‌سنگین ابوطالب در برنامه ویژه امشب جام‌جهانی به‌قلعه‌نویی: ما تو غار کنار عادل هستیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26172" target="_blank">📅 22:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26171">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddacab4fa0.mp4?token=qne6aq_EMybj5wzGCmEkxT9JkBbrIJ6Fa0wM0HKUOXypom0jZ4pd8QpAlxmo1Sv_ZNKAJNdZFiiTTNcfaK3Z3jfWw48L2LMmRq1zlySVsQHW7gZXelnjxQAwINcYtbX-OvA4IGxKuYhETBLlvpFTSHeb4HTY3mqzhetJ3tku1TB1KhMLRx7_jIltPaNM7HaApxsaiS8icmnKMHzECI1z0vtMxVOof8l3XNmu7_vKnJjoBtx5R14bCI5VxMFMXFmDNyimPS8ty5XMVeR01WDS0RygdhEsN024bQ0ln3aTVXFsd12uD7dvgXjyk3TCsvwdgPFDIXn4_dmsYkTIzTeQEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddacab4fa0.mp4?token=qne6aq_EMybj5wzGCmEkxT9JkBbrIJ6Fa0wM0HKUOXypom0jZ4pd8QpAlxmo1Sv_ZNKAJNdZFiiTTNcfaK3Z3jfWw48L2LMmRq1zlySVsQHW7gZXelnjxQAwINcYtbX-OvA4IGxKuYhETBLlvpFTSHeb4HTY3mqzhetJ3tku1TB1KhMLRx7_jIltPaNM7HaApxsaiS8icmnKMHzECI1z0vtMxVOof8l3XNmu7_vKnJjoBtx5R14bCI5VxMFMXFmDNyimPS8ty5XMVeR01WDS0RygdhEsN024bQ0ln3aTVXFsd12uD7dvgXjyk3TCsvwdgPFDIXn4_dmsYkTIzTeQEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اینوقلعه‌نویی‌بشنوه‌دیگه فکر کنم شکایت کنه؛ تیکه فوق سنگین عادل فردوسی پور به قلعه نویی در بازی امشب: آرژانتین بارها تا آستانه حذف رفت. فاصله‌اش با حذف5سانت و 10سانت و 30 سانت بود اما خدا کمکش کرد و موند در این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26171" target="_blank">📅 22:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26170">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22beea35ed.mp4?token=MrIrbPFPkgXCwNljLMESHr5aQLcgQzQgMWqHP6hU79ZAE5KOw3R0UdNgn92AA9pzF9gBLpz4b7fyMMIwfoX29_Lv0CHPANzPHCzd_9sK_13WrFo96xNmElT-4FDMXm6esxUZXF5zVelT_dLz641BSiezYfOP-89PIPGj8sO9bNA4ZaViNiXfodov4Q_URaI-R_vF83rjJl94MvGYaOy8FtnaaWzMVrK04nc6GuIloZaVjgtBSluT4RWuLVAFnzI_6UvZzOcT9Rv-lH4pwm19B0m8H5ANZksQqIinJIWuXudP_cz0VXlqdDG7Kkb8UtvjyTc5hUxg9AL5tUVD2C-tHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22beea35ed.mp4?token=MrIrbPFPkgXCwNljLMESHr5aQLcgQzQgMWqHP6hU79ZAE5KOw3R0UdNgn92AA9pzF9gBLpz4b7fyMMIwfoX29_Lv0CHPANzPHCzd_9sK_13WrFo96xNmElT-4FDMXm6esxUZXF5zVelT_dLz641BSiezYfOP-89PIPGj8sO9bNA4ZaViNiXfodov4Q_URaI-R_vF83rjJl94MvGYaOy8FtnaaWzMVrK04nc6GuIloZaVjgtBSluT4RWuLVAFnzI_6UvZzOcT9Rv-lH4pwm19B0m8H5ANZksQqIinJIWuXudP_cz0VXlqdDG7Kkb8UtvjyTc5hUxg9AL5tUVD2C-tHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه سنگین و کاملا مستقیم علیرضا نیکبخت واحدی به میثاقی درگفتگوامشب خود با ابوطالب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26170" target="_blank">📅 22:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26169">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOF6818Ou4UhfYIjFhNZ3ZGWrLQgksj9sNFFNYY_E8euLDZO0-qNe8gooJmwGndgEsi2v9SBUKUg-tewkCJAdujbL2OE1MKsCeaV9Yus0JZaQPCf0tmkB58I3Dtz794XhcibS6o48J-dAsVUm4upX7rwsz3lGM4gnAflIS2krEFm3sQsX4fzrrl5HdrR7p-lVFBjPuGD-D4pbhMq21iWsFd-KJt0Ya6GKf-y4nSbO5cOGpyjaaZGGB-jRsqfRbmKFUs7-hgRhMY0AB7HxohT9m07ZI-peWYylzmG15YMxVt9kCSsJtNuR11XWb95gGasuK8pNL_ABZV1qlZUGfBgzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
20 ابزارهوش‌مصنوعی درسال 2026؛
بهترین ابزار های هوش مصنوعی در دسته های مختلف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26169" target="_blank">📅 21:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26168">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed6167b3d.mp4?token=sRPfaFnEvLSFmN1pbCIzA8LNl3DHfEgPeAytKxEGvOrVh2jt70kulctlYoStF-tvyN4-bKboBGes75026jZXXhorjEUr-_P2x7zkhx0qic0qtK7fY4YNXVSVW3ext5nDniy41Nqsyqn6MqL3WCC_m2uwT4B5g71TCAxddzW31XBPFa2AW0ExEH0SfMrhpOB6zinh94KyVGqWgCdKeodsD5pOPIgXCn0yteNjx_Ciku7L-2tfQdXCM7XL99WtDJxhPq_omCsraRP3H7wMX18pl9MplhU0Lgpc-b8Nj9Pg6L7rVYH1zrcH-iMWmwveh6pmCNEQamBUSxEkhXtEf00hiDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed6167b3d.mp4?token=sRPfaFnEvLSFmN1pbCIzA8LNl3DHfEgPeAytKxEGvOrVh2jt70kulctlYoStF-tvyN4-bKboBGes75026jZXXhorjEUr-_P2x7zkhx0qic0qtK7fY4YNXVSVW3ext5nDniy41Nqsyqn6MqL3WCC_m2uwT4B5g71TCAxddzW31XBPFa2AW0ExEH0SfMrhpOB6zinh94KyVGqWgCdKeodsD5pOPIgXCn0yteNjx_Ciku7L-2tfQdXCM7XL99WtDJxhPq_omCsraRP3H7wMX18pl9MplhU0Lgpc-b8Nj9Pg6L7rVYH1zrcH-iMWmwveh6pmCNEQamBUSxEkhXtEf00hiDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌ های اسپانیایی: دوست‌ دختر یامال رابطه 5 ساله خودش رو با دوست‌ پسر سابقش به خاطر یه درخواست مسافرت از طرف یامال تموم کرد. گویا قرار بوده ازدواج هم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26168" target="_blank">📅 21:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26167">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwVT-wPheBLxn-Z7_2VqJ6Dq4sOFYa0Th7OYq7a3-d-0SwUyGgZ2nj-jvFpf3Ejp0Auy0efmjqP4D7Wfd4bHYzb2wDSlQCs_eD9liy5LzI6r2FHXFEVMn0_EfrAG94UbMvyWui4jvOmNadzzJIyvlYxLgiqW4vlgpUpvUSKYFhbufNIKYuGeLQzWiIx8tqoQJdA3eWsMTqMmP0Y_d6BbztLmzctT-1be4opoX3hwCRCS-etlPoeptrEmLVYeW7PxNv7K5jXpQ6zpqTsY0_hVcSeHQ_AhzkI8_kju8TIeNip5KTYZl2BACMPRt7SkI3Ellhd53ikE3Fr94xHBPDvOgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام مدیربرنامه‌های داکنز نازون؛ این بازیکن قراردادش رو با باشگاه استقلال فسخ کرد و‌به‌شکل رسمی از جمع آبی پوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/26167" target="_blank">📅 20:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26166">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTDEG-_-1ckq3-P6urZ2KnwbYNW6gN4isMWa_QGBM9-GXX8Cq5sf2VKkoe6rpJta-S7L7mGVqKJ90hjJOzSIXRkdr7pq5V6Y3DzyH5bVAFoAr8oyl-kbSdHwHiaHG44MU8Wwi21_Jbd26vQFjwh5KL1ZIMxcz6FRyjG6YQze0CdsouAr2N37wMLHlxqjcfUEwgR_q1bTJf86JbrTr6pjTAIMQcqYif5IxjKLLHeN21-4z1c1GYy_PIkhcnn5HA8bzpZrTwoUjhv-Ka0KQSccmswAJeq9JsEVsn7niLuHx51_QnvSoNB__aI1glgtXbq42OL9pS46ZZwvLKFcQHrN_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ جدایی داکنز نازون مهاجم خارجی استقلال از جمع آبی‌ها قطعی شد. نازون به مدیریت آبی‌ها اعلام کرده دیگر به ایران باز نخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26166" target="_blank">📅 20:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26165">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHNldr1muznay08VUa5Y38FTySp65exLQk7NCwxovOB8noVqOwN8FU1pUyzTtMlf9E06iieB8CdK80UkvdZacLHCQJkTNvygVjG26-pe2tb2_qij4MzuxfeNbJ3_ZHBDaaFN6tlU8tvJ7jfWlnCr2kcU0UOMOBpt4t0D5RJGSbpR3LRBRGr-EjUaIH5B2wJMUvE_uBJqe2Byuh__Q5cY8RVDNX1vwL5yWFuhkyvYO60EoGnglmZn86hBMlxTTdcEUdxAL-5guh8q4llSoIkFUlNYVVm-DwDXlv5QlGQPn5VNKalQdyyQ-kq0SYTW5T1EbQexxB-MoWQaoLwVort5KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌اخبار دریافتی رسانه پرشیانا؛ حسین ابرقویی دیگر بازیکنی‌ست‌که به احتمال خیلی زیاد از جمع سرخپوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26165" target="_blank">📅 19:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26164">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Edad-0Gn1zdQc6shryhpAi9KwB76fBECv9pSFlL8qI86Nke5CRG4kzXFZG8CtWMaK6njyW165Uhz_eRwv3eRFrf1jUX26CAKSKPu1yEYQn0lIe2iNnTyO1aQugadr-P03szcWiIDiKsu7ocZhRWUvOJp3mYK31lGR1zYUHbqmMja_Y_DAUKAtO1GyFYp7LQuNcbqzPidExJ5Dlp3tAoNKTJJSdnYYVJMisfdqEP6bzTXEyyM-8Y_eXS3Tw2Nql3Fk8U2PQ2wwN7y3CDSgOuffftrEPXS9qvelB6uLGYxzcpDk6XUSNcy58t0ldTXANPlEbtA0WawSX02IIbeb_kXgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مدیرعامل‌ تیم نساجی امروز صبح به مدیریت پرسپولیس اعلام کرده تا فردا فرصت دارند که 150 میلیاردتومان بابت رضایت نامه دانیال ایری پرداخت کنند تا بندفسخ‌او رو فعال کنند. در غیر این صورت اجازه جدایی به ایری رو نخواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26164" target="_blank">📅 19:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26163">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424844d43d.mp4?token=WyBRuTPR6TYWjOaVnJm-mznSXnUGnFKrOKmh3Pr0nFrVWxiJwihEO27VW60wFbvvTh-GX0y94OABInszJyPSXOMvx0yhQfDY7aWiRrtYBduMv9JxkjZ88-ssdyv3CWAZBlyWubRanuzaGh7aZ9rlc1hkxDBl_69Cb-BbRT2De-gvko9FPT4P1WE90UYpinNi7o7ucm9H4lcEpD8P7iVgfLEUk2rfWA8U-sFWsGxvhQCzKZc7YgIRgbRNbNOd6zaZBkx6o1LV4wAK3zpCBEsbv6Ei5b7ssPaMq4FyGij5K4ydq3GAxsi_gN7ihbby-fsiFmAYRGmDOcm8GcFsgcPXtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424844d43d.mp4?token=WyBRuTPR6TYWjOaVnJm-mznSXnUGnFKrOKmh3Pr0nFrVWxiJwihEO27VW60wFbvvTh-GX0y94OABInszJyPSXOMvx0yhQfDY7aWiRrtYBduMv9JxkjZ88-ssdyv3CWAZBlyWubRanuzaGh7aZ9rlc1hkxDBl_69Cb-BbRT2De-gvko9FPT4P1WE90UYpinNi7o7ucm9H4lcEpD8P7iVgfLEUk2rfWA8U-sFWsGxvhQCzKZc7YgIRgbRNbNOd6zaZBkx6o1LV4wAK3zpCBEsbv6Ei5b7ssPaMq4FyGij5K4ydq3GAxsi_gN7ihbby-fsiFmAYRGmDOcm8GcFsgcPXtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
خوان کاپدویا فولبک اسپانیا در تیم قهرمان ۲۰۱۰ توییت‌کرده‌که‌توفینال ۲۰۱۰ جلو هلند من یه سکه با خودم بردم گذاشتم یه جایی زیر چمنا برای خوش‌ شانسی و به کوکوریا هم‌گفتم‌همین کاروبکنه امسال.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26163" target="_blank">📅 19:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26162">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nt8BASQlTkyOz69XKRDUWOoxT38PB2h94RHdqLKp2lYl-jIz4mir-rZwbLjbUkvPob9F2DLgTM6K8YCVrcodBJM1VfZHJDPgFRW_lpn1y67WlCzwYlqM16hP1IBox5pt4Mlpkwgzp1O5o4D011SMk-0Bbmz41Y1fCmF7wldWZeYYIqhVhVhMbxK3fr0U2NyTPjFaOEMWTdMo01W1MUVHea1d9DOUlGJ7CToaVUUD-Sdc86EEjYq2-BiQ0eG9wE6GC_pM_6cXGKZcJ18U3D6HaRQBldftFp7XEG3FGBCYIpmcTDsYqDZNWs9fS_LyBcnWENsaPvg6GaEQSmLH_1u1WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
معنای جامع و کامل کلمه آندرریتد؛ فابیان روییز ستاره‌پاریسن‌ژرمن50 بازی ملی داره و تا حالا شکست‌نخورده توبازیایی‌که‌برای اسپانیا انجام داده.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/26162" target="_blank">📅 19:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26161">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021b11787b.mp4?token=LWF0EamqcC0cSD3RhH5dhQDDbpzGjSnFZ1a3Uwg9upzj3yCdjqRSERi64fVGsoN3LsyrhggPWatATvuCd6Kl4E8LeILizcu07ZLm4Wcxp1P0FA3mYqSWpkqPXniuYV3A4g14Q8jP8E2rthnVnO8Z25Y5WVdIijmT3IUeS8yWCApus69-qBxy0y7uCJ36ccNGB4L-kuPOpL4-5CTjL2gmpw7M3pZW-4y4hi4zpxytJfXOUlTYhHEfKv2d9b4V6m7fovXgLsgD1zXFGXNVNB_w9PfUAMIMOsLnW0cjcZ0R87x57W8GbGoQbtfNIp0VzhVZWKPIL7cZdnucEm4xH_75JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021b11787b.mp4?token=LWF0EamqcC0cSD3RhH5dhQDDbpzGjSnFZ1a3Uwg9upzj3yCdjqRSERi64fVGsoN3LsyrhggPWatATvuCd6Kl4E8LeILizcu07ZLm4Wcxp1P0FA3mYqSWpkqPXniuYV3A4g14Q8jP8E2rthnVnO8Z25Y5WVdIijmT3IUeS8yWCApus69-qBxy0y7uCJ36ccNGB4L-kuPOpL4-5CTjL2gmpw7M3pZW-4y4hi4zpxytJfXOUlTYhHEfKv2d9b4V6m7fovXgLsgD1zXFGXNVNB_w9PfUAMIMOsLnW0cjcZ0R87x57W8GbGoQbtfNIp0VzhVZWKPIL7cZdnucEm4xH_75JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26161" target="_blank">📅 18:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26159">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522741a6f4.mp4?token=Ccx4VwFj5BMxws-PMsSP_nKVNGPPa7e8t8X4R3OAOfXiv4mno4ayjT5IXmnMrAPPrEqeiUu4sGyjbat6mgfL02B9igMF0nIAdp_WO8luNjVveFcW4dc-pEK5TlrfLY6eCx9ovwQVZefsQDo89XKuSJwDEX0MRp79TlG18-Bj4u16W4fa4hn_61g3pJwqKdLxM7BbevfWQRZJ80BHmuyTw5caUQO9yKYWllVsU_y21BrrXxVLzW_KxXKy6h4T1oHLJVUSa4epY2h7e2_RQgi7QjGotUa_QR1tzhYgG6-g6rw2mjeI_2wSOKBtxquNp8KY2fxA7hDFfY13uWgCC3jwkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522741a6f4.mp4?token=Ccx4VwFj5BMxws-PMsSP_nKVNGPPa7e8t8X4R3OAOfXiv4mno4ayjT5IXmnMrAPPrEqeiUu4sGyjbat6mgfL02B9igMF0nIAdp_WO8luNjVveFcW4dc-pEK5TlrfLY6eCx9ovwQVZefsQDo89XKuSJwDEX0MRp79TlG18-Bj4u16W4fa4hn_61g3pJwqKdLxM7BbevfWQRZJ80BHmuyTw5caUQO9yKYWllVsU_y21BrrXxVLzW_KxXKy6h4T1oHLJVUSa4epY2h7e2_RQgi7QjGotUa_QR1tzhYgG6-g6rw2mjeI_2wSOKBtxquNp8KY2fxA7hDFfY13uWgCC3jwkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی خفن سوسن پرور دربرنامه اخیر قیاسی؛
قیاسی از سوسن خانم پرور میپرسه که کدوم ورزش رو دوست داری؟ میگه ژیمناستیک قیاسی میگه خب چرا؟ سوسن میگه: چون میخوابی پاتو میدی بالا!!!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26159" target="_blank">📅 18:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26157">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219a5ecb02.mp4?token=l21LYFaPUdPMpKPg2wsfEiHtuAlsI_cMx-w56BAlroElLKh5qudd1SpiheqoJv0jz_UWinKEKE0dStIGZzkvICRftxu5By4bKgLXlQARtbIhKQgeFhWNl6n6RqO2CycW_146CENMsrHisCFVM71BSIq5vktRv4bvmYriQ7SQxbpCx6dkCQE5sP67agHSnRbV9hcu2e0cDuUBaMBv_FLjF53QsfSK5hnoYjPoiyoTVszPZpIcAJI_elsfyRoWyIUHGBxCAQr3JQpx0RFiKHSNY-RPMqApxATzKMR3LoXZKkLn_QnEK4-3BYDmqfERTF6mVqH7t_819CLWIV7kbPqurg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219a5ecb02.mp4?token=l21LYFaPUdPMpKPg2wsfEiHtuAlsI_cMx-w56BAlroElLKh5qudd1SpiheqoJv0jz_UWinKEKE0dStIGZzkvICRftxu5By4bKgLXlQARtbIhKQgeFhWNl6n6RqO2CycW_146CENMsrHisCFVM71BSIq5vktRv4bvmYriQ7SQxbpCx6dkCQE5sP67agHSnRbV9hcu2e0cDuUBaMBv_FLjF53QsfSK5hnoYjPoiyoTVszPZpIcAJI_elsfyRoWyIUHGBxCAQr3JQpx0RFiKHSNY-RPMqApxATzKMR3LoXZKkLn_QnEK4-3BYDmqfERTF6mVqH7t_819CLWIV7kbPqurg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترهاوقتی‌امتحان 19.75 میگیرند
🆚
پسرایی که امتحان 0.75 میگیرند و درباره‌اش حرف میزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26157" target="_blank">📅 18:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26156">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ij54hqkR_MRsHih8MNMTy5uwxjqgRHUe5EH_dqafubhxwJaxWbGCTKHVhpX0aLN4WwFhpp7s9tLf70_ImZtOsEtIqHhZ666Ugam43vHEhTqfhxRqSdQhtLdBpSqj_ClBPGhzYahNmztCpj0x5-aSBVPNSSzxZTcUEmEeRQ5ZNXi3drLTItj4a4Q04QoG3AEHIjQxt1tLozeS4RIeBU6ENeq-RUGyW2YQV5iyMzPXtArMRvoadn3PzunbE9oT0rlFbTyXaYnn-jdOLQGIhjAuHAHPC7bLBxnFX-PiYJqri4R3d5OyQ4q8BtqngK6IdRCnJmC9iDixcKspShxGLuPXPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26156" target="_blank">📅 18:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26155">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C97l4wjNrqFli7m7XRJ2ytUlJCXYFtLlDBa9pZOqE5kVwL-WmiSUCfJZfd1ozzcGwlctpIybUSmgic77RDj-5qNaApJxdTKHIivOfIlJDEVKT0rJFiDp2yCh7Z2pwTO-J6c0UodEiB5bDWXNP8j99z5OYRKwGBNkR86NztRlYZBZAqUpKnJ6SHEkGNZGxvsS-17w-gwK-rmwrJ4a2A1LyGCcl9SS-S3F-1jUkAlY8cB22XhN6PlslU220JLh1w7GyQseTlWSFSJhAqCRAElyJB6jqHiOE24Z3dvF7LLRQyUdD8zOx9nGfBlI2eTrmIPBzZ0IQcLFoyf4jQc8WRNIYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پنج روز پیش پرشیانا
🔴
محمد عمری26ساله باحضور درساختمان باشگاه پرسپولیس قراردادش روبه‌مدت‌سه فصل تمدید کرد. حتی مدت‌دقیق‌قراردادش هم گفته بودیم. عمری آفر خوبی داشت ولی تارتار مخالفت کرد اینم موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26155" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26154">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b054f61942.mp4?token=r7hbsasuOjFLpPrYElRU97_8NhX0w4q8zgYztOfqwF1rPcx7ChTwHp3lL5QGixT8Sh9bkJqR04RdV6DbErcmyAjFK4ckUDPRI9YpsIlnleCiYLJiAs4rbSoyxaCyS1HQ4CQUlO-cz0nJXtzOuqsgWAkdAAOA7TfaQ-9bCDVHbdZVdpKJjruukq6_GtsdZsNed8fwI1Y5gcm7uT_2dgo_0FOBtGjdvD4OenyTnIfIxEtLhPH0w95OVhWDVyIlI5ENIqUhGS8pNxA8FGYiKZMh5WYzY5mQ_nHFGWisicH_oNkwaMyya5GGhcZTtX3ELKfuxVY6JoxFuWfz1qBQxPPQaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b054f61942.mp4?token=r7hbsasuOjFLpPrYElRU97_8NhX0w4q8zgYztOfqwF1rPcx7ChTwHp3lL5QGixT8Sh9bkJqR04RdV6DbErcmyAjFK4ckUDPRI9YpsIlnleCiYLJiAs4rbSoyxaCyS1HQ4CQUlO-cz0nJXtzOuqsgWAkdAAOA7TfaQ-9bCDVHbdZVdpKJjruukq6_GtsdZsNed8fwI1Y5gcm7uT_2dgo_0FOBtGjdvD4OenyTnIfIxEtLhPH0w95OVhWDVyIlI5ENIqUhGS8pNxA8FGYiKZMh5WYzY5mQ_nHFGWisicH_oNkwaMyya5GGhcZTtX3ELKfuxVY6JoxFuWfz1qBQxPPQaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
قالبی بسیار زیباوسنگین از فوق ستاره هایی که باعث‌شدند ماهاعاشق‌فوتبال بشیم. چه زود گذشت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26154" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26153">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1819c235ea.mp4?token=PIzTaneI66XTpz5a1J52Z_tuUPQY-VmM3YBG_SPiVHvMHDEZGX8oMb6oFYmUCfzXIX4uGaFqvN68rMWMwHICxiwcmr0kmKElh7mhARKtHi63ZaGXx0wBDt_CBzX1lkWld-XxguiLyA5fWeI5_0n0X_pOHR_pNDxSHEzm3dSRkEHkEV_UqfntD3z1B06GteEPenXEQqgfqKFaoeTr93JiRlPzPCW6aj6gG32CtGTpN_6I0yOERhoCAf5aD_q1w6Inv-lVCsjwghM4Qorl5TWrvzfECRWT6C97gs7bmZfWVxbBOLa0qShLtvEgYRoFgOb1FZcnRJaZVyXUUEciclRgYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1819c235ea.mp4?token=PIzTaneI66XTpz5a1J52Z_tuUPQY-VmM3YBG_SPiVHvMHDEZGX8oMb6oFYmUCfzXIX4uGaFqvN68rMWMwHICxiwcmr0kmKElh7mhARKtHi63ZaGXx0wBDt_CBzX1lkWld-XxguiLyA5fWeI5_0n0X_pOHR_pNDxSHEzm3dSRkEHkEV_UqfntD3z1B06GteEPenXEQqgfqKFaoeTr93JiRlPzPCW6aj6gG32CtGTpN_6I0yOERhoCAf5aD_q1w6Inv-lVCsjwghM4Qorl5TWrvzfECRWT6C97gs7bmZfWVxbBOLa0qShLtvEgYRoFgOb1FZcnRJaZVyXUUEciclRgYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
نیکو ویلیامز ستاره‌تیم‌اسپانیابلافاصله بعد از اینکه مدل‌روگرفت به این‌شکل به مادرش تقدیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26153" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26151">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjFQJIbo9nT7fAEHGbjNrfVKWXUu9pWKkIjHSLbP1W-_lHJLiz6MWK11CCfkYpBtaSWFYaitGzFU__ktfU7CuwUAiqC3DUgQbb9wLbjrkbgGZUuKN1k5qUYPoL-Jmj-zV8xwzWThJLme3YfJ4AoHN9bKl7ixIrnmFNNRV5_N9bUNu731SGBKQ6AjaUDT-_42Z92b1AEeDTkpQaH6-NxYcQBENBgBxUDToxBBKMJpa9Vk_PXx4Q24xcDXI0sMkOODJRwlgW-1jcUfFretcKJHPSPxF4OVZEBv8jKj9E0q6ToCq2MVUmzttUN4vBqQRGk_qQhJ5XEAGujsIvkrPuON5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین بازیکن 6 دوره اخیر جام جهانی؛ زیدان، فورلان، لئو مسی، لوکا مودریچ، لئو مسی و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26151" target="_blank">📅 17:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26150">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HN1QkyLLliEHgsorxZlVZSM60UOs2ZE4RIG5nrc2j-uWe5hcwmz5hJ1tBqiO6sKzFTawlpomXLeJ2kb4KfgNaSCWsUc7yEOXmBxOhD3tcbc80KcJJCc4XurwalaMKeiDsOZUucL6jN5fSasyzotrDIoIn0zqIhVqQK2_P9qlRVntILXWPYGmzAOl045zxtTNuapIfgLpjbZGtlehpOTIoOdvsaago6u5yrAtp-0TnmNZzHk7I4asi_5zmtu8qkiH8X5ZthrJJyip9h-9edMqJJpTQIe1lNnz-pK8IuwiX23ulUHB4Dom5M478kYMDqakI_Pg6FkZ_083mubzn9i6Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درحالی که با قهرمانی اسپانیا هیچ گزینه قاطعی برای کسب توپ طلا دیده نمیشود ، فرانس فوتبال در آخرین‌آپدیت‌خود درماه آپریل "عملکرد فردی در تمام مسابقات بزرگ و مهم" را جزو ملاک‌های مهم انتخاب برنده توپ طلا در سال جاری اعلام کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26150" target="_blank">📅 17:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26149">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc40ade6c.mp4?token=E7jd_2GP1EcSMbIPsTxOuZa6NlMQZMGwQFvx3A_JVu0eF6UKYM_UXRtsiqoNqXIKAUQZoo5-Zp_6HFlhs3FZGSvSsmftfThz1ZnMgBSSzkWr_W-gm6ZVfV__Erw4oqp56A-xAfbeY0I85m7w3o2B_R57hLo-nc5iThp5qJy2x3LB-up-YA-uJGNZBN2eG81-je8OZgMMcUdc5al4pZzxv5TECzf4Iht8AtvnsBHhiFSewRhUijZUuMqr4kAyDdL1VBsTb261jC2zfQsJ1G5IecXhSRs9tXpc8EZAPpeXpm6eJNW8ZYRuWdKlXKqxlT5UeVzL51_pZqwEOZs5DA7JJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc40ade6c.mp4?token=E7jd_2GP1EcSMbIPsTxOuZa6NlMQZMGwQFvx3A_JVu0eF6UKYM_UXRtsiqoNqXIKAUQZoo5-Zp_6HFlhs3FZGSvSsmftfThz1ZnMgBSSzkWr_W-gm6ZVfV__Erw4oqp56A-xAfbeY0I85m7w3o2B_R57hLo-nc5iThp5qJy2x3LB-up-YA-uJGNZBN2eG81-je8OZgMMcUdc5al4pZzxv5TECzf4Iht8AtvnsBHhiFSewRhUijZUuMqr4kAyDdL1VBsTb261jC2zfQsJ1G5IecXhSRs9tXpc8EZAPpeXpm6eJNW8ZYRuWdKlXKqxlT5UeVzL51_pZqwEOZs5DA7JJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام امتحانات نهایی پایه‌های یازدهم و دوازدهم چهار استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، تاآروم‌شدن شرایط لغو و به تعویق افتاد. وضعیت دانش آموزای  بقیه استان های ایران:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26149" target="_blank">📅 17:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26148">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YD7k7leLpKF7mbzL5ZwtXERZnxgsOVuM5QCdj2tuVdwR74L0nDKh3GZ3rGFwZMYOeXPYetvvAUvgBsFc6nCv7VqpD3dxzXJRQc_tCFHMrnlDPP7bHBY5MIT75qI1UL9wPqgA6YVDVoYg54ty5q1oLn1OW0LpzfoLv7o4hSeAB2UcL_2h64uA4BwcrjlZB-QMJ2Rf7tNeIUwl_ocy8_l_4EQ0BH0Y7DgEDPAmdM2ywOF-92QhhWbQpY8KfJjjjXotmKhE8sPjVGUKIfsoAPG5AhBvN9JwUcgWlzgUg364TMWfr6K4iLZLL-PfYGFPjKi7hK1u6E1C9B3NEXmTo-XRUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تو نوزادی مسی با اون همه افتخار نشست کونش رو شست. تو دوره نوجوونی‌هم‌یه‌کلی جام با بارسلونا برد. تو 16 سالگی‌قهرمان‌یورو شد. تو 19 سالگی جام جهانی رو برد. این وسط هم بالای 10 تا دوست دختر داشت لاس خشکه میزد. این بشر دیگه از خدا چی میخواد؟ چی روش میشه اصلا…</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26148" target="_blank">📅 16:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26147">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICSaXDfBecK0Lv-Z_R9i48zJXPSMSnRx819N8omfOBnNdJ4yK-Z3rOeRBq1rFryBb-MVeOUBh4jljmBEB4ZAWtYx0b__jwPQoSfNwZmaQtitCOMuh23x1OotFDIxot0A8Zdrc6XYuaI9Dvgy6-p-cSygBEQ4dS6M3CJnGoi9jepUkdbo5IWDpq_KPSBSmgVW9-bMQYaHFQ1f1ouCFogzo7MDY7KVX_h6pApAJbgxtBkqGenkg4HABtd8b9hLYVqeoJeO9HoDY0mWn-BmIc-QLPM-ukPnUcJMvBGHEJqZ2NrF65lzET2NEQqWj69yDVJAC6E1_R5jyRYJdPdTfxY2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتزوری‌درحال‌شخصیت‌گرفتن؛بعدِانتخاب روبرتو مانچینی‌بعنوان‌سرمربی؛حالا پائولو مالدینی اسطوره میلانی‌ها بعنوان‌مدیرفنی تیم‌ملی‌ایتالیا انتخاب سد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26147" target="_blank">📅 16:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26146">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pS3Wm3L-wyTbVD9eR133-AUxzxDUlqXEbn7dBbzAa8LwW3FVH_ImDLfJFwwBOmR8hN8zeQ3l34UqBGZvWxtNimasfBBH-C93yfffw3UvNa4talB_8EdOHgKZ-0DFZip9aEDKUx26yzqdu3HHJFGMsXpSj5-O1MNDY8vbdQG5T086Cykb0mtyXKePR0zlROKRBOkN2mEiScBz68gs8zPWNK2N-4YlSoI0L2Oi7mAX-dta__1zUc3_HfUkSZg6sqhPkRvJdE2dY1c6Pwihg-vC9YwpiLLyvCuLn4C7HE6zkgEgvhX0B0GbihB_9eXjnO98jFnaoQsmKXU5qRnNnC2Blw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛بامخالفت‌تارتارسرمربی پرسپولیس جدایی محمد عمری وینگر سرخ ها از این‌ تیم منتفی شد. ضمن‌اینکه محمد عمری برای تمدید قراردادش با باشگاه به مدت سه فصل دیگر به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26146" target="_blank">📅 16:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26144">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VzE46063BafDaXSAzwYSVk5VPUQ34RUjAf7q1tiokRZego5iNbGyjFW9TUj_mehNq07uOBavKxL02QdZRnCmJgMXxFuIlBV4UAv4xQBlbrJGLvvuPR_7O3nWWmkJOhD0mPz7BosEqbvvaG4xoza-n16ON4JDRbrUr3LJsK0Jh0yUZCq_7aFlIirC8LDJFAjq55DTD6U9g6rT5ZFSsZbuaaCuq0-lRxC4tEsGraqWDby0m3t83z8dRRW0_oeHjEta3RKnuMT2ynTZA11MAJEDjFivMuMth85wrYBHEW9xXcMH0rW1QJUrRCnb6R-Uegk9ubHMnl1iPN4bjbgdatHxHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PE59kq5VQjZk8u7EcTuqvWyJmaWsyS0c0UWpiSZfIWXXZ01VodX_uQWIGls4tMcB7ZN1ynwLgcp4a7Ss27jbrfwdSA_imLfKuAyHVvzV4MGw4ySn-YuROgfZovU4L68hhULLBJu866N6lmh509FJxQvEMGaXKqRGy9dbOJtKrs1azHk38TCLmAHwY_Ibw5J57p71i1nsCsCOsxYjYYYszmUsZuwgKJJR7SAQTs8yNNtR7g3I2sPxHTJqeqcS9JQspW5jvO8xSvadtrP7Lz9uhUTErKE3m94HZoBKyTpXyA-hTMgItgGdLu2Q9KDII1ufIMHx5205AIPb20cv-mDQ5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26144" target="_blank">📅 16:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26143">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqyJtozMzqEdhJ1Zc2_lWx_ELSN-08eKda7OO00_zttXb9v2sHlfKhfls61CEIHkMRSDvoFSFYuaBgfhmMwY_WU-LzFO6jNWkopnlyq0QqiBIVDtPJE8s_yQIkwNlZMpE8st29AblaD6xLbTS4KcNs3RCT1lM6J0pMqvRbOEjdup59X7RNO7KYF0Y8w9nKs6NfgxOeBwhf7V8M6SR8P2s77F6OuNNIguXWYfQl_nVzBCnzkX_2lnPr9QB2XF82oB0LGjqeA7SjMHmZBuzrR6UVrKWbFNO_vSmaV6Tw4AyoQVXioMlqvvjdTiZbN8g7u8yEBW-OkX-7YOETFRbvGCnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لئونور ملکه‌آینده‌اسپانیا: بی‌محلی به گاوی؟ من اصلا همچین ادمی رو تومراسم‌دیشب ندیدم. بچه‌ها فوق‌العاده‌بودند و یک‌شب‌استثتایی برای تموم مردم اسپانیا ساختند. نمیخوام راجب گذشته حرف بزنم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26143" target="_blank">📅 16:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26142">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gX5MSAGRU2pVvILllUT7wrk4e_1dgqm6bGDqtvjGHoqIoHMNUMN66PWisKI__pSOYA70kcHc5NoUJylEJDPWNLuXwZcZZOcXnknHLytPINn5b63LWRsKYm81tGOpL4Fi6O0TX0tUQheLNcMWxfl2LYc3isTo2Ib-2YFRc6bp27cilu5FKa_-uB5sHSlwYgKuDG0uFiuaFoghTGKiNVRnk2zd56wjfdCi7B9j9klUjeeodoneRpqTZZeBXiih5-_VmL1rd5gF96ClorzPkQNMLw-BCME7GkvNnD7dK5QAG8LHGTyiGAsPZyrL0SN-6f37e4hmrSPLduTZbBbZDSMuRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال ستاره جوان اسپانیا و دوست دخترش همراه با کاپ قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26142" target="_blank">📅 15:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26141">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JR64UJsnjObJsse2CUnr6_sTf3FgZmZDvP1ruB1JUrO-m6wCzB2iQCN2EwaRvIlgf3ILygkMv3zSiildnYOTBZQIlFq4MzmiyuV6TUjeHXyeBZ8e-RvcynzPGMb-M2_iqgrEK_vOwTXu6VXHZBLEuW_SWnpHa-isyVPLS6jFlDyCGtmrSBl_v7suzKWEM68EiaKob9iqtS0mCVcd0ksfNTxoLEU0fglMLXmgnqc-e8YEbNsxUMAzFlQop8l3_GVyhcSBtUEJTDHdCG6-A26ncgTBNowVISf5YVVj8MW4-miz8az29inKT2KLT0CngEWzJ5hqPdgj8bCSuX_VfAypMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26141" target="_blank">📅 15:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26140">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6473e7bf72.mp4?token=SECgLq2pyVwifJeLjwW5hManwMP_cBcd7_k5yIVFdt5SEEhpZWh0ID7cjf7JK6n1w1uldMFe06Osg4897xxKom43eSs1wVVyaWi8RF5A8UknSUHxOHLHMDipLjpbkjzsKG5YFsHvIK82yPXrStHZikNFMGWOMxvHLuUJ5LbIkFlBWAHovQoD4DbbuBkkuYczxjgtuBFoo0GOR9_vvWNeJE_BAWei6lcwlTn4bSpewd88IgDdeQOUDwOyzQ3useJRTjXzFOypWPq4RNwqGWGJvIOYGYBZbMiFbXbDiVp4vIcz5yIZQWkIMRnh2a4ELC5IzPeYHOrxaQTbu4SAICHPIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6473e7bf72.mp4?token=SECgLq2pyVwifJeLjwW5hManwMP_cBcd7_k5yIVFdt5SEEhpZWh0ID7cjf7JK6n1w1uldMFe06Osg4897xxKom43eSs1wVVyaWi8RF5A8UknSUHxOHLHMDipLjpbkjzsKG5YFsHvIK82yPXrStHZikNFMGWOMxvHLuUJ5LbIkFlBWAHovQoD4DbbuBkkuYczxjgtuBFoo0GOR9_vvWNeJE_BAWei6lcwlTn4bSpewd88IgDdeQOUDwOyzQ3useJRTjXzFOypWPq4RNwqGWGJvIOYGYBZbMiFbXbDiVp4vIcz5yIZQWkIMRnh2a4ELC5IzPeYHOrxaQTbu4SAICHPIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس فوق سنگین روزبه حصاری بازیگر مطرح سینما به علیرضا بیرانوند
: اینجا ایرانه چاله میدون نیست. با کشتی گرفتن با بزرگ‌تر از خودمون بزرگ نمیشیم با احترام کردن به بزرگ تر، بزرگ میشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26140" target="_blank">📅 15:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26139">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/of50ixJ5R8RQp_NZAkxBCYZUdXsOudtpeem6dAss-r9Pj_h8iTD7IUYHl8hy8fsk1hNaCfQOfoaibCjiK74UedhCXDIKytrCVJCXi42xlJmKPL5EHKJ0BQe2UMOyvZKzMcwira1HztEt8pxdHVppPUMOqwuBEjV3H0VdgRbxUKNncbaMwEnag4qTpeas352fMoNAJbOAdxP6p0S3Fjfi1QXC9QQzq3Dd-AeFrTixZWm68trKlKmn-kLOvlp5GT9LbfVs7CnQuQpQCaWjXv4ZIOh7d3S2pAcDftJQlBEzj0fSVSMsfqGcEVQRlr0rtPIva6rb0S9UWqxrckieewyCdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26139" target="_blank">📅 15:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26138">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSUcJpMQ63axNS1OplZ9L57lJB6z3sn1KZdgGxbSC6niBYRld3g9R1KPkR-73iw8P0Eym40Q8E2KqQ9UG3Giopowaaq_yNRVlhXuyuHF1JCJGGYZ6zYGOWtgawV-F1ROmnsjO2Z-YKOjmyaItOBVqw7CJ3SlnmPT2Cw5rsAc3_yyI3s65pfTyZwJ2uKy5nXqajFKqsp421C_n5tJn_NCmqAxs52or-7eii4PgV_XqOWwum0LLJ9dy-UbNJW5eL_7_xgVdQM1Mv-_rwYp9poVTJf1W4iM8PSFwis2UBKrQjhU-Ou_MHm-E-8FWpDZIcMJ1XoM7V5Ko5CUorYyf6pXhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
آرمین سهرابیان مدافع میانی سابق تیم استقلال باعقدقراردادی دو ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26138" target="_blank">📅 14:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26137">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LI7kQr6PpuziFOZl6agHAQ4UgBVTl_I3NUv9uN_ITMKkJIASAqMn_j4qv8fB5sxu6v1ySB_LBI-ph_YOWBjg3eehkcX95rnKLTo-nTX9etNlH9fBhTxaSvigTw6xFm9ooMO0oGnciSO-VIqbV4LtZn6WL-af9hjhbjWEj3zQnAqN3-i_7rX2rYNblsnduCGV4g3KRg4IlmIRI_SEABUEUlt8clNwKTkl1JahjutBeRDjrwGZ-Ki6MZY8lmWQ8mnBHi_9oTMK4zCGWkqxVs7_QY0k9Whwgo8-KscaWun-_kZwVYx9ke4lGn9N2kId5Dk5mG5mMfB7fXMS3agkAuH4cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام مدیربرنامه‌های عارف غلامی و آرمین سهرابیان در ترانسفر مارکت؛ این دو مدافع میانی از جمع آبی پوشان پایتخت رسما جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26137" target="_blank">📅 14:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26136">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه فینال جام جهانی 2026 شب گذشته عادل فردوسی پور؛ برنامه جذابی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26136" target="_blank">📅 14:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26135">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bd8QyH8UyN92u0DG7sHuzWjfgM-Tbu1CC5VmVgrGihbq1TytEaCpK_2wZJ9bSbfn1HKzo6fclmbiQ--Ikg1FjWsd5pW9Exf6VZnF3D3j9VDkKj-Wm2pdZkLnbf09AloZOzFdN-3T7Uumg4iXsIVCtDYAgVvIeoqVH2tojGzvlBomPGko43AW8q079UbcX7a4mTdiKACdm39IqWkOgshSOuoPyGIpy07r_e7vtYu-YNMqQW_vQcTZdSSE_9zGUloOHRW3C6bjE0y_yVX7MsfepZu0P5IVayEI_JsNr1Jqd5lt0puqICrusEz-KRWeutwlYfGKeu8VXFYBHdeJVrKocQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیران هلدینگ خلیج فارس از عملکرد مدیریت‌فعلی باشگاه استقلال به هیچ‌عنوان رضایت ندارد و در هفته پیش تغییرات گسترده‌ای که مدیریت آبی پوشان رخ خواهد داد.
❌
علت نارضایتی هلدینگ بابت هزیته هنگفت برای جذب ستاره های خارجی استقلال در…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26135" target="_blank">📅 13:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26134">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpkZQSyAIzdI5HPC_9BCSA5qx3JoDjpJW0Xf3hqeS2AfijqGEE75jmJwWptADgpeIOJXz6R0Rbqt55uLlBK5H7ZPEMQjD38eL5Zsk22L1rlpOcv2NVJMYYk8rgFxK9pLbiVMaq-RQt16rdj1VIqPGmKJzRLf5IUmV1K5D4UrsUU1i9AQXsCHIdzYPOSm0UplWtoV8NhDEyMdiuYOdnSXXsGiXYHckdNgNjaN2SXx3aPIcnbh8r4PmfMLt9Q5YP7TsWB2ewNTiVsHYMeJl3ngrdMwTJRZ4unjA_2j2cPavBYO_2Y1JWngUIdugx4bu-uDUZQtG1P7uI350KpxQSqqLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26134" target="_blank">📅 13:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26132">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWe2YLRADYyVwfNj_ugPFuUp_BkDIASgmWcF_sAy5hTFMfpJ809hW67x_Wj4tGkoQHy-qVxKdExdhOqohbIxToi4UEUR89ptwEmycX5A_R4nZGg3c-PiqXAJ4rxLER5xtVcsSoIpunTBhTGVouUgRjQbPeUJV6bpQAzYwTGiVskJrGtwzhyAWfjdRScZ7UaVO_1Cwk_fA34LJhNDpN2mZhRFcVmMe5SHeIEJAzqNkxp484_aiwqba6bE4F92UDDJuTiOVjtWjnLZvOHwOEjGUNeqnFrUdcIkCZoeEPShHiict63J_g4zfOhqwr8ZG5UFv8hz_7sJDL7xQZfOexytPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26132" target="_blank">📅 12:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26131">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsxkIBmZk_FBbexV22fohC6dFLvexzFimRt9XwrLk7JpIPDJzoWakEFfFn5fazG7q91bYxNSCRd67LIlp2MQH6vBtk-nreqga7HIRUeEP70LugjPEUtjD4SDEwdHzZk8Ncgqn-t1duiqs7fm3uJQ121XEJJqZlDFaekUyO7Vt-yFc28Ls3r85ZuQzHSe8eeRdBtR2yIroWUdJrcDuI0VL3TLdygjtTNXVELRevb_3V6jfjFGABO7LGja2lom1O0KAmCQMlFsloMtjaAH3Q-ljwoQUUWmXeAlMMJUlJ_xdr0JtWM7JwH98RbG1ZWul9yiFT427hjoj71vXOf0fr64-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26131" target="_blank">📅 11:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26130">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/il5jWLWly2fqpLL0fm15IJGCPAkZB0hy3m5uJ6jpoV-7esXFEpSqAb4fcQ22bcboK3LIjbzBvi93QyYnczZNNS_UuBxKir4Doka3q6WXI47HWglglQtSev36n2tBdwNE8ifZ5aJBK_cuDiUUb8ael4Gnnk5jeLaIqAVYdKdF3ro6baxBke5w5d9d62O-6dvxGmVwlT5jngJunrHr1gmUM46CEk3x5QkuqvGRUK_n4hMmbzGFRDHkPcZ4ACzWTwx5YoPADDG7ID-0MUhfcz8-kyc6ufWcatWwd68uWcIqN7S6swLhlbLVcYsvL0ZRSOmIyZL0xuH8GPi0NKzs0R-u4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26130" target="_blank">📅 11:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26129">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrIsbJp0YBP7mPvMC42Vg-CCWPhTpVKWhUimq__sx7uH4IHmSwgFQNKkhE4IR4scLVz01mHQOfDPxuHwh6cRqqlaKPwCG_5nZFVYUOXkb5ugi6ezSPK8_c9pIl_Vlh72mcT_iaXDA8AfUWNDtPXzeohe-8pV2JdP99VNGbwXxMFxwrL_Jo1FLSyqH8VHyPGSk-b0Dm2CRs94f2P3IevZi2OKecWDe2G0t-0_9D0p9Na4PFwNTbssymgDzhy6KuTIOmZcNP2BSth4nLQJG9Mi3FeLtML2NKqJqsXTQu8Xyos0qyLFA7urJkxjVaUXogHCoeFU4ljweEfTFVi-0h4LMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#فوری؛ باشگاه پاری‌ سن ژرمن بزودی قرار دادی چهار ساله به فران تورس اسپانیایی تا تابستان 2030امضاخواهد‌کرد. تورس به مدیران‌بارسا اعلام کرده که‌دیگر‌علاقه‌ای به موندن دراین باشگاه ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26129" target="_blank">📅 11:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26128">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202f77d369.mp4?token=mNivYloZQ7LMgtjUxGCSEM6GEL57o51OlpYUQfRLlagDUZ7NtK9YQkmfulLVamMSb-KOBo1-AVxbUIvaV4rlFIu4bPg31cREUstyv8OSea1WTZ1_oJ2DqLFNdmPA5gx5wjTKuvetRpragiWw-Jw4di_j6yYux5xMuVddRhMReWCzF9aoN7oJMiWpeEfonStoAhOzL5dQ0EQFphNd7-15yxlFtUqHQbWN8kBmjSqtt9IfglT_OsREW3fAf5q_cFdq8GIkShwAVG0noByKerzBZow-eLuIwZQUnpSfafkW_oYP-PG2LQeichhllyvWBZPURugKCeEDBzRNTI2GV1Ul2qzS3qpgSNfqSxU27bXTL8nA2Lh2AU3j-stTMg9atdKr5FbCIBMKgTB_SSgUT22Np5Pu40t7L-ryWaBO2czaXSByhyy8pZL5KcKFtX6bZ_4O_CDtTkfKO-eI_ttkQZejRZTLyBiBG2ahBqupbdMeR24fuQSkcrr_0IznHElenU0LXH_jbzdPqY2wby8PrfCimVi2GFIFGE3Jf4BoPcNa4jz9WSy17zXDCT_Y0KskdRvF-L0T_BWc_9_65SlhfWKzlNIdt1-F0s_x7OcJirI-xMrvVxOf9F4FA1YQVFyuyUJ_DL86wmbqqRIpKXGQLnCat8TbUxik0Fe1kPLDvYOqqLU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202f77d369.mp4?token=mNivYloZQ7LMgtjUxGCSEM6GEL57o51OlpYUQfRLlagDUZ7NtK9YQkmfulLVamMSb-KOBo1-AVxbUIvaV4rlFIu4bPg31cREUstyv8OSea1WTZ1_oJ2DqLFNdmPA5gx5wjTKuvetRpragiWw-Jw4di_j6yYux5xMuVddRhMReWCzF9aoN7oJMiWpeEfonStoAhOzL5dQ0EQFphNd7-15yxlFtUqHQbWN8kBmjSqtt9IfglT_OsREW3fAf5q_cFdq8GIkShwAVG0noByKerzBZow-eLuIwZQUnpSfafkW_oYP-PG2LQeichhllyvWBZPURugKCeEDBzRNTI2GV1Ul2qzS3qpgSNfqSxU27bXTL8nA2Lh2AU3j-stTMg9atdKr5FbCIBMKgTB_SSgUT22Np5Pu40t7L-ryWaBO2czaXSByhyy8pZL5KcKFtX6bZ_4O_CDtTkfKO-eI_ttkQZejRZTLyBiBG2ahBqupbdMeR24fuQSkcrr_0IznHElenU0LXH_jbzdPqY2wby8PrfCimVi2GFIFGE3Jf4BoPcNa4jz9WSy17zXDCT_Y0KskdRvF-L0T_BWc_9_65SlhfWKzlNIdt1-F0s_x7OcJirI-xMrvVxOf9F4FA1YQVFyuyUJ_DL86wmbqqRIpKXGQLnCat8TbUxik0Fe1kPLDvYOqqLU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26128" target="_blank">📅 11:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26127">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3tF2L1TMnxdaf74w9QlNvsrYcU-xRpwQKlBxlnIhJTlErlqJsziBWy9KguDmYpdA9Y5DHNHeXMv6Ep8az3MW4Hp9EoCwgTNQ8GCGYBsvn14k-hOjB8YbLiBfe2oodWHy2Hr4DeNeBWAjY1bNaGD9i_FXaGZcrHqGMC6akvYuSIpC6H05FNhIqfY1ixB5UEfCvEC5xGap2bLFDuNAQdLHjT2o2ayD0fo2KFFhjKnCcltFqTlg3XPgi1FA28At_fvcAgAVPdL-QWhBcprvkjLo3RnDEq3r4XUMzGa-90tPwSyDw8kGt055jql3BTzBQc1M1wSzIGQaK4qwnuEKcGdaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27dd0a5169.mp4?token=EvLb2Y1FYqpZK9KO-QmFZuUr81yC_CD5MZJSLBCl7Kdy_O9Sato4b-Uxp4Qc45t_6VD5lWnBoRTxOq1jQ4fuhGEPT5ApxCxND-jCYQaZ_JLg9oyw6PgkmoGUBwji8Y3S_CH8WTKVgp2dYs5Yyu01tGdRzurC3w0AISfWjudfbmJRCwu5yQAtx2P9kXJNCWQeZLTVXPA5SDWMaMkoEEDSjMhSp2SHvRDKeQ1lc6aI91Xjj43gRN-kpHTad3WNAf-IbXyhI9c5N_KXqnP9xhs_77aG-JhW1r5EdA-DpLk9XHQBjsQTQwuxMp1cr9IuOTpeL6j6zNpbgyEb3KpafuA2tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27dd0a5169.mp4?token=EvLb2Y1FYqpZK9KO-QmFZuUr81yC_CD5MZJSLBCl7Kdy_O9Sato4b-Uxp4Qc45t_6VD5lWnBoRTxOq1jQ4fuhGEPT5ApxCxND-jCYQaZ_JLg9oyw6PgkmoGUBwji8Y3S_CH8WTKVgp2dYs5Yyu01tGdRzurC3w0AISfWjudfbmJRCwu5yQAtx2P9kXJNCWQeZLTVXPA5SDWMaMkoEEDSjMhSp2SHvRDKeQ1lc6aI91Xjj43gRN-kpHTad3WNAf-IbXyhI9c5N_KXqnP9xhs_77aG-JhW1r5EdA-DpLk9XHQBjsQTQwuxMp1cr9IuOTpeL6j6zNpbgyEb3KpafuA2tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🩵
آپدیت جدید تلگرام دیشب اومد؛
چند تا قابلیت جدید بااستفاده‌از هوش‌مصنوعی اومده. چندتا عکس رو میتونید مثل اینستگرام پست کنید تو یک پست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26126" target="_blank">📅 10:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26125">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a101f8f4.mp4?token=Dfx2hZiWES9Wbv-XCs9m0kWNjXCOPRR1dYpbr7g9aytCzD_n9W70eT16Iwd7mZmgaLss_b7hCtB48VQh9lqAxF4UN-KhS6J2NvZImLhQmZ_bf8XgqyQahhwIw7f9YbmUv02pP0dAZEViEa_XQ4GDI6tDqPVpgQ2GwShmaZdc55r3ijUaaPpEvM2qbb_k_hOGEWX0B3OBDSyFCiQEuUvo1FQE0JGvDAEzKJlkvjWisXjkrHt068Cpr0bztYTcDDo-k2ysEDV_NtvXGnFsf0_bD-JlfyBAMDXsoz_YvPW7Mkgi_iZhAhh3xk3ZYm3zidFOVpQOoPk493jNFyDpWbkcOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a101f8f4.mp4?token=Dfx2hZiWES9Wbv-XCs9m0kWNjXCOPRR1dYpbr7g9aytCzD_n9W70eT16Iwd7mZmgaLss_b7hCtB48VQh9lqAxF4UN-KhS6J2NvZImLhQmZ_bf8XgqyQahhwIw7f9YbmUv02pP0dAZEViEa_XQ4GDI6tDqPVpgQ2GwShmaZdc55r3ijUaaPpEvM2qbb_k_hOGEWX0B3OBDSyFCiQEuUvo1FQE0JGvDAEzKJlkvjWisXjkrHt068Cpr0bztYTcDDo-k2ysEDV_NtvXGnFsf0_bD-JlfyBAMDXsoz_YvPW7Mkgi_iZhAhh3xk3ZYm3zidFOVpQOoPk493jNFyDpWbkcOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26125" target="_blank">📅 10:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26124">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1235d344e.mp4?token=m-GnSXubx3o4pbkjCsqtD5TJM7WYKybcOw7tWZNN-ic3eec-NDNQvz4jWzmppzcGVF0z1Ci7eunz8L2OD43-porOYJ7jSJjQs0yfqK6MRmo05pVorQjJ7LCJuyoKE81LGzlq8O5P8rhXtLcz_tNxz6b01k6PJKJjNgKe1ootJ_rKeNrvkkpFTCYsDsKaffO0bdQzV-vESmHsY50Iv_DMXOejXaPJyMI0bFjux3tybCMM6sDzobh16fW143smWzNZFSTcmWmbzKFL_DGSn5WPRYYFwiSE3VRApv5S_oJExjKLg18Iq0iRq0-fhohl6sonoHkTVpmxLSmZrz-kPRv9FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1235d344e.mp4?token=m-GnSXubx3o4pbkjCsqtD5TJM7WYKybcOw7tWZNN-ic3eec-NDNQvz4jWzmppzcGVF0z1Ci7eunz8L2OD43-porOYJ7jSJjQs0yfqK6MRmo05pVorQjJ7LCJuyoKE81LGzlq8O5P8rhXtLcz_tNxz6b01k6PJKJjNgKe1ootJ_rKeNrvkkpFTCYsDsKaffO0bdQzV-vESmHsY50Iv_DMXOejXaPJyMI0bFjux3tybCMM6sDzobh16fW143smWzNZFSTcmWmbzKFL_DGSn5WPRYYFwiSE3VRApv5S_oJExjKLg18Iq0iRq0-fhohl6sonoHkTVpmxLSmZrz-kPRv9FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد ترامپ‌موقعی‌که‌کاپ‌رومیخواستن ببرن بالا ازپیش بازیکن‌هانمیرفت‌ بره‌ کنار؛ رئیسفیفا اینفانتینو دست ترامپ رو گرفت جدا شه از بازیکن‌ها، جدا نشد وایستاد تاکاپ ببرن بالا؛ فِش فِشه ها اتیش بازی بالای استادیوم چرا آبی بود. قرمزنبود! ازقبل بازی چرا آبی تدارک دیدن!؟ فکر میکردن تیم ملی آرژانتین میبره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26124" target="_blank">📅 10:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26122">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dt9jG49J87Oug_IBgYxNlktkPO5jt1hP5W-6KrynKCa-fNs7wTUXeyPRQqQi4sdXl3w4LS0RR4eR696MFcDcyO1_kABLPDh3zztM8bIKqaOj86vxRJfz2B8XzM1hPdErqd0SIronI06MNazIN4IxcTfb7HGBuViOnhJQmsMMfUyQtl-pi4hWHFCsu5cPJYfodr9LPqGussfd47hyeiQmVXnFvzrrD39VtFr-E0-C2qKiy-8DfjU4NQm2ta9wUNMGeoIqyKbgxAv3I5XC91okSR4j4IHaIv47ryk3KqvvBXE3pD5KWuhVqFkmbkshCH7y5eg4EabOKml8qQdh426N0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hEXXsEpPQy-djOTr1PwPdM5mAdRQHssLJgX3O98LGVVq6j6NlewKDCUQoFsN3LeGOJGqbFF9SV-QpTyS_dwQvOxu5UZ1agSlMtXxfQTfOGYSiElJtY5k8l5roJc93RudrLyEyTBiJjDsUdG2T-rmj-XVTF9liRjj3BjJMd7U9brzuJDGVS542sb4_E2fMyIrEwQeYf5cNXzJ3zTU6nCSM11tkfnbZZ8viJeS5ED8amN0WcZ2caHn9QcgMvqd8of2xJAxJxBp3YdsOcu_NuOak_45tCh6JINnOfc9xlp6Q5fiyh_sqcWzybKOP1GR5JkljIPk_kie8jAAJ72XUITbxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26122" target="_blank">📅 10:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26121">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c071bd0be.mp4?token=e_m8dLBRO0UyyxEihg-fi2maohTsRT6x1aIzpID1AsncBmPEprEcXsYMAL877vsaEUU3K1YD4l0p6RY6wjsHfMMhOyJYE4l51uAyndexw6xsSs4N-nwHRvR-iuChVtQ1avN6yZ9vEWoWCOF6ke-5ioSVAiyXVGzQJzP7W8oSDoN92SzEFw9LyGOiGmGT57VQ6rFI1Rtm14szlma40DQ9AHzsoXaXlUkqLfKoi4Mz40uy7HlbhXVsdODRLwozi0kPTahQ6NGYJDMu7jWnP7cWojEY-y6ZW1OG1q4POFrBCnyepXOiAplGGiXadi7zFTYoJuU0L9_guCBaNPhFXTA_bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c071bd0be.mp4?token=e_m8dLBRO0UyyxEihg-fi2maohTsRT6x1aIzpID1AsncBmPEprEcXsYMAL877vsaEUU3K1YD4l0p6RY6wjsHfMMhOyJYE4l51uAyndexw6xsSs4N-nwHRvR-iuChVtQ1avN6yZ9vEWoWCOF6ke-5ioSVAiyXVGzQJzP7W8oSDoN92SzEFw9LyGOiGmGT57VQ6rFI1Rtm14szlma40DQ9AHzsoXaXlUkqLfKoi4Mz40uy7HlbhXVsdODRLwozi0kPTahQ6NGYJDMu7jWnP7cWojEY-y6ZW1OG1q4POFrBCnyepXOiAplGGiXadi7zFTYoJuU0L9_guCBaNPhFXTA_bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حماسه‌جدید خیابانی دربرنامه زنده؛ خداحافظی اوس جواد با مسی و میراث مارادونا با شعر مدونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26121" target="_blank">📅 10:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26120">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=sDzn57a3y_1TnLfqlmb_T-1IgJByQlOYimFF38RlnkuZZL_In2J3lhApfgoQ6BKzXLRCc4If0Zd_kyDXYbdJaXjGIS3vrH0J9ev-HUo3Zl-Fq795DcYPnVidiUtdutKOcUG_g3nzoq12BsWMoEYg2Kh-34772l1T3LGSr2v0zx1gLXrwSypqPNjotuiIWtIVAV6aVQg2kNBhx3DKNaMyX_VNMZ433mXWGq_AkK0p1RvR9RLvJ852CCNxQUaODd38hqjbtebXqEf1M_PcpeGt2vozXdcZuJ5C6jc5put72qs4DnbZ2Im0xbyJ2dDwDhnNIE9-oDljW9qgtFo5a2JApg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=sDzn57a3y_1TnLfqlmb_T-1IgJByQlOYimFF38RlnkuZZL_In2J3lhApfgoQ6BKzXLRCc4If0Zd_kyDXYbdJaXjGIS3vrH0J9ev-HUo3Zl-Fq795DcYPnVidiUtdutKOcUG_g3nzoq12BsWMoEYg2Kh-34772l1T3LGSr2v0zx1gLXrwSypqPNjotuiIWtIVAV6aVQg2kNBhx3DKNaMyX_VNMZ433mXWGq_AkK0p1RvR9RLvJ852CCNxQUaODd38hqjbtebXqEf1M_PcpeGt2vozXdcZuJ5C6jc5put72qs4DnbZ2Im0xbyJ2dDwDhnNIE9-oDljW9qgtFo5a2JApg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
#تکمیلی؛ اینجا دیگه عادل آن‌فایر میشه و خطاب به قلعه نویی میگه من تو جنگ‌های این یک سال اخیر ازتهران‌تکون‌نخوردم ولی‌تویی‌که خودت هرسری فرار میکردی تو ویلات‌نیا ازاین‌حرفای‌عجیب‌وغریب بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26120" target="_blank">📅 03:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26119">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=vaOqEQwLfljI26j4G2c72aDJdF2urBgYEhqKXb4HuViNhhKPrZWkSh945aOkGYc8ji03MjaubNqApSKRGTd1CDvQYRQHxWQ4Q4_GIvlhOTBI5zbqahLc4Rdg0GngZhtKmqMjDG84EDJ6nkq7JzYfwu6xf_EJqFRyFSrRXMNRQir4dCvV_RpPdbTd5SuZi-oLVte8MroEcJYIUwEsWV561CM0t5dfO0leR8C9QDsc0vMeVkY8nzVz1_sCyjXj6fl9DxAb1KG2GO07n_Gaeb4bjLTjGpwwjlsN5eIqwiLFS1Q6Wd9_Pl0UM6k-usQ7m_x2qZJ34JTxzU_UOckEsDpMGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=vaOqEQwLfljI26j4G2c72aDJdF2urBgYEhqKXb4HuViNhhKPrZWkSh945aOkGYc8ji03MjaubNqApSKRGTd1CDvQYRQHxWQ4Q4_GIvlhOTBI5zbqahLc4Rdg0GngZhtKmqMjDG84EDJ6nkq7JzYfwu6xf_EJqFRyFSrRXMNRQir4dCvV_RpPdbTd5SuZi-oLVte8MroEcJYIUwEsWV561CM0t5dfO0leR8C9QDsc0vMeVkY8nzVz1_sCyjXj6fl9DxAb1KG2GO07n_Gaeb4bjLTjGpwwjlsN5eIqwiLFS1Q6Wd9_Pl0UM6k-usQ7m_x2qZJ34JTxzU_UOckEsDpMGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26119" target="_blank">📅 03:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26118">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=pCi_qBGgsyziR6cE44aQfQzZzY95BQ9NC66ch2zZX1fxDyt51z4j1rCvEw7cnRZvBdcvEnS_vO7kPc0LAHkzwXJH39WIoG3XVz15LOBplNZDcNBps7M-t1xRGNWa-XhFeqtPRnDHc__yUgpLkpNLK7ugPrkmcJmMN4szT_YfHRjDP5EfPKbk7_veeKbnGfBrt99vaA94PtkS3rjwc3qL-zv0iYv7ahF0JI4QH396_ykjptoQwk3fXSc-E0sXbE7muzXqm5TZWdAzQ67hZIdOnPieLT7g7ariRL1C9Af0xC_S4IyIjl-556dMZdB43S98Y8EM2wWAJcNjtT9D3rzuJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=pCi_qBGgsyziR6cE44aQfQzZzY95BQ9NC66ch2zZX1fxDyt51z4j1rCvEw7cnRZvBdcvEnS_vO7kPc0LAHkzwXJH39WIoG3XVz15LOBplNZDcNBps7M-t1xRGNWa-XhFeqtPRnDHc__yUgpLkpNLK7ugPrkmcJmMN4szT_YfHRjDP5EfPKbk7_veeKbnGfBrt99vaA94PtkS3rjwc3qL-zv0iYv7ahF0JI4QH396_ykjptoQwk3fXSc-E0sXbE7muzXqm5TZWdAzQ67hZIdOnPieLT7g7ariRL1C9Af0xC_S4IyIjl-556dMZdB43S98Y8EM2wWAJcNjtT9D3rzuJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26118" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26117">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94e4b0c7b.mp4?token=dOOkCvG5rE8yUGz1X28U3UYM54deXnDsAX5CEkZjEDGGFfXBlED_meQUXb9s1IbKKQYFGGEc4T2GvdpzmoZ55RfjdCdkv_rBAsZfq1qmEiGqZ3jH7t1ClCeSnZW9dyg_9QWqQcLt_dViO9iHKYRQH5c-HUOfr4YrSDdoUTcNfaM0yvCAzxSBmm8BxkzRwWs45fesAY4zLX30cf-JYcJQGdXlFcgCQ0ECKyVf-_YI3ZcJdn5c8V-g4TpUNuiOcZAy0tlvwFKvk487TtaFo45N3z-on99YPaebR26I3SM0LKBHcV9Gi-e3Bl-2Zj3kBcT4Ye7LeEUsX60QK9GgL30Zbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94e4b0c7b.mp4?token=dOOkCvG5rE8yUGz1X28U3UYM54deXnDsAX5CEkZjEDGGFfXBlED_meQUXb9s1IbKKQYFGGEc4T2GvdpzmoZ55RfjdCdkv_rBAsZfq1qmEiGqZ3jH7t1ClCeSnZW9dyg_9QWqQcLt_dViO9iHKYRQH5c-HUOfr4YrSDdoUTcNfaM0yvCAzxSBmm8BxkzRwWs45fesAY4zLX30cf-JYcJQGdXlFcgCQ0ECKyVf-_YI3ZcJdn5c8V-g4TpUNuiOcZAy0tlvwFKvk487TtaFo45N3z-on99YPaebR26I3SM0LKBHcV9Gi-e3Bl-2Zj3kBcT4Ye7LeEUsX60QK9GgL30Zbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نسل‌جدیدعلاقمندان‌به‌فوتبال:اینادقیقاکی بودن که بازی اسپانیا
🆚
آرژانتین روداشتن نگاه میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26117" target="_blank">📅 02:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26116">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e72188ac69.mp4?token=ZbBX4mm6IwcRqQREkxaa1I0uUR27ZrTiZzZELV4avZtnVZqrj3mPeOV1RRgqCHsuwri-3J3cVnWsH340kLZbEJdN68_MCR-2q2PN2Livb3fNE9Fh0DN64q2rHG2zRwHS9SONFG_H8eNuT9DGZH6WpgoopDYwWud8ljo5965PmvbSgWub_z0hGuC4tg3pllmgrphzXuxDYfgx0geV5HAnHmJtkfaykBJYnGatByc9ZsPtqegQvicLksv9c_lpBG_OAJewBWEiTqoKUiZYB5yC7dz5byLpn_15PnOE1VbKQQj8GVY1aCxNDP_uZNM0dvfCOTG-FCO_EPfW3UNDTOvVfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e72188ac69.mp4?token=ZbBX4mm6IwcRqQREkxaa1I0uUR27ZrTiZzZELV4avZtnVZqrj3mPeOV1RRgqCHsuwri-3J3cVnWsH340kLZbEJdN68_MCR-2q2PN2Livb3fNE9Fh0DN64q2rHG2zRwHS9SONFG_H8eNuT9DGZH6WpgoopDYwWud8ljo5965PmvbSgWub_z0hGuC4tg3pllmgrphzXuxDYfgx0geV5HAnHmJtkfaykBJYnGatByc9ZsPtqegQvicLksv9c_lpBG_OAJewBWEiTqoKUiZYB5yC7dz5byLpn_15PnOE1VbKQQj8GVY1aCxNDP_uZNM0dvfCOTG-FCO_EPfW3UNDTOvVfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نسل‌جدیدعلاقمندان‌به‌فوتبال:
اینادقیقاکی بودن که بازی اسپانیا
🆚
آرژانتین روداشتن نگاه میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26116" target="_blank">📅 02:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26114">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LM-WLncrmgFRWHyxUtlmFosrthJ1fdpXeOQxArt6cngVMuueYD5Ot8Sr6xJpW9Cs0FsJA3b-n65JyS_QDTd3FzsplnlkZ6kA5mb1aouttuE9YiDD4bilTNeCVGw-uNnG_FJxBSx0pB4sZGH67dWbLZggBAWxnXn0C8qKN104TLmrhQPmFuX4IoL2RuCifRD0skhfM-mGLvHzgaw4SvZRSYL2hkngfxKPt5zrGgffmoOxLu1avCXRhZgni2aEnFMobc9R1azXLFGdKNsMv5z6JbI0wrtXbL4yQeTftm7YyUSFNZjUa2y9UauDbzvrtBrIoMtZkIrBi9l6QVczXqXy2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛ سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26114" target="_blank">📅 02:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26113">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nevajvB9L8AbevUZbheBYDm3UO9DUAwUWKOfKke7Tl1EFLVtRy3MO8OYFaUOgdH82ivT37WOZvI-GRDdWUlV6AH-VrS44ZEPhrCGj2AXWVSGB97jlLnM3PP8_oRKOI98WEG4pR9G0wYbRwnCir5xHLEGMioOnf7ThftHyk0IdVqRblAN7adkooY6aZOBeNpYAlU5UtTXdgabkDylEEweUL9h579D0K3seALKWhqQfCFtNmwZBqQyT1yVse3yeTdwEvsZzqt-M_6YxcggSKOP-pdiNrB_4YDA0ZdUefjIRTh6-F8X1JIf1NgfEeMdfc0kidfHgrSwimQ2RPH2pWmLvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26113" target="_blank">📅 02:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26112">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u98fkJl5X8dCylVplRMOygZs2EbacmLSLQUFkmSApVSsPtre-llMQIMqHiCPe59rTzgIBJ9tHW-6NpwyBvtBLmQRw8zDCr6KOK8g8P0UAqihKP5mDUCmwC5xwZgzys7eJw5xnF8QmoWBBz6R3ETLKf3wU2_OlG_DMR1dxoKR_Se3_ZiK0pemKi-oGDGDcba96XJ716qMalNubxMm3n2MnKQzTGp1yBg_v2bfi8zc1WR3-Mhqv5No4LYOdpD8EeY0Jpl9I5HxIJP5z_4OhDpn7WI0NmtuyKpOz8Oj82pX2IXJtwXmJRE6KKUCuVhuhCcgBWNVA1Bf2t0yIKTwYDUuvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فکت؛باحذف انگلیس،ایران، اسپانیا و آرژانتین تنها تیم‌های شکست‌ناپذیرجام‌جهانی هستند! اسپانیا و آرژانتین بدبخت باید تا آخرین نفس برای قهرمانی بجنگند، اما ایران؟! ایران یک مأموریت مهم‌تر دارد؛ حفظ رکورد شکست‌ ناپذیری! دو تیم برای بالا بردن جام‌جهانی میدوند…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26112" target="_blank">📅 02:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26111">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F31GKHcTDGQT4L01Tf-sziOVJ7GFuqJGWngf-oyhblG7WW0w4F11OF6fs1FmgkAO95knYolKfP-7cx588e9c3W0OE9AT3DjzTvbasbfMfRhg7WW6y0eA4YByem1zC0fmzmSE9jLRu9ySzMp7qtek77BAuCVq_86bRxpiO6uqTJ4VfYBZhTfkBQcf-bDvNOunRr4VXt660bem6F9j5P5KrIhBQTxtR5tCcaMJYz-gM8LJxgK_UptT25hhenAJQByLllOxs94kanQW-1c9QL7-0_Y7vXatdA4lQuF8z6huizsbqH9thAtcouJBz-giauSzDFKr64GZ66IH2T7KWlmXLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با عدم گلزنی لیونل مسی در فینال؛ کیلیان امباپه با 10 گل‌زده آقای گل‌ جام‌جهانی 2026 شد. همچنین امباپه با 22 گل‌زده‌لقب‌بهترین گلزن‌تاریخ رقابت های جام جهانی رو دوره بعدی مسابقات از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26111" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26110">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ju4Xpe8-bJ0hYyrE85CCt9DWDn4SIPdWfLTX3sNAkxR3FyifZteSPEt6gTHQxNKBxAb1wolSoLESsyT-bwtoMb_scCUumG4OMLYc68WHwZwFqGzVSdDvEk0WJEd62AKXfBBlGI7bwYx7o0FoybtRNWiyzDJP43nhhA0JyfhCdz4Bn8O15ufsqEu6R8EU3_byaqhdRs_RMjgQiO1tHLXoJP_06GIeDyHyFmUMHjsK-Z3A4hC6UMuUorotKyRnx5vEG1ozdqu8cr8X6-uzi1j3KUllxIO0XW7oc3rYjn45yHREpOPdlhyQYZKwCe5ahafYDsESv6iOI6KYg70aBjnvPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
پایان جام‌جهانی 2026 باقهرمانی اسپانیایی‌ها و گل نجات‌بخش فران تورس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26110" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26109">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACFMev-ODfal_UICdZHZV5OkXRabsS8MLTP3hoOmrSSt2FK79X1HM04nTRe9Xmyd5IvQxFsz3uBu3Oi1e7vHCGvE2tI0NU5ZMuwlEYEpk7og_hpedSRAeq9EHKXHjQQ35S_725eSPvbq0IJgJ0PKdLlIhaHsWaJeKCUDvTboSMzHqWPb_ydE8miRw4gNwGNTsPaReLQtVjxIL5ykYLiIGTV5_xMztxKCVCmN9733HYjomzgH7bRa-pbpZzkJSTHcmFd7NXrx13mcwM5ui_GmD69gUPcLDqPnvnXUocY9zaDjbYTILGTPCIWEAnT2-gIgDnSjMGNTZBQSbYaIcelnKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرژانتین وقتی فینال رو به‌اسپانیایی‌ها باخت که دریک رپر کانادایی روبرد آرژانتین شرط بسته بود. او در این جام جهانی روی هم 10 میلیون دلار باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26109" target="_blank">📅 01:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26108">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teYk9p_aiP-3aAylLfdVVcUYCorYSf0NWzhyI393vH0HwZ5dfssglcna0uDYUA6-qEuEPAKDrSGp6_4SKQVE1xh_OjD6QW6IRhI3pKupjuH6tbp_M5s73aIX5CbRjxR2RaxvAQJm_18NZXjo6z4d0UnZmJbruN4Ur_GwZTz8Tbe93Jruxnh4SaNw-cvyBXeXTSl9YS5QxYgrrVX6_JIFteVLLikjoGHX_4QZ7GUkm_nQgvWsZ03EkeSVC9DEt8G24u4zhTYKIQ40lvO4YIsCbp8dzAC0nSewErYY5aXHhqvMzs0lkQOfhjxSJnmhJn70UUwVJKchbibsBrosINjiDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید بلینگهام هم اومد:) فینال هم یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26108" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26106">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9oJDPSm18CwHsVO1aBv6nbHOU9iJIH7n-Tj8bd-oDpIvb7mdpY7gqiRZFk_miXpIdAXHxV0wS7gEYKyaDiOLoN0CO99eDalBVO3QMDqpR0qV2BNMNnAGuYAwptDE6tvnxACURIjXsJ29p8oFSiI2SZwpaZuD_R6BQ_EJa-4g2xVCDOUlWz4EjYW07QTyenwZZp9yym9RAdgAczjOjz7vjLkKkZax5fd1MlZSFS9EDKeqAlRX3A51bngMnDP49mi29FLTvGkne6xPGCAhz4FnnAVR7cJHfT981XpG53rKvquXaWW-0y-ht1Eua0qpEV8qxHSolpRbvSJHh1fpKuATg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26106" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26105">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKVfxfdmymmGjpOUrJXEsWrTJusCfjCnU0gwAzdmbllwLmH5bh8e91hAGCkgabsUmiwGxTcRJCPX22txTOHOARYds9600kEqg-M_xXvEQRjG5P1NAJO31N-JMjbRPqcYDBqvzZCdOP2rNIYd_-wXQaRro7v8uI3kyggJxMM3Z8S81bZni9umk79ftOkn7ZAhEjVColiLP_0Llrxld2-rTEZDflklsaVhTZA9zy5v40ENHfWVKR8r7vNaVhaOk-HPen53F0P7bNKpWDkIGWfdJ48AMFN78IveWRWVCoqwfVWeUCoxH2CFDRF-g8qz_TgZtwgdvZfY5_Q_qfDMZHo04Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26105" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26104">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-4-5M3lPE2KLY4etIPkjVzModrzbuK8eN9j00Lo5QBD2HTQIYaxrIbgny-jUWADTv2sAqMXEPHXJxmXchbxzFxP4olz11aaiLstphU8A9TAjkec8intHZXyOzXKYDs9d-I7F_ItR2URZ9PfsND3o9vaAl6f7Hf1ozOBA80wj4caMuFfjDki1bkQbduMzqOx3dk8ewZhs7jeh40GR4XF7dqFtQc3l-ffR00tsxmQMWGFPUbR7DU6t09Ll90iEThSGFxsr6wEfwBRU4SKbQi_YZyTjXBHyef597yP7mu3EguMfR5w2xxWkekzVpJsQnhFWaS9I4NH_FBT2kfKto59RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بعداز 12 سیو بالاخره‌مارتینز تسلیم‌شد؛ گل اول اسپانیا به آرژانتین توسط فران تورس در دقیقه 108
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26104" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26103">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b656d9cc6.mp4?token=swtPc1l9szlx5G4iJ9r1zpG6CDgamtag9-KPddQVegaFSGNAWWjeICbV6LM8FoJGraYF83oVrHbKL4LHXaheJ4hToy7Mvu6vCpL6QcGVk06KbdkJMjPVaMls2Es9Ep8MTTMhSoQdsyLfWvyRNRsjnHRpjVNdLfHp3YnCK_5N3aZMYGpMxxzSBEPlWsUv8zgIREPNPes1wm596_dvEmJJqIWBZ3Mo8iaf25vx0ubAqnozu52ZdLNmAZs68CZ1YvJER7SlDmAuCy63Fg2--JqiiYr4Hxb7TfcNwJQD8KzNf7t8qTdNgqMnbGaWscuI8-wgxchC5po7A8z4jsceWFkizw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b656d9cc6.mp4?token=swtPc1l9szlx5G4iJ9r1zpG6CDgamtag9-KPddQVegaFSGNAWWjeICbV6LM8FoJGraYF83oVrHbKL4LHXaheJ4hToy7Mvu6vCpL6QcGVk06KbdkJMjPVaMls2Es9Ep8MTTMhSoQdsyLfWvyRNRsjnHRpjVNdLfHp3YnCK_5N3aZMYGpMxxzSBEPlWsUv8zgIREPNPes1wm596_dvEmJJqIWBZ3Mo8iaf25vx0ubAqnozu52ZdLNmAZs68CZ1YvJER7SlDmAuCy63Fg2--JqiiYr4Hxb7TfcNwJQD8KzNf7t8qTdNgqMnbGaWscuI8-wgxchC5po7A8z4jsceWFkizw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26103" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26102">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBhzXVTr8nk00l2glxVnzQLHNB2jREiiAWYqzRqsjO5bawXQOi3VfjJQ_x-lQbKSQbpSVwqueUAcoiGIeZ6g34p2QyEJB0VErAjsQqjjwZsPtNXQCg4uDBOXOhUzG4iQGEoh27dQzx6CI0kBNZE_bXOfmrOHCTmHz2Z_Mc0QBc9KbCU572wahOUHojquuS41puuFREECd4ajsgTYLye9cxqdG1sobzuKDt3crn_EAYnwpvWkgT-lpaaV1FUNj9fL1btGXKmLUcTWa08uILQBwTDKs_kUHzeu403_JhFWYPvPJXCnqmqRATzB3a0PkaBzym5GudXT_lpX1qau7RZMQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
ارزانترین بلیط برای فینال جام جهانی ۴۴۵۱ دلار و گرانترین آن ۱۸۸,۸۰۳ دلار قیمت خورده است. به‌عبارتی ارزانترین : ۸۴۱ میلیون تومان و گرانترین: ۳۵ میلیارد تومان و ۶۸۳ میلیون تومان ناقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26102" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26100">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TPDsZPzdYwNCMykTTrfmqBTOX270WUN_i70J2doI7Bq2fdKdR9a6DZ5FevTaf-rWdh91IVVKfQqHOY6_ZMkkI2oH3deJWRn5NHK_XSOy_YVg008jrikdB-wxJFFvpW0n8hIjUfO1gOKCYf0kAn7ZycIa-CRc-HCoYkhybhnWM8s-JT6IEhFwcLw_DmBIQONncv-bkQJ1JskIedTIgADI40uF8Er0fKZgjxkpc5DeBReUavSogrAOZd2M2BH71BX3EbUy9AAXfVu2B3Ibj2QyTObybWRy0NBxrjmd608uRtjzEsZ3Wu0MG0W8remOTUl_eIX4FHwx2zCRAVftxOxjhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wz0BwyK_YgmxwF6nlcnXVaSSXMnaA3LBKba2Bvabuy_uBL1jdgVw80L4Ui5KzMTiT_tUspthY5wKqddVuCXrBAEXdLnZ97oJ6COqeB8_S1xHp_31egCCKT-AOckqcp66VTCaPiI2GugRfgPwgo0Fos_LNrzet1-tfZlzngcfQCMZwUDee7L5qvE7_-rM8jPYzTLsGu9iFfHUNUf9V4L6zxbkGcpWCzBzBd4vk9dyicOeA2yuwf4NcD407CDDuwcNmYVqVaTORWWLJfAGAdvi3C0Ryf_eV8dP4Aoqex1SjQNvVeo842t6tSVf_CjV1V727oAfD0Zd0w6fPQc-VuJJow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
ملکهٔ آیندهٔ کشور اسپانیا به‌تازگی به‌ طور رسمی سه‌سال‌آموزش‌نظامی خود را به پایان رسانده است؛ ازش پرسیدن هنوزهم به گاوی فکر میکنی؟ خندیده گفته دیگه نمیخوام راجب این موضوع حرف بزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26100" target="_blank">📅 00:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26098">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mqcjyf_HdtQym4NJUPPtosxoIBoSG4BXGbqSAlAc3zMtG_Ps2U9rIy-joWONAj-MZroBX1B0C4B6ZPhiJ4-WyJDm1BfuC_n_DlW9Lzu8qDCiTGhPR3dAbxVAksMSmYNryTi5-E9-pG6dOwGF-vMpPqFi1HDAkJXUXc-RklTbhzcss5s1DX8HSjh56MypmP1XhAO7P3kJ7aKLQ-fqlKwG-JaMAH4Q0vCZr9jJiFYJaHPJ5C1ZG2jsYba4ibARxb0TGGmbLgQmWvL1-qjFKOala570i9UBpsf6wZXLOm83mV7qNFkAWCPx0R1d4j-xni8mPuzvZFWswqTUVBOEJv1-jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K9ldLSozMYlFe1AvpX_JNBTztV4yVfeJ-OAR4349GNYSodpDfk2QrEC0tl8xKh7ShqJ598MkrfkNxyrGZkEsxNSGViD0jtlLyAqh6Xs_pGFPBVKT-D0sznfRpQrfQPEMNIZzQjt0RavIBe34DQ7Q5VOS4bSlxNxiqGFGBtUPvG5_WlfmnNfZT11fi2xOwDnrBCGSfUrzCJu_84DysLs21PtLdHi6BUkBJ8VQtfKT0zoYWSFIlysfgFI0Ipy43ilxFhgAaIIvx6smkpVJ_N9EvDKrMvhsi78og8BmMqa6VQGsu2ojoLwXhH-HyDpQ0TdEtsdWOOipHs7RGu9UpMidQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ویدیو کامل اجرای بین دو نیم فینال جام جهانی با حضور شکیرا و بیژن مرتضوی؛ عالی بود ببینید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26098" target="_blank">📅 00:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26097">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🏆
لحظاتی کوتاه و جذاب از اجرای امشب شکیرا خواننده کلمبیایی درمراسم بین‌دونیمه بازی فینال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26097" target="_blank">📅 23:53 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
