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
<img src="https://cdn4.telesco.pe/file/rbPGknbRdlXdLSZ2BQX0xP_IHZ1WdynCiMUtgv0oVGdE2m3g2iuQ0oEaqfjWm1NzJErwKEsrX3b3itLmkHU3Eri96G4ZhDU06X4GpAXirPI0G2dHD0-mspK1VXCjvwOAZCpy_goSUyXNNWizai1-f1pdpsFTVPlfNbpDNH7wK9_h7cgxQIE-DTA4v0DVAtoP6lxBOa6kWYZoBRZnMEyCwb3_pY2y1umWpbiW_oGBC-S3M-9awsalzi5dCSFDaHJCOF7M3_XnyiZ2Xvjq7FQXND8WCnLBEo6aeMjLR0GgNlaYD-OcJM1BvpHiCpAsrb9ED-g8mg_8XpEiHHe41JPTsw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.06M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 22:49:51</div>
<hr>

<div class="tg-post" id="msg-691035">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
عضو ارشد انصارالله: عربستان خواستار میانجی‌گری ایران شده است
🔹
پیش از این سخنگوی وزارت خارجهٔ ایران تأکید کرده بود: «انصارالله بازیگری مستقل است که خود تصمیم می‌گیرد؛ نه از کسی دستور می‌پذیرد و نه نیابتی دیگران است».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/akhbarefori/691035" target="_blank">📅 22:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691034">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
وحشت ترامپ از افشاگری رسانه‌های مستقل
🔹
ترامپ جنایتکار، در اقدامی خلاف قوانین بین‌المللی ورود خبرنگاران شبکه‌های خبری سی‌ان‌ان، ام‌اس‌ان‌بی‌سی و وبگاه پولیتیکو به کاخ سفید را ممنوع کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/691034" target="_blank">📅 22:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691033">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0510776e2.mp4?token=TYML69b1P0eubrf6Yy1HRWMS8PrUYI0W3ZCE4nAhAP0W6sSCioOvoW4tKKsaA_ZRmcNEygm7rvOcGjr8SMkgMCI9IN8K_Lw0LIvZP1gh541f6odFGsJJpgAx0DOevs4XiA3a36iv1I6aBsoQ5Voj2rmWeCXHUC5pkSPcD0iYV0iHPSeX_7Vqa2UrQ-7WBKR_x1RCjnbSxTmqJzXjLXCO4RxVVa258Mf9CRO09lAKebEuTJuGKhFav3JUPbGqq0pRUft60gCyXIcR1i9sdaOeCSGwmKTE6lxxLNL2eoka0i_o4Y_1u1qnmLGEmV8C7_8flHAr2c2QwiZtWeFTwzsU3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0510776e2.mp4?token=TYML69b1P0eubrf6Yy1HRWMS8PrUYI0W3ZCE4nAhAP0W6sSCioOvoW4tKKsaA_ZRmcNEygm7rvOcGjr8SMkgMCI9IN8K_Lw0LIvZP1gh541f6odFGsJJpgAx0DOevs4XiA3a36iv1I6aBsoQ5Voj2rmWeCXHUC5pkSPcD0iYV0iHPSeX_7Vqa2UrQ-7WBKR_x1RCjnbSxTmqJzXjLXCO4RxVVa258Mf9CRO09lAKebEuTJuGKhFav3JUPbGqq0pRUft60gCyXIcR1i9sdaOeCSGwmKTE6lxxLNL2eoka0i_o4Y_1u1qnmLGEmV8C7_8flHAr2c2QwiZtWeFTwzsU3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معطلی رانندگان بدون امکانات پشت مرزها/ اینجا منطقه آزاد نیست، منطقه آزار است!
🔹
نبود امکانات اولیه رفاهی و معطلی‌های چند ساعته در صف‌های کیلومتری ترانزیت، روند عبور از مرز را برای رانندگان خودروهای سنگین به کلافی سردرگم تبدیل کرده است./ تلویزیون اینترنتی مدار
گفت‌وگوی کامل در یوتیوب
👇
https://youtu.be/qJni4yP2kbU
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/akhbarefori/691033" target="_blank">📅 22:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691032">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4168e38cac.mp4?token=m99kE59F_Avhdf3SoczCY4lTJaXZWvG4gE4BamF3F_a59MDnW9GBU13SKXBl7S4RFm0PiHPtavit9Zv14Tsuji3WBY655823siDbYaED261UdtBRNgTJHJNiyZ0DR1VdToUTZ2JZagDlwyTaSMABN6nPOtf-BVJ5jpz7cCjQIR9AqdnF_caRPaGdTbyJATmKc0XtVV1BdY2ujlPm7FQzfXIHuy4M1evVIaS5jlYsKZgeYa7xgcyca8H3t96xCnnoskzS14Fi8gvt16_ZC1xz52es9a_MIgI6daxorGXWBWXv3Fjjh-p3OzOYK5WzR9J9gGyZUu7VUai6F4Q_IsAR4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4168e38cac.mp4?token=m99kE59F_Avhdf3SoczCY4lTJaXZWvG4gE4BamF3F_a59MDnW9GBU13SKXBl7S4RFm0PiHPtavit9Zv14Tsuji3WBY655823siDbYaED261UdtBRNgTJHJNiyZ0DR1VdToUTZ2JZagDlwyTaSMABN6nPOtf-BVJ5jpz7cCjQIR9AqdnF_caRPaGdTbyJATmKc0XtVV1BdY2ujlPm7FQzfXIHuy4M1evVIaS5jlYsKZgeYa7xgcyca8H3t96xCnnoskzS14Fi8gvt16_ZC1xz52es9a_MIgI6daxorGXWBWXv3Fjjh-p3OzOYK5WzR9J9gGyZUu7VUai6F4Q_IsAR4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درد دارو
🔹
صدای شما از چالش‌های درمان؛ بازتاب مشکلات و سرگردانی بیماران در تامین داروهای حیاتی.
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
#درد_دارو
@Alo_fori</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/akhbarefori/691032" target="_blank">📅 22:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691031">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ادعای واشنگتن‌پست: تعداد بیشتری از نیروهای نظامی آمریکا در جریان جنگ با ایران کشته شده‌اند، اما پنتاگون این تلفات را به‌طور عمومی اعلام نکرده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/akhbarefori/691031" target="_blank">📅 22:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691030">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmFI_i8AVuOz-lco_HUObAGuPdCB2ATa_OFBr_0XhjCSbLckchbjGHiI_y9ccanIwcJGdVPugyfOogJLhVt-bbs2jX5pWYobmJUrriPCyvNwhsIu5J1_XV77KbRnVa2PcZRIM7TxpCtWr_oEFoVvUSwKunG0gxiRh9VBjRIytxqR70AeEQZzIGIoy-M1C0Ggdlaka9TMWUWgw7Wvk4zdUw1FscPtuOXFqc1P077GzshR-3ZuwryuRwYis9mo6VtpSkHp_Mc5vl33XV3IMN68u0vgnE3ShHf8-zsDB4OO8Udc7Cql81CRVieLjgrbMZxem8dxYVcYlBDxhHLhKRFPjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازار اجاره جنوب تهران هم دیگر ارزان نیست؛ بررسی ۱۰ فایل منتخب نشان می‌دهد حتی برای واحدهای میان ‌متراژ هم مستأجر باید با ودیعه‌های چند صد میلیونی و اجاره‌های سنگین دست و پنجه نرم کند
/ تیتر تجارت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/akhbarefori/691030" target="_blank">📅 22:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691029">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20dd4c53c0.mp4?token=ls9ch3fIkyNmR6_TWSOLG-pBETU20n5l7xQrwj1Qk0h2x9booFKrtd9ybhHGV-g04lznUnNknixTQXkDo6QsWRtU5QocrPOOFreiAnWWoZXsa0pk8Plwkvhca0xBRmpZPbBLjjTxL_gCl9ujm4efpn60p89fsmW_Yl5TyjHFk0bTL74J5_y6UucrXih8Fz-kX5i8GzpqNWu3HlVMWX9tBNB4XYQHfFW5C86vPuCXPdcEFx9WvWCMjule4MBsqf2JZ3CvhuJ1Wfa-eyZAaAcOHrKraZJqqpYQGxumt1yVX1jsCw6NU3Orh0wN-bo1ACpIZIm32_2ZjPsTehsqFl1rBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20dd4c53c0.mp4?token=ls9ch3fIkyNmR6_TWSOLG-pBETU20n5l7xQrwj1Qk0h2x9booFKrtd9ybhHGV-g04lznUnNknixTQXkDo6QsWRtU5QocrPOOFreiAnWWoZXsa0pk8Plwkvhca0xBRmpZPbBLjjTxL_gCl9ujm4efpn60p89fsmW_Yl5TyjHFk0bTL74J5_y6UucrXih8Fz-kX5i8GzpqNWu3HlVMWX9tBNB4XYQHfFW5C86vPuCXPdcEFx9WvWCMjule4MBsqf2JZ3CvhuJ1Wfa-eyZAaAcOHrKraZJqqpYQGxumt1yVX1jsCw6NU3Orh0wN-bo1ACpIZIm32_2ZjPsTehsqFl1rBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایش شجاعت جان‌برکفان در رزمایش هزاران نفری جان‌فدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/akhbarefori/691029" target="_blank">📅 22:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691027">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oi62KwyDVzPpbilyshTSrDcnH9HKLuCWzz9RMHUw6EWInV8Lx91bMTrw1muVV4VJ4xxhlPiBYlma0uoA-apjbytvsldv1W4R8Zr9dwmh3zlNidOdpUsK-4QfhYHP4NY4Xbb8XJISpV8RCZkzqc9CcCEgESEHfUl5vWJ5rAvysXwTSBymTrE3UcaRS0LGV8yo1w1CUhRq9llCpUI-JAj8xsFSJ9T3T3wM_d858m1GO2iWMSXmrSf8Nw-By-LBbofy_hh-r85h4GxtCAIqhr4uF-ePqAM8rF2CfZ9J4O-eAwOxtf7KCBpvACEtCThaWxY_ivaFuHe9GnMhZ3f5a9sL7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQX3aXswWaNE2i7euBDWOtX_s8m-KXVEcfxBjj6JYuG0s_79X2o-VAjwRGqQ8bH4D0ZqaIun6ZcbEeHjqkhP8GD1EejeDd0N9P9Hx-51dJd3g8HlL6SMtTVwcgJNcLnqTVsujdL2K69D9GcXHkzDYmY_l0hxpUUnHxvqMhatJLmJI-VL-2mOKoZRq1E_-V13cU7GLrhk2wjTPhL_APJF-xFoBJeaCw7GKoMXcE-EJcTp9oCpw-n29LAIodi-hR0TcmU10YtkESBS9C1gDKhqLceSY81zlAVQlMUcERf0x5zGEzN4JPcyRsaMqDMkD1-DeBKDIIjwIlrD8scMjbL0uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">میزان خرده‌فروشی آنلاین و کالاهای تندمصرف در سال ۱۴۰۳
🔹
آمار انجمن تجارت الکترونیک تهران نشان می‌دهد «زیورآلات، طلا و مسکوکات» با ۴۵۰.۷ هزار میلیارد تومان، بیشترین سهم را از میزان مصرف خرده‌فروشی آنلاین در سال ۱۴۰۳ داشته است.
🔹
پس از آن «لوازم خانگی برقی» با ۲۸۹.۶ و «مد و پوشاک» با ۲۳۸.۴ هزار میلیارد تومان قرار دارند.
🔹
در بخش کالاهای تندمصرف (FMCG)، «خوراکی‌ها» با ۹۰.۸ درصد سهم مطلق بازار آنلاین را در دست دارند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/akhbarefori/691027" target="_blank">📅 22:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691026">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
پوتین: روسیه هیچ برنامه تهاجمی علیه اروپا ندارد و آماده همکاری و احیای روابط با همسایگان اروپایی خود است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/691026" target="_blank">📅 22:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691025">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7R9oqY-FcLTZ4Fe5S9vOmC0kFtMuD7KqFal1ttSTn9aAYVXqioc8PjgJi4fpP587Z20lvtF8GLBBat22ZTlwjsRWiB7SwkmCDOnNZ3FLsTr8V_hcN9ZpCnaLCCNnp_p6nFNbEX_evGFZkpRDue9bXDA3LREijz8r9Fbl5rSOc4rJnKBCerW3ygZkDAJFuraKfLzVO6IsMV5tp__DKa3_0mGnO6WVkvMVIKMImD1LAftYOLT7NerIbAvhPgpcAHyE1CwIuOatnXPDG8_0yqk2lW0MQRKRmzkQiLwNndUKNNqxSoKv_ylWa85_mrbbs6evL5T26dnebzNUdDw89NcSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بوریس جانسون: عمران خان در زندان کوچکی در پاکستان در حال مرگ تدریجی است
🔹
بوریس جانسون، نخست‌وزیر پیشین بریتانیا، با اشاره به وضعیت عمران خان، نخست‌وزیر سابق پاکستان، خواستار استفاده بریتانیا از نفوذ خود برای کمک به آزادی او شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/691025" target="_blank">📅 22:21 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691024">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac7470020.mp4?token=kN68K7qcT02f1VZRbWbP-h8FSOEeAFhqRYiZxVEyWH-JBnvu7YLGnwb_7ULHLwM1T33XHV7OwS6B4lAzvDQPMdGeOaFeepykKkT4uqKnhj-0KhBYcJqwO9aV9dpKRlHEovAoBCpcXm_mZSUIs1SuRLnudcmQB513AvZDKprSOX2OXwugJwhIjKcikBaz5ZzD4S21zKrGG4VPE-5ebTMCdbAlsCbZPQhxpTiU80XrxtL1_VPuyxouHBMz9s0Ny5szaIuloYXD75IX6akdBeE2cyGHih-WLeS4vu3BKWLqh_pkiZY2sYqHDpq2KhYucyWX6GpIvwnC_WA5Idg7cQ066g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac7470020.mp4?token=kN68K7qcT02f1VZRbWbP-h8FSOEeAFhqRYiZxVEyWH-JBnvu7YLGnwb_7ULHLwM1T33XHV7OwS6B4lAzvDQPMdGeOaFeepykKkT4uqKnhj-0KhBYcJqwO9aV9dpKRlHEovAoBCpcXm_mZSUIs1SuRLnudcmQB513AvZDKprSOX2OXwugJwhIjKcikBaz5ZzD4S21zKrGG4VPE-5ebTMCdbAlsCbZPQhxpTiU80XrxtL1_VPuyxouHBMz9s0Ny5szaIuloYXD75IX6akdBeE2cyGHih-WLeS4vu3BKWLqh_pkiZY2sYqHDpq2KhYucyWX6GpIvwnC_WA5Idg7cQ066g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیرترین موجود زنده جهان؛ کوسه گرینلندی که ۳۹۰ سال از عمرش می‌گذرد/ متولد شده قبل از نیوتون، موتسارت و داروین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/691024" target="_blank">📅 22:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691023">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a4994b7f7.mp4?token=TNgK5O_DscgLJKgwMqb3qtpPb-qKeZb4Mh2Q6Ibm9tgUaVFWmHiqSl_eelsjODINWFbfDrL3BEY69xVxDy2OJGUSCJGg8TcMLaobRocYlbqi6UxHNNcGeMmxZcc2vpSAromUYVc2IIRpZMVLsmhWcH6aZLQJ0U4Pq-5sqK-NeU_EContiWXLtapVz3kERXEN28pFcvnTJ9TuC7T3rMTpAjjq1-yPW0OLHtWvtXpMFZCztyw4p-_aYTnPXxhY9ZCee0ZiDn2pjhiFb2K5gOFaNYNmim_TYQh3bhoq6QxSpOH26XHI2r7ZX4otFjjsrf5Vp0Jk3Twp-SmTdXVbty0fwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a4994b7f7.mp4?token=TNgK5O_DscgLJKgwMqb3qtpPb-qKeZb4Mh2Q6Ibm9tgUaVFWmHiqSl_eelsjODINWFbfDrL3BEY69xVxDy2OJGUSCJGg8TcMLaobRocYlbqi6UxHNNcGeMmxZcc2vpSAromUYVc2IIRpZMVLsmhWcH6aZLQJ0U4Pq-5sqK-NeU_EContiWXLtapVz3kERXEN28pFcvnTJ9TuC7T3rMTpAjjq1-yPW0OLHtWvtXpMFZCztyw4p-_aYTnPXxhY9ZCee0ZiDn2pjhiFb2K5gOFaNYNmim_TYQh3bhoq6QxSpOH26XHI2r7ZX4otFjjsrf5Vp0Jk3Twp-SmTdXVbty0fwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لبیک یا خامنه‌ای
🔹
اوج همبستگی و وحدت مردم در رزمایش بزرگ جان‌فدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/691023" target="_blank">📅 22:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691022">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1-v3wbGYG-trDD2BF2Q_stJy2AQLGhYDtFIJpe2mfmqmiczkZQv-6-UFbrgUuVfLsjD2t1ebg_26y9wi6jo-Bm43CMr-qvfJqHHz9LcKA0DR4fFN1A0kM6k9pO2gq0WZwv_ocedjdm288zaa18ARwHfx3uRmviuq9rJlk2IpDQ1FuRX2Y0nNVFNoR8Ubk22xVOLDjiyf-0S1JOdXLPlQb3JI25bBeYBTCwibDHcZcPcTWlI-tok5Rs5QXY2wjHSWeWPELCsKIbb5IpqGTVP1Ef0sPRZQWZNa3vf91aN5idRBNz2c1oOjrSlwxqchiu-M_Wc1mTKv0cHXqxgulDDcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای مضحک ترامپ: محبوبیتم در جمهوری‌خواهان ۹۵ درصد است!
رئیس‌جمهور تروریست آمریکا:
🔹
میزان محبوبیت ترامپ در حزب جمهوری‌خواه اکنون ۹۵ درصد است که یک رکورد محسوب می‌شود. رونالد ریگان با ۸۶ درصد در جایگاه دوم قرار دارد. متشکرم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/691022" target="_blank">📅 22:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691020">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
تهدید به «فرستادن به استخر»؛ زیدآبادی درباره مرگ هاشمی رفسنجانی: فرزندان هاشمی مدعی مرگ عمدی پدرشان هستند
🔹
زیدآبادی: اگر مدرک دارند شکایت کنند، وگرنه تکرار نکنند، حالا تندروها هم همین را می‌گویند. یک طلبه روحانی را به «فرستادن به استخر» تهدید کرده. قبلاً هم در زمان ریاست‌جمهوری روحانی، طلابی پلاکارد داشتند: «ای آنکه مذاکره شعارت، استخر فرح در انتظارت!»
🔹
یعنی مرگ عمدی را قبول دارند و دیگران را هم تهدید می‌کنند؛ اگر قوه قضائیه قصد بررسی این موضوع را دارد، این افراد را احضار کند: اگر مدرک دارند، پرونده تشکیل شود؛ اگر ندارند، باید بگویند چرا چنین ادعاهایی می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/691020" target="_blank">📅 21:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691019">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ادعای الجزیره به نقل از یک منبع آگاه آمریکایی‌: ۶۰ میلیون بشکه نفت ایران یا نفتی که احتمالاً ایرانی است، در نفتکش‌های تحت تحریم بلاتکلیف مانده است
🔹
واردات نفت ایران یا نفتی که احتمالا متعلق به ایران است توسط چین، به ۴۴۰ هزار بشکه در روز کاهش یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/691019" target="_blank">📅 21:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691018">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمرکز اطلاع رسانی بانک صنعت و معدن</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6ec2409e.mp4?token=kNa41A0aZhWPPz8bXRfg1cKSN74XdnOf9IZMQQh1v0ApY0tNc9ISOe1otPfAk_oJqiLVgumIgms6886FLkTupfU_uUmki1hLKoSvcFU6q6sigXMjdK272D60oNZIyrLSD20bkV-nZyvESKkMPEMqXqDPd5uC8e3-x4rk-5eNnq7odDOsfjePPwO57Hp95-1ukVvaCn6bdCyTjfve50g3EnaaK6OfPJvPEEKl7pvJBi-Tby4NK2R78vuF8tEuMF_igyd8LDEvqL2nhfEYYnwAAFGynYLWeNOl7AvEBMd2dMDg4HUQCuIxj6TfcuqZFwDp_faTY68kLtT8dhHYtV9m0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6ec2409e.mp4?token=kNa41A0aZhWPPz8bXRfg1cKSN74XdnOf9IZMQQh1v0ApY0tNc9ISOe1otPfAk_oJqiLVgumIgms6886FLkTupfU_uUmki1hLKoSvcFU6q6sigXMjdK272D60oNZIyrLSD20bkV-nZyvESKkMPEMqXqDPd5uC8e3-x4rk-5eNnq7odDOsfjePPwO57Hp95-1ukVvaCn6bdCyTjfve50g3EnaaK6OfPJvPEEKl7pvJBi-Tby4NK2R78vuF8tEuMF_igyd8LDEvqL2nhfEYYnwAAFGynYLWeNOl7AvEBMd2dMDg4HUQCuIxj6TfcuqZFwDp_faTY68kLtT8dhHYtV9m0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دکتر
شایان
:
بانک
صنعت
و
معدن
طرح
توسعه
واحد
داروسازی
فریمان
را
به‌تنهایی
تأمین
مالی
می‌کند
🔹
مدیرعامل بانک صنعت و معدن در جریان سفر به استان خراسان رضوی از تأمین مالی کامل و یکپارچه طرح توسعه واحد داروسازی دانش‌بنیان فریمان توسط این بانک خبر داد و اعلام کرد: طرح توسعه این پروژه تا پایان سال به بهره‌برداری می‌رسد.
▫️
در راستای حمایت از تولید، بانک صنعت و معدن متناسب با سرمایه‌گذاری مجری طرح، مسئولیت کامل تأمین مالی طرح توسعه این واحد داروسازی را بر عهده گرفته تا بر اساس برنامه تا پایان سال افتتاح شود.
سایت
|
بله
|
تلگرام
|
اینستاگرام</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/691018" target="_blank">📅 21:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691017">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7586235fd.mp4?token=Gf9fjwTkbNCf8yNzcWwNDUdQrks-Syi73HoyN0ZKZixJiG3tgQofqZbFhbaHOFjYyCNEbpG3v-Gu6GWxEKeo8gy-hmG0czkypxdgRhG8mfRFsGHogAVrWHhQZX1Ru7fMhNK6eeKUF1BUyZHYKCKTZhWin1SLFV4VsDod0DymcYkFf-e2NSVS_DM9EY8NZzARtwe0gZNwqyamtT6_g4dvLBn2SXUNCUBaOyhH2UUnvGOr2-mnIDUs2qDo2LH5dr2wY8-NgIBaRII14A551-49ny7UXhVrtJLXj8iKlqi8OCPzCrjGDEnA9fjtU6mLQgowcDn86Qkp0ZBTlfyVi79J6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7586235fd.mp4?token=Gf9fjwTkbNCf8yNzcWwNDUdQrks-Syi73HoyN0ZKZixJiG3tgQofqZbFhbaHOFjYyCNEbpG3v-Gu6GWxEKeo8gy-hmG0czkypxdgRhG8mfRFsGHogAVrWHhQZX1Ru7fMhNK6eeKUF1BUyZHYKCKTZhWin1SLFV4VsDod0DymcYkFf-e2NSVS_DM9EY8NZzARtwe0gZNwqyamtT6_g4dvLBn2SXUNCUBaOyhH2UUnvGOr2-mnIDUs2qDo2LH5dr2wY8-NgIBaRII14A551-49ny7UXhVrtJLXj8iKlqi8OCPzCrjGDEnA9fjtU6mLQgowcDn86Qkp0ZBTlfyVi79J6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این تنظیمات رو یاد بگیر چون باعث میشه با گوشی سامسونگ عکس‌های خلاقانه بگیری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/691017" target="_blank">📅 21:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691016">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار آذربایجان شرقی(Admin)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d741aca11e.mp4?token=lPlEHrMs2OU0jt1k8S_jBlsVqzXDjrNNSI0yLyVLjc2LcMFYar2eebxsOJdW3mwAYfQ-ZKHbyI3m-c3ShJZGdX8S-2PAmFolmcyUMEZaGF1GIATfGQKxCep1URJp-iOF1xrGnP-2ALMkTFJuLPAeM8T5pRFGNmoL8CbBzjJ7OooYSPYX9znIcPz2cvvaooceZSzj6d3g7Z7Z_8foIBYNe6PR_Ol1BeL-HafLziWSqXeeE4Q9BSEdpnj0CPzz58DwduB8KThKBMRK9XWT-29HkJ-GmYZXoCW68hQaBEEGpKnFtOFY-7w8xDUfLVJfpMGvQ7cuADP-fTDrMM9T8Bxo9oeI-BzFvs0inmd9ZWD8_rhDSK2tukK9QDXTLhvny3Iz_DMb9i3fslBe6zWwu7ZvxQGn3XautWDIlJJZUpAQDtrnpLth8U7PQLj_b0swsAaLi-pRd_KcLl4nZDPoU0Z3m3GPi9K2FjCv20AE3XtLmQweS3jO4JIbqPjzK0VE5Luvhyj3zI-B4SqCALclTiCgKgt0h-N5aA7HyQH3q80dPpeDWvUClt6k7pnKkrxXmkrIXu-UfOrfD-K8oLkpiJ1LlbQ5LG5kduvg2ACIjQjz62u71W7Z5yGYeBu4x6gycxbjffpOnB63rrh2aMkkuQOI3pdS-nyDa7yfuQd247EbRJU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d741aca11e.mp4?token=lPlEHrMs2OU0jt1k8S_jBlsVqzXDjrNNSI0yLyVLjc2LcMFYar2eebxsOJdW3mwAYfQ-ZKHbyI3m-c3ShJZGdX8S-2PAmFolmcyUMEZaGF1GIATfGQKxCep1URJp-iOF1xrGnP-2ALMkTFJuLPAeM8T5pRFGNmoL8CbBzjJ7OooYSPYX9znIcPz2cvvaooceZSzj6d3g7Z7Z_8foIBYNe6PR_Ol1BeL-HafLziWSqXeeE4Q9BSEdpnj0CPzz58DwduB8KThKBMRK9XWT-29HkJ-GmYZXoCW68hQaBEEGpKnFtOFY-7w8xDUfLVJfpMGvQ7cuADP-fTDrMM9T8Bxo9oeI-BzFvs0inmd9ZWD8_rhDSK2tukK9QDXTLhvny3Iz_DMb9i3fslBe6zWwu7ZvxQGn3XautWDIlJJZUpAQDtrnpLth8U7PQLj_b0swsAaLi-pRd_KcLl4nZDPoU0Z3m3GPi9K2FjCv20AE3XtLmQweS3jO4JIbqPjzK0VE5Luvhyj3zI-B4SqCALclTiCgKgt0h-N5aA7HyQH3q80dPpeDWvUClt6k7pnKkrxXmkrIXu-UfOrfD-K8oLkpiJ1LlbQ5LG5kduvg2ACIjQjz62u71W7Z5yGYeBu4x6gycxbjffpOnB63rrh2aMkkuQOI3pdS-nyDa7yfuQd247EbRJU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهریار را همه با شعرهایش می‌شناسند؛اما پشت این نام، زندگی‌ای بود پر از انتخاب‌ها، دلتنگی‌ها و اتفاق‌هایی که مسیرش را برای همیشه عوض کردند
🔹
از تبریز تا جایی که نام «شهریار» ماندگار شد، قصه‌ای هست که خیلی‌ها فقط بخش کوچکی از آن را شنیده‌اند.
🔹
این ویدیو، روایت کوتاهی از زندگی مردی‌ست که شعر، فقط بخشی از داستانش بود.
۲۷ شهریور،روز بزرگداشت استاد شهریار
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/691016" target="_blank">📅 21:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691014">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jDbfJmGoY3LmlCzF5RwKjcDpMY_L2iGL8BKgOoyItdPJi9lahZ-P6EEJMQTObWmWp3i100UQN3J3yswAlpNO3YxOb87Ddt6kgdTx6-ci_FR5wIspos1W4kU6uZnAFU1xnGBJ2XGCCYyLpJdQVytKZ5ij4-8go7_B9KsV4DzHwqM_Hxp6125UtWWCz5e4IoLKps83erToEITad4O6VxZuVeBQukohLe5iS83Xpi9bYp7YLAMDN8D6QTqEd_WRAh7_DSM8bRXGH6oHP_6zQcc1JWxCAsVz1QSPqntZNdAAwvRjj2JlL6aXIXn9S0udbeG4cFHHCHZBtSZy8SOH5REyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TAO7c7AIlWKzq4xJvoc4Wuk1FK3ujtQMq5cC0cMys465Koo5elpNbYVZsxUX7zSPQ3IZ_v73gn8hmLHxzrLXjkf0lQRW0f23MN135JWJ7ahoB92engN4Q42h6jcgmOmGF09Z9eQtEvstq_Pm-2a9oVnDQNYb4ac2Xjvhc4iTr029cgndVkKEJ8vIh8tPnZN4r6AiFHMGBtU4dfjBQkDR-YRVIKfjiLw_DFSqXzT2j9xdfJ5gGxN1Xpe2orYvC4bxPmlfbsC8P5bFOwmkxBcqT9JN5c2MnSjp4hpFxRI6zU1sn_aMWCT133Kd9YBjJe8tEddil6arWeVyS0s5obSSiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مشارکت بانوان هلال احمر در رزمایش بزرگ جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/691014" target="_blank">📅 21:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691013">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
فاکس بیزنس: فرستاده آمریکا برای افزایش فشار بر ایران عازم امارات، ترکیه، عمان و بریتانیا شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/691013" target="_blank">📅 21:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691012">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0e624bbe2.mp4?token=H4pOFIrzkZnSGnMhkPgOoXLpZytKWLQBHbNdTT27Wsq2WEEr225mwHQUMGiUELv4OWFufI2LRFJg_tVtfiThF6WW6JaAD4WYZ1HhnrC4z4tPp1Td98MuDCLvUUpr8PsXk-teRgSPG71X_258l84W_TtdooZXPlTxbHHwMYMYh0Nv2RO9-MObKs7qvZ2Tq9nldGuSoeMn1KGaOMMTah7tcYdV5jt9o_RGmX0Cmg-YOzdLbVaw2YCtzCkWjz7CoBjq4Ohb6agVUAbFjhFNnaknIpZ4sI30mhms0O4mwfol0zoTwKY0c3ZhU2acfAiV-UUS5UVOIXVO2MgVUX5P-FekGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0e624bbe2.mp4?token=H4pOFIrzkZnSGnMhkPgOoXLpZytKWLQBHbNdTT27Wsq2WEEr225mwHQUMGiUELv4OWFufI2LRFJg_tVtfiThF6WW6JaAD4WYZ1HhnrC4z4tPp1Td98MuDCLvUUpr8PsXk-teRgSPG71X_258l84W_TtdooZXPlTxbHHwMYMYh0Nv2RO9-MObKs7qvZ2Tq9nldGuSoeMn1KGaOMMTah7tcYdV5jt9o_RGmX0Cmg-YOzdLbVaw2YCtzCkWjz7CoBjq4Ohb6agVUAbFjhFNnaknIpZ4sI30mhms0O4mwfol0zoTwKY0c3ZhU2acfAiV-UUS5UVOIXVO2MgVUX5P-FekGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو وایرال شده از نوزاد تازه متولد شده که حالت خاص اون مورد توجه کاربران قرار گرفته است
😁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/691012" target="_blank">📅 21:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691011">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
العربیه به نقل از منبع آگاه: وزیر کشور پاکستان طی ساعات آینده به ایران سفر خواهد کرد
🔹
او در تهران درباره تشدید اقدامات انصارالله در یمن گفتگو خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/691011" target="_blank">📅 21:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691010">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
جنگ در کمین انگلیس؟
بی‌بی‌سی:
🔹
دولت انگلیس از شهروندان خود خواسته است که مواد غذایی کنسرو شده و آب آشامیدنی ذخیره را برای جنگ احتمالی با روسیه آماده کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/691010" target="_blank">📅 21:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691009">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mA2Yb45UJ_C3PN_Rg97KMSNxf0Qs5gbHKRbcQheX8STc3-MQRjbHUkJShS2nCCoxxTEzJgwaZIUgIgKJT7IMYDgqgqk2VEyhNlaG5qT4kwVdCedMKyYsbu2_dnF1GUzf7rY7q6CUyAlgcmsneemGqhrbkte585ETj3q1-yxFCy9NQpGu9fTIxdXXeF92yufU1meYcEiXqKn1akZmxf5XQ4w5TJtVpwpZerVorHfGpm-uzP4_W6hH7LVSQ9-a-M9lHp_5OQ4ExKC544xZAynJDG9j87ZuiHePLB2kSA_k2FKBm6bTMY3w9Xf8ZK1NvJ1SwcPNwZd_0_1RStQ21u6-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام های درد بدن رو بدونیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/691009" target="_blank">📅 21:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691000">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ar24WWoHkI2SFkF7xjyXTJpzQ5-IKjozJTuVzT4kVMHkPjmWhn9UJqsdVy156PBEdDrnge3D0txoM3ZPz2j8-twfvPt6m0giQ8wIQckkCbccvKtKrC-ALQ6MazyzJ6wK3jvMLRJUi1rwa5FurqS9xwVWp7FvnSpilWnfgZvl3CsxneDi8ol6RVdKbwJsni743NCcjstf3BJwKaB2mKSwBSmefj2EiX5onQh2ioH4bebVXf3junoFhQigDzyca5GrI8zS38r0JW4x-z9kmpPK9UYSmdc7l-SLluaMYy6_drmAje7PybdH3Zi5zwqkN3GGe6hnquDLX8MYQM4DKGNhnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZCnnQlmrhJed9z9CTu9Wg_MCKxKp9GWR_FzmmHb8bFBxk5DkK14dKB01VfS_h_nAvDGVyq8ORyQh8LNVvnT1Bk_RQHjPNxes22cQo2Dhq_b2nmFikYvjInK7P3DGEnumUtBM7I0E4vOOXkNMDTIUAKTRdZqb-kLWnX5_NQqocfUrtfWb9FDUG4PUQ8-EVEDHaTe6nVDDPw--t7qNGwM8HSrEJH5TFB0BGSdchM2qmsIS-dPGfqVIMjkSjJabqDZ5OW3RBZ-nf_Xwrs9dAkmO-RaEPo73O1Lw8ivIlJ8PbXjDu_3cGuXoAnftV70sU7gnwr6M4EMmRZNAjmbOGfR-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5wTr8ut2bIjVTtE4h5yEmdJC_0qqEXWn_RQORSF0lsu5UwsX0uEQ-54uGVwZkL2ZQDw55nwVKFV5XSqo2ijkdwMO6jTFI7KQhVLKucMec5_u1WgEHivXSnIJ_NJSJsv5lZJdnNGh4bYrFbSp4d7RhZ9VHF6DZjHOHz4QUc79ky8_mloze6G08G0Y7Nfm-JAr63lTKTcWwWpCpsvXr4n8TeH9W8yLWzTI8hueBFfqT8DAwgEkqm0rZtHuV25tM3DGdX93DadvalXNPcovmJE2xzVg0ItJ5qwwSu0FlnsHvcizTi-2jjuu9eStXTMt08eTDn0L6eAl6u32tEsAzSuSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SPqHf5dWXZZw9MirsRb5l5tdG5ZptHXatO1qmP8DzLbqV0MDC1lFWcL1JMpZLTpjEIQynLQHXBjRJ2P2rGTORWaCDwH2DgXolGrqHLLDJKmHFEbUZeIpy8F-t_JI2yAgnib7dzBm_RMcU4ZYV6FpW5VA4Tb9vRrYj-vBX_XouEsIhU62wLWA3MOZEcC5z4mDsStI0Do0d2oLUNzCkYAJaXusy4ZHtLy4KWqzdv4Lz7oIl1I8K8iBx19zZoF7qGthAG4Eb_BfN95627uJDDo3o3i1Kjk2icsBRzHwME3KwlbGn1xaP7qq-mS4QUD4PrMOz31yL-S140MtnHPZZKxH6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GHiq2hg3mbuU2OQaUSMk_e8S6cYh_Udq2ytiwImRpKXAtfuT4n7aziK2XbUuOn2IPnC_MVIEQJPyjvduQ9BIabXe9VH5MwV8ACGzEC1o_gs_IUBbrmxGIWPlfPIt6aN7xmAqPJIDdVQn7eJrwz5JaowPvIROQeUQ740GIIv0rONx4i_PsX8NRFFWDQEpmuM3A7gSYgU9zKRm4bc1zDfAaf72XOCSo0bxQfNU7QrC17tQ61quSHLK7GQzy1ycuMXBKytYS_kF6Vqsv4nS1SN9J2bK3Vva0h-dwGZCRZ1j4zYLQRM4KrcYGE6XAwFo1Xja-J-PZLfIxoLds0pgilZLew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ok4YJzCpIujoAEpAOJwEndTu2Lb3L6S38-ZyFnjG0B-49hY1vyZIcsuUEudXPpDsRfbAMDGBgC3a4wTyQ6xDW-55evHVSyhweLi7ezHYa9fSJycbzgRehaM4vGtWwVRy6HcqZDUCqj7D8zei3gOcFuz2V8XqZJM18qKT9kRoyZubQRYYoSKFp3bQTa6_HqsgfXC-CmY-CUE-9GvK4B6BMKXLsWPXt_4anTrWvcatw3PoashjO0Xw004Fg4UtLajhLCwjL_ks4j1zaXGAZh6VEF-pUwsSC3VAn8RZYdduhv9wvaM1uvXOETIHIYdZkpjxO2k5ZFUxeZq2Rzcqz8I9jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1lg_I6V_YIMX57wje62pjNzBgrWQ2PCD527j7wlkiAD393992KHlvmW0Dop4F4a8g-7SG0RYmEVN6Qye_9UB8c5xJ8P2li8W1LoB6PtI1uU94ykWrtLxgc4LtgaJ8VHNBbZ0fcdhgi4KJcQlf3VRWF2tEP0ADxtBBsZBUQnDnSpkmlUklcua5GPSFniH8ygcYTesfcwVtmat0H5EtS0OBbctpNeMlPgRGC2a5cZLb4imInAlk9YBMyRkBu-p-5BbWpFp0_KH2W0t6VMXyC_h1Q8KCLTtT7VI3gdM70EG3FtPjhJqn4GY3J2_XKpC9Z_ljzPqGEatCwyfUiaBtBpAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IH-npPI6B9raBRc_Gmsbt2FE0KP1tfyFraorbUbbU6K_jaEzVDmCyww0WSVJyf_XdodjqpKu2ERXDL6vwAail44Shb5g7LVfPNch9f72okAH7WFYdnU0WBIneB_Bweh5bB0nVYz2_sRCAMA8owaKPxhOouLvjXTcOfoRUECMIFMw3nOZ9ivz12mgpJ07ejgKEiVTfaKZ2ZV63aIAYELRtKB6zLEz4sPos__8fMTq3G3z8Hdl_JJwiqioNvnJs2GtI0j8nYWJdlVqvPSoW4jG9SIJKJyyzFqvNRISILG9kofmkXE_NnZjuU1tBpOg2jg9Iirb3bwDp0zVpD17hlAiTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oTM7eruR1WzPlD3ojnyftmJcuWmPozfGd_PRCE3yMG2sf6jOdqBP0xXCb5j2pIBaKePBSMqyLuFda11yris5B7xK2EKkKWk02sWwoKe4PcjNw1kAlYUBlTcsN87DEuQK8T89C9sncE55mUP2BwMmtyyChhxFv1HI_0MxYDf9MQSqI55rMS4MQVDjw3DBgt4Y2soqj3OwcX_eqYid-IdXF_H4bZXo6pTAzu-jMEiGZUnMug9trFX48gwzAa9d7dcNdqOOyinaVtBFHuVCM_mL2YxAzjGak0nFWDvWhMqzrmaWA7S7s4ob5kUTAf_fzJdXXJSf9Wfc07SD0XX9l4qNZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پرچم ایران امانت دستان کوچک؛ جانفدا میزبان کودکانِ و نوزادان ایران زمین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/691000" target="_blank">📅 21:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690999">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKI7aVXwWW3BIHBfk-sV1U9h7idHM4G3ShdOmd7zmUSt9CZ0E4WIJSm9JX3dcCpz9n94UOpkF7fN-n_N_bX3OnX2tx7rLUplC2ryFCPjsW8w7vGIA-SsE1h-VvhOl461OpngpUzFkogCGc5ztokZruJaaqhmhG6yGRiHnwbTBozhbDnVqW6VmzwGh9flYYYMbBIG6Vltg4H4I3UmKxK4U2_6ADs-QQFf1xz1VvlQFRlj_quRAwTdJ0xJBopgbMKD5zQLtKNB7kgACWrIaRg20iwz27tr6vOrjuFcRMHgJ-iSFwzmGGE5j1fCDCjzDxMpUJm2tjajpW5t6z1adRfvBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: دوره‌ای آغاز شده است که در آن هواپیماهای شما، از نوع F-35 و F-15، مورد هدف قرار می‌گیرند و شما مجبور می‌شوید گزارش دهید که به آنها آسیب رسیده است
🔹
آنچه که روزی یک کابوس وحشتناک بود، اکنون به یک واقعیت روزمره تبدیل شده است؛ شما باید با این موضوع کنار بیایید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/690999" target="_blank">📅 21:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690998">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e616241d65.mp4?token=EZjkt34QwpsSo5N_9njdf8BcKJGaw4RrQmBBmDd6ZjgwoSPtbGwb98pcaBLwviLgvb-AYPLgPlvKoKmswHZUoonkrMWC2c8RuL06xHsxK6srTmfg0nTJLVVU9AlRn0vwF57Ld7bpK6c_6iMZVf2Lrt_G7-rMLvOKPzzYjDLomCJaiyhflY6pD6t1TPKXg6W7oaU4I4pzqscLtJ9BTdA1byabOs51jF8WUbi37119qheNhO2eZgrZZn66piH_PutN0FYcpuHYytW_FvHtOdfeZHKPMreeZ7UgobMJHr9fyTMSL8zzKhbH51E-xwTdcC0UhNBQPbxEUP5vyBmoxZ_mNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e616241d65.mp4?token=EZjkt34QwpsSo5N_9njdf8BcKJGaw4RrQmBBmDd6ZjgwoSPtbGwb98pcaBLwviLgvb-AYPLgPlvKoKmswHZUoonkrMWC2c8RuL06xHsxK6srTmfg0nTJLVVU9AlRn0vwF57Ld7bpK6c_6iMZVf2Lrt_G7-rMLvOKPzzYjDLomCJaiyhflY6pD6t1TPKXg6W7oaU4I4pzqscLtJ9BTdA1byabOs51jF8WUbi37119qheNhO2eZgrZZn66piH_PutN0FYcpuHYytW_FvHtOdfeZHKPMreeZ7UgobMJHr9fyTMSL8zzKhbH51E-xwTdcC0UhNBQPbxEUP5vyBmoxZ_mNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال‌وهوای سینمای دهه ۶۰
🎬
🔹
صداها، دیالوگ‌ها و ملودی‌های فیلم‌های آن دوران برای خیلی‌ها حال‌وهوای خاص و نوستالژیکی داشت؛ «خط پایان» محصول سال ۱۳۶۴ نیز از فیلم‌های پرفروش آن دوره بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/690998" target="_blank">📅 21:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690997">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
یک گزارش جعلی هوش مصنوعی؛ آمریکا نزدیک بود به کشتی چینی حمله کند!
سی‌ان‌ان مدعی شد:
🔹
یک گزارش اطلاعاتی تولیدشده با کمک هوش مصنوعی، نیروهای آمریکایی را به اشتباه انداخت؛ آنها تصور کردند یک کشتی چینی حامل قطعات مورد استفاده در تسلیحات هسته‌ای است و نزدیک بود علیه آن عملیات انجام دهند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/690997" target="_blank">📅 20:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690994">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tJdGeQBYQ1Jex--_-M-t_EcUh7KAMlVvGhqeDmyE_wNSHpMCNJMNEJY0RKQu-YULMDsTm3Gmtttw3rP9Jh35Z2HJHefcKRoxnd3-XL0EfsHygABZ9QhThIhjmfJKLkzNu7SNHO0zANyLcBCWgTbhGbtP9dOgij6otfdy2DBTE2gUe8ctN4vI7XMBuYCtXB05naAwMK6edSU4qc6ZcEwhRq4xQWMBBJ_kuR_blKuX1wPjxGUWiMghtXbKIM5BhxNDrg05RW2g-hT4GtN9qQaKDN2Yt07NL8lNAhbY9Z4DcVWHrX1AMIMP2YtnVfWMFSMzu_loMKuAovU87wvbLIIyhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZpZ4UR7D7DwgKpSTxNz0IFHSFkhoD-snqkxKMqHkOnjOrRE0ZHu6woNh_QHfux5bTgTMzn3YREiihPud2VnCIZyZC_ftXU22pskiVho-dwuP3H7WcWP2T3VyzSaVBij3u9ucjBRm1dbu3tfREMXkbSrRbZCzpUMSspfKILIT5T09m1h0j-pPzOrTB_aBwOIxXrjUgMvhrGWG0oUr1DCVN4fjW4cusaDdDxk-e7qPScZY8ZHN3KhNsZ8WSXLYuMmqMFQEjJs046YJXbTaE-V_cfGpkKITkL4PVRLblVEXHsd3JR6bttMuX8h6QVM_7HNZiuvAtBaO0LlJ7HqrC0xP4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4179a1b0f0.mp4?token=CiLbjJ25cBxzu4pGQKhUB2MgYadtThZHwIwvis7SXy0sDqJP_HUXm6-Mp5NDHC7sydSoqcv5q25VxDRjOFkQQqWzj8bgP7F9R4CR_MWPaqipeSBSwvdsO1_o4mixZB8F7dRBfejv2MNK-YyxEuzMrVwiV0wnoPoBZjxIORCjLhCimAbiv-3BUEAMm2632dierwS0aVKSkIQYwXMCHE8i-KeF5hYHD5zKBHSSmljxV10aPmYzJ8NdzCRNt1v85bU99ctm9HWuLvgaxHRtaZk-qEfIWR-J_s4Dt5OqcKy9nsXcXtdECYLEmf96hA1V3LOBN-v7BlIGXvML3vue-9dTMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4179a1b0f0.mp4?token=CiLbjJ25cBxzu4pGQKhUB2MgYadtThZHwIwvis7SXy0sDqJP_HUXm6-Mp5NDHC7sydSoqcv5q25VxDRjOFkQQqWzj8bgP7F9R4CR_MWPaqipeSBSwvdsO1_o4mixZB8F7dRBfejv2MNK-YyxEuzMrVwiV0wnoPoBZjxIORCjLhCimAbiv-3BUEAMm2632dierwS0aVKSkIQYwXMCHE8i-KeF5hYHD5zKBHSSmljxV10aPmYzJ8NdzCRNt1v85bU99ctm9HWuLvgaxHRtaZk-qEfIWR-J_s4Dt5OqcKy9nsXcXtdECYLEmf96hA1V3LOBN-v7BlIGXvML3vue-9dTMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به یاد کودکان شهید میناب در رزمایش جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/690994" target="_blank">📅 20:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690993">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار سیستان و بلوچستان(Admin)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d58954e4.mp4?token=mewuTf0-qaY94WNXKpG5dBhFUUvJFxiY4u8_Q2PulBxprmw0c0gTdd_-OknaBKpNqyPUkb2uD491o8GpwmTpTrsxIhTzBH5nKL2uTiTN6ofSW7WWAmaOyW28_1nhacoYv374skdDsAMf_LmqRD2BRsLmyLVbbWdxTJQV7XN2lUdmx5ThQXTIfamKSjds4JWGb5ngr0x3Whtvqd7z0Y8GIMNkn0IKBlxaWG-FjmNNZjlJC1y_2y9n5udANliXsNhtbsuF_oFLbAQwqphjnoUOZ8KSKb-GL-oyQWgcM4K78fHvCyx3eyOlyjT-WghbrR_jpoaoG9I53ArCh10egdc31o3dyilBvETps-7af4y3Z9Kbl62uca6FVqWSUUAl4qSOBoos0Rf3eblKfY_HYHErjebRcxGc07WS1cnjdf4DLvGgyLkzb3Yxxe1RF7nSbA6ZsY9ZL1ckfwDLkdgItybDjcQGEL0ERYZUIkK0eqwVY9Rncd0KwgQOg8tcBogpc5Gtp8ME0u80VPkxS9WNTDFWEsItwiG7hR4uz9C_Fxv7p-yp--JuRHnH7MGiC_pjjwXL3fs0aN9M9NwrL7QQQe0OnhMKwWJbmkqlWPc51EdCEgkReJB4PAC8RqKDM9sqpd7VUbotb5Z4kwhZUbtVpaagpF2GbGCrmaejg1u7Ggbmzoo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d58954e4.mp4?token=mewuTf0-qaY94WNXKpG5dBhFUUvJFxiY4u8_Q2PulBxprmw0c0gTdd_-OknaBKpNqyPUkb2uD491o8GpwmTpTrsxIhTzBH5nKL2uTiTN6ofSW7WWAmaOyW28_1nhacoYv374skdDsAMf_LmqRD2BRsLmyLVbbWdxTJQV7XN2lUdmx5ThQXTIfamKSjds4JWGb5ngr0x3Whtvqd7z0Y8GIMNkn0IKBlxaWG-FjmNNZjlJC1y_2y9n5udANliXsNhtbsuF_oFLbAQwqphjnoUOZ8KSKb-GL-oyQWgcM4K78fHvCyx3eyOlyjT-WghbrR_jpoaoG9I53ArCh10egdc31o3dyilBvETps-7af4y3Z9Kbl62uca6FVqWSUUAl4qSOBoos0Rf3eblKfY_HYHErjebRcxGc07WS1cnjdf4DLvGgyLkzb3Yxxe1RF7nSbA6ZsY9ZL1ckfwDLkdgItybDjcQGEL0ERYZUIkK0eqwVY9Rncd0KwgQOg8tcBogpc5Gtp8ME0u80VPkxS9WNTDFWEsItwiG7hR4uz9C_Fxv7p-yp--JuRHnH7MGiC_pjjwXL3fs0aN9M9NwrL7QQQe0OnhMKwWJbmkqlWPc51EdCEgkReJB4PAC8RqKDM9sqpd7VUbotb5Z4kwhZUbtVpaagpF2GbGCrmaejg1u7Ggbmzoo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنگاه که افراسیاب با سپاه توران به مرزهای ایران تاخت، سیاوش، شاهزاده جوان ایران، داوطلب شد تا در برابر او بایستد
🔹
نبرد آغاز شد؛ اما آنچه پس از میدان جنگ رخ داد، بیش از یک پیروزی یا شکست ساده بود. تصمیمی گرفته شد که سیاوش را در برابر خواست پدرش قرار داد و راه زندگی او را برای همیشه تغییر داد.
🔹
این نخستین گام از سرگذشتی است که به یکی از تلخ‌ترین و ماندگارترین روایت‌های شاهنامه می‌رسد.
📖
روایتی از شاهنامه فردوسی
این داستان ادامه دارد...
@akhbar_sob</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/690993" target="_blank">📅 20:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690992">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfFQ1ga9Uq7IHlHlw-vjI29AUq3L2cast31NBZqtoTRVDlhwL_nitfeph4LMxJn8iVbVuek_oOywa6fqvIjznQCc0KZDxUbu3W-6a6gcCdYdU9ggeB4faq58YJ0fwGwbwK7oXw_L8O5BYVGIJYcvQ2bTXuJ9qoThgnJfQfc5kQ0oqlJDTxWGEDpicXTulkxOTopjofQKlDLVYUlSQ_grtUOXVzn0CwS9GncFi94bVNhPisBtFENqLTAAyT3FSm7P2k-5MBn8pK54IRMHAKN2IvqbXUaT4JaKqXccEcat4V5r3yqiDSRE0GkIF97yLfCuGVCrdm9gK66kiGascKuAIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یادداشت کمتردیده‌شده‌ی رهبر شهید انقلاب خطاب به جانبازان جنایت وحشیانه پیجری
بسم الله الرّحمن الرّحیم
عزیزان من!
از امتحان الهی سربلند بیرون آمدید.
صبر و استقامت شما یکی از برترین جهادهاست.
شفا و عافیت و عاقبت‌بخیری شما را از خداوند متعال مسألت میکنم.
سیّدعلی خامنه‌ای
۹ مهر ۱۴۰۳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/690992" target="_blank">📅 20:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690991">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: کارزارهای نفوذ با هوش مصنوعی در ایران، چین و اسرائیل
🔹
شرکت‌هایی در ایران، چین و اسرائیل از مدل‌های هوش مصنوعی منبع‌باز چینی مانند DeepSeek برای ایجاد شبکه‌های حساب جعلی و انتشار هماهنگ محتوای سیاسی در شبکه‌های اجتماعی استفاده کرده‌اند؛ طبق این گزارش، کارزار منتسب به ایران با حدود ۸۰ هزار دنبال‌کننده در نیمه نخست ۲۰۲۶، نگران‌کننده‌ترین مورد توصیف شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/690991" target="_blank">📅 20:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690990">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63097770d9.mp4?token=AMJ-0OtwHrBC-sTyUf53_kaBZVunezfs6JNpbyhKPnlwuSuQzTW5FkhNyaEjNU49IUkg6BCshTJzGZQiS31054zI5X0FsVi8DyqsOfLhOBPn8rjubBI0_X9om2wgoRzZckxk27SUJONdIdMjQZh1chZPMglJzQx2RxzhMi2q8kMza3o7q-o3Ct765ss352tJgx9q6E0MKL0YcH8DBGiGGvpnG1tIFMgSRKagI3S8xa_u-y3CULuXPQ9GUnRo0BAOr7VUbcE9ov1aACpcV_nAyHI3sppVBafQPeWj1TFBq4_e1p8wG21Nd7IWU4T8dOJxxwTXykh1vXqrWaETDtCJww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63097770d9.mp4?token=AMJ-0OtwHrBC-sTyUf53_kaBZVunezfs6JNpbyhKPnlwuSuQzTW5FkhNyaEjNU49IUkg6BCshTJzGZQiS31054zI5X0FsVi8DyqsOfLhOBPn8rjubBI0_X9om2wgoRzZckxk27SUJONdIdMjQZh1chZPMglJzQx2RxzhMi2q8kMza3o7q-o3Ct765ss352tJgx9q6E0MKL0YcH8DBGiGGvpnG1tIFMgSRKagI3S8xa_u-y3CULuXPQ9GUnRo0BAOr7VUbcE9ov1aACpcV_nAyHI3sppVBafQPeWj1TFBq4_e1p8wG21Nd7IWU4T8dOJxxwTXykh1vXqrWaETDtCJww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هوایی از شکوه حضور مردم در رزمایش بزرگ جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/690990" target="_blank">📅 20:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690989">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای سازمان تروریستی سنتکام: از زمان از سرگیری محاصره دریایی ایران، مسیر ۱۰۵ کشتی تجاری را تغییر داده‌ایم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/690989" target="_blank">📅 20:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690988">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e096ac356d.mp4?token=tckhzq45rkHRhd3hxCsqvof_xyXLdX45YgqXq52hko-_L6IAA_qWG4RJ2wZ5FVINEJXz1BISe96c3SIhJI-LC8VXn1spBJVYPM5nk5hD_ZWm7ct510csbJEXjBzvs-XUJ3ipCFh-p9-CxxGfftQvfSfffd-Uz9pOBYbj1CoztpL2RqXc26lirnFZqxVUjWPjIb8HIQvw_trwJ2T2mzxMDRj0aR9X8ZkoZEWEzF8ec7C1EPBT997tvWXnEigm2BlxFu-esIY6AlhoaP3jwSx2xz2IXA6LcFmtBnb_bFJ7WGaf1V4nUuUv4wa8r-SpzMZuCPZ5QnSuxUBY_TuvDAB4uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e096ac356d.mp4?token=tckhzq45rkHRhd3hxCsqvof_xyXLdX45YgqXq52hko-_L6IAA_qWG4RJ2wZ5FVINEJXz1BISe96c3SIhJI-LC8VXn1spBJVYPM5nk5hD_ZWm7ct510csbJEXjBzvs-XUJ3ipCFh-p9-CxxGfftQvfSfffd-Uz9pOBYbj1CoztpL2RqXc26lirnFZqxVUjWPjIb8HIQvw_trwJ2T2mzxMDRj0aR9X8ZkoZEWEzF8ec7C1EPBT997tvWXnEigm2BlxFu-esIY6AlhoaP3jwSx2xz2IXA6LcFmtBnb_bFJ7WGaf1V4nUuUv4wa8r-SpzMZuCPZ5QnSuxUBY_TuvDAB4uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ قمارباز: ایران شرورترین کشور جهان است، خیلی سال است، ۴۷ سال نه، ۵۲ سال!
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/690988" target="_blank">📅 20:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690987">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
اسامی شرکت‌های هواپیمایی ایرانی که امروز در فهرست تحریم وزارت خزانه‌داری آمریکا قرار گرفتند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/690987" target="_blank">📅 20:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690981">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ty347jXroadQGFQB2b1MpCpfI2jvfhuwaYLTEM6tEsH0zV6AV_xfqiZVUQrV2uc-lxPr7TNk81JMtxhX0Q04spYZ11usHviX5umFZCvNTgPM3l-hssgf8KnkUMuG72Xrc2ze9QlWEOij_V4cxxziorMpK_d3agKbTuzHEz7aJC15GUAPGZ0ZmpHu7W9T5MBhwzL8VeyWZa-7z9fRoa2BNLQziC3nvH6fMb0tUnPu5SYfJe9HEaWyX1IXZYKkfJs_499O5Zu9yz7g0advPWgaNRnwWDnXP6pGhESs7VY3Gv5qw1wOoXTEjVBrj_V3j47QwZZ9g4pupNt2oXFyKIrQtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GkWNvmcfl8hzaH1ukYV0_6Lkei3lAJ5j76a0pA_F60cJM_O8WDRPzv2HE2kEsvQ40pSrqzIeHvHTmaopeG2otHD0xp4hVeRURLpYBdc-PdXPouyDS7pl6S__KFF4ao7bE3VAR0MxaHkwAnafd_diBjcXIPvBOchpTU5pT4imig5ITrLzVAJhE6ctAaLmR-NBVoOAPkNXlCUGCH8CjeVkFm8VNCqltdpYHUyZWFMzZCPUwAtn3W--5hUbnXwLlRiv0V9vbCXozsMLZIqcKfFgoGwaCrvacFTtSE0ZiE9ZpfKVR2fmpHiwkdVU_Q8SpKtB6rpVKAE3w8alrZvtmI_Zqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oNzZ0ESgDrqqYw_mnV38AE4xhvVdtmbwYGhubAw04Qw3zt5dIw60IGi8m1qg2m--ck4mfMAiI5Cu6V_42DKxG0-SbM2O-433Kz5dSlRr0jKsNMj1A5f46zUtDkGJjZgVKU3T94beOjkKKZPuBnXNsNoa1FFmZwUCGCXm5JMTqCgF3ZcBQZ4Yf8_LfzePzOBOwqDy5DLVcOFnWfjhlZnyxEsdtmLc-JFlOrp1NvlrIwSe8SmGNGvmKziPm-ND_7UkXMjMYYkpWQW8D2srlpJypzywxOz3N3J6Ud2lowMgQhfT_2y8M6JUABeqzPA1FKYBHm8Y6cf0su_gar99cwyUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R6mT6vSnCuyBJANNdSgV8zb6JPDUwrl_4fOGiZOzAOK_HdrayM8BY0abrL_d1J1Cez_nv53PvvfhAEls9eCN5600BJMCokOdH69f2GefOp8GdtUyPpH611Q3AXTOGK5m0Q1t2hmsgu9ogU88FF8UuJKjhptczPsnX29z8UPL8rxBL2wcgo_AD4nYhcX4lEDHU-4lQVqqShb9Qo7_F3mMl0mf43aV3OraHzA5mqZWsXuBhTq2mgCGnazjvbwStAfpFa4kLR2bq-1Em-9Fe3A0y3EhhPXfsUUNcne9jWF9ZNc9DGadrixtkDCE1w2DwudbbdfvdTAj6755xTT5dK8v_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ja9jP1Mt9YWHn--9-8mmnrRJRjuEGf4qaIvxchu3Lc4rndAQ21Vq-2jGLohT9mPz-nxMmSiuppgKQG5Y7gfNWfhHsnJRtZaM57C7V4oQRFwi4Ci6TN4kKj0wAMA4stFUiAMRhMS2FRgN0wRWsji84Iy-Vp5PhnK73lZkwxVdjwZ5uptoK0hQlu5p_wdYNHWsK9gqj5D957lDJWkAg0GdWxb0l93fCuQFaOX5699FlfCw4bT39C_8NqxoENtSp0_-4gWEpOOGt-5NnAQvhtjejyD7K-0Ct1Y12CdH7xHRDnyW6D6Mqx7CYYeEpvELFUy8jhBujOYW_JBasSp3axwpVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دیگه خرما رو ساده جلوی مهمون نزار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/690981" target="_blank">📅 20:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690980">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdw7DCuWa-EIu2ijSypHDgEMpQwyWfTcT9bn_5VIUVlf1vfdHJf6QbotaplvPIuYitdOiYjOHkNB1JnVLZD1hMWNYeEaeWZTMZ2sFLWEBxxAl7dJMg5a0ySqe8uZH14Iivrc2mB7CDLk_KbBzuoAGjI7VnDtXwoESXg7q2su1BCBIJVziq6G5awn-3h6vqG1rkS4fuLqH06BrKvsVUkRnl3JvmSS9QqCzUsRUIZGpz1c7haXbym-PNZrPOJ9cEnMBPsk0LtnPqm7ewVcnJ6-5lDii0rtDdZJxodNgZUwXGzDsdfabLG_DPs5otpfQSUfKvc6udnchltZv23YZmmLFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
احمد الشرع،رئيس جمهور سوریه درخواست عربستان سعودی برای اعزام جنگجویان سوری به یمن برای جنگ علیه انصارالله را رد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/690980" target="_blank">📅 20:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690978">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUMiOx93j5VQ42-6zgZEJnmtuXJAUmoHqfsGlotkMZoqTzWdybaiEJkjppQ6DcNX0WwzHAI_bDXpJXv_yWihpXW_bwhdZaav4f1Wxbj0swLfxhtx6AjslFXzMzJpYD5xMv3Xe1dAPSWbO912zBI5LCAQN2SYdFg5QAKT2TSZ0trRH41rHw0YuT6eIA2vulX2MKSezDKAOkG8j8H6qpEcnGxcCw2kDZq48wvSGFTVDAclgxV64SVlRfZbMuVr8y2LXrbz5VIQAjHpe5IjeF9Ld9XZNMxMPMcTecJzCz6MVTMdeFr9Ugm5ESqiSzJEZaHgMYrV85CQp3quDzPYQoNSVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iquFqaLPjy2yCa7f8WIG7cea9Q2VnpWfsIDKr0JJhqEECxgUNwznL0IpIIKjMdq32acBmkcFOkx_DW3znWyuuSjw0k0j77SsBjMgCn_N91k_1_O5idLH4hVfIrll5c6Fie_5kY4dSoq4wJpjDNIVJMG7M0hBpRs7KZGrWHZIjmNx84FNViK9yPrFnKISnYNOntPZ9X5b5cdHSuJnyxaI76kHUlCNqWTIplzdagkI6C0Ye-Hvf5xUfGcakFmBqW8A01rpHYhpJJAQFDqJhYs6xWVBQccjfHxfol0Ch_J5AnrwYXzS6gG7jA92huB_THdHQuaEIdY03BajHM4zazWXrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مراسم دو ماراتون در بوستان ولایت با تایید مجوز استانداری تهران برگزار شد
🔹
درحالی‌که از ظهر امروز تصاویری از همایش دوومیدانی در بوستان ولایت در فضای مجازی منتشر شد، پیگیری‌ها حاکی از آن است که این مجوز یک ماه قبل به درخواست اداره کل ورزش و جوانان استان تهران و با تایید استانداری تهران صادر شده است.
🔹
در سایت رسمی این رویداد نیز، «تهران کلاب» و «هیات دوومیدانی استان تهران» به عنوان برگزارکنندگان معرفی شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/690978" target="_blank">📅 20:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690977">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
هانتر بایدن، پسر جو بایدن: اسرائیل از حمله ۷ اکتبر اطلاع داشت، اما برای جلوگیری از آن اقدامی نکرد؛ جنگ غزه شبیه «نسل‌کشی» است
🔹
۷اکتبر ۲۰۲۳ روز آغاز عملیات طوفان الاقصی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/690977" target="_blank">📅 20:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690976">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDYJZTCsVJS6XRZzAAfyWoGP2U0SBWPq-b2NJi2SnqEHkOsX3A75vRJihLk8s1SvruhyIMZ2rnEB2bjlKzaCM2FUuOzCMBYkvY0x88_lMbplB8ozBk1aVLZaEMVCNQoSWufWsdHQzUye92_0NVmrugxd0bVH8kRq5E1r1hs461TTo0uEEaEpI4QEDqynCFxEZAKr9NjgTWUiRexzFzKVT72HIGcEYyUOOV4Fb_-5WTrzXBz57x7mJq8PmwCIbE-94vPclr40MCrcz0i6iDaUufzulRMtqYDL8v3m-CBMOqQ4oBbEZ05JDrioLqex114bn4_EbBMlsp3j0DmME3iMnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۱ کشور به‌عنوان اعضای جدید در شورای حکام آژانس بین‌المللی انرژی اتمی انتخاب شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/690976" target="_blank">📅 20:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690975">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
ادعای ترامپ: با حوثی‌ها در حال گفتگو هستیم؛ حوثی‌ها نیز تمایل دارند به توافقی برسند #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/690975" target="_blank">📅 20:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690974">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ادعای ترامپ: با حوثی‌ها در حال گفتگو هستیم؛ حوثی‌ها نیز تمایل دارند به توافقی برسند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/690974" target="_blank">📅 20:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690973">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c989965e.mp4?token=qizsSyo5NCElKBkGySsH49CP6DQTKP_3c-aU_wcbZPw9EkjMq5fe_ElGqLbVD-tTKT7i728el7Doz2hvws_ct1tUR3tXsveTMxkbOpKTcFBimkDAUyidq0zZmabfK2NlGZ8dX2JldG8uwR60rTYdvJ9E_6dE-xwrLvt8Q3k1wxwyk_bbxgXQtbDCxQ2b3nFPHYowcGfTz7OgFbhbWIREgu0oGx5YFNuERkio3DrrT_xvaU718CiXOmxRcjz2T1KPEU4WR1UGqjyrsbd_AmmITZIKUzxirFjnpyCC78WjsCwtVez1DEBAEdtxyTsK5LiOzVil9OwE-tElOxzt0hHm5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c989965e.mp4?token=qizsSyo5NCElKBkGySsH49CP6DQTKP_3c-aU_wcbZPw9EkjMq5fe_ElGqLbVD-tTKT7i728el7Doz2hvws_ct1tUR3tXsveTMxkbOpKTcFBimkDAUyidq0zZmabfK2NlGZ8dX2JldG8uwR60rTYdvJ9E_6dE-xwrLvt8Q3k1wxwyk_bbxgXQtbDCxQ2b3nFPHYowcGfTz7OgFbhbWIREgu0oGx5YFNuERkio3DrrT_xvaU718CiXOmxRcjz2T1KPEU4WR1UGqjyrsbd_AmmITZIKUzxirFjnpyCC78WjsCwtVez1DEBAEdtxyTsK5LiOzVil9OwE-tElOxzt0hHm5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تانکرها چطور کار می‌کنند؟ چگونه هزاران لیتر مایع بدون واژگونی حمل می‌شود؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/690973" target="_blank">📅 20:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690965">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vyzPLkxyVN0cjSU7f1RRWRxi4IUJ4HFttkzhp1hxZwIH-qGbEu0IxghTM5A3d2GC5tuhyvGQ-bgAmL99V1Js-sCxd7EWLEILJYRotF-IOvSDyolmZ1GXq5YdrU7WGT4IHck2kMMc5b0y1UufE0Ee66Qf9A6XHx_pPOHhnKiaVoQhz2GD75U1i_RbUSl1zdAXG2ImQAQ5MrRdwaQsuM_KsjLTOtJk7wQknylqMogO12ijwDVe-g_t_E-fYG9JgVZHu1iVmD5Kq9zUVLJAXb716lcTnOD4FX-n9QD-MXcw8dpvv-VNkPhh5KNGOhHIXU_toSF4nMz8oCVEyD_feWqNrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q77HhC3RGXvkCfy91D0znN9OIAI64xmNWszAVy3gzVxz8qLeQWvd26ZzEYS5R5AHlarZ177IheaI-Q2asZL63bNOKsIeaSPk9wqTTQFnJvr8QezNyO4kbZo2iUnHdat8FmBj8nM0S1rT3I74s2Ko3qq6CKS54TUYlEKJubTzywiVv8LD-QYxD3zXY4fXfROfZvLszW4sazz96DQgFPPERy0Ns7KtQM9pJghHMwrCx60f6psRjrzlf531555vNCE1mVJt8ETLKpHpriv9a6FhgOFHcqEYFv-Euu_Vmod6lNgs0Al7XfHTtt1bXhtJlyYWdO6jee-DDztlrxfSewqtwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oha1pRyOwlEzwMIuPMBjPUbNPLwmzWeuXh54MP0Pd9iYQAbQCjT9_NPP6AIoLWoV9xj8b1v92pMFHS6qAQeKJ7rDe6vY8ZqPrxjQPPGyXQbEbcRNmA9XNDegsMxjCyYNkU0LW5ozfs2XtIBYSll78WnEbg90wnZTyv1ZLZvU6p9YImnU9A3RVTr2QCVl0fEdbUJN_lhvs7uqF4i9tEs50vQqy0CSfCtZQJnpOFsFzjgEqvtxxYGTNPS8ZtFUHu1LxcVRGeZ-chjP1Mc9fGIVevMxuSIZ3IoL1XcnvkQV8JmBJmJZKsce1b4QdtEN2k3eWh7G9Ty-kg95hzZI9S9BLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQNZB6EQ3DgX6Oz2eFa0MtIIXl5Ci5gJUMskMQyBRKlCB9YJSEyWb0acXeYHl2Q--lB7zu5EbjyIbt_984Wsgxu80MPKaH-Tvc_tYm800WJ6I7SCNt5aSYQb7eukNVBOmendIR2KynuF9dL9aILqdd_PPBoa15ue1R69hxye69K_OhyrQc4zgrFee9hYkES8CkJj_PGWTwJ90_qqkwS-A3ydp8oiNHlDsKvC9zRvsiC9s1C-TXWWVJzlvbCLpiu_ygUB4ZX2fIioodFhy0gcefPJzmRBDqHxID1UbdcSNxHerzKe4glQ12Y8n9xVENe3Tu1R0j8WU4m1aN82KdWOfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RVtEWlyPO3FC5A3JQ2uPWG4vdma9UILPllXoYSNiARmtKywXbEJS6xz53OHm_a0zn4FL6w5--YXUra5_cHtUPCsr_xcRN8r7pSvvyCXQAKalviOKjGcr5fdEoE0kCG-OsLBhP8qXOycV3uJfFlF5-5JWf_s8ASmOiTxsH7AtUTxQBS2bsL4wxRXESnnK3RCaG7blJrUgFnsvoo5NtALAgMxLia9UsSXKMFtwWHOqfonFqETj2C_Cv9fK5RZlFqcY2kksFpjbvHEYTknLKBD_bHkrjlFyYIVyOJort1YWPdS93HjsakfqPlhxeolxUWKodgMUFCKbpV7FpRyyeQXv1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SjAc7FKDI_pcC6ArL_KZ3gcm0lr01e8NVULj86wJKB3Z6KRl5I9Hwsz6kd37LemgiHmSjsHba6Fyyhvg6kNWvdgH2rr_VDYMz4E_yCiEIqDRqHjAyAOvkhcd-jfrNb11peDccWNiGVQy0-xjCSrkgD8uxbilu0Gf2fNeRvlw29UDswCkm9swcwHHm4r9XNqhNKcz3AEzj8e6VBZeSAltn1-w3hpgtnJxbPgiW2T1dcsqd_alE7w9tHggLApF3PAND7dVDQF4FZKryMMgu8Pvy-8yZ-_vhLf7ppJDAratv_4qeDzA_xdya48xjwL43E20vSNDlExlOfb5ot_M9H_hRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aNg3GKRSHUJIMeqVU9ZDIVcMmWrY6TBMUZ0UF9o5sNdTPkSv-tzmG-Z8-bGp1Zj75HA5Dbnn0Rldoqo5cPkAPjYbxwCr2l7sbT5uwsgkuE-nw518hrU2qE55QXzF5OLarYYHHeIpFj5-i6VaQ2Obo9WmwpWmNA3AKAuhKV3AQz29g653pbuv3oZFs3Yd6F4Adp1gqo5ODH8BiOFgHROZnUWLBHya0wjfyJuIiexZoQx1rNQR-1BfUrIDQc7m0L0QVYQgaRGOPNQQvT86lWGyLJflNjNVUMcVa6VP43Q-A5N5ux-HDkolFsDle8un8w_dmbFykjM7LLsjvm-XwCBW1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PSmFCdg8Qv3fH_4vsR1Oj-EEwdEwqrpBaMFXeBnX5ipvv9gFEDj_-bltrXJWan8b704K5wD62Pi6nml91rste_MoyBqVVnEIV3m4xRye7NwN85mH2ZOLbjd-zi5P7GIfjbRdzo8NCL_6fZAmHZR1bXkLolr9qp2zoOOLrf-LQqRrXV584ARVE2v7Ga4PvOobBVXosa4sCBP2cV8BVv7wQg3kH19zXDbz9K3W5Mf9RvMl7Zi2qNdOdTMAUTTJINcutzgsgY4ZTvT3sXd0Gf1HnlQ4i107YcZMhJhA-GQXsIUzZA74RXSrXCPqizjje0mXGeNpFMha4CAHOsM9wujBsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور خانوادگی اقشار مختلف مردم در رزمایش بزرگ جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/690965" target="_blank">📅 20:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690963">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZ-7a3_jUNRQ8ecfjgGIazmmyfZ-JkDkB4cAOegrG5mwgkdEDZpmQxTWJo--s11MZTVDCaWCFtO0Ydpt_pANVoRFgWyW7j7m1_5IHEU-6OFtRGqmgsptQByQ1XV6MSmc1W1RitLg1e4XHnnaHqJ9cfCAU2KzWp6rLh4YV8dNA4hmG61sw_1LHv9kg61uooAm9TpYmyjfn-i-7e7ChCmIn4jpn9SXSCNxe25EKvvhHBr-8FMnhgwa6C9PDtQ7PedmNwBZI9S7aMJFivC-9tkGQ5oSIQf8SF5XJOUYUA_1MrnMPRJ0ePhA_J4VUo0Zos01NqMDPZIQqwF0UzOXbG7KAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قطعات حساس F-35 سر از هنگ‌کنگ درآوردند
پولیتیکو:
🔹
قطعات حساس جنگنده F-35 که از استرالیا به آمریکا منتقل می‌شدند، به‌اشتباه به هنگ‌کنگ رسیدند و این موضوع به بررسی کنگره آمریکا منجر شده است.
🔹
گفته می‌شود محموله شامل کانوپی مجهز به فناوری پنهان‌کاری بوده و پنتاگون و لاکهید مارتین در تلاش برای بازیابی آن هستند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/690963" target="_blank">📅 19:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690962">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe19ff3eb5.mp4?token=qpHK8kgIifzMdWdXgYbh8YDPfH9V2qoj8Ja2TCFoCxmpV_l1b0tG9I9BTQEUD8Gp0cMOmRRNDRnqVAQDl1CbsTik9_aujC74IZlWBBstmfELEog8A29GRdEAYk9fI7TOJnYO79BRAj-AJHo-Rvkb7mODbeOFh1E3ASc21Jw1YUgn7ttjZu8XOdbeo5H3CncM1fJL98x4yfamzJd2OK7EWesPgz_ykm45f14ozHv25DmvJSDy5-55sS2UnizJrRt7SorhpGOBr3UZAvjDgQb4JTZlCi0pnWiQyJmyxbBZ9-UKL6TGz5-GdOG82VktbqUdtmc8LnNQf3SJ9Bv3GVxxyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe19ff3eb5.mp4?token=qpHK8kgIifzMdWdXgYbh8YDPfH9V2qoj8Ja2TCFoCxmpV_l1b0tG9I9BTQEUD8Gp0cMOmRRNDRnqVAQDl1CbsTik9_aujC74IZlWBBstmfELEog8A29GRdEAYk9fI7TOJnYO79BRAj-AJHo-Rvkb7mODbeOFh1E3ASc21Jw1YUgn7ttjZu8XOdbeo5H3CncM1fJL98x4yfamzJd2OK7EWesPgz_ykm45f14ozHv25DmvJSDy5-55sS2UnizJrRt7SorhpGOBr3UZAvjDgQb4JTZlCi0pnWiQyJmyxbBZ9-UKL6TGz5-GdOG82VktbqUdtmc8LnNQf3SJ9Bv3GVxxyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماده‌ای کمیاب از نهنگ عنبر که ارزشش به ده‌ها هزار دلار می‌رسد؛ چیزی شبیه مدفوع و استفراغ که در ساخت عطرهای لوکس استفاده می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/690962" target="_blank">📅 19:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690961">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
یحیی سریع از ناکامی توطئه سعودی‌ها در صنعا خبر داد
سخنگوی نیروهای مسلح یمن:
🔹
تلاش‌های جنایتکارانه دشمن سعودی در صنعا (پایتخت یمن) که با رنگ‌وبوی داعشی انجام شد، ناکام ماند و بدون پاسخ نخواهد ماند.
🔹
هنوز مشخص نیست که منظور یحیی سریع از طرح داعشی عربستان سعودی در صنعاء چیست، هرچند برخی کاربران عربی از کشف و خنثی سازی یک عامل انتحاری در تجمع امروز میدان السبعین در صنعاء خبر می‌دهند که این موضوع هنوز هیچ قطعیتی ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/690961" target="_blank">📅 19:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690952">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hvMoEHFCSqkaaRL6iYBvcIAFSpov7_yb5P6uJdgz5dq_Bko4lIAAOqSu9PZiP2TwaVSLAWqBEz7E3BrfW4VrtcRaLf30egka92KYv-LAX91HC8xDCvB-dYTG3me3BvM2lhgHPVnXL5ZP73-iS3kvewzfLmgnSrlOfrb_7AC5MbnfWE0gIdaX0B0s_EcmbZ43JFaY0KsIssYSct18F0av17fwpG7EoXdBfSFsaUyKi8wY0NsuUAGxE6eWQfg2dFQDb6v2ZGZdAOblzaVXKjlHoSu_2EC8huesUofsm9bI6W7Qa0QL7hQOAifaPpMHTCrBILXdd_dYwkZvKQ7UfJgKZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ztb1CdKhacWljUUBPhc6bBk92A_D8w4Jby1CQP_WzRyQGzQ5RPtczshaa56gT-CfsYnxTsbAu45yFzmI0bw0RS6VMz8Ex7rbEDJfybFOR6lqDc-DsOAEhXRy-vpKEbk1M3yYvIku0WAps_MA65GtDkkSN7BZKK_o0szAX0lBslNgMCUDNhywifYgMkWAOV2VEmHqO8ZgzIephskYgKTjv6hvuogMJ0ZBHXERJ5zv7kDJ4yLLJb-BvI-UOW3w5V03bI_v63QvqchndGmLrlF3WxlPhHHSN1k3GHeXbuhrFBfnMwTglzY3tdJ8oMJBPOh8Q_zN077XESKr6e6fczRbDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QJeIagX-BhuSbIO3ixABZTWrAjz_X0CAoD2hQVxPVW_nTyPDsRd--Zp6Ojn8uhY9LnWq9Ae4ufIdIOYM7AYbFLTYewxK50msBPkcWSxGSpcB3qGPASg-2xU2fi2PnfLlO8jdWs9tlz99XLVNrC8DRPO_vu8K-QiA7lOIvimjtpazQlD-jpwrQ7vQ1tvVPuRVGuW4M6QxTeu53s8aDxPA53OejfYvxXqFONlJ7eWQvXRk365vWYeexQq1HNlEZ1NZpt893mwLR0iiCveVuI6SV_fw2wxZBnW2VeLmb7I8Jd8X1zDWKNOvDvd_nqcD1W3dz0ipMc-v5G4YkCeDXXZu9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sFNVsGZkND6brNTAWsfKAm1SsMZyXagZn0-VfmU9SpkefcPRxWVQsPQN1JbsJu-j9w_u_wyxKwcqdzEkmcWvz4l1jjCak6hY2qGro1JMkOjecsDrmsgZDQVL63ZF0isSuhFBh_7E6kfNxIgmXuePLL-VVZ6uvLri93cbixOWRSwuuCu9FxTr6gt_QLngFwqhffq6uH5hQnhjja47k0yAab-xSTgVGWQ82W6b2FJSNZp2ZuFVRferhGkCsD_XoQRmoTprfaUVaDtdAd2qhxA7hlDBTv0T0MwaLQ22SyvpWDPNWP2oQQ1uvHo0QBUTZ1yYmx7BJGr4uTxHdv86zQ1_mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XExpUCRxEhLaBk19EYkUCm4NnEHE11Usq0zmnTCyaTFxhnLWT_PbmskjsasqWD7eeCWyAe8h-FbnXu7v6E4hLTm4Je4qvNvkmUeBaaz3lO7Qjcv_nHA3TP6gPjrVvNY_cCK_HIXrNrJMQmwaYGxO-fy2Lsmf99wMgTEauzRjIioNCkKA2v59WGB9SsHjobUBdvzdkWOr5nGALSAqY5LqwV5GfSMpcD0EVsnUswBVYP_EhNnrkdPjd7EyHlolHO8yZrfRHqwRxt-YFpDvDIvKuW8_rWtvMHXfO2tsk_QhGZiHU_DWYIbwzUCxPSL-cVllm2_hgzbV3DLxb1zoUIAmLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GH6oi7liP_5ASP0mhLYsX7dr6Eow0QndsAbMKlEA7PaOvVELBhwnqMxNPL9lPexmvIIrvM4a94bXZVFH7A6Vwuh43coVAAUnpp9dfnK4CW1el8kAxZ3oGbj-7x3jSGCEQk8WZCuoeBow0EP6Ng6X4E7lUAMu_56w1LBk4NmBGQDU-maEcLPAhw048Y033Uc-3u1BHI9Q2JjdwGTzC4b4cHtytjwaokh046zoXZA81HMlqLZJD4rnRlMO3Z2xfREWWgZbrUgtlhFBEZJz6a8Bzst2P5PFx8zsht1vdwkpfe0SYsq8Fleq0Jrp1b3b6JDdULeZvffnsGEmvSgfAaOrIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nYyY4gquvwEOlkGFhjd1XcOPp3TO-ry4y2WOhR-yFnYK9Vfo53XOmUefCV3ge7bp1xmugd1af5BqPac-7YkzO_8nr3MaYqhC3paEjt3XgrXbIrY0nooshGLPS_GcR5pNAGrohySC6ad9aGAizQwTOyU7YIzxIyEqObHWLyq49_hzLS3ScwZanwsBYd6z0zv8ZPtmrjI6lk88gj08VBcqWNa4K3UuH_82PKo6joOKQlX6C9oRsKP6NFa3UC1hKlmLCWbttQ23IzC6n2Yv7DBFcbLcbRox8qKKtpVlyOGuA2N8A2YusfEyHGNrwKj-nM_aRzpPxQ7uYGBkgCx-Zpa12Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q4vCLCpV_Mud1n_1C6srJDsGjqTSzceuQD8B9Wo84b_wBv7v7Abpq9uiiiuOoelhn9uBSkhV0OpYjYs_4sXV-jjhKWJtBVrXPQFb27w_ZOt_oCtCX4Ky3nVZNH4QBG3dqG-ee-agJzXIalKBdhYCvKD5LAKCDmURzTgwrw5He_FA393yGA-srYWmjWW6hKGHoVuN3ADDTIAZm3kBWpAJ_ESWfxACBxaAGs59xgLiaMEKBPNhJyNzsprnWUcpOdp2hZKB4pmRJuUAA05WsLg4dtoGYXUn-qAa9YfmuYnxP4ki2S_D6JuTT_sNnE3Y25iQvgn0LtUcyY0qxH3RCZgIuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07146f6366.mp4?token=iEzLA0_iq0Vz-Q2D1Phv3xSJfFLSJ_UFJRhkO8YJKT7k0pi-zdFxzS8JdBbZZcjL5cF55VFw8l2e8uVnYPY8guXstwZAu6diG5HnT_6RA4PKtH5FAMVunR--olWB3zWSfCCa1GmwTtBqTvGKjsmN5evLZuogM-d3vieLyPOZopI51h-3OFCkqf38NHrDDBMjiy-ijlHKOupG-NuuwTr2Yxnpo2aiYOW_T4cwrZNb6Cg9kmTQ0mDLk-0VZphC3NJJWVcu9CMEZlYTHc04k1gAcAars6nRw7JClf3LrJqgLke-o076VFxTfpRLjL3YtaGclmgg2XYP41-OlJtYNNnzog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07146f6366.mp4?token=iEzLA0_iq0Vz-Q2D1Phv3xSJfFLSJ_UFJRhkO8YJKT7k0pi-zdFxzS8JdBbZZcjL5cF55VFw8l2e8uVnYPY8guXstwZAu6diG5HnT_6RA4PKtH5FAMVunR--olWB3zWSfCCa1GmwTtBqTvGKjsmN5evLZuogM-d3vieLyPOZopI51h-3OFCkqf38NHrDDBMjiy-ijlHKOupG-NuuwTr2Yxnpo2aiYOW_T4cwrZNb6Cg9kmTQ0mDLk-0VZphC3NJJWVcu9CMEZlYTHc04k1gAcAars6nRw7JClf3LrJqgLke-o076VFxTfpRLjL3YtaGclmgg2XYP41-OlJtYNNnzog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم، سربند و دوش انداز جانفدای ایران بر روی شانه و سر و در دستان زنان با غیرت ایرانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/690952" target="_blank">📅 19:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690951">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
هزار دلار پول یه باک گازوییل در ایالت فلوریدا!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/690951" target="_blank">📅 19:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690950">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
پرواز استاد دانشگاه با جت‌پک در چین
🚀
🔹
یکی از استادان دانشگاه ژجیانگ چین در جریان روز بازدید عمومی، با استفاده از جت‌پک به پرواز درآمد و توانایی این فناوری را به نمایش گذاشت؛ صحنه‌ای شبیه فیلم‌های علمی‌تخیلی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/690950" target="_blank">📅 19:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690949">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
هشدار تب کریمه کنگو/ رئیس مرکز بهداشت یزد : با شناسایی ۷ مورد قطعی ابتلا به تب کریمه کنگو و فوت یک بیمار بر اثر این بیماری، شهروندان گوشت مورد نیاز خود را از مراکز مجاز تهیه کنند و از کشتار خارج از کشتارگاه خودداری کنند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/690949" target="_blank">📅 19:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690948">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caae7d32e1.mp4?token=FyZUZFqTvqDl4wH6FX23cLIpPmbaFPpHpKV5FgfNj0SUlbW8Zpvtf-2qmnWmCZcLvdN1yDvq6bCv_Ts2aAE_sI__fksNOCmcfZ-OZGS79wvvuAoLFyty7T_6PM8bthwW319oSaqqLgx99zMMYV8yr9R8qIriyvGyjeVzgAjCUspGb6pm0uawi2DYYprUMxke9nVJ8e9f3-yPEsMcwCHHhSNww8CT7H_He6PlqmITIKMvHUSGXLQoJrKy0MM6ixTTU9_8rqN2eqtI0-K6yAHn4ADWxG2WsB6an7SkO61FAl8EFuZ2OngCMIFQHzotrgHdDpvZCOQn31Xlez24gRU97Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caae7d32e1.mp4?token=FyZUZFqTvqDl4wH6FX23cLIpPmbaFPpHpKV5FgfNj0SUlbW8Zpvtf-2qmnWmCZcLvdN1yDvq6bCv_Ts2aAE_sI__fksNOCmcfZ-OZGS79wvvuAoLFyty7T_6PM8bthwW319oSaqqLgx99zMMYV8yr9R8qIriyvGyjeVzgAjCUspGb6pm0uawi2DYYprUMxke9nVJ8e9f3-yPEsMcwCHHhSNww8CT7H_He6PlqmITIKMvHUSGXLQoJrKy0MM6ixTTU9_8rqN2eqtI0-K6yAHn4ADWxG2WsB6an7SkO61FAl8EFuZ2OngCMIFQHzotrgHdDpvZCOQn31Xlez24gRU97Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخم‌مرغ خام چقدر وزن تحمل می‌کند؟
🥚
🔹
در این آزمایش، میزان تحمل وزن حلقه‌ای از تخم‌مرغ‌های خام پیش از شکستن بررسی می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/690948" target="_blank">📅 19:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690947">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
پرچم ایران روی سرهای جانفدایان ایران در رزمایش ۳۱۳ هزارنفری جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/690947" target="_blank">📅 19:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690944">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa588871d.mp4?token=pcF-aFGnPCJyRpA2fVhtjKvcy6Ii_ILJtbu7GDn_kw5E-1VUy-wGT7mgaQYSWQca1im-cY1R9a1BtfmR8Lev-bOFgOikHpyRoKnb1lZuW5y6LgCvnwhHS49xMrVzJD9qU73iZnfC9o8pe9uaqPQf0HmZ9XqnQUpxoX9498zEOU_2HRoHOH3GchmGo7TqVquHOB2OBvYsNJ2VZfXP_TI233mZU4jrHPHOCr2ZT2Aablhv32JNWnIw0K5PYzXzwKzpNYE9kySYAElSs2IMs5xZVBLmqCJXZ9Jhfn5shgos7Ay3I3pzHUMNwIBln_gRQqgM4FSupk6onMLOAc57of_jyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa588871d.mp4?token=pcF-aFGnPCJyRpA2fVhtjKvcy6Ii_ILJtbu7GDn_kw5E-1VUy-wGT7mgaQYSWQca1im-cY1R9a1BtfmR8Lev-bOFgOikHpyRoKnb1lZuW5y6LgCvnwhHS49xMrVzJD9qU73iZnfC9o8pe9uaqPQf0HmZ9XqnQUpxoX9498zEOU_2HRoHOH3GchmGo7TqVquHOB2OBvYsNJ2VZfXP_TI233mZU4jrHPHOCr2ZT2Aablhv32JNWnIw0K5PYzXzwKzpNYE9kySYAElSs2IMs5xZVBLmqCJXZ9Jhfn5shgos7Ay3I3pzHUMNwIBln_gRQqgM4FSupk6onMLOAc57of_jyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به یاد "مهدیس نظری" فرشته مینابی...
🥀
💔
به مناسبت بازگشایی مدارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/690944" target="_blank">📅 19:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690943">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d3b7367f3.mp4?token=b_lCgFkc7Xe5JQEJIkukclEMKmDWr9grvlJTJ-FxHmHsFDgksSJrKXt02DlkrABCVbEpotwwKatUwcfLQfr_NmAw0DW-ID0q0KVjJdksn2AXXeYW3hRGtjRsQnhVJg96lSqLzBcCNWI55Z1QAXE5F2z9eQQFLajasW9Hj00w-McgTUHujd2a03Kc4Pvw1TupEKBgp7Pbzp8om4C3Iwzm9C6-A0zDDu0zH_BRyU7H1oiPXOK5cp0hkI2ctPnqbHiAXyUIxghM3qrAUaVZ-0hbhQx4gI_QaS8UFKKSj5YbAPAPNIlpghrer4SPzMrMictK1oospho6MyZcLRsUhDK_-zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d3b7367f3.mp4?token=b_lCgFkc7Xe5JQEJIkukclEMKmDWr9grvlJTJ-FxHmHsFDgksSJrKXt02DlkrABCVbEpotwwKatUwcfLQfr_NmAw0DW-ID0q0KVjJdksn2AXXeYW3hRGtjRsQnhVJg96lSqLzBcCNWI55Z1QAXE5F2z9eQQFLajasW9Hj00w-McgTUHujd2a03Kc4Pvw1TupEKBgp7Pbzp8om4C3Iwzm9C6-A0zDDu0zH_BRyU7H1oiPXOK5cp0hkI2ctPnqbHiAXyUIxghM3qrAUaVZ-0hbhQx4gI_QaS8UFKKSj5YbAPAPNIlpghrer4SPzMrMictK1oospho6MyZcLRsUhDK_-zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یاشار سلطانی، خبرنگار: هنوز مشخص نشده که موشک رو کی شلیک کرد (به کشتی‌های عربستان و قطر) و توافق رو بهم زد!
🔹
یه عده خودسرانه موشک زدن؛ کشور داشت آزادانه نفت می‌فروخت و پولش رو می‌گرفت ولی یه عده بی‌دلیل به دوتا کشتی تجاری موشک زدن.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/690943" target="_blank">📅 19:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690942">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/081e9989db.mp4?token=OxVLJks-DActSNHwkLJJwjRupRcrjqpl8AjIVef4dKxpKzM5HJVPOfPl2TIxqjZg4zmTluEvzGuptqofCLHBgk1Ms-8IBozwGkqGmOLDopRWwWEq3BV7D2HNdGbgKvdWgNyNySc57EfsHOXRvd5nAIl9LwABbsGMWbxOt00rbF6in_BpIaUlY0fpXaGGdRl5-T7N2C3KmvoJDL_JcMSKdfFXH1xNSCLE1iy4Wk_J_03maXtgTLa3dwlWreJzjgBfcSRl41x8V0u6yFUVORKjvJNX2kclioNjJA_mUn4rx_RmAkmwslOQVshd3JbAbw3x95WZL12bXzl-I_vL69r4nFYQVZhfiDyR4hzWGeW0yZoGyTQ30hDzBiqL9qsMzme7OHRvIxa4gVXFkHkSuTyK5Dxz_xYlYaN5m9G3mV1vRUxhklhZaY1Yh03yMPZ-vL5YZld9PmY_tjkDZ-Hfgmsziu3DHHKnqJS1sxTJEST7AC925no0Fgd4GmWabI7U2GKp18r69r9iNxbASvgBAVbzoB3_6Te_jmFsguXnTF_gGfuzxc430CY6LZBMXJlLjOCGzvqyBDC8zoRZ4wP1SX3LgWL2BloaiCWJzZzzBcSa94BA4HNmoZhNuSkdDvgTcLIwo_r24edR_OsX4mWNnFPBNJUV-NPTjARjSPOgTZUXOvc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/081e9989db.mp4?token=OxVLJks-DActSNHwkLJJwjRupRcrjqpl8AjIVef4dKxpKzM5HJVPOfPl2TIxqjZg4zmTluEvzGuptqofCLHBgk1Ms-8IBozwGkqGmOLDopRWwWEq3BV7D2HNdGbgKvdWgNyNySc57EfsHOXRvd5nAIl9LwABbsGMWbxOt00rbF6in_BpIaUlY0fpXaGGdRl5-T7N2C3KmvoJDL_JcMSKdfFXH1xNSCLE1iy4Wk_J_03maXtgTLa3dwlWreJzjgBfcSRl41x8V0u6yFUVORKjvJNX2kclioNjJA_mUn4rx_RmAkmwslOQVshd3JbAbw3x95WZL12bXzl-I_vL69r4nFYQVZhfiDyR4hzWGeW0yZoGyTQ30hDzBiqL9qsMzme7OHRvIxa4gVXFkHkSuTyK5Dxz_xYlYaN5m9G3mV1vRUxhklhZaY1Yh03yMPZ-vL5YZld9PmY_tjkDZ-Hfgmsziu3DHHKnqJS1sxTJEST7AC925no0Fgd4GmWabI7U2GKp18r69r9iNxbASvgBAVbzoB3_6Te_jmFsguXnTF_gGfuzxc430CY6LZBMXJlLjOCGzvqyBDC8zoRZ4wP1SX3LgWL2BloaiCWJzZzzBcSa94BA4HNmoZhNuSkdDvgTcLIwo_r24edR_OsX4mWNnFPBNJUV-NPTjARjSPOgTZUXOvc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بحران سوخت به ترکیه رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/690942" target="_blank">📅 19:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690941">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
نوسان قیمت نفت برنت در ساعات اخیر
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/690941" target="_blank">📅 18:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690940">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
ادعای مشاور ترامپ در امور کشورهای عربی و خاورمیانه: رئیس‌جمهور آمریکا برای پایان دادن به درگیری با ایران در نزدیک‌ترین زمان ممکن تلاش می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/690940" target="_blank">📅 18:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690939">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc98ee2c9.mp4?token=Qnr0N0jhaEsiytTNUm3HgyFmwooT5wroGJkuVDq_g9xEoSOD_KVHmu0qrRxPAY0P8D-PXSjONjcy52039pdA597JVLsGOff7BgKESNprXvN6G46kypM-V6H8n3TVZstS9W0aB8V9S9L1pBt9NUX49ibrAUnrUvowrbQDOWTLbwc0Fcj_Y6d1GAvM22pT5RQIljrjNnBuDnkBiLSqIfN_qfImMewojc2Ncr5ow6nkpiYze0oWvjhnc2tSGE6Vnio4iGniWG5RnAOrS2zX_H9V2SYFRwlc5VEOKEMwYbIDaiaTBOC8kM02gaxNyiBGgHY7kqECLeNz6kvUT2V9YkmDAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc98ee2c9.mp4?token=Qnr0N0jhaEsiytTNUm3HgyFmwooT5wroGJkuVDq_g9xEoSOD_KVHmu0qrRxPAY0P8D-PXSjONjcy52039pdA597JVLsGOff7BgKESNprXvN6G46kypM-V6H8n3TVZstS9W0aB8V9S9L1pBt9NUX49ibrAUnrUvowrbQDOWTLbwc0Fcj_Y6d1GAvM22pT5RQIljrjNnBuDnkBiLSqIfN_qfImMewojc2Ncr5ow6nkpiYze0oWvjhnc2tSGE6Vnio4iGniWG5RnAOrS2zX_H9V2SYFRwlc5VEOKEMwYbIDaiaTBOC8kM02gaxNyiBGgHY7kqECLeNz6kvUT2V9YkmDAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور رئیس‌جمهور در رزمایش بزرگ و مردمی جانفدا در تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/690939" target="_blank">📅 18:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690938">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
ادعای یک مقام دولت تروریست آمریکا: عملیات عقب نشینی نظامیان آمریکایی از عراق ۳۰ سپتامبر(چهارشنبه هشتم مهر ۱۴۰۵) تکمیل خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/690938" target="_blank">📅 18:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690937">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
رسانه‌های رژیم صهیونسیتی: پرونده‌ای جدی مربوط به جاسوسی برای ایران از درون ارتش اسرائیل، هم‌اکنون تحت بررسی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/690937" target="_blank">📅 18:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690936">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8531e9c2a5.mp4?token=RZ1PMrE52K7IS635Dkya-VGh4jE7KVTTOagouUxXaKG0AkH_uzMqTMTDJ6-lRdSGdrPUUUIIFq8TJSviHMwBkPq63ygVUgpmAAOOmP3u23uZkQGNQYbZK5YivjZS0VSpMngbrju98KQoeyXDJUY9y_o0USrHlo5C_aflW9gP3fKrGSXysBAXbwz6NUp6M2cPn2q_y1tN7cI6LByDSi1t7xwoh3NkMdcZBIdeYaJ_6Yh55jzVRTu-VjhtFW1yKoHh5qqI6oxaSVV_OydzqbSjgQMiw229JFsnAg8VxKr-_TNBx_3-WchtuHzzxm-mOC7gXzVwVZxo1uVgcHknEQbvCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8531e9c2a5.mp4?token=RZ1PMrE52K7IS635Dkya-VGh4jE7KVTTOagouUxXaKG0AkH_uzMqTMTDJ6-lRdSGdrPUUUIIFq8TJSviHMwBkPq63ygVUgpmAAOOmP3u23uZkQGNQYbZK5YivjZS0VSpMngbrju98KQoeyXDJUY9y_o0USrHlo5C_aflW9gP3fKrGSXysBAXbwz6NUp6M2cPn2q_y1tN7cI6LByDSi1t7xwoh3NkMdcZBIdeYaJ_6Yh55jzVRTu-VjhtFW1yKoHh5qqI6oxaSVV_OydzqbSjgQMiw229JFsnAg8VxKr-_TNBx_3-WchtuHzzxm-mOC7gXzVwVZxo1uVgcHknEQbvCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا حالا مار تازه‌ به‌ دنیا اومده دیدین؟
👀
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/690936" target="_blank">📅 18:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690935">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaTVNlTdHw_D6ZqloAWTrYAc1RWJVE32YLjc5QQbVTBQueUFjWQ8C7R5t2jcWfvhrmGQ-suD9UJSyX3hI_osUBfvbUPtqlruhJuMM84P1oQuFsgyVECvA5ltJ2n3LzuiLuNEsnx2VbrWDy5REOPmwbwMxHu9DFSy0zHq_QvrYtVVjPse_iJixrEqmw4U5CDNSEwc0Ry__zGQdJxOpEhJEXWiQzipoO4-9OJHAjp4gfMldbuI7vOc4fT_xcGVwgRskEn12mhqgm2dwzOOvWL_jlQtFqnouwKURnPYPjOcpnqwzracNUWWpa9jRk7n1Jozd574GpBvMZJuJ4bGkYTcYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیت‌کوین از ۸۰,۰۰۰ دلار عبور کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/690935" target="_blank">📅 18:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690934">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
از گذشته تا آینده…
🗞️
➡️
💡
🔹
دکه‌های مطبوعاتی قدیمی، با چهره‌ای نو و هوشمند، دوباره به قلب شهر بازمی‌گردند.
🔹
این‌بار نه فقط برای خبر، بلکه برای ارتباط، راهنمایی و زندگی شهری هوشمند.
🌐
🏙️
✨
طراحی زیبا و هماهنگ با مبلمان شهری
📍
راهنمای زائران و گردشگران
💳
خدمات شهروندی در چند ثانیه
📺
بستر نوین تبلیغات شهری و محتوای دیجیتال
ما گذشته را حفظ کرده‌ایم، اما آن را با آینده پیوند زدیم.
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh
🔸
http://eitaa.com/mashhadsaman
🔶
https://rubika.ir/mashhadsamesh
🔸
https://ble.ir/mashhadsamesh
🔸
https://gap.im/mashhadsamesh</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/690934" target="_blank">📅 18:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690933">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
طرز تهیه رشته و ماکارونی در هند
🇮🇳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/690933" target="_blank">📅 18:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690932">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
العربیه به نقل از منبع آگاه: وزیر کشور پاکستان طی ساعات آینده به ایران سفر خواهد کرد
🔹
او در تهران درباره تشدید اقدامات انصارالله در یمن گفتگو خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/690932" target="_blank">📅 18:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690931">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/974fee3d52.mp4?token=fOrjyBTmgoeWdxchsl98oZ7OmEh4grvDUJqktr8IzE9yq34FfkpFeADD43TsWxzXtNcrqr1tN2d0C2VZIihwngaV8AQH2vuo90Rta375E2pAoMd2zN8iWa3Z7EIgxvEI9NcLekQDP-FI_NtO51NiIbSD8H5wFMRl0shlL_VEcrPRLKtZh5w_dr64-1TjHlJyhMN1ZkFlmnXLhORL6X6rZmtcn8j3HspXsaWuKxVhDQ12bGUBpXWsii6Nm8U7NloiSdGBmc_IBDrss08aKSay67aySWjQlvhCD5XnhLwUXdjHs2xjJcVsVIZ_zf-S8kt5kAaGP4775QHztFnaq0qslw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/974fee3d52.mp4?token=fOrjyBTmgoeWdxchsl98oZ7OmEh4grvDUJqktr8IzE9yq34FfkpFeADD43TsWxzXtNcrqr1tN2d0C2VZIihwngaV8AQH2vuo90Rta375E2pAoMd2zN8iWa3Z7EIgxvEI9NcLekQDP-FI_NtO51NiIbSD8H5wFMRl0shlL_VEcrPRLKtZh5w_dr64-1TjHlJyhMN1ZkFlmnXLhORL6X6rZmtcn8j3HspXsaWuKxVhDQ12bGUBpXWsii6Nm8U7NloiSdGBmc_IBDrss08aKSay67aySWjQlvhCD5XnhLwUXdjHs2xjJcVsVIZ_zf-S8kt5kAaGP4775QHztFnaq0qslw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برافراشتن پرچم خونخواهی و انتقام در مراسم رژه جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/690931" target="_blank">📅 18:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690930">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d717437bb3.mp4?token=szyKb-TNd9j9h_M7gUk2qpCmFVeLjNDdqZcwCQW8SGVJTT7ftu9GfOfVbweKtJYqR0bX_RR4-MhgRcT7QNbIBdRHZFV-3omw4mDcRA9syuFOqMzYRe0x1im5xH4QTa_wNeT-QjEMibssNorkV8yVpN8ZeoNi-_yGQ0HHpQa1feKT15H56z8EAZWYxrvdP8S0LBSNxGFlavZG-YsP7uV0T9gxpiYvL4SHsvtQvfR-SnlFEOzAPK3e7qwb4DptvR8CcOmAJSiad4GOeh_Qnl3EqFZnc9EPHT7_4IZDEktbdkBXwgfyW6fkL-3_X3t09x2zmQm1QPL0J-xLh-CzluhbMUCNOoX3O9fh0f0x0wWCGlilgYh7BUWAPsJ59LxjwYLQ4zkosjmFf1dswvV2UrcZlcQDVg9DPizljQPTriTmU7x9oEpzBHYuMbY7K1oOu7rklNcqH2rdlnW7mPeljzy7I3hPEmddDJ4c-_UifeGqvIfraokFhvB4Vp9ztV2ut5H28FdllTomIG_l5-8GWHbrD63kTvXx2JlaILhAAHWNINbEhOxCVUrCqmfBDCh0Z8w1-UARZ6QWKsS8ZH8Cz1iNISqYnNY6rLVuczHwz6-bsRiH5pDvZ9w_7b5gJ33BOekndptVlc6mzr7cUTwL9yeSY0x4HO3wiCHQ9jz7wvwPARg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d717437bb3.mp4?token=szyKb-TNd9j9h_M7gUk2qpCmFVeLjNDdqZcwCQW8SGVJTT7ftu9GfOfVbweKtJYqR0bX_RR4-MhgRcT7QNbIBdRHZFV-3omw4mDcRA9syuFOqMzYRe0x1im5xH4QTa_wNeT-QjEMibssNorkV8yVpN8ZeoNi-_yGQ0HHpQa1feKT15H56z8EAZWYxrvdP8S0LBSNxGFlavZG-YsP7uV0T9gxpiYvL4SHsvtQvfR-SnlFEOzAPK3e7qwb4DptvR8CcOmAJSiad4GOeh_Qnl3EqFZnc9EPHT7_4IZDEktbdkBXwgfyW6fkL-3_X3t09x2zmQm1QPL0J-xLh-CzluhbMUCNOoX3O9fh0f0x0wWCGlilgYh7BUWAPsJ59LxjwYLQ4zkosjmFf1dswvV2UrcZlcQDVg9DPizljQPTriTmU7x9oEpzBHYuMbY7K1oOu7rklNcqH2rdlnW7mPeljzy7I3hPEmddDJ4c-_UifeGqvIfraokFhvB4Vp9ztV2ut5H28FdllTomIG_l5-8GWHbrD63kTvXx2JlaILhAAHWNINbEhOxCVUrCqmfBDCh0Z8w1-UARZ6QWKsS8ZH8Cz1iNISqYnNY6rLVuczHwz6-bsRiH5pDvZ9w_7b5gJ33BOekndptVlc6mzr7cUTwL9yeSY0x4HO3wiCHQ9jz7wvwPARg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آکسیوس: جنگ در ایران باعث افزایش تقریبی ۱٠٠ میلیارد دلار هزینه برای مصرف‌کنندگان آمریکایی از طریق افزایش قیمت سوخت، از تاریخ ۲۸ فوریه تاکنون شده است
🔹
ایالت تگزاس بیشترین میزان خسارت را متحمل شده است پس از آن ایالت‌های کالیفرنیا و فلوریدا
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/690930" target="_blank">📅 18:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690929">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/690929" target="_blank">📅 18:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690928">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzQx-lTpDQRdmLYg3xejZIG3F_Ls9AoS82K6XOT9hftDXxd6_vXC96977terrCimFFVcjQpuXimxodApqhTZh8qV4mB9RWcMZVTwG5haAo-JjXMgfT3X5qxqX7Ng1rdyvVs6RU7KuQGKXCMaG1bAEx-TSdUggKeTGM5AnXZJRuvHgYtxDENQ8BRVwYIBoOfLtL3GxvS9iSpK1yUnjCpuUymezafMaTBROY8necGfrrnIplnRUVlGnyMFxBESrjTxL-6BQ1KR8nCgaz5Qr9QUgbfgx98mrCKELyYjDx8j0mPCSBQcBwE95wX3GGmp40du1LvbhNa-T6TRxTlDi_E75Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زبان و ادب فارسی یکی از بزرگترین ظرفیت‌ها برای ترویج فرهنگ و تمدّن غنی ایرانِ اسلامی در گستره‌‌ی جهانی است
🔹
برگرفته از پیام رهبر معظّم انقلاب به مناسبت روز پاسداشت زبان فارسی و بزرگداشت حکیم ابوالقاسم فردوسی  ۲۵/اردیبهشت/۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/690928" target="_blank">📅 18:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690926">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wd5ZRLcbFLfJyqaIz5x2euLRrNyzXDeYJYckwrly7bi7pc5UUDBbxU7DBdsJDrFK2y3aaSrwJz8uSneX2La3afaGVmaGOWt-sbNq5QIk4E6TKb1R_3xH79I0nI8muKfDu7kHq-M7XSxSknL7bAxjH-xOaYxF2Culu4DZs8s60fkA4ORVN-hSsKf7CuHXc-GPkXl4O_ZlLQ53QGqMaCMIuOvshrMRNXWFSiLL7-kZL8vM_uxSEemyWLUTkmGV5vpx2xvLgP9E_AaGVZgynA8dcNd67XSadVWfiFqRhvY84ij3AXsfVatYNUu2qnO3H6k0ZxIhgjNQBrzs-Nblv7A7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd18f3e035.mp4?token=tW5z4snSi1fUB-2kQH7cWpAZxpFTIsMsq3jbT5Iwex5geH1dLsLpAcmrDsWOqKt09hpA0whTAh39UMiGZj2lNFCC4s4bIA02282UZUXhfG3Ad5Gz2yHKvXSdFX-F-p0F911BI5PwXXIeEzvkBdzPQbJu-P06LwhmDAKT5uhJriVLRvaisoIWy4XSUJdrN2mWVuY0rP93IDBHWzbOpoNGyGtFGl1eBrbqqJ1VKPm3epCeo68JbtfX53V1IVI7VR6YfLHvJhULVnQFkDS2PhVMRsbURq7kDk6kIL3IwnBEZzv6w3IHFWJ2b8ZsHiqjctbTjz7yJBWYG6bXuU-qDYg-dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd18f3e035.mp4?token=tW5z4snSi1fUB-2kQH7cWpAZxpFTIsMsq3jbT5Iwex5geH1dLsLpAcmrDsWOqKt09hpA0whTAh39UMiGZj2lNFCC4s4bIA02282UZUXhfG3Ad5Gz2yHKvXSdFX-F-p0F911BI5PwXXIeEzvkBdzPQbJu-P06LwhmDAKT5uhJriVLRvaisoIWy4XSUJdrN2mWVuY0rP93IDBHWzbOpoNGyGtFGl1eBrbqqJ1VKPm3epCeo68JbtfX53V1IVI7VR6YfLHvJhULVnQFkDS2PhVMRsbURq7kDk6kIL3IwnBEZzv6w3IHFWJ2b8ZsHiqjctbTjz7yJBWYG6bXuU-qDYg-dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور مقتدرانه بانوان کلاه‌کج‌ در رزمایش جان‌فدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/690926" target="_blank">📅 17:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690925">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKWhy270Sbfv6up2H0uJerCqLwzdVKyTFiUXhWegYkBf-OSK5rAc5Dlu8LFppEJyNiKazoe9Xmyto2IK7K3YqW3XC1tMBVpQ8crMvDHQlGgdRKJ7xujCQbCnaKxL2705SwKrnUD2GKiTwspFh3FpS8a70DmDjn-TSEj0VRXooaYubOirzTcyubSH7Tv0HrhNteTfNSbctsPAXCicynZTGyrVDql6Vj6sEvHLDXDNXGwGyAc8ZGQprFieRINguXDH_K1euOCAAHQHyYYRVSAe2CMgzLoS1xjHpm0S9dP5NHuvYAFhE9iCru444D219UL4S8aLviGHb2sSdJTQzRsT4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هزینه جنگ ایران و آمریکا؛ ۴۳.۶ میلیارد دلار
بن فیری‌من، عضو ارشد مؤسسه کوئینسی، به نقل از برآورد سنتکام:
🔹
هزینه جنگ جاری با ایران حدود ۴۳.۶ میلیارد دلار بوده که معادل حدود ۵ میلیارد دلار در ماه برآورد می‌شود؛ رقمی بیشتر از برآورد قبلی بازرس کل وزارت دفاع آمریکا./ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/690925" target="_blank">📅 17:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690924">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f327cc1ca.mp4?token=rMFleqE6pq_Z_ctIihPqEBLJYfvf_ac2q_VpKH8wU47rUxMM2IfVnlwvWBBCRgH3J2MTjm1TW3VkRAGERJnhUzqVqwxxxuKBIzycp4mH0yRYRVoiKwuQJU0d60JXWnSAHL0GUB63W8gEaVVhOBfuf0M6ajr9UjdCdaSr3Uk2avwS-jytRfNeFpXJRcj3gpG4f_H8mOa2KrKbXgmMOZvZvXtmOwEG9LuelOHaTI28HEAT4STUdztKVVI7lj1_SgumUZCMEvbMXXSqmqAthaFkazCnBL1RRS1wEARJWgAopuZqZzQcaTVDpX5-v7szsmfo4H65pm3DrRrg85l9y29qOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f327cc1ca.mp4?token=rMFleqE6pq_Z_ctIihPqEBLJYfvf_ac2q_VpKH8wU47rUxMM2IfVnlwvWBBCRgH3J2MTjm1TW3VkRAGERJnhUzqVqwxxxuKBIzycp4mH0yRYRVoiKwuQJU0d60JXWnSAHL0GUB63W8gEaVVhOBfuf0M6ajr9UjdCdaSr3Uk2avwS-jytRfNeFpXJRcj3gpG4f_H8mOa2KrKbXgmMOZvZvXtmOwEG9LuelOHaTI28HEAT4STUdztKVVI7lj1_SgumUZCMEvbMXXSqmqAthaFkazCnBL1RRS1wEARJWgAopuZqZzQcaTVDpX5-v7szsmfo4H65pm3DrRrg85l9y29qOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو وایرال‌ شده از صحنه وحشتناک یک تصادف
🔹
هشدار: دیدن این ویدئو برای همه توصیه نمی‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/690924" target="_blank">📅 17:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690923">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
پیشروی بیشتر انصارالله به سمت غرب یمن
🔹
نیروهای مسلح یمن وابسته به جنبش انصارالله، رشته کوه‌های «الأغبرة» در منطقه «المضاربة» واقع در استان «لحج» مشرف به تنگه راهبردی باب المندب در دریای سرخ را از اشغال نیروهای وابسته به عربستان آزاد کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/690923" target="_blank">📅 17:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690922">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
بحران سوخت در پاکستان و روش‌های عجیب مقابله با آن!
🔹
پاکستان برای صرفه‌جویی در مصرف سوخت، ساعت فعالیت بازارها و مراکز خرید را تا ۹ شب و رستوران‌ها را تا ۱۱ شب محدود کرد.
🔹
دولت همچنین مصرف بنزین خودروهای دولتی را ۵۰ درصد کاهش داده و هزینه‌های غیرحقوقی و سفرهای خارجی دولتی را محدود می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/690922" target="_blank">📅 17:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690921">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aad723577.mp4?token=p6-jzAiCDblgEywWIR4sbRZO4yYgWGT9L3gGagOrfq3uKUR93k3xsPJamiLX6fclGnUY1vMDFns6YmaET6Rmxwi3a-WRns5XP1oqZccu6kbidPkUv_AceVud-Ho-OVL4QCXOo3ATFIU2al5fuFEc5OrCK6Sk9uCHaQzswdzdwCEseutTuUk7lsion8E-4Oy_TM4sQ61aceQjbXoxSgDBo8ym466DqBWtDctbVUqfc9IFL3lHbzn9Wv8S8wLMs2OVpz7VrsYyS0oUwPODB_rSzWhcf4K-4y8hpGDFQqsn-HHSYy0bRWGDEocTKGZ2gMxNGs0wpHwjwXlSw0CsrsH2H1r-ecHzkcesaxdlrZ_wUIwyJHjKJ-yKGBvqgxUlwLJ1o6cqc0SH4u9KkdMKHmUetp0aDdfZy4yfIedXSg1H-qbaZ9I-cPjkNVsc82fb_s0_RSYvru6oqfeRqnRlp6QrSAbDMX3GLpHlP9TB-yJqpm_vCEtlLVsXHlcymWqV5H8IcDhIsyumyLyq0lOwYF3lKWcl5rfva34uVG1fL8iPc4t6dWEutPjsdFfqqkrliYAMj1-fvES_BaRbNmCnEOH2RwqeovmlKPn4YliW2LRvKN0Z8hwx9-PFFoUTD1JG6zSMQ5elrUPO9RgYZcsA7yMW-jg2-usj4A3-NOxN0LRpCWI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aad723577.mp4?token=p6-jzAiCDblgEywWIR4sbRZO4yYgWGT9L3gGagOrfq3uKUR93k3xsPJamiLX6fclGnUY1vMDFns6YmaET6Rmxwi3a-WRns5XP1oqZccu6kbidPkUv_AceVud-Ho-OVL4QCXOo3ATFIU2al5fuFEc5OrCK6Sk9uCHaQzswdzdwCEseutTuUk7lsion8E-4Oy_TM4sQ61aceQjbXoxSgDBo8ym466DqBWtDctbVUqfc9IFL3lHbzn9Wv8S8wLMs2OVpz7VrsYyS0oUwPODB_rSzWhcf4K-4y8hpGDFQqsn-HHSYy0bRWGDEocTKGZ2gMxNGs0wpHwjwXlSw0CsrsH2H1r-ecHzkcesaxdlrZ_wUIwyJHjKJ-yKGBvqgxUlwLJ1o6cqc0SH4u9KkdMKHmUetp0aDdfZy4yfIedXSg1H-qbaZ9I-cPjkNVsc82fb_s0_RSYvru6oqfeRqnRlp6QrSAbDMX3GLpHlP9TB-yJqpm_vCEtlLVsXHlcymWqV5H8IcDhIsyumyLyq0lOwYF3lKWcl5rfva34uVG1fL8iPc4t6dWEutPjsdFfqqkrliYAMj1-fvES_BaRbNmCnEOH2RwqeovmlKPn4YliW2LRvKN0Z8hwx9-PFFoUTD1JG6zSMQ5elrUPO9RgYZcsA7yMW-jg2-usj4A3-NOxN0LRpCWI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصادف دریایی
🚤
🔹
برخورد کشتی گارد ساحلی چین با شناور فیلیپین.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/690921" target="_blank">📅 17:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690920">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c81627115.mp4?token=lIp9auQzh6qwu0wHG65KAbP2wY38vDbOggxo6h-37PwRQesTFt5FzMybTZuOaMWl9WIGv2c4jDSb9p8aXa1Ptd1LeOhxmeE6Vwwi-05E2Iy24G3leYjsMxkPYnHosot79_uErvRWXvS443Yg26CS9UBtMKdW__nyoS10egF_7p5hgotmqFDLms0-gXy5XIU63NaPgxmN-uE2JHOWMOlq7czt_Rh5mmcPIH_HCiOj6G_kzEQZ4c8CdnKeqjpehOhBzByfaeZzZNmO9F1c8LUMKhNCwXYt8q4NzCKnNyv3E84pCHnxXVvqNah7mikWkBADNzaqUfHGhfGddJ76CnQIQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c81627115.mp4?token=lIp9auQzh6qwu0wHG65KAbP2wY38vDbOggxo6h-37PwRQesTFt5FzMybTZuOaMWl9WIGv2c4jDSb9p8aXa1Ptd1LeOhxmeE6Vwwi-05E2Iy24G3leYjsMxkPYnHosot79_uErvRWXvS443Yg26CS9UBtMKdW__nyoS10egF_7p5hgotmqFDLms0-gXy5XIU63NaPgxmN-uE2JHOWMOlq7czt_Rh5mmcPIH_HCiOj6G_kzEQZ4c8CdnKeqjpehOhBzByfaeZzZNmO9F1c8LUMKhNCwXYt8q4NzCKnNyv3E84pCHnxXVvqNah7mikWkBADNzaqUfHGhfGddJ76CnQIQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ابتکار جالب سوپر‌مارکتی‌ها برای مقابله با رسید جعلی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/690920" target="_blank">📅 17:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690919">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
جزئیات جدید از موشک قاسم بصیر، کابوس ناوهای آمریکایی
/
روایت کارشناس نظامی از موشک «قاسم بصیر»؛ ارتقای دقت موشک حاج قاسم با جستجوگر اپتیکی و قابلیت درگیری با اهداف متحرک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/690919" target="_blank">📅 17:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690918">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04ebf0623b.mp4?token=EojJPsb_mDIcN2mn4NybAu0SNDz5Obbk35PNVn5dP29E-5FLXFkzA8FOvvUl-uF8kSb0k3epRdkWFQwRQPayYacQJUE7B5AJ2HZFVZakeTvnyykk-AckZltWHmOALce69WamB4AfH5KPFbVB05LkgBs5EXmK0hkNLNU9s3SEssTAwTBDFJgdVjCv3PywfegSMK5kjWRkjRCwZ52orf4kQuyVXfHfIsDsviEBaqh96EurMwMHStVp4Z1WFBTvROmZvmiSpLy5j83uFH8fxnbLPYwYpSsJEzNUVk_BmEPm2E-GcGJWs8xaYt5bMlRSzJueuFIZf6Uk1J5Oq9nOZcDpUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04ebf0623b.mp4?token=EojJPsb_mDIcN2mn4NybAu0SNDz5Obbk35PNVn5dP29E-5FLXFkzA8FOvvUl-uF8kSb0k3epRdkWFQwRQPayYacQJUE7B5AJ2HZFVZakeTvnyykk-AckZltWHmOALce69WamB4AfH5KPFbVB05LkgBs5EXmK0hkNLNU9s3SEssTAwTBDFJgdVjCv3PywfegSMK5kjWRkjRCwZ52orf4kQuyVXfHfIsDsviEBaqh96EurMwMHStVp4Z1WFBTvROmZvmiSpLy5j83uFH8fxnbLPYwYpSsJEzNUVk_BmEPm2E-GcGJWs8xaYt5bMlRSzJueuFIZf6Uk1J5Oq9nOZcDpUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نودا یوشیهیکو نخست وزیر سابق ژاپن در سال‌ ۲۰۱۲‌ درحال پخش تراکت کنار ایستگاه مترو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/690918" target="_blank">📅 17:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690917">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuy0GuL_MhVc_jUKfctUOYVOsQlXeeFhn_O0NbUyPmrMxW1qp1IfvHmqybWUUXAyG0TIR-yoz-JG6awosJg2cZSibjqGkeVPQozyW_wP6Q--v8wEL6YAK1AAscNNvH9sWZ2r_EwrgSrDS687etNoIOl2ypzZ53POcgcidb8zQV2AI8g828kEMfxKp2zEpkngxlHv82f6o2Nrnw7_yZs03hgERro1gkjQd87yqMVDn_aeil6SOFg-XNIejouySwxQOZ6Ou-8fTXlgYyk0alcBXeEMtLNK7oRdt88MYG_tNMQgB9YVYz7ZErcqcPscZd19GgAraX2Tw2FFGkQEXA1x_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
منابع عربی خبر از صدای انفجار در شهر طائف عربستان می‌دهند/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/690917" target="_blank">📅 17:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690916">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adce80df20.mp4?token=G9d7uQHvoOLOEP9HM72SxRJe-Sqz1KZ-9vl-cVDK68tsMDTSjsm_MMhhD3eHXC6w8MMfReRhjDZ_PT4fazFtYph85nbAYuXYAt4X0ewWPAoqq_2meIKDM6U8bKpAv8o3vDw0EGzXZicUv8fYoAH9TCVKV6uHC5WAOTJO9rxgs7kEkTZnCNsknml4-FhXQFNnwqQ42zxE9-lic0lMBPl_kMxA1oXJwmGVR1F75CHYhoP3u0h55-wDkJwOMp8MXAD9P1KNOfcDqdThjsfMkNwviHRnu6ssYiwRfAZzYkmEnL_hcEVRiCCxLbwLRc2S2GDP1HU7YEj7mBuCFUeLcEnxOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adce80df20.mp4?token=G9d7uQHvoOLOEP9HM72SxRJe-Sqz1KZ-9vl-cVDK68tsMDTSjsm_MMhhD3eHXC6w8MMfReRhjDZ_PT4fazFtYph85nbAYuXYAt4X0ewWPAoqq_2meIKDM6U8bKpAv8o3vDw0EGzXZicUv8fYoAH9TCVKV6uHC5WAOTJO9rxgs7kEkTZnCNsknml4-FhXQFNnwqQ42zxE9-lic0lMBPl_kMxA1oXJwmGVR1F75CHYhoP3u0h55-wDkJwOMp8MXAD9P1KNOfcDqdThjsfMkNwviHRnu6ssYiwRfAZzYkmEnL_hcEVRiCCxLbwLRc2S2GDP1HU7YEj7mBuCFUeLcEnxOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا بهتر است آب را نشسته بنوشیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/690916" target="_blank">📅 17:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690915">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4HMjKZWcY9ynhcoPFz_ly0rm_gzT_GLCZVN3FE5nLKnE6ctQCJmrwvLPmJ45JLKXnvunNIbG9wJ46YT9I1qWadjYVUuNh1U-Leh_2_3ztQFDQGDPsNOZO-GVzBg0t5zCOe3YSNQzCAOWdFwVUPhfIEr_4zcflh5SL8w8r-SlsAwXFqQUyYqwn21-ehbUP3_4eixXxSlNhD02b8z7OrePxOK-fnGbI6jL7NUWMSkS6ksHugX0dQMPOztGRrujInOzmqQHCo6aO4ijbhAuSrQCu7Mc_Sh3Zp4wN_K3Kpc9NAmewupJtNjhkX45p1G3TYudqwUmQ073tjektHE1HFdew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷۵۰ هزار دانشجوی جدید راهی دانشگاه‌ها می‌شوند
🔹
بیش از ۷۵۰ هزار دانشجوی جدید در سال تحصیلی جدید وارد دانشگاه‌ها می‌شوند.
🔹
از این تعداد، ۴۵۰ هزار نفر کارشناسی، ۱۵۰ هزار نفر کاردانی، ۱۳۶ هزار نفر ارشد و ۱۴ هزار نفر دکتری هستند.
@amarfact</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/690915" target="_blank">📅 17:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690912">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IaJdjp6Y2KGEK2YOe5ditScZy3kSaNXbEyU8DF6L5t__mUutOP8QXdUPERPuo214wWEqWy-gMM3Trso3nvnor98WkLkogTKIUz_XA3R1MCkUeBkNK9fln2iHMhDlk0jBkafb33wi7rUWGaEIOONQRoOtYtT2dmKfxFKVhgP0Bhdq23GcecTib_kKJjmG-TFPCmlfBqtUtvXH0bH0mi5ZFO_qTpox6MIp1fJ8r1gQtNFkGZEirWW-FhTQf5645BZLvWVsU_GYf6oCY450m6eOey-LTQqzBEVOABisaFMwbrTeQClMjS7QkLJ7SsIZs7eQJOR1EAmMhKLtm_NtzWJovA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M2YOd7bmxSXX9qYWs3kYzSXenHCrsWCRsfPZMpCOYFsPnFwAGVMBbyfisAm0z-zKbyVsXj7EvsRNzbcOzUowlQ_ikPWW_dkrsvJCjSM8rBReQP9cqtY1MaSDEk7QMnf4d3mVw7IhwSZptck_fKpsv8VwWLgd4lGx4FHGSq9RoJ8bO2GwqItrWt5EteToI7-GSMrRAeRJf-1IeMWYOfrYEya8xBdjFTfEfY6nfi5LQoflQsixGhxmFzc55pJJXUkFIsVUUfB9VUpDuMbQt5ShEKye85RxOy6eiA_HC0modvQHRazCMQjqHH8TQIO2cFcoMy0REhGWgBe22plLtWQMAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KQWMU4LNlbqVx13vgBrPrVgP6S1ju8tRBJne0owXRM9j36NqKdn9Lk2YFhEFBu_k26kxVH5K50l261YkoiDt15-A6-iIDp9qDNgItGZkMt9V6ZkT5N4pOUOsC5aQ7JaDjiWXqRiMaRkzrilaCMuBZJ1FkxxB9HAMBYLiktNw_J_c7xL5gaM7BMvircfWRSD_8D7_HV3j-fjxzrshap1tIgpFxXBzYXfT_e8MKX3Dito8XSKgTrgxHr29B_ffnPTyhqOABEEBkcJrxkvsgMpSuukGMFICjPTeEulSyrS3tjcoIvTfFOuDVi_Dy27ZH0Nu4h9vnTDa3tl586zzNOO6Ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عروس رفته گل بچینه
🔹
حضور نمادین کاروان مراسم عروسی سیریک در رزمایش جان‌فدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/690912" target="_blank">📅 17:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690911">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cd8152537.mp4?token=dQKaAvM7xXRdJbPga1iHJomP6ac311W04uNEr6gIwi9LmnBmk82eswbyyholSUnBoQNButnj-TjOZTfLJ-LvvcK9S3d8Ie274g7HRSb1Q4O69bMxcvePpTGpYaLBvwsS4kCVApbz4Xu_0tKJ1W-diHZVMh0svbx7kWyrGB8IP_sbARjII9Uo2pjwcpBJuL-3nSYYvqie1Jfr3cbLly6MxK-09_EOyS5lXx2Pk3ZynhZ-iXa2XcaHCZovT7TRENJZSHsXMpRcf1_b5efVebWNvKR5bQsqhi8xmrutkbuVgNkFwCDNOHvrZBPjF-uknaN1Mh8ZQFr3yefyVU95Ugx8n6xCk4jtuJ8eMVNEfwshJ78K3HHmt7eUgriTZ0ofv6T186GbQEkuCdt4jzIoFKPI1D1vuE0AbOJCeNG6RjfQUqIKgI20DcAc-upaOg3tLa0yitL6g2gf7fWJ6xqip_PJ6FZJ-aSDbtHOqUG86uQEirH3vTW0AD8FLQgIfA5epTaQS0lyExGFa9XvrPiuv7G9ngNDEzLPMbbGZX9W2njeIvqCijq1UajGcmgoFn0qGO7Uqxt0M6L9jGzRqr8H5HeC0sS8_ENL5NqIaSsowtAbEglrzULN8OlY18uwDLhSt_pwZvl3Nxk8aWuWkuxneabBHjCN7weDuJGKkruarxOPmII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cd8152537.mp4?token=dQKaAvM7xXRdJbPga1iHJomP6ac311W04uNEr6gIwi9LmnBmk82eswbyyholSUnBoQNButnj-TjOZTfLJ-LvvcK9S3d8Ie274g7HRSb1Q4O69bMxcvePpTGpYaLBvwsS4kCVApbz4Xu_0tKJ1W-diHZVMh0svbx7kWyrGB8IP_sbARjII9Uo2pjwcpBJuL-3nSYYvqie1Jfr3cbLly6MxK-09_EOyS5lXx2Pk3ZynhZ-iXa2XcaHCZovT7TRENJZSHsXMpRcf1_b5efVebWNvKR5bQsqhi8xmrutkbuVgNkFwCDNOHvrZBPjF-uknaN1Mh8ZQFr3yefyVU95Ugx8n6xCk4jtuJ8eMVNEfwshJ78K3HHmt7eUgriTZ0ofv6T186GbQEkuCdt4jzIoFKPI1D1vuE0AbOJCeNG6RjfQUqIKgI20DcAc-upaOg3tLa0yitL6g2gf7fWJ6xqip_PJ6FZJ-aSDbtHOqUG86uQEirH3vTW0AD8FLQgIfA5epTaQS0lyExGFa9XvrPiuv7G9ngNDEzLPMbbGZX9W2njeIvqCijq1UajGcmgoFn0qGO7Uqxt0M6L9jGzRqr8H5HeC0sS8_ENL5NqIaSsowtAbEglrzULN8OlY18uwDLhSt_pwZvl3Nxk8aWuWkuxneabBHjCN7weDuJGKkruarxOPmII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جشن تولد ۳سالگی؛ برای مرغ!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/690911" target="_blank">📅 17:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690909">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
ایتالیا ناو جنگی به باب‌المندب اعزام می‌کند
🔹
وزیر دفاع ایتالیا اعلام کرد رم برای تأمین امنیت عبور کشتی‌های تجاری خود، بدون انتظار برای تصمیم اتحادیه اروپا، ناو جنگی به باب‌المندب اعزام خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/690909" target="_blank">📅 17:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690908">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0278da7f4.mp4?token=p68iGRy9qVYWpqy0H8Avwh9i4vlnq9GANTvc-YOjddUn9d_tWCoyA0rCrN6YmPaUjcNReXh3kPvAhJZIJ2-bddidM52SbYZCgwFry1vzGdu4U2sG2ICORCxv7cNY_Md-nrdb4xmXLmACekj-meyStOKiubMiqc3NRWnr56wNBcdWHMaOeijbNno4GlOYy5ImoEP5R_Y4xJy8pRjm3UyKgRQIRsab6MmsrB2jx0OD1bPJcLGR3GWRn9VRcY965cXtTaYe6bf0kzDftlTTOxNHEKs-4Or-ReJA3RwNS_FqiVNQHvfsZqxULQFjp4H3WGD--NW8m0pjZEHL3B5JLQoFDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0278da7f4.mp4?token=p68iGRy9qVYWpqy0H8Avwh9i4vlnq9GANTvc-YOjddUn9d_tWCoyA0rCrN6YmPaUjcNReXh3kPvAhJZIJ2-bddidM52SbYZCgwFry1vzGdu4U2sG2ICORCxv7cNY_Md-nrdb4xmXLmACekj-meyStOKiubMiqc3NRWnr56wNBcdWHMaOeijbNno4GlOYy5ImoEP5R_Y4xJy8pRjm3UyKgRQIRsab6MmsrB2jx0OD1bPJcLGR3GWRn9VRcY965cXtTaYe6bf0kzDftlTTOxNHEKs-4Or-ReJA3RwNS_FqiVNQHvfsZqxULQFjp4H3WGD--NW8m0pjZEHL3B5JLQoFDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی تغییر چهره رویا نونهالی صحیح نیست و مربوط به مصاحبه خواهر اوست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/690908" target="_blank">📅 17:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690907">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5Ufkit4w0JlmxYgrqehkwq0RjzFgQnG4Mp0u_47O0AcyKFfqSK07ahZ31CE-SIrVaimWToQVO0XcZU-s_JpbKPLhHHGLX0-YfQca6Onw3kpdS-5eQBkkO7SzhvhTRGLmIOIth2q-5tYPE1YMslrZab7KqccZdLCUOrEVWxQUMKwCnx7eIEiMS-afOvoxxQ5gc9KCZjtSCU0mhzbiVnp_i3sWvA4tUctB-Z_0bvfYifc0BXTkzz4WfCRyCrVC15hpcIsaUVtzpND39gV3umIsOrJdWvnrrXfOwKAgiywzMyVJjdJ_bWjnJS95WaoI4TS5vP23gnr0X04U7kMrue4PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از ۹ نفر تراستی که طبق ادعای روزنامه کیهان ۱۱ میلیارد دلار نفت ایران را فروخته‌اند ولی پول آن را برنگردانده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/690907" target="_blank">📅 16:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690906">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c705d1f9e.mp4?token=QwERncah59u87AfWuQL6PEu9tm-3Gakjzd8EXvTftMQ60Fmk-D1yts_VF8_aJGxQ4ocJu3X8TkXS12KCJkAhG57gI2JgRHlj6Xo3BL3ZORIiCCxMZhEempWamwUC9yw-eKfnqGaT4GDNXGOnB9nCPI3TpGeY5VQvc36icVrc4ecNXQqG4FuqJt1ZQgTupBTZ0PiWn0Jyynssju2Da-gT9IqQBwxZQoAIEw0XBTCn9_kzGbS6INq7iZTS9u75mKRpTOm9KlK5vgWV3X4rWCyACKSFY94Jxho9eIIA2ww0ZNKFwkPwV0ze2nXoKPBXUe-7D-P0lBQh9d1yNhYyTWOTHQi5YMJt5ZY1v-Nw3FTqbNI03YCnw82NzX5MfqK9kL4RBmAwNcza98tiDiPcd_DrUQ0BgKl6hxp6qFsv2Q-TFqPxbRKBC4W-Vn7IQIIq5P7L1oxcKeI3AqrqImkZ-21xiZuI6p8k5ABT3hbK5xvybLtYJ2xdriUnHU-c877Xwd-LpWxqZI1rIjEaA1jSLxllUuh6m6pUxKp5XqUJHD3wg-9eDxoGG1nHoHRqz2mbX0-CMkAB-SP3QlRO8qQHsfPpfL6OSXaFUghqoWSOjbHo2JEaXfH4Kcz7rd-I2eUxLbcN4gpugxynbX8G1b4gglcpRI-vgZRgGEGczp_a-hS45mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c705d1f9e.mp4?token=QwERncah59u87AfWuQL6PEu9tm-3Gakjzd8EXvTftMQ60Fmk-D1yts_VF8_aJGxQ4ocJu3X8TkXS12KCJkAhG57gI2JgRHlj6Xo3BL3ZORIiCCxMZhEempWamwUC9yw-eKfnqGaT4GDNXGOnB9nCPI3TpGeY5VQvc36icVrc4ecNXQqG4FuqJt1ZQgTupBTZ0PiWn0Jyynssju2Da-gT9IqQBwxZQoAIEw0XBTCn9_kzGbS6INq7iZTS9u75mKRpTOm9KlK5vgWV3X4rWCyACKSFY94Jxho9eIIA2ww0ZNKFwkPwV0ze2nXoKPBXUe-7D-P0lBQh9d1yNhYyTWOTHQi5YMJt5ZY1v-Nw3FTqbNI03YCnw82NzX5MfqK9kL4RBmAwNcza98tiDiPcd_DrUQ0BgKl6hxp6qFsv2Q-TFqPxbRKBC4W-Vn7IQIIq5P7L1oxcKeI3AqrqImkZ-21xiZuI6p8k5ABT3hbK5xvybLtYJ2xdriUnHU-c877Xwd-LpWxqZI1rIjEaA1jSLxllUuh6m6pUxKp5XqUJHD3wg-9eDxoGG1nHoHRqz2mbX0-CMkAB-SP3QlRO8qQHsfPpfL6OSXaFUghqoWSOjbHo2JEaXfH4Kcz7rd-I2eUxLbcN4gpugxynbX8G1b4gglcpRI-vgZRgGEGczp_a-hS45mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت یک توریست آمریکایی از پدیده «دور دور» در ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/690906" target="_blank">📅 16:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690897">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZo4qj9m_J0f5_UezuAwHNXyvtyLJ8_bNeSL4zkMAZQggN6Adv4LxZ1bG3XmW3BmaXrD2DGPuV_loznkHsCzpLLMzpk8HekilIWmnOJiDQcTkuozef2Oxqv7SZfJSvwB-gR9z_z8DdpWS1PC0khzU5HiRImrX2v2z9-VTgTl7LZmXOZVl_okpMf61q3GU8HSqMWUOM1JARdv68U61gD1g_2RqhjAvL0Xu0zbjWhc-nVzE0DmG7KcwIsePg7U6KZHNBFizYHJ95UPE7CPooW2uiPBtNTRTZvuLnVMAkcccELsqBP9GNKRkxLBvEQLhV4-IzB4etqMmCVTSHj1SUWShA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P6fzwc87MXOxc6RQKR_CFkA47e_i9eCcyHADefRHniT9Titnqps8P4HeFCzcBCrIlbeTQ4aRLyedmdJ1ojlroGpdvbWnfa0OLy9zrRQJo_rqqjzH-gXdshc3pf2btp1TTay193Brlbffs80Bzx8vKcJhWb3UWowGkOTOITabUzAkAHW2Dd7Xadby7qAniRIcvBvhIFZmsRgFjw785LniszYNd1ekAbZFj8I_WaM3iHIwuYjT0C8PiZOMEOMX7BlxAUkh3IomJ6n2H8ZEmB1d_qJ-KcvvLWmG4hs2Sdjays5eShqZTnhAF-p4S8gmshzJpr8H8Jqva0Gv8UEcq6i_Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GdzOTYQZFD3gqXbeeSN9fyyZZckDsozWdA_yWjbBe1Ydfy3Kv8tc19tJM9IDXwMLSuGWar194LYSYnzaOr3upeivm_kSlRCmuu8dLzvE_t4mZMOkms4Szdp1KVrCdpePgsZUOltDbf5O0uxYLFVbTxuMP2e9RVs4uUmHVY3X0mXJ_lf05nBFgjOeigP7oZIGAYXiwt15b93Q5Hx2w3niEJRcPYZ75ofXTRHqfk2qxECt8q5jSqUqG_1MBoqgj-Lhv4smun117WDpD2Y1uSg1bIxiAL0y2-GdXkqdwsxWEEYoW0fudUBw_X2ojb3AkBq-9GWU7jeoymctnaS6VYg8dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQsWcgKRF2aNa1OhLjxK4hlFjJb1EmaB0kcEY-VPCH0GfcsaegSyG0U9JT_umhfGboS4mbeRbpYrETT5iFXKaA1Ve5_G-PUvvS-serZnb2rcNzunGbgB7t-BgrdfnvqjhjDP0Av-XSsvLzq2o3RlGT7Ndd0GCvUhlMo_2XKgoE9VR0MB3r-Vtfj5EBGPm-4Wvd1hbrXgZK1_VO3p3q8Eslcy8B5WOfAbXhfvYSgMaMcXqYnlPeJx5K0AB3eEKi0PfRNJ-aG32lpXcRXHd-sNWwFYnw--XVJC62sFSutnfEdidBzJSyqHeJDma6tOZWUm_6SCktGjDTslOgxXXFVx6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jc-zBoZnJ39z85sELhFTPHejLlJYjvDBeM0YhQk8cgoZA27VLusZRT2PlQkBh489T73Pbo7PEWl8uiCJaeTwhOSJNSN2yjkki315Hd6O2gBgxZiMxOlXbrIuVw-r8UPIQ1qOlC_cJaWxBLF6psUnrjUlZ_6ov0zlVW4hQiS9YFF4vuCBLWFJkItmQ9NQBCrDsadCXBgxibI_J2WRNyV26SOJlyiOh0dW0McmAe3_FpGQYYwKQlq73eH7TGGrbMVzyYcrmWUzDSl3puJdulgpzZnb5W2QSh0L3k6nXVJaYSi9UKO81ekj6K1EGQxt7xFOM4Va8sXNByW_dmAGuTVE5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pkFmhHbtquIEhQZIHmk9WKSNyDroPxdyktf9x3150SPSgvZkFoUOJkjP63ErhKFdinQM6Crs3F7fIZmLZpYDHJJx959vDQLH1xGLsRX6FTLo60CIuSbx_YI0HV1hANX68UuoNLfId3a5Hu4ZBqv-wMZUpjt00Km3Mg8-uqErHksi0bLPumVxbwOTegp4Mx-HlyBhbckDGHQtKaQW2zSwgLuV5UUZGcJPZcG3NJW40nLOxN03wUnblsPFXvFXCmgpX8TjXzOikgn1tGFs-4DKxF__fanFOsFy5w08PwivgtDMNTua_G8gLEsQFvITxr-5EQ8Pd5kVxfYCTl-2xe2huw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M73GjLt2cD-Iq64gRbPsoIpMvs_EEmD4A_roisQdA12QKvKs941ThrE4Fe5HfDlOrNpA_NVrrdksHcxPRBscfxiMcFAWqz-XFpWCh3ud2N5Ld3ZB3jEVvA5k48F1XoumTzJAvzrANOCNIyMUMRRblaqUuIS7EKjOr4ipbcy5aVkTvk1BLhRbFpZ_DSp0kVCl88YFeZ8IuGy9rubED_M9pObzJS9j54mN1PX2Lj_y6LedLqAv2gE2k7IsHyluUAW5YF0FyRbqbwyoG4_ATPhVUVZEvZ1Xc5dygNwVv4sSjAdu-snqYypMDTaYbWuy7W1hqUOqOeGcpK0bbTEDw1RR5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2XBHXZ4Dunk42azIQhUVryu9wVxLWRxNb71XRir7MUiG8UezSGHRqLWxne_PMJ9JaMdVtJ9KJ5TPVIUVXuEdKFEVblwapq4kD3IwQq_Jm22iZrZKYhO6DNA9SGx0jkpmuJZsVeeZ_dFsTkrANBaAY21BRRl5vzmouKEm9S5BT3ujmAk35LN6cpZzHTH4C-t2COrq7_dGXMrj98lJKUXgVZ25h5r75pGSRXWxJFl40FmCVoxtIKnrOmPHKs0o9SED0qVVTmIP31sHO9lPqS188fKfjRTApyCF66XF4DmnE58ENYcfJfcTEK2qznEqpr5AbrY9sb3yK2Uk8Vt5HoUmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lG6fW2GbM5VRcIDEAOk8BA5kh6PZl4aoQy6WFtUV5dX6E0iTLWqBjGceB3kqJoRBpyvcZKYADHFX9y8AvVJha7-Ur-0ljIHi-nCm4ck44Y4ZSGmX96BWaWRhi4Z5HWInwpgE347XjSLBPEtOlW5JZqTcZyS6TDrSYJb5ALYlLPu0aKbwM7qypHkACI-clqIb2ctgmWlFYxxttnSOlkdNIiGYsv0mAwXDJKOuXrY0EPOoGrsw5aGdx81yC6CQAd-RpQqJSxOHs5hT-NRYn-GfflCS9jyEWkpD3tK_o1OYh4Gz9jFZqee2c7NjnYKW1CKG2No9pUtsSpxl_UOSGgixJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور ویژه زنان با پوشش‌های مختلف در رزمایش مردمی جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/690897" target="_blank">📅 16:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690896">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
ادعای چاینا نیوزویک: تیم سعید جلیلی به ترامپ بهانه‌هایی برای بهره‌برداری سیاسی داد تا دور دوم مذاکرات اسلام‌آباد را متوقف کند!
🔹
انتقادهای تیم سعید جلیلی از تیم مذاکره‌کننده بهانه‌ای برای ترامپ ایجاد کرد و در توقف دور دوم مذاکرات اسلام‌آباد مؤثر بود.
🔹
این رسانه با اشاره به مخالفت جلیلی با مذاکرات منتهی به توافق هسته‌ای ۲۰۱۵، بر ادامه گفت‌وگو میان ایران و آمریکا تأکید کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/690896" target="_blank">📅 16:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690894">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f234919aa6.mp4?token=YyRaybkVt5oGFAC6OOLRJuzWWvV6TKartK09ETJ0h-QZ-FVEMoYGUb3Y6CGdNZWsUj0DG56fuOS3iXqZbqZNEDnZHHV3d7OlA1lK9AgZyltcZBcDIDUwnRv0HiVEIQTHrpcOFPLvpOxdxQqkAt-xnIIJ37FCONmqRH1-kuYF0DU3O5Xe5qqHfXo8UFmvyE-4iKjl0AZY9zLZd55N2vhu4fs0ERKOOxwPzE8LIUUNsoFczRKeZ5pd01lDBNy77Q-pXSZw3jxSLhwE-j89DxkPTC-5bD69v14HX568lJ3PuW-Dm_cKKl9HocSk-cI-CACF0W0vUfq9aP54wg08UPvRMoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f234919aa6.mp4?token=YyRaybkVt5oGFAC6OOLRJuzWWvV6TKartK09ETJ0h-QZ-FVEMoYGUb3Y6CGdNZWsUj0DG56fuOS3iXqZbqZNEDnZHHV3d7OlA1lK9AgZyltcZBcDIDUwnRv0HiVEIQTHrpcOFPLvpOxdxQqkAt-xnIIJ37FCONmqRH1-kuYF0DU3O5Xe5qqHfXo8UFmvyE-4iKjl0AZY9zLZd55N2vhu4fs0ERKOOxwPzE8LIUUNsoFczRKeZ5pd01lDBNy77Q-pXSZw3jxSLhwE-j89DxkPTC-5bD69v14HX568lJ3PuW-Dm_cKKl9HocSk-cI-CACF0W0vUfq9aP54wg08UPvRMoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل جمعیت در شهرهای یمن به خیابان‌ها آمدند
🔹
جمعیت زیادی در ده‌ها شهر یمن از جمله میدان السبعین صنعا تجمع کردند و حمایت خود را از نیروهای مسلح یمن اعلام کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/690894" target="_blank">📅 16:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690893">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3785fb895a.mp4?token=EHixS4QVoruVKqunkiIyN_ZBuDHR9vzhSNaysCyV_hDVWanmmieu6WPG6eIwI00iYClLd4SkqxNjh-WF5p8getr6ad-kQOKiUaTQH5vdwR375SK6c1uPpPoz6BD68hri0QoY_G0K6V-nA4YT0lgoVtTG_JpZ0_5T3BT6MA5fXtdGOr8itvjj2SNBUQkM0nNgBtIcqYmsUXbWit-g9Tp1AvqLdp0W-Ixw-QcZQ9ucDDC3mr-oAU3CgJWIM3NC1m2ky_Jtl9CrfoSaTrWfUUS49pren6ACwlLPNvtWzCUpCG8_lGDiOyZeXCABMi8QXgAP5wKXuAd-uck0V95lnmIC0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3785fb895a.mp4?token=EHixS4QVoruVKqunkiIyN_ZBuDHR9vzhSNaysCyV_hDVWanmmieu6WPG6eIwI00iYClLd4SkqxNjh-WF5p8getr6ad-kQOKiUaTQH5vdwR375SK6c1uPpPoz6BD68hri0QoY_G0K6V-nA4YT0lgoVtTG_JpZ0_5T3BT6MA5fXtdGOr8itvjj2SNBUQkM0nNgBtIcqYmsUXbWit-g9Tp1AvqLdp0W-Ixw-QcZQ9ucDDC3mr-oAU3CgJWIM3NC1m2ky_Jtl9CrfoSaTrWfUUS49pren6ACwlLPNvtWzCUpCG8_lGDiOyZeXCABMi8QXgAP5wKXuAd-uck0V95lnmIC0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شغل عجیب در کانادا؛ زندگی در ارتفاعات برای رصد و گزارش آتش‌سوزی‌های جنگلی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/690893" target="_blank">📅 16:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690892">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f46e85377.mp4?token=ZVVhuMaolvmXXJFZghvOrGnEdcPYMsNG5wUgByRmSbG9C_jnc_UukFYSxb4yRIkJLHEkrsao1qMsF0_fEZf1jBGUEvW7DebFojLWVIWtzTADHYAMimgqB2DaqDpyMWEXk5HRmcq1-BIF6Gy-Alp9djpEu5uE1Vh0Jqb6-cCQU594DfxtlH9IXN8R-lydqkt6hc8tCz_W_S4cXWDpc21Q4UIaSXRfQzUHQwPI3CtebdqGopF3_fQml1mUgaXSL6JYIBKAkqZqwC0KwyyJhI8ygc5E_fN3X6tYfwqWrOzFIC5xLAyorWtgBGBd6Td5j-5nbjZXnC8N9gbvDjesJvoZxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f46e85377.mp4?token=ZVVhuMaolvmXXJFZghvOrGnEdcPYMsNG5wUgByRmSbG9C_jnc_UukFYSxb4yRIkJLHEkrsao1qMsF0_fEZf1jBGUEvW7DebFojLWVIWtzTADHYAMimgqB2DaqDpyMWEXk5HRmcq1-BIF6Gy-Alp9djpEu5uE1Vh0Jqb6-cCQU594DfxtlH9IXN8R-lydqkt6hc8tCz_W_S4cXWDpc21Q4UIaSXRfQzUHQwPI3CtebdqGopF3_fQml1mUgaXSL6JYIBKAkqZqwC0KwyyJhI8ygc5E_fN3X6tYfwqWrOzFIC5xLAyorWtgBGBd6Td5j-5nbjZXnC8N9gbvDjesJvoZxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همزمان با برگزاری رزمایش، دوی ماراتن ۱۰ کیلومتری امروز در بوستان ولایت برگزار شد
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/690892" target="_blank">📅 16:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690891">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ced362324c.mp4?token=I9mmBkGloMEA8_17W9RIfZHWZnPI9Ix2xkR1K-JLtlXXeAicDqc-kDCGOBJP6ZyicG-pz-_jCxppa6aZZLMmP18Gc7fW7TigPNZCMzUpIaJNV783F-SpEruPCX9blTqdNpux5lCWT6RA0x2pTicihKm9O0KHr3H2ntoyCKAl-0ZxyMLGB4YMLAJCRZ9b5ZXXXT30-HvWm3W26_egOo1IT8JcTTKeaDydLdjIHYGe6To0h2pE2P7gG0soJs-yFU6z972lEL_Ae5T26pin_1pgoCGGZraYufQIwo6hvtHhq0dSXkeBq6QSI3np_wMGYvqqtmhfIb8eQ7c1AwPjVhtfqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ced362324c.mp4?token=I9mmBkGloMEA8_17W9RIfZHWZnPI9Ix2xkR1K-JLtlXXeAicDqc-kDCGOBJP6ZyicG-pz-_jCxppa6aZZLMmP18Gc7fW7TigPNZCMzUpIaJNV783F-SpEruPCX9blTqdNpux5lCWT6RA0x2pTicihKm9O0KHr3H2ntoyCKAl-0ZxyMLGB4YMLAJCRZ9b5ZXXXT30-HvWm3W26_egOo1IT8JcTTKeaDydLdjIHYGe6To0h2pE2P7gG0soJs-yFU6z972lEL_Ae5T26pin_1pgoCGGZraYufQIwo6hvtHhq0dSXkeBq6QSI3np_wMGYvqqtmhfIb8eQ7c1AwPjVhtfqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زابلی حرف زدن محمدرضا هدایتی و ادای احترام به سیستان و بلوچستان
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/690891" target="_blank">📅 16:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690889">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
اعتراف صریح ماکرون: تنگه هرمز اساساً مسدود است و هیچ توافقی برای بازگشایی آن وجود ندارد
رئیس‌جمهور فرانسه:
🔹
در درگیری منجر به بسته‌شدن تنگه هرمز نقشی نداشتیم، اما با پیامدهای آن زندگی می‌کنیم و خواستار راهکار دیپلماتیک برای تنگه هرمز هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/690889" target="_blank">📅 16:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690888">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sl8WaPTSqPy2eJK09jL-9rnwRViP4j1LUY9FkEnp-Q2XOr8AQ9Eq19Njlgphw43jQIRhF6-KY-NaEMarW03poo64nRRrU2dfSkgCcatohkOsFK-mpDfkXKIJP9DAVOprID4RNKKWp1GMfXAx_4TwyFpvE_yjBkqGHf9QkbAQ9JY7OLf_t2VV0ttngvEvU_7F8WIDl2vAerzRFwmXgatuEQPHZnl-CL9XlxTdsKEmcfIHHV_cTfD6CEZaf5hpQFcvEiS9PtNTPK_TiD8JulN_5O-2wPgSVicOyhVac7VftKDvbYmaJ6PFxbCdG4Qk9eL9jrYr2DHNyTfhnV1goMjEmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#دیوارنگاره
| تصویر استاد شفیعی کدکنی روی دیوارنگاره میدان جهاد
🔹
به مناسبت روز شعر و ادب پارسی و به پاس بیش از ۶۰ سال تلاش استاد شفیعی کدکنی برای ادبیات فارسی، از جدیدترین دیوارنگاره میدان جهاد رونمایی شد.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/690888" target="_blank">📅 16:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690887">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nm4UvBFhMmlC90g7agKovfhoRThSXqXirngDdq7PyieqhkgNcYUwSkTPP6V9Zv8cYz0xwe26CWR29N1muC_cnZtnLTMcg9idaTJ3JdlRdBcIr1-Wa6p8pWDhp4t03isuGUBbB-PMoNml5GeOrpR8w3RrqmHtMsaUR1pdyIwYHeP7O8BWyUL-IzU1liO43tf4k4Hi1ufV0kHlnxZ4b6VCwiW2gUrm77OEC7Ule6RNFEf9E2RPXQ6yXKSHhYaDO4mfZTdoQFT9LV45br3bR9d5zhrWJp70QdnulOgdZtsmTj1f91vbJCN8KGzYrdIKhi6f7n0g9VcRS35uCNgOVDRWJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکل اصلی مدارس دولتی از نگاه افکار عمومی
🔸
در این نظرسنجی بیش از ۲۶ هزار نفر شرکت کردند که سهم روبیکا حدود ۵۴ درصد، بله ۲۸ درصد و تلگرام حدود ۱۸ درصد بوده است.
🔸
بیش از ۳۵ درصد شرکت‌کنندگان کیفیت پایین آموزش و روش‌های تدریس و حدود ۲۴ درصد هم کمبود امکانات و تجهیزات آموزشی را مهم‌ترین مشکل مدارس دولتی دانسته‌اند.
🔸
کیفیت آموزش و شیوه تدریس، در کنار کمبود امکانات، از چالش‌های اصلی مدارس دولتی است؛ مسائلی که مستقیماً بر کیفیت یادگیری دانش‌آموزان اثر می‌گذارند.
@amarfact</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/690887" target="_blank">📅 16:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690886">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b17ebd898f.mp4?token=rsptvKZFaalfwXjXZHN4Y2ccz5Mle4w_Ol33JnmjRm7A2_5EVSU-mr_usq4V5qSWZiKIhAgZcg8bBSyL4J01bait21cUNvwN4ub8w7QEb_53NE8-EhoypJtJeJZQP1lOWKFhkoqWmU74zOHCUo_NsVvKGwVYhyeVkg9RL8zmMhr4a2jfIJJqQMx18hlW-HykBurxNYHTo8ZhQFlrlSmdzK_W6I8lSMEKG76g2hjGlMLaxIqG6Nqp3oEv-36sBENiXsdR5MobqLgn22eHnEBjdiVB-l5MVPHPzBwCtseUF-UFboLnWPxdMsaS1T94Gf6UMzc3bMvPEJRwIcqe4X6m-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b17ebd898f.mp4?token=rsptvKZFaalfwXjXZHN4Y2ccz5Mle4w_Ol33JnmjRm7A2_5EVSU-mr_usq4V5qSWZiKIhAgZcg8bBSyL4J01bait21cUNvwN4ub8w7QEb_53NE8-EhoypJtJeJZQP1lOWKFhkoqWmU74zOHCUo_NsVvKGwVYhyeVkg9RL8zmMhr4a2jfIJJqQMx18hlW-HykBurxNYHTo8ZhQFlrlSmdzK_W6I8lSMEKG76g2hjGlMLaxIqG6Nqp3oEv-36sBENiXsdR5MobqLgn22eHnEBjdiVB-l5MVPHPzBwCtseUF-UFboLnWPxdMsaS1T94Gf6UMzc3bMvPEJRwIcqe4X6m-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سفر خارجی بدون مطالعه قوانین/ جریمه شیشه دودی برای ایرانی‌ها ۴۰ میلیون آب خورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/690886" target="_blank">📅 16:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690885">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f7ca0163c.mp4?token=tH9Gt64w4WnEr3vEUhGcZRWHiBx7UiCb9-qAetfIQyzB84KG3AlZ4W-mZxcS6CEaSYxdGge8ufaJzeSXQb6_D749Zztb8xdQVa4fKhmz5fMytPZjKpTtzxk0fFKbbWKitfctkD4aMIObjlIshjK-fCxbEM6h58TgBih-4GgZkodCKRutoOKAJC3ulg5YiGw7kfiTpH224VwWpgD6Zyef_9KcRfNElLV99p_aE4Y9NIfTLZnLVTuyVsv_yYIJM2xjKrUzO0-sXNLj2oTNHl7lEQdvrj54Jr1pz_BKBFoJJaZa392BHs9kj1p-AVTvNVpr0VCvjEnbNwuRQPEtK2Y25joLcQK8n-h2Taw-H_6S7K0LJaup4jBnPqtUMHnrGpjolXz_f5F6XZtM8KJzz0_z0AwTJXzBhZfHYyTNnIhudTJb8IgbzHzRs8wvOPE9YKjETxO63GQoQ3hvFh78G0yylsoagpYOv6ztL8lQjVxJbfzgeH8qLmcjLRFvxqLsmb3emVcrjkjfgn0IV41VjvkiRSoejjY46C-6op-Nh_PFf0INBZ1uKyN1RTz2jD61_SWjuoMyY0zpVDlWfT_5LO0XvaXHxsxKssmywvUsgOc3ltAh3Dds-F28JxsWOe44tGLWwT5suJIj1jLY3pPyDcjRK9iKahbZqdgzNvaMCcflK9Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f7ca0163c.mp4?token=tH9Gt64w4WnEr3vEUhGcZRWHiBx7UiCb9-qAetfIQyzB84KG3AlZ4W-mZxcS6CEaSYxdGge8ufaJzeSXQb6_D749Zztb8xdQVa4fKhmz5fMytPZjKpTtzxk0fFKbbWKitfctkD4aMIObjlIshjK-fCxbEM6h58TgBih-4GgZkodCKRutoOKAJC3ulg5YiGw7kfiTpH224VwWpgD6Zyef_9KcRfNElLV99p_aE4Y9NIfTLZnLVTuyVsv_yYIJM2xjKrUzO0-sXNLj2oTNHl7lEQdvrj54Jr1pz_BKBFoJJaZa392BHs9kj1p-AVTvNVpr0VCvjEnbNwuRQPEtK2Y25joLcQK8n-h2Taw-H_6S7K0LJaup4jBnPqtUMHnrGpjolXz_f5F6XZtM8KJzz0_z0AwTJXzBhZfHYyTNnIhudTJb8IgbzHzRs8wvOPE9YKjETxO63GQoQ3hvFh78G0yylsoagpYOv6ztL8lQjVxJbfzgeH8qLmcjLRFvxqLsmb3emVcrjkjfgn0IV41VjvkiRSoejjY46C-6op-Nh_PFf0INBZ1uKyN1RTz2jD61_SWjuoMyY0zpVDlWfT_5LO0XvaXHxsxKssmywvUsgOc3ltAh3Dds-F28JxsWOe44tGLWwT5suJIj1jLY3pPyDcjRK9iKahbZqdgzNvaMCcflK9Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توهم ازدواج با گلزار؛ روایتی تلخ از اعتیاد و اسکیزوفرنی
🔹
فیلمی وایرال شده از دختری که با مصرف شیشه به اسکیزوفرنی مبتلا شده و فکر می‌کند با محمدرضا گلزار ازدواج کرده و دو بچه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/690885" target="_blank">📅 16:26 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
