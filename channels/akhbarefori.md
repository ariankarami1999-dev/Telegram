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
<img src="https://cdn4.telesco.pe/file/OmnSSnxanoCXCxHJckNwsPtokqW-sErO63vLTsE7iUJHcjh_x8CWZ7lqy8f-gmdUANYH0KEJsmXrM9vS2H3eIHvUruRnhVpWsbiglnCnCdlnOvOKn14kJ902aRBg_Ht3dNXuBY4hzjRlI6UAzfKGbnAMUuRk7VlcoN2rXHZv1CUBwzluD2tU4tlbp7zQFNniYy_6YCINDjH-ZTOfr2DtCvyULJ4dJfxUPHqf0PeBHyqZry3o6tCqCpUPToR1DFp-e0R6qpiUNQTwngh2nfU_i0EZVADl36EHeFOC3b_tsrw2EU58js78A1qSKgznmf-LqsemhfzobkIsRfYhdoauzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.49M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 02:47:14</div>
<hr>

<div class="tg-post" id="msg-660679">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8pfN5WPERRgI3dxXzY0yK9ZfNzCwTUdBk60nDXpDGp7XKyAZ6tIGTdz-Q6dNtIJHnMBcny6uNGAB-Y0vJ5WBgjVifgtgpZUNcpNZJ7mLpqBAHtkqbqjLBx-nMREDGRZfxOXUYx-L9qUwaezcueQBn9A2m8VAamKtwHNJDbMa-7ydKUjiFJDas2WWF3X3OOwhFDZaDS2lkO-W407j5PN3HMeQD860UTgaUyA7ufjAi79U2PYL6lbKO2PxZKulSqQP6nYlyxmbO2uN6XcyzDVH1IISMPL8zOPTK6QfGhZPevIdQBCGg-P42mnqX9r_0z9AMOv21WnouNYBpcqgaqB_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/akhbarefori/660679" target="_blank">📅 02:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660678">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ما آمریکا و رژیم صهیونیستی را از هم جدا نمی‌کنیم اما در شیوه‌ها و روش‌ها اختلا‌ف‌نظرهایشان کاملاً مشهود است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/akhbarefori/660678" target="_blank">📅 01:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660677">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
بقائی دربارهٔ مرحلهٔ پیش‌روی تیم مذاکره‌کننده ایرانی: کار ما به عنوان دیپلمات‌، قطعاً از کار مدافعان وطن پای لانچرها و پشت سنگرها ساده‌تر نیست. شاید دشوارتر هم باشد، چون باید چشم در چشم دشمنانی بدوزیم که می‌دانیم مرتکب چه جنایاتی شدند و برای احقاق حق مردم و تثبیت دستاوردها با آنان مذاکره کنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/akhbarefori/660677" target="_blank">📅 01:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660676">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
بقائی: مردم ما، بغضشان از غم فقدان عزیزانمان -از دانش‌آموزان تا رهبر شهیدمان- را، تبدیل به یک «خشم حماسی» برای دفاع از ایران کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/akhbarefori/660676" target="_blank">📅 01:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660675">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
بقائی: ابرقدرت بودن ایران یک شعار نیست؛ ما دو قدرت اتمی را شکست دادیم
سخنگوی وزارت خارجه:
🔹
ایران ۲ قدرت اتمی که برخی کشورهای دیگر هم همراهی‌شان می‌کردند را شکست داد. ما شعار نمی‌دهیم بلکه واقعاً ابرقدرت هستیم.
🔹
جمهوری اسلامی ایران پوست ایران است و دشمنان می‌خواستند پوست ایران را بکنند. هر انسان وطن‌دوستی فهمید که این تفکیک (میان ایران و جمهوری اسلامی) تفکیک موهومی است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/akhbarefori/660675" target="_blank">📅 01:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660674">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
بقائی درباره تفاوت ایران امروز با ۶۰ روز پیش رو: لن یضروکم الی اذی و ان یقاتلوکم یولوکم الادبار ثم لا ینصرون
آن‌ها جز آزارهایی اندک به شما نمی‌توانند رساند واگر با شما پیکار کنند با عقب‌گردی، از شما روی برمی‌تابند و شکست می‌خورند، سپس یاری نخواهند شد
این وعده خداوند است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/akhbarefori/660674" target="_blank">📅 01:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660673">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
بقائی: ما شعار نمی‌دهیم
🔹
ما با دو قدرت اتمی و بسیاری از دولت‌هایی که حمایتشان می‌کردند و هدفشان فروپاشی ایران بود، جنگیدیم و یک وجب از خاکمان را ندادیم. هر انسان وطن‌دوستی فهمید که تفکیک جمهوری اسلامی و ایران از یکدیگر موهوم است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/akhbarefori/660673" target="_blank">📅 01:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660672">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
بقائی: احساس اقتداری که امروز تک تک ایرانیان دارند، بی‌سابقه است. جنگی که علیه ما به راه انداختند، ما را مقتدرتر کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/akhbarefori/660672" target="_blank">📅 01:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660671">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
بقائی: همه امید ما این است که همانطور که مردم در صدوده روز نشان دادند، در میدان ادامه دهند و به مسئولان خودشان اعتماد کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/akhbarefori/660671" target="_blank">📅 01:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660670">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
بقایی: تازه ابتدای کار هستیم، مدافعین وطن در عرصه دیپلماسی به اندازه مدافعین وطن در عرصه نظامی نیازمند حمایت هستند
🔹
کار ما تمام نشده تازه در ابتدای کار هستیم، مدافعین وطن در عرصه دیپلماسی به اندازه مدافعین وطن در عرصه نظامی نیازمند حمایت و انگیزه بخشی از جانب مردم هستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/akhbarefori/660670" target="_blank">📅 01:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660669">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
مذاکرات جمعه ایران و آمریکا در سوئیس الان قطعی نیست
بقایی، سخنگوی وزارت خارجه:
🔹
جلسه جمعه تا چند ساعت قبل قطعی بود ولی وقتی قرار شد روسای جمهور دو طرف (ایران و آمریکا) تفاهمنامه را امضا کنند، قرار شد درباره جلسه جمعه فعلاً تامل شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/akhbarefori/660669" target="_blank">📅 01:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660668">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
بقائی، با اشاره به تجربهٔ برجام، دربارهٔ بند ۱۴ توافق اینطور توضیح داد: ما برای پذیرفته شده این تفاهم‌نامه از سوی بازیگران بین‌المللی، به یک قاب حقوقی نیاز داریم و آن، «قطعنامه شورای امنیت سازمان ملل» است
🔹
اما در عین حال، می‌دانیم که آمریکا به تعهدات بین‌المللی خود پایبند نیست. با این وجود، با استفاده از همان سازوکار خیلی از کشورها را مورد تهاجم و تحریم قرار داده.
ضمانت اجرای این تفاهم، قدرت ماست؛ اهرم‌هایی است که ملت ایران در این مدت تولید کرده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/akhbarefori/660668" target="_blank">📅 01:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660667">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
بقائی: ضمانت اجرای این تفاهم قدرت ماست، اهرم‌هایی که ملت ایران در این مدت تولید کرده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/akhbarefori/660667" target="_blank">📅 01:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660666">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8KdIPQfg2ehomozqJHnvZ9wT941VUttoLppMEdxrx8cJX6rhtXhITRSxocRjKVVWpqO1SpsA0rx88sBwMhR00vSofGFquS6_1yMcmLP-D5-_OPPMDBeVdW2wju35kJB0Bt0DeTG3z55iBMUMW6Bc50C-zMoC71nZhwfWDWsAuipw4wvGetGH9UF_eISI5fs15Ha4ja5CYXlsU5eQmhjGghMFpX52JZ0L-tiGTI-FaTriSNb_pgLXe8jXxeXj2X5n6rRSGKcodkHDqPm7ojz5iEXJuXtXOBE-SaweqnV3WYgOZqpHBPRgd-UPk6si08_VOLExive167s4CaO9XHXrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینفلوئنسر آمریکایی؛ آنچه ایران به دست آورد
🔹
۳۰۰ میلیارد دلار
🔹
برداشته شدن تحریم‌ها
🔹
کنترل تنگه هرمز
🔹
حفظ برنامه موشکی
🔹
عدم تخریب برنامه هسته‌ای
🔹
آنچه ایالات متحده به دست آورد:
🔹
افزایش قیمت بنزین
🔹
میلیاردها دلار هزینه
🔹
عدم دستیابی به اهداف اصلی
🔹
آمریکایی‌های کشته‌شده
🔹
ما فریب خوردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/akhbarefori/660666" target="_blank">📅 01:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660665">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
اگر تعرضات اسرائیل در لبنان ادامه یابد، نقض تعهدات آمریکا محسوب می‌شود
بقایی، سخنگوی وزارت خارجه:
🔹
اگر تعرضات رژیم صهیونیستی به لبنان ادامه یابد، نقض تعهدات طرف مقابل در تفاهمنامه خواهد بود
🔹
ما آمریکا و رژیم صهیونیستی را از هم جدا نمی‌کنیم اما در شیوه‌ها و روش‌ها اختلا‌ف‌نظرهایشان کاملاً مشهود است.
🔹
رژیم صهیونیستی نمی‌خواهد کوچکترین فرصتی به هر روند دیپلماتیکی بدهد. اما این مسئولیت آمریکاست که رژیم صهیونیستی را وادار به احترام به تعهدات آمریکا به ایران در این سند کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/akhbarefori/660665" target="_blank">📅 01:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660664">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
بقائی: بند ۱۳ مشخص کرده که شروع مذاکرات درباره توافق نهایی زمانی انجام خواهد شد که مطمئن شویم اجرای بندهای ۱، ۴، ۱۰ و ۱۱ شروع شده و تداوم پیدا کرده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/akhbarefori/660664" target="_blank">📅 01:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660663">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
بقائی درباره بند ۱۳ یادداشت تفاهم: ما فقط در این بازه ۶۰ روزه راجع به بحث هسته‌ای و رفع تحریم‌ها و سازوکار اجرای بقیه بندها صحبت‌ خواهیم کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/akhbarefori/660663" target="_blank">📅 01:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660662">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpkgmew9w7ny5PtBVN65r4dIl569bgGAkPXxpIbDhbrOu6cn83PIupyzacTifq1AUanPwNMCy99p6Tc3I7kd2Lnpzs312RYGYxpuVTfkB67FghBUISlQlVmjL5deQ_z8VEY-WsPgVpC5YE8WlAJtcDRewqPRhU5EzWzEA0Vz6wxauS97NBIJ-IgAKMlyWurhc9v83J6iVRdHgFqJOh0kSzNkC_01ux3uVjp6GOvo8IrhA1a7pvkCVrsq1fY4Nm9WNYNfuDO5I_fmxZ7ZT3yUXldo-SfL5gLKl5uOpYftBvJttGCRRhELRXe8BIlGPWIaCa571R7XlcOTxXT42x-E1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل چهارم انگلیس به کرواسی توسط رشفورد ۸۵
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/akhbarefori/660662" target="_blank">📅 01:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660661">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHTxfvN8Xs7wdRbG3KqwghzYUbQpK1BZzCftomjvDW00wocqkAxCP05AS8M1vvUJep_c6qVqA5EivAWxTH4Cje0lc_c1bkRod5CPARQYAWcG2qxdpc7ga_he4aYiNpMeORdlXUs4QmiExc3ib6acjnYm8Y1c7YwQQLfsSTRAGC3uyuYxlGBFEq-NXM08X56Lunrh9HifLPUp8r0fKhbiw1zX1MPVtubxNTE4LeZzIPjTSFia8aJJEstoOBw4t-R491vgeEpZPN-5GC0KGS7Al-piCkThK2ZEMInmjLEgQiU1IwpDIIBYhktX9nIlMnWjnCciQVTBuJuOQpt7PYnnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اوپن سورس: در تمام عمرم معامله‌ای یک‌طرفه‌تر از این ندیده‌ام. کاملاً شوکه شده‌ام
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/akhbarefori/660661" target="_blank">📅 01:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660660">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
بقائی درباره بند ۱۱ یادداشت تفاهم: ما تجارب گران‌سنگی درباره مذاکرات با آمریکا داریم تلاش برای تعهدات متقابل است. احتمالا یک کارگروه تخصصی راجع به این موضوع خاص تشکیل شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/akhbarefori/660660" target="_blank">📅 01:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660659">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
بقائی درباره بند ۱۱ تفاهم: مهم این است که بتوانیم هرگاه اراده کنیم از اموال بلوکه شده استفاده کنیم، سازوکارهایش هم دیده شده، آمریکا متعهد هست همه موانع را برطرف نماید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/akhbarefori/660659" target="_blank">📅 01:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660658">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
بقائی: در جریان مذاکرات، همه تجارب تلخ از بدعهدی آمریکایی‌ها طی سال‌های گذشته را مد نظر داشتیم تا نتیجه بهتری حاصل شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/akhbarefori/660658" target="_blank">📅 01:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660657">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
همزمان با تفاهمنامه، درباره ۳ موضوع دیگر هم مذاکره شد
بقایی، سخنگوی وزارت خارجه:
🔹
فقط درباره تفاهمنامه مذاکره نکردیم؛ همزمان با متن، درباره آزادسازی دارایی های مسدود شده ایران، درباره بحث بازسازی خسارت و لغو تحریم‌های نفتی به صورت مجزا مذاکره کردیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/akhbarefori/660657" target="_blank">📅 01:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660656">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
بقائی: این تعهدی است که از امروز شروع می‌شود در حین نذورات هم باید ادامه پیدا کند تا رسیدن به توافق نهایی
بقایی:
🔹
ما فقط روی قول طرف روی کاغذ حساب نمی‌کنیم
🔹
ما فقط درباره این متن مذاکره نکردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/akhbarefori/660656" target="_blank">📅 01:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660655">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
بقایی: تحریم نفتی ایران باید برداشته شود، نه روی کاغذ بلکه با همه ملزومات آن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/akhbarefori/660655" target="_blank">📅 01:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660654">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
بقائی درباره بند ۱۰: یکی از تحریم‌های آمریکا، تحریم فروش نفت بوده که هزینه‌هایی برای ما ایجاد کرده، طرف مقابل متعهد شده همه را لغو کند نه روی کاغذ
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/akhbarefori/660654" target="_blank">📅 01:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660653">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
بقائی: در این بازه ۶۰ روزه نباید طرف مقابل نباید حضور نظامی خود را در منطقه تقویت کند و نقض تفاهم به حساب می‌آید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/akhbarefori/660653" target="_blank">📅 01:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660652">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5af3d26a8.mp4?token=JyvcB66z8L2ot5MhAagQh4dbvn7kYprUbUGk3PdAZLvd6cPQXlk9NEcmG7U9Tm3hI2o47lqQfVvq-pxNx9FR443Y_TZ915CeFVPseXn1IGc_DjYy0aa78lorInTi_Egj0_rN37_DhPOXyETfc3tbf0LTnaJUuqmt3aQF7E2ZrdoiCis8n8OFHxd-Ix9mCcD28D9TrkPGoEM8ydLceJkFeSFBGiBHi6uSTby29HnfDVt-lr0CWG4D4OUEJDUnCdeyqL086kroMUJhBx-xLfnzbEpaLr3BjBln1gaq9nnAd4T4HccAY8ofWiMz-qBkXmuR2vr09m6SZUSeCfvqhKDCaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5af3d26a8.mp4?token=JyvcB66z8L2ot5MhAagQh4dbvn7kYprUbUGk3PdAZLvd6cPQXlk9NEcmG7U9Tm3hI2o47lqQfVvq-pxNx9FR443Y_TZ915CeFVPseXn1IGc_DjYy0aa78lorInTi_Egj0_rN37_DhPOXyETfc3tbf0LTnaJUuqmt3aQF7E2ZrdoiCis8n8OFHxd-Ix9mCcD28D9TrkPGoEM8ydLceJkFeSFBGiBHi6uSTby29HnfDVt-lr0CWG4D4OUEJDUnCdeyqL086kroMUJhBx-xLfnzbEpaLr3BjBln1gaq9nnAd4T4HccAY8ofWiMz-qBkXmuR2vr09m6SZUSeCfvqhKDCaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل چهارم انگلیس به کرواسی توسط رشفورد ۸۵
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/akhbarefori/660652" target="_blank">📅 01:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660651">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
آمریکا متن تفاهم‌نامه با ایران را منتشر کرد
🔹
یک مقام ارشد کاخ سفید آمریکا متن این سند ۱۴ ماده‌ای را برای رسانه‌ها قرائت کرده است.
🔹
این سند با عنوان
«تفاهم‌نامه اسلام‌آباد میان ایالات متحده آمریکا و جمهوری اسلامی ایران»
منتشر شده است.
🔹
بررسی‌های اولیه نشان می‌دهد که متن منتشره توسط ایالات متحده با متن تفاهم‌نامه منتشر شده از سوی ایران مطابقت دارد./ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/akhbarefori/660651" target="_blank">📅 01:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660650">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
بقایی: تعداد بند های توافق ملاک نیست مهم منافع ملی کشور که در توافق گنجانده شود، برای ما دستور عمل های شورای امنیت ملی که صادر کرده بود بعد آتش بس ملاک بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/akhbarefori/660650" target="_blank">📅 01:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660649">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
بقائی: متن تفاهم به دو زبان امضا شده؛ این اوج شفافیت ما در اطلاع‌رسانی است. اگر فقط متن انگلیسی بود دچار تفسیر سلیقه‌ای می‌شدیم. این متن کاملا منطبق بر متن انگلیسی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/akhbarefori/660649" target="_blank">📅 01:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660648">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
بقائی: رقیق‌سازی مواد غنی شده، موضوع جدیدی نیست و برای این مطرح شده که راه بر گزین‌هایی که به هیچ عنوان برای ما قابل قبول نیست، بسته شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/660648" target="_blank">📅 01:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660647">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
بقائی: ما از ابتدا گفتیم مواد غنی‌شده ایران به خارج منتقل نخواهد شد؛ در صورتی که طرف مقابل دائم مطالبات زیاده‌خواهانه‌ای داشت که درنهایت به نتیجه نرسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/660647" target="_blank">📅 01:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660646">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
بقائی درباره بند ۸ تفاهم: ما درمورد تنها بعدی از موضوعات هسته‌ای که صحبت کردیم درباره رفع تحریم‌ها در بازه ۶۰ روزه بوده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/660646" target="_blank">📅 01:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660645">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
سازمان ملل: از توافق ایران و آمریکا و بازگشت دیپلماسی استقبال می‌کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/660645" target="_blank">📅 01:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660644">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
بقایی، سخنگوی وزارت خارجه: بدون هرگونه مماشاتی، اجرای تعهدات طرف مقابل را رصد می‌کنیم. در صورتی تعهداتمان را انجام می‌دهیم که طرف مقابل به تعهدش عمل کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/660644" target="_blank">📅 01:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660643">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
بقایی در پاسخ به اینکه اگر آمریکا بهانه‌تراشی کند: ان‌قلت بیاورند ما هم ان‌قلت می‌آوریم؛ تعهد در برابر تعهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/660643" target="_blank">📅 01:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660640">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
واشنگتن امضای تفاهم‌نامه با ایران را تایید کرد
🔹
دو مقام آمریکایی بامداد پنجشنبه به وبگاه «آکسیوس» گفتند که واشنگتن و تهران، یادداشت تفاهم برای پایان جنگ را امضا کرده و اکنون اجرایی شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/660640" target="_blank">📅 01:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660639">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
بقائی درباره بند ۷ تفاهم: متن تصریح کرده همه تحریم‌های یک‌جانبه آمریکا اعم از اولیه و ثانویه برداشته شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/660639" target="_blank">📅 01:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660638">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بقائی:  از هیچ فرصتی برای مستندسازی و پیگیری و تبیین جنایاتی که علیه ملت ایران اتفاق افتاد نخواهیم گذاشت
🔹
از هر سازوکار و نهاد و فرصت بین‌المللی برای احقاق حق استفاده خواهیم کرد. اینها خارج از این یادداشت تفاهم است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/660638" target="_blank">📅 01:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660637">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
بقائی: قاعدتا از هر سازوکاری استفاده خواهیم کرد که این تعهد صورت بگیرد برای ما منبع آن مهم نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/660637" target="_blank">📅 01:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660636">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
بقائی: بعضی از آسیب‌هایی که به ما زدند به عدد و رقم درنمی‌آید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/660636" target="_blank">📅 01:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660635">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
بقائی: بازسازی خسارات ناشی از جنگ برای ما فوق‌العاده مهم است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/660635" target="_blank">📅 01:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660634">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
بقائی در پاسخ به این سؤال که چرا برداشتن محاصره دریایی در متن نیامده: چون زودتر این اتفاق افتاد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/660634" target="_blank">📅 01:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660633">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
بقایی: اگر متن را مبنا قرار می‌دادیم باید رفع محاصره از امروز انجام می‌شد اما رفع محاصره زودتر انجام شد. باید در عمل شاهد این اتفاق می‌بودیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/660633" target="_blank">📅 01:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660632">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
بقایی، سخنگوی وزارت خارجه: موضوع تنگه هرمز به عهده ایران و عمان است. فقط ایران و عمان ۲ دولت ساحلی تنگه هرمز هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/660632" target="_blank">📅 01:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660631">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
بقائی: در رصدی که انجام شد مشخص شد کشتی‌های ما بدون مشکلی وارد بنادر شدند و خارج شدند و این تعهد {آمریکا به رفع محاصره} شروع شد. تعهدات ما پس از امضای این سند شروع خواهد شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/660631" target="_blank">📅 01:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660630">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
بقایی: با عمان تا حدود زیادی به سازوکار مشخص درباره تنگه هرمز با حفظ حاکمیت ایران رسیده‌ایم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/660630" target="_blank">📅 01:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660629">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
بقایی: تصمیم داریم برای اطمینان از تردد ایمن کشتی‌ها تدابیری اتخاذ کنیم قاعدتا خدماتی ارائه خواهیم داد و هزینه‌اش دریافت خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/660629" target="_blank">📅 01:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660628">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
بقایی: ما برای دهه‌ها نگهبان تنگه هرمز بودیم اما سواستفاده شد و ایران طبق حقوق بین‌الملل تدابیری اتخاذ کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/660628" target="_blank">📅 01:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660627">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
موشک‌های ایران فقط برای شلیک شدن هستند نه برای مذاکره
بقایی، سخنگوی وزارت خارجه:
🔹
موشک‌های ما اصلاً دوست ندارند که کسی درباره‌شان حرف بزند.
🔹
موشک‌های ایران فقط برای شلیک شدن هستند نه برای مذاکره.
🔹
درباره توانایی دفاعی ایران در هیچ روندی و با هیچ طرفی صحبت نخواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/660627" target="_blank">📅 01:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660626">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
بقایی، سخنگوی وزارت خارجه: قرار بود طی ۳۰ روز محاصره برداشته شود و متقابلاً ایران هم درباره تنگه هرمز این کار را انجام دهیم. اما بعد از تحولات مربوط به حمله رژیم صهیونیستی به ضاحیه و تهدیدات جدی که از سوی ایران انجام گرفت، مذاکرات فوری انجام گرفت و قرار شد آمریکا تعهداتش را فوری انجام دهد
🔹
در رصدی که انجام شد مشخص شد کشتی‌های ما بدون مشکلی وارد بنادر شدند و خارج شدند و این تعهد {آمریکا به رفع محاصره} شروع شد. تعهدات ما ‍بس از امضای این سند شروع خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/660626" target="_blank">📅 01:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660625">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
متن فارسی تفاهمنامه نیز به عنوان سند رسمی به امضای ایران و آمریکا رسیده است
🔹
با پیگیری و پافشاری ایران، متن فارسی تفاهمنامه اسلام آباد میان ایران و آمریکا نیز به عنوان یک سند رسمی به امضای دو طرف آمریکا و ایران رسیده است. /تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/660625" target="_blank">📅 00:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660624">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUIS4aPCK7HlgE1womJNvZZ6MdTOcnJfgBVf58khcYxTe0kHcQWzjE4BrreSasJFprrmbkbTSl-1wAcVXeQa8xBr-KAysR2dBnWFUp3Fp21jh_VRxiQuydrJr1kFQ2ncJexbic6i2ZVT6xqW1xfqydqEZJTfLylqlbiuV8yHiTdbA9Fh0CsY-ElRvT6_C6wXa-FRs5YrnH9XsVHBl1Uv7WFM8rPHBHwKHWv3z4_NdAYm84h6LVhYqtezkGuGKcY_504eZ_fL4sIaX_aKfOp0or3CJd7nQmgPWXWqdxRCbd8bHBGCr2MYcjoNCfXUErskplhyVb0-z-ncQcCSLFMvbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشنگتن امضای تفاهم‌نامه با ایران را تایید کرد
🔹
دو مقام آمریکایی بامداد پنجشنبه به وبگاه «آکسیوس» گفتند که واشنگتن و تهران، یادداشت تفاهم برای پایان جنگ را امضا کرده و اکنون اجرایی شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/660624" target="_blank">📅 00:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660623">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
بقایی، سخنگوی وزارت خارجه: تصمیم حکیمانه جمهوری اسلامی این بود که در این مرحله درباره موضوع هسته‌ای مذاکره نکنیم. قرار شد تمرکز بر خاتمه جنگ باشد و این کار را انجام دادیم
🔹
از زمان اجرای تفاهمنامه، که الان است، ظرف ۶۰ روز درباره موضوع هسته‌ای و تحریم‌ها مذاکره کنیم. اگر زودتر هم مذاکره به نتیجه برسد، بهتر است. ولی با توجه به پیچیدگی موضوع، عدد 60 روز منطقی است  و اگر لازم باشد، این زمان تمدید می‌شود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/660623" target="_blank">📅 00:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660622">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
متن کامل تفاهم نامه ایران و آمریکا منتشر شد
👇
khabarfoori.com/fa/tiny/news-3223896
🔹
فاجعه اختلال بانکی / در این بانکها پول نگه ندارید!
👇
khabarfoori.com/fa/tiny/news-3223880
🔹
پزشکیان و ترامپ، جمعه تفاهمنامه را امضا می کنند؟
👇
khabarfoori.com/fa/tiny/news-3223875
🔹
حماس با تحویل سلاح خود موافقت کرد
👇
khabarfoori.com/fa/tiny/news-3223690
🔹
تصویری از همسر زیبای نیمار
👇
khabarfoori.com/fa/tiny/news-3223828
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/660622" target="_blank">📅 00:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660618">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
بقایی: تفاهمنامه ایران و آمریکا قرار شد که به صورت دیجیتال امضا شود
🔹
وقتی تفاهمنامه به امضای روسای جمهور دو کشور برسد نقض آن هزینه بیشتری خواهد داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/660618" target="_blank">📅 00:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660617">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
بقایی، سخنگوی وزارت خارجه: کار ما پایان نیافته بلکه کار تازه آغاز شده است. هم باید مراقب اجرای آن توسط طرف مقابل باشیم. و هم درباره موضوع هسته‌ای و رفع تحریم‌ها مذاکره کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/660617" target="_blank">📅 00:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660616">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بقایی، سخنگوی وزارت خارجه: اینکه در این مرحله یک توافق خاتمه جنگ را امضا کرده‌ایم به این معنا نیست که گذشته را فراموش کرده باشیم و درسهایی که به بهای گزاف آموخته‌ایم را از یاد برده باشیم.
🔹
الان کار ما سخت‌تر از قبل است؛ چون همیشه اجرای توافقهای بین المللی…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/660616" target="_blank">📅 00:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660615">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بقایی: الان اگر متن را مرور کنیم خواهیم دید که چیز ناگفته‌ای را در این مدت نداشته‌ایم؛ همه موارد را کم و بیش بیان کرده‌ بودیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/660615" target="_blank">📅 00:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660614">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بقایی: الان اگر متن را مرور کنیم خواهیم دید که چیز ناگفته‌ای را در این مدت نداشته‌ایم؛ همه موارد را کم و بیش بیان کرده‌ بودیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/660614" target="_blank">📅 00:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660613">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
بقایی: تا این لحظه برنامه حضور تیم‌های مذاکره کننده در ژنو پابرجاست اما امضای تفاهمنامه به صورت دیجیتالی بوده و مراسم امضایی در سوئیس برگزار نخواهد شد
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/660613" target="_blank">📅 00:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660611">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
بقایی، سخنگوی وزارت خارجه: جمهوری اسلامی ایران نشان داد که دوستانش را در هیچ شرایطی تنها نمی‌گذارد. برای ما آتش بس و خاتمه جنگ در لبنان به اندازه ایران اهمیت داشت و دارد. در بند اول یادداشت تفاهم، سه بار نام لبنان آمده است. احترام به تمامیت سرزمینی و حاکمیت ملی لبنان آمده است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/660611" target="_blank">📅 00:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660610">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd6ca52db.mp4?token=Llqr8k4wrYKWAZl_68uPxhUNjn9vCMDtZibGJ-ZE8h-CmmTQeUpWGzccjvN-BJswk76FHb6Qe44PDhKp6gXymKq8VjyK1rOJk0fFjuYj0qRjjYhcZCKXt26q5OI45O3lav8u0En7HJ6pDOROwE6_seUBct5rA29b5bUQkNirU2BfKtrjsxphJZh40TD802gVmdRsvaf0b1mHWLQckrJwDx3vxIyaNmCU-LQnHIg_S3Ifgu6j9kR9dyd9P4MuhFzFAkpQOwUcDev8U1zdt-4ktuZ1YRujyNVKITJgy3XW0cszZ2OAl9pto9MjSoMKOVY2HfEfkCpegqlMgGOWG6LexA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd6ca52db.mp4?token=Llqr8k4wrYKWAZl_68uPxhUNjn9vCMDtZibGJ-ZE8h-CmmTQeUpWGzccjvN-BJswk76FHb6Qe44PDhKp6gXymKq8VjyK1rOJk0fFjuYj0qRjjYhcZCKXt26q5OI45O3lav8u0En7HJ6pDOROwE6_seUBct5rA29b5bUQkNirU2BfKtrjsxphJZh40TD802gVmdRsvaf0b1mHWLQckrJwDx3vxIyaNmCU-LQnHIg_S3Ifgu6j9kR9dyd9P4MuhFzFAkpQOwUcDev8U1zdt-4ktuZ1YRujyNVKITJgy3XW0cszZ2OAl9pto9MjSoMKOVY2HfEfkCpegqlMgGOWG6LexA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بقایی: همین الان که در حال صحبت هستیم متن توافق رسما به امضا رئیس جمهور های دو طرف رسیده است
🔹
قرار بود که بامداد روز ۲۸ خرداد ماه رئیس جمهور دو کشور این متن و توافق رو امضا کنند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/660610" target="_blank">📅 00:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660609">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
بقایی، سخنگوی وزارت خارجه درباره تفاهم نامه ایران و آمریکا: متن تفاهمنامه ایران و آمریکا الان رسماً نهایی شده است چرا که دو طرف آن را امضا کرده‌اند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/660609" target="_blank">📅 00:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660608">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d1114b63.mp4?token=gKgX6juhCQac0eDPZ3QJ5MaOqKkf82WUMhmlFNMvOs2aOPivH9aULtt78yWMy2C5VHWcE-MehebUD-sEvcpmu2dQgURe9wLj8QSE5G1O14OFB20xCqUaCLNfgl4WLRcgvPk-u8SZLtMfKOC_CeeEonRj7Dnar6T4xqOkl2mqg-jhdM7lsijHOL1WNrLY3tK1s-x2-cKvy-PDdGqT6dSlkM6I85sZHpeTB9bu_o0vAa0ECtmDWfw7STk0NBjzcx2h0XHeAkNT38XJxSt9o910VvWnkbluirmgqCu2y5KXmvu7Tf2xkuqws97uH-Z7d6_GftzPSdBdZQOojxtuSOxNxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d1114b63.mp4?token=gKgX6juhCQac0eDPZ3QJ5MaOqKkf82WUMhmlFNMvOs2aOPivH9aULtt78yWMy2C5VHWcE-MehebUD-sEvcpmu2dQgURe9wLj8QSE5G1O14OFB20xCqUaCLNfgl4WLRcgvPk-u8SZLtMfKOC_CeeEonRj7Dnar6T4xqOkl2mqg-jhdM7lsijHOL1WNrLY3tK1s-x2-cKvy-PDdGqT6dSlkM6I85sZHpeTB9bu_o0vAa0ECtmDWfw7STk0NBjzcx2h0XHeAkNT38XJxSt9o910VvWnkbluirmgqCu2y5KXmvu7Tf2xkuqws97uH-Z7d6_GftzPSdBdZQOojxtuSOxNxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم انگلیس به کرواسی توسط بلینگام
🔹
انگلیس ۳ - ۲ کرواسی
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/660608" target="_blank">📅 00:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660607">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
داسیلوا: ترامپ در انتخابات برزیل دخالت نکند
🔹
رئیس جمهور برزیل در جریان یک کنفرانس مطبوعاتی در واکنش به اظهارات ترامپ که پیش‌تر برزیل را خطرناک و از نظر سیاسی ناخوشایند خوانده بود، گفت که از ترامپ می‌خواهم که در انتخابات برزیل دخالت نکند، همانطور که برزیل به دنبال دخالت در فرآیندهای انتخاباتی آمریکا نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/660607" target="_blank">📅 00:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660606">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2vsdU1ozQ29OSqM9Zgq75xVl7Unv6LZA9e85yVkg-Z0xpWGOsHasG6OM6Z8GFEWxlQia1rd2n2osiOCifFK0kfOr0EPLXaM6FO-mzhAOLK6GKwCmBY_PHTcUmmjQcwNazsdgrffwnPDMA4_Jgv1WqzvW820oZjy9z6NA4AtM4JZ-qbg1ZFPNtne7Vpcvm1TAgga1vmOI_wP62QVPtnvJBs_By_FFjAmNmjCieiNv2Yd7vobFX4P35JxCi4MYRhnTCzdQK65GMje2a4ADjASXobP6lfX14OFNiWB6e1HCQ8M127ch-pdHF2uQmZYbUKJEnNXgPAe3PlUChtkQMxUjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در
#شب_سوم
محرم، شبی که به نام نازدانه‌ی اباعبدالله، حضرت رقیه (س) گره خورده است
✨
امشب یادمان می‌آید که آسمان، جایگاه فرشته‌هایی است که زود پرواز کردند. به یاد شهیده  خردسال
«آوینا برزگر»
عزیز؛  باشیم که امروز او در میان پروانه‌ها، مهمان سفره‌ی حضرت رقیه (س) هست .
🕊️
@Heyate_gharar</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/660606" target="_blank">📅 00:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660605">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ff0adc2d.mp4?token=d6haNlPYugQBop1ARXiXQiofyVB1bufM20uJFseiCDaO_XrdnEjCfnw0y10ppe36GeyaNUewEnSI06y42zufFSa7Y9_RXuj5N8G-bJ_eWgpqNpb3y4xFS2qPRQAgx4Tq7gL9ebUqp6cL8znPdgmP4zwcVkxM4ib_F1p-nwtiprN2UZE0Y_OBa-Tin22xwK0FxJyF4xfOeHbZOel_JAARRCSVAfjKLzHvE-kd4sSjCWSheoY_rDfVu4fj1m6OvCCciO7tigBppkBhDVP1vHIwiEPkb6ug1e__qrQotRy7_aqHAY2iXfbx7cHvyaAZd4IjXAnNTFgP3rGsIBwztep55w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ff0adc2d.mp4?token=d6haNlPYugQBop1ARXiXQiofyVB1bufM20uJFseiCDaO_XrdnEjCfnw0y10ppe36GeyaNUewEnSI06y42zufFSa7Y9_RXuj5N8G-bJ_eWgpqNpb3y4xFS2qPRQAgx4Tq7gL9ebUqp6cL8znPdgmP4zwcVkxM4ib_F1p-nwtiprN2UZE0Y_OBa-Tin22xwK0FxJyF4xfOeHbZOel_JAARRCSVAfjKLzHvE-kd4sSjCWSheoY_rDfVu4fj1m6OvCCciO7tigBppkBhDVP1vHIwiEPkb6ug1e__qrQotRy7_aqHAY2iXfbx7cHvyaAZd4IjXAnNTFgP3rGsIBwztep55w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدباقر قالیباف: خون‌خواهی رهبر شهید آزادی قدس است؛ ۱۰۰ نتانیاهو بند کفش امام شهید ما هم نمی‌شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/660605" target="_blank">📅 00:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660604">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acmgtQlKL7J49UA3kp7IzKrH_coIdLxr2VgJ7zkhcqkKAk51N_KbUQJgJx2zHWbTAjiRMh_DVF9Ty2VfOjC6T0Jj9Ar_719YDZ5aiQqJBT786hxwX_dU8LcF63WzQoI0hnk4d7AY2Zxry_oFQXapciE6XQiEWHrLaRadcLH2F4iu6oRpz9ECFD8GFNnIoKF_dtaYkqGoURvdzZpbzN3J_oWayA7TpWKmKp57jPOVXtEZ3dIDBZZuiVCuhJEI6W2LmdTMjhCz9x_fpFpjdXvb_T81Dk0D38K_9VMvEDle_5MyLKzgznpypY10IkWlvBq0sxEx_XXAe9dNcuZBgHVpUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری کمتر‌دیده‌شده از شهید سپهبد علی شادمانی در دیدار با فرمانده شهید کل قوا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/660604" target="_blank">📅 00:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660603">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4ed067d22.mp4?token=qxjWHvHn0pjALXU06sbaQzdqKuItuv-DxRk9O3FOxlWFNabkEaiey1Yo7yPYZyBUqvu1FnpnwSPwxVtfIu9UGAcboJH-kI-SC1uVOVXoyM4Dt63N8AXPoyPGhg_1xgoH6U38ueojo1PeAV0nftZTEg5h1I0jYyFsb6M2HEdhgoVJBkeUaim-PwHJLSKGPjhJ3Z78EEjkqg7NMYPYX53qPwjA5v3fATm_R_IyPKfiW5ZyOtbsX8THEt6Sb_2x_dRl-buCWUZ9nMPnuOdUbV6sNWOHl4ucqc1EpcVloCdYNpY-SeTIrv3LwqSJdUuouqJoT7WIROfMHX9GjOCCo5Uzsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4ed067d22.mp4?token=qxjWHvHn0pjALXU06sbaQzdqKuItuv-DxRk9O3FOxlWFNabkEaiey1Yo7yPYZyBUqvu1FnpnwSPwxVtfIu9UGAcboJH-kI-SC1uVOVXoyM4Dt63N8AXPoyPGhg_1xgoH6U38ueojo1PeAV0nftZTEg5h1I0jYyFsb6M2HEdhgoVJBkeUaim-PwHJLSKGPjhJ3Z78EEjkqg7NMYPYX53qPwjA5v3fATm_R_IyPKfiW5ZyOtbsX8THEt6Sb_2x_dRl-buCWUZ9nMPnuOdUbV6sNWOHl4ucqc1EpcVloCdYNpY-SeTIrv3LwqSJdUuouqJoT7WIROfMHX9GjOCCo5Uzsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم کرواسی به انگلیس توسط موسی ۵+۴۵
🔹
انگلیس ۲ ــ ۲ کرواسی
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/660603" target="_blank">📅 00:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660602">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28df5a9b7c.mp4?token=M4JjW_LnJOsGEeMCFEG8ToZqOp6C3WMwZxNJIlegeGbwaFGtSO6e6ICtb2vj7rig9v5S5SvVeqy8kGUZz6pPZbfHkpZbtKttYfzdKxafIXW_2fX7zx--7vobTFyKkP_-O2MQlYA1-I6UqRiVTuSr93NAIR7ge_QZPo7zoorxfnqRuP-a5Qv2qFLsu_uICEL6Yne9fCGSJesBS63FlLPhLgucDMFVSj8_PshGI5zUrMOG6uxRqH25uQl-uE1aP8EgV--k4UX4eG0BM4CyS8SCH_tls2Aic_WCEg5AAYR7EI-ZVJtzUvd1J8sFGN06GKr0xHs9CMkf9_UIoDWWMojY0DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28df5a9b7c.mp4?token=M4JjW_LnJOsGEeMCFEG8ToZqOp6C3WMwZxNJIlegeGbwaFGtSO6e6ICtb2vj7rig9v5S5SvVeqy8kGUZz6pPZbfHkpZbtKttYfzdKxafIXW_2fX7zx--7vobTFyKkP_-O2MQlYA1-I6UqRiVTuSr93NAIR7ge_QZPo7zoorxfnqRuP-a5Qv2qFLsu_uICEL6Yne9fCGSJesBS63FlLPhLgucDMFVSj8_PshGI5zUrMOG6uxRqH25uQl-uE1aP8EgV--k4UX4eG0BM4CyS8SCH_tls2Aic_WCEg5AAYR7EI-ZVJtzUvd1J8sFGN06GKr0xHs9CMkf9_UIoDWWMojY0DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضربه سر زیبا، کین بار دیگر انگلیس را پیش انداخت
🔹
انگلیس ۲ - ۱ کرواسی
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/660602" target="_blank">📅 00:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660601">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
روایت خلبانان جنگنده های F۵ ایران که پایگاه های امریکا در کویت را هدف قرار دادند
🔹
این‌قدر پایین پرواز می‌کردیم که از بین دو تا کشتی عبور کردیم؛ عرشه‌شان از ما بالاتر بود؛ یعنی ملوان‌ها از عرشه ما را نگاه می‌کرد
🔹
هواپیماهای کویتی به اشتباه سه جنگنده امریکایی را که قصد حمله به ایران را داشتند به جای ما مورد هدف قرار دادند
🔹
هیچ فیلم و عکسی نگرفتیم؛ اصلاً فکر نمی‌کردیم، برگردیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/660601" target="_blank">📅 00:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660600">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvtjDYC1j9NRDT579odyqCgMC4FfCAxlKgzdam_JxWxvy_l2hr6rvleiOdIDk4HXCNALpgTf71MeDiYePG0Ap6dxxUgVygMdZahRecZ7zbOpDNpMGknZU4l7UO-txntPCFt5EHNhfijkOsqsU2IPn-dJfGNrkXuCtRFOdPTkR_vKuSvIRxiJugHLRs4xdauMdjgS2uP42MeXoByT8WgbXsO9A5Ycu90-q77LHOeK08bjmwg_yOiyKkZ_uW7hnvd_r47Wq8g6NXGYwQAmt--1zR0rOefQR2CHDBrFJ541M2PttKc4CgzD4K3ru0NtSifkdaNuG3yxC_GyM_TSjBacxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برتری سرمایه انسانی در ادراک عمومی
🔸
در این نظرسنجی بیش از ۴۱ هزار نفر شرکت کردند که سهم روبیکا حدود ۶۴٪، بله ۲۶٪ و تلگرام ۱۰٪ بوده است.
🔸
حدود دو سوم شرکت‌کنندگان مردم و سرمایه انسانی و حدود ۱۱٪ هم موقعیت ژئوپولیتیک را مهم‌ترین سرمایه ایران می‌دانند.
🔸
در نگاه عمومی، سرمایه انسانی و جایگاه ژئوپولیتیک مهم‌ترین دارایی‌های کشور تلقی می‌شوند و این برداشت بیشتر از تجربه زیسته مردم و ارزیابی عملی آن‌ها از ظرفیت‌های ملی شکل گرفته است.
@amarfact</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/660600" target="_blank">📅 00:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660599">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe26318adc.mp4?token=D-36qnPU7ep7VDqPjjlzxUyB8nOIci8PNCjKNvH0WPnYGZa-ILbhp_Fj1p7wUDlHRNE0i3-OvVnIJ7sfTKLinrlIoqi-o8Ooqv_pG39e6sJFcz1uc-s9ll6GFj6pfYbvlly_B5YTwLX2VAK4Ukf5hLEbj9JfK98a-PqSMztrLvrm-GGr88M1UUZG3kYYm7cAhMUFJidxHz9hTU-wPruN0DqGcVcHPZ1EY5Pu7DA1FMDrMpUzVGtq0_YckAdadar2iSHzobDpQZxDDQX8EtFboKcM_8KwPIyB27izXeHJU_M--h1GpXehXxe-Ol2NpWAL6Kjhsnl4KP4V0URUXde4D2plA06ukGTl-m25TTbr_G7cRjxf76Y5Ukck25zUs1AHjfZrjyZiqm8gGSFWUfMfuwMnzsj39aDZ0hCyAp8NzDaH5zM7w-OlvjmyZe7sPtr2mGMfXH5HNt7Dx_dwKw_kDOapQNZTdsVUB3HhnB2nXS-5BsfdzQPgImtnRB3hMimHd5s3eHOISN-FP3f2v7PX0Dv0L3PJBQAMK6ZEtexv8wKQH7gW7qzI8Wz9Al9m1z09eL14Wxfzl7Nnz1OducnA8DzzP5WnsPJ6wohqC9yUoy-UhAtjGzdGtm7jk-ZMhaFg3bOKpDkdlMQDY6aaeXU_UbTZgziZQbJA0S--sM9lsPo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe26318adc.mp4?token=D-36qnPU7ep7VDqPjjlzxUyB8nOIci8PNCjKNvH0WPnYGZa-ILbhp_Fj1p7wUDlHRNE0i3-OvVnIJ7sfTKLinrlIoqi-o8Ooqv_pG39e6sJFcz1uc-s9ll6GFj6pfYbvlly_B5YTwLX2VAK4Ukf5hLEbj9JfK98a-PqSMztrLvrm-GGr88M1UUZG3kYYm7cAhMUFJidxHz9hTU-wPruN0DqGcVcHPZ1EY5Pu7DA1FMDrMpUzVGtq0_YckAdadar2iSHzobDpQZxDDQX8EtFboKcM_8KwPIyB27izXeHJU_M--h1GpXehXxe-Ol2NpWAL6Kjhsnl4KP4V0URUXde4D2plA06ukGTl-m25TTbr_G7cRjxf76Y5Ukck25zUs1AHjfZrjyZiqm8gGSFWUfMfuwMnzsj39aDZ0hCyAp8NzDaH5zM7w-OlvjmyZe7sPtr2mGMfXH5HNt7Dx_dwKw_kDOapQNZTdsVUB3HhnB2nXS-5BsfdzQPgImtnRB3hMimHd5s3eHOISN-FP3f2v7PX0Dv0L3PJBQAMK6ZEtexv8wKQH7gW7qzI8Wz9Al9m1z09eL14Wxfzl7Nnz1OducnA8DzzP5WnsPJ6wohqC9yUoy-UhAtjGzdGtm7jk-ZMhaFg3bOKpDkdlMQDY6aaeXU_UbTZgziZQbJA0S--sM9lsPo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: انتقادات به‌جا و حتی برخی انتقادات نابه‌جای مردم نسبت به مذاکرات را به جان می‌خریم و از ملت تشکر می‌کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/660599" target="_blank">📅 00:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660598">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
قالیباف: پرداخت هزینه خدمات عبور از تنگه هرمز در تفاهم‌نامه تثبیت شده است
🔹
کشورهای ساحلی تنگه ها در قوانین بین المللی حقوق و وظایفی دارند از جمله این که دیگران باید هزینه خدمات شان را پرداخت کنند.
🔹
دشمنان ایران را خدا از احمق ها آفریده و باعث شدند ظرفیت…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/akhbarefori/660598" target="_blank">📅 00:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660597">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6wpKc3HADIVdhhjD13PyeNIzp0CNRocCdYr8hvDsnry_fQLXUY5SrDpdbL3y6c6WIkuqy6DXzczwHSZv5oiuKWlvIZUCSRUGtmhx4pl8juBq2JtHtP1dWtEbJFXbi6AU_66LZZ056t-M40xLeKcmZTmlGpgO2SOVjhWeQZBR3ni4obelR8KYVD0Cw9TtnkoXqrsy-oNQWWwGfdGSm1R5UWHAS_62C3oF3Ndhzx9YzMGSdYgljneIl4n-nEBmQPN8HnBJOxpwzgLOTuMfVztmGRPX9S4wlLi3prGy6_Y2bR8-A2PjAc5ENdXfUfSNcvC4KhxnQAuJ4XjaYD-PD6CpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا استفاده از مایکروویو برای سلامتی مضر است؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/660597" target="_blank">📅 00:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660596">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adf4812f88.mp4?token=cwj0IuKEOq-BCT4g8L-UNtL7SP3tBIVEkF_Asoq1iNgEGP3fewjW0hwfUq6K1tf-liLqoEHcyPD-AesmN1M3asdxdbhNEX3XsMxCTgquehbkV4VOHE6K3vr8MmJbAWU2RVvrsMYkmqaYDxpqUddfe_vXM-wbOVZ0t_b4_RgSL_HERaI2erzYE0R7D5L0r6Q5BVvv3fXa4GT0QwCarGB_X6BvwmASAXoEn9uYwXwP7HKzGAiUGR_Z367QP_z_QeYNtqYYT9fCpHiWButM1k7H3jhlq9lhxmar0e-luDpcU_ma6ybVNUa2cK7xuKb_JGvPStqwq7G4LgV05bnP1xYBBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adf4812f88.mp4?token=cwj0IuKEOq-BCT4g8L-UNtL7SP3tBIVEkF_Asoq1iNgEGP3fewjW0hwfUq6K1tf-liLqoEHcyPD-AesmN1M3asdxdbhNEX3XsMxCTgquehbkV4VOHE6K3vr8MmJbAWU2RVvrsMYkmqaYDxpqUddfe_vXM-wbOVZ0t_b4_RgSL_HERaI2erzYE0R7D5L0r6Q5BVvv3fXa4GT0QwCarGB_X6BvwmASAXoEn9uYwXwP7HKzGAiUGR_Z367QP_z_QeYNtqYYT9fCpHiWButM1k7H3jhlq9lhxmar0e-luDpcU_ma6ybVNUa2cK7xuKb_JGvPStqwq7G4LgV05bnP1xYBBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوپر گل مارتین باتورینا به انگلیس در دقیقه ۳۶
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/akhbarefori/660596" target="_blank">📅 00:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660595">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtoBBmx0nDet6jr9jHWJ3WbeCCioTR9FtbRJWEvvXlybeA2GPjX_xUbORerWa7FEtwO5FWQ2W7kdRtJ2t_K9Q3dn58Rpz-zjKshNRoGO3T2wkc5zCfH9_ikWFuiGzbevTHIpGjze8qRDClnMcWjMXrI5ffOlXdCv8thFUKtP-l4Pnp4NVEWtH3PNZsK-mERTqRKvrlx1GQOux1xc_y7Ol_OrQhLDTl6WRFQ-ixld1-Vxp4C82LZkWIMjNV4bRe5W4opjawIUzyKrLMfvbJdDyir66SZ0Sb5E3_IrMuDQKlit54h3zhwx3SJKnwFg6P0fbl-SVHkhy9DK_5FcgjMaMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله صهیونیست‌ها به جنوب لبنان با بمب‌های فسفری
🔹
رسانه‌های لبنانی گزارش دادند که ارتش رژیم صهیونیستی به شدت ارتفاعات علی الطاهر مشرف به شهر النبطیه را با گلوله‌های توپخانه و بمب‌های فسفری آماج حملات وحشیانه خود قرار داده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/660595" target="_blank">📅 00:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660594">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58a21e6cec.mp4?token=Sof23oDFZDnFDJ27FN1Mxehmmj6YJK7yWnFtCdOLu4S9BIB3SFCj1XSqGHhPXWmLbaFzRTk3Ty0nP0g3U3hSclncuOJkEGN0SVY8pAAUN6lVAmf0BkxkPKb5A-tlSA2Yi_p4vzsCZdz3SVEvJaW18Q7-cZvXCAR8EDopl_tI2wps8SrPdtNpkDZtQe0hPeBGb06A71mEamxO2hUlV-EuibGyM7FEsAk0rhe-RSWx3_-JTlQMk0WB4k4hBcu5Z_UuckiQFEzcTIHykyPnsbRIM_0ngW9JFvJM7fJPJxiHKKi8UGqo9ZiOp1GgtW5TAEVGtYpyxc8HX0uGXxXrU4kf4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58a21e6cec.mp4?token=Sof23oDFZDnFDJ27FN1Mxehmmj6YJK7yWnFtCdOLu4S9BIB3SFCj1XSqGHhPXWmLbaFzRTk3Ty0nP0g3U3hSclncuOJkEGN0SVY8pAAUN6lVAmf0BkxkPKb5A-tlSA2Yi_p4vzsCZdz3SVEvJaW18Q7-cZvXCAR8EDopl_tI2wps8SrPdtNpkDZtQe0hPeBGb06A71mEamxO2hUlV-EuibGyM7FEsAk0rhe-RSWx3_-JTlQMk0WB4k4hBcu5Z_UuckiQFEzcTIHykyPnsbRIM_0ngW9JFvJM7fJPJxiHKKi8UGqo9ZiOp1GgtW5TAEVGtYpyxc8HX0uGXxXrU4kf4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو وایرال شده از یه ربات انسان نما چینی که کنار خیابونا میشینه و از مردم پولِ کمک جمع میکنه
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/660594" target="_blank">📅 00:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660593">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85d797efbe.mp4?token=h5iAEkgDZXbsJ2diO_3Fj4MTtInhFUx8HjP2gMbxXW3AsKMTQH4qDX_gAGssUSja9ieeq3nL_oLAm2z0Lj1daREcgN8hXQKrWlLzHu1PKPETvK9bqjLpMMI2-49_Crusy2H1YEUm8xtJx6tW7lr0SEAwE0FeXMtF6209rHsVO7n8rXbLfLKETZx8db4oCaMKANyrhTcx_SggmQszRLnMHqwK_AFwYvoRbkcpPvpUcPk3TFZcxbWo4qYwIQvBbYOlCSdMqAIqqsggl5BLiqsBUuUEjUJNEg5fpmdYkXydCPaseVCvglomd-XE5R2CZlsgx-kIzJIAJ2uGfRGeSWtC9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85d797efbe.mp4?token=h5iAEkgDZXbsJ2diO_3Fj4MTtInhFUx8HjP2gMbxXW3AsKMTQH4qDX_gAGssUSja9ieeq3nL_oLAm2z0Lj1daREcgN8hXQKrWlLzHu1PKPETvK9bqjLpMMI2-49_Crusy2H1YEUm8xtJx6tW7lr0SEAwE0FeXMtF6209rHsVO7n8rXbLfLKETZx8db4oCaMKANyrhTcx_SggmQszRLnMHqwK_AFwYvoRbkcpPvpUcPk3TFZcxbWo4qYwIQvBbYOlCSdMqAIqqsggl5BLiqsBUuUEjUJNEg5fpmdYkXydCPaseVCvglomd-XE5R2CZlsgx-kIzJIAJ2uGfRGeSWtC9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: هرجا دشمن به تعهداتی که داده عمل نکند شمشیر ما موجود است و با منطق قدرت به او خواهیم فهماند
🔹
من دیپلمات نیستم اما خوب بلد هستم به آمریکا تفهیم کنم که باید چه کار کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/660593" target="_blank">📅 00:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660592">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
قالیباف: مدیریت تنگه هرمز را براساس قوانین بین‌المللی پیش می‌بریم
🔹
براساس این قوانین ما حق داریم هزینۀ خدمات در تنگه هرمز را دریافت کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/660592" target="_blank">📅 00:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660585">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b75MqjNyKmz7_sx-qJgS1rRIuLroGy61H8yvMA8YomQwDnZ33Cqi-p9fssh5ZM3pUbgmUiUU7ZNjOq4BebaXx0PLWPoEsQ3AVDCJsbSKjmuXbbn2OTBdpVKy6F6VawFEP3e5SW-T006WSNsty9ziGW--TbvjOPmKIrGBXJb5nOd03fWX-_yUvOiY7ODTKDSbAce6CFtRCB-1iYMV5YI3LCCb9EtI8QI-JUc6Lkw5zLJjrN4wCGwKKNJFRwKZYrrI6ae5cg1FW05HB4J3LrojK7U1A72K4tDNv-Ob_OzaBOWNePMTeajmhlVAoijYK2gxeBpVGNu7Hgo9n9l2OX_L9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IaoMGNB9BFuXyjkP_9XDEXD4unWTFOYcAnElkiT0s-uZBCMBjgKBlML5kyz4AwbGVBprG01vhtYsm5U2pjgfPUJpSasNZn3aLntur57Buw3a7B_z1xTaebpny2J109SG4yQfXuNZDPhyBfEG8S3yufVIMvPSqZvw8CJYRXp2JVRbl6dX0ufkNk0XJ4wY5gptZgejl7fA9ejZ8TIqj4X5IiKq4DNVGZoMNOeY_d7GtHFO5cUngX1DslTy8D45bdM4R73nM6IwmLWuADVLiSHfYsdYOrTYeEAtgmSMvWVDXXnRrIQrolmefskIYIqLC1JjtFO_A9w_4eTtQ9y68hyyYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U4TxoNMIFJxNvP_rN1PWJfOA3HuIbtMyzNwRMxrDFFX_Wi01N6NybhXfT__NS1heAA0l4cf7VM2ZIC5pdDtXAUP9v47aS6BZDCsYwFbEAq1oJ4RozB5QkcFVVYr4-6zbWVt2qFRAGVUuYyVGUcIvHgVOKvPL3Vxdg8bv6O6d0_xsCLMzhLq3-fTrh01wHAQZBJtzn-1mmzdgrwJ84_ByH3idr-l44A2trHHXhzTlaNRt6bdu2g1E34lW-X4gcEQptomiid0SttUk90FmF0vsfr8dsjli3M4uLHp4lge36X3WdN3ZLuqvfscccjfWdGNv3GIWcVW0f1Li5Ls1zQ3PjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GnF5RplNBGjev_EXqh55jWOl2zzh4tGNRhCVLvw4Js7_IfcZHCEw3SFDgYaNutXkiQ0QvPyECHrX7eUhhGbd87B1Df6dlScXmzXgF_bAOgjhmJoWC6aRaG4q3raLnlBYUPcf5FUVzIMEKQ-OvTjje79SG9ifuM8HKqym18qhvvCj8puq3mc775jlCcC22cyqX020Kmdx7A2CRp8PKchfMTZzM6Sga6LCfaNleLLEIEEfngt_eSSAZA_inDhcsytDpiKFcQh7AGCvxyT-6k44oNDYAuY_aVZPsUWdeYe9-lgg5YfZ3Z61irQGLvNPElsEqZy9pCgX5-VwVgvLVtDU9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k45Hw89sDYYvPZJ4zFlokw1JRkfQePoYcmomJSfKfq32ouVZcOrr90rMzhp2PoGhsWv5vTUn3e5NpqVlMS2ZDuasvBkLpJlri-2wmrJEvyzlTd4Yrv-wijgKlFrKyax2pOwpXCFi4SmxDtOSiGSHuGEIuc4XVfJetH_yTzkz_DkujLDkFgZ1QKm8ozbJzSb2ct5orVDj20a5YHAoQRckOAGpzVPaXfEriigiAHc41e1uolNOhnk1TaSoH7NVstOok8Gkay54bPJ0bbjcUEe-4iz9T_fJWLcmXbBBKWjbjJnLryLVQKgleR2jgiUSZifTMvSIcGtyOB2MsREExSMcMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SudorTki_IB6JVrWffzuvKT4ztJknQhhDaDGZonFjLHVCrX3sfen2K9gTyQn-lYPXvzVFLf4VPNFuaw1L6Nd9CB2ksd0rmEB-95m7rSVbTDoVz_FKcVvXa-ob_rzcpmPPhttHOY8KnSm-EBYDBIvL4vF-MtVRtsjovPvDPTMRX_WjSqnBClbV8cATEI9lhjxVMNMrzlDIw9Afn89tRNoINuDKkZ2VwalKItAndYYlgjF2-HhDFhaaOSVKQU7oZI4pxE24nFYxAZjXsLFEt8WLJ5KiBWFanq4FqTJeTt0J9AsAGge8udAQIykG9m5_39oZuK8KNipq3yy8bPz1MH0Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QwZyBF0Y88T5VSO60tOjCHVcTud6LYRP9rLcLNfYXC8WZh7O9fJgAzVcGwsDw5jbAcE7taV3NtOWRMBwB_yQiES-gj1wUE-l-SAX7iuTLkQaseqqE1QryskBY3We5p8VlZ1EVSUzVBnc9UvZG00sYoIbdnW7gPIcLEm1Wv5cho2FsnF0llCPsFA5n2NrFSn6rc0lLqeVsdGnrKa8VRiSqidDh4trjExeABGjKy3y_wtQa5NyzbbyfFcUPfwo6KaKH4ePfvaFp9TAAR4Z0zZjjVs7VCxDm5bVa9Flmmtm8uxV-6DWSZf3Kjg5MR2oBCmMldibGDRTXh0vfgdGNJKNOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ویژگی ها و احساساتی که در ابتدای عاشق شدن به وجود میاد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/660585" target="_blank">📅 00:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660584">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2_s0YlZei4sC920G--1hi7tPIAmhGQQFcMkGGgZlHZEpay1ce9soXHR1h3pe5FhzwP5anZJwnzAPYR44oxuBgnLRv5z7SfWx0WB33Dut0-4FV9VJpj161fRlcFn0_wiIPR5TqwSq-RFLn7Kd2skanP7HCVq5pYna1mI6VwvDFmskHSz6hvSgLGJ80rGwbd_Lko8vrmC6ZVe_jSe5cYinh40nIruuQALTgaIbizq4KCe-Z8KZ1RDRFlSSndr7990zXuUob8Fmf5c0p55EevigV3W1UZYESPTONAuaKyl8tX2MHMAXGKyHDPZia-H41jnIWCDHdW6GH-PQC5bdoDyRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/akhbarefori/660584" target="_blank">📅 00:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660583">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تا ده‌ها ساعت تو مسیر بودند تا با اتوبوس و ماشین و شناور به محل کارشون برسند و بعضا تا سه هفته هم امکان برگشت به خونه نداشتند. بدون تعطیلی و بدون استراحت.
این فقط بخشی از جنگ و پشت صحنه‌ی تولید پایدار گاز در پارس جنوبیه...
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/660583" target="_blank">📅 23:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660582">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
قالیباف: بازهم تاکید می‌کنم که تنگه هرمز هرگز به شرایط قبل بازنمی‌گردد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/660582" target="_blank">📅 23:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660581">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
قالیباف: ما دستمان روی ماشه است و اگر دشمن زبان منطق را نفهمد دوباره با زبان قدرت وارد می‌شویم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/660581" target="_blank">📅 23:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660580">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
قالیباف: اکنون براساس تفاهم‌نامه، باید ابتدا بندهای ۴، ۵، ۱۰ و ۱۱ و اکنون تأکید می‌کنم بند ۱ نیز در اولویت اجرا قرار گیرد تا پس از آن وارد سایر بندهای تفاهم‌نامه شویم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/660580" target="_blank">📅 23:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660579">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
قالیباف: قبل از مذاکرات اسلام آباد اعلام کردیم موضوع لبنان و آزادسازی پول های بلوکه شده باید محور مذاکرات باشد
🔹
ما چیزی به عنوان پیش‌شرط نداشتیم، هرچند ممکن است خواسته‌هایی داشته باشیم. البته به میانجی گفته بودیم که بحث آتش‌بس لبنان و آزادسازی پول‌های بلوکه‌شده،…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/660579" target="_blank">📅 23:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660578">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
توضیحات قالیباف در مورد فرآیند مذاکرات اسلام آباد
🔹
طی ۲۴ ساعت ۳ دور مذاکرات با متن و ۳ دور مذاکرات سه جانبه با حضور میانجی برگزار شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/660578" target="_blank">📅 23:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660577">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e223f9d98c.mp4?token=kZzsZA3-bKLZuAhrILV0JoHMeP_aLh0zRg8pJ1zNbZkcxpSfNJWoW6HoiPSTIYeSKj1zWQ9xTyZXWoaT-ZxVIzxtDt43b0goLpInbMZUuSQHvkW9LHqeTSRCGVL1t0XObVoA7docUrtD-JZrk84DkTd5vw8ODzlwvjPrmJI6K0lR8Izg6WQau_Njbw1qzREoszgkyeNSTkkjhIj3-6X4k5QRYR9fjHgXNdA5EYGoJ8BGvVeHr5qqoC0s6_DmnE6L6AZIB7fdo_FAHHFX4NDNYEfNWsfu0noDCOSY5290uI1HKwX7qqGPntyM50-2Wqo7ee_buAKPrsryLvhmMJzO3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e223f9d98c.mp4?token=kZzsZA3-bKLZuAhrILV0JoHMeP_aLh0zRg8pJ1zNbZkcxpSfNJWoW6HoiPSTIYeSKj1zWQ9xTyZXWoaT-ZxVIzxtDt43b0goLpInbMZUuSQHvkW9LHqeTSRCGVL1t0XObVoA7docUrtD-JZrk84DkTd5vw8ODzlwvjPrmJI6K0lR8Izg6WQau_Njbw1qzREoszgkyeNSTkkjhIj3-6X4k5QRYR9fjHgXNdA5EYGoJ8BGvVeHr5qqoC0s6_DmnE6L6AZIB7fdo_FAHHFX4NDNYEfNWsfu0noDCOSY5290uI1HKwX7qqGPntyM50-2Wqo7ee_buAKPrsryLvhmMJzO3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول انگلیس به کرواسی/ هری کین با تکرار پنالتی گل زد
🤩
🤩
🤩
🤩
🤩
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/660577" target="_blank">📅 23:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660576">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
قالیباف: من برای پذیرش حضور در تیم مذاکره‌کننده کراهت داشتم
🔹
من نه تنها داوطلب حضور در تیم مذاکره کننده نبودم بلکه کراهت هم داشتم و قبل از پذیرش مسئولیت مذاکرات من تمام تلاشم را کردم که این مسئولیت به من سپرده نشود.
🔹
یکی از دلایل من برای عدم پذیرش این…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660576" target="_blank">📅 23:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660575">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
قالیباف: در طول جنگ نمایندگان چند کشور اروپایی به ایران آمدند تا از ما خواهش کنند
🔹
همان کشورهای اروپایی که سپاه را در لیست تروریستی گذاشته بودند از مسیرهای زمینی به سختی به ایران آمدند تا با ما صحبت کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/660575" target="_blank">📅 23:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660574">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
قالیباف: مهم‌ترین ضمانت برای تفاهم فقط قدرت ماست وگرنه دشمن قابل‌اعتماد نیست
🔹
ترامپ قطعنامه‌ رسمی سازمان ملل را جلوی چشمان همه پاره کرده پس به هیچ وجه قابل‌اعتماد نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/660574" target="_blank">📅 23:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660573">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
قالیباف: من به‌عنوان خدمت‌گزار مردم به ملت عزیز می‌گویم که پس‌از پایان بحث مذاکرات و امضای تفاهم، اولویت ما میدان خدمت به مردم است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/660573" target="_blank">📅 23:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660567">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UTukM1FsteWwkPdKaezb6U_Kloxfa8vYPianomRpaifnuaWK9bOqCGC-9s9unJ1SuOohJ0Ktuo3D_3wmtnnOrTq3RzWESTEiAL9l0G_fde48dG77LUc-jK0AMOKjz3HN9V2gTsdorXEjUiNpzRvPac_mTXk_pikN7io-XeTUfb3aY-lA9phLvQOYB6bB1QQlt8XRqGn5v9tW1O4QDmh0MlEuuSxIto_paNaX5Fw1_a0O1zcHYuE8tli5Upe0DN5JxIiZ3_In-NkxRxnS5MHY61pHgLrpVw0GOqajsKL9y-7DcUbCgxERHzQrUmS3uEiq_SMRwqPQZRSsjSXLE9uDQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W1wu4fAfLYYXBzaUf6T2bmsyL64lBBgSJp4RI8I8Oy17115K19E_VamI5cJgTMAezg1NRBf_2kMLqlahMVQyT1y3D-osxoQHEiyHw26rBBXDG0ENkd0DiAZcF6-097gxeO-3_uCrU2d2-fkyfVNZqrvrqwZ4mQ63Edtc8DLu5Q9Ejf73NJ_V76VFB5ZfnUgBrBP-AabqPTJtV-r9wGohy4zMRrpBrhHrBKvdJ1O_AiifLG56urP8GIdvxzLYD6goW8RYTOuxGRT3wG5mdm_omxVbhK5ijwgx-ntXFXyNrOPUF2YaN3dzlEe47IJL4BATdKGQBCv3nxiCecmrGns_YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pIgrwNHrsh4s80YuUmNixeUAn-RZ95G3nplKvMwsZhecpQVbnENZf2Ywv4mS76QlEDI86Rsj32LRv0OkvxtiBZpSTPuAyNdcALADuR8-4jGUSzWMgBKtbz1hL50XR3c1PMD8J2kRa0KBTj0yLzV4cs9cYDTkPT4DiRKlv7gacTar-o7xX17Hhjobwd99mZz6_0avnaaZvFlo-E0RoVKYP_sKYHa9mqpDepRpYYOYRzyCAY0WQeA63UPWuX36nHcUtBl0052K9L57Wea-bEScR5BKUPNa2G6KHuVfB9y7NiWY2cJXB0StUqnaZPWaRmPj5c3C9Kz5JkrW4VRRKP3PBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QmipZ0kEIWX10QNmG-ap_JUbUm-J7oseXit8qUzOgt2HMJ102dQBcAkV4se7XMOw5H7qadhBgGAek-nf2lQRBdVMoMCskviA-UyAiuJkbCF7la6t0aIoVlAc3ntOwAfMT5etiA54uAik-_QIPBQoRWBY3TgRB6T0amjH9fRZqoAGpACWijHYSyuagzftJlGG-bNf83iRYW9FTau2d-E0_8ruGZ9ky8Gzgk69e526IVk0EJJb8cS2BxydgRJriD7xRe8S1DyD3bUDTF_Fez7q5reqWvy5upO88iZl9R1ej578uSrjYCXj05dgBVGA4w1_SxQ8XUMoD6wZKkMmRkMwsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TB01v05C2HRGtf-vHc5IriSuJYArOV_rbY7qGMlrwDrZ91VrqVaeKrdQkKlj-5ZDutKCgjns9bfZZCAo7pQVYYjIZAnFnijoZD0EHbrSHPqcD7JoPM8-DQRznEZuAqflBtJIWE7Kkpk9bgEHjUeyl7gwGzbWEvXNdrL_6sd22w51Pz3mWDDeZuTA5GQKGjyACAGqdm7Li4hmsiavDOv8pJwPhbXlJjlqgd5NYrfBH-_dVe819P-7VBTHTuD8fxl8fS3xdpEG-mKVjDKzf3n5MGmwIxMvyw3TdXbpZvVG-pD-Neb2z1jTmxieqUaCgTZ_9_49fNXHuVjAxU4JoeFo2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B6H3mvQKWXseJqo4Q3GGBguBq4ZYdqD4SYroA5QVTp6d4VB0Xssh_R7p6gkK6F0ZtppaoJvGXOxp2DiPZCXKP93lJN04DPAbULHGeqTKb7FUVo2mX6Jm-pUKWwh_U8k2_OaOObkskT2ILFC79mOLJziUDIEXLMuZ0wdMjzZtT4EodnxV1Kxie6nEYQDSTvpN4-REfjuBZE3jIQDYUd1E0qnWDiRWWpT2QGPTp39O6pYqy2CLhUHrkLHtZv7hzJ3lh1dJG5tuZk1BY-3Cw3yY63kE6weBEf6RTOlaXqYh3FrZie5pUt4qkJjTj37ozE32arhX6z4w0UkQ-Eb0IfBaCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ماکان، پسر جاودانه ایران بر شانه‌ی قهرمانان
🔹
همزمان با آغاز رقابت‌های جام جهانی و با حضور تیم ملی فوتبال ایران، پویش «ماکان کجاست؟» بر تابلوهای تبلیغی پایتخت اجرا شده است.
🔹
پویش«ماکان کجاست؟» با شعار «بر شانه قهرمانان ماست» تلاش می‌کند مفهوم قهرمانی را فراتر از میدان نبرد و زمین مسابقه تعریف کند. قهرمان، می‌تواند کودکی باشد که فرصت رسیدن به رویای خود را پیدا نکرد، اما یاد او در خاطر همه قهرمانان ایران است.
سازمان زیباسازی شهر تهران تلاش دارد یاد و نام «ماکان نصیری» و ۱۶۸ دانش آموز مظلوم مینابی را که در پی حمله موشکی رژیم صهیونیستی و آمریکا به مدرسه شجره طیبه به شهادت رسیدند، در حافظه جمعی جامعه زنده نگه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/660567" target="_blank">📅 23:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660566">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
قالیباف: قرار بود آمریکا محاصره را ظرف ۳۰ روز بردارد اما ترامپ گفت همین امشب محاصره را برمی‌داریم
🔹
اگر مذاکره نبود این موضوع اتفاق نمی‌افتاد و اگر موشک نبود حرف‌های من پای میز مذاکره بلوف و خالی‌بندی تلقی می‌شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/660566" target="_blank">📅 23:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660565">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
چرا ایران در روز آخر مذاکره حمله به اراضی اشغالی را متوقف کرد؟   قالیباف:
🔹
ما هر آنچه که می‌خواستیم با حمله بگیریم را چندین برابرش را با مذاکره گرفتیم. ساعت ۲ صبح ترامپ آتش‌بس را در کل لبنان داد و با آن ادبیات با نتانیاهو صحبت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/660565" target="_blank">📅 23:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660564">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
قالیباف: فرق مذاکرات الان با دوره‌های قبل در این است که امروز علمِ پیروزیِ میدان، پشتوانه مذاکرات است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/660564" target="_blank">📅 23:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660563">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
قالیباف: وقتی خواستیم در جواب حمله به ضاحیه به اراضی اشغالی موشک بزنیم طرف مقابل گفت که نزنید، ما گفتیم حتما می‌زنیم و اگر پاسخ بدهید منطقه را می‌زنیم؛ این فرهنگ غالب بر مذاکرهٔ ما بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/660563" target="_blank">📅 23:22 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
