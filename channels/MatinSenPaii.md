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
<img src="https://cdn1.telesco.pe/file/NYgB6X0tp4dqLBWNwlgxq0zXDmBUQCz_yYU1GtiE_8r9YPo10idqRs_5_36DONmajCxw2Crjl1Q0go1F0o6YTHeFFIprGFuOhFHQ_SHJ2fGY7N_VReeEVFkba7ec_AWir3zAswy8DGG36JSicbVVqMQH8mmknQUsQi2fCnAtFQv6ZXYtOrH5oVFHCjJBkEiNRS9OfAJUoDw4lHB6tR-ugwiRU8A3gXnpkHP-dVm_2hzZ4_nCkwgCpfB4l30clg4B6OL7zkh9dRrNqWjph8BoLp5stwTNt-Ph1Nozpq8rcX5yw3rjIBoMKEo1AqlCm4ZoyBJ1G3zCxMOAwJWUz2UMog.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 158K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPaiایمیل کاری: matinsp.job@gmail.com</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 08:43:32</div>
<hr>

<div class="tg-post" id="msg-4297">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r8IbrQSI_mPeHO7U-tlXHFaKsZqIIIpkyM5KkPkD6MgLnhTpH5F-UNyMfBELHp2GykwAosoeHyvUQCSdJ7CtpY4Uv8kCLS-rECYXdD58MJgRfWDqKqYUq0sIZ3vvGLqbqH8xzRizGXXQY8ZdZWMhzZJsflhLIjkTsoM2UgCu-cbnrbDC7Xi32PbaOx8Rs5E4ATW1TLu7soQnNZ6F30zVkpDtYIfqCvVta1vDgmt5IGC57GD560LlvvefhKR16xIhWLLPVcp641FkRDyh25ThwSg_cASk4k813Pr5Fow5eqCQ1MNc60KkEnGX5cwOgeMuEf3qP59c31Vsqwu8YMjhRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AsOTT195xrjIF0ruuGjivrbTkln0sW5YYVunV2WQwgBzrOwJBZdt5y1uMByuJtZ6Q-KZMwn8oTup8fiAKHlvBK3_RQ5Of3GxDFk7xUw304rJc_N0tdM6hcich_63ppal7jVSNT20mDF9Y1NBsqzO-tW8eUZ3K_uLE52zB9Aecvuw76YZW2b9daKbi1gOK_xVchm9tDohY4VTLgITj7KiAm3KHVi6diw2c3qpFUBARja4WTuRsxdsxgcPvMkkx_k284uleGQbM9YertBnr6g0KMM81qBotUfz7Gs3W28i_gMnKr3Bf2jld40uzK5olkMTBWPaJ2Rko2l3Z1yobJOiFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pbh5UdrLIvgmJdeZabN1UDIryEC9ZhugIWzony4bEHecQj42k2HYxgQyRUxwUAlJ7hRv2yqlppRPbBQbcZJ4ZteOHhr4BcXLUEAsmVprxSzw5AVqBdIn_QXFlruhdZtPo3NiGDOpuWYHqJj4P6svAu38VoO2VGLi3O0K2JsLnteeiairnW60QNV0kwxOw_ORqTIWkf4xMGMk5d3HcxSyvc4NzM-Ul0v7uqThN8N44iTh81Agt6M2AF5hav071jV7Oj9N_Pb0Ed9FJ88q4TuHaYzqN2gXdwEhzT8KQGgOkXVR3W_mvZfHgcrxEopu3_llIibAmEYel_nlWSTn1_ZaIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی هزینه‌ی هوش مصنوعی از حقوق مهندس هم بیشتر می‌شه
خلاصه:
شرکت «آنتروپیک» (Anthropic) حدود ۲.۳ برابرِ پولی که بابت حقوق و دستمزد می‌ده، خرج زیرساخت و پردازش (Compute) می‌کنه! یعنی با حساب حقوق سالانه ۲۲۴ هزار دلاری (با احتساب تمام مزایا)، سالی ۵۱۵ هزار دلار به ازای هر مهندس خرج پردازش می‌کنه. در حالی که ۱ درصد از برترین شرکت‌های نرم‌افزاری فقط ۸۹ هزار دلار و شرکت‌های میانه بازار (میانه آماری)، کلاً ۱۳۷ دلار خرج می‌کنن. حالا ۳ تا سناریو برای سال ۲۰۲۹ داریم که نشون می‌ده این شکاف عمیق چطوری ممکنه پر بشه.
همونطور که اشاره شد، آنتروپیک ۲.۳ برابر حقوق پرسنلش، در حال حاضر داره خرج زیرساخت و پردازش می‌کنه. با حدود ۵,۰۰۰ تا کارمند و تقریباً ۱۰ میلیارد دلار هزینه‌ای که توی سال ۲۰۲۶ برای آموزش مدل و استنتاج (Inference) می‌کنه، سهم هر کارمند سالی حدود
۲ میلیون دلار
هزینه پردازشی می‌شه؛ اونم در مقابل حقوق و مزایای کلانی که برای هر نفر احتمالاً بالای ۵۰۰ هزار دلاره!
بقیه بازار نرم‌افزار خیلی از این رقم‌ها عقب‌ترن. ۱ درصد از برترین شرکت‌ها سالی ۸۹ هزار دلار به ازای هر مهندس روی هوش مصنوعی خرج می‌کنن؛ یعنی ۴۰ درصد از یک حقوق ۲۲۴ هزار دلاری برای یک مهندس ارشد. این رقم برای شرکت‌های میانه بازار فقط ۱۳۷ دلاره! اختلاف فاحش اینجاست:
۲.۳ برابر حقوق
در لبه‌ی تکنولوژی
۰.۴ برابر حقوق
در صدر بازار
نزدیک به صفر
برای شرکت‌های معمولی بازار
حالا بقیه‌ی بازار چقدر می‌تونن خودشون رو به این سطح برسونن؟ جواب این سوال توی ۳ تا سناریو خلاصه می‌شه.
(توضیح نمودار خطی(عکس سوم): نمایش سه سناریو برای هزینه‌های هوش مصنوعی به عنوان درصدی از حقوق مهندسان تا سال ۲۰۲۹؛ در سناریوی خوش‌بینانه، این رقم به رکورد ۲۳۰ درصدی آنتروپیک می‌رسه)
سناریوی بدبینانه (کاهش قیمت توکن‌ها برنده می‌شه)، سناریوی پایه (رشد ۱ درصد برتر بازار کند می‌شه)، سناریوی خوش‌بینانه (بقیه بازار تا سال ۲۰۲۹ به نسبتِ هزینه آنتروپیک می‌رسن). هر کدوم از این سناریوها، هزینه سالانه هوش مصنوعی به ازای هر مهندس رو نشون می‌دن(عکس دوم)
توی سناریوی خوش‌بینانه، فقط هزینه هوش مصنوعی به ازای هر مهندس، با کل درآمدی که یه کارمند توی شرکت‌های معمولی SaaS تولید می‌کنه برابری می‌کنه! همین الانش هم شرکت‌های آنتروپیک و اوپن‌ای‌آی به ترتیب ۱۴ میلیون دلار و ۶.۵ میلیون دلار به ازای هر کارمند درآمد دارن، که بالاترین رقم توی لیست ۲۰۰۰ شرکت برتر فوربز (Forbes Global 2000) به حساب میاد.
ساختار هزینه‌ها، دقیقاً جا پای ساختار درآمدها می‌ذاره.
موتورهای محرک توی سناریوی خوش‌بینانه:
قیمت مدل‌های پیشرفته ثابت می‌مونه، چون هزینه‌های آموزش به ثبات می‌رسه و تقاضا از عرضه جلو می‌زنه. فرآیندهای کاری مبتنی بر ایجنت (Agentic Workflows) نسبت به چت‌های معمولی، چند سر و گردن توکن بیشتری مصرف می‌کنن؛ طوری که «گلدمن ساکس» پیش‌بینی می‌کنه مصرف توکن تا سال ۲۰۳۰ حدود ۲۴ برابر بشه. تازه، اگه شرکت رقیب قابلیت‌های جدید رو سریع‌تر عرضه کنه، دیگه پرداخت صورت‌حساب هوش مصنوعی یه انتخاب نیست، بلکه یه اجبار حیاتیه.
ترمزها در سناریوی بدبینانه
: قیمت توکن‌ها توی سه سال گذشته، هر سال ۱۰ برابر کاهش پیدا کرده. مدل‌های متن‌باز (Open-weight) دارن با کسری از هزینه‌ها، شکاف کیفی رو پر می‌کنن. از طرفی شرکت‌هایی که مصرف هوش مصنوعی رو بر اساس نقش یا حجم کاری کارمندان سهمیه‌بندی می‌کنن، می‌تونن شیب این نمودار هزینه رو خم کنن و کاهش بدن.
نظر شخصی: اصلا نمیشه پیش‌بینی کرد:) با اومدن ایجنت‌ها، سناریوی توکن داره مطرح میشه. از اون طرف، چین غوغا کرده و با رایگان عرضه کردن مدل‌هایی مثل MIMO و GLM-5.2، واقعا نمی‌تونم نظر بدم.
منبع مقاله:
https://tomtunguz.com/ai-spend-breakeven-2029/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/MatinSenPaii/4297" target="_blank">📅 00:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4296">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یه مقاله از نیویورک تایمز(با اینکه ازشون خوشم نمیاد) دیدم که توی هکرنیوز بحث‌برانگیز شده. داستان در مورد اینه که با پیشرفت سریع مدل‌های زبانی، مهارت‌های کسایی که فلسفه خوندن، چطور توی بحث‌های اخلاقی هوش مصنوعی و Alignment مدل‌ها داره به شدت کاربردی می‌شه. و انگار یه بازار کار جدید داره برای این رشته شکل می‌گیره =)
لینک مقاله:
https://www.nytimes.com/2026/07/05/business/philosophy-majors-ai-jobs.html
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/MatinSenPaii/4296" target="_blank">📅 23:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4295">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اگر میمو روی اوپن کد بهتون ارور ۴۲۹ داد که به لیمیت رایگان رسیدید، نترسید. یه continue بگید دوباره میره ادامه:)</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/MatinSenPaii/4295" target="_blank">📅 21:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4294">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اگر میمو روی اوپن کد بهتون ارور ۴۲۹ داد که به لیمیت رایگان رسیدید، نترسید. یه continue بگید دوباره میره ادامه:)</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/MatinSenPaii/4294" target="_blank">📅 20:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4293">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DxxDcRKgv1oSd2d92WQbVewur_aEEceH_VbwgMdpCpcDitZI61lN2_Tm0IJ7CKSOwSmmG0audjwoRxuOL0P2aAZ9beKeHupQg01xfvkKMUOJxz0WuVScmpTHxfFWt9WCyH3EQrghMxyW80_JaBRezVpD7qDfvKv5lLI7JnMfp1VNqNH7OgeirDNRE0OtzigWBRFA1v6lOYCn5cyLpV8xBlxASayJR5vbWFW-NPk-3cNHvLgLWsnw59oX1K8jipddUbwLkRUEGSHSyDAizohn94vxPaxna1WYycN8_nbIDKoOyEcAgVbxv-e_kACbysGAXUmML2ulh9mzRQLCuOllFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زبان برنامه‌نویسی Cyrus(کوروش) چیست؟
سایروس یک زبان برنامه‌نویسی متن‌باز و جدید است که برای ساخت نرم‌افزارهای زیرساختی و سیستمی طراحی شده؛ یعنی همون نوع نرم‌افزارهایی که نزدیک به سخت‌افزار کار می‌کنن و به سرعت و کنترل دقیق نیاز دارن (مثل سیستم‌عامل، درایور، یا ابزارهای زیرساختی).
فلسفه اصلی سایروس این است: هیچ اتفاقی پشت پرده و بدون اطلاع برنامه‌نویس نیفتد. یعنی کد باید همیشه روشن و قابل پیش‌بینی باشد و برنامه‌نویس دقیقاً بداند هر خط کد چه کاری انجام می‌دهد، بدون رفتارهای پنهان یا پیچیدگی‌های اضافه.
چند ویژگی مهم سایروس:
بدون گاربیج کالکتور
: بر خلاف خیلی از زبان‌های مدرن (مثل پایتون یا جاوا) که حافظه رو خودکار مدیریت می‌کنن، سایروس این کار رو به خود برنامه‌نویس می‌سپارد. این یعنی کنترل کامل و دقیق‌تر روی مصرف حافظه، که برای نرم‌افزارهای سریع و حساس خیلی مهمه.
کامپایل مستقیم به کد ماشین
: سایروس از فناوری معروف و قدرتمند LLVM استفاده می‌کند تا کد رو قبل از اجرا به‌طور کامل به زبان ماشین تبدیل کند؛ نتیجه‌اش برنامه‌ای سریع و بدون واسطه است.
سازگاری استاندارد با سیستم‌عامل‌ها
: طوری طراحی شده که به‌راحتی با نحوه‌ی کار سیستم‌عامل‌های رایج هماهنگ باشد.
سینتکس ساده و مینیمال
: تلاش شده که نوشتن و خواندن کد تا حد امکان ساده و بدون ابهام باشد.
قابلیت‌های پیشرفته بدون هزینه اضافه
: مثل ژنریک‌ها (نوشتن کد قابل استفاده مجدد برای انواع مختلف داده) و چندریختی (Polymorphism)، بدون این‌که سرعت اجرای برنامه رو کند کنند.
ساخت افزایشی (Incremental Build)
: یعنی موقع تغییر کد، فقط بخش‌های تغییر‌کرده دوباره کامپایل می‌شوند، نه کل پروژه؛ این باعث سریع‌تر شدن فرآیند توسعه می‌شود.
هدف کلی سایروس این است که زبانی باشد نزدیک به سخت‌افزار و ماشین، اما بدون این‌که خوانایی و سادگی کد قربانی شود.
این پروژه هنوز در حال توسعه است و به‌تازگی نسخه بتا (Beta) آن منتشر شده. اگر دوست دارید بیشتر بدانید، امتحانش کنید، یا در توسعه‌اش مشارکت کنید:
مستندات:
https://cyrus-lang.ir/en
گیت‌هاب:
https://github.com/cyrus-lang/Cyrus
کامیونیتی:
@cyrus_lang
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/4293" target="_blank">📅 18:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4292">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آخرش یا atomic mail ایرانو بن میکنه یا ما atomic mail رو از کل جهان ابیوز میزنیم
😂
😂</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/4292" target="_blank">📅 16:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4291">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دیروز و پریروز می‌خواستم ویدئو بذارم، اما با اینکه موضوعات زیادی دارم برای ویدئو ساختن، حس کردم که کمی عجولانه‌ست و تایم گذاشتم که هم خودم کمی بیشتر با ابزارها کار کنم، هم وقت داشته باشم برای مطالعه‌ی شخصی که محتوای باکیفیت‌تری ارائه بدم. برای همین تا وقتی حس نکنم کافیه، ویدئوی جدیدی منتشر نمی‌کنم
❤️</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/4291" target="_blank">📅 16:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4290">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ghTuKw8pNkg3LkSsFxcPGm5aKmNK5SZKevFEvatxgMZ7irfKliPEkg8ai6bfezUOxnoVWUaA_6wZ6bIcT64BcgezLt0b5sGMZGOchpsSdAFE-XnB3zFS32ceABXL2nliRXZX94ASF0XtF9CP_qoUUJjw9gaIunGJvAIgKwMtNGEAfOJ5-gK4MlzhU-Q202XrYQXXmtk_Jpmd-Mer0-KxSY23TsylOcJoH8JgrN2LtsBSg7XddwRIyTANvs-7-TZfzT7O_EMO89Bg6ztf2iCORrST--Fe8ObMKhiPRbZfUsuRz0VpY05dh4QtfSdeN7g0WgeZiZIp0em5KvhKNZs2Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا هزاران پست سیو می‌کنیم ولی هیچ‌وقت نمی‌خونیمشون؟
🤔
اسم علمی این رفتار
Digital Hoarding
(ذخیره‌سازی وسواسی دیجیتال) یا "
پارادوکسِ بعدا می‌خونم
" هست.
این اصطلاح رو اولین بار
Van Bennekom و همکارانش توی سال ۲۰۱۵
و داخل یه مقاله توی مجله‌ی
BMJ Case Reports
مطرح کردن؛ اونجا یه مورد بالینی رو توصیف کردن که یه مرد ۴۷ ساله هر روز حدود ۱۰۰۰ عکس روی کامپیوترش ذخیره می‌کرده بدون این‌که هیچ‌وقت سراغشون بره.
از اون موقع، این پدیده به یه حوزه تحقیقاتی جدی تبدیل شده. تحقیقات جدیدتر (مثل مطالعه‌ای که سال ۲۰۲۳ توی مجله
Journal of Obsessive-Compulsive and Related Disorders
منتشر شد) نشون می‌ده Digital Hoarding با الگوهای شناختی و هیجانی شبیه به اختلال وسواسی-جبری (OCD) و وابستگی هیجانی به اشیاء مرتبطه؛ یعنی حذف‌کردن یه فایل یا پست، همون حس ناراحتی رو ایجاد می‌کنه که دور انداختن یه وسیله فیزیکی.
چرا این اتفاق می‌افته؟
👩
هر بار که پست مفیدی رو سیو می‌کنیم، مغز دوپامین آزاد می‌کنه؛ حس «پیشرفت» بدون این‌که واقعاً کاری انجام داده باشیم.
✈
ترکیبی از
FOMO
(ترس از دست دادن اطلاعات) باعث می‌شه به‌جای مصرف محتوا، فقط جمعش کنیم.
💤
نتیجه؟ انبار دیجیتالی از Save‌ها و بوکمارک‌ها که عملاً هیچ‌وقت سراغشون نمی‌ریم.
چندتا راهکار عملی:
قانون 5 دقیقه
: اگه محتوا کمتر از 5 دقیقه وقتتونو می‌گیره، همون لحظه بخونید؛ وگرنه رهاش کنید.
سقف هفتگی
: حداکثر ۵ تا ۱۰ آیتم توی یه هفته سیو کنید تا تلنبار نشن.
دسته‌بندی و پاک‌سازی دوره‌ای
: هر چند وقت یه‌بار Saved items رو مرور و پاک‌سازی کنید.
اگه واقعاً مهمه، به‌جای سیو کردن، همون لحظه یادداشت بردارید یا اجراش کنید.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/4290" target="_blank">📅 16:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4289">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آخرش یا atomic mail ایرانو بن میکنه یا ما atomic mail رو از کل جهان ابیوز میزنیم
😂
😂</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/MatinSenPaii/4289" target="_blank">📅 15:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4288">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cIpELbjZ4s03UhcYQQ2i45-Mefcy-2Cler2JhXsB7bdJ7GBze1AUb8TaBvbIWYZkxtDuD615H3JOmvISG_jAr1cTvKfFlRJnJgyt8ladI6SPkLSAdKqTmWef5zA6nLuS7ELJc7R1hCY1hKRX8KL55GHGFmxc02XCBTTm1TktKQEdp4uRgLY6CPMC2adBCDZw6sbaR42J5jACiz71lfRWhK2kagp__Fwoe-bw_dpe5gFOm5UYQfLFkNvh9xTR9YpNAKn8XOVrxxVLejKI09sjFFUQnddpjTZyT70NUiEwsW3dgLX9tJaB2hVxJWClc4aJN2L4hP9Xez9KA_qkUPk8Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس نتونست لینک مقاله‌ای که بهش دادم رو باز کنه به خاطر firewall امنیتی توییتر، خیلی راحت با قابلیت Browser که اینجا: https://youtu.be/_30_ng3Hyfs یاد دادم، روی دسکتاپ برام هم عکس‌هاش رو دانلود کرد هم مقاله رو کامل ترجمه کرد:)</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/4288" target="_blank">📅 14:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4286">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rH-PJqWq_2BodoCNiI8_yXiNnJxvQteUTuaJ5HAC2kwX74V80vM4qIhRjNAJFV0Ms8CQb0g8NG9CzZfIWH-ykSjkhyM7To3oRoeIWQ8G5zyoDBZ2ukrL_GGMP5CoN4B49DdQ-oIv_CLdmbZJsYB0r6G0W1Kor-926DPGdGfyt-cfNny-F9qRTaFbCsMQ7qTG1-t4Eotbx-985oJ-sPQQWkrb1tLLI5BBqNeRMdzlI987MzRWaj6-NYiZBtHaeHI8LQxwpr9eEJZgZ-cxuZNn5TDPiK81rfpuolFsARuxjLQ3TlACXey9vVBfrxemZTGfT53s072mrPi0xuQbuKsQVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vJv2b_4YQs6xUfyEGTRMv6D0Q9toxRaZ8gDNzGNOjEmWGGAM-LvrgS0zSwGBakU-8zr6TaFbeFT8HNUQOt_c8LVhbmANLi2-Uw58FIOv8RbC9Vzp5YVfsnMgdMB2Z-qvVOXA0zVNbPUQBOshonsppQktmyaCmW1BBiuqJia6DKdXFy90QHxjCPWgojvbiOdYXHgPfVHKMht-SYVM2gXL0LGYqUcHjVODHsvCEYV-rTXUz47rhOs519LSiEqjaJM8eGDP73_qURNQ4yS1yf6YtNiYVIs2yQ-cFKyQbRxwyPpP_LDh_jnYSHtZfuYQTrlMyMDNxC5q2eKuOUdDurN_WQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هرمس نتونست لینک مقاله‌ای که بهش دادم رو باز کنه به خاطر firewall امنیتی توییتر،
خیلی راحت با قابلیت Browser که اینجا:
https://youtu.be/_30_ng3Hyfs
یاد دادم، روی دسکتاپ برام هم عکس‌هاش رو دانلود کرد هم مقاله رو کامل ترجمه کرد:)</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/MatinSenPaii/4286" target="_blank">📅 14:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4285">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OB9a3abgJ1XByMPCWnv8H-PcBFTdLvCpS4_XvVCi-Pz-oF37I8TrOczwigDpXlDYw7EoRFMmZ95G7ibGEKSuu3Mc3oxfEIwQJKuVDCZ6D5VPbu8aiKXxf7QnHx6ECuUaBfkkr6z6i0fpfY0qVjMxKQ5S6seGiVmERe2FM4Pwk74PFmmzbVmUTV6Nt-nTy3bn6VVumrSf_H8tHQg2dkPZkHcpn9iOU6ItBrcoxlYL4_2XcSHPivrSS1n56qRfTekNsePFwkYZCJ5JwEFRMRWy_8CHC-UIoePYOd6cyhYwlwWQueH8knuVpz9xvaFytX3K9rFsCDXQXlYZeaGi5zw3Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه با docker کار می‌کنید، احتمالاً درگیر زدن پشت‌سرهمِ دستوراتی مثل
docker ps
و
docker logs --tail 50
هستید تا چندتا کانتینر رو همزمان مدیریت کنید. این کار هم خسته‌کننده‌ست و هم ترمینال رو به هم می‌ریزه.
ابزار
Lazydocker
دقیقاً برای حل همین مشکل ساخته شده؛ یه TUI برای داکر و داکر کامپوز که تمام کارها رو با شورت‌کات‌های کیبورد براتون انجام می‌ده.
-
بدون switch کردن:
همه چیز از مصرف منابع (RAMو CPU) تا لاگ کانتینرها به صورت زنده توی یه داشبورد یکپارچه نشون داده می‌شه.
-
سرعت بالا با کیبورد:
لاگ دیدن، ری‌استارت کردن یا پاک کردن کانتینرها فقط با زدن یک دکمه کیبورد انجام میشه (بدون نیاز به موس).
-
پشتیبانی کامل از Compose:
سرویس‌های داکر کامپوز رو هم به خوبی می‌شناسه و مدیریت می‌کنه.
-
بدون کانفیگ:
با زبان Go نوشته شده و فقط یه فایل اجرایی باینریه؛ نیازی به نصب سرور یا دیپندنسی اضافه نداره.
و خلاصه این ابزار سرعت کارتون رو چند برابر می‌کنه.
گیتهاب Lazydocker  + آموزش نصبش
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/4285" target="_blank">📅 14:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4284">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اگر روی هرمس برای اتصال به api به مشکل VPN برمی‌خورید، از تکنیک رایگان وصل کردن پروکسی کلودفلر که توی این ویدئو توضیح و انجام دادم استفاده کنید: https://youtu.be/Ae8oyaIHi9o</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/MatinSenPaii/4284" target="_blank">📅 13:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4283">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پیرو ایمیل یکی از بچه‌ها، تست کردم، با موفقیت بدون شماره مجازی و با atomicmail فیک تونستم api key رایگان Nvidia بگیرم:  سلام متین خوبی داداش متین به خدا شوخی نمیکنم همه میگن سایت انویدیا برای اینکه Api بده باید شماره مجازی بدی و از این کارا من تو گوگل سرج…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/4283" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4281">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GaM937gzOlMixdOTm-9aypNdNi9sARbhRAxbCGTUcbIh9OxYzSK2_DNz8Pdwpj6U1Jjrz26_B8aSAsEUpU4q9fnedckozhJtjW1udNc2KPUTXL8qpJIpU5ofwO2pe5KMRfCJLzZ6SH2VBzyfJVTNnuGqRoC2sjco5LIl5fBdoOs6FF9_llxLcLRBYKpbPp8aBqmmmNow1-DkMLTsN9iTkDkBI0A1FmHfNqLvbeH3DOkGIyLfsyiahW6m5gka3pzCJnZGP2qQN1k47WVxiXNIE5emokdp4tsgVp7vWwaA9XrAU-UDjv9gmHlBeGw3eytLuPnyTt4eLTEFAQZpu1U2Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cLNmMuOycOp1NNs3bu_HZ6jtMSVsYeYHcuVEIWf0BepR1ZPXRPN8XiOoTJyOHuv0zb2ClNPCtWIbuqcuQ9jH9j0C8khBFVugXHvxwogR50l1Ko_TuWMywVGVfyKp1ATuRkCVobQxXhTK7BWdR5jCiF0C0y72lW33VDLpTfFPvFUFtPIV3QmTjQqdlsCnPD7ZLI4xailaGrB4XeE4dZbNRvf3E__vC6sRCl4goSu7Pb7Pk_JqW1MtUzPQrU0V8zMGIsnAIC289j0hlIDjFtdSOc0sM-D2zBxBwyaKNeambk1ez9G9PxjVBBsA3QUamS7OpjmNq7e8VMDZd2gWrDgpuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیرو ایمیل یکی از بچه‌ها، تست کردم، با موفقیت بدون شماره مجازی و با atomicmail فیک تونستم api key رایگان Nvidia بگیرم:
سلام متین خوبی داداش
متین به خدا شوخی نمیکنم
همه میگن سایت انویدیا برای اینکه Api بده باید شماره مجازی بدی و از این کارا
من تو گوگل سرج کردم و هنوز هم شماره مجازی نخریده بودم
https://build.nvidia.com/settings/api-keys
ببین دقیقا ادرس هم برات گزاشتم
تو گوگل سرچ کردم Nvidia Get ApiKey
بعد سایت اومد بالا ازم ایمیل خواست
تازه atomicmail وارد کردم ایمیل گوگل هم ندادم
بعد که وارد کردم منو برد تو یک صفحه ای یک کپچا داشت تایید کردم و رمز عبور خواست اونم اوکی کردم
بعد گفت نام کاربری رو وارد کن اونم وارد کردم
منو مستقیم برد تو صفحه apikey ها و استفاده هم کردم
با تشکر از محمد عزیز. نمیدونم انویدیا وریفای رو برای ایمیل‌های شخصی برداشته یا اینکه کلا برداشته</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/4281" target="_blank">📅 11:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4280">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اگر روی هرمس برای اتصال به api به مشکل VPN برمی‌خورید، از تکنیک رایگان وصل کردن پروکسی کلودفلر که توی این ویدئو توضیح و انجام دادم استفاده کنید:
https://youtu.be/Ae8oyaIHi9o</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/4280" target="_blank">📅 11:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4279">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یه پروژه‌ی خیلی عجیب روی گیت‌هاب (با اسم Pon) منتشر شده به تازگی که تونسته پایتون ۳.۱۴ رو مستقیما به کد ماشین کامپایل کنه و دیگه نیازی به Interpreter و مفسر نداره. این برای پرفورمنس پروژه‌های پایتونی می‌تونه یه انقلاب باشه
👍
https://github.com/can1357/pon
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4279" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4278">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یکی از دوستان رو اون روز باهاش صحبت کردم، برای یادگیری فرانسوی داشت از Hermes استفاده میکرد در کنار منابع و ... دیگه‌اش. و به شدت راضی بود و می‌گفت حس میکنم بازدهیم چندین برابر شده
جالب بود برای خودم</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4278" target="_blank">📅 02:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4277">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یعنی حس خوبی که وقتی از api رایگان در سطح کلان(
😂
) استفاده می‌کنی، با هیچی قابل مقایسه نیست. فکر کنم Open Code ازم شکایت کنه اینطور که دارم توکن میسوزونم</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4277" target="_blank">📅 00:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4276">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یعنی حس خوبی که وقتی از api رایگان در سطح کلان(
😂
) استفاده می‌کنی، با هیچی قابل مقایسه نیست.
فکر کنم Open Code ازم شکایت کنه اینطور که دارم توکن میسوزونم</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4276" target="_blank">📅 00:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4275">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d956281ee.mp4?token=u-EXjjps-tfFmJecEgHxyD8CMoYzVL4zdn8LL14qZ-vgxihDboT--d2MWMNfsySC2Rn30HmgKOuItGXOuLNKELNZF5TBnDG3g-S8PsVs70bAsu0tWkL4qWzZy2J2uEnp1f-kOQyjJXshZJvlXQFNmwL3R0ALqBvJQPNrcIyLNiWLTEnEA1H1Bp8GW4Av1MDVwi0-nw3LT04nuhbgwYzWpXJwhysABBSvXpbY7UDd7wiPon6qlkWUjlCCv_pZttFOzwtsk7XLMaQfdgWL7l6qcyqYA2jzIcvO2SPXxfcLhAnOWAIB4u5KMZFvPYlB9XpNLs79hhQiUO8mVj8xeI0Orq0NU1-uOLd1q_7qgj-dLnUIr7m6bjMaaYKXzzVftqg2ZrVFGFGh95ZFj4tUwmurnZ6LdZUit1ckeU6tliQ8JHiTREti77Ci-TTxXQq-aY_0swf_8z22jzETRtF7KoV-w78PLUh0l2VoH93t270DsdG238BIGuVFYNiL1NNAOukFk9rxJIxJdOt_J4lA4kM6Wt3necRQUoNI2dlG6Wy-ne2Z-SDqNQIQItZl6EKyl-1S22PYZo5a3ovfOpbIL9FSlmItNL2pByutkjzD_nuptDy0CHvKKJtF6r_o3SXuGbvufECpN1IH46gT2hy5RLQj3wcVgLQXzuxrrxb22NehxvI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d956281ee.mp4?token=u-EXjjps-tfFmJecEgHxyD8CMoYzVL4zdn8LL14qZ-vgxihDboT--d2MWMNfsySC2Rn30HmgKOuItGXOuLNKELNZF5TBnDG3g-S8PsVs70bAsu0tWkL4qWzZy2J2uEnp1f-kOQyjJXshZJvlXQFNmwL3R0ALqBvJQPNrcIyLNiWLTEnEA1H1Bp8GW4Av1MDVwi0-nw3LT04nuhbgwYzWpXJwhysABBSvXpbY7UDd7wiPon6qlkWUjlCCv_pZttFOzwtsk7XLMaQfdgWL7l6qcyqYA2jzIcvO2SPXxfcLhAnOWAIB4u5KMZFvPYlB9XpNLs79hhQiUO8mVj8xeI0Orq0NU1-uOLd1q_7qgj-dLnUIr7m6bjMaaYKXzzVftqg2ZrVFGFGh95ZFj4tUwmurnZ6LdZUit1ckeU6tliQ8JHiTREti77Ci-TTxXQq-aY_0swf_8z22jzETRtF7KoV-w78PLUh0l2VoH93t270DsdG238BIGuVFYNiL1NNAOukFk9rxJIxJdOt_J4lA4kM6Wt3necRQUoNI2dlG6Wy-ne2Z-SDqNQIQItZl6EKyl-1S22PYZo5a3ovfOpbIL9FSlmItNL2pByutkjzD_nuptDy0CHvKKJtF6r_o3SXuGbvufECpN1IH46gT2hy5RLQj3wcVgLQXzuxrrxb22NehxvI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
آموزش کامل Mahsang VPN | تنظیمات جدید CDN Fronting و اتصال پایدار
اگر می‌خواهید با روش جدید اتصال Mahsang آشنا شوید، این ویدیو را از دست ندهید.
✅
آموزش نصب و راه‌اندازی
✅
تنظیمات کامل CDN Fronting
✅
روش جدید اتصال
✅
بررسی تمام گزینه‌های مهم برنامه
✅
نکات افزایش پایداری اتصال و رفع مشکلات رایج
اگر قبلاً در اتصال یا تنظیمات Mahsang سؤال داشتید، احتمالاً پاسخ آن را در این آموزش پیدا خواهید کرد.
🎥
ویدیو را از کانال TakTarfand ببینید و اگر مفید بود، برای دوستانتان هم ارسال کنید.
لینک مشاهده ویدیو در یوتیوب :
https://youtu.be/35-GhIi-egg
@mobamoz_channel
⚡️
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/4275" target="_blank">📅 23:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4274">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام
❤️
توی این آموزش، تمام بخش‌های برنامه V2Ray را از مبتدی تا حرفه‌ای به‌صورت کامل بررسی کردیم؛ از اضافه کردن کانفیگ و Subscription گرفته تا تنظیمات پیشرفته، Routing، آپدیت برنامه و حالت‌های مختلف Tunnel.
🇺🇦
لینک آموزش در یوتیوب:
https://youtu.be/i1-XenoSalk?si=5jbQK3BrGAe4ctsu
اگر موضوع یا نرم‌افزار دیگری هست که دوست دارید آموزش کاملش را ببینید، داخل کامنت‌های یوتیوب یا گروه تلگرام پیشنهاد بدید تا برای آن هم آموزش تهیه کنیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/MatinSenPaii/4274" target="_blank">📅 22:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4273">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">توی همین 5 دقیقه شد دو میلیون</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4273" target="_blank">📅 20:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4272">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kZlk9dB3XIU9CnY9rXTLdbAOzimd3tEKLhWVKGjCvPOkrThS3JaLWPdCHwORDhoQZfuhGVY6vfBmVDTX2gBB8QCZ8LFnNKCO2_41vUf9rWcqxwOMGUh65nFX_6aPJU4AZyjfycOMOuopAC8LWfFuhBrpq9pdAV0UNKQRav0qprz6-bDguvWUH-VEgDYm3hvbnykThsZrN4b-mFnJ5gqQR-j_vEk2bhQTNEKKNep8o7ndnTyajfSQUqimRPNUDjE6ceylqcnwL1duIR2EbHsk8nfSaHbj5m7GlnixHanglVGHhHCkp-3dRQPvpUSbnMKVfjSIpLWOYDWHeZO-XYvulg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه جوری داره توکن می‌خوره که واقعا توصیه میکنم همچین کارهایی رو با api پولی و اشتراکای محدود مثل claude pro انجام ندین درود بر چین
😂
😂</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4272" target="_blank">📅 19:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4271">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N1x3BfPFnFHHIdJeX0rVk8m-zhM8aiL-4Ywb0y8UF6EXYu5ZsU4B2pQciQaUdUV-s4FOqqaStEqiVxEAtD5h2hsSBx7vnUmFepMfZzPk3oswxfnoz9X1TiR3sQ0UEq_hC-mV88adXmE_16AhaGcyD2s7XniDnoKh2BJ1C0JhMOJrdHkuBO6DssCD8MUIVcIZkCcYnNaCB-8iB9yYsxUp16PfUEi3Md2F7vgd8K6AVzci23QSSnXOD7IycxI7zZfzQNxgJG9XSp9ycgXtRUCqfmrFaEbG-mqPV_ycZBE5xf5c3NYkCzV6oPQkcf7QULsRZFd5Y6ipaMnP5g79lAcJVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه جوری داره توکن می‌خوره که واقعا توصیه میکنم همچین کارهایی رو با api پولی و اشتراکای محدود مثل claude pro انجام ندین
درود بر چین
😂
😂</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4271" target="_blank">📅 19:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4270">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M338fNN5ZfoQA1P_kGLdOxAmSZG1cPDgQI3_q2H3Qgcng0ghGN6O00iTbxjmGolrJriRWhmPrYzu1e5eAdB9446P-5P1nVvnoM4vLtJoPQsEEmhWfEiZkz3-vwmtr5HyYXg1Nf1Brm5ZbdsK3xmw6sEdDPUB3xVzcby5Etwy2wLzp5cKvCsC2lwnkoyRFdEQmwmT_lbjPsi5MYw_PtIksR0j7QGkYaDxljZ9LwgcdBHrZABmfWocijt5LGK6NBSQEGubs80KoPNWdQNjWEfIbr6yLvVMSzYd6kR29SOVQQUT-SJpvpXFURXqXQdSOGtyOc_11OYllNMKTvBOMYlOjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب این قراره خیلی باحال بشه
😂
برم ببینم تا چه حد پتانسیلشو میتونم بکشم بیرون</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4270" target="_blank">📅 19:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4269">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PR7GGCFj6f6eZA3b21V2K39JK0um38GdLDPmhzDA5q-2W4X2Hl7Uz9PlNI5fnNSaeCYtfCXnnRvXZbwbJh3axaB-_mslQZY5pXrKl66wDXbVEl20R0iVF5CuQVcemMpkNQzUWrV0xMkDqZKC2UazNLBLZPbenOGalCNEcjSykVrzeI3uxF1h1RiujjUbroxMBQfE9KEXZjsjSGHVWOHE8HCxqkE6I3G4RWhX24TVbizKotaHdXwZFIxo86e0tyH7Ohqe0Xk94wxCgmosHrx5b6wmdKtyD2tzd-9w4w0dTFguympk1iqVZ-jCoxRLhbhHI_gtBV6pTbETr-mNaHUq-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب این قراره خیلی باحال بشه
😂
برم ببینم تا چه حد پتانسیلشو میتونم بکشم بیرون</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4269" target="_blank">📅 19:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4268">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ANhPAByzDjKoQwEjvdi9A3XxJi-oW86Jy8Zam2_F2Lk7lBBqtdDhHHeOX0ZDQmkPQuC21ylXueR5qk-AfvEeLCxnuLmKEicF0hiB9I5AdHKqimWmcgJwSHR7a725jcZjWukEpb2SiAJy3RAnhjtazXY0Ad4vw8HoZKhUupyuc6CazxpervR4POilJQYFcDNfTnsYCY6TyvyItbi7VXEoycHEgyNpH5SSwXk6xFK-86ogUCgxzc3AiNsqdCAkYgorGcwqQzwWGfdBKgoJc5JYl-CzGREez3oW8kxYrGBqL324LfhNY-VxfQYgJhoxyoVacAPvEcgSlmT2KaBXFzpCjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به زودی احتمالا به Hermes اضافه بشه برای کارای روزمره
😁</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4268" target="_blank">📅 16:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4267">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خیلی از بچه‌ها به من ایمیل دادن که متین چه مسیری رفتی؟ یا برای اینکه توی حوزه‌ی ai یا برنامه‌نویسی یا شبکه یا... وارد بشیم چیکار باید بکنیم؟  اولا که خیلی لطف دارید به من، اما من هنوز خودم مشغول یادگیری برنامه‌نویسی و کامپیوتر هستم(که به زودی با کمی اوکی‌تر…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4267" target="_blank">📅 07:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4266">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4913b2f340.mp4?token=Udp7wZRw_MFK6Q9_PBGYWUV-toqK7ISTjgTbppvtLPx3vO_t2Kcs3AV5UtZG2evrp9A1TsA1TpGs0RXLu3cllD_lu-6aKEzMt_L2qIZC_nM3eeI-ZvDc72kHN9PbQBvbOxJ4Q_1ZBT6CNOzsft7-IL3Veqp4YKExvyvO-ObdyzYZkVW7gLO8WKJ4cRewoFXJBcYvgDN0fPL-gSyOrbGJBOW-Ho6_vzQ-sCDyqoInXcJMD5bPS32UguAsaIgg_FutrEeO1ik7qF5guNn6aDeTdlqrGLYz45tF8EiHVI4pfBicSBaDdQcVKHgsqle_u1XbmzRaM6FQtE_yG3zPJeOxWg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4913b2f340.mp4?token=Udp7wZRw_MFK6Q9_PBGYWUV-toqK7ISTjgTbppvtLPx3vO_t2Kcs3AV5UtZG2evrp9A1TsA1TpGs0RXLu3cllD_lu-6aKEzMt_L2qIZC_nM3eeI-ZvDc72kHN9PbQBvbOxJ4Q_1ZBT6CNOzsft7-IL3Veqp4YKExvyvO-ObdyzYZkVW7gLO8WKJ4cRewoFXJBcYvgDN0fPL-gSyOrbGJBOW-Ho6_vzQ-sCDyqoInXcJMD5bPS32UguAsaIgg_FutrEeO1ik7qF5guNn6aDeTdlqrGLYz45tF8EiHVI4pfBicSBaDdQcVKHgsqle_u1XbmzRaM6FQtE_yG3zPJeOxWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه ابزار رایگان رو دارم تست میکنم ببینم هایپی که دور و برش هست اصلا واقعیه یا نه و اون عملکردی که می‌خوام ازش رو با مدل پولی مقایسه می‌کنم، اگه خوب بود بهتون یاد میدم</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4266" target="_blank">📅 01:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4265">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رفقا
freemodel.dev
گویا api رایگان از claude opus و اینها میده، منتها به هیچ وجه سایت امنی به نظر نمیرسه. استفاده کنید اما نه برای پروژه‌های حساس و چیزی رو در اختیارش نذارید. روی هرمس شخصی و لوکالتون هم ترجیحا نزنید.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4265" target="_blank">📅 00:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4264">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">متین واقعا باهوشه اولش بهم گفت برو فلان ویدیوم رو تو یوتوب ببین و تمرین کن و وقتی دید اینکارو نمیکنم گفت خب باشه خودم بهت یاد میدم تو کلاس. بعد جلسه اول بهم گف تکلیفم دیدن سه تا از ویدیوهاش و ساختن چیزایی که توشون یاد میده‌ست. و همشو هم باید تا جلسه بعد تحویل…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4264" target="_blank">📅 00:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4263">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">متین واقعا باهوشه
اولش بهم گفت برو فلان ویدیوم رو تو یوتوب ببین و تمرین کن و وقتی دید اینکارو نمیکنم گفت خب باشه خودم بهت یاد میدم تو کلاس.
بعد جلسه اول بهم گف تکلیفم دیدن سه تا از ویدیوهاش و ساختن چیزایی که توشون یاد میده‌ست.
و همشو هم باید تا جلسه بعد تحویل بدم</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4263" target="_blank">📅 00:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4262">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">Matin SenPai
pinned «
خیلی از بچه‌ها به من ایمیل دادن که متین چه مسیری رفتی؟ یا برای اینکه توی حوزه‌ی ai یا برنامه‌نویسی یا شبکه یا... وارد بشیم چیکار باید بکنیم؟  اولا که خیلی لطف دارید به من، اما من هنوز خودم مشغول یادگیری برنامه‌نویسی و کامپیوتر هستم(که به زودی با کمی اوکی‌تر…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4262" target="_blank">📅 23:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4261">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">برای نصب کردن 9Router روی سرور اوبونتو اول sudo apt update && sudo apt upgrade -y curl -fsSL https://get.docker.com | sh sudo systemctl enable --now docker و بعدش این دستور رو بزنید docker run -d \\   --name 9router \\   -p 20128:20128 \\   -v "$HOME/.9router:/app/data"…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4261" target="_blank">📅 23:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4259">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XYwLfHUHJPayQrnCBq9vCUiK4Lq-51Wplvn-dCEGoYKzwUqc1wf-vINHIVT0u4mUSU-sC2v_Q1_6dCJ5rbDve6frmRMrXBWJ4VwJV9D1iIFQwHMHzWBR8UXVK42sP6pt_kFnmWXlgv31SGtARIO0GAAf32pnBT7ZK2kFnJa7gMnQzNyK2D5i0Z9m_e7WN8J0otNEnVLaiYpb_6diFVUu7qEblXMrQ3uXpazbMqNrDDkyDfQe6DAU-S4T4wTJ3N4VI_0hZFxQWzrmT_VZHsmcyvEqX5lmBnpRjkfbdzIrifj__IUUoogRlrzy61b3JYmenDfXVq19Gsp6YuU3jm4o2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HaVPZnJyOVpGBO7o5QY8AAh4ocsXOmtKNUgRh1ak63DfE8i_ryzzX9JPzVTx3zouWkCabf0tVXnrC1s6eT6Tl3XCStfj34YG03vvnrdq-cU0TUe__JvZgg6nQY51oM_Tq3RcavF8yoT-53n2RtMIZLsTyz7BhplOzw7oGVdSAe3BxXDF-XVrGAxhuzvaQVQ9fVkFU-PbyFMGD99xadHyhIGlodkI0autnNmSbh78ArDQknQ6t-6xNxc_fkuiPCdSP4ktupccCVlWn29EfeV-GLCPfsvd1saPe0gXOFvBNCYx8mvNymg5fUP_6HkBboFvAO_MBjpTUzpYJ-A-JL1_UA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من عذرخواهی می‌کنم از همگی. حق با شما بود. متاسفانه درست بود و الان برای من هم پولی شدن مدل‌های Mimo روی Nara:) گویا سایتشون باگ داشت فعلا از Open router + Nvidia nemotron استفاده می‌کنیم</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4259" target="_blank">📅 22:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4258">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یه ابزار رایگان رو دارم تست میکنم ببینم هایپی که دور و برش هست اصلا واقعیه یا نه و اون عملکردی که می‌خوام ازش رو با مدل پولی مقایسه می‌کنم، اگه خوب بود بهتون یاد میدم</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/4258" target="_blank">📅 22:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4257">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">امروز اولین جلسه ی کلاسم با متین برگزار شد و واقعا دوسش داشتم
🌱</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4257" target="_blank">📅 22:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4256">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خیلی از بچه‌ها به من ایمیل دادن که متین چه مسیری رفتی؟ یا برای اینکه توی حوزه‌ی ai یا برنامه‌نویسی یا شبکه یا... وارد بشیم چیکار باید بکنیم؟
اولا که خیلی لطف دارید به من، اما من هنوز خودم مشغول یادگیری برنامه‌نویسی و کامپیوتر هستم(که به زودی با کمی اوکی‌تر شدن شرایطم، راجب خود برنامه‌نویسی هم ویدئو داریم) ولی در حدی نمی‌بینم خودمو که بخوام توصیه بکنم جدا؛ دوما در حال حاضر، فعلا خودمو نمی‌تونم هنوز متخصص هیچ حوزه‌ای بدونم. که اصلا بخوام راهنمایی‌ای بکنم توی هر حوزه‌ای. خیلی افراد بهتری از من هستن که بخواید سؤال کنید. اما یه سری نکات رو می‌تونم بهتون بگم که خودم با تجربه بهشون رسیدم و شاید مسیرتون رو کمی کوتاه‌تر کنه:
۱- دنبال پرسیدن مسیر از من و دیگری و این و اون نباشید. اگر توی این چرخه‌ی باطل بیفتید و هی دنبال ویدئوهای مصاحبه‌های آدمای معروف راجب زندگیشون برید مثلا زاکربرگ و بیل‌گیتس و... یا حتی پادکستایی مثل طبقه ۱۶ آقای علوی، هیچوقت نمی‌تونید اون چیزی که دنبالش هستید رو پیدا کنید.
صرفا برای اینکه گوش‌ـتون به یه سری اصطلاحات این حوزه عادت کنه این چنین پادکست‌ها و مصاحبه‌ها رو ببینید.
۲- شما الان AI رو دارید رفقا. می‌تونید به راحتی بپرسید، Roadmap درست کنید برای خودتون، شروع کنید به یادگیری، بعدش هم توی توییتر بیاید و وارد کامیونیتی برنامه‌نویسا/یا هر حوزه‌ای بشید، تایم‌لاینتون رو درست کنید و مشارکت کنید توی بحث‌ها، اشتباه کنید، یاد بگیرید، و...
۳- همیشه حواستون باشه که علاقه‌تون کجا ظاهریه و کجا واقعی. خیلیا هستن که دوست دارن «از اینترنت» یا «با کامپیوتر» یا «با گوشی» پول در بیارن، اما اکثر مردم وقتی واردش میشن تازه میفهمن نیم ساعت هم اعصابشون نمیکشه پشت لپ تاپ بشینن. عجولانه تصمیم نگیرید و راجب مسیری که می‌خواید برید، خوب تحقیق کنید
۴- توی یوتوب خیلیا آموزش‌های خوبی دادن؛ با ترکیبش با ai و مشورت باهاش و کاری که می‌خواید بکنید و هدفتون، می‌تونید به یه جمع‌بندی نهایی برسید و اون موقع هست که تازه می‌تونید نظر یه متخصص(مثلا بکند یا ai engineering یا حتی یوتوبر یا دیزاینر یا فرانت اند) رو بپرسید و اون هم برای صیقل دادن Roadmapـتون هست صرفا، نه اینکه بخواد صفر تا صد آموزشی رو بهتون بده. من هم خودم از خیلی از دوستان توییتر راجب بکند پرسیدم وقتی برنامه‌ام کامل شده بود، بعدش رفتم راه خودم رو ادامه دادم. وسط مسیر هم چند بار چرخید پلنم با پروژه‌های مختلف</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4256" target="_blank">📅 21:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4254">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FFmxgaw_WUtc5Wul5cWZMZWTVRUPPDLIPy8q6urhAV4VosH-JNEKVzKh9Es3JN849V72XSICLS1c2sTrU0PJ-j6jC4N8p3jyyxOLbC3fVquZ9Pt1ArLWI2LkURuJBj7WFlbgvEdss69r5pC7UYdcSYcwPxCnzH0Ws3mcOMkf7560IbQ3Y7LHiSdSHk6vTyhirokgyp7lADsO2vZet4ny5o5gWc_roV-i6zPCghCXw3B_t5-6S7yfNH2CI6962o9o5UIUzu-9IPgK7VbJGjG6aqEz6NFp_b4yzgNetl560kngm_aeG3-vAf62AA8vrj73eXXIWbvuLaa24YaPOxB9_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WhpCi7wvVCjyroBHycyEvd9SC1-xfitB9wiev5x6e5oITyPkU02oF9ri0QXNuZqJ58tIUl_-oazD2kDVwMBqwOCqxRPTG0kb8ropxPuLqjY66BCbd1Yu7IQtjhnLM-pFfitkV1uSrEv7dzsXNWaVncpEeuvJapXcKO-mT5AaFXu9sp8_NMoTCMDnJqic5YMwBbDbepqV-AWr1T9o2D_S3GyVdlYZ7rRZvOsyad0p6VypAOJ0nKzaK6FEZqGM422LP1BHMFYf1nhJT-0NpfHgwYKnbUIVWAo0nPe0TjmAuiCxt6UcKvqDbPUmj3wVdU-b3_uQ5U5gP_6qEJ75qb6Cjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من عذرخواهی می‌کنم از همگی. حق با شما بود. متاسفانه درست بود و الان برای من هم پولی شدن مدل‌های Mimo روی Nara:) گویا سایتشون باگ داشت
فعلا از Open router + Nvidia nemotron استفاده می‌کنیم</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/4254" target="_blank">📅 21:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4250">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhitednsProxyProfiler-Android-v1.0.7.apk</div>
  <div class="tg-doc-extra">55.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4250" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پروفایلر پروکسی WhiteDNS نسخه ۱.۰.۷
🛠
پروفایلر پروکسی WhiteDNS یک ابزار تشخیصی برای ویندوز و اندروید است که بهترین ترکیب‌های پروتکل پروکسی/VPN را در یک شبکه پیدا می‌کند. این ابزار می‌تواند هم بررسی‌های محلی بدون VPS و هم تأییدات عمیق‌تر مبتنی بر VPS را اجرا کند.
🌐
ویژگی‌های اصلی
اسکن شبکه محلی:
آزمایش سریع بدون نیاز به اعتبارنامه‌های VPS.
🏠
اسکن VPS:
تأیید از راه دور عمیق‌تر با استفاده از اعتبارنامه‌های VPS شما.
🖥
تست پروتکل‌های VLESS، VMess، Trojan، Shadowsocks، WireGuard، Hysteria و HTTP.
🚀
پشتیبانی از انتقال‌های TCP/RAW، WebSocket، gRPC، XHTTP، HTTPUpgrade و mKCP.
🔄
پشتیبانی از ترکیب‌های TLS، REALITY و بدون امنیت (در صورت معتبر بودن).
🔒
تشخیص دسترسی‌پذیری، فیلترینگ، پورت‌های مسدود شده، مشکلات SNI/TLS و رفتارهای شبیه DPI.
🔍
نمایش نتایج تشخیصی دقیق و اطمینان از شواهد محلی.
📊
کمک به شناسایی ترکیب‌های ایمن‌تر پروتکل، پورت، انتقال و امنیت.
🛡
نحوه استفاده
برای یک آزمایش سریع بدون VPS، گزینه
اسکن شبکه محلی
را انتخاب کنید.
⚡️
از
تنظیمات پیشرفته
برای تست پروتکل‌ها، پورت‌ها، مقادیر SNI، انتقال‌ها و انواع امنیتی بیشتر استفاده کنید.
⚙️
وقتی به شواهد قوی‌تر سمت سرور نیاز دارید، گزینه
اسکن VPS
را انتخاب کنید.
🌍
آی‌پی VPS، پورت SSH، نام کاربری و رمز عبور یا کلید SSH خود را وارد کنید.
🔑
اسکن را شروع کنید و پروفایل پیشنهادی کارآمد یا نتایج تشخیصی را بررسی کنید.
✅
نکته مهم
اسکن محلی نشان می‌دهد که شبکه فعلی شما به چه مواردی دسترسی دارد. اسکن VPS شواهد قوی‌تری ارائه می‌دهد زیرا هم سمت کلاینت و هم آنچه واقعاً به VPS می‌رسد را بررسی می‌کند.
🧐
نسخه:
۱.۰.۷
🏷
@WhiteDNS</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/MatinSenPaii/4250" target="_blank">📅 21:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4249">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بهم یاد داد از این وبسایت‌ها برای جزوه‌ها و تحقیقاتم درست کنم</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/4249" target="_blank">📅 20:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4243">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Eq_qJdWy0B2ZS2TbNT5Bhcr3fI3e0h2RSpZjVHJ-iaYDDcv1cnvvOGHk46PxFRzqRSlB9zal2zeIM68DTHAMlOe5V9UVZwhQZcs1hFPIEMSaqig59j0P94q4BG-9ATPdRzD9ndcMFbKtTsc-QWLO8uPn7iflthLhd7YiGk5lEOz5wXsxy2W6Jozvf6vjY19djZPBta_bYqKNVD47CtILeVDjb_IbQFmxPid31ILTdr71PoTp3kN_NqnD-cmuIG9QDUuAavp6cHLv8TRjJVVgRlALy3QDJTMBw-lTsGO9kf1x-nXkjTzuIPsyd5d_0GHU9sZsRo6CcqeTS5DAHqzF9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Wwuk5Ua3dkEUF7EQ1sQVO_2ftLRCmeJH2s6o9snxBirIzCMUWA16rPeKyw3hmxbDLo2ZVN5SaSBFJUrQ7BDnJeZMo3zV8Gr7XFk03St70Z0tI1iHoGPAatDauQAYCfssPGVtNpbTP95-aUdJsPdUMdS-ugRW3GB1TL7q_hcZdfE0WGvbeaCC49kAv1qkQtr3JBPHR11z3LcU7oOMZ9WL4i79pQguDkDDpmnPdZW-0a-irAjGkoZ18-VszpVwNeTaylw6bFsdgQLpvKDO0PRoRnKGu9NSzzVhyXRD_RbD43qfoBOTEZeseEKAfiXyE2kPPKlHMKH_zyLCHn4zOrwY2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JXlLw2e1YUHN8VdOOf3uClgqeTRa5uV7lKhfmIIjOhC_scMxH1N1qSQTv72PhxjsXnTrF6t8GktlFX0WlR66Yv6BnNXvvZieOt7O-4QxFzDeHGaOFsMgIY2ib3dQlhhHY1peuBNpB2tX40LTKCBXZE57AyZ1eT0XWKyBFH2J8vT2tJBWXhWDQVjkqFefrVKJIRLP6pJk7RjMZjuVXGyJAlgMzmkI6C8DdohD4lFEZ5QyTw7iNjOteBTxzxHy15YGPOgFUIr7GUVMOvrvmo8SzBmoSYfPkkUYPFOhjPsuGR1gXBBL9Dnyk7Pf99RTCwjD2gyOOhvWTuL8Ny3KyEo7sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/etq9a8dyEjPWszzQYXhgF0JqY9WHlg4sJ3ZrPPjOpA7eDYIg7IJvnE128nJuSY2XojQaBUpUCRiZT6eh-mDa1fEu7HaRQgQf3oSFYpEWvm6AZa3bUVmUXoxfNpJrbHQQpRC56-iETfkz8F98kG49OlpALJnkPjwS1nDt1VReB_cBahTV1Ci-p5xNn-ufY08JuKQglj91NJmVJz4V5crHmILUfR6QPh8qXmmLrGFkZCh8I3otmqM6zWBNv7bKmSkETBrq_y-jIv5IEANIePUO2zaxwY21cZxBSRlWJK9af9w3IxyvDV6KMIS0-TYAY76TOzEpw7hNaB1PIJgDR-1H6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AJil_SeRKlQ6CdfnMuX1AiwS0_o8-lqv1K9EyHfbDB4TMmPaIfLJTQzuEERA5GKAfj59XJyYsa99o1TBihK3e6rBgVMA7a6VpGR125TXkMDRzCcyWsDFMPlOIbNGJaJlEMA8TLaF5gI57vvvd8OnutpDgrKq43mWC6gQkX6sc8q8MgE4WqyxpOtceDDYOwzUht5xi0LRN5hnuFdPuAqVFb3QH4QCjeM3xJEwcAhxuv5R3LBQFhh1BwNw092P8hTcaYFGIKTlqXFgw1_jzq-3vUJBOU3BC1pvOxjDfRRm3rdzomznfbosMhCCiIeYoThENSTpHTI4AeYZyok-8_lBfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uyqcM_yY87uQXydSpbLKrGw_Or4ISFA0xK2yZw9mebIwTk5H4kemN5wl32Yh4OiaRfRP6b_xI_mB5jwe3IdWVP-K_LZo5PO0c_vDyrAylyFTqU8qIyL-vOQcs-d_m_vE_BNSFofqqxNZIVmHC_LahX3VkfkKdySViszenpG0xYpEhvvk9Ah5NGCGNnp5-u74r5SlChlIG-IB2YwU9pvHFloctnhvWKpUkd-abWSPsL3X6X0HzmaqFMh5V-5jR8gn-9qh97HXffzWw2nLEWrobjp_kesKPwTcynqSj1bNMIWavkIsqs7QXqDwF0pRY8gmd6l1Y5n3t5n7wobpniwylA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تیم مهسا توی آپدیت جدید، یه صفای حسابی به UI دادن
😁
اما UI کوچیکترین بخش اپ هست که عالی شده.
۱- هسته‌ی سایفون برای ایران بهینه شده و به راحتی تمام، وصل میشه(الان با همون پیام میدم)
۲- اسکنر قدرتمند اضافه شده برای اسکن آیپی cdn_fronting
۳- الان میتونید از سایفون+آیپی تمیزتون، کانفیگ بسازید. مثلا من اینو ساختم با لوکیشن آمریکا:
psiphon://?region=US&protocol=cdn_fronting&aggressive=ON&cdn_type=any&cdn_ips=
104.16.73.68
%2C104.18.180.6&cdn_sni=
pypi.org
&no_sni=false&skip_cert=true&proto_tls=true&proto_http=true&proto_quic=true&builtin=true#psiphon+2026-07-05+20%3A26%3A39
۴- یه منو کامل برای Chain کردن دوتا کانفیگ V2ray(مثلا یه کانفیگ آمریکا دارید که کار نمیکنه، یه کلودفلر دارید که کار میکنه. با کلودفلره وصل میشید به آمریکا و آمریکا VPN نهاییتون میشه)</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/4243" target="_blank">📅 20:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4242">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کتاب کامپایلرها و طراحی زبان - Introduction to Compilers and Language Design
اگر دوست دارید بدونید زیر پوست زبان‌های برنامه‌نویسی چی می‌گذره و کامپایلرها چطوری کار می‌کنن، این کتاب آنلاین یه منبع رایگان و عالی برای شروع طراحی زبان و درک کامپایلرهاست. خوندنش برای عمیق‌تر شدن تو مفاهیم پایه‌ای سیستم‌ها خیلی بهتون کمک می‌کنه:
https://dthain.github.io/books/compiler/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/4242" target="_blank">📅 20:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4241">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تعداد پنل‌های وی پی ان بر پایه‌ی کلودفلر کم کم از تعداد کاربرا بیشتر میشه
همشونم شبیه هستن تقریبا. زیاد فرقی ندارن با همدیگه</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4241" target="_blank">📅 19:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4240">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بالاخره کار مقدمات و آموزشا تمومه
کم کم توی ویدئوها میریم سمت ساختن پروژه‌های واقعی</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4240" target="_blank">📅 18:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4239">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lwYck2ot_JhApNrRZofKU8d2BTpjTe931a7gZ1C2UHa-_7wCNavu4GUN2lQfK8XfU0_wDKPkC1RAWj2BfuRLak6YzC_nTvTRsL7mWmxp6rZFpLKEpdyEHgyQt3umGOiAiRiAs0kKEDX1fxQKkY0NSt7XUA7Vw509UrXdnTY_1mtygjgZzTCojWQMHrhLHaX_M01sV5l26hOMZ0WALCZG01pz-cDm-E-i18LWiDMqFXg1-D3Ezr_HYGC7l0N3klykUFVwCGORp8NctSeJvLuBAmJgzdI-cjZwaiSE5qxdPl8xrB9NbSQEh5tSUyCalFZ5SeWSKTQyRgpWRf-Y5DqQBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز Hacker News رو چک کردم، یه سورس تو گیت‌هاب ترند شده که پرامپت‌ها و ساختار دقیقی که برای Design System با مدل Claude استفاده می‌شه رو افشا کرده. برای کسایی که می‌خوان از AI برای ساخت سریع UI کامپوننت‌های یکپارچه و سیستم‌دیزاین استفاده کنن، این ریپازیتوری عالیه. با دستور /learn بدیدش به هرمس و تمام.
گیتهاب پروژه:
https://github.com/Trystan-SA/claude-design-system-prompt
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4239" target="_blank">📅 17:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4237">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TPNr0Gv4JsQQb54V92pl_PHCmgngz4OSb1XkszMVKIZdldcNwuvOVSeyLXcSfy_SMP2ucwtxW7Yha1NkvEyoGaezqUDZU2yDcEEIHJxe-JDe9zqOpEUrpzKJ8lL9Cve4XbJrA13LjLgZbWIqwgLXqNPBnSsiGjLFHrHx_Pj9Ja6pcMQgGiDwcZrO4tVYRawGIiBqC1RPaJoxI5S1N3T6mH-rODq84Mcoql8ByJwoYV8Jurbf5ROoUvtmQFSLP_HF8M7pMo26TSe6ztZnzrit_BDV81TrV2KT5cUeBzLN3fcuEJlz4o1YAbLFsEjZ7hjhSIvTHkYgVvJJ-KD3ydwxTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PcxgxOznebVD1_xdjuSpo2976MlO7yztH0SQEdUTj-0JbO0VCQMIwrqMBnFw8saOKzJ_zrCfPTh-drpZqfjF8E5-IE8igD6bETE6c7c_V_p3zBpag6a9T7FOpAOn7odRiNkrXDVl28FLIZR_gdQsnNOS1LdcXhrPHdldcZGmaBF-Ul4v87CrRSbwGqEjjCPxJkY48ZCIjfE4WKugCwEAAPM3T6AjS-cAlpkHjCHbni3gisOcfbUoH9AW7aR8zNFy6VdBLnTyxL79SS86T98DHii_3VxGrqD9mZRHg84B8Gn9-I5HkHXZa8kjr7ckCUpxybJWfmjhjvY7TyB0sQP_MQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه سری از دوستان کامنت گذاشته بودنکه این api nara که پولیه و کردیت می‌خواد و فلان.
سایت Nara چندین تا مدل mimo داره
که همین الان یه اکانت جدید ساختم و مجدد تونستم با api key اش به mimo 2.5 وصل بشم
شما صد درصد از چیزی غیر از mimo 2.5 (mimo hermes , ...) استفاده کردید</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4237" target="_blank">📅 15:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4236">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hermes-Commands-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">7.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4236" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دستورات استفاده شده توی ویدئو، با توضیحات کامل
سایت ConEmu برای ترمینال:
https://github.com/ConEmu/ConEmu
سایت Nara برای API رایگان:
https://router.bynara.id</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4236" target="_blank">📅 04:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4235">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ipmeQgMetL4lSR4P8_dxxYRnJzbTJL54FiRvBPWhNaFSZBPMHO7dFSZfIgCFeR_ByvtkZ7HMa_ctLL5NqB-rDzLYqLwp1AnD9-CPawP6tjkl_2i74BPNoEMsnKv4h6tNULwMG2qwRO9he3EKPtk5y7ouFWweLdX50n0vCKznae24YC2jQsqyESDE_Hkdz5rkwMvawRsLOKreTFf0vn2aBwhRtun-E2rIG_gT7khKKANJqIUTtp9jgt6AbYekQ0q3wuwMecW2vPxxLeduFaCl34IvWbtFT2KfPEqo95Fen1QOCBB49U4Gd5QPdZOYBiVfCn5PBYSaK7YeflOiwJM6vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
مثل یه حرفه‌ای از Hermes استفاده کن! 47 دستور مخفی هرمس که باید یاد بگیری
⚡️
فایل خلاصه‌ی دستورات:
https://t.me/MatinSenPaii/4236
⭐️
چندتا از چیزهای باحالی که تو این ویدئو می‌بینید:
دستور
/learn
: با این دستور به هرمس یه داکیومنت یا سایت رو میدی، می‌خوندش و کامل یادش می‌گیره! دفعه بعد که سوال بپرسی از همون دیتایی که یاد گرفته بهت جواب میده. همینطور ازش یه Skill شخصی هم می‌سازه!
دستور
/goal
: یه هدف بلندمدت براش تعریف می‌کنی و اون توی کل پروسه‌ی توسعه یادش می‌مونه که باید به اون هدف پایبند باشه.
دستور
/snapshot
و
/rollback
: دقیقاً مثل سیو/لود کردن تو بازی‌ها. یه جای کار رو سیو می‌کنی، اگه هوش مصنوعی گند زد، با یه دکمه برمی‌گردی به قبل!
دستور
/yolo
: خاموش کردن ترمزهای امنیتی هرمس!
دستور
/suggestions
: اگه گیر کردی و نمی‌دونی قدم بعدی برای پروژه‌ات(یا زندگیت
😂
) چیه، اینو می‌زنی و خودش کارهای هوشمندانه‌ای که میشه انجام داد رو بهت پیشنهاد می‌ده
دستور
/moa
: ترکیب قدرت چندتا هوش مصنوعی با هم (Mixture of Agents) برای حل باگ‌های غیرممکن. با چندتا مدل موازی و یه مدل تهاجمی
دستور
/browser
و
/bg
: دور زدن محدودیت سرچ تمامی مرورگرها برای ایجنت با CDP (Chrome DevTools Protocol). این یکی فوق‌العادست
دستور
/pet
: این رو دیگه باید خودتون ببینید...
😂
بتمن رو تبدیل به ترمینال پت می‌کنیم
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. از api رایگان هم استفاده شده توی کل ویدئو. دو تا ویدئوی قبل رو دیده باشید، عالیه
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4235" target="_blank">📅 04:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4234">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دانش و پیشرفت علمی، پیش از هر چیز، به پذیرش نیاز دارد. دنیای علم آن‌قدر گسترده و پیچیده است که با ورود به آن، با انبوهی از اطلاعات و دیدگاه‌ها روبه‌رو می‌شویم؛ دیدگاه‌هایی که گاهی با باورها و عقاید ما همسو نیستند. اما اگر ظرفیت پذیرش در ما وجود نداشته باشد،…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4234" target="_blank">📅 02:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4233">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBloom.(Tin.)</strong></div>
<div class="tg-text">دانش و پیشرفت علمی، پیش از هر چیز، به پذیرش نیاز دارد. دنیای علم آن‌قدر گسترده و پیچیده است که با ورود به آن، با انبوهی از اطلاعات و دیدگاه‌ها روبه‌رو می‌شویم؛ دیدگاه‌هایی که گاهی با باورها و عقاید ما همسو نیستند.
اما اگر ظرفیت پذیرش در ما وجود نداشته باشد، توانایی درک حقیقت را نیز از دست می‌دهیم؛ به‌ویژه زمانی که حقیقت برخلاف باورهای ما باشد.
در نتیجه، از جایی که گاردهای شخصی و تعصبات وارد میدان می‌شوند، گفت‌وگوی علمی عملاً پایان می‌یابد. علم زمانی رشد می‌کند که ذهن، پیش از هر چیز، آماده شنیدن، اندیشیدن و پذیرش شواهد باشد.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4233" target="_blank">📅 00:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4232">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/509058c8eb.mp4?token=SpAjPOqY-t3IvZxXQ7kGVukmazj6Lm8kjgYgQQcMTQ1Uzg11CQNwUwS46Pa_cACMJ7torG4d7uJUsLvFW4qDFA5vt4PFs4SHHQh0FdyUatYbfI-9N8jcNfZ_EmnV4LfHQmIUZKL_9Mfh5jWqRqJAFALG2d6zHp1BS65Lsso0fTLP-KO_2zdIBm-HF09bIyv7Wp7TFBl9xXKV_i8kuBbEWD9UQ30U4uDyv3JJmDHw_bbIpCpxAwHtDAw3ShBFIodZqf6aHVlbQGx4T_DQIEAOyTCgy4MrXiY7dKOvyfKVMHyqEVAcFrwRvV-kypvkY0_mqeZq5ivMVlZR9xZ0fk9Qrw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/509058c8eb.mp4?token=SpAjPOqY-t3IvZxXQ7kGVukmazj6Lm8kjgYgQQcMTQ1Uzg11CQNwUwS46Pa_cACMJ7torG4d7uJUsLvFW4qDFA5vt4PFs4SHHQh0FdyUatYbfI-9N8jcNfZ_EmnV4LfHQmIUZKL_9Mfh5jWqRqJAFALG2d6zHp1BS65Lsso0fTLP-KO_2zdIBm-HF09bIyv7Wp7TFBl9xXKV_i8kuBbEWD9UQ30U4uDyv3JJmDHw_bbIpCpxAwHtDAw3ShBFIodZqf6aHVlbQGx4T_DQIEAOyTCgy4MrXiY7dKOvyfKVMHyqEVAcFrwRvV-kypvkY0_mqeZq5ivMVlZR9xZ0fk9Qrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید براتون عجیب باشه ولی من خوشم میاد وسط ویدئو به ارور بخورم و بهتون نشون بدم که ارور ترس نداره و میشه خیلی راحت، راه جایگزین پیدا کرد
👍</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4232" target="_blank">📅 23:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4231">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iWiFnuXD6MYomIvhhIac6tZ8zgzYZWfjtZrDFkD2-bZAroQrc2qDjj1t-MsJ8rP6mqkJf43TKkDi9CjNdPOnUhyqujdGg90XRwfO8PDc-iWYf7QgEIC2Stuyfh2_wt3L0c2oun54hPTd0xiv2GMDTPncRwk_gYUeOcltytLa5npzoeWZ4kfARtA1OL3MBFVYqmAgr2aO0AmLCdA-P38kTQ0NCXzXOYK1FghOtYJTaxUP2ogRejbTsXdiZ00ShrcD5v-TZ7-b82zZYvIhNZ9gNZdK9tfiUSJWRQl90_004q1XdB-XvXPSZBHGHaPkacHRPq7Sh49ML7DRomp9pBv-vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر، قابلیت Deploy کردن پروژه‌ی جدید رو برای اکانت‌هایی که با سرویس ایمیل‌هایی مثل Atomic mail ساخته شدن، غیرفعال کرده.  با جیمیل اکانت بسازید موقتا. شاید پرووایدر دیگه‌ای تونستم پیدا کنم که راحت بشه ایمیل ساخت که کلودفلر گیر نده</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4231" target="_blank">📅 23:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4230">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/STzwzGsCfiKgX8wdJxJdOMK3CxWHI_xvuhyB2a-YISTsoafJ-pVBQNRYJiV9laaCW8hnmAUUeJC7tUGu4BqGfWx_Qmzet0EE4TSykfpn7cuFQLUn_lhEz77BigV9N_tCcTGdJ4Wa2q_z0gco5o-sgXruXQ4oLlUdAuirgew8duzgL_n3oA81sJoRsiOaJCNC1aftPG2Sygpukz7Eq2rqRS2NAIZX4VjnqFqN81C1yHU8xAalx1RKeNRURwmXviaBSVhbViQKOjq_Tr6M-p7iyOeOUcL1neUPjP8qTB6c8YuUyKTFcyndTZZjXe00sV-X6SBboSjUgSPjQmS4CiPOTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر، قابلیت Deploy کردن پروژه‌ی جدید رو برای اکانت‌هایی که با سرویس ایمیل‌هایی مثل Atomic mail ساخته شدن، غیرفعال کرده.
با جیمیل اکانت بسازید موقتا. شاید پرووایدر دیگه‌ای تونستم پیدا کنم که راحت بشه ایمیل ساخت که کلودفلر گیر نده</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4230" target="_blank">📅 22:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4229">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">روش فارسی نوشتن درست و حسابی بدون به هم ریختگی هم توی ترمینال یاد میدم توی ویدئو. که یکی از دوستان عزیز توییتری دیشب بهم یاد دادن</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4229" target="_blank">📅 21:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4228">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">توی این ویدئو که دارم ادیتش میکنم، کلا با cli پیش رفتیم و از اپ دسکتاپ استفاده نکردم برای هرمس. علتش هم اینه که پروایدر شخصی اضافه کردن روش هنوز داستان داره و محیطش پر از باگه همچنان. با اینکه آپدیت هم کردم الان هنوز همونه</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4228" target="_blank">📅 21:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4227">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🛡
آموزش کامل نصب و راه‌اندازی سرویس MTProto با ابزار MTProxy  فیلترشکن قوی و پرسرعت برای تلگرام    https://www.youtube.com/watch?v=pyvB6VSPhwg   @WhiteDNS</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4227" target="_blank">📅 20:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4226">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🛡
آموزش کامل نصب و راه‌اندازی سرویس MTProto با ابزار MTProxy
فیلترشکن قوی و پرسرعت برای تلگرام
https://www.youtube.com/watch?v=pyvB6VSPhwg
@WhiteDNS</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/4226" target="_blank">📅 20:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4220">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Y53s_9P3ugZn-REJhR3a3aZV0ICjo52ql72q-ucatJTQwSMx4vTfX34xCj1fVipO-kTK9JKnqMksTbePW8ujo83-8KeNM_4cdcKE2oznfj0SfaDE1a00X3zN4355fDAk7agkqiW5aN7LVdJpeDM3YzXjwAyZ8axqUFlrwHWLHexX3xE1R9UNaJzWSEbt5MBoezP5rH9Aq5eVfquTONAV613I78rx7Gskwxq0NFKxuv2L-vjElyAmUuHrdGoizdL4HANd5t1D4lLdXWjuc4kvUtSAfibUHhSbR-Pjw1MhxwrpZW4daBPh1wyHcaB5jtX03IwEVCmxykgBw_reTpgjRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ne6TVcpDHHL51L_mewbFZw19GZ46VXSpN1dBVOir-Z11U5nudrUAwZusddBYHVkQbwg039L9tsk_5kn_t3JqU1UMNGn2sziyzmWSNQ6ua3Oa62KQGY7aN6WbrtMYKlatLA-DtRLMpV3A5Haq9h66z5g_50ihM4JytybGMI4NvNtd8znu7PZxgsCH142HvWeABObUGQ0dOPz_XKxWv1O92wbnMdJYF0rI12HfuK2-CEaAc5PhSN85DYYEWGaKaoFw_sS-9ds2HMTPKNkg-lkpdlPBAXneVwkPibS0QWRnIhOv_7Q0ie17Daj9K-2c30KRU6SclTbnJaNS4HWDhwpuOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dlEABkdHLugnc2LJRHa2EBIeGrmQaJQlGYNr8xTHXXRry4XA-85gtYRGeZDz-1JV6awDCbVr8Dh_rEVFpu_PCBZ2HFLv-9HCKOP4FEyqFhBVtMiDoh0pBae-YzOKfYS68xN6EvumQ6aOH8LAQHHWJAMBQRAiNi5LI3J-oiRDKXlJdy3P2XMJn0KZnFFxqxQnZbGeHPJ0a867xJV3IPTPWoTTihjXMhMexxJgDs5pOXcjUtWYCBtQDQkUKqwrergmgoLilUkJtRrkGcE-yfTE3ILkte2ZNoIA7FCLFJ6YzZxSBFiCxdBclZilxiKg2t7lsv6djL846GZ_fRVTFPeNTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lIJtw5umjVOfX7rWVS95AcHv0c0Q-W9psLeyk5VZ7npdNXLRSy6pU-_4gy2qB_dKJBPgPcwi80UaAWsvd6nOoZpRsNFW4pMBftr3m6RS0stOG_B7meTbf0nhw5eLYHHCRjpmCVZSRHq36-gr0_yurD_dTSJdik_WX8WLhJ_rXLb76q6pJ5Ynx4L9WmWMYC2vYwJGZNun-gVZ-zpUlBi9H9tJOCZ7HRmW7XF09OKSqKOBPOiTyXpSaOV808Y6GpaKtxnqur_G8yEUS2e-pIPtRVUHkLeIebCPjlX_jv_l4liifuENkdDgDQQmXUmbPMW5FMwKCkQTDEQk_U1IXYFVJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GQIK3A-tZFmZ_OgUYCyZJD8CvmfwZ-wPAbL_Kn2fCIjxyQFrpe2gFFkbkGWqhtRXq3shLK8N9omdg5XLWbF-QRaUHH_Fq4EYxwITaC3GAR8J6y7i9vDzf8lMgaGxUA05L1448og-kF0LnQiOfwkfxqcuhy-2xQtvt2_cRLwkO-74_eyHhHwo3O25BCxfgz1XVvETYzb3y2VQS9ahTt8L41Hzg_qK-a8peF5adLGa3c3OhMOEGWzfq6y7Hhyl_dzlXGKu2O5mFnVdENOqrZLQ-oMDWB_vHUDz0CMdmcy3Kt-J82Usa5utPbfmsRMejIGn3EkSPZZIwMv5-0nTYXCF1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/awkHW8PLRa-sSP-EUAi8QotmQvP3-I7VIA5J_WiFTtRObHVCxKDhuSc5vWBkPU0NqB2fomUdkTNPzJp8txJw6Kych86qvdD-mDdboBCyP1ilsDmOyuZk9MIfIZekNFa3Kxms1oT19yX1qhq9qmIWcfhHU4JkL-g9AAJh9bbOUIOSYPNRvBgC2S0c9ieyJt96RyQFDbzt8rNkzs4ePEFqXR_Nvp3rQy2goPp8TOZtPxEjW9uLuOxc063jNTa2xLnAcpgUzJD0MwYs3RiNy6z5YnL7t3KHaFEx032DPfDqKHTi9A9Z5cnDIamSzFUVHQ-rQomvNbW1GB7zMxTR4_flSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راجب این هایپی که در مورد «ادیت ویدئوی بلند با هوش مصنوعی» راه افتاده چندتا نکته می‌گم و دانشم رو از ۵-۶ تا ویدئویی که تا الان دیدم باهاتون به اشتراک می‌ذارم:  1- نه. اگر دنبال جواب مستقیم و سر راست هستید، هنوز نه. هنوز توانایی این رو نداره که با هزینه‌ی کم،…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4220" target="_blank">📅 20:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4219">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/djJ06NjEER0iZqi3v3vNRsANDMzOWWeZ46hwIWqWrM3Bukb5RGf9SAaGxYPdbQrgj6V_bULhkX1RN4gCnh4tzeRSza5hkf0OdR2R2pEhEBOQFaOwY796qjWdL2ny0i6EF3-FHl33GctvD17TJ-QuHeyKfG9jhZZIY_5BNPNDlpsJa1PWtpG_n4ayaV2Ug0BPYR1ad_aN6RppwVMOITIqm7tIYFPtCNlnCKaHUtvaROIR7T0SUzo0s-qw-nbUW0Y54IpnxTE0XnNE_2sGtXjlB2cFrGRjJJCC87gJPFICh0jugz4LRtOYaXKbBeoGJ1-S8ShKWl_EU4iVqEj1UNr1TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راجب این هایپی که در مورد «ادیت ویدئوی بلند با هوش مصنوعی» راه افتاده چندتا نکته می‌گم و دانشم رو از ۵-۶ تا ویدئویی که تا الان دیدم باهاتون به اشتراک می‌ذارم:
1- نه. اگر دنبال جواب مستقیم و سر راست هستید، هنوز نه. هنوز توانایی این رو نداره که با هزینه‌ی کم، بدون اعصاب‌خوردی و بدون زمان زیاد اون کاری که ما می‌خوایم رو انجام بده.
2- چیزی که من از ویدئوهای این دوستان عزیزمون فهمیدم توی یوتوب، اینه که میان با مدل Whisper و یه انجین شروع می‌کنن به کات زدن(که همون هم پر از اشکاله و نیاز به ادیت فراوان داره) و بعدش شروع می‌کنه با یه سری mcp و یا پلاگین کلاد کد که اونها هم اکثرا نیاز به api key پولی یا اشتراک دارن(کما اینکه خود کلاد کد هم نیاز به اشتراک داره) یا یه سری ها هم با Hyperframe، واستون موشن گرافیک می‌ذارن.
3- حتی همین موشن گرافیک‌ها و... هم باید قشنگ و دقیق بهش پرامپت بدید. این نیست که خودش متوجه بشه و این کار رو بکنه. همینطور توی این ویدئویی که تام‌نیلش رو گذاشتم، طرف برمیداره کلاد کد رو اگر درست یادم باشه با Opus 4.8 می‌ذاره روی Extera High effort که خب توکن بسیار زیادی هم می‌بره و فقط ۴۸ ثانیه‌ی اول ویدئو رو باهاش ادیت می‌زنه(بقیه‌اش رو داده ادیتورش
😂
خب مرد حسابی، واقعیت رو بگو دیگه. که مابقی ویدئو رو دادی ادیتور خودت ادیت بزنه)
4- هایپ اطراف برنامه‌نویسی هم زیاد بود، و تا حدودی تبدیل به واقعیت شد و الان ai سرعت برنامه‌نویسی رو بیشتر کرده. پس شاید بتونیم انتظار داشته باشیم توی آینده‌ی نزدیک، با هزینه‌ی کم و یه اشتراک معقول، زحمت ادیت رو از روی دوش ادیتورها برداره. ولی جایگزینی رو بعید می‌دونم</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4219" target="_blank">📅 19:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4218">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">کاربردش می‌تونه اینا باشه:
۱- وقتی دوست دارید هر چیزی رو بگید و در لحظه کامپیوترتون تایپ کنه
۲- یه ایجنت لایو با Hermes بسازید
۳- و کلا کاربرد عمومی. مخصوصا برای کسایی که disability حرکتی دارن و مثل خودم توان تایپ کردن زیاد رو ندارن</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4218" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4217">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">چند روزه می‌بینم همه دارن در مورد whisper حرف میزنن. خواستم بگم یه ساله برای تبدیل گفتار به متن از Handy استفاده می‌کنم و واقعاً بی‌رقیبه. کاملاً آفلاین با پشتیبانی دقیق از فارسی. حرف زدن با کامپیوترو خیلی ساده می‌کنه. github.com/cjpais/handy‎  فقط کافیه شورتکات…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4217" target="_blank">📅 18:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4216">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uFK9tpek2_mVBNPXNEpXDiJ5bWrlFtfw49J7YvgFJCANq8MY7tcyEJOYDnJyOIGKWCBgbjILLC5EAAn9i_wHEEzydYptnw7OqJC15exVbXdzgdhYjb5uJ0yd8M5Q-1a-RHqKChiRN2SLP25tob7wHlO13RZjzwMV_eN5bg3CIDQL9YiRt49WQi15bHNLyIux9q1NxWllWDFdAkehGARF4HP4Ah4lWVWCTBmAmZyhNpQHa3wo2t8ApG4sQ8jyVvzZGdtml-PnS9ChNo3Lp37mja_U9eKy9lgG7IM5joXcAcsFdJx8JPHXcfwI5RwOAhZ3q9DGDLpDf2Kl7evOmcUz1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند روزه می‌بینم همه دارن در مورد whisper حرف میزنن. خواستم بگم یه ساله برای تبدیل گفتار به متن از Handy استفاده می‌کنم و واقعاً بی‌رقیبه.
کاملاً آفلاین با پشتیبانی دقیق از فارسی. حرف زدن با کامپیوترو خیلی ساده می‌کنه.
github.com/cjpais/handy
‎
فقط کافیه شورتکات رو نگه‌ دارید، صحبت کنید و رها کنید تا براتون تایپ کنه.
اگر دنبال یه ابزار STT بی‌دردسر و رایگان برای لینوکس، مک یا ویندوز هستید، حتماً تستش کنید.
✍️
apt_hq</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4216" target="_blank">📅 18:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4215">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dZZaLSP8MLXgGT8QA86WZPA7hdp8ntSZPOL24TPvPNxr0Pv-lL66nJW9mha-dj01VKdDYYxRBG0gmZqxDZAOEWYVd0MgY80BUwdJNY7pm7kGnmrZJi62jMLR4g7aFwpRij4HIOYOaqLl7Ubie4MYnpL2gCPE-trU_PAoEdHmQi7vW0HYtTVLSlMoTz2Bm6FekWg830FhPW1Sgs7js5YFss0aSHQRD3ol6dmQ0_fgWWM9cN0q18fB4iXUdOKxf8szjXiohTyELfqyMptv_QQO7U-BUcEppJ44hcr7W1OHJB6d3RFOrV2-j9grXiTz3xPXyxxQTTkqH4nrqF9thlDq2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا به دادم برسه
3 ساعت و نیم شد ضبطش
😭
😭
از بس دستورات هرمس زیاد بود یا طول میکشید(کل ویدئو رو با api رایگان رفتم بدون سرور و... و واقعا هم خوب بود) و قلق داشت انقد شد
اما ادیتش کنم ۲۰-۳۰ دقیقه بیشتر نمیشه</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4215" target="_blank">📅 17:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4214">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">برای مثال کیوریتور (Curator) که توی ویدئو توضیحش میدم، یه جورایی کتابدار هرمسه که تو پس‌زمینه سیستم بی‌سروصدا کار می‌کنه.
و Skill هایی که خیلی وقته استفاده نکردید رو پیدا می‌کنه و آرشیو می‌کنه تا سیستم سنگین نشه.
ویدئو پره از اینجور دستورات و همه رو هم تک به تک انجام میدم و تست میکنم و صرفا روخوانی نیست</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4214" target="_blank">📅 16:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4213">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">هرمس قشنگ یه کارمند تمام وقته. ویدئویی که تا آخر شب می‌ذارم رو حتما ببینید، تا بتونید از تمام پتانسیلش استفاده کنید</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4213" target="_blank">📅 16:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4212">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">به زودی یه ویدئو داریم برای تمام دستورات ریز و درشت Hermes</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4212" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4211">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">به زودی یه ویدئو داریم برای تمام دستورات ریز و درشت Hermes</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4211" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4210">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mSXrU6XRWc713SP4vBFVkTPuk5-tZMruhPKvFLy0bfUl1MAZHqyxhEZJbs-ZWVF7X6XwtA0VsjZR6EoEMXh1WAfL0iBFjewL8V5VbtHlOGmtOIWszW5nijqk6volfE-bQZrjNxU1UIzxhhNSOOwf8hedfyRPROKtsX_ukDN-qDqHfGl-aolFdXeDC_IZpsBzJIG-qu7xpBagU0bqbi_t5d5mrHtJbYqkQIHSbSazuEj5yhxgTSFc27U28nefu_RZVhBN1Zw9hYYRaxnFqgjgooScxFYX7xz88pL815KwuZkuqNDJFBOWdJj3gQawtOW0FLW3A30qG6O3Vl9UsG6u5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این داستان، ایرانی بودن</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/4210" target="_blank">📅 01:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4207">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YxxcaWQX-Bd_AvuqD9nbpBZIPog-8Z2LnaIrwvv_0YNq0b8tFs0UNeqUkrKXKWMLcFFidDd-KpfY6cum6ySz7tdcwPNBf9vtTfpCJj7BSMAKBiBMcdbYp--O9Z2O6w3mD2K9E3ALXveGD6NlpwKL4-VTcmOX_FH_IBA_TgDMJgBdPOlKQTcY0iql3FxeNwdClbJxZE_WIQNCpGyAXP_trAvqo6OZHBPeLxHep2_85JDkXbMTI9P9DzYHVXSP4_6BBlMQ-9cIhAwEVKd6lWui1Tj5zoJLouOn6JMLP16gDo34DOmL4zn0djGgL9Yjre1sN2GgR2ioFCU3Jd3v1QTpZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pCRqwdjKkVkhmDmPFwPCcDQm4jHlwrKFkG6SfF0cOKLn9wQ399TFzRA1VJz7ahiJd_Wdv5O2Xf8hCL9xz4KBeOQj5nwSDZcrrITC2D7WF2CU4mzJSwGLxLlqmTUCfP8PZEru-GVHnMARnKpdIc7WgMUoLAjwx5yAg-4m20sY8d4ddtf4hXZ1Zo3_YHe9Ea8bD2AF5NHq_C2mbLaNN9ihnc0fjFmFrTUglWCrPruszAW_V_ac3W53AQ4Vz_mA58Fv_PjoH43SkuFwiKi1zMA0gkWJNQ6CkGxlyJWRWvuB1qEvAvkzwKs8v40ZBMaNUqsqnj0BrKNyInL_daccGyJX_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vuUoUl7PB6Z5cp0_Jd3UYuxosM2A6rRTTeHx3u6teTBA4rWsXypO3ATK-k2sMfURExBBDDYF0tKH0n_dXZpKVj1ZXjuNbgrqR6vl9GI-jE350Wfdm4WsYHgxe85hMouUU-RC2VnKulWG8d3fIAfcdHpZ5quvXpwSggV5vOuRPcHMuukjZ5yt8nnhSjrLZ3-HPvTF3PWMLHuzPcR-CXYj2gY_0_6VPhVJ9uaHjQ3-l0if4YPx57F-236dN4Dat4tsBhZHwvEXxYfx0eXO9IUdW7lDH48lQLdYWNZoC11aEK9rNYcq0etP4nGgI4CYcMnNg85NnPdexmd8LtvbAjOqYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توی Hermes اگر از دستور Compress استفاده کنید، به صورت دستی زمینه گفتگو رو فشرده می‌کنه و چیزهای به درد نخور رو حذف می‌کنه. هرچند خودش وقتی توی هر Session به 50 درصد ظرفیت برسه این کار رو انجام میده، ولی تأثیرش روی توکن مصرفی خیلی زیاده! همونطور که توی عکس دوم می‌بینید
💪
/compress
—> فشرده‌سازی معمولی کل تاریخچه.
/compress here
[N] —> فقط تا قبل از N پیام اخیر رو فشرده می‌کنه (N پیش‌فرض ۲). پیام‌های اخیر کاملاً دست‌نخورده می‌مونن (وقتی می‌خواید مرز فشرده‌سازی رو خودتون کنترل کنید).
/compress [موضوع خاص]
—> مثلاً /compress database schema — خلاصه‌کننده اولویت رو می‌ده به موضوع خاص (مثل schema دیتابیس) و بقیه چیزها رو یه خورده شدیدتر خلاصه می‌کنه. و محوریت حافظه‌ی Session حول همون موضوعی که گفتید می‌چرخه.
حالا شاید سؤال پیش بیاد، که متین آیا این قضیه، کاری به اون حافظه‌ی بلند مدت و حلقه‌ی یادگیری خود هرمس نداره؟
✉️
باید بگم که اتفاقا چرا. هرمس قبل از فشرده‌سازی، memory flush انجام می‌ده تا اطلاعات مهم از دست نره و توی حافظه‌ی بلند مدتش ذخیره می‌کنه. و این شکلیه که چیزی از قلم نمیفته!</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4207" target="_blank">📅 01:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4206">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=j9yJFILb1ugi11O28ZQ0Iei62ocZmB7kwfd8jCfvyHNnUuIR0qeyshwIv2w2jF5ho6cJagX_zlrqmXwfjy1LLKgsB-zYFkBqgZCCMAsyjgNEtxH05EaJtCJTwzKx9iqyN2--pjvJv3PDYYo-Ba1NApDyMZxPN4xXx8sQg8Mqyi9QeOnwYo_Ppzxyf4y2wbE1e4yQ301YSSEbknBPpNyU6R_aDchQ7C5WneE7wcXTz1-rvlf42p12RzTbvjTgUrx7bybIlk39grh2Da1pLCjs1PfDkRbTuLP4iR1eYPnHSYS1_NAu2DodXsmnbG2xSOjzA_JhfOVzjelHfOeAHuPOGIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=j9yJFILb1ugi11O28ZQ0Iei62ocZmB7kwfd8jCfvyHNnUuIR0qeyshwIv2w2jF5ho6cJagX_zlrqmXwfjy1LLKgsB-zYFkBqgZCCMAsyjgNEtxH05EaJtCJTwzKx9iqyN2--pjvJv3PDYYo-Ba1NApDyMZxPN4xXx8sQg8Mqyi9QeOnwYo_Ppzxyf4y2wbE1e4yQ301YSSEbknBPpNyU6R_aDchQ7C5WneE7wcXTz1-rvlf42p12RzTbvjTgUrx7bybIlk39grh2Da1pLCjs1PfDkRbTuLP4iR1eYPnHSYS1_NAu2DodXsmnbG2xSOjzA_JhfOVzjelHfOeAHuPOGIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی نهایت آدرس ایمیل با یک دامنه روی کلودفلر:
https://youtu.be/Z069VNFAgAc</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4206" target="_blank">📅 19:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4205">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خب دوستان GLM 5.2 اومد روی Nvidia وقت استفاده‌ست
👋</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4205" target="_blank">📅 19:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4204">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bmr866Xcz9n-F7-JUlpx8AUnr0ZmGMVhO3JCvpExNZs_STY-v2kpoO1fTWRc-21RyzY_lQF_btgAbsgagQysNa8BjrSc2Lb4uZko8_oEupzIuiC1l3IPwHWHJ9xHsUqSqfx6Uhe92637N1hKm9iJsYMkN6Q98weHR9nVo0zFwrhydeArfXuOlg2fm_Omq6os5EgLJCbL-GQNHjFHAAr0b2Cq5yNrGNcrRTYYnFy3rOQbi8ynJdgs2-WsdINwVs21yK0zXVAbe3-DoLPooE0hV0iy6mSu8gbeupsSQmQPrxhZ9cZSP62l5UwsXFproEoRiOhnFTn5-qTLOB0IYi12ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دوستان GLM 5.2 اومد روی Nvidia
وقت استفاده‌ست
👋</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4204" target="_blank">📅 17:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4202">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gDqTegAP7V5iGswlhtTFDnpeM_EqF8vtypmoRAVcE7-1SlN9O-yevwO4YpHc0a9r4Dfdf-vAIZa2mVSo3HSkapeF6yff3RSgJQv2IY2P-8kLDCyJisjQJlrNd26Gid9lkqE5EuxMUQeX8WiyL6zU21wHy6-IrHzLd5CTKc69vgoyHGPltEaZ-OBLhrjTOfPH5s8AaHvsTpELsEuz-iDNFguQFJcFN9bvgQ_WRT3i4MP8Y2V8yXOMtKF4Un1uwh19WqdeW_Fwxg3a3x6EtTojBJ3DRz8hEO5deW-m58bhggQJ9yOkHIQeneYaxc_sO26XzxRNchVEnUKefeWi8TzLlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VY9kBAdolvTAnHEjLUibztyCjBE7ajxzmpCEXdbT9mQd89gEVqvnjwmyBEduBjfsaJJ3G-SdaaNtqzWy_X944mZuaFpvd3tR65ru6hTfqTO-9lsgsSGCxHD864AlfbvYN7TzOqiGVGjnaozgpibfy7tr7KJlgO6jDbu2ClLpENO8Qgb_9RhE08gmzdV7f0zzvlr83tYpUmCyHjigXW-5bzcuqPuOixHp3hn7Fgv66uAgp3WGI-tujtU7lTkDCdYAUqDY2dY9uZ_S0o_HuiRum2Kq5ZtDvxAGTihnFkJVpGplCfNTg5rWR3RGewvG5TO-DawOYjtIMutYi6YaqHPacA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">چیز بامزه‌ای نوشت اما پر باگ. دیشب GLM 5.2 برام دومی رو نوشته بود که کار می‌کرد همینو الان با sonnet-5 هم تست میکنم</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4202" target="_blank">📅 17:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4200">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sOEpdUFHGnoMY54tNpVPwESsBHOjLRKwegB61VnvQKMUcvKK73sGpWRJe-OeGtElVcmc-L1yRQEPNk7C-UdJAuFnoRY7sK_nP9gQufxOPOqiQLlLytps7JmTOiFa_UDGHw_C_4W3ymvjJ_JKtAK_ILi90gHJnBqf5pKIEq-fndNonBun2d5le_9bIDdwmGF8914aOrn_AjdGYLjgSK2qjjzwYpApQZ8UncT3f7z2Y5OzNrchCWAWhq9g0IZ_ZZ5ZbpPQIc7WexcomzKPEuArxjuLQFPQ66NN0rte0L5MNitX2_HmJd0JMVJ64VbO6LeyL8c2DSnQocaHBQYzqOlnbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G8eAWHLmWB7bAAN9xv41_A0PVSN7-w-9pxU24a98O3t-m0FOpWhG-e_O1J2PY1FjV_SNMmwDW_9ifbTGjz2daAGUnZS7LK-fk34vVwdjhRq0uKy7G42WnfSPMWvs8eFr2F8wW9awk2OUK98loSzNEUDS4YayaXGy0d0Q5CqsTeam0r6SbNwkGrf7xLAkmgoSO3sUA_2-iab5Unw2IyaqwBuM6_LsHNCBkxlf7hdKM7g2L5255LI4ItTNzTRpj380sYvAm6QW1KhOqdSzx1ju9GcclYyLsfGyaz_i3NBt10Ezx8ND78hCxEoBC68q3OA1PTlnNnRq1X8_C40QLY32Hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بریم ببینم با یه تسک گنگ و غلط غلوط چیکار میکنه</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4200" target="_blank">📅 16:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4199">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LlU1Rv2SSC9QBt81y2H4gp3MDI9ylW_XXiZr-zTilNWnmLPOpyaq0YlWngwZGO0iE14fVqrFMy0Soe3Ar_01jMk98oHv3S3-0qjy2YcxeSo2IL1Zg1sKgw-Tbcn2QD4zx7l8mBSt6ZMnPgBfByAhnO8MtB76CN-qo-UJvKq4JFYZSJ6S3KS-UfOpKp6fWouQQBi4yU9F0oJmuJPmProApJYCmjTy30otQqm7NV5hUhf2LnrIdhukMQ0TqthOGt6Z2Ijx4yOzeZGzb7GiL-j2Knxiht_TFsfq31QUJXchyFRAbLTuZjb_VNiBfRGguZuVeEUztAHxnZbNxrgsRp_gyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثلا هیچ فعالیت روزمره ی معمولی غیر تخصصی و تاحدی تخصصی ای نیست که با chat.qwen.ai نتونی انجامش بدی و نیاز به خرید اشتراک chatgpt یا claude یا gemini داشته باشی. البته دارم تواضع به خرج میدم و میگم که qwen صرفا از پس کارای معمولی برمیاد! برای سرویسی که میتونه…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4199" target="_blank">📅 16:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4198">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fUBEGR4dggzzxAEZJU5J4_q9L1mdpDjv7LuwKw-KJUGEW9BjBeoyg3ly8FDFG0-JGHZUv9-3cM2vKgILYIWVlHn-tGHb40fBcgHMIJsX2jIHaFEMW3LE3NPcBZOmjadyAlWaoki6uwcvMp4xBJqUu9Sy1kMYhTSAQ0s3825OkFrHrJ-dGQLTBj3DnddJGGLRzslmy-aPhNWWcjUIjKQW-a2g3KJrRLrnbhC5vE7XGOmLqiHryDprWr4qszRKFIllPvRPpt_vpJJjMIbi4RmJYL0opBTZSGnZlbGRHmAaXCPSO7wjGnzvh74LUWrmKdZgufpHViNPh6uDCkyl3e6CGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثلا هیچ فعالیت روزمره ی معمولی غیر تخصصی و تاحدی تخصصی ای نیست که با
chat.qwen.ai
نتونی انجامش بدی و نیاز به خرید اشتراک chatgpt یا claude یا gemini داشته باشی. البته دارم تواضع به خرج میدم و میگم که qwen صرفا از پس کارای معمولی برمیاد! برای سرویسی که میتونه پروژه بسازه، مموری زیاد داره، عکس میسازه، فیلم میسازه، ریزنینگ قوی داره و برای هر سوالت یه لشکر ایجنت بسیج میکنه استفاده از واژه غیرتخصصی تحقیرآمیزه.
✍️
بوکانت</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4198" target="_blank">📅 16:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4197">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">توی مدلهای چینی طبق تجربه‌ای که روی هرمس داشتم، MiniMax m3 خیلی بهتر از Kimi 2.6 کار کرد واسم روی api انویدیا</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4197" target="_blank">📅 16:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4196">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">به قول یکی از بچه‌ها هر روز جوری با Claude کار می‌کنم که انگار روز آخرمه</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4196" target="_blank">📅 14:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4195">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex با هر ایمیل هم می‌تونید یه اکانت بسازید و... بله خلاصه
🥰
اینم لینک نصبش: https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/4195" target="_blank">📅 13:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4194">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VssHFwNebfT0SPByL2aasqWhwPo-mwY64xU9FW7sS-yv4at7HsJZNe5y9-5c0KK6ftNj3geG83FPVRJ75PDmCJDNkJwcipmcOSomNeesUkd1Echa-RECrvdBbbzXJAjE5Z3F-f8LaK7YqO7RBwkYXx77zoLCQp8zamxSHdQkUBE4MKOcQYfgS4-A3uunSabTRO32BgAqrThDuQsravn8GfkzAoV6DXB_fyfT6RyszYrTQPh05yKP5NuW5ime3Ea6MIiPdDErPKcmaX8jSkjfNi7cJKBFB-R05Om0zYiOBlKf_fj21IoFXlMukcNu6x8OYXJapuQuxNjZ7T1yUikgtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex با هر ایمیل هم می‌تونید یه اکانت بسازید و... بله خلاصه
🥰
اینم لینک نصبش: https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4194" target="_blank">📅 00:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4193">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ia7MySwNBZqGIPElqZ4E-BkY95P1e9-CfBc7y2raOkCBl-LaNv5bBWw9ae-qOn_J9zPFycGqJ4miSOBFszCa_CVjCQsWdmSQs6sLeJzss52eL2cJbk1TN8frz-ZpsGXFrBhW-Nzs3cFmzb-NUvwt_RBHbjY3SZf5oltsXhigZ_R6MaL_dAWKRyodfBW_YfXgmqVmdQ6mGglorWR1F2VkVRVqxReT0JT1SUve5q5hpi5JoMEiScEoOhFzdjczn9ZHGkExANHwKPf-i9EYJrq925RvJbSMqel3f7L8jY4PaP6sSoIHA6aIOjxSsa2V5j59Ey-8qwMt0jBDA930TMyb8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex
با هر ایمیل هم می‌تونید یه اکانت بسازید و...
بله خلاصه
🥰
اینم لینک نصبش:
https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4193" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4192">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-text">‏DoH HTTP Proxy یک ابزار سبک و کاربردی برای ویندوز است که با ایجاد یک پروکسی محلی، درخواست‌های اینترنتی را از طریق DNS over HTTPS مدیریت می‌کند. این برنامه زمانی مفید است که DNS شبکه دچار اختلال، جعل، مسدودسازی یا ناپایداری شده باشد و تلاش می‌کند با استفاده…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4192" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4191">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3A27Sx52a6cA_nixf-CqoWM5UrYD_PTytvF9SG3KigXLPT3i9Kd3TeBci1Zh_DPJZh625poM2qeTFMt21KvhNf68hOiEVBXS8Q4PWJXdpdPyv2mbBjb19TvGOdw8gqDrA5XjkkinobHr6o_ZulXYc9uztRnkgOydAQnN70KlCadWnIf9cLpl9Hgt6AMGyH4qohx36q_3pfuVTFleytD07LlsHvkj0Jl6Iojgs4M5tLas_DLGq_lv9v6uemqjhkHz4a4dw1EALCZvcrcPXPTBwjbsGBZvwXaBinIrMxV0YufksN7T2cD4VQu-yjgqAKVYoFOLorcZeQbLdOO0xtvxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
DoH
HTTP Proxy یک ابزار سبک و کاربردی برای ویندوز است که با ایجاد یک پروکسی محلی، درخواست‌های اینترنتی را از طریق DNS over HTTPS مدیریت می‌کند. این برنامه زمانی مفید است که DNS شبکه دچار اختلال، جعل، مسدودسازی یا ناپایداری شده باشد و تلاش می‌کند با استفاده از endpointهای DoH، کش نتایج قبلی، fallback و حالت اضطراری، اتصال کاربر را پایدارتر و قابل‌اعتمادتر نگه دارد.
لینک دانلود برنامه:
https://github.com/SAMPA-ASA/DoH-HTTP-Proxy/releases/latest
لینک پروژه
👇
https://github.com/SAMPA-ASA/DoH-HTTP-Proxy</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4191" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4190">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EQOL3Cdk_MSd4W09WFJOW-nEuBt78QlpscB9KLckhKNFXbJhDXgjk-IF1oYSIB_8eOXQVfYBugrUV8gHAfyfOSyUqPfUrVDDD5es2YNKbkNcLSj2PdkZ_K4U0VNlbXvj4knTwG4I2IhARuiSraY_E0EcrW5cvt3lDOtQ42NkMI-djV0yRU82emhfJ2eUkmW4yDXtIkDxYu2cUhRH8ileJUsLA6EWG6SBcVChYPivXzeJAGcyGXfmWdo1_upLPtYdBNSwp-rdaxftmDXz7DJwnVTEa4R7KBH7Y-yyf6JOqUdP8LO16DSfn8IvZ-i8bGpYb6xcrJXGqFfzE6rvt5ZLOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از تلگرام برای ارتباط با ایجنت هرمس Hermes استفاده می‌کنید بهش بگید که تاپیک فعال کنه یا فرمان /topic بزنید. بعدش بهتون میگه که برو توی تنظیمات BotFather و گزینهThreaded Mode روشن کن بعد از اون برای هر موضوع میتونی یه تاپیک جدا باز کنی و ایجنت موضوعهای مختلف باهم قاطی نمیکنه
✍️
Hessamsh</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4190" target="_blank">📅 23:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4189">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">برای هرمس، 1 هسته سی پی یو و 1 گیگ رم به عنوان Minimum کافیه. اما پیشنهاد میکنم 2 هسته - 2 گیگ رم باشه</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4189" target="_blank">📅 22:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4188">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sm8eDskA6P34waPVForNgyApui8StLY9iP5SwwEAiWW2jJAkjQebjwafQho8m_p8CtcKRqq_voRrqgPOJEoVFnv8rTlbAjv1-wMxzYVGlVoN9sJth7PvrpTu8z9qwRu2EQ1ICh4TVXHAr2Ew3bCjjeLwJTJbuh5e9OzEIukMJPqAzia33QI5sKw8ce-LXwNdHmEp84seFbyx3YfTrUXpp7hfAis6n1xnbxJjCV8yd-AOijRwQDP6ckZli6gwPxJX9104cwKigBbimVvzDJoOkfVQnV75MF6654HYhTZ-Y5WSp-cuPDlaibV4nPZjOsV0m1HEVaQYKc39iCPUbtN4Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:  matinsp.job@gmail.com  سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4188" target="_blank">📅 21:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4187">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:  matinsp.job@gmail.com  سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4187" target="_blank">📅 21:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4186">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:
matinsp.job@gmail.com
سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4186" target="_blank">📅 21:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4185">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D7A9NhXSZO1IpJC90hiY6cAgrPT_XJo4I0_dDTiC1uzCgQ3uDZ2kj25dgVJhAFAk_0cjxcXe3K4B5jFq2GR6LGsd0BTnjXDLS2uGkUgAb9SYwv6WY5sx7CdTiw3-OVfMs31sI4lXDLR6P0jO6Jbi9huuNe2VOPLOnt86neFiNIe4iyAG_bm5NJhl_QDEgAlqBNk6nTJVfLoO9XUzEo5-l_G4Oyk2EWW_Jb5M5RC_PQTLOlCE-o6Vd1aEdaw4pAuXrLvxVc26IwBgg-hHmr1EZyEpJTGvqiImQM2m-ff_nLweCU57FfdHjHt-QugVllLx7-0B7Yyux6VqBG82CDHE3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی هم تر و تمیز و عالی</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4185" target="_blank">📅 21:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4184">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فیلم آموزشی Clash Party
https://youtu.be/gMFH88yRghg</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4184" target="_blank">📅 21:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4183">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4183" target="_blank">📅 21:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4182">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.
نتیجه این تست، هر ۳۰دقیقه داخل این مخزن گیتهاب برای سرویس های متفاوت قابل دسترسی خواهد بود.
🌎
ساب مناسب اپ های V2Ray, V2rayNG & ...
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
🌎
ساب مناسب Clash Mi, Clash Party
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
🍏
IOS App
: Clash Mi, Karing
👾
Android App
: Clash Party, Karing
👍
Mac App
: Clash Party
📱
Windows App
: Clash Party
📱
Linux App
: Clash Party
@WhiteDNS</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4182" target="_blank">📅 21:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4181">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بن شدن حساب‌های کلاد واقعا نگران کننده شده. هرکسی هم بن شده از ایرانیکارت خرید کرده یا سابقه خرید داشته</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4181" target="_blank">📅 20:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4180">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بن شدن حساب‌های کلاد واقعا نگران کننده شده.
هرکسی هم بن شده از ایرانیکارت خرید کرده یا سابقه خرید داشته</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/4180" target="_blank">📅 19:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4179">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">☠️
نصب و استفاده از Hermes، آینده‌ی هوش مصنوعی
⚡️
فایل لینک‌های مورد نیاز: https://t.me/MatinSenPaii/4178
⭐️
توی این ویدئو: 00:00 چرا هرمس؟ چه استفاده‌هایی میتونیم ازش بکنیم؟ 04:17 نصب و راه اندازی روی دسکتاپ(ویندوز، مک، لینوکس) 13:47 نصب و راه‌ اندازی روی…</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/4179" target="_blank">📅 17:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4178">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hermes-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">886 B</div>
</div>
<a href="https://t.me/MatinSenPaii/4178" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دستورات نصب Hermes روی سیستم‌عامل‌های مختلف و سرور
سایت YottaSrc:
https://yottasrc.com/
سایت Netlen:
https://www.netlen.com.tr/
سایت Senko:
https://senko.digital/</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/4178" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4177">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qhg_exNz9D1D908k9cZTo2geBqgZ8k5eQxxOXgjLfgQxzuOO2Zdmv-ISVLZGDAEAegnvGL94etCGUMX_O3BNzFEODS9EZV4QrvCZ_tYo7Hdse2g14ONu2vWNZdY58J4U7lpblmrQzIPVEUOb_ec3bePyNiSQbww1cuFI_4v5g3yDdg7-kBvviut1QbidGlCAWy7YyoDyfhGHySG4uNDfty1NkIS-3jr5u81OdZGxa1OrpMtKrbz65o6omTRQDv7t5bpKoGj4WvVwupTbUXMCUQV6qv28v-WoVou65KIuzZOTCVLKYwhLuquKdcnrZyVKC4sXdozNsbDs2OmSOwXgwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
نصب و استفاده از Hermes، آینده‌ی هوش مصنوعی
⚡️
فایل لینک‌های مورد نیاز:
https://t.me/MatinSenPaii/4178
⭐️
توی این ویدئو:
00:00 چرا هرمس؟ چه استفاده‌هایی میتونیم ازش بکنیم؟
04:17 نصب و راه اندازی روی دسکتاپ(ویندوز، مک، لینوکس)
13:47 نصب و راه‌ اندازی روی سرور لینوکسی
16:46 نصب 9Router روی سرور لینوکسی
18:10 استفاده از API و مدلهای رایگان قدرتمند Nvidia
21:20 دور زدن محدودیت دسترسی به API ها با Worker کلودفلر
22:40 استفاده از Endpoint 9Router بر روی لینوکس و ساخت Combo
24:31 اتصال Hermes به اکانت تلگرام( و واتس اپ و دیسکورد و...)
26:35 نوشتن یه کرون جاب کوچولو که هر 5 دقیقه قیمت بیت کوین رو بفرسته و تحلیل کنه
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. دو تا ویدئوی قبل رو دیده باشید، عالیه
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/4177" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4176">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ویدئو 2 ساعت و نیم ضبطش زمان برد، بعد از ادیت شد نیم ساعت
😭
دستم شکست انقد با موس اسکرول کردم</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4176" target="_blank">📅 04:15 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
