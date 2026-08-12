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
<img src="https://cdn4.telesco.pe/file/kQTnWz9_dPFhiQrfnjHw1dBVLYTjOAZkO1Fo8TtMqbHd5O-dkMHJL9qSQTxl09qB2jKIByRpwSeekQDXo93iTg6CszYrgOUMNyC7ZC5e0Ja-VZxTL35_RRg1uYjOcTd6ZuXPU8elYLqkUQgbeTboSW8-GbOpD-cFwkXMZrDKfcQUTWIM7zS2MvUBhhKlSAKs8YsTeMGLZFrQOJzmxOs3lQ-ojPRB8Ye2ZgQyQ000nvfuNaOUXxmbcIUwuQbBtQXmbaj6QCSxnshHM2Tu3CuNK1Urk7L5hfPKC1DuwnACUWLy9MMaFGjkKmgk-p-sIjfrZ0B9cWtdHYsNCBBkKrlo7w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 21:44:00</div>
<hr>

<div class="tg-post" id="msg-455742">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKosrzjMTS3XxCZM-s3dfv8rbm3TWYVTgkkYOt3E0Od-CT4A3YyFOH2Fv-hxmtOeEv0kYtXGl0rjN8CuynhMEflN-hOPkjc98uvhkvsPShkgwTxCljAHn8-ZL4yqGAa_1O4Zn2SiWqUauxleeERwiaoerTk6pWM1We6jLVEguN5G74h-zfw-IgXKweWrVkf_W5jygxF9J8SQ0MRh5pq1ZckwM9U41ClKmesLgjuqGKBHHSrxR8JmP9QU1UkS7VaWgm_VUxBvvZlYqEwmhpDbQWFnUEpZX2ygsko2e86kWVsU38_eFwhbogZpQB14jqplk50SwV0QQW0n7yeLgjbj2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیکر شهید ۱۸ ساله پس‌از ۳۸ سال شناسایی شد
🔹
فرمانده بسیج اصلاندوز استان اردبیل:  شهید جاوید‌الاثر اکبر بابازاده، متولد ۱۳۴۹ بود و در تاریخ ۱۳۶۷ در عملیات کربلای ۱۰ در منطقه ماووت عراق به شهادت رسید.
🔹
پس‌از ۳۸ سال، پیکر مطهر این شهید والامقام شناسایی شده و در روزهای آینده تشییع خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 992 · <a href="https://t.me/farsna/455742" target="_blank">📅 21:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455741">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmDTEd1QyzqPnXdzd9_qL3H8uEeN4VVfz_Qod27_uaAraIyOPgR0cyqdFtum7FBb_Epwe2nFOU5NArtbQpFjZo6zC8W6dM5-DjcdKJAa2-QpKWDy44ArD2kxHplqYIyry_Bav91w4YOlF_qUEi2QdK6EXAfVFAanae_xXmeB-K3Co4FkkS-NTUrFeCOt6LqxMkNvArAToj6ODK-4pB3Jzk4GAG4QxbklEkI9ZwBCz2Y6qOLx9vq1Ip8KbetVcHQQ7AxiwpXSGN0TMT9-ojBOeXP6LEPpkhScU-6NNimD7_jYCuB1k7Zk0mZNUlRSk3lymGDL8Ag24CS8MwhQtR-0rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویب کنوانسیون خزر ایران را از کریدور انرژی جنوبی حذف می‌کند
🔹
الموتی، استادیار روابط بین‌الملل: در این‌که رژیم حقوقی دریای خزر باید مشخص و روشن شود تردیدی نیست اما باید کنوانسیونی به تصویب در ایران برسد که دست‌کم درحد قابل‌قبولی منافع و امنیت ما را تامین کند.
🔹
در کنوانسون دریای خزر حدود بستر و زیربستر مشخص نشده و تصویب کنوانسیون دریای مازندران، بدون تضمین و ترسیم خط مبدأ به‌معنای واگذاری برگ‌برنده در حسّاس‌ترین مذاکرات پیشِ رو است.
🔹
شهید رئیسی نیز در اجلاس قبلی سران کشورهای ساحلی، تصویب این کنوانسیون در مجلس ایران را منوط به ترسیم خط مبدا مورد تاکید جمهوی اسلامی ایران دانسته بود.
🔹
همچنین یکی از حساس‌ترین مباحث، موضوع عبور خط‌لوله نفت و گاز در عرض دریای خزر است.
🔹
این طرح، نفت و گاز ترکمنستان و قزاقستان  را به باکو رسانده و در صورت اتصال آن به مسیر ترامپ و یا دالان زنگزور و از انجا به ترکیه و اروپا، ایران را از کریدور جنوبی انرژی حذف می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/farsna/455741" target="_blank">📅 21:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455740">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAWSWb8H-elEkV3mJo_Fh5dTQUZkI_zZuiGNeS1LSKEez0X7OQEcM5v1GrVi_7LBCJxvZn8vE1yqtaMueUZPKBL5I49xCsZTRCGb2j-gRJpA2Xd8tB94Ilfa-ioHhYfqo3RiQWOChXyhQOxE5iO7fJg6sQwnroZKDq9qP9w3bgjfdbJvyx1qsGJgsjWeSz0BGbYxp3a1Yu1Lq8xYtCGXTw8q7L8gXadVQMZZO9drjkqyv4kWwJ-Byc72FZsuYn-8nZ_6BcRKZZTW_I-Urw9deblUzOD6neW8e33ybEo3knlIvIDXs56sHooYBQcfYYbaDo5CKZDXy3xJFPutlJU8TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«غلامحسین محمدی» سرپرست سازمان تأمین اجتماعی شد
با حکم وزیر تعاون، کار و رفاه اجتماعی، غلامحسین محمدی به عنوان سرپرست سازمان تأمین اجتماعی منصوب شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/farsna/455740" target="_blank">📅 21:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455739">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2MYAytrWO5gN702BS8ekLHmCKyRQh0BZMR2p6KokumRZYBHw-_6O04qCkuI8HvE6xeZKZqgBE8sDsq631OqX_ICKVtdR1xTafIv6kLLuAY0H0kDsyvX8IryjiNT4QKDvGOosPbZ21l3p3dJ9A8wScSmkYWflJMyVB8YOFjplWVDzFuLL8nCGZzDJYaawBIeMnl-vA6MP7w5w0CLDseHlFLEywwf_Sccs_bE3twm0FREuKMiHz2MQdVbI6WHQUty6Txw4edw00guXoqcmUmo2hrlRxaQxC2x69R27Kh21m9zlAdCXR6qOFqLvJJKrJQ16VvvE9GFcJypc3hCOpnAfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ثبت‌نام دوره تخصصی «هوش مصنوعی در روابط عمومی و رسانه» آغاز شد.
🔹
این دوره یک برنامه آموزشی جامع، کاربردی و پروژه‌محور است که به شما می‌آموزد چگونه هوش مصنوعی را وارد فرآیندهای واقعی روابط عمومی، رسانه و ارتباطات سازمانی کنید.
🔹
در این دوره ۲۴ ساعته، از تولید محتوای حرفه‌ای و مهندسی پرامپت تا تحلیل افکار عمومی، رصد رسانه‌ها و مدیریت هوشمند بحران را به‌صورت گام‌به‌گام فرا می‌گیرید.
🎉
ویژه مدیران و کارشناسان روابط عمومی، رسانه و ارتباطات
⚠️
مهلت ثبت‌نام: تا ۲۷ مردادماه
📝
ثبت‌نام دوره حضوری
📝
ثبت‌نام دوره آنلاین
مرکز آموزش‌های آزاد خبرگزاری فارس</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/farsna/455739" target="_blank">📅 21:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455738">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/farsna/455738" target="_blank">📅 21:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455737">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وال‌استریت‌ژورنال هم بلوف‌زنی ترامپ دربارۀ تنگه هرمز را زیر سوال برد
🔹
درحالی‌که ترامپ در روزهای گذشته بارها به قصد فرار از شکست، ادعا کرده کنترل تنگه هرمز را را دراختبار دارد، نشریۀ آمریکایی وال‌استریت‌ژورنال امروز با انتشار آمارهایی دربارۀ تنگه هرمز ادعاهای او را به چالش کشیده است.
🔹
این نشریه گزارش داده که روز گذشته ۱۴ شناور از این آبراه بین‌المللی عبور کرده‌اند درحالی‌که که پیش‌از جنگ روزانه ۱۳۰ شناور از این مسیر عبور می‌کردند.
🔹
وال‌استریت‌زورنال نوشته از میان این ۱۴  شناور هم ۱۱ فروند مسیری را انتخاب کردند که تحت مدیریت ایران قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/farsna/455737" target="_blank">📅 21:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455736">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c06ad40e89.mp4?token=tYkq8Iw95pnPwGAO_BJO3c4yHSvs5_hGZKrzHpuFsKpZDZnQxgYsE1pZx9MQXU2jxNtoyAxMCDnb1F-gjfGorJTkpbXbu3w2l4riP7z0KiI_YhpoV6ZfTSB4thFefTesM-TPkQXS1SJcs89a5zI4R6mIRDTBtQ_-WXqN8dMaqhfY-rdRdU_wqo7ehFLayprd2roF6LZdcwy6NbVFon3n1G-LjrJvu-Ucw0_zCpbDQT5WUK0mu1ZHBSnHBAWVQOAuTbKIMS3A0Vx31c3AxrDcTBMkO-KG1UgNI7Mwf72SZqe-tL-cKfWULiJ3yfv9yiMOmRHcXw7XdpWrDNVXg0Wrbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c06ad40e89.mp4?token=tYkq8Iw95pnPwGAO_BJO3c4yHSvs5_hGZKrzHpuFsKpZDZnQxgYsE1pZx9MQXU2jxNtoyAxMCDnb1F-gjfGorJTkpbXbu3w2l4riP7z0KiI_YhpoV6ZfTSB4thFefTesM-TPkQXS1SJcs89a5zI4R6mIRDTBtQ_-WXqN8dMaqhfY-rdRdU_wqo7ehFLayprd2roF6LZdcwy6NbVFon3n1G-LjrJvu-Ucw0_zCpbDQT5WUK0mu1ZHBSnHBAWVQOAuTbKIMS3A0Vx31c3AxrDcTBMkO-KG1UgNI7Mwf72SZqe-tL-cKfWULiJ3yfv9yiMOmRHcXw7XdpWrDNVXg0Wrbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان سوارکاران در راه حرم سلطان خراسان
🔹
کاروانی متشکل از ۲۸ سوارکار خراسان شمالی، از روز گذشته حرکت خود را آغاز کرد تا پس‌از پیمودن مسیر ۲۲۰ کیلومتری، فردا در سالروز شهادت امام ‌رضا(ع) به مشهد مقدس برسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/farsna/455736" target="_blank">📅 20:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455735">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15d9f23eb0.mp4?token=UVH996Q5HzQSri46RFqKq6WfRKH005HDmf6bTrm4sUW1-lHE-6MEbi78QOlGS59_kaYSIf6_2krE72ZJGuPrdOAkV5QmygfdsJVL0a7hvtODcGKF3EVu6X20tUrvlnXi4bPJ35aoY-Mhkyq8KRpYUyGRSOGRHOJGshOPWMP3crmGXCpGnf3R3pIHTnCgV7oR-WrMchhQ1bEmR0BN9uuYZn75uLSKEVdag6N3JF7lM0AaKhuSwRiPIjn7azUL_S58AJURvyjfRQABi3cHl2OQCARR6EvnG3IKdMeC7FZVrMgmJvd1TWOznhd6D88add_pqMi6xRZpTHTbSInzZwLTZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15d9f23eb0.mp4?token=UVH996Q5HzQSri46RFqKq6WfRKH005HDmf6bTrm4sUW1-lHE-6MEbi78QOlGS59_kaYSIf6_2krE72ZJGuPrdOAkV5QmygfdsJVL0a7hvtODcGKF3EVu6X20tUrvlnXi4bPJ35aoY-Mhkyq8KRpYUyGRSOGRHOJGshOPWMP3crmGXCpGnf3R3pIHTnCgV7oR-WrMchhQ1bEmR0BN9uuYZn75uLSKEVdag6N3JF7lM0AaKhuSwRiPIjn7azUL_S58AJURvyjfRQABi3cHl2OQCARR6EvnG3IKdMeC7FZVrMgmJvd1TWOznhd6D88add_pqMi6xRZpTHTbSInzZwLTZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۴ ساحل قشم آلوده به نفت شدند
🔹
سواحل سوزا، شیب‌دراز، نقاشه و بخش‌هایی از جزیره هنگام دچار آلودگی نفتی شدند و مدیرکل آلودگی دریایی سازمان محیط‌زیست می‌گوید که علت این آلودگی هنوز مشخص نشده است.
🔹
هماهنگی‌های لازم برای پاکسازی کامل این محدوده انجام شده و پیش‌بینی…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/455735" target="_blank">📅 20:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455734">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hi17i6bhgQkxSujQQfjrM1S8Xx8TUJvkXMfLS6vQw7CGZLW6fC0GDUw6H732QuOt1Mqg3VpJUb_iDvu9jrbgWidKcQBpJTTsEoxbLbMr2t4W0098ZJrprMNcKzyspGrEb9U1ngk9P9pTkdQVXjdZemVosBKm5hdplaZCclROupEHd_lTLiUL6yETwyFByR9HUFRljxU9-XFLGX1rgy_Pa_WuG64mk_OsTrS_iQWFQiApvLHcyKdRywGQC6F6BBUC2dL90VZvO9g6ZhtLZyThgudZGA07jGmV3ORcoGMOQW6skUFSDX1sFAfjIzpX4fear-CrWVoqHC2zkRyDBZKmIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار نقدی: حتی اگر این جنگ سال‌ها طول بکشد تا روز آخر موشک شلیک می‌کنیم
🔹
آمریکا هزاران منافع اقتصادی در سراسر جهان دارد و همۀ آن‌ها را می‌توان به راحتی نابود کرد.
🔹
باید به سطحی از بازدارندگی برسیم که دشمن دیگر جرئت حمله به ما را نداشته باشد.
🔹
ما هرگز جنگ واقعی و تمام‌عیار با آمریکا را تجربه نکرده بودیم تا بدانیم که دقیقا چگونه باید با آمریکا بجنگیم؛ در این ۵ ماه، ما یاد گرفتیم چگونه این کار را انجام دهیم.
🔹
در این جنگ ما متوجه شدیم ارتش آمریکا از آن‌چه ما تصور می‌کردیم ضعیف‌تر است.
@Farsna</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/455734" target="_blank">📅 20:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455733">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6484ef1de9.mp4?token=YVPKBtADSssHWvMCA-A4UylnFJcLEBmrF4YrvITpm6RNE3kFIgICR-s71A5aJltMMy-nT0EkOeWDUED-Ricc5RUTh2ZUZJhox94-yaYqW6fuMcTkH0nPFRT4CI0xQIq0UJzNsuwbJCTumfe4-ulfk2l0iPRXKKULZyLRxnmeltFBAibMK4Mgfc6USAJTgNzyr58RfZgt3zNzrMFTW_U3fv-0MbToTbgurmKr9AnBu3eP0bK7a2YitGlV-5meWAHVssokjSex5PE9qnvpdg30oOpQFt66dV0nnwA4xq9d4OoYfV5GFQZoDMswk0hPlzR2FrTTpTky6cVg-kVGDlEiNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6484ef1de9.mp4?token=YVPKBtADSssHWvMCA-A4UylnFJcLEBmrF4YrvITpm6RNE3kFIgICR-s71A5aJltMMy-nT0EkOeWDUED-Ricc5RUTh2ZUZJhox94-yaYqW6fuMcTkH0nPFRT4CI0xQIq0UJzNsuwbJCTumfe4-ulfk2l0iPRXKKULZyLRxnmeltFBAibMK4Mgfc6USAJTgNzyr58RfZgt3zNzrMFTW_U3fv-0MbToTbgurmKr9AnBu3eP0bK7a2YitGlV-5meWAHVssokjSex5PE9qnvpdg30oOpQFt66dV0nnwA4xq9d4OoYfV5GFQZoDMswk0hPlzR2FrTTpTky6cVg-kVGDlEiNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای حرم امام رضا(ع) در شب شهادت ایشان
@Farsna</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/455733" target="_blank">📅 20:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455732">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCMeuKKCCLzAVeDz0WjBe2zSf-wdPhl0UAbbmvRdiS9jG-DYewRL6ch8Mi2WY0taayE2797iL3uWk69DhoCXm2bLCR2O3Y-9_yt4IAwiq5d8Dwm5VF7uqSq7xjlF2HvOmf5gdCi0xLVeYG3cI5DPtKoTXHre7ZSZaLEuMyZp-dAH-ppDjOl0vTqQcvrPHJir5bLTwMALy_pHFByFiMMVU0IX7PBR5yNq9JU29XTVJtzTiQF-QYEXxoymPnZwDHxmpv9LR-1fRu8Z6V9FpwSSwP448bs1ybqf69d5zBEaEpDgL3L7WakFhDE_CB_lR2zPeqt7UkVlYshMRqqIvfQbJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار نخست‌وزیر عراق با فرمانده سازمان تروریستی سنتکام
🔹
الزیدی، نخست‌وزیر عراق گفته در جریان این دیدار به پایبندی بر خروج تمامی نیروهای نظامی آمریکا از خاک عراق تاکید شده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/455732" target="_blank">📅 19:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455725">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kv_UTcXppO4gH03c6ODjMdOi_3W_bZX2Fd_SOjjQWkw-ZTmKd7IR3DMwmN6SAlq6pcVCElmOgQohhVzGAc9T9mq8cqnULHrdS4jjM75AWQdYh2kSrDBYQEkpcZQaZHYBveBhBkEc9fvF-htgI2NXcoLdS3spTJUpwi_e5bNmyhXhx-rTu6K43evYdxq6Rmufe2dSuN7pjAcFWDsr6ro7S2eE2Zm6NQv3t6LQCRBJzxjwo82X-6xfEeMdACsb0nToI15xDNIkaneS74qBCugo4AD8CGM6_E4iGhsJ3uXD05oXrjJHsTgnEabK7kJn-vIQMJvzDrchkvPxwO3NhigVow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7ILFgiVulhV6QsKmFIgDkt__KRPJKUuWykQaLU5yRMXlERFbwWhioemx2SlNh1q7MuPXcb7-n8bd3rADo82VvuuHmiQ4fIYVNwEAABjEwqIlZlqQMzbbiivKKmlT1otaVp50Vig7o2U8UVC45SNKYGvhWk6XzqPHIiu6pBB98rRWPbO7S9H6pEqzvy6159IJPkTFlFJ0JgP4VLp7vGE3TaIq3QDtLCEt689dIegwUp0jyUFbKmOxE91MF23ggrFxN-J1ib06DhNLMBX6tMFvmPzmtm0YosrszbGMPm1sXDXDjZ845X7J5ue2xnlrzFCfsmmg7B1t7ePOmD0DYd6pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oE3tgE4EdlYQH9mmkXXDkCzP-KkwrUrLzjgUPwjGOd_Q-SheykR64FIGgwGSNEWqUrckXAgqzlTdmVkX_2ctpD14qRi0_7nI5xqU1PYgI9Lrm2XKUGVVhHRuxpZFNvahqvubs-xuLXBBVw5kpQNN23gM7lFLokX2MfnvchxGq7PU7ko86RrNWKNgjPpdi--bdn87QTxscFoSBc4tAnI0nIYARXIQ6yYFfbrZ4jBESSGJjJGtTcAUQGXovCcUPRZWSC08f8FN69_n0kOZmZvnvezb6HXddq4G8LOs1g8nkFcgMOrLm21tfyFcAy2uBChNaGBI5TNzVm1ThDX8mL7f7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/URnDqnJalV2pwoncFZkbH1P_qJrjmIfNI1caXfGfgCGcAdcUdXUGPt3xMP3Dm9eU2JG-ojXQRP1BF8To_u2Llr4nPPvkddkiG_du0892anKuQlu1_uUNv53lbuo_6EN380TUIYRa6ARd08Y_4GU0ciI7aD5QR3uDOT9NuvOfuJjIFy6pvnrQvGgS8BH6e3wXplzb80Lew1sf7Np6W9PdC0LMNhV9Q_jF80K2b606LCn873C3RKx1MZTmmYMiEEPwEZGmQOWoi_2Ga8D8OLgLmGlpM0Krv-5pl-MglKkicHAaeLHjhGbYFvPrFv5YRz-tLrzpGb-TeoDSBAk1-8kx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O0PRECLI-PJeDYlxnVrK0riixRWF38z0m-5FKp_cP7YIBu8s4rIHoIQzkZyAqlMtMnxp9m_hq2FvI_KYuOvnX4nJACrk406J-yhYOND9n6RKohZqITDyjDdkivmBRzCdAses1JBodT_B1PsSB_tjRSGXHg9yv90ZqfO1Ni8p_OhKT8HFr9gnz_fBaGuVvPy8v0iiMMWV6cUUPcaeKU3urr_eTyvlYKg0BpwtAVVrQ0R2rIRlXjb68QJlzDbqd6AHI-5C4cMoGHAtTPsvhG8zrCOAC5_FevwRErlfrn3wGXR49oKUirbVkK3ZoTFvwPzAH23qSaO0r7xIcXg79yz_AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eO4DBveWaHv9MZ1uqnyJ9EQNuQhcXPy2XgbJUt0nOdMaPCOXVoB_TvgB5dFiBuRbWldKS3zpinvS1cvzcA5pbN7fzxEt2E-9p01eSS9JodpuvhXbF3tUgEwxcYaVYboSzGoKvcARRHi_mdgygdieaM41pUmkdsiO-J4ShGssmVtPdec7EV01WvfkXhY20unISREF2Ki8pnp4r0XG1-XBJlpHRJ6Y2v_QXnbvTHSu1gK-H4Oa1bwUVi9MSL1qTMwHHPh5BUQQ3RTZHlXLvDItUpDGji0yPkA_T6dSFE4l14wn-laduU97dYTCWQQlVcpK8kpHsAJBiqdp7q4zjtmVaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RfOC5YjEcH7ayxV5cTvTweAoWy5rfFZy15CDk3d-yWCIgLV1rvVD0Bd4Ce_BNjv9KUGZBECoFGJOusG0Jj4cXK7zQSeAX_gTzlONTTDChRRDFUEIR8rpK3SBRvZEigZ-1db-OfKtXsKbHi1D_8k8qpSXAv6yy1-CY7OHbJTze773sMbYdp6-mCU0jSNu17Hcn16BQ7muSXT6debXPca3kP6eRa-Ti0M_IQgQAFqI4jDL7sHQSlcaE3EzvsqA-MV1u44gocp1m5EN193EaOE9ce4OuDi0rAWfJYO0s1qZZ7iUf5m9KznLY__xOmG8tz9GMYWOfOTZhD_rdr5uEy3r4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مردم تبریز با پرچم‌های سرخ خونخواهی عزای شهادت پیامبر(ص) را برپا داشتند
عکس:
حسن محمودی
@Farsna</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/455725" target="_blank">📅 19:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455724">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🎥
جاده‌هایی که به پناهگاه مردم ایران ختم می‌شوند
@Farsna</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/455724" target="_blank">📅 19:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455723">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59c3dff57b.mp4?token=hZYBiB2-PxkwZtAN5i0fZxWzi09lz72w3NWvxOH6kzpIUW7rP0ggGWMf-gjs6PagZzuEJGz4YmzNMBvNZutV95U6RTEBLZtxYv1vZ-JXS5x7vQvqfecqiLSkBSuV1sTUB30iMeQ5ivEicocd9FebIN2e76yqiLFlWl8wERoEz0wr6gS7-9fn3jwAMeubUekdC6Yfw_5BousqoW3LGCESYkkab70FF9jgbQLABQx4sOFFqf8tyVoMsq9vP2EZ91yR6X-11t5DuPeeVlTxon_9kwIdTRYCWdw4YAbbpAqOTF1_Or5N-ifonMjgmlCIGpbRazNpdQD0bmqM60RCRkmD6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59c3dff57b.mp4?token=hZYBiB2-PxkwZtAN5i0fZxWzi09lz72w3NWvxOH6kzpIUW7rP0ggGWMf-gjs6PagZzuEJGz4YmzNMBvNZutV95U6RTEBLZtxYv1vZ-JXS5x7vQvqfecqiLSkBSuV1sTUB30iMeQ5ivEicocd9FebIN2e76yqiLFlWl8wERoEz0wr6gS7-9fn3jwAMeubUekdC6Yfw_5BousqoW3LGCESYkkab70FF9jgbQLABQx4sOFFqf8tyVoMsq9vP2EZ91yR6X-11t5DuPeeVlTxon_9kwIdTRYCWdw4YAbbpAqOTF1_Or5N-ifonMjgmlCIGpbRazNpdQD0bmqM60RCRkmD6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فوران آب پس از شکستگی خط‌ انتقال آب به بجنورد  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/455723" target="_blank">📅 19:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455722">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/141b8c11ad.mp4?token=uuWIyE7RZg4giYhp05a44iEsNdayou2trvjei-lGS8Bewa7d9F94EHQklO4NRs8D_cL_pqZ9uhT5XlJQj5gapLVPPf2fJ7Bem2wncKgMnqzAu5jvMoDZeDG5zNzuKhaio5i8Uzi-ELodtSlBVI-HAdgGrTpRvSVOZ_r99H532fAzt5EzC9uidJXGMU0r9cRBVKH-mR1h2AQsxk8XOz0NxidM-qtemR7dg8tJ-uoRnaN-h2RJw-6IH9StBD2muJqJVNxmC-IDSb9mYIhD1sSpmgj_p5XZ0zqqf7dNVve85HG-yDp39ij7VpEc8pb_l0WICbXwubRkIGo5SPWLuJqEQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/141b8c11ad.mp4?token=uuWIyE7RZg4giYhp05a44iEsNdayou2trvjei-lGS8Bewa7d9F94EHQklO4NRs8D_cL_pqZ9uhT5XlJQj5gapLVPPf2fJ7Bem2wncKgMnqzAu5jvMoDZeDG5zNzuKhaio5i8Uzi-ELodtSlBVI-HAdgGrTpRvSVOZ_r99H532fAzt5EzC9uidJXGMU0r9cRBVKH-mR1h2AQsxk8XOz0NxidM-qtemR7dg8tJ-uoRnaN-h2RJw-6IH9StBD2muJqJVNxmC-IDSb9mYIhD1sSpmgj_p5XZ0zqqf7dNVve85HG-yDp39ij7VpEc8pb_l0WICbXwubRkIGo5SPWLuJqEQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرار کامیونی ترامپ سوژۀ طنز مجری آمریکایی شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/455722" target="_blank">📅 19:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455721">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رویترز: هیچ گفت‌وگویی میان ایران و آمریکا در جریان نیست
🔹
خبرگزاری رویترز به نقل از «یک منبع ارشد ایرانی» نوشته: هیچ گفت‌وگویی برای تمدید آتش‌بس میان آمریکا و ایران انجام نشده، زیرا هیچ توافقی وجود ندارد و در نتیجه چیزی هم برای تمدید وجود ندارد.
🔸
خبرگزاری آناتولی ترکیه دیروز مدعی شده‌ بود ۲ طرف با تمدید ۶۰ روزۀ آتش‌بس موافقت کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/455721" target="_blank">📅 18:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455720">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plBX3gU_8J8ooIuiC_XUcSn50o_bWrJGqCdc8nEErnSS5m5leN5B9mziD1svp6qJW_CK7wwNlWct075wf8aXif3o2yzTErZTqmVVaya8GnfRmaLC4YHszTvHO-lpAJHoDbKF9q6Gw2iAbzu5E9WSZd2xTcmtrl_hLTeHJw4I3N3OJy5TXnJ1M0lMIRynLnkD0Us8WIxup_1btT8X4GqlUcCZ3wt_AQ7sMKYVS6uT5Y-vhfH2-TZdn9QXhHiT5pBd4uqO8_gZ1melscZCsG35UM3vPI4lSlxIe5pTT6nI3YC5nZPiWeKCJEXDKUlcemNwPm1ZSmGCRzRNX1mVNvEkZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راز بیدار شدن پیش از زنگ ساعت
🔹
مغز انسان یک ساعت داخلی ۲۴ ساعته دارد که زمان خواب و بیداری را تنظیم می‌کند و بر فرایندهایی مانند دمای بدن، فشارخون و ترشح هورمون‌ها نیز اثر می‌گذارد. نور محیط، به‌ویژه نور صبح، نقش مهمی در تنظیم این ساعت زیستی دارد.
🔹
وقتی هر روز در ساعت مشخصی می‌خوابیم و بیدار می‌شویم، بدن به این الگو عادت می‌کند و مغز می‌تواند پیش از زمان معمول بیداری، بدن را برای بیدار شدن آماده کند؛ به همین دلیل گاهی بدون زنگ ساعت، تقریباً در همان ساعت همیشگی از خواب بیدار می‌شویم.
🔹
این ساعت داخلی با تغییر برنامه خواب یا سفر به مناطق زمانی مختلف می‌تواند دچار اختلال شود و نتیجه آن خستگی، بی‌خوابی یا خواب‌آلودگی در زمان نامناسب باشد. شناخت سازوکار ساعت زیستی می‌تواند به درک بهتر و درمان اختلالات خواب کمک کند.
متن کامل گزارش را
اینجا
بخوانید.
@FarsnaTech</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/455720" target="_blank">📅 18:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455719">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eboSpMHJMW9xz-tEZRItFoflVF1lpN7hgpmjpauRKG9i4V_aHo-2jp9HPCWXE5vx2hcqY6FnYjdeUbk5dcLq3nQFJkMGW7PcYho1gBpaAhFfoFhwnJ_RTWShdzGkjWSPCLxAh9VC87eeAK9sFN1XUP3IMedWqcTywGG37a8lc6KtheRgBs-awS90glwjdPs2dQ4bXdq-B2R5t-4YbEKWF81tx4d3phEqZrgKjATIgB7RELinHxEFrIxCzN-d7MVAREfDoOTqzPH9OsdI6XXQAWNPgfsQy1YMBNC8IBxXx4EmtnOugxfRHXwLb_7O5yU4sb-XaePV1pLfGkRTcfesJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دالیچ سرمربی جدید امارات
⚽️
زلاتکو دالیچ سرمربی کرواسی در جام‌جهانی ۲۰۲۶ که سابقۀ نایب‌قهرمانی جهان با این تیم را هم دارد، به‌عنوان سرمربی جدید تیم ملی امارات انتخاب شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/455719" target="_blank">📅 18:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455718">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a7eedd60c.mp4?token=Q_J62PpW2Z7K9f1MxLMlG51B5PhMdkKov_54L5XfPR9_zCPTsDkwC9Ax7Lb1tVMXP_u1ulzXnvx3e9csFT9RtJit2wQnIRdCUulykALLCO76EWr7jJm1-bCs-Iy1W53sahx4l_abN_YY1mdCcIk6ejbAwdhN8IllTfTeXKyYTOrHNYCSzGiSb20L2qbOiy0Z59wBSrnYQ5yM_3srImawSUe2ySr1Twf70j3XnRafA_s0TnyLkhT0wfUUZdPMxPmCMZbuWcNxps6iD3TqnwCN_acM3swAIGUzT-1ktcvh45h9CpJpnbcRK3WXoOJHj1MGEJTeaYwGBDdlbYiTnE0PDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a7eedd60c.mp4?token=Q_J62PpW2Z7K9f1MxLMlG51B5PhMdkKov_54L5XfPR9_zCPTsDkwC9Ax7Lb1tVMXP_u1ulzXnvx3e9csFT9RtJit2wQnIRdCUulykALLCO76EWr7jJm1-bCs-Iy1W53sahx4l_abN_YY1mdCcIk6ejbAwdhN8IllTfTeXKyYTOrHNYCSzGiSb20L2qbOiy0Z59wBSrnYQ5yM_3srImawSUe2ySr1Twf70j3XnRafA_s0TnyLkhT0wfUUZdPMxPmCMZbuWcNxps6iD3TqnwCN_acM3swAIGUzT-1ktcvh45h9CpJpnbcRK3WXoOJHj1MGEJTeaYwGBDdlbYiTnE0PDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش شدید تابستانی مردم کهورستان هزمزگان را غافلگیر کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/455718" target="_blank">📅 18:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455717">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">احتمال کاهش کارکنان سفارت آمریکا در منطقه
🔹
سی‌ان‌ان گزارش داده که با تداوم درگیری‌ها در کشورهای منطقه، واشنگتن قصد دارد تعداد کارکنان سفارتخانه‌های خود را در منطقه کاهش دهد.
@Farsna</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/455717" target="_blank">📅 18:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455710">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJxonTHoM7hyImq64fsWCcYOiw6hiprt6g44QdPKHVJGzXo0NDMiJI1jeM1XQtkNsAHX_AUGd3pqWim2ybjeYHtkKEfVt1KJPQGvLuBtxpVPF9BGcNucgg9M9TeI9RdKzXsgkUpQ-nPNIGVkUTEce-kfCITS7fXyPxcCaR2FExholK8nrLmYFJz9LbxEB9qJ2E74CUGlV3bHT63kfY32FDQpzXuP672PJO0N5uAp03-YB8bdOW-v-bXsw1chnKUNn7_jdZr_0YpH7yMKTeaCZEVRhHkPaq2JxNOeeJfTGqgAjvZQa7BnwPHsEUed5hVZoDLG7BCaJSqAUwHNsp_gIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EZ4UW5fy5-XVMFj_xDEB7PRL0aDEhJUjGGOvCQX3UzU_HmKol6fmH7i4FErH-eANd-Pd2kOISpjSaSHLcxy_P5XQOQfqLascU1UsOJX6CkAZwvb2vajz3qXDZI1OKQpacZgv305Uf0sF0AtbeIdrFoZF9PgG9bLWCbWlNFivCLRNg2QK7J4_He_p5_k7M1HLGm4hII8OI0BmogFtjq2WJe1cJgr9N3v6Ltycr7_KPv-yh6Qq0kj5XCnMJHRju5OBxoRNDofxV4KEKfDu9aJPCilhBtQ4a7dWSzhHjoUzbCRxlJhjTY1CuCrMN93PvEMoAVIumB9HDzZ_eLU6_dNmSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDO0cTxrCtm8fEycNUAuKG0PHgpwmlUHKB1R-KWJcx6x13iMkdtPSP91KgKrrC3H_sk9VDaJ7vPMEE3nJ3twBUsoqACMOk817zpwl3rl9SPSzIzaZ3RCeHP5EhiaZTEwVwUw-_IrirlW5Rf0dEnk86EFsw1NIPBIKwUksf2M2092GerzQi3IE48k4eDX0tYcMe-E6L2Gzkj3QGjPP6uvIoYznj7gFVODYC2yDLNBe7sZIz0MAAvW61tIjMZjUWr4hkt74Njp8mnLfrWnVxywa4yXb5OSorUDKCSRzQo00h5SyLpIwUbgCkWvaQ_HO7ubV1F2pS_AhCnhO5QZf0rCSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j-49tcMJHB0aiiFB1IJ8PJfCAC1f3R08gRbHXZiw1hlwMDFbXlyxj6d2H8X5OiWEH-6fEJAEiQBJQQr0opXYoNqcbdknrDVDk4n-GrvSnrEZSjPkaq1z06AuaQfYpKvYWzTO5WAXdpGpEweaUiskxOpnSBMnp64yOnTdZofkU4Hreru3tf0-infZ7maKlOIJtqJmMHiqHrxQjEH5V0JA8r_GtOMAFT8cMa8ynUQdR540-YVRHndVPJ-kfSH_DTlmebZFn3s3XRfzQPifMmpajpeIG9PkzCKwD4YUZuYfGlNExgiZZiixhzYbcFs8SCC3KqF7a9iByyHE6jyRQ1U5FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v75ZKMmikUrGYk3ouGiPk6du9j_QAG_Sumi5VbBlwWsMk6fX2ioSjOZHp3SZYlFeJAgWUjfKIl_g2RzE-3WEtuOeJJ5nQlkBuczB9jq8s8Qy0l7WJX6nHweTunG4KQMYzbPv8d28xEut27qLCaNG2L04POniyY2-qWq6w9wQ-FtoFsul_F-ZEhvfmacUpyf3KwH-Siqv3IRTJsxGJYErZdpG98ba9Kp89-VA_VzYYVeI-FK0a4r6Z-k4auYeaapJtiA8rfbAtZdASrZR6A1UObi_XhZlZk0nIy_-417MQeH263LZVnGk9VpiRxOOBrjFOeGzyU-5l0eqfunjKjxJNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hXa0tLAMTz-Q0dh3aWGCfGK1GL-0Rr6Vu8khhQ3OffOiknEctxtN9MnRl6RdEtP2DGLfOJdL-OMXj_pDV6j4HUWl80r92aaWsODuwVN0DiBXd0GAAc3Gkpgf7yV8cKDzCnzPGcKxN5Q8GVHkQPxdX0LqmfYjyarp7pI_XzLW7N6-LutBl2sulnTPrH1HdoM-yZf-5gR-l8BNm8xyc_wHxcx4dH-1L3nL60SVKNQlohZ6fReRPsvJppYugxwFPa2bhjfSvSVWUyqaLauRzR3yiY3DrfUcXowNALzas40vTWVjQ6jbF00aB51-EkJOlm5HakPuecEe-2jRTmbWeMQBwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bZDpq2qs75sk8UWtKoSBv08NBdlwqBN1tG_h8v9aUct5_SbZdwemZpkiAUUihtPJJ2B2_orYJnOkF1RyBZqLkdjpJQVCl3MKSgWnxQcT7Wze3WutzvwjvF_pUsmRIhrDkyWMnEodlSBA2PvKu7yhWwbwC_UyQzO_82qKdHsETIKWh-kvTnXyAGF4m7sI4dcNEe0VaKPaH_i8tTKwdr4T1QPTyVSbiSVuLdalXkPydvBxM5fDwPy4Y_DlDDaAmventifxR3I640RXRBZRyYTzHq4Dv-ildsCuuJLa5oSZUru3PcAQe4oj5IV0KYrqWl0dr6eKLlh1jsyqRd0Q-qZPBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جاده‌های مشهدالرضا میزبان زائران پیاده
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/455710" target="_blank">📅 17:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455708">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZxsUa9AsCiEQ2wsURU7dBIdd2W8CvJxb26WU4mRhBn5coWHzHgIxG905Bg9X-s9jwTLmmhuuGuuOTGzp6lGXaRixPwiqNUkucrj_DCQIdAM5Aw3OjjbXmUnwPSYrs1SRzxv1t2tgBGIX4rSMlyfT4H02rUoeeR-CgiaU37vc0R0oMUZiyw37YWQU3Qjg2uWENyRnfkV4lhX96j2R1oSNPGSHDohOnRCgy6Fs21NJeuyj2wE66Jh9tqD_BIqfBXpkyHMOEETUE-VyTpMIBuTTc7L5EMESSIBmGSvYwnW2xK__xpWHeEKRqm1B0B9D7pFlc-kQL_bMV_w0v82lXuDpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EQe2f2ZgTYhfhmL0AG5fPUeZyY4Mj1l8MgPgdYH2rEmcMAPd6RvppLfAvYVUyo0nxhfw9JAjCW-BM_FrI76WkF0ekYSbZztU1FCUZLe3nE2mcWVaMYKZQ_MDGwH2AjRh6MdlynYNVvCJtj5vhF2xxz56OYnaaqiPiJQKNe1iHfhrWiY_IZ4KEiG-B-d7luDPCk3Q77V85dWmOGtRBShIC43zPoyRxbOhmL6EoTMFREARnaFV6EoafG57aAAGFBNOVs6HshmSYunOu-WC1-jIb63X6nT0Fh1YNNSGG623OBURqkHwc9Ob7mMObNiLsCiWITHqLA6XmYqv27ozcizmDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار طائب و پزشکیان
🔹
نشست اعضای هیئت اندیشه‌ورز بسیج جامعه پزشکی امروز باحضور رئیس‌جمهور، وزیر بهداشت و رئیس سازمان بسیج برگزار شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/455708" target="_blank">📅 17:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455707">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/481c7f3175.mp4?token=Qjzf1ArG44oCKo6e4RPyVTLGfPKkDLsrZ36yjdC2Xf0bMIb_P4Mv-IZ_tQx9eryP5DiG5zn7WwC9tBhNemVAnKDkcPWfo1TTdMOr-zRlgDAEhr84ILKUTtMFtJtqQaKp7ilTUc_nrNJr_HOtRUPoZK2XesuGhhMs63iPUmr1lwW_7DcwcYpjDS-6pjGR3LjoIJk4Z0hg4EafgEXklGWkcAHIFTk71g4DmBE12o3DEWx5cpYIhuNbDoa392sNfXxGO5gi8mSj2cI2Mff83PxC530BUp-L_ZuibBLF6yWk-Q1J3MGc9T_Be1adubmQtAjLQVoGK8Gqj2QLi1fWsX6MCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/481c7f3175.mp4?token=Qjzf1ArG44oCKo6e4RPyVTLGfPKkDLsrZ36yjdC2Xf0bMIb_P4Mv-IZ_tQx9eryP5DiG5zn7WwC9tBhNemVAnKDkcPWfo1TTdMOr-zRlgDAEhr84ILKUTtMFtJtqQaKp7ilTUc_nrNJr_HOtRUPoZK2XesuGhhMs63iPUmr1lwW_7DcwcYpjDS-6pjGR3LjoIJk4Z0hg4EafgEXklGWkcAHIFTk71g4DmBE12o3DEWx5cpYIhuNbDoa392sNfXxGO5gi8mSj2cI2Mff83PxC530BUp-L_ZuibBLF6yWk-Q1J3MGc9T_Be1adubmQtAjLQVoGK8Gqj2QLi1fWsX6MCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فوران آب پس از شکستگی خط‌ انتقال آب به بجنورد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/455707" target="_blank">📅 17:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455706">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8783e567d1.mp4?token=D1ublcitVQTgw30rC-287zhXOx6wQvCq35lIoHINfdmKz85uvpTauLo_av4JexvrKeQFot_h5OxIpXtOcyzCxvXnVbm4ZHXnc_vrRJc2tFoQYTrQAcEQPCh9_PXR3nUP0wAG1SCYrvlZXHhtsvAGADuIBNOD56useEuV6KIKFKWjwpp6ebF055soEdfTwVDSJMl77xsjLlmnJqRd0Cht6RoWrBZKL1ZVcOB5jM_e-Wo40mGMTyEjcmYhSX8_V4wbpXxMZ62hLcif1Mrl3g2DVM7GOQeDcGPgAJezBdPsOs2E-rvg1FH77T541gcm08jmnrx6lBF-52DPCgAcu8kShA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8783e567d1.mp4?token=D1ublcitVQTgw30rC-287zhXOx6wQvCq35lIoHINfdmKz85uvpTauLo_av4JexvrKeQFot_h5OxIpXtOcyzCxvXnVbm4ZHXnc_vrRJc2tFoQYTrQAcEQPCh9_PXR3nUP0wAG1SCYrvlZXHhtsvAGADuIBNOD56useEuV6KIKFKWjwpp6ebF055soEdfTwVDSJMl77xsjLlmnJqRd0Cht6RoWrBZKL1ZVcOB5jM_e-Wo40mGMTyEjcmYhSX8_V4wbpXxMZ62hLcif1Mrl3g2DVM7GOQeDcGPgAJezBdPsOs2E-rvg1FH77T541gcm08jmnrx6lBF-52DPCgAcu8kShA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اصفهانی‌ها در قافله عزاداری ۲۸ صفر پرچم خونخواهی برافراشتند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/455706" target="_blank">📅 17:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455705">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a8ee27a23.mp4?token=LGvrZxYHuXqTKQCvNOo6gO19sPUUdxB9tbYj4jE4HWkunn3vs9Uc0PqvFzaTezaZsoDPXvbIIfqtvwWLNfERDmzVEiPFFh9uWT7T6xuxFEEWvUVy_mcw7Hz3k_Uatv_U7o0A6ayAJeYemV-n-NtsTWHs3uSF8I84C2WBUOs0YMCh33BKqx_Cnz1Wk5Ei1dK5T8pCgTU0OuxTsgWhjcmXF2uI8jiNaTqt_P42VH2ysB-k108JseXZRFE3wQW7eaP4nk74C67jhRTtWPtwFfvk6IpBA9Q-0LKW_J9daQSDW4pWpxDqoolXK993_D-Ln9bKn1xiHPe_jo4z9tJVTLf9Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a8ee27a23.mp4?token=LGvrZxYHuXqTKQCvNOo6gO19sPUUdxB9tbYj4jE4HWkunn3vs9Uc0PqvFzaTezaZsoDPXvbIIfqtvwWLNfERDmzVEiPFFh9uWT7T6xuxFEEWvUVy_mcw7Hz3k_Uatv_U7o0A6ayAJeYemV-n-NtsTWHs3uSF8I84C2WBUOs0YMCh33BKqx_Cnz1Wk5Ei1dK5T8pCgTU0OuxTsgWhjcmXF2uI8jiNaTqt_P42VH2ysB-k108JseXZRFE3wQW7eaP4nk74C67jhRTtWPtwFfvk6IpBA9Q-0LKW_J9daQSDW4pWpxDqoolXK993_D-Ln9bKn1xiHPe_jo4z9tJVTLf9Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مرگ بر آمریکا و مرگ بر اسرائیل در رواق دارالذکر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/455705" target="_blank">📅 16:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455704">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کشف ۱۲۰ دستگاه ماینر قاچاق در بندرلنگه
🔹
پلیس امنیت اقتصادی استان هرمزگان از کشف یک محموله دستگاه ماینر استخراج رمز ارز دیجیتال قاچاق ز یک لنج باری در گمرک غرب استان خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/455704" target="_blank">📅 16:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455703">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CC1GxH4vF2FEUCEl7OtoAGrTAYItfHmJZ9ACp03SnKsUQtNEaJDpheT6M1wMXUUbVH0NkBaH0MvQNKbIGpaTJsHjXeFgOHQmf5fNz3LZ3v7nN-O2lek_pPSpFzTfQk9qAS3AZDzSpclltUi6CZwzrNepv9lt6DgpgSlPzw87VH_Q6m-627sJHroY7IQhBcg7GeosfMQhIftnXWG39c2_JDq5sBm0La2HNuMlqG1J-sAbKY4Cwqjg0ZMe1knJcU6L1oTx3gtwOUOJ8MA7rEOkhA7gQuF_23qg5HOYJIzrJGll_zEzcTeAXnRZ33c7bWx_9Zfl8tcfUKF1OmTSjyWG0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی: ایران و پاکستان عقبۀ راهبردی یکدیگرند
🔹
سرلشکر محسن رضایی در دیدار با وزیر کشور پاکستان: ما دولت، ارتش و ملت پاکستان را از سرمایه‌های بزرگ جهان اسلام می‌دانیم و خرسندیم که در تحولات منطقه‌ای، بیش از گذشته شاهد مشارکت و تحرکات نخست‌وزیر و فرمانده ارتش پاکستان هستیم.
🔹
از ابتدای انقلاب اسلامی تاکنون، همه رهبران جمهوری اسلامی ایران، از حضرت امام خمینی(ره) و مقام معظم رهبری شهید و رهبر فعلی، پاکستان را عقبه راهبردی ایران و ایران را عقبه راهبردی پاکستان قلمداد کرده‌اند.
🔹
علاقه میان دو کشور، علاقه‌ای حقیقی و اعتقادی است. روابط و علاقه میان رهبران، دولت‌ها و فرماندهان نظامی ایران و پاکستان، سرمایه بزرگی برای انجام کارهای بزرگ در منطقه و در جهت پیشرفت و تعالی دو کشور به شمار می‌رود.
🔹
حوادثی که در پاکستان رخ می‌دهد، موجب نگرانی ملت ایران می‌شود و در جریان جنگ علیه ایران نیز مردم پاکستان به‌شدت از ایران طرفداری کردند. این سرمایه بزرگی است و ما باید با همکاری یکدیگر هرچه بیشتر از این سرمایه در جهت پیشرفت دو کشور و تقویت همکاری‌های مشترک استفاده کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/455703" target="_blank">📅 16:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455702">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f7fe62ca8.mp4?token=qWWg3fx9s_TxQqqv-uRh_nCzk2UQtb_AfhB6MdOeLtavVO8qLvIPNP5sUl-ln_2YFnGL-i7AsGsUDvVqplF0XPecZmiDs-og4ybW5MbNT-UTg6qnZABdfnjJEa2qzPj50u8z9iU_YpFEa_WJSLmx8RQlENXOv92rGP5bslUjVkviTtfxXYCx1BXK6YGYi1mLuTfM__r0XMiSCBNCaU6GUeiZ2FBTvacg08smaogL8aYIwSaYiYrsJq3fFKLuE61id_426Y-hlqGSJW6A8v_lufP-DdxqnpfRO0QsknV52t8-5Mc9BaMC9lyqEtJpDkhLaXHh-TQLODI2KdAY04U69Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f7fe62ca8.mp4?token=qWWg3fx9s_TxQqqv-uRh_nCzk2UQtb_AfhB6MdOeLtavVO8qLvIPNP5sUl-ln_2YFnGL-i7AsGsUDvVqplF0XPecZmiDs-og4ybW5MbNT-UTg6qnZABdfnjJEa2qzPj50u8z9iU_YpFEa_WJSLmx8RQlENXOv92rGP5bslUjVkviTtfxXYCx1BXK6YGYi1mLuTfM__r0XMiSCBNCaU6GUeiZ2FBTvacg08smaogL8aYIwSaYiYrsJq3fFKLuE61id_426Y-hlqGSJW6A8v_lufP-DdxqnpfRO0QsknV52t8-5Mc9BaMC9lyqEtJpDkhLaXHh-TQLODI2KdAY04U69Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط جنگنده F-16 نیروی هوایی ترکیه
🔹
این سانحه در جریان یک پرواز آموزشی در استان یالووا در شمال‌غرب این کشور رخ داد.
🔹
طبق گزارش‌ها، خلبان این جنگنده جان سالم به در برده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/455702" target="_blank">📅 16:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455701">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9230adbb4a.mp4?token=JBTAMkdte2O6w3eEN9ooXmTePkQPFjXsrJhEWPKwZ2EVYFCKDAhJRpvF33D4PnD9DI41MhGqHMQ4FxQN3R_k5ETD1BNbuPCcqPBAJZOFqBz1Hfm-915noxVuXNSEhEQS4r19ay8Ki2gaHHnyonjTiqoY5-Pz7RR7EB8fHASvL-CGS1diTAg_MWf5DkNQXXpxMC-kS3KQN1tDt_7v_iD4aQk0ldZCNrlLfZv3A4aVwAPvH1ztjqBNJriWx7XhuSnt8YUWYBbQ7dJq4BlN8aygkEwnS2wiv0yLZO42-qoQSFnPdmztcjMyE4VSCNWgN6pJxA0TZ8dqJzjUttGKho1C9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9230adbb4a.mp4?token=JBTAMkdte2O6w3eEN9ooXmTePkQPFjXsrJhEWPKwZ2EVYFCKDAhJRpvF33D4PnD9DI41MhGqHMQ4FxQN3R_k5ETD1BNbuPCcqPBAJZOFqBz1Hfm-915noxVuXNSEhEQS4r19ay8Ki2gaHHnyonjTiqoY5-Pz7RR7EB8fHASvL-CGS1diTAg_MWf5DkNQXXpxMC-kS3KQN1tDt_7v_iD4aQk0ldZCNrlLfZv3A4aVwAPvH1ztjqBNJriWx7XhuSnt8YUWYBbQ7dJq4BlN8aygkEwnS2wiv0yLZO42-qoQSFnPdmztcjMyE4VSCNWgN6pJxA0TZ8dqJzjUttGKho1C9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جاری‌ شدن سیلاب در آبشار سوری شهر مجن استان سمنان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/455701" target="_blank">📅 16:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455699">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n4ZxsCf5AVLAq930HKYtakjvEWyXCyS0ampovJELUqTgnK_CiE_cnuKweQGvHGhGERiY5bqfSFe7tOLl2zbxhm3Cw8vHI_4-QIMjTGmmBvstRBaSnRezn4I0w60_U3AwkzSKAtDZBCzy7eypj0r7jZTUMFLdhxIy5wPVDcxklQ9_5-nNkbGIr_mcyGNjneFFS5dWJ1G6wWzaPvs_nzX3Yi7UjErSihwFS9cKFc5q5LzEpCH1pnhVEAsLBDUDK0h03nPSV3cf0-yl7FndDOBmqF3hXwXRD-nChvjHDLyBwS-lGf73Ir6GRHEE2LtHyBBo7h_IYoXSNX4rRY-SU0Yo4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wh5nZEBurgJBwNADEKGLlMFuhUcS_PlLjfZ_tYMiNZhlSYHkj9oi7hL7AaMAIuRHc6w69tCrQ_T6XiRTzuWyedU_UrJAo0M3v-4ApSoV7bCDwrXHj7qQpX-8WPlDFZ2g0kvqSd9OSJ4nKNvehuJeBtRK4NCKnecbeMUSEgpGlDhwRRTC6cnXi1FS0bWSVv1XjWN-h0q1P79k_edbwrlYF8SWz79CDaZeNQ_KhzK1A_WvW7LulEFXW4IGx2x8rks8aQlCg9FE02fKbtiwmi6NcOFuVJKVmoiI-wCVGP3YYl5HKdN230ZTIHHxHOo6fkKof4jBtXMrExHQOwccJVV5LA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر وزیر کشور پاکستان به مشهد
🔹
سیدمحسن نقوی، وزیر کشور پاکستان با استقبال علی‌اکبر پورجمشیدیان قائم‌مقام وزیر کشور به مشهد سفر کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/455699" target="_blank">📅 16:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455698">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBDbxbUeVWz0htwlcOkMrspuEnpfHiFxU05iRNGjJx1ETioVkQaub3ZOFemx3CWfg2TWapq28INCUVpG9zi7h2I8BYSc1Uol34HLzc2zBZ2Bb9NQa8jqOK6ZBEBzcvyTeRQkOyjvreRN06dM7ueySzH9D4U5ej49OnLB2DOOjqJoFPTlgsOI4kdn9tdpw3TzaOAhVzTgQP_I1PW7EOMnV5CLhi-guCGuIBwmnsvqYHuWpE8WovN-tHSPK8a8DOLDOPm6EymATtzz10g3YJBCJZAQXleHLmBwiyI8pW1vjbNypWT1WDbnJ1Zs2jlTo3wzjg5nvauVyNN8hDuxm7vvJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایرج خواجه امیری درگذشت
🔹
حسین خواجه‌امیری، خواننده پرآوازه موسیقی ایران که با نام هنری ایرج شناخته می‌شد، امروز چهارشنبه ۲۱ مرداد در سن ۹۴ سالگی دار فانی را وداع گفت‌.
🔹
این خواننده صاحب سبک که طی روزهای اخیر در بستر بیماری بود، در طول سال‌ها فعالیت هنری خود در عرصه موسیقی بیش از پانزده آلبوم منتشر کرد که از جمله می‌توان به: نیاز، پرنده، بزم عاشقان، قصه زندگی و... اشاره کرد.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/455698" target="_blank">📅 16:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455697">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5921e2d406.mp4?token=NdRtZFRsi4aZNfeulBC7c1V502NPnl4CR1o2WO_xtPlzmEpgfLV1QhD4iLcfIu6CFGvKzQA6Yq3jIdytSf-YBK-DK0880r-_UJebDaRWE5Ts-vGRtyn6FiFBNwXPuHVb3v-7lnndA9bO8fIQU-VAKXfcmwtKfjcS-tKD8sr03pvt4oRvZdaJEGC3DX99PUq5UylzAiPZ6LATpxCTPfZ8I8i0s8Yj5adwRuTRsL9okgN8dWLz5wJdfr-NnUIbTESlk_5Ilw_ywNXxw7UWsOOi2XT_wuUbL0mkUO3KPLVx_E98EuAZ2BtmPd8xD6_a7McBKITB6nEhvKEB4qlf7FmX1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5921e2d406.mp4?token=NdRtZFRsi4aZNfeulBC7c1V502NPnl4CR1o2WO_xtPlzmEpgfLV1QhD4iLcfIu6CFGvKzQA6Yq3jIdytSf-YBK-DK0880r-_UJebDaRWE5Ts-vGRtyn6FiFBNwXPuHVb3v-7lnndA9bO8fIQU-VAKXfcmwtKfjcS-tKD8sr03pvt4oRvZdaJEGC3DX99PUq5UylzAiPZ6LATpxCTPfZ8I8i0s8Yj5adwRuTRsL9okgN8dWLz5wJdfr-NnUIbTESlk_5Ilw_ywNXxw7UWsOOi2XT_wuUbL0mkUO3KPLVx_E98EuAZ2BtmPd8xD6_a7McBKITB6nEhvKEB4qlf7FmX1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کنوانسیون کاسپین چرا خطرناک است؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/455697" target="_blank">📅 16:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455696">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BK2FsKtOkX64yViSb6qSQCEAbSoZNcSq7aztjFlKazg0tf5akeF0-S9RTXqcfaVgmmQYpO1HWpvoF-RcVEfWofr--4BzNUrMstvG1FHxSQ2vuYgqbKMNy_WeQudhIavXCOyK93uU-5Wl_HaYWIRMHdejqxjBftyFfPqi9-uWnJDZnmPfkNK7YP5qiB7VuiaMvtqRM7M5ddDTNvWT_k0CxIwGgOXWj4wQBghxu6I0NYFbayjkTTigcTYjE66A3Q9IiEWJPozLM2dcXjNoOEG53McaDC57gmZFW-9x1Y5lL3nlkd4agWYrEfjB7pneP12LhSTYvw5WeaQ4S8g8saI4kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وندی شرمن: کنترل ایران بر تنگه هرمز ممکن است همیشگی شود
🔹
به‌رغم ادعاهای ترامپ مبنی بر کنترل آمریکا بر تنگه هرمز، معاون پیشین وزارت خارجه آمریکا گفت که ایران در آینده قابل پیش‌بینی و شاید حتی برای همیشه کنترل تنگه هرمز را در دست خواهد داشت.
🔹
او همچنین در اشاره به روی آوردن دولت ترامپ به تشدید فشار اقتصادی بر ایران بعد از ناامیدی از گزینه نظامی، تسلیم مقامات ایران در مقابل فشارهای اقتصادی بیشتر آمریکا را بعید خواند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/455696" target="_blank">📅 16:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455689">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HD66yN_ol2W95sqfkjQwEQQbsnFurrWYq11JB-APpk2sIINosVp_9kdx8NlGfaMp3LfYXjuDKdcKqPfvkpL53ZzumbfwvD4r-9SmxlmoFGYM1QUzXqoGzmrul0819bAZ3JDwPHf1rLoP3d1t-m6Kl5Nxzlf0vX4hvs7YsfmyJpgEhw0W6xnPnzYHS4jHLoaHAOgXLLswehv0chy60dV-KU79b1UJMswykVSOyd_QR9aIeF5FsMWpb7gCjf6bdJjqi3WBNRv0BPOnho3u7CJu0cn5oMkn7-7FJU0hub_jWZekOCr7_hFX8TeExPSvLxGbY-qNW_4MLb-liw8WvPUHyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bU-aLKM9wSsFQHVZXfKJlhJo5kZMxHqEqHVBgByZmF9GlyJ-4bgJAzfuTEM3QWuv4vTo1B-ZzsL-pC-m6iBjM-_1PtPeayz40qPgJDiG67Pe5QLL5geAoz9faus3D-3LTDRe2Gpl9X_OATJSOdCXlH4NGSaIZJ-GmX47fxKQ0vTGhpc1YmnDpYzS2AL8V0w3j-xU8q7OTCEbRQMs4TASj2q1x1ZXi1b595f73YuSwfe2Bbc58tNfmX33yxEeyipjkYJnWfPvQ0s-vUfaa4UHYSvpKcBEnqUyxjx4KuLhZTwsBb7dXphG0W-GCCN95KGsGfLNIwDpcbLLVCMMmi-Wqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HDTf3EtIQy9sNB6C9ZfHrJEzjuBtoRnF19FLu8LgjqX_ORYNCtJKFBHd14FZYBwfofJJDVx8av4O8ag_37H14ML8T2H8-oflJY5eI-GxvQWbwWbNTdyUWRWpEjL8C4fEDcr1h2JzM3GjVuuf9O3l0N9bEy_eVm5sxFhvdFxOfngvClRXLkXrpg9_VfiYuBlCMixEe-dPRcV4YNryNTbB7qStMPQpQ0_IY5G5LQ7tAtNUitygN4Imj865k7TkKqEscxHYlVHw5UEnymNBxQEXnSTYCdQ8YACXgDecfWXsM51MVGr4TioukjE1teCSauwvszdk1gMFTk55UBjHnQr3eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MSg5-pTqBewdmgTxk5jIJhXc94S278Qfem7ujxwiFDsCTvc5gGB0JqCTphkGko6dK-6yLNm0GbOjUDtDn2bfd8L3iDbHDvXu1lu3PDy6mNGqYyAYiGi9AzBLBzZmqFF7SEozOQUL0bYUrxg4C9tHPpf_M1-u8Sronf2fXfacRwvE8j2-_AJGUD60M-j3eOLSmhV0AwPAHhf8BmmPfM-n23WKZTwyP3a860c5ixQjqN7jtQ-o2aOkYQXUsTLeySjkBso5RRuuIv-Zn9Oq4WX6oHdVcNAKqKiXayd5Oto8AAZV1iPfe2CVURZuO4GU8xFMLWC7TW6uwn5J_Tahud4ttQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8iixtKaHFgzwVIvoAYrs4IqLMqIm6K3TB_Y8DcuD4EMNo8xB21hdNNVy4OO1RDMmd667CalEp5Kw0RUaZeINLfb53iiiMoRlUZXzIp8Bn3wfYSrUBZRauVWoJXLuhmi-6Ab9QNEK8i0EaCMan6BhMDoZyH5ljt6csC2YtHltY6SY6dVpGiPlVjtlh9S9jkUdMAEOauRzdczGuKMz2DzZnG-KwFaDhLIPLqmyeJn4WNBlK7Y68X0rbny3WJMuUE32dDcoBPmmrAnImmIZqxjzpuOejnU6JSQisYie-BcffeMYUhBT1hlml897Yg7c915UMOWebhiV2TGu4kORvtczA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tLoNqZ7vMw46jJXbTSH4mlwYmUcFNcfnkXeI1FE13-vANej4u3esZ2Rhbkty5DmPUwY0HeLl0k4ccm0Mg5QHnDws_6m5Eh7930wUQVLmzoQJIl0Eww2hLEgPBW4z6XSngIxP8V2PBtYZL53nd1xru3P3baDfalus63H07Nc_HYYwvQb4a_spW-ckH7nk8vJPunW84rh42L0zJ0Df5BzLfiSO0KbrhOkbj2GkgzO0XQDGpmFhfARdg5ovEJXLlrFDuYoSnndJBHKVBEatQB8Uo2QG-ZP3K_VzMsh18Q6Sa9UuVMOiU92EA-lJYtWpVduG8tB6-1nSirwkyI95HXWEyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sHZfa_UvrvVi2goCPcSHb860K5_miQGVoUFiFmCeI-kRQBKwf_3eCSOZ2-QLXOHXmBBA1qJLARPqpWCqF08Ne_rC80TV-UUqjUH2-smUZdtKF511HOmUlRBOXMg31nae316wKP_y0hizDKowizc_lw-3BCw1XF1ODCWxS7UeypD2fLXyS5f3XVyP1Xs9eDfJmsC7hiEajJy0rq5J5zO25SvEvSKf2hNbEYDhFoRh5GfQCVSusZJ_L4aoeJRBeN2vQNWeenTI0ETsCT6R_P_ffpVdojrjlIxGXSqG4T-x7vbVw_JlSmSLSCNHWG0oAPYin_Fw6B0p7jLXlp1tnEy_wQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری سنتی یزدی ها در مسجد گوهرشاد حرم رضوی
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/455689" target="_blank">📅 15:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455688">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">شرور قمه‌کش تهرانی دستگیر شد
🔹
شروری که با قمه‌کشی، ضرب‌وشتم شهروندان و عربده‌کشی در خیابان‌های تهران اقدام به ایجاد رعب و وحشت می‌کرد و تصاویر اقداماتش را در فضای مجازی منتشر می‌کرد، دستگیر شده و در اختیار مرجع قضایی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/455688" target="_blank">📅 15:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455687">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGDPgFEuLzS4V3G0A6kioan7eKaddq2sroo9zJFY8_H488XFMheSRR3dPDxTDy9G5Tfp6AwjtJWPpmTNp1Hk021iqA9R3LDINSPtHHtRpoQ40nMT5HAehRt-BUfH02LfOKyGlwEMHQ1LfTywS9REDs_5petrjpvkZLo9VbfYJMVK18StZfXOBHu8zONTxQtdgLqB2b9ZzJ5OzK7jKpj2UdIah7aGcGkvICa_F70BJr1kZo2j_j575Spod89kMlaCa6-PHQa5jEMVjZ0w2sMEc5ju6lcRHTnS3IkHnUUn7Lpu6_a3xVjWsMvbl-rX9wftYVSmlN1HnD_CozD7ZfVpTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رقم قرارداد تارتار با پرسپولیس مشخص شد
🔹
درحالی‌که طی روزهای اخیر شایعات مختلفی درباره رقم قرارداد مهدی تارتار با باشگاه پرسپولیس مطرح شده، پیگیری‌ها و شنیده‌های خبرنگار فارس از برخی مسئولان این باشگاه نشان می‌دهد قرارداد این سرمربی با سرخ‌پوشان حدود ۶۵ میلیارد تومان است.
🔸
قرارداد تارتار با پرسپولیس یک‌ساله است و این مربی برای فصل پیش‌رو هدایت سرخ‌پوشان را برعهده خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/455687" target="_blank">📅 15:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455686">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7290b786c9.mp4?token=W1_SMId7yULT10myS9KL3kceH4DixeXjfNyKV-Tkl6Zz3u26MStZw1WpAa0wPpLIWycmdwY2n-lcSz6XzomaEVXkw3RQpPkKEBDVgHyKnfa9Bhlc8Fj6xd10EhWxTiqNIp-WJk6bRASK3wZoIRkZJGyWKIqPcnHT0dx0GfUdSxesB8jEk2rTEo69dVg-fvBuz3LgEyII37xD5R8FvPkcTp_SbmZVM0bq7wcijsiUjvGFliuMiyt76BY1V4olVzIj8Zl9cP9mE8i9fpsXAXdpef4QlD7HljkiyG6fBLNj1ieP_ABQg3NKI_7PsLqU0PWFIYZ6iZimmSpM1GMA0OZ06g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7290b786c9.mp4?token=W1_SMId7yULT10myS9KL3kceH4DixeXjfNyKV-Tkl6Zz3u26MStZw1WpAa0wPpLIWycmdwY2n-lcSz6XzomaEVXkw3RQpPkKEBDVgHyKnfa9Bhlc8Fj6xd10EhWxTiqNIp-WJk6bRASK3wZoIRkZJGyWKIqPcnHT0dx0GfUdSxesB8jEk2rTEo69dVg-fvBuz3LgEyII37xD5R8FvPkcTp_SbmZVM0bq7wcijsiUjvGFliuMiyt76BY1V4olVzIj8Zl9cP9mE8i9fpsXAXdpef4QlD7HljkiyG6fBLNj1ieP_ABQg3NKI_7PsLqU0PWFIYZ6iZimmSpM1GMA0OZ06g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای حرم حضرت معصومه(س) در روز شهادت امام حسن(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/455686" target="_blank">📅 15:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455685">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">احتمال شنیده شدن صدای انفجار در جاسک
🔹
فرمانداری شهرستان جاسک از احتمال شنیده‌شدن صدای انفجار در جاسک دراثر عملیات خنثی‌سازی مهمات دشمن خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/455685" target="_blank">📅 15:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455684">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxnKm9CcGWcZ8EGH-wump91B7SIl4k5SEgHesg-tUPoVbnCLNVRrwhb5__YWeg4FNwr2iUQw1YP997zC0wlOPQFZaksFZOpL0k_NqJ02K0A_swI0hP28B0Xh1kyMK11WRIhiKzGF7HY5K8x8xdQlWn4xVjHszZqcohgQOF3mfzP7kh8PkOHgv5dnjkS1aP21sAsiubX2Zgq6vhVYpQplYFz3kEg-iVCy660xl06L93VmE0BfAUu3xe5xyge6MYYuEXXQptdfHpSUy0lVu4UWsKqh0-ZTUMAG-faDDT70S0Mmt_23HiB0GAcGHXQqYZYeQDDCbSmBDLegn7eM3Rs0LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: دشمن به دنبال فروپاشی از داخل کشور است
🔹
جنگ کنونی پیچیده‌تر از گذشته است و دشمن به دنبال فروپاشی از داخل کشور است؛ بنابراین باید مأموریت‌محور و موضوع‌محور پیش رفت.
🔹
نباید مردم را از خود برانیم، زیرا آسیب خواهیم دید؛ برای همراه‌سازی نهادها با مردم باید از نگاه سیاسی و حزبی پرهیز کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/455684" target="_blank">📅 15:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455678">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NGvnISMjL--zrOFRUJhucuZgFn5AzAUZd_UXDz21yzepNgIMRlOyR09SuKIMYDgLLKRo95wN5P1duajPDRCSbDqcfXxfc0JmX20IVFAqw43Ele7Re3GJlgCk9tnZGqBt-GWjHIc1RIvpkH-fr19ns7srimrdo87whforfZTZgr8O5Q96lnItEZrxaanre3n-PLHCmUaT_tQIk_Px6hJ_ak-gviygCW54ZgU7rjPY7qq8VtrqtikRSGBMgt0RJhR4snW5TfARJ0uGglMZMTzR2ItTVdX72AQw3RPU4Gl8BHCvPuR0-ZgMwsnrHSyJb8H7wv-_gNkHQ7O7ufpN5xzPpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H2U8l2Cb_9VhJCnqOYX54EB_EV1hLgSo-rRmL-saBcSJ82rPU38PSvmWk1NbV-IUvv4HkCgqPYqo4wN__FX_XjcDK1wefJb99s4IrVGOmMK6p8w-LTuuiX7A7p2uCC7DkjJRk6eALfNv4cdoWk8b23vjB5j6ZQ0bgb_1C8kvbbIrOgX9iowZfrOrUyvhxcTJ7KtjVBVfNje1MxsujfaS2nZpXsR5foSjr-2UO3bQcwDl4exiVQyZJcfLwcMTwx82c7VnQeteETJNBmm2p7-H-a4uQTOo-o9v-WXRwM-6T4OGlfm6yljwQNNDbqtth2UnCejS66i9DcGi0gJyXXJBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cD2dnJRukc_SGCi6z51AjZGMJ-IxDykD64TKbSooPzEu3RaqkeepemFSxlnPvaSKIZJzFJvySoLUykvbPP2mO1OTHSYoEoe9q08J6anUMXA0_1jl9ueAfltIrKxH-H0hpFchebVrUa6GnflCpbRmLDgYV0kOdyN9Rcp0xUG3SZFCsuLOsIrYfhjh8RmtMHEOTVhMesjiSDWXj4_ildoKcXcwQ1u3tnUNi39WyO8Jf-PfBGnT44zz0XIIlIgJlQ3vbiiyi5eCvGbl3MF5FsdPxsoMmzOF7ITV4vEgmEXb81DYfcGrUUlTpCcft54Yepp14sdjrK9qtFtlFeiGdlhw7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VXGpK1aYvMdFoZ_p_c2PXrv0EWQcjnd0DfxOSGe-19iF1pRuaGM0ddx3KF96x55SI_eacAcAS6UTcnFDPNfAqeG_CcMokXQA9O--DfAk21sKnKkkNLCMk1VgAEXCwr2VHwHCUP6YqKTwt1KNPssGRUlBy-Mt_qLqU5gyq2D0-pMTdqdutOCHyGgiO4jRW9z8sQvUjYTAWgfzrsOBuZ3zuKhM7tRx9GtTgUhAQZQP6M_br2W5o49nZvRUDRwVL9pKHz6XB_qu9UoqPhbqygV9_jfAtHNb7YNu6HONecKloPDnFUDNnoAgJl4DGyNYvF7r4UVXOpY8CxcvSxYOOy21rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L5N-lz0b-rylBHBcnEyNjiRnIOiCrD7qpN5juYEFegSfJGYBc_AwLdfOWnYcsoudjZdQDSBjtgFsDCQQGkBUw52VwGPmuScI1r0RdMPhVerFgA1CYJ-SjgjSaWwbWQEXxLXaF0fX_HC0Is-uX2405TWEwY2Zr7TO3Zs52GX1sLW9QCM6SzCnR77Ve8h3l5rIY11tpJJNPuHyc9CVPHpvFRVeJbAEpo36L7RuP9QwCP3JCU9xA5swjBtf7IBW_ddnNZV8r0dt927C7hqFabMzLEgGPZ0Rj0Th6lqGBHpsZnG6GLvCJzcBhlJYC1Ae0JuPrPeBgbJso8NBD7nC4BP2mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BcS9CvwfRuhiEKGGXrhxeix-nWcC0xI8AHC4A626wnKFgOhEcyqQVTL0M_icmLsSH4r3SFTTDp-lJSmB46AdTkJULhMk78hL6_xbYnXbsn7IGV1Sz5267hxqhpAoEO62H4b_kdpCRhaePW67L5fPchn24E-AgSQ6pHJ1iympTesAq6nFsp85Nf1LDcMOrFKfe7igHgSM-6KKjf4mepmPbkh2QFmjhJSrf36LPhD0lkj3zIyVAxhV73pCKt5ZJMWJ3_ju0y5nxBNoDVaHU-4uu89enwZZq1aG7kpn1lOu8Kxwk6lfs6kTvWJZEfnURNVJAFpJjzl8IIwV2oVR82D0xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری ۲۸ صفر در بازار تهران
عکس:
علیرضا شمس
@Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/455678" target="_blank">📅 15:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455677">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">رویترز به نقل از یک منبع ارشد ایرانی: هیچ مذاکره‌ای درباره تمدید آتش‌بس با آمریکا در جریان نیست
🔹
وی افزود: از دیدگاه ایران، آتش‌بس تاریخ شروعی نداشته که چیزی برای تمدید وجود داشته باشد.
🔹
آمریکا ۴۸ ساعت پس از توافق موقت آن را نقض کرد و چند روز بعد از آن خارج شد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/455677" target="_blank">📅 14:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455676">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uz89VBX_pHH5_HwdYFcNIT6Yn6cSQTmY3kGdF2ZE_sV5hXFtJG322eBBxDV6DwWwX083lTXWWKv0jRXDfiXRvyj9fUhm_bCNDeUL8N_abAegDsnvQI5AcVN49HAuhF4Bd64TK9dTBY2kLvcaj61sQMk6kgVlv3QydeT-OdnyeD_QLtGGZ4iRxVnaZ6VR9l8MSDbsf0jUkIS0T9I0BteaXBYupkKcUFfSI7hFjEYKP6DctFCcBeOmoJFr3RCkrwj_EXv2N-njQecrPaSVRYAAfWFCF4Kz5-2kO9eCETxOkT93NPYzPwy1VCd71RU_bziDfwN9G-dF00lb9X6Y3UE9yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: مدیریت مصرف باید بر اعتماد عمومی و مشارکت مردم استوار باشد
🔹
باید مردم را همراه کنیم و در مدیریت مصرف انرژی به‌گونه‌ای عمل شود که موجب نارضایتی عمومی نشود.
🔹
اطلاعات مصرف باید با جزئیات بیشتر تا سطح استان، شهرستان، شهر، دستگاه اجرایی و حتی واحدهای مصرف‌کننده توسعه یابد.
@Farsna</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/455676" target="_blank">📅 14:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455675">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8U10_YJWNwOhhTgM6uIxNyRlo5xsgrPmFfgVjLTCEULwQxkY1FhLbRfvGj4f3lMaBpmLLhDNEw5hO_qR1HR_XZ13_SUT2nBQiK7X-TpvIPOj2eQ_J1SHQ3SUkF1O4Bthwlsih12Y8GdlDs7QyCuZjWsXxwvVeS_pmdMSPR-Pu4Y6OFNYbbu6ehacIGSgNcGU-NUZ4WmAjrNg06YyC3FUiwLjUDOKSJHyZiunRIfr0NHIM8KmjvMDieLhqf6nIwGWk2DgafSfXasoK7BswBXgHFqgFtdyyxExaLOwhso85Xt-E44hy5KhR1ISpe6pHkdP1kb1Jpy5jgjRREhrTCPIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون فرهنگی سپاه: ائتلاف خبیثان عالم نمی‌تواند بر هوشمندی ملت ایران اثر بگذارد
🔹
سردار معروفی با بیان اینکه ملت بزرگ ایران از هر قوم، مذهب و گرایش سیاسی در تولید، مبارزه، تثبیت و نگهداری انقلاب نقش داشته است گفت: ما ملت شهادتیم و ائتلاف خبیثان عالم نمی‌تواند بر اتحاد و هوشمندی ملت ایران اثر بگذارد.
🔹
در طول تاریخ امت‌ها نافرمانی کردند و امامان را هم تنها گذاشتند اما ملت ایران اسلامی با پیروی از ولایت هرگز نگذاشت پای دشمن به خاک این سرزمین مقدس برسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/455675" target="_blank">📅 14:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455674">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rn8YT4mdbxOW2ZH9IIoZkZrtDsX7TZO7DQvmZeeLRjLZ_ntOYqs8d6iNia70jNwVNX8Zu3UwzKd1xe8ioQRrsmIxZg13eBVUP94v1q1V_whvnFe8Ejy9BMmh1T1q9IhbMX_N7e2xZtZ4OtOgmmVwT6pBadZ0kkFYg6cpU5Pfkbw1wLt5a84sS560oi4a98XW0IL-1V0peN8PTVz5tyalK4Kh_fx9xqFS0jjYRK2m0_OWjnkgyxWIEBeUX1vHfGY9F9hC0Vc9FwFFBIsZ-ldQmrThHm4uQttTNnRu0kQsGMwB4ARd77kKVOmc2S9xcigaDSxDp88b1llVguMIlsTQqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلودگی نفتی ناشی از نفتکش سرگردان در سواحل عمان
🔹
سازمان بین‌المللی دریانوردی امروز از نشت گسترده نفت از نفتکش سرگردان کارولین بی‌زانگی در سواحل عمان خبر داد و اعلام کرد که بخشی از نفت به سرزمین اصلی این کشور رسیده و برنامه مقابله با فاجعه نفتی در دست اجراست.
🔹
به گفته این سازمان، نفت در شمال شرق جزیره قبلیه در حال حرکت به سمت ساحل است و برخی گزارش‌ها حاکی از رسیدن آن به خشکی است.
🔹
بر اساس تحلیل تصاویر ماهواره‌ای، لکه نفتی تشکیل‌شده در اطراف این نفتکش به سرعت در حال گسترش است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/455674" target="_blank">📅 14:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455673">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0EsJy3jKX8MQGnSPqUxbXCYdmRsws6jC2_wz0YrgrdMaPu8fgj8FAlxFE5f5QTSFckWP0WmgEnnJ6ZPNyOBgqfpB_EcjEPyvHZemDjXrAQSyzep1ALgtT4EqOp7PV4uHvIJ3TjUA92IMXJBqwUeDvBuOKKMb8epU8mTYycAhDc5DyWjhWc3txkoJjc-Xw1CsmWqlCy9mH_47sGpYiF7-C6HDPtyIsospQgG_-Z82vI_WmCShLXv8J1yxaK06jTcpkKybwOh0gjnJrX733tv1-oCr5w-PQNhETJQZc5lLA2g43MP1_mwqC7SgZwXaqyFx5VO7steCJgMhihkL5xCCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در گفتگو با نخست وزیر ژاپن: ایران به دنبال ناآرامی در منطقه نبوده‌است
🔹
آمریکا و رژیم صهیونیستی با تجاوز به ایران، ترور رهبر انقلاب اسلامی، شهادت جمع کثیری از غیرنظامیان از جمله دانش‌آموزان میناب و تخریب زیرساخت‌های غیرنظامی، موجب برهم زدن صلح و ثبات در منطقه شده‌اند.
🔹
ایران خارج از قوانین بین‌المللی عمل نکرده و همواره برای بهبود روابط با همسایگان تلاش کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/455673" target="_blank">📅 14:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455666">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TuOp3ldNDwgvuQR9m1nwElSG7PuBQnJGiC4qoclNrmyUHveMq1lDqbz03OQ0r1R_MhbhnDLmEOMD8JJ9Rjetl5jp6armztkC8bhjiXOTBzVcRN6FXaAKJTGAjrvAAHGg86hjpKSL8R3LeYKThECpwJYuiJDB73ucIrWKzu-J5iONG30xWok1u7CZ-gwwSsHNqdiE3ZA6dIN8SBhwg2zGe5h_0GJO4qrQXogQc9nj1-RC_TUdtASGz7qMqaJB9quoVZvJAg5d-ccgunUJC4lMTfZJIu8xyBtV0vO6F4EJP38yMSWcIClrCz9Pxq8YcxEAvggl43heSN4OQkmjLYTgDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DcGiddw4phn5rWP5UcWpsCgweDIIzcgYZIK9bLbOYGIuP1UCinw0qUMrKeJtbtCmwiQ32E2v1_XURd2Vb-YFL-xdBvf1AqK3z3OlBlOw_XzvYGOabb2Ry8wP0rH641lAVfRnA_n3w-A9osrcBmLonW8CQblkpUyKhm8p9EMAw7ZSyCXl5wLvKZDzy9J7l6-lNsueMQPNHa5O3EqkfsxP3Oun_MlTEdeHvoPkSRF-vio1kTwPICccBdmUqZdJ0O6OBooobDVUSpYOq3vgOP8XlVK5ZyDXK5dp6fvSUomi3Nyz5SuT9lNb-i5vyEP53ZS8e9Ll3G9UmSxvll0mgTgs8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QJNUX0IxusFuPUR9FmTNcRnq7zz584PIxuKq5KL9GmQdoKdJqOUgE4udoXgoxAOFMPhDsV1r-NnrW7BgtrHpS-Jc8NgqeM_fpx9JjiIDOIH-mTYvYOzdplAscifv6C5D2q_wfqoGvwctWH15LhdWPw1ZndNs9he6wqsRJSC5ybmeS6eolMhyRxpcezUFaJW9Wmc7fVfbv7Ofp3pklmtqbQglUG9U_UtVXlxely-fXbGWCbu6bVs4nHFDJ_QGObpxT2vbmX1tuklrkyTh6XTGsfEur4q82d7Hq31hSrgGvly19Z9PsfpSGw8muYt5vJeZoAXOgGlQfVnvFvOtAry7Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gSKVjs7bvPEyb91sf3EOaWQq3JxrF7erriC35kIyKJHZrXBYso6P_9yQ9T37CIEjGM8ERtnb9nEVcsDoHfECjnqDb23ah3_CH9juCjUWMs0jCCZaFcrhVIJMvW4VW-nBcwzNRuEfLsQf18stuTgQm17v6dZDQyBAv28ci8jCAuAwNAG6Trg4WEEDa14Dx4baSm6MFcqW2ijv4fMmYirtO6PFyVNfu-CasMrMQQGTLbZbrfMBnGS69SVPQdYUgv7qhqm_gTIJfCTxwfJ5N_YZvpLEC0WU1zMcFfEiS5ANAJb_Xs_PVoyeMQbJdgxrY26aYUHUToF5Cq8gfUbiJp97QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p0MkLL9Cj_9topofhr3A-beyut7ZZcbp4XJLQ8V-1S_g3oPCr01q8Dh7BmzPBGu498jlBKa1QiSlBwLDZQtrjvs58hO9N4XYL4LTBGp4NerxYPPboblvPeJUBRSkNvDn9JpRjfsUgD3R9R25hjfGLYZ_hsHZ759mzbqPYauvZINt2nZelIwztVFCW4fF2oqdoO5FiM2Ewz44Wm_z6ITDLSjnlUfNCbDtXQipVebGfa17b8ms8BQy4ACHu-pwufBvva1arZ6wU2Izny4M-L569POHruRMCrk8gDu-1U8woH9ILwN_IhoQiG7PuB0eabUq0H4_tsC40Yx4IrW2vKP6hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/An3KFEj_9peMjdhDSRTzlNW4Gg48otF4e2YbCOqPoaVf3KunXq-0kDehhPKs8KgV9fyIhlYzN7FCTbuaGCJI2Fubfrtts74LhrJ1Ei1zaah8tyuGG4CGXbLMdtzGJ-dWrnjo415SqtkABiMq0OgkT4rSCuwGNPGNdh6llAZ-BRkmNWBftBSqdhV-Zp_8yBK36_ORIEVLoGmcJ14TAlynzMfGLaar-MT3DKyKIJrhb4nWHf9g9X_rRP3Nvw9ne4MHCRk5xMmta_OKaTzRyyhWKbZsvYciBOnoxb3CBh7xWWYGyT8gle5606RpAOme8ACQlM_GIkHir7bx131dg3Ihig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A6nDKmtUyA12PipdSqSp0x3JDkkhCByPXFmKnWJK-8OikRtffDHh0L8XJuUR6H1P6gOqPZdg4pvuVy7rScZB4OYSNVd9JVmBEKwLn6RwHkVoOdNe9oUydbHK0AdSM9cQNx_MSTwi_rUc-mOmcX3wkYDogTu3bWEG6tWBJAKFCUxbzpgv789khCmWcRdHu9Tg3vT7VKQ3cYlhtwtV74745U-T6Wug03ra0ui0mDtaiDhUwlyzhRw-P247g2tkZFyF4GyEu-FJViK9jqV0Wrj2n-lJvVMYDYr188rhRscg771tE8PgNTrBwX1rvHZOrLU64RNYz-3AntV_x_1CGFRg3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری روز ۲۸صفر در قم
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/455666" target="_blank">📅 14:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455665">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/540ee24ab5.mp4?token=uNeMoqpH-mKTZA4LeIggKBrSXrsHKwK9yob15xl-DYMZngHNtRPm2rKzu4EnqkEDOQH6hGn4om57hxRL69IZKJY1swKy8BTfizuJT7K_CaeloEY1ee9sgOiLbK93ZufVwobTqfZjlnePjWoZmEaNO7BJXpArf-VJEvVhaR9cuGaC8kDbRG0ZdHrrlknefEA4uPZlooAteavdEt9cFJVVc3TM3IEXwJ4taSAQhj6LleEUqRpqKwb2zR2sOks-9oPe2ZQbyycGi8eRw62YPFAM3RF56E7g087xbnKCpWLZ81JGpmQRunIvndeAEYCzlFkV-hU7F8x2_rRCm5UOZ35uxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/540ee24ab5.mp4?token=uNeMoqpH-mKTZA4LeIggKBrSXrsHKwK9yob15xl-DYMZngHNtRPm2rKzu4EnqkEDOQH6hGn4om57hxRL69IZKJY1swKy8BTfizuJT7K_CaeloEY1ee9sgOiLbK93ZufVwobTqfZjlnePjWoZmEaNO7BJXpArf-VJEvVhaR9cuGaC8kDbRG0ZdHrrlknefEA4uPZlooAteavdEt9cFJVVc3TM3IEXwJ4taSAQhj6LleEUqRpqKwb2zR2sOks-9oPe2ZQbyycGi8eRw62YPFAM3RF56E7g087xbnKCpWLZ81JGpmQRunIvndeAEYCzlFkV-hU7F8x2_rRCm5UOZ35uxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گله قوچ اوریال در پارک سالوک خراسا‌ن‌شمالی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/455665" target="_blank">📅 14:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455664">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuwwGPb0-VM9Vgwk6RuscpDItMIgRaX5MRJtbXL89Qlmcd0lj6ZHQLsBgaRO2omYv9wwAkMX92UIwavy7A3ZCUaHbJpxdFsD45Z1Z3ur6OMRKXL7a7HLFPsy-mxGj4dKJTXh2Z1WDUl_NSz8uQDlE3hJdG0RFCqZbAyWEk-w7oPTfPMrJMYcDAMugfK-3zQ7EdlF9O30PsVx8kK5bvK56EM680O99u7aQ3LyBL1-Gr6y37wStBzx2OuckWU3rFhfxqNGYhlRzbFD3YsjvaIq6Okox6PKnpY9rArKKh5F5KwIhialfU_n21Zz3HMn6L7Kof0UuKhorxqEBD0tnBvddA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ ساحل قشم آلوده به نفت شدند
🔹
سواحل سوزا، شیب‌دراز، نقاشه و بخش‌هایی از جزیره هنگام دچار آلودگی نفتی شدند و مدیرکل آلودگی دریایی سازمان محیط‌زیست می‌گوید که علت این آلودگی هنوز مشخص نشده است.
🔹
هماهنگی‌های لازم برای پاکسازی کامل این محدوده انجام شده و پیش‌بینی می‌شود عملیات پاکسازی ساحل تا پایان امروز به‌طور کامل انجام شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/455664" target="_blank">📅 13:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455663">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FR4O6d2kUCZu1SJCorEiHLaBM9PPL_4PkyEg56zc0WCrK9n3rIn3gHdPNYibGzxjP8nCfCgTOSX0J7U_Q-O2uy-kgyQXlBgWm5qQEC_B6aNMl-VuqHZ4i0F1e8LAURDBbdBRu9ssuvlNsEzXpzCOc2_dGqHdRWbDHYoBgEfiVrlgc4Ev3pOJHz9tAgwG7ovPmUb8RHkgb4e_cjiT3EPrgh5SINNkkbpd_CVDDynG_e93Lme_Sqc1KHVyrUALJ_tVcwD4dldmxffYgUj_fXdp6wsp5TrcYvSSkz8bLG0VzQBezaj7cvsbFMMrrOWxawwX9axUKKXB971k8abFsyyjGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتلانتیک: ترامپ تاب‌آوری ایران را دست‌کم گرفته است
🔹
رسانه آمریکایی آتلانتیک نوشت رئیس‌جمهور این کشور از گزینه نظامی به فشار اقتصادی در قبال ایران روی آورده اما «ایران بارها با تاب‌آوری خود، آمریکا را غافلگیر کرده است.»
🔗
گزارش آتلانتیک را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/455663" target="_blank">📅 13:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455656">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4azqZtlgsXQW46j4UcQkJIwX72pNKLnB459-HoKYu8Q3rn5sn9MO3uDEU-PDKFDLUkE7V1zVHRtBT97ToNRKcwvhOo1HIzp509S7nQnFIxDSMzlNidGCEuCugN6f-7wIjq-rHwNjPe5f5OP27rLcXLZ4pFn9zCR-8kt6AXKrWsGLQNJagbdnU4o22Ol_HzQqsi88RSbFPqN5m-31Voc4GNBxSF87PaoJTPo_97ysn42uJc-x2OmXwpr9Cw22wJUWrNt6sgD2tpxbhXk7nWrm29UILc4o84EtBRb1FJa9UtazFWo7IavCrq39dGxyKT0Qcsq9oB4l2C8_OlvaZborw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J_abhs2J2vOsHtrZt8ZYginNMrqsZaQ0S7jkx-BbHluamWmXhuY-JqnemRv_hfJbqHUD2CZ0UuRG_0iey1df8SckwDTczj4RAVwJ2_WoKpbeTHYCE-p8xfZmlAUVn-nFhvKpo7m4suZnMMC-hSg28PqctaOC6sfyV1eJgYoyIaPj2npaHTYf31jiUZpfVlptd67op6I_2Nxk4i36axH5bzcZnacn8dCw02M9NyoXXmr8ghQlVGpM54Znunxh0HueWexUq2DNZZdw1XL9yFOcqb2Xq7slzq_qwGWfNytw-aRwmKHRQ_l05I96EGeic0MwlcHB7Wac34oA94XDyTQTFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/huzoAwO8Kh0_GmsL3XVY1EWFOqfFAZ6_eaXgETSlUk4R3nsQ2iB08o9LdYbfez5_FQveRme4SN5ME6I6zOFblv039RN9Pgk2R0oMmy2ylWroa-rH0d58qUp7Dt9uyTj6V1XRBSV4JsLmGT04qfeLGJ6HnfwLGBfTrLFvJcof5LFpxGWn9GGAMQb_2qPalFzYYSFFFwXWCQEfRVLC0fSbQlzxMvzuicSt68-cgCVmdDdmg2skWSwg8GQiZ95z0mLewN5eQuvke28_X0V6nK3aNIsxY6Qvn5NITeK1DJxyi43dV_6Hi63TimrtgH4TRwkQA1Fn-8LY_zATJMI8uCX-_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cs2smzjypYBGRgRwahWhhwFvuQG7g4Z3-a61xM_ep9xuaA6SrUTNPgdqVHXr-fHk1m0lW_efP-eodo8Zxz8KvUdtchP7jzoB6C7DvuOu4w8HaHdqIDKm0R097lAcsFl4iyBa2CK9pnbsAERHYlf5MZdY1ASZwkcZflPqS-ZkBQVzxLyAQ0nTl1Aj0heLX5I6sbwoXNEzwd6gahJ4FB00oHHJN_y4NCG50K91nrM4tiLtaX9mEiHc0wAWaBWU8jx6d-bh3LX5zNKxNFaeMw05umkCvZIMoAYTLI8WgFqUraOk_2LMhFhIdN2dAK1goEC6q19-sp-xvU_inO_LeqSr5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfTfjSAF79ZDicz7UmSrjIphfp85euWghL5j4XhSpHqtGPYOKeEWawBIYBaOr-y9hryyBIdW6NJkQ-kY4CYPqlzXWpWM8Ny8JzragTVjCFNrJIZDHQTLcJ_xgW4D-LqTAD5oNABp9TaZgpYK3WYhoFu4RCCfg-0j4q4cle6mjH30Vt2r_L7zV9A9kluTIZ2Q5bgEob0L8bvR6P5NygHf5T1zdVQwbPmtWNPe7z94Z9NJ74UY9R-DSOL-pMVLjp0ppt35gkcDz3ekYgpwuFqzplUlnoCkbzdCupjEdqXByTEq-f1AK5pc0fdeaUCnrmDZPE_VVvLKMzZLiqFpNSqd9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q7ZlQWAEZ60bvvpr1oArf-NjWhtKxMI6nusOG_uGoMNL6b0rA6XyE_IT3AzsjZvNXA7zyd_t2QZov1r2KJm8XQMjTo2cc-vk8oTFX1JbMPtc69CATj-BJbnJaNb-hvC1MWpMJkfMYWc_nObvZKNSDIQiVbk4yaSsjM3QA0M3ztxBaslOYIZB1kSEA3SDm25HIBbfsSatjjDYJ7LW9ItMiWeJBl6jLp9WattnoLa0o-g41f5s3bP9d1FvWtw17m83Y30-rgwKYLXdJQXek_71fe37mXQg5vLNI7odpUx4UhAPH5r-NBLBX8kqCYL0a_U_AU0wylF1z4JUMSMIBNAkhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مشهدالرضا سوگوار امام حسن(ع) و پیامبر اکرم(ص)
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/455656" target="_blank">📅 13:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455654">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sMzovs7bh4No9Rn1EZBDy_B48UYVOiBNGrn9ecUjzM_UNAIs-pAUiw6C5p_OpJNmykMxEj9_-c-OdR1tqt2_rQf6BM7iKrWzFABmdJnaVDe-LceMssBVyjRA2yTNLgOG_IeNka-6IHM4YdMoJ7vFiKLecTnhBMpgHmxuXut_sZN2cbXxL7Q4pRQ4zmzHlj8UHJPIjIkiaVd1jYZh9FVVWDQtL9FkzMwOlNqUgW5eNPROsb9ZjcINAb6NPZNiOIeyTZtgLco6UFfrsHp0sy1aFldYd0HprwS3DgrFLxE2081J3-zKweIHu05SIY8eknBHO2kkLdCaUxlKw4qpYSCgaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B7A5vPNYcTSyxqar2_Jbusk7asV6SChq3EwrX1Kb4s55D1WCs3J9mKiCg2vFxJLGyfISgL1KocUrAVVhsjyTzDCJyuJmX8iy5ZQzbanyKu7NU4S87KoIdXml3KzbQoA2nShzKprU-QyVSCD5DdCo0Aa9mko7yoTOPYumdXsRwvA1OSM0cBt01MYbNl7yTmUvyFCJnm3ytpO7T1GjUNgfQTpgGqkJ16_eFQ1EpqTGpR2QeAJPaL61pyx_nL2FL4BSltIn8T6Ghs7eWaJJvAdyf1NZ2zHmUn2iKQVfbw_18jdratXVxspZQr5mHGX2kxukWDBg-nLWy13IeapeRJG2wQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
مراکز اسکان زائران امام رضا(ع) در مشهد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/455654" target="_blank">📅 13:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455653">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9199df8e7e.mp4?token=OLgzl13s23DZfM_dq01RCYRQPCPdmpgMRYcUQXn2Zm5RjHFMCCcE-jYPSPfEqGwwP7e3-HF5587AMrYGHzWPvT7jNEI9Ik-j1fnh-ze8a5joJpK24Gx_04GTaxOwdXWM-52XEGq3FNzHQSWDWV1H3FqXTwTkcE_s6ASN8JY-njyw__Bowl7i3KrgO5dYDOb4JJH9p28gp3bh1stxlUHjWpOEO6BytoZlKUeHJez8hNg-PLl3uSYoo6o7LFFku8qMZrTYud8kKWFHKEu3vZB22_F48P-Dqi70E62ZPuJ0CPVwCAjAiYi-STIqUS3PPCUxW1kILxuPaM58rXpgM85TnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9199df8e7e.mp4?token=OLgzl13s23DZfM_dq01RCYRQPCPdmpgMRYcUQXn2Zm5RjHFMCCcE-jYPSPfEqGwwP7e3-HF5587AMrYGHzWPvT7jNEI9Ik-j1fnh-ze8a5joJpK24Gx_04GTaxOwdXWM-52XEGq3FNzHQSWDWV1H3FqXTwTkcE_s6ASN8JY-njyw__Bowl7i3KrgO5dYDOb4JJH9p28gp3bh1stxlUHjWpOEO6BytoZlKUeHJez8hNg-PLl3uSYoo6o7LFFku8qMZrTYud8kKWFHKEu3vZB22_F48P-Dqi70E62ZPuJ0CPVwCAjAiYi-STIqUS3PPCUxW1kILxuPaM58rXpgM85TnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ورود ۴میلیون زائر به مشهدالرضا
🔹
معاون وزیر کشور: تاکنون بیش از ۴ میلیون نفر از زائران داخلی و سایر کشورها وارد مشهد شده‌اند و تمامی امکانات و نیازهای لازم برای خدمت رسانی به آنان فراهم است.
🔹
بیش از ۷۰۰ هزار نفر به‌ویژه از استانهای خراسان‌رضوی، جنوبی و شمالی…</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/455653" target="_blank">📅 13:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455652">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4069322e1.mp4?token=ElkAWExOQoA_vKaunK2KHXYaano7zuZ2JPzREHOAR1HSWG83kiImgtfu0dZcCrHnxUo4yxWtAxdxSPYb_NdFzP50_mFQpvPuruO1RA89oiTt0sY3FUuj4FNinu-cYB_kVVgHOq8P9G4XGDv99ZOn_Zx9T0W5sPpjA6nAFzSFxYN1dH2zRWNLGjMunQm1QOFW52ENqGyyQhXXhZiWB6aM3PVIKNiLfTvUAHC8SnGos4ZpzWrL9j3Cx0cw0o_dOLEtMqvGdK7d7BFRz7Cqy-eR1p8aTxo-8EZCa1FFXdk9RnVmzddBr5SN_ZHX1F9_rYmCvxtuekbkicqIjh5hi5QrXzfQmsfCXIRn-kZR6Hwf-rVq8OW0wsI4aYDhPk96EV7ekOX4wwApoBtqBV1SQNv4ZqoY89jaR5pOBqrQU1N_nDV3-9wI2HqWEUV-SIJW2QcwZ19jRPuL9BqGhaCbtgwLqA6O8fHEqtNeCbg0yobTgay975JAoAhin76x2-aP85XxQ-zmCzuRMXAUgLtcz4m0-wTaubsiMU6jCblHMFxhVEMP2pYBImLTfBlm8P7lVdqsRQgzivvl3JA4SBb_XZnFm-hqxKQGLTZEDI5uqgbwtL18vmTCu692VKV71GtHtCNWw4-YBZi5AjMXtb18Of3vv7RNu1oR2aQYz6qnm315kdo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4069322e1.mp4?token=ElkAWExOQoA_vKaunK2KHXYaano7zuZ2JPzREHOAR1HSWG83kiImgtfu0dZcCrHnxUo4yxWtAxdxSPYb_NdFzP50_mFQpvPuruO1RA89oiTt0sY3FUuj4FNinu-cYB_kVVgHOq8P9G4XGDv99ZOn_Zx9T0W5sPpjA6nAFzSFxYN1dH2zRWNLGjMunQm1QOFW52ENqGyyQhXXhZiWB6aM3PVIKNiLfTvUAHC8SnGos4ZpzWrL9j3Cx0cw0o_dOLEtMqvGdK7d7BFRz7Cqy-eR1p8aTxo-8EZCa1FFXdk9RnVmzddBr5SN_ZHX1F9_rYmCvxtuekbkicqIjh5hi5QrXzfQmsfCXIRn-kZR6Hwf-rVq8OW0wsI4aYDhPk96EV7ekOX4wwApoBtqBV1SQNv4ZqoY89jaR5pOBqrQU1N_nDV3-9wI2HqWEUV-SIJW2QcwZ19jRPuL9BqGhaCbtgwLqA6O8fHEqtNeCbg0yobTgay975JAoAhin76x2-aP85XxQ-zmCzuRMXAUgLtcz4m0-wTaubsiMU6jCblHMFxhVEMP2pYBImLTfBlm8P7lVdqsRQgzivvl3JA4SBb_XZnFm-hqxKQGLTZEDI5uqgbwtL18vmTCu692VKV71GtHtCNWw4-YBZi5AjMXtb18Of3vv7RNu1oR2aQYz6qnm315kdo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کشف پیکر مطهر یک شهید در یک تاریخ خاص
همزمان با شب شهادت پیامبر اعظم(ص) گروه‌های تفحص شهدا موفق به کشف پیکر مطهر یک شهید دوران دفاع مقدس در منطقه عین منصور واقع در شهرستان موسیان استان ایلام شدند‌.
@Fars_plus</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/455652" target="_blank">📅 13:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455651">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tybssFfvOBcHZluOTrYkYGs9wrRmMa6bobhrFtdHGRh-qhLGZzzKjrsc0LcfoBQaXyXCw3l2uy88sOv5rpJA0Guleh494v80WyRKGorJJfetCsMwHFU0fM53ITmzRxY1w8Qkq5J-7uVzByXgwQO7RWHmBMPkXVs4_yra8-A1JFfdhpw-3dYUz-fJed67RRIUvHTJ6ZEqBwo78Xz9v9_22lgsstiTA-a65QKOhjnZt-bfgmaP05Z13yMnMo-mFgAwTbydboWMhkV3aiXD1BQVK5eqxARZ64AND4SVhcz-ZkNZSaTa6cARdvCBGQeuCk0i3Pym6veAovIkIdEf9bdTMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملۀ پهپادی به یک نیروگاه برق در لیبی
🔹
الجزیره گزارش داد که نیروگاه برق الزاویه هدف حملات هواپیماهای بدون سرنشین قرار گرفته است.
🔹
شب گذشته نیز کارخانۀ ترکیب و بسته‌بندی نفت در پالایشگاه «الزاویه» هدف حملۀ پهپادی مجدد قرار گرفته بود.
🔹
هنوز هیچ گروهی مسئولیت…</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/455651" target="_blank">📅 13:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455650">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khnUVOzFpWSs1rpFkJhVts_kvLARueYAcsCU1VzD0Uk6Y7Tb14zxbfGPLRb8w_TVPK1pvPmPu1-uScmvoQUQwR-hXTDulrVTJDA8P90ErRlgD_bHiBciMUDRczUGIaQl5SHsu67TT8RyGdIyec8ocnpJ6bp9_X7Li5wufsVtBuuomL7A1eOKMVYhd-8Z-W7IljLq5a2iMT-XKOeJE9sLU-TflsEB94ExWcNpJL1-s8iEgeeF05tMKn9WDbmIJgo5_-MZhXu1gMu-dMR8z_JWndszoThr7oCBijgoHvqISAkLCXdb6EkNMjDgnkZGKrvfTMS62q2nxud8VyUbzpsilw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازدید نمایندۀ ویژه رهبر انقلاب از منطقه ویژه اقتصادی لامرد
🔹
حجت‌الاسلام وکیل‌پور که به نمایندگی از رهبر معظم انقلاب برای دیدار با خانوادۀ شهدا و جانبازان جنگ رمضان به لامرد سفر کرده است از صنایع منطقه ویژه اقتصادی لامرد، ازجمله بزرگ‌ترین کارخانه آلومینیوم ایران بازدید کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/455650" target="_blank">📅 13:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455649">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83e54c2f77.mp4?token=rWHlwTsScAIJ1zpZwQNpe4g2FRUpaVEj3bdrlwXNBZzwE541v7E1Hzcy_ShaYWcF0xrA-OThjMUbd5W7ehGIhoIOMUlHvUNOFQ3ve7aHdaayMOMX2AFUt87wuGyHH6csod78KugBo8jNudhnN14mgvIcD28S5WWE4WtUZchj7lN-VcAtBKMauOMOSDnWoJNJcFF2ttuX3WW5jgkhNM-aWYm9GNrNfJdBoiH7_Wen1RKy8i0p3jbGfk9zxMjhjd1u1JSnNcdjbDf1ew7YOqq89VChRlB__BAL8Brx1jP0jvuhiFtGsn8qkhHhU8opptaUKQv9eacSD6t-U38t6cbKKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83e54c2f77.mp4?token=rWHlwTsScAIJ1zpZwQNpe4g2FRUpaVEj3bdrlwXNBZzwE541v7E1Hzcy_ShaYWcF0xrA-OThjMUbd5W7ehGIhoIOMUlHvUNOFQ3ve7aHdaayMOMX2AFUt87wuGyHH6csod78KugBo8jNudhnN14mgvIcD28S5WWE4WtUZchj7lN-VcAtBKMauOMOSDnWoJNJcFF2ttuX3WW5jgkhNM-aWYm9GNrNfJdBoiH7_Wen1RKy8i0p3jbGfk9zxMjhjd1u1JSnNcdjbDf1ew7YOqq89VChRlB__BAL8Brx1jP0jvuhiFtGsn8qkhHhU8opptaUKQv9eacSD6t-U38t6cbKKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به مخفی‌شدنش در کامیون حمل غذا واکنش نشان داد
🔹
ترامپ دربارۀ واکنش‌های کاربران فضای مجازی به مخفی‌شدن او در کامیون حمل غذا در فرودگاه و تغییر هواپیما از ترس تهدید ایران، گفت: این موضوع مربوط به سرویس مخفی است. من فقط از دستورالعمل‌های آن‌ها پیروی می‌کنم.…</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/455649" target="_blank">📅 12:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455648">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پروازهای فرودگاه بندرعباس از شنبه از سر گرفته می‌شود
🔹
اداره‌ فرودگاه‌های هرمزگان: فعالیت پروازی فرودگاه بین‌المللی بندرعباس از ۲۴ مرداد آغاز خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/455648" target="_blank">📅 12:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455647">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بازی اول استقلال در شهر قدس با حضور تماشاگران
🔹
سازمان لیگ: دیدار استقلال و مس شهربابک از هفته اول لیگ برتر در ورزشگاه شهدای شهر قدس و با حضور تماشاگر برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/455647" target="_blank">📅 12:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455646">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCBiQeJi7aJNyu2k1o34F72Q9EhGti0P2dFX0XHwuRV7nG1M2mVXCnowhiheeSWOfXxSNrVBgZjtP-1OWD8slg_ANBdmsLop0LtSSV1Cw-DBeGUC_p1EsqbhiRxGK59SAOFK6-Q9CvAQGtvvTXKHiyLAKhPBMdUz2V2gzMVd6vaYOw1VcNbZ1DTGVCYq3Ww9jVTonh3QDVvPePOqCB_OQ9ukqDBvnfAAJ2q3MhYwKRcxOfyPMoliGTjcloDPXfVm_GTSVrZRzSA0WpKF6v5yVprB52G92j1iTscWbyMxCYccChr5k987Yl2yL5D-FKQ7-E4nRJbYoyDWuI_nSa2taw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غریب‌آبادی: خزر نباید به عرصه حضور قدرت‌های خارج از منطقه تبدیل شود
🔹
معاون امور حقوقی و بین‌المللی وزارت امور خارجه با بیان اینکه دریای خزر ظرفیت آن را دارد که به یکی از عرصه‌های اعتمادسازی و همکاری منطقه‌ای تبدیل شود، گفت: امنیت خزر نباید به عرصه‌ای برای رقابت یا حضور قدرت‌های خارج از منطقه تبدیل شود. کشورهای ساحلی خود قادرند و باید بتوانند درباره امنیت، ثبات و آینده خزر گفت‌وگو و تصمیم‌گیری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/455646" target="_blank">📅 12:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455645">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVS263ez-ujlfhGu81GmIK4vVstGMMHg9Y3x0CUs05qhYcVP7UdqFFPPvIrk8wmV6jh83N645UQfQmLqujn9Q0aQ4ssFenTmRAJBndJbxNY-i7nT0VbkL0rYTjOorGjkYMxOgjDGfce17vLAsPTEXA8g9s_DkIU083FjdBxRmI0dAz1KaSmOT7UxaRLMcljT6Tq-CN4GJJzWNtooy6mPJU1kXR6KwuSXJaEtM5_5l26L66eGk2jTqWyz5WrC1LMvxkf7Q8uszqoUtbKGQbz8rq8Y9E0-Qb8TBvl3uDOT19fmcHUe857RbXdfWlqVrhhxa8iMSXuzV_n4jdA0iQ7PPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتین اروپا را تهدید کرد: به توقیف کشتی‌ها پاسخ می‌دهیم
🔹
رئیس‌جمهور روسیه: توقیف کشتی‌ها چیزی بیشتر از دزدی دریایی نیست؛ اگر کشورهای اروپایی کشتی‌های تجاری روسی را توقیف کنند، مسکو پاسخ مشابهی خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/455645" target="_blank">📅 12:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455644">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbcf87c51.mp4?token=caq4ILi6Y2dI-1Nm5jaAPbDM-dWEun7QO2Qna7oJ8eDCKcywdga3d4tOWj63P9nMfQYBdzByfLOhGJeznUqXLoSIgcguwgx18VXEBIN3JdxSPvSUV0JhUcCU_ZBP7UJK1slBOQnVacB6pkdN596r1Xvo4nePGWcTq-pH3BMrhASOXSoJwhuyOr8zxFpsh_6YKYhdC1e5p6st6ZqxM9GZ1DTaxpiPJzxs7TfKnnrikVPkt93VR_gsrMhilwa1Q_WOGCuyXxIMwdpmoUBwQ6zZOA50fOmWmY1vXwP-CRin8bslgfrKm-Y_wjdmarRnQxzPsSQ3R2s9Qj47StKbPJ4IbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbcf87c51.mp4?token=caq4ILi6Y2dI-1Nm5jaAPbDM-dWEun7QO2Qna7oJ8eDCKcywdga3d4tOWj63P9nMfQYBdzByfLOhGJeznUqXLoSIgcguwgx18VXEBIN3JdxSPvSUV0JhUcCU_ZBP7UJK1slBOQnVacB6pkdN596r1Xvo4nePGWcTq-pH3BMrhASOXSoJwhuyOr8zxFpsh_6YKYhdC1e5p6st6ZqxM9GZ1DTaxpiPJzxs7TfKnnrikVPkt93VR_gsrMhilwa1Q_WOGCuyXxIMwdpmoUBwQ6zZOA50fOmWmY1vXwP-CRin8bslgfrKm-Y_wjdmarRnQxzPsSQ3R2s9Qj47StKbPJ4IbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همتی: بریکس باید از گفت‌وگو به اقدام عملی برسد
🔹
بریکس می‌تواند سهمی مؤثرتر در شکل‌دهی به معماری مالی بین‌المللی فراگیرتر، متوازن‌تر و مقاوم‌تر ایفا کند.
@Farsna</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/455644" target="_blank">📅 12:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455643">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d9774d60a.mp4?token=pTEB58d9P2s50f6ifKGir5M3GCsh3GziD-vC8kJcRsNx-o4X2VENrKFmPi9c0P0PDcfPR8pRd8gOVQz6_Y1LctXnTSOXnPET7KAAhbePpQXgQyvfWi-b6frfwbq5sSalLCVPlM_MTSbMHNKpXL93C5Dex3hC9WJy-Qwz_poU6w8t-yQTEWYOlKII-Hq0y4hcXZ8qgbghZ-xkY55y4dz_JErVX8Hgs5tdSiBBv65t08Y2Dwizzhlqu5PbEkc5gclImgxqldf1UFyvSw8JFgk558quTfeR8tTjiJvm-OjsgeYV_tV64A0a2F6w2WbIgzsIMT5-EVrOLhX3Bp7qhhAngQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d9774d60a.mp4?token=pTEB58d9P2s50f6ifKGir5M3GCsh3GziD-vC8kJcRsNx-o4X2VENrKFmPi9c0P0PDcfPR8pRd8gOVQz6_Y1LctXnTSOXnPET7KAAhbePpQXgQyvfWi-b6frfwbq5sSalLCVPlM_MTSbMHNKpXL93C5Dex3hC9WJy-Qwz_poU6w8t-yQTEWYOlKII-Hq0y4hcXZ8qgbghZ-xkY55y4dz_JErVX8Hgs5tdSiBBv65t08Y2Dwizzhlqu5PbEkc5gclImgxqldf1UFyvSw8JFgk558quTfeR8tTjiJvm-OjsgeYV_tV64A0a2F6w2WbIgzsIMT5-EVrOLhX3Bp7qhhAngQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقوع سیلاب در تویه رودبار دامغان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/455643" target="_blank">📅 12:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455642">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726c99adc1.mp4?token=MqJux69aeTd_CN7Gc095Vh3RBjPXrdZtd2KJR1kpaJdciKFVkEExuZYzs0X9OZuVFRdJKQ2AW_PBZAAq4FEeE7eiqfV_mxKFYtp6MShC6DKevS1kTbHRK83wnWGn6ZuGBX-6D5WpS0hbHXyzWovQ8YrcXEERhqWPp9pa-mb0CBwYXVJSil8SxfZ754Rb0LdalQ04_w-SCGqCQUJdHZDUEbuKvSXHq3MTI8zPtTjIAiqGoLghe7UXWIIEqEsaGJarnfFk3LEgcIm4DtIcZBRHKgJEmcmldlf943fVs2CmDDmwjXAkWbZtLX_5BYtyyq5HxdrabnSKrPHl5NJnPRBnDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726c99adc1.mp4?token=MqJux69aeTd_CN7Gc095Vh3RBjPXrdZtd2KJR1kpaJdciKFVkEExuZYzs0X9OZuVFRdJKQ2AW_PBZAAq4FEeE7eiqfV_mxKFYtp6MShC6DKevS1kTbHRK83wnWGn6ZuGBX-6D5WpS0hbHXyzWovQ8YrcXEERhqWPp9pa-mb0CBwYXVJSil8SxfZ754Rb0LdalQ04_w-SCGqCQUJdHZDUEbuKvSXHq3MTI8zPtTjIAiqGoLghe7UXWIIEqEsaGJarnfFk3LEgcIm4DtIcZBRHKgJEmcmldlf943fVs2CmDDmwjXAkWbZtLX_5BYtyyq5HxdrabnSKrPHl5NJnPRBnDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی مرگبار کشتی مسافربری نزدیک جزیرۀ بالی در اندونزی
🔹
یک کشتی مسافربری امروز در آب‌های نزدیک جزیره بالی اندونزی دچار آتش‌سوزی شد که در پی آن یک زن ۱۹ ساله جان باخت و ۱۷۲ نفر نجات یافتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/455642" target="_blank">📅 12:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455641">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/890f1cb4b0.mp4?token=aZtWLCT82Gxns_CWrWizbAfCwn_A2uwExExIS7gcFw8bU1kRhvrLQedXWvFg-dMETzTHqs8H38Vx6MdjCcla9Lf5UtmX9ZBRiXLe0VAw3ojkASaMJ7BK5KXQWxwHlDnAIG4uEzB4CNpHkROsihtFwkBd4KJlxR02OQUyb5O-zZyxn_oCrnR3vzyjFyPhaEmE6qjzlPAjYthnkgkQrFoDXiUJnHEBpWMM2kNSiEhn4fTiWZy-aVEzyOt9Uon3H5DCl6BaXci563ZlwvDm1LgRDgRwwrBSa4Iuk4QRUMZYfJplBjl62EHRllzq1sTKSXMFAkty_DsSAxosgaJfRgUPLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/890f1cb4b0.mp4?token=aZtWLCT82Gxns_CWrWizbAfCwn_A2uwExExIS7gcFw8bU1kRhvrLQedXWvFg-dMETzTHqs8H38Vx6MdjCcla9Lf5UtmX9ZBRiXLe0VAw3ojkASaMJ7BK5KXQWxwHlDnAIG4uEzB4CNpHkROsihtFwkBd4KJlxR02OQUyb5O-zZyxn_oCrnR3vzyjFyPhaEmE6qjzlPAjYthnkgkQrFoDXiUJnHEBpWMM2kNSiEhn4fTiWZy-aVEzyOt9Uon3H5DCl6BaXci563ZlwvDm1LgRDgRwwrBSa4Iuk4QRUMZYfJplBjl62EHRllzq1sTKSXMFAkty_DsSAxosgaJfRgUPLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستۀ عزاداری ۲۸ صفر در بروجرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/455641" target="_blank">📅 12:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455640">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moccsO7Fb1ckkNm-EuOlI69iX-Ur1E6Q_xLuWupyg77WplTeC9HEv2R4xi4rya3vufLTWvoNpdQzN3SVJ1pVwwHw1I07gA8DkN4CRNpVChfPoxKqvcRz4TqU6qNVCm0Z1sPPetjal-VQoIMek6sjbj8YXdoXHqRQUT2aN-y5mVjVqhgZR_A2A6Y3jUYUcZJV-dulTw8bWYMxB7-tX4X5oAWmXCbMK9rRgFKUU0_YHYious-YViWChMJSjAwn4x_uinDio9CA0T3SnWK2s760aKsgRN8AyLJ7ZgiAeS1XgGEKX6pcv4yjiMN6YWXwNZW9Zvnja4efPujLw_ZYk4BHdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رقم تاریخی اجارۀ کشتی برای انتقال نفت عراق به خارج از هرمز
🔹
رویترز می‌گوید که شرکت «ریلاینس اینداستریز» هند برای اجارۀ یک ابرنفتکش برای حمل نفت خام عراق بین ۲۳ تا ۲۵ میلیون دلار به یک شرکت کره‌ای پرداخت کرده است.
🔹
پیش از جنگ، هزینه اجاره چنین نفتکشی حدود…</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/455640" target="_blank">📅 12:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455639">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-OpPG_YnJJVhESh9kjXrjdRtztqJRHP_o7QO19YNgI_Xc6kMnGUX3NA-lcNnPLjJMhe-6F8scpChngeesGyFKEutaV2EJJh9OV-afsocjXR4FA2oDwZzp3ZI9Cj_33w5AEZYkxpOdYLsDfIqCTX0E5np_4XggcO2Z8WmSL_idyIVr8_Zgbzf2195Ilfxqqy3RZUpDa1_Bd7tN3qSdNvUKnpOOH2VuMK__8awwnOhmyHaXO-1Ybx487OT8zHHkIT97xCLTRjdQzk6TTLdsH_q_tem7OG0i4l3iY1bqwX5IiYUaZyzCfWxaqceFieRe7fV83caGdsV_d9KTILPwv0gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زنگ اول به یاد شهدای میناب
🖼
پوستر باشگاه خیبر برای بازی روز جمعه مقابل فجر سپاسی
@Sportfars</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/455639" target="_blank">📅 11:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455638">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pheAtqzlrBqqtAQbs-j9J0-k6lllhEFy_9a48hnW1tylfDOqVvIfMWXH4dsqtJ0uIClRmoQHLKqR5121GDAdCHBx0QjEHdruUO5dFsfiyzYfe2ccDLktn2ZWh9TMFHRqbZeU7-bCmDcfAGDX5a8358ldyEKcFDj8XtfZoDT8K-yIfreXuXlQ_t3XyfKOPgcGHTamX63ZYV8Sg-q7rSBV0h0qIlOsDWy0HfSrn8Kx4UraBfrGXbmf4tueukE8cfQuh1qenoAmu08L6OZ_uSkduARfWAtMkzLXRd56H1mQrGA0Zo5KrYSA2LmI3X81DPcj9pyPybNDwcbstjXtBLvc9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورود ۴میلیون زائر به مشهدالرضا
🔹
معاون وزیر کشور: تاکنون بیش از ۴ میلیون نفر از زائران داخلی و سایر کشورها وارد مشهد شده‌اند و تمامی امکانات و نیازهای لازم برای خدمت رسانی به آنان فراهم است.
🔹
بیش از ۷۰۰ هزار نفر به‌ویژه از استانهای خراسان‌رضوی، جنوبی و شمالی در حال طی کردن مسیر پیاده‌روی به سمت حرم مطهر امام رضا(ع) هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/455638" target="_blank">📅 11:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455637">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cschg2a5TNqi-REKgpMC5v-lH-gk7LuW8HcEwRR90nudChb0UFsmJEVZoc08GJSsqsDHgZDw_Y_AaZVYvFs3mNWCdXPrAGuooteP8Pb4s5_65bMeV8vfy8yxRFmziwdwh410VXvD1QhxaO7VBN_RJ1L3PfRiFhUNDhofwdRTjovGfM_oSGUWFo5AjlJ76x8tLPjDJRuuAmyUnURljTOztJ39Pcx0-tipkmQDOC7RA5AsYb-DrNyncPrOMHFnMvwlREyNdxIqjQqfOvvDfISQkLn79Fu_tzzDcMyUKd9l7JfFVHQy3N0G0hSVbj_dosPv-lK2awgBZLTUshsqJfD6Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابهاماتی که می‌تواند از کنوانسیون خزر برجام بسازد
🔹
عدم تعیین دقیق سهم ایران در کنوانسیون اکتائو هرچند از سوی وزارت امورخارجه یکی از محاسن این کنوانسیون معرفی می‌شود، اما ابهام موجود در آن می‌تواند آینده این قرارداد را با شک و تردید مواجهه سازد.
🔹
آن چه از…</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/455637" target="_blank">📅 11:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455636">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67d701b488.mp4?token=QguAugS8GIOOcgXGcfiFkY4PnqRkUj3E_Z2_sf7GsmqCCwojMM5TYF5_FRUNwGp3IPyeD2ODTETkhbxaOAzXZTr9KW9YxarsyASG2iD8xBiV2XgLUKyjvZURSlAy9eDour9A9jX6jf-KIlXve4VK-8oExCkfnQYiPHirVg-1BVolDN1hjN9R0MShM1wqaOYskIa3fZKdGXA23vzm0wa__U56RUttr_ARs1KOetUDNc7Rhq9XVpZXC_YGJWzYX8nn9aD170QHW5t1hNHCRcUJixhzVJSoJoC9X4ncFWIN7Zzmau13ePDhXt4uMO6xBhe8pkkY64ncevI5hCscErG6aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67d701b488.mp4?token=QguAugS8GIOOcgXGcfiFkY4PnqRkUj3E_Z2_sf7GsmqCCwojMM5TYF5_FRUNwGp3IPyeD2ODTETkhbxaOAzXZTr9KW9YxarsyASG2iD8xBiV2XgLUKyjvZURSlAy9eDour9A9jX6jf-KIlXve4VK-8oExCkfnQYiPHirVg-1BVolDN1hjN9R0MShM1wqaOYskIa3fZKdGXA23vzm0wa__U56RUttr_ARs1KOetUDNc7Rhq9XVpZXC_YGJWzYX8nn9aD170QHW5t1hNHCRcUJixhzVJSoJoC9X4ncFWIN7Zzmau13ePDhXt4uMO6xBhe8pkkY64ncevI5hCscErG6aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری ۲۸ صفر در استان چهارمحال‌وبختیاری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/455636" target="_blank">📅 11:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455635">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYx78ZM2H447vEZXYKmXhHDKa6qP-4yYgHCwuLfDIUiAkKe0cudS8J_eIsM3wcHwqJ98HnfwIMMXi1S-xGmk4rn_keLEaj09R2lgsLwz7Ldikfn0vparBVvQ5aBJQRre3EIw5yJCCHSefIVyX6Lw6L93YtZo-9F3i4tRV28vra4v-DpknYHV9NlEPXaZfk6ck_xF_HWL4UX3xbU1L9BCQlftg10FrBHjdFxwe4JV3oBol0YNZ8GnY-BISOiwLqoOgmm0WaH9mnAFy1okLGyv7L6gLCwap9HjZRR8hSh2vVYd0Zf2eTl_eHCnzmChWatDMORZpkGOStXuZlLP_7LCzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان پس‌از تلفات در دریای سرخ: حوثی‌ها را محکوم می‌کنیم
🔹
ویر خارجه پاکستان خبر داد که روز گذشته در حملۀ یمن به یک کشتی تجاری در دریای سرخ، ۳ پاکستانی کشته و یک نفر دیگر زخمی شدند.
🔹
اسحاق‌دار که کشورش هفتۀ گذشته با عربستان و ترکیه پیمان دفاعی موسوم به توافق مکه را امضا کرده، درباره این حادثه گفت: «پاکستان حمله حوثی‌ها به یک کشتی تجاری را به شدت محکوم می‌کند.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/455635" target="_blank">📅 11:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455634">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b6fbdc815.mp4?token=v2laezx5YDWaNmcV9XK32d-zw8ufcCN0c2XDFX3zz2jXS9QzTreSa-JPUhY_h0ScCerNV6ON2W3uqP2vxFSGV23bXCuSSp6t4dhlBw2ydfILxKEx13HzSHBYDyphNHuklt8oGJ9OUkyPkjwK-EtKBJKrkG_5VLCRwWylY5bQnmDnk1wVCMnxvf2UFjG254i6Y_ox4HwgMseKhdBRlyhkU4jBRA1QXfxBpOZdMjUdG4TjTXLRkNYGj2ai_FR87Ov1RgZoAI4muV-WRCncjwbI_tQH2si8mHzLKv3Vg0TeU7Wgog9BseZeqCgqlq9qM8T-I2LzuCrgsAn4h3hE4kyV8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b6fbdc815.mp4?token=v2laezx5YDWaNmcV9XK32d-zw8ufcCN0c2XDFX3zz2jXS9QzTreSa-JPUhY_h0ScCerNV6ON2W3uqP2vxFSGV23bXCuSSp6t4dhlBw2ydfILxKEx13HzSHBYDyphNHuklt8oGJ9OUkyPkjwK-EtKBJKrkG_5VLCRwWylY5bQnmDnk1wVCMnxvf2UFjG254i6Y_ox4HwgMseKhdBRlyhkU4jBRA1QXfxBpOZdMjUdG4TjTXLRkNYGj2ai_FR87Ov1RgZoAI4muV-WRCncjwbI_tQH2si8mHzLKv3Vg0TeU7Wgog9BseZeqCgqlq9qM8T-I2LzuCrgsAn4h3hE4kyV8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای امروز زائران در کنار ضریح مطهر امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/455634" target="_blank">📅 11:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455633">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iv1HzOKjOT-qXLfHUJjynm7DocrONE3-9dowCFtH5YRjSckJL7zyG7uakOns56Pnp0PO3Kc3u2zRh3QjNTcu4BppSwTsN-pf64WL6Cz6WYWClzZfNu76FeJlXj3QVB9Zp0-I5N5DnF8V7djkiGLIRpIm30XSP3UA_nFCCV7A0HruJ6F0nWgmlp5zof8gCO1lIaZUGxOukRh-sgBUuxNsufqVfrVf5KXSBfznF3e8fvJ472Yar9pe25lqjBYs9cjM3whAQsRVtPIh3DMwhw1McFCb4aAFSgEdq_tGzWHPTytBqQeKc4Y2Lz_tVvGsYLEdTyACe9GceWJ354clfN25bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رهبر شهید انقلاب به روایت خودش: من بیست‌و‌هشتم ماه صفر به دنیا آمدم
🔹
من در شهر مشهد، مرکز استان خراسان، در جوار آستان امام هشتم، علی بن موسی الرضا علیه‌السلام، در یک خانواده روحانی به دنیا آمدم. زادروز من، بیست و هشتم ماه صفر سال ۱۳۵۸ هجری قمری است.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/455633" target="_blank">📅 10:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455632">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cebcbf02ec.mp4?token=W1ZdU8IQOHOQavHjytrlmT50jDteiuWxT7JpaDYrED3xUrsm_sY2JNnt93da2ArPtmkNfTanXoh9UMhHgN0Rpao4-pmDJBitMkFfcn-0EyIU30fsl5aUbL7YzkScijbtsChQmx8FSuvE2nRFAGAM7kVTQ062STykHyO1c6dHGvqLDLNmKEpMolpUNd8SGRgRALBkgcgFbhBFQvCzuoluFSkp_qzOogmdyDTJJFvO9oDvtqfr5re2AhOfwmVuXhRB8YpWRRMb0CPAmFlVgpKipJtqLU5pD3ehFqYYL_UHWKFky8oRxa3XlPij5_gMLhUXWQu9S7w55dIUxUy3jU2ppA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cebcbf02ec.mp4?token=W1ZdU8IQOHOQavHjytrlmT50jDteiuWxT7JpaDYrED3xUrsm_sY2JNnt93da2ArPtmkNfTanXoh9UMhHgN0Rpao4-pmDJBitMkFfcn-0EyIU30fsl5aUbL7YzkScijbtsChQmx8FSuvE2nRFAGAM7kVTQ062STykHyO1c6dHGvqLDLNmKEpMolpUNd8SGRgRALBkgcgFbhBFQvCzuoluFSkp_qzOogmdyDTJJFvO9oDvtqfr5re2AhOfwmVuXhRB8YpWRRMb0CPAmFlVgpKipJtqLU5pD3ehFqYYL_UHWKFky8oRxa3XlPij5_gMLhUXWQu9S7w55dIUxUy3jU2ppA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر آموزش‌وپرورش: سهمیه‌های کنکور در اختیار این وزارتخانه نیست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/455632" target="_blank">📅 10:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455631">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9vp5S950Ef0rfB2uo3k2wiC8-vdbPnjNuOrQ6Yq4EcPIoHJSxH2oihvz2fgzrU1dtLRiBEwNGJtPTKojJKlUBJERFZKgJSl1aZj4Bt_PHAmDodgPFd34de2zvndoEqJ2lHv1t3N_5isXz_Xhc1a8Os6c8tYGWhM5ALzbBuZppyMVj52hJN7XYiuKHt91Fz6-u4CE7vraFqQ6vYYOyRfZs5t0fiLbC9WOsmxoA1SCoUwCoC2wlK9zaTTH-GvcusFo3kNNaX_21y-EZrG0hC0V_iFIKL9HFA_EAd7ak1kxP07Ydb5gkFBtw-nuZXSUjDAKFyFMc4rxHB5R60CkNRM7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پهپاد ناشناس پروازهای فرودگاه هانوفر را متوقف کرد
🔹
به گزارش پلیس محلی، مشاهده یک پهپاد، پروازهای شهر هانوفر در مرکز آلمان را تقریباً به مدت دو ساعت مختل کرد.
🔹
دست‌کم شش پرواز مسافری با تأخیر مواجه شدند و یک فروند هواپیمای باری که از پاریس وارد می‌شد، به فرودگاه نورنبرگ هدایت شد.
🔹
بر اساس گزارش‌های رسانه‌ای، این پهپاد نه تنها توسط کارکنان فرودگاه به‌طور مکرر مشاهده شده، بلکه به مدت حدود دو ساعت در حریم ممنوعه فرودگاه در حال پرواز بوده و موفق شده‌است از سامانه‌های هشدار و رادارهای پلیس فدرال آلمان عبور کند و هیچ هشداری را فعال نکند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/455631" target="_blank">📅 10:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455630">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c78d3270c.mp4?token=Vc8go2dcckRYfBWIiGi2H0x5dx6TxJyqtc1REY6FY6gFCVtE_cNNd53EuLHYzUzqNSQwfKRNMSj3AjRJXoQv9g7oTFuBy6g3yLnJxehk5Wllai4DAIcmn5KD5cu3TD5SoS1toFsjzUvSoHwbNcEMRmXZ3S-isSKRTiFejqbAD7CQBkJGrH1ap3lYsKi2A_t_1_3bQiW1yv0YhRRgP79ZavLItFe_aDoEFBzPXuRA7ah-lBwpKNKPITTPwTeQKtjSjng6Oh3QGcfjmtd3zN66DrMbFkLIM47HtELonaKFPbm2iIF6alaKD8ojVng3qfRA1hwAMU2qLiRqMn_U0z4Z0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c78d3270c.mp4?token=Vc8go2dcckRYfBWIiGi2H0x5dx6TxJyqtc1REY6FY6gFCVtE_cNNd53EuLHYzUzqNSQwfKRNMSj3AjRJXoQv9g7oTFuBy6g3yLnJxehk5Wllai4DAIcmn5KD5cu3TD5SoS1toFsjzUvSoHwbNcEMRmXZ3S-isSKRTiFejqbAD7CQBkJGrH1ap3lYsKi2A_t_1_3bQiW1yv0YhRRgP79ZavLItFe_aDoEFBzPXuRA7ah-lBwpKNKPITTPwTeQKtjSjng6Oh3QGcfjmtd3zN66DrMbFkLIM47HtELonaKFPbm2iIF6alaKD8ojVng3qfRA1hwAMU2qLiRqMn_U0z4Z0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعرخوانی محمد سهرابی در حضور رهبر شهید برای امام حسن(ع)
@Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/455630" target="_blank">📅 10:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455629">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پس‌لرزه‌های شکست طرح براندازیِ ایران در موساد
🔹
بی‌بی‌سی فارسی طی گزارشی با اعتراف به طرح براندازی علیه ایران عنوان کرد که رسانه‌های اسرائیل از برکناری دو مقام ارشد موساد به‌دلیل طرح ناکام سرنگونی جمهوری اسلامی خبر داده‌اند.
🔹
این رسانه نوشته: کانال۱۲ اسرائیل گزارش داده است که یکی از این دو مقام، از ماه دسامبر گذشته (آذر ۱۴۰۴) رئیس اداره اطلاعات موساد و دیگری رئیس بخش ایران در این سرویس جاسوسی بوده است. نام هیچ یک از این دو مقام در گزارش این شبکه تلویزیونی اسرائیل ذکر نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/455629" target="_blank">📅 10:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455628">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc43da2f16.mp4?token=XNomifOCXW5krG62IRsZA5wH4I7onJP3564bOK8RxTR5Yjt_L5cXbLlCb3afdIQL7z9wA8I6APQhXmZoj80zM6FTnxFWaAyQmuCtxeo1h-phO7zPt_cc8krhlcCSdp7PWuK2kgU6hyv8-zoqBhi0p8a0wlqcNwY6cNkr_P5Zs_RKWCz5QMFlheKRZ5eVUTd-zJIS1L-NECu4Tdvuswf3Ep2DDO3auo-zn7RhTbqzoRoEpyjZOLSTwo_ildkzHdOKhOKqCPo1QkJXMvL71n5wW5s61TV47pRSlIjYQO-hxp0Lgm6K81CgMCTTk2ytkV2mLppK0BpTKxuHAofgSoastDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc43da2f16.mp4?token=XNomifOCXW5krG62IRsZA5wH4I7onJP3564bOK8RxTR5Yjt_L5cXbLlCb3afdIQL7z9wA8I6APQhXmZoj80zM6FTnxFWaAyQmuCtxeo1h-phO7zPt_cc8krhlcCSdp7PWuK2kgU6hyv8-zoqBhi0p8a0wlqcNwY6cNkr_P5Zs_RKWCz5QMFlheKRZ5eVUTd-zJIS1L-NECu4Tdvuswf3Ep2DDO3auo-zn7RhTbqzoRoEpyjZOLSTwo_ildkzHdOKhOKqCPo1QkJXMvL71n5wW5s61TV47pRSlIjYQO-hxp0Lgm6K81CgMCTTk2ytkV2mLppK0BpTKxuHAofgSoastDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آرزوی جوانی که با ویلچر همراه زائران پیادۀ مشهد شده
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/455628" target="_blank">📅 10:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455627">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تردد در مسیر چالوس به مازندران یک‌طرفه شد
🔹
پلیس راه مازندران: به دلیل ترافیک سنگین در مسیر ورودی مازندران، تردد در مسیر شمال به جنوب چالوس تا اطلاع بعدی ممنوع است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/455627" target="_blank">📅 10:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455626">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be267c7e00.mp4?token=ExcIpArnaRtcOyq2b7D7Gx8jkcNYzs3uHRi4s4XbPXnOaCjcxxZQyNUUF3PoCczF6IQ8CKrU8rWu6NDNtQ8pHu5uFnU7FHKX_EAOrLd7MNVsg-_iCKG8XEhdGH2eMvpeKFqN2W2KNVs8RCnoW9TnbDyDPe4LF6My0yWEBOgFimtSTHyCzs_40zhJwFjRqCKRb5mUwwAbcqZOnsFPQAD9qVFnUqap9zFIYydlBmpN1X_-BSWfO99V5f146i-44Mgyo_-uAFrkXb5ibgR75TsLaIeMCRS94FuzViIlnWgfBemlerSrw8sNjmFHjX9VwTgeT1LCtqi1rn_3pIcU0Twb4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be267c7e00.mp4?token=ExcIpArnaRtcOyq2b7D7Gx8jkcNYzs3uHRi4s4XbPXnOaCjcxxZQyNUUF3PoCczF6IQ8CKrU8rWu6NDNtQ8pHu5uFnU7FHKX_EAOrLd7MNVsg-_iCKG8XEhdGH2eMvpeKFqN2W2KNVs8RCnoW9TnbDyDPe4LF6My0yWEBOgFimtSTHyCzs_40zhJwFjRqCKRb5mUwwAbcqZOnsFPQAD9qVFnUqap9zFIYydlBmpN1X_-BSWfO99V5f146i-44Mgyo_-uAFrkXb5ibgR75TsLaIeMCRS94FuzViIlnWgfBemlerSrw8sNjmFHjX9VwTgeT1LCtqi1rn_3pIcU0Twb4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوگواری هیات‌های عزاداری در حرم امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/455626" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455625">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs61PwSMt_8RUOXTG5hMlk7Yg-gqGinnLjUCDBXkUXVi4QY0dpkuZTcxm1sJLCMv6bJ7g5GUpUwGWnOlAILz6L37fpbcyJR0W-j01OqD4d3oslMMiTk9U-YVJmo-YiqpL00PItaEnHt0Sk5hUAmEMLwskVlE6xTR4_YaPlmwuUXtIv4ylP8MYQ5rtvufe_JODObYBQFalu7wQtkQwYF4KLB3IM3JkYOF8Rx3b5sZccdyoAcMYazGrGQs3yX1izAVQ9knp_A6Mv_94xn9md_MkVkuCWF4wzTTV4UfUnvQYajDlgqLbS737dLXs6-6jMvurmuTH0MjpXA1ivMNPuh7XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اثر وارونۀ حمایت ترامپ از رئیس فیفا
🔹
«حمایت ترامپ از اینفانتینو باعث تسریع برکناری رئیس فیفا شد»؛ این محتوای گزارش امروز(چهارشنبه) گاردین از نتیجه حمایت علنی ترامپ از اینفانتینو در سخت‌ترین دوران ریاست ١٠ ساله‌اش است.
ترامپ روز گذشته علناً در صفحه خود نوشت: «اگر فیفا به هر دلیلی حتی به فکر برکناری رئیس خود، جیانی اینفانتینو، بیفتد، مرتکب یک اشتباه بسیار بزرگ خواهد شد.»
🔹
این حمایت رئیس‌جمهور آمریکا درحالی شکل‌گرفته که پروژه برکناری جیانی اینفانتینو هفته گذشته به دلیل طرح فروش جام جهانی به شرکت برادر ترامپ به اتهام سیاسی‌کاری و سوءاستفاده از قدرت فیفا کلید خورد.
🔹
تلگراف گزارش می‌دهد این حمایت علنی رئیس‌جمهور آمریکا، مخالفان اینفانتینو را متحدتر کرده چون به شائبه  «دخالت سیاسی» مهر تأیید زد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/455625" target="_blank">📅 09:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455624">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbWz1kmUv1m4qYMaS9p6LR-IhcVT60o9fRGVBapWCLxoLPU6tv_vNOCQ8BvxF1u5TiCS-c40-2sue9YoXkmnrNzku8l9ZKX0s1ZYqufSGQclX-iPcLi9P7XWM1HNEJ7ImVfY_4z-hBw61K3uivK1hUJyK1Qh-P_An3eE6LkhipOkt-VnAVJ0VxAYcMNwB_4IpC0MoRaXW6s1LKeQy6PDqyz3VAP8ILs3f1atn_T1XlbfniwexgCySZApRwJM8-VPqor-TA08scgzjF9v8mkkY3VV4tvBZjckbIIRpx_d6et19oKnBBexzUoplD8zLZb2NK9xDthj8i2dKUyMM2D3PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوای پایتخت قابل قبول است
🔹
شرکت کنترل کیفیت هوا: شاخص آلودگی هوای تهران بر روی عدد ۸۶ و در وضعیت قابل قبول قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/455624" target="_blank">📅 09:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455623">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqPTOkIORkY2mIYWecbkUMCHo3Co6uPeZ2tnoOfC0lpu512IYTm3cJ1XjHsfq43JU5MB7SZtFItKfzWKvR3W9-Uh7cWdSDWywuDY44piqI0g8tM0lIU65nPB4Fh8lxSeWh6y1vnb1s8y390WXI2gV4kYOODwPmvpxf7L_ZZksRr6hTWsVA4PYuL67cGBEbosmnjCJaZm8Ex0E1wBHSeLrWu6eeb0-U2_0__R4dko-MtmqJ1fU-Lc2yADHwwk9qmhySYb6LfmEDIP6DFCs-EwvlOIflryw-mERYfltrFcP0IbngNsMcCdilYMlTeZtO0tjo5cZpq48GUZM47Ne35Prg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابهاماتی که می‌تواند از کنوانسیون خزر برجام بسازد
🔹
عدم تعیین دقیق سهم ایران در کنوانسیون اکتائو هرچند از سوی وزارت امورخارجه یکی از محاسن این کنوانسیون معرفی می‌شود، اما ابهام موجود در آن می‌تواند آینده این قرارداد را با شک و تردید مواجهه سازد.
🔹
آن چه از صحبت‌های مسئولان وزارت خارجه استنباط می‌شود، این است که «سهم ایران در این کنوانسیون مشخص نشده است.»
🔹
عراقچی در این‌باره گفته: «بحث سهم ایران از دریای خزر در کنوانسیون اصلاً مطرح نیست؛ به دلیل وجود اختلاف در این زمینه، این موضوع به‌طور کامل از متن کنوانسیون کنار گذاشته و به مذاکرات دوجانبه یا سه‌جانبه میان کشورهای ساحلی دریای خزر موکول شد.»
🔹
اما در بررسی متن ۲۴ ماده‌ای این کنوانیسیون هرچند اشاره مستقیمی به تعیین درصد یا سهم کشورها با ذکر عدد نشده است، اما در سازوکار تقسیم بندی به وضوح آمده که آب‌های سرزمینی «تحت حاکمیت» هر کشور از خط مبدا (پایین‌ترین حد جزر در ساحل) تا ۱۵ مایل دریایی، تقریبا ۲۸ کیلومتر تعیین شده است.
🔹
این یعنی ایران از ساحلی که تحت حاکمیت دارد (که حدود ۱۱ درصد کل سواحل احاطه کننده دریای خزر است) تا حدود ۲۸ کیلومتر به داخل دریای خزر، آب سرزمینی دارد و مابقی آب‌های خارجی یا بین المللی محسوب می‌شود.
🔹
در این صورت سهم کشورمان از کل دریای خزر، کمتر از همان ۱۱ درصدی می‌شود که در سال‌های گذشته مورد اعتراض قرار گرفته بود.
🔹
داریوش صفرنژاد استاد دانشگاه و کارشناس مسائل قفقاز در این خصوص می‌گوید: «تصویب کنوانسیون در شرایط فعلی، عملاً سهم ایران را به حدود سه و نیم تا پنج درصد تقلیل می‌دهد و این موضوع با مواضع تاریخی و حقوقی جمهوری اسلامی ایران همخوانی ندارد.»
🔹
شعیب بهمن، کارشناس مسائل بین الملل نیز معتقد است که «تعیین حدود بستر و زیربستر باید پیش از تصویب کنوانسیون انجام شود» چرا که الحاق ایران با ابهامات موجود در این کنوانسیون با تصویب احتمالی مجلس، بعدها می‌تواند «اهرم فشار حقوقی ایران برای دفاع از حقوق خود در مذاکرات آینده را عملاً از بین ببرد‌.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/455623" target="_blank">📅 09:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455622">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c13ebcd55.mp4?token=QLt22AQuNQciKd37mzRFhzUvDqf4t6eBvEZnlsP4Sk-mBi634P9TFeAN4zR1w7ZY-E-bxNtwgtP2I78iPNsudp_i5fcGMN_Zf3UOadV9OkQDp6nYaLH66eHWO_TXlrntspQGpTXZ0hOqzfIcgeVr60Saoo1GgW-OpJ2IpvZ3B1M0agrQsy-0di1F7sYausXGRKqlGJiWOa1WM5Lv-pxWz5-nZAGY9Qz4KtYMuKjS9YZwVpyqc_iD6utVGn0fie4rdb6FHpTqBToGnJkONliUAN0oKPhqD76DURaNFvs0zIkbXFoXr30uhXmAV2w-Xs3A-nE-rYx6PaxqbMDbtPoMag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c13ebcd55.mp4?token=QLt22AQuNQciKd37mzRFhzUvDqf4t6eBvEZnlsP4Sk-mBi634P9TFeAN4zR1w7ZY-E-bxNtwgtP2I78iPNsudp_i5fcGMN_Zf3UOadV9OkQDp6nYaLH66eHWO_TXlrntspQGpTXZ0hOqzfIcgeVr60Saoo1GgW-OpJ2IpvZ3B1M0agrQsy-0di1F7sYausXGRKqlGJiWOa1WM5Lv-pxWz5-nZAGY9Qz4KtYMuKjS9YZwVpyqc_iD6utVGn0fie4rdb6FHpTqBToGnJkONliUAN0oKPhqD76DURaNFvs0zIkbXFoXr30uhXmAV2w-Xs3A-nE-rYx6PaxqbMDbtPoMag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نقش اشعار رهبر شهید انقلاب بر کتیبه‌های عزای حرم امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/455622" target="_blank">📅 09:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455621">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-text">🎥
چگونه پیامبر(ص) را وصف کنیم؟
🎙
استاد عالی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/455621" target="_blank">📅 08:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455620">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6d38210a0.mp4?token=PLlOedxr7L5pi6tlCPZmYEZLuWFGv2RKgRbo0NaU9I0dmEp0e3lgH948I_VCdJvGzQZttBYE847JIWZFh5yt3lvs64L41y50AVR8ySRZOKzTThZCO7ujyewAM3K2NxTcGCuESktOGX2sqKfzLUmcMDKBLrO7pPjPNoXL5zWBeY-Rx6NFJ1jmnhI4Yw9ppOwo6pZbJdIR3AP7ELWQK5kaK-lEUL3Xpo7m0oiyaYGY5_MzZSyETMpwwEwDPcC2Z5HikbD0T0bWQqDvyEN1yt3lh3uacZdoN9k-ITcCotN45juUO7Wg-barbX_07rRjFWOeqMf3S5oazOspVlFUOhl-OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6d38210a0.mp4?token=PLlOedxr7L5pi6tlCPZmYEZLuWFGv2RKgRbo0NaU9I0dmEp0e3lgH948I_VCdJvGzQZttBYE847JIWZFh5yt3lvs64L41y50AVR8ySRZOKzTThZCO7ujyewAM3K2NxTcGCuESktOGX2sqKfzLUmcMDKBLrO7pPjPNoXL5zWBeY-Rx6NFJ1jmnhI4Yw9ppOwo6pZbJdIR3AP7ELWQK5kaK-lEUL3Xpo7m0oiyaYGY5_MzZSyETMpwwEwDPcC2Z5HikbD0T0bWQqDvyEN1yt3lh3uacZdoN9k-ITcCotN45juUO7Wg-barbX_07rRjFWOeqMf3S5oazOspVlFUOhl-OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرکت دسته‌های عزاداری به سمت حرم مطهر رضوی
@Farsna</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/455620" target="_blank">📅 08:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455613">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LdsIEiMmmD3btLjY4RSEgRXkJLSW3GY8gKJY_A8u46L5djS4Cv4X3SK4qlBrpnADA3UuQx_JFGNE5_2_YWNEazkoYL5rRybyLlpVX4WCS7xQ1mUul8rS8ealJmc99On9e4CjR8tg9ePrJKsWGf3AGWlnrlRKAb7BPnKjsyB-7QhC3sWlLutHomsy82Q40OArJAv__ygwQnTnpDI6IbdWGaSQVVEv8YNigYHjUczNbKFDmhxk_u0kA4D6nOO7RVoFyOT8VTgxn3pETPctFaxrkcObxffXaVOhdziih1uYpyGMAef-7E_TxFIma6MqSOIfmUSvzJLyyxmmTV-WhYSPRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FUn3_ZbOka40vLILKKXZrp-Gj6rXLmVE_9SO74bgalBxfyBFUL56bvh57iwahOqOeJzARZ-A7hGTDMxWyzPmZ8LNvK1UM-nRtpbZJ6i-t05PZFJFiw4FfdO9Xr-0WTP2WQ5d97pgrLyoxQfj98kog8CZ5Yp4CRyooC7k5kri7Qui9_FNoaeDwBaTaNEtaLYbkgcUBhEaZ-8yGPqyi6HVwY27e6fK8poEKh9MrcMah-sle4ZOxASLhDE8lBqxeCjyjudf-8hTIg84hEsTrmpBjW-jR4qALFPrDz21y_cVLX0CChabomKk7EBB_GZz9dnic6lSUdf3MIH4nQME_DyCrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CaMsz4dhX_kM-z0_pzvCux_dOjgLmWT3kFjavvWjTHRmPoHceFe6ijNvC56nTPevxii6Ierg-5ZpgjM9dDf1_N2zZMcu4B3cR0Ci5-bfvcXHRdhO2YtMm_wteG6bXNPmSU8ZIR9ps3-nKQE4xBJQr6kL6X9rWo06ZVG_eNIMLGOGASCeWviPoDDGKM2dgKrVoVJB3uqdfdNt8ULoTnNoutW6aeNhJN41i05IXuIfJCZKEtoBUI85O2TgEOrsvbTFbRUMb_t4N1vuOlj1EWqpoQA07kVBLvYwWKuh-f9_UNv6jZhdPBZ_RTqxRmdhBH0KMf6jDSteXZloMaBJ8dv-tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LYkHdl9QhueM9L-8YARBA95swiXu8vXzU7YT0C8a5swl0ErSU6YjQpIRKrDyReoUfCGPB-JXoKqyLKugu4QtWhs9UDAdCGW5_L9HbUZf8qkx4c0N7NeQyVZkSNfWb1MMAQpy4V7fA9cghFLbmgvWpzbWymTkwdDTOfDGvVcezK555rfdY_Ysl-xwufjyE9AlG0J5uSKX6CHGfNEIomYkfaV_h-DB7ApTqBpy3fbZ1YCoUgfWHSEB2rsEEjG9SPp8X9mo_jyexTfD16vgVXsoMFd8H9xNR5aNsMIVE45flb0HJu1FIOFQN6eOG1Lvp9S_U_-_gj7i1Uw_A-6NwW8k0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N3MEvtv1J25uExtNYtyH0EAqlRZy3byLs50JtLNrDQ4tw5pF5lzfWLIh9d1pBFiepw0LsrS_wWgjDLXHimmQLs3SzBVZQGNuLEd8WLU2sTT_2xm6jrFKPxxi11VcGw_Ae5cYW2BQbjY62d6JYeZq9zhvwgf_wMezoTWy-7XhXqxdWTJCse0hd1n2TVPxts-Rf6gHY3Vsh7r2696nUPPlPuXPALq8h96wB8R23IHtJYU56LVu8LKU4oRZxfa_r8sVyp90qZngtwbrgt1zpq6LKOS7sdiJLvY2Av8XLEysJ8qrnUWqjBKSOhUkirIoJ8FgjVHEGj4aOCE88xrj9fFbIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qOC4f6p466to0Mb2PVVjVILAbk0Xn8EYC68kxG-JBA0k2M9ZLF-NZAYGa8FSmaTKp1Zv15Bln0yg9_HQkc67NLHS_i5WaWyZ5VVhFtNKCcJ0-iyCq-T8bPFunCFBBuN4ZGEgREFgemL3I98c06NP4uM7tb-NkcZ3o7BcZyCbNTZFQ5sdZ-cHYS56bwGVZepvaCsRUXm-t44IhFeHBwC3xaUjUYm0PBHfhMzqNJdxx_TgpBIn-oLAu_e7I0B4aNPwiT-ID2arG67qieSowQRqxEGrwF796XWAc7lRxGe05RCUJ8L8eMWhn0D2Rx0wfDOYPz97UDTopRRxMmrvYS8hNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MRSc6FGsy4N5Tw-0Zt2cIwebReU5cV0sahzb33ba7dole18W5SjZ0YCTAgqmbtFQT8xKTtsp3ly3xvXFL7LtfFKflUHVEs34isomLVn-r7YFICgXiq14F5hZZRFvRtA-Ie4IOrXy02Re1EdzuARTfZJUKPfEo4oauU6R0pQ8ts_WjxMV87e2fbplB_ZvxFcqgQV0SeWQu2bY6zl7CZrWUaMc7j6Cjb3Hg70KMgpOhK3WYn8OKYCrbGT1kgkTszI-x6JVznNTQPnK82u1SWiI9npw-gROJgWIstIcA6HwmMlqn0Dxw42dYnx5t2J-fLGOnv50zU_bf-KKWil-Dj_-lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری سنتی بوشهری در سوگ آل‌الله
عکس:
احمدرضا مجیدی
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/455613" target="_blank">📅 08:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455612">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f424ea43a0.mp4?token=JURIgphUtA461trx-Q83i2V6iQDnTlHRihK3MAYXKsLZGOIHq3ywi_LI1_fBIld9VrPVund8g5kZG6xrLQ0f4SmNXorGTtVrIJQ_iJADWakmK5WxFksG79eHwctirnk0zuuoBhtfuNAgq0FuPnGkWbhAW73TaSSF2LhlHjah7-jbw82Ef8QnzWAl63GbVywnVBfRYrVXWQ7V7BqzoCNU_73mi7VNGv-sqxHvt_91eS2vKeZNjK4rUJajR9vNfB9KcIm7esOs-Mnt5suGH-1DzKDndZs5QvKlnuEYjiTwPOzT5Rj5gZG_X02XAhCPQd48MUKzNefAugTyytSH0kQnxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f424ea43a0.mp4?token=JURIgphUtA461trx-Q83i2V6iQDnTlHRihK3MAYXKsLZGOIHq3ywi_LI1_fBIld9VrPVund8g5kZG6xrLQ0f4SmNXorGTtVrIJQ_iJADWakmK5WxFksG79eHwctirnk0zuuoBhtfuNAgq0FuPnGkWbhAW73TaSSF2LhlHjah7-jbw82Ef8QnzWAl63GbVywnVBfRYrVXWQ7V7BqzoCNU_73mi7VNGv-sqxHvt_91eS2vKeZNjK4rUJajR9vNfB9KcIm7esOs-Mnt5suGH-1DzKDndZs5QvKlnuEYjiTwPOzT5Rj5gZG_X02XAhCPQd48MUKzNefAugTyytSH0kQnxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای زائران رضوی در مزار رهبر شهید انقلاب، در شب شهادت رسول اکرم(ص) و امام حسن مجتبی(ع)
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/455612" target="_blank">📅 07:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455611">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGtzEv14OgJMyAMtc82c00J1CSQzemxwyZsDHAOnEtrxuyfK3ZFJQA5C4k4YCNx8O4ISBanb38MsEuxt-Ug0IKRpYFE971c4l6pMl2KRBAgUvY8yRu4wtYdSWgzg_u93wx68DB3UkwOg2XzoHjawFvp1NCZ955ruxBVOG9l9OPbTdDe3PDYRVtiyHD32bRWfXaw3xXJEGxU5zO058muzDy7ioLAT1BbOYQsAoxvMzeJx3PPCuYl9D9u8QS8dVyVrg1BwqUfLPQ4oC5nOZM6v7nULXCj1fBM-jYG8zqNPRDVxQmuMzD4YEhKwk-_KFH_ZWb1OtQZiJrjFPgn5S1s8Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار آبگرفتگی محلی، و سیلاب در حاشیه و بستر رودخانه‌های مازندران
🔹
مدیریت بحران مازندران با اشاره به هشدار سطح زرد هواشناسی اعلام کرد که خانواده‌ها از اسکان و توقف در حاشیه و بستر رودخانه‌ها و مسیرها خودداری کنند.
🔹
همچنین هواشناسی مازندران نیز از احتمال آب‌گرفتگی محلی، جاری شدن روان‌آب و پرآب شدن رودخانه‌ها در پی رگبار باران، وزش باد و رعدوبرق طی ساعات بعدازظهر و شب خبر داد.
🔹
طبق هشدار هواشناسی، کاهش دید، ریزش سنگ، اختلال در تردد و احتمال وقوع صاعقه از پیامدهای این سامانۀ ناپایدار است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/455611" target="_blank">📅 07:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455610">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0rVTdfvMaam09q-4BwIbASB13rGawqqH9vqzgUdapsnwm8GnwJq1mrSlrqc3e-9rZs1OmzCibnjZ-yT40f18FljXrxDwVmyRYhq77SmjsPbRZ2gYJp_evjhHHMSyh5q17isIsPwoB-8lDmmkFz2BRIH-BfNvNNRSmdqaUG56IVXS9XMoSnpyBHLU_yUa6WNEzjrNNu73tL6pcJV7Scv1g-PGMYx1sdGSukc17psgK2h9qeChQVfcGBKU4WgNFQVQ2xN0zjWiEZgo-mfmyDS8UIDbocuSBirGg_gC0-jZhV96rZWg3w_dWMsxv-kTR12sD2i0i7xyjubG3-aCYlInA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخفی‌شدن ترامپ در کامیون حمل غذا سوژه شد
🔹
گزارش‌ها دربارۀ خروج مخفیانۀ ترامپ از ترکیه و جابه‌جایی او با یک کامیون حمل غذا، موجی از شوخی‌های کاربران را در فضای مجازی به‌راه انداخته است.
🔹
روز هشتم ژوئیه (۱۸ خرداد)، پس از برگزاری اجلاس ناتو در ترکیه، رئیس‌جمهور…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/455610" target="_blank">📅 05:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455609">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان
🔹
المیادین گزارش داد که مناطق مختلفی از جنوب لبنان هدف حملات هوایی و توپخانه‌ای ارتش رژیم صهیونیستی قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/455609" target="_blank">📅 05:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455608">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6hTXLOPZ4-fRTsB4lhxYnvQap-xOe1JAPezvYNFnHZZLL2_lsnc4fj1Wz943DoVy4qEvy1AU1b-kiV8tqWM0u8JjSOcgKKOMg0ifn8NYN6Ey-YDTVD7lzElH88TR0sTRU09_5FzajOHepKIANshNHSyJyzpr4smidN7fM7FCKF5583MJclntRuNOeHworFoTlwMMiZWLSTpf0_ob_qmmY6mN3jav9euNjDzCkQsA5kIEKiVx-or-SJ2NvJS3mehV1TXHK7K223dhvZu9KvUDwW3wJbwxbWnC1cIXdZfYB40_hVx3gOrQYMNmOFGN2UxbMlanBxq_SCBl0N4ZImDjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن‌پست به نقل از پنتاگون:
بر اثر حملات آمریکا به یمن در سال ۲۰۲۵، حداقل ۱۵۰ غیرنظامی کشته و ۲۵۰ نفر زخمی شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/455608" target="_blank">📅 05:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455604">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C5ig_xLfdqazfqScuMnYuFNWVbrWdcPn1OLqawisDDPR0WnkAV4K-gdLouSuV1FHiLtae8D7OXNrUnqPsq5LgnqMCkpPVZPaXv2924RpzBrcOgOg3nZugDWC1FoTbHic-nqKp6Y1T197pRhSMEJtmBQnt408d829skpL79QCiNdwsqbfWg3pE-4sX0_tkcI-p6Qb3TwPfV4naMEfViNnJRfV3F5-jG34LpktyLxvnZQGqNPN8NwR2oKt4kyysQ87MrxlJAWVirEnz2NbLOAreIyvCOPwUfJ2mNb7H9Fm_dz8JEwuxlLfoNkUEwULuNbaG6SpCfJ3CvwZJcUcIXaznw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GUFhNEtofi_evHO94QkTnNwNqBL3V0leA2EYfNcIbhs2hxdM31W8l51WJnAT0uzb6u2-fUzjasev1sa8uXJp47DlHzwEN3ljqx-x_1xlOdv8nsvdFZCu5k9epsFW2AFq7VHhwnn9NBDlOU3JrtK2r_LoJYYvzZMNLta6I-T5zL80vfx02N3zeFt3mFGK9GT8Sk8DabkhTe9jEbIaa--hIM8-cX2nvQ7bVPPnWqxOnQKlm4Ac8ww8MspH81jbkItpKhjYxYppqUpmGpAFI5LGUWGK-hbcy43qt12HqijyEKJsiRg8VZL6lfu5wecvYrH9fWWffv2hnksAsGVNvtExLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pfROCUHWzd2cZfTh2EPP8rf0dli4gxKZhUWGBSdxXYPKAkS-dXFXBWRefr6n00_Y-7nvgKRzIz9YOLtOMaaPleoDPuyELTGfhyu221dYE_UcdR6670JzXd3LeBmCQRLwGZJEjWtZXzxus-izo8UK6H4wfAerG2D915YR4aluXvQiRoUiBEqci4V55KmLl0QvbLS_TDBeHv9U4RWkH3zQypFyoFIZzR9aH6PVy3BzaljR1jW9Wp_iTXx4phrfYiQeolzPASmaCta2x9vE8JmazBT-zqGPYKtwMt7GFRDxvwYvxgEtdBZE5g2ZpdYsXh4F745HvyiqSTlRGyYB96wcPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/srB10CMVk05lBlNY59_32Mp_ubaNekTlhMcq_3nv-sV0zHCRzKwwXSd_osj1lHcw8_VD2MM61n1gxC49Tvq3b5hwKAMXXBhSzdiKRcPK_eVT8cFM32lyNxTaE4rJLM-gWT0zDN7Iv0jywnb0OYy4_uCo9QZcaVpVtfVbmVf6mzbpCoqdStRI3TtZ5XjOXgVxU0O7r74AFBONZ33dUcEKHI1yqZVzjZU0m--RJ_6OnPFESgBSA5iUUInEM5Z0ZXh9wdGMWcd2oz-v9oD42SF-f9p2OO3NXjq9NUQL0fAfiUulkUtQJSI40ldaol2WBmxf2__sVyawzIQc_31W3VDs7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مخفی‌شدن ترامپ در کامیون حمل غذا سوژه شد
🔹
گزارش‌ها دربارۀ خروج مخفیانۀ ترامپ از ترکیه و جابه‌جایی او با یک کامیون حمل غذا، موجی از شوخی‌های کاربران را در فضای مجازی به‌راه انداخته است.
🔹
روز هشتم ژوئیه (۱۸ خرداد)، پس از برگزاری اجلاس ناتو در ترکیه، رئیس‌جمهور آمریکا در حالی که کاخ سفید همچنان مدعی بود او با هواپیمای «ایر فورس وان» در حال سفر است، ظاهراً از ترس تهدیدهای ایران بی‌سروصدا و با یک هواپیمای نظامی دیگر این کشور را ترک کرد.
🔹
ترامپ ابتدا در مقابل دوربین‌های خبرنگاران سوار هواپیمای ریاست‌جمهوری «ایر فورس وان» قدیمی‌تر در آنکارا شد، اما بعدتر به‌طور مخفیانه و از طریق یک کامیون خدمات پذیرایی فرودگاه که معمولاً برای بارگیری غذا و سایر تجهیزات مورد استفاده قرار می‌گیرد، به هواپیمایی کوچک‌تر منتقل شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/455604" target="_blank">📅 05:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455603">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49537d50f.mp4?token=cuP5u7Gd00j1REos1fceIozKk-YAPrcusHJOxc77yBOoSOqShWWXQDuXckZicx7ujFZMMXZN5QCiOVAe6kuiZWE3z7NWI-lSqnGVxMhAxBrZaMAuU8FWvNwanwKC7VBoBBxIJkt3RjhW-YKjFwFpCfkBa3ZlAg8BWeUW9Bb07UIUK1G3QdUiBS74QPC45Q7R1-e3aQHSAaFtIRXBVCDLtfdWcI6d9zpuDAe9ffXBcGaPbMfAS01oSo-nrTzf9mJMGFc6E0x793gQkn1dUSE_85vvk5HvjgUMkr3A8CbZm6wS8YpiE1OaU48FBelP7qatJUxrev_Avi--ljx3kvj8pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49537d50f.mp4?token=cuP5u7Gd00j1REos1fceIozKk-YAPrcusHJOxc77yBOoSOqShWWXQDuXckZicx7ujFZMMXZN5QCiOVAe6kuiZWE3z7NWI-lSqnGVxMhAxBrZaMAuU8FWvNwanwKC7VBoBBxIJkt3RjhW-YKjFwFpCfkBa3ZlAg8BWeUW9Bb07UIUK1G3QdUiBS74QPC45Q7R1-e3aQHSAaFtIRXBVCDLtfdWcI6d9zpuDAe9ffXBcGaPbMfAS01oSo-nrTzf9mJMGFc6E0x793gQkn1dUSE_85vvk5HvjgUMkr3A8CbZm6wS8YpiE1OaU48FBelP7qatJUxrev_Avi--ljx3kvj8pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملۀ پهپادی به یک نیروگاه برق در لیبی
🔹
الجزیره گزارش داد که نیروگاه برق الزاویه هدف حملات هواپیماهای بدون سرنشین قرار گرفته است.
🔹
شب گذشته نیز کارخانۀ ترکیب و بسته‌بندی نفت در پالایشگاه «الزاویه» هدف حملۀ پهپادی مجدد قرار گرفته بود.
🔹
هنوز هیچ گروهی مسئولیت حملات پهپادی اخیر به زیرساخت‌های انرژی در الزاویه را برعهده نگرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/455603" target="_blank">📅 05:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455602">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کرۀ شمالی موشک بالستیک آزمایش کرد
🔹
وزارت دفاع ژاپن و ستاد مشترک ارتش کرۀ جنوبی اعلام کردند که حداقل یک فروند موشک بالستیک از منطقۀ «وونسان» در کرۀ شمالی به سمت دریای شرقی شلیک شده است.
🔸
این پرتاب‌های موشکی کرۀ شمالی در حالی انجام شد که قرار است کرۀ جنوبی و آمریکا رزمایش مشترک سالانۀ مهم خود را هفتۀ آینده آغاز کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/455602" target="_blank">📅 03:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455601">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09f0c890df.mp4?token=jXlDhOMMJJPILde7LgDpC8rT9bX3uKpyPFZDZzl-3gsN1hMiyOq90zgSFlmPCkCZDj4gX9hH-_ftuuLb_Gy7x0MKGWLv-0qLue4_XMQ_MDS5AOFi5BNi5rXqfaKvR9JtOGiFFnzFpurKwCPn7zyMtX1ydv0dPKOtPhw7TYW0PgB02OLerlv866nvVwyBdoNeYhsyFpMGtK3ndM2iIXIMSdvhGUP8GHOhM3B8NKIv1d2mp3jbIsDVoG_ht3HmraJUjBYh9OAxAqcklypC6UgOo8-hVTK4EOZCAbydvC_052DUY2_U4IiIYZS5eEeA-m-pSDN4SSvTGENG1saKDJPvOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09f0c890df.mp4?token=jXlDhOMMJJPILde7LgDpC8rT9bX3uKpyPFZDZzl-3gsN1hMiyOq90zgSFlmPCkCZDj4gX9hH-_ftuuLb_Gy7x0MKGWLv-0qLue4_XMQ_MDS5AOFi5BNi5rXqfaKvR9JtOGiFFnzFpurKwCPn7zyMtX1ydv0dPKOtPhw7TYW0PgB02OLerlv866nvVwyBdoNeYhsyFpMGtK3ndM2iIXIMSdvhGUP8GHOhM3B8NKIv1d2mp3jbIsDVoG_ht3HmraJUjBYh9OAxAqcklypC6UgOo8-hVTK4EOZCAbydvC_052DUY2_U4IiIYZS5eEeA-m-pSDN4SSvTGENG1saKDJPvOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دمام‌زنی زائران مشهدالرضا(ع) در خیابان‌های منتهی به حرم مطهر رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/455601" target="_blank">📅 01:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455600">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حملات توپخانه‌ای اسرائیل به مناطقی در غزه
🔹
منابع خبری از حملات ارتش رژیم صهیونیستی به مناطقی از شهر خان‌یونس در جنوب نوار غزه گزارش دادند.
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/455600" target="_blank">📅 01:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455599">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">معاون وزیر کار: نقص اطلاعات فراجا، کالابرگ برخی افراد را قطع کرد
🔹
پیگیری خبرنگار فارس از وزارت رفاه نشان می‌دهد کالابرگ برخی افراد حاضر در کشور به‌‌دلیل ثبت‌نشدن اطلاعات ورود در سامانه فراجا متوقف شده و وزارت رفاه پیگیر اصلاح این اطلاعات است.
🔹
معاون وزیر…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/455599" target="_blank">📅 00:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455598">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4f1ffff9.mp4?token=dEVrZmp6rwcDOxkW5OuHoUk23swhia6RWKq4NA83DGTpMAVeGfZhhVlk01cl3XJMxHvgKEPYSRR4wh2F2n5NIcTMdpU4krMuhAEKaWxgkXfq2Mp25W1fagyBdUxnVwBADcvsNmq6s12HqQBUCN3MTqioVbqpfSPH2j_c0Ce4MCG2NXciUpBi7HTOVaE7RxluroLrWpywT777R9T_p3B6T41WOme1iZPnEtMAuSrMztEd3l-ttizlzPBkhLU2b4LTQDdLKsCqnLGYQxnjXYEMNU6Pg1pO44yn6ecQSqvRzDbJB9sMK3d5Yl88xiWN2J4836SoSuOVf8J47ljt0dFFnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4f1ffff9.mp4?token=dEVrZmp6rwcDOxkW5OuHoUk23swhia6RWKq4NA83DGTpMAVeGfZhhVlk01cl3XJMxHvgKEPYSRR4wh2F2n5NIcTMdpU4krMuhAEKaWxgkXfq2Mp25W1fagyBdUxnVwBADcvsNmq6s12HqQBUCN3MTqioVbqpfSPH2j_c0Ce4MCG2NXciUpBi7HTOVaE7RxluroLrWpywT777R9T_p3B6T41WOme1iZPnEtMAuSrMztEd3l-ttizlzPBkhLU2b4LTQDdLKsCqnLGYQxnjXYEMNU6Pg1pO44yn6ecQSqvRzDbJB9sMK3d5Yl88xiWN2J4836SoSuOVf8J47ljt0dFFnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر صهیونیست: نمی‌گذاریم غزه بازسازی شود
🔹
«گیدئون سعر» وزیر خارجه رژیم صهیونیستی با بیان اینکه یک سال است که غزه بازسازی نشده، گفت که نابودی تمام سلاح‌ها در این باریکه یکی از پیش‌شرط‌ها است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/455598" target="_blank">📅 00:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455597">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1d0f154e7.mp4?token=B6YxqyIwYlVMAfjnNjyatd_6UuoYbXo0KoEivshGu9IIh2ZLVRQnDpiB4VwCGVD1PbnZkeHyMWcEpOmoPibZugwSeIZmQuxG14Lw1jnpMSIRRw9jn1iqXWMRxv1TZZMVg7dSSMn5v2GFgHZ2JrIC7TmmU13DdKHEl2uRFELTtqtqKQmFNa109sarwCB_nOl-WLbsNE4OKfjm7kr2-2nRXis_OXlB2izP-c8cMMm4Dp4d-oUm_UjmH4H73NaV2iYGgItb1O8hzIRgYYxYasE0qhrHlzswEneCHRGhPgT1cWBIDN28AY3wf19Qal6xJeKn4PDWvJH0sUrj-XBnJx29ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1d0f154e7.mp4?token=B6YxqyIwYlVMAfjnNjyatd_6UuoYbXo0KoEivshGu9IIh2ZLVRQnDpiB4VwCGVD1PbnZkeHyMWcEpOmoPibZugwSeIZmQuxG14Lw1jnpMSIRRw9jn1iqXWMRxv1TZZMVg7dSSMn5v2GFgHZ2JrIC7TmmU13DdKHEl2uRFELTtqtqKQmFNa109sarwCB_nOl-WLbsNE4OKfjm7kr2-2nRXis_OXlB2izP-c8cMMm4Dp4d-oUm_UjmH4H73NaV2iYGgItb1O8hzIRgYYxYasE0qhrHlzswEneCHRGhPgT1cWBIDN28AY3wf19Qal6xJeKn4PDWvJH0sUrj-XBnJx29ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع خون‌خواهی دانشجویان مشهدی در جمع زائران امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/455597" target="_blank">📅 00:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455592">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MgFICeFf3Y7PjkECF35iMXqQYfPvPZgMB4vmZt1VguNW0sM8JymYQP6ivIwfmdWy5FcB575FvJp6F-BQfQxjrtKx29DaNlY_seft97sMpdqK3RDpGPjgxe7y57TREkp1-OVP12gxo53vJyJtZCT970nCZaEwwKKxDp12-5HngDwJTm4uJ8-4lYZwemGFauONWRL-Emnuygs334khH6yRJXoy5eZzaE_6lmXZUNhfPRK7V-gSn5RWqXbmnTSrThpKngBy0YUEt_PJg1IKP_d522LpdftYUpf0VK0mnsBl8oV0DJ0jBzGsiX1keLZPeO9rRUhc1yR-Rn_8hFilllevHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hqq5T5foOG1SeIlAiHhwlM2hr12oj-0r4ihLqAhzV9rU2LUpKhmTrKtqckuZaemMZcBJBk6axXaudK5eR5_hR_NDd8v5vNaRYJP4d0yJpNjvS01KGWjDJe9PhwsLQKaYEu5IVfwNSVZ9gnSwekYwY_ld0aBtDEUfckKUX4ylVcubZKeGMYgJoYtzLg6V06WlOzxpH3-sk6HmgrDNcPJigzFG33ui-lz9OjgO2NKMVcTrX_FLSbVJ607iK0nW4kVk9xx9ccB3VynOesYw34IOAMJoupMpLDzZjmquIVy_B1eB7hTR4k_el10C_aMkbSgsJCffjO7eVBFHgqaR6lmHuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sa6NATKFNuWEKfLiOvnoaBXUsAGIAS1H5LrY2EeAfy-E65laSbQeCPYuRloG79WDJqcVAHugwSJYL-dW1PdfbNlmVrCXidvnSjQYMrvz5iTN-BSEPrKcOyIUQA8XbSbIdqr3l5HWDIMqvtP5BvcnF2NXrJd7L9QQUDGxo9Gb0UAb4ZrTJZBDGauOiCmHs7UJH7gpB_FX77yDse-qNyDn3jj-j7GgzPGUNHQGfiVUDPeNYOy_c2sN5ywFfRDeRL0w74sQJFKaB5HQVmo-rLwEeK8n4YlEQnhu34Zd1F-dbW-5bqmMHEvrKIRZW8b_QGNJyXhibvvC2Tewi954S8bHxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kszIISgDrRfgSWbSiP3wl5Wnxcs-W3-DRsERlXrl7dr63dha0xQ4ElxbE-KgMQadxK3wUE_F9pdqlcb-e8d3Xv-iuOrVkrEbYRr053-beTLmnYLR16jWnGWdY4IgAFIeAbGcWisur9vCqyFFm3kprhJO_PdpimJZNAaNN7Q6OHGVk80cLHfxH6wwgJT9gURU-kEcIOw330TR6jIkj_V4YKOIhK7QmOLmms6v4GRgQ06O1XB_IKnplBXbB1-xNstvlVdaIFnlVhqxtcsYuU7-_TuqT4Vj1W__gJhdj1Z3OHnAy7AvHIHVrPcfo4un5LO_Kg6t726OY0M5QQLmltK9cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HbmldwLnbvU4I7JsqqwRPouplqXC6b0Ua49SiVx-km5uRYELRrtsHOtJRAfxy8_BN2Qe5GKGouOgGE3TYCOzEgwkd-PngwqWsmDLWLPiwuPRZRF4pE-lRI5LhIyuMkxoxky4xRK4_Cvh-X0aZjH813bxIpp2KPwzwTTrjUreLDs1spgyIl8ySC3UgnomVqlKqSOTe8g8SH9ovpcNmDL2hG-2xwuGh87ctBucKaTrUUcmbPHkTzi_6wGXa3ahQwCvFsJ3rTeXQSE4qzQ_peSH7OmMUecXvv4_Xkw0uhnsqThbF4wPsrky8lBeLLoV0ozp9GwLgkJzn5O1vnGWcH9l7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حرم مطهر رضوی در شب شهادت پیامبر اکرم(ص) و امام حسن مجتبی(ع)
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/455592" target="_blank">📅 00:15 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
