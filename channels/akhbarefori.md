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
<img src="https://cdn4.telesco.pe/file/SO-jp_AnMUkUBJiEIUtyrPBL3SICCV6L8EjpuJG5g9JpdV0paAhdXoek4AS8c8VUIZsY-lli-xqShMGmJK8o6JAbRi5IVn_rKW-vYeHLJe9qETyDVqEBI6ppUq2mO3KE1v2_R2CKn85b3xH6t-LsTHrP9bxpe4LlrN3GTExkZGE7iqOzk_eNbxEgeNmY5OLsldXOd3VjVG_sklmCLEeVtQp3hs6MFAIiPv_sssfavcUVZ-0D868d5Yek5wQAsimK5JzlB0WoK-O4ihd2NuQ93Zz1R7Xa9SymPcPu9x1QRAF5Dc5WdCzFDYRfmq7_X0vnhlrZWUZQDZGRy_HmqmcXGA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.08M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 13:01:52</div>
<hr>

<div class="tg-post" id="msg-677679">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d5ffc4c3.mp4?token=fqJrlXOo6sywgULF9i25AEvJ4u7z97tremdOdZG_Vo6KqYttiFcPV4Tx5fA0M-3eGKkOGhhVzpbrJ3CQeuYdN2_SXS9ZLKN4Mo9M2wZLrJ2x-UDnsFc4qIWdAcKZCx3qlmsUCa2qwM_vWqoxgFmjvr0NCjolBnRA_2NBTbfOCpEu9BN86xfQ-vxBJwP2oevvBJxa3Y9T02Ea21LMhJc71lgE-YSJQp8goz2e5sMryMV_m53IdIwYGHxHt_pj7Hd6pUk_8LX2XzWo18nADBhoVoYzdOzePacdGwXt73tvGPxKEtpMrtdIShNYmZFyZNsOSpPoumiPmdeVS5G6tjb28w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d5ffc4c3.mp4?token=fqJrlXOo6sywgULF9i25AEvJ4u7z97tremdOdZG_Vo6KqYttiFcPV4Tx5fA0M-3eGKkOGhhVzpbrJ3CQeuYdN2_SXS9ZLKN4Mo9M2wZLrJ2x-UDnsFc4qIWdAcKZCx3qlmsUCa2qwM_vWqoxgFmjvr0NCjolBnRA_2NBTbfOCpEu9BN86xfQ-vxBJwP2oevvBJxa3Y9T02Ea21LMhJc71lgE-YSJQp8goz2e5sMryMV_m53IdIwYGHxHt_pj7Hd6pUk_8LX2XzWo18nADBhoVoYzdOzePacdGwXt73tvGPxKEtpMrtdIShNYmZFyZNsOSpPoumiPmdeVS5G6tjb28w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهیدی که بجای سردار رادان در جلسه شورای دفاع شرکت کرد
🔹
سرلشگر شهید «غلامرضا رضاییان» رئیس سازمان اطلاعات فراجا ملقب به «ابوسجاد» که به جای سردار رادان فرمانده کل انتظامی در جلسه شورای دفاع نهم اسفندماه شرکت کرد و به شهادت رسید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/akhbarefori/677679" target="_blank">📅 13:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677678">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3a26eaf0d.mp4?token=iLh2oHWgmTUraT1Sq6p5G1dnvexGybNeunRGF1PGVgjOiYTDKyKXwueZfB36U0hmHDb_UTZM7Kv5F25CNd5BrRTQNsGU20F0X8fsqQSSFBa4XMKqcMHeYG7_meeY4-jhfbu6kJ_2LEZP_ujfgn_WuW6B39PxK3-b1znzG_1N1ci1H8tKp8RUbgMTI_31vLl_XEuHRXwwIQKtfwKXZHFfHC1zAOXTVZyNNCLh5-qiMPYjrdHFMQtHREGwq_VDbxOICwuAAd1LNccZo7g_M1m1-sZtBOJ8r9ETpxc9Q_R-V54uisVFbFGTsEYEL-e5ca5Xnxx19aWKCOcUWHLD4gaVTWrKwnkirT_8AgugLVbQtt-XldHEW-kyteI8dTDL3txQwT8I1VXo9aFF2-Q-Az8T0XTN91CQl98tUFCCTqBmax-95waiQYD3dJS9RvOdPgtNNWi8pm7hs1qlTmFeBDNqGAN5w0hxB6AQ4Pppx8-AMN1Mylru0JEOGnD-_9fXycWT8ST4qN4HfZpDZLS-h4dmv-e7Qaarsbj5A0LSZ993W5kxUuNDZSxqQzL0cpho_4NCwELnYhTt3kMnCgmpepTdj0L6nN5NmtITjUvVxbEHPVRsY5BnLkaiihblysWu9Ig6MWJgttziymyqAQf5c781MxyV9MaqbAS4GFHjKWRxI90" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3a26eaf0d.mp4?token=iLh2oHWgmTUraT1Sq6p5G1dnvexGybNeunRGF1PGVgjOiYTDKyKXwueZfB36U0hmHDb_UTZM7Kv5F25CNd5BrRTQNsGU20F0X8fsqQSSFBa4XMKqcMHeYG7_meeY4-jhfbu6kJ_2LEZP_ujfgn_WuW6B39PxK3-b1znzG_1N1ci1H8tKp8RUbgMTI_31vLl_XEuHRXwwIQKtfwKXZHFfHC1zAOXTVZyNNCLh5-qiMPYjrdHFMQtHREGwq_VDbxOICwuAAd1LNccZo7g_M1m1-sZtBOJ8r9ETpxc9Q_R-V54uisVFbFGTsEYEL-e5ca5Xnxx19aWKCOcUWHLD4gaVTWrKwnkirT_8AgugLVbQtt-XldHEW-kyteI8dTDL3txQwT8I1VXo9aFF2-Q-Az8T0XTN91CQl98tUFCCTqBmax-95waiQYD3dJS9RvOdPgtNNWi8pm7hs1qlTmFeBDNqGAN5w0hxB6AQ4Pppx8-AMN1Mylru0JEOGnD-_9fXycWT8ST4qN4HfZpDZLS-h4dmv-e7Qaarsbj5A0LSZ993W5kxUuNDZSxqQzL0cpho_4NCwELnYhTt3kMnCgmpepTdj0L6nN5NmtITjUvVxbEHPVRsY5BnLkaiihblysWu9Ig6MWJgttziymyqAQf5c781MxyV9MaqbAS4GFHjKWRxI90" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اربعین، سفر همدلی و همراهی است
🔹
با رعایت نوبت، صبوری و همکاری با نیروهای خدمت‌رسان، می‌توانیم بازگشت زائران را سریع‌تر، منظم‌تر و ایمن‌تر کنیم.
🔹
چند دقیقه صبر، سهم شما در خدمت‌رسانی به میلیون‌ها زائر است.
↗️
ما را در
cheshmberahim.ir
دنبال کنید
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده‌ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/akhbarefori/677678" target="_blank">📅 13:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677677">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCVhmMQM1j6ArFx6LZhnbLMa-_aBb1nIEke2-bXoA8FMrU0gwo9kE4iE2qcuZKMKUqCNZsi4gHzygjR5JARY_iP6z53IcSKoALEqyxHiyDHrFPh8694FV1sxc7NpWpPRTXMixcQfi_asouiMVE3sOGKpm66Ibv4XJuVfYsMGdYzUCuziwpp5kqfMSQMiRiHPd9mbhP6MMEoShhLvIV6bBo1J8-7KVc1kiiIppS3bb-x4jXmTbyIqawBIo7ndb1AsSQ8N8rLXWZ2ASsONKY7IMY-TQosrEN7swsG9ZjDbGU--2k8PtqA8O-RN5DRdZuqSm2R5u7mbF0bamKIFbUVthQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ژورنال امنیت ملی: ترامپ می‌تواند هرچقدر که بخواهد بمب بریزد، اما نمی‌تواند تنگه هرمز را با بمباران باز کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/akhbarefori/677677" target="_blank">📅 12:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677676">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36ba8b111b.mp4?token=sqWttwMtUIMmNK37_jtFmnjYu5XEqp5xsigB-8R4hTwCHwWYi2NvJR1VKdTHRVeJTFnPshlj0hd91U9_MeLcH0X0qr3Ga1zXUsnJ10lsf7eUcspf-ovFp3q4Um6g82AYHKx9Y8E9aIgxasqdCSOGODzfCsp3SXYc7M6B6ZcAcW8buL4GKOYmeU3bgysQz27VDOPhqV-kItL1lt7rt37x88VL51X18i6hlZ5qabOnO5OEFF0yucqjCEikZWI4ypE_7wKJrDW3zn1tGnVsh01bwEykKyuiW7ozSNwI2vTcoZPx3Ij5dcaa_RumLPwh8B6brDhdQ1Xe3_JeHMKR7hEfsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36ba8b111b.mp4?token=sqWttwMtUIMmNK37_jtFmnjYu5XEqp5xsigB-8R4hTwCHwWYi2NvJR1VKdTHRVeJTFnPshlj0hd91U9_MeLcH0X0qr3Ga1zXUsnJ10lsf7eUcspf-ovFp3q4Um6g82AYHKx9Y8E9aIgxasqdCSOGODzfCsp3SXYc7M6B6ZcAcW8buL4GKOYmeU3bgysQz27VDOPhqV-kItL1lt7rt37x88VL51X18i6hlZ5qabOnO5OEFF0yucqjCEikZWI4ypE_7wKJrDW3zn1tGnVsh01bwEykKyuiW7ozSNwI2vTcoZPx3Ij5dcaa_RumLPwh8B6brDhdQ1Xe3_JeHMKR7hEfsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایتی از شاهکار به یاد ماندنی اکبر عبدی در فیلم مادر
🔹
همه در پشت صحنه گریه کردند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/akhbarefori/677676" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677675">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
فارس: طرح بازگشایی تنگه هرمز کذب است
🔹
یک منبع نزدیک به تیم مذاکره‌کننده هسته‌ای، ادعاهای مطرح‌شده درباره موافقت ایران با بازگشایی تنگه هرمز را تکذیب کرد و گفت: «جمهوری اسلامی ایران هیچ توافقی درباره بازگشایی تنگه هرمز نداشته و اخبار منتشرشده در این باره کذب است.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/akhbarefori/677675" target="_blank">📅 12:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677674">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
مرکز آمار ایران: جمعیت از ۸۷ میلیون نفر عبور کرد/ ۱۲۸ هزار تولد تا رسیدن به پیش‌بینی امسال
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/akhbarefori/677674" target="_blank">📅 12:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677673">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WT37U0SThntggd7zaTU7sSGm0POYNLWv7qEVTsGyQpxDDFngci5Ochcf67vp0ZbS7DtkTLAzYZNU4Q2JPztLPToaG7cHnXU5EKt2w5ayuKpcPUd0-r-fDk-Ym40wzPjpiIIpIGKHJgOdpk6rC2lFXBDFtABMumGrTZUh0SwJlAVQQq6xjH7usOnw-clKPB5MU74lpiS0O2DTu6IBZYQRcFD8M5AtTwh5j-lQlW9KTAWYqQ5b0ztndmXv7X6T6-lTP-4D6YA8dpZKWPDd4hEQqMzw0HWhMJ_uGTaYLROGqKkXesZylajnhVRs9TUL377AyCQQ1PGHdBAABIPFIxFICg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جهش ۹۹ هزار واحدی بورس
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۹۹ هزار واحدی به ۵ میلیون و ۱۵۴ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/akhbarefori/677673" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677672">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22124f4ef.mp4?token=JgzbStbt7G-JxfHvzL_gDEw9gE-DFld2dy3RBlx86kZ7vlgr55XrxLtQgvY3AdGc1GxQk_t9IytTfh8pcesdxm_Nf36zfSO-Mv6d2q6EiD0lKgm-KuHavQ3WiXUj_BD5WLiZ_iEArTTJ18e0p2vZx89ccdcs2exkWU8oMfFzosZsBjuhRkZm0G_agePrv7uFueIf8D76wfnOCwHMs2HCo0wimXUQyV4pdF5rlHLFUcqErdFitHv2_B5Z5la7oYZwGH6_ZajlgobrtP564s3ayzjXMH8I58gN9bMz0dxVvEQF9kHaVWINOZuKAjjHGodxC8bPwh3i6a_6gEaGE5vpkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22124f4ef.mp4?token=JgzbStbt7G-JxfHvzL_gDEw9gE-DFld2dy3RBlx86kZ7vlgr55XrxLtQgvY3AdGc1GxQk_t9IytTfh8pcesdxm_Nf36zfSO-Mv6d2q6EiD0lKgm-KuHavQ3WiXUj_BD5WLiZ_iEArTTJ18e0p2vZx89ccdcs2exkWU8oMfFzosZsBjuhRkZm0G_agePrv7uFueIf8D76wfnOCwHMs2HCo0wimXUQyV4pdF5rlHLFUcqErdFitHv2_B5Z5la7oYZwGH6_ZajlgobrtP564s3ayzjXMH8I58gN9bMz0dxVvEQF9kHaVWINOZuKAjjHGodxC8bPwh3i6a_6gEaGE5vpkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«راویان پرچم سرخ» روایت اربعین را به شبکه سه می‌آورد
🔹
مستند «راویان پرچم سرخ» با محوریت سفر کاروان اهالی هنر و رسانه به پیاده‌روی اربعین، امروز روی آنتن شبکه سه سیما می‌رود.
🔹
این مستند امروز ساعت ۱۶:۳۰ پخش خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/akhbarefori/677672" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677671">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تخلف در تصحیح اوراق امتحانات نهایی تکذیب شد
ابوالحسن مصطفوی، عضو کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
هیچ تخلفی در روند تصحیح اوراق امتحانات نهایی صورت نگرفته و گزارش نشده است. بعضی تخلفات که در فضای مجازی اعلام شده شایعه است و صحت ندارد و اگر کسی مدعی چنین موضوعی است سند ارائه کند تا پیگیری کنیم.
🔹
سطح سوالات امتحان نهایی دانش‌آموزان استان‌های جنوبی هم‌سطح سایر دانش آموزان بود و تفاوتی وجود نداشت.
@Tv_Fori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/677671" target="_blank">📅 12:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677668">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eh_OVCDlTuxRpUSslM9Gl9SwTIXPLEtiYf77EnQIwszT0Z_SALI77K5g6VlGFbSy7fMXar2q4fzuA0oQhDxQS5WyAn6qwkWp2KaEyc_1iSGKbQC4YDJ7pYl9w_dbGa1oTJt_aWCLVamaTgxCduoGUlZC3m9EYbnm9MOeDtzcatBo0GxETyuH3zuSqZDr6R43v1KefkfyDtM2_87sc1ubnzEKBJDMuPzLT3HVRx_G5AmbU9iRgjf4I_m7WovfUyJixppZNY91GEjLh6oheIhF8Gk5jXUewGJOemoP8_iA10IYLrbChvb4w2BrkgehuYbGxcp2j_n82eNAGPB1T6bibg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQe9eBW0UNpK9Yip9HlezMwrnmGSOJIZCFVidh-kLA_V4ZmIb7RxqJFnN9oSYX5JfVwashOef84sa4kqRzJs9INYZhX-GmFjxQ3ulRclnUm-zuc5Ew1tKp1O2In-LJEvqEMZfSpmqLPkLRdLxxVuJy-Ys9agKO-G3d9rcOxEjIhvV37e4DR3Vzzx4n0hn97d5mNxYijQbih6CqJrdmu7eXVZauPEbJr6PT1_xjgFR-XhpphfpIJQNRmM56sWZ6278hE0ewNqnPXqQXyXJZXsIzovZJ1keTtDZngwWLGftC7aRUAw2PHdVHoBPiSROgWKBdZf6jkArmWJ9bPLQvU1Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VuFidJq4bYRveP0vJN8Tkomy-i97A-uLmp7CXvJ9vCSWLSrlkpp2VuWlARuML_sjF7xFK4E0EzsH10c0x2y_WTjMcIMZEjuMmzdxmy2Q-Mc0dI1_iunM8v4rAqqYhvgBQ4h9qaSMyIQxxyVpLDKbDGBw8Ab9U507JDQreWjQIXmn8BLgCfwSqQ_IPubm3ntdJZlG64t7BpUnyp7dOmZYCZIaLLUsEg11zOFjcTXtu-7-nOf-qO_6NY_8Nxy-XaXVPkH1d4qKzHJgDenOpY-IdRO0g_-Mognj5K_MzKckaH6vM5DTkx4RbT-l9H4PAuUbdy_l6hOjdtOwGAOy3vN0Ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
استایل خیابانی نوید محمدزاده خارج از ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/677668" target="_blank">📅 12:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677667">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
نیکزاد: افزایش قیمت بنزین منتفی است  نایب رئیس مجلس:
🔹
رئیس سازمان برنامه و بودجه درباره بنزین گفت که ۲ راه بیشتر وجود ندارد؛ یا سهمیه بنزین جابجا شود یا اینکه قیمت افزایش پیدا کند.
🔹
طبق توضیحات آقای پورمحمدی افزایش قیمت بنزین منتفی است و جابجایی سهمیه انجام…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/677667" target="_blank">📅 12:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677666">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
اوکراین: یک پالایشگاه نفت و یک پایگاه هوایی در استان ساراتوف در جنوب غربی روسیه را هدف قرار دادیم.
🔹
هاآرتص: ترامپ به مهارت خود در معامله‌گری افتخار می‌کند، اما در نهایت متخصص حرف‌های تو خالی است.
🔹
رئیس پلیس آگاهی فراجا: آمار سرقت در مرزها به حداقل ممکن رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/677666" target="_blank">📅 12:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677665">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
دولت پیگیر صدور «گواهینامه موتورسواری زنان»
سخنگوی دولت:
🔹
فرآیند کار برای صدور «گواهینامه موتورسیکلت زنان» در حال طی شدن است
🔹
اتود اولیه گواهینامه آماده شده است، اما آنچه برای متقاضیان اهمیت دارد، نمونه اولیه نیست
🔹
وقتی زنان با موتورسیکلت تردد می‌کنند اگر گواهینامه نداشته باشند، به نوعی برای جامعه و دستگاه قضایی بار ایجاد می‌شود. به همین دلیل، دولت پیگیر این موضوع است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/677665" target="_blank">📅 12:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677663">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgeNEhmMlDli--H1rr2mYyIBA3HDIQAdU-qViGYWKSSIQgNqpHR9l9tAQgbolL2OQf34g8hhDgbzMpsNfDJE2e_AM7V_Z9t5IDb4tgQqzj_Ue_LaLqIjZKkW3ErW8iRYp4k2dV1ser39YO_5YbTXvuM93xXVWMjjaKZOpG1WLybytI-lVAHEfi35tS6lPfd0c3Z_TnGhhIyGBJ9AF2Wg9ZIBMTTVvKgXjCY_S59nwm3IdyfXLFwjbHrtthbFV43oktodks6T0OtIAbQvzFr3QhTjDifi4Z1IlM5Aj5jV6Ma-NckaEhe4XFzcAw99Y6EIH7lbNotzad0X2ElpXFgeSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سپاه چرا مرکز آمازون در بحرین را هدف قرار داد؟
تسنیم:
این مرکز بخشی از زیرساخت رایانش ابری و پردازش داده‌های ارتش آمریکا بود که در تحلیل اطلاعات و پشتیبانی از فرماندهی و کنترل عملیات نقشداشت که هدف قرار دادن آن با هدف کاهش توان اطلاعاتی و عملیاتی آمریکا انجام شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/677663" target="_blank">📅 12:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677662">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80257c9d1b.mp4?token=Bj3SITOJvtYtLUyF45Nk290FbjYs3j-y1Xgl3IT4qNcStKPZwB_kepeDWmoC0qEWysa8fkn83AFUispTknNQqJaXYtqz9JSx8gymyz2tTUoC5egN7j41-y8hnt0r1uZeb7t6RAo6Clneu7esX59H5HdenCYuRjH3puUzdpKWCRT1BnHjdiFjRgUtVVzzpg7-ap-9DOgz-NMbcckTHtlQRtmT5CdoW_ubr1pZ5pv5c9LMI4j1fTQv3o7VTDUvUlRPebKF_wW9PNfZeS9qbcFozNVCU_YQLhOXK205Lk8DIKBiPrtSS13XIFgTc3T8JNCe75_Y1TfiD92-EilGXwlE8yUqmLpAMG4KbiTPUSOfzHCYWAxosuLIpK8wZRJqMpZDMtmu2KOjQU2yEqspDB5ucYbkFYYtKgzGF2lKkdDRchXFUk7A-3Vc3dqr_qR_5UHq_s2KefuT2xfc9C5j3Fc3nf_H_SGYxN3PUsaxY6pEPqWQm6cbQnlxrJqmYGyzuw-LjZyGc_L9SXMkhiRqdFSuBCz3IfrtXh0BhZzOVDq9rHW0rkGmhX7OucTT_5gcu3EUeHAUGpMPO8_QQSXq_0HTeedj-Qk4zv4PfOCq4yzq4f_OyS4au4LAR7slxTQsyacDX0KPcZuKpc-P72b1pxtaJKczRoie8nB8RfAjIKIkekg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80257c9d1b.mp4?token=Bj3SITOJvtYtLUyF45Nk290FbjYs3j-y1Xgl3IT4qNcStKPZwB_kepeDWmoC0qEWysa8fkn83AFUispTknNQqJaXYtqz9JSx8gymyz2tTUoC5egN7j41-y8hnt0r1uZeb7t6RAo6Clneu7esX59H5HdenCYuRjH3puUzdpKWCRT1BnHjdiFjRgUtVVzzpg7-ap-9DOgz-NMbcckTHtlQRtmT5CdoW_ubr1pZ5pv5c9LMI4j1fTQv3o7VTDUvUlRPebKF_wW9PNfZeS9qbcFozNVCU_YQLhOXK205Lk8DIKBiPrtSS13XIFgTc3T8JNCe75_Y1TfiD92-EilGXwlE8yUqmLpAMG4KbiTPUSOfzHCYWAxosuLIpK8wZRJqMpZDMtmu2KOjQU2yEqspDB5ucYbkFYYtKgzGF2lKkdDRchXFUk7A-3Vc3dqr_qR_5UHq_s2KefuT2xfc9C5j3Fc3nf_H_SGYxN3PUsaxY6pEPqWQm6cbQnlxrJqmYGyzuw-LjZyGc_L9SXMkhiRqdFSuBCz3IfrtXh0BhZzOVDq9rHW0rkGmhX7OucTT_5gcu3EUeHAUGpMPO8_QQSXq_0HTeedj-Qk4zv4PfOCq4yzq4f_OyS4au4LAR7slxTQsyacDX0KPcZuKpc-P72b1pxtaJKczRoie8nB8RfAjIKIkekg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردم در مورد قاچاق برق چه می‌گویند و برق‌آشام‌ها چه کسانی هستند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/677662" target="_blank">📅 12:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677661">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
سایت خبری العهد: هراس آمریکا از اقتدار ایران و پاسخ این کشور به هرگونه تجاوزی نظامی آمریکا، ترامپ را وادار به عقب‌نشینی کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/677661" target="_blank">📅 12:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677659">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30df4735aa.mp4?token=oiES3Ac7uu46jewMBvaM_sBOajmTYuNHDXrw6xSZpCQoTAm2q3WxmirwJBWk2LiNNps670FyXBQ8i3QqcBNRgYeto6DQ8bUd0bBF2wv-Qj-2xT-aw9QrWZpUCapC_U0y4LSmBKMgPd0cU2EssVPRGSzKto3ggA6J3TNCwf6xLfCD-faJ2oQnaxY4Qx2k5LtcPqfulv2G-aMHzfk38MhzscZDTzefvzkH2TFl-ONYhqvOOYS5JkqhhiczMOJZ8ApLEMj6VYLBmTIjFGaX62Z4qpuCXMpuanVVWpNXZaBUigAnspmjCEhFSG9YpUr2cH4ZZCuwlpmn3ssqtokA0bhDAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30df4735aa.mp4?token=oiES3Ac7uu46jewMBvaM_sBOajmTYuNHDXrw6xSZpCQoTAm2q3WxmirwJBWk2LiNNps670FyXBQ8i3QqcBNRgYeto6DQ8bUd0bBF2wv-Qj-2xT-aw9QrWZpUCapC_U0y4LSmBKMgPd0cU2EssVPRGSzKto3ggA6J3TNCwf6xLfCD-faJ2oQnaxY4Qx2k5LtcPqfulv2G-aMHzfk38MhzscZDTzefvzkH2TFl-ONYhqvOOYS5JkqhhiczMOJZ8ApLEMj6VYLBmTIjFGaX62Z4qpuCXMpuanVVWpNXZaBUigAnspmjCEhFSG9YpUr2cH4ZZCuwlpmn3ssqtokA0bhDAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری از پیکر شهید ۲ سالۀ جنایت آمریکا در قشم
🔹
سینا جعفری به‌همراه پدر و مادرش بامداد امروز در حملۀ آمریکای جنایتکار به قشم آسمانی شدند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/677659" target="_blank">📅 12:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677658">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faf0ccaf39.mp4?token=UH_GXNTc440gForAZCxf9KZUQDG07zy54whReIu1A4haNNFDPacCfcdv0T0hLeHSPi7S_pO9KoD2vlatHXdWR2XdJNCzK4Xf_CtU7HVDp7S9q1HFEhSMe5a3kKd7gMO0Qw2gJJRcKxyzLWtnDwN9te6FuUsQP8fm_PnyOZgum1DJP-jdGNFPzUpY7J4eWaqfrJ6VKGL1L3mxSRZN06kcJ_cPJ_bBxG_ouSa_0wU_TJTL8iymNAQEHfT4xaoiXUgOnCifXzrmE07WOf4mHdLtFhqJziC1klAWQwDY9NrXzwZK2jglxLCK7UTe_74NNRJWaihI94XdeVPzoA7g6-htj2hoAgFtrpzUZk7r72D0LNR2Vo9B-tLSUbCdsZ19jfH5DhHaJLMXG_d_tshBfxEvcVGkrcEsdNITYTfld6jSb-S5BOtXN7zQUzVuIBmcLhDyY-fGlqyApn4p687Xgv9628e46Ck7VUYUzNrwYDxuhOqsBpqVsW-2XOzvHhC8uX7CnMa987b6HgOZ8SyLBSRgeIFWEj_fN9owLvxjQCPKPVfd7IFvMykMhg86aMdyJ2eWcxxnvNHtG6NWBEhFx--4GyC-dEpInANDH8q482H2MU9Cly-gPklev1nd1uS7LCXjEr7lWDpDt5n6H_rnDXZqmJpGf3_9g93j2fUH-aNBStw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faf0ccaf39.mp4?token=UH_GXNTc440gForAZCxf9KZUQDG07zy54whReIu1A4haNNFDPacCfcdv0T0hLeHSPi7S_pO9KoD2vlatHXdWR2XdJNCzK4Xf_CtU7HVDp7S9q1HFEhSMe5a3kKd7gMO0Qw2gJJRcKxyzLWtnDwN9te6FuUsQP8fm_PnyOZgum1DJP-jdGNFPzUpY7J4eWaqfrJ6VKGL1L3mxSRZN06kcJ_cPJ_bBxG_ouSa_0wU_TJTL8iymNAQEHfT4xaoiXUgOnCifXzrmE07WOf4mHdLtFhqJziC1klAWQwDY9NrXzwZK2jglxLCK7UTe_74NNRJWaihI94XdeVPzoA7g6-htj2hoAgFtrpzUZk7r72D0LNR2Vo9B-tLSUbCdsZ19jfH5DhHaJLMXG_d_tshBfxEvcVGkrcEsdNITYTfld6jSb-S5BOtXN7zQUzVuIBmcLhDyY-fGlqyApn4p687Xgv9628e46Ck7VUYUzNrwYDxuhOqsBpqVsW-2XOzvHhC8uX7CnMa987b6HgOZ8SyLBSRgeIFWEj_fN9owLvxjQCPKPVfd7IFvMykMhg86aMdyJ2eWcxxnvNHtG6NWBEhFx--4GyC-dEpInANDH8q482H2MU9Cly-gPklev1nd1uS7LCXjEr7lWDpDt5n6H_rnDXZqmJpGf3_9g93j2fUH-aNBStw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عقاب آسیا هنوز آماده است؛ نمایش آمادگی بدنی عابدزاده در ۶۰ سالگی
🔹
احمدرضا عابدزاده، دروازه‌بان سابق و محبوب تیم ملی ایران، همچنان و در ۶۰ سالگی نیز از آمادگی بدنی برخوردار است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/677658" target="_blank">📅 12:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677657">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DX6G1eqQ_nGut_hWrwqGH_OoMQymOQBMVLAPgjtCYb0RswBVsF0TM_P0Fulud-bVrF1PiGchn-gF_VdS4vI7MpoTqVw8WotwpK-fKxsXr7kle3a9vphtQJsGEmwO8FqPW3GpmYCkEd2uaIFfmI24chfAVwyt4p6iqjNd9_BCpuPN-xRrB0yqB0PdKgib7WnCmge1f-pQAhRYoaYTjERi-GBDRMvvjYB5jaLM6IZ1cNfpPpbLrUUdZofSScp3CGxDBIK18PgfyGyTW_rFbBijKv22Lm-Bnm6mMJAnA-3k--8Cu_B7q1SF8Up9A8FQ4ZnIQOLiko4SpVWF3LF-JwRHlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چطور روانشناس زرد رو از روانشناس حرفه‌ای تشخیص بدیم؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/677657" target="_blank">📅 12:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677656">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
سخنگوی ارتش: از فرصت آتش‌بس و تفاهم‌نامه برای واردات تجهیزات و بازسازی توان رزم ارتش حداکثر استفاده را کردیم
امیر سرتیپ اکرمی نیا:
🔹
از فرصت تفاهم‌نامه و لحظه‌به‌لحظه آتش‌بس نهایت بهره‌برداری انجام شد، در این مدت، واردات تجهیزات جدید، تعمیر و بازسازی سامانه‌های آسیب‌دیده و همچنین تولید سامانه‌های جدید در دستور کار قرار گرفت. پهپادهای جدیدی که اخیراً از آن‌ها استفاده کردیم نیز حاصل بهره‌گیری از فرصت ایجاد شده در دوره آتش‌بس بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/677656" target="_blank">📅 11:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677655">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/144ba700bd.mp4?token=mARAa3Nm8NYYboqp1-mypnZ3D_ThmrqMPh5OO7xEHQyBaN3qV6dH1IhZN_LZKQrIM0PE_xA7aWUbCgQ73f-rl1q7a7N3mtpI28Vy9H0UtqtJVVBJ4qt24jR3k0k9MIMdSP8tI4KkqWVk0orVXwizjOJpk4M_m2UwqMfC2oex2Lgdfa3b9ge57KVoUHhDkwBkutdDcaeASDTMjK78RTLhHU1REbW8rTKRIp9bxL2uWp8VS9_AfbT2UknWlTZ2TgD1aoGrQYEwsVB2mG7tZLv3KNY0FmpmJzt2K2etBTlHyZP1dQCTwxmHC4-lH3bRA8azewyY5nGY-kiYdWLAe4uO8Wc7tlkQwakiRZyouA2GWAtiiyDv4h1Ol7sDTCPtjkgrCUS0VeT-h9zuj4rncd76ttvMeAjGHV-BUF1jgKE-UcS6c-18xGjQHBi7PQBcH4h1364LUtxvNHs_mkfaDtMkx-HRt60y_vEAF6QzHJ4L9nXYrA0wEl8ySO7J0nRq9dKOspK2XUO5cNryh9tYgvBKrW7IpxwGBrXiLtQE8F9EgA_HvcvsSammV9MHzJGGY_qEbYtuTAVpU8WQneFdctR1p_y519fvFzycTUfzIcSMfLrUX4o9ktmfb-upL8S9iQZcEFCOFUyAVEqvvNTDOnrWSnMNRN_Pn4laW1DCKTfjHlM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/144ba700bd.mp4?token=mARAa3Nm8NYYboqp1-mypnZ3D_ThmrqMPh5OO7xEHQyBaN3qV6dH1IhZN_LZKQrIM0PE_xA7aWUbCgQ73f-rl1q7a7N3mtpI28Vy9H0UtqtJVVBJ4qt24jR3k0k9MIMdSP8tI4KkqWVk0orVXwizjOJpk4M_m2UwqMfC2oex2Lgdfa3b9ge57KVoUHhDkwBkutdDcaeASDTMjK78RTLhHU1REbW8rTKRIp9bxL2uWp8VS9_AfbT2UknWlTZ2TgD1aoGrQYEwsVB2mG7tZLv3KNY0FmpmJzt2K2etBTlHyZP1dQCTwxmHC4-lH3bRA8azewyY5nGY-kiYdWLAe4uO8Wc7tlkQwakiRZyouA2GWAtiiyDv4h1Ol7sDTCPtjkgrCUS0VeT-h9zuj4rncd76ttvMeAjGHV-BUF1jgKE-UcS6c-18xGjQHBi7PQBcH4h1364LUtxvNHs_mkfaDtMkx-HRt60y_vEAF6QzHJ4L9nXYrA0wEl8ySO7J0nRq9dKOspK2XUO5cNryh9tYgvBKrW7IpxwGBrXiLtQE8F9EgA_HvcvsSammV9MHzJGGY_qEbYtuTAVpU8WQneFdctR1p_y519fvFzycTUfzIcSMfLrUX4o9ktmfb-upL8S9iQZcEFCOFUyAVEqvvNTDOnrWSnMNRN_Pn4laW1DCKTfjHlM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام: همه ۸۰ میلیون ایرانی حزب‌اللهی نیستند/ خانمی در صداوسیما گفت مملکت متعلق به حزب‌اللهی‌هاست و هر کس ناراحت است برود، در پاسخ به او گفتم شاه هم همین حرف‌ها را زد
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
در مصاحبه‌ای گفتم گروهی در کشور حزب‌اللهی هستند و ایثارگر هم هستند طوری‌که به حال برخی از اینها غبطه می‌خورم.
🔹
در حال حاضر دشمن وظیفه خودش می‌داند که جمعیت منسجم ایران را به تکه‌های متعدد تبدیل کند؛ حزب‌اللهی، نیمه حزب‌اللهی، بی تفاوت و....
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/677655" target="_blank">📅 11:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677654">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1630d256d.mp4?token=snduDx8G8-UsoUqqBhgJG0zIPazVRBWI1kndL84ppFYkkvaZlTYf_033tdIder_Lfr3oWqP6Co7iBEPbMhvSx_W7OeXntWC9-k4e2HQfzTKJAvqIUromYeLwuPcgGZSr7MD3cAtuAbHqbQRC3gV6iMGbuE5ld2FMtLZ-5SurdDYwJ5OtD8PkV1ETVD10ka9yY6j7HFe-hJCGZi6aMJMCl91uCEDOO7qwMEI2oh6hHjyzgCe--03XssnwhmDc527gXzUMssyVG49vsr6qeSklphjwaqVxViCHbveChQK2AOKxdS2v3dqIFL32Tkb2PeG4SeqONFn2oCkLqtKRzGqxclO0HSS_KjMpQ3Fp16nreHgzQ_f69WUVeEQqIRP9jOZUNbcro5SdHBbjZgdJNehyEkxjsNFkqqSrVMdGWeO6IPb9-k2M761XqiOge2NK4g2M91txBYcsprGAKVyowlwmSLA3M4LYh2xOZl5qIZnY7lhJrIMDqAoiIxYBMaranErwPgmRZnmTFstTqdRIOIFO8Wv6YhKhLGI6V3qCLhsYkbEEGV5Qp8-U6VHNDH7Yht30U5nYS2pfzls4WGi3I0DIYjpg9qyGDSQOhaXAxsfwGVKJUXoYD1o-i24x5xqAxw0GNz0kvJ6zOiwHCYynrmyxVz6dkdUFgQHZZB3ZlKYu1GE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1630d256d.mp4?token=snduDx8G8-UsoUqqBhgJG0zIPazVRBWI1kndL84ppFYkkvaZlTYf_033tdIder_Lfr3oWqP6Co7iBEPbMhvSx_W7OeXntWC9-k4e2HQfzTKJAvqIUromYeLwuPcgGZSr7MD3cAtuAbHqbQRC3gV6iMGbuE5ld2FMtLZ-5SurdDYwJ5OtD8PkV1ETVD10ka9yY6j7HFe-hJCGZi6aMJMCl91uCEDOO7qwMEI2oh6hHjyzgCe--03XssnwhmDc527gXzUMssyVG49vsr6qeSklphjwaqVxViCHbveChQK2AOKxdS2v3dqIFL32Tkb2PeG4SeqONFn2oCkLqtKRzGqxclO0HSS_KjMpQ3Fp16nreHgzQ_f69WUVeEQqIRP9jOZUNbcro5SdHBbjZgdJNehyEkxjsNFkqqSrVMdGWeO6IPb9-k2M761XqiOge2NK4g2M91txBYcsprGAKVyowlwmSLA3M4LYh2xOZl5qIZnY7lhJrIMDqAoiIxYBMaranErwPgmRZnmTFstTqdRIOIFO8Wv6YhKhLGI6V3qCLhsYkbEEGV5Qp8-U6VHNDH7Yht30U5nYS2pfzls4WGi3I0DIYjpg9qyGDSQOhaXAxsfwGVKJUXoYD1o-i24x5xqAxw0GNz0kvJ6zOiwHCYynrmyxVz6dkdUFgQHZZB3ZlKYu1GE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از جاری شدن سیل در دره ملاطس در جنوب شرقی عربستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/677654" target="_blank">📅 11:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677652">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDZ6-PQnU-iACsSh9CauTbFCyrweIA46JWqY9Cc7NcdyP0BjtxFvkZobZPDO2fZQhH0B5sV8aZWu7uJ6Obm0zw6KOmxsSxpmgEKdefT7GPAHhjdDMZ3i_VbKxp29_4K9rz8SMySlhwFBs1dF9dkNEcpYeq8F_pdE7ZMjm7JuaYbqH6hzpmC5onVxcQh7t7HU_-7d7hJdMLE1rWRGDCoPYvGXGiL1LVNfCZwYf5JA-wIf6JKECpfDRzVFKLaiUnwQbybNJ0NhbUdq7f1voXumyrB3nHRXCe71ryiHzUcOhM0V4KTeLwdufjJnt3A_V6_-MCsZYcuHSpBGRCjDmybTjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ArXwAYkMwtEV2x6sbTdMjmySEXkIyoHBA4WcZ_h9hWpwrfObYiGELJIaLfsOGegruE3o9Ipxh-G0nMh5lpoRiIOLK-Hgzln7RMlDLsyHCQXCMTQMEXAf3Z2X28AUMqs9Is3ROFBUuCaoMOEyfY5m3Hh_zKAEEglCFfHxDC6MhiuuBLokmCSo293vq2VA_UZ2Ip3Y3bw_nlB5zob6hhEItd5xg3NGsMw7x59yfMx8_N1CylFK5uHJr4w-EZlfJ-Tg3CizVBI9dlmg24udEmSqiCsU3PnzwbaEgluPynL2dWR73F1gMXFmhDAXvecQRJHnNR8USIeO8RnJve__UKtQDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
امیر جدیدی، بازیگر سینما عضو تیم ملی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/677652" target="_blank">📅 11:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677651">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4c2PYLge7xxLrAIsPz6i004ykNF_mgGJOSz4dp-3W-pZfCCTBJtGm8AvKAkwAe86fpz4MEfWKhML4mKRO5jJsP6X8i6905eVGEOzjYJBtp7IHspUxF1Bg4Kji2E14Xh9-Fw37T47Qy3td28RGz_UNngOTJnFHfVqcxTVUfHXOVJkTclmG_G4MBEdrAwukXQ6NW1YzLYrqmt5NuIhU-acj4mqPrfDmL--HC_2a_J-EpR5hYqqxSJlesNS7POc_7oLoOf2nRP4iCjP_HNHTBVXY3490OOpeyrCAxeMYQOajjN_VLxNIIVCvTo82DXr84hZMIFmLp9veoHaBGFPZRDkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت روز طلا در ۱۱ مرداد ماه
🔹
در بازار طلای امروز با کاهش قیمتی نامحسوس روبه‌رو بودیم.
🔹
قیمت‌های اعلام‌ شده از اپلیکیشن میلی، به‌عنوان مرجع قیمت معاملاتی طلا استخراج شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/677651" target="_blank">📅 11:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677649">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WS7i80MsButdOSN2uRXi8wz8I5Mc-vpAlHC_cxebB_i8n4I1pdsYZeD3PN4AIy7VZ7xly2UowmOxD00fsCVGCxpwCWLc40npwBNcHafNmrfAFb5_c1GNWvlQxoQNPFXZ9WkXTK8_Xssh8-9byga_G5Rwi0djnf8XtJ3xseaAQExwAJpnNA4shrxt5d0_hM9nX7IQz9b3RhQ_l7v79lc5mBkSkHORbix6sxvbjKbMRl9FE8sERnar6kmNvszWGigV01bYcV86eAQHkvT69E4p8lb_J_V8Q5trJV4_VzEMyytvOG6ZuqV_OBx5UuZu28dBjdP2KBkHlN-JjTv2VdEimw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت تتر در ساعات اخیر کاهش یافت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/677649" target="_blank">📅 11:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677648">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61093b3671.mp4?token=SSjZCh-lxgd0i9W6kTa9ZFJ0EZD9EVPd-_0uhy8faY23fWoXSI0ZUsK9sb4VdBJnyETKEP0aG2wwqrBCr-dtH9jbuPd5Wg9R-V0VTBz-2c5pqeeSlprYEVwXfa9e63ZVHNaLsPUhwxT8mQW-4ovdOCTJik7MvP1ZKYZWmhEheSDamKgJwfNb-cuzJpGeBoj6cndocz84_kaMHIRuMOUkBB7V-2UjAJBLyvQ6au-bHsnllp-fQnH-0-UG8o1xA4OT_yEMc_foBnlXm777HmUkSFr-OsH7cvAHcOkrutfBWVSPFFtJv015B21TQ_V8KMAqxkfpqfrH7wGUwpPvLT1IuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61093b3671.mp4?token=SSjZCh-lxgd0i9W6kTa9ZFJ0EZD9EVPd-_0uhy8faY23fWoXSI0ZUsK9sb4VdBJnyETKEP0aG2wwqrBCr-dtH9jbuPd5Wg9R-V0VTBz-2c5pqeeSlprYEVwXfa9e63ZVHNaLsPUhwxT8mQW-4ovdOCTJik7MvP1ZKYZWmhEheSDamKgJwfNb-cuzJpGeBoj6cndocz84_kaMHIRuMOUkBB7V-2UjAJBLyvQ6au-bHsnllp-fQnH-0-UG8o1xA4OT_yEMc_foBnlXm777HmUkSFr-OsH7cvAHcOkrutfBWVSPFFtJv015B21TQ_V8KMAqxkfpqfrH7wGUwpPvLT1IuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚗
🧹
خودروی همیشه تمیز، بدون ذره ای گرد و غبار!
جارو شارژی خودرو  با مکش قدرتمند ۴۵۰۰Pa و ۲۰–۲۵ دقیقه کارکرد مداوم
کم‌حجم، سبک و قابل شارژ با USB — همیشه همراهت، همیشه آماده!
⚡️
🧼
از صندلی تا کنسول، از زیر پا تا گوشه‌های دست‌نیافتنی…
همه‌جا رو در چند دقیقه برق بنداز!
🤩
🌟
قیمت اصلی: 1,598,000 تومان
🔥
قیمت ویژه فقط برای امروز: فقط 1,089,000 تومان
🔥
🏠
پرداخت درب منزل
خرید
👇
memarket24.ir/dirmob/180124/g-en26903</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/677648" target="_blank">📅 11:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677647">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2vG27lZoel2nfZLdoTcZtcGfkyYxIUnN7p-e4AI7KT0vo1ItJeid5wxtpamg2q1lUZ3W7O25d7CddgXI4leFiAtSJgDHl6N0oW8u6i1bx4UEBPBp0MjayoOFSGnEBvy_xco8qf2VnNl8RLn2B2X6wL1icI6cepFqOmMS91vbBxGEryBqV_TxtaC0gjI2OzpV-IbJAywF5R3WhVk9AlSSHaFy0Po9MYHPaM5ZXgcqgrUjk29gz2YEa7_ET8BmUHNek166nALFoSibBlCaOkeSkJ6KKXgi8L8Dwgva-nBP1WSuc9dV9BRjIpZveDfSzLKNipaK7XVhnS1XhMsOOgAUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باراک راوید: اعلام لغو حمله توسط ترامپ بار دیگر نشان داد توانایی نتانیاهو برای نفوذ بر رئیس جمهور آمریکا خیلی کاهش یافته
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/677647" target="_blank">📅 11:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677646">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خبرفوری
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/677646" target="_blank">📅 11:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677644">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8f19887bc.mp4?token=Pid1VU16NrSHnwl3ykrPHhigZIfdkuaT9XgkH6W4YYHqct8QgfkLqL2nP-HZRRWGBh5kMlh9XexsU4M-RKDTHd36D_QwVlTI00ctrJGMqcW_kGHZ0Mr0JrcMLgZliMXiHmHnJq2lyVaVcSDqKScWKXCyEtxMubahHLNiiXSX7A-IgwM0IaPJX-qhPbS2Hs0Lem3O36trQlGX_8qrUfrfpAoyscARzf9M7jJiunLFGbxYq3pEYQiUyIlRpcNpATm30hWOG0VCthc86a7CK4IzRNBdZCeXCu-AFSrjsgChQ-Htd1tzno1qodkuUd24YbmcVpgBXufJEP5CQx-Jr39NXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8f19887bc.mp4?token=Pid1VU16NrSHnwl3ykrPHhigZIfdkuaT9XgkH6W4YYHqct8QgfkLqL2nP-HZRRWGBh5kMlh9XexsU4M-RKDTHd36D_QwVlTI00ctrJGMqcW_kGHZ0Mr0JrcMLgZliMXiHmHnJq2lyVaVcSDqKScWKXCyEtxMubahHLNiiXSX7A-IgwM0IaPJX-qhPbS2Hs0Lem3O36trQlGX_8qrUfrfpAoyscARzf9M7jJiunLFGbxYq3pEYQiUyIlRpcNpATm30hWOG0VCthc86a7CK4IzRNBdZCeXCu-AFSrjsgChQ-Htd1tzno1qodkuUd24YbmcVpgBXufJEP5CQx-Jr39NXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاموشی تنها نیروگاه اتمی مجارستان در نتیجه کمبود آب
🔹
نخست‌وزیر مجارستان پیتر ماگیار با اعلام تعطیلی نیروگاه هسته‌ای کشور به دلیل کاهش شدید سطح آب رودخانه دانوب، از محدودیت برق و احتمال جریمه مصرف‌کنندگان خبر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/677644" target="_blank">📅 11:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677643">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae21676b1d.mp4?token=USIFFHtPsPyZdKt-hkkWBBg29bfiLoqtdfK6vyFXGp3asd39QEIq_RaUNzqusaQ6nPzqBkyFlLujlylJlCKWQZ6KtDNzUGh3FMU5C8-eJFuUL-wPUwiASwZlhoR8Er7jWizlSFCABzxqr-dQ05Rufa7ZjRUuDPYCwWgzxIDreu8cW2z_9CgeQheluZo5ZQMUOx1sLelKkqIHz6HafKEBCGyOVFeMH7msJfjcahsjOx_ty8bMaOvOK_vn0XC04F53Je5gm5iehDF936Mj4LcypOf6OpmxYoLByAC3nlYsbWaytBjJzcAFg94hq6C-YVBbAvOs2-NpEufr8UOlkIJgSjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae21676b1d.mp4?token=USIFFHtPsPyZdKt-hkkWBBg29bfiLoqtdfK6vyFXGp3asd39QEIq_RaUNzqusaQ6nPzqBkyFlLujlylJlCKWQZ6KtDNzUGh3FMU5C8-eJFuUL-wPUwiASwZlhoR8Er7jWizlSFCABzxqr-dQ05Rufa7ZjRUuDPYCwWgzxIDreu8cW2z_9CgeQheluZo5ZQMUOx1sLelKkqIHz6HafKEBCGyOVFeMH7msJfjcahsjOx_ty8bMaOvOK_vn0XC04F53Je5gm5iehDF936Mj4LcypOf6OpmxYoLByAC3nlYsbWaytBjJzcAFg94hq6C-YVBbAvOs2-NpEufr8UOlkIJgSjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فلامینگوها در خلیج گرگان
🦩
#اخبار_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/677643" target="_blank">📅 11:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677642">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBAQPHwSnFftNbVl-Q0CA2oEpse_Pn6__ae4gfYCiGTvcgFXIfQZ05jvLcJ1KHl3fWxbW98H3_Z1Z8RRDHMEzvBRGjEeBgcvXrRXw7uGzlImAXp-vlqUhv17nc_n8sVgYD--LJPXM9T6GIV1rQmvvN1aY3U-T2jPtsOMmAci8WcLVpCy5Y-xhUX66FSXGGy4Tk4sv1GhJ9HpH5zOvdDAFluA3lu8cBUPhx-uJWAFhJ2qXDxMFpCrxtLFE-V7S0cRfKLJTbwM4I-3ZuE15FjApGg-APacH6CLDUk3q1nsp9BBYnjOgJMXurb1HfY7TP_YW1ZLitj5J1hG_Bj8Ld1VhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بشرا شیخ: برای واشنگتن در ایران کار تمام شده است
🔹
آمریکا به موشک‌های پاتریوت و تاد نیاز دارد.
🔹
اوکراین به پاتریوت‌ و تادهای آمریکا نیاز دارد.
🔹
اسرائیل به پاتریوت‌ و تاد آمریکا نیاز دارد.
🔹
عربستان به پاتریوت‌ و تاد آمریکا نیاز دارد.
🔹
قطر، کویت، بحرین و امارات…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/677642" target="_blank">📅 11:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677641">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea5ad612f.mp4?token=W1AxiU2TdF8V3odFzLPKnm276yGwjiCBnhdCdBDYDZZEszoGp08o6Ikf16GEi2gZaORS0dTjm7pVKJRoeSD0kiKSDnO9NdlGh3p8I-rjpeXZm0MIVhZfmK8Cnp4HluiVa6J9jrTvdCTf1_WwkTM6OCqkAk7EJJR9AgQnGrWnTe69fWhwM7Le1XTUNUdluW4Pl5fqBzD3oIdh7FjB76rwKjkkJ0l9pm9hbJAjEgmSnqFB1QB3sK-juFw6nVctkMyrpozdeKtkhOxO5F3WJdICOr_Q1XZrCxtgsiaEfS1J5TXzwQ2MrAjtCabWn0WOuAgxdBtM51vg8_ZZFEhcXxS9Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea5ad612f.mp4?token=W1AxiU2TdF8V3odFzLPKnm276yGwjiCBnhdCdBDYDZZEszoGp08o6Ikf16GEi2gZaORS0dTjm7pVKJRoeSD0kiKSDnO9NdlGh3p8I-rjpeXZm0MIVhZfmK8Cnp4HluiVa6J9jrTvdCTf1_WwkTM6OCqkAk7EJJR9AgQnGrWnTe69fWhwM7Le1XTUNUdluW4Pl5fqBzD3oIdh7FjB76rwKjkkJ0l9pm9hbJAjEgmSnqFB1QB3sK-juFw6nVctkMyrpozdeKtkhOxO5F3WJdICOr_Q1XZrCxtgsiaEfS1J5TXzwQ2MrAjtCabWn0WOuAgxdBtM51vg8_ZZFEhcXxS9Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور پرشور زائران حسینی در کربلا در آستانه اربعین سیدالشهدا(ع)
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/677641" target="_blank">📅 11:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677640">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
هشدار پلیس فتا درباره رسیدهای جعلی در معاملات آنلاین
پلیس فتا فراجا:
🔹
فروشندگان در معاملات آنلاین، صرفاً به تصویر رسید بانکی اعتماد نکنند؛ ملاک، واریز قطعی وجه به حساب است.
🔹
به ادعای انتقال وجه از طریق شبا و واریز در ساعات آینده نیز اعتماد نکنید و تا دریافت وجه، کالا را تحویل ندهید.
🔹
موارد مشکوک  را به شماره ۰۹۶۳۸۰ گزارش دهید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/677640" target="_blank">📅 11:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677639">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
درگیری میان نیروهای مسلح یمن و عناصر وابسته به ریاض
🔹
منابع نظامی در یمن اعلام کردند که نیروهای مسلح یمن با عناصر وابسته به عربستان در جبل هان واقع در غرب شهر تعز درگیر شدند.
🔹
همچنین گزارش شده که در این درگیری‌ها حملات توپخانه‌ای نیز صورت گرفته است. این درگیری‌ها به منطقه الصلو در جنوب شرق تعز نیز کشیده شده‌ است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/677639" target="_blank">📅 11:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677638">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6tUV5YzpfpQYP5eljaCH0dgeytbpJ_c0x0_YvJUrNKYjasGzdLUxNPV2WdxtZvnTGID1LXh8mAJH9YZXY-gtA_s9Gqm8WTVFI-UNnQ3HD1oV8xRFyWEFP3FyU9KsNfrY7gLfDRhcpNhPA3g12_b_Gc8RctfZb7ixh3a5tvGWYSmPOVye-ZwY-ajpxKR-PMY8StK7zrP0yGQ1uOwSB4XD69Ed6NhPkRvvqtMBJ4dBFckWIWuQ-_rnJd7THsJSfmU3FVFNFg0q4QIXfa3iv77ijjXHALzgkarfyE1D9ZkJe1N_DyKX5w_2FbTLggo-fTG72F57K5kbE5ptIHM5uxHbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرپرست وزارت دفاع: نه غافلگیر می‌شویم، نه منفعل؛ هر تهدیدی را به افزایش آمادگی و تقویت بازدارندگی تبدیل می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/677638" target="_blank">📅 11:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677637">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_3B8jorWHIyqxuTK3ycg9dkLIXK91vALS0GK2v7umxaw4DKUQYtJ1l9H4iNvXgrGzw1MIsW-ggPz_WLVadlWUlXVTrCxQ_80FL3SDFCzmLFBsbJyifk43-BFJt8fzUJKYYqZ9MvUuzx41g6own_TXne2hHdNnR5a7GoPDMMG7qb3sC0OwgREhWgH0C_H_sMNj3o0ZwtfSGgk9eIAHw07GgTlWARKq47PIVLHxgUCWwdrm5usJH4augTdT4ygs0_bCo-OWsILJ97qtyaEGDA_vZMOXmmKcwqWWYOuCT3804o4wb53ZoZKyA6R0plWwjQvYyDYStsJx_hQdTV_HORiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر مسائل دفاعی و امنیت ملی آمریکایی: واضح است که در ظاهر، این ادعا که ایران با رئیس‌جمهور ترامپ تماس گرفته، از او خواسته حمله نکند خنده‌دار است
🔹
سرانجام بخش کافی از هشدارهای نظامیان به رئیس‌جمهور منتقل شد که اگر این حمله را انجام می‌داد، برای آمریکا…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/677637" target="_blank">📅 11:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677636">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
ابهت و زیبایی حیرت‌انگیز در خودروهای BMW موج می‌زند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/677636" target="_blank">📅 11:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677635">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WY6fN5BZnv_uurdfV3BxOH8OU2pNkqHVEo9M0BTA1QAiQQRWv4rbzd2EpoLS_CSvel5kW3Jj6L9Qjn1encMkQ71FIQ8RfhW2NhaYpPYtwUh6W1hFUPHoM2OeLUWx_Iw5qWTdYCLxn_I7CJBhGxhO_I69xiRCc-oWm09LGfrOHz3rlRMlHWLQiJdGd_af9lwwxH0MFjt1m0bsAbZ2eT7RZDlcAunRBwitTeGRLT3eCa_YtGqTjnQhuPTMHtKSXn3dFj-EqHdbVJlzwqQHnb7XsuAYeAERIOEO1vyTiGS3Jukv1_ujLWI4oXK7o2yLBXQSmYAOdVW9tZTV1_7lIsi4Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر نظامی و اطلاعاتی: ترامپ ادعا می‌کند که ایران و کشورهای دیگر از او خواسته‌اند حمله نکند و قطعاً نه به دلیل کمبود مهمات.
😌
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/677635" target="_blank">📅 11:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677634">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e8752ae23.mp4?token=vdry_W_bFcjoUlJe4xOLWk-9Ia-dQD0wGoQbpP9mNiCCoCr15B1vD29YTWKdCHcas6qRmyWUcq_ymlNyjOmoJCgzKl5K5_EioWkdrEknyFrBnGgDSNj9LehTRJ2MwXLDrTVbaF7ohUt_CeYRJ_oUPAhvwL2tMTZLKWSL66OAGhU1WO_I020gmf8sI30J4STJXjpTm4zBJ8vWITpnzP1sO0iHYzZf38KGmt_PrvYPQAhcaUJBpK472jS9etXMwvryq-jbn5Vt7lrgZD8qehxMF3kKQpY_bpne1snVxce3Ms_7wg1HkkLx-Peb-lDWLH39Hhwo_QezOTnbNmp2f1xHgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e8752ae23.mp4?token=vdry_W_bFcjoUlJe4xOLWk-9Ia-dQD0wGoQbpP9mNiCCoCr15B1vD29YTWKdCHcas6qRmyWUcq_ymlNyjOmoJCgzKl5K5_EioWkdrEknyFrBnGgDSNj9LehTRJ2MwXLDrTVbaF7ohUt_CeYRJ_oUPAhvwL2tMTZLKWSL66OAGhU1WO_I020gmf8sI30J4STJXjpTm4zBJ8vWITpnzP1sO0iHYzZf38KGmt_PrvYPQAhcaUJBpK472jS9etXMwvryq-jbn5Vt7lrgZD8qehxMF3kKQpY_bpne1snVxce3Ms_7wg1HkkLx-Peb-lDWLH39Hhwo_QezOTnbNmp2f1xHgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رد طرح آتش‌بس ترامپ در غزه توسط شیخ زکزاکی: درخواست خلع سلاح حماس «بزدلی» است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/677634" target="_blank">📅 11:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677633">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBgKqxIiSj0S2ES5CCSQcwIDiG6SVaUVVC7CM9rEyoic6ao0w8ruypRzHFXGGcjAG7_oYbz_yKpj5lNN7toBja0PXVSK88hKu6MpmX4fEGglIoKlVmX1r6mN1GeQDdtQKBO0UmWEc-beZXSKZy2KYIR2AmdT0-SnMnAeNisGTI8vm8TLpOpW7G-w2DDyXsOZUuNn_d_dPaIJLm39I64NTsC5wP7rac1TxKvQ004P6YhUXbkUOZWHtTzGyZ2qRzGfeAMNWvEtXNXPzNA8tyr5wHZ4MhPwzwuCaZdEGJbOcC8WrtgH5Z0mJjyvXWW7F8uJUkIU6aSt19FNBW9_4YtnpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر نظامی و اطلاعاتی: ترامپ ادعا می‌کند که ایران و کشورهای دیگر از او خواسته‌اند حمله نکند و قطعاً نه به دلیل کمبود مهمات.
😌
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/677633" target="_blank">📅 11:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677630">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cf768c0fb.mp4?token=RFeJDkJsg797jdG6IbAlPDV_RapjrQSb6czCxgnD5ZN4RgMEtc_a4LZuJ69nCnSM1wO3CUsCbgzR0h4JZh0yAKQWL_tg0gpIKJHNsD82LTF2giLhUK5Sp4q_ivNgGQZM0F5gSkT4DtyUHZoddsR5vV7ppEptpJu6Gp8yYgy-Ek1BTz4HgpmuBx0isFc3735S364C4-t-2GaKj9uaxb7ZWgZ4NcQj2AwcNqUxUW7FjgvVQsKEFzGmDpUANtSmMMMvKbC31TvdZB44mX6WSlrllz7RxXECqda31GvyouzYA7s_GgswSfKyCotJ1Qm42GTDH45YHvBFSETlzqxAjnmksA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cf768c0fb.mp4?token=RFeJDkJsg797jdG6IbAlPDV_RapjrQSb6czCxgnD5ZN4RgMEtc_a4LZuJ69nCnSM1wO3CUsCbgzR0h4JZh0yAKQWL_tg0gpIKJHNsD82LTF2giLhUK5Sp4q_ivNgGQZM0F5gSkT4DtyUHZoddsR5vV7ppEptpJu6Gp8yYgy-Ek1BTz4HgpmuBx0isFc3735S364C4-t-2GaKj9uaxb7ZWgZ4NcQj2AwcNqUxUW7FjgvVQsKEFzGmDpUANtSmMMMvKbC31TvdZB44mX6WSlrllz7RxXECqda31GvyouzYA7s_GgswSfKyCotJ1Qm42GTDH45YHvBFSETlzqxAjnmksA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دوقلوهای تازه متولد شده همدیگر را در آغوش گرفتن و می‌بوسن
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/677630" target="_blank">📅 10:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677626">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ELhKovOmJFUxbjYTSYPN2xyoodtfL0NvLNExOUcOqGwjsfRTAHzazu9U_CwatfJZy_K9f5XZmfPRA2ArmN16nFgfsJeJqksgIQpaWJxEktW5H3IJ1tfk_fbLruio38VigouMb6mOa4nshiB42Jn4IYMY-CQuFcvL4IARw3R_y8CA31aU6XAoatAFzHrvl84d1UyxqdPsODFzYojqtlEsNuzNAS5t-XYPcYpdk9EBga_8RB-hfExS9USZq6FuVZ5-sEjIIJfOx-tS2qlNTCZNbduERkjX1XzTqfQl2Yo0hznFO4mviZJfIINC1WM9X-V2Rl6cDyb_esNHL1Xb9o4OCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HQjxgkDY1WmoqoUPRqMA7xJGX4UblpmRXp722-Zj-M6mxpsLDlMlPkPX6CVyi-iyELHVDMXEpm6eltanXRbxdwhvIZlxBZBpkPkfi8rP_FNGjyMnu18-dsER1pw0awn7_yTphPfGtuyW1X37fK2UZoic9P9B47DbOFa4AC6OhP8PRH6imNIMAlveqgDquM9LmsyHW-9Um8ZZap0OhO14obMbnuBmooxSXuQ9dvsbSTZlepdBGyGkrOuBNkiDqS-DFZdVFjfYuc_9Ao7NDpVC9DHdkaG4coUQcorSbWsiX1ZiGCoOC_qtEjZxp2vwFpd3tb2JBq_p1zChD6W-rakzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ahHB5_1w1OFJMvHX_qZuXMkbLig6diSnD3l1rma3ZHEg28N7nJk7vJfVgqeSaGzgRxN-OkxnOkQKzTtz5EKZ5QDicvBOezjaBgWBONAocIZq9mYcflEPh5a6YTQMhwXxAlDIOTKKgbgwwnA0hr4lvTWo2DTnSL7bD0_Cj3nz6nvbBNv7cl5jIwmIZKOXacc7mfYm6oYL6ZtLeAtyU6myf6F9HLWaDP_fv0jJfiZrXk7o8Y9rXs23QejW-7n-6zHNQ6kjk29L1kNX7Xj3VwhrYtbBSsWu4v3BjZyxFEkjQ8dY1UvlUu-HRy-uR1QWqoFF9J6HY8vsNxO-8VCdawTI_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fRLFBH_gkRnIL05Qt3NAKg9HWS_AHzCQmqPqcZ5kti08mWWwxRGKxfAv0NQiAF3x6TOcyDxMgWz9ibrq60FVnlOffBVTOgFYwwyd_Yfd3ODNmyQzCNZVoix1l6N6KwIO4ALbEL95UN0x57OShBAlyqsasBez9yOTfet8sjpYURkTIi-Q9GYv_hYY1tXqCXBRn3b-hsrUGy5q_UWQhfGiCBlOMj6E63oYyW7gHDitCejeWIpsybsZFEoZajSzcZtw_anOtkqqRz0Wd_yOQV_DJ5Zdf3T4TzEeKeP4VkWTofkm1dh7G8TBwaQaN-flR4jjB6_kmYwgphDkypUDslJ7_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ویرانی‌های برجای مانده از حملات هوایی بامداد امروز رژیم صهیونیستی به جنوب دیر البلح در مرکز نوار غزه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/677626" target="_blank">📅 10:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677623">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NE2RHr22vpjzya1N0PZhq9PwPnYleOFw9Mit_N-Y74kglX3ft6WFRZe1EbFwEStVmMxubndWg7_sZwE5UM6brnKtKdAtxgiX0HE7pTO8MvfwcKzXhv7K2m2VrmbLDtVBGdIDvGT-_GjZjWzw8UdEKgVw5KU5_zE0I9nd1qXyElpuMENsJehKzr14hT_e5NEmPxjXixMdKnKT3n-cWoUiksOMAZiEiNoIcJNeYvk8wuRsm0qkjAFtNA1Wo1vnEDFT363U_5Yw35ad6JwmQ3fN-9fz4VntkWb9mZCNquC7pNbG-GjNbRvsM9f6b_VSGhkUW2AEnJhYANW0oaVlgdPhEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دولت ارمنستان استعفا کرد
نخست وزیر ارمنستان:
🔹
طبق قانون اساسی ارمنستان، در اولین روز جلسه مجلس ملی، دولت استعفای خود را به رئیس جمهور تقدیم می‌کند.
🔹
رئیس جمهور طبق قانون اساسی استعفا را می‌پذیرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/677623" target="_blank">📅 10:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677622">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqR4NxGG7VW3ig8QoFfuGWenwUV_hcrqWBvKVwI7LC6azEipuseqNEpt25jravMhLbvkayFFvIO7LA5arUewdICleL3EPf7yDIEe2dOeGmVMQ-EyBrKglmP3vzhq4MJ_gfuBhsb_KU_T3cp5ViGn07veoCwp4lYJIIlhUgWD3F_7G_XrGGJ3dPTeO2bSBOtfzccs3Bk-i_5YoFtnAWZN3LmxXzXFAfbVC1hzDr1gC0JwM6N1MD1jtkuNpYGFXsLpCZsK8QpsbIDEvW3oQnfKRfcn6IfstriTZDX57ZzyRi7eCn9Vq69ot8RQQRPJq-8FGcVlX_9tXWdduCrcEnVGng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشانه‌های افرادی که از لحاظ عاطفی برای شما مناسب هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/677622" target="_blank">📅 10:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677621">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
چرا از رهبر سوم هیچ صدایی در رسانه منتشر نمی‌شود؟
همشهری:
🔹
هر فایل صوتی لایه‌های پنهانی دارد که سرویس‌های اطلاعاتی می‌توانند از آن ابعاد فیزیکی، جغرافیایی، زمانی، سخت افزاری و زیستی گوینده را استخراج کنند.
🔹
آکوستیک محیطی و هندسه اتاق:
هر فضای بسته امضای صوتی منحصربه‌فردی دارد. با محاسبه زمانی که انرژی صدا پس از قطع منبع ۶۰ دسی‌بل افت می‌کند، حجم تقریبی اتاق تخمین زده می‌شود.
🔹
تحلیل فرکانس شبکه برق
: سرویس‌های اطلاعاتی با تطبیق نوسان‌ها با پایگاه داده لحظه‌ای کشورها، تاریخ، دقیق ساعت و حتی بخش خاصی از شبکه برق محل ضبط را ردیابی می‌کنند.
🔹
طیف‌نگاری و امضای سخت‌افزاری دستگاه
: میکروفون گوشی‌های همراه فرکانس‌های بم را تضعیف می‌کنند و قطعات ارزان‌قیمت اعوجاج هارمونیک خاصی ایجاد می‌کنند که مثل اثر انگشت دستگاه عمل می‌کند.
🔹
نویزهای پس‌زمینه:
صدای سیستم‌های تهویه، ژنراتورها یا تجهیزات خنک‌کننده مشخصات فنی محل را فاش می‌کنند.
🔹
زیست‌سنجی صوتی:
رزونانس‌های مجرای صوتی یا فرکانس‌های فورمانت ابعاد فیزیکی نای، دهان و بینی را نشان می‌دهند. الگوی تنفس و وقفه‌های میان کلام هم وضعیت جسمانی، ضربان قلب و میزان استرس گوینده را مشخص می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/677621" target="_blank">📅 10:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677620">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
کارشناس عراقی: انتقال تسلیحات از سوریه به عراق توسط آمریکا و با هدف حمایت از گروه‌های تجزیه‌طلب در اقلیم کردستان عراق انجام گرفته است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/677620" target="_blank">📅 10:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677618">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjOYVfuGT5Uu6P4Lu7az-ZzOwKt2mIqFhFONA1Ilnm_XJwXMyzV7dCWderhN1ysTAAJ10rD0wonkZl0j9TKMuBs1eQPM39vQXHB-n-U6mwQcr5QmnjlQOGU25K_N1RQ3i_ChZz0nv1i5ofgKrJKdvsCevZ5uNMoK_7hNQbMRjCANAe264qk9loacx4I1mlLNvYxwic6Y2nGE4ynvphjb4m8yxJVOKvvnFlVWpSkxLIV865gHrZMciGvBbQc5olEsyFcrQne38Y1rXE-gPLm0_qs5EAjkAxJDcjXJADePle2W1616oPFcSc47XTFaUpaSJqvg-SW1ZdmPu036euMUtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک‌تایمز: آمریکا با بمب ۲ هزار پوندی خانه‌ای در قشم را هدف قرار داد
🔹
نیویورک‌تایمز با استناد به تصاویر، ویدئوها و بررسی کارشناسان مدعی شد آمریکا در حمله به جزیره قشم از بمب ۲ هزار پوندی «مارک-۸۴» استفاده کرده است؛ حمله‌ای که به گفته مقام‌های ایرانی،…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/677618" target="_blank">📅 10:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677617">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecSn1HbBS5Tz1YPer59PvFykwBcdj2-HvvHNE_LVXw1w9tPBHLdakcbh_p-UvrehhBXDfVdgAkhrAdC5HWjSFFTI__aT_emPbQuPk48C2FarbxiRJcx6PUtQr9-hYValExhh3J-Ii7CC5So3Xo3ywsVXZ1Ysk_0jZa2luygR9Og1J1_IT0La8bDa6qkusQ1PHzatzreXOVreCbkVR1h3Tnz3tYfpg-xHSpHYt-OrN1yL8b0lz4YgSxWxvbrYhj7fabefnBZOMaqbaCx82Wc0RCmyN37YInEWNBruSoQKAdSd-hD8C3QWRYaYNYKHswrdm3kGcoc9AGqLKurTYPeKOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امور داخلی کشور: مدیریت شهری برای مردمی سازی خدمت رسانی به زائران اربعین گام خوبی برداشت
رئیس کمیسیون امور داخلی کشور و شوراها در مجلس:
🔹
در طول سال های اخیر اقدامات خوبی برای بهره گیری از ظرفیت های مردمی در برگزاری این مراسم انجام شده است. مدیریت شهری نیز گام های خوبی در فعال سازی و به کار گیری از این ظرفیت ها داشته است.
🔹
همچنین درباره اقدامات فرهنگی انجام‌ شده از سوی شهرداری تهران با طراحی شعار « یا لثارات الحسین» و نهادهای مختلف برای خنثی‌سازی فضاسازی دشمن علیه مراسم اربعین گفت: تبلیغات امروز اهمیت زیادی دارد. دشمن به دنبال عملیات روانی، شکستن روحیه مردم، ایجاد دوقطبی در جامعه، بر هم زدن وحدت و یکپارچگی جامعه است. رهبر معظم انقلاب اسلامی نیز همواره بر حفظ وحدت و هوشیاری در برابر جنگ روانی، جنگ شناختی و جنگ ادراکی دشمن تاکید کرده‌اند. از طرف دیگر اقدام مدیریت شهری برای مردمی سازی خدمت رسانی به زائران اربعین گام بسیار مهم و تاثیر گذاری است/ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/677617" target="_blank">📅 10:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677613">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/442feeb9ec.mp4?token=UOhs_aYK-qxBcRx2Fh-tJjTLKasWGYKue4u5OcKB1L8vvk22JoHJCjvmamkQO4_DPhZmL8bL111x_RIaZ0Uv2idmRxA62krXyyvG4usCjHefPrSL5gxk1zErym50CQ8Gz1VS48p3KGkyLE86e5nHf4t4qR_TiIdAB-am_kmOfxoy9xvlAYisI4a7ztOdw0kBNEWIZRETAmO5w0_Hs5BNXSS03By5PqVxTZSamj9pBjjIOk2EEuMiDEyB87P8JSYGZVCnS_k1sbbxhOMJHLqp-tjjw5AociGn_nGyMr4B64RWbAAULq2gXoDGETEbbhqwY_Y86CJaYbVhQkN6YwM8Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/442feeb9ec.mp4?token=UOhs_aYK-qxBcRx2Fh-tJjTLKasWGYKue4u5OcKB1L8vvk22JoHJCjvmamkQO4_DPhZmL8bL111x_RIaZ0Uv2idmRxA62krXyyvG4usCjHefPrSL5gxk1zErym50CQ8Gz1VS48p3KGkyLE86e5nHf4t4qR_TiIdAB-am_kmOfxoy9xvlAYisI4a7ztOdw0kBNEWIZRETAmO5w0_Hs5BNXSS03By5PqVxTZSamj9pBjjIOk2EEuMiDEyB87P8JSYGZVCnS_k1sbbxhOMJHLqp-tjjw5AociGn_nGyMr4B64RWbAAULq2gXoDGETEbbhqwY_Y86CJaYbVhQkN6YwM8Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی قابل تأمل از دختری ۱۹ ساله که در این سن دهمین عمل زیبایی خود را انجام می‌دهد...
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/677613" target="_blank">📅 10:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677612">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc59a098af.mp4?token=h8uMvmtKORwowrtqn8ueq994zcuq261nEpniqtW9b4666BksiL9P4M0o81aDngp2JycyC6r9BImIeDQluCCV6VSix8a7iuaRjBB0YH7yGuP1U-KpR7joE_A7BOUY3w9wo90hJywxyEy7mpxpZxFmMHPjn8eO4-4CR3ndk5-joPu6TXHWiXVjRR36XPxFzZZ5iWpcpFz-TzEbxAFLwqAhUgDjza5dbynMTPZjzEz02OmqvDZDfb_uuWMOeDb1u6JV6DomP6aES9LwGbhy1CIM_0ifLm3phKIuN9Iv5h9VHgJuXCc-leiiUyBjQzavZ_aKtuAwWxShavqZCwMzCxsk8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc59a098af.mp4?token=h8uMvmtKORwowrtqn8ueq994zcuq261nEpniqtW9b4666BksiL9P4M0o81aDngp2JycyC6r9BImIeDQluCCV6VSix8a7iuaRjBB0YH7yGuP1U-KpR7joE_A7BOUY3w9wo90hJywxyEy7mpxpZxFmMHPjn8eO4-4CR3ndk5-joPu6TXHWiXVjRR36XPxFzZZ5iWpcpFz-TzEbxAFLwqAhUgDjza5dbynMTPZjzEz02OmqvDZDfb_uuWMOeDb1u6JV6DomP6aES9LwGbhy1CIM_0ifLm3phKIuN9Iv5h9VHgJuXCc-leiiUyBjQzavZ_aKtuAwWxShavqZCwMzCxsk8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به سبک انیمشین درون و بیرون، برای بچه‌ها غلات صبحانه شیر و میوه آماده کنید  مواد لازم:
🔹
یک پیمانه غلات صبحانه دلخواه
🔹
یک پیمانه شیر
🔹
نصف پیمانه میوه تازه
🔹
یک قاشق عسل
🔹
یک قاشق غذاخوری مغز #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/677612" target="_blank">📅 10:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677611">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e17b7771b.mp4?token=oAZdoPBsww5CtDUz0rJMkPVZ5MHY4fc0N5hLZFp0ngtKZ9PZg9QIsOBS2ZcR4ib38opB-KTbEVMgTFkx0w4NwH_QM0BGoq2XUvXdwf-_ov2sPEyk6Yar-DHd4YP00PSpXsQc1MyI7RaccV5YaTRmqPY3RTI1SZocfWvPHdYxcdbYb8xDJrVJK1glWjJbkzk8bNpomteCgr-IrJ5nUbX8FRM17y1igdDXrm1KZC8i1QTXHb2rXAL7s3UF4dABmcGsJJsDhDX4AVLx6ui939UXRhK2L-GTJZ60uVK8B5RgNSHZ3zagPqps_gHGjMY3luoOH6VZ9IV2GCmkW2TaIcnXALg5Nd-IS8Bd5x3786-VF2d6o3L4eXq6qwZVrtOgscJDOxuIra0TStRFPviWSzkldhMWF1gpoVPcjD5y5leMuxxhhO2L-YgWvmZ1FCN872mdSCAom7_yTA9LVRz9ZQC3a5zWdYGDA1nui40LQMs-zXnIwUmrG4RjxmG_-vWVgM4hF0Y8I8xKcA7i6_AYABakTc0RsgO4LvvpKSN9Vvuw_Uhndf7VNcRLGvveT-axwBtwCr5eLirj2ngiAGzRZveH_jthVVI9aI-fdcwwiBJF7UnGabngNSWrOFJ92u6yhh1cd1orC1nk8bPvPDodEibLpZePzaLqbbQ0BLAckuWCtkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e17b7771b.mp4?token=oAZdoPBsww5CtDUz0rJMkPVZ5MHY4fc0N5hLZFp0ngtKZ9PZg9QIsOBS2ZcR4ib38opB-KTbEVMgTFkx0w4NwH_QM0BGoq2XUvXdwf-_ov2sPEyk6Yar-DHd4YP00PSpXsQc1MyI7RaccV5YaTRmqPY3RTI1SZocfWvPHdYxcdbYb8xDJrVJK1glWjJbkzk8bNpomteCgr-IrJ5nUbX8FRM17y1igdDXrm1KZC8i1QTXHb2rXAL7s3UF4dABmcGsJJsDhDX4AVLx6ui939UXRhK2L-GTJZ60uVK8B5RgNSHZ3zagPqps_gHGjMY3luoOH6VZ9IV2GCmkW2TaIcnXALg5Nd-IS8Bd5x3786-VF2d6o3L4eXq6qwZVrtOgscJDOxuIra0TStRFPviWSzkldhMWF1gpoVPcjD5y5leMuxxhhO2L-YgWvmZ1FCN872mdSCAom7_yTA9LVRz9ZQC3a5zWdYGDA1nui40LQMs-zXnIwUmrG4RjxmG_-vWVgM4hF0Y8I8xKcA7i6_AYABakTc0RsgO4LvvpKSN9Vvuw_Uhndf7VNcRLGvveT-axwBtwCr5eLirj2ngiAGzRZveH_jthVVI9aI-fdcwwiBJF7UnGabngNSWrOFJ92u6yhh1cd1orC1nk8bPvPDodEibLpZePzaLqbbQ0BLAckuWCtkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وحید شمسایی: امام‌حسین(ع) خودش دست ما را می‌گیرد
وحید شمسایی سرمربی تیم ملی فوتسال درباره حضورش در کاروان اربعین حسینی:
🔹
این حضور به این دلیل است که خود آقا دست ما را گرفته و امضا کرده است. اولین بار است که با کاروان و به شکل گروهی در این مسیر حضور پیدا می‌کنم.
🔹
زیبایی اربعین همین است که هرکس با هر توان و شرایطی، به عشق امام حسین (ع) قدمی برمی‌دارد. فرقی نمی‌کند عراقی باشد، ایرانی، بحرینی، یمنی یا از هر جای دیگری؛ همه کنار هم هستند و از این سفر معنوی بهره می‌برند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/677611" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677609">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
رانت، مافیا و دست‌های پشت پرده در مصوبه تعیین‌تکلیف نیروهای شرکتی  بیگدلی، عضو کمیسیون اجتماعی مجلس:
🔹
مصوبه هیئت وزیران درباره نیروهای شرکتی تحت تأثیر رانت و مافیاست و به جای تعیین‌تکلیف، به هدررفت بیت‌المال منجر می‌شود.
🔹
رئیس سازمان اداری و استخدامی باید…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/677609" target="_blank">📅 10:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677603">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAlldt23hzkbfY9ABBK1mdEwhiLfDX9kJ_YyM_eZ7U2c9ElJAD5bY7toE3RTA9vYsaBKD54KKvfbbV5nyGjSkOvP-ML57OIoifqKA1KZveGqKxkj3B9OsxrYnrKoUehOENWblc9hcj0Pq916nF9J-a-nsDQxeiSJlv_IksQ41l-i-mgBik2W8LYbdtusyT52J0EAkFibzglgaENj599qxcWYqoEh5FJGzMiEg8qLqNAgdgu-dktKniaoboclz-t5c4HopL0I_GxZh6IA2tHp0Mp60O1IeD2FntOkDCRug81ciSIXJTfN4w1Y508BpO7rdmZSU18BX65UwtQcWqmqlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر روز ناسا؛ رنگین‌کمان آتشی در آسمان ویرجینیای غربی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/677603" target="_blank">📅 09:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677601">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
فرصت دوباره انتخاب رشته برای نهمی‌ها و امکان تغییر رشته در پایه‌های دهم و یازدهم
مدیر کمیسیون مقررات تحصیلی شورای عالی آموزش و پرورش:
🔹
نهمی‌ها می‌توانند در آزمون تعیین رشته مجدد شرکت کنند.
🔹
تغییر رشته در پایان پایه دهم و در پایه یازدهم (فقط درون شاخه نظری) امکان‌پذیر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/677601" target="_blank">📅 09:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677599">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
رانت، مافیا و دست‌های پشت پرده در مصوبه تعیین‌تکلیف نیروهای شرکتی
بیگدلی، عضو کمیسیون اجتماعی مجلس:
🔹
مصوبه هیئت وزیران درباره نیروهای شرکتی تحت تأثیر رانت و مافیاست و به جای تعیین‌تکلیف، به هدررفت بیت‌المال منجر می‌شود.
🔹
رئیس سازمان اداری و استخدامی باید در این باره پاسخگو باشد./ باشگاه خبرنگاران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/677599" target="_blank">📅 09:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677598">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ad4M5qDHRfo1QyIcpS1LILAkdHyR21BRT_OhMqWqQOiIZUM8v_DwmFWmykX1awfnQJnSXzbGBjVHMBx-lWlJ4ps_faK88iXuxomopYc0a7uWmBqAtOPWrp7GqlqvbF3v7b0SXDb6C6WtCVMwZzkzYK39NHc7NfDvFDirQU9K-BQeM0rziR9p9HR8C5YI20eVW6LTEQzdCwIG7LWvdvq-rp_YCDPgbVTvwH2cEwKXn8vO6CbvlnApaWqhbHK8rjk8jl-WiiFpgk_QYq9l4aCfW3mb2qxRRWrkA6dpt5VzNgo4XHioWF1a8Bnf0KPCnYhcMDBY1s63oV3_-GbdUWttkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح فروش فوری کیا اسپورتیج 2025 کوشا خودرو
✅
قیمت قطعی
⚡
تحویل حداکثر 20 روزه
📅
شروع ثبت‌نام:
یکشنبه 11 مرداد 1405
🕚
ساعت 11:00 صبح
ثبت‌نام و پرداخت وجه به‌صورت آنلاین از طریق سامانه فروش کوشا خودرو انجام می‌شود
👇
🔗
سامانه فروش:
https://sale.kooshakhodro.com/
📄
دانلود بخشنامه فروش
⏳
ظرفیت محدود است و ثبت‌نام تا تکمیل ظرفیت ادامه خواهد داشت.</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/677598" target="_blank">📅 09:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677596">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/231656c732.mp4?token=mGiGy-SEPdF1QaRUdaTVAu9_OC3VtxPPT16XGOkGv9_RSWoym7pX8aj7zG9id2osEvLdpYOBpXyT8FpmDW1CWtXBf9bD_sR0YZH31Azb9O9R_bRGEO6xBybLrl7r-WlyDsGYnQ08yJwVdngcIO-NeS9Q0BfL6YE37cQP5xMwFAAfpEJTHX0b1muvwIKnhlGux9etK4eXrFXI049X_0HC7ZC5jC6xEO_lzSPmfu0wtTGCbD4Z6nB6k0nhzEwvnGRV_06CQC5-Fk1CChxGrdO3gh4xryVICcgi0m8-b78zoJo3DTpCtu8c3VokepoH7C9b4vnYVorPthWd-CeIi9_nfl24OP0jxmW9RX5KmDg2oxcoWLkyMO65ts1yPw-may2GIpoaYPjhVic0jhwiFMwfS6FwqofdMDGulS2cjTf9abaH1q_ReMUcEiUbIqYJOhODbkDcEOnVe1lFZgcB9vI-eXR3Vpfra5N1NAIthmCGDY6Bmrqr6A_eggdFkqBM2Ij-wLucqdtV-WhF3KKkj-hMBHWiaj6pfiyj6D3Esgmb56HUzMmvOd4yJZNGFcW3EGJ8oxGwmBJSDWQQnB_X7mxXyR5v5Zh0UNqRN2FsvbxqFEFxc90LUifkXvt-tNUnwjcezI39Ad-0WBBKSMkyoEoeNAYigv7uMJsAxppyTDPcoLE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/231656c732.mp4?token=mGiGy-SEPdF1QaRUdaTVAu9_OC3VtxPPT16XGOkGv9_RSWoym7pX8aj7zG9id2osEvLdpYOBpXyT8FpmDW1CWtXBf9bD_sR0YZH31Azb9O9R_bRGEO6xBybLrl7r-WlyDsGYnQ08yJwVdngcIO-NeS9Q0BfL6YE37cQP5xMwFAAfpEJTHX0b1muvwIKnhlGux9etK4eXrFXI049X_0HC7ZC5jC6xEO_lzSPmfu0wtTGCbD4Z6nB6k0nhzEwvnGRV_06CQC5-Fk1CChxGrdO3gh4xryVICcgi0m8-b78zoJo3DTpCtu8c3VokepoH7C9b4vnYVorPthWd-CeIi9_nfl24OP0jxmW9RX5KmDg2oxcoWLkyMO65ts1yPw-may2GIpoaYPjhVic0jhwiFMwfS6FwqofdMDGulS2cjTf9abaH1q_ReMUcEiUbIqYJOhODbkDcEOnVe1lFZgcB9vI-eXR3Vpfra5N1NAIthmCGDY6Bmrqr6A_eggdFkqBM2Ij-wLucqdtV-WhF3KKkj-hMBHWiaj6pfiyj6D3Esgmb56HUzMmvOd4yJZNGFcW3EGJ8oxGwmBJSDWQQnB_X7mxXyR5v5Zh0UNqRN2FsvbxqFEFxc90LUifkXvt-tNUnwjcezI39Ad-0WBBKSMkyoEoeNAYigv7uMJsAxppyTDPcoLE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ترفند کاربردی برای نگهداری مواد غذایی در یخچال
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/677596" target="_blank">📅 08:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677595">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
رئیس سازمان امور مالیاتی کشور: مهلت ارائه اظهارنامه مالیات بر درآمد املاک اجاری عملکرد ۱۴۰۴ تا پایان شهریور تمدید شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/677595" target="_blank">📅 08:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677588">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba72b522c9.mp4?token=KHw_rTBEzRnQ9iGTKrmx3pP50xMsJY9WOFxawTjwI98UXaA4fvlOnAzLqBtneVCIljTLgxJTt2AQb6w1yc0v-y8jXlY_Mdg-Ut9fyQRM4mRZkT3rCqnTYghjVUHXZQG9niVh_0fZOhgIIfy7L5mGrOi5Wz9nRKPqtiiqIdIePLOIOB5bKXWzU8P0jnOuJ6Fry4KM9FRlwmO8Eq_pEqbcCcz-phyqeKdZZ7NsBhSr_wJ6JPn2eaCV3p-ilGSfZRhcFqE0-ytN1H4SFCl-JqmGsD89KsC6gdnCQSKhSR3dR2w8invmymjovzXzZLsopYYkds0GRawvcfh5JRZSn-ZHbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba72b522c9.mp4?token=KHw_rTBEzRnQ9iGTKrmx3pP50xMsJY9WOFxawTjwI98UXaA4fvlOnAzLqBtneVCIljTLgxJTt2AQb6w1yc0v-y8jXlY_Mdg-Ut9fyQRM4mRZkT3rCqnTYghjVUHXZQG9niVh_0fZOhgIIfy7L5mGrOi5Wz9nRKPqtiiqIdIePLOIOB5bKXWzU8P0jnOuJ6Fry4KM9FRlwmO8Eq_pEqbcCcz-phyqeKdZZ7NsBhSr_wJ6JPn2eaCV3p-ilGSfZRhcFqE0-ytN1H4SFCl-JqmGsD89KsC6gdnCQSKhSR3dR2w8invmymjovzXzZLsopYYkds0GRawvcfh5JRZSn-ZHbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات انسان‌نمای نظافتچی با کنترل مشترک انسان و هوش مصنوعی با دستمزد ساعتی ۳۰ دلار وارد خانه‌ها شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/677588" target="_blank">📅 08:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677585">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f0205d5.mp4?token=eUVu2AqVJW78VuWiVSRMalOVLMsEIEQXm6snbE3gJ9x3GmBnZHfnROaSwdLiosflsDHySYAm2wSjozDSsg84M1P18UckyTeQAR_-VNAjHhvukTgNhabpxzTG7fumlwSUyx1jRG7R0f4gSlpByUnTIKxzqB0TO6abpz5pCeZyFZHrRjjlMjEZSEzqtcqkmeBuZb2DNj8HMjE2tSiD7Ecyi5v-6-n598WYDe2N95YuIDuuIZb8yKopchQafGjkKOL4iIgVoGgXuSpvTRmiCTgZog0FyBCIW-mkltpJMfOvjE46Be9Zl-TE5pFP7lTWsLGDeyE6CaXLiMf2oAUUnxlQCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f0205d5.mp4?token=eUVu2AqVJW78VuWiVSRMalOVLMsEIEQXm6snbE3gJ9x3GmBnZHfnROaSwdLiosflsDHySYAm2wSjozDSsg84M1P18UckyTeQAR_-VNAjHhvukTgNhabpxzTG7fumlwSUyx1jRG7R0f4gSlpByUnTIKxzqB0TO6abpz5pCeZyFZHrRjjlMjEZSEzqtcqkmeBuZb2DNj8HMjE2tSiD7Ecyi5v-6-n598WYDe2N95YuIDuuIZb8yKopchQafGjkKOL4iIgVoGgXuSpvTRmiCTgZog0FyBCIW-mkltpJMfOvjE46Be9Zl-TE5pFP7lTWsLGDeyE6CaXLiMf2oAUUnxlQCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخلیه اجباری شهروندان به دليل اتش سوزی گسترده در ايالت واشنگتن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/677585" target="_blank">📅 08:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677584">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a987ea5b89.mp4?token=v9ptQJ4BoxpnoSJ8RA1fB7f5Oq2cAUWkD0KyTRh9r3lkg76AMP5J_8itmmC_YNfA4g0i1eBSty0KQLK0CAOVrwzg25srPDmsvBZsn2nucfFKB-0_9RmeSs4p1J5R4DaO4UTa-4W9QajYAXjA4s4F_XunN0neCH24ca-DCvrWUbiK4aEkSsBUYRjgTbYKB_uS3g75m9aMFSKo5U0zjLbsD2dkLe6DvQb5PD_IJ6QGO1ejk8_vMhFdIne3c_TltJqEudjgxcZ2Sf9FOdQ9w3ml6hZ4lvjlQv4uesvNxm3GrGUgHFePRodA7hV6WF4xjCrGBPkoSKs0-QVdm2WhhHnveA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a987ea5b89.mp4?token=v9ptQJ4BoxpnoSJ8RA1fB7f5Oq2cAUWkD0KyTRh9r3lkg76AMP5J_8itmmC_YNfA4g0i1eBSty0KQLK0CAOVrwzg25srPDmsvBZsn2nucfFKB-0_9RmeSs4p1J5R4DaO4UTa-4W9QajYAXjA4s4F_XunN0neCH24ca-DCvrWUbiK4aEkSsBUYRjgTbYKB_uS3g75m9aMFSKo5U0zjLbsD2dkLe6DvQb5PD_IJ6QGO1ejk8_vMhFdIne3c_TltJqEudjgxcZ2Sf9FOdQ9w3ml6hZ4lvjlQv4uesvNxm3GrGUgHFePRodA7hV6WF4xjCrGBPkoSKs0-QVdm2WhhHnveA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فقط با یه صندلی و چند دقیقه وقت، بالاتنه‌ات رو قوی‌تر و خوش‌فرم‌تر کن
💪
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/677584" target="_blank">📅 08:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677574">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E0xrgMdPCFfXuwCUUmjCgvEwk-ufVDDybDuSPFoYGysHCKJYm3nN0G5VctndL-V70tyY7oB5j9qUOictUSUhsWp96IP7B-HVW3b2EsQwL5t2RpaDUB6yr2GULIlmLzX9x8tb9hCwv8kO56enD3krcxxGqjnUgNcaDvwssRRDQEBKJqgQqK5oKFV9Z_8NJMt8r76O8TjNWFxUGmma4Klia6rird1gTIhPFxf9OiGaO10cNjwYcW6Tj8aMANR8yrUZGyTpGgvHGbJUfObTyZNBKoI3iE32Tv0NQoJfMcfioUL0S1MYGkulg1bQLvhswJJAD3AlrzR00_809PuG84xMSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z8hlhdIUHOdDxIR-bsATfHAzlaVtKdp7k0ZjLJ1zm4xnQ5kXgDT1D9ymfUzyFpO-aRiwj-Z21xhxUCtUCO7G55diviAMMP8Z7Od4v-I7vH_ILJu3dPy-5qOyD80ZiADsCZPmiVONl1DBKrROEbKaRxQmEiy2KMkGdIAg0FRHc3MaPCHwKy3Ef0JPwebr05IagsxS4Nik7mvrBap92ryE-EI4LceWB_NadvEl3k0NEIyX9PJk99fgDlf_TkAfXxIo7Vf9pokt_umisB7zIrmSJe2wU4GMWcOlHNH-c_-iUdxskb_nK3AiLkY-Iu_rkR6IGTgmALNUgWh6pUZbcxEa5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gIQI88XNBf0mt5Rm269pIrALENXg2TaTqj4Bq3Z9qZ4NdyKcP4KMYUnENgDxnVF7m8SJh_vJsHKBMCLgJW6vyA3UNR7rxlUMNlQJaJrdkVlK76iHf10-lhO_WI3RHCBm0_Rpo5fudy3Dz_pnxYySztx4GjbnVDXLWskKOSczzrM9uVM17CjssaxtOEp18c5DZ_VFf8IJcaP20w1vUiWNd1K7BqiAC_28VAqs7NaZBmIqk7cvWF2usQAfQO107HNCW4V1-z6VT5cwkzl2gkbTi6xEXxpIXCDmlUB7-ewH1UvB9K2Otf4rrZuWVJH_uqzq16zw48LdnuLVnPxi8zbNWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qS5mgFD9qSQAgibhozzn1MWO4EfV-vZxgAPWfFSaGD5ELrB_q0auU7WW-x5IS3Q86hNswpnL1KDiRaDmOsee7MFkpSOC0qD4CXkKdWrskEHsvPuaVNOGkuIHMk3YX77BXFZkPPW7t34RqWIeNBlO6a5uImp5RJd-TFjF3pjM7utjGaUEc0m2meT51uGe6LGdjFsNomN71-8jpQKESmInTiIlNrG-qs7OLVJEha5NWI8rMAkZRtKvh8u4wld6F3129QKs0_UolWeGciBiIZYP1LZ55KRRRk_auwjhyIG7E04hSn42he35fkK3CpVVtxYHBQcAgbL7r71zezWbexoP3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vCNTVAJxDH2s1MLl0uc9mrOZbEH0vVnoDnFEKERJ6UjNi2F93dh_i7vVGR-rPG5rvKjhDOnjjzG2Lk_aYCoRQR9z0nWSJ2ZP_FagbDnx9AkLlA3mQ9L01ZpPw1Liep6uCAdXgBu_PR5hwgO_HYdbexrVPPkQXj3ROz4tX6GltO-6f9Wl65Nq9uxFOYcaXoaW4skXDlIzR9YMJe_XPgpNALzpG98cwRuezntctki7NID5j7cMmKZ0F6Dbpg739KyD12ebvrFcXMlcryAvgFBMDn4WFUOFw3L4WDjQ_E4vpH38hL8SZCxbdDMh4-gRxNNpd2h6PQ7nEByjQBB4-w72DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VS8OIuxiypYDq-ah91Ab4sKhOluAw0H6I2h4ybW8pB--hpsF3HbrTIkFF89aGgA4cQz92yr3_pxHOBxkydTL3BiHB_0bH1ABPhrdXIyYz4aUmUusKrH3ab1C3fxGUY5S_mry8vAjjfBjwLZVoPMWHy8vUKIcKmccHmHzC542Ih4pLPhOfL9FhuP4THA11-FC0VUW3eI1xdrqoR_TL2uQti4OlJ0q7mAVlOoVNg45gXHmP-rNCaWrZdHh9ftpA-BL_sUIjZbNbzMOyyCWSJTRxJkkyLgZiVBeIY6wZ310y1U6aZFJ3YD0TkYr1Rv5R0NFK_ZrMUZlB7o-VNnQmyDoqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j1ag60hqz3kED4F6bMDjuUxR4aqYIk_A_nSjbnfb6Sgk3Wjd4ACE4UFqKcEVTHMaUnipWEQ8CVJMW3364hDU824qp-VC06WYAB4oyhEgj9MiGnaNemMF1vNLqoZiSrEbJa0Y5AYNWnhNUN1EZJdZH9COz9wqIpyHOdXX-0V1v9CXDwsityqELr1MYTlUvtxqLh4fRGvE-aRdD0rUQR-IfJqqXpeU1wfW1WB6zoEdAMxp5Vcx7N-uRLuPSEuwx5IvK7GAxBF8rSWFNFnLGAvlg4cyQ57P07G6C_I0IL8vYOsCjvDquqAkuYEXp47z2tpH2nloCGLkpFrlga4iLmkddg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gYWE-gIeqGwkdXHzBi8X-L1m07-Qiv_r2FZMduQJWuplBDYwAM19_tCpCZKCK71G3YO9K-zR7G7W1pcMV2XhgGeF5aykNY2C5QfwNM1EFycOpsaBqVKaPETvqZgBpczWupIa8VF4dhlGtSLOtATllULSuVLpdY9FGttZtHEYwc6dk1fglKO_YYUU3dCZZGpPLHzjIVN0JtAM0jdptYMHZjfeRur9xQqAh6LDGLIVqzcu6zny4DALq84Pa_gPNl0U6OzU_x3l0Cvfiovf3luoQu4fa4KitJMYENT4Py9Wjm-PwdqCuvXCTHvmanULaFNmT2-FbMis6FUuJ0QMNi1vAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTD8V4-lNO8cISMZQPpRlxZNqDEEbzcKkpSQTe8N72rRmJatiqRCfcG-FG2MV6uL1TtaDNHSf0F2physDFbPq4OGwpWFzrYUdfUg1G_cn7lWOqWkN_5Uue7bcuz8PhkpYzWs-IhqyiOyEBsDcpkzwENqO9S8rMXMOdeRy8QCqXOlHs4rR5fjgOXivjkXbMwJ1rP0JTBw2m3nMcjLQgExFfEUqmspp3sm4iCyiZpRk9W5bWtp9mVSslR6lC8zb8E9iNxvDdstI8KXaUF9ZYykFAwxFi1pb7ksTVTJTfA3vbhXNNse-XIQhJWkM-7fDG3B7VBkh-rRaSDGNhkC2jTxGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1997XKkmBsOp9D-5yIBFqW5ol6kCFk3HDXLGLouF9RronSlq7-ma0t_nKec_M3wF76wBG0V60ANyL4YGJ6Dj1OC116VZ3lu_n1E4BFjs9KZ8_70sQUKWRK__UiUR7Ev1m2DRx_tCDx6D67ERgFn-U4K80aPmoe_nwsiaEoGeFC0DBMb4An_EDaOG4csU3NgYDU1k-YQwqNL2Qc0cV1CksOYutxsJ6bUCDBoVGR0libOFIB76YRYpZ8uxHkPAtYpRPq4LSdUhYb2OXhHjCxvazuZy85Lj1woCgV3tnVDBlf-L9nthUiiK3SpyeUJrQkN_b4aRnt9ggWQfV6YgYvO3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با دانستن چند ترفند ساده، می‌توانید هنگام خرید میوه؛ شیرین‌ترین، رسیده‌ترین و خوشمزه‌ترین‌ها را انتخاب کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/677574" target="_blank">📅 07:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677566">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f86c80e059.mp4?token=j_S6xzKTX8PLsYLpfGMLwo3I0Bcjyj2qrbpKNd02ydFau_pCZ4lK9IODCM15JYkggyrRUGitHqNdS9e918tIROn-4-nqS5cmvcxymC53UreSO4iOJs4HL2ZCCE3lGC0st2alyNVXjeyMzBw5Fj8Vw0GyPVjFJeR6H5u6Q5KsiieSR4GFCEN7hMiOnJi5EJmMdiBqc4AnxXW9jXsj-OkxSWl2fkTAQIOc_msrJdpaAeacJun8zvuD7GttcipdFQ49HxZL6d4Ru0HwdQ6HutHoZKJH1pDo6pSG5u0xyQA_Ff0MXLrEZfGlVFv9_jfNxelVAm6jaduDR3BDL4cj7wVh5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f86c80e059.mp4?token=j_S6xzKTX8PLsYLpfGMLwo3I0Bcjyj2qrbpKNd02ydFau_pCZ4lK9IODCM15JYkggyrRUGitHqNdS9e918tIROn-4-nqS5cmvcxymC53UreSO4iOJs4HL2ZCCE3lGC0st2alyNVXjeyMzBw5Fj8Vw0GyPVjFJeR6H5u6Q5KsiieSR4GFCEN7hMiOnJi5EJmMdiBqc4AnxXW9jXsj-OkxSWl2fkTAQIOc_msrJdpaAeacJun8zvuD7GttcipdFQ49HxZL6d4Ru0HwdQ6HutHoZKJH1pDo6pSG5u0xyQA_Ff0MXLrEZfGlVFv9_jfNxelVAm6jaduDR3BDL4cj7wVh5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان آتش در شرق واشنگتن؛ هشدار تخلیۀ فوری صادر شد
🔹
در میان وزش بادهای سهمگین با سرعت بیش از ۷۰ کیلومتر بر ساعت، آتش‌سوزی مهیبی شرق واشنگتن را درنوردید و هزاران نفر را مجبور به فرار از خانه‌هایشان کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/677566" target="_blank">📅 07:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677565">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggyaFHQzrp9gzTTXTTHX9xulpd6vqA_hxr6SA1w81G3rw__sDeKlzSyVx_DH5J5yrI7oyVyNSI2H1sa8FZqysNQTX8jZa4YTzCWRGckxldPuh5L0hDCBKdaXPAcQK7Y_k3H0tEcAgPpZazs7gr6KjVdGlatBIZGVgMBC3phntJtjiV_0zL1TOllPoT91fha-AnjIy-OX4iAkX9KmT5njyvgAaZmy_6mFZKuEOiamhx6XHaMUgjipxhwzvbyweoSAHidfOrB_KCwB50NwuV0axMzpiho55P0Sqs3Nhxa4mars0dMzIoZPMy3Uz_TK9877ala7qPQoeoZ_eJWloQ5tHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران، مظنون اصلی حملات سایبری به تأسیسات آب ۷ ایالت آمریکا
🔹
ایالت میشیگان روز شنبه اعلام کرد که ۹ سیستم آبی این ایالت هدف حملات سایبری قرار گرفته‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/677565" target="_blank">📅 07:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677564">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست کافئین | فصل‌دو،قسمت‌ده</div>
  <div class="tg-doc-extra">عین القضات همدانی</div>
