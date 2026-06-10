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
<img src="https://cdn4.telesco.pe/file/WaIisjjQRvtJP1DajXDstszTfTRPLKR4X8fQf9fJ5EnPMvBY97-C01z0C0_7slXrTk5fAmPmlzff651eV_Rqikq0CPN4umyDoRlxKU0mujeJrTN16nisPHESGFUIWArJzqtoMhDaUpvL8iIxxxmIcIVjwj6jKDHsBHgug0rD8-C90saEmHAEVoRNVrLrlhRISXPwoxR6CcnujSdQcGf6sMkNcZSJdqXm-fGCHB2VMANqHb8wdnlXg6MLJXGSiuZdtoMoA1T3jf20-4SFa7rj9LGKXH4Py9A-os4xiJPr92bSm2izwv4l6-u-jcYj8z2ue8JJjNBwDXnJxEF5v0-Eyg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.62M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 18:02:50</div>
<hr>

<div class="tg-post" id="msg-658070">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AINTvgvswRHasVBHL7hHQRglAXaVCw8J_A3yiObhaVt_XBosZJgyMQ6IlTAlhRAPhnDC6_W9uRWRZKi3-1FmM5ESLU3nxELsuS4LwizbhIkFjZPBy0H-jLNASUQyqlM2kehjbhZ3wX1iwgVm8l5z3U67GMXn-uC4qdAPpf3Tg-Vx4LzBkL8mkUJbt61hGqZBakBi30Swx97_lCnR0migQghqS9vSAmvb-vVysPNAt97O-C_lHpLvgQkTE4F1u1hYGT3zMzmOkPd6Gi5J57yzATYfXlBMfPAB5uI-pwUJ1FmjM91SLjc81Ua5eafc-_dPzkUpULEUFItb-9mhe0Cw4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویب قطعنامه علیه ایران در شورای حکام؛ تهران: پاسخ می‌دهیم
نمایندگی ایران در وین:
🔹
شورای حکام آژانس با رأیی ضعیف قطعنامه‌ای سیاسی درباره فعالیت‌های هسته‌ای ایران تصویب کرده است.
🔹
ایران از حقوق مسلم خود کوتاه نخواهد آمد و به این قطعنامه پاسخ خواهد داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/akhbarefori/658070" target="_blank">📅 18:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658069">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ترامپ امشب سخنرانی اضطراری برگزار می‌کند
دونالد ترامپ:
🔹
امروز ساعت ۵:۳۰ عصر به وقت ساحل شرقی آمریکا یک سخنرانی اضطراری ارائه خواهم کرد./ خبرفوری
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/658069" target="_blank">📅 17:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658068">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1RLa3dMZwhfg5Wkvr4IW7gj4aryyi_v_Un2j21BFUPIXaKEZKluGZhzr3YIWHD87D3J_LJmajE8-Dax4Sz8lwDselceO4Fq8Wigoq8_pK0YBvjkjAJtP584cWR0irHMGIAE6C-W-qJ3I6bvRDeoK85f1nW4pXbpk-8EbRZvi2ovG3gLx5Qfpzx_S0r0JIWaHQrPIBlqHRV1sw6l2NvNivOd5z3R1viiBxU-qfBhBa-rkBVmDnAtGQu84F6mjc3Gy9CLcaqVCdJS-z9GjRwutTfCQ0TJlQ9J7aUE_FLoG1DuLJ8zH0BX3sjzrC_8ObtLAyvGnpQm5WfZaK0m-Ipn-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایتان لوینز، روزنامه‌نگار آمریکایی: ایران در تمام طول جنگ یک دانش آموز را هم نکشت
🔹
ایالات متحده ۱۵۰ دانش آموز ایرانی را در ۱۰ دقیقه کشت. ایران در تمام طول جنگ یک دانش آموز را هم نکشت. چرا ایران به‌عنوان «طرف شرور» تصویر می‌شود؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/658068" target="_blank">📅 17:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658067">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">حمله تند کارشناس شبکه افق به صادق زیباکلام: زیباکلام لعنتی بیشترین نفع را از ساختار جمهوری اسلامی برده است ولی به رهبر شهید توهین می‌کند/ رهبر شهید ما هنوز دفن نشده است ولی زیباکلام به ایشان اهانت می‌کند و می‌گوید آن که مزاحم همه بود دیگر نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/akhbarefori/658067" target="_blank">📅 17:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658066">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-text">🔸
روایت مخاطبان خبرفوری از بازار مسکن
🔹
ارسالی از البرز:
سلام وقتتون بخیر توروخدا صدای ما مستأجران روبه گوش مسئولین برسونید واقعا کم آوردیم هرساله چقدر اجاره بها افزایش پیدا می‌کنه مگه مامستاجرا آدم نیستیم که ی زندگی خیلی ساده برامون بشه آرزو.
🔹
ارسالی از مشهد:
با سلام از مشهد هستم شمارو به امام رضا به داد ما برسید اجازه خانه‌ها و رهن خیلی بالایی مگه چقدر حقوق میگیریم خرج خونه.پول برق گاز آب تخلیه چاه به خدا موندیم با دوتا بچه چکار کنیم تورو خدا یه فکری برای صاحبان خانه بکنین لاقل اجارهارو بیارند پایین که شرمنده بچه هامون نشیم
🔹
ارسالی از کرمان:
سلام تشکر می‌کنم بابت این کانال اطلاع رسانی فقط خواستم بگم به داد ما مستاجر ها برسید خواهش میکنم متاسفانه صاحب خونه ها خیلی بی انصاف شدن تواین شرایط که خودشون دارن می‌بینند.  آخه این انصاف نیست نمی‌تونیم هیچی بخوریم هر چی داریم باید بدیم صاحب خونه تو رو قرآن به داد ما برسید.
🔹
ارسالی از شیراز:
سلام خدا قوت.اصلا نظارتی روی قیمت اجاره خانه نیست مالک میگه میخاید این قیمت نمیخای خوش آمدید ، یه سامانه ای باید راه اندازی بشه که راه دور زدن املاک یا مالکان گرفته بشه ، مثلا اگر بیشتر از یه مبلغی بخان اجاره بگیرن ۱۰ درصد میاد روی مالیاتشون یه همچین چیزی،  لطفا شما که زبان رسانه رو بلدید این متن منو با یه اصلاحاتی که بلدید به عنوان یه پیشنهاد مطرح کنید . ممنون
🙏🏽
🔹
ارسالی از پرند:
سلام وقتتون بخیر  تو شهر پرند کسی نیست نظارتی کنه هر جور دلشون می خواد خونه رو میدن اجاره کسی هم نیست جلوشون بگیره ما تو چهار جنوب زندگی میکنیم سال پیش ۲۵۰  رهن نشستم الان املاکی به صاحب خونه گفته ۲۵۰ رهن اجاره بها ۱۶ ملیون مگه من کارگر ساختمانی چقدر در آمد دارم که ماهیانه هم کرایه خونه بدم هم خرج خونه خدا از املاکیای بی انصاف نگذره که رحم ندارن فقط به فکر جیب خودشونن  اگه قانونی باشه   درست وحسابی املاکی  حساب دستش بیاد ما مستا جرا اینقدر تو استرس واضط اب نیستیم میگن ۲۵ پر صد اضافه بشه به قرارداد ولی املاکی ۲۵۰ در صد میزاره روخومه ها ما شکایتمو به کی کنیم
🔹
ارسالی از اصفهان:
سلام وقت بخیرمن ازاصفهان هستم واقعاکسی نیست که به دادمامستاجرین برسه شوهرم بازنشسته است مستاجرهستیم مگه چقدره حقوق یه بازنشسته اضافه میکنن که اینقدر هم اجناس راگران میکنن وهم مبلغ رهن واجاره همراه خداکم آوردیم زیربار گرانی ورهن واجاره له شدیم آیاکسی صدای مارامی شنود مادرکشوری هستیم که همیشه ازهمه دنیاجلوتربودیم پس چی شده که حالااین همه بدبخت شدیم ممنون که پاسخگوباشید
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/658066" target="_blank">📅 17:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658065">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfvwxfXbTW3wIWwijilcaaLL34GWBY6k7OCRY-V1Sxx337OMdVNkxIj9xSg-LwwVSks46eq-ECh6g4Iy5c5EJ3VC0r1NjTr0-qt2L90sNJU1a9612ntQMzAV3NjpSYn0ouL53mz8YZiqb1j1IVSevIdpBa_i0Og08rh8qpU1CigpIJq9kkuH6MJclTPwOIfuCXodT7DqEdiJrw0p5T4u3SZzEinUjYXMZUMqcOivshTjvy6Bp_vR48t_NKfxwyEFVJ7KkGQcN68FhuEniCl7L2kRIVtp8qHixW9TndOeQya13j7OkEVf80BzBfE1SF_iCEyZ0rqz7uv1EC59s_PncQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ساحل فیتوپلانکتون، چابهار
🇮🇷
#ایران_زیبا
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/658065" target="_blank">📅 17:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658064">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
بقائی: آمریکا با پیام‌های متناقض به روند دیپلماتیک آسیب می‌زند
سخنگوی وزارت خارجه:
🔹
آمریکا با ارسال پیام‌های متناقض، تغییر مکرر مواضع و نقض‌های پی‌درپی آتش‌بس به روند دیپلماتیک آسیب می‌زند؛ ایران هرجا لازم باشد از دیپلماسی و در صورت اقتضا از توان نظامی برای دفاع از کشور استفاده می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/658064" target="_blank">📅 17:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658063">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
تأیید خسارت در پایگاه نظامی «رامات دیوید» در پی حملات اخیر ایران
ارتش رژیم صهیونیستی:
🔹
در جریان حملات اخیر جمهوری اسلامی ایران، پایگاه هوایی «رامات دیوید» مورد اصابت قرار گرفته و دچار خسارت شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/658063" target="_blank">📅 16:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658062">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ارتش عراق: پرونده انحصار سلاح وارد مرحله اجرایی شده است
🔹
ارتش عراق از آغاز مرحله اجرایی الزام‌آور طرح ساماندهی گروه‌های مسلح و انحصار سلاح در دست دولت خبر داد./ ایرنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/658062" target="_blank">📅 16:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658061">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
«خانه صانعی» جان گرفت
🔹
عمارت شهرآرا، به عنوان خانه طراحی شهری و مرمت بناهای تاریخی شهر تهران، به کانونی برای گفت‌وگوی میان طراحان صنعتی، معماران، مرمت‌گران و شهروندان تبدیل خواهد شد.
این مجموعه علاوه بر اجرای پروژه‌های مرمتی، طراح و مجری پروژه‌های بزرگ در حوزه مرمت، مبلمان شهری، نورپردازی‌های شهری، طراحی فضاهای شهری، پلازاها، فضاهای مکث و همچنین المان‌های شهری در سطح شهر تهران است.
استقرار این مجموعه در خانه تاریخی صانعی، عملاً این عمارت را به یک پایگاه زنده برای تولید تجربه، آموزش و تبادل دانش در حوزه مرمت و طراحی شهری تبدیل کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/658061" target="_blank">📅 16:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658060">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
افزایش اعتبار کارتکس گواهینامه از دو به چهار سال
پلیس:
🔹
از ابتدای تیرماه مدت اعتبار کارتکس آموزش و آزمون رانندگی از دو سال به چهار سال افزایش می‌یابد تا متقاضیان فرصت بیشتری برای تکمیل مراحل دریافت گواهینامه داشته باشند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/658060" target="_blank">📅 16:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658059">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJfIC_NI8xtYdLuQn5Gf07blU-_Z7jP97lOkKhQUypDD1h4_n3vVNom1DyVzt5WYr-tvr6BjxIxX8vzAkbY_XWwGu74VtNAFhCjkejcQp0y5GukLhXpuc_N1oJfKKntaxmeKfURXzHAjMqPRHPSA0TCncwRhsHLlnzNgzT3BHeKOQr9vNQNrZDcBYOkDC0KQXBUDqmXwRboFiDeSZ1xX4IwGhcFkY9PYzUxaBhQWpUIJMmIYD9h6le3tL8MwZYYIkQh5q2ZyD-R1hXWAYChU7PBQ_lVaYvdpVaK0G39yRjErplSyJf3y5BrIr62pEdXrR4DWWs05If4QpF9ODZobMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلای جهانی در یک روز ۱۲۰ دلار ریزش کرد
🔹
قیمت جهانی هر اونس طلا در معاملات امروز با ریزش ۱۲۳ دلاری حدود ۳ درصد کاهش پیدا کرد و به ۴۱۳۴ دلار رسید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/658059" target="_blank">📅 16:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658058">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
بقائی: جام جهانی نباید بهانه‌ای برای آزار تیم‌ها شود
سخنگوی وزارت خارجه با اشاره به برخوردهای نامناسب با برخی بازیکنان و کادر فنی برخی کشورهای حاضر در تورنمنت در مبادی ورودی آمریکا:
🔹
فوتبال باید زمینه رقابت سالم و نزدیکی ملت‌ها باشد و جام جهانی نباید به فرصتی برای تحقیر و تبعیض تبدیل شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/658058" target="_blank">📅 16:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658057">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
سفر هیات قطری به تهران
🔹
هیاتی از قطر برای رایزنی درباره روابط دوجانبه و رویدادهای منطقه‌، وارد تهران شد.
🔹
قرار است در این سفر، افزون بر بررسی روابط دوجانبه و تحولات منطقه، درباره آخرین تحولات مرتبط با روند دیپلماتیک برای خاتمه جنگ تحمیلی آمریکا هم گفتگو و تبادل نظر شود./ صداوسیما
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/658057" target="_blank">📅 16:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658055">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQZWJspkyirDvQ6kdiobwP5XUVff-zcLwjKZwncnrHMW5fHeQTEIvUoeqGzgM8jFmwIKBX5j6NSmbAC_mAxoScgsaxdvTXPySxKO49GcOcTmiqUUCGXBajEXTfw53qcH0iAgxEpElv38RMiJzeCP6gdWIImaXgXN5XqdAW2WhE8DbBPfV_nJ9crL4f4rUc2y1eFo7V41Z1h_lghYFyRzoES34LIDoRJc_aaolkpHiYS9ni5JfNmC-ehLasCnupJk2SGyQWf8jwNsLL1XEK1ZALdXFeouVbZv83nJZ_q9-pF_8xYPaQqzB6lBEmGo_sPstDgDo-6OfEmA4FshpBJxVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سد منجیل پر از آب شد
🔹
به لطف بارش های گسترده اخیر سد منجیل نسبت به پارسال پر آب شده است.
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/658055" target="_blank">📅 16:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658053">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
قطعنامه ضدایرانی آمریکا امروز در شورای حکام به رأی گذاشته می‌شود
🔹
پیش‌نویس قطعنامه ضدایرانی آمریکا با حمایت انگلیس، فرانسه و آلمان امروز در شورای حکام آژانس بین‌المللی انرژی اتمی به رأی گذاشته می‌شود.
🔹
در این قطعنامه از ایران خواسته شده درباره تأسیسات هسته‌ای…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/658053" target="_blank">📅 16:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658052">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3b7d6fc75.mp4?token=aRj_mNko-r_l-cKrVBY-UBhL8153u-s0EQnM5BTNM4kbGRZ4wa1W3ZU0e1GCi4zf5nf9Gjh00nrTjNkZH8QXFdQ27ilK7iBmpIOh0iTGk0SAW-OVqCsuj7Fr3TrG235Q-5KrskulKgkQS7hXnIryS0Psr7ivYVzgGt4U8G4FphguQgVsQMaQ8ou2lxvl_E7pZFZpO_GplcEr86--dgn7O4AGcbdXdfWghaBAb1OTQ_aEuvUxUmjlSEOOLrkameVu6MKLHeJTCoiXFLq3IDJ0uy6PSPNsKCIiiX4-tFyd1ZkE_oLoIDRbf1lr7EhMa827JwSXDXEeF0o5X4OWg64GmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3b7d6fc75.mp4?token=aRj_mNko-r_l-cKrVBY-UBhL8153u-s0EQnM5BTNM4kbGRZ4wa1W3ZU0e1GCi4zf5nf9Gjh00nrTjNkZH8QXFdQ27ilK7iBmpIOh0iTGk0SAW-OVqCsuj7Fr3TrG235Q-5KrskulKgkQS7hXnIryS0Psr7ivYVzgGt4U8G4FphguQgVsQMaQ8ou2lxvl_E7pZFZpO_GplcEr86--dgn7O4AGcbdXdfWghaBAb1OTQ_aEuvUxUmjlSEOOLrkameVu6MKLHeJTCoiXFLq3IDJ0uy6PSPNsKCIiiX4-tFyd1ZkE_oLoIDRbf1lr7EhMa827JwSXDXEeF0o5X4OWg64GmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راهنمای کامل خرید طلای آب‌شده  #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/658052" target="_blank">📅 16:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658051">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">🕊️
هر روز ما به مدح علی می‌شود شروع
هوهوی صبح باد صبا مدح حیدر است
▫️
جلوه‌ای از حضور پرشور و دل‌نشین مردم در مهمانی بزرگ عید غدیر در برنامه «پناه غدیر» مشهد مقدس
💚
▫️
این اجتماع باشکوه، به همت هیئت قرار و مجتمع فرهنگی امیرالمؤمنین برگزار شد
@Heyate_gharar</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/658051" target="_blank">📅 16:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658050">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Age3bKP-5qQkuCpMn9hvh2bk1KZ88aACYv86UvyCUZit4OUGF56VHtgHOYdQ0BeyOoRwrw6HfcpoOoMIS5i8c2YK_Y9iJgGD8F4adbPcFXamlO1_fJmLjc9V1RI-nnJVAEc2VVzGc_oyiM2PiFnv1XMjSj_TqVAv4BqoY42VVplALNdT_A8FBJj7wrptflM7OJn0zblP4DOPzE1fNB2bIJZjKwEZqefKFp1n6oJwSZjzjO13NtPaBLZuO_lI3FmUmkBJMB2eR88EbFvN1ESQ4MybEoY2DTA1wnyB-zomKNUPxSc6bdE20fRj6i4LTzPfC7FAf7wOnh28d1_A29x98g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط اعتماد اروپایی‌ها به آمریکا؛ فقط ۱۱ درصد، واشنگتن را متحد واقعی اروپا می‌دانند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/658050" target="_blank">📅 16:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658049">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
جزئیات جدید از حملۀ پهپادهای ارتش به پایگاه آمریکا در بحرین
یک منبع آگاه نظامی:
🔹
بامداد امروز پایگاه هوایی شیخ عیسی و یک سایت راداری آمریکا در بحرین با پهپادهای جدید ارتش هدف قرار گرفتند.
🔹
در حملات اخیر به پایگاه‌های آمریکا در بحرین، کویت و اردن، حدود ۷۰٪ اهداف با موفقیت مورد اصابت قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/658049" target="_blank">📅 16:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658048">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
واکنش نتانیاهو به سخنان اردوغان: در جایگاهی نیست که بخواهد به اسرائیل درس اخلاق بدهد
🔹
نتانیاهو، رئیس‌جمهور ترکیه را «دیکتاتوری یهودستیز» خواند و مدعی شد که او علیه کردها مرتکب نسل‌کشی شده و مخالفان سیاسی خود را زندانی می‌کند، بنابراین در جایگاهی نیست که بخواهد به اسرائیل درس اخلاق بدهد.
🔹
نخست‌وزیر اسرائیل در ادامه مدعی شد که ارتش اسرائیل «اخلاقی‌ترین ارتش جهان» است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/658048" target="_blank">📅 16:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658047">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
یک نشانه نگران‌کننده برای اقتصاد؛ شامخ به کف ۸ ساله رسید
🔹
شاخص مدیران خرید (شامخ) در فروردین‌ماه با ثبت عدد ۳۸.۵ برای کل اقتصاد و ۳۷.۴ برای صنعت، به یکی از پایین‌ترین سطوح ۸ سال اخیر رسید؛ رقمی که نشان‌دهنده رکود شدید اقتصادی است.
🔹
افت تولید، فروش و سفارشات جدید و همچنین افزایش تعدیل نیرو در صنعت از مهم‌ترین نشانه‌های این وضعیت است.
🔹
کارشناسان اختلال اینترنت، کمبود مواد اولیه، جهش نرخ ارز، محدودیت‌های ارزی و نااطمینانی ناشی از جنگ را عوامل اصلی این افت می‌دانند./خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/658047" target="_blank">📅 16:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658045">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/973ea2928b.mp4?token=Bi1oWDxwnSa9u3aI0bX7hLHtyJsS1c-sZQEy1yOL5z8a5jdYusHYf6i1cjqHUuU3FBK4-m39ryFEO94vXoqjYF3zPO1OhWctb0mBr34Ndr9gZvTdr2oK8lRzKwzPrBfjrKvrobUjaDU9s4tmYFb4Y-DQGDBn5MEDwvcG_8uscIO8cEQE9fiN-44sjWGXi-p-vhP34tVxDgnqtzj8BpgdnLcfP7CTtvoftNxxkgsp5U6nbGLhvt4XO6iV9KGKKLnNjxnIKexeujrnxpcHHZfrrWTGpypVVyOIxA9T4arwnncVoM4di5vblGTXVQUsiVY9LSGOxiQVl-QRZg2_4E5QmBO_a8wH0rmfISUJfAcpstvuTNXuvLwoyewJQSewgk196ycFsdqG_OqAVqhFVYcqbW1afUblh7bsigb9-1bQEroT4Mk6I5xtGuQIlAPqZcJZ-xnLV00xeX7jQ4EG2qsQpo631Cl_s9dhomHE9ZHzuKZESG_odhkAHcXdNI4_gJuFdapkqlcbFZMlHCyPR9lywJyHYuZnInb-6JCadL5jAlGwH6ZSTr7cXOGyHyxQSSVTtrebMlrXZR3WH7WJBi81tclu7iQzPA1ml6X1_SnHKTgV3w1ZGGlsnBxMYgQKbIJ03jSFIZWsUMigVIcUy0sqs3h4eN-5XdQizR1iXvzdF0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/973ea2928b.mp4?token=Bi1oWDxwnSa9u3aI0bX7hLHtyJsS1c-sZQEy1yOL5z8a5jdYusHYf6i1cjqHUuU3FBK4-m39ryFEO94vXoqjYF3zPO1OhWctb0mBr34Ndr9gZvTdr2oK8lRzKwzPrBfjrKvrobUjaDU9s4tmYFb4Y-DQGDBn5MEDwvcG_8uscIO8cEQE9fiN-44sjWGXi-p-vhP34tVxDgnqtzj8BpgdnLcfP7CTtvoftNxxkgsp5U6nbGLhvt4XO6iV9KGKKLnNjxnIKexeujrnxpcHHZfrrWTGpypVVyOIxA9T4arwnncVoM4di5vblGTXVQUsiVY9LSGOxiQVl-QRZg2_4E5QmBO_a8wH0rmfISUJfAcpstvuTNXuvLwoyewJQSewgk196ycFsdqG_OqAVqhFVYcqbW1afUblh7bsigb9-1bQEroT4Mk6I5xtGuQIlAPqZcJZ-xnLV00xeX7jQ4EG2qsQpo631Cl_s9dhomHE9ZHzuKZESG_odhkAHcXdNI4_gJuFdapkqlcbFZMlHCyPR9lywJyHYuZnInb-6JCadL5jAlGwH6ZSTr7cXOGyHyxQSSVTtrebMlrXZR3WH7WJBi81tclu7iQzPA1ml6X1_SnHKTgV3w1ZGGlsnBxMYgQKbIJ03jSFIZWsUMigVIcUy0sqs3h4eN-5XdQizR1iXvzdF0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جاده بهشتی الموت به تنکابن
#ایران_زیبا
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/658045" target="_blank">📅 15:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658044">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
اعلام جرم جدید دادستانی تهران علیه زیباکلام؛ قرار نظارت قضایی زیباکلام تشدید شد
🔹
با وجود اعلام دادستانی تهران مبنی بر قرار نظارت قضایی زیباکلام مبنی بر ممنوعیت هرگونه فعالیت رسانه‌ای و تولید محتوا در شبکه‌های اجتماعی به مدت سه‌ ماه، این فرد با نقض این قرار،…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/658044" target="_blank">📅 15:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658043">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18337c03b1.mp4?token=grhgCOn07S6nC3UVSn4NsBKjFdi-is9iEvciVt8ge0XW7VAoWaKczOZK9e0iFP-YpsmNjl-xFthOksOaWfp3F1ZVAkALzKlywrr-Lh6ySpHuzvznwGsJTf-IT0bmFDdVJ1fQg37_m6-rd9vJbtvZ8VeFoU408NuCJVTutcBKA0ONsNjS18promM5Ng7HlG_TFMTeCD8yr3mBPy6iFAqw3_Z5Tl-GXppWR4YWnfEFWunqe4GsP9blGR6D5_brfOfRUcYGjxE1ujIE3vrbZ5tiy4RNGzmNd9xnpL3siEQCjBCFDntAnT7V_6K3dx0pFW9GnGWk0bzBiUmqtWqhSlw-5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18337c03b1.mp4?token=grhgCOn07S6nC3UVSn4NsBKjFdi-is9iEvciVt8ge0XW7VAoWaKczOZK9e0iFP-YpsmNjl-xFthOksOaWfp3F1ZVAkALzKlywrr-Lh6ySpHuzvznwGsJTf-IT0bmFDdVJ1fQg37_m6-rd9vJbtvZ8VeFoU408NuCJVTutcBKA0ONsNjS18promM5Ng7HlG_TFMTeCD8yr3mBPy6iFAqw3_Z5Tl-GXppWR4YWnfEFWunqe4GsP9blGR6D5_brfOfRUcYGjxE1ujIE3vrbZ5tiy4RNGzmNd9xnpL3siEQCjBCFDntAnT7V_6K3dx0pFW9GnGWk0bzBiUmqtWqhSlw-5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط بالگرد ارتش پاکستان در کشمیر
🔹
ارتش پاکستان امروز اعلام کرد که درپی سقوط یک بالگرد نظامی در منطقه کشمیر (تحت کنترل دولت اسلام‌آباد) همه سرنشینان آن کشته شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/658043" target="_blank">📅 15:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658042">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9247a5c8de.mp4?token=ZsKry5ShhHgL4T3N9k8lMR2k7GtniYoFpec9pHZCW3TvEcjJXU8Fg6_0VKShKvFb7HJslu4VCiYUFKZ2MZkYMFX9W6PMDRzp5p3MuMeGiVxFvTkpjct7Lg9zoVJ0Ulx5Q3jpWRbQA4ufEVfpnElMsISBFqEuoz1rfEbi3GB_3rQEGHbAh0MA4FJbYSqrfMVb9G6fk_U4Cyea2wC9IcP6ll-5a8Jg44nh-797ztPLzzUm7Vdcn1MF-ycVuxbBA6e-GJ8cfK1yx3_ScBg9unhQQLuRyc9Bw0pBLQ3gNz-VORu7_VoEE1XhGK0IKh2tC9IghK0oHUE5NmAr29ck0p5AUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9247a5c8de.mp4?token=ZsKry5ShhHgL4T3N9k8lMR2k7GtniYoFpec9pHZCW3TvEcjJXU8Fg6_0VKShKvFb7HJslu4VCiYUFKZ2MZkYMFX9W6PMDRzp5p3MuMeGiVxFvTkpjct7Lg9zoVJ0Ulx5Q3jpWRbQA4ufEVfpnElMsISBFqEuoz1rfEbi3GB_3rQEGHbAh0MA4FJbYSqrfMVb9G6fk_U4Cyea2wC9IcP6ll-5a8Jg44nh-797ztPLzzUm7Vdcn1MF-ycVuxbBA6e-GJ8cfK1yx3_ScBg9unhQQLuRyc9Bw0pBLQ3gNz-VORu7_VoEE1XhGK0IKh2tC9IghK0oHUE5NmAr29ck0p5AUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلاغی که آرایشگر گراز شد
🔹
در پریمورسکی روسیه، یک کلاغ و گراز با هم همکاری می کنند. ویدیو نشان می‌دهد که کلاغ با آرامش روی کمر گراز نشسته و دارد با دقت تمام پشم او را می‌کند. این کار گراز را از شر پشم های اضافی در این تابستان گرم رها می کند و برای کلاغ هم مصالح ساختن آشیانه راحت فراهم می شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/658042" target="_blank">📅 15:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658041">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
پزشکیان: مدیری که تصور کند برای حل مسائل تنها یک راه‌حل وجود دارد، در واقع شکست را پذیرفته است
🔹
بنده شکست را نخواهم پذیرفت و معتقدیم برای عبور از چالش‌های کشور راه‌های متعدد و ظرفیت‌های فراوانی وجود دارد و دانشگاهیان و نخبگان می‌توانند در شناسایی و به‌کارگیری این راهکارها نقش مؤثری ایفا کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/658041" target="_blank">📅 15:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658040">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دادستان کل کشور: توقیف اموال اشخاص بیش از میزان محکوم‌به یا خواسته خلاف قانون است.
🔹
عارف، معاون اول رئیس جمهور: دولت به دنبال افزایش مبلغ کالابرگ است
.
🔹
اتحادیه اروپا: از دیپلماسی برای حل پایدار موضوع هسته‌ای ایران حمایت می‌کنیم.
🔹
محیط زیست بوشهر: ۲۵ آهوی جزیره خارک قربانی بمباران آمریکا و اسراییل شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/658040" target="_blank">📅 15:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658039">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
طناب زدن با آهنگ تمام قومیت‌های ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/658039" target="_blank">📅 15:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658038">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
کشف کلاهبرداری ۳۸۰۰ میلیارد ریالی در کاشان و قاچاق‌های کلان در اصفهان
🔹
فرمانده انتظامی استان اصفهان از کشف کلاهبرداری سه هزار و ۸۰۰ میلیارد ریالی در کاشان، دستگاه گنج‌یاب پنج میلیارد ریالی در فریدن، ۱۲ هزار لیتر سوخت قاچاق در نایین و چهار تن چوب قاچاق در شاهین‌شهر خبر داد.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/658038" target="_blank">📅 15:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658037">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBcviq9dsAmohcDGLM-exE9mtg_eiN01WIW2_jJSLFnSuzA46AT2EPW0VkdqOiu8ToL8Kq200PgTn4dduE1Lk1C14tw2N4X5xQPDilxMTSUCm6O8FfNQwlc1TjGlvzE0l-K0Ukg5DE-bLDN3UYnZ58az7KZ9yHyHXTGfACPnxmn9xHGm8XYF8fAeilwCQqKV4LMgYcXjxnxFH7QOnehF3kVBgxG6SC9aw9HQ6tKTAuTiCYWhqH9xJa8UM2Qj-KepXuKjPQ8cNJe9jLvYEvPBQfYKrdFAtShPjWY-KKC_X4YIGjRyX2PIKle8C1qK2pvCQUSOKi1JbRODezB6xsP2Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش سفیر ایران به حمله دیشب آمریکابه سیریک: مغولها هم در حمله به شهرها، به منابع آبی آسیب نمی‌زدند
کاظم جلالی، سفیر جمهوری اسلامی ایران:
🔹
‏جامعه جهانی مقابل حملات عامدانه آمریکا و رژیم صهیونیستی علیه زیرساخت‌های شهری و مدنی ایران سکوت نخواهد کرد.‌
🔹
حمله به مخازن آب و تأسیسات خدماتی علاوه بر آنکه نقض فاحش قوانین بشردوستانه بین‌المللی است، جنایت علیه غیرنظامیان است که با هدف مختل کردن زندگی آنها در آستانه فصل گرما انجام می‌شود.
🔹
وحشیگری کنونی، در تاریخ بی سابقه است، مغولها هم در حمله به شهرها، به منابع آبی آسیب نمی‌زدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/658037" target="_blank">📅 15:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658036">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eu7Oxc6VSgrNZzq469abF0nnxWKUBIwEm2VJgg6MB96PrPxfdeHDVaHmyqTdgsgK1TMGGjh5b6HOT4CWj2LT4of0kp1RrNAIK4sfWddZ0vJvf9e5f_quK5k9l56reICXBF1Na15h5aAjMZskPk0rmlWxfW8xBrJQ-7AzwL1ZDLzjeeQe6uIl0WOo0JbVBrsQR9_c9YJvQ8Iv2S_i1DJ78A2QugRYdwobLiPl6dXP0CZfSZIFtsVrCihQU9mFVOJaUSmeru8C3pzIL3LDaYzihkdCyHxVpTghUyS8wYjCtoNOCh5-pZFLqUdqogaa9tY_lCw9db1Pnqzsp2Q53AcPxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیکود نامزدی نتانیاهو برای انتخابات آینده را اعلام کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/658036" target="_blank">📅 15:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658035">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5301cd06f2.mp4?token=rJ8JsfLkHI4pm2fe3cdc-hImgRJ5lljkfqcLcyMwg2gWGvujJV7JI9ucnVRwUMkwZU_Eg2pCAXnox2ErNYV1ELxCl4brpY2x1u3UoQJwbARyxmXYmuXEuEG9a7oHw2RUb-sH53E_oFdHEOF13Z2xC6ZanmYhD8DST5DX0tzMjm1Ln5nXhJI_u_pIxE_zOWOEK3X61TgguDMffcCA9ZbLyf5My6mK95gdXWGgDgNY0s4BaM-svjEg2M8nXM-uDWvNnQBScxNeqayh6Zq0rE30VVdecC3H3ABddIkPC5vlrR_bpZaibWZDsBd2IPhvNh8TiKGArgYbB-RvayWz0VYKIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5301cd06f2.mp4?token=rJ8JsfLkHI4pm2fe3cdc-hImgRJ5lljkfqcLcyMwg2gWGvujJV7JI9ucnVRwUMkwZU_Eg2pCAXnox2ErNYV1ELxCl4brpY2x1u3UoQJwbARyxmXYmuXEuEG9a7oHw2RUb-sH53E_oFdHEOF13Z2xC6ZanmYhD8DST5DX0tzMjm1Ln5nXhJI_u_pIxE_zOWOEK3X61TgguDMffcCA9ZbLyf5My6mK95gdXWGgDgNY0s4BaM-svjEg2M8nXM-uDWvNnQBScxNeqayh6Zq0rE30VVdecC3H3ABddIkPC5vlrR_bpZaibWZDsBd2IPhvNh8TiKGArgYbB-RvayWz0VYKIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپادی به صیدا و شهادت دو شهروند لبنانی
🔹
منابع لبنانی گزارش دادند که در حمله پهپادی رژیم صهیونیستی به خودرویی در شهر صیدا در جنوب لبنان دو شهروند لبنانی به شهادت رسیدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/658035" target="_blank">📅 15:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658034">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
کشف ۱۶۳ هزار لیتر گازوئیل قاچاق در سواحل میناب
فرماندۀ پایگاه دریابانی میناب:
🔹
۳ مشک ماری حاوی ۱۶۳ هزار لیتر گازوئیل قاچاق در سواحل این شهرستان کشف شد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozga</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/658034" target="_blank">📅 15:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658033">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
تکذیب ادعای وزیر ارتباطات درباره مصوبه ۳۲ بندی
🔹
اطلاعیه روابط عمومی مرکز ملی فضای مجازی: روز گذشته وزیر ارتباطات در نشست خبری اعلام کرده بود که مسئولیت اجرای مصوبه تسهیل دسترسی به سکوهای خارجی و ارتقای حکمرانی قانون‌مند که به عنوان مصوبه ۳۲ بندی شناخته می‌شود بر عهده مرکز ملی فضای مجازی است که این ادعا از اساس غلط است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/658033" target="_blank">📅 15:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658032">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWL-VtxLbrBNM_K1P1ZOi-RA09_expSbDIH1uXbpZS5bYhY_9V9crOsK4GDcDk79F27_DMT626xv5wDcfL4LgVkJEyCvsTDDfQ_uymbEWVbSULn55_qBtjiGXox3a28cvzSVLdmNg9xRMD36bLpaSCPXQ9OBoAX6gKf1LdtA1endr_svVJkkZ-oBbC00kSnaoJWaXFb1Bp6MIo4q5utxoWpVUmo52iIRsxThAE2FfofUfLrG6y6OEl_AUqrob0wxPOY-5m5Yg5ycUgPmGlnYY67tWZ6Gh0Gzx24apc7YZorPehhqOmDwcjE3QGW5gcaXLSCRND8juFEVHEcszGq7Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خواب نما شدن ترامپ: ایران حقوق نظامیانش را نمی‌پردازد
رئیس جمهور دروغگو آمریکا:
🔹
رسانه‌های خبری جعلی از گزارش دادن دربارهٔ اثربخشی محاصرهٔ دریایی ایالات متحده خودداری می‌کنند، موفق‌ترین محاصره در تاریخ جنگ‌های دریایی. هیچ چیزی عبور نمی‌کند مگر اینکه ما بخواهیم. این یک دیوار فولادی است!
🔹
ایران هیچ کسب‌وکاری ندارد، حقوق نظامیانش را نمی‌پردازد و هیچ یک از صورتحساب‌هایش را، و به سرعت در حال تبدیل شدن به یک کشور شکست‌خورده است! مقدار زیادی نفت خارج می‌شود. سپاس خداوند! رئیس‌جمهور دونالد ج. ترامپ
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/658032" target="_blank">📅 15:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658031">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
قطعنامه ضدایرانی آمریکا امروز در شورای حکام به رأی گذاشته می‌شود
🔹
پیش‌نویس قطعنامه ضدایرانی آمریکا با حمایت انگلیس، فرانسه و آلمان امروز در شورای حکام آژانس بین‌المللی انرژی اتمی به رأی گذاشته می‌شود.
🔹
در این قطعنامه از ایران خواسته شده درباره تأسیسات هسته‌ای بمباران‌شده و اورانیوم غنی‌شده آن‌ها توضیح دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/658031" target="_blank">📅 15:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658030">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91330768c7.mp4?token=DnWJ8Vu1JDmkycfTnMSGypqpV_2peXcRAaA3-OFuWyymb5yVrsj1NmMIecf0vwItm0tAZ59WkYlDy3htHZuJ6DGwsepxghd7m7Z5rlM9wu49VZIfjLJ1k-JzNpiNBddw26ZSx1N93-LzzgQ7ATm_fK23k74vj0kCSaEgN7bQPlpzK6eGoLH8JnmLPtqhe2YiB7_m6nJBSqpIzWXj_L5G0MQuE95UT04qt6I0rnq4zQ_xCCYprW7mlhkmZMCQkpsJTh1o0eq1S-bsgrNK5nCxWs68I1-ec18-8V3DSytYelqDxni27bvHkQXbo8GqMuAjRl5I-3k3l4lLQjsqzbSbSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91330768c7.mp4?token=DnWJ8Vu1JDmkycfTnMSGypqpV_2peXcRAaA3-OFuWyymb5yVrsj1NmMIecf0vwItm0tAZ59WkYlDy3htHZuJ6DGwsepxghd7m7Z5rlM9wu49VZIfjLJ1k-JzNpiNBddw26ZSx1N93-LzzgQ7ATm_fK23k74vj0kCSaEgN7bQPlpzK6eGoLH8JnmLPtqhe2YiB7_m6nJBSqpIzWXj_L5G0MQuE95UT04qt6I0rnq4zQ_xCCYprW7mlhkmZMCQkpsJTh1o0eq1S-bsgrNK5nCxWs68I1-ec18-8V3DSytYelqDxni27bvHkQXbo8GqMuAjRl5I-3k3l4lLQjsqzbSbSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌بازی ضدچینی تایوان با موشک‌های آمریکایی
🔹
تایوان برای اولین‌بار با سامانه‌های موشکی توپخانه‌ای هایمارس ساخت آمریکا شلیک واقعی انجام داد و حملات دقیق فرامنطقه‌ای را شبیه‌سازی کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/658030" target="_blank">📅 15:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658029">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db1b80511c.mp4?token=d9Su_Es5PerFfTm08krOkxceyqpF4u9Z29swmfrCBK3Slg2DAtNFq3Aiaa-Y41f3ppOQLkbjk1cwooS3KeKeo-boKSEN5L7o2Elz45JfzllMX4M-piJsxlld_5gP7hCLcbbecP51LLMQP7syC3BDmTwqT4NwZ5NgtO1N_HPyrutUVfOxTZWeflMXpIMGGHYF-eK6_iBmQdkHLqQEUj-Z1juZwlCo9poOEOxvh9DF3nO-P_9E0o5CP0tewPeS65ajUfMkkUEltDQUfFO9B5A6AwINo6-fW_f1sYGjP8fSU2-VxnYwQrqcSiL4l6NDOKX98H3SoGdGnca5opDI6zulkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db1b80511c.mp4?token=d9Su_Es5PerFfTm08krOkxceyqpF4u9Z29swmfrCBK3Slg2DAtNFq3Aiaa-Y41f3ppOQLkbjk1cwooS3KeKeo-boKSEN5L7o2Elz45JfzllMX4M-piJsxlld_5gP7hCLcbbecP51LLMQP7syC3BDmTwqT4NwZ5NgtO1N_HPyrutUVfOxTZWeflMXpIMGGHYF-eK6_iBmQdkHLqQEUj-Z1juZwlCo9poOEOxvh9DF3nO-P_9E0o5CP0tewPeS65ajUfMkkUEltDQUfFO9B5A6AwINo6-fW_f1sYGjP8fSU2-VxnYwQrqcSiL4l6NDOKX98H3SoGdGnca5opDI6zulkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی خضریان، عضو کمیسیون امنیت ملی مجلس: بررسی‌های جمهوری اسلامی مبنی بر همکاری اردن با متجاوزین به کشور ما، تنبیه اردن را در پی داشت/ این رویه شامل کشورهای هم‌دست خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/658029" target="_blank">📅 15:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658028">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
ترامپ باز هم پل‌ها و نیروگاه‌های ایران را تهدید کرد
🔹
دونالد ترامپ در مصاحبه با فاکس‌نیوز گفت که در آستانه صدور دستوری برای انجام حملات جدید به نیروگاه‌ها و پل‌ها در ایران است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/658028" target="_blank">📅 15:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658027">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/933efea1c1.mp4?token=eIl0xCx-k9_qNM0-wM-QaSkhDqjLrjvPGSuEK_kz6IMKG4DQ6yJ2pUBfwob650z2SqeuUsei8OY5Z4QFsxmH_OXRmD6x5UeQG9DQUchtc3nnXJfmT3Z-GqocB7K8A3lUR-Xeq9VNjkiUFOkPxqfGcOAK8HNSQHRB9t0y82IkHIv-AgWvuf58w2LEUre884IgKvSi6f6oCBizfZzAK7cR7MuZ4WE8IXpAHA9-k9V7kLxbHwG5XJV-f7MMt3Nx5LWzwwTxs-F0BMsrGl9u-TwadC4AmI976nzECX93H2-AFD7IFDTs6XW2CRYn6IQJeSeCorTzmMrILx3z5vWJrI9uZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/933efea1c1.mp4?token=eIl0xCx-k9_qNM0-wM-QaSkhDqjLrjvPGSuEK_kz6IMKG4DQ6yJ2pUBfwob650z2SqeuUsei8OY5Z4QFsxmH_OXRmD6x5UeQG9DQUchtc3nnXJfmT3Z-GqocB7K8A3lUR-Xeq9VNjkiUFOkPxqfGcOAK8HNSQHRB9t0y82IkHIv-AgWvuf58w2LEUre884IgKvSi6f6oCBizfZzAK7cR7MuZ4WE8IXpAHA9-k9V7kLxbHwG5XJV-f7MMt3Nx5LWzwwTxs-F0BMsrGl9u-TwadC4AmI976nzECX93H2-AFD7IFDTs6XW2CRYn6IQJeSeCorTzmMrILx3z5vWJrI9uZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله حزب‌الله به تجمع خودروها و نظامیان رژیم صهیونیستی با موشک منحصر به فرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/658027" target="_blank">📅 15:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658026">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بحران در بیمه تکمیلی؛ ۷۰ درصد پرداختی‌ها عقب افتاد!
فضل‌الله رنجبر، سخنگوی کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
بیمه‌هایی که توانسته‌اند تقریبا به روز شوند درصدشان خیلی کمتر است؛ حدود ۳۰ تا ۴۰ درصد، اما اکثریت نتوانسته‌اند به روز باشند. یکی از دلایل این موضوع همین شرایط تورمی و گرانی‌هایی است
🔹
اخیرا هم که مدیر بیمه مرکزی منصوب شده، خواهان این شده‌ایم که گزارش تکمیلی را بیمه مرکزی به ما بدهد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/658026" target="_blank">📅 15:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658025">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
رویترز: هیئتی قطری امروز راهی تهران شده است
🔹
خبرگزاری رویترز به‌نقل از منابع آگاه مدعی شده که «هیئت مذاکره‌کنندهٔ قطری صبح امروز پس‌از رایزنی با آمریکا، راهی تهران شده تا در زمینهٔ نهایی‌سازی یک توافق گفتگو کند».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/658025" target="_blank">📅 15:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658024">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6oXXDz-Xs_kHC2pdFLGcAck-MzNdIBSh7NvZQvutRc11wK1kM4_VVbDeDzJOT3afB0MHfWM1kxaANDklUs7e5wKm7IQpnsVEtUfjZW-b108S44Qm-EXti1ubXXkN7hgJafCn3fdndcsuDQB-gYNyYfKzy5JDeC9n8ONbA9CoP61Uq-dnV0Oae0mszmzVtJp41KpXqWm2fy2wyHvo3SEY_Y1_zQUmF8rPDIidKQz7z8wD--xzJuXJAEzlezTxB_ORMyxOG82GWwiIo0KUZeVbcrgrY1QJgfujeSLmzvX7iu_xppuf4NVFWpRIV0MpckAx6jxwlXHegTGmd1GuoA_Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط بالگرد ارتش پاکستان در کشمیر
🔹
ارتش پاکستان امروز اعلام کرد که درپی سقوط یک بالگرد نظامی در منطقه کشمیر (تحت کنترل دولت اسلام‌آباد) همه سرنشینان آن کشته شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/658024" target="_blank">📅 14:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658023">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36692261c5.mp4?token=gwonyYIqRlWXxzxosP0Nmy_4dYfu7p3WNIFrIPrm7n5EPLOzvZuloIuF5RsW_ylRkVgULTupLGhG1K5kvrpeYNUl6AMVziwsDhOgtxgkwozLJF8ukVuItFSRQjlu8itC1pR8HllQS7eU-xHV4ga0v8iHfxJqh7LmMfRXWC_wEZuZneQB296rD_eGyQva0sinYaOWfFTg6BQ6XNGT6sG6VBuifz5aD5cBHVF0moylw16YXTK-4mU9I5jRoYtrfWOh1uUF2wJAj7i50vcY6dP16f1xe3545vRSAP1k50kwN9rmw9NoN9VU0AzmkjS7a-hBqAXNekMvp3_kiuvvEa6Z6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36692261c5.mp4?token=gwonyYIqRlWXxzxosP0Nmy_4dYfu7p3WNIFrIPrm7n5EPLOzvZuloIuF5RsW_ylRkVgULTupLGhG1K5kvrpeYNUl6AMVziwsDhOgtxgkwozLJF8ukVuItFSRQjlu8itC1pR8HllQS7eU-xHV4ga0v8iHfxJqh7LmMfRXWC_wEZuZneQB296rD_eGyQva0sinYaOWfFTg6BQ6XNGT6sG6VBuifz5aD5cBHVF0moylw16YXTK-4mU9I5jRoYtrfWOh1uUF2wJAj7i50vcY6dP16f1xe3545vRSAP1k50kwN9rmw9NoN9VU0AzmkjS7a-hBqAXNekMvp3_kiuvvEa6Z6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پالایشگاه بزرگ روسیه هدف قرار گرفت
🔹
پالایشگاه نفت در استان سامارا پس از حملۀ پهپادی اوکراین دچار آتش‌سوزی شد. این پالایشگاه یکی از بزرگترین تأسیسات صنعت نفت در منطقه و بخشی از شرکت دولتی روس‌نفت است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/658023" target="_blank">📅 14:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658022">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
معاون امور زنان ریاست جمهوری: احتمالا صدور گواهینامه موتورسواری زنان از یکماه آینده آغاز می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/658022" target="_blank">📅 14:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658021">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEyVpnYsvWVCazsjZJ_jsLnggyPUj5zmDkTQDXQ5ZfJk39MJaOa80CoGMoKTCyTBp6V4JvD3QGVYROvLp5EnxNsR3dsVr3Q4FW3l4Wrl61yybs_vRIrjQiurvNOWTtlMF9l8IPm4X9BUnEA6Q_Q8y1kJGFKuW--HnmMUkku76GWo5sU3kX-1rK5p9ntcPsA73I8ynLV-8LxiuO8KBmuju5zeVrCHo8imuZaEauKv2eHIDVKtlsVSAjM_KYxWH52k3IjMVx4I6Hv5neC8-S3eM4AcTTv6Gd9hem7QJpkAh5P2AjDcH9EYLTF5AwrA8QK8k50XAPFh78WKELzrqs9dtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از کشف تجهیزات پشتیبان هدایت جنگنده‌های صهیونیستی در لواسان
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/658021" target="_blank">📅 14:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658020">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZK7g1uLf27oO9Ll4G9Zlbl3BxfRxJ82V1JoaMs1JpZWGUWXt3VvSMUYBCytsYBI3DV2K2WTakunjz8IEuWq0LuZEa4Ov8LBTPsuTVIT_tWjgPUNetOSOThMK5u4GEteLXnC0_Ec90_lr2V0xhOa4LbMTckm-MtWXFlQCk6A8pMuK0-QsefQbAmxYD3awGfuVFdkSsXu5NTCj9D9Qn5pUeoqhkvqLzIL9WOY0Jug63t22Cz4nuyDsOZ-iGtv1_Md0An8V1o7NVx2B5bku7vijPm8VDVpDBWNufZZKRQlKMoxAelWWdYqLMzSFK2nci03VCmFYnVTnmytiy34Sa0Agg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای جدید ترامپ درباره مذاکرات و توافق با ایران
رئیس‌جمهور آمریکا:
🔹
ارتش ایران کاملاً آشفته و بهم ریخته است. بخش زیادی از آن، مانند نیروی دریایی و هوایی آنها، دیگر حتی وجود ندارد - آنها کاملاً شکست خورده‌اند. ایران فقط حرف می‌زند و هیچ عملی انجام نمی‌دهد. آنها برای مذاکره در مورد توافقی که برایشان عالی بود، خیلی وقت صرف کردند، حالا باید هزینه آن را بپردازند!
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/658020" target="_blank">📅 14:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658019">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce354e84e.mp4?token=g_Hy6icmtfJgHzr1U07nVOzukNgibdpr6SKoaIlxpzij1otvnpfYw2kRlugnH9rnNdTtf6pH52j4JbLJksKE92CcACd0zCoIhKtTVJU91jGRrsvCt8MtbERZHaZrvAugddA7mG-IEQyiznVTtfv2ODHD070dDrMKNVn2LgTQ4UveIl0AercYGjqy_xM4T-4JwjjoS7rryq2Ol45JuMMipymyiy3h70zIxKUPbWNhy_4b3FivAAnXvwRVC0xcUE_Nm-Y6QIizuNy8pRsdAPnaEjTBuEh1YqWiQyyGdT0MCv3kZIeR2vwGnP1rAue1T2q3Yka-u7TPjskvnCkIB9Sy5oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce354e84e.mp4?token=g_Hy6icmtfJgHzr1U07nVOzukNgibdpr6SKoaIlxpzij1otvnpfYw2kRlugnH9rnNdTtf6pH52j4JbLJksKE92CcACd0zCoIhKtTVJU91jGRrsvCt8MtbERZHaZrvAugddA7mG-IEQyiznVTtfv2ODHD070dDrMKNVn2LgTQ4UveIl0AercYGjqy_xM4T-4JwjjoS7rryq2Ol45JuMMipymyiy3h70zIxKUPbWNhy_4b3FivAAnXvwRVC0xcUE_Nm-Y6QIizuNy8pRsdAPnaEjTBuEh1YqWiQyyGdT0MCv3kZIeR2vwGnP1rAue1T2q3Yka-u7TPjskvnCkIB9Sy5oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی خضریان، عضو کمیسیون امنیت ملی مجلس: اسرائیل اگر خط‌ قرمز ایران را در لبنان رعایت نکند مورد هدف قرار می‌گیرد/ حضور مردم در خیابان دلگرمی رزمندگان در میدان جنگ است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/658019" target="_blank">📅 14:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658018">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tqpm71swWzAmiql7MgEqm5o8mAlFRm2frYBSLBx3lrXPHgm-tQpWG8iBEzvIlN2Y30bjZ6ullDskZSUSZblbhoRfEe7ZfzP3DBaO3cos8VKleXSaN2eZLS9OYOoPS6UB-ylxg98AndhjwGmqq7F-O6UBIOAxDUvE1JzmEZtkIhjeT_kIoUgIiwFPtmb1oiQZFjjfsR-YIQDQ9UAIe6nkycCxbjiFMecVbwUCOcdmQt07hmUjLyvveGDMA4Y12F8ZCSIjwpD1qLhvlHd3PFZ_0DFIq2S96rW8MLapt2pEVqASUE1RZ3Hy1id1ov4fcouLgjrNJ50NnwS1lJCBI0GOVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸ کالای برتر تجارت جهانی
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/658018" target="_blank">📅 14:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658016">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
قالیباف: جمهوری اسلامی ایران به هرگونه تجاوز با قاطعیت و بدون درنگ پاسخ می‌دهد
رئیس مجلس:
🔹
با وجود شهادت فرماندهان و دانشمندان در جنگ ۱۲ روزه، نه حرکت علم و دانش در کشور متوقف شد و نه توان دفاعی و بازدارندگی ایران کاهش یافت.
🔹
فرماندهان شهید و دانشمندان کشور با سال‌ها مجاهدت و ایستادگی، نام خود را در حافظۀ تاریخی ملت ایران ماندگار کردند.
🔹
ملت ایران ثابت کرد که پیروزی نه در تجهیزات و امکانات، بلکه در میدان اراده‌ها رقم می‌خورد.
🔹
جنگ‌های تحمیلی اول، دوم و سوم به جهان نشان داد که مسیر فتح و پیروزی از دل ایستادگی و شهادت می‌گذرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/658016" target="_blank">📅 14:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658015">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c69e0ed52.mp4?token=NHd_fv1mZOYOyCm6rleGfcgFTv08iIHdn8JN1dxq5wuhRdYh9Zm60Wt6Q1wqB_IwHPyCVlpcPzv8K4Gy0Nl1UOVwr4FLhN1vx0I8gXfV6IlweVvr2b3JMxbkeoewyfUj0kWHuauRkDPE16OLBZUgYiXMbcZDGk4UWT2V3zDVo3QvJGdy6b5TGyoV-cXs7dcVrdEKJ2STmBOtb3WOgvh_u3iqGAsOTwyYRnSyw1xxVTUqQN04ecMsG6Cy_mBw3FE5FxpYIJjqho8TRKRk0ybj6lVruT32oHyguf1BvgZI54CZrmRsTIvU1cXPazL8nuPZBf348vi2N-4eLygsLQvHxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c69e0ed52.mp4?token=NHd_fv1mZOYOyCm6rleGfcgFTv08iIHdn8JN1dxq5wuhRdYh9Zm60Wt6Q1wqB_IwHPyCVlpcPzv8K4Gy0Nl1UOVwr4FLhN1vx0I8gXfV6IlweVvr2b3JMxbkeoewyfUj0kWHuauRkDPE16OLBZUgYiXMbcZDGk4UWT2V3zDVo3QvJGdy6b5TGyoV-cXs7dcVrdEKJ2STmBOtb3WOgvh_u3iqGAsOTwyYRnSyw1xxVTUqQN04ecMsG6Cy_mBw3FE5FxpYIJjqho8TRKRk0ybj6lVruT32oHyguf1BvgZI54CZrmRsTIvU1cXPazL8nuPZBf348vi2N-4eLygsLQvHxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مادر شهیده زهرا حداد عادل، همسر رهبر معظم انقلاب: داماد من قبل از اینکه به خواستگاری بیایند تافل‌شان را گرفته بودند، اهتمام زیادی به یادگیری زبان‌های خارجی داشتند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/658015" target="_blank">📅 14:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658014">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887a04c96d.mp4?token=uyjTxu1cNIhgsZOxgEh_7U2Q_sREID5sKWvu_uoRaGHC12KnuNRbJeEC75GuhAolSUYzaElMbRU-FoCgnI6KK-2-PMqA2X3-GRGXMtitm_Sdslz8pRu6GYtf9Q1LbxM81pTGW-Rfd-9YmHAbgeLHOKzYibPb3AGY2r2K-Wqd7NufdAHH2L0cVstqcBddR1xdW5cO5XwgW4ahpjZUSrB0gS0QRNQVNgW49lr9w8_foCtNZT5jZ_2Xq77v44cjowyzcknQ3IKgXxEwPAOtIgNGLmQzQZ0bVEkOmrdRS58F9WxyKz1Mguydl3DW044DxPhdUWofhs6fEETVSmcDvg9nXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887a04c96d.mp4?token=uyjTxu1cNIhgsZOxgEh_7U2Q_sREID5sKWvu_uoRaGHC12KnuNRbJeEC75GuhAolSUYzaElMbRU-FoCgnI6KK-2-PMqA2X3-GRGXMtitm_Sdslz8pRu6GYtf9Q1LbxM81pTGW-Rfd-9YmHAbgeLHOKzYibPb3AGY2r2K-Wqd7NufdAHH2L0cVstqcBddR1xdW5cO5XwgW4ahpjZUSrB0gS0QRNQVNgW49lr9w8_foCtNZT5jZ_2Xq77v44cjowyzcknQ3IKgXxEwPAOtIgNGLmQzQZ0bVEkOmrdRS58F9WxyKz1Mguydl3DW044DxPhdUWofhs6fEETVSmcDvg9nXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی خضریان، عضو کمیسیون امنیت ملی مجلس: مطلع هستیم اردن پایگاه و آسمان خود را در اختیار آمریکا قرار داده است و حملات به اردن پاسخی دفاعی بود/ تاکنون ۱۶ پایگاه آمریکایی در منطقه مورد هدف قرار گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/658014" target="_blank">📅 14:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658013">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0072a5f4.mp4?token=kuqyOkBsul6Y5ox8RnQHOKkap-cakLbp03cU1fuxzyVGmKzerAbRA7cx9C-ylX22JLxekzwbP3oBGGlXFTRG0OifphsiElVsLBoNTwISPZ04-T7nZwTm8maXCk_BcH4nSv1c4bkAPAJaCbTSaHcHKM89iRN1HuNNaqu-YQYVOtzzFD8mXA7UXU9jKWC3_UWCT5wT-KaJetuCr1d1QONsMG-32E9E7rd-yioVOLW7o9WIZu2VgJWTZjcOex8LFUsidSHkPBTq1HCzeWwUIw2lbEAjXySYxihBbKwDQzl6Ohf1OFUfAZ-7aXuWH8_sLBshQp8Bs_mVEd0TlxB7OJog0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0072a5f4.mp4?token=kuqyOkBsul6Y5ox8RnQHOKkap-cakLbp03cU1fuxzyVGmKzerAbRA7cx9C-ylX22JLxekzwbP3oBGGlXFTRG0OifphsiElVsLBoNTwISPZ04-T7nZwTm8maXCk_BcH4nSv1c4bkAPAJaCbTSaHcHKM89iRN1HuNNaqu-YQYVOtzzFD8mXA7UXU9jKWC3_UWCT5wT-KaJetuCr1d1QONsMG-32E9E7rd-yioVOLW7o9WIZu2VgJWTZjcOex8LFUsidSHkPBTq1HCzeWwUIw2lbEAjXySYxihBbKwDQzl6Ohf1OFUfAZ-7aXuWH8_sLBshQp8Bs_mVEd0TlxB7OJog0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیزر قسمت یازدهم از فصل چهارم
🔹
در این قسمت روایت قسمت اول از تجربه‌ نزدیک به مرگ آقای مسعود نبی چنانی که به دلیل بیماری کرونا به کما می‌رود و در آنجا اجازه ورود از تاریکی به نور را ندارد و در کنار روح مادر همسرش حقایق زیادی می‌بیند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: مسعود نبی چنانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/658013" target="_blank">📅 14:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658012">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c50a24bda.mp4?token=Cs9mlhMQcM_DKik88MDQBnhH35DUxtYexTJg1Fnlq1quMZ7BGy1jpbrzqwB8JMM2aDN4DYXkuj8QCb9XZ07LvnEiQBY5rN2QPvCQoSxX7T3DWfynFt9hhLyWJoHbhy5wMeNGoRuqZh5R-zsSVrUaXw2WtiMFcbg5NL77wGqEQIMCMbj4H5Mq6MFInsR2odfaoT8zCMWtCYISEZZQrYF-OcoE0_riuBHaHISlbh8J-mmLONA3zgc8C1wG-MthlY_2Zl4lN2uijUwocEJTi4wPKyAZFXN2tk_GkWq516Vw0eODY8TxXWTU8ZL_jWLHkeI2oTx4Rswp3boTH-NfGBE0r34s79LU0BQnd68W5DRprrtHnhvS5HOSl4wydRNwDDCIFnVBBZB8skUwKm08PD7fCG73My_xaDfr0oAxIVISiFwtfTthWbfLhHYA3AhO1NyVW56iuUoJM8bi5Jq_17pXOhAWa77CYrqv6p5a1sTx_VBS23_Bhn9AMXpNKSkr61OrpfkB7zY4w3CfquW36Fq_TOjusCuabD07qW4e9rQfI0-Xil2_KiNjsHJzuoR23ZO-yb2dFa1i4qjJJ8Ox0Ty04-4LFemFRjh3KVxiaVWC382g2XOb58Uk5zNxO1Na0egLW5WWvSYAsLahOd3tQ2jNxKjbbsq8KzNUkvZ1eBDl4MM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c50a24bda.mp4?token=Cs9mlhMQcM_DKik88MDQBnhH35DUxtYexTJg1Fnlq1quMZ7BGy1jpbrzqwB8JMM2aDN4DYXkuj8QCb9XZ07LvnEiQBY5rN2QPvCQoSxX7T3DWfynFt9hhLyWJoHbhy5wMeNGoRuqZh5R-zsSVrUaXw2WtiMFcbg5NL77wGqEQIMCMbj4H5Mq6MFInsR2odfaoT8zCMWtCYISEZZQrYF-OcoE0_riuBHaHISlbh8J-mmLONA3zgc8C1wG-MthlY_2Zl4lN2uijUwocEJTi4wPKyAZFXN2tk_GkWq516Vw0eODY8TxXWTU8ZL_jWLHkeI2oTx4Rswp3boTH-NfGBE0r34s79LU0BQnd68W5DRprrtHnhvS5HOSl4wydRNwDDCIFnVBBZB8skUwKm08PD7fCG73My_xaDfr0oAxIVISiFwtfTthWbfLhHYA3AhO1NyVW56iuUoJM8bi5Jq_17pXOhAWa77CYrqv6p5a1sTx_VBS23_Bhn9AMXpNKSkr61OrpfkB7zY4w3CfquW36Fq_TOjusCuabD07qW4e9rQfI0-Xil2_KiNjsHJzuoR23ZO-yb2dFa1i4qjJJ8Ox0Ty04-4LFemFRjh3KVxiaVWC382g2XOb58Uk5zNxO1Na0egLW5WWvSYAsLahOd3tQ2jNxKjbbsq8KzNUkvZ1eBDl4MM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرایی تبدیل ایران به قطب چهارم جهان از زبان اندیشمند آمریکایی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/658012" target="_blank">📅 14:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658011">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
شورش در مکزیک در آستانه افتتاحیه جام جهانی ۲٠۲۶
🔹
یک روز به بازی افتتاحیه جام جهانی ۲٠۲۶، معلمان معترض مکزیکی برای چهارمین‌ بار اعتصاب گسترده‌ای به خاطر کم بودن دستمزدشان به راه انداختند و این‌بار تا ورزشگاه میزبان افتتاحیه رفتند. اعتراضات تا جایی شدید بود که ارتش مکزیک مجبور شد وارد عمل شود و این ورزشگاه را از دست معترضان نجات داد!
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/658011" target="_blank">📅 14:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658010">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
️
انهدام یک پهپاد متخاصم در آسمان خوزستان
🔹
یک فروند پهپاد متخاصم توسط شبکهٔ یکپارچهٔ پدافندی ایران صبح امروز در محدودهٔ روستای چال بلوطک شهرستان اندیکای خوزستان منهدم شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/658010" target="_blank">📅 14:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658009">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f133308e2.mp4?token=GSA6EwGvKUeA6GTF5DJSRMYgTdQhhNZxVDRi66RiH0-bctc6q-FpTOIjkS3XWqVrmeFj3Njj2t3ez396l10vlm6rQsGDLq_sggbqwLQ8qM3c_CqwaB5UY0Gvz_nTPgSKX_BsdyHiXfhvOIMY9eU9n6kv6z8E_MUSm1fdNFJPKmvlVGoR27GbMZ-RXAJ2ZiaocCN8Zb0ruxFR5KObT2yJjT2kH4v1tGqWzW8LrtvBhZKTVhEm_KwZOFyhE4UhLkwQ5YiBF3pZqZOZiYteDXeR5mKa1wLebWBA8B0XATANxFTjI-daQrQMvG5Yxm6Qe4ptDPNPt74Fqcix-avyB-wSYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f133308e2.mp4?token=GSA6EwGvKUeA6GTF5DJSRMYgTdQhhNZxVDRi66RiH0-bctc6q-FpTOIjkS3XWqVrmeFj3Njj2t3ez396l10vlm6rQsGDLq_sggbqwLQ8qM3c_CqwaB5UY0Gvz_nTPgSKX_BsdyHiXfhvOIMY9eU9n6kv6z8E_MUSm1fdNFJPKmvlVGoR27GbMZ-RXAJ2ZiaocCN8Zb0ruxFR5KObT2yJjT2kH4v1tGqWzW8LrtvBhZKTVhEm_KwZOFyhE4UhLkwQ5YiBF3pZqZOZiYteDXeR5mKa1wLebWBA8B0XATANxFTjI-daQrQMvG5Yxm6Qe4ptDPNPt74Fqcix-avyB-wSYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران خانه همه ماست... #ایران_من
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/658009" target="_blank">📅 14:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658008">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24df01c49a.mp4?token=II1IhYoGLex6TjiqzbCbXjgyW5YNvh9JYEs2lRNJyhKgnI79ZJVkdPgfdIE4wUKW0Qu6TRQiNia5Nv757vl2yZ5VdK2KpvUTjMt6PchwIdygAaUEdOG58Xk8mYMSPNfB7hqPQa9K_kxu5OOjnQ3wIN22xfwtScejJ845OYAafT72kgrUMJVjb9oMnTRAMX7bEsmy06iGsatFvpQLH1lQvjof8Bo2J5pSC20yNO-RNiAnQO5in3zfCFFLrsQtYCzLjaukuQdktM9OFIpxg9bGHxjd1ll7vTEa4zPjBR-viOMTS6gq20n0-D1nhgYvhywbe9jf24fmmEAJtqPv3Ed5mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24df01c49a.mp4?token=II1IhYoGLex6TjiqzbCbXjgyW5YNvh9JYEs2lRNJyhKgnI79ZJVkdPgfdIE4wUKW0Qu6TRQiNia5Nv757vl2yZ5VdK2KpvUTjMt6PchwIdygAaUEdOG58Xk8mYMSPNfB7hqPQa9K_kxu5OOjnQ3wIN22xfwtScejJ845OYAafT72kgrUMJVjb9oMnTRAMX7bEsmy06iGsatFvpQLH1lQvjof8Bo2J5pSC20yNO-RNiAnQO5in3zfCFFLrsQtYCzLjaukuQdktM9OFIpxg9bGHxjd1ll7vTEa4zPjBR-viOMTS6gq20n0-D1nhgYvhywbe9jf24fmmEAJtqPv3Ed5mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویرانی گسترده صور لبنان در پی بمباران اسرائیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/658008" target="_blank">📅 13:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658007">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزارت راه: برنامه‌ای برای افزایش قیمت نهضت ملی مسکن نداریم.
🔹
اموال ۴۷ نفر از خائنین به وطن در خراسان شمالی توقیف شد.
🔹
اردوغان: ما هم در معرض تهدید هستیم/ حملات به سوریه و لبنان را تحمل نخواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/658007" target="_blank">📅 13:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657998">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FJxALYHF90TKyifi76d5ECvWyXIKTXD_aYuXTP2GpCABKlFYBgVgVRBJ6Fedbh4OAKrOFsEx43sJqB7Hgfe_bQZHaZJMj4lheqFS0xiCaIvNvPpqkwxqmEU4n6_hkwUNUEt-lGK7yttICznU1ZdwpRYZGJZMPOwrShSTNRrhludM3lUsKnbi2K8UsRSAbky3jwj3HPUWKhEEjslLR18hMD5DzK9d3y-Nys-t6KrjuZq9RjM5bz1avzj_vq3sHvZktVCTd8rJAn_XYxZCrXRiQt7Z-eF12JUG9PjgnMLkiJOwDYOumCAHge6Qi6cu2Jb5pxAdPIamIpVgnuCAlxlVnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UsUQeqmOOBMA3sCVaA0KpZeH8oSnF2EFPNJ9zrrOo0XU1e6tlUn02HoW_AVRjEe3IzbM0-wiOY5n4VaUkGNdxoh3rA6GGqtonB-1QTy3V7TTVg4RB2bHVri6cyZPftA3qvDp3M3sNV_Txvur8mSQJh5wohK4LsdXJIGsfnc3jXOCIfdMNJ9Ql4MTH1m8wuyLJa4QhcUhJ3iozm7C1dJe0Pkk6EqZzbJV5-Nc1lfnmgZZb4a0LtVYEt4m6yhS8p7crQ43zBSOrP4S3Wmn3BCWDOlAKVYVublPjsvkJpY_4MrJ18ycGoSly5TvdHi9GKq6Mh56k4FMwblH9T6-cNCKRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KQOWidPAB6pdv8WuBTF_gESTyJZbaxhj5crFsLN8njpUuQaKhc1sj5PR3Gt5BxyKrwJL9kssJuoSJg3lnOJnmzYNPkuXfkj5-OHpq-yQVcqJbN6r_WOGk4tewyPZodKHScCXgDM9LG9gJEmtm40mL4tOgvUYZRXRSVyvNcb4Fk8zEnyLuvXy9yxocI6ADsZiFS3UqYpBadnmaxuNt5-SZelV2n6bBkbEdbErE6GMs38Wy3nOl0yyzNWooV4tDOsdSjtgU9xAbZI_L_4nZBOQVeUumaTIHs_GRuJqFNu0CH_xCREJBnZIfsDewtjxMRRtG_Wrb_LyEdJmJvqgEsSd7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UdmAJUP9aaiNn5niTdNbvUVooHCxf7dibAZzfq9UFartUuW-JEsCNYNVkFbkWttD5HP-MSw_pKRnNN_JgGT8gbEFcG3Y9x3fnjJ3bLdpOEasOCWId69p48LoS9GV2FKeQEzdJffsq-GChH4Cd38djr87dyRJOYnQFRoG1CWMzyfVV_q9Wssei9G9Kwl5m9hqUkCV9JKbbkn6-jKbJiGPPL7b4RR0OTdyqEG6Vo1A2wvJJ1HWVWUR1Tpt2fFE-OEY0wrQAJKoF0BtizzlveBc_s_UMQ4u4p6tqPjSuYOl4taZB_UMZDuABOoO9Pipzmub6EXoaA9Kd9WyM2nkgJubJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t-ksnoirdPvlHquxfYN1WQ07UeH6958sCcUByWd_45Rf3J9OXyH7lpmVv-egQHiJtGbnxdxUpr0hWT8zYUds7r2ylDgfTpGlCHXq8Qyt5t4yIbpXopUFVOLlnXPYZlRHVCmHIMzcgFv0Lx9qa1Zs6Hjo5AyJTOLEjUtjQ8Ce0cgn3u0wtEez2JwIewb63BYHZ0J2evOcDIkKoPDD0O2KyfdryNsXzebVc647UH9yO5PxBSJuziG_whhZftG3AqogU0dhe0MwgqX1_a-yTmJXBSlNv2cJ-ilEuALwnwQImOBwgxHT4VOlGQwiMZSx8lfo-DIMPoc5ANT_IFgEFrBEjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-pTuMRvVFhkyunygK0IDqyFlwQJGWm34gW2TGuzII3Bkv1H2rkLSgZVyML_lgycm4IYoO3iFVLQpUhyY03ek7glGz2VBU7wGDydnHoirSdmf88PByHBk6p95ilGyVuwtVtc-2t-MoGpViuvc8KNs-xGijskyROsxrQmlQpp-_o_gW4kP4BFgOk9tIb8jDtsBJVBd1WollN5JtgrzdxbfrXU9aiI4u6CTa9MMr6L2dydet6tuL8vVlSxvN-Wb_mw06_B_pxhxu_mEUwYX5qHqakfJSyPAiGaIgfVODPRgjGuNAsDhZH-UYr8MlUta1wQN1va4C42lMAvSlqQSiYIIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f_882jEr5kJxwVHzWc3b6jkcni8H9dwmfsRRGwsL3QV3BpwbwtlajoZnXvI8tMue3G9pJzIvWk075PLUBjQywmBc1tySChcqK3gLJZTnigQFJbVSyu2keR9eqJXEFVjDW3A2ZzXpA7EhLyk5Kt0fZvLUK0zKWb3hcpTDRszLokeJeHkhxmwMQGtqNEhP_PyzbsuoPcIvpBQK9rbniKjjKDIHbwrVNA7dLT8Hn6jLS93Z6VFDCH6S6E5pj2TVXBfOG80c1ltvMyArIoXiZW8u7hYW3kMBYKC-NlT5A6816ypUBwo4Y7ov63MIWSa8eIJrms8Kf2tkAqqSomrOalfCSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kAx5MGgTRbJLyES-BD28x1V3OfkEwR1sWPdRa31agstED5uCMY3MY-jXgEBfs9Z4GjVhY8KnQ8sFLJe8ag53KpHQ_MqL_fVTPzD2Ffa1_joqk5hCVimPLf5Mz6_vTB-7IuxyVeE78ypAZeatk3OFGlQ_tVRaHuMvo6UBRb3e1cFCCDuIZkGB-_ulrvsh8PYvu0ETk8cXZnN614Ktt1J7-GjvlyTZPdVoowMIq7mqGUUfzxcvyjecAPX1zqYQXF0j4pgMl4EbMFDKbyzLDKH5RvzfaNdePlq-HrGJzeROxIv4fECVe8Tz9PVKloYIAbugEgRNQ-QOOaxS__JH4UkGNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۸ استایل پر طرفدار پیتزا در جهان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/657998" target="_blank">📅 13:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657997">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54533a804c.mp4?token=otNeQ1_WSfkalSTS0lTVVwiC7I8Ggy7s8feuZHfcBjcrvoHhHpJ9yuZS8bc4jF0ro82E3CC72Ra7g3ai7EkYV0xQ40lFuNz_VBWpa9s3ljDn-02u9kZ5qIkQqM6QGFg0Q8c7scr2WejZzobgDNmY-z6PxJ4z1dBzQa-g4oS7vAcbcqiisXQl8l2VxOrTMqJI7Jkk5kYwmwBmcLsdwJ4vXfn1h5pGCyqvZUfpZPuF3r1HYh9E2qt8B2Z7l9HlIzzFkYmHGZzLtzDgi-KzdYvX_oaS3kWRZV3QUJRd2cWDtgyYl3a8xPELpL70sgTJ7d3WRs2udOuh3wE5P33YW6mS8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54533a804c.mp4?token=otNeQ1_WSfkalSTS0lTVVwiC7I8Ggy7s8feuZHfcBjcrvoHhHpJ9yuZS8bc4jF0ro82E3CC72Ra7g3ai7EkYV0xQ40lFuNz_VBWpa9s3ljDn-02u9kZ5qIkQqM6QGFg0Q8c7scr2WejZzobgDNmY-z6PxJ4z1dBzQa-g4oS7vAcbcqiisXQl8l2VxOrTMqJI7Jkk5kYwmwBmcLsdwJ4vXfn1h5pGCyqvZUfpZPuF3r1HYh9E2qt8B2Z7l9HlIzzFkYmHGZzLtzDgi-KzdYvX_oaS3kWRZV3QUJRd2cWDtgyYl3a8xPELpL70sgTJ7d3WRs2udOuh3wE5P33YW6mS8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: باید از حالت نه جنگ و نه صلح خارج شویم   رئیس جمهور:
🔹
دشمن خواب این را ببیند که ملت ایران تسلیم شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/657997" target="_blank">📅 13:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657996">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-Jv4BFXnUI0T_PnwDS1vCyLn8GUWWhtw31DV7CZ2cq1Wl4T1_Fsb-HIPJvVmiG4LcaARSryBWelxe1DCLgOd7JgSu9NVFK7wTzQQh9qDiAr13EJc8HE0ZhKWE1kspnmQPzYgqqNmG6L4CuP6jmXhO_6t3jV-E5CAyFI4cv5-xw12ZvD_liJrEOamJVUc-sFCBXQwNHNnTYRWTpZuYFQT1w05faWavNp_O5oHs32Br8bynKZTaqOIWNWCicHrdRausedn1KrRAhBs3eT1udLcwABFcay-0U6KDp2BPp5y9RqCBDUF64cM_cUFHM0IaafM0WG8zwaK4cIGGUUa-80wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر کشور حاضر تو جام جهانی، چندتا بازیکن داره که متولد همون کشور نیستند؟
🔹
ایران: دنیس درگاهی، سامان قدوس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/657996" target="_blank">📅 13:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657995">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085a6fb159.mp4?token=sUMCPLyt3J29H0hrOsbCf0MEtYv6VftQ2pDpVAGKXpg3KvxfZC_NACtownHSVQNkucCaPeYeW4nzne5RNjXP0CvupTFaTMlvlMsh0Xp6eZultb7iaM7_FhmS_2z91a6s7yUaKF8wa1zKdufsRaSB5QkX0srcLRs2EO_JgrVSlzrOk3xE_C5Jgaw-jX-RiL-x5MDOTKUBNOlcX9wFkVO2SVWNrPeKTx6OTJjVaCvJs_fFGOI3RJ4yfiblWfxcTVcS7PJcqOVXeiV06Scbk1cTpmXkED6AX7FKAfimzkgTuyeAqVFfE0MOinQmg6J9wPZFpBIIvXGv64vomktVqZrwHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085a6fb159.mp4?token=sUMCPLyt3J29H0hrOsbCf0MEtYv6VftQ2pDpVAGKXpg3KvxfZC_NACtownHSVQNkucCaPeYeW4nzne5RNjXP0CvupTFaTMlvlMsh0Xp6eZultb7iaM7_FhmS_2z91a6s7yUaKF8wa1zKdufsRaSB5QkX0srcLRs2EO_JgrVSlzrOk3xE_C5Jgaw-jX-RiL-x5MDOTKUBNOlcX9wFkVO2SVWNrPeKTx6OTJjVaCvJs_fFGOI3RJ4yfiblWfxcTVcS7PJcqOVXeiV06Scbk1cTpmXkED6AX7FKAfimzkgTuyeAqVFfE0MOinQmg6J9wPZFpBIIvXGv64vomktVqZrwHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بمباران نبطیه توسط جنگنده‌های صهیونیستی
🔹
جنگنده‌های صهیونیستی شهرک حومین الفوقا در شهرستان النبطیه در جنوب لبنان را بمباران کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/657995" target="_blank">📅 13:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657994">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eX-klUvTpBkJehst6P0cTirVLj6uxjHlCtNjO2vCAYUI9pQcGHI161cd-eveBXsFZZ6Ko6FStOUJEsjuTY36eFDYxVm6QGR9MR_wgDDbol0Hfcz28tUKNICmyRTRkiSnhh5wQarpNos950rFprYeYXYQh70LT5gj_CPBuV13DTTfRaGayDl391uMZ-y20W__ip-ws-AY-tNNsEDFQ4vxw8nSdJS1oUeLLKpSg6IRfYZPvnNj2CTqFCbW-WtMY4S0Ccaf5elnJlQpNeTeo05TYzNKFPhWkIpCMKpOY4_HLsvNixjY57Fo7iR7GJUNm52nuI9xDbcG_-9ZRc5GwAvarg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویش امید در زیست بوم ایران
🔹
هلیا، گونه ارزشمند و در معرض انقراض ایران صاحب پنج توله شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/657994" target="_blank">📅 13:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657993">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNqkxg3o5Yatx1YBx9KIfdtWoAF2pipraRaO1_NU4Cnqv5RBqLjVVvuIe9mBYOM9jnUXkQUsh-H2GSt5kklJcPPvtOi5y9l1S2aGvpCwVfUX9Ej11P6cfGtKq9rPFrBAVVz2YWsfGoYy0J-mU3Q_IaaN2w_Q81RlAvwhb-51GJS-Q0XoGClnkv4FOxnWaeD79iOwKSGkZRTMtETtM9BtzIFI0T0hQ1dizOKyBrvch_m58dGTVJYp0vYeKePHxI4iG8w4nDTTmqfAH2t1d69-zT2791GpFSnmLBBPUrY_y04CzAUmnhlrNbAcXoeuJbTBuGF9Lhv3YYKCL6D6jFfYYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خسارت ۱۵۰ میلیارد تومانی حملات دشمن آمریکایی به تأسیسات آب‌رسانی سیریک  مدیرعامل آب‌وفاضلاب هرمزگان:
🔹
در پی حملات آمریکا، زیرساخت‌های توزیع آب شرب شهر کوهستک و ۱۰ روستای بخش بمانی تخریب شده است.
🔹
این خسارت که بالغ بر ۱۴۰ تا ۱۵۰ میلیارد تومان برآورد شده،…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/657993" target="_blank">📅 13:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657992">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
گزارش حادثه دریایی در نزدیکی سواحل عمان  سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
🔹
گزارشی از یک حادثه در فاصله ۲۰ مایل دریایی شمال‌شرق صحار در عمان دریافت کرده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/657992" target="_blank">📅 13:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657991">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72050b3b4.mp4?token=NfTIqmpeOTHoivZ4ZwWwS_kuMrxWLih26q7OyoGvzd8KXRKRxe1qf8m6y_gDoeV55FYWlepFxJoAZ8K_37hPhXUAJGT0UbDSJzyrL59EN4biLD0bmOVsIsuyi2V1qVL3fxrIXgd8I3r8GvNcUe0vB8sFGhbs7YxxVLKZEQZXvG3NvX-iI_uEzQDtIMxxzXmdmUUs1DWX5irD_Z4EtO2fc4Z5NYkY3EoBc0VU30leWxQr2CpRBiWwqxLzNweBbvNZpTp_6mmnkCvjT26gvDwLEW9tpSxUxbflBaS1JeFoVsg0jD_XRt5GzkXknjmGQIOBcrv9XVns4WgfdvWzHJW_Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72050b3b4.mp4?token=NfTIqmpeOTHoivZ4ZwWwS_kuMrxWLih26q7OyoGvzd8KXRKRxe1qf8m6y_gDoeV55FYWlepFxJoAZ8K_37hPhXUAJGT0UbDSJzyrL59EN4biLD0bmOVsIsuyi2V1qVL3fxrIXgd8I3r8GvNcUe0vB8sFGhbs7YxxVLKZEQZXvG3NvX-iI_uEzQDtIMxxzXmdmUUs1DWX5irD_Z4EtO2fc4Z5NYkY3EoBc0VU30leWxQr2CpRBiWwqxLzNweBbvNZpTp_6mmnkCvjT26gvDwLEW9tpSxUxbflBaS1JeFoVsg0jD_XRt5GzkXknjmGQIOBcrv9XVns4WgfdvWzHJW_Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زندگی میان شالیزارها و جنگل‌های همیشه سبز مازندران
🇮🇷
#ایران_زیبا
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/657991" target="_blank">📅 13:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657990">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKEbH76u0OnaM27zC-a5uk_t8zoWrTgNgF-Hgz4AOTjarfTl5P7IO82EKlHBZrJTodWPRzBfr3jZzJRt6dFiLSg1nbe49y5j9yIIrVsqGSMKey6wqNVmPnOhmwOBazNwlpMJ5yn7lW0kw2e2_RPn3r7qZJxf3Fj9p6IH23FBQaoOl5SrCQQXwKaDcTdEgArL_uvJZHXIoMx_eL8l-f3LUWu6SI4voyjCNmxpYVZk782VWNOGqHNlgKlubvzoE9KC-_i8OFTXhWK_XnK5xlWN2zrLT0zBPvelvZu6bXE9VjXHfVH3eVZEvOhg9VrV2JTjoETf8Q4BRaSx9G32_Jm4og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش حادثه دریایی در نزدیکی سواحل عمان
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
🔹
گزارشی از یک حادثه در فاصله ۲۰ مایل دریایی شمال‌شرق صحار در عمان دریافت کرده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/657990" target="_blank">📅 13:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657989">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
آلبانی علیه داماد ترامپ؛ معترضین البانیایی: پروژه لوکس کوشنر را متوقف کنید
🔹
در ادامه اعتراضات مردمی در آلبانی علیه «جارد کوشنر» داماد ترامپ که در حال ساخت استراحتگاه مجلل در خاک این کشور اروپایی است، مردم دست به تظاهرات زدند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/657989" target="_blank">📅 13:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657988">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
منابع از وقوع آتش‌سوزی‌های گسترده در مرکز اربیل و شنیده شدن صدای انفجارهایی در نزدیکی پایگاه آمریکا در اربیل خبر می‌دهند
/ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/657988" target="_blank">📅 13:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657984">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bba0f34ba3.mp4?token=Q7XWbMpKrvLYWxgtbEJTGM8vLo0vz7j_jW8WXwjZkr8Fmpm0wdI6HP154otsPBjNHTIBQP15L5PpbJ7U-5-EQ-iZ_nQkpoOR5y21CwRUzyl6VCM_loRoucXhZQmLEzNR2Igi_L-tI9xFJpNyPxYOTpV4ST2wPvkGoOzYKMz76i7zdM__-JbPL_YqX6DCqj5OXszrQgpuY50-6gHijdvKSAaMqgDCppwkeRZanJBsz-_i_henZEGT4tuX9SiwXyoSw810j2_RQd1prAqLsoPfVLbqF5c8b06xjGWNZ94JSZjO36WEWi_PQ0sOSRxUsWYY9yqNsijhuYzEQg2kw41LSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bba0f34ba3.mp4?token=Q7XWbMpKrvLYWxgtbEJTGM8vLo0vz7j_jW8WXwjZkr8Fmpm0wdI6HP154otsPBjNHTIBQP15L5PpbJ7U-5-EQ-iZ_nQkpoOR5y21CwRUzyl6VCM_loRoucXhZQmLEzNR2Igi_L-tI9xFJpNyPxYOTpV4ST2wPvkGoOzYKMz76i7zdM__-JbPL_YqX6DCqj5OXszrQgpuY50-6gHijdvKSAaMqgDCppwkeRZanJBsz-_i_henZEGT4tuX9SiwXyoSw810j2_RQd1prAqLsoPfVLbqF5c8b06xjGWNZ94JSZjO36WEWi_PQ0sOSRxUsWYY9yqNsijhuYzEQg2kw41LSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراضات ضدمهاجرتی در بلفاست به خشونت کشیده شد
🔹
پس از انتشار تصاویر حمله یک پناهجوی سودانی با چاقو، اعتراضات ضدمهاجرتی در بلفاست ایرلند شمالی شدت گرفت؛ در جریان تجمع صدها معترض، یک اتوبوس، چند خودرو و یک ساختمان به آتش کشیده شد و ساکنان آن تخلیه شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/657984" target="_blank">📅 13:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657983">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVEbMHiGFLBdez6bSv-tekHLR3H8bVnu2-MVeQTfMStyDRjFYBrbVnWOg-p9Okg52otz1Vw8pivZJHy4iYN0QLvUbiSNTCTgDnvHKyj5y-E0BWjJVk8iLsAILf-R6U2O9jTHLemAW9hX-2JoEvKcWrp7vKSCbac0ka9KpkZ1LLZy8z0ZRbjPOToQEyHW6pnhQqmjjqTX-j40abDhFUsLr1jpI6Vi9RcNh4Zos_kAAl-iogAk1zbleSv7ipuEVAtGdDsFN3wCPfEUQj9Ai-OsZ0BYcU9NLbNMaA_AWy86ms97sjnTzSue-1jMj4FHOVSw59sU2L7dV1An3NtMvGSgmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمسخر ترامپ توسط کاربر آمریکایی: چرا ایران هنوز هلیکوپترهای ما را ساقط می‌کند؟؟ آیا آنها نمی‌دانند که ارتششان نابود شده است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/657983" target="_blank">📅 13:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657979">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6CDO8ivUjkg8HunBEx6dx1SUPBhlZQyihNJmeGGBkKdiNkrnh7Em9EGDzwwSXXntd-nvstLYfPOps_5fwqJWMrzg9coYLge4wgzKWHMFWGMTUEZvELiDTIDj5WR4gMSV9MRAyJ7ra2yQOotdbeB_4uAEd4pu_k7tD5eOvQUYEG0OJOPZrkfwsyuWHp-5XP6OjYDvQcNtndP4e4b9vdaEjtnaaGyc2t_RWVzzXhx4ZpJ8DDwoUP3mG-JnWkXSreORKCCnUuMlQYRXlkEk1Gr85xGSNUnGis0OEa7Wj-RstcUUfS0pw32xbvdhXYa4Hoyz3lLFDJRsYdWIArV_avVYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q8xakLz0aqCkHnqyfvi41IFwvk7g5xXGlQWqq5oltiRa5PQ-KetqgSVWxmmlgcueEIO0HEgZ2zhRn236iR4LIsqyPUL8rOY6DF8O8KUmJRTH6qdDMH7vWuIkuZVlGHsFlUlFmXb5fkT17Ot8Pt4gAiLk6wAwKRQI75bosR5R-jc_mKMiqfXFt0cBDfclKw_QMNUPUfoA2mTs3oZFOLVTQNJqVibacaO7Lgwv63JlMwOsafiU-qWh2Mg4Lunqqk5437LRn328jEZEzKdTGBXwEfVgnsBCtuIC-bVCuM9Tm5vFXszI9kZPgalkNj_lM7jrwiNjray4_4EXsLqHPLlFxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OCvAoV8cMrQQmi9MMT6etaWf07a87pF3D_dXff6H93g10eI6rCXq6pYcMLhf6jClmYCGRN3IAd8-dWsFrzxbgMME81173KzrCWNgoZyl06tebcGc4VZl3CCmF1V1_L8hE715okBw0h2FiMO801i1udfxI6PLpMT6QcPnpZKtiF4iD2hS9v1xB7wqjGoNdOmwiBr2cGFzcbIVzMYcGltfXI8Xjm8hqYZ-9SgLDnJWaDf1B8VSp7RKxHXeVQHJmREZoLmyZIFAAr0XlEEvFFwY9glgVPnNgzDZ5oydkpq26fC20-nMYQh-iWd0XdtQCz9fRWD0KFrO1Ce_C4b0e3ITjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lIYE1UtIHRYAORdts9vT0axkTpdc0yVjVEZtrfDYpSjH5NwlV2dW2XsfWB3L_uqXgk11Obd04Jd2xaFI3MZVm4TlOMbWt5RQcHYZckfUnZ_ZZ6Fi2-Q3wkSqWDuQaZq96-jeAfrfmfkHOE_J6A-u8BOcdKwF5XhRUDwMOrfvniruphd99_ViCWhNylR8ejhqvW2MF2rawvynZuLXjaTYTEYJcdNB88Qu2-KlitkS2RY_yPmToYc9UPhlStcPRr11eXFpGhUUbmbZ5ND9mqw8AxVy6ICcJ-FJxtS2SBjzlTpD8Sw-EJn0QTY_yNCWNvUreBtQAJxI0d9-arPFgJU-DA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نرخ‌ جدید بلیت‌ اتوبوس در مسیرهای مختلف اعلام شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/657979" target="_blank">📅 12:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657978">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
هر فرش ایرانی، هزاران گره و صدها ساعت تلاش را در دل خود جای داده است؛ اما چیزی که آن را ماندگار می‌کند فقط نقش و رنگ نیست، بلکه داستان‌ها، فرهنگ و هویتی است که نسل به نسل منتقل شده‌اند
.
🔹
شما کدام فرش ایرانی را بیشتر می‌پسندید؛ تبریز، ترکمن یا اصفهان؟
روز ملی فرش ایران گرامی باد
🇮🇷
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/657978" target="_blank">📅 12:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657977">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
روایت پزشکیان از دیدار با مقام معظم رهبری پس از حمله دشمن به جلسه شعام
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/657977" target="_blank">📅 12:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657976">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8fe3c6691.mp4?token=JCLMMUgzAey9rshHCCg8ANFSOa5Po9LZeyWtEvUBQf0Ed7BV8VYYSdr1nMUaz1AHlKgR4ClXUUUSbHncCpvGtPRzGBjxNmoPTa_rtPhl_ZHLDpxx2dt6Neo_VH9j6PCFTzJRGsZvBSs6tXknkNvvfnmy912NCm4aNP8YQ6JCbx_spK_BJJDJAedMSHvifFf1fPQRxMr1-P5_CD0KGgdjwapFsb0r0WZSXjLQDb7l2vWn6Mh8DNsoQqyeodzP6iqQ0Tj5JUe5JIH6yU7nfBNzCERdEe1DrHOmo5XMU-gDwxP6j07oNysKb4zuTffN7kzhXOK2Wj-FXX4PN3jzDLS8sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8fe3c6691.mp4?token=JCLMMUgzAey9rshHCCg8ANFSOa5Po9LZeyWtEvUBQf0Ed7BV8VYYSdr1nMUaz1AHlKgR4ClXUUUSbHncCpvGtPRzGBjxNmoPTa_rtPhl_ZHLDpxx2dt6Neo_VH9j6PCFTzJRGsZvBSs6tXknkNvvfnmy912NCm4aNP8YQ6JCbx_spK_BJJDJAedMSHvifFf1fPQRxMr1-P5_CD0KGgdjwapFsb0r0WZSXjLQDb7l2vWn6Mh8DNsoQqyeodzP6iqQ0Tj5JUe5JIH6yU7nfBNzCERdEe1DrHOmo5XMU-gDwxP6j07oNysKb4zuTffN7kzhXOK2Wj-FXX4PN3jzDLS8sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت پزشکیان از دیدار با مقام معظم رهبری پس از حمله دشمن به جلسه شعام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/657976" target="_blank">📅 12:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657975">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpF1K8rWchvbLXEyhnrzXuOJHIEgDL0jsfhSN7JyuhjoO3xe2wxDpGmBjdDiq0a86NsRca49eQWRcTXRVDoWLtc_FCkYlArYigO7uoH7vhu5XYwd-U8ZtQ51iONxR3iqaS9JSaSZYWCoWzCq0NtWswnzI786KaTVQHG1FA4OKXUpjLtM6ZgpKlp99l_B0E_nx-36c2fxGPmykKzrylLRGym-P0CE2C7mjXjqZHPxk8krq5pydNv4OPLkcjnuHm8N7KFvOfkMCAOTfTAAgzHibd4V4JfEE-vh1yN5MekyKPLUlNQnOL06Ov69BG_HiUrwFQTZqAlUABUP0uAtoTYlLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد ۵۲ هزار واحدی شاخص بورس
🔹
شاخص کل بورس با رشد ۵۲ هزار واحدی در پایان معاملات امروز به ۴ میلیون و ۵۹۳ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/657975" target="_blank">📅 12:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657974">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a9b3aa89.mp4?token=UtgZjQnLbZqWE4BXOLFQ9OmDLz8xYnSinfG7VGeAggQLH9nvxSwLImc81doEXpB5xemV06zoqCaX8_sSj7odXhuCnXkvAB0k_MR3du2KhJjjgwh_s79exr4kQDhcJ_WLqhjLgU3acDcwP4aVkFyGVHDmzPZRh1TIG3UGJHoXwlcNWbjjEcY-ME5N0tSkqVY1y1iMj3cqcWQe-ekq8WnX00bdbQFg89P-hl5N9Lda8uuvcyEKLFX6o93cOkmM6svnC1cnz2dCmL3zqfY2KVifot4TbaSa7CxO4sWgTiHc8vOzJrvmRWuEMI6Vi0oTE85Tz-rFuHPEoMsKT29g63JlVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a9b3aa89.mp4?token=UtgZjQnLbZqWE4BXOLFQ9OmDLz8xYnSinfG7VGeAggQLH9nvxSwLImc81doEXpB5xemV06zoqCaX8_sSj7odXhuCnXkvAB0k_MR3du2KhJjjgwh_s79exr4kQDhcJ_WLqhjLgU3acDcwP4aVkFyGVHDmzPZRh1TIG3UGJHoXwlcNWbjjEcY-ME5N0tSkqVY1y1iMj3cqcWQe-ekq8WnX00bdbQFg89P-hl5N9Lda8uuvcyEKLFX6o93cOkmM6svnC1cnz2dCmL3zqfY2KVifot4TbaSa7CxO4sWgTiHc8vOzJrvmRWuEMI6Vi0oTE85Tz-rFuHPEoMsKT29g63JlVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمی از تمرینات آماده‌سازی تیم ملی ساحل عاج برای جام‌ جهانی با قرائت قرآن و دعا
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/657974" target="_blank">📅 12:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657973">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
بقائی: (جهان)اگر می‌خواهد ایران را بفهمند، بروند زبان فارسی را یاد بگیرند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/657973" target="_blank">📅 12:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657972">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
انفجار در قشم تکذیب شد
فرماندار شهرستان قشم:
🔹
انفجاری در قشم رخ نداده است و صدای انفجار شنیده شده مربوط به قشم نیست.
🔹
ساعتی پیش صدای انفجار از سمت دریا در قشم شنیده شده است اما هنوز هیچ منبع رسمی منشاء و مکان انفجار را تائید نکرده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/657972" target="_blank">📅 12:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657970">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
انتصاب اعضای جدید هیئت مدیره مرکز خدمات حوزه‌های علمیه با حکم رهبر انقلاب
🔹
بر این اساس، حجج اسلام والمسلمین حسین رحیمیان، محمد جعفری گیلانی، محی‌الدین مکارم شیرازی، قدمعلی اسحاقیان، محمدمهدی حقانی و محمدحسین احسانی، به همراه نماینده مرکز مدیریت حوزه علمیه قم، نماینده حوزه علمیه خراسان و رئیس جامعة المصطفی العالمیه، به‌عنوان اعضای جدید هیئت مدیره مرکز خدمات حوزه‌های علمیه منصوب شدند.
🔹
جلسه تودیع و معارفه اعضای جدید هیئت مدیره مرکز خدمات حوزه‌های علمیه در روزهای ابتدایی خردادماه جاری با حضور حجت‌الاسلام والمسلمین محمدیان معاون ارتباطات حوزوی دفتر مقام معظم رهبری، دکتر ایروانی معاون نظارت و حسابرسی دفتر مقام معظم رهبری، اعضای سابق و اعضای جدید هیئت مدیره مرکز خدمات حوزه علمیه برگزار شد.
🔹
در این جلسه ضمن تشکر از اعضای سابق و رئیس مرکز، براساس نتیجه رأی‌گیری از اعضای جدید، حجت‌الاسلام والمسلمین حسین رحیمیان مجدداً به عنوان رئیس هیئت مدیره مرکز خدمات حوزه‌های علمیه انتخاب شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/657970" target="_blank">📅 12:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657969">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaY1Zs0BlqxDyaGYAzFQfHoRsZxmjcBPRiDDV08JMaiqycRbVYE6LhjvtDb9RQadwy_ZZWfkNcOhAd3TcTA1nAE6u1k1xfTFslD7HrRIvWgGow5EiSKYTjVLK2UHCQMhcx6Nlsip5MDQaFkQji-7_zYBeNJ7RM5647PIEpscBIWSj9iZ5cG6Dk_H9jJX518NjHpo7rVd1a9ngOFoQ7eEZgkYJeUD5rIoFKj38EJbV3wOkuP4EORC40sBCYM1nRyHcA3h6I1iHETP1dwtmRbobS96x1bUkcI0OlxnpNhKVA4gRA5MG1sZc39Lb9GOhpC_FyjHW3e3cKHhUzEhzjc2fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخاطبان عزیز خبرفوری، «مسکن مهربانی» فرصتی است برای روایت تجربه‌های شما از انصاف، همراهی و مهربانی در بازار مسکن
🔹
اگر صاحبخانه‌ای منصف را می‌شناسید، او را به ما معرفی کنید. همچنین اگر خودتان صاحبخانه‌ای هستید که با وجود افزایش قیمت‌ها، رهن و اجاره را به شکل منصفانه تعیین کرده‌اید و تلاش کرده‌اید شرایط مستأجران را درک کنید، از شما دعوت می‌کنیم تجربه خود را با ما به اشتراک بگذارید.
🔸
فایل صوتی ۱۵ ثانیه‌ای ارسال کنید و در آن نام خود، شهر محل سکونت و تجربه‌تان را معرفی کنید.
روایت‌های خود را با الوفوری به اشتراک بگذارید
👇
#مسکن_مهربانی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/657969" target="_blank">📅 11:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657967">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1yaILG44YlgeNPAfxEEx5kMzs6xrBiH14-rfiUkdpjf9xTRy1BuzTMFCruM-2NpP9s64gOEIDxLN1X2vJh2-i2zbvlOXm23jbJ-c0Iz6GzOzslPwWNSa4X-jHpAZA4QVz8CONZ7wOPLGGmYIoofLvDf4KZh5tuWzgfiu19UpCSe6Mk1RP5SYpnms32b2sm1yXo8nV3z1GdWlXAtVQ0Aje52OHbHeg0VHqARwqU--g_S61LIw8dCDvu6HuoJPQkBDkyFd_v9kW2tT5fDBvnprJO-pE_uW1lxcrCNlUxBS_NVPlhAqyL0xlKrMoUeh77mAXu9JvmkGWIHR8cTqBfKgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش سخنگوی کمیسیون امنیت ملی مجلس به تناقض رفتار آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/657967" target="_blank">📅 11:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657966">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88af73221b.mp4?token=kD0mSJYgq_boPeqXPsH6M4bS8naIcWh71oTAVZtELjA7UGWtmxoqn-bdHDSFKdyaOLQR6589kJqCHlPaX4DMgCBT00LBOmORO0ZQm8D7nyxYLn1zLipNIke1JEtAeJuKRdzWc2l1G6027z1uZy-RhpdgfDp2ECvaJQTn8nJp7Qcrv4aMt96P-8tRa2CKFugeyx5N77tuYdPqfZmUUojSscY1rZDmQuQiOigqhAkTExOQdwebiVF6wkiexXQpNRuDml7zMRiVIfzVo9H3vyiXvXx-Jo-d1k1IiYjbNnO_B8cToi-FpGDMmrLuvC-mDzheuB7ML9PwQsCN8aRtw8bRbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88af73221b.mp4?token=kD0mSJYgq_boPeqXPsH6M4bS8naIcWh71oTAVZtELjA7UGWtmxoqn-bdHDSFKdyaOLQR6589kJqCHlPaX4DMgCBT00LBOmORO0ZQm8D7nyxYLn1zLipNIke1JEtAeJuKRdzWc2l1G6027z1uZy-RhpdgfDp2ECvaJQTn8nJp7Qcrv4aMt96P-8tRa2CKFugeyx5N77tuYdPqfZmUUojSscY1rZDmQuQiOigqhAkTExOQdwebiVF6wkiexXQpNRuDml7zMRiVIfzVo9H3vyiXvXx-Jo-d1k1IiYjbNnO_B8cToi-FpGDMmrLuvC-mDzheuB7ML9PwQsCN8aRtw8bRbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر لحظه انهدام پهپاد MQ9 ارتش تروریسیت آمریکا با آتش پدافند هوایی نوین سپاه
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/657966" target="_blank">📅 11:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657965">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2166226625.mp4?token=TAGUCewbbGF8GxBuPl0Yyemp19ycRV8b8FY7ujwwr_x3luv6chn8MFo9AQQ6TgT4QpknbeKJw05fi1S68MT3QHckSU_op4D3eIy7TdCPsx2zSf3hBSRI5jx5IAimEl1dixw48cjLSFoN7e27_5HfX8WNubOAcjee8C-QHqOL0nT8AhMVL9blNBZ0PCBooFg1O_z-hDztxgGULDmlp1kUybetvNoO71PfJ5pP_VGtrXk5YUhJGkcFlKWYovC74u25_dPqlgTBFWkkXDqNIA7EMlfXBIXzxsCtu08en7B2nwSWJwPFWQbjCmssREs8iMGdZJiEyCYz60RfWPwxApgibQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2166226625.mp4?token=TAGUCewbbGF8GxBuPl0Yyemp19ycRV8b8FY7ujwwr_x3luv6chn8MFo9AQQ6TgT4QpknbeKJw05fi1S68MT3QHckSU_op4D3eIy7TdCPsx2zSf3hBSRI5jx5IAimEl1dixw48cjLSFoN7e27_5HfX8WNubOAcjee8C-QHqOL0nT8AhMVL9blNBZ0PCBooFg1O_z-hDztxgGULDmlp1kUybetvNoO71PfJ5pP_VGtrXk5YUhJGkcFlKWYovC74u25_dPqlgTBFWkkXDqNIA7EMlfXBIXzxsCtu08en7B2nwSWJwPFWQbjCmssREs8iMGdZJiEyCYz60RfWPwxApgibQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار آهنگ جدید امیر تتلو از داخل زندان
🔹
امیر تتلو که حدود ۳ سال است در زندان به سر می‌برد، آهنگ جدیدی به نام «رفتم که رفتم» را منتشر کرد؛ این اثر از طریق تلفن زندان ضبط شده و در بخش پایانی آن، صدای گریه این خواننده شنیده می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/657965" target="_blank">📅 11:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657964">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d0d226502.mp4?token=efrHWANVsOy9vP11L5UYxQFXw_3OrTpzzWcDcv1W7xG3ERvciSEbxPY6i4gph5hAkTvieptiIFOFubqznPMqzBuNBHQbS4vjTT-Y4uQtdWeIEtQAtLlNnlaPc4aZma3xcLe24YJOpg6h9lsss3-Umfc5R9P-3sj9qH1Fg8Ze7GZhC-58S2nxIumbl_Ij5vR7KQwZ1cnZw0faiAjBRFTaO7CuLx68vqO4al5S3xAxprhFqJPWH5lDMq7vDGlLR87edKHa44SYYw15wSyfOQJ7ApIlkqacdjI_jfmMfPmjXcDaxjseJdBI5eAA8hKTgP7EH2LsfUyoRTMNcD5y2Myd7FzJCiUszKihWObNXL6wE_D2wLbE5VA4D8pQb4AhujvfFXC-k93AZ4BzV5GNU43ZQpYETBGpR3_gIRS3CkJwqvCNBvU28JBlIg2OJJO0OKgHRtW6ep8L8ixZJqoe-6pzHkJRyJ4D0LQgMle1lEQAI3aHRETwX2MC6x8PY4_dE4Bt94ua-I6nsGoTf3JFufK8_8M3JS-J8GSe8jlXab46avVbTAQZWREojEvQUuQClnIBdtMimwvK5Iz_-iuTR2ZQdP6zZ1FR-6SbmGu288fmxsVK7LBa099zohPFycn9ondtpPO3Muur3jVHsV2DwZ7wV3wlCBEnguG_DLvO02sAxEs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d0d226502.mp4?token=efrHWANVsOy9vP11L5UYxQFXw_3OrTpzzWcDcv1W7xG3ERvciSEbxPY6i4gph5hAkTvieptiIFOFubqznPMqzBuNBHQbS4vjTT-Y4uQtdWeIEtQAtLlNnlaPc4aZma3xcLe24YJOpg6h9lsss3-Umfc5R9P-3sj9qH1Fg8Ze7GZhC-58S2nxIumbl_Ij5vR7KQwZ1cnZw0faiAjBRFTaO7CuLx68vqO4al5S3xAxprhFqJPWH5lDMq7vDGlLR87edKHa44SYYw15wSyfOQJ7ApIlkqacdjI_jfmMfPmjXcDaxjseJdBI5eAA8hKTgP7EH2LsfUyoRTMNcD5y2Myd7FzJCiUszKihWObNXL6wE_D2wLbE5VA4D8pQb4AhujvfFXC-k93AZ4BzV5GNU43ZQpYETBGpR3_gIRS3CkJwqvCNBvU28JBlIg2OJJO0OKgHRtW6ep8L8ixZJqoe-6pzHkJRyJ4D0LQgMle1lEQAI3aHRETwX2MC6x8PY4_dE4Bt94ua-I6nsGoTf3JFufK8_8M3JS-J8GSe8jlXab46avVbTAQZWREojEvQUuQClnIBdtMimwvK5Iz_-iuTR2ZQdP6zZ1FR-6SbmGu288fmxsVK7LBa099zohPFycn9ondtpPO3Muur3jVHsV2DwZ7wV3wlCBEnguG_DLvO02sAxEs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر لحظه انهدام پهپاد MQ9 ارتش تروریسیت آمریکا با آتش پدافند هوایی نوین سپاه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/657964" target="_blank">📅 11:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657962">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uuL4rs3h6KoX5New9Qsn_4fRM5t-s4Ulw6xUVL6e96KZeXQYE-_w8sqC7kX8ti0dbsU62p8TnUGDKX38ZTFmCj8wOUJS2omAry3OLN8RChAe40NpEdD0DHGKeyoVyBwTuBlJnItaIZeXxZ_6Ax1RCngBV1YswEDimO4_oUPem4cVYeI6MzbIKqfxn1Ri07n4yEumI_4mkFBghLnf9gGp4pnqmmnZWnQCCOjB5ea82cJ0DYwWV6h3sIXlwhVccvzlwWxdEsvLNbgSgwh1HDI3d_Ejjad99pyAwzphcESkNdlIi5zvEaFxJMXyYutagIftXadDgrM9x1ROwfpvYYL4ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U-biwmhovjU-IBE1lk1peaiXufiHcLMJnwmIEZdU9z_h7ujj71B3Wr_1GNEWdgis_KveU3Vzge4HmJyTF7_FtqyUQQ4xatq-hv4zrWhbq6SXVuX-kL2EfL-7RMRZA9t0DZwOAULvrK_x2mQpVLmAQEyu0HQMWrEvZOKV1uZdP_cKFTRbGoc5-PDzohQwN7fos1bvN3KB_llkfIvlQTLvr60LsNUVuUhURX7a_rC1Ios4QuXtBtcAyBZ1wgWzyul_kC6kLa4gR2kl0F5uiccYlWYCWIK4uFGkMA2CvVWPLCBFT-13j-ZN8rie7YRVl8-pRLJx1cyC1HVlkCgwejGYXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
استقلال و تراکتور در لیگ نخبگان؛ گل‌گهر در لیگ قهرمانان آسیا ۲
🔹
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌گهر در لیگ قهرمانان آسیا ۲ شرکت می‌کنند.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/657962" target="_blank">📅 11:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657958">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ادعای سازمان هواپیمایی: پروازها طبق روال عادی در حال انجام است
مجید اخوان، سخنگو و سرپرست روابط عمومی سازمان هواپیمایی کشوری:
🔹
در‌ حال‌ حاضر تمهیدات جدیدی اعمال نشده و پرواز‌ها طبق روال و برنامه‌های پروازی در حال انجام است./ خبرفردا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/657958" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657956">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZt-enFw-ss6ENHEgqLhX7rho4twndbCJP1knDKymzx1lbDD3Bx-cwczGxJlynD3blgLzAVLwHRhzBoY6YY_B6_UWR3vtU2ve5QWc_6BsgiaohOAVQ8p4JJJ5IqNIDluXPCgqOsYlj-4vrLEKUqPWTA8yU2IKxjglAKGJEmkCL1u4Ukq4Gm-v-gKqjMZyG8OMkgwaRnpaBKFyc7H5EfijZgbR4w3ZP2Mm1rZX19dS9lSZWhYAssvLegUwZFpJmdsHgC6rpPvc8yl1fUtZZRCj2jTq8KS4CSYAo-GNCAi7xUmvjfWzu-0QfTXS2y1PGO9SCoB27maB5ZOJZdoLyfoDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت به ۹۱.۳۴ دلار کاهش یافت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/657956" target="_blank">📅 11:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657955">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4w5suylZHHXCZ94tAqhc75BvObaQ34J4Nx5GGPDQyO_WYi4XE23epAvlaWISvviZ4_HePT2PmUZRiLt8lkTJ_W0-YAo2tSO7qAlZOk3CEcecFKTWA1yRNwmgWRlo6eOYlQ9c12pC_MkzD26WU2THxR_pi52oWLK8f93Y85V7MoqjGJjQHayDwxl7zgV3r2K3y-u7aGMu-AA0WA26B9llmRhU8flIY0HhaKALu7s7vvj82QXOrY8CJioaDydZW2jswbjZ72vkD78GY58WMZCOWIjB4XitU2zEU9boQyiQEc5nXY4fnNPjCw6S0NiTKZakdn793e9qeje3tzUXJdACw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینجا خط مقدم جنگ است؛ سربازان گمنام جبهه تولید، با دستان پینه‌بسته‌شان از مرزهای اقتصاد کشور دفاع می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/657955" target="_blank">📅 11:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657953">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO7ESkH7eDrs7kqFBbsCk2mg1qCiVfR9I8DzIvlinRUP3ACpLIsw4GPZYVJcAqPfbzTsO06gS4YvV3v-F_u6GT4Hx9UyEWsUgFcegdYg4ryQE_bRgYFjsqwjqs_6vQHb1x6b9CzLk3KnBrG_Kepidmd4IN6Jyw2H-m3esZl0Iwhctlp6KoVz9PR1ISMIzMCD5f3Vvp8FHIJZqYl9ehL-rxY57xMOamZkSHIchtpb61nj0XPhs0cqhQDhbakVnATsr8ce7UfTW-k8qnFsTatISA3BXu2IyaVFj8XkUXqWOoyzlZjedM5pftcczuLJ3PKpjVT4Pw0o3gRnIfmRgVnr_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر فدراسیون والیبال برای دیدار تیم ملی والیبال ایران مقابل برزیل در جام ملتهای والیبال
🔹
این دیدار بامداد فردا پنجشنبه ۲۱ خرداد از ساعت ۰۲:۳۰ به وقت ایران برگزار می شود.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/657953" target="_blank">📅 11:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657952">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92e56a49cc.mp4?token=Uek04GXBFVXDYua2JdZBYEIlDD8G0UtCbujLWIcWxQes-lXE7yuAYlwg5IQp3brhHFsZR1vKDI7jZ-g_IavI1is4KkfSEWNHVEUmjZUEaQ6yqdN4RHLt103HLrB62MsMNGpicftNDdLAn5IEu8FlafLVtqoUCUpNbf9ucFR4zcTdQA5UTA4_vJsvzPCxvKyYqifc6kwtIb6emOLwG01JVXRky8j84mTZ-UNBdNEk-k-c1LWD3MpySQf7rm-kRIzO_9qHjGdUiLoyraeD6z5Nrsx2P10qHHsgEbtGCzjEKqVvoxTK9ZGEkcdsSg2-_bqCGEBns5nedHIaj5JhiE4fKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92e56a49cc.mp4?token=Uek04GXBFVXDYua2JdZBYEIlDD8G0UtCbujLWIcWxQes-lXE7yuAYlwg5IQp3brhHFsZR1vKDI7jZ-g_IavI1is4KkfSEWNHVEUmjZUEaQ6yqdN4RHLt103HLrB62MsMNGpicftNDdLAn5IEu8FlafLVtqoUCUpNbf9ucFR4zcTdQA5UTA4_vJsvzPCxvKyYqifc6kwtIb6emOLwG01JVXRky8j84mTZ-UNBdNEk-k-c1LWD3MpySQf7rm-kRIzO_9qHjGdUiLoyraeD6z5Nrsx2P10qHHsgEbtGCzjEKqVvoxTK9ZGEkcdsSg2-_bqCGEBns5nedHIaj5JhiE4fKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا همه دارن مو سفید می‌کنن
⁉️
😨
توی خیابون که راه میری، انگار پیری زودرس به همه سرایت کرده؛ همه درگیر موی سفید شدن، اونم فقط به خاطر افزایش سن و ژنتیک
😢
اما حقیقت اینه:، فقط رنگدانه‌ها غیرفعال شدن! من خودم هم همین مسیر رو رفتم، موهام داشت سفید می‌شد، اما با این روش علمی و ساده، الان دوباره موهام مثل روز اول «مشکی» شده.
♦️
بدون نیاز به رنگ موهای شیمیایی
♦️
کم‌هزینه و ساده تازه، برای اینکه خیالت راحت باشه،رایگان بهت مشاوره میدن حسرت جوونی رو نخور دیگه، روی لینک زیر کلیک کن
👇
👇
bam30.com/ads/landings/22703-2e958
bam30.com/ads/landings/22703-2e958
bam30.com/ads/landings/22703-2e958</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/657952" target="_blank">📅 10:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657950">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9ER6LB-3uexiIrpicGAr6RuDh0dJRCIU0RIRGJgVQxnhm9dL8Ig5saEcnWPeZhmYIpxNI1411AkprjD46raSIAlU1sjtiQ-JpoGXql78gARwynrAj1x4OeeUoyUipKq_T6dxuBKINbSxQmielUZtATWGPBJxcChsExDS5457bTEwbrvNJu96kQkqXmRQ45pVnX7OjRvnL_mNzYoAJaaUmFu6TQpCNIMUWS7RxKNZtJdwWKxjd7XWjJcNA7Ns_gWT0-2WCfiLG-crPeXQbJa6JkWV0tbXLBuUkSITqJK9puRM-enmINspgnlAtdSvSUHpBU3CIvqmflkZFAqki444w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فیفا سهمیه بلیت هواداران ایران برای سه بازی تیم ملی در جام جهانی که در آمریکا برگزار می‌شود را لغو کرده است
🔹
طبق قوانین جام جهانی، هر فدراسیون معمولاً بخشی از بلیت‌های بازی‌های تیمش (حدود ۸٪ ظرفیت ورزشگاه) را دریافت و بین هوادارانش توزیع می‌کند.
🔹
فدراسیون فوتبال ایران می‌گوید این سهمیه از آن‌ها گرفته شده و دیگر نمی‌تواند بلیت رسمی در اختیار هواداران ایرانی قرار دهد.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/657950" target="_blank">📅 10:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657949">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYHVWD28lrI_go1vFw_Yw1G6mtKoNaQT9VW2pMGbol2U0WjoYRtqTOiNVhfWRVXu-PYuETnnJoSnyBeYr-uR2EB4wo4uprxg7RKqeTMi3lFCpQr-OCLNiDyDbPtNbePvTBb0f9fTnevj2eZ3DhIBlVI2q5P4ucYbLaCKhW7JRW81qInI7L11CCgQbTY8VObbnirMeLs2X15i3BKDJQCNs8qd9bTUdEDV2Uexx-VtZoBXxolGFJyh6O7pUhSwoJ1vQXid4B9gPoc6ZS8F9SsbcGq4sQfnSRrdCG-VNMH7kukvtXVSYgipX6QtUwHyL9WYazCu1CUmphXMUml7wARTxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سپاه هیچ صفحه‌ای در توئیتر ندارد
🔹
سپاه پاسداران اعلام کرد هیچ صفحه رسمی در توئیتر (ایکس) ندارد و تمامی اکانت‌های منتسب به این نهاد جعلی هستند.
🔹
پیام منتشرشده در یکی از این صفحات نیز با هدف ایجاد تفرقه عنوان شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/657949" target="_blank">📅 10:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657948">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXV903533MFWbvxPc4VI5l92t69gRK1TThzRMWEICqnpvqiv_LLVAddKozX4AMwjhykpn3wAQO6-uTW3ap_hCoflWyXxFsY0hy5NELBSsp8YJdMG8kYS-A-1x64F75UZ3wopF2r9jxjf4aMsTk-r9yyNKgLRLfUBoViLpS-aty4Ep3Dwt2Q6cOJ_kquo6Vr5tDtXnYG8YYllDGgPCiRvUnPY7UE9HdOTPDon_VuqrOx_gR6PAIxcEGjWkpa_LhqRLN0Yc6Gek60EEsfoAVzC0GU1IIquZDM2cHJp1BCaBFUblTOmB1uzARTXt8WyIIuQ5szl9wzxqQVWE_qCF12stw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت یک متر مسکن در تهران چند؟
/ خبرفردا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/657948" target="_blank">📅 10:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657947">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
امتحانات مقطع کارشناسی دانشگاه‌ها مجازی شد
معاون آموزشی وزارت علوم:
🔹
امتحانات مقطع کارشناسی به‌دلیل فراهم نبودن شرایط حضور دانشجویان به‌صورت مجازی برگزار می‌شود.
🔹
این در حالی است که آزمون‌های تحصیلات تکمیلی طبق روال حضوری خواهد بود.
🔹
همچنین در صورت تأخیر در اعلام نتایج آزمون‌ها تا آذرماه، شروع تحصیل این دانشجویان به بهمن‌ماه موکول می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/657947" target="_blank">📅 10:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657946">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9JBi9i72n3LYWRzYYiWnU6naIHJwXSfzp4A-SuKmm5icpPIAeyZ30CD11jQPAuWyObfXJssGFTs2E8XptrBExaSv8dCoZUV3ei3HVocydg4EeeuguJCdF__VFFLduoqff746FXp2ksZRHgooxuQA51seNhIELnXSBH_kw-7Q3WGBieX8QqaclK6vC0bV_imRoem5M0bKZLUrFqbSCcnwwjplxZKI3P-9B8A7QOw8SCQlscho2iOjQ44xXkiqXZ0hZdku1SRJbQI6wLjSF3NS6g-ykYUDn37ts4UhIZKp0X3khUczxc9RFlZRr_hcnZFW-7K3CpayiTjzRPcqXx3Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر توییتر: ترامپ ساعت ۶ عصر: ایران نه نیروی هوایی دارد، نه نیروی دریایی.چیزی باقی نمانده!
🔹
ترامپ ساعت ۷ عصر: دیشب ایران یکی از هلیکوپترهای آپاچی ما را بر فراز تنگه هرمز سرنگون کرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/657946" target="_blank">📅 10:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657944">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a482f7f99d.mp4?token=Mu7nfekMmyj4SL_GZbBM-iCJuw0CUbhYzXbLfb5Gr549c2FnlkgyGBFco5dKLwmUdt8TPeSmTvd8kLOY4_1aGiLDT5y7fUOPlVACqnCx8m42nwG3WrLy-ODS_1GUQX49snPrHO3eWyWPK8dVTp4jprSTGRDJpNKsVgdC6d7u-SBR1jDm2NFJZmBOg_iYGEabHV5FUdGjxV4o-x7nzkZjwY_WmYIvJV7PXtvYvQC3HCmeqV6YdNKkF4Js3wCKB7zhkCKGf7QpnLopb-8CZizWDiIeL_nEKrJdKbcXfLSJZDWgV5euOShnZcMRsb6c6BSRUv5CsQ1fJfuQRdq8hs6OdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a482f7f99d.mp4?token=Mu7nfekMmyj4SL_GZbBM-iCJuw0CUbhYzXbLfb5Gr549c2FnlkgyGBFco5dKLwmUdt8TPeSmTvd8kLOY4_1aGiLDT5y7fUOPlVACqnCx8m42nwG3WrLy-ODS_1GUQX49snPrHO3eWyWPK8dVTp4jprSTGRDJpNKsVgdC6d7u-SBR1jDm2NFJZmBOg_iYGEabHV5FUdGjxV4o-x7nzkZjwY_WmYIvJV7PXtvYvQC3HCmeqV6YdNKkF4Js3wCKB7zhkCKGf7QpnLopb-8CZizWDiIeL_nEKrJdKbcXfLSJZDWgV5euOShnZcMRsb6c6BSRUv5CsQ1fJfuQRdq8hs6OdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات حمله آمریکا به زیرساخت‌های آبی سیریک  حمزه پور مدیرعامل شرکت آبفا هرمزگان:
🔹
نیروهای آمریکایی به زیرساخت‌های حیاتی توزیع آب در شهرستان سیریک حمله کردند.
🔹
در پی این حمله موشکی که ساعاتی پیش به وقوع پیوست، دو مخزن استراتژیک آب در بخش بمانی هدف قرار گرفته…</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/657944" target="_blank">📅 10:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657943">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5ITvqYn_KGiQ6klro30fq9-phvMV1GgK9vOyPkJTEZ8iBkEvxaNAsMKNFrSg0u69ltA5wemdYYwU3U8OgQ5fJY7pbI1nT47C7DxpBZ7Ja4jEYc_TTzlgOHxjXuxkkiljZBF3qczWeoPeUwQwO5EFPOZLG_OGG9MrL2fVE2a-hxRr5laYVYRGa9SQOkOppHUGeY1WbyBj6cPqMVRJpSd3BCydvEcvHn4KEp7ILZk-h_utn9jgHX2YvRkxvqiibAsOQgW5rg5vl4WDfNJfhoY-Oukt1R8QZPQaRidwUxZPsdglGCyXUqQIAQ2cuh7L4Jt2xSOOb0BCbAAu33C_Fqxvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخستین عرضه اولیه ۱۴۰۵ بورس تهران، مربوط به گروه توسعه مالی فیروزه با نماد «
وفیروزه
»
فقط تا ساعت ۱۲:۳۰ چهارشنبه ۲۰ خرداد
ادامه خواهد داشت. با توجه به شرایط بازار انتظار می‌رود این عرضه اولیه با استقبال گسترده‌ای مواجه شود. شرکت در عرضه اولیه «
وفیروزه
» در
تمام کارگزاری‌ها با ثبت سفارش خرید از طریق سامانه معاملات برخط امکان‌پذیر
است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/657943" target="_blank">📅 10:31 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
