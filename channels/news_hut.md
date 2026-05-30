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
<img src="https://cdn4.telesco.pe/file/hWTyKqVK6ea1yiJ2u_KQEwwydZkQAsDxCbkBEU0Kq0uAToDDSPeG_1xk5jh0fRoEux2VH6O1P7B2zSz2PIPvc3gH0GVCksswo390WwuCXsUvuPBJsURUVGDrBT1t20hMjj9BH8EAzRxwLO1dU4KwDqrCbGRktddvLm0ZhTk5NR84YEpxSl6EhdNHOekPC7Or1egRgcdqqPVItsacLbY3mY059hB7b3-CwUUi7Qx8k_RTk07fneXQrkY8vQzDh7cOWUo84A_ECRVFN2QVxhxu-15E-4Hf_1IbRsGEkXhRnzEbqWQUf8PdmDPCXzc08-pzpnGKVxpuqSOc0Pxlw9fHbg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 152K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 18:20:33</div>
<hr>

<div class="tg-post" id="msg-65162">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
پیت هگست: وزیر جنگ امریکا: محاصره دریایی همچنان پابرجاست و به‌صورت دقیق انجام خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/news_hut/65162" target="_blank">📅 18:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65161">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OE3y153OiEV0-w7QCO-fKoFU8sMxgLOlv1FzMg70HSBrKlEmgZ7yh2vFWsEksoFCQGANjRHJYVWDs_szx1hy8plWTfwxiEVOyCf2BhhnzqhH0EyWFA9L9IB6-EgAzEThXoQZ7UWBQob-qIE0LjfC8iB_Ngb1By93bQtRCVz70iukDdpLNm4zSEOO6wS-u19r2pU13-lZMtjHBcEvwhCnjC28TDjuzueQAxeaOfw36mAtEPjuyRKazuyQLehNs08J57hT4WYjRcCcIxZAvrzeYAyfIW2X4ny3YWIr4ZTg1IhdP3HjQ7CLrBtNrf9kF0UKHsBLSZe2O-hjikfaom0llg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی: من فهمیدم ترامپ برای بار سوم در حال خیانت به دیپلماسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/65161" target="_blank">📅 13:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65160">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/news_hut/65160" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
✅
🎁
کد هدیه 100 دلاری:
Sport100
🌀
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🥇
صرافی معتبر
🌐
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/65160" target="_blank">📅 13:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65159">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YiH3qu-K4PtYkBhrTTKLS4_3QFL-k9kMJ4-lovwveLuZ9FDpYRTOAsRIDBJTl-1b-_fR_fJmuHGS49o9QNUSnxC8ujKH48-HII1tEb5AjaLzbSrYGModpryJn6z55ZIIidsRLXOPtflnr8DHbqJzLD03uh8hhsp9FH1GwB0HPUFAgLQ7pwafQOWUk-qhnqnfphdpNTum_CDbQNIe4_Ob_DIZE6GnUaDUfp7agM-SKevGYeDmoOWejTRWeaJFiSUaNRZSfQKd84va9bfvS_HP7pWceyGa8eZVcaGpKOB9E2g6ZiE8arqBry4gixQq5HObjXEgH7UpYgXZP-YmADa6vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
فینال لیگ قهرمانان اروپا
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
⚽️
🔥
😍
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/65159" target="_blank">📅 13:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65158">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p_viwmkKmpjGLen1S98g3xeQOQ1w2OhZ8YF2cVsQjxUNsSt-4nheazKedLVLxMQDyx_w34A7tBDuFIrrvxEYAA9n_rTc3kBHxhymTKJpKUjmwgY5AHZiozC7huvhCmH3OjwlseM0uyFf6T6kMuFluUaIk9jJnkuhO1UlNGC_fhr18zx7KWlPPnCplJd-g5b0q_9Q-sbXB3hMBlUHj1oDA1F1NTI5tLNP_wA9zA7Zpbgj41B7ZU0hNYqfJN7sOSk6KNm28v7yRhzSHUxpyH-K8fOrMxx9APgJHl_xieund3gbxUekhh-So_d8EOZLdAE4wFXzYBhFlf1PYmon4HjbLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاخ سفید آخرین معاینه پزشکی ترامپ رو منتشر کرد؛ ترامپ ۷۹ ساله در «سلامت عالی» با عملکرد طبیعی ریه و سیستم عصبی قرار داره، و قلب‌ش۱۴ سال از سن‌ش جوون تره
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/65158" target="_blank">📅 13:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65157">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
سازمان سنجش: کنکور ۲۹ و ۳۰ مرداد ماه برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65157" target="_blank">📅 11:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65155">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BwvqwIokekMc6LMURdDbKyF85EwBEVEOUzMwYI4E0JIYpYxmHOQ_EF-9isDGHAE_GFnkTIK45aW--pV2O4m-PtGYUXqr_crRiQivaAxXPKgX50WeKdnEsedlWvbm-wlAG5bcCRyzSCeIgM1_T3OGpObplA25krmszVyeHetMXCjmtvxRCe9oiv5B2gJiTH0iClPGFFHbeKmNVpOaxf16X7plQaymxg6P9XyJcUxtF0I0VF0FIUcD_1mnIEfk4MhEWgIc8fSZKyDoGxA52EX-9ZiwNUDBBBjqJ_hxd4CZ4PfUUNhvzU8dRKzJoqzSWYNOfTqz8kaF-QARIeznIrTFVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U8PMP7CfPVh9Mx2_x7ciZFH3t2BTU6ZG9P3s417vBkFSPjGm03_VPSxq3SlXSsbahjkMwm5UudT5dUca5Jh09_ly3ccjGC-FN-J28kjlghjoSjQtPXp2Igm9kM0eQr7xWPdkGZ1LNPZJzMmeRv0h6ahBaB47bJksCpZyaE0Uu4NoYBObu37p2gQIRH_0txxpKn_aZXRphjLZFHawIto2cqtDw_wx2bQZRwS1mHLUE6vylWlX9PJ1G9hbg390Ls693IrSj_cU8uv5Z59i0ehr1cPNzq8tYqLN1Q-okAFy8uuUtiz6olo8ADO9Trdo2b8VorEWyUdP5DDuBirbj-ISuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ملت اینجوری دارن قربون صدقه‌ پزشکیان میرن چون حق مسلم مردم رو ازش گرفتن و نصف نیمه بهشون برگردوندن!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/65155" target="_blank">📅 10:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65154">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/auBluwErLAa62oWB-NPDXkoZ6wj8pWqR9YkleFXzK0wiMuzaxheRpY__yHc8tJhM6Kx2KzM58zDbc6rRSE3kl7JkAM_thoECfvtvT4z4Iy0CPeFlJzeHb6p7Cxe4m4U9W4sxLrYzOEdRztxLEY2zmH6c00qkFlrPHTQEKpaQAsTckTvAIP1eQu4_lHBrtz33mhiOtgU4fjPYdmCIy0nT1x-v8FI6lDNbioMZPvF0tbkztehJwrSSzBos48L8jGAjg6KhW8Uq3AfVbbcIegEdzzrkgzH5p-N6b8WCq3K_M7spJCrmhN-JaeIxh1WWVw5XaO25Nvgo0bjo14Xv4zO89Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از عروسی‌ها و صیغه‌های نمادین تو تجماعت شبانه حکومتیا یه پسر ۱۷ ساله با یه دختر ۱۶ ساله تو تجمعات عروسی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65154" target="_blank">📅 08:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65153">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
😮
تنها سایتی که با عضویت بدون  واریز 500,000 تومان شارژ بی قیدو شرط میده #وینرو هست
💰
👑
#معتبرترین سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65153" target="_blank">📅 00:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65152">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kObEhiNjRM9MTYOtkjV24Ql-x26oQ_e7YZpjKW0fahQVl-KZQ2HqKaUguw3xxVGUQwDa-UxltbgMwazw-RFsSbTrXAj35djZGZ6bxIhQEaE-0rdYl2O5Xtl_XmokFWTGK2H_Y64JMykkGOJzgsIOyyNmyimwJT5sMRdIbdNR2RInDxv8ifeoHioFUHJnw54rVLlpims1_o04rpOmxpLG2kZgW6t1Mm4MjxWO61LJfWLgNml_7BTe3VFX_rcpf1HePqcgg7kvaVtFE8l9NRq6cugHuidKa1xfmKSOb1_qAgxP8PfL8Rdp6J8_VGTGCniEn-RPXNseUeeZukyEcvfUUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
😮
تنها سایتی که با عضویت بدو
ن
واریز
500,000 تومان شارژ
بی قیدو شرط
میده
#وینرو
هست
💰
👑
#معتبرترین
سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا
a8
🎁
📱
@winro_io</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65152" target="_blank">📅 00:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65151">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=s8M7_Mch-aoz0aoESh4jpuOlUi7atHif4F8H9swPIIiTtMLjfRln91iPI60Am1wcxaQemuVQM8-QQXBreNETwBhLps13_cUpoEHq6OJ9XictYBQXrbQNY_AtOuixYyVcKShfZrpDC2doFT_VhMWr3Tf9rdzEKFtUTIkSd8UjqvnCeqt2eTp3BiyzX4Aw-foUnD8ZXIookSS8j7J21F1qqc6b7Bil1ccDTfVS_d40WsEA0IRSeznacXGlYNnHnD3_o_pirlOk0p-InH9xKDvkzxR2x_iLStOHt-ZTNtO6qkg_PfNldeTtVLC-YIpi96SeeeMiP6lzUcHarmzLLmCceQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=s8M7_Mch-aoz0aoESh4jpuOlUi7atHif4F8H9swPIIiTtMLjfRln91iPI60Am1wcxaQemuVQM8-QQXBreNETwBhLps13_cUpoEHq6OJ9XictYBQXrbQNY_AtOuixYyVcKShfZrpDC2doFT_VhMWr3Tf9rdzEKFtUTIkSd8UjqvnCeqt2eTp3BiyzX4Aw-foUnD8ZXIookSS8j7J21F1qqc6b7Bil1ccDTfVS_d40WsEA0IRSeznacXGlYNnHnD3_o_pirlOk0p-InH9xKDvkzxR2x_iLStOHt-ZTNtO6qkg_PfNldeTtVLC-YIpi96SeeeMiP6lzUcHarmzLLmCceQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
اسکات بسنت، وزیر خزانه‌داری امریکا:
ما حدود ۱ میلیارد دلار از ارزهای دیجیتال ایران را توقیف کرده‌ایم — کیف‌پول‌ها را به‌طور کامل گرفته‌ایم.
برخی از دارندگان ممکن است همین الان در حال تایپ باشند و ندانند که کیف‌پول‌شان گرفته شده است.
این پولی است که از مردم ایران دزدیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65151" target="_blank">📅 00:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65150">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLdSU_4-ywGJstVR_SJz9NDmLmh91Y4i1BWyICuhuXBWUkCCPHMldTGbHduXiQRqEBC9MXn290sbnKI1Aqew1J8OZRWlMIHqc39xymxk0DKfRFQHAjn6_mslX-cQhC1qY5u-eynYl197Bsa9QBzq2ZNxQWhKRxgC2-LxtNse9ECLsjsuLl53z0OtAcM-xON_qr7gnlSfoybWq8NO4WMrwQnVe6vqXHydAOK_VNZeCGSrJNHU8ss_8_3vXxJq4vyeh82t19hgUQfDqMtmVDOLbPX--ObY6p-yz_wkOkYyM-JjXTjLJSq6CevGUcTqLb31TBrwd2K_01J-uL2e2_bCsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحویل بگیر آقای املاکی!!
ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس:
ترامپ باید بدونه که ایران به عنوان پیروز میدون شرایطو تعیین می‌کنه
نقد مقابل نقد، نسیه مقابل نسیه، هیچ مقابل هیچ
البته برای موضوعاتی که مورد مذاکرست نه آرزوهاش.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65150" target="_blank">📅 23:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65149">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbbKkdwSmPUlHUbOx336EHBahShknqBzPLl6_DC5PM26-5ThzM7qSwBw22LNtu3z90PGsW82EiZWV9voBPxWup8CNlNn9KEHd3v8dz8CRK0HqB-g9fFllm3GekVbGEyzEhlcz1GlD5tnoh9OZTbDzCzl1m9fiBFPbEIb-nilQkpE63wF3QLHrMMDGDpGcx3vYZUM48eh9X-7dqAaUJyokL2S42jCSWY-rPbE52M0YNxM_ulEEXpo6IRMH5VApupVLpeUS5InFX-d_06U_BusYJpKvWxn0M472O6O-P65kX9aSZDN2to6q32FogH-rugMZjG90vpItfsr9U2WNj7utg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمودی، رییس شورای هماهنگی تبلیغات اسلامی تهران: ستاد آماده‌ی تشییع جنازه‌ی علی خامنه‌ای هست و میخوایم با جمعیت میلیونی برگزارش کنیم ولی زمان‌ش هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65149" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65148">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uf4lnEgAOhl2BFlWy1CEJs30VL7v6fgsHLLk84JnFmi2XnOAIvsxgsihhz-gF4pVnD7Vv0k4MO79HXkyAUYh0xSEqAbwTJ-fzpUrTGZnjelcIifHw17UYlkLEtreRB_FLwBIP8AdClCICNhd8mPbSQ22yISTLoh-LCZcFlw1K78bibxu84Owx3dv6bU9LCNVQHaJRbzG2SejGxIPQXFkgJ1_OQtt8Inj4eqBAIM1aX82VrUIBXtV1Kx61BkaWpHq8orjax-K7EYs6Eu59p1uLdr37rk2ziZMHYRkIXsEoOV2huNz3Iw5W2r1g1c-1cdOnKZBRvv5ZrHzq3-yePKABQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پاری سن ژرمن
🇫🇷
-
🏴
󐁧󐁢󐁥󐁮󐁧󐁿 آرسنال
🏆
فینال لیگ قهرمانان اروپا‌
🇪🇺
⏰
شنبه ساعت ۱۹:۳۰
🏟
ورزشگاه پوشکاش آرنا، بوداپست
🎲
با بیش از ۶۵۰ نوع آپشن پیش‌بینی
⚡️
با بالاترین ضرایب پیش‌بینی و
بیمه صد درصدی
💯
📊
نگاهی به آمار دو تیم:
✅
پاری سن ژرمن در
۹
بازی اخیر خود در لیگ قهرمانان شکست نخورده است.
✅
آرسنال در
۱۴
بازی اخیر خود در لیگ قهرمانان شکست نخورده است.
📈
میانگین گل در
۱۰
دیدار اخیر پاری سن ژرمن در لیگ قهرمانان
۲.۹
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر آرسنال در لیگ قهرمانان
۲.۴
گل در هر بازی بوده است.
🧠
وقتی بازی با فکر انجام شود، باختی وجود ندارد.
⏩
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/CH100
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65148" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65147">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
گزارش فعالیت پدافند قشم
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65147" target="_blank">📅 21:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65146">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‼️
بقائی، سخنگوی وزارت خارجه: در این مرحله بر خاتمه جنگ متمرکز هستیم و در مورد جزئیات برنامه هسته‌ای مذاکره‌ای نداریم؛ مدیریت تنگه هرمز باید بین ایران و عمان تعیین شه
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65146" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65145">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خبرگزاری فارس به تازگی اعلام کرده ترامپ مفاد توافق ایران را تحریف می‌کند.
او ادعا کرد که ایران موافقت کرده تنگه هرمز را به صورت رایگان باز کند و مواد هسته‌ای خود را از بین ببرد هیچ‌کدام در متن اصلی وجود ندارد.
ایالات متحده باید فوراً ۱۲ میلیارد دلار از دارایی‌های مسدود شده ایران را قبل از ادامه مذاکرات آزاد کند و آتش‌بس کامل در لبنان (طبق شرایط حزب‌الله) نیز الزامی است.
این توافق هنوز در انتظار تأیید نهایی در ایران است. منابع آگاه اظهارات ترامپ را ترکیبی از حقیقت و دروغ توصیف می‌کنند تلاشی برای ادعای پیروزی زودهنگام.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65145" target="_blank">📅 20:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65144">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⭕️
رایگان بدون واریز شرط های فوتبالی ببند از همون اول موجودی 500 هزارتومانه
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65144" target="_blank">📅 20:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65143">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAbSqKRgcf631p825h6MPnGIiFy2LjWLiMnauyOrscr-cJnW4lZFMjN9diLJLWVoZ9OLD7lBnYG_bCthyfwQ49coA9iuNgdYRPtghVMkcgrBMsP_EYpcRViNZ4xUJGL5dGzjy7oUUosMGf7FnZNv1nacevt7jzZicXMSTvwT0sN9YlbkOkZKq8ZjUP7b3aIMlcif-xFOyN0aTFzfwJi5tMcmQqAYnBYi6dhJGI_7DYVEHVWRa1Ijih4qqLjfJXzKfq-i0yTI9IqHyPOsmRZ8le59H-G3vP1mJzGzHcj_tJMx-EJHu9pR1QnUbz1F8gnVrJgOzSu-5kgLTQPTQJFznQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رایگان بدون واریز شرط های فوتبالی ببند از همون اول موجودی 500 هزارتومانه
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g8
📱
@winro_io</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65143" target="_blank">📅 20:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65142">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3lj1cSi1TbZIN_GuCMhXzkvIrWkrEwjOLmBfrSIWWeaJLIXZmH9dbiFT3YE_c8rIQJFCpwtbL-1odvULftBk2AdPFYl5eeh5olHe5fAB_lIudOqcQbBuCNOltLVLtjfbgFTH3-BMqJhZP9pHUmG0yYEjjgQ-gBtxJWoKBJlQ9-i9I0V0Yj8TaakWWETv20uvrx_PrUmIWrvUyfqd87GXkOa4C0gKFqrt9pihegAsU9tIDY8Yx0LXV40CspE_gvH214swfV6Y8lMbvOL_TX5WYOwO_zFQ4inSC6WfkdmQFlqUmmMPrynpweviS_iEjVvp3ryEsnZ3QrinVbPIZG3ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف:
۱- امتیاز رو پای میز مذاکره نمی‌گیریم؛ با موشک می‌گیریم، مذاکره فقط برای اینه که طرف مقابل بفهمه قضیه چیه
-۲ به قول و قرار و تضمین کسی اعتماد نداریم؛ فقط عملکرد مهمه. تا طرف مقابل کاری نکنه، ما هم قدمی برنمی‌داریم
-۳ برنده واقعی هر توافق کسیه که از فرداش خودش رو برای جنگ احتمالی آماده‌تر کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65142" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65141">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⭕️
🇺🇸
🚨
🚨
ترامپ در تروث : «ایران باید موافقت کند که هرگز صاحب سلاح یا بمب هسته‌ای نخواهد شد. تنگه هرمز باید فوراً باز شود؛ بدون هیچ عوارض یا هزینه‌ای، برای عبور آزادانه کشتی‌ها در هر دو جهت.
تمام مین‌های دریایی (بمب‌ها)، اگر وجود داشته باشند، باید از بین بروند. ما با مین‌روب‌های قدرتمند زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز فوراً مین‌های باقی‌مانده را پاکسازی یا منفجر خواهد کرد؛ که تعدادشان زیاد نخواهد بود.
کشتی‌هایی که به‌دلیل محاصره دریایی فوق‌العاده و بی‌سابقه ما در تنگه گرفتار شده بودند محاصره‌ای که اکنون برداشته خواهد شد می‌توانند روند «بازگشت به خانه» را آغاز کنند! از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین، زیر کوه‌هایی که عملاً در اثر حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند، دفن شده است، توسط ایالات متحده بیرون کشیده خواهد شد کشوری که طبق توافق، همراه با چین تنها کشوری است که توانایی فنی و مکانیکی انجام چنین کاری را دارد و این کار در هماهنگی کامل با جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام شده و سپس آن مواد نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی رد و بدل نخواهد شد. درباره موضوعات دیگری که اهمیت بسیار کمتری دارند نیز توافق حاصل شده است.
اکنون به اتاق وضعیت می‌روم تا تصمیم نهایی را اتخاذ کنم.
از توجه شما به این موضوع سپاسگزارم!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65141" target="_blank">📅 18:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65140">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEbFx9vgjaItp0tcd4kbGrmPSz38yYC-Ygpf8W8Ei6F6Ww0ruLUA3f4dCVOp7qcpJeqin2Rfw4v00XKcUPfIL12NCqaMKeiPWHP4gbiu5CeLDc_rxl3ga1-WsIe0GF6sSzbN_ZTnspLqsC5btcQVmw9li7q7rf5xoWso-1kdwpxncjax2pxSp13v03c4EeIqtnzs4bKyPOADFQp6sZn2gyrkJ8fvSApuG0LeVyykxEOhxLkiFU1t48kV9FQ87qXd6NY89XJwa52zWTMBtVV4HFIBk6fYswS3dWpK8_z3SkWLEr2dwqxkb0TCYFwbUffTsP9jHvFN75_wibpNe2RkhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی مشاورین املاکه
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65140" target="_blank">📅 17:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65139">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">Barko VPN_v2.2.apk</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65139" target="_blank">📅 17:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65138">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.2.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/news_hut/65138" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👈
بهترین فیلترشکن حال حاضر ایران
👉
💎
با همه نت ها پرسرعت کار میکنه بدون محدودیت
💎
👌
پیشنهاد ما دانلود این فیلترشکنه
🔧
لینک دانلود داخلی با نت ملی با سرعت بالا
👇
https://uploadb.com/plx39j7b72sy/Barko__v2.2.apk.html</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65138" target="_blank">📅 17:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65137">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qxy0KmutFgk2mSkQ7j_ZtlwcatFZUs5FsfM6K9ZsKtO_TuU9MT7B30AzXq-LVefbb052UrqtbhokdQzww341KfVSzj8j2pbsL2phlp0fUhEWZNnEgNGbVfB-W5iVDtDFFXUi8_u68I4Mi0tR_p0vtO5qPVPdACVz6UPLVzCxJczAB9uzhlJo1OOoQWH9oSKjcgJqGJEU6EBgjzSdCr4OqTkCDzlKrJHOtj8Y_1Qi9fSFGzProsW8Z6xFF76p8VJzNyIoNtghac45QPBDxCGk0n9Tun-d6tFHcKp0MCzfFYjG0b7OShSnMbNgLtK0j7bHyGOC2e7bPXo8rsmWIq2hNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نت نداشتین این دوتا شده بودن سمبل شرافت و نجابت حکومتی‌ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65137" target="_blank">📅 14:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65136">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyZ5xgL1-ckWiZ26LCkbdHGRpxeO-kjQUl_XcXyMTs66e-LEYkMRpkSeEiI5TvZKhJGb6QnXbTrA5EXGf4SWbPswQGarlMNs2FoGRhzwP-Ag6LbWnX4BkZpHKxJh47cDBMu0DPw8yfrJ77ZkfC7zIBdtp3lHvCMFwByt_at8H1juE4k7aaMtchjb3iH3a4JcYaRl3DuMJr0oldQ6r2aVYvV-m31DITw7EmA3BGJDEOU286w7L3kZq-Cmxnm4QTdsgaxrG72gjHWulhC71obM337qA4VUisuD901dJsHcJRIVcIho1m6HGOqLiQ6tx1KGDZKLbxwugRn54TmwAjtFGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌های حمید رسایی تو کانالش درباره چه کسی شایسته جایگاه رهبری است با آیه‌یی از نوح و پسرش که حتی صدای خود طرفداران حکومت رو هم درآورده
خیلی‌ها میگن مجتبی رو به پسر نوح تشبیه کرده
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65136" target="_blank">📅 13:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65135">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=qINp1RLu11hz7Ebr2FjM2S1JPZb12YQ65_JS3QRGrMavXVNemTAwuYo6m-dH1KZuw_zYv1LRAuTnrit0C6KYCBfA3hNPaYl6jP5HfZq6W21KMDUyQDRjkv6K47-3Mz3wKfCFXoe05JB0YJKzk9TbFJ7B8ZJrYO9tF5ypyOnlfXkUwUkiuaTGyofU7asdiyKZLF6ZXjDEJlVQYXyqOp4-whQWaJXQlQjVnbf1SFN5rV3pupoVQhWutF02V_OJCZJZ2SfMiKw-4zDlvjDS1h9wlJ6QQ4TT2q0L1o49dSwB84-3u5U8V3HT3VhMrv9dVXm-_Mgpev2S3KfYYeYIaiVlNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=qINp1RLu11hz7Ebr2FjM2S1JPZb12YQ65_JS3QRGrMavXVNemTAwuYo6m-dH1KZuw_zYv1LRAuTnrit0C6KYCBfA3hNPaYl6jP5HfZq6W21KMDUyQDRjkv6K47-3Mz3wKfCFXoe05JB0YJKzk9TbFJ7B8ZJrYO9tF5ypyOnlfXkUwUkiuaTGyofU7asdiyKZLF6ZXjDEJlVQYXyqOp4-whQWaJXQlQjVnbf1SFN5rV3pupoVQhWutF02V_OJCZJZ2SfMiKw-4zDlvjDS1h9wlJ6QQ4TT2q0L1o49dSwB84-3u5U8V3HT3VhMrv9dVXm-_Mgpev2S3KfYYeYIaiVlNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماهواره فضایی شرکت آمازون دیشب حین پرتاب به این شکل پشم‌ریزون منفجر شد
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65135" target="_blank">📅 12:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65134">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⭕️
بدون واریز شرط ببند و بازی کن چون وینرو با ثبت نام و بدون نیاز به واریز
۵۰۰هزارتومان بهت میده
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65134" target="_blank">📅 12:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65133">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHVsWU0RWCjJ6semxi_jC741uMuG6fFohNjACHd1vWVFJZ89nAv0VX4mM081yN8w-vSc9NzdFPTeXPDrg00f8uIh_gcoYZH82BIu63g0_i7UAT7EnNYR5oJxhoENc-dKQ-1onenG0j8SAH2LpwBDY8giotIebDdv7OILbzixhX39QkzOfI-Zq38OzzmySFwt2Wiiy2wu5CDlGU22QSaHIULyZWRsMhJ5PDEG9G1n_dNpbirDp-Kbs9mkNagFYsvaVP4IeWzaBnCZaSZMcc5RCB3sNMyveyc_sTAi_riBxuY3NS1iQKlYUCcPc_ofjdNIUcjLRAOj2JI6x-XsY49JoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بدون واریز شرط ببند و بازی کن چون وینرو با ثبت نام و بدون نیاز به واریز
۵۰۰هزارتومان بهت میده
❌
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r8
📱
@winro_io</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65133" target="_blank">📅 12:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65132">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUdIxH_pEV6ugogxLYYJYElqPOQalm8mC6c4tkcMBnVeMgvJJDnsetYD-y12qOXL0vz_Pp0tfisWWOmgOPUN2MMlOV1w-i1E5rPSh1oDS_g3MD9MJuxa3PQS5ipI1oX4-k33PStjlUwa2mNQQ_15NciZ7D_c-16rJoF8khwNtne7I-uT8zhlbLDDSXktCTvRUzL6W129RL13YOmhRr6A1nH-IJE1lPmu6D6ylJGCPggdmbIQsTNGQ0Ku5MKMVUsP9kTA83-o6-2Iq6-VhPH-PFz8BeJMXKIX84Ge0v-7mbvQFJaAal00r9mxpF2CaEAECQ4Pf5GVLLKULUmTyrw5_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
واشنگتن پست: دولت ترامپ داره به اداره چاپ اسکناس فشار میاره تا ۲۵۰ دلاری با عکس ترامپ چاپ کنه
قبلا ترامپ ۱۰۰ دلاری های با امضا خودش تونست به چاپ برسونه و اولین فرد درحال درحال خدمتی بود که این اتفاق براش افتاد
همچنین طبق قوانین امریکا عکس افراد مرده میتونه فقط رو اسکناس چاپ بشه و از سال ۱۸۶۶ که این اتفاق بی سابقه‌ست
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65132" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65131">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=WE7ac0YIDN5zkabq0VnoR8DUOoGPf3Erq9OLVCj_1pDTckNjyC_tNNb368kFEGytQppUO2qDI5gEBsbxg8TshX4tcx0weSoLlfUtLx91XP3sqlXhAfrGaDRjrHn0vZKDefDEoJQ_fG3E2HZDiBAuNGum_RT1h92cbYRYoMUDUKu3Gn42R80ZKtooiC4USRggQ2jYNDChkVr6evsG_ou15_lNBBUQ6RvIvm1vlzkUSIxsPk0KiUcdsME8kaIJP38_1R4NerPXJGIDKonxbhb7qWRa23kGS6FNypUEYp72uyUME_cCdQk-gm5_sIoGosLDa5u8j9gVCnmR83MZa2ELLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=WE7ac0YIDN5zkabq0VnoR8DUOoGPf3Erq9OLVCj_1pDTckNjyC_tNNb368kFEGytQppUO2qDI5gEBsbxg8TshX4tcx0weSoLlfUtLx91XP3sqlXhAfrGaDRjrHn0vZKDefDEoJQ_fG3E2HZDiBAuNGum_RT1h92cbYRYoMUDUKu3Gn42R80ZKtooiC4USRggQ2jYNDChkVr6evsG_ou15_lNBBUQ6RvIvm1vlzkUSIxsPk0KiUcdsME8kaIJP38_1R4NerPXJGIDKonxbhb7qWRa23kGS6FNypUEYp72uyUME_cCdQk-gm5_sIoGosLDa5u8j9gVCnmR83MZa2ELLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: کشور‌های عربی مثل امارات و بحرین و مراکش برای تاسیس دولت فلسطین به پیمان ابراهیم نپیوستن بلکه چون اسرائیل رو یک متحد قدرتمند علیه ایران می‌دیدن به این توافق روی آوردن
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65131" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65130">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2SoEsCwsQYPC1FA7UbJIZZkRoy7FQ00LMf7-i0G-sA4crdqxxcyKWXWDxsmOeUwMz1Eoh0-ie_KUsTAuyPbspHQdP_q3sDgqQz156_STl79myZXLzozWijRTJzBLF-hX1VslTC0rreThQnwDDc4_eB_YeD_TOLfBzz7wMFx12stKTuz5B72H1KW2M9pyz1g0zxq6_GOg0eA0KUNAx8KF76TV09HPwMj4m-X119bLI9C-FDFT-okiuDTkK-dFOWAXPfv5ZkjUzGV8C-mQ9jgUB1wlNWKNUpOFawz2IsRjCKod1cWGiQw2XeNoM8nlHGejbawh6EG9_PM0TfP0BGaTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش دفاعی اسرائیل: از زمان عملیات غرش شیران تقریبا ۲۵۰۰ عضو و فرمانده حزب الله و ۸۰۰ نفر از اعضا رو از زمان شروع آتش‌بس حذف کردیم‌.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65130" target="_blank">📅 08:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65129">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
اگر همین الان توی سایت #وینرو عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر،…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65129" target="_blank">📅 01:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65128">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pi7hLJkTmjVSwnq9m3Xbgqoc3n05sDnwo6GZ9lXDhGwyyFB_wvBe_mBxfG8uQmj6ZNcXZ88FEHbRxRm5kxMz7EQU_8ZAxLCdWGVGs9sGxaHKaCu75jmJupQo9iLoUizDkdH7D3p3vWfrPxB2jiSdCZtICrhKI3Kqw4tqyPd_vjLwlJUfhFks8jJPUZR7ALt6LTKWmmiWfuic6jQ1EoJH9ItyLX3wJExDfPI37lsLtDiQK8rFG4DD7BV9rg9NtU6adfpHrSOcys9Z-ETFKFjPa3-2npd6yTrT51rqJ4ltTMtz4Sj4-JTl3TBAnehg5FDFhEXfmquP4JPdqFIGFk21pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اگر همین الان توی سایت
#وینرو
عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
🔴
این فرصت محدود رو از دست ندید:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a7
📱
@winro_io</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65128" target="_blank">📅 01:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65127">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
گزارش صدای انفجار و همچنین پرتاب موشک از شهر جم استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65127" target="_blank">📅 23:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65126">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011753724a.mp4?token=UUVgiIqjKbdgA7pyS4N0nDQrikPfEpSdZ27i1ghUim5NXJhYDx8K2lTpu_H0MMIgSEF0iuzLsxfvdkDSg8noS_ZyMycIXinBZNcGGyiltLv062PAnlvWy6pJry9ttxCggAYss4GcZbylr8tuCMeLIs2ixtg3xWjzHrjW2EsIpdseNUg6i2PzMWxggpe9dLRW537mSz7lslZhZPMfC_syTaJZmEgqGFVcggAPHuMKLvtJAkXARyr0ZabIxZ7l8E8zJ0N_DuAivVD-l7pcQlAdkGRMO7zSy45USlnOiTUn92Eo63GwP3yjrkIRjhg3AmGZDn78Z_c2SGkZ2L-4PlsjdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011753724a.mp4?token=UUVgiIqjKbdgA7pyS4N0nDQrikPfEpSdZ27i1ghUim5NXJhYDx8K2lTpu_H0MMIgSEF0iuzLsxfvdkDSg8noS_ZyMycIXinBZNcGGyiltLv062PAnlvWy6pJry9ttxCggAYss4GcZbylr8tuCMeLIs2ixtg3xWjzHrjW2EsIpdseNUg6i2PzMWxggpe9dLRW537mSz7lslZhZPMfC_syTaJZmEgqGFVcggAPHuMKLvtJAkXARyr0ZabIxZ7l8E8zJ0N_DuAivVD-l7pcQlAdkGRMO7zSy45USlnOiTUn92Eo63GwP3yjrkIRjhg3AmGZDn78Z_c2SGkZ2L-4PlsjdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا کاهش تحریم‌ها برای ایران روی میز است؟
اسکات بسنت: هیچ گزینه‌ای روی میز نخواهد بود تا زمانی که تنگه هرمز باز شود و ایرانی‌ها موافقت کنند که باید اورانیوم غنی‌شده با درصد بالا را تحویل دهند و نمی‌توانند برنامه هسته‌ای داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65126" target="_blank">📅 23:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65125">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umsJiJfuN5TmJPdIcUpLsPSZEG-ZdOX-rJ6F_FZwq_-p4ExhhBt4TCIiTZ0y1aaXXY41q08BUZU7Z0v93u6hi01EZgUdHPfyNHZt0tNshaIU9-yuZBS4avTqLDj5U9eLYtr7yEXsJFaePSmHuFq0TPxWihV2LKDfWOpYpX5e5cBw6LCuOoWGPOAFwtwZRDId4rjM143xRigXFh6Up-VAIU3SHDG_Y-vRvOz-ag5FyEkAIkDXgJnlvjZyaML0O7wX2xOYIYRFHSNBzEPpvi-wdwtBIxi_l51vExcv2ae6otkgtadJJGtB-_w4DbxkH3-y8ZBZ1n9RfOP7ddlpz1eXpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
گردونه شگفت‌انگیز جام جهانی
🏆
⏩
با پیش‌بینی رقابت‌های ورزشی و بازی‌های کازینویی، مراحل هفتگی «گردونه شگفت‌انگیز» ویژه جام جهانی را تکمیل کرده و هر هفته تا دو چرخش دریافت کنید.
اطلاعات بیش‌تر و قوانین:
🔗
bfrd.link/WCW
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65125" target="_blank">📅 23:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65124">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🇺🇸
#رسمی
؛ توافق موقت ۶۰ روزه‌ی ایران و آمریکا نهایی شد و متن توافق، فقط منتظر تایید ترامپ است، هرلحظه ممکن است خبر اعلام شود
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65124" target="_blank">📅 22:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65121">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=oW4TIZ9i-UmlxoXIUTlFL90PJpiev2765S8k0mpCIRQFuqDdE9fGXxywBkmEPM2kFnIgpEgFLt270k-28cuqZ6ka8awet618llQpe2cHljpyOQAYiWZZzQfTeOMqFfxre8yd1si-U3W0o7tTlkNqxLtpnX6pVRjdBwrY2PzXUH98fesYsacmov5iIqv5o8qdYKcM48Tl3-OY8JZdhQAgAJF3NWBfilIJSyDY1XbCxATxmqM-G-ivDxw6FlzCw4Wn2hZuVAdep34dsVYsUXhrp1TJpz9aDQFrtAs-XQ2MHZB2Z8edshNIahC4Yi4abMr8GarpL3FFxlBm3mooQxieQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=oW4TIZ9i-UmlxoXIUTlFL90PJpiev2765S8k0mpCIRQFuqDdE9fGXxywBkmEPM2kFnIgpEgFLt270k-28cuqZ6ka8awet618llQpe2cHljpyOQAYiWZZzQfTeOMqFfxre8yd1si-U3W0o7tTlkNqxLtpnX6pVRjdBwrY2PzXUH98fesYsacmov5iIqv5o8qdYKcM48Tl3-OY8JZdhQAgAJF3NWBfilIJSyDY1XbCxATxmqM-G-ivDxw6FlzCw4Wn2hZuVAdep34dsVYsUXhrp1TJpz9aDQFrtAs-XQ2MHZB2Z8edshNIahC4Yi4abMr8GarpL3FFxlBm3mooQxieQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درحالی که جمهوری اسلامی اصرار داره یکی از بندهای توافق آتش‌بس تو لبنان باشه  نتانیاهو و اسرائیل در روزهای اخیر بشدت حملات رو علیه حزب‌الله افزایش دادن
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65121" target="_blank">📅 22:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65120">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">به گفته باراک راوید خبرنگار Axios، به نقل از دو مقام آمریکایی، یک تفاهم‌نامه ۶۰ روزه توسط تیم‌های مذاکره‌کننده ایالات متحده و ایران مورد توافق قرار گرفته است و در حال حاضر منتظر تأیید دونالد ترامپ، رئیس جمهور ایالات متحده و تصمیم‌گیرندگان ارشد در ایران است. طبق این گزارش، این تفاهم‌نامه شامل بیانیه‌ای مبنی بر «بدون محدودیت» بودن تردد دریایی از طریق تنگه هرمز، رفع تدریجی محاصره کشتی‌ها به بنادر ایران توسط ایالات متحده متناسب با افزایش تردد آزاد دریایی، تعهد ایران به عدم پیگیری سلاح هسته‌ای و تعهد به برگزاری مذاکرات در مورد از بین بردن اورانیوم غنی‌شده با خلوص بالای ایران در بازه زمانی ۶۰ روزه خواهد بود.
علاوه بر این، طبق این گزارش، این تفاهم‌نامه شامل تعهد ایالات متحده برای بحث در مورد کاهش تحریم‌ها برای ایران و آزاد کردن دارایی‌های مسدود شده ایران خواهد بود. همچنین قرار است در مورد از سرگیری جریان تجارت و کمک‌های بشردوستانه به ایران بحث شود
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65120" target="_blank">📅 19:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65119">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⭕️
توییت جدید اسکات بسنت وزیر خزانه داری ایالات متحده.
دولت ایالات متحده هیچ تلاشی برای اعمال سیستم عوارض در تنگه هرمز را تحمل نخواهد کرد.
به ویژه عمان باید بداند که وزارت خزانه‌داری ایالات متحده به شدت هر بازیگری را که مستقیم یا غیرمستقیم در تسهیل عوارض تنگه دخیل باشد، هدف قرار خواهد داد و هر شریک مایل به این کار مجازات خواهد شد.
همه ملت‌ها باید هرگونه تلاش ایران برای ایجاد اختلال در جریان آزاد تجارت را به طور کامل رد کنند. روزهای ارعاب تهران در منطقه و جهان به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65119" target="_blank">📅 19:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65118">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا #وینرو  بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65118" target="_blank">📅 19:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65117">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nytbbmBxXV3CMAicJuewqD4N8xhKh6_K_XMdKUQy0W--MCZ4-3UvHKLM6D-Jlh4HaYD0Wxw7hDLhCGSNXMJCkIrIlLUp3CSw3ovY6_21ad_5RouFjPcTEhwy4oofym5fNu6VPj06gSIYWz9RbakwwXxliUtfAw8GkboriPTMdV2zhQy6uP9u8MDUAjOdVU5umXXoI6rZ9gUZwXT5Hv7WUB5_CaHL421I5pzzNy7Qy-69UTJlhLq7ULHfvy3V90PA0C_FQJ06xWoggUGwAt-7QQ8iVI4lV6XcRiBUtc2qXUedTGyEOlT0-bbG27mKc2Jqo2w-ddTWbEYH8GDSTLvinA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g7
📱
@winro_io</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65117" target="_blank">📅 19:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65116">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9Ahz2pJmtZUaicQA91jBR3xrie51pugwZNdsMWJYOngiLuy-WMv_KCwnOiiz68fFMhBDcORnSX9_BM1MKHKr6f4Sxn6U9_tVk5vXb2cqrZcRCjyyIlnvagFQuLUsaFC47FUK7aN3afg1xQtBTRiOmHC-Cg16XpbfQRwrYY4pG0p3DjPcTNkeM7Mwsg3cBj-0eQZBbgjoGpu5Dy1ck0iDOorcJE6wZgCp2rdcNL4HyVJfaDSXdyXaYD0VoDK63ajPpFgho97YkOoHomLmUOzXot3kpVw0VxlJpggT3QZT8P4sWimAbu-rSdomZMobwXIHVZkh2vI0CzBJkQraPW-Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📰
آکسیوس: اکثر شرایط تا سه‌شنبه نهایی شده بود و مذاکره‌کنندگان ایرانی بعداً اعلام کردند که تأییدیه‌های لازم برای امضا را دریافت کرده‌اند. ترامپ در جریان توافق قرار گرفت اما به میانجی‌ها گفت که «چند روز» برای بررسی آن می‌خواهد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65116" target="_blank">📅 18:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65115">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUIF31mZjcZzrZ2XpsAAj1g1mUmpbugVBjPckwYVryC5xenYiaof82kG_ymyRqawf4k3r-JMoWnTA72cp-aB9NIBmS_AUWWP5OHTCXqFCQAcM5suRDXjT9KpMFFlVGE1MBLcOCbr-x_DeOJdOkk51bywRevxXaRn2f3w4GNwe1-XFPfYXhXrWWBnJcfZU_Ta46wTWzoRetPiGobPYr5CYkN3EulrX3-pj_o-olbxoeYqXtc5cFhLIZxwRN3kBZvn7IvJsSZaR_YJeJo-wR3CVxLH-Ptr8zfq-Dz7ju9Dn007cXAHY2CeZUchY6Q-rVRjdBuzNxfpamgJ9_ok1YxFTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوارنگاره جدید میدام فلسطین از حرف جدید مجتبی خامنه‌ای درباره اسرائیل؛
" رژیم صهیونیستی 15 سال آینده را نخواهد دید"
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65115" target="_blank">📅 16:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65114">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Xi7XNTmvmO1Y96SonqylcD5TWN5VoUMt7Csd2aoEZYoh0U_p4rAA8GlTUN3qdq0jYr9FEtP-HCr1cuzIqjJ1JwuklY4DCIRXlSt5yRFoi-RFqjyNbLABPDdPdMZM6xFKU7MPTNpee1BDdhvvWrtrPSW5FWCyPds0kILUynrQozk_8din_TK2WnME_ybSxDZv-ImT9u6EuXdiQZy3IiC1xi-rb-s48rV6UmpwLgyJ38Yw0YQIjMJiZna58JFnlpS7npDgL_JgD1gNK8vKpzlUVk7sHoi3xKiaecMYKZnQg27sdl5rN7ZqYk4Y3B7phMrRFtwuMNorn0GpdYyWHtVrTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا پشمامم حقیقتا ریخت
✔️
➡️
تبانی نتیجه دقیق ضریب 15.00 رایگان
😳
10 میلیون ببند 150 میلیون ببر تضمینی
💸
فرمای تضمینی و صدرصد رایگان
⚜️
🌟
https://t.me/+BDjkK6j2gcQ3MGFk</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65114" target="_blank">📅 16:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65113">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJ2xmDM0SUXNbYP5b1ZzbkH2tlasTZzKxJHz3L-yo3r0VBHf4w7aLciwgLXyrvmR8PEad_pxXXzEmbk3gm5toxcM31-GJR-qU6gIKqA45tiO9S2PgfkHCa9otH_JXN5-714IgSMIQ8z5zTK9cNDTpemKKst93IE3B0t29gEZ1bSF0TwmgufUMIBiN0TU4U_6tRdM4NiD3nQe8SyGRM2miCpD0nHWigx1spux3mePj2SybGd6sz-yUPP1oT3dNzZDFYeN5bioJ8tkaBjvhxI6xwia4zv7fY2UTWdccYt5A1bUrlyHUDd77NcdbaQxVAAgQlCMxFJvwliApVJTA0buoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⁉️
نت بلاکس
: سه ماه پیش در چنین روزی Iran دسترسی به
اینترنت جهانی
را قطع کرد. در حالی که اتصال اکنون تا حد زیادی بازگشته است، شاخص‌ها نشان می‌دهند که کاربران هنوز با
فیلترینگ
شدید مواجه‌اند، مشابه دوره موقت بین اعتراضات ژانویه و آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65113" target="_blank">📅 16:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65112">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حملات تازه اسرائیل به جنوب لبنان؛ تل‌آویو از هدف قرار دادن زیرساخت‌های حزب‌الله خبر داد
ارتش اسرائیل اعلام کرد حملاتی را در جنوب لبنان انجام داده و زیرساخت‌های متعلق به حزب‌الله را در منطقه صور هدف قرار داده است.
ارتش اسرائیل در بیانیه‌ای کوتاه گفت این عملیات علیه «زیرساخت‌های حزب‌الله» صورت گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65112" target="_blank">📅 13:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65109">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">باراک راوید، خبرنگار آکسیوس: ایران ۴ پهپاد یک‌طرفه به یک کشتی تجاری آمریکایی شلیک کرد. ارتش آمریکا این پهپادها را سرنگون کرد و پیش از پرتاب، یک واحد پرتاب پهپاد ایرانی دیگر را در زمین هدف قرار داد.  @News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65109" target="_blank">📅 13:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65108">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/65108" target="_blank">📅 03:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65107">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/news_hut/65107" target="_blank">📅 02:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65106">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">چرا نت من قبل از وصلی ها بهتر بود، چه وضعشششه آخه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/news_hut/65106" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65105">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">عمو Pishgiri بهم sms زده و گفته خشخاش نکارم
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/news_hut/65105" target="_blank">📅 15:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65104">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/news_hut/65104" target="_blank">📅 15:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65103">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65103" target="_blank">📅 14:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65102">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:  @News_Hut</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/news_hut/65102" target="_blank">📅 08:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65101">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rux21kXgs8HaRU8m7uRhqaxJZ89zM0S1Q7mOtVn5m73KMp-4ZpU5eNMpcoPcoOEQ0T8xzPkU1vnCCm7aFXJZZXoGck_Bg-snp7viFx80a-ANm3UU6SAIb_iZqEiYR91plgQ5Otd1LTtEkpu7Qk-SSoAcAAYgJ_-zxtx0tT0X2EtTrPUADm0OoDMOdRyNCOe4oSXGd24rURBCZeCVzEz3sNfRh4Sp754wfNNT2Ea0ODqw6503FT0xY2aHoM2UQWDemjEKNaSlk32sDxkUl_tZo3hs4kv6Ir9P5NbO9em2p6wK6uJQME11Kcx3Y2SdAVUC-NwNEE0PfnxXvyKSNZ3LuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:
@News_Hut</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/news_hut/65101" target="_blank">📅 08:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65100">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">امروز ۶ خرداد عید قربونه
@News_Hut</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/news_hut/65100" target="_blank">📅 08:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65099">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ir2Ki68jpZAolPw19x-r0mlIxUi0HqcEUGaiHUhYwUjETuK1zTlnkjEYECySGmqh0TQ-58L0ShsyvAZZoKqJQ6aoNmlXbCfyngb4TgKGIvkgZeA4PHcBoBuctt8D2MXJMBrnJbjaOFE2nR6O3KgqmR6fLg2zrOfdeiV2YXtQLy9GWK5XJFH-ZdN4CJ4Y8NYJbqYICOOLubNNPn54OXKZjwdZUXw8MqXVFc6QupG0fUQ1h7UtwOv6hoh0XQirkqlR0eIwBrDgfrxD6kzlSAAMHvdzvil5hzbe35_Njver0UXWBKvr-p14wHX9-IOdz6ib_CW5KKGbWY12jJxGZqPG2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه ها پارمیدا دیگه بعدش آنلاین نشده
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/news_hut/65099" target="_blank">📅 08:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65098">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اولین صبحِ اتصال اینترنت بخیر جوون ایرانی
🫂
#hjAly</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65098" target="_blank">📅 08:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65097">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">جالبه یه یارو مثلا نورالدین الدغیر خبرنگار الجزیره تو تهران میاد توئیت میزنه همچی تموم شده و فقط امضا بین دوطرف مونده
خبرگزاری داخلی و وابسته به حکومت همینو بعنوان خبر میزنه ینی شما بیصاب شده‌ها به منبع ندارین خودتون؟
@News_Hut</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/65097" target="_blank">📅 03:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65096">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NRBPECwnvp9AnopeEzmoUkGBF8xMXcpeB931YkqmJk0flD4mejnFsP3k8ks3s0DguYnlQ0KkwR6jqqOFh6QI5yZhOHG4mQ2OXGtLfszBsqHdxDEWyJApOSC89JGP5zrTaVADHgkBznQ1NpvuMeuOosOr5Cap5_aNfSEWD2ODWQj5agmFSFna_C-QIPSboN0AcsFyicr3ILvh8sVGC0LkslLotuM57q6XN9UXxEVxIfVP1YTmfBlpziCehfszy7GS9jOvVMFNRqRJP3nBfsnwjc5k51hr3wU6zAkIcm_diihJjCk5tnHPhH8YF-gro83biK6bhRKXtBE-6Nj_c9mwaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:  «اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم»…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/news_hut/65096" target="_blank">📅 23:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65095">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اتاق اصناف: از این به بعد فروش سیگار نخی ممنوعه
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65095" target="_blank">📅 22:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65094">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n15wUeUDB0G5oEjP03l0YEuSsAXNihXqnIjUQYmRJxHpbpL_NCW8oDjYVctY3bVcNJNTetXKCYcVto21GPjluI7F2tVum7eIkuOGKIpEJ3dQonDyQKfjD9R8RzOUSxHPDGMbPPGJM0IfEfz1CDUdApcK4CJ4MqSt0MR6Uezv8A3EDsJhTPc1KwrEpy7ZxxvadmGL3_i_x4yfTntxH3aOVKAoC2xE1AMkE8Tg5knvCJzeY3V8xWdjkSCIluqkotGBQ_7Rr2zhk-_aN7M3PwUkL2BT1WWGRUsmySBZ_YnrLSv8H7CCjCHUpaOMjme8dyP0Vk7vlTQVINxcuUeKNTtI0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: همین الان معاینه 6 ماهه‌ام تموم شد، همه‌چیز کاملا عالی بود از دکترها و کادر فوق‌العاده مرکز پزشکی نظامی والتر رید تشکر می‌کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65094" target="_blank">📅 22:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65089">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نت خونگی.npvt</div>
  <div class="tg-doc-extra">9.3 KB</div>
