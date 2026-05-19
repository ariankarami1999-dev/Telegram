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
<img src="https://cdn4.telesco.pe/file/PFF_fqcfT7S9ZitWt0ouashaK2auqZLOOfUf9RaFpWbiA4ZZelNs-Uy1IkR6oPsC-1DfU7dvaBhf0fuL6InidoOn-SA8Fj2hfCC1xfE4XzNkC2jrKW27Fk3klM42R5Uq3pBEdBXGxC4fu1axG9gW_whGOe7ZUmouKVo5pRAAHOSCo2rdfmNn6s-m3roMeQ0ulDkd43URpfhMpvEtEDe5t_ObLIfdFfRuOwjN2T3lyClNslRjMm1ske3caU1OgnAolMwJiiNTNFb_Q26Swe-a3er0oiUmW770rie2taGRseeUtyDfjxWZ37c3at7rROnUzaGvBTdNq1NOAPPw4lB3CQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 14:16:55</div>
<hr>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sypTZV1vIjeI7eIZT8v9hz1EQc_lP7yhE61zkCt4YdBI7GD6XVDhT4n9V9PuY_GZ-bCO2I7wjVyBSxU2z_XaOuG97KApb87uMSjTma_2N0OCYzs5KaQdewxdQ5VgeBJHwkso18nsFOEvbHS4G6ZpfEfOF34Qe9NiIWuWi0cnqUGn73gX3wU1v3Vl8tKV_TPFcoQ-MI0vOCPt7AAXs_afHszQdE8OcDj_w7IG45_ex-FflSll-LIAxBVLoQY5iKzplfZ-tXbTYgEQFPa7ePs7W07I-jTV32hJAZ4ZA7N7BysRkYAdNCa063E-qP9AhwQBd1Vt0UtUaYMx1nx3tQYtww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست‌های ترامپ اینها رو گیج کرده ،
آشنا که «معاون ویژه وزارت اطلاعات» بود و بعدها رئیس مرکز بررسی‌های استراتژیک در دولت روحانی شد نوشته که شاید «از عقب» وارد بشن!  :)</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farahmand_alipour/5052" target="_blank">📅 12:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1T0I1r9fQwHM4B-imEB675behykA-L6MpQiZ98i40kXJS--SQMazXi44oNktcIQFVcfcpK-bzpQElHG5mArbEgQ9vM3A2Ubk3g8auZka4sJHjq1grnBHBxd_cK1UHcyjonAzacL4faeaTn4vqUmTtWM25UqEUifUP2DJ3NgsoZ0Tth8GhIVoBDRttrhZ0ZBk5lm9r7dpuxzvkaFv7bmmpHbCXVCAqc5DVctbjMADuak9dvySqgw9EfcI75aZaGl638Dl5a6E_dY09ffhdUjlJj7jix8S8f7KK79s-NcE-lGXr_UzgTtXxUbG8uvUffwPxxBcUH5Xtjfw4GKFp20RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان که ۸ هزار نیرو و سامانه دفاعی موشکی و یک اسکادران جنگنده در عربستان برای دفاع از ارتش عربستان
در برابر «تهدیدها»! مستقر کرده گفته آماده است در صورت نیاز این تعداد را به ۸۰ هزار نیرو برساند!
تمام حقوق این نظامیان بر عهده عربستان خواهد بود. مقامات عربستانی در سال‌های اخیر هم بارها گفته بودند که «سلاح هسته‌ای پاکستان» در خدمت دفاع
از «حرمین شریفین» است!</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farahmand_alipour/5051" target="_blank">📅 12:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpthwZgIkbMA7sCVK_0cl6bHgWl6QYolfQcn9gsCb3SShyFHUC4APvsnvWoB7qXrEamAEcedjQySTX8EdvftiFBhN6rh0wTzB7OuGZzy2OY1wG-ihxvTB5wtuyK1ADoSxEcqg63GK2UPDrOtgtZ3IgSUCz-nszcGFkOptyescNLpDv4Jr2iDaAXIPOsvFZ2jlV4Vpwt307Oz_huSF9-Irm5LvVqMZHx_2oMgEcIVIvdirY4wwFP106_GzVBTqnqb2v1SklDGy927LUw4mL9SWpXNyvW4lfZzBd4mj3IJxm3R9W1FAcHeFBf3EqA_wKRPP6wd-YOrIyFIO7aPJkNPTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود این جمله :
رئیسی شاخص و مدل عینی
حاکمیت اسلامی است!
نهایت الگوی اینها فردی شبیه رئیسی است! که دیگه همه به چشم دیدیم
کی بود و چی بود و چه کرد!</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farahmand_alipour/5050" target="_blank">📅 11:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BB7nxT2BVsuKQrRsYOAEjZCdn0nTXXohY1afTJUFHov2tn9Esb0UXvG9H9cPBUrzn7WSzwhMnk_Nw9nZSHL5HIo1N9bKHE8uylxdZc1_uvZEQ9U00cmRv6wMP812twnMYMCrTdcjQEUe4IWHZIxwChmvX1ZQNfTQErvSc8iiauM1ZldpwU_7KSQB4v_I_DPP9A1cqSc-IZtpcTpOFC4jPiTQQ4UAfjBuSVCDz8Nu9mov61TfqZ6hqCF3RKw0S68fE2LP2Lj1Q0DGNGGkcUQNUDFtpa0dBQHJ6_AbHhBVplrbTOK3sUbxk-hP-C6CRqkLMtoxvfmMk3rRxegruGFMng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر توییت ترامپ که میخواستم حمله کنم به خاطر کشورهای عربی حمله نکردم و…. بر بهای نفت در بازارهای جهانی.
کاهش حدود ۷ دلاری بهای نفت</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5049" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=Hab7rxLjKBW_c-g6GVDqzjAY0oIK0zQyGUjJC-0OqiLxVScmJLXmoydUAgQ4pNIDnS4NW3_-puMwMJfgsE8dBhMRoTjUZm0garwHvWM1bD87l0JTnXnCxp7H8JhkmMpx6OA7Xu739TWT-g65eboRZFBlaMPkOWxwBNH3PZiukn6fke423yKSxKwyYXyrTWc24fn_u1DW4ilrW7Aym6tJRUSqInDFglcb-jAe6JRzsAStVowxz0gUwM69lP5JbuE6IqSx0TYvWAQ2u0xxKsM3ytr_im0cGE1NcVv-UiMVhE49ipIbkeqtJdpYTEcoI2R82PplkIyAqMvtop4pyscgUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=Hab7rxLjKBW_c-g6GVDqzjAY0oIK0zQyGUjJC-0OqiLxVScmJLXmoydUAgQ4pNIDnS4NW3_-puMwMJfgsE8dBhMRoTjUZm0garwHvWM1bD87l0JTnXnCxp7H8JhkmMpx6OA7Xu739TWT-g65eboRZFBlaMPkOWxwBNH3PZiukn6fke423yKSxKwyYXyrTWc24fn_u1DW4ilrW7Aym6tJRUSqInDFglcb-jAe6JRzsAStVowxz0gUwM69lP5JbuE6IqSx0TYvWAQ2u0xxKsM3ytr_im0cGE1NcVv-UiMVhE49ipIbkeqtJdpYTEcoI2R82PplkIyAqMvtop4pyscgUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعال شدن پدافند در اصفهان</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5048" target="_blank">📅 00:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5047" target="_blank">📅 00:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5046" target="_blank">📅 23:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ :  از طرف امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و رئیس امارات متحده عربی، محمد بن زاید آل نهیان، درخواست شده که حمله نظامی برنامه‌ریزی‌شده ما به جمهوری اسلامی ایران را که قرار بود فردا انجام شود، به تعویق بیندازیم.
آن‌ها اعلام کردند که مذاکرات جدی در حال انجام است و به نظر آن‌ها، به عنوان رهبران بزرگ و متحدان ما، توافقی حاصل خواهد شد که برای ایالات متحده آمریکا و همه کشورهای خاورمیانه و فراتر از آن، بسیار قابل قبول خواهد بود.
این توافق مهم‌ترین بخشش این است که
ایران هرگز سلاح هسته‌ای نخواهد داشت!
با احترامی که برای این رهبران قائل هستم، به وزیر جنگ، پیت هگسث، رئیس ستاد مشترک ارتش، ژنرال دنیل کین، و نیروهای مسلح ایالات متحده دستور دادم که حمله برنامه‌ریزی‌شده فردا به ایران انجام نشود.
اما همزمان به آن‌ها دستور دادم که برای انجام یک حمله تمام‌عیار و گسترده به ایران، در هر لحظه‌ای که لازم باشد، کاملاً آماده باشند، در صورتی که توافقی قابل قبول حاصل نشود.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5045" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مقامات پاکستانی هر ۱۰-۱۵ دقیقه یکبار میگن به دستیابی به توافق بین ایران و آمریکا خوش‌بین هستن.
موضوعی که نشون میده وضعیت برخلاف حرفهای مقامات پاکستانی اصلا خوب نیست.
🔺
یک : پاکستان در کنار بنگلادش یکی از متضررترین کشورها از بسته شدن تنگه هرمز بوده. اقتصادش دچار ضربه بسیار سنگینی شده و باز شدن این تنگه برای پاکستان و اقتصادش، به یک «ضرورت» تبدیل شده.
پاکستان فقط برای یک ژست در سطح جهانی در پی رسیدن ایران و آمریکا به توافق نیست!  بلکه برای نجات اقتصاد کشورش دست و پا می‌زنه.
🔺
دو : پاکستان قرارداد امنیتی دوجانبه با عربستان داره و در صورتی که جنگی بین ایران و عربستان رخ بده، وضعیت پاکستان بسیار دشوار خواهد شد چون بر اساس این قرارداد باید مشارکت پیدا کنه در دفاع از عربستان، همین امروز هم ۸ هزار سرباز و یک اسکادران جنگنده در عربستان مستقر کرد و البته سیستم‌های دفاع موشکی،
پیامی به عربستان که در کنارت هستیم و پیامی به ایران!
اما وقوع جنگ بین ایران و عربستان، برای پاکستان یک کابوسه! خصوصا اینکه جمهوری اسلامی در پاکستان نفوذ زیادی داره، اما ارتش، دولت و نهادهای امینتی همه با عربستان رابطه بسیار گرم دارند.
🔺
در روزهای اخیر خبرهایی منتشر شده بود که پاکستان مواضع ایران را به طور مثبت‌تری به آمریکا منتقل می‌کند و همین باعث سوتفاهم‌هایی شده بود.
بهرصورت اینکه پاکستان امروز دائم تاکید میکنه که همه چی خوبه، میشه حدس زد، وضعیت وخیمه.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5044" target="_blank">📅 20:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=XD5xZqUvgRkK1pE8xj_b0YoD6f71n2v9Y0W8Xymb2inyRHzFZ0iHEMlMoijcYNBw62NQK2AKMNHcmgSLjb9RVDZlKSyRjEFobHYDEt58euIRm8r5Nykc_ckC4TTX3GCpUaqaiEL2diCYdwFysSmY2BscNV1888fJc3cPYT_GvuOBRKMAbdh0MsJo0Rp7O5DVeW66U_DD7z6UqVp3k99hyBVDz9-52IrLTbgyH-GD1DDdT6G3evBVPqP_o-rxYfywVOrU-85FUZw1D3gRufQt_qwEDWcs7mMlYruIVgtxE6Xx6hv8CvVeGShS7fYUefI57x7wOxdTXzEy3PNa_AljzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=XD5xZqUvgRkK1pE8xj_b0YoD6f71n2v9Y0W8Xymb2inyRHzFZ0iHEMlMoijcYNBw62NQK2AKMNHcmgSLjb9RVDZlKSyRjEFobHYDEt58euIRm8r5Nykc_ckC4TTX3GCpUaqaiEL2diCYdwFysSmY2BscNV1888fJc3cPYT_GvuOBRKMAbdh0MsJo0Rp7O5DVeW66U_DD7z6UqVp3k99hyBVDz9-52IrLTbgyH-GD1DDdT6G3evBVPqP_o-rxYfywVOrU-85FUZw1D3gRufQt_qwEDWcs7mMlYruIVgtxE6Xx6hv8CvVeGShS7fYUefI57x7wOxdTXzEy3PNa_AljzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‏رویترز: پاکستان [کشور میانجی‌گر میان ایران و آمریکا]  در چارچوب پیمان دفاعی، یک اسکادران جنگنده، ۸۰۰۰ نیرو و سامانه پدافند هوایی به عربستان سعودی اعزام کرده است!
سامانه پدافند هوایی برای مقابله با موشک‌های جمهوری اسلامی است لابد!
پیش از این
مصر هم یک اسکادران جنگنده و خلبان در امارات
مستقر کرده بود و به ایران هشدار داره بود.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5042" target="_blank">📅 16:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5041" target="_blank">📅 13:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏
🚨
رویترز: پاکستان دیشب پیشنهاد اصلاح‌شده ایران برای پایان دادن به جنگ با آمریکا را ارسال کرده است.
🔺
دیروز مارکو روبیو وزیر خارجه آمریکا  گفته بود که «پروژه آزادی» (عملیات آزادی تنگه هرمز) به درخواست پاکستان متوقف شده بود زیرا که پاکستان گفته بود که توقف این عملیات می‌تواند به دستیابی به توافق با ایران کمک کند.
موضوعی که در نهایت رخ نداد و هیچ‌گونه توافقی حاصل نشد.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5040" target="_blank">📅 12:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8KHSUCPPNm9cRF6DQf-9VAThw4tHtuo8e6nXu1d78RzS9fStZKNpOHeePjVUr0LwZ3qhdywpsR9QOQaHjQF5YRs_nBP4XEnPE32BP8rarwiaMeVpmp9oNSUZTp4IFrX9pI2V_Dq63wxgT8I_5Q0rYdI-5UGYKC9bZvPI9Qf_s2neaAXGzKiUCwALDFTmSh-wHDC-Ycm-7N6QiMz4FfpiVZXQlzNxvql3kFSCve1AK9AI_KWyUCEv3dwDRogpvVvbg7BcfkGsd5fDFA9pH71Xa2BwQGkzOMdr7CiNSni-HgOh64VmRdvDHkA1QO4qDyYASKMizw-EjdkAIe6VPc3mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبه و مغز متفکرشون، فواد ایزدی می‌گفت، سالی ۱۲۵ میلیارد دلار! ۴ سال، ۵۰۰ میلیارد دلار!  هی «غنائم احد » رو افزایش میدادن!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5039" target="_blank">📅 11:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPoewp7_F5K-yeoIsycLFhr198zjQU72kDwL3Dbt9FmG2h88H2S8xlSDwvYwIsfz0u7jDXNTch9t68O45q4Otl_BVvpuBNAVIwHLrAt88URtZY_YM0yz6JEiqI9Cbh8k90yrvl342rleODHuCPxq6WllhjxPlEDtn6TxMSSc_3-ySo1nEss8ezJeGY222SIpxm6wxk10TE2Xe55Gll--yo80BojmLohaUPEL5GQWgf3a5DrTUMLg9ey81puuVZL-0Sb7-4SlwXuNWyR3gGCbSNDTuh1Yafrmvy7oI2VYxWn13kbHgyNZdPk6ZyyNsrxRb4Iuij8SJsyZQ5Wo0-QF3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی ۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!  توی ایستگاه مترو هم از زبان رویترز  نوشتن که قراره ۱۰۰ میلیارد دلار درآمد داشته باشیم!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5038" target="_blank">📅 11:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QwifmdBDtbdhFfIvHONMiVwrEkx-JZLowYgoTelcQnuZaOTFRWZbmVnFBceJXZuPQUPQRu5ViPW1IBIgEs2-uJtjxQ7BYW5RyP49E3okMnX0_GWnlUGbaa6XqnOmshglnD9hnqjRDyXkXpeZ0O47CtnGm2A7vB_3wIwJ2nWA906hyeE_UXjqAFj9-tjbdLiTdr2TKRneKdyWDJqcp6tOeJVSCTMnRFwfjNmWY_9qyvXQiuoRvSP41TlfTPlII-zysUNLkloLjAixika-1qaaKnWhyLjj0QxOuA_OL2j9-GjNBOmPtyByasr-M91yumF9tCkqvJ4bsXLNDhx5BZST1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DTW09uoG9JfIZJyuKf6LgxGxJx6nzdYBOLGQdOcpZEOE1cljlj4_aqizurn8fG1UN-r9X1ymuVCzmdsJudP4b0P1Wg5Qy-RHEinaepHUJnWnd4f_PkVW6-LlHYPukitp_Pvm_59rS0Y2ynrSAqZzC4ReFS0XpPzhSwqbJK-rtwxpjzLlh8EhH7ZgVoIjTU2du43fUowjMoxGAvKCyxqeAXETZ34YHo5HerjIBPxs_9sHNNGoV55K90-Bre0qhqsPsO9NqypthSNeIgR8pyjfGBVYrXRdlmIDI76SD3HTxzIyuDJHJHWB3dbdY1wTnfq-syNwvIneiK5zoQ6kj4ElxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی
۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!
توی ایستگاه مترو هم از زبان رویترز
نوشتن که قراره ۱۰۰ میلیارد دلار درآمد
داشته باشیم!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5036" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=ZKTS8IZmm0bMEGax88dF-3t8QBnOjqy0s6DbBaSrdUsmhSh6mZ_ua5BmhgF5SKWeDhlizrOlDc-cPPjTFXRdjoR52UUhO64SEQ2Ao-9912SspFTaT23RU_Y_RHwo3psaqKO0idKmzwhTkxxo7eR4dGGrCs0fIFcs9pfg_gA3W-hZCfP4L_o8DX_bL8DSx5FHSCOKnNDNWlQmbxUf8pYnqst-lYL7x_GQyMnJtKb9Q9pkLlZDeaV5amLLExz6es3fsnMFQDE2S_fhuwP2Ymb_e4MuZH5xM3UWXPaZ_5YO3D011RJhxGVMxBpXJIEvYiuj_CaT-v0iiI-Y8bhwf8OloA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=ZKTS8IZmm0bMEGax88dF-3t8QBnOjqy0s6DbBaSrdUsmhSh6mZ_ua5BmhgF5SKWeDhlizrOlDc-cPPjTFXRdjoR52UUhO64SEQ2Ao-9912SspFTaT23RU_Y_RHwo3psaqKO0idKmzwhTkxxo7eR4dGGrCs0fIFcs9pfg_gA3W-hZCfP4L_o8DX_bL8DSx5FHSCOKnNDNWlQmbxUf8pYnqst-lYL7x_GQyMnJtKb9Q9pkLlZDeaV5amLLExz6es3fsnMFQDE2S_fhuwP2Ymb_e4MuZH5xM3UWXPaZ_5YO3D011RJhxGVMxBpXJIEvYiuj_CaT-v0iiI-Y8bhwf8OloA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسلسل بردن تلویزیون و آموزش رگبار میدن!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5035" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=VNbEWbtrAZbGWNDjT8f29cPSAanDxgRfP30qXcUDZrk6kK9rxcl0_IreypDGMCm7mlS2IMSqeFBEZ3eD8Zpi6RGrK_ff4ptO57PtGg7J5DJ6KzwjycUMqDjPAN28f38mqkMYcNqIGzKgdziN6rAPCIfc37MPpqjlMxkQeP-Kt5zYBlKdnc1evV7qpwOpMBGYcUnKUstA0En_sa4X-lr-M2wnwyI0Wl_1eiEo7CrMNuf87aUNbwYvyWPO5OYvBcJx4aRy_SFdW6UIpVoj8ol9LdoQCSPsxKj4SW8L8VBEe8whdJBgaDcfREUmAWlqIPKzfvLlfOG6dhhY4fMg1dlRLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=VNbEWbtrAZbGWNDjT8f29cPSAanDxgRfP30qXcUDZrk6kK9rxcl0_IreypDGMCm7mlS2IMSqeFBEZ3eD8Zpi6RGrK_ff4ptO57PtGg7J5DJ6KzwjycUMqDjPAN28f38mqkMYcNqIGzKgdziN6rAPCIfc37MPpqjlMxkQeP-Kt5zYBlKdnc1evV7qpwOpMBGYcUnKUstA0En_sa4X-lr-M2wnwyI0Wl_1eiEo7CrMNuf87aUNbwYvyWPO5OYvBcJx4aRy_SFdW6UIpVoj8ol9LdoQCSPsxKj4SW8L8VBEe8whdJBgaDcfREUmAWlqIPKzfvLlfOG6dhhY4fMg1dlRLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما :
آماده‌ترین برای حمله به ایران اسرائیله.
اسرائیل نه خسته شده، نه پشیمانه
نه به آتش‌بس مقیده ، نه کم آورده</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5034" target="_blank">📅 07:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Khkf3M1O24e_PZd1zJ-VTI71FlKOR1VUi5YMF35K088OjmfKwMJN_MBO1JuqZ3eQe3R3cBXZMqxBLmv-RVaZLdu2x_5o17MXjfyAv6w26CQSGrQtNYeupJid0kVE-SVfeBOF6T-Jzgz9i3OSfv-vQKQoUg1Jg-BVbQPJ0GVgjfVKDYHgXSYXG3ybO8LGPRHFWWlhTMsPJNWHZvoX0fPiqB9koxHoqgjTfbc40Wog3p8yHU5bFGy-HF1V9FLueLIDLmGOFAlt94StZRC7GUF-PAhLRt2QnwztVfR8sQ7TCO06crk2jnfLA8Rmheo0Bs4QRbueTni7YsQSk8eJVER44g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5033" target="_blank">📅 01:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک منبع آگاه : ترامپ روز شنبه با اعضای ارشد تیم امنیت ملی خود دیدار کرد تا درباره مسیر پیشِ روی جنگ با ایران گفتگو کند.
‏این جلسه یک روز قبل از آن برگزار شد که ترامپ گفت جمهوری اسلامی «بهتر است سریع حرکت کند، وگرنه چیزی از آنها باقی نخواهد ماند».
‏به گفته این منبع، معاون رئیس‌جمهور، جی‌دی ونس، وزیر خارجه، مارکو روبیو، رئیس سیا، جان رتکلیف، و استیو ویتکاف، فرستاده ویژه، همگی در این نشست در باشگاه گلف ترامپ در ویرجینیا حضور داشتند.
‏این جلسه تنها ساعاتی پس از بازگشت ترامپ از سفر به چین، کشوری با روابط نزدیک با ایران، برگزار شد.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5032" target="_blank">📅 00:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سخنگوی وزارت دفاع عربستان:
۳ فروند پهپاد که از حریم هوایی عراق به سمت عربستان می‌رفتند، رهگیری و نابود شدند.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5031" target="_blank">📅 23:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c29FgNEEwStb010_tbunBZCOBGONLKaJF-VvprqQyLZCqTuLqN1O9ohRB8RIJkT04ZY0ZVwX7GLum9Ts3y4iNCy_xU1oDKtR_k4Q4IgNpbgc5TmD7pF19Ah3BOm8MeQTYebJoQ8CpDZzyqXZNvbRGoFDJ4aBAatEKYFQ2WOutKtQ19unQHI7tuCs_pupWxEE57ca2PQJrBqeNlUqFwC0OEeHX675653s9ou4cV_3XgbukOhy1GZnURxSvDnM2x-ABTcrn43woHpgb9UlQOfjC8JaOVv7Yvpvyv0-XvrbInBKgbv6deTVjdFiQsek0uNzqQPV4GO_8ooYXhHJuC94Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5030" target="_blank">📅 23:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m366r1NED6MTjSbQlAMVSW1T2Pur-lGcRouTY_PNtMHMIIPzW2fElEPzuh83BQiMeSpo-Fhcoe-zbBiD0FlrNKUM_I-srehp9A-O0BJB5q0XT_9l9or1p9x2gOQ4ZE4bsMKSX5DorNw2D2skPVkZufjavp18In9Q8DNQR1ci_LQMotahUDQcs6bLxlaGe68J0l0Z9PFEwIXKwy5JjUuORbA5NgTnrJn78eGIhRmu--wsvG_K2ifLkFXdbJNUGFFmGwtqUwGxWvY99Ag54760ctP71KKoe99HtBvuynIhiekIhwcF-riFe0zdxGh0PzKJ9hWMabv8FIkENYgvtvoSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادبیات سخنگوی کمیسیون امنیت ملی مجلس.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5029" target="_blank">📅 23:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5028" target="_blank">📅 23:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5027">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNqDGA3K8GNgEmBjG0klcHcNf37c9VL1EussA9oosZc2bEOXhj-d887Ba4hTOMvo0DRIvgubPFxmJf9BOdpqr2wtWLFC0zXWfVee3BxY-3DXem__pok1vIXX94zumI_n-3PHYKwwqF_kP4yOgDSv29bJ4IzeKdjlzoYjzwFz5T0nFXPbaRoP8H2afPe-gBTwNXoOlzUDGL6eJCaSM4zybdA7-a0OVF-IWc9WkYYSEwl63v5d8y5V14F061ANbOifmSkEZlOUJGbYzG3LfZQNBcNcf8tW6KSxh9cIMx8Imbeee8n5aewTujtVtEYqFDC7R4TMDWl647DsVUDI0B2kdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟
در پایان جنگ ۸ ساله
۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و
شما «جام زهر» نوشیدید!
خود صدام حسین در سال ۱۹۹۰ به خاطر حمله به کویت این سرزمین‌ها رو آزاد کرد! خودش به اراده خودش! نه به زور شما! شماها که جام زهر رو نوشیده بودید و تموم شده بود! اصلا خمینی بازگشت این سرزمین‌ها رو ندید!
چون یکسال قبلش مرده بود!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5027" target="_blank">📅 23:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344237687c.mp4?token=AQr0u5FLalszswhdPZ3NRq673U2gRM4WhuFMWfwSz0BqK7DnyPtChdU47B7HDjiitdBcvh-WjO7k-MJpbgQZk4Bjm6zJwiwVvJkqe0Zy26G97U6mobDUWPhNiSX3NLerWDxsOSP7YDaVR-y1z9_VwizkmdlLZ7KX2tSBAesQ_zGXIB3MNvKz0_Vs10FBbGU-1jsgoLJxswDEhMqHAKmqWeolfF2IR2DqRN1YPBdH60oOLQepqWoYvOO92GiEvP8B0whVevftfBgKS6CBbFFMMrcrHb1drqWSM23Je8__HT-u0gnb2GMUMutvTqDmXHKNJ_QAaysmZ8jUq5rdOli6pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344237687c.mp4?token=AQr0u5FLalszswhdPZ3NRq673U2gRM4WhuFMWfwSz0BqK7DnyPtChdU47B7HDjiitdBcvh-WjO7k-MJpbgQZk4Bjm6zJwiwVvJkqe0Zy26G97U6mobDUWPhNiSX3NLerWDxsOSP7YDaVR-y1z9_VwizkmdlLZ7KX2tSBAesQ_zGXIB3MNvKz0_Vs10FBbGU-1jsgoLJxswDEhMqHAKmqWeolfF2IR2DqRN1YPBdH60oOLQepqWoYvOO92GiEvP8B0whVevftfBgKS6CBbFFMMrcrHb1drqWSM23Je8__HT-u0gnb2GMUMutvTqDmXHKNJ_QAaysmZ8jUq5rdOli6pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۶۵۰۰ ایرانی رو به اتهام‌های ساختگی - که سنت همیشگی این نظامه - در سه ماه اخیر دستگیر کردن!
هر روز هم آشکار و در خفا اعدام میکنن.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5026" target="_blank">📅 22:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIgGQvxBrT4bkWVAlDS0Wk2vj0yFv-tnrAZ65LxKme1AWG4BYCKGVCqeWg_RhCOd8rFZaaBweU3DxUzhJU3iwpu0sOhtl1jP4QuvKbDnypn3Fxi88CFTWz2bSjB1lLZW4t-jChj569hxBd_ol-CZBhqEDPOxXQd0sdWVPm7tMzCyHEkkObxfjrHBXLDKC8GZln6GQ1i0U9EtQUgV7VNaGSB2FnN5sR20h8vUsvRbEWsEitm8kisVbZB-yPyuLe00azWuk8heKk9TNxKWHGhdkgDluuL675X53emj7-6Wj0ofSQqDH83bEwthdM-Cn9WlTSSmcZMpUc7hXXUa67Z16g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدصالح جوکار، رییس کمیسیون امور داخلی مجلس : «در این مدت پیشنهاداتی از سوی آمریکا مطرح شده اما جمهوری اسلامی همچنان بر همان بندهای اولیه تاکید دارد. شروط ده‌گانه خامنه‌ای خط قرمز هر مذاکره‌ای است.»
🔺
ده شرط جمهوری اسلامی که میگن خط قرمز هستن:</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5025" target="_blank">📅 22:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس: آمریکا یا باید شرایط جمهوری اسلامی را بپذیرد و تسلیم دیپلمات‌های ما شود یا تسلیم موشک‌های ما</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5024" target="_blank">📅 22:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏ترامپ به اکسیوس: من هنوز معتقدم که ایران خواهان توافق است و منتظر ارسال پیشنهاد به‌روز شده از سوی آنها هستم.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5023" target="_blank">📅 21:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
ترامپ روز سه‌شنبه جلسه‌ای در «اتاق وضعیت» با تیم ارشد امنیتی - نظامی خود برگزار کند تا گزینه‌های اقدام نظامی علیه جمهوری اسلامی را بررسی کند.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5022" target="_blank">📅 20:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5021">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iknlk0HR_KkjZeeHp6w-zuoog6tIXP2vdrzMgADUBAtaSmCklzNCw1ndR0RacUtQYc2Y4g-86A_3ujstDMuUycDR_IG-ysFQ4PlMVm8eavBnDerPxAcRU9WpB5IRi7XDn85byPbiTyRjJ5l8luC0fCauje_2J7SStqYoCKalq96nTXhxG3EPCTCoXmazhGrpVfk7h80gLXfGl7k5KoXd1XOAII0zG7aWeq5BntLwmhhjc-VuMu3W0BkilE1TowCEYOTTgRuA-q6iGUCez4qQxaxxG1X39YKi8Dv5tvBPo1caFWNFdO3mxywcic33MCbtz5PpkCIgIvXxDIRod1BdbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ :«برای ایران، ساعت در حال تیک‌تاک است و آن‌ها بهتر است خیلی سریع بجنبند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان بسیار حیاتی است!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5021" target="_blank">📅 20:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=QFY2z7_D6pr1CtVi4e53Lqyd8P9ykNzH_VZBv_6VjikS96FGG_c72djwQmjMltCBdRNqupMAVfytUUmyHwBjM6Cyt9mKI49Nl4OAn1vfRBTuapVtDzxhsFwuQMKjq6mmWfjeul20ijA4mx93Jg1xt3woj_dJbkVd4KWrOYMNwhAoMFxEjbfobu4CA3EVwNGLAqpzTfHiPlqYY_nVEK_gggw90h1z2bCcbxot1vo48K1ryjzcN0uBxuT75vnAEw5_S2eQe8X6JwcdPi4xnyEHH-BWpGDpY-YTy-GjDddgrW7ormiFQp3W1MFOHeK47eJsh0WHcA1Bpy9T3Ag5AO3cEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=QFY2z7_D6pr1CtVi4e53Lqyd8P9ykNzH_VZBv_6VjikS96FGG_c72djwQmjMltCBdRNqupMAVfytUUmyHwBjM6Cyt9mKI49Nl4OAn1vfRBTuapVtDzxhsFwuQMKjq6mmWfjeul20ijA4mx93Jg1xt3woj_dJbkVd4KWrOYMNwhAoMFxEjbfobu4CA3EVwNGLAqpzTfHiPlqYY_nVEK_gggw90h1z2bCcbxot1vo48K1ryjzcN0uBxuT75vnAEw5_S2eQe8X6JwcdPi4xnyEHH-BWpGDpY-YTy-GjDddgrW7ormiFQp3W1MFOHeK47eJsh0WHcA1Bpy9T3Ag5AO3cEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خطیب نماز جمعه دره سن‌گابریل - کالیفرنیا:
تغییرات بزرگی در آمریکا در حال رخ دادن است،
و اسلام و مسلمین نقش مهمی خواهد داشت
وقت دعوت به اسلام فرا رسیده.
مردم آمریکا «باید» به سمت ما بیایند!
باید بیایند!  باید، چرا؟  چون ما «راه حل »
را داریم! خدا راه حل‌ها را به ما داده!
قرآن و سنت داریم!  اینهاست  که
آمریکا را نجات خواهند داد.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5020" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5019" target="_blank">📅 19:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4siSybJcTWx3tdFdYCj0vVarF5vTBrPMr02yv8xWaNNfczeFmVf8HlK6_xfQkYLzdg3zim-z4tbdLsCi5iRLiryaAX06g0tcSmaH1by0kw1UfZnbYaGiwIh9WXv_NMp3z0s53mJc_DAoX3pZ9Av48C_GMWZv3qZrZplkVoM9B863nSMMUHWneVDlx1g9UYwMsnZ9cIeFhIY8JLPE8_HUCLIi2K6QzZwf00NbWnmA4qeD-NnQUd3qMbLQWYe6O9aBhfpMxnlZK-WkuSB0NxSRzNll8Itp5fiwZO42GbVQ4pQeVAPRFIauuC_KUWP4zkQlBUvLHOmEEAI7yhEyo6erg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5018" target="_blank">📅 15:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5017" target="_blank">📅 15:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5016">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !
‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا
‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا
‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای
‏۴️. عدم آزادسازی حتی ۲۵٪ از دارایی‌های بلوکه‌شده
‏۵️. توقف جنگ در همه جبهه‌ها [لبنان] فقط منوط به مذاکره است ‌‌دست یابی به توافق!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5016" target="_blank">📅 14:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5015">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b64429192.mp4?token=Gl1QYtgobdFlUomno5fpdY-qFSaLxQSV-x6rZe6UinWGR3faKn0nXHDPZ4u5h5prL2g7yxHfUo4_r7FRtTy45C3Rt1F9d5aoxsTW5PqokZnW05mhbpi_JI0WTxf6wAWwKDEYyp-6TKTewLF_JH_go1mvr4UDoj57Q4WeGg5OTdctwnPdm9xsyR9sHHmz-dFGc5erVW8HflkGMavL-6c2q9fPDQh9eN8UgnoXKutK7o3-pDr89k4bXwwxY33IV_XmII0Y1dtIku2ESdmSFYjekw9Y-hV3Ttzop4FIRqdcV7ENkP9x7DM-gObvhn_oZ4bVojumaFFnUftQjTZgIOdtHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b64429192.mp4?token=Gl1QYtgobdFlUomno5fpdY-qFSaLxQSV-x6rZe6UinWGR3faKn0nXHDPZ4u5h5prL2g7yxHfUo4_r7FRtTy45C3Rt1F9d5aoxsTW5PqokZnW05mhbpi_JI0WTxf6wAWwKDEYyp-6TKTewLF_JH_go1mvr4UDoj57Q4WeGg5OTdctwnPdm9xsyR9sHHmz-dFGc5erVW8HflkGMavL-6c2q9fPDQh9eN8UgnoXKutK7o3-pDr89k4bXwwxY33IV_XmII0Y1dtIku2ESdmSFYjekw9Y-hV3Ttzop4FIRqdcV7ENkP9x7DM-gObvhn_oZ4bVojumaFFnUftQjTZgIOdtHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشه عنبر خانم!
ولی روی این حرف‌هاتون بمونید
فردا که به خاطر ۴۰۰ کیلو اورانیوم
نیروگاه برق و پتروشیمی و پالایشگاه و… رو زد، نیایید بگیم ما مظلوم دو عالمیم و نیت اینها تجزیه خاک ایرانه و… !
اون وقت برو پوست پرتغال بخور و عنبر نسا دود کن .
تا می‌تونید از این ویدئوها پر کنید و یادآور بشید جنگی که بر ایران تحمیل کردید بر سر هوا و هوس‌های هسته‌ای تون بود و دشمنی‌تون با جهان!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5015" target="_blank">📅 10:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=cpDYPqRfsk0KzyV43o2SRetf-WH29hjSMLM8s7VdoMFf4Ku170QtcLbAYWjkvqtRYvt-8R1Rxb6c_tSgQ3eGsReX_FstIt9P0COA5eQVp0wkXn5XVzLzP5Ra1BtQw_P1dKEEC9aNeEBjsLlB3jnPulhxVKmERkgMO6XDje9OnynR7kkqLi1jvieLyi_qSctb6RbxzWwcTf1VRGZfWcxBn-CDAe19ZsBUEm2nlUFpDoUzOtvum42sphsZHb-WLTFVWYya1eL3PIetBl8EjCqu4FCUn5aBlplq72A1_R4V9QRxtSc7KCnmkwExtcYBiEiOJlsvderY4ZOxPtGYmpK6UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=cpDYPqRfsk0KzyV43o2SRetf-WH29hjSMLM8s7VdoMFf4Ku170QtcLbAYWjkvqtRYvt-8R1Rxb6c_tSgQ3eGsReX_FstIt9P0COA5eQVp0wkXn5XVzLzP5Ra1BtQw_P1dKEEC9aNeEBjsLlB3jnPulhxVKmERkgMO6XDje9OnynR7kkqLi1jvieLyi_qSctb6RbxzWwcTf1VRGZfWcxBn-CDAe19ZsBUEm2nlUFpDoUzOtvum42sphsZHb-WLTFVWYya1eL3PIetBl8EjCqu4FCUn5aBlplq72A1_R4V9QRxtSc7KCnmkwExtcYBiEiOJlsvderY4ZOxPtGYmpK6UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهزاد فراهانی، بازیگر (پدر گلشیفته فراهانی)
میگه ما … داشتیم و انقلاب کردیم ، شماها هم داشته باشید و انقلاب کنید!
چه افتخاری که جمهوری اسلامی رو برپا کردید!
چطور روتون میشه اینطور وقاحتتون رو نمایش بدید، در دفاع از رژیمی که فقط در سال گذشته میلادی، مسئول ۸۲٪ مجموع اعدام‌های جهان بود!
که ظرف دو شب ۴۰ هزار ایرانی رو قتل عام کرد!
ضحاک روزی ۲ جوان رو قربانی می‌کرد.
در یکسال میشه ۷۱۴ جوان!
در چهل سال میشه ۲۸.۵۶۰ جوان.
کاری که حاکمان شما در دو شب کردن فراتر از افسانه ضخاکه! این نوع از حکومت افتخار داره؟ تباه‌تر از این در تاریخ وجود داشته؟</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5014" target="_blank">📅 09:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=WXBCLpRYPs_bkBXSfQKatELqtoZ-wBJq_UBNbEzIQXyegenKvFgHO_Yt-m4A9LF1Wwu17S2igWZdHPueCe8n5esXqFz5U7RZYuw2vTrfLLEWWr1gl0xXNoz5rm12LH3XCpb9EqXUOOpssMJKoZrm2w8RMfRdBHRJXTplyVW2EmV0gzIxCyWHwUQsWeOGbD0urBa45MpvGKg_V_U59DLBOGvPq2raKgZnd4NRdSK7TUS-KHLfW4JHwrlSiCyeIgBPIdB0Tib1c5aRtM5SRXMMMS-C_uyVq8vWQEz-lR_TkpRmJ0xLo2G8APyFS6Yz9aPL4RV4XtiIOpdXyy3gN94pXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=WXBCLpRYPs_bkBXSfQKatELqtoZ-wBJq_UBNbEzIQXyegenKvFgHO_Yt-m4A9LF1Wwu17S2igWZdHPueCe8n5esXqFz5U7RZYuw2vTrfLLEWWr1gl0xXNoz5rm12LH3XCpb9EqXUOOpssMJKoZrm2w8RMfRdBHRJXTplyVW2EmV0gzIxCyWHwUQsWeOGbD0urBa45MpvGKg_V_U59DLBOGvPq2raKgZnd4NRdSK7TUS-KHLfW4JHwrlSiCyeIgBPIdB0Tib1c5aRtM5SRXMMMS-C_uyVq8vWQEz-lR_TkpRmJ0xLo2G8APyFS6Yz9aPL4RV4XtiIOpdXyy3gN94pXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش کار با اسلحه در مساجد</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5013" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b965352735.mp4?token=laHkfDimJTkPQPa1Zc-5YzMbUoS_q8JsKujvkJfzUctKb7FHMo0g2TDCF8jrTVvvEPKNXhTJwTpN6jJbUcWGIDf2TaZA_RJ29GWR7l3AktezLqewXC-UUBhoqCy11ak_X15PgzMIZ4KzotH4rDO6fcUHrpFIHaJrr9Q5uA-rF233AQoZwApqcy2UZau5vrDgziqo2C13E-i0uGIvew0cIk2kdNvwdmW36L3W0w820SYIFDF4FgrPuo4EXgHdGMzKhSBJoL9BQgnyS4_gyXxa-3RB-ysXWBz3UKv5znmPKcTpMee6BrkODMiBwEUxd6OaC_Fj6VOMCe4Tuyr8fJbt1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b965352735.mp4?token=laHkfDimJTkPQPa1Zc-5YzMbUoS_q8JsKujvkJfzUctKb7FHMo0g2TDCF8jrTVvvEPKNXhTJwTpN6jJbUcWGIDf2TaZA_RJ29GWR7l3AktezLqewXC-UUBhoqCy11ak_X15PgzMIZ4KzotH4rDO6fcUHrpFIHaJrr9Q5uA-rF233AQoZwApqcy2UZau5vrDgziqo2C13E-i0uGIvew0cIk2kdNvwdmW36L3W0w820SYIFDF4FgrPuo4EXgHdGMzKhSBJoL9BQgnyS4_gyXxa-3RB-ysXWBz3UKv5znmPKcTpMee6BrkODMiBwEUxd6OaC_Fj6VOMCe4Tuyr8fJbt1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ
که مشخصا اشاره به جنگ با جمهوری اسلامی داره</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5012" target="_blank">📅 21:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316762f84e.mp4?token=uVTrhgEqklqXMm18hD9gCZ8b5KuXW4P-1ij4ikqeGCLmSi6Xjwo8E6W90cvCJW-mYKhmSghWgYcMslf7AlKohow3b2nJDImNRA0RbFbcvDn6pK0t3GyXOjVhSjvlUFUupB-nQ8cmaye-hnxLEgEoanVBN776DeeJtLZh0RRb-H8-3q9vfNDgTBNugtESdw58cHEvuWQ2IClmGcgf6AoOWBYXBF9fn7fGfzleIyV9FGpPotSHsgdgzxSWqPUezNDfoeWB2RpWVltNhctq0Q7ATOFbyLHEIJO9t9PdS5KrtZKxBC_yU80KD3hhDE9hTrKHW6GH9ddpwgKnC82NUQmlIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316762f84e.mp4?token=uVTrhgEqklqXMm18hD9gCZ8b5KuXW4P-1ij4ikqeGCLmSi6Xjwo8E6W90cvCJW-mYKhmSghWgYcMslf7AlKohow3b2nJDImNRA0RbFbcvDn6pK0t3GyXOjVhSjvlUFUupB-nQ8cmaye-hnxLEgEoanVBN776DeeJtLZh0RRb-H8-3q9vfNDgTBNugtESdw58cHEvuWQ2IClmGcgf6AoOWBYXBF9fn7fGfzleIyV9FGpPotSHsgdgzxSWqPUezNDfoeWB2RpWVltNhctq0Q7ATOFbyLHEIJO9t9PdS5KrtZKxBC_yU80KD3hhDE9hTrKHW6GH9ddpwgKnC82NUQmlIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی  تفنگ به دست در تلوزیون ظاهر شدن خوبه یادآوری کنیم از سلف اینها خانم «هاله مصراتی» که ۱۴ سال پیش تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5011" target="_blank">📅 19:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5009">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BTUPHM9s9ta1coHqaiTvMFjnsGJZcUccLUWq-rlIbhbmTqurI41Y12gDsFB487IKCFCPoHapURMyNletL-8oyZ-LYgLG5vwNyMzWGJp9ABRI7pDd7AkThyMq8GkkEBhrY4GfchXyc4L6i0VAXIg2-8Jh7jWSfXTs55CJImJ6Rh8y-l7UP1Y2cRlR5KZbqcuPQOzv2a1a-pELZr0QtNdYbS6jzcTNcm4pV0dOl_n-dwEp3cGvzGAbvuDlISCvgj2LbJZhtaul-K3PX1knIE13cCsHM459MWiHdqVotINDenjcp3JAWeTHpRnwVr1wWKCzhRj93WBCDjUZnE5l4XcVLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YdZvB0kdH1ANtOOAguJOfbd7WdUPVRnFgyXqzkYvpTijNk0TI2tgI9hVfx3TLa5O7rLBxHC0ERpBkrm_71MP9N6vkwtdEMh7_XLLuagMQsKEvBFbyYxDvItdwOO7s8yXLObLzSU1ohr6VFBGrsvyG6-BLB--0SJAGDpHK1DXEAyIwoUrle1_BxQe53qQjPfllFkglt0teeKOhd6cgG58f_qIZn0Kj2kX9bnzG3kQUKH29Dj_xUOhSvSbN6oSyBzbvi_0P2EJhwP9WFIS75w_3D-d6MVN1Gym5T5ig_5DV_U4dEigG1tJ7bY0fow392F8MiDktVAW28MlmPaiJtc9bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی
تفنگ به دست در تلوزیون ظاهر شدن
خوبه یادآوری کنیم از سلف اینها
خانم «هاله مصراتی» که ۱۴ سال پیش
تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5009" target="_blank">📅 19:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دوستان بزرگوار، این صفحه به‌صورت مستقل اداره میشه و من تقریبا همه زمانم رو صرف انتشار و پیگیری اخبار میکنم.
اگر این محتوا برای شما ارزشمند است و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5008" target="_blank">📅 19:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">در ابتدای این فایل صوتی که خبرگزاری فارس منتشر کرده، به نقل از
حداد عادل (پدر زن مجتبی خامنه‌ای)
نقل شده که فرزندان مجتبی خامنه‌ای در این ۷۷ روزه پدرشون رو ندیدن!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5007" target="_blank">📅 18:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gxpLIPRa1F9F-MxTJr64GNDZugXfDkJHfE5fvuEvm-5fesKYmSPgupebUUzKR_LtCw-97tkUN8H3jWhJ-5DQdbWHsvBLT9074PoJ3zO6D_g9TeBCEtH_0K9IvjUAp-TeaOwFW0GIqzKvp6o_BI5ggVWmGBhPIdr9aQspCdESv_ThZ4yAmyp6rURM9I1fZSqnZrwWZIyFbyBxeOqjOd_DZy23bx4cQJ7fAjcz1O5J5TPIkhaMDZQy2oInoEYTvdkpXmRm4dbijlCweBuGo-5pcYn6nw5BonuOeeBjKY3btRfWRoqVjij1KMQNIDyc9Sv2nIADrSMtJNIoKzD2gBU8gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h4ubfWYMwvILkLqvHXSV8raBJr5Cnf8q0OBuN-xyZZ1hY45EvCjQgG_X_dXUKUETQiqvaQw4BZyvdVlXKORM7NasFXn_BvLAszH_8-9AEK5jsxu7yWI-Q8JxD5OFdsc8PNZJJX-hfGravz1LhiIHAkkpg8UpQlmFS3DXwhh5xCKxAMZItY8Cyqv6VfBkzF79yn2vnTpB88yOnGMlTENPMFeLedt5-tzPFiOMiX3lc7Zc_fGx_JDGX2DtPEZ2GQ_7xZDPcMVkc1i7yA_2yiBmADt1EjcRsEhzM6bwl5xVXaTQ-BAV9cKfLR0NyXLprkI_BzwMIIaPTLExRnT60KBtvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5005" target="_blank">📅 18:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=tEfjlQHL_ZPwLE5njidQ7h2vLk-ml3hv_LfTocAeS1qvz2GqXDj_e_ynoIDljvzkHDr9JMHnNOym3SECvA7-0wi2XAfY3jK3F_CcPq-NrD9Gz0PmfJ_zk_jWFd9VrvvPijLFSHG3Kbm27C-PsBVLGRgcNcDvdB0SchSKG2n0u-JYAWPcg7U-ou2mE2_LarsttzJl5ItZztqFtJhJZXMI9rXasWG6-sfpKqYZx3ZOfwgDZGYCTUnd41t-kUEi_4V94LDUIA_ocg3xwHLW49JyEIp772lRgLLxTvnJQHT8STGzlFTbKOjDKeiXrt8C8wKclMBanqMwwmsmJznRrlYQcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=tEfjlQHL_ZPwLE5njidQ7h2vLk-ml3hv_LfTocAeS1qvz2GqXDj_e_ynoIDljvzkHDr9JMHnNOym3SECvA7-0wi2XAfY3jK3F_CcPq-NrD9Gz0PmfJ_zk_jWFd9VrvvPijLFSHG3Kbm27C-PsBVLGRgcNcDvdB0SchSKG2n0u-JYAWPcg7U-ou2mE2_LarsttzJl5ItZztqFtJhJZXMI9rXasWG6-sfpKqYZx3ZOfwgDZGYCTUnd41t-kUEi_4V94LDUIA_ocg3xwHLW49JyEIp772lRgLLxTvnJQHT8STGzlFTbKOjDKeiXrt8C8wKclMBanqMwwmsmJznRrlYQcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟
چرا خانواده ، چرا فرماندهان؟
چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته
لذا شرایط عادی در بیت بوده»
صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5004" target="_blank">📅 18:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5003">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پیام‌رسان‌های حکومتی «بله» و «روبیکا» دچار اخلال شدند و بعضا از دسترس خارج شدند.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5003" target="_blank">📅 18:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=nPU1lJ60__0nn3OvlKiRE3gmrSG6DqSTyCqOMtmP2pvBWwM66BleE1GLYtbuSrpgwab85g0b8oQcrEdLW3J4jIiLpMLs6YBK2HUxBc8vcXqZrWvJdSMVJIdfeqWoXF1rX5yCtmixVU4Csjo4uzmAtdRVctLpuiPoMA5tI8SE6yAEOBN6xxYseleK0hd79AE7vaUNJpVypJ9O2PtgmTj-1ha2WPHQYTCLfWDnf5wu0ZINDyJOe-32RiYkAMMayd6BeD7CQRJeNpljPyAQPnRUl_zzRqJs2x73wHlMYKZixWhZ5y9k8QmgW5WWH88ZOusyXl6CsRXxq04qe7FDx5t22w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=nPU1lJ60__0nn3OvlKiRE3gmrSG6DqSTyCqOMtmP2pvBWwM66BleE1GLYtbuSrpgwab85g0b8oQcrEdLW3J4jIiLpMLs6YBK2HUxBc8vcXqZrWvJdSMVJIdfeqWoXF1rX5yCtmixVU4Csjo4uzmAtdRVctLpuiPoMA5tI8SE6yAEOBN6xxYseleK0hd79AE7vaUNJpVypJ9O2PtgmTj-1ha2WPHQYTCLfWDnf5wu0ZINDyJOe-32RiYkAMMayd6BeD7CQRJeNpljPyAQPnRUl_zzRqJs2x73wHlMYKZixWhZ5y9k8QmgW5WWH88ZOusyXl6CsRXxq04qe7FDx5t22w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه از متولدین ۱۳۵۵ تا ۱۳۸۷ خواسته تا خودشون رو معرفی کنن !</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5002" target="_blank">📅 18:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=bIFcnHE1NZYS7cBZ9wc6j3dScLL9GTh-8K61XRRh06Unc3KAlSTTf9NaKe5Z46qeVZebDLjx1A3sMAAA1pF_9W_1Lwps3gCKwiKHpAOu2lKzMuLS5GXIKXU2vINGWdbhqM4Jb93IBkPoEAuvCiVaFoAPPNn_Hos6Q3nW-65nHNCmvklxZudqLN-bZbmXjW0qv60gTxJaR3Yy5RGAzpVAmbYrrdxNZyqLiM_UwZa5W78yTrnieQg6vF3pyg9LI7LSlTua5d4o6vG6hQ8HtqlyI-u-v-nEVaclad_3ngoxYVJWEJX3Wg6nVA_Vbd4k4jFk_421nRkDQN7bN25elvqgaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=bIFcnHE1NZYS7cBZ9wc6j3dScLL9GTh-8K61XRRh06Unc3KAlSTTf9NaKe5Z46qeVZebDLjx1A3sMAAA1pF_9W_1Lwps3gCKwiKHpAOu2lKzMuLS5GXIKXU2vINGWdbhqM4Jb93IBkPoEAuvCiVaFoAPPNn_Hos6Q3nW-65nHNCmvklxZudqLN-bZbmXjW0qv60gTxJaR3Yy5RGAzpVAmbYrrdxNZyqLiM_UwZa5W78yTrnieQg6vF3pyg9LI7LSlTua5d4o6vG6hQ8HtqlyI-u-v-nEVaclad_3ngoxYVJWEJX3Wg6nVA_Vbd4k4jFk_421nRkDQN7bN25elvqgaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.
و نتونستن چیزی پیدا کنیم …..
این همون حادثه‌ای است که میگن
مجتبی فقط کمی زخمی شده
این همون حادثه‌ای که توی
صدا و سیما گفتن همسر خامنه‌ای (مادر مجتبی) هم کشته شده
، بعد از ۱۰ روز  گفتن نه! زنده است!
یعنی وقتی داستان زنده موندن مجتبی رو پررنگ کردن، داستان مادرش رو هم تغییر دادن!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5001" target="_blank">📅 15:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5000">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVTJyFHZcT_OiapiL-Xk7xktJ27hsbGz9sQB29djV9ct6i97bONOHZ7DmXkLBWEDSCGFACj8cND1MyFv90XC6t1sjtaXt8UfHe57vfAWxWdMz7o0Fnp8Fdg94Sv0bGuqjd7H8Ehidw5b3xgPCeGiUd9ZP-T9lx3Ot2d-Cf2g-9Le4uBO7iDF4qeac1njO5VzSxMKm_itDWm9gMCNZhpvsMAbAW882OD0syfEUdZfSQfEHTfsoauIGs4NDqX8C0yOeI5W6PCexJm_0hWYv0O0UZs7nlFc7uHAg2CGS4sv9lVWdFqNhTPhjMpnmDKbe1PiUVu0MR6hKGZpxwCHRbKlkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5000" target="_blank">📅 15:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=c2wonRYwQooCchxVfOZ7dPuLVjJAiuf0p7pwuRATWMCuIyzSO_y7PJoiTTv3WO_UY71MV3GQE75tUXSNDtW3m2HHJ-z543QB4tcjlFcobdvmIaV0Qk0ssd1KNAc_HYOH9VMSSIw7xDcjGCxfEE9KLuS0iBtak28BYf_yY6-63j-ovXJS6M5OpuzAphG55VnEd7l5tjRyjnvlMIURAra8a5b9myFqIm7_RHP_9XIYwKq2fVN4UTiUPNCgXkswIyv9-O3FmQq22yBOaaVPJhC-8jRyLrV8m6kcDcAQFJV48JGiyrSlI8S_ckjSWIjYvs18bAUvuzrgAOMfRYWqJ8R6zqrMiUtXYNSoC2TQZjbaxt3EW_GjkBzvr8X3NCUYGSaTiH2et3YwprbArrMueDsh4HPONHF9Krn3Vkz0eAwen-WZHfgv0orlNsqy7fiqWF0Wv6sa_CjPVCA8iV_L-aKYppPHX8_65BhHaiJronmscKF4TT0g_cw_C3PbiKi2exjaIXSBacYkaMNxMBh38X4Onvl9O52eVxs4sLLD4Rk9Ifx4EJ_uo9rzSNWeJmWYJraGUltvE6K2biaxcJRhTjaJSOdQ8MLQno4kvvVyt4rut5DC7KxFxSLvxPrCHI0jsj1IvaDN40MD_vz5xWMVBKEiROzjC9Dkhr6GrQrJlMSwHQU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=c2wonRYwQooCchxVfOZ7dPuLVjJAiuf0p7pwuRATWMCuIyzSO_y7PJoiTTv3WO_UY71MV3GQE75tUXSNDtW3m2HHJ-z543QB4tcjlFcobdvmIaV0Qk0ssd1KNAc_HYOH9VMSSIw7xDcjGCxfEE9KLuS0iBtak28BYf_yY6-63j-ovXJS6M5OpuzAphG55VnEd7l5tjRyjnvlMIURAra8a5b9myFqIm7_RHP_9XIYwKq2fVN4UTiUPNCgXkswIyv9-O3FmQq22yBOaaVPJhC-8jRyLrV8m6kcDcAQFJV48JGiyrSlI8S_ckjSWIjYvs18bAUvuzrgAOMfRYWqJ8R6zqrMiUtXYNSoC2TQZjbaxt3EW_GjkBzvr8X3NCUYGSaTiH2et3YwprbArrMueDsh4HPONHF9Krn3Vkz0eAwen-WZHfgv0orlNsqy7fiqWF0Wv6sa_CjPVCA8iV_L-aKYppPHX8_65BhHaiJronmscKF4TT0g_cw_C3PbiKi2exjaIXSBacYkaMNxMBh38X4Onvl9O52eVxs4sLLD4Rk9Ifx4EJ_uo9rzSNWeJmWYJraGUltvE6K2biaxcJRhTjaJSOdQ8MLQno4kvvVyt4rut5DC7KxFxSLvxPrCHI0jsj1IvaDN40MD_vz5xWMVBKEiROzjC9Dkhr6GrQrJlMSwHQU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«راس امورشون ۸۰ روزه تعطیله» :)</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/4999" target="_blank">📅 15:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nit4ZX1PtQY90VcbkFwckYgjA0hyiKCVDUubuzLKvpIPi8MSUBhQIQYwdwYobOLkRbwtycysEAP4l-Ou-AmFMo51lyXLbC3SaYGt0gmWGBG9p8J94lzeoY9xpvT-LU0W5XZRaa_5r9pgaYReV8-FEjcJNNS70FyGW6eEhbI2IioJjFNV7_-ZwS2AVVFZufe7iUxzIU4rcQKF4FQV0TMd8dBu-PR6spkICSwfK_CNQ_hOK59lNyTo5_q0b1dWzu57lhuTOGc2-drUxrwmCvtTBzvEUmWXRGAOvK8o9aIAT3cwjroKKb1zEwozhLBwNekrs9GCvwYkdVZ5Z-XtyLXy5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/4998" target="_blank">📅 15:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4af299654a.mp4?token=pRE4N_ybpk0UEnRF8GZdnp8wlPkM0ZcDIQCSovKy_FKw4o75YK8FUDJVMYzuGVycry6fqjGEggJ5JPA0iQZi76NpY-pQIVugfe_EG1uV-eRWg89iJ2fC1nHycvsNZ90ODj7LrWpD2hY8Qr-FvlQN0Xmnb79lsX4VNS53kS4iS_PI5ja6sll8ey1l9dax3vEsLM8qRfrQ-O-sfs2EI8JHCtb--c32kau_4BpQkm6dQ5yxy5qcRnQfmK4MpON4ZlIA1U1NXyfMO43w4lGZf_bMU3inRPZct1w5YmPGHXa47Pu5D3mdEmW7Ya1H93xjWIDKHnDaY-OjYN7cBVZERzLWVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4af299654a.mp4?token=pRE4N_ybpk0UEnRF8GZdnp8wlPkM0ZcDIQCSovKy_FKw4o75YK8FUDJVMYzuGVycry6fqjGEggJ5JPA0iQZi76NpY-pQIVugfe_EG1uV-eRWg89iJ2fC1nHycvsNZ90ODj7LrWpD2hY8Qr-FvlQN0Xmnb79lsX4VNS53kS4iS_PI5ja6sll8ey1l9dax3vEsLM8qRfrQ-O-sfs2EI8JHCtb--c32kau_4BpQkm6dQ5yxy5qcRnQfmK4MpON4ZlIA1U1NXyfMO43w4lGZf_bMU3inRPZct1w5YmPGHXa47Pu5D3mdEmW7Ya1H93xjWIDKHnDaY-OjYN7cBVZERzLWVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری تلویزیون جمهوری اسلامی:
- بگذار پرچم امارات رو نشانه بگیرم
- احسنت</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/4997" target="_blank">📅 15:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOEY2mIHALeuACSxO1-d8sdvYx7jPX6sg-XP38v7-CdJ0OlcLpCJE4trKz3QlCEgYHM0fl8qAkUWXlNwFexAuuS9B-Fcx0rl3UsZIAGIxIVODfwy-6FapUh_GSGKWb0ycfmss6wUqnqlM3JR60hMqWzxSwRQcBZKKhOyPxdH-cKAbrd_5YMbQjlWoPqaQM0CFeTRvjYn3UmAEIPsEXI25Dr2jAn9yEYdb5KMc2y8BZTnIq_UGdBvftp7UwPSfwlRXku3iWMwPM1ijGJIcZwcco1Wa7YSj2kR9U9j-dSVef4PKbxYI6vHSG9zEbQeiBi2-SApZJrvgMfgE2Zflqlc1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده کل نیروهای قسام در غزه دیشب به دست اسرائیل کشته شد.
قسام در واقع نام نیروهای نظامی حکومت حماسه.
مثل تفاوت نام حکومت «جمهوری اسلامی» و نیروهای نظامی اش (سپاه پاسداران)
البته ج‌ا ، متفاوت از همه کشورهای جهان، دو نیروی نظامی داره: سپاه و ارتش.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/4996" target="_blank">📅 14:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4995">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cscgbAq2dM9tQyqx0IfDPYDjtH0SymMSjfheVLMgmb_pvioRAIqda-kt3nxDoBf2sIquQ7QpG1_BYHO2THPuj9eDBh86dWvsogZ3d_9JCjp3YPco55MIDfqjWnO1ishZQ-S3oMcsaP8bALkLy3RXvouHOky8g0O8ZUehx2rk4jcrpq0Sd-mUNNvvpzCEnE-64xMZPnflGzPi-u_Sc3F2-SEyizEk5gy9Y9BpUK0Eg5qdKvJiepbTPXEJb254TDDjBo_LEOz8DpJ1jgxRRDqBl1NgcBA2Wb8Zc_XwWEW-s9SAsOSiFQuvmFlYr7Xx9c71237G8lBtqBCByaKNPGMEcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم جنگ بعدی‌شون در ۷ اکتبر که توی تهران و قم و مشهد هم شیرینی دادن و اینهم از ۶۰٪ خاک غزه که از دست دادن!   دیگه توی آمریکا هرگز دولتی سر کار نخواهد اومد که بره به اسرائیل فشار بیاره بیا و به گروه تروریستی اسلامگرای حماس خاک بده کشور اسلامی شعبه جمهوری…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/4995" target="_blank">📅 12:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toLAD5wDvjq5IMk1mWLZSaJ-CpKW9XkaJfo_wBSDE8_9owFmDMG1LJlfv412RVJwbM1GC07kIB3KawFGLCmV60lbSCJfHCdT4zGipRoPsHyL33nqBB7f4foqQI-Bo6lCNBbYIedY8vr0YGS08EPZzbwdSt0gC9djKssW8e0Uuynwcjx-2-BueVagRK-KPdNCWFjET6xiiB8MbICAKAP9MzGq26G40aYl7F5uLRUrWzYBnoCWVW3lT5Qicf489t3ODOs-Qf-TBXzzc_1ODmjAPVZMr12rCDPeExHL9F1Z9dl99ht3kworkfniXgjihbMLEmO4h-0-wbZSX-JShWTR1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا سال ۲۰۰۰ از توان خودش استفاده کرد، به دولت اسرائیل فشار آورد، به شما کمک کرد گفت ۹۶٪ خاک اشغال شده شما رو از اشغال اسرائیل خارج میکنم (در کرانه غربی)  غزه رو هم که خود اسرائیل رها کرده!  بیایید و کشورتون رو ایجاد کنید.   عرفات گفت نه! ۱۰۰٪ ! کرانه باختری!…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/4994" target="_blank">📅 12:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emWzscxOiHnjY_GH6JRZmncxxaYgtqrMRh_jo97-5C4Sk0z9ormwEFvQAniqDc633k_Ri7rEB1nQmhjGrHklO9DaPdzcm2UuGzWQZBXaP_sgUg6IREEh0U7UzYx7kuTy-DnLlXQgneIYuW88D6zK7K83wD_8deThq_PaKOmM7bIeIOymSbivA1TwsyXyHsbdeSCXHYXv06MJamSu2QrdpvcGULJP9PAqooAIHeIFAbdUdsgxA3Nj-hjFJy58ZKfeQehZo37Te1WkVLBq3C3OO3eVRe40HGAoMdI9xwnreuNON49JsBiRgMIA8Jy6CrHnozcXkJLTJwAdr8RCVUsXCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عرض ۶ روز ، مساحت اسرائیل ۳ برابر شد و غزه و کرانه باختری اشغال شدند!  ولی اشغال نبودن!  برای ۲۰ سال هیچ وقت دست اسرائیل نبودن!  دست مصر و اردن بودن!  دست عربها بودن!  گفتن بیشتر میخوایم! نه بیشتر بلکه «همه» رو میخوایم! باختید! شکست خوردید!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/4993" target="_blank">📅 11:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YL5oDt3YjvD-d__EbE8-bDaemYHxWtcd2Zz1dyB9lBt1bw3-9tp6RA8EvZgyOiyy9h8XB4dDaFDMeP7eSm4r3AEOmUXoGiuVl2vbfCvBxsLMTcfRkmKzJd6nKi-VxPQDJofNCW8g2B9bJl5vVXZIAONqLsLznXdrLGm-INab8xbJC-6Le5qQH8TUeMeq3Ngd6O_5NYl4-TEO2sy0Bm9C57USQqj4OFKn8jkFBhFosvOW0-z0-7n_xzVmxdsdjlrBfVDUNcGePbxrvXNHSb0rfa9sLKRF8Pigr0MaZzp7zKfB2ljk9RURhf1G3sKwFGzHqYPJ2tGbTJCHZyP121ZB5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد برای ۲۰ سال!! از ۱۹۴۷ تا ۱۹۶۷ نقشه فلسطین و اسرائیل این بود! تمام این‌سرزمین ها دست مصر (غزه) و اردن (کرانه باختری) بود.  توی این ۲۰ سال می‌تونستن کشور فلسطینی رو تاسیس کنن! اما این کار رو نکردن!  چون «همه سرزمین‌ها» رو میخواستن!  اینکه دوباره حمله کردن…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/4992" target="_blank">📅 11:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpVHFH-pHeSvt1iApHEfmHtuRlsLcEIkFnGB3eJWVu4dM6bzOVSbuR6ucmJynuvC8nkgE0qvWgEIcjyPIffRrvWxfpSm8wf-6mvH95Osga_ZToQytKqoLbTVHZ1pVtvPwcNZmxn1smuYSqvsh0qjvMNqjh5POfLNscW5sCQ8dqxIbKXYtEOGB30cOcByrT7ld6ICWPBK_B-BqEpFW5XrY7bMWpy7wehbMZLGnMxaWvOVwtoDqEhBTovJdYzWWgPEsQfPxUloS5SbTtXv-BhmIuFT-JtuwyL1CYiZyKZtfGRH20iCEsBrFx-sLbG3DbDu4B4ZohrFf5iDL7U4ykmL7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی سازمان ملل، طرح تقسیم فلسطین رو ارائه کرد (فلسطین یک واژه و نام یونانی است برای این سرزمین و هیچ ربطی به عرب بودن و مسلمان بودن نداره!)  اسرائیل هیچ سهمی از «بیت‌المقدس / اورشلیم» نداشت!  در سرزمین‌هایی که اختصاص یافته بود به اسرائیل حدود نیمی از جمعیتش…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/4991" target="_blank">📅 11:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bohlJT-hvUEfw9DAvT6_SQZP4tELG9SFjZgylMWX-pnTx5wCjboIFVrvLh1c6yG8eK53CFpAczBs7Bu-vmmXu5zI9jsMORR4djIMIcs4_oJcGLdMCJITOwfVXCSXgiSqLlmnTxzOgRw5FV6T-HfHr0JEGnVzbGReW9YRvDU8GPpaxk-WbYOO8E2e7a9CRJ9Vh5IXGQIdf3f3HMgLah9n4ebEsaHkkd1pk7_DrpLcSBnuv-StOZb2bJFMXTfmznFb8DPYBREjnrdU1QrztC8Fmexecvf4cGbZHgFjDEE9SGVKsRzxqXuPg1i8-ZkSqrdYYpwxqjUKzEqCiBZJJQsrYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیل کلینتون :  به فلسطینی‌ها پیشنهاد داده شد که ۹۶ درصد از خاک کرانه باختری [به اضافه نوار غزه] مال اونها باشه تا بتونن کشور خودشون رو برپا کنن و به جای اون ۴٪ از خاک اسرائیل بهشون داده بشه.  اما قبول نکردند و طرح رو رد کردند.  حماس به دنبال ایجاد یک کشور…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/4990" target="_blank">📅 11:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=foOEuQuZA6OfZuvnH81HlMhcecVeTvM3vG17GGZjA5P1EfWzw6B3BIghl8RIGv6PUNgIhoq5gGB2T0GTCnrx8NIRjnqLLA6EBGsOnuoPgv2Y6wr9acOkUWpMGvx1eld0F9NEfgk6Ks0sraDBC3A-8_bstIeGUAPPXje9KlCtNvlnzhTVgB76AtjsvP_aZrnoAAIbeM-Twa1YoqNV53jWvXGEGG8uxjTJ1jWj9Y62FO1TG2gdf6SfOIeYGWYz1Pui_gCG48QcJ8L1Q3_9B4X7P73YjEbX2eoLutyG1BSVhEoDYVYrjnHRf8ZmPCOggD4m9fPPDxfVDTnvSx_Vxmru6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=foOEuQuZA6OfZuvnH81HlMhcecVeTvM3vG17GGZjA5P1EfWzw6B3BIghl8RIGv6PUNgIhoq5gGB2T0GTCnrx8NIRjnqLLA6EBGsOnuoPgv2Y6wr9acOkUWpMGvx1eld0F9NEfgk6Ks0sraDBC3A-8_bstIeGUAPPXje9KlCtNvlnzhTVgB76AtjsvP_aZrnoAAIbeM-Twa1YoqNV53jWvXGEGG8uxjTJ1jWj9Y62FO1TG2gdf6SfOIeYGWYz1Pui_gCG48QcJ8L1Q3_9B4X7P73YjEbX2eoLutyG1BSVhEoDYVYrjnHRf8ZmPCOggD4m9fPPDxfVDTnvSx_Vxmru6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیل کلینتون :
به فلسطینی‌ها پیشنهاد داده شد که ۹۶ درصد از خاک کرانه باختری [به اضافه نوار غزه] مال اونها باشه تا بتونن کشور خودشون رو برپا کنن و به جای اون ۴٪ از خاک اسرائیل بهشون داده بشه.
اما قبول نکردند و طرح رو رد کردند.
حماس به دنبال ایجاد یک کشور و یک میهن برای فلسطینی‌ها‌ نیست. فقط به دنبال کشتار اسرائیلی‌هاست.
🔺
بعد از عملیات ۷ اکتبر ۲۰۲۳ ، اسرائیل ۶۰٪ از خاک غزه را نیز تحت کنترل خود درآورد.
در تاریخ ۷۰_۸۰ ساله اخیر، هر بار جنگی راه انداختن تا با جنگ، سرزمین بیشتری بگیرند، بیشتر باختند.
🔺
امروزه در دنیا، نه آمریکا و نه کشورهای عرب، هیچ کس هیچ فشاری به اسرائیل نمیاره و دیگه سرزمینی به فلسطینی‌ها تعارف نمیزنن! هر بار بهشون تعارف زدن گفتن کمه، جنگ کردن، بیشتر واگذار کردن!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/4989" target="_blank">📅 11:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4988">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQ6AdmcQmv0XlHXLFJxiIpsDhzeRNzdLBjsFdr7Lu4iCHAFmLyrxZcaM0MLGsOlOEMPEsurHMKtgp4wCEp2Ct1JrE0YnDt51r3jVZemx--uxAAQhB3_1SXIGz72dPkNYzZPgR-NiPQAtAqPt2fRTvPiM5aNcneIUk7eARZu0V2P7PomUZrQH0kK_WlVbz6Xgv6MACGWVrp-SvW0BD9IPMvUWLKER5lRcF5-eTaWqltC97mUhcxhtoFRo2vqx_oopdbRev2RITGXI3Bd7sioPwr3OgyV4qO1PTXBrxVzcUHKfX3gJwXvEZnuFEvHmkndE8NaFZyD3BvjLiLbbjdfJYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/4988" target="_blank">📅 11:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfjSFL-1rtuzafesnIgmrJDhzElz74sDNEu94XrrIoeumI49xvIkyXsWfblOuyBTBpbuTnG1_vjAHTuRJkdk63Ub9bxpFgevISoI059nYwbY5AjvR3Bjc-tEC_xVkw_3OeW6ZEAoSc0X4CvDAyY3WjndjoE33oHxkZxbfl-Gakg_Hd1GKnfEpe9y33W00LY-RtD65mW8GUdne2eg71jlXgAc7CaobByLugwXL3K3zQIZtW7rXFFy6VZZjWE_TEtDtQaIS7iEhrZW-ZrswqcrayjHl5Iwp8uNheHbSOtUQjAXX7wFTo63klOTtDibGq3_XnW0V424GXcFMU9FHBE4GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4987" target="_blank">📅 10:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4986">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=CLZvxd6QB2rsX1Jb5ScR12MuLnJ0J5cav6k2mKqisczFe3JSo2V4l2cYe-hSUcpoTYqGk27NIw2M14IOn2ouoMTS5uNjdE1WLrmTrwYRrTucWpesdgNz6OXcNexDlswxztQvlhXf7_U0y9FWINq9xut-HXK7D2-H26grP-k8SSqcvrRm5N6cCLti67kcpHVaKksa7wfVzRiL7NhaQL_9VOev7QrMkwQ7017NYmtY41RF8zWwdusgwbJGkjMYVV5IKWjM-VqTjJQEUK7sIvZHORCqn04pi3GCsaMcHcJBwQST_ENBd0v_Wsr-JiKvJJuMjUelREc-KU3hchjGNOHK_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=CLZvxd6QB2rsX1Jb5ScR12MuLnJ0J5cav6k2mKqisczFe3JSo2V4l2cYe-hSUcpoTYqGk27NIw2M14IOn2ouoMTS5uNjdE1WLrmTrwYRrTucWpesdgNz6OXcNexDlswxztQvlhXf7_U0y9FWINq9xut-HXK7D2-H26grP-k8SSqcvrRm5N6cCLti67kcpHVaKksa7wfVzRiL7NhaQL_9VOev7QrMkwQ7017NYmtY41RF8zWwdusgwbJGkjMYVV5IKWjM-VqTjJQEUK7sIvZHORCqn04pi3GCsaMcHcJBwQST_ENBd0v_Wsr-JiKvJJuMjUelREc-KU3hchjGNOHK_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین یکتا، همون چهره‌ای است که قبل از شروع کشتار ۱۸ دیماه اومد تلویزیون و گفت خون هر کس ریخته بشه پای خودشه و بعدا گلایه نکنید!…
این همونیه که اومد حامیان رژیم رو دعوت کرد که هر شب برید توی خیابون‌ها
حالا هم در کنار تیم ملی فوتبال، در یک اجتماعی اینگونه رسوا، داره مجری‌گری میکنه و میدان ‌داری.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/4986" target="_blank">📅 09:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4985">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمملکته</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=J4mu04LMffSnjicDG9UTx7dWGzp3YY5HRFHRb1gm_MVGcA1q7v1VsYnaolDm5ckz4Ys9px3aED4RjZfRLLk8Et2iP1kiP60L8LxYtc4lhO1hUDiQaZzCmv4VLyIfrGM3btuz4hT_cOws_AN3orwowg4PgxylYj063nmmENPtcm9njT0M0anK_J1RnD3TXb-3mDJe_nOIh7uzixN9f3d3xxR0pDJUmkDf7Y5YkzuOwCpUm6wy1vbVpnznBJBV7P2PyE3ueOIPGjOgVUIg3E5HBuyH2WiKfyTzv1MuLVEXSyhyPurt85ExQgaLlqZifCJZkLd8l1YOtCzqWXn1-712BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=J4mu04LMffSnjicDG9UTx7dWGzp3YY5HRFHRb1gm_MVGcA1q7v1VsYnaolDm5ckz4Ys9px3aED4RjZfRLLk8Et2iP1kiP60L8LxYtc4lhO1hUDiQaZzCmv4VLyIfrGM3btuz4hT_cOws_AN3orwowg4PgxylYj063nmmENPtcm9njT0M0anK_J1RnD3TXb-3mDJe_nOIh7uzixN9f3d3xxR0pDJUmkDf7Y5YkzuOwCpUm6wy1vbVpnznBJBV7P2PyE3ueOIPGjOgVUIg3E5HBuyH2WiKfyTzv1MuLVEXSyhyPurt85ExQgaLlqZifCJZkLd8l1YOtCzqWXn1-712BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
جمهوری اسلامی به جایی رسیده که نفر آورده با ماسک آموزش کلاشینکف تو برنامه زنده صداوسیما میده
📝
توان جنگیدن با آمریکا که ندارن (در صورت جنگ زمینی)، این برای کشتار مردم بی‌سلاح ایران در اعتراضات آینده ست.
📝
اسلحه بیاد بین مردم، فرصت انتقام تعدادی از ده‌ها هزار نفری که توی دی‌ماه کشتند هم بوجود میاد اما ابعاد این احتمال بزرگ نیست. ابعاد احتمالی مسلح شدن، اختلافات بین باندهای مختلف مافیای اشغالگره که با تنگ‌تر شدن محاصره اقتصادی، از خشونت سیاسی به خشونت فیزیکی دست خواهند زد. برای پول راحت‌تره آدمکشی تا برای عقیده.
@mamlekate</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/4985" target="_blank">📅 09:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4983">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYtqEC6TxZdE0TGMUmWYmyaFdvsy74TKOBkAxaEQwNJVgv3t4R8QB5Sda65tiFdd0K8W_hx9uv3AnMogQ8m-by9fDIisbyrt2-HWFkqNcSa0A156DxyQat4C10w-e-Y3SgDAsAuxoTm9sUkzwaoMlC7yB37HKEefwAdLBAb9XqHLsZ54fdoKmYxOWS4wKm_hYjXTsbYdo_KCKh--fVCnbITbCPfUpPMYDJCpTa7jtBwtwP42wR6gYYu4hQQFn18-4O1flXb6QhfCybw32CxKuBfslVqhNwlcmQyfRrlL4KHxuoi-4Eg6GBIIUn_a-L3Erq2C_I3kAQB07GcJV1ycxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=EQO69LWmtLMk90PeyqPvV9uAG7n73rtNJM_rAao-Ue9BPtGvhBFIin_vxVXXkzQeIEY9gkqx-gCKetMfJMw9WRIWourqCX768TpBzT2wmEvywPc03eNL1QyxNgh_6yapE4XbOuGdwtOD4WjeNNAe9AAJk6MZodQTT8ZQl1yPr-Z1ov8ckVHcn0P6cu9Gt3XveND6XdTtDq9lzT3G76FqNk0vTVmmpO5BqNvr10pUCfMRJqzyZ_gk8BQKc7OuBLmMPIAMmLa0ouj8Tn34d7JICZo0UQUukn9nv9lEeVOOeqVoUZUeGnFLCXnlfPPLkm1FABAFml9GteC8HNnxxNs5Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=EQO69LWmtLMk90PeyqPvV9uAG7n73rtNJM_rAao-Ue9BPtGvhBFIin_vxVXXkzQeIEY9gkqx-gCKetMfJMw9WRIWourqCX768TpBzT2wmEvywPc03eNL1QyxNgh_6yapE4XbOuGdwtOD4WjeNNAe9AAJk6MZodQTT8ZQl1yPr-Z1ov8ckVHcn0P6cu9Gt3XveND6XdTtDq9lzT3G76FqNk0vTVmmpO5BqNvr10pUCfMRJqzyZ_gk8BQKc7OuBLmMPIAMmLa0ouj8Tn34d7JICZo0UQUukn9nv9lEeVOOeqVoUZUeGnFLCXnlfPPLkm1FABAFml9GteC8HNnxxNs5Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/4983" target="_blank">📅 09:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏ترامپ: امشب، به دستور من، نیروهای شجاع آمریکایی و نیروهای مسلح نیجریه، مأموریتی بسیار پیچیده و با برنامه‌ریزی دقیق را برای از بین بردن فعال‌ترین تروریست جهان از میدان نبرد، بی‌نقص اجرا کردند.
ابو بلال المینوکی، نفر دوم فرماندهی داعش در سطح جهانی، فکر می‌کرد که می‌تواند در آفریقا پنهان شود،
اما نمی‌دانست که ما منابعی داریم که ما را در جریان کارهای او قرار می‌دهند. او دیگر مردم آفریقا را ترور نخواهد کرد یا به برنامه‌ریزی عملیات برای هدف قرار دادن آمریکایی‌ها کمک نخواهد کرد. با حذف او، عملیات جهانی داعش به میزان زیادی کاهش یافته است.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4982" target="_blank">📅 09:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=UYu3hyTVn35wxa_6ns_03JZmAE-q5drNfJWuIgqJJGo_3KUnxCBs_wv3Jb3DIreZlj9pugliGlQHOxwrs5gJle4u-KcxCZLfIET-uWRi5TuAGGNokeLgopQYKeNH0tEEjQGFThP1XfYmkK76kXpUH2KXc_yAlz6sx4u69jVwcb5u_btsQBAyTH5wCcNhny5MGnPbwWt4KKFlZ6hNzNQFvKZK5EJbEVx3wkKNZ-XoFJlEXULxu-tCrOH3o0lYfZGIBF5P0ors530rsSPlUN4F66ImMhc4lqeSASWtbtPbXP-vgjz7FYARlm0Rg_5vmfu6ebQJTHxm7sV44GqfA0O8ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=UYu3hyTVn35wxa_6ns_03JZmAE-q5drNfJWuIgqJJGo_3KUnxCBs_wv3Jb3DIreZlj9pugliGlQHOxwrs5gJle4u-KcxCZLfIET-uWRi5TuAGGNokeLgopQYKeNH0tEEjQGFThP1XfYmkK76kXpUH2KXc_yAlz6sx4u69jVwcb5u_btsQBAyTH5wCcNhny5MGnPbwWt4KKFlZ6hNzNQFvKZK5EJbEVx3wkKNZ-XoFJlEXULxu-tCrOH3o0lYfZGIBF5P0ors530rsSPlUN4F66ImMhc4lqeSASWtbtPbXP-vgjz7FYARlm0Rg_5vmfu6ebQJTHxm7sV44GqfA0O8ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها نشانه سقوطه. نشانه هراس.
پروپاگاندای پوشالی رژیم رو باور نکنید که میگن بعد از جنگ قوی‌تر شدیم!
اینها ۷۰ روزه رهبری دارند که خودشون هم تردید دارند که واقعا داشته باشن.
اینکه ۷۷ شبه، هر شب هراسیده در خیابان جمع میشن. اینکه ۷۷ روزه اینترنت رو قطع کردن و علنی هم میگن چون ترسیدیم و …
ترس اصلی‌شون هم مردم ایرانه!
و اینکه خون اون چند ده‌هزار ایرانی که ظرف دو شب کشتن ، حکومت ظالمشون رو غرق کنه.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4981" target="_blank">📅 08:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4980">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOGd_zrpywDFDin8Z-a5EOs76R5CT5xsnCt8V8sVrmPGwkXQfLnOI_pnlMfqmGi9sm4ICJsBmbm4D88uf26CsCtGqGEpz9tdJb0aSmPrlpTnvfi5BklMHgv1haS71aeiDKyhs_wYtw4zAJytcmFdYp5uhUhLncTXp8kdgCJ_dpYd-tj0KYOmj_uEo68ZXLYflEZhnJbK5uklP_WHKXizFxvwsiuRmGdZagH5J6Or4HVfPXUQs5flO2gDXqqTi-lSgvqX0kT-mYjTcOMch8CqoxOR8vpo7D-7aGcmiur3lVe3xH9RJWusjKOA1swenwj2Hb77S_c-DLCewsnr5LF-2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفت‌وگو با فاکس‌نیوز با اشاره به افزایش هزینه‌های اقتصادی ناشی از تقابل با جمهوری اسلامی، از آمریکایی‌ها خواست این فشار کوتاه‌مدت را تحمل کنند و گفت جلوگیری از تهدید حکومت ایران اولویتی بالاتر از پیامدهای کوتاه‌مدت اقتصادی دارد.
او 'گفت: «متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا گفت شی جین‌پینگ، رییس‌جمهوری چین، برای کمک به حل بحران ایران و بازگشایی تنگه هرمز اعلام آمادگی کرده، اما تاکید کرد واشینگتن «به کمک نیاز ندارد.»
ترامپ گفت چین «۴۰ درصد نفت خود» را از منطقه تنگه هرمز دریافت می‌کند و افزود: «اگر او بخواهد کمک کند، عالی است. اما ما به کمک نیاز نداریم. مشکل کمک این است که وقتی کسی به شما کمک می‌کند، همیشه در مقابل چیزی می‌خواهد.»</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4980" target="_blank">📅 08:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v93uxyY7rvuDJxik8FqcwJnpBoFuszS7KRNaE78F5rqYaCV2cxsCf2gIWuvE7AlmFomraMv3WAY55DCpUiIyr-iLUEfpC53igWHWu4tt_5QiZFEzdCYiTu7Uxqnr8EzFtzxuwwJHgtISeL8udgJHvtCvQnC_9Mos92VB5NY5pPGzY4hlonMT2snYkj2CwpwuseQEVOGZ0L5HzVaSC969mQh7Igdkj-vYyEaQrMstbJ3ioWDhsCtYtheVuPFmgqxGRDMJrmP6-e5WseTGwBOI-_D51mp2NEDkUZBX5vPJJsY8v6MtkHIg8jhYcdI_4LaLgUN77k9ryAF85wUUIJHb-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگن رهبر شجاع‌شون  ۷۰ روزه قایم شده
یک عکس بیرون نمیده!
یک فیلم ازش منتشر نمیشه
یک فایل صوتی ازش منتشر نمیشه
پیامی که میده حتی امضا هم نداره!
از طریق امضا می‌تونن جاشو پیدا کنن؟
یا موضوع چیز دیگه است؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/4979" target="_blank">📅 19:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4978">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZAAOv-T9TDQ8up6E0zJUCj0qF6FKB8UI60ul2hn1Veq_jFh12pLqW-a6RZbFoHNPljjjXei0_KboPa-WZ7jlSQM43SCURVwqwNMa_XNHXnwLiVcIGaTmV8FvrJc-K3hYKZFBJacSMioVkOLR2p28zrzB2Cl_kZfACO6qCUyc4iWGpw_mZ_8pyJJUCZLvkKh6rs_tP8-CjAnaME8Q1kkuKNLkr8crPaIgGodkRETcaI4QI8ET6xv7A40xK2cHxeatTWpgmUb8H4tvMu_MelETmNmkNP6e95Isxa_VxirLmbxmHZkVjhS8ggnb-s3mrz8tnO_hmbBdhTAP9eqW_caCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/4978" target="_blank">📅 18:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EN278CpySWIDU07_79uYMLP7_cGjbiwnA-v4ZicKB8Gtfo9NzxoDFSWGIBw-td3XeuquL_1wq4gaKpU0fQUd1tzzQHM2tjeT1jGUJHRpPmqc5P5BbSup3PXxdGyHB0xJ9u2_Se_vVLJT_DBZRJRwAiiGVYnbHbGjUVn0i6ezJ_0GJ5ljt75pYcXl8jxLsK0I5edN9goDvhhaVuJC8bKcJrcBn_Femuy_-pGnL5JAo-6A6PzwUlqtYpT_5RENOEyuqrl6XhCDxnLXSp_Hfz6ow8CKUCPoF8RnMA1Ij9l_6_On6Y1UWHlKG7FNdlD_JdPoVCQ46xb2N08CX92CnM2TPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت آمریکایی تمام هدایایی که چینی‌ها بهشون داده بودن، قبل از سوار شدن، در سطل آشغال ریختن،
نگران از اینکه مواردی در این هدایا باشه که برای جاسوسی استفاده بشه.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/4977" target="_blank">📅 16:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
برد کوپر، فرمانده سنتکام، گزارش‌ها مبنی بر اینکه جمهوری اسلامی هنوز ۷۰ تا ۷۵ درصد از ذخایر موشکی و پرتابگرهای پیش از جنگ را حفظ کرده است «نادرست» خواند. او در جلسه کمیته نیروهای مسلح سنای آمریکا گفت ارزیابی‌های منتشرشده درباره توان موشکی جمهوری اسلامی با واقعیت مطابقت ندارد، اما از ارائه جزئیات اطلاعاتی خودداری کرد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4976" target="_blank">📅 16:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=fvkMnB-kTMlEpKfhDwBYze0Ao3ZGTy_3QG7BZB4oIoVQfG0H9icktgrXvteUd5WiPL_3IZNuL9U7PDp5JeH26wt4DpwcUI8Wh_tLAmsBW-vym6wyK-gVd2KGdKRJZkZ6Vsyh40Ybs5sKKYGQFOlmX2MOEpCAeNEQ5ZNCFxC9f6jhwo9brCYvWBBPMVCJEKL4uoMJhI2lR71IalnBet1VLbsbIDvxRUyAhj8l_joBRPfSc-rVFUn2KNkf_KbRyrzSYfHvsN_ePnf46mvj7b1orQM40_kyEHC03k2lEJrYiVT_nX-W7CPNl7UQEdRD2d6hMMSyrDS5OEhHMPOblYJfOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=fvkMnB-kTMlEpKfhDwBYze0Ao3ZGTy_3QG7BZB4oIoVQfG0H9icktgrXvteUd5WiPL_3IZNuL9U7PDp5JeH26wt4DpwcUI8Wh_tLAmsBW-vym6wyK-gVd2KGdKRJZkZ6Vsyh40Ybs5sKKYGQFOlmX2MOEpCAeNEQ5ZNCFxC9f6jhwo9brCYvWBBPMVCJEKL4uoMJhI2lR71IalnBet1VLbsbIDvxRUyAhj8l_joBRPfSc-rVFUn2KNkf_KbRyrzSYfHvsN_ePnf46mvj7b1orQM40_kyEHC03k2lEJrYiVT_nX-W7CPNl7UQEdRD2d6hMMSyrDS5OEhHMPOblYJfOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : می‌دونم سؤال‌های زیادی در خصوص سفر چین وجود داره ولی بگذار اول در خصوص پیشنهاد جمهوری اسلامی بپرسیم ، آیا شما طرحشون رو رد کردید؟
ترامپ : من طرحشون رو نگاه کردم از سطر اولش خوشم نیومد دیگه انداختمش دور!
خبرنگار : توقف ۲۰ ساله غنی‌سازی برای شما کافی نیست؟
ترامپ : آره توقف غنی سازی ۲۰ ساله خوبه، اما در تضمین این توقف تردید هست باید ۲۰ سال واقعی باشه نه ظاهری</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4975" target="_blank">📅 15:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
ترامپ در خصوص ایران: ‏«ممکن است مجبور شویم کمی کار پاکسازی انجام دهیم، چون یک آتش‌بس حدوداً یک‌ماهه داشتیم.
‏ما در حقیقت آتش‌بس را به درخواست کشورهای دیگر انجام دادیم.
‏من خودم چندان موافق آن نبودم، اما این کار را به عنوان لطفی به پاکستان انجام دادیم، آدم‌های فوق‌العاده‌ای هستند، فیلد مارشال و نخست‌وزیر.»</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4974" target="_blank">📅 15:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا دیروز گفت که : «در جزیره خارک در سه روز گذشته هیچ بارگیری نفتی انجام نشده است. معتقدیم مخازن ذخیره کاملاً پر شده و هیچ کشتی‌ای وارد یا خارج نمی‌شود.»
او افزود که این وضعیت باعث تعطیلی قریب‌الوقوع تولید نفت خواهد شد.
با این‌ وجود امروز خبری منتشر شد، مبنی بر اینکه  یک تانکر بالاخره بارگیری کرده و اعلام شده که «برای اولین بار» در طول یک هفته اخیر بوده.
جمهوری اسلامی بخشی از نفت اضافه خود را در تانکرها و نفتکش‌های کهنه و‌قدیمی ذخیره می‌کند تا جریان‌ تولید، نفت متوقف نشود.
با این‌ وجود و در صورت صحت این دو خبر (عدم بارگیری در سه روز اخیر، فقط یک بارگیری در یک هفته اخیر) این به معنای مشکل جمهوری اسلامی در صادرات و یا ذخیره نفت است که می‌تواند به توان استخراج و تولید نفت ضربه بزند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4973" target="_blank">📅 10:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔺
رسانه‌های اسرائیلی : ترامپ در بازگشت از سفر چین، در خصوص از سرگیری دوباره جنگ با ایران تصمیم خواهد گرفت.
تحلیل شخصی‌‌‌ام: گره میان جمهوری اسلامی و آمریکا و اسرائیل، از زمان روی کار آمدن مجدد ترامپ تا وقوع جنگ ۱۲ روزه با گفتگو باز نشد،
سپس در مذاکرات در حد فاصل جنگ ۱۲ روزه تا وقوع جنگ ۴۰ روزه، این گره‌ باز نشد،
از زمان آتش‌بس تا امروز ، که ۳۷ روز از آتش‌بس میگذرد، از جمله در مذاکرات سطح بالای اسلام آباد باز نشد!
بلکه حتی این گره به واسطه بسته شدن تنگه هرمز، کورتر هم شده و هم به واسطه حمله جمهوری اسلامی به کشورهای عربی منطقه و پاسخ نظامی آنها، وضعیت بدتری پیدا کرده.
از آنجایی که هم جمهوری اسلامی خود را پیروز جنگ ۴۰ روزه می‌داند و این موضوع در مذاکرات اسلام‌آباد هم کاملا واضح بود و عامل اصلی شکست مذاکرات شد، و هم آمریکا خود را پیروز جنگ ۴۰ روزه می‌داند، اما تمام مشکلات هسته‌ای، غنی‌سازی، موشک و… سرجای خود هستند، پیش بینی وقوع جنگ سوم بعید نیست و احتمالا این بار جنگ با حمله به زیرساخت‌های ایران شروع شود.
برخی از کارشناسان جمهوری اسلامی در صدا و سیما حتی پیش بینی وقوع «چند جنگ» در دو سال آینده را مطرح کرده‌اند.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4972" target="_blank">📅 09:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4970">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sAOaChZjV1xQIncxxJTwQSBhFN1RrS2E2ipJwxH2cDvIrvRPMKy1npurT1eot92K0mj9HUthwj4RO6PeLZZRVC8dDe5JGKcLQQx4veA-385ab0-GarZD_zJ3Wc_klepOTnUywFCIp7oxJl8l-PvwzVDzXBBqXGR4hu48wFsBZFx3JN-E2XfxvrpG5WyG6d_aAoHCgI2M7eC1EdPJrr4DTJj4iqvEnTmU6PMO7OKrf8vzP9wm1b20rrbi3gnRSMo-tijlZn7T6t9gwy0Wy7dhMqIVwHpGs0SYRhnuRcP3hVuJM1Kx67zcMtVMRoE915SfYVv9kOavgXZNoEjFs3MKVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WD3OF4xbcGD8Ciws6DX1Bp4e9LqBkh-cTucuJdveobtTFVgwjhkKJAQqwUf9Aofd34dj4Is1GTbrqvGkxvB1aBVItWQFfz8IU_3kRUdKb-DdaW3jbN59kl1zXg-9RiJo_tpYmKYPtQaRy_yQpM5gOaUHR2zc8wAlH0dZrHDSdZOuqPzVvraV_13AcwK8MCvjoiF5CNfAYJesw-UQtK6Dj1Ta4jlfugkwcB-ZYAPawxgc-kbABNZfqj9nELsMKOIvf0qUpvCKHjDgDf1QgAtfQTGqD0QlTnTeUBgWkyN0HY4c4x740x06UZXFT1rAtApzTufZONRhrLwNcPDirLanng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی توییتی زده
که «هر کس در نهان خیانت کنه، به طور علنی رسوا میشه»
که منظورش اماراته و بحثی که بین عراقچی و نماینده امارات در جلسه «بریکس» رخ داده! و اتفاقا حرفهای عراقچی نشون میده که امارات بوده که اینها رو رسوا کرده و به شدت ناراحت شدن از حرفهای نماینده امارات که چرا در این جلسه چنین حرف‌هایی زده.
اما با زدن یک توییت! اعلام پیروزی میکنن!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4970" target="_blank">📅 08:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUHD7qqzYyw8Hz6llW4qt7g8-GDprS85NueG5CJqGUcbGLWSTXblpljjAwbKB0DucePPM7IJAgZ8F6cZjLL-UqNCMQKy_J1g2WnQWui9z5fh4p_l6af2_CJzzyJM6ofxgbOx9rywIivcvpVPbCLaEM5nUkI-s6EC-jzqle7ad5_h1x3BMxUPyV4OHVYtoPiBWm2ipNQKv8EVsDPr-sfNy3ZWKTzWkUg_pVlyJ5nRUxaHkfPgWAT5gBdltI-_U8a-YisMZAoSbCL710sqesojbQZ30dg5W7Lm4pdCCJtsTJLXDKRtFUO3_37ildaYHt-mm7xx3ArcoX8Xd-OgpsOgKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس جمهور در صدا و سیما:
با علی افشاری، پرستو فروهر، عبدالکریم سروش و….. تماس گرفتم
و از مواضع آنها تشکر کر‌دم</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4969" target="_blank">📅 08:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نامه رسمی کشورهای عربی به سازمان ملل برای درخواست غرامت از ایران
بحرین، کویت، عربستان سعودی، امارات متحده عربی، قطر و اردن در نامه‌ای مشترک خطاب به سازمان ملل، خواستار پرداخت غرامت از ایران برای خسارت‌هایی شده‌اند که جمهوری اسلامی در طول جنگ به این کشورها وارد کرده.
این درخواست در نامه‌ای که دیروز به آنتونیو گوترش، دبیرکل سازمان ملل متحد ارسال شد، گنجانده شده است. در این نامه، آنها همچنین ادعای «غیرقابل قبول» جمهوری اسلامی درباره قوانین جدید عبور کشتی‌ها از تنگه هرمز را محکوم کردند.
پیشتر نیز در اجلاس اضطراری وزرای خارجه اتحادیه عرب نیز قطعنامه‌ای تصویب شده که رسماً از ایران خواستار غرامت شده بود.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/4968" target="_blank">📅 21:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=buQGTsrK0lHkUjc07pVW-O8WPH62iXy4uo9DfR2u58y-cbC7tUxd4YhW_h1NT0ILByGtxfGxwWsmG2P9Z-g73aLR_WoeiMbuNtGSGQA20eiUdsbd2wFZQixjOGs_4PKs__8hO6oJ6Riy-EQpLErGAuLFFbEAjwpEktehQgvhpZd_WzFMQmF1oH2jR9ac_lxN4iDPMngwM2V7AkQi4_lnvp7T9S7ZDoxUz7y1l828oLn51gqtAaj0mlYydA7Gr0laBoObGRCkMZQKfWqcMjACFxqytQ24LX09bJ2j1mHM-GaFLVskhkkaT9o4R40zk3sxTwgHdI78v4Xr8mCBxeJZUxaNGXFTj_cbehHOat9gNfF_zi69jeF30hxYL_m5heWnXOdnLQN-WU5VnrXUo9OsFST2SnAcoQbfEpFp58odDfb-tUaF06I3RtU30qLPs_GQjwAQyzjnAHnf8OFCY_t1-huykoDwvzB6R5Nxk8HUWsQjAigfUJikMul3bWRVh1ia7Cj2j1AWPMelw8uaiFBamusoqZolK4BaZI6h3VrgSUWhCdn62JnQp9R6vVjQGpV7K1LFca9Bg5Yotf__D_5JEVHjLEFXDkJFnZJR15AkNkWEEgwSgvtOowEhxPcSDFyB77ZViJpGNpmtT1lyTNAygTovJUxyOak1Niy0yKNg8mc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=buQGTsrK0lHkUjc07pVW-O8WPH62iXy4uo9DfR2u58y-cbC7tUxd4YhW_h1NT0ILByGtxfGxwWsmG2P9Z-g73aLR_WoeiMbuNtGSGQA20eiUdsbd2wFZQixjOGs_4PKs__8hO6oJ6Riy-EQpLErGAuLFFbEAjwpEktehQgvhpZd_WzFMQmF1oH2jR9ac_lxN4iDPMngwM2V7AkQi4_lnvp7T9S7ZDoxUz7y1l828oLn51gqtAaj0mlYydA7Gr0laBoObGRCkMZQKfWqcMjACFxqytQ24LX09bJ2j1mHM-GaFLVskhkkaT9o4R40zk3sxTwgHdI78v4Xr8mCBxeJZUxaNGXFTj_cbehHOat9gNfF_zi69jeF30hxYL_m5heWnXOdnLQN-WU5VnrXUo9OsFST2SnAcoQbfEpFp58odDfb-tUaF06I3RtU30qLPs_GQjwAQyzjnAHnf8OFCY_t1-huykoDwvzB6R5Nxk8HUWsQjAigfUJikMul3bWRVh1ia7Cj2j1AWPMelw8uaiFBamusoqZolK4BaZI6h3VrgSUWhCdn62JnQp9R6vVjQGpV7K1LFca9Bg5Yotf__D_5JEVHjLEFXDkJFnZJR15AkNkWEEgwSgvtOowEhxPcSDFyB77ZViJpGNpmtT1lyTNAygTovJUxyOak1Niy0yKNg8mc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور چین، شی جین‌پینگ،
با موارد‌ زیر با رئیس‌جمهور ترامپ موافقت کرده:
۱.
در موضوع ایران، به آمریکا
«هر چیزی که ترامپ نیاز دارد» بدهید
.
۲. سویای بیشتری بخرید.
۳. نفت بیشتری از آمریکا بخرید.
۴- ال‌ان‌جی بیشتری از آمریکا بخرید.
۵. ۲۰۰ فروند هواپیمای بوئینگ بخرید.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4967" target="_blank">📅 20:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=GCG1mHGVSUgS6iTR-43Dyt8KAiyndZPaUbkJWf16P2y2d2u8H32kH3QZ6tPeu2YwK7YSlWRnLaHBNu-iix1ntJTb5e16e638VU6ZRxps5Ubuf6oTbY6yiECJU4Y4phARaI5NF4q3ZJD7UmvvuBcHFonvTRbceX9ID5F8UUt9xaa214MEs1A1RwHC5p_oAwiPLG_FbCIaaqWW0fThkIJrU3dUp2uAGWt0NJQVCEQ4mmAq-_PlyU_AV4yHb6AxugI3hx8fvwOjFtuFKCIgjPbdm1SJWCb91mVaCRHaIoMhXRgS7mgjDBxQClFMJYFFjofpvUZwFxazzoRFpJ1pbK-HTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=GCG1mHGVSUgS6iTR-43Dyt8KAiyndZPaUbkJWf16P2y2d2u8H32kH3QZ6tPeu2YwK7YSlWRnLaHBNu-iix1ntJTb5e16e638VU6ZRxps5Ubuf6oTbY6yiECJU4Y4phARaI5NF4q3ZJD7UmvvuBcHFonvTRbceX9ID5F8UUt9xaa214MEs1A1RwHC5p_oAwiPLG_FbCIaaqWW0fThkIJrU3dUp2uAGWt0NJQVCEQ4mmAq-_PlyU_AV4yHb6AxugI3hx8fvwOjFtuFKCIgjPbdm1SJWCb91mVaCRHaIoMhXRgS7mgjDBxQClFMJYFFjofpvUZwFxazzoRFpJ1pbK-HTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/4966" target="_blank">📅 17:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2182de948.mp4?token=XA74P-Co2zyTjOc0pTu4yeK-qR9SUAiPHu2759dtTC4DwGXtvc3PJyYErk50Wge3BHnwmlRO8zzjVAE8OjssN1XZbsMHnK6xBfHBummwUBki8229ASdqUwcK0MeWUG_I7R1w5h2Yvk_ylS10XNWnAAbLUmhrJRXFhN8TK-xvYSVhJQk6qvoHMSzoV3PJ6WYB3rit9KtZQjRntmEQtIUK7alzXqOrAtZimn84-_ZAyCjeyuQG0uQsY8gj0WveMVbxSjOJq0-tFPFe7f6LlHIZUh7OZJZdPI8e8WUlf8oQEqXAY8zq6OHOkkjOwJ0-hgfYcyZ2mxKOSFVz5UCo56UCRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2182de948.mp4?token=XA74P-Co2zyTjOc0pTu4yeK-qR9SUAiPHu2759dtTC4DwGXtvc3PJyYErk50Wge3BHnwmlRO8zzjVAE8OjssN1XZbsMHnK6xBfHBummwUBki8229ASdqUwcK0MeWUG_I7R1w5h2Yvk_ylS10XNWnAAbLUmhrJRXFhN8TK-xvYSVhJQk6qvoHMSzoV3PJ6WYB3rit9KtZQjRntmEQtIUK7alzXqOrAtZimn84-_ZAyCjeyuQG0uQsY8gj0WveMVbxSjOJq0-tFPFe7f6LlHIZUh7OZJZdPI8e8WUlf8oQEqXAY8zq6OHOkkjOwJ0-hgfYcyZ2mxKOSFVz5UCo56UCRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4965" target="_blank">📅 17:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
سپاه یک کشتی رو در اطراف امارات (فجیره) توقیف کرده و در حال انتقال اون به سمت سواحل ایرانه.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/4964" target="_blank">📅 11:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006c04d7ac.mp4?token=MFfSCYYID0wL97VxTyMJ0aLIn796hEL2LqJUqhyktr2VhynrjQ2mEyxctIfN7JIdjYJKaorvJsYqg6bXgzf-KjOZDlsk4pQcfJYme0CTUnxavoGMchCfH2MLD1OVnIRQ2UXm7_Yxc2sEpsNzvAQYewdrgfyxlyV0Uh52bI6dVj3ULQU3mEgEp1kzYy3tR2q7bFg1fNlzcWtEHZfE1ZBXJUioteSpuXY88g6-PYunigOfDfn74Ai4Q7xvQduFUtNxqvNoJsBuzzeK_RtQfD1EWcdcTZGfTfRsx9uITV6NoBR6gKBmRTxBObBCZV0uzV13hyj5yP-MoSlTrwpzq7goUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006c04d7ac.mp4?token=MFfSCYYID0wL97VxTyMJ0aLIn796hEL2LqJUqhyktr2VhynrjQ2mEyxctIfN7JIdjYJKaorvJsYqg6bXgzf-KjOZDlsk4pQcfJYme0CTUnxavoGMchCfH2MLD1OVnIRQ2UXm7_Yxc2sEpsNzvAQYewdrgfyxlyV0Uh52bI6dVj3ULQU3mEgEp1kzYy3tR2q7bFg1fNlzcWtEHZfE1ZBXJUioteSpuXY88g6-PYunigOfDfn74Ai4Q7xvQduFUtNxqvNoJsBuzzeK_RtQfD1EWcdcTZGfTfRsx9uITV6NoBR6gKBmRTxBObBCZV0uzV13hyj5yP-MoSlTrwpzq7goUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب اگه نهادهای اطلاعاتی آمریکا متوجه شدند که جمهوری اسلامی به ۳۰ سایت موشکی از ۳۳ سایت موشکی در کرانه‌های تنگه هرمز دسترسی پیدا کرده،
[دسترسی پیدا کرده، یعنی در حملات آمریکا دهانه ورودی این سایت‌ها مسدود شده بود و دوباره دسترسی پیدا کرده]
نمیشه سریع اینطور نتیجه گرفت که : پس اگه جنگ از سر گرفته بشه جمهوری اسلامی قدرتمنده و…. چون دسترسی پیدا کرده.
این گزارش یک بعد دیگه هم داره
:
اونهم اینکه نهادهای اطلاعاتی آمریکا روی این۳۳ سایت موشکی اشراف اطلاعاتی کاملی دارند!
می‌دونند دقیقا کجا هستند،
موقعیت جغرافیای اونها رو دارند، و این گزارش یعنی وضعیت اونها رو مرتب رصد می‌کنن!
و خب اگه حمله‌ای بشه، می‌تونن در همون ده دقیقه اول شروع جنگ،
اول دوباره دهانه اینها رو ببندن!
اگه قبل از جنگ ۴۰ روزه نمی‌دونستن
موقعیت این سایت‌ها رو،
و در پی حملات موشکی جمهوری اسلامی پی بردند به موقعیت این سایت‌های موشکی ، الان همه رو زیر نظر دارند و رصد می‌کنند
و شناسایی شدن!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/4963" target="_blank">📅 10:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4962">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فهرستی از رهبران کسب‌وکار که به همراه رئیس‌جمهور ترامپ در سفر به چین شرکت  کرده‌اند:
1. ایلان ماسک، مدیرعامل تسلا و اسپیس‌ایکس
2. تیم کوک، مدیرعامل اپل
3. لری فینک، مدیرعامل بلک‌راک
4. استیفن شوارتزمان، مدیرعامل بلک‌استون
5. دیوید سولومون، مدیرعامل گلدمن ساکس
6. جین فریزر، مدیرعامل سیتی‌گروپ
7. کلی اورتبرگ، مدیرعامل بوئینگ
8. مایکل میباخ، مدیرعامل مسترکارت
9. رایان مک‌ایرنری، مدیرعامل ویزا
10. لری کالپ، مدیرعامل جنرال الکتریک
11. سانجای مهروترا، مدیرعامل میکرون
12. کریستیانو آمن، مدیرعامل کوالکام
13. برایان سایکز، مدیرعامل کارگیل
14. دینا پاول مک‌کورمیک، مدیر اجرایی متا
15. جیکوب تیسن، مدیرعامل ایلومینا
16. جیم اندرسون، مدیرعامل کوهرنت</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/4962" target="_blank">📅 10:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=izqVk9izFpRNc8ZzETpX6XVnN5kXz93W4fPB8zK7PucdtvcICzV_WAevxl0xV9o8kxfW5JUl5evgaOBIe7XCswOBvROa18hfaWFL9SYEJMxrfbO2voEDdT522DNeYudxDPMtrgMTBFUj6tO0QsI_T22u6tKaVspJ1QnnPLzCPOnwLIFi4ZEZaGH_CxnDKp0l7fp4y0YG1uJkoJWkDlSqROuPwQIUrt4E48kD416w1SLp_67jysW4Z0d35JCRZbbXY_l8jXg-Uz7c3ekkRBpvlgzkl5O2F1fhQFx8TGCMdYbpqtXgrbQ3v6JR3ufDfjiEYmQsOu9_fryNq88C8xF2fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=izqVk9izFpRNc8ZzETpX6XVnN5kXz93W4fPB8zK7PucdtvcICzV_WAevxl0xV9o8kxfW5JUl5evgaOBIe7XCswOBvROa18hfaWFL9SYEJMxrfbO2voEDdT522DNeYudxDPMtrgMTBFUj6tO0QsI_T22u6tKaVspJ1QnnPLzCPOnwLIFi4ZEZaGH_CxnDKp0l7fp4y0YG1uJkoJWkDlSqROuPwQIUrt4E48kD416w1SLp_67jysW4Z0d35JCRZbbXY_l8jXg-Uz7c3ekkRBpvlgzkl5O2F1fhQFx8TGCMdYbpqtXgrbQ3v6JR3ufDfjiEYmQsOu9_fryNq88C8xF2fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور چین در دیدار با ترامپ :
چین و آمریکا از همکاری سود می‌بینند و از تقابل زیان.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4961" target="_blank">📅 10:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCSyOXnwxTQ9oX_EPZ6mHlEaPftlO6_x6PIvk9puL_AN2w9QEPx2gsJRNqxuhz9HJ5XLI8c7vilY9u-kRES6etEsuUOeYjIoPx0OPeYmTAdIoL3JMwS3JrmhjQgDIsOdhfZhX6DW6O5r64ZdVNiAzyhJ5crdsQ8mDEpxK1Bq8tlyv2QAp1ooafiaiWytxKHLB6GibZrEq5lpru-T5CG23yOg6IDmbikcZIFpsKklsu05ZkhfwLz-ZuzZB4F_qNse2Nc1yyP0wLtuhH9g_PLzmmEbAfUBkXRv5mpI55HxM7AZX1TAZ0QYEd3cmA1LpbJK9zifeVxoeg1Coa2NjKiMfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات در حال ایجاد فنس‌های محافظتی برای دفع حملات پهپادی است.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4960" target="_blank">📅 21:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">جمهوری اسلامی : ۴ مامور دستگیر شده در کویت در چهارچوب ماموریت گشت‌زنی دریایی بودند که به خاطر اختلال در سامانه ناوبری وارد آب‌های کویت شدند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4959" target="_blank">📅 20:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
ناکامی «هفت باره» دمکرات‌های سنای آمریکا در طرح محدود کردن اختیارات جنگی ترامپ در جنگ علیه جمهوری اسلامی.
دمکرات‌های سنای آمریکا هفت بار طرح محدود کردن اختیارات رئیس جمهور در  جنگ علیه ایران را به رای گذاشتند و هر ۷ بار شکست خوردند.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4958" target="_blank">📅 20:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
در یک اقدام بی‌سابقه دولت لبنان با طرح شکایتی در سازمان ملل، جمهوری اسلامی را مقصر تحمیل جنگ‌های ویرانگر به لبنان معرفی کرد.
لبنان در این نامه نهادهای جمهوری اسلامی، از جمله سپاه پاسداران را مسئول درگیر شدن این کشور در جنگ، برخلاف خواست دولت معرفی کرد.
‏این شکایت می‌گوید که این درگیری منجر به کشته و زخمی شدن هزاران شهروند لبنانی، آوارگی بیش از یک میلیون نفر، ویرانی گسترده در روستاها و شهرها، و اشغال بخش‌هایی از خاک لبنان توسط اسرائیل شده است.
لبنان در این نامه گفته با اینکه سفیر جمهوری اسلامی را اخراج کرده، اما او خاک لبنان را ترک نمی‌کند!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/4957" target="_blank">📅 20:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4956">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwNRECDXBlMb-vV_5dCNPNL5c0yevoqxTDWawLSV8xt-deh5mhznXlbbER477EAdm24FxDD9rAbfUhN64G7k4bQzSmx7-UM-wSVWU1Is9dsQ4TgiVRDbdfwH8Q8UIboD0tt1989VvUQ2Xq1OuHAyJc6quGRGRuGHXCdnz5qX88DbvpVJhkxvPLoWDwvRcbmsXysho0VRVDaRa-WKGWA3u2AaNjCnCOCEffhhKUGbbIUhhWDl7LmvjDZoCxFlMGaW-687fT2fpWHtIDl43eNWHArJh-A5OoQy_HfDNISTVBmeeJiz25PxyxQD0_7nrysELSKxcAlxEauDHf9-AOiQ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی از رسانه‌های فرانسوی دست به انتشار گزارشی به نقل از «فلورین تاردیف» خبرنگار «پاری‌مچ» زده‌اند که حکایت از روابط پنهانی امانوئل ماکرون و گلشیفته فراهانی دارد.
این خبرنگار فرانسوی در گزارش خود نوشته که سیلی که زن ماکرون به او در کنار در خروجی هواپیما زد، به خاطر همین رابطه بوده.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/4956" target="_blank">📅 14:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4955">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تداوم انتشار اخبار مشارکت نظامی امارات و عربستان در جنگ ۴۰ روزه توسط رسانه‌های غربی :
وال استریت ژورنال : رئیس موساد در طی جنگ ۴۰ روزه حداقل دو بار از امارات دیدار کرد.
‏گاردین: ‏اختلافات داخلی میان کشورهای حاشیهٔ خلیج فارس، به‌ویژه بین عربستان سعودی و امارات، در محافل خصوصی معطوف به این مسئله بوده است که آیا خشم کشورهای عربی از حملات ایران باید تا حد تلافی‌های نظامی ادامه یابد، یا این اقدام ممکن است سطحی گسترده از تنش غیرقابل کنترل را ایجاد کند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4955" target="_blank">📅 14:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4954">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
‏«کنگره ملی کردستان»، نهاد فراگیر تشکل‌های کُرد، با انتشار بیانیه‌ای صحبت‌های دونالد ترامپ درباره ارائه سلاح به گروه‌های کُرد برای مقابله با جمهوری اسلامی را رد کرد و هشدار داد چنین اظهاراتی خطر ایجاد یک کارزار خصمانه هماهنگ علیه مردم کُرد را به همراه دارد.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4954" target="_blank">📅 14:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4953">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_r5vL_E6WEuKj0YRaexy7uiUsW3QiGCet7qyNR11Q9Jm-Lx-4FNP4onZXNOnDJicVp1LuZkJnrhV-zbXmGABQ1920npNz0V2Ao7GGBC8osbmpuNE4a6J3B0bkFtqsfvZme5Y2yfii_OVO1uxslj-AiQoKvuZsShgWaOR90KugGSHzYtGn4pvQySmqOftVHk_EQpD-Fr8BnVOB6EPtk9ar8nKHEBVVqHIWYynRYTYC0ZpgWr0SbJXbZ6acwsv_mjnMVQRsWStgjB-A8caqXztWXkvMdnwimfcLCpkY-qYiVfo5NGQWG5B4i3nE6Jk4PdqBvKHTzHmrS_2shimWZETQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دولت و حکومت نیستن
مشتی راهزن و گروگانگیرن</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4953" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVFmpeuzTejCdVwNIZ9B3nRXAYX0rlrNxODzMQht44Ss0FZck8MoGvExTGD3zONw8Yqwgk2gJ0hK4VjOXdFhxgdUcKbVqk4jcb0L_w1cqc0INiq7hFiAxWQz9TynScE4sJFyGCPP4vTHNBe7abCkqNcWmT2CzZMt73hydkZM0yIMecaaeyCim_pj51BYotAwkPt2FUn8Qf37N8DRU5LZXYOr3oGxSItWOjk9WqqMMc-aw0HDLjukq9xDgZTAhfHzyimNVb3WJrMW7l0gha658bCFSjWlaWgqtns0WyiwPuSqGF8BBg3sLyfmoWIqxPCktUkwt-Tv8G89jJ-fhkfhkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا به خاطر حضور اسرائیل مسابقات «یوروویژن» رو بایکوت کرد و دیشب غایب بزرگ بود.
نماینده اسرائیل اما با اجرای یک ترانه عبری - فرانسوی - انگلیسی
به مرحله نیمه‌ نهایی رفت.
در اسپانیا فقط ۴۰٪ از جوانان حامی
این بایکوت بودند. (در ایتالیا ۳۳٪)
یعنی از هر ۱۰ جوان اسپانیایی
فقط  ۴ نفر حامی بایکوت بودند!
نماینده ایتالیا هم از ناپل بود و یک ترانه
با حال و هوای جنوب ایتالیا اجرا کرد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4952" target="_blank">📅 10:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4951">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RW_VuRhd4PNptzCEveyGTy5xAnRniQs34tumtLREZPfFe_kmOfY9P_0afzFfF_A_CELG5TFZlMr18Bh53Fn1x46LPVgVuUwx5Q9XeLsaJKELatVVkfOL8ff670_hoYXwio3rVZZM2sBUV9JKxlig_rs1nHb2c5BJuHud4G4PYUarDaCqWv4rP75RRQWFmmOA15tBuBjq5dw4AXc-_DERSxNqos0_MbIEhzWzLhgMuDD7BqxBbJ6LOkf-lV_q1CKi_9CCCIkfyFJnZezuGNFI9yRuzbbYEsCFSq7nibByeJX44-JW0R9qDciad5X1cHuZdgqLloU1tgAVOT0PZljPow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏نهادهای اطلاعاتی آمریکا:
‏جمهوری اسلامی دسترسی خود به ۳۰ سایت از ۳۳ سایت موشکی خود در امتداد تنگه هرمز را احیا کرده.
این سایت‌ها در زمان جنگ ۴۰ روزه با حمله به وردی آنها مسدود شده بودند.
همچنین ۷۰ درصد از لانچرهای متحرک خود را همچنان حفظ کرده.
‏و مجددا به ۹۰ درصد از انبار و سکوی پرتاب زیرزمینی دسترسی پیدا کرده.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/4951" target="_blank">📅 10:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rIAVGgueh-vM1JrU5CctvRCG-dMLAzi5olx_6QIHVAfm1KMNYTxVv9lBAxJ0w3PKGDLmXm-q2oE0SHyyvnNZoyiTL7YCt9hOx1cl5CRTe6TvN2z-F7vpKwd7M5DKMaOzD9P_1O7LsQQwHCl_MR1N1e-6CEYriYkRs9now11iGyczezCsQ8fGT92KPWbfeXX0x5E2nlSaTvcdg7gxaw1pf2Y4v8O06XE9EL_6UvyE_Zyzx3BUgAVV0HxFbT2IVmajXDTuB1gqPT6VhJR7v8D5qc5RIMRZWFk7AvmDwSEwYEr9fu1Pw3kWgNCGIdvn_AAqD0oWaNuExp7vNx82nbsA67E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rIAVGgueh-vM1JrU5CctvRCG-dMLAzi5olx_6QIHVAfm1KMNYTxVv9lBAxJ0w3PKGDLmXm-q2oE0SHyyvnNZoyiTL7YCt9hOx1cl5CRTe6TvN2z-F7vpKwd7M5DKMaOzD9P_1O7LsQQwHCl_MR1N1e-6CEYriYkRs9now11iGyczezCsQ8fGT92KPWbfeXX0x5E2nlSaTvcdg7gxaw1pf2Y4v8O06XE9EL_6UvyE_Zyzx3BUgAVV0HxFbT2IVmajXDTuB1gqPT6VhJR7v8D5qc5RIMRZWFk7AvmDwSEwYEr9fu1Pw3kWgNCGIdvn_AAqD0oWaNuExp7vNx82nbsA67E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد شاهزاده رضا پهلوی  از سیاست‌های ترامپ، «از یک طرف می‌گوید مردم باید قیام کنند و در عین حال می‌گوید صبر کنید، ما در حال مذاکره هستیم. این همه را گیج می‌کند.
شما نمی‌توانید سیگنال‌های متناقض
ارسال کنید.»</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/4950" target="_blank">📅 10:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa82a5c855.mp4?token=KDJ6OCfXFvWT6vyXayI87Q7zB7ZeXSJiCxnthmabNV8h9DmRDzwzvGoWaOmnKn_kr9Ta8SI5kL_ddlh-SBJOncq076o7gPJP1yt3evgVXnR5B-776i9TsIiti0wjBZgKuJDnyhqYjSBAqpDltIbO_JzAgmveXnvT1nJ_tPnGq0qFpEnaQgJ_3Hz6jQ7UBBGPca9Tf8M9lg2uF7KMwnz3OyO44biLxCS3gccAQIUyCGH3djsBqAVhCN0In-z8ETBpkNqS6Zm2me1jo0L2JTX8ALOfXq6Mm6H19e4zlZNpAvxB8rAHOdFuSBx-hFEa6JMk91Q8bplotve-Q1gwaD6KBplnDL5kcMGJmNKGpdr_XSoP9g4eVfk96Ak4pYo4zoPnzHCMfbLHiLanz0KtsbIOTtTOEsFs6Tj5pDA5POaeCwujvLS68L50MR6C9tzHOoABk5eB9muHEsRvWCMM44Ono8dHHWtAUQyomBW2Jh2UI7Ib9IsjI3Z2IZ2pKn6jUIRTQ_twUYckOe5GAwvMegWekzRvLLEtHWNgy2sXUNR7KWT01W9Wr3JAoWv2uTsdHKziSCOoW4ix3e95_1-baBQFYLCAcKumzaESpvMlLaIOyP0t8vAXzQbP8m8tNb1rr8Iw7k6oTReHSzieuEV-JEOSvZsdj2wPAW-t4kgphyez0bE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa82a5c855.mp4?token=KDJ6OCfXFvWT6vyXayI87Q7zB7ZeXSJiCxnthmabNV8h9DmRDzwzvGoWaOmnKn_kr9Ta8SI5kL_ddlh-SBJOncq076o7gPJP1yt3evgVXnR5B-776i9TsIiti0wjBZgKuJDnyhqYjSBAqpDltIbO_JzAgmveXnvT1nJ_tPnGq0qFpEnaQgJ_3Hz6jQ7UBBGPca9Tf8M9lg2uF7KMwnz3OyO44biLxCS3gccAQIUyCGH3djsBqAVhCN0In-z8ETBpkNqS6Zm2me1jo0L2JTX8ALOfXq6Mm6H19e4zlZNpAvxB8rAHOdFuSBx-hFEa6JMk91Q8bplotve-Q1gwaD6KBplnDL5kcMGJmNKGpdr_XSoP9g4eVfk96Ak4pYo4zoPnzHCMfbLHiLanz0KtsbIOTtTOEsFs6Tj5pDA5POaeCwujvLS68L50MR6C9tzHOoABk5eB9muHEsRvWCMM44Ono8dHHWtAUQyomBW2Jh2UI7Ib9IsjI3Z2IZ2pKn6jUIRTQ_twUYckOe5GAwvMegWekzRvLLEtHWNgy2sXUNR7KWT01W9Wr3JAoWv2uTsdHKziSCOoW4ix3e95_1-baBQFYLCAcKumzaESpvMlLaIOyP0t8vAXzQbP8m8tNb1rr8Iw7k6oTReHSzieuEV-JEOSvZsdj2wPAW-t4kgphyez0bE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد یه عده زمان جنگ با آب و تاب می‌نوشتن که تیم جمهوری اسلامی همگی «دکتر» هستند! دکتر قالیباف،! دکتر رضایی!
دکتر لاریجانی!
مثلا دکتر لاریجانی چند سال بعد از اینکه
«سرتیپ پاسدار» شد و رئیس سازمان
صدا و سیما بود و صد تا شغل دیگه داشت، تحت نظر «غلامعلی حدادعادل»
مدرک فلسفه گرفت!
اون محسن رضایی و قالیباف
و بقیه شون که هیچ!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4949" target="_blank">📅 10:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4948">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.  هرچند…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/4948" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhfl0PBM9rWakLKfbkgzsrRM5sA-_jAMptBNEZbMg_2ymSO3LbhPTnVYpdPeSfJhuB8n7wSWr0tmlOS8utMZl0Xky7xfZTVU0naTLtJM2BBuSF5mx5nIqj3w-zMMncMWZv76E810DZr8CAuPJ9Ord-JaAoL3hfSfNc5E8U9Vtek3zkt0TiNJBSQu3giuHQok-yCeDqjO7CKRsFCGY3zBIGLC0OoH13KlwFW68HLJ29phFzR5EU84D9KyuZrs17gmzDKD1r3eR51w4uxg8WKyz5c5TSoeazn9dp_KUhBRroYpQZVWvbGb1ztTh0Yaz2KfcczTXDlZS3sdTBu7zlEd8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.
هرچند این نشان معمولاً بخشی از پروتکل دیپلماتیک واتیکان محسوب می‌شود و معمولاً پس از چند سال خدمت به سفیران مستقر در واتیکان اعطا می‌شود، اما فضای ژئوپلیتیک کنونی و اظهارات اخیر پاپ درباره تنش‌ها با ایران، باعث شده این اقدام به موضوعی بحث‌برانگیز تبدیل شود.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/4947" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
