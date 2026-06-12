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
<img src="https://cdn4.telesco.pe/file/QtJj4gA4RFpnucMxrw2sYGix7DgdUfZPkgyatjoxIMexLBCafxxHFCP6ewiYKyLIjbf0iEbJR-4lU6WmBWP9iM1ZgShfMdc0sT6coH_zZfcQt20ASAKdppOyCzLlO1gxzSn5dnzitNBIHim7BakKHEDX-m3XmrITCLNR9keYAfyIzB6SuQuTGXu924sOgf4YBjXQXMGu9FFmdlPE_8q78x8EBeAHP7LaWxAtrepZ4UZ_byy197x_gZi4tNtPo4q9PQti-0y5RFoozpOfEfluA3-ame-6FPO0CtlbnFV14edw4Kolbt1LNpRvx5ugI_mbiH-ZbwmkJsPWkcUcq87PNw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 982K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 20:15:04</div>
<hr>

<div class="tg-post" id="msg-127450">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
عزیمت پاپ لئوی چهاردهم، رهبر کاتولیک‌های جهان ازاسپانیا در پایان سفر یک‌هفته‌ای، به دلیل نقص فنی در هواپیما به تأخیر افتاد
🔴
پاپ به سلامت از هواپیما خارج شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/alonews/127450" target="_blank">📅 20:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127449">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OR0Gz1PraFTs1YN8TYq8fCReRMvUEdah4BORoEdvMvWSgtvy0RerrZf-LuK9ZZRtVPp6rdOCiw7xO86HnuYLZ5N_nZO48NQ9xu2meuoApLP3MOp5Rc5TBYBygfrDMu_ajb9u_CSEx3z0JX5EbvZNSSzVRgIlW7b0sTYtOnL9F4wJmd5e5WujpPCIr2xJQnSkUvJuwD8yftkJsaHryrlIxBLoeb3RapPQO2lrPy3X226EElT4jBrjOiR7C-Lo3wlVkFxCr-TFxbsvkSQfdsp9hIqL4M2h3MkTsvFc14Fv5IRJDP7F1vTmr4PKw1pWoXxvbvZEWJhp2CXpTS_2QkoLXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی اسرائیل به شهر النبطیه در جنوب لبنان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/alonews/127449" target="_blank">📅 20:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127448">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4978ed4fb.mp4?token=H2xB---aiygTLelr7ek6AiPXssYiUcUHLLY5No4_dNnbpJ1oAGE-q6myM5ZuluO7ArAlQMBFPovbDGqkjvL-k9tsMcnQFEDgIfZipzYNAZgfFawHnBsNvZ5gUs9KK85JNIvAqsgnuoGVpn2IMmNYHyxncWwKRcLGEooXCJX7MQvRHJG12gEjdLJBgaRQnfdb6fXCLJSIZ2J5zrn_e_7GyFsaEf3FH74VGteyZ9SjiNlICO5LWujvp-1eyXVClbmHHr5kVQL-B3F1aAMvXBQByW7tJP8VY3stGi5e95Vf3rtTYovaUhaPngFlGEwj7mveJ0iSU80nMT4EPafNRgyZAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4978ed4fb.mp4?token=H2xB---aiygTLelr7ek6AiPXssYiUcUHLLY5No4_dNnbpJ1oAGE-q6myM5ZuluO7ArAlQMBFPovbDGqkjvL-k9tsMcnQFEDgIfZipzYNAZgfFawHnBsNvZ5gUs9KK85JNIvAqsgnuoGVpn2IMmNYHyxncWwKRcLGEooXCJX7MQvRHJG12gEjdLJBgaRQnfdb6fXCLJSIZ2J5zrn_e_7GyFsaEf3FH74VGteyZ9SjiNlICO5LWujvp-1eyXVClbmHHr5kVQL-B3F1aAMvXBQByW7tJP8VY3stGi5e95Vf3rtTYovaUhaPngFlGEwj7mveJ0iSU80nMT4EPafNRgyZAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توافق کنید جواب اینو کی میخواد بده؟
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/alonews/127448" target="_blank">📅 20:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127447">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
یک مقام اسرائیلی به روزنامه یدیعوت آحارونوت: ترامپ ما را فریب داد و توافقی که قرار است به‌زودی حاصل شود، بسیار بد به نظر می‌رسد و اصولی را که هنگام آغاز جنگ با ایران درباره آن‌ها صحبت کرده بودیم، برآورده نمی‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/alonews/127447" target="_blank">📅 20:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127446">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c291502e6.mp4?token=GK7TSxBf9WVGRxirxD-mRYbjMBT5OaAV6pnYq5QR9kDWbJUzvPoMfua-r5Cto9NRc4_u8eFxafJiyC1Ldwm2LQNGZoUPBUfAYmW7ul2rk9vpDNwk9X9fZALUEs-NOCBlqqFh45hBwMZCl4QjJ3fq3Ct9rJpe8KvqwowL9pyNdBtrseMj-4stAtrIQDqSsjHGTRBLPScs-rJOLfTT1sx6mXsJeDSQXj987yrz5Sn7K0_rARgmdbjESllpT6wUGcNnkxENd_oJsZT94tISJLVz4xvPxxOwNzRYbNbavkxEqHbUyOgp7umf0jYJ66uxoWviTjj_M2uLZ6sLOTBsnTbo9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c291502e6.mp4?token=GK7TSxBf9WVGRxirxD-mRYbjMBT5OaAV6pnYq5QR9kDWbJUzvPoMfua-r5Cto9NRc4_u8eFxafJiyC1Ldwm2LQNGZoUPBUfAYmW7ul2rk9vpDNwk9X9fZALUEs-NOCBlqqFh45hBwMZCl4QjJ3fq3Ct9rJpe8KvqwowL9pyNdBtrseMj-4stAtrIQDqSsjHGTRBLPScs-rJOLfTT1sx6mXsJeDSQXj987yrz5Sn7K0_rARgmdbjESllpT6wUGcNnkxENd_oJsZT94tISJLVz4xvPxxOwNzRYbNbavkxEqHbUyOgp7umf0jYJ66uxoWviTjj_M2uLZ6sLOTBsnTbo9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حادثه تیراندازی در میدلند تگزاس
🔴
برابر گزارش‌ها در این تیراندازی چندین نفر زخمی شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/127446" target="_blank">📅 19:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127445">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: رئیس‌جمهور ترامپ در حال حاضر به سمت توافقی با ایران پیش می‌رود که از دیدگاه منافع آمریکا، از جمله منافع مشترک با اسرائیل—برای جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای—است و ما انتظار داریم او این اصل و اصول اضافی در حوزه موشک‌ها و نمایندگان نیابتی را حفظ کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/127445" target="_blank">📅 19:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127444">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1ujqLdm0o3rRawp-4e0kxFwO4EhbViR837PPbbB6Gm_YVifbSWxIeqhPpfSbTdzy_CY55TkQQlJqqYiQBArR49jwTriuzhaHEipsHOEPMsrnpoORh_cVE9mX4DK9kfct3cR5tF_ujCM19wccB0jSRA-jYDn-NW78CMaqRkSYXbvmcvGzNppm0RBUk3mi31-IhRoPM_vMnoX4LyGUNkVYEg9_rrbC3dx5xlAJP_I3DuGkNR5GSvu6L9XZjKWxElTBnJ8HEfDdtv-K9uiJQuVtgPLgvHiH2zpXUX3XaQsbZGhlzUEdJ_mfVTKryQdo4PdZWsVWcFxoY_F3b2kcLImEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / نخست‌وزیر پاکستان، شہباز شریف:
در میانه تلاش‌های شدید میانجی‌گری پاکستان، ما کاملاً از کمپین مداوم اطلاعات نادرستی که توسط کسانی که می‌خواهند توافق صلح را خراب کنند، آگاهیم.
🔴
با کنار گذاشتن سر و صدا، می‌توانیم تأیید کنیم که متن نهایی و توافق شده توافق صلح به دست آمده است و پاکستان اکنون به طور نزدیک با هر دو طرف برای نهایی کردن مراحل بعدی همکاری می‌کند.
🔴
صلح هرگز به این نزدیکی نبوده است که اکنون هست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/127444" target="_blank">📅 19:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127443">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
کانال 13 اسرائیل: ایران می‌تواند هفته‌های طولانی به سوی اسرائیل، موشک شلیک کند!
🔴
ایران هنوز هزاران موشک بالستیک و شاید حتی خیلی بیشتر در اختیار دارد که می‌توانند به اسرائیل برسند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/127443" target="_blank">📅 19:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127442">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سنتکام: به گشت‌زنی‌های خود در آب‌های سرزمینی برای اجرای محاصره دریایی علیه ایران ادامه می‌دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/127442" target="_blank">📅 19:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127441">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc5aef8f6.mp4?token=f5aWa1tkiNZxgc1BXNSwwVuZ3zYD156dGnfccloC8aeFlHJAOSLPRmGBe6WQoMYNSghlwLMzdG4lN7ieaofX7XRvRlTnM5ImBmGzgrDGEXlp2xAhVhsJngSmGL4RgoqENVJCMsd4sL6S4lQs3V0-nMGRTGlMsuUH1pPkW0k7Ei_jjKakX7gw9jTgA1a0WVaMuj0aYRTfJ7R3JYG1gJG45sSGZ7FCmQFjE2dxBWm1_m90h5J0c9EdFjacD2vHv9kcGBbdioBZmSQtCRA5T5cX-L951gOuZPcYQaBdzWpdGeUMh7uaWW11tsOBE8HX1dePV1HRLuP9zWs43jKFi3mukYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc5aef8f6.mp4?token=f5aWa1tkiNZxgc1BXNSwwVuZ3zYD156dGnfccloC8aeFlHJAOSLPRmGBe6WQoMYNSghlwLMzdG4lN7ieaofX7XRvRlTnM5ImBmGzgrDGEXlp2xAhVhsJngSmGL4RgoqENVJCMsd4sL6S4lQs3V0-nMGRTGlMsuUH1pPkW0k7Ei_jjKakX7gw9jTgA1a0WVaMuj0aYRTfJ7R3JYG1gJG45sSGZ7FCmQFjE2dxBWm1_m90h5J0c9EdFjacD2vHv9kcGBbdioBZmSQtCRA5T5cX-L951gOuZPcYQaBdzWpdGeUMh7uaWW11tsOBE8HX1dePV1HRLuP9zWs43jKFi3mukYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروی هوایی اسرائیل به منطقه
تفاحتا
تو لُبنان حملهِ کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/127441" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127440">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63455018a4.mp4?token=fb4Z1rq_woW-CJREXhdyji4bvs3-wxGeNTTxthA8lmuD8u6EzODU_fFCYt42ei1HCBDt5l0KONIivuiU4izpmvzJDjliVx48jkdXdTByRY5Ls3v4D2F0qqIr0mBejZa0Oza2SwSGx7NZ9-OLF8YzoDsDGES8Uw8pZ2InmMnEx-0-zj8d_viKTdeJY1Ikt6eljuq8M3SaNO-3yaSnxPN1OvUVkfu4GItB4rFpfyVmspAgZ1cGx8d-PERklZICu05PSXbfwDxfz5vKN4xnLVSJ3R1YVNqa6cNkqI5LDBySJBSxSOwHYLsdntcliDateV3JgQozwg0GmoHhLOiphV6yJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63455018a4.mp4?token=fb4Z1rq_woW-CJREXhdyji4bvs3-wxGeNTTxthA8lmuD8u6EzODU_fFCYt42ei1HCBDt5l0KONIivuiU4izpmvzJDjliVx48jkdXdTByRY5Ls3v4D2F0qqIr0mBejZa0Oza2SwSGx7NZ9-OLF8YzoDsDGES8Uw8pZ2InmMnEx-0-zj8d_viKTdeJY1Ikt6eljuq8M3SaNO-3yaSnxPN1OvUVkfu4GItB4rFpfyVmspAgZ1cGx8d-PERklZICu05PSXbfwDxfz5vKN4xnLVSJ3R1YVNqa6cNkqI5LDBySJBSxSOwHYLsdntcliDateV3JgQozwg0GmoHhLOiphV6yJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپاد FPV اوکراینی باعث ریزش زمین شد و سربازی روسی را زنده دفن کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/127440" target="_blank">📅 19:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127439">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHmi3oFg2z-eS1_dqr12nUXx8bN647snnk9qwXr0a8aa4EqPJeMDZ2ebxVkitEXojKHfDAoYKuCg_rCJQoYYDfylRa9zxJNvtzVxqJOW34d9yt70Fed-4l29ahD2RabtJT41NHRFbgo5QPFDvQZ3vpXbnJYp4E5savtX-7KG-LFk2CbZa0TFvmJUnB5NXvX64f5UJCeZos0UV9VsEi-XBOqGjRQfCligNbm6myVVpR0Koft_N589XdO9NfNwsIuqk-Rh_rZhpzXbkSJEs3ILSpXpeCz8oJDwVR882w-igPQDGZVsB9z1_3_RoOfIUs2q5fUQp5FYkI3IhSS8f_IQTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمود نبویان در واکنش به توافق احتمالی:  وقتی خرش از پل گذشت، برمی‌گردد و به ریش شما می‌خندد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/127439" target="_blank">📅 19:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127438">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jURtBX91-8-BmkQZ3j3L6bBb_T3SX2kj8nGEEOkXI7OJ6XYEYCM8EHx3IK8JeDTiPS9cB08sz12ClwfD8Xq8YdtUiYFgTkaQDaF6sKw5oMvIm7jplCeEAR6DRPsvuYjJ-_nt8hi4InizD0SjSGjS9FiQLGqcdH-IqgtG_yolUC9GHQaub2VuHPjESXBRHgqFkxux0smTOiGaUBdF33CS7iuItD3K_BCvksafMRgb3_m9OWjJoD_lnbCfdJCz5ckByg7aDfoBqsiG9Kc-5v0eG-xTi_VmQ5_G9YHSEMFYyc8n3v1agBlBj-VEkDLxlwdW2e8j_HEKonyz5oEHu1ONvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / ترامپ توئیت عراقچی را بازنشر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/127438" target="_blank">📅 19:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127436">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6036168b0a.mp4?token=NcRVFzlw4VGCPuJm7BLV8wgdqMkXd7RpABHKiIJjRxnIZ_gPf_10oqER9Mnb80USnvDVcxGtFSALytGuetqjoTIiZtNiB9q0_d5yb59oIvdzbwq64gxObr3S1vUd_lyKns50PG5tqp28HiPJdkZ-oKPD9Yq-3g0OaxtaKMhjGD_UMiqFNQTM5jko8s1p9oP8tyBeJIrU5aeG0572nWt-dhF41G2FRMjAiJfQ4SD28tyttpz8zMdXaAGESy4EwmTxHpfyVDf2vpaW4QzgOqX0aZ7Czj2iOnJ5MxyfXxKxIgTd5P62PQh-6jdPM6c0OS4JUI7FdgI466Sq6b-XBLzDuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6036168b0a.mp4?token=NcRVFzlw4VGCPuJm7BLV8wgdqMkXd7RpABHKiIJjRxnIZ_gPf_10oqER9Mnb80USnvDVcxGtFSALytGuetqjoTIiZtNiB9q0_d5yb59oIvdzbwq64gxObr3S1vUd_lyKns50PG5tqp28HiPJdkZ-oKPD9Yq-3g0OaxtaKMhjGD_UMiqFNQTM5jko8s1p9oP8tyBeJIrU5aeG0572nWt-dhF41G2FRMjAiJfQ4SD28tyttpz8zMdXaAGESy4EwmTxHpfyVDf2vpaW4QzgOqX0aZ7Czj2iOnJ5MxyfXxKxIgTd5P62PQh-6jdPM6c0OS4JUI7FdgI466Sq6b-XBLzDuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حملهِ به روستای اَلسَرفَند تو جنوب لُبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/127436" target="_blank">📅 19:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127435">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فوری/العربیه به نقل از یک منبع دیپلماتیک: آمریکا و ایران آمادگی خود را برای امضای توافق به میانجی‌ها اعلام کرده‌اند
🔴
دولت ترامپ در حال برنامه‌ریزی برای برگزاری مراسم امضا در ژنو، احتمالاً در این آخر هفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/127435" target="_blank">📅 19:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127434">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
شبکه ای‌بی‌سی به نقل از یک مقام آمریکایی: پیش‌نویس توافق مورد موافقت سطوح بالای نظام ایران قرار گرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/127434" target="_blank">📅 19:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127433">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سید عباس عراقچی، وزیر خارجه: حفظ یادداشت تفاهم اسلام‌آباد هرگز به این اندازه نزدیک نبوده است. تا زمان نهایی شدن آن، رسانه‌ها باید از ورود به حدس و گمان درباره محتوای آن خودداری کنند.
🔴
در راستای رویکرد مسئولانه و شفاف ما، تمام جزئیات در زمان مناسب با عموم…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/127433" target="_blank">📅 18:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127432">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6UJD7G2tnLL2-v01srTRvVpGW0MWj0Jm9OvtxeR1IAGKfaRlibrBOVAt5sa129TFwpk3AU0lX52znOniydXVAwCPHt33qfbYvmKqjB7msAIVHGWsLEF9AD2aIS10O2Jbzz8SPbaQElz3VzoFCyxxP6DqSgW90WRfk4lP4m2kFNs7XqmWTjhq8N0g-jeJLBtVWSY3jaPBBXW_1_HueqOizoGhNW0Qhj9hA4k8MH1vVspL3CfA5_e1n_TtynFGriqdVILkaHAo0sYdwZSGleYIrUTuBpwT53i9ptP4vZK54RVd2wsP2Auwc4YrKkmKNdtnzpuDocdvaUZGzQRkgZMGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو حمله هوایی اسرائیلی به شهر صرافند در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/127432" target="_blank">📅 18:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127431">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
سناتور لیندزی گراهام: ایدهٔ یک صندوق بازسازی ۳۰۰ میلیارد دلاری، با توجه به اینکه چه کسی در ایران مسئول است، به نظر بی‌توجه می‌آید.
🔴
این مانند طرح مارشال برای آلمان است در حالی که نازی‌ها هنوز در قدرت هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/127431" target="_blank">📅 18:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127430">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0JawyejPMzGhRMPXPs0duK76jJN30HEEBjScJ9vmRirP1zsTz_U58pjP01tl6Vj1f7f_cVs-ES6ln7QlOHSuXF6rgLBSTjA0ZyuO3_p_hSPp59wsG9R1zBDeqES01V52grYnVnlrKFHrQXKsvWeEwlIO0B9hUiOlsKWMcTqvg1cOOSClz5zrwsUfWUkeeOkJEVBzhy3VfjZ1ot24ysHQ5urnK9FR1FFKwSHfaj9HKvwewqK24okD08TBNvAHbJP5-VE5Rnm1mhIQtqAEUORtJONz5i_MQgHF-OC_4Hbbso-4kl7w54LFiZUywN67BkPYFuEm9nUVIXbxP63Ef46hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جی‌دی ونس: اولاً، ایرانیان هیچ وجه نقدی دریافت نمی‌کنند و هیچ وجهی صرفاً برای امضای یک توافق یا حضور در یک جلسه آزاد نمی‌شود. این توافق به گونه‌ای طراحی شده است که نگرانی‌های ایالات متحده و متحدانش اولویت داشته باشد، و اگر جمهوری اسلامی ایران تعهدات خود را انجام دهد، فواید اقتصادی به آن‌ها و کل منطقه سرازیر خواهد شد.
🔴
این توافق پتانسیل بازسازی منطقه و منجر شدن به صلح پایدار را دارد.
🔴
چند مورد عجیب را در گزارش‌های چند ساعت گذشته متوجه شده‌ام. اولاً، افرادی که (به درستی) ماه پیش می‌گفتند دونالد ترامپ یک رئیس‌جمهور تاریخی است، اکنون بر اساس گزارش‌های رسانه‌ای تایید نشده یک توافق را نقد می‌کنند. ثانیاً، افرادی که می‌گویند به کلمه‌ای که توسط سپاه پاسداران انقلاب اسلامی گفته شده اعتماد نکنید، ظاهراً به پست‌های شبکه‌های اجتماعی ناشناس با منبع ناشناس باور دارند.
🔴
رئیس‌جمهور قرار است به هر روشی که باشد، نتیجه خوبی برای ما به دست آورد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/127430" target="_blank">📅 18:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127429">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/738cca7c3a.mp4?token=ZaaijVM34LGHliIIKQaiYlvNu3F8aNV1JmrWZ1DewBD-ryTCoJQZzAWMlyg8Q3ROoXXdnRzl8PsrQsCqF1F8C29_EGqa--9PHyFdUAqXUa3LLlv2TBK4la3PzM9q2irsB7HNDOm-NkO6Pp0t1TY4NaAw4Niwh91cQHgnFplj-vaXVWtsCbXct7WgXzJEOm1Xg81Dpm6xK_RjY4ceoF7cTiN6N6ZWw87s6P27_bGXGTdT7L8KDJswZiAnYURDV8G2ZoY-NEs-1DdyC0HMz6GEd4wLb7t3u1dbKf1Nrdn1PInaVnWWCIFpBOeviU_vIsuiVvmaejBJjtGuQxJS0gwk1oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/738cca7c3a.mp4?token=ZaaijVM34LGHliIIKQaiYlvNu3F8aNV1JmrWZ1DewBD-ryTCoJQZzAWMlyg8Q3ROoXXdnRzl8PsrQsCqF1F8C29_EGqa--9PHyFdUAqXUa3LLlv2TBK4la3PzM9q2irsB7HNDOm-NkO6Pp0t1TY4NaAw4Niwh91cQHgnFplj-vaXVWtsCbXct7WgXzJEOm1Xg81Dpm6xK_RjY4ceoF7cTiN6N6ZWw87s6P27_bGXGTdT7L8KDJswZiAnYURDV8G2ZoY-NEs-1DdyC0HMz6GEd4wLb7t3u1dbKf1Nrdn1PInaVnWWCIFpBOeviU_vIsuiVvmaejBJjtGuQxJS0gwk1oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
الشهبیه، جنوب لبنان، پس از حمله اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/127429" target="_blank">📅 18:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127428">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
یسرائیل کاتس، وزیر دفاع اسرائیل:
«اسرائیل باید توانایی اقدام مستقل برای جلوگیری از دستیابی ایران به سلاح هسته‌ای را حفظ کند و به همین منظور به ارتش دستور آماده‌سازی داده شده است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/127428" target="_blank">📅 18:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127427">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9qe0WSDXPnC3Rtzst18nEPL_vza7ATWZexL9DogjJQuZLuOW-LA-CUB1jUyKWCUxwKQWdkuxRnAbvnJ_JI9xnNeiaRMAfZJBNXsCSR25N8apO4rCbIUUvTOQewZ8eDO7IfOcjSQqMmkvJtYH2HhTdFDyc5KK2-d7ljo5EAsN_16I_O18L29xZvRUG362W5zuU68tqKCu6enZ6os98ZM0Wg_UD4XnW5QGgwLWdaH7Ru69-fdCl1pgNXkE5L44HJ5XW4mg_D_fNxPrIroHqoMQq5U5RTBqr5-zkztcBOtcQpjub9KSzBEeuDJgSGt3RgDV32tz2iqB3mbYcG6X4_b1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سید عباس عراقچی، وزیر خارجه: حفظ یادداشت تفاهم اسلام‌آباد هرگز به این اندازه نزدیک نبوده است. تا زمان نهایی شدن آن، رسانه‌ها باید از ورود به حدس و گمان درباره محتوای آن خودداری کنند.
🔴
در راستای رویکرد مسئولانه و شفاف ما، تمام جزئیات در زمان مناسب با عموم مردم به اشتراک گذاشته خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/127427" target="_blank">📅 18:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127426">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
پزشکیان : باید فرهنگ مصرف بهینه را به یک گفتمان ملی تبدیل کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/127426" target="_blank">📅 18:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127425">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
کاربران در سراسر جهان از اختلال در اینستاگرام و فیسبوک گزارش می‌دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/127425" target="_blank">📅 18:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127424">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
جزئیات توافق ایران و آمریکا به ادعای رویترز
🔴
رویترز به نقل از یک مقام ارشد در دولت آمریکا: برنامه هسته‌ای ایران برچیده شده و مواد هسته‌ای تخریب و خارج خواهند شد.
🔴
توافق با ایران مقرر می‌دارد که این کشور از گروه‌های نیابتی حمایت مالی نکند.
🔴
توافق با ایران…</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/127424" target="_blank">📅 18:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127423">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
جزئیات توافق ایران و آمریکا به ادعای رویترز
🔴
رویترز به نقل از یک مقام ارشد در دولت آمریکا: برنامه هسته‌ای ایران برچیده شده و مواد هسته‌ای تخریب و خارج خواهند شد.
🔴
توافق با ایران مقرر می‌دارد که این کشور از گروه‌های نیابتی حمایت مالی نکند.
🔴
توافق با ایران بر پایه اقدام و دستاورد است
🔴
توافق با ایران شامل بازگشایی تنگه هرمز است
🔴
تا پیش از اجرای مفاد توافق، هیچ وجهی به تهران پرداخت نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/127423" target="_blank">📅 18:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127422">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
امیر دریادار سیاری : ما تو منطقه خودمون قدرت داریم، اگِه مرد هستید جلو بیایید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/127422" target="_blank">📅 18:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127421">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
پوتین: روسیه به آن سرعتی که ما مایل بودیم در حال پیشروی نیست، اما هر روز به‌تدریج در میدان نبرد اوکراین پیشرفت می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/127421" target="_blank">📅 18:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127420">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
شبکه خبری ای‌بی‌سی به نقل از یک مقام آمریکایی: تردد در تنگه هرمز ادامه دارد.
🔴
شبکه خبری ای‌بی‌سی به نقل از یک مقام آمریکایی: تردد در تنگه هرمز ادامه دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/127420" target="_blank">📅 18:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127419">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: اسرائیل از مناطق امنیتی در لبنان، سوریه و غزه عقب‌نشینی نخواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/127419" target="_blank">📅 18:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127418">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
رئیس ستاد کل نیروهای مسلح : هرگز به‌ دنبال دستیابی به سلاح هسته‌ ای نخواهیم رفت و توانمندی‌ های نظامی ما ماهیتی دفاعی دارد و در چارچوب ایجاد بازدارندگی تعریف میشود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/127418" target="_blank">📅 18:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127417">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
اعتراف به همسرکشی پس از یک ساعت گریه کنار جسد
🔴
مرد جوانی پس از قتل همسر ۳۸ ساله‌اش با چکش و چاقو، حدود یک ساعت بالای سر جسد او نشست و گریه کرد و سپس خود به پلیس اطلاع داد.
🔴
بر اساس اعتراف متهم، اختلافات مالی و مشکلات معیشتی عامل اصلی این جنایت خانوادگی بوده است. تحقیقات درباره پرونده ادامه دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/127417" target="_blank">📅 17:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127415">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ترامپ:
آنها افراد بسیار بی شرفی برای توافق هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127415" target="_blank">📅 17:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127414">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSIl2sledBDOCeDTLVxcis9AuDebW09fQLQ4g_ZPzE1GmMshCD6DwroSkwrEcpmrCuEEbLb8nNPaH1fbXzZL14I_ttG8vMVoEogRR55WFnrLZWJetaxteGnLvbx1ZbAdYDX574QQugyHb8lFBg-WLZlKzi5zWS7YP3Iefv3xj1GTbfcxWBDVzTFZl3ATd_ZEogKVwZRYA_TJmw23nfCP-7qIwieb_kxYS5mTxnFon2UurgnNE-MgFfFBhdVYUPsnskTijvSv0NPS78FEsbqrRbJg7WuswZb2gjyFBckiT2l-SYSy_7Uasj0fWYkHW3vTaXCvsbppgHPF0NziBMMk9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
شرایطی که ایران به اخبار جعلی داده است، هیچ ارتباطی با شرایطی که به صورت کتبی توافق شده ندارد. آنچه آنها گفتند، از جمله بیانیه ضعیف و ناامیدکننده‌شان درباره انجام معامله، هیچ ربطی به حقیقت ندارد.
🔴
افراد بسیار بی‌انصاف برای انجام معاملات. با آنها مفهومی به نام مذاکره منصفانه وجود ندارد. شگفت‌انگیز! علاوه بر این، حمله پهپادی کاملاً منعکس‌شده آنها دیشب به کشتی‌های هندی که از تنگه هرمز خارج می‌شدند، کاملاً غیرقابل قبول است.
🔴
بهتر است سریعاً به خودشان بیایند! رئیس‌جمهور دونالد ج. ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/127414" target="_blank">📅 17:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127413">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
یک مقام کاخ سفید به فاکس نیوز گفت: مواد هسته‌ای ایران نابود و منتقل خواهد شد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/127413" target="_blank">📅 17:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127412">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
یک مقام کاخ سفید به فاکس نیوز گفت: مواد هسته‌ای ایران نابود و منتقل خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127412" target="_blank">📅 17:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127411">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
امیرحسین ثابتی: کسی حق ندارد تنگه هرمز را به امید رفع تحریم یا محاصره باز کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127411" target="_blank">📅 17:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127410">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMsW1bUje5Y9w8s1IJffGlE41LiwM_soytyEMQmyxqwOfraLeUQ2SwD8OFz7ud0ubjOoJ2bJmRigZQxBmVXcgdh1TvAE56xdKGepIguG5Em61ROIo76uatPNGRbpQPl0BzsFCYGvyS1P6NC6i04jVVpGz7CsYCehs1OFKCSuApCUHBAgC5UWuA6B984awN5n79qh5gSU3BHMdfJukobKCzdDN3NUmDX_1-y_kIanltaV_bRkF-Ae331TX14zD08Gc3dS3gloZTjyQgMuUWkjWv51IsTBO1jsc2_RLM4VqFlvdPIbyOmYx58pYYdbaKHlmWfRjzS30bc8ilLbFgebTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مرندی:
روز یکشنبه هیچ اتفاقی در ژنو نمی‌افتد. هنوز کارهایی برای انجام دادن وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127410" target="_blank">📅 16:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127409">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
وزیر قطع ارتباطات:
از سرعت اینترنت راضی نیستم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127409" target="_blank">📅 16:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127408">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnxu_1LxPOtV6sfVDowZvT7M4wjDiNEmiWg9wZJi1b8X2fSXd-td3iDXRuTZWH68oSS4Q1Q3ZpVtN6c_pERpoE3yRxNt0PTuqAJza2dW3s5iOCsOmayMqSCsbluwmItemIXDEhWNwYkc2ftSng_4r_-Gu3L7OqwJw1OSWDxVokopm-46V8WFNiUEMGOXBtahZLLZsKl8djUuKNFT0BGTh9o_CohjEXAN7XzdGjvVgbBwoq7WfywBkVU4aLrZQD9RtsAocr8VDUmk8Q9DHTNCOJGnHsaQdQcCKHM4Uc88DrZGv4I_mesYJRr5XL1wifOW0oARBDlLKbghIX0W2p73rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژست‌ گروهبان در مراسم‌ فتوشات جام‌جهانی
😎
ساعتشو دیدید یا نه کرد تو چشممون
@AloSport</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127408" target="_blank">📅 16:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127407">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCfXtIsKfJeKIFhUpx93BDS05Fp28K7kC-hqhPpoImBV1-L7pyVFS7seO9jm6M4HZlYNVv9o5URS-dlDape6JA7YssYPYqjKeUQGpwFO5eOcpz2PvooQ7jxk_jszKlwF42be9a4lL1zPe9KQXbIezokr-ui_sw4M95JQ2foLTMGunujOJ9q4eEibzYTB6QG3v7zP_NNIDNIR565RztB8SOgQXOzj8Ha7HlHjNRy_Q1dR5VHP4BjsktK4llJf5-3omanu9Hl0O0AT8g6_-GmbZE3BiE2kxnYBv3UkWW63U1Wi6kJeabCLMsaTQGnWFOxloVGQYAOERw9mBHa6H8E0IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: هیچ تفاهمی تا به امضای رهبری نرسد، کوچک‌ترین فرد از امت ما ولو کودک ما قبول نخواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127407" target="_blank">📅 16:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127406">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فوری / فارس: ادعای امضای توافق در روز یکشنبه در ژنو کذب محض است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127406" target="_blank">📅 16:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127405">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
فوری / فارس
:
ادعای امضای توافق در روز یکشنبه در ژنو کذب محض است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127405" target="_blank">📅 16:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127404">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKsdfpd9XrWVT_vRYGgJWi54iE2OfbcvJxOPp0o_XFyg17EPWaHy3rz2u4nRf14eMpysYioAH22PYS-YoRgR71xyn4UNZapyjTHPnYkwXxbEZ3R_qUaekAv7gD_lZN17qpoGMyM8FnUXpCbChLSag4bK0yVcDqDFiVxWV2JnhIeQ2qCE2jDiQFNR3RGQVBWZ4aaLJLD7G9gn5F36dgMQZk8JlMKCMvqapX_GV6CCiGjDZTPULoxc8J3SyGDPDgD7HHJcsGeuK-GA517sFaZxM2j7hwNXUd7JEiNunAg0IrFswm_WR1f8Pba0_WjUTd4YaYbPHZlFqQX5m03MuCfssw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل، یونان، قبرس و ایالات متحده روز جمعه مرکز انرژی شرق مدیترانه را راه‌اندازی کردند که سکویی جدید برای همکاری در زمینه انرژی، فناوری، نوآوری و پژوهش ایجاد می‌کند.
🔴
اسرائیل می‌گوید این ابتکار با هدف تقویت همکاری‌ها در امنیت انرژی، امنیت سایبری، زیرساخت‌های حیاتی و توسعه فناوری از طریق اتصال دولت‌ها، مؤسسات دانشگاهی، پژوهشگران و رهبران بخش خصوصی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127404" target="_blank">📅 16:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127403">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
اداره ملی اقیانوسی و جوی آمریکا (NOAA): شرایط ال نینو اکنون در بخش گرمسیری اقیانوس آرام شکل گرفته و دمای سطح آب دریا در ماه‌های اخیر به طور قابل توجهی افزایش یافته است.
🔴
بسیاری از پیش‌بینی‌ها نشان می‌دهند که این دوره ممکن است به یک «ابر ال نینو» تبدیل شود و حتی در میان قوی‌ترین نمونه‌های ثبت شده قرار گیرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/127403" target="_blank">📅 16:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127402">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqvoziIZ4YdyrcZwvSQhvFTdvjwCVnb7p0ZUPq2nzbJsQ0T3KbtzZV7muH7YliUoQXk88rI1u9kMpBmqiZy5uQcFP02cwbIpEZ2LgR-YUMIGXLT1B25rTeznEGM4m4SZP8SMDnK4wlHPoQ-nNPH8aKxyThnvFXy1n_5jci74wWbfvTWRJLPyDKoByvt-xrZVpNfth_XTNCAbou1EtXKNGLc-LIwS8uUfMAXd4Agw6cLeCmjURLypNYu99n8dQYFs6GyW3taU9fvFY7jPIVBTNy_a1GkHIVMT2H7ReLtoF-fgGb03K8DmEIDF6pMoH2XCRarWHRObkI750kk63plD5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری یونهاپ کره‌جنوبی: سامانه پیشرفته پدافند موشکی KM-SAM (Cheongung-II) که هم‌اکنون در امارات متحده عربی مستقر است، در جریان حملات ایران بیش از ۶۰ موشک رهگیر شلیک کرده است.
🔴
بر اساس این گزارش، این سامانه موفق شده حدود ۹۶ درصد از اهداف مهاجم را رهگیری و منهدم کند که نشان‌دهنده عملکرد بسیار بالای آن در مقابله با حملات موشکی و پهپادی بوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127402" target="_blank">📅 16:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127401">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
خبر فوری رویترز:
توافق توسط جی‌دی ونس و قالیباف امضا می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/127401" target="_blank">📅 16:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127398">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VJFbfVePlGZcqsn-6MK_iDY3R8j8tUqnBQMs_-6zt5rlb2hxf06b-OpGT9UhrPOaEylKERAJ90pF6jT2eShndnwCxXpz7OIUmbN-5RxPGzZXjtUuQPNevp-YzhuKMAPlo5qS7oDGZOVUiH8k1L0kcsfj2Y-OXc5Zc9PTxycHo3BK8DfAwogafUQT_IPmnhJAaGcMxgrj6D1zf5mXK2W-Vr-AdOpAaIzU0PCWiIAhAkjXnlTOcKAG3cyll0b-cjpoPE6xxkAYwxXHhKIeML1MHqmw4ZAVPTSHeXhgVENc6X6PQldYkpRxQl6j3b7DzF5-yHKzlmwor8grsb6J9cn4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j-kUVyfrNbTb359Fj3zvItRvzrIR0Ttv0Yjjng23jgZaMBt_0h6TTdtRDJFi0ULUBgtQJPWKHVrgGXCVdnAp5-Cm98OFKJ6nk65h6z37xQSr34J7Ng6khjsEiwlmG9EhYKzLJ1jEzWQwVKUMOnosnup2lrIJBHonxrvgSrupPDk6Y1ak22Q6nTfMNYfzSkQSMvHSc-iIhOPVDGj9EwPqaCH1ILjDuQx0PVzKH9afI-gOGPHaCXHbD3znSJmhsrRMV4T5qrMjRkjYhhCu8BBggAafmcAojc9CVGDlHL5IShSAGRXv9L0I6FUtFxWXwRDu_xyZIih310pLVPpS8akXtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OqqSnQQ-0AclDjGqtgaySFJYXSinU4y-6WcoZR_KHz4HmY8uyF8TLuTQjTSGeSkT26viIJN2WZUaVslsd_wpV4BMdE4VYMv89K4Ja4gHqqQkNLbCVBj4j7CTZ9aiIpAqNQGyvHOww9MEOaGBDzUQgBiUw0D6qbRpa1iZpAeQZ5p9bRFeCSfzCWMfIZ3BeCW_BX0xNF1sNK084HhypUYzeN9KgE0s6Pv9MlJHOyq6Pd1tdIqZ0QXPf3w8L8D75JjmoPou8o9IqFUmA73v3bkAWebXQZMWU3lawvC-QhZU3U6QuM7N9uTIopFe-_LG9xWVhneijUaafP9uPRQTOnNJ_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیروز دونالد ترامپ جونیور در هتل لوکس د آنگلتِر در کپنهاگ، دانمارک، همراه با گروهی از مأموران سرویس مخفی دیده شد.
🔴
دلیل حضور او در دانمارک مشخص نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127398" target="_blank">📅 16:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127397">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
سی‌ان‌ان با نقل از منبع آگاه : اسرائیل به آمریکا فشار آورده تا تو تفاهم‌نامه، دارایی‌های بلوکه‌شده ایران آزاد نشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127397" target="_blank">📅 15:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127396">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
رویترز: دولت ترامپ بنا دارد برخی مهاجران ایرانی را به آفریقای مرکزی بفرستد!
🔴
دو وکیل و یک مقام آگاه به خبرگزاری رویترز گفته‌اند دولت دونالد ترامپ قصد دارد شماری از شهروندان ایرانی و دیگر مهاجران را به جمهوری آفریقای مرکزی اخراج کند؛ کشوری که سال‌هاست با بی‌ثباتی، خشونت و فقر گسترده دست و پنجه نرم می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127396" target="_blank">📅 15:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127395">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سنتکام : ۱۳۶ کشتی رو منحرف کردیم و ۹ تا رو از کار انداختیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127395" target="_blank">📅 15:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127394">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTvEx6qll4KAJ28kmh9SHfqCjZJKGJlTR0AzwbWdSv8E2lrtk4Or-OeeDJEbStZ5dZrCzjUUuT39Q9_ncmYCXMf9xzooLdH-uK0eN7X6eDCDOMSkn-pFBQKIBYWETUSwwwKE47-nDXGw1M2AM91oq4WNB5WAFSCAYs0l46b1Cf321hAhNkkeX-8w96hEeo_71Nx0k6cXmz33CpymuzHxbSpmQWEk3sAozybz0EUJkNi8N4vX2zPZzwAty9xWqOgqLZoJJOo9P1AnANhV4nq3RNcPI4473bfwHr2oV5r1WlqmR-wvk-xLR8ouAF0pHdTPHa2FN3i5qFvC7ijXZNNceA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره: در مذاکرات اولیه، ممکن است به همه چیزهایی که می‌خواهید دست پیدا نکنید، اما به تفاهمات مورد توافق خواهید رسید.
🔴
برخی از این تفاهمات ممکن است سپس به مذاکرات اصلی و جامع برای حل و فصل بر اساس برد-برد منتقل شوند - منظورم مذاکرات آمریکا و ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127394" target="_blank">📅 15:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127393">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
وزارت امور خارجه روسیه به شهروندان روس هشدار داده است که هنگام سفر به تایلند احتیاط کنند و ادعا کرده است که آنها در معرض خطر بازداشت یا دستگیری به درخواست آمریکا قرار دارند.
🔴
مسکو ادعا می‌کند که سازمان‌های آمریکایی در تایلند عملیات‌هایی برای دستگیری روس‌هایی که مورد توجه هستند انجام می‌دهند، گاهی بدون اطلاع دادن به مقامات تایلندی، و ادعا می‌کند که بازداشت‌شدگان تحت تهدید، ارعاب و فشار روانی برای گرفتن اعتراف یا پذیرش گناه قرار می‌گیرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/127393" target="_blank">📅 15:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127392">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3fa4b0e2c.mp4?token=U2e8UTIolqV6TPqMqjP1qHu8PWrfrf8zXjI2Q4GnYKa1grncapG1o0iCZ2NYDEwjqgGcDyp-ZBw__2_EyK4e1br9M0Tp0Lc7LpWhzfbgw_K6nvcKVzyKv0tBKXx-wACUzZUohmnaJsVqQww3XiypEPKDOwwUOirvY79YPnc1aqTTjh_TkPuNvUiK3XIIjhGoWqw3pqxrP8qQ9H-7qxhec2YSrXSbHRrZDKgJuERHDwMEvgN-jniHP-gReIVFGc3gOwQbLOwqZgtEWgCb85J2bAGgOuDbMOcugO0fAW7NWPgeN4kiDK03NB_lbEI8f1rGSY2ZEObwOoYVCMPrk5ZxUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3fa4b0e2c.mp4?token=U2e8UTIolqV6TPqMqjP1qHu8PWrfrf8zXjI2Q4GnYKa1grncapG1o0iCZ2NYDEwjqgGcDyp-ZBw__2_EyK4e1br9M0Tp0Lc7LpWhzfbgw_K6nvcKVzyKv0tBKXx-wACUzZUohmnaJsVqQww3XiypEPKDOwwUOirvY79YPnc1aqTTjh_TkPuNvUiK3XIIjhGoWqw3pqxrP8qQ9H-7qxhec2YSrXSbHRrZDKgJuERHDwMEvgN-jniHP-gReIVFGc3gOwQbLOwqZgtEWgCb85J2bAGgOuDbMOcugO0fAW7NWPgeN4kiDK03NB_lbEI8f1rGSY2ZEObwOoYVCMPrk5ZxUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
‏سی ان ان تمام ۳۹ باری که ترامپ در این ۹۰ روز به رسانه ها گفته «توافق با ایران نزدیکه» رو کنار هم چیده که بسیار چیز هم عجیبی شده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/127392" target="_blank">📅 15:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127391">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
قیمت نفت در معامله‌های روز جمعه (۲۲ خرداد) پس از ادعای ترامپ مبنی بر پیشرفت مذاکرات پایان جنگ بین تهران و واشینگتن، بیش از ۴ درصد کاهش یافت و به پایین‌ترین حد خود در حدود ۲ ماه گذشته رسید. این اقدام، نگرانی‌ها از تشدید تنش‌ها پس از حمله‌های تلافی‌جویانه اوایل هفته را کاهش داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/127391" target="_blank">📅 15:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127390">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2c410ab66.mp4?token=T-knushMztkc9UM9FFJUiiUAJ8hK3mdr24FzkXCFgChfP0HpZEGGFzIvoC098iyXR7hLviSdU9iQ_XN-mpltKVF7eBSISgKKVye74JDJpvDDZ42BUlUfO5e3pQbLZXMvN2zRJASuPkB2m6Um9da2Yo-Xv4BmydCTZewr4-Ebyv5722tw2yDqxMyF5wNGwSW0a_LYOqzMJpwFY93xS4Mgn67VXbtNloIQLENOXBJXqIpJOu3X-QRz8RARSgKPL6yGuZc34euR3XqzhKnrOoOmu1IjpMQch0EoZCUfmp0bMG1jzPWlweYMslrEIfcLd7p3NFBOSjZ6yIy1FCwVStIjug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2c410ab66.mp4?token=T-knushMztkc9UM9FFJUiiUAJ8hK3mdr24FzkXCFgChfP0HpZEGGFzIvoC098iyXR7hLviSdU9iQ_XN-mpltKVF7eBSISgKKVye74JDJpvDDZ42BUlUfO5e3pQbLZXMvN2zRJASuPkB2m6Um9da2Yo-Xv4BmydCTZewr4-Ebyv5722tw2yDqxMyF5wNGwSW0a_LYOqzMJpwFY93xS4Mgn67VXbtNloIQLENOXBJXqIpJOu3X-QRz8RARSgKPL6yGuZc34euR3XqzhKnrOoOmu1IjpMQch0EoZCUfmp0bMG1jzPWlweYMslrEIfcLd7p3NFBOSjZ6yIy1FCwVStIjug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روسیه به تقویت شبکه دفاع هوایی خود در مسکو ادامه می‌دهد و سیستم‌ها را بر فراز ساختمان‌های بلند مستقر می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/127390" target="_blank">📅 15:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127389">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
رویترز: ایران برای حفظ لبنان به عنوان اهرم فشار در توافق پرمخاطره آمریکا می‌جنگد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/127389" target="_blank">📅 15:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127388">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">📱
لطفا توییتر الونیوز رو دنبال کنین
🔴
پست های انگلیسی در رابطه با جنایت های حکومت به انگلیسی نوشته شده و افراد مهم منشن و هشتگ های مهم قرار داده شده.
🔴
ریپست کنین. مهمترین کمک این روزها جلوگیری از پروپاگاندا حکومت علیه این قتل عام مردم هستش. خونشون نباید پایمال…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/127388" target="_blank">📅 15:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127387">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
نتانیاهو: تا زمانی که من نخست وزیر اسرائیل هستم، ایران سلاح هسته ای نخواهد داشت.
🔴
ما و ترامپ در مورد عدم دستیابی ایران به سلاح هسته‌ای اتفاق نظر داریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/127387" target="_blank">📅 15:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127386">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
بر اساس محاسبات ریانووستی با استناد به داده‌های گمرک آمریکا، ایالات متحده در طول دو ماه درگیری در خاورمیانه، 8.28 میلیارد دلار از صادرات نفت و 6.84 میلیارد دلار از صادرات فرآورده‌های نفتی درآمد کسب کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127386" target="_blank">📅 15:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127385">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idj377ZyOtsMR4kpNMJNlywH89ey3fI9o96x6z9ZZp0AzJdbiT6Ov7XtHpUKVg36nCpT7lQEdRnKMweiUy4VjfylL__18Phzl-PnVHAit1Uh9VgtpSVpkpi4EoJPBc5znC2T9g3lSCuQBz_0j_cjWzFjLqwNX6gJfxMfRvIk_42uyHDnRswuCcqJxVtEhB3M_u9DU8bPScx1v0rn7JoMuoEIv4z26aH1pMUMAs4Oe6tKnlhEobquMJdCBi9CAP9k6Qhz4Cwcdamat5ckl5Pr65JmSFMty9ti-bK122AWGfF56gMYji0ZJfH4aEzV3gansHc_hBBkxUi09FfpE4dwKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل دستور تخلیه فوری سرافند، توفاهتا و مزرعه سینا تو لُبنان رو داده
🔴
دلیلش هم نقض آتش‌بس از سوی حزب‌الله اعلام شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/127385" target="_blank">📅 15:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127384">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hT4WZlz9ymGUccOGyQvWxQtr4p9PPznoFh_CuEVK-ofQ3L1O_ZxdTdKuKs2ZKCLLMPj3vWlyiHoflquTeILx2qz5n6fy6r3zSWx8ivB5rnb4s_PoFSuzNHtrE8uT5VbrWmdHgpSNZUYc0TA1Zb7HBmzp3hqOso__mS-Dh61A3kDZ7ornIHRv91MoBg7NozbVUcUFf5ec2WWwT9L654vKorg65ZI_2QQ42rOnbD2lDnGu0rA_cJ9TqGMpB8JUsfQR82vXvEzlqeaPnIgWdpaMJ9_Zbq-U0YS1XTz3ZrvyHDDlXd_u3QK4aRvkJzpBdga6f9A_eEukiJsI0iuX_rcT8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رائفی پور: خون آقا رو پایمال نکنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/127384" target="_blank">📅 14:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127383">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UerQNrslxkbekq0BaFqXYoIiqiFy9LkJgI2IlYIGZ--p6pwnP7Ff6v5bz-366B6P4X8Dt6tiCJnfs1sz4QXBSic2BoM8Hj4sPqxzpxcFu0Qs9aOj376ZGbAi8kvkUm-pYuMx9o-A3ZP3ZmpDgDZ9rvvJX7TQp7367yHeFFHl8eO2csfESkxtsMS0u0ZbFcI8QbpoB15-tzEjJZcem6c97LAF2-TfigPNi6PdZSAvGMTmtbqQg3M5-PWeTJBMHOsgHEwmlapdrkQIxcSi_m9H13iWilUa_ISmOdhNmX2-8m-KvV0N3fo1KZtue0VV0eQDWYsQDaIp65K-8ji8_4CTRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امام جمعه اهواز: سازش با دشمن در هیچ سطحی جایز نیست
🔴
عقب‌نشینی در مقابل امریکا و اسرائیل ممنوع است، باید انتقام بگیریم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/127383" target="_blank">📅 14:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127382">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbcWV0seMIfKo8vZgc5MbFTcW2aKvkXGsl5vAyrExGpeXOirdURsynC05Vh6OYtgzKTwhd4adEDE1spSE6ooQEgE4kzLcxVYVROK4PDkKxK9jussnJ2_jAjMz7PorhKlbmNIvPMsR8z4L2CnLVwsYcMZiYoYfIqPYQutNqmsE8e00J69s1ViljVJ8yiuc_-ehFbxZN-UyT3bu0lCvxA63wUzhqcSATiUo3B5VIdWOEqD5p35p7k2c6FZmbh5qqQnIfZDX7Q81n_AyMjIUCsectLHN52PvPkqc0dJphpwonC6WmgcTr0aDbEKRwQB-pH9AMdVDzLHFfkHkvi_zaf8OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش تند نبویان به خبر توافق: می‌خواهند متنی خسارت بار را به عنوان پیروزی جا بزنند/ مدیریت تنگه هرمز از دست خواهد رفت و تحریم ها هم لغو نمی‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/127382" target="_blank">📅 14:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127381">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
تیراندازی در نزدیکی کمپ تیم ملی آرژانتین در کانزاس سیتی آمریکا
🔴
حادثه تیراندازی در یک ساختمان مسکونی رخ داده است که منجر به مرگ یک نوجوان و زخمی شدن دو نفر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/127381" target="_blank">📅 14:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127380">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/390974dead.mp4?token=cwrtGR1viE9zSBN9o0aop1MTFtJZjbZ40yP-h4X-dfeDsLJiun-85i9SdR0CC64X7i7nlMUI2ljUgb7IuQrhKwlc3IfHMm2qB-wVfzzW5K1XTZkwskUxWxnsHimNIUtUXEcSTlICejg2RuGKfJ3zLL5UIyUOxoPk0zMdpl_nXWVb4XSNPWUMD1wgOgxKOgoFHXVhiazog9Hd3iXvENSs9KiAqEi78GrIswnHPI0cv1wFNIAGkLOxSTKfdN09yWxGizO9wlq-TsSzHygoTlN-WeD5QSyAk7z9aQD4nDvXdiBaWPStnr27JsyLoUiI6r3Ru6bNFuOnhanrY5-TuAVQU5yEoHsL9-Grd7vopw4PllUhxU8S8Jn_N3wOyGLSIYQXwqGcp3RBhgkC1S7seZVj62s-h5-2zvfx-msxkBE0znc9lobENYV4tDw4Imv5QhyVhExXxZ0VJRYGP0YuWuzd2NM56XiA5wOXIEwxCicWPHC3PBIUs4pCiKfMJABYZJg2i1dTM_yp1IGeEWGuIRtfIIb4xXYGmKPP9MUbkKER4_kX_bShcFBVwnUmF3Dv5DisZWR5O1VOxJFXG3ITqig4LD6hbGS6b6NtFC5s2WR4TBsCKJ5jfLAK1jYzDCysGSd2kcdy5fmck1QshPCFpCaTBxRCwrV3dQhguUs1Wzpr2Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/390974dead.mp4?token=cwrtGR1viE9zSBN9o0aop1MTFtJZjbZ40yP-h4X-dfeDsLJiun-85i9SdR0CC64X7i7nlMUI2ljUgb7IuQrhKwlc3IfHMm2qB-wVfzzW5K1XTZkwskUxWxnsHimNIUtUXEcSTlICejg2RuGKfJ3zLL5UIyUOxoPk0zMdpl_nXWVb4XSNPWUMD1wgOgxKOgoFHXVhiazog9Hd3iXvENSs9KiAqEi78GrIswnHPI0cv1wFNIAGkLOxSTKfdN09yWxGizO9wlq-TsSzHygoTlN-WeD5QSyAk7z9aQD4nDvXdiBaWPStnr27JsyLoUiI6r3Ru6bNFuOnhanrY5-TuAVQU5yEoHsL9-Grd7vopw4PllUhxU8S8Jn_N3wOyGLSIYQXwqGcp3RBhgkC1S7seZVj62s-h5-2zvfx-msxkBE0znc9lobENYV4tDw4Imv5QhyVhExXxZ0VJRYGP0YuWuzd2NM56XiA5wOXIEwxCicWPHC3PBIUs4pCiKfMJABYZJg2i1dTM_yp1IGeEWGuIRtfIIb4xXYGmKPP9MUbkKER4_kX_bShcFBVwnUmF3Dv5DisZWR5O1VOxJFXG3ITqig4LD6hbGS6b6NtFC5s2WR4TBsCKJ5jfLAK1jYzDCysGSd2kcdy5fmck1QshPCFpCaTBxRCwrV3dQhguUs1Wzpr2Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار صداوسیما: اکنون تنگه هرمز کاملاً آرام است و نظم ایرانی در آن حاکم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127380" target="_blank">📅 14:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127379">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glmsNzP-F9Xg-99Y2824bhPnbCUcyu4rM7BlV151lsmzftol6sgOEvl0oJkbYaJHBa9AXOTV7fSZ_fbW-8PEfxdIKlCUJdJJBRljxG6s0iJjXvMBjdBPwyW3aSqw_rQXf2Gl9SLsiqkWx0ukV8Bh-tYBCSmnXPF7a4JOgbyjdsU0TBtkRhJ7j-51lMCFznI1cledR3o8zXmCyKOSuw93NiDomZaRdOmrqK0fxB9nrgF4JDyc3pEObUZqS1KdYLb7wS7RoClGrDhtfmKZleILCtasTiinTKhrCZMDYuhCbJiflC9xaxLSITuaK5RHKG5iokVi2mHAB5AiMaa_ap8iRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خودروسازان در حال ایجاد یک ائتلاف مشترک برای اعمال فشار جهت وضع مقررات جدید هستند.
🔴
این اقدام با هدف ایجاد شرایطی برابر و افزایش توان رقابت با ورود گسترده و موج فزاینده خودروهای مقرون‌به‌صرفه و ارزان‌قیمت چینی به بازارها صورت می‌گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127379" target="_blank">📅 14:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127378">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0QY32Y4XQlFKD1pZDZzCWj-4gfocOci-0kqjibd_koI-ypoHsmCvf3nlufKWxB8WsoN7v0qh_xo-_6tRH0PIJtS0_tH8NPO5OyB_35v1jCyYM_Yp-O9iQ4SFv3ABN51Igxv1uuwCuHPZBndWljmlw8rOMgOjBSHUvA2z_0zWxr11Ep426ZmeEDjVMCatiRwOihq-2QeDnKEX0sU4DF_y_jsM1ywFP9BbuCnGLtTPhedXXid5pnrak8YC3pmfIWoemU8yNgAgtjGpmDn36i7JzNWo53TBs0zPfinmmYURWZn8oTutVcZh0ymyqa68EeB3fv2gvMoA5tEYQCw3QLJSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/127378" target="_blank">📅 14:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127377">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c811e80be0.mp4?token=eDFvjK-PUX74wy5zjPZOKqoc7szR09l1l_4PxWfWazwtGUpwJ-_3-eferzQjiWDdPFcNwaN27D9Bvvy9nmSSMlh1TqW1_vXsfFxHKKR13Zu2qlLoWqXbbUGHmfTfUMIlJdRFW6P2tbX_74K9Hg22CazQaeGhKixOzUSTK-Gng69BBKmNydTg7MKQGqZk8Jyn2cfo-Sq-0_1JEeyhYGO9GPNG94rnZBtZqDoaDIrwFSiTjl2vpPy_usBcsMIxqe_zliFA_jFu667rvII82p2W5vcBU9ycPdsY-moXtMnDYKtQ8zP9UqgXEyFuq4hYG6fxiu9nz97TE-_36q4ZK2Gb3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c811e80be0.mp4?token=eDFvjK-PUX74wy5zjPZOKqoc7szR09l1l_4PxWfWazwtGUpwJ-_3-eferzQjiWDdPFcNwaN27D9Bvvy9nmSSMlh1TqW1_vXsfFxHKKR13Zu2qlLoWqXbbUGHmfTfUMIlJdRFW6P2tbX_74K9Hg22CazQaeGhKixOzUSTK-Gng69BBKmNydTg7MKQGqZk8Jyn2cfo-Sq-0_1JEeyhYGO9GPNG94rnZBtZqDoaDIrwFSiTjl2vpPy_usBcsMIxqe_zliFA_jFu667rvII82p2W5vcBU9ycPdsY-moXtMnDYKtQ8zP9UqgXEyFuq4hYG6fxiu9nz97TE-_36q4ZK2Gb3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این ویدیو قدیمی مجدد وایرال شده!
🔴
فائزه هاشمی: مجتبی، بن سلمان ایرانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/127377" target="_blank">📅 14:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127376">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
العربیه: وزیر امور خارجهٔ پاکستان در گفت‌وگوی تلفنی با مسئول سیاست خارجی اتحادیه اروپا دربارهٔ تلاش‌ها برای دستیابی به تفاهم میان آمریکا و ایران گفت‌وگو کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/127376" target="_blank">📅 14:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127375">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
خبرگزاری ایرنا: تهران تضمین‌های مشخصی در مورد دریافت خسارات از طرف‌های ثالث دریافت کرده‌ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/127375" target="_blank">📅 14:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127374">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5tnQmn0wrh8tm4gZBcc5sSWEz6yCKG_itU810uwi5Y3-C9wE-FMqC-nXz0q4bED7SeU61RUtC0EfJEo2A4yhhuh-AAPYes7PTI0E6QtbQVYUnsXTBlFl7hLgD97F5IIBsXSIk5pCiUjtgd6TIbycdEhz4FPP8ps3F3RBC6j3FxAQ6u63KomARDwsf64gX8GnY4JzMUvIaLF-iDSe90K28W9lF0Rsbv-qcHv67M_9EXJyhp88ca683PS6fZZ-SJJwsMMl6_wmRcyZfrQnnIPmwQfe3CELs2tJMwMgvwLnMT1HR01oWYmNQA103zG5oPd8OUxgOMDzi4aMx4Kkqxxow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی:
توافق چیه؟؟؟؟ اینترنت رو قطع کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127374" target="_blank">📅 14:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127373">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6v1BvlKK9w5C1-6FB_d9LIyCgnX8vUcrQE_mUHTJl5WqebEGjV62mdbw0xj5QhQ4ZW6IhObvBLY5LgyMZPDF7r3GsI2ls4kM8s78yT2BuJGtkA680Do1Dq3NiUQ3i7WuirEfLSVxIFMzMBf5LI0GV8QWjMHjVud8-j_0xBUCge1xFMrVJ2_tRXhgT-8NmRn7bVsWAhd7a00Qik0Pwmh3ULcUu8OPy0lCKruwZrDIqRYpQHxigrNwXnm_laI5dSBnex1XINMNp78YPW0ln98Q0flMmPjy7PP0JuLgZMJCUg1AJVJe6zZJTKSfYUYmPIyCQItmAeQ-LCAPYwcMhm0vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جزئیات خواسته های ایران در تفاهم به روایت ایرنا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/127373" target="_blank">📅 14:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127372">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گویا تجمعات شبانه امروز هم ادامه داره</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/127372" target="_blank">📅 14:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127371">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بعد از علی کرار! علم‌ماند برقرار! که مجتبی آمد و رفت به رزم و امضا</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127371" target="_blank">📅 14:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127370">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a44893f6f.mp4?token=BDROoNNhIhVWeXZXaHvxoZNi07GzD-ZU7_9aVp1gukcf0nU2dTwq4N0NpH5S_DaxUEBcCO9ZF6epTcB2bJI05p8Q94PR3x1dcSHz0LJNJxNvba0EfukV0PRjUmGtwvW2ejW6CtT51fIYrsmQEUSTVAXBP3wHN5UVta6PzarauIfji7K8wzL5kdbkHNWv10HYTh0_ayLwMsdWGGvVHgWQlq58S_O_ss_LecV_UzD-koJOOrPEak6LElEAY8g4ZQTkVpDBphVYOkY1v4TLeI-rKPb0tscx9OAa9QVkCWkv1GJMozg076F5KyUtS_tteTcRSQHTEHH2RgJwCnfp_vNBNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a44893f6f.mp4?token=BDROoNNhIhVWeXZXaHvxoZNi07GzD-ZU7_9aVp1gukcf0nU2dTwq4N0NpH5S_DaxUEBcCO9ZF6epTcB2bJI05p8Q94PR3x1dcSHz0LJNJxNvba0EfukV0PRjUmGtwvW2ejW6CtT51fIYrsmQEUSTVAXBP3wHN5UVta6PzarauIfji7K8wzL5kdbkHNWv10HYTh0_ayLwMsdWGGvVHgWQlq58S_O_ss_LecV_UzD-koJOOrPEak6LElEAY8g4ZQTkVpDBphVYOkY1v4TLeI-rKPb0tscx9OAa9QVkCWkv1GJMozg076F5KyUtS_tteTcRSQHTEHH2RgJwCnfp_vNBNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
۶ سال پیش"علی خامنه‌ای" گفته بود :
- اصلاً پیامی مستقیم برای ترامپ ندارم، چون حتی در حدی نمی‌دونمش که بخوام باهاش پیام رد و بدل کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127370" target="_blank">📅 14:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127369">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
فایننشال تایمز: هفته‌ها بمباران ایالات متحده و اسرائیل، مجتمع‌های موشکی زیرزمینی ایران، از جمله یک سایت اصلی در نزدیکی یزد را هدف قرار داد.
🔴
با وجود حملات مکرر، ساکنان و تحلیلگران می‌گویند که ایران در طول درگیری به پرتاب موشک ادامه داده است.
🔴
در حالی که به نظر می‌رسد بمباران، میزان شلیک ایران را کاهش داده و به ورودی‌های تونل آسیب رسانده است، ارزیابی‌های اطلاعاتی و دیپلمات‌های غربی معتقدند که تهران بخش عمده‌ای از زرادخانه موشکی، پرتابگرها و زیرساخت‌های زیرزمینی خود را حفظ کرده است. طبق گزارش‌ها، بسیاری از تأسیسات ظرف چند ساعت یا چند روز بازگشایی یا تعمیر شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127369" target="_blank">📅 14:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127368">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فوری/سخنگوی وزارت خارجه: متن توافق پایان درگیری ایران و آمریکا تقریباً نهایی شده و منتظر تأیید نهایی نهادهای تصمیم‌گیر است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/127368" target="_blank">📅 14:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127367">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
فوری/سخنگوی وزارت خارجه:
متن توافق پایان درگیری ایران و آمریکا تقریباً نهایی شده و منتظر تأیید نهایی نهادهای تصمیم‌گیر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127367" target="_blank">📅 14:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127366">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
فرودگاه هامبورگ در پی یک حادثه امنیتی تخلیه شد
🔴
شبکه ان‌دی‌آر به‌نقل از پلیس هامبورگ اعلام کرد که فرودگاه این شهر در پی یک حادثه امنیتی به‌طور کامل تخلیه و تمام پروازهای آن متوقف شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/127366" target="_blank">📅 14:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127365">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
خبرگزاری دولت: هدف اصلی امضای تفاهم‌نامه، پایان جنگ در تمامی جبهه‌ها در منطقه است. در این تفاهم‌نامه پایان جنگ علیه ایران به اضافه تمامی جبهه‌های دیگر منطقه به شمول لبنان مورد اشاره قرار گرفته‌است.
🔴
نام کشور لبنان به عنوان بخشی از توافق پایان جنگ در صورت امضای متن فعلی تفاهم‌نامه مورد اشاره قرار گرفته‌است و
آمریکا تعهد می‌دهد که رژیم اسرائیل را وادار به پایان جنگ در لبنان، کند
.
🔴
عبارت تمدید آتش‌بس در متن فعلی ذکر نشده‌است و اشاره به چنین عبارتی در برخی گزارش‌های رسانه‌ای نادرست است؛ متن تفاهم‌نامه خواهان پایان قاطع جنگ در تمام جبهه‌ها می‌شود.
🔴
تهران تضمین‌های روشنی برای آزادی دارایی‌های مسدود شده بر اساس ساز و کارهای مشخص و مورد نظر تهران دریافت کرده‌ است و در صورت تصمیم تهران به امضای تفاهم‌نامه پایان جنگ، بخشی از دارایی‌های مسدود شده بلافاصله و بقیه به تدریج در طول مذاکرات، آزاد خواهند شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/127365" target="_blank">📅 14:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127364">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d242dab561.mp4?token=MaMfg3QkOZHmfu3ixB6Xg9McANvBLvYPBmjix8cZVrhcyPjH_MpCWWLIIvqGMv2eQT0PBSzspWCi3u7OISnMj_lpniPo3KQPF0GDWFC6xcc16AK9wkXOB3hawu1L6C9IoCHtMDd6nJhtP-VzLeHNs23227a67nVxFwtDYoaZRJdwVzmspwr5qssDqVzsHGtR6VxbRFN-uXBDvrRY-HwoSehW1QywJVrRb14_AgMrED53R7vFrbTWHc6E2Zh0FjPiRX2VYN4IJoPmVfVl0oAHSL0ogBlB_RvotNrHcHy7MeETmc_vV37CiQp9faQIf0968ffs5sufNeZD7oglM5u3aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d242dab561.mp4?token=MaMfg3QkOZHmfu3ixB6Xg9McANvBLvYPBmjix8cZVrhcyPjH_MpCWWLIIvqGMv2eQT0PBSzspWCi3u7OISnMj_lpniPo3KQPF0GDWFC6xcc16AK9wkXOB3hawu1L6C9IoCHtMDd6nJhtP-VzLeHNs23227a67nVxFwtDYoaZRJdwVzmspwr5qssDqVzsHGtR6VxbRFN-uXBDvrRY-HwoSehW1QywJVrRb14_AgMrED53R7vFrbTWHc6E2Zh0FjPiRX2VYN4IJoPmVfVl0oAHSL0ogBlB_RvotNrHcHy7MeETmc_vV37CiQp9faQIf0968ffs5sufNeZD7oglM5u3aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ملت وقتی به تحلیل‌های خوش چشم اعتماد کردن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/127364" target="_blank">📅 13:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127363">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
خبرگزاری دولت: متن نهایی تفاهم‌نامه تا زمان پذیرش قطعی آن توسط دو طرف منتشر نخواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/127363" target="_blank">📅 13:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127362">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
خبرگزاری دولت: به گفته سخنگوی وزارت امور خارجه جمهوری اسلامی ایران، کلیات و متن تفاهم‌نامه پایان جنگ میان ایران و آمریکا تقریباً نهایی شده‌است و در انتظار تصمیم نهایی نهادهای تصمیم‌گیری در ایران است
🔴
تهران در طول دوران تبادل پیام‌ها، برای اطمینان از اجرای برخی مفاد تفاهم‌نامه تضمین‌های معتبری از برخی طرف‌های ثالث برای اجرای تعهدات پیش‌بینی شده دریافت کرده‌است
🔴
بر خلاف برخی ادعاها که از سوی برخی جریان‌ها و فعالان سیاسی در طول قریب به یک ماه گذشته مطرح شده‌است، متن تفاهم‌نامه پایان جنگ میان ایران و آمریکا با دقت و وسواس بسیار تهیه شده‌است تا جای هیچگونه تفسیر به رأی و فرار از تعهدی برای طرف مقابل وجود نداشته‌باشد.
🔴
تا زمان پذیرش کامل متن توسط جمهوری اسلامی ایران، تمامی متن‌های منتشر شده در رسانه‌ها، صرفا گمانه‌زنی‌های رسانه‌ای هستند و متن نهایی تلقی نمی‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/127362" target="_blank">📅 13:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127361">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/127361" target="_blank">📅 13:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127360">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
پزشکیان: ملت ایران با وجود همهٔ فشارها و تهدیدها، از استقلال، عزت و تمامیت ارضی کشور دفاع خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127360" target="_blank">📅 13:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127359">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
تسنیم به نقل از منابع آگاه: فشار نظامی و دیپلماتیک آمریکا برای تغییر در متن ۱۴ ماده‌ای پاسخ نداده و آمریکا از طریق واسطه قطری اعلام کرده است که نیازی به اصلاحیه‌های اخیر آمریکا نیست.
🔴
این متن همچنان نیازمند بررسی و نهایی شدن در نهادهای ذیربط در ایران است و تا آن زمان سایر گمانه زنی‌ها و خبرها، معتبر نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127359" target="_blank">📅 13:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127358">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
اسرائیل هیوم: ایران موافقت کرده است اورانیوم غنی‌شده خود را تحویل دهد.
🔴
از غنی‌سازی بلندمدت صرف‌نظر کندو  آمریکا ۱۵ میلیارد دلار از دارایی‌های ایرانی (در قطر) را برای نیازهای بشردوستانه آزاد کند.
🔴
ایران باید متعهد شود که به دنبال دستیابی به سلاح هسته‌ای نباشد. تنگه هرمز بدون محدودیت باز خواهد شد. هر دو طرف متعهد می‌شوند که اقدامات نظامی بیشتری علیه یکدیگر انجام ندهند.
🔴
پرونده لبنان همچنان شکافی بین آمریکا و ایران باقی مانده است. انتظار می‌رود یادداشت تفاهم روز یکشنبه در ژنو امضا شود، در حالی که ترامپ برای اجلاس جی۷ در فرانسه حضور دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/127358" target="_blank">📅 13:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127357">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
کلش ریپورت: مصر و ترکیه در حال برگزاری یک تمرین هوایی مشترک در چندین پایگاه هوایی مصر هستند.
🔴
این تمرین شامل مراحل نظری (یکپارچه‌سازی مفاهیم رزمی، تبادل تخصص‌های آموزشی) و پروازهای عملیاتی متمرکز بر مأموریت‌های عملیاتی مشترک است.
🔴
هیچ نوع هواپیما یا تعداد آن‌ها به صورت عمومی اعلام نشده است
🔴
این تمرین پس از مانور دریایی مشترک «دریای دوستی» در سپتامبر ۲۰۲۵ برگزار می‌شود، که اولین تمرین‌های دریایی مصر و ترکیه در ۱۳ سال گذشته بود.
🔴
دو سال پیش، برگزاری یک تمرین هوایی مشترک بین این دو کشور غیرقابل تصور بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127357" target="_blank">📅 13:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127355">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
فارس: آمریکا عقب‌نشینی کرده، ایران بررسی را آغاز کرده و هنوز هیچ توافقی حاصل نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127355" target="_blank">📅 13:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127354">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
بلومبرگ به نقل از یک مقام گروه هفت: توافق بین واشنگتن و تهران به احتمال زیاد یک یادداشت تفاهم خواهد بود، نه یک توافق نهایی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127354" target="_blank">📅 13:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127353">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
بلومبرگ به نقل از منابع: توافق بین تهران و واشنگتن ممکن است یکشنبه آینده در ژنو امضا شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/127353" target="_blank">📅 13:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127352">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a72e0fc3c.mp4?token=HRqY-A1xsUprRJs28bZ_l9m7LyZ_R3qaZwMIyz7jqkH9n6WFBlA1TXYRwkUv5P492kYQvN9LUiCk4OIkp7JvxgihGNyXdgQIgAy_Bsufu183k_jvFf9GJSnhRAAdMMocsx0dt2DxcMH2MeQ3oLSkI2_trAgSTpH7Rllq_8BWpjmS-dJcFOvuzIN5bsa6ncVzwxIBa2jfPx6r2jmaa7Saba39DSdyChayDtPPhdc-WSI-1A4JZf9p6rXzIltbuJui7g-R9hHpGnD9Y37IXzQGKnfdQmksqzXxFQ4UE4EJgyOJct_Mr-jJ5wyAsXO1GEvzm-r1a8-dMJd5iFOB24ChcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a72e0fc3c.mp4?token=HRqY-A1xsUprRJs28bZ_l9m7LyZ_R3qaZwMIyz7jqkH9n6WFBlA1TXYRwkUv5P492kYQvN9LUiCk4OIkp7JvxgihGNyXdgQIgAy_Bsufu183k_jvFf9GJSnhRAAdMMocsx0dt2DxcMH2MeQ3oLSkI2_trAgSTpH7Rllq_8BWpjmS-dJcFOvuzIN5bsa6ncVzwxIBa2jfPx6r2jmaa7Saba39DSdyChayDtPPhdc-WSI-1A4JZf9p6rXzIltbuJui7g-R9hHpGnD9Y37IXzQGKnfdQmksqzXxFQ4UE4EJgyOJct_Mr-jJ5wyAsXO1GEvzm-r1a8-dMJd5iFOB24ChcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروی هوایی اسرائیل داره به روستای تبنین تو جنوب لُبنان حملهِ می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127352" target="_blank">📅 12:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127351">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
مقامات گروه ۷: تفاهم‌نامه آمریکا و ایران ممکن است همین یکشنبه در ژنو امضا شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/127351" target="_blank">📅 12:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127350">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceca5f8bc2.mp4?token=a5TlP1OoWLXNgZDI01dyhFAGsfLlcAoQ3Dxo20N6AK8WYcQUjOYHIAIvErikXN4FH2K46iylm7bu_wmi5VaR0GVaJRZ8J9mLzdyafJLdKlmgifY_gQXAqcKNNoq4_9K0aP3kWGmZCQEWy33HiCRdP8_oeQb029ddMyKTafnj3zQeulDHIVZIEWX_WWBJLdPsyksO7b9oF0as4Po41BuGLdRziaC4lT6409g2vrcF-bjYrPC6tS1RXMNXrbBvfDvbasCEAFkN9n7tPE_PDpffvnO4zwlhVFjmWG9goLn3FtvJHZpX2aQmNF75KlGi_QLjtHYiWpGp0cVbAWXoJytEoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceca5f8bc2.mp4?token=a5TlP1OoWLXNgZDI01dyhFAGsfLlcAoQ3Dxo20N6AK8WYcQUjOYHIAIvErikXN4FH2K46iylm7bu_wmi5VaR0GVaJRZ8J9mLzdyafJLdKlmgifY_gQXAqcKNNoq4_9K0aP3kWGmZCQEWy33HiCRdP8_oeQb029ddMyKTafnj3zQeulDHIVZIEWX_WWBJLdPsyksO7b9oF0as4Po41BuGLdRziaC4lT6409g2vrcF-bjYrPC6tS1RXMNXrbBvfDvbasCEAFkN9n7tPE_PDpffvnO4zwlhVFjmWG9goLn3FtvJHZpX2aQmNF75KlGi_QLjtHYiWpGp0cVbAWXoJytEoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست به مناسبت توافق ۴۴تا پرس سینه زد و فیلمشو منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/127350" target="_blank">📅 12:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127349">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
خبرنگار العربیه: یک تیم حقوقی پاکستانی در مراسم امضای توافق ایران و آمریکا در یک کشور اروپایی حضور خواهد داشت.
🔴
ایران درخواست کرده است که امضای توافق با آمریکا در یک کشور اروپایی انجام شود تا به آن جنبه بین‌المللی بدهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127349" target="_blank">📅 12:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127348">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
مقام آمریکایی به Reuters : دو تا پهپاد ایرانی دیشب خواستن به کشتی‌های تجاری تو تنگه هرمز حملهِ کنن، ولی رهگیری کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127348" target="_blank">📅 12:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127347">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
رسانه عبری i24: از جزئیات توافقی که تاکنون اعلام شده کاملاً مشخص است که ایران تضمین‌هایی از آمریکایی دریافت خواهد کرد مبنی بر این‌که اسرائیل تا پایان دوران ترامپ هیچ‌گونه فعالیتی در خاک ایران انجام ندهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127347" target="_blank">📅 12:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127346">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل: مذاکرات نهایی ایران و آمریکا بر مسائل اقتصادی و هسته‌ای متمرکز خواهد بود و شامل بحث‌هایی درباره برنامه موشک‌های بالستیک ایران نخواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127346" target="_blank">📅 12:40 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
