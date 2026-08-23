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
<img src="https://cdn4.telesco.pe/file/i8NolV736fDDHYAkbn6BJVxJg-uuHwB5UYaYqHAs73SnfTNY1bo1T8C__eqv0LTlMWJtfmXoFL93Uop4EkmyRc6ll4aLyt0mBWD-TvWmuj-7JZHJmzV_9oZf3Amb_BkGsjZtWlgusDvnEUFybwumK_NMjAjZr2yeM_LzlkUBMWCsjTmI9LJ86CGEJasvp3Aypw35RrG_DcNYrBhs3KUhpAPolnTLC4cegt11Ysn3VbFxDXo1YX833zd79ld6Pd4LJikKJLeYaES2J7sx1Df5Lp_ZxFy17zxv67q_OFHGJ0umbzLla8rrBJwa6mVRwnQW0_pcqv1JYy015IyUyTNJdQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 442K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 23:42:06</div>
<hr>

<div class="tg-post" id="msg-21406">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اناق جنگ با یاشار : این خلاصه از بهترین ویدیوها از ساعتی پیش که مسابقه شروع شد تا همین دقایقی پیش درست کردم که هیچ جا پیدا نمیکنید.
گرندپری «Freedom 250» در قلب واشنگتن و در مسیر اطراف نشنال مال برگزار می‌شود؛ مسابقه‌ای ۲۵۰ مایلی که نماد ۲۵۰ سالگی استقلال آمریکاست. ترامپ که با فرمان اجرایی زمینه برگزاری آن را فراهم کرد، پیش از آغاز مسابقه با خودرو ریاست‌جمهوری یک دور نمادین زد و پرچم سبز شروع را به اهتزاز درآورد. هم‌زمان، نمایش هوایی گسترده‌ای با حضور بمب‌افکن‌های راهبردی B-2، B-1B و B-52 برگزار شد تا قدرت نظامی آمریکا نیز بخشی از این نمایش ملی و میهن‌پرستانه باشد. هم اکنون ترامپ از جایگاه ویژه در حال مشاهده مسابقه می باشد. البته بیشتر در حال صحبت کردن با اطرافیان است تا این لحظه…
@WarRoom</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/withyashar/21406" target="_blank">📅 22:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21405">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">جمهوری اسلامی اعلام کرد از امشب هر نفتکشی از مسیر جنوبی تنگه ی هرمز(متعلق به عمان و آمریکا) عبور کنه جریمه میشه و یا خود کشتی توقیف میشه و یا اموال کشتی مصادره میشه.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/withyashar/21405" target="_blank">📅 22:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21404">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">شاهزاده رضا پهلوی: قیمت دلار امروز از مرز ۲۰۰ هزار تومان گذشت. امروز قیمت دلار ۲۸٬۵۷۱ برابر زمانی است که جمهوری اسلامی به قدرت رسید. حاصل نزدیک به پنج دهه حاکمیت فساد و ناکارآمدی در جمهوری اسلامی، فقر، فساد و انزوا برای ملت ایران بوده است. تجربه این پنج دهه یک مسئله را برای همه روشن کرده است: در جمهوری اسلامی اصلاح ممکن نیست. قطار ایران در بهمن ۵۷ از ریل تمدن و پیشرفت خارج شد و امروز جمهوری اسلامی آن را با سرعت هرچه بیشتر به ته دره هدایت می‌کند. امروز وظیفه تک‌تک ایرانیان، از جمله کارمندان دولت و بدنه اداری کشور، این است که به هر شکل ممکن با اخلال در فعالیت‌های مخرب جمهوری اسلامی و تضعیف آن، زمینه برکنار کردن رژیم و نجات ایران را فراهم کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/withyashar/21404" target="_blank">📅 22:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21403">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مایک جانسون، رئیس مجلس نمایندگان آمریکا، به فاکس‌نیوز گفت آمریکا در حال ورود به مرحله جدیدی از جنگ علیه ایران است و دولت ترامپ همچنان به‌دنبال پایان دادن به جنگ است.
او گفت تمرکز مرحله بعدی بر
فشار اقتصادی و تحریم‌های شدیدتر
خواهد بود و دولت آمریکا می‌خواهد با افزایش فشار، تهران را به پذیرش یک تسلیم وادار کند. جانسون همچنین گفت ترامپ «شبانه‌روز» برای حل‌وفصل جنگ تلاش می‌کند. این اظهارات هم‌زمان با اعلام اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره اعمال
«سخت‌ترین تحریم‌های تاریخ» علیه ایران
مطرح شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/21403" target="_blank">📅 21:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21402">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d23c54da.mp4?token=Rg9qwhoGYttfu1-wBR9VRIvkitfYD9G73QE7W8laU48BK7nArjSOxt1ZrdrzXCl_Nkfg_71HPgIFapodxtOSsrLdgls-xyw43WR-m8Bs8Z5AgXXvR7ElwrOrUpsQhkQycTFebiQ6bn3Vw20ct2107mQAnYFHMwlEYI3JyuQONF9emzgndNtQL-eDMxftc5tVcqYF5-y5B5hZGqoONmbgOZm1RMYuS7c0l94OG0TTO28VjOfjvqolBGjnfODvFUUBp0HUEtXZzmcyXJwI9_xlYJ6p5scm5ZLLlQ6HziB7e0KtFpj2FCmzHTHFkc83JRvn5yOE4V5qKFFNWyp9WzJr7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d23c54da.mp4?token=Rg9qwhoGYttfu1-wBR9VRIvkitfYD9G73QE7W8laU48BK7nArjSOxt1ZrdrzXCl_Nkfg_71HPgIFapodxtOSsrLdgls-xyw43WR-m8Bs8Z5AgXXvR7ElwrOrUpsQhkQycTFebiQ6bn3Vw20ct2107mQAnYFHMwlEYI3JyuQONF9emzgndNtQL-eDMxftc5tVcqYF5-y5B5hZGqoONmbgOZm1RMYuS7c0l94OG0TTO28VjOfjvqolBGjnfODvFUUBp0HUEtXZzmcyXJwI9_xlYJ6p5scm5ZLLlQ6HziB7e0KtFpj2FCmzHTHFkc83JRvn5yOE4V5qKFFNWyp9WzJr7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : از زمان ازسرگیری محاصره دریایی علیه ایران، مسیر ۷۰ کشتی تغییر داده شده و فعالیت ۳ کشتی دیگر نیز متوقف شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/21402" target="_blank">📅 21:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21401">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">واشنگتن پست : تعداد مجروحان آمریکایی در جنگ با ایران به 774 نفر افزایش یافته است. این آمار شامل 18 کشته و 756 مجروح است. طبق داده‌های وزارت دفاع آمریکا، حدود 60 مورد جدید از جراحات در روزهای اخیر ثبت شده است، که شامل آسیب‌های جدی مغزی ناشی از انفجارها در حملاتی است که پایگاه‌های آمریکایی در منطقه را هدف قرار داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/withyashar/21401" target="_blank">📅 20:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21400">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نتانیاهو: ما به شرایط قبل از ۷ اکتبر باز نخواهیم گشت و اجازه نخواهیم داد هیچ گروهی در غزه به شهرها و مناطق اسرائیلی تهدید کند یا امنیت را تضعیف نماید.اگر حماس فوراً از پرتاب بالن‌ها و برگزاری تظاهرات‌ها خودداری نکند، هدف قرار دادن مسئولان این اقدامات را تشدید خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/21400" target="_blank">📅 20:21 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21399">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سخنگوی دولت : خبر خوش برای مردم، سود سهام عدالت (۲-۳ دلار) از 2 تا 8 شهریور واریز میشه
@WarRoom</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/21399" target="_blank">📅 20:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21398">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اورشلیم پست گزارش داده است که اسکات بسنت، وزیر خزانه‌داری آمریکا، قرار است روز دوشنبه ۲۴ اوت در یک نشست خبری جزئیات برنامه جدید دولت ترامپ برای تشدید فشار اقتصادی بر ایران را اعلام کند. این نشست ساعت ۲ بعدازظهر به وقت شرق آمریکا برگزار می‌شود که با توجه به…</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/21398" target="_blank">📅 19:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21395">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اکسیوس: وزیر خارجه سوریه، اسعد شیبانی، امروز یکشنبه با رئیس سازمان اطلاعاتی اسرائیل (موساد)، یوآو گالفمن، دیدار کرد تا تلاش‌هایی برای کاهش تنش بین دو کشور صورت گیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/21395" target="_blank">📅 19:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21394">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/21394" target="_blank">📅 19:21 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21393">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/21393" target="_blank">📅 19:07 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21392">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بی بی نتانیاهو الان این شماره رو گذاشته  مردم زنگ بزنند اگه عبری بلدید صدای مردم ایران باشید
+972544700047
@WarRoom</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/21392" target="_blank">📅 18:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21390">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c60dddfa42.mp4?token=irlMmnkPdlPmLwQstZkNX5-HifNoCZpb9qebKH5o2aKy4B6HMNQn10YRISrp4YEBroMM5bO_kgv67jlxoEBtKtTZ0T5TmFZMgYVpM9EgOdPJ0DlxGtK-qQuZX0_KI9g9TL_QunYeQLkLhIC0BMFibbHs8nO8EkWXmMvhYjjrLG_RcIg_uGi66NgWaWPXbdADW_4Nvfb8NIZnP_6s3ISFXv0Cw4Ccg6xs2ZRPah5KRimZk7c50xztHZK2opcimmY46rtJpilU8PJ8YLEowTsTUbWfqvHrih_VIYcv95nDViPWZ_U3Xn2bNvLCTmdpjzkgkCLJLnU3JoEoZvCwEaRioRB7a62YNHuN6ti2BQqhsiAIaJUpmNoXaShRs3LCggBdhba6rv_l0PsC3nK2VGSo9ykoGxxvlQpP5AvxPX6m9uY7iwWk62MlMU7J4q3WMNLMKEsGdwcofK0Nx0Ncxtrz9EtnbThMlE_Bwb3o3p5D7hjj2ii0gsiBmMhH6HHzVmG53QtBYifswhcm318S1fF4GI4CDhV23yfddd01fVk2tNbkc_19zUzLj_mimfzHWKrugd5Z6Nw-RsYVkQ261MYlZLKZbY7AKYA_eoO-KysdqxWDRiRgmvKrpy71qtRcpmh62Vp3-w_nsJJgmR7ppFTZ5oEgNsiwu-0W-_OFKhdPTAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c60dddfa42.mp4?token=irlMmnkPdlPmLwQstZkNX5-HifNoCZpb9qebKH5o2aKy4B6HMNQn10YRISrp4YEBroMM5bO_kgv67jlxoEBtKtTZ0T5TmFZMgYVpM9EgOdPJ0DlxGtK-qQuZX0_KI9g9TL_QunYeQLkLhIC0BMFibbHs8nO8EkWXmMvhYjjrLG_RcIg_uGi66NgWaWPXbdADW_4Nvfb8NIZnP_6s3ISFXv0Cw4Ccg6xs2ZRPah5KRimZk7c50xztHZK2opcimmY46rtJpilU8PJ8YLEowTsTUbWfqvHrih_VIYcv95nDViPWZ_U3Xn2bNvLCTmdpjzkgkCLJLnU3JoEoZvCwEaRioRB7a62YNHuN6ti2BQqhsiAIaJUpmNoXaShRs3LCggBdhba6rv_l0PsC3nK2VGSo9ykoGxxvlQpP5AvxPX6m9uY7iwWk62MlMU7J4q3WMNLMKEsGdwcofK0Nx0Ncxtrz9EtnbThMlE_Bwb3o3p5D7hjj2ii0gsiBmMhH6HHzVmG53QtBYifswhcm318S1fF4GI4CDhV23yfddd01fVk2tNbkc_19zUzLj_mimfzHWKrugd5Z6Nw-RsYVkQ261MYlZLKZbY7AKYA_eoO-KysdqxWDRiRgmvKrpy71qtRcpmh62Vp3-w_nsJJgmR7ppFTZ5oEgNsiwu-0W-_OFKhdPTAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جنگ اخیر کی بیشترین پول رو در آورد ؟!
@WarRoom</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/21390" target="_blank">📅 18:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21389">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کمیسیون امنیت ملی جمهوری اسلامی:
دریافت هزینه خدمات از کشتی‌های عبوری از تنگه هرمز تصویب شد‌.
@WarRoom</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/21389" target="_blank">📅 18:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21388">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a2f95843.mp4?token=agShzAAwLDohp3fETIugH-B2kPJ-blNjo1__iIuZqEIesFg4764lEJbjzmLgWclbr397W4qqyZDXxvTK6Kn2x1FTJ6kUPcToNF7VBBKw8M-Su9zS2qrjDWalpRgJWMBH3e4PapT6S6Hf4nInAueH4IYMRg-RMiWszlwAex9FKNdxJdUANvIc0gXMPZogGJnmBm7ulPyYPy8B_KDNnUTNthuTaSNBSZ1BBzUaLjibuHPbF4pz1HZNqUgSkDeZPwmjl_3Vuvlm3NsZ5pjjYLuHuM2nUxNjqpQyLPZMv0Nt2jrTtsL_niyorFZvRGn8h6MzsJpnDQL7k_VAYEBC6QPHaIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a2f95843.mp4?token=agShzAAwLDohp3fETIugH-B2kPJ-blNjo1__iIuZqEIesFg4764lEJbjzmLgWclbr397W4qqyZDXxvTK6Kn2x1FTJ6kUPcToNF7VBBKw8M-Su9zS2qrjDWalpRgJWMBH3e4PapT6S6Hf4nInAueH4IYMRg-RMiWszlwAex9FKNdxJdUANvIc0gXMPZogGJnmBm7ulPyYPy8B_KDNnUTNthuTaSNBSZ1BBzUaLjibuHPbF4pz1HZNqUgSkDeZPwmjl_3Vuvlm3NsZ5pjjYLuHuM2nUxNjqpQyLPZMv0Nt2jrTtsL_niyorFZvRGn8h6MzsJpnDQL7k_VAYEBC6QPHaIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زامبی ؟ بدترشه ، نسل ۵۷
@WarRoom</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/21388" target="_blank">📅 17:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21387">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بنیامین نتانیاهو:
«پهپادهای کوچک می‌توانند بسیار مرگبار و دقیق باشند و به‌سختی دیده شوند. ما سال‌هاست روی مقابله با این تهدید کار می‌کنیم و آن را در اوکراین، لبنان و ایران دیده‌ایم. حالا تلاش می‌کنند این تهدید را دوباره احیا کرده و وارد غزه کنند. دستور من به دستگاه امنیتی و ارتش اسرائیل این است که
خود پهپاد، اپراتور آن و محل شلیک یا پرتابش را هدف قرار دهند و هر کاری لازم است برای محافظت از شهروندان اسرائیلی انجام دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/21387" target="_blank">📅 17:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21386">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">میدل ایست آی: ده‌ها پایگاه اروپایی در جریان جنگ ۴۰روزه از عملیات آمریکا علیه ایران پشتیبانی کردند؛ بریتانیا احتمالاً مهم‌ترین حمایت را ارائه داد و پایگاه‌ها و زیرساخت‌های نظامی آن، از جمله دیه‌گو گارسیا، در پشتیبانی از عملیات آمریکا مورد استفاده قرار گرفتند. فرانسه نیز به هواپیماهای نظامی پشتیبانی آمریکا اجازه فرود و استفاده از پایگاه‌های خود را داد. بلغارستان هم اجازه استفاده آمریکا از فرودگاه‌ها و خاک خود را صادر کرد و به این ترتیب، با وجود مواضع متفاوت برخی دولت‌های اروپایی در قبال جنگ، زیرساخت‌های نظامی کشورهای مختلف اروپا در پشتیبانی از عملیات آمریکا علیه ایران نقش داشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21386" target="_blank">📅 16:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21385">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نیویورک پست
: در هفته گذشته حدود 200 کشتی چراغ خاموش از تنگه هرمز عبور کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21385" target="_blank">📅 15:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21384">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دیجیکالا از دسترس خارج شد تا بعدن بتونه گرونتر بفروشه
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21384" target="_blank">📅 15:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21383">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">یاشار داش دلار تو بازار من الان 210 چنج کردم</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21383" target="_blank">📅 15:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21382">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏دونالد ترامپ در‌تروث با انتشار ویدیویی جنجالی از سخنرانی خود، به انتقاد شدید از تلاش‌های حزب دمکرات برای محدود کردن اختیارات نظامی رئیس‌جمهور آمریکا پرداخت.
‏او در این اظهارات طعنه‌آمیز گفت : اگر علی خامنه‌ای در حملات کشته نمی‌شد، دمکرات‌ها احتمالاً او را برای ریاست‌جمهوری سال ۲۰۲۸، سنای میشیگان یا حتی مدیریت کمیته ملی دمکرات‌ها (DNC) نامزد می‌کردند!
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21382" target="_blank">📅 14:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21381">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حمله هوایی اسرائیل به غزه
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21381" target="_blank">📅 14:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21380">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دلار کف فردوسی ۲۰۱،۰۰۰ تومان
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21380" target="_blank">📅 14:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21379">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دلار ۱۹۹.۰۰۰ تومان (رکورد تاریخی)  تتر  ۱۹۷.۰۰۰ تومان (رکورد تاریخی)  بیتکوین ۷۶.۶۱۶ $ انس جهانی طلا ۴.۶۰۲ $ (آخرین قیمت) نفت برنت ۹۳.۹۹$ (آخرین قیمت) @WarRoom ساعت ۱:۳۰ دقیقه تهران</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21379" target="_blank">📅 14:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21378">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دلار ۱۹۹.۰۰۰ تومان (رکورد تاریخی)
تتر  ۱۹۷.۰۰۰ تومان (رکورد تاریخی)
بیتکوین ۷۶.۶۱۶ $
انس جهانی طلا ۴.۶۰۲ $ (آخرین قیمت)
نفت برنت ۹۳.۹۹$ (آخرین قیمت)
@WarRoom
ساعت ۱:۳۰ دقیقه تهران</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21378" target="_blank">📅 13:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21377">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حبس مهریه بالای ۱۴ سکه حذف می شود
نماینده نجف‌آباد در مجلس اعلام کرده طرح اصلاح نحوه اجرای محکومیت‌های مالی در صحن علنی تصویب شده و بر اساس آن، مجازات حبس برای مهریه‌های بالای ۱۴ سکه حذف می‌شود.
برای مهریه‌های زیر ۱۴ سکه نیز امکان اجرای حکم با استفاده از پابند الکترونیک پیش‌بینی شده است.
این مصوبه برای بررسی و تأیید نهایی به شورای نگهبان ارسال شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21377" target="_blank">📅 13:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21376">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">رسانه های کره شمالی : دولت کره شمالی اعلام کرده است که قصد دارد توافق دفاعی با ایران امضا کند. در صورت نهایی شدن، این اقدام می‌تواند منجر به تعمیق همکاری‌های نظامی بین پیونگ‌یانگ و تهران شود. این توافق بالقوه در بحبوحه تنش‌های جاری بین ایران، ایالات متحده و اسرائیل مطرح شده
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21376" target="_blank">📅 13:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21375">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">صداوسیما در اقدامی ، اطلاعات به ادعای آنها محرمانه و مکان‌های دقیق تردد پسر ترامپ و نقاطی که در تیررس است را منتشر کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21375" target="_blank">📅 12:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21374">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بامداد امروز یک شهریور، کارخانه‌ نوشابه‌سازی ایرانشهر طی حادثه‌ای در آتش سوخت. هنوز از میزان خسارت‌های مالی اطلاعات دقیقی منتشر نشده است. مسئولین این واحد تولیدی در حال پیگیری این ماجرا هستند. @WarRoom عمو نوشینیاهو ، بی بی کولا</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21374" target="_blank">📅 12:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21373">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رسانه های عربی : ارتش اسرائیل (IDF) مدتی پیش به ساختمان‌های متعلق به گروه‌های تروریستی در روستای زوتر الشرقیه و حداتا در جنوب لبنان حمله کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21373" target="_blank">📅 12:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21372">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دلار ۱۹۶،۴۰۰ تومان (رکورد تاریخی)
دلار بازار آزاد ۲۰۰،۰۰۰ تومان
تتر  ۱۹۵.۳۶۰ تومان
بیتکوین ۷۶،۲۳۷ $
انس جهانی طلا ۴.۶۰۲ $ (آخرین قیمت)
نفت برنت ۹۳.۹۹$ (آخرین قیمت)
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21372" target="_blank">📅 11:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21370">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4i5kn0KxwzTl_UnxkHpYrnZlURdAEVRjFwlq7-L3r-uOVjlTjZYyOhIPMW8Tm4dstlocAzEhB5wUi9crmFZLSUSdMmFDmMDq8OPiylZWDU4XNQnX6IsF7s3UJ9N3nmVxvJASXvr7FG6s6xpRVN9jW7yAQRyrXLLYqV0q1noJ7lVZfv51LFThTn2XTOvgWWuFkEunN0NCf38IVrYWrxB8i9nkajpVXGL53RQOBtR8t3xiycvD6ygbq640pHkFW-O5KEvMyTYhb9bQUnomWCW8JjaIHsGIVtpkCiF4Y-iuhkKWd1TY1uc--fCoCSmRX9fxk8SyO1-dHVnmzb78h5J4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بامداد امروز یک شهریور، کارخانه‌ نوشابه‌سازی ایرانشهر طی حادثه‌ای در آتش سوخت.
هنوز از میزان خسارت‌های مالی اطلاعات دقیقی منتشر نشده است.
مسئولین این واحد تولیدی در حال پیگیری این ماجرا هستند.
@WarRoom
عمو نوشینیاهو ، بی بی کولا</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21370" target="_blank">📅 11:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21369">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وزیر امور خارجه سوریه:پیش‌بینی می‌کنم که به زودی مذاکرات با اسرائیل در مورد یک توافق امنیتی از سر گرفته شود. ما دست دوستی دراز می‌کنیم و از اسرائیل می‌خواهیم که از این فرصت تاریخی استفاده کند
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/21369" target="_blank">📅 11:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21368">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">العربیه: فرمانده ارتش پاکستان، عاصم منیر، روز دوشنبه با پیام‌هایی از آمریکا به تهران سفر می‌کند.
این سفر در چارچوب تلاش‌های پاکستان برای شکستن بن‌بست دیپلماتیک ایران و آمریکا و از سرگیری مذاکرات پس از ناکامی دو طرف در دستیابی به توافق نهایی درباره پرونده هسته‌ای و تنگه هرمز انجام می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21368" target="_blank">📅 11:32 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21367">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4wZAPIJJmXAz-kMDkcxS9Omn5WwT3Ohk7FF2LP1I6YxLNTDDXOOiPKy8VgHvUSDg3Ehsni49948fWzyEO7hlfI-vHMlGQd03CLorJmTc2DU1ZPCaVx99121xZubgq_jjRQlaiSV5A4EqCO9224DYkTWY_UjTJA8Vit0Y13pJVyFQ1hdDXb6a5_bv19kGxDwjhmyW2LxS2NE6Qp083GGxbyRnKG3JQ_aMCypbap-o1uTWRu_a33B5LlTVGSzqhLRTuMOgDR6no4KB7kGvQSSxsSZ51VRdOtNwr5RgzDTLpPRH5psFVfYLnvbafICwZbe5P3hop95nkjkiaDUGMpecQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهده دایناسور در مناطق بیابانی خراسان رضوی تکذیب شد
دبیر شورای اطلاع رسانی اداره کل حفاظت محیط زیست خراسان رضوی
:
طی روزهای اخیر تصویری در شبکه‌های اجتماعی دست ‌به‌ دست می‌شود که موجودی شبیه دایناسور را در محیطی بیابانی در شهرستان بینالود نشان می‌دهد.
تصویر مذکور کاملاً مصنوعی، تولید شده توسط هوش مصنوعی و فاقد هرگونه واقعیت میدانی است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21367" target="_blank">📅 11:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21366">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">روزنامه تلگراف بریتانیا : هکرهای ایرانی یک حمله سایبری بی‌سابقه به یک نیروگاه در بریتانیا انجام دادند که منجر به از کار افتادن آن به مدت ۴ روز شد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21366" target="_blank">📅 11:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21365">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e96ca1be3f.mp4?token=E0B3cgpgbuLbnAZzL0k1bZb-QWuF9a6dnGXNM7I0j29SlknySE5ABAjObxhsQvq8TexxjRWwY-rQoeCSa8Fzvhp5iGhpv3d-XeIsc7Ko_Q2ERUgCnknYCrm-kOmhjp1HtcT4ZgVmK2_pQqV_TreqPXSTpRyE1mzGe1Zc-0Ol_auUGjFod0fvAfRhK9IpStSpyqkhHFw1CdxylY5xaqhcTBbMts-9ZsnAoICvujW0j3XTzyrgvIE6Oc6OoO-1igUTaNCafwTfFH7a795ULSbnhqXA5sVvcB6VhpQJ-QaKRcRsyRFz1alg6tCf9Uyh7yX62XUboZZ9CKGugqJh9YH3AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e96ca1be3f.mp4?token=E0B3cgpgbuLbnAZzL0k1bZb-QWuF9a6dnGXNM7I0j29SlknySE5ABAjObxhsQvq8TexxjRWwY-rQoeCSa8Fzvhp5iGhpv3d-XeIsc7Ko_Q2ERUgCnknYCrm-kOmhjp1HtcT4ZgVmK2_pQqV_TreqPXSTpRyE1mzGe1Zc-0Ol_auUGjFod0fvAfRhK9IpStSpyqkhHFw1CdxylY5xaqhcTBbMts-9ZsnAoICvujW0j3XTzyrgvIE6Oc6OoO-1igUTaNCafwTfFH7a795ULSbnhqXA5sVvcB6VhpQJ-QaKRcRsyRFz1alg6tCf9Uyh7yX62XUboZZ9CKGugqJh9YH3AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت من وقتی یه شب دیگه هم باز نزد !
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21365" target="_blank">📅 03:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21364">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLadan</strong></div>
<div class="tg-text">ترامپ فعلا داره با کانادا کل کل میکنه. توی کانادا همه از دستش کلافه شدن، دیوانه باعث شده وضع خراب بشه و همه چی گرون شده بیش از حد</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21364" target="_blank">📅 02:21 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21363">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">چرا خبری نیست ، ترامپ آخر هفتست شلکس‌ کرده
😁</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21363" target="_blank">📅 02:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21362">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcvH0wT6sJl6DQpvQyPTqg9UJFUSfeRQuNcqrKpqaTn2LVLy4YU8YOumGOlum5zDPWjizjdywGeMbfo-20ePPwJtvdKOSShSdKQIxVlJj0vpFjrWDahARp4uZhERLT_is40Pq4rT6B0PJyMAD47HOSnIPMRLnO0cAl8yP2gwFJdgswZg72BJ2qthUDnW7Y03XlZ_jBlLYrX8CBWF5vESmwhdXry7G_a1FlYf17REs9S8BjXR0JcVs_RzPFGxM9SSsHjKDiJd8JiW6il7nLvLEkHpGd53kXzQXQkxrL3llwZ2JR5KCTkCUd1HC28zEjevd_hASqP0Z_NRQCbWXHF78g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث دوباره انتشار داد : قلمرو جدید ایالات متحده : تنگه هرمز.
مقامات کاخ سفید بار اول که این پست منتشر شد به رسانه‌ها گفته بودند هدف رئیس جمهور از این پست شوخی است. خود ترامپ امروز به فاکس نیوز، از لفظ در حال حاضر تنگه برای‌ماست استفاده کرده و با توجه به نوشتن نام خلیج فارس، کاملاً مشهود است که این پست خطاب به حاکمان رژیم جمهوری اسلامی است و به آنها نشان می‌دهد تا زمانی که آنها هستند کنترل تنگه در دست آمریکا است .
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/21362" target="_blank">📅 00:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21361">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFbis9LsOQE944tsFLbDc9qwXBmjja9ZhQO1mqLegj8G1PaFlwjKrDXeI5aARH-mnnwbgohw-dTWAxHNj0DIqCvHKqYN5DIUrE76L0lOk1pPuUbiby5t94n2IeXSh73N6YoaUqLqRQ43ex0nmIBadU5XL0o5naGmS9LAkdgBcx_C2R7wUH0t23H6KHAt5oQxBbY_khWwJ0E2ogx39t-IHA0lNAcr9buc2J_a3PhoPl28PiGRvNlAOOv84WymQXvsoeCPfewVfJZNVbR6TlsdU4czEYEXAv_Zv4dxH6UbNHCjHVJqpmT74bieOHkbbmCH8LnhF_mGcu6gzZQmT20GZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن کج بند رضایی : مردم خودشون در خانه‌ها و محلات شروع به تولید محصولات مورد نیاز جامعه باید بکنند. @WarRoom یاشار : یعنی‌کوکتل مولوتوف درست کنند ؟
😂
😂</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21361" target="_blank">📅 00:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21360">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM</strong></div>
<div class="tg-text">الان ما تخم مرغ لازم داریم چطوری تخم بزاریم. یه امار بگیر اگه کسی بلده به مام یاد بده</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21360" target="_blank">📅 00:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21359">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">محسن کج بند رضایی : مردم خودشون در خانه‌ها و محلات شروع به تولید محصولات مورد نیاز جامعه باید بکنند.
@WarRoom
یاشار : یعنی‌کوکتل مولوتوف درست کنند ؟
😂
😂</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/21359" target="_blank">📅 23:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21358">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2d5b2a1a8.mp4?token=JgrSKmt1mrIf8_3McJbqXd2cgHpqZ1OZckYurXwvBnR_j5ql-thPmlYQXygb3pyYVfrim0ipMb-SOfRpaZUDkO_R9sH77XGGwbl7bUHMfoGgNJDefN5VwSGALF7y4vDbMTecROrFcvG9tZ6ApCmWsSp0BhAnwN-3wg7QFn1LeUsd0nObLbLXVUekaD36TcmnzB1-R3HJp8sNwB7QvnqJboPcYtc-DIB640sCbal4AnkXb8AJUHo_Fvvo0J8zlowrgAwTm-f7AFK6xMgJhRdEnSlPPhddVquePvBP2tmFK5GIV-53YT0WongHxI0G5Vj5w5fVyP62QlOGP5APTD38cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2d5b2a1a8.mp4?token=JgrSKmt1mrIf8_3McJbqXd2cgHpqZ1OZckYurXwvBnR_j5ql-thPmlYQXygb3pyYVfrim0ipMb-SOfRpaZUDkO_R9sH77XGGwbl7bUHMfoGgNJDefN5VwSGALF7y4vDbMTecROrFcvG9tZ6ApCmWsSp0BhAnwN-3wg7QFn1LeUsd0nObLbLXVUekaD36TcmnzB1-R3HJp8sNwB7QvnqJboPcYtc-DIB640sCbal4AnkXb8AJUHo_Fvvo0J8zlowrgAwTm-f7AFK6xMgJhRdEnSlPPhddVquePvBP2tmFK5GIV-53YT0WongHxI0G5Vj5w5fVyP62QlOGP5APTD38cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتشبازی برای اجرای‌حکم عروسکهای نتانیاهو و ترامپ بود
😂
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/21358" target="_blank">📅 23:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21357">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گزارش های زیاد از انفجار در تهران سمت انقلاب فعلا میترسم یهو میگن جشن امام ۱۸ ام بوده
😂
فقط بدونید @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21357" target="_blank">📅 23:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21356">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ET3odEiWBhqe_MFm8ERodacVlAn8Jjru9ycZqOVOTojZ4YDvIyTx7VwZR7qjRiC_NqKg8JoVXxC2dT-WoGWfOWIqFeSE0c7I2tqgoCHu5eVcicWVCN81lGV3uCT2SPomHfXJurut78HAXNqndluV6s78yBQXr-uX1Oq14zZ95_t4oirCUvYpAvxwKwx0a96Be9lI-90dMeq-uv8h0bAgHn0NznZjsl6HgdzMcMVJPdYktXAPb_aZfBicx7dNl8MV8VFF7C6mvIHvs5yhrh5Dk-CmJ4ukBiWNhhNC9y4dQr1IG_KYByOlQ6oNSz6-86iZeAiLri9itg31ROxqX877mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش های بسیار زیاد ، ستون دود تهران از زاویه دیگر
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21356" target="_blank">📅 23:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21355">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b588a12e.mp4?token=eBkCaM5PsqtvBjsE5skifTK55wh2G1VNJde2zkUD-viAOkMnLBNohUUnqtGDTp1j-NwvVmryZkIPMAnoddkTq72X-XnuTRHDstpbTsHiYFG4oRahFGl1UedDWrA3L_iHhKvowGaLVwHme9Pig_5LH58rlvHwmVaYoy02QmEEF44lSeAn3ExC3ZDOP9pGLhu7j93dUksetK4uRKZcmemi5oq5h0Ny8M4PQQDejALJpcDkLGiDWeRrBpr8YxRb5J9T8WBDMofk9SKPJ-RSvECpbe-hyIkjKgrKtKUcc1iXJra7r1MJmPP09Zk6X0nySvFamOicqIU8enIxSfwTyuG2vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b588a12e.mp4?token=eBkCaM5PsqtvBjsE5skifTK55wh2G1VNJde2zkUD-viAOkMnLBNohUUnqtGDTp1j-NwvVmryZkIPMAnoddkTq72X-XnuTRHDstpbTsHiYFG4oRahFGl1UedDWrA3L_iHhKvowGaLVwHme9Pig_5LH58rlvHwmVaYoy02QmEEF44lSeAn3ExC3ZDOP9pGLhu7j93dUksetK4uRKZcmemi5oq5h0Ny8M4PQQDejALJpcDkLGiDWeRrBpr8YxRb5J9T8WBDMofk9SKPJ-RSvECpbe-hyIkjKgrKtKUcc1iXJra7r1MJmPP09Zk6X0nySvFamOicqIU8enIxSfwTyuG2vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدای انفجار و ستون دود تهران ، دقایقی پیش
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21355" target="_blank">📅 23:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21354">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBD1MaPfX9H5ZDzN68Ha6FKwlAI3NXxewPeA9HIQXqAqVtRS_P25wG81Fv9zMXo5J9rXKezzftdMfZjs8MxDmGFZunH-vhU36xWIcwjU1mk0d1T7rteoJj9Zhcje60feqq5_kIVzMcsBgHm8iABcs6Ka_r8IRi0h_jX__gd2muhAkV4mMLJrCYq4glkD163QmbodYpVZRE1UkOW0AuKCB0-z4Q4n7RDOydXdB68ifUI940lXmHJAZMANgAslmvO1II4ge5RTmRwmWk6vxCAYk1YzR8Rgoe8Y-9ePOJeEt5dBjhavQTX-Ymf73cZ6FICwMgYas8IGD8whEBjc4IN2YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم دودش ولی احتمالا بخار مال خشکشویی عمو خشکخشکیاهو است
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21354" target="_blank">📅 23:12 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21353">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گزارش های زیاد از انفجار در تهران سمت انقلاب فعلا میترسم یهو میگن جشن امام ۱۸ ام بوده
😂
فقط بدونید
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21353" target="_blank">📅 23:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21351">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">موشک های کروز ضد کشتی به سمت کشتی های بدون مجوز در تنگه هرمز شلیک شده @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21351" target="_blank">📅 23:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21350">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">محسن کج بند رضایی : ما با عمان روی مسیر تنگۀ هرمز توافق کردیم که یک مسیر میانی است اما این موضوع روی کاغذ است و تنگۀ هرمز زمانی باز می‌شود که آمریکایی‌ها به تعهداتشان عمل کنند
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21350" target="_blank">📅 23:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21349">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21349" target="_blank">📅 23:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21348">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گزارش های زیاد از صدای تیر اندازی در شهر اندیشه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21348" target="_blank">📅 22:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21347">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">محسن کج بند رضایی: در صورت ادامه محاصره اقتصادی شرکت های اقتصادی آمریکا را در منطقه خواهیم زد
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21347" target="_blank">📅 22:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21346">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وزیر اقتصاد جمهوری اسلامی : احتمال انحلال چندین بانک در ایران وجود دارد
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21346" target="_blank">📅 22:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21345">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آغاز موج جدید سنگین حملات هوایی اسرائیل به جنوب لبنان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21345" target="_blank">📅 22:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21344">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گزارش های بسیار از صدای انفجار مهیب از تنگه  @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21344" target="_blank">📅 22:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21343">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اورشلیم پست گزارش داده است که اسکات بسنت، وزیر خزانه‌داری آمریکا، قرار است روز دوشنبه ۲۴ اوت در یک نشست خبری جزئیات برنامه جدید دولت ترامپ برای تشدید فشار اقتصادی بر ایران را اعلام کند. این نشست ساعت ۲ بعدازظهر به وقت شرق آمریکا برگزار می‌شود که با توجه به…</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21343" target="_blank">📅 21:56 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21342">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گزارش های بسیار از صدای انفجار مهیب از تنگه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21342" target="_blank">📅 21:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21341">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کانال 14 : تهران آماده است تا فهرست اهداف خود را گسترش داده و شبکه‌ها و تأسیسات انرژی منطقه‌ای را فراتر از مرزهای دریایی تنگه هرمز هدف قرار دهد
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21341" target="_blank">📅 21:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21340">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نتانیاهو: تا زمانی که من نخست‌وزیر هستم اجازه نمی‌دهم هیچ کشور فلسطینی تحت کنترل ایران تشکیل شود
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21340" target="_blank">📅 21:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21339">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QELs6r6F5lqkHZ5mc0egM_Yn1g9HQ3Hv0uacCGABKFfleQUreCaXNNdDK-UDMgkFcObOui_KIGey_ohNyhHdtncgpaQCPlIe7X1gHJNXe-XQro6LewpGXaKsu6mTyAajLGVqCw-215jAeT3M8ddVVE5YBVX7feQRx7OIF7VvoT7nwESWYFvNXRSi8u2T41wn4Uh5HrHxwdjFXmgXisqWp0qlqaon6h7PyvEiPycj4E9njHuL_IHQcRdskv8i5LnR8UUb-Jd6_2991J76HFGCeOXOVc9-4MDyo1LxKBdZDf6Q_l6aIbQPm_eSW-DYHkv2-MwYwJD812P8debeBzh1ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل
یک فرمانده گروهان را که حملات تروریستی را هدایت می‌کرد و در تلاش‌ها برای بازسازی زیرساخت‌های زیرزمینی حماس شرکت داشت، از بین برد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21339" target="_blank">📅 20:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21338">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">جروزالم پست در یک یادداشت دیدگاه هشدار داده است که اسرائیل باید گسترش نظامی ترکیه در سوریه و شرق مدیترانه را یک تهدید راهبردی جدی تلقی کند. نویسنده با اشاره به حمله اخیر اسرائیل به پایگاهی نزدیک ادلب، مدعی است
ترکیه در حال ایجاد سامانه راداری و پدافندی در آن منطقه بوده است
. او با استناد به هشدارهای کمیسیون ناگل، حتی احتمال تبدیل‌شدن تهدید ترکیه و سوریه به خطری بزرگ‌تر از ایران را مطرح می‌کند و خواستار تقویت نیروی دریایی اسرائیل و تعیین خطوط قرمز برای آنکارا شده است. در پایان نیز با لحنی بسیار تند می‌نویسد:
«از ادلب تا استانبول، اسرائیل در صورت لزوم حمله خواهد کرد، نه دفاع.»
این موضع، دیدگاه نویسنده مقاله است و اعلام رسمی دولت یا ارتش اسرائیل نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21338" target="_blank">📅 19:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21337">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeWRwCI__9ijb4gNHPNgOf_Z5ZvRVvFbZ3J4B1YmIqOJ_EcKAZTrf07xxliBmAwvK125EOuaTlURHgV-sjtC7wSQCUqAf3m6eNfk7PpXBpuZSfDsrwCAl57x0-gxH6k28QuKpDnJbtTCwpT3vY5AV7wqmwNwx5pWEFhbuSYfm2g9Jm7OIc4_akghYz42vlVPcICZGC3egZ16femLz7yUJV3FuKK9IlLEO0z0SZfpsOjv4P81Mu0VQk71UTcMhvPit0Mt8Cm6f7EHvvbKMaD3Ci8nPZzevOehTeGvuKuTu_gy05_hclGF_iuLk3tzh8NaASRdsJRds2OmDPzrsGZNyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورشلیم پست گزارش داده است که
اسکات بسنت، وزیر خزانه‌داری آمریکا، قرار است روز دوشنبه ۲۴ اوت در یک نشست خبری جزئیات برنامه جدید دولت ترامپ برای تشدید فشار اقتصادی بر ایران را اعلام کند
. این نشست ساعت ۲ بعدازظهر به وقت شرق آمریکا برگزار می‌شود که با توجه به اختلاف زمانی فعلی
، برابر با ۹:۳۰ شب دوشنبه به وقت تهران است.
بسنت پیش‌تر صراحتاً گفت:
«ما این رژیم را فرو خواهیم ریخت.»
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21337" target="_blank">📅 19:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21336">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اکسیوس به نقل از مقامات آمریکایی: حدود 40 تانکر نفت شب جمعه از تنگه هرمز، به سمت مسیر عمان و مسیر آمریکایی، عبور کردند. این میزان معادل حدود 16 میلیون بشکه نفت است. @WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21336" target="_blank">📅 18:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21335">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یاشار : کتاب اوستا ، یسنا ۴۳.۱ آمده: «اُشتا اَهمایی یَهمایی اُشتا کَهمایچیت»  «خوشبختی نصیب کسی می‌شود که برای دیگران خوشبختی بخواهد.»  @WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21335" target="_blank">📅 18:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21334">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89d69f232e.mp4?token=oeXpTSOCpwBXM0lQsSy5pFKX9iFSqpr7Sf89apSL5j0mM7chcJaqXr-ec-wNWptsKUhJ2zffVxEkrVWm9OtWCFX1lznBVXh762kgF8V9Qo5b4oc7t_lysbLt0FZsW-Z7-UQvKlEJo4ztP5OjXfOhhaUBTZAZ7TBz_OB3a8lO4FvGXbpNWATfMqn6qkcaKHmlSPrczeL2f4Vmn2PPyL7-EoCOT-r7ghPILKjDgXrqeA1zH4ZFIQGkRdCZ-lr3SpPjPd4WBbH7MFLxG5-ONxG-R83Xy8kuxw5nStskGQ_sA02dCD3dZD9C_yzn4HDyM9PhoUrfZgOhTPKyf_Z-4gf1mw7UG3Qa4WBqL5Jyh9SjhFMA-nKcSbnACEPqXVfnrf9cARg4xtX7svGDZGlSvBEX57MoEIob88XeQVDVPTdxoA4BGaiN1U0fwLCAN-Sjx1P31902qiqKLnFPqIiEr3FHnx5pEK85Za4Q5yUFctwLZzDG6lNxisbuRlRzOdxTKm_svDeaZND2qFgxfuzZ7-J50SbzZ2Zaet5Zm_ZSWtrHJpzYiPvlT9Hj7hU29PWQXSl5bp8EeB-Fau_sy2j27Xo5o5owvjwEY1rmYM6Jvf-NbmbUsha4NUOf8lw_n9SeYD2YTxHViYaomy7Hdpcw8Onj--dUWJrDdZxL5cFywn2IsLk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89d69f232e.mp4?token=oeXpTSOCpwBXM0lQsSy5pFKX9iFSqpr7Sf89apSL5j0mM7chcJaqXr-ec-wNWptsKUhJ2zffVxEkrVWm9OtWCFX1lznBVXh762kgF8V9Qo5b4oc7t_lysbLt0FZsW-Z7-UQvKlEJo4ztP5OjXfOhhaUBTZAZ7TBz_OB3a8lO4FvGXbpNWATfMqn6qkcaKHmlSPrczeL2f4Vmn2PPyL7-EoCOT-r7ghPILKjDgXrqeA1zH4ZFIQGkRdCZ-lr3SpPjPd4WBbH7MFLxG5-ONxG-R83Xy8kuxw5nStskGQ_sA02dCD3dZD9C_yzn4HDyM9PhoUrfZgOhTPKyf_Z-4gf1mw7UG3Qa4WBqL5Jyh9SjhFMA-nKcSbnACEPqXVfnrf9cARg4xtX7svGDZGlSvBEX57MoEIob88XeQVDVPTdxoA4BGaiN1U0fwLCAN-Sjx1P31902qiqKLnFPqIiEr3FHnx5pEK85Za4Q5yUFctwLZzDG6lNxisbuRlRzOdxTKm_svDeaZND2qFgxfuzZ7-J50SbzZ2Zaet5Zm_ZSWtrHJpzYiPvlT9Hj7hU29PWQXSl5bp8EeB-Fau_sy2j27Xo5o5owvjwEY1rmYM6Jvf-NbmbUsha4NUOf8lw_n9SeYD2YTxHViYaomy7Hdpcw8Onj--dUWJrDdZxL5cFywn2IsLk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به فاکس‌نیوز : ایران در حال تغییر موضع است، در حالی که دولت او خود را برای اعمال موج جدیدی از فشارهای اقتصادی بر تهران آماده می‌کند.
آنها اکنون در حال تغییر موضع هستند، زیرا وقتی کشوری دیگر نیروی دریایی و هوایی ندارد، حرف چندانی برای گفتن ندارد.» او افزود که «نمی‌دانم اصلاً با چه کسی باید مذاکره کنم.»
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21334" target="_blank">📅 17:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21333">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اکسیوس به نقل از مقامات آمریکایی:
حدود 40 تانکر نفت شب جمعه از تنگه هرمز، به سمت مسیر عمان و مسیر آمریکایی، عبور کردند. این میزان معادل حدود 16 میلیون بشکه نفت است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21333" target="_blank">📅 17:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21332">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">روزنامه معاریو: آلون بن داوید، خبرنگار مسائل نظامی این روزنامه، مدعی است که مقامات ارشد ارتش دفاعی اسرائیل  معتقدند که نخست‌وزیر نتانیاهو در تلاش است تا تنش‌ها را در غزه افزایش دهد تا انتخابات اکتبر را به تعویق بیندازد.مقامات ارتش اسرائیل گفته‌اند که نمی‌خواهند وارد یک جنگ جدید و غیرضروری شوند
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21332" target="_blank">📅 16:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21331">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzIo-hztrCjN9kh2tsuhlvDT4NtxyZEWzkxP7vT5A4AFQBYg00ktfjURGWH1FjJqlC1qxE-wgxxgVMRDNljHfYpiH8NkZWb-G_lMpgjGdQ6jb7jEBEFBPALCS61hmQgbW1OnSLNbggZx3ViEkP-DN0ugVkcg-8iWWCDzdwo0EtJIbkdoTJ-yOZzlMu4WZGEF77Um5I5vQWP_Z3rBiwBpG6LtXCqKMgNQKzJrYh6eWLZtiVAl_uoXU6ZS3YvqxA96qFQnYLc7huRFlrIOFBDdicSjQlfyFfKlx5zFqnp_u3xSDDNZdl49gpA8CqxDwURdKtLEE0mA07kf9n0oIF_2AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز صبح انتقال سه تانک از کمربندی یزد بسمت جنوب کشور
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/21331" target="_blank">📅 12:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21330">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رویترز : آمریکا روز دوشنبه تحریم‌های اقتصادی جدیدی علیه ایران اعلام می‌کند که احتمالاً خریداران بزرگ نفت ایران، از جمله شرکت‌های چینی، را نیز هدف قرار خواهد داد
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21330" target="_blank">📅 12:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21329">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLlTupcNShr4LmHD2z9MOwXyOsrjRXzkpmiLwt3U_Cw2QTy5_G9C8xidukg_SZJ9hAJomcQK44PXIcAXx3bamAl1liHOQdZIg8Zf_XzNUcnUeywdfAY9dmRjhxKL2EFaphGSrQGwevNeQhm3OOd-yPK7zEU6OCxND8tEAvXG9GnUiJq094O4Zwl2ID7YPu5HSNp3LnpkzrqXXhOUvsu2pUyzv16q73feKFmQdblH3dOSRBbuTiNJTVPDAgcTOshgjR3EPjNNkOuZjsTGLFPtaKnkX2KRotgl9UScNo-Bl8TGwHfKhqMsi6UszKNPZxFYi3TwoMGcijp1SJd8CsE7Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">lكارنامه شاهزاده رضا پهلوی ، كتبى ١٨.٠٤ و معدل شفاهى ١٨.٧٢ ، انضباط ١٨!
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21329" target="_blank">📅 11:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21328">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CITab76TpFQ8XvGI4Jl5sICAYXU78tKHkWPTl50rmTRd7_oz4nHY7pHCsW5fTNOEo-bUwgiQeFXOzKFKKf8RXjCang6-o6I00hcxbfdcAwxlZADNQHMsl8TOeZOMiFZHJGKpyZrAoeXFLfMbjKAB2VhEPWC7ctzWQ9uiGxIn6TO7l_3mpKs-sJGh1_BJOZMA0Ne9mipKAn-USDDBBFReH4XEvZbxDj49u6CRPXPEqdfOC1BlPwrHeR9EPJyjXBdQt9qeSAH3nvA5nYLmBtm9HJIWFrTjD9ZrBcH8YzAs2QpIvPZi21j98MHhT-xvND91LJHkZyJzivreVmfGgR_Emg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک تانکر نفتی، با نام "ال ماقام"، شب گذشته تحت نظارت هوایی شدید نیروهای آمریکایی با موفقیت از تنگه هرمز عبور کرد، در حالی که سیستم AIS آن غیرفعال بود.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21328" target="_blank">📅 11:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21327">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یاشار : کتاب اوستا ، یسنا ۴۳.۱ آمده:
«اُشتا اَهمایی یَهمایی اُشتا کَهمایچیت»
«خوشبختی نصیب کسی می‌شود که برای دیگران خوشبختی بخواهد.»
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21327" target="_blank">📅 11:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21326">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تابناک : گویا راه حل چهارمی برای بنزین پیدا کردن!
کیفیتو انقدر پایین آوردن که مردم از ترس خراب شدن ماشینشون دیگه بنزین نزنن… دولت با همین ترفند ساده، مصرف رو کنترل کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21326" target="_blank">📅 10:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21325">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مدیرعامل شرکت نفـت ستاره خلیـج فارس استفاده از متانول در ترکیب بنزین این پالایشگاه را تایید کرد.
انجمن خودروسـازان ایران پیش از این در نامه‌ای هشدار داده بود که استفاده از متـانول در بنزین سیستم سوخت رسانی، باک، فیلتر و پمپ بنزین، لوله های فلزی، واشرها و قطعات پلاستیکی را دچار خوردگی شدید می‌کند.
مدیرعامل شرکت نفت ستاره خلیج فارس: استفاده از متانول در سوخت در کشورهایی مانند چین، آمریکا و اروپا تجربه شده و این ترکیب هیچ آسیبی به خودرو وارد نمی‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21325" target="_blank">📅 10:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21324">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آمریکا و کانادا در تلاش خود برای دستیابی به توافق تجاری شکست خوردند و به همین دلیل واشنگتن از صبح امروز، 50 درصد تعرفه بر محصولات کانادایی به ارزش حدود 20 میلیارد دلار اعمال کرد. مارک کارنی، نخست وزیر کانادا، در پاسخ به این اقدام، تعلیق مذاکرات با آمریکا را اعلام کرد و گفت که کشورش به تعرفه‌های جدید «دلار در برابر دلار» پاسخ خواهد داد. این تصمیم پس از سه روز مذاکره متوالی در واشنگتن بین دومینیک لبلانک، وزیر کانادا، و جیمیسون گریر، نماینده تجاری ایالات متحده انجام شد ، تعرفه‌ها بر محصولاتی اعمال خواهد شد که حدود 5 درصد از صادرات کانادا به ایالات متحده را تشکیل می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21324" target="_blank">📅 10:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21323">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پاکستان برای هزینه میانجیگری بین ایران و امریکا ‌۱۰ میلیارد دلار درخواست کرد
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21323" target="_blank">📅 09:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21322">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a8d76ce15.mp4?token=lMKG6PN75AOByJHb5g-zuErzSqxXtPbKWemnl8tss7Zli57PSYS5HACEIHpPg2l-vEDcAtwFVVVBU7KNRlEsrqUxvyS4SXZuK8AmE8qKWRtYtVpL6oBC4R8lQg7UtQ2jIPrQVU3klRLzlUT9-rUQCA5O8Y_1s7ZQsorSNWqAsXX07fQe-TY0Nm3Gi2k_m_C-0Pv0KHWmsfwwCxBXhwYV1pBE-FaVtF0TP3KXe9kgIB4XyJPYchSeNs0QLWJTEHnfMX8YMHIplfbQSita74a5e4knvoBikxFYGX65acFtfKUCCBe8DF7rzuHTuqoB2OWitVcfBgYr7CZ6YJV7F_fBKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a8d76ce15.mp4?token=lMKG6PN75AOByJHb5g-zuErzSqxXtPbKWemnl8tss7Zli57PSYS5HACEIHpPg2l-vEDcAtwFVVVBU7KNRlEsrqUxvyS4SXZuK8AmE8qKWRtYtVpL6oBC4R8lQg7UtQ2jIPrQVU3klRLzlUT9-rUQCA5O8Y_1s7ZQsorSNWqAsXX07fQe-TY0Nm3Gi2k_m_C-0Pv0KHWmsfwwCxBXhwYV1pBE-FaVtF0TP3KXe9kgIB4XyJPYchSeNs0QLWJTEHnfMX8YMHIplfbQSita74a5e4knvoBikxFYGX65acFtfKUCCBe8DF7rzuHTuqoB2OWitVcfBgYr7CZ6YJV7F_fBKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور ترامپ در مورد ایران:
ما مجبور بودیم سلاح هسته‌ای را از ایران بگیریم. ما مجبور بودیم این کار را انجام دهیم.
این باعث افزایش ناگهانی قیمت نفت شد، نه به آن بزرگی که مردم فکر می‌کردند، اما باعث افزایش ناگهانی قیمت نفت شد. قیمت‌ها خیلی زود حتی از قبل هم پایین‌تر خواهند آمد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21322" target="_blank">📅 09:22 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21321">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5a0b2336.mp4?token=IlqNzerPb0U-eg59GGeIcSaCDyJHwt31SkpqoOeCruEj7ubq8ubDMyIZ-ykF6HTW43VDX-qY5l6mYiYEsmVQKwJ1sARsVsFTWHJJB0aR88zQPqAZuX-BNMR4fpLpcjW3xJMmcE9YU7FgzMhEdJWXQAcix7ORmPrxTzwr0mz4TTOFIKJxE_yXpxY-wP5sB2jh0Qh64FUbohAHoreBsBz9TJ6X1xg41qKZ8bIx4hC0I_NiDLvr_9tEXjo62x1z9Oku9ocwnaNi9m3jF9BV1qfsvqJ0Si4iEOca4aassxPBXIdBdin0L8OuC3LTpQogDBo7fqz6esvmEKcsSD_Whg54gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5a0b2336.mp4?token=IlqNzerPb0U-eg59GGeIcSaCDyJHwt31SkpqoOeCruEj7ubq8ubDMyIZ-ykF6HTW43VDX-qY5l6mYiYEsmVQKwJ1sARsVsFTWHJJB0aR88zQPqAZuX-BNMR4fpLpcjW3xJMmcE9YU7FgzMhEdJWXQAcix7ORmPrxTzwr0mz4TTOFIKJxE_yXpxY-wP5sB2jh0Qh64FUbohAHoreBsBz9TJ6X1xg41qKZ8bIx4hC0I_NiDLvr_9tEXjo62x1z9Oku9ocwnaNi9m3jF9BV1qfsvqJ0Si4iEOca4aassxPBXIdBdin0L8OuC3LTpQogDBo7fqz6esvmEKcsSD_Whg54gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: الان میگین چه غلطی باید بکنم؟
برگردم، کمی بیشتر ایران را بمباران کنم؟
جمعیت : آررررررررره
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21321" target="_blank">📅 03:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21320">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e05213aef.mp4?token=G2rOM1UtKNK6ckM4UHOmlOUle4Bn5mV5pIQi0yH0rd9G43846XUnTkMDAvmwlhcVpCU9KJOygo24LQQHu3Fewt9I0o7x45q9bhww-HOFQzBp6gC9CfrvuEesG8-8SGVDmIUhTdTtezpuOTxBd-7VA_CI6HuoG8QV3i9RDh-IJWpwuWn-9Pyy5os7wS1kQq0DUh_Av1sLvQlWv-VpVFPfjoWbVHxR-XFxd9PIlpVpX2SU2NwQoLluCfTSr8iwkDd5wlu0WHy-h3SR5hS_7A0R7Zd2PR8R9AlDnHcmWo7-CFZAIEiPPFyeuVti7rw9SFAIJ_BEBwS3hwrH1Dvu8ClPxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e05213aef.mp4?token=G2rOM1UtKNK6ckM4UHOmlOUle4Bn5mV5pIQi0yH0rd9G43846XUnTkMDAvmwlhcVpCU9KJOygo24LQQHu3Fewt9I0o7x45q9bhww-HOFQzBp6gC9CfrvuEesG8-8SGVDmIUhTdTtezpuOTxBd-7VA_CI6HuoG8QV3i9RDh-IJWpwuWn-9Pyy5os7wS1kQq0DUh_Av1sLvQlWv-VpVFPfjoWbVHxR-XFxd9PIlpVpX2SU2NwQoLluCfTSr8iwkDd5wlu0WHy-h3SR5hS_7A0R7Zd2PR8R9AlDnHcmWo7-CFZAIEiPPFyeuVti7rw9SFAIJ_BEBwS3hwrH1Dvu8ClPxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن بمب‌افکن‌های B-2 یک سال پیش به امید ایران برای دستیابی به سلاح هسته‌ای پایان دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21320" target="_blank">📅 03:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21319">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33aa06c32.mp4?token=JNOWwvc3y9uMDULnOCsEMmVxiK270Tw5lFWEXWWL_KF5njqGO5HzFO06Hp6-OG3-7Sswh2Mf2SaIjL1XSdJe9N8cw0mq2R1qotZXnVz7pw0dddQTdKupPtMFSMB0QbTdnTBsBNC1AwokGGE94thQg7RT-DypNN0ZidoncskcOcjtawGSbiPOYA2YXmiWaMzqEb5XmTxOIrG72tfA1xq4S1ici6tP9wBpuVk6wR-HkQeD2nIFgxkxU3X8_Q0un9VVg3WOza-t3QZRGJRo2beMqeNm4DQj2kAQo3ZRgryzk2lis2pdjH4jdGSUd_Fh60CQ-fB8aVvKSBIWC2bR-hU2Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33aa06c32.mp4?token=JNOWwvc3y9uMDULnOCsEMmVxiK270Tw5lFWEXWWL_KF5njqGO5HzFO06Hp6-OG3-7Sswh2Mf2SaIjL1XSdJe9N8cw0mq2R1qotZXnVz7pw0dddQTdKupPtMFSMB0QbTdnTBsBNC1AwokGGE94thQg7RT-DypNN0ZidoncskcOcjtawGSbiPOYA2YXmiWaMzqEb5XmTxOIrG72tfA1xq4S1ici6tP9wBpuVk6wR-HkQeD2nIFgxkxU3X8_Q0un9VVg3WOza-t3QZRGJRo2beMqeNm4DQj2kAQo3ZRgryzk2lis2pdjH4jdGSUd_Fh60CQ-fB8aVvKSBIWC2bR-hU2Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اگر من در انتخابات میان دوره ای شکست بخوریم، استیضاح می شوم.
قرار است من را استیضاح کنند. آنها خودشان هم نمیدانند چرا.‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21319" target="_blank">📅 03:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21318">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5060626161.mp4?token=YgZp0F6UJfl7bRaj8-xvrjUtqnBpfFhlQkjdQ7GM5YbOLsdJ-mhxxN51xdgG-FVXyIijb1Qj40f-xAOmiGf1ioX4A6RRuIaMPFFu98s49kkkoGXNVvRs8CdQni8qNSuoM6qL3VhSQ1KhLEyLrz598PHVMLndXsvJkv51rYERtlAiozi33Q-4fcXgqmleKWOPG11aVxM94JzlmExArOG7fCUTk2UCD5E5jiD9Y_gSs-3fnmvtw_hGnXoUnmuGdIN4jNXUASmHcPtQqE7zzM3aAzEuZmOwGidP_DBey1FF6gy03MLeCytRBMpcqTsv8zeyvCwFIrlJWOhVBBlF40jOBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5060626161.mp4?token=YgZp0F6UJfl7bRaj8-xvrjUtqnBpfFhlQkjdQ7GM5YbOLsdJ-mhxxN51xdgG-FVXyIijb1Qj40f-xAOmiGf1ioX4A6RRuIaMPFFu98s49kkkoGXNVvRs8CdQni8qNSuoM6qL3VhSQ1KhLEyLrz598PHVMLndXsvJkv51rYERtlAiozi33Q-4fcXgqmleKWOPG11aVxM94JzlmExArOG7fCUTk2UCD5E5jiD9Y_gSs-3fnmvtw_hGnXoUnmuGdIN4jNXUASmHcPtQqE7zzM3aAzEuZmOwGidP_DBey1FF6gy03MLeCytRBMpcqTsv8zeyvCwFIrlJWOhVBBlF40jOBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
این در واقع یکی از بزرگترین مشکلات من است: نمی دانم با چه کسی در ایران برخورد کنم.
این تنها کشوری در جهان است که هیچ کس نمی خواهد رئیس جمهور شود.
آنها می گویند: "چه کسی می خواهد رئیس جمهور شود؟" نه، نه، من نمی خواهم رئیس جمهور شوم.»‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21318" target="_blank">📅 03:14 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21317">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">این خواهر پژی جمشیدی چه بی لولیه بی حیا دو زاری ، من ۹۹٪ فوتبالیستایی که دیدم دوزاری بودن ! این جماعت چرا اینجورین !</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21317" target="_blank">📅 03:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21316">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سنت‌کام : نیروهای ایالات متحده از زمان تقویت محاصره بنادر ایران، ۶۷ کشتی تجاری را تغییر مسیر داده‌اند، ۳ کشتی را غیرفعال کرده‌اند و ۲ کشتی را برای اطمینان از رعایت مقررات به بازجویی و بازرسی برده‌اند. @WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21316" target="_blank">📅 02:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21315">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تکزاس زیر 1942 و Azul قبول نیستاااا</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21315" target="_blank">📅 02:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21314">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromJoshua Milani</strong></div>
<div class="tg-text">داش یاشار از کف تکزاس با تکیلااااا جات خالی</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21314" target="_blank">📅 02:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21313">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxGNDDwhYwGrSOgJoJ4SOLowmfcEkgV8sJHYGQzTSfSPqz3pYk4ExtLigt48OeKXM74AYMtmeH7KpyeZi-10jxJkBL_wNnL4YwORdLuIe7xIoQsPyg_2MLv8tWV18CX4sQ5duC9wb5AeA8J03OuCRvPgHijcAwxfpa1FhGNzmMBg0FhmD3JCe7B73moOxZwsovYBcTuwbGlUI2cvisYmsw-WvkR2nu-QDeZNhBs-ZSv3PA1nyBUFqupYkaEfMJN2dHF87zroyzKDjXq5E0vPDIK1LAgOI8ZMKpEhGuxZAp3VYpewyTljSbm9I59fNJ0OIz703T3opnGx7tWoHUbO4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگه شلوغ شد
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21313" target="_blank">📅 02:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21312">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">جنگی
⚔️
⚔️
⚔️</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21312" target="_blank">📅 02:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21311">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBaba barghi</strong></div>
<div class="tg-text">اقا یاشار گل مرد مردا
مارو از جنی واکرا بینصیب نکن مشتی
کاکو شیراز یه لشکری هوادارتن
🫡
🫡
🫡</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21311" target="_blank">📅 02:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21310">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from؛)</strong></div>
<div class="tg-text">یاشار ماهم داریم راکی میخوریم از غرب تهران مستیم مستت
🥃</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21310" target="_blank">📅 02:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21309">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اتاق جنگ با یاشار : اول از همه باید به تغییر رژیم در افکار بوجود بیاد ، بعد اینام میرن ..</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21309" target="_blank">📅 01:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21308">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21308" target="_blank">📅 01:52 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21307">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">۲ ساعت دیگه میرم بالای منبر اگه بیدارین
😎</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21307" target="_blank">📅 00:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21306">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkBwR7q7nS20drqqzkrGPTnDR0lLOpWMUwJoiMcOlTBq-F3MzlFHkuhj3Tko6o7sJyveyu1F3kccKHiWeFoi0GGph-URld3kdnZflsZJpHSw9eiWmbpprJCQAzisEpzYswbQyfa4WOH4JlTi94pHHMDkVGqsKwKgnKTv9oJGQJmFkifJ5EHXt79M1ANb8wzdmAgbXzHB8rBsV0sM3cFhPaPVcOPjbX2V3-acD5I6W8PNAuJRMcQauS5umkORnZLcYEvXeB4mWluyK5wwEINbcPwi7WswA1te9vOLKPbGfjMsyllweJ8TVHs0Wz1biEkFBaWlaAjkBe7ddudlFvhOnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقایقی پیش، یک جت جنگنده F-35A Lightning II نیروی هوایی ایالات متحده هنگام فرود اضطراری کد اضطراری ۷۷۰۰  اعلام کرد…
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21306" target="_blank">📅 00:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21305">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6b4cd2471.mp4?token=Qch48caBDDtIAbLJed3sxfzdAnvQdlgBf4eK4W6Jy8ZL6uULqbhDEKrbyc2lOTQJhQpoj_oBOEosXNbIogDCtWL9N4KdSQ0IamqR-mOiRG5xr_a-4GKcD98Dd4r5iFVK_1dOvCKFnHa9Jrr4VCw2MLZ1n5SM2yQIJin0zvwDEPci07XDdgru0PnHX-77IyrNfjHpzO2lsEeXNJ8WITCYPX7PRmmLq6w6nzp0V7Y7truK0iBMS1AvCZsNsodcfmVAhW8PfTBiPo7vNTCTMXfNlFGJYjuwS3HLi_s8BxOme2W0_758GM-6ZROgX2hlzyeV-3kSDDx3rBWobNHkmERc5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6b4cd2471.mp4?token=Qch48caBDDtIAbLJed3sxfzdAnvQdlgBf4eK4W6Jy8ZL6uULqbhDEKrbyc2lOTQJhQpoj_oBOEosXNbIogDCtWL9N4KdSQ0IamqR-mOiRG5xr_a-4GKcD98Dd4r5iFVK_1dOvCKFnHa9Jrr4VCw2MLZ1n5SM2yQIJin0zvwDEPci07XDdgru0PnHX-77IyrNfjHpzO2lsEeXNJ8WITCYPX7PRmmLq6w6nzp0V7Y7truK0iBMS1AvCZsNsodcfmVAhW8PfTBiPo7vNTCTMXfNlFGJYjuwS3HLi_s8BxOme2W0_758GM-6ZROgX2hlzyeV-3kSDDx3rBWobNHkmERc5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: درباره حرکت ایران به سمت
جنگ اقتصادی
؛ آیا این به این معناست که گزینه‌های نظامی آمریکا محدود شده‌اند؟
ترامپ:
نه، به هیچ‌وجه.
ما
کنترل کامل بر تمام آن منطقه مرتبط با تنگه هرمز
داریم؛ و منظورم حتی مناطق خشکی در داخل آن محدوده هم هست.
آن‌ها بسیار مایل‌اند به توافق برسند، اما به نظر من هنوز آماده پذیرش
توافق درست
نیستند.
من فقط توافق‌های خوب (تسلیم کامل )انجام می‌دهم.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21305" target="_blank">📅 00:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21304">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تنگه دعوا شده ، گزارش چند صدای انفجار / شلیک از غرب جاسک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21304" target="_blank">📅 00:18 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21303">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56ecd2c26.mp4?token=rdhMGafiPuiJc8l8NrCXKzUow-NSBDEIrtTqGo4n73gUlzH30E6tFNhalarBSO-f7_K4DA7R-rCk085O8MSXN7lhjuZwotYhVQDn89vw3miTV99x61cDoIjDOQne5YpFpzXuewnTj4zG9VxEhiQL2CSGuAnH5BzpxlTeG3k_xGSqJylCCxt5Ggt85fldWFPl0flF0Vo9ZVtmHQ7zX76a1Ot9ammzNpCvyd0AptYvhRfHACGsspROAoMDj4kM9caYWXVECE8f4DsjGCTctCQMIBJbA89gFQs-RuHsn0g7Kivj3_m1hniFe1MZriNn2eVN-7YskeU6Q8jjmbIMIcwY5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56ecd2c26.mp4?token=rdhMGafiPuiJc8l8NrCXKzUow-NSBDEIrtTqGo4n73gUlzH30E6tFNhalarBSO-f7_K4DA7R-rCk085O8MSXN7lhjuZwotYhVQDn89vw3miTV99x61cDoIjDOQne5YpFpzXuewnTj4zG9VxEhiQL2CSGuAnH5BzpxlTeG3k_xGSqJylCCxt5Ggt85fldWFPl0flF0Vo9ZVtmHQ7zX76a1Ot9ammzNpCvyd0AptYvhRfHACGsspROAoMDj4kM9caYWXVECE8f4DsjGCTctCQMIBJbA89gFQs-RuHsn0g7Kivj3_m1hniFe1MZriNn2eVN-7YskeU6Q8jjmbIMIcwY5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21303" target="_blank">📅 00:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21302">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b84ef4f3f.mp4?token=R9oqXd5A0_h5DkoAf3d9paweK7h4ASAaFrOj9eIkHtnESG5mskPQka1iym0P2sW0g3R5UhpZmfnghubI3bjkAGnYRZN10XehU7U7csEh-_tYFx-WDh-Z3J8DrOFmqONqLOSpCgzC_LKYJCQKVdA9cBYnD1CC47jKXbzpj5rGGZOmCoWZliVCqBGbudOHkeAR164__b_hDW5MKjn0F8Tg08E3rNan_8_XcwxTmp0woiMWkjdMNZt6N5jO_Af1iAUGuZEO8iVbokI0nxXxjKL-jb-opV1CKMvpVSCe2kQGoeCjJXl8ycyXyK_Rq087JLlomlZ93cCmNhSLgxaqmjkwnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b84ef4f3f.mp4?token=R9oqXd5A0_h5DkoAf3d9paweK7h4ASAaFrOj9eIkHtnESG5mskPQka1iym0P2sW0g3R5UhpZmfnghubI3bjkAGnYRZN10XehU7U7csEh-_tYFx-WDh-Z3J8DrOFmqONqLOSpCgzC_LKYJCQKVdA9cBYnD1CC47jKXbzpj5rGGZOmCoWZliVCqBGbudOHkeAR164__b_hDW5MKjn0F8Tg08E3rNan_8_XcwxTmp0woiMWkjdMNZt6N5jO_Af1iAUGuZEO8iVbokI0nxXxjKL-jb-opV1CKMvpVSCe2kQGoeCjJXl8ycyXyK_Rq087JLlomlZ93cCmNhSLgxaqmjkwnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده، تصاویری را منتشر کرده است که نشان می‌دهد جنگنده‌های F/A-18E و F/A-18F Super Hornet همچنین E/A18 Growler نیروی دریایی ایالات متحده، که بر روی ناو هواپیمابر کلاس نیمیتز به نام USS George Washington در دریای مکران مستقر هستند، در حال آماده‌سازی برای انجام عملیات‌های شبانه هستند
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21302" target="_blank">📅 00:11 · 31 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
