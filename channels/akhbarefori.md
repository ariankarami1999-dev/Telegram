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
<img src="https://cdn4.telesco.pe/file/CNoGlY32KlQEyH1R07cQGT2ieZH3v4eL2WPNNiE6emna2bPfHvWmFDCqdj7TS7vQmdQdkrqpD516ONQOAePBl4yr3HbYVQRapflXXpMJzM85O1ZfujGbQk2wYrW4Ll-oNpcVJukhSOYYaDT7wa_MhJcwbNRcAJQmiMaVqU0MEvQTGG260z01EnKAiW9FwiZUHiEyPMI7SWHsdErtKZlVOrS7D3grZimzG6I4aXmhOjXVizTmLeesVddA_T1NBRyl5PTNp7NVAb4AGXaockfQipl8qj9mvVBu7e5iKp3DG_WLoQWNzDMl0R9c3dndIShrEpzPthlVK5myFpZji6YV4Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.34M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 15:59:41</div>
<hr>

<div class="tg-post" id="msg-684222">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
سی‌ان‌ان: فشار ترامپ همزمان علیه ایران و کانادا به بن‌بست خورده است
استفان کولینسون، تحلیلگر سی‌ان‌ان:
🔹
ایران پس از شش ماه جنگ همچنان مقاومت کرده و کانادا نیز در برابر فشارهای اقتصادی واشنگتن ایستاده است.
🔹
به گفته او، مشکل ترامپ این است که فشار آمریکا می‌تواند همان‌قدر که به طرف مقابل آسیب می‌زند، برای خود واشنگتن نیز هزینه ایجاد کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6 · <a href="https://t.me/akhbarefori/684222" target="_blank">📅 15:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684221">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwywlUx94n7PmPHiULIvuh-0y0-da5AgHbZBj98d1IUfPF14SoaW6h8ZTtajI2OzX3LE9Gi6qN3SyEVRWPrLzbmfz0g8J4BuR9ksUw9D8qqZccxcMVkWIuJ_YV2v52DLJqPF8CN1Be-vT40RWoJEpr36lwLNI_mLCMDiXfC4rmzE5ACVngXfzAZEKBA-0w19VckaJFjo-18AI7cpRLXZtQFVslT9hxON-AtLuhyvLi--fsUv6Wzp_Eut5L67VQ0GU5r5JqaoJ7i-aD6tziR2j240ICgaGeGAkr52NbiorUI5o5BEUY-OmqL79m0NAwv1bw5v9JkZGp3mXTr8IT0xVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سیدابراهیم سقزی درگذشت
خانه موسیقی:
🔹
سیدابراهیم اسماعیل‌زاده مشهور به سید ابراهیم سقزی ـ خواننده اهل کردستان ـ پس از سال‌ها تحمل بیماری درگذشت.
#اخبار_کردستان
در فضای مجازی
👇
@Akhbarkordestan</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/akhbarefori/684221" target="_blank">📅 15:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684220">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnrDbjQTdtd3dxRzZ8q8LuEMa2sjAHKw6R56MEz5uVgH9ZGvVafQUAbz663VZaVr9jooI0YCunvEOkVn3mBSCTf171bA1tTOFEPF8elqPvI50MgI8DIm4KFC3j04I9wQhgkvJuVZziw8Bu1N8_yHuFRb6g7ETBmpLPRkgvlQzfTsU9Pru4__psx9TAf9Qx9-SIB-hqKozEqs6jNte_8ZCfTnm4NgZ0sXbeJqNJagRikBjcELU_wHpXOQKhRayyd1dftbWOx9yhWcjqDD9pu-XGRdCEykQ11I4TLDgw_ZAOQyAIryaFTWFRTrsDcSH611OUgr7eCd-35QpyhhV9_C_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۶ کاری که ممکنه باتری گوشیت رو نابود کنه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/akhbarefori/684220" target="_blank">📅 15:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684219">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5w6WHICnO3ZIdSA0kKPcdh7-SFHPR9PXQ8qnKjNRMPc368CLL5hvzR-gsHSbmEoNB8cezl3P4LT7x0NpWjC9G2G_eFDjTnb_kUoBcCU24CYBcf2gsrRmYoHWgkjPogzWpgeilZcvKW6FK1lXIkNWxHcyuH6jmPtwwTKYuE8reJqt6gsnSp3ySBRjSe2cmaDJZ6ee33fsJglk6HTPIzqimJQ41U_Yc2WV5bsK3PTnBziC7zoXAkSljaM7OXb0_W2q-iY7okavXuCCQcQ8e8_P1llbQFrGxUx8u-TNP9fjL3rXkzhnLY64qVzj0MWzZRPBBxtAprg9KA2_IG6iJ5QCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بزرگ‌ترین عرضه تویوتا توسط هماتلکام در ۴۸ ساعت به پایان رسید
🔹
عرضه ۷ مدل از خودروهای تویوتا توسط هماتلکام با استقبال گسترده بازار همراه شد و در کمتر از ۴۸ ساعت به پایان رسید. این خودروها در سه کلاس سدان، کراس‌اوور و SUV و در سطوح قیمتی مختلف عرضه شدند.
🔹
در جریان این عرضه، بیش از ۴ میلیون بازدید از محتواهای مرتبط و صفحات فروش ثبت شد و بیش از ۲۳۰۰ تماس با کال‌سنتر هماتلکام انجام گرفت. همچنین اختلال کوتاه‌مدت سایت در زمان اوج استقبال، در سریع‌ترین زمان برطرف و برای کاربران اطلاع‌رسانی شد.
🔹
هیوا میرزایی، معاون بازاریابی و روابط عمومی هماتلکام، این استقبال را نشانه افزایش تقاضا برای خودروهای تویوتا دانست و از توسعه سبد محصولات و اضافه‌شدن برندهای جدید خبر داد. هماتلکام همچنین تأکید کرده عرضه خودروها تنها در صورت موجود بودن خودرو در ایران انجام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/akhbarefori/684219" target="_blank">📅 15:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684218">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jviRSZaR3VmgeluuCiYS4zb_T0N5gqAzvCbQV2rCkK9K8-yxS_OV78LQQkYpptV-O0jPPHKcAiJy2vgL5JcD5P_RXYvk1lcyoVkwLEUHElZh7HkKbRtMW3CQ4KXmzPFiP0V1EgrXTaqX9uWMlsl6MY5N2T-cKCDgMqhIUW2jGIBwedMqbt1K79A-yNowWv2hcxOHBWNGSwmDR8K913lbsCJfmNZSuFRa0JFud0v5LA2kMHmlmlo8_POggRw26T5sYUmp5CAW3xZPmQ4962S4K867P-qV65ODuHqS05rv7t4BPRVS0S6E_4X9b75m3U6ZtoaF0zeWC8ta_AL8Q0JCHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت کاهشی شد و به ۸۹ دلار رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/684218" target="_blank">📅 15:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684217">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
قطر: تلاش‌های ما برای بازگشت ایران و آمریکا به مذاکرات، ادامه دارد.
🔹
عراقچی با همتای عمانی خود در تهران دیدار و گفتگو کرد.
🔹
وزیر امور خارجه سابق آمریکا: نتانیاهو نه فقط در آمریکا، بلکه در سراسر جهان به اسرائیل آسیب زده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/684217" target="_blank">📅 15:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684216">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7e9fc883c9.mp4?token=hInm5-yeHjEpKeW2VYhcZSBFCU60KSxIlKfJLHsTLtudGitbkBlyQp5BD1FNiKvrRQEhN6H2BJrtO6cqn3y_QpoZDfKMwMO8RvsbRTkLFiIlwwj1DrSbkc7cs4T4Ic7o0HvxwcbrtAU3HsyncRypBZWfzeo8ysvyWPuIG2fEc3FG5CNgueVfITg4ldRAC6h5BZbbtNCiPtZzPmkj_Xax1SvEKpR8-9VGDSexco2T711dxjvYanrVdmfzy7ubWfZ1mC2E6tFs0oFhehNPZEWBm4ssHS4qDISjNpjbGzbForf6L53YTuT3-Oqve5W3ot4sqMZ3bQGRZwXZvNZkRSSvyAcLpJTeB4I7YC3J4vyDeoxrkxIoydHWCyck5qixNtG1-20TBseKLk28S-DgC86UEooIOuFto-aUXaNTLXocGFnMa-uAciXTcLilu2VGVSuJ06CtCybaHz34SNlSCcwMe9dj0Nv4hsTXrdXTjzN-GdLbFFv4r0LtBRF0kMOlU1X55CLGOVpuyGxRwSN35M91qGdGZc_4DmlDkM9ZLCp4UzKn4XhNJZMsnVwFw1f3fBwY_-Bq2OC8Plqb_2VQF_GzHXcCzcjbIMwQlpZLHRNGfUZAZyLGAHjWaYt5LYajdLv1JxMMfw8j0fd_faNkzt97RjNlQNeiinRRCQN82Vc3Dek" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7e9fc883c9.mp4?token=hInm5-yeHjEpKeW2VYhcZSBFCU60KSxIlKfJLHsTLtudGitbkBlyQp5BD1FNiKvrRQEhN6H2BJrtO6cqn3y_QpoZDfKMwMO8RvsbRTkLFiIlwwj1DrSbkc7cs4T4Ic7o0HvxwcbrtAU3HsyncRypBZWfzeo8ysvyWPuIG2fEc3FG5CNgueVfITg4ldRAC6h5BZbbtNCiPtZzPmkj_Xax1SvEKpR8-9VGDSexco2T711dxjvYanrVdmfzy7ubWfZ1mC2E6tFs0oFhehNPZEWBm4ssHS4qDISjNpjbGzbForf6L53YTuT3-Oqve5W3ot4sqMZ3bQGRZwXZvNZkRSSvyAcLpJTeB4I7YC3J4vyDeoxrkxIoydHWCyck5qixNtG1-20TBseKLk28S-DgC86UEooIOuFto-aUXaNTLXocGFnMa-uAciXTcLilu2VGVSuJ06CtCybaHz34SNlSCcwMe9dj0Nv4hsTXrdXTjzN-GdLbFFv4r0LtBRF0kMOlU1X55CLGOVpuyGxRwSN35M91qGdGZc_4DmlDkM9ZLCp4UzKn4XhNJZMsnVwFw1f3fBwY_-Bq2OC8Plqb_2VQF_GzHXcCzcjbIMwQlpZLHRNGfUZAZyLGAHjWaYt5LYajdLv1JxMMfw8j0fd_faNkzt97RjNlQNeiinRRCQN82Vc3Dek" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مراقب باشید! آن‌ها با «قانون» به شما حمله می‌کنند!
🔹
آنچه امروز پلیس آگاهی از آن پرده برداشت، یک کلاهبرداری ساده نبود؛ بلکه یک «جنگ روانی و حقوقی» بود!
🔹
اعضای این باند، با لباسی از جنسِ قراردادهای رسمی، به دنبال خودرو نبودند؛ آن‌ها به دنبال «خونِ پس‌انداز» مردم بودند!
🔹
ترفند آن‌ها ترسناک است: آن‌ها با تظاهر به مشتری بودن، شما را در تله‌ی قراردادهای «حق فسخ» گرفتار می‌کنند؛ جایی که شما با امضای یک کاغذ، در واقع دارید اجازه می‌دهید جیب‌تان را تا آخرین ریال تخلیه کنند!
@Tv_Fori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/684216" target="_blank">📅 15:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684212">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q45kwsRgofpKZs3k-ixUtxwEhCW9vjryPB4aWhhPEX9lHmmza939uGEW7EvUEl3JlOCOA07su0GwSx-9IeqTwj_rFayM_m4kD3cBHatNnEQWNoCmhFc8l4PaOrrnijb4rfxzyaONaBadmMITzNXxYm4G7HkGMsQd4XoPjd4kZUEoKOuObFJFEoPjVg_pTMJ3mxl4GQ2XJgakOggBYd44wfmVcFS5BVmqzQ7tDzO4TEhtLbqZV_uuIWin_-w1n0l3mPHSZKssTSGzqA6xq65E62btbdet34XrJe49aUIMWApktM_886DrV9IbOXloUJPEEJqAiSCYh7K7N1gtlGalQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XL5mQhIC7nlOgGP6It6afKwHGf5Q57kOYPZdQU3bE5CH_unQ8r8VlI_fnzkkVYcyEQFV3IPw-8f91nmGd33YFoPfq4fOLjHWX3ptKb5Br5WfZb5waboRyaFmBl9ntkU4yTCj8ImIgtHeZEeuDwRAhAZ5Tly0l-ZkL9crw8Qqog7dc3wPw2hwBiEbBWL8Q_ZYipkVLdZJOy41ce91UF1nD37Vgm1nOb0cvDjK8qQGaxTeYp6nBfK3UP21RIPYMIqPfpqqIDo2yKEUOzdj_sX9EWt1D2TpeRznrFEJpuRz8f1xW4lw6mdxL82uHJX83OsEdGi-C3Zh9JHpLxSGXDRLeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DjZ4p9Q3T5TcB9cPwMKQikxyBuyxRZyGS8-d0mOPLEJnoKs3P85N5ksk_VkwDU3aY5MhADX3rOW50zHfGs_AdH9EhtDTOkwuOp1Q-ui5Th_wyFAemC__4Xv_1JUpknie4exMKTNfGfzUzyuhxMt5jg-bp0moeP6bSmxWLuM_x0A2u5qV-WhoohnJ3MD23aQ2K3PVP33ZCGhkA4goD1yuQ6M9WlDc5XMpbnlTa36FNjXmFlJB4lHDkL7Jhbj0pcVEAsA7l-tXugZQwgT5G962zMuJBZWToJn174zlj56d3zd-IMSKfs1JwgBQg8MVXhydqv7GUGoC3bRh1Ln72eLxLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QsXW7cgUVvktP475A1m5Qv8uzGmbJSb--0YvvXIVkhnKvgXToWRdSu4Jzr-pW2bu9nffslrpS5P7rQWO1j524VPtUmQnpVCKpFaIpS_k2BiCSGzDvFJ90wBBXKWxP5yUG4Vw8V3fDP2kSTO_VbCov90OuhKZAFTWdfcFpBd1ZFwrQ9bOiD24HpjoEPCgOlRbCeewa2hmLAqW5Bz-RKzwdDQtuOMYxF_Vxq-SkzBqXWlEZc2cTmN3puvHPTsWjXrMjFAYBDqcQw7bH-WKKoD6VmdeUEeFmcvYR84M0lP7JhSNIA_rTmfu0x9_fIgap5bvtg9a-IyujON-COrLtwELDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
استفاده از گوش‌پاک‌کن بیشتر از این که بهداشتی باشه به سلامت گوش‌مون آسیب می‌زنه #حواست_هست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/684212" target="_blank">📅 15:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684211">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3X0qHFAC88rbXSXQOg6dI9Ro9y0dYTVYVTbIVlfA1d9hiiI-0HReMV8d8gNMHNm54Xa8QfcYRipUNqxF-ioDFVsy_WfWEv3pUaAQ8pkIcC9BKzOak3kFbdAV4Zwi88-Onqo5bmWM4Vs6QxWlm5-039TXPNCaXokBN_sMwlh0WfE8lf0Krxo982XNi27vZ-AjgZsyxDg5U9wDc8wvmp417bB2SG5ZQdv0JtUq5NgMCeEEB9sUL7SiBtYNKM3EfAkqGnvRrI37KzEYxCLeSB5m6iHs5JMLoKeR4w2_C-LFLO0XaSPOcQvebYictTInYhxak_LlPe0HavLsj54l90asw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از ظرفیت‌های علمی تا حکمرانی نوین؛ مأموریت معاون علمی در کرمانشاه
🔹
معاون علمی، فناوری و اقتصاد دانش‌بنیان رئیس‌جمهور در جریان سفر به کرمانشاه، از پارک علم و فناوری استان و شرکت‌های دانش‌بنیان مستقر در برج فناوری بازدید کرد.
🔹
حسین افشین در این بازدید ضمن آشنایی با ظرفیت‌ها و توانمندی‌های شرکت‌های فناور، در جریان مسائل، فرصت‌ها و قابلیت‌های موجود در زیست‌بوم علم و فناوری استان قرار گرفت.
🔹
شناسایی ظرفیت‌های علمی و فناورانه کرمانشاه، تقویت ارتباط میان بازیگران زیست‌بوم نوآوری، حمایت از شرکت‌های دانش‌بنیان و ایجاد زمینه برای نقش‌آفرینی مؤثرتر ظرفیت‌های بومی در اقتصاد دانش‌بنیان، از اهداف این سفر است.
🔹
این برنامه همزمان با هفته دولت و در چارچوب رویکرد معاونت علمی برای توسعه زیست‌بوم نوآوری و حرکت به سمت معماری نوین حکمرانی علم و فناوری در کشور دنبال می‌شود.
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/684211" target="_blank">📅 15:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684210">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iz1gwEyuyrXP1AB0qozsq2Pvn2gwnl7gxHdrrM2ehDeKrlzlrgwq4ju4-67y9kqQYlAEGDQQET-RTXu_MZ5Yc4fusi_cbTXAmMzz02IZ3OLYvGviiI2kZzwtgD3a-BUoR4c4_19fFwYqv49wLE9z-eR7yHg5AaoZv9BbM0X2PTJ0V_rCGeBD5AFQhYnocQlkWFcwnaHP-iU9WBPzaTr9K5wtSQuptpygXXXAWZei2-IUoVsiuz9-9OkEEAei_sgvGbAHw5Ip3uTIZ6ckvAlft2WLmFmCe5pEnbpfl56SWDPmwRx8GrR2Erdt7-H9tJRUAFA1jsOFkTkTkQZpLqV1Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
واگذاری سهام «سیمان تجارت مهریز» در فرابورس
⬅️
نشست خبری معرفی سهام شرکت «گروه صنعتی و معدنی سیمان تجارت مهریز» با نماد «سمهریز»، با حضور مدیران شرکت و خبرنگاران بازار سرمایه در فرابورس ایران برگزار شد. این شرکت در راستای سیاست‌های دولت در زمینه واگذاری بنگاه‌ها، توسعه نقش بازار سرمایه و مولدسازی دارایی‌ها، در فرابورس ایران عرضه خواهد شد.
⬅️
مدیرعامل شرکت با اشاره به ترکیب سهامداران، برنقش کلیدی بانک تجارت به‌عنوان سهامدار عمده تاکید کرد.
🔗
مشروح خبر
👉
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/684210" target="_blank">📅 14:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684209">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
ترامپ دوباره توهم زد؛ ایران حقوق نظامیانش را نمی‌دهد
رئیس دولت تروریستی آمریکا:
🔹
ایران حقوق بخش عمده‌ای از ارتش خود را نمی‌دهد؛ وی مدعی شد که ایران دچار یک بحران انسانی است که باید متوقف شود.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/684209" target="_blank">📅 14:56 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684208">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
جزئیات نسخه تازه مصوبه مجلس
🔹
بر اساس ماده‌ی ۱۵، همه‌ی اشخاص حقیقی و حقوقی ۳ ماه فرصت دارند تا فعالیت‌ها، قراردادها و ارتباطات جاری خود با کشورهای خارجی را با سازوکار جدید تطبیق داده و در سامانه شفاف کنند.
🔹
تولید اثر هنری بدون مجوز از نهادهای قانونی کشور،…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/684208" target="_blank">📅 14:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684207">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سارقی که گردنبند دزدی را ۱۰۰ میلیون قمار کرد
🔹
در این ویدئو روایت پیرزن مالباخته از شب حادثه و اظهارات عجیب سارق دستگیرشده  را در
#گفتگو
با خبرفوری ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/684207" target="_blank">📅 14:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684205">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUU0dI7OZ5NZ91cCc6h3G5u2YbSKJ3rArVjwXDc3xuujV9vw_qmSbFZ4u_6U9dKVvEVQPqc3-Lez2_Ermwx84vh9Az4oI535QgBfSnidzlFcvxpWbpQconpeJV44Zhs80oS-2FkyEiSI-rc7RHm1EOFS7A__DV1Q0gljLS0PL_TiQ4e82A2a30wkfY2o1xz3TsGQsdLzThTeRNw3Tykx-czawxtRk1NzoaJY1-SB59iHnWfSsYPHoxo4UwrIU4mURUxLx2KWqbwtvHw1P2VOuCOvwRTEpyn6nwTWGH7Jx8mdQ04dlhA0gfV8BsPZpNKMK3USwjyRfox7b5I-rK9cng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ونس، معاون ترامپ: باید به یاد داشته باشیم که کانادا یک ایالت... ببخشید، یک لغزش فرویدی بود؛ واقعاً اشتباه لفظی بود؛ کانادا یک کشور است!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/684205" target="_blank">📅 14:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684203">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEIwhkpEl3PVzz8PGd8zs9e5Qw4SotXbL3qWGJvdRKMiZ_bPtpofuwFLzxHxbUi6HkkC5RsNQ0x7WC6SgVNtbwOVQzpn_M3Ac12CzoRpMVVmwKqNRiSf606z1JS1Dv6lEjGPPLAvjVnK1HnWNkCoyg3jerHEqJSwsOsVjBD1cttmK_hCwhdalSzgAuo2fSauGDmuhQBIe7YmMkaSEUMz1KMc3Jaz-Umcc4gvG8JeEayO-2EmZS-a3L5IdCT7XQxkX_qDER6jKHLBzOo8aefnzw9ZEA2y70wJRGmdDmdyOBqj2yuKTHNsm1WtWhGlaw3NeWd6dRviHouWul1KXdDSAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاکسی‌های برقی بابک زنجانی به آبادان و خرمشهر رسید
🔹
فارغ از تمام حواشی، پرونده‌های متعدد و دیدگاه‌های متفاوتی که حول عملکرد بابک زنجانی وجود دارد، راه‌اندازی ناوگان تاکسی‌های‌برقی دات‌وان تریپ در منطقه آزاد اروند را باید یک تحول کارآمد زیرساختی برای مردم جنوب کشور قلمداد کرد.
🔹
شهروندان خرمشهر و آبادان که سال‌ها با دشواری‌های رفت‌وآمد شهری در گرمای طاقت‌فرسا و فرسودگی وسایل حمل‌ونقل دست‌وپنجه نرم کرده‌اند، اکنون فارغ از کشمکش‌های رسانه‌ای، ذینفعان اصلی یک ناوگان هوشمند و پاک هستند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/684203" target="_blank">📅 14:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684202">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما مهم‌ترین دلیل کاهش استقبال از سالن‌های سینما و تئاتر چیست؟</h4>
<ul>
<li>✓ کیفیت پایین آثار</li>
<li>✓ عدم تنوع ژانرها</li>
<li>✓ افزایش قیمت بلیت</li>
<li>✓ رونق شبکه‌های نمایش خانگی</li>
<li>✓ ضعف اطلاع‌رسانی</li>
<li>✓ سایر موارد</li>
</ul>
</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/684202" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684201">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
مدیریت هدفمند عرضه ارز، بازار دلار را تعدیل کرد
🔹
بانک مرکزی با تنظیم هوشمندانه عرضه ارز و پاسخ‌گویی به نیازهای واقعی اقتصاد، روند بازار دلار را به سمت ثبات و کاهش نوسانات هدایت کرد.
🔹
این اقدام در راستای کنترل تقاضای غیرمولد، تقویت آرامش بازار و صیانت از منابع ارزی کشور انجام شده است.
🔹
تأمین ارز کالاهای اساسی، مواد اولیه تولید و نیازهای ضروری همچنان با اولویت در دستور کار بانک مرکزی قرار دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/684201" target="_blank">📅 14:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684200">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNByrrhWdEe-JRD4s7ZhQr9C4PCsdfuFDtNr9uESDlFYXf9KOouBpSPR4qLYsAq0aWwu37RJi0trSUUU5GHsTYAKQg5JdwASEONka2lb-3KVPqAaabn9p_3jpkkn3GJjeXIy67RLmv0PmZiKOn0-ZDmDUXhvkRC75JArKanXl7tqv0YeVvPdT0ueLxqC8KG0FEJAmV1KPuXJVkrQqmCp_pLUzAmkice_Jc5Ht-fMLjK4_n3Wx9g06KEU2AlgYL3c5gYMv1UH30CNnC648p_hXROe3D3O5hZq93cahXmuVm_hybu0Hc-2ofSikA_aYISx3d58sTeZI1zz7sFl6vHMZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بسنت: هیچ‌کس از تحریم‌های آمریکا علیه ایران در امان نیست  وزیر خزانه‌داری آمریکا، درباره چین و ایران:
🔹
می‌خواهیم امروز به‌صراحت اعلام کنیم که هیچ‌کس خارج از دسترس تحریم‌های آمریکا نیست. هر فرد یا نهادی که معاملات را تسهیل کند و بخشی از شبکه‌ای باشد که نفت…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/684200" target="_blank">📅 14:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684199">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
قاچاقچیان مسلح سلاح در سیستان و بلوچستان زمین‌گیر شدند
🔹
مرزداران استان سیستان وبلوچستان از قصد قاچاقچیان مسلح برای انتقال محموله سلاح غیرمجاز به داخل کشور مطلع شده و در جریان یک عملیات، با قاچاقچیان مسلح درگیر شده و موفق شدند ۲۲ قبضه سلاح کلت کمری، ۴ قبضه سلاح شکاری، ۲ قبضه نارنجک دستی و ۱۳ تیغه خشاب را کشف کنند.
🔹
قاچاقچیان با استفاده از شرایط جغرافیایی منطقه از محل دور شدند و تلاش برای شناسایی و دستگیری آنان همچنان ادامه دارد.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/684199" target="_blank">📅 14:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684198">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e71e6b12e.mp4?token=QI5KuqpgJa2G9p1yTtVlzYKRXes1i5g7W2Eoe0StNYqO4YR2QXfAc7UNhI33zCfxDlHlt0tMe4C4-r5McS6rQJIZ8cFRm2u7qnWsM_4AaQPJ_7bNufnuHNjG12ItyQFhS4KbJTOulp7CTV4x6l1NlbzEA5SmmsPk0v-fkdUbhaGYKVlwZ2svbYMsHjHhjffXeWYJ0F1CLy7y0tqXul5r4PtrMhgnAqZYlUqIMFyYfIIlT-j1eA1AE1RVxpQBr73hDzmH1mJnlTJuNV9YNh9ByJKAeK0hW3kJtIOupWjnG4mVdTasH_ueU8ABESv_mJlzg0M9JQJeTYtvlnLTRT4Lpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e71e6b12e.mp4?token=QI5KuqpgJa2G9p1yTtVlzYKRXes1i5g7W2Eoe0StNYqO4YR2QXfAc7UNhI33zCfxDlHlt0tMe4C4-r5McS6rQJIZ8cFRm2u7qnWsM_4AaQPJ_7bNufnuHNjG12ItyQFhS4KbJTOulp7CTV4x6l1NlbzEA5SmmsPk0v-fkdUbhaGYKVlwZ2svbYMsHjHhjffXeWYJ0F1CLy7y0tqXul5r4PtrMhgnAqZYlUqIMFyYfIIlT-j1eA1AE1RVxpQBr73hDzmH1mJnlTJuNV9YNh9ByJKAeK0hW3kJtIOupWjnG4mVdTasH_ueU8ABESv_mJlzg0M9JQJeTYtvlnLTRT4Lpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فقط با یک بشقاب و سوزن، مدل لباس‌های قدیمی‌ رو‌ عوض کن و لذت ببر #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/684198" target="_blank">📅 14:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684197">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: آمریکا دیپلمات‌هایش را به خاورمیانه بازمی‌گرداند
🔹
بر اساس یک سند داخلی وزارت خارجه آمریکا، بازگشت دیپلمات‌های این کشور به سفار‌تخانه‌های آن در منطقه که در جریان جنگ علیه ایران تخلیه شدند، ممکن است از همین هفته آغاز شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/684197" target="_blank">📅 14:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684196">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
سامانه امداد تجار اتاق تهران؛ همراه هوشمند کسب‌وکارها
🔺
اتاق تهران با راه‌اندازی سامانه «امداد تجار»، بستری غیرحضوری و شفاف برای ثبت، پیگیری و رفع چالش‌های کسب‌وکارها فراهم کرده است. فعالان اقتصادی می‌توانند مشکلات خود را ثبت و از حمایت‌های قانونی و بسته‌های حمایتی دولت مطلع شوند.
👈🏻
کسب اطلاعات بیشتر: ۱۸۶۶ و
https://digitalchamber.ir/emdad</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/684196" target="_blank">📅 14:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684195">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjjVIc76rCFyJzwZWkU76a26EFuIr6kEnu8njIYSBfmCjPr0xGa1WMV8SY00WDDxz1taM4AeQ_JEej8K12WYL2cgn9RA0vtPj2PTiHkaR_ZoEmKKa1Bo2fCvn5WG55txuh0UjJU-nP1LQ027VDBa9_0FrIhHkAa7X19sD3S0_BVJcbrcIXDOw6qyQMS86EgYJQL8YJLJqlkE-qYDUuy-ZvrCUVlBiBQDaPaCBOGuVPfnCw2pePiaJewzngXJ4z3GO88Lp7pNi_MdMOPKRJRWAU3JtFR1HSnxGS4rIE61VElFWQMHB8EIyQuKZ2XmWEmBSvTyKk2UKblcXmhKiaPr1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به اطلاع میرساند شرکت توسعه منابع آب و نیروی ایران قصد دارد ۵۷ دستگاه ماشین‌آلات راهسازی و سنگین خود(شامل انواع جرثقیل، تراک میکسر، کامیون، دامپتراک، بولدوزر، لودر، غلتک، بیل مکانیکی،‌ پمپ بتن هوایی، بونکر سیمان، تانکر آب، تانکر سوخت و...) را از طریق مزایده عمومی به فروش برساند.
🔹
مهلت دریافت اسناد:
1405/06/11
🔹
اطلاعات تکمیلی در سامانه ستاد به آدرس
www.setadiran.ir
بارگذاری شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/684195" target="_blank">📅 13:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684194">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ادعای الحدث: فرمانده ارتش پاکستان به ایران پیشنهاد توقف محاصره دریایی و لغو تحریم‌ها را بر اساس تفاهم‌نامه ارائه کرده است  الحدث به نقل از منابع آگاه:
🔹
واشنگتن در ازای توقف حملات گروه‌های نیابتی ایران، پیشنهاد توقف محاصره دریایی و لغو تحریم‌ها علیه ایران…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/684194" target="_blank">📅 13:56 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684193">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سرلشکر محسن رضایی: آمریکا در آینده منطقه جایگاهی نخواهد داشت.
🔹
معاون وزیر آموزش‌وپرورش: شهریه‌های اضافی مدارس غیردولتی باید به اولیا بازگردانده شود.
🔹
ثبت‌نام پذیرفته‌شدگان دکتری پیام نور از ۷ شهریور آغاز می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/684193" target="_blank">📅 13:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684192">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a712ce05a.mp4?token=bukpgLbnLEMcP5EPbCF51ADILIZ0arZ6euRZSP6QK0vAmjLV8dcRO9ratbEOShGHePu4GPM0WIUEJiyHjPskq4HbJjBtObQhiCYXyqJxlt7_A7chaiTQ2pdYJM8bDD4S7Gn_gqsO6BQUKdVTXZU2ZzRnYl8lWD-Wx3l2AdknBdvNw2ouPwwDhnyRzGmtCYS5T6zmaXJaMf2ZkwqXS6d4tIy49K--CRUCnCjOWB8o5tEd15kZRXWBQBUoLT7m3RYpJHY98_faMQdHzBQY_rGKZUUtW7oVdGmDlFMqX15VWZFoLjmfZ9Np9C3GHWqyrC-WOYWhyYef_3QfLJjF0vvisg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a712ce05a.mp4?token=bukpgLbnLEMcP5EPbCF51ADILIZ0arZ6euRZSP6QK0vAmjLV8dcRO9ratbEOShGHePu4GPM0WIUEJiyHjPskq4HbJjBtObQhiCYXyqJxlt7_A7chaiTQ2pdYJM8bDD4S7Gn_gqsO6BQUKdVTXZU2ZzRnYl8lWD-Wx3l2AdknBdvNw2ouPwwDhnyRzGmtCYS5T6zmaXJaMf2ZkwqXS6d4tIy49K--CRUCnCjOWB8o5tEd15kZRXWBQBUoLT7m3RYpJHY98_faMQdHzBQY_rGKZUUtW7oVdGmDlFMqX15VWZFoLjmfZ9Np9C3GHWqyrC-WOYWhyYef_3QfLJjF0vvisg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا اواسط هفته آینده موبایل های کشف شده به دست مال‌باختگان می رسد
سردار عباسعلی محمدیان، فرمانده انتظامی تهران بزرگ در
#گفتگو
با خبرفوری:
🔹
ما قول می‌دهیم تا اواسط هفته آینده تمام موبایل‌هایی که کشف شده به دست مالباخته ها برسد.
🔹
وقتی میلیون‌ها تلفن همراه با قیمت بالا در اختیار مردم است و در استفاده از آن دقت نمی‌کنیم، سارق به سمت سرقت وسوسه میشود.
🔹
دوربین‌های سطح شهر می‌تواند به ما برای شناسایی سارق کمک کند.
🔹
اگر زمانی ناخواسته با سارقی مواجه شدید حداقل خوب ببینید و خوب توصیف کنید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/684192" target="_blank">📅 13:49 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684189">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
حالا زن در خانه چه کاره‌ است؟
🔹
زن هوا و بوی خوش خانواده است؛ یعنی حضور زن در خانه آن حضوریست که علاوه بر خودش، برای خانواده هم مهم و حیاتی‌ست و اصلا بدون این حضور، خانواده به معنای واقعی وجود نخواهد داشت.
🔹
«المَراَةُ الرَیحانَهةُ و لَیسَت بِقَهرَمانَة»…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/684189" target="_blank">📅 13:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684188">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O66qR8lvdOy-N68suNRscWIOe89WLvT5tjelFFUAC1VXwVvxHDjGq_n_osPV62LAvYsMqFeKz-1P6UBVUCfVANpMNydKH5U6OvUop5NSMV41-bxwsWV5I-P2fIFLEe1XjnD-HDp_NFFQU9ukvXiRhbwtASfB0YL4bbNouvWAA2AlrhQ6gWl1dbv49iuPDYBPt7kViCqQkY6rYTrnDjY6OPEFlU34PfRs3mw-67tKQa1aVf-o6EMupyALrK2HamFrChp2jRKNjbOjQ--dlW8DNEKYvWWO71NAklr4pbmCfLsFAThiq5Sg28PqrnQbYKt4krjorH2HCmmw-HpWBJABCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بسنت: هیچ‌کس از تحریم‌های آمریکا علیه ایران در امان نیست  وزیر خزانه‌داری آمریکا، درباره چین و ایران:
🔹
می‌خواهیم امروز به‌صراحت اعلام کنیم که هیچ‌کس خارج از دسترس تحریم‌های آمریکا نیست. هر فرد یا نهادی که معاملات را تسهیل کند و بخشی از شبکه‌ای باشد که نفت…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/684188" target="_blank">📅 13:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684187">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
جزئیات نسخه تازه مصوبه مجلس
🔹
بر اساس ماده‌ی ۱۵، همه‌ی اشخاص حقیقی و حقوقی ۳ ماه فرصت دارند تا فعالیت‌ها، قراردادها و ارتباطات جاری خود با کشورهای خارجی را با سازوکار جدید تطبیق داده و در سامانه شفاف کنند.
🔹
تولید اثر هنری بدون مجوز از نهادهای قانونی کشور،…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/684187" target="_blank">📅 13:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684186">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d8c30461.mp4?token=ktwiDvQxFl2PdLNxDKs-l9E2ijO9beI5zvwXNfVO5cC_SRP0xrJfHXb11AgMKvQwjNTeXgdCYGF3QspkJYh2ZfSduYGo-tj6cajk-yiQRh2Fr1jtFkXOAYJ4yjFYSAOyJ3xLXW-dWfKCVv6p2Sv6BPhVJZU1PP1h8Vcz8tfNeWc2bzGgndLLjnIuVGjacAfIhNcxVDoOQSHYzo7aNDgMazcj0p_m7lYjc9kei8qkwhZDSWnC117DjDYTT-KHhgLBxfGtPKSzAPoXyokU9gx3_Lu0U1MjRJyVcLON8SSeM0jaeA5Mk-YXMJGEYyqnEsQ59TWz8HDn44zwTDTeHHYgOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d8c30461.mp4?token=ktwiDvQxFl2PdLNxDKs-l9E2ijO9beI5zvwXNfVO5cC_SRP0xrJfHXb11AgMKvQwjNTeXgdCYGF3QspkJYh2ZfSduYGo-tj6cajk-yiQRh2Fr1jtFkXOAYJ4yjFYSAOyJ3xLXW-dWfKCVv6p2Sv6BPhVJZU1PP1h8Vcz8tfNeWc2bzGgndLLjnIuVGjacAfIhNcxVDoOQSHYzo7aNDgMazcj0p_m7lYjc9kei8qkwhZDSWnC117DjDYTT-KHhgLBxfGtPKSzAPoXyokU9gx3_Lu0U1MjRJyVcLON8SSeM0jaeA5Mk-YXMJGEYyqnEsQ59TWz8HDn44zwTDTeHHYgOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پادشاه جنگل‌های هیرکانی
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/684186" target="_blank">📅 13:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684185">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
سازمان بین‌المللی دریانوردی: در طول ۶ ماه درگیری در تنگه هرمز، ۶۸ حادثه دریایی به ثبت رسیده
🔹
این حوادث دست‌کم به کشته شدن ۲۰ دریانورد یا کارگر بندر منجر شده.
🔹
کشتی‌های با پرچم لیبریا، بیشترین خسارت را متحمل شدند؛ ۴ حادثه هم برای کشتی‌های با پرچم ایران ثبت شده.
🔹
حدود ۵۰ درصد از مجموع کشتی‌های آسیب دیده را نفتکش‌ها تشکیل می‌دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/684185" target="_blank">📅 13:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684184">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c4d927062.mp4?token=TEDktf_sWsmFyRNA-rKOAdyv6dnm-CIb-u2ZE6r_d48KGsj1ZY2v5SL0VwnnrG6MGh8Y9FDanEdYBsiny6_YBAJndk1jLjf5ncpmqXHMjcCAiD22cXjJc7fIxSvp5OoZRaP1ltRk7V5wldjYTAzPdvVQDq3rLVhwtZPZPK-k_L7oEvxrqbzB4klctkNtkFao4JHlefzId9OlMoXeSMk4UoXwZYtuS_gOWHlMPflrd7uw1x5q86WbjuI-5DqlloOn0afhCwKwZE3HDOkeY8YG_x_vMzvWVAMUx5rJ4HPLUQoXxmd6Bg6dsql5LtUjUxHSaQiriwYPorLrEt2n50pUlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c4d927062.mp4?token=TEDktf_sWsmFyRNA-rKOAdyv6dnm-CIb-u2ZE6r_d48KGsj1ZY2v5SL0VwnnrG6MGh8Y9FDanEdYBsiny6_YBAJndk1jLjf5ncpmqXHMjcCAiD22cXjJc7fIxSvp5OoZRaP1ltRk7V5wldjYTAzPdvVQDq3rLVhwtZPZPK-k_L7oEvxrqbzB4klctkNtkFao4JHlefzId9OlMoXeSMk4UoXwZYtuS_gOWHlMPflrd7uw1x5q86WbjuI-5DqlloOn0afhCwKwZE3HDOkeY8YG_x_vMzvWVAMUx5rJ4HPLUQoXxmd6Bg6dsql5LtUjUxHSaQiriwYPorLrEt2n50pUlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر دیده‌نشده از اصابت موشک‌های سنگرشکن به ساختمان شیشه‌ای در نبرد رمضان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/684184" target="_blank">📅 13:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684183">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
هشدار پلیس فتا درباره کلاهبرداری با جعل صدای آشنایان
🔹
معاون پلیس فتا هشدار داد کلاهبرداران با کمک هوش مصنوعی می‌توانند صدای افراد آشنا را جعل کرده و با درخواست فوری پول یا اطلاعات بانکی، افراد را فریب دهند.
🔹
پلیس توصیه کرد پیش از هرگونه واریز، هویت تماس‌گیرنده را از طریق شماره‌ای که از قبل در اختیار دارید بررسی کنید و رمز، کد تأیید و اطلاعات بانکی را در اختیار کسی قرار ندهید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/684183" target="_blank">📅 13:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684182">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mt2bJF9Uxp21MF7rWtjLKqHovusl4i-ZL1_qxNGhIy4MetEoVbV5QxTtG84VOGIHox8V8iJV0ER1n_Ky2jSJFj66Sg_603EGlr45_hUv2f_w9jDPh-BQzrCYAeh6WFXRrgtn6-DY5t2mqb5MJjS4gF0oGmgOO1EjR9pFE-S2xhHTkVmehpXTM6gVb3b1FdOET7JEAr_loDPLq5ylh2XilIVCJe690T-dN7I7ri4IugyRSWBiWLsPkfONuPl39GnKAyNFTCq1bUb11mb7U_JNrxdgbpgdExtGK3cL9x56o8sGV5wkVBdmr0jfmHP5WdLd6tq-0tvXNnTSGGaeuZoTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بسنت: هیچ‌کس از تحریم‌های آمریکا علیه ایران در امان نیست  وزیر خزانه‌داری آمریکا، درباره چین و ایران:
🔹
می‌خواهیم امروز به‌صراحت اعلام کنیم که هیچ‌کس خارج از دسترس تحریم‌های آمریکا نیست. هر فرد یا نهادی که معاملات را تسهیل کند و بخشی از شبکه‌ای باشد که نفت…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/684182" target="_blank">📅 13:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684181">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13e70222e5.mp4?token=UOv-Sk3F2AxlUyRcamkwi_VpWQfPHDCFQ-aFl1ecCVhfQ4YBQsnDdxPD6rXuAP7SjOWSpcSF2ZS30qRhMJu4WkcaOpR2h7KakRSMNY5_DLRYNuTMxL0s53SlW_uYqJHB3fvhGlF0ewcz7AEm53XkPGu1A5UA5sL1awL1odkcTeK1o7IZMG5J1zm1Iu1pPkTtmb52RM54NWj8ZptaFX3zY-3CRGPpiKC0LrFUqrJ4PoHG_Sz_S5_6TlcPDbXmf7jBssCIh5zpjXNr1dlq7hF9OsWo1CXWV1UbumbXAVZ2asCc-OZV6lq8XKapHEqeXNPzVzqiIfTbYbtL_6sMdItLzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13e70222e5.mp4?token=UOv-Sk3F2AxlUyRcamkwi_VpWQfPHDCFQ-aFl1ecCVhfQ4YBQsnDdxPD6rXuAP7SjOWSpcSF2ZS30qRhMJu4WkcaOpR2h7KakRSMNY5_DLRYNuTMxL0s53SlW_uYqJHB3fvhGlF0ewcz7AEm53XkPGu1A5UA5sL1awL1odkcTeK1o7IZMG5J1zm1Iu1pPkTtmb52RM54NWj8ZptaFX3zY-3CRGPpiKC0LrFUqrJ4PoHG_Sz_S5_6TlcPDbXmf7jBssCIh5zpjXNr1dlq7hF9OsWo1CXWV1UbumbXAVZ2asCc-OZV6lq8XKapHEqeXNPzVzqiIfTbYbtL_6sMdItLzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین: با تحریم‌های غیرقانونی آمریکا مخالفیم  سخنگوی سفارت چین در واشنگتن:
🔹
تحریم‌های یکجانبه آمریکا علیه ایران مبنایی در حقوق بین‌الملل و مجوز شورای امنیت سازمان ملل ندارد و پکن از حقوق و منافع قانونی شرکت‌های چینی حمایت خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori |…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/684181" target="_blank">📅 12:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684180">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPUGU83QeeWFH9vYmLakcscx0qIzl3OY_eTXXat1S8U1eoZ1IXQkED2vY6mT1T31kjpRqHwvRFMWuesic9gQyvO4H-tEFjU46HNQdXs5fU7_SaxIManCpP_WijRAYuIIElQSXFKp9b5cOmLlRXbM6J-_-qkYbhJnw3VFptFh_fPXIH-oIY6kbo1SbRMK2Z89UyCD5EgYMM2kIOJlYyct90DlTuFIJgFX0Xz-_JSAItHvxsJGan46uCyFjjVYTrMIx4vWAiRfVKQiEREZLb26VcaUvj7vB8iWGIqPnKWLWAdAZQCS7Ep9Ntwdwnuc0KoUkMWrphlfhleOrriGX4D3GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکورد تاریخی جدید بورس با جهش ۲ درصدی
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۲۴ هزار واحدی به ۶ میلیون و ۲۲۴ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/684180" target="_blank">📅 12:39 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684179">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
لحظاتی از دیدار صمیمانه سرلشکر محسن رضایی و فیلد مارشال عاصم منیر در تهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/684179" target="_blank">📅 12:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684178">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOyrtkaYZHUNqgbL5wulRXE-ai9aa_pymeDDaWkD73UOIOWe5DZsTznJsoIzZcrEubjNaLbvRSVnO7nuje67E_FAvtUURUnjmPLE_yT_n-dUK5hhqC0rlA6-N22VJfaG19p421WJDrHKGlj9CvxbMdzQMuXR80wp5RSwGZbMOeYJS2SHusghQBLjAQuwGPaflO55jOhUjjNKKFgngDWHJhZlzfcExTy2TbNfC-3CY9RtnabRaPWdu-aaONt5StJ2DXadrR5pRam642eklMm7nxuAiIze19lUTWbz3JysiFhPDOJkbOb3ZXkXZJG2bybu1ZHp6qT4daIVnkeer0Xccw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بسنت: هیچ‌کس از تحریم‌های آمریکا علیه ایران در امان نیست  وزیر خزانه‌داری آمریکا، درباره چین و ایران:
🔹
می‌خواهیم امروز به‌صراحت اعلام کنیم که هیچ‌کس خارج از دسترس تحریم‌های آمریکا نیست. هر فرد یا نهادی که معاملات را تسهیل کند و بخشی از شبکه‌ای باشد که نفت…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/684178" target="_blank">📅 12:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684177">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_fcyk6fflA2R3EJkdbts1EjPc-PWswL1s4-qoeA149MC_XgODWEsjvQuUI-IhYiKOK2GqfU69wDBC2MYircN6IyrN7SdBv5Yen1WqYHZV2iqtR_JeXB0c3d7G5NtvBbkSPjQFdbb7jossuiviRvXEoddVlPEt3SqedUpB6pgmUAV2gV8x5yTUExMC3dddIfAdDYHKaJUf4BQmYwFDBCADiHF_j2CFB-lgfYg6XKI5jYcg-0utQIafROxb9V64BuYYF_AUWNDw9z4QjVGqxAL-p9j33qu28mvEko188R2wNTBnFL4lF8LRTIn7SOasQ-FGNzS8Fdi93YWLvFHK9aOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمهیدات جدید بانک مرکزی برای تقویت عرضه و مدیریت بازار ارز؛ تسهیل خرید اسکناس برای فعالان اقتصادی
🔹
بانک مرکزی در ادامه سیاست‌های جدید ارزی و با هدف تقویت عرضه‌ ارز، پاسخگویی به نیازهای ارزی فعالان اقتصادی و تعمیق معاملات رسمی اسکناس، تمهیدات جدیدی را برای توسعه دسترسی متقاضیان به اسکناس ارز در شبکه رسمی بانکی به اجرا می‌گذارد.
🔹
بر اساس این تصمیم، با توجه به تقویت ذخایر ارزی بانک مرکزی متعاقب اجرای سیاست‌های جدید ارزی از اواخر سال گذشته و حسب ارزیابی‌های به‌عمل‌آمده از تحولات بازار ارز، از روز سه‌شنبه مورخ ۱۴۰۵/۰۶/۰۳، کلیه اشخاص حقوقی می‌توانند با مراجعه به شعب بانک‌های عامل ملت، تجارت و صادرات، نسبت به خرید اسکناس ارز تا سقف پنج هزار (۵۰۰۰) دلار با نرخ توافقی اقدام کنند.
🔹
همچنین اشخاص حقیقی نیز می‌توانند با مراجعه به شعب بانک‌های مذکور، نسبت به خرید اسکناس ارز تا سقف هزار (۱۰۰۰) دلار اقدام کنند.
🔹
این اقدام با هدف تقویت عرضه ارز، پاسخگویی مستقیم‌تر به نیازهای ارزی فعالان اقتصادی و تعمیق معاملات در شبکه رسمی اسکناس انجام می‌شود و ظرفیت عرضه ارز از مسیر رسمی شبکه بانکی را افزایش خواهد داد.
🔹
بانک مرکزی همچنین اعلام کرده است سایر برنامه‌های مدیریت بازار ارز نیز متعاقباً اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/684177" target="_blank">📅 12:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684176">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرمانده نیروی زمینی ارتش: مرزهای ایران خط قرمز نیروهای مسلح است به آن نزدیک نشوید!
🔹
رئیس شورای عالی قضایی عراق با رئیس قوه‌قضائیه دیدار کرد.
🔹
رسانه‌های لبنانی از تمدید ۶ ماهه اقامت سفیر ایران در لبنان، از سوی اداره امنیت عمومی این کشور خبر دادند.
🔹
استفاده از تلفن همراه برای دانش‌آموزان دبیرستانی در فرانسه ممنوع شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/684176" target="_blank">📅 12:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684175">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
عرضه ۵۰۰ میلیون دلار اسکناس بانک مرکزی به شبکه بانکی؛ آمادگی برای افزایش عرضه متناسب با تقاضا
🔹
بانک مرکزی در راستای مدیریت بازار ارز و با هدف تقویت عرضه اسکناس و تسهیل دسترسی متقاضیان حقیقی و حقوقی، امروز نخستین مرحله عرضه اسکناس ارز به شبکه بانکی را آغاز می‌کند.
🔹
در این مرحله ۵۰۰ میلیون دلار اسکناس در اختیار بانک‌های متقاضی قرار می‌گیرد تا از طریق شعب منتخب و صرافی‌های بانکی به متقاضیان عرضه شود.
🔹
بانک‌های متقاضی تا ساعت ۱۳ امروز سوم شهریورماه ۱۴۰۵ فرصت دارند حجم مورد نیاز خود را برای عرضه در شعب منتخب و صرافی‌های بانکی به بانک مرکزی اعلام کنند.
🔹
بر این اساس، تمام اشخاص حقیقی و حقوقی می‌توانند با مراجعه به شعب منتخب بانک‌های عامل، نیاز خود به اسکناس ارز را از مسیر رسمی شبکه بانکی و در چارچوب سقف‌های تعیین شده، تأمین کنند.
🔹
بانک مرکزی اعلام کرده است در صورت افزایش سفارش‌های ثبت‌شده از سوی شبکه بانکی، آمادگی دارد حجم عرضه اسکناس را متناسب با میزان تقاضای ثبت‌شده افزایش دهد.
🔹
ورود ۵۰۰ میلیون دلار اسکناس به شبکه بانکی در نخستین مرحله، در حالی انجام می‌شود که بانک مرکزی بر تقویت عرضه و پاسخگویی به تقاضای واقعی بازار از مسیر رسمی تأکید دارد؛ اقدامی که می‌تواند دسترسی متقاضیان به ارز را افزایش داده و از شکل‌گیری تقاضای هیجانی و نرخ‌های غیرواقعی در بازار جلوگیری کند.
🔹
بانک مرکزی همچنین اعلام کرده است این عرضه محدود به رقم ۵۰۰ میلیون دلار نخواهد بود و در صورت نیاز شبکه بانکی، امکان افزایش حجم فروش وجود دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/684175" target="_blank">📅 12:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684174">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4awvj_M8qPDhER1BHbXoauzvRio2HU86LJON5pWOuHBBSNPU9IaZ3D4xZXaUYVaFxK6MtmVOiVvop0TyMUsGirPwvZngg4Pbctr6_bxKoFJmasPcw4aWCrdq2D9OHY747nm3Z8XkdtYfqeehVrMfsVc7pAOUc7Ubv7xkR6JLAUyIwX8RHmZU7Bt8ggwUX69bToigojsASHVTTWEVMr4bhB6lXpocFADCp26Dj67IHZ3vfNgs8tbf_eM4pzeCE6WaDv0SkrOjUOlaAPQ02ZrGKb64m4PD-ol3DhxybM9rk9XIzbo-KjnEUGEdTqbjPG_av3bjHXta2zEY5HgBuYCog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودروهای داخلی ۲۰ درصد بیشتر سوخت مصرف می‌کنند
🔸
مصرف بنزین خودروهای داخلی حدود ۲۰ درصد بیشتر از نمونه‌های خارجی عنوان شده است.
🔸
در ۱۵ سال گذشته موتور جدیدی در خودروسازی کشور توسعه نیافته و ضعف فناوری موتور از عوامل اختلاف مصرف سوخت است.
@amarfact</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/684174" target="_blank">📅 12:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684173">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
عارف: طرح موسوم به «مقابله با نفوذ بیگانگان» به فعالیت علمی کشور ضربه می‌زند  معاون اول رئیس جمهور:
🔹
دکتر قالیباف قول داده است این طرح را از دستور کار مجلس خارج کند و حتی اگر این اتفاق رخ ندهد، باید از طریق رایزنی با سایر نهادها از جمله مجمع تشخیص مصلحت…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/684173" target="_blank">📅 12:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684172">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845a0dd0f0.mp4?token=AwReGE5FO_5e-Q0c_cI8WX6dPzT7d-KeqcJlzxFT8TDu1rZ_sNhNkTycDk1pnI-mQKUUX78cEJpL7krNiN1U6uptjcbrroCURcZVA5gHrIelvPPriDePnp5FYnuRi-4Zzq3_-Mo3ds1WiHtnOtqtiTL74MXxNmMzxOFWtBjF_kobn8PwW5dZ_JW3nAbtmerhr-RX2_P9HFp-ifmB5mgrP5DPhYq_-NVryF42sb3JgLgroxF24xA-LS14O-EXPeKvjvucsCO1t6DZtsklJNm6r-ThJUFVsOatez9-VeclkGhDscq1dY5hd-SOEswQqd_iIvIwGlbM8bwwqNy7gw8tLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845a0dd0f0.mp4?token=AwReGE5FO_5e-Q0c_cI8WX6dPzT7d-KeqcJlzxFT8TDu1rZ_sNhNkTycDk1pnI-mQKUUX78cEJpL7krNiN1U6uptjcbrroCURcZVA5gHrIelvPPriDePnp5FYnuRi-4Zzq3_-Mo3ds1WiHtnOtqtiTL74MXxNmMzxOFWtBjF_kobn8PwW5dZ_JW3nAbtmerhr-RX2_P9HFp-ifmB5mgrP5DPhYq_-NVryF42sb3JgLgroxF24xA-LS14O-EXPeKvjvucsCO1t6DZtsklJNm6r-ThJUFVsOatez9-VeclkGhDscq1dY5hd-SOEswQqd_iIvIwGlbM8bwwqNy7gw8tLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ونس، معاون ترامپ: باید به یاد داشته باشیم که کانادا یک ایالت... ببخشید، یک لغزش فرویدی بود؛ واقعاً اشتباه لفظی بود؛ کانادا یک کشور است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/684172" target="_blank">📅 11:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684171">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3271fe998.mp4?token=F50JQeBcqfItygwsV1xagBoviATlSOJWpLQcEwJGvMKAoLrO3zxntXIE1RFTAzqV2vtQK3IuCDDLlZikovCxW17N_u8MivGvTOoATPZzjmXLj-cyaRN6IixkvayNZg2K7B7TJKxV_QhHle48Ly9OWwSlLk2tFP3QVn2IHXOJVxRQOYXArUxB5vbGU1XdCKlIvbXuVKy6KsrKlD5C2zyn5YBhD3iBue18c4QMQsey3lx6ND2l7_8ULqsM0-KCvTij9ViwYYSRfgr9xjMi7h2N83UU8_NSVN-LNbczzBAQG78ZZCY9kcwJFLSzb5Eg5TdtPluto5A3iU8UoJY_d5dFv4smPQMFBIbeACcZXBXZ-UF7ArwnSCPDi1ByQtEVmA4e4D1N-QkR9op7nTlprNmqHgq6-fhXPNPJKc78ltskkr9OyuREKebkIZfRLNOzh4T_U21EkXMY0XDajpeT2X5oKM2R3wgN28niQHmA4cV2owAtEbrky1SEKJQx0RQadVE4iyZIdjZ45v9dmOdtN1RXdK6b-QJgSTBx6uJPpO6ldu9jhWaUOb5TysM7a5R9fzo5dcRwpobq5Ns1Xq9shG_BfkKTN481mJWCFpR-tlQaMfhq3EuMayOlmGoiE2ctOsSaAGmF58jxC4Iu4t902vgUib4R9uqAM6ZM2k2U85vANFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3271fe998.mp4?token=F50JQeBcqfItygwsV1xagBoviATlSOJWpLQcEwJGvMKAoLrO3zxntXIE1RFTAzqV2vtQK3IuCDDLlZikovCxW17N_u8MivGvTOoATPZzjmXLj-cyaRN6IixkvayNZg2K7B7TJKxV_QhHle48Ly9OWwSlLk2tFP3QVn2IHXOJVxRQOYXArUxB5vbGU1XdCKlIvbXuVKy6KsrKlD5C2zyn5YBhD3iBue18c4QMQsey3lx6ND2l7_8ULqsM0-KCvTij9ViwYYSRfgr9xjMi7h2N83UU8_NSVN-LNbczzBAQG78ZZCY9kcwJFLSzb5Eg5TdtPluto5A3iU8UoJY_d5dFv4smPQMFBIbeACcZXBXZ-UF7ArwnSCPDi1ByQtEVmA4e4D1N-QkR9op7nTlprNmqHgq6-fhXPNPJKc78ltskkr9OyuREKebkIZfRLNOzh4T_U21EkXMY0XDajpeT2X5oKM2R3wgN28niQHmA4cV2owAtEbrky1SEKJQx0RQadVE4iyZIdjZ45v9dmOdtN1RXdK6b-QJgSTBx6uJPpO6ldu9jhWaUOb5TysM7a5R9fzo5dcRwpobq5Ns1Xq9shG_BfkKTN481mJWCFpR-tlQaMfhq3EuMayOlmGoiE2ctOsSaAGmF58jxC4Iu4t902vgUib4R9uqAM6ZM2k2U85vANFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف کلینتون: مصرف گسترده مهمات آمریکا در ایران، توان واشنگتن برای دفاع از تایوان را محدود کرده است
/
تمرکز بر ایران و خاورمیانه، ذخایر تسلیحاتی آمریکا را خالی کرده است
🔹
هیلاری کلینتون با اشاره به مصرف بخش قابل‌توجهی از مهمات آمریکا در ایران و ارسال تسلیحات به متحدان واشنگتن در خلیج فارس، نسبت به کاهش توان این کشور برای مواجهه با بحران‌های احتمالی هشدار داد، در صورت اقدام چین علیه تایوان، آمریکا ممکن است برای کمک به دفاع از تایوان با وضعیتی دشوار روبه‌رو شود؛ چرا که ذخایر تسلیحاتی‌اش پیش‌تر تحت فشار قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/684171" target="_blank">📅 11:56 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684170">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d754d5d97.mp4?token=Rm4poEJBCOCCO8zAQxC21LnHwSW77kvBghMUUQlUWU-tm8MpF219rSYE5SMGrhsbTef-eKvs30wtl_UvCD1-rR5JrKK-WxmASaWsIocqvGHDPVnQXLFQzqwHR202mOFGH9sZkhg-fBzKvr8PLJhSPmXT58cp03kvkEa9oFE-mud7zX0pmFRPrdytOLK2ZtaqNRk0wh6eqUYwO1TN9kmNSOQ78OaINHcWS9N8F8ahNG4FzNlHYGWuH5r0J4WC1LOEsjEtKQYHNKBG02gURifJCZ7JAQoRAVzv44eo7oZXmKKkaSybLPCzcCG0hI0UDlXpsO_4--JgGr0hq46gCuV2fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d754d5d97.mp4?token=Rm4poEJBCOCCO8zAQxC21LnHwSW77kvBghMUUQlUWU-tm8MpF219rSYE5SMGrhsbTef-eKvs30wtl_UvCD1-rR5JrKK-WxmASaWsIocqvGHDPVnQXLFQzqwHR202mOFGH9sZkhg-fBzKvr8PLJhSPmXT58cp03kvkEa9oFE-mud7zX0pmFRPrdytOLK2ZtaqNRk0wh6eqUYwO1TN9kmNSOQ78OaINHcWS9N8F8ahNG4FzNlHYGWuH5r0J4WC1LOEsjEtKQYHNKBG02gURifJCZ7JAQoRAVzv44eo7oZXmKKkaSybLPCzcCG0hI0UDlXpsO_4--JgGr0hq46gCuV2fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تابلو نقاشی نیست؛ لرستان همیشه زیباست
🇮🇷
#ایران_زیبا
#اخبار_لرستان
در فضای مجازی
👇
@akhbarlorestan</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/684170" target="_blank">📅 11:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684169">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
ادعای کپلر: شمار عبور کشتی‌ها از تنگه هرمز طی هفته گذشته ۲.۵ درصد افزایش یافت و به ۱۲۱ مورد رسید
🔹
۴۶.۳ درصد از کشتی‌ها از مسیر تعیین‌ شده از سوی ایران استفاده کردند.
🔹
تعداد کشتی‌های تحریم‌ شده که از تنگه عبور کردند، از ۹ مورد به ۱۶ مورد رسید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/684169" target="_blank">📅 11:48 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684168">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3a673c1e.mp4?token=XldwbjvfstYH4qge2_S5_rOYQZje-dVEFxMbvRnmqMU8cjEDXe7vuQywQhuC18I55NHrBbChnp2obkQp-3BaVQmYmReKGprWLm6S4RKs-3587i7LLKO7Js3EY__nHzLU0MBLMf2oYErboAG4HcDTY_HnoSaGS-dwAsfN9pF200l4L1Fm4YFGrIcKRI7KfM4JdtxGPw6aJJ_NIM3sIRctEtJ0mUOOPf5ljQprS7KGBnXYHRrFmKxDFbRmvEjlsSgeJbnuaRFg19qNmeLzG4JKYPRwUjK8nFsf2f4AKfn2RQ2AM1czBAocJYbBnn0sKAolFSvkKK25RJGNTSn_nuZInA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3a673c1e.mp4?token=XldwbjvfstYH4qge2_S5_rOYQZje-dVEFxMbvRnmqMU8cjEDXe7vuQywQhuC18I55NHrBbChnp2obkQp-3BaVQmYmReKGprWLm6S4RKs-3587i7LLKO7Js3EY__nHzLU0MBLMf2oYErboAG4HcDTY_HnoSaGS-dwAsfN9pF200l4L1Fm4YFGrIcKRI7KfM4JdtxGPw6aJJ_NIM3sIRctEtJ0mUOOPf5ljQprS7KGBnXYHRrFmKxDFbRmvEjlsSgeJbnuaRFg19qNmeLzG4JKYPRwUjK8nFsf2f4AKfn2RQ2AM1czBAocJYbBnn0sKAolFSvkKK25RJGNTSn_nuZInA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ چرخ زندگی
🔹
بازتاب تلاش و خلاقیت همراهان خبرفوری در کسب‌وکارهای خانگی؛ گام‌هایی استوار برای چرخش چرخ اقتصاد خانواده.
🔸
مسیر راه‌اندازی کسب‌وکارتان را با ما به اشتراک بگذارید؛ در یک پیام صوتی ۳۰ ثانیه‌ای نام، شهر، نحوه شروع و نتیجه کارتان را بگویید و عکس کسب‌وکار را هم ارسال کنید. روایت‌های منتخب در خبرفوری منتشر می‌شوند
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/684168" target="_blank">📅 11:48 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684166">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a9dbd2ef.mp4?token=rXCqNPRnW-8AEkYsTNcuPOTpfz5LC47bwEcQUPY1LSCBqGRKIaZenLYv1j8oMql9xmwtCj0f3Ffc_I3As57or4DaVIFJJKvv3dkx8FDCqU5mI1DR_nQirovEd81v3veTyiVHgg0YNuM3PckOXknSTpfZClxGlEUKNme7t5GyMkAHpuCejTO7Emjv01nD8c4N9IEh35ETcTS6Y-AFU0noWTnmiUqnxv_g7A1EBUAWbSmzLC1vm9vnwSPor1QyTobCxWx8KXs4fs3iTkNED72-CMUXEm9gNp-5KNjHqhSP4MgznOLn70OpvN3jyNbQsVqWAddjqTAI2-7VgW2ylJfRsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a9dbd2ef.mp4?token=rXCqNPRnW-8AEkYsTNcuPOTpfz5LC47bwEcQUPY1LSCBqGRKIaZenLYv1j8oMql9xmwtCj0f3Ffc_I3As57or4DaVIFJJKvv3dkx8FDCqU5mI1DR_nQirovEd81v3veTyiVHgg0YNuM3PckOXknSTpfZClxGlEUKNme7t5GyMkAHpuCejTO7Emjv01nD8c4N9IEh35ETcTS6Y-AFU0noWTnmiUqnxv_g7A1EBUAWbSmzLC1vm9vnwSPor1QyTobCxWx8KXs4fs3iTkNED72-CMUXEm9gNp-5KNjHqhSP4MgznOLn70OpvN3jyNbQsVqWAddjqTAI2-7VgW2ylJfRsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد نامزد مسلمان سنای آمریکا علیه رسانهٔ نزدیک به ترامپ
السید خطاب به ترامپ:
🔹
تو نمی‌خواهی دربارهٔ قیمت بنزین صحبت کنی؛ نمی‌خواهی دربارهٔ قیمت مواد غذایی صحبت کنی؛ نمی‌خواهی دربارهٔ‌ خدمات درمانی صحبت کنی؛ نمی‌خواهی دربارهٔ این جنگ تجاری احمقانه که اقتصاد را نابود می‌کند صحبت کنی؛ جنگی که در حال نابودکردن ارتش خودمان هم هست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/684166" target="_blank">📅 11:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684164">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vyYaIGsGPANFQ6OhPTZUvCXFKDF8LIxIjEBGvCDQamIcQ5fAguofRE1BB8NtHz2Hb5Hv6HFvPN-k6_PsmVT1vJye1f3_jcI4o8ob4hg8e9CAoNkmezAeCYlDZ13GtZ_CjF1V4if1uJN0BcTYk_6YPIOeWxV8g-hVGxKpYDWTS7keDpCYj4JNgAqkkHEgEEkyZaaKd44ddQa6OnqkoYpu3EAuql8NWIAzCRUCB817twaSiezqTF7Y-FZmBsLRMNKLcgEu83meEOMCN3yfUUIU2VMwQJMSlheKnGRKWdiR1DaVcjNLvP1bTlG5VDVM7kJMTtis8kj0m6FbY3HBSIdfWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AhxoASpHy3I4FoLw9v8cCuVj9xogo0NiIhz7Q4Z6sPawQK15Sw5ry8HIip1Dvxt2pYp-cANrD5DmdVLZ-r_pzfG_3TRxvHse8ovIgqIVpMCIG41a-YS9tq_1nsG3kNHfGyBeMNXJUhJIagiCJXTuDdAhfn7TNNVeZRYa9ljPHfOBCeKU3JX-4v4_l_12xFzwzbBlzBSbnmGD_efyNjqP7svKiG7nfT0PoOAOF0_uOBN7phYsnUH8FWTtxycDtwZNaAGZ0Dlwm-v2xdvwIiMjm6V6Pv5ugENTbNZRFFy3gOEtKt-tcOWgxZzvd3iFIlDPTpoVFXBfgbAMMH5eM96ZAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نویسنده سابق گاردین: مصاحبه درباره حکم سنگسار سکینه آشتیانی ساختگی بود
🔹
سعید کمالی دهقان، نویسنده گزارش جنجالی گاردین در سال ۲۰۱۰ درباره سکینه محمدی آشتیانی و ادعای حکم سنگسار او، اعتراف کرد مصاحبه با آشتیانی هرگز انجام نشده و متن آن را خودش ساخته است.
🔹
او بابت انتشار این مطلب عذرخواهی و مسئولیت آن را پذیرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/684164" target="_blank">📅 11:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684163">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmfJCal5lF4VUqSB_mrYn9dqSnzHZQNnOtsuGtTQiinWdgs77JOFMJtA12eshgfX5k657KEBcGuL6dOK008gAVX568JPaKH6Sf_B4uukYWxL1EwhRC5zlRJdRHRoov74ikcaQ8yR35AYPtT2v4eF-uf4iQ3yuXfkZcawZdRSjlXnISpl77CoMlM78JXTE8k6j1j27pmhi74fvOZrmn1DefbX_T-WQZ9JBHaePTM1ngOvvRMxqvV9-SXISlwCgJWyitfQhSb9UnSKKGMt0njd6V3KZxGzF-eSuT94sIQ7Kv0EjLgIJD5Wx693nx5Gcg05v8vgtrMHS-0f9n3qsdndGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بسنت: هیچ‌کس از تحریم‌های آمریکا علیه ایران در امان نیست  وزیر خزانه‌داری آمریکا، درباره چین و ایران:
🔹
می‌خواهیم امروز به‌صراحت اعلام کنیم که هیچ‌کس خارج از دسترس تحریم‌های آمریکا نیست. هر فرد یا نهادی که معاملات را تسهیل کند و بخشی از شبکه‌ای باشد که نفت…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/684163" target="_blank">📅 11:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684162">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097af909b6.mp4?token=KwdtMT4hAMfvWU1zlqTKzVy8a-1bep8k1R7qwKuwdUllVUs74oQflWYz26yJq0Isv5kBh6x6P1_RDSOl8oqTpIhK9bJ0gTGh29cLEm4KeOphQsftp96i5EXD78uVXDu1UEteCAZABLlFcU88DUGIU327VBFqvpw_DnQLvh1t4woTiLqd1whNDRL_8GFdvCYJDx8-K4xXmdv7Bk4Bc4gf7aCuhbXY4bXeKomzApqeIGBjPoeT56Ni3O7VLrvToCmPL5Z8jeymE7X_3ClTzGQ2dlLdQJPVojcKiaKCYaWfsiOrL43d1webLUoS_KmZ_LYNJMWc8PvINxpFEEldkX0fwa40Yq5r-BIpZVk-Byq2WdbJY41BfBENAp2ShFJeaXWm8XdF7jSpx-kx6tCyaBSIDOiybah2c4Oozl1fF4VmcFQiePsNwTRa36ZgKqmgCP14CAU_E_kOvTbiqiw1sbykoZMCtDdCdQT5f9LS2Ttv9RaGy1zwJXvMFY5QhprxYKXZvdwfSb8R6HSwhXCf9YGh3q8Qi01Pxo103L7xILgjh8_qTjE8lUQNT2uMexwNGIp9yY-R9odBA5wW_UAS9DbBR60r-L-XyvUFJUuvrgdR3JxW8anbKDyJXVJYg5k8KJRZVQQU0JrpAJ7ML3WcrS2xjSbP_oGSW0FV-hC1HNOdW3M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097af909b6.mp4?token=KwdtMT4hAMfvWU1zlqTKzVy8a-1bep8k1R7qwKuwdUllVUs74oQflWYz26yJq0Isv5kBh6x6P1_RDSOl8oqTpIhK9bJ0gTGh29cLEm4KeOphQsftp96i5EXD78uVXDu1UEteCAZABLlFcU88DUGIU327VBFqvpw_DnQLvh1t4woTiLqd1whNDRL_8GFdvCYJDx8-K4xXmdv7Bk4Bc4gf7aCuhbXY4bXeKomzApqeIGBjPoeT56Ni3O7VLrvToCmPL5Z8jeymE7X_3ClTzGQ2dlLdQJPVojcKiaKCYaWfsiOrL43d1webLUoS_KmZ_LYNJMWc8PvINxpFEEldkX0fwa40Yq5r-BIpZVk-Byq2WdbJY41BfBENAp2ShFJeaXWm8XdF7jSpx-kx6tCyaBSIDOiybah2c4Oozl1fF4VmcFQiePsNwTRa36ZgKqmgCP14CAU_E_kOvTbiqiw1sbykoZMCtDdCdQT5f9LS2Ttv9RaGy1zwJXvMFY5QhprxYKXZvdwfSb8R6HSwhXCf9YGh3q8Qi01Pxo103L7xILgjh8_qTjE8lUQNT2uMexwNGIp9yY-R9odBA5wW_UAS9DbBR60r-L-XyvUFJUuvrgdR3JxW8anbKDyJXVJYg5k8KJRZVQQU0JrpAJ7ML3WcrS2xjSbP_oGSW0FV-hC1HNOdW3M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اون چیه که مثل یه شربت خنک وسط تابستون به دل میشینه؟!
🍹
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/684162" target="_blank">📅 11:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684161">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b84d78758.mp4?token=q-Ywizx8rBGt8WEebBLRssDhNjN7sZX0Oth1VnVU2GESZdLue30is_ITzXYPLAnxQoK3kewupRPthFkota8joMHFuAK_JDS3xe9XYcbwzEu9n6Ht3UcPaaxea0aX3a-uOSAMRq9nviFsUh1fXVRnQWQx4vremv9hZ0TwdIJ_CU1KUWx_Srk8X4SGjn4CYZMBvbMGwtU759R8MnF071GozBBf1PdTbbmSM9Co4rX6x3DzPSQvgR2yydt7GTmjWwgS10kPZnnFAOZ2PiRQuYgy8cDdYF-bjKB6buNxT5cqgRBtQPseqghKm_cKnBf9bDx-eIG_pg1Ecjs5Ga7LWrjAgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b84d78758.mp4?token=q-Ywizx8rBGt8WEebBLRssDhNjN7sZX0Oth1VnVU2GESZdLue30is_ITzXYPLAnxQoK3kewupRPthFkota8joMHFuAK_JDS3xe9XYcbwzEu9n6Ht3UcPaaxea0aX3a-uOSAMRq9nviFsUh1fXVRnQWQx4vremv9hZ0TwdIJ_CU1KUWx_Srk8X4SGjn4CYZMBvbMGwtU759R8MnF071GozBBf1PdTbbmSM9Co4rX6x3DzPSQvgR2yydt7GTmjWwgS10kPZnnFAOZ2PiRQuYgy8cDdYF-bjKB6buNxT5cqgRBtQPseqghKm_cKnBf9bDx-eIG_pg1Ecjs5Ga7LWrjAgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تبدیل دوچرخه معمولی به دوچرخه برقی
🔹
هواوی موتور برقی جمع‌وجوری طراحی کرده که به بدنه دوچرخه متصل می‌شود و چرخ عقب را تا سرعت ۳۲ کیلومتر بر ساعت به حرکت درمی‌آورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/684161" target="_blank">📅 11:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684160">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEb8UmQuZImhxdpHseMkK92OvleHXHNDG0QeCAsdQiHScr9wBgIz8ST6wHtbk_aP3JDc_5C9KpX3XZK_V7pcTODxkgs-SiBm8deDHM8FOFBpPZIc2mCaMu6a-Lg7WE6G490BtuFcKL8FHt4o1caAKIOYyBmeTy6TlskNmepvJU77RNxLxFoNB6-nUpnCid5r4nMfeCs1EYLgXm_bUMsRThm4lEfE1ObtibqBzZ9xwqfANqbxZwS8zNXckzxZwUM-Vr0w31mRclsR1akbftCgqLUQZl2OTs9ratMWrQGs28MqctMMxQ2kNFG1Ud5HKu86JyRpmGfKguVVfPWTbMEicw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار مدیریت بحران نسبت به ناایمنی «بازار پروانه» در اراضی عباس‌آباد
رئیس سازمان مدیریت بحران شهر تهران در گفتگو با ایسنا:
🔹
بازار پروانه واقع در اراضی عباس آباد از لحاظ ایمنی خطرناک و پرریسک است. سازه‌ای که به این بازار اختصاص داده شده، برای این حجم از تردد مناسب نیست.
🔹
خطر ریزش سازه دور از ذهن نیست. ۱۷ عامل ناایمنی‌ در این بازار شناسایی شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/684160" target="_blank">📅 11:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684159">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wr_jw2xvKo_RsmdIRx5CsT358YWmQZv42-JxbzRwNG-gzxnsbKGx-2NNFPDiHv-Y1VPmhIKg1rjjy6xeUuxKn0YMcC6uGAG50-9IOI-JiPhctld17BAwilwDD1llYnYS7-w0qs4tycoi2ph7pNa_PWd2lVBKjKvsHfdGXZVhjOR37J2tH2YS4brGPu6oFseynXNhaGnNAJ8A1J8Rd8FbP8x6ShdVCPr78hSsZ6W-UXIbdrLEdQCGnRH4ZorWSf3vIzVDOyBtEID0CHucb1_5fJrRCSwDymSIqB6wg5t0p5yUyJ70FKT2-kNuPmOh4uSYxKipjJnDx40LG80JRVKKpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قهوه رو اشتباه نخورید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/684159" target="_blank">📅 10:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684158">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ریاض و پاریس بر راه‌حل دیپلماتیک درباره ایران و تشکیل کشور فلسطین تأکید کردند.
🔹
شورای شهر تهران: یک خیابان در منطقه یک به نام اکبر عبدی تغییر می‌کند.
🔹
دبیرکل حزب الله روز جمعه در مراسم میلاد پیامبر اکرم(ص) سخنرانی می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/684158" target="_blank">📅 10:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684157">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
بسنت: هیچ‌کس از تحریم‌های آمریکا علیه ایران در امان نیست  وزیر خزانه‌داری آمریکا، درباره چین و ایران:
🔹
می‌خواهیم امروز به‌صراحت اعلام کنیم که هیچ‌کس خارج از دسترس تحریم‌های آمریکا نیست. هر فرد یا نهادی که معاملات را تسهیل کند و بخشی از شبکه‌ای باشد که نفت…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/684157" target="_blank">📅 10:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684156">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
آمریکا مبادلات ورزشی و دانشگاهی با ایران را تعلیق کرد
🔹
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (OFAC) با انتشار سندی اعلام کرد که واشنگتن فعالیت‌های ورزشی و تبادلات دانشگاهی با ایران را به‌طور نامحدود متوقف کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/684156" target="_blank">📅 10:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684155">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e288783b01.mp4?token=oorkRMs5rdi_S8tRRo2mV0P7y5zIdeQowjgZJYFnsvbKARk4CXbVH6_pko_iLwNCa8MrzkWCf15KrZ7GaGRvpRyWjEPtn6Gs2EM1SdJBupXuEdcjbKkfT3BzeMaz_DG4n51prLBCVY5ytiaWNzz1U4p745aI62yYJyC25iC6SngLAXgFZdV1szOSqhiot-QESWRYup_VWzAWz8IUT66yrRlSEt8q1S7KV8ISjo-2bahrk2K8JwEDlwKSdyswxqF_Lnzlp-EqPXn1EMfUH1QRNm2xFZNt-w9NuY2vd3uDL32VqLyIHcWMHYA4GL2qWuLj5Y9dF0tDyq2f7RJQvZYOLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e288783b01.mp4?token=oorkRMs5rdi_S8tRRo2mV0P7y5zIdeQowjgZJYFnsvbKARk4CXbVH6_pko_iLwNCa8MrzkWCf15KrZ7GaGRvpRyWjEPtn6Gs2EM1SdJBupXuEdcjbKkfT3BzeMaz_DG4n51prLBCVY5ytiaWNzz1U4p745aI62yYJyC25iC6SngLAXgFZdV1szOSqhiot-QESWRYup_VWzAWz8IUT66yrRlSEt8q1S7KV8ISjo-2bahrk2K8JwEDlwKSdyswxqF_Lnzlp-EqPXn1EMfUH1QRNm2xFZNt-w9NuY2vd3uDL32VqLyIHcWMHYA4GL2qWuLj5Y9dF0tDyq2f7RJQvZYOLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شلیک محافظ نتانیاهو به هدفی نامشخص؛ وحشت در تل‌آویو
🔹
محافظ نتانیاهو در خیابان‌های تل‌آویو بدون دلیل به اهدافی نامشخص شلیک کرد و شاباک این اقدام را قانونی خواند.
🔹
شبکه‌های اجتماعی و رسانه‌های اسرائیلی تصاویری را منتشر کردند که در آن‌ یکی از محافظان بنیامین نتانیاهو، نخست‌وزیر رژیم صهیونیستی در حین حرکت کاروان در یکی از خیابان‌های پرتردد شهر، ناگهان  با اسلحه به هدف نامشخصی شلیک کرد و موجی از وحشت و سردرگمی را میان مردم ایجاد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/684155" target="_blank">📅 10:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684154">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f637191d0.mp4?token=q7KHcfElprjWZBr3dvj74I44gP4SZV43OaxKknzfNuBf5358HsVXfDcU3lFhGf7EXsToS0N-teyblsIg9AvTaTRWYsgwehJA4ZpuMxXBnGevzO3yfsn0s4aR2NiUQY8KGOPe6WnP3ufR0gzfljvPvgHepJtAz7NBSKsG9kkKB8pVLe8oAxk65Tj6EZj51AbrPv4AlPDyp9Fnr-M5NIWdXFBGOvQ0sg297f8W7OKMlLpb1sUKmEgaF1cP6oEHKAmqeOFDzNmYbE_qQsmaX0KPtQt3czxrsnPnGMDHQthk9wMyN5tJ7zKJelmq64ITCyZvi6uI4xlN4zntMVc4TGus3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f637191d0.mp4?token=q7KHcfElprjWZBr3dvj74I44gP4SZV43OaxKknzfNuBf5358HsVXfDcU3lFhGf7EXsToS0N-teyblsIg9AvTaTRWYsgwehJA4ZpuMxXBnGevzO3yfsn0s4aR2NiUQY8KGOPe6WnP3ufR0gzfljvPvgHepJtAz7NBSKsG9kkKB8pVLe8oAxk65Tj6EZj51AbrPv4AlPDyp9Fnr-M5NIWdXFBGOvQ0sg297f8W7OKMlLpb1sUKmEgaF1cP6oEHKAmqeOFDzNmYbE_qQsmaX0KPtQt3czxrsnPnGMDHQthk9wMyN5tJ7zKJelmq64ITCyZvi6uI4xlN4zntMVc4TGus3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلاهبرداری از خریداران خانه در پوشش مشاور املاک با آگهی جعلی
پلیس اگاهی تهران بزرگ:
🔹
متهم قبلا در مشاور املاک کار می کرده است ؛ با درج آگهی جعلی به مشتریان تصاویری از خانه‌ها برای فروش و اجاره ارسال می‌نموده و سپس از مشتری بیانه ۱۰ تا ۵۰ میلیون دریافت می نمود
🔹
این پرونده ۴۰ شاکی دارد که طرح شکایت مطرح کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/684154" target="_blank">📅 10:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684153">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hobZJHoEj1VhZaW-BLEwJ6En7DfYg3xWcZTb39vuHSrzcr9bqrNzF5BRXxRzgy-vTs56ukEX2Mubh0Bo-8fWCPJY7phtViLww2Qlmkg6aoPMFDosCWHLuvBQUjV1uCOb006jzojGtLo2NYw7qjODzVAupOF5xMkwLQxy9X7_xeKZkNBOgoGJzgi-yVLsiirp_Hg_WQcVaNOAxZL3-Frp3GnOzCi5dgv2yslRSzboxTpTkV4s9V1QOq7Px3MnP0C0ilpaVZjR4W3u9FdzMznY4Yez1Vglb5SsNp6ILSfNFoYI1NUWFztO2yWy__scpe1iswxdkLQXhFSRw-mylV81jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکس روز ناسا
🔹
عکس روز ناسا سایه زمین را در طول ماه‌گرفتگی به نمایش می‌گذارد.
🔹
حفره غول‌پیکری که در این عکس می‌بینید، سیاه‌چاله نیست. این سایه زمین است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/684153" target="_blank">📅 10:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684152">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640bf74b28.mp4?token=C3y2XB0Pvl-AMfP6ze0SC0XQbb5HAx-x3Tg2k-QxpaT-lFPA8jOne3UkYFOgjmOL7XJWjcoA7HwZbHT2KP2FHyfp3Fsi6cyPrsM0F9mAGbbuLX79b8RvItY0P9ajGYgNxZ3hWF3UmI8IkyNsDJ6ehmFsjUUZvxA7iPh9V3M23i27LlMPXfRK5gI9tUD9m6GD4k8FnrDXN2DqYMJZFWwxN_Om1LulXMzU-S7GjVQy1m2NZmcKzcLRlCB55WQjhYcgeP8pf8Q966hK6wjpurMn2-f_cT60GVN-ZuU5Cpo1khfpJKsPti2I-NQGpXt-bOrDPlL7ngf7x6S_v51XZTybYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640bf74b28.mp4?token=C3y2XB0Pvl-AMfP6ze0SC0XQbb5HAx-x3Tg2k-QxpaT-lFPA8jOne3UkYFOgjmOL7XJWjcoA7HwZbHT2KP2FHyfp3Fsi6cyPrsM0F9mAGbbuLX79b8RvItY0P9ajGYgNxZ3hWF3UmI8IkyNsDJ6ehmFsjUUZvxA7iPh9V3M23i27LlMPXfRK5gI9tUD9m6GD4k8FnrDXN2DqYMJZFWwxN_Om1LulXMzU-S7GjVQy1m2NZmcKzcLRlCB55WQjhYcgeP8pf8Q966hK6wjpurMn2-f_cT60GVN-ZuU5Cpo1khfpJKsPti2I-NQGpXt-bOrDPlL7ngf7x6S_v51XZTybYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان در جنوب فرانسه برق هزاران خانوار را قطع کرد
🔹
گردباد و طوفان در جنوب فرانسه خسارات زیادی به بار آورده و منجر به قطع برق هزاران خانوار و اختلالات پروازی شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/684152" target="_blank">📅 10:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684150">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8ffe97176.mp4?token=EW4w57ja5HP4354bk5cA4-tedpMdbQSzJA-GggnrpC3FTxBxaWWAoiBb7ANwW7GzbWmjvL1k93croJodP618u2vks5ta-atxKOk5dJgcJ9Hdf6xQSr7msbIisEwhc5SnAysQIijowBE_ryBKpLqim3iCsh0-0FvPw-rB8wq61hgVD-S7p9-pLel2hTtI1AM_7JAKokAnEOiZxhTEvEEXIAGfFdomWnTTSQL13Fw91vtr8eQTBU9SOpoQhZt6-PddjoM6TD6u-ZZw8Cu_xDXvceHoJCZEKM_hjGdKR_tI2y8x6oMVx-mMdqTAUkb7l6Gk1EVjqdL0IvaFFzFbj42nHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8ffe97176.mp4?token=EW4w57ja5HP4354bk5cA4-tedpMdbQSzJA-GggnrpC3FTxBxaWWAoiBb7ANwW7GzbWmjvL1k93croJodP618u2vks5ta-atxKOk5dJgcJ9Hdf6xQSr7msbIisEwhc5SnAysQIijowBE_ryBKpLqim3iCsh0-0FvPw-rB8wq61hgVD-S7p9-pLel2hTtI1AM_7JAKokAnEOiZxhTEvEEXIAGfFdomWnTTSQL13Fw91vtr8eQTBU9SOpoQhZt6-PddjoM6TD6u-ZZw8Cu_xDXvceHoJCZEKM_hjGdKR_tI2y8x6oMVx-mMdqTAUkb7l6Gk1EVjqdL0IvaFFzFbj42nHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکبار هم که شده این مدل زرشک‌پلو با مرغ رو‌ درست کن، مطمئنم پشیمون نمیشی
😋
مواد لازم:
🔹
برنج دو پیمانه
🔹
مرغ ‌پخته نصف سینه
🔹
قارچ ۱۰۰ گرم
🔹
سیب‌زمینی یک عدد
🔹
زعفران
🔹
نمک و فلفل و پاپریکا و آویشن #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/684150" target="_blank">📅 10:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684149">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر آموزش و پرورش: برای اول مهر آمادگی ۱۰۰ درصدی داریم و کلاس‌ها به صورت حضوری برگزار خواهد شد
.
🔹
شرکت مدیریت منابع آب: ۴۵ درصد مخازن سدهای کشور خالی است.
🔹
نماینده پارلمان عراق: واشنگتن به دنبال سلطه بر کشور است.
🔹
روزنامه عبری: اقدام علیه ایران می‌تواند به جنگ اقتصادی جهانی تبدیل شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/684149" target="_blank">📅 09:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684148">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d8eabf04f.mp4?token=h20cu588hpMbynAmi04v8Tl8CU_Uz8Ddseaxma7lxc5crpaIg3P1UHDGGIgPldtKA-xc96tf-W0vh64hyzydqo4XWKiy6ZGAyBMZSHblDoEWkSoE6XSB4doXKUMNr3_qPg579JJhyBL0i1TQjNNViWON77FGSgi-_7OElW1QnRujyJEJhUValANLABECWuF9CM5_b80c3EYhf3ub_9nKW7wpl5iDyP0u_1S-GNCVMQrtAofLfJjT-xbhnmxfLt3ZlIH-Jns3ldRmC_jtYd-ObyG3PWCKxy3KiV1XyfWxSSlfDlez15xKGgRlFV10os3zeGW1vPJICdEnZRt2COJSTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d8eabf04f.mp4?token=h20cu588hpMbynAmi04v8Tl8CU_Uz8Ddseaxma7lxc5crpaIg3P1UHDGGIgPldtKA-xc96tf-W0vh64hyzydqo4XWKiy6ZGAyBMZSHblDoEWkSoE6XSB4doXKUMNr3_qPg579JJhyBL0i1TQjNNViWON77FGSgi-_7OElW1QnRujyJEJhUValANLABECWuF9CM5_b80c3EYhf3ub_9nKW7wpl5iDyP0u_1S-GNCVMQrtAofLfJjT-xbhnmxfLt3ZlIH-Jns3ldRmC_jtYd-ObyG3PWCKxy3KiV1XyfWxSSlfDlez15xKGgRlFV10os3zeGW1vPJICdEnZRt2COJSTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثبت یک شفق قطبی سفید نادر در نروژ
🔹
شفق قطبی معمولاً سبز، قرمز یا آبی است. با این حال، به‌گزارش ناسا، اختلاط گازهای جوی می‌تواند در صورت همپوشانی رنگ‌های مختلف، رنگ سفید نیز ایجاد کند که در نروژ این پدیده دیده شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/684148" target="_blank">📅 09:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684147">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBzYb2Mwpp0cvTxBnrmET3klUtdmo6u9TRdU5LldN6LC465vaB9LrhF-UPC27QSG5PkFAkEuy6AFD8yIrEmVVV1AeqOtvE9RaLyUw4QncKZEZ5CVV4jLbPWP9aflFLdM8eqk_Y5klqFdQIHoOIyjdSmHUSH6MzvADxxzeNaBku5ud1oTcADAxCwbB5A-DBwd5l7sDD6hXLHannnlA4tiP0J81jBbOy_BMLUocIazECKPcl9P5BGEnZsMDDzNfaAnREKhxN1HypiYcCg7UIIXy49d-ns30s2X43JwMcrPoGaNSKlQ12Xr0Od_bODrp84zOQhDXk1Qry23gwcCJPZsEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرشچیان: ممنوعیت واردات لوازم خانگی؛ شوک به بازار و هزینه جدید برای مردم
احمدرضا فرشچیان، عضو هیات نمایندگان اتاق ایران:
🔹
تغییر مداوم مقررات واردات لوازم خانگی، هر بار یک شوک جدید به بازار وارد می‌کند و در نهایت، هزینه این بی‌ثباتی و گرانی کالا را مردم از جیب خود می‌پردازند.
🔹
ممنوعیت‌های مقطعی واردات لوازم خانگی، تجارت را گران و کند می‌کند و منابع کشور را هدر می‌دهد.
🔹
به‌جای ممنوعیت واردات لوازم خانگی، باید از ابزار تعرفه‌ای استفاده کنیم. اگر واردات لوازم خانگی به نفع کشور است، باید پایدار باشد؛ نمی‌شود امروز واردات را آزاد کرد و فردا دوباره ممنوع کرد.
🔹
از مسیر کولبری و ملوانی هم باید از قواعد مالی و قانونی همراه با پرداخت حقوق گمرکی تبعیت کند.
🔹
مجوزهای کوتاه‌مدت سه یا شش‌ماهه برای واردات لوازم خانگی می‌تواند واردات را چند برابر کند؛ چون فعال اقتصادی تصور می‌کند فرصت واردات به‌زودی از بین می‌رود و همین موضوع «اشتهای کاذب» ایجاد می‌کند.
🔹
فرشچیان: تغییرات مقرراتی باید به حداقل برسد تا بازار لوازم خانگی و تجارت کشور بر پایه ثبات، برنامه‌ریزی و شفافیت حرکت کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/684147" target="_blank">📅 09:49 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684146">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnZD3-ULcOJRANCoL1142EpgWx2eragM5cZ0L5FsrtePAGp-bwl-Y5wqOjN9YI63wtkeCAHAKoOGT5SWgqn9wcUGM9cWEORYTKlcODQ5DNIAq4Q9UiMcu-a_00I9pWrB_VNCtS27aWj0bSauiabBL6Mx0v9XR-qxj18LI_ID4uI81kUlFqcet_d2qSgoA-uQc60V-1lMbj_U01m10MdU5pVV3wBoXe83ErwzZrG0MtANp0DObA-wmSLKJVyF1IDDP8zSX0fEDgowAZpjzE_EpNNT52Ynkt8eOz-nADpkIeYpOa0hMb9SzNkgLbK4bQ5umLYSJFi2octe4HmfgxPG5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشنگتن پست: تهدید‌های اسکات بسنت در صورت ادامه تجارت چین با ایران توخالی خواهد بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/684146" target="_blank">📅 09:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684145">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edf914bc14.mp4?token=GUopI-CC3dL8zWiIW5v6qz-DVn7M_OkDUyuT8PDZfpYMF-atQjiA_rH6ljZ8h_XsGspCxs--NVpjXJohGc6FOgCba5OWPaatDCxr0JnFGwsRudQla3Ht4NRa4If9oINDt5OoTq9dYmb6UxC6Zk5Wvb46sDkZ7YgkL0xaOVOuDGyEdGvLCcG-pz_PEVDWOmFIMIqCVgckG6onqOlpgqSnX6YqsQdvKldB4jl3XPd3m70vImHwlVZZeE3m_aVslPq6FOCGedqqZYPYGpeKgMJ3BvV2TizsmErPIcbtxagJLt9RN9zJH5HOvsOFztNCCsnzCEyd0NByGqvmQVztuAltRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edf914bc14.mp4?token=GUopI-CC3dL8zWiIW5v6qz-DVn7M_OkDUyuT8PDZfpYMF-atQjiA_rH6ljZ8h_XsGspCxs--NVpjXJohGc6FOgCba5OWPaatDCxr0JnFGwsRudQla3Ht4NRa4If9oINDt5OoTq9dYmb6UxC6Zk5Wvb46sDkZ7YgkL0xaOVOuDGyEdGvLCcG-pz_PEVDWOmFIMIqCVgckG6onqOlpgqSnX6YqsQdvKldB4jl3XPd3m70vImHwlVZZeE3m_aVslPq6FOCGedqqZYPYGpeKgMJ3BvV2TizsmErPIcbtxagJLt9RN9zJH5HOvsOFztNCCsnzCEyd0NByGqvmQVztuAltRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بزرگ‌ترین شمش طلای جهان، با وزن ۵۲۱.۲ کیلو در استرالیا تولید شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/684145" target="_blank">📅 09:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684144">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
رشد ۶۱ هزار واحدی شاخص بورس
🔹
شاخص کل بورس تهران در دقایق ابتدایی معاملات ۶۱ هزار واحد رشد کرد و در سطح ۶ میلیون و ۱۶۱ هزار واحد قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/684144" target="_blank">📅 09:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684143">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
آغاز ثبت‌نام مسکن استیجاری تهران و مشهد از فردا   وزارت راه و شهرسازی:
🔹
ثبت‌نام مسکن استیجاری زوج‌های جوان در تهران و مشهد از فردا آغاز می‌شود.
🔹
از ساعت ۱۲ روز سه‌شنبه ۳ شهریور تا پایان روز چهارشنبه ۴ شهریور متقاضیان مسکن استیجاری زوج‌های جوان در استان‌های…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/684143" target="_blank">📅 09:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684142">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b68eab9e4.mp4?token=kvyT4T3x0osNA7i_cpilOtGLx18seqhtgWOp3Qx502wZL6iqUROygfaEONSTZ6CFY21G2iZzdMDn5HWXtFZzkM5Up82MRdIhofLsrpKJ6CLZ4FkzwmEqbGAv2tN6LiXfHc4hp1L7uHObAYn1UyJkutkKIWqoyC3rvcjC2B4WVEJzOjtG4hLudkw-eMxKdXz-FmZTECQ9XV_7e6E11lDmGi3SHd1BAAonFKJh2_oeGZKb-CCpQsC3qndnGmKBCeFK_GKBe_UnQlGQAxA0CwOWOv8hrqMw0r-o-bIGLI9N_pn4yZ3vL-rrBa6-ysx6OIOlZKuFHHFI3-iplQqc6W8CPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b68eab9e4.mp4?token=kvyT4T3x0osNA7i_cpilOtGLx18seqhtgWOp3Qx502wZL6iqUROygfaEONSTZ6CFY21G2iZzdMDn5HWXtFZzkM5Up82MRdIhofLsrpKJ6CLZ4FkzwmEqbGAv2tN6LiXfHc4hp1L7uHObAYn1UyJkutkKIWqoyC3rvcjC2B4WVEJzOjtG4hLudkw-eMxKdXz-FmZTECQ9XV_7e6E11lDmGi3SHd1BAAonFKJh2_oeGZKb-CCpQsC3qndnGmKBCeFK_GKBe_UnQlGQAxA0CwOWOv8hrqMw0r-o-bIGLI9N_pn4yZ3vL-rrBa6-ysx6OIOlZKuFHHFI3-iplQqc6W8CPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جیانگ شوئه جین
،
کارشناس مسائل بین‌الملل: پاسخ ایران می‌تواند به جنگ اقتصادی آمریکا بسیار دردآور باشد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/684142" target="_blank">📅 09:28 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684141">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
معاون سرمایه انسانی سازمان اداری و استخدامی: تا پانزدهم شهریور ساعات کاری اداره‌ها ۷ تا ۱۳ و دوساعت بصورت دورکاری صورت می‌گیرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/684141" target="_blank">📅 09:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684140">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
یمن: کشورهای منطقه از پیوستن به تحریم‌های آمریکا علیه ایران خودداری کنند.
🔹
دبیرکل سازمان ملل: جنگ با ایران محدودیت قدرت ابرقدرت‌ها را نشان داد.
🔹
توپخانه رژیم صهیونیستی صبح امروز مناطقی در شمال اردوگاه البریج در مرکز غزه را هدف قرار داد.
🔹
حمله شبانه باندهای مسلح در هائیتی، دست‌کم ۴۷ نفر کشته و ۲۲ نفر زخمی شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/684140" target="_blank">📅 09:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684139">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
صدور آرای متهمین یکی از عجیب‌ترین پرونده‌های قضایی سال‌های اخیر کشور در استان هرمزگان
رئیس دادگستری هرمزگان:
🔹
حکم قطعی محکومیت افرادی که با سرقت از خطوط انتقال سوخت هواپیما، اقدام به قاچاق آن می‌کردند، صادر شد.
🔹
متهم اصلی به ۱۲ سال حبس، ۷۴ ضربه شلاق، ۲ سال محرومیت شغلی و پرداخت بیش از ۱۴۴ میلیارد ریال جزای نقدی محکوم شد.
🔹
متهم دوم نیز به ۵ سال و ۶ ماه حبس، ۷۴ ضربه شلاق، محرومیت شغلی و پرداخت بیش از ۵۷ میلیارد ریال جریمه محکوم شد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/684139" target="_blank">📅 08:56 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684138">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3472337bdf.mp4?token=uV8xHfE6RodWP1Q1gh9MEM9V8bO34OMyzMKYWUd5CB0YAsiEUgPpI59huWY9rL9h-2aX-ap_v7jAJc2Uy0mczQh1V8NSJ5zotU-1w8am94ckM7ZfWn8ZIszVn1Gc1R7QFG8LEWE9Vf47PaqOokfvI49AEAC9hiK-6UeGEDiVdFsfBBa6C9YoQ_Tfyui_zR245v03TdKrojOhKV4rsjr31HoGSrAh3MUDVkU_5HXyl52oIjiR9achT70R8H019kgPH5oaMGUwYl14YkZXQkRjnkqZI8LNJSjL2xZASNyEKjTiBA5FQA5fxUUSnFywmHAHSNikA_iu6Fu-CmzAakIF2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3472337bdf.mp4?token=uV8xHfE6RodWP1Q1gh9MEM9V8bO34OMyzMKYWUd5CB0YAsiEUgPpI59huWY9rL9h-2aX-ap_v7jAJc2Uy0mczQh1V8NSJ5zotU-1w8am94ckM7ZfWn8ZIszVn1Gc1R7QFG8LEWE9Vf47PaqOokfvI49AEAC9hiK-6UeGEDiVdFsfBBa6C9YoQ_Tfyui_zR245v03TdKrojOhKV4rsjr31HoGSrAh3MUDVkU_5HXyl52oIjiR9achT70R8H019kgPH5oaMGUwYl14YkZXQkRjnkqZI8LNJSjL2xZASNyEKjTiBA5FQA5fxUUSnFywmHAHSNikA_iu6Fu-CmzAakIF2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارت زرد برای یک ربات فوتبالیست
🔹
در بازی‌های جهانی ربات‌های انسان‌نما در پکن، داور به خاطر یک ضربه خشن به یک ربات کارت زرد نشان داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/684138" target="_blank">📅 08:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684137">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
کشتی‌های مرتبط با عربستان در لیست «پرخطر»
روزنامه انگلیسی فایننشال تایمز:
🔹
شرکت‌های بیمه در برخورد با کشتی‌های مرتبط با عربستان سعودی محتاط‌تر شده و آن‌ها را در زمره «کشتی‌های پرخطر» طبقه‌بندی می‌کنند.
🔹
عربستان سعودی در حال انجام مذاکراتی با واسطه‌ها در لندن برای دستیابی به یک سیستم حمایتی جهت بیمه در برابر مخاطرات کشتی‌ها است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/684137" target="_blank">📅 08:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684136">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNTSUIUk54b2plxFOTGbR0HMMYji2BwZ7cw9KyJuhetdmeG1j2bgJnGFFnDpq4xIW93v-jQiZE-wkvZWNoJmJbp6xFKnKDNvtPZmuznNiCGi3ljxy55oDAbu12QSauvlSNK-KyVi8DpMrFj148C5Q5Zn4Bc66Tf4rxmGTBHPGMSymBLlfFx_TBaX9BztX9wXUcmRh9fQQo6ZjeQ1Aohq_tIUOs9iVe1j9W21SaFKY4H0-_luvDwfg76Skgh1NWBeHDLhXtHGTk83wzSW8s8IKeINYhKRKQ6MFxXAOYpqb_fBvxa7erkUTJIYMG3BtY83FnCNiNUWj4jyrSZiRqx6kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رابرت مالی: ایران از مواضع اساسی خود عقب نشینی نمی‌کند
🔹
«رابرت مالی» نماینده ویژه سابق آمریکا در امور ایران در واکنش به کارزار فشار اقتصادی علیه ایران: تهران از مواضع اساسی خود عقب نشینی نمی‌کند و تسلیم نخواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/684136" target="_blank">📅 08:39 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684135">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wym1hmDtyT14FLHOhh2s8I2oCbfzQM3U6Lrjf5aLEa_NDqHb3CAv58C-NYgr7Gb8xHZHrngffa54LpaTSdv9S7QpqrFEBnKZIiLNNYzRhdhH3gQU9j5QxAFyzubtFYo7nU3XwvIBMR7JTOU8nNHU3ckpf45gPElrkoRVfdDq6DUSeWC46K7TKF86zgJG3L7t-KtydWvnTQCMxMfp-TTp-ZhglraXVitdiBBZidxZiXDfRqYKNznDmIVY7wlEno2CHInqXShK3RRghjt5dc-p6IrAljyNMgz8kVXAPPliAkJ3L71hJqH3tC6686BnA6Fkl-8M9C4p8uDnVRd-K4QyxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میلر مذاکره‌کننده ارشد سابق آمریکا: طنز ماجرا این است که اگر آمریکا وارد جنگ نمی‌شد، تنگه هرمز باز می‌ماند
♦️
در تاریخ دکمه بازگشت به عقب وجود ندارد و در نهایت، خشم حماسی به فاجعه‌ای بزرگ منجر خواهد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/684135" target="_blank">📅 08:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684134">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79b76fcf2a.mp4?token=iBSXfXRjL2SHx-HyfyJQNXsKbPvjD4-UA0LqXlwg4to4w2frh-_XAmYrXXZZ-pODTuZS6QIrujsjISolhZpShi20nDZAVBlp7j8T-4XmaP8zbLfDcoqWmSod6OlZ44X2YkEfARHcQfCu_LUitfsQ9qidmm1y3ZIFrzXXVmK1FnWIs-kWcvHXgZPjtn3CvyNF1_isI69XyxLuOYRktMpH07qNjX9L3OgYt4E_LlyM4KBPuaXRVOxMr8mYmfJuNP1tT37cse4pqbi-tP0wCwMCL5oJAmok8vrA48a0gqKRAW96JMSBMkd8xlknIq81j_RxZXfY2XJs4wcyOSUayYpS8YUvpxeZSOjstq44bFSwXYCpnZ2_N_k8-FBDlSX-w8-JBwgt2TKrBS98aF3A5DsVl2KlKjMexeTXEiG4v_yGw9q-CSidT-dR0ZEqIHfiEuFzOf3J2jp90DFr8kCeUuDH-PsBcp9Pp6okOMWgn5PUZvTfGX3frf6eajOooZs1iK_r3PEtZbS-96-UxDtrMGZmA6DySQwQJgqlhrFF9p9dZdVloGnMEH19o5C42P1RGrkf0R7RpDIYNf3loY7M22I_XOWMhjKwOMb4gkEzCtuODyZpEl2zF3pB1vuH5QMt_zuBJDDKPMvA6AJKR2QFE87_JV9Da-LoY7UD6My8WwkebOE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79b76fcf2a.mp4?token=iBSXfXRjL2SHx-HyfyJQNXsKbPvjD4-UA0LqXlwg4to4w2frh-_XAmYrXXZZ-pODTuZS6QIrujsjISolhZpShi20nDZAVBlp7j8T-4XmaP8zbLfDcoqWmSod6OlZ44X2YkEfARHcQfCu_LUitfsQ9qidmm1y3ZIFrzXXVmK1FnWIs-kWcvHXgZPjtn3CvyNF1_isI69XyxLuOYRktMpH07qNjX9L3OgYt4E_LlyM4KBPuaXRVOxMr8mYmfJuNP1tT37cse4pqbi-tP0wCwMCL5oJAmok8vrA48a0gqKRAW96JMSBMkd8xlknIq81j_RxZXfY2XJs4wcyOSUayYpS8YUvpxeZSOjstq44bFSwXYCpnZ2_N_k8-FBDlSX-w8-JBwgt2TKrBS98aF3A5DsVl2KlKjMexeTXEiG4v_yGw9q-CSidT-dR0ZEqIHfiEuFzOf3J2jp90DFr8kCeUuDH-PsBcp9Pp6okOMWgn5PUZvTfGX3frf6eajOooZs1iK_r3PEtZbS-96-UxDtrMGZmA6DySQwQJgqlhrFF9p9dZdVloGnMEH19o5C42P1RGrkf0R7RpDIYNf3loY7M22I_XOWMhjKwOMb4gkEzCtuODyZpEl2zF3pB1vuH5QMt_zuBJDDKPMvA6AJKR2QFE87_JV9Da-LoY7UD6My8WwkebOE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جفری ساکس:
غیرعادی ترین وضعیت تاریخ آمریکا عادی شده است
🔹
جفری ساکس با انتقاد از رفتارهای اخیر ترامپ متوهم گفت: تهدیدهای شدید و تغییر مواضع ناگهانی او به امری عادی تبدیل شده؛ این چیزی نیست جز عادی‌سازی کاملِ یک وضعیت کاملاً غیرعادی، من هرگز چیزی شبیه این ندیده‌ام.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/684134" target="_blank">📅 08:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684133">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
عضو هیات رئیسه مجلس: مجلس با هر نوع افزایش قیمت بنزین مخالف است
رفیعی:
🔹
مجلس به‌طور کلی با هر نوع افزایش قیمت بنزین مخالف است.
🔹
مردم نباید تاوان مشکلات موجود را بدهند.
🔹
با عدم تولید متناسب سوخت مواجه هستیم.
🔹
هنوز طرحی درباره بنزین نهایی نشده است./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/684133" target="_blank">📅 08:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684132">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3623ddd23.mp4?token=AcDGMcwus_P9DPRotzwDnuD2SIUiyowfua9wc5SKyi_0hMo_Bbe3MxCCp4J4ur5dqA_1ECx6XDs4J-jvox5RWvNdFMynj-jvnjAogsrM_NdCH_Q9MaApEG7nvJGEKcMtgdgoqK72HGCsAvzKDlB8TYKgB9A3Yz3NTKpAOHY9eJJNN2scc9Nt9WuYmCE8CPMA_AYt0ZC2iC3XHYlghaaOdjZBr6eHUYJOZ807pArzP6YMSjXBKgrrhSDb2OOJlQHcsEOwvJGm90GkBFhHe34dExGaDP60FPjEIeCyiQC8UhrrjXUYL-E3ZgRBfwCWuya2RcMXxYc0OeRg-B_LbBJXkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3623ddd23.mp4?token=AcDGMcwus_P9DPRotzwDnuD2SIUiyowfua9wc5SKyi_0hMo_Bbe3MxCCp4J4ur5dqA_1ECx6XDs4J-jvox5RWvNdFMynj-jvnjAogsrM_NdCH_Q9MaApEG7nvJGEKcMtgdgoqK72HGCsAvzKDlB8TYKgB9A3Yz3NTKpAOHY9eJJNN2scc9Nt9WuYmCE8CPMA_AYt0ZC2iC3XHYlghaaOdjZBr6eHUYJOZ807pArzP6YMSjXBKgrrhSDb2OOJlQHcsEOwvJGm90GkBFhHe34dExGaDP60FPjEIeCyiQC8UhrrjXUYL-E3ZgRBfwCWuya2RcMXxYc0OeRg-B_LbBJXkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیر مرد ایرانی: حتی اگر مجبور شویم خاک بخوریم، هرگز ایران را تسلیم نخواهیم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/684132" target="_blank">📅 08:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684131">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d858531b62.mp4?token=Z455jxGxH-1tPR7GC4u6VVYVSVN7hcmZAyLdGUy2RrzXu3bMkPc7NFkfFEuSk1IW6felSKGfBhXs17BQEeKQ8G11z5xtzVQ03iYjzLM-EG0qXEwhEd6gdShdfeywKqRPa2ApBvRFbiGGWsXDzAaAYuAC8FwCP6BW6FD-PqUursqk_IR4ohd9uM0TPexwwvS3vmC0enpKvVs3YGXswWsKF-iyT6apPs9M-FKU7oQA9Zb6VNLH1OIfj_Ye3n1_tkP4Pjr0VwhOQMEkd4kaGnjVQDz0TI8QPE2AZF5cmpq3bWhdp9pxtOZjnhRDwni8L2Elw3fftHrK17BrPbFZo7qLbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d858531b62.mp4?token=Z455jxGxH-1tPR7GC4u6VVYVSVN7hcmZAyLdGUy2RrzXu3bMkPc7NFkfFEuSk1IW6felSKGfBhXs17BQEeKQ8G11z5xtzVQ03iYjzLM-EG0qXEwhEd6gdShdfeywKqRPa2ApBvRFbiGGWsXDzAaAYuAC8FwCP6BW6FD-PqUursqk_IR4ohd9uM0TPexwwvS3vmC0enpKvVs3YGXswWsKF-iyT6apPs9M-FKU7oQA9Zb6VNLH1OIfj_Ye3n1_tkP4Pjr0VwhOQMEkd4kaGnjVQDz0TI8QPE2AZF5cmpq3bWhdp9pxtOZjnhRDwni8L2Elw3fftHrK17BrPbFZo7qLbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیراندازی در خانه‌ای در آمریکا؛ چند کودک کشته شدند
🔹
در پی تیراندازی یک فرد مسلح در خانه‌ای در شهر بیلینگز ایالت مونتانا آمریکا و آتش‌گرفتن این ساختمان، چند بزرگسال و چند کودک جان خود را از دست دادند و عامل تیراندازی نیز با شلیک گلوله به زندگی خود پایان داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/684131" target="_blank">📅 08:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684130">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0Y_3yRWq4eJRWntO19uas1vOFJH2e4ubNpOjsL3GW7tYjsBHtdl-zmbsmMgyqqX6lfel6J4r0oEw22FTgyxxwPmuN6VlOiRhlSKsRzYMS0an3TLycCepqb1vWjkVMdN6GqeohfjTX-LxKqg8R1-cU4Li99vUUZdxs0QErsmig4j01m0GlaEEdSXQy-MKO7dRjp_LKze4AjCXH0u-vokFWKIixASZZITUp6emGWju-2cW6_BPJLXOC4Zg9MKMIWaHr0kf_yszNtS3xyizGJgTI_NtfU45DowZaes9VApCUiGNSBcS4mjzwwtd4uGlNqr-VBFcS7c2ZEzCqPMVTuM8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرماندهان نظامی یمن خطاب به عربستان: موازنه قدرت تغییر کرده و معادلات جدیدی حاکم است
🔹
محمد ناصر العاطفی وزیر دفاع و یوسف حسن المدانی رئیس ستاد کل نیروهای مسلح یمن با تأکید بر تغییر موازنه قدرت، هشدار دادند که یمن ابزارهای ویرانگری در اختیار دارد که متجاوزان تاوان سنگینی خواهند داد و آنان راهی جز پذیرش یمن آزاد و مستقل وجود ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/684130" target="_blank">📅 08:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684129">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70ccf903d.mp4?token=Kq8brE9vkslIhjPE2r46HX4sqVgUjPAc3DHaYK4DJHMFKbDBRAf8pQtvdwzwC2VtoPHtWJKWg1uWUE6l394nxXDlbTi5nbBJyuaEbfZF9OGKmEIrBmgfV3k3FfQs5_q4f-dwHl2nGQCwiGvQB0Iesc7IcX9fMDr5yrd_1D1TYi_QNq0fBm4-aGAHHyDp8YIWmk4Pqi_klX6qe7BEgwGQatlDRt9Zdo64fY554ZG4kcKf67d5hFdNoSFufqXUSSPJREzMIycrhpE_nW6gWvyayqe5Byn9EDgzB8wS0Q-__AiqhBrgKCDWMtZZ0l8MO8VyVG4m1Amygnz7N87878zJNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70ccf903d.mp4?token=Kq8brE9vkslIhjPE2r46HX4sqVgUjPAc3DHaYK4DJHMFKbDBRAf8pQtvdwzwC2VtoPHtWJKWg1uWUE6l394nxXDlbTi5nbBJyuaEbfZF9OGKmEIrBmgfV3k3FfQs5_q4f-dwHl2nGQCwiGvQB0Iesc7IcX9fMDr5yrd_1D1TYi_QNq0fBm4-aGAHHyDp8YIWmk4Pqi_klX6qe7BEgwGQatlDRt9Zdo64fY554ZG4kcKf67d5hFdNoSFufqXUSSPJREzMIycrhpE_nW6gWvyayqe5Byn9EDgzB8wS0Q-__AiqhBrgKCDWMtZZ0l8MO8VyVG4m1Amygnz7N87878zJNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمرینات اصلاحی برای قوزپشتی یا کایفوز #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/684129" target="_blank">📅 08:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684128">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
بیانیه ارتش پاکستان در پایان سفر عاصم منیر به تهران: گفت‌وگوها بسیار سازنده بود
🔹
ارتش پاکستان در پایان سفر فرمانده ارتش این کشور به تهران اعلام کرد که عاصم منیر رایزنی‌های سازنده‌ای را با مسئولان بلندپایه جمهوری اسلامی ایران پیرامون صلح منطقه‌ای، جلوگیری…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/684128" target="_blank">📅 07:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684127">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
اعلام وضعیت اضطراری جنگنده F-۳۵ آمریکایی در حریم هوایی عربستان
🔹
گزارش‌های رسانه ای حاکی از آن است که یک فروند جنگنده از نوع F-۳۵ متعلق به ایالات متحده آمریکا، در حین پرواز بر فراز آسمان عربستان سعودی، وضعیت اضطراری اعلام کرده و متعاقباً وارد حریم هوایی اردن شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/684127" target="_blank">📅 07:48 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684126">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8enAKtTQtCTyITOA7O5JaO2q2RQxKoVxpibBdAXaD_EOrr2UQnAWgPG4631Htw8n2Gxqa7pbIAkYj2Ts5cFBwdsw-ZR6nj6x8hn5W74Wkr-2zquk6lUtwPTMOYq0k7QPo8oQcGyOzSMMuNc2EK5Y96_TLBAFFsznwAqTsEO0MpfayTUe5FzLbqvp2zjfH3N5K02xrYPELYMFUDP6Ra9DqXE9gg5Gfv8gt-h_hhBV-8JZ2XEzc8mJ37lsdz6xbDzc0N00uyS0ptlnFe1Hhr0uwEAWrrhSW_Q72yA_xPJebdk6pKUTfG_AOK8Ynnw1Turrcuf9JnoJeZrXqktTwegYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بامداد امروز؛ هدف قرارگرفتن یک نفتکش در تنگه هرمز
🔹
سازمان عملیات دریایی انگلیس: یک نفتکش در آب‌های ۱۷ کیلومتری منطقه «الشیشه» در شمال عمان، مورد اصابت یک پرتابه نامشخص قرار گرفت و موتورخانه آن از کار افتاده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/684126" target="_blank">📅 07:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684125">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHImDcCWXOpnSkIT-upZ43BbTVN5uRmyJs1jmVDU_f5Ue2xKfQXEF4lPN2SVTjqeZJmOoZEGaMXbiWXB3C2wz9OxKE5zkdRZX-Yb2fv8m924gSzThEC7P1Qvu9sG6ijlYDt8PYnCNM-BPpQ8THcFa-FORIIYSPSEdMueCwx6diLXeLLUcgX2ytZ_MSv6DWjuq8wtxmnhJJTo8YcA31w0I3q6rSG7GKf48YAtIX-lk-EtuLW9nXhUQGjBgQ3FqolDbS-jGREMWxl4WtldCOaNEJxkEezuEtcpJRQi2CBwlMgcczRahmGGCmyrm1FbLQd79uyYaigYgEyz2L_DaD4IGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این کلوچه‌ از بطری پلاستیکی ساخته می‌شود
🔹
پژوهشگران با استفاده از مخمرهای مهندسی‌شده، پلاستیک PET را به ترکیبات قابل استفاده برای تولید مواد غذایی تبدیل کرده‌اند.
🔹
این مواد با فیبر و نشاسته ترکیب و با چاپگر سه‌بعدی به شکل کلوچه درآمده‌اند.
🔹
این فناوری هنوز آزمایشی و پرهزینه است، اما می‌تواند در آینده برای تبدیل زباله پلاستیکی به مواد غذایی در شرایط خاص مثل فضا یا مناطق بحران‌زده کاربرد داشته باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/684125" target="_blank">📅 07:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684124">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRwVkZljwF46JH6wZ1cD9BETDGraCiytKV1iX0y6ByCDc_dGetIr8Xn5pwne5Su3MLkGsGQQv2-R9ex_pzzwZ0zn0T3kvPeWFnMcDo6ix_8JYNgLmlPZ5z6lH0htWqdWu26lU4HGjjVTHYH6uMAqUdGOCtufqWPfsPUYQi89WQlW1LMB28puk6juOd_sQ-KADEAOx98ibsAQKKRFZocIqlFeYP-cy3C64YJ6Ld5a5zsCOpmAhyt7LmBERRBkMpCqudJWJdnoI-VDcrXK3ky-h_Gw-yraTxhr3hwYAApm8Zv_zE9mBJ9e7tNbE7B4ICgeDW5oHTQjWq7gn0Hwm_wipg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمایت آمریکایی‌ها از جنگ علیه ایران به پایین‌ترین سطح رسید/محبوبیت ترامپ در کف ماند
🔹
حمایت افکار عمومی آمریکا از جنگ با ایران به پایین‌ترین سطح از روزهای ابتدایی درگیری رسید و محبوبیت دونالد ترامپ نیز در پایین‌ترین سطح خود باقی ماند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/684124" target="_blank">📅 07:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684123">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">#چند_خبر_کوتاه
🔹
طرح مقابله با نفوذ بیگانگان، در دستور کار صحن علنی امروز مجلس
🔹
کپلر: روز دوشنبه تنها یک کشتی حامل کالاهای اساسی از تنگه هرمز عبور کرد.
🔹
آمریکا در آستانه بزرگ‌ترین لغو ویزا؛ خطر اخراج ۲۰۰ هزار خارجی
🔹
اوکراین به یک پالایشگاه نفت در روسیه حمله کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/684123" target="_blank">📅 07:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684122">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
پزشکیان: زور و قلدری آمریکا راهگشا نیست؛ عاصم منیر: فرآیندها را با دقت دیپلماتیک پیش می‌بریم  رئیس‌جمهور در دیدار با فرمانده ارتش پاکستان:
🔹
آمریکا باید لحن و رویکرد خود در تعامل با ایران را اصلاح کند، چراکه تکیه بر زورگویی و قلدری، تنها فرآیندهای اجرایی…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/684122" target="_blank">📅 07:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684121">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8gB0mHTVAEpi1ev7JoAiMbZwZaLOcFDMGT4HygDOSNYvjRr0uSxH67X99oQfyYv86CnVnMGRi2y3aVzabasZ6dcvIQqwcR7FlwFh73CgEv6eleHm96UHbDM6PcfQ4rYCHUypG2JqmkTnIFesIsFNvHjd5kNEhm9f8snokEVGpJzJv0BzXBPQAy5ogo4sRSuOrfiRL13KmYpwJpeytUsv0oLuj1v52pQuJ9wqMH4d459E5-2CCYIe9fErCLs8pY23OfBQVn_1XJksXwg5kV8cb2M9vzFhMpl16zYiKHRrHO6AOjf8lUbUiobEVlC9tE0uPvUdXhkuK-oUYc6_8jfYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۳ شهریور ماه
۱۲ ربیع‌الأول ‌۱۴۴۸
۲۵ آگوست ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/684121" target="_blank">📅 07:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684119">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cwv7Q6k_13QhPJExip6CoQLztGYjEsI-iGb18WKw7YVC_gt68_PiKV8c0yVpoXpHs7YUkZyjvbbMcfISM2oyfOKlkq-SlEq3LDoEPKsR3ko9Dunn0_Uby-DpmwO6e1whjIIjOnmK_hX6N_mPrdP9sdhT35GeA5cHIv0appaGC55B9CRcgLDG2Rh8w23V8hSkgGIwJ26KZ6GMzCOX8tGx86CksY9yneZg6MH8joZGo0RqX1ZxGdtLnDVLOSk4bJSMwcJbiD0neDCjIKVnBTkxZtG9ZDby04k7_kXHx3IRl6f43ziR1WwlPM_dTCWbJDcWdbn4XiKmoSSrLJsWlPoI1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩺
سلامتی رو به شانس نسپارید!
فشار خون بالا معمولاً هیچ علامتی ندارد، اما می‌تواند خطرات جدی برای سلامتی ایجاد کند. با یک دستگاه فشارسنج خانگی، هر زمان که بخواهید در کمتر از چند دقیقه فشار خونتان را اندازه‌گیری کنید.
✅
اندازه‌گیری سریع و دقیق
✅
قابلیت تشخیص آریتمی
✅
تشخیص فشار دیاستولیک / سیستولیک
✅
حافظه ذخیره نتایج : بله
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
💰
قیمت قبلی: 1,698,000 تومان
🔥
قیمت ویژه: 1,398,000 تومان
📦
همین حالا سفارش دهید و با خیال راحت سلامت خود و
عزیزانتان را زیر نظر داشته باشید.
https://memarket24.ir/product/brief/41275/180124/</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/684119" target="_blank">📅 01:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684118">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
تأکید اندیشکده آمریکایی به نمایشی‌بودن تحریم‌های جدید علیه ایران
🔹
عضو ارشد اندیشکده بروکینگز با اشاره به طرح ادعایی آمریکا برای تشدید فشارهای اقتصادی علیه ایران گفت: طبق انتظارات، این طرح چیزی جز یک کارزار تبلیغاتی و پُرهیاهو نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/684118" target="_blank">📅 01:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684116">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6_LdznMtw4UQxNHrpdwaBrABHNHSXFXxikgXxx2j-DVApsCensHcFPeT35O8AhMIA5x47-Ar7R4iG8XGa5Z8JYAIxo_uGVJ_CyrDk2YdSz4L2OLOLbS5mMbFv2sPZpwGc7ir3YTVZIAeNeHVuy3hlDrpoWmDkRMBTnptDOuFQbyesQFOcGCt86GFR002cynB4FXtKdWcXi1P9Csq4wY5KTTz0XfQowhbPsj_MaddSX0oHSG1FiIPFBjRW3gVmvBRhHhh6ctFTh18s5Bk1houDtS9sxok3UqBHvlf9Jfr6pOqt2CCmbEbcPZRVZFiWV0mfUDtwB-4KBQmRWQTjdItQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82af1dfb6c.mp4?token=DZhENg8Tai9mXjrL4IcnOcRFPz8bb-TIjHylIgPg4DDc-XsK2aztG2DfUMrzjlh6HsEaSagleWOtI_snK797TcuT-yWsbb_EG46LhJPPH-qe4kt7aO36dxxL53TvIY9wxjYNuazt1uM995OjxK2YE2b2f5_qkxCS8SQzySRY662bdMZ0v-t6_RASjSX_GKu1jEAJJKHVONyqn90hZwDyui2FuBqxdeExyNEdIWJ2iA9K3_ekSi-J0a9dL5pG2kG0ghh2LAvu-VXq8VeB7FvsNlN_fAvbr5vLKfxw2JPX2_hdMGMHsmQ_9MHxEb-X6A_UlmmqCT1zABWhSG5P3IQk0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82af1dfb6c.mp4?token=DZhENg8Tai9mXjrL4IcnOcRFPz8bb-TIjHylIgPg4DDc-XsK2aztG2DfUMrzjlh6HsEaSagleWOtI_snK797TcuT-yWsbb_EG46LhJPPH-qe4kt7aO36dxxL53TvIY9wxjYNuazt1uM995OjxK2YE2b2f5_qkxCS8SQzySRY662bdMZ0v-t6_RASjSX_GKu1jEAJJKHVONyqn90hZwDyui2FuBqxdeExyNEdIWJ2iA9K3_ekSi-J0a9dL5pG2kG0ghh2LAvu-VXq8VeB7FvsNlN_fAvbr5vLKfxw2JPX2_hdMGMHsmQ_9MHxEb-X6A_UlmmqCT1zABWhSG5P3IQk0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش طعنه‌آمیزسفارت ایران در آفریقای جنوبی به گزافه‌گویی‌های وزیر خزانه‌داری آمریکا درحالیکه بدهی آمریکا از ۴۰ تریلیون دلار عبور کرده: مهار کسری بودجه توسط وزیر خزانه‌داری نادان آمریکا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/684116" target="_blank">📅 01:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684115">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قشقاوی:
همان جوانی که پهپاد ساخت، می‌تواند اقتصاد را هم متحول کند
حسن قشقاوی، سخنگوی کمیسیون امنیت ملی و سیاست خارجی در
#گفتگو
با خبرفوری:
🔹
همان‌طور که جوانان ما در حوزه آفندی و پدافندی نظامی توانمندی‌هایشان را به دنیا نشان دادند، در حوزه اقتصادی هم باید بتوانند این توانمندی را نشان دهند و آثار تحریم‌ها را خنثی کنیم.
🔹
همان جوانی که پهپاد ساخت، می‌تواند در اقتصاد هم خلاقیت و توانمندی خودش را نشان دهد، باید بستر حضور جوانان در اقتصاد فراهم شود.
🔹
اگر کسی ۱۰ کارخانه دارد باید تشویق کنیم تا ۲۰ کارخانه داشته باشد و اگر ۲۰ کارخانه دارد بتواند ۱۰۰ کارخانه ایجاد کند. نباید در تولید محدودیتی ایجاد کنیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/684115" target="_blank">📅 01:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684114">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9872e711e2.mp4?token=paBRwtuB69F503kpVPuQ93OXGbcPUk1Qhfvn_Wk414vlpAMlxuj61td6P4qk7PSFQjWKqxn9hykF_CH-3mtbQX2smamxABOUu3-Np2Q5q-E64qhRgnLrJZAniUCTX0PGH4XjNcGTzj8BkiD24y9TxOZXSHYvwkNiEgXVD5qwvfgxi5LRUmwoQ_i-N8MfOtY4ID6UXEFbqmkBYAReF17jSR8e_qQ2TAzLa_tjz8SzttkVtMkcyTljGUxQZTJK5a_Jo7n_0MFbDahi0lG5IgYNUyBinG3wbuwfuetKW9RZUqClyPvxQ4lEyujBica3rUI7ef6errdfsf7RRZXobwwxyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9872e711e2.mp4?token=paBRwtuB69F503kpVPuQ93OXGbcPUk1Qhfvn_Wk414vlpAMlxuj61td6P4qk7PSFQjWKqxn9hykF_CH-3mtbQX2smamxABOUu3-Np2Q5q-E64qhRgnLrJZAniUCTX0PGH4XjNcGTzj8BkiD24y9TxOZXSHYvwkNiEgXVD5qwvfgxi5LRUmwoQ_i-N8MfOtY4ID6UXEFbqmkBYAReF17jSR8e_qQ2TAzLa_tjz8SzttkVtMkcyTljGUxQZTJK5a_Jo7n_0MFbDahi0lG5IgYNUyBinG3wbuwfuetKW9RZUqClyPvxQ4lEyujBica3rUI7ef6errdfsf7RRZXobwwxyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس سی‌ان‌ان: ایران آماده مقابله با تهاجم اقتصادی آمریکاست
🔹
شبکه «سی‌ان‌ان» در ویژه برنامه خود در خصوص جنگ اقتصادی آمریکا علیه ایران با «جاستین وولفرز» استاد اقتصاد دانشگاه میشیگان و سرهنگ «سدریک لیتون» تحلیلگر نظامی گفت‌وگو کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/684114" target="_blank">📅 01:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684113">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrUxArsxXAh0oMR9GFgMTBkLcJSdnhG-ugjTgg2AHokSPOIxnejqpr0q4WdhvCw827lBbhlK6_Cq8W2amt7by3yJrbTehOC5Co-6FkGHmlKif4ptDPnnNiHCqeMAUvxJQsihvuvXi-iG3InIlGbvMCnQyxoROMVoarkwwf52YT6Jh_vdQOMmbzC1JE3e1gpA_4d6losGpquSDMnnpmFnDkOtTTss3mj7YXG9Gc_k49pzFnGaDkeaB-0uQ64721giYWgqGvAE4PrRQ_he27GLX5-v2TT-d1v16kL7Nb32YDP2uDasQz8rcQyPfsbgSQiJVuLq-2ZHpq1Oeg-s-Rln1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد مرندی، تحلیلگر سیاسی: در جریان دیدار آقای عاصم منیر و دکتر قالیباف، پیش‌شرط‌های ایران برای بازگشایی تنگه مورد بحث قرار گرفت
🔹
میانجی پاکستانی، ضمن انتقال دیدگاه دولت ترامپ، موضع ایران درباره مسیر پیش‌رو را دریافت کرد؛ نخستین گام در این مسیر، اجرای این پیش‌شرط‌ها از سوی آمریکا است. به احتمال زیاد، عاصم منیر اکنون موضع تهران را به واشنگتن منتقل خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/684113" target="_blank">📅 00:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684112">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEwAJ_etfMM8nR2dX8qOSSzd_kQtp3dT8g6NUeqir7P8sqr_jWrIwn5qx3Oku6MGX2B9YdRbTwyBsYsKrCT0kL07K-QpBpTaGfsRjTgYdJZFp0tzN4BdZ1KaE30WNSFTUKofPDEC5-f7P70QRqHL8XUprwWtfNThun5yi5l0U3w3nRR6UACOre1WUn-RnB7Sq9WK5I0fJoiYkDNMYTnt4kHpOK_7mOo0him4FNgDPQEFVk36hJ78dWrt2Mf8QAY546_vAkiJHtsppDtl9YrDsVdMY3FDG9CodUsPkGTJzdPtOjg9oedk9g3vRXGNm00AORdhRfL7nrU0MsMqXabSTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه GBC:دونالد ترامپ در مسیر تبدیل شدن به احمق‌ترین رئیس‌جمهور در تاریخ ایالات متحده قرار دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/684112" target="_blank">📅 00:49 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684111">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LALPFwJcS-Blpaz8mizV7SDurVc4u0XHfyaEGylED0BnnnoGwqXZWKT5F0RrmZzfVkdLEvQAGxtJnhzy6XLjqJXTEavGThONcYHkendu66l6XEr6o0rksozeD-90Qto3BMu6BoXNdVwQZFsTjFczpH781uIhRiVRVzfQPhgfLDlBv8spzMQ5wh3gkSGZ6WsnPi9FcuxqFFSgg13N_1L60Z1pCsTFsEA8tkavuCCCgQksGE2hCvffOGJUZ3CWgI4IZXKMjKL6VhR9p9oqkeN32SIMbPhZmjHRHEBHcgUiZgVsGuq13B262lg-37QLrsM50ugSCIdyyIrIt28jxDMRoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آنسا: جنگ در ایران به ایتالیا ۱۲ میلیارد یورو هزینه ایجاد کرد
خبرگزاری آنسا:
🔹
ایتالیا اعلام کرد که با جنگ در ایران، ایتالیا با هزینه انرژی نزدیک به ۱۲ میلیارد یورو روبرو است.
🔹
افزایش هزینه بنزین و گازوئیل را در دوره شش ماهه تقریباً ۵.۸ میلیارد یورو تخمین می‌زند. هزینه سوخت ۵.۸ میلیارد یورو، هزینه برق ۳.۸ میلیارد یورو، مشاغل کوچک بیشترین آسیب را می‌بینند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/684111" target="_blank">📅 00:45 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
