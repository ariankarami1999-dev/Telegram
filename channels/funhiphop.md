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
<img src="https://cdn4.telesco.pe/file/OFbmYhHh9HamxCIBwieuc4OvK-9MRtbaT8u24o0sLXBZeVl7fcFAkxbY-lZHLVti4kQ_6SLRhm1fNk5F9jezHTsPU71KDoisVP3guItdxZ_2gsnJwhPA9cmGQsVRVuNBV6sU1FC4AtmxlKMl2oDABqY4NJgxo4DwWLKwu-af3n6fyaDTodNabZodYMoGID_ixeTdToyO5_UPhD5sQ2TpMWrEDnS0UUHpDNJaIKyCa_VoDhvyZuiFB8bONn5XC6JI-TH7Gik4N9SRPiGOedbGoNRpq-XAI9tW-pjuDizTadMgtxXAiR7pfF-Mda039x3WLxGG4m6uMnBSuw2mR_RJ6Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 174K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 03:30:22</div>
<hr>

<div class="tg-post" id="msg-77027">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFR5ix3yzHjp44206KgfO56zGZlXqRGIVG6hDzHmfh10JS4cvHyyEKYV5AYYltLcw5-Goc5W7Ya6_RyIgBwDCq4H-REXas7Eb6tjAXGrTPaeZ_yw9rbNFuJHlC7JQHkOpq-RKV8N8FFKO6z_foBzl_NDI-trY0wLbCw040H2R1kfKN_DZTT8N4dg_vNDhowJnZlpmet23zosZ2suUOHrCZIiReB_CkOLI3byyi9QkJlUiT72_KcCHM26PHqT2Ct6ReM68iirLKoTIPSw9R8zqDgg_VuJ1R4rP6sxvvuqpnShdxEMJd1Dbn6jN68JCTch9K-Xuq5pMZn4hSg4p7em6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب قهرمان جام جهانی هم مشخص شد
از سال ۲۰۱۰ به این ور ea هرچی پیشبینی کرده درست در اومده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/funhiphop/77027" target="_blank">📅 02:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77025">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">درحالی که مذاکره کننده‌های ایرانی می‌گن تا پول بلوکه شده ما رو ندید مذاکره نمی‌کنیم؛
رویترز گزارش داده وزیر خزانه‌داری آمریکا می‌خواد با اون پولا خسارتی که کشورهای منطقه از حملات سپاه دیدن رو براشون جبران کنه و داره طرحش رو بررسی و تدوین می‌کنه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/funhiphop/77025" target="_blank">📅 00:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77022">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یه چیزیم صادقانه بگم اگه مهدی پاکش نکنه
مواظب پیام‌هاتون، پروفایل هاتون،مخصوصا پیام‌هاتون در فضای مجازی باشید حتی کامنتای فان‌هیپ‌هاپ
نظارت از پارسال شدیدتر شده
تمام‌پیام ها حتی گروه های خلوت تحت نظرن و پیام هاشون رصد میشن
اکثرا بچه اید عقل ندارید اما خب  یکم محتاط باشید آیندتون رو بگا ندید
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/funhiphop/77022" target="_blank">📅 00:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77021">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اگر به من بود قانون فضای مجازی استرالیا رو تو ایران اجرا میکردم  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/funhiphop/77021" target="_blank">📅 00:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77020">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5uV5XkOYgCH60g51cElI_cPoWStucdUg61MSdFIgl99UwRe2Vk3icRvundPl2w5jLde2bGLewAG13Jqy63vuXqhrmJHIlDD0OlZlxjr39QvS0yRszR9HRAuQu9P6ehmNqskmMFkigg3cxkG6J3dkAsjWIyR85X7vxjMw122mTLzSTmS6JwINtrl3k1AERJvlTovPL9UO3yq9GK7MKMjNjLh3adteIeWTovIR7MuKl5Bhw4LyxGt45IqR3Cureud4gs2VIgA_s9uxBJJCZfuI2tyviYAgB74mP_y3B3pDX1kM18ynz9NvW_bQFX5FnJKr3mGrxQvaTCKisCc2bKwuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر به من بود قانون فضای مجازی استرالیا رو تو ایران اجرا میکردم
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/funhiphop/77020" target="_blank">📅 00:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77018">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-wwo4kYrwzASI729PdMFCoPcwuPeVbM2EshW3FqR3OpgvEF2Sjwl9-Mk0bHUoD4qn32Lfjd2nKRwxy4gdctFMijFoNKo3YepT5BE9uTPfcBdZc7dPIBLNnkZBeVAHpbvqGe9Z8_VloUAjoWUW6xqIUplEdCreZBhA5KOlLUynPUx3UPr6YFzW31-OdV3La19PE161nwy6CmKpeL-Gv4JlVfSE0STq9CFwZhU1tP7JeR203vwfG9SVz3Wj-pgy0iupxB31fB79KhysewFJ-hvIier5KX8QtxWOnfr0f3x4JCaJERnbFouyIEL57yEfT6FoQxDufQHx3vlB5Rsn6nMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمب جدید از CNN
اسرائیل تعدادی از نیروهای آموزش دیده خودش رو در کشور آذربایجان و در نزدیکی شهرهای شمال غربی ایران مستقر کرده و از سمت دیگه در مناطقی از ایران عملیات مسلح سازی مردم و تغییر رژیم رو در فکر داره
+آناناس
🍍
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/funhiphop/77018" target="_blank">📅 00:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77017">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">محمدجواد لاریجانی (برادر علی لاریجانی) در صداوسیما:
رفتن قالیباف به اسلام‌آباد غلط و یک هزینه بزرگ بود. ترور رو با ترور متوقف خواهیم کرد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/funhiphop/77017" target="_blank">📅 00:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77016">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJIH1Z23uB4OCTG5Kgntle0DSKAC5xvKB8uXTf9KY2GHa21pmaosqwRLWUVYoKAtK5UWHTqiVnEDOsKOnbnky3aJEKJM-3utE7872ezCWehxex-6Ma3tGFOWn0bmwN3_B6h246sC8aHs6A4XlKp37c6PoKIAa0uQSpQ7_1zDZ7qbd-IrgbnjXpKDNab7f5EsB54uypcQKkBhScgNCvNt9WotKGnvIN_3Py9WK541Rl7bb33bX4n_aUuBF963s_pydl4a8C2O1FMYos7_L7qKw1KMN1zfg7iUcczJ4aQ_u5PKSF0diXLy6pzp5UfslQZ_ylZsww0lXva_JCjyERecxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک عده هم هستن مثل تصویر که تو جریده بهشون میگیم "ملا به ماتحت"
و به وضوح خایه مالانی که وسط باز نیستن
از دسته ی اول بهتر و قابل احترام ترن
درکل چه جاوید نام های دیماه، چه کودکان میناب بچه های همین خاکن که فقط دخترای میناب سپر شدن واسه یک عده، همین.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/funhiphop/77016" target="_blank">📅 23:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77014">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElaxWMjY7aJ33nB98pywHeiI3MNuC_kjjVfEetMig1MJVQ9JQy204plPnDCH7zX90VerWJPaDQAN3NW30Gyo5O97Tx12jIwjIsiwL1n-Sm6SZ2yFQvkFlWvWIPmgnSFfsFlvsaVOChgJydRU2A_2ke1BXVgnG99cj8ivcft9-LlRBup-IWVMrQYq1KKl6vvCM1vggWiOrW00neZVwDpRurI2UqsuYSfH5O7L3wKbguLa7gNOK_HwaUvrVhl2Wh9jvfxwNZt9umdFjlsrR8MFNsbSOPVtpbHIWYa9ssIuei9GJzLLSUc4gJBoI0QBLoVPm-DVNoYEp8rxordOq4wsTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یا ایران بوده گرفتنش
یا دیماه اتفاقی واسش افتاده
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/funhiphop/77014" target="_blank">📅 23:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77013">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVhZrxvoS9auRUW699cJAQKxkfjGNjwScs2xlmKlIhrox8QIXtAxSbbL8KJk2crBGCY3Z7h7ofdh8fA7UME_KnlFK4qmvIy8IPjyW1VCSYy_R1TneFOE2z2XZtmixiVxdTk_41ka8JpHPXh0-UDyINwm2RtJ4BTIjOnfKTorh0_sM1JnfQUOutkMvpc3sDb-lRpRRCb3iP8QPQ65eHQ43EXSb24ANF8w_oopD6y2athX_quIZPj-GCPheKWmRq9kq0HFjXZcSdY17enSgz_n9A6-S8rNsNyEirP8IGiYMNp8LGkvMMjN4p90I8PvGhGxxMz5V_ukZohsVDfyrNo2bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیپهاپولوژیست به هیچ عنوان این عکسو باز نکنه.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77013" target="_blank">📅 23:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77012">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXfnlnoKcRUepbdm5CdpicTmdvIkUOs3ifgrRQiiURqPTbLp_xr0gaz3K8Mh1kr4FdY4x7vtJQP1APUH-ZKdBRnxeXh5CpJjlG4iWZc-JSYzrYZktwmFblWT2P0eSTg9HRpgy7dJQIsXDaltUUpjd9v92SXk8N-QmQRrIntJFGLOo0LOVjbAYHYkyrJ91sanXWOspQdi07zdiUFZwxRtnsZksj_zquwXrc9v1sHcpgjSGn2uF0TfJvce7XqjAipWJkXuy0Z3OCsd_8eRbP8BlK6ya08AP6UseKsbtOGnEYtzUQI4ZFReAvfSGsxaYlwN9nFgFi47owwIjn3UjOmPpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این مادرقحبه ها چرا دارن اینجوری تبلیغ میکنن.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/funhiphop/77012" target="_blank">📅 23:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77011">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/funhiphop/77011" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن حرفه ای لنزبت
🤩
۱۰۰٪ بونوس اولین واریز
👏
اپلیکیشن را روی موبایل اندروید خود نصب کنید و بدون نیاز به vpn وارد سایت شوید</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/funhiphop/77011" target="_blank">📅 23:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77010">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIKJ32ckMx8hZ6MMFVTxYCWGx2RCvPEtEjY3fyGriIlH0tTd8uVFNcwJuT827Ev3NuFCpYGxNvERR5iOMYEJJIlRMhBXg6tK5D0fndVr71Vaxmg68Dvl7CmqFlYgp0Jduu_OrbnIIK4981ELuji_KVrRNgtgJuPUHPnBvvd5qVP1brttGrgSFsl9tiP_S56NoZQH2eHTquPiE0PKqEo9QV9yTOMhJexcYRpqrKPmltCEfI1ZLwd-kvjyHq1pJFPSxt4bQYQMPjoDlxlRV6jfwI5HfzSXRlpVHwRr4LsYoRYcJftVsGve9-IVYl2fAEDgK8-AtsmG3xktVb3cRQY4tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لنزبت بهترین و حرفه ای‌ترین سایت پیشبینی
🔥
🏆
↗️
بالاترین ضرایب و متنوع ترین آپشنهای پیشبینی درلنز بت
↗️
🔣
0️⃣
0️⃣
1️⃣
بونوس برای هر واریز
💳
شارژ کارت به کارت آنلاین و درگاه
🔠
🔠
🔠
🔣
0️⃣
3️⃣
کش بک هفتگی
🧑‍💻
با انواع دیلرهای فارسی زبان
🪙
واریز و برداشت انواع رمز ارزها
💵
💻
همین الان وارد لنزبت شو و از جوایز ویژه ما لذت ببر
g16
🅰
🔠
🔠
🔠
🔠
🔠
🔠
🔠
📱
http://Lenzbet.cloud
📱
https://t.me/lenzbet_official
📱
https://instagram.com/lenzbet_official</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/funhiphop/77010" target="_blank">📅 23:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77009">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbUA5eRZ4rRJvIJHSpaD8ZDN2PXb3BQtb9Pv12ES0d8SkqqH8k5bHACGgEUTr0RkZesHryR-12haGBO1Z4y4S0NoGXZdIaoW98foDH0ddTDMdPSyaJTznxYoxDlPdQvnJtAxhAq8BVTawvMBoa2FpepNxeb3d2GWYgXz5Dg3vOYH3eU05cPt4G2BrLbqc1YMI_wfN0oZBlidm_nEQYYXQZ1MjKlQPu5BIMKALx1IlKu0fGAZHN76JaodsLaXLABoQhPSn8iFURrZx5aQIAjIl5nc7R3oIrnews5HYjHBOSDORC_E04CivsAsKp2lj0jVjHc8a3eC5RXvy1Rs2-4rqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسهال خالص
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/funhiphop/77009" target="_blank">📅 22:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77008">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خارک صدای گوز قوی  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77008" target="_blank">📅 21:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77007">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خارک صدای گوز قوی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77007" target="_blank">📅 21:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77006">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خواستم این رو برسونم که اتفاقات خوبی قرار نیست بیوفته
هرچی جک و جنده که تو خارج بودن دارن برمیگردن ایران و طرفدار حکومت میشن
جدای اینا بعضی افراد هم که حکم های سنگینی هم داشتن دارن به بهونه برگشت به آغوش باز ج.ا دارن برمیگردن به ایران
بنظر من همه این داستانا یه تله هست برای کشوندن افراد بزرگتری به ایران برای محاکمشون
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77006" target="_blank">📅 20:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77004">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nePZ0Pp1u47V9CVQJ3FSDhMHeUSL4PjRe4Bp_5MOSR_PffrU-OExtsuAvOLs0_wBIiLOMn6MqGGz0DtHpaEotJgqNL-T3aMXM-Hw1y_A4JDbGZRqnkgL4nwBDpoN_m2Jm7PGhYQYNUkXgBlbdYx1CiyznogOiWNrF3DAMstMjzYRDTV_Jot5gTl496-C9lpcR0CAPCLWXovEpEJ3SkkDKX8_JCxRg_VYziHK7o5URWCyJPYX08KswWAPnGFuWDehplLiWNtMm5PMNpC68EyNXIx-T16nhM4IHzm4G3wUVgAnQ_l2hu4E7lMN3CijcS24X6TVXza3fgCNVaE7B3MLTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باور میکنید comatozze سالم تر از نیکا فلاحیه؟
ایشون هم اکنون در ایران حضور دارن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77004" target="_blank">📅 20:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77003">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHE3AM</strong></div>
<div class="tg-text">مرسلی حرکت کن مادر جنده</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77003" target="_blank">📅 20:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77002">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IquPkXqnxeThmd387WwOZ7Unnl3jTh8LT6-Xcr56F1u0KX7licK4onftAfe_mC7nr2ol0j9w93FBPNZ0x14OGmhGT0y-P2I8gm7fxv6KGwGcQyHEte9r4u1CBBSGVA8G4tYDOh3JqS2Zye26EEN6mCPy9gNdUJ_jZR1gSEWegxNKscVA8EZrFgsOc9JOrE_ponltqR_68v7Cf7Kh6k_jXp-wSIUJOv-bd-sJQ3vls6oYJpfO6-bL-UpiQzYDBw9K93yIf-2QaHYE8995QfRNt3astJnWr2YaOcQIVH8hSB1x4hgg_OLxM4843V8sVI3sSYA5v1jBNmNzq2AML1bC-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز فرداست دنیا جهانبخت هم برگرده ایران
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77002" target="_blank">📅 20:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77001">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">من بین ویلسون و خلسه "و" رو انتخاب میکنم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77001" target="_blank">📅 20:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77000">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔥
ارزان شد
🔥
هنوز بابت VPN هزینه‌های نجومی پرداخت می‌کنی؟
🤯
ما اینجاییم تو این شرایط سخت اقتصادی، حداقل سهم خودمونو انجام بدیم و با قیمت منصفانه سرویسی پایدار و باکیفیت ارائه بدیم
🇮🇷
❤️
💸
پلن 1 ماهه نامحدود
⚡️
(
✌️
دو ‌کاربره فقط )
❤️
🔥
249 تومن
🔥
❤️
لینک ربات
👈
…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77000" target="_blank">📅 20:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76999">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZzZtb8NEzvFnZvYGE-YVOX7QUp5KNbTMJtS2puFxK0sOUD7G8lGh1QAHdS_U9Xr0hx9ShN1u4LgInc95L1THJudhPF6b5vVonfj9c88hYzqXYdtZehOKndPkK3MurHGeEBZGIAK17wAMtgcHyUAz6DUZxPpsFMLEXXRaJ_eJxv8JRdcYp28z3wXvHvm1dgyUkYtN2U5KD2R5__YyQpB4jvGFqdnycRQsAklss202Nggt4q8KEQBwc30XqZUbcX3froj7pPCRlDs0HT1ba1TinR9_xZT6ThmhU_yi1s9n6TuhKf1wHtaJdGrUoCPTLRrWycibkEpy3jqdWmqg61h6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ارزان شد
🔥
هنوز بابت VPN هزینه‌های نجومی پرداخت می‌کنی؟
🤯
ما اینجاییم تو این شرایط سخت اقتصادی،
حداقل سهم خودمونو انجام بدیم و با قیمت منصفانه
سرویسی پایدار و باکیفیت ارائه بدیم
🇮🇷
❤️
💸
پلن 1 ماهه نامحدود
⚡️
(
✌️
دو ‌کاربره فقط )
❤️
🔥
249
تومن
🔥
❤️
لینک ربات
👈
@Window_VPN_bot
💻
به همرا پشتیبانی قدرتمند WINDOW VPN  تا یک لحظه هم قطع نشی
😉
@window_community
:کانال تلگرام
🛫
پشتیبانی:
@WINDOW_SUPPORT</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76999" target="_blank">📅 20:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76998">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9652823ca5.mp4?token=uarb94zXCkwAn-krWdtpINRfZBwcPS1OErZIefQj7_6V4T2Az1T-oRu_l08JTrzUuQ2CRLL5RT8L8-7GehA8fK3QbqzNx1hH20QPD5BHJ3PixTnrtuoCVhC-Z1q4nFF88LI6HDuTo0n64bmYfktBCMIr85d0jOG3QX3RKYPqdp7MdTCNKdrvUALrkJgyxWxVZfO5iVl4I7_1M7NDPoVQbgfFG7g5tyZ5uhgucIDTqcn1AqnHR_QekZLkg88OwOKR2dBDKn4zmBcX2xc0GYDaD614bLghLZqE7hgi_M57MvDYnyxFrq4wwWnVVpJzi2MAVzl0GzREfs5B9H_f_L3fIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9652823ca5.mp4?token=uarb94zXCkwAn-krWdtpINRfZBwcPS1OErZIefQj7_6V4T2Az1T-oRu_l08JTrzUuQ2CRLL5RT8L8-7GehA8fK3QbqzNx1hH20QPD5BHJ3PixTnrtuoCVhC-Z1q4nFF88LI6HDuTo0n64bmYfktBCMIr85d0jOG3QX3RKYPqdp7MdTCNKdrvUALrkJgyxWxVZfO5iVl4I7_1M7NDPoVQbgfFG7g5tyZ5uhgucIDTqcn1AqnHR_QekZLkg88OwOKR2dBDKn4zmBcX2xc0GYDaD614bLghLZqE7hgi_M57MvDYnyxFrq4wwWnVVpJzi2MAVzl0GzREfs5B9H_f_L3fIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو کامنتا بنویسید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/76998" target="_blank">📅 19:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76997">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بانو آنا د آرماس ببینید.  @Funhiphop | AmooFirooz</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76997" target="_blank">📅 18:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76993">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TpLyBrt3gpXhUd-XfKQBjRwthIax1XfDIG3iV3cfDfCZDCXIg7qOJH3Dz2HIdT8XbTcrb8hiejY46Ye398NpfkoMy0tK1WPYN8Gh4ZRVbwvSXtvusglhB67i2w0Uqp1MhMxuBk5khUbhqlBhM7vUcgnKecB2-0HQquyFhy02K4u6I6Irq8OBbY9Y2diSROyFCc9GK3sib2UWvqJq8YQM_KmAHewUjsxtrnhPtVwozEFLfhUrNrQK6WHaOyVZiEQRUHnCikzK99tbj3HH6HV_vsvtjkNm-UY6UC6y7jdpMBi-L8xDdWvn9QpSTYsJxtxCC1MDk4U515xGAoNsXCNjoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/txl2FoaZUfHcYfuZh8SIYALVLgn1TnO1i_cIw6_oY3j5wf6l5fUgSt7ogNqluaRq7e-fRrJ63AMK3SWjXQRAzFGzrAVE8cf5rKWSuDQIBySPe599_LnZypCiX3sjzLFttEsJKg2FbVAzt1F1hqKtv2HW-9wIfBkc2Sds0geq3Hi1z5mgljWP1fsB9YwTr1QpglW0bh029wLrg0VRPB81Beusz1FpkJyjjeDoNecDJnhTiiEG9zzs_Ehl02eVMNdbZpQsZSho9WhJr05pNIqphpxpn_L4Y0WDa9xjLWu6bssf0TF4F1FUtW-1lUzy84_yWQXIFcKI2OITGSdLQvl-Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rjRQBdPKjSt3PrfUPO0VPgC2W1xQdlmnBYiXDVrktO4E34qVhxCq9l5fWZcBOBhGgF37P5xLyfoA2YxvUq6SM1nt9su9bZEyj4qCRGLKc5RdL0FKuXx5rCHe4fAshBDxy52Ydwdgh6jYxAbjK_HTdQWQyjPU4CwJy0rJpQhby1wQpStAva6zKoNDPkDKQgA_SB0bivq-SlcNMWOp9fsGu7n358Viw1GrtTsnyvpcfcqITbQA5JPqQgK1zTcmmulE0VVBTv3GLDTZKqkz684NWuL93V9OVdx_fadRwGNDLD5Val4OJjrbE2foxjMq_8Ra49-BJeq1k5h0A4kVtK4vgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNhhVsQ_x3HfV_QJFJHZoJuQjzF4V_B5gEQ-Ge-xac3IpUOCvNTD9VQxqlV0lr4rt3KtEyR5vr2GUWfKxplP4IoDMTW8Asgtkcx7TDGGPFvBESQEVOSLO7NVzpALc4n4e49-0X6B58y6VL_TiWlP7uzWEPM9BM1B-pVAJ5orOF4kKEGKuQ3P3hhUkKOrlFEDsFjXlev-g5sHG2OizPv5thlr3mW7J_Ys3KmTc5QwgX05RDwl4fUkWKmIe-BT_F4TZeJCMlVLg260UB7LUroRW7fRS8OLN41T9emcPxWNSlos2c5GQncCewe7HZTRuGamQbbIVr4LDVZd-4PZlwIzBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بانو آنا د آرماس ببینید.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76993" target="_blank">📅 17:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76992">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OctgiX7yFvH6uGokFZFA3ZwdKfMSWo0QPTviGLTkzHjagUfH7OGxiktwKtP22Gx2xrqQr33CrChNKCFj1ByKIIBMFgFOBWZGgNDFlMF34E8HCUGHaBs7ZGeONo5xnTR5aA7jijRckFhzKpC-MhacvhgNeN2XUMYPFYOQaq1LsfPcrnc-cfSwmXh0kIMpD2hFb8EqC7kvgyeS0swSTiamicHbXSx49MpjTcFLnS8hfHRK1kN93jh21Mcq5xF-0CqQlYUjNqcf3BuL7hxWe_BRUoe_b2fkojuWq_4QBU7uXRm_LBoVowqIaaiByAP1JTLoN6r_W6ChT9Z6bbO0eDUX-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر خوب برای ممبرای ۱۵ سالمون؛ اسکین وینیسیوس جونیور به بازی فورتنایت اضافه شد، برید عشق کنید
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/76992" target="_blank">📅 17:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76989">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/771a0a778a.mp4?token=eY8G1mS5ZG_EMBMq8eSq1iJJQG9-fKe1AEa4k7e8xx9bxJxepNmGfRRVrvrQShhAWZAsZU7kCNJMzEEYTCV5E5SDYJzzATO4TpRav5EtXW4sprPaJzkq99AvWrfsQLvzSQheut0EVx47fCkckTKpi4Z4e1qo-7ac6d3RRicsq5r2kqqsbNa4WpvFhkH86Irw3WsBsRt-Wf3_qMnPogGewWXNAzHQmCxD_ygG8L4WafSC6sLWS9CAqqkaRdIT95caVasXodiS5YLQtzZhgZjVUbCZhOmhlxdl0-4yrDPGO1W9XPVQi8lPZSeS8V3qltrwVhNbOVop7iCx4FF_uAEOJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/771a0a778a.mp4?token=eY8G1mS5ZG_EMBMq8eSq1iJJQG9-fKe1AEa4k7e8xx9bxJxepNmGfRRVrvrQShhAWZAsZU7kCNJMzEEYTCV5E5SDYJzzATO4TpRav5EtXW4sprPaJzkq99AvWrfsQLvzSQheut0EVx47fCkckTKpi4Z4e1qo-7ac6d3RRicsq5r2kqqsbNa4WpvFhkH86Irw3WsBsRt-Wf3_qMnPogGewWXNAzHQmCxD_ygG8L4WafSC6sLWS9CAqqkaRdIT95caVasXodiS5YLQtzZhgZjVUbCZhOmhlxdl0-4yrDPGO1W9XPVQi8lPZSeS8V3qltrwVhNbOVop7iCx4FF_uAEOJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگ داخلی پارت 2
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76989" target="_blank">📅 17:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76988">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خلسه هم آدم جالبیه، به ویلسون میرینه میگه وصلی، بعد همزمان با جی‌جی هنوز رفیقه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/76988" target="_blank">📅 17:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76987">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">جمهوری اسلامی پاکستان ۲۰ هزار نیروی سرکوبگر به مناطق آزاد جامو و کشمیر جهت سرکوب معترضین ارسال کرده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76987" target="_blank">📅 16:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76986">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJIdSHZUeU9ab6zm2c0hLKpLq6XU35o3R3CvdMQhQgZta4g0WH_s6Cv0JBcEbn5n3tUk-NmH_wVaJq9QAqqjXOh2BQp-WxkZQzDIaaqyMnbQfb0O7X4iSjObe4R3NimuNwrocYaiWiGhQ9cYs5PaImlD_TEF_ORKb9WJRfua2TqMwFsYM21iYbh0yp6ONQyzk1NOP42WWuw5bJEQTdmXpQ_0IViv5QcGU1FuDLKox_A8wHND4AFuf-74tfz1UM48RYJNKqT16gXsGXsT7QPs0dnvO5KD7gFSOykjcFu6TaO3VYVQKUtLbbdHdsgiCMRhVHpL-QrzhlNiJp3C61_XuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان عزیز سلام و عرض ادب میخوام یه ذره بی ادب شم تو این ویدیو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76986" target="_blank">📅 16:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76985">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">او اینقدر بزرگ و قهرمان بود که حتی دشمن خونی او یعنی دونالد ترامپ
اورا "سان آف اِ بیچ" یعنی خورشید ساحل به معنی بینهایت و قدرتمند خطاب میکرد
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76985" target="_blank">📅 16:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76984">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iR96A7GLvDDg3KgvHwDbdGELlRb35AvGc-09ptlpMkxZg9VEdXfa4M8GP5tclz40Z1zNJeNBqcguCPl9TkYmsyByq3_wS1zU4ZR0mQwGjIu02XvznH3BsJNcmDWuLuNZ42ZADDO5fSaA8kaSZzjz9_zij8Q1kfq3TGfwDzgUJdPJK74TSwlGrcaQsFpFPGLzZaDbAvZNHu--F3mpCEd5aUKheRqhGtkosmiePsBE3Sl-YOAcFGZnXfTRVdJzbuSVX2uGZ3dCxCIIwQDpcFu_f4GZZPpwWyvEp-P4AFLA2mc-Cgs47RoAP6ips005AHay_Si0fjxOy6c9sJi3YVShsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه زوج اندونزیایی اسم بچه تازه متولد شده‌شون رو "علی خامنه‌ای" گذاشتن.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76984" target="_blank">📅 16:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76983">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🗣
تجربه‌ای متفاوت از اینترنت پرسرعت از جایی سرویس تهیه کنید که تو نت ملی شدید هم باشن
🛡
🔺
سرعت بالا و پایدار
🔺
پینگ پایین و ثابت بدون پکت لاس
🔺
مناسب برای استفاده روزمره و حرفه‌ای
🔺
پشتیبانی سریع و همیشگی
🔺
ساب‌لینک برای مدیریت مصرف
⏱
اعتبار یک‌ماهه
🧑‍💻
کاربر…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76983" target="_blank">📅 16:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76982">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mX3sQ-nnCA-v9c65q2FJ66HPC8gsWDnIqKR3EB75KJCcFcApYsxB-ORbkVu2_3BN-hrjQRuVF-HQ9HpguAB14939NJlrJudvlCxDyumEr3iZJvapUsLns8py7yXsWOUL6YTwNSXHo7FIiRyWEpzp012zmA5a2ceUdX2KN0t_JnwFpRb4OlHJAXFudmciYjfYKKcfI2Jy3gQSYoCxOgArgwHzDD2XPCiz7IWab1YyCgVFFzKH_Beh-F8GBNAYmYkaDk66GSd2co9BzUTQ2ITCRkhuG9za9nV7qakNwQv4tW16J1YcXz4lhfH3oQs8gW5UCffY9zHwbjXNg4X_sHhPWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
تجربه‌ای متفاوت از اینترنت پرسرعت
از جایی سرویس تهیه کنید که تو نت ملی شدید
هم باشن
🛡
🔺
سرعت بالا و پایدار
🔺
پینگ پایین و ثابت بدون پکت لاس
🔺
مناسب برای استفاده روزمره و حرفه‌ای
🔺
پشتیبانی سریع و همیشگی
🔺
ساب‌لینک برای مدیریت مصرف
⏱
اعتبار یک‌ماهه
🧑‍💻
کاربر نامحدود
🚀
با زرین بدون محدودیت وصل باش
🤖
بات هوشمند
💎
رضایت مشتری
👤
پشتیبانی
📣
کانال
🔸
زرین وی پی ان
🎤
Zarin VPN</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76982" target="_blank">📅 16:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76980">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">جام جهانی رقابت بین هافبکا اسپانیا با هافبکا پرتغاله</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76980" target="_blank">📅 15:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76979">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">به مناسبت نزدیک بودن جام جهانی خاطره انگیز ترین بازی که تو جام جهانی دیدید و یادتون مونده رو این زیر بگید.
- خودم هفت یک آلمان برزیل.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76979" target="_blank">📅 15:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76978">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دوستان این وسط بازی نبودا، خیلی واضح اونوری بود</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76978" target="_blank">📅 14:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76977">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">استوری جدید امیرحسین قیاسی  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76977" target="_blank">📅 14:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76976">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqIuNraQ73HRa0MMt3SPXG-7YQG_Orfmd3MOROtadgpKq8j5zKx15_A4yHGVyDDre0WImmMVb7v7-Nb8TrrYL9G7A5uz6_rxqDEOIlE6otjVOnS8okmUtbHrfVoPcgBQrAUMVDlNxk8-TA8q0eVt74jUzEKoXd-HWxZWstxNq3kpzFQQGNBlnfu6ODwHKUArY9he_fHm3wDD62Tg7SYCW3N1KbFeaNCRqrzL2wmRmluAAONRpwTo_vkLHNFYGCexKJ9AaTCyU-R2R9rim5JKAtf2QVT8lm72M0AryRVsgAo5FyUhznri_5dqty3s0RgPBjuD3yj2XYdOoe_X198WRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید امیرحسین قیاسی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76976" target="_blank">📅 14:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76975">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نت بلاکس: اینترنت پاکستان داره قطع میشه  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76975" target="_blank">📅 14:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76974">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بهترین خبر امروز هم اینه که وزیر خارجه پاکستان یه بار دیگه داره میاد تهران قلب بذار بنویس خدایا شکرت
😍
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76974" target="_blank">📅 14:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76971">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ادامه در پست بعد.  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76971" target="_blank">📅 13:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76967">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CAbxlFmyi3kMk_LqGw7DapCxQ_5w37J4KI6C1wes307BubjZNiqxT732-OK5umVWP1x3pUs8X8sxAwba1hwLoloxMRNDe8wTFBoRDfx453BHaltIlp8egvCIyj7ZbK_WOySFPtrnAqbjEHBE-ssZV8XOKdCxq2cKtvNXbaWhKp1PFB2p3xufvZXWHZynmQmckrHe_oYWKmX9miBktjr0diMg4K3AHeiVk3NSbrRJsTwF_lzm1aYVw5iNrT9o44EzltJKr9x4BsvsZvFmHxvwj0gRs1-O0Js_mUYKksXocFhNmF1UyGYmKRZlnoQ0gLQhZM5JW3m8pIXuQZbxtjs4hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GwcSb3EfnZWVTT12e2PtZZ3sPesecjC7XJwCCQlKsOY2T5ttGNXfWlX4L-8yupUfhDo_Oz_zt8eDbz1nu8zPaRC-L758HBKuVfYe1Z6Xj5_ot_-aDHrM0iFEZhMAutnEw_3pTEucWNoqVcx2EMy1A85X7BpbDvtBsufaIoMPHnZWHeia4iXrHmNnkmut2c0k9CXzno47io81w7J031neTmGVA1Dx5GGACb6qty7qKgcSnq5kOhXESOFmvjlJlZuvIS-UCocmwHJKMDSQ9W7M59yG6AoV-jt2VlJ26O0F78H8fNXVebC2XVguq3C6igcMJOk5GX07MIdhbTE-pX7FTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ncg57xqyRinV5QNwYA0cedu92e0ZD2ZBPEdExLOyHB5pRSLBHfFOFdPtvTWS2MW87PKDm2SvW7TLlPnwN5lGQFyLJMhY1huaxx-Y4vHw7Qdm2yswR2NKtgylzwwrbux-vR2OTFBFTYiEj7sq--eLRAdSCk4e5zO0pYk6pGLw9--bRhpWK_WLqUVdm_wudj5XcPeqZZKldcU0y05Qy27o0yB0CF-M9U6IWKZNN9widQzOErz5Zs9D3XXbYSqPHM0i0om1bbKPFAHWA_QSglcKqleYve5p2eLLB4fRFedV2Kvp6f6jkQwS9H9eLRLoJXToBVJrz731ZR5ISeUMjusFzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iON55MiHP0KTlMLJMtuYGlVyX0tXhsLxDvXbJ5enG3ZC6nsQQuodyXCfWwoAvQykcWFu_is4aZ2pLJ4ew3PXhq2hVwZZRU0DcBcz11H2H-aGApDl3jR7pt2fFwvv_YrL-tWbm51ZRsPoo-S2dqjMFE5nP1rkJZhqBNrIcDYWTgiPtuXIhKrsHuQmGPrjf8aNffxDrdJ5VncSvczjkTGs_nDzzwpPJEStvD78--SGqzKPdWsT68ITSwFwP__VE0_qI2XLHzFEjW7O2Hm_ddyO-CjJnZZgPF6mSmxQX57SUILhVnYhNfigb_SeXxTWUTkREEc_hX1Qy0F6RNbsC6BPzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ادامه در پست بعد.  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76967" target="_blank">📅 13:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76966">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pwhnzduc8t4e2zmU-Wq2DdpdtqilwiOwMnpnVJLAV7YKIowSAwbUTFA1dp2kUyZkSpBJAXUizH1Ge1EM_ZyGhjEjUXHuVrCGBW1bLfzqVKA-CeWKOh-2-3MrbG4zh9Uehwm7GjixsqB6hl04U2PXdnVrAvuadnFEN6A_K1-rm1W4cnoqbj5yRU_Tw96fXZkM81rIPp5wVe9IDd-klLjIaUrdfM6gDXqHZ3TNPPnZGahjMUwa4HpWkiVBM8BEXRxZxl2cQRt6Bacb2jvQGXlo4hQokee6t5IuwCAwFZHy5HMz3Qrdhkrsmvw-prEdhU2cyK4GffLFcQF7LhfmF1wQAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادامه در پست بعد.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76966" target="_blank">📅 13:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76965">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpK8isyomUSf9HDtqeLF-YESUsSjOJ5Sf5u6PqMoO2X-NAw4FKmjdrQhM7sf-UHneZOBFsG-oJAk1UQslMrrpcctnZa-AtqaGJsXJB1eTipH94XeoybQvVjH8RzMCOeMb9rttt4e3lz8uuuad-nChmHodCjE31N9CBn6G9qWQQjTxe4Myr_I07RZk7HKIfVcpN5XtPmBqK6YvINETeI75UJNtWWEkMY2fVJZt1q29n_2bvSXzt1OwLO90HK6Gz8lgacDT8Fnqf8eKhdlBCXf50W16jKHmwbkjf-sziPRRi666mzpYhjItgaALEsiSmy60SBCkaR1cloPt1OYTxVRjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان چجوری بیاد تهدید کنه مثل جیسون استاتهام
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76965" target="_blank">📅 13:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76964">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">میگم وسط این اعتراضات مسالمت آمیزتون چرا کِل عروسی میکشید  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76964" target="_blank">📅 12:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76959">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یادش بخیر امتحان شیمی نهایی ما افتاد به قضیه خرس و شهید رئیسی، ۲۰ روز به تعویق افتاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76959" target="_blank">📅 12:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76958">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6RTogO0CIabb9nOzRrlrubxcJ7B72oy3TyPEmNCLhMaJjZsjmGyEORz7-aqMaoGns40z70tSGuRZKStR0j86aI870cCF4rmvjejY1ulcCwYtSdECEFIHTpnP88LnhZID5k9Znoz2Noz6q6wWc6E3Kc7pdBIl1YPwVGHvsN7Uj3_h_MNxc3p5n5pl7CvQu-ivhQI6GJ9sxEAL5bZdjFJsKzfOnGttYimaCMAuvU1GCjYikrACbVkXT2J6xjmxtyrTJcL5LwjubkHuCV_qjAb0b-K3RsQFDHbvNj_ro6s8zfsrytyprusxDHs68eEsUzWSLE2Ez9g4pgnp3-UNYGflQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگم وسط این اعتراضات مسالمت آمیزتون چرا کِل عروسی میکشید  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76958" target="_blank">📅 12:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76957">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ce83d7ab.mp4?token=c33KDe6gqqgeYkITULKtRbB8LMUpXMmM7nP635z2CglEqMlmibRCXPKTJ6sB0oJBJ8zdEKR9OfjJ2cqW5ZcCIWajIqrC8-LX8Uw6tHeCs63ue9KEuifDaeMnfZL5RRa-C38eMbGEQHNfQCXi3WT1t2egqyVCeTKC9l8Sg3f6fYZz3Anb3zoCdnxmCnqq7_X-S7lkmG4KCsk612vWZz1-ESj-dJTotiTQlO0JjvCeyPoKDPk76qTcrew6f7Hjnid5NAbqDtg6Ki_fFJWKMo5SI57rC5PQ1cLmeqT-bkBNvVoqeCwxtPibQ-_BQYIJ-dgJETDi1gn7cTS9MS3d_EwlRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ce83d7ab.mp4?token=c33KDe6gqqgeYkITULKtRbB8LMUpXMmM7nP635z2CglEqMlmibRCXPKTJ6sB0oJBJ8zdEKR9OfjJ2cqW5ZcCIWajIqrC8-LX8Uw6tHeCs63ue9KEuifDaeMnfZL5RRa-C38eMbGEQHNfQCXi3WT1t2egqyVCeTKC9l8Sg3f6fYZz3Anb3zoCdnxmCnqq7_X-S7lkmG4KCsk612vWZz1-ESj-dJTotiTQlO0JjvCeyPoKDPk76qTcrew6f7Hjnid5NAbqDtg6Ki_fFJWKMo5SI57rC5PQ1cLmeqT-bkBNvVoqeCwxtPibQ-_BQYIJ-dgJETDi1gn7cTS9MS3d_EwlRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من که میدونم نصف پسرا برا دختر بازی رفتن  @FuunHipHop | ALI</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76957" target="_blank">📅 12:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76954">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فنای اسپرز بیایید بالا میخوام بخندم بهتون</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76954" target="_blank">📅 11:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76953">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نت بلاکس: اینترنت پاکستان داره قطع میشه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76953" target="_blank">📅 11:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76952">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0fllZ3RCduHURYfk_OOcQvD49kXG4DQwhM1pTOewbdrmn4GbMDMw7gWcLQIbXgrDpZ9xLtHXIM8sRzE_Fxq6u-M3dc807x82bRTXsgy22i2OVuY8HPKQzavLBAoD4WvxFaHZ3SGMP_qt6pRRgauA7fY0O6Yqs1brr7VB2zAF3zEY1UPJOcAYsnyDPvDQVh9bUGO2g-_nf7R9foNNClN6DXBfhkr500EqTi9WibJ03y2pfrAOj8PfNb3Q_nVQjkGIbWInmIoi0qriRHKdR4YGvXeq-2_UraNtEHn4qVqdgv0SY93pD6beC7f0E91GLCQkF4ENj3k3UcRAEaBBvVJmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد میکنم سریال جدید اسپایدر نوآر با بازی نیکولاس کیج رو حتما ببینید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76952" target="_blank">📅 10:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76951">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">شایعه شده که خولیان آلوارز رباط داده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76951" target="_blank">📅 10:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76950">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jr9mqgIpdPXEit9T7VP4wY183Vw0w18U0DN1tc_7uDQqvLQ_66kigH0oXrD9IExr9IpEGmYCtWJU1rqKLFeUnFq_W7xKt4kdsrHqJNjATh8olat13atCx2lmeRRB4YL1-y-tTv4kY6jbwVEhDWXompwFMkRz3OSXRphsvjGCBFxkJ1G0NkpBMSfV4RM0wt4cdrAd2QxLvp94FnqiQISRrgHG0vO8LooFcN-mIAkIvzT-n-xLDf2AEdvVK4wswuQH2fiCEFCzurEUOfhNHrwawyWIOMlNPeBHX6DV0QJv_4pZIR8BVL8_kdeSX8Evgfw7kQg4hn3P07hnFeHJIEaZWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رومانو : رک و پوست کنده بهتون بگم، ناصر کیرشم دست پرز نمیده چه برسه به ویتینیا و نوس، پرز رفته دنبال جذب اولیسه.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76950" target="_blank">📅 09:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76948">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YbS4mauxdHn8mp0hQoANhDPRo6gXt9C21CZ59lLaM2w75zLRb2bRthvPhebAydLKYADbQ28NttUQqeLm9ZnE8t1m1Dy2moU2TE5u2y7mipgloe26MfuPIjzaollPUW2HnLFvAt1SJAGsG_0eRag1gRjnsJvBDHM5kjnkIuuTY9fqWyQns4zY4YB_Ph2zSA3Rfl8hrqMmp-TJOi9wzJ9eOpEOrSZM4f7QmvNwcb_WFjATmxuU8ZLexBGj9_cPKuXcu60TmasYDPCSp7vlqsvGYEosemSnQnZgkD0YJagA43ZF2n7LxAwh6JCWRH-P3S_ZsFCNkbMbj_AOatA9AONZNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SI82lzNuME284R2oLHsSUEeo76BoSxUhazGvlhZdFVEOLzzIGeiq1-X02lmG22yniZ7fkZOphgiFkh7YYUs_eUlClEgo07HoJqcgKkytBLRY7EOxo5IPQy2skQG9MMH6y_fV1gkNA50m4m-e7W_tQ5mdJJtYn_da3S9cFvnA0PaP2HhN8UIWSz5UyQM3qD0gY0l_FpTb55_tvvigCW26aHKAl0fqiXkIyPKZE4osVhJewqdfLhAxv2jEASDh2Xa9MR_fqBfRNM4rfKPJT0SfKIgT-uHBfubE-rQD7v4ApzpFM9lQj25nxtkGWiLrs-8rBgQ1RdngwZvk8Nq9AH1Lpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76948" target="_blank">📅 09:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76947">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6cwuq6q2ifRBedJk2QRvE_kowZPzlTc6C-3poEGUI8C9HO6ie-rJaRrBe1ywkMbhjJUNdxUB7GMgqFtiVhllhKU33Zg-CGyATYiRDsGK5-V8UIlppM-D7PbyaNulCMKXY5OYgyeiCDezV0TcgnMn4BUODh5G_AvV5ersV5Nbozd6kuv4zZrE-AUB5-69FzCLbhv7Iu3UWvVkJgEWX32jR1NkllUrrek0JSUq7PTFepF988cukiRT2VsPeovccOJdJHbrnVOd6hANAkowaevqxiInf0iENLB48HSVHNXvP79D9A79L4_CqpnPKDY7xV96UczTfTMqTwsSqPKgR14Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
برزیل
🇧🇷
-
🇪🇬
مصر
🏆
رقابت‌های دوستانه بین‌المللی
🌍
🕔
بامداد یکشنبه ساعت ۰۱:۳۰
🏟
ورزشگاه کلیولند براونز
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
برزیل در
۱۰
دیدار اخیر خود،
شش
برد و
یک
تساوی کسب کرده و در
سه
بازی شکست خورده است.
✅
مصر در
۱۰
دیدار اخیر خود،
پنج
برد و
چهار
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر برزیل
۳.۴
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر مصر
۱
.
۹
گل در هر بازی بوده
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب :
۱.۱۹
🧠
اگر مجبور به پنهان‌کاری شدید، مسیر اشتباه است.
R16
🅰
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76947" target="_blank">📅 09:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76946">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">روابط عمومی کل سپاه :
بسم الله القاصم الجبارین
فمن اعتدا علیکم فاعتدوا علیه بمثل معتدی علیکم
ساعت ۰۱.۳۰ بامداد امروز چهار فروند نفتکش متخلف با تحریک و هدایت ارتش متجاوز آمریکا بدون هماهنگی و بدون توجه به اخطارهای مقرر نیروی دریایی سپاه، قصد خروج غیر قانونی از تنگه هرمز را داشتند که پس از اخطار، یکی از نفتکش ها مورد هدف واقع شده و متوقف شد و دیگر شناورها متخلف به عقب برگشتند.
به دنبال این واقعه ساعت دو، پهپادهای آمریکایی یک دکل مخابراتی در قشم و یک دکل را در سیریک مورد اصابت دو پرتابه قرار دادند. در پاسخ به تجاوز ارتش کودک کش آمریکا بلافاصله دو پایگاه هوایی آمریکا در کویت به نامهای علی‌السالم و تاسیسات مهم باقی مانده در ناوگان پنجم نیروی دریایی آمریکا در بحرین هدف آتش موشک‌های بالستیک نیروی هوافضای سپاه واقع شدند.
به دشمن متجاوز و کودک‌کش اخطار می‌کنیم در صورت تکرار این شرارت‌ها به پاسخ محدود اکتفا نخواهد شد. مسئول عواقب بسته شدن کامل تنگه هرمز به روی خروج نفت و گاز شما خواهید بود.
و ما النصر الا من عند الله العزیز الحکیم
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76946" target="_blank">📅 07:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76945">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">باز شب شد آمریکا جزایر رو تصرف کرد سپاه هم آبراهام لینکلن رو غرق کرد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/76945" target="_blank">📅 03:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76944">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/76944" target="_blank">📅 01:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76943">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">باز شب شد آمریکا جزایر رو تصرف کرد سپاه هم آبراهام لینکلن رو غرق کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/76943" target="_blank">📅 01:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76941">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الجزیره:
15 نفر از اعضای تیم رژیم جمهوری اسلامی واسه جام جهانی ویزا نگرفتند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/76941" target="_blank">📅 00:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76939">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TXxndGpA35Wz5yNBFTIr2eHZpPUhmgvHXuzBlliJItY_sbw0lgTkJPE1aBuq0C9d1nOJ1B_cOJ6EDilKyXsB5FDhRrsr0OBu8f5YnLO0y4r00wHYqKHzjjJTWRGpx7w19md5piOyvMrB04LQOwmWy8BTI_AhQTyrZXDfVa1YC4jdhCNNRIzISIpARgiuVAG3zAbaCD2aF0p-2C3pYHaTzaQSYkYMtwPHcIZdiQ-iPa3wN4hFqeNSb8jMUE__wbErsnAadw9FwJkj3LneYW2AKvzH0zQyyDMVkPbkz2TeCgEbc1k9YPROTIkMpVTGciJuZpf373CYx7sp9Kg3sjWLMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UsllOPh9ChruR63ASDrgr7bDs8FHOS4msPaAY9xKdnqsXQqS37uOqTTOw5K0SEItJlyAKs8ouPshKp6G2RD84bX7Cs2Dw925KRpIkDNrt8wHVKV7BJM74RezQMN5dQF9YUrkH1c0tCkXocaK2uSoPBkvpVa6_xkmdVbYfnPpYSlfQwQzzoQd9F8e0XTtkEIgQsIws4n54lEyPuUy55ru8bATsifzDW6_4dG_VXMMb4gVYNCFzOGXW2kCFXvp2EMEqe5JHbwQ-N-KpQc4lWHWW1TSe_oUIdGl8N6GLlKNsc7N8so6eC92dg1oSu8kwDaLsElRUZibIcbkbDk4d9UTRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ناو هواپیمابر نیروی دریایی آمریکا(لینکلن یا بوش) دیروز در خلیج عمان و در فاصله حدود 280 کیلومتری از سواحل ایران دیده شده.
در مقایسه با موقعیت مکانی این ناو در چندروز گذشته
این ناو 50 کیلومتر به سواحل ایران نزدیک تر شده
!
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/76939" target="_blank">📅 00:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76937">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4adf695bc9.mp4?token=DE69Rwy4UPhxZkpgnzD46pNyugnF-ili2K6Gpd4z0s-KqbvFD2ski3N4rVBIRYwDOndBbbT6F3tv3JO5wORq1M9lD8WM9CyDWYCDErDm2t3LMO0gz7n11_Z6kBhLTI1FPrCquE7wQpF8mZ22ScNxQoo_WN5HUsbw5H75C810Ft0acwswvS87Atp6KwmVLVBdKgCelBELvchUZg1qh-7Nn8HEZVMxVfGbc5opG19QbzndFoRyME44MUPC6uu3BWXKm4H0OKT6GDmvDjfC6-8oDMC_FuAGqWtt2-C2em2Ut70SB2WIbFPUsRocuPChZtwl9pW3R6Gbf1_XUBcvCX3RCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4adf695bc9.mp4?token=DE69Rwy4UPhxZkpgnzD46pNyugnF-ili2K6Gpd4z0s-KqbvFD2ski3N4rVBIRYwDOndBbbT6F3tv3JO5wORq1M9lD8WM9CyDWYCDErDm2t3LMO0gz7n11_Z6kBhLTI1FPrCquE7wQpF8mZ22ScNxQoo_WN5HUsbw5H75C810Ft0acwswvS87Atp6KwmVLVBdKgCelBELvchUZg1qh-7Nn8HEZVMxVfGbc5opG19QbzndFoRyME44MUPC6uu3BWXKm4H0OKT6GDmvDjfC6-8oDMC_FuAGqWtt2-C2em2Ut70SB2WIbFPUsRocuPChZtwl9pW3R6Gbf1_XUBcvCX3RCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنظرم جی دی ونس  گزینه بهتریه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76937" target="_blank">📅 00:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76935">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ی سریا میگن یوتیوب رو نت مخابرات بدون وی پی ان بالا میاد، تست کنید ببینید واقعیه یا نه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76935" target="_blank">📅 23:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76934">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3980333f44.mp4?token=fXGGQgCcUoQ5ViQy019cnZBVQQqNIbZyHzWDRnfqUWVXWiIL_-xkUZIdyQsCj4gQ6mppPG89t7eLdnF6nMTYdyiI49bvibahSo_7Qx1w1DCbKyh-KTGYz3DAvlZ5z9njluqa6MJs0CEyqK0_YN1WSYLc3dd5r6YBfMX1AVL8Sp7TyKN44Swc_JEolYRMlhTOtK8KdiJYGIX6ahJCVeNdMKGykOUH8RmbqkDDelgx1AvXu7_lgTKErflUZCztiNNKqP35PB8k-_HDh-3gJPj1Ix74mNbRObA6mAT6h51tQEiHbeN57ISjF6ydeX6ijWaBUN65nYMUTEqEh-RQ0WPIrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3980333f44.mp4?token=fXGGQgCcUoQ5ViQy019cnZBVQQqNIbZyHzWDRnfqUWVXWiIL_-xkUZIdyQsCj4gQ6mppPG89t7eLdnF6nMTYdyiI49bvibahSo_7Qx1w1DCbKyh-KTGYz3DAvlZ5z9njluqa6MJs0CEyqK0_YN1WSYLc3dd5r6YBfMX1AVL8Sp7TyKN44Swc_JEolYRMlhTOtK8KdiJYGIX6ahJCVeNdMKGykOUH8RmbqkDDelgx1AvXu7_lgTKErflUZCztiNNKqP35PB8k-_HDh-3gJPj1Ix74mNbRObA6mAT6h51tQEiHbeN57ISjF6ydeX6ijWaBUN65nYMUTEqEh-RQ0WPIrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موزیک ویدیوی شکیرای مناطق محروم (زن مورایس) برای جام جهانی هم منتشر شده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76934" target="_blank">📅 23:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76933">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مهدی ترابی بگا رفته و احتمالا جام جهانی رو از دست بده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76933" target="_blank">📅 23:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76932">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آکسیوس:
به حضرت عباس قسم مذاکرات یه جوری خفن داره پیش می‌ره که پشمام پسر.
نشونه‌های عجیب و غریب مثبتی از ایران دریافت کردیم و مذاکرات به شدت سازنده شده.
ویتکاف امروز رفته بود با کارشناسای هسته‌ای آمریکا صحبت کرده بود تا ببینه شرایط نگه‌داری اورانیوم ایران تو آمریکا قراره چه شکلی باشه و آمریکا یه تیم خفن ۱۰۰ نفره از کارشناسا هم تشکیل داده که این کار رو بکنن.
ما به شدت به توافق نزدیکیم جوری که اختلافای الان رو می‌شه تو نصف روز حل کرد مثلا آمریکا می‌گه بعد از توافق باید تو ۶۰ روز مذاکرات بعدی رو جمع کنیم ولی ایران می‌گه نه ما ۹۰ روز وقت می‌خوایم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76932" target="_blank">📅 22:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76931">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خبرنگار:
فینال NBA که قراره بری تماشا کنی، ارزون‌ترین بلیت اون حدود ۸ هزار دلاره. خیلی از مردم عادی آمریکا توان خرید چنین بلیت‌هایی رو ندارن.
ترامپ:
خب، می‌تونن از تلویزیون نگاه کنن. دیدنش از تلویزیون مجانیه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76931" target="_blank">📅 22:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76928">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">واقعا فاز اینایی که میگن جنگ بخاطر جام جهانی متوقف شده رو نمیفهمم انتظار ندارید ترامپ بخاطر تیم ملی ایران که ویزای ساعتی بهشون داده بیاد جنگ رو توی خاورمیانه که تموم بازیکناش کصخلن , متوقف کنه  عملیات اگه انجام بدن تو خاورمیانه قراره رخ بده نه وسط زمین فوتبال…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76928" target="_blank">📅 21:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76927">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">لطفا اسراییل رو با هسته ای بزنید دهن این قمار باز رو ببندید
ترامپ:
ما در برابر ایران موفقیت‌های بزرگی کسب کرده‌ایم. آنها در موقعیتی نیستند که سلاح هسته‌ای داشته باشند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76927" target="_blank">📅 21:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76926">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">واقعا فاز اینایی که میگن جنگ بخاطر جام جهانی متوقف شده رو نمیفهمم انتظار ندارید ترامپ بخاطر تیم ملی ایران که ویزای ساعتی بهشون داده بیاد جنگ رو توی خاورمیانه که تموم بازیکناش کصخلن , متوقف کنه
عملیات اگه انجام بدن تو خاورمیانه قراره رخ بده نه وسط زمین فوتبال جام جهانی تو آمریکا
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76926" target="_blank">📅 21:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76925">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76925" target="_blank">📅 20:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76923">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">برنامه سیاست با علی و تحلیل اتفاقات منطقه در طی 24 ساعت اخیر
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76923" target="_blank">📅 20:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76922">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">طی 24 ساعت آینده جنگ میشه اگه نشد هفته بعد این پیام رو دوباره بخونید
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76922" target="_blank">📅 20:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76918">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">این از دکترمون
اون از دلو که فتیش زیر بغل دختر داره
اون از داریوش فتیش عرق پا و بدن دخترو داره
اون از حصین که فتیش بی غیرتی داره
من کیرم تو حوزه ی فعالیتمون
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76918" target="_blank">📅 20:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76917">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirhaz</strong></div>
<div class="tg-text">بیاین بهم پس بدین وطنمو
چهار ماهه آزگاره نخوردم پای همسرمو</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76917" target="_blank">📅 20:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76916">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مامان شام درست نکن نمیایم خونه
ما عادت داریم شصت همو بخوریم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76916" target="_blank">📅 20:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76914">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یکی از روی عشق و حال پا میخوره، یکی مثل توماج توی زندان نیروهای جمهوری اسلامی مجبورش میکنن که بخوره. پیدا کنید پرتقال فروش را  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76914" target="_blank">📅 19:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76913">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYEKX2uaWgB39mvfLL9F8FUDdvBhJE3mLVtCzWReTrD_knhWT9DPvkwGerR7PnEZaaJQD4_UXNKe8RaSyoD0RoJLMR4wp_HCl3KdHqAimne_MRqincoGduvUweNRQrA3bBC5DC4PtGvbgbq4_WmE-OxigbwfS-PC3zvDuiL7d3doVEOfgC-UHk1LxO27M7bGvEWL-HF2-uSGbRTeZf7Y1wZbQNWv63e5E5aH4TK5mzqpxeGN233ONgOoW8ZKwVNQ3TUg7O28moyDdqx4Y8FCMiih-g124aZZkds-nS_4BFETq0iDa9A87rX49PmXivOjlwGsJByDh5z4KopA5iCdXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از روی عشق و حال پا میخوره، یکی مثل توماج توی زندان نیروهای جمهوری اسلامی مجبورش میکنن که بخوره.
پیدا کنید پرتقال فروش را
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76913" target="_blank">📅 19:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76912">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دکی: برید پیج گوچی مین محتوای خوبی برا پا دوستا میزاره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76912" target="_blank">📅 19:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76911">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bb569f0ca.mp4?token=fuLMo60XrZTny5-B-nU7SVPdJEb7y_xKr4JMJ_odC4FIh85kqnBo8YPyvidOy5RSu1Z34BIA3ZVOFD5Aafm7vOG-XY0b2XwZsomIuMWDi-ay0EuYOJUJrpHTYoCrt6_fMC6XBS2JYr258FC5RJa8LKbyb1fuzSdiYnefIiq3BQ2YcOCh4wJyqDxrdiSwNLpgMgPZAgvBkFPlEBKVGXCiCeu6oaxPDbIJNJZeVYyvh2Lge2o3fc9ogfQW113Es_3VQyTarcRGys2dpsQX0K1OhvZbUl6dHLBbAHq9DKUIlFUM8C_Ewcs-99SDTSQE_7WTUO3lRgaw5TU9yeLxz9Sm6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bb569f0ca.mp4?token=fuLMo60XrZTny5-B-nU7SVPdJEb7y_xKr4JMJ_odC4FIh85kqnBo8YPyvidOy5RSu1Z34BIA3ZVOFD5Aafm7vOG-XY0b2XwZsomIuMWDi-ay0EuYOJUJrpHTYoCrt6_fMC6XBS2JYr258FC5RJa8LKbyb1fuzSdiYnefIiq3BQ2YcOCh4wJyqDxrdiSwNLpgMgPZAgvBkFPlEBKVGXCiCeu6oaxPDbIJNJZeVYyvh2Lge2o3fc9ogfQW113Es_3VQyTarcRGys2dpsQX0K1OhvZbUl6dHLBbAHq9DKUIlFUM8C_Ewcs-99SDTSQE_7WTUO3lRgaw5TU9yeLxz9Sm6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدممممم ویناک عکس پا خوری دکی رو پخش کرد
😂
😂
@Funhiphop | AmooFirooz</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76911" target="_blank">📅 19:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76910">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ha4PqQMIfoKiIZYb5rnjeV4MhNEjvnFzH0ys_mKGbuitTDhPmOM38t6XooN-_83b05NjFicuOyiNK7ZVX4OxY8DMHxOkNFETb1WssMcveW-5IdjXfLlRelo2AJCrVs_-i-Y3El-DkDwrP1_ug02d__JhOjGJxQTu1A0CmaYCdXSFRtTIiHJlHIJehDTeyCJhgqN9uJoR93wF60nrrC740Sz9R5YtGbfgra0XN7JcutSwOjDQ03d0lLoHHaEEmdndlGaFPpBazkE25KhZlSC2p-BAKNfdi0LpbgrMLSKkbPlxHROqYGgF_IAjIqZ1qvO7RKuXo5uUzLlTHZL95IbVZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیرم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76910" target="_blank">📅 19:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76909">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAqprYMiOVNmZ52dCWb3Y8NS4kPn8abzL7WPtZrIPuxXUXMNbRXuNXqEUe9rjK2LNs9JjNQLu-Znv7Nh1WnLkoQdYoXO7hILnDqI_tYibvU1vSl5ut3G1jbGJYq6_88neVNgQ0zMEoIDtIKFuQXxmCd7p2qihWxNwcv7ByqK2M-nNI4vwzF8rlmhOZwSJPUVFdtMY2BeY4Jspo2qwmKC_RiDEvQsEtrnDl63rIJOdjTKMk6i808Gaz5qSDhQrlT5M4KkjIcySf9rhrlN4SuXjfnzKX1Yddk8VVKMgnnnOkNvKtpbjyfetGOoFJs5FOZa8HoAIoYVLNPX6U88vGehrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی واسطه بخر
۱۰ گیگ ۱۸۰
🚨
۲۰ گیگ ۲۸۰
🚨
۳۰ گیگ ۳۸۰
🚨
۴۰ گیگ ۴۸۰
🚨
۵۰ گیگ ۵۸۰
🚨
با ارائه کد تخفیف hiphop  تخفیف ۱۰٪ بگیرید
سرعت بالا و لینک ساب اختصاصی
📩
همین الان پیام بده
🔤
@wevpn_admin
🦄</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76909" target="_blank">📅 19:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76908">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بیت کوین بگا رفت و به 61 هزار دلار رسید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76908" target="_blank">📅 18:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76906">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1e8ce80ae.mp4?token=H2D94V0MPyZJXOgXN08cIphS7ZNkHnK0Vo5YH0xxB3YzX2AvraWmbp76e6tX3AHCSs3pAe5gN0f8EFveD7S5tT9mTkWksZjL0hge5402c3lFQ6gqChaC3YnFnh3hsnXHprDmQ4upHcaZb6td8lLwgtpqt24JMU3zizqTnbCJc1ENN9kJvkavLqC2Rfb9kWwO2BwS7MYVfcNzlx8SJrN-aNVpFkLBrMs-1Dmaafi4AaKUzScpok5hxBy-UH3cIUwZopykSnj_Z9fFDtUiRGEcusofchusKHCBfSoWgbHhzWSVuw_bxPj_El_GAIVA_OLU9GnCpDE99BGT0yFKEJGidA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1e8ce80ae.mp4?token=H2D94V0MPyZJXOgXN08cIphS7ZNkHnK0Vo5YH0xxB3YzX2AvraWmbp76e6tX3AHCSs3pAe5gN0f8EFveD7S5tT9mTkWksZjL0hge5402c3lFQ6gqChaC3YnFnh3hsnXHprDmQ4upHcaZb6td8lLwgtpqt24JMU3zizqTnbCJc1ENN9kJvkavLqC2Rfb9kWwO2BwS7MYVfcNzlx8SJrN-aNVpFkLBrMs-1Dmaafi4AaKUzScpok5hxBy-UH3cIUwZopykSnj_Z9fFDtUiRGEcusofchusKHCBfSoWgbHhzWSVuw_bxPj_El_GAIVA_OLU9GnCpDE99BGT0yFKEJGidA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیت دکی و خلصه بزودی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76906" target="_blank">📅 18:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76903">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnDWbNOhg46xJgDIWf43Es1-hZZIfFi7A7Z6HzTVcPeXW05EBA9sVqVIxTUZJgXAC24Mb1HyD85t9DEYBI3MikJIeIYf_LeG57j2eLYO5lEHKGc7ym6N9A-RC14SewTT8hXbn9FfYWuDwOYTlChWcf25dlIJT-rcsyzWobIRCcFGpgwM3aYh6QWco-fQtj-t_NBcP5hKcgaHkYnugXK-sRQ_6ETm7kKevAjdhyAVn-daJcY6qJLbHRDk7VsaNlw4xjyTENyAyooF3GTrGdMRFPoWLjcovGo9eOtIJiaj0zZ2rHUYv3mY9X0pXrWeAnwuq0jb6_qfDfxJQaJiF6dYEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه هفته اول بازی های تیم ملی توی لیگ ملت های والیبال
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76903" target="_blank">📅 17:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76902">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghgT7pb13S13_7s4HTCXQvOPIR5o2rh47c1ZGPjYqSGC4Omel2hTdmZMhnu9Ao1Cg1zHrgQmnolfyXbS9zyqA5RKjcReG1Q78yR9Sn-Kx6sRWBI_qyBCAFMmwaZpI8j5BTgO3t44ic8GL1oU0S5zOY9oTSnFVvdqUB2znrXSb8LRU4LV-iJO9npCb0u_rwQLzNsH0rAClt6RQ2nVMUgtV2KjHW1lQvEkLVUeCYMpN1SiW0xN5PNivl9dieG3Uqfp_JMogFGMKf3VyuwJdldsqIcogIH7zXBMO8U25fd5Z4ZNaYkYa0OeRr6JINGnTaOe2NNpyQQbJfnGHv772VvZUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام رونالدو فن یادته سر این بازی چقد مسی رو مسخره کردی؟
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76902" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76899">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">راستی یاسینی هنوز تو زیرزمینه یا بالاخره فرار کرد؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76899" target="_blank">📅 16:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76898">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnC46AasKwoiQPhITYtpi9Bg4TSyWGeNWC4PLsVzhj_DbWH44-jfLGetjh-W2ME0SHxf0kXyBMM9hCeorzvYQn7-uouWcqx6LiZJ9ZpYJiSWqshUNwfdZLmtnq-yNqYU5f7s1XIr_fmhJNIRwM0t_O02gTFPm5w98F2S4lv0XG_ddwvOWcHTu6nzQ3L7_NVsBDoYnnbk3mGSXtU0zY995VdfuDNOwDmL2Ka4qlZeBh8yDHzLn3ql5BLSaFW6ys-4NPz7zBzU6iP7SW4l1fHIn8YKTeg-TIUfRZYQH0PR5J9CEvMYV0ANJpWTp0zuliEbuXVKAJ2qlg-0_Qj7OeMWVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستید ملکه جدید فرانسه بزودی قراره گلشیفته فراهانی بازیگر ایرانی بشه؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76898" target="_blank">📅 15:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76897">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نروژ برا جام جهانی عجب حرکت خفنی زده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76897" target="_blank">📅 14:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76896">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmUYnc0oiwbbv0wVUJjCZNuKsFa5ZTmtQMekvbkOl-0vWFnUoYse00A55jF4TPvJaD0vDDxK-OUCtjx0kyb7FWWS8gTaxnldjSusdzv8vVNQghnbTFpCS2IkyvoJgI1kDyQxuXSbbxfiv4Bt2i-I7uJryv6-DaTkIqkFzhZ4p554sGgsPLdeIGOPfY_H38Zi1UuYHzOTeaaWufWVeaxL8AzSMzRohBjOLjAog2JLBNBsL2sbllRhZnMwAoxqC1aQz07W7ul9juHlToRBFmODbhWFZ8I1MvetiPa-40nGsMnEbptqolJoIF4tGqIQfaGcAFJKwmD5xqkP35n8Ion70g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نروژ برا جام جهانی عجب حرکت خفنی زده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76896" target="_blank">📅 14:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76895">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نزدن رعد و برقه نترسید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76895" target="_blank">📅 14:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76894">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اسرائیل جنایتکار حملات خودش رو به جنوب لبنان دوباره آغاز کرده، خواسته این مردم حمله به صهیونیست های کثیف و حمایت از برادران لبنانی ماست، لطفا بزنید، لطفا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76894" target="_blank">📅 14:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76893">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وای اگر قالیشاه حکم جهادم دهد.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76893" target="_blank">📅 13:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76892">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3tOzwm7AUcYCTEbT6DgNhuJKl_BlalkYtiFQbjNN4KIjR90lctBwr0skaD9vR-xbJ2fdwdt4YUY_JSeUQR0tkTHufjF6bNGyanf7W9UF_IOni8AMbAf4Gjf0wJS2qKTUuZ0sxSz8vud7N0HnA1ukp6qgA1qEVrx4XS7nG98MKPDwi4gfapzZfv8YU5TbDQYlsab_3E1MgT5IW003O2an1MU61v1U0iyUKpQti1U9TfrhosU3Pm3XyoyzOu6yIOstV-x5P0GRmS0pqUKI-S6YyJYyeKTlKtcd-CgS70BhzvtA3FUEpVelJaeTCFn0rs3HHBy1fsa2MoGfGkWbVbS6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76892" target="_blank">📅 13:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76891">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مرکز ملی فضای مجازی:
طبق بررسی های فنی و ارزیابی‌ های عملیاتی که انجام دادیم، قطع اینترنت الکی بوده همچین تاثیر معناداری روی خنثی‌ سازی حملات سایبری پیشرفته نداشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/76891" target="_blank">📅 13:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76890">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4cedd5da.mp4?token=UzzW2QHp1H07s12z_DAbs5aYnCM8khkjQ_qhdh8Rntnrxxa66rvdI7a9czBIt9WPTEQGrAnOFISgs-3M7LOFVyOl61ZMH2ACZOZUV4UbAU5y_8WOyRlPhKIOzitIxTxhKHDZHpKok3vL-0bZKZTD0ve7xr60PXJ_BVOQ1vXo-PwlpCxG_haxYL3kfh3bD6tsegoGwx75GSkJdqhGPc1mh70i5yEkUgUxLbytMYQbKfCEVFjquOZdaBYP9E7MIfTs7X9PrN0xYHB30AepN5zB2mFfaD9KH8Z7wSnGIEF6XVMV9HE2qEcO0hWjtr-xnDF8Q8qWtRJ76lna1YRORRFadw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4cedd5da.mp4?token=UzzW2QHp1H07s12z_DAbs5aYnCM8khkjQ_qhdh8Rntnrxxa66rvdI7a9czBIt9WPTEQGrAnOFISgs-3M7LOFVyOl61ZMH2ACZOZUV4UbAU5y_8WOyRlPhKIOzitIxTxhKHDZHpKok3vL-0bZKZTD0ve7xr60PXJ_BVOQ1vXo-PwlpCxG_haxYL3kfh3bD6tsegoGwx75GSkJdqhGPc1mh70i5yEkUgUxLbytMYQbKfCEVFjquOZdaBYP9E7MIfTs7X9PrN0xYHB30AepN5zB2mFfaD9KH8Z7wSnGIEF6XVMV9HE2qEcO0hWjtr-xnDF8Q8qWtRJ76lna1YRORRFadw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه اوه جنگ داخلی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/76890" target="_blank">📅 13:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76889">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تون 1.5 دلار شد
Make Pavel Mom Great Again
#MPMGA
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76889" target="_blank">📅 12:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76888">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تو هند 4 تا دختر یه پسرو دزدیدن بردن بهش تجاوز کردن.
پسره الان رفته برا باکرگیش شکایت کرده.
دخترا هم دستگیر شدن.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/76888" target="_blank">📅 11:48 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