</div>
<a href="https://t.me/news_hut/65089" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
🚨
🚨
کانفیگ‌ها و سرور هایی که بصورت منطقی براتون وصله
،
در صورت عدم اتصال می‌تونید گوشیتون رو بزارید رو حالت هواپیما و بعدا امتحان کنید
.
🌐
‌ ‌
لینک دانلود NPV با نت ملی
🛒
‌ ‌
لینک دانلود مستقیم برنامه از گوگلپلی
🛒
‌ ‌
لینک دانلود مستقیم برای آیفون - 𝐍𝐩𝐯 𝐓𝐮𝐧𝐧𝐞𝐥
🚨
🚨
🚨
تعدادی از کانفیگ های V2RAY متصل منطقه‌ای؛ یکبار کلیک کنید همه رو کپی کنید.
vless://392c0d0a-157f-4fe0-b528-11586477cbe0@185.213.165.81:38024?security=none&encryption=none&headerType=none&type=tcp#%40HutNewsPlus%20VPN
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.16.80.73:2096?path=%2F%3FTelegram%25F0%259F%2587%25A8%25F0%259F%258%D8%B97%25B3%2540WangCai2%3D&security=tls&encryption=none&insecure=1&host=sni.jpmj.dev&type=ws&allowInsecure=1&sni=sni.jpmj.dev#%40HutNewsPlus%20VPN
vless://e0a98968-eb18-417a-87e7-c8933aac5f13@31.59.40.53:52729?security=none&encryption=none&headerType=none&type=tcp#%40HutNewsPlus%20VPN
🚨
🚨
🚨
پروکسی‌های متصل منطقه‌ای با نت مخابرات:
https://t.me/proxy?server=62.3.12.2&port=8444&secret=ee6f7a6f6e2e7275f22c5421fa893965
https://t.me/proxy?server=91.107.169.174&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=176.65.128.238&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=195.254.165.4&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=5.75.248.201&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=87.248.129.5&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
@HutNewsPlus</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65089" target="_blank">📅 22:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65088">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVfm_cLQwPRI6aNg5NeniCyJNfAY9XAdtNqay0w9m2bctGP3IIj92niS2P_ZaUUWT54IhckDpoVqMq6VthcNxIFB1skZJ7YVBaDoIEvyrQEfRhI_iP9DmOxyMr14lPmrkqvS3vmWS6gJEqAanI4GdkDZQGoaWltfPy_EKdeykukUYWEOZRSd4_9200dGOF2bQDIRUykLfqA-7DMaKDkDVUAoAgmZK9QWgP5kfspA8Jp57tsxRWVA8FYpzs_M_JSw2GfQkmsuvOZVxrcGDWlSFOzw6zVEAgsgHdQ7PUQMmkW0wYYp2IRQ9SN2t5rQ9YJr9r-560Pqb_32iK3jJGB7rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد عوده، فرمانده ارشد حماس، توسط اسرائیل ترور شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65088" target="_blank">📅 22:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65087">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEsteghlalPage</strong></div>
<div class="tg-text">Barko VPN_v2.0.apk</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65087" target="_blank">📅 22:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65086">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEsteghlalPage</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.0.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/news_hut/65086" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🤖
فیلترشکن :
🟣
Barko Vpn
🟣
v2.0
(20260108)
🔹
🔹
🔹
🔹
🔹
🔹
🔹
📝
مشخصات :
🟡
بدون قطعی 100% پرسرعت
🟡
برای تمامی اینترنت‌ها
🟡
مناسب شبکه‌های اجتماعی
🟡
اتصال خودکار
🔹
🔹
🔹
🔹
🔹
🔹
🔹
✅
تست شده و متصل !</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65086" target="_blank">📅 22:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65085">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نت بلاکس: دسترسی به نت تو ایران به ۸۶ درصد رسید، اینترنت همچنان فیلتره ولی امکان دور زدنش فراهم شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65085" target="_blank">📅 21:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65084">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a691fae5a5.mp4?token=USW9JlL4XI0rBtcNHW74sWd0irthd9m3mSZPxA9nKjvbamci-uqyOULGCSU7siNZZCI2eFb4d5L0PfEO9RWCZW4t6t3vLcWLgH4yARK_myA9eiYmDd5Q_mXnVCAlmACUBWJlKeTKUeFC699aS_c0-5EmYAmY7__EEpRkqyeEegDjynDLLK9cH2TfLW3OsVBY3cCTBmkzOwtbaSrC3HZj0E1oidYrQ7hVV-jnaLFqOBvJh-p9CwE7s6Y_vXDLlHPldCbaj3Mo7Ra5bFfq8P94bFZkxCzhkMdSOLoTYJw1s57gQo1xa6wgKe4sUQEhuqkwSGM6p8BGXq2BSnaoAKvjlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a691fae5a5.mp4?token=USW9JlL4XI0rBtcNHW74sWd0irthd9m3mSZPxA9nKjvbamci-uqyOULGCSU7siNZZCI2eFb4d5L0PfEO9RWCZW4t6t3vLcWLgH4yARK_myA9eiYmDd5Q_mXnVCAlmACUBWJlKeTKUeFC699aS_c0-5EmYAmY7__EEpRkqyeEegDjynDLLK9cH2TfLW3OsVBY3cCTBmkzOwtbaSrC3HZj0E1oidYrQ7hVV-jnaLFqOBvJh-p9CwE7s6Y_vXDLlHPldCbaj3Mo7Ra5bFfq8P94bFZkxCzhkMdSOLoTYJw1s57gQo1xa6wgKe4sUQEhuqkwSGM6p8BGXq2BSnaoAKvjlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کم‌کم تمامی vpn های رایگان دارند وصل می‌شن  @News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65084" target="_blank">📅 17:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65083">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFudo.</strong></div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/65083" target="_blank">📅 17:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65082">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کم‌کم تمامی vpn های رایگان دارند وصل می‌شن
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65082" target="_blank">📅 17:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65081">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMKPX</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFpDlg44GPFtPU-vKGLZawv_hQyv-FkTMZwvkEbSKOWS0jUnVZsOR3ydCLtmMqPSBzYT1K5It1R2hS5k7EALguGQp5B02O7mDoJI5Nuq3H6861MBWm2C1XxVNZN8gm_UHELVLYQfZtB5XTDhtED5Z_n9zt18twB1a33gEoOi-wAaA91-C02OcjUwWtvjpt1nX5bqu2MYzzYz1yg1LBoCxis8cfPvQfzcePZs8X6ypor9lqHgtQMZ-IukOPNCCqpoymUdkQN-cvae4S2hDR1TDu_fkmy4_7b_VsK1u77Oi25te4pHZ1jJ4eV4qp98GGXLjrVskgf6awOKpjz4GlOT3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65081" target="_blank">📅 17:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65080">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMmdi</strong></div>
<div class="tg-text">درود
کسانی که نت مودم دارن میتونن با jump jump به اینترنت وصل بشن
ما هم بعد از سه ماه قطعی به جهان برگشیتم
بر باعث و بانیش لعنت
به امید آزادی ایران جونمون
❤️</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65080" target="_blank">📅 17:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65079">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.  @News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65079" target="_blank">📅 17:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65078">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIYtum1Pn_ljFeBvwKOOjrw13DqbzA6_Lk9lCy2b8kL9vkZmmTJENi8Rahs_OqofdtuP66edyi9LVWmratZDNhkc5iDIyxSIlLnun7Mkx40yMJFZhw5OS1n6kOaU7A_6RbWu0p0zIul9veUMxjReC7xBHEppaVv7upijmeyNK6VnRJPjhA2kDhTLptAtn2UrheYE_Z5ox3C5JsWoADiPLCUDI0yOmNcJhKxnKLOKJ1SqtF0Hb5_dM94QWizG8W_j4Ilgf8GzqXKyTameUBG0vJUbPX2lDLZZmiVNlrI9eVZEOYcw5Os8CuZRzYNtcS6wNdbTReGh-H1E_579rKis7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65078" target="_blank">📅 17:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65077">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‼️
خبرگزاری انتخاب: ۴ شاکی حقیقی رفتن شکایت کردن و با دستور لغو مصوبه بازگشایی نت باعث توقف اتصال مردم به اینترنت بین‌الملل شدن.   این چهار حروم‌لقمه عبارتند از: رضا تقی پور، نماینده مجلس کامیار ثقفی، هیات علمی دانشگاه شهد و عضو شورای عالی فضای مجازی رسول جلیلی،…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65077" target="_blank">📅 14:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65076">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVQQ9Mlsrgjv7xfk9-uuigUxAxiNy0WNdyv4zwiCwNikptVIr8KdcnPU-k65LGaz4TE-KmcFKaMnalfGZWCUzXBjkdy2V0iOBdYUX6nMEu5jUXf1gxQAmlnFGHPUkBbpzZjW3AbUFtI4PuUSQGZJOhL3jY1UgbVcWS3vTupijca8uQesmY7qZUbe6Acuv7GBcL4NQJ4vs-Sk793hcEqUeeHpZBsuk7X9cSZk71DXwo7Dl4xKe5FP6LEqN7HGqt5MKL4F1RaMir8r9eMk8mJIVPUxF6LTSGr5JAVTzXpZ66ijK9B33NLbElILR2vw_buTtjsKn1LC8vE2EwowZc6eUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری انتخاب: ۴ شاکی حقیقی رفتن شکایت کردن و با دستور لغو مصوبه بازگشایی نت باعث توقف اتصال مردم به اینترنت بین‌الملل شدن.
این چهار حروم‌لقمه عبارتند از:
رضا تقی پور، نماینده مجلس
کامیار ثقفی، هیات علمی دانشگاه شهد و عضو شورای عالی فضای مجازی
رسول جلیلی، برادر سعید جلیلی و عضو شورای عالی فضای مجازی
محمد حسن انتظاری، عضو شورای عالی فضای مجازی
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65076" target="_blank">📅 14:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65075">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سخنگو دولت: بازگشایی اینترنت توسط پزشکیان به وزارت ارتباطات ابلاغ شد و امیدواریم تو روزهای آینده باز بشه  @News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65075" target="_blank">📅 13:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65074">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇺🇸
ترامپ:  اورانیوم غنی‌شده (گرد هسته‌ای!) یا فوراً به ایالات متحده تحویل داده می‌شود تا به کشور بازگردانده شده و نابود شود. یا ترجیحا، با همکاری و هماهنگی با جمهوری اسلامی ایران، در همان مکان یا در مکان قابل قبول دیگری، با حضور کمیسیون انرژی اتمی یا معادل…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65074" target="_blank">📅 12:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65073">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee692e46c.mp4?token=aHf92Ssn5_zmLUxUJgJgiwJ3b2G_faY7YXlTT14fUVu_cznWlBull3R9Sf76PearUOYiErr2NsExyyoktb4Cs0vRrJ9qmsxdOEuvrBzhupN8BXYfmw0fg2PtXVqMRhTU9i-4JCaKG_vnGowe7LI-EaCziW_wYp2McKC4c8D_HIjVKlOxgXrS3gtyLimSeiPOHVgx56N3ZdjSvnNVIxlUWnuw49RxhbuE5Us7QoC7LdS233LyYrH_a26QvGDYe3uVL77t8spUeAWX4DfU0o29pM3zeAuQ7q4ESsEMLqKUxcw_JqZQ3M1YwHyoEnzt1J_hOHksCUCMEHnDHzlcWknDKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee692e46c.mp4?token=aHf92Ssn5_zmLUxUJgJgiwJ3b2G_faY7YXlTT14fUVu_cznWlBull3R9Sf76PearUOYiErr2NsExyyoktb4Cs0vRrJ9qmsxdOEuvrBzhupN8BXYfmw0fg2PtXVqMRhTU9i-4JCaKG_vnGowe7LI-EaCziW_wYp2McKC4c8D_HIjVKlOxgXrS3gtyLimSeiPOHVgx56N3ZdjSvnNVIxlUWnuw49RxhbuE5Us7QoC7LdS233LyYrH_a26QvGDYe3uVL77t8spUeAWX4DfU0o29pM3zeAuQ7q4ESsEMLqKUxcw_JqZQ3M1YwHyoEnzt1J_hOHksCUCMEHnDHzlcWknDKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگو دولت: بازگشایی اینترنت توسط پزشکیان به وزارت ارتباطات ابلاغ شد و امیدواریم تو روزهای آینده باز بشه
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65073" target="_blank">📅 11:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65072">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رهبر سوم جمهوری اسلامی: سه چارتا جنگ کردیم همه دشمنان‌مون رو تا ناموس شکست دادیم جوری که ویران و حیران شدن.  @News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65072" target="_blank">📅 11:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65071">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‼️
رهبر سوم جمهوری اسلامی: پدرم، علی خامنه‌ای خلف پیامبر بود و بعثت الهی یافته بود(از طرف خدا مبعوث شده)  @News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65071" target="_blank">📅 11:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65070">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فوووری برای اولین بار رهبر معظم جمهوری اسلامی با سوییچ از فونت لوتوس۱۲ به فونت تیتر ۱۸ در جمع حامیان‌ خودش حضور پیدا کرد  @News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65070" target="_blank">📅 11:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65069">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aTRx_W4S9kYu4PSFST0ACI2DjZd-sE_BXtmST02lOB_p_gJbNyKboiZzWLU9BS8ZjcDBUjDSt_GCkWnUWvftPqu8njJQyIy7IR63qpJ7I4c1Ac6cxaMeU9Otn2YIYxGLJUWrAzNDZNHgkekLBoDOGjAJTpnprL-997CZQN25hfGk-_66JKMJxwyeJ_BLW3GvnCUBkbomZKd5UXuxu4UZtA6ANfvDZeM_2tVqdfvnZ10wFJTNDQm-YqoFp8EpEPTs_BhsxJo-JB5X6Kj6h2lKszDOIkM0RwIfHcH-M9qNTnGz_wIKwt8jgMjLsECcnKJHQPCy55t26bwM6WeKCA6hzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوووری برای اولین بار رهبر معظم جمهوری اسلامی با سوییچ از فونت لوتوس۱۲ به فونت تیتر ۱۸ در جمع حامیان‌ خودش حضور پیدا کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65069" target="_blank">📅 10:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65068">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mOOIPXDHZWzHu-L3WILIrU8GJnCjzzufmXh-aXrA5i_otktij8RsTojQqYjpDFTX7vj29qPoq_eQpUsqZliMr10gMRZxIb3-Aq2VKA274bN8QKaKvjfsOS-axwTpKGX-6KiMObwIsJ4qsFnHp2zCqEwlPqkbkQYKvwl5QFGTEzci07DVdX4bKWXghL3wjC4TweZPMHh3SvnwCEj72Dje_ASWSEr4hq5HyFAIs3m8bTsmDYyRETHLWCo_roNm9QidXHyZqy7YsaPxMACo4d3kWc5dowYh1yQS8LtplIdj3Mv5n9eA0vf9ZOK3RcWqq65rjtzdo1OhyFyinvv5gVi4xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:  اورانیوم غنی‌شده (گرد هسته‌ای!) یا فوراً به ایالات متحده تحویل داده می‌شود تا به کشور بازگردانده شده و نابود شود. یا ترجیحا، با همکاری و هماهنگی با جمهوری اسلامی ایران، در همان مکان یا در مکان قابل قبول دیگری، با حضور کمیسیون انرژی اتمی یا معادل…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65068" target="_blank">📅 08:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65067">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AW2EQXXvdahuDbVa8iZ8xIriYi0NT2XaFLoze3zcAeJC_sivmlbEVl99VQ-B8RR3M4zGSovyp3Z540JxOoqSPK4GWxkOnG6GdKq9cRDecpGc8eLgTlyImAdQqWAsNXL9Ux5wdMzQZA-Bo0OzE9ds2WvSat69O_r8AmlHE48SZK-bto81aKQeCTG2uzrhvz_2Y8Y98dHo94B3L9T2Ql8j9zb6U9REzcBpcbw-VxuiHz9phzUMBcxuhWK4MQs8vGfBZYkXBkWNNqt2xnvbMGQqNAMQ_dJevNnIxK2POuBN5ucCjtSJNydWxu5VnjZPiEhIIYAFeemVnCpqz49TWf_W1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شنیده شدن ۴ انفجار در بندرعباس و شهرهای جنوبی سیریک و جاسک  @News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65067" target="_blank">📅 01:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65066">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">صابرین‌نیوز: امریکا دو قایق تندرو سپاه رو با جنگنده زده و ۴ نفر هم کشته شدن</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65066" target="_blank">📅 01:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65065">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vevyWLIxTR2MVX-c_O7_iiZEvgWu-gE47k_Vq8a_7iMPSziPvydUr5koKrAGf4D4WlyRs-IMlEKTnwZV4odErt7MmAiGcYlqvtB0dyhOy5aORJ_Gp7drZZKHksVIb6SGXO-6xaZslnNcy6LuKQB6Y1Ik0u-PoEtTbfPnt9uYgU8T8tgmgPmXbQRzcoBsJkhB2xydMJocels5iIN-b7D2lCijNJ22LG97hHBPKeTlNTtLTRkM8V0i7n4fCBooz9s0M1Z1dmAa2vXrZ6zBuxhjFLyGTiiEbEngSNHjnt1YlE4wJ87b7mz5DWDwB9pvKqM8twAOTeKGFupdnrtmLfvWkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
اورانیوم غنی‌شده (گرد هسته‌ای!) یا فوراً به ایالات متحده تحویل داده می‌شود تا به کشور بازگردانده شده و نابود شود.
یا ترجیحا، با همکاری و هماهنگی با جمهوری اسلامی ایران، در همان مکان یا در مکان قابل قبول دیگری، با حضور کمیسیون انرژی اتمی یا معادل آن، این فرآیند و رویداد نابود شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65065" target="_blank">📅 01:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65064">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
شنیده شدن ۴ انفجار در بندرعباس و شهرهای جنوبی سیریک و جاسک  @News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65064" target="_blank">📅 01:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65063">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFY9hxnBOs1OkIlhYjcCg1VJIg-Ee0FSYt4pdkWvQXdNt1OINsBu4Ns47VvwRc2zWc6d4PbB2GnJkAP14MUGb-uSZIi4rDyHiEtMTQsNFYPLyTgPXDx-u39v9nkZOopoJekLVaLpOFOKUHYQXzmck5YM4DUrkaKfrKPI3HCYriuwdx2XjfIYtjsaEVjJbylPYrVDagc4vBTsmaAroehhyyjUIc7v0wiXrIGL7rHIYwZTzNbVAGYR3wUMUg1DshTYs66AqVuIzo8Bd3_YqOiFV0hTak2XXz_XS3v_01bzcWuYEk9bYpaajbd3d_7ZEyubhY4dKnM74CTao84Yi6dKqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری تایید نشده مربوط به انفجار لحظاتی پیش در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65063" target="_blank">📅 00:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65062">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
شنیده شدن ۴ انفجار در بندرعباس و شهرهای جنوبی سیریک و جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65062" target="_blank">📅 00:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65061">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
📰
آمیت سگال، خبرنگار شبکه 12 اسرائیل:  ایران در حال حاضر فقط حاضر شده به توسعه سلاح‌های هسته‌ای رو متوقف کنه، در حالی که ایالات متحده چندین گزینه برای ذخایر اورانیوم غنی‌شده ایران پیشنهاد می‌دهد، از جمله فروش آن به ایالات متحده، انتقال آن به یک کشور ثالث یا…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65061" target="_blank">📅 21:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65060">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">به صورت قانونی، ما یه "شورای عالی امنیت ملی" داریم که به "شورای عالی فضای مجازی" دستور میده که به بقیه اپراتورها بگه که اینترنت رو ببندن. به صورت غیرقانونی هم سپاه رو داریم که زنگ میزنه میگه اینترنت رو ببندن. زورش میرسه، میکنه! حالا دولت رفته یه "ستاد راهبری…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65060" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65059">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
ترامپ: من به صورت الزامی از کشورهای خاورمیانه درخواست کردم که پیمان ابراهیم را سریعا اما کنند تا «جمهوری اسلامی ایران» را در ازای بخشی از توافق پیمان ابراهیم داشته باشند  @News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65059" target="_blank">📅 19:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65058">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
ترامپ: توافق با جمهوری اسلامی ایران!! به خوبی درحال پیشرفته این یا توافقی بزرگ برای همه هست یا بازگشت به جنگ بسیار بزرگتر.  @News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65058" target="_blank">📅 19:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65057">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🇺🇸
تروث طولانی و مفصل ترامپ درباره توافق با ج‌ا و پیمان ابراهیم:  مذاکرات با جمهوری اسلامی ایران به خوبی در حال پیشرفت است! این موضوع تنها یک توافق بزرگ برای همه خواهد بود یا اصلا توافقی صورت نخواهد گرفت؛ بازگشت به میدان نبرد و شلیک، اما بزرگتر از قبل و هیچکس…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65057" target="_blank">📅 19:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65056">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‼️
فارس: همتی، رئیس بانک مرکزی برای بررسی و گفت‌وگو در مورد آزادسازی ۱۲ میلیارد دلار پول بلوکه شده تو قطر به دوحه سفر کرد @News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65056" target="_blank">📅 19:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65055">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyOfiPIwShSoMIZmPPvqn4StD08Wfe0y4spB46cVJPJngIrNl5lOdPkImxTozZ0IdC6hHxD7l9EdI34gHDBRiHWDbGihcbBkc5s093HbXI1jjk14PVBxBaRqQcHwgj2s8k36Mi8DFvTxECiUM_JIYqheubVAymKKX18-fQhVNp2DIjfhw4EOHICRxtOdQEvaJ_F-fkJ_9rheAX_BolRMrc4bj4ywsY-bxSmXvjmeDQ2XvwCgfkdeKNiJ55UMDjUrkcz8Mj9qOH25nLEhPqtEf3wi1IaV0Y5wX8qQvp_GBoSOpiVFkNbR3vHN37elDm_gMTT5TfxkfqNsCwHVk8ytIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی گفته یا اموال بلوکه شده تو قطر رو آزاد کنید یا حتی یک گام هم در راستای توافق بر نمی‌داریم  در واقع الان دست بالا با جمهوری اسلامیه نه ترامپ! اینطوریه که می‌گن می‌خوای حمله کنی؟ خب حمله کن ۴۰ روز کردی مگه ما چیزیمون شد؟! #hjAly  @News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65055" target="_blank">📅 18:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65054">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">جمهوری اسلامی گفته یا اموال بلوکه شده تو قطر رو آزاد کنید یا حتی یک گام هم در راستای توافق بر نمی‌داریم
در واقع الان دست بالا با جمهوری اسلامیه نه ترامپ! اینطوریه که می‌گن می‌خوای حمله کنی؟ خب حمله کن ۴۰ روز کردی مگه ما چیزیمون شد؟!
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65054" target="_blank">📅 17:59 · 04 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
