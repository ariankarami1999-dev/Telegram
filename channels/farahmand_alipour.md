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
<img src="https://cdn4.telesco.pe/file/gvECDOmNUx6HOysHFLkktbAHlAlXrsoAL6Be418BIxCzSHWynrAH3XdCQtrgY9RMyVDScOPEZOmDLp2ZsX9TSiPVA9p5RYPS35O-F_IipEZbWCGzcAbZ0LYhhvmy0JlAXQgpZhSh0w3c4KPkdifzmdu5EWyJ9vIpSVKm9au-UfppHZ_bEvD22Svad0r2gyToyMp3gGUUGuMJvuhCDds44_O_VPhtMmDMEMCtxBdn1dYBILdbm5vpIRHuikl6XFrWr9N64XG8yR7aWrHxdFpXWZtxEAHXviUEkE0iJ5yI4h_7b0qOiEq2_Cs0j3-knUiW9mzzvsPdKIpbd7IMqDoXfg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.6K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 02:56:49</div>
<hr>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=GF1UkNbw5RhA93yp1mSNL8CWu4MxqtdLFHyb51FqEB2a6Q3eRWPM0MBpzCzp5WUXQNhaECHnh65Ok5asXfDzmLoPSbhgjB2k9EEuOozGOBzwVrzSpZ-EDPvQb4YMYN4mdsDutRBSZ9YYvEs4pkoZqY-J_uchXLMNuaFXT-g4RdNakO2-EgypQnWPSIw2XRpcHvjvnDvYHy5ZiUUhMfF3_en6USPLjk8TkssTKmomKyNuZ45j2ljuFNoMVWU8kNPdr4YewWUcLvqOa-YZcuo9_SCJ1gruHoA4e3j1lD3tdMQj9dXveVQG6wTTvWbEysNV1TpJRWv30n1XVsBB4DyBbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=GF1UkNbw5RhA93yp1mSNL8CWu4MxqtdLFHyb51FqEB2a6Q3eRWPM0MBpzCzp5WUXQNhaECHnh65Ok5asXfDzmLoPSbhgjB2k9EEuOozGOBzwVrzSpZ-EDPvQb4YMYN4mdsDutRBSZ9YYvEs4pkoZqY-J_uchXLMNuaFXT-g4RdNakO2-EgypQnWPSIw2XRpcHvjvnDvYHy5ZiUUhMfF3_en6USPLjk8TkssTKmomKyNuZ45j2ljuFNoMVWU8kNPdr4YewWUcLvqOa-YZcuo9_SCJ1gruHoA4e3j1lD3tdMQj9dXveVQG6wTTvWbEysNV1TpJRWv30n1XVsBB4DyBbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل کوثری :
‏سردار کوثری: شمخانی برای جلسه فرماندهان در بیت بسیار اصرار کرد
‏سردار رادان جلسه را نیامد و سردار پاکپور هم نمی‌خواست جلسه را بیاید اما دستور شمخانی برای حضور بود؛
‏وزیر دفاع با معاونینش در جلسه حاضر شد؛</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=pfQd1RFoIb_pYjvjjK7tQybT7GR5mhCKDZAqEmvALlsUCatp6RFWaPFrwVlg4RHkgWr83PydnLpeuQkPrMO-BXSHqwcDOWHSDnIWf70aSkajIku7P3vnQ9GIRTC5k8M28LrBCaHB4rqch1LF4gUTwLgBR57WG1mpEzwxw0UrXgswUzg-7gRbRSy1gbDEh-BVHoQGI3yi70LaCfDY5_UJbvmhUoeSB37BH1q8IzTxJwcqNOQPOcRhiL89GL1aBS2ihzW5XA3yjvfQ2yCwzr_Wa7FA4vxwJuGI_GQo6mAJqPlOy2v7gXneXBHQlxSa2-Cm2BY3ZBMnkzEHFG-CKyDmVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=pfQd1RFoIb_pYjvjjK7tQybT7GR5mhCKDZAqEmvALlsUCatp6RFWaPFrwVlg4RHkgWr83PydnLpeuQkPrMO-BXSHqwcDOWHSDnIWf70aSkajIku7P3vnQ9GIRTC5k8M28LrBCaHB4rqch1LF4gUTwLgBR57WG1mpEzwxw0UrXgswUzg-7gRbRSy1gbDEh-BVHoQGI3yi70LaCfDY5_UJbvmhUoeSB37BH1q8IzTxJwcqNOQPOcRhiL89GL1aBS2ihzW5XA3yjvfQ2yCwzr_Wa7FA4vxwJuGI_GQo6mAJqPlOy2v7gXneXBHQlxSa2-Cm2BY3ZBMnkzEHFG-CKyDmVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCZ1yXQ6FhRPmcxxyBg6KVDd_Sp59V1PYH-JA540T6TtWtfR-H10TncZsV4JyZEZs_wmmVU_5yN8vpzZ6EAhHfpq9d_TXaIEY5biUDIfUGm1texnKh7_ltAYd56wwYjKIClxtW-7a-X1vgy-mDSYtU4raNsldyX_w0nB3FjMxFSKAm9mLjly5WvhBYzsN63GkWe9Vx85ogWP_-26SKoJhtYiuGSLvXoU40XTiA6_ir0FeTncpUj_C0FJKdOL0gxtWd1cqLE-ibfTopuSA_EKBf6lPkV7NrTiz94bGBv4LAUf667Xjzr3RG6dpSxzsAGZSiz-yfr7xHu91Jrsf6ITbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDD8QKRBOgDsnWDMdjA64O6zFksCOimNUqa_yZHEc5vRyMrEBisy3Ums_07eE_eT9-0DAskJMqDLtheC3MO-wLb6yWps1VbIBDsd4CqFVVgGcF6fZKqc6HGGpn1iY37J4MailIHcoiZDj18cwVd4mxyVgonpjk1J188n2Uct5KG1Yp4Z8lnqf7oOCkouOv6qVwWScAlpA6EFN0qwGbxEuiOA-OQ6KmhWcOmWYCWyE-a_nnS-jxZu1tHO22eXsV7luRFOWcpezJUkvV8_hcSNuUt98kMzPYjbfzB3UDVy-SM_Dwcl3n6Y7-T4k2A7Q7mw4uNG6Pv9SWOgGdQeXc16Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eILzOXHOarqSYIIAHSyCHWhdzZB4X3md3DyUFOBnBW4tBrpBYXtHhH3LKYtY_lwxiHx7ShwvKEj-9DuOkEayvRZITOEIkGY1cduOuUgZMWmj9A76513ay7rMAfvgUV-UJ-rEB77jExd5nYXkFKKuhaChzqYLegnEy-iVsXhYnSVQacTSWbc8t2lVE90-Dsq4gr7Ko0arMiiXh3d77epV3KINMJ_FP1cYqezlU5UXcPjseMsPBCkdULLdE72z95o9oJK6npUrKSentI6YfXa7Mj9i898NGHGNy5G9qSlq3vEvDz2C5PG_MyBHXwkIg7g_PrGtYgfTNj53iTkDKHoYNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jl2X1-CitVn0L4EDM-RE9P6e66odRt2ME5x0UMAGY0-pQ8Rziuv-_40FfDDNFH_7beJSW_IYCEFNyXCm8V4b4_Wg3ut9ZU8oreoCodVqLPK0S4gEcCy8od6u_pAo4unuOKzkRCNPpOQom9Dw4BwCDr7UZcJpejSM4K7i10ewhbuu2-J7500Q4W0BdYj2PEsuYhJ8xTACCVpShLE8xMQ_9jcTd_XY4Kp48tb-qYZYurMsJTA-YW72vWjC-Q5DvAigOSJWaxVD8G-N7Eq_YgObzX3YruxZ9-Jyaqjo7GJ7PKEVU7I_YujAkF1HkjLbnW0K7qEdfyCLxaE44oqIPC5nuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FF3uMIDUj01msi45aWfMC_O5FM_K_vjR_1t2xZLco_0qh01kLNqkCI_JcQiWKdQkUfQwg20LEZIisTyBj1T3nzuAbKYYx6epsYCKzx2O2PSk275HkUueCY4FPW-WRaVj6XhtJikTyv3R5SrvNYAosttmEbE4iL_Ne3-F4jsYPsB6tLODDgx9UTTM2dvjmXenq1MByJypGaMBo2IfQ99a9OXc6i26Fiw0ef--obA8fMfPG4902NQGM-Ie6QeiFkvJ-Xx6XzexOyUC-OJukf3zofSDORgHN5BQPgc2BWSBbZEQ9wE3r_uqoZSh9pNuqSB-AUxUB9Q6C8CCjyJq7crarQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mjUYHbNVt_c-xm-KxtTQGavRe55dl2GWVUOboGagwbvp8i1OVOA-aeeJ1XKn6DKi3E-lHJ5VBvQExPe6iiV6y-W-7dpKCtbeQ3YmnJCMfdUQmHG5-N5aIMtbeOavaDXaZPQUqE99Znh-9fwZQqFEjbzzgIhjVHQ2_HKkBMPon_Kcs8tBmVgbW4nWwPE5oBn2aN2ZFLTF2hVwEUQWSLQWnzIYHJRLiHDdd8_G4WylGfuDCPB1fBy8YMXg8o74F_bTkOQL18RgRYCaKz-jyAw1MTo8qXPc8q5YZz8heEbL6GDs7RjnE2NomYkLGbHWgDCsZQEJ5uW1PfVw6ObPpziZ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oTAc9oFRclu3KwjpG926TwFrmFXRfPIMLWhJY2vZbDpgFed8zYj_IBvxOB3D0dFK7BAlOB3k-yGUmWIydcC2nvDPffAtdfBdNsUvJh9Q3eNEG_OIWzIf3AKYpoyio_N1UDTpsdJiFGWTN3Bmiixnsuk-0Kde5KB8zelw6erNJUttpYq7HCimT1H1lpnX446BzpMMSQz_XSD48A0M3BG1bJZgTBGXoIj19c_VRkt7f8OecQNvaZhK6AedO85i35RO_LwcgAa9bg0s2fsUX1DQYb2OVsR2_VhLLWclH1qdMtBm4KEQdbj8Nzgz43IbsLZyA0U4OFYw7xbfbRjGbrn6Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M8092S92cD92Z57R7e8RPPVN2hNhRH5IhIT8RNonlRN3M9GXwFyARm27EXH_exNKJdOyFodMznGaP8qxEnj3wv6snhQ-NmyZ2YRjaDMPvz0MGl4OLSvoXsJkMKxvq3lvMp-XHKWcN6tl7Lxvvnml7-eykw7TWWr9s7Pfawli1vcWx1CtybPjc1bwC4oK9aGsbkd1Uta7aBnAJW0NDMc4O482-9vtbTQsqCxOIb9nX87m7k6IDkuSZLQPVoflFLcxw0dzW4Kf0ziJsk_Yxf-C7v3l_AdB_KPZUx0oj3RL9pXwZmSqXksRnLV00szph6X0hNRLWv9-EywPtMQxWNsw2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیرین مدرسه ساز در ایران،  ۶۲٪ از مسئولیت ساخت و ساز مدرسه  رو به عهده گرفتند. حدود هزار مدرسه.  فرض بگیریم همه اینها مدارس ۶ کلاسه هستند (برخی ها فقط ۲ کلاسه هستند)  اگه هر مدرسه ۶ کلاسه حدود ۱۲ میلیارد تومن هزینه داشته باشه، هزار تا از این مدرسه‌ها میشه…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6524" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNEw_mb40CjoTGjLg6duRqUYPDL8fFH3hoj9vWW6p7--Je5Hq68zwqvVDlOUyoQFL34vtrT8LR9JYLoejO2SYO7V25xPQo99qmUk9pG3zrmFL8gQQl8ssQHBbhUSGUDdtn-f9ZX6PEtopguYeOjdjDuO_-hyYB6TJQOpHpSZXuExUWjFxZvZK8CRZadDB6bNbsJsWDYLsMujfFWM8YZnA-rSMAMbn3HDfeyuwuhHW2TxVunySXmKizUWzDB5ijPGeZjXqV_gI6Vji7iqDRf22qQPz5_tW6-nTLtAIM3CefBAShFL0Y4MItrClH8YA5sZRXDlSWX2-U7GusjltLFy3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا این متن با دقت بخونید و قضاوت کنید:    پدر یک خانواده،  نیمی از درآمدش رو صرف مواد مخدر میکنه،  موضوعی که باعث فشار  و فقر در داخل خونه شده.  مادر خانواده ، چون بعد از اجاره و….  پولی براش نمی‌مونه، معمولا از بقیه کمک میگیره که پول پیاز و سیب زمینی و…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6523" target="_blank">📅 14:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">لطفا این متن با دقت بخونید
و قضاوت کنید:
پدر یک خانواده،
نیمی از درآمدش رو صرف مواد مخدر میکنه،
موضوعی که باعث فشار
و فقر در داخل خونه شده.
مادر خانواده ، چون بعد از اجاره و….
پولی براش نمی‌مونه،
معمولا از بقیه کمک میگیره
که پول پیاز و سیب زمینی و قبض آب و برق رو بده  برای سیر کردم شکم بچه‌ها و…..
هر روز هم دعواست که اگه پدر اعتیاد رو ترک کنه، هم پول بیشتری در خونه می‌مونه، هم کار آبرودارتری پیدا میکنه و پول بیشتری در میاره،
هم خانواده از این فشار و تلخی.
🔺
حالا سوال : به نظر شما افرادی
که به این خانم کمک می‌کنند، دارند کار خیر می‌کنند در سیر کردن شکم این بچه‌ها، یا دارند مسئولیت رو از دوش پدر بر میدارن،
و اون هم با فراغ بال بیشتر، با شنیدن غرهای کمتر، پول خرج اعتیادش میکنه
و در واقع کمک هست به پدر ناشایست؟</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6522" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=jBn8yXAFm8RUYKTtgYFp4Ji68TaHOmLHldCJ7hVjhW7X9JpZq6X60rnkrMgBmo_7pG-GX4TszmGPBw9uTFG-xDzy21t0pvt-pR7w8UddyMn1oE8drNFfeibP4o7GDHIXwHOYYLgw9lOXMNiIXAyBaljpc6Rm9Fhcbexs0go7iogR1ENMVoV5Zlb6n76tQCZDEAUQV2rAINorN4DOAQwM1DS3-w4hKC_OdrNjxQelU8XzVPznLDI8D6hQI66W26cO4KtKTgajmQAyAeG6Km4wMTjBQPSaLbpnnbU25VC9ijaXgCcRpA-C3Z3R99YBJ6p3yRwAZ0AqbfiGsrokLnMe5Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=jBn8yXAFm8RUYKTtgYFp4Ji68TaHOmLHldCJ7hVjhW7X9JpZq6X60rnkrMgBmo_7pG-GX4TszmGPBw9uTFG-xDzy21t0pvt-pR7w8UddyMn1oE8drNFfeibP4o7GDHIXwHOYYLgw9lOXMNiIXAyBaljpc6Rm9Fhcbexs0go7iogR1ENMVoV5Zlb6n76tQCZDEAUQV2rAINorN4DOAQwM1DS3-w4hKC_OdrNjxQelU8XzVPznLDI8D6hQI66W26cO4KtKTgajmQAyAeG6Km4wMTjBQPSaLbpnnbU25VC9ijaXgCcRpA-C3Z3R99YBJ6p3yRwAZ0AqbfiGsrokLnMe5Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رجب صفروف، عضو تیم روسیه در مذاکرات رژیم حقوقی دریای خزر، مرداد ۹۷:
‏همه ما انتظار داشتیم ایران درخواست ۵۰ درصد بکند. قانونی هم بود. اما جلسه اول یکباره جمهوری اسلامی گفت تقسیم برابر بین ۵ کشور، یعنی کمتر از ۲۰درصد
‏برای ما عجیب‌وغریب بود که چجور ایران دارد از حقوق خودش گذشت می‌کند
‏این برای بقیه کشورها مثل هدیه الهی بود. از خوشحالی نمی‌دانستند چکار کنند</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6521" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6520">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbfFSJiTnLRGR2RUsLQXnScXf9XKEUjNwYYdui1jNx1qsIzy0ilDtTtoCKBi2R2YkopRoITmAfuacKLcCxGAaEsER23owEfeFCMhsTlb8TmlWaX6lZgYEFKj80Dph0ztAJmXfuadTmsY2YcFALx61brVs9E-Vjt4yLe2rUpHK2sXVVOmJ923Cv7hUi5yUqzGvNSR4A04v5MVBaVAeGiVzhxfyFnhKiKTIJH1Rlqo97E4ZAFEjlQkbelW84BFDAfZ12ARTO_Xg8wt4d3B4-3gP69w0XW5pKZKWrIAksdhE0hdI3uwM76vJR_HAhxhHM0eEpwrCSvCWr9KRzRfGoD3vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی به عنوان رئیس شورای عالی امنیت منصوب شد.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6520" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6519">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSD1qUH69vTcBd62Gvk06EaQ2uacnAehuG0sFRJKYSi9mk3iupk4LeanDHSuijZ-_3chBE7ER3mBuZ680qpaLLSTrVhqEBEGY211XTTzlRJdmnvSg8GqCC9XM9xnPTEAZQBZDVAP3kOp4Yxs7NDNqRFC2faaFI1sM5NosDxOi040oAcBjGyY0Xnzq8JoyQDR-IHJtQOMF5RdsvaHNHCMGdeydrx2M-uZjj_zL3joGOTo3t6cmWkEm1EA-2HA_CzXDSiNTpagFJqHncTe1G7CoKaxXY7Av-nHLe8SyjDtJn5rPVQ9sRnuWHhlCVbFGwYXLdJoKWJqczLEBM1mTt8OOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«حمله‌ای گسترده در راه است…
نه، صبر کنید، می‌خواهند مذاکره کنند.»
این یعنی «دیپلماسی نمایشی»
که مدام در حال تکرار است.
استفاده از زورگویی، وعده‌های شکسته
و اخبار جعلی به‌عنوان ابزار فشار،
راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید.  ما به نمایش‌های بیشتری نیاز نداریم.
- فهمیدن حمله به کشتی‌ها و زدن زیر تفاهم‌نامه نمی‌تونه براشون دستاوردی داشته باشه ، از ترامپ میخوان که مذاکره کنند.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6519" target="_blank">📅 22:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDonVAY5-0ehq4jRhtMYiZPtUPXuA2JC9WN9Ty1sBAfEec9lnEOAUQbO4MSLGMLjMfRPPVo2NK7615rUM8KC6st1b5A_nUe9HI_xlgY2zFWiQ0pFX9YEnPs9YH91_lxQdnBA1UTJwtMFgAUWsSC_50abHM3JJjwlpED9GZQbLCLYDgg1QW_Rrom6RhDBJ1eFhIkpXfSb1UeQxyrXJPp9gwGUI_8K5Nq9MrVcrF-a5TrPmCWn-DjXdTtnQtWEmK4qK1mM1Nt6nP9M_WvCQqnS9ko2LZ8cqpPAEeRt2zHdSfHSKq4SJhPK1XkAAmboqYHEsgD3JDH0kZnnDCtE5prcLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به امید بالا رفتن قیمت نفت و فشار به ترامپ، زد زیر تفاهم نامه  و حمله به کشتی‌ها،  که با اقدام به موقع دوستان خودشون  در حزب کمونیست چین،  نقشه‌هاشون نقش بر آب شد!  خدایا عظمتت رو شکر!  اما در عوض برنامه آمریکا در پاسخ  به اقدام جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lARvUPgAgcyTaTjq5994VXXOpzy2ILpcCEyVBq9fiRf26ZvvN5SyLyCejI69z0qs9CHIN-r8e98Swzxo3u1JmNO4c-uSRV6MnL_UWIz3Oddy0FD4N1SgTQXyN9nVaunCI1tKz7XlUdRdtDQiGeUzVfEsXOiPdEvFXE3j8m5OQkC2QD33yZBZ1I2VmogH2VQvQpl2CX68wyjVU08j_wxOEqe-2JEyXb63BwvqJ7kvqnbM6IHtNueR2430bYg-FD-Mg75Tm4H-0n9d6pX7IUF27MKqPMKxteoB25jYw0vkZV4kH0tshSU8VusYB_Hj3o8CBJ4Gr6IbpqT0E5AQRT0F9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم : افزایش تولید نفت کشورهایی چون امریکا (که رکورد تا یخی زد)، کانادا،  برزیل، قزاقستان، ونزوئلا و….. است!  نکته سوم ترامپ!  و به نحوه مدیریت ترامپ برمیگرده!  بازار نفت به شدت حساسه به اخبار  و به انفجار و ناامنی و جنگ و…..!  خیلی وقت‌ها قیمتش «روانی»…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bw6BDdxo9m8a9q877SFpXelUnRx7bixCRetGSSUxHDDiTn7q9__uhAUWd4fTXjGg-2LupulUZnd5-roaA0TSlhqYgMAyPrTKiqlVKU31jFbVkRW81YawPCjCYrmEs1nVy2QSneyYoUA1busrZOwLrfxEfiRSLGtK1787kjv9hz0ttEy3pD1L82NyOh8jD6sgUgRfd0iYO7XQUbWcbH4njwHM6ssyH0iii6Z96i2zl6vrLW4zGmE-XQ9vUkybqoDF4ZOmn3AatOxrYQQH6cip5ZtRhVXNX3P9-XsNsvFFGiD_Mm4KCM6xyYjjCijzhZOEJg7aKW3uHpS5JmTOgYJrmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VEVdrJJDsrGwcHo16-idHUAPZvFul2-6HRGzWUdSaSYdZ1uYsHSQPLt7FA1ftDgirqOho3TTI5kxfezdJ0C1DSj8e_Dr0OF9rY5luqZeXjBXNE7RyvJCuZjwlfhpzqVTBF474VF-rtSxvGyS1x9Ud3Ts3wU_nosHsO1_ikLh64ppKH8vE1Z4lzr2AFE2qvHcJ8Fkkwi7i5kp82WXRzbgDiaQa0srxGnTZQbJ2LMVjWMaX1SA_tBzYL_rhYGTfLo4Jo0Dk5o8y-ogesHoscCY2JW1AvjfrnUSzqiSm5jzPdeDh75X4LMPmWhsP8fpfP3Hr9IbM544U8TTSOvVceWlGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tUnXYrvnZxhnpvEHII3ABspQ9kAEzuEAp2frZ5ABGVxHlxXe537jfkdNCbrzRhvxQIL25sojfnQUMqZz8vANogyCp6xi0Qgci_y3UpmSKm_vPMEG7yzwPRgPPwcjWaWIVbJhS8SqEuj5tabo58h2qUDJ4lSr2qbJ4d7B9CPPsSLPmvVm9Tr4CpINyNeRPChn_8hXBLbKae--ksivACPkWVgrqjp2wB7u2IvbdrTk8bIGYsV3_mQKR73lfBOMaWsiNeFcFcqsxjy2AnlDzzY5MsSH0s01xf1J9X7T9J501E8C0pvYw9G3dW3G12wAWDmOPMNoCRp388P_it4ujw-Kfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.  اینها دنبال «اتفاق مبارک» افزایش قیمت  نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.  اساسا با همین منظور شروع به حمله  به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6513" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=SkNUU8wOLtXQxIw9ZymcVdRoK_s5NrX0AS5VLpPlBZJ07iNpJkTAC-0fpzmG5NwdYjDDslxoKcIXTLBd7mNyfVJ8VayiwvX6MlUXFry_gf99resdXnDl9cewu33adHt_o1kZcafAMb6xxjZ91A8QWd9ZqL0sWDkVMNo6luWNPC0l14MWzGRJZ1evO5qe6-irug1j7zrczrSpDhp0IHewbtvG85ZDrVrd2ENGQb4z2abkY8lll7VryKe9ryvGRZf26MaXn9OE9jL-xfagcGFVvzKdZO7HhsOVl9SLp2D9aPykS3UHVMSkUonGZpT5sP9KJfYEajgqH9EA1dIejAB0_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=SkNUU8wOLtXQxIw9ZymcVdRoK_s5NrX0AS5VLpPlBZJ07iNpJkTAC-0fpzmG5NwdYjDDslxoKcIXTLBd7mNyfVJ8VayiwvX6MlUXFry_gf99resdXnDl9cewu33adHt_o1kZcafAMb6xxjZ91A8QWd9ZqL0sWDkVMNo6luWNPC0l14MWzGRJZ1evO5qe6-irug1j7zrczrSpDhp0IHewbtvG85ZDrVrd2ENGQb4z2abkY8lll7VryKe9ryvGRZf26MaXn9OE9jL-xfagcGFVvzKdZO7HhsOVl9SLp2D9aPykS3UHVMSkUonGZpT5sP9KJfYEajgqH9EA1dIejAB0_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.
اینها دنبال «اتفاق مبارک» افزایش قیمت
نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.
اساسا با همین منظور شروع به حمله
به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6512" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.   خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.   او همچنین با اشاره به اعتراض‌ها…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6511" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=lRussC_4VjcqGd5vPqI_yE8Zea4Lz_WiGQIs6DEQM3M-WH1P653gTYJbkRiMd4vyvYNJRc64Z-e4iRPYJxmEuXXf_zxLd6IZ06FQgVI423cA0Ml3XhlxPOwlwJHNA6nklcV0lKV7MYhOtYONtD3JhGwlMIq6hyihwTysgypI6QX58WerzMQNYoNCuRnyiuluh93IVJTwSjU-45I5F87Seth3_Ao_fL8qtcf4FdFAPeNCflciuRhJv0jhS-ubN9dI8zbZzESfbjUhWuBpzrW3F5N05JkSnL9FIK5navAyRMw-fJQJ3-e_eWSix4iJo1g3Jui8tM7UJMRnPaFe1CbQPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=lRussC_4VjcqGd5vPqI_yE8Zea4Lz_WiGQIs6DEQM3M-WH1P653gTYJbkRiMd4vyvYNJRc64Z-e4iRPYJxmEuXXf_zxLd6IZ06FQgVI423cA0Ml3XhlxPOwlwJHNA6nklcV0lKV7MYhOtYONtD3JhGwlMIq6hyihwTysgypI6QX58WerzMQNYoNCuRnyiuluh93IVJTwSjU-45I5F87Seth3_Ao_fL8qtcf4FdFAPeNCflciuRhJv0jhS-ubN9dI8zbZzESfbjUhWuBpzrW3F5N05JkSnL9FIK5navAyRMw-fJQJ3-e_eWSix4iJo1g3Jui8tM7UJMRnPaFe1CbQPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.
خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.
او همچنین با اشاره به اعتراض‌ها و تجمع‌های خیابانی گفت دولت مسعود پزشکیان به پایان دوره خود نخواهد رسید.
@iranintltv</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6510" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7mV6azgv6kGlRWnL6QKQalHj68JiMgO1gNcGwRU1ZQGe1EVzY8IFxseMK4UkHeiTdxWTuAPAkeoJPq7jSTr0V5txwsByphqoz4e0cvw688X6n343_2c_q2fgWr9_EnRJh0yX_YljKF9IYh8kPYVWH2DhbppFxmoGXOM6Nx_TrhOR1gZq_GA9ulqAFU5M3wV2PhEbq9sS-cPYMYO_9VgBAX9M47XToo6Vt0oS4Cfgxd9D1a6ig3xD0MOjbRgHRsz-hVcjn2WI4bdVMmS11LUGqIV6gALl0gdyl7syK738g65j953aYdqiOy_fP_Rnp0vLN7lmu78CzUpNLY6eUlvoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sznu-DFyznZE9NK7iY_G3WHMRwBWJkIi-GlpRnd4Il1d27H1Vx4WE6UM0IyfWxBaNsuVrFrN-rzzi7Z9TIfE8xa8uI4s6GCT0WE1SYBxrclEsyiC4y5XgDm1nYP4D5kDrVqHNaHdacQHFylgbXj3KU9aiiVB3tekD1HiyrULZau_hPEE9Q8XG0eOSVoPiNBlitKfg7oktGefd5gSOGv1BpyAmqF1Aiv2l3jj5Y41pt0qopHB63V6IXZyxBDoDoPOGxshaSvlIydo9fCwxbH9E-wqZQrHyInnu78AUP7Te5vmXggdnYxrjmVcmbLdBtzrwJvLarMN2qK5RS79XRkP3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=AwpfyQ_k124NWWY962RN1l-GqfxjlSsiKGyZjOI8zKI9uXMp0_np1dqalQXWWG8-Xllhd3UghFGYZ0ps4PvHayKemnxCnYLHdPG7yQyLnxLbPCoAQx1N-RW3xhdeycSZHnQUqsOkoLr2OE7dvIhzWIyRkUhtohiipyPqGs1yn7e8ghg8YoM1I-gd5SQ5JGDczvMvsq7hDCtbUoKdUpAIxFNgry4Lgg8t0UjtwE5eiWuPkSlbboWGaEFW16jA-WZsZHagvSE_EFxrgWa1Ku603aU8_XukTaqJATrpWexOtgclv7AJA3DLDWAJAfyBLpRiWSKvGiwDKbLvWz37rR_FQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=AwpfyQ_k124NWWY962RN1l-GqfxjlSsiKGyZjOI8zKI9uXMp0_np1dqalQXWWG8-Xllhd3UghFGYZ0ps4PvHayKemnxCnYLHdPG7yQyLnxLbPCoAQx1N-RW3xhdeycSZHnQUqsOkoLr2OE7dvIhzWIyRkUhtohiipyPqGs1yn7e8ghg8YoM1I-gd5SQ5JGDczvMvsq7hDCtbUoKdUpAIxFNgry4Lgg8t0UjtwE5eiWuPkSlbboWGaEFW16jA-WZsZHagvSE_EFxrgWa1Ku603aU8_XukTaqJATrpWexOtgclv7AJA3DLDWAJAfyBLpRiWSKvGiwDKbLvWz37rR_FQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!
که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده
و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6507" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bot-NlGtbg-QQZOOXKcoXXdZgZ2xSojfeAC4yffkc2WwrQ2v2pHYjPjb4VQ2bVpDicaO8qTNSdYswiZRfnXZzEjLmqwR1x8DLz5-r_Ni6fZFIluA-y3HdMLRFJrt9MVqaQJrPjtS1twci9I6nhQ8u2ZXUFU3cxMRq8KG-HbiCi6Dupwxz-AiXxqBtthB3CaEZLplZwjFlnLAzUk3YoKugDCZzaodq8gVON1aqBW_I3xdvTnNQHEH9OEMK4-1yyRNC8GGx9MbevErYw9kV9DPArTPlrwBjNpGRaGo2bvl0Iz-1ZDn2qESQRp_daDE_tBBEH1CYpdG3jWnqkrL8Sxw8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBBCPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHcthD65L4YgwadOtAYix56JYY6IOC93shXA5Y6krQDIS3kANhRsHVvRXJij65uMSIEy2E-3LEspbSvYVwI1FBIwDM6SseKtXMnX6QXpU_xts84FifQSCclC5pLXOTQ0ko0Lh3B8UeF_loyJGauG5LvhZla7cN2oitPGwCscJ0kt3xwz6UH95_KBQIQ823g1zwMILDiPFMUXtmwylNeJtQUQ1tvwALhdqSaXp_zXM0924ZMsO4vimepKUVX4oIal0X2LkdK3aLnhXaiC1QpY6yQ2W35Xo4O9pOIMzfWa86pJx3CfClhKH3qPp_oLDcL3XYLqRAb08IhoaZOhWRdP6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔻
سازمان عملیات تجارت دریایی بریتانیا می‌گوید یک گزارش باتاخیر از یک کشتی در فاصله ۹ مایل دریایی (تقریبا ۱۶ کیلومتر) از بندر «مخا» در یمن دریافت کرده است.
بنابر این گزارش، یک شهپاد به این کشتی در دریای سرخ برخورد کرد و باعث آتش‌سوزی شد اما خدمه و کارکنان همگی سالم هستند و نجات یافته‌اند.
به گفته این سازمان این کشتی اکنون غرق شده است.
جزئیات بیشتری منتشر نشده است. ساعاتی پیش حوثی‌های یمن که همسو با ایران هستند، اعلام کردند که با موشک بالستیک به یک نفتکش سعودی در دریای سرخ حمله کرده‌اند.
این هشتمین شناوری بود که از زمان آغاز محاصره دریایی علیه عربستان سعودی هدف قرار گرفته است.
سخنگوی نظامی حوثی‌ها به زمان حمله اشاره نکرد.
📷
Getty
@BBCPersian</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29785e012.mp4?token=L80KaQxKfRu6Y1XqAzFqasD3OMKUwgZTGq3E60RixVI0XARc1DdWpvzQyIroWtG0ORdpG9lD3fuJyO-WLl8pTJow8Fl1-x3JdgOdugf7GQJ-ZU6UEqoCUczqp3OzlaeXSvmcMKK5Dfs7PmWPth9Y5jbV6HOLfgJ0JIPOsWDwZ0BeM4it6P2DQ_3jr07Fg2AKanadFPLBUB-QDWvVpc6ij8FXaseyLgbijShJYz40fvS5yRRrjpG1K_o3T5o1rG5v7eJN7318U4pJ94-eQx4P-fBdiY6FnbPt8iEHTCNmuDOol1R3EfB8H-5C7WsnDFK22b7vYDh-cRftiDyyWUeaTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29785e012.mp4?token=L80KaQxKfRu6Y1XqAzFqasD3OMKUwgZTGq3E60RixVI0XARc1DdWpvzQyIroWtG0ORdpG9lD3fuJyO-WLl8pTJow8Fl1-x3JdgOdugf7GQJ-ZU6UEqoCUczqp3OzlaeXSvmcMKK5Dfs7PmWPth9Y5jbV6HOLfgJ0JIPOsWDwZ0BeM4it6P2DQ_3jr07Fg2AKanadFPLBUB-QDWvVpc6ij8FXaseyLgbijShJYz40fvS5yRRrjpG1K_o3T5o1rG5v7eJN7318U4pJ94-eQx4P-fBdiY6FnbPt8iEHTCNmuDOol1R3EfB8H-5C7WsnDFK22b7vYDh-cRftiDyyWUeaTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اثر یک انفجار در جنوب لبنان ۲ سرباز ارتش اسرائیل کشته و ۷ تن زخمی شدند،
ارتش اسرائیل دست به حملات توپخانه‌ای زد
و سپس دستور تخلیه فوری روستای المنصورن را صادر کرد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6501">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=iSyARvD6dPfbzpek-bFXv_M_DTXqkK-DP2RgnISJeED42kBjqSJTffRc6ZBJdqJVXKPx9rvkRgzNVAREEtr_kwW27aW8rYcb184FRoLFyBwTnN8nHT8WFuHx5rzZ8-HF8n9k-IsyTT2UEtBUCf0MUjETrrF0CWmxGvchAdEWZwWMtE8h7rPejcxYErZ7bC6pFkdMjD4qb40EbYOAKT16zrWo--vtVFiZoFDDHUjYzvZIR3RRQF4Do_JrUbkVq7vS9z92lTjmbYukbq02Mv25EsOmpVmEybabcEBF0n56h4Rx0UP-tneNkXemQlwyjWSCrd3nG0WAzZhE-E-e0l8row" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=iSyARvD6dPfbzpek-bFXv_M_DTXqkK-DP2RgnISJeED42kBjqSJTffRc6ZBJdqJVXKPx9rvkRgzNVAREEtr_kwW27aW8rYcb184FRoLFyBwTnN8nHT8WFuHx5rzZ8-HF8n9k-IsyTT2UEtBUCf0MUjETrrF0CWmxGvchAdEWZwWMtE8h7rPejcxYErZ7bC6pFkdMjD4qb40EbYOAKT16zrWo--vtVFiZoFDDHUjYzvZIR3RRQF4Do_JrUbkVq7vS9z92lTjmbYukbq02Mv25EsOmpVmEybabcEBF0n56h4Rx0UP-tneNkXemQlwyjWSCrd3nG0WAzZhE-E-e0l8row" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی منطقی بود!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6500">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=c0Pizj8nJ2YuTg1JD667Od1ATki204uDfLl3UO9qMD7w3jQwVEFEF-sUEYa-N-26uymYd0FiWmOkls_B9Ax9kHlO9B67zKfPIQ6PhiIsP5LUkrVZqcKBcDwUdQl6lZ38r6lm1N6lY0ZNYmPnuG9T1SllBSquPQ7c-HSoQOj08Wk0YLJiqsfbQ2WC__w0DMvnwMp84ohn8g1Ayb60O3m6ayI6AxPiWdDnfreShKsqDty3hGCloKjEatLnavSVyr3Vt7l1uOYBg8c4ylUfVGApfM9-JpI-9etXONcXuESdtZ2PvnTqLpMb3onVnjdzHwm0qBb4CY9zN0HSJpXEE62sdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=c0Pizj8nJ2YuTg1JD667Od1ATki204uDfLl3UO9qMD7w3jQwVEFEF-sUEYa-N-26uymYd0FiWmOkls_B9Ax9kHlO9B67zKfPIQ6PhiIsP5LUkrVZqcKBcDwUdQl6lZ38r6lm1N6lY0ZNYmPnuG9T1SllBSquPQ7c-HSoQOj08Wk0YLJiqsfbQ2WC__w0DMvnwMp84ohn8g1Ayb60O3m6ayI6AxPiWdDnfreShKsqDty3hGCloKjEatLnavSVyr3Vt7l1uOYBg8c4ylUfVGApfM9-JpI-9etXONcXuESdtZ2PvnTqLpMb3onVnjdzHwm0qBb4CY9zN0HSJpXEE62sdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xt_ATbu3kcncYWcUdZnggXW_hbuVjq4GXABY0wyDHCg2Zg28qEC3pBgsHz-Fex1wKjmCLccg3X-0HeXfxykOQbyLzBVKbyIga2kOVR1nv5zfC6FUtcmMrJdbxiGDtyAqaZGgxVnKI5oUs03iux9MGP_JXwCf-5suK1yhN1Fa4fX13eZBNtjuKCkiFox04JsjvxGzlXPKP8qJsHbnUdGNmklAZeb3g5fXvhWcxtN_LTTLUyq3Nmzye81QNV8qxryMrZskpAnYImqg7jaHOjm1J8AjWUXW4_4MbC8yvEdeb8eEe2OhUQzS2jaWSfc6Ekq2mQAZd55vD9IK6LGdvroKvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDxUlveU6TJ6P4iyh-IKN-sVxcSUAHThDnzfvEw5KCENh0mV9s37lrTTJaIFV3rKdlawj82ecbJxY9E1OglJEteKZGPDuzRg-QPNcWb8jLXj4NaNiXtEIkyPQ1pYk-43D6zBrscfx_wscrB9FsEiZekowHK0oc3L83tpdoHz7j_GS4GnCuaE5O0UMIgJ2b22o7lHy43saO9b3Ke90paPLGhv3vklM0sKGpDb5BvqCfWI-5PLkp6Yh2uQGlNLLc1jGcH1dlNmW2JsR6I4J4eOkW9nLG7uYHXrgPSzHbq6dZ7nY7zX2wgr5OQfUIv10PpYuzJUzKN-UCgRj0JPedKZqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsGBo1KfBPqNawBECnbcWVXmm5mpBqT1i1DW01MS-gbtyydTPyZBEMNIN9l6cEbaya6sIAwbSDzgRYcHcCQ0eFoWNiULXyvJlrpx1NGYChXhDaMspE4PAedxJMNWo6d-Uq-CqfE4m8ukNcCiWjl_X9qpLYd4TKGUOuc2_XvQpJBisdGRTVGWOmRpmQWUHTx1pXDhrbrnXCn4Wed00aVxsefTXC8vm9BBOM5eRE2JgJmhhb1n_smAioEqkixRb7QWybR042H1J8hBbkYagvb_eUJYvMbNDkJvkXOHszS3jslN_5qXNu0lVug5Wp6SZKsxevRSU4p_QSQluGhI0WKo7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.
عراق : از طریق خط لوله انتقال نفت به ترکیه
کویت : خط لوله به عراق و ترکیه و همچنین به عربستان
بحرین : از طریق خاک عربستان و‌دریای سرخ
عربستان : صادرات از طریق سواحلش در دریای سرخ
(همین الان هم ۷۰٪ صادرات عربستان از دریای سرخه)
امارات : دور زدن تنگه و صادرات از  خلیج عمان)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=sPgbdwHP_NuEDhqgOuFSU6OLcnuRPRMEH5q8MVlxJOCTHSAlJwgK0700ya--0L7uF2fC3OTopVvGEuvIzIFDtfnZq4x-OT7k6Qidh1n8ZwloHgje91r2KjxG0cGpTRrybVTVJnVpAE8RqfYUH9MA9RJ6grUqF_V0YGl04Vh8j-bORCK4Ek2jHlgmyfis457B4bPOj2oT_hFsUdL7rCGzo186VF1w3Q8eK8GGurqA_WctS-ZbUypGc2s6je728iIS7tigKipeUZqfRA0X1HuECvH1qIkofd8_XKofuqMqRfHnB3iP0XeXZIxje8sEwrs0t1iqS3mJL1-wJqp4bb1Vhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=sPgbdwHP_NuEDhqgOuFSU6OLcnuRPRMEH5q8MVlxJOCTHSAlJwgK0700ya--0L7uF2fC3OTopVvGEuvIzIFDtfnZq4x-OT7k6Qidh1n8ZwloHgje91r2KjxG0cGpTRrybVTVJnVpAE8RqfYUH9MA9RJ6grUqF_V0YGl04Vh8j-bORCK4Ek2jHlgmyfis457B4bPOj2oT_hFsUdL7rCGzo186VF1w3Q8eK8GGurqA_WctS-ZbUypGc2s6je728iIS7tigKipeUZqfRA0X1HuECvH1qIkofd8_XKofuqMqRfHnB3iP0XeXZIxje8sEwrs0t1iqS3mJL1-wJqp4bb1Vhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم. می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر
همه مردم برای ایران سختی‌ها را تحمل می‌کنند!
[تحمل نکنند هم یا زندان یا کشته میشن]
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.»
اونهایی که به قول خودش بین ۳ هزار نفر رو کشتن، نامرد و وطن فروش نیستن، کسانی که به کشتار و ظلم معترض هستند، نامردن!!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">جزئیات تازه از طرح تغییر رژیم ایران؛ قرار بود کردها «زیر پرچم شیروخورشید پیشروی کنند»
🔸
یک روزنامه‌نگار سرشناس اسرائیلی در گزارشی تازه نوشته که هدف حقیقی این کشور از جنگ ۴۰روزه با جمهوری اسلامی ایران، تغییر رژیم در تهران بود نه صرفاً نابودی برنامه هسته‌ای و موشکی‌اش.
🔸
نداو ایال مدعی است که ساقط کردن جمهوری اسلامی در حالی به‌عنوان هدف اصلی تعیین شده بود که نقشه راه حقیقی برای عملی کردن آن ترسیم نشده بود؛ تناسب این هدف با امکاناتی که اسرائیل در اختیار داشت به‌طور عمیق بررسی نشد، دولت بنیامین نتانیاهو هشدارهای ارتش این کشور در مورد مخاطرات این طرح را نادیده گرفت و به عواقب آن، مانند آسیب به جایگاه اسرائیل نزد آمریکا، فکر نکرده بود.
🔸
این روزنامه‌نگار در گزارشی که روز ۹ مرداد در مجلهٔ ضمیمه آخر هفتهٔ روزنامهٔ «یدیعوت آحرونوت» منتشر شد، جزئیاتی را از مباحثات کابینهٔ اسرائیل و اختلاف‌نظرها در میان مقامات ارشد سیاسی، اطلاعاتی و نظامی این کشور پیش و پس از جنگ‌های اخیر اسرائیل با ایران ارائه داده که خود آن را «اطلاعات تازه» خوانده است.
🔸
گزارش «رؤیاهای بزرگ؛ افشاگری‌های تازه دربارهٔ طرح تغییر رژیم ایران»، نتیجهٔ «یک تحقیق جامع» نداو ایال بر اساس گفت‌وگوهایش با ده منبع نظامی و سیاسی اسرائیل بوده است.
🔸
این روزنامه‌نگار مدعی است که تلاش او تصویری دقیق‌تر از پشت‌پرده‌ها در بالاترین سطوح امنیتی و سیاسی اسرائیل ترسیم می‌کند؛ فراتر از ادعاهای پیشین که دو روزنامهٔ «نیویورک‌تایمز» و «هاآرتص» در ماه‌های گذشته در خصوص تلاش دولت اسرائیل برای تغییر رژیم در ایران و جلب همکاری محمود احمدی‌نژاد، رئیس‌جمهور پیشین، به‌عنوان یک گزینهٔ رهبری منتشر کرده بودند و به‌شدت بحث‌برانگیز شد.
🔸
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از بین بردن برنامهٔ هسته‌ای و مهار توان موشکی ایران را هدف‌های اول و دوم جنگ ۴۰ روزه اعلام کرده بود.
🔸
نتانیاهو اما از آغاز کار پنهان نکرد که هدف سوم جنگ هم فراهم کردن شرایطی برای مردم ایران است که بتوانند کار حکومت جمهوری اسلامی را یکسره کرده و اسرائیل نیز از وجود چنین رژیمی که نابودی این کشور را عملاً دنبال کرده و با تشکیل گروه‌های نیابتی در محور موسوم به «مقاومت» در اطراف اسرائیل «حلقه آتش» به پا کرده، رهایی یابد.
🔸
نداو ایال گزارش خود را حول این ادعا نوشته که «تغییر رژیم ایران» هدف واقعی جنگ بود، نه یک خواسته فرعی یا شعاری تبلیغاتی.
🔸
به نوشتهٔ او، چنین هدفی قرار بود بر اختلاف‌نظرها دربارهٔ ماهیت نهایی جنگ با ایران در میان مقام‌های اسرائیلی نقطه پایان بگذارد، در حالی که برخی از مقامات و نهادها همچنان خواهان محدود کردن جنگ به اهداف مشخص و معین نظامی بودند.
🔸
نسخه کامل این گزارش را در
وب‌سایت رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=r2Stol9tonDwJjpLHeD4SHidD54kHfWkV70tPqvoz2k84om9FQ3otRw9uqcsBTudM_0zUFdO8nWRrpnbIUOUUD-00Srxy4-nwN2bhlzZAfZA1mzDqd3e_tUm0F0rauUlUtaPpdwfzoZR52JyoHfR1mE0iNN-IRhP7fvZa_IgvZ6F8jEhMbDEs6xaEb8WQ9RiSVNlK8NOt1q62kKFva8RSbgIJQwz5IxbtMJtyz1BrgrGOeNGWkqc6Gb4Y9J2ceSSRiiFx5UdTK2jFJXPpb0mHX2HtmicjCZZg8UdJKKXGs8LSgXswOnTOHrjm0laW3BhjkEkEMFMxrm42oJ_YRYgdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=r2Stol9tonDwJjpLHeD4SHidD54kHfWkV70tPqvoz2k84om9FQ3otRw9uqcsBTudM_0zUFdO8nWRrpnbIUOUUD-00Srxy4-nwN2bhlzZAfZA1mzDqd3e_tUm0F0rauUlUtaPpdwfzoZR52JyoHfR1mE0iNN-IRhP7fvZa_IgvZ6F8jEhMbDEs6xaEb8WQ9RiSVNlK8NOt1q62kKFva8RSbgIJQwz5IxbtMJtyz1BrgrGOeNGWkqc6Gb4Y9J2ceSSRiiFx5UdTK2jFJXPpb0mHX2HtmicjCZZg8UdJKKXGs8LSgXswOnTOHrjm0laW3BhjkEkEMFMxrm42oJ_YRYgdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=lKlvkSSVM-1C6Svna6Okxt8vNNBB1nuDM6D4pITvMAq1OQD6GPx9lgs-rXRz46Sc67zMqAUJULyDLuEVQt73eSHxnI1lK3snc3vlxVduJ6hnNqoP8IOSThrdca_RNxG_FZNWFyxJsrpLMItmIaIrtSUpyao8UFTVSXgCjNFhtLgYKZ1CeUXLWfXQ6b-FQjJbkPgefrYpI8t6zlPj6XOEHDbg0uqJHTp-jWrXR3OskTJwKdKEzHmqKIupG4uiMNm4b0xwdqW7ywHEsEacLN6rogYoJi2DA42zCuF52dI_y3HKcGfAMg9y6HGIT8dW60x-kZ1qcD6wEt32asnLmDVorQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=lKlvkSSVM-1C6Svna6Okxt8vNNBB1nuDM6D4pITvMAq1OQD6GPx9lgs-rXRz46Sc67zMqAUJULyDLuEVQt73eSHxnI1lK3snc3vlxVduJ6hnNqoP8IOSThrdca_RNxG_FZNWFyxJsrpLMItmIaIrtSUpyao8UFTVSXgCjNFhtLgYKZ1CeUXLWfXQ6b-FQjJbkPgefrYpI8t6zlPj6XOEHDbg0uqJHTp-jWrXR3OskTJwKdKEzHmqKIupG4uiMNm4b0xwdqW7ywHEsEacLN6rogYoJi2DA42zCuF52dI_y3HKcGfAMg9y6HGIT8dW60x-kZ1qcD6wEt32asnLmDVorQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تبعیت از ولی‌فقیه بر مسئولان واجب است»
می‌دو‌نید شمر تا آخر عمرش
از اینکه در کربلا شرکت کرده بود
هیچ گونه پشیمانی نداشت!
شمر خودش از فرماندهان ارشد امام علی بود!
توی روایات اسلامی هم هست که
هر بار بحثی پیش می‌اومد دفاع می‌کرد از کارش! میگفت  تبعیت از حاکم اسلامی بر من واجبه !</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=I3FH13eOeNkh9VQhqKlM8dCETF5stwsVZT52ElSNnmGo9NFCfHCbV5dXfde0qTL8-zYj-o8NQJa19nulld3DLICw4Nlo_1tX8OP744-auHzad7CqDi5PK6f9ZdqolhkWuiG89ryYYKzoSwEzb7m3msk0TzXR7IVOBSt5Bnorc28tPlqQ-8vECedXRwhfqO8d9NYbhi9kGvSOMAEdGJ7ETvh24g-woXSAohrntANDnw-KKL5O0rNuQP9KeItkKKNewjJR02PKc9SOUfFg0THA-QPbxnRq0zGUDP1nYO-5EWBkZpGMOIyRye9oygY1RhsswcxDkqx3lr8XzD4DZ9He1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=I3FH13eOeNkh9VQhqKlM8dCETF5stwsVZT52ElSNnmGo9NFCfHCbV5dXfde0qTL8-zYj-o8NQJa19nulld3DLICw4Nlo_1tX8OP744-auHzad7CqDi5PK6f9ZdqolhkWuiG89ryYYKzoSwEzb7m3msk0TzXR7IVOBSt5Bnorc28tPlqQ-8vECedXRwhfqO8d9NYbhi9kGvSOMAEdGJ7ETvh24g-woXSAohrntANDnw-KKL5O0rNuQP9KeItkKKNewjJR02PKc9SOUfFg0THA-QPbxnRq0zGUDP1nYO-5EWBkZpGMOIyRye9oygY1RhsswcxDkqx3lr8XzD4DZ9He1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPe961cXVYINLT4Aztdw8z3hkgJzmJeUxw1TKbPOqzkMuL3JnizSOdBZgg2kcsc7m1x2cBx2vtJ8P0J0xxngqSkUp5UpQeEW2E5inSS3G8OXbysiXNxtE-m6zgLZgrvljT6I6i3KaawQSTwe3AQ6dF_cxLWJYCT5Wl7LZ_e5yYolnVxmRXKAZ3Qmg_0xhYM2r6OqJC_uEswlPPdxx6e29EqsnQRo7RP1CWZ5thM-rHPg0Bf9WClY5lWQK_5QZ6fZ87Ci_dfvr1IRoXmDU7UKhqPCChvBiyICIHa30TrVmV_UToap1yENkMPGTOQ3zWZKA3lh5gPHNkQMnXDMCtJ2XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_qfOJbr_oYSPQM7JdFngHAb6N9JnVSLgHo_K8fMFncoCFxFOhejfFrttODVnyilBsYXGgRjiRHTqSVD5OS8q9XO2okIRxucRBycLkeMa0kTUc6E-CUnVbs_2GeUabLIir1soQJeaBCvYBbbVegW8qbsGeNL0zp2kXiFsDNSAeyAtQYxFh-FxiENqBgousBfI0Oi2mDY2-_T0YSYvWWt5PJPl7irQvEydhnUPJqRP0ssHgy6nW31gxqLIk66_ylRMLWPsrx-ULWl51stR6OabtTt7_P_3A06DXEvoLWQJZvnIWw0G1eqvxjsYczN7VG0tDzZKsqYsApLTCduZQ_4EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ig5CVlbFy1YwRFDnYZmg92q19q2wQ4lBrI0ZktyUHkhMDDfLi_RNSe7aizH6bwU-t6xdKN4-QIbqBgWzipx_nvcvRrRFEcNq1SvdQZ9lwAi6oJuGY-M7ZidJM9rx2dwOaDOM_zjj98AUxrUUBx6IMqrCVJOu3wnUtE6sAW_ulfdWcVqm0iU5RL_qzgx1Z3fcaE04S2CMA-ZzNsRU0d2thlt2zuSzGxHx4RGu3eBlfAs9xRIEqXgAQNEzo4bOGDqirTEkiU2Bp3iJzafmbY1KMxlGU4gacFNlLlnef3iq21LtIRs5N1rpwAmdgjiFtlmPvZiCW-bWu8Hr2iJv9SrbxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G65yCW4BPrba_4-2spfje9kMiaW4pGYDHMGVMj2yHkuv72LLKW7CxikxFT0nfhB7WTcXLDq_AM6Pk5t6y8Xf_EyePnqWOjlZv8lgBqq32iYEmu1iibIfV6F2waAaGQiXwKIrPyLczz69Fps0pSYx2Hr0ZTnFL0U1JmundWjjq_RonHmtF9q7CstdyOZBaoDmhEz0qODjEGFSbrFFeqIcI1jXLP74U5qWf-NhfgQWlESRx2ZiNHaQ_DHUsB9kU7R1QJpxqpxtOFGb2QSoqeWoVJX_YHU6flNa_tRWQiAEEhEfHoMV_d5fIpSXg4J61bvw9G1HEV5N-bpK2wk4tYQcVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7OWtx8w0J4gSdZdH5EirmMJ92EqNL35S1lriQs6DfSBQcvcBALk1it68hT7eqzO3NA8mo6HBWw9FS6I0WY-fez9eEmLp0vHS8f6Ddsf6-67fqfcFy0UQenGk9KgFyNlbXV0lReHw5oImLKk_psoXtg77KJqe5n9GcjgHBIWiXgTvrySvdrxnCQr9LVsYpSn9mju4cwyEK_3CaGZpIrWljC1Ba7yBZ7EoSm7FMD03zGQW0oVgncaKUX7T3zGhcbP62coQaq3LlfzX-Btu9j9BFhK85PhzX1GGVSTq8eC7VMIFEOcmzbcuPxOF66HVfg_eerkxVGMGsJZSSHAHCeK6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAk4KEZILqTsphgyNnL7ju4rqkXYQjjBDQHt5F-EaBBDbWJUatjn13hoGul6PY_d745ulv9Yf9qAy47HAxQUnhwbvJYMKF3eJIgiTfOudsfNmvsSP2zWUO8Uixa-Zg_24KVoP9hIK4Tku5atvBNb9KNVBwRSY8ggQLWa6ZbZHA6hiqnVqeU3QBRZfAZEmYs5zfo59PG-KR2LwXL-vpZWZTdIfueoRrTAPkD4vsYTkq6rIRCDfHuNtNGSIc4yIkuzVK2K7cVUDVRCKjfDtB_M0pD9zlIUBc-8WB__KOIxI6E3PA23lP8LcSlh653rbmwGYZgDFJXuG2ATPB8Qr3NzOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PikWYbew8IuvJBoNl4-mHDHaIzjE4BZ6F77bI-MdTQyInzAfleghHIMGAJrQDdvjq2ituda49k3FTv0ZRzhi6P-nJ-v0aCnBKfBMQp7Ur6Kn1wdd4Zhu0X7d0pVGSqh35-2BdZrbTJLDQYCCDUbsOvb09SdlSeUGfMhF8ubqdUVcWmb_5WRxryDW1NW0B-SlYdn3lTtcwhQs-WNf7C7Ut6aJSYnNXsBjqgipg0N78g6MQT_3M3xqSHvTqTjny_fx8V022oUbrO13zlH4T8-A3u9jVoGO3nuE-3J1YZD5NoJFG37-rXrimHeGU6O5I_7DkxR0npr375af_-HOChxgFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g09vQ0ceAegszjjGyYmP_4Ea8xrG-KapEbaOfhyFFMJvmMiI3BiApSRV0jW33I_rn_N2V2UnI3dM7Qt7eIQO359zfpNpM5XfLGxaRk9bijZ0GI1_gmZmesKGZx0gKk5OWbZ8aTbnO-ZFxVyT0a_Q7Ikgu1YObLPHrsJpvXzVfHN-cdd9VKOMOQCzgNdhTwnICzh3T9U2Y9sNp-uK2N8_ArGry4JL_5YVV9ELOjlMTXRIF63NQwOTAVARO4SePWkdcUdTqfMfJt-lnyZpL4laqVIZ--oxgmrDnl7tqyB1VsEcBTowCU30HBL-kqxth5-q9M2llSoIckwbH9AFefNDAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDMmQFxsQPZjoLmUTYw2eG2mIKNVbY1zSO-VHNh-jPmf6nauccOXnFQex3ub4lHyO2piwx1FU3vG-tOf_2aREE8kpwY1px7EAJWpcLdHUzh65eeLEo0UptyHO7OngSwKAMNqfwuEprx2qY9wrsmN5OMhkaeEgWrdMJWBcG8k23PzQidFFwfIksZrmwPCqoU2Bw0hq-EevI7p2UysEyxqQ4JFZBfLsY12CEdehEA_ZhxcdpuIwZXG89iXW3HOQ7yrL_Zhut9HLPQTNDqXUshuGiCrQOkbLcl-18eFipMZ_PVoQgVKQ6-RYXrdRZVaUKmDUwrCMkBMVJFfSKMs6Oq_dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرعون، جسد نخست زاده خود
را در دست دارد، زن فرعون گریه می‌کند
و موسی و هارون،
در گوشه‌ای از تصویر دیده می‌شوند.
برای مجازات فرعون، پسر او،
و نخست زادگان «همه مصری‌ها»،
«حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس
که در زندان بود.» همگی کشته شدند!
حتی! حتی نخست زادگان گاو و گوسفندهای مردم مصر!
و این تصمیم و اراده خدا بود!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4BMQUUbSsdsjcC57Eef_XVbeFSLK-JcIHE5fTr90UGEriSnzLU8FXZFon8evpYUX6fm3L0WzYs1Dq4km6dfSoH5Wub9-vX2wt0VuvXewSmRXTIPcA2lvLMbYkm9INqMwWPWw_vtczxNe9K2CjZprqsWPyCkN-NzdgHFckOYJ08qW8xnOsraiA6SYQ1Sk2byp0NyGfn7LLE4tYH8Dh2Cblu4zJpx_be_F7Qn5hQKHOcXo21xpgF68kfUeTzb7sXHxPkiBfX-ppXll5oBt2yPc_f8FDkcpge1OkS1DiKovPK07mEDaBq8Pkr00rFVNh8sAz3fW_9Q019IInEEjdSLsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iN_fkbHK4GlJW1t3YJ1cXI7Lix29r3gn7YSWMEEnfAC5OxfTTroQEBRWOkyHaSiDYQT2i8zpdYJX5re0lZmIRCu__BFJ12h1YtjD9YqcQp9-WA4kBH1ebGcITVFslun58oGJv2xZD_fM7Hi5ETomAfFXqSxEXyC4SE_CDszN3xzSpEfza_y93VDFNl08iwKtaUovn_0woAtbDWyyFEWGGZxZHFsK5lo6UDg7Hu1eKRVuS5qqaoj3H1VFtqOttV6HuG8sBBdkMOPhg4p5a2gQpFjxz3jFkMf0WKQQfa0a8ScZZhlY48n0PejtstsqcQs1QR-fRnBAhbsekCRITfhhrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8Qpyy3yIQGSC1rrBJHaubjcp01PGFlU9cviN1BLEVx2oha4T2_n1qs5vIADxM-YREax4lgKDq6YMbqC_vOjp1Y-WmFye8uR8CotUnTcQF0cqzvVyAr5vXsiCnuyTLvYPiB9iYBwLfi2Q9EzOkMGD3I5ICSTVrBsCxnYi7WvR2KoImG42ET1hk6iSiMUWNz5HD-cXe_WhQr-lvF5qhZi9EnZHB0_DvppBAWbbkBV0JfRD2ukXDsHOTXOuA64m5g2pgB7J-3qkNpq1mTiTvZi44p9X9Ooef44DOP0BPPtlHy3rj3XojfL3HHR8EoJQeiBNX9ag4di-GjK8B5yYKIn5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0qDKMA3K4hpRlawT9sT1c7zDrEts66gZi2GkHEEp4Am_NGwcCr9aLwIE0MmtXzlbMAeAF6fBYdItwAULTo3HAUd87zSyM9VT8w4_AewgJcqv5mMQr9vNiVG066LVXzHvxMVylp9_gf1_ERtieG-MEnm1zbjhAvx2T82MOUpAPMyYZV42cDNDTib4vVY6ltxxk6zAfWxFq-Nf_Z0B4_jF2mf-fEGwDmJGyWHG3Cw00aCDtAfLq04J5V0cSJiRsVZP5UHds-qNuSdtpxP_i2n3Nt0aBGibOBiEqE6jeDSVC8kwUwfSqZJO3CYeZQKwKb-r0t18qRK7cKmzsdVavZv8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -
سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!
تباه در تباه!
خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».
احمد شاملو - غلامحسین ساعدی - اسماعیل خوئی - منوچهر هزارخانی - هوشنگ گلشیری - باقر پرهام - محمد علی سپانلو
اینها روشنفکران ما بودن،
جامعه آرمانی اینها، ترکیب کمونیسم و اسلامگرایی بود!
از مسببان انقلاب تباه ۵۷.
از مسببان گمراهی یک نسل از ایرانیان،
از‌مسببان  تنبیه نسل‌هایی از ایرانیان که هنوز  به دنیا نیامده بودند!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEkqIVC0T8S9zWBGMUpGL2O1ehgb-ym9qHejrfwMN8cBa9fQ6LtyOtwRWVEqqgU1ajf_xuejz0MkZUxm3VwRwHjEUgVLlZ_vQ-s9_f2nK88lMrbC-LF6DzD3Ae9u5CakwBp8mLT3VESLlFmSh3ZiHnOWXLdOUASeJFy-8IoASdHYpzcE3trgZXZoCVDFcjM6WQ69NcRE4sdqKZB2-gQqyXFCy3DUMFAzqJwQfNF2PbXD0J09gSVZ29hLJZwugVDp0Sm7F6hsmiBlez1J-h8aH2IFZUyjP8VZSbpKhY-uX-d95hT-5xVDFZhPOf0VgMHYC5-LsnxAO2RFpiXFglBIVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=oYrB44PAf1YkNAudtBlCM8aDA9UxpGm11Lo0--j5ZrjOhwM-n9uYo0PQUg97K_FVnuJS0-2DcCEg2mswj1x_HgZme57hlRScYhTPblNHWfUDwibhlFDgE3cz79EVR_U9KfJR_8mszon_G9kzUqxScLcQGleZ6x6YUaMlqrP8qNb5PFxc8HSYKhiy8uw3YIlHjNkNG7P1Ph4dJOV_HRXxEAS-e7nmtPHDNpVOJ5duvG3uW-F6csNxrMCoqK7lRFnCzdmZI3cyKR-K-6_dySopuvXL1WFy4ft5YufA_pY98zToF75t5YN6ZbDz5xNtfsTEJwAubZ60Mbrr7YRTq9JnQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=oYrB44PAf1YkNAudtBlCM8aDA9UxpGm11Lo0--j5ZrjOhwM-n9uYo0PQUg97K_FVnuJS0-2DcCEg2mswj1x_HgZme57hlRScYhTPblNHWfUDwibhlFDgE3cz79EVR_U9KfJR_8mszon_G9kzUqxScLcQGleZ6x6YUaMlqrP8qNb5PFxc8HSYKhiy8uw3YIlHjNkNG7P1Ph4dJOV_HRXxEAS-e7nmtPHDNpVOJ5duvG3uW-F6csNxrMCoqK7lRFnCzdmZI3cyKR-K-6_dySopuvXL1WFy4ft5YufA_pY98zToF75t5YN6ZbDz5xNtfsTEJwAubZ60Mbrr7YRTq9JnQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tj-5PHCnmAZCzMWV5lB39R6jz-h99niD5DtKY4hma-lzrMAjVa-KIHAfNEQlXOosTR5JHY_4j531MXY8MswaOr1AFM7bloczjTZBrcl2Uf-qc1P2LFjqpnj8aaXdy5-X_WTVf3VZ4IwclGVarjsadhiJt8Yt7D6WCfB3gatORUFgnAUu5Vk68sg0DTsKp41DnnmqV29QpFWcyrkTrlZfNR5Jb0doPggaE5uKM55jd0nDURU_st3PTJk9hpNzLNss_w3iy3dUEJNvOvX1AbVhZm4YlXe6R_R5b381YChgIZwmSb0km5Q5SYMsTWH9yyg8wMalUKa3oULqBPjAJUDpnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUKthHLjlHBjDsOwywLbi4RLwAm5FvXDuWtSBdT86wQSmGvY41i1WCPEeCoCv2PVOTZqBo8t0tiQT6PzoL6TGLPnwz2FZWvQn7sUYCEVGR-5Vp26a3A5TnXgXGjv8_RqIkTbA4s5i3vK5nJSV-grXjxVhiP6lFu6BYIC_tEcBFzj8nvggWxBOTACqjWcSu-QDsMVw0YInuGdbo_UUrYgijajzWLI1SoZJDB94fFTM3cT74ex_4CHUeOw0HTfAEJMKFSGqEYTjaqdpr9CHPTQJZ5SmJc18xBcOPw-8u628xGxTxEwS-3Fr-5Ol15UcbHkD6xNY1oEcWYH_P_tUYZOwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnTQWlIS24yjq7ks4Gx93NZE3yIYi6H4ndWR8CslWFjZB6-iNabAkzVKq13ZQSivXXVfn78-iZxY0BcETY7pG3Uv2OnGDZlddDWkt0Iq5KXOa_aTIrYQXs8qP7TqsqWaX30zyxwwRtBguLaI67zSTxbr91lFofJy-otUgp-IevbA_l8p7xajiBfL4zBzK-EuS7glQ888mcE88AleXWwOU234V_SCwj5p51cGOc5F1miD5mwpeJoQCg30jpy8h7OCKtAjEPOESRLRUyo_Qd_mYq1AN-Zwh5ZeGy5DSU0RPZiOAUWAU6R6g4X4IuGfKzlG93GzHo-pIqEBfBi5SRwkyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7ZygmVFEoavBu1J_7ChgRhgOXlastby5nGM1TG0GRFMV35qjeI9yIcLt1FazMMRbRiVkdAusyxXp2MF3Qlrd-ggKzZyze3i_nABpbshiUQUhaOGHm98EzG8DeTD59yLWQJbMQULng1_1Czxe3ny-crYS3zREu4ACRtiimzBOAM5T42QzAEooJ5Wn-sgrqlORsvV15mKs-O8-dsNy2wRib2mjY7SHJWpeoRvBfB1HxIsNttLExyauPWd-ifgeZ4OSzBSspW9g0ibdzgMMmNXLJHTdporSASFUJtdGkHIQX8l7k3F28e05fzHIPCjlVXoWwmYGK9Ki7K0XVUkw7HsWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3JYEdseoK47Oci8s67Nwp4wGWOCFXJESmMicsPX7iwEOYVLl14Z-atM1CF-PXjdJBKkSx-cH9MZm7L3E6x3qWFiUo_3B3d9NC_OkwKvPTmPahbI3UdvV43RO2bCiQ9qsp-CI7v6ITUhPk7y2sPZOIcPU2aaPajkUTsvUOUPSHLxaYDCNeh1VDOxMow2K8qVtZ9A0gkgcSFLqNdKLViRk3cHihJ8D3iChsl2EQl4nCBWPtAENFMmxdKkhV8L7TFuAt6zf5I2GrJM9NW01VhZh5l_Gt_OwP3NuZhNNIf8j-tyNc8bIyS-_UHPGufoRaobAX23EFzmHPZ7AajCjylnPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S59wXDygpgAYQC8uUnbZKaG6f2lrDhF0qkk3THAAjCcWgCq1Iz8Doq2anY_rV3adOqOHJhD5kyyVr8JskCROqzr8LOHnQpiuBrzRxxW6BCJs024HZof3yzvnjaCf_QVT-vby_4mxh1rOxxg8GSqozzXS-Y3NK-dn1to_xQiL0Y2KkxdFe7Kq1Nsj4dJZWc_IwW3Hjmu_wHGiLM3PO4K_0ciRyYzMuYtZ5PGq0DsKyVjTIArLIItjLTKY5opY75C3zv05_13NB3IliWz187deeUAw2TcOlPyIYPeb8cNrJuImbU5JfJp2frwEm6BX1TuLc6CJ-txz1Io63SB5HTC06A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSiZ7BN9CLgYOgFBTp29KA791Fgy0DoPZ8nyG0BF6KdtsUmhIbTJAQ2pVbQBmeeDXgM4nHeFhQvHQERqOc8EdGnuzPRIhupLN_4Hmy8D38IkQinQc2RgvYvEV2_v843kW07BNLAw_NfzB8fhkUsQLxrtIxaKKewFrbA4t0Nqzc6XdP3TR0Zw2muvLz7k4ZHcaW3blmh9SEf7Rx1hRVtqXco2-3eu465Ure_durpo6zZuyMZ1BTDxUX0yhAKAvHUOdQF4-vAxFzHQ81ADaAbA9yvggnCwsn6YN33sRzO2GMrwj2Ow82oRa7me55ZHE59lwO5xyre3TFvARxKFguwphA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8f_U2XiTQVFUgX-Tn2WKNlGVjBVvq16WVawgj2EL7C59ozJu4rcwT8samk2herEevCMv02zO-yoFiwoJze_Oqu2G9BGNP9sSgEwvpNa-bxSmNp77qO2naGRwejOl7nsnslEimzItwbXUUYB9k5I1chcdA_SjkuOPAP-YyrJ2XHk4If4jLEUw7XLBtD85ZtkfY2KeTOfJZj1H3r3R3GZcdpYlGGxppknMz4_KqDmpeNdx-NN-XEPt6FXcPT5g3GKRKOw7JeBvU_cKaf-rMOXNbgggdZCoPP7pjY_yDaGmWLopwybjD0YHuZctj0ANLFswBi9svLFl-jRq_V9BdKomA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دولت ایتالیا آزادی رفت و آمد هوایی و دریایی
بین ایتالیا و اسپانیا رو به طور موقت لغو کرد!
این بدین معناست که تا اطلاع ثانوی،
پروازهایی که از اسپانیا به مقصد ایتالیا است،
دولت ایتالیا مسافران آن را کنترل خواهد کرد.
اقدام دولت راستگرای خانم ملونی،
فشار بر دولت چپگرای اسپانیا را افزایش می‌دهد.
دولت پدرو سانچز هم اکنون نیز دارای کمترین حمایت شده و پیش‌بینی‌ها حکایت از آن دارند که در انتخابات سال آینده از قدرت کنار خواهد رفت
گرچه برخی از راستگرایان امیدوارند با انجام انتخابات زودهنگام، انتقال قدرت سریعتر انجام شود.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=pGnUjQS5WD9Pmk-KW68G992hXt4Z2ea29U2RKvao_fF4V5lSME7ddsGsjqbIAAmt4oeXnpddtwdpayosyYUxgkdInGJqbLUXMKjZmzAQpuou_zvL6CZjy0s7J3_KJf6BYfzTknQD_9_p9v9ByEOb_-oKaQb1Q9NLJ5hCng8jikzGOB9KSny0UZ1U4CVhzskmWBL2NHFNynz_387HwRp1vQs5sEkayM-k5XlIh3s57BfyGZq363ESrDwvTZJvDMWXtjUKg2HnPwpBneDy7L6EeHI74IpmGmVCIOQ4nf05Fbkewyoub3NnQ1YqyM0RnxDyFRUa1oQ7eMN57XypjJi8KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=pGnUjQS5WD9Pmk-KW68G992hXt4Z2ea29U2RKvao_fF4V5lSME7ddsGsjqbIAAmt4oeXnpddtwdpayosyYUxgkdInGJqbLUXMKjZmzAQpuou_zvL6CZjy0s7J3_KJf6BYfzTknQD_9_p9v9ByEOb_-oKaQb1Q9NLJ5hCng8jikzGOB9KSny0UZ1U4CVhzskmWBL2NHFNynz_387HwRp1vQs5sEkayM-k5XlIh3s57BfyGZq363ESrDwvTZJvDMWXtjUKg2HnPwpBneDy7L6EeHI74IpmGmVCIOQ4nf05Fbkewyoub3NnQ1YqyM0RnxDyFRUa1oQ7eMN57XypjJi8KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFyWnqLAgXUS6qd9gzyNQUHXcOG1s9vfkqY_n13rUpm3VZIMvlLOXPVtpLOTlrNMGgUMYJI8JotfT0KtVc-G1NFBKJTxO6UtEgPD_rRJAGYnldPrwMGblljM7ZzbllAxrdtncKG8P8VF6wfnHzSn8KkZE16BKNo81DWjNTM5RgXScE_G_TlcoAktWgYiw8Uv5RzuHcJ3ZxhxvQXE_qyIMIqRgiHESL_IGCFctamLZEovPKG0t6Sji7hihcbbgaD6lV_rYoKKxejAnn5hLwcwZ81vwPEqPJcu2pUlWI60dcGqqHRbXnhozgy7c173NjLP5MAE9RtPVPa47RKC_erWJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQD24WFZyxu5Jf8WuTHy1yyy7AY_w5nBehm8LEjPsgfgXefiop47enHBOxngvobrZv11iES7jUqmCizN2xzyoQ_sS6kzrAK34KRiADV0_nRsqhppTLjk1s6x01ujTRdEjWOq0P5lpR8m1L6Nw1K2P5cuhORqmWsWig4CMLpVr5Jny9kNZT1E7BxiHTLSgkpN3_TrqiH6yqLjJYXWxSU9Jw4NvP4XrxIqRecwvB8wT9nJR_CYuSqG0GeEoNul5VBer6hGO438FSbIofWua0-hwvkqAyfaUAzfreUiwWpe04tTjxxLz4xpWr8ZXnM_RIB1eG7MOvjKGCcz5Rz4FR3Z_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSraK4Egvirp7lA5pBJIYRVJAgV7BL6Btcwp7ltjDP0HjsAqCqfRiq36U5TNwRE9McSxbX6U6ruYUeFbamm6TQ4iv0-5M7_bnd2fHR1VRxZqXCkB6KxGeNcSIHvyiHkDJp-v0Mkai-OpjmWykt22GdAQ5FnDHgg8ebJONlROUAzqUfFY7la9p47H9FrGkfZ61Wqy1Ari2V-cHHmJWNIvy5jorbFwU6iU6Lq8UQE7aV6a2i5wEKW2HOcJht4cb_sFg_E8L0c65GoHMqql0A98eKUp7PBvnJ_IEE2JuZZW8V34O-9S4OEduf0ARR90veA-56Obn40ych3hHuQr7Cl9FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5E1UjqRem9zZOv7vbdIkzr5-gPQxY_IkSsxuQt1MMvnQLwhvDNBktgU77u1YP0CHO-Ex4HsDdJ4Q44GKiXD4a7VXvn0X5whMbMnLF0gpsezdy2kViAYSuvbs5jwX0vS-Y1nFPIQNdrpqlAqvyTMK1tHGOffxwLFbIhSasZtQa7BzGJgpvxmvaSXUfUy775Y0aiIPbBkj6e6aKPcQ68v1ArNR-znrTqStMn0a7QoJHd3KgCHI0HT1rNS5rcto9GV0fX0qOdxQbBOK_uAHjCPj3p61xZs7dp7dxp9hhmpOlChqWm97jNStlp-Oh3XBENX6M7NOaCNIIQ0rJclsrlATA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUH_xSgzsdgw2XM6dtOeygRYpoQLAisHwbrlWsQcYCt4JrePPNRfZQk05kP8wR92oAusJSWFFAUBlgp2NJw_m2WzzVRS0oWGPkSNbblsWX0Q31OpxKZzWtrG9tvNwIkcjUUSaSQh2oDXMdTYQ8z8yHXsg34KVDSGHuokV0cUZhU5PaFWBFgl4F17E-t1ooxpDyG4vPIWr87l5RWBf0hputQGEQSNCViCEY0oVyqKnzcRoGG--j_-0dT34hWkQirwSZZg_Z-xc9hqX5F0lHSsM9EtqCGxhDTAfaYng2e7EF4S-B3iV--816kMrHznW3PAXAiM5o7VYT1sZty2qfqeUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3_f7tiT54NlQmcKCd8gIhySF8dT8AnRLI5ZC_re3B8yz7ICtnt4mIB031JGo2TLrpYz76vdDvoO126TcrK-CRu4geff_UzNCBttRuVz407ZA5pxJTrA6INc11SLEffYcqRuFVW8z1bkq6miLS3y1wmaVHMmclUq9TUtRdY26kNMlJybrbCCPx3qgVbYeBps1vG4tvclRvcF8HZwew6UhqI_Nv2zUbJ_jm_1HasZc9GUp__Fpiky7S9-cXYZ0NKYQ_dUqvzKGuERlkhVock2LjSUMoATlH5Kcc2vDcodaEqjcYqbBwFpfDarixkH6jaGVJHeCCvCKCImvn7ZdoBRGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVhCvOnaHkaz11GiLlFEMPbXFsCH9kKs-7wgvNamfdceZYghQMzYK6BgB3v_ZcV2mdRAGupR48yFqjUL4SqGRcLqE__ldm7qIMm28T5nqiFy1WVVE4nSdiSKtcmXNTkY3vA0KwM6WdtgzBG--dB6H9LtoyJUz5464xgXYT4ZkM8q3k7f3dNROmFAd6Hn0ymU44BkYIiO-UzcJ1u0pJe5eYjKLANDAB7rJwEynxPesFBnbtheT2rbu3Je3DgH2jhUHot6hGCJ979VXjHJM_75KItdOTQFyxKg-0L-DRr6L6FQv_hn24kMGy2b9eekzIPmgc-wBbF7fT82Vjc-xZR-pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=KnnepBzn5a6CQ5zQDp3xOw5ArI1kK-BPkgeMAN__w1HqW4K_Md3L0ZzOpeyKvs0KG7AAK5tgZx1wl8iw6k3PtjWYD2FJB1gSr0ATkJPWGTwgC4Kcz0ltHu0hfvlXZlRziw1pFXJZmsbcCPuj_Gnc0B6DUkJb8AUk9otOOX6dgh-AlwqoBcbuf3HE9DFPkQ5xbURA-oesNnuDMRFIE9TdO1gaIb0UOU3LwgC_XgBzaI2MjcJGW-GBcnyM7XOa5DMGRMFLam6RHiBl6kEDW9qcPR331MnNn_AT5DACletYoS8gsfXQwPjiWT4brdNphTv3OESVLw__G9nCtTMkcujphEmTERgs7NnAbGcnEsswIOCMWQvJE51fhr2NIxx0MUhnIm1YIT1tRoX44g1glACbDSgQfEollyBUZswUCRBhJZsOWk3MgNuMHpF_HtqZ9Zf-y0LMh6RlgMx-xRaVPQrz_Hjn4sAMXkUPa8fxDNB9wl3SJNeteFeQ198XpprEqonSgKvT0I32-Wu8tUMC5qoPp0bNmQr1hYypw2N4_0oKGwvFu4cDdgS8fXEsU1JPZaP1wDgVYUMPzfgrexeTWeBtixkCPP4qRgD_R73aZKadeQ_kZIGc2DCz6Nd00RBMY_1fylNL5Qlmwjz4YphdubW4iehAQm9kl7GmdrOUf9aBUJ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=KnnepBzn5a6CQ5zQDp3xOw5ArI1kK-BPkgeMAN__w1HqW4K_Md3L0ZzOpeyKvs0KG7AAK5tgZx1wl8iw6k3PtjWYD2FJB1gSr0ATkJPWGTwgC4Kcz0ltHu0hfvlXZlRziw1pFXJZmsbcCPuj_Gnc0B6DUkJb8AUk9otOOX6dgh-AlwqoBcbuf3HE9DFPkQ5xbURA-oesNnuDMRFIE9TdO1gaIb0UOU3LwgC_XgBzaI2MjcJGW-GBcnyM7XOa5DMGRMFLam6RHiBl6kEDW9qcPR331MnNn_AT5DACletYoS8gsfXQwPjiWT4brdNphTv3OESVLw__G9nCtTMkcujphEmTERgs7NnAbGcnEsswIOCMWQvJE51fhr2NIxx0MUhnIm1YIT1tRoX44g1glACbDSgQfEollyBUZswUCRBhJZsOWk3MgNuMHpF_HtqZ9Zf-y0LMh6RlgMx-xRaVPQrz_Hjn4sAMXkUPa8fxDNB9wl3SJNeteFeQ198XpprEqonSgKvT0I32-Wu8tUMC5qoPp0bNmQr1hYypw2N4_0oKGwvFu4cDdgS8fXEsU1JPZaP1wDgVYUMPzfgrexeTWeBtixkCPP4qRgD_R73aZKadeQ_kZIGc2DCz6Nd00RBMY_1fylNL5Qlmwjz4YphdubW4iehAQm9kl7GmdrOUf9aBUJ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=CAH1-KTu6Xf0yloHEPrQF6dWAdHy2bRhzdUGqYk0NBFhFyhmjqNRfvuqVlFI9eRNzHEd53zHg0fvOI8EUHrXON2vpVRTVOcJEdWqq41s5tFq07CcgEdizPxrDQrJaLozaRuhH6kIXJ8kT-qfLNrOpowOYmbpJdpUScXFrqx2sOndZQHs7P3gxrRTVDrLXWJlIqkH8nSjvVNiYudnEN6Bc_m1SzO2cBIGfSLIweTm4LJbq_sbmj7DYRF-Sfxmt_ul_vt7Pl6Eulm8P0cxj05FUuCdjtp78p8oCA2kjy8g9-HKevfn5H9CAz4G4uBUFtFKU4uXfBT9tfgciWz90XATuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=CAH1-KTu6Xf0yloHEPrQF6dWAdHy2bRhzdUGqYk0NBFhFyhmjqNRfvuqVlFI9eRNzHEd53zHg0fvOI8EUHrXON2vpVRTVOcJEdWqq41s5tFq07CcgEdizPxrDQrJaLozaRuhH6kIXJ8kT-qfLNrOpowOYmbpJdpUScXFrqx2sOndZQHs7P3gxrRTVDrLXWJlIqkH8nSjvVNiYudnEN6Bc_m1SzO2cBIGfSLIweTm4LJbq_sbmj7DYRF-Sfxmt_ul_vt7Pl6Eulm8P0cxj05FUuCdjtp78p8oCA2kjy8g9-HKevfn5H9CAz4G4uBUFtFKU4uXfBT9tfgciWz90XATuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKv61CHxAXeEcgM33O1IT0un-vzn4jp-iCF-EbIHRlS9dAxBuWM7x9wMtsAJc-BZuKxdQfqDmZYSuhLLYU9SUcg-PZGXCocVQO2U9GsuYifo6qWBDz05c_qAK6c8Bb6o9DcWQvCh1tpv_3Hgf6T1yEPTa5xVcSI87zO5XoHkQnwM_oTTkC4HHHG9Vm2CzXBINNjdgBY2BhbAFczXUEKHncG_AwmZXSSnBV2NQ9KXPKKlYArtv-yIIU95cfxnEDPwhW-Wj9er1ABl6aRLblwekMS1aYtFO8_4lnqVUdQV1pSgrAYqiz7au9wXjUys6ZFAaCiW9htckVULd7ORrWuvzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzTtbO-W45Lya_p-WhzOZZIBMC-oLXBWPyY_KmHR98v-dM3Axm_sstqkrO64YyJILCCRdj5tY31q02ula4booYiGk2UuKqzQdV-D2JNxPvRFFJfx0jcezvNhP9eLXYz0byTToCJbcdwoZkDrPx1_Ew1IxraNHSff11iKHkhzwdHxJ2ijYvRPUN6jRkTbr52FNsU-wPqpvtdxFBCxGDq0FFBZ2Bkd0ZMmGy-_ckphK0mf2Z9osw13y0cJIiQcrKwd_m4OqRy9xojv15flT-B9wBz_sjoNR7-dWh_Ftcn3K3CwuppISr0abQWAWsp4OwObu75g9vBxxqzPq-SrvOjIdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=p-dTUXMhDm6bTCn94DQyFSj8nkCjE_U0NNwlmxl8VT2C9i2gOYkkzzY5r57xt8wbKfrxbuwfIkiO8PdnY9B3TAZkU2IQRy9yBVp3EPJGkRsFgleD6RZ8_cQMePx99S0cbc8w5hi2BY4U71bFGPIrxL638ZcgRa2Q_KmaSl6E0Hb_rtRCHLIHuU58JSfRoRoqk1sg7P2ZCVbXsNP3vidHGCwKyF5mUet6N86qoDUq3TYl1Kdo2mrDKyHyAeITXX2-oyiC5cTK3Nq3fY4iqrfIYguIXpQedjcbp8PBiI5hslAvvInHwAkW4c859TOa2-BwXnU8jDewgof4RIgSDCcvbjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=p-dTUXMhDm6bTCn94DQyFSj8nkCjE_U0NNwlmxl8VT2C9i2gOYkkzzY5r57xt8wbKfrxbuwfIkiO8PdnY9B3TAZkU2IQRy9yBVp3EPJGkRsFgleD6RZ8_cQMePx99S0cbc8w5hi2BY4U71bFGPIrxL638ZcgRa2Q_KmaSl6E0Hb_rtRCHLIHuU58JSfRoRoqk1sg7P2ZCVbXsNP3vidHGCwKyF5mUet6N86qoDUq3TYl1Kdo2mrDKyHyAeITXX2-oyiC5cTK3Nq3fY4iqrfIYguIXpQedjcbp8PBiI5hslAvvInHwAkW4c859TOa2-BwXnU8jDewgof4RIgSDCcvbjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGkWmrw7ljHbfYNC3vepwVEb6mUNGMW_qxnrLJn6w4xYTK9Kd6EQQl6LK2B6DCGP01ctDxoEbZB2kFJuMbgafWoaTIUyHGSr9jxRywwAlTlPGXegRQr80uPow5J7JI9In2lYr4Fv7A2IfbEHXiuw42zumign91DBIBfowDutI-3ZWZDs6q22TR5j-QcbfSIoXNMOPjYIIM6BoDGdcSnIU_cK-VpmEamdPUUvtjMFzIc6NoX5K77gqUcf8pEA9ux6V_R0ti9JAMk80S-LCOEHBEi1SLctsz1cSlQJnhUmxIyoMWBtqXn0XOVpJ1-34sYTxFIGd39NhjzALdoc7LVyvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی ۶-۷ جمله نوشته که خط به خطش دروغه!
نوشته که مصر یک شریک مهم منطقه‌ای برای ماست و نمی‌دونم امنیتش برای ما فوق‌العاده مهمه!
در حالی که مصر و جمهوری اسلامی ۴۷ ساله هیچ رابطه‌ای ندارن و مصر حتی ویزای توریستی هم به شهروندان ایرانی نمیده!
همون موقع که پروازهای جهانی در اوج بود، حتی یک پرواز بین دو کشور هم نبود!
نوشته که اسرائیل علیه اتحاد و همبستگی اسلامی است!!
مصر حتی برای کشته شدن خامنه‌ای، یک خط تسلیت هم نفرستاد! براش این اندازه هم اهمیتی نداشت! کدوم همبستگی؟؟!
🔺
دیروز به دو کشتی حامل گاز مایع در مصر حمله پهپادی شد، دو تن از مقامات ج‌ا به روباز گفتن این فقط یک هشدار بوده از سوی ما.
دمپایی پوشان یمنی هم گفتن کار ما نبوده!
حالا این اومده میگه ما روابط مهمی داریم و همبستگی اسلامی!!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQpBB95D962pVsi8wLleZphJTAVIy0qLlKYO5hE5KCCDNIE8EXc0BsD0PMrvphOqjSmn-FJs9W_Ici2KgQnceYbetz9N1JhXPRA3rmaYR84Za8vHhpl3dmy0Id3GHJRaIkIAIXSzzqpfcHtP6IjjddbA3zD-i6r5zJ7qED-gR3njcJPgBk3YCcBirlOtfrwCIPdl9VkeoHhVxAAbsBCRzUpRz8TgLz5ItERnkbXhhMZYsSOGvzNCXkbgL5pIZO8vFxU96MXPviVmbT7SMGe_8f2tpmD75GD1bM7lG0BB78E0lI9kAzEQFQvB-gics8r-DYyArIpRZL-NbxBq3k1Aeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1NzlI-2wcXZR8L0kbNgB5h1XiZzAa40byrxH8vy3MokIWxBKVorUVn86bCoGu57cNieOtJbUOy2Xb_pKBC1cCb7sCsJM9AXpeckPRbceixV2SXZTXJvzZnmDwbl6vEt63f8kkJ1yYfMFTazZwQItiMx3ZmNqxL8bjCGyb7O0UKDc9z0DHZ9_wiZlW8sYpTUmf3ze1LG3B5GYYYSSQqX2lK2kJz-ExMU0SqaODJOmDfJa7oBbh7Zsmzh4lBgNkKzbtM0D0S5kJ-vVqYvhl0S-5GkXC4LVdC2H1J4FFVvIEsAuzp66EGkD_OYnmytpXeLwSQH4HsY4JEAUX--F6Kr1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mnfx3jvhSm2bNy_2N0eFGqTYRIzv6_pMENCQMr96eX877fh98b-6sJLpEyNAwsVCzRTcqFiBPBoJwu1u3FOK8wL2FogXNrPqyjalfd_l2DztRVpxonDyiQnuhRsqboA-6wlYSwH_sKjDnj9rxSCpazgWAtP8QWuvsflyrbbnHS6fhkKZTfhqLS83L8cmBhXtsYbkE9AIu1TKt-j_Fvte1sDDM7i_IocJFCToGNnQXJIw0f3IYwMm2WE3O8xTsap-irIbsbddf0L0lTLm9F1DXsD7PZdrkaDr6OyOmYTCcwVCqMwWwGJHlGPb-dTZ7RU5trmQLlSe4_bY30xwNNOcng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه بار هم درباره حجاب نوشتم،
در حالی که اکثر زنان جهان اسلام
(نمیگم همه‌شون، ولی اکثریتشون)
دوست دارند مثل زن‌های غربی لباس بپوشن و…..
زنان غربی هیچ تمایل و انگیزه ای
به لباس‌های زنان کشورهای اسلامی و چادر و مقنعه
و عبا و نقاب و برقع و پوشیه و ……. ندارند!
نیاز نیست حاصل تمدنی که اسلام
و جامعه‌ای که ساخته رو در ده تا کتاب قطور جستجو کرد! همینکه جمهوری اسلامی با حکم
«۷۰ ضربه شلاق» و «گشت ارشاد» و بگیر و ببند و پلمب، ظاهر حکومت و فرهنگ اسلامی رو حفظ میکنه، نشون میده، این تمدنی که میگن،  یک آدم برفی و یک توهم بیش نیست!  که به سرعت آب میشه و میره!
فعلا پول نفت پشت سرشه و بگیر و ببند!
حاصل ۱۴۰۰ سال عمر و ریختن ثروت و اموال مردم ده‌ها
کشور برای صدها سال به پای این درخت، هیچی نبوده!
نه هنر، نه علوم انسانی، نه صنعت، هیچی!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgX617RoBVuyu9HGj9fEtkbBHcetV0jAXNNJ7lte_Iqzwqz3yu0fBD2V_HI5z85lxWVhz-8fsaSTAmrLqVoW6JbD2IAdpDSfabeVIct3TienW7ifJp8mjIZ-k1qVr76c7qwV9msWG5cPRrBgWuWGp9Bz47uYNZvgsDXQkbRx2NVaYnr1lMiOjyEG2w0n8rjFJphonxxTIH8IKcQQ0AHLYBUGJUQTKfjebMmGfr_-RP4hKVNmTckNN6-YLLJBkzMHGMLUgQ-TITV5CJfXf71hqKJxnSYMh7X5-nnxqzpfLPMZ50LWH-6GOTrE06hwVtxIaPTXxUaxb-otBoxuD8dZ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5XK7DbUiNHwGFXrN5sYDWgW3F77ERDE4Gs_smpVChjmOMyfAnoLRBOxBwlUFqT7J6qSzUHFfQhpN9Ae06c5IT9aEM63rrBByYlySdSa_LKB-U3ZW5Ha1rFvESOEjIc0osLK6Tn_yTqvfISnT-32lf-S7smU0ucNrqk_2R_S1huUh-imhLqnHiE2_LHQdwE7AF7K0rfVa9EJ1vKWccaXLcIpJUjjuaK0Z_SUEKqVK5IwddEWQHCikZP6ThhuWNkNwh1FY_Vf3k5cRSaurWAxH57UI1u2CElSSHL5K9mymp7tQoJDs5mYihZapOofGpppR1JxNpMnpWdMNjooLAerETu8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5XK7DbUiNHwGFXrN5sYDWgW3F77ERDE4Gs_smpVChjmOMyfAnoLRBOxBwlUFqT7J6qSzUHFfQhpN9Ae06c5IT9aEM63rrBByYlySdSa_LKB-U3ZW5Ha1rFvESOEjIc0osLK6Tn_yTqvfISnT-32lf-S7smU0ucNrqk_2R_S1huUh-imhLqnHiE2_LHQdwE7AF7K0rfVa9EJ1vKWccaXLcIpJUjjuaK0Z_SUEKqVK5IwddEWQHCikZP6ThhuWNkNwh1FY_Vf3k5cRSaurWAxH57UI1u2CElSSHL5K9mymp7tQoJDs5mYihZapOofGpppR1JxNpMnpWdMNjooLAerETu8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnAY2uOV-qcW-7odqyKaiPpRUbqapcZgbRETe3OoEdo7S7i_zE_NAlXSEQjO2vWyh5Mc5s4TcxqiEFHeXQr0n0mVWjWvS6u5RlCNl8xGLXW5_7QaTzZ9ficmkmlMpncW1fTFeuwbgl0yo-bckPvMP8ZzeCfEqfajW4Eb4xCidPjl5q2tGlrEv1yMMtqigAb7Ntm9qpmY34bhuWQDe00S4GIpFchDZq7-Prvv1WmPOL2cP2GntELYR0VX8BYLv4N7P2Pj8QBjEnp_4HFJOiMHP93a0o5-2uDnaW471kkFcRJWiip1JIOQTjJPpb9azO20ybWu58WDPrvapyE5KqYMsVww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnAY2uOV-qcW-7odqyKaiPpRUbqapcZgbRETe3OoEdo7S7i_zE_NAlXSEQjO2vWyh5Mc5s4TcxqiEFHeXQr0n0mVWjWvS6u5RlCNl8xGLXW5_7QaTzZ9ficmkmlMpncW1fTFeuwbgl0yo-bckPvMP8ZzeCfEqfajW4Eb4xCidPjl5q2tGlrEv1yMMtqigAb7Ntm9qpmY34bhuWQDe00S4GIpFchDZq7-Prvv1WmPOL2cP2GntELYR0VX8BYLv4N7P2Pj8QBjEnp_4HFJOiMHP93a0o5-2uDnaW471kkFcRJWiip1JIOQTjJPpb9azO20ybWu58WDPrvapyE5KqYMsVww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=uENRJQCtCce0dRVgoiQ_Z-xtkrgliujvoJKJQ44Mc6bf1jNm3cyz6IKUQF5Hjuj4ezr9ShpuN4YkKCeswwESruENCayjuX6HxaCKkO5_Ix2w0uelnkL6ltHhKQLU_uyABeLs0F8ayH6Nkd4Mmq8qc-N8FoqxDCS1a6EwZGl_BlZnXOs55uNBSQxX7ty_rI0_zF2ivQ988UJFNzQXA7i0PmwLBoqectSDg1bu5a62mM-fDnHStSZK6Qv1pKsxdPyHnkv5C4iXnYo9gVzKeC1cTfc1RqhtwsGZ4ggbcWgRC9qM9f-I84Fp1whfygwmQl1d7hZnenLOnPw7wJJJzjgLxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=uENRJQCtCce0dRVgoiQ_Z-xtkrgliujvoJKJQ44Mc6bf1jNm3cyz6IKUQF5Hjuj4ezr9ShpuN4YkKCeswwESruENCayjuX6HxaCKkO5_Ix2w0uelnkL6ltHhKQLU_uyABeLs0F8ayH6Nkd4Mmq8qc-N8FoqxDCS1a6EwZGl_BlZnXOs55uNBSQxX7ty_rI0_zF2ivQ988UJFNzQXA7i0PmwLBoqectSDg1bu5a62mM-fDnHStSZK6Qv1pKsxdPyHnkv5C4iXnYo9gVzKeC1cTfc1RqhtwsGZ4ggbcWgRC9qM9f-I84Fp1whfygwmQl1d7hZnenLOnPw7wJJJzjgLxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6-R96gMyYT6MI0hVZtG3GAB7o1EnZWB1UAG664sJ1t7zHHbp28mMtbauCC3vKmjOWVk90BpPDDs8GWFKGhBkc1tfiIO4An69gJS9kPIj95mNcvenFAN1TgYHmuE-vlaLa5lIjvIwQw-6nDSJSP2e0JAeMLExA1c7d8o0wsQUeKEoSdDc-4gMu0k865pN8rkho1OKKERRA1I-ndW6gXV21h7GSqXeFU631KElRd3G7r1VvenbK222MEzGhMt7eUQfS_HD9jSsI6oWUrZZBG2aHlUGiweCg4dhX8firEHAdyBaEY1auXIalglUVEpsZrB8ekLc5Ld-sP5B8pW0lZoBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzKMpZyIQzVySGmF6BXDPxcJmXRPPAKScTtLZrOC8NVEN2HmYcUm0oiWTmJVBi-wgegyY4AnyzRaMHfZGTJkt7utAYfLN2f4F2beO4CTuRHqHM_y1RwZ6ft2TXidGXBAnqic-sAmrphSrgXhEvdl8Zd6YUss7t2RABrivkvH6_kjzzVreiFrnv7IRu923j6kkGptRyEsDAMVY9BNZcVIuVIzRPx5NOFvmcD8aNkfRCmeI47LaHfyCq6-8SDO0Vi1PM1K_2QTEC62W7bV5aIWO0NAmaIhVv2DHHBCUkQNvwoGqrj7l3ykvLk20YUZUevhTrzvrub9cLU3OCzbhlbzrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=Cjrv3UDRcPUGmWF_oFu6-INgtGCfViuVFD6HF5vQjoZFHUEAVE8rtREhQIiKCIguWEogd384Nrew8LgIq2qVUWpD31W43njjfy8PBXrBBSQUthb_PmPkzfcdmxAu9lVqV9hDpkZkY2e8REpbQwAId69UvFp0xdxK0XUIQE_NR6xorm1LY3z_5uwWQiRY-zWfAQgYokBlQP08qM6K8v3UPQY1bqAysE8mCWNK9CepTci7Nhy74tajzpe2t7rUh7SBjqq0Nmp2l5OfnIE_0ibW25kIVJkzr2GMEhMAlD8tBzwof1CPC_TBoID_m4rAaJKT_kfrOHl_bO9fXA-IZUhO3BaqXrxsoI0LgaUDNTc19ZPZQcxIlQhf1--qQrochk72TzjG51aibJXQWvpMXSAJxzT6Ot8mdtNykOMmhmHYhuhMWpkqd0anemZ45uNVBY6qW8upmM9AJvlcV6Pdh1Dq4Wy8rsE5k2JOE_ii-slNOq2iQEzB6YXtugvQ2IwsxzoUkjwHXzvuCpoy5bpxhX7f0UV7HaGmgXvOJTD01RWtucioZ4EGRcdvdOfDf2v3bF0b5lM_K9n3F0tKQONqZCq3WHwDJp-Pc-0co70fn1HlryODvleEhSs6kGLbaxGyYOzaor2frBtgotWRCzMcpoXF8DVeOideYza2_JgKgbVhHGE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=Cjrv3UDRcPUGmWF_oFu6-INgtGCfViuVFD6HF5vQjoZFHUEAVE8rtREhQIiKCIguWEogd384Nrew8LgIq2qVUWpD31W43njjfy8PBXrBBSQUthb_PmPkzfcdmxAu9lVqV9hDpkZkY2e8REpbQwAId69UvFp0xdxK0XUIQE_NR6xorm1LY3z_5uwWQiRY-zWfAQgYokBlQP08qM6K8v3UPQY1bqAysE8mCWNK9CepTci7Nhy74tajzpe2t7rUh7SBjqq0Nmp2l5OfnIE_0ibW25kIVJkzr2GMEhMAlD8tBzwof1CPC_TBoID_m4rAaJKT_kfrOHl_bO9fXA-IZUhO3BaqXrxsoI0LgaUDNTc19ZPZQcxIlQhf1--qQrochk72TzjG51aibJXQWvpMXSAJxzT6Ot8mdtNykOMmhmHYhuhMWpkqd0anemZ45uNVBY6qW8upmM9AJvlcV6Pdh1Dq4Wy8rsE5k2JOE_ii-slNOq2iQEzB6YXtugvQ2IwsxzoUkjwHXzvuCpoy5bpxhX7f0UV7HaGmgXvOJTD01RWtucioZ4EGRcdvdOfDf2v3bF0b5lM_K9n3F0tKQONqZCq3WHwDJp-Pc-0co70fn1HlryODvleEhSs6kGLbaxGyYOzaor2frBtgotWRCzMcpoXF8DVeOideYza2_JgKgbVhHGE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=n1h8BNSvTIpYBm-YZp_DEMrigVEurfpjkCDtjCYdYMGZ7Lu0WStL8p9k7encGwz0jGMUIRUTF1B-dUvxAgXrPgNPZsCpUVXVR9wP7xpa2HSL0RB5SO3sswAqwXf_VNhuGwtip8XMaNs3_Tig_vftwZoBkrpbUsGUnltFBVuBkrk9NbvEvnc4zM-gcOHDHS6HWLJMhxNSPsxCQip9iBDKR_J5aufO_5Z3hSC4tDH_-9YVR7COZk-W8bnkoprpzyY09YIv_bqq-Pho3r8rCUT8kzONMy-n937Bqy9NSazwZRYTsgy5mSSRXJy2-zsdL0O3Sh9pqhLC5jtB21jKubjsyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=n1h8BNSvTIpYBm-YZp_DEMrigVEurfpjkCDtjCYdYMGZ7Lu0WStL8p9k7encGwz0jGMUIRUTF1B-dUvxAgXrPgNPZsCpUVXVR9wP7xpa2HSL0RB5SO3sswAqwXf_VNhuGwtip8XMaNs3_Tig_vftwZoBkrpbUsGUnltFBVuBkrk9NbvEvnc4zM-gcOHDHS6HWLJMhxNSPsxCQip9iBDKR_J5aufO_5Z3hSC4tDH_-9YVR7COZk-W8bnkoprpzyY09YIv_bqq-Pho3r8rCUT8kzONMy-n937Bqy9NSazwZRYTsgy5mSSRXJy2-zsdL0O3Sh9pqhLC5jtB21jKubjsyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cao_S2VoE6UC_BLxmW7PVgQORdfcwmuGLNgPAxxtHCs3GvlMgcB2zE9WTQPs73U5lfDXBqIAZWtI7ys7vyJviJfHkCtpKdzlxi3idTDnWYiuyqkrhBNamX1oEgFAnygTvvTJ9_53oZW43EE1Eh322rOL0qPmtgVWcA8bqanKSNpJMpjRMdiynCCdnzQuZiqmHyzcvHZNgkynTwQuKrzTURMTe9Z6oq7NzMoSVg-TyysY_urP-m_zkkBF5ziqlif8hNjomtliC8DBmzqhGPrc_RI_VAQVBQPYDnU4kHM2f8OKgJauHMFN8cyEPx9gFycZi4FRIjNQHmc9btfQlwqmKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vkideNER7sEH6XLn-hpu7PZeAXtZgIRznne2oi9RzdNEnA_n0VGLjrcXgLJ_eDyoEng1Y123rM2EJ64e7JtB3QVJ5ZzxuxLF1jySJWJcjf29ZBOiOwWRog0BJQ4tNEzwQICp5GOuopg-Aahk70_EBH6XONMWh_F-BE3FNVGUvbHUaPCxaoJyO7DhSTGR3Jqsg8Or9JtRfZzKkfhl7BJuknPGVq07oHDmnjrkFJhR9y-lvtQM_5QGHPuwE7AineCLkAdBmFANdi6ui-UcNOTpBB6iAC8yycdn_rmbEImNaP8SVvCCP6M6FfdH_PBXLbMQNQPIgMk70F5p5pQ1YHtVzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DB28lZAVnOmZ1Ov3rc18xoI2mgsnm8qgrlwqOcOdUSIy3EKdlE4LP3OjwOcz8hfv8K--7bY0JzCS603u4fXys9FZv3D9K8IvdLrAK8yXOBi80NfdGujVBoV5qAyT_CY2U0n7a6ZnArTieRilPggMHYHaMkiPpVURIG3cSvqlBM95Oh6opXY5z9BWaGk90TsoJa4rywyww9nv51tlgjQexULouIgqe3qnWIv-KxfePUKA9JSfhGLhyq9reGR6RNwiXS3e-M-0ffs87v1i2kSjrFiVSF_eiK61ZifND76YJit_PZUsVBt0Ym80YO5Ym-zIfWK4vpb9d_UaxFcKhQ0Rjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=K7urVSY-hHyKMcn5hQLD51SVHIG1fYK6vCoBHKEV7TntmcqjFz3kmwtgM0EVuo5pWGEPuPddJ9CMBMCKoDn0TuQKECzzuDcT_Exxc7UZ7a2Nuyavg8uoVH7IB2gbeg91ZzprmcCtdCjyPL0-QPA16uS11BDD5OrqzYYqHqReTl4U6WjuC7h02tiU2qDPTjGoDrzruzN6RJkXG36DQ762CV-uNym01lznhYPbURlwAjM02rXbgVFJOUE8xkm2p1pSZiQZPbJzfha9SnFXyxe1ogVcKJkUUUOU1TM5H4eSE13G0LeMvlV8To6Qa5G926MlhjlH31uWEhFB-PQ6kEe3AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=K7urVSY-hHyKMcn5hQLD51SVHIG1fYK6vCoBHKEV7TntmcqjFz3kmwtgM0EVuo5pWGEPuPddJ9CMBMCKoDn0TuQKECzzuDcT_Exxc7UZ7a2Nuyavg8uoVH7IB2gbeg91ZzprmcCtdCjyPL0-QPA16uS11BDD5OrqzYYqHqReTl4U6WjuC7h02tiU2qDPTjGoDrzruzN6RJkXG36DQ762CV-uNym01lznhYPbURlwAjM02rXbgVFJOUE8xkm2p1pSZiQZPbJzfha9SnFXyxe1ogVcKJkUUUOU1TM5H4eSE13G0LeMvlV8To6Qa5G926MlhjlH31uWEhFB-PQ6kEe3AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
