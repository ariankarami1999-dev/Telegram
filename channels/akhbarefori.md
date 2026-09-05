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
<img src="https://cdn4.telesco.pe/file/MwFTyyjH0Nl7IleWE3JkE1Nw6GCSCwsrt3WLeGIpKV4MtrxrxRhrMU-xrnNI2L-DzgUOvfJgoh1FXJVncpIU4FTqBXhZN-OAJs2tczfMEKnx9Y_zGhxfvSzkR3Zwf5v7fliZ1_fUHvhgiZCitYWfLL8FmDcJ7kwmkgGw7Ey22XdbAXHtYBlo1YrpuPvnFEH2ppOH57s38TuM0ZbUmApfhzuGHhCLXiy_B7qPNE9wqzB7jcHuoYg8vNtQyMhcztB8UPbDq08VgkWb68X5sE82Pe3iewz4mL57DH8bBVE7cDDKqgyN_oodlVpp9JSsZBoXZsH_io1I0gBmNYsKxSyyvg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.42M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 21:59:09</div>
<hr>

<div class="tg-post" id="msg-687509">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ادعای رسانه صهیونیست: ایران در حال آماده شدن برای یک حمله شبیه ۷ اکتبر است
ادعای جروزالم‌پست:
🔹
ایران در حال آماده‌سازی برای یک حمله هماهنگ و گسترده علیه اسرائیل در چندین جبهه به‌طور همزمان است. این سناریو شبیه به حمله ۷ اکتبر طراحی شده، اما با این تفاوت که از ابتدا برای گرد هم آوردن تمامی مؤلفه‌های محور مقاومت برنامه‌ریزی می‌شود.
🔹
بر اساس این ارزیابی‌ها، ایران به دنبال ترکیب نیروهای خود با حزب‌الله لبنان، حماس، حوثی‌های یمن و شبه‌نظامیان طرفدار ایران در عراق در یک کارزار واحد است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/687509" target="_blank">📅 21:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687508">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VglW0WEzJXA4CuYZtLBOqBaMSanRRz9XTg6U5wO6L98g8LBpKO3xSBXaAZ5ZQG1nqHKVbOgDtybsjGMWTIqjYFZ7H12cDAiuc06FmacRZdK7JBDJ1v1ZljFvjCvL6pSepjkeDQ3cxt-aMRqceH-I7ypO2ps1YlCYF0uIOq0REF0cgoIanH8FB2MTHs6CB7CDfN4eiNt6J6qZ5lM1F4BiBFo1xDuEChkW-mEhWT0gVKMLU2iW8PwblMUh25OA4FqHxa4sS6zXd5hhBhEGm9L1XEazAn8HXIgac4faj5pQjhno1KWdiRMpHHaS2LFyH5n5wrv6Ye8hl8RJbA_57wkZBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کارمزد خرید طلا در زرپی برای همیشه نصف شد!
🔹
از این به بعد کارمزد خرید طلا در زرپی به‌جای ۱٪، فقط
۰.۵٪
است.
🔹
یعنی با هر خرید، هزینه کمتری پرداخت می‌کنی و بخش بیشتری از سرمایه‌ات صرف خرید خودِ طلا می‌شود.
🔹
این کاهش کارمزد موقتی و کمپینی نیست؛ تصمیمی دائمی برای کم‌هزینه‌تر و شفاف‌تر شدن خرید طلا در زرپی است.
🔹
اگر طلا می‌خری، چه به‌صورت دوره‌ای و چه با مبالغ مختلف، این تغییر می‌تواند در طول زمان تفاوت قابل‌توجهی ایجاد کند.
🔹
برای آشنایی بیشتر با زرپی و اطلاع از آخرین خبرها و قابلیت‌ها، عضو کانال تلگرام زرپی شو.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/akhbarefori/687508" target="_blank">📅 21:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687507">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
سنتکام: ناو جورج واشنگتن مجبور به فرار از دست موشک های بالستیک ایرانی شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/687507" target="_blank">📅 21:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687506">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f5a97038f.mp4?token=iP1Ax3CWiBVpXN2mdrGTfR_VORzvLlt8d8JIleGvppU5YlTUugaUP6NBlRHwkCH5R5iQTyYD_jLI4WCYpSesq_3HVTok-v23bV5ct4_DzZk1n7MAeT0Y3lprYP-HbMHxZo-vW4hmqbT5Dqmvk_9N1i25C4F72rC2PPil3399DX430iOdTcYLcATbpEo4R84KmYQ2ttAv9LxJ0ULHo36xzddt2WFD5tCFZ2jj6i3JLAnr62DlPw-rBhyK02xbeghSAqZEMQjI21u7g_9zg0vGyLO48jPl1j8nX8agrpuKmEidrRUhc7y8MhTn4HRE-pCKTumMaumrKgeq6NLNXCbU2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f5a97038f.mp4?token=iP1Ax3CWiBVpXN2mdrGTfR_VORzvLlt8d8JIleGvppU5YlTUugaUP6NBlRHwkCH5R5iQTyYD_jLI4WCYpSesq_3HVTok-v23bV5ct4_DzZk1n7MAeT0Y3lprYP-HbMHxZo-vW4hmqbT5Dqmvk_9N1i25C4F72rC2PPil3399DX430iOdTcYLcATbpEo4R84KmYQ2ttAv9LxJ0ULHo36xzddt2WFD5tCFZ2jj6i3JLAnr62DlPw-rBhyK02xbeghSAqZEMQjI21u7g_9zg0vGyLO48jPl1j8nX8agrpuKmEidrRUhc7y8MhTn4HRE-pCKTumMaumrKgeq6NLNXCbU2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جان بولتون: هگست صلاحیت تصدی وزارت جنگ‌ آمریکا را ندارد
🔹
طبق گزارش‌ها، هگزت برای پست «سخنگوی پنتاگون» به ترامپ درخواست داده بود؛ پستی که با توجه به سوابقش، گزینه بسیار مناسبی برای او محسوب می‌شد. اما کاری که الان به او سپرده شده بسیار فراتر از توان و حد توانایی‌های اوست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/687506" target="_blank">📅 21:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687505">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
حملۀ هوایی صهیونیست‌ها به علی‌الطاهر با وجود ادعای تسلط بر آن
الجزیره:
🔹
جنگنده‌های رژیم صهیونیستی شهرک المنصوری و ارتفاعات منطقه علی‌الطاهر در جنوب لبنان را بمباران کردند. بمباران ارتفاعات علی الطاهر در حالی است که رژیم صهیونیستی روز پنجشنبه گذشته مدعی «کنترل عملیاتی» این ارتفاعات و ورود به دو مسیر زیرزمینی در آن شده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/687505" target="_blank">📅 21:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687504">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZ5TBiJF0mODV4yyjOxvwbpucoy2a1GA2afhN0hspZruGzK-b_bCRKg9PoxNNJiij1phQnFTmnHrmYAVNAt7qXxWi8BO0faGLhiWqWWmkhP5uKtnPVXL9hoquXBSVHWCJ0qa2aLsKA5ZoLo3utAZ0jqRO7g55GJL4nmoflUoruYbwVSK5hmOBi4Ykn5RiZQ9Q0gkpEYqGUqHkiVpqEZFSRrdA0yXocu3SfuMffpJ2cV0jHRipJSus5QHORxmTsGHm781oUX5umHdnpVpDktzSY04_6MUcUSQz5IHIF7txN0oot7UppptZjmh8lwMRaHBSdR8fT_NSLuqdef8opl5MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد مرندی: اکنون تمام کشتی‌های نیروی دریایی آمریکا هدف هستند. هرگونه حمله به کشتی‌های ایرانی با حملات متعدد به کشتی‌های مرتبط با کشورهای شرکت‌کننده در تجاوز ضد ایرانی مواجه خواهد شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/687504" target="_blank">📅 21:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687503">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5fEE6Xmid7XEz7mzA2IDIB9zEfVm6PomtJBnBJLlZgk7rdaMP_NP8-fqp0cpT-rlgfwPO-_xhu4nxM8ZBFiTPA-UE6heVIFaComen2hJuRnMyXsn5ec6h6Bi0Pvt5rsTRmctHZnj7L-Gj5PTtVY1i3Uiv8dwoRncpV6a0R92zjMyDeoPDgNKHuaEcAxTmuxAY4iLN4TY8o5jj1eH9TE936GDtkyHTGSHDuRmtUhcGHlwzVJFpgKx-dLKqXVafuShFnLQ9mqcBAwa3qB9A4Bug4XfXLO3VvE_WG6nRto9w55rKjSb3Xy2GlSVC8kQ27AAv8EP2v7AgQ1TGz8fy3ALA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه در محکومیت شدید حملات غیرقانونی آمريکا علیه شناورهای ایرانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/687503" target="_blank">📅 21:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687501">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تذکر قاضی‌زاده هاشمی به دولت: ادبیات سیاسیون و دولتمردان اصلاح شود
امیرحسین قاضی‌زاده‌هاشمی در
#گفتگو
با خبرفوری:
🔹
اگر امنیت جلوگیری از جنگ می‌خواهیم و اگر صلح‌طلب واقعی هستیم، باید یک روایت قدرت به خارج که ما در موضع قدرت هستیم از ایران انجام دهیم و به‌درستی روایت ناتوانی دشمن را بگوییم، به جای اینکه بیایم به سستی‌های خودمان اشاره بکنیم.
🔹
اینکه ما بیاییم یک روایت ضعف ارائه دهیم که هنر نیست و امیدواریم که ادبیات سیاسیون و دولتمردان اصلاح شود و بعد کم‌کم شاهد توسعه آن در ادبیات مردم باشیم. به نظرم ما هنوز به این بلوغ نرسیده‌ایم که فصل انتخابات با بعد از انتخابات متفاوت است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/687501" target="_blank">📅 21:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687500">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22a6521f5d.mp4?token=GItTsLAKorWs5EQNgzyhTD_FNi2Mm8WorQ6FtX0JKim3Y1c9pQFxs5GcMaD5nMoyq7Dl-ptQy4aU6pDidozEN3qc5xauyt9T_1cRSL4lrvbxpjtNEz-VMoS70P18yBh5mxfEe9iVehxrMJr3H-VffiCLeDxavrbV0UcfjUaQRDLhZxVSlQZChWjYwWWzigfU1W2yjBm3SNf666O-OrBg7YvrGU9W-5AUZeQaU7FZO4FGwLpstJbyqY-xIEz5hBxs4k7Bd6ROKqEClqEov6QrRJBwyuohqeevZkg2axvq4mBQ8osJ1b4WV9jrMhcQWiNqX6z1T10JzaBNsJWakpKhkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22a6521f5d.mp4?token=GItTsLAKorWs5EQNgzyhTD_FNi2Mm8WorQ6FtX0JKim3Y1c9pQFxs5GcMaD5nMoyq7Dl-ptQy4aU6pDidozEN3qc5xauyt9T_1cRSL4lrvbxpjtNEz-VMoS70P18yBh5mxfEe9iVehxrMJr3H-VffiCLeDxavrbV0UcfjUaQRDLhZxVSlQZChWjYwWWzigfU1W2yjBm3SNf666O-OrBg7YvrGU9W-5AUZeQaU7FZO4FGwLpstJbyqY-xIEz5hBxs4k7Bd6ROKqEClqEov6QrRJBwyuohqeevZkg2axvq4mBQ8osJ1b4WV9jrMhcQWiNqX6z1T10JzaBNsJWakpKhkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثبت حضور پلنگ ماده در منطقه شکار ممنوع کوه سفید/ پریزاد نام پلنگ جدید شناسایی شده در دماوند
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/687500" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687499">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4f970358b.mp4?token=GXq8qISXklNNxOKbawT4YxpBspGDyPtnN7Q9TqSp1uvn2uI16jds7_zf0-PnS6xsBETeSsG9-4I2_o12BBWpNb26foJMCnf9HaxlJeBZCG3zRfj-qR0cTAhstByr7hTPXXxxiPTjfpJX8ayo5GJbGpgszGIB7iJlWm7I0qGHbVyMIcw9rR9iXIHXjiEoP1OExKQs1a29iR3s_AyH36eiAAo469AcseZVN-pagEjFGxyCLnKae8qDNnM4hJ2K-FOiUMuLEahaRBTlJPn2t1VEhz6UuGJIMGZSNRtfKZlyv45lqY0fVY8guvSeFeaIhucTtMKaUN4O54rrDprPAxKeDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4f970358b.mp4?token=GXq8qISXklNNxOKbawT4YxpBspGDyPtnN7Q9TqSp1uvn2uI16jds7_zf0-PnS6xsBETeSsG9-4I2_o12BBWpNb26foJMCnf9HaxlJeBZCG3zRfj-qR0cTAhstByr7hTPXXxxiPTjfpJX8ayo5GJbGpgszGIB7iJlWm7I0qGHbVyMIcw9rR9iXIHXjiEoP1OExKQs1a29iR3s_AyH36eiAAo469AcseZVN-pagEjFGxyCLnKae8qDNnM4hJ2K-FOiUMuLEahaRBTlJPn2t1VEhz6UuGJIMGZSNRtfKZlyv45lqY0fVY8guvSeFeaIhucTtMKaUN4O54rrDprPAxKeDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این کدهای مخفی خروجی‌های خاص و متفاوت از هوش‌مصنوعی بگیرید #هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/687499" target="_blank">📅 21:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687498">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
خبرنگار صداوسیما در جاسک و قشم: صداهای شنیده شده در این مناطق ناشی از تنبیه شناورهای متخلف در تنگه هرمز است و در این مناطق انفجاری رخ نداده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/687498" target="_blank">📅 21:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687497">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
سخنگوی قرارگاه مرکزی خاتم‌الانبیا: به ارتش تروریست آمریکا هشدار داده می‌شود در صورت تداوم شرارت، ناامنی و مزاحمت برای کشتی های ایرانی و محاصره دریایی ایران، ضربات نیروهای مسلح جمهوری اسلامی ایران علیه شناورهای نظامی آمریکا در منطقه شدیدتر از قبل خواهد بود و امکان گسترش آن نیز وجود دارد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/687497" target="_blank">📅 21:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687495">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSNYNs4HN0pdFSMxW0BM9uUxpE-QJlypN8gHds6dvzIHsoyBDGK6CABpgGxcdIfQbDrJ2pt0znQ9PDz1WNMZ8AS-z8CFIHOJHDbWqi4WC_Yd82nbHK0V8l2USZ-8ShpN5_Enc4rVEqtFLDmwna4AshrtffHTXzi8gq4QtVnaEs9mVKIQwgdRJELP2ZV4Baw5Svrt959m4-ipOdI_0CjQOTv-oYZlvM6kaQmIBP2YnYO253paxYVWuvWcuhDGLqNJ_UHubz7PLF9Q0551MLY4xY_VAv-89D9HbEUBykeTe-u06aNrs26eQnyi5VzhcxCiWo4lb7-stg0GoQpMK1648g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر معظم انقلاب: امروز روزی است که چشم‌انداز غلبه نهایی حق بر باطل، و اسلام بر کفر به‌مراتب بیش از همه‌ ادوار گذشته به عینیّت نزدیک شده است
🔹
بخشی از پیام رهبر انقلاب اسلامی به مناسبت هفته وحدت | ۸/شهریور/۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/687495" target="_blank">📅 20:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687494">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
خبرنگار صداوسیما در جاسک و قشم: صداهای شنیده شده در این مناطق ناشی از تنبیه شناورهای متخلف در تنگه هرمز است و در این مناطق انفجاری رخ نداده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/687494" target="_blank">📅 20:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687493">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-RR59dutna6g4zvtTrbgRH-HhecBZq4S1BuXTOAVtF5s2BD05oGJQydMA_1jPM8zpzPYVq7Xk-BXedOBRCWCWkPFbDcrhEwNWhz6Snv3Ux_RaYtWu_8garzz6Fe1o6J41K1R2cBGy0IAqDK5b-q4psP-AmTiLtXos4Visr3MSM_6tTIHjSi5YzpY0gDWtpKqHsr85wkO3zDDGGt2HtxrjxQSOlMK2wr6JPNbFB-d1wuucrr2HPbylsSExRX0CryTX_ueKliKuH-XiPwGJIZHu7k2gqsRUr90W7Q_zamoEpuvFbnlUJ_XcQpzH4gilC2FH5v5jg8Xu197QDP5txp2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افتتاح متمرکز هزاران پروژه‌ خانواده ارتباطات در سراسر کشور
🔹
رویداد ملی «یک ایران متصل» به‌زودی با حضور جمعی از مسئولان دولتی و فعالان حوزه ارتباطات و اقتصاد دیجیتال برگزار می‌شود. در جریان این رویداد ۷۹۴۷ پروژه ارتباطی و فناوری اطلاعات در سراسر کشور با برقراری ارتباط مستقیم با ۳۱ استان به بهره‌برداری می‌رسد.
🔹
«یک ایران متصل» قرار است تصویری از دستاوردهای دوساله وزارت ارتباطات و تلاش خانواده ارتباطات کشور برای توسعه دسترسی عادلانه مردم به خدمات دیجیتال، افزایش پایداری شبکه و تقویت زیرساخت‌های اقتصاد دیجیتال ارائه دهد.
🔹
هدف نهایی این طرح‌ها، کاهش فاصله مناطق مختلف کشور در برخورداری از زیرساخت‌های نوین و نزدیک‌تر شدن به مفهوم عدالت ارتباطی است./ ایرنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/687493" target="_blank">📅 20:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687492">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
مورخ برجسته اسرائیلی-بریتانیایی:
طراح و معمار این جنگ نتانیاهوست؛ او یک روان‌پریش نسل‌کش است و هدفش نابودی ایران بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/687492" target="_blank">📅 20:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687491">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/051a0fae8d.mp4?token=phhf4toChYAj2IJf8bbeI0IeRl_cR4bW38glBHaFxEms_9HmVfZYkU5hdxVOneNbjSo1OWnZDhsT09UaVwZqtQqwCbHtYN6EDGnAP_bISyFVVEtRkfJuK1wKZE_da0Fp3jn0lDPDe0boyCFkW1ZH6vOjU2zpdUFo5TkTv4vXMMmXhsg4LKL6H96_v6qvkJ8p-dsbJwxmXKutBu0MlbcfQcbvTZTnFXe63oyybTvQVdgsmnwCRaaYlLV_t2xsyiD-lc3mS3TLzhNpsmKDeQNGAuBMLRPVsmbiQNRuQCRTkv2Yt0Iq5MgGzqRYKXNox_wshZBaMQNxpdGz97Ss9s80sJu3dgm3y_xFnGPbI7G7jKE0Zx2O_XQkDFJX2bvz0UwjQKjlrNRsRy45DJhp-cRjEDynFyM6Ro3wVhQqLsNjN4e3OdiIe82rgZa0oIHB-wY4lNETTqErfOMUYuylRGE7iAuMfsGWVHBNiX2AUs5jy0I6Vnyed8XsoT2yJA-UUHdqglpK4-BLLZAm-CMaV2m0FbHyR0bsoLKIYEb69v-EItReIdl-3Na259EeBFfBcY5X55fNZpdtCpmIfdU43AfRmYbPkBVKXfZM5ZJAqT3Nub6_8oDKTOx20FwrvDWA7R4XS-srlXY35uPr5n2jiKs4awUS7UfK_osEPMdwUZgSNWY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/051a0fae8d.mp4?token=phhf4toChYAj2IJf8bbeI0IeRl_cR4bW38glBHaFxEms_9HmVfZYkU5hdxVOneNbjSo1OWnZDhsT09UaVwZqtQqwCbHtYN6EDGnAP_bISyFVVEtRkfJuK1wKZE_da0Fp3jn0lDPDe0boyCFkW1ZH6vOjU2zpdUFo5TkTv4vXMMmXhsg4LKL6H96_v6qvkJ8p-dsbJwxmXKutBu0MlbcfQcbvTZTnFXe63oyybTvQVdgsmnwCRaaYlLV_t2xsyiD-lc3mS3TLzhNpsmKDeQNGAuBMLRPVsmbiQNRuQCRTkv2Yt0Iq5MgGzqRYKXNox_wshZBaMQNxpdGz97Ss9s80sJu3dgm3y_xFnGPbI7G7jKE0Zx2O_XQkDFJX2bvz0UwjQKjlrNRsRy45DJhp-cRjEDynFyM6Ro3wVhQqLsNjN4e3OdiIe82rgZa0oIHB-wY4lNETTqErfOMUYuylRGE7iAuMfsGWVHBNiX2AUs5jy0I6Vnyed8XsoT2yJA-UUHdqglpK4-BLLZAm-CMaV2m0FbHyR0bsoLKIYEb69v-EItReIdl-3Na259EeBFfBcY5X55fNZpdtCpmIfdU43AfRmYbPkBVKXfZM5ZJAqT3Nub6_8oDKTOx20FwrvDWA7R4XS-srlXY35uPr5n2jiKs4awUS7UfK_osEPMdwUZgSNWY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری وزیر کار دولت شهید رییسی: برخی کارکنان موسسات نفتی و پتروشیمی بیش از ۲۵۰ میلیون حقوق می‌گرفتند
صولت مرتضوی، وزیر کار دولت سیزدهم در
#گفتگو
با خبر‌فوری:
🔹
در طول تاریخ افزایش کالابرگ و یارانه در هیچ دولتی به اندازه دولت شهید رییسی افزایش نیافت.
🔹
در دولت شهید رییسی حقوق حداقل بگیران ۱۷۰ درصد افزایش یافت. در سال ۱۴۰۰  با تورم بالای ۵۰ درصد دولت را تحویل گرفتیم و با تورم ۳۳ درصد تحویل دادیم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/687491" target="_blank">📅 20:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687489">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee0880e45.mp4?token=Mv7iimG4PtJDZoneD3x7rLrmWUiIS4UwVPaQyJ5-KbY56KGukXPO_lE1v7msxwH6unSPi68U99P71u1jcd0sE6usEV8P93DW7MsHNPV7IUabp9kh9hAFArUTPzkVTXLblLdyBJuHM9KunBsVpORg0FrB3vEO0zcgxChzMYIdyI00c71La15lHl6CM3x787CGaxXAdvnkelRHIVSvBlohCqc98QBmx7FaL04r_vRSoxVNaNYzty6CumlRTE0nQv1Q-PE5Ymx1-H2Um-Q6pVd7uDHCsAZw60FI5273T7TJL9mG6F1U4NLwWHOh193SSxf3QJ1JHiKMTMzcZ5FOAdoCug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee0880e45.mp4?token=Mv7iimG4PtJDZoneD3x7rLrmWUiIS4UwVPaQyJ5-KbY56KGukXPO_lE1v7msxwH6unSPi68U99P71u1jcd0sE6usEV8P93DW7MsHNPV7IUabp9kh9hAFArUTPzkVTXLblLdyBJuHM9KunBsVpORg0FrB3vEO0zcgxChzMYIdyI00c71La15lHl6CM3x787CGaxXAdvnkelRHIVSvBlohCqc98QBmx7FaL04r_vRSoxVNaNYzty6CumlRTE0nQv1Q-PE5Ymx1-H2Um-Q6pVd7uDHCsAZw60FI5273T7TJL9mG6F1U4NLwWHOh193SSxf3QJ1JHiKMTMzcZ5FOAdoCug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فروریختن پل معلق در لحظه افتتاح اندونزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/687489" target="_blank">📅 20:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687488">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
آغاز مذاکرات پوتین با فرستادگان ترامپ در مسکو
🔹
کرملین از آغاز مذاکرات ولادیمیر پوتین رئیس جمهوری روسیه و فرستادگان ترامپ تروریست(کوشنر و ویتکاف) در مسکو خبر داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/687488" target="_blank">📅 20:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687487">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b76139f2e.mp4?token=LDPefTE7nNPu-gjkqtKdnVgyYYdYB95UEX81jL95ARqcoUu6VksC0Fde4U--SctDDIXg1UYrLQg9JpR18R-Ohl4V92FLK525FViZtkUZec3JTUgmfS5qUoznnUohdeesk54NSBqbS0mAR0QX3WXWMZWy8qE2Ggte9cDGRCtNMnZV08Qtqll5-SLOeaEWZwC82PuG0Zp00SNn8Wiit4qvYVc9nNjnsJsa76Cu9Sqq9DwTvF8SeI7V3Tp4M8dpeF25jrg4P9iP7eGjm-JiQ-eEneM4l84zDM7EvXwGTIRpYBCktUounzSOEO4xt62e1aSeP2nz1g-dCbwhvIv2FJBiiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b76139f2e.mp4?token=LDPefTE7nNPu-gjkqtKdnVgyYYdYB95UEX81jL95ARqcoUu6VksC0Fde4U--SctDDIXg1UYrLQg9JpR18R-Ohl4V92FLK525FViZtkUZec3JTUgmfS5qUoznnUohdeesk54NSBqbS0mAR0QX3WXWMZWy8qE2Ggte9cDGRCtNMnZV08Qtqll5-SLOeaEWZwC82PuG0Zp00SNn8Wiit4qvYVc9nNjnsJsa76Cu9Sqq9DwTvF8SeI7V3Tp4M8dpeF25jrg4P9iP7eGjm-JiQ-eEneM4l84zDM7EvXwGTIRpYBCktUounzSOEO4xt62e1aSeP2nz1g-dCbwhvIv2FJBiiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی نظم تردد ماشین‌ها به دلیل مسدود شدن مسیر راه که بیش‌ از ۹ میلیون بازدید خورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/687487" target="_blank">📅 20:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687486">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b3afd89d.mp4?token=I5v4D-TE2s-Mq3ybcF0Jr_2rdG2cToff0M5Y_D1jnjLskM3CI7HcsstD6hQu8k4ghSU0KfArtIni_rRDGxviYXwbegcZRGC7zl9H8RwJFLeqKZVij3CrVABZLR9JPwozh82nF6Mf2YgWvsGsABvu-vym_EsiL-1J1TpOV45nJickuP9Xd_cBTlep3ZvQ92mYXUg9_aeQ-1yZxZ1Xu6AVQTJOFya_b8HBauutLYMAmevs2mclBh8-3WbIRnofpsw9TQbro_RvFY1JcKJ8-Mbaoby_8BnEut7JBgHFod-6ZKP6Jr0-6SJnDsobS0ngDDlMJWERJGO80BJqOZMV32qYaL7-JrprU6YnhzY90FlI_uvJOWdMuRs_5PGXrpsLuK36jPGVni57k1TGWGI3lbm_36TNlxof4IPL7Dw9WaITLZykmarwfU9ICmaP9cEZukhmfhNnm_VOOKkc_FX7mXc-TTDQ88sZvJ-ULVbkEAPGi1pAE38RmeGrlhrks8jfNSfDLAEH58Dkfd4PaksSEjV6AeTsmjORlK_RQ6-Sc1oGh5hbm1PoFWTWjYxhFIJw0ISYJYn7io9qiDDbpifE6fBQGzzcO5qeRPQQyA0mYw_BUb-Coc-Ws8Xly4eBREdpTLsrdYW-g5fRd4kEvCzWvGadaZ9s5ccpYSYogSMCJYxL6wk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b3afd89d.mp4?token=I5v4D-TE2s-Mq3ybcF0Jr_2rdG2cToff0M5Y_D1jnjLskM3CI7HcsstD6hQu8k4ghSU0KfArtIni_rRDGxviYXwbegcZRGC7zl9H8RwJFLeqKZVij3CrVABZLR9JPwozh82nF6Mf2YgWvsGsABvu-vym_EsiL-1J1TpOV45nJickuP9Xd_cBTlep3ZvQ92mYXUg9_aeQ-1yZxZ1Xu6AVQTJOFya_b8HBauutLYMAmevs2mclBh8-3WbIRnofpsw9TQbro_RvFY1JcKJ8-Mbaoby_8BnEut7JBgHFod-6ZKP6Jr0-6SJnDsobS0ngDDlMJWERJGO80BJqOZMV32qYaL7-JrprU6YnhzY90FlI_uvJOWdMuRs_5PGXrpsLuK36jPGVni57k1TGWGI3lbm_36TNlxof4IPL7Dw9WaITLZykmarwfU9ICmaP9cEZukhmfhNnm_VOOKkc_FX7mXc-TTDQ88sZvJ-ULVbkEAPGi1pAE38RmeGrlhrks8jfNSfDLAEH58Dkfd4PaksSEjV6AeTsmjORlK_RQ6-Sc1oGh5hbm1PoFWTWjYxhFIJw0ISYJYn7io9qiDDbpifE6fBQGzzcO5qeRPQQyA0mYw_BUb-Coc-Ws8Xly4eBREdpTLsrdYW-g5fRd4kEvCzWvGadaZ9s5ccpYSYogSMCJYxL6wk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۵ ترفند کوچیک، کلی تفاوت در آشپزی!
🍳
#ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/687486" target="_blank">📅 20:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687484">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733e045414.mp4?token=bHT6hlOci_Yt06xwuMWSncOwZK2D6OcILafD0wzCxC2-IIXgmqiI7kNxmqIfF0Q9u2mza20JR2hzDeFmlvscAtyH54L-EULSG1nef3UOEZFp5Vkl9ZGK60YEukITbN8CMzxAU7rtrHtFiZLLy0tpPBMONBrx8ArskoFm-N9dAG2g5gPZo7Sd9IK7Uf2uWT9S0I7zm1-qfiTV5VyFhV5Cz-YyTMhdyFN8UFfyWhtTdzW-Tcxt5vc5p4OKfqxitkfYp5wY-xQdZVs3AkrwLMhd4gJuJ6IL1iPG-iwCf2QPieO8WRO__oE_QJVwhZCnzoxFxFBawEwTf1Ct3CzQxItamw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733e045414.mp4?token=bHT6hlOci_Yt06xwuMWSncOwZK2D6OcILafD0wzCxC2-IIXgmqiI7kNxmqIfF0Q9u2mza20JR2hzDeFmlvscAtyH54L-EULSG1nef3UOEZFp5Vkl9ZGK60YEukITbN8CMzxAU7rtrHtFiZLLy0tpPBMONBrx8ArskoFm-N9dAG2g5gPZo7Sd9IK7Uf2uWT9S0I7zm1-qfiTV5VyFhV5Cz-YyTMhdyFN8UFfyWhtTdzW-Tcxt5vc5p4OKfqxitkfYp5wY-xQdZVs3AkrwLMhd4gJuJ6IL1iPG-iwCf2QPieO8WRO__oE_QJVwhZCnzoxFxFBawEwTf1Ct3CzQxItamw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت اضطراری در نتانیا بعد از تیراندازی نظامی صهیونیست
🔹
به دنبال تیراندازی یکی از نظامیان ارتش صهیونیستی که در جنگ غزه شرکت کرده بود، نیروهای امنیتی صهیونیست وضعیت فوق العاده در این منطقه اعلام کردند.
🔹
رسانه‌های عبری گزارش دادند که این نظامی بعد از جنگ غزه، دچار اختلال روحی و روانی شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/687484" target="_blank">📅 20:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687483">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDD1Xvn4R5QPNTzlJvrGH8Zf3-VGcOPOXx4YLjMuuk347pwaX1uLyUVV2t6R7qD8hx1i4rx6sPWn-5isiqYZkbC6l_Wu7YPRGCF8yPDS6kc8eE3MzcQAzbj1r1Pri4o4Ck9CTDr_Thx7tZu1OTv2N-IGeDVxvDkJbGLYbuA6EfkglthqllP-0zfUh2TpKqgE21d8Hmvo2dZPqO4gU328SQu0N2bnrsjiUSCqM-4qv1XNX13S4vCIMj9VLyTwiKgwVADjL0CNe8-b8JH27mHM03qKX3K_Y11nCtyCEYAKz_6jooja7lgLAc-ZF2KqaRFnxGJE9SfUAr5D7cUQiGGm8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری؛چالش های شروع سال تحصیلی
🔹
اگر برای شروع سال تحصیلی با مشکلاتی همچون  گرانی لوازم‌التحریر، لباس فرم، هزینه ثبت‌نام و ...  مواجه شده‌اید، تجربه خود را با ما در میان بگذارید.
🔸
روایت خود را در قالب ویس (حداکثر ۳۰ ثانیه) یا متن ، همراه با نام و شهر به آیدی زیر ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/687483" target="_blank">📅 20:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687482">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
دنیس راس، مذاکره‌کننده سابق آمریکا:  احتمالا ایران در مقطعی تنش را تشدید کند، اما این اقدام ممکن است همزمان با ارسال پیامی به میانجی‌ها برای تلاش جهت یافتن راهی برای خروج از این وضعیت باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/687482" target="_blank">📅 20:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687479">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
عصبانیت هگزث از حملات ایران به ناوهای جنگی آمریکا
پیت هگزث،‌ وزیر جنگ آمریکا:
🔹
اگر ایران به کشتی‌های ما حمله کند، نفتکش‌هایش را نابود کرده و غرق می‌کنیم.
🔹
ما می‌توانیم تمامی نفتکش‌های ایران در دو منطقه سنتکام و اقیانوس آرام را هدف قرار دهیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/687479" target="_blank">📅 20:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687478">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">12 Ane Manaee (1404-01-25)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/687478" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه دوازدهم
حجت‌الاسلام امینی‌خواه:
🔹
شأن نزول "سوره قتال" در ابتدای شکل گیری جامعه اسلامی و اولین مواجهه نظامی با براندازان بیرونی [03:53]
🔹
"سوره محمد(ص) "، مانیفست مقاومت برای تحلیل فضای عاشورایی جامعه امروز [10:14]
🔹
"الهیات جنگ" یعنی، درک خطر موشکِ بدون تقوا و اقتدارِ بدون اعتقاد [18:22]
🔹
ترامپِ مشکل‌گشا و رهبریِ مشکل‌ساز!.. خطر نفوذِ نرم کوفی مآبان با پمپاژ شبهه در جامعه [20:16]
🔹
چالش استفاده‌ ابزاری از نام رهبری در خدمت اهداف برجامی! [38:53]
🔹
سوره محمد(ص)، نقشه راهبردیِ ورود به جنگ و پرهیز از جنگ [41:45]
🔹
انطباق با منطق رهبری، شرط لازم برای دستیابی به پیروزی [47:40]
🔹
فداکاری اهل‌بیت علیهم‌السلام برای حفظ "ظاهر دین" به قیمت“ گشاد بودن پیراهن خلافت” بر تن غاصب [01:04:05]
🔹
خطر بی‌ثباتیِ ناشی از بی‌دولتی، یکی از تهدیدهای جدی برای جمهوری اسلامی [01:12:36]
🔹
تحلیلی بر تفاوت‌های تفسیری تسنیم و المیزان، از توجه ویژه به شأن نزول، تا تمرکز بیشتر بر تحلیل عقلی- فلسفی [01:19:31]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/687478" target="_blank">📅 20:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687476">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de28e29cb.mp4?token=ML1qOobRtqBY2vbQlNxwORyAfhXA9k2rxXJjC6d19saLK0VX2fEn9yXnbfiMkbmcg4BJu8A-Ts1oedXwJPhpErg-17YqzkOibF5i1PdDQa7JaUW6Yu0sPfspn7DZskqt1jY75xUpB3GYyRt9EqkcQnAmZRHKSqq9DHZNzkPPNjMKRQAEHQiSNBuInvkclUzGfOUF1aqJZ4HFzp7NIRJJNUs7x4-ziA1bazUFND60gh2LDYJmyjaD-dXOwyoYURbQ0INOgczNDDpAdiSMTjhvQdXOOBwVuO-greriiSRDnInJDfHCRlymMW4y5ccOEPRdMfFC5hqRCLsH_L1KgN7GHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de28e29cb.mp4?token=ML1qOobRtqBY2vbQlNxwORyAfhXA9k2rxXJjC6d19saLK0VX2fEn9yXnbfiMkbmcg4BJu8A-Ts1oedXwJPhpErg-17YqzkOibF5i1PdDQa7JaUW6Yu0sPfspn7DZskqt1jY75xUpB3GYyRt9EqkcQnAmZRHKSqq9DHZNzkPPNjMKRQAEHQiSNBuInvkclUzGfOUF1aqJZ4HFzp7NIRJJNUs7x4-ziA1bazUFND60gh2LDYJmyjaD-dXOwyoYURbQ0INOgczNDDpAdiSMTjhvQdXOOBwVuO-greriiSRDnInJDfHCRlymMW4y5ccOEPRdMfFC5hqRCLsH_L1KgN7GHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزشی ۳۰ ثانیه‌ای که به اندازه یک عمر ارزش دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/687476" target="_blank">📅 20:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687475">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFfRBl8FyyVsJu2_1vszXGAKAHSGLUyA97Jm9-gt4oZCCp9DS-T6R9mZkkqFAMOqtqKJKTjv0c6m08oVcfXrsv5-bjEQA9Dqqu9YOet7QZqiB-D7AGgHMs_eVejndTeqrS1yR59UCo6jIxbP0q-mP1VzeuUk6KdjrP9o0GWF1eOjZGxthSXt4aluV9h1fxO5VMA9ZMw_ie4p3j8N1kEEN_c_QZ0CrGRI5jckltRt8wfY92F-KLIf0YGhmXCBkqmlDm6ZpnSz-tfq4AqeeCLG-6CS0ap0rlTBFrHM4uieGf6pw4xDpMlnCNNLgOPrLZNbIJKm3_KSZkZQyTvSM5aYew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اهدای یک سال اینترنت رایگان به خریداران مودم 5G در آمل
🔹
پس از پوشش سراسری نسل پنجم اینترنت همراه اول در آمل، ۵ نفر از مشترکانی که تا ۳۱ مهر ۱۴۰۵ اقدام به خرید و فعال‌سازی مودم‌های 5G در این شهر کنند، یک سال اینترنت رایگان دریافت می‌کنند.
🔹
این طرح با هدف آشنایی بیشتر شهروندان با قابلیت‌های نسل پنجم و افزایش استفاده عملی از زیرساخت تازه توسعه‌یافته در آمل اجرا می‌شود. خرید و فعال‌سازی از طریق مراکز فروش و خدمات همراه اول در آمل یا فروشگاه اینترنتی به آدرس
shop.mci.ir
امکان‌پذیر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/687475" target="_blank">📅 20:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687472">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163c87db5.mp4?token=PLZvjU9tY9-byaZfG2RHfFgAXLxt4ZWZUE5IsTM8kWlkMPi3YZz2s2nyEd0k7k7orpdOT5f9Wen22_zGrb2_ve8caVnHetF3H72BerHhQ4a7RLQ-4iXZQHgk5NfiarraYEbKNikvVabRF8YpVrADV2uPyVhZz2bgWkLc2-JXZK2pEL6BQzptQasauz9LWKt21DzN2tk38ue9nc46uYCZXF08Yhsv-55F7rfCkcjUA0prl4LvUnQYbKWGbMRDZPAdr_4Ib8JEI7g72lPI2RG1W_NME4lwk07M0PLNlz5FpeCgVDKCGfuuprqoppBl6d2Jy4Blguwl9eO-D1mH0V858w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163c87db5.mp4?token=PLZvjU9tY9-byaZfG2RHfFgAXLxt4ZWZUE5IsTM8kWlkMPi3YZz2s2nyEd0k7k7orpdOT5f9Wen22_zGrb2_ve8caVnHetF3H72BerHhQ4a7RLQ-4iXZQHgk5NfiarraYEbKNikvVabRF8YpVrADV2uPyVhZz2bgWkLc2-JXZK2pEL6BQzptQasauz9LWKt21DzN2tk38ue9nc46uYCZXF08Yhsv-55F7rfCkcjUA0prl4LvUnQYbKWGbMRDZPAdr_4Ib8JEI7g72lPI2RG1W_NME4lwk07M0PLNlz5FpeCgVDKCGfuuprqoppBl6d2Jy4Blguwl9eO-D1mH0V858w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر نیرو: زمستان سختی نخواهیم داشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/687472" target="_blank">📅 19:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687470">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvrYoy6FjQ57oXXKLbEySC3bFJaXeNjBDSSW1_yi3qRsoYRFBk8ge63NEaC5J12Orq6DGnV_Z7IcKcKohAQ7UbFk-yd-QcrCpUUu5LlFAOXPf_kRUOS9uWx7xroqB1jotzhVghWEebxLPSAM9CtjeS0g_kgn-Y7D8Gan96rormw7KnW8LpYfFPuE0MCrm8w6bcC1efHTSsnxfF2SlVU3i3SeNdvkH911Rw9Q0__hJ6BTbdCC8F2ohMxLXLais3SYPPsq9-NF5a3O7ifjzFMhpNKUDW_8OU7DudbqsOPtVQPLtmU3oEzJVATNDy8TW5yTPF7mbZvwVh1755mptwx1uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
تندیس «بارگاه امیرالمؤمنین (ع)»
این تندیس، فقط یک المان دکور نیست؛
روایتی‌ست از شکوه حرم و آرامشی که از آنِ دل‌های مشتاق است.
✨
مشخصات محصول:
▫️
ابعاد: ۲۰ × ۱۶.۵ × ۱۴ سانتی‌متر
▫️
متریال: سنگ مصنوعی
▫️
وزن: ۹۴۵ گرم
▫️
طراحی باکیفیت و باجزئیات
▫️
مناسب دکور منزل، محل کار و فضای معنوی
💰
قیمت: 5,198,000
قیمت با تخفیف ویژه: 4,995,000 تومان
⏳
موجودی محدود؛
برای ثبت سفارش، همین حالا اقدام کنید.
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop
@ghararshop</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/687470" target="_blank">📅 19:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687469">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a5487963f.mp4?token=O-OXqZGOh2a6jn7xzT_OxHjprwS6c_-L-Rgrf5qEGjMIOkBY8WsiTwww50DpaF6esa9UzN_8HqUTwjk-4iflijsi08uPr0E0ZQvwUJPeIv7YLGYxMVlSs-HE2P1Yq1QzsereNaV1S6ebVRkJCJ8RKdAhia7Tck5cxmW1LwsmtjBW0-HPPfS-OyrA2E3eyzVgMGXFQU9yptXVLDNY3e7TtfBtsjFIiQUljU4wxvyTHWicoEC3wNJaAeYuM9Qq0h9FjYsPb4jAMM84jIj5XIPGe3wRKjlwfnR9XnIrH4Cnet2U43VTa9cT_1Kqu48GNiC6nH07Ftdtuxi3IVTQk-sqtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a5487963f.mp4?token=O-OXqZGOh2a6jn7xzT_OxHjprwS6c_-L-Rgrf5qEGjMIOkBY8WsiTwww50DpaF6esa9UzN_8HqUTwjk-4iflijsi08uPr0E0ZQvwUJPeIv7YLGYxMVlSs-HE2P1Yq1QzsereNaV1S6ebVRkJCJ8RKdAhia7Tck5cxmW1LwsmtjBW0-HPPfS-OyrA2E3eyzVgMGXFQU9yptXVLDNY3e7TtfBtsjFIiQUljU4wxvyTHWicoEC3wNJaAeYuM9Qq0h9FjYsPb4jAMM84jIj5XIPGe3wRKjlwfnR9XnIrH4Cnet2U43VTa9cT_1Kqu48GNiC6nH07Ftdtuxi3IVTQk-sqtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر نیرو: دیگر قطعی برق برنامه‌ریزی شده نداریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/687469" target="_blank">📅 19:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687468">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
جان باختن ۲ خلبان اف۴ در یونان
🔹
خبرگزاری رویترز به نقل از مقامات خبر داد که در پی سقوط جنگنده آمریکایی متعلق به ارتش یونان، روز شنبه هر دو خلبان جنگنده جان خود را از دست دادند.
🔹
این حادثه در خلالِ نمایش هوایی در پایگاه تاناگرا در شمال آتن رخ داد و جنگنده در فاصله حدود دو کیلومتریِ فرودگاه سقوط کرده است. گزارشی از مجروحیت عابران یا ساکنان منطقه دریافت نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/687468" target="_blank">📅 19:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687467">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
هانتر بایدن: ارسال تسلیحات به اسرائیل اشتباه بود
🔹
هانتر بایدن در پاسخ به سوالات مهدی حسن، روزنامه‌نگار انگلیسی، اعتراف کرد که تصمیم جو بایدن برای ارسال تسلیحات به اسرائیل اشتباه بود، سلاح‌هایی که برای نسل‌کشی در غزه استفاده شد.
🔹
جو بایدن از دوران سناتوری تا پایان دوره ریاست‌جمهوری خود، یکی از حامیان بزرگ رژیم صهیونیستی در آمریکا محسوب می‌شد و از معدود سیاستمداران غیریهودی در آمریکا بود که علناً خود را «صهیونیست» معرفی می‌کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/687467" target="_blank">📅 19:44 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687466">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای فاکس نیوز: نیروهای آمریکایی پس از آنکه ایران به دو کشتی جنگی آمریکا موشک شلیک کرد، سه نفتکش ایرانی را هدف قرار دادند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/687466" target="_blank">📅 19:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687462">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bXuvTbL9tTKkKpe7WtuZKegwFYOiZDKyVKvU93w8DfrnUbnPOP2oSOn5-pCZD0fvwITZ0mhn7xWIKaAZHbi9OnAzS8tnAPg7m0QgvfkyQAmLUgP45pQBi_ukZV9XogvgUumxnGXzrj0fAFPcFGT9nUFVImuKHrWumpzUYmnrQgZQ5tmTV6GwocddeZ_mlqLVQtoqzjxs-zKe70KNcaWTbpdwr2bXpDQWoP5X4LiUiS7Xqqldl60xyB3HoTucdxg6nwhFC2fSyoB4r9T6hI-B26qzs_juuvrmK3fF9Oe1nSawCf5Zg5o4u4xY96SBedqVkHlLav9bKfggWpE3x7Gd2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qoNrQyBm15tyTcek5Q6rpqJCZ-FHZE0Pd7MGlLSyNUaB3CC5KOVWoTUbx-i0IWErm67-uR38q7ceHieJfwsh1NgsAxiTZFI0xXatdFl0oKzFww0BrwTB0DSYWP166aexJ3HLBY6m6ZQEE-BGWSfJXX9dj8tWbWFg47K3sBc1rxSV2NqQfljIwzwy29z9wfX1t6ZjsAWju1R3nrOaKtueM4INr7hpEKmW3ku6OGfTkK8BVtgxKWvcf5cMhZ8cgRlcS8cHuaFykoP_JYczpL9qH29LzupzI5vDoGV6f0NOUJ_CwJZMnsdP3TaIJ-8KBtLCuezLTWjbujtMuIcQBJrovQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X1Wi_BYBdw5EMJdifQ6oXDe1ZvxRBwUvZ0XuYQPcNG29ihg7geQWyAIE9nDUOx7mjJc5wV3wK_libd0FIxaC8WT3ttSj4L2R2GwSG_fRckv7GRWzFLKm1ZxVzDvOhehylOrw43I8fF6lOxJlHOyg2Efa3nmZPXxB_OvepTMGmC6khpL2wvWwMYJhhdvC9zC1SNBgRrM25UMJWQ7cOLiUc2RKVC6U76j42EJkBs0AWfmSS4y-L6rdWLoLIjchpRDzinSGFjJD-Cd6-AZhrGPlMjzBNR694DECXTVr-3Z7AyZ-az-hPNSHZS9P7rnnjCNUD3j1Gea5iMlKuLjWjW4-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A7taUyfNYNXt_KVO26VkVFwQKSP6uyOAjy1U_6Tg7NXP5ihZg4_mV43nNbxq0fkyBN6AkicWIDjXxauYd72Ti43CfSIXge4zUibF9dk-TJY86doAQHEe68bvRpJIQgAZUCQCp7uDkzsUOPXaS9YaV8HfI43b_P7PFHybjHh1lHUfNk4sfV_QtasE0fNJ-dbXPxk2Es_OIqJUCxNbpRSMZLvVDOReI2qZdCkwbiKqL5SBu3FE6LsEsFSDdMW_AM_TG_TpN1khZZa9yWMlKSP6fdUX0qM_V5xYFcJePib-XxTd7X2QEP1rA34v6eoIgBxozPEEq5iYmYY0KrQvaMTYEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
«تابان فردا» وارد بورس شد؛ هلدینگی با سهام ۸ غول نفت و پتروشیمی ایران
درباره‌ تابان فردا بیشتر بدانید:
🔹
تابان فردا با سرمایه‌گذاری در زنجیره نفت، گاز و پتروشیمی وارد بورس تهران شد.
🔹
بیش از ۸۹ درصد از مالکیت تابان فردا در اختیار شرکت سرمایه‌گذاری اهداف است.
🔹
خالص ارزش روز دارایی‌های تابان فردا حدود ۹۶۰ هزار میلیارد تومان برآورد شده است.
🔹
تابان فردا امسال ۲۵ همت سود محقق کرده و برای سال ۱۴۰۹ چشم‌انداز ۳۲۱ همتی دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/687462" target="_blank">📅 19:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687461">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
صولت مرتضوی: اساساً میدان رقابت‌های انتخاباتی میدان وعده و وعید بوده است
صولت مرتضوی، وزیر کار دولت سیزدهم در
#گفتگو
با خبر‌فوری:
🔹
اساسا داوطلبان و نامزدها در انتخابات طوری برخورد می‌کنند که اساسا تمام گذشته را زیرسوال می‌برند و این اغواگری است.
🔹
آن‌ کس که فراتر از توان اقتصاد و ظرفیت کشور وعده می‌دهد، قطعا وعده‌اش دروغ است.
🔹
اگر کسی وعده بیخود داد و نخواست وعده‌اش را عملیاتی کند، لیاقت و شایستگی این مسند را ندارد و مجلس باید حتما برخورد کند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/687461" target="_blank">📅 19:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687460">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
حادثه دریایی در شمال خلیج فارس و دریای عمان
سازمان عملیات تجارت دریایی انگلیس:
🔹
گزارشی از حادثه دریایی در شمال خلیج فارس و دریای عمان شامل چند کشتی تجاری دریافت کردیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/687460" target="_blank">📅 19:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687459">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4010eaa.mp4?token=n8NK-w09nWy70HLf7zOJ0N65FxWn9RZFeT6C24tUSjisGmlzXA3_BwrxLuYXFdFhiNcChKOD47TtUbrlhVG7Y56IbtzCNqrtH1mnUezR-2q9DkABIbpxCkn0YK3MPK6huU0hJBDzwD3-e4dHDhXFx8Cx5TK1l5ze5EURrWWBjmZ0GuZPX3YH_qIUS24BHZumYMJ0aaOrmb8nAy_rWL0EpoR7k8ouFN4GshFGCxi2XUPksS3s0NyuBTIAHceQCUfvU01De2rYwiN1a7BPpX0y4jNACpZRBQnqIi5xSKjJYvAyThERBTXhh6fQVOtDLRCiHMWJUt2cgXMNk3Iz8baKxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4010eaa.mp4?token=n8NK-w09nWy70HLf7zOJ0N65FxWn9RZFeT6C24tUSjisGmlzXA3_BwrxLuYXFdFhiNcChKOD47TtUbrlhVG7Y56IbtzCNqrtH1mnUezR-2q9DkABIbpxCkn0YK3MPK6huU0hJBDzwD3-e4dHDhXFx8Cx5TK1l5ze5EURrWWBjmZ0GuZPX3YH_qIUS24BHZumYMJ0aaOrmb8nAy_rWL0EpoR7k8ouFN4GshFGCxi2XUPksS3s0NyuBTIAHceQCUfvU01De2rYwiN1a7BPpX0y4jNACpZRBQnqIi5xSKjJYvAyThERBTXhh6fQVOtDLRCiHMWJUt2cgXMNk3Iz8baKxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار تانکر سوخت و جان‌باختن ۱۰ نفر در ورودی سنندج
رئیس اورژانس کردستان:
🔹
درپی وقوع یک حادثه رانندگی منجر به انفجار تانکر سوخت در محور سنندج - همدان، ۱۰ نفر جان باختند.
🔹
عملیات امداد و نجات و پاکسازی محل حادثه همچنان با حضور نیروهای امدادی و آتش‌نشانی ادامه دارد.
#اخبار_کردستان
در فضای مجازی
👇
@Akhbarkordestan</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/687459" target="_blank">📅 19:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687458">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال:
۲۰۲۶ به «سال از دست‌رفته» اقتصاد خلیج فارس تبدیل شد
🔹
امید به بهبود شرایط اقتصادی در سال ۲۰۲۶ عملاً از بین رفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/687458" target="_blank">📅 19:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687457">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksUMoQuPyKTux1iQqnm3jMqGlqM7bOXPGju71ajm0mlHXrzpKKovdNkkjtHt_DBw7GJNHr1_p4dtcTekfYbl0sOUZenRGTogYgNpOpM1lyLvnLo-uTF1_Vq0I3blo3Ur1PhvLIwjX5PIAmErV7i6xPiVbgBGGHISHvgkEqXNEyKEgukpI2ggbWaez68hG80bhqLki2t3GOlPnaVFL5Fd5YDyLzUDjVmEg34DRdz1SnEZrse9WRG1vtk11owYjIDjgll9-XzUp-torWpDdbFVLq9uWRZ2kxO7owRTx6qiW4MsV5497uo6nh2BWipbZIinEw_FuQRcGN_U3fc8RS8TGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز پرقدرت
#اسکورت
روی پرده سینماها با فروش ۶.۵ میلیاردی و همراهی ۳۵ هزار مخاطب
🔹
«
اسکورت
»، پدیده‌ی جشنواره فجر پس از سه روز اکران و همراهی ۳۵ هزار تماشاگر، در میان افتتاحیه‌های پرفروش سال قرار گرفت و پیش‌بینی می‌شود این موجِ استقبال روز‌به‌روز گسترده‌تر شود.
🔹
با نقش آفرینی:
امیر جدیدی، هدی زین‌العابدین، افشین هاشمی، مهدی زمین‌پرداز، هادی شیخ‌الاسلامی و با هنرمندی رضا کیانیان
پخش و تبلیغات این فیلم را،
شهرفرنگ
برعهده دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/687457" target="_blank">📅 19:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687456">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5b18bebc9.mp4?token=MztnwxwC9cyeXq-CiY1myW4-Gaq5XnFvxkkNoap3xEI4C-pYe3hs4YvjHipW3uMC12AWJLz1HoOZ_dLAD-qPgt8F3q5RkbczOlwx6wL-aYG4b728-8km3D_QsPOZagtMM9Xd2qSeZPd6VV3SwBCUede8Myjs5PHInhiThxq9rmdbgErmMw29XrKv6I_sMk4CeXhCihs8thAzDS-stCrleKWT1r1l9Qxe1fB794V7HG7Q1YJHkElq-saxZlegypOeYlJn0gKZDQtDeE9zULg75_9J9u4bRRnvQiusqphTZgMFGIpe9OivdsII8SvoQWLrYoIfJEnBdgr4aPNsSwJOUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5b18bebc9.mp4?token=MztnwxwC9cyeXq-CiY1myW4-Gaq5XnFvxkkNoap3xEI4C-pYe3hs4YvjHipW3uMC12AWJLz1HoOZ_dLAD-qPgt8F3q5RkbczOlwx6wL-aYG4b728-8km3D_QsPOZagtMM9Xd2qSeZPd6VV3SwBCUede8Myjs5PHInhiThxq9rmdbgErmMw29XrKv6I_sMk4CeXhCihs8thAzDS-stCrleKWT1r1l9Qxe1fB794V7HG7Q1YJHkElq-saxZlegypOeYlJn0gKZDQtDeE9zULg75_9J9u4bRRnvQiusqphTZgMFGIpe9OivdsII8SvoQWLrYoIfJEnBdgr4aPNsSwJOUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقاد شدید نماینده کنگره از دولت ترامپ: مراسم عروسی در ایران را بمباران می‌کنید و یک پسربچه‌ی شش‌ساله و چهار عضو خانواده‌اش را می‌کشید/ زودتر این جنگ غیر قانونی را تمام کنید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/687456" target="_blank">📅 19:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687455">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
گزافه‌گویی فرمانده سنتکام علیه ناوگان نفتکش‌های ایران
🔹
دریادار «برد کوپر» فرمانده سازمان تروریستی سنتکام در سخنانی خلاف قوانین بین‌المللی گفت که در صورت لزوم، ناوگان نفتی ایران را نابود خواهد کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/687455" target="_blank">📅 19:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687454">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2293727863.mp4?token=M15XXwdiMuSmkW4Dhyhvmmx3N5Xg7R3dY0CXNR5V1UzhlWjWRwr8A5uZfW7BQ-hqlKvA79eAjzgFRVaWVIweF7VGFQu0lu4WJtMAKEIXwEPPbSct2F9YbrHORz_snJmEDvJ62IL8vzuv70mNlDcRYH0lpDT9wztAh7fDF3z8IYkSSSWmSHvdz6xji4fVyoe-_keQ3uXJti1Z8uyhx_u6ThVSEsb5gSYsgaEbPsPC0V9LHxC2eVFz4JCzeZMX_9gt7Ui_br7PtE2SVxp8h-1Xo2C1JXBEfNDgrmLqzU8cKcV_LLmV3XUS6pvoQuSNb2Da6sEtkR5LkJrwcmeoqwMmhi6A9BZoy5v5YIf248BxpGO8QAytNYm8UU_TBSAqDx3iXR_ReP54zgVeT2fOr9hJjNUbBpOhxCZaxGwgQ1SeGy457z79HZfllqBrd-cPspjNDop9fpQ1LCkZTI7kwdKBxXS5kyspH94zy2L7VPATt57wJMhjr5RxVrlUbq0PRuFV4lpq2OkLUtrEPe3ojPyS9ffGLps6JTSxn3XV-7dvKiVq9iAfw_uFN-RK8fAS6zrV4I3ErRdjBFLID0WIvs5AkdQKPaCUE7Uzltu7TUgP4SKnJIO-J5esF_VIJJA046BgbRYPU7O0Uep2JyhkpDhfn22rS7BZCGFsE7bVj3DUkIs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2293727863.mp4?token=M15XXwdiMuSmkW4Dhyhvmmx3N5Xg7R3dY0CXNR5V1UzhlWjWRwr8A5uZfW7BQ-hqlKvA79eAjzgFRVaWVIweF7VGFQu0lu4WJtMAKEIXwEPPbSct2F9YbrHORz_snJmEDvJ62IL8vzuv70mNlDcRYH0lpDT9wztAh7fDF3z8IYkSSSWmSHvdz6xji4fVyoe-_keQ3uXJti1Z8uyhx_u6ThVSEsb5gSYsgaEbPsPC0V9LHxC2eVFz4JCzeZMX_9gt7Ui_br7PtE2SVxp8h-1Xo2C1JXBEfNDgrmLqzU8cKcV_LLmV3XUS6pvoQuSNb2Da6sEtkR5LkJrwcmeoqwMmhi6A9BZoy5v5YIf248BxpGO8QAytNYm8UU_TBSAqDx3iXR_ReP54zgVeT2fOr9hJjNUbBpOhxCZaxGwgQ1SeGy457z79HZfllqBrd-cPspjNDop9fpQ1LCkZTI7kwdKBxXS5kyspH94zy2L7VPATt57wJMhjr5RxVrlUbq0PRuFV4lpq2OkLUtrEPe3ojPyS9ffGLps6JTSxn3XV-7dvKiVq9iAfw_uFN-RK8fAS6zrV4I3ErRdjBFLID0WIvs5AkdQKPaCUE7Uzltu7TUgP4SKnJIO-J5esF_VIJJA046BgbRYPU7O0Uep2JyhkpDhfn22rS7BZCGFsE7bVj3DUkIs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر آموزش‌وپرورش: در مدارس دولتی هیچ مدیری حق دریافت شهریه هنگام ثبت‌نام را ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/687454" target="_blank">📅 19:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687453">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/593d9a8f06.mp4?token=WVePxenTtgBCCg9V8wCDaPsogw8-AjSex7ZBXotgpMHEs_bhrX5gU0ke6Qb7KZmwCJ1prSBLDlK81Qvejf_0xOueNFrsS4fwTnmF1I6lVddJil4hCpHtREqIAFfYOMB3MDINPBLKvaK5VJTLpEkmEbpi9XKT9aV8WBc0I9kHywnYPjw1LHRtY9QAQdowgv0josgNgJvkwtld_Vs8_MGiQorbsAcCDLAKRajrbjETH6vVA8XG5mC9yKTh6bCRy5LjjWP87iAHAhq1AFq4PsAOvwZLuC3O2U4pvxGr4LINjM0vv-vqxM_q6X_j-T0uNFy92tTtftaH7aiW9n1SmmdOFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/593d9a8f06.mp4?token=WVePxenTtgBCCg9V8wCDaPsogw8-AjSex7ZBXotgpMHEs_bhrX5gU0ke6Qb7KZmwCJ1prSBLDlK81Qvejf_0xOueNFrsS4fwTnmF1I6lVddJil4hCpHtREqIAFfYOMB3MDINPBLKvaK5VJTLpEkmEbpi9XKT9aV8WBc0I9kHywnYPjw1LHRtY9QAQdowgv0josgNgJvkwtld_Vs8_MGiQorbsAcCDLAKRajrbjETH6vVA8XG5mC9yKTh6bCRy5LjjWP87iAHAhq1AFq4PsAOvwZLuC3O2U4pvxGr4LINjM0vv-vqxM_q6X_j-T0uNFy92tTtftaH7aiW9n1SmmdOFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه حمله آمریکا به تأسیسات هسته‌ای ایران در قسمت جدید سریال سیلو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/687453" target="_blank">📅 18:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687446">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SPBYPObdzCLBl9rDIboO0dOR5Y5Yt33xWi1YBwo2UdVLe149cBWkZiD0jmH6tzpOoi1qXYeM24gauskQCmOc8wSViXumKPkKSyefapBjI62ugMSxtZsTIWHHM_c0M9R4FOK-UjF-aVko5nArrhw9ASHVC6hFpTJsZ5jnI1vu2P0uiXOkhfYBUfuny8vpzcke4Boj5uP-REEBUeFBvwxNq5mFmsvkRLtDH-wNLYXWnLPW_fcMcfpYRpzLy8J5Is34ry9B_5XrO1_chC-ZXnqTTl2M6_84hQqCFjyqm3cHX2vR8p7S9t9-tAe-b5CexnIgSodeY4VwruNVnaqTR6l-jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SP9DxbXe8uXVe_-YLwM9OnR0VNTHV64dNgmlNA8m5-3Wu0YBXS8QTDiqGNLMccUdh23jOdYxzCVH9_JEOMOPv2Zm0alyQPCihn7S8xhPZdvY3rOKYisR-CVFsMpCuhjMucyiPWQ896fujjTyFhER9gs4Br0BJRQ3l2Fr6ORPBKHGfucA3GwrFyQGI5-MFOSgx4H7HuUkMwZcWf2Uq2OpetIhPfIBRLtEhuYBNSNrF8RGVmvVflp6GQnK_fovpUMp7V4TGOuOHBDyQqTd0qm_trWNHDlmGHabNlJBwrJP0rioHdjDmqcVFwzPpVVi2wMKnUvZvXegv-Ax5J7X39793Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S8o56VYDC1WaH4dECWvjjFWwrGea2UcSsBr--a2qb8cbg4HlYiTISFcQMwIrsxNcXZ2iXub4CmBmb6jeAVU381WJx7_Bgv0zccVzRf_1xQB4rmNL2dUjGc7qrgb39gsENY5o_iSXggfB1QwVNrX5y5JOAxvT3eu52kwDZvkHZFy30XzQcFB_ZffuFphlG-evq8LxEaW_gMhV-3N8TK35ZyYnm1b5IDAdKGoXK4I9YKPNXH24oCsXZgwvDmgeRFmMF3k5Qhu5lXUzTiQqi69ZwdhgzrHOC7MW7Xrg8YBDMAVgwITrDugzN6d5jN57MVjyBYpmUcW32EASxhjKHCaMsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VWgQPm2_hgwtw4VcNaI-mPV0xzOvUQ1XllKIczt6W6SBJv4iFpzoehIEFx1H2TLjRYmbb_oUfR5URFFvhXTnEiO7dqZVfFwYQZ2Go8l_hoXHht2YEBCVevykMipydqubateKa2_FLX62kCpz1xqFbzj_daaBxPtZrVI0orG--sUhM5AKcpshApq-yPe5SULicwfsVL5X9wqBMfmrz60z0IHu8KP2a6wp6uxsmLwQ-ztr8mmAqDD-GnYnJkuQPvwgx2_d-XlAUimVup-vVK-4E5COl3TAY45Eju-5aiDflFzyb3PUOqYQaWNTdAMkxMVOiZ5ODmR_Cq1RKcZ_E4gNkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ADHZICdNjUkMKALZytwSiUGjCY7AwoSakxxNQIgkp5TJ2kU6NDhm0-bH_WID2g-v-7ob_oPzynLlhGohjHOWWI35phIKTDK5yBG8R3lbAYUsKCbRo-cuvS7i1V_UyStjV0NImsadQhD4izxM_vd058sBdD5v3-KQHM8EyZ7fQWpPrpBYqQkUx7KXLzm_4mgXGllhcNMxlLBHVQwkKfyJ6LAZxmGNzqoqIYgL9aMJZVF4FaI8a9ZfIeM5pJw-71iQdrD_PYf6hdDCmyJa6Ejq5DoQFvAJJDYzXV0avWgs1jDjiG4xnJNguVBb0yLELzSksM1lFewnAxXN1YtcapTIfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jxJNGUqKWyLI-CYlwsnk4BrHscjAfssYaHVBOwCKGAUr4NfSgTaO-JO-eRul0Oaosh8_kuBOt5cv0ZzEuWJGufJv_JW_sY91wV8tzj7T8Xj23gtaQcOqveoUEVh5zkDjNUQYvPRJmeN2HpQesl4gq6AvbFFqYd7uQG10nBLy-3xwQgF032DS42N2aNTfJ32Fl6Zn0HHRKucW6AnShB71qzk2HnFQGa4xYLc_nr_mgIL-KM23B5YmOkZ3tmrvZcZB2BELUlVCl5GaMo3YhwI89h31HJ7w-fT5KRlJuyMzQKDTYXeUcPkQWegBfYO5LpejbpZNeQU6HZBf9d5F_LCWbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FWc4WC62UbKwnCT5dpKFGZCv6x3yWwoP9gHaDxQXmjBKbp7KJ5v7Ytnw6vuM4QMYsPf--XsbOAYMSQ-Mk1IU6FIWvDbkxwMQHUzQEu_RhOUdKBU3WYplmUQD8ueMqzMY_IHGzG5vKZcpOPzPvS7Xirl6qJqbFYdEqIPQDUqokAgpBK4FBah8zva9AQCCkvIut2WwEW29bdsUs1TWUS67xeG6M7NwNHxtPCZCz68RkWS5l25T91UP6-KOYrfX-6PNsNxD7NvIB_2HpqGBDk8_H_F6F7D4Odt0GLtlU0Br5pTQb3fhK_EyH6946xDm70uDjJEpV_qEzZBCdkT9puqS6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
در آستانه هفتاد و پنجمین سال فعالیت بانک صادرات ایران
🏛
موزه بانک صادرات ایران افتتاح شد
🔹
موزه بانک صادرات ایران با هدف حفظ و معرفی میراث تاریخی و فرهنگی بیش از ۷ دهه خدمت‌رسانی در پی برگزاری آئین رونمایی افتتاح شد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#موزه
#روابط_عمومی
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/687446" target="_blank">📅 18:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687445">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
پوتین دستور توقف حملات به اوکراین را صادر کرد
🔹
به‌مدت سه روز هیچ حمله‌ای به کی‌یف انجام نشود؛ این تصمیم در چارچوب مقدمات سفر هیئت آمریکایی اتخاذ شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/687445" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687444">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
ادعای سنتکام: نیروهای آمریکایی سه نفتکش نفت خام ایران را هدف قرار دادند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/687444" target="_blank">📅 18:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687443">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
ساعت کاری ادارات تغییر نکرد
🔹
با ابلاغ رئیس سازمان اداری و استخدامی، ساعت کاری فعلی تا پایان تابستان باقی خواهد ماند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/687443" target="_blank">📅 18:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687442">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCvmwXvUF8jXu9kCG5rBD31aMfRPFaeoV_2BR-k6K-AmKIdsddn65RVLizXNS1g48pix-U0S_imbZ0KidO_jAIISUNE7vuyvz2zUlIwBcXVFPaWYCXdpOeHZr5Bz3nZSageonzu85eIy3asuHTmbr9N8X98xs0uo5eHDQxwG9jL2qwEsrZw6tEtrgmAMaPhWASW3aUnyue-3QpzTodzWd6SIx7CnkbKXBPFz86iMgjT-bPbH27wbMt5WCSieY3fDSr5dcvjkrPyraj5HwQ3GzOYsNsOLYVYqPubwf6ovOeWj5XBS8FfnQ9dUA2C1MY-QHlpYCEgsmtiEHUp55pM_fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاروان زندگی به شهر زنجان رسید
🔹
همه باهم برای ایرانی قوی
💪
🔹
همه دعوتید به رویداد کاروان زندگی،تجربه‌ای نو
🙏
🔹
با محوریت موسسه فرهنگی هنری تبیان(پرسان)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/687442" target="_blank">📅 18:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687441">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
روسیه: اعضای گروه ۲۰ خواستار پایان جنگ آمریکا علیه ایران هستند.
🔹
نتانیاهو: هیچ بازسازی در غزه انجام نخواهد شد.
🔹
زلنسکی: آماده‌ایم تا ۳ روز از انجام حملات به مسکو خودداری کنیم؛ انتظار داریم روس‌ها نیز از حمله به کی‌یف خودداری کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/687441" target="_blank">📅 18:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687440">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
تصویر ادعایی سنتکام از هدف قرار دادن ۳ نفتکش ایرانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/687440" target="_blank">📅 18:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687439">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5cdd869e8.mp4?token=f07rO0eXtykZz_9nUeNi-UOFxyKnmL5tEUGKhiCLjQWVLO3qE2wbgcDdQC3LGnGBxhu7uTrE7TTyavVaJ59dQUm1-wvz45vDTJeBwlWy1BEB2dmZ5HwbXmkLJIIiPEMs6CUiGlFoATNAcBR1m6LKPdFWxcZrQAOzqBxAr3sl64W-kohjlyb2TM30RJeHTKCnjcL9BoYMuIow5_QVQyMa36JDOyTREhFhKFGXKlDbWzo_lGdkiBNVRjQQh6JX-jvX9e7mGtvF_WK7QcMA_6QTVirTY2VMCCgHVvpFyMOIfxefxr03U2twGlcbcXGPc8WqiFrpQGVOxyM0S9XZI95rIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5cdd869e8.mp4?token=f07rO0eXtykZz_9nUeNi-UOFxyKnmL5tEUGKhiCLjQWVLO3qE2wbgcDdQC3LGnGBxhu7uTrE7TTyavVaJ59dQUm1-wvz45vDTJeBwlWy1BEB2dmZ5HwbXmkLJIIiPEMs6CUiGlFoATNAcBR1m6LKPdFWxcZrQAOzqBxAr3sl64W-kohjlyb2TM30RJeHTKCnjcL9BoYMuIow5_QVQyMa36JDOyTREhFhKFGXKlDbWzo_lGdkiBNVRjQQh6JX-jvX9e7mGtvF_WK7QcMA_6QTVirTY2VMCCgHVvpFyMOIfxefxr03U2twGlcbcXGPc8WqiFrpQGVOxyM0S9XZI95rIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیلی ساده و کاربردی میوه‌ها رو به انگلیسی یاد بگیر و کم‌کم دایره‌لغاتت‌ ‌رو گسترش بده #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/687439" target="_blank">📅 18:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687438">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f07a869d6.mp4?token=qTkRWkTAxsggKJ8emb_eCgJziCkFwcSG1KvIF7ioQ059nPe_CguZg42rKwChLpgoqZCIgRJO_qLlakQN3IIXpkuCAxT5czD6ixn1NnRctZOYRSUz7MfdaXHZ0bjeAe_tYNKjLxn2fEUucAU4JKzK2XgnSYRqM-ZTH3R9pKjE_meFVgfy4KL050ohfEOu-60w0JgC2p0zUyKIZGrpYhOiwKDvRVvr4Fykvtnz1I65f3sZRQTLnCECBzHR4ZFPBJvRbmqiFszoCCY0XLtzP4hqVyQiVshDH5NgZHl6c32XELXdMqw24Rf8ltTiu0-OVXsvwjd9u1o_V7dEzf0wEhpIUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f07a869d6.mp4?token=qTkRWkTAxsggKJ8emb_eCgJziCkFwcSG1KvIF7ioQ059nPe_CguZg42rKwChLpgoqZCIgRJO_qLlakQN3IIXpkuCAxT5czD6ixn1NnRctZOYRSUz7MfdaXHZ0bjeAe_tYNKjLxn2fEUucAU4JKzK2XgnSYRqM-ZTH3R9pKjE_meFVgfy4KL050ohfEOu-60w0JgC2p0zUyKIZGrpYhOiwKDvRVvr4Fykvtnz1I65f3sZRQTLnCECBzHR4ZFPBJvRbmqiFszoCCY0XLtzP4hqVyQiVshDH5NgZHl6c32XELXdMqw24Rf8ltTiu0-OVXsvwjd9u1o_V7dEzf0wEhpIUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«آبراهام لینکلن» از جنگ با ایران تا دعوای مستی در تایلند
🔹
ناو هواپیمابر «آبراهام لینکلن» که ماه‌ها در جنگ علیه ایران حضور داشت، پس از پهلوگیری در تایلند شاهد درگیری دو خدمه مست خود در پاتایا بود؛ دو نظامی آمریکایی در پی این درگیری تا پایان حضور ناو در بندر…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/687438" target="_blank">📅 18:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687432">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| تهران روشن |</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0259de181.mp4?token=iVBQAWo0rJ4qfOs9NFUJFTKDnUCM85VaPjJ_szTyqySYOjYhMVY_1i4KNTwlK4BjF5okroNZzSCamlMPGGEWocq-toYZw_F5ndpDKqY9o2fn4em4MHUtCAvcfu2BBX7Ko4CooM8Ir2UaJSP3dPD1K7Gm7KuHtFiOI4USRPHqAAeUv_mbbbGUVmiURwmyFB-CIB9Oy3cJELy6aoQ8Xe_tY2NuXA_UvIk7_r6sjqOHGGRCW5gx5cHlYBJmIsPiFfMmHb_1W6GVPxUyRVFdUcbzZCkwrAqoLAC26hR-j85pgSpCUil-vma0VXbz03Ci-JClalaZQ1NmzqR0pWgKlCoGrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0259de181.mp4?token=iVBQAWo0rJ4qfOs9NFUJFTKDnUCM85VaPjJ_szTyqySYOjYhMVY_1i4KNTwlK4BjF5okroNZzSCamlMPGGEWocq-toYZw_F5ndpDKqY9o2fn4em4MHUtCAvcfu2BBX7Ko4CooM8Ir2UaJSP3dPD1K7Gm7KuHtFiOI4USRPHqAAeUv_mbbbGUVmiURwmyFB-CIB9Oy3cJELy6aoQ8Xe_tY2NuXA_UvIk7_r6sjqOHGGRCW5gx5cHlYBJmIsPiFfMmHb_1W6GVPxUyRVFdUcbzZCkwrAqoLAC26hR-j85pgSpCUil-vma0VXbz03Ci-JClalaZQ1NmzqR0pWgKlCoGrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت یک تشکر ساده اما عمیق از سیم‌بان‌های فداکار صنعت برق
و چه زیباست وقتی مردم، خستگی این زحمت را می‌بینند و با محبت و قدردانی پاسخ می‌دهند....
‍‌‌‌‌‌‌‌‌‌#سیمبانان
#صنعت_برق_عرصه_تلاش_و_خدمت
💫
با ما همراه بمانید.
🆔
@tehran_roshan</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/687432" target="_blank">📅 18:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687431">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qsy4YzxWMQUQ7Vz6-FZCMognT5d9MATUJLBxbn2881tQd0wfWqVWo6M5mCZWKpaThip4KFPGjrLO4Ufc2MV9EsV-EjkDT7KYguCuYQp0nWKKodSP1MzXZMel7kN4bOVKmV1GtgIq6AlXSMXxgohpgChoI8VtrXPxuBJre4S-cS9VYDtronLs9IWuuTqn_1QfQiwVjwjuIESjcV43ei-6_lr_GRAqiUdKjbNJkg5GYMg0_Yym5ZoeZgd0jK6brjqmbXClFXZ1cB44VuAz7MNL_qE_QlCfWlHNGBVSIBE386qTYf25QzwqrVK9iIZRhBvrUj-lxt6YBfgy0R-1kXS3fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
احمــد کلاتــه
🔅
همایش سیستم بازاریابی تکرار
شونده
🔻
مشهــد - آمفی تئاتر شهدای سلامت(برج سپید)
🔺
چهارشنبه ۱۸ شهریور ماه ۱۴۰۵
🔸
رزرو بلیت:
🌐
metatickt.com</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/687431" target="_blank">📅 18:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687430">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ht5XuWYOFAgVP5TKQB74GUrxeLE5vmVJeu5kPfLx6a0wdEepglPsfjsOvNgxsJpvQtajummey530k4iy2rPjYz1xzRUJ0qAWPAUsWN-ghfgSna7HX4zyVHklU1W85AhECzhr1Okv15kCAyEHlhcb1TiZ__bOE4bmduhQo8zoLlifQwvAhazPeo3efAJrhyFPhl-LtR493I57IXIt7f9U0DJayLf2Z6fgXAJGCjz2NB_ifNtn7gDrDVAd4C5KX2MREyC9EQTRNh3wANgO77sT4nToj-flVsm4iwLpnFZYDV9ivZ6ClONH58ugEl5fd9eEbmPWldd2-DfoMmP3rEYRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چهل مطالبه رهبر معظم انقلاب از کارگزاران نظام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/687430" target="_blank">📅 17:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687429">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
صولت مرتضوی: دشمن نقشه داشت که ۸۰۰ هزار‌ نفر در فتنه دی ماه کشته شوند که تدبیرها اجازه نداد برنامه دشمن عملی شود/ وقتی فراخوان صادر شود دیگر ماجرا با اعتراض اجتماعی تفاوت دارد
صولت مرتضوی، وزیر کار دولت سیزدهم در
#گفتگو
با خبرفوری:
🔹
جمهوری اسلامی از بانیان فتنه دی ماه نمی‌گذرد.
🔹
این امکان وجود داشت که بهتر از این موضوع فتنه دی ماه را مدیریت کنیم.
🔹
نتانیاهو گفته تعداد قابل توجهی را برای ورود به ایران آموزش دادیم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/687429" target="_blank">📅 17:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687427">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
هشدار امنیتی سفارت آمریکا در بحرین
🔹
سفارت آمریکا در بحرین به شهروندان آمریکایی مقیم این کشور واقع در خلیج فارس نسبت به حملات احتمالی ایران هشدار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/687427" target="_blank">📅 17:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687425">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83203145ee.mp4?token=Y8kmoWeMdIT5lv6IPdMoyFru3ctjut-0IJqmKitWOJI5ocmC5dmYlXkASArDh23EmMQXCPtxHNF39biq8KAW5jf3-p7m_7ODoVlNioKlr_3r_E21DcFSfKpjrTBe85FkUOgujd_n3-nu3-T6T2V-W_DA3KtIjg6zYS3i0RJE7YkYAi-rDGZfP4UP-uWwx3v9ZQXlEegxxPfug5Ih-oFfuYfmAWb3KBGt9ebwvp_cJEcplio2vOME5AKxXQGguqOstRuh8jioiSVkRbEKFq48Z69wto0XQkpQ1XjZ9EECkYm1yW5VEK1K0yjCkHw6psxMecKTYTzDLmxwSaWcTh8V7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83203145ee.mp4?token=Y8kmoWeMdIT5lv6IPdMoyFru3ctjut-0IJqmKitWOJI5ocmC5dmYlXkASArDh23EmMQXCPtxHNF39biq8KAW5jf3-p7m_7ODoVlNioKlr_3r_E21DcFSfKpjrTBe85FkUOgujd_n3-nu3-T6T2V-W_DA3KtIjg6zYS3i0RJE7YkYAi-rDGZfP4UP-uWwx3v9ZQXlEegxxPfug5Ih-oFfuYfmAWb3KBGt9ebwvp_cJEcplio2vOME5AKxXQGguqOstRuh8jioiSVkRbEKFq48Z69wto0XQkpQ1XjZ9EECkYm1yW5VEK1K0yjCkHw6psxMecKTYTzDLmxwSaWcTh8V7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای سنتکام: نیروهای آمریکایی سه نفتکش نفت خام ایران را هدف قرار دادند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/687425" target="_blank">📅 17:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687424">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل پنجم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/687424" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687423">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک اقتصادنوین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdVVUUWtwK4z_jJy88xANuew0JrZAvdtMBCr-qbcQ1VFHviLbnA8Sbb0pZl5nV0oxHoE896q2XoAT8Z_orEaq-AsTkszE__-OhpwitlNR4Qe2UCLKo4AXXHdqJ9AFMrSH5p7g_zQTwnyGXlmhQrniGJukn-esQxzjsTXrlF-dhFPzWrVxYBcoMhHAHc45mM2W72EsMQzLFHxnPb1W2Ii7UD6QWYfPvU3HhVqGSmxskvS9vIv42Ixmk-wPQ9OKdU_Q8FKMkdNwyc2DJ6bVwbAv8oPMfa1hiU_m8YBwGld1i1dfaEVgKMKjuEwn8QrZsJefaPwyHPHvdkoCdX81AJiOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر بهداشت خطاب به مدیرعامل بانک اقتصادنوین:
🔸
اقدام مسئولانه شما در حمایت از تامین دارو، شایسته سپاس است
🔹
وزیر بهداشت، درمان و آموزش پزشکی اقدام مسئولانه بانک اقتصادنوین در حمایت از تامین داروهای مورد نیاز کشور و تقویت توان مالی شرکت‌های دارویی را شایسته سپاس و تقدیر خواند.
🔻
اطلاعات بیشتر:
https://enbank.ir/s/mfa9ZF
☎️
02162740
🌐
www.enbank.ir</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/687423" target="_blank">📅 17:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687422">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
عراق: اردوگاه داعشی «الهول» به زودی بسته خواهد شد
🔹
روسیه: اعضای گروه ۲۰ خواستار پایان جنگ آمریکا علیه ایران هستند
🔹
پلیس امنیت اقتصادی خراسان رضوی ۲ لکوموتیو ترانزیتی قاچاق به ارزش حدود ۱۰۰۰ میلیارد تومان را توقیف کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/687422" target="_blank">📅 17:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687421">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-dlffEPNSxuMfw6gbNjx25jnS6it0Rj-y5XMUwwI-Yd1c86LJNkfA_C6aCkeTLp89Tei6pGTgKLF5DWZ3F-3Pk9zqltxq-F-pMy_GF3bCPtZhhVyA4dW5ACtG64rMWQu8I7u14SxUi-pYt0dY7Q2CN8d_1sFCTi73GORvl7SIJ6Dg2CqGr6l-R2b7sHOi-AEYUxsmFRkV4SsucNAoNgR9O8y5iIGAWlN8TwxGRC6_czMxJUwlmO0fPDiAc49ZIQP1tvfOvxBTpAgnmhZ21hmJ9MLU12P_wfzm-zlVDjn4s5nO433HZgiy8djXoVf2KL5RXFmZMx97yjbhaYl-aV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای
سنتکام: نیروهای آمریکایی سه نفتکش نفت خام ایران را هدف قرار دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/687421" target="_blank">📅 17:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687420">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
راه‌آهن: خبر توقف انتقال ریلی کالا از چین و روسیه به ایران کذب است
راه‌آهن جمهوری اسلامی ایران:
🔹
ادعای ممانعت ترکمنستان و قزاقستان از انتقال ریلی کالا به ایران به‌دلیل تبعیت از تحریم‌های جدید آمریکا، صحت ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/687420" target="_blank">📅 17:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687419">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ادعای نتانیاهو: سؤال اصلی انتخابات این است که چه کسی رژیم ایران، حزب‌الله و حماس را نابود می‌کند؛ ما این کار را انجام می‌دهیم #Demon
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/687419" target="_blank">📅 17:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687416">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| نَبض تهران |</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efa895fc11.mp4?token=KNnZFG4SSJaNHEg4J2JdzdzUly9mqHLTq9_C5byqUTsOk7PABZcnnzaVhadLYyNcdeYeYV5kFm5Ndo5XMDb9Jdo-i9B5hLODUG0tOTSfIj1QqB_Aq6Q9VYFStPET0F0K0pul1o7uVnohXQRfz4eE2T9i476KV6pZxkdWusE2WIXmpOGMQhnOeKOTAjdqCsvbdyWWlD13Wge0xiU_EgwzrTfGytv_ozpyMeek46unJbwyARq9tnXH8Fnh5BBiJG8zl9sxdZXFIVVtHDyVWrOaKmNcZHPNnOgJuAA06uC5SvN7NR7QWEDvqoxdODDvt3V-HcbB5aFOa25SlSZBcQ4LnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efa895fc11.mp4?token=KNnZFG4SSJaNHEg4J2JdzdzUly9mqHLTq9_C5byqUTsOk7PABZcnnzaVhadLYyNcdeYeYV5kFm5Ndo5XMDb9Jdo-i9B5hLODUG0tOTSfIj1QqB_Aq6Q9VYFStPET0F0K0pul1o7uVnohXQRfz4eE2T9i476KV6pZxkdWusE2WIXmpOGMQhnOeKOTAjdqCsvbdyWWlD13Wge0xiU_EgwzrTfGytv_ozpyMeek46unJbwyARq9tnXH8Fnh5BBiJG8zl9sxdZXFIVVtHDyVWrOaKmNcZHPNnOgJuAA06uC5SvN7NR7QWEDvqoxdODDvt3V-HcbB5aFOa25SlSZBcQ4LnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
سامانه پیامکی گزارش ماینر و برق غیرمجاز:
30005121  _ 30006121
📌
استخراج غیرمجاز رمزارز، یعنی مصرف برق یارانه‌ای برای سود شخصی و تحمیل هزینه به شبکه و مردم
#قاچاق_برق
|
#برق_پایدار
روابط عمومی شرکت توزیع نیروی برق استان تهران
🆔️
http://ble.ir/bargheiran</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/687416" target="_blank">📅 17:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687415">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FB90gjInEhEZfu_BhTOvDVtBSbM3FMmqbSyjcfnaJ0Bl0aZLrxCsNv2YvtL7NpF7JoNTY55q3UbqNmb321LqhRFoEhA7ocjqYax5WlmguwjwnMw00OWTriGyowqjLu4NP5qago2abJ4okqh8sVpJUIcifHVdRWuFxtv_xgquovd-gOt6dJji8mvIUYCvgYgX2qqQfuDEv2T2aJbWkSdQxyLxRTlmoz0SM6au_5eSFK0WcWYiILD3pj9URyFxLmOrhmEvCcF884Kp2NLSFHhZ36xeH7VeIAvkfiUrKSwWVJCyjJpunPL28yhG90mQuU8R_saqzU4VhVnS_uwOP_el2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وبینار رایگان «پشت پرده سکوت مشتری»
مشتری جواب نمی‌دهد؟ شاید هنوز فروش از دست نرفته باشد!
🔴
خیلی از فروش‌ها درست جایی از بین می‌روند که مشتری سکوت می‌کند. این همان پشت صحنه‌ای است که که باید ازش خبر داشته باشید.
در وبینار پشت پرده سکوت یاد می‌گیرید:
🔹
چرا مشتری‌ها پاسخ نمی‌دهند؟
🔹
چطور بفهمیم مشتری مردد است یا علاقه‌ای ندارد؟
🔹
چرا پیام‌های پیگیری معمولی نتیجه نمی‌دهند؟
🔹
چگونه دوباره گفتگو با مشتری را شروع کنیم؟
🔹
چطور مشتریان خاموش را به مسیر خرید برگردانیم؟
این وبینار با تمرکز بر تکنیک‌های عملی فروش و بررسی موقعیت‌های واقعی برگزار می‌شود.
📌
ثبت‌نام رایگان
👇
https://survey.porsline.ir/s/HnTcBfTL</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/687415" target="_blank">📅 17:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687414">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
جزئیات اجرای حکم قصاص خواننده مازندرانی
رئیس کل دادگستری مازندران:
🔹
حکم قصاص نفس متهم ۳۰ ساله پرونده قتل یک جوان در کافه‌ای در بابلسر، پس از تأیید دیوان عالی کشور، هفته گذشته ساعت ۴:۳۰ بامداد در زندان اجرا شد.
🔹
درگیری لحظه‌ای و بدون خصومت قبلی بوده و پرونده با استناد به فیلم دوربین‌های مداربسته، نظریه پزشکی قانونی و اقرار متهم رسیدگی شده است.
🔹
اجرای حکم که ابتدا برای ۱۸ خرداد تعیین شده بود، به‌دلیل ایام محرم و صفر و با هدف جلب رضایت اولیای دم به تعویق افتاده بود.
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/687414" target="_blank">📅 16:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687413">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
جزئیات نسخه تازه مصوبه مجلس
🔹
بر اساس ماده‌ی ۱۵، همه‌ی اشخاص حقیقی و حقوقی ۳ ماه فرصت دارند تا فعالیت‌ها، قراردادها و ارتباطات جاری خود با کشورهای خارجی را با سازوکار جدید تطبیق داده و در سامانه شفاف کنند.
🔹
تولید اثر هنری بدون مجوز از نهادهای قانونی کشور،…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/687413" target="_blank">📅 16:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687412">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJMXf-EwZFiPkZZFjd7oyF25wwhXp-ElNWKw6Ps4YsM4RjG2TjTvpYHBdtQFjxpbsuCB50mJ7B2r9opuWeaamLAqJw6HMczq409XvygL0NrUKcKsdWmO7qCY5n3RcuZWI-kZgzExVRDRMBDKuU5DfjD-ILxq8MlXV_8HYWVkCnhppMKyV32WJWH3vZ97GT2gc46rb9kxhkukyFg0MT8MlKNfxmJZM2DweCfU45yuKZ5IEUIjQPYehFoCRKXY0gZWN_QOYWYjoK5HnUZgsrT30qx2QUIDKUUiFfTWmrbBzgs7vixKzXXM46PevvfWYvVgtt6E50OlBor8QDFZWkB4PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلی بر حال و آیندهٔ صنعت فولاد در جهان، خاورمیانه و ایران
🔹
به قلم امین ابراهیمی
🔹
مدیرعامل شرکت فولاد خوزستان
🔹
نایب‌رئیس انجمن تولیدکنندگان فولاد ایران
🔹
جایگاه واقعی فولاد ایران در معادلات جهانی، بسیار فراتر از تصویری است که حتی بسیاری از فعالان داخلی از آن دارند. آمار رسمی انجمن جهانی فولاد برای سال ۲۰۲۵ گویای این واقعیت است: ایران با تولید ۳۲ میلیون تن، دهمین فولادساز بزرگ جهان است و علی‌رغم تمام محدودیت‌های انرژی و فشار تحریم، تولید خود را نسبت به سال قبل افزایش داده است....
ادامه گزارش
👇
akharinkhabar.ir/local/10995391/
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/687412" target="_blank">📅 16:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687411">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgzSeezY1rxFlfDCValOSKFh2OA6dZ150VMBuI-tjNGP6kwGUF93yd4liNTw5MCtFWMIRwTx2Gkn3jZXBoEeGyJKvBLMwPvFZgt8mn1CEQOPt2dlVWLyEC6O1RTpSwcttKFJgtcWhodFt8gs4uqCqbwOvnH85PjuNEwFFEI6cggZLs32ebePaMx7lKVRdZ1HIs7PjahssPuy-h3GkG7xlXuLgbEmhbMqLjGJQt6sJDwD3ezW2Y86aiD-IjPWI2tASBDF2ORVGkQ5wLvWRYfYEsQFjP9Kmtpu_eahEMFkBRFjGQHnIBpeQQjcdqnNygLeCuPsdRzjRhDdQWeJ6N_2fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصطفی طغانی قهرمان کشتی پهلوانی شد
⁣
🔹
نماینده ایران در وزن مثبت ۱۰۰ کیلوگرم کشتی پهلوانی با پیروزی مقتدرانه برابر حریف قرقیزستانی قهرمان بازی‌های جهانی عشایر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/687411" target="_blank">📅 16:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687410">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXvXvvKU4g9Z51lI-ks7ntzev8f0PLeOV7-78GvKIh2r3DQH52LTzh5VJLptfMr8XELh0EExiUr5jpA3cfAWtd9dkZgaSQdi_ILmAVPwppsSsKU8uJVXqdMAVhR6HuldZeWfG36cmZFIckFpARDCs7f1eDMJv1glfWSKTRyObcz-Fw4JM5_ahKiXJoogcwe4V5VYKonK3c-8Be2Xs81-mlViSjS6iYuMbB1nDnl_B0sXQLzcE7AnqWps2ZcGOdY3IK9OvTjI8MIzEvB3KkGPkI8FTrObj-Ftnr72mbaLfMY-JyomJJmxPEZK6RsjAR4f28MFVEMqMpltQTYLALJllw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پراکندگی جمعیت مسیحیان در منطقه غرب آسیا
🔸
بررسی داده‌های مرکز تحقیقاتی پیو (Pew Research Center) نشان می‌دهد کشور قبرس با ۷۸ درصد و لبنان با ۳۱ درصد، بیشترین سهم جمعیت مسیحی را در منطقه غرب آسیا به خود اختصاص داده‌اند.
🔸
حضور درصدی قابل‌توجه از مسیحیان در کشورهای حوزه خلیج فارس، عمدتاً حاصل مهاجرت نیروی کار بین‌المللی به این کشورهاست.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/687410" target="_blank">📅 16:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687404">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R6MS8Vr8B773unUKoj0k5FSOradpn0UXuPF_gIY8zCzR5hdc7c6IM1LX1Y6GILkGaQ-sdFW6FG4F235Z42UQuN4-n3dW6inSLBj-EJjQFf-CFph2k1JGjgb7fy_jWLWjt6GtFgHV4Z0AsuTyGJXfhPO6CI5oZ3ugKfzd9bwdBzB9xHz1GxQ8t7JujrgYYYaSi1Ef0gYPQPgYNTO89FilZP9Y3eZUGJdhMf2w04LbHXe9_jlPIsBEe6RbUFKeIg36MrUeeVfmq1_MVlsIDuCscIbWgCz4-TlBah-TfIb4lWJTDhacxplOFXFxFEyNwHJEai01YjLtxajqD1gCOf9rIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SFvRns4gZuONqGswCZPty6SzmOwlCyk-X_qmEZg_P6KaOetI7qS1XC6LckYRe4TKNIwb5_ZHM0GOforcNHbBmjT0i9_p548Oc0ShsUZAgM5tCpHS9eNxf0rlAf1llk9hPDvbAwxObrWRnNH0dXqhjyOS5v5HwjjIRq896A3EbqCox8KYCGLBMh9gsXPLa34M9ofTUyYLDB6K9mV9uhbt9o-ZC6fZKJ8YmsHvzp7L2B-arZj4bTJYESBvP6Rqaew1t-epw2VpTyip9r2eNC0_62zfZhNtGgrbYRGp_8LOr8gBZkB45jaTtDNwv5eHxs_wSyMJCEG2iHkcYxG7Jke0RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lOJ3yPxKBQbGlY1Nr1RFrunzxkfJNmPGf4-Oz4tUujwFd5_YOw7e4OkCzgBQaVjw4pw7cGtDqo_8svWreXok93OsoakfZCAPcRJWLv5ARlyaNKajs035n3BsH0xpRX0QKPhTTCUxbaBxBjvUV9VKu9CtyNv_BkZV2Z4Ui3OxpXoMFUErmgFKT2vtZPUOcOPYJg1867efB725A1eZIwKzcSOABQMG9iCrOUd1xREFo5zcVdmV-COYdpGs2oljsisksuzOCLzfl-UyQif5Q2myhGVqJq9LIDkRZEM4d3tsR_uHLYixbE4r-Vkdps7ozlFKGyjE6lQmSwH6yBxglDRRtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MC_f5EcCjHvO0U8Kbq6DzSb3yiEJ2ZDZC6lryUUGMhnRa0C6n2ZZ_CW-m6AyTdzCpDqCR5-xUIV3RLrfVBDMhhkqwRV23bB-i_7ap9UFb3d7f9eMUUQKssatStzYBU3hTvb_jW9DB5mzfGeuoI-GWe0-n1y4TLHRLkS3b-9D1cOdP_HHdJ88VmASoZ4g_zWj4SaVepVJ-Coi6Xwe7gWmoHO4MbzpA4HLfzm3zmP9-YqsL4uSN7yH2aNkJ2bStPadcmmwNpeOdp_BkgemWZDcISh82ViPG7awhIpMTOShDsfURB5vFNdp-Eb3GChmQwSaYIVZl7M2VMexTUov0Je6Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WFtEzsGUWi7L-YVYqLm1OuvbCX0TRPB4xgfLAF8uGDyOxfHmrVnUvutLSs_FtGMNWvwFysz1zCoLDIlMgKVKZ0tuQGbkPN71y8YkBM-_Is67p1vNArHm0uuE6OHIBgJeC2D4tOc5i1QJ0ZRsffLHiAwSEY8Ibkwdri6IyU47rvDkPsPEG8jOLk6zHAcQVCB766HhoZeLd-vJ9fk_2hv2mFN5H7vHjjql1dEN_eAA9WTNZkaP-xronbk3as3Wn4zOhQ8UPsXA0cD-NQ2oxRMFZdjmPt-s-qdaaskd-KU8CX6VDdAMxnht2ntbZ67cJgo3fyp28RU-9DCy819voP1W-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d4GTLUN2tor76GwPb5_W3a-u3W5ktTNua_86fw9ny521bBlCxCz8-oqDgyoGGjrFwm8KrQfZ14ZGzGmG69au8mANN47x7T6XlmRd2VAAc-I7AUF2saxTb2ZqMsUb6ADBEdB7oXqDNl3sPZ07Nrzph_T50mXmfBOH0fpG4S_cDlSNLpkDbTcKA71oc639uaj9-xfceBOIHL_LgSC3q-7c9PF2v-xT13xw5OPTerYW0IxWxOGzpPIrYSfQOS5H9WOf3OHLMUDs2WBk7a-DY60e8tDt2b_gR9GrszAn6uFKpBhs80L1ChN7PbbFe_vPX_9dE6YsVzgAKsU-20wqVagWmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چطور با ریسک کم‌تر از بانک دو برابر سود بگیریم؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/687404" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687403">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دستیار رئیس کل بانک مرکزی: با وجود محدودیت‌های امسال، وصول ارزهای نفتی ۵۰ درصد بیشتر از سال ۹۸ و ۹۹ بوده است.
🔹
سخنگوی آموزش‌وپرورش: از اول مهر حق‌التدریس معلمان شاغل و بازنشسته ۲ برابر می‌شود.
🔹
تجاوز جدید صهیونیست‌ها به منطقه وادی الرقاد در حومه غربی درعا در جنوب سوریه.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/687403" target="_blank">📅 16:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687402">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eb32a6f8.mp4?token=XXV9u75OYqh0VWt2I9X5LcCclbVfQE4ZNQibICF4I75PIzRM5u1FXLA4NwZkghWd4PX21mU4DAjlN8MawNhZ973tBtrJdqyIz-PgUvRAIsTe8IZSrjdi6jzzCdTSlaEfrjbjwjtn2wg0c_1VcYN1-kXV1xIifIhYiBnI_3Y4-duegFyr1K4yqFk_6Pw7wR0Kj3pjYL-dlVgssV8qmbXhK34ZoO-zJ-qYB-UOuoOTPq0nV4GU-CBQ-lv_44xjqtCR19EuP7kK3A9xxwwsq1-V_nJ-62GpoNv07j8TN2Aqnq3SSU641qq8rQ9dmodPI-zD9Uq5rZov1nXxFDsQworHxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eb32a6f8.mp4?token=XXV9u75OYqh0VWt2I9X5LcCclbVfQE4ZNQibICF4I75PIzRM5u1FXLA4NwZkghWd4PX21mU4DAjlN8MawNhZ973tBtrJdqyIz-PgUvRAIsTe8IZSrjdi6jzzCdTSlaEfrjbjwjtn2wg0c_1VcYN1-kXV1xIifIhYiBnI_3Y4-duegFyr1K4yqFk_6Pw7wR0Kj3pjYL-dlVgssV8qmbXhK34ZoO-zJ-qYB-UOuoOTPq0nV4GU-CBQ-lv_44xjqtCR19EuP7kK3A9xxwwsq1-V_nJ-62GpoNv07j8TN2Aqnq3SSU641qq8rQ9dmodPI-zD9Uq5rZov1nXxFDsQworHxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط جنگنده ساخت آمریکایی در یونان
🔹
یک فروند فانتوم اف-۴ نیروی هوایی یونان در جریان نمایش هوایی در شهر «تاناگرا» این کشور دچار سانحه شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/687402" target="_blank">📅 16:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687401">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8srnJoZ5uMLLPjvsvOUiep7pDzAfvHh1uJZBG0SPDhaxXqgqSqcFSl9hCKq4m0oFr6SG4l9zTt3ejPQZVRArfkRMfkwaq0hBffzNtTpVbBYXsJTbzIVDXzaJpq4sBrKsWY8nInlRLZFN86RW-mOLInU5MNS1_Dq5QGFhDAsQE4Jw17VEuN_b6LIS8XycitMjejsvYxjXcfFzg2G6V2OEY2251fj2uNYebLoJjIbu2PjNjNSM7oq7W2B21SHrJ93jMQMs2gAwR_iefd84lFSMxLpTsTaHUIvLLe8suWfdXFowT8pxEde7uFwE5U2lE2pZOz6CXex2LUcfpB4GsPXYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نسخه تجزیه ایران روی میز کنگره آمریکا!
🔹
روزنامه صهیونیستی جروزالم پست در مقاله‌ای پیشنهاد کرده است که کنگره آمریکا با تصویب قطعنامه‌ای، استقلال اقلیت‌های قومی ایرانی مانند کردها و عرب‌ها را به رسمیت بشناسد و راه را برای تجزیه ایران باز کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/687401" target="_blank">📅 16:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687400">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee8aedc93b.mp4?token=TnaHhul7pPs5B-cG0rShDtBvRawBCToNT0uHo_73P6xa4Qp31A-LCLHcqu_cGWjk75JLuTPHXLGMPEiLWUUkTXUqf3UhDcedwJz_eCIeVZLNZD1qtZMDL3Cco7m9jUNLE0-vNvEt5Uju19pR3xAFsiYVUodFUrZ0MuVlQihDQFQD4e-ScTpWZFpykHVFBcMQT78bOB1RnW2SYSu0-ypycoJVfehFFShfglRpie3HcfGtn_0nCRlLi0hIyc-7PhR01s1I1bMSQHuUURMByRYI1wyYEEjEzgQWugWP4pN9LCll-3IYPVXg-A5hXvgemmAcvn_F4VEwRj5oaIAauq3l0RGnZ7MMTcS40Bt26y-ZbRb_zcl8YOmmiM6v-3igSXEED2YZ5EhiOqdE7kTDXISUMJuME2Fu1d9dCzOeiMaRJ-NvDuSS1irRJfrK6ZfYXNpcQ-46kbN2OEG__8BiQVPIr4Coaa94pGOjw8kvfXePO4pqMcbUeeeYmE5kv1HusZrFtMOmi8aKG3GQIHNkofxbOnT0fl74_hgC9JoKPkzH_jLti4VFT_QY71ilcY5fWz-QPmf0L5B_ZFJIj8cI0iVIGO5bp8fnu2j_u-H3VQvFzqbxM45jox58j1_6s02_zaWUiamFuwnsPoEKqEciOqakUz-WPnMkRJC-Q-wr1ZyKj1M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee8aedc93b.mp4?token=TnaHhul7pPs5B-cG0rShDtBvRawBCToNT0uHo_73P6xa4Qp31A-LCLHcqu_cGWjk75JLuTPHXLGMPEiLWUUkTXUqf3UhDcedwJz_eCIeVZLNZD1qtZMDL3Cco7m9jUNLE0-vNvEt5Uju19pR3xAFsiYVUodFUrZ0MuVlQihDQFQD4e-ScTpWZFpykHVFBcMQT78bOB1RnW2SYSu0-ypycoJVfehFFShfglRpie3HcfGtn_0nCRlLi0hIyc-7PhR01s1I1bMSQHuUURMByRYI1wyYEEjEzgQWugWP4pN9LCll-3IYPVXg-A5hXvgemmAcvn_F4VEwRj5oaIAauq3l0RGnZ7MMTcS40Bt26y-ZbRb_zcl8YOmmiM6v-3igSXEED2YZ5EhiOqdE7kTDXISUMJuME2Fu1d9dCzOeiMaRJ-NvDuSS1irRJfrK6ZfYXNpcQ-46kbN2OEG__8BiQVPIr4Coaa94pGOjw8kvfXePO4pqMcbUeeeYmE5kv1HusZrFtMOmi8aKG3GQIHNkofxbOnT0fl74_hgC9JoKPkzH_jLti4VFT_QY71ilcY5fWz-QPmf0L5B_ZFJIj8cI0iVIGO5bp8fnu2j_u-H3VQvFzqbxM45jox58j1_6s02_zaWUiamFuwnsPoEKqEciOqakUz-WPnMkRJC-Q-wr1ZyKj1M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس الجزیره: چرا رواست که به ایرانی‌ها گفته شود «علیه حکومت خود قیام کنید»، اما غربی‌ها نباید از دولت‌های خود انتقاد کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/687400" target="_blank">📅 16:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687399">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
نتانیاهو: خبرنگاران محل اقامت پسرش در آمریکا را لو دادند!
🔹
بنیامین نتانیاهو نخست وزیر رژیم صهیونیستی درباره ادعای ترور یائیر نتانیاهو، پسرش در آمریکا، آن را اقدامی واقعی و جدی قلمداد کرد که به زعم وی به دخالت نیروهای امنیتی و نیروهای کمکی انجامید تا او را به‌سرعت از آمریکا خارج کنند.
🔹
او در عین حال افشای محل اقامت پسرش در آمریکا را به گردن خبرنگاران انداخت و مدعی شد: این اتفاق در پی اقدامات غیرمسئولانه تعدادی از خبرنگاران و افراد دیگری رخ داد که مکان یائیر را لحظه به لحظه فاش کردند: آدرس دقیق محل اقامت او، تصویر آپارتمان، شماره طبقه و شماره واحد.
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/687399" target="_blank">📅 16:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687398">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
قیمت مرغ کاهش یافت
🔹
براساس گزارش میدانی، هر کیلو مرغ به ۲۷۰ هزار تومان و ران مرغ به ۲۰۰ هزار تومان کاهش یافته است.
🔹
وزارت کشاورزی اعلام کرده نهاده به حد کافی وارد شده و بخشی از آن توزیع شده است./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/687398" target="_blank">📅 15:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687397">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ترامپ متوهم: ویتکاف و کوشنر در حال بردن پیشنهادی به مسکو برای پایان دادن به جنگ هستند #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/687397" target="_blank">📅 15:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687396">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
حزب‌الله: تجاوزات صهیونیست‌ها با سکوت بین‌المللی و انفعال دولت لبنان ادامه دارد
حزب‌الله لبنان:
🔹
دشمن اسرائیلی همچنان به تشدید تجاوزات و جنایات خود علیه لبنان ادامه می‌دهد؛ کشتار، بمباران، تخریب و انفجار سیستماتیک منازل و روستاها، پاک کردن آثار آن‌ها و نابودی تمام مؤلفه‌های زندگی در این مناطق، بدون هیچ بازدارنده‌ای و با بهانه‌های واهی.
🔹
تجاوز تروریستی این رژیم در روز گذشته، در سایه سکوت مطلق بین‌المللی، همدستی آشکار آمریکا، غیبت کامل دولت لبنان در قبال پذیرش مسئولیت‌هایش و اصرار شرم‌آور آن بر استمرار گزینه‌های اشتباه، به شهادت چهار تن و زخمی شدن ده‌ها نفر انجامید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/687396" target="_blank">📅 15:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687395">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSalGS4XbwxVd3phHBEEPKTCn6h50jENLFHTzQQL4azJ9ZK0gon8N690IIPyeJVmRuohv93IRzTysX1SnydBV2C44RbDhoIS_mtN0GEefTrPs_OeSSdQArdwjT21Jq2ydYpHoG2urJyp07ZY9L4tg9gpZdvPWZyrZP2RgqZKl3-8YZhGXm-9OcA-9V2obZX-JjdGlb8NTqcVkpToTEk9-ezgmdyh8x3vFf3Ytb3KXu6x7PpEYsnn87HdMk2qan23bPpe58xTGTSPsJNpMgdWa0IED3IHvVuhhflYFEga0tW9jCBcO0_8T2HPg9CAcf-z9JNLgo3FxcgtoXVvgfifQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدام اپراتور کمترین قطعی تماس را دارد؟
🔹
تازه‌ترین آمار سازمان تنظیم مقررات در بهار ۱۴۰۵ نشان می‌دهد همراه اول در چند شاخص مهم کیفیت شبکه، عملکرد بهتری نسبت به رقبا داشته است.
🔹
در بخش اینترنت سیار، نرخ موفقیت برقراری سرویس داده همراه اول در شبکه 4G به ۹۹.۶۵ درصد رسیده و در 3G نیز ۹۹.۴۲ درصد ثبت شده است. در تماس صوتی نیز همراه اول بالاترین نرخ موفقیت را داشته؛ به‌طوری‌که موفقیت برقراری تماس در شبکه 3G این اپراتور ۹۹.۹۶ درصد اعلام شده است.
🔹
این آمار نشان می‌دهد کیفیت شبکه فقط به پوشش محدود نیست و پایداری تماس و اتصال هم نقش مهمی در تجربه کاربران دارد./ ایلنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/687395" target="_blank">📅 15:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687394">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
اذعان نظامیان آمریکایی به دستور پنتاگون برای بمباران زیرساخت‌های غیرنظامی ایران
شبکه MS NOW:
🔹
نظامیان آمریکایی اعتراف کرده‌اند از وزارت جنگ دستور بمباران زیرساخت‌های غیرنظامی ایران را دریافت کرده‌اند.
🔹
ارتش آمریکا زیرساخت‌های غیرنظامی و چندین پل ایران که اهداف نظامی نبودند، هدف قرار داد و این نقض قوانین بین‌المللی است.
🔹
فرماندهان پنتاگون به اندازه کافی برای جلوگیری از تلفات غیرنظامیان در جریان حملات هوایی در داخل ایران تلاش نمی‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/687394" target="_blank">📅 15:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687393">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7051ae1e2a.mp4?token=fL3PKniqeye49kg4RXLA2vGP3IjcFnw4-AXgAjfXdsqYzP9l89qJY81itx_HF1s7Dh0c3fYLJuKXOVEn1FmfoH5aklnYONtihwVtahkf9mWwSU-G5uY120yzU6PZ1Z0cDt0OSGgClozzOfi7qwOYInNno8uO3h1LOxOaT_5IOMc5Ikp_v0iUgv7j3U7hQiMlmZ1Vh9nHm0E82sE7E-RyOCF2KosnR9iaqTFTuSMKRonnljL0QUFUe09-bRCReFaJ8zBOwAX1J_1-ZBOgstOlW_WT1tTOE9W6FXCFKt-pjXO-fsNeUjqZsRIernUftqh5oI3hXtCJDP_EJZznovbXiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7051ae1e2a.mp4?token=fL3PKniqeye49kg4RXLA2vGP3IjcFnw4-AXgAjfXdsqYzP9l89qJY81itx_HF1s7Dh0c3fYLJuKXOVEn1FmfoH5aklnYONtihwVtahkf9mWwSU-G5uY120yzU6PZ1Z0cDt0OSGgClozzOfi7qwOYInNno8uO3h1LOxOaT_5IOMc5Ikp_v0iUgv7j3U7hQiMlmZ1Vh9nHm0E82sE7E-RyOCF2KosnR9iaqTFTuSMKRonnljL0QUFUe09-bRCReFaJ8zBOwAX1J_1-ZBOgstOlW_WT1tTOE9W6FXCFKt-pjXO-fsNeUjqZsRIernUftqh5oI3hXtCJDP_EJZznovbXiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاری که نخ‌دندون با دندون‌هامون می‌کنه فراتر از چیزیه که تصور می‌کنید #حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/687393" target="_blank">📅 15:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687392">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1410094cdb.mp4?token=WU5WYs1eM50jHZmEzRxkE5PgWh-DhZ-Et65iy6j1s1iZLb6wnJHlEdzrMxp6wjifmdc8CJzgsWSXy0BZFig6jJxuQQw52-cxCAlE8y200Y8rZvcMhGbgBqJtnWmhZg5xXNNa4vCM-dnPNb5IwOWZunBKqYhaQVXT_fxtkhmEJ2DMofdqrJ-amQ7fGZfy8w-8EyjaaiZ9tlJaA6WISkg6_HcQf9swhnQRTHLsR0B3MWvHprQJ8rwbwX3kkrgIYcCHPpxPcTT1WVXiCDSKrxzEa6u-u41Xf98gUzDAOV_OTXgMmG0-iuBxqw7hIYnY3ulOCBKCNnr45hgINNVu5t7tYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1410094cdb.mp4?token=WU5WYs1eM50jHZmEzRxkE5PgWh-DhZ-Et65iy6j1s1iZLb6wnJHlEdzrMxp6wjifmdc8CJzgsWSXy0BZFig6jJxuQQw52-cxCAlE8y200Y8rZvcMhGbgBqJtnWmhZg5xXNNa4vCM-dnPNb5IwOWZunBKqYhaQVXT_fxtkhmEJ2DMofdqrJ-amQ7fGZfy8w-8EyjaaiZ9tlJaA6WISkg6_HcQf9swhnQRTHLsR0B3MWvHprQJ8rwbwX3kkrgIYcCHPpxPcTT1WVXiCDSKrxzEa6u-u41Xf98gUzDAOV_OTXgMmG0-iuBxqw7hIYnY3ulOCBKCNnr45hgINNVu5t7tYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای نتانیاهو: من به توانایی خود برای سرنگونی نظام ایران، یک بار برای همیشه، اطمینان دارم #Demon
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/687392" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687391">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZeIulm6UqaD3vZJTv-g2M-9mf7JaBABaWtDHu5pLQJ74Fjjpgz_LtP0InlzDrSxdAZzCizAiVTBu4bGr35mrm2pr-XNVNuF4fs0KCCCjt-X8eqrPsvoPXPp9MbaMzmCsJPSqDKidvFBkueIPqkmsQjd3Bg-R-oPkYjWP-PHVlf_ihMUz62yZddrsvBBe3Hb1iQbeevp5h99f5Ghd_1vFgmrZEZhq5KP5fAewKX9J2ZyX4_Z-7Yaqp0_3LXkLLLnwcYvPgKKenu-GTPalGpOiLAoPiCEvrDQFljw0Qv8beZmD257PpkFDGuSFOiJXJ74X49yX1qg4I2yNrMExktdjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون علمی رئیس‌جمهور: دوران صرفا تولید و مصرف فناوری در ایران تمام شده؛ به‌دنبال مرجعیت فناوری هستیم
حسین افشین، معاون علمی، فناوری و اقتصاد دانش‌بنیان رئیس‌جمهور، در جمع نخبگان استان آذربایجان غربی گفت آنچه از یک دوره مسئولیت باقی می‌ماند، نباید به چند ساختمان و تجهیزات محدود شود؛
مهم‌تر از آن، ساختن توانایی‌هایی است که کشور را برای نسل‌های بعدی فناوری آماده کند.
او
هوش مصنوعی، فناوری کوانتومی، زیست‌فناوری، نیمه‌رساناها، رباتیک و فناوری‌های فضایی
را از حوزه‌های اثرگذار بر آینده کشور دانست و تأکید کرد که ایجاد ظرفیت به‌تنهایی کافی نیست؛ این ظرفیت‌ها باید به
کاربرد، حل مسئله و خلق ارزش
برسند.  افشین همچنین تأکید کرد که هدف ایران نباید فقط
استقلال فناورانه
باشد؛ در حوزه‌های منتخب باید به سمت
مرجعیت فناوری
حرکت کرد؛ یعنی ایران نه‌تنها فناوری را مصرف یا تولید کند، بلکه در تعیین مسیر آینده آن نیز نقش داشته باشد
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/687391" target="_blank">📅 15:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687390">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
عارف
:
افزایش عدد کالابرگ‌ها را فراموش نکرده‌ایم و تا هفته‌های آینده آن را حل می‌کنیم./صداوسیما
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/687390" target="_blank">📅 14:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687389">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a32b841d6.mp4?token=lchty0zvQDfUOUbORq9nZzg6z16KXNyhkbZrrh6OqyDMdgMgu6i8UmaYuPoUDx6QDxPbGPu8XFxgldN0iNBaljFVyEdifGN0cG-atz51bhQRqnv3TConITRW_Km3xAnu9ip-QuYY0eVypP5S0Pe0PxJqzxJeBCWJ3PNDsUouj5xfsvN6Ausz0cHrQzhqXyww27VHpzJ0rG3mWBCGqxdjMJlI4t-Z8yq-vLMOG3vQZxLeY-m1ZWrID2of-FXxUyD0WLCl6q-4Y0y76iag8xOI8HBuIXYRoNE5xa1SrSUZ5nTLDDYnuea2FPnDCIUnlQZqOINk0dhbAVthuA4PJf5iEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a32b841d6.mp4?token=lchty0zvQDfUOUbORq9nZzg6z16KXNyhkbZrrh6OqyDMdgMgu6i8UmaYuPoUDx6QDxPbGPu8XFxgldN0iNBaljFVyEdifGN0cG-atz51bhQRqnv3TConITRW_Km3xAnu9ip-QuYY0eVypP5S0Pe0PxJqzxJeBCWJ3PNDsUouj5xfsvN6Ausz0cHrQzhqXyww27VHpzJ0rG3mWBCGqxdjMJlI4t-Z8yq-vLMOG3vQZxLeY-m1ZWrID2of-FXxUyD0WLCl6q-4Y0y76iag8xOI8HBuIXYRoNE5xa1SrSUZ5nTLDDYnuea2FPnDCIUnlQZqOINk0dhbAVthuA4PJf5iEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاتز وزیر جنگ اسرائیل: منتظریم ایران به تصرف تل علی الطاهر واکنش نشون بده تا از غل و زنجیر و محدودیت‌های ایجاد شده توسط ترامپ آزاد بشیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/687389" target="_blank">📅 14:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687388">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5ck1NrfBMrbMsYbsNJwVGAMYbNMDjYRih1C8jf7517n2KiA7y7NzlhxurxxRUJuZGCGqcdIZzQh8zBX5C9ETlyD8kT3HK_yzuX7Ug5weh5_MXtWtBORgzfs_jZUcbaSk4UWCTUx26gtHEppFKc0QGXD-KSQAQRGBH5twBmlO6wZ1Z1U5qPNBnZ6WfMWgRksOMi5uF80VwuJSFcYkVpyqa_frmNSuviNmeWVstlh2QRrUKVbFgXQgx2AAciUwxKLEV__xj2LtVGDhvlb47LsQIpY8mKXPdHs14bkgJk6OAbzpct_mUUUGbCdKbNl4Xmqn7MXxMP1ua6QivaT50Bhzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پارلمان پاکستان برای اولین بار در تاریخ این کشور، فرماندهی قانونی هر سه نیروی مسلح (ارتش، نیروی دریایی و نیروی هوایی) را به عاصم منیر، فرمانده ارتش، واگذار کرد
🔹
او می‌تواند بدون تأیید کابینه، پرسنل را در تمام خدمات بازنشسته، مرخص یا حفظ کند. دوره پنج ساله او حداقل تا سال ۲۰۳۰ ادامه دارد.
🔹
او به عنوان فیلد مارشال، رتبه و مصونیت قانونی را برای تمام عمر حفظ می‌کند و برکناری او نیاز به رأی دو سوم پارلمان دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/687388" target="_blank">📅 14:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687386">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ناو زنگ زده آبراهام لینکلن، نماد فرسودگی هژمونی آمریکا
🔹
ناو هواپیمابر «آبراهام لینکلن» متعلق به نیروی دریایی آمریکا که زمانی نماد قدرت و سیطره این کشور بود، این روزها پس از ۲۸۶ روز حضور در دریا، به دلیل فرسودگی و مشکلات فنی فراوان، سرانجام روز دوم سپتامبر…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/687386" target="_blank">📅 14:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687385">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMx7kyyrOHnQ4LTQHm3J3WlRq2bbHbc8GQalfCS3-MjWZZob2NnC9Z1uP1FKs_2_msctXWeTMxiKQus7MD7-GEYQDs_6KO3izz6j_gy8p7mCeXD2MFdqA-h1epsXX7VTiraIDnZt1LXuY0VM_siOooX1nWUtIUCGKXSys8Kr4EKb8Y_-FMlfj5qPACioi04j3c-IOysuvfspz_xEHfdh7JzF2ctRkmoO5wnPeyUPkB5ulSpQaVUZqcIuIIA-seyUkfxNkkTS8iTLCFDD4HCh5192nT1MgWFKaxJ5kq_ZmwHxt6pMGDu0uxDtyk8sk17Vdxjm73nPBTlNxmcGjAnX9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸۰ درصد نوشت‌افزارهای کشور تولید داخل است!
🔹
۸۰٪ نوشت‌افزارهای کشور تولید داخل است و بخش عمده مواد اولیه نیز از داخل تأمین می‌شود.
🔹
صنعت نوشت‌افزار ۱۲۰ تا ۱۳۰ هزار شغل ایجاد کرده و ۱۹ هزار صنف و ۳۰ هزار تولیدکننده مستقیم دارد.
@amarfact</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/687385" target="_blank">📅 14:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687384">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7cce2cc97.mp4?token=KnK1ZhMar8evR7we5IN5CRIlLj0nLUWX02gw0THYS5rBtjHw2QwqOSROdVkzkYstiKrTxDacti74xhsLC7Bq89fxj34CntVwuBMc3T688-A4-f1htezSJ0LB08kK-GnKvMkdjO2gmcWEa8sEZTV2G81uQkeDOEFP-XjLOV8qRgKjEhYXGWt3qNOpgZIpFguIOpl4wSFNYGcT3dJBbdD2zHF-7gLQvEiVAg8piDmGdi_ZUAz6rOH8TIozwWg-6zZh1haZiNsSq_5fKPiAw4EN5Cgl6iRnf6UpQfZSfTb7Op1_WR1RcITSN-lT5-W3NsSaNn27snYsupxzMHa7KO-R5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7cce2cc97.mp4?token=KnK1ZhMar8evR7we5IN5CRIlLj0nLUWX02gw0THYS5rBtjHw2QwqOSROdVkzkYstiKrTxDacti74xhsLC7Bq89fxj34CntVwuBMc3T688-A4-f1htezSJ0LB08kK-GnKvMkdjO2gmcWEa8sEZTV2G81uQkeDOEFP-XjLOV8qRgKjEhYXGWt3qNOpgZIpFguIOpl4wSFNYGcT3dJBbdD2zHF-7gLQvEiVAg8piDmGdi_ZUAz6rOH8TIozwWg-6zZh1haZiNsSq_5fKPiAw4EN5Cgl6iRnf6UpQfZSfTb7Op1_WR1RcITSN-lT5-W3NsSaNn27snYsupxzMHa7KO-R5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لباس ساده‌ات فقط یک کم گل‌دوزی کم داره تا خوشحال بشه
🌺
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/687384" target="_blank">📅 14:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687383">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Up89yzxMapoHqZ7Gh2uUH3SuiR6BR7f0leOZAHvyIIx7hbRObCh4cKonTx_4e6NzkymAJdCla-D6W9XzYSa1O2El1JuK_K29NSZmmDZ24ul7iHOmvavd4zgRatcVGzgVUMW_16nnyBUky585QwohZJxc-Hlmy-KKx98Ona5ItAa3XWh9Eg_IZardCcyDlfbJl4PeTIFQsvQRIe3KevXLtzLXjVvGFFlUy6leX0RImNV_DVtPuTDX9P4Lf4wXMmsJxIPIKyhQOyerB5oaL_2-KoFhaS7YJchDUDXGQiZBCXeMKx_dPWlYfah084KWynpTvsFPYFkbqyvQ20nTtjpOHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محکومیت ۱۸۰ هزار دلاری مهدی قایدی
🔹
با رأی کمیته وضعیت فدراسیون فوتبال با توجه به شکایت علیرضا نیکومنش از مهدی قایدی، این بازیکن به پرداخت مبلغ ۱۸۰ هزار دلار بابت اصل خواسته و مبلغ ۵ میلیارد و ۴۸۹ میلیون و ۵۷۰ هزار ریال بابت هزینه دادرسی در حق خواهان محکوم شد./تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/687383" target="_blank">📅 14:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687382">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
توجیه فرانسه برای حملات آمریکا علیه ایران: توافق منقضی شده است!
🔹
مدیرعامل فرودگاه امام(ره): پرواز مستقیم ایران - تونس مجددا برقرار شد.
🔹
رسانه‌های لبنانی از پرواز پهپادهای شناسایی رژیم صهیونیستی بر فراز بیروت و حومه آن خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/687382" target="_blank">📅 13:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687378">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار قم(Admin)</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R00M35YigQmd-OXjR-ZA3PWj6wLSDDH4CKH-fziKAaePwNy8bqNFW2sD1Py4fYMCU8mE0Q9tL9gkbxvJt7VyLoRzIB3US-mCuSFeWjCHtr-Y-32XkzGJcuEhjeKM8YjbNYUcIWJCUNR83mobQ_CGSWrEFTdYgg65-p4RxgqBxFd3OpRSWeACi-SPaK3fQCTj5m7p4EizxZR4_eIMngaWedURn7M0OBkbkwKJVSkEBwRHFp-t2tcEbnSNZ2k8i84WWwXVb1PedF-ra9oGluXZxGwfmq-f_lJG5KoIzOEXyNA1-Fxob4vzsVEoWcNhsbW3uEg5WPZIQ5DGNg55jha8-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DBYVb8ipzeKg7gfn-wbrEFED_sMgX2hNmPdMw3-XWJHvQKS82H4l52NX1Fj67-VwK8SHTs8Ke0XqVBf6jYqVYDk1cXH5BmjjKO8cxniX-cnmr0oVQGifU2PA_pmSKZeVyYZBVeI7AOwyMpc3bmHGLfFoHjRAu2pHiNL-Mh9pT1X2-uYO_AHGWu2BaKJopZhuVtVBOL-fBwNfehEzu1V_aVBHCpGDtIiSIPkrAGS9x3ld35t5myABX9w3xC5CwbUkbbRDvt4JIcxF2p6nZ8MkJgcDdsxAM7N4boagbOAubI8iot-3h_9O5ptjSpBrWB99b6Nhdqr9_yATC3tWbIixSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W4Z7un5ECQ912de6V_MaB-zItg-StOcw1nynrypSRgXqAvGNelCwQyBV9iA77UWcQGW4f4yYHCGKUv5EdR19RVGL2QNcjT02oy79agbpcv9AZmjzBU0eruxOChpjL-Bq74s32n_6rSzoA3KN0GqRj5ucpuYPHU1AZ6wy0Y_dGd5jn952cnmsHcv7d29H3nG20cPWdDsfGo1zcjU4GEeBmd3wHG6twgMC7D4pmE94p3iqfhOxYD_mlRn1-LnmF3EabdlVF1iq7U2niWZB_GQrk6wE16jdouJl_DkFA1ap5WxsWKVc4kaOOzYzzzbk2ldbYYX8nNOcnPOz5cOOINM0Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QGzLFghAV0XXf6_xYGu9WgFvmr6h3khwS8lm21qYYx7Kfvzd6a2CzFu5zEzALKKY1VzyLGHj5OmSlY5rrp6C_G_EwvrE4M0NcShZKDNRC9mPB8KYBsjFlFPyDlTORc1FEpdKTjl396sBpBZy5MC22KRr66fqYYFBs7oPAV50NLvLDfg1JSEsVHtHav5Gvw_NMaFBb1zSFa7xE6jXYMBswy2jSkvnRQbyxXy0wH_jAd5y8XlL-u5eoU1-bhPCuqc6BoSqeFf4X0hSRKlBKhrNagvkkSI8YNHoNxz-tENodktkIiM-1VqEFrPGkqZgVFx0Yj9POii4b0pWxqfXJXUwPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
امروز شنبه ۱۴ شهریور ۱۴۰۵ روز قم است
🔹
قُم تلفظی از نام کُم است که اعراب آن را به صورت امروزی درآوردند.
🔹
برخی پژوهشگران، واژه کُم در نام باستانی کمیدان (کمیران) را در معنای "شهر" دانسته و بین واژه‌های "کمیران"، "شمیران"،"تهران"، "چمران (در نواحی ساوه)" و "ایران" ارتباطات واژه ساختی قائل شده و نام قدیم قم را "کمیران" (در معنای "ایرانشهر") دانسته‌اند.
#روز_قم_مبارک
@akhbareghom</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/687378" target="_blank">📅 13:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687377">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
هلاکت ۲ تروریست در سیستان‌وبلوچستان
نیروی زمینی سپاه:
🔹
یک تیم تروریستی وابسته به آمریکا و رژیم صهیونی که قصد انجام اقداماتی بر روی اهداف از پیش تعیین‌شده در سیستان‌وبلوچستان داشتند، مورد ضربهٔ قاطع قرار گرفتند که منجربه هلاکت ۲ نفر از آنها شد.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/687377" target="_blank">📅 13:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687376">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a344525474.mp4?token=KRv9HbuT6VivSfb2p8d5xFtSw2-RvFu-mquqcyATP9um8EeQghAwMbmX4wWF_cVJa5Stl3nft2F-vrxH_d3i-sW0Z7F-uL8xlCLgqnuIKGpTzKOM7xtZYhQXhYah0TRFlEdkPhzXKPDvPn8vHMejNWTZxhIHw9I6Cmw9jSkTsvPlAaOMaA2nW4RQjQ1iP9bc7sM6Mx2VdbKqHzK2IjjESTQqGmgeEFBZp3FD7BDc_brQ-UbHjKeQOB32dd3PnSkKKxrTLHfm41TPh1lNGPthlW8E66AhXASDm6KoTNUCQvKCTrrlmX8TmjhrLGZ6wvuZ0tzZ8UEaAzZ1eO5iLxhnnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a344525474.mp4?token=KRv9HbuT6VivSfb2p8d5xFtSw2-RvFu-mquqcyATP9um8EeQghAwMbmX4wWF_cVJa5Stl3nft2F-vrxH_d3i-sW0Z7F-uL8xlCLgqnuIKGpTzKOM7xtZYhQXhYah0TRFlEdkPhzXKPDvPn8vHMejNWTZxhIHw9I6Cmw9jSkTsvPlAaOMaA2nW4RQjQ1iP9bc7sM6Mx2VdbKqHzK2IjjESTQqGmgeEFBZp3FD7BDc_brQ-UbHjKeQOB32dd3PnSkKKxrTLHfm41TPh1lNGPthlW8E66AhXASDm6KoTNUCQvKCTrrlmX8TmjhrLGZ6wvuZ0tzZ8UEaAzZ1eO5iLxhnnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علت خارش محل گزش پشه
🔹
علت اصلی خارش شدید ناشی از نیش پشه، واکنش سیستم ایمنی بدن به بزاق این حشره است. هنگام ورود بزاق پشه به زیر پوست، بدن آن را به عنوان یک عامل بیگانه شناسایی کرده و منجر به ترشح هیستامین می‌شود. این فرآیند باعث گشاد شدن رگ‌های خونی، تورم و قرمزی موضع شده که در نهایت احساس خارش شدید را ایجاد می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/687376" target="_blank">📅 13:36 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687375">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی بانک قرض الحسنه مهر ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7U-GsMKe7mycHg-7CMOo927mySkpmeObXFo3s-CuHSftc8homIwioz35HBI1k2azh7rC252D6hKyiT5QcLmWkSmiMzNZSJKkKFInjddoXDQDg8pU85H8EfX4rmx3_dyEp0DLS2uOEfP96by4RM-tf_tJgX-a52oBfrvsFottkd5QPAMuj6oxYr4-H1wZqbmi2p8SEG90MGj-MxoEBMee6RlKxmlmrbKJRHN-uKRHIGlOzHwGY__wd9C9UBf7PyUHeFaTpw5l6zjhu-PcgKfDKT1mCZejTnwMNobG3iNHjhDn3fMhdVOxKMwahA-d2ArJaO6Y5YR8m3Af8DfJacXHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
🔹
🔸
🔹
🔸
🔰
آدرس جدید دسترسی به سایت و پیشخوان مجازی بانک مهر ایران
🔹
آدرس‌های جدید سامانه‌های بانک قرض‌الحسنه مهر ایران به شرح زیر اعلام می‌شود:
🌐
سایت بانک مهر ایران
qmb724.ir
🌐
پیشخوان مجازی (مهر من)
my.qmb724.ir
🌐
چت بات
qbot.qmb724.ir
🔸
🔹
🔸
🔹
🔸
🆔
@mehreiran_bank</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/687375" target="_blank">📅 13:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687374">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پزشکیان: آموزش و پرورش مهم‌ترین چیزی است که می‌تواند کشور را نجات دهد.
🔹
دادستان تهران دستور تعیین تکلیف سریع محکومان مالی، به‌ویژه کسانی با بیش از ۱۰ سال حبس را صادر کرد.
🔹
توانیر: برق ۱۶ واحد صنعتی دارای ماینرهای غیرمجاز در یزد قطع شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/687374" target="_blank">📅 13:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687373">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f02229aa4.mp4?token=giDPqvFgGTqXINgzhqhTJG0xKB4idExJqXnJiFCxYTFW5C7ukXjGzRA9BQOD33Gcz_rnKj4Lwfm7DdPyFJCMMnGJD6vM3b7Z5rTvz1z6XhIUnVg4la6wucusxIYIkTwW9WYBLrATh2aShwTezI73oKXvtqsBaPh722uW3DJ06dKM1FjT3-B4R99NZZ1Y9ttTD9cv9cjVqGHBh8BybOKnCiKvTVz8lyXu4pmImwUxH2osRsN53bmSN1oFewzycsxmkLvjhHFz1yccwZSjc3renNZGBQQezQ7yz713XxUHNBs41yKiKW3UVBinR2-azvx8gi84H6CHIBx6cWduE5UEEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f02229aa4.mp4?token=giDPqvFgGTqXINgzhqhTJG0xKB4idExJqXnJiFCxYTFW5C7ukXjGzRA9BQOD33Gcz_rnKj4Lwfm7DdPyFJCMMnGJD6vM3b7Z5rTvz1z6XhIUnVg4la6wucusxIYIkTwW9WYBLrATh2aShwTezI73oKXvtqsBaPh722uW3DJ06dKM1FjT3-B4R99NZZ1Y9ttTD9cv9cjVqGHBh8BybOKnCiKvTVz8lyXu4pmImwUxH2osRsN53bmSN1oFewzycsxmkLvjhHFz1yccwZSjc3renNZGBQQezQ7yz713XxUHNBs41yKiKW3UVBinR2-azvx8gi84H6CHIBx6cWduE5UEEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: وقتی جوان ما در خیابان مشکل دارد مقصر ما هستیم/ ما نتوانستیم آنها را درست آموزش بدهیم
🔹
ان‌شاءالله خدا کمک کند تا راه حضرت ابراهیم را برویم و بت‌شکن باشیم
🔹
یاد نگرفتیم با همفکری به یکدیگر کمک کنیم، یاد گرفتیم دستور بدهیم و دیگران اطاعت کنند؛ اینجاست که کار خراب می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/687373" target="_blank">📅 13:23 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
