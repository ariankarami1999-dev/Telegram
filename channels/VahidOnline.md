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
<img src="https://cdn1.telesco.pe/file/BMQyW_zyusNN3ZGK89x5qR0-Y4uLESNENBjwfAp08RFj63-FBmnGm4W8pUNf5Aq9QZvH1LkmjnlKCF9688HZiUOf89GcJoYDv3yfVFG9ldZxO3KQ21J9bilo3mhmP3TtgUS9ZuFc1NsS5nGnDpJ0X4ZKQO8Vde-Foz8SfaGC9-qswMB4hVk6iD7L0zOt87BsOKQC6tGekQXkHawmaLSFAIdjgN8AX5lG-ZGOSmSFuixFyiRCeUnUfOzPDnVNMHcZ9xFRzCFWm23nhWYLcZO1OuwTnm6MekSvoF-khhVlMwKcKi6wD8BJZupj__vCQ_4Nlbc8yy_yt50RbnMlYnV6Kw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.39M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 23:46:47</div>
<hr>

<div class="tg-post" id="msg-78623">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JUqxoa12H0cqv2hiY7_uUi_HkYBa0d3PvSMwgPL3qqyNTJo6udXEIYtd34_z_7tSURstxfqHxXYEqpJehoXbNU3jCTrpALowDR02k5_lL9Jp0RRGAt7GDC0w8EpAFEcVECqOIcTZAE3jH-Twaw88aSvOCxegHwluF_ZFhsLYTmtkyZlos-s2jy_8g7h0H-DwL26ofMAtr7yrvP9Z4ICedHZbJ1ZU7-LWHEljSOuyRxLhVCl9TkjSwQWLeFSoWLC4ql51WI2NiJ3gKvbCCoQfYEuqZWd8KUuVd5wbo7Trz1QZHt3lBkBcgmwTUj1HS17wk7vMzv0Xh7I8-0kBrktVvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نفت ایران در پی افشا شدن توقف کامل بارگیری نفت خام کناره‌گیری کرد
معاون ارتباطات و اطلاع رسانی دفتر رئیس‌جمهور ایران روز یکشنبه ۱۲ مهر اعلام کرد که استعفای محسن پاک‌نژاد، وزیر نفت، مورد پذیرش مسعود پزشکیان قرار گرفت.
مهدی طباطبایی در شبکه ایکس نوشت که حمید بورد به به عنوان سرپرست وزارت نفت منصوب شده است. بورد به عنوان معاون وزیر و مدیرعامل شرکت ملی نفت ایران فعالیت می‌کرد.
کناره‌گیری پاک‌نژاد از وزارت نفت در حالی رخ داده که محاصره دریایی ایالات متحده علیه ایران که از ۲۳ تیر ماه دور دوم آن آغاز شده است، صادرات نفت ایران را به‌شدت کاهش داده است.
وزیر خزانه‌داری آمریکا روز نهم مهر اعلام کرد: «ایران در ماه سپتامبر صفر بشکه نفت خام روی نفتکش‌ها بارگیری کرد» و افزود دولت دونالد ترامپ در حال قطع «حیاتی‌ترین منبع درآمدی» جمهوری اسلامی است.
داده‌های اولیهٔ ردیابی نفتکش‌ها که بلومبرگ منتشر کرده و همچنین اطلاعات شرکت‌های کپلر و ورتکسا نشان می‌دهد در سراسر ماه سپتامبر هیچ بارگیری نفت خامی از بنادر ایران ثبت نشده است.
اسکات بسنت هفته گذشته در گفت‌وگو با شبکه فاکس‌نیوز اعلام کرد برآورد دولت آمریکا این است که حدود ۱۵ میلیون بشکه نفت ایران همچنان در مسیر تحویل، عمدتاً به چین، قرار دارد و پس از تحویل این محموله‌ها تهران «چیزی برای تجارت در برابر هیچ چیز دیگری» نخواهد داشت.
محسن پاک‌نژاد ساعتی پیش از استعفا، بر اساس ویدئویی که رسانه‌های ایران منتشر کردند، گفت درآمد ناشی از نفت فروخته شده «وصول» می‌شود و این روند ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/VahidOnline/78623" target="_blank">📅 21:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78622">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_4n-If7Q5-UtWAz0jIPPlXuh36DsEVc623PdjFW9RhR_uDuj1xaRlychgrW0L6LhjRqAh556mhE1PqchB7Mgi9_4XOF4CvJL1jyjquO9uyNVo9oidcWetUOCjS8PvWMUVtE5DChOfs4Z4cghiCSPA5agf3AahdmG3MS06xHmgZyoPT25ONjV-WpI6PI6pHA2s49yv_Yo7gOkTfnmb3mG5TVrIqD7dq2lttc69OYMBsDpc5agbC4RwFVIef9CceQVK4Dy33EfdcbEZ_PJAl5bmMRo0T_UC7k8CS-bQnF_5DlaMCFOGoMAa7irN-T53PJ3fAjvZMSWS4eCH7zfrexgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار ارز و طلا در یکشنبه ۱۲ مهر همچنان در مسیر صعودی قرار دارد. قیمت دلار آمریکا با افزایش نسبت به روز گذشته به ۲۷۳ هزار و ۱۰۰ تومان رسیده است.
دلار در ساعت ۱۵ روز گذشته ۲۶۸ هزار و ۵۰۰ تومان بود و به این ترتیب در کمتر از یک روز ۴ هزار و ۶۰۰ تومان، معادل حدود ۱.۷ درصد افزایش قیمت داشته است.
یورو نیز از ۳۰۲ هزار و ۲۰۰ تومان به ۳۰۷ هزار و ۴۰۰ تومان رسیده و پوند انگلیس با افزایش از ۳۵۲ هزار به ۳۵۸ هزار تومان معامله می‌شود. درهم امارات نیز به ۷۴ هزار و ۳۵۰ تومان، یوآن چین به ۴۰ هزار و ۸۴۰ تومان و لیر ترکیه به ۵ هزار و ۶۴۰ تومان رسیده‌اند. قیمت تتر نیز ۲۷۱ هزار و ۶۰۰ تومان اعلام شده است.
در بازار طلا و سکه نیز روند افزایش قیمت ادامه دارد. بر اساس نرخ‌های منتشرشده امروز، هر گرم طلای ۱۸ عیار حدود ۲۶ میلیون و ۳۸۵ هزار تومان و سکه امامی حدود ۲۷۳ میلیون و ۸۳۰ هزار تومان معامله می‌شود. سکه امامی نسبت به نرخ ۲۷۰ میلیون و ۹۰۰ هزار تومانی روز گذشته حدود ۲ میلیون و ۹۳۰ هزار تومان افزایش داشته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/78622" target="_blank">📅 15:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78621">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVW4whK3My570GGy4Q4BEwgkKviyzYyrVb3frMWXUgo25zHKQwZN-QZHinsp3lJMsZFqnGFD3X9KzhLzDPX2xVv3yzcP998iT9u25VzLdLx99EdvJQG3EWWqcghdVdEuQlORbYbY7OJDs7uaLEXjX2dc9NAsjAABF7c7rXE7A9FM02Km9fKVlw1C1SOhMmLXX-Cs-dCwFs9ALGv2NOJgWuTLI3rE6q-GYbWMCE0J_kAUuJmarhPw5UTEi02z70faVHGuZ1E8_xJaiwpG4pcfQnn1elbJxN9C6KGEXH2C1Q_ekxlM_Qyi6euscImB01mfplTIbzPBIKPLZT1qC5WPRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز یکشنبه ۱۲ مهر با اشاره به دیدارهایش با مقام‌های کشورهای منطقه گفت این رایزنی‌ها «بسیار موثر، محترمانه و دوستانه» بوده است.
او افزود: «ما مسیر جدیدی برای ایجاد اعتماد میان کشورهای همسایه و جمهوری اسلامی ایران آغاز کرده‌ایم و به‌خصوص در حوزه خلیج فارس، این مسیر را به خوبی طی می‌کنیم.»
وزیر امور خارجه جمهوری اسلامی همچنین گفت کشورهای حوزه خلیج فارس در این روند با ایران همراه هستند و به گفته او، «اراده مشترکی برای ایجاد صلح، ثبات و امنیت در منطقه خلیج فارس، با مشارکت خود کشورهای منطقه، شکل گرفته است که اکنون به‌طور جدی دنبال می‌شود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/78621" target="_blank">📅 15:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78619">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D5ELcLssYPnOPZezQwgy-IonFavQtwfF11G1cOzMinMSj5xnlD0YqZODX6nf7MTyqvO0s5HC2-tiQyoLKVv6kr9j7P8dfyiIUtJRYPkDRPbOKbk6Dozqr4zicc0UdC0G-yWfzR1bvCHOHoEVSU4XhMbBVxGWObhSkVtNBO_ndQE_HUW-L8pooBc3IKeUWLrpIz58fXO_QpStg3docfXmszqHXgdcB8TCpir89vnNs4i4Hgo7qZjCme9dVC3nGzO_b1wgB9KBQ07ZA7mCwqacWJQOHhpgjzzqzB5KLpn-DkrD4It4aIRAUIiNVtg3v485efF-6UUzr3wIum9DJCVQBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2e9c326279.mp4?token=TIb4KMc9tJHyx4EalXOZoRsb4xNzQ3R89mSqH6tsGT86QmqOK_QON4uqbb53U9rvuV_BCquwxDlSbWW11MeIR3GuDQVbTsm2KZnSssnIceaqsSfOvNnP9tW_FXtTf4iKWJZ8zii96C75mKh6EGRBEMaaL_oFaSyCyuOGX1rAIKH2tKw2RrYS9z8X48np-7b_rN7vJPNoi3bZOWChhEZi3tT4PPFzDtVu-iCEnVQ7AaCLXdff9sGUPQvDP0k2yir-QHHgrevomNptxDhRde9vYmGtFooY0K5RUCAqZnoVbdWsWPCqroLqoEjUX-nTivuMy7dhq3t4GFycifQP-pKV4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2e9c326279.mp4?token=TIb4KMc9tJHyx4EalXOZoRsb4xNzQ3R89mSqH6tsGT86QmqOK_QON4uqbb53U9rvuV_BCquwxDlSbWW11MeIR3GuDQVbTsm2KZnSssnIceaqsSfOvNnP9tW_FXtTf4iKWJZ8zii96C75mKh6EGRBEMaaL_oFaSyCyuOGX1rAIKH2tKw2RrYS9z8X48np-7b_rN7vJPNoi3bZOWChhEZi3tT4PPFzDtVu-iCEnVQ7AaCLXdff9sGUPQvDP0k2yir-QHHgrevomNptxDhRde9vYmGtFooY0K5RUCAqZnoVbdWsWPCqroLqoEjUX-nTivuMy7dhq3t4GFycifQP-pKV4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، روز شنبه، با اشاره به تحولات جاری میان تهران و واشنگتن به خبرنگاران اعلام کرد که به‌زودی درباره ایران تصمیم‌گیری خواهد کرد.
رئیس‌جمهوری آمریکا با تاکید بر اینکه «ایران درهم کوبیده شده است» گفت: «تصمیمی است که درباره ایران خواهم گرفت. تنها مسئله این است که یا از راه آسان خواهد بود یا از راه سخت. ما این موضوع را یا از راه آسان حل می‌کنیم یا از راه سخت.» او در ادامه افزود: «ضمنا همان‌طور که می‌دانید، ایران عملا از هرگونه برنامه‌ای برای دستیابی به سلاح هسته‌ای دست کشیده است.»
@
VahidOOnLine
پیت هگست، وزیر دفاع آمریکا، روز شنبه، ۱۱ مهرماه، از پاسخ به سوال‌ها درباره اعزام ناو جدید خودداری، اما تأکید کرد که رئیس جمهور آمریکا «مصمم است» از دستیابی حکومت ایران به سلاح هسته‌ای جلوگیری کند.
هگست که روز شنبه با خبرنگاران سخن می‌گفت از پاسخ صریح به این پرسش که آیا جنگ با ایران تا پایان سال جاری میلادی، سه ماه دیگر، به سرانجام خواهد رسید خودداری کرد و تصمیم در این باره را با دونالد ترامپ دانست.
روز شنبه، چند رسانهٔ خبری آمریکا گزارش دادند که پنتاگون در حال اعزام ناوگروه ناو هواپیمابر «تئودور روزولت» و یک گروه آبی‌ـ‌خاکی تفنگداران دریایی به خاورمیانه است؛ اقدامی که در صورت اجرا شمار ناوهای هواپیمابر آمریکا در منطقه را به سه فروند می‌رساند.
وال‌استریت جورنال به نقل از مقام‌های آمریکایی بدون ذکر نام آنها نوشت این اعزام، همراه با گروه آبی‌ـ‌خاکی «ماکین آیلند»، بین ۹ تا ۱۰ هزار نیروی نظامی دیگر به منطقه می‌افزاید. به نوشته این روزنامه، «تئودور روزولت» به ناوهای هواپیمابر «جرج اچ. دبلیو. بوش» و «جرج واشینگتن» خواهد پیوست که در منطقه حضور دارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/78619" target="_blank">📅 15:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78615">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BlymUWEv8xqivwGMaCj8NAhs4C-u18ggLd_KZK3wXBtx75l-q46i8ozUoE4cRsQVourV0vOpEwevlZCAttMKrL9qM3M3C3XooimkGjdD5ZUiT5JGWqmQ07cc_DwN8nnV52vKgF9rRJnuDcjg4tDMFd3ybMF1BecKHU3WiBtB1P9awkqSWE38Bvq-gqItCzRLNdxzUMidh6bjBb-a7zXzct6fjxgydYSDzG219nQa77Hti4uAvn37VibykbeXQj0cGEskNpE_j4UwWPl4xzL8smrJJ29K98esiKUb3DEiVrpC2mjh9CAZinKWclhe_QimWYdf-ykintgU5lBJxZI46A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bifFh_P-mVPNndmEwG1YC92XXGWRKFa2MoQ1OalRX6aymvGRRvUGXtodyKbbLk--r6Wjy5TKipD8MaQVFpS0ugDaq8vVRRR4b1HpJlRGlArQ1UAGgRrj6UyjXZ8ls_01TFF8G_Xty0EjFkdTV4qMpumJBEqX4l939XW4n4N0-Yr7wIu3bG3SuwjBG8S-GOO2VWvm0SmyG8LozjIvPjvIAOakiSMawutnqChKQdRg1HKCoQ_JGaKT9ogN48GvvpuX27ZX_auFZRbf7FAFL9mKdf2OtJJf6bs28r9lGOI-kLfEgDI2Q7uaLpZswk3ystlOp0MfiGXKxQayB0nXPAoxSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ndgm7oEL62v5b8noGUvnK92mA22gkNZ85fcR96LkuizKqsX6LH9BYff0wdtXBghj6T0lG33OyM5OwaMtsalnsZ6yzKXM5MfCy0p9Smrv-7XJ4UI6pWTTzgbRqOwPWsYrTk87IOzDatDnnblYZ_ny8VgmglYeOM-vLhn4SGnjWS0nzK5aKQjXDTjYAln4Ex2IirH2JYqp64UAfVvfxRPdBhsNSWl2KJiBvg6wLlZ079eEKPrIr_R8Yfl8EUUEMhtAjibQz1PhvD4Uh4dAYZcSJQrSjP8P8N44IejYJhuGC12CkmN-q8PGuLqhiAtb0mWQPtj7HWILzy3Hq6CoUr375g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kqBp3KPRMRqz9r2eHJbE_tpdLO9Z0XVFqILo5KUVoOUPhGFIIwJ5Qqh0cxBAYCDswcCiuLAoI43PSKMO5GH_9dPZ9ZEzAH7eEKqHTIKUEibA6nLwDNCaC866C05NXPHhBEdnAL5ZY-jxuVy91Pp7-OH1AOrn1Ndu7qAn8yL98FkQ6yTkz_y0tYiRNvoNmdnlrvXnE_nJwtML4RJ4HduQ59T0mkcEvzqqqCVPtNmR4TAwr9GrnubvrSeqpzvug8akbypVAhCspHcGKs8syHEPMP_KX5_djSEhpwts_BN1Y53zq4j3zGVuTyxM8HhoByBo9cLcSiAtbujEdwT1XyrESA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
صدور و تایید احکام اعدام برای سه زن در پرونده‌هایی با اتهامات امنیتی، نگرانی‌ها درباره استفاده گسترده‌تر از مجازات اعدام علیه بازداشت‌شدگان و متهمان پرونده‌های سیاسی و امنیتی را افزایش داده است.
🔸
محبوبه شعبانی در پرونده‌ای به اعدام محکوم شده که امدادرسانی و انتقال معترضان مجروح از جمله اقدامات منتسب به اوست. مژده هاشمی بازرگانی، که حکم اعدامش در دیوان عالی کشور تأیید شده، از شکنجه، اعتراف اجباری و محرومیت از وکیل انتخابی سخن گفته است. سودا ابراهیمی شمس‌آبادی نیز با اتهاماتی از جمله فعالیت رسانه‌ای و ارسال تصاویر برای رسانه‌های فارسی‌زبان خارج از کشور به اعدام محکوم شده است.
🔸
هر سه زن با خطر اجرای حکم اعدام روبه‌رو هستند.
@IranRights</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/78615" target="_blank">📅 15:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78614">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LBFZmd6kHbT3OkaRkUGvzhTydEyLKTiR_tdUmltIbrjeHI0RaAf4rCILz9vnr3oNY62FIVnRirP-xcTWZpYtYspiP3l9eh8s4A6Y8J88JIW33ED5iDQ2Cu1oSF32VR3MLucXa0MBaH5KJ7LlXjiGduPPHgJIJM6OY_kUdpBsawrejVSC6-vLtqzTYW7JCzpj5ZBAYJGjLZbqG_5VLYbYdJX423xLbeB5CE3FsqGC3YcUZDAjMe_HPe-INonXPe54VTfM8LBaBzEVh6XhemyX4pnK8lczoojBx4dZZHim-LoP0sFAkE0kHtvwI_q1iKw5f6c09j-k2-kpnv2sq__Xtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس روز شنبه یازدهم مهر از شنیده شدن صدای انفجار در تنگه هرمز و هدف گرفته شدن یک کشتی تجاری در مسیر عمان خبر داد.
فارس مدعی شد، نفتکش «اور وینست» که تحت اسکورت آمریکا قرار دارد، هنگام ورود به تنگه هرمز سامانه رهگیری خود را خاموش کرده بود. این خبرگزاری دولتی نوشت، این دومین هدف‌گیری یک نفتکش در تنگه هرمز در روز شنبه است.
این خبر پس از آن منتشر شد که خبرگزاری مهر ساعتی پیش از شنیده شدن صدای انفجارهایی از سمت دریا در جزیره قشم خبر داده بود و احتمال ارتباط این صداها با شلیک به «کشتی‌های متخلف در تنگه هرمز» را مطرح کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78614" target="_blank">📅 20:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78613">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtA_EFboczpsnm8pdzpvUvVDURRtBFnNY47yb0w2Jw-sQSISaHNrlFH2nWVIXbS4S363dyfALPZnJjAO_MT4PNR_uAQ9h7v_iIZt6czQrfkYujs6OF1s6vf0biRcrbOl_xStU1-nzsCbvckit90RlEFC_O4c0iI1tRs3WcvrA8vA-Of26Q3pzUKlOG9i_f2y8Qd7cTRQRpPvsr1y29FO9cA0ERmOfJmQzmUWFDxpV9RZdJJQn0zb6YomWZrhGJgeMGRVhYkSUJnlZjT2dWuRZOLjNXSIr0l4poQ-dI2a7zD5T-M06T62hL1DEDiiH97THAAhaoar2sAEMR96D61OwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی انتشار گزارش‌هایی از شنیده‌شدن صدای چند انفجار در جزیره قشم در عصر شنبه ۱۱ مهرماه، خبرگزاری مهر نوشت این صداها مرتبط با اقداماتی در خلیج فارس و تنگه هرمز است.
این خبرگزاری بدون استناد به منابع رسمی نوشت «هیچ اصابت یا حادثه امنیتی در پهنه سرزمینی جزیره» رخ نداده است.
خبرگزاری مهر در عین حال این «احتمال» را مطرح کرد که صداهای انفجار شاید به «شلیک به کشتی‌ها» در تنگه هرمز مرتبط باشد.
این در حالی است که همزمان، تصاویر متعدد و گزارش‌هایی در شبکه‌های اجتماعی منتشر شده که یک قطعه بزرگ و استوانه‌ای‌شکل را در محدوده‌ای شهری در قشم نشان می‌دهد که ظاهر آن به بخشی از یک پرتابه نظامی-دفاعی شبیه است.
گزارش‌های تأییدنشدهٔ دیگری در شبکه‌های اجتماعی نیز حاکی است که پیش از سقوط این قطعه، صدای عملیات پدافندی و چند انفجار در قشم به گوش رسیده است.
مقام‌های رسمی تاکنون توضیحی دربارهٔ تصاویر منتشرشده و این حادثه در قشم ارائه نکرده‌اند و رادیوفردا نمی‌تواند جزئیات گزارش‌های منتشرشده را به‌طور مستقل تأیید کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78613" target="_blank">📅 20:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78612">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iXVt26EmE1VuAOWmmtGDhdmcffnQv-wMN_osvre6Piy8_H6J883EUKcVbJHxC6UsZAODXwxJwmCBD5TPxGYtXMUpQXx1_TwGE8EoEhlF58IXkym0YKt323VYou5uKhHQ1fZJsTL-BA5KZtYRmA_87XdbN8ctX-PDw_m3BOuSQrNhpGRgltnBBHDURD82DATMKMvEttB_t5hhUSYywSaCCIlpdMpJjnIKLWteenoBXvQ_RmoubKi-FDah2N3F0q6ZJSgNhuIG1-73_EetEmwbSdEhCEn9fJVsKO85k0gpP9mSqmPvQMGMJHNf8Nl5PijRyr4wvXS881xd3BiHsCO0Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی از قشم  حدود ساعت ۱۶:۳۰:  صدای جنگنده خیلی نزدیک اومد صدا زیاد قشم  همین الان قشم موشک شلیک کردن  16:34 دقیقه   وحید جان از قشم سمت اسکله بهمن موشک شلیک کردن صداش خیلی وحشتناک بود معلوم نیست شلیک کردن یا جنگنده بود ولی هرچی بود صداش خیلی زیاد…</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78612" target="_blank">📅 17:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78611">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jxgf4lxOOFhugM3m0Oc3owMb6gU1VX9JU3AhKyRFAS1k0cQoCdFw2Tq_82BJueW3iZMT__FtvIGQ5W-af_7kxc7-kzk5rCUhX1kIfEiE5V6-60VD18469MfK0oq6WvMuGt_w9gU3VEmtNiZ5UAcVmZoNL0zEXmao01u2VUkt42GBGM52QYUyWKouMSZL1Q_t3EFH7JmF_VBm19GlWvxTHYNT_nV7Nyx9Qq2ZqGYH6wulEN4rBnzZtWioNwWJIIo3KEOnXavVkSM68UpTd_YIBVhzK4d3tj3556bS5bUJSBPwuNYjBr7avOgR0xmowWHWDqxhNkjJF51MOseDjLoXlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند کاهش ارزش پول ملی ایران روز شنبه ۱۱ مهر ادامه یافت و بهای دلار آمریکا در بازار آزاد برای نخستین بار از مرز ۲۷۰ هزار تومان عبور کرد.
بر اساس نرخ‌های اعلام‌شده در ظهر شنبه، قیمت فروش دلار به حدود ۲۷۱ هزار تومان و یورو به بیش از ۳۰۵ هزار تومان رسید.
این در حالی است که روز پنج‌شنبه قیمت دلار در بازار آزاد حدود ۲۵۸ هزار تومان گزارش شده بود؛ به این ترتیب بهای دلار در فاصله دو روز بیش از ۱۳ هزار تومان، معادل حدود پنج درصد، افزایش یافته است.
افزایش قیمت ارزهای خارجی در حالی ادامه دارد که بانک مرکزی جمهوری اسلامی روز چهارشنبه از برنامه‌ریزی برای عرضهٔ دو میلیارد دلار اسکناس به بازار خبر داده بود.
قوه قضاییه نیز از برخورد با کانال‌ها و صفحاتی که آن‌ها را عامل «قیمت‌گذاری کاذب ارز» می‌خواند، خبر داده است.
اقتصاد ایران همزمان زیر فشار جنگ با آمریکا، تحریم‌ها و محدودیت‌های فزاینده بر تجارت خارجی ناشی از محاصره دریایی قرار دارد.
ارزش پول ملی ایران، از ۲۳ تیر، زمان آغاز محاصره دریایی آمریکا علیه ایران، تاکنون بیش از ۳۱ درصد کاهش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/78611" target="_blank">📅 17:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78610">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbcNzN3JZS5znbFL3nUNAMrjnD5IkvfQPKYO6GrsnO4ZkYbQwbHDdFqhV-CY7UXKPpdlPpy-y3CGh5DycsEiLxrReduUH2fMGdVG43AnmLm-FV6EyQ1cwZzguEvPZs9zR-e5OdqpBCkyRT5CIhFi1pC3cfHOG9uDshpujKIFNVvX3lyovXqI6e-riayqSCX_L3z63rmtvEQRD68RSx3A2RxmuhBtuG2ahXEGivCly9nlmuyr1HQqyS23vd7AgycFw8OGrVialj-MS873HD7WxoZgNhaF0yf8O-yUuOK1f9EFFzJr7N7SipEY1jVH4F1cqZPN3Ftlmj8DkB9aBxaflA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا در گفتگو با رسانه آکسیوس،‌ با تاکید بر تاثیربخشی محاصره دریایی ایران اعلام کرد، ایران برای نخستین بار از زمان آغاز صادرات نفت، در هفته جاری هیچ نفتی برای بارگیری و انتقال از طریق دریا نخواهد داشت.
او همچنین با اشاره به کم اثر شدن نفود نیروهای مسلح جمهوری اسلامی در تنگه هرمز افزود، آمریکا عبور ۱.۱ میلیارد بشکه نفت از را از این آبراهه تسهیل کرده است.
وزیر خزانه‌داری آمریکا همچنین گفت واشنگتن در حال منزوی کردن ایران «به شکلی بی‌سابقه» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/78610" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78609">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3cTtXh_6DopGarUql5raNJ6IODCSRnFe-xGfRk5aPH0HZvLedojlZQIzB01qEcHRuLg67RMgL2M4nc8QGkOyt9Z7d81BIIKCmLiWZpwJHzlSF6jXaYuZVfGONH1fPnpG-GE6NlvdZDU_1VN3abOcQ8N1zrS2gdQAu1anSgOvaqivUmowFUXgItFFArdNZdS1Hf2sX48D1bYVA_NrLlPEXqzyVHmqLAiREbDzKGukijF8IBLBDpWXMFdi3SW_xgZ0YQs6d-dcVKAFqz7zJPNimfMv8UVyyVH0b05WCx4JraxmMvrjHlESU1f_KD3gNj0-7yrwPoXEwVB-IZsZAGOPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس مبارزه با تروریسم بریتانیا دو تبعه ایران را به برنامه‌ریزی برای حمله‌ای تروریستی علیه جامعه یهودیان منچستر متهم کرده است.
پلیس بریتانیا روز جمعه ۱۰ مهر ۱۴۰۵ این دو نفر را «سلام احمدیان»، ۳۶ ساله و ساکن لیورپول، و «رحمان صالحی»، ۳۴ ساله و ساکن سالفورد، معرفی کرد.
این دو نفر روز یکشنبه ۲۹ شهریور در منچستر بازداشت شدند و روز جمعه به اتهام انجام اقداماتی در راستای تدارک عملیات تروریستی تفهیم اتهام شدند.
قرار است احمدیان و صالحی روز شنبه ۱۱ مهر ۱۴۰۵ در دادگاه حاضر شوند.
پلیس می‌گوید این دو نفر برای پیشبرد توطئه ادعایی خود با فرد سومی در خارج از بریتانیا، که احتمالا در ایران حضور دارد، در تماس بوده‌اند.
به گفته پلیس، احمدیان و صالحی از طریق پیام‌رسان‌های رمزگذاری‌شده با این فرد درباره تهیه قطعات لازم برای ساخت یک بمب دست‌ساز گفت‌وگو کرده‌اند.
این دو نفر همچنین متهم شده‌اند که فایل‌های ویدیویی آموزش ساخت و مونتاژ بمب دریافت کرده، مایعات و تجهیزات مورد نیاز را تهیه کرده و برای شناسایی و بررسی اهداف احتمالی حمله از اینترنت استفاده کرده‌اند.
«ویکی ایوانز»، معاون دستیار کمیسر و هماهنگ‌کننده ارشد پلیس مبارزه با تروریسم بریتانیا، گفت این بازداشت‌ها نتیجه تحقیقات مشترک پلیس مبارزه با تروریسم و نهادهای امنیتی بوده و به خنثی‌شدن توطئه‌ای علیه جامعه یهودیان منچستر منجر شده است.
او اتهام‌های مطرح‌شده در این پرونده را «بسیار جدی» توصیف کرد.
این توطئه ادعایی هم‌زمان با اعیاد مقدس یهودیان، سالگرد حمله تروریستی سال گذشته به کنیسه «هیتون‌ پارک» و افزایش گزارش‌ها درباره حوادث یهو‌دستیزانه در سراسر بریتانیا خنثی شده است.
دولت بریتانیا دو روز پیش از اعلام این اتهام‌ها، جمهوری اسلامی را به دست داشتن در تلاش برای خرابکاری در پایگاه نیروی هوایی سلطنتی «فیرفورد» متهم کرده بود.
«دونالد ترامپ»، رییس‌جمهوری آمریکا، روز چهارشنبه ۸ مهر ۱۴۰۵ در پاسخ به پرسشی درباره نقش ادعایی جمهوری اسلامی در حادثه امنیتی اطراف این پایگاه گفت واشینگتن در حال بررسی موضوع است.
پایگاه فیرفورد پیشتر در اختیار نیروهای آمریکایی برای انجام حملات علیه مواضع جمهوری اسلامی قرار گرفته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/78609" target="_blank">📅 17:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78607">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DTITp46v0Wn3mRC9YGe882kkZWvYpijuc6CIMRdqC2JNQrMiJRltTUR0pok9NVuhgzJrxvuIer6-Jf2TOlKNF_z6LQnjlCPxPzxHhjEsHjBccWPOUZ8RE8arMGCQVqSIeXSeYIp-G5-leRr1tCgsptgeWI2ezs2-e2zOk0usiKNSMRB6Zj1W8MrauRIRc4jQ6Af7eBO90dtWl1W4KaHWlX3Z-KeudZjxqbcCP__zeYr-FKC9Zzzm_rxo7dzqvkE3gUpWvd47pi4Q3-AAyrTVutG6Pvu0aaCGiYTDgtZDCHQIFm5ygt090yEBw7H0m_3clTu3BkyBPTr3weYmzIGy9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cgA4ndTrdcHUWJ5C2RqhgUyXNWQn3tkUjPnc_UMbgg85mHGTUqqF7sU5ZvXeaezmXIoSntPakQLTrwR4dRgdmNTg_YSpVyHuBoAWjKi5wWhi1ZJ7FOv4y0PdyCBwLFk2CQeaK2XD1IIinxsIPJ4nzLCBaYoeUdk0PQ8yJ5Frl_pYHmc7u7HRaPc6DYeaKnIzOf4kSHVPIg4KAugiJhSAuVyP1it6lu2OZ2sckJAdPP0Nl-hJ3LIa6xzLCfIzLyTGAtV222PZ9yacTekSnJYULI2yXqaYAUqJCXVFmRVaZcZWLRBkm-Uge3BJdyIYOJslDnWMHTe94aZVv-IGbZfoIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتانیاهو: جمهوری اسلامی سقوط خواهد کرد و «روز آزادی» مردم ایران فرا خواهد رسید
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مصاحبه‌ای اختصاصی با روزنامه دیلی‌میل که روز شنبه ۱۱ مهر منتشر شد، گفت که به اعتقاد او جمهوری اسلامی «سقوط خواهد کرد» و خطاب به مخالفان حکومت ایران گفت: «ایمان خود را از دست ندهید، روز آزادی شما فرا خواهد رسید.»
نتانیاهو در این گفتگو مدعی شد حکومت جمهوری اسلامی ایران در شرایط کنونی «بسیار ضعیف» شده و گفت محاصره آمریکا به رهبری دونالد ترامپ، سپاه پاسداران را به‌شدت تضعیف کرده است. او در عین حال تاکید کرد که سقوط حکومت ممکن است زمان ببرد.
او درباره برنامه هسته‌ای جمهوری اسلامی نیز گفت اسرائیل با همکاری آمریکا، مانع دستیابی ایران به سلاح هسته‌ای شده است. نتانیاهو گفت: «اگر ایران اکنون سلاح هسته‌ای داشت، چه اتفاقی می‌افتاد؟» و افزود که جمهوری اسلامی همزمان در حال توسعه موشک‌های دوربرد است.
@
VahidOOnLine
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتقاد از سیاست دولت‌های غربی و به‌ویژه بریتانیا گفت آنها انتقادهای خود را بر اسرائیل متمرکز کرده‌اند، در حالی که به گفته او، تهدید جمهوری اسلامی و نیروهای نیابتی آن را نادیده می‌گیرند.
او خطاب به معترضان در بریتانیا پرسید چرا به جای اسرائیل، مقابل سفارت جمهوری اسلامی اعتراض نمی‌کنند.
نتانیاهو گفت: «چیزی که به مردم بریتانیا می‌گویم این است: کجا هستید؟ کسانی که علیه ما اعتراض می‌کنند، چرا مقابل سفارت جمهوری اسلامی اعتراض نمی‌کنید؟ چرا تمام زهر دولت بریتانیا متوجه آنها نمی‌شود؟»
او افزود: «چرا علیه جمهوری اسلامی جهت‌گیری نمی‌شود؟ چرا علیه نیروهای نیابتی آن نیست؟»
نخست‌وزیر اسرائیل همچنین دولت‌های غربی را متهم کرد که تهدید جمهوری اسلامی را به رسمیت نمی‌شناسند و گفت: «این حکومتی در ایران است که ده‌ها هزار نفر از شهروندان خود را کشته یا مجروح کرده است.»
او افزود جمهوری اسلامی اقتصاد غرب، منابع انرژی و آبراه‌های بین‌المللی را «خفه» می‌کند اما موج خشمی را که علیه اسرائیل وجود دارد، متوجه جمهوری اسلامی نمی‌بیند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/78607" target="_blank">📅 17:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78606">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyKpiI9OEUPpWoKFcopYGha3u0xEmiF5zORvI_c_boo6_AWkxa0-8adMHQjH1Fu5dtN1hH3B2Fs2Zh0JXoFqK5u8bI_RFNv50W42czN4JcQ38NsxkWVtFAlAo9lvhCMkt_LrJHnvtOhxoEtBKQDP6dsDx2LUtYibjAvFb9vI2UzZYqdr_l_pQGaCVwa9SvG6rndzq_VclO0u_XvhsMrykhiSFEMmKgqsN3GxiOBok3uFmRdX7ijRJYRSt8wCkeRO0hZXM4_w9sR6j6My20geV709epoFRp3s_Kq1zI-0ti-0Pkl-AlZHe5FL3BxHBpHqaTEKwUx4bD--wd3CeZcUow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی تیراندازی مقابل ساختمان دادگستری مهاباد در روز شنبه ۱۱ مهر، یک نفر کشته و چهار نفر زخمی شدند.
امیررضا رسولیان، فرمانده انتظامی مهاباد، اعلام کردە  این تیراندازی مقابل در دادگستری این شهرستان رخ داده و در جریان آن یک نفر کشتە  و چهار نفر زخمی شده‌اند.
یک منبع مطلع به ایران‌وایر گفت فرد مهاجم که چند سال پیش فرزندش را از دست داده اعضای خانواده فردی را که او مسئول قتل فرزندش می‌دانسته و در حال حاضر به عنوان متهم در زندان تحمل حبس می‌کند هدف تیراندازی قرار داده است.
به گفته این منبع، مهاجم پس از تیراندازی توسط مأموران انتظامی در محل بازداشت شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/78606" target="_blank">📅 17:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78605">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYVLC3l-OwbYVktEqimBmaUSR8U8QsFlCqmGFCEYa4f9lAKkFZPcFdL0za8uq9C7k_z72gx_uEZi7BUgxL1GrBjrZu1x7X9I-p_iIXgXuSLTQEA7_ub45Vix3AHcjLZuUmDL7op_2GsU-HDbTRF9GvHIx7sY4w_dbWYUKnGJ6rvMsc3EOzRHTikCsete3QYM95J-cd-wrfTsanpqz_SbHHPhV9jzRO-7WrE4Qhjq4_qdiMipummJGnJ2l2YEER8hPY39DZBglNl4An2f1WMACOg9nT_cOKOpTNUaxTW9DabvjNokFgwDnPgMKkvcsOoy-gaTdrw7y1XfeNF-VXfnZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت اطلاعات جمهوری اسلامی روز شنبه ۱۱ مهر از بازداشت ۳۱ نفر در شهرستان سیرجان در استان کرمان خبر داد و آنها را اعضای چهار «شبکه سازمان‌یافته خرابکاری خیابانی» معرفی کرد.
این وزارتخانه مدتی شد افراد بازداشت‌شده برای شرکت در «فراخوان‌های سراسری» سازماندهی شده و در حال تهیه کوکتل مولوتف و ابزار تخریب دوربین‌های شهری بوده‌اند.
وزارت اطلاعات همچنین این افراد را به دست داشتن در «آتش‌زدن فرمانداری، تخریب بانک‌ها و ساختمان‌های دولتی و حمله به مقر پلیس» در جریان رویدادهای دی‌ماه ۱۴۰۴ متهم کرد؛ رویدادهایی که در اطلاعیه این وزارتخانه از آنها با عنوان «کودتا» یاد شده است.
در این اطلاعیه جزئیاتی درباره هویت بازداشت‌شدگان یا مستندات مربوط به اتهام‌های مطرح‌شده ارائه نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/78605" target="_blank">📅 17:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78604">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MJTow-sT1ZJh3NX2mdb_1dlKW1-ikjC1vWcz7FIzf8U3kPP7fyPKX9M_O-VgfzG_B2OsH9PsepkPF0M06KhwPLuFsgGqzQvKFYSHRQSp8U74xLynSq2ZO0RmZrM_8UJtUJJUtngGLqV5aYMHueaVuOXvAiRqHXSLTNTmgsEvooFXU3Eg6U4DHZN-i7WBZcThsHokBoXOOTGZ759CNDE6zUiQXaZF5pzB-eMi8r6AxAiRmfVdlovFQDMRTG8CbBIbpbR0HIC6p5K2E_ObezEstm6dOZNWRR8u3UR6S1J3S7jVRJQXJDAyfIMKNpMpCmKhTc9gGeDki9-kyKbZV2jYUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام «سیاوش جمشیدی خیرآبادی»، از بازداشت‌شدگان اعتراضات سراسری دی۱۴۰۴، در بامداد شنبه ۱۱مهر۱۴۰۵ خبر داد.
قوه قضاییه همچنین ادعا کرده است که جمشیدی خیرآبادی شامگاه ۱۸ دی ۱۴۰۴ در خیابان ناصرخسرو شهرکرد به‌سوی ماموران تیراندازی کرده و سپس از محل گریخته است. براساس این روایت، او دو روز بعد، ۲۰ دی ۱۴۰۴، درحالی‌که یک قبضه سلاح کمری همراه داشت، بازداشت شد.
در اطلاعیه قوه قضاییه آمده است که حکم اعدام این معترض پس از تایید در دیوان عالی کشور اجرا شد. بااین‌حال، در این اطلاعیه توضیحی درباره زمان برگزاری دادگاه، روند دادرسی و دسترسی او به وکیل منتخب ارایه نشده است.
مقامات جمهوری اسلامی معترضان دی‌ماه ۱۴۰۴ را «کودتاگر» خوانده و آن‌ها را به ارتباط با آمریکا و اسراییل و تلاش برای ایجاد ناامنی متهم می‌کنند.
«مسعود پزشکیان»، رییس‌ دولت جمهوری اسلامی، نیز در سخنرانی اخیر خود در مجمع عمومی سازمان ملل مدعی شد که مردم ایران طی هفت ماه گذشته برای «دفاع از ایران» در خیابان‌ها حضور داشته‌اند.
او معترضان را افرادی توصیف کرد که به ادعای او، آمریکا و اسرائیل آن‌ها را «تهییج» و مسلح کرده بودند تا در داخل کشور ناامنی ایجاد کنند.
صدور و اجرای بسیاری از احکام سنگین علیه معترضان دی ماه از جمله احکام اعدام ذیل قوانین «تشدید مجازات جاسوسی» صورت می‌گیرد که از منظر حقوق‌دانان و فعالان حقوق بشر شامل موارد جدی‌ نقض حقوق متهم است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/78604" target="_blank">📅 17:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78603">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پیام‌های دریافتی از قشم
حدود ساعت ۱۶:۳۰:
صدای جنگنده خیلی نزدیک اومد صدا زیاد قشم
همین الان قشم موشک شلیک کردن
16:34 دقیقه
وحید جان از قشم سمت اسکله بهمن موشک شلیک کردن
صداش خیلی وحشتناک بود
معلوم نیست شلیک کردن یا جنگنده بود ولی هرچی بود صداش خیلی زیاد بوددددد
قشم همین الان یه صدایی شد
سلام وحید جان چند دقیقه پیش یک موشک به سمت تنگه شلیک شد.
سلام وحید
دور و ور ساعت ۴:۳۰ جنگنده رد شد
سلام ساعت چهارو نیم بعداز ظهر امروز قشم  صدای جنگنده امد خیلی وحشتناک بود
[این پیام متفاوت هم بود که نمی‌د.ونم چقدر درسته. بعد از یک ساعت معلوم نشد صدای چی بود.]
قشم پدافند بالا نریمان و زدن
وحید
خیلی شدید بود صدا ها
معلوم نبود چی بود
رادار تازه ۳ روز بود درست کرده بودن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/78603" target="_blank">📅 17:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78602">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/742b2ddd5c.mp4?token=I9nM5dnKz4us-arHxYS9cqARUszWwrfpvUihr59qmsu44paakyTd2uG57s02txTDDBXFL1XVYAIlpvew877nMWfKxm3oBwpRvLw-wmVW7peoUXujYpE1Q3MJg_P7xJ4Su2YBwOQixmIb0gMq0IoltqcebzH49QrAE5dE1-qXXaF2l1zYEIV5u0sLCMR0q26C2uoSmimG-NG-ysvrqFaNZADmiycIC5LcSPuJsYApfozdHALALYCQ7FjOvuaIWEl0cos4ln6mDiArjqO_ulTferb3dc5fLHacRqVg_K9wuys5eil0YNpmtz5g8RqPamU09fTSwpDT8r6gQRv5HVAeAA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/742b2ddd5c.mp4?token=I9nM5dnKz4us-arHxYS9cqARUszWwrfpvUihr59qmsu44paakyTd2uG57s02txTDDBXFL1XVYAIlpvew877nMWfKxm3oBwpRvLw-wmVW7peoUXujYpE1Q3MJg_P7xJ4Su2YBwOQixmIb0gMq0IoltqcebzH49QrAE5dE1-qXXaF2l1zYEIV5u0sLCMR0q26C2uoSmimG-NG-ysvrqFaNZADmiycIC5LcSPuJsYApfozdHALALYCQ7FjOvuaIWEl0cos4ln6mDiArjqO_ulTferb3dc5fLHacRqVg_K9wuys5eil0YNpmtz5g8RqPamU09fTSwpDT8r6gQRv5HVAeAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، روز جمعه، در سخنرانی خود در آلاباما با اشاره به ضربات نظامی به ایران و انتقاد از برخی رسانه‌ها گفت:  آنها نمی‌خواهند موفقیت ما را ببینند. وقتی نیروی دریایی‌شان را منهدم کردیم، نیروی هوایی‌شان را از بین بردیم و چند ماه پیش ضربه‌ای مهلک به ایران زدیم، نیویورک‌تایمز و رسانه‌های جعلی می‌‌گفتند اوضاع ایران فوق‌العاده است. آنها همه‌چیزشان را از دست داده‌اند، از جمله رهبرانشان را.
او با تاکید بر خلأ رهبری در جمهوری اسلامی افزود: آن‌ها یک دور از رهبرانشان را از دست دادند، بعد دور دیگری را، و سپس نیمی از دسته سوم را. حتی یک دور رقابت راه انداختند که ببینند چه کسی حاضر است رهبر شود، اما هیچ شرکت‌کننده‌ای نبود و همه می‌گفتند من نمی‌خواهم.
بخشی از مشکل ما اکنون این است که اصلا نمی‌دانم باید با چه کسی طرف شوم. هیچ‌کس حاضر نیست رهبر باشد.
می‌گویم در ایران با چه کسی باید حرف بزنم؟ اما هیچ‌کس آن اطراف نیست.
در می‌زنیم، تق‌تق، ولی کسی در خانه نیست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/78602" target="_blank">📅 05:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78600">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mdnH90u9SpoYcBlMxLIDrno2_JChfNL0mg1yUaNfU18K-nxuOxMBBlvYZrgHdcEUwr8NAjRU6uGJr4umMUq6YzrtjLPNf1OiEEm1xrwjHkA3q8qKHz_MpTSfkVWLt150BjfUmdKeBPJB8uNl22dUUW71l4UC11wts99JKmeEY8B0aBINOMNlplvURahUPC3ZcTO47qguEi7jN-j-FR2kL1pOYUZGLnGX9Uh_NLXvYc63Md229cMwfJECajB_j8IZyhiHjWFobnjLmS-Ut0af0HFMPftIEi3TUdOEPBnEv1GcoZNBsDDv2svLmGCIg5InwAfQ2LvrnTbbJbn64l09tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WA0PtOEedSUy_XtT-Fnprc_qch3yv29-YdH2rerjYUUSNBO3aeS2nkBl1bk6pDCdEFGiXTnFy0xasR2pt8CoQLvQvnWm9BhlObPGmguJZ1rysMNR-7lth3ftGGdzdX5TZE98ulCPiIeScu9IRI5BJsdWiHQv46bw1WD0FDDXVQlXpBHeGoqngT46YQdSpHDHIYadnFaAxx7Grq5QWBZhA6tzsVbnBgjXZ6RvZ_dfQc-YGnRWn3s2irBhtc-5wjiywdijnJ_QIimbPMgajLTEnHRJAwusSrbsm1iuQOd_1CnTxoKpG8k3dYcvHV5PbNQc6IWNLGAJeuRzHYw5szEfiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وکیل «الناز شاکردوست» اعلام کرد دادگاه تجدیدنظر استان تهران، حکم بدوی یک سال حبس تعزیری و دو سال محرومیت از فعالیت‌های سیاسی، مجازی و هنری علیه موکلش را تایید کرده است.
الناز شاکردوست، بازیگر سینما، به دلیل انتشار یک استوری مرتبط با اعتراضات دی ماه ۱۴۰۴ به دادگاه انقلاب احضار و به اتهام «فعالیت تبلیغی علیه نظام» به یک سال حبس تعزیزی و دوسال محرومیت از فعالیت‌های سیاسی، مجازی و هنری محکوم شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/78600" target="_blank">📅 18:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78599">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/84b4ce621c.mp4?token=uyB5we2QUIEjYIHSFhXXGhzT_eHTt_5mQvDDpExBNZrzihli08sr4Wfu8Wxxs4e4HMdkbFiiLVmSLSz1J8t6uCItXkicVg4t7MGuRbMyQWAgRBAWXdEhuGUfgAVlKklgsrz2HYqO3UJjxbLsXkrjoTgdTJAGMeW3CkURF1J6U90Th_UBCwlSnHru1EajtYtRdfcaEOxsgJBsdUUhnKawCqMaK_RYtrXOtfDU9oHOx1uHcDW1PAnMDXHNcsXcSBYcgOr5aFd7fqaGyoKAnYSY8GSN0ulcWd6U6ce9tsjLLNcQIDlc3G1z2IbW64qPicHSBz0DROtKQR65dS9_l0ta6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/84b4ce621c.mp4?token=uyB5we2QUIEjYIHSFhXXGhzT_eHTt_5mQvDDpExBNZrzihli08sr4Wfu8Wxxs4e4HMdkbFiiLVmSLSz1J8t6uCItXkicVg4t7MGuRbMyQWAgRBAWXdEhuGUfgAVlKklgsrz2HYqO3UJjxbLsXkrjoTgdTJAGMeW3CkURF1J6U90Th_UBCwlSnHru1EajtYtRdfcaEOxsgJBsdUUhnKawCqMaK_RYtrXOtfDU9oHOx1uHcDW1PAnMDXHNcsXcSBYcgOr5aFd7fqaGyoKAnYSY8GSN0ulcWd6U6ce9tsjLLNcQIDlc3G1z2IbW64qPicHSBz0DROtKQR65dS9_l0ta6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا، شامگاه پنجشنبه نهم مهر ماه، ویدیویی در شبکه اجتماعی تروث سوشال منتشر کرد که حضور گسترده معترضان در جریان اعتراضات سراسری
دی ماه
در ایران را نشان می‌دهد.
در این ویدیو، معترضان شعار می‌دهند: «امسال سال خونه، سیدعلی سرنگونه»
realDonaldTrump
این ویدیو رو ۳۱ دسامبر ۲۰۲۵ ده‌ها اکانت عربی و اکانت‌های مرتبط به یک سازمان سیاسی خارج از کشور منتشر کرده بودند و گویا بیشترین توجه رو هم در اکانت این مسئول اسرائیلی گرفته بود که بارها ویدیوهایی با شرح اشتباه هم منتشر کرده:
GadbanWaleed
اون روزها خودم هم کلی ویدیوی مهم از شهرهای مختلف ایران منتشر کرده بودم ولی به درستی تاریخ این یکی شک داشتم که مربوط به اعتراض‌های ۱۴۰۱ باشه و نگذاشته بودمش. به ویژه اینکه منبع اولیه‌اش اکانت‌هایی بودند که همیشه کلی ویدیوی قدیمی رو هم با شرح نادرست بین ویدیوهای روز منتشر می‌کنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/78599" target="_blank">📅 17:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78598">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحسین باستانی Hossein Bastani</strong></div>
<div class="tg-text">🔻
معمای «تیم شش‌نفره» در حکومت ایران
مسعود پزشکیان اخیرا به «تیمی شش‌نفره» در حکومت ایران اشاره کرد که در مورد بحران جاری با آمریکا «اختیار دارند تصمیم بگیرند و تصمیمات با هماهنگی آنها اجرا می‌شود». به دنبال انتشار این اظهارات در مصاحبه با سی‌بی‌اس، رسانه‌های رسمی ایران روایت‌هایی را از ترکیب تیم شش‌نفره منتشر کرده‌اند که عمدتا در مورد پنج نفر مشابه و در مورد نفر ششم متفاوت بوده‌اند. بخش ثابت روایت‌ها اغلب بر رئیس‌جمهور، رئیس مجلس، دبیر شورای عالی امنیت ملی، رئیس ستاد کل نیروهای مسلح و فرمانده کل سپاه تمرکز داشته، هرچند نفر ششم را برخی رئیس قوه قضاییه و برخی وزیر خارجه دانسته‌اند.
اشاره مسعود پزشکیان به وجود این تیم، البته اهمیت داشت، ولی این اشاره نه اولین بار بود که صورت می‌گرفت و نه نشانه تحولی کلیدی در ساختار تصمیم‌گیری کلان، یا مثلا ایجاد نهادی با اهمیتی مشابه شورای عالی امنیت ملی بود.
در تیرماه گذشته، عباس عراقچی در مصاحبه‌ای با برنامه یوتیوبی «ماجرای جنگ» گفته بود چارچوب مذاکرات با آمریکا در شورایی تعیین می‌شود که به «کمیته شش‌نفره» معروف است. توضیحات او اما نشان می‌داد که جایگاه این کمیته پایین‌تر از شعام ـ شورای عالی امنیت ملی ـ و در حد یکی از کارگروه‌های داخلی آن است. عباس عراقچی در گفتگوی خود، مشخصا از کمیته‌ای «در داخل دبیرخانه» شعام سخن گفت که ابتدا «کمیته هسته‌ای» و سپس «کمیته مذاکره» نام گرفته و در نهایت به «کمیته شش‌نفره» معروف شده است. مطابق اظهارات او، این کمیته از مدت‌ها قبل از جنگ چهل‌روزه فعال بوده و در زمان‌های دبیری علی شمخانی و سپس علی لاریجانی در شعام، به‌ترتیب تحت مسئولیت این دو نفر فعالیت می‌کرده است.
البته روایت عباس عراقچی از قرار داشتن این کمیته زیر مسئولیت دبیر شورا، این ابهام را ایجاد می‌کرد که آیا ریاست آن، مانند شعام، با رئیس‌جمهور است یا اینکه سخن از جمعی شش‌نفره است که رئیس‌جمهور را شامل نمی‌شود، ولی جمع‌بندی‌های خود را به رئیس دولت ارائه می‌کند.
در هر صورت، عباس عراقچی تاکید داشت که تصمیم‌های کمیته باید «عینا مانند مصوبات شورای عالی می‌رفت، تایید می‌شد و بعد ابلاغ می‌شد»، که اشاره‌ای به لزوم تایید مصوبات از سوی رهبر جمهوری اسلامی به نظر می‌رسید. او همچنین، به این سوال که آیا تصویب آتش‌بس (موقت) در پایان جنگ چهل‌روزه «با نظر آقا مجتبی» بود یا نه، پاسخ مثبت داد، هرچند در مورد شیوه تصویب گفت: «ارتباط ما با کسانی بود که رابط بودند و مسائل از آن طریق منتقل شد.»
قابل تامل است که مسعود پزشکیان، که در مرداد ماه از دو نوبت دیدار با رهبر جدید جمهوری اسلامی خبر داده بود، در مصاحبه‌هایش در سفر آمریکا هم به همان دو مرتبه ملاقات خود با رهبر اشاره کرد، که نشان می‌داد دیدار جدیدی با مقام اول حکومت نداشته است.
به عبارت دیگر، با گذشت هفت ماه از رهبری مجتبی خامنه‌ای، ارتباط تیم‌های حکومتی با رهبر کماکان به حلقه «رابط» اتکا دارد که، در مورد آن حدس‌های متنوعی مطرح شده است. از جمله، گمانه‌زنی‌هایی که حسین طائب رئیس جدید سازمان بسیج را از افراد موثر این حلقه می‌دانند.
🔹
ادامه  مقاله در لینک زیر در دسترس است:
https://www.bbc.com/persian/articles/cr9dw7dvjxj1o
@HosseinBastaniChannel</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78598" target="_blank">📅 16:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78597">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTkoKNx5LQfpS0I6KYk29vYGRbmWmSq2gMii1lqSmciHHB64xUhANoBQWxDH0TqsFhHpgIr9y53arbmZ11Gy73rX5mULaEn8m6i3HrI4ZUaNcLVvP0dGbVrJtbHgcVgKww6zzrp22tPwogHRqW-9NsrJwdnFSTLLneWiBPhFSKPkqqqqznTEukpl2Bqw3-KpT1cvl-92xxupD0CdtTEXQn9GotSXhwjJFD0HUINdPJfPomdFMRhlnNjEzqqdf6G9Ek0FBakjpV5DQi3ZWqsKov9kOaxNkIs7eHaHiamuulmlnC1dlAGM4n7KCny48BH9DhU9LoI8BL408NG5kFrFvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه‌داری آمریکا می‌گوید ایران در ماه سپتامبر حتی یک محمولهٔ نفت خام هم بارگیری نکرده است. داده‌های شرکت‌های ردیابی نفتکش‌ها نیز نشان می‌دهد در این ماه هیچ بارگیری نفت خامی از بنادر ایران ثبت نشده است.
اسکات بسنت شامگاه پنج‌شنبه، نهم مهر، در شبکهٔ اجتماعی ایکس نوشت: «ایران در ماه سپتامبر صفر بشکه نفت خام روی نفتکش‌ها بارگیری کرد» و افزود دولت دونالد ترامپ در حال قطع «حیاتی‌ترین منبع درآمدی» جمهوری اسلامی است.
داده‌های اولیهٔ ردیابی نفتکش‌ها که بلومبرگ منتشر کرده و همچنین اطلاعات شرکت‌های کپلر و ورتکسا نشان می‌دهد در سراسر ماه سپتامبر هیچ بارگیری نفت خامی از بنادر ایران ثبت نشده است.
این در حالی است که برآورد کپلر و ورتکسا از بارگیری نفت خام و میعانات ایران در ماه اوت حدود ۲۲۰ تا ۲۵۵ هزار بشکه در روز بود.
ایران همچنان مقداری نفت را که پیشتر بارگیری و در آب‌های آسیا ذخیره شده بود به خریداران چینی تحویل می‌دهد، اما این ذخایر بدون خروج محموله‌های تازه از ایران رو به کاهش است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/78597" target="_blank">📅 16:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78596">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-3fqrOuFEO6rOCqL7dKjlmUeujsukJ3RazypuxsX4P-UIVRRfQn9UfbXKnETFDqIjQHYNxYzVVqkEZhEOrczvzV_nHruZM2pZ1eVsWcIGTAByDSQDOWdYboBw283Hu2nWm64aTKeSG3KWfnLZCDlJlZc9JXB61eXAnKC-hL-SHut-SF6jy8AFVZnk6Ld6ZuBkXEAGj79_X8x_9NyO3IBjIvEh72bBM_OS6R9Kc8Kl9Tvd2hT__h-UTqfqPHThVyoDPUeI8vtMyvoPPlD_fOyBQfLlYWY27KSBJ4LjGypKBB0ZSV83mgcbALDHtn8z19nf5-ccVlJCKOsqAiN2qIqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، روز جمعه دهم مهر ماه، از وقوع درگیری مسلحانه میان سپاه پاسداران و اعضای «یک گروه تروریستی» در یکی از روستاهای شهرستان راسک در جنوب سیستان و بلوچستان خبر داد.
تسنیم با اعلام این خبر افزود نیروهای سپاه «در حال پاکسازی منطقه و بررسی وضعیت» هستند.
همزمان خبرگزاری حکومتی فارس نیز از آغاز «اقدام عملیاتی» سپاه پاسداران از صبح جمعه در راسک خبر داده است.
این خبر در حالی منتشر می‌شود که روز پنجشنبه نیز قرارگاه قدس نیروی زمینی سپاه با انتشار ویدیویی از یک درگیری مسلحانه، از کشته شدن ۶ عضو یک «گروهک تروریستی تکفیری» در منطقه منزل‌آب زاهدان خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/78596" target="_blank">📅 16:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78595">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYDDSjcIoBDJDZqeMY9z4DpAY5uHgtfNXqlAlg1znd1kRFOWcN-4BIEldUzmZSf50MUvMfgF1nO8-P7PDuXFsYFG7FO1P011Bzn6C0wNooBH8-JZfran_hkBPuIsXJQPQBOM0BmJLY2XS1oLnBcL-b6qL4UDzbDWug4borFH0NWLwVQ5Q2bBzyztrvJjyePyncvLVCYIIrRVLDfqqAHQVQ_qI_oWQTOIfJ-r35ZIaQr2agzdhqFcrhfUY2cg8tkOL3SXwhoKmJ9mIhbyJgu7Ww9gSXn2wE_JfF61lAzdkociheyuyDklXOAsU15iO1GR3hvDakrlVD4tX4I-3VX7xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در دو اظهارنظر تازه دربارهٔ ایران هشدار داد اگر مشخص شود تهران در حادثهٔ پرواز فلای‌دبی به مقصد اسرائیل دست داشته، «به‌شدت هدف قرار خواهد گرفت» و ساعاتی بعد بار دیگر گفت به اعتقاد او ایران «در آستانهٔ تسلیم‌شدن» است.
این اظهارات همزمان با ادامهٔ تحقیقات امارات متحده عربی دربارهٔ احتمال تروریستی بودن حادثهٔ پرواز فلای‌دبی و گزارش‌ها دربارهٔ تقویت حضور نظامی آمریکا در منطقه مطرح شده است.
رئیس‌جمهور آمریکا شامگاه پنج‌شنبه، نهم مهر، به وقت ایران، در پاسخ به پرسش خبرنگاران در کاخ سفید دربارهٔ احتمال ارتباط ایران با کمک‌خلبانی که به خلبان پرواز دبی به تل‌آویو حمله کرد، گفت: «بر اساس آن‌چه می‌شنوم، می‌گویم پاسخ مثبت است، اما همین حالا در حال بررسی آن هستیم.»
تاکنون هیچ مدرک علنی دربارهٔ ارتباط ایران با این حادثه منتشر نشده و تحقیقات دربارهٔ انگیزهٔ کمک‌خلبان ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/78595" target="_blank">📅 16:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78594">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBI_cHyr9yBqclXdpKTHi_W2aCTTpZq5lpzkLDplHMUjQec_3rPbOV3HYELZsl7QTS7ayRzpX4hzFJ9gd0KrdI5m9zx_E7Ip6Xs15BkeYJ3WHRQkTz5So7vhiURr7rmqTaRaVKamTqDKbcqQZk8IPnV10x9yRr_kamGyJvXAB5dhrOZIFDJVX1-Q-2UA6QKwK-XaNyUSAVdYOJ8nKe3_vmRy4RstN2oimtNRZnU6mng5HqHW8dV1y0jynB4nYTAQgIaqwc2Dls_pSpa8w7kYoHtogKyZQZLzx4UngoWbBR6NI1NMbReYqpIdC-y5n_1oK0RUAPpD_hTS_UA5mKHa8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه شهروند اهل کرمانشاه، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در شعبه ۲۳ دادگاه انقلاب تهران به اتهام «محاربه» به اعدام محکوم شده‌اند.
بر اساس اطلاعاتی که به سازمان حقوق بشر هانا رسیده، سیروان شعبانی، ۲۵ ساله، هنرمند و نوازنده و سرپرست یک ارکستر پاپ و سنتی، خسرو محمدی‌نیا و مسعود توشمالانی هم‌اکنون در زندان قزلحصار کرج نگهداری می‌شوند.
هانا گزارش داده است که این سه نفر روز ۱۹ دی ۱۴۰۴، هم‌زمان با اعتراضات در اسلامشهر، از سوی نیروهای امنیتی بازداشت شدند و پس از آن مدتی در سلول انفرادی نگهداری شدند. بر اساس این گزارش، آنها پس از ماه‌ها نگهداری در شرایط انفرادی و آنچه هانا «اخذ اعترافات اجباری» خوانده، به زندان قزلحصار منتقل شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/78594" target="_blank">📅 16:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78593">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hDLi3V5iM2mTSwkMP5O9j-mkHMpNuCMMTbxQ6YZpS-P6nBjVtVJGqJIcRzZ0CI4JLKFIVy_8O0sgRuqfTgk31OrPBPLTC6g9FPAIb3n5dXIrvK3akN9pd-Z_IEwSwGzMk0PgKTZPM1n-_HX6HqTWpwuPijiRq6aTyilV1qRjQU-VuigkYXDEbhS3uMTKb1INRsW42pKmqow1zuMG1jngJj2zX7Z8Q6-1S3wsbAE4EOfXA9gRPYUEJAjct9GXRI4X2-w9X2VlUSbFjDvtd1VMV7PTkwCI3aXt1QTfXODayfVupJMKssVC1z4OIrrVC8KSEp6Rk11lgJjlGChBlSFuCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
«عملیات تجارت دریایی بریتانیا» (UKMTO) گزارشی از یک منبع ثالث دریافت کرده است مبنی بر اینکه یک نفتکش هنگام عبور از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته و در پی آن آتش‌سوزی رخ داده است.
گزارش شده که خدمه در سلامت هستند. میزان خسارت و تأثیرات زیست‌محیطی در زمان انتشار این گزارش مشخص نیست.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/78593" target="_blank">📅 23:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78592">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W-naMxPBDLQJSsej3AlKBDfNGlZlR7zpCEtY9OOylKdBKVHfCLN0Xc6pkHH-blbn7D8cZ_lJ0XxpXKWzWLS6gXRQDkTeGRgqWCZdZXoY9bnZ-5oIgS6ay5xK-x6hnuxEMhdyxKUbgbyc13BUNZwMnwyLNzQhG7aUsn17ZeNQiK8n31vuV5LsB7H7FSS7QVjVYFVdknMlJfFWLYDV8hnNnSLT2edmVYaoESbHjKAr_IkWtyPfosVhtmBSlGSheos-j9_Fjbac2vqF8_LczlTjxBqxXZLziT1OjQzGEXgP-bCPg9nzpbpWvoBXLX2Illf3BFMOpSjNmAwv0cHQgSo9bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
من بارها گفته بودم که برای از بین بردن «تهدید هسته‌ای ایران» ۴ تا ۶ هفته زمان لازم است، اما من این کار را در یک شب انجام دادم! باقی آن زمان فقط برای این است که مطمئن شویم اوضاع همین‌طور باقی می‌ماند.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78592" target="_blank">📅 21:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78591">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QN_MIWwNip-IRcm2ZQYUObm6YeZau6SkQOxzcyMy0AGfoW4lP2vR4o8PhCmOYul2bJbUR4hyZn9XCjn84HiKaCJjXqFqVaMAKGvn6biNA1BNmIdlo2diIihRdYWC1G_dfJhK0d2X7bOooR4kyH5cWiGDsJ-fHBDyE2k5yraxdXluSjDBQ2VpK6XP_P1HdTNHxknu7QZa4Bimo-nmcIRpZvKSsWtOVkUgu7BaIxb62DrJirU53BO9VfnVz6sLuoqSeFg-AJ6CmK5jWysSTmjdWU4FjFWbPsLMYOninoxiIt6yT2NpqvgeF_tK89eCi6dvSsDzdewHOxkiUi03ffLIeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس جمهوری آمریکا، در مصاحبه‌ای مفصل با مجله تایم گفت پیشنهاد اخیر جمهوری اسلامی برای پایان دادن به درگیری‌ها و بازگشایی تنگه هرمز را به دلیل «ناکافی» بودن آن رد کرده است، و افزود احتمال تشدید حملات نظامی آمریکا علیه جمهوری اسلامی را منتفی نمی‌داند. این مصاحبه ۶ مهر در کاخ سفید انجام و روز پنجشنبه ۹ مهر منتشر شد.
دونالد ترامپ در پاسخ به این پرسش که چرا درگیری نظامی با جمهوری اسلامی بر خلاف برآورد اولیه او وارد هفتمین ماه شده است، گفت پس از حمله بمب‌افکن‌های بی-۲ به تاسیسات هسته‌ای می‌توانست عملیات را متوقف کند، اما تصمیم گرفت «فراتر» برود تا حکومت ایران نتواند توانایی‌های خود را «به شکلی متفاوت» بازسازی کند.
او گفت: «توانایی هسته‌ای آنها را نابود کرده‌ام. نیروی دریایی‌شان را نابود کرده‌ام؛ ۱۵۹ کشتی در کف دریا هستند. نیروی هوایی‌شان را نابود کرده‌ام. همه هواپیماهایشان از بین رفته‌اند. رادارشان را نابود کرده‌ام.» رئیس جمهوری آمریکا همچنین گفت اقتصاد جمهوری اسلامی از بین رفته و تورم آن حدود ۳۰۰ درصد است.
ترامپ گفت آمریکا عملا کنترل تنگه هرمز را از جمهوری اسلامی گرفته است، و تاکید کرد شب پیش از مصاحبه حجم عبور نفت از این آبراه به بالاترین میزان تاریخی رسیده بود. داده‌های جدید نشان می‌دهد صادرات نفت خلیج فارس در روزهای اخیر به‌ شدت بهبود یافته و به سطوح متوسط سال ۲۰۲۵ بازگشته است.
در بخش دیگری از مصاحبه، خبرنگار تایم به اظهارات اخیر ترامپ درباره احتمال «نابودی ایران» اشاره کرد و پرسید آیا چنین اقدامی واقعا ممکن است. او پاسخ داد: «بله، این کار را خواهم کرد. ممکن است.»
هنگامی که خبرنگار درباره مردم غیرنظامی ایران پرسید، رئیس جمهوری به سرکوب اعتراضات اشاره کرد و گفت حکومت ایران طی ماه‌های اخیر بین ۷۲ هزار تا ۷۵ هزار نفر را کشته است.
ترامپ همچنین گفت از تصمیم خود برای مداخله نکردن مستقیم در جریان اعتراضات دی‌ماه پشیمان نیست، و عملکرد دولتش در قبال جمهوری اسلامی را «باورنکردنی» توصیف کرد.
او گفت ایران کشوری بسیار بزرگ‌تر و دورتر از ونزوئلا است، اما «نتیجه همان خواهد بود» و افزود: «آنها می‌خواهند توافق کنند.»
در پاسخ به پرسشی درباره علت رد پیشنهاد اخیر جمهوری اسلامی برای آتش‌بس، ترامپ گفت رژیم ایران پیشنهاد بازگشایی تنگه هرمز را مطرح کرد، اما شرایط آن «حتی نزدیک به کافی هم نبود.»
رویترز گزارش داده است پیشنهاد ارائه‌شده از طریق میانجی‌های قطری شامل پایان درگیری‌ها و بازگشایی تنگه هرمز در برابر رفع برخی فشارهای اقتصادی آمریکا و دسترسی رژیم ایران به دارایی‌های مسدودشده بود. مذاکرات غیرمستقیم همچنان ادامه دارد.
خبرنگار تایم سپس پرسید آیا دولت آمریکا پس از انتخابات میان‌دوره‌ای حملات به جمهوری اسلامی را افزایش خواهد داد. ترامپ پاسخ داد: «ممکن است.»
او از ارائه جزئیات خودداری کرد، اما گفت آمریکا طی شش ماه گذشته ذخایر تسلیحاتی خود را افزایش داده و شرکت‌های دفاعی با فعالیت شبانه‌روزی در حال گسترش تولید هستند.
رئیس جمهوری آمریکا در پایان مصاحبه هدف اصلی سیاست خود در قبال جمهوری اسلامی را جلوگیری از دستیابی آن به سلاح هسته‌ای دانست و گفت: «موضوع اصلی که همیشه مطرح می‌کنم این است که ایران نمی‌تواند یک قدرت هسته‌ای باشد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78591" target="_blank">📅 17:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78590">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahRGeTszTUqcJXXe6jb21b0xlNaCu2sbnMS9B_53qVfJFdusG2ggnBhoi2AoSaINTldWEVfVtVvbRYubIJAFmPRT99Mj9wKVQzZFsvZzJvvYtt_rE-1XX823Qfp7eJcBU2HxV3CZesxl_aJ1c8kQeWLB_vfBCTBS4Nv5R4F_U8jMl4nnl3qXF3lWBWgPESQLT7h5k7y_kOf4YuEBHqnoMu0HPZFg1nXlyqvQ-gEksH5co9AnievfJl4lPRiKPYRry5h0t7pCe58F8I3N2dZZJRs2AW3aeAQPuV2wbWvODynFJSq5N0ALyZqi2T-T_d9fvhQMEG2RBaXrpV3er3VzuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد ایران روز پنج‌شنبه با افزایشی حدود ۱.۵ درصدی نسبت به روز گذشته به ۲۵۸ هزار و ۹۰۰ تومان اوج گرفت.
دلار آمریکا در مقابل ریال ایران طی یک هفته گذشته بیش از ۱۰ درصد، طی یک ماه گذشته بیش از ۲۰ درصد و از زمان آغاز جنگ حدود ۶۴ درصد جهش داشته است.
در بازه یک‌ساله نیز نرخ برابری دلار در مقابل ریال ایران تقریبا ۱۲۵ درصد رشد داشته است.
قیمت سکه امامی نیز در لحظه تنظیم این گزارش در بعد از ظهر پنج‌شنبه از ۲۶۰ میلیون تومان فراتر رفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78590" target="_blank">📅 17:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78589">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JwDS3KlLUPGjIbzsTnuRegpdNkWUEnWiF5EYtYYecjcZj2JkVwKf0XpZ7eykZxkkzwT2eTr3Fl2GH8TsycrkHR-M7ERkLhASqm03-MhoeMfLzlAQ4XIWMJEUgvnDrmhTKukYmz60oBe9Ax_cjBRH8Et3D6LhxTeQs3OycmiM7Qn7v7x-trwa6UrACzULo7KBJVmoE43i13j8bq_7mEQt-4OiwhFwYY9_hrrFhf7Z8bv-8Kjp53cVVcThOaHGHsU3xBU7uisTlTiFf1FCTL6KHU4ZPI-35wEkRrBnIxS7h_Us-FAQS-VqVE8-TqVTeCvHmgvIuqurBNEERQfX9_M4EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«فرزانه فصیحی»، دونده المپیکی ایران، در واکنش به اظهارات تازه «احسان حدادی»، رییس فدراسیون دوومیدانی جمهوری اسلامی، او را «بدنام‌ترین ورزشکار تاریخ ایران» خواند و نوشت که ورزشکاران جوان باید او را «عبرت» قرار دهند، نه الگو.
فرزانه فصیحی در متنی که در صفحه اینستاگرام خود منتشر کرد، خطاب به احسان حدادی نوشت: «در جهان موازی تو باید پشت میله‌های زندان می‌بودی و از هیچ حق شهروندی برخوردار نمی‌شدی، ولی چه کنیم که اینجا سرنوشت صدها و هزاران جوان پاک و معصوم رو هم سپردن دستت و حالا فاز نصیحت برداشتی.»
این واکنش پس از آن منتشر شد که احسان حدادی، چهارشنبه ۸مهر۱۴۰۵، در گفت‌وگو با وب‌سایت حکومتی «ورزش سه»، درباره ورزشکاران زن گفته بود: «با زنان دونده جلسه می‌گذارم و به آن‌ها می‌گویم تو می‌توانی مثل خیلی از ورزشکاران زن، مجازی شوی با ۳۰ هزار، ۵۰ هزار، ۳۰۰ هزار فالوئر، یا می‌توانی قهرمان شوی.»
فرزانه فصیحی همچنین با اشاره به «ریحانه مبینی»، «زهرا زارعی» و «فاطمه محیطی‌زاده»، از ورزشکاران زن دوومیدانی ایران، نوشت تصور این‌که آنها بخواهند از آموزش‌های احسان حدادی پیروی کنند، برای او «مثل کابوس» است.
او در ادامه خطاب به رییس فدراسیون دوومیدانی نوشته است: «شریف بودن ربطی به مدال و قهرمانی نداره. تو ثابت کردی با خورجینی از مدال هم می‌شه به قهقرا رفت و منفور یک ملت شد.»
اشاره فرزانه فصیحی به «پشت میله‌های زندان»، به پرونده قضایی احسان حدادی در دهه ۱۳۹۰ بازمی‌گردد. در آن پرونده اتهام تعرض و تجاوز جنسی علیه احسان حدادی مطرح شده بود و دادگاه نیز رای به زندان، تحمل شلاق و جزای نقدی داد. با این حال پرونده با دخالت نهادهای امنیتی مختومه شد.
در سال‌های اخیر برخی از زنان شاخص دوومیدانی ایران نیز کشور را ترک کرده‌اند. «الناز کمپانی»، رکورددار دوی ۶۰ متر با مانع ایران، از مهاجرت خود به آمریکا خبر داد و پیش از او «مریم طوسی»، رکورددار دوی ۲۰۰ متر داخل سالن زنان ایران، به آمریکا مهاجرت کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78589" target="_blank">📅 17:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78588">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zf0c_Xn5B-I9LmkA0OUX6sWvkk0yQ0Z8m1QV4hlti1tBLCkVfg73GPYssp5RIqmay-Txq-Ol6l3QmqXumlDHv4YGoYhssGR78sXEvjEuTfkUbKmF87cZq4yPkaUNxts9LcJHvtNqfuVto5pDvlSak3jK_pYhZjdC_D2UYHQpTuDXhNEhPyQkz1-0XWVfx9InufKMLtUUdBVEkj_tx9ogEEGJJ3qditpgEKoFGUQpWZjJ3H_jiqE9SFXlKws0QtsLWCM6QKiZOEbyphFE716ZGYaTEDVcVM_pHdql-to8sIOWM3MEfhguqkBaACfe_VEA0ZIwFT7nROVrw4pf6odGyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایمان صادقی، بلاگر ۲۰ ساله و از بازداشت‌شدگان [اعتراضات دی ماه] در کاشان، به بیش از ۱۳ سال حبس تعزیری محکوم شده است.
او بابت اتهام «تبلیغ علیه نظام» به هفت ماه و ۱۶ روز حبس و بابت اتهام «انتشار محتوای مجرمانه برخلاف امنیت کشور» به ۱۲ سال و شش ماه و یک روز حبس تعزیری محکوم شده است.
«انتشار محتوای مجرمانه در رسانه‌ها و مطبوعات منتهی به هتک حرمت اشخاص» نیز از دیگر اتهام‌های مطرح‌شده در پرونده اوست.
ایمان صادقی ۱۱ بهمن‌ماه ۱۴۰۴ بازداشت و پس از آن به زندان کاشان منتقل شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78588" target="_blank">📅 17:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78587">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZnmEzrfH_R_g7_Jd7nyOBEI1WS65JBKGjq4lTmLkGLp0arby1VoviE3thZSV6KQ3Jd9y0-NAXPbRnSGok3pXEFHWs4mXxk6zTgil1_gjBgjQHqUK-N6cpWfeqjmC3PJTRfsKad0DtyFG2VdNbsPbNj772wPwK16seNhnOsr91YEGg-w7IcsmNsCoep77wXWU64Cr657bu7IocLdE3AsJiS7hR5-smMaCLUZO0gGrQ-XYjAOlnNu_KxnN7Pr_cjBHK9kqyyNuDo8ZX0W2_D5bkvEDNgzkq9INBw5BPDTmvQ3Mrp3zTNplwfGsp7rowZHZLY7wblPW7MwqfMSmCdSX7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، چهارشنبه شب، گزارش نیویورک‌پست از اظهارات اسکات بسنت، وزیر خزانه‌داری آمریکا را منتشر کرد که گفته است اقتصاد جمهوری اسلامی ایران، «ظرف دو هفته» هیچ‌چیزی برای تجارت نخواهد داشت.
محاصره دریایی بنادر ایران مانع آن شده است که جمهوری اسلامی از طریق دریا بتواند نفتی صادر کند. دلار آمریکا نیز در روزهای اخیر با سقوط خیره کننده ریال جمهوری اسلامی، رکوردهای تازه‌ای زده است.
آقای بسنت به فاکس‌نیوز گفت اقتصاد تحت محاصره جمهوری اسلامی ایران به‌زودی و پس از تحویل آخرین محموله‌های نفتی خود، در حدود دو هفته دیگر «چیزی برای مبادله» نخواهد داشت.
به نوشته نیویورک پست، بسنت در مصاحبه با فاکس‌نیوز ارزیابی کرد که جمهوری اسلامی به دلیل فروپاشی اقتصاد خود که با اجرای «عملیات طرد اقتصادی» شتاب گرفته، از روی درماندگی به‌شدت مشتاق توافق است و هشدار داد که مشکلات آن طی دو هفته آینده به شکل چشمگیری وخیم‌تر خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/78587" target="_blank">📅 06:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78586">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdUSeGi845DNES-a3bj8uliz-QQzxcB5zVxEUVJni9kj7xWTb_j-D_i7SVMe5GXmOylheilzLLo_R_WVGbLUx41ueNMeMQvVOBn5IX3WzC0WKEyLoMQJPtkUsmAFfj6xvFutqPaAThu6BxEXZXTRA_UCPoKOz_5nJDOisMcOFVY5ZKleXRzD6AEwr5SYFMf57bTi_rRFoM934qKp0oBkozvp69D-wH3YoRyzZ7FyzxoHsTaGDITWmCwFxoYt4jh61d98rmmu0VX_g58BYuxmQ6nD2HiJdYznsM74J2EjdysX3wDyVFTfHHF7oQlWgMVwF8UjPMVe5nYKQwMvJ3vP8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش آکسیوس به نقل از یک مقام آگاه، مارکو روبیو، وزیر امور خارجه ایالات متحده، روز دوشنبه ششم مهر پس از به بن‌بست رسیدن مذاکرات با جمهوری اسلامی ایران، دستور داد هیات ایرانی حاضر در مجمع عمومی سازمان ملل، از جمله عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، فورا آمریکا را ترک کند.
یکی از مقام‌های آمریکایی به آکسیوس گفت: «روبیو هیات ایرانی را که بیش از حد مهمان مانده بود، بیرون کرد. مجمع عمومی سازمان ملل تمام شده بود و وقت آن بود که بروند.» بر اساس این گزارش، نمایندگی آمریکا در سازمان ملل دوشنبه شب به نمایندگی جمهوری اسلامی ایران اطلاع داد که هیات ایرانی باید فورا نیویورک را ترک کند.
آکسیوس نوشت عراقچی و اعضای هیات چند ساعت بعد راهی فرودگاه شدند و بامداد سه‌شنبه با پروازی از نیویورک به دوحه رفتند. منبع دوم نیز درخواست آمریکا برای خروج هیات را تایید کرد، اما گفت عراقچی از پیش قرار بود دوشنبه‌شب برای بازگشت به تهران حرکت کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78586" target="_blank">📅 06:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78585">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DtA1nuAzc17AW3fZf1jHMPpvplw3CDMfyq7JB5XRtC3TkI4R_WMWqpt-GrFljLnddRb1SETExTBxY5UOw8SSBeGnTHYZOqsV4hFn0oowG9mPPFnBoEWrCRRQACCvQiIV_G7a7SJVqRVp9ytQ-Ua2Ti1dYu6Dwd-B4IVTWGPmsd7hKN4th98_Izs6GWRq0sylTf38juu3G0JlWWFtC2_B_2yEomJA0mbMkY1ZOCv37YCWZSJbO3GXCMLUJTZs16z5BADJzmpD3o6fydCwmmUAGpQ1w59SdDs8bsd6L3hvGIuA99FhiSq7iPt-z2VnICeMZ2OZR7ZSX-DM4UVAAw_5vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، در پاسخ به سوال خبرنگاری که از او پرسید اگر رهبران جمهوری اسلامی به گفته او «دیوانه» و «غیرمنطقی» هستند، چگونه می‌خواهید با این افراد توافق کنید؟ رئیس‌جمهوری آمریکا پاسخ داد: «شاید آن‌ها را منفجر کنیم. باید تصمیم بگیریم. منفجرشان کنیم، توافق کنیم، وقتش دارد می‌رسد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78585" target="_blank">📅 00:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78584">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7e8aa88a9b.mp4?token=gI2g9cSqJkHQGpFJfWY_e025u_QRo4lRQfV_XmPTqCHXn3wQeYTvvYsUcwlTMwh5vL_nPB7UQBUz76t2AY3YFi2w5pBMxTLb6OBOYwAQqJRJRkgm4SUn7TSbea_-TrNuE9BQBqK7B91IxTOprVQiqkxl-_k_meIvUGSjVwKi2tFF0VuO5-S_NEidGMIwDOdnPTy6GUl0CrOoDnQulU8NHMDb8wLpChcLUqBVpTiVCAG4HummnmRgDr6lq43RcAxnw34-wQS-TKoGuXS9XhdmIVb7ukNuMHYSBP-BSclpQT1gnP_esVv7sBXjNjVy0sfzkYxp5yvUrAEhI0edau3Saw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7e8aa88a9b.mp4?token=gI2g9cSqJkHQGpFJfWY_e025u_QRo4lRQfV_XmPTqCHXn3wQeYTvvYsUcwlTMwh5vL_nPB7UQBUz76t2AY3YFi2w5pBMxTLb6OBOYwAQqJRJRkgm4SUn7TSbea_-TrNuE9BQBqK7B91IxTOprVQiqkxl-_k_meIvUGSjVwKi2tFF0VuO5-S_NEidGMIwDOdnPTy6GUl0CrOoDnQulU8NHMDb8wLpChcLUqBVpTiVCAG4HummnmRgDr6lq43RcAxnw34-wQS-TKoGuXS9XhdmIVb7ukNuMHYSBP-BSclpQT1gnP_esVv7sBXjNjVy0sfzkYxp5yvUrAEhI0edau3Saw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در تازه‌ترین اظهارات خود درباره ایران گفت تحولات جدیدی «بسیار زود» رخ خواهد داد.
ترامپ گفت: «خیلی زود» خواهید دید که اتفاقاتی رخ خواهد داد. او در ادامه گفت ایران «عملا ویران شده» و با تورم بیش از ۳۰۰ درصدی و وضعیت نامناسب اقتصادی روبه‌رو است. رئیس‌جمهوری آمریکا همچنین بار دیگر گفت که در جریان جنگ، نیروی دریایی و نیروی هوایی ایران از بین رفته و تجهیزات پدافند هوایی این کشور نیز نابود شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78584" target="_blank">📅 22:48 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78583">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlHM6EGxh7v4bt1ZQpftR3UuiwxoHc1RU_2WdX1sZa7Sn4iJwk-MHv6lnDZQP4ydZvmEwwljthcfZrQfIrdoishCEFi4O_MG9GZIg1NI0rJUi2hL7wXBTNyCMY9l69LkrAgglADU5saML6Et3Lx7r7v0MpykON38fXnf4y8IX5kr3si_0HyrTdl6ZjKuq5w_8kZH9IlAZkRFK3KdHGbTd12Y0aFYjrs6SDWZOw1rnvfX1PyCJI7RgqAj3eczaMw0KjuO59bWaC6aI0jRzpPDNCF06DI0Xew8AdhsPmcN0fU7m2q-X6Y2EdNJ0YycY43D_DVDlM6ELbQ73sBCuN2Xyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندی برنهام، نخست‌وزیر بریتانیا، روز چهارشنبه هشتم مهر، اعلام کرد که قرائن و شواهد قوی نشان می‌دهد جمهوری اسلامی ایران در حادثه امنیتی اخیر در نزدیکی پایگاه هوایی «فیرفورد» (RAF Fairford) تحت مدیریت آمریکا نقش داشته است.
پلیس ضدتروریسم بریتانیا روز یکشنبه پنج جوان ۲۳ تا ۲۵ ساله — که همگی اتباع بریتانیا و ساکن لندن هستند — را به اتهام آماده‌سازی برای اقدام تروریستی دستگیر کرد، اما آنان روز بعد با وثیقه آزاد شدند.
پایگاه هوایی فیرفورد در گلوستشر بریتانیا که پیشینه‌ای طولانی در استفاده توسط نیروهای آمریکایی و ناتو دارد، از ماه مارس به عنوان نقطه‌ای برای پشتیبانی لوجستیکی حملات ایالات متحده علیه ایران مورد استفاده قرار گرفته است. بریتانیا مجوز بهره‌برداری از بمب‌افکن‌های آمریکایی مستقر در این پایگاه را برای هدف قرار دادن سایت‌های موشکی ایران — که کشتی‌های عبوری در تنگه هرمز را تهدید می‌کنند — صادر کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/78583" target="_blank">📅 20:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78582">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQZgGoqUesfvsxWv1N9EBdF2PH4pov_0MNXGiMkzO5KS1kfk8hXuq6SFxHkgu0By_bQgOT78j0dZOBE0JhHdAXJn5b0WlkbBxZoDmiBgxUz2WUyBPxY__YzmGyPdlQNhZxZqYNRSK103x1oZgw0ijJMLXAZXKNnjLB6JkIZw2awrE0f-J9-g_2IoVPIfB4E58fIzN0Di6XHZrO7la4nLZn37v8tg2z9wcB250Nde9TssRsFPH6na8Fy-WWOowRIvU-wwJkLn46tRw2pPN0fTk9eVe5xQ7s4axYbYlJln24NTeQNWVtgc7zdbeIFjjgpSjUb3arm5vPvodbmII57jCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه، چهارشنبه هشتم مهر گزارش داد صرافی‌های رمزارز معاملات تتر را از ساعت ۲۱ هر شب تا ۹ صبح روز بعد متوقف کرده‌اند.
بر اساس این گزارش، این محدودیت از امروز ساعت ۲۱ تا یکشنبه ۱۲ مهرماه اعمال می‌شود و سقف خرید روزانه برای هر کاربر دو هزار تتر تعیین شده است.
این اقدام در پی افزایش پرشتاب قیمت ارزهای خارجی و سقوط ارزش ریال انجام شده است.
عصر چهارشنبه قیمت دلار در بازار آزاد ایران از ۲۵۵ هزار تومان عبور کرد و هر تتر نیز حدود ۲۵۵ هزار تومان معامله شد.
پیش از این بانک مرکزی جمهوری اسلامی نیز اعلام کرده بود اعطای وام برای خرید طلا، ارز و رمزارز ممنوع است و این ممنوعیت شامل تسهیلات مستقیم و غیرمستقیم بانک‌ها و واحدهای دیجیتال نیز می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78582" target="_blank">📅 20:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78581">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhsDtybTDJiNawPJQR3uDrlr-z9Jdc3kDL5kLikMybQ--MCuFi2QbKvpFOK3eIN_ycoaPbglecu6ckC0yoeEL4M9UjNV05f777JxFwxtpTS162zyRIdcW-0Y06Y-smean7MeTeL0WcnBqloLlDW0EC9rP4kX3DYAkuPjTgL29Oq89MbwqlPh7JiMbVDnLgkNxDD3fJnNznCnJZEo_x6c4dqtFxZvst6hQhhRBo_Mq3WSzU4NZntXrkJOxYDvOd5jl5DfB8bSyKXqkN92Vl5hTG7WAj3LZ4Xan5-JUOKh4vc3RUm4U_FzEQmrnEsSjMreniGprXVlvjLwiD045y5JfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد تهران امروز از ۲۵۶ هزار تومان گذشت و دادستان تهران به ضابطان قضایی دستور داد با «عوامل اخلال در بازار ارز» برخورد کنند.
بر پایه داده‌های پایگاه‌های اطلاع‌رسانی طلا و ارز، دلار ۲۵۶ هزار و ۵۰۰ تومان، یورو ۲۹۰ هزار و ۵۰۰ تومان و پوند بریتانیا ۳۳۹ هزار تومان معامله شد.
دلار صبح امروز ۲۵۵ هزار تومان بود و دیروز ۲۵۳ هزار و ۱۰۰ تومان، یعنی در دو روز سه هزار و ۴۰۰ تومان بالا رفته است.
همزمان دادستان تهران از برخورد با فعالان بازار خبر داد و گفت ضابطان قضایی مأموریت یافته‌اند با بررسی میدانی و رصد فضای مجازی، عوامل اخلال را شناسایی و به دستگاه قضایی معرفی کنند و گزارش اقدام‌هایشان را روزانه بفرستند.
نیروی انتظامی جمهوری اسلامی دوشنبه ۱۱ نفر از فعالان بازار ارز را بازداشت کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78581" target="_blank">📅 19:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78575">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rv1mh6Uv39jtYrP3nmPpvur_Umb_rezE5lPv1mikkOyXFkSi7p6K_o94XBar5xhALsLPhmv5BU6vX2cVsgcaWkaTWLFBDCL99VEVJpks7CMSml-qVkV-ADbwtsz4Qfa00K3e8DfpxIA26YAGhv82-PWf1mKdGacVZC7VRWEKLyWQj4pI3fNUS41mkHiRJC13-t727AMgBESJ4KsaqyY5olSKiyqtIoMAhmWQ_4vQxYuEj3FpGTy4lxzxgqLUFvtz9jARFgmpPmmeXyL8i11aN9bqmsFs0950REEJS1lDtq607591AlOQ3Egc8Xj8Sad3pP3vs9xqs0UXjJxXU4vrzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0e653b47a5.mp4?token=p5aVvNjfYwN6YNUIamdM0SH5czbeVxH4_CrBDgRpXxxtu4mePzf7Odk8VEgZKE3scvFbtfJhK-wkDMARTfk_kOnOmLNAvtekQwZF-1qR2TKlaqeXHde5wB-Me_l7JA7IWjBrSZriyS5u5QLx18cE54PcpRf040_cFPYFyKtNnj3TML7EPcrRBtowSxvEJ4dxoayrbYfaRQG-NOELCeV3o-5ChsT3meOyaPYITonGWxI0-Q1fJSMHBMT0Sp_mVNFqPLnGBWcSPUAymfVABGHTRp-VIIj5D2Dr59aRb3oHBM3M-7MTq5SM1KARw4Lt93mCANO5Tmzr4WFUFW0JtwG1sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0e653b47a5.mp4?token=p5aVvNjfYwN6YNUIamdM0SH5czbeVxH4_CrBDgRpXxxtu4mePzf7Odk8VEgZKE3scvFbtfJhK-wkDMARTfk_kOnOmLNAvtekQwZF-1qR2TKlaqeXHde5wB-Me_l7JA7IWjBrSZriyS5u5QLx18cE54PcpRf040_cFPYFyKtNnj3TML7EPcrRBtowSxvEJ4dxoayrbYfaRQG-NOELCeV3o-5ChsT3meOyaPYITonGWxI0-Q1fJSMHBMT0Sp_mVNFqPLnGBWcSPUAymfVABGHTRp-VIIj5D2Dr59aRb3oHBM3M-7MTq5SM1KARw4Lt93mCANO5Tmzr4WFUFW0JtwG1sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی فرود اضطراری یک هواپیمای خطوط هوایی «فلای دوبی» از مبدأ دوبی به مقصد تل‌آویو در عربستان سعودی، نخست‌وزیر اسرائیل گفت کمک‌خلبان این هواپیما پس از حمله با چاقو به خلبان دیگر، ظاهراً تلاش کرده بود هواپیما را با سرنشینانش سرنگون کند.
بنیامین نتانیاهو، در پیامی ویدیویی که روز چهارشنبه هشتم مهر منتشر شد، گفت: «در جریان پرواز، هنگامی که هواپیما به کشور نزدیک می‌شد، یکی از خلبانان به خلبان دیگر حمله کرد و ظاهراً تلاش کرد هواپیما را با همه سرنشینانش سرنگون کند.»
او مسافران هواپیما را «قهرمان» خواند و گفت آنها با اقدامات خود «از وقوع یک فاجعه بزرگ جلوگیری کردند».
نتانیاهو همچنین گفت عربستان سعودی کمک‌خلبان این پرواز را که به ادعای او به خلبان دیگر حمله کرده و تلاش کرده بود هواپیما را سرنگون کند، بازداشت کرده است.
او افزود: «خلبانی که دست به حمله زده بود بازداشت شده و اکنون از سوی مقام‌های سعودی تحت بازجویی قرار دارد.»
نتانیاهو همچنین دستور آماده‌سازی برای مقابله با تهدیدهای احتمالی بیشتر را صادر کرد.
یسرائیل کاتز، وزیر دفاع اسرائیل، نیز روز چهارشنبه این حادثه را «تلاش برای یک حملۀ تروریستی» خواند.
او در بیانیه‌ای گفت: «حادثه جدی در پرواز فلای‌دبی یک تلاش برای حملۀ تروریستی جهادی بود که تنها به لطف شجاعت چند مسافر اسرائیلی خنثی شد؛ آنها وارد کابین خلبان شدند، تروریست را مهار کردند و با دستان خود کنترل هواپیما را به یک خدمه پروازی دیگر که در آنجا حضور داشت، بازگرداندند.»
رسانه‌های اسرائیلی روز چهارشنبه از احتمال ربوده شدن این هواپیما خبر دادند اما بعداً گزارش دادند که «بروز درگیری فیزیکی بین خلبانان» در هواپیما باعث تغییر مسیر و فرود اضطراری آن شد.
بر اساس این گزارش‌ها، این هواپیما از نوع بوئینگ ۷۳۷-مکس کد اضطراری مربوط به ربوده شدن را ارسال کرده و پس از آن ارتباطش با اسرائیل قطع شده بود.
به دنبال این اتفاق جنگنده‌های اسرائیلی به پرواز درآمدند و فعالیت فرودگاه بن‌گوریون نیز متوقف شد.
ویدیوهای منتشرشده در شبکه‌های اجتماعی که رویترز محل ضبط آنها را پرواز FZ1073 تأیید کرده، مسافران را در حال رسیدگی به دو مرد مجروح در کف هواپیما نشان می‌دهد که دست‌کم یکی از آنها لباس خلبانی بر تن دارد.
در یکی از ویدیوها، یک مسافر اسرائیلی درخواست کمک می‌کند و می‌گوید مسافران «تروریست‌ها را مهار کرده‌اند». با این حال، مقام‌های فرودگاه تبوک و این مسافر هویت فرد یا افراد مهاجم را مشخص نکرده‌اند و جزئیات دقیق چگونگی درگیری هنوز روشن نیست.
بر اساس اطلاعات وب‌سایت فلایت‌رادار۲۴، این پرواز ابتدا یک پیام اضطراری عمومی ارسال کرد و سپس پیام اضطراری دیگری فرستاد که احتمال «مداخله غیرقانونی» را نشان می‌داد. هواپیما پیش از نخستین هشدار اضطراری، در کمتر از ۳۰ ثانیه نزدیک به ۱۴ هزار پا کاهش ارتفاع داشته است.
به گزارش این وب‌سایت، هواپیمای بوئینگ ۷۳۷ که رسانه‌های اسرائیلی اعلام کردند حدود ۱۵۰ مسافر اسرائیلی را در خود جای داده بود، بار دیگر پیام اضطراری اولیه را مخابره کرد و سپس در فرودگاه تبوک در شمال‌غرب عربستان سعودی به زمین نشست.
از سوی دیگر، شرکت هواپیمایی فلای‌دبی، مستقر در امارات متحده عربی، اعلام کرد علت درگیری‌ای که «در کابین خلبان پرواز FZ1073» رخ داده، همچنان مشخص نیست و موضوع تحت بررسی رسمی قرار دارد.
سخنگوی فلای‌دبی در بیانیه‌ای گفت: «در این مرحله، دلایل و انگیزه‌های اصلی این رویداد مشخص نیست و همچنان در چارچوب یک تحقیقات رسمی در حال بررسی است. از همه طرف‌ها می‌خواهیم تا زمانی که مقام‌های مسئول در حال جمع‌آوری اطلاعات و روشن کردن ابعاد ماجرا هستند، از گمانه‌زنی زودهنگام خودداری کنند.»
خبرگزاری رویترز به نقل از مقام‌های اسرائیلی اعلام کرد کمک‌خلبانی که این حادثه را رقم زده است، شهروند عمانی است. دولت عمان هنوز درباره این موضوع اظهارنظر نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/78575" target="_blank">📅 19:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78571">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bzOY_zasKbUMZoQi345GOtv7WrVjNr3MJHdhgkUDRkJU833JvUvCpIZOEjh7TCGBm5AJe_6e5xg8c5HumdF4-WCgan3v8hqczmDYR3kf9EyFTXcJnkrm8nPiAaqReCeA8n2nEZUSp6xGRcTraT81aut5g_hrdncI36I9p2Jc9c0rsAANsJwXNNmoqPcGlRAKEaviVUnn188945Mk4a902SawVuJ9XbKukT1hHQCH-WAhuursnL4kIGne015H0cJsR4Q2U3yGm65fsWs08Nud8pSzFNLQCbsz7V9VxV5oSrSPww8DRj10s-MWeUGtOBNtbJiRumK4BeGuCgxh8MMAyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NAwfI9E03PjMngrla8QBvI5l-he6vAWNoS-hiBn3e9pG4S-xpHFIxe2WbUiahg2gPJzRt4iFcMiJzi4c_x6kJjIplD4IwLL2vxYJR4k_AXT2qusDGD3PdDZ87qUusPtG7N_xtkUqcKP2eyhMXmRi9xAUTr77BGpdHkxJMGU3oL1O5rx1ztcT0qutdMISPC73R0zCEc5c1_9Rd2wooWrEhFRHWTTvGC114lWSWHl4jZLtVqCtMhe0Nbt4N6_crd4Tji4tzI7-YdyfFEYOW8CCWOwstwssYXMb92IizLIOnHL91CRON0mfItJlCGbbwPi7kJmm8xmO3vXzmFR9Ki4Z6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FBrAh3dAuh4Wwt8NVXe6PcT6XZpvNZ_cUzx2CkETvl0bVUWFXX0IkLSuU9N3_tpPTVBVo3H_GmNFnoH7FES1GusVPXFMALN7xZnidsuo93XPxqGggyUZU6cvIn1z7GgiH76ZAnAAjFfIF-rYNVUEsPMype5_SlCPf0Gr4xL84MQ0V-vIwE8BoZHN-K5XXRwQ0WUP5z42QzFJBjrBRJb5YGb5EoC21BT9XljXzqDycFslBW6nXSJ2XFRkW7Z2e3vkOm18lW-sHBuLZRafHre_Dv4bihBi64TULZ4Z50zyg79yQ1eoa_KJbpZwKcDfIvEeglbF42irXWqvVFk8x-NNUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rz2ywG13JuvqHG3VAEAQeB1_qNz81lwqOAj2IfCp-Bt_EmLOWvR8tQYJ2Ef4eBuZaX7dY6JRyiXbEKxEdWVNBFfzR0LKOAgtbkaBQQq4kqGgvsCeO-ExibPflPykYzlESXSh-nhfJmnB8oWw1wLVGsrq_lR0pxI3CtQYo0PlemI6lIQyBjKdRMkIpvCyvfkzlY1EWQtgrFpRAfJ1SOEgDIYsj7TxdK5QbQqT-PzR92Mlfnam-MCta2x9onGJ5Rn73uda7lYJNHT7VFLemfwJRYcSUXn8il-Fmc_8fg-Z1t_xya69321w5GmLefMlX2lqktCDXXA1lMHaOtecyyE1ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
«برای کمک به پدر مجروحش رفت که  هدف گلوله قرار گرفت»
🔸
هفت روز طول کشید تا خانواده محمد عباس‌زاده بتوانند پیکر تنها فرزندشان را تحویل بگیرند. در این مدت، بارها به مراجع قضایی و نظامی مراجعه کردند، اما پاسخ روشنی دریافت نکردند و تنها به آنها گفته می‌شد منتظر پیامک بمانند.
🔸
فشارها پس از آن نیز ادامه یافت. برخی از بستگان احضار شدند، از اعضای خانواده تعهد کتبی گرفته شد و مقام‌های امنیتی برای نحوه برگزاری مراسم و حتی روایت چگونگی کشته‌شدن محمد برای آنها محدودیت تعیین کردند.
🔸
خانواده با وجود این فشارها، پیکر محمد را در زادگاهش اهواز به خاک سپرد؛ در حالی که پدر مجروحش هنوز در بیمارستان بستری بود و نتوانست در مراسم خاکسپاری تنها فرزندش حضور داشته باشد.
🔸
سرگذشت کامل محمد عباس‌زاده را در یادبود امید بخوانید.
https://www.iranrights.org/fa/memorial/story/-9241/mohammad-abbaszadeh
@IranRights</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78571" target="_blank">📅 19:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78570">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbigX49JOhP36Qvs3Y4zq30AAO0p13Q0ZO1Zq_q_fRpjGpvKvdXVT-NqdOYEH1_vw3s_otOlB0gJ6ZGFi_lsL-mqCnO3Xx5m870B2rxMxeAVeuPvHIr8LCyBTaMBoWkyj6Y09m2dtx-_AUsO-N2jOjU4YvIAUENFoNJkNwl9rXHdHB6X_e12dTJj5O_TrnR3maZa590XRKmtKh8khBX-483ehr6aWh4BNu4i6-UPJjwiHLlEbbTCpkeGyQ-B_DwAiTdW6tuBhlNxC12uM9CYdviZ4ibh5Ho0AMV6juyHCIgc9fa8i1p_VOcXwtw34xfcmWFtrhVAZxHA_5zdC30NDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی اعلام کرد دو نفر را که در اعتراض‌های دی‌ماه سال گذشته در مشهد بازداشت شده بودند، بامداد چهارشنبه اعدام کرده است.
بر پایه اعلام مرکز رسانه قوه قضائیه، علی همتی سیستانیان و مجید نیک‌اندیش پس از تأیید حکم در دیوان عالی کشور اعدام شدند. قوه قضائیه آنان را به دست داشتن در کشته شدن چهار نفر از نیروهای امنیتی در منطقه‌ای در مشهد متهم کرده بود.
در ادعای قوه قضائیه آمده است دو متهم در بازجویی و در دادگاه به حمله به یک فروشگاه زنجیره‌ای، آتش زدن آن با کوکتل مولوتف، آتش زدن یک بانک و تخریب اموال عمومی اعتراف کرده‌اند.
هیچ اطلاعاتی درباره روند دادرسی، دسترسی متهمان به وکیل انتخابی یا شرایط اخذ اعترافات منتشر نشده است. اعترافات تلویزیونی در پرونده‌های امنیتی جمهوری اسلامی بارها از سوی نهادهای حقوق بشری به اخذ تحت فشار متهم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/78570" target="_blank">📅 09:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78568">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sya9aE06WZXiWULC4VJcEVoy3VTEflU16UcLIf4jQDNifqBXc2-hVPjc0tsy_tDm5TpbmMKxS7FoHeB3nyKBI0wGKVU_KHO4LlEkmKBoJNRDz5S2B4cK2e7fAdh0RewDQHGe0AdUidYT8AfkCnVWHLXtUDk658dBRluJIHuWCJ86g9YtJ3mkEMLnPAe7Y3a2BCCCqDXz4NSKksNUE1A1qT1XBeqlPnZB7fL1L26oU6yD7Lc1hjkqrvGOxcl6oedg7rA_XwKh05z6UqzjCJMpfSIRiS9SsWzmUTS0OQ78DzqMNGgwzPwiiM2u75J0YzgPDYFVF8pe-QIufIi7eNbzQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LnhvUufAXijFV-7XPb5r4_-lIUDQ5xAoXhkn3N3YqQ7Yu0xsyNEofOhd_JM_uM2fYIOS_cWq4cE1Itr8In23K9J4VFAkPh9ahE0CblueoedgPcYqChA7iZN7jrFJ9rxiSXYhllEW6RycwPTKvswdlCHVtUJs6GfOX8jaWqwzCtdSkdjRRs6aYoLzLM8hNDuRjFVYI4ywXTZCGFi5jYk0jAbaArut63sSYGzsowi6Uf7aEFCdFR_2aLv28xTKEU_mrVT6Wu1tzbQR70qLb3j1Gz9K13hvrWN8iW5-AwhN7BD_4seuC-_4ivM6Eh3UaLq5mNrhufts0Oye5mvRJ_w6ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محسن رضایی، دبیر "شورای عالی امنیت ملی"، در دیدار با شاهین مصطفی‌اف، معاون نخست‌وزیر جمهوری آذربایجان، با تکرار مواضع دیگر مقام‌های جمهوری اسلامی گفت: «ترامپ در باتلاقی گرفتار شده که نه می‌تواند مذاکره کند و نه می‌تواند بجنگد.»
او افزود: «شروط ایران به آمریکا اعلام شده، اما ترامپ قادر به تصمیم‌گیری نیست و آمریکا از سر استیصال در جنگ نظامی به محاصره هوایی روی آورده است.»
رضایی ادامه داد: «آمریکا آینده‌ای در منطقه ندارد و ایران با قدرت در مقابل آن ایستاده است.»
@
VahidOOnLine
ساعاتی پیش از این عباس عراقچی در آستانه بازگشت از نیویورک به تهران گفته بود که ماموریتش در این سفر این بود که شروط ایران از جمله درباره بازگشایی تنگه هرمز را به اطلاع ایالات متحده برساند.
وزیر خارجه در جمهوری اسلامی گفته بود که «ایران در این خصوص طرح دارد، شروطش، کاملا عادلانه و منطقی است و اگر آمریکایی‌ها ادعا دارند که دنبال توافق هستند یا دنبال یک راه حل مسالمت‌آمیز هستند، ما این راه حل را معرفی کردیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/78568" target="_blank">📅 21:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78567">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f601498008.mp4?token=G7GD6WQYpY_rSl6d5gn-10-IRfH4zOp2vFAKsHVrRIl6gxcleVd35KZulnvSnXPby7Ky0wuJNjYPBQtPOmYnoOQ1FJPVpynRemo1QSp-xE6ra3ots-ewnGbk9q08tNClqjZCFtKhZXI5ezZ9VYVxB3azaKW9MfewgHgZY8t_ONznD2i-MYs15XD-oWiifybd2x1n23HCbKCcHsh43Q6Gy2Hoq8DEOSq40pg5in4LeZCYiDWXv_UnjEBNqHT3PHJv55gbI8ZU5SCP20X9rMwwNJkiLutunjYXALCGCBWBsh9T9ivHP4uBujHp9zd21QR4IFd-7HYvJSJTiZsbZ9aIqw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f601498008.mp4?token=G7GD6WQYpY_rSl6d5gn-10-IRfH4zOp2vFAKsHVrRIl6gxcleVd35KZulnvSnXPby7Ky0wuJNjYPBQtPOmYnoOQ1FJPVpynRemo1QSp-xE6ra3ots-ewnGbk9q08tNClqjZCFtKhZXI5ezZ9VYVxB3azaKW9MfewgHgZY8t_ONznD2i-MYs15XD-oWiifybd2x1n23HCbKCcHsh43Q6Gy2Hoq8DEOSq40pg5in4LeZCYiDWXv_UnjEBNqHT3PHJv55gbI8ZU5SCP20X9rMwwNJkiLutunjYXALCGCBWBsh9T9ivHP4uBujHp9zd21QR4IFd-7HYvJSJTiZsbZ9aIqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، ترجمه ماشین:
و ایران سلاح هسته‌ای نخواهد داشت. آنها به‌شدت در حال شکست خوردن هستند؛ خیلی بد، خیلی بد. این وضعیت خیلی زود تمام خواهد شد؛ خیلی، خیلی زود. آنها سلاح هسته‌ای نخواهند داشت و قیمت نفت هم به‌شدت پایین خواهد آمد، درست مثل قبل.
من مجبور شدم آن سفر کوتاه را به جمهوری اسلامی ایران انجام بدهم؛ سفر بسیار خوبی بود.
فکر می‌کنم در سال‌های آینده درباره این موضوع کتاب خواهند نوشت و تاریخ کشورمان را خواهند نوشت و خواهند گفت که این یکی از مهم‌ترین کارهایی بود که انجام دادیم. در واقع، این یکی از مهم‌ترین کارهایی است که در دوره دولت من انجام داده‌ایم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78567" target="_blank">📅 19:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78566">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AsSyxtU1whrlrqq4D2Zrja-kzq8OVUc_tLh_7FTYRjXj7otDde6-ONhGRKR7K3sXO6sKUujmTVFiNsqOHNKy9SKk_VEtseu098DWisCRJKQhVnsi_eqVzYg1UkuaAhwCP1Xa8nj9JhSI_wgmor7x2T7rV3W1sGp8IJ29-2vJll-sR3eo0RnaKinn0Rh5ChqEWrLQP59XAxXWzPZ6MZPi_wV3GRO5UgYVeGAV16VSRwDPF0z-14P7nmczs1iJf07P_aeebb6LkIxlQz6IAWMK1r-LQd-rVGv3OVgaXNjptjXbBSrnbVM6qSSSK2xMwpDJMOsW90DovyzcrCDhazdcDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ونس: ایران با نقض تفاهم‌نامه اسلام‌آباد مرتکب اشتباه شد
جی‌دی ونس، معاون رییس‌جمهوری ایالات متحده، در مصاحبه با وینسنت کُگلیانیز، پادکست‌ساز و روزنامه‌نگار محافظه‌کار آمریکایی، مقام‌های جمهوری اسلامی را مسئول فروپاشی تفاهم‌نامه اسلام‌آباد معرفی کرد و گفت آن‌ها با هدف قرار دادن کشتی‌های تجاری در آب‌های منطقه مرتکب اشتباه شدند.
ونس افزود: «فکر می‌کنم ایرانی‌ها متوجه شده‌اند که اشتباه کردند. آن‌ها با ما توافقی امضا کردند، آتش‌بس برقرار شد، قیمت انرژی کاهش یافت و این امکان وجود داشت که اگر ایرانی‌ها به تعهدات خود عمل می‌کردند، از بهبود روابط با آمریکا منافع زیادی به دست آورند.»
او همچنین به ابهام‌ها درباره وضعیت مجتبی خامنه‌ای، رهبر جمهوری اسلامی، اشاره کرد و گفت واشینگتن با قطعیت نمی‌داند که او زنده است یا نه، اما شواهد موجود نشان می‌دهد که همچنان در قید حیات است.
ونس ادامه داد: «ما فکر می‌کنیم او زنده است. البته با قطعیت نمی‌دانیم. من هرگز او را ندیده‌ام. اخیرا هم تصویری از او در مقابل دوربین ندیده‌ام.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/78566" target="_blank">📅 19:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78565">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nLYU5ynMtKspEaDg8MTInqEUPe4Wu3_hrHLDTui9rwL8xcn6GG3RAnVcInyYRTJJQoo0p29i407VfjvXNF2GadtfrqEwmRzphMqRFLdi4FA3IlillrNERlDbHR5DA7tiQWMPuzi-bYdKNI4qXZYi3DbEMI_tmbfDiMVaeQDBmHIG-SQqU9bVmStPrwIc-G982Ac7IHWiSCE1qeOVLeo6nt7RgoOYCy2s4_hxZTAHZY_ftHNEqoo-2fxmt7-9U6e0NY9dB3p6drytOv7byWbl2ujBe9IsN3lzUV_vg9zP_AsyVcWR1xnZswE6yeEHVVjUYKJBAh4JWYRKfWYkVmoq0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد تهران امروز از ۲۵۳ هزار تومان گذشت و رکورد تازه‌ای ثبت کرد.
بر پایه داده‌های پایگاه‌های اطلاع‌رسانی طلا و ارز، دلار در ساعت ۱۴ و ۳۰ دقیقه به وقت تهران ۲۵۳ هزار و ۱۰۰ تومان، پوند بریتانیا ۳۳۵ هزار تومان و یورو ۲۸۷ هزار و ۵۰۰ تومان معامله شد. سکه تمام امامی ۲۴۹ میلیون و ۵۰۰ هزار تومان، نیم‌سکه ۱۲۸ میلیون تومان و ربع‌سکه ۶۸ میلیون و ۵۰۰ هزار تومان قیمت خورد.
دلار دیروز ۲۴۴ هزار تومان بود، یعنی در یک روز بیش از ۹ هزار تومان گران شده است. نرخ ارز سه‌شنبه گذشته حدود ۲۳۳ هزار تومان بود و در یک هفته ۲۰ هزار تومان بالا رفته است.
دلار در ششم مهر سال گذشته ۱۱۱ هزار تومان بود. بهای ارز آمریکا در یک سال ۱۲۸ درصد بالا رفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78565" target="_blank">📅 17:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78564">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GV7-AjwEeFFPT2BwwI_k0SQB-zZT0_VxvQSpo6nL1RKUuM1WJ1bRne2xTe_eGdXgSlQysIy7fe2sn3eadunHzmqvG5w_B1ykTDIirbFPmVMVPMsll2ihKTWzIzgh6-DpfuPfIg5F5UWy3WvLoU3t4dPxdomdJTL_Kdz4nvi2f73dD4MrqGozrfVmQvXy6S2LNbo62bBjSdeXG6Ul1NpALWFgmURcwpAdiYU85-wWxzxyLhKgeZazwE_XLvAPNrjRus6_aLOwvIN0qQGIZFhY-pyRSBA4G9iHUcn9qJi4tJxRuGPGR2lL9aig5xNu3qn1AFDIQyg1FPd4U-gDEV5EHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم از توقیف یک فروند هواپیمای مسافربری شرکت هواپیمایی کاسپین ایران در ترکیه خبر داد و دلیل آن بدهی سه میلیون دلاری عنوان شد.
بر اساس این گزارش هواپیمای توقیف شده بوئینگ ۵۰۰-۷۳۷ بوده است.
این هواپیما زمانی که برای پرواز از استانبول به تهران آماده می‌شد با حکم قضائی متوقف شد و مسافران مجبور شدند پیاده شوند.
شرکت خدمات هوانوردی «تمسیل گزتیم» می‌گوید کاسپین حدود سه میلیون یورو به این شرکت بدهکار است.
بر اساس این گزارش، این شرکت حکم توقیف را از دادگاه گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/78564" target="_blank">📅 17:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78562">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cR6UkvGjXAhHiPQznVhTH5tLibNCULjMPH0iJd2L6wDtrBD6OZHx1TC-XVMmdsA5vANzS7HiD0Mvo5ZFjaJmlxrVVa20XMUGrAOlkvxNG5k4X0oAR0PF_owvn6fSXcj0e8lIJuNwiGnV36kxAyvfyFa4C8dBy8ea1Vgkbq_4ZP5N-pFXMoS4Fjgp5d7uwWk_ECHL17KHJMHBzCtwFO72JHVBwOsTZA_gUGF5po8GM10LdMPir9PIWoAq4Dtav39cQvICxUZHhsVTozJ3jS3Zrc4Vcy-iJRRGQ9gEfeyIC5QHDbtw8ySF0ajPIGc3uiN1CuYTHPnsY5jW2VW5WtnJMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/azmiCvGkrLV6r0B4H1QXnAR7eTY5ZDFEzAwOHO99whByjD2m9__V2T2jzudKntnMee6H4-3abs0DBWz1ekDFA_JJNvLZ808e-s0rQlB0_rV9c2FmK76cTRL4xGeJBYaUit5orKLlVnkiQXYtqU1py-2pQnEQrS76k16a40nAXHYcEPisOn3DusKsZf7FQLIi-94Rm15Lt6UIdt-qbDmCX41APyC2fPkSrFHVlAlzz3c9lJWD0nmuNh8JMVzdGfsV1Vo8V7rkwGqZ1ZreTYQt-GFLSg544z-1pGN30ps2Lby_UffXGtCmR3ql57cX_d4r8ihmQM5vDfNFdQ-u8kCblQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی روز سه‌شنبه ۷ مهر متن نامه‌ای خطاب به مردم آمریکا، دانشمندان، دانشجویان و اصحاب رسانه این کشور منتشر کرد.
در بخشی از این نامه که به زبان انگلیسی نوشته شده، آمده است: «حساب خودتان را از اشغالگران فلسطین که خواه‌ناخواه باید آنجا را ترک کنند و به کشورهایشان برگردند، جدا کنید! ما می‌توانیم همزیستی مسالمت‌آمیزی با هم داشته باشیم.»
سپاه که در دوره اول ریاست جمهوری ترامپ در فهرست سازمان‌های تروریستی آمریکا قرار گرفت، در این نامه از آمریکایی‌ها خواسته است «در برابر سیاست‌های دولت خود موضع بگیرند» و «امور خود را به جای اراذل به اندیشمندان بسپارند.»
@
VahidOOnLine
حسین محبی، سخنگوی سپاه پاسداران، در نشستی خبری با خبرنگاران خارجی درباره نامه سپاه پاسداران به مردم آمریکا گفت در این نامه درباره «میزان محبوبیت» سپاه پاسداران در ایران و خدماتی که به گفته او به مردم ایران و منطقه ارائه کرده، توضیح داده شده است.
محبی گفت: در نامه خود حقایق ژئوپولیتیکی را برای مردم آمریکا روشن کردیم.» او افزود: «از مردم آمریکا خواسته‌ایم که نامه ما را حداقل یک بار مطالعه کنند.
سخنگوی سپاه پاسداران گفت: هیات حاکمه آمریکا به مردم خودشان دروغ‌های بسیاری می‌گویند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/78562" target="_blank">📅 17:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78560">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cd1gUsOcYajJCfzpAXkbcr45sCyc49I8vPTRHEjLyvE3ZfRDeKxd3X8W60IV5--DKyD2iPfsTqVkeSKIjLk2vvVkx9MqQTjt1O9eLggegFyZcyE-iqrx5Rh7Qg81H6gUNV5fU0-aH9kvmFkenGcpjFcqF0j_TJrnppKbW8Jp8JA1etYNmfrCmbHfinEVzoa4tuWcmyn2oTmxqLJlrWimhhqnFk5bOcforWQ3ZCdVRPny60cDG20y_Q5fNbHknAT7ApYjSmm3KeYe6_PXEwsrf4tP9ArpnT1Ex8p4pVZftk2eJGZpmKTydH1piAaoEI8fN8AhX7usJ0neikS6PdZyYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/McU31r_N8bcdVT7JKbu-jW-dP99yDQkjGj8JHL0Cba4Ru-we3HMZb4XJLYUIsLB0krCfr04uf5kmQTCUzN4gXQrvw8ogmrYLYuIgnOcMdQITJSriO7UcrNSeC1_dfF_5or7Kn_dHuNDZFlrxv6LL5Uxq8lqbtA7XYXhgmRqZz2R5JElZtu1QchsJterB8LbiucMDvjWHB_ojKnYrnsvZ2re2bDK2ByKfp_PHrBzB78guMXFd9GGfpf49HfhQGDBFhkA1qmfrbQuseBdPfFZrFCYJiYMN3KkwVqG_2lvDt22u03cJoDUgoX7LzFNej6eAG1zo-QVaCsFBznd9b5hWgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شورای اسلامی، سه‌شنبه هفتم مهر در جلسه علنی وبیناری مجلس، آمریکا و کشورهای منطقه را به حمله به زیرساخت‌ها و نفتکش‌ها تهدید کرد.
این در حالی است که روز سه‌شنبه جمهوری اسلامی در انتظار پاسخ رسمی آمریکا به پیشنهادات تهران است که دونالد ترامپ قبلاً گفته آنها را رد کرده است.
قالیباف گفت: «در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت و اگر امنیت ما تامین نشود، هیچ زیرساختی ایمن نخواهد بود.»
رئیس مجلس شورای اسلامی در عین حال مواضع دونالد ترامپ علیه جمهوری اسلامی در جریان مجمع عمومی سازمان ملل را «سبک‌سرانه» خواند و به او گفت: «بچرخ تا بچرخیم.»
روزنامه خراسان، نزدیک به محمدباقر قالیباف، هم نوشت: «اگر مذاکرات به دلیل اختلافات هسته‌ای به نتیجه نرسد، جمهوری اسلامی فرصت استفاده از نقشه دومش را خواهد داشت تا به انجام حملات پیش‌دستانه روی بیاورد و یک دوره جنگ پرفشار را قبل از پایان انتخابات میاندوره‌ای به ترامپ تحمیل کند.»
شماری از نمایندگان مجلس شورای اسلامی نیز دیگر کشورهای منطقه را به حملات جمهوری اسلامی تهدید کرده‌اند.
از جمله علیرضا سلیمی، عضو هیئت‌ رئیسه مجلس، در گفت‌وگو با خبرگزاری خانه ملت گفت: «باید پذیرفت که امنیت در منطقه یا برای همه خواهد بود یا برای هیچ‌کس».
او افزود که جمهوری اسلامی در برابر هرگونه اقدام تخریبی در منطقه «تماشاچی نخواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/78560" target="_blank">📅 17:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78559">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1d7707475e.mp4?token=m2XrXbE9lNxBWL3moVbBLhnUxphaPYPvu-yFUqTRXNp4zvAm9h6NAQ7xLJFksOHODwSwuSCnQaNGAQoi8q_BRbore7m_auBIpEkNEAp2Pt9cUgqXhykKScdRB8hj7jj4egmvF2qlUvLuawINTwcM6CB7LBfFQfJpKNqcBpdclSQ1NY7KTagi9sQHbRlxBdg_yCQW0WifGD9cByKtz0fV0PkJldIAJBars_OOifSPfYSUmEf6N98tMcMXFOLRGnhD7S03M8I8coac_mJvz9KvNKJVltg9ngViFutr00kJ6F10UoBKHqyKX0y6hec9h5RvealWyCf6Wstt4LL4QgdxEBwanC4xCf7xRq8hBG8Parsl9xXVttoK2DlMgf321rRB5V9Nyfr7JPsnLGSJunsh-4KS0foxJhvsgH2xaMckGrBGP3CNu-LKBvUsalPXSw-tBzD8A1_JvearbunYZweOg0pevOxUbe-hzJ3vKtkwY2QK3MKbvfXdwngiwUCYK-69nc98XV3VEcmF3pyXIX2bepYtCgT6gktczCo5M-_7ZOun4m-BtLgXmGLqRzlbddTGHTQDl0LkEa4lryGp7s2EKAfsv5X_q_qVGabutNgHyrF_Wx47-urPRUvoRz1RjTkDZS1wmQdCRFH4rnCNOOtDDoZQ8TwV2-t5TJRqN_4t4Mk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1d7707475e.mp4?token=m2XrXbE9lNxBWL3moVbBLhnUxphaPYPvu-yFUqTRXNp4zvAm9h6NAQ7xLJFksOHODwSwuSCnQaNGAQoi8q_BRbore7m_auBIpEkNEAp2Pt9cUgqXhykKScdRB8hj7jj4egmvF2qlUvLuawINTwcM6CB7LBfFQfJpKNqcBpdclSQ1NY7KTagi9sQHbRlxBdg_yCQW0WifGD9cByKtz0fV0PkJldIAJBars_OOifSPfYSUmEf6N98tMcMXFOLRGnhD7S03M8I8coac_mJvz9KvNKJVltg9ngViFutr00kJ6F10UoBKHqyKX0y6hec9h5RvealWyCf6Wstt4LL4QgdxEBwanC4xCf7xRq8hBG8Parsl9xXVttoK2DlMgf321rRB5V9Nyfr7JPsnLGSJunsh-4KS0foxJhvsgH2xaMckGrBGP3CNu-LKBvUsalPXSw-tBzD8A1_JvearbunYZweOg0pevOxUbe-hzJ3vKtkwY2QK3MKbvfXdwngiwUCYK-69nc98XV3VEcmF3pyXIX2bepYtCgT6gktczCo5M-_7ZOun4m-BtLgXmGLqRzlbddTGHTQDl0LkEa4lryGp7s2EKAfsv5X_q_qVGabutNgHyrF_Wx47-urPRUvoRz1RjTkDZS1wmQdCRFH4rnCNOOtDDoZQ8TwV2-t5TJRqN_4t4Mk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"#سپهر_بابا کجایی؟"
⚠️
۱۲ دقیقه ویدیوی دلخراش از مرکز پزشکی قانونی کهریزک تهران پدر «سپهر شکری» به دنبال پیکر پسرش Vahid نسخه ۴۰۰ مگابایتی: twimg  آپدیت دو روز بعد: #سپهر_شکری در پی گزارش دروغ صدا و سیما درباره این ویدیو و انتساب این ویدیو به خانواده داغداری…</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/78559" target="_blank">📅 17:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78557">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RGmNym0MkgscTbQDFmQgf1lpFzw72sLI-b11P5mfW_anAvXUpAirdB7d8QNzepR9iY8ub6PR5Fzb3drnGpxzMJyziB6liPF45VDKejUdldPyK5mYbVjCJikHYO8DJQ4TMgXImztOH5rtki0J7m5OjgwNq2ux9wQPEufjRgOrdDiakGV5SevIsvVNMIe2ov4mKB0DuC2vCw74_nvwSA5-hyPD40HlBmu7Vidf6s2nk8DMJvWOuT3U2WZgCsayQZRjtaYbuSmhtDbLbrJZY_xjc-abuQT0vcCA4FEvPKKNiJPZfwGQQUQzA2q5GQnZRLCgwYJJpS9iobuF_chJGjmv_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CA6B7yqWHQ6todCtNwv8EOUII2xrvrZ4FQpSc8R2wYGWmW1DQg-xzEob1wWCup-NSxvaVjEym7RH-EmRgcmf17mXtzJdXw9KSZiuaBEeVrHLfrH87b0tyrLBSiiRL9iymwTjzGTjULAd155vlW3HF84FBnoda5_WMVIA_sRzrIoQwpoPKiPVzvG-IM45KIuFPij2T6R3cZGqmq8MiTFWKkL_dEuUb8Lxa3vbneInmp5EcamDgiD5NJRRu96jdZOPisV3FoYP9im4vhZ62YTP1NG-gbyL3iORyMOvEvX5OkpyfmwawPHjp6fZNi65SQPDvQypL0U1ypTTTeiSytDadg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه ایالات متحده، روز سه‌شنبه هفتم مهر در گفتگو با شبکه فاکس‌نیوز گفت رژیم ایران پولی را که به دستش می‌رسد خرج مردم نمی‌کند، بلکه آن را صرف ساخت تسلیحات و صدور انقلاب می‌کند.
او با اشاره به عملکرد تهران طی سه دهه گذشته افزود: «مسئله صرفا تحمیل هزینه‌های اقتصادی بر این رژیم نیست. پای هر دلاری که ایران در اختیار دارد در میان است. آنچه آن‌ها در ۳۰ سال گذشته انجام داده‌اند این است که هر زمان پولی به دستشان رسیده، چه در چارچوب رفع تحریم‌ها در دوره اوباما و چه از مسیر فروش نفت و گاز، آن را برای ساخت بیمارستان، جاده یا بهبود زندگی مردم ایران خرج نکرده‌اند.»
روبیو در ادامه گفت: «آن‌ها این پول را تنها برای دو هدف استفاده می‌کنند: ساخت تسلیحات برای خودشان و صدور انقلاب. آن‌ها این منابع مالی را برای تامین مالی حزب‌الله، حماس و شبه‌نظامیان شیعه در عراق به کار می‌گیرند. آن‌ها این پول را برای حمایت مالی از تروریسم و طرح‌های ترور در سراسر جهان خرج می‌کنند و بنابراین هر پنی که به دستشان می‌رسد، پولی است که برای مقاصد این فعالیت‌های مخرب استفاده می‌شود.»
@
VahidOOnLine
مارکو روبیو، در گفتگو با شبکه «فاکس نیوز» با تاکید بر اینکه نباید ایران را با حکومت فعلی آن یکی دانست، گفت: «مردم اغلب این اشتباه را می‌کنند که ایران را معادل یک کشور عادی می‌دانند. بله، ایران یک کشور است، اما مشکل ما کشور ایران نیست؛ مشکل، انقلاب و سیستمی است که بر آن کشور حکومت می‌کند.»
او با اشاره به مقامات جمهوری اسلامی که با پوشش‌های دیپلماتیک در رسانه‌ها ظاهر می‌شوند، افزود: «کسانی که در ایران تصمیم‌گیرنده هستند، روحانیون تندرویی با دیدگاه‌های آخرالزمانی‌اند که باور دارند رسالت دینی‌شان رقم زدن روزهای پایانی جهان است.»
روبیو همچنین هشدار داد که دستیابی چنین رژیمی به سلاح هسته‌ای، یک خطر غیرقابل‌قبول برای جهان خواهد بود، چرا که از آن برای باج‌گیری و کشتار استفاده خواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/78557" target="_blank">📅 09:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78556">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZkhNPuCg5BE-Fvcm3nDOBqf0BlNq7bcZ6qHUDhdQ27bUnaEd8q1frPfQbIBd2HqKGqWTrvxNig9gWViC9x1JAhmhEKg2D3Vbe4iJeDXGjTkiDXaDsINEV3sP7UVKAwiJEmPj7Da_IcrFAhS-ur1vr4VKiEUU1Vc9P5uMbqjo7w1BADkGyIP0bWhlWDRzuT_sJTq33n1KTvaXvAWuMtlozdEPZBTIDaDy1WeOh-7M-k0vuCe0luTvPM-TdWgpxxXSjTr1vQ2LeaX55kYHW2WC9BlvR28S4C6TtFKN6KnOeFZ5VAqdzr8yTc5WXqRbGI_a_4Mk5fs0ebUlNXI1qGHaiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ، ترجمه ماشین:
اکسیوس همین الان
گزارشی
منتشر کرده که مدعی است «ترامپ» به ایران پیشنهاد کاهش تحریم‌ها و آزادسازی منابع مالی مسدودشده را داده است. این حقیقت ندارد. من به آن‌ها هیچ‌چیز پیشنهاد نکردم!
گزارش اکسیوس، مثل بیشتر گزارش‌های دیگر، یک حقه و دروغ است که فقط برای ارضای «سندروم جنون ترامپ» آن‌ها منتشر شده است. آن‌ها باید این گزارش جعلی را فوراً پس بگیرند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/78556" target="_blank">📅 01:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78555">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e65799ad06.mp4?token=NIA2F7JY89U9LjFUk-UQeC6XumuUL9iaZkrLewLoj1lNhBpvIRoWCJEc5QaAbNOl6zGo7_96llhrekf57n9gYXsYpAw8LsNSdvmybS2sJMVc5VKxacL32YgPRdIY0ptnk0fLfwo1NrBcrwX02BNUl9aWtz4Noie2YS-qb6v7GZ8yfzoOioc_S9Og9o9g3xGNPHAOmYHi-NS4IwQepWeOXZR-9Sk_iwdPcEBIiSStlp_CHlJk81XK4eiL-R8p7tZNfvHoK7_W7y9AZjqkD6CGgZYxYWd9Sg2P7WF-PQTs9Ra1jWdbAs0-gHWb4uH8kTQGHTCitsAT_FEgC6nInMPf0w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e65799ad06.mp4?token=NIA2F7JY89U9LjFUk-UQeC6XumuUL9iaZkrLewLoj1lNhBpvIRoWCJEc5QaAbNOl6zGo7_96llhrekf57n9gYXsYpAw8LsNSdvmybS2sJMVc5VKxacL32YgPRdIY0ptnk0fLfwo1NrBcrwX02BNUl9aWtz4Noie2YS-qb6v7GZ8yfzoOioc_S9Og9o9g3xGNPHAOmYHi-NS4IwQepWeOXZR-9Sk_iwdPcEBIiSStlp_CHlJk81XK4eiL-R8p7tZNfvHoK7_W7y9AZjqkD6CGgZYxYWd9Sg2P7WF-PQTs9Ra1jWdbAs0-gHWb4uH8kTQGHTCitsAT_FEgC6nInMPf0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز دوشنبه ۶ مهر ۱۴۰۵، در کاخ سفید گفت آمریکا «خیلی زود» در جنگ با جمهوری اسلامی پیروز خواهد شد و پس از پایان جنگ، قیمت بنزین به‌شدت کاهش خواهد یافت.
ترامپ گفت: «این جنگ تمام خواهد شد و ما در این جنگ پیروز می‌شویم و قیمت بنزین با سرعت زیادی پایین خواهد آمد. هیچ‌کس دیگری نمی‌توانست چنین کاری را انجام دهد.»
او درباره برنامه هسته‌ای جمهوری اسلامی نیز گفت آمریکا مانع دستیابی تهران به سلاح هسته‌ای شده است و افزود جمهوری اسلامی این موضوع را می‌داند و حاضر است به آن اذعان کند.
@
VahidHeadline
متن زیرنویس، ترجمه ماشین:
ایران هرگز سلاح هسته‌ای نخواهد داشت. ما خیلی زود در آن جنگ پیروز خواهیم شد. آن جنگ تمام می‌شود و قیمت بنزین به‌شدت پایین خواهد آمد. هیچ‌کس دیگری نمی‌توانست این کار را انجام دهد. هیچ‌کس دیگری.
اگر دموکرات‌ها سر کار بیایند، مرز فوراً باز خواهد شد و میلیون‌ها نفر درست مثل قبل سرازیر خواهند شد. این وحشتناک‌ترین چیزی است که در عمرم دیده‌ام.
بله، آنها حاضر نبودند جلوی ایران را بگیرند که سلاح هسته‌ای داشته باشد. گفتند: «بگذارید یک نفر دیگر این کار را بکند.» البته این را درباره خیلی‌های دیگر هم می‌توانم بگویم. ما جلوی دستیابی آنها به سلاح هسته‌ای را گرفته‌ایم. آنها هرگز سلاح هسته‌ای نداشته‌اند و این را می‌فهمند و حاضرند آن را بگویند.
وقتی جنگ تمام شود، دو اتفاق خواهد افتاد. اتفاق اول در واقع همین حالا هم افتاده است: ایران هرگز سلاح هسته‌ای نخواهد داشت. این موضوع بسیار بزرگی است، چون اگر می‌خواهید آشوب و فاجعه ببینید، بگذارید آنها یک شهر را با سلاح هسته‌ای نابود کنند.
فقط درباره اسرائیل و بخش‌های بزرگی از خاورمیانه صحبت نمی‌کنم. نباید بگذاریم با سلاح هسته‌ای به ما حمله کنند. برای همه آن آدم‌های احمقی که فکر می‌کنند اشکالی ندارد، من با آنها سروکار دارم و آنها دیوانه‌اند. هیچ تردیدی در این نیست. آنها آدم‌های بسیار دیوانه‌ای هستند. همیشه این را به خودشان می‌گویم. می‌گویم: «مرد، تو دیوانه‌ای.» اما آنها نمی‌توانند سلاح هسته‌ای داشته باشند و ندارند.
پس این موضوع بسیار بسیار مهم است که ما در چنین وضعیتی قرار داریم. این کاری است که سال‌ها پیش باید توسط رؤسای جمهور مختلف یا کشورهای دیگر انجام می‌شد. لازم نبود حتماً ما باشیم، اما ما با فاصله قدرتمندترین کشور جهان هستیم. بهترین تجهیزات نظامی جهان را داریم.
و ضمناً، اکنون بیش از هر زمان دیگری در تاریخ کشورمان تجهیزات نظامی تولید می‌کنیم. چاره‌ای جز این نداریم. شرکت‌های بزرگ دفاعی در حال گسترش فعالیتشان هستند. مثلاً لاکهید پنج تا می‌سازد. ریتیان هم تعداد زیادی می‌سازد. همه‌شان دارند مقدار زیادی تولید می‌کنند. اکنون بیش از هر زمان دیگری در تاریخ کشورمان تجهیزات در راه داریم و به‌زودی واقعاً تولیدشان شروع می‌شود، چون این کارخانه‌ها قرار است شروع به کار کنند.
قیمت بنزین خیلی پایین خواهد آمد و همین حالا هم، می‌دانید، اگر نگاه کنید، فکر می‌کنم پیتر، این صددرصد است.
پس ما ارتش ایران را از بین بردیم. تقریباً هرچه داشتند را از بین بردیم و هیچ‌کس درباره این واقعیت صحبت نمی‌کند که ایران هرگز سلاح هسته‌ای نخواهد داشت. هیچ‌کس درباره این واقعیت صحبت نمی‌کند که ما بدترین تورم تاریخ را داشتیم. هیچ‌کس درباره این واقعیت صحبت نمی‌کند که در دوره بایدن شما برای بنزین خیلی بیشتر پول می‌دادید.
بیایید درباره همه این چیزها، می‌دانید، همه‌چیز صحبت نکنیم. در دوره بایدن، شما خیلی بیشتر برای بنزین پول می‌دادید تا الان.
و کاری که من کردم این بود که وارد جنگ شدم تا جلوی چیزی را بگیرم که می‌توانست یکی از بدترین اتفاق‌ها برای جهان، برای ما و برای بقیه جهان باشد. اسرائیل الان نابود شده بود. دیگر اسرائیلی وجود نداشت. دیگر خاورمیانه‌ای وجود نداشت. و بعد موشک‌ها و بمب‌ها به سمت ما و اروپا می‌آمدند. و من جلویش را گرفتم.
و این آقا داشت ۱۸ میلیارد دلار در آیووا سرمایه‌گذاری می‌کرد. او می‌گفت: «من می‌خواهم از آمریکا صرف‌نظر کنم. قرار نیست ۱۸ میلیارد دلار خرج کنم»، چون ما یک دیوانه و یک کشور دیوانه داشتیم که با سلاح‌های هسته‌ای این طرف و آن طرف می‌گشتند، چون قدرت بسیار زیاد است.
اما هیچ‌کس درباره‌اش حرف نمی‌زند؛ هیچ‌کس درباره همه آن کارهای باورنکردنی حرف نمی‌زند.
باز هم، خیلی از شما... نمی‌خواهم بپرسم، چون می‌گویید: «اوه، ما قرار نیست این را گزارش کنیم. ما رسانه اخبار جعلی هستیم. اجازه نداریم گزارشش کنیم.»
همه شما حساب 401(k) دارید. لازم نیست چیز دیگری درباره شما بدانم. حساب 401(k) شما در مدت کوتاهی دو برابر شده است. دو برابر شده. ثروت شما دو برابر چیزی است که مدت کوتاهی پیش بود؛ تک‌تک شما، و این به خاطر من است.
خوش بگذرد، همه. خیلی ممنون.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78555" target="_blank">📅 23:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78554">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">"ترامپ در ازای امتیازهای مشخص هسته‌ای، به ایران پیشنهاد گشایش اقتصادی می‌دهد"
اکسیوس، ترجمه ماشین:
دونالد ترامپ، رئیس‌جمهور آمریکا، آماده است در ازای برداشتن گام‌های مشخص از سوی ایران در ارتباط با برنامه هسته‌ای، به ایران تخفیف تحریمی بدهد و دارایی‌های مسدودشده ایران را آزاد کند؛ مقام‌های آمریکایی این موضوع را اعلام کرده‌اند.
🔻
چرا مهم است:
پیام آمریکا به ایران در حالی مطرح می‌شود که میانجی‌های قطری و پاکستانی این هفته بار دیگر تلاش می‌کنند میان دو کشور در حال جنگ به توافقی دست پیدا کنند.
▪️
در حال حاضر، دو طرف بر سر مسائل کلیدی فاصله زیادی با یکدیگر دارند. ایران می‌خواهد مذاکرات بر تنگه هرمز و محاصره دریایی آمریکا متمرکز باشد، در حالی که دولت ترامپ خواستار آن است که ایران با امتیازدهی در زمینه هسته‌ای موافقت کند.
▪️
با این حال، این پیشنهاد پس از آنکه ترامپ آخرین پیشنهاد ایران را رد کرد، روزنه‌ای از امید برای دستیابی به یک گشایش دیپلماتیک ایجاد می‌کند.
🔻
تحولات اصلی:
میانجی‌ها امروز در نیویورک با عباس عراقچی، وزیر امور خارجه ایران، دیدار می‌کنند تا درباره پیشنهادی از سوی قطر گفت‌وگو کنند که طرف‌ها طی چند روز گذشته مشغول مذاکره درباره آن بوده‌اند.
▪️
انتظار می‌رود میانجی‌های قطری اواخر روز دوشنبه یا روز سه‌شنبه با مقام‌های دولت ترامپ دیدار کنند تا برای دستیابی به یک گشایش تلاش کنند.
▪️
یک مقام آمریکایی مطلع از مذاکرات غیرمستقیم، این گفت‌وگوها را «مثبت و سازنده» توصیف کرد و گفت ایران «نشان داده است که در مسائل هسته‌ای انعطاف‌پذیر است.»
▪️
اما این مقام همچنین گفت هنوز اختلاف‌هایی وجود دارد و تأکید کرد «تا زمانی که به مسائل هسته‌ای پرداخته نشود»، توافقی در کار نخواهد بود.
▪️
این مقام گفت: «طرف‌ها همچنان درباره زمان‌بندی تعهدات و اینکه چه کسی باید ابتدا کدام گام را بردارد، اختلاف دارند.»
🔻
آنچه می‌گویند:
این مقام گفت: «تردد در تنگه هرمز همچنان در حال افزایش است و محاصره و تحریم‌ها همچنان موقعیت ایران را تضعیف می‌کنند. موضع آمریکا هر روز قوی‌تر می‌شود و رئیس‌جمهور ترامپ همچنان صبور است و کاملاً به هدف خود مبنی بر اینکه ایران هرگز به سلاح هسته‌ای دست پیدا نکند، متعهد است.»
▪️
این مقام افزود که کاخ سفید نسبت به وعده‌های ایران بدبین است و ایرانی‌ها را متهم کرد که با شلیک به کشتی‌های تجاری در تنگه هرمز در ماه ژوئیه، آخرین تفاهم‌نامه را نقض کرده‌اند.
▪️
این مقام گفت: «آمریکا این بار به تضمین‌هایی نیاز دارد که نشان دهد ایران جدی است و صرفاً تلاش نمی‌کند از شرایط دشواری که در آن گرفتار شده، خارج شود.»
axios
🔄
آپدیت:
ترامپ تکذیب کرد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/78554" target="_blank">📅 20:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78553">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3aba301950.mp4?token=WFNmXaNeIRmsVtf6MjIvb860sI1LWe-z69e8oTtXdfK-1-goreM163sL1Vabyo2ao4P8uSdOqM3w7YJeIkR7zj64lQmLthkxQzNomBmYtxfwCuQncyTkqGDh83z5JljssyZEppNJYv5Ebjqfp2UQrNSlOtMmrlzpPXMeUPpB0EPi5fbtlvTswh32oUYWAepiy5gFGEYyH-yRqSgj0DrVoUHeR_qzaDVKiSug5VqmxXWTfzIAvWtp2s6Piq9PuEC8os2qgp8dab1sR9ihAFq6192DA5lhRMuWIQm8VxuQmCAbshckqCeDUQQxbak87ZbruLEzhPDBl-iJZRUTHeux6A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3aba301950.mp4?token=WFNmXaNeIRmsVtf6MjIvb860sI1LWe-z69e8oTtXdfK-1-goreM163sL1Vabyo2ao4P8uSdOqM3w7YJeIkR7zj64lQmLthkxQzNomBmYtxfwCuQncyTkqGDh83z5JljssyZEppNJYv5Ebjqfp2UQrNSlOtMmrlzpPXMeUPpB0EPi5fbtlvTswh32oUYWAepiy5gFGEYyH-yRqSgj0DrVoUHeR_qzaDVKiSug5VqmxXWTfzIAvWtp2s6Piq9PuEC8os2qgp8dab1sR9ihAFq6192DA5lhRMuWIQm8VxuQmCAbshckqCeDUQQxbak87ZbruLEzhPDBl-iJZRUTHeux6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامحسین محسنی اژه‌ای، رئیس قوه قضائیه جمهوری اسلامی، روز دوشنبه ششم مهرماه از دادستان کل کشور و مقام‌های قضائی خواست تا با آنچه او «وضعیت برهنگی» توصیف کرد، «قاطعانه و با برنامه‌ریزی» مقابله کنند.
اژه‌ای خطاب به مدیران قضایی گفت: «نباید از هیاهوها ترسید... رئیس جمهوری هم با مقابله بابرهنگی موافق است. مجلس هم قطعا موافق است که این بساط برهنگی جمع شود.»
جمهوری اسلامی در زمان اوج جنگ تصاویر زنان بدون حجاب حاضر در تجمعات شبانه حکومتی را به‌عنوان حضور ایرانیان از اقشار و افکار مختلف، پخش می‌کرد و در اختیار رسانه‌های بین‌المللی قرار می‌داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/78553" target="_blank">📅 16:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78552">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbWHWd45OkDqI2eDeftR14Prhi0Fj7meW5fV3QD3UtvS2aVR9Z-VEEGZizWK5q4MdZzFBW0izdt3qSPJeZUQHAm4PFUIRiAYoSAJzxXjiH4cObAA0CY4LkVqRHIM0fp96F7sMEESiEiBpbkPqifohKGb491zO_4pejc5WyZ3WbwvnFeZyzOK3KBVO0MvomyzFyOpwVqKoqCSQJt4wVqf1YP2NuZYtUeUex7VLeeyTFc7_eB8DE-CdRb4hXaQC4CRJspSncKPUij7YvoKOon_r_5DVeQ_oc3UcTCHheHarSX3V07muRPdE_WF1npJSSqu-HFn3f4kTztiQIYa6ik_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مایک والتز»، نماینده آمریکا در سازمان ملل متحد، گفته است واشینگتن پیشنهاد هفت‌روزه ایران برای آتش‌بس و بازگشایی «تنگه هرمز» را به دلیل شروط تهران، از جمله «دسترسی به میلیاردها دلار دارایی مسدود شده» و «لغو تحریم‌ها»، نپذیرفت.
والتز روز یکشنبه ۵مهر۱۴۰۵ در گفت‌وگو با شبکه «ان‌بی‌سی نیوز» درباره دلایل مخالفت دولت «دونالد ترامپ» با پیشنهاد ایران گفت: «آنها میلیاردها دلار پول مسدود شده می‌خواهند و خواهان لغو تحریم‌ها هستند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/78552" target="_blank">📅 16:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78551">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q2efeHpijwk1rS--DLofNUMmeck5G7B4eyKmTccZh0f3W6x9mkCQ-TphduaMDihfvjC5kZviHozErihg-54D4dvr7nYFzwP1CvzUGVUGCuLQjPMdqWVNe2Aelnl5TIAnrfHHynN__iO6yaYhap1KCaJKnVrW7cgZaoj7cE-Dam1UbWQmuN_TovZQJFA4eLbhQOaDo1V4tBLPlcnYR6JX8MAnEaqYn7Dh5PqXqbUoJzbL7Ue48XCrfejLLFbUMBumuK1eWRZvS29tWqmvJiLg1O11_-Hiz3FLq0MFfGzfijKuJY01fj2414xKNRSdeP5YdOsz_Lznc5fe3NmZ7Cb2rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت ارز در بازار آزاد ایران روز دوشنبه ششم مهرماه تنها در چند ساعت بیش از ۶ هزار تومان افزایش یافت و دلار از ۲۳۶هزار تومان به ۲۴۲ هزار و ۵۰۰ تومان رسید.
سقوط آزاد ارزش پول ملی ایران، همزمان با تشدید تنش میان تهران و واشنگتن و در حالی که تحریم‌های همه‌جانبه و بی‌سابقه آمریکا علیه جمهوری اسلامی ایران ادامه دارد، وارد مرحله جدیدی شده است.
سایت‌ها و کانال‌های اعلام قیمت ارزهای خارجی گزارش می‌کنند که روز دوشنبه، یورو به مرز ۲۷۶ هزار تومان رسید و پوند بریتانیا هم رکورد ۳۱۸ هزار و ۶۰۰ تومان را شکست.
@
VahidOOnLine
قیمت دلار در بازار آزاد ایران ظهر امروز دوشنبه ۶مهر۱۴۰۵ از مرز ۲۴۳ هزار تومان عبور کرد و رکورد تازه‌ای بر جای گذاشت.
اما خبرگزاری «فارس»، وابسته به سپاه پاسداران، افزایش نرخ ارز را به اظهارات وزیر خزانه‌داری آمریکا، کانال‌های تلگرامی و فعالیت دلالان نسبت داده است.
دلار صبح دوشنبه از مرز ۲۴۰ هزار تومان گذشته و تا ۲۴۰ هزار و ۵۰۰ تومان افزایش یافته بود، اما تنها چند ساعت بعد قیمت آن از ۲۴۳ هزار تومان نیز فراتر رفت.
@
VahidHeadline
به نوشته هم‌میهن، قیمت سکه معروف به امامی نیز روز دوشنبه در کانال ۲۴۳ میلیون تومان قرار گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/78551" target="_blank">📅 16:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78550">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBt-TvugxAI0Tkruvzdw81KUiNMUHh6DFOBzTKu9UY4geZW9S5_tP9pxMeuIsf87V2o69HI3IRU8CQantksSx_wJmQln-uTf2K1ZtnnyR3_8XNd0MZli9O7MaBDG21xzG-1CCoAiSczDK60876COfAeesbv7ZpqzdICWGM6S_EMELa6g3p7IHKSeK2FGxMFBKVnnVdJnshuSjbbQQSkcMVZYGYzfw23-suMqK6RBa0ylO_3qBnSACszI0JdEQxVysadRG431DoWXqeLFzVL5xxeAZSzy0lU0QYJbpMewe-zn9ZCVZGyqR5t_egBQpzUsp3G7NA44scLEZ3myv7_Wew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محبوبه شعبانی»، از بازداشت‌شدگان اعتراضات دی۱۴۰۴ که به‌تازگی به اعدام محکوم شده، امروز دوشنبه ۶مهر۱۴۰۵ به سلول انفرادی زندان «وکیل‌آباد» مشهد منتقل شده است.
خبرگزاری «هرانا» گزارش داده مسوولان زندان با اعمال خشونت، محبوبه شعبانی را از بند «آرامش» خارج و به سلول انفرادی منتقل کرده‌اند. دلیل این اقدام تاکنون مشخص نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78550" target="_blank">📅 16:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78549">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/16f966f0d3.mp4?token=ih1yByxz3_rbhQr7qyowryOTiiiyKfAVza9ht-DdZliQcvnHNqKboLLo0piyKNouozOIiJr4yzmrjI40Ez5SJCQGsjJfxyR3f67PEn35rWLCOHC3gKzvxDt2l6HFTDRulMFxEr0lOreHT37McKxUW8Di-JyI3r2kS3mR0TJkahthJIRhyaHsgEmOp7XbO8iSvyKcsVWBYGsXmyFhAWJ0M-278SKPQf0fVn_oMCekk49rSVd8t2hd7hhVIfu5E-roif8QjkNLyazhYaUGji-B-mLfNfeKzOayHD18Fu6Ii8LJTgdi2I49KHV3p9X0mVaa0X1M_pXyIpeRAlFS2sgPNA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/16f966f0d3.mp4?token=ih1yByxz3_rbhQr7qyowryOTiiiyKfAVza9ht-DdZliQcvnHNqKboLLo0piyKNouozOIiJr4yzmrjI40Ez5SJCQGsjJfxyR3f67PEn35rWLCOHC3gKzvxDt2l6HFTDRulMFxEr0lOreHT37McKxUW8Di-JyI3r2kS3mR0TJkahthJIRhyaHsgEmOp7XbO8iSvyKcsVWBYGsXmyFhAWJ0M-278SKPQf0fVn_oMCekk49rSVd8t2hd7hhVIfu5E-roif8QjkNLyazhYaUGji-B-mLfNfeKzOayHD18Fu6Ii8LJTgdi2I49KHV3p9X0mVaa0X1M_pXyIpeRAlFS2sgPNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"از او بگو به دنیا.. از او که قصه ای داشت
او جشنِ زندگی بود.. سروی که قد برافراشت
از اُجرتِ گلوله .. از شر که می‌هراسد
از مادری که او را از خال می‌شناسد
از او بگو به دنیا.. ای شاهدِ غروبان!
این رقصِ بی‌سران است، این داغِ پایکوبان..
یاد آر اگر رگت را با مرگ می‌خراشی
تو بازمانده‌ای تا او را گواه باشی!
دیدی که بر مزارش، رقصِ پدر کدام است؟
این هلهله عزا نیست.. آئینِ انتقام است
از او بگو به دنیا.. از نغمه‌ای که سر داد
از او که نیمه جان بود در کیسه‌های اجساد…
از او بگو به دنیاااا"
monaborzouei
Lyrics: Mona Borzouei
Music & Arrangement: Reza Sadeghi
Producer & Concept: Sia Davarnia
Executive Producers: Mahshid Hamedi Boromand & Farshid Rafe Rafahi
Director: Carlito Brigante
Video Producer & Director of Photography: Avid Eghbali
Ebihamedi
📱
youtube
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/78549" target="_blank">📅 18:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78548">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hxxzDpYRTPs7f2qFMQWx2eg0X9uhP_3epdZKLvQx9uZ0sNZ8LPDkoPELvuTr5ZlFvaDOipRnpF3CyI96WriM5i3LwcVWYhGQTHZB4Dm3qbcYSaik75GNfsy-GdxNdGk5Ma46xomnSMWy0zE7nPxZIjCQaxwvTGAI4cGFDz2Cx17eMsn1j5YlSZH3rkVIoLWvs4DdQm_hPFBOQQDqDjMGxOxVzHCTEV_qEjVi4kVp1sTAO-SE9YU01qU33Jx4bs02ORIL_20adPRut-WbzYm6NRFoRJCGCrmOEcH6zUpR9OWpOU-c3Z6lM0FclEIhibJLEM4iMtJaedErqtlvlRe8XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا، روز یکشنبه پنجم مهر ماه و یک روز پس از آنکه اعلام کرد پیشنهاد ایران برای پایان دادن به جنگ را رد کرده است، در گفتگویی تلفنی با آکسیوس گفت انتظار دارد مذاکره‌کنندگان آمریکایی این هفته مذاکرات بیشتری با ایران داشته باشند.
ترامپ گفت: «انتظار دارم این هفته مذاکرات بیشتری با ایران داشته باشیم. آنها می‌خواهند به توافق برسند، اما این توافقی نیست که من بخواهم به آن برسم. این همان چیزی است که شاید یک سال پیش با آن موافقت می‌کردیم. آنها بیش از حد روی مواضع خود پافشاری کردند.»
به گزارش آکسیوس دو منبع منطقه‌ای نیز اظهارات ترامپ درباره برگزاری مذاکرات بیشتر در این هفته را تایید کردند و گفتند انتظار دارند دور دیگری از گفتگوهای غیرمستقیم میان آمریکا و ایران از روز دوشنبه برگزار شود.
با این حال، آکسیوس گزارش داد مشخص نیست اختلافات میان دو طرف بر سر مسائل اصلی قابل حل باشد. ایران می‌خواهد مذاکرات بر تنگه هرمز و محاصره دریایی آمریکا متمرکز باشد، در حالی که دولت ترامپ خواستار تعهد ایران به امتیازهایی در پرونده هسته‌ای است.
@
VahidOOnLine
پیش‌‌تر:
دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز یکشنبه پنجم مهر در حاشیه حضو در مسابقات گلف جام رؤسای جمهوری در شیکاگو، از رکوردشکنی انتقال نفت از تنگه هرمز خبر داد و تاکید کرد به محض «تسلیم ایران» و پایان جنگ، قیمت نفت به‌شدت کاهش خواهد یافت.
ترامپ با اعلام آنکه شنبه شب «مقدار بی‌سابقه‌ای» نفت از تنگه هرمز منتقل شده، افزود این میزان حتی از مقدار نفت منتقل‌شده پیش از آغاز جنگ نیز بیشتر بوده است. او همچنین گفت قیمت نفت اکنون از دوران دولت جو بایدن پایین‌تر است.
@
VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/78548" target="_blank">📅 18:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78546">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NsedHActZKpBLgXGV_YSJ3wP_BNOjrqt_W2OZ_AwwY5etQe3icBEMUSR5mB_EH8eFAROn3KgJQbyVresgLRNfcRQSyYdw66a6InTA95ki9pMzrMuqb-hXK9H0bfb5o1Wm8z9H8ilgIXpYwBa0VrmocLyIIKj0krX_NIc0Qxg2HRRx7MffKNAEM_pKN0_qZqPRMih6EQKvwmKcgXdKu7-H9Qf6A0S9tBu-F_h0odLTKf3uQGZLX-60ygzenzGZD6epzxkOrapgG1CqiheF6Un2iMq8cfbyeRyGcqy9en9L4jvUHsgayPy-VyO4H6dXjHLbj6eUKjl4GlEPIIS_I1vAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i1XmDi7fapC08Ov-tRM113keCczhyZ8kpWGiOdcQalAlW9Y795ELWBkr77mDXsgie7dAbCDJ0F6Z5_-Dze8W61y9nOLaAh6zByRaSiK5QhZvmjbGpdh6PC_w6WBHc0tiTuXblDy3vwx937AKc3OPWlTflcjgAsu6Nuimxhu-h7C0vUXTn9FLQ8gzap3m7NuNxB1LP-nzUxh-fRxpv_SO5YufEpQTfACLLyeNxJrxLHvgPC-jQwtixbHt7zxOxsQ-nk694kc-JnpFiGUC_gfJ81TlllENxHunGUw9z1R0XdzXBTIjB6b9Xz3n9wz4DkZvdMqcQWNNM2ejOoSHG-YNBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، می‌گوید با وجود اعلام علنی دونالد ترامپ درباره رد پیشنهاد هفت‌روزه تهران، هنوز پاسخ رسمی واشنگتن از طریق میانجی‌ها به جمهوری اسلامی منتقل نشده است.
او با اشاره به اظهارات متفاوت دونالد ترامپ در روزهای گذشته افزود: «متاسفانه از رییس‌جمهوری آمریکا حرف‌های ضدونقیض زیاد شنیده می‌شود.» عراقچی گفت تهران منتظر خواهد ماند تا واسطه‌ها «نظر قطعی» واشنگتن را اعلام کنند و سپس درباره گام‌های بعدی تصمیم خواهد گرفت.
@
VahidHeadline
عراقچی روز یکشنبه ۵مهر ۱۴۰۵، در گفت‌وگو با برنامه «میت دِ پرس» شبکه ان‌بی‌سی نیوز، در پاسخ به گزارشی درباره احتمال ازسرگیری حملات آمریکا پس از انتخابات میان‌دوره‌ای این کشور گفت: «ما کاملا برای ازسرگیری جنگ آماده‌ایم. در برابر هرگونه تجاوز جدید ایستادگی می‌کنیم، حتی اگر به جنگ آخرالزمانی منجر شود.»
او در عین حال افزود: «هم‌زمان آماده دیپلماسی هستیم. انتخاب با رییس‌جمهور ترامپ است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78546" target="_blank">📅 18:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78545">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/125cba9619.mp4?token=F1hQoBBmuU7P0IUkdFwRVjK09ETSDSjfUKpHDa9hbAEZaLTcSdr0Aeu860wW9FvJHJO2rPFtcwEGIfsSwGdSofjRs4E87GP48zo2ULnFn8JyoOn3G5hOWmEdTLBjS5fYf8S-DSNHsBgh1aktpjzHmaUOq8mu8Bz7pKlivC0dDBDAk9rqO5H7Bxy4hn3-yv7YHHLQUMkF8p7f-0SMPH0ku3qn9w3WqSiLjsBWK5VR0LJi9yieXz49l1-aUiS1k4QUt_lHLgQaNK7Bi4TftkKpbzZlQQk1PW1ftnvf8GqbanhxL24_X35uCaGfhRUf1qUGatxQ0yU73Fd70lKLD1kUmg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/125cba9619.mp4?token=F1hQoBBmuU7P0IUkdFwRVjK09ETSDSjfUKpHDa9hbAEZaLTcSdr0Aeu860wW9FvJHJO2rPFtcwEGIfsSwGdSofjRs4E87GP48zo2ULnFn8JyoOn3G5hOWmEdTLBjS5fYf8S-DSNHsBgh1aktpjzHmaUOq8mu8Bz7pKlivC0dDBDAk9rqO5H7Bxy4hn3-yv7YHHLQUMkF8p7f-0SMPH0ku3qn9w3WqSiLjsBWK5VR0LJi9yieXz49l1-aUiS1k4QUt_lHLgQaNK7Bi4TftkKpbzZlQQk1PW1ftnvf8GqbanhxL24_X35uCaGfhRUf1qUGatxQ0yU73Fd70lKLD1kUmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه: دومین زیردریایی بدون‌سرنشین آمریکا را در تنگه هرمز به غنیمت گرفتیم
نیروی دریایی سپاه پاسداران انقلاب اسلامی روز یکشنبه پنجم مهرماه با انتشار بیانیه‌ای مدعی شد که یک زیردریایی هدایت‌پذیر از راه دور بدون‌سرنشین (زهپاد) آمریکایی را در تنگه هرمز شناسایی و به غنیمت گرفته است.
در بیانیه سپاه آمده است که نیروهای نیروی دریایی این نهاد در یک «اقدام هماهنگ و پیچیده» و با استفاده از اشراف اطلاعاتی و جنگ الکترونیک، این وسیله زیرسطحی را که  «برای جاسوسی در تنگه هرمز» فعالیت می‌کرد، به دام انداخته‌اند.
سپاه این زیردریایی را REMUS 600 معرفی کرده و گفته است که آن را به غنیمت گرفته و اکنون در اختیار متخصصان نیروی دریایی سپاه قرار دارد تا اطلاعات آن بازیابی و بررسی شود.
رسانه‌های وابسته به جمهوری اسلامی نیز هم‌زمان ویدیویی از این وسیله زیرسطحی منتشر کرده‌اند و آن را به‌عنوان «دومین» زهپاد یا زیردریایی بدون‌سرنشین آمریکایی که در جریان درگیری‌های اخیر در تنگه هرمز به دست ایران افتاده است، معرفی کرده‌اند.
براساس گزارش رسانه‌های دولتی ایران، این زیردریایی یک وسیله نقلیه زیرسطحی خودران (UUV/AUV) است و برخلاف یک زیردریایی سرنشین‌دار، خدمه‌ای داخل آن حضور ندارند.
این خانواده از سامانه‌ها برای ماموریت‌هایی از جمله شناسایی و مقابله با مین‌های دریایی، نقشه‌برداری از بستر دریا، شناسایی و پایش زیرسطحی و جمع‌آوری اطلاعات دریایی استفاده می‌شود.
ادعای امروز سپاه در حالی مطرح می‌شود که پیش از این، در ۱۷ شهریورماه نیروی دریایی سپاه از توقیف یک وسیله زیرسطحی آمریکایی دیگر در نزدیکی ورودی تنگه هرمز خبر داده بود.
سنتکام در آن زمان اعلام کرد که آن زیردریایی به‌دلیل نقص فنی متوقف شده و «حاوی اطلاعات حساسی» نبوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/78545" target="_blank">📅 18:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78544">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WbQ8e7hSXCrj8syTRQfV-hTBjQFtjT-d08g4yQzM76afDIdkwRiCjlSoW0Xhg6p6r-yVm0MaXKftfSoDsMeTW2IbRDTcE3Iuo3p1AovHhSaqQTm3m-xfboSv0Nl4Nh_LBs7OJ8JlcgvpMI1fkHsEmte7LLAn01SErAzzJ-qJck4xRW0HLXpqYL07TXS_FgqDa196h6v1bs_RR1DBpxqCQcFVHt74wf9gFiOp74xdRaXfW3f_bE_oao9SamQRnNqWKOjzuxWDhkBhrG3Y-WDRfiJdtqo7VOF0hbWYSdHGZpxx4vuXpv1Y9RLFiUwb__dc_3atG44zPmHdJXMiOUVvrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد اکرمی‌نیا، سخنگوی ارتش جمهوری اسلامی، در گفت‌وگو با خبرگزاری دانشجو گفت: آمریکایی‌ها در منطقه در وضعیت مناسبی قرار ندارند، اگر وضع آمریکا خوب بود تلاش برای تغییر وضعیت نمی‌کرد. آمریکا ممکن است دست به یک تعرض بزند اما ما از گذشته آماده‌تر هستیم.
اکرمی‌نیا گفت: آمادگی انگیزشی و روانی داریم و تلاش کردیم تجهیزاتمان را بهینه کنیم و تجهیزات جدید وارد سازمان رزم کنیم.
سخنگوی ارتش جمهوری اسلامی افزود: اگر دشمن دست به تعرض بزند منطقه بیش از گذشته درگیر جنگ و ناآرامی و خشونت خواهد شد و کشورهای منطقه آسیب بیشتری خواهند دید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/78544" target="_blank">📅 18:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78542">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dsHIryTIJrCdh2kC9qnhcxZQYrhQJgHkgTMrCNnRmaiFbiUV5mdV0EsAIc9fft4vjwFb3ZF7FdSXx8C-zNVQyhPKl0xVVvKxZa5X20O88est581vAVQ4zI99_YyfR4ihyukvFMWiRsviH3ijxfjlSTlCZU8bMlJeQOhxt_KHAOsYra94SYGlzyhM9DxcvGGt4s5F2S_A1IyJ1R_umWaVGpJv0GivYOfF-pcjm3UKZA1FOEemZhhCbf2i6PbvkT_5rZsDXfH6J5D4Hy25PJYXDKcI3oJi6ZE-WI5frmAdd-EON_j3z2_DjRxU3ibI2Uu97rQq5TfECpJWkskPNN9M5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dBgOiX0OGLjdWrYj94aQqeH9vyZ3FA1P87SOLeG8oe1yCRDWCMl3PSHTE7Dq-KEUCShoM_N16n2V4_TUP4BqZUxA4CZlWi829Dgk523kEbuRPwF7lGpNO7_hB4AHhvR_3cN64LeZ4pvQ1ushVO0Jnx33NOJAfZ_ltVN4hZZnCZCKSrQZTpMrQ1PJZFKJkLL_xx48tISQmtG_m254yL1NHpCQostcPRM58EREC-ZnIRiUdxNK4THUg71cDTcafJp3fI_TB3xHlJ9Sf7OtSlgdIIVufcxgJpBLmsmfwfJhkj7yjqRuOpmAXvqtRdyJbtQbRKytFHbPRqNKXQlcfOfjTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمید رسایی در پرونده شکایت محمدباقر قالیباف به ۱۰ ماه حبس محکوم شد.
این نماینده مجلس شورای اسلامی گفته است که برای اجرای حکم خود را معرفی می‌کند.
دادگاه به استناد ماده ۶۹۸ قانون مجازات اسلامی، حمید رسایی را به «اعاده حیثیت و رفع اثر از ادعای نادرست از طریق انتشار تکذیبیه در صفحه اول نشریه ۹ دی» و ۱۰ ماه حبس تعزیری محکوم کرده است.
گفته شده است با توجه به اینکه این جرم قبل از دوره نمایندگی رخ داده، حمید رسایی مشمول مصونیت پارلمانی نیست و دادگاه او را برای اجرای احکام احضار کرده است.
@
VahidHeadline
عباس عبدی، روزنامه نگار و فعال سیاسی، به دلیل انتشار یادداشتی در روزنامه اعتماد به یک سال حبس تعزیری محکوم شد.
روزنامه اعتماد هم در این پرونده به دو ماه توقف فعالیت و انتشار محکوم شده است.
آقای عبدی در بخشی از این یادداشت که ۱۶ اردیبهشت ماه در روزنامه اعتماد چاپ شده بود نسبت به انتشار «اخبار جعلی» از سوی برخی از نمایندگان تندرو هشدار داده و گفته بود: «این افراد تحت نام نمایندگی هر چه بخواهند می‌گویند و کسی هم در مقام اصلاح آن‌ها برنمی‌آید.»
در پی انتشار این یادداشت، دادستانی تهران او و روزنامه اعتماد را به چند اتهام‌، از جمله «ایجاد دوقطبی کاذب و اختلاف میان اقشار جامعه» و «نشر اکاذیب و مطالب خلاف واقع» تحت پیگرد قرار داد.
@
VahidHeadline
صادق زیباکلام نیز در پی مصاحبه‌ای با خبرگزاری آنا به یک سال حبس تعزیری و از باب مجازات تکمیلی به منع هرگونه فعالیت رسانه‌ای، مصاحبه، یادداشت‌نویسی و انجام مصاحبه به مدت دو سال محکوم شده است.
@
VahidHeadline
حکم یک سال حبس در پرونده حشمت‌الله فلاحت‌پیشه نیز در دادگاه تجدیدنظر تأیید شده،‌ اما به مدت پنج سال به حال تعلیق درآمده است.
سیامک رحمانی، روزنامه‌نگار، نیز پس از تفهیم اتهام و صدور کیفرخواست با اتهام «فعالیت تبلیغی علیه نظام» به پرداخت جزای نقدی درجه شش به میزان ۸۰ میلیون تومان محکوم شده که این رأی قابل تجدیدنظر خواهی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/78542" target="_blank">📅 18:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78541">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spdn2_xFOjy3A6DLZ4zCUHGYWaDspAbyMkG3J2vE7OrtxwCwW2n6lp-qSXdXCjDGWi2kZ7D9bWXL5w2cHKbwAFixaUe2p-gFroRhYiA_Bv-lgflthNL15sHYydLihz1KqfO0bgxqziCkNBO7SDwLRQzTq09lWCyEhUJDyC3snUgx3RvC4oEnG40mikC_n7jT-UToci-up-lEnXI4i8s7pfmiWYpZcNp6aayDeKBoZlYaATwf_ltPUHJtp5B34UrCmF4f4RT8zJVHTGJ4trf7zrB4ktbUl2NGQBBlYq3zuVZmuleUnNU9ytCfOxPrFEPNFaUN4mm4aSsveQLhpmcTVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم پنج سال حبس دیگر برای علی یونسی، دانشجوی مهندسی کامپیوتر و دارنده مدال‌های المپیاد نجوم، در دادگاه تجدیدنظر تأیید شد. این حکم پیش‌تر از سوی شعبه ۲۹ دادگاه انقلاب صادر شده بود.
یونسی و امیرحسین مرادی، دانشجوی فیزیک دانشگاه صنعتی شریف، قرار بود با پایان محکومیت قابل اجرای خود در آذرماه ۱۴۰۵ آزاد شوند، اما با تأیید حکم جدید، علی یونسی همچنان در زندان خواهد ماند.
تابستان ۱۴۰۴، این دو دانشجو هر کدام به اتهام «فعالیت تبلیغی علیه نظام» به ۱۵ ماه حبس محکوم شدند و علی یونسی نیز علاوه بر آن، به پنج سال حبس دیگر محکوم شد.
یونسی و مرادی از فروردین ۱۳۹۹ در زندان هستند و بنا بر گزارش‌های منتشرشده، در مجموع ۸۰۸ روز را در سلول انفرادی و بندهای بسته سپری کرده‌اند.
این دو دانشجو در پرونده اولیه در سال ۱۴۰۱ هر کدام به ۱۶ سال حبس محکوم شده بودند که در مراحل بعدی، میزان حبس قابل اجرای آنان کاهش یافت. با تأیید احکام جدید، هر دو همچنان از ادامه تحصیل و حضور در دانشگاه محروم خواهند بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78541" target="_blank">📅 18:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78540">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان قشم صدای انفجار از روی دریا اومد
قشم۱۲/۳۲ انفجار
وحید جان صدای انفجار از سمت تنگه میاد خیلی فاصله داره تا ساحل جزیره قشم تا حالا ۵ تا۶ شنیدم
از ساعت ۱۲  تا ۱۲۳۰
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/78540" target="_blank">📅 00:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78539">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIEHqpgeSFDoXY0L8HvADfddQRfQo8FjCv_qCY3kuXW2HhMCfGzKvvafZyJXTrhVgG4_6RKEfL3AXf8oVSQ7nUMVqJuX4e0vFkarm-E9Q9LB_-q5Mew6-XG5Qq5yYPmcO0Nl10n97n5VHqFB1N2rPEsMVnSwvGw5eJVtkxo_OAQwJrzBKH3hob1dKibYtsApktk1hWo5R5lV7sOuGzgR0b8oAUFjKFiTnmFeCV1deuUoXNi3Bvw4FoUQkmlxNZCIbFZJaUEeymrcGWVgnNdeTFQI_UIwO_bZJUrDCBr-nIelWo4s1vgiNm1AORVzbSvYNAi24mAPhG8xZQ3fZPdBUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وبسایت آکسیوس، روز ۴ مهر ۱۴۰۵، به نقل از یک منبع آگاه گزارش داد مذاکره‌کنندگان آمریکایی در جریان مذاکرات غیرمستقیم با عباس عراقچی، وزیر خارجه جمهوری اسلامی، به او اعلام کردند که ایران کنترل تنگه هرمز را در اختیار ندارد و بنابراین نمی‌تواند برای بازگشایی این آبراه شرط تعیین کند.
عراقچی در این مذاکرات شروط تهران برای بازگشایی تنگه هرمز و ازسرگیری مذاکرات هسته‌ای را به طرف آمریکایی ارایه کرده بود.
بر اساس پیشنهاد جمهوری اسلامی، تهران حاضر بود تنگه هرمز را بازگشایی و مذاکرات هسته‌ای را ظرف یک هفته از سر بگیرد، به شرط آنکه آمریکا محاصره دریایی بنادر ایران را لغو، تحریم‌های فروش نفت را رفع و آتش‌بس در سراسر منطقه را دوباره برقرار کند.
بر اساس گزارش آکسیوس، مذاکره‌کنندگان آمریکایی روز سه‌شنبه در جریان این گفت‌وگوها به طرف ایرانی اعلام کردند که جمهوری اسلامی کنترل تنگه هرمز را در اختیار ندارد و در نتیجه نمی‌تواند درباره بازگشایی آن شرط تعیین کند.
در حال حاضر ده‌ها نفتکش روزانه تحت حفاظت آمریکا از تنگه هرمز عبور می‌کنند و میلیون‌ها بشکه نفت را به بازارهای جهانی منتقل می‌کنند. با این حال، حجم انتقال نفت همچنان به‌مراتب کمتر از سطح پیش از جنگ است.
مسوولان آمریکایی می‌گویند طی ۷۲ ساعت گذشته حدود ۶۰ میلیون بشکه نفت از طریق تنگه هرمز منتقل شده است.
در همین حال، قطر و دیگر میانجی‌های منطقه‌ای برای ازسرگیری مذاکرات میان تهران و واشینگتن تلاش می‌کنند، اما اختلاف دو طرف بر سر موضوعات اصلی همچنان گسترده است.
جمهوری اسلامی خواهان تمرکز مذاکرات بر تنگه هرمز و محاصره دریایی آمریکا است، در حالی که دولت ترامپ بر دریافت امتیازهای هسته‌ای از تهران تاکید دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 458K · <a href="https://t.me/VahidOnline/78539" target="_blank">📅 22:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78538">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/aa5e4db158.mp4?token=ku2W43YZ0-wmG2R6s_F6Qewf4F2LV6GG7amaA1GQyhoLeKsd15ltOeIoNp-3gmduzRjRrUqytBPhIPXdBlg9epAyDFbgXrL9v1knsJf7HpN9fK0zB9I8tiP13SdYvpQxsJzVOdpXu-Sv9N8Ax7XsasneTkWCc5WLuEUISy9P0agIpNLENOA6u6Z1Z1jc9UtEaOS9eXw7DM8ES_ual6RQAUzz2Dd_hzSNHvTtx6UU4iOBc9rk-sTnC7uaYLHPj23ZiF9x2AWdaOYjLIXsCTtV-KIhoPsMiMce8XsrLY4qmZR5y4-d0bqWIIP1sSzRFS5D6CMumDvNRslT6Eu7wrEN5A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/aa5e4db158.mp4?token=ku2W43YZ0-wmG2R6s_F6Qewf4F2LV6GG7amaA1GQyhoLeKsd15ltOeIoNp-3gmduzRjRrUqytBPhIPXdBlg9epAyDFbgXrL9v1knsJf7HpN9fK0zB9I8tiP13SdYvpQxsJzVOdpXu-Sv9N8Ax7XsasneTkWCc5WLuEUISy9P0agIpNLENOA6u6Z1Z1jc9UtEaOS9eXw7DM8ES_ual6RQAUzz2Dd_hzSNHvTtx6UU4iOBc9rk-sTnC7uaYLHPj23ZiF9x2AWdaOYjLIXsCTtV-KIhoPsMiMce8XsrLY4qmZR5y4-d0bqWIIP1sSzRFS5D6CMumDvNRslT6Eu7wrEN5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز شنبه چهارم مهر تأیید کرد که پیشنهاد جمهوری اسلامی ایران برای بازگشایی فوری تنگه هرمز را رد کرده است.
ترامپ پیش از ترک کاخ سفید در گفت‌وگو با خبرنگاران گفت: «من پیشنهاد آنها را رد کرده‌ام. آنها می‌خواهند توافقی انجام دهند که بر اساس آن تنگه را فوراً باز کنند، چون به‌شدت در حال شکست خوردن هستند.»
او افزود: «ما با قدرت در حال پیروزی هستیم. کنترل کامل تنگه هرمز را در اختیار داریم و مقادیر عظیمی نفت از تنگه هرمز خارج می‌شود. دیشب ۲۹ کشتی از تنگه عبور کردند. آنها می‌خواهند توافق کنند و من هم با توافق مشکلی ندارم، اما آن توافق قابل قبول نخواهد بود.»
@
VahidHeadline
او بار دیگر گفت جمهوری اسلامی خواستار بازگشایی فوری تنگه هرمز است و افزود: «آنها هیچ پولی به دستشان نمی‌رسد، چون پولشان را از تنگه هرمز به دست می‌آورند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/78538" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78536">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hg_fqOeIIGLL7DcBSsyCxcZvi50C6hoN0VNOf3ks_7VrM_bZ-5PsHdiH7ZCyd_nd56hWRcmUTHeKrfVmPUs1JLrnWWWPe-eKEe2QVf0o1oUAxNK-YzlanlgkmLiwPVGMoSVzRa9LuGoV43vHixk7OnzefEOc8vHV4T9mQ6ogvBF4JiMY2nMV6biZeWFtV0QlqOZbAl7CSZNbETK1mKew6A4xM_A3rwn5MgJqfwaV91kj96qcfJo458gIRLSCn4iBH-MLqex7UbcSnRCXQbZ33Kkj7nr-t2t4Xl8RddX5q4sm6xE3Y3mwd9MPK8KlbeUm7na59U_k2UGMV-11XnE3Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/19b541c60b.mp4?token=pTVcdcCZRxBy7ZeDQyIwFCKMcum0KaHCgIj9Wz19skYMyrG1X4IKkOhSyAcqjCzbtIdvpnELBnLOVWTp2xY3MDEztSs_BbUodAPyFydy701_t9bhYjd4_O8gLv8afgkwE2gCCYSms5wud0Sc9woGzraj3cvjToOzrDbGdUla6bspaMiNuf0LsXInkvfsuXle_seH0vaKMP9perar_oE8GGY04cK5qVqkqx-OMGhdEXhpD6YueU3bp4hLljCN1nYB5XYiJ4zxk-5cu3MqH_eBH6b78MFWuGp3XEY1XiExrkH6ndtbMAZJYI9yqX9f2_Y_NrdvFws7sSyMq7_ueFfn4w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/19b541c60b.mp4?token=pTVcdcCZRxBy7ZeDQyIwFCKMcum0KaHCgIj9Wz19skYMyrG1X4IKkOhSyAcqjCzbtIdvpnELBnLOVWTp2xY3MDEztSs_BbUodAPyFydy701_t9bhYjd4_O8gLv8afgkwE2gCCYSms5wud0Sc9woGzraj3cvjToOzrDbGdUla6bspaMiNuf0LsXInkvfsuXle_seH0vaKMP9perar_oE8GGY04cK5qVqkqx-OMGhdEXhpD6YueU3bp4hLljCN1nYB5XYiJ4zxk-5cu3MqH_eBH6b78MFWuGp3XEY1XiExrkH6ndtbMAZJYI9yqX9f2_Y_NrdvFws7sSyMq7_ueFfn4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادستانی تهران در پی انتشار تصاویری از اجرای نمایش «تهران پاریس تهران/ پل»، علیه عوامل این اثر اعلام جرم کرد و پرونده قضایی تشکیل داده است.
مرکز رسانه قوه قضاییه شامگاه جمعه ۳ مهر ۱۴۰۵، بدون اشاره به نام نمایش اعلام کرد «رفتار خلاف عرف و شئون دو بازیگر در یک تئاتر روی صحنه» موجب ورود دادستانی تهران شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78536" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78535">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phaffM9ZsxKhozFxrXCH1mlMQd8mPmagvIISwUFoA3i1q-g4IQpvjzCCCL-TqOeQXTbc9u2ZhQgOJRBN-8FobY7--U6BeDJjQ6GTlfkarCDWhCWVTK_I9OBs67D_aNIKj2niXluTouKgbNUnu1v0Eog4EI0u8SQtU6vW3UItkkmsyBeQvAxKaifNrBJ-s7o4A_3jN-97hMh7457dx86R1xVXQMW0rlRyaiepeoSHX7MCMAw2BN9DUBEbtXd75ytpLf7eewdvV8p00jEVHKSTQIG7Ci2pafpS1SXXF4QH56pQO9rFkKguYMDi4XqaTNB8F83C4ywhljxDyMTW5mAbHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محبوبه شعبانی»، از بازداشت‌شدگان اعتراضات دی۱۴۰۴ در مشهد، به اعدام محکوم شد؛ زنی ۳۳ ساله که براساس گزارش‌های منتشر شده، در جریان اعتراضات با موتورسیکلت خود به انتقال معترضان مجروح به مراکز درمانی کمک می‌کرد.
هرانا خبر داد شعبه اول دادگاه انقلاب مشهد، شعبانی را با اتهام «اقدام عملیاتی جهت تحکیم اسرائیل، آمریکا و عوامل وابسته به گروه‌های اپوزیسیون» به اعدام محکوم کرده است. به نوشته هرانا، حکم امروز به وکیل او ابلاغ شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78535" target="_blank">📅 17:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78534">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JorjSShweoSABVWPsvksz93P-poxij7TgWav2R03YE8D6Ox2fjJ_CUifmV0frQ8PFvqcto4F9zaK8XQPmcEEfBJfTYAiceS5nw90UzbWaqoAsHYYQJ4PPl9JZWaalTU2kK5FMhM3s5oJbk5QwaUO9i8C7vqgGhT0cBG5zFMCbeFQgIPOSuRAmXfbc9b5zQnbHmcWK7YNPFud5SgNExGkQ0QMC_VruzuadqrwfuPnWvg0LIU_Y6FAN7c4IzO7Y7_2njZE330x3NTm9xr26p7-ejRPoXy4Kunm-LsVO0c07KJOW7-XjMHPSyez33VZznhxFUcRKINhW8HNlzVLGoggMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«امیرحسین موسوی»، زندانی سیاسی محبوس در زندان اوین، در شعبه ۱۵ دادگاه انقلاب تهران با دو اتهام «محاربه» و «افساد فی‌الارض» روبه‌رو شده است؛ اتهام‌هایی که می‌توانند به صدور حکم اعدام منجر شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/78534" target="_blank">📅 17:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78532">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hiB4gWSOw_pgDt1ieq3r1v-lk1mO-GqDxOdYv4PNma3phAj71P7qnkFACKjbyiwftxIrIuDHOsXmjk9-6osyCnVYmjBGHncsCH2HcSLfj7nLybBDkKV7Mf6aTWSUpqPPPlcMqEdfJVXWdX-Wx_Szo-ReypyqkVBAvr-d903Uue3wosDcLKQPqJWAsVuDwx9YGLHnknrzL34Ogz3jTAJbNukNBuVdezL9BRmGPpvSdcYV5OGCID0k32N3HxDjYUG48axaVYy_PDtdA2IYfeghiYjV1T4aPeUPNWtqtdpAfWHkdEMzJU9kpU6OpwRBUKRezMyWqv3vUL8J1uJTwmWE-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f732caa14c.mp4?token=tcKdpMiTItKh-2ScRLarYu3ecxHpVQvFh3t9501T34aaLaxOAht3w7tdTctp5qSQVOSVbdFPxd9gQBqNWPTULrN679fJoMlbWQIo-Bvprjj9cwDHHRklTyNZkWPomRY0FN-QV0Y9S8fDAmThs0YUPOUdVKNEFAEgkFDTlCzpRRVdZEj7Ltlgzivo7Y6wWPoL7YbLKGrXU5fTBr39nt0zaaOEVYLtj8cDylFg9DXQsUQ3yV2tyhU3oTepsFLXqVsHQ3sHXbTD3cnqM6ltUiQpYMF_dkd6BjHlx2c-_XQdSHYOIhkx5IZCmTwvO8lZ47Rc9aXnHCsvanR3dUyYz5pALw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f732caa14c.mp4?token=tcKdpMiTItKh-2ScRLarYu3ecxHpVQvFh3t9501T34aaLaxOAht3w7tdTctp5qSQVOSVbdFPxd9gQBqNWPTULrN679fJoMlbWQIo-Bvprjj9cwDHHRklTyNZkWPomRY0FN-QV0Y9S8fDAmThs0YUPOUdVKNEFAEgkFDTlCzpRRVdZEj7Ltlgzivo7Y6wWPoL7YbLKGrXU5fTBr39nt0zaaOEVYLtj8cDylFg9DXQsUQ3yV2tyhU3oTepsFLXqVsHQ3sHXbTD3cnqM6ltUiQpYMF_dkd6BjHlx2c-_XQdSHYOIhkx5IZCmTwvO8lZ47Rc9aXnHCsvanR3dUyYz5pALw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در  دو واقعه جداگانه دست‌کم ۲۰ نفر کشته شدند:
یک دستگاه اتوبوس مسافربری بامداد شنبه ۴ مهرماه در آزادراه همدان ـ ساوه واژگون شد و بر اساس گزارش مقام‌های امدادی، ۱۱ نفر از سرنشینان جان باختند و ۲۴ نفر دیگر مصدوم شدند.
@
VahidOOnLine
برخورد یک اتوبوس مسافربری با تریلی حامل میلگرد در محور بیرجند ـ قاین در استان خراسان جنوبی ۹ کشته و پنج مصدوم بر جا گذاشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/78532" target="_blank">📅 17:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78531">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhp5ud_ZsHlCSo-pg4zMWKBYEZRfTjDBKN7HkiRAGBTST-z4OG_eK1B_jF9za7fA1n1oBi1l8omBZsVyKLXBGf8youCFKrAgjMwANw1eeFtDJw71KnJumTJBjqIG7het7clmo5GrUh4NPsbwRzThEU0OHxVX_z5BepAniQrqZ24dJyYxwgDJ0u57zuzGbLypXfBFxHtDeuERHor9koLjNWlr1fkpzFoi7U-kegN9mBDGJbTKEvTidOcMyD8W0Q2oN4Ik6O_YpFOEUicuJeyLHYH3SaFcfxw4qIbj1T6VlPDfJwoYphGRrJgNdQnScLIyvQEAshwYTugQZ1GhVAlzvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه تجدیدنظر استان قم حکم ۷۴ ضربه شلاق پرستو احمدی و هشت نفر دیگر از نوازندگان و عوامل «کنسرت کاروانسرا» را بدون تغییر تأیید کرد.
ابوذر زمان، وکیل دادگستری، روز جمعه در شبکه اجتماعی ایکس نوشت بر اساس رأی شعبه ۱۶ دادگاه تجدیدنظر قم، پرستو احمدی، چهار نوازنده و چهار نفر دیگر علاوه بر ۷۴ ضربه شلاق به دو سال ممنوعیت از فعالیت در امور سمعی و بصری و ممنوعیت از خروج از کشور محکوم شده‌اند.
دادگاه کیفری استان قم پیشتر این ۹ نفر را به اتهام «جریحه‌دار کردن عفت عمومی از طریق تولید و انتشار محتوای مبتذل و خلاف اخلاق در بستر فضای مجازی» محکوم کرده بود.
پرستو احمدی در آذر ۱۴۰۳ ویدیوی «کنسرت کاروانسرا» را که بدون حجاب اجباری و با همراهی احسان بیرقدار، سهیل فقیه‌نصیری، امین طاهری و امیرعلی پیرنیا اجرا شده بود، در یوتیوب منتشر کرد.
قوه قضائیه پس از انتشار این اجرا علیه عوامل آن اعلام جرم کرد و احمدی و دو نوازنده همراه او نیز برای مدتی بازداشت شدند.
در رأی بدوی، دادگاه پوشش پرستو احمدی و همچنین تولید، تصویربرداری و انتشار عمومی این اجرا در فضای مجازی را از مبانی صدور حکم عنوان کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/78531" target="_blank">📅 17:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78530">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dsGjWgzDJ1DELh-2lRBSgLJJGcWxt8Dhq_f6XuJ70HRsXtTzS1WPNiX19Dh29_QvafQ2qG7l6TdoOnbq8oYZWx9L5GKl_BjYcYijkzNXd3gJswchrzT70X4tQ0S_5TdX9EJyDNdPc7whtFUvAbV5luHdDvp-6UvI6B_08k97fQezCf4aLVlVhGOvmQlyYCJChaBukQZpJcYayJzN8yGC_t4A9w9ODQU3unKstR5GWxWr0khVVisMOuVKBqIINT03BQFn69TOVsk_O24nSyF2MVJVmXZLNU1SV3bCylldjWp6nUY9kxAAKYCunxQiO6hSziPmBi_e-Hprdm25q06SwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه وال‌استریت ژورنال به نقل از «مقامات آمریکایی» گزارش داد که رئیس‌جمهوری آمریکا، پیشنهاد جمهوری اسلامی برای برقراری آتش‌بس هفت‌روزه را رد کرده و به دستیاران خود گفته است که انتظار دارد پس از انتخابات میان‌دوره‌ای ماه نوامبر، بمباران را از سر بگیرد.
دونالد ترامپ بارها هشدار داده است که در مورد تاسیسات هسته‌ای «کوه کلنگ» ممکن است دست به اقدام نظامی بزند.
وال‌استریت ژورنال می‌گوید که پیشنهاد جمهوری اسلامی شامل بازگشایی تنگه هرمز و ازسرگیری مذاکرات هسته‌ای در ازای لغو محاصره بنادر ایران توسط ایالات متحده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/78530" target="_blank">📅 05:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78529">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezMu2ASgSKNnPoY32U2Fd3ODUZpVW-mQmxaGM0SP-BaktCf8QbD_l1psWawuipWPseMD_RUdJoi8vzM6ScGYD2br4lrTuBbYRBf7xoqDn_pH2YFZAEC7ggo22rDD4G-3GbLqzRDq5Ip_nrNakIKTr1aT4-ku4ZIAb_mBbA1tHj1Lbz0K6wrkLBg8p_lt-ny8djnY28F-v1VjH0SVJF8CrR448pl7d4Rch_iFpRoMVzBR_Tm26U7_IrHnll5xd8D1eYU2AQ79uZC9tfqznG1I6XGvlZPaXg-r2LlRg2CbtazZXjf3W7SaY7WjMR8hSvggfKgwT3fTg6bhnFAB_HSNwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مخبر، مشاور رهبر جمهوری اسلامی ایران، هشدار داد که در صورت تداوم محدودیت‌ها و قطع خدمات فرودگاهی برای پروازهای ایرانی، هیچ‌یک از کشورهای منطقه نیز اجازه نخواهند داشت از خدمات پروازی بهره‌مند شوند.
مخبر روز جمعه، سوم مهر در شبکه اجتماعی ایکس نوشت: «همسویی با آمریکا در اجرای سیاست‌های خصمانه در خاطر ملت ایران ماندگار خواهد بود، هر چند راهبرد ما در این مورد مشخص است: پرواز در منطقه یا برای همه آزاد است، یا برای هیچ‌کس.»
پیش از این محسن رضایی نیز تهدیدهای مشابهی را مطرح کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/78529" target="_blank">📅 17:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78528">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eL-rgojX7lRjEFatFA1WCZpoBqwCKqDfxam6dp-ikH1z95rYVy3Q4V_k4uRuo_8ykmy29wpMDoslipd3pQgBF88H167PMfETi7KQXGYX_7sQxMXtxPba1qWJLUzx_sXccfRNi1O7pwjUjZsyOW10IKWTq4VUsINUWnQTk16akJKz6jwFVYZazDQuGmMKXOql4RpH1QDzrchDMDOgMtka39c4ltLtUPQRIwgyYRwBqvL351OgseYELJSil_GL5IGoCsffR79DdDl7yoqzueX6g2AJ08TAcXTFessrtv2MxmfzEVjGDrPN8qnCjLwyElQsGxACNjiYfew7R_Rq5YMOUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع مطلع خبر داد که فرودگاه‌های اربیل و سلیمانیه در اقلیم کردستان عراق از روز جمعه سوم مهرماه پرواز هواپیماهای ایرانی را معلق کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/78528" target="_blank">📅 17:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78527">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfRo3eBdTeIJfoTNwSRjdFWFhyTPzOFVHSIiDC7ASck6LcCsmWiMobVa0Oun5YSiG1jloMyS69RicTg5qZC26t29zzG5lQb25kdWa_rHfw0ClQz8ceK6VnNvXwwkRNP7V9P2TGnbL9HDyQv9t_u5kQk3S8Hq8XN3R6z5HI0Q8yOIOkWjwf_ZA1DIkFa3EYTjsWYcb6GBtPkPrFNYIO6puU_x5E4mHlapEO_R24qbB7TTwK2PCjz3NdQ0ar37PhoqThBNWGvv4ITQIQrGfLjaOaTbT0AP_LTxLJtc_CRYV3VWLg_Vw8F9Jg3JSBoL9RvoDhmki_p7wt4EFqOb4ivwmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی عراق از توقف تمامی پروازهای ورودی و خروجی از مبدا و به مقصد ایران، از فرودگاه بین‌المللی نجف خبر داد.
مدیریت فرودگاه نجف با صدور اطلاعیه‌‌ای اعلام کرد: بر اساس دستورالعمل‌های رسمی صادرشده از سوی نهادهای ذیربط، تصمیم گرفته شد تمامی پروازهای فوق، از ساعت دو بامداد روز جمعه سوم مهرماه تا اطلاع ثانوی متوقف شود.
پیشتر فرودگاه بین‌‌المللی بغداد نیز از توقف پروازهای ایرانی خبر داده بود. این اقدام در پی تحریم‌‌های اعمال‌شده از سوی ایالات متحده علیه خطوط هوایی جمهوری اسلامی اتخاذ شده است.
روز پنجشنبه نیز فرودگاه‌های امارات به همراه برخی از کشورها از جمله ترکمنستان و آذربایجان، از اعمال این تحریم‌ها خبر دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78527" target="_blank">📅 17:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78526">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwVIypSoWYiiWKc1Tbpgl-MS1LDQaQtQU87FpCOq366xpIHDF66P83mqkNyLMW6-5peZz-QkcuOUJ6EhGvAh434ugdctfA_TH_Mj9XL0ZuTZ04DY18fC-1Bt9HyBAnLbuSueKjYvnUBjr9IQ29OLTifM0hip2LKjOLcUB3r-vQ4EnYnmw4TKAGKmtz2nbpPH1cnXvpD6ZDT-nS-aaPEyXUNSPNFik9MwPOxeKA_TWMtOS8rkFkdLhwOaZKQbGMjyw-8R5RtmgoAJJ7AD6S2FjS8VckE0MScLktni3TPOySvHrYDpCCZVdXTI0Ef1KGfqG9scF4wFLDUVEVgYZQ48KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه اسکای‌نیوز می‌گوید وزیر امور خارجه بریتانیا در دیدار با همتای ایرانی‌اش به او گفته است که بریتانیا «ارعاب، تهدید یا اقدامات خصمانه در خاک خود» را از سوی گروه‌های وابسته به ایران تحمل نخواهد کرد.
اسکای‌نیوز این گزارش را روز پنج‌شنبه دوم مهر به نقل از منابعی در وزارت خارجه بریتانیا منتشر کرده اما منابع رسمی دولت هنوز آن را رد یا تأیید نکرده‌اند.
اد میلیبند و عباس عراقچی روز پنج‌شنبه در حاشیه نشست مجمع عمومی سازمان ملل متحد با یکدیگر دیدار کردند.
وزارت خارجه ایران می‌گوید عباس عراقچی در این دیدار از اقدامات آمریکا و اسرائیل انتقاد کرده و گفته است ناامنی منطقه و تنگه هرمز پیامد حملات نظامی آمریکا و اسرائیل «با حمایت برخی کشورهای اروپایی» است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78526" target="_blank">📅 17:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78525">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJw8zMWXdh-WnQlNBkw7iXHMupdsPXeUCM9zGgo075EUMsBjLmfKbYqrSKvDoqv8p9WNraf0aDSvN7RjmQiOOOChxhsBYmNr1j6vI-k4FtXgCUuaHHJGwV8ec5MKK3a3JBiWpU2pb3t_jVgGYytpAo9bTDMMJCiWQYQIz7BTXyx5dj4MvZHxW5Nh97sbK3w99sybJH832zWQaGFExtVDByok_8-N9lGKNVwdNOvJmXEi-Db8Pe2cd6mh60B7Hsm3qx77okKXL0i1udjCdAX121A3hG1PYvJ-pNHGLM1tH2R4fee8YSLVKy2TrkzIrc6g-yZonqX66LESipMz8LdQcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور فرانسه از اعزام نیروها و تجهیزات نظامی این کشور برای محافظت از یکی از تأسیسات نفتی عربستان سعودی در مقابل حملات خبر داد.
امانوئل مکرون روز پنج‌شنبه دوم مهر در یک گفت‌وگوی تلویزیونی اعلام کرد که فرانسه در پی حملات شبه‌نظامیان حوثی یمن، «تجهیزات و نیروهای نظامی» را برای کمک به حفاظت از بندر راهبردی «ینبع» در عربستان اعزام خواهد کرد.
او گفت: «ما برای حفاظت از این تأسیسات، امکانات نظامی شامل نیرو، رادار و سامانه‌های دفاعی اعزام خواهیم کرد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/78525" target="_blank">📅 17:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78524">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FF9sq-LEzQPZoSb1ZcZP5O9wDoDJQVnmcudGR2fiDzTsgSPGG7HyCHuVqpsK1T0Fw4peMgUyIm2t4u_7WwoAtGBX1q1AkT_tMp96xLv14J5be_GroKXvahwllAqrwW8qYkgkNiaSIffo-_lDRWh0gPqOFIEBleSEuNxAZ1Hjux0OTqU854_Nxe25GtEMuxptxxxPY4yfxqs4nDsnPgn5-TRFBjm9M-icex_S_bQRiuAdoC4G31vRihGmL7vwmX95LuzA2ekUgLqTr2GVfRQoa39cfqkrPlomZkEvF_ojfKc_FFmSHvlvDqIcQRwY6MZJQ1dhA3LUeO3NpOEQyauUOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر کل ناتو با اشاره به تشدید تحریم‌های اقتصادی آمریکا علیه جمهوری اسلامی اعلام کرد مردم ایران هر روز آن را احساس می‌کنند، اما برای رژیم حاکم ایران منافع مردمش اهمیتی ندارد.
مارک روته در گفت‌وگو با فاکس‌نیوز تصریح کرد دولت دونالد ترامپ با حملات خود، برنامه هسته‌ای و موشکی جمهوری اسلامی را که «تهدیدی برای اسرائیل، خاورمیانه و اروپا» است تضعیف کرده و اکنون فشار اقتصادی بر جمهوری اسلامی را تشدید کرده است.
او در پاسخ به سوالی درباره اظهارات بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل مبنی بر اینکه بزرگترین ترس جمهوری اسلامی از مردم ایران است، تصریح کرد که به نظرش این حرف درست است و مردم ایران از دست حاکمیت به ستوه آمده‌اند.
بیشتر بخوانید
.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/78524" target="_blank">📅 17:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78523">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAD0Bkzy8d24Wcl-pgt6cLEJEmifWmyhHmRrRRWAqVh0nH_KCpa1_DqUBflq79yhFQpmI0GHrchOzLmkm4nMrlI-8mfDwscqKY4LdgBIxGKGlUjYf93-6kOmERVN7flJlFYughIWlbdq4CxTBpDOLh98yIHYWvJGPX_1z-p_nnYq-HmtI9URqqt7oc53t8zZbiubLVH_QFfr6U8AVsdhPli5_mF0nIFAsTUtFUi8vx1zZwU4CAG0geovjwsvY1Gp8qiNnN6MsLZ7CU1U1VrU_qqrVOHjnD6WfwDFqwt0jWdvFmBXUbeRZIIAKrv64deq-XS4sSSse2U1VLGGYmLDaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت کلمبیا روز پنج‌شنبه دوم مهر از قطع روابط دیپلماتیک این کشور با ایران خبر داد.
در بیانیه دولت کلمبیا گفته شده است این تصمیم بر اساس ملاحظات مربوط به «امنیت ملی در سطح نیم‌کره» گرفته و از روز ۱۹ سپتامبر (۲۸ شهریور) اجرایی شده است.
کلمبیا در بیانیه‌اش حکومت ایران را به داشتن ارتباط با «گروه‌های نارکو- تروریستی» متهم کرد که به‌گفتهٔ کلمبیا امنیت این کشور را تهدید می‌کنند.
دولت کلمبیا همچنین تهران را به دلیل مسدود کردن تردد در تنگه هرمز و حمله به سایر کشورهای خاورمیانه در جریان جنگ با ایالات متحده و اسرائیل، به شدت مورد انتقاد قرار داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/78523" target="_blank">📅 17:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78522">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iD5U0IVCJLo3PXNrCYzGkDeLKWPQDsyHt03NTKV45wGW0eIuMA-6eLqhMUhkKWR0jOvzGizH_wGlGenj-bSzTOm07cY5iunvFfpVgGAOnAOssJVEOVj3HdRl-mJLtF7krMFGmcyEPPv4lo7NqSDbOz4j2TpACr53MPaRjkeWh7z3WlfxYAaofqfDzUO0a7EmxLX_0GCbHtg2v6IOXkDZa69xEMzYkxPRCg7ZuFQu74rRjqKMhSjdKIEF_EJ3UFQA9Ff5MNhMD93Ek5w43OMNTwlCVoA4hEDidfS8mqebkwbJgC9FOPNmIUhuyKwEBs5zEIRrVCyYxx2-BOHjMV33SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه بریتانیایی جوییش کرونیکل در گزارشی روز پنج‌شنبه دوم مهرماه از محاکمه غیابی هفت ایرانی و یک شهروند لبنانی از جمله محسن رضایی، دبیر شورای عالی امنیت ملی و احمد وحیدی، فرمانده کنونی کل سپاه پاسداران جمهوری اسلامی در پرونده بمب‌گذاری سال ۱۹۹۴ مرکز یهودیان آمیا در بوئنوس‌آیرس خبر داد.
بر اساس این گزارش، دانیل رافکاس، قاضی فدرال آرژانتین، با صدور حکمی ۶۴۸ صفحه‌ای، اتهامات هشت متهم را به‌طور رسمی ثبت و دستور مسدود شدن دارایی‌های هر یک تا سقف ۵۰۰ میلیون دلار را صادر کرده است.
احمد وحیدی، فرمانده کل سپاه پاسداران، و محسن رضایی، دبیر شورای عالی امنیت ملی، در کنار علی فلاحیان، علی‌اکبر ولایتی و چند مقام و دیپلمات پیشین جمهوری اسلامی از جمله متهمان این پرونده هستند. قاضی اتهاماتی از جمله قتل و جراحت با انگیزه نفرت نژادی یا مذهبی را مطرح کرده و بمب‌گذاری را جنایت علیه بشریت و نسل‌کشی طبقه‌بندی کرده است.
مرکز آمیا تاکید کرد حق دانستن حقیقت، دسترسی به عدالت و تعهد بین‌المللی به تحقیق و مجازات جنایات علیه بشریت نباید به‌دلیل پناه گرفتن عامدانه متهمان در خارج از کشور بی‌اثر شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/78522" target="_blank">📅 17:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78521">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37b765df18.mp4?token=Gfz5QA6u9742ttYjLqteQDAjHYH9eUl10WMENYGXpGNDV0Cq0ImLlVLwtCN9wyz1hpsHdmY6nJKZAnhQg944kqMwouurNU-s8vrjDPiIyB0nrKQ30N0tA0x7OgGg2GaRfuIZ4Fd-svyLIiN04voIuujXthv6BVaEqtBbz7i8HJWqnsAqyPuAaTn9CzDVhKq1zk7o3_joa0aKUn0crbRvDIevOAj1cpPBO3pdPiImLqliJYftUlESgffkhCJEu3UCOR7epvTVadvZlTSDm9rMH8bUM01Rmq5dghuPn14X4EGOujTnQvRcG_M2Jgqh21BkkTNVDMKIh6ojhiqVtsHxqw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37b765df18.mp4?token=Gfz5QA6u9742ttYjLqteQDAjHYH9eUl10WMENYGXpGNDV0Cq0ImLlVLwtCN9wyz1hpsHdmY6nJKZAnhQg944kqMwouurNU-s8vrjDPiIyB0nrKQ30N0tA0x7OgGg2GaRfuIZ4Fd-svyLIiN04voIuujXthv6BVaEqtBbz7i8HJWqnsAqyPuAaTn9CzDVhKq1zk7o3_joa0aKUn0crbRvDIevOAj1cpPBO3pdPiImLqliJYftUlESgffkhCJEu3UCOR7epvTVadvZlTSDm9rMH8bUM01Rmq5dghuPn14X4EGOujTnQvRcG_M2Jgqh21BkkTNVDMKIh6ojhiqVtsHxqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دنی دانون، سفیر اسرائیل در سازمان ملل، در ویدیویی که منتشر کرد، یک دستگاه استارلینک را به ناصر اسدی، نماینده جمهوری اسلامی، پیشنهاد داد و گفت: «می‌خواهید آن را بگیرید و به تهران ببرید؟ می‌تواند در ایران برایتان بسیار مفید باشد.»
دانون در این ویدیو می‌گوید: «فکر کردم مناسب است این استارلینک را به شما بدهم. اگر سخنان نخست‌وزیر را شنیده باشید، می‌تواند بسیار به کارتان بیاید تا پس از آنچه با مردم ایران کردید، اجازه دهید به آزادی برسند.» او همچنین گفت: «ما مردم ایران را دوست داریم و برای تغییر رژیم در آنجا دعا می‌کنیم. آن روز خواهد رسید.»
این همان دستگاه استارلینکی است که بنیامین نتانیاهو هنگام سخنرانی در مجمع عمومی سازمان ملل نشان داد و از رئیس جلسه خواست آن را به هیات جمهوری اسلامی بدهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78521" target="_blank">📅 06:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78520">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scksXwkFiuzV4whF_iwSD1O-17bEx1pbxLrUogzxiqaYBcmpTVRPw-flYKQr7EBM6UfnCD5h2UaaI7sWC31f8ZmnubOLZ_cQfV271c8hwhynAcMtKM8JxInU8-pV42M0I6W6l963FALVm5nffJhsLufGZtn8r9X8vgO4GCw0rm5RgZtiT7dvGjiwW-Lrh3aVaEORKksqjfADmPVhMmkP_kbS_hRm9c3dpOuLW0x27M-TJF_MtcHPI2dI9cRedYL7MZH1_DVaIS1pbplmp9VLp1Sksq-SzAZfUsTYXdS4pMcC0w-ZkEDIEiFUvrshsjj6n8cZIrdW9urDKGr509pKtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش سی‌ان‌ان، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران، پنجشنبه دوم مهر گفت تهران پیشنهادی به آمریکا ارائه کرده است که می‌تواند به بازگشایی تنگه هرمز و ازسرگیری مذاکرات برای دستیابی به یک «توافق نهایی» منجر شود.
عراقچی گفت این پیشنهاد در هفته جاری از طریق میانجی‌ها به واشنگتن ارائه شده و بر اساس آن، آمریکا باید ظرف هفت روز شروط مشخصی را اجرا کند تا مذاکرات از سر گرفته شود و تنگه هرمز بازگشایی شود. او جزئیات این شروط را بیان نکرد، اما گفت این موارد «چیزی بیشتر» از مفاد تفاهم‌نامه اسلام‌آباد نیستند.
بر اساس این گزارش، تفاهم‌نامه اسلام‌آباد که در خرداد میان ایران و آمریکا به دست آمد، شامل کاهش تحریم‌ها، آزادسازی دارایی‌های مسدودشده ایران و توقف عملیات نظامی، از جمله در لبنان، بود. یک مقام کاخ سفید نیز در واکنش به اظهارات عراقچی به سی‌ان‌ان گفت گفتگوها از طریق میانجی‌ها «مثبت و سازنده» بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78520" target="_blank">📅 06:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78519">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مسعود پزشکیان در مصاحبه با فاکس‌نیوز، از آمادگی جمهوری اسلامی برای توافق و کاهش غلظت اورانیوم غنی‌شده خبر داد، اما درباره محل نگهداری ذخایر هسته‌ای و تضمین تبعیت سپاه از توافق، پاسخ روشنی نداد.
مجری این شبکه همچنین با اشاره به کشته‌شدن معترضان و حملات نظامی برخلاف وعده‌های رییس‌ دولت جمهوری اسلامی، پرسید: «چه کسی در ایران حکومت را در کنترل دارد؟»
پزشکیان در این گفت‌وگو تاکید کرد جمهوری اسلامی خواهان جنگ نیست و مدعی شد جنگ به ایران تحمیل شده است. او گفت تهران آماده دستیابی به توافقی در چارچوب حقوق بین‌الملل است، اما فشار برای وادار کردن جمهوری اسلامی به تسلیم را نخواهد پذیرفت.
او با اشاره به توافق و تفاهم‌نامه‌ای که به گفته‌اش پیش‌تر با طرف آمریکایی امضا شده بود، از تمایل به ادامه همان مسیر سخن گفت و آمریکا و اسرائیل را مسئول حملات و کشته‌شدن رهبر پیشین جمهوری اسلامی، فرماندهان، دانشمندان و مقام‌های دولتی دانست.
بخش مهمی از مصاحبه به میزان اختیار پزشکیان بر نیروهای نظامی اختصاص یافت. مجری با کنار هم گذاشتن وعده خودداری از اعمال زور علیه معترضان، عذرخواهی از کشورهای همسایه بابت حملات و اقدام فرماندهان علیه کشتی‌ها بدون اطلاع «رییس‌جمهوری»، پرسید چرا تعهدهای او چند بار نقض شده است.
پزشکیان ابتدا به آمار کشته‌شدگان اعتراضات پرداخت. هنگامی که مجری دوباره پرسید چه کسی تضمین می‌کند سپاه از توافقی که او امضا می‌کند پیروی کند، گفت قرار بوده گروه‌هایی برای هماهنگی، رفع سوءتفاهم و ایجاد کانال ارتباطی تشکیل شوند، اما فرصت راه‌اندازی آن‌ها فراهم نشده است. او همچنین نیروهای آمریکایی را به شلیک خودسرانه در منطقه متهم کرد.
مجری در ادامه پرسید: «چرا رییس‌جمهوری ترامپ باید با شما مذاکره کند و نه با فرمانده سپاه، ژنرال وحیدی؟» پزشکیان در پاسخ، از بی‌اعتمادی عمیق میان تهران و واشینگتن و خروج ترامپ از برجام سخن گفت، اما توضیح مشخصی درباره حدود اختیار خود در برابر فرمانده سپاه ارائه نکرد.
مجری با اشاره به آمار نهادهای حقوق بشری و گزارش مجله تایم، پزشکیان را به چالش کشید و پرسید: «شما جراح قلب هستید. چند نفر از ایرانیان در ایران توسط نیروهای امنیتی کشته شدند؟»
پزشکیان بار دیگر آمار رسمی منتشر شده توسط حکومت را تنها آمار واقعی اعلام کرد. او گزارش‌های خارج از کشور را مغایر اطلاعات حکومت دانست و خواستار ارائه مدارک هویتی قربانیان شد. در عین حال، از ضعف مدیریت رویدادها ابراز تاسف کرد و گفت استفاده از سلاح در تظاهرات خیابانی پذیرفتنی نیست.
ادامه گزارش :
pezeshkian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78519" target="_blank">📅 05:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78518">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ویدیوی کامل با ترجمه ماشین
بخش‌هایی در خبرها:
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل گفت: «می‌خواهم با دقت به سخنانم گوش کنید. روزی، و شاید آن روز چندان دور نباشد، مردم ایران آزاد خواهند شد.»
او افزود: «حکومت آدم‌کش آنها به‌دلیل دروغ‌هایش، فسادش و بی‌رحمی‌اش سرنگون خواهد شد. این حکومت شرور سقوط خواهد کرد و همه ما آن روز را جشن خواهیم گرفت.»
@
VahidOOnLine
بنیامین نتانیاهو در بخش پایانی سخنرانی خود در مجمع عمومی سازمان ملل متحد، بار دیگر به خروج نمایندگان کشورها از سالن و حضور معترضان در مقابل ساختمان سازمان ملل واکنش نشان داد. او با یادآوری سرکوب اعتراضات در ایران، خطاب به این افراد گفت: «زمانی که رژیم ایران هزاران نفر از مردم خودش را کشت، شما کجا بودید؟ شما درباره مردم ایران هیچ چیزی نگفتید.»
نتانیاهو در ادامه تاکید کرد: «اما باوجود سکوت و ریاکاری شما، نیروی مردم ایران چیره خواهد شد. فقط مساله زمان است. یک روزی که شاید خیلی دیر نباشد، مردم ایران آزاد و پیروز خواهند شد و این رژیم پلید سرنگون خواهد شد و همه ما آن روز را جشن خواهیم گرفت.»
@
VahidOOnLine
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل گفت: «مستبدان تهران؛ می‌دانید از چه چیزی بیشتر از همه می‌ترسند؟ از مردم خودشان؛ مردم شجاع ایران که برای مدتی طولانی، فداکاری‌های بسیاری کرده‌اند.»
نتانیاهو افزود: «از معترضان بیرون و نمایندگان ریاکاری که این سالن را ترک کردند می‌پرسم: کجا بودید وقتی مستبدان ایران ده‌ها هزار غیرنظامی بی‌سلاح ایرانی را کشتند و مجروح کردند؟ وقتی هزاران نفر از مردم خودشان را کشتند و مجروح کردند، کجا بودید؟
آیا تجمع‌های گسترده برگزار کردید؟ اعتصاب غذا کردید؟ آیا مقابل نمایندگی ایران در سازمان ملل اعتراض کردید؟ آیا در دفاع از مسیحیانی که در ایران و سراسر خاورمیانه تحت آزار قرار دارند، سخنی گفتید؟ نه. چنین کاری نکردید، زیرا شما معترضان قلابی حقوق بشر هستید.»
@
VahidOOnLine
ده‌ها نماینده حاضر در مجمع عمومی سازمان ملل متحد روز پنج‌شنبه ۲۴ سپتامبر، همزمان با آغاز سخنرانی بنیامین نتانیاهو، نخست‌وزیر اسرائیل، سالن را ترک کردند.
نتانیاهو در واکنش، نمایندگانی را که سالن را ترک کردند «بزدلان بی‌اخلاق» خواند و از دیگر افرادی که قصد خروج داشتند خواست پیش از آغاز سخنرانی او سالن را ترک کنند.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل گفت: «قطر میزبان عاملان کشتار هفتم اکتبر حماس است. اکنون تازه‌ترین کشوری که به عامل گسترش گسترده دروغ‌های یهودستیزانه تبدیل شده، ترکیه است.»
او افزود: «اردوغان یک مستبد است. او نیز میزبان رهبران تروریستی حماس است. او هزاران غیرنظامی کرد را کشته، نسل‌کشی ارامنه را انکار می‌کند و روزنامه‌نگاران و رهبران مخالف را زندانی می‌کند. در واقع، فکر می‌کنم در این زمینه رکورددار جهان است و البته رقابت سختی هم وجود دارد. اما فکر می‌کنم او نفر اول است.»
نتانیاهو گفت: «او به‌طور غیرقانونی قبرس شمالی، بخشی از کشوری عضو اتحادیه اروپا، را اشغال کرده و به‌طور مرتب علیه یونان، عضو ناتو، دست به اقدام می‌زند. اکنون می‌خواهد سوریه را تصرف کند.»
او افزود: «البته این تعجب‌آور نیست، زیرا تقریبا هر روز خواستار نابودی اسرائیل می‌شود. او می‌گوید قرار است حاکم اورشلیم شود. نه آقا، نخواهید شد. این کشور ما، شهر ما و پایتخت ابدی ما است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78518" target="_blank">📅 23:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78517">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/475bcac205.mp4?token=Zi3KPE9s1GAiHKKkParlNGXzrCEU8Dc0ReLoOrff-QX1GLI_B3Ur3yObYnji_BeU2I_8SG_irD2egGRG3xWTuJhm2bKL0aduIUsr90tsh2Qj6Sh3yLYmAIXzF6_NbEyOtPXWtJ_bmsSpqLGBkP75rZ4NQrmz_ZH-502qg_ZmB4JkIRwky9IWDYqAzLm2iljvvSrYjbHx2j3WoSZ0HBbRhVw4q6HyWWd8mv4Y5ZIsvkkyAo7MiDAfxUcYAV53NUnl3T8wrAxehx7wEfg3A5gXONnv201QKJ34WVTB-pdz-QzcEoxukhc4PslTW3nKsxxHCocflwSEXOtlLFxMwpLWqg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/475bcac205.mp4?token=Zi3KPE9s1GAiHKKkParlNGXzrCEU8Dc0ReLoOrff-QX1GLI_B3Ur3yObYnji_BeU2I_8SG_irD2egGRG3xWTuJhm2bKL0aduIUsr90tsh2Qj6Sh3yLYmAIXzF6_NbEyOtPXWtJ_bmsSpqLGBkP75rZ4NQrmz_ZH-502qg_ZmB4JkIRwky9IWDYqAzLm2iljvvSrYjbHx2j3WoSZ0HBbRhVw4q6HyWWd8mv4Y5ZIsvkkyAo7MiDAfxUcYAV53NUnl3T8wrAxehx7wEfg3A5gXONnv201QKJ34WVTB-pdz-QzcEoxukhc4PslTW3nKsxxHCocflwSEXOtlLFxMwpLWqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رهبران دو اقتصاد بزرگ جهان روز پنج‌شنبه، دوم مهر، در کاخ سفید دیدار و دربارهٔ موضوعاتی از تجارت و تعرفه‌ها گرفته تا تایوان، هوش مصنوعی و جنگ ایران گفت‌وگو کردند.
در این دیدار که در کاخ سفید برگزار شد، شی جین‌پینگ از ایران و آمریکا خواست که در اسرع وقت مشکلاتشان را با گفت‌وگو حل‌وفصل کنند. رئیس‌جمهور چین همزمان از میزبان آمریکایی‌اش خواست که به‌سرعت و از طریق مذاکره، جنگ با ایران را پایان دهد.
رویترز به‌نقل از منابع آگاه گزارش کرده بود که چین در گفت‌وگوهای پیش از سفر شی جین‌پینگ، در مقابل امتیاز احتمالی آمریکا در زمینهٔ فروش تسلیحات به تایوان، پیشنهاد همکاری در اعمال فشار بر ایران را مطرح کرده است. این پیشنهاد به‌طور رسمی از سوی پکن تأیید نشده است.
تایوان از دیگر موضوعات حساس دیدار روز پنج‌شنبه بود. چین این جزیرهٔ دارای حکومت دموکراتیک را بخشی از قلمرو خود می‌داند و بارها با فروش تسلیحات آمریکا به تایوان مخالفت کرده است.
به گزارش خبرگزاری رسمی چین، شین‌هوا، آقای شی در کاخ سفید از دونالد ترامپ خواست که در قبال موضوع «استقلال» تایوان، با «دوراندیشی و احتیاط» رفتار کند.
این دومین دیدار ترامپ و شی در سال جاری میلادی و نخستین سفر رئیس‌جمهور چین به واشینگتن در بیش از یک دهه است.
شی جین‌پینگ عصر چهارشنبه به‌وقت محلی وارد آمریکا شد و دونالد ترامپ در پای هواپیمای او در پایگاه اندروز از وی استقبال کرد.
این نخستین بار در ۱۱ سال گذشته است که یک رئیس‌جمهور آمریکا برای استقبال از یک رهبر خارجی به این پایگاه می‌رود. آخرین بار باراک اوباما در سال ۲۰۱۵ در آن‌جا از پاپ فرانسیس استقبال کرده بود. موضوعی که نشانه‌ای از احترام ویژۀ دونالد ترامپ به همتای چینی‌اش به‌شمار می‌رود.
کاخ سفید همچنین برای پنجشنبه‌شب ضیافت رسمی شامی ترتیب داده که شماری از مدیران شرکت‌های بزرگ فناوری آمریکا از جمله اپل، آمازون، آلفابت، اوپن‌ای‌آی، تسلا و انویدیا به آن دعوت شده‌اند.
شی جین‌پینگ چهارشنبه‌شب در بدو ورود به آمریکا ابراز امیدواری کرد روابط پکن و واشینگتن باثبات‌تر شود و گفت دو کشور باید «شریک باشند، نه رقیب».
پیش از دیدار دو رئیس‌جمهور، مقام‌های ارشد اقتصادی دو کشور بر سر تمدید آتش‌بس تجاری به توافق رسیده‌ بودند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، پس از گفت‌وگو با هه لی‌فنگ، معاون نخست‌وزیر چین، اعلام کرد توافقی که افزایش شدید تعرفه‌های متقابل را متوقف کرده بود، تا ۱۰ ژانویه تمدید خواهد شد. آتش‌بس تجاری فعلی قرار بود در ماه نوامبر به پایان برسد.
در جریان جنگ تجاری دو کشور، تعرفه‌های متقابل در مقطعی از ۱۰۰ درصد نیز فراتر رفته بود.
مقام‌های آمریکایی همچنین از احتمال اعلام توافق‌هایی در زمینهٔ کشاورزی و موانع غیرتعرفه‌ای خبر داده‌اند. آمریکا می‌گوید چین در اجرای تعهد خود برای خرید ۲۰۰ فروند هواپیمای بوئینگ نیز پیشرفت‌هایی داشته، هرچند هنوز سفارش تازه‌ای اعلام نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/78517" target="_blank">📅 18:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78516">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2513034044.mp4?token=We05P8l2i6lVwWxpfoLYgWhcfRja-dqvUR53KXOc_sbmreqCdP-hy4szMVzEBNb9fRY06sblM24WoXO7Oe-r9Oc65h46Lgbhkr-s8k4fUnMINjjRNYv2Q8EmAWeCtTa7vVwXIJekR42CZGjP67YFKbvqYSaHEmOLP1D2ztp4ta62E7AfnHbQvLVWs94e9P-sTDJqxPofmRDyh5Zm_L5Fe7M1ZZAatk_N9mjCSzDG5KGYs-Uc4XDJgJ2yFbZiOvL5D3zOuVxUMALREti28zgsURfHDteg05lgzIbO7pRsB7Q2JoiOUaX6VxZfy4wgv0ty9sq9vV79gXX5RiNy0q2rsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2513034044.mp4?token=We05P8l2i6lVwWxpfoLYgWhcfRja-dqvUR53KXOc_sbmreqCdP-hy4szMVzEBNb9fRY06sblM24WoXO7Oe-r9Oc65h46Lgbhkr-s8k4fUnMINjjRNYv2Q8EmAWeCtTa7vVwXIJekR42CZGjP67YFKbvqYSaHEmOLP1D2ztp4ta62E7AfnHbQvLVWs94e9P-sTDJqxPofmRDyh5Zm_L5Fe7M1ZZAatk_N9mjCSzDG5KGYs-Uc4XDJgJ2yFbZiOvL5D3zOuVxUMALREti28zgsURfHDteg05lgzIbO7pRsB7Q2JoiOUaX6VxZfy4wgv0ty9sq9vV79gXX5RiNy0q2rsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارزش ریال در مقابل دستمال کاغذی
FattahiFarzad
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/78516" target="_blank">📅 17:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78515">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29d6b98e99.mp4?token=B7hcdPY-byu8uEBNk2X6pENhzH_oEQgnynBDzN_Gpy7arw3GodQpy7kZllf_xO6Lk8kgI2qYYzc8tz22c8_mE51PeazCq2ogaEG86FSwaZhnlSKos5OWCYrz_tFECtN0lw_jK54t0w-dTwqSsvsskwviMdxMe6-RPZVMkHQtwM3mD7JOpzD4p6bROgy5sVR479Uel0uTHHcuSUXjC0YurEvUeYgfJT5tA_lI9ppQO42fnJVISbsYIeQJ0hhoDuu-lCjzBQo8QmL6mJw_rfec1rEitkSeSOdIK7DGG-C0ybXZgbOvyuKXeuGUoZ6fhBYKUZ_qJ9vQgiBzd7z3yKc3SJZ5tsLa0uOwPtzRGFANM6nd8WQNB-Fz0PKHGvB79SoUUhGO85TEdN-sF_RbM3s1SyE9pdktS8QxK40MiBvCQiIeuo-d04kbFZyT25CVfJoc5Nm6T-sNt8Kh9liqBVeYgcNlBNbrB-cX1V4lx-f-iMmPBF6hZKMtaWDO2cEzUoiOx53eYdsAHUgjl16iBgyy8unTympJ08ZG20Wtbx7wMnKWwt5eNqIl2HroscNNW3FUqYiMbHnbBCpWz6hZ9jhpBEoIhWaCaLVfoYBdtdYcFLPNoP3ZcgHSuAM8esc1JzwjmIlnj09PctU5UM3Fh4zGxUAI1-WWtmVcMYbzbp0-i8U" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29d6b98e99.mp4?token=B7hcdPY-byu8uEBNk2X6pENhzH_oEQgnynBDzN_Gpy7arw3GodQpy7kZllf_xO6Lk8kgI2qYYzc8tz22c8_mE51PeazCq2ogaEG86FSwaZhnlSKos5OWCYrz_tFECtN0lw_jK54t0w-dTwqSsvsskwviMdxMe6-RPZVMkHQtwM3mD7JOpzD4p6bROgy5sVR479Uel0uTHHcuSUXjC0YurEvUeYgfJT5tA_lI9ppQO42fnJVISbsYIeQJ0hhoDuu-lCjzBQo8QmL6mJw_rfec1rEitkSeSOdIK7DGG-C0ybXZgbOvyuKXeuGUoZ6fhBYKUZ_qJ9vQgiBzd7z3yKc3SJZ5tsLa0uOwPtzRGFANM6nd8WQNB-Fz0PKHGvB79SoUUhGO85TEdN-sF_RbM3s1SyE9pdktS8QxK40MiBvCQiIeuo-d04kbFZyT25CVfJoc5Nm6T-sNt8Kh9liqBVeYgcNlBNbrB-cX1V4lx-f-iMmPBF6hZKMtaWDO2cEzUoiOx53eYdsAHUgjl16iBgyy8unTympJ08ZG20Wtbx7wMnKWwt5eNqIl2HroscNNW3FUqYiMbHnbBCpWz6hZ9jhpBEoIhWaCaLVfoYBdtdYcFLPNoP3ZcgHSuAM8esc1JzwjmIlnj09PctU5UM3Fh4zGxUAI1-WWtmVcMYbzbp0-i8U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی قلهکی، از منابع "نزدیک به حکومت"، با انتشار این ویدیو نوشته:
'''
اختصاصی: «تاجیکستان» و «جمهوری آذربایجان» آسمان خود را بر روی پروازهای «ایران» بستند
«پرواز هواپیمایی وارش» از تهران به «شهر دوشنبه» _پایتخت تاجیکستان_ از مرزِ هوایی لغو شد و به فرودگاه امام خمینی بازگشت.
🔻
پی‌نوشت: مسیر پرواز هواپیمایی وارش از سمتِ ایرانوبه مقصد «دوشنبه» _پایتخت تاجیکستان_، ورود به آسمان جمهوری آذربایجان و ترکمنستان بود که پیش‌تر آذربایجان و ترکمنستان آسمان خود را بر روی پروازهای ایرانی بستند و پرواز نتوانست وارد آسمان این دو کشور شود و بالاجبار به کشور بازگشت.
'''
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/78515" target="_blank">📅 17:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78514">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n11XH6DNZX2yox6TmPloBxmuZMetMk4rmTjFw71iLbHhrhtkklPSNRD3ptFMHE84TAUYwKSavIky3Po2DWwqN4MarFt7CpBvthpTUxkk-2eH9XYzCyPAB_6f0srIW4oQTXIqbuBKEBvWeK4oEBRV7vnw2i48ZS8xK8gwLRNK2aizN-A3vhEQxwlp2V4fvDjAFfMxeEFkTbbWnaC0PEEIBiOKQ5S8ZGF5tTKhtOomzgxC0q2XzKZvkzFXN5wTskoICqBDVZrq052ZpLvSVIGWzmVJRbxvEwbnUPO4--0AkKFRiZhIL8FVO-5TRgVlKjQUALUw9j8cSfS3sGZ2qxEQsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه دوم دادگاه انقلاب رشت ۹ وکیل دادگستری در استان گیلان را در یک پرونده مشترک به مجموع ۱۴ سال‌وهفت ماه‌و۱۵ روز حبس محکوم کرده است.
هرانا خبر داد «معصومه پورشهرانی»، «طاهره پوراسماعیلی»، «شادی فلاحتی»، «غلامحسین لایقی»، «حسام احمدپور»، «لادن آصفی‌راد»، «محمدرضا تاک»، «کیان طاهر‌اجارود» و یک وکیل با نام خانوادگی «دلیلی» در این پرونده محکوم شده‌اند.
هر یک از این وکلا با اتهام «تبلیغ علیه نظام» به هفت ماه‌و۱۵ روز زندان و با اتهام «توهین به رهبری و بنیان‌گذار جمهوری اسلامی» به ۱۲ ماه زندان محکوم شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/78514" target="_blank">📅 17:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78513">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcwvwxKg4sNOYpVA4pXuYAaNd4oNdmRI_dApefxsPMWBB1nN3maHRmflzFuF-XzLzAuhicq3zTxop-fyoieEpC9hOKr2_M7onJRzTdVNI6DYrSDb1ZnHhHzAMWDS6zswyaf0PLzvEvdDpbMpXHORzPj6WlPKRODdKAUBRSiMi_Sn1DuDVMpxvADi_zkWIy5fspU9bi0yeDIqTq8SUs1mT3U8VJVygnMtCpL47belqxPb-pW9XfW4GLX-XvkzeWGl4QmJkfhAKXKjCCeYXGI0oOKqaXxKbO9AOdEdm6NxSXctRdh0jQQ7mdDhe7TNjsozKalK2eu7rl3Fy8b73FisxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات متحده عربی روز چهارشنبه اول مهر فعالیت بانک ملی ایران در این کشور حاشیه خلیج فارس را ممنوع اعلام کرد.
این بانک در بیانیه‌ای اعلام کرد: «این اقدامات در نتیجه تخلفاتی مرتبط با رعایت نکردن مقررات، قوانین و تصمیمات نظارتی لازم‌الاجرا در امارات متحده عربی اتخاذ شده است.»
این نهاد افزود که این تخلفات شامل رعایت نکردن الزامات قوانین مربوط به مبارزه با پول‌شویی، تأمین مالی تروریسم و تأمین مالی اشاعه تسلیحات بوده است.
بانک مرکزی امارات اعلام کرده تمامی شعب بانک ملی ایران در این کشور از انجام تراکنش‌های مالی به مقصد ایران و از ایران، از جمله تأمین مالی تجارت و انتقال وجوه، منع خواهند شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78513" target="_blank">📅 17:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78512">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awjJ0TnchYuSsM9kD1QqJRR6mQd9bdTf6jaWGiQNRQvqjB8pUhEN8afoREwJoZiIqQydaaVVGbcMauqRnFLopoWBGc_xoIPxSGSnFyapbNQK1LXQAYOfKVkp4snu-CY9oYWJYpeqoaKwrdL7Gz0YgLGtBqYe0HthrjP8NHY4FDyq103K8ki8fYyvV07zVTHeQZABikMagIyjXRXZYol-zlNd9x255Y5sOadk2VHEXXv-aib0h8q-Kzp2CgBD05suHJ3L229PiZlN9ZBWk0drfprYV8lwN_YCotnQFrnf7ArGv_0tt_JnXSQO3GBFIdS3jfg22geacYhnFV5Pi1MkTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی تاکید رئیس‌جمهور ایران بر ادامه برنامه هسته‌ای و عزم جمهوری اسلامی برای تسلیم نشدن در مقابل فشارهای آمریکا، ارزش ریال ایران دوباره روند نزولی گرفت.
نرخ دلار در مقابل ریال ایران روز پنج‌شنبه با ۱.۴ درصد افزایش به ۲۳۵ هزار و ۴۰۰ تومان رسید.
نرخ یورو در لحظه تنظیم این گزارش در ظهر روز جاری به نزدیک ۲۶۸ هزار تومان و پوند بریتانیا به ۳۱۳ هزار تومان رسیده است.
سکه امامی با نزدیک به دو درصد افزایش هم اکنون بالای ۲۴۰ میلیون تومان و سکه بهار آزادی با ۱.۷ درصد افزایش بالای ۲۳۶ میلیون تومان معامله می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/78512" target="_blank">📅 17:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78511">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeiC1xgts5fSF39o_cNbh-OUn4RMOuxX0RBQc2BQaQgGUtGGwyTfeGkTb1KuKxm35J9oF5gV9NfyICEqgUGuMQwubmoYQWfMUUVAGEoDqzxQGnNGcS7_9YoAqg2-n2rXsLaCIx5QYfGS1TA-pNsAjBdKfHKsWwksfalYt9iN1UqF69thAXmyHaDmp0i8ODmowMhR0EpU6TUd97LGhrRTPcSeDg8rfGem132aXFTxDcxYZnCGxyMEAEjmlSKXO4Z7ClAR17ok4wnCBAd-65QACNbQttcwoEQj7RNwnl5C_Rb1Xr9s_iAhH2fid7NoBg2sgABtDgU1RddKJlRZAX9o6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت ردیابی نفتکش‌ها «تانکر ترکرز» می‌گوید نزدیک به شش میلیون بشکه نفت خام توقیف‌شده ایران، به ارزش تقریبی ۶۰۰ میلیون دلار، در حال عبور از اقیانوس اطلس به مقصد ایالات متحده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/78511" target="_blank">📅 17:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78510">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tLppMKIwuR7F5vYKe-s5DQBX2Rg6bUyYqQUPKngEbfutxTZM9r_ySvvW4kVTudBZKCFHv29xw0A8mQc_WaQfxGs_1xRf56vPq8pAeJqDGn2yYdcykbVpryLoW_Y1qf_WyJwli7DXodKWyENnKxHwIbI2Qw23Bz64roMfgfeBL9N5GorlpwUY_uVstLIineTyE5Qw7EPTnxw_QSqrL65Xa913FjMv5FcbzOr1a_kbqgdtx1DOIrdW-agIXtkg5kCmVD0DSF3oTuNFiiliBkcerbUmePEWdYUPhTBPlxlCvnm6dO-_vFtHPdGAozlbgqDUDTIZnVppJMMcOqFPmRUMhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس اطلاعات رسیده به ایران‌اینترنشنال، همه پروازهای شرکت‌های هواپیمایی ایرانی به امارات متحده عربی لغو شد.
پرواز شرکت‌های هواپیمایی ایرانی به امارات از شهرهایی از جمله تهران، کیش، مشهد و شیراز برقرار بود که اکنون لغو شده است.
لغو این پروازها پس از اجرایی شدن محدودیت‌های اعلام‌شده آمریکا علیه فعالیت خارجی شرکت‌های هواپیمایی ایران صورت می‌گیرد.
اسکات بسنت، وزیر خزانه‌داری آمریکا، پیش‌تر اعلام کرده بود از اول مهر فعالیت شرکت‌های هواپیمایی ایران در خارج از کشور متوقف خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/78510" target="_blank">📅 17:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78509">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPox0SkALCLZ8oZiMUSvfUFtNpha3dY-XRuP8Rt7eZ0QuidAGypE0DcYkspx3GcfII7Q_JyNV2sMmDXp8hzcK5Jlm_Ahhk61XGHrsyI40bmDSO2Rss2nufVLQZvTwJkLq6IR0qx-zgYaQj8ztBBhIWy9EhRzdAHRjdRFIsKSov-lrjzDaybHLDtk-O2TGpY-iG9xF_JYPJgcXVJEYO3WN97GkYUzqr6k4zcbImcFmBy2TDGAXR8JQbNkCG8PRbuC8HSQE8sI-EeQBzLh_0zDcp7FtpSZT1xZgdUJUVX3TQG041qF771Tb-cv5RThCuxpyuLdAhqhdOw3kWN8Fr7taw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دفاع مدنی عربستان سعودی پنجشنبه دوم مهرماه، با صدور هشداری از تلاش دوباره برای حمله به مکه خبر داد.
این هشدار برای شهر مکه صادر و پس از لحظاتی لغو شد.
عربستان سعودی برای برخی از شهرهای ساحلی دریای سرخ از جمله طائف، جده و تبوک، نیز همزمان هشدارهایی صادر کرد.
در همین ارتباط ترکی المالکی، سخنگوی رسمی نیروهای ائتلاف بین‌المللی، اعلام کرد که شش فروند موشک بالستیک شلیک‌ شده از سوی شورشیان حوثی، رهگیری و منهدم شده و پدافند هوایی نیز تلاش برای هدف قرار دادن طائف و ینبع را خنثی کرده است.
هفته گذشته نیز عربستان سعودی، شورشیان حوثی را متهم به تلاش برای حمله موشکی به شهر مکه کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/78509" target="_blank">📅 17:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78508">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v4qfkMyx5dSwQVpX_lnjHq-eLFKiyvj8m_GMORTRQSQhy4cepW6GGDyIInvLvKttL9dORrsF9fMwIPcDb4YqKc9CyMlF16x6PBAyA4zD2RlMbD24ZME9EZDNYHRXLcRGl2Bt7ETsZ7fIyD_6VwXBSP_axQtcM_Cc9voos-SMlmyGSlQCbot3V18h5gK76TkpRFQc9mbjOV6pt5fEPUvOlBRl28APf-cTzVonW_Xj4FSOFpsQrIRtN7sImyEgogIA0CjUMjR1-0G68_RlPpA4vnh-f0etLsn2D3oA3N-B8BVHKPWrD066HTvN0iCVcW8U7ExyoDGGfeYNQ6KEdvnUDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام «ارغوان فلاحی»، زندانی سیاسی محبوس در زندان اوین، پس از پذیرش اعاده دادرسی متوقف شده و پرونده او قرار است برای رسیدگی مجدد به شعبه هم‌عرض فرستاده شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78508" target="_blank">📅 17:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78507">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a986602075.mp4?token=fmWKar75UusvFBBJzMl0LZQHSsdopaOl2Z8UTgWRdw9egn3GFNgOIuSsyqHTnN8oVkOVkI0ItnHCJF3mCUITvk5Hv5wSzUe8k6uMlUoddaOf68dLBg9DVfgQyBJdunMkPYETw--LL02KCBqeb_hQeN1uBo1LMcgcR6DxOX6yeyWYQ221JruSzeroP5Slz6ghhB0YdttwaaRUqOObMqDdDWyIBodWH3fUcs4PjGcG1r8vDWyo9FmTSBLbYt5WSj7i3uum5jpGIVbDAMSLn_sPuweak0bdsvsLc1pUCAVr2bNFMVf26QJBdMuGcs5Yeq5WjGf0I9nSz8DzA4dfT1_eSg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a986602075.mp4?token=fmWKar75UusvFBBJzMl0LZQHSsdopaOl2Z8UTgWRdw9egn3GFNgOIuSsyqHTnN8oVkOVkI0ItnHCJF3mCUITvk5Hv5wSzUe8k6uMlUoddaOf68dLBg9DVfgQyBJdunMkPYETw--LL02KCBqeb_hQeN1uBo1LMcgcR6DxOX6yeyWYQ221JruSzeroP5Slz6ghhB0YdttwaaRUqOObMqDdDWyIBodWH3fUcs4PjGcG1r8vDWyo9FmTSBLbYt5WSj7i3uum5jpGIVbDAMSLn_sPuweak0bdsvsLc1pUCAVr2bNFMVf26QJBdMuGcs5Yeq5WjGf0I9nSz8DzA4dfT1_eSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ تن از آسیب‌دیدگان چشمی خیزش مهسا با انتشار پیامی ویدیویی، خواستار لغو حکم اعدام علی زارعی شدند.
غزل رنجکش، عرفان رمیزی‌پور، مرسده شاهین‌کار، مجید موافق، حسین نوری‌نیکو، حمیدرضا حیدری، سالار وطن‌شناس، پارسا قبادی و علی دلپسند در این پیام از مردم و نهادهای حقوق بشری خواستند در برابر جنایات جمهوری اسلامی سکوت نکنند، صدای علی زارعی باشند و برای جلوگیری از اجرای حکم اعدام او تلاش کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/78507" target="_blank">📅 17:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78505">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پیام‌های دریافتی:
ساعت ۰۰:۱۳
انفجار شدید بندرعباس
همین الان بندرعباس موج انفجار حس شد
وحید قشم لرزید
انفجار دریا بود
00:24  بندرعباس، صدای خفیف انفجار از دور
سلام حدود ساعت ۱۲ یه موج شدید پنجره های ما رو تو بندرعباس لرزوند
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 449K · <a href="https://t.me/VahidOnline/78505" target="_blank">📅 00:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78504">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X2UnoSK8U3jxJMe3yQ7GyWjj3bb1Es_1bxccM4kZJmSRCvMudxg-v-kJnUfv5OiX1fNmIqsD577CRjDh5mPjxJY4X2RQFxfpc0sCDwKkGWu4q0EbSgUacbVMRpD7SSITU4_24ESIQRrQtb_nYRXWBfI-tIwJDqmoaIyOqcJoR5WNBMWu977Qiet3lTkTuSeaoWDxf10CzJGrCbGg1z1ccrmKYIWiqOdTE5vRWQO0cng7brvGeGaVQfJJZDN90eaB39lNLQ1pfUky-KA8pWUjVlreAAZ6zLof81nG6CsFyFnsR1yxzQ1qrdew768JT8K_E0vkV2zeza3YgXDz-mbuiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط‌عمومی قرارگاه قدس نیروی زمینی سپاه پاسداران، از کشته‌شدن سرتیپ حسین ظریفی، فرمانده عملیاتی قرارگاه سجاد شهرستان سراوان، در جریان یک درگیری مسلحانه در این منطقه خبر داد.
روابط عمومی سپاه، روز اول مهر ۱۴۰۵، در بیانیه خود نوشت ظریفی در جریان «آخرین عملیات رزمندگان این قرارگاه در منطقه سراوان» کشته شده است.
همزمان، حال‌وش گزارش داده است که احمد هراتی زراعتی، مسوول اطلاعات قرارگاه عملیاتی سجاد سراوان، نیز در جریان درگیری نیروهای نظامی با افراد مسلح در منطقه جهاد آباد سراوان کشته شده است.
بر اساس گزارش حال‌وش، این درگیری روز چهارشنبه یکم مهر رخ داده و دست‌کم ۱۳ نیروی نظامی و امنیتی دیگر نیز در جریان آن به‌شدت زخمی شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 451K · <a href="https://t.me/VahidOnline/78504" target="_blank">📅 21:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78503">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/813923332b.mp4?token=W9FRKB5JLnXWk3XjySmEopNyo80ewJiK9PiW2BbZkXHqO5LZN672boIVAKp5HHb8XgNYyHrZCVbBecUSOM6sgCd6M3eN3b2F65Rshi-1CIjQdlZOK0hys4UyOl3I3j26pIa87YHv1S9_cbldiuAxkXmRaR6xgKMLJkp5RTKPe8yDDef2FFwjEfzgqONNpypmyVaKl9Do40e65lHcDJ8Ki-WjD_br8zgKT2ktG8GqJplmYr2_-c3aDoZFKoxFAy9lr8g1H0FjKbRutkKm-xqT4F9C4ZY94ROzQlFcfWO8Qgt1s-pRL6CB_95UvuZ-IbOus14z5KvqjYNjR0YHsKBQYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/813923332b.mp4?token=W9FRKB5JLnXWk3XjySmEopNyo80ewJiK9PiW2BbZkXHqO5LZN672boIVAKp5HHb8XgNYyHrZCVbBecUSOM6sgCd6M3eN3b2F65Rshi-1CIjQdlZOK0hys4UyOl3I3j26pIa87YHv1S9_cbldiuAxkXmRaR6xgKMLJkp5RTKPe8yDDef2FFwjEfzgqONNpypmyVaKl9Do40e65lHcDJ8Ki-WjD_br8zgKT2ktG8GqJplmYr2_-c3aDoZFKoxFAy9lr8g1H0FjKbRutkKm-xqT4F9C4ZY94ROzQlFcfWO8Qgt1s-pRL6CB_95UvuZ-IbOus14z5KvqjYNjR0YHsKBQYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، روز چهارشنبه، اول مهرماه، در حاشیه نشست‌های مجمع عمومی سازمان ملل متحد در نیویورک، از ادامه رایزنی‌ها با میانجی‌گران درباره ایران خبر داد و جلوگیری از دستیابی تهران به سلاح هسته‌ای را مهم‌ترین موضوع در هرگونه توافق احتمالی دانست.
به گفته روبیو، دونالد ترامپ همچنان برای دستیابی به توافق با ایران آمادگی دارد، اما چنین توافقی نیازمند مذاکرات دشوار و فشرده با مشارکت میانجی‌گران خواهد بود.
وزیر خارجه آمریکا همچنین با اشاره به تنگه هرمز، از ادامه عبور نفتکش‌ها از مسیر جنوبی خبر داد و حفاظت از کشتی‌رانی و باز نگه داشتن تنگه را از ماموریت‌های ارتش آمریکا عنوان کرد.
روبیو درباره جزئیات رایزنی‌های دیپلماتیک توضیح بیشتری نداد و تاکید کرد: «اگر قرار باشد توافقی حاصل شود، این اتفاق در یک نشست خبری رخ نخواهد داد.»
@
VahidOOnLine
روبیو در واکنش به سخنان مسعود پزشکیان که ایالات متحده را به نقض قوانین بین‌المللی متهم کرده بود، به شدت از تهران انتقاد کرد.
روبیو با اشاره به کشته شدن هزاران نفر از مردم در تظاهرات، حمایت مالی از گروه‌های تروریستی برای حمله به همسایگان و تاسیسات انرژی، و سرپیچی از قطعنامه‌های هسته‌ای تاکید کرد که جمهوری اسلامی ایران بزرگ‌ترین ناقض نظام بین‌المللی در جهان است.
او تصریح کرد: «نمی‌دانم ایران چه حقی دارد که به کسی درباره حقوق بشر یا نظام بین‌المللی موعظه کند، در حالی که خود به طور مداوم آن را نقض می‌کند.» وزیر خارجه آمریکا افزود که حکومت ایران با قتل‌عام مردم خود، نقض حاکمیت کشورهای همسایه و بی‌اعتنایی به قوانین جامعه جهانی، صلاحیت اظهارنظر در این زمینه را ندارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/78503" target="_blank">📅 20:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78502">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f3a6c0f2e6.mp4?token=IXCF1P50Pe3IfTUM_lIVN9I65RirMgvuSwiW1z8eeTdNYhFj9VkrsMMeMQ8qs4W8_mmk8Xm-sxCcdgRprc9nWVu1F6D-gU5FUt5oqn_MS0Ic2K3p_ClVzd5UpZre3-n_JBV772dMxCW7K559RO6Ra90DQBTOTQ8zW4ZmuijK5wwPcuQaYx-WNDxDzRWBspPHZDp95ps_LO1oFgd4XjxnWFVtqcMaWsHcz8pi51VF-I1dsSFnDB3RWtmxCwjxotJv1q7jDE49-teOX_SwdmRpL9EdFSl7Pqo_E_pBGNOaIDhP7B5ogDsed58ChxEqZtDXgXt5Lv5btswmRWkaGsnQ8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f3a6c0f2e6.mp4?token=IXCF1P50Pe3IfTUM_lIVN9I65RirMgvuSwiW1z8eeTdNYhFj9VkrsMMeMQ8qs4W8_mmk8Xm-sxCcdgRprc9nWVu1F6D-gU5FUt5oqn_MS0Ic2K3p_ClVzd5UpZre3-n_JBV772dMxCW7K559RO6Ra90DQBTOTQ8zW4ZmuijK5wwPcuQaYx-WNDxDzRWBspPHZDp95ps_LO1oFgd4XjxnWFVtqcMaWsHcz8pi51VF-I1dsSFnDB3RWtmxCwjxotJv1q7jDE49-teOX_SwdmRpL9EdFSl7Pqo_E_pBGNOaIDhP7B5ogDsed58ChxEqZtDXgXt5Lv5btswmRWkaGsnQ8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی: اگر کشورهای همسایه پروازهایمان را ممنوع کنند، پروازهای آنها نیز متوقف خواهد شد
محسن رضایی، دبیر شورای‌عالی امنیت ملی جمهوری اسلامی، کشورهای همسایه ایران را در واکنش به محدودیت‌های اعمال‌شده علیه پروازهای ایرانی تهدید کرد و گفت اگر این کشورها پروازهای ایران را ممنوع کنند و وارد همکاری با آمریکا شوند، پروازهای فرودگاه‌های آنها نیز متوقف خواهد شد.
رضایی گفت: «اگر کنار آمریکا باشید، ما شما را تماشا نخواهیم کرد» و هشدار داد در صورت ممنوعیت پروازهای ایران و همکاری کشورهای همسایه با آمریکا، «فرودگاه‌هایتان پرواز نخواهد داشت».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78502" target="_blank">📅 19:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78501">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پزشکیان: از مذاکره برای صلح نمی‌گریزیم
مسعود پزشکیان، رییس دولت در جمهوری اسلامی، چهارشنبه اول مهر در سخنرانی خود در هشتاد و یکمین مجمع عمومی سازمان ملل متحد گفت متن سخنرانی‌اش را از پیش آماده کرده بود، اما پس از سخنان دونالد ترامپ، رییس‌جمهوری آمریکا، و «تروریست» خواندن جمهوری اسلامی، تصمیم گرفت عکس علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، و دانش‌آموزان مدرسه میناب را به حاضران نشان دهد.
پزشکیان همچنین گفت: «هر کسی را که می‌خواهند تخریب کنند، نام تروریست بر آن می‌گذارند. ۲۰۰ سال است که ایران به کشوری حمله نکرده و فقط از خود دفاع کرده، اما ما را عامل ناامنی می‌خوانند.»
او در بخش دیگری از سخنانش گفت: «آمریکا و اسرائیل با آخرین تجهیزات به ما حمله کردند و ما با قدرت دفاع کردیم.»
پزشکیان گفت آمریکا و اسرائیل جنگ را به ایران تحمیل کردند، اما جمهوری اسلامی «با قدرت» دفاع کرد و در عین حال «برای صلح از مذاکره نمی‌گریزد».
او درباره برنامه هسته‌ای جمهوری اسلامی گفت: «برای دفاع از کشورمان از هیچ‌کسی اجازه نمی‌گیریم. ایران نمی‌پذیرد که دانش هسته‌ای در انحصار چند کشور باشد؛ سلاح هسته‌ای را عامل امنیت نمی‌دانیم.»
پزشکیان در ادامه درباره تنگه هرمز گفت: «نمی‌شود همه از تنگه هرمز بهره ببرند و راه کشتیرانی بر ایران بسته شود. استقرار ناوگان‌های متخاصم و گسترش جنگ باعث امنیت کشتیرانی نمی‌شود.»
او درباره شرایط منطقه نیز گفت: «در منطقه‌ای زندگی می‌کنیم که جنگ مرز نمی‌شناسد و بحران یک کشور به همسایگان سرایت می‌کند. از این رو همسایگان خود را قوی می‌دانیم.»
@
VahidOnLive
پزشکیان: یا امنیت را با هم می‌سازیم یا ناامنی را با هم تحمل می‌کنیم
مسعود پزشکیان در مجمع عمومی سازمان ملل گفت: «صلحی که برای همه نباشد، صلح نیست. یا امنیت را با هم خواهیم ساخت یا ناامنی را با یکدیگر تحمل خواهیم کرد. ما آماده گفت‌وگو هستیم، اما زبان زور را نخواهیم پذیرفت.»
او افزود: «سخنان ترامپ نزد افکار عمومی جهان و اندیشمندان، نشانه بارزی از خوی قلدری و منطق زور و مغایر با منشور صریح سازمان ملل است.»
پزشکیان گفت: «ترامپ بداند که این سخنان ملت ما را منسجم‌تر می‌کند و باید بداند که ملت ما در برابر زور سر خم نکرده و متجاوزان را پشیمان خواهد کرد.»
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/78501" target="_blank">📅 18:28 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