</div>
<a href="https://t.me/akhbarefori/677564" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
🔹
عین‌القضات همدانی
🗓
در این قسمت، بزرگترین کلاس درس تاریخ را برای «پرداختِ هزینه‌ی صراحت کلام»، «شکستنِ تابوهای ساختاری در اوج جوانی» و «حفظ اصالتِ درونی در برابر سیستم‌های مسموم» مرور کرده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/677564" target="_blank">📅 07:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677563">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cc1795597.mp4?token=SRqp3NxO9w_IOI5x_wzi1ypG26PfiuFn1VVlYe9MB5XMyiyQWR4o-zUY-M40GKEIwfwOhJnvytZflpe4tRIWhwmTdM7DAAsJbceLTXCR-ixjTXZ1qubREvJj1KDPnoDNGTxuGJO_nPu-4FeVCgQGYqLsjvY-OvcjIxwV6y7j68zDhtOCzSt5jla9gYXAX8yJV7OCcrbCAaBfxxDQtHIDyFdLAJvQfxrW1cZrftmZeYR0f0MUamUofQZndZ5KaxpWWHN9__PZ3FlkdsdvJaolZAHslgJK5MXQ0F_wFTU4iv1FCJGujbasDki3zi0VUu48EjSHU5x4Zsun5MC_Y55wpLOPtc5mzR9Fij-JfY88SIoAdNZQmOAxPlznV5gomyXkyjtljch9Z62Otb3u31c3rHzh60mbyqmcZ6w2T-6jf8jb7oQakJCTnlKuTRQBBnm37WtV3n81ENICZGeyy5Koa9pzy-7o-LNY-3ySMcLnvCjOAL4CRFJyKRIHALbWJTvv1GAsoDOVFaD8QbCivGu-mAGIDeu42DDlUfQj6Ipd-YaA2Y_Dm7_s9QuPW0TPqzfjq8pRwRlFxp9IqEWZX0jXtFxMaikj5pq2FLSBZzGnb7u7ncPoCcVDnMl15AHRqzfS4xgcgAklPU4ziHKrmciCZ9zmW_LiYsa9XDwAqwiJ2g4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cc1795597.mp4?token=SRqp3NxO9w_IOI5x_wzi1ypG26PfiuFn1VVlYe9MB5XMyiyQWR4o-zUY-M40GKEIwfwOhJnvytZflpe4tRIWhwmTdM7DAAsJbceLTXCR-ixjTXZ1qubREvJj1KDPnoDNGTxuGJO_nPu-4FeVCgQGYqLsjvY-OvcjIxwV6y7j68zDhtOCzSt5jla9gYXAX8yJV7OCcrbCAaBfxxDQtHIDyFdLAJvQfxrW1cZrftmZeYR0f0MUamUofQZndZ5KaxpWWHN9__PZ3FlkdsdvJaolZAHslgJK5MXQ0F_wFTU4iv1FCJGujbasDki3zi0VUu48EjSHU5x4Zsun5MC_Y55wpLOPtc5mzR9Fij-JfY88SIoAdNZQmOAxPlznV5gomyXkyjtljch9Z62Otb3u31c3rHzh60mbyqmcZ6w2T-6jf8jb7oQakJCTnlKuTRQBBnm37WtV3n81ENICZGeyy5Koa9pzy-7o-LNY-3ySMcLnvCjOAL4CRFJyKRIHALbWJTvv1GAsoDOVFaD8QbCivGu-mAGIDeu42DDlUfQj6Ipd-YaA2Y_Dm7_s9QuPW0TPqzfjq8pRwRlFxp9IqEWZX0jXtFxMaikj5pq2FLSBZzGnb7u7ncPoCcVDnMl15AHRqzfS4xgcgAklPU4ziHKrmciCZ9zmW_LiYsa9XDwAqwiJ2g4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عین‌القضات همدانی و جسارت بیان حقیقت
#پادکست_کافئین
| فصل‌دو،قسمت‌ده
☕️
🔹
اعجوبه‌ ۳۳ ساله‌ای که نشان داد وقتی یک مغزِ مستقل و جسور، خط‌ قرمزهایِ منجمدِ سیستم‌های متعصب را به چالش می‌کشد، چگونه می‌تواند با طغیانِ فکری‌اش خواب را از چشمِ حاکمانِ زمانه برباید؛ حتی اگر بهای آن شمع‌آجین شدن و مسلخِ جوانمرگی باشد.
🔹
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://youtu.be/hwciVLCsnpI?si=Sn7kIHdYXQ8FWRVS
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/677563" target="_blank">📅 07:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677562">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHvn1hoy1_qI04jev1SUQrv_uRu6-V3TD_Zlar1x_h2MWMDjhRnRQkUvBata08qgMXpJwCG2DQzZ5E4YNnbrOOCS7sFBv82FFfymiAJ9JksxirEkCoQvRHPv5QPE3ZnHfBGpRAAuyxnBN8Ufm_TFHo3HjqhKsKq_j3OxWBcsQwcv0WfArtZs_lr3GSt30vPotldbYfycJOoDTxLNtEWMup0w4YakG2R9n9HOMPLbVhK9IVBfogK8xdalp-nPkVZbeqfcGx063dwAllHHTqmS21E5cdoUA4dBuC93r1GIh068y0o0chtVml67CQfLx1hmPl_nWAMsczM-0rY0JJijPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۱۱ مرداد ماه
۱۸ صفر ۱۴۴۸
۲ آگوست ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/677562" target="_blank">📅 07:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677561">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ادعای
منابع خبری به نقل از مسئولین نظامی: ادعاهای تروریستی رئیس‌جمهور آمریکا مبنی بر اینکه ایران خواسته است حملات را متوقف کند، صرفاً یک دروغ جدید و یک تلاش مذبوحانه برای باج‌گیری از حاکمان خلیج فارس و تحت فشار قرار دادن آن‌ها با تهدید است
🔹
چه او به تجاوز خود ادامه دهد و چه از آن عقب نشینی کند، نیروهای ما در بالاترین سطح آمادگی قرار دارند و برای هر احتمالی آماده شده‌اند. اگر مواجهه اجتناب‌ناپذیر شود، میدان نبرد تعیین‌کننده خواهد بود و در آن زمان، همه خواهند فهمید که چه کسی قدرت را در دست دارد و چه کسی کلام نهایی را خواهد گفت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/677561" target="_blank">📅 06:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677560">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ادعای المیادین: تعلیق حمله آمریکا به ایران پس از تلاش‌های جی‌دی ونس، معاون رئیس‌جمهور، و رئیس ستاد ارتش آمریکا برای منصرف کردن ترامپ از این کار صورت گرفت
/
موضوع کمبود ذخایر موشکی عامل کلیدی در تصمیم ترامپ برای تعلیق حمله به ایران بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/677560" target="_blank">📅 06:44 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677559">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flb3iM0STzAChgJJLrdcwCa7J8AS_i5wtrrpi3bGfGLKaUeEbkQ69R56yqjbVREAcoBSTnDjG1M_cbHhZVcKcEtz0B4BNLKA9PO-wadv9VEIVJrTtgGQ4MlZag62httEfCMQ7BX08tSs4uJ-Sp0MNNrcpA6HMhk5GmkcCGwtJ86AYks77iNyfZp89HvQVh9rQlzZDPrSFXnlT6daaWAFbkPdubqTh5hp74aLPQlzneUPyQaEt2txCnUKfPcfa3oIL-orbavaiG-dgiv4aK96NtKz1od-qs3egB7lI9JwhTYxAE1dLSHg9UlONkS8_ap0zaBNkG8swgQbIcXmhPuvqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای خوک هار: من با لغو حمله به ایران موافقت کردم
ترامپ:
🔹
ایران و دیگر کشورهای خاورمیانه از ما خواستند پس از توافق بر سر چارچوب‌های یک توافق، هرگونه حمله را به تعویق بیندازیم.
🔹
این توافق شامل بازگشایی فوری، کامل و همه‌جانبه تنگه هرمز و پایان دادن به تهدید هسته‌ای ایران خواهد بود.
🔹
با توجه به این درخواست، من موافقت کردم، به نفع همه جهان و همچنین برای اطمینان از اینکه ایران موفق و مرفه باقی می‌ماند، حمله را متوقف کنم، مشروط بر اینکه توافق به‌سرعت حاصل شود.
🔹
ایالات متحده در آمادگی کامل رزمی قرار دارد و برای اقدام علیه ایران آماده است.
🔹
اسرائیل به شرط دستیابی سریع به توافق، در پایبندی به لغو حمله به ایران با ما همراه می‌شود
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/akhbarefori/677559" target="_blank">📅 05:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677555">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRBwzgwXzY7nQyxv4nD9Ggja7izOt4NXSj-kvQ5B8vkGyfc3pwsn05iloVo9X-XBrPrJ_oYl35sjAXboaR7gp5tZZDbhW3hcxhMIn8F1dPvYxyGmQI_1b_Ykz3p_AKAFl8PljR9sBcO5QNm2dYFWj1hL85o3CidzTi0k3wgqO-J_CldczigUUOodyh2uNPXrmcyLMUXy-kXcuRVIQdZnh2XVTC9QMw9d7vvJYTJOh7mwW4C0-oE6fx6R1H5X4ctQ_cohFkm_hEnkvOFtmXoP8h5Q20maQfFoV_gLJbXOO0d_CbOLMdXOLoowmvK30mrLp9Ed7zJaqmQCfCnjAHnhcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیست و نهمین پست سگ زرد در ۲۴ ساعت گذشته
🔹
دونالد ترامپ در ادامه پست‌های رگباری خود، تصویری از جلد مجله نیوزویک درباره ونزوئلا را منتشر کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/akhbarefori/677555" target="_blank">📅 04:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677554">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ادعای اکسیوس: میانجی‌های قطری روز شنبه در تلاش برای دستیابی به توافقی جهت بازگشایی تنگه هرمز، به‌طور جداگانه با عراقچی و ویتکاف، فرستاده ویژه کاخ سفید، و مقام‌های عمانی گفت‌وگو کردند
🔹
به گفته یک منبع آگاه از این مذاکرات، این گفت‌وگوها پیشرفت‌هایی داشته است، اما هنوز مشخص نیست که این پیشرفت‌ها برای کاهش تنش و مهار بحران کافی باشد یا خیر./ انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/akhbarefori/677554" target="_blank">📅 03:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677553">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ادعای آکسیوس: بن سلمان، ولیعهد عربستان سعودی در گفتگو با ترامپ نسبت به طرح آمریکا برای حمله گسترده به ایران ابراز نگرانی کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/akhbarefori/677553" target="_blank">📅 03:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677551">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
ادعای رسانه‌های امریکایی: در پی درخواست‌های وزرای امور خارجه ترکیه، قطر و پاکستان مبنی بر آمادگی ایران برای برگزاری جلسه‌ای در ژنو، سوئیس، به منظور ادامه مذاکرات، فرماندهی مرکزی ایالات متحده به طور موقت به مدت ۴۸ ساعت، عملیات شبانه خود را متوقف کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/akhbarefori/677551" target="_blank">📅 03:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677548">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d85ffc549.mp4?token=oY9jtBKzwMDQFRjw1zYQD2-tYs98oL-5JMRkeMY1L-L35Lrat8JJOrTHvm72PsDlpFfBo1OVxpVGXS3E9QmZ6MaAXKUaFVe6zNRlXvvEpBfb0Ls1Lhe_e2tmzkYhkfaOo6_o1YrC9_MXrzP341pZpZCrMC9f5ecnPY5rAOec0ReI9eehk44KTCvhoh8qrxsYq_eurRgosbCupxlSaIq0-7gVGOkXG5vt3UwtTo_jhGRZqOnXxx9StfTZS22c7fAuiyJEvGk-e7KRHf9IWUrL-R3SmKzPleMGJdQaEHFddFgrhHxXmvTVz0ig4Yqpy9u3BGDFCrCXGVUlBqb51BFfbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d85ffc549.mp4?token=oY9jtBKzwMDQFRjw1zYQD2-tYs98oL-5JMRkeMY1L-L35Lrat8JJOrTHvm72PsDlpFfBo1OVxpVGXS3E9QmZ6MaAXKUaFVe6zNRlXvvEpBfb0Ls1Lhe_e2tmzkYhkfaOo6_o1YrC9_MXrzP341pZpZCrMC9f5ecnPY5rAOec0ReI9eehk44KTCvhoh8qrxsYq_eurRgosbCupxlSaIq0-7gVGOkXG5vt3UwtTo_jhGRZqOnXxx9StfTZS22c7fAuiyJEvGk-e7KRHf9IWUrL-R3SmKzPleMGJdQaEHFddFgrhHxXmvTVz0ig4Yqpy9u3BGDFCrCXGVUlBqb51BFfbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ستون دود برخاسته از مقر تروریست‌های ضدایرانی در سلیمانیۀ عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/akhbarefori/677548" target="_blank">📅 02:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677544">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌ شدن صدای انفجارهای پیاپی در مقر تجزیه‌طلبان تروریست در سلیمانیه عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/akhbarefori/677544" target="_blank">📅 01:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677543">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgS7JgROEyJ3UxTlziKDA4m7fKwHK_GMxh4nYD6A8BFbwpw5-_A14CzqiIvkt6SxC-TYp8l9jEuo6UH6STa5BEXg5m9fXNRWTCYm14ypa2AXyQtrYYOMZoOjLtEvLhOwf7ORT68lDCOhvU9CJlQPSWlNOkNCDFjUA1rCFTZKMfdhXmHxJ7ZlHxdH-S5JBdXK-LTRWBmzjmfN0x9kgeRNJMnK2JlXcsc1C1af6S1-1W_SsIkb5AQkaDfn_0ADElD6asv3vMjyAKOTBPs5iYvS1BeEW9BHuyIGxj68lKf_XTB43h98tX6L8g6YWWzL59wedQmeAotK8vuqTZrT7bbIKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/akhbarefori/677543" target="_blank">📅 01:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677540">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
هشدار رئیس کل دادگستری گیلان در خصوص کشت مواد مخدر در روستاها
🔹
رئیس‌کل دادگستری استان گیلان با تأکید بر برخورد قاطع و هوشمندانه با جرائم مواد مخدر، نقش دهیاران را در پیشگیری از کشت مواد مخدر کلیدی دانست و هشدار داد در صورت اطلاع از کشت این گیاهان و عدم گزارش آن، با متخلفان برخورد جدی و قانونی خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/akhbarefori/677540" target="_blank">📅 01:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677537">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">40 Rooz</div>
  <div class="tg-doc-extra">Mohsen Chavoshi</div>
