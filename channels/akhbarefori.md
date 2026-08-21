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
<img src="https://cdn4.telesco.pe/file/GeJG2unAENGvcz9OFwsX0HPiYyaeOUDDtriiKi_zw1Tq0WOEtcKTXmoHmIf_QbF3YNkhTk3YTUnIGtmc-P43N__Vnbr7TGMEYh1xK_sBj-e_x4EWo5mS_9e639Nw0SeFewdKgS9KxplIlGEs5TltdtNmryNB5A-DWbRikEq69ydkl2wiV6FDomKnlllKPUK5dobBiPyhreM2oqqKVNQ1hP6oXnPq5zMP-OUV-yQpOpmJ0bLH5_PmpRA-XjajV3R2bj_-UXBnulEJgA79j17HjMTMBvEiSP8_eL0PhroF_2JzAYDB5jN6iSli4xWMpFpL0gUarWPhMC_L_3C1Koc6iw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.04M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 04:16:20</div>
<hr>

<div class="tg-post" id="msg-682950">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ترامپ: ما تنگه هرمز را کنترل می‌کنیم
🔹
رئیس‌جمهور آمریکا بار دیگر در اظهارنظری مغایر با واقعیت‌های میدانی مدعی شد که کنترل تنگه هرمز دست ایالات متحده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/akhbarefori/682950" target="_blank">📅 02:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682949">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ترامپ: ما تنگه هرمز را کنترل می‌کنیم
🔹
رئیس‌جمهور آمریکا بار دیگر در اظهارنظری مغایر با واقعیت‌های میدانی مدعی شد که کنترل تنگه هرمز دست ایالات متحده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/akhbarefori/682949" target="_blank">📅 02:33 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682948">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYlQzmQok7sjyl3AlhWqkqWGdm5CkM8GiA4QtJeYvZKxuK-hOLzuD0_tbPAuVHKHdonNDoJvWEVDpjHvTjimFM5WRcIPRdAdH4ld6kUrIgnucWXrKDnxipXuBhutR7_aMUBgiQHFeM8sefvEPATjs88ZXAOQubEPD0_QMgCBgtotcJ3FlJ5rllwhIxpEUyzYMFwldJxgGDQrJrZT-ecATSdt0s1yWBhNldJC7fBZtYzNtYQ9OyHfAx19jV-MRf47qkZMSyihfpZqdU3f92OQF8TtBcIhDOZohTLvb-Zn9nNrWsfDInnpe-iP4V7XJfP43NUZPYOP3KQ4vH1vNagX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به یاد آن سحرگاه جمعه‌ای که پیکر آقای شهیدمان در جوار حضرت رضا علیه‌السلام به خاک سپرده شد
🔹
ای تازه بهشتِ این زمین دارالذکر
ای آینۀ اهل یقین دارالذکر
ما هستی خود را به امانت دادیم
پس باش مراقب «امین» دارالذکر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/682948" target="_blank">📅 01:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682946">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0655d59c4.mp4?token=eGQxqONekQ9ib64Ny5ZPnl8BwgUBNmeVAyRLx6JM9009LJdEV_SEl1YoabrCMwKNTaFKtbwa9eJXugNgsi64K1v__3_TPCv-fZkMFlZ5WZg4D362vdB_yW0hQLRgtx583OISBiUUfxG9x-tCJHPSdcqyCtsUIGRosrUAGBeIZ7Pqr8UwdroxTtOk6BzWH5nKdYeueGc3m-ba3_Bw2IwGsWXC7xkq_gTlCwo-7mNGXSkEZMbE3ZnoPZyeWZEVFpmgZqgWGBux5QRSVpIIIumNQt7caIX1hYORv6-CoIq3s_VQ6l7-8lOF8O1Ocx6AzpeLH_Cuke2d2Se-TxO1VtQhxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0655d59c4.mp4?token=eGQxqONekQ9ib64Ny5ZPnl8BwgUBNmeVAyRLx6JM9009LJdEV_SEl1YoabrCMwKNTaFKtbwa9eJXugNgsi64K1v__3_TPCv-fZkMFlZ5WZg4D362vdB_yW0hQLRgtx583OISBiUUfxG9x-tCJHPSdcqyCtsUIGRosrUAGBeIZ7Pqr8UwdroxTtOk6BzWH5nKdYeueGc3m-ba3_Bw2IwGsWXC7xkq_gTlCwo-7mNGXSkEZMbE3ZnoPZyeWZEVFpmgZqgWGBux5QRSVpIIIumNQt7caIX1hYORv6-CoIq3s_VQ6l7-8lOF8O1Ocx6AzpeLH_Cuke2d2Se-TxO1VtQhxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفندهای کشیدن نقاشی سه بعدی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/682946" target="_blank">📅 01:08 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682945">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIbLD1euGoHSVpT3LG0I-a391wiEPlV2gwX_albnNEcT4U5e0xEi-5pPD0OPjk9mPYd4DMzaDNtb6SGUnTGrOumtHj5YfdkwWVFEMNIj6NxEeuHSoNCv66F6B8uF22AZCWbVW46UaD1WomGzgU1rU5HCrw81HczWgIZoLkKkObXNLtIOMeM-c8FrP0E2u27T_7EGxMXb7Io7bfMUA86fBN2cI_F0uTgFQ_Ekig0CAMdz4Y9P08mRJN4rmuTAONtB6VWjGPc8_ZeoEoEoLJftjeO7Ih-3ll_speFCOOVmLIRhpN-m9I7l0sBvqltWeMIyXdxfuOemSLao9vhDRcGHbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد مرندی در واکنش به پست ترامپ: جمهوری اسلامی فرعون را به زانو در خواهد آورد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/682945" target="_blank">📅 01:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682944">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e460f436ee.mp4?token=T5Crn-TSUZgvlr_lBgTBv6G8y9Ux3dAJGvbFQUVkqf6iOrf5i64i5jqsqAyhyc2s9BWObvL1U0fnpZ2PCEUk_V9eTa0ni_PFQ7OURMUaFnoJyx539BqJ2vIvdLyU8aE0NooF1Hl7bht3VyT4MkKWJVMGRlzPTsJRZgLkzHvhU9u7Kj5quauaMMMHvWLWsAnc35E9ojh1S_BWcRBb6H3jGX3hCR0C8kk-op-TE3pCCHGtArhsPRPySDzAQTUtz7zhLxKfcjlRUQ8rigq8jTOzP_0oM2FohyS0q6qxW4UzfkToYQ8WyvPe08Hewj2jBl2C7OQ6tloW0gnqxSuLPT9AaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e460f436ee.mp4?token=T5Crn-TSUZgvlr_lBgTBv6G8y9Ux3dAJGvbFQUVkqf6iOrf5i64i5jqsqAyhyc2s9BWObvL1U0fnpZ2PCEUk_V9eTa0ni_PFQ7OURMUaFnoJyx539BqJ2vIvdLyU8aE0NooF1Hl7bht3VyT4MkKWJVMGRlzPTsJRZgLkzHvhU9u7Kj5quauaMMMHvWLWsAnc35E9ojh1S_BWcRBb6H3jGX3hCR0C8kk-op-TE3pCCHGtArhsPRPySDzAQTUtz7zhLxKfcjlRUQ8rigq8jTOzP_0oM2FohyS0q6qxW4UzfkToYQ8WyvPe08Hewj2jBl2C7OQ6tloW0gnqxSuLPT9AaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساخت کیف پول و کارت با چند تکه مقوا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/682944" target="_blank">📅 01:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682943">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
گزارش‌ها از حملۀ هوایی اسرائیل به ارتفاعات علی‌الطاهر در جنوب لبنان حکایت دارند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/682943" target="_blank">📅 00:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682942">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
گزارش‌ها از حملۀ هوایی اسرائیل به ارتفاعات علی‌الطاهر در جنوب لبنان حکایت دارند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/682942" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682941">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سالی یک متر از آب دریاچه ارومیه تبخیر می‌شود
محمد کوهانی، دبیر ملی شبکه‌های محیط زیست کشور در
#گفتگو
با خبرفوری:
🔹
سالانه حداقل یک متر تبخیر از سطح حوضه آبریز دریاچه ارومیه را داریم که طبیعی است. اکنون تراز دریاچه به ۱۲۷۰.۹۳ متر رسیده که نسبت به سال گذشته، یک متر و ۱۳ سانتی‌متر افزایش داشته است.
🔹
همچنین وسعت دریاچه با ۲۸۵۰ کیلومتر مربع، نسبت به سال گذشته ۲۲۴۴ کیلومتر مربع افزایش یافته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/682941" target="_blank">📅 00:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682939">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZ0jTfUliz_EeDtDTJEN5n6yow7LdFokZW0-GB8qpbljLmIbdOU1FKxqX4arhEF_VY1ZyZC2sl-6uYkozxSLibpGF4lDoyuiqs5AvCrtr0yKR8SXftLoggjLSVJGUMEEOjnoXlVI8L6P8zmo_Az6S5CG3Sc3ndh74YRBFWjKqrckkXkmUlUM2v_Q-BSqh4ZKhss_KGm8qIaOmzTYMoEUs-EzgcHndBnR7eT9S1vaueNPIQoRbRDTrGPTCsTUM79KspZzMXZncXp33qj_qvYtSTlHoXoyJ6X-oabhZZ7xD9VlSEBIAv48hfN37xDGSK3aiV2Cql3ZIxwbcXXHdbDQ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش فارسی آلن ایر، دیپلمات سابق ارشد آمریکایی، به تهدیدات اقتصادی ترامپ علیه ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/682939" target="_blank">📅 00:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682937">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoquNDAYnrufNTO8u2W6ve9KjzpKgx6Wa8pyQH0TDHMdSmztU3OkqUsNOhCEtJRhsJKPMjuzTxjp985A60me1U0zAa2uS0s5je4_UjBpcwzYpknlJC5q0ljAJKP96Q5lEEf1bs6F09HdVcrMgPP6ScRA1Ev_rgZT87HiTJALfH4UZ2g0jdxH8jRJhTc95IGDRkPteh-46b0qLdwu67WHmt45RIqYZCPZOKB9MBoqn6-CcBUMh8OqoWS7sXb2s5stp2Ro1cVdzn7sFg4S0cDBfZ5NgdXUbXxKxO_xBY6SIcs7rxtqzINSJdrfv-i0PF6ocv5tnATFc4WehGjIaEbY3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله پهپادی به دو منطقه‌ در جنوب لبنان
🔹
به نقل از المیادین، ارتش رژیم صهیونیستی پنجشنبه شب، مناطق «علی الطاهر» و «المنصوری»  در جنوب لبنان را هدف حملات پهپادی خود قرار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/682937" target="_blank">📅 00:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682936">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ناو بحران‌زده لینکلن عازم آمریکا شد
🔹
ناو هواپیمابر «یواس‌اس آبراهام لینکلن» روز پنجشنبه پس از یک ماموریت ۹ ماهه که بخش اعظم آن در پشتیبانی از عملیات‌های ایالات متحده علیه ایران سپری شد حرکت خود را به سمت بندر خانگی‌اش در سان‌دیگو آغاز کرد.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/682936" target="_blank">📅 00:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682935">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aec764cbf3.mp4?token=Sb7zjjyH4nlaWTwIKMC_G62GB_7vlR-3_R6BCbmhmukhRDuzUvfugAJBnmT_tA7PJFWIrllSteNnAQ88EhpVijlQDufqyPTk4GMwxj9Oks6kjGZsMw07C86FeRj6WsXSxtPNqvsaF5BSDQpa7boFxavL-MX1SKk_WEXYBfH7DtooiNXOt3HhWFwV1iwxhePGaEf6hiGLO-1mkL6jIR9xV6kizJR4UYGxFYNI-UC-Oto-8eFtnaFRQQ5mFb0lc48ghY8ZUxkuQLbhoKhx9id5zsadpikSszPOZKOQSnWYL8BoeAeAjpP3KBnfeIdQgII3BQlQXy7XzVJC9uQTGAbCGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aec764cbf3.mp4?token=Sb7zjjyH4nlaWTwIKMC_G62GB_7vlR-3_R6BCbmhmukhRDuzUvfugAJBnmT_tA7PJFWIrllSteNnAQ88EhpVijlQDufqyPTk4GMwxj9Oks6kjGZsMw07C86FeRj6WsXSxtPNqvsaF5BSDQpa7boFxavL-MX1SKk_WEXYBfH7DtooiNXOt3HhWFwV1iwxhePGaEf6hiGLO-1mkL6jIR9xV6kizJR4UYGxFYNI-UC-Oto-8eFtnaFRQQ5mFb0lc48ghY8ZUxkuQLbhoKhx9id5zsadpikSszPOZKOQSnWYL8BoeAeAjpP3KBnfeIdQgII3BQlQXy7XzVJC9uQTGAbCGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غیبت ملانیا ترامپ از ترس ایران ۲۵ روزه شد!       وبسایت Wonderwall:
🔹
ملانیا ترامپ پس از انتشار ویدئویی که سرویس مخفی آمریکا آن را تهدیدآمیز و مرتبط با ایران اعلام کرده بود، ۲۵ روز است در انظار عمومی دیده نشده است.
🔹
مشاور او می‌گوید ملانیا آرام و قاطع است…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/682935" target="_blank">📅 00:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682934">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ایرانِ فردا را نسوزانیم!
🔹
بیشتر از یک ماه دیگر، زنگ آغاز سال تحصیلی به صدا درمی‌آید، اما حقیقت این است که سال‌های تحصیلی ما بعد از کرونا، دیگر هیچ‌وقت شبیه گذشته نشدند.
یک روز سرما، روزی آلودگی هوا، روزی تعطیلی و حالا جنگ...
🔹
هر بار بحرانی از راه رسید و چیزی را از مدرسه گرفت. گاهی یک روز، گاهی یک هفته، گاهی ماه‌ها از کیفیت و استمرار آموزش.
🔹
و هر بار، آموزش‌وپرورش آرام‌تر و بی‌صداتر، یک قدم دیگر به حاشیه رانده شد.
🔹
اما مگر می‌شود آینده یک کشور را به حاشیه برد؟
فناوری را می‌توان خرید. کارخانه را می‌توان ساخت. ماشین‌آلات را می‌توان وارد کرد. حتی عقب‌ماندگی‌های اقتصادی را می‌توان، با سال‌ها تلاش، جبران کرد اما انسان توسعه یافته را نمی‌توان وارد کرد.
انسان توسعه‌یافته، محصول سال‌ها تربیت است، محصول همان کلاس کوچک.
🔹
و کودکی که قرار است پشت نیمکت بنشیند، فردا پشت میز تصمیم‌گیری این کشور خواهد نشست.
آینده یک کشور، یک‌باره ساخته نمی‌شود،
🔹
آرام و بی‌صدا، هر روز در کلاس‌های درس ساخته می‌شود.
پس لطفاً آموزش‌وپرورش را فقط یک وزارتخانه، یک ردیف بودجه یا مجموعه‌ای از ساختمان‌ها و کلاس‌ها نبینیم.
آموزش‌وپرورش، کارخانه ساختن آینده ایران است.
🔹
آموزش‌وپرورش این چند سال با زخم‌ها و چالش‌های جدی روبه‌رو شده و هنوز به ثبات و قوامی که شایسته نسل آینده است، نرسیده است.
حالا یک سال تحصیلی تازه در راه است و این بار نباید اجازه بدهیم بحران‌های امروز، آینده کودکان را هم تعطیل کنند.
🔹
مسئولان، پیش از آنکه دوباره تقویم را ورق بزنند، سال تحصیلی جدید را جدی بگیرید.
برای مدرسه‌ها، برای معلم‌ها، برای دانش‌آموزان، برای تداوم آموزش، برای روزهایی که نباید از دست بروند، فکری کنید.
🔹
کودکان فقط آینده ایران نیستند، آنها ایرانِ فردا هستند.
و ایرانِ فردا، از همین امروز، در کلاس‌های درس آغاز می‌شود
.
#سرمقاله
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/682934" target="_blank">📅 00:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682933">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjw2-82zcPNqvbl8J51waMZcAo6I0k9Eu20JweO1bSFx9i6e5a82rJtfcg2au3h2XBoTC8NIRSEVob7MarlQAWcJoU491m9EY6JiqExpy0VxkBNbLTIhBVuoLvVfXPJ-wc9ytmQSZsipdv3-4CrT1Vp7HSJ9uA8UrJbSJOk21kuCDbNv00fJZxMJKckayMMbVuT7jfJa0t2LFI_zUsgEjoPeW7bN21XQzD0ia4-3HrbYYYg9kML1FLzw8z8Q_xtK8RHZ4SMw7JBsyqjYpOFcg1n0BfKj9bYeWjwVQa06vkhNiaMFEsybSNorfmtnmmCWpcjIcIc3UPn_NHugaCMXtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/akhbarefori/682933" target="_blank">📅 00:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682932">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
ادعای جنجالی اکسیوس درباره کریدور مرموز آمریکا در بخش جنوبی تنگه هرمز | آمادگی اسرائیل برای حمله پیشدستانه ایران
👇
khabarfoori.com/fa/tiny/news-3239064
🔹
سیل خودرو خارجی در راه ایران | سقوط قیمت خودرو در راه است؟
👇
khabarfoori.com/fa/tiny/news-3239150
🔹
یک پیش‌بینی تازه درباره زمان حمله احتمالی آمریکا به ایران
👇
khabarfoori.com/fa/tiny/news-3239076
🔹
«فروختن گذشته»؛ وقتی آینده از دسترس خارج می‌شود | چرا عکس مهمانی‌های خصوصی ایران مورد توجه قرار گرفت؟
👇
khabarfoori.com/fa/tiny/news-3238977
🔹
موج تازه تحریم‌ها علیه ایران | وزیر خزانه‌داری آمریکا: فشار اقتصادی جایگزین درگیری نظامی می‌شود
👇
khabarfoori.com/fa/tiny/news-3239179
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/682932" target="_blank">📅 23:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682931">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
میانگین روزانه معاملات خورد بورس از ۳۷ همت عبور کرد
🔹
هفته پایانی مرداد برای بورس تهران با یک جهش قدرتمند به پایان رسید؛ شاخص کل ۳.۷۷ درصد و شاخص هم‌وزن ۵.۱۱ درصد رشد کردند و به‌ترتیب به ۵.۹۵۲ میلیون و ۱.۶۸۶ میلیون واحد رسیدند.
🔹
در این هفته میانگین روزانه معاملات خرد از ۳۷ همت عبور کرد؛ رقمی که با وجود کاهش نسبت به هفته قبل، همچنان بالاتر از میانگین ماهانه ۳۱ همت بود.
🔹
پول حقیقی هم در مجموع حدود ۴.۵ همت وارد بازار شد؛ دارویی‌ها و فلزات اساسی در صدر جذب نقدینگی قرار گرفتند، در حالی که فرآورده‌های نفتی و بانکی‌ها بیشترین خروج پول را تجربه کردند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/682931" target="_blank">📅 23:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682930">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf377f0d6.mp4?token=J1LIMwia6Qkam481EJVJQK9q0rAvW_fG8ByAOyCviB8v53Jfw5Xrk4bNHN6uwLrS5e6ldfz_a9ok4bQs92NVXEXPxge9kqT1fdxIXHmgQkZxcHnG25Ozyr-RBSe9MQd3WTviNbf4QfR_VXwhxkPbQpD7Ct4-HhFQo0oFh2nAUsra8BrwjBS7CPFpvhuZkl9ofbancfWFFZ3p1gOOFzEhfJkPiusLevQEtTzAOmcHYX4DLS3JQ9CeCurfVPvU5-0P-Jh5GM9c_sgcxJi2tTPySJjOCN6dcIHiTIm_5oDHC8L2dW3g9Vc6IxcyDw5fYIOn0DOJMg8sL50m2YEoq-HsQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf377f0d6.mp4?token=J1LIMwia6Qkam481EJVJQK9q0rAvW_fG8ByAOyCviB8v53Jfw5Xrk4bNHN6uwLrS5e6ldfz_a9ok4bQs92NVXEXPxge9kqT1fdxIXHmgQkZxcHnG25Ozyr-RBSe9MQd3WTviNbf4QfR_VXwhxkPbQpD7Ct4-HhFQo0oFh2nAUsra8BrwjBS7CPFpvhuZkl9ofbancfWFFZ3p1gOOFzEhfJkPiusLevQEtTzAOmcHYX4DLS3JQ9CeCurfVPvU5-0P-Jh5GM9c_sgcxJi2tTPySJjOCN6dcIHiTIm_5oDHC8L2dW3g9Vc6IxcyDw5fYIOn0DOJMg8sL50m2YEoq-HsQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، کارشناس حوزه مقاومت: با توجه به فشار دشمن، احتمال سقوط بخشی از تأسیسات علی‌الطاهر لبنان در روزهای آینده بالاست/ همزمان دولت لبنان به‌جای تمرکز بر اشغال جنوب این کشور، فشار بر جمهوری اسلامی و نمایندگی ایران را افزایش داده است/ آمریکا، عربستان و رژیم صهیونیستی به‌دنبال حذف و تضعیف جمهوری اسلامی از معادلات لبنان هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/682930" target="_blank">📅 23:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682928">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f158b8bc4.mp4?token=NUl8qCOGQU45ome9H-NJ8GV-KfwG32yi8B50W6sRsSt_a0scxO_Mypb1l7Cv3mmxjn-Ja7Xw7_QW8Mybr01m0skrJiazUt0SxvE287wQHa2-dxqATi8VAF9t1elWZWB9EjwwRae0MRTGGtWbJnnaoPKRtbYDr3mixB0bd14vp9LnjDU5qURGGVtwVt1NxyaI9CihpCIb3CX9tulD1IKZqJgh1ucLMTT4hI3uawT7KnDtYx3UJ04oKneEGa9vmc3h1SHPz3j01KieLKMHcwb5I5F4FXF-Fx3chBOvLq2dF0YpiI1Tp2Kcly49ON9SQL5GTV5ne_snf9GIjPFm0SgNDxxXLtflncxcQFNq6kVESpRCx-et9GO6rEGSB6IjjIHd1sWgNNZl-ar8it9zX-UZOWiWBnbBlFSuO8cF5lAZuFXu13xCx1ppUobxf_FVAgx_L6SNFhfv7QEhnwTcYbqd5c_f-XqrzZtDWRChfxiXYLkwjYt556UomghbBaDKdw0dtfwYe4x4uBsMahCEJfZ7c_sKlxO_lff1eL8jSNRaf7gner-sSqOF1O6PF5TComPMaiZ9qulfrozbZ6hcubsgK7IlP4w87fv9Eo6d5vaNDoh_DJYq6pL96sqUcnuluVKi57iXpbn5embIH_DjKlRiBlgwdT9wftOJuSRdmlYE8sE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f158b8bc4.mp4?token=NUl8qCOGQU45ome9H-NJ8GV-KfwG32yi8B50W6sRsSt_a0scxO_Mypb1l7Cv3mmxjn-Ja7Xw7_QW8Mybr01m0skrJiazUt0SxvE287wQHa2-dxqATi8VAF9t1elWZWB9EjwwRae0MRTGGtWbJnnaoPKRtbYDr3mixB0bd14vp9LnjDU5qURGGVtwVt1NxyaI9CihpCIb3CX9tulD1IKZqJgh1ucLMTT4hI3uawT7KnDtYx3UJ04oKneEGa9vmc3h1SHPz3j01KieLKMHcwb5I5F4FXF-Fx3chBOvLq2dF0YpiI1Tp2Kcly49ON9SQL5GTV5ne_snf9GIjPFm0SgNDxxXLtflncxcQFNq6kVESpRCx-et9GO6rEGSB6IjjIHd1sWgNNZl-ar8it9zX-UZOWiWBnbBlFSuO8cF5lAZuFXu13xCx1ppUobxf_FVAgx_L6SNFhfv7QEhnwTcYbqd5c_f-XqrzZtDWRChfxiXYLkwjYt556UomghbBaDKdw0dtfwYe4x4uBsMahCEJfZ7c_sKlxO_lff1eL8jSNRaf7gner-sSqOF1O6PF5TComPMaiZ9qulfrozbZ6hcubsgK7IlP4w87fv9Eo6d5vaNDoh_DJYq6pL96sqUcnuluVKi57iXpbn5embIH_DjKlRiBlgwdT9wftOJuSRdmlYE8sE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیچ‌جای آیات و روایات نگفته صدای معین و مهستی و داریوش حرام است!
/ تلویزیون اینترنتی مدار
موضع عجیب یک روحانی درباره خواننده‌ها
👇
https://www.aparat.com/v/mkfc6hp
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/682928" target="_blank">📅 23:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682927">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تولید خودرو نسبت به سال قبل ۴۰ درصد کاهش یافت
محمدرضا نجفی‌منش، رئیس انجمن قطعه‌سازان خودرو در
#گفتگو
با خبرفوری:
🔹
تولید خودرو نسبت به یک سال گذشته ۴۰ درصد افت پیدا کرده که جنگ، نرسیدن به‌موقع مواد اولیه و کمبود نقدینگی از مهم‌ترین دلایل آن بوده است.
🔹
این کاهش تولید باعث شده حتی قطعی برق در تابستان هم فشار خیلی محسوسی به بیشتر واحدها وارد نکند، چراکه اگر برق هم می‌بود شاید کاری برای انجام دادن وجود نداشت.
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/682927" target="_blank">📅 23:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682926">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73d2f9f680.mp4?token=NYgOZity48dVpueft7ONkt2ZPXqtp6cGHytuaEl8DjJKGWQ-33lrL7WwdDH589T7ifvzYah8LOlH8PymB4CcyiyFf-9Qfg2lfrDzy4CAlGiSAiPWfBZ5WReab70l7Ll1hSm9ly7AxSbHgibQo1JgNASitJcbH8yG9qFmjh3pCkJ3QAIHyIzMEAVuZxKWHluSfyOQlkkjMgjJza3em1ShikPsqY3TmT7D7fBECklQY_eUJzcZVFhK2mcS3Rjjpm50niLIIN3nvpET1sB4FG6VG9vYoricUbwR_hcQHHa8aQq8dzGuIFKNqwCgoASnyVruO6YSO9cn6HVNe949QoqVbXdusokFBNZXcUycs-G2tjIhyIwhZLHEJdbigRk9XfPRsRHn5-ZE1tpOsNM-IJ-MxOC9VQVeCjUgSrarORiwsSJJ9sSmvFi7MgXSgHK6HdHAC0A_wsYCq8uy_oh8RFhw1tLgRZNegT7R-8j0Lz2nFnwury4nA7a6H0IIDFbTzXDWLLaxbxcXfQu8kdQPuKAUjISmWq80QEi5EE1rbvx32VSEHCNbKNIRrtgoT5O3ynq4tvadRGGC12hlFn-3md08Siy81Sqt0dnilym4N67wplWWIXB3IlWPiByq169ltgle8y1BNdSmacsaRs0yksK6af7ESdgADuKW-uFmz2E_euo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73d2f9f680.mp4?token=NYgOZity48dVpueft7ONkt2ZPXqtp6cGHytuaEl8DjJKGWQ-33lrL7WwdDH589T7ifvzYah8LOlH8PymB4CcyiyFf-9Qfg2lfrDzy4CAlGiSAiPWfBZ5WReab70l7Ll1hSm9ly7AxSbHgibQo1JgNASitJcbH8yG9qFmjh3pCkJ3QAIHyIzMEAVuZxKWHluSfyOQlkkjMgjJza3em1ShikPsqY3TmT7D7fBECklQY_eUJzcZVFhK2mcS3Rjjpm50niLIIN3nvpET1sB4FG6VG9vYoricUbwR_hcQHHa8aQq8dzGuIFKNqwCgoASnyVruO6YSO9cn6HVNe949QoqVbXdusokFBNZXcUycs-G2tjIhyIwhZLHEJdbigRk9XfPRsRHn5-ZE1tpOsNM-IJ-MxOC9VQVeCjUgSrarORiwsSJJ9sSmvFi7MgXSgHK6HdHAC0A_wsYCq8uy_oh8RFhw1tLgRZNegT7R-8j0Lz2nFnwury4nA7a6H0IIDFbTzXDWLLaxbxcXfQu8kdQPuKAUjISmWq80QEi5EE1rbvx32VSEHCNbKNIRrtgoT5O3ynq4tvadRGGC12hlFn-3md08Siy81Sqt0dnilym4N67wplWWIXB3IlWPiByq169ltgle8y1BNdSmacsaRs0yksK6af7ESdgADuKW-uFmz2E_euo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پدری که چشم انتظار فرزند کنکوری خودش بود، قبول بشود یا نشود زندگی ادامه دارد/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/682926" target="_blank">📅 23:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682925">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
نماینده دائم روسیه در سازمان ملل: روسیه ایران را برای از سرگیری مذاکرات با آمریکا تحت فشار قرار نمی‌دهد
🔹
ایران یک کشور مستقل است که خودش تصمیم می‌گیرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/682925" target="_blank">📅 23:38 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682924">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6ce052442.mp4?token=Gc8-siZ2AYUgAQgBVERdxTQ1o4oMr9xJRbzq6gN-pvoKbhfcqGGFbVn8IQFbWSK5kb--6N38qbJUkzJ-3YjYT0wcLuJN1-Ri610V6iU3zAbAC-VfXeKnQGq2COSDUNdeaNC-m_ZPpLhEIvlr8W4EcwoEI2Thbo18G9_rLpO4qc6lHjaauJ8O1T9T7LHAWOIsKo-m4u4Ou-hlBWxeylkMbV__qXylLJjDFYRKOwrzKsbyhqBuVq1DXTw4-6bzdofh84K3oe5ZjYDFD7uNMvR75ViRCaJ8lwV-HOmF5KTyRtt3n6sd_HfAFIp30sCoSTgTFrBNkbYEYEJ8YEJA5uo6nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6ce052442.mp4?token=Gc8-siZ2AYUgAQgBVERdxTQ1o4oMr9xJRbzq6gN-pvoKbhfcqGGFbVn8IQFbWSK5kb--6N38qbJUkzJ-3YjYT0wcLuJN1-Ri610V6iU3zAbAC-VfXeKnQGq2COSDUNdeaNC-m_ZPpLhEIvlr8W4EcwoEI2Thbo18G9_rLpO4qc6lHjaauJ8O1T9T7LHAWOIsKo-m4u4Ou-hlBWxeylkMbV__qXylLJjDFYRKOwrzKsbyhqBuVq1DXTw4-6bzdofh84K3oe5ZjYDFD7uNMvR75ViRCaJ8lwV-HOmF5KTyRtt3n6sd_HfAFIp30sCoSTgTFrBNkbYEYEJ8YEJA5uo6nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صنایع دفاعی؛ نمونه‌ای از اقتصاد مقاومتی
امین طباطبایی، استاد دانشگاه و اقتصاددان:
🔹
ما در تولید صنایع دفاعی کاملاً تابع اقتصاد مقاومتی هستیم؛ این موضوع تا حد زیادی به چرخه تولید داخلی و ایجاد اشتغال نیز کمک کرده است./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/682924" target="_blank">📅 23:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682923">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تاراج ۲۵۰۰ مگاوات برق کشور توسط ماینرهای غیرمجاز
مصطفی رجبی مشهدی، معاون برق و انرژی وزارت نیرو در
#گفتگو
با خبرفوری:
🔹
عده‌ای با استخراج غیرمجاز رمزارز و مصرف ۲۵۰۰ مگاوات برق، فشار مضاعفی بر شبکه وارد کرده‌اند.
🔹
در حالی که کشورهای پیشر‌و مانند روسیه برای تامین امنیت انرژی خود و جلوگیری از اتلاف منابع، استخراج رمزارز را تا سال ۲۰۳۰ ممنوع و جرم‌انگاری کرده‌اند، ما همچنان در حال مقابله با سودجویانی هستیم که برق مردم را می‌بلعند.
🔹
این ۲۵۰۰ مگاوات، معادل ظرفیت تولید چندین نیروگاه بزرگ است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/682923" target="_blank">📅 23:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682922">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxy0ATacKUgrRcows8N2cRjIC2mTdfMpiQqnJkQxHYhQ9dLKuxVeOQ5GwqN8ArPAA5waJ2aQVq5KzdLt4gdalINh3kbUiUX7EQIPqGs1S65NGpDr891aShpD_n7Mt8wCh3eEQaHPjt3ZuPLf-NaDGwC1wii8ngjmokmykrZO5A9JGsXa235kUu9RQWynEJhRt82CbPDKAAfy5E_RmDb_w9rmkxHE94K2PMkxMukALi1mibLtmd4agK0QfbVr61BFt2UnFOOGoyR-ek2bApxjod2srZ0QgaV7mgp43dy0-3IWZyWntG_6hXP6AeJ-tjWkfZYj2e5b8FOW-4kn3zPM2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای پولیتیکو: جنگ ایران زمینه بازگشت دزدان دریایی را فراهم کرد
پولیتیکو:
🔹
جنگ ایران زمینه بازگشت دزدان دریایی سومالی را فراهم می‌کند و تهدید پرهزینه دیگری را برای مسیرهای کشتیرانی جهانیِ پرتنش اضافه می‌کند.
🔹
جنگ ایران به دزدان دریایی سومالی که کشتی‌های تجاری پر از سوخت و کالا را شکار می‌کنند، جان تازه‌ای بخشیده است، تهدیدی که سال‌ها خاموش بود.
🔹
به گفته ویندوارد، یک شرکت اطلاعات دریایی جهانی، اوایل این هفته، گروهی از دزدان دریایی یک کشتی باری را در سواحل سومالی تصرف کردند. این پنجمین حمله از این دست از ماه آوریل بوده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/682922" target="_blank">📅 23:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682921">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b3f784dbc.mp4?token=H4LEBTocwx-PeaaNTH3IHKFgMtJkD_D_r_Emcmp9jDUinrx0dEyYtTfNsGnHufi99biwIW13b8XEj-aI_sXiIpA9wpPW5Lm1unQNGK5xUhM-eAdo_SdJW6FNvVymfOSD3ucGHVB16zbYFXZXibTayjdHX2CQv3_72FJ4m5lPP1USZkeoE7Q-8GJ62q8ihqrA5AY6yUZV4svPP67YPHqqj6IMzs0uqztdJavxie-fxzFN9rvOlHjsyLzMShrYa0FXzxOUsGSzNbDZi17adBQOxHg_5_ubY-8NpfOyypoSghyVzmUeRKjxoxgkfHxIQsaLYGBWrJQ1czVtGleMcU2BQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b3f784dbc.mp4?token=H4LEBTocwx-PeaaNTH3IHKFgMtJkD_D_r_Emcmp9jDUinrx0dEyYtTfNsGnHufi99biwIW13b8XEj-aI_sXiIpA9wpPW5Lm1unQNGK5xUhM-eAdo_SdJW6FNvVymfOSD3ucGHVB16zbYFXZXibTayjdHX2CQv3_72FJ4m5lPP1USZkeoE7Q-8GJ62q8ihqrA5AY6yUZV4svPP67YPHqqj6IMzs0uqztdJavxie-fxzFN9rvOlHjsyLzMShrYa0FXzxOUsGSzNbDZi17adBQOxHg_5_ubY-8NpfOyypoSghyVzmUeRKjxoxgkfHxIQsaLYGBWrJQ1czVtGleMcU2BQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفند کاربردی پاک کردن چربی از روی هود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/682921" target="_blank">📅 23:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682920">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b616f7192.mp4?token=L8QKf69H_QKNr-z2meWtMQVdJaudqoy1vdaL2LVr5Philwb2CldhHCeHUEpVZ6Yw4ie2j9PzTxyc_WmzY8hzU4pD1pxCIlvPuVfFRUi-fJzrnbwXpuqonV5TATr-3WhtWn8KcKYeMKPF_08hI5xNF4P5pnNvMvOWczS0E4kKOtq8eyKB-AE79vCiD2CDU5HXxDIbmT23_wGrkaWnhYpmOBSkx2UhpNny8lFYkY30gFzcZI0M0mRnT4l3oVwVDkf5BrXLBYBQT2NtGxC5hsdndVC84Um6mk3bB8-cUgCmoy3XZO6MPJ20-UcUsonAH_dc5sAAJcx30A28u9cxigud6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b616f7192.mp4?token=L8QKf69H_QKNr-z2meWtMQVdJaudqoy1vdaL2LVr5Philwb2CldhHCeHUEpVZ6Yw4ie2j9PzTxyc_WmzY8hzU4pD1pxCIlvPuVfFRUi-fJzrnbwXpuqonV5TATr-3WhtWn8KcKYeMKPF_08hI5xNF4P5pnNvMvOWczS0E4kKOtq8eyKB-AE79vCiD2CDU5HXxDIbmT23_wGrkaWnhYpmOBSkx2UhpNny8lFYkY30gFzcZI0M0mRnT4l3oVwVDkf5BrXLBYBQT2NtGxC5hsdndVC84Um6mk3bB8-cUgCmoy3XZO6MPJ20-UcUsonAH_dc5sAAJcx30A28u9cxigud6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای
ونس متوهم: باید مطمئن شویم ایران دیگر به‌دنبال بازسازی برنامه هسته‌ای نیست
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/682920" target="_blank">📅 23:18 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682919">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c72520a86.mp4?token=Rm0TxykH_z8zcG6u8vaAZk9UgJl2A1uKU8bUiOk1Vp6CFwbe-BXIKGvtvxj7pdEeE751fi_64_kvHNnEQ7P9AWdsw19aKrwaqrOrIe93fMUKPVrs_AHhTnXrPH3i2rw9ywdKIIvj-xXsdMI1DaWc7GsKVro9-n0LFpAZKvJOIkS6u3fAMZoudcvUY8rXY6Aw5PQbjfe1mgXR8YzqyeHhI6-jBEeapYAtEveKSUXPi-LwnlnvEDYpNH_TL_TpXoc39EnwQ4EpLIczjLtDdKNbGHdivHvI6kl8uhDG-J7_3HKVJqwejJzMpOEfVPMe462W2pY3tdYVOOvRLSJ3sOhuEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c72520a86.mp4?token=Rm0TxykH_z8zcG6u8vaAZk9UgJl2A1uKU8bUiOk1Vp6CFwbe-BXIKGvtvxj7pdEeE751fi_64_kvHNnEQ7P9AWdsw19aKrwaqrOrIe93fMUKPVrs_AHhTnXrPH3i2rw9ywdKIIvj-xXsdMI1DaWc7GsKVro9-n0LFpAZKvJOIkS6u3fAMZoudcvUY8rXY6Aw5PQbjfe1mgXR8YzqyeHhI6-jBEeapYAtEveKSUXPi-LwnlnvEDYpNH_TL_TpXoc39EnwQ4EpLIczjLtDdKNbGHdivHvI6kl8uhDG-J7_3HKVJqwejJzMpOEfVPMe462W2pY3tdYVOOvRLSJ3sOhuEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر طراح سوال الان جلوت بود بهش چی میگفتی؟/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/682919" target="_blank">📅 23:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682918">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
یمن: مانع عبور ۴۸ کشتی شده و ۸ نفتکش را هدف قرار داده‌ایم
🔹
عمر البخیتی، سخنگوی دولت یمن (مستقر در صنعاء) و معاون وزیر اطلاع‌رسانی این کشور، از دستاوردهای نیروهای مسلح یمن و تثبیت معادله «محاصره در برابر محاصره» علیه عربستان سعودی تمجید کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/682918" target="_blank">📅 23:13 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682917">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
مالک شریعتی، عضو کمیسیون انرژی: عرضه آزاد بنزین بعد از اجرای طرح باید سقف قیمتی داشته باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/682917" target="_blank">📅 23:09 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682916">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
ادعای ونس: ما به فشار اقتصادی بر ایران ادامه خواهیم داد و در نهایت به هدف خود خواهیم رسید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/682916" target="_blank">📅 23:09 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682915">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69d47f6841.mp4?token=qFyQ2ayovhJuABThcXVy7wUBrg-EVIAnpHzxiCj9evRHw6_gXErx0rBggLksrFx3KobRQYIrFQ7ZhyxwGKfn2r_Kr_OoOxR5tsHwdH66PQn4V0vRytK7WYwjcy2lLPJR_k3h_D11DtCZ_jdwl3_7dW08b8zUskWZQbiUynwI-q35Rh8VP_atbWN68t8Z7wNCvD31Z9ACgoH-vqZHELKyzB6RKy5chz-ewKYToiwKeu7pJCrMe4wvhVUVNdFVZKdeFxl8jcdalgNUkDzrYnLwdHrdbHb1fc6dVSQBJ6VgU_rLuv1vgY1Gkn-4W0CUAGm9L7gHO3nOATE2dsAb_vpzVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69d47f6841.mp4?token=qFyQ2ayovhJuABThcXVy7wUBrg-EVIAnpHzxiCj9evRHw6_gXErx0rBggLksrFx3KobRQYIrFQ7ZhyxwGKfn2r_Kr_OoOxR5tsHwdH66PQn4V0vRytK7WYwjcy2lLPJR_k3h_D11DtCZ_jdwl3_7dW08b8zUskWZQbiUynwI-q35Rh8VP_atbWN68t8Z7wNCvD31Z9ACgoH-vqZHELKyzB6RKy5chz-ewKYToiwKeu7pJCrMe4wvhVUVNdFVZKdeFxl8jcdalgNUkDzrYnLwdHrdbHb1fc6dVSQBJ6VgU_rLuv1vgY1Gkn-4W0CUAGm9L7gHO3nOATE2dsAb_vpzVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سانحه هوایی مرگبار در آمریکا
🔹
برخورد بالگرد پلیس با یک هواپیمای کوچک در فرودگاهی در ایالت پنسیلوانیای آمریکا، یک کشته و دو زخمی بر جای گذاشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/682915" target="_blank">📅 23:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682914">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b70v5t5qpl7qvfQr15InG57D0RX_2WauNXnHtSLSeeQUWjjdUNQddma2lWFDIhoi4VBgb3MbEGaR2EIzteOihI9LJoQPIlgfkjMM6l-Z7fsjEGxbJFstwjijWFpOwvwOhrgmkqb01LjJMsNG5LnbSI45VvYjqeEWJmq6SiwLtWmU7ZyXrqySDvxriR0affIj6j9XJ6XVe1mPB4Tp1IrPvl9jMuBLdYKFc7hg9Y_TuEdzPBLtJJQo2buqXHKTdz30xrZ3j1GcmqyvxMLm5K1QM6D3BtSqxo3zlklaAx8SdKOoq1EGI4qT6DCsqFazv84-QYz9sF0_ED__sFbcC6OCbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین اقدام ناتو در بلغارستان از ترس حمله احتمالی ایران
خبرگزاری bta بلغارستان:
🔹
شورای وزیران بلغارستان در یک بیانیه مطبوعاتی اعلام کرد که رومن رادف، نخست وزیر با مارک روته، دبیرکل ناتو، گفتگوی تلفنی داشت.
🔹
طبق گزارش‌های رسانه‌های خارجی، این دو در مورد فضای امنیتی اروپا با تمرکز بر خطر احتمالی اقدامات تهاجمی ایران گفتگو کردند.
🔹
روته شخصاً حمایت کامل ناتو را تأیید کرد و از آمادگی نیروهای دفاعی اتحاد برای پاسخ به حمله احتمالی خبر داد. در بیانیه مطبوعاتی آمده است که هرگونه حمله به یک کشور عضو ناتو به طور قطعی به عنوان حمله‌ای علیه اتحاد تلقی خواهد شد و تمام اقدامات ناشی از پیمان آتلانتیک شمالی متعاقباً انجام خواهد شد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/682914" target="_blank">📅 23:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682913">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ظهوریان، نائب رئیس‌کمیسیون اقتصادی مجلس: در صورت افزایش قیمت بنزین ۶ تا ۸ میلیون تومان هزینه به دهک‌های فقیر اضافه می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/682913" target="_blank">📅 22:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682912">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ناو یواس‌اس جورج واشنگتن وارد خاورمیانه شد  سازمان تروریستی سنتکام در بیانیه‌ای:
🔹
گروه رزمی ناو هواپیمابر جورج واشنگتن پس از ورود به منطقه تحت مسئولیت سنتکام، در چارچوب یک استقرار برنامه‌ریزی‌شده در خاورمیانه در حال فعالیت است./ ایسنا
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/682912" target="_blank">📅 22:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682911">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/105f0ad8e0.mp4?token=kUZN0G2g4PDKyAmpShM2aTzZ4L7JEjJGFKpCWBi0dnWq9jE-pqLZzesHaLxawrz5THpbtUuyxojw7mudiIFlnw8HRvR6uT1Ua0146Io6z8akQkCOAx8s1Fiu1FgTCYmT2lnHH6t4BZenmKpGARtXArWloB7SEfpv62zljNG0iQcS5znMayFkKSak0M8lXzsumMn-4n1s5BUWqpI5mzcElQjtyanUw4KU7Vqaedc2y_Z1dwndTfZAd7xHh3wbJ0kXXhL0prjJbyWv5dAgjMaQDecPkQlo1O9KTyifqjP9geijqh2_p8OWwu9xhAMT60xMTSQrYx_heX_wpMyoN9kyMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/105f0ad8e0.mp4?token=kUZN0G2g4PDKyAmpShM2aTzZ4L7JEjJGFKpCWBi0dnWq9jE-pqLZzesHaLxawrz5THpbtUuyxojw7mudiIFlnw8HRvR6uT1Ua0146Io6z8akQkCOAx8s1Fiu1FgTCYmT2lnHH6t4BZenmKpGARtXArWloB7SEfpv62zljNG0iQcS5znMayFkKSak0M8lXzsumMn-4n1s5BUWqpI5mzcElQjtyanUw4KU7Vqaedc2y_Z1dwndTfZAd7xHh3wbJ0kXXhL0prjJbyWv5dAgjMaQDecPkQlo1O9KTyifqjP9geijqh2_p8OWwu9xhAMT60xMTSQrYx_heX_wpMyoN9kyMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مالک شریعتی، عضو کمیسیون انرژی: طبق آمار رسمی روزانه ۲۰ میلیون لیتر سوخت قاچاق می‌شود که ۸۰ درصد آن گازوئیل است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/682911" target="_blank">📅 22:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682910">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
ظهوریان، نائب رئیس‌کمیسیون اقتصادی مجلس: افزایش قیمت بنزین مثل چیپس و پفک نیست که راحت بتوان قیمت آن را تغییر داد
🔹
هیچ‌کدام از ۳ طرح مطرح شده، برای بنزین مناسب نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/682910" target="_blank">📅 22:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682909">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
الجزیره: کشتی‌ها از بیشتر دستورات آمریکا سرپیچی می‌کنند
🔹
الجزیره با استناد به داده‌های شرکت کپلر گزارش داد از ۱ تا ۱۹ اوت، ۲۳۶ کشتی از تنگهٔ هرمز عبور کرده‌اند که ۸۳ فروند به‌طور آشکار از مسیر ایرانی استفاده کرده‌اند، درحالی‌که تنها ۳ فروند از مسیر عمانی عبور کرده‌اند.
🔹
براساس این گزارش، در میان ۱۱۲ شناور نفتی و گازی عبوری نیز ۲۱ فروند مسیر ایرانی را انتخاب کرده و تنها ۲ فروند مسیر عمانی را برگزیده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/682909" target="_blank">📅 22:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682908">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93342efec.mp4?token=h4ng3ZUo-dwyPb93BcBdZaZj1kLJtJhvbXrBf0iq8kvON3a26BHA5VJmrSRBpnTppEJgseoSNwZNatwVUONsOGmo5gq2dH5RpaPiJSsZbX4iw0lqU1MLJR7k5tTZ24t2zZZF2PYPMknxYuqj2Kmoyoy1yPbv17VhRdloGx2Q1cGkF9K4LY3ceglTC7DQbtslLxPA84s0UQRiv_SLnnK2UzJ0ihqHUyQd3dUR7bLwin4pnsirKG_vFzmE8T3nzBR8RwyPvZc7l-g5y24wz6JWs4Kar_EMq2FuEHqlXu-WJjDkEofcfBAAQ-7rqMRHfvAp-9udbY4WDIIkzfBq8mP13Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93342efec.mp4?token=h4ng3ZUo-dwyPb93BcBdZaZj1kLJtJhvbXrBf0iq8kvON3a26BHA5VJmrSRBpnTppEJgseoSNwZNatwVUONsOGmo5gq2dH5RpaPiJSsZbX4iw0lqU1MLJR7k5tTZ24t2zZZF2PYPMknxYuqj2Kmoyoy1yPbv17VhRdloGx2Q1cGkF9K4LY3ceglTC7DQbtslLxPA84s0UQRiv_SLnnK2UzJ0ihqHUyQd3dUR7bLwin4pnsirKG_vFzmE8T3nzBR8RwyPvZc7l-g5y24wz6JWs4Kar_EMq2FuEHqlXu-WJjDkEofcfBAAQ-7rqMRHfvAp-9udbY4WDIIkzfBq8mP13Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مالک شریعتی، عضو کمیسیون انرژی: تخصیص سهمیه نباید به تعداد خودرو باشد و باید به خانوار تعلق بگیرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/682908" target="_blank">📅 22:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682907">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنهاد کتابخانه‌های عمومی کشور</strong></div>
<div class="tg-text">📚
🍯
کتاب شیرین؛ مسابقه‌ای برای بچه‌های کتاب‌خوان
نهاد کتابخانه‌های عمومی کشور با همکاری شبکه نهال برگزار می‌کند:
🎙️
مسابقه تلفنی «کتاب شیرین»
👧🏻
👦🏻
ویژه کودکان و نوجوانان
📚
کتاب‌های مسابقه در شهریورماه:
۱. «سی قصه با پیامبر(ص)» | حسین فتاحی
۲. «روزی روزگاری ایران؛ هنوز یک نفر باقی مانده» | مهدی میرکیایی
۳. «روزی روزگاری ایران؛ با نام دیگری صدایم بزن» | مهدی میرکیایی
🗓️
شنبه تا چهارشنبه
🕕
ساعت ۱۸
📺
شبکه کودک | کانال نهال
لینک خبر
📌
@iranlibraries</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/682907" target="_blank">📅 22:41 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682906">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b118b3002.mp4?token=rFyHdA8e5ikZw9TtkW8_xmDJlyfUUuJc8NeHqsEB-BQ7ZV77RIrgzZFIhIJWaSB5scI8wJn3VTSrtOTqFaN8F5lJaATJxy4rUKP3cSMXc5qhslq5rwyuaRAf5CSBjbAMv7QInzfczggb-YzAqCEcXm4WS3rFPxq0S1CqJAzLpjQQy3MZnR6dFDMsfJlqkamMopsTxXDJZM-P1L3zKqVWLKQXfJ8ymH59Qflqm8WWHrVHzodJ4baY6tROJ5O1jwVCdi3ROiMMtxYGGL1qWoLzxJuo1OmZ9KfmGTQowkKEr1g76BgMv5fdq6V7g0xF0SvOLAEbdvdtYcRhsTvPeGXHJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b118b3002.mp4?token=rFyHdA8e5ikZw9TtkW8_xmDJlyfUUuJc8NeHqsEB-BQ7ZV77RIrgzZFIhIJWaSB5scI8wJn3VTSrtOTqFaN8F5lJaATJxy4rUKP3cSMXc5qhslq5rwyuaRAf5CSBjbAMv7QInzfczggb-YzAqCEcXm4WS3rFPxq0S1CqJAzLpjQQy3MZnR6dFDMsfJlqkamMopsTxXDJZM-P1L3zKqVWLKQXfJ8ymH59Qflqm8WWHrVHzodJ4baY6tROJ5O1jwVCdi3ROiMMtxYGGL1qWoLzxJuo1OmZ9KfmGTQowkKEr1g76BgMv5fdq6V7g0xF0SvOLAEbdvdtYcRhsTvPeGXHJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روش‌های بهبود رتبه اعتباری برای وام
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/682906" target="_blank">📅 22:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682905">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4WgJtfHQXPD4fM6QeizzgsAAsunXDI71rVp4LUa3JDyMYtA85bixw_e7hmO3QzKLGNSnIQU_KdKVvMumyzLt1wnEJJ0fyY5mbSolqItxlag4_g0Guxj0oduBxO6mSNm2gFcuObG9jsVQPhFMFPyX23P0fIGWsFMjgCvuLWKG7hICSgNcKg6E5XizlDx27t7ONLOc2B2uNiJ5hD_WrTFKJL2bK8ZkrmSsBOS5a2d3khH0nr1RPOuz5nvyiN9U7-ndxUYECyTOwf1jE9eyW7lq1XrBg0IGZWYtE5sivXVf7i0vB6teokaimHWUfGRHi4G-QwvtX5kjUnPHyuioi5SFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار ویدئویی از ترامپ ۸۰ ساله با پوشک بزرگسال!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/682905" target="_blank">📅 22:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682904">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a47126c77.mp4?token=FvDmT_YkEdu6MOxDdkLfSOu1qiTjclhZv9PkhqbYR89GWVQONNEJaha-y9BYaeK8p1GXNOsiz7BdNRHcs3R-Wpm2Xnt655Bx5iNu2Okgo1Wj469wlbxoSgh3UqFTQY5vmUCdztL2Sbv6vhqyt1MS5AEbYMuIUzfGaI9yT2Na0BZJdMQFZ_WphspPg7WFSXwSlwxfMfnQqSm2uZiy7IG24ogCQuJ-u_1AjcTv1m3_pw62sxmbQ-ma_ZX3DxcgREUNcbSxIdZOPJaFxPp1_b9dKJEZ39hdEDVtyFqMSJkwuEo93RUpw-m7mgNq9msrv-IYXwypzWF-VQOwgnp6OJUfDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a47126c77.mp4?token=FvDmT_YkEdu6MOxDdkLfSOu1qiTjclhZv9PkhqbYR89GWVQONNEJaha-y9BYaeK8p1GXNOsiz7BdNRHcs3R-Wpm2Xnt655Bx5iNu2Okgo1Wj469wlbxoSgh3UqFTQY5vmUCdztL2Sbv6vhqyt1MS5AEbYMuIUzfGaI9yT2Na0BZJdMQFZ_WphspPg7WFSXwSlwxfMfnQqSm2uZiy7IG24ogCQuJ-u_1AjcTv1m3_pw62sxmbQ-ma_ZX3DxcgREUNcbSxIdZOPJaFxPp1_b9dKJEZ39hdEDVtyFqMSJkwuEo93RUpw-m7mgNq9msrv-IYXwypzWF-VQOwgnp6OJUfDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مالک شریعتی، عضو کمیسیون انرژی: در حال حاضر تخصیص بنزین به خودرو است نه خانوار؛ ۴۷ درصد خانواده ها حتی یک خودرو هم ندارند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/682904" target="_blank">📅 22:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682903">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
بنگاه‌های متوسط، آب رفتند
🔹
داده‌های اتاق بازرگانی ایران از یک تغییر نگران‌کننده در بازار کار خبر می‌دهد. در فاصله اسفند ۱۴۰۳ تا مرداد ۱۴۰۴، کارگاه‌های ۶ تا ۱۰ نفره ۲۲.۳ درصد و کارگاه‌های ۱۱ تا ۵۰ نفره ۱۴.۲ درصد کاهش یافته‌اند.
🔹
در مقابل، تعداد کارگاه‌های یک‌نفره ۱۲ درصد رشد کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/682903" target="_blank">📅 22:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682902">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/410779a898.mp4?token=PRt7ss0C_q_bMhrf2FHGaZtpsELXO5CVDWH0Di2rny7Dj5O2fxYTFBrw0n3TrOEvn09_k5vC7-k3j1DxPLItRAP4R0gMORI1COOV5Ql30v0r62fw9cS4AxqcKzWSUfQ3AOZ-vAEyl1Mr-TtXYmt7btKlULwVaatAhTiF_tLg2inG3L5lrdz2ocrBgO0s-XIHqcoekL6W4NfG3NzU1mQoZteHLFFFECkCVSTFj7z3YYNlEpd8D8j2aCaqEFggjkhwjo546rB0I--VVNcNTFZqS2H3HgrJ-sQ96UiQ2-t4PDdnba8CMRSB-ZiyJvvfyukmJFYwyzunvxjGC05DiuINeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/410779a898.mp4?token=PRt7ss0C_q_bMhrf2FHGaZtpsELXO5CVDWH0Di2rny7Dj5O2fxYTFBrw0n3TrOEvn09_k5vC7-k3j1DxPLItRAP4R0gMORI1COOV5Ql30v0r62fw9cS4AxqcKzWSUfQ3AOZ-vAEyl1Mr-TtXYmt7btKlULwVaatAhTiF_tLg2inG3L5lrdz2ocrBgO0s-XIHqcoekL6W4NfG3NzU1mQoZteHLFFFECkCVSTFj7z3YYNlEpd8D8j2aCaqEFggjkhwjo546rB0I--VVNcNTFZqS2H3HgrJ-sQ96UiQ2-t4PDdnba8CMRSB-ZiyJvvfyukmJFYwyzunvxjGC05DiuINeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مالک شریعتی، عضو کمیسیون انرژی: در حال حاضر تخصیص بنزین به خودرو است نه خانوار؛ ۴۷ درصد خانواده ها حتی یک خودرو هم ندارند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/682902" target="_blank">📅 22:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682901">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
خط لوله ۶ کیلومتری قاچاقچیان سوخت در میناب جمع‌آوری شد
🔹
فرمانده پایگاه دریابانی میناب از شناسایی و جمع آوری ۶ کیلومتر خط لوله انتقال سوخت قاچاق در نوار ساحلی این شهرستان خبر داد.
🔹
این خط لوله توسط قاچاقچیان به‌صورت ماهرانه زیر ماسه‌های ساحل و آب دریا جاسازی شده بود.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/682901" target="_blank">📅 22:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682893">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YVHyObqFpxOSrEwq2NDxSo720JvRwX3JW049IWzUvDwK46uHERvWmG2ZbQGd9RktNrlGwGO1Q_9F5BgSYpB_CpIGa4JOf65xn4avANqjoB-QIMXVQGxtIm-mSvAO2z6k-djzdfCNsWWExR8augw000CQji01GIqclWPAn-Na8SDuGKTMAofokqFauzlWrxi5utizlEtLplbjw1N5y7dm_9j2aqq6uSvalyQgO7tNZ6kh_x7BeQVtrQYpShM_XI1FR_aQ3ayM2kF28bTn_vl4FpfYCvfZvgHq5dkU6P_WRzSG9wwoR1yGv83XcMwT2cHFxJ8mM5EAga4D8pjRhJa_PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XhlnAGZ1C8yntRiU_GCnt-lfBen88zkfmDkhC2Y9ORRiHWHOqMCXuOxpYh6rKD83DoZkwBU7jNTVTzrr2m--brdMv6NmaM5E0eEpZXzdoQmSiO5L4BmUbYC31tVdBLVc_tDtwnog7yb8kO1M5IWW3Y9bAHyjBVtmFbabsqcclH2mVs2QoK8WZWXa4qL_ZU9PVP3bCPXg0u3hx9Et3-cR_ep4mQtnzy0XSIhLg1EFKIM1bmzTgP3yMN6lhVTrHHMPEA36dRqrvTytKrxtqHRIQtVvMon2qBGmCaZpoaJhoiV0g5ji6z0KZn0e0xEF7l0iiIHVN_PWNj7CCzfvHHIkuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LhcDsg4L_T-iO8-dTDgP1J7eoIHzaENzLPbUGckEFMG8SlbehI9kuc_y2TPHvV8Rc_9mAr8maKHF6Su2hkkmbRQXM2NH2mGiG6FzdMCKHvSmU1P1lbGnXfPCu5iTtJ-soCmHmdyI8lz6uBEZd4TgZQ0y7kJeR89YxFvdPywIO5PenUJWPROX-Tm9CcqR2BGrOzOUxj5AIPvkth3zcB3eskQiKgEn37grnq2uxLkRNTKU_3h1omz6ZxkUjCbJdH12WFhklcg5elnpxVyqp54xKYLncG8iK4OoaTup4AYxlDEXYQSP3Uz8vbhOgjgHFQ1yGZUH7Qa3EVAxaeaEQawh-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDB1YFH0I44EhrlGABgM4tZysLCLRRRu9jVObOgTdagN1mTjiqOccJK5pCnDMEz3Pef7FvhfgoE9kRSZhVcIZ6BMFruPgWfosjEGt3fW0oSI-zB9TmztF5v5STIqyol-jZI9aBP-_VQrVlxuaz5YAKKlvQI8mbm6FaJhbsQr07L5Je1JxMPMYBHQUAEzFN3QlLdc8aY_mFkPHa9v85gHXaLUM-9OJm23hUGf14yLzvljf-urc5F35OWbrocoikMGByShZExZVVEs6ohWY90vMGWiR25-JkkBvatTwbsbNN1t6yYLSxNYUrLbowPpFujjQC59CfZrqIxRAOwpDqY_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r_vZFN1MNuibkFtUx8CQa3ifMRRJKSkTsuKkFXDtmNBwUbCsGs40cjzeYbkARyJRNNC-nd3qlL98q0lG-m9YGXzJj3pqgu_q2o2CTVwQ9peHbWs-7VtJCD-ZqwdixOn8OYOE2CDzfsN69pAYJvEEiZAxBLDx94fJSeOb3QaVc1ERR3nSiUEdwUziVcCbwXkH7Iif-VqLyQV6fPDk92OHieuaGgtKZI0p9d14KEHBDJomjR4z21uxmJkeWpBM7PFbBruOBBgQlI78jJBm-iM-pPVsz_tLxbzP2MPYwq1VqXL6eS7ptTFFbr8kLAKmKaPmU8AwQXkg3GhPKdMVy2OPcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p0rlIaxoiocDi42IYbu5iVHpCu28QHxjT_3PP3GYZrxtXgXCl8HNLo2BPMmJmcAprShE94S6Bjrmd3E1thwTKOVnUZcNBQIZ3StAGeT2ASz8GXeodPA-jnceMiMS_UwNtKbabhG-Yg9s0TWWfnq51x9FWLFT6egdBAfyfZxKoQo4kVcNlwuuRL4SA6WVMEiDABdvQphpJumhlaCNFsJxYmJW9ejz24ZuxASol1e-LPWNIkr2o3X0AJQtptNf7l69PlgRlsgbndepDSWac3wSILPth0mJxBqF2BaxB6HZ5kj6kuYE-K0bERzfKZ1UGxKIh40DSD2oTSSyXK9T44_xYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uzvhH9zMzV3pZ6J4ssfkMN6LQ3sEyZ04eZP_NkJjMwoDcOvUPJZRlie4CgSWF8nqaR9AbhsqoHZCZDuFSyU3CQ-9Bf3YVD9fYGTSsUGuQ4mYTSq2gIKLJDPbtaunUUP846xIOq_xc4oPF9gOxkMROX0gQzsSpxY8x8_TYR2sOd4O-eWU7R2e5z9EMWRkkYVslEwLuPBeAuq-Y6AF3Wn6-3JnjoFDzeGBULrcZTiPhmF9SJtX7PP6v0fa3Bmrxloir6Ykepws-LQvsJlLegpwDtNV7_lb4wv8zNbS_laVzkOPYskZMEX-XEaJoHmZ915YYNNUQHlSAPvVyQGecd6D-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mPxQjJEGqiE8EbvQrltFimEGWeQ_MzVlMrjcPwnxqJuzvqEK35qhUv38jL_uYTE5Ur-B3fUwymQrif9q2xK58eIi1XqK3GHUuNbeVHsELo42RHI4us8wtYCBpK3AkBmIYPZr-j3voZ_r21yINCpMIQut6vnWxPPCeU4Gapjs9MvdlAVU8yWv821SAYNilZ-9qbMcmH-BEOSwH44S0Ar4gyUdRKRLN6lKT81GnHuMUuqpBtyI2EYOOxD3UyhW5swBdHzLFOCm4n6RxcU38PRF3oYLHSWVAQwuJ4UxLHP8Oe3-I5a3AbWkpQBG0pWILr_6gRJy_SOVAw-Fr-ZBfPUX5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🥀
ای سامرا ! مهمان مظلومت کجا رفت
ابن الرضای سومین ، پیش رضا رفت
آه از نهاد مهدی ِ او تا خدا رفت
دور از وطن چون کشته‌ی کرببلا رفت
#پروفایل
#بگراند
شهادت
#امام_حسن_عسکری
(ع)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/682893" target="_blank">📅 22:18 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682892">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jj8biQJdiwWzI-V3QZEPZX9lu4Jc3RXDcU5sz4O9lG6-eC58OS-Xwzv9ccrdzJYT8Ili5RlQlcjQP77BJCMWi8bZrKeelYlB8Igt6-jAONgMVrz6quqJFYWOg1n9_C8p2ieVx9kbt5ZbwcqDqVcD4p1WeztFQDDiar_OYfgqB7ct2btgWluMAb3fOg9kg3B6SoKXFszl59peMyubqSRN1v_6lWfSA2QE4p-1kQKt7dEi-EMNL0o0MsZ8sFHR3MK8FhKoxkjUkSE3UDc_bGTbH7hVQZIufOybnoYvB3V2KzuBtTXWIUvK3SSz6FeOvm0-xil-cNtNA8tCdmx3vWNrSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش قالیباف به اقدام مشکوک حلبوسی، همتای عراقی خود: درباره ما خواهند نوشت که ما دو ملتی بودیم که نپذیرفتیم پاورقی روایت‌های دیگران شویم
🔹
رئیس‌مجلس عراق در یک عمل متوهمانه اقدام به استفاده از واژه جعلی خلیج عربی کرده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/682892" target="_blank">📅 22:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682891">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRWs8NqFzglA25Gd6lcWoJc8C5dpM9KhgAom-cf_gsXTaGR05VLRtMdwQuFd7-2-3B1r7K-BE5af_n2o0c36QlNnZNnQNSMSLp9A0gvJF7DSLu1i5IHfEgRcqDzFbUD2fCcnjIEvwvBgtBTkpO_9d6qa5vV3EOJMKfMViFMmnIamR6Aa0Yv-36jFsYvLQX12Kx5pvG8esh24I67VDdJDXOdUOpuEkH253tq0j2mdaZdU_i90AL9CC4ErC4moTDFMo_-DHwMeRfGCwbcgvvpPUQvde4GAuozI-RcaOucVQJtgj9lVAPA0uETBEAJ1uyLJ17vV8CLZY2sOL7HuAXQeEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روستای زیبای آغویه در کلیبر تبریز
#اخبار_آذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_sharghi</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/682891" target="_blank">📅 22:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682890">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-text">ششم ربیع الاول، سالروز ارتحال کوه عظیم‌توحید، استاد العرفاء مرحوم آیت الله العظمی حاج سید علی آقا قاضی طباطبایی تبریزی (قدس سره)
ان شاءالله عنایاتی از روح‌بلند این ولی الهی بهمون‌نائل بشه حمد و سوره ای برایشان‌قرائت کنیم</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/682890" target="_blank">📅 22:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682889">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdNc_TUmq91GdAvWos8NAsRnMDk4T3jogyin0yK81i9EaFKcbvEHWHKsiCSZBrVpx_ii8p1v8NLFISyR3sUq2rCDVwu6yJce6s0fiS2Ypn9zAaxwVj8RYFOHV1nwxny9jE57d06yPaWcui8qwU5dF2yoUgsxW2gZSdcUQh0j5Em2ngqykxZwBuvU4ARxmPpA3exFT8oMKoQaH5JxzvHybWbn3eQYfUvK0xUv0s-jA-g2uPpkWnaYTcsPcshbqwRv-4CV_Nn4CO9SQQfjhA-tFKcZVEPlCMTCf2hY74PQIZYFeEkLBNEz5GM0nY0sxH30CH6RqX4RsjHiVAonFb0EYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیدا کردن دوست سخت است؛ اما نگه داشتنش، گاهی سخت‌تر
🔹
امام علی(ع) در نهج‌البلاغه یادآوری می‌کند ناتوان‌ترین آدم کسی است که نتواند برای خود دوست پیدا کند، و ناتوان‌تر از او کسی است که دوستانش را از دست بدهد. دوستی واقعی سرمایه‌ای ارزشمند است؛ ساختنش زمان…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/682889" target="_blank">📅 22:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682888">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9f21d2d79.mp4?token=WAYPxMPc_FiHI46BsmzqumLK9ZsFVv54W7zQr9sMNwDLTNPXz2erKuBIDGgAI_N3tFZJ-i3P8jJ4yObvlnTFaWOy83jR8Jqx4NKsTm01Lg7mCdydxKo4JeyF59RLK0eaHlS_fiuET5Zvmp8XELcypyxdM_0kD6ijrY54WopQdgoGSS2pWUzf7dEmIShjylUucM0KRr899g4WQ3F7qp4mSYTdjJD3nt46pCK6t3bNC1g4mH_PvnSnwgY5wHSIFUko3o9OTlaUO7tCRU6FR36e5w4nAGhR97MnZSEWAAZAMfQdRFHo0smfrliK_FVgXegN81e5pKmcwmJcZDMqDlryoZ3MpjF8RzeEixURwWzvo2IhiuUW5sKPy9UzIDypcPOwOCVJ1lgSLSBi7NHFvSb5VZyWki_X52Fq5-Nio3oBouypf4qbUbZssDBUqMpQczw2UvRhCkVbmu7C3STmmUfllGffI33zIePittU3DRhWEgjQ5ooKpjIaYRKLmlMX1W2gO0BnjjQmHz_ixEogLThp9EigvvgZQRsMSqp3QComHyyrpXOGwvT3kcWEiBuG1-gVXRayV-y_kYcun1jWyjdHqddtE2WxBZ9Y5saM3GOEKmdbGB1ea1vWwDkKs3pCD5N_lWhjThB9wL4QhhkP4naimu4VkWAg9cfmMMQqJaiQ2DU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9f21d2d79.mp4?token=WAYPxMPc_FiHI46BsmzqumLK9ZsFVv54W7zQr9sMNwDLTNPXz2erKuBIDGgAI_N3tFZJ-i3P8jJ4yObvlnTFaWOy83jR8Jqx4NKsTm01Lg7mCdydxKo4JeyF59RLK0eaHlS_fiuET5Zvmp8XELcypyxdM_0kD6ijrY54WopQdgoGSS2pWUzf7dEmIShjylUucM0KRr899g4WQ3F7qp4mSYTdjJD3nt46pCK6t3bNC1g4mH_PvnSnwgY5wHSIFUko3o9OTlaUO7tCRU6FR36e5w4nAGhR97MnZSEWAAZAMfQdRFHo0smfrliK_FVgXegN81e5pKmcwmJcZDMqDlryoZ3MpjF8RzeEixURwWzvo2IhiuUW5sKPy9UzIDypcPOwOCVJ1lgSLSBi7NHFvSb5VZyWki_X52Fq5-Nio3oBouypf4qbUbZssDBUqMpQczw2UvRhCkVbmu7C3STmmUfllGffI33zIePittU3DRhWEgjQ5ooKpjIaYRKLmlMX1W2gO0BnjjQmHz_ixEogLThp9EigvvgZQRsMSqp3QComHyyrpXOGwvT3kcWEiBuG1-gVXRayV-y_kYcun1jWyjdHqddtE2WxBZ9Y5saM3GOEKmdbGB1ea1vWwDkKs3pCD5N_lWhjThB9wL4QhhkP4naimu4VkWAg9cfmMMQqJaiQ2DU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادویه‌های مفیدی که با چای باید خورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/682888" target="_blank">📅 22:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682887">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9fa1a5abe.mp4?token=WaqqlqnDBjjgXOfaYJXafsel2UGnDetYVDYnqDwDdR0UZy0P3GjMcXQqZPwU2Qm0sEGdIB1YV0lQqLpO9KENooriqXfRZ4JRr7V8sFN1SXdhtQLDwEZR1mdhQqGM4OtoBoJ-KORTpnrLVS6ezarzFimmFCV3S6Jz5VQKY97C5fUmIX-RkYRB9_22FEcjuQcrHo2SJMBs1sd6mROe3sLuRMeILDA6CmI7VE8j5hFVx9rb2tWGxU98gzF6hOWeeEBrTJh0PjkW9X53_Sh1Cg5OfriYfc9VPv87D7Ma1G8V_4uuHbXOuaQMcKzFxqB-FI5Dr252JsiaSEhQg5npTvCdUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9fa1a5abe.mp4?token=WaqqlqnDBjjgXOfaYJXafsel2UGnDetYVDYnqDwDdR0UZy0P3GjMcXQqZPwU2Qm0sEGdIB1YV0lQqLpO9KENooriqXfRZ4JRr7V8sFN1SXdhtQLDwEZR1mdhQqGM4OtoBoJ-KORTpnrLVS6ezarzFimmFCV3S6Jz5VQKY97C5fUmIX-RkYRB9_22FEcjuQcrHo2SJMBs1sd6mROe3sLuRMeILDA6CmI7VE8j5hFVx9rb2tWGxU98gzF6hOWeeEBrTJh0PjkW9X53_Sh1Cg5OfriYfc9VPv87D7Ma1G8V_4uuHbXOuaQMcKzFxqB-FI5Dr252JsiaSEhQg5npTvCdUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطره‌ احساسی دختر بچه معروف عکس جشن فرشته‌های بیت رهبری از رهبر شهید در برنامه محفل ستاره‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/682887" target="_blank">📅 22:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682886">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5QHrNdfrJHbXo28_xzR-ZlAXC_wmJzBOMMH4GZXkaLx3oNQbmKAoee8cCVrPDsspPUV3nRMtFUyo2p04I9LXcLXIrc-a2cTMFiUDbIVXnVcnRpZkzfaUl-ML6ncl0UIGSVW3jEQ5wyHKiJ--wxgNBPBpWhF4Tj5lzZYGc0r2Z3BToUNmcprtqzUKO94BuT3XtFlh87nf0ekmsH7Y7bfKgAvGPYxH6dKvXMOOznpZYoSFyyI2g7DISlUwOZQjn0oQ3S2VgynN9XVx9aojtGc47dB8CFJsRmBu88ng5VP7gRA53o_nCz3KlrpO5XtkUu7YdoXeU_CaEhxUBoW0Cu9zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☘
أللَّھُمَ‌؏َـجِّلْ‌لِوَلیِڪْ‌ألْفَرَج
☘
☀️
مصادف با سال‌روز آغاز امامت امام زمان عجل‌الله تعالی فرجه‌الشریف
♻️
اجتماع بزرگ مردمی
#تجدید_بیعت
با حضرت ولی‌عصر عجل‌الله‌تعالی‌فرجه‌الشریف
🗓
شنبه ۳۱ مردادماه ۱۴۰۵ ساعت ۲۰
📍
مکان: مشهد مقدس - عرصه میدان شهدا
❇️
همه با یک ندا برای شما آمدند.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/682886" target="_blank">📅 22:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682885">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
تمرکز عجیب بازار ایران؛ ۸۰ درصد سهم بازار در دست فقط ۲ درصد برندهاست
🔹
بررسی بازار ایران نشان می‌دهد بخش عمده سهم بازار در اختیار تعداد بسیار محدودی از برندهاست.
🔹
تنها ۲۲۴ برند، معادل ۲ درصد کل برندها، حدود ۸۰ درصد بازار را در اختیار دارند.  در مقابل، ۹۸ درصد برندها فقط ۲۰ درصد سهم بازار را به خود اختصاص داده‌اند. آماری که از رقابت شدید و تمرکز بالای بازار ایران حکایت دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/682885" target="_blank">📅 21:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682884">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heheWVyDYwlFWvRUQdhaI9EfBZUvPNST4Ac0CazXOHnKBGDX7_-Ok2G6b0t5_grpU7N9vL2BxowQg6Jqm-bN1n6ES6aQyQfbMn1lrIxx7IBpF7EGeTSGjPZbal1XtWnLgkBRzrGNmozYeliRj1Z8iFiw5-oAtogp5rYz3CSp8rfXeKVlGFHTUe4YkDNNXuE37f1NPGim4FVm0i4eVhYSbYoX_0hbf00dot4lC07OAFIl3crKUDirQ4JKRjGJNN9Kjl4ec5ufGc-qZRQEvhuFGbfTDoN0qqnm0xH0e69typMqK3nfmcuoGZZKVNzBSSf2J-qW2R4nhnGINXis8NKLQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: پس از حمله اسرائیل به یک پایگاه هوایی در سوریه، موضوع حضور نظامی ترکیه در سوریه به مسئله‌ای جدید تبدیل شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/682884" target="_blank">📅 21:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682883">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b1a89278d.mp4?token=Sbyp90P4ZM52FD-Iy8maIiZj-idzBWQa7AHnNY_pN0yE4TIB6d_ZNae1Jng0HZpAEDEoUl4SaiSMwTfDeoCB2lhpdppBwiYyy75ePsdAaq0b4AbdtT9RR0-cfinAzfwnrbp7L49tLnd0gq6mlLG0DKY9rXk2wlSzoB-rdFobm6BGu9_1wv9EPh4JNK2w9pEpHe1ftqowLKBlHJITqKNEjPZe1vPY1YZ9tYZr4KfUb3nY93RtAqJk47L-Ve4AsItcTarRR23aObPutPfB-1tHi9BYaSLIFrTgwt4zw-VNuflyGLKSDLrSAA7p_m2tKxGzddJ1-evt6Ea834FX5KhSlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b1a89278d.mp4?token=Sbyp90P4ZM52FD-Iy8maIiZj-idzBWQa7AHnNY_pN0yE4TIB6d_ZNae1Jng0HZpAEDEoUl4SaiSMwTfDeoCB2lhpdppBwiYyy75ePsdAaq0b4AbdtT9RR0-cfinAzfwnrbp7L49tLnd0gq6mlLG0DKY9rXk2wlSzoB-rdFobm6BGu9_1wv9EPh4JNK2w9pEpHe1ftqowLKBlHJITqKNEjPZe1vPY1YZ9tYZr4KfUb3nY93RtAqJk47L-Ve4AsItcTarRR23aObPutPfB-1tHi9BYaSLIFrTgwt4zw-VNuflyGLKSDLrSAA7p_m2tKxGzddJ1-evt6Ea834FX5KhSlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار ویدئویی از ترامپ ۸۰ ساله با پوشک بزرگسال!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/682883" target="_blank">📅 21:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682882">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
بازداشت زنی به اتهام تلاش برای بمب‌گذاری در ساختمان کنگره ایالتی نیویورک
🔹
پلیس فدرال آمریکا (FBI) از بازداشت زنی خبر داد که قصد داشت با کارگذاری مواد منفجره در ساختمان کنگره ایالتی نیویورک، یک عملیات انفجاری اجرا کند.
🔹
اف‌بی‌آی با تأیید این خبر ادعا کرد که این زن پیش از عملیاتی کردن طرح خود برای بمب‌گذاری در ساختمان کنگره ایالتی، شناسایی و بازداشت شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/682882" target="_blank">📅 21:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682881">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
راه رفتن دوباره پس از ۱۰ سال
🔹
این دختر پس از ۱۰ سال، برای نخستین‌بار با کمک یک اسکلت بیرونی رباتیک توانست راه برود؛ لحظه‌ای که شادی او را به همراه داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/682881" target="_blank">📅 21:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682880">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4df8662988.mp4?token=ZJjyH4YPoEWITbUcF8kwd75ko1Ahe8cdNmfzWlQtCBCCtTw3zsBqo1KaBeubzQeGZNzhtmZyR2xUN1PDWd-tF7Xyb-_V2h_kpHfX9Po8lqD4ZGfoGOBekeFgcTjlBKodSBl4FKBvH-nnQykO9MGhyIdnxOt-z9rtAICNYzMCH-x2xGqO_pKSVB3SLJu0e3kSCrpszXtyExqe8DEWRYhI2lXCFsEADoLLAQmbaqDyQNw0Ne-N67f8Orl8PyuItPZFcGfi0vDjTGDn_5hzBk3w-qLqpqqfXcqwP0PDk3gYnZZVzPALZCzi-uU7EbmMqvLISWurjZyUgT_PFBGpNB-xqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4df8662988.mp4?token=ZJjyH4YPoEWITbUcF8kwd75ko1Ahe8cdNmfzWlQtCBCCtTw3zsBqo1KaBeubzQeGZNzhtmZyR2xUN1PDWd-tF7Xyb-_V2h_kpHfX9Po8lqD4ZGfoGOBekeFgcTjlBKodSBl4FKBvH-nnQykO9MGhyIdnxOt-z9rtAICNYzMCH-x2xGqO_pKSVB3SLJu0e3kSCrpszXtyExqe8DEWRYhI2lXCFsEADoLLAQmbaqDyQNw0Ne-N67f8Orl8PyuItPZFcGfi0vDjTGDn_5hzBk3w-qLqpqqfXcqwP0PDk3gYnZZVzPALZCzi-uU7EbmMqvLISWurjZyUgT_PFBGpNB-xqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موفقیت یعنی فرزندم به آرزوهایش برسد، مسئولین به فکر خودشان هستند/
خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/682880" target="_blank">📅 21:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682879">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXPyoCyQDnFv_4C7EGMpMwhPYrF0whuVQ4TxgJxTfZS2mpYxZKWK0IqIbqdYS_EQZ-RB4b5KA9G9eQvpzCMh4rDxCR6dkYUB5kB0TRY6_1Id2O8NoD-wfIg277fE-LvJIySLGHyUQ_hLxGwzerNWlGlUc6UE0ofhWQZ095n0LOmu51TfJ3MSmMgRCLyJJ4gAjbcSCJJ6tTtafc1dRg5zyKU_BOcnIaUfHmcvDKtamJNsxsTtqadm5X7EI-fq-YupGSV7JaYhGQO131zbVhLZy1R_wjrqN2cwDpuCZ0ImVgMoft_ntm7LfJz88U7g_eJUvpRNV4fTPhDqoyWp92yaFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیمی از مردم آمریکا منتظر یک سال درگیری با ایران هستند
🔹
نتایج تازه نظرسنجی YouGov نشان می‌دهد نیمی از آمریکایی‌ها، معادل ۵۰ درصد، انتظار دارند جنگ با ایران یک سال یا بیشتر ادامه پیدا کند.
🔹
این نگرانی در میان هر سه طیف سیاسی آمریکا افزایش یافته اما بیشترین رشد به مستقل‌ها مربوط می‌شود. اکنون ۶۱ درصد از مستقل‌ها و ۵۸ درصد از دموکرات‌ها معتقدند جنگ ممکن است یک سال یا بیشتر طول بکشد. جمهوری‌خواهان نیز نسبت به ادامه‌دار شدن درگیری بدبین‌تر شده‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/682879" target="_blank">📅 21:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682878">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b9c1fa384.mp4?token=nDlTzJ6VB1A-g1STRNVeHT5ri5m2nfvFYcIRbV8XznwcLGp3wIaWhiCT0Gl1HosgrX6IJpZdJUvOdKR2j9rz7UvHox5TQrTJw9k5OEb0Hd-2r-T5TKa2cPCBs-0rYz8dW76qL2wc_6MU-0JfMqJblDUGAFwiBpCbNP7O2bzKmaMTZPwdnNzJ3TFJjvQOs8DDP4XZlvFrT9z2BQFC_sq3qxt0z1OKfdM9foTagLpmFTNR4cwmXucjO7JvsacD-tSz8rHmRG4phxn4IeMYiLB95KtU1tFiszmg9ejq6iKRJyzafrmYqcLPAPRC6Np_GG9Nkr-VRnTLhZXeFOz0tlhxLrCRSmi-6O514hFoZLaJd75QBFYSZ9UlxUEn4zQGNRV6ZIAsYyR5YL7D0uJbMUSdc-VLlrB_J5NnbnZ8JCMoGD3GuvGatbAlhxoqfZlYYERGbT5OS6n4G_SYaF2tQXiiXAn3rn0F2BYyW5_YWOV6ITVUszljeIlDSMtiY5NQv4lntOlUxc5_ruKPh0JmvgkBGQDZJLV_aPXm0iRUg9Srkbgw1xAgrp57xsp2TyFw7UMAVdmnhg_pNfeUGc0MJqm_IFvfJrhUJyvZA1C49Iq3_ddrPXsgKvyfs6DVwMw-868HAlj6OMiKqdbqpyYSBCrYOsWDb8Fsvk07Nhw-XvISlao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b9c1fa384.mp4?token=nDlTzJ6VB1A-g1STRNVeHT5ri5m2nfvFYcIRbV8XznwcLGp3wIaWhiCT0Gl1HosgrX6IJpZdJUvOdKR2j9rz7UvHox5TQrTJw9k5OEb0Hd-2r-T5TKa2cPCBs-0rYz8dW76qL2wc_6MU-0JfMqJblDUGAFwiBpCbNP7O2bzKmaMTZPwdnNzJ3TFJjvQOs8DDP4XZlvFrT9z2BQFC_sq3qxt0z1OKfdM9foTagLpmFTNR4cwmXucjO7JvsacD-tSz8rHmRG4phxn4IeMYiLB95KtU1tFiszmg9ejq6iKRJyzafrmYqcLPAPRC6Np_GG9Nkr-VRnTLhZXeFOz0tlhxLrCRSmi-6O514hFoZLaJd75QBFYSZ9UlxUEn4zQGNRV6ZIAsYyR5YL7D0uJbMUSdc-VLlrB_J5NnbnZ8JCMoGD3GuvGatbAlhxoqfZlYYERGbT5OS6n4G_SYaF2tQXiiXAn3rn0F2BYyW5_YWOV6ITVUszljeIlDSMtiY5NQv4lntOlUxc5_ruKPh0JmvgkBGQDZJLV_aPXm0iRUg9Srkbgw1xAgrp57xsp2TyFw7UMAVdmnhg_pNfeUGc0MJqm_IFvfJrhUJyvZA1C49Iq3_ddrPXsgKvyfs6DVwMw-868HAlj6OMiKqdbqpyYSBCrYOsWDb8Fsvk07Nhw-XvISlao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا وقتی سرمایه‌ای می‌خری شروع میکنه به ریختن؟!
🔹
شاید این اتفاق برای شما هم پیش اومده باشه، جوابش در این ویدئوست، راه‌حلش رو هم گفتیم
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/682878" target="_blank">📅 21:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682876">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32311f490a.mp4?token=IPmlcYmjRof9nS0ETVQk2p7Lu6eF7Kv91-DP1Yo2BidvgM4m3lAOxU5_iLRUUQsx0cuJ4ztZNjzP8vMkGmkERSq-rSy3egPTrdirv7R-UvMUMnYYztHtrFLt6kE1Fc29Zn_BGfIA352FHbqLuND0uTh_j1P0-pM64qZ0xnR_VGWWzWA777sUxuRjrLgxCGL7bOd_iZAKcdZYH93dY-DKL_cKwjMhJHwPvPcnp3kKC4NxstR97xWu8E5A2XvSgY9DICma8CGC6azxC_rhlzdba5RtoijVMaZibeguT6w0Cp-ra9zlXelqo2glftF3NrCxCkjfD9AL9N_dHASisqOsQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32311f490a.mp4?token=IPmlcYmjRof9nS0ETVQk2p7Lu6eF7Kv91-DP1Yo2BidvgM4m3lAOxU5_iLRUUQsx0cuJ4ztZNjzP8vMkGmkERSq-rSy3egPTrdirv7R-UvMUMnYYztHtrFLt6kE1Fc29Zn_BGfIA352FHbqLuND0uTh_j1P0-pM64qZ0xnR_VGWWzWA777sUxuRjrLgxCGL7bOd_iZAKcdZYH93dY-DKL_cKwjMhJHwPvPcnp3kKC4NxstR97xWu8E5A2XvSgY9DICma8CGC6azxC_rhlzdba5RtoijVMaZibeguT6w0Cp-ra9zlXelqo2glftF3NrCxCkjfD9AL9N_dHASisqOsQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد خونخواهی مردم حاضر در مراسم چهلم «آقای شهید ایران» با پرچم‌های سرخ در حرم مطهر رضوی #خونخواهی #تقاص_خواهید_داد   #WillPayThePrice
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/682876" target="_blank">📅 21:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682875">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/865c03b40e.mp4?token=qeKcfTk3Nqc5o_B7wy50gjSsbzfBuesF5h29DA7_vygXoltWr5ws6aquOY31y4D_dIihUaHE67mM8Wi9B2XqqnqVc2upQZUiyi-gnnAhzehcesaePJ0rqU6x0HdthuGyXOcLaHo9IMoRpde1lfIlrVFgAL5kcMQo-mvvfeYLT1_CdKS4KUI_uXbF7txj3XO2tJfYTJvSO5lK4Tm1wccEG9hQAi2D0fVaoJQPgun6JFJjAydCGZCaSL0GBqWdiDu6c8Wi1021kguM4GnRq-Wq8-a0HFxkjGVj589gf0n3_HWgHMyZwXI_CZIi9Z9GXuIDtJTCgVzHgUbwq0Zq7yo1SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/865c03b40e.mp4?token=qeKcfTk3Nqc5o_B7wy50gjSsbzfBuesF5h29DA7_vygXoltWr5ws6aquOY31y4D_dIihUaHE67mM8Wi9B2XqqnqVc2upQZUiyi-gnnAhzehcesaePJ0rqU6x0HdthuGyXOcLaHo9IMoRpde1lfIlrVFgAL5kcMQo-mvvfeYLT1_CdKS4KUI_uXbF7txj3XO2tJfYTJvSO5lK4Tm1wccEG9hQAi2D0fVaoJQPgun6JFJjAydCGZCaSL0GBqWdiDu6c8Wi1021kguM4GnRq-Wq8-a0HFxkjGVj589gf0n3_HWgHMyZwXI_CZIi9Z9GXuIDtJTCgVzHgUbwq0Zq7yo1SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: آیا کارزار اقتصادی علیه ایران شامل چین هم می‌شود؟ چون چین شریک اقتصادی اصلی ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/682875" target="_blank">📅 20:59 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682874">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDf2UfP8yCRBMlcBZ4jEbJbeepv6HvPZnan3GNrtZTvldZLetpVCutTGUxf_Pz2a1qD4Y2SW5C5lYrCBbROiBuLPHjW2bbj5axFnW54xRJ1Fl6TFtAyMFdqMJaV4rXJLHXdoax-6vK1R2yKIEr3eZh2NAU43npCN5moqglvKTAA8fTaecNODlrI_rE8Jcdwa4RbWME1In3Af1CTxMVrNFB_LgLGJhuAqdtOOBLqp1k-ard2AtqWpGMRwcGdB112zZONQ_ioQUM26JJadYRYgJeienYtmEkcus7596-ockR-FyThwMAtUADI5yJ_3SdPPKif26qWPgGmJIiRB5AL0mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشنگتن: احتمالاً‌ درگیری گسترده نظامی با ایران از سرگرفته نخواهد شد
وزیر خزانه‌داری آمریکا اسکات بسنت روز پنجشنبه در گفت‌وگو با سی‌ان‌بی‌سی:
🔹
اگر ما (کمپینِ) فشار اقتصادی حداکثری را اعمال کنیم، به این معناست که احتمالاً درگیری نظامی گسترده‌ از سر گرفته نخواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/682874" target="_blank">📅 20:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682873">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11037e9cfb.mp4?token=pvPR-GNw7OLFgwBHRVVPF0pRHkyR72nNBG3tuV6RX52I-v9PDogK_psVbdqLIj7zmnIOwKFY2bt5h2MdhcAGsLtjgo0vpykYpmf5auOjZ_sctwxFrBwkJ1vLpSKZ6iX_SMl0agBNx-0a__4OheScHoDa2hE3gArp3_GoU8bSWyU-7FdtX_yAjAsMoIbSRlngMgeoYOl6ki52WMe0PQgD97Q65_h37oT5JmAQ7Dxf7hOwA51xX8Z6evd9aWjYA1Lq5OLFZO_UrTQN_dPYIK5umnIVHshSF6fflDgE72LJ1hzXoCPdPGbptZjnaX9xVtSD-BSH4Gqn0TQFhDXkO_vwkB2_rlHwmECLJM0YEYVqdqNpFyx3AJGaw8sZYSj_Dnn8LvkyYVNKadY8k7obFHcO24roihJ8bw39qhCGTTCEeiojm5jExj2mHGbgSj7q_SdApaa_FJzPkeHnN7o3_kGmlOgQ5U4ig3SKhLSaLsLzWh_fo2hngvRw7sYx9RUc2oIlHmFIszvcVUqhVGNMfwGQvC_vNThGLwvbwvCAHootEjbhhP8sl99qD_Ojv-WQYJuEyZ-UuyE5wsivSe8Ede-Az165aAbQMU4zCatD03V-yjGLPrpu93Sh1HODckCxa9IYrad3l9GXTSGKK0_98b-b1aHpNW5g96fGYMqjuW7nTAM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11037e9cfb.mp4?token=pvPR-GNw7OLFgwBHRVVPF0pRHkyR72nNBG3tuV6RX52I-v9PDogK_psVbdqLIj7zmnIOwKFY2bt5h2MdhcAGsLtjgo0vpykYpmf5auOjZ_sctwxFrBwkJ1vLpSKZ6iX_SMl0agBNx-0a__4OheScHoDa2hE3gArp3_GoU8bSWyU-7FdtX_yAjAsMoIbSRlngMgeoYOl6ki52WMe0PQgD97Q65_h37oT5JmAQ7Dxf7hOwA51xX8Z6evd9aWjYA1Lq5OLFZO_UrTQN_dPYIK5umnIVHshSF6fflDgE72LJ1hzXoCPdPGbptZjnaX9xVtSD-BSH4Gqn0TQFhDXkO_vwkB2_rlHwmECLJM0YEYVqdqNpFyx3AJGaw8sZYSj_Dnn8LvkyYVNKadY8k7obFHcO24roihJ8bw39qhCGTTCEeiojm5jExj2mHGbgSj7q_SdApaa_FJzPkeHnN7o3_kGmlOgQ5U4ig3SKhLSaLsLzWh_fo2hngvRw7sYx9RUc2oIlHmFIszvcVUqhVGNMfwGQvC_vNThGLwvbwvCAHootEjbhhP8sl99qD_Ojv-WQYJuEyZ-UuyE5wsivSe8Ede-Az165aAbQMU4zCatD03V-yjGLPrpu93Sh1HODckCxa9IYrad3l9GXTSGKK0_98b-b1aHpNW5g96fGYMqjuW7nTAM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد خونخواهی مردم حاضر در مراسم چهلم «آقای شهید ایران» با پرچم‌های سرخ در حرم مطهر رضوی
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/682873" target="_blank">📅 20:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682872">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
تحریم‌های جدید آمریکا علیه ایران، حزب‌الله، روسیه و کوبا
🔹
وزارت خزانه‌داری آمریکا امروز پنجشنبه تحریم‌های جدیدی علیه افراد و نهادهای مرتبط با ایران، کوبا، حزب‌الله و روسیه اعلام کرد.
🔹
سه نفر از افرادی که در این فهرست قرار گرفته‌اند مرتبط با ایران هستند. همه این افراد ترکیه‌ای هستند. ۷ نفر هم در ارتباط با حزب‌الله در این فهرست قرار گرفته‌اند که تابعیت یک نفر از آنها ایرانی است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/682872" target="_blank">📅 20:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682871">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ادعای رویترز: آلمان برای ایرانی‌های مخالف خط تلفن ویژه راه‌اندازی کرد
🔹
خبرگزاری رویترز مدعی شد که دفتر فدرال حفاظت از قانون اساسی آلمان (BfV) برای مهاجران و پناهندگان ایران، روسیه و چین، خط تلفن ویژه‌ای راه‌اندازی کرده است.
🔹
این خط برای مخالفان سیاسی در نظر گرفته شده است. آلمان این اقدام را برای شناسایی عوامل تهدید و جلوگیری از اقدامات احتمالی راه‌اندازی کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/682871" target="_blank">📅 20:46 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682868">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
درستکار: آمریکا به یک نفر ویزا ندهد، تیم را اعزام نمی‌کنیم
سرمربی تیم ملی کشتی آزاد:
🔹
برای حضور تیم ایران در مسابقات امیدهای جهان در لاس‌وگاس، اگر آمریکا حتی به یک کشتی‌گیر ویزا ندهد، تیم را اعزام نمی‌کنیم؛ چون ما یک تیم هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/682868" target="_blank">📅 20:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682867">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab8e709b84.mp4?token=QJkLipLToRQ25GCwRB8oz3xeUe61VeoOPEqq1iD_5lboqXDgDMjprunrOLZ1jj6vtBGa_lZ_RoDhUs9g7R7Ua406gIJYtWmWl4qGTZnbwjF3jzPcNHR-hhrCcpzHUlsd9s1zDwTePi9QGuLFUfkkS5PRibUPsraVs87GeaxgZFybRDhL2xOXMFISFftUTsu4cdWqeRmCW6y0osKxs_eCCULwf38hpdOdcug7w9j4nH7uRWOCxoE4WH4YjPZm8rOku8my1LPSAN9vks8xXhNqz3seLwnEkCZ9s09qhKkvnMQGF2nkb-gbxU6JA-ceKzYu_YRDqgIIpVziv90iy-Mwlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab8e709b84.mp4?token=QJkLipLToRQ25GCwRB8oz3xeUe61VeoOPEqq1iD_5lboqXDgDMjprunrOLZ1jj6vtBGa_lZ_RoDhUs9g7R7Ua406gIJYtWmWl4qGTZnbwjF3jzPcNHR-hhrCcpzHUlsd9s1zDwTePi9QGuLFUfkkS5PRibUPsraVs87GeaxgZFybRDhL2xOXMFISFftUTsu4cdWqeRmCW6y0osKxs_eCCULwf38hpdOdcug7w9j4nH7uRWOCxoE4WH4YjPZm8rOku8my1LPSAN9vks8xXhNqz3seLwnEkCZ9s09qhKkvnMQGF2nkb-gbxU6JA-ceKzYu_YRDqgIIpVziv90iy-Mwlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لفاظی کاخ سفید؛ ادعای وزیر خزانه‌داری ترامپ درباره رویکرد شکست خورده تحریم‌ها
🔹
«اسکات بسنت» وزیر خزانه داری آمریکا درباره  اعلان جنگ اقتصادی از سوی «دونالد ترامپ» در پی شکست واشنگتن در میدان جنگ نظامی علیه ایران، با تکرار لفاظی ها ادعا کرد: سخت‌ترین تحریم‌های…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/682867" target="_blank">📅 20:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682866">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTjobGFtyYoKBO4sdSN0IsQ2EUqkBvaxehQFg_EzJwYHaaCNIlLDX8UcRN8cU0R4RUr92ZoFpqcKUlZVUtkepv-Eax7YnBIoapECtmAi4rZjHqHP1S78zJuEZtG2h1IZPQrDFyRKQuxdqCLULuc9XzyBqdOHi680ZoBPByNlwK4qx5LZgpKPsfQSOhfP8ytQQn26Ie6nm9vu-XYSLyYSxyAxQsKsy4fVerswRaSI57enLbCw8dANa2cMFoz9zCuB9OjDl0NiJJgtNMt_ZiS5iiNvOg8O6KCoE7rUYAzDj_Tqz9-9MViVwiw_j51gPQleR5LRyDrFji3U2YQn40xVFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لفاظی کاخ سفید؛ ادعای وزیر خزانه‌داری ترامپ درباره رویکرد شکست خورده تحریم‌ها
🔹
«اسکات بسنت» وزیر خزانه داری آمریکا درباره  اعلان جنگ اقتصادی از سوی «دونالد ترامپ» در پی شکست واشنگتن در میدان جنگ نظامی علیه ایران، با تکرار لفاظی ها ادعا کرد: سخت‌ترین تحریم‌های تاریخ علیه جمهوری اسلامی ایران اعمال خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/682866" target="_blank">📅 20:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682865">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
واکنش فرانسه، آلمان، ایتالیا و انگلیس در بیانیه مشترک، به شهرک سازی جدید صهیونیست‌ها در کرانه باختری: این کار غیرقابل قبول است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/682865" target="_blank">📅 20:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682864">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
تجاوز جدید رژیم صهیونیستی به خاک سوریه
🔹
منابع خبری از تجاوز نظامی جدید ارتش رژیم صهیونیستی به مناطق جنوبی سوریه و نقض مجدد حاکمیت این کشور خبر می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/682864" target="_blank">📅 20:17 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682862">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XveDCle2425mbj-LGz-bH5g6Lgu9LonliVxp6ZnSoNkiMgoZfyPJAewY8AU_OKcWbwy8FxRWba_pdQvOaqXc7iLpShoFSyObuJT4k8h9x2glBbizwE6_wM89gGHwJlSP2gnpQYvgoOHO9UJraQqsJwuzO0UsZtRr9w-MGhmivbmLTixKIaBViFZCQ2WkfkBwCXD4o4696XI2WhNv7wQHFgtJHk6MrO-wgYFq5KxBOACYlmD352yZbzQ1xdCqTLKpOrk8BS79kjEyggM5NPRP4Wza8m2tyQTVQs99qJQmRSF53qMazG4WTfTjkIl4uIYxx7kpnbSFEtYOKx_VH0Af6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویری منتشر نشده از سخنرانی رهبر شهید انقلاب در حرم مطهر امام رضا علیه‌السلام
🔹
مراسم بزرگداشت چهلم «آقای شهید ایران» از سوی رهبر معظم انقلاب در حرم مطهر امام رضا علیه‌السلام. ۱۴۰۵/۰۵/۲۹
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/682862" target="_blank">📅 20:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682861">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/235238142c.mp4?token=YC8ZM-Cp8tMo82UMHNHpUdmp9NzzdRHZVGKfvFWFicOCZdRhwRqelc3LUYv-nd7G7kHCwzUuUJWtCclo3ljO72JhxjU-26ZMYXevdXgy5N16FJ9ImhS86AiJNkxHpISziG7ene1KLaqRgObdv84rSKAJl1NXQbCmz8sMWTA2w5yg_s6Z9FfETmtvDv5DnS7jC6YJkyu9b1Q1ORLw_mAhRcn73TCHMC44SzqCKXkrSG47kH-lXHBk3dznuo5K9_Cd9hXIMAlpofvoScSpAMgPKJ2ZFbxE3zY5bpeu1_FHXD1ACRBEXwSqM-adeI55KnmhqzdzmJIphknyJue5GVfLGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/235238142c.mp4?token=YC8ZM-Cp8tMo82UMHNHpUdmp9NzzdRHZVGKfvFWFicOCZdRhwRqelc3LUYv-nd7G7kHCwzUuUJWtCclo3ljO72JhxjU-26ZMYXevdXgy5N16FJ9ImhS86AiJNkxHpISziG7ene1KLaqRgObdv84rSKAJl1NXQbCmz8sMWTA2w5yg_s6Z9FfETmtvDv5DnS7jC6YJkyu9b1Q1ORLw_mAhRcn73TCHMC44SzqCKXkrSG47kH-lXHBk3dznuo5K9_Cd9hXIMAlpofvoScSpAMgPKJ2ZFbxE3zY5bpeu1_FHXD1ACRBEXwSqM-adeI55KnmhqzdzmJIphknyJue5GVfLGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کامل‌ترین راهنمای لکه‌بری در خانه #ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/682861" target="_blank">📅 20:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682860">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba2666f082.mp4?token=ExMCmSun-K5jN9D3-EtcPT95WeEvqS7bfOcS7jOi1liqenTbNIiHG2PJoiBVmkAsjt8XyceJynFihvELEIFeSg73Zm9xVLAfE3-2GttYCVRNyF-IhX9-EX3rMZLxrF6ZKKE64JRqo_niAfMWt4BrMymZdWxV-Mt1TxcRaKF-h1KBrJ5ywcsGZ-W_dJvZVylsY-xJ3CB21eUuhaTEtcP3SKyfJWf0WRI0HsAhtYbEcPOOjyPMtfXXSoVM8XwEM-OayXNkzlG8hD0kzD-553bnuFA2qaZQ3m3GmDgNEXmibEeGcdOPwJsFOb4v6J29tom97AFPURR1PPz2Xfi9U8m_Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba2666f082.mp4?token=ExMCmSun-K5jN9D3-EtcPT95WeEvqS7bfOcS7jOi1liqenTbNIiHG2PJoiBVmkAsjt8XyceJynFihvELEIFeSg73Zm9xVLAfE3-2GttYCVRNyF-IhX9-EX3rMZLxrF6ZKKE64JRqo_niAfMWt4BrMymZdWxV-Mt1TxcRaKF-h1KBrJ5ywcsGZ-W_dJvZVylsY-xJ3CB21eUuhaTEtcP3SKyfJWf0WRI0HsAhtYbEcPOOjyPMtfXXSoVM8XwEM-OayXNkzlG8hD0kzD-553bnuFA2qaZQ3m3GmDgNEXmibEeGcdOPwJsFOb4v6J29tom97AFPURR1PPz2Xfi9U8m_Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری منتشر نشده از سخنرانی رهبر شهید انقلاب در حرم مطهر امام رضا علیه‌السلام
🔹
مراسم بزرگداشت چهلم «آقای شهید ایران» از سوی رهبر معظم انقلاب در حرم مطهر امام رضا علیه‌السلام. ۱۴۰۵/۰۵/۲۹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/682860" target="_blank">📅 20:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682859">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea40a0464.mp4?token=fvnwfeRWXjyRSDJdMmL4u1596JM84ZkpDHy1BT_fWEmb9HslB3zUKXoIupEIuUJUcGsDzZvtSvacXItqv62dLTfjmYO2htvd9D18enAh5LzBWE0TyvHH3JmjyYIpjbt0rM50TtLU-QWAahgz5F3hVVsrYPag506NcuK55s0vEIjZZOSN8QtJ5kLp2ZB3dNl669OH42_aK-PZP6BnHdMvvvsR7fgaUD14vAXKgxqcuepznh1GGrDWL-dJyimAT4Uoub0jo0cM8zJ65bBtMC5MDDSneF-qc2S0YVsQGisYDL1vEHGbeitwLj5AqqLGn17JYyIh0SrvPn1CBm8us8OBPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea40a0464.mp4?token=fvnwfeRWXjyRSDJdMmL4u1596JM84ZkpDHy1BT_fWEmb9HslB3zUKXoIupEIuUJUcGsDzZvtSvacXItqv62dLTfjmYO2htvd9D18enAh5LzBWE0TyvHH3JmjyYIpjbt0rM50TtLU-QWAahgz5F3hVVsrYPag506NcuK55s0vEIjZZOSN8QtJ5kLp2ZB3dNl669OH42_aK-PZP6BnHdMvvvsR7fgaUD14vAXKgxqcuepznh1GGrDWL-dJyimAT4Uoub0jo0cM8zJ65bBtMC5MDDSneF-qc2S0YVsQGisYDL1vEHGbeitwLj5AqqLGn17JYyIh0SrvPn1CBm8us8OBPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ساعات پایانی...
جشنواره ۱۰ سالگی "چرم مَنطِـ"
✨
تا %𝟴𝟬 تخفیف
✨
«تمامی محصولات»
➕
𝟮,𝟬𝟬𝟬,𝟬𝟬𝟬 تومان هدیه اسنپ‌پی
با کد: PAYZ63R
حضوری و آنلاین
👇
🌐
manteofficial.com</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/682859" target="_blank">📅 20:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682858">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/999bcdb3b8.mp4?token=s2_0uLp2Z-OQ8Ie-WLDi7z3ZknZDDwEk5d9Erd7U0e1pOYRTmn1l22B_TyV8J8fDMCynnZi1eLklYk5jyiZQmHbkavim7ttOLtwxg7QwV7sVAU31C6MeVJFZha6KNQ9JPorc_8LBCrztp1w3CH20lUza_7NA4DbZhmQD3DdYF_XFA4WSVfXwM170q4vhPF_GagaiwUhoWNw5xGgwKF4iSUcfoTgHDw1xRS8gXNATOBHp9MnOFMFcy0VjrcWr5qfc8auvvLRBf3vAT-3ZIjDCp4PxxShlYKNO-Hk-bjv2nSvOhEX4NBoQFsZIBlwUQ19xlEbBZPY1NbH5S1PkJbDWZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/999bcdb3b8.mp4?token=s2_0uLp2Z-OQ8Ie-WLDi7z3ZknZDDwEk5d9Erd7U0e1pOYRTmn1l22B_TyV8J8fDMCynnZi1eLklYk5jyiZQmHbkavim7ttOLtwxg7QwV7sVAU31C6MeVJFZha6KNQ9JPorc_8LBCrztp1w3CH20lUza_7NA4DbZhmQD3DdYF_XFA4WSVfXwM170q4vhPF_GagaiwUhoWNw5xGgwKF4iSUcfoTgHDw1xRS8gXNATOBHp9MnOFMFcy0VjrcWr5qfc8auvvLRBf3vAT-3ZIjDCp4PxxShlYKNO-Hk-bjv2nSvOhEX4NBoQFsZIBlwUQ19xlEbBZPY1NbH5S1PkJbDWZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اهتزاز پرچم‌های خونخواهی در بزرگداشت چهلم تدفین «آقای شهید ایران» در حرم مطهر رضوی
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/682858" target="_blank">📅 19:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682857">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
داوطلبی که فراتر از انتظار خودش پاسخ داد؛ آنهایی که شهید شدند در کنکور مهم‌تری قبول شدند/
خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/682857" target="_blank">📅 19:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682856">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
چین خواستار راه‌حل دیپلماتیک درباره ایران شد
🔹
سخنگوی وزارت امور خارجه چین در واکنش به مطالب ایران ستیزانه رئیس جمهوری آمریکا گفت که تحریم و فشار به تنش‌های خاورمیانه پایان نمی‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/682856" target="_blank">📅 19:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682854">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjY0WhFXSZSBFDdBUu5bJ2zu_imc3rDZz0rdJdtOWaLGsGeLtKQBQKD7sXtGlfq9Enx4ewZRPfqRDzVzb1Wp7OyyHbvVUty9bngjWADpiXH-6ngXJUlaozi2SAkahlU4PAUVHgYh8t3GJuuQWu8T-Lg7qcbFNaHdqOfPjIyxZIyVLOXrsdcP0w4q0MmyABT7UuPuHz0jFQ5RDP9UaqOA2qr6LvSv6GtlBMlpn7UkntROVF-rcj98s0Pro1yMyhn1RB6HVC97OM7WIY09_57X2klntpUo6q_tKEB01JUtPD0TuGVXG8fdfMybKhVeHmY7pX3_rnPbGsSOFsHb1OC27g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از هر ۴ ایرانی، یک نفر «سرآشپز» را دیده اند؛ پربیننده‌ترین برنامه سرگرمی‌محور ایران در ماه‌های گذشته
🔹
طبق نظرسنجی یکی از مراکز معتبر از هر ۴ ایرانی، یک نفر بیننده برنامه «سرآشپز» است؛ آماری که این برنامه را به یکی از پربیننده‌ترین برنامه‌های شبکه سه تبدیل کرده است.
🔹
«سرآشپز» یک برنامه تلویزیونی در حوزه آشپزی و سرگرمی است که با ترکیب آموزش آشپزی، رقابت و فضای سرگرم‌کننده، توانسته تنها با پخش ۲۰ قسمت به چنین میزان مخاطبی دست پیدا کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/682854" target="_blank">📅 19:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682853">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
ناو یواس‌اس جورج واشنگتن وارد خاورمیانه شد
سازمان تروریستی سنتکام در بیانیه‌ای:
🔹
گروه رزمی ناو هواپیمابر جورج واشنگتن پس از ورود به منطقه تحت مسئولیت سنتکام، در چارچوب یک استقرار برنامه‌ریزی‌شده در خاورمیانه در حال فعالیت است./ ایسنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/682853" target="_blank">📅 19:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682852">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
«فروختن گذشته»؛ وقتی آینده از دسترس خارج می‌شود | چرا عکس مهمانی‌های خصوصی ایران مورد توجه قرار گرفت؟ | توجه به گذشته بخاطر حالِ نامعلوم امروز است!
🔹
در سایه جنگ و مذاکرات، اگرچه خیلی کوتاه اما به یکباره فضای مجازی ایران به تسخیر عکس‌هایی از مهمان‌های خصوصی دهه هفتاد و هشتاد درآمد. مهمانی‌هایی که نشان از زیست پنهان طبقه عموما متوسط ایرانی داشت. واکنش‌ به این عکس‌ها هم قابل توجه بود. عده‌ای آن را به علاقه ازلی جامعه ایرانی به گذشته‌گرایی تعبیر می‌کردند و عده‌ای دیگر هم آن را با فضی سیاسی دهه هفتاد با ‌آن مختصات سیاسی مورد نظر متناسب می‌دانستند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3238977</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/682852" target="_blank">📅 19:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682851">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/320a0c6138.mp4?token=kQKum0FnVw3QzheWy8A4acZrCI4GPMCu6m1tMxwLVhyNzh1V1_gxi-G9zikaUCOaC4dRlWEkLG03P7KrEH9wj8-3HPb_t6r-MHKDm8nYWvgH76EcbHXXN4CiHDk4Dy4xqZc74_WRFxiRWlhmKjHvx5fRIPhZa3fmB5CiHe3h2u9iCIN0nbn7kYrOuHP8BJ5kis1rdL1u36HHR-FSz-oL2q3EtDOeiePCwCE8qOH10-fnWj9AyxinTMK7zwHKu8BM7A8Quqzn8VryiZ4TPQ3gdHeElg2kKQFnZ4RWu426q43EgFpEAm6Xvoj8qjE1w4cve0TQlAS9aO5hdV9d10x0vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/320a0c6138.mp4?token=kQKum0FnVw3QzheWy8A4acZrCI4GPMCu6m1tMxwLVhyNzh1V1_gxi-G9zikaUCOaC4dRlWEkLG03P7KrEH9wj8-3HPb_t6r-MHKDm8nYWvgH76EcbHXXN4CiHDk4Dy4xqZc74_WRFxiRWlhmKjHvx5fRIPhZa3fmB5CiHe3h2u9iCIN0nbn7kYrOuHP8BJ5kis1rdL1u36HHR-FSz-oL2q3EtDOeiePCwCE8qOH10-fnWj9AyxinTMK7zwHKu8BM7A8Quqzn8VryiZ4TPQ3gdHeElg2kKQFnZ4RWu426q43EgFpEAm6Xvoj8qjE1w4cve0TQlAS9aO5hdV9d10x0vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع غذایی آهن
🩸
🔹
عدس، اسفناج، گوشت، لوبیا و جگر منابع آهن هستند و ویتامین C به جذب بهتر آهن کمک می‌کند؛ اما کم‌خونی همیشه ناشی از کمبود آهن نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/682851" target="_blank">📅 19:17 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682850">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPIhxBQPSofZ5K2NOUHua7Mq3CFccX-BZgee-TlgrqZPJT3Nx8Vo_eAlQ923g4Ub3NuPOS0qvMVQ9Dxwv_yyL1LNXshMvJjw7mfpcwJcc5UuOu9Z8WTPPYMTgT958D_sAY9tZd96_YsOR378ozD5eG3Ai5UA-W9j4MJvDe8Hv5JvsGY2e2F0RALWEbrkq2GBt78bDEVFNzf6AduSphuy-UivX-Cn9-F8m5zis6t6jxtZ7Nn_6tMA2m6O6O6V2Mzj2VFCrGreA4Qi-bSpTPIhi6T9sKEtMk_K8BvmTrDYUKrxYPlJsgDJ7hd-B5fO_TWW96vg7zN3rxTsJ23gI78_KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد  رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/682850" target="_blank">📅 19:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682849">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7dd4f3fdc.mp4?token=MHAwsEO4hzYRtSlS06CUM2n6q9yZuRRjIB1aHmPtTmCiJ_mI-4Fv9nNgGA6UtmsjNJJAlOSWjGKNX51JiFTJU6j7BdA0qzkL3wEF0VH9XEYW5h0Ot31SDG0reZER6IhC_EbaSA59ezXAERE5RMrPhU8UXaVU9Sm8uTxAK4sgx2EtgpORa_zy1Js5oYnzjAp3A05mzBHs0dGsCa3IMLDNC5tudCxT6LWRVKx84u7Poiyb-PHnZWGlVGfJ6s7ZAEpSldEGvgjoaqgmJkDXLgfbWiKecpP3J-H18uhTigr7329W-Efz_Jh-XAb6XaJjO3tAYKqck_POvjAD1qDalghfYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7dd4f3fdc.mp4?token=MHAwsEO4hzYRtSlS06CUM2n6q9yZuRRjIB1aHmPtTmCiJ_mI-4Fv9nNgGA6UtmsjNJJAlOSWjGKNX51JiFTJU6j7BdA0qzkL3wEF0VH9XEYW5h0Ot31SDG0reZER6IhC_EbaSA59ezXAERE5RMrPhU8UXaVU9Sm8uTxAK4sgx2EtgpORa_zy1Js5oYnzjAp3A05mzBHs0dGsCa3IMLDNC5tudCxT6LWRVKx84u7Poiyb-PHnZWGlVGfJ6s7ZAEpSldEGvgjoaqgmJkDXLgfbWiKecpP3J-H18uhTigr7329W-Efz_Jh-XAb6XaJjO3tAYKqck_POvjAD1qDalghfYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش قالیباف به اقدام مشکوک حلبوسی، همتای عراقی خود: درباره ما خواهند نوشت که ما دو ملتی بودیم که نپذیرفتیم پاورقی روایت‌های دیگران شویم
🔹
رئیس‌مجلس عراق در یک عمل متوهمانه اقدام به استفاده از واژه جعلی خلیج عربی کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/682849" target="_blank">📅 18:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682848">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد  رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/682848" target="_blank">📅 18:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682847">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90ed43fd93.mp4?token=gCN-I4zi5jGVGu_9mwUEfeNvNZwc4lgMTrdYS1d_rcbdXIJGVfuSuO4pPaU95FDzVTbs2re2qtsUBTVXQELSBP1ePk0p9k2cvXLtEe-OD9477gGrRJfRQbjxXtLrejHHmL1QfIVdTkL50mDBPr-LxfVkxbDjemGEwq27NXDuXAoKRZKpWPFj7k_M-eqGwekBRDyGytbGr8V5sPgFUKqPMue2D-xOFEwsjGfbUZe0aKx0qknYBeBIC7h6Ai12cjg747H66XSkz8rL80TARIXauF3KLjVRVKqrspf20mzPSfg8eSjeVIMkDNR_4VDL0c9L1dke5of8SA9E9ALjYhrvWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90ed43fd93.mp4?token=gCN-I4zi5jGVGu_9mwUEfeNvNZwc4lgMTrdYS1d_rcbdXIJGVfuSuO4pPaU95FDzVTbs2re2qtsUBTVXQELSBP1ePk0p9k2cvXLtEe-OD9477gGrRJfRQbjxXtLrejHHmL1QfIVdTkL50mDBPr-LxfVkxbDjemGEwq27NXDuXAoKRZKpWPFj7k_M-eqGwekBRDyGytbGr8V5sPgFUKqPMue2D-xOFEwsjGfbUZe0aKx0qknYBeBIC7h6Ai12cjg747H66XSkz8rL80TARIXauF3KLjVRVKqrspf20mzPSfg8eSjeVIMkDNR_4VDL0c9L1dke5of8SA9E9ALjYhrvWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داوطلبی که به اصرار خانواده آمد و سفید داد/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/682847" target="_blank">📅 18:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682846">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfb59856f4.mp4?token=BvMOKmRYtNbjNrm6MfhesU329CnTLyNQGujBwje6anMfU-48qvQP5yd3YGA3XwOsXU4czjZlyvEW6AF9AYpFz0G5EJkBHpkOZax7sVOFyAL3FcLV7RFTAeSQpHztnCNrgiNuj6cI3o5ir6QA5qoGHhJSeNjMRlnV5iB1nQzrQqIiEAqn7sfCODmBkypnEbNlWZw4n9umzlvGTBoJ45F3ytE2XY-ontD6smjMUKvKr2rFbF-1FVPdjO2JzMZUy82nggK5kHZfj9u-WdG49ibZhU5T2hrfxf98a6b6ogLXwFNSpugzWe--_bTal0akDQAmUgeUbI0arsM8pHAWlvOxIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfb59856f4.mp4?token=BvMOKmRYtNbjNrm6MfhesU329CnTLyNQGujBwje6anMfU-48qvQP5yd3YGA3XwOsXU4czjZlyvEW6AF9AYpFz0G5EJkBHpkOZax7sVOFyAL3FcLV7RFTAeSQpHztnCNrgiNuj6cI3o5ir6QA5qoGHhJSeNjMRlnV5iB1nQzrQqIiEAqn7sfCODmBkypnEbNlWZw4n9umzlvGTBoJ45F3ytE2XY-ontD6smjMUKvKr2rFbF-1FVPdjO2JzMZUy82nggK5kHZfj9u-WdG49ibZhU5T2hrfxf98a6b6ogLXwFNSpugzWe--_bTal0akDQAmUgeUbI0arsM8pHAWlvOxIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ناگفته‌های بسیار مهم افشین علا از گلایه‌هایش در فتنه ۸۸ و نوع برخورد رهبر شهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/682846" target="_blank">📅 18:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682845">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
نگرانی امارات نسبت به تبعات اقدام ضد ایران
ادعای وال‌استریت‌ژورنال به نقل از منابع:
🔹
آمریکا از امارات خواسته فشارهای اقتصادی علیه ایران را تشدید کند.
🔹
این در حالیست که مقامات اماراتی بیم آن دارند راهبرد آمریکا در قبال ایران به بخش‌های اقتصادی کشورهای حوزه خلیج فارس ضربه وارد کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/682845" target="_blank">📅 18:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682844">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nbl3nHZQ32a_xA4d-UQe28eFZ6Weh7tlybZEprBWebOn14bFvGmvSyHVzTOdea26fNCAr__bAngyzzuxUJNsjAIReIQYpKn3wVSmcvi9ClNdP-KY_UPxXiagOO9vbGFNQm4FPriCDTbn5ZYRIDxwuzhqZtdrHgPlOPHEZ5qmkWXJqoAt4j7cv3nsRI3RsFgK9ggP5kh1q2ZNaaJl982h-CQQaS4u7B6w1G2ks7GGXzXENCDS-mbK0cY_1AVsGgXsl0gxUHJ8RYDnqBW-5T_I-_Xn9K5lr1kDtyTTqEGW04iRwJeCLPLwSbgy2-snsOq4wYTMXK6PO-RLeeLAfL4QnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هواوی Pura X View با نمایشگر عریض معرفی شد
📱
🔹
هواوی گوشی Pura X View را با نمایشگر عریض ۶.۳۹ اینچی معرفی کرد؛ طراحی این گوشی برای تماشای ویدئو، مطالعه و بازی بهینه شده و هواوی آن را نخستین گوشی هوشمند عریضِ غیرتاشو معرفی کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/682844" target="_blank">📅 18:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682843">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdQ-6fpTDMYxsH2sn82HQ5Rl4o-Vk6VK53bJ9npr2APAh-D5S7jVI83otyRWSTQGtyUG8sH8Pnky4jqA1n2rqHX0FXIhSTq9iTE6wcDHToZVa4sXFhBHZGdsLzFYXBUuEpDScs5p1ulf9oclkMMiBMpBO6gQNJREallW6K__5ntIXwXEKQw6h_OqLbR3R7n62FO2-hvZQM-yNVL1S5Ro4qaDaao-gCsjumK6KUA-MG_7tkXQ4GWcT2fHFFT52s2s6AwG8ybwyD1XOgeg8IBUYmhAalcIvNtz5z-CIzhFXGeMkNIgWGNDrRXqbtjeaPVwJzfU5Jau6025KJMhiBmJNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد  رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز…</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/682843" target="_blank">📅 18:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682842">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q90buqZkdQM5GrTY167MmioHfQCQuDmh3kHBucgfcbjZSTP5jAebrCwbYjE9j2EbAsTmIukuiJtCKD58G7Ug0LZp8wfugyQ1_gFr9Ph0xNSxN30WjbEPEgTol4ljQvAy-JRdxJMipCkEt_0YUhvws_23LUOosEJiDD-px94ufbr57ZXVilhfNkggU1Ly--2V6TEk7xNVIDc7p2v9_p8f2Rm-WEk0vBq6Mn57K2c419TzokPF2C7KIpO_ZwDfq-Z3nfOU9_YSrjcHFhx0QpjSVUl9iVbUxvr9W6kfRFfsB-MAqJVgu3f83e3KD3X_zkRj2gF-Nwilb-fytF-OmGkNDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد  رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/682842" target="_blank">📅 18:18 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682840">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gwQajq3taj_BrvalAoUgs6Q-MkaI8h5WKC_Klgg2D0rywKAW6cMcfeGTov97q2Tcq7iTdS29EKe2JouIdwbWdnergN6deDJzccXINrjqNXaDOYRIerue-EFItVtWI-x4ly_wTChzcKvi27CYV8DaF1ySOMS_MPwyHY4dvHjqOZdVPJ0WdAceeLxh3kDe9Te4h1xknNYBC4jGuYFMqkPQcHZk90PUUT9lLDmH6-_pnCk5mrssPGlsaa9GbEn4qAQ94i1Sw1wALq__Au-9H20HlKMNRQTfwTmOOMu9yGAjs6Piv0OBCoasqqexINy80pPwNUNE2NkW1yDEeeHXlhnSwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njOEQgnnRDGNEu7AL-AImFedYucE_oEV4rAHo8aCpFWG-1leYiVzMdSY6WiBvmseTh4fk5ijvotg6nNBXaJV1MF2pPeJC9y5-M4KeYRmQAZmpoI8XtJHYBhdpSGB4gyuSLr9SSoOr23kT-cw_oLJrK0GwULyxo1DKjF_Ma7OnYmJrftIg6uTtNF1Yuzv1GTFBb6qI22e6JOWWwPEZvOhjoXBu338PpXT0VP0i0Yxj2RljaCAyaR8bObgDV_FTGX-DNl7zXFYi_Mel75fKnipGRML2emyo0wRQ3jTVw4e0r1n4hcaMsN0dMRD8MEcZ61L-19Dx1GlgQ4DEMcGjGX4Ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور یک ناوهواپیمابر جدید آمریکا در منطقه
🔹
تصاویر ماهواره‌ای Sentinel-2 از دیروز، یک ناو هواپیمابر آمریکایی کلاس نیمیتز را نشان می‌دهد که در خلیج عمان در حال حرکت است.
🔹
این ناو هواپیمابر که مشخص نیست آبراهام لینکلن است یا جورج واشنگتن توسط حداقل یک ناوشکن موشک‌انداز کلاس Arleigh Burke همراهی می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/682840" target="_blank">📅 18:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682839">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/761bcaff79.mp4?token=LFkNSXv7adD1QFWFdCFn_vv2F0UU3O9qrlNLLbj6mPcdLEzGPbgjAAwSMvvJbPfDn810q0WuYZg7rUa47CqKTMqnSbDfSZoYpRC1If4scvOqJoQJ1on1CueIpiaB4gz4sXLsJFAOp21vXem0yIATVPEEuAVKpTTU3jgmNcIMWs-BnyY0R8E90GTPOHLyWcl6demAQJ-Wrh-1dGmjckC1UIGcvP8Ar7r0iY-D_IjbX1I3MA5lLXVY2Gm_lIONOv7wegv7Efh1fPUSHcbogBPyrPQMAHUsRdxg0iTtXMa-NEz36B0OZRG_ngtEgegZRtOEoAIAd98gy2poY1MDTyg6Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/761bcaff79.mp4?token=LFkNSXv7adD1QFWFdCFn_vv2F0UU3O9qrlNLLbj6mPcdLEzGPbgjAAwSMvvJbPfDn810q0WuYZg7rUa47CqKTMqnSbDfSZoYpRC1If4scvOqJoQJ1on1CueIpiaB4gz4sXLsJFAOp21vXem0yIATVPEEuAVKpTTU3jgmNcIMWs-BnyY0R8E90GTPOHLyWcl6demAQJ-Wrh-1dGmjckC1UIGcvP8Ar7r0iY-D_IjbX1I3MA5lLXVY2Gm_lIONOv7wegv7Efh1fPUSHcbogBPyrPQMAHUsRdxg0iTtXMa-NEz36B0OZRG_ngtEgegZRtOEoAIAd98gy2poY1MDTyg6Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطره همتی از توصیه رهبر انقلاب
عبدالناصر همتی با اشاره به خاطره‌ای از دیدار خود با رهبر انقلاب در سال ۱۳۹۸ گفت:
🔹
«به آقا عرض کردم من هر جا می‌روم، حساب کردم ۴، ۵ کشور که دلارهای ما آنجا بود و با آنها پول داشتیم، رفتم و دیگر خسته شدم؛ هیچ‌کدامشان همراهی نمی‌کنند.
🔹
آقا فرمودند: پس نتیجه می‌گیریم؛ برو قوی شو اگر راحت جهان طلبی!»
🔹
همتی با نقل این خاطره، به توصیه‌ای اشاره کرد که بر ضرورت قدرتمند شدن کشور برای تأمین منافع و حقوق خود در عرصه بین‌المللی تأکید دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/682839" target="_blank">📅 18:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682838">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8959805b.mp4?token=l3JMQXfupqOyS90mzIAgibG45OqPkHBdsSiIq2C1J7aLIWWjqwIryqRlf-2yzA2wnctzFVjAr8A7ETiSAuhibad46cJzHz5rmGAbHl9QaTEhF6m_FNry3dg7lkJivR3QL5eLgtPgENg3jxDx9Zb3Qflx6xhLn-FVaU9Q9FJLgQBQpjZUHGjQB2JhOTQEJtIs4mJ_BToAsLCqmzxIiq_jQIHZW_daA2gAXAcspB71w8vn8mgdbhOnBNqrtXInvecGdRIUMBVh7WPzjbA7tmgf-Wb7Vitn9VKHn7is67L6HcH-lYgg0CFfL4DlgrAD7NtLBGclQt199ge8MUrjXw9Ftg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8959805b.mp4?token=l3JMQXfupqOyS90mzIAgibG45OqPkHBdsSiIq2C1J7aLIWWjqwIryqRlf-2yzA2wnctzFVjAr8A7ETiSAuhibad46cJzHz5rmGAbHl9QaTEhF6m_FNry3dg7lkJivR3QL5eLgtPgENg3jxDx9Zb3Qflx6xhLn-FVaU9Q9FJLgQBQpjZUHGjQB2JhOTQEJtIs4mJ_BToAsLCqmzxIiq_jQIHZW_daA2gAXAcspB71w8vn8mgdbhOnBNqrtXInvecGdRIUMBVh7WPzjbA7tmgf-Wb7Vitn9VKHn7is67L6HcH-lYgg0CFfL4DlgrAD7NtLBGclQt199ge8MUrjXw9Ftg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پس گردنی لیونل مسی به کوین سالیوان در دیدار صبح امروز اینتر میامی با فیلادلفیا یونیون
😳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/682838" target="_blank">📅 18:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682837">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaMAZV7_moS8BYJ29QwyEfzlGTt0vbW6cMt0tKlqwhQzkAOrrp_rjtE4Vaq-vVagYdXe1Ls-UVvGg3sxq5sYdZ-1J271QbvUvQlNOVgzJT5GamyLcV3dD2ZnbrkFMUS1AOuzHJwADFSx-6YHxGJ2pdjZnOnFvZQywHkyaQ0buS4d0bQXh-7DfKFpuPUrnssSxWMIJYObtH2Ca8E_HzThZAeEpgmZsvAKGQECIHVYej2h6wlwSwd5QQ-esyU2ZIgC9I5TxEctO9wDECf0VfbwCAHP9FAgx2YyafecLX6Hcgk3GD1ZPzYHQEYF7vjORfaOrVcA0ZJtD48HE4TUbAT2Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عملیات شکست حصر
🔹
رئیس‌جمهور آمریکا بامداد پنجشنبه ادعا کرد که «خردکننده‌ترین عملیات اقتصادی» در تاریخ را ایران آغاز کرده، ادعایی که در شرایط کنونی، ضرورت شکل‌گیری یک جبهه منسجم و قدرتمند در داخل کشور برای مقابله با فشارهای اقتصادی و شکست این حصر را بیش از پیش آشکار می‌کند. عبور از این شرایط نیازمند تقویت همبستگی ملی، استفاده هوشمندانه از ظرفیت‌های داخلی و اتخاذ تصمیماتی است که دشمن را وادار به عقب نشینی کند.
🔹
هشتصدوسی‌‌وهشتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/682837" target="_blank">📅 18:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682836">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ادعای بلومبرگ: چین میلیون‌ها بشکه نفت خام عربستان خریداری کرد.
🔹
سه نامزد مورد حمایت ترامپ در انتخابات مقدماتی جمهوری‌خواهان شکست خوردند.
🔹
۱۴ هزار نفر در آلمان بر اثر گرما جان باختند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/682836" target="_blank">📅 18:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682835">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DM3U_8F8FcflXbEbBgLRGnH2N2fi5_cPbxeTRSYQajcU2f-AtWWe04rKmczpZqo3vTxRAnT4ExbFNDpmOzRIL8jMNtNwb8UH9FgfoD2R9jfW0NTQ38YwT9QOwxdE2FEctnvISWVrZjdng0_SWUnDxcZAKCB6PqepPZSdaZvzhPb-Tyd3gaa54MdV82hvO_4T95_0eFIFsz4z39lrqONvovfl8XkrEtRhm4W_oKAThi1fMUcYLP_Iyq5daVUOHOEo8ftPvtULsjQuie1nQUx379tUd3zcK9ZTZ_sMLHyM0-QyyxBPyklZYgPpn7pMxIonm9AT1lUpzB3dPT6lUAbUKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عارفی که نامش با عشق، عرفان و عمق اندیشه درآمیخته است؛ عطار نیشابوری
🔹
فریدالدین عطار نیشابوری، از بزرگ‌ترین شاعران و عارفان تاریخ ایران، تنها یک شاعر نبود؛ او با آثار ارزشمندی مانند «منطق‌الطیر» و «تذکرةالاولیا» اندیشه‌های عرفانی و انسانی را به زبان شعر…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/682835" target="_blank">📅 18:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682834">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b03c53ba.mp4?token=Gvsvcw-edSUMzXvc_EH_aTS3E7nOYb-U779EUJ72vAC5PUpQVxnabkiG2H3fopNNPQYxMJvgwKkF-63whFegFA7SdcwUkGRtyKE4zAZAbV3M5gH0EfbL95qROuKSdzY5HY2paR6gn3xwmEmZ2RYHBGNrSboCoT6G_a2G00nyytVjs5h-bMSacrZU8p1240g-EEC9-yk_OG116bUjNxUKCVHfO9BaMLAK3dstbYX6OIFhqZC7F_G8Wj4j0HjzyR1-SjTGJ8w20pI6GMkwaftkpbgWbPESkOa4az8maLCtKhL_AnE4hhG0Nsn_tWvgUyCSuNWKEp3_D6br5OhzZSDefg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b03c53ba.mp4?token=Gvsvcw-edSUMzXvc_EH_aTS3E7nOYb-U779EUJ72vAC5PUpQVxnabkiG2H3fopNNPQYxMJvgwKkF-63whFegFA7SdcwUkGRtyKE4zAZAbV3M5gH0EfbL95qROuKSdzY5HY2paR6gn3xwmEmZ2RYHBGNrSboCoT6G_a2G00nyytVjs5h-bMSacrZU8p1240g-EEC9-yk_OG116bUjNxUKCVHfO9BaMLAK3dstbYX6OIFhqZC7F_G8Wj4j0HjzyR1-SjTGJ8w20pI6GMkwaftkpbgWbPESkOa4az8maLCtKhL_AnE4hhG0Nsn_tWvgUyCSuNWKEp3_D6br5OhzZSDefg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر آخر الزمانی از انبار استراتژیک سوخت در منطقه کی‌یف در حملات شبانه روسیه منهدم شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/682834" target="_blank">📅 17:53 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
