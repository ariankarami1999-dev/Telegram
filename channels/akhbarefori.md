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
<img src="https://cdn4.telesco.pe/file/edHwB3Tg161wjMCQG7ePdnsXc2Z6NyfSrKNlpYg-SzjP0Cgot7dwF4Yij4Tv6P-9fLaXrVgRhVLvqTOWS2V2oOv0uVHRPMF-jT2c_o2zPhhYg3gfAANjNfTdwiIOdBTCSr5QWfK3TAyYUIRkhSgg9aCCnVrXhIIuvBc8BM_0lYxxW1BXs1RUucr7bJCJve7aqktPaveTkNY3lFBWTiQE_U08iZ0R5UzF_MbOpKPLNLmL1uolgpNECjbEKB5wznPDf5sXJoVh-qdWWLYNJTeuMHqzKlxevTdUXYHGBo7Z4bS6BX7_kLjFmtsrJ2OOUXdURgNyVuC1uQlNVyJAGrf4wg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.38M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 17:39:15</div>
<hr>

<div class="tg-post" id="msg-670557">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
رسانه‌های آمریکایی: روند عبور کشتی‌ها از تنگه هرمز کاهشی است
رویترز به نقل از داده‌های کشتیرانی:
🔹
تعداد نفت‌کش‌هایی که از تنگه هرمز عبور می‌کنند، دیروز به پایین‌ترین سطح خود در دو ماه اخیر کاهش یافت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/akhbarefori/670557" target="_blank">📅 17:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670556">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
صدور کیفرخواست برای عباس عبدی و مدیران روزنامه اعتماد
🔹
متعاقب انتشار یادداشتی از سوی عباس عبدی در روزنامه اعتماد، دادستانی تهران به دلیل جنبه عمومی جرم علیه نویسنده و روزنامه اعلام جرم کرد و پرونده برای انجام تحقیقات به بازپرسی ارسال شد./فارس
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/akhbarefori/670556" target="_blank">📅 17:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670555">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-text">خرید ارز اربعین؛ ساده‌تر از همیشه!
💫
امسال با آپ و بانک شهر، تهیه ارز اربعین از همیشه آسون‌تره.
📱
بدون مراجعه حضوری برای ثبت درخواست، با اپلیکیشن آپ می‌تونی ارز اربعین رو برای خودت، افراد تحت تکفل یا دیگران ثبت کنی و تا سقف ۲۰۰ هزار دینار ارز بگیری!
✔️
کافیه وارد سرویس «ارز اربعین» بشی، اطلاعات لازم رو وارد کنی و بعد از انتخاب تاریخ و شعبه مورد نظر، ارزت رو از یکی از ۱۱۰ شعبه منتخب بانک شهر دریافت کنی.
💢
یادت باشه قبل از هر کاری باید توی سامانه سماح ثبت‌نام کنی! از اونجایی که فرآیند نهایی شدن ثبت‌نام در سماح حدودا ۲۴ ساعت طول می‌کشه و پروسه تهیه ارز هم زمان می‌خواد، حواست باشه خرید ارز رو به روزهای آخر موکول نکنی که فرصت رو از دست ندی!
⏳
#آپ
#ارز_اربعین
#اربعین۱۴۰۵
#بانک_شهر
#اربعین</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/akhbarefori/670555" target="_blank">📅 17:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670554">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/186f179d33.mp4?token=jgx5_McgRVop0TAgY7wF22xWG9rVGwzmTtrRfgWfTL9HEbU_mZYzX9bXRqDD4zcVASKi_P_7ASigLMSlfPnPl395dhOPC1x2siY3QD0ohNXtDNhKwkcDCL_O78Ndgmus8D8GQG7-QMUt282q-qEV1P9mVAy8GjYIiitExLn22hrw-_E_X8MpW1vG64pTQ7acO52c4hLad17XqTra8ztn88k_1X8YvMRfJmxkzz-bl-ODtpZ0u_mfwamMdqEbS25h2kxdhQqpZ3HRtG3SnhMZvHb3fdFw_juPDLdnzaEB0fHQi0wDTd9ag9wAXsmDSIoM0i9b09m8unLnKN84zw1ejg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/186f179d33.mp4?token=jgx5_McgRVop0TAgY7wF22xWG9rVGwzmTtrRfgWfTL9HEbU_mZYzX9bXRqDD4zcVASKi_P_7ASigLMSlfPnPl395dhOPC1x2siY3QD0ohNXtDNhKwkcDCL_O78Ndgmus8D8GQG7-QMUt282q-qEV1P9mVAy8GjYIiitExLn22hrw-_E_X8MpW1vG64pTQ7acO52c4hLad17XqTra8ztn88k_1X8YvMRfJmxkzz-bl-ODtpZ0u_mfwamMdqEbS25h2kxdhQqpZ3HRtG3SnhMZvHb3fdFw_juPDLdnzaEB0fHQi0wDTd9ag9wAXsmDSIoM0i9b09m8unLnKN84zw1ejg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از لحظه‌ پیاده شدن مسافران یمنی هواپیمای ماهان‌ایر در فرودگاه حدیده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/akhbarefori/670554" target="_blank">📅 17:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670553">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a93e52233.mp4?token=QbX1V5Amu5iY273VdO3ziDsTma-g6MlfqFZ8Ep0XDFkijxQO-Pv57bH6A0GEkerHkh-C6iFsEcfuq-sKQSLpLHGCiwUKDVbNdwrp6kQbkSMmJO1F-DdAtKOaty6dRKEy6qpsNSVxUT3ZRBwQyPAFnXr6aAYP0hZvWI6lFe0GrFPNFYp4xdiXUGwXg1skDYBeS4ULQAFQPHD8vxS_9q6oM0PcpATCTEvziTvwDhwwcpiPci7pbFWB5SnhoDmD05nIrhRIF3QzKP0_-ru8nl4Sug6mwNhaQ6WxutVx6qpimgddSt-9E4RC4UV-DN64-xSdJ4fg7xpHcHG_5D0nPjBFYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a93e52233.mp4?token=QbX1V5Amu5iY273VdO3ziDsTma-g6MlfqFZ8Ep0XDFkijxQO-Pv57bH6A0GEkerHkh-C6iFsEcfuq-sKQSLpLHGCiwUKDVbNdwrp6kQbkSMmJO1F-DdAtKOaty6dRKEy6qpsNSVxUT3ZRBwQyPAFnXr6aAYP0hZvWI6lFe0GrFPNFYp4xdiXUGwXg1skDYBeS4ULQAFQPHD8vxS_9q6oM0PcpATCTEvziTvwDhwwcpiPci7pbFWB5SnhoDmD05nIrhRIF3QzKP0_-ru8nl4Sug6mwNhaQ6WxutVx6qpimgddSt-9E4RC4UV-DN64-xSdJ4fg7xpHcHG_5D0nPjBFYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ترین‌های جام جهانی تا اینجا؛ از آقای گل‌ها و گران‌ترین تیم‌ها تا مدعیان اصلی قهرمانی در یک نگاه
▪️
قسمت سیزدهم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/670553" target="_blank">📅 17:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670552">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
پاسخ در راه است...
🔹
تصویر معنادار یمنی‌ها در واکنش به حملات امروز عربستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/670552" target="_blank">📅 17:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670551">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkZ589UmFRY-F_Br2cKHsBC0FGbBoZn2jW90Ygl0GNRHwdTklaJBdTmStOYPF7GB3JsFrDnniV08RGSWboZLe5aoTuCDbVoygQtUGOSq3QUTE5b4miKlGE6vbmt1y9iwuPk4VewVZUB0nSdA0FeT4ivT34Z4aKxjZIl2QRj9GAumX0ocx9Pq4GY-glisrWxTu-4KwTjSxiVmcECj9T_jaQ_Au--iZ1MxlA1U_mGA_lFqOqJMejJHrKcLbk6dBMAjIM_p7xpLcyTvu5ryCAID37Pp-2lrjGHtMT76SddWfopaV96JZzXPVL4e_NcJKtAnDJDR9_84tX_nNzq50BYRxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت به ۷۸.۶۰ دلار رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/670551" target="_blank">📅 17:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670550">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0lblehvomsRpVpDsLFUqjG3JW7815BbEcXbB9hOU1UZ-fiSo_YWVO2NZRQnNK3JsAOzTVgh1OoCKN1ouoW6vkluWcv3BNHAiIvPGZn9PhHYIW1hmgOwJv91cmwxMsQbUr0pJdHXRL0fmwwZTPO3h0rY7sHIK2pzWsLrmN_SMUSJ5NXCZnzAHZydaYTiXYVdZyIAkbdt0GqSJvtUepVoBUogk6GBJoTg-cN7cKrYSMjK5xP7wFgnSKAcaM4S6AFn_X0-O4yb3Dr31MFAv4SUpKu-WD4W9PEKLCdyBNtYS0XOHN5PLANUL5PknKPDHqQVPRGoAXyCe27XWlUxBSP66w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی سپاه: حاکمیت و مدیریت بر تنگهٔ هرمز را با قوت و قدرت اعمال می کنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/670550" target="_blank">📅 17:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670549">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tu6_iDsesRXK0HuXOmY6cz4wJX1VRDreYVtVOUbCrM8d40eqsy38_VQ8gCRCwkKtkfFRfXrHn09VY9tEe52TqYomls5X7ZLchw8AjXYWnUyRFOCKIkZ2OxCmlFtxH6pd9beX4moebqNY5yiI5P4YR7jUOklJKCbRFp3zOQ5y0mrNlSMjTLDv9pRHLQusqmRzA4XU9nUGfEGk0x_jMsn-E2RNlfn4J9ssENfhaZHBzOFhEseh6c0BHsya2PqqjlQxco3zDzvZDN2h1Fvhjkl9iIrq9tBZgHwI-SfnyFtLrRMcr8FKhQRMQulspOYP4hJJML4M3ro39RqBIFjri_7EZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویدئویی از لحظه‌ پیاده شدن مسافران یمنی هواپیمای ماهان‌ایر در فرودگاه حدیده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/670549" target="_blank">📅 17:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670548">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2WMZ0__USCt6BqDJBl-HyuQG_CCybo9HxWLQx3yHSs0RVs_NFFU6C-jOf25tBcOLNYtif-v1_P-SwXSEwycCVUykakklN0kR3nx6fMh3wDVO8IaDc81x5SnSJg3WkybvnpGf-R0ZM_9eiDLvSc0JQk89hVGP9HSKCMKuB7oX1ZtLKCx3Ss79i89s8K_Qm4yqPPW3AS9aHBFVFjLWAOswz0GY0vovj8O3-ZicS-kgiiJVqflm8RrYDm21xoHtE_n6-IK9rTeHeVQxTqvzUxjFd4RrCqNNJkQACVmtlOl3JhoMmUF0nsrFrMEJSHmlkcpH05pttQHvs3GT4tlLQgeYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با یک آزمون، استخدامت رو تضمین کن!
🎓
کارفرما دنبال مهارتِ روی کاغذ است، نه فقط ادعا. آکادمی آریاداناک این فاصله رو پر کرده؛ بدونِ نیاز به دوره‌های طولانی!
✨
آزمون تخصصی + مدرک معتبر + رزومه درخشان
فقط با چند کلیک، اعتبار حرفه‌ای خودت رو بساز و از رقبا پیشی بگیر.
🎁
کد تخفیف ۲۵٪: aria25
🔗
ورود به آزمون‌ها:
https://ariadanak.com/ariaacademy/
📞
مشاوره و راهنمایی:
۰۲۱۲۸۴۲۴۵۴۳
۰۹۹۲۶۶۶۸۴۲۴</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/670548" target="_blank">📅 17:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670547">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
آزمون وکالت ۱۴۰۵، ۱۴ آبان ماه برگزار می‌شود
🔹
ستاد مرکزی اربعین: کاپوتاژ  اتوبوس و خودروهای شخصی در ایام اربعین ممنوع است.
🔹
وزیر آموزش و پرورش: مدارس غیردولتی اجازه افزایش سلیقه‌ای شهریه را ندارند
🔹
شرکت اسرائیلی: مسیر جنوبی تنگه هرمز عملاً از کار افتاده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/670547" target="_blank">📅 17:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670545">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
شیطان خون‌خوار: ایران در آستانه دستیابی به سلاح هسته‌ای قرار داشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/670545" target="_blank">📅 16:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670544">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‌
♦️
سخنگوی قرارگاه خاتم‌الانبیا: به سران کشورهای منطقه هشدار داده می‌شود هرگونه همکاری یا پشتیبانی لجستیکی از ارتش آمریکا، به‌منزله جنگ علیه حاکمیت و امنیت ملی ایران تلقی خواهد شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/670544" target="_blank">📅 16:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670543">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‌
♦️
سخنگوی قرارگاه خاتم‌الانبیا: به سران کشورهای منطقه هشدار داده می‌شود هرگونه همکاری یا پشتیبانی لجستیکی از ارتش آمریکا، به‌منزله جنگ علیه حاکمیت و امنیت ملی ایران
تلقی خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/670543" target="_blank">📅 16:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670541">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff97123423.mp4?token=C0ERI12SLiiKDNYhVyL9_Ftrxd7-q97AI8695biiT2JJwP_rKdb4cT2SYKe5Jqv4wwqiBsnQqd81UdyAqFT8cPn-r5RiYJmfgrXh-jcxYn-lRRKkfgkpF9Cux4ViaBcJjBgki7oOIjNafTPbYTt3HTqGBt_FYlV3CFkSP9R3awy7skkOv2mDwBpllpbDVa6TDa4M5fEBx4Uz5Gd_W3iEw6lP6_E6V6NTsM3Kqm_6OIo7-ExTKpcqFYQWxqh9OwTOm7NW0rrLqkFfhVc2Xas8WGrYyE6RqmGqvZpdWg5plipM09mI3x8IggK9fql9xa8I1NliwNPibJZHYjTzMe4O1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff97123423.mp4?token=C0ERI12SLiiKDNYhVyL9_Ftrxd7-q97AI8695biiT2JJwP_rKdb4cT2SYKe5Jqv4wwqiBsnQqd81UdyAqFT8cPn-r5RiYJmfgrXh-jcxYn-lRRKkfgkpF9Cux4ViaBcJjBgki7oOIjNafTPbYTt3HTqGBt_FYlV3CFkSP9R3awy7skkOv2mDwBpllpbDVa6TDa4M5fEBx4Uz5Gd_W3iEw6lP6_E6V6NTsM3Kqm_6OIo7-ExTKpcqFYQWxqh9OwTOm7NW0rrLqkFfhVc2Xas8WGrYyE6RqmGqvZpdWg5plipM09mI3x8IggK9fql9xa8I1NliwNPibJZHYjTzMe4O1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی قرارگاه خاتم‌الانبیا: نمی‌گذاریم آمریکا در تنگه هرمز دخالت کند
سخنگوی قرارگاه خاتم‌الانبیا:
🔹
ایران با هرگونه ایجاد اختلال یا ناامنی در عبور و مرور کشتی‌های تجاری و نفت‌کش از سوی ارتش آمریکا، خارج از مسیرهای تعیین‌شده ایران و بدون مجوز نیروهای مسلح، با قاطعیت برخورد خواهند کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/670541" target="_blank">📅 16:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670540">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d76806ced.mp4?token=lCDWpfIs-q5vHRDduldfNExpvhry-8lJq9ZWaFYeqeWF2hmAL1e8sVxfTueaxg_Hkfo4yglEof6n2Wosk67zLaq_ebx42tDrGl2Chy2mb31jHXSCP0D2pAlwpR_jJipqeqAuGzh3aEIdckLAjX8K_KVCPETqni7bYZhd6tgD6lrwV8RzZXzpO24GFgy348msGbVZfP3PH81Hy_AHXFm3SwYOFyG_EpR4cE5SOJCq-VU5MsU51h97Ssef1AnAj9Pa17CYOCLTDUB4CpkLqSvVKRgjjrKitVdCemg0ZKnauREoIlKD_2Uu7FYSTIFhMbjJRFUiUCtnB63PVltrx7JkLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d76806ced.mp4?token=lCDWpfIs-q5vHRDduldfNExpvhry-8lJq9ZWaFYeqeWF2hmAL1e8sVxfTueaxg_Hkfo4yglEof6n2Wosk67zLaq_ebx42tDrGl2Chy2mb31jHXSCP0D2pAlwpR_jJipqeqAuGzh3aEIdckLAjX8K_KVCPETqni7bYZhd6tgD6lrwV8RzZXzpO24GFgy348msGbVZfP3PH81Hy_AHXFm3SwYOFyG_EpR4cE5SOJCq-VU5MsU51h97Ssef1AnAj9Pa17CYOCLTDUB4CpkLqSvVKRgjjrKitVdCemg0ZKnauREoIlKD_2Uu7FYSTIFhMbjJRFUiUCtnB63PVltrx7JkLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توهمات خوک زرد: آن‌ها هیچ شانسی برای بازسازی ندارند. ما آن‌ها را تحت فشار قرار داده‌ایم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/670540" target="_blank">📅 16:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670539">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f08115117b.mp4?token=c_vcEHC2schW-Yjy0W6YAswZAg15HYp0FAnC47Nm_o3ZVNGq9QNqTCjrTi47Y8-0M2cxDu8o97dZBjKBsrsJfT5YDDZ_DPFEE_SfsHU1j6i8drs3Asd7mOtjGh-teJp-iu9HEroMn57ns5CJoB7OBeIVZF9GT5TQ0txkBHjheJpRfVmMYku3LZ4shcqh8q6tsXBdnDxPMEu08Z60zb3eIXYlfxIrnbRkjnq6Y6HzMmXa4QEwc46p-5jZgMR5SF_WXb-0WJpVjW7vSGEa7Ds0BhzJRipjQoTjAdFt8h_hmBaDGgiAc5D3zipjPKcHJG3wE9dzXQc7uLqww8OpKRwyRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f08115117b.mp4?token=c_vcEHC2schW-Yjy0W6YAswZAg15HYp0FAnC47Nm_o3ZVNGq9QNqTCjrTi47Y8-0M2cxDu8o97dZBjKBsrsJfT5YDDZ_DPFEE_SfsHU1j6i8drs3Asd7mOtjGh-teJp-iu9HEroMn57ns5CJoB7OBeIVZF9GT5TQ0txkBHjheJpRfVmMYku3LZ4shcqh8q6tsXBdnDxPMEu08Z60zb3eIXYlfxIrnbRkjnq6Y6HzMmXa4QEwc46p-5jZgMR5SF_WXb-0WJpVjW7vSGEa7Ds0BhzJRipjQoTjAdFt8h_hmBaDGgiAc5D3zipjPKcHJG3wE9dzXQc7uLqww8OpKRwyRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه فرود هواپیمای ماهان ایر
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/670539" target="_blank">📅 16:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670538">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7491e8f22.mp4?token=U66NHzwTDIR_d8zJLue2cNDzkSVB-MfMug_ZRQ6b0h2qOKP3D9H5JyWXudvLqUq__IO2gCm4wRy2jPK634rSZk8wHiPhccPXCHdd_CYfvHym2wMS_kahuvTL7ntUzXyqhSQg8nXH33ZD2cuYWYwN9awux_VGAkKcOWcWnaQFsXhWZdUX0rPo5Rz5JdpmrI1Qp5KDHnj0xA3d3ouPaeEJOwwY0PEHY8YK73-BlLF0vQ8-IWXmz07ENKuynjXCgR4BNHiqxOAe8fNNJRs6Sm2WTI25byFA3op4SgHfcZRUZepjaLN9mTkNqtOiUwq8LUg31VPn2Sm7BPRnW6Sz7RMIpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7491e8f22.mp4?token=U66NHzwTDIR_d8zJLue2cNDzkSVB-MfMug_ZRQ6b0h2qOKP3D9H5JyWXudvLqUq__IO2gCm4wRy2jPK634rSZk8wHiPhccPXCHdd_CYfvHym2wMS_kahuvTL7ntUzXyqhSQg8nXH33ZD2cuYWYwN9awux_VGAkKcOWcWnaQFsXhWZdUX0rPo5Rz5JdpmrI1Qp5KDHnj0xA3d3ouPaeEJOwwY0PEHY8YK73-BlLF0vQ8-IWXmz07ENKuynjXCgR4BNHiqxOAe8fNNJRs6Sm2WTI25byFA3op4SgHfcZRUZepjaLN9mTkNqtOiUwq8LUg31VPn2Sm7BPRnW6Sz7RMIpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش سعودی فرودگاه صنعاء را بمباران کرد
🔹
شبکه المسیره از بمباران فرودگاه صنعاء توسط ارتش عربستان سعودی خبر داد.
🔹
همزمان وزارت دفاع دولت وابسته به ریاض نیز خواستار تخلیه فوری این فرودگاه شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/670538" target="_blank">📅 16:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670537">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6355d1623.mp4?token=C2VwE8eq6-6mzJY0jOJTF-qeFOViYi10_7puBpoC-pOTa2Q0gQ5bUuuCAwFpfhyyq_Hd_aTCqqT0Guc0gIq0VoqJj3yj3MCBKrr78wY4QDfe2DAyl8C_UAythOUfqhjYduYl-xhSEyYe5jX-qzmwduAi9mHq3RsHj82fK7VvsGcKW9Fxnivmvn5yuHmD4ooTlChxzGB8NdBKH4dItsFz8kAIfFOFoxIV9bUtyYS_99LjkomKG22vHB18zjmzQ2AqrJJSZbaB_WfdixNhrV_O4r9hG__8SizYvnWzaoaXDXEAtTlDBK9g7fCA4NHE93Kjp3CwaNWOPCiN9Rwk348vAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6355d1623.mp4?token=C2VwE8eq6-6mzJY0jOJTF-qeFOViYi10_7puBpoC-pOTa2Q0gQ5bUuuCAwFpfhyyq_Hd_aTCqqT0Guc0gIq0VoqJj3yj3MCBKrr78wY4QDfe2DAyl8C_UAythOUfqhjYduYl-xhSEyYe5jX-qzmwduAi9mHq3RsHj82fK7VvsGcKW9Fxnivmvn5yuHmD4ooTlChxzGB8NdBKH4dItsFz8kAIfFOFoxIV9bUtyYS_99LjkomKG22vHB18zjmzQ2AqrJJSZbaB_WfdixNhrV_O4r9hG__8SizYvnWzaoaXDXEAtTlDBK9g7fCA4NHE93Kjp3CwaNWOPCiN9Rwk348vAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توهمات خوک زرد: آن‌ها هیچ شانسی برای بازسازی ندارند. ما آن‌ها را تحت فشار قرار داده‌ایم
.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/670537" target="_blank">📅 16:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670536">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc25c6702a.mp4?token=QePGZ1acT4P1gOOgtQOXVfSer98wptaOwbLkLo6DT-xboxapKxtW3HXralMjRB2tOxNsAYh8zwgxQmbCX3QvbxKCKBNFGhYHoywM19sYpI9m2dADWvCrscuga-UB2ZapY5XQBOd8Op4FPjZ7fiCz2o1CdkpE7hL2PT_AiCjnNEYq_QYjS0Re3F1luC7lBZGV09XCHEHQMpu64uA72yCRccg7JF1b23h40CbnIbhu6bHyDY0uhcX5R1OcAuU6CM7K1RPKxdxuy1P4ege5lo7SENZExHLvrSdK6tZIamepK7L0GORyh5nozakjVHF2Q9xgrvNnXTTSECMMt_SGHXnO_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc25c6702a.mp4?token=QePGZ1acT4P1gOOgtQOXVfSer98wptaOwbLkLo6DT-xboxapKxtW3HXralMjRB2tOxNsAYh8zwgxQmbCX3QvbxKCKBNFGhYHoywM19sYpI9m2dADWvCrscuga-UB2ZapY5XQBOd8Op4FPjZ7fiCz2o1CdkpE7hL2PT_AiCjnNEYq_QYjS0Re3F1luC7lBZGV09XCHEHQMpu64uA72yCRccg7JF1b23h40CbnIbhu6bHyDY0uhcX5R1OcAuU6CM7K1RPKxdxuy1P4ege5lo7SENZExHLvrSdK6tZIamepK7L0GORyh5nozakjVHF2Q9xgrvNnXTTSECMMt_SGHXnO_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان خون‌خوار: ۵.۲ درصد از رئیس‌جمهورها کشته می‌شوند و ۸.۵ درصد تیر می‌خورند؛ رئیس‌جمهور بودن خطرناک است
🔹
تو جزو همون ۵.۲ درصد خواهی بود!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/670536" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670535">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
شیطان خون‌خوار: ۵.۲ درصد از رئیس‌جمهورها کشته می‌شوند و ۸.۵ درصد تیر می‌خورند؛ رئیس‌جمهور بودن خطرناک است
🔹
تو جزو همون ۵.۲ درصد خواهی بود!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/670535" target="_blank">📅 16:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670534">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d708202c.mp4?token=CEyN21olIbO4ftQdFyLIFE2artYD7hBIVtJRdZJ3CB1fnPoqXriz0CNjULA3tmLRco0LwE0lpiFMBO0rmMBUd-MeqtH9RLZSt0OJy-9sJX8SL3dn3tWJQE09sNAtwS2EW9ggGmN9gtqv8cLkx3_myU3bJE81wNAOeJGqZ8G1-zOGlvP_YCOMQdR9L-zvwNqMeaKeQu5J84QIVM5zHrhspX93o2_u6l4l83zc1QJwq6Jbpx5Q4V0m1ZRBIM-hdKIVG2GMi9Kl36ED7KJp_AvWv8PpfkhrkQ6TxpQ7KPbk1P9-T2cVSrwQtks4x4oJbeuc667e7cOk-WHdGwonD_W7Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d708202c.mp4?token=CEyN21olIbO4ftQdFyLIFE2artYD7hBIVtJRdZJ3CB1fnPoqXriz0CNjULA3tmLRco0LwE0lpiFMBO0rmMBUd-MeqtH9RLZSt0OJy-9sJX8SL3dn3tWJQE09sNAtwS2EW9ggGmN9gtqv8cLkx3_myU3bJE81wNAOeJGqZ8G1-zOGlvP_YCOMQdR9L-zvwNqMeaKeQu5J84QIVM5zHrhspX93o2_u6l4l83zc1QJwq6Jbpx5Q4V0m1ZRBIM-hdKIVG2GMi9Kl36ED7KJp_AvWv8PpfkhrkQ6TxpQ7KPbk1P9-T2cVSrwQtks4x4oJbeuc667e7cOk-WHdGwonD_W7Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: اوباما به سمت ایران گرایش پیدا کرد و به همین دلیل، ایران قدرتمندتر شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/670534" target="_blank">📅 16:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670533">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4cb46e412.mp4?token=YRsTGfTNPazhbzQDZj9ud6NlGToaKK0pB-Hxv2ADnWoE0hgFdBefCYIU3aRUEf6oAPBhTx0iB-gEZDv9bDIr5QOxK44GcqquRAiMpSfmewauS6UhfQSYRbptLnm7PwSjkiMHOmYEZGixpyPMjCy04apWFNuuVR6xqFUC0a0swdLC_UYzuCj8vKrBtT0bp8gKVsM-DRHTnflkK5o1hMNZBwrTOZXOPqd4NGvpzwOHBAFl1_WUIde4whKwQ2joW780r28wSJQ-5Vvfbizhw-B9lq1vpsL8AKuKOCFrZuqPvDIAG34IEzHiZduBMun81EM4H9HLU9_KUAZunJ3jTEekqgdam75n2cVK1HJu5GDV-UfuRQecr6okRuKOEwyBAgtpQ5SIR4RTR5xuIntc2Lf7QOGwDQDOMImdUHac8up3RqQZdgtAQtRRuVwI5xgU38i2F3d-mJFY5M_xSZnYvLLzpM4QCNLQvDXw7yM4Het65mT2Y3M3q8A5Omgk8MQgInxvGuSxoRZGtudupGjFIsxB-Qge4PZg6A5-mT9YvhrkxSQ1KAqMQnmIqZozDSn4y25Gro9ArVHRCA2z48kOg-MnS8l4Psv7ecAwNOQ7nr1GHAQNUuRhE7AYcjhPIpH168msL1gc2cZgTvWPJzYJdcqq6OVTlIfJVAxhZnydCBqRORE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4cb46e412.mp4?token=YRsTGfTNPazhbzQDZj9ud6NlGToaKK0pB-Hxv2ADnWoE0hgFdBefCYIU3aRUEf6oAPBhTx0iB-gEZDv9bDIr5QOxK44GcqquRAiMpSfmewauS6UhfQSYRbptLnm7PwSjkiMHOmYEZGixpyPMjCy04apWFNuuVR6xqFUC0a0swdLC_UYzuCj8vKrBtT0bp8gKVsM-DRHTnflkK5o1hMNZBwrTOZXOPqd4NGvpzwOHBAFl1_WUIde4whKwQ2joW780r28wSJQ-5Vvfbizhw-B9lq1vpsL8AKuKOCFrZuqPvDIAG34IEzHiZduBMun81EM4H9HLU9_KUAZunJ3jTEekqgdam75n2cVK1HJu5GDV-UfuRQecr6okRuKOEwyBAgtpQ5SIR4RTR5xuIntc2Lf7QOGwDQDOMImdUHac8up3RqQZdgtAQtRRuVwI5xgU38i2F3d-mJFY5M_xSZnYvLLzpM4QCNLQvDXw7yM4Het65mT2Y3M3q8A5Omgk8MQgInxvGuSxoRZGtudupGjFIsxB-Qge4PZg6A5-mT9YvhrkxSQ1KAqMQnmIqZozDSn4y25Gro9ArVHRCA2z48kOg-MnS8l4Psv7ecAwNOQ7nr1GHAQNUuRhE7AYcjhPIpH168msL1gc2cZgTvWPJzYJdcqq6OVTlIfJVAxhZnydCBqRORE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد: خیلی محکم به ایران ضربه خواهیم زد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/670533" target="_blank">📅 15:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670532">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
خیال‌پردازی گستاخانه خوک زرد درباره تنگه هرمز
ادعای رئیس دولت تروریستی ایالات متحده در رؤیاپردازی جدید:
🔹
ما بر تنگه هرمز کنترل خواهیم داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/670532" target="_blank">📅 15:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670531">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIhZXBT35inJXX3qVHCv2rNZvRReZUt-SzxQfCRN4U8TguQhOlJkiiEfueVQIkLlLg1CkXXsTyYLV9vIgY6trRnVa4np3dhArrt4y42-JpDIyosKvCr0IIaeeXXIbDc_EBDbgXlrxrwF69SgutBewcTSX7vfS74TPh4M_pv-XC7Mf4gJVc7w6RFaGJmx5zfpxuT250uleg5IR68sK29o1m0W_HbsAFOD2VEbArZU-VlNPV7DBT758FTedTUIv95FpCD99hdUALpNsbzHO-9uvunqLyUCv4r5dIOGUAaXQXTN8m1WTETIr_g7HowooUFx21trglVZAkpiLaXbdG5_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیژن مرتضوی، خواننده و آهنگساز ایرانی مقیم آمریکا با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/670531" target="_blank">📅 15:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670530">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22da5e019f.mp4?token=MEZH6B1v8EPE2jXs31m962phJQtBXmbSzIQmK4oGFYQd-nn74aQTrnco5bEAjDjrMrjJcO2__ANp0lumlOB8LYuNuBy-EUnwNE1HtVxklN3tsZ-lnYGMWfOouDn4utK_qyoCF5Ej1fb3iZiSewwwQvxLU_q7ra9R0MvuAsTluz9JCNF89FFIHUGY7neDdfqjknUhtWuNxyVvxBKWID2oMxQgVEhi6PaIgJACh-oCuIiWU1IhRZ9IQORrF0DEuyii3xye9n_ZKV2oMY4R9DNb3mWxUYiAaMEXUwCsHRL5YvRC3f4eXkeJxxMm4MOt6bQMKmzzn3w1RhuOzrPPhUEMnSV3PogXcbLQ-20EB0ZgSTOl8d7E3jB5Cfp-njbKPE2UvELl7PO2bb6xZfDzbjrCOi9rLpPy28Xj2sDRztFmHDYkaFkqKDW3OoeB8tNADZJYSbD3sYzFafc97iq43CSUZG43eZAJ30Qg-CL4XGH583e18x4PRwwBlpV4rpi41GqOoz71rP5YC4nOjpCXCK_l72r-tEHp3jXT13S3RyzcLHl9uDCiikFLbmQoo9Clyl_Xhv6L1pzzhZw8SGp5i-uNWm1_ImeNmnYAqb8-B1uREGUOrw0GeIfFj_ncfywnVWTNrnUnlm0fPjoIPaA_ZMrsMZrXKVBrFyUTMYsl_17SdLY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22da5e019f.mp4?token=MEZH6B1v8EPE2jXs31m962phJQtBXmbSzIQmK4oGFYQd-nn74aQTrnco5bEAjDjrMrjJcO2__ANp0lumlOB8LYuNuBy-EUnwNE1HtVxklN3tsZ-lnYGMWfOouDn4utK_qyoCF5Ej1fb3iZiSewwwQvxLU_q7ra9R0MvuAsTluz9JCNF89FFIHUGY7neDdfqjknUhtWuNxyVvxBKWID2oMxQgVEhi6PaIgJACh-oCuIiWU1IhRZ9IQORrF0DEuyii3xye9n_ZKV2oMY4R9DNb3mWxUYiAaMEXUwCsHRL5YvRC3f4eXkeJxxMm4MOt6bQMKmzzn3w1RhuOzrPPhUEMnSV3PogXcbLQ-20EB0ZgSTOl8d7E3jB5Cfp-njbKPE2UvELl7PO2bb6xZfDzbjrCOi9rLpPy28Xj2sDRztFmHDYkaFkqKDW3OoeB8tNADZJYSbD3sYzFafc97iq43CSUZG43eZAJ30Qg-CL4XGH583e18x4PRwwBlpV4rpi41GqOoz71rP5YC4nOjpCXCK_l72r-tEHp3jXT13S3RyzcLHl9uDCiikFLbmQoo9Clyl_Xhv6L1pzzhZw8SGp5i-uNWm1_ImeNmnYAqb8-B1uREGUOrw0GeIfFj_ncfywnVWTNrnUnlm0fPjoIPaA_ZMrsMZrXKVBrFyUTMYsl_17SdLY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◾️
سوگواره رسانه‌ای «بدرقه یار»
▪️
از تمامی هنرمندان، عکاسان، خبرنگاران، فعالان رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود آثار و تولیدات رسانه‌ای خود با موضوع تشییع رهبر شهید انقلاب در داخل و خارج از کشور را به دبیرخانه سوگواره رسانه‌ای خبرفوری با عنوان «بدرقه یار» ارسال کنند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگوتایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر و مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبرفوری ارسال کند.
▪️
به آثار برگزیده هر بخش، ضمن اهدای یادبود
#بدرقه_یار
، جوایز ارزنده‌ای نیز تعلق خواهد گرفت.
📅
مهلت ارسال آثار: تا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق شناسه
@Badraghe_yar
در تمامی پیام‌رسان‌ها ارسال کنید.
برای اطلاع از جزئیات بیشتر، کانال رسمی سوگواره را در تمامی پیام‌رسان‌ها دنبال کنید.
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/670530" target="_blank">📅 15:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670529">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1de61a4eaa.mp4?token=k9ReRy_HLjAknvCNJhWI3vovmz3B-ne6XySnnh4NIcBIWFRt6Jz2KdKK6IY3FLMQWNPlN_-X-BD0_epHTQbqqcP2z6KCxahtaHDCmI1JecOMt2i2Hf63WU4HIcwW7x0vFRsEYICI03Mh3YNjRl0tSY5Aq0MmjYyRHfzBxDZc-NfR8aUWoJ35eChh1E_Wq-C0GbZrqcfCuk5gThQzTZQmXmPlZcIGq8NG0w2xMKZohDlVPfNm3rZDfUFDMVTNRJ4H1VIXwVTE5FEgpKYbgbfxwfBWxKHDAri7X6KKuDtGYoDg1EeWL-bukOxNjBwsoBkbyNfwOSNuG4pIh8Y0odtlkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1de61a4eaa.mp4?token=k9ReRy_HLjAknvCNJhWI3vovmz3B-ne6XySnnh4NIcBIWFRt6Jz2KdKK6IY3FLMQWNPlN_-X-BD0_epHTQbqqcP2z6KCxahtaHDCmI1JecOMt2i2Hf63WU4HIcwW7x0vFRsEYICI03Mh3YNjRl0tSY5Aq0MmjYyRHfzBxDZc-NfR8aUWoJ35eChh1E_Wq-C0GbZrqcfCuk5gThQzTZQmXmPlZcIGq8NG0w2xMKZohDlVPfNm3rZDfUFDMVTNRJ4H1VIXwVTE5FEgpKYbgbfxwfBWxKHDAri7X6KKuDtGYoDg1EeWL-bukOxNjBwsoBkbyNfwOSNuG4pIh8Y0odtlkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه فرود هواپیمای ماهان ایر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/670529" target="_blank">📅 15:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670528">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amDgqQPnbtuSce5_LbzYk-Rl-SPu8R6KNSG0djAXiRTJx2Qlcx-kcPoKM98-gwCJ2M73D9ECW3ayd8KR4PPMGwbNDBa-bJMGn9bIgnibFpaV-7rYrNcyzeo6Nxjy5Iq6-I1IZa45UCQLGPj42i8O98WZlMnqcCKM7qVGOU9HfygZqmzITeXWcKsqF2ZnKvm4AtEAUAhPkh1PrFYujeVVcw1TZBBsksd3ysBJH9pbuE9pCPGAUequ7UDg1eY1QDN5s_lJr3KTr16yQE1FwhmXtecyf8wCSgxehhZl5WcD0oYym0u80gSONsG71AZHJe59Xd7whGS7YmCa8Av8zplgBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش: ساعاتی قبل، یک فروند پهپاد متخاصم دشمن متجاوز آمریکایی با رهگیری و شلیک موفق سامانه موشکی زمین به هوای دلیرمردان نیروی هوایی ارتش، تحت شبکه یکپارچه پدافند هوایی کشور در بندرعباس، مورد اصابت قرار گرفت و منهدم شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/670528" target="_blank">📅 15:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670527">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">💠
ماجرای جنگ ۲
💠
روایت متفاوت جواد موگویی از تشییع رهبر شهید انقلاب در عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/670527" target="_blank">📅 15:31 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670526">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
تردد کشتی‌ها در تنگه هرمز صفر شد
🔹
داده‌های سامانه ردیابی دریایی MarineTraffic نشان می‌دهد از عصر روز گذشته، یکشنبه، تاکنون هیچ کشتی تجاری که سامانه شناسایی خودکار (AIS) آن فعال باشد در حال عبور از تنگه هرمز ردیابی نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/670526" target="_blank">📅 15:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670524">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I63SxN7RRgJ0Rn7tnkr3Iye9fzkSNu0vNEx_eXP6eKBhj9RZDzvWbtgbKoatUA7zNfOFOtAplebUOmp_w1U01bJAYD3G94SUeb1qMlFg0aUiayIyPX6SSb3YeS4gLxOGQL94chxqrrz1UakdJqEUZfqvJLvU2jL2tNJETi0_MQ-Eq43S4FiJ8AcgfI_bLUL_JXo_skMkYCI5vQHowkHPY_G5I9YUkW15eNfJYpU9HCROU_t4bhLnjqzXRGIxE-KgUy3MfvjP8HoZbpEpNSjFnBfaDz0XkLWhV2qZxCI6U_61FV_hpsiRt3JtQQSpDCiQFeGg1X54tZUTIePg8B-KcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fp7Lty5xh67yv3ARIcwTo8mUaJFKlCr8TQdf4rVlCM7w3XEHJlmUb2rOnBrWOoDzukMLVPJ1LkxHlf-UihotNQ87rORxbhGmfHoiRldv41Pc2jLDKgrHCdtUeG3BDxqgVGF_JLar5q8LxUgckkA4bdREpolDmW66fZJM_c7uSffqYlNtxFCtCHMDK1-xv9eHYL-iOBv89YW0omhIT1pUK3sAZTgRRQgNMfXXZGYSSfy9VXNGD76WpN79N-I6j8zP2dIeXsfBCRDDG1SXlkJizq_4ljKfEgkJgdznOGRvMqXJwGbHvs_cbHjQYev_uuyB4DXZADGGgcMF_3VmCUOydQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عضو دفتر سیاسی انصارالله: هواپیما با موفقیت فرود آمد و محاصره شکسته شد
🔹
هواپیمای ایرانی پس‌از حملهٔ عربستان به فرودگاه صنعا، در فرودگاه الحدیده در غرب یمن فرود آمد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/670524" target="_blank">📅 15:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670523">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c02f55f5.mp4?token=PQYeKD9TshLyvKx2C-y3kYhsJKmyQM4_O28HIv_Q6LbmM9cb384FdKY50bBZoVgLntdoBpv0DHPPsbKaYFYBr_ptyDHkxwsPHzxXRYRU3OrS0tM-yypBvBFOcgDFu1YqxZxPX_HGFA8FHmxeXXvLij45ODtISgEmtcBbfRoSR8lXxCdoaOP_I_UsmlVy9r7kjDe8M9_TJlBHpFEBTQiFCIfbxyNgUKaWpLlTe8XYexqksYjtLbbiCaD_EyWI4ByWtkgOHlSmhzIYzDhgtkuXNRVQiFPQxo581lH66eEUsqUxc6rPHJsdUn4WyCerjdcipA-r1Wny0CIiFG2N8FngqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c02f55f5.mp4?token=PQYeKD9TshLyvKx2C-y3kYhsJKmyQM4_O28HIv_Q6LbmM9cb384FdKY50bBZoVgLntdoBpv0DHPPsbKaYFYBr_ptyDHkxwsPHzxXRYRU3OrS0tM-yypBvBFOcgDFu1YqxZxPX_HGFA8FHmxeXXvLij45ODtISgEmtcBbfRoSR8lXxCdoaOP_I_UsmlVy9r7kjDe8M9_TJlBHpFEBTQiFCIfbxyNgUKaWpLlTe8XYexqksYjtLbbiCaD_EyWI4ByWtkgOHlSmhzIYzDhgtkuXNRVQiFPQxo581lH66eEUsqUxc6rPHJsdUn4WyCerjdcipA-r1Wny0CIiFG2N8FngqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای شما هم همیشه سوال بوده که این صحنه‌های آخرالزمانی در فیلم‌ها چه‌طور ساخته می‌شوند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/670523" target="_blank">📅 15:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670522">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
اقدام خصمانه انگلیس علیه سپاه پاسداران
🔹
دولت انگلیس در اقدامی ضد ایرانی و در همراهی با سیاست‌های خصمانه آمریکا، نام سپاه پاسداران انقلاب اسلامی را در فهرست ادعایی خود از گروه‌های «تروریستی» قرار داد.
🔹
طبق این تصمیم عضویت، شرکت در جلسات سپاه پاسداران انقلاب اسلامی یا نمایش عمومی نمادهای آن اکنون در انگلیس جرم محسوب می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/670522" target="_blank">📅 15:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670521">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEpKrW9Do4UqdMRoICzj-jN1aVpz3BDlElc5c96ryV_zNgdmIDASXR_hSJ9NhUT8ko1PiMRO5KjHJ_KqiPaUunAb6Z1zalpBf6t_ZR9lsK5VFy7Yw_iDIw7iTJAtd_eNErR7z5GAsEs5XKdg7i2eqR_jMfNkF5_ZBw-L7pvIHbtD9ZuLzmgqa74ldChJf74lJ2AOovo2-lC550You3Cx5CuVDgVvnX8Jm6vjuN6W2hcl1h6_bpipfp4XdO39UuhKvcOAc-o5nBzxe9mEYZxqGQdbodAbh7sIQ7mRI2-7tfxV-ndS1F82P3sLko9dTr0T7WFznQSpDG-ugR1P4H3LHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی بریتانیا: گزارش یک حادثه در فاصله ۵۰ مایل دریایی جنوب عدن در یمن دریافت کردیم
/ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/670521" target="_blank">📅 15:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670520">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j48lCREzcsrXJ7H055fh4DTYh8Vrv-2IBp0IXxnMr-mC2BbzLY84CziVhTnFBje2M2cTuZhn4jv68tV4BIclhk08gUrcePL2mAY3kQpjIoB5RZ_b8EZ7lqhX-n8rwefjDswUwfNjk6lR9nq_dbaVG5-VRid9xtBxUD055J6lTuDwqGb8ageUqfR1gysuUDrwxuGYiP6Iim8xw60nPPGsQat4MStQP2nuW1rVXAM6GxC4JD5lYoLFjGm7zitapJF08yuUGkBhFD9VdR5IyYDYo3G2An1qK16KHAevc0qgguL5fohfSnKIr2xTzFJu7G6thgAqbNvbO2N_eF0j4k987Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه پاکستانی: روسیه هواپیمای روز قیامت را به ایران اعزام می‌کند
روزنامه دیلی‌اوصاف مدعی شد:
🔹
در بحبوحه افزایش تنش‌ها بین ایران و آمریکا، روسیه ظاهراً گام نظامی بزرگی برداشته است.
🔹
روسیه جدیدترین هواپیمای مرکز فرماندهی روز قیامت خود، Tu-214PU را به تهران فرستاده است که در شرایط جنگی هواپیمای بسیار مهمی محسوب می‌شود.
🔹
این هواپیما همچنین یک مرکز فرماندهی پروازی نامیده می‌شود؛ زیرا به رهبران ارشد و فرماندهان نظامی کمک می‌کند تا از یک مکان امن با یکدیگر تماس برقرار کنند و در مواقع اضطراری یا درگیری‌های نظامی بزرگ، عملیات را رصد کنند. /خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/670520" target="_blank">📅 15:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670519">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در امارات
🔹
منابع خبری از شنیده شدن صدای انفجار در امارات خبر دادند. وزارت دفاع امارات با صدور بیانیه‌ای فوری اعلام کرد که در یکی از انبارهای نظامی زاید آتش‌سوزی رخ داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/670519" target="_blank">📅 15:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670518">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
منابع یمنی: عربستان همزمان با نزدیک‌شدن هواپیمای ایرانی، به فرودگاه صنعا حمله کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/670518" target="_blank">📅 15:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670517">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca8bcaccc.mp4?token=rwA1xNgn-8cjCDeRN8OrCmvfusC9RS_oF9RmLUdhuIxGp6u8QhebUTT0JhEOIoOF5R7J9Rgdd4_0tVRYcpxGrhLz5xlR1zBRBjq4GhuESVpS0l91b3CT7BkhklClrm-iILv3rS31J1B3r_QWjTYvEN9tHUP6g4JzXBiZFjLWCiUyDJmBR2i62A9VClHcqazY4_H3xilHAMhbBJUxkHdDeBGgSjxf-KvFd5TyUJsw0fbW7f77fOUDlE8QGl3cutrd2-zlZ4lNM0GTEOKrwaULHIwayk6l2Wj9k1KL5rxSaQkwqsxgGWcCBRfKeA-EeoFB908kmXMbI8PYZAoe8rObXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca8bcaccc.mp4?token=rwA1xNgn-8cjCDeRN8OrCmvfusC9RS_oF9RmLUdhuIxGp6u8QhebUTT0JhEOIoOF5R7J9Rgdd4_0tVRYcpxGrhLz5xlR1zBRBjq4GhuESVpS0l91b3CT7BkhklClrm-iILv3rS31J1B3r_QWjTYvEN9tHUP6g4JzXBiZFjLWCiUyDJmBR2i62A9VClHcqazY4_H3xilHAMhbBJUxkHdDeBGgSjxf-KvFd5TyUJsw0fbW7f77fOUDlE8QGl3cutrd2-zlZ4lNM0GTEOKrwaULHIwayk6l2Wj9k1KL5rxSaQkwqsxgGWcCBRfKeA-EeoFB908kmXMbI8PYZAoe8rObXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سمفونی «مظلومِ مقتدر»؛ روایت رنج و فداکاری
🔹
هر پیروزی، حاصل صبر و فداکاری مردمانی است که برای حقیقت، از عزیزترین داشته‌های خود گذشته‌اند.
🔹
موومان چهارم «سوئیت سمفونی مظلومِ مقتدر» با عنوان «خون دل»، عمیق‌ترین لایه‌های احساسی این روایت را با آواز بازگو می‌کند؛ روایتی از رنج، استقامت، ایثار و هزینه‌هایی که برای حفظ عزت و سربلندی این سرزمین پرداخته شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/670517" target="_blank">📅 14:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670516">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSjdYNQ1n2NuVLiAYHvPbZs6zJ_iddIR_1Mo3XSQamf6GirHCcpX8iVbuHEcPbjBP0F0IIM7Ds9qPa0PXyw7ZW_HXyzZIpaa9NN62_Q4W76KbDHUD0BReW7qnVvXSEANNEU5M2H4CRR6aDauis-fsHH6Na_AcfxxRamGf2eeLobX539wUJOr2XINvoRUqlYIAfSsq-7d0gfiTDlcD2aO8A3W9-26-zGKhFJ9XtHVQPoSHUKiFfEXvec-zYVxWw-N-3xLdTa7fAdYKR7XbK9coztU2_lCliT8x6eedrMtJvOpXIdeo109VHYyh_kHMpNZIvg2ybtlCjffKFEtfylhXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میچ مک کانل (Mitch McConnell) سناتور جمهوری‌خواه تندرو و ضدایرانی هم که یکماه است ایست قلبی کرده و در بیمارستان بستری شده و هیچ اطلاع دقیقی در مورد وضعیت او در دسترس نیست.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/670516" target="_blank">📅 14:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670515">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d57059b301.mp4?token=RV7vvVVqQbsxe0Cp7OY6g2yn2OQCP4vwcgtxMXgE4EeFE1u58F8Zdkno6GK3ifb8sIG_6it8SzWgl0zCWPplIRnEQ8PTrWZoRAKkW4crR3yHHIr6O8dUW9vCwduMdz2szj_52KHL-c_Apm-4JQTdzirCMJvI1flLw5Oyzj1_xHyapV0SDZewZvqcF7AYKI3Q8stUkEJe_CDPIMlmGolwiBQCmvZArX6tqg4s_Pr2nw3lx0c1invLI3w_QGxRfuCXKku-JoEuS76XI6bEqaKtPmR3zsayFFEU33uk2Kky3NaEUC4u6MZoAOVjhJ1skpNf2H9Vll5waTTfHEjaxtXoMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d57059b301.mp4?token=RV7vvVVqQbsxe0Cp7OY6g2yn2OQCP4vwcgtxMXgE4EeFE1u58F8Zdkno6GK3ifb8sIG_6it8SzWgl0zCWPplIRnEQ8PTrWZoRAKkW4crR3yHHIr6O8dUW9vCwduMdz2szj_52KHL-c_Apm-4JQTdzirCMJvI1flLw5Oyzj1_xHyapV0SDZewZvqcF7AYKI3Q8stUkEJe_CDPIMlmGolwiBQCmvZArX6tqg4s_Pr2nw3lx0c1invLI3w_QGxRfuCXKku-JoEuS76XI6bEqaKtPmR3zsayFFEU33uk2Kky3NaEUC4u6MZoAOVjhJ1skpNf2H9Vll5waTTfHEjaxtXoMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تداوم حملات گستردهٔ اوکراین به نفتکش‌های روسیه در دریای آزوف
فرمانده نیروهای پهپادی اوکراین:
🔹
دیشب ۱۵ شناور روسی از جمله ۷ نفتکش را در دریای آزوف هدف قرار دادیم که تعداد شناورهای منهدم‌شدهٔ روس در ۸ روز گذشته را به ۱۰۵ رساند.
🔹
طبق گزارش‌ها اوکراین در هفته‌های گذشته دست‌کم ۴۰ نفتکش روسی را در دریای آزوف هدف قرار داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/670515" target="_blank">📅 14:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670514">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFEmPzkCB9GDuv76NbRp04cVKcXnj-3YATwIdSpSKklGUZjCWWhuYQyX8t8rPqFm7CtlYwPnzo9IUfZCjSXtoeIDONeh5qKEor5Khlno3O3UpsTEfEdz1UYsOK6DW2bZ7b5lBwV7L0jCfhSEF7xkOouiWaB0EzTRF9QKp1MhDAZjDkdnj266MFjmtGLS6dSuZDW92R-Bz2TD29N7Gb6TthU9BbAdKvHSmbR-qHqNLvuFNcItxHil1wSUlpRAr9NvwGiglE1O3j5pi9PZJgC89nR6FkL5pWbd2ol_M3JBYpvcgBgCL9ALrN4GGVs0l6Isa7XmSh1HH2ZfnNqA7ubX7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش سعودی فرودگاه صنعاء را بمباران کرد
🔹
شبکه المسیره از بمباران فرودگاه صنعاء توسط ارتش عربستان سعودی خبر داد.
🔹
همزمان وزارت دفاع دولت وابسته به ریاض نیز خواستار تخلیه فوری این فرودگاه شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/670514" target="_blank">📅 14:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670513">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
ارتش سعودی فرودگاه صنعاء را بمباران کرد
🔹
شبکه المسیره از بمباران فرودگاه صنعاء توسط ارتش عربستان سعودی خبر داد.
🔹
همزمان وزارت دفاع دولت وابسته به ریاض نیز خواستار تخلیه فوری این فرودگاه شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/670513" target="_blank">📅 14:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670512">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ارتش سعودی فرودگاه صنعاء را بمباران کرد
🔹
شبکه المسیره از بمباران فرودگاه صنعاء توسط ارتش عربستان سعودی خبر داد.
🔹
همزمان وزارت دفاع دولت وابسته به ریاض نیز خواستار تخلیه فوری این فرودگاه شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/670512" target="_blank">📅 14:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670511">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3OXq-7iRgYicHRq61yhNV12Lz67G8IwWxJhU2lIegwOZZWrOkUv4AjbXNKJb73vubwyqnFkZ9z5b0GSc792n934j8B-olBw2ACbk-eFcq7Egpzcc90EWydOpI1tWyZWPNmXiCDXdd8k2r93PihMJTbj5HFvELTqJrHz9_ij_CP9Gm0m1PEoxJep1pp1noRxm1sF_M7SdYOWY-CUFzgkv4-9P-J1Ox6iQ8nanUAA4uKFTK46ZK2v3dDVrnqHazEEEtaKv4pcRrH3-EXaTqY8JOJ6oT_q2CEYEQH3-ckY9hqV-Vo5kDITLuZn-UbXWlA2y8I6W58NLsiyP9fx8GuiMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین بازدهی بازارهای مالی در سال‌ جاری
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/670511" target="_blank">📅 14:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670510">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f53e24f4a.mp4?token=rSqCdusksGXF_kg0u-QQJ_QuY9Pw6pPUWPlpsKxG8NIdyquE9_I-I23WinyiCMISAT3xCdYfjgo6gpXD8Xq8YuvGFEfggF1lNYIqA5H6awVioWRXEMk2t0IRaZ5P6bvjkqiq8ZayrnC8ioVEkaRRNUf95vpzV-BGgxmZa3fVoJBQNRPMHg-q9I9kmnsxdqjnEFojYuAAGgIEFqJGjERCnr_eYQ36H7-B4Qw-INCox7X7AEDf4Kd2GaX8xXbq2DnqvB8VXvHdrWpv8pe12pP3CMty341OJCaISPCQnmsnMEYqrAsFR81U2kgKP2-Xgz93fKsTRW2IJGlnfVCLyKDZWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f53e24f4a.mp4?token=rSqCdusksGXF_kg0u-QQJ_QuY9Pw6pPUWPlpsKxG8NIdyquE9_I-I23WinyiCMISAT3xCdYfjgo6gpXD8Xq8YuvGFEfggF1lNYIqA5H6awVioWRXEMk2t0IRaZ5P6bvjkqiq8ZayrnC8ioVEkaRRNUf95vpzV-BGgxmZa3fVoJBQNRPMHg-q9I9kmnsxdqjnEFojYuAAGgIEFqJGjERCnr_eYQ36H7-B4Qw-INCox7X7AEDf4Kd2GaX8xXbq2DnqvB8VXvHdrWpv8pe12pP3CMty341OJCaISPCQnmsnMEYqrAsFR81U2kgKP2-Xgz93fKsTRW2IJGlnfVCLyKDZWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنگۀ هرمز در پی نقض یادداشت تفاهم توسط ارتش آمریکا، همچنان بسته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/670510" target="_blank">📅 14:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670509">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
ایتالیا: نمی‌فهمیم چرا نخست‌وزیر ما از ایران تهدید شده!
خبرگزاری آنسا ایتالیا:
🔹
تاجانی، وزیر امور خارجه ایتالیا، پس از آنکه چهره نخست وزیر در فهرست سیاه یک روزنامه ایرانی قرار گرفت، گفت: تهدیدهای ایران علیه نخست وزیر جورجیا ملونی غیرقابل قبول است و ایتالیا علیه تهران نمی‌جنگد و نخواهد جنگید.
🔹
این تهدید «غیرقابل قبول» است.
ایتالیا علیه ایران نمی‌جنگد، به همین دلیل است که ما دلیل این حمله علیه ایتالیا را نمی‌فهمیم.
«این یک حمله باورنکردنی است.» /خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/670509" target="_blank">📅 14:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670508">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
استانداری خوزستان: در پی تهاجم هوایی آمریکا به نقاطی در ابادان تاکنون دو شهید و سه مجروح گزارش شده است
/مهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/670508" target="_blank">📅 14:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670507">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
برق ادارات پرمصرف این هفته قطع می‌شود
🔹
حدود یک‌سوم جمعیت ایران تا ۳ دهه آینده پیر می‌شود
🔹
تهران و مسکو به نهایی‌سازی قرارداد تجارت گاز نزدیک شدند
🔹
کرملین: کشورهای حامی اوکراین، جنگ‌طلب هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/670507" target="_blank">📅 14:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670505">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
اصابت پرتابه‌های دشمن آمریکایی به آبادان
«حیاتی» معاون امنیتی و انتظامی استانداری خوزستان:
🔹
ساعت ۱۳ و ۴۵ دقیقه امروز دوشنبه ۲۲ تیرماه شهرستان آبادان مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت.
🔹
تاکنون مجروحیت یک نفر در اثر این حمله گزارش شده است.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/670505" target="_blank">📅 14:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670504">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k08tjoHbcl3h_-Kpz9Y7K3A2YLHmtUx04kovuf0Mar5MJ-MaZJYICArJNfok5uMIilc1zKNLMfD0Hm5HClFy6D--WEiXYVZPBE40_K9pDMvHZMDs55kF7pD7IJagLa2UXBNYm40OK2pUzO8l2o7AEzHcCW3BCrFTJ-4a5shHCG4R8Hu9no7RBl_Iny0M2OIqC50raGWEgjsc6m09X9RF7QBfOtVz-8ww0Jnzeb6EBfxwP0N7Kq5PclgrJduepbviQ2mhJ7UyNDtqY2SHi9PKla8Tv2qfNpRj1_vWKIxb9uMqJkkSGs_ABELCxybEVLcgvJIo0boI-JO4yjJgdql3DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما او را به خاکِ ایران سِپردیم؛ ولی یادمان باشد که او
خاکِ ایران
را به ما سپرد.</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/670504" target="_blank">📅 14:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670503">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80c4d6e586.mp4?token=ewPunu8yJYrfel_3FrUhKB0E-s2lBI8eFaYTWZ8XLJRRMfXWFoUNiVBfE0TvVrSel-yLAoXQSuN7HvSn2EVcqA2ptFy2_qT6eXGfhwSutHAr5yqEgfTim0DMEcJCAtqhH4f653kaapcPPY-nANBlv0KfGrOVknz1xE46fCJ2t3hY-e83mG_52_i7W1QAQiodbwkA0aODa9OIgwsXsCDq1TxU0fs22O5-jkLkQAKg_FPQTquVmr0mdKSwyBGhmyTgRM9fAP9q8yV-Eu8lD51IWRQGxdTG2OVYOBcvSjbezDxWx2zoS-MdfsTO8AyO-Sg0TltD7yUvvsAnb_s4a7jhmazq0w2pJ8x-E9-xb2bV0vUsOwMcUmOcx4NAi_FnOqbQDjJfAK6y-AXqqlncbNm1TZiNuupiH74qJ-v28TddcT0wcazkmjZNYr-hkFag5P3FF1I9BGZAVr12F7wCVULV0OjUBHj63jWBdb-Dmxd96thM6dE92skAnz8J0ry1rQ_xEF2XmLq95Vlxdd-HiJ-WgtXF2Bh0C3DZL6I8MjtSrG63XrECjZCVK7VQn4kYq8aVMfDNOTfqJJj8OrbJzdxp6MugeLR5xoVB1v8in6rZAcpwQ-ooJ-QpfG3dP7KwSShEZJOppigdsU_CQi5_LxCvQ1IqJhjS9389CfXCdGzR6wk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80c4d6e586.mp4?token=ewPunu8yJYrfel_3FrUhKB0E-s2lBI8eFaYTWZ8XLJRRMfXWFoUNiVBfE0TvVrSel-yLAoXQSuN7HvSn2EVcqA2ptFy2_qT6eXGfhwSutHAr5yqEgfTim0DMEcJCAtqhH4f653kaapcPPY-nANBlv0KfGrOVknz1xE46fCJ2t3hY-e83mG_52_i7W1QAQiodbwkA0aODa9OIgwsXsCDq1TxU0fs22O5-jkLkQAKg_FPQTquVmr0mdKSwyBGhmyTgRM9fAP9q8yV-Eu8lD51IWRQGxdTG2OVYOBcvSjbezDxWx2zoS-MdfsTO8AyO-Sg0TltD7yUvvsAnb_s4a7jhmazq0w2pJ8x-E9-xb2bV0vUsOwMcUmOcx4NAi_FnOqbQDjJfAK6y-AXqqlncbNm1TZiNuupiH74qJ-v28TddcT0wcazkmjZNYr-hkFag5P3FF1I9BGZAVr12F7wCVULV0OjUBHj63jWBdb-Dmxd96thM6dE92skAnz8J0ry1rQ_xEF2XmLq95Vlxdd-HiJ-WgtXF2Bh0C3DZL6I8MjtSrG63XrECjZCVK7VQn4kYq8aVMfDNOTfqJJj8OrbJzdxp6MugeLR5xoVB1v8in6rZAcpwQ-ooJ-QpfG3dP7KwSShEZJOppigdsU_CQi5_LxCvQ1IqJhjS9389CfXCdGzR6wk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جهان‌بخش پس از بازگشت از جام‌جهانی، نانوا شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/670503" target="_blank">📅 14:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670502">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
عراقچی: گفتگوها درباره تنگه هرمز در سطوح سیاسی و فنی ادامه خواهد یافت
🔹
در سفر کوتاهی که به مسقط داشتم با وزیر خارجه عمان دیدار کردم
🔹
به همراه هیئت‌های حقوقی و فنی، درباره هماهنگی دو کشور ساحلی تنگه هرمز برای مدیریت این تنگه و تردد کشتیرانی به گفتگو پرداختیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/670502" target="_blank">📅 14:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670501">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
محکومیت ۱۲۰۰ میلیاردی سرشبکهٔ‌ اصلی قاچاق سوخت در میناب
رئیس‌کل دادگستری هرمزگان:
🔹
حکم محکومیت افشین بادپروا، یکی از سرشبکه‌های اصلی قاچاق سوخت در بندر کلاهی میناب، صادر و به پرداخت بیش از ۱۲۰۰ میلیارد تومان جزای نقدی محکوم شد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/670501" target="_blank">📅 13:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670500">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/710326a1fd.mp4?token=KXusA792UnewLAJDD1T8BgZIBzyYHMr4HpQ253FAcxi2BSfyz1xLXR1C7huwouyn8Ka8kau0G69R7K7p2xqc5LqDFXIpsGhqvUz9dvus09pW5OeAiv0L1CaLd7LxJ_v9hFXWWaTA30Cai1vk0aAJN4LUydvIlG4HAiCt6Zml2CTLd4owgZn6CtQAn5tyS43q3Y1ftWclHAPADUcV3IxiEOI7lBoiwCRvcJf7H7n2NFRYgQ53geXRsJxwHvWFyuvsNHOsG662IgGgB0fAF16T-l_Q8JNOkrnGLP1nya9RAbd8LV1swj7ld40D7sqgIgzuU6SrIj-bCDVZ_6Xkj63uyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/710326a1fd.mp4?token=KXusA792UnewLAJDD1T8BgZIBzyYHMr4HpQ253FAcxi2BSfyz1xLXR1C7huwouyn8Ka8kau0G69R7K7p2xqc5LqDFXIpsGhqvUz9dvus09pW5OeAiv0L1CaLd7LxJ_v9hFXWWaTA30Cai1vk0aAJN4LUydvIlG4HAiCt6Zml2CTLd4owgZn6CtQAn5tyS43q3Y1ftWclHAPADUcV3IxiEOI7lBoiwCRvcJf7H7n2NFRYgQ53geXRsJxwHvWFyuvsNHOsG662IgGgB0fAF16T-l_Q8JNOkrnGLP1nya9RAbd8LV1swj7ld40D7sqgIgzuU6SrIj-bCDVZ_6Xkj63uyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از شلیک موشک های قدر، عماد، خیبرشکن و ذوالفقار در پاسخ به تجاوز ارتش تروریستی و کودک کش آمریکا در سحرگاه و صبح امروز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/670500" target="_blank">📅 13:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670499">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e0259577f.mp4?token=cDhEjMwakKNhMH-hRmB90t9ZZUZoDX6z9MC0dqRzqGvcx1sxsS37luBh8VlW_kFC--AuQhFO53TpqHiwb_R6YuoAYv6vPyvm98PFBXIPSxNvqbDi9iZpk9s_uj-_fdS3iYagU2Pnk8JLunKghGZz5GXoOp7mUUUsgEwztPbiMX7dgQ9CcilvNI390Y6yAQg7RHPMsCrvdM2DuB8H_-GCrF0TS3Oe-jebhxnSkzWxfSmAqA3xbblvSNWjXHwzp72zSEAaUbzLdgx5nbIAtcSZutGeDmE3-ghipZnNZq_Sv428B15C__xMSTtK3Z_AzS6Wr2I5ziJxn2mNI4keXcR7VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e0259577f.mp4?token=cDhEjMwakKNhMH-hRmB90t9ZZUZoDX6z9MC0dqRzqGvcx1sxsS37luBh8VlW_kFC--AuQhFO53TpqHiwb_R6YuoAYv6vPyvm98PFBXIPSxNvqbDi9iZpk9s_uj-_fdS3iYagU2Pnk8JLunKghGZz5GXoOp7mUUUsgEwztPbiMX7dgQ9CcilvNI390Y6yAQg7RHPMsCrvdM2DuB8H_-GCrF0TS3Oe-jebhxnSkzWxfSmAqA3xbblvSNWjXHwzp72zSEAaUbzLdgx5nbIAtcSZutGeDmE3-ghipZnNZq_Sv428B15C__xMSTtK3Z_AzS6Wr2I5ziJxn2mNI4keXcR7VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این روش آسون و خلاقانه سرخ کردن سیب‌زمینی، مهمونات رو شگفت‌زده کن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/670499" target="_blank">📅 13:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670498">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRbvwugMO_u5RYEEGAyWDGMVfYF8IKFd9cwDl0Unxp-fObMFGhgk9mB97w10bqGWC3WEtyikyrez2iiJaGlw1TVHGT50dzvEg_atF78wjEclefmIpjOhShqjJJHhI82EE4VHvY6ttiHHMx8FBMySU4cmJw2c8gIP-PucGYbKmmOU_Q7d1ult3ifQjFm-jav1zzAvNxj1y-jvel6wylVavCNf_Ti-DQ3DeCQ7A3mav888ecXi10YyOnV9eW5MTaA7ysS3ZzIhXnTf5AmrKd65Y0rUFDMws9Q5qeAGCWTyDjAbAFT4I4kmdic7rCBXNpV9nAkGIMUEyW7JXgYJIc61uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ با ایران فاتحه دبی و دوحه را خواند!
🔹
تازه‌ترین گزارش شاخص جهانی زیست‌پذیری اکونومیست از افت قابل‌توجه جایگاه شهرهای خاورمیانه، به‌ویژه حاشیه خلیج فارس پس از جنگ با ایران خبر می‌دهد.
🔹
در رتبه‌بندی ۱۷۳ شهر جهان بر اساس شاخص‌هایی چون امنیت، سلامت، آموزش، فرهنگ و زیرساخت، دوحه با سقوط ۷ پله‌ای به رتبه ۱۰۸ رسید.
دبی و ابوظبی نیز هر کدام چهار پله تنزل کردند و به‌ترتیب در جایگاه‌های ۷۹ و ۷۶ قرار گرفتند. /خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/670498" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670497">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
ارز اربعین از بازار آزاد گران‌تر است!
🔹
با کاهش قیمت دینار در بازار آزاد به ۱۱۰ هزار تومان، نرخ ارز اربعین به نزدیکی ۱۲۹ هزار تومان رسیده است./ فارس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/670497" target="_blank">📅 13:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670496">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
ژاپن به‌دنبال ایجاد سازمان اطلاعاتی متمرکز با الگوبرداری از غرب
🔹
ژاپن برای نخستین بار از پایان جنگ جهانی دوم، با کمک متحدان غربی در حال ایجاد یک سازمان اطلاعاتی متمرکز است؛ نهادی که گفته می‌شود با هدف مقابله با تهدیدهای فزاینده به‌ویژه از سوی چین و روسیه تأسیس می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/670496" target="_blank">📅 13:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670495">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnpTKCH_ayeabqMroPJoQGjPhT-dbtITXPe-toPNfR-QjoZzRROAPHHDIKFruduHIeG0l6ErGMBF8ItKS7U9h-N6vTyATnTmzQeWApIyAAZ4DfcaxkMfA5BWRmKQ06TFB-nKGaHTpKIABBB3zMQW5ecw4ODMOIthyJW6VUEulxtThLKA-J4stxrm331U04-HnqVW3Wyyc7epNp4AIA9VEVsr77HFkGCEirs4IkcPT3-ddl7kF5RhXqEc2yolBhjFelxDKQ9ixI7J8m0M2T3PLVJ-ae9otz6dNv_bVvVtKYGZbxzmScdDGQK9_6G9AqLUdzO2MEaj-VmN4J9pK4-iQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۲ تیر ۱۴۰۵؛ ساعت ۱۳:۱۰
🔹
قیمت دلار امروز در واکنش به درگیری‌های نظامی ایران و آمریکا در تنگه هرمز و انسداد مجدد آن توسط ایران، آرایش صعودی گرفت و در آستانه ورود به کریدور ۱۸۰ هزار تومانی قرار گرفت./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/670495" target="_blank">📅 13:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670494">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
چین خواستار عبور آزاد و ایمن از تنگه هرمز شد
آناتولی:
🔹
چین در بحبوحه حملات نظامی مجدد بین ایالات متحده و ایران، درخواست خود برای عبور «آزاد» و «ایمن» از تنگه هرمز را تکرار کرد.
🔹
لین جیان، سخنگوی وزارت امور خارجه چین گفت: «تنگه هرمز تنگه‌ای برای دریانوردی بین‌المللی است. از سرگیری عبور آزاد و ایمن در این تنگه در اسرع وقت به نفع همه طرف‌ها است.» /خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/670494" target="_blank">📅 13:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670493">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
خیلی ساده و بدون هزینه از این دمپایی روفرشی‌های ترند بساز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/670493" target="_blank">📅 13:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670491">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
دارو ۵۴ درصد گران شد
🔹
با اعمال موج جدید افزایش قیمت دارو از نیمه فروردین، میانگین نرخ داروهای تولید داخل ۵۴ درصد رشد کرد.
🔹
در این میان، اسپری‌های دارویی با جهش ۱۶۳ درصدی و ویال‌های تزریقی با افزایش ۱۲۷ درصدی، بیشترین رشد قیمت را ثبت کردند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/670491" target="_blank">📅 13:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670490">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pv_smMJB0AMyqWVXCkIO56WjZ52woMCsFrZObiopj8Qx5AGYgpdWtSt2pqjtLPej9Zi5VM1MMFIGB3AlXCYn8jLfEEtc5hisZcQuJCuJynkVF7iUnAvmJ8En0tie7FAjJzPdf8O6jAHxCBxV7cZZY8Ch8WU6_FR9Le0BXzEYW1HaIRamwtkne5_we_KeN7bWRiXTmEmWC6zPnwsio3Z3_bk_GOAVNS0q80JCqOUQQNldboSOHLGZwu5vAnIddhV69_A-L-87SDiWxTveLRU-QS0LiGwr4Rtxj4EmYgAI_xTXA01P72tqYdIOKb38FKM7eWJi3sCOdOGbjXpzGOUymQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر منتشر نشده از شهید محمد ضیف
🔹
عزالدین قسام، شاخه نظامی حماس در دومین سالروز شهادت محمد ضیف، تصویری از او را منتشر کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/670490" target="_blank">📅 13:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670489">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
گمرک بازرگان مجاز به ترخیص خودرو شد
🔹
براساس ابلاغیه گمرکی، گمرک بازرگان به فهرست گمرکات تخصصی مجاز به ترخیص خودرو اضافه شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/670489" target="_blank">📅 13:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670488">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b4de78a1.mp4?token=vRzYs_1qQMSAWKaOvqwWa8u4qOiMdVk3OpwACjcqI8f3cgWRAvKKE6c8VQhQHFjjV7ImwGC04HTE71PtCRhvT8EqStOTjkqz7sIxVMC3LCpO3N15_cFlSnZnpg7NxgTN2wbDDDiueRm7Cb2UUbnv8k0gTQ6WEsYm2rbP8aEiJfuOKe0iETwuSSzwQ1XS2hTF6au_6sMx7txWqpWqPYEnQD-ffI3aAO10XO99AFwggStE-pT9-GeTipT3RMMNycdx9xnyhkkwAGBQeStuw4gMXpWDDAkO9n78Fw58FU44jfkY-jpay8Ls-e0mTiZVoHK6_vnd95-OR5LiWl-ijyqoWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b4de78a1.mp4?token=vRzYs_1qQMSAWKaOvqwWa8u4qOiMdVk3OpwACjcqI8f3cgWRAvKKE6c8VQhQHFjjV7ImwGC04HTE71PtCRhvT8EqStOTjkqz7sIxVMC3LCpO3N15_cFlSnZnpg7NxgTN2wbDDDiueRm7Cb2UUbnv8k0gTQ6WEsYm2rbP8aEiJfuOKe0iETwuSSzwQ1XS2hTF6au_6sMx7txWqpWqPYEnQD-ffI3aAO10XO99AFwggStE-pT9-GeTipT3RMMNycdx9xnyhkkwAGBQeStuw4gMXpWDDAkO9n78Fw58FU44jfkY-jpay8Ls-e0mTiZVoHK6_vnd95-OR5LiWl-ijyqoWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات شبانه اوکراین به زیرساخت انرژی روسیه
🔹
در ادامه اصرار اوکراین به زدن زیرساخت انرژی روسیه، تأسیسات نفتی در مناطق استاوروپول و کراسنودار هدف یورش پهپادی قرار گرفتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/670488" target="_blank">📅 13:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670487">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
مهر: شنیده شدن صدای انفجارهایی در حوالی بندرعباس و قشم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/670487" target="_blank">📅 12:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670486">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ادعای چین: تردد آزاد و ایمن از تنگه هرمز به نفع تمامی طرف‌هاست
.
🔹
پیش‌ثبت‌نام دانش‌آموزان پایه هفتم به صورت غیرحضوری از طریق سامانه «
مای‌مدیو
» است.
🔹
گرما، جان ۱۰‌هزار اروپایی را گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/670486" target="_blank">📅 12:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670485">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
مصاحبه اختصاصی خبرگزاری وایس آمریکا با فرزند شهید تنگسیری و دلایل بستن تنگه هرمز و حمله به کشتی ها در تنگه هرمز از زبان ایشان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/670485" target="_blank">📅 12:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670483">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YFHyIzq_SU1iO12Is6FSsWn3t_th5Wt1yEI_ZVB5W3XQR6uIAO2wtqbdoeeQRTYh2SofECwU46uQyiXFcM1KF_P-xF1QmB357BMP5BsuPXqG7636h7xZgddk_et2igxz0PyaNhhHW2rhR6dBXAvvHRG0D6hwgDAoxvxu86XzdegWpHo8DEEnTwreXfPbe2XWHYHVJ_J-TGZIkrF4gZFbK952Doq6UapVXipd8IfqSo-NBtfk1fNlojRbM0MYm7fvZeyjutekkGoT_kf-KPCGpfJHI3jXvzi41DJMCDSfuYc4IM322zAmExUc6XekK4kl2Wr-B3FdMnusax8Mm-qaHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qkHMAtmPxj-Q7-J5b4CKNTW3FeUICH7Shl8igrlrPVi3842lsIUPUT_1mh0rKC_PCfTiC9lFqlzdX2pyCSzRxpQ3p0nYdLzBX9f6gii0UBqcOK65SjSIlBGKAuMh6vh1FQ6E-4hOTIavo6eLU6bpTqr7Hx1ma8rH-BZICWDzJxZ6Xfcc4gs5OgR5FsaXFFJAMG4MNsWLtK7V1hbZtD0ITm6krLzOtIJUDM6Q20CYOaCoTHU3w-p-_CRQlbF11K2EM1h4kG4bkhZPIBYWLUgFGhZgaa81On5z3irYrsjOsM2qiFwpdOTNnn8GJY553gQOECOf2g5bVZbHO_d52cpKNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آتش سوزی در جزیره خارگ رخ نداده است
تانکر ترکرز:
🔹
گزارش‌های آتش‌سوزی یا حمله به جزیره خارگ تأیید نشد؛ تصاویر ماهواره‌ای نشان می‌دهد افزایش حرارت ناشی از مشعل‌سوزی برنامه‌ریزی‌شده تاسیسات نفتی است که از ژانویه ۲۰۲۶ تغییری نکرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/670483" target="_blank">📅 12:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670482">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
محسنی اژه‌ای: اگر کسی در حاکمیت کار مردم را لنگ گذاشت قابل بخشش نیست
🔹
باید زمینه‌های فساد را از بین ببریم و اعمال فسادزا را خنثی کنیم؛ از ما توقع می‌رود مطالب را درست برای مردم تبیین کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/670482" target="_blank">📅 12:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670481">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf18d1a26.mp4?token=J6skzmq_lB8fAmkdNAnOgkVOZuWIL3itVMzaxSxHsZbLzgB3sGlpP9i4mPWUQbmFv3NZFxWf_XQgbnPr6Pv_VawfytGAS-ipch58u4HXQD1T404zCwDSEjbyllfl2gAQySCIZNPs1KjlMpLrb_Q-muflxcHbtgIs5s5u0ryf3RoKSerme0u9rdvZProm4ElK3iaRpl3vAt8gMhIqRRZ5tyjK-eFT6zhOrAhSjkQiPCk9Gy01jtZ72Rgb9NtYDnEM23aLJmHPJSJ9AAPWFPXPYY3M2axrLbYqk3xO20pVxz5X8QjFQzBchKBm0pnYs4j5jNBsOPJHZV0ZV0YAxAM_Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf18d1a26.mp4?token=J6skzmq_lB8fAmkdNAnOgkVOZuWIL3itVMzaxSxHsZbLzgB3sGlpP9i4mPWUQbmFv3NZFxWf_XQgbnPr6Pv_VawfytGAS-ipch58u4HXQD1T404zCwDSEjbyllfl2gAQySCIZNPs1KjlMpLrb_Q-muflxcHbtgIs5s5u0ryf3RoKSerme0u9rdvZProm4ElK3iaRpl3vAt8gMhIqRRZ5tyjK-eFT6zhOrAhSjkQiPCk9Gy01jtZ72Rgb9NtYDnEM23aLJmHPJSJ9AAPWFPXPYY3M2axrLbYqk3xO20pVxz5X8QjFQzBchKBm0pnYs4j5jNBsOPJHZV0ZV0YAxAM_Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای مسیر پیاده‌روی اربعین از بصره تا کربلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/670481" target="_blank">📅 12:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670480">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbVFu8l9Jriq8g6zR0IA0ytCNSK-Wmhe_joPAjr72ApctTprHuJQcbQGLyaSJ6aYDnqSg0otXSlo0uYjQHzk8WF_F4_NOYsfiNYcr88ZGQk-Co6RYez9R6B0iy7HGxc07aMI6Z7GjXOTfJm72m8_FrZCm6sk-BRYRWO7SQSw6EFigbfIt9lAa2AbgDCppUyUQIkvAMZTCdetQYtHgs4HRuX_xWONEjlNb1cjBgJAGBTzFF9au2ExkDzEVOeP8Ns0wCDIPigMkGn33jxJKYftH2HrbaAfeHiHQ3O2_CsMWYa4t4ObyHTy06O2WM-rAwh-b7ohIdAUz9AQwCJCtMi12A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ریزش بورس به زیر ۵ میلیون
🔹
شاخص کل بورس در پایان معاملات امروز با ریزش ۸۹ هزار واحدی به ۴ میلیون و ۹۶۷ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/670480" target="_blank">📅 12:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670479">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
جزئیات از حمله ارتش تروریستی آمریکا به تاسیسات آبی خوزستان
🔹
مدیرعامل سازمان آب و برق خوزستان از حمله بامداد دوشنبه ۲۲ تیرماه به ایستگاه پمپاژ زهکش RMD در محور ماهشهر–هندیجان خبر داد. در این حمله، «شاکر محیسنی» به شهادت رسید و یکی دیگر از کارکنان مجروح شد.
🔹
این ایستگاه نقش حیاتی در مدیریت زه‌آب اراضی کشاورزی منطقه دارد./مهر
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/670479" target="_blank">📅 12:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670478">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5RqR4vsBh9PoFd76zEZiRkD59sBiB1aeEUq3aGQURTcLQFy59jgN7W8aATgAiY9hg2lEqYLW-fLRNklBbLsar9De0TfCOESrVcg0k00yOd5Vi9yVsTJNFzO_X5Up9lgRkYx3vKyO0G_zIrpjLUHoCV1kYl5OoIXEUSQ0G6laErkqQFQDCrIyPfk1iNQtAJtQgn7wwFvam8vmDi8dndz1FeqQKj0H8u0p6-y_1fF6kpowD2DkNbJKbXRP2OC_EeADgOSRXU-q1oxVpkA2AUP40_pYEG2_iI3Qt779CCpz475tGiODfDxcpGao-oIL9AyYQp81R-C8MGS4c434YjESg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دولت بحرین دو نوجوان را به جرم شرکت در عزای حسینی مجرم شناخت و زندانی کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/670478" target="_blank">📅 12:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670477">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e33e67c24d.mp4?token=b3xHVnJHNP5laLsCKKkpvzxPegD5asQ-uFPKoxnjd8HiRH2DJWLR44vqsbIo3ZX4Y7BIbBk3qtnEd5o0piP1vRRZ8Qsya6Q3tqfOXQQtFjz3g3NpWl7qVIlCsXQj3yA9csuKeIEnND_7lYtgzbqRt9t1WoUgSxDnMC2o87Te5WvR1hsCWOEW4mZf5meS9PpbxZ2reGYEcSJjE1CvLVmj2VNLMQENUTNRCCf8KqmugWDXZS26dWfYInS519HPKOc4hPS-9laqcud7wwfnVybjGCtdeYbS_1mxTzpxDhggmLDrziCUANncpbPE3ZpRnNMqUf97whMz1cQSdZjGEGL8yIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e33e67c24d.mp4?token=b3xHVnJHNP5laLsCKKkpvzxPegD5asQ-uFPKoxnjd8HiRH2DJWLR44vqsbIo3ZX4Y7BIbBk3qtnEd5o0piP1vRRZ8Qsya6Q3tqfOXQQtFjz3g3NpWl7qVIlCsXQj3yA9csuKeIEnND_7lYtgzbqRt9t1WoUgSxDnMC2o87Te5WvR1hsCWOEW4mZf5meS9PpbxZ2reGYEcSJjE1CvLVmj2VNLMQENUTNRCCf8KqmugWDXZS26dWfYInS519HPKOc4hPS-9laqcud7wwfnVybjGCtdeYbS_1mxTzpxDhggmLDrziCUANncpbPE3ZpRnNMqUf97whMz1cQSdZjGEGL8yIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جورج گالاوی، سیاستمدار مطرح انگلیسی: لیندسی گراهام مسئول ریخته شدن خون میلیون‌ها نفر است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/670477" target="_blank">📅 12:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670476">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKYy73x7kQO4xuD9Ogt0UzK1BjltTQWxxrxWUzn1kb4UHyGI0h4oApvOWnq-0jCTHmxHPtbt52PxnBwsQ0LjUeS-zwe1I2oDDiG4RF5sqkt0cwuxnfF5JamjiUYzaoZQ2Z60DyOuZpZR1IOLM69uscERdFYbbQst4D9HOWcbRUB1vcGKD27My0VrJXTR6mCgmHHX7IpcLvvQUFrxcbRDjQgheQ1NTG07c0_owocOcELeUCNBz-9k368hjRLnV03h3gnmtN4lRQapHrNzRctUo3gAA-47o9hZYamtQcHSlFENYGIArVmWHJ3sMDM_yf0yfVbPD-tDFvsym2nN16_eaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سم نیل، ستارهٔ پارک ژوراسیک، درگذشت
🔹
سم نیل، بازیگر سرشناس نیوزیلندی که با نقش‌آفرینی در فیلم‌های ماندگاری چون «پارک ژوراسیک»، «پیانو» و ده‌ها اثر سینمایی و تلویزیونی به یکی از چهره‌های محبوب هالیوود تبدیل شد، در ۷۸ سالگی درگذشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/670476" target="_blank">📅 12:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670475">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
حمله دشمن به منطقه‌ای در محدوده شهرستان نایین‌
معاون امنیتی انتظامی استاندار اصفهان:
🔹
در دقایق اولیه بامداد امروز دوشنبه ۲۲ تیر، حمله دشمن آمریکایی به منطقه‌ای در محدوده شهرستان نایین، یک شهید و هفت مجروح در پی داشت.
🔹
مجروحان به‌صورت سرپایی مداوا و اوضاع تحت کنترل است.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/670475" target="_blank">📅 12:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670473">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QghoFsjUwxpfJApow3DikuaJpAh08sE4IaW_1MAWMxpZaHBslytJrXZ-j8sqY2QlvOjSfHaswrN_BSl4rKexesnekcKTf4GAKSSkwK3ryuGxkJCjGR6dSM6E-o7YcDZ4GiHki_s9XFpaDPywQ5pv5gG2MJTuPh984O-EVxhC1_AWK16a-Vovb1WUSTFiSGqCXPw_uf02h0w6PZIPUvo-7a6JceNj_8BVKcqh6WyPjDgaIDnt1GRxTlVQfZ-eVbmqhpwRxjS6Ll4so-Q9BIlWZqImpnR1HvI2AoGrHewEVGacRe_AomcOIPsnCreBH14SG1ZwyuQRE1tZ0gvinrEJ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران کدام نقاط کلیدی آمریکا را زیر ضرب برد؟
🔹
در پی نقض بندهای تفاهم‌نامه، ایران مجموعه‌ای از اهرم‌های اقتصادی و نظامی خود -از انسداد تنگه هرمز تا هدف قرار دادن مواضع زیرساختی، لجستیکی و کنترل دریایی آمریکا در منطقه - را فعال کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/670473" target="_blank">📅 12:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670472">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
بقایی: سفر لاوروف به تهران در حال برنامه‌ریزی است
.
🔹
توزیع کارت آزمون ارشد آغاز شد.
🔹
علی‌اف: روابط میان آذربایجان و روسیه عادی شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/670472" target="_blank">📅 11:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670471">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3914cfc6.mp4?token=ekZ82yKXSNAYh5J9k2K3V85EeoHA4CMu50SXq8EY36mLeC6egO1PCdxVD9apTXJt9nn7oV1pgpO5LTY3iH5KT6bKM8EHIKzv1B6D3FsAoeQtsXbfLjy97RXtx6aUGXmy3_iLU8e2-3WU1VNhK-ThTiW7DspMI9vSqdBLGLJ03ZNqPeY0pkr426XEMB46QFooru6xxssiPgArqcaF4ZXewXa_iqRNKv5iLtnDcw1hXoq5gvL4YWLLTokJWS-FuhWrsX9fuGDymCcG1621QA7CmnGk_XVSDEbvTlbrYeX720O9q4frQ9OYhBURRiPCic040VhtMqfZoF6kAbAO-OtiaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3914cfc6.mp4?token=ekZ82yKXSNAYh5J9k2K3V85EeoHA4CMu50SXq8EY36mLeC6egO1PCdxVD9apTXJt9nn7oV1pgpO5LTY3iH5KT6bKM8EHIKzv1B6D3FsAoeQtsXbfLjy97RXtx6aUGXmy3_iLU8e2-3WU1VNhK-ThTiW7DspMI9vSqdBLGLJ03ZNqPeY0pkr426XEMB46QFooru6xxssiPgArqcaF4ZXewXa_iqRNKv5iLtnDcw1hXoq5gvL4YWLLTokJWS-FuhWrsX9fuGDymCcG1621QA7CmnGk_XVSDEbvTlbrYeX720O9q4frQ9OYhBURRiPCic040VhtMqfZoF6kAbAO-OtiaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ما در فرایند دیپلماسی دست‌بسته نیستیم و استفاده‌هایمان را از این زمان کرده‌ایم و خواهیم کرد
🔹
می‌دانستیم که آمریکا پیمان‌شکن است و با علم به این موضوع و با چشمان باز از ابزار دیپلماسی استفاده کردیم.
🔹
مردم ایران تجربه تلخی از پیمان شکنی آمریکا دارند و برای ما دیپلماسی یک ابزار است و مردم ایران حامی تصمیم گیرانشان هستند؛ شیوه و کیفیت مذاکرات دیدگاه طبیعتا متفاوت است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/670471" target="_blank">📅 11:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670470">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f188a0d7db.mp4?token=qGKulgnFLHL1tzRI386G762SObRWlrf5BJNHqulf5onGmyM6tPtMPhUfJr22S2p7Y7-CEqfF_mKt9sKBImh9_0CvxXhavyoP_6f--aJsLn7q3omTyCWEMG7_q3UrkJkLIg-nbfYygQMMl069MDZRcHeb41pDr6BShzmdGeH9kRzJdBCl4GyahZdsSPU_HXyGfNQ30U5ETrH9oNxfIFVE0pnkxGdjwLiTFZd3hA7IuyxJ1Re9FqLjmOC2B6iBO9_3TCWK160yzoMWDbgbwpzgP19WpliYIzKnMGuLB5N3oanYX1pqM8CWEvKfyeB_VUiesrp-d2QKtti_1e-YL7_jwSkPiJFL1O1K4tkWSTyM4atxmkE_3kS9XL5bHwwBbKxlptZk2k53ESmesQ62R8uwSzZcQ9WmBrhRPL98WNwMM8hsZpLhnaE5T5NStQB42aZEqWElV9Ds-uGnaBxlnGGtX5wb_X6QDCwXOP-aoYGs_SqL0WnFmjE13X_9prQPtoSlBotxuat5R8Yi5g70HEsj-UM9k0JIPWBf3dD42UuuO-7ld2Jsru-cRX-m1m3gD2U4wSirl27iyGGVi3G2rdQidVNr1THRbT2_a_O-qAT5E1PXcNp6_mGWuu_A5q2IMptWRZ8UICPh9GxxMQ1Xpv6PeAJktsQgIFOxubRukIK1jbU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f188a0d7db.mp4?token=qGKulgnFLHL1tzRI386G762SObRWlrf5BJNHqulf5onGmyM6tPtMPhUfJr22S2p7Y7-CEqfF_mKt9sKBImh9_0CvxXhavyoP_6f--aJsLn7q3omTyCWEMG7_q3UrkJkLIg-nbfYygQMMl069MDZRcHeb41pDr6BShzmdGeH9kRzJdBCl4GyahZdsSPU_HXyGfNQ30U5ETrH9oNxfIFVE0pnkxGdjwLiTFZd3hA7IuyxJ1Re9FqLjmOC2B6iBO9_3TCWK160yzoMWDbgbwpzgP19WpliYIzKnMGuLB5N3oanYX1pqM8CWEvKfyeB_VUiesrp-d2QKtti_1e-YL7_jwSkPiJFL1O1K4tkWSTyM4atxmkE_3kS9XL5bHwwBbKxlptZk2k53ESmesQ62R8uwSzZcQ9WmBrhRPL98WNwMM8hsZpLhnaE5T5NStQB42aZEqWElV9Ds-uGnaBxlnGGtX5wb_X6QDCwXOP-aoYGs_SqL0WnFmjE13X_9prQPtoSlBotxuat5R8Yi5g70HEsj-UM9k0JIPWBf3dD42UuuO-7ld2Jsru-cRX-m1m3gD2U4wSirl27iyGGVi3G2rdQidVNr1THRbT2_a_O-qAT5E1PXcNp6_mGWuu_A5q2IMptWRZ8UICPh9GxxMQ1Xpv6PeAJktsQgIFOxubRukIK1jbU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرف‌های بی پرده یک روحانی: بسیاری در لباس روحانیت زندگی یک نسلی را نابود کردند و وجهه دین را نیز خراب کردند
/ تلویزیون اینترنتی مدار
این گفت‌وگو را در آپارات ببینید
👇
▫️
https://aparat.com/v/qypc186
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/670470" target="_blank">📅 11:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670467">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ecf0c49d7.mp4?token=IUdogZg9PKns1okdzWktQpijpuOwgtA79-wxtDuz5GXK5hkUCf4Lz8aV3z9-UzuXlITFHwyA8Re4qVuxYg2cO9o-fGcVvmldxhGginUw_FMhBSAU_1iuMZYhfnv5IwvJKgCEh06RkQN-ikkB0vtUCRSrhLubnOJ6wpmSFN9P6OaxP3JUEXsrgqFr2roPXkael-hDRSuZRShb1o0N1u8uOjs0ofk6-aVN2iKWkqXfhBphrZ1TAl0T726eyd_Pc2Y1x5e40J19e8sVHOSnqayUBnh9hiaDpp2fcW7hI0qyZZHzefqCcuEDQH5_N2ta3M62GdQ2QJ6ZoTQ_nVehbN-eFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ecf0c49d7.mp4?token=IUdogZg9PKns1okdzWktQpijpuOwgtA79-wxtDuz5GXK5hkUCf4Lz8aV3z9-UzuXlITFHwyA8Re4qVuxYg2cO9o-fGcVvmldxhGginUw_FMhBSAU_1iuMZYhfnv5IwvJKgCEh06RkQN-ikkB0vtUCRSrhLubnOJ6wpmSFN9P6OaxP3JUEXsrgqFr2roPXkael-hDRSuZRShb1o0N1u8uOjs0ofk6-aVN2iKWkqXfhBphrZ1TAl0T726eyd_Pc2Y1x5e40J19e8sVHOSnqayUBnh9hiaDpp2fcW7hI0qyZZHzefqCcuEDQH5_N2ta3M62GdQ2QJ6ZoTQ_nVehbN-eFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش جالب بقایی به اظهارات وزیر امور خارجه فرانسه درباره ایران
🔹
وزیر امور خارجه فرانسه دوست دارند هر از چندگاهی صبحتش در نشست سخنگویی انجام شود.
🔹
فرانسوی ها باید یاد بگیرند درباره مسائلی که به آنها مربوط نمی شود انتظار نقش آفرینی نداشته باشند.
🔹
اروپایی‌ها نباید رویکرد مهدکودکی خودشان را به دیگران تسری بدهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/670467" target="_blank">📅 11:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670466">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58e81135af.mp4?token=BDOqjrpI9pkVzRaMKYBcvwBohoOoVCSayRmsfvw8Kh5ggRUG2hvdiuXjnWhaa_w4jiisufILdFdEfefiWeH1Ygm96eOxDG4s82jdj6sOB7uWaL0vbdLEsgEvGX3Wd5Tbh8-6F8ZzJzmpFuyEIaZAClHzDFNjRq0sNCAxL1z8TyGxDnHiHuzOayhA3tgJJZ2aiRcaTxy-YyoVN5gwOjDqMYEgzZi3eAwnnuMHlVU3YbXAdHpuu_evmnVGFVmoWnrtCtjRa_kczf2XwVyib-ABxFZdlyedyY6gFsTxe7bm6AEZDzjThFonCV-voNv1zoF07QTxx02aQEeoqvVmt7tD5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58e81135af.mp4?token=BDOqjrpI9pkVzRaMKYBcvwBohoOoVCSayRmsfvw8Kh5ggRUG2hvdiuXjnWhaa_w4jiisufILdFdEfefiWeH1Ygm96eOxDG4s82jdj6sOB7uWaL0vbdLEsgEvGX3Wd5Tbh8-6F8ZzJzmpFuyEIaZAClHzDFNjRq0sNCAxL1z8TyGxDnHiHuzOayhA3tgJJZ2aiRcaTxy-YyoVN5gwOjDqMYEgzZi3eAwnnuMHlVU3YbXAdHpuu_evmnVGFVmoWnrtCtjRa_kczf2XwVyib-ABxFZdlyedyY6gFsTxe7bm6AEZDzjThFonCV-voNv1zoF07QTxx02aQEeoqvVmt7tD5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش سخنگوی وزارت امورخارجه به ادعای ترامپ درباره درخواست ایران برای مذاکرات؛ طرف آمریکایی صادق نیست و یک بازی روانی است
بقایی:
🔹
ایران با میانجی‌ها در تماس است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/670466" target="_blank">📅 11:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670465">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
نیوزویک: ایران ترور ترامپ را برون‌سپاری می‌کند!
ادعای نیوزویک:
🔹
تلاش‌های ایران برای ترور در خاک ایالات متحده معمولاً شامل برون‌سپاری واسطه‌ها می‌شود.
🔹
تهران به جای استفاده از عوامل آموزش‌دیده خود برای حمله، از منابع خارجی استفاده می‌کند و واسطه‌هایی را برای استخدام شبکه‌های جنایی محلی یا افراد مسلح اجیر شده می‌فرستد که امکان انکار را فراهم می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/670465" target="_blank">📅 11:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670461">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe9610fe89.mp4?token=Os-taGKIvTf-NJDwcbniHge1989TB4WpN8dqHDcdTyzqaHg-7KreZYwJ1VrhNN851UIUSGPP0HH-z3GwGpl0lwG0rPWdKBaluh3jYFhJrxvrCHAc4dkdxDrc5CFQT8Wz1pVE-mDsXons4aY6hopMAKcDd-5XS6D17A8kQYiAFAMZ4bf9L8WA8-oYRG8YqQV_FeKsGXAHcOTUWWVOBHfz0amkdV9oTlHM1hHd4rI5PA3A64wTglghMnd0Qnh_X8sgfSNsCEy0BdxuTuHYsBGdnuIwcZLWeXfGUs1zFW7pnupni2UI163Asg0GrZs6jjn6gsck939A3c8YUEYsye_sFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe9610fe89.mp4?token=Os-taGKIvTf-NJDwcbniHge1989TB4WpN8dqHDcdTyzqaHg-7KreZYwJ1VrhNN851UIUSGPP0HH-z3GwGpl0lwG0rPWdKBaluh3jYFhJrxvrCHAc4dkdxDrc5CFQT8Wz1pVE-mDsXons4aY6hopMAKcDd-5XS6D17A8kQYiAFAMZ4bf9L8WA8-oYRG8YqQV_FeKsGXAHcOTUWWVOBHfz0amkdV9oTlHM1hHd4rI5PA3A64wTglghMnd0Qnh_X8sgfSNsCEy0BdxuTuHYsBGdnuIwcZLWeXfGUs1zFW7pnupni2UI163Asg0GrZs6jjn6gsck939A3c8YUEYsye_sFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◼️
بدرقه یار
◾️
پیام‌های صوتی مخاطبان خبرفوری در پویش «بدرقه یار»، آخرین جمله به رهبر شهید؛ بازتابی از ارادت، دلتنگی و وفاداری مردمی است که حرف دل خود را با رهبر شهید در میان گذاشته‌اند.
◾️
این صداها، بخشی از بدرقه ماندگار ملتی است که در سوگ، همدل و در وفاداری، هم‌پیمان مانده‌اند.
◾️
کانال رسمی سوگواره «بدرقه یار» را دنبال کنید
👇
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/670461" target="_blank">📅 11:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670460">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39700be49e.mp4?token=CtHOqgbjBEc73qRoQJ7psqb3cSDDcBzXTf8v2OOUR_X_Pn3ab7qOp6UERAfhqYLeiRyy1SSAFr7ZCc7X7jaVCRDu3N_59w0KWmYtNK_HWcc59eIrnjW9QX413pkUq7o42owC3y0W9CCT-RBpgBOBmOrS0Kxy6N4MgnfYL9JLPvRatyMG_WXbU3RgA_oggWMyBeUS_sWQs4Z2j_6OCLsFWNtz3rSnW9R55kaKFKeKqyQ2amFbnxHuZwQ3PCkT2o-D425rDTYNfoG_LC13avDmmGCN-3kbvsj2edNZYidOasm1M5CKbfT4V2jOKasyKp4f8m0sABjuk0lCUesU66vUbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39700be49e.mp4?token=CtHOqgbjBEc73qRoQJ7psqb3cSDDcBzXTf8v2OOUR_X_Pn3ab7qOp6UERAfhqYLeiRyy1SSAFr7ZCc7X7jaVCRDu3N_59w0KWmYtNK_HWcc59eIrnjW9QX413pkUq7o42owC3y0W9CCT-RBpgBOBmOrS0Kxy6N4MgnfYL9JLPvRatyMG_WXbU3RgA_oggWMyBeUS_sWQs4Z2j_6OCLsFWNtz3rSnW9R55kaKFKeKqyQ2amFbnxHuZwQ3PCkT2o-D425rDTYNfoG_LC13avDmmGCN-3kbvsj2edNZYidOasm1M5CKbfT4V2jOKasyKp4f8m0sABjuk0lCUesU66vUbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ منفی سخنگوی وزارت امورخارجه به ادعای گروسی مبنی اجازه ایران به آژانس برای دسترسی به تاسیسات هسته‌ای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/670460" target="_blank">📅 11:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670457">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/152f9f93c8.mp4?token=YU0D_8yNe_5ZK4M0L7mDyYIyLoR0Etk1G2EDf5Jst3lP0yFOW74q5f2hC1FH7TtrbTDlovWFxCzsPT6ROl3ouKfP74Sy-rT3CQbgsCOPZmyJBEuvGyEMT-LNQ8RhJzJKUtHBLeOlsGyujO1jV1AVHopDiy6W-tG97TASYTZmTGpEmoStQaMmij2zR_o5cD8s8Bf1E9ulVyX-MLCBO8SEwJYT4P07bElZSZbDte-iomwUGqYdcgkAMQSOAlBREmAtMx7QpjcXgvcTrrMJxmDiRn3E0qmc8_S2AXFjwtKCu2JNWiJ_mf0ztVEHFCg0M36YmSC_eqdWgc1CsblvFDm9nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/152f9f93c8.mp4?token=YU0D_8yNe_5ZK4M0L7mDyYIyLoR0Etk1G2EDf5Jst3lP0yFOW74q5f2hC1FH7TtrbTDlovWFxCzsPT6ROl3ouKfP74Sy-rT3CQbgsCOPZmyJBEuvGyEMT-LNQ8RhJzJKUtHBLeOlsGyujO1jV1AVHopDiy6W-tG97TASYTZmTGpEmoStQaMmij2zR_o5cD8s8Bf1E9ulVyX-MLCBO8SEwJYT4P07bElZSZbDte-iomwUGqYdcgkAMQSOAlBREmAtMx7QpjcXgvcTrrMJxmDiRn3E0qmc8_S2AXFjwtKCu2JNWiJ_mf0ztVEHFCg0M36YmSC_eqdWgc1CsblvFDm9nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا ایران دولت فعلی افغانستان را به رسمیت شناخته است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/670457" target="_blank">📅 11:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670456">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4368a18b89.mp4?token=BSRBfx7CM5V3EJnYhSexkShUq--h6zacgORQzw4-xErKEIvGBh0R4DxRJSnvfF-HtShrzrntAFMKR1R1siQR0-fZTipeyBsHZWu1LjQdTlHlFnRiKEPI8M4FRvdDo29CXvCN2aleB4PvBqIp-ujF8EeFfv62VrXp2w1zPnyAkaWlXzlgpEE_uHtQC7qfg7_dxAa5AZDyePIgw_4eh8Omr1j4RilSjus0_l2XygXPETYSK9WGvG7gkGCsCvTLLG2fcwHC08AquttXZg0dvgtHldOU6va4EseYuyKHZiLfVUpZTbDG1LWsWpjcpTIwZWikk5a7mdV7KFMdzGFNR0MRow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4368a18b89.mp4?token=BSRBfx7CM5V3EJnYhSexkShUq--h6zacgORQzw4-xErKEIvGBh0R4DxRJSnvfF-HtShrzrntAFMKR1R1siQR0-fZTipeyBsHZWu1LjQdTlHlFnRiKEPI8M4FRvdDo29CXvCN2aleB4PvBqIp-ujF8EeFfv62VrXp2w1zPnyAkaWlXzlgpEE_uHtQC7qfg7_dxAa5AZDyePIgw_4eh8Omr1j4RilSjus0_l2XygXPETYSK9WGvG7gkGCsCvTLLG2fcwHC08AquttXZg0dvgtHldOU6va4EseYuyKHZiLfVUpZTbDG1LWsWpjcpTIwZWikk5a7mdV7KFMdzGFNR0MRow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: به هیچکدام از کشورهای منطقه حمله نکرده‌ایم
بقایی:
🔹
کشورهای منطقه از وضعیت ۴ ماه گذشته که به‌دلیل حضور آمریکا به چالش کشیده شده، درس بگیرند!
🔹
مقایسهٔ ایران و رژیم صهیونیستی توسط وزیر خارجهٔ ترکیه حیرت‌آور است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/670456" target="_blank">📅 11:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670454">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e8effe0eb.mp4?token=OrDkf7mgW3_gNjC1qKGZAOy-ArjRLF9ekaCgJ7HkB0nrVCchJi0T1pNqcBAULFSlmQa5c6mH727dMwYix2yolWaHqHKA1uBRdQmJ9NzODkUaiEvzVP4tBeyrWZ1YpJ2jjItKlcfInESidpm5pwAq3U0sylOj5R5CaJG6NBSOS83SH-V_MSjodPNuqUpTF6rDgmRb2DXIuLkDQHQcKZ6AWQtJ-VQGiktrqp2tzvZSUXCYlnlW11sPvVwad4CrDkad5-ULI_fSbZ-xmZgKMFYo8TIFeJM-5abKUHdL8zhVIqZ5T6sGl3l3z5muZzlkW0V6uKeiEg0F7PJOthF2ayXHgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e8effe0eb.mp4?token=OrDkf7mgW3_gNjC1qKGZAOy-ArjRLF9ekaCgJ7HkB0nrVCchJi0T1pNqcBAULFSlmQa5c6mH727dMwYix2yolWaHqHKA1uBRdQmJ9NzODkUaiEvzVP4tBeyrWZ1YpJ2jjItKlcfInESidpm5pwAq3U0sylOj5R5CaJG6NBSOS83SH-V_MSjodPNuqUpTF6rDgmRb2DXIuLkDQHQcKZ6AWQtJ-VQGiktrqp2tzvZSUXCYlnlW11sPvVwad4CrDkad5-ULI_fSbZ-xmZgKMFYo8TIFeJM-5abKUHdL8zhVIqZ5T6sGl3l3z5muZzlkW0V6uKeiEg0F7PJOthF2ayXHgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: آمریکایی‌ها از روز اول تقلب کردند
سخنگوی وزارت امور خارجه:
🔹
آمریکا با تحریک کشورهای منطقه سعی کردند مسیر امن تنگه هرمز را دور بزنند و بند ۵ یادداشت تفاهم را نقض کردند و امنیت کشتیرانی را در منطقه به خطر انداختند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/670454" target="_blank">📅 11:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670450">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bb5b272db.mp4?token=q8uXDOoW5SSYOne_ENVuGldz-UldNLYGe0qpr2_n7UQaYorNtrDLP8KM223wPKA2qcNqHVgRGYAnjISKbwoe4pDhFAzbiZVHRSHQ85I7FXzAha6ZFevA3ykZqV38B3vYA3K9QrDY-9Y7YkhU1J26YGP1SDmS1D2pithtXLGb4BvZLZVyZ4ZNccwNyI_biZEqYu_764_Ya2CKzt-UFPmQrM8xcTUNeQ3a6-qpIg-12VK3YARy8ut0-sq0D3QbdRr9PU4k9qhzb1YHopprvxD0v-7ZKJdXTLvRQG7CdSNBGt0ZXGlcMffH8azsh3qr4tyYzuLyBsm-MRySoq1EOngNKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bb5b272db.mp4?token=q8uXDOoW5SSYOne_ENVuGldz-UldNLYGe0qpr2_n7UQaYorNtrDLP8KM223wPKA2qcNqHVgRGYAnjISKbwoe4pDhFAzbiZVHRSHQ85I7FXzAha6ZFevA3ykZqV38B3vYA3K9QrDY-9Y7YkhU1J26YGP1SDmS1D2pithtXLGb4BvZLZVyZ4ZNccwNyI_biZEqYu_764_Ya2CKzt-UFPmQrM8xcTUNeQ3a6-qpIg-12VK3YARy8ut0-sq0D3QbdRr9PU4k9qhzb1YHopprvxD0v-7ZKJdXTLvRQG7CdSNBGt0ZXGlcMffH8azsh3qr4tyYzuLyBsm-MRySoq1EOngNKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آینده تفاهم صلح اسلام آباد چه خواهد شد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/670450" target="_blank">📅 11:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670449">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8b85f616b.mp4?token=K9LzYxgz9hCJnOG41iqgdSz1Oy4Pol75nPrLQxbbLh9BwpN9K5L8s0pNXRcYBCWpnhVLXwAHMMNluOQ-52ibU0N1liKfCoaAtaez0LZMWDfwK2Cik3VG8t213slX6gWM-Gw-SrqOX_j7MZrlMV1MetrzhxGSWXNBCR6drEIX5I5is8AtZkBgR2phTJrCO9ua9-w76y_mdRsSY6Q9vbcj_ewHlAME3iclCGU7jKKmiz0m3I3JpEq4nfJL-7pxlLiFftCzJDGx-WihYUx8iYsvUWpv5NkZJAHwnwHmd5x0gSuakob77jzNPinlq8OlNpc2f2C-SXgn6tmYVk2csl-NQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8b85f616b.mp4?token=K9LzYxgz9hCJnOG41iqgdSz1Oy4Pol75nPrLQxbbLh9BwpN9K5L8s0pNXRcYBCWpnhVLXwAHMMNluOQ-52ibU0N1liKfCoaAtaez0LZMWDfwK2Cik3VG8t213slX6gWM-Gw-SrqOX_j7MZrlMV1MetrzhxGSWXNBCR6drEIX5I5is8AtZkBgR2phTJrCO9ua9-w76y_mdRsSY6Q9vbcj_ewHlAME3iclCGU7jKKmiz0m3I3JpEq4nfJL-7pxlLiFftCzJDGx-WihYUx8iYsvUWpv5NkZJAHwnwHmd5x0gSuakob77jzNPinlq8OlNpc2f2C-SXgn6tmYVk2csl-NQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: بی‌تردید تفاهم‌نامه وارد مرحلهٔ بحران شده
سخنگوی وزارت خارجه:
🔹
آمریکایی‌ها در پیمان‌شکنی این‌قدر کم‌صبر بودند که حتی اجازه ندادند بازهٔ یک‌ماههٔ تعهدات ایران دربارهٔ تنگهٔ هرمز تمام شود.
🔹
ما در مسقط صرفاً دربارهٔ تنگهٔ هرمز با عمان مشورت کردیم و اصلاً قرار نبود موضوع دیگری مطرح شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/670449" target="_blank">📅 10:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670448">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/866026ebb3.mp4?token=sLbDCaFQ8RMjnA8WTzwOM2twj69AHMzBmlAQkhcunqQwL9O-xPM6bPvUkQb2gsMZOLeBN1xXfxoVicPQkO3_lauAdOJOxx3qsvzASAJchSZB9ZTwekIi6U6Mw1glxlUqFj8PaK2ug6uQgek98f-YZqu8MGmYtO0Pt3ShFlEwbERljLswS_e7MKecL65y7_Amz67OTzHMwMOcA7-cvxzTg8-JeJdFXoYsE6khpAUu1GIKfM_JFygPch-6voQ2VehydgrSidZhvfvjBnFuN2QOy5Z0REBSj77poDoJ_qKQYbQoWpECZuiDfk5E4rhdfMAXHIRLo7NGDHoJq9oJhze9ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/866026ebb3.mp4?token=sLbDCaFQ8RMjnA8WTzwOM2twj69AHMzBmlAQkhcunqQwL9O-xPM6bPvUkQb2gsMZOLeBN1xXfxoVicPQkO3_lauAdOJOxx3qsvzASAJchSZB9ZTwekIi6U6Mw1glxlUqFj8PaK2ug6uQgek98f-YZqu8MGmYtO0Pt3ShFlEwbERljLswS_e7MKecL65y7_Amz67OTzHMwMOcA7-cvxzTg8-JeJdFXoYsE6khpAUu1GIKfM_JFygPch-6voQ2VehydgrSidZhvfvjBnFuN2QOy5Z0REBSj77poDoJ_qKQYbQoWpECZuiDfk5E4rhdfMAXHIRLo7NGDHoJq9oJhze9ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت امور خارجه: خون‌خواهی رهبر شهید ایران یک مطالبه است
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/670448" target="_blank">📅 10:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670444">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d0736354.mp4?token=TBzh1jSdaGpTHK0mEE0pnvfyLh-ET63eoVT1WL8vFdrqWujHz72GJwOfNB0gvRi3IspKAPPjV6dWjzdHxIk0ynJOEb3FAmE54AOAiwgESAaCkcP55H2RufVJtkHyG5OvHlEZEge6NQlgaixfQ3yFxEhKEeZbsWqVPlGqCG-jGbaVeFVqs6RSyHlJFc8atngZglEb9epiMFUamgen6_6Aud3gPfUxjHb7UzgFnoPgSNUHrpnELIj3edckRQ8M5LIjIoXJ6fpcV975eLt_gTY-uE1w_cCBWp8YNsb4oDpVO7-u3LuDC81XaN2n7TqYaL25g3Xu_uvtbuNDoQVS5wycLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d0736354.mp4?token=TBzh1jSdaGpTHK0mEE0pnvfyLh-ET63eoVT1WL8vFdrqWujHz72GJwOfNB0gvRi3IspKAPPjV6dWjzdHxIk0ynJOEb3FAmE54AOAiwgESAaCkcP55H2RufVJtkHyG5OvHlEZEge6NQlgaixfQ3yFxEhKEeZbsWqVPlGqCG-jGbaVeFVqs6RSyHlJFc8atngZglEb9epiMFUamgen6_6Aud3gPfUxjHb7UzgFnoPgSNUHrpnELIj3edckRQ8M5LIjIoXJ6fpcV975eLt_gTY-uE1w_cCBWp8YNsb4oDpVO7-u3LuDC81XaN2n7TqYaL25g3Xu_uvtbuNDoQVS5wycLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وحشت رژیم صهیونیستی پس از به درک واصل شدن لیندسی گراهام
باید بسیار نگران بود، ایران از اجرای سیاست «چشم در برابر چشم» سخن می‌گوید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/670444" target="_blank">📅 10:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670441">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b64e8341f.mp4?token=Qe-8GRj0dJpoP-m2FLQ2rXPyLTDiRK_BlCm21xKU3v-oB_8urnJbUZZ7m4luYAdaCNsHaqh5Wp3hdSO_uRIMOAPzTIJCOBm6vvH8rL-BFWctmyTauxNDTcuFFEt1Y5U_p4z12Mh58U9-3JGpFWkXlJpgX4BMG16XHLsEkzZZP2B-lQxiit9F1JfwmwqShHW2RBQZc4ITyrWgdT6G6BAcunEgfeBJo6l_OBeplQI-LtA8PmT1R2wBK0cMSlrlXC7P2nPoJ70-As1FCCWrekS0RuofCCynOK2-f6O1TfztoV3mQ7UY56bFNuMZVPsr_o49UUVPPmTL5wTdoMH5G1AcHrAFFtRQ5OFq_DZwkt0XAzRffOxK_lzEFXRsfekf0hKpg7u3Miecr3TRS5KCyxdkvdhRDAVtdx8gh5ew5TDFFJnUf0PZQg-ybg1ZaZdY0IDbkp41b3AmJtbVUnP3bnf1BSkaFpErdqLSoHof2BaEA3dMFUSJx-v8tvjzjkZo3_59YVrsss-W7HnHi2o0fH-JLkxvKufQslnZJqwQuo7Xfn9Vo4fl6Lf2ZvE0C78SOeo6ypjN5GhLmCpQ74Avm6_5hSgij57h5VSfKAL0jDJZjwPRmXe-NiW2bqXq8EKzIP88pI0_KlyeK9cbmg5iGOygF-3Lh5DmuDRXa0QaoRj1x30" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b64e8341f.mp4?token=Qe-8GRj0dJpoP-m2FLQ2rXPyLTDiRK_BlCm21xKU3v-oB_8urnJbUZZ7m4luYAdaCNsHaqh5Wp3hdSO_uRIMOAPzTIJCOBm6vvH8rL-BFWctmyTauxNDTcuFFEt1Y5U_p4z12Mh58U9-3JGpFWkXlJpgX4BMG16XHLsEkzZZP2B-lQxiit9F1JfwmwqShHW2RBQZc4ITyrWgdT6G6BAcunEgfeBJo6l_OBeplQI-LtA8PmT1R2wBK0cMSlrlXC7P2nPoJ70-As1FCCWrekS0RuofCCynOK2-f6O1TfztoV3mQ7UY56bFNuMZVPsr_o49UUVPPmTL5wTdoMH5G1AcHrAFFtRQ5OFq_DZwkt0XAzRffOxK_lzEFXRsfekf0hKpg7u3Miecr3TRS5KCyxdkvdhRDAVtdx8gh5ew5TDFFJnUf0PZQg-ybg1ZaZdY0IDbkp41b3AmJtbVUnP3bnf1BSkaFpErdqLSoHof2BaEA3dMFUSJx-v8tvjzjkZo3_59YVrsss-W7HnHi2o0fH-JLkxvKufQslnZJqwQuo7Xfn9Vo4fl6Lf2ZvE0C78SOeo6ypjN5GhLmCpQ74Avm6_5hSgij57h5VSfKAL0jDJZjwPRmXe-NiW2bqXq8EKzIP88pI0_KlyeK9cbmg5iGOygF-3Lh5DmuDRXa0QaoRj1x30" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرغ رو به این روش درست کن
😁
مواد لازم:
🔹
ران مرغ: ۴عدد
🔹
رب گوجه: ۲قاشق غذاخوری
🔹
فلفل دلمه ای: ۱عدد
🔹
پیاز: ۱ عدد
#آشپزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/670441" target="_blank">📅 10:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670436">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYvXyhQSO4inE2duA1Xf_hyzXQXlBhPJNgLknXWV9s1P-WyL-H-VGUyZH4PL0b1dyNx22hW0Tblin5aLjpQsh5v1U2cAs3rzvcm6wZmz0Fvp461-8mZ9KUPz5-RXo-Rp-pmga7WcpsTrtatJFKeqgPh4rxw2LQl4tsteDMxEbQL8la7-KcGchVT-Hy2y4NnKpEQC7RoPW6B4UU_g7euCOA6e_Xwdx-K6HpdjFDOp-AC3y-L8wxgc2Qb8nTwMx3MZdBds8c5ZOrCvIOuszS1rLmmWBYNPV-UAAzXOx4VWBDwLCuDj7TifBREBKu7gW7f56eYixfAxyBhtQ2PsvtSE9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کوه‌های رنگی در مسیر زنجان_ میانه معروف به آلاداغلار
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/670436" target="_blank">📅 09:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670434">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/822c55e4a6.mp4?token=PQJ0NDHW2rsEsa4KkwtNEaeJhDuOeiK_Pes8kcW3QKYHfSW79Tc-hBW6vxAJRZBC4e3oRy469kCuxwL1WWUsUV-CWw7CaFx00j-GSzQAW28YjTwQViTWJRfdEQEceUZsSov3EE0Emznc_67VR7lVVefhwk10NJSomnO-L9D9cHwvQEaZtOte5d5tPGNjT3r_OUgngILc-RzdV-3TjIkAtA1JvnhjZa5dhyS8qytdVytX7wU5sXepbTfVZGrlJ-6T3TAl3xLKvEZ-KeSC1SOnEZkBd_1xO04fwk6sWEtKOp2R0n6wsxwO86oSnkw29orI4LAkbs9tZsVKdhi0iOIgHB_peVoUtKj2aFvoaXrv4kl5M9AUrS-WY8Jmi1Nm74PxyEk7-YHRe-CzpjjvW5o1Mtz1HrVW0L1AuQDqbOY3OZsJLi-TPe1ASagWXlhKKjKD-OB-qCL7nYSnWdTndrLmYUx007r-48D6oLxxfsP2WXQCwsx5o2FAzghyl8UE4_n_kj9JM8gdgEmAW4uisJc9VdY2MdirgqzKooAQbxD1OdskuAxrUwYXZd5cMs6fwYrQCmDbr7xeXGy58C7q7hqh6FWvLwLdq74Io8D9166VCVNNJCOHhV17wKZs5oCISXpYZc8BnVVVBzWyAFik89oovKScrakCT0yb_fPiXlMEKoY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/822c55e4a6.mp4?token=PQJ0NDHW2rsEsa4KkwtNEaeJhDuOeiK_Pes8kcW3QKYHfSW79Tc-hBW6vxAJRZBC4e3oRy469kCuxwL1WWUsUV-CWw7CaFx00j-GSzQAW28YjTwQViTWJRfdEQEceUZsSov3EE0Emznc_67VR7lVVefhwk10NJSomnO-L9D9cHwvQEaZtOte5d5tPGNjT3r_OUgngILc-RzdV-3TjIkAtA1JvnhjZa5dhyS8qytdVytX7wU5sXepbTfVZGrlJ-6T3TAl3xLKvEZ-KeSC1SOnEZkBd_1xO04fwk6sWEtKOp2R0n6wsxwO86oSnkw29orI4LAkbs9tZsVKdhi0iOIgHB_peVoUtKj2aFvoaXrv4kl5M9AUrS-WY8Jmi1Nm74PxyEk7-YHRe-CzpjjvW5o1Mtz1HrVW0L1AuQDqbOY3OZsJLi-TPe1ASagWXlhKKjKD-OB-qCL7nYSnWdTndrLmYUx007r-48D6oLxxfsP2WXQCwsx5o2FAzghyl8UE4_n_kj9JM8gdgEmAW4uisJc9VdY2MdirgqzKooAQbxD1OdskuAxrUwYXZd5cMs6fwYrQCmDbr7xeXGy58C7q7hqh6FWvLwLdq74Io8D9166VCVNNJCOHhV17wKZs5oCISXpYZc8BnVVVBzWyAFik89oovKScrakCT0yb_fPiXlMEKoY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز خاموشی‌های برنامه‌ریزی شده در کشور/ نیروگاه‌ها و شبکه برق با حداکثر ظرفیت در حال فعالیت هستند
مدیر امور مشتریان شرکت توانیر با اشاره به برنامه‌ریزی خاموشی‌های احتمالی:
🔹
این برنامه‌ها دو روز قبل اعلام می‌شوند و برای دو روز آینده نیز برنامه قطعی برق در کشور اطلاع‌رسانی شده است.
#برق_مردم_کجاست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/670434" target="_blank">📅 09:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670428">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQ7WrVruh94rHH-XBaGCo4VSlju2zDkXJYeT4ggsKAi8i8vv1dl82jpv93_ZpWHbfj_VWst_YQm4XQ0BkcUySf06fywIqTBnW0zdii7luSQYvpJAT3qxbBS4yqejUN9boEHA0a4cpVnyOO2Hbl2qMg_d33bT8Ebm4hQRXK4rv5r9eW3tW7Scf0muU4GdaPRc5lvtM7vFAjPCX6O7T0u1Bw4phK_cJbAO6Ha-qHJbcr3gXurGm6vYXVhcCJOdL_4fxmGpTX6841IkX12etAC_0LOaqYlyKxWXRBWiTML1jgqGXFD5B3m03giXbq0GaHwdpbKEWBrJsldQVRIZBJ9Y7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتقال سهمیهٔ سوخت به کارت بانکی کلید خورد
🔹
براساس مصوبهٔ جدید هیئت وزیران، وزارت نفت و بانک مرکزی و وزارت ارتباطات مکلف شده‌اند که زیرساخت‌های لازم برای انتقال سهمیهٔ سوخت از کارت هوشمند سوخت به کارت بانکی را ایجاد و بهره‌برداری کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/670428" target="_blank">📅 09:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670426">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff0dfaeeb.mp4?token=V6H39I0CLS8YKDPSDHb7BP6yCc2GCX6csGmf_5UIgmo9-I-klh5BYrJRtqx9EXeeLh8H0U5hxKMBzwfsPMNVdnAM3Vn35vS22TMzd3e9xALX5rE3XtyGzGmxvjHhQUqzLZV7G8amiGRrkH6MoarPFjK9EI_QwCHXl9t-37P1gh2_O5rCFZEI5yOZ9wUrW38YVbO1by_3_TZGbPAX3OT-9PigMn61O62anWiHSYdNeMue4DAVqnt03tzjUViV9wQZoBisfWYgraq2C7lQ74a1wRwmPhMcGHH4Jm-iXVlJhc5NYHIErFUTXQ2Q06_20M7FgrotflwhCSswIQMB23nh7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff0dfaeeb.mp4?token=V6H39I0CLS8YKDPSDHb7BP6yCc2GCX6csGmf_5UIgmo9-I-klh5BYrJRtqx9EXeeLh8H0U5hxKMBzwfsPMNVdnAM3Vn35vS22TMzd3e9xALX5rE3XtyGzGmxvjHhQUqzLZV7G8amiGRrkH6MoarPFjK9EI_QwCHXl9t-37P1gh2_O5rCFZEI5yOZ9wUrW38YVbO1by_3_TZGbPAX3OT-9PigMn61O62anWiHSYdNeMue4DAVqnt03tzjUViV9wQZoBisfWYgraq2C7lQ74a1wRwmPhMcGHH4Jm-iXVlJhc5NYHIErFUTXQ2Q06_20M7FgrotflwhCSswIQMB23nh7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرگردانی خودروها در سیل ویرانگر شمال شرقی چین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/670426" target="_blank">📅 09:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670424">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‌
♦️
سپاه: تاسیسات و زیرساخت‌های ارتش متجاوز آمریکا در بحرین، رادار دوربرد هوایی FPS و رادار کشف شناوری در پادشاهی عمان منهدم شدند
روابط عمومی سپاه:
🔹
تنها راه باز شدن تنگۀ هرمز برای تردد شناورها، پایان یافتن مداخلات ارتش متجاوز آمریکا در این تنگه و احترام به حاکمیت کشورها بر آب‌های ساحلی خودشان است.
🔹
ادامۀ این مداخلات حوادث بزرگ‌تری را در حوزۀ نفت و گاز جهان به‌دنبال خواهد داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/670424" target="_blank">📅 08:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670413">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NbrMKxc4sZt77BZ7VpfxCU786b26aDHod0h8UQjTUoswx72D33Q4iBUsuVM_UWY8MNvZ-JZZh1HinxLZv_wvCr8QfuyZD-dy5f2MGs6TuK2sYqsQNy4B9y8tp9mpMeCrssEWi_Yko_GCELNj2YI-YvEkvjw086kxS_jX86RTyF_HwunvQBA1x3-t-zcpUwCnJNj0PajB99nUZhDMTUUU7ez7WYJbkR4qMotlUsAp9fvLS66sL9GydAgZQgUMrPrUkOQ9UIRMe_4YSGbNNms_7M6ZW73NRRkUoTLEveRhGLIeYwYRx-wpgQxi70kvASvLYakxOH5eVAWicFazl17kNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ucui_BrfF19ziKP_EqEhveq1quIIZlc8cZX97xmXINrSneb0LD_Ar95YW0ig_QYzONMni0_34YQsLrsO1bV-8Aopn2Q5ak1YIOqgznuIxZ25A9VEMPDljr-oulKtx95yhjg6sjnxM0YeY405IjPbzBW0Iqype3geOE-P5jfkHrtMj6F8i7tZk4UbqxKyRYhakrD-sES_6w_PNiZkrgDgh_RB7j-NiJuIcRQqtIZohHAlGR949mZ3nrqVGRd_NHI8qf-SdpB3WV3UbKuy-LPNtCFKNP6P_ZnP4sSWlVeKggPxkvfjzK8Y3tlsSe0OLZvkW3My-z8hEziN9eJ3f8ULEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o7ok2aRAmkCh_fPJ4Ni4EVY7m6qI3_I4rDSJIVFqJAcIKQ-vD0-FHfSE3E7dGIc5PFzfcgfdxdfgPmBllq2ts_hWdbE9BGuYt3dlD3lQuZAVeWhf8d4n9DFvCgDRN9KxmflXeM89isz39FcTUfZGDggBA1K9dUrtB4IyAQHJzU83HRyfEH37IRGHp5ZE2p8FB1dh6bOuQfo5pUW8ciqFA0RuKzhqbFvef8c_Jp1DChShI8MnKjI-2f-6WTEnxGVCWv6Ytj60g7r4RqD47-bYzrQ8rl8uE89p5dRd8SlfEE44nMWI0RNKmYDQXi3m8E1QX8kyC60hNgdrXTOnQ8Yspw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JwdUkprefC81zm5bEhIAtGkYtWYWNafwmByp1rbeToaDaQfLy5j1HHqFbe7ujNej38JpN5OtDjiLhGF_NfKyYjAVZuhGQEdkUVY4lPySKafXq3Ws1fImhqfQzkazWhSXs16qRGivNldv7kALCbD-7zSgggdHe3ktcerXSPKmkkJ5vEhlDWeIhhh7pKxzcEcbIPtJZIUc0hNV4DLU7lMAln4z0U9R_prKXA5UAEWaq1Af6t66M4zwtUQKa87IGb2ImpCLjlVbXhVk-YwfzQFUbxs4TzZALFwZ-bIieMO9FCvX805YtfwbmgArCTvGEsc09VyZCAT2QOsqlWCriydQGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjCXlN9qH_5ldGA7JwDGzxSBBi-0-hqsrwbdF3l4FxryWFcm2bwHG_pWkKvUAWoe8qPR-LXCyNSnBCCvkAPwoRa1kr8Z00FqSl1DwBbUuFnZHEyUhwSPGAmTB6hXF9dGuhqnp17dRemQC4K_esb_mX-9GmLwoUcqmrZJH5rnOvx2x--_9vtpSDtSCeoTIbCj1cXmrMFwCITqzAeCapucaSjCMjxi4ZF2GNdtkjapL125RC52NkWLNgD8yPcT1dlCdBI4vu2RSCl4AUNnLqWmdrzVw6wNwXmHCVVNr8hFa001k8jaejk40I4T-Ge1TTEnMz8PC0tTIjiuB6F1q9SfMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K0ngLBh-7u3ujxq3MNSAaI9xnqLwO4eKoAKWyt5U7LnY4nHnb0R1TK4hKtHkDcZ_5K5qr7FpEXsW8sXvI4ldPI5VBkO9vqi5O3eGyZvLC7WbYv47holPO8gWzADl6MMLPlABh30eDyL3WJYhuT20kdkLUgME_Q9ILAmgA0Czv2d19wtrYS2PGv7JHzOIag6k3unw7FDDW8I0G-9nxGfWmR4_XDDFPI9r5m4FY3cgh6h1WKTqkyDGHtimhYoemvhrGyPcuaXI1b2C3KIqMWIbWkjqCrYmTE28F_geVf2esc46djjQxx9OZPzwKV5QFqj5FMuOe-yLsAffXUdsnqc2Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/khaAqP229j0wNsB-OnDjQxFi8YBEsBMOtbk6r1n15AmMa_ZJDmBIMAejjVW4GkZ9z-y815TXBqfAhOyYRzpXhZZxaRZZh859Cb2tI4t94B4J_58TtlO6HgNhroUk9IANW8U8HTD-sm9ET2yxJ3YJiYxajUBgg5_nEY6sDFFQFFiKiHKoVIYy__R-9h7EQjQ8wDAvRCIXrpL4CEL59_mTvQ-NuvPe5UH_brX3ApeLYl0wfFgXsfoRGODkCaL6nXtr5yjhpk5amejtc_xKV3bt9MVx0faJD0bY-aPMkto2u1zORxkjHX6kc6zw7T4YXWNRl6k_2ARtqitrbqGaXXu9kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s120GK3KjmeQvJVt2og7hVqyUL-v1IBlH8T2C7wH8rkooffBri7AMnovJvs7DqcYgJlTZ0C133YUFM4JkuRAa674rt3zPQAtmpqVL5-vavkipRH2qsrkFyfOis9un1yEmk7B99Bdsy5ZqKUiiD6lz0Akf2bsNPDBmcXumLWkIVlsaU9O2EPCKwQwOCXciEcvZROy8LnM5rOn-Y7z6orQVNQKJumHBWVJoCK3N-rYbIbaEDSL32AvPKHpQ1uTxCtFH_x3lpxbusnxolsjQ4HV2KbptzQlfKB_pf03y0oRIfi4Mcllbh9tbx2T6U66H0awLM1FtDHpjcabCeiL0d0dVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q7gOFvKocDulgcWaQzFipkEl0-cqv1C6Db_b4mN878OCCjUp_W9woFBKwrTjNCmo-88P0AATwW21sUGFFztRvXRJlprfhiwlaPuEXWHEOU0i-UU9x2pAJ6irB81IKjEVo6fwjCsc9TxJx6o7B5cmhZLcvqwTAwLcBbmnzZmsM84dUQHfrNC0FpJusc0HxjwswNqew0AAmP8HJrIckC1mYjs1rEy4CX6nXwOnkgwK8yDp_ucKSxeF0baUmynak7z8dLgHH9_WRRp-_7EiJoTxBNAnXSJu8Ai9bfwBKKC8Dqma-r1gGB2SZ6JYUDJwKwaM0Fhd3-0JHZBPf0jnTA74xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">◾️
سوگواره رسانه‌ای «بدرقه یار»
▪️
از تمامی هنرمندان، عکاسان، خبرنگاران، فعالان رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود آثار و تولیدات رسانه‌ای خود با موضوع تشییع رهبر شهید انقلاب در داخل و خارج از کشور را به دبیرخانه سوگواره رسانه‌ای خبرفوری با عنوان «بدرقه یار» ارسال کنند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگوتایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر و مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبرفوری ارسال کند.
▪️
به آثار برگزیده هر بخش، ضمن اهدای یادبود
#بدرقه_یار
، جوایز ارزنده‌ای نیز تعلق خواهد گرفت.
📅
مهلت ارسال آثار: تا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق شناسه
@Badraghe_yar
در تمامی پیام‌رسان‌ها ارسال کنید.
برای اطلاع از جزئیات بیشتر، کانال رسمی سوگواره را در تمامی پیام‌رسان‌ها دنبال کنید.
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/670413" target="_blank">📅 08:45 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
