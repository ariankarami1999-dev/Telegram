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
<img src="https://cdn4.telesco.pe/file/gIvpIJSgRxlr4ykGs00TtXAsW1GhjgP6xMHa4fJtbnqSsp56i5Et-UUtdU_d_3qSvRNazznWT58l2E1ruXm39NuqbJH0nGB6iMsS8gDnABBsYi8JyabwAfYvL4sDAU-_QuHYo8Yzu3w0MZcAAqK8QYq7qRGwJqU1N8W9B4PZUnzor99k25OBzNtLVxFNdNm54esQmFgNNy3Cm6vHBO18V1c8UINDmgOzKI1IuJ4qBWX4IE9rRSmCtO1RNYqC8QbcVf4CTMGtM2tlg1EZeyg5IEdDu-Kcih6svojlkpoE_SEuTzLuZ1IXCEn_WepAB7gf1Qh9JTQrAtEe3bukyMC_hQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 02:49:00</div>
<hr>

<div class="tg-post" id="msg-20290">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">شلیک های متعدد در تنگه هرمز!</div>
<div class="tg-footer">👁️ 541 · <a href="https://t.me/SBoxxx/20290" target="_blank">📅 02:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20289">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFpytBOGdSrNVW8kZ1WRo1KivSekL1ztsuhJkHC25i1y1qC8a5g6UY06gWdr319E5uik2bst3zRtPmXDWY2ntnndbS7Z9Dtj4w7A9T7VYRQm7_-gqJ85ASOihO_RKLyZMZNOEJVjqXlYXiVXMLz306p7_g2Cp8u_ZOT2aAgs8BPwnDbPpEpyEcQ1ZXZW-wYnt-bo_cQtLU1S5jrG0dIVcr4AISI6oD2cjJ7wnr7S5eNpufV0O6PGX-M7w5lNAAvRuarrQEcCAD0oNsur6SWBV5mOcyp1_3051W_PbyMCYhoJraQYYCPggGkWuTNFdH_Afg9Qa0cbafg8lf0vHgzmZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحول در پدافند لیزری اسرائیل  و تغییر احتمالی معادله بازدارندگی ایران
گزارش اخیر درباره پیشرفت‌های شرکت البیت اسرائیل در توسعه سامانه‌های لیزری، صرفاً یک خبر فناورانه نیست؛ بلکه می‌تواند نشانه‌ای از آغاز یک تحول راهبردی در موازنه نظامی خاورمیانه باشد. سامانه پدافندی پرتو آهنین  Iron Beam تاکنون توانایی خود را در مقابله با پهپادها و برخی تهدیدات هوایی به نمایش گذاشته و اکنون مهندسان اسرائیلی آشکارا از چشم‌انداز گسترش این فناوری به حوزه رهگیری موشک‌های بالستیک سخن می‌گویند. اگر این هدف محقق شود، ایران با یکی از جدی‌ترین چالش‌های راهبردی تاریخ معاصر خود روبه‌رو خواهد شد.
اساس قدرت بازدارندگی متعارف ایران در دهه‌های اخیر بر زرادخانه گسترده موشک‌های بالستیک و کروز بنا شده است. تهران به دلیل محدودیت‌های ناشی از تحریم‌ها و برتری هوایی رقبای منطقه‌ای، سرمایه‌گذاری عظیمی روی توسعه موشک‌های دوربرد انجام داده است. این موشک‌ها نه‌تنها ابزار حمله، بلکه ستون اصلی بازدارندگی ایران محسوب می‌شوند. در واقع بخش مهمی از محاسبات امنیتی ایران بر این فرض استوار است که در صورت وقوع جنگ، حجم بالای شلیک موشک‌ها می‌تواند سامانه‌های دفاعی دشمن را اشباع کند.
اما فناوری لیزری دقیقاً همین منطق را هدف قرار می‌دهد. تفاوت اساسی میان رهگیرهای موشکی متعارف و لیزر در هزینه و ظرفیت درگیری است. هر موشک رهگیر سامانه‌هایی مانند پیکان Arrow یا فلاخن داوود David's Sling ده‌ها هزار تا چند میلیون دلار هزینه دارد، در حالی که هزینه هر شلیک لیزری در مقایسه بسیار ناچیز است. به همین دلیل، اگر اسرائیل بتواند لیزرهای پرقدرت را برای مقابله با موشک‌های بالستیک عملیاتی کند، دیگر مجبور نخواهد بود برای هر تهدید از یک رهگیر گران‌قیمت استفاده کند.
اهمیت بیشتر این تحول در پروژه لیزرهای هوابرد نهفته است. برخلاف سامانه‌های زمینی که با محدودیت افق راداری و شرایط جوی مواجه‌اند، لیزرهای نصب‌شده روی جنگنده‌ها یا هواپیماهای ویژه می‌توانند در ارتفاع بالا به موشک‌های مهاجم نزدیک شوند و آنها را در مراحل اولیه پرواز هدف قرار دهند. چنین قابلیتی زمان واکنش را افزایش داده و احتمال موفقیت دفاع را بالا می‌برد.
البته هنوز موانع فنی مهمی وجود دارد و هیچ تضمینی نیست که رهگیری موشک‌های بالستیک با لیزر در آینده نزدیک به واقعیت تبدیل شود. اما اگر اسرائیل از مرحله مقابله با پهپادها و موشک‌های کروز عبور کرده و به رهگیری مؤثر موشک‌های بالستیک برسد، بخش بزرگی از مزیت راهبردی ایران زیر سؤال خواهد رفت. در آن سناریو، تهران ناچار خواهد شد برای حفظ بازدارندگی خود به دنبال راهکارهای جدیدی باشد، زیرا ستون اصلی قدرت متعارفش دیگر همان کارایی گذشته را نخواهد داشت. به همین دلیل، موفقیت احتمالی دفاع لیزری علیه موشک‌های بالستیک را می‌توان یکی از معدود تحولاتی دانست که قادر است معادله بازدارندگی میان ایران و اسرائیل را به‌طور بنیادین تغییر دهد.</div>
<div class="tg-footer">👁️ 540 · <a href="https://t.me/SBoxxx/20289" target="_blank">📅 02:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20288">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">منابع اطلاعاتی سعودی اعلام کردند تا ساعات آینده، گروه های مقاومت عراقی به عربستان حمله می‌کنند.</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/SBoxxx/20288" target="_blank">📅 02:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20287">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خلاصه
یادداشت الجزیره | تحریم‌های جدید آمریکا؛ تلاش برای خفه‌کردن شبکه اقتصادی ایران، بدون ورود به جنگ مالی با چین
موج جدید تحریم‌های دولت ترامپ علیه ایران را باید فراتر از یک بسته تحریمی معمولی دید. وزارت خزانه‌داری آمریکا نزدیک به ۶۰ فرد و نهاد در ایران و چندین کشور دیگر را هدف قرار داده و تلاش کرده است شبکه‌ای را که به تهران امکان
فروش نفت، انتقال پول، خرید فناوری و تجهیزات، حمل‌ونقل و دور زدن تحریم‌ها
را می‌دهد، همزمان تحت فشار قرار دهد. اسکات بسنت، وزیر خزانه‌داری آمریکا، این عملیات را بخشی از راهبرد «خفه‌سازی اقتصادی» ایران توصیف کرده است.
نکته مهم این تحریم‌ها،
ماهیت شبکه‌ای آنها
است. آمریکا به جای تمرکز صرف بر شرکت‌های ایرانی، واسطه‌های خرید در چین و هنگ‌کنگ، شرکت‌های لجستیکی، کشتیرانی، شبکه‌های موسوم به «بانکداری سایه»، شرکت‌های مرتبط با تجارت نفت و حتی برخی فعالان ناوگان سایه ایران را هدف قرار داده است. این شبکه اکنون از ایران تا چین، هنگ‌کنگ، سنگاپور، امارات، سوئیس، مالزی، بریتانیا، فرانسه، یونان و چند کشور دیگر امتداد دارد.
هدف اصلی واشنگتن، افزایش هزینه هر مرحله از تجارت خارجی ایران است؛ به‌گونه‌ای که فروش نفت، انتقال درآمد، خرید تجهیزات و جابه‌جایی کالا برای تهران دشوارتر و پرهزینه‌تر شود. به‌خصوص شبکه‌های خرید فناوری دوکاربردی مورد توجه قرار گرفته‌اند؛ شبکه‌هایی که به ادعای آمریکا از شرکت‌های پوششی و واسطه‌های شرق آسیا برای پنهان کردن مصرف‌کننده نهایی تجهیزات استفاده می‌کنند.
اما
بزرگ‌ترین نقطه ضعف این استراتژی چین است.
آمریکا چند شرکت چینی و هنگ‌کنگی را تحریم کرده، اما از هدف قرار دادن بانک‌های بزرگ چینی که در تجارت نفت ایران نقش دارند، خودداری کرده است. این تصمیم اتفاقی نیست. چین بزرگ‌ترین خریدار نفت ایران است و اعمال تحریم‌های ثانویه علیه بانک‌های بزرگ این کشور می‌تواند پرونده ایران را به یک بحران مستقیم مالی میان واشنگتن و پکن تبدیل کند. بسنت نیز صراحتاً گفته است که نمی‌خواهد با این اقدامات «سیستم مالی جهانی را منفجر کند»
بنابراین،
مرحله بعدی تحریم‌ها تعیین‌کننده خواهد بود
: اگر آمریکا به سراغ بانک‌ها، پالایشگاه‌ها و خریداران بزرگ چینی برود، فشار بر ایران می‌تواند جهشی شود؛ اما همزمان خطر تقابل اقتصادی با چین نیز افزایش می‌یابد. اگر واشنگتن از این مرحله عقب‌نشینی کند، ایران همچنان می‌تواند بخش مهمی از نفت خود را از طریق شبکه‌های واسطه‌ای به چین بفروشد؛ البته با تخفیف بیشتر، هزینه انتقال بالاتر و درآمد ارزی کمتر.
در واقع، این بسته تحریمی نشان می‌دهد آمریکا تلاش دارد
تمام شریان‌های اقتصادی ایران را باریک کند، اما هنوز از قطع مهم‌ترین شریان ــ چین ــ پرهیز دارد.
همین مسئله احتمالاً سقف واقعی کارزار فشار اقتصادی جدید علیه تهران را تعیین خواهد کرد.</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/SBoxxx/20287" target="_blank">📅 01:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20286">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-text">البزشکیان:
من میخواستم مردم بیان تو صحنه
و اصلا ریاست جمهوری تخمم نبود.
ولی حالا خودم اومدم تو صحنه
و مردم به تخمشون نیست.
@Piknikanalyst</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/20286" target="_blank">📅 23:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20285">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پزشکیان:
اگر تحریم ادامه پیدا کند، گرانی افزایش می‌یابد</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/20285" target="_blank">📅 23:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20284">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا دقایقی پیش از اعمال تحریم‌های جدید علیه ایران خبر داد.</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/20284" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20283">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlRyhQ8qPlAhpsXnfh32TYNl9mqRVtrnTxTJloSU1ABv672ErjBxgB3sDdAtDvXl4w3KifEewOWDuKjWW-_X3qaNs6MIGyEIENGcu5W-tWt7Q4_O5QzUKp-0vQi1pQUHXFVmJOAhkEIJACQm8VWCd7RZC28ZdA_jvUPZxJ-5R2m8tngCPIdTNDW2At1EUQGVPK2speANTns2h2-9bXHrVLRhYUZV3cZ3xg6vDj1KyEqPrAxl-GPu2aL1zyo1RmInsFLnkWb2TIBvW_EEU54EIhfHo3XWvXdGkeurgPYlROU77B56YpxbNtDPX0l7u04pFnncC37prZFlZV1RESZT3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح نسبتاً بالایی است و با این وضعیت انتظار می رود طلا موفق به ثبت سقف جدید نشود.  به نظرم بالای 4630 فروش دارد.</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/20283" target="_blank">📅 17:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20282">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح نسبتاً بالایی است و با این وضعیت انتظار می رود طلا موفق به ثبت سقف جدید نشود.  به نظرم بالای 4630 فروش دارد.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/20282" target="_blank">📅 17:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20281">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ:  دیگر انتظار خوش رفتاری از من نداشته باشید!</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20281" target="_blank">📅 16:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20279">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWyp71lCl3uvKu2U4b4rMZ_8JAmb__Z6SeUHvBpooiczxMqQ2nmT40ueJPpZSJKe_O_8sQ6_0vih_E9PigJmAy4RwlVOpTf_NRJhpRXVxbMZ1UqhKYHtoMbZ66xv1FAdXmoqfoj1ZhJs_mML_JTNh2PI8FNR4h15zUNZJ5Bsn-1Qr3c6MF7vFffAwm1ZmFTVxCtuEieigT4Smrp8j_z_yCqxBt7QMqahAE5Ia2bPYbSz5d20OlO-6587ebuu9QGARFI-TDZQpZbE2l2njgwAEC2DTi7XfESc0EBQn_E3Q6_v0AoTXf9_WZ1UqF3SYbVD9xV8sgxB80HV5BK-XG_FeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
دیگر انتظار خوش رفتاری از من نداشته باشید!</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20279" target="_blank">📅 16:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20278">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-CgF_qCnC3mmqs-dbIm8tSaAS98YTDiWY7mK1eH7DmNyUdUzT6jGXTkRRTKkCK-YBVfBliwQ6zcSyh6OtvoBTVxHSGc4R8PRNVnm7JmtsN4G2Wc6S7at6sOhHWUqRZo60Hqmaq5NlA_sP36VYBybWTBIXBKXUXgG2vLDd-kYXmcYn8IY3Uoup6mJhLMgZHqLpMU6ijbGUJCAvxMkvl_tbIPDdMcqRwYIFm4_vRW8JZdX9j65ciScm5Y4sPzD0CsVVZrPn2i8QX9cISk2X1d6fZiQGixw9jH8WqU9O7hg1QW41boDXp_peRsSwtf-87cFtJlGvPJm-yMcsHp4uLL3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس
:
آمریکا در نبرد تنگه هرمز، دست بالاتر را دارد.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20278" target="_blank">📅 14:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20277">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICivBsEnXaiu0N_8CpXgOcFG8GRLOr0Ra9mxsfCICYCxLDGsOtRXyXFXOA5pNZ78IXGiyEQhQIReVWonilCkHlpItTGqhM61FYdufVn8cq6DGc0b0RZA0VnbyEQoVG5lrUbtoEXeXwY6TopeUb2K1tBruyoiOBX4DcOfgxVYs41FebRvS1gbifGD4Pto0rr33v7VxPv6tMqCqopmzm4Fgrkajo8grQ9Ryarx2SzBHhPU9hrH2_dipxypTt3fzlrQUFCUE1SsOP983KLD-sDekK-qLjUPT9gydV1SN-T_bWRRcSNxdW110PdBKiYbpFL0vuxfvp6_gP0bKJ4AtBztNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/20277" target="_blank">📅 12:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20276">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pd0S7Rr3aV4FuQJppTZg0m4uIHnlo7n77VDXjRRlzcyv5tIE06a-J5Qenj-XPOuT9yriosgDu7dLbujc-O8zN-TfWymk_6tIYAJ18yZ5Un-j2z9KcDp1iaq9NkMVyOUb5BbY6L17qyZxBcy3KcPu5zHOQ_snkz8qS816dDETCg27AoXngrogpZPD01VxS1EItH-naq0r5HQ6SRbGf9oPIgBffYl0J-INBo10QJSMfhOyJfeGSO0lCPoe92IHLWKGbCDrJn8RqjcV5t5QFiMZkkk-Q9NQuvZLzjLiB_JU4T-PgBr2gLboFKiDJfrl54R5SzXus0kLYXVRfIbIrDanPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح نسبتاً بالایی است و با این وضعیت انتظار می رود طلا موفق به ثبت سقف جدید نشود.
به نظرم بالای 4630 فروش دارد.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20276" target="_blank">📅 12:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20275">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">این بار هم ۳۰۰ پیپ دیگر</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20275" target="_blank">📅 10:28 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20274">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">عزیزی، رئیس کمیسیون امنیت ملی مجلس:
هیچ کشتی‌ای بدون اجازه نیروهای مسلح از تنگه هرمز عبور نمی‌کند</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20274" target="_blank">📅 10:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20273">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حملات توپخانه‌ای اسرائیل به حومه دمشق</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20273" target="_blank">📅 00:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20272">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یورش پلیس آمریکا به خانه پسر ایلهان عمر  ️روزنامه دیلی میل که این خبر را پوشش داده، نوشت که پلیس شهر مینیاپولیس واقع در ایالت مینه‌سوتا به «آلفا نیوز» گفته که سه‌شنبه حکم تفتیش خانه عدنان، پسر ایلهان عمر، اجرا شده و در جریان این بازرسی، اسلحه و مهمات از خانه…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20272" target="_blank">📅 00:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20270">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بد نیست بدانید ایلهان عمر یک نکبت اخوانی است که اساساً به صورت نیمه غیرقانونی در آمریکا شهروندی گرفته و اساساً زادگاهش سومالی است؛ یعنی کشوری که دقیق ترین تعریف «دولت فرومانده» Failed State را دارد.  عًمَر همچنین یکی از سگ های وفادار به اردوغان است.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20270" target="_blank">📅 00:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20269">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی:
اگر محاصره ادامه پیدا کند، صد درصد ما منافع اقتصادی آمریکا در منطقه را با موشک هدف قرار خواهیم داد.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20269" target="_blank">📅 23:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20268">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حملات گسترده ارتش اسراییل به جنوب لبنان</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20268" target="_blank">📅 23:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20267">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پزشکیان
:
اگر وحدت و انسجام در کشور نبود، قطعاً ما خیلی جلوتر از این از هم پاشیده بودیم</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20267" target="_blank">📅 22:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20266">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AM6kBoJIxQjaYDqF-ewMGcXY2i9Lw5MYH-0qefu0esXK1cqy0W0HnJU0ZN22WM92v79honeCAH-2Hhqcvr0xu3UW72WfNT6LGZCxXvLfbXVOdm8mCeTrKYo-9vKlOSrU0SiqR2zjwuxyou8Y2OFQRmZKMQSqR3UVI_Sg0Os-BGYmds2OlW3G0XVg_KRi8S-D7zHywMidVQAb4yO7t3gdYReqlXNgWwl9WJeta2yEjWPCmy-9XE6-aHPVmB-IyCpsXdtfLczaayJ6J-SMgOQF5Q97gUlYk8KCxrtxJhnxNY6zJilg_jQYzXJtr1oPXCWHPSa_b96x1C69QAfKf9CLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازگشت به تفاهمنامه مخالفت کرد!  کاخ سفید، درخواست بازگشت به مفاد یادداشت تفاهم ژوئن با ایران را  با مخالفت ترامپ رد کرده است، که این امر تلاش‌های دیپلماتیک این هفته برای از سرگیری مذاکرات را پیچیده‌تر کرده است.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20266" target="_blank">📅 22:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20265">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ:   کاری که ما در مورد ایران انجام می‌دهیم به این معنی نیست که جنبه نظامی را کنار گذاشته‌ایم   نمی‌خواهیم با ایران صحبت کنیم و به دنبال ملاقات با آنها نیستیم!</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20265" target="_blank">📅 21:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20264">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ:   احتمالاً بانک‌های چینی به فهرست تحریم‌هایی که علیه ایران اعمال شده، اضافه خواهند شد.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20264" target="_blank">📅 21:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20263">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خلاصه مقاله آسوشیتدپرس که دقیقاً تاییدی بر دیدگاه ارائه شده است:   ضعف اصلی استراتژی جدید تحریم‌های آمریکا علیه ایران، نه خود ایران، بلکه چین است.  واشنگتن می‌تواند شرکت‌های ایرانی، شبکه‌های کشتیرانی، واسطه‌های مالی، شرکت‌های هنگ‌کنگی و حتی برخی شرکت‌های چینی…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20263" target="_blank">📅 21:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20262">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حملات گسترده ارتش اسراییل به جنوب لبنان</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20262" target="_blank">📅 20:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20261">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خبر بسیار مهم اینکه این اسوه تقوا و هنر نیز به کشور بازگشت و به همین دلیل قیمت تریاک در ۱ ساعت حدود ۴۰ درصد رشد کرد.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/20261" target="_blank">📅 20:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20260">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWr0SDFGiVYuDW3ub0_5k_M8hPrrTbIvzik8DufqDWpfPRgzJvJUgYSdaCKuyYdmGAtypRiQXv4Mubxd6ufqDVmiQuW1PT7edkZParylQsCqub9OU7byW6RhPP4qSh_07vOp2F1taIpP3-cSYiLEy20txvIGCwAxFkyOT8TxWuNRtW-LUnaxQZOApcKa4zZHFoj9rzSNHTka5cYD4ExLVG-gWgq4hwW5XHIcvZJh3Y7TgL-apB3_GNHpP6egd-kiPUTrGNX91PwYtPL3t4_6BXfu4-CWX288hyVr1KRIZFtVjdABjPA02CjRaq0bm5DrArPbuspffXQDG2JdKdf_VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر بسیار مهم اینکه این اسوه تقوا و هنر نیز به کشور بازگشت و به همین دلیل قیمت تریاک در ۱ ساعت حدود ۴۰ درصد رشد کرد.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20260" target="_blank">📅 19:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20259">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">باید بگویم خیلی خوشحالم که عمانی هم نیستم!  از یک طرف ترامپ می گوید آنها را بمباران خواهدکرد از یک طرف دیگر ایران می گوید که باید مسیر جنوبی را ببندد که البته خودش هم می گوید بدون نیاز به مجوز عمانی ها هم این کار را خودش کرده!</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/20259" target="_blank">📅 19:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20258">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ایران می‌گوید با وجود محاصره آمریکا، همچنان به فروش نفت خود ادامه می‌دهد.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/20258" target="_blank">📅 19:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20257">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ایران می‌گوید با وجود محاصره آمریکا، همچنان به فروش نفت خود ادامه می‌دهد.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20257" target="_blank">📅 19:38 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20256">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یک دور از 4570 حدود ۳۰۰ پیپ داد  دور‌ بعدی احتمالا محدوده ها را ببیند</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20256" target="_blank">📅 18:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20255">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">محدوده های خوب خرید طلا برای امروز  شاید به این محدوده ها نرسد لذا توصیه می شود به صورت پله ای زیر 4580 خرید بشود و در خود سطوح افزایش حجم داشته باشیم.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20255" target="_blank">📅 17:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20254">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حملات گسترده ارتش اسراییل به جنوب لبنان</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20254" target="_blank">📅 16:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20253">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سخنگوی کاخ سفید:
در حال حاضر هیچ مذاکره‌ای با ایران در جریان نیست</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20253" target="_blank">📅 16:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20252">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دقیقاً 20 روز از این داستان نمی گذرد و بحث حمله نظامی روسیه به انگلیس دارد قوت می گیرد!</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20252" target="_blank">📅 16:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20251">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انگار یک دستمال سفید را دور اسکاچ سیمی بپیچید!</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/20251" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20250">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خالد شیخ محمد، که به دست داشتن در حملات یازده سپتامبر متهم است، قرار است در تاریخ ۵ ژوئن ۲۰۲۸ در پایگاه گوانتانامو به همراه سه نفر دیگر که همدست او تلقی می‌شوند، محاکمه شود.  این تروریست که در سال ۲۰۰۳ در پاکستان دستگیر شد، از سال ۲۰۰۶ در گوانتانامو نگهداری…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/20250" target="_blank">📅 13:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20249">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7OIlozkM7kFUzZ4A_rXhBa1e4tmEpMfSTAjOQUgBifgNSIjqQdGqDHwKqrYUleUUvqIycNTg8dY8GIUkrWEKS2bcvipANTRY-bT3U31kYbZe5mUqB-7082cvXCYCQbslqKF_4UB9tPYFsK-VqG5a-69KOJGldAXKRjOGnCh-MuNclMXcm4J5dv7nVLrjZihAr40tz2c-DnXEZvYZAmKoKocoRgjBmanVHgA6UJDtqkvTng2zpExzGtkLC_l-i_btfBVOApVYhHslOn0wtYwRL-p3AFN6kxnQP7A6s57oeYdrsNdX08wVY-UwgHqZq7DuCsYI1OlaLt5lIwKaup0Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خالد شیخ محمد، که به دست داشتن در حملات یازده سپتامبر متهم است، قرار است در تاریخ ۵ ژوئن ۲۰۲۸ در پایگاه گوانتانامو به همراه سه نفر دیگر که همدست او تلقی می‌شوند، محاکمه شود.
این تروریست که در سال ۲۰۰۳ در پاکستان دستگیر شد، از سال ۲۰۰۶ در گوانتانامو نگهداری می‌شود.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20249" target="_blank">📅 13:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20248">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lI2N7vahHZvP1awzGWHJNBrppJ4pIMoSHeXt1A_bVwqUZAIKfOajkVZ9_-Z8RvAo31aJUO9FkEhMN9vqaAIRe2d9NOw1CgKr35kcXYMtVKvsvzvJbgmeCP6LXeaw5iwEQXu_U2d0QNiRNdiYDG4ZSqugf-Lxp7mrn5p0HffZ4hHoj9uQSEN15-9YKlxFaMnORDesPpElTC9VLv1ygen8e7lENhj4l7OeQfPngaxo1tn2nBOWzUPPpVvs1yZtbH5SEZo0uhRfV28StqzJz-Ut0UyINxUjZDKBrymqPDOJQaTn8j4HdUi8_JpQOJ3_V5oKosCtQqIcbF8YqhCcwuVZjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح نسبتاً پایینی قرار داد و پیش بینی می شود طلا یک کف سازی انجام داده و رشد خوبی پس از آن داشته باشد.  خرید در حمایت ها شدیداً توصیه می شود.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/20248" target="_blank">📅 13:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20247">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfNZbi8GNFYLn9dkvByIjhkhUJVdgsduAsz67fBLwHjsjLCTdtuhoARsw7tkFXIU2Bm6EOMnMz8AG_s0oL9QJHtUnFB76yvlzjJTt1MC6pfErQhUQubph9eBuKMZu0mclm8lLNx-A-kSdlQRxJtdWHnSKNio9M3MMqkH-iJetM4RRVGlC58MLNkkVWyUDLf1i5fIiA0fxrirt1ICi98vdBzJmAVJazJadw2lR_BGpZLf4AGEDFyuyyxEjXTfRUAM3wUtbdX859ZeCfZTpqhbU2o9RXl4YIIhf7BbrVkxw8Z8vG1eHFa1C-ADHXMVYEHNZxW8e3dk0YWdyHN6ku2RrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح نسبتاً پایینی قرار داد و پیش بینی می شود طلا یک کف سازی انجام داده و رشد خوبی پس از آن داشته باشد.
خرید در حمایت ها شدیداً توصیه می شود.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20247" target="_blank">📅 11:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20245">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KkQZHZIquPXTxdOtnc3nTbOg9RoO9ZkjE3zdZH4NhdQlqN0U90gIObjwR9MTGAxZylO2c3kBTjg1mGzAc0IL6zqVkPn0iLoVKFDK6ST8cNAiRTV027p2NxZQvUzQtxJJ8m6rhfLmvC_j6ZiZMGzEUryBxmkUt64NV6di-ZwIu8CdXxHJfNgXNxUsEO2UAY_rMyWucws2qKYRWicpIiwJn5uQtL7zsHLWHsittvVdrWmE-YZBIe756xPxAnNpoYgGJ8ikD9sW0x_kpnLpFm9s4ilWEMe3Uq5ShL66mfJ3pGrQayyoz9SKLZ2k9MbbW0aKV3iEnSKRVIhBrbYnf5dnRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GSv64GsD1WS8OkmeXtYpNR9EXBtsBbkAT5eKfLWTKKM6D0TPB7D3RGcmE-Q4HaWPBw0Wn6NJEhWT9Sv9eTN5ijJSM31K6sDf2Pc45MAT9SxklWK6byu9f2qbR9-D5A_hIX2ABZrImm0on0tfOr6AzChO70di2uXgXBiHqgGMeS034Y2fQb3UGEberXL-HGjLSjf4_6pb-lQhId4icEolxP4l_0rs43ysCFhQtl9HyHR27pftGHBRKZspITYnnTRu2Kzrnd-nqS0Vhvb2HGkfLsy2mvmDxvI-a6oEcxPpbKFTCFqE1kQ2RWQIa09gi-1rCg185AUF9Xtb1S72xk7oIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و فشار فروش روی دارایی های ریسکی و احتمالاً طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20245" target="_blank">📅 11:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20244">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f65ff1052.mp4?token=Y3bSNHpLqOGaQ20M98ChXlJ6PtYThm4uxQqFrrkDxH10ZKs7CepEmc8kKFVBvAqoRVOjESSj362o4_tvntCjZ2opWTDd2dGP5lLuZqxdUw2KXMjcHlmSuLZprOo5MywFVMjjG444iMx4taloDKdQijJCG71WYf6Ad9V7opdNDo2RYAMcDsRLmCKrXmrFQb82xPjcnmoa2dQeybpOCDD2tt2nnmkrZXCSWwJMDU9jB8zCCaIxeiD3LsKUb1J2JVY8p_JpDQKUocXwv1eL2g5ZVg2MlGZH8TZ9efIwkq71E8-Vmj26QhX1PbporUOe1kfYs1rHiptiD-9acY9pPBtf6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f65ff1052.mp4?token=Y3bSNHpLqOGaQ20M98ChXlJ6PtYThm4uxQqFrrkDxH10ZKs7CepEmc8kKFVBvAqoRVOjESSj362o4_tvntCjZ2opWTDd2dGP5lLuZqxdUw2KXMjcHlmSuLZprOo5MywFVMjjG444iMx4taloDKdQijJCG71WYf6Ad9V7opdNDo2RYAMcDsRLmCKrXmrFQb82xPjcnmoa2dQeybpOCDD2tt2nnmkrZXCSWwJMDU9jB8zCCaIxeiD3LsKUb1J2JVY8p_JpDQKUocXwv1eL2g5ZVg2MlGZH8TZ9efIwkq71E8-Vmj26QhX1PbporUOe1kfYs1rHiptiD-9acY9pPBtf6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیخود نیست صنعا را پاریس خواهرمیانه می نامند!
ناموسا این ویدیو را ببینید! پلیس های ریقوی یمنی دارند مردمی را که هر کدامشان یک کلاشنیکوف بر دوش دارند «بازرسی» می‌کنند!
به خود تفنگ شان هم‌ کاری ندارند و اصلا مشخص نیست هدف بازرسی چیست؟!
شاید فقط دنبال بمب می‌گردند چون میدانند اگر فرد مسلحی بخواهد با این جماعت درگیر بشود که ظرف ۱۰ ثانیه به گوشت چرخ کرده تبدیل خواهدشد</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20244" target="_blank">📅 00:36 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20243">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">به نظر می‌رسد داریم به لحظات ملکوتی وطی دبر حافظه تاریخی با علی آقا کریمی نزدیک می شویم!</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20243" target="_blank">📅 22:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20242">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">به نظر می‌رسد داریم به لحظات ملکوتی وطی دبر حافظه تاریخی با علی آقا کریمی نزدیک می شویم!</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20242" target="_blank">📅 22:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20241">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">قالیباف:   رابطهٔ راهبردی ایران و چین به اجازه هیچکس نیازی ندارد</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20241" target="_blank">📅 22:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20240">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTfvY0CV6o6Q2O0iVOxUHSYRIlg_ocID8guOPqG1m2uVm6_xIHo9l5mceU8nhYhskInQylyOjBBpG0RfNCQRx_gmty_c1E94W4DFuwgEJfr4sBnR7he-w80wtGXNN0ASv78ORY2HgWy8xmlwIdMvXWi_2p_gM0ErP9yhHsY_D5SgE8iLwj51Y8qcYijEmdoChkrvrMoNAKENdxkxnR93fm1eY588-IK-_Dihs7N0faPq0slbOrke22ucFXkfZZX4PmuRmtx1yXsHiqbTfIqtXobArdOVCVENzk_RSfadLrnPqw87wSpJYkqUIz7TcrbVPt5JUjGEEccSZmVA09_m9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفتگو با الجزیره گفته که برای گفتگو با ایران شتابی ندارد!</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20240" target="_blank">📅 21:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20239">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">در دنیای فاینانس میگویند همه تخم مرغ هایتان را در یک سبد نگذارید!  به عبارت منابع درآمدی و دارایی تان را گونه گون سازی کنید (Diversification ) تا اگر یک منبع تهدید شد، منابع دیگری باشد که جایگزین بشوند.  حالا حکایت ما را ببینید که در سال‌های اخیر چطور به چین…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20239" target="_blank">📅 21:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20238">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20238" target="_blank">📅 21:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20237">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یک نفتکش هندی هنگام عبور از تنگه هرمز توقیف شد.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20237" target="_blank">📅 21:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20236">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPgCRaEl8eeMkTxUF7ZhDQEsi3IWz9X7kjUBcPu45hYgt00AVA4gAeFg6kQGZf22yy85ftIpvDnvTNrVA3YIxn8phCmb7o6t1Gg4dwPQ8Olp6iWnMltVXoA4imfLNkpmMKLtu8T6ieRO8Z3cehZ47L3Ov6u3sgFtyBtmThciZdkYR5zVDK8OZ1jDpN_7MWUyb0zrmsCpgoLK1MzcKNlyDtmbkuj7R28uvkLR_ppGTyOyDAuUiLhGXbELz0t4tPyumZb0X3h33yzMHSQ3JzjoroCSuArPGw_e-j_sebGwhLmOhQg_5iFv6CaG5jjBuZPBVsmqvGZBAymLt3GVOUHT7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواننده Secret Box از 18 ماه پیش می داند که چین
«تا جایی که می تواند از اقتصاد و حاکمیت ایران حمایت خواهدکرد»
و البته از
خطر و ریسک این All-in کردن به اتکای چینی ها
هم آگاه است و متوجه است که به محض اینکه آمریکا یک امتیاز اساسی به چین بدهد، ر
وسیه و ایران هر دو
در موقعیت بشدت ضعیفی قرار خواهندگرفت.
اقدامات احتمالی ایران و پیآمدهای آنها را هم دقیقاً
1 سال پیش در یک نشست لایو اینستاگرامی
مطرح کرده بودیم که اغلبشان تا کنون محقق شده اند.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20236" target="_blank">📅 19:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20235">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خلاصه مقاله آسوشیتدپرس که دقیقاً تاییدی بر دیدگاه ارائه شده است:   ضعف اصلی استراتژی جدید تحریم‌های آمریکا علیه ایران، نه خود ایران، بلکه چین است.  واشنگتن می‌تواند شرکت‌های ایرانی، شبکه‌های کشتیرانی، واسطه‌های مالی، شرکت‌های هنگ‌کنگی و حتی برخی شرکت‌های چینی…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20235" target="_blank">📅 19:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20234">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEzURlOVij6qNZWKXI9rNRrwSMjU0PWj0mA0J5-rJw_mlZx6eYoL4txrGxHZdtKi1VwJNhTS34qFqUufWPJ-uDj0HXxLs2WYBLYWIcOSkRU8myRk-Sf7Pe_jPVSE-fngRaLdDiNpq49NhDJULpJM3XClJMbBow2y5k7nIE828oi7KSLSDZLMlyBg_l8Xvw8vrYQ0bR6IWYnsNaSB6_pm-SvW58WWK9qbbm-HxYJktn6V_zJF4Nk3mOrFfIkrKPYLDiZCkd6KRycY53yqqxNvbeBvCrjsV2tGSd05qaJ4mGfsLJCZoOu2uQkFy6GZCOhckClX__t8gSGRDPu3gAzTow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/20234" target="_blank">📅 19:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20233">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c39d5bd85c.mp4?token=WozNut0YsjTYyddl0sPdwxiTF5pMAyqZvXsfuybcqz4vUSTybEbcfsZEO3emqKplzaKWrWy8KYILKi4Jdoee4j5m1aEyRM81en4oA6SZdz0eLyJ_-HENQO5NY2wyaEJXOylJTdhgy9ed6kra12aKRVeHYa9dkMGLqzD6W8aaCJIT6mCVtWmfOCARU3GI7icZHBwAWVXckKtl5aDC0OfO0QRVa6K8ToRNp-GzNQwKnN0rqKNqguT7QBb9RrYsAJhEvzDL484jQ2uYP2LhhPVg5_CN78N8nL6favvnWRvpwqvpsxrcs23Bu1MH_q5Tzl8y_3Bz4O_cYGch58nhybHlsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c39d5bd85c.mp4?token=WozNut0YsjTYyddl0sPdwxiTF5pMAyqZvXsfuybcqz4vUSTybEbcfsZEO3emqKplzaKWrWy8KYILKi4Jdoee4j5m1aEyRM81en4oA6SZdz0eLyJ_-HENQO5NY2wyaEJXOylJTdhgy9ed6kra12aKRVeHYa9dkMGLqzD6W8aaCJIT6mCVtWmfOCARU3GI7icZHBwAWVXckKtl5aDC0OfO0QRVa6K8ToRNp-GzNQwKnN0rqKNqguT7QBb9RrYsAJhEvzDL484jQ2uYP2LhhPVg5_CN78N8nL6favvnWRvpwqvpsxrcs23Bu1MH_q5Tzl8y_3Bz4O_cYGch58nhybHlsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضرغامی:   مذاکرات مثل خوردن گوشت الاغ مرده در بیابان است!</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20233" target="_blank">📅 18:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20232">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نگاهی به فیلم «رشته ها»!   امروز، ۶ اوت، سالروز بمباران اتمی هیروشیماست؛ روزی که در سال ۱۹۴۵ برای نخستین‌بار در تاریخ، یک سلاح هسته‌ای علیه یک شهر به کار گرفته شد و جهان وارد عصر جدیدی شد که در آن یک بحران نظامی می‌تواند، در صورت خروج از کنترل، به تهدیدی برای…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/20232" target="_blank">📅 18:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20231">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ: می‌خواهم ضربه اقتصادی نهایی را به ایران وارد کنم
ترامپ لحظاتی پیش مدعی شد: آمریکا جهان را تحت فشار قرار می‌دهد تا ضربه اقتصادی نهایی را به ایران ورشکسته وارد کند. آمریکا در حال فشار آوردن به تمام کشورهایی است که هنوز با ایران تجارت می‌کنند تا روابط خود را به طور کامل قطع کنند.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20231" target="_blank">📅 15:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20230">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-poll">
<h4>📊 اسرائیل تحت هدایت کدام دکترین و چند بار به تاسیسات هسته ای کشورهای منطقه حمله کرده است؟</h4>
<ul>
<li>✓ دکترین مونرو — 2 بار</li>
<li>✓ دکترین بگین — 3 بار</li>
<li>✓ دکترین بن گوریون — 4 بار</li>
<li>✓ دکترین شمعون — 2 بار</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20230" target="_blank">📅 15:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20229">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ناصر نوسان کف دلار را در 195000 بست.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20229" target="_blank">📅 13:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20228">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تحلیل عوامل سیاسی چرایی شتاب شدید رالی اخیر دلار</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20228" target="_blank">📅 12:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20227">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دلار فردایی تهران
⏳
192,300 تومان!  کاملاً مشخص است به صورت دستوری دلار را دارند بالا می برند تا جناح تندرو را به تسلیم وادارند یا دستکم گرانی ها را به گردن آنها بیاندازند.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20227" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20226">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1KLbpxYDJbELM8K24fJ8K65da0AM5MN59VfcQ0WZgFPsyqXRzOrtbHwHXxsJxOW6r2-Q0ePxbPa7HbtbMVJ2DTN_u625BjhBND5EBgcW-jUuIHJjqTOwqSiNygBKPgjJg4WN4mkdICRhvqQ2CHLs4EqfseduGl6fWu_D2ohRgDAZrV6ewMoAlTE7PVvRo5ykVlVsqmP5xXZgDCcSdkye1TGFHpDEOAa9ZE4GozkiOR1t4ws4OdsAWL7g569NwG0q3Q11KsDLm1Xp5OYV9ORVSxJyEFiIjXSKkVSGC7yLdA791ogcUFeTIjVWDoruvGAID1yATbi6jVOXWtNLBpsWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش
تا زمانی که بتوانم پادکست های GeoMarkets را دوباره از سربگیرم، این جدول هر روز ارائه خواهدشد.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20226" target="_blank">📅 12:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20225">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lx5XjjmclEVAIRm1UxBbqNq05sFZPZEGN6dctke3H0psdLoBvVaUk6-AQxgApouRYbg6KAq8nEb6Gkiqmwcif3eEj94AFTZ9ZcRiPZ-4ms1atFL3yqMoKUHIjd0UEtGgIdS1G3PB_F5mgjdeCD2i3hnni0KQiqDZln-600kXiEX7bYorrcmLcXJFcqST_jz3u-rtFDqDC1TODTj69y6p56KkN7Hz6uohV_cr2MDzuCh7sRGjAn8Sm81ypkXLR3gX-ixZJCLeLZ7JVywNSwpaxU2geOprLBM-mU_jf8zONYikDpk2J8byJxHJbti-jIXbHqNz46-Y078qEe53B2rJNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتصال ریلی ایران و چین   پس از آغاز نخستین محاصره بنادر ایران در ۱۳ آوریل، حمل‌ونقل ریلی کالا از شی‌آن چین به تهران افزایش یافته و تعداد قطارهای باری این مسیر از حدود یک قطار در هفته به یک قطار در هر سه تا چهار روز رسیده است.  این مسیر ریلی پیش از آغاز بحران…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20225" target="_blank">📅 12:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20223">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X8zrVyV3CCmjZnjM9NpcwPQtadPXRbpE3V3xI9GWfNvVmbDx00j7-GJOfYVP5xVmLUdiZqj-3KY_N1aEn22Fxe_R8-sfx79zYqBvYB7OX12Af2Kn368BQSGtxKkZearKsb8vfg4AMog5We-yTBbxeoCWt9EMF8WxVr8lHIiX6QpjT8_pDmCR_8_TVUlMDJULQGH-gMM4pjE6y8F6iV3cJIkHrPGSf0ksiJjjtfq--8rKlip-5ubPPaju4V2tdPs4BcNYbwWjnhDCtodzLMRkKr-Zqsm1TkjHIGt4VmvEesJs-keQ9EM4q6z6tYJKfVNYshEl2kR0Q136EmNKF37sAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nTa0kEjvWbdh0HGNd0mPrJYQJX8coEIs-Ez8jaAgJOco12kXAMIhkXfaDVNL1mQN7gHH6dAKjEd4H-gD6zvDwu69ICRwgB5TfkYw1wBYbDyTgL7sBpvXC-bx4KIghCI7FgyW8rWZelGlOXuiY-g6w3vsmOMGmvKcTgMFI4-x9cnQJ1JhLNHyQUQIuYCN7c26_puDNoZWtCYGPUFXWieeYAm7lzs4lE0OB3n7C7to5KizDlRCKNlsW-YMtq2kAtNroiWckeAEj3wSfVb8Khjm7QeTxb1TLZotWseXlJhTCnY112jTgJDV5BmaigPs8OWeGAAyooptFNK_C1MVKvnyqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم بسیار بالاست و پیش بینی می شود شاخص نزدک افت داشته باشد.  طلا هم با این وضعیت قاعدتاً امروز باید به افت خود ادامه بدهد.  دقت کنید که سقف دیشب عملاً جعلی بود و بعد از ثبت آن حدود 800 پیپ افت داشت.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/20223" target="_blank">📅 11:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20222">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUNSIO1064udaOy5wapujpa2eX96ev6LgVfdpxwZpoOWgaLhyqUKxkDzdVlsfrchZSlG_OPI8GJXbr0ruol7HiEq7X0qDP8CAD0e7Yy1LN-5lN-9AuMDR90iZZzBD1d3dzcu2MkuYy7YsZ0Ki7RxxKo7pqbfq-1qgBZQWzP5zKxN12Uw7idqI8G_7wNvmGBZ0IO2d_Vxrrr-2yrSq5oD3YFhc472DBgu4l-QwNTRpQl1RiiFCAGqklsTIHtDit71xisw4O2fyxbEoCJ-PMCRF4HaTjgNbpCetVKmV3mYQdg5mJhiVx_TUkg6v2QxX0OCv_yP1dEYsLdZaqQQIzlLsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و فشار فروش روی دارایی های ریسکی و احتمالاً طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/20222" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20221">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">عاصم منیر به تهران آمد.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/20221" target="_blank">📅 11:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20220">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDfDwsm-jQj1uKZACyj0tmHhixTJlbstlL8jRg2wOOpd0WzlJ-_jcTU3AeN7lkIe0NUccEV9xYOerFLcP6ilamqg7e7XYzI4Aeg2pXT-7gNjUku1MQh7NG203JFFBJdcq-fZdgrYaXLoHOx5d_r4-Q0w-PP0h9VXfjy13Vnx9dqRE3OcwdWxNquStcMScOCw4--R4CKoUEhtrRuVimoGmkBqSbeKKPbSvzMKz-Ik1h5b14iTaaajXIWwtw7GfY_df0kEdpNw9dbJEHOySJs67U8Sfe4P274TaY0k2Zt8d90jyQRB_cdCzmkgPolCO3mgFlaGIlvPWicH8L5rV0gSdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه NBC:
حملات موشکی و پهپادی ایران خسارات بی‌سابقه‌ای به تأسیسات ایالات متحده در خاورمیانه وارد کرده است که از هر آنچه ایالات متحده پیش از این با آن مواجه بوده فراتر می‌رود
- میزان این خسارات از هرگونه تلفات قبلی ایالات متحده در تمام درگیری‌های گذشته فراتر می‌رود.
- بازسازی زیرساخت‌ها طبق منابع خبری، میلیاردها دلار هزینه برای واشنگتن در پی خواهد داشت.
- این حملات نه تنها به تأسیسات اطلاعاتی، بلکه به سیستم‌های رادار، تجهیزات نظارتی و پایگاه‌های نظامی ایالات متحده در عراق و سایر کشورها نیز هدف قرار گرفتند.
- این خسارات سؤالاتی درباره توانایی پنتاگون و وزارت خارجه در ارائه حفاظت کافی برای تأسیسات خود برانگیخته است. کنگره از همین حالا بحث‌هایی را درباره تأمین مالی بازسازی تأسیسات آسیب‌دیده و تخصیص مجدد منابع اطلاعاتی با توجه به افزایش تهدید از سوی ایران آغاز کرده است.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20220" target="_blank">📅 10:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20219">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZVyaoO_f3AmQiBYO0Z_dNVYh1SnOT_EH7yk5igCdDpnxzG2H16qhwCFxipuRr7EPJlcIEvQuq4JFW4Fb2jAAbmUbChiWTPt7h9qG-t-_z2gcjPrOzD1VdFXcTjT1ylH2GHI8Bmbk28Oy4xieqhd16lBe710f-q7vo1FuCgV_IzP4nMkwbFWmX22xsAw4oGkhRsvzHimV7ZT1yU-AWyN66_JMC1stAJzxuETQZD5Gf_YITaLcSCKoN-5ypg3yZ8Y0ayvD06k9Wtttk6k8Ym7Ma9cA4DlfXVPUFzx2QyA1FoXwqaXggfC3pA9uBj2JW_ro8TF8BClpeg09nFPe7Bq7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
روز شلوغ انتقال نفت در دریای عمان
🔹
کپلر: در دریای عمان دست‌کم ۱۵ عملیات انتقال کشتی‌به‌کشتی در حال انجام است.
🔹
حجم نفت خام درگیر این عملیات حدود ۲۵ میلیون بشکه و مقداری فرآورده نفتی است.
🔹
نکته مهم اینکه منشأ این محموله‌ها تقریباً از تمام کشورهای نفت‌خیز منطقه به‌جز ایران است.
@khate_energy</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20219" target="_blank">📅 09:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20218">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ می‌گوید توافق هسته‌ای با عربستان سعودی تنها در صورتی پیش خواهد رفت که ریاض به توافق‌های ابراهیمی بپیوندد و اسرائیل را به رسمیت بشناسد</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20218" target="_blank">📅 02:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20217">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c56a73bd.mp4?token=E1rTrpU-flnJqogxawvuTg4sWO7xLvgundLOj1J9J6IRvmKC19ppN2zp5pNCaGyH1sEwS3D0dU_R7f2-PKdLaCs4ip352EPVbtWIjFwUknMFL3MFbHfaqLpP15p9Uth3fVu9PYOFxPYu5sFI-rTMrj4bI3kqqso3h9Z3oywl5FP8SHTeigqPmeyOJpg3hdM9uecXWnqj5tmbUQA4K28cF-Cy1vQAVOkfI_K72dgge8qCxeRR_uMVD9ZRL1PiRa6S9ZB35d5XjwhGWlfwdHA9LyBpR_Do5DnBJJ7u63wY_9BNCxcTcKltS4bSKRhvDq50MOcOEzMajNreWW1gpW5hdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c56a73bd.mp4?token=E1rTrpU-flnJqogxawvuTg4sWO7xLvgundLOj1J9J6IRvmKC19ppN2zp5pNCaGyH1sEwS3D0dU_R7f2-PKdLaCs4ip352EPVbtWIjFwUknMFL3MFbHfaqLpP15p9Uth3fVu9PYOFxPYu5sFI-rTMrj4bI3kqqso3h9Z3oywl5FP8SHTeigqPmeyOJpg3hdM9uecXWnqj5tmbUQA4K28cF-Cy1vQAVOkfI_K72dgge8qCxeRR_uMVD9ZRL1PiRa6S9ZB35d5XjwhGWlfwdHA9LyBpR_Do5DnBJJ7u63wY_9BNCxcTcKltS4bSKRhvDq50MOcOEzMajNreWW1gpW5hdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی overbought است</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20217" target="_blank">📅 01:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20216">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خیلی overbought است</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20216" target="_blank">📅 01:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20215">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یکی از همراهان کانال این را فرستاده و گفته:  پایین کانالتون شاهد خروج سفیانی هستیم
😁
سبحان الله راست میگوید این شیُ عجاب دیگر کیست؟!</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/20215" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20214">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5affe27b93.mp4?token=I_6IrUCyvhI9qt_8hGQfSDaZpF_bAbzR6VgT9XS45-h1ogm8qgAppMxJtRz4aEQDLdiD56n8JRyA7h5bKapEWb55kVIyqkqG8NmM8XcArDaPCognkhTaj7VAymFCb5qQnMzMbi47pOlyTLVHZ4slgtcAeXHkfuJ907waAKQRwxDsZ-TDmIxsbgOLf0TQwX_gLTM2hWUhPlPpixa-IYDz7-0B3KQBRXyW2-YmJF3IlUCXDLrsEW27VhIiBGfmxv2gMN-aETwdIuKCESJSauX6SSuPE1HejD9iI_8m6yGRPKlCF1IUwPZsl1pgC81U8hunfkMXTvy8OwbZivxZ0dyc4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5affe27b93.mp4?token=I_6IrUCyvhI9qt_8hGQfSDaZpF_bAbzR6VgT9XS45-h1ogm8qgAppMxJtRz4aEQDLdiD56n8JRyA7h5bKapEWb55kVIyqkqG8NmM8XcArDaPCognkhTaj7VAymFCb5qQnMzMbi47pOlyTLVHZ4slgtcAeXHkfuJ907waAKQRwxDsZ-TDmIxsbgOLf0TQwX_gLTM2hWUhPlPpixa-IYDz7-0B3KQBRXyW2-YmJF3IlUCXDLrsEW27VhIiBGfmxv2gMN-aETwdIuKCESJSauX6SSuPE1HejD9iI_8m6yGRPKlCF1IUwPZsl1pgC81U8hunfkMXTvy8OwbZivxZ0dyc4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از همراهان کانال این را فرستاده و گفته:
پایین کانالتون شاهد خروج سفیانی هستیم
😁
سبحان الله راست میگوید این شیُ عجاب دیگر کیست؟!</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20214" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20213">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20213" target="_blank">📅 01:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20212">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اقتصاد_ایران_ممکن_است_از_دوره_ریاست‌جمهوری_ترامپ_جان_سالم_به_در.pdf</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20212" target="_blank">📅 01:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20210">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">اقتصاد_ایران_ممکن_است_از_دوره_ریاست‌جمهوری_ترامپ_جان_سالم_به_در.pdf</div>
  <div class="tg-doc-extra">299.1 KB</div>