</div>
<a href="https://t.me/akhbarefori/677537" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
۴۰ روز
🎼
چاوشی
🔹
موزیک جدید چاوشی به مناسبت اربعین حسینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/akhbarefori/677537" target="_blank">📅 00:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677536">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDRA1vdwii2NE4Egh4LI4G-tKc2ZLajNeZTPR_lDMgzBiGpmzTTyFRSD1xyHuVnOCGd2fRTxFw0nKXBPKsXyPXITiVJE8mPUjq_xzZJUtDg9_J2NgPq4ho6tsxOpoaJe59tfUNavFWl5DM3u3eiNhfUFJGh18FmQ-AOq4voEZkaN4JjyhIvkCQotkjfL769jk666IFYKs0FUTMt-oua-CUU1kxdtOWYuU98r-St4PXIi7p5IM8O955lbJQeljW-40etB-oIrLlgfmK52W40WOs4HYmTKtrqVhbsUhOMo3NyxQNQC9mm2VWVaq8XFAtZ1QOaMnre12-XNY4FJwvewFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت خارجه: تداوم محاصرۀ دریایی و حملات به اهداف نظامی، غیرنظامی و زیرساخت‌های ایران، مصداق «عمل تجاوزکارانه» و نقض منشور سازمان ملل است و ایران از حق دفاع مشروع خود استفاده خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/akhbarefori/677536" target="_blank">📅 00:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677535">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtVXEL0pDbX6YM5B5JM0ryxA6zrBXA34OCVP9vqfWrYIB00iAvha-7K4-Ru0Ba_jv9qLQvdlDu-tSbdSjpVXCU_iX_lBCDEbFEkstJqZ-D2fvUGPlZt9i1bfTbdG80ZrD3fKXaSyXFFmvLSiKkTHGCSQ_JfGyw6PikobN2FzElaWIaVSaKTKnRoNLAmUeFe4cNz9NovS1KP3BWYDtAllFK12apqqp-Dq2Dw32c2dH2D47tHz7rp1UmrFCzi4CWs-GwoThGUsGk7s9Tn0hC5h-junnx30luXE9B8qXRgZDAuP-JcmPDW2llFb3KB3e9mHS9cU9WmckcRsNk_XfB44bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تجاوزکار می‌بایست با تابوت برگردد
🔹
طی روزهای اخیر تب جنگ در منطقه بالا گرفته است و به نظر می‌رسد آمریکا قصد دارد بار دیگر دست به حماقت بزند. آمریکا اخیرا برای شهروندان خود در منطقه هشدار امنیتی صادر کرده است اما با این حال به نظر می‌رسد این هشدار صرفاً محدود به شهروندان آمریکایی نخواهد بود و در صورت تکرار خطای این کشور فراتر از شهروندان تمامی نظامیان و منافع آمریکا در منطقه و حتی سراسر جهان نیز در معرض هدف موشک‌های ایرانی قرار خواهند گرفت
🔹
هشتصدوبیست‌وپنجمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/akhbarefori/677535" target="_blank">📅 00:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677534">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf3TMCj2DuLiu1YuqWHMyB5XKAveI19nbSDStKmmd-h1lYL_Q6ASeBzpGn77uCtRUTBjt7bdceXi40T9InCNkpaCNHdc1fxQCQBnYc_t6jPbAAwzvMrRu5-gbwOFI0yUhh0sSDmuO0bImK0Cr989sQ_IfaExq82xL1HjyIAWVUos5zm-uioMS65gAlcWammf8AIi0thLYKDsucjdPKkZwcMUvYPifFqBHBTEiV3KHKwEXNLTzqTEF1ZTuyNF4lg7Hv-oTi8U6ZUd3GroL4q2BmqH6E6vlgUqsvEPJajGAaNbUAa71--Xa2MIsGxLBnXoJjY0avCMFys041YupEL4Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعداد هواپیماهای سوخت‌رسان آمریکایی در رژیم صهیونیستی همچنان در حال افزایش است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/akhbarefori/677534" target="_blank">📅 00:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677533">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIXZ76Jt2R0nJ6SdLEw3-0IJ3tgUzpmheI2Hr49s0GJ4gpfyAm2iUeG8xnusCYoAHGlcEXuNO9cwe_AlNgVQJ7Li4VIGN8dPhL8h032YLS5F8tPOkaw5LX8aEjFGN4_b6nO2pc0tZW1QfbwHdkaqvOduXNn3CbJF7iutmfvTcKfwkyzVNUN7kH8PaxO43a0XFoaQHNbl1DBQWazAdnvJbibLzcHzLAEbNaqQyFBSIkb9i62uHPaJNFaPuuZak9kGHCeSnP98o9v3b24GrWmXUVq_LrsBNKW4B-N2K24j2SKnbzcuVST0nJAWboDeZGB-MXF1k6FSz92eK_S5hzN9hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دو سوخت‌رسان آمریکایی از فرودگاه بن گورین برخاستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/akhbarefori/677533" target="_blank">📅 00:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677532">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mq4RhFN_8xrTXSj3Pbwh7AaFPpGnvM-eUKtVSWblsL09fubDEHaLuqpnsBfL8pyIqSsQ4HxnkpNDa6x8IvxIsaDdeFEKxlOys2sucR7y4XwzA2qTABfIIjk1dDZ91VjptdiX-equtZT1W-il-qSzMw3pPvj2e28gkAV6jnVOu0G0d5JxEGLBXQ4bfrNyk5j0QFeRdrGXp3eeJ9-3Db_jV_y8vf5rmybTm7F4gfPkb58KqqI4SW_fEJj0QNFvp5ExHaxldfdRWneUt6ToKv66cCTMupDicHfQkwfvV5Xsq3V84S-l6WE1JdPMFHKWgAsYjhMu3K6pioUAenkfGWb-pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک هواپیمای شناسایی آمریکایی (آواکس) از پایگاه شاهزاده سلطان عربستان برخاست
🔹
براساس داده‌های ناوبری هوایی، دقایقی پیش یک فروند هواپیمای آواکس آمریکا در آسمان عربستان به مقصد یمن رصد شد.
🔹
آمریکا این هواپیما را از سال‌ها پیش برای جاسوسی هوایی و به عنوان رادار متحرک طراحی و استفاده می‌کند.
اخبار لحظه‌ای جنگ
👇
khabarfoori.com/fa/tiny/news-3234810</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/akhbarefori/677532" target="_blank">📅 00:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677530">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
کاظمی: برنامه‌ریزی‌ها برای بازگشایی به‌موقع مدارس انجام شده است
وزیر آموزش و پرورش:
🔹
سال تحصیلی جدید در شرایط فعلی، طبق برنامه از اول مهرماه و به‌صورت حضوری آغاز خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/akhbarefori/677530" target="_blank">📅 00:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677529">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چند پیشنهاد جایگزین برای گران کردن بنزین
اسماعیل حسینی، سخنگوی کمیسیون انرژی مجلس در
#گفتگو
با خبرفوری:
🔹
افزایش قیمت بنزین در سال ۱۴۰۴ نه مصرف سوخت را کاهش داد و نه وابستگی به کارت اضطراری جایگاه را از بین برد. شنیده‌ها حاکی از آن است که دولت دوباره به دنبال افزایش قیمت بنزین است.
🔹
پیشنهاد جایگزین این است که ابتدا باید سیاست‌های غیرقیمتی و عدالت‌محور اجرا شود. انتقال یارانه سوخت به کارت بانکی متصل به کد ملی، صدور صورتحساب الکترونیکی، توسعه سبد سوخت و توزیع عادلانه یارانه انرژی می‌تواند فعلا راه‌گشا باشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/akhbarefori/677529" target="_blank">📅 00:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677528">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3af1f4879.mp4?token=TE80ialzJ5eakYfzxrunulnId8naxacv-BkB7fLYPJ_tUqmKSDolB1eBm8a5XhRGIWroBoDhhMmIoAPLBVnmYFyiV0XNn0sYanttr4sZQxHSGUrLer_fSmzaJQw8hc-DrTveNNVg-dFUhqGqA0t-1ulSYykOaTpvtaxTaScxu51biUhyXVZLbBFqtSeP76WuoJaEh_4PyPvlvLtcVGzITljPldPkf9wSQvYgU_tYw2WcafgVnwLb1rS9Eb3xpUss9DocrK4Uoy3LFXfCO9RAnv7WoDomXdZYF1wN5hYwP9cP095h4tJ0lpBX9ZEare5_RQ-xwvt2YTAKk_mamtszzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3af1f4879.mp4?token=TE80ialzJ5eakYfzxrunulnId8naxacv-BkB7fLYPJ_tUqmKSDolB1eBm8a5XhRGIWroBoDhhMmIoAPLBVnmYFyiV0XNn0sYanttr4sZQxHSGUrLer_fSmzaJQw8hc-DrTveNNVg-dFUhqGqA0t-1ulSYykOaTpvtaxTaScxu51biUhyXVZLbBFqtSeP76WuoJaEh_4PyPvlvLtcVGzITljPldPkf9wSQvYgU_tYw2WcafgVnwLb1rS9Eb3xpUss9DocrK4Uoy3LFXfCO9RAnv7WoDomXdZYF1wN5hYwP9cP095h4tJ0lpBX9ZEare5_RQ-xwvt2YTAKk_mamtszzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه‌ای که سوژه شد؛ شکستن صندلی کنعانی‌زادگان در میانه مصاحبه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/akhbarefori/677528" target="_blank">📅 00:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677527">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66cf7e52d7.mp4?token=Xpi18RNH83g7ZafRstbJY62pzEhF33qMKjMrKmjPZW3x1zrqkFeWRSrWRBopX86-XMk2W9lmaQAMOwYHr9BtQ02uUamChwY7tkMd0TyyPEs8Xq-tsfyigXiSmWtfW3_e_bYlPeI5OYdBbsB9DKrYqz1Hg7TM6r4nWrxCdAsp-Ww8LiF_aqQvwXGEtuUd5ExyQeL6Gd3AzlsJyqx2YW7QVRJsxw0Bks5UIU00P3cOlSVM4WOnv9Y4L-Pc20UhRq3ApjlY1Dwp9ij3235OdDEIMlePmqTyKs8k4eVWc8vPOl-JXEAGEKyPRk7QptcJ0pzypMBquDrsI_X8e9IdLk7UGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66cf7e52d7.mp4?token=Xpi18RNH83g7ZafRstbJY62pzEhF33qMKjMrKmjPZW3x1zrqkFeWRSrWRBopX86-XMk2W9lmaQAMOwYHr9BtQ02uUamChwY7tkMd0TyyPEs8Xq-tsfyigXiSmWtfW3_e_bYlPeI5OYdBbsB9DKrYqz1Hg7TM6r4nWrxCdAsp-Ww8LiF_aqQvwXGEtuUd5ExyQeL6Gd3AzlsJyqx2YW7QVRJsxw0Bks5UIU00P3cOlSVM4WOnv9Y4L-Pc20UhRq3ApjlY1Dwp9ij3235OdDEIMlePmqTyKs8k4eVWc8vPOl-JXEAGEKyPRk7QptcJ0pzypMBquDrsI_X8e9IdLk7UGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رنگ‌های اصیل ایرانی؛ هویت بصری ماندگار در هنر و معماری ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/akhbarefori/677527" target="_blank">📅 00:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677526">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVXaagVgm5wyGmqob0_iZs_yrdtHeL1PCk20g0aq-iAu4wuDlhYCmNjrkikLmGLFK2fsVPLtJ_6dee6kE2ubIggeGnRMch22UnN14_cisced3G6-cgqdlrwTYsgI53dRWrLIG6bseCoOIzBJx7nB1Jzm34ZNWi56GDrs8V0CInewD9WqH8qmRD982Z67D5_L7bP4e8Js_f0squyMxXEWttFN02FJgC1SCisTqpBS4JQRmXBgMV__tSa_sY5RY4_5UwSqwr3p8IjlsB1FdggQ0R3MfXNllQTkGOIh5jbYv_f9iz5RCGP_ZvnBCTat9gJSvRPfgngxEQYAfGxeWC3E6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
هدیه سفر کربلا برای ۱۰۰۱ نفر از عاشقان حسینی؛ زیارت آقای شهیدان به نیابت از رهبر شهید انقلاب
✨
‼️
کافیست عدد
۲
را به سرشماری
۳۰۰۰۱۱۵۲
پیامک کنید.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/akhbarefori/677526" target="_blank">📅 00:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677525">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ادعای المیادین: اطلاعاتی وجود دارد که تأیید می‌کند گروه‌های تجزیه‌طلب برای انجام عملیات علیه ایران، از خاک عراق، در حال آماده‌سازی هستند./انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/akhbarefori/677525" target="_blank">📅 00:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677524">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8de4ff1be5.mov?token=l7FU43D-ZT66ZShEC8qDBojgIjcuhsgnhgKSXoJ_MvfV3gEFkAkxx88PYikCQ0trxnY_kzs7ZBDcfrj47GOsTFLf1av7OAWBclqirQ2GSQXp4E8F94IoJFGuxHJvVu8eBO5hyzsjezR-LpU-6x9F1HQ7inNbE7ZPhLE7MckOmIW4I1v3O0jacY6SVIfnBML04okssImsw4PKve2hQ63JOYrH9ccSEhlc_fdOKNQ-IuFYRHFhAsN2c3cPqoI64IVV9PYKvxmjZY78pDNM-oAk40KAYLSst2G2-oS2lxfAl7HqvTCovfmWfZF1qjr3NRez5Mz1wuBW_c46fqcP7Ilmcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8de4ff1be5.mov?token=l7FU43D-ZT66ZShEC8qDBojgIjcuhsgnhgKSXoJ_MvfV3gEFkAkxx88PYikCQ0trxnY_kzs7ZBDcfrj47GOsTFLf1av7OAWBclqirQ2GSQXp4E8F94IoJFGuxHJvVu8eBO5hyzsjezR-LpU-6x9F1HQ7inNbE7ZPhLE7MckOmIW4I1v3O0jacY6SVIfnBML04okssImsw4PKve2hQ63JOYrH9ccSEhlc_fdOKNQ-IuFYRHFhAsN2c3cPqoI64IVV9PYKvxmjZY78pDNM-oAk40KAYLSst2G2-oS2lxfAl7HqvTCovfmWfZF1qjr3NRez5Mz1wuBW_c46fqcP7Ilmcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم اکنون|یک بمب در محل جشن تولد ژنرال الکساندر چایکو،فرمانده نیروی هوافضای ارتش روسیه منفجر شد
🔹
چندین فرمانده نظامی روس کشته یا زخمی شده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/akhbarefori/677524" target="_blank">📅 00:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677522">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffPRpWRoS_FpV3aBwYvH_83pJTph6gitqX0NyasyCuIhwV5q6m-1nchpAs3TTAY2-u6VO9T1uic6KpxzHEMJrqs5Tk09O8RJXMch_DrUu8-ti-DpPeStHbIsO2uqJzSRMjZRh5wT0i33tqqpDJ8LbjKmHYatiF84UchTag6VKY65r2GkaJ2GX_vkUWKDkMaqDnmC4YkWjtdtsKhshHowjtUikYojIxazDLDnYQm9npdD8Vq0phdrcJiEQFhb6dcZ1L8e6nkuSmGXOqVTdP7InGuZL6qU9pke51QXHxp1NJA7ZJh0M5Vo4FNFrHeXoK97WGRlIaM38i0Yb47TPnmt8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/677522" target="_blank">📅 00:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677521">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
جزئیات تازه از احتمال حمله قریب‌الوقوع آمریکا | نتانیاهو: دروازه‌های جهنم را به‌روی ایران باز می‌کنیم
👇
khabarfoori.com/fa/tiny/news-3234810
🔹
جنگ ایران در پیشگویی باباوانگا پیدا شد | او از چه گفته بود؟
👇
khabarfoori.com/fa/tiny/news-3234757
🔹
هدف از حملات احتمالی آمریکا به ایران چیست؟ | مدل جنگ عراق تکرار می‌شود؟
👇
khabarfoori.com/fa/tiny/news-3234815
🔹
افشاگری تازه مشاور پیشین احمدی‌نژاد از حمله به محل اقامت او + ویدئو
👇
khabarfoori.com/fa/tiny/news-3234644
🔹
ماجرای درگذشت فرمانده بسیج شرکت ملی گاز ایران در مسیر اربعین
👇
khabarfoori.com/fa/tiny/news-3234640
🔹
با نصب اپلیکیشن خبرفوری، از خبرها جانمانید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/akhbarefori/677521" target="_blank">📅 00:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677519">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چرا ایران با هیچ کشوری قابل مقایسه نیست؟
🔹
آمریکایی‌ها در مورد ایران اشتباه فکر می‌کنند و معادلات خود را به غلط چیده‌اند. به اذعان کارشناسان غربی ایران با همه کشورها فرق می‌کند. چرا؟ در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/akhbarefori/677519" target="_blank">📅 23:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677516">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
باج‌گیری ۳ هزار میلیاردی ایران اینترنشنال از مدیران بلندپایه اقتصادی کشور
رئیس پلیس امنیت اقتصادی فراجا:
🔹
اعضای یک شبکه سازمان‌یافته موسوم به «باج نیوز» با جمع‌آوری اطلاعات شخصی و خانوادگی مدیران بلندپایه برخی صنایع بزرگ، به دنبال اخاذی و سوءاستفاده از این مستندات هستند.
🔹
بسیاری از این اطلاعات فاقد اعتبار لازم و ساختگی و دروغین هستند.
🔹
این شبکه تلاش می‌کرد ضمن تخریب هدفمند مدیران و فعالان اقتصادی و اخاذی از آنان، در روند سرمایه‌گذاری کشور اخلال ایجاد کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/akhbarefori/677516" target="_blank">📅 23:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677514">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
یک مقام آمریکایی به خبرگزاری آکسیوس گفت که ایران در روزهای اخیر بسیار تهاجمی عمل کرده است و برخی از مقامات آمریکایی از میزان آمادگی تهران برای تشدید جنگ شگفت‌زده شده‌اند
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/akhbarefori/677514" target="_blank">📅 23:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677512">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بدهی دولت به تامین اجتماعی ۱۲۰۰ همت شد
احمد فاطمی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
دولت حدود ۱۲۰۰ همت به سازمان تامین اجتماعی بدهکار است. در بودجه ۱۴۰۵، پرداخت ۲۷۵ همت از این بدهی در قالب اوراق پیش‌بینی شده که دولت تاکنون آن را پرداخت نکرده است.
🔹
بهانه‌ای برای عدم پرداخت بیمه بیکاری وجود ندارد و سازمان تامین اجتماعی باید از هر طریق ممکن و از طریق خط اعتباری دولت و بانک مرکزی، بیمه بیکاری را پرداخت کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/akhbarefori/677512" target="_blank">📅 23:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677511">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
تماس تلفنی عراقچی با فرمانده ارتش پاکستان و وزیر خارجه ترکیه
🔹
عراقچی در تماس های تلفنی جداگانه با فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان و هاکان فیدان وزیر امور خارجه ترکیه، ضمن بررسی آخرین تحولات منطقه‌ای، درباره پیامدهای اقدامات تجاوزکارانه و بی‌ثبات‌کننده ایالات متحده آمریکا و خطر تشدید تنش‌ها و ناامنی در منطقه گفت‌وگو و تبادل نظر کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/akhbarefori/677511" target="_blank">📅 23:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677510">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff1e3182e6.mp4?token=EHajlRnrCqS-86phKRJ6y70BfXdowIxB-5MnOJb7-WvpycppOGTskwmac8EN8vmnIcyKKmrNWORS6aPENHXnaAuqIZKPx0AQFnhZW2z99fHdYYF8lK1AP8Li0iWodHxr52KBQ-o1KvwlNeHjml2cBeJ-lpZjOxepjNzA-lc0F2qEjQ6BT7OnXnhB9kQCQ5ak48uPlSMSVyUpuu1ctlw0IbYZEkfMGhrypXu8wimASG7HxkGtv5TLZ_LG-Mp7ptN1Z5yWotdROjbfqRQCTOs2O6yAZxKH2mWKj8pkB-CdxEbA5t45-OkFrCh3TpNjMa83RQuaa1HK-8v658JO4zd8BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff1e3182e6.mp4?token=EHajlRnrCqS-86phKRJ6y70BfXdowIxB-5MnOJb7-WvpycppOGTskwmac8EN8vmnIcyKKmrNWORS6aPENHXnaAuqIZKPx0AQFnhZW2z99fHdYYF8lK1AP8Li0iWodHxr52KBQ-o1KvwlNeHjml2cBeJ-lpZjOxepjNzA-lc0F2qEjQ6BT7OnXnhB9kQCQ5ak48uPlSMSVyUpuu1ctlw0IbYZEkfMGhrypXu8wimASG7HxkGtv5TLZ_LG-Mp7ptN1Z5yWotdROjbfqRQCTOs2O6yAZxKH2mWKj8pkB-CdxEbA5t45-OkFrCh3TpNjMa83RQuaa1HK-8v658JO4zd8BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع سیلاب شدید در هند
🔹
بارش شدید باران امروز در شهر ایدار، واقع در منطقه سابارکانتا در ایالت گجرات هند، موجب جاری شدن سیلابی قدرتمند شد و خسارت‌های فراوانی به اموال مردم وارد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/akhbarefori/677510" target="_blank">📅 23:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677508">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0cf2384e8.mp4?token=JiZ_aZkfyJ-_3C-brg2JH7hRECTLG4qIJ4rTOYEn6qF89Tavhi41dCSVJCmV80JHGffynY77mBSl-OJ-1AnI3wA6CayaQviI_Ckmjxot7MyDIsbOjRExcMEfm_aw2Yq3uCkXPpieLXqMvVtpMbeaJq0k48yjGLCFO0N2zhRskPcH8QU5NBIm3dc0C7Q1MrbJe6o6aWDPjo3PnWneq_WI9slA_YcW41ONAQMVak5RPEu8VaNPywG_wuyjX7vw2LwkE81wkdKxskLp5TK4eDurxRcOXKcoW_kvDzKt0yKBNAo4LoSCbtKrSBIZMkBx8Szrm5fIpSw_3-d5YRmwG1-FaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0cf2384e8.mp4?token=JiZ_aZkfyJ-_3C-brg2JH7hRECTLG4qIJ4rTOYEn6qF89Tavhi41dCSVJCmV80JHGffynY77mBSl-OJ-1AnI3wA6CayaQviI_Ckmjxot7MyDIsbOjRExcMEfm_aw2Yq3uCkXPpieLXqMvVtpMbeaJq0k48yjGLCFO0N2zhRskPcH8QU5NBIm3dc0C7Q1MrbJe6o6aWDPjo3PnWneq_WI9slA_YcW41ONAQMVak5RPEu8VaNPywG_wuyjX7vw2LwkE81wkdKxskLp5TK4eDurxRcOXKcoW_kvDzKt0yKBNAo4LoSCbtKrSBIZMkBx8Szrm5fIpSw_3-d5YRmwG1-FaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متکی: یکی از استراتژی‌های آمریکایی‌ها این است که ما را تا آبان یا به مذاکره، یا این واسطه و آن واسطه، یا به حملات محدود و غیرمحدود، مشغول کنند تا به آنجا برسند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/akhbarefori/677508" target="_blank">📅 23:14 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
