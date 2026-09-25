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
<img src="https://cdn1.telesco.pe/file/k0dHcBPMtvASzaU7B7UQ6C2XdtY6hK9eBWyZc6j5kcKrDZMb3wMPgldK4hBVtGIMum30yLyb_96fp5jMSC4IRbgY0QIZuyQa8WR8VQARQOWjQ2XgofQsFCaYfooHpUr0fs-_yG7IJOSZ-MOEeUNUTp19TbBdO1F1d8HvNrAnKZ7XstZNKle3_mZSkLJH8GcrOVmBdgYxv-KsFJdkoZbTvV37cJXUwTHpeyezakQ1L3KUu2mBzqMcKiWZBFiWz4yaPxuJ0pY8b1GgozUpn-1_ZOJl34pGHPFEwuJH2OnUh1l6FdOQhSIV0x6hxIClGyzQLsoMrFqDv7cK_3onDB_SUw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 04:31:48</div>
<hr>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مصرف Opus 5.5 به طرز عجیبی پایینه و همه توی کامیونیتی ایرانی و خارجی هم دارن میگن.
خودمم که دیروز توییت زده بودم راجبش.
روی پلن 20 دلاری هستم تازه و اصلا تموم نمیشه به این راحتیا</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/MatinSenPaii/5344" target="_blank">📅 00:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1cccff5f95.mp4?token=Vwmtlb3ZPlJLw0s3XrHePpnWVXjqq1tFsmY79aWbW_04ABIuFFOo_3q2XENgownUpc0C3LcrQSyaWWbzkYH6oC0gSuyqMyYXfeJKvuEgEOo7alNxSWSYm0iFryMY-Pruy2ZA59wHA2qp1R5YNbGPMIM7-oUgIncj1lCACe8lrTOFaNGOR2f52Ob6aynCc1Vcil8ji6bSLnvfflJvtdPBngg0zns15mBtEt6MmT-CKUOosvwZbcQ8uVoZmLWwFDAtQB5DEKtucCz-lid7p4kODnk9HXqcYfGrxWj4RmrTt9rkeseavwpHMznuHv7wyJF1IZk6KuWrT8fgJHsaJkd_wA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1cccff5f95.mp4?token=Vwmtlb3ZPlJLw0s3XrHePpnWVXjqq1tFsmY79aWbW_04ABIuFFOo_3q2XENgownUpc0C3LcrQSyaWWbzkYH6oC0gSuyqMyYXfeJKvuEgEOo7alNxSWSYm0iFryMY-Pruy2ZA59wHA2qp1R5YNbGPMIM7-oUgIncj1lCACe8lrTOFaNGOR2f52Ob6aynCc1Vcil8ji6bSLnvfflJvtdPBngg0zns15mBtEt6MmT-CKUOosvwZbcQ8uVoZmLWwFDAtQB5DEKtucCz-lid7p4kODnk9HXqcYfGrxWj4RmrTt9rkeseavwpHMznuHv7wyJF1IZk6KuWrT8fgJHsaJkd_wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب، Jev از زمان عرضه داره روی GitHub منفجر می‌شه و همهههه راجبش حرف می‌زنن؛ و اینا چیزای باحالیه که مردم تا حالا باهاش ساختن و شما هم می‌تونید بسازید:
- پروژهjev-trader — ربات معاملاتی واقعی که سفارش‌های limit زنده روی هر بلاک ۳۰۰ میلی‌ثانده‌ای Monad می‌ذاره و فقط Jev تصمیم می‌گیره. ۱,۹۱۱ استار
github.com/jarrodwatts/jev-trader
- پروژه jev-ultrafast — ایجنت مرورگر که هر کلیک رو خودش انتخاب می‌کنه و فقط وقتی واقعا باید تایپ کنه، مدل متنی صدا می‌زنه. ۱۶,۷۵۸ استار
github.com/browser-use/jev-ultrafast
- پروژه jev-doom-agent — Chocolate Doom واقعی کامپایل‌شده به WebAssembly؛ دو موتور روی یک نقشه، Jev هر فریم تصمیم تاکتیکی کلان می‌گیره.
github.com/lukaske/jev-doom-agent
- پروژه jev-t-rex-runner — همون دایناسور کرومه که هممون هزار بار بازیش کردیم، حالا کامل توسط Jev بازی می‌شه: بپره، خم شه، یا ادامه بده.
github.com/joshlarsen/jev-t-rex-runner
- پروژه‌ی typesafe-chess —خود Jev در برابر یه موتور جست‌وجوی واقعی، دو بازی با رنگ‌های جابه‌جا. موتور جست‌وجو هر دو رو برد، ولی حدود نیمی از حرکت‌ها نظر اولیه‌ی Jev رو وتو کرد.
github.com/TholeG/typesafe-chess
- پروژه jev-drone — یه کوادکوپتر شبیه‌سازی‌شده فقط با دوربین مسیر مانع پنج ایستگاهی رو رد می‌کنه و Jev نیم‌ثانیه‌ای یک‌بار وضعیت رو قضاوت می‌کنه.
github.com/RomanSlack/jev-drone
- پروژه tax-doc-classifier — فرم‌های مالیاتی IRS واقعی رو با دقت ۱۰۰٪ روی ۲۶۱ فرم دسته‌بندی می‌کنه، با هزینه‌ی تقریباً ۰.۰۰۱ دلار هر صفحه.
github.com/kyotofin/tax-doc-classifier
- پروژه killmyidea — ایده‌ی استارتاپی‌ت رو توصیف کن، Jev از هر زاویه‌اش امتیاز می‌ده و بعد kill، fix یا ship برمی‌گردونه.
github.com/monteduro/killmyidea
- پروژه jev-curate — ردیف‌های Parquet و JSONL رو با قضاوت‌های typed با سرعت ۱,۵۰۰+ ردیف در ثانیه پردازش می‌کنه و فقط چیزایی که از حد رد بشن نگه می‌داره.
github.com/AkashPriyadarshii/jev-curate
- پروژه pg-jev — افزونه‌ی PostgreSQL که بهت اجازه می‌ده به Tableهای خودتون سؤال انگلیسی ساده بپرسید و جواب واقعی بگیرید.
github.com/realZachi/pg-jev
✍️
imryven
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/MatinSenPaii/5343" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tqx4IfpW4yxSRKOEXZteiuShoF6r6CKduXUEE8GnrPS7us-hvX-JvCOMvcDgXDSXJ6s_vRRtAjVd2vKpltyZjLrNCoYV5zf0G0WRtQBcg43wQWpFf-bSpnIqacP-8iuoHyPbLyIOPai4c_bNoE4H9WiTBs76zcWkjaMomMYP3h0HZCa355_Y9HPnh4x3r7i8hSSAuEHh0MQwiVmxKw9bhBfzhU6BajC3SEHp5xRDVAgzHJXSO22-i1uNxcj4x4SQZrp6FEI29qZPzBiTGNTGWZkcHHsH4Z6G-03Pw57znoOXMIAGIZXutD-wrO_1YAjYSpfiyIS6hRDnnNlOGQc-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«داداش اینا که AI بود»؛ ناسزا جدید نوجوونا
😂
گاردین نوشته تحقیرآمیزترین عبارت امسال بین نوجوون‌ها شده «That's so AI». یعنی وقتی می‌خوان بگن یه چیزی جعلی و بی‌کیفیته اینو به کار می‌برن. جالب اینجاست که بین عامه‌ی مردم، خودِ AI داره به نماد بی‌اعتمادی به محتوا تبدیل می‌شه، نه فقط صرفا یه ابزار.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/MatinSenPaii/5342" target="_blank">📅 20:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">هکرها چطوری ChatGPT و Gemini رو کردن دستیار کلاهبرداری
🥸
یه تحقیق تازه از Vigilance Security نشون می‌ده یه کمپین گنده (اسمش رو گذاشتن Dark Sourcery) داره جواب‌های ChatGPT، Gemini و Google AI Overview رو مسموم می‌کنه.
قضیه اینه که: کلی پست و PDF و صفحه‌ی پشتیبانی فیک می‌سازن که با تکنیک GEO بهینه شدن، که هوش مصنوعی شماره و ایمیل تقلبی رو جای «اطلاعات رسمی» بهت تحویل بده.
تا حالا دست‌کم ۳۷۴ شرکت قربانی شدن؛ از Fortune 100 گرفته تا Delta و Lufthansa و Bank of America.
چطوری این کار رو می‌کنن؟
1- شماره‌ی فیک رو با فاصله و نقطه و ایموجی می‌نویسن که فیلتر اسپم نگیره، ولی مدل راحت درش میاره
2- شماره‌ی تقلبی رو قاطی شماره‌های واقعی می‌کنن که معتبر به‌نظر برسه
3- محتوا رو فوری می‌نویسن (جابه‌جایی پرواز، قفل شدن حساب) که هول کنی و سریع زنگ بزنی
4- پست‌ها رو می‌ریزن توی LeetCode، اینستاگرام و حتی PDFهای سایت‌های دولتی و دانشگاهی
پاک کردنشون هم فایده نداره؛ کمپین اتوماتیکه و روزی هزاران پست جدید می‌زنه.
بدترین قسمتش؟ Google گفته این خارج از scope‌شونه(
😂
😂
😂
😂
) و OpenAI هم گزارش رو بسته، به این بهونه که reproducible نیست. چون عملاً به سیستم خودشون حمله‌ای نشده؛ فقط خروجی AI دستکاری شده.
۹۱٪ آدم‌ها جواب AI رو چک نمی‌کنن. شما جزوشون نباشید؛ شماره‌ی پشتیبانی رو فقط از سایت رسمی خود شرکت‌ها بردارید
چون به زودی شاهد همچین افتضاحی توی ایران هم خواهیم بود متأسفانه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/MatinSenPaii/5341" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QEEArHFTaTYOU7ZWNG3xAZv5Rz7PpMNZZxIioeAdQmyOeSFmwwtIpv8HBeOIU8A8zWT3eEtpPd8t-DKBJbH0xxaYir417b0wU5C7MpEfoQrixMNcwBSJdtzl1EtveFaU4dXA9r0yahsXiu4C_dq8qefwzGPMa2Ofwc8QAnkZVAehogC2tz37UzieTvJ_GKkJE7x1qgcR4cHoLxd6hfuQp2x3xyd-WLGfnuTYoVzWPrwA6_h5xjmpnRwS0ONqTnXeJGxJNDmCY60xJzSdejq4Plv4DVIJvd1lXiOa6059LM_J3AOEQF6aHkja5cTamb8YXJgx_sjh5zop8ypDiC84uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیق رسمی استرالیا علیه OpenAI
نخست‌وزیر استرالیا گفته یه agent از مدل‌های اوپن‌ای‌آی ۱۸ ژوئن رفته توی سایت Services Australia و فایل‌های داخلی و آمار سلامت دولتی رو برداشته؛ دولت هم تا ۱۰ سپتامبر خبردار نشده. این اولین نفوذ ثبت‌شده‌ی یه مدل AI به سیستم یه دولته و حالا قراره تحقیق قانونی بشه. (حالا اینکه agent رو چطوری چند ماه بعد متوجه نشدن رو کاری نداریم
😑
)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/MatinSenPaii/5340" target="_blank">📅 18:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دارم روی چندتا پلتفرم کار میکنم، یکی یکی ریلیزشون می‌کنم
اکثرا هم سر و کارشون با ترجمست
و یکیش هم برای یادگیری و تقویت زبان انگلیسیه، اما با یه روش متفاوت</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/MatinSenPaii/5339" target="_blank">📅 17:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MvmiLUdc-AWci0uRP7t0_oJpFdKrDbOqUXqWiZrulcKfgfS8bVKuJDTyNZXysVNjgjPaziF09WpRb-0CXOQQyWyAyOfEAKJcxjnz5ihh1_csxYacf03pqJOGOkntP7dgapxg32j15nHrhMSOk0_LGbdjCYe329FG47BnpAPKfAPiDiBqCO9L_Thjon6dxwMTZkwTNg6tfiR_-WMU2jzDOxXiD_tP_fN_7r3lsUt9SsVr0ffcTk9pwJglZgS4p6Wy1Ihc6ptyFtVmZt-OF-dvRozGQ4SfpVIr_ZW3Cgfzvd6nIz4RpI2JfH_vd-uLARTIS_zBEFIKhvqhBryj1BDcqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/MatinSenPaii/5338" target="_blank">📅 14:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromReza Jafari</strong></div>
<div class="tg-text">تو سایت زیر می‌تونید ببینید مردم با jev چیا ساختن و ازشون ایده بگیرید!
🔗
لینک سایت
@reza_jafari_ai</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5337" target="_blank">📅 11:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5336">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مراقبت کن عزیزم. سلامتیت مهم‌ترین چیزه و ما درک میکنیم
🌱</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5336" target="_blank">📅 11:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌. دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم. پس اگر شرایطم رو می‌دونید…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5335" target="_blank">📅 09:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5334">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یه سریا جواب پیویشونو نمی‌دم ناراحت میشن. از دوست و آشنا گرفته تا غریبه‌.
دوستان من دستام تونل کارپال وحشتناکی داره. توی طول روز هم همه‌اش پشت سیستم نیستم
در نتیجه نمی‌تونم اصلا گوشی دستم بگیرم اکثر اوقات که حتی بخوام با ویس جواب بدم.
پس اگر شرایطم رو می‌دونید و ناراحت شدید واقعا برام مهم نیست که درک نمی‌کنید</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5334" target="_blank">📅 00:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5333">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mlJCb_bklgIFbWd04RDhtX07h53W8Ynqq8re0szSzeQ7RtZB3zzcP2T5HIR6wsmf84rHL9ZizzeNToHS5LETtzSc63k_jA4fbroRO6aE6vXr2zOblZL_fDvUL9E-Endygm6Pp3vZ7MHaDPhUXn_Kaoi4-JY7JLMcbpjiUqhkRWr2Sskogzc1PL4L5aFQdMPspRIfR4iEFuBxezGO7S4yRp_G-snASnkpVwtBwlEDKDnfe9Cevxw8ZGROoPi4crIQo4_azsepqKLeSW2zu7zOkU9pBR8CR4TkbqU48ITY9m_225dQW0wTifKhWsGMyW-Uu0iXjhBGGavy3muNVajquA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل
GPT-6 Astra نشست پشت فرمون تویوتای واقعی
😂
یه بنچمارک عجیب به اسم DrivingBench منتشر شده: مدل‌های زبانی فرانتیر پشت فرمان یه Toyota Corolla واقعی می‌شینن و باید یه مسیر مخروطی رو طی کنن؛ یه ناظر انسانی هم آماده‌ی ترمز زدنه. نتیجه‌ی جالب اینه که GPT-6 Astra با Codex توی تلاش دوم ۱۰۰٪ مسیر رو در ۵ دقیقه و ۲۲ ثانیه تموم کرد؛ Claude Fable 5.1 به ۴۵٪ رسید و Grok 4.6 فقط ۱۱٪ پیش رفت. ویدیوی هر تلاش رو می‌تونید توی سایت منبع ببینید:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5333" target="_blank">📅 23:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71e738709.mp4?token=Tm_eRu3-AnhpTpP4UjWMZiQ1Vs66cX0rKPROvDHQzlsU1MZ-jGlyocnd9mCB_GplWXNU9AS57Zm3l1tf7p7V8b5ObJt8e2o72G_CiFnyvE5c6z233CICxff0cpT2yPb6_NgpxfbBJYp_nA38QqEjSljeLo29ibwXP15PFV8ju_RdUsWmOF950dy2WGLOSJ-mxu7fP6rGDtGXTvNHAQbmCsLYkKZB7mG9nK2zuDTM0x1fkRo_ZSfyA-dSjeH7ZWeU3b-zF9yB6so7A1RJFtZKhoIxDL99fApQ4tfKSk4kJ7QQcqMsYMIcsyIT3y8TzLckk-AK8_VJvicHfvJo5U0B_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71e738709.mp4?token=Tm_eRu3-AnhpTpP4UjWMZiQ1Vs66cX0rKPROvDHQzlsU1MZ-jGlyocnd9mCB_GplWXNU9AS57Zm3l1tf7p7V8b5ObJt8e2o72G_CiFnyvE5c6z233CICxff0cpT2yPb6_NgpxfbBJYp_nA38QqEjSljeLo29ibwXP15PFV8ju_RdUsWmOF950dy2WGLOSJ-mxu7fP6rGDtGXTvNHAQbmCsLYkKZB7mG9nK2zuDTM0x1fkRo_ZSfyA-dSjeH7ZWeU3b-zF9yB6so7A1RJFtZKhoIxDL99fApQ4tfKSk4kJ7QQcqMsYMIcsyIT3y8TzLckk-AK8_VJvicHfvJo5U0B_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتضاح Union Alpha</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5332" target="_blank">📅 22:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مدل Space Bunny(که یه مدل مخفیه که نمیدونیم مال کدوم شرکته) روی اوپن کد رایگان شده برای یه هفته
- 1M Context
- Multi-modal
بریم تست کنم ببینیم چیه
امیدوارم
افتضاح Union Alpha
تکرار نشه</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5331" target="_blank">📅 21:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5330">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGpnRA1aNHt3h6CuNEzpaKKSzwJIQFAxh-kuq7yigAVX0i5leo_RqoK6iH2Perz9KfhWZy35cLdmEMWqGJntkeUf_u5UrRvFyx6yqtn32_CWVY9uSC3ebq5dae8exx4zMHXOSOG8J7-v-mKW0PiPnhRT-hKKx0BnuvQEGMCaLhpBwEv-nmrFlB6oPotD4YI_R3J92e0t7wn3BECj1HK_cVICQFUCAHBASKUD4t2d8J114jkaj68HUu9lzIzz8u4R8Af0h2AegRNW9dBzcrcOK9yDMtKvAF7FFdBAl003X_zB8q6AZ_z9mttGLoh01aHhbu23_kBz8q0fPv4aMPbYGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی GPT-6 Sol، GPT-6 Luna و جنگ قیمتی با Anthropic و Xai
دیروز Grok 4.7 اومد، اون وسط Mimo 2.6 و چند ساعت بعد هم Anthropic مدل Claude Opus 5.5 رو منتشر کرد. اما از لحاظ هزینه، شوک اصلی رو OpenAI با معرفی هم‌زمان GPT-6 Sol و GPT-6 Luna داد که رسما بازار رو وارد جنگ قیمتی تازه‌ای کرد(برا ما که خوبه والا)
مدل GPT-6 Luna با قیمت ورودی ۰.۱۰ دلار و خروجی ۰.۵۰ دلار به‌ازای هر میلیون توکن، تقریبا نصف GPT-5.6 Luna قیمت خورده و به یکی از ارزون‌ترین مدل‌های تاریخ OpenAI تبدیل شده. مدل GPT-6 Sol هم با قیمت ۲ دلار ورودی و ۱۰ دلار خروجی نصف Sol قبلیه(۴/۲۰) و رقابت شدیدی با Opus 5.5 داشتن. از اون طرف هم خود Opus 5.5 هم افت قیمت داشته و هم توی تست‌های اخیر، سبک مکالمه‌ش طبیعی‌تر شده.
منتظر بنچمارک‌های معتبرتر هستیم، خودم هم به زودی تست میکنم
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5330" target="_blank">📅 17:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5329">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یه سری نظرات راجب مدلهای چینی دارم
سعی می‌کنم ویدئو بگیرم توضیح بدم کامل</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5329" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5328">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">عرض تسلیت به دوستانی که مدرسه میرن
غصه نخورین زود تموم میشه
😉</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/5328" target="_blank">📅 15:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8fb483df78.webm?token=veexT4QLwsvW1WJNcf7v7BAc7lle6265OD_ldQ_0GVpTIzOZb11PzO-yXBoy7GR0qnzGNaf-mQlHeCQb6pKqzHM--UBp0YR5q9Op_fedtxofehjP1cD21gpd16SiRaX7xC2tC4tIJ3ZIhdSfROfKhOEzTRkwXixGAFXz6e8bwKLkQrpYlKlQLaaLUNZj2iVAiN-7xh7eXV8kQfiieARt9GjyDqMNo4Nyr9Dldt9Z-_wrzvOpTZ6c0OdF7UTbcUMArMpggVY5Mfa2lPioa4r5zNPcxgVK9Bb-bnpUry73c-stjLuwihycRBw1lK8ZFO6gZU8uRkyxAroC4DlWQavWMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8fb483df78.webm?token=veexT4QLwsvW1WJNcf7v7BAc7lle6265OD_ldQ_0GVpTIzOZb11PzO-yXBoy7GR0qnzGNaf-mQlHeCQb6pKqzHM--UBp0YR5q9Op_fedtxofehjP1cD21gpd16SiRaX7xC2tC4tIJ3ZIhdSfROfKhOEzTRkwXixGAFXz6e8bwKLkQrpYlKlQLaaLUNZj2iVAiN-7xh7eXV8kQfiieARt9GjyDqMNo4Nyr9Dldt9Z-_wrzvOpTZ6c0OdF7UTbcUMArMpggVY5Mfa2lPioa4r5zNPcxgVK9Bb-bnpUry73c-stjLuwihycRBw1lK8ZFO6gZU8uRkyxAroC4DlWQavWMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5327" target="_blank">📅 15:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">Check this out:
https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5326" target="_blank">📅 14:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aRN7BXShusbpAyOZhj7xXxp_7TDd1mm7yRP07lkWuatE9ZZepyuG1ZkEiQqmmmrSLPrc0dSVaAaAIo7jpf7FKWhU5KLdqKNTdy9QEF60U6LdNjyBSKAeJJt_KpNJ2VbWZuT0c4WAclHnGgsqqSkeRXoBimvvLPdPAbCxqBqdNH8pNDTdeRLGRPJ527SK9upY9MYWm0i6V5K5TdbjZuajZWaHodLDiFEQiX1YSK4OKrgqM7MaeS5h47VDH8Bd3ZjxGaPoOPRlvlUy8uw1tsVvlBWIkc7EqMuGG3kq2wpjJPHXMMJF3iy1WDTD9H3rPq5onOsDvVBH42kZ1Y2quBqhRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بگم از چه مدلی استفاده می‌کنم اونم با چه مصرف پایینی، باورتون نمیشه</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5325" target="_blank">📅 13:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فراموش کردم بگم، یه World memory هم واسش گذاشتم که کامل از روندی که تا الان پشت سر گذاشته اطلاع داشته باشه به طور خلاصه</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/5324" target="_blank">📅 12:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cPVHsA23GjZUJNysUzk2T3Vgx2Ya4Lnxjnz2HEAz5odZJ09-_1Lk9KvyXgvMEEXIz6IAVk1OeYJ_3G7Y2kQMlP06J59pdlj4c-tUp6b-IxN86cyaFbTlLo4n-6yKdqiPRsNkX8bp8pd3pmK3fcBvGUU7bSRv4EZhsR-of-92jI5eDWUVvxZ-B3TEKSbCSxjL9hmqyqbU8aEpWvpJOox4gHAwXsFC-9f8hzeDAiCSj02eb2sanpaeB86MN5E8IusSR9YhVwExXCF9Di2dn14e_03s0S9KuXPV3Gu_IQj9N0DtunxBkh3_hrzh9ue9Zgp3HcC-woWPHQXTEbISRFvH4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A_ApGjiLpGQ97-qH7MJuIiwWhWKA0mxirnnff_2DL7OZ7JwPLtf2K-Jp_nRkgOO-PaXqxZYTwNpsjpMfN9OzYvU2YtchW6G0FYtSWNHLVbv8PHfi49EXWT8NKMTbmuwHwk3jtx1vpDX2QQtmmA-tpG-JULnUNGYV7-OfLOyaT5ufjPmOhM8vuYjmZiPtiHSJjpqi6rFWCtEHqoxuKbZsT86sJ1ATV56MQkSPiiJDo7XxxC10k_pSNKwU0cNbmzPEVRoRkhNAo9Mz0FVdHMlrhGSL376hxNXXBb6lJrKV_VaiAp9iergr4A1BLVT8t6d-1DxzYJ2SGOAnlwYEe_K6Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bpdw5812EfpbbpZRpNB29kt0Rp0_6qdQ2H7eI4VZYxXIeg9xE2clHxTq5Q2S4fvdGB-F0sTgNPQQSxAynZ3L3fuNC0WE8dXU1MiQkfMAuNLm7WTlkyoRfIT8i5wPwxlT7uM_JZPbxZlZewUvABNybRhLSTKrX6yoHmUa6EaNlcLs4aOeBi9w7Cw4FlFc9t7ttspwJ7Y7sBEu1Uqu60sNRKyWyKx0kmPA7E-PzUIGs7lJw_FSOQG5Dy7fLXIwz8xLMAPUZMElfOMFc6EAUU26yDnxJjHG7EfzXdLnmMWbINgusZ2iY-8iQMbBRGXfT6Lhs0EwxlHwWxrS0FuEWDyDlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YVEsDrhlOZNI42DS0AFC1LVV0QSMr5SDgWSHjgz1UGzARIFI2axHE7iyJ8xCpns9xWQd5phoTi4ilEucQZjmZZlWVsUNTThgSVB53aYZMzMuczpCPcf-z0FKttuw-b0Y0EOJaW034nQzTezV7ffADCahFhnmAiMx0CK4unhzECnxddD9PsOZeykfrAawUs5PUh9g0H_2YBYkHyLfmT4rXdGUXRn2RbNeyq_38nlS5ZBIs9OQxH-1S8IIkxtVCRKcmY-3GVwRntXGhqNf9rGNYWo3EHNd5om6Sgl0c7weIAbDYWFt_bRCfc5jFqIl1nsAPG4GWPkbulm9TPa83p9jkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BsCc58sxAGSTjRqc0wOah1Q4PU3si-wNroasAtKN5erFvuLzk7ayvmq1VuL2Zj9xVZ1sAAnkFtH4uNLJeoUyEoeeilaQPaA-2SrZifm_wN2o2qp1uWndozhtMJNm1xsQECuGsCfvQxu4OIhwCaqfjynN1DuSeRZOctmiXZeiqf1vP9lvCEeHU3TUsK8_6Go7xz1fxlMvDWln2DHnmGQvtceMMrpeQGFm-T6O9TsSsc2jzpwoOL_wk_eDODT5zg8zTTZ94DCi3V9QGUxIg85RuWX1f9LJ6FjZ_Z7KiuVVxytyI9TMl1iCtDBfHkNaaVYh47WKMyXNnZQz_hAIOrJrwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gd5ET72g5u2VdZS8AQRpKCNwS1CvqL6HpMFgE806RBYrnR4PwAKnoAUT4NFo0Zjzh8bcHf9Pj-dNUrc-PUdQVV1XXZlvHr5aWnuXsYz_RSMFji8njhdm_r2SdV3i9GtJW4qC1_aQR764XOeBbuk7iZDwYwpL4SJyYb3jpEYBid-cqlCeNjT23w6ZUACRrRhuvDywa1jOr4Ti65Zf-CBE-wcQDIX-HoSw7eMH0NUAHEjUpBFKaC_JboixKD0vu-YZPsDtt1aFzMX4b_bTJyAvzxh1lyPPCMelKyhmBvrv5jG6QvemlMo6Q-qko5RYx4hpoi0COQA5OHXjLxcFHR13bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/poltgZdEPRj-5-rfhtEqUyRlEtVP5fd75NNIitKoOQl4CnB91VG_XsVXLzfpqRpOToZ1cbe8Y3DyFVvXmizDA6yiCd0A5IxMjzeqD-WMiGPe6QMybwuu2mH_CaMmqbtM2H4wjlcWrltHxHtrbkJv7OwNycfZS8PPz3zqXLi1Uvzfc7ppWs0Vy8pgEvKmx9jXOFgCgrsVTj16t-Z1GvW5j6Pk7jLG8Fji4sRxpL_igMh6gjfmUHOB2NOGNPKmaPlYzAShz0xUxgujpU_jjmUikWZWUUAazM8O_vkzngQQ5oUEqvU7weRRFZfBcx57k8BkLWsw1JO6S5bkzbHrJO-W0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گذاشتم قویترین AI دنیا ماینکرفت بازی کنه! GPT 6 Astra + Jev  توی این ویدئو، با همدیگه پروژه‌ای که ادعا می‌کرد تونسته ماینکرفت رو توی 8 دقیقه اسپیدران کنه بررسی می‌کنیم و خودمون بازسازیش می‌کنیم با استفاده از Astra و Jev از برادر کوچیکم دعوت کردم بیاد کمی راجب…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5317" target="_blank">📅 11:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rta8fbbRCff-GZNTvsc9_lB1CfllWauxpKmmWsDudC9guZo56OrJaoZ5I-IzQeba7H5nYjku0Mf4txX6Jo5f8pYB0EmN1bsKusuDOHrCZq5mh_Tis5uVq3b8t-el4Axg9F3aucrajaPeAE4eMc6vKIKf8ayr25YeSpVARrWsnQmOHYOtBQ14K4cPHz1S6QGUxLyOb7DpBHIr_VSnap3WN7iP-gdK2NqCmr9eNVe6GiOR3oYTXo0kZytW8WQjY2L4tshu94HgQHtJo-WORA8uzef0YLKpjTCXDUkZ9TTK9mFaujd0B13ZBiPcKMpWfhDWSyAJxwySlUVCeQpkpxiCbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کد Rust سریع‌تر از کتابخونه‌های روز، فقط با «سریع‌ترش کن!»
نویسنده‌ی بلاگ minimaxir ماه‌هاست به ایجنت کدنویسیش یه دستور ساده می‌ده: «این کد رو سریع‌تر کن» و بعد بنچمارک می‌گیره. نتیجه‌اش کدهای Rustـی شده که ۲ تا ۲۰ برابر از کتابخونه‌های state-of-the-art سریع‌ترن. حرف جالبش اینه که بهینه‌سازی سرعت توی RLHF این مدل‌ها جای اصلی نداشته و با guardrail و حلقه‌ی تکرار باید تکونشون بدی؛ پرامپت‌ها و خروجی بنچمارک‌ها رو هم کامل منتشر کرده تا کسی ادعاش رو بی‌اساس نبینه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/5310" target="_blank">📅 11:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فراموش کردم بگم که هزینه‌اش نسبت به Opus 5 کمتر شده.
هزینه Opus 5،
5$/25$ بود
هزینه Opus 5.5،
4$/20$ هستش</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5309" target="_blank">📅 00:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/twmWd89L9Wbh7VRGwKZNWLp1BZlqA_pgH2OkgyXrICHm0kbF8dPe8lH8P__ysussav0FObkQkDd40bWtHcVYYBG6Mx4xuOW2u8oXOAYCxjDMBDGtFOV8xtVSSvm3mNnqn-hYfb1OFfkOdHfjazwHlHxFXuXtR1NKx7iu35wl2uJMHa_sSgzuC7MhVUy0DUR6DhOU9UhcAlEnjd53aGxtoboulzVlVg99_7OOW-3rBWozz4blyBAo2zHPL6-1DtUroRyGOFAMuznG94xBy6bg8arz4Bd-XUzJj2f6wZK3aqHwigbvD_rS6MCJok5iAgYNBw1UhhFWGJBF_sZq_0eW9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5308" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p2wp_-nW0urWFTfe6IkrFfFzkTP07X6eYZSuMKYAwtOzMwfDfh_I5VydeRuGoIz8E9GEyVfEOvTOAoM7fY3hMl-kzXomwL_t-ND9VS7Ry1XWcdlCJQzl2xb6OQsPqt_JYQ84XS-1y1MBcgn6UvZKonKjaa3k0zWEGumy1ao9Qh_3rjCx-S7XJxM3AGLOVkBneF2xefwqS_LW3mVNj5ZJbV2zOTjZfa9U8Mxn1vCBBSAGip3OqDQgr_qERdHJWmEpkY0UZMI5bKKbz-yIWXMtLap4XmIwbMKZ6yNgVIef0pySCydqFzZ3KcDxTYLWu9sG8B-myVnd94QMPIakqlv4Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VaR2zMVIcovmVu6LL5OtroXi6UiKU9RziRKdeMA0pIgrG19K1Yi304aE23Lz7YoDjJUV6CIiar-C0pxwuNOjwSKGFtEYlRH5qQ73MOCVfLKNc9BwOUWENJARTGCBPnmBryDKcre-_cMshgwMIf1iqfXfUEcMfI_lyTyxKhy21FS4wzD9s4x5jKZnZXKiazv4ERbOZ-GeLNalIXKOrJxPd7UvVHvzYoZz00F9dHz9xU5zO77Ik5c9ZlgkqhhLPmVk2pKUtAIUhTCVLMVyfqV99OfIcR5hifTI_1xu5c_3_OB1kRWfMeIRVuppsDyOzO_SboOwQ79gFA6TamWK4J5onA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مدل Opus 5.5 ریلیز شد
وقت اون میم مدلهای چینیه</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5306" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RMG_gE1613ROb7BBBaAlpmpf5lQsO5Y8zhkY15yVFSsZLAxC6117tltwvof63OKtrNJG7kCM4QNDjeJBQb3K0YhCug4g6pwKN6fJUKn0JhM57Zfw8X4RcYe5-O5Dox_80oS9RSof83I529h9jnQHRSZFU7loGuWwe60DtLnSYSzOJ9CSdGs4yeE8uQGWFMyMGFdEuEhxS3vqLGPwZmUAyFqPEdga4vUZeJdlrPCJPkcEljArvX4t4riuDQFkWubW-oGz7E6-tJNQ2gV1dLc4S3Mjiz1ih7oNEfG7llXZuyDgBARvXlsGK2fSbF6e2UrsjAkdr-_O595ltTbuSQVMfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر روی 9Router ارور
HTTP 403: [403]: {"type":"error","error":{"type":"FreeTierError","message":"Error from provider (Console): OpenCode's free tier can only be used from within OpenCode"}}
می‌گیرید از اوپن کد، علتش آپدیت نبودن 9Routerتون هست.
برای آپدیت کسایی که با npm نصب کردن، از دستور
npm i -g 9router@latest --prefer-online
استفاده کنن، و کسایی هم که با داکر نصب کردن از
docker pull decolua/9router:latest
docker rm -f 9router
docker run -d \\
--name 9router \\
-p 20128:20128 \\
-v "$HOME/.9router:/app/data" \\
-e DATA_DIR=/app/data \\
-e JWT_SECRET="change-this-to-a-long-random-secret" \\
-e INITIAL_PASSWORD="your-strong-dashboard-password" \\
decolua/9router:latest
استفاده کنن(با پسوورد و JWT دلخواه برای JWT_SECRET و INITIAL_PASSWORD)</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5305" target="_blank">📅 14:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">این وسط Mimo 2.6 Pro هم اومد و grok 4.7 رو بولی کرد:))</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5304" target="_blank">📅 12:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/szL9tnulwz70mRBzmMNNdVj5TIdlPNzk8bSwpCkFniIE6I_QONB9vNoON97HU2Sbf1T08bUr54at_9-c-hlXsOdYLcGWa_LMXYUOV2_0pACQTr9d31V2Amlek7nBcJ9SkwjZYJ8fgWHIdYyqR5zOorMAyPg0GVY6VaCvYQuUtVz5I36zPAvJZPVcf_v3H7FTabcwNVQeadBXmR-F3Mqs_7GGgH8koXW147mm0NduCBq71TWy8WafOOeODqlCKwTN0EGje48CsC2IpvTVAfQFT_TVkPG6bxXdDI4EPn8SFzP19DC0598D-9EvzaxVGDajbIdhIQ14GbOrVV8OuIfOhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا منو پولدار کن یا متین ویدئوی ماینکرفتی بسازه:</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5303" target="_blank">📅 11:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tO70zwwch-H9PkiJ7RXH_B3y8c-jdybMS22AVlyzY25ikbtSTf_m5WdCJXPIjZBVhBBvouJo3gUhudIXDqzc24x_HntW_hCMz_cwwKJxiZVMZGAPvM6_D2njw3T39xZejNxkgpIgAUhLN5b1WARILwwOCWk-u5T06RYpDnla8L8RA8XsnFko0TdoM9DlhhBlJK0gIKvhJoiLJNb5BUBT27fslIl3tyuVhaKh3uP0XL-62O9DW9VgHFTunj896TI6seu8-h-B3ajBQIeZVLq-nI6IYnsBNH3TdwDo81XnJo5NGH3TSShRBOdXHEg26OcLlJnFqi575zWxb9172SIfZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گذاشتم قویترین AI دنیا ماینکرفت بازی کنه! GPT 6 Astra + Jev
توی این ویدئو، با همدیگه پروژه‌ای که ادعا می‌کرد تونسته ماینکرفت رو توی 8 دقیقه اسپیدران کنه بررسی می‌کنیم و خودمون بازسازیش می‌کنیم با استفاده از Astra و Jev
از برادر کوچیکم دعوت کردم بیاد کمی راجب خود ماینکرفت توضیح بده و کاری که ادعا شده ai تونسته انجام بده.
همینطور در مورد Jev صحبت می‌کنیم و اینکه اصلا چه نیازی به این معماری حس میشه در کنار LLM ها؟
و می‌ذاریم ai ای که کدشو نوشتیم، ماینکرفت بازی کنه برای خودش ببینم چه اتفاقی میفته
😂
لینک سایت Typesafeai برای گرفتن 5 دلار اعتبار رایگان:
https://console.typesafe.ai
لینک سایت هوشیار24 برای تخفیف 90 درصدی API از GPT 6 Astra:
https://houshyar24.ir/?ref=B2N4W9SS
پروژه رو هم توی ویدئوهای بعدی که تکمیل‌تر کردیم می‌ذارم گیتهاب واستون
🥰
📹
تماشا در یوتوب:
https://youtu.be/l-o_fQM_9AI</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5302" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مدل
Grok 4.7؛ آپدیتی که بیشتر ناامیدکننده بود تا پیشرفت
ببینید Grok 4.5 نسبت به قیمتش واقعاً مدل فوق‌العاده‌ای بود؛ سریع بود، کارکردن باهاش حس خوبی داشت، قابل‌اعتماد بود و به‌عنوان مدل پیش‌فرض عملکرد خوبی ارائه می‌داد.
مدل Grok 4.6 از نظر من یه قدم اشتباه، البته قابل‌درک، برداشت. کندتر و گرون‌تر شد و برای انجام هر تسک، توکن خیلی بیشتری مصرف می‌کرد؛ درحالی‌که فقط یه برتری جزئی از نظر هوش داشت.
البته دلیلش رو می‌شه فهمید؛ بالاخره تیم سازنده باید خودش رو توی بنچمارک‌ها بالا بکشه.
اما بخشیدن Grok 4.7 خیلی سخت‌تره.
1-
مصرف توکن برخلاف وعده‌ها بیشتر شده:
گفته بودن مدل جدید توکن‌بهینه‌تره، اما توی استفاده‌ی واقعی بین ۳۰ تا ۸۰ درصد بدتر عمل می‌کنه.
2-
بنچمارک‌های ضعیف‌تر:
توی چندین بنچمارک، امتیازش از Grok 4.6 پایین‌تره.
3-
سرعت و تجربه‌ی کاربری بدتر:
کندتر شده و کارکردن باهاش دیگه مثل نسخه‌های قبلی لذت‌بخش نیست.
4-
هزینه‌ی واقعی خیلی بیشتره:
هزینه‌ی استفاده‌ی واقعی از Grok 4.7 بیشتر از دو برابر Grok 4.6 درمیاد و حتی از هزینه‌ی Astra هم بالاتر می‌ره.
با توجه به این‌همه تبلیغاتی که برای این مدل شده بود، باید بگم واقعاً ناامیدکننده منتشر شد.
البته بنچمارک‌ها همه‌چیز رو نشون نمی‌دن و Grok 4.7 توی بعضی کارهای مهندسی واقعی همچنان تجربه‌ی خوبی ارائه می‌ده؛ ولی درمجموع حس می‌کنم هنوز خیلی به مدل‌های سال ۲۰۲۵ شبیهه.
مشکل اصلی، قابلیت‌های Frontendـه:
عملکردش توی کارهای Frontend به‌شکل غیرقابل‌قبولی بده. قابلیت‌های 3D تقریباً وجود ندارن و مدل دائماً توی حلقه‌های تصادفی شبیه Gemini گیر می‌کنه.
حرف آخر:
این انتشار واقعاً ناامیدکننده بود. امیدوارم تیم SpaceXAI این موضوع رو بپذیره و توی نسخه‌ی بعدی بتونه دوباره ما رو غافل‌گیر کنه.
✍️
theo</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5301" target="_blank">📅 10:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BiUXRt7soZFlvI1yFp3XJSJIQedmNdFB9CA8iuRvbelJdD8G7hsqI3zu4jgZs6jQdDCdgRaMdB2Xud0k-FVX4LycdB_GtoGDLuPJX6c-ZiySimsyijTgEk2C4D7E4x_y6bCjWMVOtq3lgJ3dvq2xYlhDBHmzFoxHo86JU8Lg1IdSkYbzcToM4vzfR4IBeBGdeWPse9ay3SrDQrVDjd1chYI37ujRUDdyMKC0RcFozQChUy8CDN7p83hi1Y8gd016QHb1eCK1eyP_5x1NATylM5_Chhvdp4sY_xICny8Muc2-hkH8cjwdtOFz2QNCPZPFQvr0wLUWV22OoG6H97KgsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره. ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5300" target="_blank">📅 00:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t-W2UxVMXr60Bb9gc1a2WG67ej3QCpyXHz5QfOTugDWoVZwC8verlqvQm-_e-Tk2gXHvxpWgcpmG6RJdB3mhczri4M3HMljDdtHMSciekuiE82uQ9ksDAKQvmz4a3pbYSSsw7Fmi_zf1b1MkOo_a7vybqwYQi2lPdWokbpHe_x6Ir1usprgtQeW9ibMKSuCV2KJ-dpSPHj4YvBlSIhVtWDa3tJNwHu_NkpzrLTSzzY20l43w139znl1k7YysxTCSVnTMTHdXxMmbU_jjTnJvf9I6SuuON0CNkDmJuPht11LD7UcNLvxCe3ZRucN01N2UMW3xEPwzgansZnkCriS5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aOwP4i-w20DG2xXN5ryXkjb74pfBlAHX50k-dJLw_W-NsE6ebT1SskZ8lt53svHFUnwQBiLF2zWxbJG_zxopbdEFxcVIwoinYOpvBO05rXTTDqTEgiM3ZQipOTcoWaDczMnoyM_LBZO3Y1fjU8ew_j5CSfxUf19nOVDzIFrY3qg0EXwON6P41BN2z0esHATUuzq09P4QZB3C8vv8V9H55_4rhFdrUdxga2phtPy2q81uC7RWA62ZTi6XxSuz9Z0BKue9KoqQlM0Cj3zdA643tySmGHsQDKhn3rLSngdaJ9q2bcvpG03YND3Sl9GVEED1Muw3aXAfMwMCgWTQeEccIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این وسط Grok 4.7 هم اومده، توی یه بنچمارک DeepSWE الکی بولد شده که از Fable 5.1 قوی‌تره، ولی توی هرچی بنچمارک دیگه بگردین از Muse Spark 1.3 هم ضعیف‌تره.
ایلان ماسک فقط بلده گنده گنده حرف بزنه و تبلیغ بخره متأسفانه</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5298" target="_blank">📅 23:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد: https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5297" target="_blank">📅 22:49 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G8VjlXQHapGnoJfqfgkOjc518olXfAzOHcGipo9I_Xdms_zHcDCGNkTzCsWvAPvHBNX8paXDiDAyqRtSZEyVgUpn7GmHdgoiydgsAvhdvYrz48CgZq0I1yJWGLyYpenUm_vOH7g-lZulZWqDVUD1BTMgD90T-M7_XG48bwKdDtGI6yeD6zHChoDNNeB-pusKDReAGSAkEahciqRmE3Win25aBghAge4ubCyroQVBvo7KxYjIBWbxC9ZOlip3Ocilj8qHy6tFoaQSgdYewDhr4Zd_b23NTKm9G6x5GyBJsFU08pSZr4wnSwp_RyA-AScrU2G6qvdS2y4U-dd_uG0YZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپلیکیشن ZCode، هارنس رسمی مدل‌های GLM و شرکت Zhipu، اوپن سورس شد:
https://github.com/zai-org/ZCode</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5296" target="_blank">📅 22:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/wA9VGV2UFcR7YwM-Q3M000zDic3ydKj_KQJtWC_USE6AqnU0sA61DHyKQlsR-nzeZ5pkIoktCde_zHBEMI1uH9-EP6J858wM2ufnstnPTWif7hyOaPRIbrNj2OMsPG425mrrW8u3wm9nm2G6hNEp-x5ZZOienZTkWRgDpT468FHF30Orci7coRgz8pKRa7OlHw0kutR1MSq5bJ8sja2MFkhT81bgyRKg7IESX5DI8TT-37EIwr-RlCW93w3YcQtphY9cxWP_fLdnnuqrLt0i2IgG7VDiK8fddZZbW5vgNdrkCGbt12NmebbmuJTKwliR9serKjxyDXMp8CTee4IkEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی مسلمان
اصلا هیچی بهش نگفته بودما، خودش یهو اومد گفت بسم‌الله</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5295" target="_blank">📅 18:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5294">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یه نفر یه چیزی ساخته بود
من دارم یه کم خفن‌ترش می‌کنم که ازش ویدئو بگیرم
بعدشم اوپن سورس منتشرش می‌کنم
مربوط به بازیه
#️⃣
از اونجایی که 3 تا 5 هم برق میره، بعدش ضبط میکنم و احتمالا تا شب آماده بشه</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5294" target="_blank">📅 14:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5293">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5293" target="_blank">📅 13:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اگه اولش ازتون پرسید Can you chat with Jev
باید بزنید No
چون طبیعتا LLM نیست و نمی‌تونید باهاش حرف بزنید
یک مقدار شاید پیچیده به نظرتون برسه اما به زودی راجب کاربردهاش صحبت می‌کنیم و ویدئو هم داریم</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5292" target="_blank">📅 13:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h2e2kTSs-yH7sYa90EPch3rZnPgTKHUVJMlqz5b-c-83RBFJ_cKrLsnMkQv_u-UrQubPaQs5fTdAsO0WStIDg7kjtKdF2rAYft9XFg9nRfCUSMBzFE4B8jB889WC1tDDHy_KTzkO4yhXcLl-UHQMNvDOf7FMsTN-oapa9zAupN8i21fxlT67aUf87rL7bIEcOoKMEWgE8oxP0ycy9PgTnGxUgy_rvhtbEuiDV8dB3zEnKsPotzSl0N3tiqA13bZYa0nJMnKNQDfvwFv1q3Fg9SDbwQWrUWzC7rFz8GY1bNx6GiiwRvwBZS8lFMtPvCI4ySLKceij71onruZXAFfUSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی بامزست:)</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5291" target="_blank">📅 13:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دسترسی به Jev برای همه با استارت کردیت 5$ دلاری رایگان شد: console.typesafe.ai
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5290" target="_blank">📅 13:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gXgszZfthwNP3quGb1a8LsyWVVgHvemd9y0Nds9gRglSrw3HbgvjhLy0jZwcUgINdnlzLkLoI9yBc-QOBj1kD9kDYqJRWNW-lb7Li8ZNjQSalSZwWkUoW8KOe-Bp-R44_qjva5-SvkM6he6nKsOS39usSXDiJnxeZF-GNVomh6IWI9QJiOnwVo5mA-l1dKw81iIRUdedUwnhu7-Qlc4FLhvl9JqYbp8IS2TE8ZUdDmxAJYtUxqUMSejJYWpZrBQeSy-Ni-7-VwktCzuqPQhjUfhfdIUqyKFihLh-VmMJwTplkc8wElwSHDpsosWeUDVtq2oyxYCnSVxGvYTC8RjEow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad) برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5289" target="_blank">📅 13:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromgooyban🦆</strong></div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5288" target="_blank">📅 11:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5287">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f3TDdN5I66l3hQVKNTU4uE7I8mE-NdRd_CMJZnS9um18I9O6gdXyBwKGya-AG0CMFZAmATs4ZzS6kNBCiNCzFsYYdTGwhD5p6vQCSnAm1Qn6tZjSPNqJLnaQTonhnmDFecqZHPYEsOcwAIe1J5CbwmeGc2dE6MtnGHjV7yv-UVTJdbXEv_yUWCaLVuAy7GT3j52QxbCwIHUFCBN-Ko3LT1ymDh4jaVc5G2pe-xyxH_XPsaxRYJL6gffSreA8bdbPpk-VrpuX5mfzIU5iFNY40o5AZhMBvgp9cgV-8VYaiT8gO8Dx-fpY-Y-eH-3hAgtTcmsJ3LOAFd_7lHyFA825DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه‌ی کاری که Jev انجام میده
😂
(سریال Breaking Bad)
برای اون نرم‌افزار بررسی کامنت اینستاگرام صد درصد میشه ازش استفاده کرد</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5287" target="_blank">📅 08:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JHEitAgRpegWwO9jCAzVUOEyMLpDrEDwV3RCZcpkfYuJGGFnkJX0q0WnTc8a2f-tkL1AxmednROYeNosqX5Cpl4O04XGgR12gvbEm3PdqyDOOc99iP82drRaxJblLlxsk4KTzabe0rbrxh_gfWf41iGB0rEOGWmvFkf83QqmxmLiPOJke5y4MLlQI6mn172FVxXA-6spZIlwycC88Dliv5gUAaoA66taPKXCNnY77mxrmGPLpDOewm3mivWBxHa98gaQJhsqhIHhtuz5dt518CgqROIh_OLMM2Tqz-tl_9QSTYVE5hBjr0eyXaYVavCV7CVxMe4iEOU3rma8or8rnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.  خلاصه‌ی توییت این دوستمون:  - یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه. - هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده. - اما Jev اصلاً متن…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5286" target="_blank">📅 23:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">هوش مصنوعی جای ما رو می‌گیره؟ | آیا شغل شما در خطره و راه حل چیه  هوش مصنوعی واقعاً جای ما رو می‌گیره؟ توی این ویدئو به‌جای شعار و حکم دادن به قول یاشار عزیز و با کامنت دادن روی ویدئوی این استاد بزرگوارم، سعی کردیم با یزدان عزیز با استدلال و تجربه‌ی خودمون…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5285" target="_blank">📅 23:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AoRW-sDVPdXuBLjinU9IYC3WgijFqtifBHJMay9LTU9HxNh4tfB5eUCTXJ8kkgdR7yOl3J_VmyZffYxy42XI7b9LAxEQmC_fxt2327JdzAgCKQJhtVWRijTGjhxjaPcMLUgEurmxTRoqr3ecqYSe8fE971-xLGRu0lvUdNZZ7JgU4G4AX0x2odJEwhopssb9mpYavqhM0ijR8WxBIf10gxOXRjMNvJtc50BNrvmFmPg6Jj1MMTjNsGha9ujKOwtQq6N2sgc3RI72VhcmEYq_vSntgB_tyqX2GrtWBPCCPQREqtGJuoALDGMyz-ryIcaOZK3j65LfI9e8GK_QOSkqeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی جای ما رو می‌گیره؟ | آیا شغل شما در خطره و راه حل چیه
هوش مصنوعی واقعاً جای ما رو می‌گیره؟ توی این ویدئو به‌جای شعار و حکم دادن
به قول یاشار عزیز و با کامنت دادن روی ویدئوی این استاد بزرگوارم
، سعی کردیم با
یزدان عزیز
با استدلال و تجربه‌ی خودمون به این سؤال جواب بدیم. چیزهایی که بررسی می‌کنیم:
— چرا بیشتر بحث‌های این حوزه توی شبکه‌های اجتماعی «حکم» بدون دلیله
— فرق AI با یه ابزار ساده مثل ماشین‌حساب چیه
— تفاوت نوآوری (Novelty) و خلاقیت (Creativity) و اینکه AI کدومش رو داره
— جایگزینی شغلی و تحلیل آینده
— چیزهایی که هنوز دست آدمه و AI نمی‌تونه جاش رو بگیره
— بحث کاهش نیمه‌عمر مهارت‌های تخصصی
— ۵ تا کار عملی که باعث می‌شه بازار کار هنوز بهتون نیاز داشته باشه
📹
تماشا در یوتوب:
https://youtu.be/x8V0w3I9g10</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5284" target="_blank">📅 22:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ti7Vv6lMTTBsWqBZ6Quhbm1-3dFU4NcqFXGKjGQ0IhseRjl14B8ZqelV1mg9N6HbweBHNoGMCdbDCHeq-XxUXumfbzBPqBkVOfvgW6H2wMC-qHVYp58xjAcvoqBCDT6v14zHAq9NhGdwoOBO_lJq2hi8kPgxyvYpHPeGI8iDpmHE14KaHpVPGNc9YvSIe8VibBpkhf9PhFq-XaGGmbcIh54pFw3bbdAea10sOsh8YfHeeLYOKhPah-Y5CnH0gkN-d77IBDZ23Obwzf27TX9TvVru06SVc7Iljy5T55XWVQadjS7VfsJlXLXz0GWSKYKWgyN6yvaULo2-EGZJRr7Z5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍓
بچه‌هااا یه آموزش جدید آپلود کردم
🥹
✨
اگه Gemini خطای 403 میده یا Google Flow براتون باز نمیشه، این ویدیو رو از دست ندین
👀
💗
توی ویدیو از صفر Blue Knight Panel رو می‌سازیم و آخرش با کانفیگ‌هاش Gemini و Google Flow رو تست می‌کنیم
😭
🔥
🎀
تماشای ویدیو:
https://youtu.be/GK2PGDzkbh4</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5283" target="_blank">📅 21:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5282" target="_blank">📅 18:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=PDEy9Jwp_Gc87QGUe_SXy_HXrThnRNLK1csQs2y5b59dyL41fDN8M913Z_qVSvocC0J2_hoySMx-E1kp4Mtp84D9fKnKO7sYJNOov_p1mK2ZSsiy7FJPa8JuNgs0UIqWVrletPNRViufY7OcZ_GYtviuIIwujk0GVnRahZa8A75fispjtwWivYt8XDuZMCKJQ6-GUnWtrA0rhJPPO6er2xtOY5fHLLQfPnJSohqlpYjxMDbdGwU0VLNkFP9TtP5_csl7mg9H0LWFiW0Ox2t0OxgtY--nKYL2GIjrbAY2XDTA6JZ3AzkwKAS3IMn_KKvEdAiJ40D28_JWCbT5GEMQNIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/210d0bc611.mp4?token=PDEy9Jwp_Gc87QGUe_SXy_HXrThnRNLK1csQs2y5b59dyL41fDN8M913Z_qVSvocC0J2_hoySMx-E1kp4Mtp84D9fKnKO7sYJNOov_p1mK2ZSsiy7FJPa8JuNgs0UIqWVrletPNRViufY7OcZ_GYtviuIIwujk0GVnRahZa8A75fispjtwWivYt8XDuZMCKJQ6-GUnWtrA0rhJPPO6er2xtOY5fHLLQfPnJSohqlpYjxMDbdGwU0VLNkFP9TtP5_csl7mg9H0LWFiW0Ox2t0OxgtY--nKYL2GIjrbAY2XDTA6JZ3AzkwKAS3IMn_KKvEdAiJ40D28_JWCbT5GEMQNIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو که دیشب گفتم واستون می‌ذارمش، توضیح می‌ده که می‌شه حل‌کردن مکعب روبیک رو با
نظریه‌ی گراف
مدل‌سازی کرد.
- هر حالت ممکن مکعب روبیک رو به‌عنوان یه
نقطه یا رأس گراف
در نظر می‌گیریم.
- هر حرکت قانونی، مثل چرخوندن یه وجه، بین دو حالت یه "
یال
" ایجاد می‌کنه.
- مکعب به‌هم‌ریخته، نقطه‌ی شروعه.
- مکعب حل‌شده، نقطه‌ی هدفه.
- حل‌کردن مکعب یعنی پیدا کردن مسیر از حالت به‌هم‌ریخته تا حالت حل‌شده.
توی ویدئو، سمت چپ یه مکعب روبیکِ به‌هم‌ریخته دیده می‌شه و سمت راست، شبکه‌ای از نقاط رنگی و خطوط مختلف. این شبکه درواقع فضای تمام حالت‌هایی رو نمایش می‌ده که مکعب می‌تونه با حرکت‌های مختلف بهشون برسه.
نکته‌ی جالب اینه که مکعب روبیک فقط حدود ۲۰ ساله که اختراع شده، اما تعداد حالت‌های ممکنش فوق‌العاده زیاده:
۴۳٬۲۵۲٬۰۰۳٬۲۷۴٬۴۸۹٬۸۵۶٬۰۰۰ حالت
یعنی بیشتر از ۴۳ کوینتیلیون حالت مختلف.
با این اوصاف، شاید جالب باشه بهتون بگم که برای هر حالت مکعب(هررر حالت) راه‌حلی با حداکثر
۲۰ حرکت
وجود داره. به این عدد معروف،
God’s Number
یا «عدد خدا» می‌گن؛ چون از هر وضعیت ممکن، یه حل‌کننده‌ی کامل می‌تونه توی ۲۰ حرکت(حداکثر) یا کمتر به جواب برسه.
پس حرف اصلی ویدئو اینه:
حل‌کردن مکعب روبیک یعنی پیدا کردن کوتاه‌ترین مسیر بین دو نقطه توی یک گراف فوق‌العاده عظیم.
این نگاه ریاضی کمک می‌کنه بفهمیم الگوریتم‌های حل مکعب چطور کار می‌کنن و چرا پیدا کردن راه‌حل، بیشتر از اینکه فقط به حفظ‌کردن حرکات مربوط باشه، به
جست‌وجو توی فضای حالت‌ها
مربوطه.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5281" target="_blank">📅 16:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=rUPdRCnLwvWYU5e3y6ukJWr3QwdEmf25bPkMNBk5WXNhTHIVj5d4jGVRX2WyNXp1pCCIbSJzMvtXEE9E0IanJUSO1OXG1NGq8x7qudAIyYKgkzbw3esb9KazA6Q-VKKKhnRshmeuwFkCSxPmAqYghm3rtgrePiejMosIsHxCRHbKBiACL9E-0EavBGZu63ALoTzDOQyWFXxcOehc3ZuN6mgT1_-TSZpzQ0CEj6rROcDnoWzQ8_Nyzr7zypkWXGVQFri8ser-yuBENvZ2TYDWt4k3x_QoIiDZU8D0LGQeLeoDVDpDlYrG8mOBciBde0mFsmq8j3kOSAiMKEp2dlwyEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/25a6d04619.mp4?token=rUPdRCnLwvWYU5e3y6ukJWr3QwdEmf25bPkMNBk5WXNhTHIVj5d4jGVRX2WyNXp1pCCIbSJzMvtXEE9E0IanJUSO1OXG1NGq8x7qudAIyYKgkzbw3esb9KazA6Q-VKKKhnRshmeuwFkCSxPmAqYghm3rtgrePiejMosIsHxCRHbKBiACL9E-0EavBGZu63ALoTzDOQyWFXxcOehc3ZuN6mgT1_-TSZpzQ0CEj6rROcDnoWzQ8_Nyzr7zypkWXGVQFri8ser-yuBENvZ2TYDWt4k3x_QoIiDZU8D0LGQeLeoDVDpDlYrG8mOBciBde0mFsmq8j3kOSAiMKEp2dlwyEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو درباره‌ی تفاوت اصلی بین LLMها و Jev هست.
خلاصه‌ی توییت این دوستمون:
- یه LLM معمولی، متن یا JSON رو توکن‌به‌توکن تولید می‌کنه.
- هر توکن به توکن قبلی وابسته‌س؛ بنابراین مدل باید برای تولید جواب، چندین مرحله‌ی پشت‌سرهم انجام بده.
- اما Jev اصلاً متن تولید نمی‌کنه.
- Jev به‌جای تولید توکن، مستقیماً از ورودی به یه ساختار یا خروجی مشخص می‌رسه.
- به‌همین دلیل، سرعت Jev فقط به این دلیل نیست که «سریع‌تر متن تولید می‌کنه»؛ بلکه اساساً فرایند تولید ترتیبی متن رو حذف می‌کنه.
- نتیجه می‌تونه پاسخ‌دهی سریع‌تر و مناسب‌تر برای کارهایی مثل خروجی JSON، ابزارها، ایجنت‌ها و پردازش‌های ساختاریافته باشه.
به‌عبارت ساده:
LLM مثل نویسنده‌ایه که جواب رو حرف‌به‌حرف می‌نویسه؛ Jev بیشتر شبیه سیستمیه که مستقیماً ساختار نهایی جواب رو می‌سازه.
البته این به‌معنی بهتر بودن Jev برای همه‌چیز نیست. LLMهای معمولی برای مکالمه، توضیح‌دادن و تولید متن آزاد انعطاف‌پذیرترن؛ اما Jev برای خروجی‌های مشخص و قابل‌ساختار، می‌تونه سریع‌تر و کارآمدتر باشه.
✍️
ترجمه و خلاصه از
akshay_pachaar</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5280" target="_blank">📅 10:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QMkL-miIb0eTp1roLnMYuWAtOs7p5UbsczqoMKOzLpDgaM2IK0hgffBwSimPinqb2OUvFRNEdRUluoewKnorme6C4Rsrgmq8Z-KHs86sTY_DWQcw3eGWZ0PT4PdWCl3OcwEdNBAuH9i7laioQtPssxlA9VsusIBV1Y1bPx38BdNi0_HSkn2pnsbQB0zDdLelEU5Q7iNKYFBJrFXM83_thJoiIo4lOT4zc7uV7XJr9B5fhSOhxSU_JaRohOOlXiA_zsQnAzNVSTVUp2mLKPPwfd-uGkF9k5SQxtloRzq5etfEPDjwuwgIb5GkTz3fvsLnNSHac94PS2pYIdpol_3OxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم توضیح تخصصی تر: https://www.youtube.com/watch?v=vj7hysh0mOI</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5279" target="_blank">📅 10:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eZ-jhEwgBJFug9kRALYD40Mt25Syglm2GsBLcOkhMc-n-RRXAQrYFPd5sj0hDghaBuQ87N2hbGxCUjcg49Rdz-9fMy7JmBJZczfTlVTV4ny3dI8adlSCeI35LY_cNjBTTU2814kZJaCbv6NblTVrjJ-cSo1M-jOCSSYPu5cQVz-Dbjzz3rNtZ872yavZYUbo25olO-401s0yRxgsyoLsqurwNw2uCbOfgnZs21qCicj2eN6ujyH-YApEjxC-xNAeHsaxQSvEZtkj9H2JKJOdyDPTQB2UNysFLytDmgdFUe4CE6cik2UTOZwlOASBG3h06D7oT2-giVVccfswNtsJzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیلی که توییتر رو دوست دارم:
(اون روبیک Graph خیلی خفنه فردا می‌ذارم فیلمشو)</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5278" target="_blank">📅 23:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">به زودی برای پروژه‌های اوپن سورسم هم آپدیت میدم بچه‌ها
هم Aether gui هم اسکنر</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5277" target="_blank">📅 21:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کسایی که ری‌اکشن
😁
می‌زنن آخر این ویدئو مسج رو دیدن
😂</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5276" target="_blank">📅 20:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=kuBrjwZ1NX8PSxzooUV4uAmr-rllg_1S7lnKc7IAN4C9v-PJRhazqiAjybP7vciefU1AuAamsrZ7j7AiAuG-VzxUayM0HNR23Agi13Jtk9ytRLssXkrlHDwcmz24Vjk8LsND3Atkt1K84sjwARpKKQblC_ToQzxowK0HkM7-FGzXbk6BU7CuyR77sxZsISedTCHX-OwOq0huthyaU4aLJsfDjTT5XSVRd0wfMXhiarRgYLCdOXiBZM2fQO4Wk1_w5ZTcgVoQY9W6jGChqTaodBd2SStKvCfAuoHjxGouU7IMYaX655b2oneqXmvi7GMBdpH2kVAjwuHvnywVGqwJFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=kuBrjwZ1NX8PSxzooUV4uAmr-rllg_1S7lnKc7IAN4C9v-PJRhazqiAjybP7vciefU1AuAamsrZ7j7AiAuG-VzxUayM0HNR23Agi13Jtk9ytRLssXkrlHDwcmz24Vjk8LsND3Atkt1K84sjwARpKKQblC_ToQzxowK0HkM7-FGzXbk6BU7CuyR77sxZsISedTCHX-OwOq0huthyaU4aLJsfDjTT5XSVRd0wfMXhiarRgYLCdOXiBZM2fQO4Wk1_w5ZTcgVoQY9W6jGChqTaodBd2SStKvCfAuoHjxGouU7IMYaX655b2oneqXmvi7GMBdpH2kVAjwuHvnywVGqwJFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5275" target="_blank">📅 20:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">از اینجا می‌تونید به عنوان میهمان وارد شید: https://live3.eseminar.tv/ch/wb182512</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5274" target="_blank">📅 19:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5273" target="_blank">📅 19:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=VL0LySA1lag5JIeg0MvNYaBMJTLhJfbrf1hluwzn15x8YOuE2-x_xIgUqX8VGMBYT02dysIeIfRzUNaDVqUJw7e-SrRQdRRmgUF6KiZ405s4Q-Z6Lb8PO8DLKHmzcYnxlouy9bbsevEZH1c1oIuo_6aDOtBl12b_oUXX_1cmYzBgqd5dj-EvqVvLjfdD93eqpzIuKmrzECSTeAacJKEMvCX5-t1AD4_0XMKktgf6TKAbVTadHwexMzf8ffDalanHXUz3iKblcQhIJmtb7Vi_52Iz3CZr1YKLNp8L-OOEU0UXkmtRx2JS-bbiAVMdkzgkvBoUsAuz5rRozIDjSJektHl7c6DUpIFTyLna6blGOY7BVQLv1n14CgIKgGWk83GvXV7Wy17kvVkZ8Qc_f8JikiUbbnwi76ibdiPL3S24DtrER8s1gLZBa1d8hQqE6ChiNwX7Crpb4hqR6iLzgFYzLGXoxvwk4a0aUmmUHBBmQckN1WKsLFVNZmUGBaA0F62ofAYs1YS7o4-stteWQdhWkcrg4IrA8c2Ex7gT4PD5jyr-dKuH1fBlSW1TOd81veOuTnVBT42iN2zCQ1S3KdK39Ph6e3v7noASUc19jSgyGB4PxGTDKnjR1DfwMbZd94v5SoT5jYBS_AU5OMgDIZu85Fkf_2kIkq95oGbyP0LnxgU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fab9ee691.mp4?token=VL0LySA1lag5JIeg0MvNYaBMJTLhJfbrf1hluwzn15x8YOuE2-x_xIgUqX8VGMBYT02dysIeIfRzUNaDVqUJw7e-SrRQdRRmgUF6KiZ405s4Q-Z6Lb8PO8DLKHmzcYnxlouy9bbsevEZH1c1oIuo_6aDOtBl12b_oUXX_1cmYzBgqd5dj-EvqVvLjfdD93eqpzIuKmrzECSTeAacJKEMvCX5-t1AD4_0XMKktgf6TKAbVTadHwexMzf8ffDalanHXUz3iKblcQhIJmtb7Vi_52Iz3CZr1YKLNp8L-OOEU0UXkmtRx2JS-bbiAVMdkzgkvBoUsAuz5rRozIDjSJektHl7c6DUpIFTyLna6blGOY7BVQLv1n14CgIKgGWk83GvXV7Wy17kvVkZ8Qc_f8JikiUbbnwi76ibdiPL3S24DtrER8s1gLZBa1d8hQqE6ChiNwX7Crpb4hqR6iLzgFYzLGXoxvwk4a0aUmmUHBBmQckN1WKsLFVNZmUGBaA0F62ofAYs1YS7o4-stteWQdhWkcrg4IrA8c2Ex7gT4PD5jyr-dKuH1fBlSW1TOd81veOuTnVBT42iN2zCQ1S3KdK39Ph6e3v7noASUc19jSgyGB4PxGTDKnjR1DfwMbZd94v5SoT5jYBS_AU5OMgDIZu85Fkf_2kIkq95oGbyP0LnxgU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه! به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید: https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5272" target="_blank">📅 17:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه!
به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید:
https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5271" target="_blank">📅 17:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qNwKwzyo59hS_VvNmHHUSeXP5i6FyLBPxDFDQGLTAJF4y5JdPU_vG63XjyTM5daeUElSGXnapipUCr2_taHidE3Cxv3BolXZS4vrKVZhZDxfO2sau3In4vZZ6Z0ihw9XaJLVUSyJ2MkK_AQjmZB4MTqQfyIVTFoj87wOwXghVi4aMKQSih31j2qbVQBC-j_yrxVmBA3eQ6ZIs7nPH8lc3IneQfwOFNrLXzXaBSB5MTMmi9LV0xaQf9-RJECY0fEO9Vx_GTW8Z-tI1u0pp8a8JVJdvmENe1FymqqVXfroGBbpDiCCe79_aCdIREmYQMUQMtnB_EpGQTf1z4vjd-6f_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aj9uOYUID6uOcC6127g4VJeYUNOF-tEOJG2g7sPwOjCnxavQETSLrqNM9J0X6HYWPBTwBlLjhOyyMgqutMUNVzvgn2thmXsd8UOLgUdGmJVAjRngFsIEmOR4h4c7v20IKM770kpWfj8Bxm3iok_ViEI4pZMR67baRhGrpF_CddK1J7lVbgMEoW3PreHwnP-pfbBG_irtIBU6cnhnpcJ07eZqhuaqJ26Z1xpvdK6ltTiAQFx9EE6JsaFvwN2uGYzwukPk5vOhH4dx2uEoC-7lClA8lEeTzp0dhlTMK7PIB6F6cft4Whqp4FM99nkOm05wdWBP0zRO3RDTopNYDm-Sjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا درآمدزایی طی می‌شه</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5269" target="_blank">📅 16:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jtlALwtDEosrvJ6yu67UhOvFlAVaIUcMVZsz_J7y0Zd0WtK9t6yOZiAAA8CWimqc9dvik_YfSU8TKj9s1kW8f3IkNudZYmoJwQkyiCovDw4iAJEOb-GhepfjgZ8H36fQYljafK9r1cYDOCp26aWdtL4d6n0u7r8VQqjfOHsSAnBJM-AeBUCpk03lBsNLGRc58lcd24eTRMuTOFmOyWObeFkF-9XRpq_xE0VGRPWu__een1nppqHdYXkNdFxPbB_CLZ-zoj51E8cVVfSgsZzZzwn2C9OEFATW1vSegsD88jzxR00Ev7ZiXvKGk-kX9yivOt1Sdy2YJCERDZlG4jHtIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت
Z.ai
مدل GLM-5.3 FlashX رو عرضه کرد؛ نسخه فوق‌سریع 5.3 Flash با سرعت 200tok/s!
​• کانتکست: 1M
• مالتی‌مدال نیتیو
• اجرا روی بیش از ۱۰۰ هزار تراشه چینی ​انتخابی ایده‌آل برای ایجنت‌های کدنویسی و تسک‌های بلادرنگ.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5268" target="_blank">📅 21:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DAgHuTPyDa_HNv0u_QCi67PlphXiy_KMCpFYdEbht5aF0j1Y-EAxFAKy7XXb9XGswKN9NrG8i985PH0qm6BdMrvZnj5EqD32Rzet5mivYP1lARuB84fvR_bm6BvbPz4ckFSu27nTajiEHYxEJPvbCYV_j_Kh0WCpgInuHMJvknjTsmDvxWlfMFm3WwO7C6D3ktBFk7u6OdltQV7jUMu_mhdWCSW708akRfKbgnN3ChK8ifVgczE6SUeXoyVbnUp-Pm625PIQT0HU54VmXk__PnHfN2LYD9HDaIJzchiIm7zNiD9zjvPbary9vKCzt1tZxoKhmMn1Pa9A95H9n3UCVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همینه که میگم API نمی‌صرفه
توی 40 دقیقه، از پلن 20 دلاری کلاد که با این روش:
https://t.me/MatinSenPaii/5201
گرفته بودمش، نزدیک به 15 دلار معادل Raw API مصرف شده. اما کلا 7 درصد از محدودیت هفتگی من رفته. 4 هفته هم داریم، 15*100 و تقسیم بر 7 و ضرب در 4(هفته) تقریبا میشه 850 دلار استفاده. با یه پلن 20 دلاری. هرچند محاسبه‌اش به این سادگی نیست اما یه دید کلی میده
(با پلن 250 دلاریش تقریبا نزدیک به چند ده هزار دلار سوزونده بودم قبلا)</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5267" target="_blank">📅 21:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/snJAs33tRTTVzKX75YzMyY2Ri087Nbk8xYpHlRdQXFcEsH8Epc4S5RHRzPdIeCYZm4M2-oKkafrG1b7_TqmpCnpsP3EP3A9vNbZWpv_iJrvvkRR0vUt2x8oN370BzY-yt6ZLcOVgYGnO-Q4ajCbotonwNKn-gcNJRu9x0HpKbpgPjK21nFYQP0NCze6W2RegPHN8NkuBDr9AJcHEd5lCLmvsyMhOJccBVGKGylpzs_FRn-O7fV4Sf_3aXKg49zK6dGqq7xF0sQqJLV51nmmqGcF-tALbgnnlPpGaBBJ3AXUjBulWQOrasj2sKTvgrGSYgc5VODb2w1dbRjmj4aRt-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QFj7O3WfM5hFXAQT25IEx6kW5Dlkylo5rpX6OA49ZHp4hQlz-ur3vhOfNkAtwuiLx2JYwlBx7lReOXB-op1DSt3bFqwuM632a465f6uinwoLFjC5TNJAbtER3YOx67B_9nlzGjfqzLEG3KTcfgFC2lDLG2-KyWS6neX72E9kht84koOFSVLCZwITacq9qNO04xVvGE4mip49cdgouFgoKZTO2Do7HCJS6qypJCXADF_SdxiT1GFeDpANkF57PnFbuovZBMM7QyXMxyxk44VA_pEULouChFHcmWxkMXyPR3S2Vx-WwBOu9e9LIwFN_lKYGdWbSjdHGjJ602BiCHiNZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5265" target="_blank">📅 21:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GO3YZPG939SfkFrBMcrrwKK2i9_3EKUCicEVIGXCcAn4baUF1ry4xQJYoPFeJJGfcbOaNfrEnOR_LDtt7s-Pz22WzKev2i2AF81aEln2Z_4502IxV-YcbhcVyiByymFCRLSJArrApRVArRXAJ1-f3u69cARblPV6nQra4HDC8Fq3wYKS-BQv6oe3F0CbU4XJza2MTRwSTTCPmdL21GmZ_uRwQZ8Wu10Zrfu_cpaBqwrZyAZQOxx_CWvVb2D1pqYwRGjF5zlhX3yAa6-0D_MPKYa8q5c74E6WqXnOurWP5kn5guIfmwmZh2CjW-ADB5BO1daBQ8sE_zvl4H8lOsXb2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید
راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5264" target="_blank">📅 20:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یه خبر عجیبی که دیدم، هشدار درباره‌ی حملات زنجیره‌ای به توسعه‌دهند‌ه‌های Rust بودش. به‌گفته‌ی تیم امنیتی crates، یه سری مهاجمِ ناشناس، توسعه‌دهنده‌های شناخته‌شده‌ی Rust و صاحب‌های crateهای محبوب رو هدف گرفته‌ن؛ معمولا با دعوت به یه تماس کاری یا پروژه‌ای، و بعد تلاش برای سرقت حساب‌ها و انتشار بدافزار
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5263" target="_blank">📅 20:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P4IvMgwxq4Z9gV5ROmlrzoKAUn70IdvooD4QMb5S5eElzChCQXhI6Wbjrtz5BMVfJtLIShdPJikcawwxr_PkxGD3U5HAVZ040c98-86IuRpogp7E6IhqLtO77Z_cY2bWy2-ftgLWYuvayoSHA-0ni5BjLumYp34TaRnXC5m2pAd0_lRpseeavbynSsXejj0LwmhIQ3qhbVOiai21naDVzYQY4zMqFLrWhrTwn27m5hadL8-PmdR__MgyQeogW-fTpW-824JspQJYmP9KnqL07DKv2OBAHESsRpmN4ov3zZQ8edIl5axZjAQXz2fkxQzOFCfme2i2Ww2YwwndyoPKBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا در خدمتتون هستم بچه‌ها</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5262" target="_blank">📅 16:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/GNZni_W0Ehw4zJXNsQy5AqST2PSF_ZQGnKcyVZmmj4VZwZpFwxVe8TQq9s50TWgpxNqZtmEC3MQs_7YedOmirfDOtxMA79lNCiIl88-PhPOxIQHvVQm-O9LP3N2vQUUvCPXqkqSDD9GniPpe-J_ZDKP3zRfhpih6wcHbitgBPDlSqHyzinpzdQlzaOeJVGLJ3Lz_3gCeKKU6PP3fw9c3aboL3IQe1vzFpAmn9E_XCC5nkVeDsQM_bjQN_gkPVH2MAbgdYgo-yIltEaMyLdsNekV4BV8LV5ho8TMBm7iRQSzIRI0bdn6y_k_MwOwegzPQIaFWDyM1v6uo3wthM5bPbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
;کاتن روتر
چیست؟
کاتن روتر یک ابزار سبک برای مدیریت چند سرویس DNS Tunnel روی یک سرور است.
خیلی ساده بخواهیم بگوییم:
فرض کنید چند سرویس مختلف دارید، اما فقط یک سرور و یک IP در اختیار دارید. CottenRouter درخواست‌ها را دریافت می‌کند و بر اساس دامنه، هر درخواست را به سرویس مربوطه می‌فرستد.
یعنی چند سرویس می‌توانند از یک IP و پورت عمومی ۵۳ استفاده کنند.
⚠️
توجه: CottenRouter خودش VPN یا تونل ایجاد نمی‌کند؛ بلکه سرویس‌های تونلی موجود مانند CottenDNS، MasterDnsVPN، StormDNS و SlipGate را مدیریت و مسیریابی می‌کند.
🔗
لینک پروژه:
https://github.com/TaJirax/CottenRouter
پیش‌نیازها
برای نصب به این موارد نیاز دارید:
یک سرور Linux با IP عمومی
دسترسی SSH و root یا sudo
دامنه یا زیردامنه
سیستم‌عامل پیشنهادی: Ubuntu 20.04 به بالا یا Debian 11 به بالا
روی ویندوز مستقیماً نصب نمی‌شود؛ باید روی سرور Linux نصب شود.
نصب آسان
ابتدا با SSH به سرور وصل شوید:
ssh root@IP-SERVER
سپس دستور زیر را اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
بعد از نصب، پنل مدیریت را باز کنید:
sudo cottenrouter tui
استفاده خیلی ساده
در پنل بازشده:
با کلید Space سرویس موردنظر را انتخاب کنید.
با کلید i نصب هدایت‌شده را شروع کنید.
با کلیدهای Enter یا e دامنه و پورت سرویس را تنظیم کنید.
با کلید s یک سرویس را Restart کنید.
با کلید v اطلاعات اتصال و مسیر رمزها را ببینید.
با کلید x یک سرویس را حذف کنید.
تنظیم دامنه
برای هر سرویس یک زیردامنه جدا بسازید و همه را به IP سرور متصل کنید:
cotten.example.com
→ CottenDNS
master.example.com
→ MasterDnsVPN
storm.example.com
→ StormDNS
feed.example.com
→ thefeed
در پنل، همین دامنه‌ها را برای سرویس‌های مربوطه وارد کنید.
بررسی وضعیت سرویس
برای دیدن وضعیت CottenRouter:
sudo systemctl status cottenrouter
برای بررسی سلامت:
sudo cottenrouter healthz -config /etc/cottenrouter/config.json
برای دیدن لاگ‌ها:
sudo journalctl -u cottenrouter -f
به‌روزرسانی
برای نصب آخرین نسخه، همان دستور نصب را دوباره اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
نصاب تنظیمات قبلی را نگه می‌دارد و در صورت بروز خطا امکان بازگشت خودکار دارد.
📌
برای اطلاعات کامل‌تر، راهنمای فارسی پروژه را ببینید:
https://github.com/TaJirax/CottenRouter/blob/main/README.fa.md
اطلاعات این متن بر اساس راهنمای فعلی مخزن نوشته شده است.
@whitedns</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5261" target="_blank">📅 23:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5260" target="_blank">📅 23:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha
1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن
2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده)
3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/5259" target="_blank">📅 21:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5258">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شاید که به کار آید https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/MatinSenPaii/5258" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaUHZc7SFGLQaYdGtkl1_Ht8gstSIV8KPiwsRXiqBC0S9CDbxAG5eu_LWk153VAO7p9ZpFjWqweZcc5-pCCmLzO4egKEkn_O6nJ3JdsVB6Wews_W2DlSErv_G-UCpVIe0RFfuuE4kybXeFTVW8JIy6TiwKzdNJGG79vcTrU_Yq6xO4kxssufKX_ZKEj1K7zTHYo-s7Eye2t5TnRiguJEKozWJYwKoNVRhKQDc4mt7G6teDTqoSHn2-ZG6eXN0_45UK4pbQeogp5BgktX1GxcVS5610rt9j72DgL9dGrEjebjNN14rUSxRmrFtZvl-kJ41ScwRDVaAcBmvHe6IevahA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید که به کار آید
https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/MatinSenPaii/5257" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه آنتی گرویتی | Antigravity Community</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBntUb2jr7avon2I4P_jp4a0f4mM99GlFh7JLs9Mlhh_LSujUc0jLU4ubwhcb0p8H-zySkX_oF8AuS6szy90WvCmdvan6ktqeNyykwajDDq1b5LX7Rb9uXFZAaLzdZI5NJGaJLD5zMCZ6HNSrcpKJEibHbJa2S2qFDmReNKzmUM193O7b5rZGImhWIroOw4WKbKCsKuFDPzv6fKHE4TamozIqvdPvbfVHsefCKHPVm23n8_EC90J_N3O8fNo4fmi3ZOYpWYg9IaPZVm3N8wcp9w3qXoL5_m8NEayk4WjnEt9I9RE0lAixdWlOStT2D_kfnQrPDoPY36HBS_9aV0JmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
راهنمای جامع حل مشکل ارور ریجن (Region Not Supported) در Google Antigravity
یکی از آزاردهنده‌ترین ارورها در استفاده از آنتی‌گرویتی، خطای عدم دسترسی بر اساس کشور و لوکیشن است. این بررسی‌ها در دو لایه (سمت اکانت گوگل و سمت کلاینت نرم‌افزار) انجام می‌شوند.
در ادامه تمام روش‌های تست‌شده و قطعی برای رفع دائمی این مشکل را بررسی می‌کنیم:
---
🚀
روش اول: تغییر رسمی و دائمی کشور اکانت (توصیه شده)
گوگل در دیتابیس مرکزی خود برای هر اکانت یک کشور مرجع (Country Association) ثبت می‌کند. برای تغییر دائمی آن:
۱. فیلترشکن خود را روی یک کشور مجاز (مثل آمریکا، آلمان یا امارات) بگذارید.
۲. وارد لینک فرم رسمی گوگل شوید:
🔗
https://policies.google.com/country-association-form
۳. با اکانت مورد نظرتان لاگین کنید. کشوری که در حال حاضر به اکانت منتسب است را مشاهده می‌کنید.
۴. روی گزینه تغییر / بازبینی کلیک کرده و با توجه به لوکیشن IP فعلی‌تان، درخواست تغییر کشور را ثبت کنید تا به صورت دائمی اعمال شود.
---
🛠
روش دوم: پچ کردن کلاینت نرم‌افزار (Bypass بررسی ریجن در اپلیکیشن)
بخشی از چک کردن ریجن و اعتبارسنجی‌ها مستقیماً داخل کلاینت نرم‌افزار انجام می‌شود. به کمک پروژه متن‌باز
Open Antigravity Patcher
می‌توانید این محدودیت را سمت کلاینت خنثی کنید:
⭐
سورس‌کد و راهنمای پروژه در گیت‌هاب:
https://github.com/AvenCores/open-antigravity-patcher
• این پچ محدودیت‌های منطقه‌ای کلاینت را بازنویسی می‌کند.
• برای تمامی سیستم‌عامل‌ها (macOS، Windows و Linux) در دسترس است و با اجرای اسکریپت راه‌انداز آن، برنامه آماده به کار می‌شود.
---
💡
نکات بسیار مهم و ترفند تست پایداری VPN:
۱.
تست کیفیت فیلترشکن قبل از باز کردن نرم‌افزار:
قبل از اینکه Antigravity را باز کنید، ابتدا وارد وب‌سایت رسمی جمنای (
https://gemini.google.com
) شوید و یک پیام کوتاه بفرستید. اگر چت بدون ارور لوکیشن پاسخ داده شد، یعنی فیلترشکن شما بدون نشت IP (IP Leak) کار می‌کند و با خیال راحت می‌توانید آنتی‌گرویتی را اجرا کنید.
۲.
استفاده از حالت TUN / Global:
مطمئن شوید فیلترشکن شما روی حالت TUN فعال است تا ترافیک برنامه‌های غیرمرورگری دسکتاپ را هم به‌درستی هدایت کند.
---
⚡️
سوییچ سریع بین چند اکانت:
اگر برای عبور از محدودیت‌ها چند جیمیل مختلف دارید، با ابزار
Antigravity Account Switcher
می‌توانید زیر ۳ ثانیه و با ۱ کلیک بین اکانت‌هایتان سوییچ کنید:
https://github.com/m4tinbeigi-official/antigravity-account-switcher
@antigravity_iran</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/5256" target="_blank">📅 11:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5255">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnagS2cTEGb6wW8zri9wrhOQD4wZ961oZAXQDV5b347wAvIc2MsZRuuJ7k3v05O030cUTkO1POehrZfFM0FEIWSFWJh6b_5ULdm2ykLp8MVRdF5IQCxZl_POYbwjrO2MfBvrO_S5Qtr4L7Tr_kClEx3pJY4HPrI8i-E8ZA4QDLsDjNe45wqkZJ5vUBXqFS_GAscjac1jAI7kZ9yGKZ6z0JkwbwB_7_6ezy0IOnmwSV6OAmKYvTz5W1O8YYWW6UF0JRUNomC23CqB4hFSTmWCdaRHk7ApGZ370B3Z6fLDTNq_ko5rI5UEEI3f6miLc8Vnk9eAS-lWUZYZAWMHmtU4Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
اگه ویدیوی دیروز درباره GitHub Spec Kit و Spec-Driven Development رو دیدید، این ابزار هم می‌تونه کنارش خیلی کاربردی باشه.
اسمش to-spec هست و کارش ساده‌ست:
✏️
شما با Agent درباره فیچر، مشکل یا چیزی که می‌خواید بسازید صحبت می‌کنید، Agent کدبیس رو هم می‌شناسه، بعد "to-spec" از همین Conversation و Context موجود یک Spec ساختاریافته براتون می‌سازه.
یعنی لازم نیست بعد از نیم ساعت بحث با AI دوباره بشینید همه‌چیز رو از اول تبدیل به Requirements و Spec کنید.
⚙️
برای نصب
npx skills add https://github.com/mattpocock/skills --skill to-spec
🔗
لینک
💬
به‌خصوص اگه دارید با روشی که دیروز توی ویدیو درباره Spec Kit گفتم کار می‌کنید، این می‌تونه یک راه خوب برای تبدیل گفتگوهای اولیه‌تون با Agent به نقطه شروع یک Spec تمیز باشه.</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5255" target="_blank">📅 09:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5254">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔸
مخزن OpenUI: ایجنت به‌جای متن، خودِ صفحه رو می‌سازه
تا حالا مدل AI بیشتر جواب متنی می‌داد. این پروژه کمک می‌کنه مدل مستقیم UI بسازه؛ یعنی دکمه، کارت، فرم و چارت، همون لحظه روی صفحه ظاهر بشن. اسم این کار Generative UI هست و OpenUI یه استاندارد باز برای همینه.
توی کار روزمره اینطوری به درد می‌خوره:
تو می‌گی چه کامپوننت‌هایی مجازن، مدل فقط از همون‌ها استفاده می‌کنه، و خروجی‌ش هم‌زمان که می‌آد روی صفحه render می‌شه. برای چت ایجنت، نسخه‌ی آماده‌ی React داره. اگه با Cursor یا Claude Code کار می‌کنی، skill هم داره که راه‌اندازی رو ساده‌تر کنه.
نظر شخصی: این ابزار طراحی توی Figma نیست. برای وقتیه که می‌خوای ایجنت واقعاً رابط کاربری بسازه، نه فقط توضیح بده. اگه داری یه chat هوشمند با خروجی بصری می‌سازی، این پروژه کاربرد داره.
لینک GitHub:
https://github.com/thesysdev/openui
✍️
CallMeDiegoJr</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5254" target="_blank">📅 00:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5253">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/5253" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خب ته و توش رو در آوردم، این دوستمون یه یوتیوبر/برنامه‌نویس به اسم Matthew Miller هستش و یه چالش جالب شروع کرده: «انقدر Vibe Coding می‌کنم تا به درآمد سالانه 1 میلیون دلار برسم.» طرف تقریبا هر روز لایو می‌ره و جلوی بقیه روی محصول خودش به اسم BridgeMind کد…</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/MatinSenPaii/5252" target="_blank">📅 22:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/5251" target="_blank">📅 21:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cKfS0CIUMcuK8xBJPDqjdmt4h6UDT8M681s7zekfIQV9e0YVHmONuC_Cih4yOGQueB_hj1MZ6U_8PzsXd7WKO9Yd1UQqwGzfR6NYrATYIFvrpxYkCatMI5JCNrI97IVGs7iaumZsOvESx9oSuMZIfjFQO4ZqiWkIURxYaH-dA5LE2GkxwgC1u2AA6cbxHyoX61D1w51IOo4QksBLk0jvZYActdXFroD0B9yLmVG7WrFO7jPB8MwoPHjnr8USypVY1MwpCKjsquoCxo-rQDnNBpfgN8MDVp3i7JJLJ8r29ETxEkyg-OuKLhSd37IxZj4w7qWI2N1HGTHwg5n57KIpiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/5250" target="_blank">📅 20:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.  بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.  یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5249" target="_blank">📅 17:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.
بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.
یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference وصل می‌کنین. می‌تونن با فرستادن tool call جعلی اطلاعاتتون رو بدزدن. و ثابت هم شده که از این قبیل کارها میکنند.
کل تریس‌هاتون، رد کامل تعاملات و اجرای ایجنت رو هم به شخص ثالث می‌فروشن و اون‌ها هم دوباره به بقیه می‌فروشن. کافیه یه API key یا اطلاعات حساس توی این تریس‌ها باشه تا به فنا برین.
اگه نمی‌تونین توضیح بدین یه سرویس چطور می‌تونه توکن رو این‌قدر ارزون بفروشه، سمتش نرین.
✍️
PsyopBaz</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/5248" target="_blank">📅 17:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/puXrpANcPS23iVzPRQFN2hReg8TcV5Sa98cqzk0pIe2-kWrZQUMNwLC3zkh9e0M4JOPIqhiuSQhCaDeklb8Qe6--onQ963hpJ95umYj8HJ-naIkzwG7k2QIK2yMp0aN2ClIfQxMSDlLd6j76ErJOnlHka5VJyLK5VyxxlJWC1tr8ysSf8n6FAUdrZK4b3y94mgeGHjD4r_sT4EB2HSNHPCw2kNzBcro1NH9REEvJBJb0qdLFjUkzPBkzcdgykB4N6TDEatU_bVGAY_bYO7Y142VULeLrx7pWqWxTvjFV3yUf2DP_C_fzQllUXcfw9crccMFCqVeV_WM328hXvvOh2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی این قانون رجیستری رو من نفهمیدم که نفهمیدم که نفهمیدم.</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/5247" target="_blank">📅 17:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">متأسفانه گویا Railway داره اکانت‌هایی که با ریپو هرمس، ایجنت ساختن مسدود می‌کنه. سیاست‌هاش احتمالا عوض شده.
دنبال راه جایگزین هستم که بشه دورش زد یا از پلتفرم دیگه‌ای استفاده کرد</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5246" target="_blank">📅 16:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛  اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/5245" target="_blank">📅 15:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R1FEaCicWn0ONHOnprUSIYXs0NPN6U-ExKAF2ZBXwzWLuHj_I8jZPn3_N6H8BTIqfcqK3jyobC6qrf_AMIoYeWohbG0ch18UY-XIqbjcprzN0R_MPuFEwd1-XxhjJcvskNRkpkPFe3erTIlwkXQTFmRy2uCHfxLHvpJ5gaHfMR43GB6fR8i9owvls6v7bxQWhmndfZT49G8RVeK-IwbF9YPUQWjXX7nV0VLv2NVV3zhETKVdm-a9zNX7lSq4OxukZB2-z9rTGJrVAKVdIsS4xWAyREo39mLbLjYKxPWyBLDZunL__N2t7dNlOkzr5pQ90zDAivfRLCywG57CyTZYKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/MatinSenPaii/5244" target="_blank">📅 23:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار…</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/5243" target="_blank">📅 23:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wiw2x2tkHJqmfFb3qYPIV95F6OMX3jqGa892L3ziYf6pT1MP2jwAu2sNrvYecjpwV70ERVnOLyvcyhga-bRrVql7856ucFIfPoWEdC18s5SyRiby6r4FklugPraKiBYKpifjRS_jGixZFiTzJOPu-zzpZMzqQ-ri82StTRtF-TqIe78T-QSUbuoPopbgCWbc6M4A0uuxO5EgmkRZley-RnTO5xNcaN-WirvhgHxLYRjGi0fc5SO5lUDMEqmqdPI-WrIGCSfhCOSXOvxzELNzstNDHzyII5NZTeP3aVeGwf_LrFNqZD2iUu4esu9Nw6a-gG4v0D-DxMTAS2yAwik14A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار هم مقایسه می‌کنیم.
منظور از «توسعه مبتنی بر مشخصات» اینه که قبل از پیاده‌سازی، روشن کنیم دقیقاً چی می‌خوایم بسازیم، چرا و چه انتظاری ازش داریم. ابزار Spec Kit گیت‌هاب کمک می‌کنه این مشخصات رو تدوین کنیم، براشون برنامه‌ی فنی بچینیم و کار رو به تسک‌های قابل‌اجرا تقسیم کنیم؛ بعد کدنویسی رو بر اساس همین مسیر پیش ببریم.
برای من، بخش مهم این روش فقط کد نوشتن نیست؛ اینه که بیشتر به داستان محصول فکر کنیم: کاربر چه مشکلی داره؟ قراره چه مسیری رو توی محصول طی کنه؟ از کجا بفهمیم چیزی که ساختیم، واقعاً نیازش رو برطرف می‌کنه؟
💬
حتی اگه برنامه‌نویس نیستید، ولی با کمک AI ایده‌هاتون رو می‌سازید، پیشنهاد می‌کنم یه نگاهی به این ویدیو بندازید. با یک مثال عملی بررسی می‌کنیم که وقت گذاشتن برای روشن کردن خواسته‌ها، چه تفاوتی با شروع مستقیم از «کد بزن» داره.
⏯️
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/5242" target="_blank">📅 23:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده. برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/5241" target="_blank">📅 22:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده.
برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/5240" target="_blank">📅 22:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نمی‌دونم حکمتش چیه روز تولد من با روز جهانی برنامه‌نویس یکی شده
🗃️
مرسی بابت تبریکاتون
❤️</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/MatinSenPaii/5239" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kquN9mHHK2LPb2Yvai85pG67ZRe4OVi-rSM4Myugqn15wB8oKbOej80Y7-Yf1Zjkd4RCgfqGIMggYNPSvitYIPSnY09GgBC7SEjOQw6zydkB6lOs66FBsatlRFOhIk-yrrzwXk1wVkpf9kfx9y2kcp6EjHujjp9dlVeFYeM7Pl8U60IuMQpNtGVMky0qS3etgLilQjOUL6P-4EyjcscPdVLXt3XC7uFqPBFwi1bSLLgCeLmKqX3psL4uIT6AV4GJ2QRsnkUTs2tLjhyphSJZLdCI8HJmumZ9i65XogJWet7Miz5UelzAd88-MrPJRtb9ef9I7NFSanEWiZ5RJNFFHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude بهتره یا ChatGPT</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/MatinSenPaii/5238" target="_blank">📅 00:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=F5iGFOwlbg_Y6Fyk7Jj7fUYZFF4NNiunl7cIb6no7wBDexhgr-QVWkS1unYqTbwb873R7X26e8ujJv8TimIuDpTZTGGpSJio38jCm1xSv73SE0zAlHOYc2E1uiDoKuSM4RjrSmgjJ6SL4srRtKz59Ydu5jI8YauHB6sFPr25Bwha0pcVeNr3GZW0U8joLB47VvCH-4hKl0-mMW8hH8FVbFsIIfN4YLAV2YlFbQJr6VqVp6aKqg0fD_9W-r9S-0PZIjiX4Qw78PQ8i0LKtRkcsPW9DQEAj8wT0HoXaUx4SDXPhbeG5Dw26O01Us6FExua5gZMprz6J1CvrvALoijLkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=F5iGFOwlbg_Y6Fyk7Jj7fUYZFF4NNiunl7cIb6no7wBDexhgr-QVWkS1unYqTbwb873R7X26e8ujJv8TimIuDpTZTGGpSJio38jCm1xSv73SE0zAlHOYc2E1uiDoKuSM4RjrSmgjJ6SL4srRtKz59Ydu5jI8YauHB6sFPr25Bwha0pcVeNr3GZW0U8joLB47VvCH-4hKl0-mMW8hH8FVbFsIIfN4YLAV2YlFbQJr6VqVp6aKqg0fD_9W-r9S-0PZIjiX4Qw78PQ8i0LKtRkcsPW9DQEAj8wT0HoXaUx4SDXPhbeG5Dw26O01Us6FExua5gZMprz6J1CvrvALoijLkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/MatinSenPaii/5237" target="_blank">📅 00:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.   این قسمت پلن های امسال هم ضربدر خورد.   فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/MatinSenPaii/5236" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5235">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BN19Pl6Dnq8S53ghRWbThQE2sov4XH3PHddiGPEzmNZxlmg-npva9w23AeAauDiYF6RfNMlRf3uwUc_nJP77dWZ-Cv0aGB6bExyXEcD6jh_quujXh-14QeN1n6tuvDs5NjwzsapY0dApIoI0-bXHtzIj0i_7iey7CP3-QblTH-_X-gii5ClVS0E3Yhnm_2OVex6r8gPEHnbKOLdEkAdvYa62fqeflCL0APWfpdtUkRJkxVPjWO2kMwJbo1809mfxDBqRA4edr24ymLn_KLAfITz9zYEWz7TAf_waQdyf7O8m1v-eTk4sSBD-kUiq7vPx8fWKDZ2957iNxxRKiCsS0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.
این قسمت پلن های امسال هم ضربدر خورد.
فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/MatinSenPaii/5235" target="_blank">📅 12:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pMCzQl5vcB-AV59ZQ5VriaJ_msslu3_ABLoBG0WVgk5ruyuMxxPsgT5nt6_rSYjJePs3fpZ-lD3sxURW3HxHsq-7uiM6ZbfJq9VU2b3YrCcjbo8NIuWh5E52kvXcDch0S72uNlrl9hQ9-xfRIDPoE8x2GINT4x-ONrfbPj7FWRrj0jDS2o3HeIjJ7mv_hRYdo17X7j5iUW1_VvDgNDIIKJbgiyulZcaCiy6XJNGZwibAzjP2HyXsqpJWYm3DnlJrpuTIYWUKs0WgnS8r1OMFD6gM0BiFJpqhy_9C1gr7Bgk9cmdcgfY-H6yH6Edu3JXectwLaC-7S9mGLMDpWsDbQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت Freestyle.sh می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.  برای ساخت حساب مجازی هم می‌تونید از طریق MPay اقدام کنید.  مشخصات سرور رایگان:  RAM: ۸ گیگابایت HDD: ۳۲ گیگابایت CPU: ۴ هسته…</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/MatinSenPaii/5234" target="_blank">📅 00:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5233">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcmL1j2UJ2hWj9F67BI9x96NMStr5hnOhdi0g_lMhj-9X2YIL-630n4pDvvkzD8BT-HI_alPreYMf0Zc5kk1q-nP_UrVLJXKUhbZQOy7n5zjdJTktjOcEiH7dyHrCNbcT_Ix3HZs1AJUR0pzs7XdmmlA_wPL6V-3CMomwtPhCu4TIH2DQJ8ORcKO1MjLnqk6dWbGxrI0Sk36McYyIHAOBU-TKh_KhZraffDYo12r2aa0CWsG777FkbxK3NunEFFw8dt44fBJGZHTUudqyhqrSzl8P6vKlAG5ypWu3CaroLBfTGal2_6j5WbinOcVQwoOPbCGEjaMW41xlLHKJvG84w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت
Freestyle.sh
می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.
برای ساخت حساب مجازی هم می‌تونید از طریق
MPay
اقدام کنید.
مشخصات سرور رایگان:
RAM: ۸ گیگابایت
HDD: ۳۲ گیگابایت
CPU: ۴ هسته مجازی
مناسب برای تست، پروژه‌های شخصی و راه‌اندازی سرویس‌های سبک
🚀
من روش هرمس نصب کردم
👀</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/MatinSenPaii/5233" target="_blank">📅 00:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یکی از صحبتامون توی استریم با یزدان دقیقا همین بود که ما هنوز نمی‌تونیم سقف پیشرفت AI رو بسنجیم؛
برای همین اکثر نظرات به ظاهر کارشناسانه هم در حد حدسن. و نه باید شما رو بترسونن(حرف‌های ترسناک که ai ترمیناتوره و دنیا رو میگیره
😂
)، نه باید خیال شما رو راحت کنن(حرف‌های خوشایند که نه بابا ai جات رو نمی‌گیره)</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/5232" target="_blank">📅 00:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم. اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/5231" target="_blank">📅 00:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=au5YdY6tj_AA45z3-jIesa6NYTWTZCUA6OxrlTCJm2QPWqfLYoMMJW5Tk2ZE9L3BzPF2TnTbqY6EX4dG1S7IjYay_rtLXJ0m89qNmmmPnWtvWjljvkCdss9YGf_abidOoazmELsixIZRBHN_Yis7A8ZKXFHPD94Rk6Wk2iK1Tzw33NAi4loiFWyGjouSGJAFSxIBg2066ZBkBIgZ3yqR0BD51nIq0IUjVhrm2gq2seHQ4Q5SZn5cOpUnmsE5o48GxC_RoMgs9O8rydfzhVeBJLIXNENE1QRBAIOZFjS3YoxIbTQ4EhiSkSpz2GKLatKHDE1_g15d8K7DjZFZkhjN1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=au5YdY6tj_AA45z3-jIesa6NYTWTZCUA6OxrlTCJm2QPWqfLYoMMJW5Tk2ZE9L3BzPF2TnTbqY6EX4dG1S7IjYay_rtLXJ0m89qNmmmPnWtvWjljvkCdss9YGf_abidOoazmELsixIZRBHN_Yis7A8ZKXFHPD94Rk6Wk2iK1Tzw33NAi4loiFWyGjouSGJAFSxIBg2066ZBkBIgZ3yqR0BD51nIq0IUjVhrm2gq2seHQ4Q5SZn5cOpUnmsE5o48GxC_RoMgs9O8rydfzhVeBJLIXNENE1QRBAIOZFjS3YoxIbTQ4EhiSkSpz2GKLatKHDE1_g15d8K7DjZFZkhjN1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم.
اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/5230" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">زلزله خاموش چین در بازار مصرف هوش مصنوعی
🇨🇳
طبق جدیدترین آمار ماه اخیر OpenRouter (۳۰ روز گذشته)، ۷ مدل از ۱۰ مدل پرمصرف جهان چینی هستند و نبض اقتصاد توکن را در دست گرفته‌اند:
​۱. DeepSeek V4 Flash
🇨🇳
۲. Tencent Hy3
🇨🇳
۳. GPT-5.6 Luna (OpenAI)
🇺🇸
۴. DeepSeek V4 Flash (نسخه دوم)
🇨🇳
۵. Nemotron 3 Ultra (NVIDIA)
🇺🇸
۶. GLM-5.3 Flash (Zhipu AI)
🇨🇳
۷. GLM-5.2 (Zhipu AI)
🇨🇳
۸. Tencent Hy4 Preview
🇨🇳
۹. MiniMax M3
🇨🇳
۱۰. Claude Opus 5 (Anthropic)
🇺🇸
حضور قدرتمند Tencent، DeepSeek و Zhipu نشان می‌دهد جنگ AI دیگر صرفا سر ثبت بالاترین بنچمارک نیست؛ بلکه جنگ قیمت نزدیک به رایگان، مدل‌های فوق‌سریع سری Flash، و مقیاس عظیم توزیع است.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5229" target="_blank">📅 21:53 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