</div>
<a href="https://t.me/SBoxxx/20210" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/20210" target="_blank">📅 01:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20209">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ونس:   کنجکاوم بدانم قالیباف چقدر در درک زبان انگلیسی خوب است</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/20209" target="_blank">📅 00:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20208">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSlsC5K_0Q31ddr8m1jACKC5b3dcuAGi1kFI-7ZGVUwgwQjpQYHZ5D6Z6DOGZI7Lkn0CeeSDYHNMmEML3O4z4_BB8nZdrpvuH-6tgNa_PEvz8hTgZ6axfcep6N5jaG65HYjToM1fHfRsfW8FNvI3x3QEPJFUE7qHMQQPVViTpxg2wjU2f4NiseLbWaP4YsVGJrMT3tf4DQp9Fb7NAzXeYKIke_0IWCkdapUsPjqgDi7Yj0lAh-UIv6ryOwz4CZpE8DyRdHdRA0DGDdf-RpG0Esp5F8rtFdIYZ6IluCBmC9Cr9ZJINYOSMSbbyZXtRdjcc7KuE0cECk0Dk17vBya8Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت قالیباف در تمسخر اسکات بسنت</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/20208" target="_blank">📅 00:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20207">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">باید بگویم خیلی خوشحالم که عمانی هم نیستم!
از یک طرف ترامپ می گوید آنها را بمباران خواهدکرد از یک طرف دیگر ایران می گوید که باید مسیر جنوبی را ببندد که البته خودش هم می گوید بدون نیاز به مجوز عمانی ها هم این کار را خودش کرده!</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/20207" target="_blank">📅 00:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20206">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">غریب‌آبادی: در تفاهم جدید عمان می‌پذیرد مسیر جنوبی را کاملا ببندد
البته درحال حاضر هم نیروهای مسلح ما اجازه عبور از مسیر جنوبی را نمی‌دهند.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/20206" target="_blank">📅 00:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20205">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کاظم خان امشب اساسی رو بای نفت است</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20205" target="_blank">📅 00:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20204">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">چرند.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20204" target="_blank">📅 00:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20203">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">با این وضعیت می‌شود فهمید چرا ناگهانی تصمیم به دوبل کردن قیمت بنزین گرفته اند.  وقتی عرضه سقوط کند، کاهش تقاضا با جهش قیمت یک گزینه است.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20203" target="_blank">📅 00:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20202">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntMf2aGkfYc2OSn0Kj0X4QjDM-PbhC3S6DwphHW7z-iZFkDkCbWsBddhKQC3Vz9NpJ-KSpfLrgjM-mLFb3kk1asznrp-Y6yrDRCaCyzFHhy_igLbpT0ABM9indOfJ8ZZGaUvY9OhdD4KGlMdk-NGYC5wg47q_Io8vjiUbhDy6ixx1eapvBeihQQtrtF7bFSq9oXkN0vay8OwzNUkXGM_LTLCUH6ybwlh2vpH9q6KV0gQy5vp6aiT-9aXVbacO9FtmjZP1rxTQplQ1HN2wIIhqg4VxJFcbbm3ghqogK8rckYxuopcTk_uyuR0lg0CWxDjHNis4JsQ9cA_5o4DV23Eiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Gasoline
— D
قیمت بنزین به نظر چنین مسیری داشته باشد.
کاملاً حرکت نزولی اصلاحی به نظر می رسد و تریگر آغاز چنین حرکتی می تواند زدن تاسیسات نفتی منطقه توسط سپاه باشد.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20202" target="_blank">📅 21:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20201">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iR50GtwwAm0dUViq4Yp5xlhKUFYz-aLtbOy4NoTUPQEhplG-rM-rDjenk97JG7bb2OfwEIZY2QX_QGX0wrtFHDG3ObyXyF2oRgCzNCjdPVFC-EznmqRKQC3ZxE2QQcXS3lwHJYwvjBpQXes0Lv1RL1UILCpEKz3SAQPZjFDtXzBCfEn10AGSrhvlfLqRZt3kEWnJqKmGiar6X_dsxArsE63fkuvL1qHDm17QgTKQv_tGrzlKkkX1Vqtq2_2J6LmjTI_vEoeIfrfhl1BXJKJvpWXopupFeIHANjupi-vGD7rnaiyFU4UAVN0O-tPwgoR2WWROgZ7nTBiM6XeR8e9BRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید اسکات بسنت وزیر خزانه داری آمریکا
رهبری ایران در حال اعتراف به شکست اقتصادی است.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20201" target="_blank">📅 19:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20200">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وزیر جنگ اسرائیل: از سوریه خارج نمی‌شویم
کاتز: تا زمانی که تهدیدها علیه ما به قوت خود باقی باشد، ما از جبل الشیخ یا منطقه امنیتی در سوریه خارج نخواهیم شد.
ترکیه در تلاش است در سوریه مستقر شود و ما به همین دلیل وارد عمل شدیم؛ زیرا منافع امنیتی اسرائیل در معرض تهدید بود.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20200" target="_blank">📅 19:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20199">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ایران و عمان گفتند که پروژه‌ی مین‌روبی در تنگه هرمز را بحث کرده‌اند</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20199" target="_blank">📅 19:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20198">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVo4IQno2yI7lNvQ5D1uY3fQg9Z4XzN8lZ3NVWbd71bFiSeWivg4yqbLcGGZkvwh-aE54UvrNzhhrqlM3jf8c3YndBOBR4CWS2mJo0h0i1f9OAWTqoZfSEq6xd4SkCOnhrKHHYJBIAYmlS-gyskTSDTlmo91NMi-yTjONqc--GyOpmvlTXUkdalvl0CRLONZ9A88jWXdYfsF_zwWzt8efhzz06CfPPfOQoPOlJcXCEkwwa6RCZ0_IRq_6HbiCKKBGEEdle9Hyh66MKqMWmItDx53Xla7dcFIEJlV6MYZmMwNeEMvOxu07KQj6TFfPoZD--nt5yjpaUf0P1qWOqVKPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
تمام مین‌های دریایی که سپاه پیش‌تر در نقاط مختلف تنگه هرمز قرار داده بود منهدم و یا جمع‌آوری شدند.
همچنین وضعیت تنگه هرمز به صورت وجب به وجب تحت رصد ماهواره‌ای (نیروی فضایی ایالات متحده) قرار دارد و هر اقدامی در جهت مین‌گذاری مجدد با پاسخ ارتش این کشور مواجه خواهد شد.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20198" target="_blank">📅 18:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20197">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZJkwezDMUTl6RdRR4yoR_KQk5ByxSOf7cqPTtG4nKHH_tuWenbEYGbILb8itrGNCB-OYfBKmCADh0JILP98VFoxm6CARt7BzZ4NJv_ntRsOhs0v4Zz04-Sz1bC4CKf1bM1q10l3uHJ5QVEzmPNMly5erZkh5m4YRDccznw-jXLenSqzT67QDGpg86buEV5t5cpcuG7dJU89k-8vGcERRiPfts_6F4_DqpFrfjepuLyfvax3TW8o51mVuD87Mn4XWjicwiPiwR-niiD_KYjDbeYkayz_ZxCeLS7fgz4KHuaPGlw0Xv9xrrJPzNzN5JEtyauIMzSvRbXAZWZrsugyJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عن این مفنگی را درآوردید!  ولش کنید دیگر بگذارید بمیرد.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20197" target="_blank">📅 17:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20196">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtApE2aD_QM0-SwGhYyoLaY4l5zRgf1c3FxWwYfeEAZ4tdnuk3kRUqZt0u8s8QBRoxkKuEZ87ffKhGVupQehWq7MtzywW-jqzV6Oq6L9N3usuA1g4BKweBS9usLz4ibvAHzufwymr0AFzrfJwhOX1xwqu8-i1tnnhqrb-Fegb_luANygZBwpxD52x8qV43aI-wC7aa3CvZ1kf7UhIcwpQsil8S3zBOOIt0lokQSzOOryfW7pGMP6rK_UV2Y8eorMUFrBHjUwjdbL1t-RGoQu0WGPgO6xF-d8mipiyW68tF6UJo_EC1xptU7rizci5OS23dwv-tZ9N8oSr3sXYNm1-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ
«جمهوری اسلامی ایران که در حال فروپاشی است، بخش‌های بزرگی از نیروهای نظامی خود را حقوق نمی‌دهد و هم‌زمان، در سطحی بی‌سابقه اقدام به کشتن معترضان می‌کند؛ حتی افرادی که در حال اعتراض نیستند.
این یک بحران انسانی با ابعادی بی‌سابقه است و باید همین حالا متوقف شود.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20196" target="_blank">📅 15:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20195">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20195" target="_blank">📅 14:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20194">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حالا اگر تصویر میکنید که یک فروند ناصر همتی میتواند جلوی این روند ژئوپولیتیکی را بگیرد که ولی خب.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20194" target="_blank">📅 13:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20193">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبلومبرگ فارسی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCnzEOfl4V3P7ydkh2qRtlvoUyXMvmHDLsqWam9qj0V9uKvTn31WMUeBBvzvt8JohoUPXn20Ys0DyvkdByURN4W3BvSf__UtUfK3NXPN5HPeYbNg_QloBBY1IXHpy1LTOJYmyom6v_dLpck3jh-PcbJo2djktFKPUCLBDUsCl4MrJ8-9RJBiOIQw2lIxV3ApIvrWAIonZctlXvkHKvJj1BbIwpScsQihKnW8zWfFxu_BCjo9NiT76UGcPGgwnOI5n2tTLYXnC3jxLehhn68SWK48Ryg1kdpMZ7teoAviyPUpPAA1IZayy7GlAPtDpx9TiJCQWNox5yw6HOiDIyve9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای همتی از زمان دلار ۳٠ تومانی تا امروز که دلار ۲٠٠ تومان را پشت سر گذاشت به آینده اقتصاد خوش‌بین است
☑️
@persiannbloomberg
بلومبرگ فارسی
✔️</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20193" target="_blank">📅 13:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20192">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0FnBedPpug9eKTt36vFu4CAtfYv2PuLNWo7wK07rI3X2APv8Zd11eg9s6i94k3d2dvTuWvi8rIke67KVcYy2M8CbC3BCosYbukPwbRcbrpDD4VLH38P-3zUREIFQSjuk-K9TB5iLPKVXrp-8dXwZ76JikgJnFAvRrBiIOklzOIYSDkeVqDQIhP-v4XblQcQyFx4aNl5FVh6qL_Hc2NRo_GLIgbJ6JVUllc5Sjubxm0HSzVBKmitjO9U3jGMEjf-ZpaY3MgGnl0oJ2La4bfB6DFkjnJsWjg3625akv-PW9G8zs2KhIJp1J3hdx_PDjocEwPFJ4FzLV3RFta77nrYOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادغام شبکه خبر و اینترنشنال</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20192" target="_blank">📅 12:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20191">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">چرند.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20191" target="_blank">📅 12:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20190">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یک منبع مطلع در خبرگزاری العربیه:   آمریکا پیشنهاد کرده است که در ازای باز شدن تنگه هرمز و توقف حملات توسط عوامل، محاصره را متوقف کرده و تحریم‌ها را رفع کند.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20190" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20189">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یک منبع مطلع در خبرگزاری العربیه:
آمریکا پیشنهاد کرده است که در ازای باز شدن تنگه هرمز و توقف حملات توسط عوامل، محاصره را متوقف کرده و تحریم‌ها را رفع کند.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20189" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20188">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuHe97KZvzGUSrIv3GXJxLvtYK42RndX092htXQNJycFO0MDZ-9mMxJo9XZteuNdbA1-Bjhgp3JDBSBdLqyem-Vh1V90qzq7R3dZxPUp3XZCTYXgGUk59MQsWtQ-bkLDDYddt4a8OcLamSdYLBITrsCfWUbWr72qCTSbmG7I3chi88ug3yODCafYC3wmibLJy_asFDRxGpV0S59BC6sXeXYJRLxMPnRugYvqn1Ml6ElB5u_Ghiir14-1sRqaM0ihvcWkAGog0xqdF0ghVRU6K_j9UyGTIg-ExU4gvjcptHpbyICH9zPnRLKaMJ6dEUjKqX-Ou7Xpe7h5HoGAYGIFQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم بسیار بالاست و پیش بینی می شود شاخص نزدک افت داشته باشد.
طلا هم با این وضعیت قاعدتاً امروز باید به افت خود ادامه بدهد.
دقت کنید که سقف دیشب عملاً جعلی بود و بعد از ثبت آن حدود 800 پیپ افت داشت.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/20188" target="_blank">📅 11:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20187">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKjqE4kaMR5SnYtKGwFke8fcq_cf9qSeLca1om04qCLP2x_fYIS71qarCvzon_v17GLSflKo3a8Wqt9B3gipKPJcTDLr0AW2doZk4J5Pzp4dqlsLz_9k5GfNkJBh8ZxQEj5TWGNSDX9KksoHDrJpaqMllMGh4ES-0JHFemdgV3Bi5nVZ3qGCVI6T43m2abpDyzxj-4vFOGWy4CLNN-6tkW07kKO9nFeEEBtpIcATVZ6kxUL1TROAGlty34fEefZdofd_PCayoN0DHCtyKmqz_QRrdPdXhaXRoaWdk_J71ZjYhYMesJTdkgAG97tK9mazhll_jDDQdqhOl9k3lFJkIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج 2 نفت دارد تمام می شود.  موج اصلاحی دلار به ریال هم قاعدتاً باید آغاز بشود با تارگت 240 به بالا.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20187" target="_blank">📅 10:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20186">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndQ3tz_GWkhIilbXFY7jx0SLrt4BuNUxk2YkahKic9-0FmJ8jMGQtAxfMukNr4MM1MAeawkVVNsEgctYCDwGTgaBtiVWXM2h6EtSQe8G0Y_mhY5vPZ313th4ku87yNypy7wz0BrnzqSGkBITwaE6RZj3qtk_dtSOOT1Rfn8JfTClxRTGTadx_i856dJuOnca6jAwRiDSu7063zFwq5D5KLPvuSK2IpoRiVg4YiU0aoPHFoeYj1BlkBTdQnc5WC3m5PVr5r-CcMTxIBlybVDNUUDhr0B_EHFzFRDaHY0ZMonAYUbwRuEuLKicuYPXx_N2O4MVwktaE-aqaTSGtd8G-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20186" target="_blank">📅 03:24 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
